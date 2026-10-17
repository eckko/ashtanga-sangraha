# अष्टाङ्गसंग्रह — सूत्रस्थान (अध्याय १–५): Recall Quiz

Verse-study quiz for Vāgbhaṭa's Aṣṭāṅga Saṅgraha, Sūtrasthāna chapters 1–5:
372 cards (one per printed verse-pair), 6 questions each (2,232 in all).
Code loads from `eckko/recall-quiz-site-template` tag **2.2.1** via jsDelivr.

## What each card has
Verse, word chips, Hindi and English, a short explanation, memory aids
(frame, chain, letters, seesaw, story, pegs, puns, anchors, sandhi,
contrast, chunks, metre) and a picture (chain, table, split or mermaid
diagram) where it helps. Questions favour **order** and **match**; typed
Devanagari answers also accept IAST and plain-letter (Hinglish) spelling,
with at most one per card; mcq, multi, sandhi-split and spot-the-error remain.

## Honest limits
- Source is a poor scan of the 1888 edition; damaged units are marked
  low-confidence and carry no questions on doubtful readings. Many text
  corrections are conjectural and listed in `data/*_verses.json` `text_flags`.
- Hindi/English and explanations are AI-written and AI-reviewed, not a
  scholar's translation. Pegs and puns are the author's own mnemonics.
- The edition's two-line pairing is kept, so it may run one line out of step
  with real verse numbers (chapters 1, 2, 4, 5 and parts of 3).
- Verse order is not visible in radial mind-map pictures.

## Layout
`index.html` loader · `questions.json` bank · `images/aids/` pictures ·
`book-structure/` chapter map · `verse_book.json` + `data/` + `tools/verse/`
+ `tools/authored/` the source the bank is built from · `audit/`, `reference/`
earlier digitisation work.

## Rebuild
```
python3 tools/verse/make_bank.py .          # questions.json
python3 tools/verse/render_images.py .      # images/aids/*.svg (needs node_modules for mermaid-cli)
python3 <template-2.2.1>/tools/validate_bank.py questions.json
```
Move to another template tag: `python3 tools/set_template_tag.py TAG`.
