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
  - [x] C3b Kashyyyk + Mos Eisley (Act 2): `act2_01_kashyyyk.csv`, `act2_02_mos_eisley.csv` (Spacer Museum re-themed to spacefaring, spaceport + STAR TIDAL starliner, BONGO EXPLORER sub, Jabba's swamp motive), `act2_03_route110.csv` (podrace track, Garindan's Trick House, QUIZ DROIDS).
  - [x] C3c Mos Espa, Sullust, Mustafar (Act 3): `act3_01_mos_espa.csv` (Watto's arena, Wald's bikes, Sabacc Den), `act3_02_anchorhead_routes.csv` (Anchorhead, Routes 111–117, Sandcrawler), `act3_03_sullust_mustafar.csv` (Inyusu Tor, Starfall Cavern, Mustafar Peak, Ashen Pass, Pirin arena). Mos Entha was done in C3a.
  - [x] C3d Endor (Act 4): `act4_01_endor.csv` (Bright Tree Village, Chief Chirpa's arena, Endor Station raided by Bossk, Routes 118–121 and 123; Route 121 pier and Safari gate are shuttle pads to Jedha and Felucia).
  - [x] C3e Bespin, Jedha, Yavin 4, Hoth (Act 5): `act5_01_jedha_fortress.csv` (Jedha Temple, Fortress Vader), `act5_02_cloud_city.csv` (Cloud City, Hutt Hideout, Boba Fett), `act5_03_yavin4_hoth.csv` (Yavin 4 base, Launch Tower raid, Massassi Temple arena of Vos & Aayla, Leia's house, Routes 124–125, Hoth's Wampa Cave).
  - [x] C3f Dagobah, Kamino, Asteroid Field (Act 6): `act6_01_dagobah.csv` (Dagobah, Yoda's arena, Cave of Evil, Drowned Cavern, Routes 126–130), `act6_02_kamino_spire.csv` (Tipoca City, Routes 131–134, Sealed Vault, Asteroid Spire).
  - [x] C3g Ilum (Act 7): `act7_01_ilum.csv` (Crystal Caves, Luke's last battle, the Four Trials as Force visions: Maul, Qui-Gon, Ki-Adi, Anakin; Obi-Wan as Champion; Hall of Fame).
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
- 2026-10-31 · C3b (part 1) · see git log · Kashyyyk dialogue (138 texts). `KEEP_REST_MAPS` now also marks UNCHANGED texts as reviewed. Money: `¥` written as "credits" in curated text; the glyph itself is an art item for Step 5.
- 2026-10-31 · C3b done · see git log · Mos Eisley + Route 110 (417 texts). Decision: generic BIKE stays BIKE (hover-bike); MECHADOLL → QUIZ DROID. Total curated 1,091 (9%).
- 2026-10-31 · C3c done · see git log · Mos Espa, Anchorhead, desert routes, Sullust and Mustafar (530 texts). Vader intro and defeat rewritten; Nien Nunb male; pair trainers hand-named with speaker labels swapped by the build. Total curated 1,621 (14%). Next: C3d Endor (Fortree, Routes 119–120).
- 2026-10-31 · C3d done · see git log · Endor (208 texts). Build: plural rule for BIRD/BUG/<TYPE>-type/with/of/and CREATURE (unless a determiner comes first, or CREATURE is an adjective). Total curated 1,829 (16%). Next: C3e Bespin (Lilycove), Jedha (Mt. Pyre), Yavin 4 (Mossdeep), Hoth (Shoal Cave).
- 2026-10-31 · C3e (part 1) · see git log · Jedha Temple and Fortress Vader (132 texts). Kyber fix: Vader takes the BLUE KYBER, Jabba the RED (Mustafar line corrected). Next: Bespin (Lilycove).
- 2026-10-31 · C3e (part 2) · see git log · Cloud City and the Hutt Hideout (308 texts): cloud sea instead of sea, Tibanna mine hideout, starliner platform, Boba Fett's lines. Build: more plural triggers (type names, steal/trade/raise/catch). Total curated 2,269 (20%). Next: Yavin 4 (Mossdeep, Launch Tower, Routes 124–125), Hoth (Shoal Cave).
- 2026-10-31 · C3e done · see git log · Yavin 4 and Hoth (195 texts). Vos & Aayla speak as master and Padawan; Leia ORGANA leaves the R1 UNIT; Shoal Cave tides are Hoth meltwater. Next: C3f Dagobah (Sootopolis, Cave of Origin, Seafloor Cavern, Routes 126–130), Kamino (Pacifidlog, 131–134), Asteroid Spire.
- 2026-10-31 · C3f (part 1) · see git log · Dagobah (214 texts): Yoda speaks in his inverted style, Vader commands rather than begs, Jabba drowns the worlds. Glossary: EVER GRANDE, split POKéMON\nLEAGUE.
- 2026-10-31 · C3f done · see git log · Kamino and the Asteroid Spire. `tools/curate_texts.py`: trainer battle lines (`data/text/trainers.inc`, no map_id) now count toward KEEP_REST_MAPS by text-id prefix; all area specs re-run, 15 trainer-line overflows fixed. Shared systems (TV, match call, day care, contests) stay for C3i. Total curated 3,835 (34%). Next: C3g Ilum (Ever Grande, Victory Road, the Four Trials).
- 2026-10-31 · C3g done · see git log · Ilum (90 texts). Each Trial names its lesson (fear, loss, betrayal, the fallen hero). Next: C3h post-game (Grand Arena = Battle Frontier, islands), then C3i shared systems.
- 2026-10-31 · C3 gaps · see git log · Republic Wreck (Abandoned Ship), STAR TIDAL starliner, event islands (`gaps_01_ships_islands.csv`, 108 texts). Chewie roars on the starliner too. Next: C3h Grand Arena (Battle Frontier).
