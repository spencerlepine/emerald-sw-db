r"""Write a curated dialogue file (mapping/texts/*.csv) from a small Python spec.

    python3 tools/curate_texts.py spec.py mapping/texts/act1_03_x.csv

The spec is a Python file defining
    FIX = {text_id: [(old, new), ...] | "full replacement text" | []}
    NOTES = {text_id: "note"}            (optional)
KEEP_REST_MAPS = ("map:x", ...) (optional) accepts every other AUTO draft on
those maps as reviewed. The tool rebuilds without the output file first, so pairs always apply to
fresh AUTO drafts. A list of (old, new) pairs is applied to the current AUTO draft (an empty list
keeps the draft as reviewed). Write "\\n" as a plain \n inside normal strings;
\l and \p can be typed as is. Pairs whose new text is already present are
skipped, so a spec still works after a glossary fix. The output CSV is the
source of truth; the spec is just a convenience and need not be committed.
"""
import csv, sys, runpy, warnings
warnings.simplefilter("ignore")
E = lambda x: x.replace("\n", "\\n")
spec = runpy.run_path(sys.argv[1]); FIX = spec["FIX"]; NOTES = spec.get("NOTES", {})
# work from fresh AUTO drafts: rebuild without the file being (re)written
import os, subprocess
from pathlib import Path
outp = Path(sys.argv[2]); bak = outp.with_suffix(".csv.bak")
if outp.exists():
    outp.rename(bak)
try:
    subprocess.run([sys.executable, "tools/build.py"], check=True, stdout=subprocess.DEVNULL)
finally:
    if bak.exists():
        bak.unlink()
auto = {r["text_id"]: r for r in csv.DictReader(open("database/texts.csv", encoding="utf-8"))}
out = []
for tid, fx in FIX.items():
    assert tid in auto, tid
    base = auto[tid]["sw_text_raw"] if auto[tid]["text_status"] != "CURATED" or tid in spec.get("REDO", ()) else auto[tid]["sw_text_raw"]
    if isinstance(fx, str):
        s = E(fx)
    else:
        s = base
        for a, b in fx:
            a, b = E(a), E(b)
            if a not in s and b in s: continue
            if a not in s:
                print(f"MISS {tid}: {a!r}\n     in {s!r}")
                continue
            s = s.replace(a, b)
    out.append([tid, s, NOTES.get(tid, "")])
# KEEP_REST_MAPS: every other text on these maps was read and its AUTO draft is accepted as is
for tid, r in auto.items():
    if tid not in FIX and r["map_id"] and r["map_id"].startswith(tuple(spec.get("KEEP_REST_MAPS", ()))) \
            and r["text_status"] in ("AUTO", "UNCHANGED"):
        out.append([tid, r["sw_text_raw"], "reviewed AUTO draft" if r["text_status"] == "AUTO" else "reviewed, no change needed"])
w = csv.writer(open(sys.argv[2], "w", newline="", encoding="utf-8"))
w.writerow(["text_id", "sw_text_raw", "notes"]); w.writerows(out)
print(len(out), "rows ->", sys.argv[2])
