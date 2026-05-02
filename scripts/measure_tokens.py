#!/usr/bin/env python3
"""measure_tokens.py — honest token cost per agent query.

Runs a small set of representative queries against the canonical
`skills/*` source and reports actual token counts for:

  - Loading the entire source (the worst case).
  - Loading only the matching skill's SKILL.md (the routing-only case).
  - Loading SKILL.md + the one reference file the routing table sends you to,
    PLUS any files the skill explicitly requires the agent to load before
    that reference (the realistic case).

Why "required" matters: the rumblingstone-campaign SKILL.md mandates loading
campaign-coherence.md and ../../campaign/state.md before any domain
reference. Counting only SKILL.md + one reference would systematically
under-report campaign queries and inflate the published savings %.

Token estimate: chars / 4. This is the standard Anthropic / OpenAI
approximation for English+code mixed content. Replace with the official
tokenizer of your model for exact numbers; the ratios stay the same.

Usage:
  python3 scripts/measure_tokens.py
  python3 scripts/measure_tokens.py --tokenizer tiktoken    # if installed
  python3 scripts/measure_tokens.py --json                  # machine-readable
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SKILLS_DIR = REPO / "skills"

# Files the skill itself requires loaded before any reference file.
# Source: each skill's SKILL.md "Loading Protocol" / "Critical loading order"
# section. Paths are relative to REPO so they survive skill moves.
SKILL_REQUIRED_PRELOAD = {
    "rumblingstone-campaign": [
        "skills/rumblingstone-campaign/references/campaign-coherence.md",
        "campaign/state.md",
    ],
    # dnd-35-srd and forgotten-realms-lore have no extra preload requirement
    # beyond their SKILL.md. If that changes, add the entry here.
}

# Representative queries — (query_label, target_skill, target_reference_filename)
QUERIES = [
    ("Rules: how does grapple work?",          "dnd-35-srd",           "combat.md"),
    ("Rules: spell DC for fireball?",          "dnd-35-srd",           "spells.md"),
    ("Lore: who is the god of dwarves?",       "forgotten-realms-lore", "fr-deities-complete.md"),
    ("Lore: where is Menzoberranzan?",         "forgotten-realms-lore", "fr-regions-complete.md"),
    ("Campaign: what's Thorik's status?",      "rumblingstone-campaign","campaign-party.md"),
    ("Campaign: current arc state?",           "rumblingstone-campaign","campaign-story-arcs.md"),
    ("Campaign: can artifact X be used again?","rumblingstone-campaign","campaign-coherence.md"),
]


def make_token_counter(name: str):
    if name == "chars/4":
        return lambda text: max(1, len(text) // 4)
    if name == "tiktoken":
        try:
            import tiktoken  # type: ignore
        except ImportError:
            print("tiktoken not installed; falling back to chars/4", file=sys.stderr)
            return lambda text: max(1, len(text) // 4)
        enc = tiktoken.get_encoding("cl100k_base")
        return lambda text: len(enc.encode(text))
    raise ValueError(f"Unknown tokenizer {name}")


def file_tokens(path: Path, count) -> int:
    if not path.is_file():
        return 0
    return count(path.read_text(encoding="utf-8"))


def total_tokens(paths: list[Path], count) -> int:
    return sum(file_tokens(p, count) for p in paths)


def all_md_under(root: Path) -> list[Path]:
    return sorted(root.rglob("*.md"))


def required_preload_paths(skill: str) -> list[Path]:
    return [REPO / rel for rel in SKILL_REQUIRED_PRELOAD.get(skill, [])]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--tokenizer", default="chars/4",
                    choices=["chars/4", "tiktoken"],
                    help="Tokenization method.")
    ap.add_argument("--json", action="store_true", help="Emit JSON instead of a human table.")
    args = ap.parse_args()

    count = make_token_counter(args.tokenizer)

    all_paths = all_md_under(SKILLS_DIR)
    all_load = total_tokens(all_paths, count)

    skill_md_only = {
        skill_dir.name: file_tokens(skill_dir / "SKILL.md", count)
        for skill_dir in sorted(SKILLS_DIR.iterdir())
        if (skill_dir / "SKILL.md").is_file()
    }

    rows = []
    missing: list[str] = []
    for label, skill, ref in QUERIES:
        skill_md = SKILLS_DIR / skill / "SKILL.md"
        ref_md = SKILLS_DIR / skill / "references" / ref
        preload = required_preload_paths(skill)

        row_missing = []
        if not skill_md.is_file():
            row_missing.append(f"skill SKILL.md: {skill_md.relative_to(REPO)}")
        if not ref_md.is_file():
            row_missing.append(f"ref: {ref_md.relative_to(REPO)}")
        for p in preload:
            if not p.is_file():
                row_missing.append(f"required preload: {p.relative_to(REPO)}")

        if row_missing:
            missing.append(f"  - {label}: " + "; ".join(row_missing))
            rows.append({
                "query": label,
                "skill": skill,
                "ref": ref,
                "missing": True,
                "missing_paths": row_missing,
            })
            continue

        # Avoid double-counting if the targeted reference IS one of the preloads.
        load_set = {skill_md, ref_md, *preload}
        targeted = total_tokens(sorted(load_set), count)
        skill_full = total_tokens(all_md_under(SKILLS_DIR / skill), count)
        rows.append({
            "query": label,
            "skill": skill,
            "ref": ref,
            "tokens_skill_md": file_tokens(skill_md, count),
            "tokens_ref": file_tokens(ref_md, count),
            "tokens_required_preload": total_tokens(preload, count),
            "tokens_targeted": targeted,
            "tokens_skill_full": skill_full,
            "tokens_all_skills": all_load,
            "savings_vs_all_pct": round(100 * (1 - targeted / all_load), 1) if all_load else 0,
        })

    if missing:
        print("WARNING: some QUERY entries point at missing files; "
              "they were marked missing rather than counted as zero:",
              file=sys.stderr)
        for m in missing:
            print(m, file=sys.stderr)

    if args.json:
        json.dump({
            "tokenizer": args.tokenizer,
            "all_skills_load_tokens": all_load,
            "per_skill_md_tokens": skill_md_only,
            "skill_required_preload": SKILL_REQUIRED_PRELOAD,
            "queries": rows,
        }, sys.stdout, indent=2, ensure_ascii=False)
        sys.stdout.write("\n")
        return 0

    print(f"\nTokenizer: {args.tokenizer}")
    print(f"Worst case (load every skill md):  {all_load:>7,} tokens")
    print(f"\nPer-skill SKILL.md (routing only):")
    for k, v in skill_md_only.items():
        suffix = ""
        if SKILL_REQUIRED_PRELOAD.get(k):
            preload_tokens = sum(file_tokens(p, count) for p in required_preload_paths(k))
            suffix = f"  (+ {preload_tokens:,} required preload)"
        print(f"  {k:<28} {v:>5,} tokens{suffix}")
    print(f"\nRepresentative queries (SKILL.md + required preload + matching reference):\n")
    print(f"{'Query':<42} {'Targeted':>10} {'Skill Full':>11} {'vs All %':>10}")
    print("-" * 80)
    for r in rows:
        if r.get("missing"):
            print(f"{r['query']:<42} {'MISSING':>10} {'-':>11} {'-':>10}")
        else:
            print(f"{r['query']:<42} {r['tokens_targeted']:>10,} "
                  f"{r['tokens_skill_full']:>11,} {r['savings_vs_all_pct']:>9}%")
    print()
    if missing:
        print(f"NOTE: {len(missing)} query/queries are marked MISSING above. "
              "Fix the QUERIES table or the file paths.")
        print()
    print("Read this honestly:")
    print("  - 'Targeted' = SKILL.md + every file the skill requires you to preload")
    print("                  + the matching reference (deduplicated).")
    print("  - 'Skill Full' = what an agent loads if it grabs the whole matching skill.")
    print("  - 'vs All %' = savings vs loading every md file in skills/ (the dumb case).")
    print("  Campaign queries include campaign-coherence.md and campaign/state.md")
    print("  in 'Targeted' because rumblingstone-campaign/SKILL.md mandates them.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
