#!/usr/bin/env python3
"""Write text/chPP.CC-hindi.md and -english.md from the reviewed layer chunks.

    python3 tools/write_hindi_english.py BOOK_DIR [--part 05] [--check]

Reads layers-work/pPP/chCC/chunk*_final.json (units in order), maps each unit to its line
IDs (translation on the unit's first line, "~" on the others), and writes a file only when its
IDs equal those of text/chPP.CC.md exactly. Never touches the Sanskrit or the -sandhi files.
"""
import json, re, sys
from pathlib import Path

book = Path(sys.argv[1]).resolve()
part = sys.argv[sys.argv.index("--part") + 1] if "--part" in sys.argv else "05"
check = "--check" in sys.argv
ID = re.compile(r"^(\S+) \| ")
wrote = bad = 0
for chdir in sorted((book / "layers-work" / f"p{part}").glob("ch*")):
    cc = chdir.name[2:]
    src = book / "text" / f"ch{part}.{cc}.md"
    if not src.is_file():
        print("no Sanskrit file", src.name); bad += 1; continue
    want = [ID.match(l)[1] for l in src.read_text(encoding="utf-8").splitlines() if l.strip()]
    hi, en = {}, {}
    chunks = sorted(chdir.glob("chunk*_final.json"), key=lambda p: int(re.search(r"chunk(\d+)_", p.name)[1]))
    for f in chunks:
        for u in json.loads(f.read_text(encoding="utf-8")):
            for k, i in enumerate(u["line_ids"]):
                hi[i] = u["hindi"].strip() if k == 0 else "~"
                en[i] = u["english"].strip() if k == 0 else "~"
    if sorted(hi) != sorted(want) or list(dict.fromkeys(hi)) != want and set(hi) != set(want):
        miss = [i for i in want if i not in hi]; extra = [i for i in hi if i not in set(want)]
        print(f"ch{cc}: ID mismatch, missing {miss[:5]} extra {extra[:5]}"); bad += 1; continue
    for name, d in (("hindi", hi), ("english", en)):
        body = "".join(f"{i} | {d[i]}\n" for i in want)
        assert "\n\n" not in body and all(d[i] for i in want)
        if not check:
            (book / "text" / f"ch{part}.{cc}-{name}.md").write_text(body, encoding="utf-8")
    wrote += 1
    print(f"ch{cc}: {len(want)} lines ok")
print("chapters written" if not check else "chapters checked", wrote, "problems", bad)
sys.exit(1 if bad else 0)
