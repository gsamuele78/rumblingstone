Arco-Post-Hammerfist-P2B-Torneo-DAUTH-DM-MASTER-REFERENCE.md
=============================================================

# Torneo di Dauth — DM Master Reference
## *Arco P2B (livelli 13). Tre giorni. Quattro PG. Una città sotto pressione.*

> **Status:** canone di campagna RumblingStone (2026-05-03). Questo file è la **fonte autoritativa** per la struttura a tre giorni del Torneo, le milestone narrative, le subquest dei PG non-monaco, l'assedio parallelo della città di Dauth e la tabella degli echi a lungo periodo (BG3-style). Tutti gli altri file dell'arco P2B rinviano qui per la cornice; gli statblocks restano nei file dedicati.
>
> **Tono di riferimento:** *Andor* (intrighi burocratici, cellule, lealtà sotto pressione) + *House of David* (leadership prescelta riluttante, profeti ambigui, sacrifici tribali) + *Tolkien* (la natura che muore, ranger nei boschi, comunità sotto assedio). **Mai bianco/nero.** Ogni vittoria costa qualcosa; ogni costo apre una porta.
>
> **Patto di mastering (anti-railroad):** ogni giorno offre **3 milestone fisse** ed **N opportunità libere**. Le milestone scattano col tempo o con le azioni dei PG, mai con un singolo trigger imposto. I PG possono ignorare ogni subquest e il Torneo funziona comunque, ma ogni subquest non risolta diventa un **eco negativo** a Rethmar (vedi §6).

---

## 1. Cast e situazione di partenza

### 1.1 I quattro PG e dove si trovano

| PG | Classe | Posizione iniziale | Obiettivo dichiarato | Dispute interne |
|---|---|---|---|---|
| **Tordek Stonefist** | Dwarf Fighter 4 / Monk 9 | Concorrente registrato del Torneo (l'unico PG nell'arena ufficiale) | Vincere; sbloccare le Otto Porte; portare 150 mercenari a Rethmar | Tradizione monastica vs. dovere di clan |
| **Thorik** | Dwarf Fighter 13 | Capo della delegazione marziale di Hammerfist; ufficialmente "comandante onorario dei 150 mercenari di re Thorek" | Costruire un'alleanza Dauth-Hammerfist per Rethmar; proteggere Tordek | Ordine del re vs. coscienza personale |
| **Hella** | Dream Dwarf Ranger 1 / Druid 12 | Ai margini di Dauth; il bosco sacro locale è in agonia | Capire perché il boschetto muore; pre-tappa per Sacred Forest | Doveri rituali vs. moralità del sacrificio |
| **Artemis** | Human Warlock 13 | A Dauth come spettatore VIP; in attesa di un contatto che lo porti alla Torre Invisibile | Localizzare la Torre Invisibile; non perdere il controllo dell'Anello | Conoscenza vs. servire il Mask cult |

### 1.2 Le 150 lance di Hammerfist (canone)

> **Canon:** 150 mercenari nani inviati da **re Thorek Hammerfist** a Tordek come dono cerimoniale. Sono la "mano amica sentimentale" del re, in onore del sacrificio della battaglia di Hammerfist e dei Custodi Eterni. Comandante onorario nominale: **Thorik**. Comandante operativo: **Capitano Khorn Spada-di-Fuoco** (Fighter 8, leale, taciturno, vedovo).
>
> **Espansione possibile (subquest Thorik):** se Thorik convince il Consiglio di Dauth a contribuire e raduna i veterani delle guarnigioni minori, può portare la forza combinata fino a **~300 lance per Rethmar** (150 nani + 150 volontari di Dauth). Vedi `…SUBQUEST-Thorik.md`.

### 1.3 Il calendario di pressione (3 giorni di Torneo, 1 mondo che si muove)

```
Giorno -3   I PG arrivano a Dauth. Vanguard Red Hand a 6 giorni dalla città.
Giorno -2   Cerimonia di iscrizione. Vanguard a 5 giorni.
Giorno -1   Sera prima: gala di apertura, presentazione concorrenti.
            Vanguard a 4 giorni. Hella nota il bosco morente.
Giorno  1   PRELIMINARI. Tordek combatte 3 match. Vanguard a 3 giorni.
            Visione "Eco delle Fenditure" attivata.
            (vedi `PARTE1-Giorno1-Preliminari.md` per i match)
Giorno  2   SEMIFINALI. "Kethran Mano di Pietra" (Sethrax) si iscrive.
            Vanguard a 2 giorni. Esploratori della Vanguard avvistati a 1 giorno.
Giorno  3   FINALE → INVASIONE MULTIPLA (Tournament + Walls of Dauth).
            Vanguard arriva a porta nord all'alba: Red Hand assalta Dauth
            (vedi `…DAY3-DAUTH-CITY-SIEGE.md`).
            In contemporanea: Vaereth (Githyanki) + Xal'thor (Illithid)
            invadono l'arena.
Giorno  4   Conta dei caduti. Convoglio dei superstiti parte per Rethmar.
            Echi (vedi §6) si attivano.
```

> **Nota DM:** la Vanguard del Red Hand è una **forza distaccata** (~600 effettivi: 1 Wyrmlord minore + cavalleria hobgoblin + ogre + giganti del fuoco minori). NON è l'orda principale di Azarr Kul (quella punta a Rethmar, Clock 9/18 in `state.md`). È un **distaccamento sacrificabile** mandato a colpire Dauth come **diversivo**: bruciare 150 nani prima che raggiungano Rethmar, e seminare paura.

---

## 2. Architettura dei 3 giorni — milestone e fasi

### 2.1 Schema generale

Ogni giorno ha **3 milestone** (momenti narrativi) e **una griglia oraria libera** in mezzo. Le milestone sono **fissate sull'asse del tempo**, non sull'azione dei PG: si verificano comunque, anche se il party è altrove. Il DM le annuncia con un **tag temporale** (alba / mezzogiorno / tramonto / notte) e i PG decidono dove essere.

```
GIORNO N
├── Alba           — Milestone A (cosa si attiva ne mondo)
│   └── Slot libero (subquest, intriga, riposo, indagine)
├── Mezzogiorno    — Milestone B (climax del giorno: match Tordek)
│   └── Slot libero
├── Tramonto       — Milestone C (rivelazione / decisione politica)
│   └── Slot libero
└── Notte          — Sogni, agguati, infiltrazioni (opzionale)
```

### 2.2 Giorno 1 — *"Voci nell'Anfiteatro"*

**Milestone A (Alba):** Cerimonia di apertura nella piazza centrale. Tordek presentato. Cori del pubblico. Visione ad altri PG (descrizione cinematica): un *vecchio narratore* canta la storia di "un'arma astrale caduta dal cielo" — è il primo seme della lore Githyanki dell'Orbe (vedi `OTTO-PORTE-e-ORBE.md` §2.1.1). Nessuno sa ancora cosa significhi.

**Milestone B (Mezzogiorno):** **Round 1, 2, 3 di Tordek** (vedi `PARTE1-Giorno1-Preliminari.md`). Prima apertura della Porta 1 → cutscene "Eco delle Fenditure".

**Milestone C (Tramonto):** **Cena di apertura al Salone della Lega Mercantile.** Tutti e quattro i PG sono invitati come "ospiti d'onore di Hammerfist". È la prima vera **scena Andor**: 4 fazioni di Dauth si manovrano per influenzare il Torneo e (più importante) per decidere chi finanzierà la difesa della città.
- **Lega Mercantile** (lord-mercante Dauthim "Mano-di-Carta"): pragmatico; è disposto a pagare la difesa solo se il Torneo finisce in tempo per non spaventare i caravane.
- **Casa Vargen** (nobiltà militare in declino): vuole gloria; offre uomini, ma chiede che Thorik comandi la difesa SOTTO la sua bandiera.
- **Tempio di Tyr** (alta sacerdotessa Lyala Berthand): teme che Dauth verrà punita per l'arena "barbarica"; vuole bandire le ultime tre Porte come "abomini".
- **"Volti Coperti"** (gilda d'informazione, copertura del Mask cult): *contattano discretamente Artemis*. Hanno informazioni sulla Torre Invisibile in cambio di un pegno.

**Slot liberi del giorno:** vedi sezione 3 per le subquest di Thorik / Hella / Artemis.

**Notte 1 (opzionale):** *sogno condiviso*. Ogni PG riceve una scena onirica di **tono diverso**:
- Tordek: il monaco-fantasma di un cavaliere Githyanki gli dice "Hai aperto la prima porta. Sei un nostro nipote, anche se non lo sai."
- Thorik: re Thorek invecchiato, su un trono di ferro fuso, gli dice "Le 150 lance non sono un dono. Sono un test."
- Hella: una radice cresce attraverso la sua mano e canta in una lingua antica che lei non ricorda di aver mai imparato.
- Artemis: una maschera d'argento gli sussurra "Tu mi servirai meglio se non ti accorgerai di servirmi."

### 2.3 Giorno 2 — *"Ombre nell'Arena"*

**Milestone A (Alba):** Iscrizione tardiva. **"Kethran Mano di Pietra"** (= Sethrax il Velato) entra nel bracket (vedi `PARTE2-Giorno2-Semifinali.md`). Indizi distribuiti durante la giornata.

**Milestone B (Mezzogiorno):** **Round 4 e 5 di Tordek** (semifinali). Prima sperimentazione della Porta 3.

**Milestone C (Tramonto):** **Consiglio di Crisi.** Esploratori avvistano la Vanguard del Red Hand a 1 giorno da Dauth. L'arcimago di città convoca: Lega Mercantile, Casa Vargen, Tempio di Tyr, Hammerfist (Thorik), e — per cortesia — il Campione del Torneo (Tordek o un suo emissario). Decisione collettiva su:
1. Chi comanda la difesa? (Thorik / Vargen / Lyala Berthand)
2. Si chiude l'arena al pubblico per il Giorno 3? (rischio: panico immediato in città)
3. Si manda un messaggero a Rethmar per chiedere rinforzi reciproci? (probabile: rifiutato — Rethmar non ha uomini da prestare)

**Slot liberi del giorno:** completamento delle subquest del Giorno 1; nuovi hook da Volti Coperti per Artemis; il bosco sacro di Hella richiede la decisione difficile (vedi §3.2).

**Notte 2 (opzionale):** **agguato notturno.** Un gruppetto di hobgoblin esploratori (CR 4–6) entra in città per piazzare segnali fumogeni che guideranno l'attacco dell'alba. Se i PG sventano l'agguato → +2 al morale dei difensori al Giorno 3 (regola di drammatica di tavolo: i giocatori possono ritentare 1 TS fallito durante l'assedio).

### 2.4 Giorno 3 — *"Il Cielo si Apre"*

**Milestone A (Alba):** **L'assalto inizia.** Suono delle campane. La Vanguard del Red Hand attacca la Porta Nord di Dauth. **Vedi `…DAY3-DAUTH-CITY-SIEGE.md`** per stat block, mappa e fasi.

**Milestone B (Mezzogiorno):** **Round 6 di Tordek — finale vs Grandmaster Rihan.** L'arena è isolata per protezione (in teoria). Vedi `PARTE3-Giorno3-Finale-e-Invasione.md`.

**Milestone C (pomeriggio, sovrapposto):** **Doppio cataclisma.** Round 7: portale di Xal'thor + smascheramento di Sethrax + arrivo di Vaereth su draghi rossi. **In contemporanea:** la Porta Nord di Dauth cede o regge; il Wyrmlord Red Hand sfonda o cade. Se i PG si erano divisi (Tordek in arena + Thorik alle mura), questo è il momento del **doppio climax**.

**Notte 3:** epilogo. Conta dei caduti. Veglia funebre (se molti morti). Decisioni finali sui prigionieri (Sethrax catturato? Wyrmlord vivo?). Convoglio per Rethmar parte all'alba del Giorno 4.

---

## 3. Le tre subquest parallele (PG non-monaco)

> **Per i dettagli giocabili (NPC, prove, ricompense, biforcazioni) vedi i tre file dedicati:**
> - `Arco-Post-Hammerfist-P2B-Torneo-DAUTH-SUBQUEST-Thorik.md` — *Andor*: politica e milizia
> - `Arco-Post-Hammerfist-P2B-Torneo-DAUTH-SUBQUEST-Hella.md` — *Tolkien*: il bosco morente
> - `Arco-Post-Hammerfist-P2B-Torneo-DAUTH-SUBQUEST-Artemis.md` — *House of David*: il profeta mascherato

### 3.1 Thorik — *"Le Centocinquanta Lance"* (politica + milizia)
**Tono:** *Andor*, season 1. Burocrazia. Cellule di simpatizzanti del Red Hand nella milizia di Dauth. Un sergente che è un brav'uomo ma dà informazioni al nemico per salvare sua sorella prigioniera. Thorik deve scegliere se denunciarlo, ricattarlo o coprirlo.
**Asse della scelta:** legge vs. compassione vs. utilità.
**Eco:** influenza il numero di volontari Dauth a Rethmar (0 / 75 / 150) e determina se Conte Valerius (Arco 09) avrà un alleato politico in più o un nemico.

### 3.2 Hella — *"Il Boschetto che Muore"* (druidico)
**Tono:** *Tolkien* (Mirkwood). Una ranger elfica solitaria, Sylith, custodisce un piccolo boschetto sacro alle porte di Dauth. Le radici stanno marcendo: un'aberrazione fungale (**Mother of Fungi spore**, eco di P2 Rhest) è stata interrata sotto il bosco. Per purificarlo, serve un sacrificio: o un fey legato (uno dei pochi sopravvissuti del boschetto) o 12 esploratori hobgoblin che si avvicinano.
**Asse della scelta:** quale vita pesa di più; sacrificare un alleato per salvare il bosco, o lasciare il bosco morire per non commettere ingiustizia.
**Eco:** se il bosco vive → druid circle reinforcements alleati a Rethmar Phase 1; se muore → la Mother of Fungi avanza il suo clock di 1 a Cannath Vale.

### 3.3 Artemis — *"Il Profeta Mascherato"* (cult + planare)
**Tono:** *House of David*. Un emissario dei "Volti Coperti" (copertura urbana del Mask cult) offre ad Artemis la posizione esatta della Torre Invisibile e una mappa parziale del Livello 3 — in cambio, deve consegnare al cult un oggetto che troverà DENTRO la Torre. L'emissario ha l'aria di un profeta: parla in metafore, ammette di mentire, ammette di voler usare Artemis. Saul-davanti-a-Samuele.
**Asse della scelta:** accettare il patto e aprire la Torre più rapidamente, ma con un debito al cult; rifiutare e cercare la Torre alla cieca; uccidere l'emissario e perdere ogni vantaggio ma nessun debito.
**Eco:** influenza la difficoltà del finale di Artemis nella Torre Invisibile (P2A) e attiva o disattiva una sotto-trama Mask cult al Rethmar.

---

## 4. Roster combattenti del Torneo (selezione DM-friendly)

> Stat block completi: `Arco-Post-Hammerfist-P2B-Torneo-STATBLOCCHI-COMPLETO.md`.

### 4.1 Combattenti rivali (PNG iconici di Tordek)

| Combattente | CR | Giorno | Ruolo | Stat block |
|---|---|---|---|---|
| Kira | 12 | 1 | Apertura tecnica | Voce 2 |
| Garruk + Thug | 11 | 1 | Test gestione multipli | Voci 7+ |
| Tetsu (versione ridotta) | 11 | 1 | Sparring resistenza | Voce 1 / Vol2 |
| Lady Koryn | 12 | 2 | Esame illusione/inganno | Voce 2 / Vol2 |
| Mistress of Mirrors | 12 | 2 | Esame strategico | Voce 4 / Vol2 |
| Ironclad Bruiser / Thrain | 13 | 2 | Esame fisico | Voce 3 / Vol2 |
| **Kethran "Mano di Pietra"** (= Sethrax mascherato) | 12 | 2 (opz) | Smascheramento covert | Voce 10 |
| Grandmaster Rihan | 14 | 3 | Finale ufficiale | Voce 5 / Vol2 |

### 4.2 Antagonisti del Giorno 3 (selezione mechanically clean)

| Antagonista | CR | Fronte | Stat block | Note |
|---|---|---|---|---|
| **Xal'thor** (Illithid Coordinator) | 14 | Arena (Tournament) | `PNG/Xal_thor/Xal_thor.md` | Vuole i Bracieri di Tordek. Non l'Orbe. |
| **Sethrax il Velato** (Mind Flayer Psion 5) | 12 | Arena (covert) | `PNG/Sethrax_il_Velato/Sethrax.md` | Vuole un "Seme di Porta". Fugge alla Torre. |
| **Vaereth "Lama della Fenditura"** (Githyanki Knight 8/Psy War 4) | ~13 | Arena (Fase 3) | `MINIMAPPA-TIMELINE-ALLEANZE.md` Fase 3 | Vuole l'Orbe (proprietà ancestrale). |
| Dragon rosso giovane-adulto (mount Vaereth) | 15 | Arena | SRD | 1 (o 2 ridotti). Bersaglia Illithidi, non civili. |
| **Wyrmlord Karruk Tagliarossa** (Hobgoblin Cleric 8/Fighter 4) | 12 | Mura di Dauth | `…DAY3-DAUTH-CITY-SIEGE.md` | Boss della Vanguard. |
| Vanguard hobgoblin/ogre/gigante minore | EL 12–14 | Mura di Dauth | `…DAY3-DAUTH-CITY-SIEGE.md` | ~600 effettivi totali. |

### 4.3 Selezione dei round per Tordek (cheat-sheet)

Per il round-by-round, vedi `…CHEAT-SHEET-Round-e-Porte.md`. Schema:

```
Giorno 1: 3 round, Porta 1 disponibile, 1 uso gratuito/incontro
Giorno 2: 2 round (+ opzionale Kethran), Porta 1–2 disponibili, opz. Porta 3 finestra
Giorno 3: 3 round
   - Round 6: vs Rihan, Porta 1–3 disponibili, 1 uso gratuito Porta 3
   - Round 7: portale di Xal'thor + smascheramento Sethrax (Porte 1–3)
   - Round 8+: Xal'thor multifase + Vaereth in Fase 3 (Porte 1–3, opz. Porta 4 sacrificale)
```

---

## 5. Influenza dei PG sulla scena pubblica (mai railroad)

> Regola di tavolo: **ogni PG ha "Voce" pari a 1 + (Carisma mod) + bonus situazionale**. Una Voce è un'azione narrativa significativa che il DM ricorda e che modifica il mondo. Non è una valuta meccanica; è un promemoria per il DM di non ignorare l'agency.

### 5.1 Tordek — *Voce dell'Arena*
- Vincere un match → +1 Voce in piazza (può convocare la folla per intimidire / tranquillizzare).
- Aprire una Porta in pubblico → la sua opinione contribuisce alla riunione di Crisi del Giorno 2 (peso uguale a una fazione).
- Rifiutare una porta in extremis → +2 Voce con Tempio di Tyr.

### 5.2 Thorik — *Voce della Spada*
- Comandante onorario delle 150 lance → in qualunque Consiglio di Dauth ha 1 voto formale.
- Diplomazia con Casa Vargen / Lega Mercantile → modifica i numeri della difesa (vedi `…SUBQUEST-Thorik.md`).
- Personalmente alle mura il Giorno 3 → riduce il CR effettivo del Wyrmlord Karruk di –1 (la sua presenza dà coraggio).

### 5.3 Hella — *Voce del Bosco*
- Salvare il boschetto → un druido del Sacred Forest manda un emissario a Dauth in tempo per il Giorno 3 (1 wild shape extra come ally).
- Sylith la ranger → se Hella la convince, può guidare arcieri dauthim sui bastioni (–1 CR Vanguard).

### 5.4 Artemis — *Voce dell'Ombra*
- I Volti Coperti hanno ovunque informatori → Artemis può "comprare" 1 informazione utile/giorno (costo: 1 promessa).
- Eldritch Blast in pubblico = scandalo. Il Tempio di Tyr ha la scusa per bandirlo dalla città (da gestire).

---

## 6. Echi a lungo periodo (BG3 / R.A. Salvatore-style)

> **Filosofia:** ogni scelta significativa al Torneo lascia un **eco** nella campagna. Gli echi non sono meccanicismi numerici puri: sono **trigger narrativi** che il DM attiva quando arriva il momento giusto (Rethmar, Torre Invisibile, post-campagna). Vedi anche `campaign/state.md` §6 e changelog.
>
> **Per la tabella canonica completa degli echi:** `Arco-Post-Hammerfist-P2B-Torneo-DAUTH-CONSEGUENZE-ECHI-LUNGO-PERIODO.md`.

Sintesi rapida:

| Scelta al Torneo | Eco a Rethmar / Torre / Post-campagna |
|---|---|
| Sethrax catturato vivo | –1 CR Zalkatar in P2A finale |
| Sethrax fugge col seme | +2 CR Zalkatar in P2A finale |
| Tordek apre Porta 4 | Tordek ha 1 ulteriore "Risveglio" disponibile a Rethmar; ma –1 Cos permanente |
| Tordek rifiuta Porta 4 | Rihan diventa allievo-mentore: +1 alleato CR 14 a Rethmar |
| Thorik gestisce bene il sergente traditore | +75–150 volontari di Dauth a Rethmar |
| Hella salva il boschetto | Druid Circle reinforcements arrivano a Phase 1 di Rethmar |
| Hella sacrifica il fey | –1 CR Mother of Fungi a Cannath, ma trauma personale di Hella (–1 Sag temporanea per 30 giorni in-game) |
| Artemis accetta il patto Mask | –1 CR Zalkatar, ma +1 al Clock del Mask cult; cellula attiva a Rethmar |
| Artemis uccide l'emissario Mask | Mask cult si vendica al Giorno X del Rethmar siege con 2 assassini livello 8 |
| 150 mercenari nani arrivano a Rethmar | +1 difesa muraglia fase 1 |
| 150 mercenari **non** arrivano (Tordek squalificato o Khorn morto) | Phase 1 di Rethmar +1 CR effettivo |
| Dauth tiene → 150 volontari Dauth si uniscono a Rethmar | +1 difesa Phase 1 |
| Dauth saccheggiata → ondata di profughi a Rethmar | Phase 0 (Notte dei Drow): più civili da proteggere → +1 a CD difesa temple |

---

## 7. Cosa fare se i PG si dividono (split-party Day 3)

Il **Giorno 3 è un climax a due fronti** e il party probabilmente si dividerà:

- **Tordek + 1 supporto in arena** vs Rihan / Xal'thor / Sethrax / Vaereth.
- **Thorik + 1 supporto alle mura** vs Wyrmlord Karruk + Vanguard.

### 7.1 Regole di tavolo per lo split

- Alterna scene di **5 minuti reali ciascuna** (non round per round). Ogni scena lascia il fronte "in sospeso" su un cliffhanger.
- Se un fronte va male **mentre i PG sono altrove**, applica **conseguenze narrative non meccaniche** (es: "le mura cedono mentre tu scivoli sotto la fenditura psionica"). Mai un gruppo di NPC che muoiono *off-screen* senza che i PG lo capiscano: deve essere visibile.
- Quando i PG vogliono cambiare fronte, **costa 2 round di azione** (Wings of Shadow di Artemis, Abundant Step di Tordek, cavalcatura di Thorik). Nessuno si teletrasporta gratis.

### 7.2 Equilibrio CR per fronte

> Il party diviso a livello 13 (4 PG) ha APL ridotto. Calibra il CR così:

- **Fronte Arena solo (1 PG monaco + 1 sup):** CR effettivo target 13–14. Xal'thor full + Sethrax in fuga + 4 schiavi psionici. Non aggiungere Dorn se Tordek è solo.
- **Fronte Mura solo (1 PG fighter + 1 sup):** CR effettivo target 13. Wyrmlord Karruk + 2 capitani hobgoblin (CR 6 ciascuno) + 4 ondate da 8 hobgoblin (CR 1) ciascuna. Niente giganti.
- **Riunione fronti (round 8+ se i PG si congiungono):** restituisci la difficoltà completa.

---

## 8. Tabella delle decisioni etiche chiave (riassunto-cheat)

> Per ogni momento, l'opzione **GRAY-A** e **GRAY-B** sono entrambe "ragionevoli". Mai presentare una come "moralmente giusta": il DM lascia che siano i PG a definire la propria etica.

| Momento | GRAY-A | GRAY-B | DARK (uso DM con cautela) |
|---|---|---|---|
| Sergente traditore (Thorik) | Denunciare; tradimento punito; sua sorella muore | Coprirlo; difesa di Dauth indebolita ma sua sorella salva | Ricattarlo per usarlo come doppio agente |
| Fey o Hobgoblin (Hella) | Sacrificare il fey; bosco vive; trauma | Sacrificare 12 hobgoblin; bosco vive; chi sono i veri innocenti? | Lasciar morire il bosco; rifiutare entrambi i sacrifici |
| Profeta Mask (Artemis) | Accettare il patto; conoscenza con debito | Rifiutare; nessun debito ma cammino oscuro | Uccidere l'emissario; ferita aperta col cult |
| Porta 4 (Tordek) | Aprirla per salvare il pubblico; –1 Cos perm | Rifiutarla; un civile muore ma Rihan sopravvive con onore | Aprirla in modo egoistico (non per il pubblico, per la vittoria) |
| Comando difesa Dauth | Thorik comanda; Vargen umiliato → +ostile a Rethmar | Vargen comanda; Thorik subordinato → +1 CR difesa Phase 1 | Lyala Berthand (Tyr) comanda → spirito alto, tattica scarsa |

---

## 9. Cross-link ai file dell'arco

- **Statblocchi PNG combattenti e antagonisti:** `Arco-Post-Hammerfist-P2B-Torneo-STATBLOCCHI-COMPLETO.md`
- **Otto Porte e Orbe:** `Arco-Post-Hammerfist-P2B-Torneo-Tordek-OTTO-PORTE-e-ORBE.md`
- **Giorno 1 round-by-round:** `Arco-Post-Hammerfist-P2B-Torneo-Tordek-PARTE1-Giorno1-Preliminari.md`
- **Giorno 2 round-by-round:** `Arco-Post-Hammerfist-P2B-Torneo-Tordek-PARTE2-Giorno2-Semifinali.md`
- **Giorno 3 finale e invasione (arena):** `Arco-Post-Hammerfist-P2B-Torneo-Tordek-PARTE3-Giorno3-Finale-e-Invasione.md`
- **Giorno 3 assedio della città (mura):** `Arco-Post-Hammerfist-P2B-Torneo-DAUTH-DAY3-DAUTH-CITY-SIEGE.md`
- **Subquest Thorik:** `Arco-Post-Hammerfist-P2B-Torneo-DAUTH-SUBQUEST-Thorik.md`
- **Subquest Hella:** `Arco-Post-Hammerfist-P2B-Torneo-DAUTH-SUBQUEST-Hella.md`
- **Subquest Artemis:** `Arco-Post-Hammerfist-P2B-Torneo-DAUTH-SUBQUEST-Artemis.md`
- **Echi a lungo periodo:** `Arco-Post-Hammerfist-P2B-Torneo-DAUTH-CONSEGUENZE-ECHI-LUNGO-PERIODO.md`
- **Mappe e timeline:** `Arco-Post-Hammerfist-P2B-Torneo-MAPPE-COMPLETO*.md`, `…MINIMAPPA-TIMELINE-ALLEANZE.md`
- **PNG covert:** `PNG/Sethrax_il_Velato/Sethrax.md`, `PNG/Xal_thor/Xal_thor.md`
- **Cross-arco con Artemis:** `Arco-Post-Hammerfist-P2A-Torre-PARTE4-FINALE-Boss-Zalkatar.md`
- **Stato campagna:** `campaign/state.md`
