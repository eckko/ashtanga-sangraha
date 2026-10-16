#!/usr/bin/env python3
"""Draw the small pictures for the memory aids (flat SVG, own parchment
panel so they read in light and dark pages).

Spec types (the IMAGE_SPECS of an authored module):
  chain     {"title", "steps": [..]}                  boxes with arrows
  table     {"title", "heads": [a, b], "rows": [[a, b], ..]}
  split     {"title", "cols": [[head, [items]], [head, [items]]]}
  mountain  {"title", "top": [..], "bottom": [..]}    two ledges
  mermaid   {"code": "<mermaid source>"}              rendered by mermaid-cli:
            flowchart / graph, mindmap, timeline, pie, quadrantChart,
            xychart-beta (bar and line graphs)
every spec also has "file" (unique "name.svg"), "alt" and "type".

    python3 make_aid_images.py SPECS.json OUT_DIR   # specs: {file: spec}
    python3 render_images.py BOOK_DIR               # all specs of a book

Mermaid needs Node and mermaid-cli (once, in this folder):
    PUPPETEER_SKIP_DOWNLOAD=1 npm i @mermaid-js/mermaid-cli@11
and a Chromium: env PUPPETEER_EXECUTABLE_PATH, else /opt/pw-browsers/*.
Results are cached by a hash of the code (~/.cache/verse-study/mermaid, or
env VERSE_STUDY_CACHE), so a re-run is instant.
"""
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
BG, INK, MUTED, TEAL, ACC = "#fffdf8", "#2a2118", "#7a6c5a", "#2f6f6a", "#a4400f"
LINE = "#e4d9c6"
FONT = "'Noto Sans Devanagari','Mukta','Nirmala UI','Mangal',sans-serif"
MERMAID_FONT = ("'Noto Sans Devanagari','Mukta','Nirmala UI','Mangal',"
                "'FreeSans',sans-serif")
W, H = 360, 200


def svg(body, title, height=H):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} '
            f'{height}" role="img"><title>{title}</title>'
            f'<rect width="{W}" height="{height}" rx="14" fill="{BG}" '
            f'stroke="{LINE}"/>' + body + '</svg>')


def text(x, y, s, size=13, fill=INK, anchor="middle", weight=500):
    return (f'<text x="{x}" y="{y}" font-family="{FONT}" font-size="{size}" '
            f'font-weight="{weight}" fill="{fill}" text-anchor="{anchor}">'
            f'{s}</text>')


def arrow(x1, y1, x2, y2, color=TEAL):
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" '
            f'stroke-width="2.5" stroke-linecap="round"/>'
            f'<polygon points="{x2},{y2} {x2 - 8},{y2 - 5} {x2 - 8},{y2 + 5}" '
            f'fill="{color}"/>')


def wrap(s, limit):
    out, line = [], ""
    for word in s.split(" "):
        if line and len(line) + 1 + len(word) > limit:
            out.append(line)
            line = word
        else:
            line = (line + " " + word).strip()
    out.append(line)
    return out


def mountain(top, bottom, title, alt="two ledges of a mountain"):
    tl = wrap(" · ".join(top), 30)
    bl = wrap(" · ".join(bottom), 40)
    height = 120 + 18 * (len(tl) + len(bl))
    body = (f'<polygon points="20,{height - 15} 180,24 340,{height - 15}" '
            f'fill="{TEAL}" opacity="0.18"/>')
    y = 66
    h1 = 18 * len(tl) + 10
    body += (f'<rect x="80" y="{y - 18}" width="200" height="{h1}" rx="8" '
             f'fill="{BG}" stroke="{TEAL}"/>')
    for line in tl:
        body += text(180, y, line, 12.5)
        y += 18
    y += 22
    h2 = 18 * len(bl) + 10
    body += (f'<rect x="34" y="{y - 18}" width="292" height="{h2}" rx="8" '
             f'fill="{BG}" stroke="{ACC}"/>')
    for line in bl:
        body += text(180, y, line, 12.5)
        y += 18
    body += text(180, 20, title, 13, TEAL, weight=700)
    return svg(body, alt, height)


def box(x, y, w, h, lines, stroke=TEAL, size=12.5):
    out = (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" '
           f'fill="{BG}" stroke="{stroke}"/>')
    top = y + h / 2 - 9 * (len(lines) - 1) + 4
    for i, ln in enumerate(lines):
        out += text(x + w / 2, top + 18 * i, ln, size)
    return out


def chain_spec(spec):
    """Boxes stacked top to bottom with arrows between them."""
    steps = spec["steps"]
    boxes = [wrap(t, 34) for t in steps]
    y, body = 40, text(180, 22, spec["title"], 13, TEAL, weight=700)
    for i, lines in enumerate(boxes):
        h = 18 * len(lines) + 12
        body += box(40, y, 280, h, lines)
        y += h
        if i < len(boxes) - 1:
            body += (f'<line x1="180" y1="{y}" x2="180" y2="{y + 16}" '
                     f'stroke="{ACC}" stroke-width="2.5"/>'
                     f'<polygon points="180,{y + 22} 174,{y + 13} 186,'
                     f'{y + 13}" fill="{ACC}"/>')
            y += 24
    return svg(body, spec["alt"], y + 16)


def table_spec(spec):
    """Rows of (left, right) pairs under two column heads."""
    heads = spec.get("heads", ["", ""])
    y, body = 62, text(180, 22, spec["title"], 13, TEAL, weight=700)
    body += text(100, 46, heads[0], 12, ACC, weight=700)
    body += text(262, 46, heads[1], 12, ACC, weight=700)
    for a, b in spec["rows"]:
        la, lb = wrap(a, 18), wrap(b, 22)
        h = 18 * max(len(la), len(lb)) + 10
        body += box(20, y, 160, h, la) + box(190, y, 150, h, lb, ACC)
        y += h + 8
    return svg(body, spec["alt"], y + 8)


def split_spec(spec):
    """Two labelled columns of short lists (e.g. the two sides of a pair)."""
    cols = spec["cols"]
    body = text(180, 22, spec["title"], 13, TEAL, weight=700)
    deep = 0
    for k, (head, items) in enumerate(cols):
        x = 16 + k * 170
        body += text(x + 77, 52, head, 13, ACC if k else TEAL, weight=700)
        y = 64
        for it in items:
            lines = wrap(it, 16)
            h = 18 * len(lines) + 10
            body += box(x, y, 154, h, lines, ACC if k else TEAL)
            y += h + 6
        deep = max(deep, y)
    return svg(body, spec["alt"], deep + 10)


# ------------------------------------------------------------------ mermaid
MERMAID_KINDS = ("flowchart", "graph", "mindmap", "timeline", "pie",
                 "quadrantChart", "xychart-beta", "xychart")
CHROME_GLOBS = ("chromium-*/chrome-linux/chrome",
                "chromium_headless_shell-*/chrome-linux/headless_shell",
                "chromium-*/chrome-linux64/chrome")
# light tints (dark text stays readable on them), borders in teal and brown
TINTS = ["#e3efec", "#f6e4d6", "#f4ecc9", "#e6e2f1", "#e0ecd2", "#f1dbe3",
         "#d8e6f0", "#efe3d0", "#dcebe6", "#f3d9cc", "#ece6c0", "#dfdbee"]
# mid tones for mindmap / timeline branches (dark text is still readable)
MIDS = ["#a9d0c9", "#efc4a6", "#ebd98f", "#cdc6e6", "#bfdba3", "#e9b9c9",
        "#aecde2", "#e3cfa8", "#b6d9cf", "#f0b9a0", "#dccf8e", "#c5bfe2"]
MERMAID_CONFIG = {
    "theme": "base",
    "fontFamily": MERMAID_FONT,
    "htmlLabels": False,
    "themeVariables": {
        "fontFamily": MERMAID_FONT,
        "fontSize": "15px",
        "background": BG,
        "mainBkg": TINTS[0],
        "textColor": INK,
        "primaryColor": TINTS[0],
        "primaryTextColor": INK,
        "primaryBorderColor": TEAL,
        "secondaryColor": TINTS[1],
        "secondaryTextColor": INK,
        "secondaryBorderColor": ACC,
        "tertiaryColor": BG,
        "tertiaryTextColor": INK,
        "tertiaryBorderColor": MUTED,
        "lineColor": ACC,
        "nodeBorder": TEAL,
        "clusterBkg": "#faf4e8",
        "clusterBorder": MUTED,
        "edgeLabelBackground": BG,
        "titleColor": TEAL,
        "noteBkgColor": "#f4ecc9",
        "noteTextColor": INK,
        "noteBorderColor": MUTED,
        # mindmap / timeline sections
        **{f"cScale{i}": MIDS[i] for i in range(12)},
        **{f"cScaleLabel{i}": INK for i in range(12)},
        **{f"cScaleInv{i}": TEAL for i in range(12)},
        # pie
        **{f"pie{i + 1}": TINTS[i] for i in range(12)},
        "pieTitleTextSize": "18px",
        "pieTitleTextColor": TEAL,
        "pieSectionTextSize": "14px",
        "pieSectionTextColor": INK,
        "pieLegendTextSize": "14px",
        "pieLegendTextColor": INK,
        "pieStrokeColor": TEAL,
        "pieStrokeWidth": "1.5px",
        "pieOuterStrokeColor": TEAL,
        "pieOuterStrokeWidth": "1.5px",
        "pieOpacity": "0.95",
        # quadrant chart
        "quadrant1Fill": TINTS[0], "quadrant2Fill": TINTS[2],
        "quadrant3Fill": TINTS[1], "quadrant4Fill": TINTS[3],
        "quadrant1TextFill": INK, "quadrant2TextFill": INK,
        "quadrant3TextFill": INK, "quadrant4TextFill": INK,
        "quadrantPointFill": ACC, "quadrantPointTextFill": INK,
        "quadrantXAxisTextFill": INK, "quadrantYAxisTextFill": INK,
        "quadrantInternalBorderStrokeFill": MUTED,
        "quadrantExternalBorderStrokeFill": TEAL,
        "quadrantTitleFill": TEAL,
        # xychart (bar / line graph)
        "xyChart": {
            "backgroundColor": BG, "titleColor": TEAL,
            "xAxisLabelColor": INK, "xAxisTitleColor": INK,
            "xAxisTickColor": MUTED, "xAxisLineColor": MUTED,
            "yAxisLabelColor": INK, "yAxisTitleColor": INK,
            "yAxisTickColor": MUTED, "yAxisLineColor": MUTED,
            "plotColorPalette": f"{TEAL},{ACC},#c8963e,#5b7aa6,#8a5a83",
        },
    },
    # mermaid brightens timeline events by 20 %: keep the palette
    "themeCSS": (".eventWrapper{filter:none;}"
                 ".titleText{fill:%s;font-weight:700;}" % TEAL),
    "flowchart": {"htmlLabels": False, "useMaxWidth": False, "padding": 12,
                  "nodeSpacing": 28, "rankSpacing": 34, "curve": "basis"},
    "mindmap": {"useMaxWidth": False, "padding": 20},
    "timeline": {"useMaxWidth": False, "padding": 10},
    "pie": {"useMaxWidth": False, "textPosition": 0.7},
    "quadrantChart": {"chartWidth": 340, "chartHeight": 340,
                      "pointLabelFontSize": 13, "titleFontSize": 18,
                      "quadrantLabelFontSize": 13, "xAxisLabelFontSize": 13,
                      "yAxisLabelFontSize": 13},
    "xyChart": {"width": 340, "height": 260, "titleFontSize": 18,
                "xAxis": {"labelFontSize": 13, "titleFontSize": 14},
                "yAxis": {"labelFontSize": 13, "titleFontSize": 14}},
}


# per diagram type: settings that make the text readable at card width
KIND_TUNING = {
    # the mindmap layout is wide (about 750 px): a large font keeps the text
    # near 12 px when the picture is shown 360 px wide
    "mindmap": {"themeVariables": {"fontSize": "32px"}},
    "timeline": {"themeVariables": {"fontSize": "19px"}},
}


def config_for(kind):
    """MERMAID_CONFIG with the tuning of one diagram type merged in."""
    cfg = json.loads(json.dumps(MERMAID_CONFIG))
    for key, val in KIND_TUNING.get(kind, {}).items():
        if isinstance(val, dict):
            cfg.setdefault(key, {}).update(val)
        else:
            cfg[key] = val
    return cfg


class MermaidError(RuntimeError):
    pass


def find_chromium():
    env = os.environ.get("PUPPETEER_EXECUTABLE_PATH")
    if env and Path(env).exists():
        return env
    root = Path(os.environ.get("PLAYWRIGHT_BROWSERS_PATH", "/opt/pw-browsers"))
    for pattern in CHROME_GLOBS:
        hits = sorted(root.glob(pattern))
        if hits:
            return str(hits[-1])
    for name in ("chromium", "chromium-browser", "google-chrome", "chrome"):
        found = shutil.which(name)
        if found:
            return found
    raise MermaidError(
        "no Chromium found: set PUPPETEER_EXECUTABLE_PATH or install one "
        "under /opt/pw-browsers")


def find_mmdc():
    env = os.environ.get("MMDC")
    if env:
        return [env]
    local = HERE / "node_modules" / ".bin" / "mmdc"
    if local.exists():
        return [str(local)]
    raise MermaidError(
        f"mermaid-cli is not installed: cd {HERE} && "
        "PUPPETEER_SKIP_DOWNLOAD=1 npm i @mermaid-js/mermaid-cli@11")


def cache_dir():
    d = Path(os.environ.get("VERSE_STUDY_CACHE")
             or Path.home() / ".cache" / "verse-study" / "mermaid")
    d.mkdir(parents=True, exist_ok=True)
    return d


def normalise(code, kind):
    """Small repairs so that every diagram renders legibly.

    timeline: plain "timeline" (left to right, very wide) becomes
    "timeline TD" (top to bottom, fits a phone).
    mindmap: a shaped root such as root((X)) is drawn with its label off
    centre when htmlLabels is off, so the root is written as plain text."""
    if kind == "timeline":
        lines = code.splitlines()
        if lines[0].strip() == "timeline":
            lines[0] = "timeline TD"
        code = "\n".join(lines) + "\n"
    if kind == "mindmap":
        lines = code.splitlines()
        for i, line in enumerate(lines[1:], 1):
            if line.strip() and not line.strip().startswith("%%"):
                m = re.match(r"^(\s*)(?:\w*)(\(\(|\(|\[\[|\[|\{\{)(.+?)"
                             r"(\)\)|\)|\]\]|\]|\}\})\s*$", line)
                if m:
                    lines[i] = m.group(1) + m.group(3)
                break
        code = "\n".join(lines) + "\n"
    return code


def first_keyword(code):
    for line in code.splitlines():
        s = line.strip()
        if not s or s.startswith("%%"):
            continue
        return re.split(r"[\s;]", s, 1)[0]
    return ""


def tidy_svg(raw, alt, svg_id, panel=True):
    """Make mermaid's SVG a self-contained, scalable card picture."""
    s = re.sub(r"^\s*<\?xml[^>]*>\s*", "", raw)
    s = re.sub(r"<!--.*?-->", "", s, flags=re.S)
    s = re.sub(r"@import\s+url\([^)]*\)\s*;?", "", s)
    s = re.sub(r"<link\b[^>]*>", "", s)
    if "<foreignObject" in s:
        raise MermaidError(
            "mermaid used HTML labels (<foreignObject>), which do not render "
            "reliably as an image; this diagram type ignored htmlLabels:false")
    head = re.match(r"<svg\b[^>]*>", s)
    if not head:
        raise MermaidError("mermaid output is not an SVG")
    tag = head.group(0)
    vb = re.search(r'viewBox="([-\d.\s,eE]+)"', tag)
    if not vb:
        raise MermaidError("mermaid SVG has no viewBox")
    x, y, w, h = [float(v) for v in vb.group(1).replace(",", " ").split()]
    pad = 12
    x, y, w, h = x - pad, y - pad, w + 2 * pad, h + 2 * pad
    num = lambda v: f"{v:.2f}".rstrip("0").rstrip(".")
    new_tag = (f'<svg xmlns="http://www.w3.org/2000/svg" id="{svg_id}" '
               f'viewBox="{num(x)} {num(y)} {num(w)} {num(h)}" '
               f'width="{num(w)}" height="{num(h)}" role="img" '
               f'preserveAspectRatio="xMidYMid meet">')
    body = s[len(tag):]
    body = re.sub(r"\bmy-svg\b", svg_id, body)
    # timeline title: oversized black bold -> card heading
    body = body.replace('font-size="4ex" font-weight="bold"',
                        f'font-size="22" font-weight="700" fill="{TEAL}"')
    alt_x = (alt.replace("&", "&amp;").replace("<", "&lt;")
             .replace(">", "&gt;"))
    panel_rect = (f'<rect x="{num(x)}" y="{num(y)}" width="{num(w)}" '
                  f'height="{num(h)}" rx="14" fill="{BG}" stroke="{LINE}"/>'
                  if panel else "")
    out = new_tag + f"<title>{alt_x}</title>" + panel_rect + body
    out = re.sub(r">\s+<", "><", out)  # drop layout whitespace
    return out


def render_mermaid(spec, use_cache=True):
    code = spec["code"].strip() + "\n"
    kind = first_keyword(code)
    code = normalise(code, kind)
    if kind not in MERMAID_KINDS:
        raise MermaidError(
            f"{spec.get('file')}: unsupported mermaid diagram {kind!r}; "
            f"use one of {', '.join(MERMAID_KINDS)}")
    config = json.dumps(config_for(kind), sort_keys=True,
                        ensure_ascii=False)
    key = hashlib.sha256(
        (code + "\0" + config + "\0" + spec.get("alt", "") + "\0v4")
        .encode("utf8")).hexdigest()
    cached = cache_dir() / (key[:32] + ".svg")
    if use_cache and cached.exists():
        return cached.read_text(encoding="utf8")
    cmd = find_mmdc()
    chrome = find_chromium()
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        (tmp / "in.mmd").write_text(code, encoding="utf8")
        (tmp / "cfg.json").write_text(config, encoding="utf8")
        (tmp / "pp.json").write_text(json.dumps(
            {"executablePath": chrome, "args": ["--no-sandbox"]}))
        svg_id = "mm" + key[:8]
        run = subprocess.run(
            cmd + ["-i", str(tmp / "in.mmd"), "-o", str(tmp / "out.svg"),
                   "-p", str(tmp / "pp.json"), "-c", str(tmp / "cfg.json"),
                   "-b", "transparent", "-I", svg_id, "-q"],
            capture_output=True, text=True, timeout=180)
        out = tmp / "out.svg"
        if run.returncode or not out.exists():
            raise MermaidError(
                f"mermaid failed for {spec.get('file')}:\n"
                f"{(run.stderr or run.stdout).strip()}\n--- source ---\n{code}")
        raw = out.read_text(encoding="utf8")
    if "Syntax error in text" in raw or "mermaid version" in raw:
        raise MermaidError(f"mermaid syntax error in {spec.get('file')}\n"
                           f"--- source ---\n{code}")
    result = tidy_svg(raw, spec.get("alt", ""), svg_id)
    cached.write_text(result, encoding="utf8")
    return result


def render_spec(spec):
    kind = spec["type"]
    if kind == "mountain":
        return mountain(spec["top"], spec["bottom"], spec["title"],
                        spec.get("alt", "two ledges of a mountain"))
    if kind == "mermaid":
        return render_mermaid(spec)
    return {"chain": chain_spec, "table": table_spec,
            "split": split_spec}[kind](spec)


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    specs = json.load(open(sys.argv[1], encoding="utf8"))
    out = Path(sys.argv[2])
    out.mkdir(parents=True, exist_ok=True)
    items = specs.items() if isinstance(specs, dict) else \
        ((s["file"], s) for s in specs)
    for name, spec in items:
        (out / name).write_text(render_spec(spec), encoding="utf8")
    print(len(specs), "images in", out)


if __name__ == "__main__":
    main()
