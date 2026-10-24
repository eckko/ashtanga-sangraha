from helpers import mcq, match, order, fill, multi, accepts


def T(q, teaches):
    q["teaches"] = teaches
    return q


AUTHORED = {}

# ---------------------------------------------------------------- unit 28
AUTHORED["28"] = {
    "title": "वातपित्तश्लेष्म… रेतांसि त्वबीजानि",
    "question": "Which kinds of semen (retas) does unit 28 call seedless (abīja)?",
    "rule": ("Semens (retas) that are Vāta, Pitta, Śleṣma (Kapha), corpse-smelling, knot, pus, wasted, or "
             "urine-and-faeces are seedless (abīja), probably meaning not capable of conception."),
    "limits": ("The compound is read as eight members, कुणपगन्धि and मूत्रपुरीष each one. 'Not capable of conception' "
               "is only the probable sense of abīja. The unit says nothing of causes; any pairing with the next units "
               "is not stated here."),
    "explain_hi": ("यह गद्य-पंक्ति एक लम्बे समास में दोषयुक्त रेतस् (वीर्य) के प्रकार गिनाती है: वात, पित्त, श्लेष्मा (कफ), "
                   "कुणपगन्धि (शव जैसी गन्ध वाला), ग्रन्थि (गाँठ), पूय (मवाद), क्षीण (घटा हुआ) और मूत्र-पुरीष वाला। "
                   "ऐसे सभी रेतस् ‘अबीज’ यानी बीजहीन होते हैं; सम्भावित अर्थ है कि वे गर्भ धारण कराने योग्य नहीं। "
                   "‘त्वबीजानि’ में तु + अबीजानि की सन्धि है (उ + अ → व)। "
                   "आगे की इकाइयाँ सम्भवतः इन्हीं प्रकारों को बताती हैं, पर यह जोड़ यहाँ नहीं कहा गया।"),
    "hook": "वात से मूत्र-पुरीष तक: दोषयुक्त रेतस् अबीज।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "What does unit 28 say the faulty semens (retas) it lists are?",
            ("Seedless (abīja)", "त्वबीजानि भवन्ति: they are seedless."),
            [("Pure (śuddha)", "Pure is said of ārtava in unit 22, not of these semens."),
             ("Easily curable", "No cure is spoken of in this unit."),
             ("Like hare's blood", "That simile belongs to pure ārtava in unit 22.")],
            "All the listed semens are called seedless (abīja).",
            "अबीज = अ + बीज: without seed."),
        order(1, "Put these members of unit 28's long compound in their printed order.",
              ["वात", "श्लेष्म", "कुणपगन्धि", "पूय", "मूत्रपुरीष"],
              "The compound runs: Vāta, Pitta, Śleṣma, corpse-smelling, knot, pus, wasted, urine-and-faeces, then रेतांसि.",
              "The three doṣas come first, then the corpse-smelling, knot, pus, wasted and urine-and-faeces kinds."),
        T(match(2, "Match each member of unit 28 to its meaning on the card.",
                [["कुणपगन्धि", "corpse-smelling"], ["ग्रन्थि", "knot"], ["पूय", "pus"], ["क्षीण", "wasted"],
                 ["अबीज", "seedless"]],
                "Four members of the list and the verdict on them all.",
                "कुणपगन्धि, ग्रन्थि, पूय, क्षीण, अबीज.", role="extend"),
          "कुणपगन्धि is one member: कुणप (corpse) + गन्धि (smelling)."),
        mcq("discriminate", 3, "Which split of त्वबीजानि is right?",
            ("तु + अबीजानि", "उ before a different vowel becomes व्: तु + अ → त्व."),
            [("त्व + बीजानि", "त्व is not a word of the card, and बीजानि would drop the negating अ."),
             ("तु + बीजानि", "Without अ the word would mean seeds, and तु would stay before ब."),
             ("ता + अबीजानि", "आ + अ would give ताबीजानि.")],
            "तु (but) + अबीजानि (seedless).",
            "उ + a different vowel → व् + that vowel."),
        mcq("apply", 4, "A semen sample smells like a corpse. By unit 28, how is it counted?",
            ("As seedless", "कुणपगन्धि is one member of the list called अबीजानि."),
            [("As pure semen", "Corpse-smelling is one of the faulty kinds, not purity."),
             ("As a fertile seed", "The unit calls every listed kind seedless."),
             ("As an ārtava fault", "The unit speaks of retas, semen.")],
            "Corpse-smelling (कुणपगन्धि) semen is in the list, so it is seedless.",
            "Every member of the list → अबीज."),
        T(mcq("transfer", 5, "By the rule of त्वबीजानि, how is मधु + अस्ति written when joined?",
              ("मध्वस्ति", "उ + अ → व् + अ, as in तु + अबीजानि."),
              [("मधूस्ति", "उ + अ does not give ऊ."),
               ("मधोस्ति", "उ + अ does not give ओ."),
               ("मधुवस्ति", "The उ itself turns into व्; it does not stay.")],
              "तु + अबीजानि → त्वबीजानि; so मधु + अस्ति → मध्वस्ति.",
              "उ + a different vowel → व् + that vowel."),
          "A final उ before a different vowel becomes व्."),
    ],
}

# ---------------------------------------------------------------- unit 29
AUTHORED["29"] = {
    "title": "तत्र तनु रूक्षं फेनिलम्",
    "question": "By unit 29, what is the semen like that is discharged by Vāta?",
    "rule": ("Among these, by Vāta it is discharged thin, rough, frothy, reddish, scanty, interrupted, with pain, "
             "and after a long time."),
    "limits": ("The subject (semen) is not named; only the neuter adjectives show it. The unit gives signs only, "
               "no treatment."),
    "explain_hi": ("‘तत्र’ यानी उनमें: अब एक प्रकार के लक्षण। वात के कारण वह (वीर्य) पतला, रूखा, झागदार, लालिमा लिए, थोड़ा, "
                   "टूट-टूटकर, पीड़ा के साथ और देर से निकलता है। "
                   "कर्ता का नाम नहीं, केवल नपुंसकलिङ्ग विशेषण उसे दिखाते हैं। ‘अरुण’ यानी भोर जैसा लाल। "
                   "‘चिराच्च’ में चिरात् + च की सन्धि है (त् + च → च्च)।"),
    "hook": "वात का वीर्य: पतला, रूखा, झागदार, देर से और दर्द से।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 29, by what is the thin, rough, frothy semen discharged?",
            ("By Vāta (वातेन)", "निषिच्यते वातेन: it is discharged by Vāta."),
            [("By Pitta (पित्तेन)", "Pitta comes in unit 30."),
             ("By blood (रक्तेन)", "Blood gives the corpse-smelling kind in unit 31."),
             ("By Śleṣma (श्लेष्मणा)", "Śleṣma gives the marrow-mixed kind in unit 30.")],
            "The line ends: it is discharged by Vāta.",
            "वातेन = by Vāta."),
        order(1, "Put these signs of unit 29 in their printed order.",
              ["तनु", "रूक्षम्", "फेनिलम्", "विच्छिन्नम्", "सरुजम्"],
              "Thin, rough, frothy (then reddish, scanty), interrupted, with pain.",
              "तनु → रूक्षम् → फेनिलम् → … → विच्छिन्नम् → सरुजम्."),
        T(match(2, "Match each word of unit 29 to its meaning on the card.",
                [["तनु", "thin"], ["रूक्ष", "rough, dry"], ["फेनिल", "frothy"], ["अरुण", "reddish"],
                 ["सरुज", "with pain"]],
                "Five of the signs of the semen discharged by Vāta.",
                "तनु, रूक्ष, फेनिल, अरुण, सरुज.", role="extend"),
          "सरुज = स + रुज: with pain (a bahuvrīhi describing the semen)."),
        mcq("discriminate", 3, "Which split of चिराच्च is right?",
            ("चिरात् + च", "त् before च becomes च्: चिराच्च."),
            [("चिरा + च्च", "च्च is not a word."),
             ("चिराम् + च", "म् before च would give चिरां च."),
             ("चिरः + च", "A visarga before च would give चिरश्च.")],
            "चिरात् (after a long time) + च (and).",
            "त् + च → च्च."),
        multi("apply", 4, "Which of these signs does unit 29 give for the semen discharged by Vāta?",
              [("Thin", "Right: तनु."),
               ("Interrupted", "Right: विच्छिन्नम्."),
               ("With pain", "Right: सरुजम्."),
               ("Sinks somewhat in water", "That is the Śleṣma kind in unit 30."),
               ("Corpse-smelling", "That is the kind by blood in unit 31.")],
              [0, 1, 2],
              "Thin, interrupted and with pain are Vāta signs; sinking and corpse smell belong to other units.",
              "Vāta: तनु, रूक्ष, फेनिल, अरुण, अल्प, विच्छिन्न, सरुज, चिरात्."),
        T(mcq("transfer", 5, "By the rule of चिराच्च, how is तस्मात् + च written when joined?",
              ("तस्माच्च", "त् before च becomes च्."),
              [("तस्माद्च", "Before च the त् becomes च्, not द्."),
               ("तस्मान्च", "न् comes before a nasal, not before च."),
               ("तस्मात्च", "In sandhi the त् does not stay before च.")],
              "चिरात् + च → चिराच्च; so तस्मात् + च → तस्माच्च.",
              "त् + च → च्च."),
          "A final त् before च or छ becomes च्."),
    ],
}

# ---------------------------------------------------------------- unit 30
AUTHORED["30"] = {
    "title": "किंचित्पीतमपिच्छिलम्",
    "question": "What does the sure part of unit 30 say of the semen by Pitta, and of the semen by Śleṣma (Kapha)?",
    "rule": ("By Pitta it issues slightly yellow and non-slimy (the rest of that line is unclear). By Śleṣma (Kapha) it is "
             "mixed with marrow, abundant, bound, and sinks somewhat in water."),
    "limits": ("Low confidence; joins two lines. दहद्विष is unclear; नीलं वा is read 'or blue' (stray अ as a slip), अनीलं वा "
               "('or not blue') possible but unsuited. No question rests on the first line. 'Mixed with marrow' is literal "
               "and unexplained."),
    "explain_hi": ("यह इकाई दो छपी पंक्तियाँ जोड़ती है। पहली में पित्त से निकलने वाला वीर्य: थोड़ा पीला और पिच्छिलता (चिकनाहट) रहित; "
                   "आगे ‘नीलं वा’ (या नीला; ‘अनीलं वा’ भी सम्भव, पर ठीक नहीं बैठता) और अस्पष्ट शब्द ‘दहद्विष’ है; यह पंक्ति कम विश्वसनीय है। "
                   "दूसरी पंक्ति स्पष्ट है: श्लेष्मा (कफ) से वह मज्जा से मिला हुआ, बहुत, बँधा हुआ होता है और पानी में कुछ डूबता है। "
                   "‘मज्जा से मिला’ शाब्दिक अर्थ है; पाठ इसका आशय नहीं समझाता।"),
    "hook": "पित्त: थोड़ा पीला; कफ: बहुत, बँधा, पानी में डूबे।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 30, what does the semen by Śleṣma (Kapha) do in water?",
            ("It sinks somewhat", "अम्भसि किंचिन्मज्जति: it sinks somewhat in water."),
            [("It floats as froth", "Frothy is a Vāta sign in unit 29."),
             ("It dissolves at once", "Nothing of the kind is said."),
             ("It turns reddish", "Reddish is a Vāta sign in unit 29.")],
            "By Śleṣma it sinks somewhat in water.",
            "मज्जति = sinks; अम्भसि = in water."),
        order(1, "Put these words of unit 30's second line in their printed order.",
              ["मज्जोपसंसृष्टम्", "प्रभूतम्", "विबद्धम्", "अम्भसि", "किंचिन्मज्जति", "श्लेष्मणा"],
              "Mixed with marrow, abundant, bound, and in water sinks somewhat: by Śleṣma.",
              "मज्जोपसंसृष्टम् → प्रभूतम् → विबद्धम् → अम्भसि → किंचिन्मज्जति → श्लेष्मणा."),
        T(match(2, "Match each word of unit 30 to its meaning on the card.",
                [["उपसंसृष्ट", "mixed with"], ["प्रभूत", "abundant"], ["विबद्ध", "bound"], ["अम्भसि", "in water"],
                 ["मज्जति", "sinks"]],
                "Five words of the Śleṣma line, the secure part of the unit.",
                "उपसंसृष्ट, प्रभूत, विबद्ध, अम्भसि, मज्जति.", role="extend"),
          "मज्जति (sinks) is a verb; मज्ज- in मज्जोपसंसृष्ट is marrow: two different words."),
        mcq("discriminate", 3, "Which split of किंचिन्मज्जति is right?",
            ("किंचित् + मज्जति", "त् before the nasal म may become न् (optional; द् is also correct); the print has न्."),
            [("किंचि + न्मज्जति", "न्मज्जति is not a word."),
             ("किंचिन् + अज्जति", "अज्जति is not a word of the card."),
             ("किंचिम् + मज्जति", "म् + म would give म्म, not न्म.")],
            "किंचित् (somewhat) + मज्जति (sinks).",
            "त् + nasal → न् + nasal (optional; द् is also correct)."),
        mcq("apply", 4, "A semen is abundant, bound and sinks somewhat in water. By unit 30, by what does it come about?",
            ("By Śleṣma", "प्रभूतं विबद्धं … किंचिन्मज्जति श्लेष्मणा: by Śleṣma."),
            [("By Vāta", "Vāta gives the thin, scanty, frothy kind in unit 29."),
             ("By blood", "Blood gives the corpse-smelling kind in unit 31."),
             ("By Vāta and Pitta", "That pair gives the wasted kind in unit 34.")],
            "Abundant, bound and sinking somewhat in water are the Śleṣma signs of the second line.",
            "प्रभूत, विबद्ध, अम्भसि मज्जति → श्लेष्मणा."),
        T(mcq("transfer", 5, "By the rule of मज्जोपसंसृष्टम्, how is जल + उपसंसृष्टम् written when joined?",
              ("जलोपसंसृष्टम्", "अ + उ → ओ, as in मज्ज + उपसंसृष्टम्."),
              [("जलौपसंसृष्टम्", "अ + उ gives ओ, not औ."),
               ("जलूपसंसृष्टम्", "अ + उ does not give ऊ."),
               ("जलुपसंसृष्टम्", "The अ cannot simply vanish.")],
              "मज्ज + उपसंसृष्टम् → मज्जोपसंसृष्टम्; so जल + उपसंसृष्टम् → जलोपसंसृष्टम्.",
              "अ + उ → ओ."),
          "अ or आ before उ or ऊ merges into ओ."),
    ],
}

# ---------------------------------------------------------------- unit 31
AUTHORED["31"] = {
    "title": "कुणपगन्ध्यमल्पं रक्तेन",
    "question": "By unit 31, what kind of semen comes about by blood?",
    "rule": "Corpse-smelling and scanty (the semen issues) by blood (rakta).",
    "limits": ("Elliptical: subject and verb are carried over. Blood is the agent, but the line does not call it a doṣa. "
               "The printed कुणपगंध्यमल्पं has a म that the split कुणपगन्धि + अल्पम् does not show, so no question "
               "rests on अल्पम्."),
    "explain_hi": ("छोटी गद्य-पंक्ति, सूची का अगला अंग: रक्त के कारण वीर्य शव जैसी गन्ध वाला (कुणपगन्धि) और थोड़ा होता है। "
                   "कर्ता और क्रिया पिछली इकाइयों से लिए जाते हैं। "
                   "रक्त यहाँ वात, पित्त, श्लेष्मा की तरह कारण है, पर पंक्ति इसे दोष नहीं कहती। "
                   "‘रक्तेन’ तृतीया है: रक्त से, रक्त के कारण।"),
    "hook": "शव-सी गन्ध? कारण रक्त।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 31, by what does the corpse-smelling semen come about?",
            ("By blood (रक्तेन)", "कुणपगन्धि … रक्तेन: by blood."),
            [("By Vāta (वातेन)", "Vāta gives the thin, frothy kind in unit 29."),
             ("By Pitta (पित्तेन)", "Pitta gives the slightly yellow kind in unit 30."),
             ("By sannipāta", "Sannipāta gives the urine-and-faeces smell in unit 36.")],
            "Corpse-smelling semen comes about by blood.",
            "रक्तेन = by blood."),
        match(1, "Match each word of unit 31 to its meaning on the card.",
              [["कुणप", "corpse"], ["गन्धि", "smelling"], ["रक्त", "blood"]],
              "कुणप + गन्धि makes 'corpse-smelling'; रक्तेन names the cause.",
              "कुणप = corpse; गन्धि = smelling; रक्त = blood."),
        fill(2, "The word for 'blood' in unit 31 is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("रक्त", None, "रक्तेन"),
             "रक्तेन = by blood; the stem is रक्त.",
             "रक्त means blood; रक्तेन is its instrumental, 'by blood'.",
             "रक्त = blood."),
        mcq("discriminate", 3, "What does unit 31 say about blood (rakta)?",
            ("It is the agent of this kind", "रक्तेन: by blood, as Vāta and the others were before."),
            [("It is named a fourth doṣa", "The line does not call blood a doṣa."),
             ("It is the cure for this kind", "No cure is given in this unit."),
             ("It is mixed with the ārtava", "Ārtava is not named in this unit.")],
            "Blood is named as the agent only; the line calls it no doṣa.",
            "रक्तेन = by blood (agent)."),
        mcq("apply", 4, "Which member of unit 28's list carries the same word as unit 31?",
            ("कुणपगन्धि (corpse-smelling)", "Unit 31 opens with कुणपगन्धि, the word of unit 28's list."),
            [("ग्रन्थि (knot)", "ग्रन्थि is not in unit 31's line; the knot kind comes in unit 32."),
             ("पूय (pus)", "पूय is not in unit 31's line; the pus-like kind comes in unit 33."),
             ("क्षीण (wasted)", "क्षीण is not in unit 31's line; the wasted kind comes in unit 34.")],
            "The same word कुणपगन्धि stands in unit 28's list and in unit 31.",
            "कुणपगन्धि = corpse-smelling."),
        T(mcq("transfer", 5, "Built like रक्तेन, what does जलेन mean?",
              ("By or with water", "-एन on an अ-stem is the instrumental: by, with."),
              [("Of water", "That would be जलस्य (genitive)."),
               ("In water", "That would be जले (locative)."),
               ("To water", "That would be जलाय (dative).")],
              "रक्तेन = by blood; जलेन = by or with water.",
              "अ-stem + एन = instrumental singular."),
          "-एन on an अ-stem marks the instrumental singular: by, with."),
    ],
}

# ---------------------------------------------------------------- unit 32
AUTHORED["32"] = {
    "title": "ग्रन्थिभूतं वातश्लेष्मभ्याम्",
    "question": "By unit 32, what does semen become by Vāta and Śleṣma (Kapha) together?",
    "rule": "Semen become a knot (granthi) comes about by Vāta and Śleṣma (Kapha) together.",
    "limits": ("Elliptical: subject and verb are carried from the units before; this short phrase continues the list. "
               "'Knot' is literal; the unit gives no further sign and no treatment."),
    "explain_hi": ("यह भी सूची का छोटा अंग है: वात और श्लेष्मा (कफ) दोनों के कारण वीर्य ग्रन्थि (गाँठ) बना हुआ होता है। "
                   "‘ग्रन्थिभूत’ यानी गाँठ बना हुआ; यहाँ ‘भूत’ का अर्थ ‘हुआ’ है, प्राणी नहीं। "
                   "‘वातश्लेष्मभ्याम्’ तृतीया द्विवचन है: इन दोनों से। "
                   "कर्ता और क्रिया पिछली इकाइयों से लिए जाते हैं।"),
    "hook": "वात + कफ = गाँठ।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 32, what does semen become by Vāta and Śleṣma (Kapha)?",
            ("A knot (granthi)", "ग्रन्थिभूतं वातश्लेष्मभ्याम्."),
            [("Like foul pus", "That is by Pitta and Śleṣma, unit 33."),
             ("Wasted (kṣīṇa)", "That is by Vāta and Pitta, unit 34."),
             ("Corpse-smelling", "That is by blood, unit 31.")],
            "By Vāta and Śleṣma the semen becomes a knot.",
            "ग्रन्थिभूत = become a knot."),
        match(1, "Match each part of unit 32 to its meaning on the card.",
              [["ग्रन्थि", "knot"], ["भूत", "become"], ["वातश्लेष्मभ्याम्", "by Vāta and Śleṣma"]],
              "Two parts make 'become a knot'; the dual names the two causes.",
              "ग्रन्थि = knot; भूत = become; -भ्याम् = by the two."),
        T(mcq("extend", 2, "What does the ending of वातश्लेष्मभ्याम् show here?",
              ("By the two together", "-भ्याम्, instrumental dual here: by Vāta and Śleṣma."),
              [("By one of them alone", "-भ्याम् is dual, not singular."),
               ("In the two of them", "A locative dual would end in -योः."),
               ("Of many of them", "A genitive plural ends in -आम्, not -भ्याम्.")],
              "वातश्लेष्मभ्याम् = by Vāta and Śleṣma (instrumental dual).",
              "-भ्याम् = dual ending (instrumental here)."),
          "-भ्याम् is a dual ending; here it is instrumental: by the two."),
        mcq("discriminate", 3, "What does भूत mean in ग्रन्थिभूतम् of unit 32?",
            ("Having become", "ग्रन्थि + भूत: having become a knot."),
            [("A being or spirit", "That sense is in unit 18 (भूतहृत), not here."),
             ("Long ago, before", "No time is expressed here."),
             ("Not, without", "भूत does not negate.")],
            "After a noun, -भूत means 'having become' that thing.",
            "X-भूत = become X."),
        multi("apply", 4, "Which does unit 32 state?",
              [("The semen has become a knot", "Right: ग्रन्थिभूतम्."),
               ("Vāta and Śleṣma together cause it", "Right: वातश्लेष्मभ्याम्."),
               ("Pitta takes part in it", "Pitta is paired in units 33 and 34, not here."),
               ("A remedy for the knot is named", "No remedy is named in this unit.")],
              [0, 1],
              "The unit names the knot and its two causes, Vāta and Śleṣma.",
              "ग्रन्थिभूत; वात + श्लेष्मा."),
        T(mcq("transfer", 5, "Built like ग्रन्थिभूतम्, what does शिलाभूतम् mean?",
              ("Become stone", "X-भूत = become X: शिला (stone) + भूत."),
              [("A spirit of stone", "भूत after a noun here means 'become', not a being."),
               ("Broken from stone", "No breaking is expressed."),
               ("Stone of the past", "भूत is not 'past time' here.")],
              "ग्रन्थिभूत = become a knot; शिलाभूत = become stone.",
              "X-भूत = become X."),
          "-भूत after a noun means 'having become' that thing."),
    ],
}

# ---------------------------------------------------------------- unit 33
AUTHORED["33"] = {
    "title": "पूतिपूयनिभं पित्तश्लेष्मभ्याम्",
    "question": "By unit 33, what is the semen like that comes about by Pitta and Śleṣma (Kapha)?",
    "rule": "Semen resembling foul pus comes about by Pitta and Śleṣma (Kapha) together.",
    "limits": ("Elliptical, like units 31 and 32: subject and verb are carried over. The unit gives a likeness (निभ), "
               "no further sign, and no treatment."),
    "explain_hi": ("सूची का अगला अंग: पित्त और श्लेष्मा (कफ) के कारण वीर्य सड़े हुए पूय (मवाद) के समान होता है। "
                   "‘पूति’ = सड़ा, दुर्गन्धित; ‘निभ’ = समान, जैसा। "
                   "‘पित्तश्लेष्मभ्याम्’ तृतीया द्विवचन: इन दोनों से। कर्ता और क्रिया पहले से लिए जाते हैं।"),
    "hook": "पित्त + कफ = सड़े मवाद-सा।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 33, what is the semen like by Pitta and Śleṣma (Kapha)?",
            ("Like foul pus", "पूतिपूयनिभम्: resembling foul pus."),
            [("Become a knot", "The knot is by Vāta and Śleṣma, unit 32."),
             ("Corpse-smelling", "That is by blood, unit 31."),
             ("Thin and frothy", "Those are Vāta signs, unit 29.")],
            "By Pitta and Śleṣma the semen resembles foul pus.",
            "पूति = foul; पूय = pus; निभ = resembling."),
        match(1, "Match each part of पूतिपूयनिभम् to its meaning on the card.",
              [["पूति", "foul, putrid"], ["पूय", "pus"], ["निभ", "resembling"]],
              "Three parts: foul + pus + resembling.",
              "पूति, पूय, निभ."),
        T(mcq("extend", 2, "What does निभ add at the end of पूतिपूयनिभम्?",
              ("Resembling", "निभ marks likeness: resembling foul pus."),
              [("Made of", "निभ marks likeness, not material."),
               ("Free from", "That would need -रहित or a negative."),
               ("Caused by", "The cause is in the instrumental पित्तश्लेष्मभ्याम्.")],
              "पूतिपूय + निभ = resembling foul pus.",
              "X-निभ = resembling X."),
          "-निभ at the end of a compound means resembling, like."),
        mcq("discriminate", 3, "Units 32, 33 and 34 each name a pair of causes. Which pair belongs to unit 33?",
            ("Pitta and Śleṣma (Kapha)", "पित्तश्लेष्मभ्याम्."),
            [("Vāta and Śleṣma (Kapha)", "That pair is in unit 32 (knot)."),
             ("Vāta and Pitta", "That pair is in unit 34 (wasted)."),
             ("Blood and Śleṣma (Kapha)", "No such pair is named.")],
            "Unit 33's pair is Pitta and Śleṣma.",
            "पूय-like ← पित्त + श्लेष्मा."),
        multi("apply", 4, "Which does unit 33 state?",
              [("The semen resembles foul pus", "Right: पूतिपूयनिभम्."),
               ("Pitta and Śleṣma together cause it", "Right: पित्तश्लेष्मभ्याम्."),
               ("Vāta takes part in it", "Vāta is not named in this unit."),
               ("The semen has become a knot", "That is unit 32.")],
              [0, 1],
              "The unit names the pus-like semen and its two causes.",
              "पूतिपूयनिभ; पित्त + श्लेष्मा."),
        T(mcq("transfer", 5, "Built like पूतिपूयनिभम्, what does चन्द्रनिभम् mean?",
              ("Resembling the moon", "X-निभ = resembling X."),
              [("Made of the moon", "निभ marks likeness, not material."),
               ("Free of the moon", "निभ does not mean 'without'."),
               ("Caused by the moon", "निभ does not name a cause.")],
              "पूतिपूयनिभ = resembling foul pus; चन्द्रनिभ = resembling the moon.",
              "X-निभ = resembling X."),
          "-निभ after a noun means resembling that thing."),
    ],
}

# ---------------------------------------------------------------- unit 34
AUTHORED["34"] = {
    "title": "क्षीणं वातपित्ताभ्याम्",
    "question": "By unit 34, what kind of semen comes about by Vāta and Pitta?",
    "rule": "Wasted (kṣīṇa, depleted) semen comes about by Vāta and Pitta together.",
    "limits": ("Elliptical: subject and verb are carried over. 'Wasted' covers depleted or diminished; the unit gives no "
               "further sign and no treatment."),
    "explain_hi": ("सूची का अगला अंग: वात और पित्त दोनों के कारण वीर्य क्षीण (घटा हुआ, कम) होता है। "
                   "‘क्षीण’ √क्षि का भूत कृदन्त है। ‘वातपित्ताभ्याम्’ तृतीया द्विवचन: इन दोनों से। "
                   "इस प्रकार तीन जोड़े पूरे होते हैं: वात-श्लेष्मा से ग्रन्थि (इकाई ३२), पित्त-श्लेष्मा से पूय-जैसा (इकाई ३३), "
                   "वात-पित्त से क्षीण (यहाँ)।"),
    "hook": "वात + पित्त = क्षीण।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 34, what does semen become by Vāta and Pitta?",
            ("Wasted (kṣīṇa)", "क्षीणं वातपित्ताभ्याम्."),
            [("A knot (granthi)", "That is by Vāta and Śleṣma, unit 32."),
             ("Like foul pus", "That is by Pitta and Śleṣma, unit 33."),
             ("Corpse-smelling", "That is by blood, unit 31.")],
            "By Vāta and Pitta the semen is wasted.",
            "क्षीण = wasted, depleted."),
        fill(1, "The word for 'wasted' in unit 34 is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("क्षीण", None, "क्षीणम्"),
             "क्षीणम् = wasted, depleted; the stem is क्षीण.",
             "क्षीण means wasted, depleted, diminished.",
             "क्षीण = wasted.", role="warmup"),
        T(mcq("extend", 2, "What does वातपित्ताभ्याम् mean in unit 34?",
              ("By Vāta and Pitta", "-आभ्याम् on an अ-stem: instrumental dual, by the two."),
              [("Of Vāta and Pitta", "That would be वातपित्तयोः (genitive dual)."),
               ("In Vāta and Pitta", "That would also be वातपित्तयोः (locative dual)."),
               ("By Vāta or Pitta alone", "The dual names both together.")],
              "वातपित्ताभ्याम् = by Vāta and Pitta (instrumental dual).",
              "अ-stem + आभ्याम् = by the two."),
          "On an अ-stem, -आभ्याम् is the dual ending (instrumental here): by the two."),
        mcq("discriminate", 3, "Which sense of क्षीणम् fits unit 34?",
            ("Depleted, diminished", "क्षीण = wasted, depleted."),
            [("Swollen, abundant", "That is the opposite; abundant (प्रभूत) is a Śleṣma sign in unit 30."),
             ("Bound in a knot", "That is ग्रन्थिभूत, unit 32."),
             ("Foul like pus", "That is पूतिपूयनिभ, unit 33.")],
            "क्षीण means wasted, depleted, diminished.",
            "क्षीण ≠ प्रभूत."),
        multi("apply", 4, "Which does unit 34 state?",
              [("The semen is wasted", "Right: क्षीणम्."),
               ("Vāta and Pitta together cause it", "Right: वातपित्ताभ्याम्."),
               ("Śleṣma (Kapha) takes part in it", "Śleṣma is in the pairs of units 32 and 33, not here."),
               ("A treatment is given for it", "No treatment is given in this unit.")],
              [0, 1],
              "The unit names the wasted semen and its two causes.",
              "क्षीण; वात + पित्त."),
        T(mcq("transfer", 5, "Built like वातपित्ताभ्याम्, what does हस्ताभ्याम् mean?",
              ("With the two hands", "हस्त + आभ्याम्: instrumental dual, with the two hands."),
              [("In the two hands", "That would be हस्तयोः."),
               ("Of many hands", "That would be हस्तानाम्."),
               ("With one hand", "That would be हस्तेन.")],
              "वातपित्ताभ्याम् = by Vāta and Pitta; हस्ताभ्याम् = with the two hands.",
              "अ-stem + आभ्याम् = by/with the two."),
          "An अ-stem takes -आभ्याम् in the instrumental dual: by or with the two."),
    ],
}

# ---------------------------------------------------------------- unit 35
AUTHORED["35"] = {
    "title": "तदुक्तं ससाधनं प्राक्",
    "question": "What does unit 35 say has been stated before?",
    "rule": "That has been stated before, with its treatment (sādhana).",
    "limits": ("'That' is not named: it probably points to (the treatment of) the conditions just listed, stated earlier "
               "in the work, but which place is not certain. No question rests on what 'that' is."),
    "explain_hi": ("यह छोटी पंक्ति सूची के बीच एक सूचना है: ‘वह साधन (चिकित्सा) सहित पहले कहा जा चुका है।’ "
                   "‘तत्’ किसकी ओर संकेत करता है, यह नहीं बताया; सम्भवतः अभी गिनाई गई अवस्थाएँ, जिनका उपचार ग्रन्थ में पहले आया है, "
                   "पर कहाँ, यह निश्चित नहीं। ‘ससाधन’ = स + साधन, यानी उपचार सहित। "
                   "‘तदुक्तम्’ में तत् + उक्तम् की सन्धि है (त् + स्वर → द्)।"),
    "hook": "‘पहले कह चुके’: उपचार सहित।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 35, how has 'that' been stated before?",
            ("With its treatment", "ससाधनम्: with treatment (sādhana)."),
            [("Without any cure", "स-साधन means with treatment."),
             ("With a mantra", "No mantra is named in this unit."),
             ("With its signs only", "The unit says with treatment.")],
            "That has been stated before, with its treatment.",
            "ससाधन = with treatment."),
        order(1, "Put the words of unit 35 in their printed order.",
              ["तत्", "उक्तम्", "ससाधनम्", "प्राक्"],
              "That, stated, with treatment, before.",
              "तत् → उक्तम् → ससाधनम् → प्राक्."),
        T(match(2, "Match each word of unit 35 to its meaning on the card.",
                [["तत्", "that"], ["उक्त", "stated"], ["ससाधन", "with treatment"], ["प्राक्", "before, earlier"]],
                "The four words make the whole line.",
                "तत्, उक्त, ससाधन, प्राक्.", role="extend"),
          "स- at the start of a compound means 'with': ससाधन = with treatment."),
        mcq("discriminate", 3, "Which split of तदुक्तम् is right?",
            ("तत् + उक्तम्", "त् before a vowel becomes द्."),
            [("तद + उक्तम्", "अ + उ would give तदोक्तम्."),
             ("तदु + क्तम्", "क्तम् is not a word."),
             ("ता + उक्तम्", "आ + उ would give तोक्तम्.")],
            "तत् (that) + उक्तम् (stated).",
            "त् + vowel → द् + vowel."),
        mcq("apply", 4, "What does unit 35 leave unstated?",
            ("What 'that' refers to", "तत् is not named; its reference is only probable."),
            [("That it was stated", "उक्तम् says it was stated."),
             ("Whether earlier or later", "प्राक् says before, earlier."),
             ("Whether treatment came too", "ससाधनम् says it came with treatment.")],
            "The line says that something was stated earlier with treatment, but not what.",
            "तत् = that (unnamed)."),
        T(mcq("transfer", 5, "By the rule of तदुक्तम्, how is तत् + अपि written when joined?",
              ("तदपि", "त् before a vowel becomes द्."),
              [("तदापि", "No vowel is lengthened."),
               ("तत्अपि", "In sandhi the त् does not stay before a vowel."),
               ("तन्नपि", "न् comes only before a nasal.")],
              "तत् + उक्तम् → तदुक्तम्; so तत् + अपि → तदपि.",
              "त् + vowel → द् + vowel."),
          "A final त् before a vowel becomes द्."),
    ],
}

# ---------------------------------------------------------------- unit 36
AUTHORED["36"] = {
    "title": "मूत्रपुरीषगन्धि सन्निपातेन",
    "question": "By unit 36, what kind of semen comes about by sannipāta?",
    "rule": "Semen smelling of urine and faeces comes about by sannipāta (all three doṣas together).",
    "limits": ("Elliptical: subject and verb are carried over. Sannipāta is a doctrinal term for the combination of all "
               "three doṣas; no modern equivalent is given. No treatment is stated."),
    "explain_hi": ("सूची का यह अंग: सन्निपात से, यानी तीनों दोषों के एक साथ होने से, वीर्य मूत्र और मल (पुरीष) की गन्ध वाला होता है। "
                   "‘सन्निपात’ शास्त्रीय शब्द है; इसका कोई आधुनिक नाम नहीं दिया गया। "
                   "‘मूत्रपुरीषगन्धि’ = मूत्र + पुरीष + गन्धि (गन्ध वाला)। "
                   "कर्ता और क्रिया पिछली इकाइयों से लिए जाते हैं।"),
    "hook": "तीनों दोष एक साथ: मूत्र-मल की गन्ध।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 36, what does the semen smell of by sannipāta?",
            ("Urine and faeces", "मूत्रपुरीषगन्धि: smelling of urine and faeces."),
            [("A corpse", "The corpse smell is by blood, unit 31."),
             ("Foul pus", "The pus-like kind is by Pitta and Śleṣma, unit 33."),
             ("Fresh flowers", "No such smell is named.")],
            "By sannipāta the semen smells of urine and faeces.",
            "मूत्र = urine; पुरीष = faeces; गन्धि = smelling."),
        match(1, "Match each word of unit 36 to its meaning on the card.",
              [["मूत्र", "urine"], ["पुरीष", "faeces"], ["गन्धि", "smelling (of)"],
               ["सन्निपात", "the three doṣas together"]],
              "Three parts make the smell; सन्निपात names the cause.",
              "मूत्र, पुरीष, गन्धि, सन्निपात."),
        T(mcq("extend", 2, "What is sannipāta, as the card uses it?",
              ("All three doṣas together", "A doctrinal term for the combination of all three doṣas."),
              [("Vāta and Pitta only", "That pair gives the wasted kind in unit 34."),
               ("Blood mixed with Vāta", "No such pair is named."),
               ("A disease of the urine", "It is the doṣa combination, not a urinary disease.")],
              "सन्निपात = the three doṣas together.",
              "सन्निपात = all three doṣas combined."),
          "Sannipāta is the combination of all three doṣas (a doctrinal term)."),
        mcq("discriminate", 3, "Which reading of मूत्रपुरीषगन्धि is right?",
            ("Smelling of urine and faeces", "मूत्र + पुरीष + गन्धि: having their smell."),
            [("Urine and faeces without smell", "गन्धि means having the smell, not without it."),
             ("A smell that brings on urine", "No causing is expressed."),
             ("Urine that smells of pus", "पूय (pus) is not in this compound.")],
            "मूत्रपुरीषगन्धि = smelling of urine and faeces.",
            "X-गन्धि = smelling of X."),
        multi("apply", 4, "Which does unit 36 state?",
              [("The semen smells of urine and faeces", "Right: मूत्रपुरीषगन्धि."),
               ("Its cause is sannipāta", "Right: सन्निपातेन."),
               ("Its cause is blood alone", "Blood is the cause in unit 31."),
               ("Its cure is named here", "No cure is named in this unit.")],
              [0, 1],
              "The unit names the smell and the cause, sannipāta.",
              "मूत्रपुरीषगन्धि ← सन्निपात."),
        T(mcq("transfer", 5, "Built like मूत्रपुरीषगन्धि, what does पुष्पगन्धि mean?",
              ("Smelling of flowers", "X-गन्धि = smelling of X."),
              [("A flower with no smell", "गन्धि means having the smell."),
               ("A smell that kills flowers", "No killing is expressed."),
               ("Flowers and their smells", "गन्धि is not a separate noun 'smells' here.")],
              "मूत्रपुरीषगन्धि = smelling of urine and faeces; पुष्पगन्धि = smelling of flowers.",
              "X-गन्धि = smelling of X."),
          "-गन्धि at the end of a compound means 'smelling of' that thing."),
    ],
}

# ---------------------------------------------------------------- unit 37
AUTHORED["37"] = {
    "title": "आर्तवमपि शुक्रदोषैरुपसंसृष्टम्",
    "question": "What does unit 37 say of ārtava joined with the faults of śukra?",
    "rule": "Ārtava (menstrual blood) too, when joined with the faults (doṣa) of śukra (semen), is itself seedless.",
    "limits": ("Doṣa here is 'fault' of śukra (as in the list of unit 28), not the humour. No verb is printed; 'is' is "
               "understood. The unit does not list the ārtava faults separately."),
    "explain_hi": ("अब आर्तव की बात: आर्तव (मासिक रक्त) भी, जब शुक्र के दोषों से युक्त हो, तो बीजहीन ही होता है। "
                   "यहाँ ‘दोष’ का अर्थ विकार या खराबी है, जैसे इकाई २८ की सूची में; वात-पित्त-कफ वाला अर्थ नहीं। "
                   "क्रिया छपी नहीं, ‘होता है’ समझा जाता है। "
                   "सन्धियाँ: आर्तवम् + अपि → आर्तवमपि; शुक्रदोषैः + उपसंसृष्टम् → शुक्रदोषैरुपसंसृष्टम्।"),
    "hook": "शुक्र के दोष आर्तव में भी: वह भी अबीज।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 37, what is ārtava that is joined with the faults of śukra?",
            ("Seedless (abīja)", "अबीजम् एव: seedless indeed."),
            [("Pure (śuddha)", "Pure ārtava is the one of unit 22, not this one."),
             ("Easily curable", "No cure is spoken of in this unit."),
             ("Like hare's blood", "That simile is for pure ārtava in unit 22.")],
            "Ārtava too, joined with the faults of śukra, is seedless.",
            "अबीज = seedless."),
        order(1, "Put the words of unit 37 in their printed order.",
              ["आर्तवम्", "अपि", "शुक्रदोषैः", "उपसंसृष्टम्", "अबीजम्", "एव"],
              "Ārtava too, with the faults of śukra joined, seedless indeed.",
              "आर्तवम् → अपि → शुक्रदोषैः → उपसंसृष्टम् → अबीजम् → एव."),
        T(match(2, "Match each word of unit 37 to its meaning on the card.",
                [["अपि", "also"], ["शुक्रदोष", "faults of śukra"], ["उपसंसृष्ट", "joined with"], ["अबीज", "seedless"],
                 ["एव", "itself, only"]],
                "Five words carry the whole statement about ārtava.",
                "अपि, शुक्रदोष, उपसंसृष्ट, अबीज, एव.", role="extend"),
          "Doṣa in शुक्रदोष is a fault of śukra, as in unit 28's list."),
        mcq("discriminate", 3, "Which split of शुक्रदोषैरुपसंसृष्टम् is right?",
            ("शुक्रदोषैः + उपसंसृष्टम्", "A visarga after ऐ becomes र् before a vowel."),
            [("शुक्रदोषै + रुपसंसृष्टम्", "रुपसंसृष्टम् is not a word."),
             ("शुक्रदोषैर + उपसंसृष्टम्", "शुक्रदोषैर is not a full word; the ending is -ऐः."),
             ("शुक्रदोषम् + उपसंसृष्टम्", "म् + उ would give शुक्रदोषमुपसंसृष्टम्.")],
            "शुक्रदोषैः (with the faults of śukra) + उपसंसृष्टम् (joined).",
            "ऐः + vowel → ऐर् + vowel."),
        mcq("apply", 4, "In शुक्रदोषैः of unit 37, what does दोष mean?",
            ("A fault of śukra", "The card reads दोष here as fault, as in unit 28's list."),
            [("One of the three humours", "Not here: the card reads it as fault, not humour."),
             ("A treatment for śukra", "Treatment is साधन, not दोष."),
             ("The colour of the śukra", "No colour is named in this unit.")],
            "दोष = fault, flaw (of śukra) in this unit.",
            "शुक्रदोष = fault of śukra."),
        T(mcq("transfer", 5, "By the rule of शुक्रदोषैरुपसंसृष्टम्, how is बालैः + इष्टम् written when joined?",
              ("बालैरिष्टम्", "A visarga after ऐ becomes र् before the vowel इ."),
              [("बालैइष्टम्", "The visarga cannot simply drop before a vowel here."),
               ("बालैसिष्टम्", "Before a vowel this visarga becomes र्, not स्."),
               ("बालैष्टम्", "The इ of इष्टम् cannot vanish.")],
              "शुक्रदोषैः + उपसंसृष्टम् → शुक्रदोषैरुपसंसृष्टम्; so बालैः + इष्टम् → बालैरिष्टम्.",
              "ऐः + vowel → ऐर् + vowel."),
          "A visarga after ऐ (or any vowel but अ/आ) becomes र् before a vowel."),
    ],
}

# ---------------------------------------------------------------- unit 38
AUTHORED["38"] = {
    "title": "तस्य लिङ्गं नाम च पूर्ववत्",
    "question": "What does unit 38 say about the sign and name of the faulty ārtava?",
    "rule": "Its (the faulty ārtava's) sign and name are as before, that is, as for śukra.",
    "limits": ("No verb is printed. तस्य is taken as the ārtava of unit 37. 'As before' means as for śukra in the "
               "preceding units; how far back it reaches is not certain."),
    "explain_hi": ("यह छोटी पंक्ति कहती है: उस (दोषयुक्त आर्तव) का लक्षण और नाम पहले के समान हैं। "
                   "‘पूर्ववत्’ = पहले जैसा, यानी जैसे शुक्र के लिए कहा गया; यह कितनी पिछली इकाइयों तक जाता है, निश्चित नहीं। "
                   "‘तस्य’ इकाई ३७ के आर्तव की ओर संकेत करता है। "
                   "इस प्रकार आर्तव के लिए अलग सूची नहीं दी गई।"),
    "hook": "आर्तव के दोष: लक्षण और नाम वही, जो शुक्र के।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 38, how are the sign and name of the faulty ārtava given?",
            ("As before", "तस्य लिङ्गं नाम च पूर्ववत्."),
            [("In a new list", "No new list is given."),
             ("In the next chapter", "Nothing is said of a later chapter."),
             ("By a separate simile", "No simile is given here.")],
            "Its sign and name are as before.",
            "पूर्ववत् = as before."),
        order(1, "Put the words of unit 38 in their printed order.",
              ["तस्य", "लिङ्गम्", "नाम", "च", "पूर्ववत्"],
              "Of it, sign, name and, as before.",
              "तस्य → लिङ्गम् → नाम → च → पूर्ववत्."),
        T(match(2, "Match each word of unit 38 to its meaning on the card.",
                [["तस्य", "of it"], ["लिङ्ग", "sign"], ["नाम", "name"], ["पूर्ववत्", "as before"]],
                "The four words make the line.",
                "तस्य, लिङ्ग, नाम, पूर्ववत्.", role="extend"),
          "-वत् after a word means 'like, as': पूर्व + वत् = as before."),
        mcq("discriminate", 3, "To what does तस्य (of it) in unit 38 point?",
            ("The ārtava of unit 37", "The card takes तस्य as the faulty ārtava just named."),
            [("The treatment of unit 35", "That unit speaks of something stated before, not of signs."),
             ("The sannipāta of unit 36", "Sannipāta is a cause, not the thing with a sign and name."),
             ("The tree of unit 23", "The tree is a simile far back, not the subject here.")],
            "तस्य = of it, the ārtava joined with śukra's faults.",
            "तस्य → आर्तव (unit 37)."),
        mcq("apply", 4, "What does पूर्ववत् tell the reader to do in unit 38?",
            ("Use what was said before", "As before: as for śukra, how far back is not certain."),
            [("Wait for a later list", "पूर्व points back, not forward."),
             ("Treat the ārtava as pure", "Unit 37 calls it seedless."),
             ("Ignore the ārtava faults", "The unit gives them by reference, not ignores them.")],
            "पूर्ववत् sends the reader back to what was said for śukra.",
            "पूर्ववत् = as before."),
        T(mcq("transfer", 5, "Built like पूर्ववत्, what does पितृवत् mean?",
              ("Like a father", "-वत् = like, as: पितृ + वत्."),
              [("Of the father", "That would be पितुः."),
               ("For the father", "That would be पित्रे."),
               ("Before the father", "पूर्व gave 'before' in पूर्ववत्; -वत् itself means like.")],
              "पूर्ववत् = as before; पितृवत् = like a father.",
              "X-वत् = like X."),
          "-वत् added to a word makes an indeclinable: like X, as X."),
    ],
}

# ---------------------------------------------------------------- unit 39
AUTHORED["39"] = {
    "title": "तेषु कुणपग्रन्थिपूयक्षीणरेतांसि",
    "question": "By unit 39, which faulty kinds are curable with difficulty, and which are incurable?",
    "rule": ("Among these, the corpse-smelling, knot, pus and wasted semens are curable with difficulty; but the "
             "urine-and-faeces kind of śukra and ārtava is incurable, or the kuṇapa, granthi or pūya kind of ārtava."),
    "limits": ("Joins two printed lines. The second line's compounds are unmarked; the card follows the data in reading "
               "मूत्रपुरीषशुक्रार्तवं as the urine-and-faeces kind of śukra and ārtava. The kuṇapa/granthi/pūya ārtava kinds "
               "and the force of वा (or) are not certain, so no question rests on them. कुणप = कुणपगन्धि."),
    "explain_hi": ("यह इकाई दो छपी पंक्तियाँ जोड़ती है और साध्यता बताती है। पहली: उनमें कुणप (शव-गन्धी), ग्रन्थि, पूय और क्षीण "
                   "रेतस् कठिनाई से साध्य (कृच्छ्रसाधन) हैं। दूसरी: पर मूत्र-पुरीष वाला शुक्र और आर्तव असाध्य है, अथवा कुणप, "
                   "ग्रन्थि या पूय वाला आर्तव। दूसरी पंक्ति के समासों का बँटवारा छपाई में चिह्नित नहीं; यह पढ़ाई सम्भावित है, "
                   "और ‘वा’ का बल नहीं समझाया गया। ‘त्वसाध्यम्’ = तु + असाध्यम् (उ + अ → व)।"),
    "hook": "चार कठिन-साध्य; मूत्र-पुरीष वाला असाध्य।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 39, what is said of the corpse-smelling, knot, pus and wasted semens?",
            ("Curable with difficulty", "कृच्छ्रसाधनानि: curable with difficulty."),
            [("Easily curable", "कृच्छ्र means with difficulty."),
             ("Wholly incurable", "Incurable is said of the urine-and-faeces kind."),
             ("Cured by Vāta measures", "No measure is named in this unit.")],
            "These four kinds of semen are curable with difficulty.",
            "कृच्छ्रसाधन = curable with difficulty."),
        order(1, "Put these members of unit 39's first line in their printed order.",
              ["कुणप", "ग्रन्थि", "पूय", "क्षीण", "रेतांसि"],
              "Corpse-smelling, knot, pus, wasted: semens.",
              "कुणप → ग्रन्थि → पूय → क्षीण → रेतांसि."),
        T(match(2, "Match each word of unit 39 to its meaning on the card.",
                [["तेषु", "among these"], ["कृच्छ्रसाधन", "curable with difficulty"], ["असाध्य", "incurable"],
                 ["तु", "but"]],
                "These words carry the verdicts of the two lines.",
                "तेषु, कृच्छ्रसाधन, असाध्य, तु.", role="extend"),
          "असाध्य = अ + साध्य: not to be accomplished, incurable; कृच्छ्र = with difficulty."),
        mcq("discriminate", 3, "By unit 39, which kind of śukra is incurable (asādhya)?",
            ("The urine-and-faeces kind", "मूत्रपुरीष-शुक्रार्तवं तु असाध्यम्."),
            [("The wasted (kṣīṇa) kind", "Wasted semen is curable with difficulty."),
             ("The knot (granthi) kind", "Knot semen is curable with difficulty."),
             ("The pus (pūya) kind", "Pus semen is curable with difficulty.")],
            "The urine-and-faeces kind is incurable; the four of line 1 are curable with difficulty.",
            "मूत्रपुरीष → असाध्य."),
        multi("apply", 4, "By unit 39's first line, which semens may be treated, though with difficulty?",
              [("Corpse-smelling", "Right: कुणप."),
               ("Knot", "Right: ग्रन्थि."),
               ("Wasted", "Right: क्षीण."),
               ("Urine-and-faeces", "That kind is called incurable in line 2.")],
              [0, 1, 2],
              "Line 1: कुणप, ग्रन्थि, पूय, क्षीण semens are curable with difficulty.",
              "कृच्छ्रसाधन: कुणप, ग्रन्थि, पूय, क्षीण."),
        T(mcq("transfer", 5, "By the rule of त्वसाध्यम्, how is गुरु + आदेशः written when joined?",
              ("गुर्वादेशः", "उ before a different vowel becomes व्: गुरु + आ → गुर्वा."),
              [("गुरूदेशः", "उ + आ does not give ऊ."),
               ("गुरोदेशः", "उ + आ does not give ओ."),
               ("गुरुवादेशः", "The उ itself turns into व्; it does not stay.")],
              "तु + असाध्यम् → त्वसाध्यम्; so गुरु + आदेशः → गुर्वादेशः.",
              "उ + a different vowel → व् + that vowel."),
          "A final उ before a different vowel becomes व्."),
    ],
}

# ---------------------------------------------------------------- unit 40
AUTHORED["40"] = {
    "title": "तत्राद्यांस्त्रीन् शुक्रार्तवदोषान्",
    "question": "How does unit 40 say the first three faults of śukra and ārtava are to be treated?",
    "rule": ("Among these, one should treat the first three faults of śukra and ārtava each according to its own, "
             "with the treatment of the doṣa."),
    "limits": ("Which three are 'the first' is not named: presumably the Vāta, Pitta and Śleṣma kinds that open unit 28's "
               "list. Doṣa is a fault in शुक्रार्तवदोषान् and is read as the humour in दोषसाधनेन; the text does not "
               "separate the two senses. No remedy is named here."),
    "explain_hi": ("अब चिकित्सा का नियम: उनमें पहले तीन शुक्र-आर्तव दोषों को, प्रत्येक को अपने अनुसार (यथास्वम्), "
                   "दोष के साधन से ठीक करे। ‘पहले तीन’ सम्भवतः इकाई २८ की सूची के वात, पित्त, श्लेष्मा वाले प्रकार हैं; "
                   "पंक्ति नाम नहीं लेती। ‘दोष’ शब्द दो बार है: एक बार विकार के अर्थ में, एक बार (पढ़ाई के अनुसार) वात आदि के अर्थ में; "
                   "पाठ इन्हें अलग नहीं करता। ‘आद्यांस्त्रीन्’ में आद्यान् + त्रीन् की सन्धि है (न् + त → ंस्त)।"),
    "hook": "पहले तीन दोष: हर एक अपने दोष की चिकित्सा से।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 40, how is each of the first three faults to be treated?",
            ("By its own doṣa's treatment", "यथास्वं दोषसाधनेन: each according to its own."),
            [("All by one common remedy", "यथास्वम् means each according to its own."),
             ("Not at all: they are incurable", "Incurable is said of other kinds in unit 39."),
             ("By a mantra and a rite", "No mantra or rite is named here.")],
            "Each of the first three is treated by the treatment of the doṣa, according to its own.",
            "यथास्वम् = each according to its own."),
        order(1, "Put these parts of unit 40 in their printed order.",
              ["तत्र", "आद्यान् त्रीन्", "शुक्रार्तवदोषान्", "यथास्वम्", "दोषसाधनेन", "साधयेत्"],
              "Among these, the first three faults of śukra and ārtava, each its own, with the doṣa's treatment, one should treat.",
              "तत्र → आद्यान् त्रीन् → शुक्रार्तवदोषान् → यथास्वम् → दोषसाधनेन → साधयेत्."),
        T(match(2, "Match each word of unit 40 to its meaning on the card.",
                [["आद्य", "first"], ["यथास्वम्", "each according to its own"], ["दोषसाधन", "treatment of the doṣa"],
                 ["साधयेत्", "should treat"]],
                "These words make the rule of treatment.",
                "आद्य, यथास्वम्, दोषसाधन, साधयेत्.", role="extend"),
          "यथास्वम् = यथा + स्वम्: each according to its own."),
        mcq("discriminate", 3, "Which split of आद्यांस्त्रीन् is right?",
            ("आद्यान् + त्रीन्", "Final न् before त becomes anusvara + स्: आद्यांस्त्रीन्."),
            [("आद्याः + त्रीन्", "A visarga before त would give आद्यास्त्रीन्, with no anusvara."),
             ("आद्याम् + त्रीन्", "म् before त gives only anusvara: आद्यां त्रीन्, no स्."),
             ("आद्यांस् + त्रीन्", "आद्यांस् is not a word form; the accusative is आद्यान्.")],
            "आद्यान् (the first, acc. pl.) + त्रीन् (three, acc. pl.).",
            "न् + त → ंस्त."),
        multi("apply", 4, "Which does unit 40 state?",
              [("The first three faults are to be treated", "Right: आद्यांस्त्रीन् … साधयेत्."),
               ("Each is treated according to its own", "Right: यथास्वम्."),
               ("A named remedy is given", "No remedy is named in this unit."),
               ("The first three are incurable", "They are to be treated (साधयेत्).")],
              [0, 1],
              "The first three faults are treated, each according to its own, with the doṣa's treatment.",
              "आद्यान् त्रीन् … यथास्वं दोषसाधनेन साधयेत्."),
        T(mcq("transfer", 5, "By the rule of आद्यांस्त्रीन्, how is तान् + तत्र written when joined?",
              ("तांस्तत्र", "Final न् before त becomes anusvara + स्."),
              [("तान्तत्र", "न् does not stay before त in this sandhi."),
               ("तास्तत्र", "The nasal is kept as anusvara."),
               ("तांतत्र", "An स् comes in after the anusvara.")],
              "आद्यान् + त्रीन् → आद्यांस्त्रीन्; so तान् + तत्र → तांस्तत्र.",
              "न् + त → ंस्त."),
          "A final न् before त (or थ) becomes anusvara + स्."),
    ],
}

# ===================================================================== NOTES_HI
NOTES_HI = {
    "28": ("विश्वास मध्यम। लम्बा समास आठ सदस्यों की सूची पढ़ा गया: वात, पित्त, श्लेष्म, कुणपगन्धि, ग्रन्थि, पूय, क्षीण, मूत्रपुरीष; "
           "‘कुणपगन्धि’ और ‘मूत्रपुरीष’ एक-एक सदस्य। आगे की इकाइयों से जोड़ यहाँ नहीं कहा गया। ‘अबीज’ का अर्थ (गर्भ धारण कराने "
           "में असमर्थ) सम्भावित। छपा ‘भवंति’ = भवन्ति। सन्धि: तु + अबीजानि → त्वबीजानि (उ + अ → व)।"),
    "29": ("विश्वास ऊँचा। कर्ता (वीर्य) केवल नपुंसकलिङ्ग विशेषणों से ज्ञात। ‘निषिच्यते’ कर्मवाच्य: निकाला जाता है। "
           "सन्धियाँ: फेनिलम् + अरुणम् + अल्पम् → फेनिलमरुणमल्पम् (म् + स्वर); चिरात् + च → चिराच्च (त् + च → च्च)।"),
    "30": ("विश्वास कम। दो छपी पंक्तियाँ जुड़ी हैं। ‘अपिच्छिलम’ के बाद का ‘अ’ छपाई की भूल मानकर ‘नीलं वा’ (या नीला) पढ़ा गया; "
           "‘अपिच्छिलम् अनीलं वा’ भी सम्भव, पर ‘या नीला नहीं’ ठीक नहीं बैठता। ‘दहद्विष’ अस्पष्ट, बिना विभाजन और अनुवाद रखा गया "
           "(‘दहत् विषम्’ या ‘दहत् इव’ केवल अनुमान)। छपा ‘प्रवर्त्तते’ (द्वित्व) सामान्य ‘प्रवर्तते’ किया गया। ‘मज्जोपसंसृष्टंप्रभूतं’ "
           "में छपाई में शब्द जुड़े हैं। सन्धियाँ: मज्ज + उपसंसृष्टम् → मज्जोपसंसृष्टम् (अ + उ → ओ); च + अम्भसि → चाम्भसि "
           "(अ + अ → आ); किंचित् + मज्जति → किंचिन्मज्जति (त् + म → न्म, विकल्प से; द् भी शुद्ध)।"),
    "31": ("कर्ता-क्रिया पिछली इकाइयों से। छपा ‘कुणपगंध्यमल्पं’ कार्ड के विभाजन (कुणपगन्धि + अल्पम्, इ + अ → य) से पूरा नहीं मिलता: "
           "बीच का ‘म’ विभाजन में नहीं दिखता; इसलिए ‘अल्पम्’ पर कोई प्रश्न नहीं। ‘रक्त’ यहाँ कारण है, पंक्ति इसे दोष नहीं कहती।"),
    "32": ("विश्वास ऊँचा। वाक्य अधूरा, सूची का अगला अंग (ये छोटे खण्ड पहले से चलते वाक्य को आगे बढ़ाते लगते हैं)। "
           "छपा ‘ग्रंथिभूतं’ = ग्रन्थिभूतम्। ‘वातश्लेष्मभ्याम्’ तृतीया द्विवचन (श्लेष्मन् का न् -भ्याम् से पहले लुप्त)। "
           "यहाँ ‘भूत’ = हुआ, प्राणी नहीं।"),
    "33": ("विश्वास ऊँचा। ‘पूति’ = सड़ा, ‘निभ’ = समान। वाक्य अधूरा, इकाई ३२ की तरह। ‘पित्तश्लेष्मभ्याम्’ तृतीया द्विवचन। "
           "छपा ‘पूतिपूयनिभं’ = पूतिपूयनिभम्।"),
    "34": ("विश्वास ऊँचा। ‘क्षीण’ √क्षि का भूत कृदन्त (नपुं. प्रथमा एक.)। ‘वातपित्ताभ्याम्’ तृतीया द्विवचन (अ-अन्त शब्द में -आभ्याम्)। "
           "वाक्य अधूरा, इकाई ३२ की तरह।"),
    "35": ("विश्वास मध्यम। ‘तत्’ किसकी ओर संकेत करता है, यह नहीं कहा; सम्भवतः अभी गिनाई अवस्थाओं की चिकित्सा, जो ग्रन्थ में पहले "
           "कही गई (स्थान निश्चित नहीं)। ‘साधन’ = चिकित्सा। सन्धि: तत् + उक्तम् → तदुक्तम् (त् + स्वर → द्)।"),
    "36": ("विश्वास ऊँचा। ‘सन्निपात’ = तीनों दोषों का एक साथ होना, शास्त्रीय शब्द; आधुनिक नाम नहीं। ‘पुरीष’ = मल। "
           "वाक्य अधूरा, इकाई ३२ की तरह। छपा ‘गंधि’ = गन्धि।"),
    "37": ("विश्वास ऊँचा। ‘दोष’ यहाँ शुक्र का विकार है (इकाई २८ की सूची जैसा), वात आदि नहीं। क्रिया छपी नहीं। "
           "सन्धियाँ: आर्तवम् + अपि → आर्तवमपि; शुक्रदोषैः + उपसंसृष्टम् → शुक्रदोषैरुपसंसृष्टम् (ऐः + स्वर → ऐर्); "
           "उपसंसृष्टम् + अबीजम् + एव → उपसंसृष्टमबीजमेव (म् + स्वर)।"),
    "38": ("विश्वास ऊँचा। क्रिया छपी नहीं। ‘तस्य’ इकाई ३७ के आर्तव की ओर। ‘पूर्ववत्’ = जैसे शुक्र के लिए पहले कहा; कितनी इकाइयों तक, "
           "निश्चित नहीं। छपा ‘लिंगं’ = लिङ्गम्।"),
    "39": ("विश्वास मध्यम। दो छपी पंक्तियाँ जुड़ी हैं। ‘कुणप’ यहाँ इकाई २८ के ‘कुणपगन्धि’ के स्थान पर। दूसरी पंक्ति के समासों का "
           "बँटवारा चिह्नित नहीं: ‘मूत्रपुरीषशुक्रार्तव’ = मूत्र-पुरीष वाला शुक्र और आर्तव; ‘कुणपग्रन्थिपूयार्तव’ = कुणप, ग्रन्थि या "
           "पूय वाला आर्तव (पढ़ाई सम्भावित)। सन्धियाँ: तु + असाध्यम् → त्वसाध्यम् (उ + अ → व); शुक्र + आर्तवम् → शुक्रार्तवम्; "
           "पूय + आर्तवम् → पूयार्तवम् (अ + आ → आ)।"),
    "40": ("विश्वास मध्यम। ‘आद्यान् त्रीन्’ = पहले तीन; सम्भवतः इकाई २८ की सूची के वात, पित्त, श्लेष्मा (नाम नहीं लिए)। ‘दोष’ दो अर्थों में: "
           "‘शुक्रार्तवदोषान्’ में विकार, ‘दोषसाधनेन’ में (पढ़ाई के अनुसार) वात आदि दोष; पाठ इन्हें अलग नहीं करता। कर्ता नहीं कहा। "
           "सन्धियाँ: तत्र + आद्यान् → तत्राद्यान् (अ + आ → आ); आद्यान् + त्रीन् → आद्यांस्त्रीन् (न् + त → ंस्त)।"),
}

# ===================================================================== AIDS
AIDS = {
    "28": {
        "diagram": {"groups": [
            {"label": "रेतांसि (छपे क्रम में)", "items": ["वात", "पित्त", "श्लेष्म", "कुणपगन्धि", "ग्रन्थि", "पूय", "क्षीण",
                                                     "मूत्रपुरीष"]},
            {"label": "निर्णय", "items": ["तु अबीजानि भवन्ति"]}]},
        "letters": "क्रम के पहले अक्षर: वा-पि-श्ले · कु-ग्र-पू · क्षी-मू (मेरी याद-पद्धति: पहले तीन दोष, फिर पाँच विकार)।",
        "sandhi": "उ + अ → व: तु + अबीजानि → त्वबीजानि।",
    },
    "29": {
        "diagram": {"groups": [
            {"label": "वात से निकलता (छपे क्रम में)", "items": ["तनु (पतला)", "रूक्ष (रूखा)", "फेनिल (झागदार)", "अरुण (लालिमा)",
                                                            "अल्प (थोड़ा)", "विच्छिन्न (टूटा)", "सरुज (पीड़ा सहित)",
                                                            "चिरात् (देर से)"]}]},
        "sandhi": "म् + स्वर: फेनिलम् + अरुणम् + अल्पम् → फेनिलमरुणमल्पम् · त् + च → च्च: चिरात् + च → चिराच्च।",
        "chunks": "तत्र तनु रूक्षं | फेनिलमरुणमल्पं | विच्छिन्नं सरुजं | चिराच्च निषिच्यते | वातेन।",
    },
    "30": {
        "contrast": ("पित्त से (पंक्ति १, पक्का अंश): थोड़ा पीला, पिच्छिलता रहित ↔ श्लेष्मा से (पंक्ति २): मज्जा से मिला, बहुत, "
                     "बँधा, पानी में कुछ डूबता।"),
        "sandhi": ("अ + उ → ओ: मज्ज + उपसंसृष्टम् → मज्जोपसंसृष्टम् · अ + अ → आ: च + अम्भसि → चाम्भसि · "
                   "त् + म → न्म (विकल्प से; द् भी शुद्ध): किंचित् + मज्जति → किंचिन्मज्जति।"),
        "puns": "केवल सुनने की सहायता: एक ही पंक्ति में ‘मज्जा’ (मज्जा-धातु) और ‘मज्जति’ (डूबता है): दो अलग शब्द, पर ध्वनि एक-सी।",
    },
    "31": {
        "frame": "सूची का अगला अंग: कुणपगन्धि, अल्प ← रक्तेन (कर्ता-क्रिया पहले से)।",
        "contrast": "इकाई २९-३०: कारण वात, पित्त, श्लेष्मा ↔ इकाई ३१: कारण रक्त (पंक्ति इसे दोष नहीं कहती)।",
        "sandhi": "इ + अ → य: कुणपगन्धि + अल्पम् → कुणपगन्ध्यल्पम् (छपे रूप में बीच में एक ‘म’ अधिक है)।",
    },
    "32": {
        "frame": "ग्रन्थिभूतम् (गाँठ बना) ← वातश्लेष्मभ्याम् (वात और श्लेष्मा, दोनों से)।",
        "contrast": "इकाई १८: ‘भूत’ = प्राणी (भूतहृत) ↔ इकाई ३२: ‘भूत’ = हुआ (ग्रन्थिभूत)।",
        "anchors": "तीन जोड़े, हर बार एक दोष बाहर: वात+श्लेष्मा → ग्रन्थि (३२) · पित्त+श्लेष्मा → पूय-सा (३३) · वात+पित्त → क्षीण (३४) (मेरी याद-पद्धति)।",
    },
    "33": {
        "frame": "पूतिपूयनिभम् (सड़े मवाद-सा) ← पित्तश्लेष्मभ्याम् (पित्त और श्लेष्मा, दोनों से)।",
        "anchors": "इस जोड़े में वात नहीं: पित्त + श्लेष्मा (मेरी याद-पद्धति)।",
        "puns": "केवल सुनने की सहायता: ‘पूति-पूय’: दो ‘पू’ साथ-साथ, सड़ा और मवाद।",
    },
    "34": {
        "frame": "क्षीणम् (घटा हुआ) ← वातपित्ताभ्याम् (वात और पित्त, दोनों से)।",
        "contrast": "क्षीण (घटा, कम; इकाई ३४) ↔ प्रभूत (बहुत; इकाई ३० में श्लेष्मा का लक्षण)।",
        "anchors": "इस जोड़े में श्लेष्मा नहीं: वात + पित्त (मेरी याद-पद्धति)।",
    },
    "35": {
        "frame": "सूची के बीच एक सूचना: तत् (क्या, अनिश्चित) → उक्तम् (कहा गया) → ससाधनम् (उपचार सहित) → प्राक् (पहले)।",
        "sandhi": "त् + स्वर → द्: तत् + उक्तम् → तदुक्तम्।",
        "chunks": "तदुक्तं | ससाधनं | प्राक्।",
    },
    "36": {
        "contrast": {"groups": [
            {"label": "लक्षण ← कारण (इकाई २९-३६)", "items": [
                "पतला, रूखा, झागदार… ← वात", "थोड़ा पीला… ← पित्त", "मज्जा-मिश्रित, डूबता ← श्लेष्मा",
                "कुणपगन्धि ← रक्त", "ग्रन्थिभूत ← वात-श्लेष्मा", "पूय-सा ← पित्त-श्लेष्मा", "क्षीण ← वात-पित्त",
                "मूत्र-पुरीष गन्धि ← सन्निपात"]}]},
        "frame": "मूत्रपुरीषगन्धि (मूत्र-मल की गन्ध) ← सन्निपातेन (तीनों दोष एक साथ)।",
        "anchors": "अकेला दोष, फिर रक्त, फिर दो-दो, अन्त में तीनों: सन्निपात (मेरी याद-पद्धति)।",
    },
    "37": {
        "frame": "आर्तवम् अपि (आर्तव भी) + शुक्रदोषैः उपसंसृष्टम् (शुक्र के दोषों से युक्त) → अबीजम् एव (बीजहीन ही)।",
        "sandhi": ("म् + स्वर: आर्तवम् + अपि → आर्तवमपि · ऐः + स्वर → ऐर्: शुक्रदोषैः + उपसंसृष्टम् → शुक्रदोषैरुपसंसृष्टम् · "
                   "म् + स्वर: अबीजम् + एव → अबीजमेव।"),
        "contrast": "यहाँ ‘दोष’ = विकार, खराबी (शुक्र का) ↔ दूसरा अर्थ ‘दोष’ = वात, पित्त, कफ (यहाँ नहीं)।",
    },
    "38": {
        "frame": "तस्य (आर्तव का, इकाई ३७) → लिङ्गम् और नाम → पूर्ववत् (जैसे शुक्र के लिए कहा)।",
        "chunks": "तस्य | लिङ्गं नाम च | पूर्ववत्।",
        "anchors": "‘पूर्ववत्’: पीछे देखो, शुक्र की सूची ही आर्तव की (कितनी दूर तक, निश्चित नहीं)।",
    },
    "39": {
        "diagram": {"groups": [
            {"label": "कृच्छ्रसाधन (कठिनाई से साध्य)", "items": ["कुणप", "ग्रन्थि", "पूय", "क्षीण रेतस्"]},
            {"label": "असाध्य", "items": ["मूत्र-पुरीष वाला शुक्र-आर्तव", "या कुणप, ग्रन्थि, पूय वाला आर्तव (पढ़ाई सम्भावित)"]}]},
        "sandhi": ("उ + अ → व: तु + असाध्यम् → त्वसाध्यम् · अ + आ → आ: शुक्र + आर्तवम् → शुक्रार्तवम्; "
                   "पूय + आर्तवम् → पूयार्तवम्।"),
        "frame": "तेषु (उनमें) → पंक्ति १: चार कृच्छ्रसाधन → पंक्ति २: तु (पर) मूत्र-पुरीष वाला असाध्य, वा (या) …",
    },
    "40": {
        "chain": {"steps": ["तत्र: उनमें", "आद्यान् त्रीन्: पहले तीन शुक्र-आर्तव दोष", "यथास्वम्: प्रत्येक अपने अनुसार",
                            "दोषसाधनेन: दोष के साधन से", "साधयेत्: उपचार करे"]},
        "sandhi": "अ + आ → आ: तत्र + आद्यान् → तत्राद्यान् · न् + त → ंस्त: आद्यान् + त्रीन् → आद्यांस्त्रीन्।",
        "contrast": "‘शुक्रार्तवदोषान्’ में दोष = विकार ↔ ‘दोषसाधनेन’ में दोष = (पढ़ाई के अनुसार) वात आदि; पाठ अलग नहीं करता।",
    },
}

# ===================================================================== IMAGE_SPECS
IMAGE_SPECS = {
    ("28", "diagram"): {
        "file": "sh1-abija-retas-28.svg",
        "alt": ("Mindmap of unit 28: the seedless semens, eight members numbered in printed order: Vata, Pitta, Shleshma, "
                "corpse-smelling, knot, pus, wasted, urine-and-faeces."),
        "type": "mermaid",
        "code": ("mindmap\n"
                 "  अबीज रेतस्\n"
                 "    १ वात\n"
                 "    २ पित्त\n"
                 "    ३ श्लेष्म\n"
                 "    ४ कुणपगन्धि\n"
                 "    ५ ग्रन्थि\n"
                 "    ६ पूय\n"
                 "    ७ क्षीण\n"
                 "    ८ मूत्र-पुरीष\n"),
    },
    ("29", "diagram"): {
        "file": "sh1-vata-retas-29.svg",
        "alt": ("Mindmap of unit 29: the semen discharged by Vata, eight signs numbered in printed order: thin, rough, frothy, reddish, scanty, "
                "interrupted, with pain, after a long time."),
        "type": "mermaid",
        "code": ("mindmap\n"
                 "  वात से निकलता\n"
                 "    १ पतला\n"
                 "    २ रूखा\n"
                 "    ३ झागदार\n"
                 "    ४ लालिमा लिए\n"
                 "    ५ थोड़ा\n"
                 "    ६ टूटा-टूटा\n"
                 "    ७ पीड़ा सहित\n"
                 "    ८ देर से\n"),
    },
    ("30", "contrast"): {
        "file": "sh1-pitta-kapha-retas-30.svg",
        "alt": ("Split of unit 30: by Pitta (sure part) slightly yellow and non-slimy, the rest unclear; by Shleshma "
                "(Kapha) mixed with marrow, abundant, bound, sinks somewhat in water."),
        "type": "split",
        "title": "इकाई ३०: पित्त और श्लेष्मा से",
        "cols": [["पित्त से", ["थोड़ा पीला", "पिच्छिलता रहित", "शेष पाठ अस्पष्ट"]],
                 ["श्लेष्मा से", ["मज्जा से मिला", "बहुत", "बँधा हुआ", "पानी में कुछ डूबता"]]],
    },
    ("36", "contrast"): {
        "file": "sh1-retas-karana-36.svg",
        "alt": ("Table of units 29 to 36, each kind of faulty semen with its stated cause: thin and frothy by Vata; slightly "
                "yellow by Pitta; marrow-mixed by Shleshma; corpse-smelling by blood; knot by Vata and Shleshma; like pus "
                "by Pitta and Shleshma; wasted by Vata and Pitta; smelling of urine and faeces by sannipata."),
        "type": "table",
        "title": "लक्षण और कारण (इकाई २९-३६)",
        "heads": ["वीर्य का लक्षण", "कारण"],
        "rows": [["पतला, रूखा, झागदार… (२९)", "वात"],
                 ["थोड़ा पीला… (३०)", "पित्त"],
                 ["मज्जा-मिश्रित, डूबता (३०)", "श्लेष्मा"],
                 ["शव-सी गन्ध (३१)", "रक्त"],
                 ["गाँठ बना (३२)", "वात + श्लेष्मा"],
                 ["सड़े मवाद-सा (३३)", "पित्त + श्लेष्मा"],
                 ["क्षीण (३४)", "वात + पित्त"],
                 ["मूत्र-मल की गन्ध (३६)", "सन्निपात"]],
    },
    ("39", "diagram"): {
        "file": "sh1-sadhyata-39.svg",
        "alt": ("Split of unit 39: curable with difficulty, the corpse-smelling, knot, pus and wasted semens; incurable, the "
                "urine-and-faeces kind of semen and artava, or the corpse, knot or pus kind of artava (probable reading)."),
        "type": "split",
        "title": "साध्यता (इकाई ३९)",
        "cols": [["कठिनाई से साध्य", ["कुणप (शव-गन्धी)", "ग्रन्थि", "पूय", "क्षीण रेतस्"]],
                 ["असाध्य", ["मूत्र-पुरीष वाला शुक्र-आर्तव", "या कुणप-ग्रन्थि-पूय आर्तव (सम्भावित पढ़ाई)"]]],
    },
    ("40", "chain"): {
        "file": "sh1-dosha-sadhana-40.svg",
        "alt": ("Flowchart of unit 40: the first three faults of semen and artava; each according to its own; with the "
                "treatment of the dosha; one should treat."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"पहले तीन शुक्र-आर्तव दोष\"] --> B[\"यथास्वम्: प्रत्येक अपने अनुसार\"]\n"
                 "  B --> C[\"दोष के साधन से\"]\n"
                 "  C --> D[\"साधयेत्: उपचार करे\"]\n"),
    },
}
