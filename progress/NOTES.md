# Working notes

## Decisions

- **Same ids as emerald-db.** Every row is keyed by the Emerald id; the Star Wars name lives in `sw_name` / `sw_title` and the proposed C constant in `sw_constant`. Net-new rows use `net:*` ids.
- **Generated output only in database/.** Hand-written input lives in `mapping/` and `bible/`.
- **Unchanged game data is not copied** (learnsets, parties, encounters, scripts, flags): join emerald-db by id. Only tables with Star Wars content are generated here.
- **Auto drafts for text.** `texts.csv` swaps every mapped name and glossary term (uppercase, whole word, longest first). The glossary wins over derived names; trainer-class names are not used in text (CHAMPION, LEADER, PSYCHIC are generic words in dialogue). Ambiguous terms are left alone and listed in `text_terms.csv`.
- **Plurals.** Emerald's POKéMON is singular and plural; CREATURE isn't. The build fixes the obvious cases ("CREATURES are", "all your CREATURES"); the rest is curated text work (C3).
- **Every image is PENDING_ART** because Step 5 redraws everything. Move animations default to KEEP_ANIM; only the renamed moves that want a Star Wars VFX are PENDING_ART.
- **Named characters are people, never creatures.** The player is one fixed character chosen at the start; there is no party member that is a story character. (Owner, 2026-10-31.)
- **Timeline frame: ~2 BBY**, starting on Tatooine (owner's primer). Dead-by-2-BBY prequel figures appear only as visions (the Four Trials), as Order 66 survivors (Vos & Aayla), or in lore.

## Gotchas

- emerald-db's PR #1 is merged, but this session's checkout of emerald-db was on branch `claude/project-thread-vu8ith`; `origin/main` has the same data (commit 99e771c).
- Item shards (RED SHARD …) are renamed to RED CRYSTAL etc. so they never collide with arena SHARDS (badges).
- `species.csv` covers the 386 real species; the 25 `old-unown-*` placeholders, Unown letter forms and the Egg are KEEP by default.
- Kanto/Sevii region-map sections (FireRed leftovers) are KEEP; they are not reachable in Emerald.

## Open questions for the owner

- CREATURE vs COMPANION as the word for Pokémon.
- Mr. Stone as Bail Organa running Incom is a stretch; alternatives: an original Incom president, or make Devon "House Organa".
- Gym 7: Quinlan Vos & Aayla Secura (Order 66 survivors) vs. another duo.
- Arena leader 1 (Kitster) and 4 (Nien Nunb) are the weakest fits.
- Many national-dex creatures are `original` names; happy to swap any for canon creatures you prefer.

## Text drafting: control codes

`build.py` matches terms whole-word. Emerald's `\n`, `\l`, `\p` put a letter right before the next word, so the lookbehind also accepts a preceding control code. Before this fix about 190 texts silently kept Pokémon terms.

## Berries

All berries are `<NAME> FRUIT` (max 14 chars). Canon where Star Wars has a fruit (jogan, muja, pallie, shuura, blba, hubba), original names otherwise. Dialogue uses FRUIT for BERRY and BERRIES (FRUIT BLENDER, FRUIT MASTER). Effects unchanged.

## Text overflow check (pixel based)

`overflow_risk` now measures each line in pixels with Emerald's normal font (glyph widths from
`pokeemerald/src/fonts.c` through `charmap.txt`, saved in `tools/font_widths.json`). The field
text box is 208 px: no Emerald script line without placeholders is wider. A line is flagged when
it is wider than max(208, the widest line of the original text). Placeholders count as
{PLAYER}/{RIVAL} 42 px, {STR_VAR_n} 60 px, {KUN} 0. This replaced a character count (36) and cut
the flagged texts from 466 to about 130.

## Glossary additions (round 2)

Plural and compound forms that the single-word rules got wrong: POKé BALLS, POKéMON MART(S),
POKéMON CENTERS, CONTESTS, GYMS, GYM LEADERS, POKéMON NEWS (HOLONET NEWS), POKéMON WIRELESS CLUB
(HOLONET CLUB), and the article fix "a GYM" → "an ARENA". Item names also get an automatic plural
(POTIONS → BACTA SPRAYS).

## Dialogue conventions (C3)

CREATURES for plural POKéMON; tall grass → scrub or dunes on Tatooine; PC → terminal (storage is
"over the HoloNet"); TV → HoloNet; clock → chrono; sea → water or stars on desert worlds. Luke is
restless and reckless, not frail; Owen and Beru are his uncle and aunt.

## Water on desert worlds (open question)

Emerald's Tatooine maps (Mos Eisley, Routes 103/104/109/110) have sea tiles, and SURF works there.
Curated text keeps it neutral ("the water", "deep-water expedition"). Option for Step 5: draw those
tiles as the DUNE SEA and theme SURF on Tatooine as sand-skimming (art only; mechanics unchanged).
Not decided; needs the owner.

## Jabba's and Vader's motives

Jabba (Archie) wants to drown the dry worlds into swamps "fit for a HUTT" (SANDO = sea titan).
Vader (Maxie) should mirror it with land: an Imperial plan to dry out worlds for industry and
garrisons (GREATKRAYT = land titan). Use this when curating the Empire's lines.
