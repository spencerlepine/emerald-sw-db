# mapping/ (hand-written)

Every file is keyed by `emerald_id` (the id from emerald-db) and carries
`swap_kind`, `map_status`, `art_status`. `tools/build.py` merges these onto
emerald-db and writes `database/`. Rows not listed in any file default to
`HOTSWAP / TODO` (or `KEEP` for generic mechanics).

| File | Rows | Extra columns |
|---|---|---|
| `species.csv` | all 386 creatures | `sw_basis` (starwars-db id, `canon:<name>` or `original`), `home_planet`, `sw_description` (datapad concept), `habitat_note` (where Emerald's wild placement doesn't fit the new planet) |
| `characters.csv` | 59 characters + 25 organizations | `sw_title`, `home_planet`, `role`, `canon_note` (how it bends canon), `text_terms` (`OLD=>NEW` pairs used in dialogue and trainer names) |
| `trainer_classes.csv`, `badges.csv`, `types.csv`, `abilities.csv`, `moves.csv`, `items.csv` | | `sw_basis`, `sw_description`, `notes` |
| `locations.csv` | 213 region-map sections | `planet`. Map titles (`map:*`) are derived: location name + room. |
| `glossary.csv` | | `emerald_term, sw_term`: generic words (POKéMON → CREATURE). Wins over names derived from entities. |
| `net_new.csv` | | `id` (`net:*`), `placeholder_from` (Emerald asset or map to copy), `depends_on` (flag / item), `balance_note` |
| `timeline.csv` | 45 story events | `emerald_event_id, sw_title, sw_tagline, sw_description, sw_lore, planet, map_status` |
| `texts/*.csv` | curated dialogue | `text_id, sw_text_raw, notes`. Keep Emerald's control codes (`\n`, `\l`, `\p`, `$`, `{PLAYER}` …). |

Name limits: creature 10, move 12, item 14, ability 12, type 6, trainer
class 12, trainer name 10, map name 16.
