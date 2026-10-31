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
