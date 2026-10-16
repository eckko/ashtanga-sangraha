#!/usr/bin/env python3
"""Build questions.json for a Sanskrit verse book from its config.

    python3 make_bank.py BOOK_DIR [--out FILE]

BOOK_DIR holds `verse_book.json` (see verse_book.example.json), the verse
data files and the hand-written batch modules (default `tools/authored/`).
Output goes to BOOK_DIR/questions.json unless --out is given.

Environment:
    PARTIAL=1          skip units that no loaded module has authored yet
    BATCHES=a,b        load only these modules from the wildcard patterns of
                       the config (module names without .py); modules named
                       literally (no * ? [ ]) always load

Verse data (Sanskrit, word split, Hindi, English, notes) comes from the
verse files; explanations, aids and questions come from the authored
modules (AUTHORED, NOTES_HI, AIDS, optional IMAGE_SPECS / IMAGES).
"""
import argparse
import glob as globmod
import importlib
import importlib.util
import json
import os
import re
import sys
import unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from indic_transliteration import sanscript as S  # noqa: E402
from gram_hi import gram_hi  # noqa: E402
from metre import split_pada  # noqa: E402

DIGITS = str.maketrans("0123456789", "०१२३४५६७८९")
MAP = {"ṛ": "ri", "ṝ": "ri", "ś": "sh", "Ś": "Sh", "ṣ": "sh", "Ṣ": "Sh",
       "ṃ": "m", "ḥ": "h", "ṅ": "n", "ñ": "n", "ṭ": "t", "ḍ": "d",
       "ṇ": "n", "ḷ": "l"}

KIND_LABELS = {
    "chain": "क्रम-कड़ी",
    "letters": "पहले अक्षर",
    "seesaw": "यदा–तदा",
    "sandhi": "संधि-नियम",
    "frame": "कौन · किसके पास · क्यों",
    "anchors": "शब्द-परिवार",
    "diagram": "चित्र",
    "metre": "छन्द",
    "chunks": "लय में खण्ड",
    "pegs": "चित्र-शब्द (मेरा बनाया चित्र)",
    "puns": "ध्वनि-साम्य (केवल सुनने की सहायता)",
    "contrast": "मिलते-जुलते की जोड़ी",
    "story": "कथा",
}
ORDER = ["frame", "chain", "diagram", "letters", "seesaw", "story", "pegs",
         "puns", "anchors", "sandhi", "contrast", "chunks", "metre"]

DEFAULTS = {
    "bank_id": "verse-book",
    "title": "Sanskrit verse book",
    "genre": "",
    "summary": "",
    "scroll_buttons": True,
    "labels": {"unit": "Chapter", "units": "chapters", "topic": "Verse",
               "whole": "Whole chapter"},
    "data_pattern": "data/chapter{N}_verses.json",
    "authored_dir": "tools/authored",
    "ref_template": "{kind} {unit}, अध्याय {chapter}।",
    "source_disclaimer": "",
    "kind_labels": {"verse": "श्लोक", "prose": "गद्य"},
    "verse_block_labels": {"verse": "श्लोक", "prose": "मूल पाठ"},
    "block_labels": {"ref": "संदर्भ", "words": "पद-विच्छेद",
                     "hindi": "हिन्दी", "english": "English",
                     "explain": "व्याख्या", "aids": "स्मरण-सहायक",
                     "note": "पाठ-टिप्पणी"},
    "digits": "devanagari",
    "id_width": 3,
    "fold_english": True,
    "max_chips_per_row": 30,
    "gram_overrides": {},
    "aid_labels": {},
    "metre_text": ("हर पंक्ति में ८ + ८ अक्षर (गिनती से)। ‘|’ पाद की सीमा है; "
                   "संधि के कारण वह शब्द के बीच भी पड़ सकती है।"),
    "extra_bank_fields": {},
}


# ------------------------------------------------------------------ config
def load_config(book):
    path = Path(book) / "verse_book.json"
    if not path.exists():
        sys.exit(f"missing {path} (copy verse_book.example.json)")
    raw = json.loads(path.read_text(encoding="utf8"))
    cfg = {k: v for k, v in raw.items() if not k.startswith("_")}
    for key, default in DEFAULTS.items():
        if isinstance(default, dict) and isinstance(cfg.get(key), dict):
            merged = dict(default)
            merged.update(cfg[key])
            cfg[key] = merged
        else:
            cfg.setdefault(key, default)
    if not cfg.get("chapters"):
        sys.exit("verse_book.json needs a non-empty 'chapters' list")
    return cfg


def read_sections(book, spec):
    """[(lo, hi, title)] from an inline list or 'path.py:NAME'."""
    if not spec:
        return []
    if isinstance(spec, str):
        file, _, name = spec.partition(":")
        target = Path(book) / file
        mod_spec = importlib.util.spec_from_file_location(
            "vb_sections_" + re.sub(r"\W", "_", file), target)
        mod = importlib.util.module_from_spec(mod_spec)
        mod_spec.loader.exec_module(mod)
        spec = getattr(mod, name or "RANGES")
    return [(float(lo), float(hi), title) for lo, hi, title in spec]


def section_of(ranges, n, fallback):
    if not ranges:
        return fallback
    x = float(n)
    for lo, hi, title in ranges:
        if lo <= x <= hi:
            return title
    raise KeyError(f"unit {n} is in no section range")


# ------------------------------------------------------------- text helpers
dev = lambda s: S.transliterate(unicodedata.normalize("NFC", s), S.IAST,
                                S.DEVANAGARI)


def fold_char(c):
    if "ऀ" <= c <= "ॿ":
        return c
    c = MAP.get(c, c)
    return "".join(x for x in unicodedata.normalize("NFKD", c)
                   if not unicodedata.combining(x))


def fold(text):
    """English text with plain Latin letters (no diacritics)."""
    return "".join(fold_char(c) for c in unicodedata.normalize("NFC", text))


def word_form(word):
    return dev(word.replace(" ", ""))


def split_long(rows, most=30):
    """The template allows at most 30 word chips per row: cut longer rows
    (long prose lines) into near-equal rows."""
    out = []
    for row in rows:
        k = -(-len(row) // most)
        size = -(-len(row) // k)
        out += [row[i:i + size] for i in range(0, len(row), size)]
    return out


# ------------------------------------------------------------- module loading
class Chapter:
    def __init__(self, cfg, ch):
        self.cfg, self.ch = cfg, ch
        self.number = ch["number"]
        self.authored, self.notes, self.aids = {}, {}, {}
        self.images, self.image_specs = {}, {}


def load_modules(book, cfg, chapters):
    authored_dir = (Path(book) / cfg["authored_dir"]).resolve()
    for p in (str(authored_dir), str(HERE)):  # toolkit first
        if p in sys.path:
            sys.path.remove(p)
        sys.path.insert(0, p)
    only = os.environ.get("BATCHES")
    only = set(only.split(",")) if only else None
    for chap in chapters:
        patterns = chap.ch.get("authored",
                               ["ch{N}_batch_*.py"])
        if isinstance(patterns, str):
            patterns = [patterns]
        for pattern in patterns:
            pattern = pattern.replace("{N}", str(chap.number))
            wild = any(c in pattern for c in "*?[")
            for path in sorted(authored_dir.glob(pattern)):
                if wild and only is not None and path.stem not in only:
                    continue
                mod = importlib.import_module(path.stem)
                clash = set(getattr(mod, "AUTHORED", {})) & set(chap.authored)
                assert not clash, (path.stem, clash)
                chap.authored.update(getattr(mod, "AUTHORED", {}))
                chap.notes.update(getattr(mod, "NOTES_HI", {}))
                for n, kinds in getattr(mod, "AIDS", {}).items():
                    chap.aids[n] = kinds
                for key, (name, alt) in getattr(mod, "IMAGES", {}).items():
                    chap.images[key] = (name, alt)
                for key, spec in getattr(mod, "IMAGE_SPECS", {}).items():
                    chap.image_specs[key] = spec
                    chap.images[key] = (spec["file"], spec["alt"])


# ------------------------------------------------------------------- build
class Builder:
    def __init__(self, book, cfg):
        self.book, self.cfg = book, cfg
        self.kind_labels = dict(KIND_LABELS)
        self.kind_labels.update(cfg["aid_labels"])

    def digits(self, text):
        text = str(text)
        return text.translate(DIGITS) if self.cfg["digits"] == "devanagari" \
            else text

    def english(self, text):
        return fold(text) if self.cfg["fold_english"] else text

    def cid_of(self, chap, n):
        whole, _, part = str(n).partition(".")
        prefix = chap.ch.get("prefix", f"c{chap.number}")
        width = self.cfg["id_width"]
        return f"{prefix}-{int(whole):0{width}d}" + (f"-{part}" if part else "")

    def chip_gram(self, word, form):
        over = self.cfg["gram_overrides"]
        if form in over:
            return over[form]
        text = gram_hi(word["gram"])
        if "क्त्वा/ल्यप्" in text:
            text = text.replace("क्त्वा/ल्यप्",
                                "ल्यप्" if form.endswith("्य") else "क्त्वा")
        return text

    def chip_rows(self, rows):
        rows = split_long(rows, self.cfg["max_chips_per_row"])
        return [[{"w": word_form(w["w"]), "gloss": self.english(w["gloss"]),
                  "gram": self.chip_gram(w, word_form(w["w"]))} for w in row]
                for row in rows]

    def aid_items(self, chap, n, unit):
        """The memory aids of a card, in a fixed order."""
        chosen = dict(chap.aids.get(n, {}))
        if chap.ch.get("metre") == "anustubh" and unit["type"] == "verse":
            parts = [split_pada(line) for line in unit["lines_deva"]]
            if all(parts):
                chosen["metre"] = {
                    "text": self.cfg["metre_text"],
                    "lines": [f"{a} | {b}" for a, b in parts]}
        items = []
        for kind in ORDER:
            if kind not in chosen:
                continue
            content = chosen[kind]
            item = {"aid": kind, "label": self.kind_labels[kind]}
            if isinstance(content, str):
                item["text"] = content
            else:
                item.update(content)
            if (n, kind) in chap.images:
                name, alt = chap.images[(n, kind)]
                item["image"] = {"src": "images/aids/" + name, "alt": alt}
            items.append(item)
        return items

    def build_chapter(self, chap, units):
        cfg = self.cfg
        labels = cfg["block_labels"]
        unit_name = chap.ch.get("unit") or \
            f"{cfg['labels']['unit']} {chap.number}"
        unit_title = chap.ch["title"]
        ranges = read_sections(self.book, chap.ch.get("sections"))
        ref_template = chap.ch.get("ref_template", cfg["ref_template"])
        disclaimer = chap.ch.get("source_disclaimer", cfg["source_disclaimer"])
        concepts, questions = [], []
        previous, last_in_section = {}, {}
        for unit in units:
            sec = section_of(ranges, unit["n"], unit_title)
            previous[unit["n"]] = last_in_section.get(sec)
            last_in_section[sec] = unit["n"]
        for unit in units:
            n = unit["n"]
            if n not in chap.authored and os.environ.get("PARTIAL"):
                continue  # a batch under construction
            authored = chap.authored[n]
            cid = self.cid_of(chap, n)
            section = section_of(ranges, n, unit_title)
            prev = previous[n]
            requires = authored.get(
                "requires", [self.cid_of(chap, prev)] if prev else [])
            kind = cfg["kind_labels"][unit["type"]]
            ref = ref_template.format(
                chapter=self.digits(chap.number), chapter_n=chap.number,
                kind=kind, unit=self.digits(n), unit_n=n)
            if disclaimer:
                ref += " " + disclaimer
            rows = []
            if "lead_in_tokens" in unit:
                rows.append([w for t in unit["lead_in_tokens"]
                             for w in t["words"]])
            for line in unit["lines"]:
                rows.append([w for t in line["tokens"] for w in t["words"]])
            verse_lines = list(unit["lines_deva"])
            if unit["type"] == "verse":
                verse_lines[-1] += f" ॥ {self.digits(n)} ॥"
            blocks = [
                {"key": "ref", "label": labels["ref"], "text": ref},
                {"key": "verse",
                 "label": cfg["verse_block_labels"][unit["type"]],
                 "study": True, "lines": verse_lines},
                {"key": "words", "label": labels["words"], "study": True,
                 "words": self.chip_rows(rows)},
                {"key": "hindi", "label": labels["hindi"], "study": True,
                 "text": unit["hindi"]},
                {"key": "english", "label": labels["english"], "study": True,
                 "text": self.english(unit["english"])},
                {"key": "explain", "label": labels["explain"], "study": True,
                 "text": authored["explain_hi"]},
                {"key": "aids", "label": labels["aids"], "study": True,
                 "aids": self.aid_items(chap, n, unit)},
                {"key": "note", "label": labels["note"],
                 "text": chap.notes[n]},
            ]
            concepts.append({
                "id": cid, "unit": unit_name, "unitTitle": unit_title,
                "section": section,
                "title": f"{self.digits(n)}. {authored['title']}",
                "requires": requires,
                "card": {"blocks": blocks, "rule": authored["rule"],
                         "limits": authored["limits"]},
                "question": authored["question"], "core": authored["core"],
            })
            base = {"unit": unit_name, "unitTitle": unit_title,
                    "section": section, "concept": cid}
            for question in authored["questions"]:
                q = {k: v for k, v in dict(question).items()
                     if v is not None}
                q.update(base)
                q["id"] = f"{cid}-" + ("p" if q["role"] == "pretest"
                                       else f"r{q['rung']}")
                questions.append(q)
        return unit_name, concepts, questions


def build_bank(book, cfg):
    chapters = [Chapter(cfg, ch) for ch in cfg["chapters"]]
    load_modules(book, cfg, chapters)
    builder = Builder(book, cfg)
    concepts, questions, summaries = [], [], {}
    for chap in chapters:
        data = Path(book) / cfg["data_pattern"].replace("{N}",
                                                        str(chap.number))
        if not data.exists():
            continue  # chapter not added yet
        units = json.load(open(data, encoding="utf8"))
        unit_name, c, q = builder.build_chapter(chap, units)
        concepts += c
        questions += q
        if chap.ch.get("summary"):
            summaries[unit_name] = chap.ch["summary"]
    bank = {"id": cfg["bank_id"], "book": cfg["title"],
            "labels": cfg["labels"], "summary": cfg["summary"],
            "genre": cfg["genre"], "scrollButtons": cfg["scroll_buttons"],
            "unitSummaries": summaries}
    bank.update(cfg["extra_bank_fields"])
    bank["concepts"] = concepts
    bank["questions"] = questions
    return bank, chapters


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("book", help="book directory with verse_book.json")
    ap.add_argument("--out", help="output file (default BOOK/questions.json)")
    a = ap.parse_args()
    book = Path(a.book).resolve()
    cfg = load_config(book)
    bank, _ = build_bank(book, cfg)
    target = Path(a.out) if a.out else book / "questions.json"
    target.parent.mkdir(parents=True, exist_ok=True)
    with open(target, "w", encoding="utf8") as f:
        json.dump(bank, f, ensure_ascii=False, indent=1)
    print(len(bank["concepts"]), "concepts,", len(bank["questions"]),
          "questions ->", target)


if __name__ == "__main__":
    main()
