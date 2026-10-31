# Emerald SW DB build checklist

Status legend: `[x]` done · `[~]` in progress / partial · `[ ]` not started.
Work top to bottom. One chunk = one commit (or a few) + push to `main`. After
each chunk: `python3 tools/build.py && python3 tools/coverage.py` (0 warnings),
tick the box here and add a line to the log at the bottom.

"DRAFT" rows are a complete first pass waiting for the owner's review; a chunk
can be `[x]` with its rows still DRAFT.

## Phase A: foundation

- [x] **A1 Tooling.** `tools/build.py` (mapping + emerald-db → database/, swap_map, auto text drafts, pending art, area progression, timeline), `tools/coverage.py`, wiki copy.
- [x] **A2 Story bible v1.** `bible/STORY.md`: 2 BBY frame, Tatooine start, 14 planets + post-game, factions (Empire = Magma, Hutt Cartel = Aqua), full cast, arena leaders, Four Trials, act summary, creature rules, net-new ideas.

## Phase B: core 1:1 mapping (DRAFT)

- [x] **B1 Creatures.** `mapping/species.csv`: all 386 species with name, basis, planet, concept, habitat notes. Starters WOOKLET / TUSKLING / GUNGLET; legendaries GREATKRAYT / SANDO / EXOGORTH.
- [x] **B2 Characters & organizations.** `mapping/characters.csv`: 59 characters + 25 organizations, with text terms for dialogue.
- [x] **B3 Trainer classes, shards, types, abilities.** 66 classes, 8 badges → kyber shards, PSYCHIC/GHOST → FORCE/SPIRIT, 3 ability renames.
- [x] **B4 Items.** Balls → capture pods, medicine → bacta, key items, held items, berries (B4b).
  - [x] B4b Berries → Star Wars fruit names (meiloorun, jogan, muja, pallie, shuura…), max 14 chars incl. " BERRY" or a new suffix.
- [x] **B5 Moves.** 22 renames (FORCE PUSH, ION CANNON, TURBOLASER, VIBROBLADE…), rest KEEP.
- [x] **B6 Locations.** 213 region-map sections → planet + name; 518 map titles derived.
- [x] **B7 Glossary & net-new seed.** `mapping/glossary.csv`, `mapping/net_new.csv` (planet borders, Boba Fett hunt, droid slicing, Death Star site, new moves).

## Phase C: story and text

- [x] **C1 Timeline.** `mapping/timeline.csv`: rewrite all 45 Emerald timeline events (title, tagline, description, lore, planet).
- [x] **C2 Trainer names.** 755 generic trainers keep Emerald names (CALVIN, JOEY…). Give them Star Wars-style names (max 10 chars), mapped by trainer id in a new `mapping/trainers.csv`.
- [~] **C3 Curated dialogue**, one file per area in `mapping/texts/`, starting with story-critical scripts (cutscenes, leaders, villains, professor), then every NPC. Keep tips-and-tricks NPCs' advice.
  - [x] C3a Tatooine Act 1 (Mos Pelgo → Bestine, Beggar's Canyon). Done: intro speech, Mos Pelgo, Route 101 (`act1_01_mos_pelgo.csv`); Tosche Station, Routes 102–103, Mos Entha town + arena + Lars house (`act1_02_tosche_mos_entha.csv`). Route 104 + Han's pad, Jundland Wastes, Bestine (town, Incom, arena, academy, flats), Route 116, Beggar's Canyon (`act1_03_bestine_jundland.csv`). Next: C3b, Kashyyyk (Dewford, Granite Cave = Shadowlands, Routes 105–109) and Mos Eisley (Slateport, Route 109–110).
  - [ ] C3b Kashyyyk + Mos Eisley (Act 2)
  - [ ] C3c Mos Espa, Sullust, Mustafar, Mos Entha (Act 3)
  - [ ] C3d Endor (Act 4)
  - [ ] C3e Bespin, Jedha, Yavin 4, Hoth (Act 5)
  - [ ] C3f Dagobah, Kamino, Asteroid Field (Act 6)
  - [ ] C3g Ilum (Act 7)
  - [ ] C3h Post-game (Grand Arena, islands)
  - [ ] C3i C-side strings (battle messages, menus, datapad UI, match call)
- [ ] **C4 Datapad entries.** Per creature: category (replaces "Wood Gecko") and a two-line datapad text.
- [~] **C5 Overflow fixes.** Check is now pixel-accurate (see NOTES); about 130 texts flagged. Rewrite every `overflow_risk=yes` text so it fits.

## Phase D: art and world details (names only; drawing is Step 5)

- [ ] **D1 Overworld sprites** (255 `object-gfx:*`) and **trainer pics** (94): Star Wars subject for each (e.g. `object-gfx:youngster` → moisture-farm kid).
- [ ] **D2 Tilesets** (75): planet / biome for each.
- [ ] **D3 Grand Arena** facility trainers (414), Battle Tent trainers, Showcase rivals (96), hideout decorations (120), storylines (22), facilities (7).

## Phase E: review and net-new design

- [ ] **E1 Owner review** of the bible and the DRAFT rows; move reviewed rows to DONE.
- [ ] **E2 Habitat swaps.** Turn `species.habitat_note` into concrete, balance-neutral encounter-slot swaps (`net_new.csv`).
- [ ] **E3 Net-new designs.** For each `IDEA` row in `net_new.csv`: maps, flags, level band, placeholder assets.

## Log

Append one line per working session: date · chunk(s) · commit · notes.

- 2026-10-31 · A1, A2, B1–B3, B4 (no berries), B5–B7 · see git log · first full DRAFT pass; 0 build warnings; 3,351 texts auto-drafted, 449 flagged for overflow.
- 2026-10-31 · C1, B4b · see git log · 45 timeline events DRAFT; 43 berries → `<NAME> FRUIT` (glossary BERRY/BERRIES → FRUIT); fixed auto-draft bug where a term right after `\n`/`\l`/`\p` was skipped (+189 AUTO texts).
- 2026-10-31 · C2 · see git log · 489 rows in `mapping/trainers.csv` (generated DRAFT names, same initial + gender; stormtrooper grunts = TK numbers, cartel grunts = thug names; BRENDAN/MAY → KAEL/MIRA). Owner may want to hand-pick names for prominent trainers.
- 2026-10-31 · C3a (part 1) · see git log · 108 curated texts in `mapping/texts/act1_01_mos_pelgo.csv` (intro, Mos Pelgo, Route 101), all within the overflow limit. Conventions: CREATURES plural, scrub/dunes for tall grass, terminal for PC, chrono for clock, HoloNet for TV.
- 2026-10-31 · C3a (part 2), C5 tooling · see git log · 106 more curated texts (Tosche Station, Routes 102–103, Mos Entha); glossary round 2 (plurals, an ARENA); pixel-based overflow check; `tools/curate_texts.py` helper.
- 2026-10-31 · C3a done · see git log · 218 more curated texts (Bestine, Jundland Wastes, Route 104/116, Beggar's Canyon). Build: a/an article fix, more plural rules, item plurals (-ES). `tools/curate_texts.py` now rebuilds first and supports KEEP_REST_MAPS. Specs that produced each texts CSV are in `mapping/texts/specs/` (re-run them after glossary changes; MISS lines show pairs to update).
