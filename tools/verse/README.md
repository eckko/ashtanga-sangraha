# verse-study toolkit

Tools to turn any Sanskrit verse text into a Recall Quiz bank (cards with
word split, Hindi, English, explanation, memory aids, six questions per
unit). Generalised from the Charaka Samhita quiz builder; a regression test
proves that it still rebuilds that bank exactly.

Needs: Python 3 with `indic_transliteration` and Pillow (stdlib otherwise);
Node and the Chromium of Playwright only for `mermaid` pictures:

    cd tools && PUPPETEER_SKIP_DOWNLOAD=1 npm i @mermaid-js/mermaid-cli@11

## Book folder

    BOOK/
      verse_book.json              config (copy verse_book.example.json)
      data/chapterN_verses.json    final verse files (see 2.3)
      tools/authored/              hand-written batch modules (see 3)
      images/aids/                 pictures (render_images.py writes here)
      questions.json               the bank (make_bank.py writes here)

## Pipeline and tools

| Step | Command |
|---|---|
| 1 units from the study text | `python3 build_units.py WORK PART_FILE... [--chapter-numbers 1,2] [--uncertain FILE]` |
| 2 chunk (20-60 units) and draft | cut `chapterN_units.json` into `chunkK_in.json`; a drafting agent follows `briefs/DRAFT_BRIEF.md` and writes `chunkK_out.json` |
| 3 check the draft | `python3 check_chunk.py chunkK_in.json chunkK_out.json` |
| 4 independent review | a second agent writes `chunkK_review.json` (patches optional) |
| 5 apply fixes | `python3 apply_review.py WORK [--chunks 1,2] [--add-source]` |
| 6 merge | `python3 merge_chunks.py WORK BOOK/data/chapterN_verses.json` |
| 7 author the cards | batch modules in `BOOK/tools/authored/` (section 3) |
| 8 pictures | `python3 render_images.py BOOK` |
| 9 build the bank | `python3 make_bank.py BOOK [--out FILE]` |
| 10 validate | `python3 <template>/tools/validate_bank.py BOOK/questions.json` (0 errors, 0 warnings) |

`make_bank.py` environment: `PARTIAL=1` skips units that no module has
authored yet (a batch under construction); `BATCHES=ch1_batch_03,ch1_batch_04`
loads only those modules among the wildcard patterns of `authored`
(literally named files always load). Also `render_images.py` honours it.

Other files: `helpers.py` (question helpers, `accepts`), `metre.py`
(akshara count, anuṣṭubh pāda split), `gram_hi.py` (grammar label to Hindi),
`make_aid_images.py` (picture library), `verse_book.example.json`,
`briefs/` (agent briefs).

Tests (each prints PASS or the differences):

    python3 tests/test_regression.py      # rebuilds /home/claude/charaka-samhita and compares
    python3 tests/test_helpers.py
    python3 tests/test_apply_review.py
    python3 tests/test_minibook.py [TEMPLATE_DIR]   # config -> bank -> pictures -> validator
    python3 render_images.py --selftest [--shots DIR]

## 1. Config

`verse_book.example.json` lists every key with its default and meaning.
Everything book-specific lives there: bank id, title, genre, labels,
summary, per-chapter title / id prefix / unit label / summary, the `ref`
sentence (`ref_template` with `{chapter} {kind} {unit}` plus
`source_disclaimer`), `data_pattern`, `authored` globs, `sections`,
`metre`, `gram_overrides`, `aid_labels`.

## 2. Data contracts

### 2.1 Units file (`build_units.py` -> `chapterN_units.json`)
List in text order of
`{n, type: "verse"|"prose", line_ids, lines_deva, lines_iast, book_split,
book_hindi, book_english, uncertain}`. `n` is a string ("1", "66.1").
`chunkK_in.json` is a slice of it; add `lead_in` (a formula line printed
before the verse, e.g. "tatra ślokāḥ") and `flags` (tool warnings) where
needed.

### 2.2 Drafted chunk (`chunkK_out.json`)
One record per input unit, same order and `n`:

    {"n": "3",
     "lines": [{"tokens": [{"src": "athāto",       // exactly the printed token
                            "words": [{"w": "atha", "gloss": "now", "gram": "ind."},
                                      {"w": "ataḥ", "gloss": "therefore", "gram": "ind."}]}]}],
     "hindi": "...", "english": "...",
     "text_flags": [{"src": "...", "suggest": "...", "why": "..."}],
     "notes": "...", "confidence": "high|medium|low",
     "lead_in_tokens": [...], "lead_in_hindi": "...", "lead_in_english": "..."}  // only with a lead_in

Rules are in `briefs/DRAFT_BRIEF.md`; `check_chunk.py` enforces the
structure (tokens reproduce the input line, no Latin in Hindi, ...).

### 2.3 Review and final verse file
`chunkK_review.json`: `{"units": [{"n", "verdict": "ok|fix", "issues":
[{"field", "where", "problem", "fix", "severity": "error|minor",
"patch"?}]}], "summary"}`. `patch` (one object or a list):

    {"n","op":"set","field":"english","value":"..."}
    {"n","op":"replace","field":"hindi","old":"...","new":"..."}
    {"n","op":"word","match_w":"me","field":"gloss|gram|w","value":"...","occurrence":1|"all"}
    {"n","op":"append_note","text":"..."}

`apply_review.py` writes `chunkK_final.json` (draft untouched) and
`changes_K.json` (`n, field, old, new, why`), and prints issues without a
patch as MANUAL. `--add-source` copies `type, line_ids, lines_deva,
lines_iast, variants, src_flags, uncertain` from `chunkK_in.json`.

`data/chapterN_verses.json` (from `merge_chunks.py`) is the list of final
records. `make_bank.py` needs per record: `n, type, lines_deva` (one string
per printed line; a verse gets its closing "॥ n ॥" added by the builder),
`lines` (tokens, as in 2.2), `hindi`, `english`; it ignores the rest
(`notes`, `text_flags`, `variants` are for the human reviewer).

## 3. Authored batch module

A module in `BOOK/tools/authored/` (name matched by `authored`, default
`ch{N}_batch_*.py`) starts with `from helpers import mcq, match, order,
fill, multi, accepts` and defines:

    AUTHORED = {"11": {            # unit number as a STRING
        "title": "...",            # Devanagari: first words or a short topic
        "question": "...",         # one-line focus question (English)
        "rule": "...", "limits": "...",
        "explain_hi": "...",       # Hindi, 3-6 sentences
        "hook": "...", "core": False,
        "requires": [...],         # optional; default = previous unit of the same section
        "questions": [6 questions, rungs 0..5: pretest, warmup, extend,
                      discriminate, apply, transfer]}}
    NOTES_HI = {"11": "..."}       # Hindi textual note per unit (never empty)
    AIDS = {"11": {kind: content}} # kind: frame chain diagram letters seesaw story pegs
                                   #   puns anchors sandhi contrast chunks (metre is computed)
                                   # content: a Hindi string | {"steps": [..]} | {"groups": [{"label", "items"}]}
    IMAGE_SPECS = {("11", "diagram"): {"file": "x.svg", "alt": "...", "type": ..., ...}}  # optional

Optional `IMAGES = {(n, kind): (file, alt)}` links an existing picture that
no spec draws. `section` comes from the config, never from the unit.
Helpers: `mcq(role, rung, q, (right, why), [(wrong, why)...], explain, rule,
teaches=None, hint=None)`, `match(rung, q, pairs, explain, rule)`,
`order(rung, q, items, explain, rule)`, `fill(rung, q, accept, explain,
teaches, rule)`, `multi(role, rung, q, [(text, why)...], answers, explain,
rule)`. The right option of `mcq` rotates with a counter, so keep module
names stable (they load sorted by name). `accepts("इन्द्रम्")` returns the
`accept` list for `fill`: the Devanagari form first, anusvara / nasal
variants (संख्या / सङ्ख्या, final म् / ं), the IAST, then only Latin
spellings that the template's own folding (js/transliteration.js:
श ष -> sh, ऋ -> ri, ṃ -> m, ḥ -> h, long vowels short, aa -> a) does not
already unite with the list (rushi, siva, a dropped visarga). The template
compares typed answers across Devanagari / IAST / Latin anyway; the list is
a safety net. Pass more answers as extra arguments, `latin=False` for none.

## 4. Pictures

Spec types (all drawn on a parchment panel, readable on light and dark
pages): `chain {title, steps}`, `table {title, heads, rows}`, `split
{title, cols}`, `mountain {title, top, bottom}` and

    {"file": "x.svg", "alt": "...", "type": "mermaid", "code": "<mermaid source>"}

for mermaid `flowchart`/`graph`, `mindmap`, `timeline`, `pie`,
`quadrantChart` and `xychart-beta` (bar and line graphs). Text is pure SVG
(no foreignObject), no external fonts, the font stack ends in FreeSans so
Devanagari renders on a bare machine. Results are cached by a hash of the
code in `~/.cache/verse-study/mermaid` (env `VERSE_STUDY_CACHE`); a mermaid
error stops the run with mermaid's own message. Chromium: env
`PUPPETEER_EXECUTABLE_PATH`, else searched under `/opt/pw-browsers`.

Writing diagrams that stay legible at 360 px width (checked by looking at
screenshots, `render_images.py --shots DIR`):
- flowchart: `TD`, or `LR` with at most 4 boxes in a row; labels in quotes,
  `<br/>` for a second line, at most about 20 characters a line.
- mindmap: write the root as plain text (`त्रिदोष`), not `root((...))`
  (the label is drawn off centre; the tool repairs it); about 12 nodes at most.
- timeline: written `timeline` becomes `timeline TD` (top to bottom).
- pie: 2 to 6 slices; xychart-beta: width 340 by 260 by default, at most
  about 6 bars; quadrantChart: short point names.
- the picture's text must be Devanagari/Hindi and match the aid text; keep
  each file under 60 KB (hard limit 80 KB, checked by `render_images.py`).
The hand-drawn Charaka pictures (quote, baton, ...) are not part of this
library; keep such files in the book's `images/aids/` and link them with
`IMAGES`.

`render_images.py BOOK` draws every IMAGE_SPEC of the authored modules
into `BOOK/images/aids/` and checks each file exists and is under 80 KB.
`make_bank.py` only links the pictures (`images/aids/<file>`); it does not
draw them.
