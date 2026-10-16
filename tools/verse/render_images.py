#!/usr/bin/env python3
"""Render every IMAGE_SPEC of a book into BOOK_DIR/images/aids/.

    python3 render_images.py BOOK_DIR [--out DIR] [--shots DIR]
    python3 render_images.py --selftest [--shots DIR]

Finds the IMAGE_SPECS of all authored modules named in
BOOK_DIR/verse_book.json (same loading rules as make_bank.py, so the
BATCHES environment variable works), draws each one (chain / table / split /
mountain / mermaid, see make_aid_images.py) and checks that the file exists
and is under 80 KB. Exit code 1 if any picture fails.

--shots DIR  also writes a PNG screenshot of every picture at 360 px width
             (Playwright + the preinstalled Chromium) to look at them.
--selftest   renders three sample mermaid diagrams (flowchart with
             Devanagari labels, mindmap, bar graph) into a temp dir and
             prints their sizes.
"""
import argparse
import base64
import os
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import make_aid_images as pics  # noqa: E402

LIMIT = 80 * 1024
SOFT_LIMIT = 60 * 1024

SAMPLES = {
    "selftest-flow.svg": {
        "file": "selftest-flow.svg", "type": "mermaid",
        "alt": "Flowchart: urge suppressed, then vata moves wrongly upward",
        "code": """flowchart TD
  A["वेग न रोकें<br/>(अधारणीय वेग)"] --> B["अधोवात रुके"]
  B --> C["गुल्म"]
  B --> D["उदावर्त"]
  C --> E{"चिकित्सा?"}
  D --> E
  E -- हाँ --> F["वात का अनुलोमन"]
  E -- नहीं --> G["रोग बढ़े"]
"""},
    "selftest-mindmap.svg": {
        "file": "selftest-mindmap.svg", "type": "mermaid",
        "alt": "Mind map: the three doshas vata, pitta and kapha",
        "code": """mindmap
  root((त्रिदोष))
    वात
      रूक्ष
      लघु
      शीत
    पित्त
      उष्ण
      तीक्ष्ण
    कफ
      स्निग्ध
      गुरु
      मन्द
"""},
    "selftest-bar.svg": {
        "file": "selftest-bar.svg", "type": "mermaid",
        "alt": "Bar graph: number of verses in four chapters",
        "code": """xychart-beta
  title "अध्यायवार श्लोक-संख्या"
  x-axis ["अ. १", "अ. २", "अ. ३", "अ. ४"]
  y-axis "श्लोक" 0 --> 150
  bar [141, 36, 30, 29]
"""},
}


def check(path):
    """(ok, message) for one rendered file."""
    if not path.exists():
        return False, "missing"
    size = path.stat().st_size
    if size >= LIMIT:
        return False, f"{size / 1024:.1f} KB (limit 80 KB)"
    note = " (over the 60 KB aim)" if size >= SOFT_LIMIT else ""
    return True, f"{size / 1024:.1f} KB{note}"


def screenshots(files, shots):
    """PNG of each SVG at 360 px width (needs Playwright)."""
    from playwright.sync_api import sync_playwright
    shots.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch(
            executable_path=pics.find_chromium(), args=["--no-sandbox"])
        page = browser.new_page(viewport={"width": 360, "height": 400},
                                device_scale_factor=2)
        for f in files:
            data = base64.b64encode(Path(f).read_bytes()).decode()
            html = (f'<body style="margin:0;background:#fff">'
                    f'<img src="data:image/svg+xml;base64,{data}" '
                    f'style="width:360px;display:block"></body>')
            page.set_content(html)
            page.wait_for_timeout(150)
            target = shots / (Path(f).stem + ".png")
            page.screenshot(path=str(target), full_page=True)
            print("  shot", target)
        browser.close()


def selftest(shots):
    out = Path(tempfile.mkdtemp(prefix="verse-selftest-"))
    bad = 0
    files = []
    for name, spec in SAMPLES.items():
        path = out / name
        try:
            path.write_text(pics.render_spec(spec), encoding="utf8")
        except pics.MermaidError as err:
            print(f"FAIL {name}: {err}")
            bad += 1
            continue
        ok, msg = check(path)
        print(f"{'ok  ' if ok else 'FAIL'} {name}: {msg}")
        bad += not ok
        files.append(path)
    if shots and files:
        screenshots(files, Path(shots))
    print("selftest:", "FAILED" if bad else "passed", "->", out)
    return 1 if bad else 0


def book_specs(book):
    import make_bank
    cfg = make_bank.load_config(book)
    chapters = [make_bank.Chapter(cfg, ch) for ch in cfg["chapters"]]
    make_bank.load_modules(book, cfg, chapters)
    specs, seen = [], {}
    for chap in chapters:
        for key, spec in sorted(chap.image_specs.items()):
            name = spec["file"]
            if name in seen:
                raise SystemExit(f"file name {name} is used twice "
                                 f"({seen[name]} and {key})")
            seen[name] = key
            specs.append((chap.number, key, spec))
    refs = [(chap.number, key, v[0]) for chap in chapters
            for key, v in chap.images.items()]
    return specs, refs


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("book", nargs="?")
    ap.add_argument("--out", help="output folder (default BOOK/images/aids)")
    ap.add_argument("--shots", help="also write 360 px PNG screenshots here")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        sys.exit(selftest(a.shots))
    if not a.book:
        ap.error("BOOK_DIR is required (or --selftest)")
    book = Path(a.book).resolve()
    out = Path(a.out) if a.out else book / "images" / "aids"
    out.mkdir(parents=True, exist_ok=True)
    specs, refs = book_specs(book)
    bad, written = 0, []
    for ch, key, spec in specs:
        path = out / spec["file"]
        try:
            path.write_text(pics.render_spec(spec), encoding="utf8")
        except (pics.MermaidError, KeyError) as err:
            print(f"FAIL ch{ch} {key} {spec['file']}: {err}")
            bad += 1
            continue
        ok, msg = check(path)
        print(f"{'ok  ' if ok else 'FAIL'} ch{ch} {key} {spec['file']}: {msg}")
        bad += not ok
        written.append(path)
    made = {s["file"] for _, _, s in specs}
    for ch, key, name in refs:  # pictures referenced but not drawn here
        if name not in made:
            ok, msg = check(out / name)
            if not ok:
                print(f"FAIL ch{ch} {key} {name}: referenced picture {msg}")
                bad += 1
    print(f"{len(specs)} pictures drawn into {out}"
          + (f", {bad} problem(s)" if bad else ", all within 80 KB"))
    if a.shots and written:
        screenshots(written, Path(a.shots))
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
