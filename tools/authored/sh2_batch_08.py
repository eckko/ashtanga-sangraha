from helpers import mcq, match, order, fill, multi, accepts


def T(q, teaches):
    q["teaches"] = teaches
    return q


AUTHORED = {}

# ---------------------------------------------------------------- unit 89
AUTHORED["89"] = {
    "title": "यदा तस्यावयवस्तदा",
    "question": "Which words of the damaged prose unit 89 are sure, and how is the unit built?",
    "rule": ("A damaged 'when ... then' clause: यदा तस्य अवयवः (when its part ...), तदा (then) ... The word after तदा "
             "is unclear in print, and the clause has no predicate."),
    "limits": ("Low confidence. The printed तदापूतप्रजां is doubtful; पूतिप्रजाम् (one of spoiled offspring) is only a "
               "conjecture, so no question rests on it. No predicate: जनयति is taken as understood from unit 88, not "
               "supplied. The line seems to go on from unit 88 into unit 90 (not firm)."),
    "explain_hi": ("यह गद्य-पंक्ति क्षतिग्रस्त और अधूरी है। पक्के शब्द हैं: यदा (जब), तस्य (उसका), अवयवः (अवयव, अंग) और तदा (तब)। "
                   "‘तदा’ के बाद छपा ‘आपूतप्रजां’ कोई शब्द नहीं; ‘पूतिप्रजाम्’ (बिगड़ी हुई सन्तान वाली) केवल अनुमानित पाठ है। "
                   "वाक्य में कोई क्रिया नहीं; ‘जनयति’ (उत्पन्न करता है) इकाई ८८ से समझा गया है, जोड़ा नहीं गया। "
                   "यह पंक्ति सम्भवतः इकाई ८८ से आगे चलती है और इकाई ९० में पूरी होती है।"),
    "hook": "यदा … तदा: ढाँचा पक्का, बीच का शब्द टूटा।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "Unit 89 opens with यदा (when). Which word of the line answers it?",
            ("तदा (then)", "यदा … तदा is the when … then pair; तदा is printed after अवयवः."),
            [("तस्य (of that)", "तस्य is a genitive pronoun, not the 'then' word."),
             ("अवयवः (part)", "अवयवः is a noun, part or limb."),
             ("पुनः (again)", "पुनः is not printed in this line.")],
            "The line is a when … then frame: यदा तस्य अवयवः … तदा …",
            "यदा (when) is answered by तदा (then)."),
        match(1, "Match each sure word of unit 89 to its meaning on the card.",
              [["यदा", "when"], ["तस्य", "its, of that"], ["अवयवः", "part, limb"], ["तदा", "then"]],
              "These four are the sure words of the line; the rest is unclear in print.",
              "यदा = when; तस्य = of that; अवयव = part; तदा = then."),
        T(order(2, "Put the sure words of unit 89 in their printed order.",
                ["यदा", "तस्य", "अवयवः", "तदा"],
                "The line reads यदा तस्यावयवस्तदा…: when, of that, part, then.",
                "यदा → तस्य → अवयवः → तदा.", role="extend"),
          "The four sure words are printed as यदा तस्यावयवस्तदा, with two joins inside one token."),
        mcq("discriminate", 3, "Which split of अवयवस्तदा is right?",
            ("अवयवः + तदा", "A visarga before त becomes स्: अवयवः + तदा → अवयवस्तदा."),
            [("अवयवाः + तदा", "The plural अवयवाः would join as अवयवास्तदा, with a long आ."),
             ("अवयवम् + तदा", "म् before त would be written अवयवं तदा, not with स्."),
             ("अवयव + स्तदा", "स्तदा is not a word.")],
            "अवयवः (part, nom. sg.) + तदा (then): visarga → स् before त.",
            "Visarga + त → स्त."),
        multi("apply", 4, "Which two are right about unit 89 by the card?",
              [("It gives the full result in its own words", "The clause has no predicate; nothing is completed here."),
               ("It is a prose line, not a verse", "Right: the unit is prose."),
               ("तस्य is a genitive: its, of that", "Right: the card gives तस्य as m./n. gen. sg."),
               ("Its verb जनयति is printed in it", "जनयति is not printed; the data only takes it as understood from unit 88.")],
              [1, 2],
              "Unit 89 is a short prose line; तस्य is genitive; no verb is printed.",
              "Prose, no predicate; तस्य = of that."),
        T(mcq("transfer", 5, "By the rule of तस्यावयवः, how is तस्य + अश्वः (his horse) written when joined?",
              ("तस्याश्वः", "अ + अ → आ, as in तस्य + अवयवः → तस्यावयवः."),
              [("तस्यश्वः", "The two short अ do not lose a vowel; they merge into आ."),
               ("तस्योश्वः", "अ + अ does not give ओ."),
               ("तस्यैश्वः", "अ + अ does not give ऐ.")],
              "तस्य + अवयवः → तस्यावयवः; so तस्य + अश्वः → तस्याश्वः.",
              "अ + अ → आ."),
          "A final अ and an initial अ merge into one long आ."),
    ],
}

# ---------------------------------------------------------------- unit 90
AUTHORED["90"] = {
    "title": "तस्या जातं जातं म्रियते",
    "question": "What does unit 90 say happens to each one born of her?",
    "rule": "Of her, each one born dies (जातं जातं = each one born, by repetition).",
    "limits": ("The line does not say who 'she' is in its own words; the data takes it as giving the result of the damaged "
               "unit 89 (not firm). No cause is named in this line and no remedy."),
    "explain_hi": ("यह छोटी, साफ़ गद्य-पंक्ति है: उसका जन्मा-जन्मा मर जाता है। ‘जातं जातम्’ की दोहराई का अर्थ है ‘हर एक जन्मा’। "
                   "‘तस्याः’ (उसका, स्त्रीलिंग षष्ठी) का विसर्ग ‘ज’ से पहले गिर गया है, इसलिए ‘तस्या जातम्’ छपा है; यह नियमित सन्धि है। "
                   "‘म्रियते’ वर्तमान काल का रूप है: मरता है। "
                   "यह पंक्ति सम्भवतः इकाई ८९ का परिणाम बताती है।"),
    "hook": "जातं जातं म्रियते: जो-जो जन्मा, वह मरा।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 90, what happens to each one born of her?",
            ("It dies", "जातं जातं म्रियते: each one born dies."),
            [("It is born deaf", "Deafness is not named in this line."),
             ("It is born barren", "Barrenness is not named in this line."),
             ("It lives but is weak", "The verb म्रियते says it dies.")],
            "Of her, each one born dies.",
            "म्रियते = dies."),
        order(1, "Put the three parts of unit 90 in their printed order.",
              ["तस्या", "जातं जातं", "म्रियते"],
              "Of her … each one born … dies.",
              "तस्या → जातं जातं → म्रियते."),
        match(2, "Match each part of unit 90 to its meaning on the card.",
              [["तस्याः", "of her"], ["जातं जातम्", "each one born"], ["म्रियते", "dies"]],
              "The three parts make the whole line: of her, each one born dies.",
              "तस्याः = of her; जातं जातम् = each one born; म्रियते = dies.",
              role="extend",
              teaches="A word said twice (जातं जातम्) means each and every one: each one born."),
        mcq("discriminate", 3, "Why is तस्याः printed as तस्या before जातम्?",
            ("Visarga after आ drops before ज", "ज is voiced, so तस्याः + जातम् → तस्या जातम्."),
            [("Visarga becomes र् before ज", "र् comes only after vowels other than अ/आ."),
             ("Visarga becomes श् before ज", "Visarga becomes श् only before a palatal च, छ or श, never before voiced ज."),
             ("A letter is lost in the print", "The note calls it regular sandhi, not a print loss.")],
            "आः before a voiced consonant loses its visarga: तस्या जातम्.",
            "आः + voiced consonant → आ."),
        mcq("apply", 4, "Which English of तस्या जातं जातं म्रियते is right?",
            ("Of her, each one born dies", "तस्याः = of her; जातं जातम् = each one born; म्रियते = dies."),
            [("Of him, each one born dies", "तस्याः is feminine: of her, not of him."),
             ("She dies at each birth", "तस्याः is genitive; she is not the one who dies."),
             ("Of her, each one born lives", "म्रियते means dies, not lives.")],
            "Feminine genitive, repeated participle, verb 'dies'.",
            "तस्याः (f. gen.) + जातं जातम् + म्रियते."),
        T(mcq("transfer", 5, "Built like जातं जातम्, what does an invented गृहे गृहे mean?",
              ("In every house", "A word said twice means each one: house after house."),
              [("In two houses only", "Repetition means every one, not just two."),
               ("In a very big house", "Repetition does not mean size here."),
               ("In no house at all", "Nothing in it denies.")],
              "जातं जातम् = each one born; गृहे गृहे = in each house.",
              "X X (repeated) = each X."),
          "A word repeated means each and every one: जातं जातम्, गृहे गृहे."),
    ],
}

# ---------------------------------------------------------------- unit 91
AUTHORED["91"] = {
    "title": "यदा पुनः सोऽवयवः",
    "question": "In unit 91, of what is 'that part' (avayava) said to be one part (ekadeśa)?",
    "rule": ("When again that part (avayava) is one part (ekadeśa) of those seed-portions (bījāṃśa) that produce the "
             "female-making (ones) and the body-dependent (ones) beginning with downward heaviness ..."),
    "limits": ("Low confidence. No predicate; the result comes in unit 92. स्त्रीकरण (female-making) and अधोगुरुत्व "
               "(downward heaviness) are literal, not firm, and आदि gives no list. The printed स्त्रीकरणां may lack ना "
               "(possible, not firm). No question rests on their meaning; the order question uses only their position."),
    "explain_hi": ("यह लम्बा, अधूरा गद्य-वाक्य है; इसका परिणाम इकाई ९२ में आता है। "
                   "पक्का ढाँचा यह है: जब फिर वह अवयव उन बीजांशों का एक देश (एक भाग) है, जो कुछ चीज़ों के निर्वर्तक (बनाने वाले) हैं। "
                   "वे चीज़ें हैं ‘स्त्रीकरण’ और शरीर में आश्रित ‘अधोगुरुत्व आदि’; इन शब्दों का अर्थ शाब्दिक है और पक्का नहीं। "
                   "छपा ‘स्त्रीकरणां’ शायद ‘स्त्रीकरणानाम्’ हो (सम्भव पाठ, पक्का नहीं)। ‘सोऽवयवः’ में सः + अवयवः की सन्धि है।"),
    "hook": "वह अवयव = उन निर्वर्तक बीजांशों का एक देश।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 91, that part (avayava) is one part of what?",
            ("Of the producing seed-portions", "निर्वर्तका ये बीजांशाः, तेषाम् एकदेशः."),
            [("Of the whole of the mother's blood", "Blood is not named in this line."),
             ("Of the uterus of the mother itself", "The uterus is not named in this line."),
             ("Of the father's body as a whole", "No father is named in this line.")],
            "The part is one part (एकदेश) of those seed-portions (बीजांश) that produce (निर्वर्तक).",
            "तेषाम् (of those बीजांश) एकदेशः."),
        order(1, "Put these phrases of unit 91 in their printed order.",
              ["यदा पुनः", "सोऽवयवः", "स्त्रीकरणां च", "शरीरसंश्रयाणामधोगुरुत्वादीनां", "निर्वर्तका ये बीजांशाः",
               "तेषामेकदेशः"],
              "When again, that part, of the female-making and the body-dependent (ones), the producing seed-portions, "
              "one part of those.",
              "यदा पुनः → सोऽवयवः → स्त्रीकरणां च → शरीरसंश्रयाणाम्… → निर्वर्तका ये बीजांशाः → तेषामेकदेशः."),
        T(match(2, "Match each word of unit 91 to its meaning on the card.",
                [["पुनः", "again, further"], ["निर्वर्तक", "producing, forming"], ["बीजांश", "seed-portion"],
                 ["एकदेश", "one part"], ["संश्रय", "dependent on, resting in"]],
                "These five words carry the sure frame of the sentence.",
                "पुनः, निर्वर्तक, बीजांश, एकदेश, संश्रय.", role="extend"),
          "एकदेश = एक (one) + देश (part, place): one part of a whole."),
        mcq("discriminate", 3, "Which split of सोऽवयवः is right?",
            ("सः + अवयवः", "अः before अ gives ओ and the अ is shown by ऽ: सोऽवयवः."),
            [("सा + अवयवः", "आ + अ would join as सावयवः."),
             ("सो + वयवः", "सो and वयवः are not the card's words."),
             ("सः + वयवः", "सः before a consonant loses its visarga (स वयवः), with no ओ or ऽ; and वयवः is not a word.")],
            "सः (that) + अवयवः (part): अः + अ → ओऽ.",
            "अः + अ → ओ + ऽ."),
        multi("apply", 4, "Which two does unit 91 state plainly, by the card?",
              [("That part is one part (एकदेश) of those seed-portions", "Right: तेषाम् एकदेशः."),
               ("The full list after आदि (etc.) is given", "आदि (beginning with) gives no list here."),
               ("A verb (क्रिया) closes the line", "The line has no predicate; the result follows in unit 92."),
               ("The seed-portions are called producing (निर्वर्तक)", "Right: निर्वर्तका ये बीजांशाः.")],
              [0, 3],
              "The sure frame: that part is one part of the producing seed-portions.",
              "निर्वर्तका ये बीजांशाः, तेषाम् एकदेशः."),
        T(mcq("transfer", 5, "By the rule of बीजांशास्तेषाम्, how is देवाः + तत्र written when joined?",
              ("देवास्तत्र", "Visarga before त becomes स्: देवास्तत्र."),
              [("देवा तत्र", "The visarga drops only before a voiced sound; त is voiceless."),
               ("देवोस्तत्र", "आः does not turn into ओ."),
               ("देवार्तत्र", "र् is not used after आ.")],
              "बीजांशाः + तेषाम् → बीजांशास्तेषाम्; so देवाः + तत्र → देवास्तत्र.",
              "आः + त → आस्त."),
          "A visarga before त or थ becomes स्."),
    ],
}

# ---------------------------------------------------------------- unit 92
AUTHORED["92"] = {
    "title": "वार्तां नाम जनयति",
    "question": "What does unit 92 say is then produced, and by what name?",
    "rule": ("Then it produces (one) mostly of form and shape, a non-woman (astrī), named vārtā."),
    "limits": ("जनयति has no stated subject. रूपाकृतिप्राया does not say whose form and shape; a dropped स्त्री- "
               "(of a woman) is only a conjecture, not applied or asked. वार्ता is a name. The sentence appears to "
               "begin in unit 91 (not firm)."),
    "explain_hi": ("यह पंक्ति सम्भवतः इकाई ९१ के अधूरे वाक्य को पूरा करती है (पक्का नहीं): तब वह (कर्ता अनकहा) एक ऐसी को उत्पन्न करता है जो रूप और आकृति की "
                   "प्रधानता वाली है, पर अस्त्री, यानी स्त्री नहीं है; उसका नाम वार्ता है। "
                   "‘किसका रूप-आकृति’, यह छपा पाठ नहीं बताता; ‘स्त्री-’ छूटा होने का अनुमान है, पर लागू नहीं किया गया। "
                   "‘अस्त्री’ में अ- निषेध है: स्त्री नहीं। ‘वार्ता’ एक नाम है, इसका अनुवाद नहीं किया गया।"),
    "hook": "रूप-आकृति में, पर स्त्री नहीं: नाम वार्ता।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 92, what is the one produced named?",
            ("वार्ता", "वार्तां नाम जनयति: it produces (one) named vārtā."),
            [("वन्ध्या", "The barren one is what is produced in unit 88."),
             ("मृणासुलिङ्गा", "That name belongs to the man's side, in unit 94."),
             ("कुब्जा", "No such name is printed here.")],
            "The one produced is named vārtā.",
            "वार्ता नाम = named vārtā."),
        order(1, "Put the words of unit 92 in their printed order.",
              ["तदा", "रूपाकृतिप्रायाम्", "अस्त्रियम्", "वार्तां नाम", "जनयति"],
              "Then … mostly of form and shape … a non-woman … named vārtā … it produces.",
              "तदा → रूपाकृतिप्रायाम् → अस्त्रियम् → वार्तां नाम → जनयति."),
        T(match(2, "Match each word of unit 92 to its meaning on the card.",
                [["रूप", "form"], ["आकृति", "shape"], ["प्राय", "mostly, chiefly"], ["अस्त्री", "non-woman"],
                 ["जनयति", "produces"]],
                "These five words describe the one produced and what the unstated subject does.",
                "रूप, आकृति, प्राय, अस्त्री, जनयति.", role="extend"),
          "-प्राय at the end of a compound = mostly, chiefly: रूपाकृतिप्राया = mostly of form and shape."),
        mcq("discriminate", 3, "Which split of प्रायामस्त्रियम् is right?",
            ("प्रायाम् + अस्त्रियम्", "म् joins the next vowel अ: प्रायामस्त्रियम्."),
            [("प्रायाम् + स्त्रियम्", "Then no अ would follow म; the print has मस्त्रि, and the card reads non-woman."),
             ("प्रायम् + अस्त्रियम्", "That would join as प्रायमस्त्रियम्, with a short अ before म."),
             ("प्राया + मस्त्रियम्", "मस्त्रियम् is not a word.")],
            "प्रायाम् (f. acc. sg.) + अस्त्रियम् (non-woman).",
            "Final म् + vowel → म joins the vowel."),
        mcq("apply", 4, "What does अस्त्रियम् tell about the one produced in unit 92?",
            ("She is not a woman", "अ- negates स्त्री: a non-woman."),
            [("She is a woman of great beauty", "अ- denies, it does not praise."),
             ("She is mostly of male shape", "Male shape is said of the man's side, in unit 94."),
             ("She is a woman who bears twins", "Nothing about twins is said.")],
            "अस्त्री = अ + स्त्री: not a woman.",
            "अ- before a consonant = not."),
        T(mcq("transfer", 5, "By the pattern of अस्त्री (अ + स्त्री), what does अदृष्ट (अ + दृष्ट, seen) mean?",
              ("Not seen", "अ- negates: अदृष्ट = not seen."),
              [("Seen well", "अ- does not strengthen the word."),
               ("Seen before", "अ- does not mean before."),
               ("Seen by all", "अ- does not mean all.")],
              "अ + स्त्री → अस्त्री (non-woman); अ + दृष्ट → अदृष्ट (not seen).",
              "अ- before a consonant = not."),
          "The prefix अ- before a consonant negates the word: अस्त्री, अदृष्ट."),
    ],
}

# ---------------------------------------------------------------- unit 93
AUTHORED["93"] = {
    "title": "तां स्त्रीव्यापदमाचक्षते",
    "question": "What do they call her in unit 93?",
    "rule": "They call her a strī-vyāpad (literally a woman's ruin or defect).",
    "limits": ("'Woman's defect' is a literal reading of the compound; it may be a technical name. Who 'they' are is not "
               "said. The data takes the line as closing units 91 and 92."),
    "explain_hi": ("यह छोटी पंक्ति कहती है: उसे स्त्रीव्यापद् कहते हैं। ‘व्यापद्’ का अर्थ है विनाश, विफलता या दोष। "
                   "‘स्त्रीव्यापद्’ को एक पारिभाषिक नाम की तरह रखा गया है; ‘स्त्री का दोष’ उसका शाब्दिक अर्थ है। "
                   "‘आचक्षते’ बहुवचन क्रिया है: वे कहते हैं; कहने वाले कौन हैं, यह नहीं बताया। "
                   "‘ताम्’ सम्भवतः इकाई ९२ की उसी अस्त्री की ओर है।"),
    "hook": "उसे कहते हैं: स्त्रीव्यापद्।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 93, what do they call her?",
            ("A strī-vyāpad", "तां स्त्रीव्यापदम् आचक्षते."),
            [("A barren one", "The barren one is named in unit 88."),
             ("A pregnant one (गर्भिणी)", "Pregnancy is not named in this line."),
             ("A kind of ṣaṇḍha (impotent man)", "The ṣaṇḍha kinds (impotent men) belong to earlier units.")],
            "They call her a strī-vyāpad.",
            "आचक्षते = they call."),
        order(1, "Put the words of unit 93 in their printed order.",
              ["तां", "स्त्रीव्यापदम्", "आचक्षते"],
              "Her … a strī-vyāpad … they call.",
              "तां → स्त्रीव्यापदम् → आचक्षते."),
        T(match(2, "Match each word of unit 93 to its meaning on the card.",
                [["ताम्", "her, that"], ["स्त्री", "woman"], ["व्यापद्", "ruin, failure, defect"],
                 ["आचक्षते", "they call"]],
                "Four words make the line: her, woman, defect, they call.",
                "ताम्, स्त्री, व्यापद्, आचक्षते.", role="extend"),
          "व्यापद् means ruin, failure or defect; स्त्रीव्यापद् is kept as a term."),
        mcq("discriminate", 3, "Which split of स्त्रीव्यापदमाचक्षते is right?",
            ("स्त्रीव्यापदम् + आचक्षते", "म् joins the vowel आ: …दमाचक्षते."),
            [("स्त्रीव्यापदम् + अचक्षते", "That would join as …दमचक्षते, with a short अ."),
             ("स्त्रीव्यापदा + आचक्षते", "आ + आ would join as …दाचक्षते, with no म."),
             ("स्त्रीव्यापद + माचक्षते", "माचक्षते is not a word.")],
            "स्त्रीव्यापदम् (acc. sg.) + आचक्षते (they call).",
            "Final म् + vowel → म joins the vowel."),
        mcq("apply", 4, "Who is the subject of आचक्षते in unit 93?",
            ("An unnamed 'they'", "आचक्षते is 3rd person plural; no subject is printed."),
            [("The woman herself, as the speaker", "She is the object ताम्, and the verb is plural."),
             ("One single teacher, left unnamed", "The verb is plural, not singular."),
             ("Her own father, speaking alone", "No father is named, and the verb is plural.")],
            "The verb is 3 pl.: they call; the speakers are not named.",
            "आचक्षते = 3 pl. pres. ātm.: they call."),
        T(mcq("transfer", 5, "Built like तां स्त्रीव्यापदम् आचक्षते, what does an invented तं वैद्यम् आचक्षते mean?",
              ("They call him a physician", "तम् (him) + वैद्यम् (a physician) + आचक्षते (they call)."),
              [("He calls them physicians", "तम् is the singular object; the verb is plural."),
               ("The physician is calling him", "वैद्यम् is accusative, not the subject."),
               ("They called the physician", "आचक्षते is present, not past.")],
              "As तां … आचक्षते = they call her …, तं वैद्यम् आचक्षते = they call him a physician.",
              "Object + name in the accusative + आचक्षते = they call X Y."),
          "आचक्षते takes two accusatives: the one named and the name (they call X Y)."),
    ],
}

# ---------------------------------------------------------------- unit 94
AUTHORED["94"] = {
    "title": "एवमेव पुंसो यदा",
    "question": "How does unit 94 extend the woman's pattern to the man, and which further deformities does it say are explained by this?",
    "rule": ("In the same way for a man, one applies the pattern 'when the seed is vitiated' and so on: it produces a barren "
             "(one), and (one) mostly of male shape, a non-male. By this explanation of the deformity of mother-born and "
             "father-born parts, that of the parts born of sātmya, rasa and sattva is explained too."),
    "limits": ("Low confidence. शुकरारख्ये as शुक्राख्ये (called śukra) is only a possible correction; पूतिप्रज is "
               "conjectural; the name मृणासुलिंगा is unclear. No question rests on these. Rasa = nutritive fluid "
               "(probable); sattva = mind (standard). जनयति has no stated subject."),
    "explain_hi": ("यह इकाई स्त्री के पक्ष (इकाई ८८) का नियम पुरुष पर लगाती है: ‘जब बीज दूषित होता है’ इत्यादि वैसे ही जोड़ लो। "
                   "पुरुष के पक्ष में बन्ध्य, (अनुमानित पाठ पर) बिगड़ी सन्तान वाला, और पुरुष की आकृति की प्रधानता वाला अपुरुष उत्पन्न होता है; "
                   "उसका छपा नाम ‘मृणासुलिंगा’ अस्पष्ट है। "
                   "फिर एक सामान्य सिद्धान्त: माता से और पिता से उत्पन्न अवयवों की विकृति के इस व्याख्यान से, "
                   "सात्म्य से, रस से (पोषक रस, सम्भावित) और सत्त्व (मन) से उत्पन्न अवयवों की विकृति भी समझा दी गई।"),
    "hook": "माता-पिता वाला नियम समझा, तो सात्म्य, रस, सत्त्व वाला भी समझा।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 94, the deformity of which further parts is explained by this same account?",
            ("Parts born of sātmya, rasa and sattva", "सात्म्यजानां रसजानां सत्त्वजानां च अवयवानां विकृतिः व्याख्याता."),
            [("Parts born of Vāta, Pitta and Kapha", "The doṣas are not the three groups named here."),
             ("Parts born of the five great elements", "The elements are not named in this unit."),
             ("Parts born of the six seasons of the year", "Seasons are not named in this unit.")],
            "By the account of mother-born and father-born parts, those born of sātmya, rasa and sattva are explained too.",
            "सात्म्यज, रसज, सत्त्वज: explained by this."),
        order(1, "Put these phrases of unit 94 in their printed order.",
              ["एवमेव पुंसः", "बीजं प्रदुष्यतीत्यादि योजयेत्", "वन्ध्यं पूतिप्रजं", "पुरुषाकृतिप्रायमपुरुषम्",
               "मातृजानां पितृजानां च", "सात्म्यजानां रसजानां सत्त्वजानां च"],
              "The man's case, the rule applied, what is produced, then the two explained groups and the three further ones.",
              "पुंसः → योजयेत् → वन्ध्यम् → अपुरुषम् → मातृज/पितृज → सात्म्यज/रसज/सत्त्वज."),
        T(match(2, "Match each word of unit 94 to its meaning on the card.",
                [["मातृज", "mother-born"], ["पितृज", "father-born"], ["सात्म्यज", "born of sātmya (what suits)"],
                 ["रसज", "born of rasa (nutritive fluid; probable)"], ["सत्त्वज", "born of sattva (mind)"]],
                "The first two groups are explained; by them the last three are explained as well.",
                "-ज = born of: मातृ, पितृ, सात्म्य, रस, सत्त्व.", role="extend"),
          "-ज at the end of a compound means born of: मातृज = born of the mother."),
        mcq("discriminate", 3, "What does एवमेव पुंसो … इत्यादि योजयेत् ask the reader to do?",
            ("Apply the woman's pattern to the man", "The quoted 'when … the seed is vitiated' repeats unit 88's pattern for the man."),
            [("Learn a new rule unlike the woman's", "एवमेव (in just the same way) says it is the same pattern."),
             ("Leave out the man's case altogether", "योजयेत् says the pattern should be applied."),
             ("Treat the man with Vāta-pacifying remedies", "No remedy is named in this unit.")],
            "एवमेव = in just the same way; योजयेत् = one should apply (it).",
            "एवम् एव … इत्यादि योजयेत् = apply the same pattern."),
        multi("apply", 4, "Which two does unit 94 name among what is produced on the man's side?",
              [("A barren one (वन्ध्यम्)", "Right: वन्ध्यम् is printed."),
               ("A non-woman named vārtā", "That is the woman's side, in unit 92."),
               ("One mostly of male shape, a non-male", "Right: पुरुषाकृतिप्रायम् अपुरुषम्."),
               ("One who is deaf and mute (बधिर, मूक)", "Deaf and mute are Vāta effects in the embryo, in unit 97.")],
              [0, 2],
              "On the man's side it produces a barren one and one mostly of male shape, a non-male.",
              "वन्ध्यम्; पुरुषाकृतिप्रायम् अपुरुषम्."),
        T(mcq("transfer", 5, "By the pattern of मातृज (born of the mother), what does an invented जलज mean?",
              ("Born of water", "जल (water) + -ज (born of)."),
              [("Giver of water", "-ज means born of, not giving."),
               ("Lord of water", "-ज does not mean lord."),
               ("Free of water", "-ज does not mean free of.")],
              "मातृ + ज = born of the mother; जल + ज = born of water.",
              "X + -ज = born of X."),
          "-ज (from √जन्, to be born) after a noun means born of it."),
    ],
}

# ---------------------------------------------------------------- unit 95
AUTHORED["95"] = {
    "title": "यस्य अंगावयवस्य",
    "question": "By unit 95, which limb-part comes to a deformity?",
    "rule": ("Of whichever limb-part (aṅga-avayava), in its seed or seed-portion, an origin (utpatti) occurs, of that "
             "very limb-part a deformity (vikṛti) arises."),
    "limits": ("Low confidence. The printed उत्पत्ति (origin) is odd here; the data notes upatāpa (affliction) as a possible "
               "reading but translates the print as given. No question rests on the meaning of उत्पत्ति. The pairing "
               "with unit 96 is not asserted."),
    "explain_hi": ("यह पंक्ति एक सामान्य नियम देती है: जिस अंग-अवयव के बीज में या बीजांश में ‘उत्पत्ति’ होती है, उसी-उसी अंग-अवयव की विकृति उत्पन्न होती है। "
                   "‘यस्य … तस्य तस्य’ का ढाँचा कहता है: जिसका …, उसी का। "
                   "छपा ‘उत्पत्ति’ यहाँ अटपटा है; ‘उपताप’ (पीड़ा) एक सम्भावित पाठ माना गया, पर लागू नहीं किया गया। "
                   "‘अंगावयव’ = अङ्ग + अवयव, अंग का भाग।"),
    "hook": "जिस अंग के बीज में बात, उसी अंग में विकृति।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 95, where does the deformity arise?",
            ("In that very limb-part", "तस्य तस्य अङ्गावयवस्य विकृतिः उपजायते."),
            [("In all the limbs at once", "The line ties it to that one limb-part only."),
             ("In the mother's uterus", "The uterus is not named in this line."),
             ("In the father's seed itself", "No father is named in this line.")],
            "The deformity arises in the very limb-part whose seed or seed-portion is concerned.",
            "यस्य … तस्य तस्य = of whichever … of that very."),
        order(1, "Put these phrases of unit 95 in their printed order.",
              ["यस्य अंगावयवस्य", "बीजे बीजांशे वा", "उत्पत्तिर्भवति", "तस्य तस्यांगावयवस्य", "विकृतिरुपजायते"],
              "Of whichever limb-part … in seed or seed-portion … (printed) origin occurs … of that very limb-part … "
              "deformity arises.",
              "यस्य … → बीजे बीजांशे वा → उत्पत्तिर्भवति → तस्य तस्य … → विकृतिरुपजायते."),
        T(match(2, "Match each word of unit 95 to its meaning on the card.",
                [["अङ्ग", "limb"], ["अवयव", "part"], ["बीजांश", "seed-portion"], ["विकृति", "deformity"],
                 ["उपजायते", "arises"]],
                "These five words carry the sure parts of the rule.",
                "अङ्ग, अवयव, बीजांश, विकृति, उपजायते.", role="extend"),
          "विकृति = deformity, abnormality; उपजायते = arises, is produced."),
        mcq("discriminate", 3, "Which split of अंगावयवस्य is right?",
            ("अङ्ग + अवयवस्य", "अ + अ → आ: अङ्गावयवस्य."),
            [("अङ्गम् + अवयवस्य", "म् + अ would give अङ्गमवयवस्य."),
             ("अङ्ग + वयवस्य", "That would be अङ्गवयवस्य, with a short अ."),
             ("अङ्गी + अवयवस्य", "ई + अ would give अङ्ग्यवयवस्य.")],
            "अङ्ग (limb) + अवयवस्य (of the part).",
            "अ + अ → आ."),
        mcq("apply", 4, "A translation reads: 'of whichever limb-part … an origin occurs, of all other limb-parts a deformity arises.' Which words are wrong?",
            ("of all other", "तस्य तस्य = of that very (limb-part), not of all others."),
            [("of whichever", "यस्य = of whichever: this is right."),
             ("a deformity", "विकृतिः = deformity: this is right."),
             ("arises", "उपजायते = arises: this is right.")],
            "The text says: of that very limb-part a deformity arises.",
            "तस्य तस्य = of that very one."),
        T(mcq("transfer", 5, "By the rule of विकृतिरुपजायते, how is an invented मतिः + अस्ति written when joined?",
              ("मतिरस्ति", "Visarga after इ becomes र् before a vowel."),
              [("मतिस्ति", "The visarga and the अ cannot both vanish."),
               ("मत्यस्ति", "That would need मति without a visarga."),
               ("मतिरास्ति", "The short अ of अस्ति stays short.")],
              "विकृतिः + उपजायते → विकृतिरुपजायते; so मतिः + अस्ति → मतिरस्ति.",
              "इः + vowel → इर् + vowel."),
          "A visarga after इ (or any vowel but अ/आ) becomes र् before a vowel."),
    ],
}

# ---------------------------------------------------------------- unit 96
AUTHORED["96"] = {
    "title": "नोपजायतेऽनुपत्तापात्",
    "question": "What does unit 96 say does not arise, and why?",
    "rule": "(It) does not arise, because of the absence of affliction (an-upatāpa).",
    "limits": ("Elliptical: the subject (the deformity of unit 95) is understood, not printed. The printed अनुपत्तापात् is "
               "read अनुपतापात् (an-upatāpa), its double त् a print slip, as the data does; questions use that reading, "
               "none the printed spelling. Its pairing with unit 95 is not asserted."),
    "explain_hi": ("यह छोटी पंक्ति कहती है: (वह) उत्पन्न नहीं होती, उपताप (पीड़ा) न होने से। "
                   "कर्ता छपा नहीं; वह इकाई ९५ की विकृति समझी गई है। "
                   "‘अनुपतापात्’ में ‘अन्’ निषेध है और ‘-आत्’ पंचमी विभक्ति कारण बताती है: ‘के कारण’। "
                   "छपा ‘अनुपत्तापात्’ का दोहरा त् छपाई की भूल माना गया है।"),
    "hook": "पीड़ा नहीं, तो विकृति नहीं।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 96, why does (the deformity) not arise?",
            ("Because there is no affliction", "अनुपतापात्: from the absence of affliction."),
            [("Because of the mother's daily diet", "Diet is not named in this line."),
             ("Because of the father's great age", "Age is not named in this line."),
             ("Because of the season of the birth", "No season is named in this line.")],
            "It does not arise because of the absence of affliction.",
            "अन्-उपताप-आत् = because of no affliction."),
        match(1, "Match each word of unit 96 to its meaning on the card.",
              [["न", "not"], ["उपजायते", "arises"], ["अनुपतापात्", "because of absence of affliction"]],
              "Three words make the line: not, arises, because of no affliction.",
              "न, उपजायते, अनुपतापात्."),
        T(mcq("extend", 2, "What does the ending -आत् of अनुपतापात् express here?",
              ("The cause: because of", "The ablative here gives the reason: because of the absence of affliction."),
              [("The place: in, on", "Place would be a locative, ending -ए."),
               ("A person addressed: O!", "That would be a vocative."),
               ("The object of the verb", "उपजायते (arises) takes no object.")],
              "-आत् is the ablative singular of an अ-stem; here it gives the reason.",
              "Ablative -आत् = from, because of."),
          "The ablative ending -आत् can give the reason: X-आत् = because of X."),
        mcq("discriminate", 3, "Which split of नोपजायते is right?",
            ("न + उपजायते", "अ + उ → ओ: नोपजायते."),
            [("नः + उपजायते", "That would give न उपजायते, with a gap."),
             ("नो + पजायते", "पजायते is not a word."),
             ("न + ओपजायते", "ओपजायते is not a word.")],
            "न (not) + उपजायते (arises).",
            "अ + उ → ओ."),
        multi("apply", 4, "Which two are right about unit 96 by the card?",
              [("It names the limb that is affected", "No limb is named in this line."),
               ("Its subject, the deformity, is understood, not printed", "Right: the subject comes from unit 95."),
               ("It is a metrical verse line", "The unit is prose."),
               ("न + उपजायते join as नोपजायते", "Right: अ + उ → ओ.")],
              [1, 3],
              "A short prose line; its subject is understood from unit 95.",
              "Elliptical prose; न + उपजायते → नोपजायते."),
        T(mcq("transfer", 5, "By the rule of उपजायतेऽनुपतापात्, how is an invented वने + अस्मिन् written when joined?",
              ("वनेऽस्मिन्", "A final ए before अ stays ए; the अ is shown by ऽ."),
              [("वनास्मिन्", "ए does not turn into आ."),
               ("वनायस्मिन्", "ए + अ does not give आय here."),
               ("वनोऽस्मिन्", "ए does not turn into ओ.")],
              "उपजायते + अनुपतापात् → उपजायतेऽनुपतापात्; so वने + अस्मिन् → वनेऽस्मिन्.",
              "ए + अ → एऽ."),
          "A final ए before अ stays ए and the अ is dropped, shown by ऽ (avagraha)."),
    ],
}

# ---------------------------------------------------------------- unit 97
AUTHORED["97"] = {
    "title": "यदा च लब्धगर्भा",
    "question": "What does unit 97 say provoked Vāyu produces in the embryo when a pregnant woman resorts to Vāta-increasing things?",
    "rule": ("When a pregnant woman resorts to Vāta-increasing (ones), her provoked Vāyu, moving along the body and lodging "
             "in the uterus, produces in the embryo dullness, deafness, muteness, nasal voice (minmiṇa; probable), stammering, lameness, "
             "hunchback, dwarfism, deficient or excessive limbs, or another Vāta disorder."),
    "limits": ("Low confidence only for one word: the printed अनक्षम् is unclear (conjecturally अनिशम्, constantly) and no "
               "question rests on it. मिन्मिण as nasal or indistinct speech is probable. The unit names no remedy and "
               "no dose."),
    "explain_hi": ("और जब गर्भवती स्त्री वात बढ़ाने वालों (वातल) का सेवन करती है, तब उसका प्रकुपित वायु शरीर में सरकता हुआ गर्भाशय में ठहरता है। "
                   "वहाँ वह गर्भ में ये अवस्थाएँ उत्पन्न करता है: जड़ता, बहरापन, गूँगापन, नकियापन (सम्भावित), हकलापन, लंगड़ापन, "
                   "कुबड़ापन, बौनापन, अंगों की कमी और अंगों की अधिकता, या कोई दूसरा वात-विकार। "
                   "लम्बे समास के अन्त का ‘-त्व’ पूरी सूची पर लगता है: ‘-पन’। "
                   "छपा ‘अनक्षम्’ अस्पष्ट है; ‘अनिशम्’ (निरन्तर) केवल अनुमान है।"),
    "hook": "गर्भिणी ने वातल का सेवन किया: वात गर्भाशय में बैठा, गर्भ में जड़-बधिर-मूक …",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 97, what does the pregnant woman resort to that sets this off?",
            ("Vāta-increasing ones", "वातलानि आसेवते: she resorts to Vāta-increasing (ones)."),
            [("Pitta-increasing measures", "Pitta is not named in this unit."),
             ("Kapha-increasing foods", "Kapha is not named in this unit."),
             ("Cold baths at night", "Nothing of the kind is named.")],
            "She resorts to Vāta-increasing (vātala; standard) things; her Vāyu is provoked.",
            "वातल = Vāta-increasing."),
        order(1, "Put the steps of unit 97 in their printed order.",
              ["लब्धगर्भा वातलान्यासेवते", "वायुः प्रकुपितः", "शरीरमनुसर्पन्", "गर्भाशयेऽवतिष्ठमानः",
               "गर्भस्य … वातविकारं करोति"],
              "She resorts to Vāta-increasing things → Vāyu is provoked → moves along the body → lodges in the "
              "uterus → produces Vāta disorders in the embryo.",
              "सेवन → प्रकोप → अनुसर्पण → गर्भाशय में स्थिति → विकार."),
        T(match(2, "Match each item of unit 97's list to its meaning on the card.",
                [["जड", "dull"], ["बधिर", "deaf"], ["मूक", "mute"], ["खंज", "lame"], ["कुब्ज", "hunchbacked"],
                 ["वामन", "dwarfish"]],
                "Six of the items that provoked Vāyu produces in the embryo.",
                "जड, बधिर, मूक, खंज, कुब्ज, वामन.", role="extend"),
          "The list is one long compound; the ending -त्व (-ness) applies to every member."),
        mcq("discriminate", 3, "Which pair of opposites stands in unit 97's list?",
            ("Deficient limbs and excessive limbs", "हीनाङ्ग and अधिकाङ्ग are both printed."),
            [("Deafness and blindness of the eyes", "Blindness is not in this unit's list."),
             ("Dwarfism and very tall growth", "Only dwarfism (वामन) is named."),
             ("Muteness and too much talking", "Only muteness (मूक) is named.")],
            "हीनाङ्ग (deficient in limbs) and अधिकाङ्ग (excessive in limbs) close the list.",
            "हीन ↔ अधिक."),
        multi("apply", 4, "Which two are in unit 97's list of Vāta effects in the embryo?",
              [("Baldness (खलति)", "Baldness is named under Pitta in unit 98."),
               ("Kuṣṭha", "Kuṣṭha is named under Kapha in unit 99."),
               ("Stammering (गद्गद)", "Right: गद्गद is printed in the list."),
               ("Nasal voice (मिन्मिण; probable)", "Right: मिन्मिण is printed; its sense is probable.")],
              [2, 3],
              "गद्गद and मिन्मिण are in the list; baldness and kuṣṭha belong to the next units.",
              "Vāta list: जड … अधिकाङ्ग."),
        T(mcq("transfer", 5, "By the -त्व of unit 97's list, what does an invented बधिरत्वम् mean?",
              ("Deafness", "-त्व makes an abstract noun: the state of being deaf."),
              [("A deaf man", "That would be बधिरः, without -त्व."),
               ("Making one deaf", "-त्व does not mean causing."),
               ("Many deaf people", "-त्व is not a plural ending.")],
              "जड … अधिकाङ्ग-त्वानि = the states of being dull … ; बधिर + त्व = deafness.",
              "X + -त्व = X-ness."),
          "-त्व after an adjective makes the abstract noun: बधिर (deaf) → बधिरत्व (deafness)."),
    ],
}

# ---------------------------------------------------------------- unit 98
AUTHORED["98"] = {
    "title": "तथा वायुवत्पित्तमपि",
    "question": "Which firm effects does unit 98 give for Pitta, said to act like Vāyu?",
    "rule": "Likewise Pitta too, like Vāyu, (produces) baldness (khalati), grey hair (palita), ... tawniness (paiṅgalya) and so on.",
    "limits": ("Low confidence. The middle of the compound (printed श्मश्रुहीनत्वक्छ्रनखे श) is damaged and not translated; "
               "the guess 'skin, nails, hair' is not firm. Only खलति, पलित and पैंगल्य आदि are firm, and only they are asked "
               "about. No verb is printed; 'produces' is understood from unit 97."),
    "explain_hi": ("वैसे ही, वायु की तरह, पित्त भी (गर्भ में) विकार करता है: खलति (गंजापन), पलित (बालों का सफ़ेद होना), "
                   "फिर एक क्षतिग्रस्त अंश, और पैंगल्य (पीलापन लिए भूरापन) आदि। "
                   "बीच का छपा अंश टूटा है, उसका अनुवाद नहीं किया गया। "
                   "क्रिया छपी नहीं; ‘करता है’ इकाई ९७ से समझा जाता है। ‘वायुवत्’ = वायु की तरह।"),
    "hook": "पित्त भी वायु-सा: गंजापन, सफ़ेद बाल, पैंगल्य।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 98, which doṣa is said to act like Vāyu?",
            ("Pitta", "वायुवत् पित्तम् अपि: Pitta too, like Vāyu."),
            [("Kapha", "Kapha follows in unit 99."),
             ("Blood (शोणित)", "Blood is not named in this line."),
             ("Rasa", "Rasa is not named in this line.")],
            "Likewise Pitta too, like Vāyu.",
            "वायुवत् = like Vāyu; पित्तम् = Pitta."),
        match(1, "Match each firm word of unit 98 to its meaning on the card.",
              [["वायुवत्", "like Vāyu"], ["पित्तम्", "Pitta"], ["अपि", "also"], ["खलति", "baldness (standard)"],
               ["पलित", "grey hair (standard)"]],
              "These five firm words open the line.",
              "वायुवत्, पित्तम्, अपि, खलति, पलित."),
        T(mcq("extend", 2, "What does पैंगल्य mean on the card?",
              ("Tawniness", "पैंगल्य = tawny colour, as the data glosses it."),
              [("Greying of the hair", "That is पलित."),
               ("Loss of the hair", "That is खलति, baldness."),
               ("Loss of the nails", "The nails are only in the damaged middle, not firm.")],
              "पैंगल्य आदि (tawniness and so on) closes the firm list.",
              "पैंगल्य = tawniness."),
          "पैंगल्य = tawniness, a yellowish-brown colour; आदि = and so on."),
        mcq("discriminate", 3, "Which split of पित्तमपि is right?",
            ("पित्तम् + अपि", "म् joins the vowel अ: पित्तमपि."),
            [("पित्ता + अपि", "आ + अ would join as पित्तापि."),
             ("पित्त + मपि", "मपि is not a word."),
             ("पित्तम + पि", "पित्तम and पि are not the card's words.")],
            "पित्तम् (Pitta) + अपि (also).",
            "Final म् + vowel → म joins the vowel."),
        order(4, "Put the firm items of unit 98 in their printed order (the damaged middle is left out).",
              ["खलति", "पलित", "पैंगल्य"],
              "Baldness, grey hair, then (after the damaged part) tawniness and so on.",
              "खलति → पलित → (टूटा अंश) → पैंगल्य.", role="apply"),
        T(mcq("transfer", 5, "By the pattern of वायुवत् (like Vāyu), what does an invented सिंहवत् mean?",
              ("Like a lion", "-वत् here = like: सिंहवत् = like a lion."),
              [("Without a lion", "-वत् does not mean without."),
               ("After the lion", "-वत् does not mean after."),
               ("Against a lion", "-वत् does not mean against.")],
              "वायु + वत् = like Vāyu; सिंह + वत् = like a lion.",
              "X-वत् (indeclinable) = like X."),
          "The indeclinable -वत् after a noun means like it: वायुवत् = like Vāyu."),
    ],
}

# ---------------------------------------------------------------- unit 99
AUTHORED["99"] = {
    "title": "श्लेष्मा तु",
    "question": "Which disorders does unit 99 give for Kapha (śleṣman)?",
    "rule": ("Kapha, however, (produces) kuṣṭha (leprosy and related skin disease), kilāsa (probably vitiligo), "
             "an unclear third item, and so on."),
    "limits": ("Low confidence. The third member (printed सदंतवा) is unclear and untranslated; 'toothlessness' is only a "
               "guess, so no question rests on it. Kuṣṭha (standard) may here mean a group of skin diseases; kilāsa as "
               "vitiligo is probable. No verb is printed."),
    "explain_hi": ("कफ (श्लेष्मा) तो कुष्ठ (कोढ़ और उससे जुड़े त्वचा-रोग; मानक), किलास (सफ़ेद दाग, सम्भवतः विटिलिगो) आदि (विकार उत्पन्न करता है)। "
                   "तीसरा छपा अंश ‘सदंतवा’ अस्पष्ट है, उसका अनुवाद नहीं किया गया। "
                   "‘श्लेष्मा’ श्लेष्मन् शब्द की प्रथमा एकवचन है, आ-अन्त स्त्रीलिंग नहीं। "
                   "‘तु’ (तो, किन्तु) पिछली इकाई के पित्त से कफ को अलग करता है; क्रिया पिछली इकाइयों से समझी जाती है।"),
    "hook": "कफ तो: कुष्ठ, किलास आदि।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 99, which doṣa is named with kuṣṭha and kilāsa?",
            ("Kapha", "श्लेष्मा तु कुष्ठकिलास…आदीनि."),
            [("Pitta", "Pitta is named in unit 98."),
             ("Vāyu", "Vāyu is named in unit 97."),
             ("Blood (शोणित)", "Blood is not named in this line.")],
            "Kapha, however: kuṣṭha, kilāsa and so on.",
            "श्लेष्मन् = Kapha."),
        order(1, "Put the firm parts of unit 99 in their printed order.",
              ["श्लेष्मा", "तु", "कुष्ठ", "किलास", "आदीनि"],
              "Kapha, however: kuṣṭha, kilāsa, (an unclear item), and so on.",
              "श्लेष्मा → तु → कुष्ठ → किलास → (अस्पष्ट) → आदीनि."),
        T(match(2, "Match each word of unit 99 to its meaning on the card.",
                [["श्लेष्मा", "Kapha"], ["तु", "but, however"], ["कुष्ठ", "leprosy and related skin disease (standard)"],
                 ["किलास", "white patches, probably vitiligo (probable)"]],
                "Four firm words; the third member of the compound is unclear.",
                "श्लेष्मा, तु, कुष्ठ, किलास.", role="extend"),
          "Kuṣṭha (standard) and kilāsa (probable) are the two firm Kapha disorders named."),
        mcq("discriminate", 3, "What form is श्लेष्मा in unit 99?",
            ("Nom. sg. of the n-stem श्लेष्मन्", "The card: śleṣmā is the nominative of śleṣman (m.)."),
            [("A feminine आ-stem noun, nom. sg.", "It ends in आ only because the n-stem drops its न्."),
             ("An accusative plural of श्लेष्मन्", "That would be श्लेष्मणः."),
             ("A verb in the present", "It is a noun, Kapha.")],
            "श्लेष्मन् → nominative singular श्लेष्मा.",
            "n-stem: nom. sg. drops the final न्."),
        mcq("apply", 4, "What does the ending -आदीनि tell about unit 99's list?",
            ("More disorders are meant than named", "आदि = and so on: the list is open."),
            [("Exactly three disorders are meant", "आदि leaves the list open."),
             ("Only kuṣṭha is really meant here", "Kilāsa is named as well."),
             ("The list closes the whole chapter here", "आदि says nothing about the chapter's end.")],
            "आदीनि (and so on) marks the named items as examples.",
            "आदि = beginning with, and so on."),
        T(mcq("transfer", 5, "By the pattern of श्लेष्मन् → श्लेष्मा, what is the nominative singular of राजन् (king)?",
              ("राजा", "The n-stem drops its न् in the nom. sg. and lengthens अ: राजा."),
              [("राजन्", "The bare stem is not the nom. sg."),
               ("राजः", "The n-stem does not take -ः here."),
               ("राजाः", "No visarga is added in the nom. sg.")],
              "श्लेष्मन् → श्लेष्मा; राजन् → राजा.",
              "-अन् stem (m.) → nom. sg. -आ."),
          "A masculine -अन् stem makes its nominative singular in -आ: श्लेष्मन् → श्लेष्मा, राजन् → राजा."),
    ],
}

# ---------------------------------------------------------------- unit 100
AUTHORED["100"] = {
    "title": "त्रिवर्गौमिश्रान्विकारान्",
    "question": "What in the unclear unit 100 is sure?",
    "rule": "Only विकारान् (disorders, acc. pl.) is sure; the printed त्रिवर्गौमिश्रान् is unclear.",
    "limits": ("Low confidence. त्रिवर्गौमिश्रान् is unclear: 'mixed with the three groups' (possibly the three doṣas) is a "
               "guess, so no question rests on it or on 'mixed'. No verb is printed. The data takes the line as completing "
               "units 98 and 99 (not firm)."),
    "explain_hi": ("यह पंक्ति अस्पष्ट और अधूरी है। पक्का शब्द केवल ‘विकारान्’ है: विकारों को (द्वितीया बहुवचन)। "
                   "छपा ‘त्रिवर्गौमिश्रान्’ ठीक नहीं पढ़ा जाता; ‘त्रिवर्ग-मिश्र’ (तीन वर्गों से मिले हुए, सम्भवतः तीन दोष) केवल अनुमान है। "
                   "कोई क्रिया नहीं छपी। सम्भवतः यह वात, पित्त, कफ के बाद मिश्रित विकारों की बात पूरी करती है, पर यह पक्का नहीं।"),
    "hook": "पक्का केवल ‘विकारान्’: विकारों को।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "Which word of unit 100 is sure, by the card?",
            ("विकारान्, disorders", "Only विकारान् (m. acc. pl.) is a sure word."),
            [("त्रिवर्गौ, a sure dual", "त्रिवर्गौमिश्रान् is unclear in print."),
             ("मिश्रान्, a sure reading", "मिश्र is part of a guess, not firm."),
             ("करोति, its verb", "No verb is printed in this line.")],
            "The line is unclear except for विकारान् (disorders).",
            "विकारान् = disorders (acc. pl.)."),
        mcq("warmup", 1, "What does विकार mean?",
            ("Disorder", "विकार = disorder, change for the worse."),
            [("Remedy, medicine", "A remedy would be औषध or चिकित्सा."),
             ("Season", "A season is ऋतु."),
             ("Seed", "Seed is बीज.")],
            "विकारान् = disorders.",
            "विकार = disorder."),
        T(match(2, "Match each form of विकार to its case and number.",
                [["विकारान्", "accusative plural"], ["विकाराः", "nominative plural"], ["विकारम्", "accusative singular"],
                 ["विकारः", "nominative singular"]],
                "विकारान्, printed in unit 100, is the accusative plural of the अ-stem विकार.",
                "-आन् = acc. pl. (m.); -आः = nom. pl.; -अम् = acc. sg.; -अः = nom. sg.", role="extend"),
          "A masculine अ-stem makes its accusative plural in -आन्: विकारान्."),
        mcq("discriminate", 3, "Which word of unit 100 is unclear in print?",
            ("त्रिवर्गौमिश्रान्", "The data keeps it as printed; any reading of it is a guess."),
            [("विकारान्", "विकारान् is the one sure word."),
             ("करोति", "No verb is printed in this line."),
             ("वातविकारम्", "That word is printed in unit 97, not here.")],
            "Only विकारान् is sure; त्रिवर्गौमिश्रान् is unclear.",
            "Unit 100: unclear word + विकारान्."),
        multi("apply", 4, "Which two are right about unit 100 by the card?",
              [("It is a prose line", "Right: the unit is prose."),
               ("No verb is printed in it", "Right: the line is elliptical."),
               ("त्रिवर्गौमिश्रान् is a firm reading", "It is unclear; any reading is a guess."),
               ("विकारान् is a nominative", "-आन् is accusative plural.")],
              [0, 1],
              "Unit 100: unclear prose, no verb; only विकारान् is sure.",
              "Prose, elliptical; विकारान् = acc. pl."),
        T(mcq("transfer", 5, "By the pattern of विकारान्, what is the accusative plural of an invented रोगः (disease)?",
              ("रोगान्", "m. अ-stem acc. pl. -आन्, like विकारान्."),
              [("रोगाः", "That is the nominative plural."),
               ("रोगम्", "That is the accusative singular."),
               ("रोगेषु", "That is the locative plural.")],
              "विकार → विकारान्; रोग → रोगान्.",
              "m. अ-stem: acc. pl. -आन्."),
          "A masculine अ-stem makes its accusative plural in -आन्: रोगान्, विकारान्."),
    ],
}

# ===================================================================== NOTES_HI
NOTES_HI = {
    "89": ("विश्वास कम; गद्य, एक छपी पंक्ति (02.02.92)। छपा ‘तदापूतप्रजां’ संदिग्ध है: ‘आपूतप्रजाम्’ कोई शब्द नहीं; "
           "‘तदा पूतिप्रजाम्’ सम्भावित सुधार है (इकाई ९४ में ‘पूतिप्रजं’ छपा है), पर ‘बिगड़ी सन्तान वाली’ अर्थ पक्का नहीं। "
           "वाक्य में क्रिया नहीं; ‘जनयति’ इकाई ८८ से समझा गया, जोड़ा नहीं गया। "
           "सन्धियाँ जाँचीं: तस्य + अवयवः → तस्यावयवः (अ + अ → आ); अवयवः + तदा → अवयवस्तदा (विसर्ग + त → स्त)।"),
    "90": ("विश्वास उच्च, कोई पाठ-चिह्न नहीं; गद्य (02.02.93)। तस्याः + जातम् → तस्या जातम्: आः के बाद घोष व्यंजन ज से पहले विसर्ग का लोप, "
           "सामान्य सन्धि। ‘जातं जातम्’ की दोहराई = हर एक जन्मा। ‘म्रियते’ = मरता है (वर्तमान, आत्मनेपद)। "
           "यह सम्भवतः इकाई ८९ का परिणाम है।"),
    "91": ("विश्वास कम; गद्य (02.02.94)। पाठ-चिह्न: छपा ‘स्त्रीकरणां’ शायद ‘स्त्रीकरणानाम्’ हो (‘ना’ छूटा; षष्ठी बहुवचन अपेक्षित; सम्भव पाठ, पक्का नहीं)। "
           "‘स्त्रीकरण’ और ‘अधोगुरुत्व’ के अर्थ शाब्दिक हैं, पक्के नहीं; ‘आदि’ की सूची नहीं दी। वाक्य अधूरा; परिणाम इकाई ९२ में। "
           "सन्धियाँ जाँचीं: सः + अवयवः → सोऽवयवः; अधस् + गुरुत्व → अधोगुरुत्व; निर्वर्तकाः + ये → निर्वर्तका ये; "
           "बीजांशाः + तेषाम् → बीजांशास्तेषाम्; तेषाम् + एकदेशः → तेषामेकदेशः।"),
    "92": ("विश्वास मध्यम; गद्य (02.02.95)। पाठ-चिह्न: ‘रूपाकृतिप्रायाम्’ से यह नहीं पता कि किसका रूप-आकृति; इकाई ९४ के "
           "‘पुरुषाकृतिप्रायम्’ के मेल से ‘स्त्री-’ छूटा होने का अनुमान है, लागू नहीं किया गया। ‘जनयति’ का कर्ता अनकहा। ‘वार्ता’ नाम है। "
           "सन्धियाँ जाँचीं: रूप + आकृति → रूपाकृति; प्रायाम् + अस्त्रियम् → प्रायामस्त्रियम्।"),
    "93": ("विश्वास मध्यम, कोई पाठ-चिह्न नहीं; गद्य (02.02.96)। ‘व्यापद्’ = विनाश, विफलता, दोष; ‘स्त्रीव्यापद्’ पारिभाषिक नाम हो सकता है। "
           "सन्धि जाँची: स्त्रीव्यापदम् + आचक्षते → स्त्रीव्यापदमाचक्षते; ताम् + स्त्री → तां स्त्री (अन्त्य म् का अनुस्वार)।"),
    "94": ("विश्वास कम; गद्य (02.02.97), एक लम्बी पंक्ति, कई शब्द बिना दूरी के छपे। पाठ-चिह्न: छपा ‘शुकरारख्ये’ सम्भवतः ‘शुक्राख्ये’ "
           "(शुक्र नामक) है; ‘र’ का वैसा ही प्रवेश इकाई ८८ के ‘शोणितारख्ये’ में दिखता है। ‘पूतिप्रजम्’ का अर्थ अनुमानित; "
           "‘मृणासुलिंगा’ नाम अस्पष्ट, सम्भवतः बिगड़ा; इसका अनुवाद नहीं किया गया। रस = पोषक रस (सम्भावित); सत्त्व = मन (मानक)। "
           "सन्धियाँ जाँचीं: एवम् + एव → एवमेव; पुंसः + यदा → पुंसो यदा; प्रदुष्यति + इति → प्रदुष्यतीति; इति + आदि → इत्यादि; "
           "योजयेत् + वन्ध्यम् → योजयेद्वन्ध्यम्; इति + एतेन → इत्येतेन; विकृतिः + व्याख्याता → विकृतिर्व्याख्याता।"),
    "95": ("विश्वास कम; गद्य (02.02.98)। पाठ-चिह्न: छपा ‘उत्पत्तिः’ यहाँ अटपटा है; इकाई ९६ के ‘अनुपतापात्’ के आधार पर ‘उपतापः’ "
           "सम्भावित पाठ है, लागू नहीं किया गया। छपाई में ‘यस्य अंगावयवस्य’ बिना सन्धि, पर ‘तस्यांगावयवस्य’ सन्धि सहित है। "
           "सन्धियाँ जाँचीं: अङ्ग + अवयव → अङ्गावयव; तस्य + अङ्गावयवस्य → तस्याङ्गावयवस्य; उत्पत्तिः + भवति → उत्पत्तिर्भवति; "
           "विकृतिः + उपजायते → विकृतिरुपजायते।"),
    "96": ("विश्वास मध्यम; गद्य (02.02.99)। पाठ-चिह्न: छपा ‘अनुपत्तापात्’ का दोहरा त्त छपाई की भूल माना गया: अनुपतापात् (अन् + उपताप)। "
           "कर्ता (इकाई ९५ की विकृति) समझा गया, जोड़ा नहीं गया। "
           "सन्धियाँ जाँचीं: न + उपजायते → नोपजायते (अ + उ → ओ); उपजायते + अनुपतापात् → उपजायतेऽनुपतापात् (ए + अ → एऽ)।"),
    "97": ("विश्वास कम केवल एक शब्द के कारण; गद्य (02.02.100)। पाठ-चिह्न: छपा ‘अनक्षम्’ अस्पष्ट; ‘अनिशम्’ (निरन्तर) श/क्ष की समानता से "
           "केवल अनुमान है। मिन्मिण = नकियापन, अस्पष्ट वाणी (सम्भावित)। ‘-त्व’ पूरे समास पर लगता है। "
           "सन्धियाँ जाँचीं: वातलानि + आसेवते → वातलान्यासेवते (इ + आ → या); तदा + अस्याः → तदाऽस्याः; अस्याः + वायुः → अस्या वायुः; "
           "शरीरम् + अनुसर्पन् → शरीरमनुसर्पन्; गर्भाशये + अवतिष्ठमानः → गर्भाशयेऽवतिष्ठमानः; अवतिष्ठमानः + गर्भस्य → अवतिष्ठमानो गर्भस्य; "
           "हीन + अङ्ग → हीनाङ्ग; …त्वानि + अन्यम् → …त्वान्यन्यम्।"),
    "98": ("विश्वास कम; गद्य (02.02.101)। पाठ-चिह्न: समास का बीच का अंश (छपा ‘श्मश्रुहीनत्वक्छ्रनखे श’) क्षतिग्रस्त है; "
           "‘त्वक्-नख-केश-पैङ्गल्य’ केवल अनुमान है; इस अंश का अनुवाद नहीं किया गया। पक्के केवल खलति (मानक), पलित (मानक) और पैंगल्य-आदीनि। "
           "क्रिया नहीं; इकाई ९७ से समझी गई। सन्धियाँ जाँचीं: पित्तम् + अपि → पित्तमपि; पैङ्गल्य + आदीनि → पैङ्गल्यादीनि।"),
    "99": ("विश्वास कम; गद्य (02.02.102)। पाठ-चिह्न: तीसरा अंश ‘सदंतवा’ कोई शब्द नहीं; ‘किलास-अदन्तत्व’ (दाँत न होना) केवल अनुमान है; "
           "इस अंश का अनुवाद नहीं किया गया। कुष्ठ (मानक; यहाँ त्वचा-रोगों का वर्ग भी हो सकता है), किलास (सम्भावित: विटिलिगो)। "
           "‘श्लेष्मा’ = श्लेष्मन् की प्रथमा एकवचन। क्रिया नहीं छपी।"),
    "100": ("विश्वास कम; गद्य (02.02.103)। पाठ-चिह्न: छपा ‘त्रिवर्गौमिश्रान्’ अस्पष्ट; बीच का ‘औ’ अतिरिक्त लगता है; "
            "‘त्रिवर्ग-मिश्र’ (तीन वर्गों से मिश्रित, सम्भवतः तीन दोष) केवल अनुमान है, कोई पाठ नहीं बनाया गया। "
            "पक्का केवल ‘विकारान्’ (द्वितीया बहुवचन)। मिश्रान् + विकारान्: न् व से पहले नहीं बदलता। क्रिया नहीं छपी।"),
}

# ===================================================================== AIDS
AIDS = {
    "89": {
        "frame": "यदा (जब) तस्य अवयवः … → तदा (तब) … [छपा ‘आपूतप्रजां’ अस्पष्ट] … क्रिया नहीं (‘जनयति’ इकाई ८८ से समझा गया)।",
        "sandhi": "अ + अ → आ: तस्य + अवयवः → तस्यावयवः · विसर्ग + त → स्त: अवयवः + तदा → अवयवस्तदा।",
        "chunks": "यदा | तस्यावयवः | तदा | [आपूतप्रजां: अस्पष्ट]",
    },
    "90": {
        "frame": "तस्याः (उसका) → जातं जातम् (हर एक जन्मा) → म्रियते (मरता है)।",
        "sandhi": "आः + घोष व्यंजन → आ: तस्याः + जातम् → तस्या जातम्।",
        "puns": "मेरी बनाई, केवल सुनने की सहायता: ‘जात-जात’ बोलें तो ‘जो-जो’ याद आए: जो-जो जन्मा।",
    },
    "91": {
        "frame": "यदा पुनः सः अवयवः → (उन) बीजांशों का एकदेश, ये बीजांश निर्वर्तक हैं → (परिणाम इकाई ९२ में)।",
        "sandhi": ("अः + अ → ओऽ: सः + अवयवः → सोऽवयवः · आः + त → आस्त: बीजांशाः + तेषाम् → बीजांशास्तेषाम् · "
                   "आः + य → आ: निर्वर्तकाः + ये → निर्वर्तका ये।"),
        "chunks": "यदा पुनः सोऽवयवः | स्त्रीकरणां च | शरीरसंश्रयाणामधोगुरुत्वादीनां | निर्वर्तका ये बीजांशाः | तेषामेकदेशः",
    },
    "92": {
        "diagram": {"groups": [
            {"label": "तदा", "items": ["रूपाकृतिप्रायाम् (रूप-आकृति की प्रधानता वाली)"]},
            {"label": "पर", "items": ["अस्त्रियम् (स्त्री नहीं)"]},
            {"label": "नाम", "items": ["वार्ता"]},
            {"label": "क्रिया", "items": ["जनयति (कर्ता अनकहा)"]}]},
        "sandhi": "अ + आ → आ: रूप + आकृति → रूपाकृति · म् + स्वर: प्रायाम् + अस्त्रियम् → प्रायामस्त्रियम्।",
        "frame": "इकाई ९१ का ‘यदा’ → यहाँ ‘तदा … जनयति’: वाक्य सम्भवतः पूरा।",
    },
    "93": {
        "frame": "ताम् (उसे, सम्भवतः इकाई ९२ की अस्त्री) → स्त्रीव्यापदम् (स्त्रीव्यापद्) → आचक्षते (वे कहते हैं)।",
        "sandhi": "म् + स्वर: स्त्रीव्यापदम् + आचक्षते → स्त्रीव्यापदमाचक्षते · अन्त्य म् → अनुस्वार: ताम् + स्त्री → तां स्त्री।",
        "puns": "मेरी बनाई, केवल सुनने की सहायता: ‘व्यापद्’ में ‘आपद्’ (विपत्ति) सुनें: स्त्री की विपत्ति, दोष।",
    },
    "94": {
        "frame": "एवमेव पुंसः (पुरुष के लिए वैसे ही) → ‘बीज दूषित होता है’ इत्यादि योजयेत् → वन्ध्य, पूतिप्रज (अर्थ अनुमानित), पुरुषाकृतिप्राय अपुरुष।",
        "diagram": {"groups": [
            {"label": "व्याख्यात (पहले)", "items": ["मातृज अवयव", "पितृज अवयव"]},
            {"label": "इससे व्याख्यात", "items": ["सात्म्यज अवयव", "रसज अवयव", "सत्त्वज अवयव"]}]},
        "sandhi": ("अः + य → ओ य: पुंसः + यदा → पुंसो यदा · इ + इ → ई: प्रदुष्यति + इति → प्रदुष्यतीति · "
                   "इ + ए → ये: इति + एतेन → इत्येतेन · इः + व → इर्व: विकृतिः + व्याख्याता → विकृतिर्व्याख्याता।"),
        "letters": "इससे समझे तीन: सा-र-स (सात्म्यज, रसज, सत्त्वज)।",
    },
    "95": {
        "chain": {"steps": ["जिस अंग-अवयव के", "बीज या बीजांश में", "उत्पत्ति (छपा पाठ)", "उसी-उसी अंग-अवयव की", "विकृति उत्पन्न"]},
        "sandhi": ("अ + अ → आ: अङ्ग + अवयव → अङ्गावयव · इः + उ → इरु: विकृतिः + उपजायते → विकृतिरुपजायते · "
                   "इः + भ → इर्भ: उत्पत्तिः + भवति → उत्पत्तिर्भवति।"),
        "frame": "यस्य … तस्य तस्य: जिसका …, उसी-उसी का।",
    },
    "96": {
        "frame": "(विकृति, इकाई ९५ से) → न उपजायते → कारण: अनुपतापात् (उपताप न होने से)।",
        "sandhi": "अ + उ → ओ: न + उपजायते → नोपजायते · ए + अ → एऽ: उपजायते + अनुपतापात् → उपजायतेऽनुपतापात्।",
        "puns": "मेरी बनाई, केवल सुनने की सहायता: ‘अन्-उपताप’: ताप नहीं, तो विकार नहीं।",
    },
    "97": {
        "chain": {"steps": ["गर्भिणी वातल का सेवन करती", "वायु प्रकुपित", "शरीर में सरकता", "गर्भाशय में ठहरता",
                            "गर्भ में वात-विकार करता"]},
        "diagram": {"groups": [
            {"label": "वात से गर्भ में (छपे क्रम में)",
             "items": ["जड", "बधिर", "मूक", "मिन्मिण (सम्भावित)", "गद्गद", "खंज", "कुब्ज", "वामन", "हीनांग", "अधिकांग"]},
            {"label": "या", "items": ["अन्य वात-विकार"]}]},
        "seesaw": "अंगों की कमी: हीनांग ↔ अंगों की अधिकता: अधिकांग (दोनों इसी सूची में)।",
        "sandhi": ("इ + आ → या: वातलानि + आसेवते → वातलान्यासेवते · ए + अ → एऽ: गर्भाशये + अवतिष्ठमानः → गर्भाशयेऽवतिष्ठमानः · "
                   "अः + ग → ओ ग: अवतिष्ठमानः + गर्भस्य → अवतिष्ठमानो गर्भस्य।"),
        "letters": "सूची के आदि-अक्षर, छपे क्रम में: ज-ब-मू-मि-ग-खं-कु-वा-ही-अ।",
    },
    "98": {
        "diagram": {"groups": [
            {"label": "पित्त भी, वायु की तरह", "items": ["खलति (गंजापन)", "पलित (सफ़ेद बाल)", "[टूटा अंश]", "पैंगल्य आदि"]}]},
        "sandhi": "म् + स्वर: पित्तम् + अपि → पित्तमपि · अ + आ → आ: पैङ्गल्य + आदीनि → पैङ्गल्यादीनि।",
        "frame": "तथा (वैसे ही) → वायुवत् (वायु की तरह) → पित्तम् अपि (पित्त भी) → (करता है, इकाई ९७ से)।",
    },
    "99": {
        "frame": "श्लेष्मा तु (कफ तो) → कुष्ठ, किलास, [अस्पष्ट] आदि → (करता है, पिछली इकाइयों से)।",
        "anchors": "मेरी याद-पद्धति: वात (९७) → पित्त (९८) → कफ (९९): तीनों दोष क्रम से।",
        "chunks": "श्लेष्मा तु | कुष्ठ | किलास | [सदंतवा: अस्पष्ट] | आदीनि",
    },
    "100": {
        "frame": "पक्का केवल: विकारान् (विकारों को, द्वितीया बहुवचन) · छपा ‘त्रिवर्गौमिश्रान्’ अस्पष्ट · क्रिया नहीं।",
        "chunks": "[त्रिवर्गौमिश्रान्: अस्पष्ट] | विकारान्",
        "anchors": "मेरी याद-पद्धति: -आन् = ‘अनेक को’ (पुंल्लिंग द्वितीया बहुवचन): विकारान्, रोगान्।",
    },
}

# ===================================================================== IMAGE_SPECS
IMAGE_SPECS = {
    ("92", "diagram"): {
        "file": "sh2-varta-92.svg",
        "alt": ("Table of unit 92 in printed order: rupakritiprayam, mostly of form and shape; astriyam, a non-woman; "
                "vartam nama, named varta; janayati, (it) produces, subject unstated."),
        "type": "table",
        "title": "इकाई ९२: छपे क्रम में",
        "heads": ["छपा शब्द", "अर्थ"],
        "rows": [["रूपाकृतिप्रायाम्", "रूप-आकृति की प्रधानता वाली"], ["अस्त्रियम्", "अस्त्री, स्त्री नहीं"],
                 ["वार्तां नाम", "वार्ता नाम की"], ["जनयति", "उत्पन्न करता है (कर्ता अनकहा)"]],
    },
    ("94", "diagram"): {
        "file": "sh2-vikriti-vyakhya-94.svg",
        "alt": ("Flowchart of unit 94: the explanation of the deformity of mother-born and father-born parts also "
                "explains the deformity of the parts born of satmya, of rasa and of sattva (three nodes)."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"मातृज, पितृज अवयव\"] --> B[\"विकृति का व्याख्यान\"]\n"
                 "  B -->|\"इससे भी\"| C[\"सात्म्यज<br/>अवयव-विकृति\"]\n"
                 "  B -->|\"इससे भी\"| D[\"रसज<br/>अवयव-विकृति\"]\n"
                 "  B -->|\"इससे भी\"| E[\"सत्त्वज<br/>अवयव-विकृति\"]\n"),
    },
    ("95", "chain"): {
        "file": "sh2-anga-vikriti-95.svg",
        "alt": ("Chain of unit 95 in printed order: of whichever limb-part; in its seed or seed-portion; an origin occurs "
                "(printed reading); of that very limb-part; a deformity arises."),
        "type": "chain",
        "title": "इकाई ९५: जिसका …, उसी का",
        "steps": ["जिस अंग-अवयव के", "बीज या बीजांश में", "उत्पत्ति (छपा पाठ)", "उसी-उसी अंग-अवयव की", "विकृति उत्पन्न"],
    },
    ("97", "chain"): {
        "file": "sh2-vata-garbha-97.svg",
        "alt": ("Flowchart of unit 97 in five steps: the pregnant woman resorts to Vata-increasing things; Vayu is "
                "provoked; it moves along the body; it lodges in the uterus; it produces Vata disorders in the embryo."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"गर्भिणी वातल का सेवन करती\"] --> B[\"वायु प्रकुपित\"]\n"
                 "  B --> C[\"शरीर में सरकता\"]\n"
                 "  C --> D[\"गर्भाशय में ठहरता\"]\n"
                 "  D --> E[\"गर्भ में वात-विकार\"]\n"),
    },
    ("97", "diagram"): {
        "file": "sh2-vata-vikara-suchi-97.svg",
        "alt": ("Numbered table of unit 97's list in printed order, ten items: dull, deaf, mute, nasal-voiced (probable), "
                "stammering, lame, hunchbacked, dwarfish, deficient limbs, excessive limbs; or another Vata disorder."),
        "type": "table",
        "title": "वात से गर्भ में (छपे क्रम में)",
        "heads": ["छपा शब्द", "अर्थ"],
        "rows": [["१. जड", "जड़ता"], ["२. बधिर", "बहरापन"], ["३. मूक", "गूँगापन"], ["४. मिन्मिण", "नकियापन (सम्भावित)"],
                 ["५. गद्गद", "हकलापन"], ["६. खंज", "लंगड़ापन"], ["७. कुब्ज", "कुबड़ापन"], ["८. वामन", "बौनापन"],
                 ["९. हीनांग", "अंगों की कमी"], ["१०. अधिकांग", "अंगों की अधिकता"], ["या", "अन्य वात-विकार"]],
    },
    ("98", "diagram"): {
        "file": "sh2-pitta-98.svg",
        "alt": ("Table of unit 98 in printed order: Pitta, like Vayu: khalati, baldness (standard); palita, grey hair "
                "(standard); a damaged middle, untranslated; paingalya and so on, tawniness."),
        "type": "table",
        "title": "पित्त भी, वायु की तरह (इकाई ९८)",
        "heads": ["छपा अंश", "अर्थ"],
        "rows": [["खलति", "गंजापन (मानक)"], ["पलित", "बालों का सफ़ेद होना (मानक)"], ["बीच का अंश", "क्षतिग्रस्त, अनुवाद नहीं"],
                 ["पैंगल्य आदि", "पीलापन लिए भूरापन आदि"]],
    },
}
