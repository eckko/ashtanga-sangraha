# अष्टाङ्गसंग्रह: Recall Quiz

Verse-study quiz for Vāgbhaṭa's Aṣṭāṅga Saṅgraha. **Version 9**: 1,519 cards and 9,114 questions (6 per card).
- **Sūtrasthāna 1–5**: 372 cards (one per printed verse-pair), unchanged since version 2.
- **Śārīrasthāna 1–2**: 284 cards (versions 3 and 4); in version 5 their answer giveaways were removed
  (bracketed right options, typed answers without a plain spelling). Ids unchanged.
- **Śārīrasthāna 3** (Garbhopacaraṇīya): 128 cards and **4** (Garbhavyāpad): 135 cards (version 5).
- **Śārīrasthāna 5** (Aṅgavibhāga): 241 cards (version 6).
- **Śārīrasthāna 6** (Sirāvibhāga): 141 cards (version 7). In version 7 sandhi rules in Śārīrasthāna 1–6
  also state their conditions (त् + श → च्श, optionally च्छ; त् → न् before a nasal is optional). Ids unchanged.
- **Śārīrasthāna 7** (Marmavibhāga): 94 cards (version 8).
- **Śārīrasthāna 8** (Prakṛtibhedīya): 124 cards, new in version 9. In version 9, 44 pictures in Śārīrasthāna 1–8
  were redrawn narrow so their labels read on a phone.
- Śārīrasthāna 9–12 are being added: their unit data is in `data/chapter209…212_verses.json`; modules
  `tools/authored/sh9_*`–`sh11_*` in this version are work in progress and not in the bank.

Code loads from `eckko/recall-quiz-site-template` tag **2.2.1** via jsDelivr.
Site: <https://eckko.github.io/ashtanga-sangraha/>

## What each card has
Text, word chips, Hindi and English, a short explanation, memory aids (frame, chain, letters, seesaw,
story, pegs, puns, anchors, sandhi, contrast, chunks, metre) and a picture (chain, table, split or
mermaid diagram) where it helps. Questions favour **order** and **match**; typed Devanagari answers
also accept IAST and plain-letter spelling, with at most one per card.

## How Śārīrasthāna was built
- Text: the owner's plain and sandhi-split files of Part 2 (`reference/ashtanga-sangraha/text/`).
- Word split, Hindi and English: the Part 2 layers drafted and independently reviewed on 2026-10-18
  (`reference/ashtanga-sangraha/layers-work/p02`), grouped into units with the same rule as Sūtrasthāna
  (two half-verse lines of one length = one unit; formula, colophon and prose lines alone): 1,619 lines,
  1,349 units, 172 verse and 1,177 prose. `data/part2_layer_unit_map.json` maps layer units to cards.
- Cards and questions: written in batches of 12–14 units, each batch independently reviewed and fixed.
- Medical content follows the owner's policy: exact translation, modern names and plant identifications
  as the data labels them (standard / probable / disputed), no dose, effect or advice beyond the text.

## Honest limits
- Source is a poor scan of the 1888 edition; damaged units are marked low-confidence and carry no
  questions on doubtful readings. Text corrections are conjectural and listed in each unit's `text_flags`.
- Hindi/English and explanations are AI-written and AI-reviewed, not a scholar's translation. Pegs and
  puns are the author's own mnemonics.
- Śārīrasthāna is mostly prose; one printed line is often one long sentence or list, and questions
  pick its main teaching points. Data notes cite printed lines as "line N (card M)".
- The edition's two-line pairing is kept, so verse units may run one line out of step with real verse numbers.

## Layout
`index.html` loader · `questions.json` bank · `images/aids/` pictures · `book-structure/` chapter map ·
`verse_book.json` + `data/` + `tools/verse/` + `tools/authored/` the source the bank is built from ·
`audit/`, `reference/` earlier digitisation work.

## Rebuild
```
B=$(ls tools/authored/ch*_batch_*.py tools/authored/sh[1-8]_batch_*.py | xargs -n1 basename | sed 's/.py//' | paste -sd,)
BATCHES=$B PARTIAL=1 python3 tools/verse/make_bank.py .   # questions.json of this version (Śārīra 9-12 not yet in)
python3 tools/verse/render_images.py .         # images/aids/*.svg (needs node_modules for mermaid-cli)
python3 <template-2.2.1>/tools/validate_bank.py questions.json
```
Move to another template tag: `python3 tools/set_template_tag.py TAG`.
