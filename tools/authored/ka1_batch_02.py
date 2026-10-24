from helpers import mcq, match, order, fill, multi, accepts

AUTHORED = {}

# ---------------------------------------------------------------- unit 12
AUTHORED["12"] = {
    "title": "ततः प्रयोगकाले फलपिप्पलीनाम्",
    "question": "At the time of use, how does unit 12 prepare and give the stored fruit-pippalīs?",
    "rule": ("At the time of use, coarsely crush a handful of the fruit-pippalīs (or as much as seems fit) and have it "
             "drunk, by the method of the Sūtrasthāna, in a decoction of any one of nine named drugs."),
    "limits": ("Low confidence. अन्तर्मुखमुष्टि (a handful?) is uncertain. The second वा can be read two ways, so the "
               "'kept a night' option is not questioned. फलपिप्पली = probably the madana pieces of line 05.01.11. IDs: "
               "yaṣṭīmadhuka, bimbī, pratyakpuṣpī standard; kovidāra, nīpa probable; the other four disputed."),
    "explain_hi": ("सँभालकर रखी फल-पिप्पलियाँ (सम्भवतः मैनफल के सूखे टुकड़े) प्रयोग के समय निकाली जाती हैं। "
                   "उनकी एक मुट्ठी, या जितनी ठीक समझे, दरदरी कूटी जाती है; ‘अन्तर्मुखमुष्टि’ का ठीक माप अनिश्चित है। "
                   "फिर इन नौ में से किसी एक के काढ़े में दी जाती है: यष्टीमधुक यानी मुलेठी, कोविदार यानी कचनार, कर्बुदार, नीप यानी कदम्ब, "
                   "विदुल, बिम्बी यानी कुन्दरू, शणपुष्पी, सदापुष्पी और प्रत्यक्पुष्पी यानी चिरचिटा। "
                   "पिलाने की विधि सूत्रस्थान में कही विधि है। "
                   "‘अन्यतम’ का अर्थ है इनमें से कोई एक, सब एक साथ नहीं।"),
    "hook": "मुट्ठी भर कूटो, नौ में से एक के काढ़े में, सूत्र-विधि से पिलाओ।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "What is finally done with the crushed fruit-pippalīs in unit 12?",
            ("They are given to drink", "पाययेत् = one should have it drunk."),
            [("They are rubbed on the chest", "No outward use is named in the unit."),
             ("They are burnt as a smoke", "No smoke or fumigation is named in the unit."),
             ("They are cooked into rice", "No rice dish is named in the unit.")],
            "The crushed pieces go into a decoction and are given to drink by the Sūtra method (पाययेत्).",
            "जर्जरीकृत्य … कषाये … पाययेत् = crush, put in the decoction, have it drunk."),
        order(1, "Put these drugs of unit 12's decoction list in the order of the text.",
              ["यष्टीमधुक", "कोविदार", "नीप", "बिम्बी", "प्रत्यक्पुष्पी"],
              "The list opens with yaṣṭīmadhuka and closes with pratyakpuṣpī; kovidāra, nīpa and bimbī stand between.",
              "यष्टीमधुक · कोविदार · (कर्बुदार) · नीप · (विदुल) · बिम्बी · (शणपुष्पी, सदापुष्पी) · प्रत्यक्पुष्पी."),
        match(2, "Match each drug of unit 12's list to its identification in the card.",
              [["यष्टीमधुक", "liquorice (standard)"], ["नीप", "kadamba (probable)"],
               ["बिम्बी", "ivy gourd (standard)"], ["प्रत्यक्पुष्पी", "prickly chaff-flower (standard)"]],
              "Four of the nine drugs, with the confidence word the data gives.",
              "यष्टीमधुक = liquorice; नीप = kadamba; बिम्बी = ivy gourd; प्रत्यक्पुष्पी = prickly chaff-flower.",
              role="extend",
              teaches="Unit 12's decoction may be of liquorice (यष्टीमधुक), kadamba (नीप), ivy gourd (बिम्बी) or prickly chaff-flower (प्रत्यक्पुष्पी), among nine."),
        mcq("discriminate", 3, "Which is the right split of प्रत्यक्पुष्प्यन्यतम-?",
            ("प्रत्यक्पुष्पी + अन्यतम", "ई before a different vowel becomes य्: पुष्पी + अन्यतम → पुष्प्यन्यतम."),
            [("प्रत्यक्पुष्पे + अन्यतम", "ए + अ would give एऽ (पुष्पेऽन्यतम), not य."),
             ("प्रत्यक्पुष्पु + अन्यतम", "उ + अ would give व (पुष्प्वन्यतम), not य."),
             ("प्रत्यक्पुष्पः + अन्यतम", "अः + अ would give ओऽ (पुष्पोऽन्यतम).")],
            "The drug is प्रत्यक्पुष्पी; with अन्यतम (any one) its ई becomes य्.",
            "इ/ई + unlike vowel → य् + vowel."),
        multi("apply", 4, "A helper has four decoctions ready. Which two may carry the drink of unit 12?",
              [("A decoction of यष्टीमधुक (liquorice)", "Right: it heads the list of nine."),
               ("A decoction of आरग्वध (golden shower tree)", "Wrong: āragvadha is not among the nine of this unit."),
               ("A decoction of बिम्बी (ivy gourd)", "Right: bimbī is one of the nine."),
               ("A decoction of त्रिफला (three fruits)", "Wrong: triphalā is not among the nine of this unit.")],
              [0, 2],
              "Any one of the nine named drugs will do; āragvadha and triphalā are not named here.",
              "Decoction of any one (अन्यतम) of the nine drugs of unit 12."),
        mcq("transfer", 5, "पाययेत् is the causative of √पा (drink). What does a new sentence बालं दुग्धं पाययेत् mean?",
            ("One should make the child drink milk", "Causative पाययेत् = cause (someone) to drink; बालम् is the one made to drink."),
            [("The child should drink the milk itself", "That would be बालः दुग्धं पिबेत्, with the plain verb."),
             ("One should drink the milk of the child", "The child would then be in the genitive (बालस्य)."),
             ("One should give the child up for milk", "पाययेत् is about drinking, not giving up.")],
            "पिबेत् = one should drink; पाययेत् = one should make (another) drink.",
            "Causative of √पा: पाययति, optative पाययेत्.",
            teaches="पाययेत् is the causative optative of √पा: 'one should make (someone) drink'; the plain optative is पिबेत्."),
    ],
}

# ---------------------------------------------------------------- unit 13
AUTHORED["13"] = {
    "title": "श्लेष्मज्वरगुल्मप्रतिश्यायान्तर्विद्रधिषु",
    "question": "In which conditions does unit 13 say the drink of unit 12 is given especially?",
    "rule": ("The sentence of line 05.01.12 continues: especially in phlegm (śleṣma), fever, gulma (abdominal lump), "
             "pratiśyāya (coryza, common cold) and internal abscesses."),
    "limits": ("Low confidence. The closing पुनरापित्तगमनात् ('again, until Pitta comes') is obscure and is not questioned. "
               "श्लेष्मज्वर may also be read 'kapha-fever'. The unit has no verb of its own; it continues the sentence before."),
    "explain_hi": ("यह इकाई पिछली पंक्ति का वाक्य आगे बढ़ाती है और बताती है कि वह पेय विशेष रूप से किन दशाओं में है। "
                   "सूची है: श्लेष्म यानी कफ, ज्वर, गुल्म यानी पेट के भीतर की गाँठ, प्रतिश्याय यानी जुकाम, और अन्तर्विद्रधि यानी भीतरी फोड़ा। "
                   "‘विशेषेण’ का अर्थ है विशेष रूप से। "
                   "अन्त का ‘पुनरापित्तगमनात्’ (फिर, पित्त के आने तक) अस्पष्ट है; उसका ठीक भाव तय नहीं।"),
    "hook": "कफ, ज्वर, गुल्म, जुकाम, भीतरी फोड़ा: इनमें विशेष रूप से।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "Which group of conditions does unit 13 name with विशेषेण (especially)?",
            ("Kapha, fever, gulma, cold, internal abscess", "श्लेष्म-ज्वर-गुल्म-प्रतिश्याय-अन्तर्विद्रधिषु."),
            [("Raktapitta, heartburn and a burning body", "Raktapitta and heartburn belong to line 05.01.17."),
             ("Wasting, thirst, fainting and insomnia", "None of these is named in the unit."),
             ("Tumour, nodule, scrofula and lost relish", "These are in line 05.01.15, not here.")],
            "The unit lists five: śleṣma, jvara, gulma, pratiśyāya, antarvidradhi.",
            "श्लेष्म · ज्वर · गुल्म · प्रतिश्याय · अन्तर्विद्रधि."),
        order(1, "Put the conditions of unit 13 in the order of the text.",
              ["श्लेष्म (कफ)", "ज्वर", "गुल्म", "प्रतिश्याय", "अन्तर्विद्रधि"],
              "Phlegm, fever, gulma, coryza, internal abscess.",
              "श्लेष्म · ज्वर · गुल्म · प्रतिश्याय · अन्तर्विद्रधि."),
        match(2, "Match each condition of unit 13 to its meaning.",
              [["ज्वर", "fever"], ["गुल्म", "abdominal lump"], ["प्रतिश्याय", "coryza, common cold"],
               ["अन्तर्विद्रधि", "internal abscess"]],
              "Four of the five names of the list, as the card renders them.",
              "ज्वर = fever; गुल्म = abdominal lump; प्रतिश्याय = common cold; अन्तर्विद्रधि = internal abscess.",
              role="extend",
              teaches="गुल्म = abdominal lump; प्रतिश्याय = coryza (common cold); अन्तर्विद्रधि = internal abscess."),
        mcq("discriminate", 3, "Which is the right split of प्रतिश्यायान्तर्विद्रधिषु?",
            ("प्रतिश्याय + अन्तर्विद्रधिषु", "अ + अ → आ: प्रतिश्याय + अन्तर् → प्रतिश्यायान्तर्."),
            [("प्रतिश्यायः + अन्तर्विद्रधिषु", "अः + अ would give ओऽ (प्रतिश्यायोऽन्तर्)."),
             ("प्रतिश्याये + अन्तर्विद्रधिषु", "ए + अ would give एऽ (प्रतिश्यायेऽन्तर्)."),
             ("प्रतिश्यायि + अन्तर्विद्रधिषु", "इ + अ would give य (प्रतिश्याय्यन्तर्).")],
            "Inside the compound, प्रतिश्याय (stem) + अन्तर्विद्रधि: अ + अ → आ.",
            "अ + अ → आ."),
        mcq("apply", 4, "Which of these patients has a condition named in unit 13's list?",
            ("One with gulma, an abdominal lump", "गुल्म is the third name of the list."),
            [("One with raktapitta, a bleeding disorder", "Raktapitta is named in line 05.01.17, not here."),
             ("One whose body is drying up", "A drying body is named in line 05.01.20, not here."),
             ("One with burning of the heart", "Burning of the heart is in line 05.01.17, not here.")],
            "The list: śleṣma, fever, gulma, cold, internal abscess.",
            "Unit 13's five: श्लेष्म, ज्वर, गुल्म, प्रतिश्याय, अन्तर्विद्रधि."),
        mcq("transfer", 5, "विद्रधिषु is a locative plural, in abscesses. Which form means in fevers (ज्वर, an -अ stem)?",
            ("ज्वरेषु", "-अ stems take -एषु in the locative plural."),
            [("ज्वरिषु", "-इषु belongs to -इ stems like विद्रधि, not to ज्वर."),
             ("ज्वराणाम्", "This is the genitive plural, 'of fevers'."),
             ("ज्वरैः", "This is the instrumental plural, 'by fevers'.")],
            "विद्रधि (-इ stem) → विद्रधिषु; ज्वर (-अ stem) → ज्वरेषु.",
            "Locative plural: -अ stem → -एषु; -इ stem → -इषु.",
            teaches="The locative plural 'in …' is -एषु for -अ stems (ज्वरेषु) and -इषु for -इ stems (विद्रधिषु)."),
    ],
}

# ---------------------------------------------------------------- unit 14
AUTHORED["14"] = {
    "title": "तेन साधु वमति",
    "question": "What result does unit 14 state for the drink just described?",
    "rule": "By that one vomits well. तेन = by that (instrumental); साधु = well; वमति = one vomits (present).",
    "limits": ("The line states the result only. That 'that' is the drink of lines 05.01.12-13 follows from the "
               "order of the text; the line itself names no drug, dose or time."),
    "explain_hi": ("यह छोटी पंक्ति पिछले पेय का फल बताती है: ‘तेन साधु वमति’, यानी उससे भली प्रकार वमन होता है। "
                   "‘तेन’ तृतीया विभक्ति है: ‘उससे’ या ‘उसके द्वारा’। "
                   "‘साधु’ क्रिया-विशेषण है: अच्छी तरह। "
                   "‘वमति’ √वम् का वर्तमान काल, प्रथम पुरुष एकवचन है: वमन करता है।"),
    "hook": "तेन साधु वमति: उससे अच्छा वमन।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What result does unit 14 state?",
            ("One vomits well", "साधु वमति = one vomits well."),
            [("One is purged well", "Purging is not named; वमति is vomiting."),
             ("One sleeps soundly", "Sleep is not named in the line."),
             ("One's fever leaves", "Fever is not named in this line.")],
            "तेन साधु वमति = by that one vomits well.",
            "वमति = one vomits; साधु = well."),
        match(1, "Match each word of unit 14 to its meaning.",
              [["तेन", "by that"], ["साधु", "well"], ["वमति", "one vomits"]],
              "Three words: the means, the manner and the verb.",
              "तेन = by that; साधु = well; वमति = one vomits."),
        fill(2, "The verb of unit 14 that means 'one vomits' is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("वमति"),
             "वमति is 3 sg present of √वम्: one vomits.",
             "वमति (√वम्, present) = one vomits; the noun वमन names emesis.",
             "वमति = one vomits."),
        mcq("discriminate", 3, "Which English rendering of तेन साधु वमति has one wrong word?",
            ("By that one vomits badly", "Wrong: साधु is 'well', not 'badly'."),
            [("By that one vomits well", "Correct: this is the card's rendering."),
             ("Through that one vomits well", "Correct: तेन can be 'through that'."),
             ("By that one vomits properly", "Correct: 'properly' renders साधु.")],
            "साधु means well, properly; 'badly' reverses it.",
            "साधु = well."),
        mcq("apply", 4, "How does the data label तेन in unit 14?",
            ("Instrumental: 'by that'", "The gram label is n. inst. sg."),
            [("Genitive: 'of that'", "The genitive would be तस्य."),
             ("Locative: 'in that'", "The locative would be तस्मिन्."),
             ("Dative: 'for that'", "The dative would be तस्मै.")],
            "तेन = by that (instrumental singular).",
            "तेन (inst.) = by that; तस्य (gen.) = of that; तस्मिन् (loc.) = in that."),
        mcq("transfer", 5, "Like पिबेत् (one should drink), which form of √वम् means one should vomit?",
            ("वमेत्", "3 sg optative: root + -एत्, as पिबेत्."),
            [("वमति", "This is the present: 'one vomits'."),
             ("वमितुम्", "This is the infinitive: 'to vomit'."),
             ("वान्तम्", "This is the past participle: 'vomited'.")],
            "वमति states a fact; वमेत् gives the 'should' of the optative.",
            "3 sg optative = root + -एत्.",
            teaches="The 3rd singular optative ends in -एत् and means 'one should': पिबेत्, वमेत्; वमति is the present."),
    ],
}

# ---------------------------------------------------------------- unit 15
AUTHORED["15"] = {
    "title": "फलपिप्पलीचूर्णं वा स्वक्वाथभावितम्",
    "question": "Which powder does unit 15 give, steeped in what, with which vehicle and for which conditions?",
    "rule": ("Or one should drink the fruit-pippalī powder steeped in its own decoction, with triphalā powder in three parts, "
             "in a decoction of kovidāra and the rest: in strong Kapha, praseka, apaci, arbuda, granthi, fever, udara and arocaka."),
    "limits": ("त्विफला is printed for त्रिफला (misprint flagged); त्रिभाग may also mean 'a third part'. A stray space splits "
               "जवरोदरा रोचकेषु (udara-arocakeṣu). बलवत् may go with kapha only or with all. The kovidāra group is not "
               "listed. Apaci = cervical glandular swellings (probable). How to render praseka is open."),
    "explain_hi": ("एक और विकल्प: फल-पिप्पली का चूर्ण, जो अपने ही क्वाथ में भावित (भिगोया) हो। "
                   "उसके साथ तीन भाग त्रिफला-चूर्ण (हरड़, बहेड़ा, आँवला; छपा ‘त्विफला’ मुद्रण-दोष है) बताया गया है। "
                   "इसे कोविदार आदि के काढ़े से पिया जाता है; उस समूह के सदस्य यहाँ नहीं गिनाए गए। "
                   "दशाएँ: प्रबल कफ, प्रसेक, अपची यानी गण्डमाला (सम्भावित), अर्बुद यानी ट्यूमर, ग्रन्थि यानी गाँठ, ज्वर, उदर और अरोचक यानी अरुचि।"),
    "hook": "अपने क्वाथ में भिगोया चूर्ण, कोविदार-समूह के काढ़े से: कफ से अरुचि तक।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In what is the fruit-pippalī powder of unit 15 steeped?",
            ("In its own decoction", "स्वक्वाथभावितम् = steeped in its own decoction."),
            [("In honey and ghee", "Honey and ghee are not named in this unit."),
             ("In cow's urine", "Urine is not named in this unit."),
             ("In a sour gruel", "No gruel is named in this unit.")],
            "स्व (own) + क्वाथ (decoction) + भावित (steeped).",
            "स्वक्वाथभावित = steeped in its own decoction."),
        match(1, "Match each part of unit 15's preparation to its role.",
              [["फलपिप्पलीचूर्ण", "the powder that is drunk"], ["स्वक्वाथ", "its own decoction, for steeping"],
               ["कोविदारादिनिर्यूह", "the decoction it is drunk with"]],
              "Powder, steeping liquid and vehicle are three different things in the unit.",
              "चूर्ण = powder; स्वक्वाथ = its own decoction; कोविदारादिनिर्यूह = decoction of kovidāra and the rest."),
        order(2, "Put these conditions of unit 15 in the order of the text.",
              ["कफ (बलवत्)", "प्रसेक", "अपची", "अर्बुद", "ग्रन्थि", "ज्वर"],
              "Strong Kapha, praseka, apaci, arbuda, granthi, fever (then udara and arocaka).",
              "बलवत्कफ · प्रसेक · अपची · अर्बुद · ग्रन्थि · ज्वर.",
              role="extend",
              teaches="Unit 15's list runs: strong Kapha, praseka, apaci, arbuda, granthi, fever, udara, arocaka."),
        mcq("discriminate", 3, "Which is the right split of कोविदारादिनिर्यूहेण?",
            ("कोविदार + आदि + निर्यूहेण", "अ + आ → आ: कोविदार + आदि → कोविदारादि."),
            [("कोविदारे + आदि + निर्यूहेण", "ए + आ would not give a plain आ (it gives अ आ or अया)."),
             ("कोविदारि + आदि + निर्यूहेण", "इ + आ would give या (कोविदार्यादि)."),
             ("कोविदारो + आदि + निर्यूहेण", "ओ + आ would give अवा (कोविदारवादि).")],
            "कोविदार-आदि-निर्यूह = decoction of kovidāra and the rest.",
            "अ + आ → आ."),
        multi("apply", 4, "Which two of these patients does unit 15 name for this drink?",
              [("One with arbuda, a tumour", "Right: अर्बुद is named."),
               ("One with raktapitta, a bleeding disorder", "Wrong: raktapitta is in line 05.01.17."),
               ("One with granthi, a nodular swelling", "Right: ग्रन्थि is named."),
               ("One with burning of the heart", "Wrong: heartburn is in line 05.01.17.")],
              [0, 2],
              "Unit 15 names strong Kapha, praseka, apaci, arbuda, granthi, fever, udara and arocaka.",
              "अर्बुद and ग्रन्थि are in unit 15's list."),
        mcq("transfer", 5, "स्वक्वाथ means its own decoction (स्व + क्वाथ). What does a new compound स्वकल्क mean, with कल्क = paste?",
            ("Its own paste", "स्व = own: a paste of the same drug."),
            [("A good paste", "'Good' would be सु- (सुकल्क), not स्व-."),
             ("Another drug's paste", "स्व- points to the same drug, not another."),
             ("A paste-free mix", "'Without' would need निर्- or अ-.")],
            "स्व + क्वाथ = its own decoction; स्व + कल्क = its own paste.",
            "स्व- in a compound = one's own.",
            teaches="स्व- at the head of a compound means 'its own': स्वक्वाथ (its own decoction), स्वकल्क (its own paste)."),
    ],
}

# ---------------------------------------------------------------- unit 16
AUTHORED["16"] = {
    "title": "मदनफलमज्जाचूर्णं वा",
    "question": "Which powder does unit 16 give, with which decoction, and in which state of Pitta?",
    "rule": ("Or the powder of the kernel (majjā) of the madana fruit, with a decoction of jīmūtaka and the rest, "
             "when Pitta has gone to the seat of Kapha."),
    "limits": ("The unit has no verb (elliptical); 'should be given/drunk' is understood from the lines before. "
               "The jīmūtaka group is not listed here. Madana = emetic nut, मैनफल (standard in this chapter)."),
    "explain_hi": ("यह इकाई एक और योग देती है: मदनफल यानी मैनफल की मज्जा (भीतरी गिरी) का चूर्ण। "
                   "यह जीमूतक आदि के क्वाथ के साथ है; उस समूह के सदस्य यहाँ नहीं गिनाए गए। "
                   "दशा: जब पित्त कफ के स्थान में चला गया हो। "
                   "‘पित्ते कफस्थानगते’ सति-सप्तमी है: दोनों शब्द सप्तमी में हैं और ‘जब … तब’ का अर्थ देते हैं। "
                   "इकाई में क्रिया नहीं है; पिलाने का भाव पिछली पंक्तियों से आता है।"),
    "hook": "पित्त कफ के घर में: मैनफल-गिरी का चूर्ण, जीमूतक के क्वाथ से।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In which state does unit 16 give the madana-kernel powder?",
            ("Pitta gone to the seat of Kapha", "पित्ते कफस्थानगते = when Pitta has gone to the seat of Kapha."),
            [("Kapha gone to the seat of Pitta", "The roles are reversed: it is Pitta that has moved."),
             ("Vāta blocked inside the belly", "Vāta is not named in this unit."),
             ("A fever in its first days", "Fever is not named in this unit.")],
            "Pitta (पित्ते) has gone (गते) to Kapha's seat (कफस्थान).",
            "पित्ते कफस्थानगते = Pitta in Kapha's seat."),
        match(1, "Match each word of unit 16 to its meaning.",
              [["मदनफल", "madana (emetic nut) fruit"], ["मज्जा", "kernel"], ["चूर्ण", "powder"],
               ["निर्यूह", "decoction"]],
              "मदनफलमज्जाचूर्ण = powder of the kernel of the madana fruit; निर्यूह is the vehicle.",
              "मदनफल = emetic nut; मज्जा = kernel; चूर्ण = powder; निर्यूह = decoction."),
        order(2, "Put these words of unit 16 in the order of the text.",
              ["मदनफलमज्जाचूर्णम्", "जीमूतकादिनिर्यूहेण", "पित्ते", "कफस्थानगते"],
              "What (the powder), with what (the decoction), when (Pitta … in Kapha's seat).",
              "मदनफलमज्जाचूर्णं वा · जीमूतकादिनिर्यूहेण · पित्ते · कफस्थानगते.",
              role="extend",
              teaches="Unit 16 runs: the madana-kernel powder, with jīmūtaka-group decoction, when Pitta has gone to Kapha's seat."),
        mcq("discriminate", 3, "Which decoction carries the powder in unit 16?",
            ("Of jīmūtaka and the rest", "जीमूतकादिनिर्यूहेण = with the decoction of jīmūtaka and the rest."),
            [("Of kovidāra and the rest", "That vehicle belongs to line 05.01.15."),
             ("Of surasā and the rest", "Surasā's group comes in line 05.01.23."),
             ("Of āragvadha and the rest", "Āragvadha's group comes in line 05.01.21.")],
            "Each formulation here names its own vehicle; unit 16's is the jīmūtaka group.",
            "Unit 16: जीमूतकादि-निर्यूह."),
        mcq("apply", 4, "A physician finds that Pitta has moved into the seat of Kapha. What does unit 16 give?",
            ("Madana-kernel powder in jīmūtaka decoction", "This is the formulation the unit ties to that state."),
            [("Fresh butter cooked with the six phalas", "Fresh butter is the formulation of line 05.01.20."),
             ("A palmful of the film of cold milk", "The milk-film is the formulation of line 05.01.18."),
             ("A lick cooked with an āragvadha decoction", "The āragvadha lick is the formulation of line 05.01.21.")],
            "Unit 16 pairs the madana-kernel powder with the state 'Pitta in Kapha's seat'.",
            "State → formulation, as unit 16 states it."),
        mcq("transfer", 5, "पित्ते कफस्थानगते means when Pitta has gone to Kapha's seat. What does a new phrase वाते प्रकुपिते mean?",
            ("When Vāta is aggravated", "Noun and participle both in the locative: 'when X is Y'."),
            [("The aggravated Vāta (as subject)", "The subject would be वातः प्रकुपितः, in the nominative."),
             ("For the aggravated Vāta", "'For' would need the dative (वाताय)."),
             ("From the aggravated Vāta", "'From' would need the ablative (वातात्).")],
            "Same build as पित्ते … गते: a locative absolute.",
            "Noun (loc.) + participle (loc.) = 'when X is/has …'.",
            teaches="A noun and a participle both in the locative give 'when …': पित्ते कफस्थानगते, वाते प्रकुपिते."),
    ],
}

# ---------------------------------------------------------------- unit 17
AUTHORED["17"] = {
    "title": "मदनफलमज्जसिद्धं वा पयः",
    "question": "Which milk preparations does unit 17 give, and for which conditions?",
    "rule": ("Or milk cooked with the kernel of the madana fruit, or a gruel (yavāgū) in that milk: in raktapitta "
             "(a bleeding disorder) and in burning of the heart."),
    "limits": ("अधोभागे ('in the lower part') may go with raktapitta (bleeding by the lower passage) or with the milk; "
               "no question rests on it. मज्ज is read as a variant of मज्जा. No amount is given."),
    "explain_hi": ("इस इकाई में दूध के योग शुरू होते हैं: मदनफल यानी मैनफल की मज्जा से सिद्ध (पकाया) दूध। "
                   "विकल्प के रूप में उसी दूध में बनी यवागू यानी गाढ़ी लपसी। "
                   "दशाएँ: रक्तपित्त यानी रक्तस्राव का रोग, और हृदय की जलन। "
                   "‘अधोभागे’ (निचले भाग में) रक्तपित्त के साथ भी जा सकता है और दूध के साथ भी; यह तय नहीं।"),
    "hook": "मैनफल-गिरी वाला दूध, या उसमें लपसी: रक्तपित्त और हृदय की जलन में।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What is cooked with the madana kernel in unit 17?",
            ("Milk (पयः)", "मदनफलमज्जसिद्धं पयः = milk cooked with the madana kernel."),
            [("Curd (दधि)", "Curd comes in line 05.01.19."),
             ("Oil (तैल)", "Oil is not named in this unit."),
             ("Honey (मधु)", "Honey is not named in this unit.")],
            "सिद्ध = cooked; पयः = milk.",
            "मदनफलमज्जसिद्धं पयः = kernel-cooked milk."),
        match(1, "Match each word of unit 17 to its meaning.",
              [["पयः", "milk"], ["यवागू", "gruel"], ["रक्तपित्त", "a bleeding disorder"], ["हृद्दाह", "burning of the heart"]],
              "Two preparations and two conditions.",
              "पयः = milk; यवागू = gruel; रक्तपित्त = bleeding disorder; हृद्दाह = burning of the heart."),
        order(2, "Put these items of unit 17 in the order of the text.",
              ["मज्जा से सिद्ध दूध", "उस दूध में यवागू", "रक्तपित्त", "हृदय की जलन"],
              "Milk, then the gruel in it; then the two conditions.",
              "मदनफलमज्जसिद्धं पयः · तस्मिन् यवागूम् · रक्तपित्ते · हृद्दाहे.",
              role="extend",
              teaches="Unit 17: kernel-cooked milk, or a gruel made in it; for raktapitta and burning of the heart."),
        mcq("discriminate", 3, "In unit 17, what does तस्मिन् (in that) point to?",
            ("The kernel-cooked milk", "तस्मिन् (n. loc.) takes up पयः: a gruel in that milk."),
            [("The gruel itself", "यवागू is what is made in 'that'; it is feminine, not तस्मिन्."),
             ("The burning of the heart", "हृद्दाह is a condition, not a cooking medium."),
             ("The madana tree", "No tree is named; the fruit kernel is used.")],
            "पयः … तस्मिन् वा यवागूम् = milk, or a gruel in that (milk).",
            "तस्मिन् = in that (milk)."),
        multi("apply", 4, "For which two conditions does unit 17 give the kernel-cooked milk or its gruel?",
              [("Raktapitta, a bleeding disorder", "Right: रक्तपित्ते is named."),
               ("Internal abscess", "Wrong: internal abscess is in line 05.01.13."),
               ("Burning of the heart", "Right: हृद्दाहे is named."),
               ("Loss of relish for food", "Wrong: arocaka is in line 05.01.15.")],
              [0, 2],
              "The unit names raktapitta and burning of the heart.",
              "रक्तपित्ते हृद्दाहे च = in raktapitta and burning of the heart."),
        mcq("transfer", 5, "मदनफलमज्जसिद्धं पयः is milk cooked with the madana kernel. What does a new phrase यष्टीमधुकसिद्धं पयः mean?",
            ("Milk cooked with liquorice", "X-सिद्धं पयः = milk cooked with X."),
            [("Liquorice cooked in milk", "The head is पयः (milk); the first member is what it is cooked with."),
             ("Liquorice and milk, raw", "सिद्ध means cooked, not raw."),
             ("Milk to be cooked later", "सिद्ध is a past participle: already cooked.")],
            "In X-सिद्ध the first member names what the thing is cooked with.",
            "X-सिद्धं पयः = milk cooked with X.",
            teaches="X-सिद्ध = cooked with X: मदनफलमज्जसिद्धं पयः, यष्टीमधुकसिद्धं पयः (milk cooked with liquorice)."),
    ],
}

# ---------------------------------------------------------------- unit 18
AUTHORED["18"] = {
    "title": "तस्य वा पयसः शीतस्य संतानिकाम्",
    "question": "What does unit 18 take from the cold milk, how much, and in which state?",
    "rule": ("Or a palmful (añjali) of the santānikā (the film on milk) of that cold milk, when Pitta is aggravated and "
             "the chest, throat and heart are smeared with thin Kapha."),
    "limits": ("सन्तानिका is taken as the film or skin that forms on milk (Hindi मलाई). 'That' milk is the "
               "kernel-cooked milk of line 05.01.17, by the order of the text. The print has a stray avagraha "
               "in संतानिकांऽजलिं; no question rests on it. No verb: the giving is understood."),
    "explain_hi": ("उसी दूध से अगला योग: ठंडे दूध की सन्तानिका यानी ऊपर जमने वाली मलाई। "
                   "मात्रा: एक अञ्जलि, यानी दोनों हथेलियों को जोड़कर भरी मात्रा। "
                   "दशा के दो अंश हैं: पित्त कुपित हो, और छाती, कण्ठ तथा हृदय पतले कफ से लिप्त हों। "
                   "‘कफोपादिग्धे’ में कफ + उपादिग्धे की सन्धि है (अ + उ → ओ)।"),
    "hook": "ठंडे दूध की मलाई, एक अञ्जलि: कुपित पित्त, छाती-कण्ठ-हृदय पर पतला कफ।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What is taken from the cold milk in unit 18?",
            ("Its santānikā, the film", "सन्तानिका = the film that forms on milk."),
            [("Its whey, the clear water", "Whey is not named in this unit."),
             ("Its froth, while boiling", "The milk is cold (शीत), not boiling."),
             ("Its butter, after churning", "Fresh butter comes in line 05.01.20.")],
            "तस्य पयसः शीतस्य सन्तानिकाम् = the film of that cold milk.",
            "सन्तानिका = film on milk."),
        match(1, "Match each word of unit 18 to its meaning.",
              [["शीत", "cold"], ["सन्तानिका", "film that forms on milk"], ["प्रकुपित", "aggravated"],
               ["तनुकफ", "thin Kapha"]],
              "The milk, what is taken from it, and the two parts of the state.",
              "शीत = cold; सन्तानिका = milk-film; प्रकुपित = aggravated; तनुकफ = thin Kapha."),
        order(2, "Put the body parts of unit 18 in the order of the text.",
              ["उरः (छाती)", "कण्ठ", "हृदय"],
              "Chest, throat, heart: उरःकण्ठहृदये.",
              "उरः · कण्ठ · हृदय.",
              role="extend",
              teaches="Unit 18 names chest, throat and heart (उरःकण्ठहृदये) as smeared with thin Kapha."),
        mcq("discriminate", 3, "Which state calls for the milk-film in unit 18?",
            ("Pitta aggravated; chest, throat, heart under thin Kapha", "पित्ते प्रकुपिते … तनुकफोपादिग्धे."),
            [("Pitta gone into the seat of Kapha", "That state belongs to line 05.01.16."),
             ("Fire overcome by Kapha; body drying up", "That state belongs to line 05.01.20."),
             ("Raktapitta with burning of the heart", "Those conditions belong to line 05.01.17.")],
            "Two parts: aggravated Pitta, and thin Kapha smeared on chest, throat and heart.",
            "Unit 18: पित्ते प्रकुपिते + उरःकण्ठहृदये तनुकफोपादिग्धे."),
        mcq("apply", 4, "How much of the milk-film does unit 18 give?",
            ("One palmful (अञ्जलि)", "अञ्जलिम् = a palmful, both hands cupped."),
            [("One fist (मुष्टि)", "A fist is the measure of line 05.01.12."),
             ("One ladle (दर्वी)", "The ladle appears in line 05.01.24, not as a measure here."),
             ("One full storage pot (कलश)", "The pot is for storage in line 05.01.11.")],
            "सन्तानिकाम् अञ्जलिम् = a palmful of the film; no other measure is given.",
            "अञ्जलि = both hands cupped."),
        mcq("transfer", 5, "कफ + उपादिग्धे → कफोपादिग्धे. Join a new example, हित + उपदेशः (good advice). Which is right?",
            ("हितोपदेशः", "अ + उ → ओ, as in कफ + उपादिग्ध."),
            [("हितौपदेशः", "औ comes from अ + ओ/औ, not अ + उ."),
             ("हितूपदेशः", "ऊ comes from उ + उ, not अ + उ."),
             ("हितउपदेशः", "The two vowels do not stay side by side.")],
            "Same rule as कफ + उपादिग्धे = कफोपादिग्धे.",
            "अ/आ + उ/ऊ → ओ.",
            teaches="अ or आ before उ or ऊ becomes ओ: कफ + उपादिग्धे = कफोपादिग्धे; हित + उपदेशः = हितोपदेशः."),
    ],
}

# ---------------------------------------------------------------- unit 19
AUTHORED["19"] = {
    "title": "तज्जं वा दधि दध्युत्तरं वा",
    "question": "Which two curd preparations does unit 19 offer?",
    "rule": ("Or the curd born of that (milk), or the upper part of the curd (dadhyuttara), in Kapha, vomiting, "
             "praseka and (probably) tamaka."),
    "limits": ("The list of conditions rests on a flagged print (तन्मक, probably तमक, a breathing disorder), so it is not "
               "questioned. दध्युत्तर is rendered literally 'upper part of curd'; its exact sense is uncertain. "
               "'That' is the milk of the lines before, by the order of the text."),
    "explain_hi": ("दूध के क्रम में अगला योग: उस दूध से जमा दही, या दही का ऊपरी भाग (दध्युत्तर)। "
                   "‘तज्जम्’ = तत् + जम्, यानी उससे उत्पन्न; यह ‘दधि’ का विशेषण है। "
                   "दोनों ‘वा’ से जुड़े विकल्प हैं, साथ मिलाकर नहीं। "
                   "दशाएँ: कफ, छर्दि, प्रसेक और सम्भवतः तमक; पर छपा ‘तन्मक’ संदिग्ध है। "
                   "‘दध्युत्तर’ का ठीक अर्थ अनिश्चित है; शब्दशः ‘दही का ऊपरी भाग’।"),
    "hook": "उसी दूध का दही, या दही का ऊपरी भाग।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What does तज्जम् (born of that) describe in unit 19?",
            ("The curd (दधि)", "तज्जम् (n. acc. sg.) goes with दधि: curd born of that milk."),
            [("The gruel (यवागू)", "The gruel is in line 05.01.17."),
             ("The butter (नवनीत)", "Butter comes in line 05.01.20."),
             ("The decoction (क्वाथ)", "No decoction is named in this unit.")],
            "तज्जं वा दधि = or the curd born of that.",
            "तत् + ज = born of that."),
        match(1, "Match each word of unit 19 to its meaning.",
              [["तज्जम्", "born of that"], ["दधि", "curd"], ["दध्युत्तरम्", "upper part of curd"], ["वा", "or"]],
              "Two preparations joined by वा.",
              "तज्जम् = born of that; दधि = curd; दध्युत्तरम् = upper part of curd; वा = or."),
        mcq("extend", 2, "Which is the right split of दध्युत्तरम्?",
            ("दधि + उत्तरम्", "इ before a different vowel becomes य्: दधि + उत्तरम् → दध्युत्तरम्."),
            [("दध्य + उत्तरम्", "अ + उ would give ओ (दध्योत्तरम्)."),
             ("दधे + उत्तरम्", "ए + उ would not give यु."),
             ("दधु + उत्तरम्", "उ + उ would give ऊ (दधूत्तरम्).")],
            "दधि (curd) + उत्तरम् (upper part): इ → य्.",
            "इ/ई + unlike vowel → य् + vowel.",
            teaches="इ before a different vowel becomes य्: दधि + उत्तरम् = दध्युत्तरम्."),
        mcq("discriminate", 3, "Which English rendering of unit 19's two foods has one wrong word?",
            ("Curd born of that, or the lower part of curd", "Wrong: उत्तर is 'upper', not 'lower'."),
            [("Curd born of that, or the upper part of curd", "Correct: this is the card's rendering."),
             ("Curd made from that, or the upper part of curd", "Correct: 'made from' renders तज्ज."),
             ("The curd of that milk, or the curd's upper part", "Correct: only the wording differs.")],
            "दध्युत्तरम् = the upper (उत्तर) part of curd.",
            "उत्तर = upper."),
        multi("apply", 4, "Which two may be given under unit 19?",
              [("Curd born of that milk", "Right: तज्जं दधि."),
               ("Fresh butter from that milk", "Wrong: fresh butter is the formulation of line 05.01.20."),
               ("The upper part of curd", "Right: दध्युत्तरम्."),
               ("The film of the cold milk", "Wrong: the film is the formulation of line 05.01.18.")],
              [0, 2],
              "Unit 19 offers curd or its upper part, as alternatives (वा).",
              "तज्जं दधि वा दध्युत्तरं वा."),
        mcq("transfer", 5, "तत् + जम् → तज्जम्. Join a new example, तत् + जलम् (that water). Which is right?",
            ("तज्जलम्", "त् before ज becomes ज्: तज्जलम्."),
            [("तत्जलम्", "त् does not stay before ज."),
             ("तद्जलम्", "द् would still change to ज् before ज."),
             ("तच्जलम्", "च् comes before च/छ, not before ज.")],
            "Same rule as तत् + जम् = तज्जम्.",
            "त्/द् + ज → ज्ज.",
            teaches="Final त् before ज becomes ज्: तत् + जम् = तज्जम्; तत् + जलम् = तज्जलम्."),
    ],
}

# ---------------------------------------------------------------- unit 20
AUTHORED["20"] = {
    "title": "तस्माद्वा पयसो नवनीतम्",
    "question": "How is the fresh butter of unit 20 cooked, and in which two states is it given?",
    "rule": ("Or the fresh butter (navanīta) produced from that milk, cooked with a decoction of the six beginning with "
             "phala and mixed with the powder of the six phalas: when the fire is overcome by Kapha and the body is drying up."),
    "limits": ("The six (फलादिषट्क, फलषट्) are not listed in this unit, so no question names them. 'That milk' is the milk of "
               "the lines before. Agni = the digestive fire, as the data glosses it. No amount is given."),
    "explain_hi": ("दूध के क्रम का अन्तिम योग: उस दूध से उत्पन्न नवनीत यानी मक्खन। "
                   "इसे फलादि छह के क्वाथ से और छह फलों के चूर्ण को मिलाकर सिद्ध (पकाया) किया जाता है; वे छह यहाँ नहीं गिनाए गए। "
                   "दशाएँ दो हैं: अग्नि यानी पाचन की अग्नि कफ से दबी हो, और शरीर सूख रहा हो। "
                   "‘कफाभिभूतेऽग्नौ’ में कफाभिभूते + अग्नौ है: ए के बाद अ लुप्त होकर ऽ बनता है।"),
    "hook": "दूध का मक्खन, छह फलों से पका: दबी अग्नि, सूखता शरीर।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "What is produced from the milk in unit 20?",
            ("Fresh butter (नवनीत)", "नवनीतम् उत्पन्नम् = fresh butter produced."),
            [("Curd (दधि)", "Curd is the formulation of line 05.01.19."),
             ("Ghee (घृत)", "Ghee is not named in this unit."),
             ("Whey (मस्तु)", "Whey is not named in this unit.")],
            "तस्माद्वा पयसो नवनीतमुत्पन्नम् = or the fresh butter produced from that milk.",
            "नवनीत = fresh butter."),
        match(1, "Match each word of unit 20 to its meaning.",
              [["नवनीत", "fresh butter"], ["उत्पन्न", "produced"], ["सिद्ध", "cooked"], ["अग्नि", "the (digestive) fire"]],
              "What is made, how it is treated, and the fire of the first state.",
              "नवनीत = fresh butter; उत्पन्न = produced; सिद्ध = cooked; अग्नि = fire."),
        order(2, "Put these phrases of unit 20 in the order of the text.",
              ["नवनीतमुत्पन्नम्", "फलादिषट्कक्वाथेन", "फलषट्चूर्णोन्मिश्रेण", "सिद्धम्", "कफाभिभूतेऽग्नौ"],
              "The butter; with the decoction; mixed with the powder; cooked; when the fire is overcome by Kapha.",
              "नवनीतमुत्पन्नं · फलादिषट्कक्वाथेन · फलषट्चूर्णोन्मिश्रेण · सिद्धं · कफाभिभूतेऽग्नौ.",
              role="extend",
              teaches="Unit 20: butter from that milk, cooked with the decoction of the six and mixed with their powder, for fire overcome by Kapha and a drying body."),
        mcq("discriminate", 3, "Which two states does unit 20 name for this butter?",
            ("Fire overcome by Kapha; body drying up", "कफाभिभूतेऽग्नौ शुष्यच्छरीरे च."),
            [("Kapha overcome by fire; body swelling", "The roles are reversed, and swelling is not named."),
             ("Pitta gone into the seat of Kapha", "That state belongs to line 05.01.16."),
             ("Pitta aggravated; chest under thin Kapha", "That state belongs to line 05.01.18.")],
            "Kapha overcomes the fire (कफाभिभूते अग्नौ), and the body is drying (शुष्यच्छरीरे).",
            "Unit 20: कफाभिभूते अग्नौ + शुष्यच्छरीरे."),
        mcq("apply", 4, "Which is the right split of कफाभिभूतेऽग्नौ?",
            ("कफाभिभूते + अग्नौ", "ए + अ → एऽ: the अ is dropped and marked by ऽ."),
            [("कफाभिभूत + अग्नौ", "अ + अ would give आ (कफाभिभूताग्नौ)."),
             ("कफाभिभूतः + अग्नौ", "अः + अ would give ओऽ (कफाभिभूतोऽग्नौ)."),
             ("कफाभिभूतै + अग्नौ", "ऐ + अ would give आय (कफाभिभूतायग्नौ).")],
            "कफाभिभूते (loc. sg.) + अग्नौ (loc. sg.): 'when the fire is overcome by Kapha'.",
            "ए + अ → एऽ."),
        mcq("transfer", 5, "कफाभिभूते + अग्नौ → कफाभिभूतेऽग्नौ. Join a new example, वने + अस्मिन् (in this forest). Which is right?",
            ("वनेऽस्मिन्", "ए + अ → एऽ, as in कफाभिभूतेऽग्नौ."),
            [("वनास्मिन्", "आ would come from अ + अ, not ए + अ."),
             ("वनोऽस्मिन्", "ओऽ comes from अः + अ, not ए + अ."),
             ("वनैस्मिन्", "ऐ is not made from ए + अ.")],
            "Same rule as कफाभिभूते + अग्नौ.",
            "Final ए + अ → एऽ.",
            teaches="A final ए before अ stays, and the अ is dropped and shown by ऽ: कफाभिभूतेऽग्नौ, वनेऽस्मिन्."),
    ],
}

# ---------------------------------------------------------------- unit 21
AUTHORED["21"] = {
    "title": "फलमज्जाचूर्णमिश्रेण लेहम्",
    "question": "How is the lick (leha) of unit 21 made, and which drugs of the āragvadha group are left out?",
    "rule": ("Or use a lick prepared with the decoction of any one of the āragvadha group, excluding ghoṇṭā, bhūnimba and "
             "bāṇa, together with soma-bark and the pañcakolaka, mixed with the powder of the fruit kernel."),
    "limits": ("ससोमवल्कपञ्चकोलकानाम् may also mean 'of those having soma-bark and pañcakolaka'. The āragvadha group is not "
               "listed. IDs: āragvadha standard; ghoṇṭā probable; bhūnimba, somavalka disputed; bāṇa unidentified; "
               "pañcakolaka group standard (cavya probable)."),
    "explain_hi": ("यहाँ से लेह यानी चाटने योग्य योग आते हैं। "
                   "आरग्वध यानी अमलतास आदि द्रव्यों में से किसी एक का क्वाथ लिया जाता है, पर घोण्टा, भूनिम्ब और बाण को छोड़कर। "
                   "साथ में सोमवल्क और पञ्चकोलक (पिप्पली, पिप्पलीमूल, चव्य, चित्रक, सोंठ) हैं; यह ‘सहित’ वाला अंश दो तरह पढ़ा जा सकता है। "
                   "उस क्वाथ से सिद्ध लेह में फल की मज्जा का चूर्ण मिला होता है, और उसका उपयोग करे।"),
    "hook": "अमलतास-समूह का क्वाथ, तीन छोड़कर, गिरी-चूर्ण मिलाकर: लेह।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "What kind of preparation is made in unit 21?",
            ("A lick (लेह)", "लेहम् उपयुञ्जीत = one should use a lick."),
            [("A sweet ball (मोदक)", "The modaka comes in line 05.01.22."),
             ("A gruel (यवागू)", "The gruel is in line 05.01.17."),
             ("A cake (शष्कुली)", "Cakes come in line 05.01.23.")],
            "लेह = a lick, an electuary.",
            "लेहम् उपयुञ्जीत = use the lick."),
        match(1, "Match each word of unit 21 to its meaning.",
              [["आरग्वध", "golden shower tree"], ["वर्ज्य", "to be left out"], ["लेह", "a lick, electuary"],
               ["उपयुञ्जीत", "one should use"]],
              "The head of the drug group, the exclusion, the preparation and the verb.",
              "आरग्वध = golden shower tree; वर्ज्य = excluded; लेह = lick; उपयुञ्जीत = one should use."),
        order(2, "Put the three excluded drugs of unit 21 in the order of the text.",
              ["घोण्टा", "भूनिम्ब", "बाण"],
              "घोण्टाभूनिम्बबाणवर्ज्यानाम् = excluding ghoṇṭā, bhūnimba and bāṇa.",
              "घोण्टा · भूनिम्ब · बाण.",
              role="extend",
              teaches="Unit 21 leaves three of the āragvadha group out: ghoṇṭā, bhūnimba and bāṇa."),
        mcq("discriminate", 3, "What does -वर्ज्यानाम् say about ghoṇṭā, bhūnimba and bāṇa?",
            ("They are left out of the group", "वर्ज्य = to be avoided, excluded."),
            [("They alone are to be used", "That would reverse the sense of वर्ज्य."),
             ("They are to be used doubled", "Nothing about doubling is said."),
             ("They are to be added as powder", "The powder added is of the fruit kernel.")],
            "आरग्वधादि … घोण्टाभूनिम्बबाणवर्ज्यानाम् = of the āragvadha group, excluding these three.",
            "X-वर्ज्य = excluding X."),
        mcq("apply", 4, "A helper cooks the lick in an āragvadha decoction but adds nothing else. What does unit 21 still require?",
            ("Mixing in the fruit-kernel powder", "फलमज्जाचूर्णमिश्रेण = mixed with the powder of the fruit kernel."),
            [("Steeping it in its own decoction", "Steeping in its own decoction is the step of line 05.01.15."),
             ("Cooling it in a dust-free pot", "The dust-free pot is for storage in line 05.01.11."),
             ("Pressing it with sesame flour", "Sesame flour belongs to line 05.01.23.")],
            "The lick is cooked in one decoction and mixed with the fruit-kernel powder.",
            "Lick = decoction of one of the group + fruit-kernel powder."),
        mcq("transfer", 5, "X-वर्ज्य means excluding X. What does a new phrase निम्बवर्ज्यानाम् (with निम्ब = neem) mean?",
            ("Of those excluding neem", "निम्ब + वर्ज्य: neem is left out."),
            [("Of neem alone", "'Alone' would need मात्र or एव."),
             ("Of those with neem", "'With' would be स- (सनिम्ब)."),
             ("Of those resembling neem", "'Resembling' would need वत् or सदृश.")],
            "Same build as घोण्टाभूनिम्बबाणवर्ज्यानाम्.",
            "X-वर्ज्य = excluding X; स-X = with X.",
            teaches="-वर्ज्य at the end of a compound means 'excluding': घोण्टाभूनिम्बबाणवर्ज्य, निम्बवर्ज्य."),
    ],
}

# ---------------------------------------------------------------- unit 22
AUTHORED["22"] = {
    "title": "रेणुकैलाशताह्वा … द्वाविंशतेरन्यतरस्य",
    "question": "What may one eat in unit 22, and with which decoction is it prepared?",
    "rule": ("Or, mixed with the fruit-kernel powder, one should eat an utkārikā or a modaka prepared with the decoction of "
             "any one of twenty-two named drugs, from reṇukā and elā (small cardamom) to aśoka and rohiṇī."),
    "limits": ("Low confidence: the scan is damaged; koraka, paripelava, sthauṇeyaka, pāledhana and pūti are unidentified, "
               "and पालेधन is flagged. शतावहा is printed for शताह्वा. The division into 22 is a guess. Only the clear names are questioned."),
    "explain_hi": ("इस इकाई में फल की मज्जा के चूर्ण से मिली उत्कारिका (पकाया हुआ एक व्यंजन) या मोदक (लड्डू जैसा गोला) खाने को कहा गया है। "
                   "उसे बाईस द्रव्यों में से किसी एक के काढ़े से सिद्ध किया जाता है। "
                   "स्पष्ट नामों में हैं: एला यानी छोटी इलायची, कुस्तुम्बुरु यानी धनिया, तगर, कुष्ठ यानी कूठ, मरुवक यानी मरुआ, अगुरु यानी अगर, "
                   "गुग्गुलु, मांसी यानी जटामांसी और शैलेयक यानी छरीला। "
                   "स्कैन क्षतिग्रस्त है: कुछ नाम अज्ञात हैं और बाईस की गिनती का बँटवारा अनुमान है।"),
    "hook": "बाईस में से एक का काढ़ा: उत्कारिका या मोदक, गिरी-चूर्ण मिलाकर।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What may one eat under unit 22?",
            ("An utkārikā or a modaka", "उत्कारिकां मोदकं वा भक्षयेत्."),
            [("A lick or a gruel", "The lick is the formulation of line 05.01.21."),
             ("Śaṣkulī or apūpa cakes", "These cakes come in line 05.01.23."),
             ("Curd or its upper part", "Curd is the formulation of line 05.01.19.")],
            "उत्कारिका = a cooked preparation; मोदक = a ball-shaped sweet.",
            "उत्कारिकां मोदकं वा भक्षयेत्."),
        order(1, "Put these drugs of unit 22's list in the order of the text.",
              ["एला", "कुस्तुम्बुरु", "तगर", "कुष्ठ", "अगुरु", "गुग्गुलु"],
              "Cardamom, coriander, tagara, costus, agarwood, guggul (other names stand between some of them).",
              "एला · कुस्तुम्बुरु · तगर · कुष्ठ · … · अगुरु · गुग्गुलु."),
        match(2, "Match each drug of unit 22 to its identification in the card.",
              [["एला", "small cardamom"], ["कुस्तुम्बुरु", "coriander"], ["अगुरु", "agarwood"], ["मांसी", "spikenard"]],
              "Four clear names of the list; the data calls these identifications standard.",
              "एला = small cardamom; कुस्तुम्बुरु = coriander; अगुरु = agarwood; मांसी = spikenard.",
              role="extend",
              teaches="Among unit 22's drugs: एला (small cardamom), कुस्तुम्बुरु (coriander), अगुरु (agarwood), मांसी (spikenard)."),
        mcq("discriminate", 3, "Which is the right split of रेणुकैला- at the head of the list?",
            ("रेणुका + एला", "आ + ए → ऐ: रेणुका + एला → रेणुकैला."),
            [("रेणुके + एला", "ए + ए would not give ऐ (it gives अ ए or अये)."),
             ("रेणुको + एला", "ओ + ए would give अवे (रेणुकवेला)."),
             ("रेणुकि + एला", "इ + ए would give ये (रेणुक्येला).")],
            "The first two drugs: reṇukā and elā (small cardamom).",
            "अ/आ + ए/ऐ → ऐ."),
        mcq("apply", 4, "A modaka is cooked in a decoction of elā alone and mixed with kernel powder. Does this follow unit 22?",
            ("Yes: any one of the drugs will do", "अन्यतरस्य = of any one; elā is named."),
            [("No: all of the drugs are needed together", "The text asks for any one, not all together."),
             ("No: elā is one of those excluded", "Exclusion belongs to line 05.01.21; elā is in this list."),
             ("No: only liquorice may be used", "Liquorice heads the list of line 05.01.12, not this one.")],
            "One decoction, of any one of the named drugs, plus the fruit-kernel powder.",
            "Decoction of any one (अन्यतर) of the list."),
        mcq("transfer", 5, "रेणुका + एला → रेणुकैला. Join a new example, सदा + एव (at all times indeed). Which is right?",
            ("सदैव", "आ + ए → ऐ, as in रेणुका + एला."),
            [("सदेव", "ए would come from अ/आ + इ, not + ए."),
             ("सदाएव", "The two vowels do not stay side by side."),
             ("सदोव", "ओ comes from अ/आ + उ.")],
            "Same rule as रेणुका + एला = रेणुकैला.",
            "अ/आ + ए/ऐ → ऐ.",
            teaches="अ or आ before ए or ऐ becomes ऐ: रेणुका + एला = रेणुकैला; सदा + एव = सदैव."),
    ],
}

# ---------------------------------------------------------------- unit 23
AUTHORED["23"] = {
    "title": "शष्कुलीरपूपानन्यं वा भक्ष्यम्",
    "question": "What foods does unit 23 have made from sesame and rice flour, and with which decoctions?",
    "rule": ("With ground sesame (tila) and śāli rice, pressed with the juice and decoction of fruit-pippalī and mixed with "
             "its decoction, or mixed with the decoction of any one of the surasā group, prepare śaṣkulī or apūpa cakes or "
             "another food, and eat it."),
    "limits": ("परिपीडत is printed for परिपीडित (pressed); that word is not questioned. The surasā group is not listed here. "
               "Śaṣkulī and apūpa are kinds of cakes; their exact recipes are not given. Śāli = winter rice."),
    "explain_hi": ("इस इकाई में भक्ष्य यानी खाने की वस्तुएँ बनती हैं। "
                   "तिल और शालि यानी अगहनी धान के चावल का पिसा आटा फल-पिप्पली के स्वरस और काढ़े से दबाया जाता है। "
                   "फिर उसे उसी के काढ़े से, या सुरसा यानी तुलसी आदि द्रव्यों में से किसी एक के क्वाथ से मिलाया जाता है। "
                   "उससे शष्कुली, अपूप (दोनों पकवान के प्रकार) या कोई और भक्ष्य बनाकर खाए।"),
    "hook": "तिल-चावल का आटा, फल-पिप्पली या सुरसा के काढ़े से: शष्कुली, अपूप, और भक्ष्य।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "Which foods does unit 23 have prepared and eaten?",
            ("Śaṣkulī, apūpa or another food", "शष्कुलीः अपूपान् अन्यं वा भक्ष्यम्."),
            [("A lick or a mixed drink", "The lick belongs to line 05.01.21."),
             ("An utkārikā or a modaka", "These belong to line 05.01.22."),
             ("A gruel cooked in milk", "The gruel belongs to line 05.01.17.")],
            "शष्कुली and अपूप are cakes; अन्यं भक्ष्यम् = another food.",
            "शष्कुलीरपूपानन्यं वा भक्ष्यम्."),
        match(1, "Match each word of unit 23 to its meaning.",
              [["तिल", "sesame"], ["शालि", "winter rice"], ["शष्कुली", "a kind of cake"], ["भक्ष्य", "food"]],
              "The two grains of the flour and what is made from it.",
              "तिल = sesame; शालि = winter rice; शष्कुली = a cake; भक्ष्य = food."),
        order(2, "Put these steps of unit 23 in the order of the text.",
              ["तिल और शालि का आटा", "काढ़े से मिलाना (उपसृष्ट)", "भक्ष्य बनाना (साधयित्वा)", "खाना (भक्षयेत्)"],
              "Flour, mixed with a decoction, made into a food, eaten.",
              "तिलशालितण्डुलपिष्टैः · …उपसृष्टैः · साधयित्वा · भक्षयेत्.",
              role="extend",
              teaches="Unit 23 runs: sesame and rice flour, mixed with a decoction, made into cakes or another food, then eaten."),
        mcq("discriminate", 3, "Which other decoction may the flour be mixed with in unit 23?",
            ("Of any one of the surasā group", "सुरसादिद्रव्यान्यतमनिर्यूहोपसृष्टैः."),
            [("Of any one of the kovidāra group", "The kovidāra group belongs to line 05.01.15."),
             ("Of any one of the jīmūtaka group", "The jīmūtaka group belongs to line 05.01.16."),
             ("Of any one of the āragvadha group", "The āragvadha group belongs to line 05.01.21.")],
            "Either its own (fruit-pippalī) decoction, or that of one drug of the surasā group.",
            "Unit 23: तत्कषाय or सुरसादि-निर्यूह."),
        mcq("apply", 4, "What does साधयित्वा भक्षयेत् tell the cook to do?",
            ("Prepare it, then eat it", "साधयित्वा = having prepared; भक्षयेत् = one should eat."),
            [("Eat it, then prepare more", "The absolutive साधयित्वा comes first: prepare, then eat."),
             ("Prepare it, but keep it", "भक्षयेत् says it is eaten."),
             ("Have another person cook it", "No causative 'have cooked' is used here.")],
            "An absolutive (-त्वा) names the earlier act; the optative names the main one.",
            "X-त्वा + verb = having done X, one should …"),
        mcq("transfer", 5, "पिष्टैः + तत्- → पिष्टैस्तत्-. Join a new example, बालैः + तत्र (by the boys there). Which is right?",
            ("बालैस्तत्र", "A visarga before त becomes स्."),
            [("बालैर्तत्र", "र् comes before a voiced sound, not before त."),
             ("बालैश्तत्र", "श् comes before च/छ/श, not before त."),
             ("बालौ तत्र", "The ending ऐः does not change to औ.")],
            "Same rule as पिष्टैः + तत्कषाय → पिष्टैस्तत्कषाय.",
            "Visarga + त/थ → स्.",
            teaches="A visarga before त or थ becomes स्: पिष्टैः + तत् = पिष्टैस्तत्; बालैः + तत्र = बालैस्तत्र."),
    ],
}

# ---------------------------------------------------------------- unit 24
AUTHORED["24"] = {
    "title": "आदर्वीप्रलेपात्पक्त्वा लेहयेत्",
    "question": "How is the fruit-pippalī juice of unit 24 cooked, and how is it given?",
    "rule": ("Or the juice of the fruit-pippalīs, as in the bhallātaka (marking nut) procedure, cooked until it coats the "
             "ladle: one should have it licked."),
    "limits": ("The bhallātaka procedure is described elsewhere and is not given here. श्रुतम् is glossed 'as heard'; "
               "it might also be read as शृतम् (boiled), so no question rests on that word. No amount is given."),
    "explain_hi": ("फल-पिप्पलियों का स्वरस यानी ताज़ा निचोड़ा रस लिया जाता है। "
                   "उसे भल्लातक यानी भिलावा की विधि के अनुसार पकाया जाता है; वह विधि यहाँ नहीं दी गई। "
                   "पकाने की सीमा: जब तक वह दर्वी यानी कलछी पर लेप की तरह न चढ़ने लगे (आ + पञ्चमी = तक)। "
                   "फिर रोगी को चटाए; ‘लेहयेत्’ प्रेरणार्थक है।"),
    "hook": "रस पकाओ जब तक कलछी पर चढ़े, फिर चटाओ।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "Until when is the juice cooked in unit 24?",
            ("Until it coats the ladle", "आदर्वीप्रलेपात् = until it coats the ladle."),
            [("Until half of it is left", "No fraction is named in the unit."),
             ("Until it turns quite black", "No colour is named in the unit."),
             ("Until it starts to froth", "Froth is not named in the unit.")],
            "आ + दर्वी-प्रलेपात् = up to the ladle's coating.",
            "आदर्वीप्रलेपात् = until it coats the ladle."),
        match(1, "Match each word of unit 24 to its meaning.",
              [["स्वरस", "juice"], ["दर्वी", "ladle"], ["प्रलेप", "coating"], ["पक्त्वा", "having cooked"]],
              "The juice, the test of cooking and the act.",
              "स्वरस = juice; दर्वी = ladle; प्रलेप = coating; पक्त्वा = having cooked."),
        order(2, "Put these words of unit 24 in the order of the text.",
              ["फलपिप्पलीनाम्", "स्वरसम्", "आदर्वीप्रलेपात्", "पक्त्वा", "लेहयेत्"],
              "Of the fruit-pippalīs, the juice, until it coats the ladle, having cooked, have it licked.",
              "फलपिप्पलीनां · (भल्लातकविधि…) · स्वरसम् · आदर्वीप्रलेपात् · पक्त्वा · लेहयेत्.",
              role="extend",
              teaches="Unit 24: the fruit-pippalī juice is cooked until it coats the ladle, and then given to lick."),
        mcq("discriminate", 3, "What does the causative लेहयेत् say, as against plain लिहेत्?",
            ("One should have it licked", "Causative: someone (the patient) is made to lick."),
            [("One should lick it oneself", "That would be the plain लिहेत्."),
             ("One should not lick it at all", "No negation (न) is present."),
             ("One should mix it into food", "Mixing into food is the next line's option.")],
            "लेहयेत् = causative optative of √लिह्: have (him) lick.",
            "Causative = cause another to do."),
        mcq("apply", 4, "A helper stops cooking while the juice is still thin and runs off the ladle. What does unit 24 require?",
            ("Cook on until it coats the ladle", "The end point is आदर्वीप्रलेपात्."),
            [("Strain it and give it at once", "Straining is not a step of this unit."),
             ("Add honey and stop there", "Honey is not named in this unit."),
             ("Pour it into a new pot", "The pot belongs to line 05.01.11.")],
            "Cooking ends only when the juice coats the ladle.",
            "आ + ablative = until."),
        mcq("transfer", 5, "आदर्वीप्रलेपात् uses आ + ablative for until. What does a new word आमरणात् (मरण = death) mean?",
            ("Until death", "आ + ablative = up to, until."),
            [("From death on", "आ here marks the limit reached, not a starting point."),
             ("Without death", "'Without' would need a negative like अ- or निर्-."),
             ("Because of death", "आ + ablative is the limit, not the cause.")],
            "आ + दर्वीप्रलेपात् = until the ladle-coating; आ + मरणात् = until death.",
            "आ + ablative = until.",
            teaches="आ with an ablative means 'until': आदर्वीप्रलेपात् (until it coats the ladle), आमरणात् (until death)."),
    ],
}

# ---------------------------------------------------------------- unit 25
AUTHORED["25"] = {
    "title": "अन्नपानेषु वा तं लेहमवचारयेत्",
    "question": "What two further ways of giving the lick and its decoctions does verse 25 state?",
    "rule": ("Or one should mix that lick into foods and drinks; and one should prepare foods and drinks with its "
             "decoctions alone."),
    "limits": ("अवचारयेत् is taken as 'administer, mix in'; its exact English wording is an open glossary point. "
               "'That lick' is the lick of the lines before. The verse names no particular food, drink or amount."),
    "explain_hi": ("यह श्लोक लेह देने के दो और तरीके बताता है। "
                   "पहली पंक्ति: उस लेह को अन्न और पान (खाने और पीने की चीज़ों) में मिलाकर दे। "
                   "दूसरी पंक्ति: उसके काढ़ों से ही अन्न और पान तैयार करे; ‘एव’ का अर्थ है ‘ही’। "
                   "‘अवचारयेत्’ का शब्दशः भाव ‘भीतर चलाना’ है, यानी मिलाना या देना; ठीक शब्द अभी खुला है।"),
    "hook": "लेह को खाने-पीने में मिलाओ, या उसके काढ़े से ही खाना-पीना बनाओ।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "Into what does verse 25 have the lick mixed?",
            ("Foods and drinks (अन्नपान)", "अन्नपानेषु … लेहम् अवचारयेत्."),
            [("Cold water alone", "Water is not named in the verse."),
             ("A pot of fresh curd", "Curd is not named in the verse."),
             ("A paste for the skin", "No outward use is named.")],
            "अन्नपानेषु = in foods and drinks.",
            "अन्नपानेषु वा तं लेहमवचारयेत्."),
        match(1, "Match each word of verse 25 to its meaning.",
              [["अन्न", "food"], ["पान", "drink"], ["कषाय", "decoction"], ["एव", "alone, indeed"]],
              "The two kinds of fare, what they are made with, and the stress word.",
              "अन्न = food; पान = drink; कषाय = decoction; एव = alone."),
        order(2, "Put the words of the first line in the order of the verse.",
              ["अन्नपानेषु", "वा", "तम्", "लेहम्", "अवचारयेत्"],
              "In foods and drinks, or, that, lick, one should mix in.",
              "अन्नपानेषु · वा · तं · लेहम् · अवचारयेत्.",
              role="extend",
              teaches="Line 1 of verse 25: अन्नपानेषु वा तं लेहमवचारयेत् (or mix that lick into foods and drinks)."),
        mcq("discriminate", 3, "In line 2, what are the foods and drinks prepared with?",
            ("With its decoctions alone", "तत्कषायैः एव = with its decoctions alone."),
            [("With plain water alone", "Water is not named in the verse."),
             ("With milk and fresh butter", "Milk and butter are not named in the verse."),
             ("With honey and cold milk", "Neither honey nor milk is named here.")],
            "तत्कषायैरेव च अन्नपानानि कल्पयेत्.",
            "तत्कषायैः एव = with its decoctions alone."),
        mcq("apply", 4, "Which is the right split of चान्नपानानि?",
            ("च + अन्नपानानि", "अ + अ → आ: च + अन्न → चान्न."),
            [("चः + अन्नपानानि", "अः + अ would give ओऽ (चोऽन्न)."),
             ("चे + अन्नपानानि", "ए + अ would give एऽ (चेऽन्न)."),
             ("चम् + अन्नपानानि", "म् + अ would give म (चमन्न).")],
            "च (and) + अन्नपानानि (foods and drinks).",
            "अ + अ → आ."),
        mcq("transfer", 5, "लेहम् + अवचारयेत् → लेहमवचारयेत्. Join a new example, फलम् + अश्नाति (he eats the fruit). Which is right?",
            ("फलमश्नाति", "Final म् before a vowel joins the vowel."),
            [("फलंश्नाति", "Anusvara stands before a consonant, not before a vowel."),
             ("फलाश्नाति", "The म् is not dropped."),
             ("फलोश्नाति", "ओ is not made from म् + अ.")],
            "Same rule as लेहम् + अवचारयेत् = लेहमवचारयेत्.",
            "Final म् + vowel → म joined to the vowel.",
            teaches="A final म् before a vowel stays म् and joins it: लेहमवचारयेत्, फलमश्नाति."),
    ],
}


NOTES_HI = {
    "12": ("विश्वास: निम्न। ‘अन्तर्मुखमुष्टि’ (भीतर की ओर मुँह वाली मुट्ठी) एक माप हो सकता है, अर्थ अनिश्चित; छपा अर्थ रखा गया। "
           "‘कषाये’ के बाद का दूसरा ‘वा’ दो तरह पढ़ा जा सकता है (‘अथवा रात भर रखा …’ या उसी काढ़े में रात भर रखा); इस पर प्रश्न नहीं बना। "
           "‘फलपिप्पली’ = सम्भवतः मैनफल के सूखे टुकड़े (पंक्ति 05.01.11 देखें)। "
           "खुला बिन्दु (05.01.12): कर्बुदार की पहचान ‘सम्भावित’ से ‘विवादित’ होनी चाहिए; इस पर प्रश्न नहीं बना। "
           "सन्धि जाँची: फलपिप्पलीनामन्तर्मुख… = …नाम् + अन्तर्मुख…; यावद्वा = यावत् + वा (त् → द्); प्रत्यक्पुष्प्यन्यतम = प्रत्यक्पुष्पी + अन्यतम (ई → य्); रात्रिमुषितम् = रात्रिम् + उषितम्।"),
    "13": ("विश्वास: निम्न। यह पंक्ति 05.01.12 का वाक्य आगे बढ़ाती है; अपनी क्रिया नहीं। "
           "‘श्लेष्मज्वर’ को ‘कफ और ज्वर’ या ‘कफ-ज्वर’ दोनों पढ़ा जा सकता है। "
           "‘पुनरापित्तगमनात्’ अस्पष्ट है (‘फिर, पित्त के आने तक’?); इस पर प्रश्न नहीं बना। "
           "सन्धि जाँची: प्रतिश्यायान्तर्विद्रधिषु = प्रतिश्याय + अन्तर्विद्रधिषु (अ + अ → आ); पुनरापित्त = पुनः + आपित्त (विसर्ग → र्)।"),
    "14": ("विश्वास: उच्च। कोई सन्धि-समस्या, पाठभेद या चिह्नित दोष नहीं। ‘तेन’ पिछली पंक्तियों के पेय की ओर संकेत करता है, यह क्रम से समझा गया है।"),
    "15": ("विश्वास: मध्यम। छपा ‘त्विफला’ मुद्रण-दोष है, पाठ ‘त्रिफला’ (चिह्नित); इस शब्द पर प्रश्न नहीं बना। "
           "‘त्रिभाग’ = तीन भाग, या ‘तीसरा भाग’ भी हो सकता है। "
           "छपाई में ‘ज्वरोदरा रोचकेषु’ के बीच का खाली स्थान सन्धि (उदर + अरोचकेषु, अ + अ → आ) को तोड़ता है; इस पर प्रश्न नहीं बना। "
           "‘बलवत्’ केवल कफ का या सब दशाओं का विशेषण हो सकता है। "
           "खुला बिन्दु (05.01.15): प्रसेक का अर्थ ‘बहना, टपकना’ रखना है, ‘लार’ जोड़ना अतिरिक्त है; प्रसेक के अर्थ पर प्रश्न नहीं बना। "
           "सन्धि जाँची: कोविदारादि = कोविदार + आदि; …कफप्रसेकापच्यर्बुद… = …प्रसेक + अपची + अर्बुद (ई → य्)।"),
    "16": ("विश्वास: मध्यम। ‘मज्जा’ = भीतरी गिरी (शब्दशः गूदा या मज्जा)। इकाई में क्रिया नहीं, वाक्य अधूरा (लुप्त क्रिया) है। "
           "जीमूतक आदि का समूह यहाँ नहीं गिनाया गया। सन्धि जाँची: जीमूतकादि = जीमूतक + आदि (अ + आ → आ)।"),
    "17": ("विश्वास: मध्यम। ‘अधोभागे’ रक्तपित्त के साथ (नीचे के मार्ग से रक्तस्राव) या दूध के निचले भाग के साथ पढ़ा जा सकता है; पहला अर्थ अनुवाद में है, प्रश्न किसी पर नहीं बना। "
           "‘मज्ज’ को ‘मज्जा’ का रूप माना गया। "
           "सन्धि जाँची: पयस्तस्मिन् = पयः + तस्मिन् (विसर्ग + त → स्त); यवागूमधोभागे = यवागूम् + अधोभागे; हृद्दाहे = हृत् + दाहे (त् → द्)।"),
    "18": ("विश्वास: मध्यम। ‘सन्तानिका’ = दूध पर जमने वाली परत (मलाई)। छपे ‘संतानिकांऽजलिं’ में अवग्रह असामान्य है (सन्तानिकाम् + अञ्जलिम्); इस पर प्रश्न नहीं बना। "
           "‘उरःकण्ठहृदये’ को द्वन्द्व, सप्तमी, ‘उपादिग्धे’ के साथ पढ़ा गया। "
           "सन्धि जाँची: तनुकफोपादिग्धे = तनुकफ + उपादिग्धे (अ + उ → ओ)।"),
    "19": ("विश्वास: मध्यम। छपा ‘तन्मक’ सम्भवतः ‘तमक’ है (चिह्नित, सम्भव मुद्रण-दोष); इसलिए रोग-सूची वाले शब्द पर प्रश्न नहीं बना। "
           "‘दध्युत्तर’ का शब्दशः अर्थ ‘दही का ऊपरी भाग’ है; ठीक भाव अनिश्चित। "
           "सन्धि जाँची: तज्जम् = तत् + जम् (त् + ज → ज्ज); दध्युत्तरम् = दधि + उत्तरम् (इ → य्); कफच्छर्दि = कफ + छर्दि (छ से पहले च्)।"),
    "20": ("विश्वास: मध्यम। ‘फलादिषट्क’ और ‘फलषट्’ (छह फल) इस इकाई में नहीं गिनाए गए; उनके नामों पर प्रश्न नहीं बना। "
           "सन्धि जाँची: तस्माद्वा = तस्मात् + वा (त् → द्); पयसो नवनीतम् = पयसः + नवनीतम् (अः + घोष → ओ); "
           "नवनीतमुत्पन्नम् = नवनीतम् + उत्पन्नम्; …चूर्णोन्मिश्रेण = चूर्ण + उन्मिश्रेण (अ + उ → ओ); कफाभिभूतेऽग्नौ = कफाभिभूते + अग्नौ (ए + अ → एऽ); "
           "शुष्यच्छरीरे = शुष्यत् + शरीरे (त् + श → च्छ)।"),
    "21": ("विश्वास: मध्यम। ‘वाऽऽरग्वध’ में दोहरा अवग्रह दीर्घ आ (वा + आरग्वध) दिखाता है, छपाई की रीति। "
           "‘ससोमवल्कपञ्चकोलकानाम्’ को ‘सोमवल्क और पञ्चकोलक सहित’ या ‘जिनमें सोमवल्क और पञ्चकोलक हैं’ दोनों पढ़ा जा सकता है। "
           "पहचान: आरग्वध मानक, घोण्टा सम्भावित, भूनिम्ब और सोमवल्क विवादित, बाण अज्ञात; पञ्चकोलक समूह मानक (चव्य सम्भावित)। "
           "सन्धि जाँची: लेहमुपयुञ्जीत = लेहम् + उपयुञ्जीत; …कोलकानामन्यतमस्य = …नाम् + अन्यतमस्य।"),
    "22": ("विश्वास: निम्न। स्कैन क्षतिग्रस्त; बाईस की गिनती तभी बैठती है जब ‘पालेधन’ एक नाम और ‘त्वक्’ तथा ‘कोरक’ दो नाम हों; बँटवारा अनुमान है। "
           "चिह्नित: ‘पालेधन’ पहचाना हुआ नाम नहीं (सुझाया ‘पालीधन’ भी अनिश्चित)। "
           "खुला बिन्दु (05.01.22): छपा ‘शतावहा’ (अक्षर उलटे), शब्द-सूची में ‘शताह्वा’ बिना चिह्न के लिया गया। "
           "खुला बिन्दु (05.01.22): उत्कारिका और मोदक का अधिक वर्णन नहीं जोड़ा गया। "
           "कोरक, परिपेलव, स्थौणेयक, पालेधन, पूति अज्ञात; प्रश्न केवल स्पष्ट नामों पर बने। "
           "सन्धि जाँची: रेणुकैला = रेणुका + एला (आ + ए → ऐ); द्वाविंशतेरन्यतरस्य = द्वाविंशतेः + अन्यतरस्य (विसर्ग → र्); साधितामुत्कारिकाम् = साधिताम् + उत्कारिकाम्।"),
    "23": ("विश्वास: मध्यम। छपा ‘परिपीडत’ मुद्रण-दोष है, पाठ ‘परिपीडित’ (चिह्नित); इस शब्द पर प्रश्न नहीं बना। "
           "‘शष्कुली’ और ‘अपूप’ पकवान के प्रकार हैं; ‘तिल’ = तिल (मानक)। "
           "सन्धि जाँची: पिष्टैस्तत्कषाय = पिष्टैः + तत्कषाय (विसर्ग + त → स्त); शष्कुलीरपूपान् = शष्कुलीः + अपूपान् (ईः + स्वर → ईर्); "
           "अपूपानन्यम् = अपूपान् + अन्यम्; …उपसृष्टैर्वा = उपसृष्टैः + वा (विसर्ग + घोष → र्)।"),
    "24": ("विश्वास: मध्यम। ‘भल्लातकविधि’ कहीं और कही गई विधि है, यहाँ नहीं दी गई। "
           "‘श्रुतम्’ को ‘सुने अनुसार’ पढ़ा गया; ‘शृतम्’ (उबाला हुआ) पाठ भी सम्भव लगता है (मेरा अवलोकन, डेटा में चिह्नित नहीं); इस शब्द पर प्रश्न नहीं बना। "
           "सन्धि जाँची: स्वरसमादर्वी = स्वरसम् + आदर्वी; …प्रलेपात्पक्त्वा = …प्रलेपात् + पक्त्वा।"),
    "25": ("विश्वास: मध्यम। दो पंक्तियाँ (05.01.25, 05.01.26)। ‘अवचारयेत्’ = ‘भीतर चलाए’, यानी मिलाए या दे; अंग्रेज़ी शब्द का चुनाव शब्दकोश में खुला है। "
           "सन्धि जाँची: लेहमवचारयेत् = लेहम् + अवचारयेत्; तत्कषायैरेव = तत्कषायैः + एव (विसर्ग → र्); चान्नपानानि = च + अन्नपानानि (अ + अ → आ)।"),
}


AIDS = {
    "12": {
        "chain": {"steps": ["प्रयोग के समय", "मुट्ठी भर फल-पिप्पली (या जितनी ठीक लगे)", "दरदरी कूटे (जर्जरीकृत्य)",
                            "नौ में से एक के काढ़े में", "सूत्रस्थान की विधि से पिलाए (पाययेत्)"]},
        "diagram": {"groups": [{"label": "काढ़ा: इनमें से कोई एक (सूची-क्रम)",
                                "items": ["यष्टीमधुक", "कोविदार", "कर्बुदार", "नीप", "विदुल", "बिम्बी",
                                          "शणपुष्पी", "सदापुष्पी", "प्रत्यक्पुष्पी"]}]},
        "anchors": "जर्जरीकृत्य = दरदरा कूटकर · अन्यतम = इनमें से कोई एक · पूत = छाना हुआ · पाययेत् = पिलाए।",
    },
    "13": {
        "chunks": "श्लेष्मज्वरगुल्मप्रतिश्यायान्तर्विद्रधिषु | विशेषेण | पुनरापित्तगमनात्।",
        "frame": "किनमें: कफ, ज्वर, गुल्म, जुकाम, भीतरी फोड़ा · कैसे: विशेष रूप से · कब तक: पित्त के आने तक (अस्पष्ट)।",
        "anchors": "गुल्म = पेट की गाँठ · प्रतिश्याय = जुकाम · विद्रधि = फोड़ा · विशेषेण = विशेष रूप से।",
    },
    "14": {
        "chunks": "तेन | साधु | वमति।",
        "contrast": "वमति = वमन करता है (वर्तमान) · वमेत् = वमन करे (विधिलिङ्) · पाययेत् = पिलाए (प्रेरणार्थक)।",
        "anchors": "तेन = उससे · साधु = भली प्रकार · वमति = वमन करता है।",
    },
    "15": {
        "chain": {"steps": ["फल-पिप्पली का चूर्ण", "अपने क्वाथ में भावित", "तीन भाग त्रिफला-चूर्ण के साथ",
                            "कोविदार आदि के काढ़े से", "पिए (पिबेत्)"]},
        "diagram": {"groups": [{"label": "दशाएँ (सूची-क्रम)",
                                "items": ["प्रबल कफ", "प्रसेक", "अपची", "अर्बुद", "ग्रन्थि", "ज्वर", "उदर", "अरोचक"]}]},
        "anchors": "स्व = अपना · भावित = भिगोया · निर्यूह = काढ़ा · अर्बुद = ट्यूमर · ग्रन्थि = गाँठ · अरोचक = अरुचि।",
    },
    "16": {
        "frame": "क्या: मैनफल की गिरी का चूर्ण · किसके साथ: जीमूतक आदि का काढ़ा · कब: जब पित्त कफ के स्थान में गया हो।",
        "contrast": "पंक्ति 05.01.15: कोविदार आदि का काढ़ा · यह इकाई: जीमूतक आदि का काढ़ा।",
        "anchors": "मज्जा = भीतरी गिरी · चूर्ण = पाउडर · कफस्थानगत = कफ के स्थान में गया।",
    },
    "17": {
        "chain": {"steps": ["मैनफल की गिरी से दूध सिद्ध करे", "या उसी दूध में यवागू", "रक्तपित्त में", "हृदय की जलन में"]},
        "frame": "क्या: गिरी से सिद्ध दूध, या उसमें यवागू · किनमें: रक्तपित्त, हृदय की जलन · अनिश्चित: ‘अधोभागे’ किससे जुड़ा।",
        "anchors": "सिद्ध = पकाया हुआ · पयः = दूध · यवागू = गाढ़ी लपसी · हृद्दाह = हृदय की जलन।",
    },
    "18": {
        "chunks": "तस्य वा पयसः शीतस्य | सन्तानिकाम् अञ्जलिम् | पित्ते प्रकुपिते | उरःकण्ठहृदये च तनुकफोपादिग्धे।",
        "frame": "क्या: ठंडे दूध की मलाई · कितनी: एक अञ्जलि · कब: पित्त कुपित हो, और छाती-कण्ठ-हृदय पतले कफ से लिप्त हों।",
        "sandhi": "अ + उ → ओ: तनुकफ + उपादिग्धे → तनुकफोपादिग्धे।",
    },
    "19": {
        "chunks": "तज्जं वा दधि | दध्युत्तरं वा | कफच्छर्दिप्रसेकतन्मकेषु।",
        "sandhi": "त् + ज → ज्ज: तत् + जम् → तज्जम्; इ + उ → यु: दधि + उत्तरम् → दध्युत्तरम्।",
        "anchors": "तज्ज = उससे उत्पन्न · दधि = दही · उत्तर = ऊपरी · छर्दि = उल्टी।",
    },
    "20": {
        "chain": {"steps": ["उस दूध से नवनीत", "फलादि छह के क्वाथ से", "छह फलों का चूर्ण मिलाकर", "सिद्ध करे",
                            "जब अग्नि कफ से दबी हो और शरीर सूख रहा हो"]},
        "sandhi": "ए + अ → एऽ: कफाभिभूते + अग्नौ → कफाभिभूतेऽग्नौ; त् + श → च्छ: शुष्यत् + शरीरे → शुष्यच्छरीरे।",
        "anchors": "नवनीत = मक्खन · उत्पन्न = बना · अभिभूत = दबा हुआ · शुष्यत् = सूखता हुआ।",
    },
    "21": {
        "contrast": "सहित: सोमवल्क, पञ्चकोलक · छोड़कर (वर्ज्य): घोण्टा, भूनिम्ब, बाण · मिलाकर: फल की मज्जा का चूर्ण।",
        "frame": "क्या: लेह · किसके क्वाथ से: आरग्वध आदि में से कोई एक · क्या मिलाकर: फल-मज्जा चूर्ण · क्रिया: उपयोग करे।",
        "anchors": "आरग्वध = अमलतास · वर्ज्य = छोड़ने योग्य · लेह = चाटने का योग · उपयुञ्जीत = उपयोग करे।",
    },
    "22": {
        "diagram": {"groups": [{"label": "बाईस में से स्पष्ट नाम (सूची-क्रम)",
                                "items": ["रेणुका", "एला", "कुस्तुम्बुरु", "तगर", "कुष्ठ", "मरुवक", "अगुरु", "गुग्गुलु",
                                          "मांसी", "शैलेयक", "सुरसा", "अशोक"]}]},
        "frame": "क्या खाए: उत्कारिका या मोदक · किससे सिद्ध: बाईस में से किसी एक के काढ़े से · क्या मिलाकर: फल-मज्जा चूर्ण।",
        "sandhi": "आ + ए → ऐ: रेणुका + एला → रेणुकैला; विसर्ग + स्वर → र्: द्वाविंशतेः + अन्यतरस्य → द्वाविंशतेरन्यतरस्य।",
    },
    "23": {
        "chain": {"steps": ["तिल और शालि का पिसा आटा", "फल-पिप्पली के स्वरस और काढ़े से दबाया", "उसी के काढ़े से, या सुरसा आदि के काढ़े से मिलाया",
                            "शष्कुली, अपूप या अन्य भक्ष्य बनाए", "खाए"]},
        "sandhi": "विसर्ग + त → स्त: पिष्टैः + तत्कषाय → पिष्टैस्तत्कषाय; ईः + स्वर → ईर्: शष्कुलीः + अपूपान् → शष्कुलीरपूपान्।",
        "anchors": "तिल = तिल · शालि = अगहनी धान · पिष्ट = पिसा · उपसृष्ट = मिलाया · भक्ष्य = खाने की वस्तु।",
    },
    "24": {
        "chain": {"steps": ["फल-पिप्पलियों का स्वरस", "भल्लातक की विधि के अनुसार", "कलछी पर लेप चढ़ने तक पकाए", "चटाए (लेहयेत्)"]},
        "contrast": "लिहेत् = स्वयं चाटे · लेहयेत् = चटाए (प्रेरणार्थक)।",
        "anchors": "स्वरस = ताज़ा रस · दर्वी = कलछी · प्रलेप = लेप · आ + पञ्चमी = तक।",
    },
    "25": {
        "chunks": "अन्नपानेषु वा | तं लेहमवचारयेत् | तत्कषायैरेव च | अन्नपानानि कल्पयेत्।",
        "contrast": "पहली पंक्ति: लेह को अन्न-पान में मिलाए · दूसरी पंक्ति: उसके काढ़ों से ही अन्न-पान बनाए।",
        "sandhi": "अ + अ → आ: च + अन्नपानानि → चान्नपानानि; म् + स्वर: लेहम् + अवचारयेत् → लेहमवचारयेत्।",
    },
}


IMAGE_SPECS = {
    ("12", "diagram"): {
        "file": "ka1-nine-decoctions-12.svg",
        "alt": ("Mind map of unit 12: a decoction of any one of nine drugs (listed here in text order): yashtimadhuka, kovidara, "
                "karbudara, nipa, vidula, bimbi, shanapushpi, sadapushpi, pratyakpushpi"),
        "type": "mermaid",
        "code": ("mindmap\n  किसी एक का काढ़ा\n    यष्टीमधुक\n    कोविदार\n    कर्बुदार\n    नीप\n    विदुल\n"
                 "    बिम्बी\n    शणपुष्पी\n    सदापुष्पी\n    प्रत्यक्पुष्पी\n"),
    },
    ("15", "chain"): {
        "file": "ka1-own-decoction-15.svg",
        "alt": ("Flowchart of unit 15: fruit-pippali powder steeped in its own decoction, with three parts of triphala powder, "
                "drunk in a decoction of kovidara and the rest, in strong kapha, praseka, apaci, arbuda, granthi, fever, udara and arocaka"),
        "type": "mermaid",
        "code": ('flowchart TD\n  A["फल-पिप्पली का चूर्ण"] --> B["अपने क्वाथ में भावित"]\n'
                 '  B --> C["तीन भाग त्रिफला-चूर्ण"]\n  C --> D["कोविदार आदि के<br/>काढ़े से पिए"]\n'
                 '  D --> E["प्रबल कफ, प्रसेक,<br/>अपची, अर्बुद"]\n  D --> F["ग्रन्थि, ज्वर,<br/>उदर, अरोचक"]\n'),
    },
    ("17", "chain"): {
        "file": "ka1-kernel-milk-17.svg",
        "alt": ("Flowchart of unit 17: milk cooked with the madana kernel, or a gruel in that milk, given in raktapitta "
                "and in burning of the heart"),
        "type": "mermaid",
        "code": ('flowchart TD\n  A["मैनफल की गिरी"] --> B["उससे सिद्ध दूध"]\n  B --> C["या उस दूध में यवागू"]\n'
                 '  B --> D["रक्तपित्त"]\n  B --> E["हृदय की जलन"]\n  C --> D\n  C --> E\n'),
    },
    ("20", "chain"): {
        "file": "ka1-fresh-butter-20.svg",
        "alt": ("Flowchart of unit 20: fresh butter from that milk, cooked with the decoction of the six beginning with phala "
                "and mixed with the powder of the six phalas, for fire overcome by kapha and a drying body"),
        "type": "mermaid",
        "code": ('flowchart TD\n  A["उस दूध से नवनीत"] --> B["फलादि छह का क्वाथ"]\n  A --> C["छह फलों का चूर्ण"]\n'
                 '  B --> D["सिद्ध नवनीत"]\n  C --> D\n  D --> E["कफ से दबी अग्नि"]\n  D --> F["सूखता शरीर"]\n'),
    },
    ("21", "contrast"): {
        "file": "ka1-included-excluded-21.svg",
        "alt": ("Two columns for the lick of unit 21: together with soma-bark and pancakolaka; excluding ghonta, bhunimba "
                "and bana from the aragvadha group"),
        "type": "split",
        "title": "इकाई २१: आरग्वध आदि का क्वाथ",
        "cols": [["सहित", ["सोमवल्क", "पञ्चकोलक"]], ["छोड़कर (वर्ज्य)", ["घोण्टा", "भूनिम्ब", "बाण"]]],
    },
    ("22", "diagram"): {
        "file": "ka1-twenty-two-22.svg",
        "alt": ("Table of the clear names in unit 22's list of twenty-two with their identifications: ela small cardamom, "
                "kustumburu coriander, tagara probable, kushtha costus, maruvaka probable, aguru agarwood, guggulu, "
                "mamsi spikenard, shaileyaka stone-flower; standard unless marked"),
        "type": "table",
        "title": "इकाई २२: बाईस में से स्पष्ट नाम",
        "heads": ["नाम (सूची-क्रम)", "पहचान"],
        "rows": [["एला", "छोटी इलायची (मानक)"], ["कुस्तुम्बुरु", "धनिया (मानक)"], ["तगर", "तगर (सम्भावित)"],
                 ["कुष्ठ", "कूठ (मानक)"], ["मरुवक", "मरुआ (सम्भावित)"], ["अगुरु", "अगर (मानक)"],
                 ["गुग्गुलु", "गुग्गुल (मानक)"], ["मांसी", "जटामांसी (मानक)"], ["शैलेयक", "छरीला (मानक)"]],
    },
    ("23", "chain"): {
        "file": "ka1-cakes-23.svg",
        "alt": ("Flowchart of unit 23: ground sesame and shali rice, mixed with the fruit-pippali decoction or with the "
                "decoction of one of the surasa group, made into shashkuli, apupa or another food, and eaten"),
        "type": "mermaid",
        "code": ('flowchart TD\n  A["तिल और शालि का आटा"] --> B["फल-पिप्पली का काढ़ा"]\n'
                 '  A --> C["या सुरसा आदि में से<br/>एक का काढ़ा"]\n  B --> D["शष्कुली, अपूप<br/>या अन्य भक्ष्य"]\n'
                 '  C --> D\n  D --> E["खाए"]\n'),
    },
    ("24", "chain"): {
        "file": "ka1-ladle-coat-24.svg",
        "alt": ("Chain of unit 24: juice of the fruit-pippalis, by the bhallataka procedure, cooked until it coats the ladle, "
                "then given to lick"),
        "type": "chain",
        "title": "इकाई २४: स्वरस का लेह",
        "steps": ["फल-पिप्पलियों का स्वरस", "भल्लातक की विधि के अनुसार", "कलछी पर लेप चढ़ने तक पकाए", "चटाए"],
    },
}
