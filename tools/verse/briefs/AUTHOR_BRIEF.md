# Brief: author the cards and questions for a batch of verse units

You write the study content for ~10 to 15 units of a Sanskrit verse text that already has verified data (Devanagari verse, word split with
gloss and grammar, Hindi, English, notes, text flags). Read first: the toolkit README (`<TOOLS>/README.md`), `<TOOLS>/helpers.py`, and 3 or 4 finished
authored units of the example book (Charaka Samhita: `/home/claude/charaka-samhita/tools/ch1_authored.py` units 3, 5, 9, 10, and `batch_08.py`,
`batch_11.py` for list-heavy verses). Match their quality, voice and structure.

## Deliverable
ONE module `<book>/tools/authored/<prefix>_batch_NN.py` starting with `from helpers import mcq, match, order, fill, multi, accepts` that defines:
- `AUTHORED = {"11": {...}, ...}`: keys are unit numbers as STRINGS. Fields: `title` (Devanagari: the verse's opening words or a short topic),
  `question` (English, one line), `rule` (English, <=40 words), `limits` (English: what the verse does NOT say, where the reading is uncertain),
  `explain_hi` (Hindi, 3-6 sentences), `hook` (Hindi one-liner), `core` (True for ~1 in 3: key teaching verses), optional `requires`
  (ids of earlier concepts; OMIT unless a real earlier dependency exists), `questions` (list of exactly 6). Do NOT write "section".
- `NOTES_HI = {"11": "..."}`: Hindi textual note per unit: sandhi joins you checked, variants, readings that can go two ways, `text_flags`,
  damaged lines (the data's `uncertain` list). Never empty, never invented.
- `AIDS = {"11": {kind: content}}`: memory aids, only kinds that REALLY help that verse (3-6, never all). Kinds: frame chain diagram letters seesaw
  story pegs puns anchors sandhi contrast chunks (metre is automatic). Content: a Hindi string, or {"steps":[2-8 strings]}, or
  {"groups":[{"label":..,"items":[<=12]}]}. One per kind per unit. `diagram`/`chunks` reproduce the verse's own words in verse order; `seesaw`
  only for a true pair of opposites that both occur in this verse; `pegs`/`puns` are YOUR memory hooks, say so in the text ("मेरा बनाया चित्र",
  "केवल सुनने की सहायता"), never as claims about the verse.
- `IMAGE_SPECS = {("11","diagram"): {...}}`: pictures. See "Pictures and mental models".

## Pictures and mental models (the owner wants these: aim for a picture on about every second unit where a structure exists)
A picture is attached to one of the unit's aids (kind diagram, chain, contrast, seesaw, story or pegs; the key `(unit, kind)` must exist in `AIDS`).
Spec keys: `file` (unique, starts with the chapter prefix, e.g. `ch3-lepa-14.svg`), `alt` (English, accurate, names the counts/items shown), `type`,
and the type's fields. Types:
- `mermaid`: `code` = mermaid source. Use it as the mental model of the verse: `flowchart TD/LR` for causal chains, procedures and "X causes Y"
  sequences; `mindmap` for a group of related items under a head (the diseases of one suppressed urge, the six tastes); `timeline` for ordered
  periods (seasons, the day); `pie`/`xychart-beta` (graph) when the verse gives quantities or proportions IN WORDS; `quadrantChart` for 2x2 comparisons.
  Labels are short Devanagari/Hindi (<=24 characters per node, <=12 nodes), quote labels with double quotes, no IAST, no Latin letters in labels,
  no markdown or HTML in labels. The picture shows ONLY what the verse says (the verse's items in the verse's order, with the verse's relations);
  never add what the verse does not state. A made-up memory picture goes on `pegs`/`puns` and is labelled as yours.
- `chain` (title, steps[]), `table` (title, heads[a,b], rows[[a,b]]), `split` (title, cols[[head,[items]],[head,[items]]]), `mountain` (title, top[], bottom[]).
Render and look at every picture: `python3 <TOOLS>/render_images.py <book>` (writes `images/aids/`); open each new SVG's PNG screenshot if the tool gives one,
and fix legibility problems (overlong labels, tiny text, crossing arrows). Keep each file under ~60 KB.

## Questions: exactly 6 per unit, rungs 0..5, roles in order pretest, warmup, extend, discriminate, apply, transfer
Question mix (owner's preferences, in order of priority):
1. `order` questions are very good for remembering verses: arrange the words, phrases or lines of the verse (or the steps/items it lists) in the
   verse's order. Use at least one per verse unit that has a sequence of 3-6 items (lists, steps, causal chain, the order of the verse's phrases).
2. `match` (word -> meaning, term -> meaning, cause -> effect, item -> category) is the second favourite: at least one per unit when 3-5 clear pairs exist.
3. `mcq`/`multi` for discriminate, apply and transfer; sandhi-split multiple choice ("which split is right for X?") and spot-the-translation-error
   (a translation line with one wrong word) are also good: keep using them where the verse offers a real case.
4. `fill` (typing Devanagari) is the weakest kind: use at most ONE per unit, only for a short word, make the stem say "type it in Devanagari or in
   English letters (e.g. dharma)", and give `accept` through `accepts(deva, iast, ...)` so Devanagari, IAST and plain-letter ("Hinglish") spellings
   are all accepted. Never make fill the only recall of an idea.
Use >=3 distinct kinds across the six. Stems <=25 words, exactly one "?" where a question; fill stems contain "____". mcq/multi need optionExplain for every
option (the helper takes (text, why) pairs); `explain` and `rule` on every question; `teaches` on extend and transfer questions. Any term in quotes in a
stem must be defined on the card. Test what the verse and card actually say: no counting questions ("how many words"), no questions whose answer
depends on an ambiguous split or an `uncertain` line, no trivia, none answerable without the card. Transfer questions use a NEW invented example built
on a rule taught (valid Sanskrit, agreeing case/number/gender) with `teaches`. Wrong options plausible but clearly wrong from the verse/card; never two
defensible options. Do not make the right mcq option the longest more than about a third of the time; write the wrong options first at the right
option's length. Sanskrit in Devanagari only (no IAST in Sanskrit); English prose may use diacritic names (the generator folds English to plain Latin).
Hindi for explain_hi, hook, NOTES_HI and aids: natural Hindi.

## Truth rules (most important)
1. Source-bound: every factual claim follows from the unit's own data (lines_deva, words with gloss/gram, hindi, english, notes, variants, text_flags,
   uncertain) or from standard grammar. No outside claims about identity, dates or doctrine beyond the verse. Medical content: say what the verse says
   ("the verse says"), no dose, no effect, no advice beyond it, no modern diagnosis; plant/drug names are names only. Cryptic or disputed verses:
   hedge in `limits` and build no question on the disputed point.
2. Read each unit's data first. If you find the Hindi/English wrong against the Sanskrit, do NOT silently change them: list it in your final report.
3. Pitfalls found by earlier reviews: state sandhi rules exactly (visarga -> o before a voiced sound after a, a + i -> e ...); -au is not always dual;
   -tvā vs -ya; no overclaiming identity; a listed item belongs only if the verse names it; compound readings may be two-way (mark them); do not call a
   form future or past without checking the gram label in the data; sentences that run across units: say so on the card and keep each question to what
   the unit contains.

## Self-check (mandatory)
`BATCHES=<module> PARTIAL=1 python3 <TOOLS>/make_bank.py <book> --out /tmp/chk/<module>.json`, then the template validator
(`python3 <template>/tools/validate_bank.py /tmp/chk/<module>.json`): 0 errors and 0 warnings for your units (the "requires ... not an earlier concept" batch-edge
error is expected only at a batch boundary). Render your pictures and look at them. Re-read every question as a student: is the keyed answer
undeniably right and every distractor wrong by the card alone? Edit only your own module (and your own image files). Do not run git.
Final report (<=200 words): units done, validator result, translation problems found in the data, any verse you are unsure about.
