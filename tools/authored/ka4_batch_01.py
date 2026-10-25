from helpers import mcq, match, order, fill, multi, accepts

# Kalpasthāna chapter 4 (Bastikalpa), units 1-11.
# Sections (sections_kalpa.py KA4): 1-4 balādi basti; 5-7 daśamūla and meat-broth bastis; 8-11 eraṇḍa-root nirūha.

AUTHORED = {}

# ---------------------------------------------------------------- unit 1
AUTHORED["1"] = {
    "title": "अथातो बस्तिकल्पं व्याख्यास्यामः",
    "question": "What does the opening formula of the chapter announce, and what do its words mean?",
    "rule": ("The chapter opens: now, therefore, we shall explain the Basti-kalpa. Basti is the "
             "medicated enema; kalpa is the formulary, the set of preparations."),
    "limits": ("The formula only names the topic; it gives no recipe, drug or measure. "
               "'Therefore' (अतः) points back to what came before without saying what."),
    "explain_hi": ("यह अध्याय का आरम्भ-सूत्र है, जैसा हर अध्याय के आरम्भ में आता है। ‘अथ’ का अर्थ है ‘अब’ और ‘अतः’ का ‘इसलिए’। "
                   "विषय है बस्तिकल्प: बस्ति यानी औषधीय एनीमा, और कल्प यानी उसकी बनाने की विधियों का संग्रह। "
                   "‘व्याख्यास्यामः’ भविष्यत् काल, उत्तम पुरुष बहुवचन है: ‘हम व्याख्या करेंगे’। "
                   "इस इकाई में कोई नुस्खा नहीं है; नुस्खे अगली इकाई से शुरू होते हैं।"),
    "hook": "अब इसलिए: बस्ति के कल्प, हम समझाएँगे।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "Which topic does unit 1 announce for the chapter?",
            ("The preparations for basti",
             "बस्तिकल्पम्: kalpa (set of preparations) of basti, the medicated enema."),
            [("The rules of the daily routine", "No daily routine is named; the word is बस्तिकल्प."),
             ("The preparations for nasal drops", "Nasal drops are not named; basti is the medicated enema."),
             ("The signs of a healthy body", "The formula names only the Basti-kalpa.")],
            "The formula names one topic: बस्तिकल्प, the preparations for basti (medicated enema).",
            "बस्ति = medicated enema; कल्प = set of preparations."),
        match(1, "Match each word of unit 1 to its meaning.",
              [["अथ", "now"], ["अतः", "therefore"], ["बस्ति", "medicated enema"],
               ["कल्प", "set of preparations"], ["व्याख्यास्यामः", "we shall explain"]],
              "These five words make up the whole formula.",
              "अथ = now; अतः = therefore; बस्ति = enema; कल्प = preparations; व्याख्यास्यामः = we shall explain."),
        order(2, "Put the words of the formula in the order of unit 1.",
              ["अथ", "अतः", "बस्तिकल्पम्", "व्याख्यास्यामः"],
              "Now, therefore, the Basti-kalpa, we shall explain: the topic stands before the verb.",
              "अथ · अतः · बस्तिकल्पम् · व्याख्यास्यामः.",
              role="extend",
              teaches="The opening formula runs: अथ (now), अतः (therefore), the topic in the accusative, and the verb last."),
        mcq("discriminate", 3, "Which is the right split of अथातो in unit 1?",
            ("अथ + अतः",
             "अ + अ → आ (अथा-), and -अः before a voiced sound (here ब) → -ओ."),
            [("अथा + तो", "Neither अथा nor तो is the word; the words are अथ and अतः."),
             ("अथ + आतः", "आतः is not a word here; the word is अतः, therefore."),
             ("अथः + अतो", "अथ is an indeclinable with no visarga, and the base form is अतः.")],
            "अथ (now) + अतः (therefore) = अथातो before बस्तिकल्पं.",
            "अ + अ → आ; -अः before a voiced consonant → -ओ."),
        mcq("apply", 4, "Who speaks in व्याख्यास्यामः, and when is the action set?",
            ("We, in the future",
             "The data labels it 1st person plural future: we shall explain."),
            [("He, in the present", "That would be a 3rd person singular present, like व्याख्याति."),
             ("They, in the past", "No past tense is used; -स्यामः marks the future."),
             ("You, as a command", "It is not an imperative; -स्यामः is the 'we' future ending.")],
            "व्याख्यास्यामः = 1 pl. future of वि-आ-√ख्या: we shall explain.",
            "-स्यामः = 'we shall ...' (1st person plural future)."),
        mcq("transfer", 5, "Using the same formula, which line would announce an invented Vamana-kalpa?",
            ("अथातो वमनकल्पं व्याख्यास्यामः",
             "The topic is the object, so it stays accusative (-ं / -म्), as with बस्तिकल्पम्."),
            [("अथातो वमनकल्पः व्याख्यास्यामः", "वमनकल्पः is nominative; the object of 'we shall explain' takes the accusative."),
             ("अथातो वमनकल्पं व्याख्यास्यति", "व्याख्यास्यति is 'he will explain'; the formula uses 'we'."),
             ("अथातो वमनकल्पेन व्याख्यास्यामः", "वमनकल्पेन is instrumental, 'by means of', not the object.")],
            "Only the topic word changes; it stays an accusative object of व्याख्यास्यामः.",
            "Topic in the accusative + व्याख्यास्यामः.",
            teaches="In the opening formula the topic is the accusative object (-म्) of व्याख्यास्यामः, 'we shall explain'."),
    ],
}

# ---------------------------------------------------------------- unit 2
AUTHORED["2"] = {
    "title": "बळां गुडूचीं त्रिफलां सरास्नाम्",
    "question": "Which drugs and which meat are cooked in water in verse 2, by which measures, and down to what?",
    "rule": ("Balā, guḍūcī and triphalā with rāsnā, and the ten-root group, measured by the pala; "
             "eight fruits and half a tulā of goat meat: cook in water until a quarter remains."),
    "limits": ("The verse does not list the ten roots or name the eight fruits, and gives no number of palas. "
               "Rāsnā is of disputed identity. The recipe runs on into verses 3 and 4; its use comes there. "
               "Measures stay as the text gives them."),
    "explain_hi": ("यहाँ से बलादि बस्ति का नुस्खा शुरू होता है, जो श्लोक ३ और ४ तक चलता है। पहली पंक्ति में द्रव्य हैं: बला यानी बरियार, "
                   "गुडूची यानी गिलोय, त्रिफला यानी हरड़-बहेड़ा-आँवला, रास्ना (पहचान विवादित) और द्विपंचमूल यानी दशमूल; ये पल से मापे जाते हैं। "
                   "दूसरी पंक्ति में आठ फल और आधा तुला बकरे का मांस जुड़ते हैं। सबको जल में पकाकर चौथाई शेष रखा जाता है। "
                   "दस मूलों और आठ फलों के नाम श्लोक में नहीं दिए गए हैं।"),
    "hook": "बला-गिलोय-त्रिफला-रास्ना-दशमूल, आठ फल, आधा तुला बकरा: जल में पकाओ, चौथाई बचाओ।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "How far is the mixture cooked down in verse 2?",
            ("Until a quarter remains",
             "चतुर्थशेषम्: with a fourth part remaining."),
            [("Until half of it remains", "Half (अर्द्ध) belongs to the tulā of meat, not to the cooking."),
             ("Until an eighth remains", "An eighth is the end point of the recipe in verse 9, not here."),
             ("Until no water is left", "The verse keeps a quarter; it does not boil the water away.")],
            "पचेदप्सु चतुर्थशेषम्: cook in water, with a quarter remaining.",
            "Verse 2 ends the cooking at चतुर्थशेष, a quarter."),
        match(1, "Match each drug of verse 2 to its identity as the card gives it.",
              [["बला", "country mallow"], ["गुडूची", "giloy"],
               ["त्रिफला", "the three myrobalans"], ["द्विपंचमूल", "the ten-root group"]],
              "Balā, guḍūcī and triphalā are standard identifications; dvipañcamūla is the group called daśamūla.",
              "बला = country mallow; गुडूची = giloy; त्रिफला = three myrobalans; द्विपंचमूल = ten roots."),
        order(2, "Put these drugs of verse 2, line 1, in the verse's order.",
              ["बला", "गुडूची", "त्रिफला", "रास्ना", "द्विपंचमूल"],
              "Line 1 runs balā, guḍūcī, triphalā, with rāsnā, then the ten-root group.",
              "बला · गुडूची · त्रिफला · रास्ना · द्विपंचमूल.",
              role="extend",
              teaches="Line 1 names five items in this order, all measured by the pala (पलोन्मितानि)."),
        mcq("discriminate", 3, "Which is the right split of फलान्यर्द्धतुलां in verse 2?",
            ("फलानि + अर्द्धतुलाम्",
             "इ before a different vowel becomes य्: फलानि + अर्द्ध… = फलान्यर्द्ध…."),
            [("फलान् + यर्द्धतुलाम्", "यर्द्धतुला is not a word; the measure is अर्द्धतुला, half a tulā."),
             ("फलाः + अर्द्धतुलाम्", "-आः before a vowel drops its visarga; it would not give न्य."),
             ("फल + अन्यर्द्धतुलाम्", "There is no word अन्यर्द्धतुला, and अष्टौ needs the plural फलानि.")],
            "आठ फल (अष्टौ फलानि) and half a tulā (अर्द्धतुलाम्) are two separate items.",
            "इ + different vowel → य् + vowel."),
        mcq("apply", 4, "In verse 2, what quantity of goat meat is cooked?",
            ("Half a tulā",
             "अर्द्धतुलां च मांसाच्छागात्: half a tulā of goat meat."),
            [("Eight palas", "Eight (अष्टौ) counts the fruits, not the meat."),
             ("A quarter tulā", "A quarter is what remains after cooking, not the meat."),
             ("One prastha", "No prastha is named in this verse.")],
            "The meat is in the ablative (मांसात् छागात्, from goat meat); its amount is अर्द्धतुला.",
            "अर्द्धतुला = half a tulā (a large unit of weight)."),
        mcq("transfer", 5, "Join invented पचेत् + अन्नम् as one sandhi string, like पचेदप्सु. Which is right?",
            ("पचेदन्नम्",
             "Final त् becomes द् before a vowel, as in पचेत् + अप्सु = पचेदप्सु."),
            [("पचेतन्नम्", "त् does not stay voiceless before a vowel."),
             ("पचेन्नन्नम्", "त् becomes न् only before a nasal, not before अ."),
             ("पचेच्छन्नम्", "त् → च्छ only before श्, not before a vowel.")],
            "Same rule as पचेत् + अप्सु → पचेदप्सु.",
            "-त् + vowel → -द् + vowel.",
            teaches="A final त् becomes द् before a vowel (पचेत् + अप्सु = पचेदप्सु; पचेत् + अन्नम् = पचेदन्नम्)."),
    ],
}

# ---------------------------------------------------------------- unit 3
AUTHORED["3"] = {
    "title": "पूते यवानीफलबिल्वकुष्ठ",
    "question": "What is added to the strained liquid in verse 3, and in what state is it given?",
    "rule": ("When strained, it is joined with pastes of yavānī-phala, bilva, kuṣṭha, vacā, śatāhvā, ghana and "
             "pippalī, with grape, honey and ghee, together with oil, pleasantly warm and with salt."),
    "limits": ("The subject is not named (the liquid of verse 2). यवानीफल may be one item or two, so no question rests on it. "
               "Śatāhvā is probably dill and ghana probably nut-grass; the oil's kind and all amounts are not stated."),
    "explain_hi": ("श्लोक २ का पका हुआ द्रव यहाँ छाना जाता है (‘पूते’ = छान लेने पर)। फिर उसमें इन द्रव्यों के कल्क यानी लुगदी मिलती है: "
                   "यवानीफल यानी अजवायन का फल, बिल्व यानी बेल, कुष्ठ यानी कूठ, वचा यानी बच, शताह्वा यानी सम्भवतः सोआ, घन यानी सम्भवतः नागरमोथा, "
                   "और पिप्पली यानी पीपर। साथ में मृद्वीका यानी मुनक्का या अंगूर, क्षौद्र यानी शहद, घी और तेल। "
                   "बस्ति सुखोष्ण यानी सुहाती गरम और नमक से युक्त होती है; मात्राएँ नहीं दी गई हैं।"),
    "hook": "छानो, कल्क डालो, मुनक्का-शहद-घी-तेल, सुहाता गरम, नमक के साथ।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In verse 3, at what point are the pastes added?",
            ("After the liquid is strained",
             "पूते: when (it) has been strained; then the pastes follow."),
            [("Before the drugs are cooked", "The cooking was in verse 2; पूते comes after it."),
             ("After the basti is given", "The pastes are part of the basti, not added afterwards."),
             ("While the water is boiling", "The verse speaks of straining, not of boiling.")],
            "पूते is a locative absolute: when strained.",
            "पूते = when strained (√पू, to purify, strain)."),
        order(1, "Put these paste drugs of verse 3 in the verse's order.",
              ["बिल्व", "कुष्ठ", "वचा", "घन", "पिप्पली"],
              "After यवानीफल the compound runs bilva, kuṣṭha, vacā, (śatāhvā, printed with a letter slip), ghana, pippalī.",
              "बिल्व · कुष्ठ · वचा · (शताह्वा) · घन · पिप्पली."),
        match(2, "Match each drug of verse 3 to its identity as the card gives it.",
              [["बिल्व", "bael"], ["कुष्ठ", "costus root"], ["वचा", "sweet flag"],
               ["पिप्पली", "long pepper"], ["मृद्वीका", "grape or raisin"]],
              "These five identifications are labelled standard in the data.",
              "बिल्व = bael; कुष्ठ = costus; वचा = sweet flag; पिप्पली = long pepper; मृद्वीका = grape/raisin.",
              role="extend",
              teaches="The paste drugs and additions of verse 3 have standard identifications: bael, costus, sweet flag, long pepper, grape."),
        mcq("discriminate", 3, "Which is the right split of सुखोष्णो in verse 3?",
            ("सुख + उष्णः",
             "अ + उ → ओ (सुखोष्ण); -अः before the voiced ल → -ओ."),
            [("सुखम् + उष्णः", "म् before a vowel stays: it would be सुखमुष्णः."),
             ("सुखः + उष्णः", "-अः before a vowel drops the visarga and does not join: सुख उष्णः."),
             ("सुखौ + उष्णः", "औ before a vowel becomes आव्: it would be सुखावुष्णः.")],
            "सुखोष्ण = pleasantly warm: सुख + उष्ण.",
            "अ + उ → ओ."),
        multi("apply", 4, "Besides the pastes, which of these does verse 3 add to the basti?",
              [("Honey (क्षौद्र)", "Right: मृद्वीका-क्षौद्र-घृतैः names honey."),
               ("Ghee (घृत)", "Right: घृत is in the same compound."),
               ("Salt (लवण)", "Right: लवणान्वितः, endowed with salt."),
               ("Milk (क्षीर)", "Milk is not named in this verse."),
               ("Urine (मूत्र)", "Urine is added in the recipe of verse 10, not here.")],
              [0, 1, 2],
              "Verse 3 adds grape, honey, ghee, oil and salt, and the basti is pleasantly warm.",
              "Additions: मृद्वीका, क्षौद्र, घृत, तैल, लवण."),
        mcq("transfer", 5, "Join invented घृत + अन्वितः, like लवणान्वितः. Which is right?",
            ("घृतान्वितः",
             "अ + अ → आ, as in लवण + अन्वितः = लवणान्वितः."),
            [("घृतोन्वितः", "ओ comes from अ + उ, not from अ + अ."),
             ("घृतेन्वितः", "ए comes from अ + इ, not from अ + अ."),
             ("घृतन्वितः", "The two vowels do not simply lose one; they merge into आ.")],
            "Same rule as लवण + अन्वितः → लवणान्वितः.",
            "अ + अ → आ.",
            teaches="Two short अ vowels merge into आ (लवण + अन्वितः = लवणान्वितः; घृत + अन्वितः = घृतान्वितः)."),
    ],
}

# ---------------------------------------------------------------- unit 4
AUTHORED["4"] = {
    "title": "बस्तिः परं सर्वगदप्रमाथी",
    "question": "What does verse 4 say this basti does, and where is it to be used?",
    "rule": ("This basti supremely destroys all diseases, is beneficial for the healthy, life-giving and nourishing. "
             "In whichever basti no paste has been introduced, one should give this very one there."),
    "limits": ("अमुम् (this) is taken as the paste of verse 3; the text does not say which paste. सर्वत्र is "
               "'everywhere' (also read 'in every case'); no question rests on that choice. जीवनबृंहण may be one or two qualities."),
    "explain_hi": ("यह श्लोक बलादि बस्ति का फल और उपयोग बताता है। यह बस्ति सब गदों यानी रोगों का उत्कृष्ट रूप से नाश करती है, "
                   "स्वस्थ के लिए भी हितकर है, और जीवन देने वाली तथा बृंहण यानी पुष्टि करने वाली है। "
                   "दूसरी पंक्ति एक नियम देती है: जिस बस्ति में कल्क नहीं बताया गया हो, उसमें इसी को दे। "
                   "‘इसी’ (अमुम्) को श्लोक ३ का कल्क माना गया है; पाठ स्वयं नहीं कहता कि कौन-सा।"),
    "hook": "सब रोग मिटाए, स्वस्थ को भी हित; जहाँ कल्क न कहा, वहाँ यही।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "According to verse 4, for whom is this basti also beneficial?",
            ("For a healthy person",
             "स्वस्थे हितः: beneficial in (for) a healthy person."),
            [("For a person with fever", "Fever is not named in this verse."),
             ("Only for the very old", "Age is not mentioned."),
             ("Only for small children", "Children are not mentioned.")],
            "Besides destroying all diseases, the basti is स्वस्थे हितः, good for the healthy too.",
            "स्वस्थे हितः = beneficial for a healthy person."),
        match(1, "Match each word of verse 4 to its meaning.",
              [["सर्वगदप्रमाथी", "destroyer of all diseases"], ["स्वस्थे", "in a healthy person"],
               ["कल्कः", "paste"], ["दद्यात्", "one should give"]],
              "These words carry the praise in line 1 and the rule in line 2.",
              "सर्वगदप्रमाथी = destroyer of all diseases; स्वस्थे = in the healthy; कल्कः = paste; दद्यात् = should give."),
        order(2, "Put these phrases of verse 4 in the verse's order.",
              ["बस्तिः परं सर्वगदप्रमाथी", "स्वस्थे हितो", "जीवनबृंहणश्च",
               "बस्तौ च यस्मिन् प्रणितो न कल्कः", "सर्वत्र दद्यादमुमेव तत्र"],
              "First the praise (destroyer, good for the healthy, life-giving and nourishing), then the rule for bastis without a paste.",
              "Praise in line 1; rule in line 2.",
              role="extend",
              teaches="Verse 4 moves from what the basti does (line 1) to where it is used (line 2)."),
        mcq("discriminate", 3, "Which is the right split of दद्यादमुमेव in verse 4?",
            ("दद्यात् + अमुम् + एव",
             "त् → द् before a vowel; म् + ए joins as मे."),
            [("दद्या + दमुम् + एव", "दमुम् is not a word; the pronoun is अमुम्."),
             ("दद्यात् + अमु + मेव", "मेव is not a word; एव (very) follows अमुम्."),
             ("दद्यात् + अमुम् + इव", "म् + इ would give मि, not मे; the word is एव.")],
            "दद्यात् (one should give) + अमुम् (this) + एव (very).",
            "-त् + vowel → -द्; -म् + vowel joins the vowel."),
        mcq("apply", 4, "A basti recipe states no paste. What does verse 4 say to do there?",
            ("Give this very one there",
             "बस्तौ यस्मिन् न कल्कः … दद्यादमुमेव तत्र: in that basti give this very one."),
            [("Give no basti at all", "The verse does not forbid the basti; it supplies what is missing."),
             ("Give plain milk instead", "Milk is not mentioned in the verse."),
             ("Give the basti cold", "Temperature is not the subject of line 2.")],
            "The rule fills a gap: where no paste is stated, this one (taken as the paste of verse 3) is given.",
            "न कल्कः → दद्यादमुमेव तत्र."),
        mcq("transfer", 5, "Join invented हितः + भवति, like स्वस्थे हितो जीवन…. Which is right?",
            ("हितो भवति",
             "-अः before a voiced consonant (भ) becomes -ओ."),
            [("हितर् भवति", "-र् comes from -इः or -उः, not from -अः."),
             ("हिता भवति", "-अः never becomes -आ; before the voiced भ it becomes -ओ."),
             ("हितस् भवति", "स् appears before त्, not before a voiced भ.")],
            "Same rule as हितः + जीवन… → हितो जीवन….",
            "-अः + voiced consonant → -ओ.",
            teaches="A final -अः becomes -ओ before a voiced consonant (हितः + जीवन = हितो जीवन; हितः + भवति = हितो भवति)."),
    ],
}

# ---------------------------------------------------------------- unit 5
AUTHORED["5"] = {
    "title": "द्विपंचमूलस्य रसोऽम्लयुक्तः",
    "question": "Which nirūha does verse 5 call the foremost, and against which diseases?",
    "rule": ("The rasa of the ten-root group and of good goat meat, joined with something sour and with the three fats, "
             "is declared the foremost nirūha, remover of all diseases of anila (Vāta)."),
    "limits": ("सपैर्बपेष्यः is damaged; only '-peṣyaḥ' (to be ground) is recognisable, so nothing is built on it. "
               "The sour substance and the three fats are not named; no measures are given. Confidence low."),
    "explain_hi": ("यह नया नुस्खा है: दशमूल का रस और अच्छे बकरे के मांस का रस, खट्टे पदार्थ से युक्त। "
                   "उसमें त्रिस्नेह यानी तीन स्नेह मिलते हैं; उनके नाम यहाँ नहीं दिए गए। "
                   "इसे श्रेष्ठ निरूह यानी काढ़े की बस्ति कहा गया है, जो अनिल यानी वात की सब व्याधियाँ हरता है। "
                   "एक शब्द (सपैर्बपेष्यः) छपाई में बिगड़ा है; उसका केवल ‘पेष्य’ (पीसने योग्य) भाग पहचाना जाता है।"),
    "hook": "दशमूल + बकरे का रस, खट्टा, तीन स्नेह: वात-रोगों का श्रेष्ठ निरूह।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What does verse 5 say this निरूह removes?",
            ("All diseases of Vāta (anila)",
             "सर्वानिलव्याधिहरः: remover of all anila (wind, Vāta) diseases."),
            [("All diseases of Kapha", "Kapha is not named in this verse."),
             ("All diseases of Pitta", "Pitta is not named in this verse."),
             ("Only fever and thirst", "No fever or thirst is mentioned.")],
            "अनिल = wind = Vāta; the nirūha removes all its diseases.",
            "सर्व-अनिल-व्याधि-हर = remover of all Vāta diseases."),
        match(1, "Match each word of verse 5 to its meaning.",
              [["रसः", "liquid, broth"], ["अम्ल", "sour"], ["त्रिस्नेह", "three fats"],
               ["निरूहः", "decoction enema"], ["अनिल", "wind, Vāta"]],
              "These are the key words of the recipe and its claim.",
              "रस = liquid; अम्ल = sour; त्रिस्नेह = three fats; निरूह = decoction enema; अनिल = Vāta."),
        order(2, "Put these words of verse 5 in the verse's order (the damaged word is left out).",
              ["द्विपंचमूलस्य", "रसोऽम्लयुक्तः", "सच्छागमांसस्य", "त्रिस्नेहयुक्तः", "प्रवरो निरूहः", "सर्वानिलव्याधिहरः"],
              "Ten roots, the sour-joined rasa, goat meat; then the three fats, the foremost nirūha, and its claim.",
              "द्विपंचमूलस्य · रसोऽम्लयुक्तः · सच्छागमांसस्य · त्रिस्नेहयुक्तः · प्रवरो निरूहः · सर्वानिलव्याधिहरः.",
              role="extend",
              teaches="Line 1 gives the ingredients of the rasa; line 2 adds the three fats and names the result."),
        mcq("discriminate", 3, "Which is the right split of रसोऽम्लयुक्तः in verse 5?",
            ("रसः + अम्लयुक्तः",
             "-अः + अ- → -ओ, and the अ- is dropped (shown by ऽ)."),
            [("रसो + म्लयुक्तः", "म्लयुक्त is not a word; the word is अम्लयुक्त."),
             ("रसम् + अम्लयुक्तः", "म् before a vowel stays: it would be रसमम्ल…."),
             ("रसा + अम्लयुक्तः", "आ + अ → आ, giving रसाम्ल…, not रसोऽम्ल….")],
            "रसः (liquid) + अम्लयुक्तः (joined with sour).",
            "-अः + अ → -ओऽ."),
        mcq("apply", 4, "A student says verse 5 names the three fats as ghee, oil and marrow. What does the card say?",
            ("The verse does not name them",
             "त्रिस्नेह is named as a group only; its members are not given here."),
            [("The verse names them in line 2", "Line 2 has only त्रिस्नेहयुक्तः, with no names."),
             ("The verse names only ghee", "Ghee is not named in this verse."),
             ("The verse names oil and honey", "Neither oil nor honey is named here.")],
            "The three fats are conventionally ghee, oil and vasā or majjā, but this verse does not list them.",
            "Only what the verse names belongs to its list."),
        mcq("transfer", 5, "A basti (masc.) joined with honey: which invented phrase agrees (words shown unjoined), like त्रिस्नेहयुक्तः निरूहः?",
            ("मधुयुक्तः बस्तिः",
             "बस्ति is masculine here, so the -युक्त compound takes -अः, like निरूहः."),
            [("मधुयुक्ता बस्तिः", "-आ is the feminine ending."),
             ("मधुयुक्तम् बस्तिः", "-अम् is neuter (or accusative), not masculine nominative."),
             ("मधुयुक्ताः बस्तिः", "-आः is plural; बस्तिः is singular.")],
            "An adjective compound ending in -युक्त agrees with its noun: त्रिस्नेहयुक्तः निरूहः (m. nom. sg.).",
            "Adjective agrees with the noun in gender, number, case.",
            teaches="An adjective compound like त्रिस्नेहयुक्त agrees with its noun: masculine singular nominative -अः (निरूहः, बस्तिः)."),
    ],
}

# ---------------------------------------------------------------- unit 6
AUTHORED["6"] = {
    "title": "बलापटोलीलघुपंचमूल",
    "question": "From which drugs is the liquid of verse 6 cooked, and how is it prepared again?",
    "rule": ("From a well-cooked mass of balā, paṭolī, the small five roots, trāyantikā, eraṇḍa and yava, a prastha of the "
             "liquid, joined with goat broth, is to be cooked again until it equals a prastha."),
    "limits": ("What the drugs are cooked in is not named. The stray 'ई' in रसाच्छागरसाईयुक्तः is unclear; no question rests on it. "
               "Trāyantikā is disputed; the small five roots are not listed. The recipe continues in verse 7."),
    "explain_hi": ("यहाँ एक नया नुस्खा शुरू होता है जो श्लोक ७ में पूरा होता है। बला यानी बरियार, पटोली यानी परवल, लघुपंचमूल, त्रायन्तिका "
                   "(पहचान विवादित), एरण्ड यानी अरंडी और यव, इन्हें भली-भाँति पकाया जाता है। उस रस में से एक प्रस्थ लेकर, "
                   "बकरे के रस के साथ, फिर पकाया जाता है जब तक वह एक प्रस्थ के बराबर न रह जाए। "
                   "छपे शब्द में एक फालतू ‘ई’ है, जिसका अर्थ स्पष्ट नहीं।"),
    "hook": "बला से यव तक छह द्रव्य पकाओ; प्रस्थ भर रस, बकरे के रस के साथ, फिर प्रस्थ भर तक।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "Which measure does verse 6 use for the liquid?",
            ("A prastha",
             "प्रस्थो रसात्: a prastha from the liquid; and again until प्रस्थसमः."),
            [("An akṣa", "The akṣa is named in verse 10, not here."),
             ("Half a tulā", "Half a tulā is the meat in verse 2."),
             ("Two āḍhakas", "Two āḍhakas of water come in verse 9.")],
            "The measure in this verse is the prastha, used twice.",
            "प्रस्थ = a unit of measure; the verse uses it twice."),
        order(1, "Put these drugs of verse 6 in the verse's order.",
              ["बला", "पटोली", "लघुपंचमूल", "त्रायन्तिका", "एरण्ड", "यव"],
              "One long compound runs balā, paṭolī, the small five roots, trāyantikā, eraṇḍa, yava.",
              "बला · पटोली · लघुपंचमूल · त्रायन्तिका · एरण्ड · यव."),
        match(2, "Match each drug of verse 6 to its identity as the card gives it.",
              [["बला", "country mallow"], ["पटोली", "pointed gourd"],
               ["एरण्ड", "castor"], ["यव", "barley"]],
              "These four are standard identifications in the data; trāyantikā is disputed and left out.",
              "बला = country mallow; पटोली = pointed gourd; एरण्ड = castor; यव = barley.",
              role="extend",
              teaches="Of the six drugs of verse 6, balā, paṭolī, eraṇḍa and yava have standard identifications."),
        mcq("discriminate", 3, "What does सुसिद्धात् at the end of the compound mean?",
            ("From what is well cooked",
             "सु (well) + सिद्ध (cooked), ablative -आत्: from what is well cooked."),
            [("From what is half cooked", "सु means well, not half."),
             ("From what is still raw", "सिद्ध means cooked, the opposite of raw."),
             ("From what is ground dry", "Grinding is not named; सिद्ध is cooked.")],
            "The whole drug compound ends in this ablative: from (the) well-cooked (mass).",
            "सुसिद्धात् = from the well-cooked (सिद्ध = पकाया हुआ)."),
        mcq("apply", 4, "How long is the prastha of liquid with goat broth cooked again in verse 6?",
            ("Until it equals a prastha",
             "साध्यः पुनः प्रस्थसमः स यावत्: prepared again until it equals a prastha."),
            [("Until an eighth remains", "An eighth is the end point in verse 9."),
             ("Until a quarter remains", "A quarter is the end point in verse 2."),
             ("Until it is thick as paste", "Thickness is not mentioned.")],
            "The end point is प्रस्थसम, equal to a prastha.",
            "यावत् प्रस्थसमः = until it equals a prastha."),
        mcq("transfer", 5, "Like यवात् (from barley), which invented form means from milk?",
            ("क्षीरात्",
             "-आत् is the ablative singular, 'from', as in यवात्, रसात्, सुसिद्धात्."),
            [("क्षीरेण", "-एन is instrumental, 'with milk'."),
             ("क्षीरस्य", "-अस्य is genitive, 'of milk'."),
             ("क्षीरे", "-ए is locative, 'in milk'.")],
            "The ablative of an अ-stem ends in -आत्.",
            "-आत् = from (ablative singular).",
            teaches="The ablative singular of an अ-stem ends in -आत्, 'from' (यवात्, रसात्; क्षीरात् from milk)."),
    ],
}

# ---------------------------------------------------------------- unit 7
AUTHORED["7"] = {
    "title": "प्रियंगुकृष्णाघनकल्कयुक्तः",
    "question": "What is added to the prepared liquid in verse 7, and what effects does the verse give it?",
    "rule": ("Joined with a paste of priyaṅgu, kṛṣṇā and ghana, with oil, ghee, honey and rock salt, it would kindle digestion, "
             "give flesh and strength, and at once bestow strength of the eyes."),
    "limits": ("The subject is the prastha prepared in verse 6. Priyaṅgu is disputed; ghana is probably nut-grass. "
               "चक्षुर्बलम् may also be read 'eyes and strength', so no question turns on that split. No amounts."),
    "explain_hi": ("श्लोक ६ में तैयार किए गए प्रस्थ भर रस में यहाँ कल्क मिलता है: प्रियंगु (पहचान विवादित), कृष्णा यानी पीपर और घन यानी सम्भवतः नागरमोथा। "
                   "साथ में तेल, घी, शहद और सैन्धव यानी सेंधा नमक। ऐसी बस्ति दीपन यानी पाचन-अग्नि जगाने वाली, मांस और बल देने वाली होती है, "
                   "और तुरन्त आँखों का बल देती है। ‘चक्षुर्बलम्’ को ‘आँख और बल’ भी पढ़ा जा सकता है।"),
    "hook": "प्रियंगु-पीपर-मोथा का कल्क, तेल-घी-शहद-सेंधा: दीपन, मांस-बल, तुरन्त आँखों का बल।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "Which word of verse 7 means at once?",
            ("सद्यः",
             "सद्यः = at once; it closes the verse."),
            [("पुनः", "पुनः means again (verse 6)."),
             ("तत्र", "तत्र means there (verse 4)."),
             ("सर्वत्र", "सर्वत्र means everywhere (verse 4).")],
            "चक्षुर्बलं चोपदधाति सद्यः: it at once bestows strength of the eyes.",
            "सद्यः = at once."),
        match(1, "Match each word of verse 7 to its meaning.",
              [["कृष्णा", "long pepper"], ["सर्पिः", "ghee"], ["मधु", "honey"],
               ["सैंधव", "rock salt"], ["दीपन", "kindler of digestion"]],
              "Kṛṣṇā is another name of pippalī; saindhava is rock salt.",
              "कृष्णा = long pepper; सर्पिः = ghee; मधु = honey; सैंधव = rock salt; दीपन = kindler."),
        order(2, "Put these additions of verse 7 in the verse's order.",
              ["प्रियंगुकृष्णाघनकल्क", "तैल", "सर्पिः", "मधु", "सैंधव"],
              "First the paste, then oil, ghee, honey and rock salt under one स-.",
              "कल्क · तैल · सर्पिः · मधु · सैंधव.",
              role="extend",
              teaches="Verse 7 adds the paste first, then four additions in the order oil, ghee, honey, rock salt."),
        mcq("discriminate", 3, "Which is the right split of स्याद्दीपनो in verse 7?",
            ("स्यात् + दीपनः",
             "त् → द् before the voiced द; -अः → -ओ before the voiced म."),
            [("स्या + द्दीपनः", "द्दीपन is not a word; the word is दीपन."),
             ("स्यात् + द्दीपनः", "द्दीपन is not a word; the first द् is स्यात्'s त् voiced, and the noun is दीपनः."),
             ("स्याः + दीपनः", "स्याः is not the verb; the verb is स्यात्, it would be.")],
            "स्यात् (it would be) + दीपनः (a kindler).",
            "-त् + voiced consonant → -द्."),
        multi("apply", 4, "Which effects does verse 7 name for this basti?",
              [("It kindles digestion (दीपन)", "Right: स्याद्दीपनः."),
               ("It gives flesh (मांस)", "Right: मांसबलप्रदः, giver of flesh and strength."),
               ("It gives strength (बल)", "Right: the same compound names strength."),
               ("It cures fever", "Fever is not named in this verse."),
               ("It removes Kapha", "Kapha is not named in this verse.")],
              [0, 1, 2],
              "The verse names kindling, flesh and strength, and strength of the eyes at once.",
              "दीपन · मांसबलप्रद · चक्षुर्बल (सद्यः)."),
        mcq("transfer", 5, "Join invented च + उष्णम्, like चोपदधाति. Which is right?",
            ("चोष्णम्",
             "अ + उ → ओ, as in च + उपदधाति = चोपदधाति."),
            [("चौष्णम्", "औ comes from अ + ओ or औ, not from अ + उ."),
             ("चुष्णम्", "The अ does not simply drop; it merges with उ into ओ."),
             ("च्वुष्णम्", "व् comes from उ before a vowel, not from अ.")],
            "Same rule as च + उपदधाति → चोपदधाति.",
            "अ + उ → ओ.",
            teaches="अ + उ gives ओ (च + उपदधाति = चोपदधाति; च + उष्णम् = चोष्णम्)."),
    ],
}

# ---------------------------------------------------------------- unit 8
AUTHORED["8"] = {
    "title": "एरंडमूलात्त्रिपलम्",
    "question": "Which drugs, and which measures, open the eraṇḍa-root recipe in verse 8?",
    "rule": ("Three palas of eraṇḍa root; likewise from palāśa a pala-portion; the small five roots; and rāsnā, balā, "
             "chinnaruhā, aśvagandhā, punarnavā, āragvadha and devadāru. The cooking follows in verse 9."),
    "limits": ("The verse has no verb. Line 2 gives no quantities. Palāśa is probably flame-of-the-forest (the word also means 'leaf'); "
               "the part used is not stated. The print reads आर्गवध for āragvadha."),
    "explain_hi": ("यहाँ से एरण्डमूल वाली बस्ति का नुस्खा शुरू होता है, जो श्लोक ११ तक चलता है। एरण्ड यानी अरंडी की जड़ तीन पल, और पलाश यानी सम्भवतः ढाक से "
                   "पल भर का अंश; फिर लघुपंचमूल। दूसरी पंक्ति एक लम्बी सूची है: रास्ना, बला यानी बरियार, छिन्नरुहा यानी गिलोय, "
                   "अश्वगन्धा यानी असगंध, पुनर्नवा यानी गदहपूर्णा, आरग्वध यानी अमलतास और देवदारु यानी देवदार। "
                   "इस श्लोक में क्रिया नहीं है; पकाने की बात श्लोक ९ में है।"),
    "hook": "अरंडी-जड़ तीन पल, सम्भवतः ढाक पल-अंश, लघुपंचमूल, फिर रास्ना से देवदारु तक सात।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "How much eraṇḍa root does verse 8 give?",
            ("Three palas",
             "एरंडमूलात् त्रिपलम्: three palas from the eraṇḍa root."),
            [("Half a tulā", "Half a tulā is the meat of verse 2."),
             ("One prastha", "The prastha is the measure of verse 6."),
             ("One akṣa", "The akṣa is the measure in verse 10.")],
            "त्रिपलम् = three palas.",
            "त्रि + पल = three palas."),
        match(1, "Match each drug of verse 8 to its identity as the card gives it.",
              [["एरण्ड", "castor"], ["छिन्नरुहा", "giloy"], ["अश्वगन्धा", "winter cherry"],
               ["पुनर्नवा", "hogweed"], ["देवदारु", "deodar"]],
              "All five are labelled standard in the data; chinnaruhā is a name of guḍūcī.",
              "एरण्ड = castor; छिन्नरुहा = giloy; अश्वगन्धा = winter cherry; पुनर्नवा = hogweed; देवदारु = deodar."),
        order(2, "Put these drugs of verse 8, line 2, in the verse's order.",
              ["रास्ना", "बला", "छिन्नरुहा", "अश्वगन्धा", "पुनर्नवा"],
              "The list runs rāsnā, balā, chinnaruhā, aśvagandhā, punarnavā, then āragvadha and devadāru.",
              "रास्ना · बला · छिन्नरुहा · अश्वगन्धा · पुनर्नवा (· आरग्वध · देवदारु).",
              role="extend",
              teaches="Line 2 is one compound of seven drug names, from rāsnā to devadāru, with no quantities."),
        mcq("discriminate", 3, "Which is the right split of बलाच्छिन्नरुहा in verse 8?",
            ("बला + छिन्नरुहा",
             "छ after a vowel becomes च्छ (always after a short vowel, optionally after a long one like आ): बला + छिन्न… = बलाच्छिन्न…."),
            [("बलात् + शिन्नरुहा", "शिन्नरुहा is not a word; the drug is छिन्नरुहा, giloy."),
             ("बलाच् + छिन्नरुहा", "बलाच् is not a word; the drug is बला."),
             ("बलाः + छिन्नरुहा", "-आः before छ would become -आश्छ, not -आच्छ.")],
            "Two drug names of the list: बला (country mallow) and छिन्नरुहा (giloy).",
            "Vowel + छ → vowel + च्छ (optional after a long vowel)."),
        mcq("apply", 4, "Verse 8 has no verb. Where are its drugs cooked?",
            ("In verse 9, by विपाचयेत्",
             "The notes: the drugs are cooked in the next line, विपाचयेत्, one should cook thoroughly."),
            [("In verse 8, by पचेत्", "पचेत् is the verb of verse 2; verse 8 has no verb."),
             ("In verse 2, with goat meat", "Verse 2 is a different recipe."),
             ("Nowhere; they are ground raw", "The paste of verse 10 is ground; these drugs are cooked.")],
            "Verse 8 lists; verse 9 cooks (विपाचयेत्) with eight fruits in two āḍhakas of water.",
            "List in verse 8 → cooking in verse 9."),
        mcq("transfer", 5, "Like त्रिपलम् (three palas), which invented form means two palas?",
            ("द्विपलम्",
             "Number + measure make a dvigu compound, neuter singular -म्, like त्रिपलम्."),
            [("द्वौपलम्", "The number goes in as its stem द्वि, not as द्वौ."),
             ("द्विपलाः", "-आः is masculine plural; the dvigu is neuter singular."),
             ("पलद्वि", "In a dvigu the number comes first.")],
            "त्रि + पल → त्रिपलम्; द्वि + पल → द्विपलम्.",
            "Dvigu: number stem + noun, neuter -म्.",
            teaches="A number stem plus a measure makes a dvigu compound in neuter -म् (त्रिपलम्, द्विपलम्; also द्विपंचमूलम्)."),
    ],
}

# ---------------------------------------------------------------- unit 9
AUTHORED["9"] = {
    "title": "फलानि चाष्टौ सलिलाढकाभ्याम्",
    "question": "How is the eraṇḍa-root mixture cooked in verse 9, and which drugs follow for the paste?",
    "rule": ("With eight fruits, one should cook it thoroughly in two āḍhakas of water until an eighth remains. "
             "Then the paste drugs: vacā, śatāhvā, (unclear), priyaṅgu, yaṣṭī, kaṇā, vatsaka seeds and musta."),
    "limits": ("The eight fruits are not named. पुष्पामि is unreadable, so nothing is built on it. An eighth 'of this' is "
               "naturally the water, but the text does not say. The paste is given in verse 10. Confidence low."),
    "explain_hi": ("श्लोक ८ के द्रव्यों में आठ फल (नाम नहीं दिए) मिलाकर, दो आढक जल में भली-भाँति पकाया जाता है, जब तक आठवाँ भाग शेष रहे। "
                   "दूसरी पंक्ति कल्क के द्रव्यों की सूची है: वचा यानी बच, शताह्वा यानी सम्भवतः सोआ, एक अस्पष्ट शब्द (पुष्पामि), प्रियंगु "
                   "(पहचान विवादित), यष्टी यानी मुलेठी, कणा यानी पीपर, वत्सक यानी कुटज के बीज, और मुस्त यानी नागरमोथा। "
                   "श्लोक २ में चौथाई शेष था, यहाँ आठवाँ भाग।"),
    "hook": "आठ फल, दो आढक जल, आठवाँ भाग बचे; फिर बच से मोथा तक कल्क।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "How much water does verse 9 give for the cooking?",
            ("Two āḍhakas",
             "सलिलाढकाभ्याम्: with two āḍhakas of water (dual)."),
            [("One prastha", "The prastha is the measure of verse 6."),
             ("Four palas", "Palas are not given for the water here."),
             ("Half a tulā", "Half a tulā is the meat of verse 2.")],
            "सलिल = water; आढकाभ्याम् = with two āḍhakas.",
            "सलिल-आढकाभ्याम् = with two āḍhakas of water."),
        match(1, "Match each paste drug of verse 9 to its identity as the card gives it.",
              [["वचा", "sweet flag"], ["यष्टी", "liquorice"], ["कणा", "long pepper"],
               ["वत्सकबीज", "seeds of kuṭaja"], ["मुस्त", "nut-grass"]],
              "These five are labelled standard in the data; vatsaka is a name of kuṭaja.",
              "वचा = sweet flag; यष्टी = liquorice; कणा = long pepper; वत्सकबीज = kuṭaja seeds; मुस्त = nut-grass."),
        order(2, "Put these paste drugs of verse 9 in the verse's order.",
              ["प्रियंगु", "यष्टी", "कणा", "वत्सकबीज", "मुस्त"],
              "After the unclear word the list runs priyaṅgu, yaṣṭī, kaṇā, vatsaka seeds, musta.",
              "प्रियंगु · यष्टी · कणा · वत्सकबीज · मुस्त.",
              role="extend",
              teaches="The paste list of verse 9 ends priyaṅgu, yaṣṭī, kaṇā, vatsaka seeds, musta; its use is in verse 10."),
        mcq("discriminate", 3, "Which is the right split of अष्टमशेषितेऽस्मिन् in verse 9?",
            ("अष्टमशेषिते + अस्मिन्",
             "-ए + अ- → -ए, and the अ- is dropped (shown by ऽ)."),
            [("अष्टमशेषितः + अस्मिन्", "-अः + अ- would give -ओऽ (शेषितोऽस्मिन्), not -एऽ."),
             ("अष्टमशेषिते + स्मिन्", "स्मिन् is not a word; the pronoun is अस्मिन्."),
             ("अष्टमशेषितै + अस्मिन्", "ऐ before a vowel becomes आय्, not एऽ.")],
            "अष्टमशेषिते (being left at an eighth) + अस्मिन् (this): a locative absolute.",
            "-ए + अ → -एऽ."),
        mcq("apply", 4, "Someone following verse 9 stops cooking when a quarter is left. What does the verse say?",
            ("Cook on until an eighth remains",
             "अष्टमशेषिते: the end point is an eighth, not a quarter."),
            [("Right, a quarter is the end point", "A quarter is the end point of verse 2, not of verse 9."),
             ("Stop at half instead", "Half is not named as an end point."),
             ("Cook until no water is left", "The verse keeps an eighth.")],
            "Verse 2 ends at a quarter (चतुर्थशेष); verse 9 at an eighth (अष्टमशेष).",
            "Verse 9: cook down to an eighth."),
        mcq("transfer", 5, "Like सलिलाढकाभ्याम् (with two āḍhakas), which invented form means with two hands?",
            ("हस्ताभ्याम्",
             "-आभ्याम् is the instrumental dual of an अ-stem: with two."),
            [("हस्तेन", "-एन is instrumental singular: with one hand."),
             ("हस्तैः", "-ऐः is instrumental plural: with many hands."),
             ("हस्तयोः", "-अयोः is genitive or locative dual, not 'with'.")],
            "आढक → आढकाभ्याम्, हस्त → हस्ताभ्याम्.",
            "-आभ्याम् = with two (instrumental dual).",
            teaches="The instrumental dual of an अ-stem ends in -आभ्याम्, 'with two' (आढकाभ्याम्, हस्ताभ्याम्)."),
    ],
}

# ---------------------------------------------------------------- unit 10
AUTHORED["10"] = {
    "title": "दद्यात्सुपिष्टं सहतार्क्ष्यशैलम्",
    "question": "How is the paste given in verse 10, and what kind of basti results?",
    "rule": ("The paste, well ground, is given with tārkṣyaśaila, of an akṣa's measure, with a portion of salt. That basti, "
             "with mākṣika, oil and urine, scraping and kindling, would overcome (the troubles of verse 11)."),
    "limits": ("The object of दद्यात् is the paste list of verse 9, understood. Tārkṣyaśaila is disputed (possibly rasāñjana). "
               "Whether the akṣa is for tārkṣyaśaila alone or the whole is not stated; no question on it. "
               "Mākṣika is probably honey; the kind of urine is not stated."),
    "explain_hi": ("श्लोक ९ के कल्क-द्रव्य भली-भाँति पीसकर दिए जाते हैं, तार्क्ष्यशैल (पहचान विवादित, सम्भवतः रसौत) के साथ, अक्ष के माप का, "
                   "और नमक के अंश से युक्त। अक्ष का माप केवल तार्क्ष्यशैल का है या सबका, यह पाठ नहीं कहता। "
                   "वह बस्ति माक्षिक यानी सम्भवतः शहद, तेल और मूत्र के साथ होती है; उसे लेखन यानी खुरचने वाली और दीपन कहा गया है। "
                   "‘जयेत्’ (जीत लेगी) का कर्म श्लोक ११ में है।"),
    "hook": "पीसा कल्क, तार्क्ष्यशैल, अक्ष-माप, नमक; शहद-तेल-मूत्र: लेखन-दीपन बस्ति।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "Which two actions does verse 10 give this basti?",
            ("Scraping and kindling",
             "लेखनदीपनः: lekhana (scraping) and dīpana (kindling)."),
            [("Binding and cooling", "Neither is named; the word is लेखन-दीपन."),
             ("Nourishing and calming", "Nourishing (बृंहण) is said of the basti of verse 4, not here."),
             ("Purging and sweating", "Neither is named in this verse.")],
            "बस्तिर्जयेल्लेखनदीपनोऽसौ: that scraping and kindling basti would overcome ….",
            "लेखन = scraping; दीपन = kindling."),
        match(1, "Match each word of verse 10 to its meaning.",
              [["सुपिष्टम्", "well ground"], ["लवण", "salt"], ["मूत्र", "urine"],
               ["लेखन", "scraping"], ["जयेत्", "would overcome"]],
              "These words give the preparation, an addition and what the basti does.",
              "सुपिष्टम् = well ground; लवण = salt; मूत्र = urine; लेखन = scraping; जयेत् = would overcome."),
        order(2, "Put these words of verse 10, line 2, in the verse's order.",
              ["समाक्षिकः", "तैलयुतः", "समूत्रः", "बस्तिः", "जयेत्"],
              "With mākṣika, with oil, with urine; then the basti and its verb.",
              "समाक्षिकः · तैलयुतः · समूत्रः · बस्तिः · जयेत्.",
              role="extend",
              teaches="Line 2 lists three additions (mākṣika, oil, urine) before naming the basti and its verb जयेत्."),
        mcq("discriminate", 3, "Which is the right split of बस्तिर्जयेल्लेखन… in verse 10?",
            ("बस्तिः + जयेत् + लेखन…",
             "-इः before a voiced sound → -इर्; त् + ल → ल्ल."),
            [("बस्तिः + जयेल् + लेखन…", "जयेल् is not a word; the verb is जयेत्."),
             ("बस्तिम् + जयेत् + लेखन…", "म् before ज would be ं, not र्."),
             ("बस्तिः + जयेत् + ल्लेखन…", "ल्लेखन is not a word; the word is लेखन.")],
            "बस्तिः (the basti) + जयेत् (would overcome) + लेखनदीपनः (scraping and kindling).",
            "-इः + voiced → -इर्; -त् + ल → -ल्ल."),
        mcq("apply", 4, "Mākṣika stands beside oil and urine in verse 10. What does the card say it is?",
            ("Probably honey",
             "The data: mākṣika is probably honey; the word can also name a mineral."),
            [("Certainly a mineral", "A mineral is only the other sense; the data says probably honey."),
             ("Rock salt", "Salt is a separate item (लवणांश)."),
             ("Ghee", "Ghee is not named in this verse.")],
            "Mākṣika is hedged: probably honey; the text does not say.",
            "माक्षिक = probably honey (probable)."),
        mcq("transfer", 5, "Join invented तत् + लभते, like जयेत् + लेखन. Which is right?",
            ("तल्लभते",
             "त् before ल becomes ल्: जयेत् + लेखन = जयेल्लेखन."),
            [("तद्लभते", "Before ल the त् assimilates fully to ल्; it does not stop at द्."),
             ("तत्लभते", "In sandhi the त् does not stay before ल."),
             ("तंलभते", "Anusvara comes from म्, not from त्.")],
            "Same rule as जयेत् + लेखन → जयेल्लेखन.",
            "-त् + ल → -ल्ल.",
            teaches="A final त् before ल becomes ल् (जयेत् + लेखन = जयेल्लेखन; तत् + लभते = तल्लभते)."),
    ],
}

# ---------------------------------------------------------------- unit 11
AUTHORED["11"] = {
    "title": "जंघोरुपादत्रिकपृष्ठकोष्ठ",
    "question": "Which pains and diseases does verse 11 say the basti of verse 10 overcomes?",
    "rule": ("Pain of shanks, thighs, feet, trika, back, belly, heart and private part; heaviness; obstruction; "
             "diseases arising from gulma, aśma, (unclear), grahaṇī and guda; and diseases born of Kapha and Vāta."),
    "limits": ("The verb जयेत् is in verse 10. 'बध्म' is unclear (possibly vardhma). Whether -उत्थ governs every member, and whether "
               "शूल governs every body part, is not certain; no question turns on those. Confidence low."),
    "explain_hi": ("यह श्लोक श्लोक १० की बस्ति का फल पूरा करता है: वह किन-किन को जीतती है। पहले पीड़ा के स्थान: जंघा यानी घुटने से टखने तक की टाँग, "
                   "ऊरु यानी जाँघ, पैर, त्रिक यानी कमर का निचला भाग, पीठ, कोष्ठ यानी पेट, हृदय और गुह्य अंग। फिर गुरुता यानी भारीपन और विबन्ध यानी मल का रुकना। "
                   "दूसरी पंक्ति में गुल्म, अश्म यानी पथरी, एक अस्पष्ट शब्द, ग्रहणी और गुद से उत्पन्न रोग, तथा कफ और वात से जन्मे रोग हैं।"),
    "hook": "टाँग से गुह्य तक पीड़ा, भारीपन, विबन्ध, गुल्म से गुद तक, कफ-वात के रोग।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "Which doṣas does verse 11 name for the diseases the basti overcomes?",
            ("Kapha and Vāta",
             "कफवातजातान्: born of Kapha and Vāta."),
            [("Pitta and Kapha", "Pitta is not named in this verse."),
             ("Vāta and Pitta", "Pitta is not named in this verse."),
             ("Pitta alone", "Only Kapha and Vāta are named.")],
            "रोगान् कफवातजातान्: the diseases born of Kapha and Vāta.",
            "कफ-वात-जात = born of Kapha and Vāta."),
        order(1, "Put these body parts of verse 11 in the verse's order.",
              ["जंघा", "ऊरु", "पाद", "त्रिक", "पृष्ठ", "कोष्ठ"],
              "The compound runs shank, thigh, foot, trika, back, belly, then heart and private part.",
              "जंघा · ऊरु · पाद · त्रिक · पृष्ठ · कोष्ठ."),
        match(2, "Match each word of verse 11 to its meaning.",
              [["जंघा", "shank"], ["त्रिक", "lumbosacral region"], ["कोष्ठ", "belly"],
               ["गुह्य", "private part"], ["विबन्ध", "obstruction (constipation)"]],
              "These terms come from the gloss of verse 11.",
              "जंघा = shank; त्रिक = lumbosacral region; कोष्ठ = belly; गुह्य = private part; विबन्ध = obstruction.",
              role="extend",
              teaches="Verse 11 names body sites (shank, trika, belly, private part) and obstruction (vibandha)."),
        mcq("discriminate", 3, "Which is the right split of जंघोरु… at the start of verse 11?",
            ("जंघा + ऊरु…",
             "आ + ऊ → ओ: जंघा (shank) + ऊरु (thigh) = जंघोरु."),
            [("जंघो + रु…", "Neither जंघो nor रु is a word here."),
             ("जंघः + ऊरु…", "-अः before a vowel drops its visarga and does not merge to ओ."),
             ("जंघम् + ऊरु…", "म् before a vowel stays: it would be जंघमूरु….")],
            "Two body parts of the list: जंघा and ऊरु.",
            "आ + ऊ → ओ."),
        multi("apply", 4, "Besides pain, which of these does verse 11 name among what the basti overcomes?",
              [("Heaviness (गुरुता)", "Right: गुरुताम्, heaviness."),
               ("Obstruction (विबन्ध)", "Right: विबन्धम्, obstruction, usually of stool."),
               ("Fever (ज्वर)", "Fever is not named in this verse."),
               ("Cough (कास)", "Cough is not named in this verse.")],
              [0, 1],
              "Line 1 adds heaviness and obstruction to the pains.",
              "शूलम् · गुरुताम् · विबन्धम्."),
        mcq("transfer", 5, "Join invented देवान् + तत्र, like तांस्तांश्च. Which is right?",
            ("देवांस्तत्र",
             "Final न् before त् becomes anusvara + स्, as in तान् + तान् = तांस्तान्."),
            [("देवास्तत्र", "The nasal is not lost; it stays as anusvara."),
             ("देवाँत्तत्र", "No doubled त् arises; स् is inserted."),
             ("देवाञ्तत्र", "ञ् comes before च/ज, not before त्.")],
            "Same rule as तान् + तान् → तांस्तान्.",
            "-न् + त → -ंस्त.",
            teaches="A final न् before त् becomes ं + स् (तान् + तान् = तांस्तान्; देवान् + तत्र = देवांस्तत्र)."),
    ],
}


NOTES_HI = {
    "1": ("विश्वास: उच्च। अध्याय का आरम्भ-सूत्र; अध्याय का नाम बस्तिकल्प। संधि जाँची: अथातो = अथ + अतः (अ + अ → आ; अः + घोष व्यंजन ब → ओ)। "
          "‘बस्तिकल्पं’ का अनुस्वार = म् (बस्तिकल्पम्)। कोई पाठभेद या text_flag नहीं। आगे की पंक्ति ०५.०४.२ में छपा ‘बळां’ का ळ मराठी छपाई का ल है।"),
    "2": ("विश्वास: उच्च। पंक्तियाँ ०५.०४.२-३; नुस्खा श्लोक ३ और ४ तक चलता है (क्रिया ‘पचेत्’ यहीं है)। छपा ‘बळां’ = बलाम् (ळ = ल)। "
          "‘पलोन्मितानि’ नपुंसक बहुवचन है, स्त्रीलिंग द्रव्यों से मेल नहीं खाता; अर्थ ‘पल से मापे हुए’, पल की संख्या नहीं दी। "
          "खुला बिन्दु (OPEN ०५.०४.२): ‘सरास्नाम्’ पर बहुव्रीहि का व्याकरण-लेबल संदिग्ध है; इस पर प्रश्न नहीं। आठ फलों के नाम नहीं दिए (OPEN ०५.०४.३), "
          "दस मूल भी नहीं गिनाए। संधि जाँची: पलोन्मितानि = पल + उन्मितानि; फलान्यर्द्धतुलां = फलानि + अर्द्धतुलाम्; मांसाच्छागात् = मांसात् + छागात् (त् + छ → च्छ); "
          "पचेदप्सु = पचेत् + अप्सु। ‘अर्द्ध’ में दोहरा द छपाई का रूप है।"),
    "3": ("विश्वास: मध्यम। पंक्तियाँ ०५.०४.४-५ एक वाक्य हैं: षष्ठी की सूची ‘कल्कैः’ पर पूरी होती है। ‘पूते’ भावे सप्तमी है, संज्ञा नहीं दी। "
          "‘यवानीफल’ एक द्रव्य (अजवायन का फल) या दो (यवानी और फल) पढ़ा जा सकता है; इस पर प्रश्न नहीं। text_flag: छपा ‘शताव्हा’ = शताह्वा (व-ह उलटे)। "
          "‘घन’ को मुस्ता मानना सम्भावित ही है। तेल का प्रकार नहीं दिया। संधि जाँची: कल्कैर्मृद्वीका = कल्कैः + मृद्वीका; सतैलैर्युक्तः = सतैलैः + युक्तः; "
          "सुखोष्णो = सुख + उष्णः (अ + उ → ओ); लवणान्वितश्च = लवण + अन्वितः + च। छपाई में ‘सुखोष्णोलवण’ बिना अंतर के है।"),
    "4": ("विश्वास: उच्च। पंक्तियाँ ०५.०४.६-७। ‘जीवनबृंहणः’ एक गुण या दो गुण (जीवन, बृंहण) दोनों पढ़े जा सकते हैं; अर्थ वही रहता है। "
          "‘अमुम्’ पुल्लिंग है, इसे ‘कल्क’ (श्लोक ३) माना गया; पाठ नहीं कहता कौन-सा कल्क। खुला बिन्दु (OPEN ०५.०४.७): ‘सर्वत्र’ का शाब्दिक अर्थ ‘सब जगह’ है, "
          "‘हर स्थिति में’ व्याख्या है; इस पर प्रश्न नहीं। छपा ‘प्रणितो’ (ह्रस्व इ) शब्द-सूची में प्रणीतः पढ़ा गया है। संधि जाँची: हितो = हितः (घोष व्यंजन से पहले); "
          "दद्यादमुमेव = दद्यात् + अमुम् + एव।"),
    "5": ("विश्वास: निम्न। पंक्तियाँ ०५.०४.८-९। ‘सपैर्बपेष्यः’ बिगड़ा शब्द है, अविभाजित रखा; केवल ‘-पेष्यः’ (पीसने योग्य) पहचाना जाता है। "
          "text_flag: सम्भवतः ‘सपेष्यः’ (श्लोक १२ की पंक्ति ०५.०४.२३ में यह रूप आता है), पक्का पाठ नहीं; इस पर प्रश्न नहीं। "
          "‘सच्छाग’ को सत् + छाग (अच्छा बकरा) पढ़ा गया; स + छाग भी यही रूप देता, पर षष्ठी से नहीं बैठता। खट्टा पदार्थ और तीन स्नेह नाम से नहीं दिए। "
          "संधि जाँची: रसोऽम्ल = रसः + अम्ल (अः + अ → ओऽ); प्रवरो निरूहः = प्रवरः + निरूहः; सर्वानिल = सर्व + अनिल।"),
    "6": ("विश्वास: मध्यम। पंक्तियाँ ०५.०४.१०-११; नुस्खा श्लोक ७ तक चलता है। पहली पंक्ति एक लम्बा समास है जिसके अन्त में पञ्चमी ‘सुसिद्धात्’ है; किसमें पकाया, यह नहीं कहा। "
          "छपे ‘त्रायंतिकाएरंड’ में आ + ए की संधि नहीं की गई (स्वर-विच्छेद)। text_flag: ‘रसाच्छागरसाईयुक्तः’ में फालतू ‘ई’; सुझाव रसाच्छागरसयुक्तः, पर छपी पंक्ति के २२ अक्षर हैं, "
          "इसलिए यह किसी दूसरे बिगड़े शब्द का अंश भी हो सकता है (OPEN ०५.०४.११)। इस पर प्रश्न नहीं। ‘यावत्’ के साथ ‘तावत्’ नहीं है।"),
    "7": ("विश्वास: मध्यम। पंक्तियाँ ०५.०४.१२-१३; श्लोक ६ के नुस्खे को पूरा करता प्रतीत होता है, कर्ता वही प्रस्थ है। ‘स-’ चारों (तैल, सर्पिः, मधु, सैंधव) पर लागू माना गया। "
          "‘चक्षुर्बलम्’ = आँखों का बल, या ‘आँख और बल’ (चक्षुः, बलम्); इस पर प्रश्न नहीं। संधि जाँची: सर्पिर्मधु = सर्पिः + मधु; स्याद्दीपनो = स्यात् + दीपनः; "
          "चक्षुर्बलं = चक्षुः + बलम्; चोपदधाति = च + उपदधाति (अ + उ → ओ)।"),
    "8": ("विश्वास: मध्यम। पंक्तियाँ ०५.०४.१४-१५; नया नुस्खा (श्लोक ८-११)। इस श्लोक में क्रिया नहीं; पकाना श्लोक ९ में (‘विपाचयेत्’)। "
          "‘पलाश’ = सम्भवतः ढाक, या ‘पत्ता’; कौन-सा भाग, यह नहीं कहा। ‘पलांशम्’ = पल का अंश। text_flag: छपा ‘आर्गवध’ = आरग्वध (ग और आ उलटे; पंक्ति ०५.०४.३४ में सही छपा)। "
          "दूसरी पंक्ति की सूची के साथ मात्राएँ नहीं हैं। संधि जाँची: एरंडमूलात्त्रिपलं = एरंडमूलात् + त्रिपलम्; पलाशात्तथा = पलाशात् + तथा; बलाच्छिन्नरुहा = बला + छिन्नरुहा।"),
    "9": ("विश्वास: निम्न। पंक्तियाँ ०५.०४.१६-१७। आठ फलों के नाम नहीं। ‘अष्टमशेषिते’ भावे सप्तमी है; आठवाँ भाग किसका, यह नहीं कहा (स्वाभाविक अर्थ: जल का)। "
          "‘पुष्पामि’ अस्पष्ट है, अविभाजित रखा; इस पर प्रश्न नहीं (OPEN ०५.०४.१७ भी यही कहता है)। text_flag: छपा ‘शताव्हा’ = शताह्वा। "
          "‘वत्सकबीज’ = वत्सक के बीज; ‘मुस्त’ अलग द्रव्य। संधि जाँची: चाष्टौ = च + अष्टौ; विपाचयेदष्टम… = विपाचयेत् + अष्टम…; शेषितेऽस्मिन् = शेषिते + अस्मिन् (ए + अ → एऽ)।"),
    "10": ("विश्वास: मध्यम। पंक्तियाँ ०५.०४.१८-१९; वाक्य श्लोक ११ (पंक्तियाँ २०-२१) में चलता है। ‘दद्यात्’ का कर्म श्लोक ९ की सूची है, नाम नहीं लिया। ‘सह’ के साथ द्वितीया असामान्य है। "
           "खुला बिन्दु (OPEN ०५.०४.१८): तार्क्ष्यशैल की पहचान विवादित (रसाञ्जन एक मत, स्रोतोञ्जन जैसा खनिज दूसरा); ‘सम्भवतः’ बनाए रखा। अक्ष का माप किस पर, यह नहीं कहा। "
           "माक्षिक सम्भवतः शहद, खनिज भी हो सकता है। मूत्र का प्रकार नहीं दिया। संधि जाँची: बस्तिर्जयेत् = बस्तिः + जयेत्; जयेल्लेखन = जयेत् + लेखन (त् + ल → ल्ल); "
           "दीपनो ऽसौ = दीपनः + असौ (छपाई में अंतर के साथ)।"),
    "11": ("विश्वास: निम्न। पंक्तियाँ ०५.०४.२०-२१; ‘जयेत्’ (श्लोक १०) का कर्म। ‘शूल’ हर अंग पर लागू है, यह स्वाभाविक अर्थ है पर निश्चित नहीं। "
           "text_flag: ‘बध्म’ ज्ञात शब्द नहीं; सम्भवतः ‘वर्ध्म’ (अण्डकोष या जाँघ के मूल की सूजन), पक्का पाठ नहीं। ‘गुदोत्थान्’ सब सदस्यों पर लागू है या केवल गुद पर, अनिश्चित। "
           "इन पर प्रश्न नहीं। संधि जाँची: जंघोरु = जंघा + ऊरु (आ + ऊ → ओ); हृद्गुह्य = हृद् + गुह्य; गुदोत्थांस्तांस्तांश्च = गुद + उत्थान् + तान् + तान् + च; रोगान्कफ = रोगान् + कफ।"),
}


AIDS = {
    "1": {
        "chunks": "अथातो | बस्तिकल्पं | व्याख्यास्यामः।",
        "sandhi": "अ + अ → आ, और अः + घोष व्यंजन → ओ: अथ + अतः → अथातो (बस्तिकल्पं से पहले)।",
        "anchors": "अथ = अब · अतः = इसलिए · बस्ति = औषधीय एनीमा · कल्प = विधियों का संग्रह · व्याख्यास्यामः = हम व्याख्या करेंगे।",
    },
    "2": {
        "diagram": {"groups": [{"label": "पल से मापे", "items": ["बला", "गुडूची", "त्रिफला", "रास्ना", "द्विपंचमूल"]},
                               {"label": "और", "items": ["अष्टौ फलानि", "अर्द्धतुला छाग-मांस"]},
                               {"label": "विधि", "items": ["अप्सु पचेत्", "चतुर्थशेषम्"]}]},
        "chunks": "बळां गुडूचीं त्रिफलां सरास्नां | द्विपंचमूलं च पलोन्मितानि ‖ अष्टौ फलान्यर्द्धतुलां च | मांसाच्छागात्पचेदप्सु चतुर्थशेषं।",
        "sandhi": "इ + भिन्न स्वर → य्: फलानि + अर्द्ध → फलान्यर्द्ध; त् + छ → च्छ: मांसात् + छागात् → मांसाच्छागात्; त् + स्वर → द्: पचेत् + अप्सु → पचेदप्सु।",
        "anchors": "पल, तुला = तौल के माप · अर्द्ध = आधा · छाग = बकरा · अप्सु = जल में · चतुर्थशेष = चौथाई बचे।",
    },
    "3": {
        "diagram": {"groups": [{"label": "कल्क के द्रव्य", "items": ["यवानीफल", "बिल्व", "कुष्ठ", "वचा", "शताह्वा", "घन", "पिप्पली"]},
                               {"label": "साथ में", "items": ["मृद्वीका", "क्षौद्र", "घृत", "तैल"]},
                               {"label": "कैसा", "items": ["सुखोष्ण", "लवणान्वित"]}]},
        "chunks": "पूते | यवानीफलबिल्वकुष्ठवचाशताव्हाघनपिप्पलीनां ‖ कल्कैर्मृद्वीकाक्षौद्रघृतैः | सतैलैर्युक्तः | सुखोष्णो लवणान्वितश्च।",
        "sandhi": "अ + उ → ओ: सुख + उष्णः → सुखोष्णः; अ + अ → आ: लवण + अन्वितः → लवणान्वितः; ऐः + घोष → ऐर्: कल्कैः + मृद्वीका → कल्कैर्मृद्वीका।",
        "frame": "कब: छान लेने पर (पूते) · क्या मिले: यवानीफल से पिप्पली तक के कल्क, मुनक्का, शहद, घी, तेल · कैसी: सुहाती गरम, नमक-युक्त।",
    },
    "4": {
        "diagram": {"groups": [{"label": "यह बस्ति", "items": ["सर्वगदप्रमाथी", "स्वस्थे हित", "जीवन", "बृंहण"]},
                               {"label": "नियम", "items": ["जिस बस्ति में कल्क न हो", "वहाँ इसी को दे"]}]},
        "chunks": "बस्तिः परं सर्वगदप्रमाथी | स्वस्थे हितो जीवनबृंहणश्च ‖ बस्तौ च यस्मिन् प्रणितो न कल्कः | सर्वत्र दद्यादमुमेव तत्र।",
        "sandhi": "अः + घोष व्यंजन → ओ: हितः + जीवन → हितो जीवन; त् + स्वर → द्: दद्यात् + अमुम् → दद्यादमुम्; म् + ए → मे: अमुम् + एव → अमुमेव।",
        "frame": "पंक्ति १: क्या करती है (सब रोग नाशे, स्वस्थ को हित, जीवन, पुष्टि) · पंक्ति २: कहाँ (जहाँ कल्क न कहा, वहाँ यही)।",
    },
    "5": {
        "chunks": "द्विपंचमूलस्य रसोऽम्लयुक्तः | सच्छागमांसस्य सपैर्बपेष्यः (बिगड़ा शब्द) ‖ त्रिस्नेहयुक्तः प्रवरो निरूहः | सर्वानिलव्याधिहरः प्रदिष्टः।",
        "frame": "क्या: दशमूल और अच्छे बकरे के मांस का रस · साथ: खट्टा, तीन स्नेह · नाम: श्रेष्ठ निरूह · फल: वात के सब रोग हरे।",
        "anchors": "रस = द्रव, शोरबा · अम्ल = खट्टा · त्रिस्नेह = तीन स्नेह · निरूह = काढ़े की बस्ति · अनिल = वात।",
        "sandhi": "अः + अ → ओऽ: रसः + अम्ल → रसोऽम्ल; अ + अ → आ: सर्व + अनिल → सर्वानिल।",
    },
    "6": {
        "chain": {"steps": ["बला, पटोली, लघुपंचमूल, त्रायन्तिका, एरण्ड, यव: भली-भाँति पकाए",
                            "उस रस में से प्रस्थ भर",
                            "बकरे के रस से युक्त",
                            "फिर पकाए, जब तक प्रस्थ भर रहे"]},
        "chunks": "बलापटोलीलघुपंचमूलत्रायंतिकाएरंडयवात्सुसिद्धात् ‖ प्रस्थो रसाच्छागरसाईयुक्तः | साध्यः पुनः प्रस्थसमः स यावत्।",
        "anchors": "सुसिद्ध = भली-भाँति पका · प्रस्थ = एक माप · छाग-रस = बकरे का रस · पुनः = फिर · यावत् = जब तक।",
    },
    "7": {
        "diagram": {"groups": [{"label": "कल्क", "items": ["प्रियंगु", "कृष्णा", "घन"]},
                               {"label": "साथ में", "items": ["तैल", "सर्पिः", "मधु", "सैंधव"]},
                               {"label": "फल", "items": ["दीपन", "मांसबलप्रद", "चक्षुर्बल", "सद्यः"]}]},
        "chunks": "प्रियंगुकृष्णाघनकल्कयुक्तः | सतैलसर्पिर्मधुसैंधवश्च ‖ स्याद्दीपनो मांसबलप्रदश्च | चक्षुर्बलं चोपदधाति सद्यः।",
        "sandhi": "त् + घोष → द्: स्यात् + दीपनः → स्याद्दीपनः; अ + उ → ओ: च + उपदधाति → चोपदधाति; इः + घोष → इर्: सर्पिः + मधु → सर्पिर्मधु।",
        "anchors": "कृष्णा = पीपर · सर्पिः = घी · सैंधव = सेंधा नमक · दीपन = पाचन-अग्नि जगाने वाला · सद्यः = तुरन्त।",
    },
    "8": {
        "diagram": {"groups": [{"label": "मात्रा के साथ", "items": ["एरण्डमूल: त्रिपल", "पलाश: पलांश"]},
                               {"label": "मात्रा नहीं दी", "items": ["लघुपंचमूल", "रास्ना", "बला", "छिन्नरुहा", "अश्वगन्धा",
                                                                    "पुनर्नवा", "आरग्वध", "देवदारु"]}]},
        "chunks": "एरंडमूलात्त्रिपलं | पलाशात्तथा पलांशं | लघुपंचमूलं ‖ रास्नाबलाच्छिन्नरुहाश्वगंधापुनर्नवार्गवधदेवदारु।",
        "sandhi": "स्वर + छ → च्छ: बला + छिन्नरुहा → बलाच्छिन्नरुहा; आ + अ → आ: छिन्नरुहा + अश्वगंधा → छिन्नरुहाश्वगंधा।",
        "anchors": "एरण्ड = अरंडी · पलाश = सम्भवतः ढाक · छिन्नरुहा = गिलोय · अश्वगन्धा = असगंध · आरग्वध = अमलतास · देवदारु = देवदार।",
    },
    "9": {
        "chain": {"steps": ["श्लोक ८ के द्रव्य + आठ फल", "दो आढक जल में", "भली-भाँति पकाए", "आठवाँ भाग शेष रहने पर"]},
        "chunks": "फलानि चाष्टौ सलिलाढकाभ्यां | विपाचयेदष्टमशेषितेऽस्मिन् ‖ वचाशताव्हापुष्पामि (अस्पष्ट) प्रियंगुयष्टीकणावत्सकबीजमुस्तं।",
        "contrast": "श्लोक २: पकाकर चौथाई शेष (चतुर्थशेष) · श्लोक ९: पकाकर आठवाँ भाग शेष (अष्टमशेष)।",
        "anchors": "सलिल = जल · आढक = एक माप · अष्टम = आठवाँ · यष्टी = मुलेठी · कणा = पीपर · वत्सक = कुटज।",
    },
    "10": {
        "chain": {"steps": ["श्लोक ९ के कल्क-द्रव्य भली-भाँति पीसे", "तार्क्ष्यशैल के साथ, अक्ष के माप का",
                            "नमक के अंश से युक्त", "माक्षिक, तेल और मूत्र के साथ बस्ति",
                            "लेखन और दीपन बस्ति जीत लेगी (श्लोक ११)"]},
        "chunks": "दद्यात्सुपिष्टं | सहतार्क्ष्यशैलम् | अक्षप्रमाणं लवणांशयुक्तं ‖ समाक्षिकस्तैलयुतः समूत्रो | बस्तिर्जयेल्लेखनदीपनो ऽसौ।",
        "sandhi": "इः + घोष → इर्: बस्तिः + जयेत् → बस्तिर्जयेत्; त् + ल → ल्ल: जयेत् + लेखन → जयेल्लेखन।",
        "frame": "क्या: पीसा हुआ कल्क · साथ: तार्क्ष्यशैल, नमक; फिर माक्षिक, तेल, मूत्र · कैसी: लेखन और दीपन · क्रिया: जयेत् (कर्म श्लोक ११ में)।",
    },
    "11": {
        "diagram": {"groups": [{"label": "शूल के स्थान", "items": ["जंघा", "ऊरु", "पाद", "त्रिक", "पृष्ठ", "कोष्ठ", "हृद्", "गुह्य"]},
                               {"label": "और", "items": ["गुरुता", "विबन्ध"]},
                               {"label": "रोग", "items": ["गुल्म आदि से उत्थ", "कफवातजात"]}]},
        "chunks": "जंघोरुपादत्रिकपृष्ठकोष्ठहृद्गुह्यशूलं | गुरुतां विबंधं ‖ गुल्माश्मबध्मग्रहणीगुदोत्थान् | तांस्तांश्च रोगान्कफवातजातान्।",
        "sandhi": "आ + ऊ → ओ: जंघा + ऊरु → जंघोरु; न् + त → ंस्त: तान् + तान् → तांस्तान्; न् + च → ंश्च: तान् + च → तांश्च।",
        "anchors": "जंघा = घुटने से टखने तक की टाँग · ऊरु = जाँघ · त्रिक = कमर का निचला भाग · कोष्ठ = पेट · गुरुता = भारीपन · विबन्ध = मल का रुकना।",
    },
}


IMAGE_SPECS = {
    ("2", "diagram"): {
        "file": "ka4-baladi-2.svg",
        "alt": ("Flowchart of verse 2: bala, guduchi, triphala, rasna and the ten-root group measured by the pala, with eight fruits "
                "and half a tula of goat meat, are cooked in water until a quarter remains"),
        "type": "mermaid",
        "code": ('flowchart TD\n'
                 '  A["बला · गुडूची · त्रिफला"] --> P["पल से मापे"]\n'
                 '  B["रास्ना · द्विपंचमूल"] --> P\n'
                 '  P --> D["जल में पकाए"]\n'
                 '  C["आठ फल"] --> D\n'
                 '  M["आधा तुला बकरे का मांस"] --> D\n'
                 '  D --> E["चौथाई शेष रहे"]\n'),
    },
    ("3", "diagram"): {
        "file": "ka4-kalka-3.svg",
        "alt": ("Two columns for verse 3: the paste drugs (yavani-phala, bilva, kushtha, vacha, shatahva, ghana, pippali) and "
                "the additions and state (grape, honey, ghee, oil, pleasantly warm, with salt)"),
        "type": "split",
        "title": "श्लोक ३: छानने के बाद",
        "cols": [["कल्क के द्रव्य", ["यवानीफल", "बिल्व", "कुष्ठ", "वचा", "शताह्वा", "घन", "पिप्पली"]],
                 ["साथ में · कैसा", ["मृद्वीका", "क्षौद्र (शहद)", "घृत", "तैल", "सुखोष्ण", "लवण"]]],
    },
    ("4", "diagram"): {
        "file": "ka4-guna-4.svg",
        "alt": ("Mind map of verse 4: the basti destroys all diseases, is beneficial for the healthy, life-giving and nourishing; "
                "rule: where a basti has no paste, give this one"),
        "type": "mermaid",
        "code": ('mindmap\n  यह बस्ति\n    गुण\n      सब रोगों का नाशक\n      स्वस्थ को हितकर\n'
                 '      जीवन देने वाली\n      पुष्टि करने वाली\n    नियम\n      जहाँ कल्क न कहा\n      वहाँ इसी को दे\n'),
    },
    ("6", "chain"): {
        "file": "ka4-prastha-6.svg",
        "alt": ("Chain of four steps for verse 6: six drugs well cooked; a prastha of that liquid; joined with goat broth; "
                "cooked again until it equals a prastha"),
        "type": "chain",
        "title": "श्लोक ६: प्रस्थ भर रस",
        "steps": ["बला से यव तक छह द्रव्य भली-भाँति पकाए", "उस रस में से प्रस्थ भर",
                  "बकरे के रस से युक्त", "फिर पकाए: जब तक प्रस्थ भर रहे"],
    },
    ("7", "diagram"): {
        "file": "ka4-dipana-7.svg",
        "alt": ("Flowchart of verse 7: the prepared liquid takes a paste of priyangu, krishna and ghana, then oil, ghee, honey and "
                "rock salt; effects: kindling, flesh and strength, strength of the eyes at once"),
        "type": "mermaid",
        "code": ('flowchart TD\n'
                 '  A["श्लोक ६ का तैयार रस"] --> B["कल्क: प्रियंगु कृष्णा घन"]\n'
                 '  B --> C["तेल · घी · शहद · सैन्धव"]\n'
                 '  C --> D["दीपन"]\n'
                 '  C --> E["मांस और बल"]\n'
                 '  C --> F["तुरन्त आँखों का बल"]\n'),
    },
    ("8", "diagram"): {
        "file": "ka4-erandamula-8.svg",
        "alt": ("Two columns for verse 8: with a measure, eranda root three palas and palasha a pala-portion; without a measure, "
                "the small five roots, rasna, bala, chinnaruha, ashvagandha, punarnava, aragvadha and devadaru"),
        "type": "split",
        "title": "श्लोक ८: एरण्डमूल की बस्ति",
        "cols": [["मात्रा के साथ", ["एरण्डमूल: तीन पल", "पलाश: पल का अंश"]],
                 ["मात्रा नहीं दी", ["लघुपंचमूल", "रास्ना", "बला", "छिन्नरुहा", "अश्वगन्धा", "पुनर्नवा", "आरग्वध", "देवदारु"]]],
    },
    ("9", "chain"): {
        "file": "ka4-ashtamashesha-9.svg",
        "alt": ("Chain of four steps for verse 9: the drugs of verse 8 with eight fruits, in two adhakas of water, cooked thoroughly, "
                "until an eighth remains"),
        "type": "chain",
        "title": "श्लोक ९: पकाने की विधि",
        "steps": ["श्लोक ८ के द्रव्य + आठ फल", "दो आढक जल में", "भली-भाँति पकाए", "आठवाँ भाग शेष रहने पर"],
    },
    ("10", "chain"): {
        "file": "ka4-lekhana-10.svg",
        "alt": ("Flowchart of verse 10: the paste drugs well ground, with tarkshyashaila of an aksha measure and a portion of salt; "
                "the basti with makshika, oil and urine; a scraping and kindling basti that overcomes the troubles of verse 11"),
        "type": "mermaid",
        "code": ('flowchart TD\n'
                 '  A["श्लोक ९ के कल्क पीसे"] --> B["तार्क्ष्यशैल, अक्ष-माप"]\n'
                 '  B --> C["नमक का अंश"]\n'
                 '  C --> D["माक्षिक · तेल · मूत्र"]\n'
                 '  D --> E["लेखन और दीपन बस्ति"]\n'
                 '  E --> F["जीत लेगी: श्लोक ११"]\n'),
    },
    ("11", "diagram"): {
        "file": "ka4-shula-11.svg",
        "alt": ("Two columns for verse 11: eight sites of pain (shank, thigh, foot, trika, back, belly, heart, private part) and "
                "the rest (heaviness, obstruction, diseases arising from gulma and the others, diseases of Kapha and Vata)"),
        "type": "split",
        "title": "श्लोक ११: बस्ति क्या जीतती है",
        "cols": [["पीड़ा के स्थान (८)", ["जंघा", "ऊरु", "पाद", "त्रिक", "पृष्ठ", "कोष्ठ", "हृदय", "गुह्य"]],
                 ["और", ["गुरुता", "विबन्ध", "गुल्म आदि से उत्पन्न रोग", "कफ-वात से जन्मे रोग"]]],
    },
}
