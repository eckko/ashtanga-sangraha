"""Question helpers for authored batch modules.

    from helpers import mcq, match, order, fill, multi, accepts

mcq / match / order / fill / multi are the helpers of the Charaka Samhita
quiz (ch1_authored.py), unchanged in behaviour. `accepts()` builds the
`accept` list of a `fill` question.

Answer positions of `mcq` rotate with a counter (`_turn`) that lives in this
module, so the keyed position depends on the order in which mcq() is called
(= the order in which make_bank.py imports the authored modules: sorted by
file name within a chapter). Keep batch file names stable to keep the keys
stable.
"""
import re
import unicodedata

from indic_transliteration import sanscript as S

_turn = [0]


def _place(right, wrongs):
    """Put the right option in a rotating position so answers are spread."""
    n = len(wrongs) + 1
    pos = _turn[0] % n
    _turn[0] += 1
    items = list(wrongs)
    items.insert(pos, right)
    return items, pos


def mcq(role, rung, q, right, wrongs, explain, rule, teaches=None,
        hint=None):
    """right and each wrong are (text, why) pairs."""
    items, pos = _place(right, wrongs)
    out = {"role": role, "rung": rung, "kind": "mcq", "q": q,
           "options": [t for t, _ in items], "answer": pos,
           "optionExplain": [("Right: " if i == pos else "") + w
                             for i, (_, w) in enumerate(items)],
           "explain": explain, "rule": rule}
    if teaches:
        out["teaches"] = teaches
    if hint:
        out["hint"] = hint
    return out


def match(rung, q, pairs, explain, rule, role="warmup", teaches=None):
    out = {"role": role, "rung": rung, "kind": "match", "q": q,
           "pairs": pairs, "explain": explain, "rule": rule}
    if teaches:
        out["teaches"] = teaches
    return out


def order(rung, q, items, explain, rule, role="warmup", teaches=None):
    out = {"role": role, "rung": rung, "kind": "order", "q": q,
           "items": items, "explain": explain, "rule": rule}
    if teaches:
        out["teaches"] = teaches
    return out


def fill(rung, q, accept, explain, teaches, rule, role="extend"):
    return {"role": role, "rung": rung, "kind": "fill", "q": q,
            "accept": accept, "explain": explain, "teaches": teaches,
            "rule": rule}


def multi(role, rung, q, options, answers, explain, rule):
    """options are (text, why) pairs; answers are the right indexes."""
    return {"role": role, "rung": rung, "kind": "multi", "q": q,
            "options": [t for t, _ in options], "answers": answers,
            "optionExplain": [w for _, w in options],
            "explain": explain, "rule": rule}


# ------------------------------------------------------------------ accepts
# What the template (js/transliteration.js, toLooseRoman) already folds when
# it compares a typed fill answer with every entry of `accept`:
#   Devanagari -> Roman (श ष -> sh, ऋ -> ri, ं ँ -> m, ः -> h, ङ ञ ण न -> n,
#   long vowels -> short), IAST marks (ś ṣ -> sh, ṛ -> ri, ṃ -> m, ḥ -> h,
#   ṅ ñ ṇ -> n, ṭ ḍ -> t d), lower case, "aa ii uu" -> "a i u", no accents.
# So "Dharma", "dharmā" and "धर्म" are one answer already. `accepts()` is a
# safety net: it adds the spellings that the folds above do NOT unite
# (anusvara against a nasal consonant: संख्य / सङ्ख्य; "rushi", "siva",
# "sankhya", a dropped visarga) and keeps the Devanagari and IAST forms
# explicitly, so the list stays right even if the template changes.

def _loose(text):
    """Python port of toLooseRoman, to see which variants are really new."""
    cons = {"क": "k", "ख": "kh", "ग": "g", "घ": "gh", "ङ": "n", "च": "c",
            "छ": "ch", "ज": "j", "झ": "jh", "ञ": "n", "ट": "t", "ठ": "th",
            "ड": "d", "ढ": "dh", "ण": "n", "त": "t", "थ": "th", "द": "d",
            "ध": "dh", "न": "n", "प": "p", "फ": "ph", "ब": "b", "भ": "bh",
            "म": "m", "य": "y", "र": "r", "ल": "l", "व": "v", "श": "sh",
            "ष": "sh", "स": "s", "ह": "h", "ळ": "l"}
    indep = {"अ": "a", "आ": "a", "इ": "i", "ई": "i", "उ": "u", "ऊ": "u",
             "ऋ": "ri", "ॠ": "ri", "ऌ": "li", "ए": "e", "ऐ": "ai", "ओ": "o",
             "औ": "au", "ऑ": "o", "ऍ": "e"}
    signs = {"ा": "a", "ि": "i", "ी": "i", "ु": "u", "ू": "u", "ृ": "ri",
             "ॄ": "ri", "ॢ": "li", "े": "e", "ै": "ai", "ो": "o", "ौ": "au",
             "ॉ": "o", "ॅ": "e"}
    ends = {"ं": "m", "ँ": "m", "ः": "h"}
    letters = list(unicodedata.normalize("NFC", str(text)))
    out = ""
    for i, c in enumerate(letters):
        if c in "़्":
            continue
        if "०" <= c <= "९":
            out += str(ord(c) - 0x966)
        elif c in cons:
            out += cons[c]
            nxt = letters[i + 1] if i + 1 < len(letters) else ""
            if nxt == "़":
                nxt = letters[i + 2] if i + 2 < len(letters) else ""
            if not (nxt == "्" or nxt in signs):
                out += "a"
        elif c in indep:
            out += indep[c]
        elif c in signs:
            out += signs[c]
        elif c in ends:
            out += ends[c]
        else:
            out += c
    out = re.sub("[ऽ।॥॰]", " ", out).lower()
    for pat, rep in (("[śṣ]", "sh"), ("ṛ|ṝ", "ri"), ("ḷ|ḹ", "li"),
                     ("[ṃṁ]", "m"), ("ḥ", "h"), ("ṅ|ñ|ṇ", "n"), ("ṭ", "t"),
                     ("ḍ", "d")):
        out = re.sub(pat, rep, out)
    out = "".join(x for x in unicodedata.normalize("NFD", out)
                  if not unicodedata.combining(x))
    return out.replace("aa", "a").replace("ii", "i").replace("uu", "u")


_CLASSES = {  # nasal -> the consonants after which it stands for anusvara
    "ङ": "कखगघङ", "ञ": "चछजझञ", "ण": "टठडढण", "न": "तथदधन", "म": "पफबभम"}
_CLASS_OF = {c: nas for nas, cs in _CLASSES.items() for c in cs}
_STOPS = "".join(_CLASSES.values())


def _nasal_variants(deva, limit=16):
    """Devanagari spellings with anusvara <-> class nasal swapped.

    संख्य <-> सङ्ख्य, गंगा <-> गङ्गा, अन्तः <-> अंतः, and word-final
    म् <-> ं (अध्यायम् <-> अध्यायं). Each site is varied independently, so
    a word with two sites gives up to four spellings (cut at `limit`)."""
    text = unicodedata.normalize("NFC", deva)
    sites = []  # (start, end, [alternatives])
    for m in re.finditer("ं(?=([" + _STOPS + "]))", text):
        sites.append((m.start(), m.end(), ["ं", _CLASS_OF[m.group(1)] + "्"]))
    for m in re.finditer("([ङञणनम])्(?=([" + _STOPS + "]))", text):
        if _CLASS_OF[m.group(2)] == m.group(1):
            sites.append((m.start(), m.end(), [m.group(0), "ं"]))
    for m in re.finditer(r"म्(?=\s|$)|ं(?=\s|$)", text):
        sites.append((m.start(), m.end(), ["म्", "ं"]))
    sites.sort()
    variants = [""]
    last = 0
    for start, end, alts in sites:
        pieces = text[last:start]
        variants = [v + pieces + a for v in variants for a in alts]
        variants = variants[:limit]
        last = end
    return [v + text[last:] for v in variants]


def _latin_variants(iast):
    """Plain-Latin spellings a learner may type for an IAST word."""
    text = unicodedata.normalize("NFC", iast).lower()
    axes = []  # lists of (pattern, [replacement alternatives])
    if re.search("[śṣ]", text):
        axes.append(("[śṣ]", ["sh", "s"]))
    if re.search("ṛ|ṝ", text):
        axes.append(("ṛ|ṝ", ["ri", "ru"]))
    if "ṃ" in text:
        axes.append(("ṃ", ["m", "n"]))
    if "ḥ" in text:  # a typed word rarely keeps the visarga: drop it
        axes.append(("ḥ", [""]))
    if re.search("[āīū]", text):
        axes.append(("[āīū]", ["single", "double"]))
    out = [text]
    for pat, alts in axes:
        nxt = []
        for t in out:
            for a in alts:
                if a == "single":
                    nxt.append(re.sub(pat, lambda m: m.group(0).translate(
                        str.maketrans("āīū", "aiu")), t))
                elif a == "double":
                    nxt.append(re.sub(pat, lambda m: m.group(0).translate(
                        str.maketrans({"ā": "aa", "ī": "ii", "ū": "uu"})), t))
                else:
                    nxt.append(re.sub(pat, a, t))
        out = nxt
    fold = {"ṅ": "n", "ñ": "n", "ṇ": "n", "ṭ": "t", "ḍ": "d", "ḷ": "l",
            "ṝ": "ri", "ḹ": "li", "ṁ": "m"}
    done = []
    for t in out:
        t = "".join(fold.get(c, c) for c in t)
        t = "".join(x for x in unicodedata.normalize("NFD", t)
                    if not unicodedata.combining(x))
        t = re.sub(r"\s+", " ", t).strip()
        if t not in done:
            done.append(t)
    return done


def _to_iast(deva):
    return S.transliterate(unicodedata.normalize("NFC", deva), S.DEVANAGARI,
                           S.IAST)


def accepts(deva, iast=None, *extra, latin=True):
    """The `accept` list of a `fill` question.

    deva   the main answer in Devanagari (it stays first: the template shows
           accept[0] as "Accepted answer").
    iast   its IAST spelling; computed from `deva` when None.
    extra  further acceptable answers (Devanagari or Latin): another printed
           sandhi form, a synonym. Devanagari extras get the same nasal
           variants.
    latin  False: no plain-Latin ("Hinglish") variants.

    Order: Devanagari (+ nasal variants), IAST, then only those Latin
    spellings whose template fold (toLooseRoman) is not yet covered, so
    "dharma" is not listed three times. Duplicates are removed.
    """
    out, seen = [], set()

    def add(s):
        s = unicodedata.normalize("NFC", s).strip()
        if s and s not in seen:
            seen.add(s)
            out.append(s)

    devas = [deva] + [e for e in extra if re.search("[ऀ-ॿ]", e)]
    others = [e for e in extra if not re.search("[ऀ-ॿ]", e)]
    for d in devas:
        for v in _nasal_variants(d):
            add(v)
    iasts = [iast if iast else _to_iast(deva)]
    iasts += [_to_iast(e) for e in devas[1:]]
    for i in iasts:
        add(i)
    for o in others:
        add(o)
    if latin:
        covered = {_loose(x) for x in out}
        for i in iasts:
            for cand in _latin_variants(i):
                key = _loose(cand)
                if key not in covered:
                    covered.add(key)
                    add(cand)
    return out


if __name__ == "__main__":
    for word in ("अध्यायम्", "सङ्ख्या", "ऋषिः", "शरण्यम्"):
        print(word, accepts(word))
