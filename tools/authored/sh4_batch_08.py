from helpers import mcq, match, order, fill, multi, accepts


AUTHORED = {}

# ---------------------------------------------------------------- unit 95
AUTHORED["95"] = {
    "title": "दृष्टकर्मणा शल्यहर्त्रा ... कष्टतममस्ति शस्त्रकर्म",
    "question": "By unit 95, what do some say about extracting the śalya, and what is in truth the most difficult?",
    "rule": ("Some (एके) say: the extraction of the śalya is by a śalya-remover (शल्यहर्तृ) whose work has been seen "
             "(दृष्टकर्मन्, experienced). In truth (तत्त्वतः), śastrakarma, work with the cutting instrument, is the most "
             "difficult (कष्टतम)."),
    "limits": ("Two printed prose lines. The śalya as the fetus is read from context (unit 89), not stated here; "
               "śalyahartṛ as a surgeon is probable. कष्टतम may mean 'most painful'. Which 'some say' opinion (units 94-95) "
               "the text holds is not said: no question on it."),
    "explain_hi": ("इस इकाई में दो छपी गद्य-पंक्तियाँ हैं। "
                   "पहली में एक मत है: कुछ लोग (एके) कहते हैं कि शल्य का आहरण यानी निकालना ऐसे शल्यहर्ता से हो जिसका कर्म देखा जा "
                   "चुका हो (दृष्टकर्मा, यानी अनुभवी)। "
                   "दूसरी पंक्ति कहती है: वास्तव में (तत्त्वतः) शस्त्रकर्म यानी शस्त्र से किया जाने वाला कर्म सबसे कठिन (कष्टतम) है। "
                   "यहाँ शल्य गर्भ है, यह डेटा संदर्भ (इकाई ८९ का गर्भशल्य) से पढ़ता है; इस पंक्ति में नहीं कहा। "
                   "‘कष्टतम’ का अर्थ ‘सबसे पीड़ादायक’ भी हो सकता है; ‘-तम’ अतिशय (सबसे अधिक) बताता है।"),
    "hook": "एक मत: अनुभवी शल्यहर्ता निकाले; तत्त्वतः: शस्त्रकर्म सबसे कठिन।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 95, what is in truth the most difficult?",
            ("Śastrakarma, work with the knife", "तत्त्वतः कष्टतममस्ति शस्त्रकर्म: in truth śastrakarma is the most difficult."),
            [("Anointing the hand with ghee", "Anointing comes in unit 100 and is never called the most difficult."),
             ("Comforting the frightened woman", "Comforting the woman comes in unit 106; it is not called most difficult."),
             ("Laying the woman on a soft bed", "No bed is named in unit 95; the most difficult thing is śastrakarma.")],
            "In truth, work with the cutting instrument (śastrakarma) is the most difficult.",
            "तत्त्वतः कष्टतमम् अस्ति शस्त्रकर्म."),
        order(1, "Put these words of unit 95 in the order of the two printed lines.",
              ["दृष्टकर्मणा", "शल्यहर्त्रा", "शल्याहरणमित्येके", "तत्त्वतः", "कष्टतममस्ति", "शस्त्रकर्म"],
              "By one whose work has been seen, by a śalya-remover, the extraction of the śalya, some say; in truth the most "
              "difficult is śastrakarma.",
              "दृष्टकर्मणा → शल्यहर्त्रा → शल्याहरणमित्येके → तत्त्वतः → कष्टतममस्ति → शस्त्रकर्म."),
        match(2, "Match each word of unit 95 to its meaning.",
              [["दृष्टकर्मन्", "one whose work has been seen"], ["शल्यहर्तृ", "remover of the śalya"],
               ["आहरण", "extraction"], ["तत्त्वतः", "in truth"], ["कष्टतम", "most difficult"]],
              "An experienced remover extracts the śalya, some say; in truth śastrakarma is the most difficult.",
              "दृष्टकर्मन्, शल्यहर्तृ, आहरण, तत्त्वतः, कष्टतम.", role="extend",
              teaches="The suffix -तम makes a superlative: कष्ट (difficult) → कष्टतम (most difficult)."),
        mcq("discriminate", 3, "Which split of शल्याहरणमित्येके is right?",
            ("शल्य + आहरणम् + इति + एके", "अ + आ → आ; म् joins the vowel; इ + ए → ये."),
            [("शल्ये + आहरणम् + इति + एके", "ए + आ would give शल्ययाहरणम् or शल्य आहरणम्, not शल्याहरणम्."),
             ("शल्य + आहरणम् + इति + ऐके", "इ + ऐ would give इत्यैके, with ऐ, not इत्येके."),
             ("शल्य + आहरणम् + इत्य + एके", "इत्य is not a word; the particle is इति (thus).")],
            "शल्य (śalya) + आहरणम् (extraction) + इति (thus) + एके (some): अ + आ → आ, इ + ए → ये.",
            "अ + आ → आ; इ + a different vowel → य् + that vowel."),
        multi("apply", 4, "Which statements about unit 95 are right by the card?",
              [("The remover in the opinion is a beginner", "दृष्टकर्मन् = one whose work has been seen: experienced."),
               ("The line itself names the śalya as the fetus", "The data reads the fetus from context (unit 89); this line does not say it."),
               ("Śastrakarma is called the most difficult", "Right: कष्टतममस्ति शस्त्रकर्म."),
               ("Some hold that an experienced remover extracts the śalya", "Right: दृष्टकर्मणा शल्यहर्त्रा शल्याहरणमित्येके.")],
              [2, 3],
              "Some say an experienced remover extracts the śalya; in truth śastrakarma is the most difficult.",
              "एके: दृष्टकर्मा शल्यहर्ता; तत्त्वतः: शस्त्रकर्म कष्टतमम्."),
        mcq("transfer", 5, "By the suffix of कष्टतम, what does a new example, प्रियतम, mean?",
            ("Most dear, dearest", "-तम makes a superlative, as कष्ट → कष्टतम (most difficult)."),
            [("Dearer than another", "A comparative is made with -तर (प्रियतर), not -तम."),
             ("Dearness, being dear", "An abstract noun is made with -त्व or -ता (प्रियत्व), not -तम."),
             ("Of the dear one's own", "That would be a genitive (प्रियस्य), not a -तम form.")],
            "प्रिय + तम = प्रियतम, most dear, like कष्ट + तम = कष्टतम, most difficult.",
            "-तम → superlative (most).",
            teaches="The suffix -तम makes a superlative: कष्ट → कष्टतम (most difficult)."),
    ],
}

# ---------------------------------------------------------------- unit 96
AUTHORED["96"] = {
    "title": "यतो योनियकृत्प्लीहान्त्रगर्भाशयादीनां मध्ये",
    "question": "By unit 96, why is the instrument work so hard, and what is done with one hand?",
    "rule": ("Since (यतः) the work lies among the yoni, liver (यकृत्), spleen (प्लीहा), intestines (अन्त्र), womb (गर्भाशय) "
             "and the like, by one who does not injure them (अनुपहिंसता) and does not let (it) touch them; and eight operations, "
             "pulling up to straightening, are to be done with one hand (एकेन पाणिना)."),
    "limits": ("Low confidence. Printed अवधार्यम् may be a misprint of अवचार्यम् (to be applied): no question on that verb. "
               "The object of अस्पर्शयता is not stated; the instrument is a reading. This clause appears to give the reason "
               "for unit 95. Prose."),
    "explain_hi": ("यह कठिन गद्य-पंक्ति कारण देती है (यतः = क्योंकि); डेटा के अनुसार यह सम्भवतः इकाई ९५ के ‘सबसे कठिन’ का कारण है। "
                   "काम योनि, यकृत्, प्लीहा, आँतों (अन्त्र), गर्भाशय आदि के बीच (मध्ये) होता है; करने वाला उन्हें चोट न पहुँचाए "
                   "(अनुपहिंसता) और न छूने दे (अस्पर्शयता; किसे, यह नहीं कहा)। "
                   "छपा ‘अवधार्यम्’ (निश्चित किया जाए) सम्भवतः ‘अवचार्यम्’ (प्रयोग किया जाए) की छपाई-भूल है; इस पर प्रश्न नहीं। "
                   "फिर आठ क्रियाएँ एक हाथ से (एकेन पाणिना) करनी हैं: ऊपर खींचना, नीचे खींचना, घुमाना, काटकर निकालना, काटना, "
                   "चीरना, दबाना और सीधा करना।"),
    "hook": "अंगों के बीच, बिना चोट, एक हाथ से आठ क्रियाएँ।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 96, with what are the listed operations to be done?",
            ("With one hand", "एकेन पाणिना कार्याणि: to be done with one hand."),
            [("With both hands at once", "The unit says one hand: एकेन पाणिना."),
             ("With a cloth round the hand", "No cloth is named in unit 96."),
             ("With a helper's two hands", "No helper's hands are named; the unit says one hand.")],
            "The operations are to be done with one hand.",
            "एकेन पाणिना कार्याणि."),
        order(1, "Put the organs of unit 96 in the line's order.",
              ["योनि", "यकृत्", "प्लीहा", "अन्त्र", "गर्भाशय"],
              "Among the yoni, liver, spleen, intestines, womb and the like.",
              "योनि → यकृत् → प्लीहा → अन्त्र → गर्भाशय (आदि)."),
        match(2, "Match each operation of unit 96 to its meaning.",
              [["उत्कर्षण", "pulling up"], ["अपकर्षण", "pulling down"], ["व्यावर्तन", "turning round"],
               ["छेदन", "cutting through"], ["पीडन", "pressing"], ["ऋजूकरण", "straightening"]],
              "Six of the eight operations to be done with one hand.",
              "उत्कर्षण, अपकर्षण, व्यावर्तन, छेदन, पीडन, ऋजूकरण.", role="extend",
              teaches="उत्- means up and अप- down or away: उत्कर्षण = pulling up, अपकर्षण = pulling down."),
        mcq("discriminate", 3, "Which split of पीडनर्जूकरणानि is right?",
            ("पीडन + ऋजूकरणानि", "अ + ऋ → अर्: पीडन + ऋजू... → पीडनर्जू..."),
            [("पीडने + ऋजूकरणानि", "ए + ऋ would not give अर्; ए before a vowel becomes अय् or अ."),
             ("पीडनम् + ऋजूकरणानि", "म् before a vowel joins it: पीडनमृजू..., with no र्."),
             ("पीडनर्ज + ऊकरणानि", "Neither पीडनर्ज nor ऊकरणानि is a word here.")],
            "पीडन (pressing) + ऋजूकरणानि (straightenings): अ + ऋ → अर्.",
            "अ + ऋ → अर्."),
        multi("apply", 4, "Which of these are among the operations listed in unit 96?",
              [("Burning with fire", "Burning is not in the list of unit 96."),
               ("Pressing", "Right: पीडन."),
               ("Stitching the wound", "Stitching is not in the list of unit 96."),
               ("Straightening", "Right: ऋजूकरण."),
               ("Turning round", "Right: व्यावर्तन.")],
              [1, 3, 4],
              "Pressing, straightening and turning round are in the list; burning and stitching are not.",
              "उत्कर्षण, अपकर्षण, व्यावर्तन, उत्कर्तन, छेदन, भेदन, पीडन, ऋजूकरण."),
        mcq("transfer", 5, "By the rule of पीडन + ऋजूकरणानि, how is देव + ऋषिः (a divine seer) joined?",
            ("देवर्षिः", "अ + ऋ → अर्, as पीडन + ऋजू... → पीडनर्जू..."),
            [("देवार्षिः", "अ + ऋ gives a short अर्, not a long आर्."),
             ("देवेर्षिः", "ए comes from अ + इ, not from अ + ऋ."),
             ("देवोर्षिः", "ओ comes from अ + उ, not from अ + ऋ.")],
            "देव + ऋषिः = देवर्षिः, like पीडन + ऋजूकरणानि = पीडनर्जूकरणानि.",
            "अ + ऋ → अर्.",
            teaches="A short अ followed by ऋ joins as अर्: पीडन + ऋजूकरणानि → पीडनर्जूकरणानि."),
    ],
}

# ---------------------------------------------------------------- unit 97
AUTHORED["97"] = {
    "title": "तस्मादीश्वरमापृच्छ्य परं च यत्नमास्थाय",
    "question": "By unit 97, what three things go with undertaking it?",
    "rule": ("Therefore (तस्मात्): having consulted the īśvara (ईश्वर, lord, master), having resorted to supreme effort "
             "(परं यत्नम् आस्थाय), accompanied by those who know it (तद्विद्यसहितः), one should undertake it (तम् उपक्रमेत्)."),
    "limits": ("Who the īśvara is is not defined (the data: probably a ruler or head of the household, not the divine), and what "
               "तम् refers to (the case or the fetus) is not named: no question rests on either. परम् is taken with यत्नम्. "
               "A prose line."),
    "explain_hi": ("यह गद्य-पंक्ति पिछली बात का निष्कर्ष है: इसलिए (तस्मात्)। "
                   "ईश्वर यानी स्वामी से पूछकर (आपृच्छ्य), परम प्रयत्न का सहारा लेकर (परं यत्नम् आस्थाय), और उसे जानने वालों के "
                   "साथ (तद्विद्यसहितः) उसका उपक्रम करे (तमुपक्रमेत्)। "
                   "ईश्वर कौन है, पाठ परिभाषित नहीं करता; डेटा उसे सम्भवतः राजा या घर का मुखिया मानता है, ईश्वर-देव नहीं। "
                   "‘तम्’ किसे कहता है (रोगी-दशा या गर्भ), नहीं बताया। "
                   "‘आपृच्छ्य’ और ‘आस्थाय’ उपसर्ग वाले ल्यबन्त हैं: ‘-य’ = करके।"),
    "hook": "पूछो, पूरा यत्न करो, जानकारों के साथ करो।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 97, whom should one consult before undertaking it?",
            ("The īśvara, the lord", "ईश्वरमापृच्छ्य: having consulted the īśvara (lord, master)."),
            [("The woman's own mother", "No mother of the woman is named in unit 97."),
             ("No one; one acts alone", "The unit says to consult the īśvara and to act with experts."),
             ("A court astrologer", "No astrologer is named in unit 97.")],
            "One should first consult the īśvara, the lord or master.",
            "ईश्वरम् आपृच्छ्य."),
        order(1, "Put these phrases of unit 97 in the line's order.",
              ["तस्मात्", "ईश्वरमापृच्छ्य", "परं च यत्नमास्थाय", "तद्विद्यसहितः", "तमुपक्रमेत्"],
              "Therefore, having consulted the lord, and having resorted to supreme effort, accompanied by those who know it, "
              "one should undertake it.",
              "तस्मात् → ईश्वरमापृच्छ्य → परं च यत्नमास्थाय → तद्विद्यसहितः → तमुपक्रमेत्."),
        match(2, "Match each word of unit 97 to its meaning.",
              [["तस्मात्", "therefore"], ["आपृच्छ्य", "having consulted"], ["यत्न", "effort"],
               ["आस्थाय", "having resorted to"], ["उपक्रमेत्", "should undertake"]],
              "Therefore: consult, resort to great effort, and undertake it with experts.",
              "तस्मात्, आपृच्छ्य, यत्न, आस्थाय, उपक्रमेत्.", role="extend",
              teaches="With a prefix, the absolutive ends in -य: आ-√प्रच्छ् → आपृच्छ्य (having consulted)."),
        mcq("discriminate", 3, "Which split of तस्मादीश्वरम् is right?",
            ("तस्मात् + ईश्वरम्", "A final त् before a vowel becomes द्: तस्मात् + ईश्वरम् → तस्मादीश्वरम्."),
            [("तस्मात् + ऐश्वरम्", "त् + ऐ would give तस्मादैश्वरम्, with ऐ, not ई."),
             ("तस्मा + दीश्वरम्", "Neither तस्मा nor दीश्वरम् is the word here."),
             ("तस्मात् + इश्वरम्", "A short इ would give तस्मादिश्वरम्; the word is ईश्वर, with long ई.")],
            "तस्मात् (therefore) + ईश्वरम् (the lord): त् + vowel → द्.",
            "त् + vowel → द्."),
        mcq("apply", 4, "A physician faces such a case. By unit 97, how should it be undertaken?",
            ("After consulting the lord, with effort and experts", "ईश्वरमापृच्छ्य, परं यत्नमास्थाय, तद्विद्यसहितः."),
            [("Alone and quickly, without telling anyone at all", "The unit says to consult and to work with those who know it."),
             ("Only after waiting three days to watch the woman", "No waiting and no number of days is named in unit 97."),
             ("By the woman herself, with the physician's words", "The undertaker is the physician with experts, not the woman.")],
            "Consult the lord, resort to supreme effort, and undertake it with those who know it.",
            "आपृच्छ्य, आस्थाय, सहितः, उपक्रमेत्."),
        mcq("transfer", 5, "By the form आपृच्छ्य (आ + √प्रच्छ्), what does a new example, आदाय (आ + √दा), mean?",
            ("Having taken", "With a prefix the absolutive ends in -य: आ + √दा → आदाय, having taken."),
            [("He takes", "That would be a present verb (आदत्ते), not a -य form."),
             ("To take", "That would be an infinitive in -तुम् (आदातुम्)."),
             ("Taking, while taking", "That would be a present participle (आददान), not a -य form.")],
            "आदाय = having taken, like आपृच्छ्य = having consulted: prefix + root + -य.",
            "Prefix + root + -य → absolutive (having done).",
            teaches="With a prefix, the absolutive takes -य, not -त्वा: आ-√प्रच्छ् → आपृच्छ्य, आ-√स्था → आस्थाय."),
    ],
}

# ---------------------------------------------------------------- unit 98
AUTHORED["98"] = {
    "title": "अक्रियायां ध्रुवं मरणं",
    "question": "By unit 98, what follows if nothing is done?",
    "rule": ("In inaction (अक्रियायाम्, if no action is taken), death (मरणम्) is certain (ध्रुवम्)."),
    "limits": ("The copula is understood, and who would die (the mother or the woman) is not stated: the card names no one. "
               "The data says unit 99 appears to continue this line. A prose line."),
    "explain_hi": ("यह छोटी गद्य-पंक्ति चेतावनी है: कर्म न करने पर (अक्रियायाम्) मृत्यु (मरणम्) निश्चित (ध्रुवम्) है। "
                   "‘अक्रिया’ में ‘अ-’ निषेध है: क्रिया = कर्म, अक्रिया = कर्म का न होना। "
                   "‘अक्रियायाम्’ स्त्रीलिंग सप्तमी एकवचन है: ‘अक्रिया में’, यानी कर्म न करने की दशा में। "
                   "किसकी मृत्यु, यह नहीं कहा गया (माता या स्त्री); क्रिया ‘है’ समझी जाती है।"),
    "hook": "कुछ न करो, तो मृत्यु पक्की।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 98, what follows if no action is taken?",
            ("Death is certain", "अक्रियायां ध्रुवं मरणम्: in inaction, death is certain."),
            [("Recovery in time", "The unit says the opposite: death is certain."),
             ("A slow, long illness", "No illness is named; the unit says death."),
             ("The fetus comes out alone", "No such outcome is named in unit 98.")],
            "In inaction, death is certain.",
            "अक्रियायाम् ध्रुवम् मरणम्."),
        order(1, "Put the words of unit 98 in the line's order.",
              ["अक्रियायाम्", "ध्रुवम्", "मरणम्"],
              "In inaction, certain, death.",
              "अक्रियायाम् → ध्रुवम् → मरणम्."),
        match(2, "Match each word of unit 98 to its meaning.",
              [["अक्रिया", "inaction, no action taken"], ["ध्रुव", "certain"], ["मरण", "death"]],
              "In inaction, death is certain.",
              "अक्रिया, ध्रुव, मरण.", role="extend",
              teaches="अ- before a word negates it: क्रिया (action) → अक्रिया (inaction)."),
        mcq("discriminate", 3, "What form is अक्रियायाम्, and what does it mean here?",
            ("Locative singular: in inaction", "A feminine आ-stem makes its locative singular in -आयाम्."),
            [("Accusative singular: inaction as object", "The accusative singular would be अक्रियाम्."),
             ("Genitive plural: of the inactions", "The genitive plural would be अक्रियाणाम्."),
             ("Instrumental singular: by inaction", "The instrumental singular would be अक्रियया.")],
            "अक्रियायाम् = in inaction, i.e. if nothing is done: locative singular of अक्रिया.",
            "आ-stem feminine: locative singular -आयाम्."),
        mcq("apply", 4, "By the card, who is it that would certainly die?",
            ("No one is named in the line", "The data: the subject (the mother or the woman) is not stated."),
            [("The mother, named as जननी", "जननी does not occur in unit 98."),
             ("The fetus, named as गर्भ", "गर्भ does not occur in unit 98."),
             ("The physician, named as वैद्य", "वैद्य does not occur in unit 98.")],
            "The line names no one; it says only that in inaction death is certain.",
            "अक्रियायां ध्रुवं मरणम्: कर्ता नहीं दिया."),
        mcq("transfer", 5, "By the अ- of अक्रिया, what does a new example, अज्ञान, mean?",
            ("Not knowing, ignorance", "अ- negates: ज्ञान (knowledge) → अज्ञान (not knowing)."),
            [("Great and deep knowledge", "Greatness would need a word such as महा-, not अ-."),
             ("Knowledge of one's self", "That would need a word such as आत्म-, not अ-."),
             ("Knowing again, recalling", "Again would need a word such as पुनः, not अ-.")],
            "अ + ज्ञान = अज्ञान, not knowing, like अ + क्रिया = अक्रिया, inaction.",
            "अ- + noun → its negation.",
            teaches="अ- before a consonant negates the word: क्रिया → अक्रिया."),
    ],
}

# ---------------------------------------------------------------- unit 99
AUTHORED["99"] = {
    "title": "तथोदरअश्मरीप्रभृतीनापि",
    "question": "By unit 99, which diseases are named, and what is said of them?",
    "rule": ("Likewise (तथा) also (अपि) of udara (उदर, a belly disease, probably ascites-type: probable), aśmarī (अश्मरी, "
             "urinary stone: standard) and so on (प्रभृति). No verb is printed."),
    "limits": ("What is said of them (that surgery is needed, or that death follows inaction) is not stated and not supplied: no "
               "question rests on it. Printed प्रभृतीनापि has lost the म् of प्रभृतीनाम् (a flagged, possible reading). The data "
               "says this line appears to continue unit 98. A prose line."),
    "explain_hi": ("यह अधूरी गद्य-पंक्ति है: वैसे ही (तथा) उदर, अश्मरी आदि (प्रभृति) का भी (अपि)। "
                   "उदर यहाँ रोग है: पेट का रोग, सम्भवतः जलोदर जैसा (सम्भावित); अश्मरी = पथरी, मूत्र की (मानक)। "
                   "क्रिया नहीं है; इनके बारे में क्या कहा गया (शस्त्रकर्म चाहिए, या कर्म न करने पर मृत्यु), पाठ नहीं बताता। "
                   "डेटा के अनुसार यह पंक्ति सम्भवतः इकाई ९८ को आगे बढ़ाती है। "
                   "छपे ‘प्रभृतीनापि’ में ‘प्रभृतीनाम्’ का म् छूटा लगता है।"),
    "hook": "वैसे ही उदर और अश्मरी भी: बात अधूरी।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 99, which two diseases are named?",
            ("Udara and aśmarī", "तथोदरअश्मरीप्रभृतीनाम् अपि: udara, aśmarī and so on."),
            [("Kāsa and śvāsa", "Cough and breathlessness are Kapha signs of unit 47."),
             ("Jvara and atisāra", "Neither fever nor diarrhoea is named in unit 99."),
             ("Raktapitta and mūrcchā", "Raktapitta is unit 21; mūrcchā is a sign in unit 46.")],
            "The line names udara and aśmarī, and so on.",
            "उदर, अश्मरी, प्रभृति."),
        order(1, "Put the parts of unit 99 in the line's order.",
              ["तथा", "उदर", "अश्मरी", "प्रभृतीना(म्)", "अपि"],
              "Likewise, udara, aśmarī and so on, also.",
              "तथा → उदर → अश्मरी → प्रभृतीना(म्) → अपि."),
        match(2, "Match each word of unit 99 to its meaning.",
              [["तथा", "likewise"], ["उदर", "a belly disease, probably ascites-type"], ["अश्मरी", "urinary stone"],
               ["प्रभृति", "and so on, beginning with"], ["अपि", "also"]],
              "Likewise also of udara, aśmarī and so on.",
              "तथा, उदर, अश्मरी, प्रभृति, अपि.", role="extend",
              teaches="प्रभृति at the end of a compound means 'beginning with, and so on': उदर-अश्मरी-प्रभृति."),
        mcq("discriminate", 3, "Which split of तथोदर is right?",
            ("तथा + उदर", "आ + उ → ओ: तथा + उदर → तथोदर."),
            [("तथा + ओदर", "आ + ओ would give औ: तथौदर."),
             ("तथे + उदर", "ए + उ would not give ओ; ए before a vowel becomes अय् or अ."),
             ("तथो + दर", "Neither तथो nor दर is the word here; the words are तथा and उदर.")],
            "तथा (likewise) + उदर (belly disease): आ + उ → ओ.",
            "आ + उ → ओ."),
        multi("apply", 4, "Which statements about unit 99 are right by the card?",
              [("The line has no verb", "Right: the data calls it elliptical, with no verb."),
               ("The line says surgery is needed for these", "What is said of them is not stated and not supplied."),
               ("Udara here is taken as a disease, probably ascites-type", "Right: the data labels this probable."),
               ("Aśmarī is a urinary stone", "Right: the data labels this standard."),
               ("The line names the mother", "No mother is named in unit 99.")],
              [0, 2, 3],
              "No verb; udara is a belly disease (probably ascites-type) and aśmarī a urinary stone; nothing more is said.",
              "तथा उदर-अश्मरी-प्रभृतीनाम् अपि: क्रिया नहीं."),
        mcq("transfer", 5, "By the rule of तथा + उदर, how is महा + उत्सवः (a great festival) joined?",
            ("महोत्सवः", "आ + उ → ओ, as तथा + उदर → तथोदर."),
            [("महौत्सवः", "औ comes from आ + ओ or आ + औ, not from आ + उ."),
             ("महुत्सवः", "The आ does not simply vanish before उ."),
             ("महात्सवः", "The उ is not lost; आ + उ merge into ओ.")],
            "महा + उत्सवः = महोत्सवः, like तथा + उदर = तथोदर.",
            "आ + उ → ओ.",
            teaches="A long आ followed by उ joins as ओ: तथा + उदर → तथोदर."),
    ],
}

# ---------------------------------------------------------------- unit 100
AUTHORED["100"] = {
    "title": "अथोत्तानाया व्याभुग्नसक्थ्या ... गर्भमाहरेत्",
    "question": "By unit 100, how is the woman placed, what is anointed, and what is then done?",
    "rule": ("Then (अथ): for her who lies face up (उत्ताना), thighs bent (व्याभुग्नसक्थी), hip region raised by a cloth cumbhala "
             "(probably a pad), having anointed the hand and the yoni with dhanvanāgamṛttikā (unclear), śālmalī-picchā and "
             "ghee (घृत), one should extract the fetus (गर्भम् आहरेत्)."),
    "limits": ("Low confidence. धन्वनागमृत्तिका is unclear and kept unsplit: no question on it. Śālmalī = silk-cotton tree, Bombax "
               "ceiba (standard); picchā = its gum (probable); cumbhala = a pad (probable). The genitives ('for her who...') "
               "stand loosely. A prose line."),
    "explain_hi": ("यह गद्य-पंक्ति गर्भ निकालने की विधि देती है। "
                   "स्त्री उत्तान यानी चित लेटी हो, उसकी जाँघें मुड़ी हों (व्याभुग्नसक्थी), और कटि-प्रदेश वस्त्र के चुम्भल "
                   "(सम्भवतः गद्दी) से उठाया गया हो। "
                   "फिर धन्वनागमृत्तिका (अर्थ अस्पष्ट), शाल्मली-पिच्छा (सेमल, Bombax ceiba, मानक; पिच्छा = उसका गोंद, सम्भावित) "
                   "और घी से हाथ और योनि को चुपड़कर (अभ्यज्य) गर्भ को निकाले (आहरेत्)। "
                   "‘उत्तानायाः’ आदि षष्ठी रूप ढीले ‘उसके विषय में’ अर्थ में हैं।"),
    "hook": "चित लिटाओ, जाँघें मोड़ो, कटि उठाओ, हाथ चुपड़ो, फिर निकालो।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 100, how does the woman lie?",
            ("Face up, with the thighs bent", "उत्तानायाः व्याभुग्नसक्थ्याः: lying face up, thighs bent."),
            [("Face down, with the legs straight", "उत्ताना means lying face up, and the thighs are bent."),
             ("On her left side, knees drawn up", "No side-lying is named in unit 100."),
             ("Sitting up, leaning on the wall", "She lies face up (उत्ताना); no sitting is named.")],
            "She lies face up, with the thighs bent and the hip region raised.",
            "उत्ताना, व्याभुग्नसक्थी, उन्नमितकटिप्रदेशा."),
        order(1, "Put these phrases of unit 100 in the line's order.",
              ["अथोत्तानाया", "व्याभुग्नसक्थ्या", "वस्त्रचुंभलोन्नमितकटिप्रदेशायाश्च", "...घृतैरभ्यज्य",
               "हस्तं योनिं च", "गर्भमाहरेत्"],
              "Then, for her lying face up, thighs bent, hip region raised by a cloth pad, having anointed with ... ghee the "
              "hand and the yoni, one should extract the fetus.",
              "अथोत्तानाया → व्याभुग्नसक्थ्या → वस्त्रचुंभलोन्नमितकटिप्रदेशायाश्च → ...घृतैरभ्यज्य → हस्तं योनिं च → "
              "गर्भमाहरेत्."),
        match(2, "Match each word of unit 100 to its meaning.",
              [["उत्ताना", "lying face up"], ["व्याभुग्न", "bent"], ["सक्थि", "thigh"], ["कटि", "hip, waist"],
               ["अभ्यज्य", "having anointed"], ["आहरेत्", "should extract"]],
              "Face up, thighs bent, hip raised; anoint, then extract.",
              "उत्ताना, व्याभुग्न, सक्थि, कटि, अभ्यज्य, आहरेत्.", role="extend",
              teaches="व्याभुग्नसक्थ्याः is a bahuvrīhi: of her whose thighs are bent."),
        mcq("discriminate", 3, "By unit 100, what is anointed before the extraction?",
            ("The hand and the yoni", "हस्तं योनिं च ... अभ्यज्य: the hand and the yoni are anointed."),
            [("The belly and the two thighs", "The objects of अभ्यज्य are the hand and the yoni."),
             ("The fetus's head and shoulders", "The objects of अभ्यज्य are the hand and the yoni."),
             ("The cloth pad under the hips", "The pad only raises the hips; it is not anointed.")],
            "The hand and the yoni are anointed, then the fetus is extracted.",
            "हस्तं योनिं च अभ्यज्य."),
        mcq("apply", 4, "By the card, how sure is śālmalī-picchā as the gum of the silk-cotton tree?",
            ("Tree standard; gum probable", "Śālmalī = Bombax ceiba (standard); picchā = its gum (probable)."),
            [("Tree probable; gum standard", "The labels are the other way round: tree standard, gum probable."),
             ("Both standard and certain", "Only the tree is standard; the gum is probable."),
             ("Both unclear, untranslated", "Unclear is the label of धन्वनागमृत्तिका, not of śālmalī-picchā.")],
            "Śālmalī as Bombax ceiba is standard; picchā as its gum is probable.",
            "शाल्मली (मानक), पिच्छा = गोंद (सम्भावित)."),
        mcq("transfer", 5, "By the rule of उत्तानायाः + व्याभुग्न... (उत्तानाया व्याभुग्न...), how is बालायाः + वचनम् joined?",
            ("बालाया वचनम्", "आः before a voiced sound loses its visarga, as उत्तानायाः + व्याभुग्न..."),
            [("बालायो वचनम्", "ओ comes only from अः before a voiced sound, not from आः."),
             ("बालायार्वचनम्", "र् comes from a visarga after a vowel other than अ or आ."),
             ("बालायाश्वचनम्", "Before the voiced व the visarga after आ is dropped; श् comes before च or छ (optionally before श), not before व.")],
            "बालायाः + वचनम् = बालाया वचनम् (the girl's word), like उत्तानायाः + व्याभुग्न... = उत्तानाया व्याभुग्न...",
            "आः + voiced sound → आ (visarga dropped).",
            teaches="A visarga after आ is dropped before a voiced sound: उत्तानायाः + व्याभुग्न... → उत्तानाया व्याभुग्न..."),
    ],
}

# ---------------------------------------------------------------- unit 101
AUTHORED["101"] = {
    "title": "तत्र सक्थिभ्यामागतस्यानुलोम्याच्छिन्नमेव",
    "question": "By unit 101, which presentation is meant, and what can be said of the rest of the line?",
    "rule": ("There (तत्र): of one who has come by the two thighs (सक्थिभ्याम् आगतस्य), because of ānulomya (आनुलोम्यात्, "
             "following the natural direction), only cut (छिन्नम् एव): the sense of the end is uncertain."),
    "limits": ("Low confidence; elliptical. What is cut is not given, and छिन्नमेव may mean only cutting or be corrupt: no "
               "question on its sense (nor on the division of आनुलोम्याच्छिन्नमेव: the data notes an alternative such as अच्छिन्नम्). The case of सक्थिभ्याम् is not asked. Prose."),
    "explain_hi": ("यह अधूरी गद्य-पंक्ति है और इसका अर्थ अनिश्चित है। "
                   "वहाँ (तत्र): जो दोनों जाँघों से आया हो (सक्थिभ्याम् आगतस्य), उसका, आनुलोम्य यानी स्वाभाविक दिशा में होने के "
                   "कारण (आनुलोम्यात्), केवल कटा हुआ (छिन्नम् एव)। "
                   "क्या काटा जाए, इसकी संज्ञा या क्रिया नहीं दी गई; ‘छिन्नमेव’ का अर्थ ‘केवल काटना ही’ हो सकता है, या पाठ बिगड़ा "
                   "हो। "
                   "पक्की बातें: तत्र और दोनों जाँघों से आना; ‘आनुलोम्यात्’ (के कारण) डेटा का पठन है, विभाजन अनिश्चित।"),
    "hook": "जाँघों से आया, दिशा अनुकूल: आगे का अर्थ धुँधला।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 101, by what has this one come?",
            ("By the two thighs", "सक्थिभ्याम् आगतस्य: of one who has come by the two thighs."),
            [("By the head first", "No head is named in unit 101."),
             ("By one arm alone", "No arm is named in unit 101."),
             ("By the face upward", "No face is named in unit 101.")],
            "This one has come by the two thighs.",
            "सक्थिभ्याम् आगतस्य."),
        order(1, "Put the words of unit 101 in the line's order.",
              ["तत्र", "सक्थिभ्याम्", "आगतस्य", "आनुलोम्याच्छिन्नमेव"],
              "There, by the two thighs, of one come, ... (the end is uncertain).",
              "तत्र → सक्थिभ्याम् → आगतस्य → आनुलोम्याच्छिन्नमेव."),
        match(2, "Match each word of unit 101 to its meaning.",
              [["तत्र", "there, in that case"], ["सक्थि", "thigh"], ["आगत", "come, arrived"]],
              "There: of one come by the two thighs.",
              "तत्र, सक्थि, आगत.", role="extend",
              teaches="आगत is the past participle of आ-√गम्: come, arrived."),
        mcq("discriminate", 3, "Which split of सक्थिभ्यामागतस्य is right?",
            ("सक्थिभ्याम् + आगतस्य", "A final म् before a vowel joins it: सक्थिभ्याम् + आगतस्य → सक्थिभ्यामागतस्य."),
            [("सक्थिभ्या + मागतस्य", "मागतस्य is not a word; the word is आगतस्य, come."),
             ("सक्थिभ्याम् + अगतस्य", "म् + अ would give सक्थिभ्यामगतस्य, with a short अ."),
             ("सक्थिभ्यां + गतस्य", "Before ग the print would show सक्थिभ्यां गतस्य, with no आ.")],
            "सक्थिभ्याम् + आगतस्य (of the one come): म् joins the following vowel.",
            "म् + vowel → म् joins the vowel."),
        multi("apply", 4, "Which statements about unit 101 are right by the card?",
              [("It says the fetus must be cut in two", "No noun or verb for what is cut is given; nothing is supplied."),
               ("The sense of the line's end is uncertain", "Right: the data calls the sense uncertain."),
               ("No verb is printed", "Right: the unit is elliptical."),
               ("The line names the mother", "No mother is named in unit 101."),
               ("It names the two thighs", "Right: सक्थिभ्याम्, the two thighs.")],
              [1, 2, 4],
              "The line has no verb, its end is uncertain, and it names the two thighs.",
              "तत्र सक्थिभ्यामागतस्य आनुलोम्यात् ... (अर्थ अनिश्चित)."),
        mcq("transfer", 5, "By the rule of सक्थिभ्याम् + आगतस्य, how is फलम् + आनय (bring the fruit) joined?",
            ("फलमानय", "A final म् before a vowel joins it, as सक्थिभ्याम् + आगतस्य → सक्थिभ्यामागतस्य."),
            [("फलं आनय", "ं is written for म् only before a consonant; before आ the म् joins the vowel."),
             ("फलानय", "The म् is not lost; it joins the vowel."),
             ("फलमनय", "The long आ of आनय stays long.")],
            "फलम् + आनय = फलमानय, like सक्थिभ्याम् + आगतस्य = सक्थिभ्यामागतस्य.",
            "म् + vowel → joins the vowel.",
            teaches="A word-final म् before a vowel joins it: सक्थिभ्याम् + आगतस्य → सक्थिभ्यामागतस्य."),
    ],
}

# ---------------------------------------------------------------- unit 102
AUTHORED["102"] = {
    "title": "एकस्मिन् सक्थ्नि प्रपन्नस्येतरं सक्थि प्रसार्य ... निर्हरेत्",
    "question": "By unit 102, which five presentations are named, and how is each handled before drawing out?",
    "rule": ("One thigh presented: stretch out the other thigh. At the buttock region: press it down, lift upward, stretch the "
             "thighs. Transverse: turn round, or lift the hind half. Head turned aside: press the shoulder, lift, bring the head "
             "to the birth passage. Both arms: press the shoulders up, bring the head's base. Then draw out (निर्हरेत्)."),
    "limits": ("Low confidence; one long sentence with one verb and no object. Three forms are flagged as possible print slips (सक्थ्यनी, "
               "प्रसार्ये, परादर्द्धम्, read सक्थिनी, प्रसार्य, अपरार्धम्): no question on them or on the 'hind half' step. "
               "Birth passage and modern names (breech, transverse lie) are probable only."),
    "explain_hi": ("यह लम्बी गद्य-पंक्ति पाँच दशाएँ और उनका उपाय गिनाती है; अन्त में एक क्रिया ‘निर्हरेत्’ (निकाले) सबको बन्द करती है। "
                   "(१) एक जाँघ आगे आई हो तो दूसरी जाँघ फैलाकर; (२) स्फिग्देश यानी नितम्ब-प्रदेश से आया हो तो उसे दबाकर, ऊपर "
                   "उठाकर, जाँघें फैलाकर; (३) तिरछा आया हो तो घुमाकर, या पिछला आधा उठाकर अगले आधे को सीधा सन्तान के मार्ग (सम्भवतः जन्म-मार्ग) में लाकर; "
                   "(४) सिर बगल में मुड़ा हो तो कन्धा दबाकर, ऊपर उठाकर, सिर को सन्तान के मार्ग में लाकर; (५) दोनों भुजाएँ आगे "
                   "आई हों तो दोनों कन्धे ऊपर दबाकर, सिर की जड़ लाकर। "
                   "तीन छपे रूप (सक्थ्यनी, प्रसार्ये, परादर्द्धम्) छपाई-भूल माने गए हैं। "
                   "आधुनिक नाम (ब्रीच, अनुप्रस्थ स्थिति) केवल सम्भावित तुल्य हैं, पाठ में नहीं।"),
    "hook": "एक जाँघ, नितम्ब, तिरछा, मुड़ा सिर, दोनों भुजाएँ: हर एक का अपना उपाय, फिर निकालो।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 102, what is done when only one thigh has presented?",
            ("The other thigh is stretched out", "एकस्मिन् सक्थ्नि प्रपन्नस्येतरं सक्थि प्रसार्य."),
            [("The two shoulders are pressed up", "Pressing both shoulders up is for both arms presenting."),
             ("The woman is turned onto her side", "No turning of the woman is named in unit 102."),
             ("The thigh presented is pulled out", "The unit stretches out the other (इतरम्) thigh.")],
            "For one thigh presented, the other thigh is stretched out.",
            "इतरं सक्थि प्रसार्य."),
        order(1, "Put the five presentations of unit 102 in the line's order.",
              ["एकस्मिन् सक्थ्नि प्रपन्नस्य", "स्फिग्देशागतस्य", "तिर्यगागतस्य", "पार्श्ववृत्तशिरसः",
               "बाहुद्वयं प्रपन्नस्य"],
              "One thigh presented; come at the buttock region; come transversely; head turned to the side; both arms presented.",
              "एक सक्थि → स्फिग्देश → तिर्यक् → पार्श्ववृत्तशिरस् → बाहुद्वय."),
        match(2, "Match each presentation of unit 102 to its handling.",
              [["एकस्मिन् सक्थ्नि प्रपन्नस्य", "stretch out the other thigh"],
               ["स्फिग्देशागतस्य", "press the buttock region down, lift upward"],
               ["तिर्यगागतस्य", "turn it round"],
               ["पार्श्ववृत्तशिरसः", "press the shoulder, bring the head"],
               ["बाहुद्वयं प्रपन्नस्य", "press both shoulders up, bring the head's base"]],
              "Each case opens with 'for one who...' and has its own handling; then one draws out.",
              "प्रसार्य; प्रनिपीड्य उत्क्षिप्य; परिवर्त्य; प्रतिपीड्य आनीय; उत्पीड्य आनीय → निर्हरेत्.", role="extend",
              teaches="Each case opens with a genitive, 'for one who...'; the single verb निर्हरेत् (should draw out) closes them all."),
        mcq("discriminate", 3, "By unit 102, which handling is named first for the one that has come transversely?",
            ("It is turned round", "तिर्यगागतस्य परिवर्त्य: for one come transversely, having turned (it) round."),
            [("The other thigh is stretched", "That is the handling for one thigh presented."),
             ("Both shoulders are pressed up", "That is the handling for both arms presented."),
             ("The shoulder is pressed down", "Pressing the shoulder is for the head turned aside.")],
            "Turning round is named first; the other way (or ...) rests on a flagged reading.",
            "तिर्यगागतस्य परिवर्त्य."),
        mcq("apply", 4, "A fetus has come at the buttock region (स्फिग्देश). By unit 102, what is done to that region?",
            ("It is pressed down and lifted upward", "स्फिग्देशं प्रनिपीड्य ऊर्ध्वम् उत्क्षिप्य."),
            [("It is cut open with a round knife", "No cutting is named for this case in unit 102."),
             ("It is anointed with ghee and gum", "Anointing is in unit 100, of the hand and the yoni."),
             ("It is turned round to the left side", "Turning round is the handling of the transverse case.")],
            "The buttock region is pressed down and lifted upward.",
            "स्फिग्देशं प्रनिपीड्य ऊर्ध्वमुत्क्षिप्य."),
        mcq("transfer", 5, "By the rule of प्रपन्नस्य + इतरम्, how is रामस्य + इच्छा (Rāma's wish) joined?",
            ("रामस्येच्छा", "अ + इ → ए, as प्रपन्नस्य + इतरम् → प्रपन्नस्येतरम्."),
            [("रामस्यैच्छा", "ऐ comes from अ + ए or अ + ऐ, not from अ + इ."),
             ("रामस्योच्छा", "ओ comes from अ + उ, not from अ + इ."),
             ("रामस्यीच्छा", "The अ does not vanish; अ + इ merge into ए.")],
            "रामस्य + इच्छा = रामस्येच्छा, like प्रपन्नस्य + इतरम् = प्रपन्नस्येतरम्.",
            "अ + इ → ए.",
            teaches="A short अ followed by इ joins as ए: प्रपन्नस्य + इतरम् → प्रपन्नस्येतरम्."),
    ],
}

# ---------------------------------------------------------------- unit 103
AUTHORED["103"] = {
    "title": "यस्त्वभ्युग्नमध्यः पाणिपादशिरोभिर्योनिं प्रतिपद्यते",
    "question": "By unit 103, how does this one come to the yoni?",
    "rule": ("But (तु) the one who (यः), with its middle bent (data reading अभुग्नमध्यः), comes to the yoni (योनिं प्रतिपद्यते) "
             "with hands, feet and head (पाणिपादशिरोभिः). A 'who' clause; the data finds its main clause in unit 105."),
    "limits": ("Printed अभ्युग्न is not a known word; 'bent' rests on a flagged reading (अभुग्न, as in unit 104): no question on "
               "that word. The one who comes is the fetus by context only. A prose line."),
    "explain_hi": ("यह गद्य-पंक्ति एक सापेक्ष वाक्य है (यः = जो)। "
                   "पर (तु) जो, मुड़े हुए मध्य भाग वाला, हाथ, पैर और सिर से (पाणिपादशिरोभिः) योनि में आता है (प्रतिपद्यते)। "
                   "छपा ‘अभ्युग्न’ ज्ञात शब्द नहीं; डेटा उसे ‘अभुग्न’ (मुड़ा हुआ) पढ़ता है, जो इकाई १०४ में आता है। "
                   "डेटा के अनुसार इस वाक्य का मुख्य भाग इकाई १०५ (‘तौ मूढौ’) में है। "
                   "‘पाणिपादशिरोभिः’ द्वन्द्व समास, तृतीया बहुवचन है: हाथों, पैरों और सिर से।"),
    "hook": "हाथ, पैर और सिर, सब एक साथ योनि में: बीच से मुड़ा।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 103, with what does this one come to the yoni?",
            ("With hands, feet and head", "पाणिपादशिरोभिः योनिं प्रतिपद्यते."),
            [("With the back and the hip", "Back and hip are not named in unit 103."),
             ("With the chest and chin", "Chest and chin are not named in unit 103."),
             ("With the knees bent first", "Knees are not named in unit 103.")],
            "It comes to the yoni with hands, feet and head.",
            "पाणि-पाद-शिरोभिः."),
        order(1, "Put the parts of unit 103 in the line's order.",
              ["यस्त्वभ्युग्नमध्यः", "पाणिपादशिरोभिः", "योनिम्", "प्रतिपद्यते"],
              "But the one who, middle bent, with hands, feet and head, to the yoni, comes.",
              "यस्त्वभ्युग्नमध्यः → पाणिपादशिरोभिः → योनिम् → प्रतिपद्यते."),
        match(2, "Match each word of unit 103 to its meaning.",
              [["पाणि", "hand"], ["पाद", "foot"], ["शिरस्", "head"], ["मध्य", "middle"],
               ["प्रतिपद्यते", "comes to, enters"]],
              "With hands, feet and head it comes to the yoni.",
              "पाणि, पाद, शिरस्, मध्य, प्रतिपद्यते.", role="extend",
              teaches="पाणिपादशिरोभिः is a dvandva in the instrumental plural: with hands, feet and head."),
        mcq("discriminate", 3, "Which split of शिरोभिर्योनिम् is right?",
            ("शिरोभिः + योनिम्", "A visarga after इ before a voiced sound becomes र्."),
            [("शिरोभी + योनिम्", "With no visarga, no र् would appear: शिरोभीयोनिम्."),
             ("शिरोभिम् + योनिम्", "म् before य would give ं (शिरोभिं योनिम्), not र्."),
             ("शिरोभिर + योनिम्", "शिरोभिर is not a form; the instrumental plural is शिरोभिः.")],
            "शिरोभिः (with heads) + योनिम्: इः before the voiced य → इर्.",
            "इः + voiced sound → इर्."),
        multi("apply", 4, "Which statements about unit 103 are right by the card?",
              [("It comes with hands, feet and head", "Right: पाणिपादशिरोभिः."),
               ("It comes with one foot to the anus", "That is said in unit 104, not here."),
               ("The line says it must be cut at once", "No cutting is named in unit 103."),
               ("Its verb is प्रतिपद्यते, comes to", "Right: योनिं प्रतिपद्यते.")],
              [0, 3],
              "It comes to the yoni with hands, feet and head; the verb is प्रतिपद्यते.",
              "पाणिपादशिरोभिः योनिं प्रतिपद्यते."),
        mcq("transfer", 5, "By the rule of यः + तु → यस्तु, how is रामः + तत्र (Rāma there) joined?",
            ("रामस्तत्र", "A visarga before त becomes स्, as यः + तु → यस्तु."),
            [("रामो तत्र", "अः becomes ओ only before a voiced sound; त is unvoiced."),
             ("रामर्तत्र", "र् comes from a visarga after a vowel other than अ or आ."),
             ("रामश्तत्र", "Before त the visarga becomes स्; श् comes before च or छ (optionally before श).")],
            "रामः + तत्र = रामस्तत्र, like यः + तु = यस्तु.",
            "Visarga + त/थ → स्.",
            teaches="A visarga before त or थ becomes स्: यः + तु → यस्तु."),
    ],
}

# ---------------------------------------------------------------- unit 104
AUTHORED["104"] = {
    "title": "यश्चाभुग्नएवैकेन पादेन योनिं द्वितीयेन पायुं",
    "question": "By unit 104, where do the two feet of this one go?",
    "rule": ("And the one who (यः च), just bent (अभुग्नः एव), (comes) with one foot (एकेन पादेन) to the yoni, with the "
             "second (द्वितीयेन) to the anus (पायु)."),
    "limits": ("No verb is printed; the data carries प्रतिपद्यते from unit 103 and does not supply it. The one who comes is the "
               "fetus by context only. Pāyu = anus (standard). A prose line."),
    "explain_hi": ("यह गद्य-पंक्ति दूसरी दशा कहती है: और जो (यश्च) मुड़ा हुआ ही (अभुग्न एव) एक पैर से (एकेन पादेन) योनि में और "
                   "दूसरे से (द्वितीयेन) पायु यानी गुदा में (आता है)। "
                   "क्रिया छपी नहीं; डेटा ‘प्रतिपद्यते’ को इकाई १०३ से आया मानता है, जोड़ता नहीं। "
                   "छपा ‘यश्चाभुग्नएवैकेन’ = यः च अभुग्नः एव एकेन; ‘अभुग्न’ और ‘एव’ के बीच विसर्ग लुप्त होकर अन्तर रहता है।"),
    "hook": "मुड़ा हुआ: एक पैर योनि में, दूसरा गुदा में।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 104, where does the second foot go?",
            ("To the anus", "द्वितीयेन पायुम्: with the second, to the anus (pāyu)."),
            [("To the navel", "No navel is named in unit 104."),
             ("To the thigh", "No thigh is named in unit 104."),
             ("To the yoni", "It is the first foot that goes to the yoni.")],
            "One foot goes to the yoni, the second to the anus.",
            "एकेन पादेन योनिम्, द्वितीयेन पायुम्."),
        order(1, "Put the parts of unit 104 in the line's order.",
              ["यश्चाभुग्नएवैकेन", "पादेन", "योनिं", "द्वितीयेन", "पायुं"],
              "And the one who, just bent, with one foot, to the yoni, with the second, to the anus.",
              "यश्चाभुग्नएवैकेन → पादेन → योनिं → द्वितीयेन → पायुं."),
        match(2, "Match each word of unit 104 to its meaning.",
              [["एक", "one"], ["पाद", "foot"], ["द्वितीय", "second"], ["पायु", "anus"]],
              "One foot to the yoni, the second to the anus.",
              "एक, पाद, द्वितीय, पायु.", role="extend",
              teaches="एकेन ... द्वितीयेन = with the one ... with the second: both instrumental, both with पादेन."),
        mcq("discriminate", 3, "Which split of एवैकेन is right?",
            ("एव + एकेन", "अ + ए → ऐ: एव + एकेन → एवैकेन."),
            [("एव + इकेन", "अ + इ would give ए: एवेकेन."),
             ("एव + उकेन", "अ + उ would give ओ: एवोकेन."),
             ("एवै + केन", "एवै is not a word; the particle is एव.")],
            "एव (just) + एकेन (with one): अ + ए → ऐ.",
            "अ + ए → ऐ."),
        multi("apply", 4, "Which statements about unit 104 are right by the card?",
              [("The line prescribes cutting the foot", "No cutting is named in unit 104."),
               ("One foot goes to the yoni", "Right: एकेन पादेन योनिम्."),
               ("The second goes to the anus", "Right: द्वितीयेन पायुम्."),
               ("Hands and head come first here", "Hands, feet and head are unit 103.")],
              [1, 2],
              "One foot to the yoni, the second to the anus; nothing more is said.",
              "एकेन पादेन योनिं द्वितीयेन पायुम्."),
        mcq("transfer", 5, "By the rule of अभुग्नः + एव (अभुग्न एव), how is रामः + इति joined?",
            ("राम इति", "अः before a vowel other than अ loses the visarga; the gap stays."),
            [("रामो इति", "अः becomes ओ before a voiced consonant or अ, not before इ."),
             ("रामर् इति", "र् comes from a visarga after a vowel other than अ or आ."),
             ("रामेति", "After the visarga is lost, the two vowels are not joined again.")],
            "रामः + इति = राम इति, like अभुग्नः + एव = अभुग्न एव.",
            "अः + vowel other than अ → अ (visarga dropped, gap stays).",
            teaches="अः before a vowel other than अ drops the visarga and leaves a gap: अभुग्नः + एव → अभुग्न एव."),
    ],
}

# ---------------------------------------------------------------- unit 105
AUTHORED["105"] = {
    "title": "तौ मूढौ हस्तेनाहर्तुमशक्याविति शस्त्रमवचारयेत्",
    "question": "By unit 105, why should the instrument be applied to those two?",
    "rule": ("Those two (तौ), mūḍha (मूढ, stuck), cannot be extracted by the hand (हस्तेन आहर्तुम् अशक्यौ); thus (इति) one "
             "should apply the instrument (शस्त्रम् अवचारयेत्)."),
    "limits": ("That the two are the cases of units 103-104 is the data's reading; the line does not say so in words. Mūḍha keeps "
               "its technical sense, stuck. No other reason is given. A prose line."),
    "explain_hi": ("यह गद्य-पंक्ति निर्णय देती है: वे दोनों (तौ) मूढ यानी अटके हुए हाथ से निकाले नहीं जा सकते (हस्तेन आहर्तुम् "
                   "अशक्यौ), इसलिए (इति) शस्त्र का प्रयोग करे (शस्त्रमवचारयेत्)। "
                   "डेटा ‘तौ’ को इकाई १०३ और १०४ की दो दशाएँ मानता है; पंक्ति यह शब्दों में नहीं कहती। "
                   "‘इति’ कारण को बन्द करता है: यह सोचकर कि हाथ से नहीं निकलते। "
                   "‘आहर्तुम्’ तुमुन्नन्त है (निकालने को); ‘अशक्य’ = जो न हो सके।"),
    "hook": "हाथ से न निकले, तो शस्त्र।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 105, what should one apply to those two?",
            ("The cutting instrument", "शस्त्रमवचारयेत्: one should apply the instrument (śastra)."),
            [("Cold water to the belly", "No cold water is named in unit 105."),
             ("Gentle pressing by hand", "The unit says they cannot be extracted by the hand."),
             ("Oil and warm fomentation", "No oil or fomentation is named in unit 105.")],
            "One should apply the instrument.",
            "शस्त्रम् अवचारयेत्."),
        order(1, "Put the parts of unit 105 in the line's order.",
              ["तौ मूढौ", "हस्तेनाहर्तुम्", "अशक्याविति", "शस्त्रमवचारयेत्"],
              "Those two, stuck, by the hand to be extracted, impossible: thus one should apply the instrument.",
              "तौ मूढौ → हस्तेनाहर्तुम् → अशक्याविति → शस्त्रमवचारयेत्."),
        match(2, "Match each word of unit 105 to its meaning.",
              [["मूढ", "stuck"], ["हस्त", "hand"], ["आहर्तुम्", "to extract"], ["अशक्य", "impossible"],
               ["अवचारयेत्", "should apply"]],
              "Stuck, not extractable by hand: apply the instrument.",
              "मूढ, हस्त, आहर्तुम्, अशक्य, अवचारयेत्.", role="extend",
              teaches="-तुम् makes an infinitive: आ-√हृ → आहर्तुम्, to extract."),
        mcq("discriminate", 3, "Which split of अशक्याविति is right?",
            ("अशक्यौ + इति", "औ before a vowel becomes आव्: अशक्यौ + इति → अशक्याविति."),
            [("अशक्यः + इति", "अः before इ would give अशक्य इति, with a gap."),
             ("अशक्ये + इति", "ए before इ would give अशक्ययिति or अशक्य इति, not आवि."),
             ("अशक्या + विति", "विति is not a word; the particle is इति.")],
            "अशक्यौ (the two, impossible) + इति (thus): औ + vowel → आव्.",
            "औ + vowel → आव्."),
        mcq("apply", 4, "Why does unit 105 call for the instrument?",
            ("They cannot be drawn out by hand", "हस्तेनाहर्तुमशक्यौ इति: thinking they cannot be extracted by hand."),
            [("The fetus has grown far too large", "Size is not named in unit 105."),
             ("The lord has ordered it to be done", "No order of the lord is named in unit 105."),
             ("The yoni is too narrow to pass it", "No narrowness is named in unit 105.")],
            "The two are stuck and cannot be extracted by hand; thus the instrument.",
            "हस्तेन आहर्तुम् अशक्यौ इति शस्त्रम्."),
        mcq("transfer", 5, "By the rule of अशक्यौ + इति, how is बालौ + अत्र (the two boys here) joined?",
            ("बालावत्र", "औ before a vowel becomes आव्, as अशक्यौ + इति → अशक्याविति."),
            [("बालोऽत्र", "ओऽ comes from अः + अ (बालः + अत्र), a singular."),
             ("बालयत्र", "अय् comes from ए before a vowel, not from औ."),
             ("बालौत्र", "औ does not swallow the अ; it becomes आव्.")],
            "बालौ + अत्र = बालावत्र, like अशक्यौ + इति = अशक्याविति.",
            "औ + vowel → आव्.",
            teaches="औ before a vowel becomes आव्: अशक्यौ + इति → अशक्याविति."),
    ],
}

# ---------------------------------------------------------------- unit 106
AUTHORED["106"] = {
    "title": "अथस्त्रियमाश्वास्य मंडलाग्रेणांगुलिशस्त्रेण वा विदार्य",
    "question": "By unit 106, in what order are the steps done, and with what instruments?",
    "rule": ("Then: having comforted the woman (आश्वास्य), having split open with a maṇḍalāgra (probably a round-tipped knife) "
             "or an aṅguliśastra (probably a finger-knife), having removed the skull pieces (शिरःकपालानि), having seized with a "
             "hook (शङ्कु) at the chin, palate, chest or armpit, one should draw (it) away (अपहरेत्)."),
    "limits": ("Palate rests on a flagged reading (तालुकि read तालुनि): no question on it. Whether the hook seizes at these "
               "places or the fetus is drawn from them is open; not asked. Objects are unstated; instrument names probable. Prose."),
    "explain_hi": ("यह गद्य-पंक्ति क्रम से क्रियाएँ देती है, अन्त में एक क्रिया ‘अपहरेत्’ (हटा ले)। "
                   "पहले स्त्री को आश्वस्त करके (आश्वास्य); फिर मण्डलाग्र (सम्भवतः गोल नोक वाला शस्त्र) या अंगुलिशस्त्र (सम्भवतः "
                   "उँगली का शस्त्र) से चीरकर (विदार्य); सिर की खोपड़ी के टुकड़े निकालकर (शिरःकपालान्याहृत्य); शंकु से ठोड़ी, तालु, "
                   "छाती या काँख में पकड़कर (गृहीत्वा) हटा ले। "
                   "‘तालु’ सुधारे गए सम्भावित पाठ पर टिका है। "
                   "शंकु इन स्थानों पर पकड़ता है या गर्भ इनसे खींचा जाता है, शब्दों से तय नहीं; पहला पठन सरल है।"),
    "hook": "पहले ढाढ़स, फिर चीरा, खोपड़ी के टुकड़े, फिर शंकु से पकड़कर खींचो।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 106, what is done for the woman first?",
            ("She is comforted", "स्त्रियमाश्वास्य: having comforted the woman."),
            [("She is turned face down", "No turning face down is named in unit 106."),
             ("She is tied to the bed", "No tying is named in unit 106."),
             ("She is left by herself", "The unit begins by comforting her, not leaving her.")],
            "First the woman is comforted.",
            "स्त्रियम् आश्वास्य."),
        order(1, "Put the steps of unit 106 in the line's order.",
              ["स्त्रियमाश्वास्य", "विदार्य", "शिरःकपालान्याहृत्य", "शंकुना गृहीत्वा", "अपहरेत्"],
              "Having comforted the woman, having split open, having removed the skull pieces, having seized with a hook, "
              "one should draw away.",
              "आश्वास्य → विदार्य → शिरःकपालान्याहृत्य → शंकुना गृहीत्वा → अपहरेत्."),
        match(2, "Match each word of unit 106 to its meaning.",
              [["आश्वास्य", "having comforted"], ["विदार्य", "having split open"], ["कपाल", "skull piece"],
               ["शङ्कु", "hook"], ["चुबुक", "chin"], ["कक्षा", "armpit"]],
              "Comfort, split open, remove the skull pieces, seize with a hook, draw away.",
              "आश्वास्य, विदार्य, कपाल, शङ्कु, चुबुक, कक्षा.", role="extend",
              teaches="A chain of absolutives (-य, -त्वा) ends in one finite verb: ... गृहीत्वा ... अपहरेत्."),
        mcq("discriminate", 3, "By the card, how are maṇḍalāgra and aṅguliśastra identified?",
            ("Probably a round-tipped knife and a finger-knife", "The data labels both identifications probable."),
            [("Certainly a saw and a pair of forceps", "Neither a saw nor forceps is named; the labels are probable."),
             ("A hook and a peg, both as standard", "The hook (शङ्कु) is a third instrument of the line."),
             ("Unclear words, left untranslated here", "They are translated, with the label probable.")],
            "Maṇḍalāgra: probably a round-tipped knife; aṅguliśastra: probably a finger-knife.",
            "मण्डलाग्र, अंगुलिशस्त्र (सम्भावित)."),
        multi("apply", 4, "Which of these places are named with the hook in unit 106?",
              [("Chin", "Right: चुबुके."),
               ("Chest", "Right: उरसि."),
               ("Knee", "No knee is named in unit 106."),
               ("Armpit", "Right: कक्षायाम्."),
               ("Navel", "No navel is named in unit 106.")],
              [0, 1, 3],
              "Chin, chest and armpit are named (with the palate, on a flagged reading).",
              "चुबुके, (तालुनि), उरसि, कक्षायाम्."),
        mcq("transfer", 5, "By the rule of कपालानि + आहृत्य, how is वारि + आनय (bring water) joined?",
            ("वार्यानय", "इ before a different vowel becomes य्: इ + आ → या, as कपालानि + आहृत्य."),
            [("वारीनय", "ई comes from इ + इ, not from इ + आ."),
             ("वारेनय", "ए comes from अ + इ, not from इ + आ."),
             ("वारानय", "The इ does not vanish; it becomes य्.")],
            "वारि + आनय = वार्यानय, like कपालानि + आहृत्य = कपालान्याहृत्य.",
            "इ + आ → या.",
            teaches="इ before a different vowel becomes य्: कपालानि + आहृत्य → कपालान्याहृत्य."),
    ],
}

# ---------------------------------------------------------------- unit 107
AUTHORED["107"] = {
    "title": "अभिन्नशिरसं वाऽक्षिकूटे गंडे वा",
    "question": "By unit 107, which other case is meant, and which places are named?",
    "rule": ("Or (वा) one whose head is unsplit (अभिन्नशिरसम्): at the akṣikūṭa (अक्षिकूट, probably the eye-socket rim) or at "
             "the cheek (गण्ड). The action is not printed."),
    "limits": ("No verb: the data carries the seizing and drawing away from unit 106 and does not supply them; no question on the "
               "action. Akṣikūṭa as the eye-socket rim is probable; gaṇḍa may also mean the temple. The noun after अभिन्नशिरसम् "
               "is the fetus by context. A prose line."),
    "explain_hi": ("यह अधूरी गद्य-पंक्ति एक और दशा जोड़ती है: या जिसका सिर विदीर्ण न हुआ हो (अभिन्नशिरसम्), "
                   "अक्षिकूट (सम्भवतः आँख के गड्ढे का किनारा) पर या गण्ड यानी गाल पर। "
                   "क्रिया नहीं है; डेटा शंकु से पकड़कर खींचने की क्रिया को इकाई १०६ से आया मानता है, जोड़ता नहीं। "
                   "‘अभिन्न’ = अ + भिन्न (न फटा)। "
                   "गण्ड का अर्थ कनपटी भी हो सकता है।"),
    "hook": "सिर न फटा हो तो आँख का किनारा या गाल।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 107, what kind of head does this case have?",
            ("An unsplit head", "अभिन्नशिरसम्: one whose head is unsplit."),
            [("A very small head", "Size is not named in unit 107."),
             ("A head turned aside", "A head turned aside is a case of unit 102."),
             ("A head split open", "The head here is अभिन्न, not split.")],
            "The head here is unsplit.",
            "अभिन्न-शिरस्."),
        order(1, "Put the parts of unit 107 in the line's order.",
              ["अभिन्नशिरसं", "वाऽक्षिकूटे", "गंडे वा"],
              "One whose head is unsplit, or at the akṣikūṭa, at the cheek, or.",
              "अभिन्नशिरसं → वाऽक्षिकूटे → गंडे वा."),
        match(2, "Match each word of unit 107 to its meaning.",
              [["अभिन्न", "unsplit"], ["शिरस्", "head"], ["अक्षिकूट", "eye-socket rim, probably"],
               ["गण्ड", "cheek"]],
              "Unsplit head: at the akṣikūṭa or the cheek.",
              "अभिन्न, शिरस्, अक्षिकूट, गण्ड.", role="extend",
              teaches="अभिन्नशिरसम् is a bahuvrīhi: one whose head (शिरस्) is unsplit (अभिन्न = अ + भिन्न)."),
        mcq("discriminate", 3, "By the card, what is uncertain about गण्ड here?",
            ("It may mean cheek or temple", "The data: gaṇḍa = cheek; it can also mean temple."),
            [("It may mean chin or the palate", "Chin and palate are named in unit 106, not as senses of गण्ड."),
             ("It is a word nobody knows", "गण्ड is a known word; only its exact part is open."),
             ("It is a corrected print reading", "गंडे is printed and kept; only the sense is open.")],
            "गण्ड is taken as cheek, though it may also mean the temple.",
            "गण्ड = गाल (कनपटी भी)."),
        multi("apply", 4, "Which statements about unit 107 are right by the card?",
              [("The line names the hook (शङ्कु) itself", "शङ्कु is in unit 106; it is not printed here."),
               ("The line says the skull pieces are removed", "That is unit 106; here the head is unsplit."),
               ("No verb is printed", "Right: the action is not printed."),
               ("Akṣikūṭa is probably the eye-socket rim", "Right: the data labels it probable."),
               ("The head in this case is unsplit", "Right: अभिन्नशिरसम्.")],
              [2, 3, 4],
              "No verb; the head is unsplit; akṣikūṭa is probably the eye-socket rim.",
              "अभिन्नशिरसं वा अक्षिकूटे गण्डे वा."),
        mcq("transfer", 5, "अक्षिकूटे and गण्डे are locatives (at). Which form of हस्त means at the hand?",
            ("हस्ते", "An अ-stem makes its locative singular in -ए, as गण्ड → गण्डे."),
            [("हस्तेन", "-एन is the instrumental: by the hand (as हस्तेन in unit 105)."),
             ("हस्तम्", "-अम् is the accusative: the hand as object."),
             ("हस्तस्य", "-अस्य is the genitive: of the hand.")],
            "हस्त → हस्ते (at the hand), like गण्ड → गण्डे (at the cheek).",
            "अ-stem locative singular → -ए.",
            teaches="An अ-stem noun makes its locative singular in -ए: गण्डे, अक्षिकूटे (at)."),
    ],
}

# ---------------------------------------------------------------- unit 108
AUTHORED["108"] = {
    "title": "तथाऽंससंसक्तस्यांसदेशे बाहुं छित्वा",
    "question": "By unit 108, how are the one stuck at the shoulder and the one swollen like a skin-bag handled?",
    "rule": ("Likewise: for one stuck at the shoulder (अंससंसक्त), having cut off the arm at the shoulder region; for one swollen "
             "like a skin-bag (दृतेरिव आध्मात), having split open the belly full of wind and cast out the intestines, one "
             "should extract (it) when it has become slack (शिथिलीभूतम् आहरेत्)."),
    "limits": ("The objects of छित्वा and आहरेत् are not stated (the fetus by context). The case of दृतेः (genitive or ablative, "
               "used loosely for 'like') is not asked. Printed छित्वा is a spelling of छित्त्वा. A prose line."),
    "explain_hi": ("यह गद्य-पंक्ति दो और दशाएँ देती है। "
                   "(१) जो कन्धे में अटका हो (अंससंसक्तस्य), उसकी भुजा कन्धे के स्थान पर काटकर (अंसदेशे बाहुं छित्वा); "
                   "(२) जो दृति यानी चमड़े की मशक की तरह फूला हो (दृतेरिव आध्मातस्य), उसका वायु से भरा पेट चीरकर (वातपूर्णमुदरमवदार्य) "
                   "और आँतें निकालकर (निरस्यान्त्राणि), ढीला हो जाने पर (शिथिलीभूतम्) निकाले (आहरेत्)। "
                   "किसे काटना या निकालना है, कर्म नहीं दिया; संदर्भ से गर्भ। "
                   "‘शिथिलीभूत’ च्वि-रूप है: जो ढीला नहीं था, वह ढीला हो गया।"),
    "hook": "कन्धे में अटका: भुजा काटो; मशक-सा फूला: पेट चीरो, आँतें निकालो, ढीला होने पर निकालो।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 108, what is cut off for one stuck at the shoulder?",
            ("The arm, at the shoulder region", "अंसदेशे बाहुं छित्वा: having cut off the arm at the shoulder region."),
            [("The head, at the neck", "No cutting at the neck is named in unit 108."),
             ("Nothing; the arm is only pressed", "The unit says the arm is cut off: छित्वा."),
             ("The fingers of the one hand", "No fingers are named in unit 108.")],
            "The arm is cut off at the shoulder region.",
            "अंसदेशे बाहुं छित्वा."),
        order(1, "Put these phrases of unit 108 in the line's order.",
              ["तथाऽंससंसक्तस्य", "अंसदेशे बाहुं छित्वा", "दृतेरिवाध्मातस्य", "वातपूर्णमुदरमवदार्य",
               "निरस्यान्त्राणि", "शिथिलीभूतमाहरेत्"],
              "Likewise, for one stuck at the shoulder, cutting the arm at the shoulder region; for one swollen like a "
              "skin-bag, splitting the wind-filled belly, casting out the intestines, one should extract it when slack.",
              "अंससंसक्तस्य → बाहुं छित्वा → दृतेरिवाध्मातस्य → उदरमवदार्य → निरस्यान्त्राणि → शिथिलीभूतमाहरेत्."),
        match(2, "Match each word of unit 108 to its meaning.",
              [["अंस", "shoulder"], ["संसक्त", "stuck"], ["बाहु", "arm"], ["दृति", "skin-bag"],
               ["आध्मात", "swollen"], ["अन्त्र", "intestines"]],
              "Stuck at the shoulder: the arm; swollen like a skin-bag: belly and intestines.",
              "अंस, संसक्त, बाहु, दृति, आध्मात, अन्त्र.", role="extend",
              teaches="शिथिलीभूत is a cvi form: शिथिल + ई + भूत, 'become slack' (what was not slack)."),
        mcq("discriminate", 3, "For the one swollen like a skin-bag, what is split open?",
            ("The belly, full of wind", "वातपूर्णमुदरमवदार्य: having split open the belly full of wind."),
            [("The head, to take out skull pieces", "Skull pieces are removed in unit 106, not here."),
             ("The chest, near the armpit", "No chest is split in unit 108."),
             ("The shoulder, to free the arm", "The arm is cut off for the shoulder case, not the swollen one.")],
            "The belly, full of wind, is split open and the intestines are cast out.",
            "वातपूर्णम् उदरम् अवदार्य."),
        mcq("apply", 4, "By unit 108, when is the swollen one extracted?",
            ("When it has become slack", "शिथिलीभूतमाहरेत्: one should extract (it) when it has become slack."),
            [("While still swollen and tight", "It is extracted once slack, after the belly is opened."),
             ("At once, before any cutting", "The belly is split and the intestines cast out first."),
             ("Only after the arm is cut", "Cutting the arm is the handling of the shoulder case.")],
            "After the belly is split and the intestines cast out, it is extracted when slack.",
            "शिथिलीभूतम् आहरेत्."),
        mcq("transfer", 5, "By the rule of दृतेः + इव, how is मुनेः + आश्रमः (the sage's hermitage) joined?",
            ("मुनेराश्रमः", "A visarga after ए before a voiced sound (here a vowel) becomes र्, as दृतेः + इव."),
            [("मुने आश्रमः", "Only अः and आः lose the visarga before a vowel; after ए it becomes र्."),
             ("मुनेऽश्रमः", "ऽ marks a lost अ after ए or ओ; here आ follows, after a visarga."),
             ("मुनेस्आश्रमः", "Before a vowel, ः after ए becomes र्; स् comes before त or थ (optionally before स).")],
            "मुनेः + आश्रमः = मुनेराश्रमः, like दृतेः + इव = दृतेरिव.",
            "एः + voiced sound → एर्.",
            teaches="A visarga after a vowel other than अ/आ becomes र् before a voiced sound: दृतेः + इव → दृतेरिव."),
    ],
}


# ===================================================================== NOTES_HI
NOTES_HI = {
    "95": ("दो छपी पंक्तियाँ (०२.०४.१०१-१०२) एक इकाई में; गद्य; विश्वास मध्यम। पहली पंक्ति में क्रिया ‘है’ समझी जाती है। "
           "‘दृष्टकर्मन्’ = जिसका कर्म देखा गया हो (अनुभवी); ‘शल्यहर्तृ’ = शल्य निकालने वाला (शल्य-चिकित्सक, सम्भावित)। "
           "यहाँ शल्य गर्भ है, यह डेटा संदर्भ (इकाई ८९) से पढ़ता है; इस पंक्ति में नहीं कहा। डेटा के अनुसार ‘इत्येके’ वाले तीन मत "
           "(इकाई ९४-९५) में से पाठ कौन-सा मानता है, यह नहीं बताया। ‘कष्टतम’ = सबसे कठिन; ‘सबसे पीड़ादायक’ भी सम्भव। "
           "सन्धि जाँची: शल्य + आहरणम् → शल्याहरणम् (अ + आ → आ); आहरणम् + इति → आहरणमिति; इति + एके → इत्येके (इ + ए → ये); "
           "कष्टतमम् + अस्ति → कष्टतममस्ति।"),
    "96": ("गद्य; विश्वास निम्न (कठिन इकाई)। पाठ-चिह्न: छपा ‘अवधार्यम्’ (निश्चित किया जाए) सम्भवतः ‘अवचार्यम्’ (प्रयोग किया जाए; "
           "तुलना: इकाई १०५ का ‘अवचारयेत्’) की छपाई-भूल है (ध/च का भ्रम); इस पर प्रश्न नहीं। ‘ताननुपहिंसताऽस्पर्शयता’ = जो उन्हें न "
           "चोट पहुँचाए, न छूने दे; ‘अस्पर्शयता’ का कर्म नहीं दिया, यह एक पठन है। ‘व्यावर्त्तन’, ‘उत्कर्त्तन’ में र्त्त = र्त (पुस्तक "
           "की छपाई-आदत)। डेटा के अनुसार यह ‘यतः’ वाला कारण सम्भवतः इकाई ९५ से जुड़ता है। सन्धि जाँची: यतः + योनि → यतो योनि "
           "(अः + घोष → ओ); प्लीह + अन्त्र → प्लीहान्त्र (अ + अ → आ); गर्भाशय + आदीनाम् → गर्भाशयादीनाम् (अ + आ → आ); तान् + "
           "अनुपहिंसता → ताननुपहिंसता; अनुपहिंसता + अस्पर्शयता → अनुपहिंसतास्पर्शयता (आ + अ → आ; छपाई ने ऽ लगाया); पीडन + "
           "ऋजूकरणानि → पीडनर्जूकरणानि (अ + ऋ → अर्); च + एकेन → चैकेन (अ + ए → ऐ)।"),
    "97": ("गद्य; विश्वास मध्यम। ‘ईश्वर’ = स्वामी (सम्भवतः राजा या घर का मुखिया; परिभाषित नहीं), ईश्वर-देव नहीं। ‘तद्विद्य’ = उस "
           "(कला) को जानने वाले। ‘तम्’ पुंलिंग; किसे कहता है (रोगी-दशा या गर्भ), नहीं बताया। ‘परम्’ को ‘यत्नम्’ के साथ पढ़ा "
           "(परम प्रयत्न)। छपा ‘यत्नमास्थायतद्विद्यसहितस्तमुपक्रमेत्’ शब्द मिलाकर छपा है; बिना पाठ-चिह्न के अलग किया गया। "
           "सन्धि जाँची: तस्मात् + ईश्वरम् → तस्मादीश्वरम् (त् + स्वर → द्); ईश्वरम् + आपृच्छ्य → ईश्वरमापृच्छ्य; परम् + च → परं च "
           "(व्यंजन से पहले म् → अनुस्वार); यत्नम् + आस्थाय → यत्नमास्थाय; तत् + विद्य → तद्विद्य (त् + घोष → द्); सहितः + तम् → "
           "सहितस्तम् (विसर्ग + त → स्); तम् + उपक्रमेत् → तमुपक्रमेत्।"),
    "98": ("गद्य; विश्वास उच्च। क्रिया ‘है’ समझी जाती है; कर्ता (माता या स्त्री) नहीं बताया। ‘अक्रियायाम्’ स्त्रीलिंग सप्तमी "
           "एकवचन: कर्म न करने पर। डेटा के अनुसार अगली इकाई (९९) सम्भवतः इसी पंक्ति को आगे बढ़ाती है। सन्धि जाँची: अक्रियायाम् + "
           "ध्रुवम् → अक्रियायां ध्रुवम्, ध्रुवम् + मरणम् → ध्रुवं मरणम् (व्यंजन से पहले म् → अनुस्वार); अन्त का ‘मरणं’ छपाई का "
           "अनुस्वार है।"),
    "99": ("गद्य; विश्वास मध्यम। पाठ-चिह्न: छपे ‘प्रभृतीनापि’ में षष्ठी बहुवचन ‘प्रभृतीनाम्’ का म् (अनुस्वार) छूटा लगता है "
           "(सम्भावित पाठ: प्रभृतीनाम् अपि)। क्रिया नहीं; इनके बारे में क्या कहा गया (शस्त्रकर्म चाहिए, या कर्म न करने पर मृत्यु), "
           "पाठ नहीं बताता और जोड़ा नहीं गया। ‘उदर’ यहाँ रोग है (पेट का रोग, सम्भवतः जलोदर जैसा: सम्भावित); अन्यत्र पुस्तक में "
           "इसका अर्थ पेट भी है। अश्मरी = मूत्र की पथरी (मानक)। डेटा: सम्भवतः इकाई ९८ को आगे बढ़ाती है। छपे ‘उदरअश्मरी’ में "
           "अ + अ बिना सन्धि के छपे हैं। सन्धि जाँची: तथा + उदर → तथोदर (आ + उ → ओ)।"),
    "100": ("गद्य; विश्वास निम्न। ‘धन्वनागमृत्तिका’ जैसा छपा वैसा, बिना विभाजन रखा: इसमें ‘मृत्तिका’ (मिट्टी) छिपी हो सकती है, "
            "पर विभाजन सुरक्षित नहीं, इसलिए अर्थ अस्पष्ट; इस पर प्रश्न नहीं। शाल्मली = सेमल (Bombax ceiba, मानक); ‘पिच्छा’ = "
            "उसका गोंद (सम्भावित)। ‘चुम्भल’ (छपा ‘चुंभल’) = गद्दी या लपेटा कपड़ा (सम्भावित; शायद चुम्बल का रूप)। षष्ठी रूप "
            "‘उत्तानायाः...’ ढीले ‘उसके विषय में’ अर्थ में। चुपड़ना हाथ और योनि का है (अभ्यज्य के कर्म)। सन्धि जाँची: अथ + "
            "उत्तानायाः → अथोत्तानायाः (अ + उ → ओ); उत्तानायाः + व्याभुग्न… → उत्तानाया व्याभुग्न… (आः + घोष → आ); "
            "व्याभुग्नसक्थ्याः + वस्त्र… → …सक्थ्या वस्त्र…; चुम्भल + उन्नमित → चुम्भलोन्नमित (अ + उ → ओ); …प्रदेशायाः + च → "
            "…प्रदेशायाश्च (विसर्ग + च → श्); घृतैः + अभ्यज्य → घृतैरभ्यज्य (ऐः + स्वर → ऐर्); गर्भम् + आहरेत् → गर्भमाहरेत्।"),
    "101": ("गद्य; विश्वास निम्न। इकाई अधूरी है: क्या काटा जाए, इसकी संज्ञा या क्रिया नहीं दी और जोड़ी नहीं गई। ‘छिन्नमेव’ का अर्थ "
            "अनिश्चित: ‘केवल काटना ही’ हो सकता है, या पाठ बिगड़ा हो (‘अच्छिन्नम्’ जैसा विकल्प स्वीकार नहीं किया गया)। "
            "‘सक्थिभ्याम् आगत’ = दोनों जाँघों से आया (प्रस्तुत)। लम्बा छपा रूप नियमित सन्धि से बिना पाठ-चिह्न के अलग किया गया। "
            "सन्धि जाँची: सक्थिभ्याम् + आगतस्य → सक्थिभ्यामागतस्य; आगतस्य + आनुलोम्यात् → आगतस्यानुलोम्यात् (अ + आ → आ); "
            "आनुलोम्यात् + छिन्नम् → आनुलोम्याच्छिन्नम् (त् + छ → च्छ); छिन्नम् + एव → छिन्नमेव।"),
    "102": ("गद्य; विश्वास निम्न; एक लम्बा वाक्य, कई दशाएँ, अन्त में एक क्रिया ‘निर्हरेत्’, कर्म नहीं दिया; ‘जिसका…’ = गर्भ, केवल "
            "संदर्भ से। पाठ-चिह्न (तीनों सम्भावित): (१) ‘सक्थ्यनी’ → ‘सक्थिनी’ (सक्थि नपुं. का द्विवचन; य अधिक); (२) ‘प्रसार्ये’ → "
            "‘प्रसार्य’ (ल्यबन्त; ए छपाई-भूल); (३) ‘वाऽपरादर्द्धम्’ → ‘वा अपरार्द्धम्’ (द अधिक; अपरार्ध = पिछला आधा, पूर्वार्ध के "
            "विपरीत)। इन पर प्रश्न नहीं। ‘अपत्यपथ’ = सन्तान का मार्ग, सम्भवतः जन्म-मार्ग (सम्भावित)। ‘प्रत्यार्जवम्’ = सीधेपन की ओर "
            "(भिन्न शब्द भी हो सकता है)। ‘र्द्ध’ = र्ध। आधुनिक तुल्य (सम्भावित, पाठ में नहीं): एक टाँग आगे, ब्रीच (स्फिग्देश), "
            "अनुप्रस्थ स्थिति (तिर्यक्), सिर बगल में मुड़ा, दोनों भुजाएँ आगे। सन्धि जाँची: प्रपन्नस्य + इतरम् → प्रपन्नस्येतरम् "
            "(अ + इ → ए); स्फिक् + देश → स्फिग्देश (क् + घोष → ग्); प्रनिपीड्य + ऊर्ध्वम् → प्रनिपीड्योर्ध्वम् (अ + ऊ → ओ); "
            "तिर्यक् + आगतस्य → तिर्यगागतस्य; शिरसः + अंसम् → शिरसोऽंसम् (अः + अ → ओऽ; छपा ‘शिरसोंऽसं’ में ओ पर अनुस्वार और "
            "‘उत्पीड्यांऽसौ’ का ऽ अंस से पहले छपाई की आदत); शिरः + अपत्यपथम् → शिरोऽपत्यपथम् (अः + अ → ओऽ); प्रपन्नस्य + ऊर्ध्वम् → "
            "प्रपन्नस्योर्ध्वम्।"),
    "103": ("गद्य; विश्वास मध्यम। पाठ-चिह्न: छपा ‘अभ्युग्न’ ज्ञात शब्द नहीं; सम्भावित पाठ ‘अभुग्न’ (मुड़ा हुआ), जो अगली इकाई "
            "(१०४) में आता है; इस शब्द पर प्रश्न नहीं। सापेक्ष वाक्य (यः…) पूरा है; डेटा के अनुसार इसका मुख्य वाक्य इकाई १०५ "
            "(‘तौ मूढौ’) में है, और वाक्य सम्भवतः इकाई १०४-१०५ तक चलता है। ‘प्रतिपद्यते’ = पहुँचता है, आता है। सन्धि जाँची: "
            "यः + तु → यस्तु (विसर्ग + त → स्); तु + अभ्युग्न… → त्वभ्युग्न… (उ + अ → व); शिरोभिः + योनिम् → शिरोभिर्योनिम् "
            "(इः + घोष → इर्)।"),
    "104": ("गद्य; विश्वास मध्यम। क्रिया नहीं: डेटा ‘प्रतिपद्यते’ को इकाई १०३ से आया मानता है और जोड़ता नहीं; डेटा के अनुसार "
            "पंक्ति सम्भवतः इकाई १०३ को आगे बढ़ाती है। पायु = गुदा (मानक)। छपा ‘यश्चाभुग्नएवैकेन’ = यः च अभुग्नः एव एकेन "
            "(नियमित सन्धि)। सन्धि जाँची: यः + च → यश्च (विसर्ग + च → श्); च + अभुग्नः → चाभुग्नः (अ + अ → आ); अभुग्नः + एव → "
            "अभुग्न एव (अः + अ से भिन्न स्वर → अ, विसर्ग लुप्त, अन्तर रहता है); एव + एकेन → एवैकेन (अ + ए → ऐ); अन्त के ‘योनिं’, "
            "‘पायुं’ में म् का अनुस्वार (छपाई)।"),
    "105": ("गद्य; विश्वास मध्यम। ‘इति’ कारण-वाक्य को बन्द करता है (यह सोचकर कि हाथ से नहीं निकाले जा सकते)। ‘अशक्यौ आहर्तुम्’: "
            "निकाले जाने में असम्भव (तुमुन् कर्मवाच्य अर्थ में)। ‘तौ’ = इकाई १०३ और १०४ की दो दशाएँ: डेटा का पठन, पंक्ति स्पष्ट "
            "शब्दों में नहीं कहती। ‘मूढ’ = अटका हुआ (पारिभाषिक)। सन्धि जाँची: हस्तेन + आहर्तुम् → हस्तेनाहर्तुम् (अ + आ → आ); "
            "आहर्तुम् + अशक्यौ → आहर्तुमशक्यौ; अशक्यौ + इति → अशक्याविति (औ + स्वर → आव्); शस्त्रम् + अवचारयेत् → "
            "शस्त्रमवचारयेत्।"),
    "106": ("गद्य; विश्वास मध्यम। पाठ-चिह्न: छपे ‘तालुक्युरसि’ में ‘तालुकि’ कोई रूप नहीं (तालु नपुं., सप्तमी ‘तालुनि’); सम्भावित पाठ "
            "‘तालुन्युरसि’ (नि को कि पढ़ा गया); तालु पर प्रश्न नहीं। ‘विदार्य’ और ‘अपहरेत्’ के कर्म नहीं दिए (संदर्भ से सिर या गर्भ)। "
            "शंकु ठोड़ी, तालु, छाती या काँख पर पकड़ता है, या गर्भ उनसे खींचा जाता है, शब्दों से तय नहीं; पहला पठन सरल है। मण्डलाग्र "
            "(गोल नोक वाला शस्त्र) और अंगुलिशस्त्र (उँगली का शस्त्र) के अर्थ सम्भावित। छपा ‘अथस्त्रियम्’ = अथ स्त्रियम् (केवल अन्तराल "
            "छूटा)। सन्धि जाँची: स्त्रियम् + आश्वास्य → स्त्रियमाश्वास्य; मण्डल + अग्र → मण्डलाग्र (अ + अ → आ); मण्डलाग्रेण + "
            "अङ्गुलि… → मण्डलाग्रेणाङ्गुलि… (अ + अ → आ); कपालानि + आहृत्य → कपालान्याहृत्य (इ + आ → या); वा + अपहरेत् → "
            "वापहरेत् (आ + अ → आ; छपा ‘वाऽपहरेत्’ का ऽ छपाई की आदत)।"),
    "107": ("गद्य; विश्वास मध्यम। क्रिया नहीं: शंकु से पकड़ना और खींचना डेटा इकाई १०६ से आया मानता है, जोड़ता नहीं; डेटा: सम्भवतः "
            "इकाई १०६ को आगे बढ़ाती है। ‘अभिन्नशिरसम्’ के बाद की संज्ञा (गर्भ) संदर्भ से। अक्षिकूट = आँख के क्षेत्र का उभार या "
            "किनारा, सम्भवतः आँख के गड्ढे का किनारा (ठीक अंग पक्का नहीं)। गण्ड = गाल (कनपटी भी हो सकता है)। छपा ‘वाऽक्षिकूटे’ = "
            "वा + अक्षिकूटे (आ + अ → आ; ऽ छपाई की आदत)। ‘गंडे’ = गण्डे।"),
    "108": ("गद्य; विश्वास मध्यम। ‘छित्वा’ आदि और ‘आहरेत्’ के कर्म नहीं दिए; संदर्भ से गर्भ। ‘दृतेरिव आध्मातस्य’: दृति = चमड़े की "
            "मशक या धौंकनी; ‘दृतेः’ षष्ठी या पंचमी, यहाँ ढीले ‘की तरह’ अर्थ में (इस पर प्रश्न नहीं)। ‘वातपूर्ण’ = हवा से भरा। छपा "
            "‘छित्वा’ = छित्त्वा (वर्तनी-भेद)। ‘तथाऽंस…’ में ऽ अंस से पहले छपाई की आदत। सन्धि जाँची: तथा + अंस… → तथांस… "
            "(आ + अ → आ); …संसक्तस्य + अंसदेशे → …संसक्तस्यांसदेशे (अ + अ → आ); दृतेः + इव → दृतेरिव (एः + स्वर → एर्); इव + "
            "आध्मातस्य → इवाध्मातस्य (अ + आ → आ); उदरम् + अवदार्य → उदरमवदार्य; निरस्य + अन्त्राणि → निरस्यान्त्राणि (अ + अ → आ); "
            "शिथिलीभूतम् + आहरेत् → शिथिलीभूतमाहरेत्।"),
}


# ===================================================================== AIDS
AIDS = {
    "95": {
        "contrast": "एके (कुछ लोग कहते हैं): अनुभवी शल्यहर्ता शल्य निकाले ↔ तत्त्वतः (वास्तव में): शस्त्रकर्म सबसे कठिन है।",
        "chunks": "दृष्टकर्मणा | शल्यहर्त्रा | शल्याहरणमित्येके || तत्त्वतः | कष्टतममस्ति | शस्त्रकर्म",
        "sandhi": "अ + आ → आ: शल्य + आहरणम् → शल्याहरणम् · इ + ए → ये: इति + एके → इत्येके · स्वर से पहले म्: "
                  "कष्टतमम् + अस्ति → कष्टतममस्ति।",
    },
    "96": {
        "diagram": {"groups": [
            {"label": "किनके बीच (क्रम से)", "items": ["योनि", "यकृत्", "प्लीहा", "अन्त्र (आँतें)", "गर्भाशय", "आदि"]},
            {"label": "एक हाथ से (क्रम से)", "items": ["१ उत्कर्षण: ऊपर खींचना", "२ अपकर्षण: नीचे खींचना",
                                                   "३ व्यावर्तन: घुमाना", "४ उत्कर्तन: काटकर निकालना",
                                                   "५ छेदन: काटना", "६ भेदन: चीरना", "७ पीडन: दबाना",
                                                   "८ ऋजूकरण: सीधा करना"]}]},
        "chunks": "यतो | योनियकृत्प्लीहान्त्रगर्भाशयादीनां मध्ये | ताननुपहिंसताऽस्पर्शयता | शस्त्रमवधार्यम् (?) | "
                  "उत्कर्षणापकर्षणव्यावर्त्तनोत्कर्त्तनच्छेदनभेदनपीडनर्जूकरणानि | चैकेन पाणिना कार्याणि",
        "sandhi": "अः + घोष → ओ: यतः + योनि → यतो योनि · अ + ऋ → अर्: पीडन + ऋजूकरणानि → पीडनर्जूकरणानि · अ + ए → ऐ: "
                  "च + एकेन → चैकेन।",
    },
    "97": {
        "frame": "क्यों: तस्मात् (इसलिए) → पहले: ईश्वरम् आपृच्छ्य (स्वामी से पूछकर) → कैसे: परं यत्नम् आस्थाय (परम प्रयत्न से) → "
                 "किनके साथ: तद्विद्यसहितः (जानकारों सहित) → क्रिया: तम् उपक्रमेत् (उसका उपक्रम करे)।",
        "chunks": "तस्मादीश्वरमापृच्छ्य | परं च यत्नमास्थाय | तद्विद्यसहितः | तमुपक्रमेत्",
        "sandhi": "त् + स्वर → द्: तस्मात् + ईश्वरम् → तस्मादीश्वरम् · त् + घोष → द्: तत् + विद्य → तद्विद्य · विसर्ग + त → "
                  "स्: सहितः + तम् → सहितस्तम्।",
    },
    "98": {
        "chunks": "अक्रियायां | ध्रुवं | मरणं",
        "anchors": "याद-सूत्र: ‘अ-क्रिया’ = कुछ न करना; ‘ध्रुव’ तारे की तरह अटल: मृत्यु पक्की। (मेरी याद-पद्धति)",
    },
    "99": {
        "chunks": "तथा | उदर | अश्मरी | प्रभृतीना(म्) | अपि",
        "sandhi": "आ + उ → ओ: तथा + उदर → तथोदर · छपे ‘उदरअश्मरी’ में अ + अ बिना सन्धि।",
        "frame": "तथा (वैसे ही) → किनका: उदर (पेट का रोग, सम्भवतः जलोदर जैसा), अश्मरी (पथरी), प्रभृति (आदि) → अपि (भी) → "
                 "क्या कहा: नहीं दिया।",
    },
    "100": {
        "chain": {"steps": ["स्त्री उत्तान (चित) लेटी", "जाँघें मुड़ी हुईं", "कटि-प्रदेश वस्त्र-चुम्भल से उठा (सम्भवतः गद्दी)",
                            "हाथ और योनि चुपड़ना: धन्वनागमृत्तिका (अस्पष्ट), शाल्मली-पिच्छा, घी",
                            "गर्भ को निकाले"]},
        "chunks": "अथोत्तानाया | व्याभुग्नसक्थ्या | वस्त्रचुंभलोन्नमितकटिप्रदेशायाश्च | धन्वनागमृत्तिका (?) शाल्मलीपिच्छाघृतैरभ्यज्य | "
                  "हस्तं योनिंच | गर्भमाहरेत्",
        "sandhi": "अ + उ → ओ: अथ + उत्तानायाः → अथोत्तानायाः · आः + घोष → आ: उत्तानायाः + व्याभुग्न… → उत्तानाया व्याभुग्न… · "
                  "ऐः + स्वर → ऐर्: घृतैः + अभ्यज्य → घृतैरभ्यज्य।",
    },
    "101": {
        "chunks": "तत्र | सक्थिभ्यामागतस्य | आनुलोम्यात् | छिन्नमेव (?)",
        "sandhi": "अ + आ → आ: आगतस्य + आनुलोम्यात् → आगतस्यानुलोम्यात् · त् + छ → च्छ: आनुलोम्यात् + छिन्नम् → "
                  "आनुलोम्याच्छिन्नम् (डेटा का पठन; ‘अच्छिन्नम्’ जैसा विकल्प भी सम्भव)।",
        "frame": "कहाँ: तत्र → किसका: सक्थिभ्याम् आगतस्य (दोनों जाँघों से आया) → क्यों: आनुलोम्यात् (स्वाभाविक दिशा के कारण) → "
                 "छिन्नम् एव: अर्थ अनिश्चित, संज्ञा-क्रिया नहीं।",
    },
    "102": {
        "diagram": {"groups": [
            {"label": "दशा (क्रम से)", "items": ["१ एक जाँघ आगे", "२ नितम्ब-प्रदेश से आया", "३ तिरछा आया",
                                               "४ सिर बगल में मुड़ा", "५ दोनों भुजाएँ आगे"]},
            {"label": "उपाय (उसी क्रम से)", "items": ["१ दूसरी जाँघ फैलाकर", "२ दबाकर, ऊपर उठाकर, जाँघें फैलाकर",
                                                    "३ घुमाकर; या पिछला आधा उठाकर (सुधारा पाठ)",
                                                    "४ कन्धा दबाकर, उठाकर, सिर मार्ग में लाकर",
                                                    "५ दोनों कन्धे ऊपर दबाकर, सिर की जड़ लाकर"]},
            {"label": "अन्त में", "items": ["निर्हरेत्: निकाले"]}]},
        "chunks": "एकस्मिन् सक्थ्नि प्रपन्नस्येतरं सक्थि प्रसार्य | स्फिग्देशागतस्य स्फिग्देशंप्रनिपीड्योर्ध्वमुत्क्षिप्य सक्थ्यनी प्रसार्ये | "
                  "तिर्यगागतस्य परिवर्त्य वाऽपरादर्द्धमुत्क्षिप्य पूर्वार्द्धमपत्यपथं प्रत्यार्जवमानीय | "
                  "पार्श्ववृत्तशिरसोंऽसं प्रतिपीड्योर्ध्वमुत्क्षिप्य शिरोऽपत्यपथमानीय | "
                  "बाहुद्वयं प्रपन्नस्योर्ध्वमुत्पीड्यांऽसौ शिरोमूलमानीय | निर्हरेत्",
        "sandhi": "अ + इ → ए: प्रपन्नस्य + इतरम् → प्रपन्नस्येतरम् · अ + ऊ → ओ: प्रनिपीड्य + ऊर्ध्वम् → प्रनिपीड्योर्ध्वम् · "
                  "क् + घोष → ग्: तिर्यक् + आगतस्य → तिर्यगागतस्य · अः + अ → ओऽ: शिरः + अपत्यपथम् → शिरोऽपत्यपथम्।",
    },
    "103": {
        "chunks": "यस्त्वभ्युग्नमध्यः (= अभुग्नमध्यः?) | पाणिपादशिरोभिर्योनिं | प्रतिपद्यते",
        "sandhi": "विसर्ग + त → स्: यः + तु → यस्तु · उ + अ → व: तु + अ… → त्व… · इः + घोष → इर्: शिरोभिः + योनिम् → "
                  "शिरोभिर्योनिम्।",
        "frame": "कौन: यः तु (पर जो) → कैसा: मध्य मुड़ा (सम्भावित पाठ) → किससे: पाणि-पाद-शिरोभिः (हाथ, पैर, सिर से) → कहाँ: "
                 "योनिम् → क्रिया: प्रतिपद्यते (आता है)। मुख्य वाक्य: डेटा के अनुसार इकाई १०५।",
    },
    "104": {
        "chunks": "यश्चाभुग्नएवैकेन | पादेन योनिं | द्वितीयेन पायुं",
        "sandhi": "विसर्ग + च → श्: यः + च → यश्च · अः + अ से भिन्न स्वर → अ (अन्तर रहता है): अभुग्नः + एव → अभुग्न एव · "
                  "अ + ए → ऐ: एव + एकेन → एवैकेन।",
        "seesaw": "एकेन पादेन → योनिम् ↔ द्वितीयेन (पादेन) → पायुम्: एक पैर आगे के मार्ग में, दूसरा पीछे के।",
    },
    "105": {
        "chain": {"steps": ["तौ मूढौ: वे दोनों अटके", "हस्तेन आहर्तुम् अशक्यौ: हाथ से निकालना असम्भव",
                            "इति: यह सोचकर", "शस्त्रम् अवचारयेत्: शस्त्र का प्रयोग करे"]},
        "chunks": "तौ मूढौ | हस्तेनाहर्तुमशक्याविति | शस्त्रमवचारयेत्",
        "sandhi": "अ + आ → आ: हस्तेन + आहर्तुम् → हस्तेनाहर्तुम् · औ + स्वर → आव्: अशक्यौ + इति → अशक्याविति।",
    },
    "106": {
        "chain": {"steps": ["स्त्री को आश्वस्त करके", "मण्डलाग्र या अंगुलिशस्त्र से चीरकर",
                            "सिर की खोपड़ी के टुकड़े निकालकर",
                            "शंकु से पकड़कर: ठोड़ी, तालु (सुधारा पाठ), छाती या काँख", "हटा ले (अपहरेत्)"]},
        "chunks": "अथस्त्रियमाश्वास्य | मंडलाग्रेणांगुलिशस्त्रेण वा विदार्य | शिरःकपालान्याहृत्य | शंकुना गृहीत्वा | "
                  "चुबुके तालुक्युरसि (= तालुन्युरसि?) | कक्षायां वाऽपहरेत्",
        "sandhi": "अ + अ → आ: मण्डल + अग्र → मण्डलाग्र · इ + आ → या: कपालानि + आहृत्य → कपालान्याहृत्य · आ + अ → आ: "
                  "वा + अपहरेत् → वापहरेत् (छपा ‘वाऽपहरेत्’)।",
    },
    "107": {
        "chunks": "अभिन्नशिरसं | वाऽक्षिकूटे | गंडे वा",
        "frame": "किसका: अभिन्नशिरसम् (जिसका सिर न फटा) → कहाँ: अक्षिकूटे (सम्भवतः आँख के गड्ढे का किनारा) या गण्डे (गाल) → "
                 "क्रिया: छपी नहीं।",
        "anchors": "याद-सूत्र: सिर फटा हो तो खोपड़ी के टुकड़े निकलते हैं; न फटा हो (अ-भिन्न) तो पकड़ आँख के किनारे या गाल पर। "
                   "(मेरी याद-पद्धति)",
    },
    "108": {
        "diagram": {"groups": [
            {"label": "कन्धे में अटका (अंससंसक्त)", "items": ["कन्धे के स्थान पर भुजा काटकर"]},
            {"label": "मशक-सा फूला (दृतेरिव आध्मात)", "items": ["१ वायु-भरा पेट चीरकर", "२ आँतें निकालकर",
                                                           "३ ढीला होने पर निकाले"]}]},
        "chunks": "तथाऽंससंसक्तस्यांसदेशे | बाहुं छित्वा | दृतेरिवाध्मातस्य | वातपूर्णमुदरमवदार्य | निरस्यांत्राणि | "
                  "शिथिलीभूतमाहरेत्",
        "sandhi": "एः + स्वर → एर्: दृतेः + इव → दृतेरिव · अ + आ → आ: इव + आध्मातस्य → इवाध्मातस्य · अ + अ → आ: "
                  "निरस्य + अन्त्राणि → निरस्यान्त्राणि।",
    },
}


# ===================================================================== IMAGE_SPECS
IMAGE_SPECS = {
    ("95", "contrast"): {
        "file": "sh4-shastrakarma-95.svg",
        "alt": ("Two columns of unit 95: 'some say' (eke): an experienced śalya-remover extracts the śalya; 'in truth' "
                "(tattvataḥ): śastrakarma, work with the cutting instrument, is the most difficult."),
        "type": "split",
        "title": "इकाई ९५: एक मत और तत्त्व",
        "cols": [["एके (कुछ लोग कहते हैं)", ["अनुभवी शल्यहर्ता", "शल्य का आहरण करे"]],
                 ["तत्त्वतः (वास्तव में)", ["शस्त्रकर्म", "सबसे कठिन है"]]],
    },
    ("96", "diagram"): {
        "file": "sh4-ekapani-karma-96.svg",
        "alt": ("Two columns of unit 96. Among (in line order): yoni, liver, spleen, intestines, womb, and the like. With one "
                "hand, eight operations numbered in line order: pulling up, pulling down, turning round, cutting out, "
                "cutting through, splitting, pressing, straightening."),
        "type": "split",
        "title": "इकाई ९६: अंगों के बीच, एक हाथ से",
        "cols": [["किनके बीच (क्रम से)", ["योनि", "यकृत्", "प्लीहा", "अन्त्र (आँतें)", "गर्भाशय", "आदि"]],
                 ["एक हाथ से (क्रम से)", ["१ ऊपर खींचना", "२ नीचे खींचना", "३ घुमाना", "४ काटकर निकालना",
                                          "५ काटना", "६ चीरना", "७ दबाना", "८ सीधा करना"]]],
    },
    ("100", "chain"): {
        "file": "sh4-mudhagarbha-aharana-100.svg",
        "alt": ("Chain of unit 100: the woman lies face up; thighs bent; hip region raised by a cloth cumbhala (probably a "
                "pad); hand and yoni anointed with dhanvanāgamṛttikā (unclear), śālmalī-picchā and ghee; extract the fetus."),
        "type": "chain",
        "title": "इकाई १००: लिटाना, चुपड़ना, निकालना",
        "steps": ["स्त्री उत्तान (चित) लेटी", "जाँघें मुड़ी हुईं", "कटि वस्त्र-चुम्भल से उठी (सम्भवतः गद्दी)",
                  "हाथ और योनि चुपड़ें: धन्वनागमृत्तिका (अस्पष्ट), शाल्मली-पिच्छा, घी", "गर्भ को निकाले"],
    },
    ("102", "diagram"): {
        "file": "sh4-pancha-sanga-102.svg",
        "alt": ("Table of unit 102, five presentations in line order with their handling: one thigh presented, stretch out "
                "the other thigh; come at the buttock region, press it down, lift upward, stretch the thighs; come "
                "transversely, turn round, or lift the hind half (corrected reading); head turned to the side, press the "
                "shoulder, lift, bring the head to the passage; both arms presented, press both shoulders up, bring the base "
                "of the head. Then draw out."),
        "type": "table",
        "title": "इकाई १०२: पाँच दशाएँ, फिर निर्हरेत्",
        "heads": ["दशा (क्रम से)", "उपाय"],
        "rows": [["१ एक जाँघ आगे", "दूसरी जाँघ फैलाकर"],
                 ["२ नितम्ब-प्रदेश से आया", "दबाकर, ऊपर उठाकर, जाँघें फैलाकर"],
                 ["३ तिरछा आया", "घुमाकर; या पिछला आधा उठाकर (सुधारा पाठ)"],
                 ["४ सिर बगल में मुड़ा", "कन्धा दबाकर, उठाकर, सिर मार्ग में लाकर"],
                 ["५ दोनों भुजाएँ आगे", "दोनों कन्धे ऊपर दबाकर, सिर की जड़ लाकर"],
                 ["अन्त में", "निर्हरेत्: निकाले"]],
    },
    ("105", "chain"): {
        "file": "sh4-mudhau-shastra-105.svg",
        "alt": ("Flowchart of unit 105: those two, stuck (mūḍha); cannot be extracted by the hand; thus (iti); one should "
                "apply the instrument (śastra)."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"वे दोनों मूढ (अटके)\"] --> B[\"हाथ से निकालना असम्भव\"]\n"
                 "  B --> C[\"इति: यह सोचकर\"]\n"
                 "  C --> D[\"शस्त्र का प्रयोग करे\"]\n"),
    },
    ("106", "chain"): {
        "file": "sh4-shanku-apaharana-106.svg",
        "alt": ("Chain of unit 106 in line order: comfort the woman; split open with a maṇḍalāgra or aṅguliśastra (probable "
                "identifications); remove the skull pieces; seize with a hook at the chin, palate (corrected reading), chest "
                "or armpit; draw away."),
        "type": "chain",
        "title": "इकाई १०६: क्रम से",
        "steps": ["स्त्री को आश्वस्त करके", "मण्डलाग्र या अंगुलिशस्त्र से चीरकर", "खोपड़ी के टुकड़े निकालकर",
                  "शंकु से पकड़कर: ठोड़ी, तालु (सुधारा पाठ), छाती या काँख", "हटा ले"],
    },
    ("108", "diagram"): {
        "file": "sh4-amsa-dritivat-108.svg",
        "alt": ("Two columns of unit 108: stuck at the shoulder, cut off the arm at the shoulder region; swollen like a "
                "skin-bag, in order: split open the wind-filled belly, cast out the intestines, extract when slack."),
        "type": "split",
        "title": "इकाई १०८: दो दशाएँ",
        "cols": [["कन्धे में अटका", ["कन्धे के स्थान पर", "भुजा काटकर"]],
                 ["मशक-सा फूला", ["१ वायु-भरा पेट चीरकर", "२ आँतें निकालकर", "३ ढीला होने पर निकाले"]]],
    },
}
