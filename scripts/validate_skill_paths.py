#!/usr/bin/env python3
"""validate_skill_paths.py — catch broken cross-references in skills/.

SKILL.md files reach out to repo-relative paths via patterns like
`../../campaign/state.md` or `references/foo.md`. If the layout changes,
those references silently break.

This validator is **conservative on purpose**: false positives erode trust
in the check. It only flags a path as broken when the path is unambiguously
a file reference (markdown link or fenced inline code) AND it doesn't
resolve under either of two interpretations:

  1. Relative to the source markdown file, OR
  2. Relative to the repo root.

If neither interpretation finds the file, it's broken. If either works,
it's fine.

Patterns recognized:
  [text](path/file.md)              → standard markdown link
  `path/with/slash/file.md`         → inline code with at least one slash
                                       (bare filenames like `SKILL.md` are
                                       skipped — too noisy.)

Skipped:
  http(s):// URLs, mailto:, anchors-only, paths without any slash.
  Glob/template paths containing wildcards or YYYY-MM-DD placeholders.

Exit 0 on clean run, 1 on any genuinely broken link.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SCAN_ROOTS = [REPO / "skills", REPO / "campaign", REPO / "AGENTS.md", REPO / "README.md"]

LINK_RE = re.compile(r"\]\(([^)\s#]+\.(?:md|json|ya?ml))(?:#[^)]*)?\)")
# Inline-code reference: must contain at least one '/' to be considered a path.
INLINE_RE = re.compile(r"`([./A-Za-z0-9_\-]+/[A-Za-z0-9_\-/.]+\.(?:md|json|ya?ml))`")

SKIP_PREFIXES = ("http://", "https://", "mailto:", "#")
TEMPLATE_TOKENS = ("YYYY", "<", ">", "*", "[name", "[id", "...", "[N]", "[X]")


def md_files() -> list[Path]:
    out: list[Path] = []
    for root in SCAN_ROOTS:
        if root.is_file() and root.suffix == ".md":
            out.append(root)
        elif root.is_dir():
            out.extend(sorted(root.rglob("*.md")))
    return out


def is_explicitly_planned(text: str, ref: str) -> bool:
    """If the prose around a ref says 'TBD', 'not yet', or 'planned',
    skip it: that is intentional aspirational reference, not a broken link."""
    idx = text.find(ref)
    if idx < 0:
        return False
    window = text[max(0, idx - 80): idx + len(ref) + 80].lower()
    return any(marker in window for marker in ("tbd", "not yet", "planned"))


def extract_refs(text: str) -> set[str]:
    refs: set[str] = set()
    refs.update(LINK_RE.findall(text))
    refs.update(INLINE_RE.findall(text))
    return {r for r in refs if not r.startswith(SKIP_PREFIXES)
            and not any(t in r for t in TEMPLATE_TOKENS)
            and not is_explicitly_planned(text, r)}


def resolve_any(ref: str, src: Path) -> Path | None:
    """Return a real Path if `ref` resolves either source-relative or repo-relative; else None."""
    candidates = [
        (src.parent / ref).resolve(),
        (REPO / ref).resolve(),
    ]
    for c in candidates:
        if c.exists():
            return c
    return None


def main() -> int:
    broken: list[tuple[Path, str]] = []
    checked = 0

    for md in md_files():
        text = md.read_text(encoding="utf-8")
        for ref in extract_refs(text):
            checked += 1
            if resolve_any(ref, md) is None:
                broken.append((md, ref))

    if broken:
        print(f"BROKEN cross-references ({len(broken)} of {checked} checked):", file=sys.stderr)
        for src, ref in broken:
            try:
                src_rel = src.relative_to(REPO)
            except ValueError:
                src_rel = src
            print(f"  {src_rel}:  '{ref}'", file=sys.stderr)
        return 1

    print(f"OK — {checked} cross-references verified.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
