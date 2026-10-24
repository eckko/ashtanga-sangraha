from helpers import mcq, match, order, fill, multi, accepts

# Kalpasthana chapter 5 (Siddhabastikalpa), units 1-11.

AUTHORED = {}

# ---------------------------------------------------------------- unit 1
AUTHORED["1"] = {
    "title": "अथातः सिद्धबस्तिकल्पम्",
    "question": "What does the opening line of chapter 5 announce?",
    "rule": ("The chapter opens with the formula: now, therefore, we shall explain the "
             "kalpa (preparation) of the siddhabasti, the named 'proven' enemas."),
    "limits": ("The line names the topic only: it lists no enema, drug, measure or use. "
               "'Proven enema' is the literal sense of siddhabasti; the line does not say "
               "who proved them or how."),
    "explain_hi": ("यह पंचम अध्याय का आरम्भ-सूत्र है: ‘अथ’ (अब) और ‘अतः’ (इसलिए) के बाद विषय का नाम आता है। "
                   "विषय है सिद्धबस्ति-कल्प, यानी उन नामित बस्तियों की विधि जिन्हें ‘सिद्ध’ (आज़माई हुई) कहा गया है। "
                   "क्रिया ‘व्याख्यास्यामः’ है: हम व्याख्या करेंगे (भविष्य काल, उत्तम पुरुष बहुवचन)। "
                   "इस पंक्ति में कोई द्रव्य या प्रयोग नहीं है; वे आगे की इकाइयों में आते हैं।"),
    "hook": "अथ + अतः + विषय + व्याख्यास्यामः: अब सिद्धबस्तियों की विधि।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Which topic does unit 1 announce for the chapter?",
            ("The kalpa of the siddhabasti enemas",
             "सिद्धबस्तिकल्पम् = the kalpa (preparation) of the siddhabasti."),
            [("The preparation of emetic drugs (vamana)",
              "Emetics are the topic of Kalpasthāna chapter 1, not of this line."),
             ("The mishaps of purgation (virecana)",
              "No mishap or purgation is named in this line."),
             ("The weights and measures of drugs",
              "The line names no measure; it names the siddhabasti.")],
            "The opening formula names the chapter's topic: the siddhabasti-kalpa.",
            "अथातः X व्याख्यास्यामः = now, therefore, we shall explain X."),
        match(1, "Match each word of unit 1 to its meaning.",
              [["अथ", "now"], ["अतः", "therefore"],
               ["सिद्धबस्तिकल्पम्", "the preparation of the siddhabasti"],
               ["व्याख्यास्यामः", "we shall explain"]],
              "The four words make the whole opening formula.",
              "अथ = now; अतः = therefore; व्याख्यास्यामः = we shall explain."),
        order(2, "Put these words of unit 1 in the order of the text.",
              ["अथ", "अतः", "सिद्धबस्तिकल्पम्", "व्याख्यास्यामः"],
              "The formula runs: now, therefore, the topic, we shall explain.",
              "अथ · अतः · सिद्धबस्तिकल्पम् · व्याख्यास्यामः.",
              role="extend",
              teaches="An opening formula puts the topic between अथातः and the verb व्याख्यास्यामः."),
        mcq("discriminate", 3, "Which split of अथातः is right?",
            ("अथ + अतः", "अ + अ gives आ: अथ + अतः = अथातः."),
            [("अथा + तः", "तः is not a word here, and अथा is not the particle अथ."),
             ("अथः + अतः", "A visarga after अ before अ would give अथोऽतः, not अथातः."),
             ("अथ + आतः", "आतः is not a word; the second word is अतः (therefore).")],
            "Two particles join: अथ (now) + अतः (therefore).",
            "अ + अ → आ: अथ + अतः = अथातः."),
        mcq("apply", 4, "What does the card say the form व्याख्यास्यामः is?",
            ("First person plural future: we shall explain",
             "The data labels it 1 pl. fut. of vi-ā-√khyā."),
            [("Third person singular optative: one should explain",
              "An optative would end in -एत् or -ईत; this ends in -स्यामः."),
             ("First person plural past: we explained",
              "The -स्य- marks the future, not a past tense."),
             ("Second person imperative: explain!",
              "An imperative to one person would not end in -आमः.")],
            "-स्यामः = 'we shall ...': the author promises what follows.",
            "व्याख्यास्यामः = we shall explain (1 pl. future)."),
        mcq("transfer", 5,
            "An invented heading joins अथ + अतः before बस्तिकल्पम्. Which joined form is right?",
            ("अथातो बस्तिकल्पम्",
             "-अः before a voiced consonant (ब) becomes -ओ."),
            [("अथातः बस्तिकल्पम्", "The visarga stays only before an unvoiced sound such as स in सिद्ध-."),
             ("अथातर्बस्तिकल्पम्", "र् replaces a visarga after vowels other than अ/आ, not after अ."),
             ("अथाता बस्तिकल्पम्", "Dropping the visarga to -आ happens after -आः, not after -अः.")],
            "In unit 1 the visarga stays because सिद्ध- begins with स; before ब it becomes ओ.",
            "-अः + voiced consonant → -ओ: अथातः + बस्ति → अथातो बस्ति.",
            teaches="-अः before a voiced consonant becomes -ओ (अथातो बस्तिकल्पम्); before स it stays (अथातः सिद्ध-)."),
    ],
}

# ---------------------------------------------------------------- unit 2
AUTHORED["2"] = {
    "title": "सिद्धबस्तीन्प्रयुञ्जीत",
    "question": "For whom does verse 2 commend the siddhabastis, and which qualities does it give them?",
    "rule": ("One should employ the siddhabastis for all embodied beings at all times; "
             "they are free from mishap, of many benefits, producing strength and "
             "intelligence, and pleasant."),
    "limits": ("The verse names no enema or drug; those follow. 'Strength' reads printed वल "
               "as बल (flagged). निर्व्यापदो does not agree with the accusatives around it "
               "(flagged), so no question rests on its form. सर्वदेहिनाम् may mean 'for' or "
               "'of' all beings."),
    "explain_hi": ("यह श्लोक सिद्धबस्तियों की प्रशंसा है: इन्हें सब देहधारियों के लिए सदा प्रयोग करे। "
                   "फिर चार गुण गिनाए गए हैं: बिना विपत्ति के, बहुत फल देने वाली, बल और बुद्धि उत्पन्न करने वाली, और सुखद। "
                   "‘प्रयुञ्जीत’ विधिलिङ् (चाहिए) का रूप है: एक को प्रयोग करना चाहिए। "
                   "छपा ‘वल’ यहाँ ‘बल’ पढ़ा गया है, और ‘निर्व्यापदो’ का रूप बाकी विशेषणों से मेल नहीं खाता।"),
    "hook": "सबके लिए, सदा: निर्विपद, बहुफल, बल-बुद्धिकर, सुखद।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "For whom does verse 2 say the siddhabastis should be employed?",
            ("For all embodied beings",
             "सर्व-देहिनाम् = of / for all embodied beings."),
            [("Only for the strong and the young",
              "The verse limits them to no group; it says all embodied beings."),
             ("Only for those with Vāta disorders",
              "No doṣa or disorder is named in this verse."),
             ("Only for children and the old",
              "No age group is named here; the verse says all.")],
            "The verse sets no limit: all embodied beings, at all times (सर्वदा).",
            "सर्वदा सर्वदेहिनाम् = at all times, for all embodied beings."),
        match(1, "Match each word of verse 2 to its meaning.",
              [["प्रयुञ्जीत", "one should employ"], ["सर्वदा", "at all times"],
               ["बहुफलान्", "of many benefits"], ["सुखान्", "pleasant"]],
              "These words give the instruction and two of the qualities.",
              "प्रयुञ्जीत = one should employ; सर्वदा = at all times; बहुफलान् = of many benefits; सुखान् = pleasant."),
        order(2, "Put these printed words of line 2 in the order of the verse.",
              ["निर्व्यापदो", "बहुफलान्", "वलबुद्धि करान्", "सुखान्"],
              "The qualities run: free from mishap, of many benefits, producing (strength and) intelligence, pleasant.",
              "निर्व्यापदो · बहुफलान् · वलबुद्धि करान् · सुखान्.",
              role="extend",
              teaches="Line 2 lists four qualities of the siddhabastis, ending with सुखान् (pleasant)."),
        mcq("discriminate", 3, "Which split of सिद्धबस्तीन्प्रयुंजीत is right?",
            ("सिद्धबस्तीन् + प्रयुञ्जीत",
             "The accusative plural -ईन् is the object of प्रयुञ्जीत (one should employ)."),
            [("सिद्धबस्ति + न + प्रयुञ्जीत",
              "न 'not' would forbid what the verse commends for all beings at all times."),
             ("सिद्धबस्ती + न्प्रयुञ्जीत", "न्प्रयुञ्जीत is not a word."),
             ("सिद्धबस्तीन + प्रयुञ्जीत", "सिद्धबस्तीन is not a form; the ending is -ईन्.")],
            "सिद्धबस्तीन् (the siddhabastis, acc. pl.) + प्रयुञ्जीत (one should employ).",
            "-ईन् = masculine accusative plural of an -इ stem (बस्तीन्)."),
        multi("apply", 4,
              "Which qualities does verse 2 give the siddhabastis?",
              [("Free from mishap", "निर्व्यापदः = free from mishap."),
               ("Quick to act within an hour", "No time of action is named."),
               ("Pleasant", "सुखान् = pleasant."),
               ("To be given only by a royal physician", "No physician is named."),
               ("Of many benefits", "बहुफलान् = of many benefits."),
               ("Cheap and easy to collect", "Nothing about cost or collecting is said.")],
              [0, 2, 4],
              "The verse names four qualities: free from mishap, of many benefits, producing strength and intelligence, pleasant.",
              "निर्व्यापद् · बहुफल · बलबुद्धिकर · सुख."),
        mcq("transfer", 5,
            "Like प्रयुञ्जीत (one should employ, √युज्), which form means one should eat (√भुज्)?",
            ("भुञ्जीत", "Same 3 sg optative ātmanepada pattern: -उञ्जीत, as in प्रयुञ्जीत."),
            [("भुङ्क्ते", "This is the present tense: 'he eats'."),
             ("भोक्ष्यते", "This is the future: 'he will eat'."),
             ("भुक्तः", "This is the past participle: 'eaten'.")],
            "√युज् and √भुज् form the optative the same way: युञ्जीत, भुञ्जीत.",
            "3 sg optative ātmanepada ends in -ईत: प्रयुञ्जीत, भुञ्जीत.",
            teaches="The ending -ईत marks a 3rd-person singular optative (ātmanepada): 'one should ...' (प्रयुञ्जीत, भुञ्जीत)."),
    ],
}

# ---------------------------------------------------------------- unit 3
AUTHORED["3"] = {
    "title": "निरूहो माधुतैलिकः",
    "question": "Which nirūha does verse 3 describe, and which ingredients can be read in it?",
    "rule": ("Honey and oil in equal parts, a karṣa, two picu from rock salt, miśi (probably "
             "dill), with a decoction of castor (eraṇḍa) root: the mādhutailika nirūha "
             "(decoction enema) made with honey and oil."),
    "limits": ("Low confidence. Which quantity (karṣa, two picu) goes with which drug is not "
               "clear, so no question rests on it. miśi as dill is disputed (fennel also given). "
               "Printed काथेन is read क्वाथेन (flagged). Whether mādhutailika is a proper name "
               "is an open observation."),
    "explain_hi": ("यह श्लोक मधु और तैल वाले निरूह यानी काढ़े की बस्ति का वर्णन है। "
                   "पहली पंक्ति में मधु और तैल को बराबर कहा गया है; फिर ‘कर्ष’, सैन्धव से ‘दो पिचु’ और मिशि यानी सम्भवतः सोया आते हैं। "
                   "कौन-सी मात्रा किस द्रव्य की है, यह पंक्ति से स्पष्ट नहीं है। "
                   "दूसरी पंक्ति कहती है कि यह निरूह एरण्ड यानी अरंडी की जड़ के काढ़े से बनता है, और इसका नाम-सा विशेषण माधुतैलिक (मधु-तैल वाला) है।"),
    "hook": "अरंडी-जड़ का काढ़ा + बराबर मधु-तैल = माधुतैलिक निरूह।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Which two things does verse 3 call equal (समे)?",
            ("Honey and oil", "मधुतैले समे = honey and oil, equal (dual)."),
            [("Rock salt and miśi", "These follow; the equal pair is मधुतैले."),
             ("Castor root and honey", "Castor root gives the decoction in line 2."),
             ("Oil and the decoction", "The decoction is in line 2; समे goes with मधुतैले.")],
            "मधुतैले (dual) and समे (dual) agree: honey and oil, equal.",
            "मधुतैले समे = honey and oil in equal parts."),
        match(1, "Match each word of verse 3 to its meaning.",
              [["मधु", "honey"], ["तैल", "oil"], ["सैन्धव", "rock salt"],
               ["एरण्डमूल", "castor root"], ["निरूह", "decoction enema"]],
              "These are the readable items and the name of the enema.",
              "मधु = honey; तैल = oil; सैन्धव = rock salt; एरण्डमूल = castor root; निरूह = decoction enema."),
        order(2, "Put these words of verse 3 in the order of the verse.",
              ["मधुतैले समे", "कर्षः", "सैंधवाद्द्विपिचुः", "मिशिः", "एरंडमूलकाथेन", "निरूहो माधुतैलिकः"],
              "Line 1 lists the items and measures; line 2 gives the decoction and names the nirūha.",
              "मधुतैले समे · कर्षः · सैंधवात् द्विपिचुः · मिशिः ‖ एरंडमूलकाथेन · निरूहो माधुतैलिकः.",
              role="extend",
              teaches="Verse 3 lists honey-oil, a karṣa, two picu of rock salt and miśi, then the castor-root decoction."),
        mcq("discriminate", 3, "What does the word माधुतैलिकः tell about this nirūha?",
            ("It is made with honey (madhu) and oil (taila)",
             "माधुतैलिक is formed from मधु + तैल: made with honey and oil."),
            [("It is made with milk (kṣīra) and oil (taila)", "Milk is not named in this verse."),
             ("It is given only in the spring month", "The card reads मधु as honey here, not as a season."),
             ("It is made with ghee and rock salt alone", "Ghee is not named, and honey and oil are.")],
            "The derived adjective names the two key items: honey and oil.",
            "माधुतैलिक = made with मधु (honey) and तैल (oil)."),
        mcq("apply", 4, "Which liquid does verse 3 give for the nirūha?",
            ("Castor-root decoction",
             "एरंडमूलकाथेन, read एरण्डमूलक्वाथेन = with a decoction of castor root."),
            [("Cow's urine (gomūtra)", "Cow's urine appears in verse 10, not here."),
             ("Meat broth (māṃsarasa)", "No broth is named in this verse."),
             ("Plain cow's milk", "Milk is not named in this verse.")],
            "The base of the nirūha is the castor-root decoction (printed काथ read क्वाथ).",
            "एरण्डमूल-क्वाथ = decoction of castor root."),
        mcq("transfer", 5,
            "In सैंधवाद्द्विपिचुः, सैन्धवात् became सैंधवाद्. Join an invented सैन्धवात् + गुडः the same way. Which is right?",
            ("सैन्धवाद्गुडः", "Final त् becomes द् before a voiced consonant (ग), as before द."),
            [("सैन्धवात्गुडः", "त् does not stay unvoiced before a voiced consonant."),
             ("सैन्धवाग्गुडः", "त् does not take the place of the next consonant before ग."),
             ("सैन्धवान्गुडः", "त् becomes न् only before a nasal (न, म).")],
            "Same rule as सैन्धवात् + द्विपिचुः = सैन्धवाद्द्विपिचुः.",
            "Final त् → द् before a voiced consonant.",
            teaches="Final त् becomes द् before a voiced consonant: सैन्धवात् + द्वि → सैन्धवाद्द्वि; + गुडः → सैन्धवाद्गुडः."),
    ],
}

# ---------------------------------------------------------------- unit 4
AUTHORED["4"] = {
    "title": "रसायनं प्रमेहार्शः",
    "question": "What benefits does verse 4 give for the honey-oil nirūha, and what does licorice add?",
    "rule": ("The nirūha is a rasāyana (rejuvenating) and dispels prameha, arśas "
             "(haemorrhoids), worms, gulma and antravṛddhi (hernia); with licorice "
             "(yaṣṭīmadhu) it is good for the eyes and conquers raktapitta."),
    "limits": ("The verse continues the nirūha of verse 3 and has no verb. The visarga in "
               "प्रमेहार्शः may be a print error or mark a separate word; the list reading is "
               "kept. prameha (urinary disorders linked with diabetes) and raktapitta (a bleeding "
               "disorder) are probable identifications."),
    "explain_hi": ("यह श्लोक पिछले माधुतैलिक निरूह के गुण बताता है। पहले यह रसायन है, फिर यह प्रमेह यानी मूत्र-विकार, अर्श यानी बवासीर, "
                   "कृमि, गुल्म यानी पेट की गाँठ और अन्त्रवृद्धि यानी हर्निया को दूर करता है (‘-नुत्’ = दूर करने वाला)। "
                   "दूसरी पंक्ति में यष्टीमधु यानी मुलेठी के साथ यही निरूह आँखों के लिए हितकर और रक्तपित्त को जीतने वाला कहा गया है। "
                   "श्लोक में कोई क्रिया नहीं है; सब विशेषण हैं।"),
    "hook": "रसायन; प्रमेह-अर्श-कृमि-गुल्म-अन्त्रवृद्धि दूर; मुलेठी के साथ आँख और रक्तपित्त।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "With licorice (यष्टीमधु) added, what does verse 4 say the nirūha does?",
            ("Helps the eyes, conquers raktapitta",
             "सयष्टीमधुकः ... चक्षुष्यो रक्तपित्तजित्."),
            [("It is fattening and brings on deep sleep", "Neither is named in this verse."),
             ("It clears the voice and the skin", "Voice and skin are not named here."),
             ("It removes the faults of the enema", "That phrase belongs to verse 8.")],
            "Line 2: with licorice, cakṣuṣya (good for the eyes) and raktapitta-jit.",
            "सयष्टीमधुकः → चक्षुष्यः + रक्तपित्तजित्."),
        match(1, "Match each disorder of verse 4 to its meaning on the card.",
              [["अर्शस्", "haemorrhoids"], ["कृमि", "worms"],
               ["गुल्म", "abdominal lump"], ["अन्त्रवृद्धि", "intestinal hernia"]],
              "These are four of the disorders the nirūha dispels.",
              "अर्शस् = haemorrhoids; कृमि = worms; गुल्म = abdominal lump; अन्त्रवृद्धि = hernia."),
        order(2, "Put the disorders that the nirūha dispels in the order of verse 4.",
              ["प्रमेह", "अर्शस्", "कृमि", "गुल्म", "अन्त्रवृद्धि"],
              "Line 1 runs prameha, arśas, then the compound kṛmi-gulma-antravṛddhi-nut.",
              "प्रमेह · अर्शस् · कृमि · गुल्म · अन्त्रवृद्धि.",
              role="extend",
              teaches="The nirūha dispels prameha, arśas, worms, gulma and antravṛddhi, in that order."),
        mcq("discriminate", 3, "Why is चक्षुष्यः printed as चक्षुष्यो before रक्तपित्तजित्?",
            ("-अः turns to -ओ before voiced र",
             "Regular visarga sandhi: चक्षुष्यः + रक्त → चक्षुष्यो रक्त."),
            [("-ओ marks the vocative of the word", "The vocative of चक्षुष्य would be चक्षुष्य; the card gives nom. sg."),
             ("-ओ marks a dual form of the word", "The card labels it m. nom. sg."),
             ("-ओ marks the neuter gender here", "The card labels it masculine.")],
            "The form is nominative singular; only sandhi changes -अः to -ओ.",
            "-अः + voiced consonant → -ओ."),
        mcq("apply", 4, "According to verse 4, which addition makes the nirūha conquer raktapitta?",
            ("Licorice (यष्टीमधु)", "सयष्टीमधुकः = with licorice; then रक्तपित्तजित्."),
            [("More rock salt (सैन्धव)", "Rock salt is not named in this verse."),
             ("Cow's urine (गोमूत्र)", "Cow's urine is not named in this verse."),
             ("Hapuṣā (हपुषा)", "Hapuṣā belongs to the yāpana of verse 6.")],
            "Line 2 ties the eye benefit and raktapitta to the licorice version.",
            "स-यष्टीमधुकः → रक्तपित्तजित्."),
        mcq("transfer", 5,
            "Like रक्तपित्तजित् (conquering raktapitta), what does an invented ज्वरजित् mean (ज्वर = fever)?",
            ("Conquering fever", "-जित् at the end of a compound means 'conquering X'."),
            [("Born of fever", "That would be ज्वरज, with -ज (born)."),
             ("Causing fever", "That would need -कर (making), as in बलबुद्धिकर."),
             ("Conquered by fever", "-जित् is active: it conquers, it is not conquered.")],
            "Same build as रक्तपित्तजित् and शूलजित्: X + जित् = conquering X.",
            "X-जित् = conquering X.",
            teaches="A compound ending in -जित् means 'conquering X' (रक्तपित्तजित्, ज्वरजित्)."),
    ],
}

# ---------------------------------------------------------------- unit 5
AUTHORED["5"] = {
    "title": "यापनो घनकल्केन",
    "question": "What does the yāpana of verse 5 contain, and which pains can be read in it?",
    "rule": ("A yāpana (sustaining enema) with a thick paste, having honey, oil, fat (vasā) "
             "and ghee, conquers pain in the anus, knee, thigh, bladder region and penis; one "
             "word in the middle of the list is damaged."),
    "limits": ("Low confidence. पृष्टशण is not a word; 'back and hip' (पृष्ठ-श्रोणि) is only a "
               "conjecture, so no question uses it. The drugs of the thick paste and the "
               "decoction are not named in this verse."),
    "explain_hi": ("यह श्लोक एक यापन बस्ति (शरीर को टिकाए रखने वाली बस्ति) बताता है। इसमें गाढ़ा कल्क होता है, "
                   "और यह मधु, तैल, वसा यानी चर्बी और घी (आज्य) वाली है (‘-वान्’ = वाला)। "
                   "दूसरी पंक्ति एक लम्बा समास है: गुदा, घुटना, जाँघ, एक अस्पष्ट शब्द, बस्ति-प्रदेश और लिंग की पीड़ा को जीतने वाली। "
                   "बीच का छपा ‘पृष्टशण’ कोई शब्द नहीं है; ‘पीठ और कूल्हा’ केवल अनुमानित पाठ है।"),
    "hook": "गाढ़ा कल्क + मधु-तैल-वसा-घी = यापन; गुदा से लिंग तक की पीड़ा।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Which four substances does verse 5 say the yāpana has?",
            ("Honey, oil, fat (vasā) and ghee",
             "मधु-तैल-वसा-आज्य-वान् = having honey, oil, fat and ghee."),
            [("Honey, milk, oil and rock salt", "Milk and rock salt are not in this verse."),
             ("Ghee, curd, oil and cow's urine", "Curd and cow's urine are not in this verse."),
             ("Fat, honey, sugar and sesame", "Sugar and sesame are not in this verse.")],
            "The -वान् compound lists four: honey, oil, fat, ghee (आज्य).",
            "मधुतैलवसाज्यवान् = having honey, oil, fat, ghee."),
        match(1, "Match each body part of verse 5 to its meaning.",
              [["पायु", "anus"], ["जानु", "knee"], ["ऊरु", "thigh"], ["मेहन", "penis"]],
              "These are readable members of the pain compound.",
              "पायु = anus; जानु = knee; ऊरु = thigh; मेहन = penis."),
        order(2, "Put the four substances of line 1 in the order of the verse.",
              ["मधु", "तैल", "वसा", "आज्य"],
              "The compound runs honey, oil, fat, ghee, then -वान् (having).",
              "मधु · तैल · वसा · आज्य.",
              role="extend",
              teaches="The yāpana has honey, oil, fat (vasā) and ghee (ājya), in that order."),
        mcq("discriminate", 3, "Which split of the end of मधुतैलवसाज्यवान् is right?",
            ("वसा + आज्य + वान्", "आ + आ gives आ; आज्य = ghee, -वान् = having."),
            [("वसाज + यवान्", "The card reads आज्य (ghee) + -वान्; यवान् (barley) is not on the card."),
             ("वस + आज्यवान्", "The word is वसा (fat), with long आ."),
             ("वसा + अज्य + वान्", "अज्य is not a word; the word is आज्य (ghee).")],
            "Fat (वसा) and ghee (आज्य) join with आ + आ → आ.",
            "आ + आ → आ: वसा + आज्य = वसाज्य."),
        multi("apply", 4,
              "Which body parts does the readable part of verse 5 name for pain?",
              [("Anus", "पायु = anus."),
               ("Knee", "जानु = knee."),
               ("Head", "No head (शिरस्) is named."),
               ("Chest", "No chest is named."),
               ("Bladder region", "बस्ति here = bladder region."),
               ("Eyes", "Eyes are in verse 4, not here.")],
              [0, 1, 4],
              "Readable members: anus, knee, thigh, bladder region, penis; the middle word is damaged.",
              "पायु · जानु · ऊरु · (अस्पष्ट) · बस्ति · मेहन + शूलजित्."),
        mcq("transfer", 5,
            "Like आज्यवान् (having ghee), which invented form means having milk (क्षीर)?",
            ("क्षीरवान्", "-वत् (nom. m. -वान्) after a stem in -अ means 'having X'."),
            [("क्षीरजित्", "-जित् means 'conquering', not 'having'."),
             ("क्षीरात्", "This is the ablative, 'from milk'."),
             ("क्षीरम्", "This is the noun 'milk' itself.")],
            "Same suffix as मधुतैलवसाज्यवान्: X + -वान् = having X.",
            "X-वान् (-वत्) = having X.",
            teaches="The suffix -वत् (masc. nom. -वान्) means 'having X': आज्यवान्, क्षीरवान्."),
    ],
}

# ---------------------------------------------------------------- unit 6
AUTHORED["6"] = {
    "title": "प्रसृतांशैः प्रकल्पयेत्",
    "question": "With which substances and measures does verse 6 prepare the yāpana?",
    "rule": ("One should prepare the yāpana with ghee, honey, fat and oil in prasṛta "
             "portions, accompanied by half an akṣa of rock salt and half a pala of hapuṣā "
             "(probably juniper berries)."),
    "limits": ("'Half akṣa of salt, half pala of hapuṣā' is the natural reading, but no word "
               "separates the two in the compound. The verse does not say how many prasṛtas, nor "
               "the decoction. Measures stay as given: prasṛta, akṣa, pala."),
    "explain_hi": ("यह श्लोक यापन बनाने की मात्राएँ देता है: घी, शहद (क्षौद्र), वसा और तैल को प्रसृत के अंशों में लेकर तैयार करे। "
                   "प्रसृत एक मान है (मानक तालिकाओं में लगभग दो पल)। "
                   "साथ में आधा अक्ष सैन्धव यानी सेंधा नमक और आधा पल हपुषा यानी सम्भवतः हाऊबेर। "
                   "‘अन्वित’ का अर्थ है ‘से युक्त’। क्रिया ‘प्रकल्पयेत्’ है: तैयार करे।"),
    "hook": "चार स्नेह-मधु प्रसृत-अंश में; सैन्धव आधा अक्ष, हपुषा आधा पल।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Which measure does verse 6 give for the ghee, honey, fat and oil?",
            ("Prasṛta portions", "प्रसृत-अंशैः = with prasṛta portions."),
            [("Half an akṣa each", "Half an akṣa goes with the rock salt."),
             ("Half a pala each", "Half a pala goes with hapuṣā."),
             ("A karṣa each", "A karṣa is named in verse 3, not here.")],
            "The four substances are measured in prasṛta portions.",
            "प्रसृतांशैः घृतक्षौद्रवसातैलैः = with ghee, honey, fat, oil in prasṛta portions."),
        order(1, "Put these four substances in the order of verse 6.",
              ["घृत", "क्षौद्र", "वसा", "तैल"],
              "The compound runs ghee, honey, fat, oil.",
              "घृत · क्षौद्र · वसा · तैल."),
        match(2, "Match each word of verse 6 to its meaning.",
              [["क्षौद्र", "honey"], ["वसा", "fat"], ["अर्ध", "half"],
               ["अन्वित", "accompanied by"]],
              "These words carry the substances and the half measures.",
              "क्षौद्र = honey; वसा = fat; अर्ध = half; अन्वित = accompanied by.",
              role="extend",
              teaches="In verse 6, क्षौद्र is honey and अर्ध + measure gives the half measures of salt and hapuṣā."),
        mcq("discriminate", 3, "Which split of प्रसृतांशैर्घृत is right?",
            ("प्रसृत + अंशैः + घृत",
             "अ + अ → आ; -ऐः before a voiced sound (घ) becomes -ऐर्."),
            [("प्रसृता + अंशैर् + घृत", "The measure is प्रसृत, not प्रसृता."),
             ("प्रसृत + अंशे + र्घृत", "र्घृत is not a word; the र् comes from the visarga of अंशैः."),
             ("प्रसृतांशैः + र्घृत", "The र् replaces the visarga; it is not part of घृत.")],
            "The visarga of अंशैः turns into र् before घृत.",
            "-ऐः + voiced consonant → -ऐर्."),
        mcq("apply", 4, "Which word gives the action of verse 6, and what does it mean?",
            ("प्रकल्पयेत्: one should prepare", "प्र-√क्ळृप्, 3 sg optative: one should prepare."),
            [("पाचयेत्: one should cook", "पाचयेत् is the verb of verse 10."),
             ("प्रयुञ्जीत: one should employ", "प्रयुञ्जीत is the verb of verse 2."),
             ("व्याख्यास्यामः: we shall explain", "That is the verb of unit 1.")],
            "Verse 6's own verb is प्रकल्पयेत्.",
            "प्रकल्पयेत् = one should prepare."),
        mcq("transfer", 5,
            "Join an invented अंशैः + दत्तम् (given in portions) by the rule of प्रसृतांशैर्घृत. Which is right?",
            ("अंशैर्दत्तम्", "-ऐः before a voiced consonant (द) becomes -ऐर्."),
            [("अंशैःदत्तम्", "The visarga does not stay before a voiced consonant."),
             ("अंशैदत्तम्", "The visarga is not dropped after ऐ."),
             ("अंशैस्दत्तम्", "स् replaces a visarga only before त-type unvoiced sounds.")],
            "Same rule as अंशैः + घृत = अंशैर्घृत.",
            "Visarga after a vowel other than अ/आ → र् before a voiced sound.",
            teaches="A visarga after a vowel other than अ/आ becomes र् before a voiced sound: अंशैः + घृत → अंशैर्घृत."),
    ],
}

# ---------------------------------------------------------------- unit 7
AUTHORED["7"] = {
    "title": "एष युक्तरथो बस्तिः",
    "question": "Which ingredients make the yuktaratha enema of verse 7?",
    "rule": ("A decoction of castor root, honey and oil with rock salt, and with vacā (sweet "
             "flag), pippalī (long pepper) and fruit (phala): this is the yuktaratha enema, "
             "literally 'harnessed chariot'."),
    "limits": ("The fruit (phala) is not named further; it may also be read as 'pippalī fruit'. "
               "The verse gives no measure and no use. Printed निःक्काथो is read निःक्वाथो "
               "(flagged)."),
    "explain_hi": ("यह श्लोक युक्तरथ नाम की बस्ति बताता है (शाब्दिक: जुता हुआ रथ)। "
                   "पहली पंक्ति के द्रव्य हैं: एरण्ड यानी अरंडी की जड़ का काढ़ा, मधु, तैल, और सैन्धव के साथ। "
                   "दूसरी पंक्ति कहती है ‘एष युक्तरथो बस्तिः’ (यह युक्तरथ बस्ति है), और वचा यानी बच, पिप्पली यानी पीपर तथा फल सहित। "
                   "फल का नाम नहीं दिया गया; इसे ‘पिप्पली का फल’ भी पढ़ा जा सकता है।"),
    "hook": "अरंडी-जड़ काढ़ा, मधु, तैल, सैन्धव, बच, पीपर, फल = युक्तरथ।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "What does verse 7 call this enema?",
            ("Yuktaratha (युक्तरथ)", "एष युक्तरथो बस्तिः = this is the yuktaratha enema."),
            [("Siddhabasti (सिद्धबस्ति)", "That name is given in verse 9."),
             ("Mādhutailika (माधुतैलिक)", "That is the nirūha of verse 3."),
             ("Yāpana (यापन)", "The yāpana is in verses 5-6.")],
            "The verse names itself: एष युक्तरथो बस्तिः.",
            "युक्तरथ = the 'harnessed chariot' enema."),
        match(1, "Match each drug of verse 7 to its meaning on the card.",
              [["वचा", "sweet flag"], ["पिप्पली", "long pepper"],
               ["एरण्डमूल", "castor root"], ["सैन्धव", "rock salt"]],
              "These four drugs carry identifications marked standard on the card.",
              "वचा = sweet flag; पिप्पली = long pepper; एरण्डमूल = castor root; सैन्धव = rock salt."),
        order(2, "Put these items in the order of verse 7.",
              ["एरण्डमूलनिःक्वाथ", "मधु", "तैल", "सैन्धव", "वचा", "पिप्पली"],
              "Line 1: decoction, honey, oil, rock salt; line 2: vacā, pippalī (and fruit).",
              "निःक्वाथ · मधु · तैल · सैन्धव ‖ वचा · पिप्पली · फल.",
              role="extend",
              teaches="The yuktaratha: castor-root decoction, honey, oil, rock salt, then vacā, pippalī and fruit."),
        mcq("discriminate", 3, "What does स- at the start of ससैन्धवम् and सवचा- mean?",
            ("With, accompanied by", "स- opening a bahuvrīhi = 'with X'."),
            [("Without, lacking", "'Without' would be निर्- or अ-, as in निर्व्यापद्."),
             ("Equal to, same as", "'Equal' is सम, as in verse 3 (समे)."),
             ("Good, well made", "'Good' would be सु-.")],
            "ससैन्धवम् = with rock salt; सवचापिप्पलीफलः = with vacā, pippalī and fruit.",
            "स- + noun = with that noun."),
        mcq("apply", 4, "Which of these is not an ingredient of the yuktaratha in verse 7?",
            ("Cow's urine", "Cow's urine is not named in verse 7."),
            [("Honey", "मधु is named in line 1."),
             ("Vacā (sweet flag)", "सवचा- = with vacā, in line 2."),
             ("Rock salt", "ससैन्धवम् = with rock salt, in line 1.")],
            "The verse names castor-root decoction, honey, oil, rock salt, vacā, pippalī and fruit.",
            "युक्तरथ: एरण्डमूल-क्वाथ, मधु, तैल, सैन्धव, वचा, पिप्पली, फल."),
        mcq("transfer", 5,
            "Built like ससैन्धवम् (with rock salt), what does an invented सघृतम् mean?",
            ("With ghee", "स- + घृत = with ghee."),
            [("Without ghee", "That would be निर्घृतम्."),
             ("Equal to ghee", "That would need सम (equal)."),
             ("Ghee alone", "स- adds an accompaniment; it does not mean 'alone'.")],
            "Same prefix as ससैन्धवम् and सवचा-.",
            "स- + X = with X.",
            teaches="स- before a noun makes a bahuvrīhi 'with X': ससैन्धवम्, सघृतम्."),
    ],
}

# ---------------------------------------------------------------- unit 8
AUTHORED["8"] = {
    "title": "बस्तिदोषहरः शिवः",
    "question": "Which readable items does verse 8 list, and what does it say the preparation does?",
    "rule": ("With a decoction, honey, an unclear word, śatāhvā (probably dill), asafoetida, "
             "rock salt, suradāru (deodar) and rāsnā: the preparation removes the faults of the "
             "enema (basti-doṣa) and is auspicious."),
    "limits": ("Low confidence. पैंढुंथा is damaged and unidentified: no question uses it. "
               "The decoction's drugs are not named. Printed शताव्हा is read शताह्वा (flagged). "
               "rāsnā's identity is disputed. The card reads basti-doṣa as faults of the enema."),
    "explain_hi": ("यह श्लोक एक और बस्ति के द्रव्य गिनाता है: काढ़े के साथ, मधु, एक अस्पष्ट छपा शब्द (पैंढुंथा), शताह्वा यानी सम्भवतः सोया, "
                   "हींग और सैन्धव; फिर सुरदारु यानी देवदार और रास्ना (पहचान में मतभेद)। "
                   "अन्त में दो विशेषण: ‘बस्तिदोषहरः’ यानी बस्ति के दोषों को हरने वाला, और ‘शिवः’ यानी कल्याणकारी। "
                   "अस्पष्ट शब्द की पहचान नहीं की गई है।"),
    "hook": "मधु, सोया, हींग, सैन्धव, देवदार, रास्ना: बस्ति-दोष हरे, कल्याणकारी।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "What does verse 8 say the preparation removes?",
            ("Faults of the enema", "बस्ति-दोष-हरः = removing the faults of the enema."),
            [("Worms and gulma", "Worms and gulma are in verse 4."),
             ("Pain of the knee and thigh", "Those pains are in verse 5."),
             ("Kapha disorders and visūcī", "Those are in verse 11.")],
            "बस्तिदोषहरः: -हर = removing; the data reads the faults as those of the enema.",
            "बस्तिदोषहरः = removing the faults of the enema."),
        match(1, "Match each word of verse 8 to its meaning.",
              [["हिङ्गु", "asafoetida"], ["सैन्धव", "rock salt"],
               ["सुरदारु", "deodar cedar"], ["शिवः", "auspicious"]],
              "Three readable drugs and the closing adjective.",
              "हिङ्गु = asafoetida; सैन्धव = rock salt; सुरदारु = deodar; शिवः = auspicious."),
        order(2, "Put these readable items in the order of verse 8.",
              ["मधु", "शताह्वा", "हिङ्गु", "सैन्धव", "सुरदारु", "रास्ना"],
              "Line 1: honey, (unclear word), śatāhvā, asafoetida, rock salt; line 2: suradāru, rāsnā.",
              "मधु · (अस्पष्ट) · शताह्वा · हिङ्गु · सैन्धव ‖ सुरदारु · रास्ना.",
              role="extend",
              teaches="The readable list of verse 8 runs honey, śatāhvā, asafoetida, rock salt, suradāru, rāsnā."),
        mcq("discriminate", 3, "What does शिवः describe in verse 8?",
            ("The preparation: auspicious",
             "शिवः (m. nom. sg.) agrees with the preparation, like बस्तिदोषहरः."),
            [("The god Śiva, who taught the formula", "No teacher or deity is named in the verse."),
             ("A further drug of the list", "The card glosses शिवः as 'auspicious', an adjective."),
             ("The patient who receives it", "No patient is named; शिवः goes with the preparation.")],
            "The two closing adjectives describe the preparation: removing enema faults, auspicious.",
            "शिवः = auspicious, benign (adjective)."),
        multi("apply", 4,
              "Which of these does verse 8 name?",
              [("Asafoetida (हिङ्गु)", "Named in line 1."),
               ("Rāsnā (रास्ना)", "Named in line 2."),
               ("Licorice (यष्टीमधु)", "Licorice is in verse 4, not here."),
               ("Rock salt (सैन्धव)", "Named in line 1."),
               ("Cow's urine (गोमूत्र)", "Cow's urine is in verse 10."),
               ("Vacā (वचा)", "Vacā is in verse 7.")],
              [0, 1, 3],
              "Readable items: decoction, honey, śatāhvā, asafoetida, rock salt, suradāru, rāsnā.",
              "Verse 8: मधु · शताह्वा · हिङ्गु · सैन्धव · सुरदारु · रास्ना."),
        mcq("transfer", 5,
            "Like बस्तिदोषहरः (removing the faults of the enema), what does an invented शूलहरः mean (शूल = pain)?",
            ("Removing pain", "-हर at the end of a compound = removing X."),
            [("Born of pain", "That would be शूलज (with -ज, born)."),
             ("Full of pain", "That would need a word like -पूर्ण."),
             ("Conquered by pain", "-हर is active: it removes; it is not overcome.")],
            "Same build as बस्तिदोषहरः: X + हर = removing X.",
            "X-हर = removing X.",
            teaches="A compound ending in -हर means 'removing X': बस्तिदोषहरः, शूलहरः."),
    ],
}

# ---------------------------------------------------------------- unit 9
AUTHORED["9"] = {
    "title": "सिद्धबस्तिरिति स्मृतः",
    "question": "Which ingredients make the enema that verse 9 calls the siddhabasti?",
    "rule": ("A decoction of the pañcamūla (five roots), oil, māgadhikā (long pepper) and "
             "honey, with rock salt and madhuka (probably licorice): this is called the "
             "siddhabasti."),
    "limits": ("Which pañcamūla (the lesser or the greater five) is not stated. समधुकः could "
               "also be read 'with honey'; honey is already named, so madhuka is taken "
               "(probable), and no question rests on it. No measure or use is given here."),
    "explain_hi": ("यह श्लोक उस बस्ति को बताता है जिसे ‘सिद्धबस्ति’ कहा गया है (‘इति स्मृतः’ = ऐसा कहा गया है)। "
                   "द्रव्य हैं: पंचमूल यानी पाँच जड़ों के समूह का काढ़ा, तैल, मागधिका यानी पिप्पली और मधु; "
                   "फिर सैन्धव सहित और मधुक यानी सम्भवतः मुलेठी सहित। "
                   "कौन-सा पंचमूल (छोटा या बड़ा) है, यह नहीं कहा गया।"),
    "hook": "पंचमूल-काढ़ा, तैल, पीपर, मधु, सैन्धव, मधुक = सिद्धबस्ति।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "What does verse 9 say this enema is called?",
            ("Siddhabasti (सिद्धबस्ति)", "सिद्धबस्तिरिति स्मृतः = it is called the siddhabasti."),
            [("Yuktaratha (युक्तरथ)", "That is the enema of verse 7."),
             ("Mādhutailika (माधुतैलिक)", "That is the nirūha of verse 3."),
             ("Yāpana (यापन)", "The yāpana is in verses 5-6.")],
            "The verse closes by naming the enema: siddhabasti.",
            "... सिद्धबस्तिरिति स्मृतः = ... is called the siddhabasti."),
        match(1, "Match each word of verse 9 to its meaning.",
              [["पञ्चमूल", "the group of five roots"], ["मागधिका", "long pepper"],
               ["तैल", "oil"], ["सैन्धव", "rock salt"]],
              "Four of the ingredients of the siddhabasti.",
              "पञ्चमूल = five roots; मागधिका = long pepper; तैल = oil; सैन्धव = rock salt."),
        order(2, "Put these ingredients in the order of verse 9.",
              ["पञ्चमूलनिःक्वाथ", "तैल", "मागधिका", "मधु", "सैन्धव"],
              "Line 1: decoction of the five roots, oil, māgadhikā, honey; line 2: with rock salt (and madhuka).",
              "पञ्चमूलस्य निःक्वाथः · तैलम् · मागधिका · मधु ‖ ससैन्धवः.",
              role="extend",
              teaches="The siddhabasti of verse 9: pañcamūla decoction, oil, māgadhikā, honey, with rock salt."),
        mcq("discriminate", 3, "Which split of निःक्काथस्तैलं (read निःक्वाथस्तैलम्) is right?",
            ("निःक्वाथः + तैलम्", "A visarga before त becomes स्: निःक्वाथः + तैलम् = निःक्वाथस्तैलम्."),
            [("निःक्वाथ + स्तैलम्", "स्तैलम् is not a word; the स् is the changed visarga."),
             ("निःक्वाथे + तैलम्", "-ए + त would stay -े त; it would not give स्त."),
             ("निःक्वाथम् + तैलम्", "म् before त would become ं or न्, not स्.")],
            "Two nominatives: the decoction and the oil.",
            "Visarga + त → स्त."),
        mcq("apply", 4, "Which root group gives the decoction of verse 9?",
            ("The pañcamūla (five roots)", "पञ्चमूलस्य निःक्वाथः = decoction of the pañcamūla."),
            [("The dvipañcamūla (ten roots)", "The ten roots are cooked in verse 10."),
             ("Castor root alone", "Castor root gives the decoction in verses 3 and 7."),
             ("Triphalā (the three fruits)", "Triphalā is in verse 10, and it is a fruit group.")],
            "Verse 9 uses the five-root group; which one of the two pañcamūlas is not stated.",
            "सिद्धबस्ति: पञ्चमूल-निःक्वाथ."),
        mcq("transfer", 5,
            "Like सिद्धबस्तिः + इति = सिद्धबस्तिरिति, how does an invented कृमिः + इति join?",
            ("कृमिरिति", "A visarga after इ becomes र् before a vowel."),
            [("कृमिःइति", "The visarga does not stay before a vowel."),
             ("कृमीति", "That would be कृमि + इति with no visarga."),
             ("कृमिसिति", "स् replaces a visarga before त-type sounds, not before a vowel.")],
            "Same rule as बस्तिः + इति → बस्तिरिति.",
            "-इः + vowel → -इर् + vowel.",
            teaches="A visarga after a vowel other than अ/आ becomes र् before a vowel: बस्तिः + इति → बस्तिरिति."),
    ],
}

# ---------------------------------------------------------------- unit 10
AUTHORED["10"] = {
    "title": "द्विपञ्चमूलत्रिफला",
    "question": "What does verse 10 tell one to cook, in what liquid, and with which pastes?",
    "rule": ("One should cook the dvipañcamūla (ten roots), triphalā, fruit (phala) and bilva "
             "(bael) in cow's urine; with it go ground pastes of pāṭhā, vatsaka (probably "
             "kuṭaja) and toyada (probably musta). The sentence continues in verse 11."),
    "limits": ("तेनै is not a form; 'tena' (by that) is a possible reading that leaves the "
               "construction open, so no question uses it. 'phala' is not specified. pāṭhā, "
               "vatsaka and toyada are probable identifications."),
    "explain_hi": ("यह श्लोक गोमूत्र-बस्ति की तैयारी शुरू करता है। द्विपंचमूल (दोनों पंचमूल, यानी दस जड़ें), त्रिफला, फल और बिल्व यानी बेल को "
                   "गोमूत्र में पकाए (‘पाचयेत्’)। "
                   "दूसरी पंक्ति में पाठा, वत्सक यानी सम्भवतः कुटज और तोयद यानी सम्भवतः नागरमोथा के पिसे हुए (कल्क) आते हैं। "
                   "छपा ‘तेनै’ ठीक रूप नहीं है, इसलिए इनका ठीक सम्बन्ध खुला है। वाक्य अगले श्लोक में चलता है।"),
    "hook": "दस जड़ें, त्रिफला, फल, बेल गोमूत्र में पकाओ; पाठा-कुटज-मोथा की लुगदी।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "In which liquid does verse 10 say the drugs are cooked?",
            ("Cow's urine (गोमूत्र)", "पाचयेत् गोमूत्रे = one should cook in cow's urine."),
            [("Milk", "No milk is named in this verse."),
             ("A castor-root decoction", "That base is in verses 3 and 7."),
             ("Honey water", "Honey is not named in this verse.")],
            "गोमूत्रे is a locative: in cow's urine.",
            "पाचयेत् ... गोमूत्रे = cook in cow's urine."),
        order(1, "Put the drugs to be cooked in the order of verse 10.",
              ["द्विपञ्चमूल", "त्रिफला", "फल", "बिल्व"],
              "The compound runs dvipañcamūla, triphalā, phala, bilva, then पाचयेत्.",
              "द्विपञ्चमूल · त्रिफला · फल · बिल्व."),
        match(2, "Match each drug of verse 10 to its meaning on the card.",
              [["वत्सक", "probably kuṭaja"], ["तोयद", "probably musta (lit. water-giver)"],
               ["बिल्व", "bael"], ["त्रिफला", "the three fruits"]],
              "Two paste drugs and two cooked drugs, with the card's identifications.",
              "वत्सक = probably kuṭaja; तोयद = probably musta; बिल्व = bael; त्रिफला = the three fruits.",
              role="extend",
              teaches="In verse 10, vatsaka (probably kuṭaja) and toyada (probably musta) are ground drugs; bilva and triphalā are cooked."),
        mcq("discriminate", 3, "What does द्विपञ्चमूल mean on the card?",
            ("Ten roots: two pañcamūlas", "द्वि + पञ्चमूल = both pañcamūlas, ten roots."),
            [("Two of the five roots", "द्वि multiplies the group; it does not pick two roots."),
             ("The five roots cooked twice", "द्वि goes with the group, not with the cooking."),
             ("Five roots and two fruits", "No fruits are counted in this word.")],
            "A number before a group name doubles the group: two pañcamūlas.",
            "द्विपञ्चमूल = 2 × पञ्चमूल = ten roots."),
        mcq("apply", 4, "Which drugs of verse 10 are added as ground pastes (पिष्टैः) rather than cooked?",
            ("Pāṭhā, vatsaka and toyada", "पिष्टैः पाठावत्सकतोयदैः = with the ground ones of these three."),
            [("Triphalā, phala and bilva", "These are in the list that is cooked (पाचयेत्)."),
             ("The ten roots alone", "The roots are cooked in cow's urine."),
             ("Honey, oil and kṣāra", "These come in verse 11.")],
            "Line 1 lists what is cooked; line 2 lists the ground pastes.",
            "पाचयेत्: द्विपञ्चमूल … बिल्व · पिष्टैः: पाठा, वत्सक, तोयद."),
        mcq("transfer", 5,
            "Like त्रिफला (the three fruits), what does an invented त्रिकटु name (कटु = pungent)?",
            ("A group of three pungent drugs", "A number + noun names a group of that many, as त्रिफला."),
            [("One drug that is three times as pungent", "त्रि counts the members; it does not intensify."),
             ("A drug pungent in three seasons", "No season is in the word."),
             ("Three doses of one pungent drug", "The word names a group, not a dose.")],
            "Same build as त्रिफला and पञ्चमूल: number + item = a group of that many.",
            "Number + noun = a named group (त्रिफला, पञ्चमूल).",
            teaches="A compound of a number and a noun names a group of that many items: त्रिफला, पञ्चमूल, त्रिकटु."),
    ],
}

# ---------------------------------------------------------------- unit 11
AUTHORED["11"] = {
    "title": "युक्तो बस्तिः कफव्याधिषु",
    "question": "What is added to the cow's-urine preparation in verse 11, and in which disorders is it suitable?",
    "rule": ("With fruits, with honey and oil, with kṣāra and with salt, the enema is "
             "suitable in Kapha disorders, in pāṇḍu disease (anaemia with pallor) and in "
             "visūcī (acute vomiting and purging); the sentence goes on in verse 12."),
    "limits": ("Line 1 continues the instrumentals of verse 10; the praise (पूजितः) is in verse "
               "12. The fruits are not named. visūcī as a cholera-like illness is probable. "
               "युक्तः 'suitable' is literally 'joined, applied'."),
    "explain_hi": ("यह श्लोक पिछले श्लोक की गोमूत्र वाली तैयारी को आगे बढ़ाता है: फलों सहित, मधु और तैल दोनों से, क्षार से और लवण से। "
                   "फिर कहता है कि यह बस्ति कफ-व्याधियों में, पाण्डु-रोग यानी फीकेपन वाली रक्ताल्पता में और विसूची यानी उलटी-दस्त वाली तीव्र बीमारी में उपयुक्त है। "
                   "‘-षु’ सप्तमी बहुवचन है: ‘में’। "
                   "फल कौन-से हैं, यह नहीं बताया; वाक्य अगले श्लोक में ‘पूजितः’ पर आगे चलता है।"),
    "hook": "फल, मधु-तैल, क्षार, लवण: कफ, पाण्डु, विसूची में बस्ति।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "In which disorders does verse 11 say the enema is suitable?",
            ("Kapha disorders, pāṇḍu and visūcī", "कफव्याधि-पाण्डुरोग-विसूचिषु = in these three."),
            [("Vāta disorders, raktapitta and eye disease", "None of these is named in verse 11."),
             ("Worms, gulma and intestinal hernia", "These are in verse 4."),
             ("Pain of the anus, knee and thigh", "These are in verse 5.")],
            "The locative compound names three: Kapha disorders, pāṇḍu disease, visūcī.",
            "युक्तो बस्तिः कफव्याधि-पाण्डुरोग-विसूचिषु."),
        match(1, "Match each word of verse 11 to its meaning.",
              [["क्षौद्र", "honey"], ["लवण", "salt"],
               ["पाण्डुरोग", "anaemia with pallor"], ["विसूची", "acute vomiting and purging"]],
              "Two added substances and two of the disorders.",
              "क्षौद्र = honey; लवण = salt; पाण्डुरोग = anaemia with pallor; विसूची = acute vomiting and purging."),
        order(2, "Put the added items of line 1 in the order of verse 11.",
              ["सफलैः", "क्षौद्रतैलाभ्याम्", "क्षारेण", "लवणेन"],
              "Line 1: with fruits, with honey and oil, with kṣāra, with salt.",
              "सफलैः · क्षौद्रतैलाभ्याम् · क्षारेण · लवणेन च.",
              role="extend",
              teaches="Verse 11 adds, in order: fruits, honey and oil, kṣāra, salt."),
        mcq("discriminate", 3, "Which case is विसूचिषु, and what does it mean here?",
            ("Locative plural: 'in'", "-षु is the locative plural ending: 'in'."),
            [("Instrumental plural: 'with'", "The instrumental plural would end in -भिः."),
             ("Genitive plural: 'of'", "The genitive plural would end in -नाम्."),
             ("Dative plural: 'for'", "The dative plural would end in -भ्यः.")],
            "The disorders stand in the locative: the enema is suitable in them.",
            "-षु = locative plural, 'in'."),
        mcq("apply", 4, "Does verse 11 name the fruits that are added (सफलैः)?",
            ("No; it says only 'with fruits'", "स-फलैः = with fruits; no fruit is named."),
            [("Yes; they are madana fruits", "No madana is named in verse 11."),
             ("Yes; they are the triphalā", "Triphalā is cooked in verse 10; सफलैः names none."),
             ("Yes; they are bilva fruits", "Bilva is in verse 10; सफलैः names none.")],
            "The card says the fruits are not named.",
            "सफलैः = with fruits (unnamed)."),
        mcq("transfer", 5,
            "Like क्षौद्रतैलाभ्याम् (with honey and oil), which invented form means with ghee and honey (घृत, मधु)?",
            ("घृतमधुभ्याम्", "-भ्याम् is the instrumental dual: two things, 'with'."),
            [("घृतमधुभिः", "-भिः is plural, for three or more."),
             ("घृतमधुना", "-ना is singular."),
             ("घृतमधुनोः", "-नोः is genitive or locative dual, not 'with'.")],
            "A dvandva of two items takes the dual: क्षौद्रतैलाभ्याम्, घृतमधुभ्याम्.",
            "-भ्याम् = instrumental (or dative/ablative) dual.",
            teaches="A dvandva of two items in the instrumental takes the dual ending -भ्याम्: क्षौद्रतैलाभ्याम्, घृतमधुभ्याम्."),
    ],
}


NOTES_HI = {
    "1": ("विश्वास: उच्च। अध्याय का आरम्भ-सूत्र। संधि जाँची: अथातः = अथ + अतः (अ + अ → आ); विसर्ग ‘सिद्ध-’ के स से पहले बना रहता है। "
          "‘सिद्धबस्तिकल्पं’ में अन्त का ं = म्। छपा ‘वस्ति’ सब जगह ‘बस्ति’ पढ़ा गया है। पाठभेद या दूषित अंश नहीं।"),
    "2": ("विश्वास: मध्यम। दो सुझाव (text_flags): छपा ‘वलबुद्धि’ सम्भवतः ‘बलबुद्धि’ (व/ब की अदला-बदली); ‘निर्व्यापदो’ प्रथमा एकवचन है, "
          "जबकि बाकी विशेषण द्वितीया बहुवचन हैं, इसलिए सम्भवतः ‘निर्व्यापदान्’ होना चाहिए। इसी कारण इसके रूप पर प्रश्न नहीं बना। "
          "‘बल-बुद्धि-करान्’ समास छपाई में दो टुकड़ों में टूटा है। ‘सर्वदेहिनाम्’ षष्ठी है: ‘सबके लिए’ या ‘सबका’। "
          "संधि जाँची: निर्व्यापदो बहु… = निर्व्यापदः + बहु… (अः → ओ सघोष से पहले); सिद्धबस्तीन्प्रयुंजीत = सिद्धबस्तीन् + प्रयुञ्जीत।"),
    "3": ("विश्वास: निम्न। पंक्ति १ बिना क्रिया की मात्राओं की सूची है; ‘कर्षः’ और ‘सैन्धवात् द्विपिचुः’ किस द्रव्य से जुड़ते हैं, स्पष्ट नहीं "
          "(एक सम्भावित पाठ: एक कर्ष सैन्धव, दो पिचु मिशि; लागू नहीं किया)। छपा ‘काथेन’ सम्भवतः ‘क्वाथेन’ (व छूटा)। "
          "मिशि = सोया (Anethum sowa), विवादित; सौंफ़ भी कही जाती है। खुला अवलोकन: ‘माधुतैलिक’ सम्भवतः इस निरूह का नाम है। "
          "संधि जाँची: सैंधवाद्द्विपिचुर्मिशिः = सैन्धवात् + द्विपिचुः + मिशिः (त् → द्; उः → उर् सघोष से पहले); निरूहो माधु… = निरूहः + माधु…।"),
    "4": ("विश्वास: उच्च। श्लोक ३ के निरूह के गुण, बिना क्रिया। ‘रसायनम्’ नपुंसक है, विधेय के रूप में (‘यह रसायन है’)। "
          "‘प्रमेहार्शः’ का विसर्ग समास के बीच अटपटा है: छपाई की भूल हो सकती है या ‘अर्शः’ अलग शब्द; सूची वाला पाठ रखा गया। "
          "पहचान: अर्श = बवासीर (मानक), प्रमेह = मधुमेह से जुड़े मूत्र-विकार (सम्भावित), अन्त्रवृद्धि = हर्निया (मानक), यष्टीमधु = मुलेठी (मानक), रक्तपित्त (सम्भावित)। "
          "संधि जाँची: प्रमेहार्शः = प्रमेह + अर्शः (अ + अ → आ); गुल्मांत्र = गुल्म + अन्त्र; सयष्टीमधुकश्चैव = …कः + च + एव (ः → श् च से पहले; अ + ए → ऐ); चक्षुष्यो रक्त… = चक्षुष्यः + रक्त…।"),
    "5": ("विश्वास: निम्न। छपा ‘पृष्टशण’ कोई शब्द नहीं है; ‘पृष्ठ-श्रोणि’ (पीठ, कूल्हा) केवल सुझाव है, इसलिए इस पर प्रश्न नहीं बना। "
          "‘मेहन शूलजित्’ के बीच का स्थान और ‘मेहन’ का अन्त भी संदिग्ध है (text_flags)। कल्क के द्रव्य यहाँ नहीं हैं। "
          "संधि जाँची: यापनो घन… = यापनः + घन…; मधुतैलवसाज्यवान् = मधु + तैल + वसा + आज्य + वान् (आ + आ → आ); जानूरु = जानु + ऊरु (उ + ऊ → ऊ)।"),
    "6": ("विश्वास: उच्च। छपा ‘अर्द्ध’ = अर्ध (दोहरा द्द सामान्यीकृत)। ‘आधा अक्ष सैन्धव’ और ‘आधा पल हपुषा’ स्वाभाविक विभाजन है, पर समास में कोई अलग करने वाला शब्द नहीं। "
          "प्रसृत = एक मान (मानक तालिकाओं में लगभग दो पल); ग्राम में नहीं बदला गया। हपुषा = हाऊबेर (Juniperus communis, सम्भावित)। "
          "संधि जाँची: प्रसृतांशैर्घृत = प्रसृत + अंशैः + घृत (अ + अ → आ; ऐः → ऐर् सघोष से पहले); सैंधवार्द्धाक्ष = सैन्धव + अर्ध + अक्ष; हपुषार्द्धपलान्वितं = हपुषा + अर्ध + पल + अन्वितम्।"),
    "7": ("विश्वास: मध्यम। छपा ‘निःक्काथो’ सम्भवतः ‘निःक्वाथो’ (दोहरा क और छूटा व छपाई की भूल)। ‘सवचापिप्पली फलः’ एक बहुव्रीहि है, बीच में छपा स्थान; "
          "‘फल’ का नाम नहीं, ‘पिप्पली-फल’ भी पढ़ा जा सकता है। डेटा का नोट पंक्ति १ को पिछले यापन का भाग कहता है, पर श्लोक स्वयं ‘एष युक्तरथो बस्तिः’ कहता है। "
          "पहचान: वचा = बच (मानक), पिप्पली = पीपर (मानक)। संधि जाँची: निःक्वाथो मधु = निःक्वाथः + मधु; एष युक्तरथो = एषः + युक्त… (एषः का विसर्ग व्यंजन से पहले लुप्त); युक्तरथो बस्तिः = युक्तरथः + बस्तिः।"),
    "8": ("विश्वास: निम्न। ‘पैंढुंथा’ छपाई में दूषित है; छन्द के अनुसार तीन अक्षर का कोई द्रव्य-नाम अपेक्षित है, पर पहचान नहीं (खुला अवलोकन)। "
          "छपा ‘सकाथो’ सम्भवतः ‘सक्वाथो’; ‘शताव्हा’ सम्भवतः ‘शताह्वा’ (अक्षर उलटे)। शताह्वा = सोया (सम्भावित), सुरदारु = देवदार (मानक), रास्ना = विवादित। "
          "‘बस्तिदोष’ को डेटा बस्ति (एनीमा) के दोष पढ़ता है। संधि जाँची: सक्वाथो मधु = सक्वाथः + मधु; अन्य शब्द अलग-अलग छपे हैं।"),
    "9": ("विश्वास: उच्च। छपा ‘निःक्काथ’ सम्भवतः ‘निःक्वाथ’। कौन-सा पंचमूल (लघु या बृहत्) है, नहीं कहा। "
          "‘समधुकः’ दो तरह पढ़ा जा सकता है: स-मधुकः (मुलेठी सहित, सम्भावित) या स-मधु-कः (मधु सहित); मधु पहले आ चुका है, इसलिए मधुक लिया गया; इस पर प्रश्न नहीं बना। "
          "संधि जाँची: निःक्वाथस्तैलं = निःक्वाथः + तैलम् (ः → स् त से पहले); सिद्धबस्तिरिति = सिद्धबस्तिः + इति (इः → इर् स्वर से पहले)।"),
    "10": ("विश्वास: मध्यम। छपा ‘विल्वानि’ = बिल्वानि। ‘तेनै’ कोई रूप नहीं; ‘तेन’ (उससे) सुझाव है, पर इससे वाक्य-रचना स्पष्ट नहीं होती (खुला अवलोकन), इसलिए इस पर प्रश्न नहीं बना। "
           "‘फल’ अनिर्दिष्ट है, पिछले शब्द से भी जुड़ सकता है। पहचान: बिल्व = बेल (मानक), पाठा (सम्भावित), वत्सक = कुटज (सम्भावित), तोयद = नागरमोथा (सम्भावित)। "
           "संधि जाँची: पिष्टैश्च = पिष्टैः + च (ः → श् च से पहले); त्रिफलाफल = त्रिफला + फल। क्रिया ‘पाचयेत्’ पंक्ति १ में है; वाक्य श्लोक ११ में चलता है।"),
    "11": ("विश्वास: उच्च। छपा ‘ळ’ (सफळैः) साधारण ‘ल’ पढ़ा गया (छपाई की आदत)। पंक्ति १ श्लोक १० के तृतीया रूपों को आगे बढ़ाती है; ‘पूजितः’ श्लोक १२ में है। "
           "‘युक्तः’ = उपयुक्त (शाब्दिक: जुड़ा, प्रयुक्त)। पहचान: पाण्डुरोग = रक्ताल्पता (मानक), विसूची = हैज़े जैसी बीमारी (सम्भावित)। "
           "संधि जाँची: युक्तो बस्तिः = युक्तः + बस्तिः (अः → ओ सघोष से पहले); क्षौद्रतैलाभ्यां = क्षौद्र + तैल + आभ्याम् (तृतीया द्विवचन)।"),
}

AIDS = {
    "1": {
        "frame": "कब: अथ (अब) · क्यों: अतः (इसलिए) · क्या: सिद्धबस्ति-कल्प · कौन करेगा: हम (व्याख्यास्यामः)।",
        "sandhi": "अ + अ → आ: अथ + अतः → अथातः। विसर्ग ‘स’ से पहले बना रहा; ‘ब’ जैसे सघोष से पहले वह ‘ओ’ बनता (अथातो)।",
        "anchors": "अथ = अब · अतः = इसलिए · सिद्ध = आज़माया हुआ · कल्प = विधि · व्याख्या = समझाना।",
    },
    "2": {
        "diagram": {"groups": [{"label": "किसके लिए, कब", "items": ["सर्वदेहिनाम्", "सर्वदा"]},
                               {"label": "चार गुण", "items": ["निर्व्यापद्", "बहुफल", "बल-बुद्धि-कर", "सुख"]}]},
        "chunks": "सिद्धबस्तीन्प्रयुंजीत | सर्वदा सर्वदेहिनां ‖ निर्व्यापदो बहुफलान् | वलबुद्धि करान्सुखान्।",
        "sandhi": "अः → ओ सघोष से पहले: निर्व्यापदः + बहु → निर्व्यापदो बहु; न् + प: सिद्धबस्तीन् + प्रयुञ्जीत (बदलाव नहीं)।",
        "anchors": "प्रयुञ्जीत = प्रयोग करना चाहिए · देही = देहधारी · व्यापद् = विपत्ति · फल = लाभ · सुख = सुखद।",
    },
    "3": {
        "frame": "क्या: निरूह (काढ़े की बस्ति) · आधार: एरण्ड-मूल का काढ़ा · बराबर: मधु और तैल · और: सैन्धव, मिशि (मात्राओं का सम्बन्ध अस्पष्ट) · नाम: माधुतैलिक।",
        "sandhi": "त् → द् सघोष से पहले: सैन्धवात् + द्वि → सैन्धवाद्द्वि; उः → उर्: द्विपिचुः + मिशिः → द्विपिचुर्मिशिः।",
        "anchors": "मधु = शहद · तैल = तेल · सम = बराबर · कर्ष, पिचु = तौल के मान · मूल = जड़ · माधुतैलिक = मधु-तैल वाला।",
    },
    "4": {
        "diagram": {"groups": [{"label": "निरूह", "items": ["रसायन"]},
                               {"label": "दूर करता है", "items": ["प्रमेह", "अर्श", "कृमि", "गुल्म", "अन्त्रवृद्धि"]},
                               {"label": "मुलेठी के साथ", "items": ["चक्षुष्य", "रक्तपित्तजित्"]}]},
        "chunks": "रसायनं प्रमेहार्शः | कृमिगुल्मांत्रवृद्धिनुत् ‖ सयष्टीमधुकश्चैव | चक्षुष्यो रक्तपित्तजित्।",
        "sandhi": "अ + अ → आ: प्रमेह + अर्शः → प्रमेहार्शः; अः → ओ: चक्षुष्यः + रक्त → चक्षुष्यो रक्त।",
        "anchors": "-नुत् = दूर करने वाला · -जित् = जीतने वाला · चक्षुष्य = आँखों के लिए हितकर · यष्टीमधु = मुलेठी।",
    },
    "5": {
        "frame": "क्या: यापन बस्ति · साथ: गाढ़ा कल्क · स्नेह-मधु: मधु, तैल, वसा, घी · पीड़ा जीते: गुदा, घुटना, जाँघ, (अस्पष्ट), बस्ति-प्रदेश, लिंग।",
        "chunks": "यापनो घनकल्केन | मधुतैलवसाज्यवान् ‖ पायुजानूरु (पृष्टशण अस्पष्ट) बस्तिमेहन | शूलजित्।",
        "sandhi": "आ + आ → आ: वसा + आज्य → वसाज्य; उ + ऊ → ऊ: जानु + ऊरु → जानूरु।",
        "anchors": "घन = गाढ़ा · कल्क = लुगदी · वसा = चर्बी · आज्य = घी · पायु = गुदा · जानु = घुटना · ऊरु = जाँघ।",
    },
    "6": {
        "diagram": {"groups": [{"label": "प्रसृत के अंश", "items": ["घृत", "क्षौद्र", "वसा", "तैल"]},
                               {"label": "आधे मान", "items": ["सैन्धव: आधा अक्ष", "हपुषा: आधा पल"]}]},
        "chunks": "प्रसृतांशैर्घृतक्षौद्र- | वसातैलैः प्रकल्पयेत् ‖ यापनं सैंधवार्द्धाक्ष- | हपुषार्द्धपलान्वितं।",
        "sandhi": "ऐः → ऐर् सघोष से पहले: अंशैः + घृत → अंशैर्घृत; अ + अ → आ: सैन्धव + अर्ध → सैन्धवार्ध।",
        "anchors": "क्षौद्र = शहद · अंश = भाग · अर्ध = आधा · अक्ष, पल = तौल के मान · अन्वित = से युक्त।",
    },
    "7": {
        "diagram": {"groups": [{"label": "पंक्ति १", "items": ["एरण्ड-मूल का काढ़ा", "मधु", "तैल", "सैन्धव"]},
                               {"label": "पंक्ति २", "items": ["वचा", "पिप्पली", "फल"]}]},
        "chunks": "एरंडमूलनिःक्काथो | मधु तैलं ससैंधवं ‖ एष युक्तरथो बस्तिः | सवचापिप्पली फलः।",
        "pegs": "मेरा बनाया चित्र (श्लोक का दावा नहीं): ‘युक्तरथ’ = जुता हुआ रथ; रथ में सात सवार सोचें: काढ़ा, मधु, तैल, सैन्धव, बच, पीपर, फल।",
        "anchors": "निःक्वाथ = काढ़ा · स- = सहित · वचा = बच · पिप्पली = पीपर · एष = यह।",
    },
    "8": {
        "frame": "साथ: काढ़ा · द्रव्य: मधु, (अस्पष्ट), शताह्वा, हिङ्गु, सैन्धव, सुरदारु, रास्ना · गुण: बस्ति-दोष हरे, शिव।",
        "chunks": "सकाथो मधु पैंढुंथा (अस्पष्ट) | शताव्हा हिंगु सैंधवं ‖ सुरदारु च रास्ना च | बस्तिदोषहरः शिवः।",
        "anchors": "हिङ्गु = हींग · सुरदारु = देवदार · शताह्वा = सम्भवतः सोया · -हर = हरने वाला · शिव = कल्याणकारी।",
    },
    "9": {
        "diagram": {"groups": [{"label": "पंक्ति १", "items": ["पञ्चमूल का काढ़ा", "तैल", "मागधिका", "मधु"]},
                               {"label": "पंक्ति २", "items": ["सैन्धव सहित", "मधुक सहित (सम्भावित)"]}]},
        "chunks": "पंचमूलस्य निःक्काथस् | तैलं मागधिका मधु ‖ ससैंधवः समधुकः | सिद्धबस्तिरिति स्मृतः।",
        "sandhi": "ः → स् त से पहले: निःक्वाथः + तैलम् → निःक्वाथस्तैलम्; इः → इर् स्वर से पहले: बस्तिः + इति → बस्तिरिति।",
        "contrast": "श्लोक ७ ↔ ९: दोनों में मधु, तैल, सैन्धव और पिप्पली (मागधिका); काढ़ा अलग: ७ में एरण्ड-मूल, ९ में पंचमूल। नाम: युक्तरथ ↔ सिद्धबस्ति।",
    },
    "10": {
        "chain": {"steps": ["द्विपञ्चमूल, त्रिफला, फल, बिल्व", "गोमूत्र में पकाए (पाचयेत्)",
                            "पिसे हुए पाठा, वत्सक, तोयद के साथ", "आगे: श्लोक ११"]},
        "chunks": "द्विपंचमूलत्रिफला- | फलविल्वानि पाचयेत् ‖ गोमूत्रे तेनै (अस्पष्ट) पिष्टैश्च | पाठावत्सकतोयदैः।",
        "anchors": "द्वि = दो · पञ्चमूल = पाँच जड़ें · त्रिफला = तीन फल · बिल्व = बेल · गोमूत्र = गाय का मूत्र · पिष्ट = पिसा हुआ।",
    },
    "11": {
        "diagram": {"groups": [{"label": "साथ में", "items": ["फल", "मधु और तैल", "क्षार", "लवण"]},
                               {"label": "उपयुक्त", "items": ["कफ-व्याधि", "पाण्डु-रोग", "विसूची"]}]},
        "chunks": "सफळैः क्षौद्रतैलाभ्यां | क्षारेण लवणेन च ‖ युक्तो बस्तिः कफव्याधि- | पांडुरोगविसूचिषु।",
        "sandhi": "अः → ओ सघोष से पहले: युक्तः + बस्तिः → युक्तो बस्तिः।",
        "anchors": "क्षौद्र = शहद · लवण = नमक · -आभ्याम् = दो से · -षु = में · विसूची = उलटी-दस्त वाली तीव्र बीमारी।",
    },
}

IMAGE_SPECS = {
    ("2", "diagram"): {
        "file": "ka5-siddhabasti-guna-2.svg",
        "alt": "Mind map: siddhabastis for all embodied beings at all times; four qualities: free from mishap, of many benefits, producing strength and intelligence, pleasant",
        "type": "mermaid",
        "code": ('mindmap\n  सिद्धबस्तियाँ\n    किसके लिए\n      सब देहधारी\n      सदा\n'
                 '    चार गुण\n      बिना विपत्ति\n      बहुत फल\n      बल और बुद्धि\n      सुखद\n'),
    },
    ("4", "diagram"): {
        "file": "ka5-madhutailika-guna-4.svg",
        "alt": "Mind map of the honey-oil nirūha: rejuvenating; dispels prameha, haemorrhoids, worms, gulma, hernia; with licorice good for the eyes and conquers raktapitta",
        "type": "mermaid",
        "code": ('mindmap\n  माधुतैलिक निरूह\n    रसायन\n    दूर करता है\n      प्रमेह\n      अर्श\n'
                 '      कृमि\n      गुल्म\n      अन्त्रवृद्धि\n    मुलेठी के साथ\n      आँखों का हित\n      रक्तपित्त जीते\n'),
    },
    ("6", "diagram"): {
        "file": "ka5-yapana-mana-6.svg",
        "alt": "Table of the yāpana's measures: ghee, honey, fat and oil in prasṛta portions; rock salt half an akṣa; hapuṣā half a pala",
        "type": "table",
        "title": "श्लोक ६: यापन की मात्राएँ",
        "heads": ["द्रव्य", "मात्रा"],
        "rows": [["घी, शहद, वसा, तैल", "प्रसृत के अंश"], ["सैन्धव", "आधा अक्ष"],
                 ["हपुषा", "आधा पल"]],
    },
    ("7", "diagram"): {
        "file": "ka5-yuktaratha-7.svg",
        "alt": "Mind map of the yuktaratha enema: castor-root decoction, honey, oil, rock salt, sweet flag, long pepper, fruit",
        "type": "mermaid",
        "code": ('mindmap\n  युक्तरथ बस्ति\n    पंक्ति एक\n      एरण्ड-जड़ का काढ़ा\n      मधु\n      तैल\n'
                 '      सैन्धव\n    पंक्ति दो\n      वचा\n      पिप्पली\n      फल\n'),
    },
    ("9", "diagram"): {
        "file": "ka5-siddhabasti-dravya-9.svg",
        "alt": "Mind map of the siddhabasti: decoction of the five roots, oil, long pepper, honey, with rock salt and with madhuka (probable)",
        "type": "mermaid",
        "code": ('mindmap\n  सिद्धबस्ति\n    पंक्ति एक\n      पंचमूल का काढ़ा\n      तैल\n      मागधिका\n'
                 '      मधु\n    पंक्ति दो\n      सैन्धव सहित\n      सम्भवतः मधुक सहित\n'),
    },
    ("10", "chain"): {
        "file": "ka5-gomutra-paka-10.svg",
        "alt": "Chain of four steps: ten roots, triphala, fruit and bael; cooked in cow's urine; with ground pastes of patha, vatsaka and toyada; continues in verse 11",
        "type": "chain",
        "title": "श्लोक १०: गोमूत्र में पाक",
        "steps": ["दस जड़ें, त्रिफला, फल, बेल", "गोमूत्र में पकाए", "पिसे पाठा, वत्सक, तोयद के साथ",
                  "आगे: श्लोक ११"],
    },
    ("11", "diagram"): {
        "file": "ka5-gomutra-basti-11.svg",
        "alt": "Flowchart: with fruits, honey and oil, kshara and salt, the enema is suitable in three disorders: Kapha disorders, pandu disease and visuchi",
        "type": "mermaid",
        "code": ('flowchart TD\n  A["फल, मधु-तैल, क्षार, लवण"] --> B["यह बस्ति उपयुक्त है"]\n'
                 '  B --> C["कफ-व्याधि"]\n  B --> D["पाण्डु-रोग"]\n  B --> E["विसूची"]\n'),
    },
}
