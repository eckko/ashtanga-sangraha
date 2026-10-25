from helpers import mcq, match, order, fill, multi, accepts


AUTHORED = {}

# ---------------------------------------------------------------- unit 229
AUTHORED["229"] = {
    "title": "अतो वृद्धिक्षयौ यथास्वं",
    "question": "By unit 229, how should increase and decrease be discerned?",
    "rule": ("Therefore (अतः) one should discern (विभावयेत्) increase and decrease (वृद्धिक्षयौ), each by its own signs "
             "(यथास्वं लक्षणैः), and also other entities, corporeal and non-corporeal (मूर्तामूर्तान् भावान्)."),
    "limits": ("Low confidence, prose. The printed अपारेसंख्यातान् is not a word; 'not enumerated' (अपरिसंख्यातान्) is only a "
               "conjecture: no question on it. The long run-together token was split by the data's editor. The line does not "
               "say what 'therefore' points back to; it comes right after the measure of unit 228."),
    "explain_hi": ("यह गद्य-पंक्ति कहती है: इसलिए वृद्धि और क्षय को अपने-अपने लक्षणों से पहचानना चाहिए। "
                   "‘यथास्वम्’ का अर्थ है हर एक को उसके अपने (लक्षणों) के अनुसार। "
                   "साथ ही अन्य मूर्त (रूप वाले) और अमूर्त (रूपहीन) भावों को भी पहचानना है। "
                   "बीच का छपा शब्द ‘अपारेसंख्यातान्’ कोई शब्द नहीं; ‘अपरिसंख्यातान्’ (अनगिने) केवल अनुमानित पाठ है। "
                   "यह पंक्ति इकाई २२८ (सम धातु वाले का परिमाण) के ठीक बाद आती है; ‘अतः’ किस ओर है, यह स्पष्ट नहीं कहा गया।"),
    "hook": "बढ़ा या घटा? हर एक के अपने लक्षण देखो।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 229, by what should increase and decrease be discerned?",
            ("By each one's own signs", "यथास्वं लक्षणैः: each by its own signs."),
            [("By counting the bones", "The line names signs (लक्षणैः), not a bone count."),
             ("By the season of the year", "No season is named; the line says by signs."),
             ("By the patient's own report", "The line says by signs (लक्षणैः), not by a report.")],
            "Increase and decrease are discerned, each by its own signs.",
            "यथास्वं लक्षणैः = each by its own signs."),
        order(1, "Put these words of unit 229 (split out of sandhi) in the line's order.",
              ["अतः", "वृद्धिक्षयौ", "यथास्वम्", "लक्षणैः", "विभावयेत्", "मूर्तामूर्तान् भावान्"],
              "Therefore increase and decrease, each by its own signs, one should discern; and corporeal and "
              "non-corporeal entities. The doubtful word is left out.",
              "अतः → वृद्धिक्षयौ → यथास्वम् → लक्षणैः → विभावयेत् → मूर्तामूर्तान् भावान्."),
        match(2, "Match each word of unit 229 to its meaning.",
              [["वृद्धि", "increase"], ["क्षय", "decrease"], ["लक्षण", "sign"], ["मूर्त", "having form"],
               ["अमूर्त", "formless"]],
              "Increase and decrease are judged by signs; the entities are corporeal and non-corporeal.",
              "वृद्धि, क्षय, लक्षण, मूर्त, अमूर्त.", role="extend",
              teaches="मूर्त = having form, अमूर्त = formless: the line joins them in one compound, मूर्तामूर्त (अ + अ → आ)."),
        mcq("discriminate", 3, "Which split of लक्षणैर्विभावयेत् in unit 229 is right?",
            ("लक्षणैः + विभावयेत्", "Visarga after ऐ, before the voiced व, becomes र्: लक्षणैर्विभावयेत्."),
            [("लक्षणे + विभावयेत्", "ए before व stays: that would print लक्षणे विभावयेत्, with no ऐर्."),
             ("लक्षणैर + विभावयेत्", "लक्षणैर is not a form; the र् comes from the visarga of लक्षणैः."),
             ("लक्षणैः + र्विभावयेत्", "र्विभावयेत् is not a word; the verb is विभावयेत्.")],
            "लक्षणैः (by signs) + विभावयेत् (one should discern): ऐः before a voiced sound → ऐर्.",
            "Visarga after a vowel other than अ/आ, before a voiced sound → र्."),
        multi("apply", 4, "A student reads unit 229. Which statements fit the line?",
              [("Increase and decrease are each judged by their own signs", "Right: यथास्वं लक्षणैः."),
               ("It gives a new measure for each liquid", "No measure is given; the line speaks of signs."),
               ("It also speaks of corporeal and non-corporeal entities", "Right: मूर्तामूर्तान् भावान्."),
               ("It names the doṣa that increases first", "No doṣa is named in the line.")],
              [0, 2],
              "Increase and decrease by their own signs; also corporeal and non-corporeal entities.",
              "वृद्धिक्षयौ यथास्वं लक्षणैर्विभावयेत्; मूर्तामूर्तान् भावान्."),
        mcq("transfer", 5, "By the rule of अतः + वृद्धिक्षयौ → अतो वृद्धिक्षयौ, how is ततः + वदति (then he speaks, a new example) joined?",
            ("ततो वदति", "अः before a voiced consonant (व) becomes ओ, as अतः → अतो before वृद्धि."),
            [("ततर्वदति", "र् comes from a visarga after vowels other than अ/आ."),
             ("तता वदति", "Losing the visarga and keeping आ belongs to आः, not to अः."),
             ("ततश्वदति", "Visarga becomes श् before च or छ, not before व.")],
            "ततः + वदति = ततो वदति, like अतः + वृद्धिक्षयौ = अतो वृद्धिक्षयौ.",
            "अः + voiced consonant → ओ.",
            teaches="अः before a voiced consonant becomes ओ: अतः + वृद्धिक्षयौ → अतो वृद्धिक्षयौ."),
    ],
}

# ---------------------------------------------------------------- unit 230
AUTHORED["230"] = {
    "title": "तद्यथा",
    "question": "What does the short line तद्यथा do at unit 230?",
    "rule": "तद्यथा = तत् + यथा, 'namely': a formula that introduces examples; the examples (the list of unit 231) follow.",
    "limits": "Prose, two words; it states nothing itself. The Hindi 'वह इस प्रकार' is a literal rendering.",
    "explain_hi": ("‘तद्यथा’ एक छोटा सूत्र-वाक्य है, जिसका अर्थ है ‘जैसे कि’ या ‘वह इस प्रकार’। "
                   "इसके बाद उदाहरण आते हैं; यहाँ इकाई २३१ की सूची (मांस, कर्ण आदि के मल; वायु, बुद्धि, स्मृति आदि)। "
                   "यह तत् (वह) और यथा (जैसे) से बना है। "
                   "तत् का त्, घोष वर्ण य से पहले, द् हो जाता है: तद्यथा।"),
    "hook": "तद्यथा: अब उदाहरण सुनो।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What does तद्यथा (unit 230) do?",
            ("It introduces examples", "The data: a formula introducing examples."),
            [("It closes the whole chapter", "The chapter closes at unit 241, not here."),
             ("It names a teacher", "No teacher is named in it."),
             ("It gives a measure", "No measure is given; it has two words only.")],
            "तद्यथा = namely: examples follow.",
            "तद्यथा introduces examples."),
        mcq("warmup", 1, "What does तद्यथा mean?",
            ("Namely, as follows", "तत् (that) + यथा (as): that is as follows."),
            [("Therefore, hence", "Therefore would be अतः or तस्मात्."),
             ("Likewise, in the same way", "In the same way would be तथा."),
             ("Thus ends, so it is said", "A closing 'thus' is इति.")],
            "तद्यथा = namely, as follows.",
            "तत् + यथा = namely."),
        fill(2, "तद्यथा = तत् + ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("यथा", None, "yatha"),
             "तद्यथा = तत् (that) + यथा (as).",
             "यथा = as; with तत् it means 'that (is) as follows', namely.",
             "तत् + यथा = तद्यथा."),
        mcq("discriminate", 3, "Which split of तद्यथा is right?",
            ("तत् + यथा", "त् before the voiced य becomes द्."),
            [("तद + यथा", "There is no word तद with a final अ here; the pronoun is तत्."),
             ("तत् + अथा", "That would join as तदथा, with no य."),
             ("तद्य + था", "तद्य and था are not the words of this line.")],
            "तत् (that) + यथा (as): त् → द् before a voiced sound.",
            "त् + voiced sound → द्."),
        multi("apply", 4, "Which statements about unit 230 are right?",
              [("It contains a verb", "No verb occurs in it."),
               ("It is a prose formula, not a verse", "Right: the unit is prose."),
               ("Its तत् is the neuter pronoun 'that'", "Right: the data gives तत् n. nom. sg."),
               ("It names the examples itself", "The examples follow; this line names none.")],
              [1, 2],
              "A two-word prose formula: तत् (that) + यथा (as).",
              "तद्यथा = तत् + यथा, prose, no verb."),
        mcq("transfer", 5, "By the rule of तत् + यथा → तद्यथा, how is भगवत् + गीता joined (a new example)?",
            ("भगवद्गीता", "त् before the voiced ग becomes द्, as in तत् + यथा."),
            [("भगवत्गीता", "त् must become द् before the voiced ग."),
             ("भगवन्गीता", "न् would come before a nasal, not before ग."),
             ("भगवग्गीता", "त् does not copy the next consonant here.")],
            "भगवत् + गीता = भगवद्गीता, like तत् + यथा = तद्यथा.",
            "त् + voiced consonant → द्.",
            teaches="A final त् before a voiced sound becomes द्: तत् + यथा → तद्यथा."),
    ],
}

# ---------------------------------------------------------------- unit 231
AUTHORED["231"] = {
    "title": "मांसकर्णादिमलान्वायुबुद्धिस्मृत्यादींश्च",
    "question": "By unit 231, which examples are listed after तद्यथा?",
    "rule": ("Examples, in the accusative plural: the malas (waste products) of flesh, ear and the like (one reading), and "
             "wind (वायु), intellect (बुद्धि), memory (स्मृति) and the like. आदि leaves each list open."),
    "limits": ("Low confidence, prose. The first compound reads two ways (malas of flesh and ear, or flesh plus the ear's "
               "malas): no question on its parse. Vāyu as doṣa or plain wind is not stated. The accusative is read from the "
               "form."),
    "explain_hi": ("यह गद्य-पंक्ति इकाई २३० के ‘तद्यथा’ के बाद उदाहरण देती है। "
                   "पहला समास: मांस, कर्ण (कान) आदि के मल; इसे ‘मांस, और कान से आरम्भ होने वाले मल’ भी पढ़ा जा सकता है। "
                   "दूसरा: वायु, बुद्धि, स्मृति आदि। "
                   "दोनों द्वितीया बहुवचन में हैं; डेटा इन्हें इकाई २२९ की क्रिया ‘विभावयेत्’ (पहचाने) का कर्म मानता है। "
                   "‘आदि’ से सूची खुली रहती है; वायु दोष है या सामान्य हवा, यह नहीं कहा गया।"),
    "hook": "मांस, कान, मल; फिर वायु, बुद्धि, स्मृति।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 231, which of these is named in the second list, with vāyu?",
            ("Memory (स्मृति)", "वायुबुद्धिस्मृत्यादीन्: wind, intellect, memory and the like."),
            [("Sight (दर्शन)", "Not named; the list is वायु, बुद्धि, स्मृति."),
             ("Sleep (निद्रा)", "Not named; the list is वायु, बुद्धि, स्मृति."),
             ("Hunger (क्षुधा)", "Not named; the list is वायु, बुद्धि, स्मृति.")],
            "The second list: wind, intellect, memory and the like.",
            "वायु, बुद्धि, स्मृति, आदि."),
        order(1, "Put these items of unit 231 in the line's order.",
              ["मांस", "कर्ण", "मल", "वायु", "बुद्धि", "स्मृति"],
              "Flesh, ear and the like, malas; then wind, intellect, memory and the like.",
              "मांस → कर्ण → मल → वायु → बुद्धि → स्मृति."),
        match(2, "Match each word of unit 231 to its meaning.",
              [["कर्ण", "ear"], ["मल", "waste product"], ["वायु", "wind"], ["बुद्धि", "intellect"], ["स्मृति", "memory"]],
              "The malas of flesh, ear and the like; wind, intellect, memory and the like.",
              "कर्ण, मल, वायु, बुद्धि, स्मृति.", role="extend",
              teaches="आदि at the end of a list = 'and the like': the list is left open."),
        mcq("discriminate", 3, "Which split of स्मृत्यादींश्च in unit 231 is right?",
            ("स्मृति + आदीन् + च", "इ + आ → या; न् before च → ंश्च."),
            [("स्मृत्य + आदीन् + च", "स्मृत्य is not a word; the य् comes from the इ of स्मृति."),
             ("स्मृति + आदीः + च", "आदीः + च would give आदीश्च, with no anusvāra."),
             ("स्मृति + आदीम् + च", "आदीम् + च would give आदीं च, with no श्.")],
            "स्मृति (memory) + आदीन् (and the like) + च (and).",
            "इ + unlike vowel → य्; न् + च → ंश्च."),
        multi("apply", 4, "Which statements fit unit 231 as the data reads it?",
              [("The line has its own main verb", "No verb is printed; the data takes the items as objects of विभावयेत् in unit 229."),
               ("The listed items are in the accusative plural", "Right: both compounds end in -आन्/-ईन्, acc. pl."),
               ("It says vāyu here is the doṣa Vāta", "The data: whether doṣa or plain wind is not stated."),
               ("आदि leaves both lists open", "Right: मांसकर्णादि..., स्मृत्यादीन्: 'and the like'.")],
              [1, 3],
              "Two open lists in the accusative plural; no verb in the line.",
              "-आदि = and the like; -आन्/-ईन् = m. acc. pl."),
        mcq("transfer", 5, "By the rule of आदीन् + च → आदींश्च, how is देवान् + च (and the gods, a new example) joined?",
            ("देवांश्च", "न् before च becomes anusvāra with श् added, as आदीन् + च → आदींश्च."),
            [("देवान्च", "न् before च is not left as it is; it takes ंश्."),
             ("देवाश्च", "The nasal is not lost; it stays as anusvāra."),
             ("देवांच", "A श् is added between the anusvāra and च.")],
            "देवान् + च = देवांश्च, like आदीन् + च = आदींश्च.",
            "न् + च → ंश्च.",
            teaches="A final न् before च becomes anusvāra and a श् is added: आदीन् + च → आदींश्च."),
    ],
}

# ---------------------------------------------------------------- unit 232
AUTHORED["232"] = {
    "title": "धान्वंतरीयाः पुनः पठंति",
    "question": "By unit 232, whose reading is now introduced?",
    "rule": ("The followers of Dhanvantari (धान्वन्तरीयाः), on the other hand (पुनः), read or recite (पठन्ति): another "
             "reading is announced; its words are not in this line."),
    "limits": ("Prose; no object is stated in the line. 'School' would be a rendering; the data says only 'followers of "
               "Dhanvantari'. What they read is not in this unit, so no question asks its content."),
    "explain_hi": ("यह छोटी गद्य-पंक्ति एक दूसरा पाठ लाती है: धान्वन्तरीय, यानी धन्वन्तरि के अनुयायी, ‘पुनः’ (दूसरी ओर) पढ़ते हैं। "
                   "‘धान्वन्तरीय’ धन्वन्तरि नाम से -ईय प्रत्यय लगाकर बना है: धन्वन्तरि का, या उसका अनुयायी। "
                   "‘पठन्ति’ बहुवचन वर्तमान क्रिया है: वे पढ़ते हैं। "
                   "वे क्या पढ़ते हैं, वह इस पंक्ति में नहीं; डेटा के अनुसार वह सम्भवतः आगे की इकाइयों (२३३-२३५) में है।"),
    "hook": "अब धन्वन्तरि वालों का पाठ।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 232, who read (recite)?",
            ("The followers of Dhanvantari", "धान्वन्तरीयाः: those belonging to or following Dhanvantari."),
            [("All the physicians together", "The line names one group, the Dhanvantari followers."),
             ("The author, in his own words", "The verb is plural and names others: धान्वन्तरीयाः."),
             ("The students of grammar", "No grammarians are named.")],
            "The followers of Dhanvantari read (recite).",
            "धान्वन्तरीयाः पठन्ति."),
        match(1, "Match each word of unit 232 to its meaning.",
              [["धान्वन्तरीयाः", "followers of Dhanvantari"], ["पुनः", "on the other hand"], ["पठन्ति", "they read, recite"]],
              "The followers of Dhanvantari, on the other hand, read.",
              "धान्वन्तरीयाः, पुनः, पठन्ति."),
        mcq("extend", 2, "In धान्वन्तरीय, what does the ending -ईय add to the name Dhanvantari?",
            ("Belonging to or following him", "The data: belonging to or following Dhanvantari."),
            [("Standing against him in debate", "-ईय does not mean opposed."),
             ("Living before him in time", "-ईय says nothing of time."),
             ("Being his own teacher", "-ईय does not mean teacher.")],
            "धान्वन्तरीय = belonging to or following Dhanvantari.",
            "Name + -ईय = belonging to, following.",
            teaches="-ईय after a name = belonging to, following; the first vowel is lengthened: धन्वन्तरि → धान्वन्तरीय."),
        mcq("discriminate", 3, "What form is पठन्ति in unit 232?",
            ("Present, 'they read'", "The data: 3 pl. present of √पठ्."),
            [("Present, 'he reads'", "That would be पठति; -अन्ति is the plural."),
             ("Command, 'let them read'", "That would be पठन्तु."),
             ("Past, 'they read before'", "That would be अपठन्.")],
            "पठन्ति = they read (3 pl. present), agreeing with धान्वन्तरीयाः.",
            "-अन्ति = 3 pl. present."),
        order(4, "Put the printed words of unit 232 in the line's order.",
              ["धान्वंतरीयाः", "पुनः", "पठंति"],
              "The followers of Dhanvantari, on the other hand, read.",
              "धान्वन्तरीयाः → पुनः → पठन्ति.", role="apply"),
        mcq("transfer", 5, "By the pattern of धान्वन्तरीयाः, what does पाणिनीयाः mean (a new example)?",
            ("The followers of Pāṇini", "Name + -ईय = belonging to, following, as धन्वन्तरि → धान्वन्तरीय."),
            [("The teachers of Pāṇini", "-ईय does not name a teacher."),
             ("The opponents of Pāṇini", "-ईय does not mean opposed."),
             ("Those who came before Pāṇini", "-ईय says nothing of time.")],
            "पाणिनीयाः = followers of Pāṇini, like धान्वन्तरीयाः = followers of Dhanvantari.",
            "Name + -ईय = follower of.",
            teaches="-ईय makes 'belonging to, following': धान्वन्तरीयाः = the followers of Dhanvantari."),
    ],
}

# ---------------------------------------------------------------- unit 233
AUTHORED["233"] = {
    "title": "विलक्षणानि हि शरीराणि",
    "question": "By unit 233, what is said of bodies and of the doṣas, dhātus and malas?",
    "rule": ("For (हि) bodies are of dissimilar characteristics (विलक्षणानि), and the doṣas, dhātus and malas are always "
             "(नित्यम् एव) unsteady (चलाः)."),
    "limits": ("Prose; the copula is understood. The data's GROUPING note says it appears to be the first part of the "
               "Dhanvantari reading of unit 232, continuing to unit 235; the questions stay inside this line. No doṣa is "
               "given a modern name."),
    "explain_hi": ("यह गद्य-पंक्ति सम्भवतः धान्वन्तरीय पाठ का पहला भाग है (डेटा के अनुसार यह इकाई २३५ तक चलता है)। "
                   "‘हि’ (क्योंकि) कारण बताता है: शरीर विलक्षण हैं, यानी उनके लक्षण आपस में भिन्न हैं। "
                   "और दोष, धातु और मल नित्य ही चल (अस्थिर) हैं। "
                   "‘चलाः’ छपाई में ‘चला’ है: आः का विसर्ग घोष वर्ण द से पहले लुप्त होता है। "
                   "क्रिया ‘हैं’ समझी जाती है।"),
    "hook": "हर शरीर अलग, दोष-धातु-मल सदा चलायमान।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 233, how are the doṣas, dhātus and malas described?",
            ("Unsteady, moving", "नित्यमेव च चला दोषधातुमलाः: always unsteady."),
            [("Fixed in amount", "The line says चलाः, unsteady, not fixed."),
             ("Equal in all bodies", "Bodies are called विलक्षण, dissimilar."),
             ("Hidden from sight", "Nothing is said of sight; they are unsteady.")],
            "The doṣas, dhātus and malas are always unsteady.",
            "चलाः = unsteady, moving."),
        order(1, "Put these parts of unit 233 in the line's order.",
              ["विलक्षणानि हि", "शरीराणि", "नित्यमेव च", "चला", "दोषधातुमलाः"],
              "For bodies are dissimilar, and always unsteady are the doṣas, dhātus and malas.",
              "विलक्षणानि हि → शरीराणि → नित्यमेव च → चला → दोषधातुमलाः."),
        match(2, "Match each word of unit 233 to its meaning.",
              [["विलक्षण", "of dissimilar characteristics"], ["हि", "for (giving a reason)"], ["नित्यम्", "always"],
               ["चल", "unsteady, moving"], ["शरीर", "body"]],
              "For bodies are dissimilar, and the doṣas, dhātus and malas always unsteady.",
              "विलक्षण, हि, नित्यम्, चल, शरीर.", role="extend",
              teaches="हि = for: it marks the line as a reason."),
        mcq("discriminate", 3, "Why is चलाः printed चला before दोषधातुमलाः in unit 233?",
            ("Regular sandhi: आः loses ः before द", "आः drops its visarga before a voiced sound (the data: regular sandhi)."),
            [("The print lost its visarga by a slip of the press", "The data: regular sandhi before द, not a print slip."),
             ("The word is a feminine singular, not a plural", "The data: m. nom. pl., agreeing with दोषधातुमलाः."),
             ("Visarga turns into र् before द", "र् comes after vowels other than अ/आ.")],
            "चलाः + दोष... → चला दोष...: आः before a voiced sound drops the visarga.",
            "आः + voiced sound → आ."),
        multi("apply", 4, "Which statements fit unit 233?",
              [("Bodies are all alike in their signs", "विलक्षणानि: bodies are dissimilar."),
               ("The doṣas, dhātus and malas are always unsteady", "Right: नित्यमेव च चलाः."),
               ("हि gives the line as a reason", "Right: हि = for."),
               ("The dhātus are said to be fixed in amount", "The line calls them unsteady (चलाः).")],
              [1, 2],
              "Bodies are dissimilar; the doṣas, dhātus and malas are always unsteady; हि = for.",
              "विलक्षणानि हि शरीराणि; चलाः दोषधातुमलाः."),
        mcq("transfer", 5, "By the rule of चलाः + दोष... → चला दोष..., how is देवाः + गच्छन्ति (the gods go, a new example) joined?",
            ("देवा गच्छन्ति", "आः before a voiced sound drops the visarga, as चलाः → चला."),
            [("देवो गच्छन्ति", "ओ comes from अः, not from आः."),
             ("देवार्गच्छन्ति", "र् comes after vowels other than अ/आ."),
             ("देवाश्गच्छन्ति", "श् comes before च or छ, not before ग.")],
            "देवाः + गच्छन्ति = देवा गच्छन्ति, like चलाः + दोष... = चला दोष....",
            "आः + voiced sound → आ.",
            teaches="आः before a voiced sound loses its visarga: चलाः + दोषधातुमलाः → चला दोषधातुमलाः."),
    ],
}

# ---------------------------------------------------------------- unit 234
AUTHORED["234"] = {
    "title": "तस्मादुदकादीनामपि समत्वं",
    "question": "By unit 234, what cannot be specified by measure?",
    "rule": ("Therefore (तस्मात्) the evenness (समत्व) even of water and the others (उदकादि) is impossible (अशक्यम्) to "
             "specify (निर्देष्टुम्) by measure (परिमाणतः), as for flesh and the rest (मांसादिवत्)."),
    "limits": ("Prose; the copula is understood. Part of the Dhanvantari reading (data). 'Water and the others' = the series "
               "of unit 222; 'flesh and the rest' are those whose measure is given (data note). How evenness is judged "
               "instead is not in this line."),
    "explain_hi": ("‘तस्मात्’ (इसलिए) सम्भवतः इकाई २३३ के कारण पर टिका है: शरीर विलक्षण और दोष-धातु-मल चल हैं। "
                   "इसलिए उदक (जल) आदि की भी समता (समत्व) को परिमाण से बताना अशक्य है। "
                   "‘मांसादिवत्’ = मांस आदि की तरह, जिनका परिमाण दिया गया है। "
                   "‘उदक आदि’ इकाई २२२ की श्रृंखला है। "
                   "‘निर्देष्टुम्’ तुमुन्-रूप (बताने के लिए) है और ‘अशक्यम्’ = असम्भव।"),
    "hook": "मांस आदि का परिमाण दिया; जल आदि की समता परिमाण से नहीं।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 234, the evenness of what cannot be specified by measure?",
            ("Of water and the others", "उदकादीनामपि समत्वम्: the evenness even of water and the others."),
            [("Of flesh and the rest", "Flesh is the model whose measure is given (मांसादिवत्)."),
             ("Of the bones and joints alone", "Bones are not named; the line names water (उदक) and the others."),
             ("Of the pores of the body hair", "Not named in this line.")],
            "The evenness of water and the others cannot be given by measure.",
            "उदकादीनाम् समत्वम् ... अशक्यम्."),
        order(1, "Put these parts of unit 234 in the line's order.",
              ["तस्मादुदकादीनामपि", "समत्वं", "मांसादिवत्", "परिमाणतो", "निर्देष्टुमशक्यं"],
              "Therefore the evenness even of water and the others, as for flesh and the rest, by measure, is impossible "
              "to specify.",
              "तस्मादुदकादीनामपि → समत्वं → मांसादिवत् → परिमाणतो → निर्देष्टुमशक्यं."),
        match(2, "Match each word of unit 234 to its meaning.",
              [["तस्मात्", "therefore"], ["समत्व", "evenness"], ["परिमाणतः", "by measure"],
               ["निर्देष्टुम्", "to specify"], ["अशक्य", "impossible"]],
              "Therefore the evenness of water and the others is impossible to specify by measure.",
              "तस्मात्, समत्व, परिमाणतः, निर्देष्टुम्, अशक्य.", role="extend",
              teaches="-तुम् makes the infinitive 'to ...': निर्देष्टुम् = to specify; with अशक्यम्, 'impossible to specify'."),
        mcq("discriminate", 3, "In unit 234, how does मांसादिवत् (like flesh and the rest) work?",
            ("Flesh and the rest are the model whose measure is given", "The data: in the way of flesh and the rest, whose measure is given."),
            [("Flesh and the rest also cannot be given by any measure", "-वत् compares with flesh, whose measure is given (data note)."),
             ("Water is measured in the very same way as the flesh", "The line says this is impossible (अशक्यम्)."),
             ("Flesh is named as the cause of the evenness of water", "-वत् means like; no cause is named.")],
            "मांसादिवत् = as for flesh and the rest, whose measure is given; for water and the others it is impossible.",
            "-वत् = like, as for."),
        multi("apply", 4, "Which statements fit unit 234?",
              [("तस्मात् marks it as a consequence", "Right: तस्मात् = therefore."),
               ("The evenness of the liquids can be stated by measure", "The line says it is impossible (अशक्यम्)."),
               ("It names the bones as the thing measured", "Bones are not named; flesh and water are."),
               ("निर्देष्टुम् is an infinitive, 'to specify'", "Right: the data gives inf. of निर्-√दिश्.")],
              [0, 3],
              "Therefore it is impossible to specify the evenness of water and the others by measure.",
              "तस्मात्; निर्देष्टुम् अशक्यम्."),
        mcq("transfer", 5, "By the pattern of निर्देष्टुम् अशक्यम्, what does वक्तुम् अशक्यम् mean (a new example)?",
            ("Impossible to say", "Infinitive -तुम् + अशक्यम् = impossible to ..., as निर्देष्टुम् अशक्यम्."),
            [("Possible to say", "The अ- of अशक्य negates: impossible."),
             ("Having said, unable", "Having said would be उक्त्वा, a gerund; वक्तुम् is the infinitive."),
             ("An unable speaker", "No agent noun here; वक्तुम् is 'to say'.")],
            "वक्तुम् अशक्यम् = impossible to say, like निर्देष्टुम् अशक्यम् = impossible to specify.",
            "-तुम् + अशक्यम् = impossible to ....",
            teaches="Infinitive -तुम् + अशक्यम् = impossible to ...: निर्देष्टुम् अशक्यम् = impossible to specify."),
    ],
}

# ---------------------------------------------------------------- unit 235
AUTHORED["235"] = {
    "title": "केवलं स्वास्थ्यमात्रेण",
    "question": "By unit 235, by what means alone should one judge?",
    "rule": ("Only (केवलम्) through mere health (स्वास्थ्यमात्रेण), by inference (अनुमानतः), should one judge (लक्षयेत्). "
             "इति closes the quoted reading."),
    "limits": ("Prose. The object of लक्षयेत् is not printed (probably the evenness of unit 234; the card does not supply it). "
               "इति is not translated. No question rests on the object."),
    "explain_hi": ("यह गद्य-पंक्ति धान्वन्तरीय पाठ को पूरा करती है; अन्त का ‘इति’ उद्धृत पाठ को बन्द करता है। "
                   "कहा गया है: केवल स्वास्थ्य मात्र से, अनुमान द्वारा, पहचानना चाहिए। "
                   "क्या पहचानना है, वह छपा नहीं; सम्भवतः इकाई २३४ की समता। "
                   "छपाई में ‘अनुमानतोलक्षयेदिति’ जुड़ा है: अनुमानतः + लक्षयेत् + इति।"),
    "hook": "केवल स्वास्थ्य देखकर, अनुमान से जानो।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 235, by what means should one judge?",
            ("By inference through mere health", "स्वास्थ्यमात्रेणानुमानतो लक्षयेत्: by inference, through mere health."),
            [("By direct measure of each dhātu", "केवलम्: only by inference; no measure is named."),
             ("By weighing each liquid on a scale", "No weighing is named; only inference."),
             ("By asking the patient's teacher", "No one is asked; one judges by inference.")],
            "Only by inference through mere health.",
            "केवलं स्वास्थ्यमात्रेण अनुमानतः."),
        order(1, "Put the words of unit 235 (split out of sandhi) in the line's order.",
              ["केवलम्", "स्वास्थ्यमात्रेण", "अनुमानतः", "लक्षयेत्", "इति"],
              "Only through mere health, by inference, one should judge: thus (the reading ends).",
              "केवलम् → स्वास्थ्यमात्रेण → अनुमानतः → लक्षयेत् → इति."),
        match(2, "Match each word of unit 235 to its meaning.",
              [["केवलम्", "only"], ["स्वास्थ्य", "health"], ["मात्र", "mere, nothing but"], ["अनुमान", "inference"],
               ["लक्षयेत्", "one should judge"]],
              "Only through mere health, by inference, one should judge.",
              "केवलम्, स्वास्थ्य, मात्र, अनुमान, लक्षयेत्.", role="extend",
              teaches="-मात्र at the end of a compound = mere, nothing but: स्वास्थ्यमात्र = mere health."),
        mcq("discriminate", 3, "Which split of स्वास्थ्यमात्रेणानुमानतो in unit 235 is right?",
            ("स्वास्थ्यमात्रेण + अनुमानतः", "अ + अ → आ; अः before the voiced ल → ओ."),
            [("स्वास्थ्यमात्रेणा + नुमानतः", "नुमानतः is not a word; the word is अनुमानतः."),
             ("स्वास्थ्यमात्रे + अनुमानतः", "ए + अ would give मात्रेऽनुमानतः, not मात्रेणा."),
             ("स्वास्थ्यमात्रेणः + अनुमानतः", "अः + अ would give ओऽ: मात्रेणोऽनुमानतः.")],
            "स्वास्थ्यमात्रेण (through mere health) + अनुमानतः (by inference): अ + अ → आ.",
            "अ + अ → आ."),
        multi("apply", 4, "Which statements fit unit 235?",
              [("The object of लक्षयेत् is printed in the line", "It is not printed (data note)."),
               ("The judging is by inference (अनुमान)", "Right: अनुमानतः लक्षयेत्."),
               ("इति closes the quoted reading", "Right: the data says so."),
               ("It gives a measure in cupped handfuls (अञ्जलि)", "No measure is given; only inference.")],
              [1, 2],
              "One judges only by inference through mere health; इति closes the reading.",
              "केवलं स्वास्थ्यमात्रेणानुमानतो लक्षयेदिति."),
        mcq("transfer", 5, "By the rule of लक्षयेत् + इति → लक्षयेदिति, how is भवेत् + इति (a new example) joined?",
            ("भवेदिति", "त् before a vowel becomes द्, as लक्षयेत् + इति → लक्षयेदिति."),
            [("भवेतिति", "त् before a vowel becomes द्; it does not stay त्."),
             ("भवेत्यिति", "य् comes from इ before a vowel, not from त्."),
             ("भवेद्दिति", "द् is not doubled before a vowel.")],
            "भवेत् + इति = भवेदिति, like लक्षयेत् + इति = लक्षयेदिति.",
            "त् + vowel → द्.",
            teaches="A final त् before a vowel becomes द्: लक्षयेत् + इति → लक्षयेदिति."),
    ],
}

# ---------------------------------------------------------------- unit 236
AUTHORED["236"] = {
    "title": "सर्वएव त्ववयवाः",
    "question": "By unit 236, why do all the parts come to be countless?",
    "rule": ("But all the parts (अवयवाः), by division into atoms (परमाणुभेदेन), because of extreme subtlety "
             "(अतिसौक्ष्म्यात्), come to countlessness (असंख्येयतां यान्ति)."),
    "limits": ("Prose. परमाणु = atom, the doctrine's own term for the smallest particle; the card adds no modern physics. "
               "Whether this line still belongs to the quoted reading is not stated."),
    "explain_hi": ("यह गद्य-पंक्ति कहती है कि सभी अवयव (भाग), परमाणुओं में भेद करने पर, अत्यन्त सूक्ष्म होने के कारण "
                   "असंख्येय (अनगिनत) हो जाते हैं। "
                   "परमाणु यहाँ शास्त्र का अपना शब्द है: सबसे छोटा कण। "
                   "‘तु’ (परन्तु) एक मोड़ दिखाता है। "
                   "छपा ‘सर्वएव’ = सर्वे + एव: ए स्वर से पहले अय् बनता है, य् का लोप होता है, और ‘सर्व एव’ रहता है।"),
    "hook": "बाँटते जाओ, परमाणु तक: गिनती समाप्त।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 236, what do all the parts come to?",
            ("Countlessness", "असंख्येयतां यान्ति: they go to countlessness."),
            [("Death and decay", "Not said; they become countless (असंख्येयता)."),
             ("One single mass", "Not said; division makes them countless."),
             ("A fixed count of seven", "No number is given; they become countless.")],
            "All the parts come to be countless.",
            "असंख्येयताम् यान्ति = become countless."),
        order(1, "Put the words of unit 236 (split out of sandhi) in the line's order.",
              ["सर्वे एव", "तु अवयवाः", "परमाणुभेदेन", "अतिसौक्ष्म्यात्", "असंख्येयताम्", "यान्ति"],
              "But all the parts, by division into atoms, because of extreme subtlety, go to countlessness.",
              "सर्वे एव → तु अवयवाः → परमाणुभेदेन → अतिसौक्ष्म्यात् → असंख्येयताम् → यान्ति."),
        match(2, "Match each word of unit 236 to its meaning.",
              [["अवयव", "part"], ["परमाणु", "atom"], ["भेद", "division"], ["सौक्ष्म्य", "subtlety"],
               ["असंख्येयता", "countlessness"]],
              "All the parts, divided into atoms, through extreme subtlety become countless.",
              "अवयव, परमाणु, भेद, सौक्ष्म्य, असंख्येयता.", role="extend",
              teaches="सौक्ष्म्य = subtlety, the abstract noun of सूक्ष्म (subtle, minute); अति- = extreme."),
        mcq("discriminate", 3, "Which split of the printed सर्वएव in unit 236 is right?",
            ("सर्वे + एव", "ए before a vowel becomes अय्; the य् drops, leaving सर्व एव (printed without the gap)."),
            [("सर्व + एव", "अ + ए would join as ऐ: सर्वैव."),
             ("सर्वम् + एव", "म् before a vowel joins it: सर्वमेव."),
             ("सर्वाः + एव", "आः before a vowel drops ः but keeps आ: सर्वा एव.")],
            "सर्वे (all) + एव (indeed): ए + vowel → अ(य्), य् dropped.",
            "ए + vowel → अय्, य् usually dropped."),
        multi("apply", 4, "Which reasons does unit 236 give for the parts becoming countless?",
              [("Their great size", "Not said; the line speaks of extreme subtlety."),
               ("Division into atoms", "Right: परमाणुभेदेन."),
               ("Extreme subtlety", "Right: अतिसौक्ष्म्यात्."),
               ("Constant movement of the doṣas", "Not given here as the reason.")],
              [1, 2],
              "By division into atoms, because of extreme subtlety, the parts become countless.",
              "परमाणुभेदेन; अतिसौक्ष्म्यात्."),
        mcq("transfer", 5, "By the rule of तु + अवयवाः → त्ववयवाः, how is मनु + अन्तरम् (a Manu's age, a new example) joined?",
            ("मन्वन्तरम्", "उ before अ becomes व्, as तु + अवयवाः → त्ववयवाः."),
            [("मनोन्तरम्", "ओ comes from अ + उ, not from उ + अ."),
             ("मनवन्तरम्", "अव् comes from ओ before a vowel, not from उ."),
             ("मनून्तरम्", "ऊ comes from उ + उ, not from उ + अ.")],
            "मनु + अन्तरम् = मन्वन्तरम्, like तु + अवयवाः = त्ववयवाः.",
            "उ + अ → व.",
            teaches="उ before an unlike vowel becomes व्: तु + अवयवाः → त्ववयवाः."),
    ],
}

# ---------------------------------------------------------------- unit 237
AUTHORED["237"] = {
    "title": "तेषां संयोगविभागे परमाणूनां",
    "question": "By unit 237, what is the cause of the union and separation of the atoms?",
    "rule": ("In the union (संयोग) and separation (विभाग) of those atoms (परमाणूनाम्), wind (वायु), impelled by action "
             "(कर्मप्रेरितः), is the cause (कारणम्)."),
    "limits": ("Prose; the copula is understood. वायु is glossed wind; whether the doṣa is meant is not stated. The antecedent "
               "of तेषाम् (probably the parts of unit 236) is not stated: no question on it. कर्म = action (deed), a doctrinal term."),
    "explain_hi": ("यह गद्य-पंक्ति बताती है कि उन परमाणुओं के संयोग (जुड़ने) और विभाग (अलग होने) का कारण वायु है, जो कर्म से प्रेरित है। "
                   "यानी क्रम है: कर्म वायु को प्रेरित करता है, और वायु संयोग-विभाग का कारण है। "
                   "‘कर्म’ यहाँ शास्त्रीय शब्द है: कर्म या कृत्य। "
                   "‘वायु’ का अर्थ डेटा में हवा रखा गया है; दोष से अभिप्राय है या नहीं, यह नहीं कहा गया। "
                   "‘तेषाम्’ ‘परमाणूनाम्’ से मेल खाता है।"),
    "hook": "कर्म प्रेरे वायु को, वायु कारण संयोग-विभाग का।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 237, what is the cause of the union and separation of the atoms?",
            ("Wind impelled by action", "कर्मप्रेरितो वायुः कारणम्: wind, impelled by action, is the cause."),
            [("Heat impelled by food", "The line names वायु, not heat."),
             ("Water impelled by the moon", "The line names वायु, not water."),
             ("Earth impelled by weight", "The line names वायु, not earth.")],
            "Wind, impelled by action, is the cause.",
            "कर्मप्रेरितः वायुः कारणम्."),
        match(1, "Match each word of unit 237 to its meaning.",
              [["संयोग", "union"], ["विभाग", "separation"], ["कर्म", "action"], ["प्रेरित", "impelled"], ["कारण", "cause"]],
              "In the union and separation of the atoms, wind impelled by action is the cause.",
              "संयोग, विभाग, कर्म, प्रेरित, कारण."),
        order(2, "Put the printed words of unit 237 in the line's order.",
              ["तेषां", "संयोगविभागे", "परमाणूनां", "कर्मप्रेरितो", "वायुः", "कारणं"],
              "Of those, in the union and separation, of the atoms, impelled by action, wind, the cause.",
              "तेषां → संयोगविभागे → परमाणूनां → कर्मप्रेरितो → वायुः → कारणं.", role="extend",
              teaches="कर्मप्रेरितः = impelled by action: a tatpuruṣa whose first part names the agent (by)."),
        mcq("discriminate", 3, "By unit 237, which pair of opposite events does wind cause?",
            ("Union and separation", "संयोगविभागे: in union and separation."),
            [("Birth and death of the body", "Not named; the line says संयोग and विभाग."),
             ("Heating and cooling", "Not named; the line says संयोग and विभाग."),
             ("Sleeping and waking", "Not named; the line says संयोग and विभाग.")],
            "Wind is the cause in the union and separation of the atoms.",
            "संयोग (union) ↔ विभाग (separation)."),
        mcq("apply", 4, "By unit 237, what stands first in the chain that ends in union and separation?",
            ("Action, which impels the wind", "कर्मप्रेरितः: the wind is impelled by action."),
            [("The atoms, which impel the wind", "The atoms are joined and separated; action impels the wind."),
             ("Wind, which needs no impulse", "The wind is कर्मप्रेरित, impelled by action."),
             ("Union, which impels the action", "Union is the result, not the impeller.")],
            "Action → wind → union and separation of the atoms.",
            "कर्म → वायु → संयोग, विभाग."),
        mcq("transfer", 5, "By the pattern of कर्मप्रेरितः (impelled by action), what does वायुप्रेरितः mean (a new example)?",
            ("Impelled by wind", "The first part names the agent: वायु + प्रेरित = impelled by wind."),
            [("Impelling the wind", "प्रेरित is a past participle, 'impelled', not 'impelling'."),
             ("Wind and its impulse", "It is not a dvandva of two things."),
             ("Wind not yet impelled", "Nothing in the compound negates.")],
            "वायुप्रेरितः = impelled by wind, like कर्मप्रेरितः = impelled by action.",
            "X-प्रेरित = impelled by X.",
            teaches="In a tatpuruṣa like कर्मप्रेरित, the first part names the agent: impelled by action."),
    ],
}

# ---------------------------------------------------------------- unit 238
AUTHORED["238"] = {
    "title": "तदेतदंगभेदेन भेदतश्च",
    "question": "By unit 238, to what two ends does 'this', when understood, lead?",
    "rule": ("This (तदेतत्), understood (गृह्यमाणम्) by distinction of parts and by division, leads to bondage (बन्धाय) or to "
             "liberation (मोक्षाय): two datives; the Sanskrit has no word for 'or'."),
    "limits": ("Prose. The subject तदेतत् is unclear (it appears to be the atomic doctrine of units 236-237). अङ्गभेद may also "
               "mean difference of the limbs: no question on its sense. The last word, printed भवतां|ति, is read भवति + इति "
               "(likely): no question on it."),
    "explain_hi": ("यह गद्य-पंक्ति कहती है: वह यह (विषय), अंगों के भेद से और भेद से ग्रहण किया जाता हुआ, बन्ध के लिए या मोक्ष के लिए होता है। "
                   "‘बन्धाय’ और ‘मोक्षाय’ दोनों चतुर्थी (के लिए) हैं; संस्कृत में ‘या’ नहीं लिखा, यह अर्थ से जोड़ा गया। "
                   "‘तदेतत्’ किसकी ओर है, स्पष्ट नहीं; सम्भवतः इकाई २३६-२३७ का परमाणु-विचार। "
                   "‘गृह्यमाणम्’ कर्मवाच्य वर्तमान कृदन्त है: ग्रहण किया जाता हुआ। "
                   "अन्त का छपा ‘भवतां|ति’ सम्भवतः ‘भवति इति’ है।"),
    "hook": "समझ की दो दिशाएँ: बन्धाय, मोक्षाय।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 238, which two ends do the two datives of the line (बन्धाय, मोक्षाय) name?",
            ("Bondage or liberation", "बन्धाय मोक्षाय: for bondage, for liberation."),
            [("Long life or early death", "Not named; the line says बन्धाय and मोक्षाय."),
             ("Wealth or poverty", "Not named; the line says बन्धाय and मोक्षाय."),
             ("Health or disease", "Not named; the line says बन्धाय and मोक्षाय.")],
            "It leads to bondage or to liberation.",
            "बन्धाय (for bondage), मोक्षाय (for liberation)."),
        order(1, "Put the printed words of unit 238 in the line's order (the doubtful last word is left out).",
              ["तदेतदंगभेदेन", "भेदतश्च", "गृह्यमाणं", "बंधाय", "मोक्षाय"],
              "This, by distinction of parts and by division, being understood, for bondage, for liberation.",
              "तदेतदंगभेदेन → भेदतश्च → गृह्यमाणं → बंधाय → मोक्षाय."),
        match(2, "Match each word of unit 238 to its meaning.",
              [["बन्ध", "bondage"], ["मोक्ष", "liberation"], ["गृह्यमाण", "being understood"], ["भेदतः", "by division"]],
              "This, understood by division, leads to bondage or liberation.",
              "बन्ध, मोक्ष, गृह्यमाण, भेदतः.", role="extend",
              teaches="बन्ध and मोक्ष are a pair of opposites in this line: bondage and liberation."),
        mcq("discriminate", 3, "What case is बन्धाय in unit 238?",
            ("Dative: 'for bondage'", "-आय is the dative singular of an अ-stem."),
            [("Instrumental: 'by bondage'", "That would be बन्धेन."),
             ("Ablative: 'from bondage'", "That would be बन्धात्."),
             ("Locative: 'in bondage'", "That would be बन्धे.")],
            "बन्धाय = for bondage (dative), like मोक्षाय = for liberation.",
            "अ-stem + -आय = dative sg."),
        mcq("apply", 4, "What does the form गृह्यमाणम् in unit 238 express?",
            ("Something being grasped (passive, present)", "The data: pass. pres. part. of √ग्रह्."),
            [("Someone grasping (active, present)", "Active would be गृह्णत्; गृह्यमाण is passive (data)."),
             ("Something already grasped (past)", "The past participle would be गृहीत."),
             ("Something to be grasped (a duty)", "That would be a gerundive such as ग्राह्य.")],
            "गृह्यमाणम् = being grasped, being understood.",
            "गृह्य- + -मान = passive present participle."),
        mcq("transfer", 5, "By the pattern of बन्धाय (for bondage), which form of the new word सुख (happiness) is its dative?",
            ("सुखाय", "अ-stem dative singular in -आय, like बन्धाय."),
            [("सुखेन", "Instrumental, 'by happiness'."),
             ("सुखात्", "Ablative, 'from happiness'."),
             ("सुखे", "Locative, 'in happiness'.")],
            "सुखाय = for happiness, like बन्धाय = for bondage.",
            "अ-stem + -आय = for.",
            teaches="The dative singular of an अ-stem ends in -आय and means 'for': बन्धाय, मोक्षाय."),
    ],
}

# ---------------------------------------------------------------- unit 239
AUTHORED["239"] = {
    "title": "भवतिचात्र",
    "question": "What does the short formula of unit 239 do?",
    "rule": "भवति च अत्र, 'and here there is': a formula that introduces a verse; the verse is unit 240.",
    "limits": "Prose formula; it has no stated object and teaches nothing itself. Printed as one word, भवतिचात्र.",
    "explain_hi": ("‘भवति चात्र’ एक सूत्र-वाक्य है: ‘और इस विषय में (यह) है’। "
                   "गद्य के बाद श्लोक लाने से पहले यह पंक्ति आती है; यहाँ श्लोक इकाई २४० में है। "
                   "छपाई में तीनों शब्द ‘भवतिचात्र’ जुड़े छपे हैं। "
                   "‘चात्र’ = च + अत्र (अ + अ → आ)।"),
    "hook": "‘भवति चात्र’: अब श्लोक आता है।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What does भवति चात्र (unit 239) do?",
            ("It introduces a verse", "The data: a formula introducing a verse."),
            [("It closes the chapter here", "The colophon comes at unit 241."),
             ("It names a new teacher", "No teacher is named."),
             ("It gives a measure", "No measure is given.")],
            "The formula introduces a verse.",
            "भवति चात्र introduces a verse."),
        match(1, "Match each word of unit 239 to its meaning.",
              [["भवति", "there is"], ["च", "and"], ["अत्र", "here, on this"]],
              "And here there is (a verse).",
              "भवति, च, अत्र."),
        fill(2, "चात्र = च + ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("अत्र", None, "atra"),
             "चात्र = च (and) + अत्र (here).",
             "अत्र = here, on this matter.",
             "च + अत्र = चात्र."),
        mcq("discriminate", 3, "Which split of चात्र is right?",
            ("च + अत्र", "अ + अ → आ: च + अत्र = चात्र."),
            [("चा + अत्र", "चा is not a word; the word is च."),
             ("च + आत्र", "आत्र is not a word."),
             ("चे + अत्र", "ए + अ would give चेऽत्र.")],
            "च (and) + अत्र (here): अ + अ → आ.",
            "अ + अ → आ."),
        multi("apply", 4, "Which statements about unit 239 are right?",
              [("It is printed as one run-together word", "Right: भवतिचात्र."),
               ("It is itself a metrical verse", "It is a prose formula."),
               ("It names what the verse is about", "It has no stated object."),
               ("It contains the verb भवति, 'there is'", "Right: 3 sg. present of √भू.")],
              [0, 3],
              "A run-together prose formula with the verb भवति.",
              "भवति च अत्र."),
        mcq("transfer", 5, "By the rule of च + अत्र → चात्र, how is न + अस्ति (is not, a new example) joined?",
            ("नास्ति", "अ + अ → आ, as च + अत्र → चात्र."),
            [("नस्ति", "Two short अ join as long आ."),
             ("नेस्ति", "ए comes from अ + इ."),
             ("नौस्ति", "औ comes from अ + ओ or औ.")],
            "न + अस्ति = नास्ति, like च + अत्र = चात्र.",
            "अ + अ → आ.",
            teaches="अ + अ join as long आ: च + अत्र → चात्र."),
    ],
}

# ---------------------------------------------------------------- unit 240
AUTHORED["240"] = {
    "title": "इति सर्वावयवशो यो जानाति कलेवरं",
    "question": "By the verse of unit 240, what follows for one who knows the body part by part?",
    "rule": ("He who knows the body (कलेवर) part by part (सर्वावयवशः) never (न कदाचित्) engages, through delusion (मोहेन), "
             "in what is harmful (अहितेषु)."),
    "limits": ("One anuṣṭubh verse over two printed lines: the relative clause (यः) in the first, the main clause (सः) in the "
               "second. It does not say which harmful things are meant; अहितेषु is plural. The print runs मोहेनन together "
               "(= मोहेन न)."),
    "explain_hi": ("यह श्लोक कहता है: जो शरीर (कलेवर) को उसके सब अवयवों के अनुसार जानता है, वह मोह के कारण अहित (हानिकारक बातों) में "
                   "कभी प्रवृत्त नहीं होता। "
                   "पहली पंक्ति में ‘यः’ (जो) वाला उपवाक्य है, दूसरी में ‘सः’ (वह) वाला मुख्य वाक्य। "
                   "‘न कदाचित्’ = कभी नहीं। "
                   "छपाई में ‘मोहेनन’ = मोहेन + न। "
                   "‘सर्वावयवशो यो’ में अः घोष व्यंजन य से पहले ओ बना है।"),
    "hook": "शरीर का अंग-अंग जानो, मोह से अहित नहीं होगा।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 240, what is said of one who knows the body part by part?",
            ("He does not turn to harm by delusion", "अहितेषु स मोहेन न कदाचित्प्रवर्तते."),
            [("He falls ill in no season of the year", "Illness and seasons are not named."),
             ("He needs no help from a physician", "No physician is named."),
             ("He can count every single atom", "Atoms are not named in the verse.")],
            "He never engages in what is harmful through delusion.",
            "न कदाचित् प्रवर्तते = never engages."),
        order(1, "Put the printed parts of the verse of unit 240 in order.",
              ["इति सर्वावयवशो", "यो जानाति कलेवरं", "अहितेषु स", "मोहेनन", "कदाचित्प्रवर्त्तते"],
              "Thus who knows the body part by part, he through delusion never engages in harmful things.",
              "इति सर्वावयवशो → यो जानाति कलेवरं → अहितेषु स → मोहेनन → कदाचित्प्रवर्त्तते."),
        match(2, "Match each word of unit 240 to its meaning.",
              [["कलेवर", "body"], ["सर्वावयवशः", "part by part"], ["अहित", "harmful"], ["मोह", "delusion"],
               ["कदाचित्", "ever"]],
              "He who knows the body part by part never engages in the harmful through delusion.",
              "कलेवर, सर्वावयवशः, अहित, मोह, कदाचित्.", role="extend",
              teaches="न कदाचित् = never: न (not) + कदाचित् (ever)."),
        mcq("discriminate", 3, "Which split of the printed मोहेनन in unit 240 is right?",
            ("मोहेन + न", "Two words run together in the print: through delusion + not."),
            [("मोहे + नन", "नन is not a word; the negation is न."),
             ("मोहेन + अन", "अ + अ would join as आ: मोहेनान."),
             ("मोह + एनन", "एनन is not a word, and अ + ए would give ऐ.")],
            "मोहेन (through delusion) + न (not), printed without a space.",
            "मोहेनन = मोहेन न."),
        multi("apply", 4, "Which statements fit the verse of unit 240?",
              [("It names the harmful things one by one", "It does not say which harmful things are meant."),
               ("The first line holds the relative clause with यः", "Right: यो जानाति कलेवरम्."),
               ("It says knowledge of the body cures every disease", "Nothing is said of curing."),
               ("The second line holds the main clause with सः", "Right: स ... न कदाचित्प्रवर्तते.")],
              [1, 3],
              "यः ... जानाति (first line) → सः ... न प्रवर्तते (second line).",
              "यः (who) ... सः (he)."),
        mcq("transfer", 5, "By the pattern of न कदाचित् in unit 240, what does न कदाचिदनृतं वदेत् mean (a new example)?",
            ("One should never speak untruth", "न कदाचित् = never; वदेत् = should speak."),
            [("One should sometimes speak untruth", "कदाचित् with न means never, not sometimes."),
             ("One should speak untruth only once", "Nothing here means once."),
             ("No one has ever spoken untruth", "वदेत् is optative, 'should speak', not a past fact.")],
            "न कदाचिदनृतं वदेत् = one should never speak untruth, like न कदाचित् प्रवर्तते = never engages.",
            "न + कदाचित् = never.",
            teaches="न with कदाचित् (ever) means never: स मोहेन न कदाचित्प्रवर्तते."),
    ],
}

# ---------------------------------------------------------------- unit 241
AUTHORED["241"] = {
    "title": "इत्यंगविभागो नाम पंचमोऽध्यायः",
    "question": "What does the colophon in unit 241 name the fifth chapter?",
    "rule": ("Thus the fifth chapter (पञ्चमोऽध्यायः), named Aṅgavibhāga, the division of the parts of the body. Printed "
             "इत्यंगविभागो = इति + अङ्गविभागः."),
    "limits": "A colophon, prose: it gives the chapter's name and number and teaches nothing else. No 'ends' is printed.",
    "explain_hi": ("यह पाँचवें अध्याय की समाप्ति-पंक्ति (पुष्पिका) है: इस प्रकार अङ्गविभाग नाम का पाँचवाँ अध्याय। "
                   "‘अङ्गविभाग’ = अङ्ग (शरीर का भाग) + विभाग (बँटवारा): शरीर के भागों का विभाजन। "
                   "यही अध्याय का विषय रहा है: त्वचाएँ, कलाएँ, अस्थियाँ, सन्धियाँ, स्नायु, पेशियाँ आदि। "
                   "सन्धि: इति + अङ्ग → इत्यङ्ग (इ + अ → य); अङ्गविभागः + नाम → अङ्गविभागो नाम; पञ्चमः + अध्यायः → पञ्चमोऽध्यायः।"),
    "hook": "पाँचवाँ अध्याय: अंगों का विभाग।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 241, what is chapter five named?",
            ("अङ्गविभाग", "इत्यङ्गविभागो नाम पञ्चमोऽध्यायः."),
            [("गर्भव्यापत्", "That is the name of chapter four."),
             ("गर्भोपचरणीय", "That is the name of chapter three."),
             ("गर्भावक्रान्ति", "That is the name of chapter two.")],
            "The colophon names the chapter Aṅgavibhāga, division of the parts of the body.",
            "अङ्गविभाग = division of the parts of the body."),
        order(1, "Put the words of unit 241 (split out of sandhi) in their order.",
              ["इति", "अङ्गविभागः", "नाम", "पञ्चमः", "अध्यायः"],
              "Thus, Aṅgavibhāga, named, fifth, chapter.",
              "इति → अङ्गविभागः → नाम → पञ्चमः → अध्यायः."),
        match(2, "Match each word of unit 241 to its meaning.",
              [["इति", "thus (closing)"], ["अङ्ग", "part of the body"], ["विभाग", "division"], ["नाम", "named"],
               ["पञ्चम", "fifth"]],
              "Thus the fifth chapter, named division of the parts of the body.",
              "इति, अङ्ग, विभाग, नाम, पञ्चम.", role="extend",
              teaches="अङ्गविभाग = अङ्ग + विभाग: the division of the parts of the body, the theme of the chapter."),
        mcq("discriminate", 3, "Which split of इत्यंगविभागो in unit 241 is right?",
            ("इति + अङ्गविभागः", "इ + अ → य; अः before the voiced न of नाम → ओ."),
            [("इत्य + अङ्गविभागः", "इत्य is not a word; the य् comes from the इ of इति."),
             ("इति + अङ्गविभागा", "आ before न stays आ; it would print इत्यङ्गविभागा."),
             ("इते + अङ्गविभागः", "ए + अ would give इतेऽङ्ग..., not इत्यङ्ग.")],
            "इति (thus) + अङ्गविभागः (division of the parts): इ + अ → य; अः + voiced consonant → ओ.",
            "इ + unlike vowel → य्; अः + voiced consonant → ओ."),
        fill(4, "In unit 241 the word for 'fifth' is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("पञ्चमः", "pañcamaḥ", "पञ्चम", "panchama", "panchamah"),
             "पञ्चमः = fifth; before अध्यायः it is printed पंचमोऽध्यायः.",
             "पञ्चम = fifth; ऽ marks the lost अ of अध्यायः.",
             "पञ्चम = fifth.", role="apply"),
        mcq("transfer", 5, "By the rule of पञ्चमः + अध्यायः → पञ्चमोऽध्यायः, how is कृषकः + अवदत् (the farmer said, a new example) joined?",
            ("कृषकोऽवदत्", "अः + अ → ओ, and ऽ marks the lost अ, as पञ्चमः + अध्यायः."),
            [("कृषका अवदत्", "आ with a gap comes from आः before a vowel, not from अः."),
             ("कृषक अवदत्", "अः drops to अ with a gap only before vowels other than अ."),
             ("कृषकरवदत्", "र् comes from a visarga after vowels other than अ/आ.")],
            "कृषकः + अवदत् = कृषकोऽवदत्, like पञ्चमः + अध्यायः = पञ्चमोऽध्यायः.",
            "अः + अ → ओऽ.",
            teaches="अः before अ becomes ओ and the following अ is marked ऽ: पञ्चमः + अध्यायः → पञ्चमोऽध्यायः."),
    ],
}


# ===================================================================== NOTES_HI
NOTES_HI = {
    "229": ("गद्य (02.05.243); विश्वास निम्न। पाठ-चिह्न (सम्भावित): छपा ‘अपारेसंख्यातान्’ कोई शब्द नहीं; ‘अपरिसंख्यातान्’ (अनगिने) "
            "अनुमानित पाठ है (रि का रे छपना, पा की मात्रा खिसकना); इस पर कोई प्रश्न नहीं। लम्बा छपा टुकड़ा "
            "‘लक्षणैर्विभावयेदपरांश्चापारेसंख्यातान्मूर्त्तामूर्त्तान्’ छह शब्द जोड़ता है (डेटा-टिप्पणी ‘पाँच’ कहती है); विभाजन डेटा के सम्पादक का है। मूर्त/अमूर्त = "
            "रूप वाले/रूपहीन (शास्त्रीय शब्द)। छपा दोहरा त्त (मूर्त्त) सामान्य किया गया। सन्धि जाँची: अतः + वृद्धि → अतो वृद्धि (अः + घोष "
            "व्यंजन → ओ); यथास्वम् + लक्षणैः → यथास्वं लक्षणैः; लक्षणैः + विभावयेत् → लक्षणैर्विभावयेत् (ऐः + घोष → ऐर्); विभावयेत् + "
            "अपरान् → विभावयेदपरान् (त् + स्वर → द्); अपरान् + च → अपरांश्च (न् + च → ंश्च); मूर्त + अमूर्त → मूर्तामूर्त (अ + अ → आ)।"),
    "230": ("गद्य (02.05.244); विश्वास उच्च; कोई पाठ-चिह्न नहीं। ‘तद्यथा’ उदाहरण लाने का सूत्र है; हिन्दी ‘वह इस प्रकार’ शब्दशः है। "
            "सन्धि जाँची: तत् + यथा → तद्यथा (त् + घोष → द्)।"),
    "231": ("गद्य (02.05.245); विश्वास निम्न; कोई पाठ-चिह्न नहीं। पहला समास दो प्रकार से पढ़ा जा सकता है: ‘मांस, कर्ण आदि के मल’ "
            "(डेटा का पाठ) या ‘मांस, और कर्ण से आरम्भ होने वाले मल’; इस पर कोई प्रश्न नहीं। कारक रूप से पढ़ा गया: द्वितीया बहुवचन, इकाई २२९ "
            "(छपी पंक्ति 243) की ‘विभावयेत्’ के कर्म। वायु = हवा; दोष है या सामान्य हवा, नहीं कहा गया। बुद्धि, स्मृति का कोई आधुनिक नाम नहीं। "
            "पूरी पंक्ति एक ही जुड़े शब्द में छपी है। सन्धि जाँची: कर्ण + आदि → कर्णादि (अ + आ → आ); स्मृति + आदीन् → स्मृत्यादीन् "
            "(इ + आ → या); आदीन् + च → आदींश्च (न् + च → ंश्च)।"),
    "232": ("गद्य (02.05.246); विश्वास मध्यम; कोई पाठ-चिह्न नहीं। धान्वन्तरीय = धन्वन्तरि का या उसका अनुयायी; ‘सम्प्रदाय’ अनुवाद मात्र होगा। "
            "कर्म नहीं छपा; डेटा के अनुसार पाठ सम्भवतः आगे (छपी पंक्तियाँ 247-249, यानी इकाई २३३-२३५) है। छपा धान्वंतरीयाः / पठंति = "
            "धान्वन्तरीयाः / पठन्ति (अनुस्वार = न्)। प से पहले विसर्ग (पुनः पठन्ति) बना रहता है।"),
    "233": ("गद्य (02.05.247); विश्वास मध्यम; कोई पाठ-चिह्न नहीं। समूह-टिप्पणी: सम्भवतः इकाई २३२ में घोषित धान्वन्तरीय पाठ का पहला भाग, "
            "इकाई २३५ तक। दोष, धातु, मल शास्त्रीय शब्द रखे गए (मल = अपशिष्ट)। क्रिया ‘हैं’ समझी जाती है। छपा ‘शरीराणिनित्यमेव’ तीन शब्द "
            "(शरीराणि, नित्यम्, एव) जोड़ता है। सन्धि जाँची: चलाः + दोष... → चला दोष... (आः का विसर्ग घोष से पहले लुप्त; छपा ‘चला’ नियमित); नित्यम् + एव → नित्यमेव।"),
    "234": ("गद्य (02.05.248); विश्वास मध्यम; कोई पाठ-चिह्न नहीं। धान्वन्तरीय पाठ जारी। ‘उदक आदि’ = इकाई २२२ (छपी पंक्ति 236) की श्रृंखला; "
            "‘मांसादिवत्’ = मांस आदि की तरह, जिनका परिमाण दिया गया। क्रिया ‘है’ समझी जाती है। सन्धि जाँची: तस्मात् + उदक → तस्मादुदक "
            "(त् + स्वर → द्); उदक + आदीनाम् → उदकादीनाम्; आदीनाम् + अपि → आदीनामपि; मांसादिवत् + परिमाणतः (प से पहले त् बना रहता); "
            "परिमाणतः + निर्देष्टुम् → परिमाणतो निर्देष्टुम् (अः + घोष व्यंजन → ओ); निर्देष्टुम् + अशक्यम् → निर्देष्टुमशक्यम्।"),
    "235": ("गद्य (02.05.249); विश्वास मध्यम; कोई पाठ-चिह्न नहीं। ‘इति’ उद्धृत पाठ बन्द करता है, अनुवाद नहीं किया गया। लक्षयेत् का कर्म "
            "छपा नहीं (सम्भवतः इकाई २३४ की समता); कुछ जोड़ा नहीं गया। सन्धि जाँची: स्वास्थ्यमात्रेण + अनुमानतः → स्वास्थ्यमात्रेणानुमानतः "
            "(अ + अ → आ); अनुमानतः + लक्षयेत् → अनुमानतो लक्षयेत् (अः + घोष व्यंजन → ओ; छपाई में बिना अन्तर); लक्षयेत् + इति → लक्षयेदिति "
            "(त् + स्वर → द्)।"),
    "236": ("गद्य (02.05.250); विश्वास मध्यम; कोई पाठ-चिह्न नहीं। परमाणु = सबसे छोटा कण, शास्त्र का अपना शब्द। ‘असंख्येयतां यान्ति’ = "
            "असंख्येयता को जाते हैं। छपा ‘असंख्येयतांयांति’ दो शब्द जोड़ता है। सन्धि जाँची: सर्वे + एव → सर्व एव (ए + स्वर → अय्, य् का लोप; "
            "छपा ‘सर्वएव’ बिना अन्तर); तु + अवयवाः → त्ववयवाः (उ + अ → व); परमाणुभेदेन + अति → परमाणुभेदेनाति (अ + अ → आ); "
            "अतिसौक्ष्म्यात् + असंख्येयताम् → अतिसौक्ष्म्यादसंख्येयताम् (त् + स्वर → द्)।"),
    "237": ("गद्य (02.05.251); विश्वास मध्यम; कोई पाठ-चिह्न नहीं। कर्म = कृत्य, शास्त्रीय शब्द; वायु = हवा। क्रिया ‘है’ समझी जाती है। "
            "‘तेषाम्’ ‘परमाणूनाम्’ से मेल खाता है; उसका पूर्व-संदर्भ (सम्भवतः इकाई २३६ के अवयव) नहीं कहा गया, इस पर प्रश्न नहीं। "
            "सन्धि जाँची: तेषाम् + संयोग → तेषां संयोग; कर्मप्रेरितः + वायुः → कर्मप्रेरितो वायुः (अः + घोष व्यंजन → ओ); क से पहले विसर्ग "
            "(वायुः कारणम्) बना रहता है।"),
    "238": ("गद्य (02.05.252); विश्वास मध्यम। पाठ-चिह्न (सम्भावित): छपा ‘भवतां|ति’ में फालतू अनुस्वार और | है; ‘भवति + इति’ (भवतीति) "
            "पढ़ा गया; अन्तिम ‘इति’ का अनुवाद नहीं। इस पर कोई प्रश्न नहीं। ‘बन्धाय मोक्षाय’ के बीच संस्कृत में ‘या’ नहीं; अर्थ से जोड़ा गया। "
            "कर्ता ‘तदेतत्’ अस्पष्ट (सम्भवतः इकाई २३६-२३७ का परमाणु-विचार)। ‘अङ्गभेद’ = अंगों का भेद, या अवयवों का अन्तर; दोनों सम्भव। "
            "सन्धि जाँची: तत् + एतत् → तदेतत्; एतत् + अङ्ग → एतदङ्ग (त् + स्वर → द्); भेदतः + च → भेदतश्च (च से पहले विसर्ग → श्); "
            "गृह्यमाणम् + बन्धाय → गृह्यमाणं बन्धाय।"),
    "239": ("गद्य (02.05.253); विश्वास उच्च; कोई पाठ-चिह्न नहीं। श्लोक लाने का सूत्र; श्लोक इकाई २४० (छपी पंक्तियाँ 254-255) में। "
            "कोई कर्म नहीं छपा, कुछ जोड़ा नहीं गया। छपा ‘भवतिचात्र’ तीन शब्द जोड़ता है। सन्धि जाँची: च + अत्र → चात्र (अ + अ → आ)।"),
    "240": ("श्लोक (अनुष्टुभ्), दो छपी पंक्तियाँ (02.05.254, 02.05.255) जोड़ी गईं: पहली में ‘यः’ उपवाक्य, दूसरी में ‘सः’ मुख्य वाक्य। "
            "विश्वास उच्च; कोई पाठ-चिह्न नहीं। छपा ‘मोहेनन’ = मोहेन न (दो शब्द साथ छपे)। ‘अहितेषु’ बहुवचन: अहितकर (बातों) में। छपा दोहरा "
            "त्त (प्रवर्त्तते) सामान्य किया गया। सन्धि जाँची: सर्व + अवयवशः → सर्वावयवशः (अ + अ → आ); सर्वावयवशः + यः → सर्वावयवशो यः "
            "और यः + जानाति → यो जानाति (अः + घोष व्यंजन → ओ); सः + मोहेन → स मोहेन (सः का विसर्ग व्यंजन से पहले लुप्त); "
            "कदाचित् + प्रवर्तते → कदाचित्प्रवर्तते।"),
    "241": ("पुष्पिका, गद्य (02.05.256); विश्वास उच्च; कोई पाठ-चिह्न नहीं। अङ्ग यहाँ अंग या भाग; ‘समाप्त’ शब्द छपा नहीं, जोड़ा नहीं गया। "
            "सन्धि जाँची: इति + अङ्ग → इत्यङ्ग (इ + अ → य); अङ्गविभागः + नाम → अङ्गविभागो नाम (अः + घोष व्यंजन → ओ); पञ्चमः + अध्यायः → "
            "पञ्चमोऽध्यायः (अः + अ → ओ, ऽ लुप्त अ का चिह्न); छपा पंचमो = पञ्चमो।"),
}


# ===================================================================== AIDS
AIDS = {
    "229": {
        "diagram": {"groups": [
            {"label": "विभावयेत्: पहचानना है", "items": ["वृद्धि और क्षय: हर एक अपने लक्षणों से",
                                                    "अन्य मूर्त और अमूर्त भाव (बीच का शब्द अनुमानित)"]}]},
        "chunks": "अतो | वृद्धिक्षयौ | यथास्वं | लक्षणैर्विभावयेदपरांश्चापारेसंख्यातान्मूर्त्तामूर्त्तान् | भावान्",
        "sandhi": ("अः + घोष व्यंजन → ओ: अतः + वृद्धिक्षयौ → अतो वृद्धिक्षयौ · ऐः + घोष → ऐर्: लक्षणैः + विभावयेत् → "
                   "लक्षणैर्विभावयेत् · न् + च → ंश्च: अपरान् + च → अपरांश्च।"),
        "seesaw": "वृद्धि (बढ़ना) ↔ क्षय (घटना) · मूर्त (रूप वाला) ↔ अमूर्त (रूपहीन): दोनों जोड़े इसी पंक्ति में।",
    },
    "230": {
        "sandhi": "त् + घोष → द्: तत् + यथा → तद्यथा।",
        "frame": "पहले नियम (इकाई २२९) → ‘तद्यथा’ (जैसे कि) → उदाहरण (इकाई २३१)।",
    },
    "231": {
        "diagram": {"groups": [
            {"label": "पहला समास (दो पाठ सम्भव)", "items": ["मांस", "कर्ण (कान)", "आदि", "मल"]},
            {"label": "दूसरा समास", "items": ["वायु", "बुद्धि", "स्मृति", "आदि"]}]},
        "chunks": "मांसकर्णादिमलान् | वायुबुद्धिस्मृत्यादींश्च",
        "sandhi": "इ + आ → या: स्मृति + आदीन् → स्मृत्यादीन् · न् + च → ंश्च: आदीन् + च → आदींश्च।",
    },
    "232": {
        "chunks": "धान्वंतरीयाः | पुनः | पठंति",
        "frame": "कौन: धान्वन्तरीयाः (धन्वन्तरि के अनुयायी) → मोड़: पुनः (दूसरी ओर) → क्या करते: पठन्ति (पढ़ते हैं) → पाठ: इस पंक्ति में नहीं।",
        "anchors": "नाम + -ईय = उसका अनुयायी: धन्वन्तरि → धान्वन्तरीय, जैसे पाणिनि → पाणिनीय।",
    },
    "233": {
        "diagram": {"groups": [
            {"label": "शरीर", "items": ["विलक्षण: लक्षणों में भिन्न"]},
            {"label": "दोष, धातु, मल", "items": ["नित्य ही चल (अस्थिर)"]}]},
        "chunks": "विलक्षणानि हि | शरीराणिनित्यमेव च | चला दोषधातुमलाः",
        "sandhi": "आः + घोष → आ (विसर्ग लुप्त): चलाः + दोषधातुमलाः → चला दोषधातुमलाः।",
    },
    "234": {
        "contrast": "मांस आदि: परिमाण दिया गया ↔ उदक (जल) आदि: समता परिमाण से बताना अशक्य; दोनों इसी पंक्ति में (मांसादिवत्, उदकादीनाम्)।",
        "chunks": "तस्मादुदकादीनामपि | समत्वं | मांसादिवत्परिमाणतो | निर्देष्टुमशक्यं",
        "sandhi": ("त् + स्वर → द्: तस्मात् + उदक → तस्मादुदक · अः + घोष व्यंजन → ओ: परिमाणतः + निर्देष्टुम् → "
                   "परिमाणतो निर्देष्टुम्।"),
    },
    "235": {
        "chunks": "केवलं | स्वास्थ्यमात्रेणानुमानतोलक्षयेदिति",
        "frame": ("कैसे: केवलम् (केवल) → किससे: स्वास्थ्यमात्र (बस स्वास्थ्य) → विधि: अनुमान → क्रिया: लक्षयेत् (पहचाने) → "
                  "इति: उद्धृत पाठ समाप्त।"),
        "sandhi": ("अ + अ → आ: स्वास्थ्यमात्रेण + अनुमानतः · अः + घोष व्यंजन → ओ: अनुमानतः + लक्षयेत् → अनुमानतो लक्षयेत् · "
                   "त् + स्वर → द्: लक्षयेत् + इति → लक्षयेदिति।"),
    },
    "236": {
        "chain": {"steps": ["सभी अवयव", "परमाणुओं में भेद से", "अति सूक्ष्मता के कारण", "असंख्येयता: अनगिनत"]},
        "chunks": "सर्वएव | त्ववयवाः | परमाणुभेदेनातिसौक्ष्म्यादसंख्येयतांयांति",
        "sandhi": "ए + स्वर → अय्, य् लोप: सर्वे + एव → सर्व एव (छपा सर्वएव) · उ + अ → व: तु + अवयवाः → त्ववयवाः।",
    },
    "237": {
        "diagram": {"groups": [
            {"label": "कारण-क्रम", "items": ["कर्म", "उससे प्रेरित वायु", "परमाणुओं का संयोग और विभाग"]}]},
        "seesaw": "संयोग (जुड़ना) ↔ विभाग (अलग होना): दोनों इसी पंक्ति में, एक ही कारण वायु।",
        "chunks": "तेषां | संयोगविभागे | परमाणूनां | कर्मप्रेरितो वायुः | कारणं",
        "sandhi": "अः + घोष व्यंजन → ओ: कर्मप्रेरितः + वायुः → कर्मप्रेरितो वायुः।",
    },
    "238": {
        "seesaw": "बन्धाय (बन्ध के लिए) ↔ मोक्षाय (मोक्ष के लिए): दोनों चतुर्थी इसी पंक्ति में; बीच का ‘या’ अर्थ से।",
        "chunks": "तदेतदंगभेदेन | भेदतश्च | गृह्यमाणं | बंधाय | मोक्षाय | भवतां|ति (छपा)",
        "sandhi": "त् + स्वर → द्: तत् + एतत् → तदेतत्; एतत् + अङ्ग → एतदङ्ग · च से पहले विसर्ग → श्: भेदतः + च → भेदतश्च।",
    },
    "239": {
        "sandhi": "अ + अ → आ: च + अत्र → चात्र।",
        "frame": "भवति (है) → च (और) → अत्र (इस विषय में) → आगे: श्लोक (इकाई २४०)।",
    },
    "240": {
        "diagram": {"groups": [
            {"label": "पहली पंक्ति: यः (जो)", "items": ["सब अवयवों के अनुसार", "कलेवर (शरीर) को जानता है"]},
            {"label": "दूसरी पंक्ति: सः (वह)", "items": ["मोह से अहित में", "कभी प्रवृत्त नहीं होता"]}]},
        "chunks": "इति सर्वावयवशो यो जानाति कलेवरं | अहितेषु स मोहेनन कदाचित्प्रवर्त्तते",
        "sandhi": ("अः + घोष व्यंजन → ओ: सर्वावयवशः + यः → सर्वावयवशो यः; यः + जानाति → यो जानाति · सः + व्यंजन → स "
                   "(विसर्ग लोप): सः + मोहेन → स मोहेन।"),
        "pegs": ("मेरा बनाया चित्र: जो यात्री रास्ते का पूरा नक्शा जानता है, वह भ्रम से गड्ढे में नहीं उतरता; वैसे ही शरीर का "
                 "अंग-अंग जानने वाला मोह से अहित में नहीं। (मेरी याद-पद्धति, श्लोक का दावा नहीं)"),
    },
    "241": {
        "chunks": "इत्यंगविभागो | नाम | पंचमोऽध्यायः",
        "sandhi": ("इ + अ → य: इति + अङ्ग → इत्यङ्ग · अः + घोष व्यंजन → ओ: अङ्गविभागः + नाम → अङ्गविभागो नाम · अः + अ → ओऽ: "
                   "पञ्चमः + अध्यायः → पञ्चमोऽध्यायः।"),
        "frame": "इति (इस प्रकार) → नाम: अङ्गविभाग (शरीर के भागों का विभाग) → संख्या: पञ्चम (पाँचवाँ) → अध्यायः।",
    },
}


# ===================================================================== IMAGE_SPECS
IMAGE_SPECS = {
    ("229", "diagram"): {
        "file": "sh5-vriddhi-kshaya-229.svg",
        "alt": ("Table of unit 229, word and meaning: therefore; increase and decrease; each by its own signs; one should "
                "discern; corporeal and non-corporeal entities. The doubtful middle word is left out."),
        "type": "table",
        "title": "इकाई २२९: वृद्धि-क्षय की पहचान",
        "heads": ["शब्द", "अर्थ"],
        "rows": [["अतः", "इसलिए"], ["वृद्धिक्षयौ", "वृद्धि और क्षय"], ["यथास्वं लक्षणैः", "हर एक अपने लक्षणों से"],
                 ["विभावयेत्", "पहचाने"], ["मूर्तामूर्तान् भावान्", "मूर्त और अमूर्त भाव"]],
    },
    ("233", "diagram"): {
        "file": "sh5-vilakshana-233.svg",
        "alt": ("Two columns of unit 233: bodies are of dissimilar characteristics; the doṣas, dhātus and malas are always "
                "unsteady."),
        "type": "split",
        "title": "इकाई २३३: क्योंकि",
        "cols": [["शरीर", ["विलक्षण: लक्षणों में भिन्न"]], ["दोष, धातु, मल", ["नित्य ही चल (अस्थिर)"]]],
    },
    ("234", "contrast"): {
        "file": "sh5-samatva-234.svg",
        "alt": ("Two columns of unit 234: flesh and the rest, whose measure is given; water and the others, whose evenness "
                "cannot be specified by measure."),
        "type": "split",
        "title": "इकाई २३४: परिमाण से समता",
        "cols": [["मांस आदि (मांसादिवत्)", ["परिमाण दिया गया"]],
                 ["उदक (जल) आदि", ["समता परिमाण से बताना अशक्य"]]],
    },
    ("236", "chain"): {
        "file": "sh5-paramanu-236.svg",
        "alt": ("Chain of unit 236 in the line's order: all the parts; by division into atoms; because of extreme subtlety; "
                "countlessness."),
        "type": "chain",
        "title": "इकाई २३६: अवयव से असंख्येयता",
        "steps": ["सभी अवयव", "परमाणुओं में भेद से", "अति सूक्ष्मता के कारण", "असंख्येयता: अनगिनत"],
    },
    ("237", "diagram"): {
        "file": "sh5-karma-vayu-237.svg",
        "alt": ("Flowchart of unit 237: action (karma) impels wind (vāyu); wind is the cause of the union and of the "
                "separation of the atoms."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"कर्म\"] -->|\"प्रेरित करता है\"| B[\"वायु: कारण\"]\n"
                 "  B --> C[\"परमाणुओं का संयोग\"]\n"
                 "  B --> D[\"परमाणुओं का विभाग\"]\n"),
    },
    ("238", "seesaw"): {
        "file": "sh5-bandha-moksha-238.svg",
        "alt": ("Two columns of unit 238: for bondage (bandhāya) and for liberation (mokṣāya), the two datives of the line; "
                "the 'or' is supplied by sense."),
        "type": "split",
        "title": "इकाई २३८: ग्रहण किया जाता हुआ, किसके लिए",
        "cols": [["बन्धाय", ["बन्ध के लिए"]], ["मोक्षाय", ["मोक्ष के लिए"]]],
    },
    ("240", "diagram"): {
        "file": "sh5-kalevara-240.svg",
        "alt": ("Flowchart of the verse of unit 240 in four steps: he who part by part; knows the body; he, through delusion, "
                "in harmful things; never engages."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"यः, जो सब अवयवों से\"] --> B[\"शरीर (कलेवर) को जानता है\"]\n"
                 "  B --> C[\"सः, वह मोह से अहित में\"]\n"
                 "  C --> D[\"कभी प्रवृत्त नहीं होता\"]\n"),
    },
}
