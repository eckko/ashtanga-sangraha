# Chapter map

Version 12; kinds: verse-study. Cards: Sūtrasthāna 1–5, Śārīrasthāna 1–12 and Kalpasthāna 1–8.

One entry per chapter with its topic groups.

- **Sūtrasthāna 1–5** (live since version 4): topic groups from `tools/authored/sections.py`.
  Each unit is one printed verse-pair of the 1888 Marathi-printed edition.
- **Śārīrasthāna 1–12** (new): topic groups from `tools/authored/sections_sarira.py`.
  1,619 printed lines grouped by the same rule as Sūtrasthāna (`tools/verse/build_units.py`):
  two half-verse lines of one length = one unit; formula, colophon and prose lines stand alone.
  That gives 1,349 units (172 verse, 1,177 prose). Each unit's word split, Hindi and English
  come from the reviewed Part 2 layers (`reference/ashtanga-sangraha/layers-work/p02`).

| Chapter | Title | Units | Sections |
|---|---|---|---|
| 1 | पुत्रकामीय | 146 | 15 |
| 2 | गर्भावक्रान्ति | 138 | 16 |
| 3 | गर्भोपचरणीय | 128 | 14 |
| 4 | गर्भव्यापद् | 135 | 14 |
| 5 | अङ्गविभाग | 241 | 24 |
| 6 | सिराविभाग | 141 | 16 |
| 7 | मर्मविभाग | 94 | 12 |
| 8 | प्रकृतिभेदीय | 124 | 15 |
| 9 | विकृताङ्गविज्ञानीय | 52 | 7 |
| 10 | विकृतेहाविज्ञानीय | 35 | 5 |
| 11 | विकृतव्याधिविज्ञानीय | 63 | 9 |
| 12 | दूतादिविज्ञानीय | 52 | 7 |

Kind: `verse-study` (template tag 2.2.1). Not in the bank: cover and preface.

## How to review
Open `chapters.json`: check that each section title says what its units say and that no chapter is missing.
Say yes, or name the sections to change; changes go to this same branch.

Kalpasthāna (quiz chapters 501–508, labels "कल्प अध्याय 1–8"): topic groups from
`tools/authored/sections_kalpa.py`. Units are the edition's two-line pairs of the reviewed Part 5
layer lines (`data/part5_layer_unit_map.json`).
