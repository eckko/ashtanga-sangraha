from helpers import mcq, match, order, fill, multi, accepts


def T(q, teaches):
    q["teaches"] = teaches
    return q


AUTHORED = {}

# ---------------------------------------------------------------- unit 26
AUTHORED["26"] = {
    "title": "उभयलक्षणसंकरे तु संसर्गकृतिः",
    "question": "By unit 26, what is the combined constitution, and who has the equal-doṣa constitution?",
    "rule": ("When the marks of both are mixed (उभयलक्षणसंकरे), it is the one made by combination (संसर्गकृतिः); one "
             "endowed with all the qualities (सर्वगुणसमुदितः) is of equal-doṣa constitution (समदोषप्रकृतिः)."),
    "limits": ("Prose, two printed lines joined, no verb. The noun prakṛti is not printed with संसर्गकृतिः. 'Both' = two "
               "of the three doṣas, and 'all the qualities' = the marks of all three doṣas together (not 'all good "
               "qualities'): both are the data's readings, and no question asks what they cover."),
    "explain_hi": ("यह इकाई कफ-प्रकृति के बाद बाकी प्रकृतियों को बताती है; दो छपी पंक्तियाँ जोड़ी गई हैं। "
                   "जब दोनों के लक्षण मिल जाएँ (उभयलक्षणसंकरे), तब संसर्ग से बनी प्रकृति (संसर्गकृतिः) होती है; ‘दोनों’ यानी तीन में से दो दोष, यह डेटा की व्याख्या है। "
                   "जो सब गुणों से युक्त हो (सर्वगुणसमुदितः), वह समदोष-प्रकृति वाला है, यानी तीनों दोष सम। "
                   "‘सब गुण’ का अर्थ यहाँ तीनों दोषों के लक्षण एक साथ है, ‘सब अच्छे गुण’ नहीं। "
                   "पंक्तियों में कोई क्रिया नहीं; ‘होता है’ समझा जाता है।"),
    "hook": "दो के लक्षण मिलें तो संसर्ग; सबके गुण हों तो समदोष।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In उभयलक्षणसंकरे of unit 26, what does संकर mean?",
            ("Mixture", "संकर = mixture: उभय-लक्षण-संकरे, when the marks of both are mixed."),
            [("Absence", "Absence would be अभाव; संकर is a mixing."),
             ("Division", "Division would be विभाग or भेद; संकर is a mixing."),
             ("Increase", "Increase would be वृद्धि; संकर is a mixing.")],
            "उभय (both) + लक्षण (mark) + संकर (mixture).",
            "संकर = mixture."),
        order(1, "Put the words of unit 26 in the printed order.",
              ["उभयलक्षणसंकरे", "तु", "संसर्गकृतिः", "सर्वगुणसमुदितः", "समदोषप्रकृतिः"],
              "When the marks of both are mixed; but; the one made by combination; endowed with all the qualities; of equal-doṣa constitution.",
              "उभयलक्षणसंकरे → तु → संसर्गकृतिः → सर्वगुणसमुदितः → समदोषप्रकृतिः."),
        match(2, "Match each word of unit 26 to its meaning.",
              [["उभय", "both"], ["लक्षण", "mark"], ["संसर्ग", "combination"], ["समुदित", "endowed with"],
               ["सम", "equal"]],
              "उभय = both, लक्षण = mark, संसर्ग = combination, समुदित = endowed with, सम = equal.",
              "उभय, लक्षण, संसर्ग, समुदित, सम.", role="extend",
              teaches="समदोषप्रकृतिः is a bahuvrīhi: one whose constitution is of equal doṣas."),
        mcq("discriminate", 3, "By unit 26, which constitution belongs to one endowed with all the qualities?",
            ("समदोषप्रकृतिः, the equal-doṣa one", "सर्वगुणसमुदितः समदोषप्रकृतिः: all the qualities → equal doṣas."),
            [("संसर्गकृतिः, the combined one", "संसर्गकृतिः is named for the mixing of the marks of both, not of all."),
             ("वातप्रकृतिः, the Vāta one", "The Vāta constitution has the marks of one doṣa, not all the qualities."),
             ("कफप्रकृतिः, the Kapha one", "The Kapha constitution has the marks of one doṣa, not all the qualities.")],
            "All the qualities together: samadoṣaprakṛti.",
            "सर्वगुणसमुदितः → समदोषप्रकृतिः."),
        mcq("apply", 4, "By unit 26, when is the constitution called संसर्गकृतिः?",
            ("When the marks of both are mixed", "उभयलक्षणसंकरे तु संसर्गकृतिः: the marks of both mixed."),
            [("When no mark at all is seen", "The line names a mixing of marks, not their absence."),
             ("When one doṣa's marks stand alone", "One doṣa alone gives a single-doṣa constitution, not saṃsarga."),
             ("When the marks change by season", "The line says nothing about seasons changing the marks.")],
            "Mixed marks of both → the combined constitution.",
            "उभयलक्षणसंकरे → संसर्गकृतिः."),
        mcq("transfer", 5, "By the pattern of उभयलक्षणसंकरे (when the marks of both are mixed), what does दोषसंकरे mean in a new example?",
            ("When the doṣas are mixed", "-ए here is the locative of the circumstance: when there is a mixing of doṣas."),
            [("Of a mixing of the doṣas", "'Of' would need the genitive दोषसंकरस्य."),
             ("From a mixing of doṣas", "'From' would need the ablative दोषसंकरात्."),
             ("The mixing, as subject", "The subject would be the nominative दोषसंकरः.")],
            "दोषसंकरे = when the doṣas are mixed, like उभयलक्षणसंकरे.",
            "Locative -ए = 'when / in the case of'.",
            teaches="A locative such as उभयलक्षणसंकरे can state the circumstance: 'when there is a mixing of the marks of both'."),
    ],
}

# ---------------------------------------------------------------- unit 27
AUTHORED["27"] = {
    "title": "तत्राद्यास्त्रयो नित्यातुराः",
    "question": "By unit 27, which constitutions are always ailing, and which part of the reason is unreadable?",
    "rule": ("Among these (तत्र), the first three (आद्याः त्रयः) are always ailing (नित्यातुराः). The reason follows in "
             "one long word that is damaged in print."),
    "limits": ("Low confidence. The last word दोषानुप्रशयितप्रकृतित्वात् is unclear; the suggested anuśayita is a guess: "
               "no question on the reason. 'The first three' = the three single-doṣa constitutions (data's reading); "
               "the noun is not printed and, by the masculine forms, means persons. Unit 28 adds the dual ones."),
    "explain_hi": ("उनमें पहले तीन (आद्याः त्रयः) सदा रोगी रहने वाले (नित्यातुराः) हैं। "
                   "डेटा के अनुसार ‘पहले तीन’ यानी एक-एक दोष वाली तीन प्रकृतियाँ; संज्ञा छपी नहीं, और पुल्लिंग रूप उन प्रकृतियों वाले व्यक्तियों की ओर संकेत करते हैं। "
                   "कारण बताने वाला अन्तिम शब्द ‘दोषानुप्रशयितप्रकृतित्वात्’ अस्पष्ट है; ‘अनुशयित’ (चिपका हुआ) सुझाव केवल अनुमान है, इसलिए कारण पर कोई प्रश्न नहीं। "
                   "‘तत्राद्यास्त्रयो’ में तत्र + आद्याः (अ + आ → आ), आद्याः + त्रयः (त से पहले विसर्ग → स्) और त्रयः + नित्य (घोष व्यंजन से पहले अः → ओ) की सन्धियाँ हैं। "
                   "अगली इकाई २८ ‘विशेषतः द्वन्द्व प्रकृतियाँ’ जोड़ती है।"),
    "hook": "पहली तीन प्रकृतियाँ: नित्य आतुर।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 27, what does नित्यातुर mean?",
            ("Always ailing", "नित्य (always) + आतुर (ailing): नित्यातुराः."),
            [("Never ailing", "नित्य means always, not never."),
             ("Quickly healed", "आतुर means ailing, not healed."),
             ("Ill in old age", "नित्य means always, not only in old age.")],
            "नित्य = always, आतुर = ailing.",
            "नित्यातुर = always ailing."),
        order(1, "Put the sure words of unit 27 in the printed order.",
              ["तत्र", "आद्याः", "त्रयः", "नित्यातुराः"],
              "Among these; the first; three; always ailing.",
              "तत्र → आद्याः → त्रयः → नित्यातुराः."),
        match(2, "Match each sure word of unit 27 to its meaning.",
              [["तत्र", "among these"], ["आद्य", "first"], ["त्रयः", "three"], ["नित्य", "always"],
               ["आतुर", "ailing, ill"]],
              "तत्र = among these, आद्याः त्रयः = the first three, नित्य-आतुराः = always ailing.",
              "तत्र, आद्य, त्रयः, नित्य, आतुर.", role="extend",
              teaches="आद्याः त्रयः (the first three) are masculine plural: the unprinted noun means persons of those types."),
        mcq("discriminate", 3, "Which split of तत्राद्यास्त्रयो in unit 27 is right?",
            ("तत्र + आद्याः + त्रयः", "अ + आ → आ; आः before त → आस्; अः before the voiced न → ओ."),
            [("तत्र + आद्याः + स्त्रयः", "स्त्रयः is not a word; the स् comes from the visarga of आद्याः."),
             ("तत्रा + आद्याः + त्रयः", "तत्रा is not a word; the adverb is तत्र."),
             ("तत् + राद्याः + त्रयः", "राद्याः is not a word; तत्र is one adverb.")],
            "तत्र (among these) + आद्याः (the first) + त्रयः (three).",
            "अ + आ → आ; ः before त → स्."),
        mcq("apply", 4, "Why is त्रयः printed त्रयो before नित्यातुराः in unit 27?",
            ("अः before a voiced consonant → ओ", "न is a voiced consonant: त्रयः + नित्यातुराः → त्रयो नित्यातुराः."),
            [("आः before a voiced consonant → ओ", "आः drops its visarga before a voiced sound; it does not give ओ."),
             ("Every visarga before न → ओ", "Not every: after इ or उ the visarga gives र् before न."),
             ("ओ is the numeral's own ending", "त्रयः is the nominative plural; ओ comes only from sandhi.")],
            "त्रयः + नित्यातुराः: अः before the voiced consonant न → ओ.",
            "अः + voiced consonant → ओ."),
        mcq("transfer", 5, "By the pattern of आद्याः + त्रयः → आद्यास्त्रयः, how is बालाः + तिष्ठन्ति (the boys stand) joined in a new example?",
            ("बालास्तिष्ठन्ति", "Visarga before त becomes स्: बालाः + तिष्ठन्ति → बालास्तिष्ठन्ति."),
            [("बाला तिष्ठन्ति", "आः drops its visarga only before a voiced sound; त is voiceless."),
             ("बालाश्तिष्ठन्ति", "श् comes before च, छ or श, not before त."),
             ("बालार्तिष्ठन्ति", "र् comes from a visarga after a vowel other than अ/आ, not here.")],
            "बालाः + तिष्ठन्ति = बालास्तिष्ठन्ति, like आद्याः + त्रयः = आद्यास्त्रयः.",
            "ः + त → स्त.",
            teaches="A visarga before त or थ becomes स्: आद्याः + त्रयः → आद्यास्त्रयः."),
    ],
}

# ---------------------------------------------------------------- unit 28
AUTHORED["28"] = {
    "title": "विशेषतश्च द्वंद्वप्रकृतयः",
    "question": "By unit 28, which constitutions does the text add with 'especially', and what is understood?",
    "rule": ("And especially (विशेषतः च) those of dual constitution (द्वन्द्वप्रकृतयः). The line prints no predicate; "
             "'always ailing' is carried over from unit 27."),
    "limits": ("Prose, elliptical: no predicate printed; 'always ailing' is understood from unit 27, not stated here. "
               "द्वन्द्व = the pair of doṣas combined (data's note). The gram label says f., while unit 27's note takes "
               "the unprinted noun as masculine persons: no question rests on the gender."),
    "explain_hi": ("यह इकाई बहुत छोटी है: ‘और विशेष रूप से द्वन्द्व प्रकृति वाले’। "
                   "विधेय ‘सदा रोगी’ इकाई २७ से आता है; यहाँ कोई विधेय छपा नहीं। "
                   "द्वन्द्व यानी दो दोषों का जोड़ा जो मिला हुआ हो। "
                   "‘विशेषतश्च’ में विशेषतः + च है: च से पहले विसर्ग श् बनता है।"),
    "hook": "विशेषतश्च: दो-दोष वाले और भी अधिक।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 28, what does विशेषतः mean?",
            ("Especially", "विशेषतः = especially, in particular."),
            [("Occasionally", "Occasionally would be कदाचित्; विशेषतः = especially."),
             ("In general", "In general would be सामान्यतः; विशेषतः is its opposite."),
             ("Never at all", "Never would be न कदापि; विशेषतः = especially.")],
            "विशेषतः = especially.",
            "विशेषतः = especially."),
        match(1, "Match each word of unit 28 to its meaning.",
              [["विशेषतः", "especially"], ["च", "and"], ["द्वन्द्व", "pair"], ["प्रकृति", "constitution"]],
              "विशेषतः = especially, च = and, द्वन्द्व = pair, प्रकृति = constitution.",
              "विशेषतः, च, द्वन्द्व, प्रकृति."),
        T(multi("extend", 2, "Which statements fit unit 28?",
                [("It names the single-doṣa constitutions", "Those are the first three of unit 27, not this line."),
                 ("The line itself prints no predicate", "Right: 'always ailing' is understood from unit 27."),
                 ("द्वन्द्व here is a pair of doṣas combined", "Right: dual constitution = two doṣas together."),
                 ("It says the dual ones are never ill", "No: the predicate carried over is 'always ailing'.")],
                [1, 2],
                "No predicate is printed; the dual constitutions are added 'especially'.",
                "विशेषतश्च द्वंद्वप्रकृतयः (+ नित्यातुराः understood)."),
          "An elliptical line takes its predicate from the line before: here 'always ailing' from unit 27."),
        mcq("discriminate", 3, "Which split of विशेषतश्च in unit 28 is right?",
            ("विशेषतः + च", "Visarga before च → श्: विशेषतः + च → विशेषतश्च."),
            [("विशेषत + श्च", "श्च is not a word; the श् comes from the visarga."),
             ("विशेष + तश्च", "तश्च is not a word; विशेषतः is one adverb."),
             ("विशेषतर् + च", "र् does not become श्; the word ends in a visarga.")],
            "विशेषतः (especially) + च (and).",
            "ः + च → श्च."),
        mcq("apply", 4, "Why is विशेषतः printed विशेषतश् before च in unit 28?",
            ("Visarga before च becomes श्", "च is a palatal: a visarga before च or छ becomes श्."),
            [("Visarga before any consonant → श्", "Not any: before त it becomes स् (आद्यास्त्रयो, unit 27)."),
             ("श् is part of the stem विशेषतश्", "The adverb is विशेषतः; the श् comes only from sandhi."),
             ("Visarga before च is dropped", "It is not dropped: it becomes श्, as printed.")],
            "विशेषतः + च: visarga before च → श्.",
            "ः + च/छ → श्."),
        mcq("transfer", 5, "By the pattern of विशेषतश्च, how is रामः + च joined in a new example?",
            ("रामश्च", "Visarga before च becomes श्: रामः + च → रामश्च."),
            [("रामो च", "ओ arises before a voiced consonant; च is voiceless."),
             ("रामस्च", "स् comes before त or थ, not before च."),
             ("रामर्च", "र् arises after a vowel other than अ/आ; here the vowel is अ.")],
            "रामः + च = रामश्च, like विशेषतः + च = विशेषतश्च.",
            "ः + च → श्च.",
            teaches="A visarga before च or छ becomes श्: विशेषतः + च → विशेषतश्च."),
    ],
}

# ---------------------------------------------------------------- unit 29
AUTHORED["29"] = {
    "title": "तेषु हि गुणमिश्रविकारकारिषु",
    "question": "By unit 29, what reason does the text give, and which part rests on a conjectural reading?",
    "rule": ("For (हि) in these, which produce disorders of mixed qualities (गुणमिश्रविकारकारिषु), in hunger, thirst and "
             "so on (क्षुत्पिपासादिषु), there is, on a conjectural reading, the designation of ill-health."),
    "limits": ("Low confidence. The printed अवारोग्य is no known word; अनारोग्य (ill-health) is a conjecture: no question "
               "on it. How the two locatives join is not sure: no question on that. The join ष्व holds on either "
               "reading."),
    "explain_hi": ("क्योंकि (हि) उनमें, जो गुणों के मिश्रण से विकार करने वाले हैं, भूख-प्यास आदि में, अनारोग्य का नाम दिया जाता है। "
                   "छपा ‘अवारोग्य’ कोई ज्ञात शब्द नहीं; ‘अनारोग्य’ (अस्वास्थ्य) अनुमानित पाठ है, इसलिए उस पर प्रश्न नहीं। "
                   "दोनों सप्तमी पद (तेषु ... कारिषु और क्षुत्पिपासादिषु) कैसे जुड़ते हैं, यह भी निश्चित नहीं। "
                   "पक्के अंश: तेषु (उनमें), हि (क्योंकि), गुण-मिश्र-विकार-कारिन् (मिले गुणों से विकार करने वाले), क्षुत्-पिपासा (भूख और प्यास)। "
                   "‘-दिष्व-’ में उ + अ → व् की सन्धि है, जो दोनों पाठों पर ठीक बैठती है।"),
    "hook": "हि: कारण। मिले गुण, मिले विकार।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 29, what does क्षुत्पिपासा name?",
            ("Hunger and thirst", "क्षुध् / क्षुत् = hunger, पिपासा = thirst."),
            [("Sleep and waking", "Sleep and waking would be निद्रा and जागर."),
             ("Heat and the cold", "Heat and cold would be उष्ण and शीत."),
             ("Pain and swelling", "Pain and swelling would be रुजा and शोफ.")],
            "क्षुत् (hunger) + पिपासा (thirst).",
            "क्षुत्पिपासा = hunger and thirst."),
        order(1, "Put the sure words of unit 29 in the printed order.",
              ["तेषु", "हि", "गुणमिश्रविकारकारिषु", "क्षुत्पिपासादिषु"],
              "In these; for; which produce disorders of mixed qualities; in hunger, thirst and so on.",
              "तेषु → हि → गुणमिश्रविकारकारिषु → क्षुत्पिपासादिषु."),
        match(2, "Match each part of गुणमिश्रविकारकारिषु and its neighbour to its meaning.",
              [["गुण", "quality"], ["मिश्र", "mixed"], ["विकार", "disorder"], ["कारिन्", "producing"],
               ["हि", "for, indeed"]],
              "गुण-मिश्र-विकार-कारिषु = in those producing disorders of mixed qualities; हि = for.",
              "गुण, मिश्र, विकार, कारिन्, हि.", role="extend",
              teaches="-कारिन् at the end of a compound means 'producing, doing'; -कारिषु is its locative plural."),
        mcq("discriminate", 3, "In क्षुत्पिपासादिष्व... of unit 29, why does -आदिषु appear as -आदिष्व-?",
            ("उ before a different vowel → व्", "उ + अ → व् + अ: -आदिषु + अ... → -आदिष्व...."),
            [("उ before any consonant → व्", "Before a consonant उ stays; व् arises only before a vowel."),
             ("उ + अ → ओ in all cases", "That is अ + उ → ओ; here उ stands first, so it gives व्."),
             ("उ is dropped before अ", "उ is not dropped; it becomes the semivowel व्.")],
            "-आदिषु + अ-: उ before a different vowel → व्.",
            "उ + unlike vowel → व्."),
        mcq("apply", 4, "In unit 29, what does the particle हि add to the line?",
            ("A reason ('for')", "हि = for, indeed: it gives a reason."),
            [("A question ('whether')", "A question would need किम्; हि gives a reason."),
             ("A negation ('not')", "A negation would need न; हि gives a reason."),
             ("A wish ('may it be')", "A wish would need an optative or imperative; हि gives a reason.")],
            "तेषु हि ...: for in these ...",
            "हि = for (a reason)."),
        mcq("transfer", 5, "By the pattern of -आदिषु + अ- → -आदिष्व-, how is मधु + अस्ति (there is honey) joined in a new example?",
            ("मध्वस्ति", "उ before a different vowel → व्: मधु + अस्ति → मध्वस्ति."),
            [("मधोस्ति", "ओ comes from अ + उ, not from उ + अ."),
             ("मधूस्ति", "ऊ comes from उ + उ; here the second vowel is अ."),
             ("मधवस्ति", "अव् comes from ओ before a vowel; here the vowel is उ.")],
            "मधु + अस्ति = मध्वस्ति, like -आदिषु + अ- = -आदिष्व-.",
            "उ + unlike vowel → व्.",
            teaches="इ, उ, ऋ before a different vowel become य्, व्, र्: -आदिषु + अ → -आदिष्व."),
    ],
}

# ---------------------------------------------------------------- unit 30
AUTHORED["30"] = {
    "title": "तस्माद्विपरीतगुणेन विधिना",
    "question": "By unit 30, how should they be treated, and where is the method said to be stated?",
    "rule": ("Therefore (तस्मात्) one should treat them (तान् उपाचरेत्) with a method of opposite qualities "
             "(विपरीतगुणेन विधिना), as stated in the Doṣopakramaṇīya (दोषोपक्रमणीयोक्तेन)."),
    "limits": ("Prose. 'Them' is not named here; the data reads it as the constitutions of the units before. That "
               "Doṣopakramaṇīya is the title of an earlier chapter on treating the doṣas is probable, not certain. No "
               "medicine, food or dose is named, and the card adds none."),
    "explain_hi": ("इसलिए (तस्मात्) उनका उपचार (तान् उपाचरेत्) विपरीत गुणों वाली विधि से करना चाहिए, जैसी दोषोपक्रमणीय में कही गई है। "
                   "‘उनका’ किनका, यह यहाँ छपा नहीं; डेटा इसे पिछली इकाइयों की प्रकृतियाँ मानता है। "
                   "दोषोपक्रमणीय सम्भवतः दोषों के उपचार वाले किसी पिछले अध्याय का नाम है (सम्भावित)। "
                   "कोई औषध, आहार या मात्रा नहीं बताई गई। "
                   "‘उपाचरेत्’ विधिलिङ् है: उपचार करना चाहिए।"),
    "hook": "विपरीत गुण से उपचार: दोषोपक्रमणीय में जैसा कहा।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 30, with what kind of method should they be treated?",
            ("One of opposite qualities", "विपरीतगुणेन विधिना: with a method of opposite qualities."),
            [("One of the same qualities", "The line says विपरीत, opposite, not the same."),
             ("One of sweet taste alone", "No taste is named in unit 30."),
             ("One without any fixed rule", "विधि itself means a method or procedure.")],
            "विपरीत-गुण = of opposite qualities.",
            "विपरीतगुणेन विधिना."),
        order(1, "Put the words of unit 30 in the printed order.",
              ["तस्मात्", "विपरीतगुणेन", "विधिना", "दोषोपक्रमणीयोक्तेन", "तान्", "उपाचरेत्"],
              "Therefore; of opposite qualities; with a method; stated in the Doṣopakramaṇīya; them; one should treat.",
              "तस्मात् → विपरीतगुणेन → विधिना → दोषोपक्रमणीयोक्तेन → तान् → उपाचरेत्."),
        match(2, "Match each word of unit 30 to its meaning.",
              [["विपरीत", "opposite"], ["गुण", "quality"], ["विधि", "method"], ["उक्त", "stated"],
               ["उपाचरेत्", "should treat"]],
              "विपरीत = opposite, गुण = quality, विधि = method, उक्त = stated, उपाचरेत् = should treat.",
              "विपरीत, गुण, विधि, उक्त, उपाचरेत्.", role="extend",
              teaches="उपाचरेत् is the optative of उप-आ-√चर्: 'one should treat'."),
        mcq("discriminate", 3, "Which split of दोषोपक्रमणीयोक्तेन in unit 30 is right?",
            ("दोष + उपक्रमणीय + उक्तेन", "अ + उ → ओ twice: दोष + उपक्रमणीय → दोषोपक्रमणीय; -णीय + उक्तेन → -णीयोक्तेन."),
            [("दोषः + उपक्रमणीय + उक्तेन", "अः before उ gives अ with a gap (दोष उप-), not ओ."),
             ("दोषो + पक्रमणीय + उक्तेन", "पक्रमणीय is not a word; the ओ comes from अ + उ."),
             ("दोष + उपक्रमणी + योक्तेन", "योक्तेन is not a word; उक्तेन (stated) follows -णीय.")],
            "दोष (doṣa) + उपक्रमणीय (treatment) + उक्तेन (stated): अ + उ → ओ.",
            "अ + उ → ओ."),
        mcq("apply", 4, "Why is तस्मात् printed तस्माद् before विपरीत in unit 30?",
            ("त् before the voiced व → द्", "व is a voiced sound: तस्मात् + विपरीत → तस्माद्विपरीत."),
            [("त् before any consonant → द्", "Not any: before च it becomes च् (दोषवच्च, unit 31)."),
             ("द् is the ablative's own ending", "The ablative ends in -आत्; द् comes only from sandhi."),
             ("त् before a vowel → द् here", "विपरीत begins with the consonant व, not a vowel.")],
            "तस्मात् + विपरीत-: त् before the voiced व → द्.",
            "त् + voiced व → द्."),
        mcq("transfer", 5, "By the pattern of उपाचरेत् (one should treat), which form of √पठ् means he should read, in a new example?",
            ("पठेत्", "-एत् is the optative, third person singular, of this verb class: पठेत्, like उपाचरेत्."),
            [("पठति", "पठति is the present: he reads."),
             ("पठिष्यति", "पठिष्यति is the future: he will read."),
             ("अपठत्", "अपठत् is the imperfect: he read.")],
            "पठेत् = he should read, like उपाचरेत् = one should treat.",
            "Optative 3 sg. (thematic verbs): -एत्.",
            teaches="Thematic verbs such as √चर् and √पठ् form the optative third person singular in -एत् (other classes differ: जानीयात्)."),
    ],
}

# ---------------------------------------------------------------- unit 31
AUTHORED["31"] = {
    "title": "सर्वरसेन सात्म्येन",
    "question": "By unit 31, which words are sure, and which parts rest on conjectural readings?",
    "rule": ("Sure words: with all tastes (सर्वरसेन), with what is suited (सात्म्येन), others (अन्यान्), prescribed by "
             "season (यथर्तुविहितेन); like the doṣas (दोषवत्), by the qualities beginning with sattva (गुणैः सत्त्वादिभिः), "
             "constitutions arise."),
    "limits": ("Low confidence. सेमं → समम् (the balanced one) and सम → सप्त (seven) are conjectures: no question on "
               "either. Line 1's verb is carried from unit 30. Nothing applied is named; no six-taste regimen is stated. "
               "Syntax uncertain: questions ask only words and joins."),
    "explain_hi": ("यह इकाई दो छपी पंक्तियाँ जोड़ती है और दोनों में अनुमानित पाठ हैं। "
                   "पहली पंक्ति: अनुमानित पाठ पर, सम (प्रकृति) को सब रसों से और सात्म्य से, और दूसरों को ऋतु के अनुसार विहित से; क्रिया इकाई ३० से आती है। "
                   "छपा ‘सेमं’ कोई शब्द नहीं, ‘समम्’ अनुमान है; दूसरी पंक्ति का ‘सम’ डेटा ‘सप्त’ (सात) पढ़ता है, यह भी अनुमान है। "
                   "दूसरी पंक्ति: दोषों की तरह (दोषवत्) सत्त्व आदि गुणों से भी (सात, अनुमान से) प्रकृतियाँ होती हैं; सत्त्व = मन (मानक)। "
                   "पक्की सन्धियाँ: यथा + ऋतु → यथर्तु (आ + ऋ → अर्), दोषवत् + च → दोषवच्च, गुणैः + अपि → गुणैरपि, अन्यान् + च → अन्यांश्च।"),
    "hook": "दोषवत्, गुणैरपि: दोषों जैसी ही सत्त्व आदि से भी प्रकृतियाँ।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 31, what does सात्म्य mean?",
            ("Suited by habit", "सात्म्य = what one is used to, suited by habit."),
            [("Untried and new", "That is the opposite of सात्म्य."),
             ("Bitter in taste", "Bitter is तिक्त; सात्म्य names suitability."),
             ("Cooked at night", "Nothing in सात्म्य names cooking or a time.")],
            "सात्म्य = suited (by habit).",
            "सात्म्य = suited."),
        order(1, "Put these printed parts of line 2 of unit 31 in order (the doubtful सम is left out).",
              ["दोषवच्च", "गुणैरपि", "सत्त्वादिभिः", "प्रकृतयो भवंति"],
              "Like the doṣas and; by qualities also; beginning with sattva; constitutions arise.",
              "दोषवच्च → गुणैरपि → सत्त्वादिभिः → (सम) → प्रकृतयो भवंति."),
        match(2, "Match each sure word of unit 31 to its meaning.",
              [["सर्व", "all"], ["रस", "taste"], ["ऋतु", "season"], ["विहित", "prescribed"], ["अन्य", "other"]],
              "सर्व-रस = all tastes, यथा-ऋतु-विहित = prescribed by season, अन्यान् = others.",
              "सर्व, रस, ऋतु, विहित, अन्य.", role="extend",
              teaches="दोषवत् uses the suffix -वत्, 'like': दोषवत् = like the doṣas."),
        mcq("discriminate", 3, "Which split of यथर्तुविहितेन in unit 31 is right?",
            ("यथा + ऋतु + विहितेन", "आ + ऋ → अर्: यथा + ऋतु → यथर्तु."),
            [("यथ + अर्तु + विहितेन", "Neither यथ nor अर्तु is a word."),
             ("यथा + अर्तु + विहितेन", "अर्तु is not a word; the season is ऋतु."),
             ("यथर् + तु + विहितेन", "यथर् is not a word; र् comes from ऋ.")],
            "यथा (according to) + ऋतु (season) + विहितेन (prescribed).",
            "आ + ऋ → अर्."),
        mcq("apply", 4, "In दोषवच्च of unit 31, why is दोषवत् written दोषवच् before च?",
            ("त् before च becomes च्", "त् takes the palatal place of च: दोषवत् + च → दोषवच्च."),
            [("त् before any consonant → च्", "Not any: before the voiced व it becomes द् (तस्माद्विपरीत, unit 30)."),
             ("च् is the ending of -वत् words", "The suffix is -वत्; च् comes only from sandhi."),
             ("त् drops and च is doubled", "त् does not drop; it becomes च्, giving च्च.")],
            "दोषवत् + च: त् before च → च्.",
            "त् + च → च्च."),
        mcq("transfer", 5, "By the pattern of यथा + ऋतु → यथर्तु, how is महा + ऋषिः joined in a new example?",
            ("महर्षिः", "आ + ऋ → अर्: महा + ऋषिः → महर्षिः."),
            [("महार्षिः", "आर् would be vṛddhi; आ + ऋ gives अर्."),
             ("महोर्षिः", "ओ comes from अ + उ, not from आ + ऋ."),
             ("महिर्षिः", "इ has no source here; आ + ऋ gives अर्.")],
            "महा + ऋषिः = महर्षिः, like यथा + ऋतु = यथर्तु.",
            "अ/आ + ऋ → अर्.",
            teaches="अ or आ before ऋ gives अर्: यथा + ऋतु → यथर्तु."),
    ],
}

# ---------------------------------------------------------------- unit 32
AUTHORED["32"] = {
    "title": "तास्तदभिनिवृत्तैरेव यथोक्तैः",
    "question": "By unit 32, by what should one know the constitutions?",
    "rule": ("One should know them (ताः जानीयात्) by cleanliness (शौच) and the like, as stated (यथोक्तैः), arisen "
             "only from them (तदभिनिवृत्तैः एव)."),
    "limits": ("Prose. 'Them' (ताः, f. pl.) is assumed to be the constitutions of unit 31; no antecedent is printed. 'As "
               "stated' points to a description not given here, and the items after śauca are not named: no question "
               "on what 'and the like' includes."),
    "explain_hi": ("उन (प्रकृतियों) को उन्हीं से उत्पन्न, जैसा कहा गया है, शौच आदि से जानना चाहिए। "
                   "‘ताः’ (स्त्रीलिंग बहुवचन) को इकाई ३१ की प्रकृतियाँ माना गया है; यह छपा नहीं। "
                   "‘यथोक्तैः’ किसी पहले कहे वर्णन की ओर संकेत करता है; शौच के बाद के लक्षण यहाँ नहीं गिनाए गए। "
                   "‘जानीयात्’ √ज्ञा का विधिलिङ् है: जानना चाहिए; इसका रूप -एत् में नहीं। "
                   "सन्धियाँ: ताः + तद् → तास्तद्, -वृत्तैः + एव → -वृत्तैरेव, शौचादिभिः + जानीयात् → शौचादिभिर्जानीयात्।"),
    "hook": "शौचादिभिर्जानीयात्: प्रकृति पहचानो उसी से उपजे लक्षणों से।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 32, which word is printed before -आदिभिः (and the like)?",
            ("शौच (cleanliness)", "शौचादिभिः = by cleanliness and the like."),
            [("बल (strength)", "बल is not printed in unit 32."),
             ("रूप (form)", "रूप is not printed in unit 32."),
             ("स्वर (voice)", "स्वर is not printed in unit 32.")],
            "शौच + आदिभिः: by cleanliness and the like.",
            "शौचादिभिः."),
        order(1, "Put the words of unit 32 in the printed order.",
              ["ताः", "तदभिनिवृत्तैः", "एव", "यथोक्तैः", "शौचादिभिः", "जानीयात्"],
              "Them; arisen from them; only; as stated; by cleanliness and the like; one should know.",
              "ताः → तदभिनिवृत्तैः → एव → यथोक्तैः → शौचादिभिः → जानीयात्."),
        match(2, "Match each word of unit 32 to its meaning.",
              [["शौच", "cleanliness"], ["अभिनिवृत्त", "arisen, produced"], ["यथोक्त", "as stated"],
               ["जानीयात्", "should know"], ["एव", "only"]],
              "शौच = cleanliness, अभिनिवृत्त = arisen, यथोक्त = as stated, जानीयात् = should know, एव = only.",
              "शौच, अभिनिवृत्त, यथोक्त, जानीयात्, एव.", role="extend",
              teaches="जानीयात् is the optative of √ज्ञा ('one should know'); not every optative ends in -एत्."),
        mcq("discriminate", 3, "Which split of शौचादिभिर्जानीयात् in unit 32 is right?",
            ("शौचादिभिः + जानीयात्", "इः before the voiced ज → इर्: शौचादिभिः + जानीयात् → शौचादिभिर्जानीयात्."),
            [("शौचादि + भिर्जानीयात्", "भिर्जानीयात् is not a word; -भिः is the ending of शौचादिभिः."),
             ("शौचादिभ्यः + जानीयात्", "अः before ज would give ओ: शौचादिभ्यो जानीयात्, not the print."),
             ("शौचादिभिः + अजानीयात्", "With अ- it would read शौचादिभिरजानीयात्, not the print.")],
            "शौचादिभिः (by cleanliness and the like) + जानीयात् (one should know).",
            "इः + voiced sound → इर्."),
        mcq("apply", 4, "Why does तदभिनिवृत्तैः show र् before एव in unit 32?",
            ("ऐः before a vowel → ऐर्", "A visarga after a vowel other than अ/आ becomes र् before a vowel."),
            [("Every visarga before a vowel → र्", "Not every: अः + अ gives ओऽ, and आः drops the visarga."),
             ("The र् belongs to the word एव", "The particle is एव; the र् comes from the visarga."),
             ("ऐः before a vowel drops ः", "Dropping happens after अ or आ; after ऐ the visarga becomes र्.")],
            "-वृत्तैः + एव → -वृत्तैरेव: ऐः before a vowel → ऐर्.",
            "ऐः / इः / उः + vowel → र्."),
        mcq("transfer", 5, "By the pattern of -वृत्तैः + एव → -वृत्तैरेव, how is देवैः + अपि joined in a new example?",
            ("देवैरपि", "ऐः before a vowel → ऐर्: देवैः + अपि → देवैरपि."),
            [("देवोऽपि", "ओऽ comes from अः + अ; here the vowel before the visarga is ऐ."),
             ("देवायपि", "आय् comes from ऐ with no visarga; देवैः has one."),
             ("देवावपि", "आव् comes from औ before a vowel, not from ऐः.")],
            "देवैः + अपि = देवैरपि, like -वृत्तैः + एव = -वृत्तैरेव.",
            "ऐः + vowel → ऐर्.",
            teaches="After a vowel other than अ/आ (here ऐ), a visarga before a vowel becomes र्: तदभिनिवृत्तैः + एव → तदभिनिवृत्तैरेव."),
    ],
}

# ---------------------------------------------------------------- unit 33
AUTHORED["33"] = {
    "title": "जातिकुलदेशकालवयोबलप्रत्यात्मसंश्रयाः",
    "question": "By unit 33, on which bases do the constitutions rest, in the printed order?",
    "rule": ("Likewise, again, the constitutions (seven, by a well-supported conjecture) are based on jāti, family (कुल), "
             "region (देश), time (काल), age (वयस्), strength (बल) and each individual (प्रत्यात्म)."),
    "limits": ("Prose, no verb. The printed सम is read सप्त (seven) on a conjecture the data calls well supported; no "
               "question rests on the word itself. जाति could be caste, species or birth-class ('birth-class' is the "
               "data's choice): no question on its sense."),
    "explain_hi": ("उसी प्रकार फिर प्रकृतियाँ सात आधारों पर टिकी हैं: जाति, कुल, देश, काल, वय, बल और प्रत्यात्म (प्रत्येक व्यक्ति)। "
                   "छपा ‘सम’ डेटा ‘सप्त’ (सात) पढ़ता है; यह अनुमान है, पर सात आधार इसी पंक्ति में गिने हैं, इसलिए अच्छा समर्थित है। "
                   "जाति का अर्थ वर्ण, प्रजाति या जन्म-वर्ग हो सकता है; डेटा ‘जन्म-वर्ग’ लेता है, इस पर प्रश्न नहीं। "
                   "‘प्रकृतयोजाति’ में अः + घोष व्यंजन ज → ओ, और ‘वयोबल’ में वयस् का अस् घोष व्यंजन ब से पहले ओ बना है। "
                   "पंक्ति में क्रिया नहीं; ‘हैं’ समझा जाता है।"),
    "hook": "जाति-कुल-देश-काल, वय-बल-प्रत्यात्म: सात आधार।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In the list of unit 33, what does देश mean?",
            ("Region", "देश = region, land."),
            [("Family", "Family is कुल, the item before देश."),
             ("Strength", "Strength is बल, a later item."),
             ("Time", "Time is काल, the item after देश.")],
            "देश = region.",
            "देश = region."),
        order(1, "After जाति, put the bases of unit 33 in the printed order.",
              ["कुल", "देश", "काल", "वयस्", "बल", "प्रत्यात्म"],
              "Family; region; time; age; strength; each individual.",
              "जाति → कुल → देश → काल → वयस् → बल → प्रत्यात्म."),
        match(2, "Match each word of unit 33 to its meaning.",
              [["कुल", "family"], ["देश", "region"], ["काल", "time"], ["बल", "strength"],
               ["प्रत्यात्म", "each individual"], ["संश्रय", "basis, support"]],
              "कुल = family, देश = region, काल = time, बल = strength, प्रत्यात्म = each individual, संश्रय = basis.",
              "कुल, देश, काल, बल, प्रत्यात्म, संश्रय.", role="extend",
              teaches="-संश्रयाः at the end of the compound means 'resting on': the constitutions rest on these seven bases."),
        mcq("discriminate", 3, "Why is प्रकृतयः printed प्रकृतयो before जाति in unit 33?",
            ("अः before a voiced consonant → ओ", "ज is a voiced consonant: प्रकृतयः + जाति- → प्रकृतयो जाति-."),
            [("अः before any consonant → ओ", "Not any: before a voiceless one such as त it gives स्."),
             ("आः before a voiced consonant → ओ", "आः drops its visarga; besides, the vowel here is अ."),
             ("ओ is the plural's own ending", "The nominative plural is प्रकृतयः; ओ comes only from sandhi.")],
            "प्रकृतयः + जाति-: अः before the voiced consonant ज → ओ.",
            "अः + voiced consonant → ओ."),
        mcq("apply", 4, "In वयोबल of unit 33, which split is right?",
            ("वयस् + बल", "-अस् before the voiced consonant ब → -ओ: वयस् + बल → वयोबल."),
            [("वय + उबल", "उबल is not a word; the ओ comes from -अस्."),
             ("वयु + बल", "वयु is not a word; age is वयस्."),
             ("वया + उबल", "Neither वया nor उबल fits; age is वयस्.")],
            "वयस् (age) + बल (strength): -अस् before a voiced consonant → -ओ.",
            "-अस् + voiced consonant → -ओ."),
        mcq("transfer", 5, "By the pattern of वयस् + बल → वयोबल, how is मनस् + बल joined in a compound, in a new example?",
            ("मनोबल", "-अस् before the voiced ब → -ओ: मनस् + बल → मनोबल."),
            [("मनश्बल", "श् arises before च, छ or श, not before ब."),
             ("मनबल", "The -अस् does not simply drop; it gives -ओ."),
             ("मनाबल", "आ has no source here; -अस् gives -ओ.")],
            "मनस् + बल = मनोबल, like वयस् + बल = वयोबल.",
            "-अस् + voiced consonant → -ओ.",
            teaches="An -अस् stem before a voiced consonant shows -ओ: वयस् + बल → वयोबल."),
    ],
}

# ---------------------------------------------------------------- unit 34
AUTHORED["34"] = {
    "title": "दृश्यंते हि पुरुषाणां",
    "question": "By unit 34, why do the varieties of constitution become countless?",
    "rule": ("Among men are seen particular states fixed by jāti and the rest; and by graded combination (तरतमयोगात्) of "
             "the seven and the others, by differences of body (शरीरविशेषेभ्यः) and by conformity to another "
             "(अन्यानुविधानत्वात्), the varieties become countless (असंख्येयम्)."),
    "limits": ("Prose. 'The seven and the rest' = the seven of unit 33 and probably their combinations (data's hedge). "
               "भेदाग्रम् ('extent of varieties') is the least sure word: no question on it. 'Conformity to another' is "
               "spelt out in unit 35; this card keeps to this unit's words."),
    "explain_hi": ("क्योंकि पुरुषों में जाति आदि से निश्चित वे-वे भाव-विशेष दिखाई देते हैं। "
                   "फिर तीन कारणों से भेद अगणित (असंख्येय) हो जाते हैं: सात आदि का कम-अधिक (तरतम) योग, शरीर की विशेषताएँ, और दूसरे का अनुसरण (अन्यानुविधान)। "
                   "‘सात आदि’ यानी इकाई ३३ के सात आधार और सम्भवतः उनके मेल (डेटा का संकेत)। "
                   "‘भेदाग्रम्’ (भेदों का विस्तार) सबसे कम पक्का शब्द है, इस पर प्रश्न नहीं। "
                   "‘तरतमयोगाच्छरीर’ में त् + श → च्श होता है, श के बाद स्वर हो तो वैकल्पिक रूप से च्छ, जो यहाँ छपा है।"),
    "hook": "तरतम योग, शरीर-भेद, अनुसरण: भेद असंख्य।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In unit 34, what does असंख्येय mean?",
            ("Countless", "अ-संख्येय = not to be counted: countless."),
            [("Exactly seven", "Seven is सप्त; असंख्येय means beyond counting."),
             ("Very few", "Few would be अल्प; असंख्येय means countless."),
             ("Fixed in number", "A fixed number is the opposite of असंख्येय.")],
            "असंख्येयम् = countless.",
            "असंख्येय = countless."),
        order(1, "Put these parts of unit 34 in the printed order.",
              ["सप्तादीनां तरतमयोगात्", "शरीरविशेषेभ्यः", "अन्यानुविधानत्वात्", "असंख्येयं भवति"],
              "By graded combination of the seven and the rest; by differences of body; by conformity to another; becomes countless.",
              "तरतमयोगात् → शरीरविशेषेभ्यः → अन्यानुविधानत्वात् → असंख्येयं भवति."),
        match(2, "Match each phrase of unit 34 to its meaning.",
              [["तरतम", "more and most (by degrees)"], ["शरीरविशेष", "differences of body"],
               ["अनुविधान", "conformity, following"], ["भावविशेष", "particular states"], ["नियत", "fixed, determined"]],
              "तर-तम = more and most; शरीर-विशेष = bodily differences; अनुविधान = conformity; भाव-विशेष = particular states; नियत = fixed.",
              "तरतम, शरीरविशेष, अनुविधान, भावविशेष, नियत.", role="extend",
              teaches="तर and तम are the comparative and superlative suffixes; तरतम-योग is a combination by degrees of more and most."),
        mcq("discriminate", 3, "Which split of तरतमयोगाच्छरीर- in unit 34 is right?",
            ("तरतमयोगात् + शरीर-", "त् + श → च्श, or optionally च्छ when a vowel follows श (as printed)."),
            [("तरतमयोगः + छरीर-", "छरीर is not a word, and a visarga does not give च्छ."),
             ("तरतमयोगाच् + छरीर-", "छरीर is not a word; the छ comes from the श of शरीर."),
             ("तरतमयोगम् + शरीर-", "म् before श would give ं: तरतमयोगं शरीर-.")],
            "तरतमयोगात् (from graded combination) + शरीर- (body).",
            "त् + श → च्श, optionally च्छ before a vowel."),
        multi("apply", 4, "Which does unit 34 give as reasons for the countless varieties?",
              [("Sameness of all bodies", "No: the line gives differences of body (शरीरविशेषेभ्यः)."),
               ("Graded combination of the seven and the rest", "Right: सप्तादीनां च तरतमयोगात्."),
               ("Equal, fixed shares in every person", "No: the line speaks of more and most (तरतम), not equal shares."),
               ("Differences of body", "Right: शरीरविशेषेभ्यः."),
               ("Conformity to another", "Right: अन्यानुविधानत्वात्.")],
              [1, 3, 4],
              "Three ablatives give the reasons: graded combination, bodily differences, conformity to another.",
              "तरतमयोगात्, शरीरविशेषेभ्यः, अन्यानुविधानत्वात् → असंख्येयम्."),
        mcq("transfer", 5, "By the pattern of अन्यानुविधानत्वात् (because of conforming), what does गुरुत्वात् mean in a new example?",
            ("Because of heaviness", "-त्वात् = ablative of the abstract -त्व: 'because of being ...'."),
            [("Belonging to heaviness", "Belonging would need the genitive गुरुत्वस्य."),
             ("Together with heaviness", "Together with would need the instrumental गुरुत्वेन."),
             ("Present in heaviness", "'In' would need the locative गुरुत्वे.")],
            "गुरुत्वात् = because of heaviness, like अन्यानुविधानत्वात्.",
            "-त्वात् = because of being.",
            teaches="An abstract noun in -त्व put in the ablative (-त्वात्) gives a reason: अन्यानुविधानत्वात् = because of conforming to another."),
    ],
}

# ---------------------------------------------------------------- unit 35
AUTHORED["35"] = {
    "title": "शरीरमपि सत्त्वादीननुविधीयते",
    "question": "By unit 35, how are body and sattva (mind) related, and what becomes countless?",
    "rule": ("The body conforms to sattva (mind) and the rest, and sattva and the rest conform to the body; then, on a "
             "conjectural reading, the imitation of form, voice and conduct (रूपस्वरचरितानुकरणम्) becomes of countless "
             "varieties."),
    "limits": ("Low confidence. सत्त्वाय- is no word; सत्त्वादि- is a conjecture: no question on the cause it names. The "
               "verb of the second clause is understood. अनुविधीयते is passive in form but read 'conforms to' with the "
               "accusative. No question on what the imitation means as doctrine."),
    "explain_hi": ("शरीर भी सत्त्व (मन) आदि का अनुसरण करता है, और सत्त्व आदि भी शरीर का; यानी अनुसरण दोनों ओर से है। "
                   "दूसरे वाक्य की क्रिया छपी नहीं, पहले वाली समझी जाती है। "
                   "आगे छपा ‘सत्त्वाय-’ कोई शब्द नहीं; ‘सत्त्वादि-’ अनुमानित पाठ है, इसलिए उस कारण पर प्रश्न नहीं। "
                   "उसी पाठ पर, रूप, स्वर और चरित (आचरण) की नकल भी, जो अनेक शब्दों से कही जाती है, अगणित भेदों वाली होती है। "
                   "‘अनुविधीयते’ रूप में कर्मवाच्य है, पर द्वितीया के साथ ‘अनुसरण करता है’ पढ़ा गया; हर -यते कर्मवाच्य नहीं होता।"),
    "hook": "शरीर मन के पीछे, मन शरीर के पीछे।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 35, what does the body conform to?",
            ("Sattva and the rest", "शरीरमपि सत्त्वादीननुविधीयते: the body conforms to sattva and the rest."),
            [("The stars and planets", "No stars or planets are named in unit 35."),
             ("Wealth and high rank", "No wealth or rank is named in unit 35."),
             ("The physician's word", "No physician is named in unit 35.")],
            "The body follows sattva (mind) and the rest.",
            "शरीरम् → सत्त्वादीन् अनुविधीयते."),
        order(1, "Put the sure opening words of unit 35 in the printed order.",
              ["शरीरमपि", "सत्त्वादीननुविधीयते", "सत्त्वादयोऽपि", "शरीरं"],
              "The body also; conforms to sattva and the rest; sattva and the rest also; the body.",
              "शरीरमपि → सत्त्वादीननुविधीयते → सत्त्वादयोऽपि → शरीरं."),
        match(2, "Match each word of unit 35 to its meaning.",
              [["रूप", "form"], ["स्वर", "voice"], ["चरित", "conduct"], ["अनुकरण", "imitation"], ["अनेक", "many"]],
              "रूप = form, स्वर = voice, चरित = conduct, अनुकरण = imitation, अनेक = many.",
              "रूप, स्वर, चरित, अनुकरण, अनेक.", role="extend",
              teaches="अनुविधीयते is passive in form, yet here it takes an accusative and means 'conforms to': not every -यते is a passive."),
        mcq("discriminate", 3, "Which split of सत्त्वादयोऽपि in unit 35 is right?",
            ("सत्त्वादयः + अपि", "अः + अ → ओ, and the अ of अपि is shown by ऽ: सत्त्वादयोऽपि."),
            [("सत्त्वादयो + पि", "पि is not a word; ऽ marks the dropped अ of अपि."),
             ("सत्त्वादय + ओपि", "ओपि is not a word; the ओ comes from अः."),
             ("सत्त्वादयः + पि", "पि is not a word; the particle is अपि.")],
            "सत्त्वादयः (sattva and the rest) + अपि (also).",
            "अः + अ → ओऽ."),
        mcq("apply", 4, "By unit 35, which way does conformity run between body and sattva?",
            ("Each conforms to the other", "The body follows sattva and the rest, and they follow the body."),
            [("Only body follows sattva", "The line adds सत्त्वादयोऽपि शरीरं: sattva follows the body too."),
             ("Only sattva follows body", "The line first says शरीरमपि सत्त्वादीन्: the body follows sattva too."),
             ("Neither one follows the other", "Both clauses state a following; neither is denied.")],
            "Both ways: शरीर → सत्त्वादि and सत्त्वादि → शरीर.",
            "Mutual conformity."),
        mcq("transfer", 5, "By the pattern of सत्त्वादयः + अपि → सत्त्वादयोऽपि, how is रामः + अपि joined in a new example?",
            ("रामोऽपि", "अः + अ → ओऽ: रामः + अपि → रामोऽपि."),
            [("रामरपि", "र् comes after a vowel other than अ/आ; here the vowel is अ."),
             ("रामाऽपि", "आ has no source here; अः + अ gives ओऽ."),
             ("रामश्पि", "श् comes before च, छ or श, not before a vowel.")],
            "रामः + अपि = रामोऽपि, like सत्त्वादयः + अपि = सत्त्वादयोऽपि.",
            "अः + अ → ओऽ.",
            teaches="अः before अ gives ओ, and the अ is marked by ऽ (avagraha): सत्त्वादयः + अपि → सत्त्वादयोऽपि."),
    ],
}

# ---------------------------------------------------------------- unit 36
AUTHORED["36"] = {
    "title": "तदावेशस्त्वनंतरजन्माभ्यासवास नया जन्यते",
    "question": "By unit 36, what produces 'that entry', and which beings are named for examining?",
    "rule": ("The entry into that (तदावेशः) is produced (जन्यते) by the latent impression (वासना) of practice in the "
             "immediately preceding birth; therefore one should examine (अन्वीक्षेत) the anūka of the person, with "
             "humans, animals, departed spirits and hell-beings named."),
    "limits": ("Low confidence; the unit's sense is not firm. अनूक (lineage? inherited trait?) and tad-āveśa ('entry "
               "into that state') are uncertain: no question on either. The genitive list joins पुरुषस्य loosely. "
               "वास नया is a spacing error for वासनया."),
    "explain_hi": ("उसमें प्रवेश (तदावेशः) तुरन्त पिछले जन्म के अभ्यास की वासना (संस्कार) से उत्पन्न होता है (जन्यते)। "
                   "इसीलिए मनुष्य, तिर्यक् (पशु-पक्षी), प्रेत और नारकी जीवों के, और उनके उन-उन भेदों के, पुरुष के ‘अनूक’ को यथोचित रूप से देखना चाहिए (अन्वीक्षेत)। "
                   "‘अनूक’ का अर्थ अस्पष्ट है (वंश? पैतृक लक्षण?), और ‘तदावेश’ भी केवल एक व्याख्या है; पूरी इकाई का भाव पक्का नहीं, इसलिए प्रश्न केवल पक्के शब्दों पर हैं। "
                   "छपा ‘वास नया’ एक ही शब्द ‘वासनया’ है, बीच में भूल से जगह छूटी है। "
                   "‘तदावेशस्त्व-’ में तदावेशः + तु (त से पहले विसर्ग → स्) और तु + अनन्तर (उ + अ → व्) की सन्धियाँ हैं।"),
    "hook": "पिछले जन्म की वासना: मनुष्य, तिर्यक्, प्रेत, नारक सबमें देखो।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In the list of beings in unit 36, what does तिर्यक् denote?",
            ("Animals", "तिर्यक् = animals (standard sense)."),
            [("Humans", "Humans are मानुष, the item before तिर्यक्."),
             ("Departed spirits", "Departed spirits are प्रेत, the item after तिर्यक्."),
             ("Hell-beings", "Hell-beings are नारक, the last item.")],
            "मानुष, तिर्यक् (animals), प्रेत, नारक.",
            "तिर्यक् = animal."),
        order(1, "Put the beings named in unit 36 in the printed order.",
              ["मानुष", "तिर्यक्", "प्रेत", "नारक"],
              "Humans; animals; departed spirits; hell-beings.",
              "मानुष → तिर्यक् → प्रेत → नारक."),
        match(2, "Match each sure word of unit 36 to its meaning.",
              [["अभ्यास", "practice"], ["वासना", "latent impression"], ["जन्म", "birth"], ["जन्यते", "is produced"],
               ["अन्वीक्षेत", "should examine"]],
              "अभ्यास = practice, वासना = latent impression, जन्म = birth, जन्यते = is produced, अन्वीक्षेत = should examine.",
              "अभ्यास, वासना, जन्म, जन्यते, अन्वीक्षेत.", role="extend",
              teaches="जन्यते is a passive of √जन्, 'is produced'; but not every -यते is passive (जायते 'is born' is not)."),
        mcq("discriminate", 3, "In unit 36, what is the printed वास नया?",
            ("One word, वासनया, with a stray space", "A spacing error: वासनया is the instrumental of वासना."),
            [("Two words, वासः and नया", "नया is no Sanskrit word here; the two halves make वासनया."),
             ("Two words, वास and अनया", "वास + अनया would join as वासानया, not the print."),
             ("Two words, वासे and नया", "No वासे is printed, and नया is no word here.")],
            "वास नया = वासनया (by the latent impression), printed with a space.",
            "A space inside a word is a print slip."),
        mcq("apply", 4, "In unit 36, what does अन्वीक्षेत ask of the reader?",
            ("That one should examine", "अन्वीक्षेत is an optative of अनु-√ईक्ष्: one should examine."),
            [("That one has examined", "A past would need another form; अन्वीक्षेत is optative."),
             ("That one will be examined", "A future passive would need another form; this is optative."),
             ("That one must never look", "The optative here directs examining; nothing forbids it.")],
            "अन्वीक्षेत = one should examine.",
            "Optative = 'should'."),
        mcq("transfer", 5, "By the pattern of अन्वीक्षेत (one should examine), which form of प्र + √ईक्ष् means one should look at, in a new example?",
            ("प्रेक्षेत", "प्र + ईक्षेत → प्रेक्षेत (अ + ई → ए); -एत is the middle optative, third person singular."),
            [("प्रेक्षते", "प्रेक्षते is the present: one looks at."),
             ("प्रैक्षत", "प्रैक्षत is the imperfect: one looked at."),
             ("प्रेक्षिष्यते", "प्रेक्षिष्यते is the future: one will look at.")],
            "प्रेक्षेत = one should look at, like अन्वीक्षेत = one should examine.",
            "Middle optative 3 sg.: -एत.",
            teaches="Middle verbs such as √ईक्ष् form the optative third person singular in -एत: अन्वीक्षेत, प्रेक्षेत."),
    ],
}

# ---------------------------------------------------------------- unit 37
AUTHORED["37"] = {
    "title": "वयस्त्रिविधं बालं मध्यं वृद्धं च",
    "question": "By unit 37, how is age divided, and what are its stages?",
    "rule": "Age (वयस्) is threefold (त्रिविधम्): young (बालम्), middle (मध्यम्) and old (वृद्धम्).",
    "limits": ("Prose, copula understood. Only the names of the stages are given here; their year-limits come in the "
               "next units and are not on this card. The neuter forms stand for the stages (data's note)."),
    "explain_hi": ("वय (आयु की अवस्था) तीन प्रकार का है: बाल, मध्य और वृद्ध। "
                   "यहाँ से वय का नया विषय आरम्भ होता है; इस इकाई में केवल तीन नाम हैं, उनकी वर्ष-सीमाएँ आगे की इकाइयों में हैं। "
                   "बालम्, मध्यम्, वृद्धम् नपुंसकलिंग रूप हैं जो अवस्थाओं के नाम हैं; ‘मध्यम्’ छपा रूप ही नियमित है। "
                   "‘वयस्त्रिविधं’ में वयः + त्रिविधम् है: त से पहले विसर्ग स् बनता है।"),
    "hook": "बाल, मध्य, वृद्ध: वय के तीन पड़ाव।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 37, what are the three stages of age?",
            ("Young, middle and old", "बालं मध्यं वृद्धं च: young, middle and old."),
            [("Birth, growth and death", "The line names stages of age, not birth or death."),
             ("Spring, summer and winter", "The line names stages of age, not seasons."),
             ("Middle, old and dying", "The first stage is बाल (young); no dying stage is named.")],
            "बाल, मध्य, वृद्ध.",
            "वयस्त्रिविधं बालं मध्यं वृद्धं च."),
        order(1, "Put the words of unit 37 in the printed order.",
              ["वयस्त्रिविधं", "बालं", "मध्यं", "वृद्धं च"],
              "Age is threefold; young; middle; and old.",
              "वयस्त्रिविधं → बालं → मध्यं → वृद्धं च."),
        match(2, "Match each word of unit 37 to its meaning.",
              [["वयस्", "age"], ["त्रिविध", "threefold"], ["बाल", "young"], ["मध्य", "middle"], ["वृद्ध", "old"]],
              "वयस् = age, त्रिविध = threefold, बाल = young, मध्य = middle, वृद्ध = old.",
              "वयस्, त्रिविध, बाल, मध्य, वृद्ध.", role="extend",
              teaches="-विध means 'kind': त्रिविधम् = of three kinds."),
        mcq("discriminate", 3, "In unit 37, what does त्रिविधम् say about age?",
            ("It is of three kinds", "त्रि (three) + विध (kind): threefold."),
            [("It lasts three years", "No years are given in unit 37."),
             ("It has three causes", "विध means kind, not cause."),
             ("It is thrice as strong", "त्रिविध counts kinds, not strength.")],
            "त्रिविधम् = of three kinds.",
            "-विध = kind."),
        mcq("apply", 4, "Why is वयः printed वयस् before त्रिविधं in unit 37?",
            ("Visarga before त becomes स्", "त is voiceless and dental: वयः + त्रिविधम् → वयस्त्रिविधम्."),
            [("Visarga before त becomes ओ", "ओ arises before a voiced consonant; त is voiceless."),
             ("Visarga before त is dropped", "It is not dropped; it becomes स्, as printed."),
             ("Visarga before त becomes र्", "र् arises after इ or उ before a voiced sound, not here.")],
            "वयः + त्रिविधम्: visarga before त → स्.",
            "ः + त → स्त."),
        mcq("transfer", 5, "By the pattern of त्रिविधम् (threefold), what does चतुर्विधम् mean in a new example?",
            ("Of four kinds", "चतुर् (four) + विध (kind): of four kinds."),
            [("The fourth one", "The fourth would be the ordinal चतुर्थ."),
             ("Four times over", "Four times would be चतुः (the numeral adverb)."),
             ("Lasting four years", "No years are in the word; विध means kind.")],
            "चतुर्विधम् = of four kinds, like त्रिविधम् = of three kinds.",
            "-विध = kind.",
            teaches="A number before -विध counts the kinds: त्रिविधम् = threefold, चतुर्विधम् = fourfold."),
    ],
}

# ================================================================ NOTES_HI
NOTES_HI = {
    "26": ("गद्य; विश्वास मध्यम; दो छपी पंक्तियाँ (०२.०८.३३ और ०२.०८.३४) जोड़ी गईं; कोई पाठ-चिह्न नहीं। क्रिया समझी जाती है। "
           "‘संसर्गकृतिः’ का विशेष्य (प्रकृति) छपा नहीं। ‘उभय’ = तीन में से दो दोष, और ‘सर्वगुण’ = तीनों दोषों के लक्षण एक साथ, "
           "दोनों डेटा की व्याख्याएँ हैं; समदोष = तीनों दोष सम, इकाई २ की सातवीं प्रकृति। छपाई में ‘संकरे’ अनुस्वार के साथ, विभाजन सङ्करे।"),
    "27": ("गद्य; विश्वास कम। पाठ-चिह्न (सम्भव): ‘दोषानुप्रशयितप्रकृतित्वात्’ अस्पष्ट है; ‘अनुप्रशयित’ ज्ञात रूप नहीं, ‘अनुशयित’ "
           "(चिपका हुआ) सुझाव केवल अनुमान है, अनुवाद में प्रयुक्त नहीं; इस पर कोई प्रश्न नहीं। ‘आद्याः त्रयः नित्यातुराः’ पुल्लिंग "
           "बहुवचन हैं, इसलिए अनकहा विशेष्य व्यक्ति हैं, स्त्रीलिंग ‘प्रकृतयः’ नहीं। सन्धि जाँची: तत्र + आद्याः → तत्राद्याः (अ + आ → आ); "
           "आद्याः + त्रयः → आद्यास्त्रयः (त से पहले विसर्ग → स्); त्रयः + नित्यातुराः → त्रयो नित्यातुराः (अः + घोष व्यंजन → ओ)। "
           "छपा ‘नित्यातुराः दोषा-’ घोष द से पहले विसर्ग रखता है (सन्धि नहीं की गई)।"),
    "28": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। अपूर्ण वाक्य: विधेय ‘नित्यातुराः’ इकाई २७ से आता है, यहाँ छपा नहीं। "
           "द्वन्द्व = मिले हुए दो दोषों का जोड़ा। व्याकरण-लेबल ‘स्त्री.’ है, जबकि इकाई २७ की टिप्पणी अनकहे विशेष्य को पुल्लिंग "
           "(व्यक्ति) मानती है; बहुवचन रूप दोनों लिंगों में एक जैसा है, इसलिए लिंग पर प्रश्न नहीं। सन्धि जाँची: विशेषतः + च → विशेषतश्च "
           "(च से पहले विसर्ग → श्); छपा ‘द्वंद्व’ अनुस्वार के साथ = द्वन्द्व।"),
    "29": ("गद्य; विश्वास कम। पाठ-चिह्न (सम्भव): छपा ‘अवारोग्य’ ज्ञात शब्द नहीं; ‘अनारोग्य’ (न/व की भूल) अनुमानित पाठ है, अनुवाद इसे "
           "अपनाता है; इस पर प्रश्न नहीं। दोनों सप्तमी पद ‘तेषु ... कारिषु’ और ‘क्षुत्पिपासादिषु’ साथ लिए गए; भूख-प्यास ही विकार करती "
           "है या नहीं, यह व्याकरण से निश्चित नहीं। क्रिया समझी जाती है। सन्धि जाँची: -आदिषु + अ- → -आदिष्व- (उ + भिन्न स्वर → व्), "
           "दोनों पाठों पर समान; क्षुध् + पिपासा → क्षुत्पिपासा (अघोष प से पहले ध् → त्)।"),
    "30": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। ‘तान्’ (उन्हें) का पूर्वपद इस इकाई में नहीं; डेटा इसे पिछली इकाइयों की प्रकृतियाँ "
           "(उन प्रकृतियों वाले) मानता है। ‘दोषोपक्रमणीय’ सम्भवतः किसी पिछले अध्याय का नाम (सम्भावित); ‘में कहा गया’ अर्थ लिया गया। "
           "सन्धि जाँची: तस्मात् + विपरीत → तस्माद्विपरीत (घोष व से पहले त् → द्); दोष + उपक्रमणीय → दोषोपक्रमणीय और -णीय + उक्तेन → "
           "-णीयोक्तेन (अ + उ → ओ); तान् + उपाचरेत् → तानुपाचरेत्। उपाचरेत् = उप-आ-√चर्, विधिलिङ्।"),
    "31": ("गद्य; विश्वास कम; दो छपी पंक्तियाँ (०२.०८.३९ और ०२.०८.४०) जोड़ी गईं। पाठ-चिह्न (सम्भव): ‘सेमं’ कोई शब्द नहीं, ‘समम्’ "
           "अनुमान (ए/अ की भूल); ‘समम्’ क्रियाविशेषण ‘समान रूप से’ भी हो सकता है। पाठ-चिह्न (सम्भव, अच्छा समर्थित): दूसरी पंक्ति का "
           "‘सम’ = ‘सप्त’ (प्त/म की भूल; इकाई ३३ में सात आधार, इकाई ३४ में ‘सप्तादीनां’)। पहली पंक्ति की क्रिया इकाई ३० से; क्या दिया "
           "जाए, यह नहीं कहा; छह रसों की कोई विधि नहीं कही। वाक्य-रचना अनिश्चित। सन्धि जाँची: यथा + ऋतु → यथर्तु (आ + ऋ → अर्); "
           "सात्म्येन + अन्यान् → सात्म्येनान्यान् (अ + अ → आ); अन्यान् + च → अन्यांश्च (च से पहले न् → ंश्); दोषवत् + च → दोषवच्च "
           "(च से पहले त् → च्); गुणैः + अपि → गुणैरपि (ऐः + स्वर → ऐर्)। सत्त्व = मन (मानक)।"),
    "32": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। ‘ताः’ = इकाई ३१ की प्रकृतियाँ (स्त्री. बहु.), पूर्वपद माना गया। ‘तदभिनिवृत्त’ = "
           "उनसे उत्पन्न, ‘शौचादिभिः’ का विशेषण। सन्धि जाँची: ताः + तद् → तास्तद् (त से पहले विसर्ग → स्); -वृत्तैः + एव → -वृत्तैरेव "
           "(ऐः + स्वर → ऐर्); शौचादिभिः + जानीयात् → शौचादिभिर्जानीयात् (इः + घोष → इर्); यथा + उक्तैः → यथोक्तैः (आ + उ → ओ)। "
           "जानीयात् = √ज्ञा, विधिलिङ्। व्याकरण-लेबल में ‘तदभिनिवृत्तैः’ और ‘शौचादिभिः’ का लिंग नहीं दिया गया।"),
    "33": ("गद्य; विश्वास मध्यम। पाठ-चिह्न (सम्भव, अच्छा समर्थित): छपा ‘सम’ = ‘सप्त’ (इसी पंक्ति में सात आधार; इकाई ३४ में "
           "‘सप्तादीनां’; प्त/म की भूल, इकाई ३१ देखें)। क्रिया समझी जाती है। जाति = वर्ण, प्रजाति या जन्म-वर्ग; डेटा ‘जन्म-वर्ग’ लेता है। "
           "प्रत्यात्म = प्रत्येक व्यक्ति में; संश्रय = आधार। सन्धि जाँची: प्रकृतयः + जाति- → प्रकृतयो जाति- (अः + घोष व्यंजन → ओ; छपाई में "
           "बिना जगह); वयस् + बल → वयोबल (अस् + घोष व्यंजन → ओ)।"),
    "34": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। ‘पुरुषाणांजात्यादि’ बिना जगह छपा है, यह केवल छपाई की आदत। ‘ते ते’ = वे-वे। "
           "‘सप्तादीनां’ = इकाई ३३ के सात और सम्भवतः उनके मेल। ‘भेदाग्रम्’ = भेद + अग्रम् (भेदों का विस्तार), सबसे कम पक्का शब्द। "
           "सन्धि जाँची: -नियताः + ते → -नियतास्ते (त से पहले विसर्ग → स्); तरतमयोगात् + शरीर- → तरतमयोगाच्छरीर- (त् + श → च्श, "
           "श के बाद स्वर हो तो वैकल्पिक च्छ, जो छपा है); -विशेषेभ्यः + च → -विशेषेभ्यश्च; -त्वात् + च → -त्वाच्च; भेदाग्रम् + असंख्येयम् → "
           "भेदाग्रमसंख्येयम्।"),
    "35": ("गद्य; विश्वास कम। पाठ-चिह्न (सम्भव): ‘सत्त्वाय-’ कोई शब्द नहीं; ‘सत्त्वादि-/सत्त्वाद्य-’ अनुमान (द छूटा); इस पर प्रश्न नहीं। "
           "‘अनुविधीयते’ रूप में कर्मवाच्य, पर द्वितीया ‘सत्त्वादीन्’ के साथ ‘अनुसरण करता है’ पढ़ा गया; दूसरे वाक्य में वही क्रिया समझी "
           "जाती है। ‘भेदंभवति’ बिना जगह छपा, केवल छपाई। सन्धि जाँची: शरीरम् + अपि → शरीरमपि; सत्त्वादीन् + अनुविधीयते → "
           "सत्त्वादीननुविधीयते; सत्त्वादयः + अपि → सत्त्वादयोऽपि (अः + अ → ओऽ); -करणम् + अपि → -करणमपि; अपि + अनेक → अप्यनेक "
           "(इ + भिन्न स्वर → य्)।"),
    "36": ("गद्य; विश्वास कम; डेटा के अनुसार पूरी इकाई का भाव पक्का नहीं। पाठ-चिह्न: ‘वास नया’ में भूल से जगह, शब्द ‘वासनया’ (वासना, "
           "तृतीया)। ‘तस्मादेवमानुष-’ को तस्मात् + एव + मानुष- पढ़ा गया (‘तस्माद् एवं आनुष-’ भी सम्भव दिखता है, पर ‘आनुष’ कोई शब्द "
           "नहीं)। ‘अनूक’ अस्पष्ट: कोश ‘वंश, कुल’ और ‘रीढ़’ देते हैं; अनुवाद में ‘अनूक’ ही रखा गया। ‘तदावेश’ = उस (अवस्था) में प्रवेश, "
           "व्याख्या मात्र। तिर्यक् = पशु-पक्षी (मानक); प्रेत = दिवंगत आत्मा; नारक = नरक का जीव। सन्धि जाँची: तदावेशः + तु → तदावेशस्तु "
           "(त से पहले विसर्ग → स्); तु + अनन्तर → त्वनन्तर (उ + भिन्न स्वर → व्); यथायथम् + एव + अनूकम् → यथायथमेवानूकम् (अ + अ → आ); "
           "पुरुषस्य + अन्वीक्षेत → पुरुषस्यान्वीक्षेत (अ + अ → आ)।"),
    "37": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। क्रिया समझी जाती है। बालम्, मध्यम्, वृद्धम् नपुंसक विशेषण अवस्थाओं के नाम के रूप "
           "में; ‘मध्यम्’ (मध्यमम् नहीं) छपा रूप ही नियमित नपुंसक रूप है। वर्ष-सीमाएँ आगे की इकाइयों में। सन्धि जाँची: वयः + त्रिविधम् → "
           "वयस्त्रिविधम् (त से पहले विसर्ग → स्); व्यंजन से पहले अन्तिम म् → ं (बालं मध्यं वृद्धं)।"),
}

# ================================================================ AIDS
AIDS = {
    "26": {
        "diagram": {"groups": [
            {"label": "उभयलक्षणसंकरे तु", "items": ["संसर्गकृतिः: दोनों के लक्षण मिले"]},
            {"label": "सर्वगुणसमुदितः", "items": ["समदोषप्रकृतिः: सब गुणों से युक्त"]}]},
        "chunks": "उभयलक्षणसंकरे तु | संसर्गकृतिः | सर्वगुणसमुदितः | समदोषप्रकृतिः",
        "contrast": "उभय (दो के लक्षण मिले) → संसर्गकृति ⇄ सर्व (सब गुण साथ) → समदोषप्रकृति: दोनों इसी इकाई में।",
    },
    "27": {
        "chunks": "तत्राद्यास्त्रयो | नित्यातुराः | दोषानुप्रशयितप्रकृतित्वात्",
        "sandhi": ("अ + आ → आ: तत्र + आद्याः → तत्राद्याः · त से पहले विसर्ग → स्: आद्याः + त्रयः → आद्यास्त्रयः · अः + घोष व्यंजन → "
                   "ओ: त्रयः + नित्यातुराः → त्रयो नित्यातुराः।"),
        "anchors": "पक्का भाग: पहले तीन, सदा रोगी। अस्पष्ट भाग: कारण बताने वाला अन्तिम शब्द। (मेरी याद-पद्धति)",
    },
    "28": {
        "frame": "जोड़: च (और) → कितना: विशेषतः (विशेष रूप से) → कौन: द्वन्द्वप्रकृतयः → विधेय: नित्यातुराः (इकाई २७ से, छपा नहीं)।",
        "diagram": {"groups": [
            {"label": "नित्यातुराः (इकाई २७ का विधेय)", "items": ["आद्याः त्रयः (इकाई २७)", "विशेषतः: द्वन्द्वप्रकृतयः (इकाई २८)"]}]},
        "sandhi": "च से पहले विसर्ग → श्: विशेषतः + च → विशेषतश्च।",
    },
    "29": {
        "chunks": "तेषु हि | गुणमिश्रविकारकारिषु | क्षुत्पिपासादिष्ववारोग्यव्यपदेशः",
        "sandhi": ("उ + भिन्न स्वर → व्: -आदिषु + अ- → -आदिष्व- · अघोष प से पहले ध् → त्: क्षुध् + पिपासा → क्षुत्पिपासा।"),
        "anchors": "पक्का: हि = कारण; भूख-प्यास आदि। अनुमान: ‘अवारोग्य’ → अनारोग्य। (मेरी याद-पद्धति)",
    },
    "30": {
        "chain": {"steps": ["तस्मात्: इसलिए", "विपरीतगुणेन विधिना: विपरीत गुणों वाली विधि से",
                            "दोषोपक्रमणीयोक्तेन: दोषोपक्रमणीय में कही (सम्भावित अध्याय)", "तान् उपाचरेत्: उनका उपचार करे"]},
        "chunks": "तस्माद्विपरीतगुणेन | विधिना | दोषोपक्रमणीयोक्तेन | तानुपाचरेत्",
        "sandhi": ("घोष व से पहले त् → द्: तस्मात् + विपरीत → तस्माद्विपरीत · अ + उ → ओ: दोष + उपक्रमणीय → दोषोपक्रमणीय, -णीय + उक्तेन → "
                   "-णीयोक्तेन।"),
    },
    "31": {
        "chunks": "सेमं | सर्वरसेन | सात्म्येनान्यांश्च | यथर्तुविहितेन च || दोषवच्च | गुणैरपि | सत्त्वादिभिः | सम | प्रकृतयो भवंति",
        "sandhi": ("आ + ऋ → अर्: यथा + ऋतु → यथर्तु · च से पहले त् → च्: दोषवत् + च → दोषवच्च · ऐः + स्वर → ऐर्: गुणैः + अपि → गुणैरपि · "
                   "च से पहले न् → ंश्: अन्यान् + च → अन्यांश्च।"),
        "anchors": "पक्का: सर्वरस, सात्म्य, यथर्तुविहित, दोषवत्, सत्त्वादि। अनुमान: सेमं → समम्, सम → सप्त। (मेरी याद-पद्धति)",
    },
    "32": {
        "frame": "किसे: ताः (प्रकृतियाँ, माना गया) → किससे: शौचादिभिः (शौच आदि से) → कैसे: तदभिनिवृत्तैः एव, यथोक्तैः → क्या करे: जानीयात् (जाने)।",
        "chunks": "तास्तदभिनिवृत्तैरेव | यथोक्तैः | शौचादिभिर्जानीयात्",
        "sandhi": ("त से पहले विसर्ग → स्: ताः + तद् → तास्तद् · ऐः + स्वर → ऐर्: -वृत्तैः + एव → -वृत्तैरेव · इः + घोष → इर्: शौचादिभिः + "
                   "जानीयात् → शौचादिभिर्जानीयात्।"),
    },
    "33": {
        "diagram": {"groups": [
            {"label": "प्रकृतियों के आधार (छपे क्रम में)", "items": ["१ जाति", "२ कुल", "३ देश", "४ काल", "५ वयस्", "६ बल",
                                                           "७ प्रत्यात्म"]}]},
        "chunks": "तथा पुनः | सम | प्रकृतयोजातिकुलदेशकालवयोबलप्रत्यात्मसंश्रयाः",
        "sandhi": "अः + घोष व्यंजन → ओ: प्रकृतयः + जाति- → प्रकृतयो जाति- · अस् + घोष व्यंजन → ओ: वयस् + बल → वयोबल।",
        "pegs": "जा-कु-दे-का, व-ब-प्र: सात आधारों के पहले अक्षर। (मेरा बनाया स्मरण-सूत्र)",
    },
    "34": {
        "chain": {"steps": ["सप्तादीनां तरतमयोगात्: सात आदि का कम-अधिक योग", "शरीरविशेषेभ्यः: शरीर की विशेषताएँ",
                            "अन्यानुविधानत्वात्: दूसरे का अनुसरण", "असंख्येयं भवति: भेद अगणित"]},
        "chunks": ("दृश्यंते हि | पुरुषाणांजात्यादिनियतास्ते ते भावविशेषाः | सप्तादीनां च तरतमयोगाच्छरीरविशेषेभ्यश्चान्यानुविधानत्वाच्च | "
                   "भेदाग्रमसंख्येयं भवति"),
        "sandhi": ("त् + श → च्श, श के बाद स्वर हो तो वैकल्पिक च्छ: तरतमयोगात् + शरीर- → तरतमयोगाच्छरीर- · च से पहले विसर्ग → श्: "
                   "-विशेषेभ्यः + च → -विशेषेभ्यश्च · च से पहले त् → च्: -त्वात् + च → -त्वाच्च।"),
    },
    "35": {
        "seesaw": "शरीर → सत्त्वादि का अनुसरण ⇄ सत्त्वादि → शरीर का अनुसरण: दोनों इसी इकाई में; अनुसरण दोनों ओर से।",
        "chunks": "शरीरमपि | सत्त्वादीननुविधीयते | सत्त्वादयोऽपि शरीरं | सत्त्वायसंख्येयभेदवशाच्च | रूपस्वरचरितानुकरणमप्यनेकशब्दवाच्यमसंख्यभेदंभवति",
        "sandhi": "अः + अ → ओऽ: सत्त्वादयः + अपि → सत्त्वादयोऽपि · इ + भिन्न स्वर → य्: अपि + अनेक → अप्यनेक।",
    },
    "36": {
        "chunks": ("तदावेशस्त्वनंतरजन्माभ्यासवास नया | जन्यते | तस्मादेवमानुषतिर्यक्प्रेतनारकाणां | तत्तद्विशेषाणां च | "
                   "यथायथमेवानूकं | पुरुषस्यान्वीक्षेत"),
        "sandhi": ("त से पहले विसर्ग → स्: तदावेशः + तु → तदावेशस्तु · उ + भिन्न स्वर → व्: तु + अनन्तर → त्वनन्तर · अ + अ → आ: "
                   "पुरुषस्य + अन्वीक्षेत → पुरुषस्यान्वीक्षेत।"),
        "anchors": "पक्का: पिछले जन्म के अभ्यास की वासना; मनुष्य, तिर्यक्, प्रेत, नारक; अन्वीक्षेत। अस्पष्ट: अनूक, तदावेश। (मेरी याद-पद्धति)",
    },
    "37": {
        "chain": {"steps": ["वयस्त्रिविधं: वय तीन प्रकार का", "१ बाल", "२ मध्य", "३ वृद्ध"]},
        "chunks": "वयस्त्रिविधं | बालं | मध्यं | वृद्धं च",
        "sandhi": "त से पहले विसर्ग → स्: वयः + त्रिविधम् → वयस्त्रिविधम्।",
    },
}

# ================================================================ IMAGE_SPECS
IMAGE_SPECS = {
    ("26", "contrast"): {
        "file": "sh8-sansarga-sama-26.svg",
        "alt": ("Split of card 26: saṃsargakṛti, when the marks of both are mixed; samadoṣaprakṛti, one endowed with "
                "all the qualities."),
        "type": "split",
        "title": "कार्ड २६: संसर्ग और समदोष",
        "cols": [["संसर्गकृति", ["दोनों के लक्षण मिले", "उभयलक्षणसंकरे"]],
                 ["समदोषप्रकृति", ["सब गुणों से युक्त", "सर्वगुणसमुदितः"]]],
    },
    ("28", "diagram"): {
        "file": "sh8-nityatura-28.svg",
        "alt": ("Flowchart of card 28: the predicate always ailing (from card 27) covers the first three (card 27) and, "
                "especially, the dual constitutions (card 28)."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"नित्यातुर: सदा रोगी\"] --> B[\"आद्याः त्रयः: कार्ड २७\"]\n"
                 "  A --> C[\"विशेषतः: कार्ड २८\"]\n"
                 "  C --> D[\"द्वन्द्व प्रकृतियाँ\"]\n"),
    },
    ("30", "chain"): {
        "file": "sh8-viparita-30.svg",
        "alt": ("Chain of card 30: therefore; with a method of opposite qualities; as stated in the Doṣopakramaṇīya "
                "(probably a chapter); one should treat them."),
        "type": "chain",
        "title": "कार्ड ३०: विपरीत गुण से उपचार",
        "steps": ["तस्मात्: इसलिए", "विपरीत गुणों वाली विधि से", "दोषोपक्रमणीय में कही (सम्भावित)", "उनका उपचार करे"],
    },
    ("33", "diagram"): {
        "file": "sh8-sapta-ashraya-33.svg",
        "alt": ("Table of card 33 in printed order: jāti, family, region, time, age, strength, each individual: the "
                "seven bases of the constitutions."),
        "type": "table",
        "title": "कार्ड ३३: प्रकृतियों के सात आधार",
        "heads": ["क्रम", "आधार"],
        "rows": [["१", "जाति"], ["२", "कुल: परिवार"], ["३", "देश: प्रदेश"], ["४", "काल: समय"], ["५", "वयस्: आयु"],
                 ["६", "बल: शक्ति"], ["७", "प्रत्यात्म: प्रत्येक व्यक्ति"]],
    },
    ("34", "chain"): {
        "file": "sh8-asankhyeya-34.svg",
        "alt": ("Flowchart of card 34: three reasons, graded combination of the seven and the rest, differences of body, "
                "and conformity to another, lead to countless varieties."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"१ सात आदि का तरतम योग\"] --> D[\"भेद असंख्येय\"]\n"
                 "  B[\"२ शरीर की विशेषताएँ\"] --> D\n"
                 "  C[\"३ दूसरे का अनुसरण\"] --> D\n"),
    },
    ("35", "seesaw"): {
        "file": "sh8-sharira-sattva-35.svg",
        "alt": ("Flowchart of card 35: the body follows sattva (mind) and the rest, and sattva and the rest follow the "
                "body: conformity both ways."),
        "type": "mermaid",
        "code": ("flowchart LR\n"
                 "  A[\"शरीर\"] -- \"अनुसरण\" --> B[\"सत्त्व आदि: मन\"]\n"
                 "  B -- \"अनुसरण\" --> A\n"),
    },
    ("37", "chain"): {
        "file": "sh8-vayas-37.svg",
        "alt": "Chain of card 37 in printed order: age is threefold: young, middle, old.",
        "type": "mermaid",
        "code": ("flowchart LR\n"
                 "  A[\"१ बाल\"] --> B[\"२ मध्य\"]\n"
                 "  B --> C[\"३ वृद्ध\"]\n"),
    },
}
