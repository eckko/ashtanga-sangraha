from helpers import mcq, match, order, fill, multi, accepts


AUTHORED = {}

# ---------------------------------------------------------------- unit 78
AUTHORED["78"] = {
    "title": "तेषां दूषणं ... लक्षयेत्",
    "question": "By unit 78, what should one know about these (teṣām), and by what sign is each discerned?",
    "rule": ("Of these (तेषाम्), the vitiation (दूषणम्), the unwholesome food and conduct (अहिताहारविहारम्), the "
             "complications (उपद्रवान्) and the treatment (साधनम्) are to be known (the data reads विज्ञानीयात् as 'one "
             "should know'); each (यथास्वम्) is discerned (लक्षयेत्) by the signs of increase and decrease "
             "(वृद्धिक्षयलक्षणेन)."),
    "limits": ("Prose; loose syntax. How दोषादिविज्ञानीयात् fits is open: the data reads दोषादि + विज्ञानीयात् ('one "
               "should know'), but the form may also be the ablative of a chapter name (Doṣādivijñānīya): no question on "
               "its sense. विविधम् may qualify the vitiation or the food and conduct. तेषाम् is not named."),
    "explain_hi": ("यह गद्य-पंक्ति बताती है कि इनके (तेषाम्) बारे में चार बातें जाननी चाहिए: दूषण (बिगाड़), अहितकर आहार और विहार यानी "
                   "आचरण, उपद्रव और साधन यानी चिकित्सा। "
                   "हर एक को अपने-अपने अनुसार (यथास्वम्) वृद्धि और क्षय के लक्षणों से पहचानना चाहिए (लक्षयेत्)। "
                   "‘दोषादिविज्ञानीयात्’ का अर्थ खुला है: डेटा इसे दोषादि + विज्ञानीयात् (‘जानना चाहिए’) पढ़ता है, ‘दोष आदि से जानना’ या ‘दोष आदि को भी जानना’; पर यह ‘दोषादिविज्ञानीय’ नाम के अध्याय से (पञ्चमी) भी हो सकता है। "
                   "‘विविधम्’ (अनेक प्रकार का) दूषण के साथ भी पढ़ा जा सकता है और आहार-विहार के साथ भी। "
                   "‘तेषाम्’ किनका है, यह पंक्ति में छपा नहीं।"),
    "hook": "दूषण, अहित आहार-विहार, उपद्रव, साधन: सबको वृद्धि-क्षय के लक्षण से पहचानो।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 78, by what sign should one discern each (yathāsvam)?",
            ("By the signs of increase and decrease", "वृद्धिक्षयलक्षणेन लक्षयेत्: by the sign of increase and decrease."),
            [("By the colour and the smell of the urine", "Urine is not named in unit 78."),
             ("By the beat of the pulse felt at the wrist", "The pulse is not named in unit 78."),
             ("By the dreams and the omens of the night", "Dreams and omens are not named in unit 78.")],
            "Each is discerned by the signs of increase (वृद्धि) and decrease (क्षय).",
            "यथास्वं वृद्धिक्षयलक्षणेन लक्षयेत्."),
        order(1, "Put these four things to be known in the order of unit 78.",
              ["दूषणं", "अहिताहारविहारम्", "उपद्रवान्", "साधनं"],
              "Vitiation, unwholesome food and conduct, complications, treatment.",
              "दूषणं → अहिताहारविहारम् → उपद्रवान् → साधनं."),
        match(2, "Match each word of unit 78 to its meaning.",
              [["दूषण", "vitiation, spoiling"], ["अहित", "unwholesome"], ["विहार", "conduct"],
               ["उपद्रव", "complication"], ["साधन", "treatment"]],
              "Vitiation, unwholesome food and conduct, complications and treatment are to be known.",
              "दूषण, अहित, विहार, उपद्रव, साधन.", role="extend",
              teaches="अहित = अ (not) + हित (wholesome); अहिताहारविहार = unwholesome food and conduct (अ + आ → आ)."),
        mcq("discriminate", 3, "Which split of विज्ञानीयाद्यथास्वं in unit 78 is right?",
            ("विज्ञानीयात् + यथास्वम्", "त् before the voiced य becomes द्: विज्ञानीयाद्यथास्वम्."),
            [("विज्ञानीयाः + यथास्वम्", "आः before the voiced य would lose its visarga: विज्ञानीया यथास्वम्."),
             ("विज्ञानीया + द्यथास्वम्", "द्यथास्वम् is not a word; the द् comes from the final त् of विज्ञानीयात्."),
             ("विज्ञानीयम् + यथास्वम्", "म् before य would be written ं: विज्ञानीयं यथास्वम्.")],
            "विज्ञानीयात् + यथास्वम् (each by its own): त् + य → द्य.",
            "A final त् becomes द् before a voiced sound."),
        multi("apply", 4, "Which does unit 78 name among the things to be known or discerned?",
              [("The number (saṅkhyā) of the channels", "No number is given in unit 78."),
               ("The complications (upadrava)", "Right: उपद्रवान्."),
               ("The age (vayas) of the patient", "Age is not named in unit 78."),
               ("The treatment (sādhana)", "Right: साधनं च.")],
              [1, 3],
              "Vitiation, unwholesome food and conduct, complications and treatment; each by increase and decrease.",
              "दूषणं ... अहिताहारविहारमुपद्रवान् साधनं च."),
        mcq("transfer", 5, "By the rule of विज्ञानीयात् + यथास्वम्, how is भवेत् + यदि joined in a new example?",
            ("भवेद्यदि", "त् before the voiced य becomes द्, as विज्ञानीयात् + यथास्वम् → विज्ञानीयाद्यथास्वम्."),
            [("भवेत्यदि", "त् does not stay before a voiced sound; य is voiced."),
             ("भवेच्यदि", "त् becomes च् before च, छ or श, not before य."),
             ("भवेन्यदि", "न् comes before a nasal; य is not a nasal.")],
            "भवेत् + यदि = भवेद्यदि, like विज्ञानीयात् + यथास्वम् = विज्ञानीयाद्यथास्वम्.",
            "त् + voiced sound → द्.",
            teaches="A final त् becomes द् before a voiced sound such as य: विज्ञानीयात् + यथास्वम् → विज्ञानीयाद्यथास्वम्."),
    ],
}

# ---------------------------------------------------------------- unit 79
AUTHORED["79"] = {
    "title": "व्यधे तु स्रोतसां",
    "question": "By unit 79, what follows on the piercing (vyadha) of the srotas (channels)?",
    "rule": ("On the piercing (व्यधे) of the srotas: giddiness, moha (fainting or confusion), tremor, raving, distension "
             "of the belly, pain, distaste for food, thirst, vomiting, fever, retention of urine and stool, and death "
             "(मरणम्)."),
    "limits": ("Prose; confidence low (damaged print). The letters after ज्वर (अनिरुधिरश्रुति) are read only on a conjecture "
               "as rudhira-śruti (flow of blood) with a stray 'ani': no question on them. No verb is printed. मोह may be "
               "fainting or confusion. Which channel gives which sign is not said."),
    "explain_hi": ("यह गद्य-पंक्ति बताती है कि स्रोतसों के वेध (बिंधने) पर क्या होता है: भ्रम (चक्कर), मोह (मूर्छा या भ्रान्ति), कम्प, "
                   "प्रलाप, आध्मान (पेट फूलना), शूल, अरुचि, प्यास, छर्दि (वमन), ज्वर, मूत्र और मल का रुकना, और मृत्यु। "
                   "छपाई क्षतिग्रस्त है और डेटा का विश्वास कम है। "
                   "ज्वर के बाद के अक्षर ‘अनिरुधिरश्रुति’ अस्पष्ट हैं; ‘रुधिरश्रुति’ (रक्त का बहना) केवल अनुमानित पाठ है, इसलिए उस पर "
                   "कोई प्रश्न नहीं। "
                   "पूरी सूची छपाई में जुड़ी हुई है; डेटा इसे प्रथमा की सूची पढ़ता है; क्रिया छपी नहीं, ‘होते हैं’ समझा जाता है।"),
    "hook": "स्रोतस् बिंधे तो चक्कर से मृत्यु तक लम्बी सूची।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 79, what is the last result named for the piercing of the srotas?",
            ("Death (मरणम्)", "The line ends मरणं च: and death."),
            [("Fever (ज्वर)", "Fever is in the list, but not at its end."),
             ("Tremor (कम्प)", "Tremor is third in the list, not last."),
             ("Thirst (तृष्)", "Thirst is in the middle of the list.")],
            "The list ends with death: मरणं च.",
            "...मूत्रपुरीषरोधा मरणं च."),
        order(1, "Put the first five results of unit 79 in the line's order.",
              ["भ्रम", "मोह", "कम्प", "प्रलाप", "आध्मान"],
              "Giddiness, moha, tremor, raving, distension of the belly.",
              "भ्रम → मोह → कम्प → प्रलाप → आध्मान."),
        match(2, "Match each result named in unit 79 to its meaning.",
              [["भ्रम", "giddiness"], ["कम्प", "tremor"], ["प्रलाप", "raving, delirium"],
               ["आध्मान", "distension of the belly"], ["अरुचि", "distaste for food"], ["छर्दि", "vomiting"]],
              "Six of the results of piercing the srotas.",
              "भ्रम, कम्प, प्रलाप, आध्मान, अरुचि, छर्दि.", role="extend",
              teaches="The results are printed run together; the data reads them as a list of nominatives ending in -रोधाः (m. nom. pl.)."),
        mcq("discriminate", 3, "In unit 79, why is the visarga of रोधाः not printed before मरणं?",
            ("आः loses its visarga before a voiced sound", "म is voiced, so रोधाः + मरणम् → रोधा मरणम्."),
            [("The visarga turns to ओ before the म", "ओ comes from अः, not from आः."),
             ("The visarga turns to र् before the म", "र् comes from a visarga after vowels other than अ or आ."),
             ("The visarga turns to स् before the म", "स् comes before त or थ, not before म.")],
            "रोधाः (retentions) + मरणम् (death): आः before a voiced sound drops the visarga.",
            "आः + voiced sound → आ (visarga lost)."),
        multi("apply", 4, "Which are named in unit 79 as results of piercing the srotas?",
              [("Retention of urine and stool", "Right: मूत्रपुरीषरोधाः."),
               ("Swelling of the limbs", "Swelling is not named in unit 79."),
               ("Distension of the belly", "Right: आध्मान."),
               ("Itching of the skin", "Itching is not named in unit 79.")],
              [0, 2],
              "Retention of urine and stool and distension of the belly are in the list.",
              "...आध्मान... मूत्रपुरीषरोधाः."),
        mcq("transfer", 5, "By the rule of शूल + अरुचि → शूलारुचि, how is सूर्य + अस्तः joined in a new example?",
            ("सूर्यास्तः", "अ + अ → आ, as शूल + अरुचि → शूलारुचि."),
            [("सूर्येस्तः", "ए comes from अ + इ, not from अ + अ."),
             ("सूर्योस्तः", "ओ comes from अ + उ, not from अ + अ."),
             ("सूर्यस्तः", "The two अ merge into a long आ, not a short अ.")],
            "सूर्य + अस्तः = सूर्यास्तः, like शूल + अरुचि = शूलारुचि.",
            "अ + अ → आ.",
            teaches="Two short अ merge into a long आ: शूल + अरुचि → शूलारुचि."),
    ],
}

# ---------------------------------------------------------------- unit 80
AUTHORED["80"] = {
    "title": "तस्मात्स्रोतौविद्धं प्रत्याख्यायोपाचरेत्",
    "question": "By unit 80, how is one pierced in a srotas handled, and how is one whose dart is extracted treated?",
    "rule": ("Therefore (तस्मात्), having refused (प्रत्याख्याय, declined the case as hopeless) one pierced in a srotas, one "
             "should treat (उपाचरेत्) him; and one whose dart is extracted (उद्धृतशल्यम्), by the procedure for a fresh "
             "wound (सद्योव्रणविधानेन)."),
    "limits": ("Prose, two lines. Printed स्रोतौविद्धं is read srotoviddham ('au' a print slip): no question on how that form is read "
               "(the order question uses only its printed position). "
               "Line 2 takes its verb from line 1. The fresh-wound procedure and the reason for treating after refusing "
               "are not given."),
    "explain_hi": ("‘तस्मात्’ (इसलिए) पिछली बात से निष्कर्ष निकालता है। "
                   "स्रोतस् में विद्ध (बिंधे हुए) रोगी को ‘प्रत्याख्याय’ यानी अस्वीकार करके (रोग को असाध्य कहकर) उपचार करना चाहिए "
                   "(उपाचरेत्); पंक्ति इसका कारण नहीं बताती। "
                   "दूसरी पंक्ति: जिसका शल्य (बाण या भीतर घुसी वस्तु) निकाल लिया गया हो, उसका उपचार सद्योव्रण यानी ताजे घाव की विधि से। "
                   "दूसरी पंक्ति में क्रिया छपी नहीं; पहली पंक्ति की ‘उपाचरेत्’ समझी जाती है। "
                   "छपा ‘स्रोतौविद्धं’ छपाई की भूल लगता है; पढ़ा गया स्रोतोविद्धम्।"),
    "hook": "स्रोतस्-विद्ध: पहले असाध्य कहो, फिर उपचार; शल्य निकला तो ताजे घाव की विधि।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 80, by what procedure is one whose dart is extracted treated?",
            ("The procedure for a fresh wound", "सद्योव्रणविधानेन: by the procedure for a fresh wound."),
            [("The procedure for a burn wound", "Burns are not named in unit 80."),
             ("The procedure for a snake-bite", "Snake-bite is not named in unit 80."),
             ("The procedure for a broken bone", "Fractures are not named in unit 80.")],
            "One whose dart is extracted is treated by the procedure for a fresh wound (सद्योव्रण).",
            "उद्धृतशल्यं च सद्योव्रणविधानेन."),
        order(1, "Put these words of unit 80 in the printed order.",
              ["तस्मात्", "स्रोतौविद्धं", "प्रत्याख्याय", "उपाचरेत्", "उद्धृतशल्यं च", "सद्योव्रणविधानेन"],
              "Therefore, one pierced in a srotas, having refused, one should treat; and one whose dart is extracted, "
              "by the fresh-wound procedure.",
              "तस्मात् → स्रोतौविद्धं → प्रत्याख्याय → उपाचरेत् → उद्धृतशल्यं च → सद्योव्रणविधानेन."),
        match(2, "Match each word of unit 80 to its meaning.",
              [["प्रत्याख्याय", "having refused"], ["उपाचरेत्", "one should treat"], ["उद्धृत", "extracted"],
               ["शल्य", "dart, foreign body"], ["सद्योव्रण", "fresh wound"]],
              "Having refused, one should treat; the one whose dart is extracted, as a fresh wound.",
              "प्रत्याख्याय, उपाचरेत्, उद्धृत, शल्य, सद्योव्रण.", role="extend",
              teaches="प्रत्याख्याय is an absolutive in -य (with a prefix): done before the main verb उपाचरेत्."),
        mcq("discriminate", 3, "Which split of प्रत्याख्यायोपाचरेत् in unit 80 is right?",
            ("प्रत्याख्याय + उपाचरेत्", "अ + उ → ओ: प्रत्याख्याय + उपाचरेत् → प्रत्याख्यायोपाचरेत्."),
            [("प्रत्याख्यायः + उपाचरेत्", "अः before उ would lose its visarga with no join: ...य उपाचरेत्."),
             ("प्रत्याख्यायो + पाचरेत्", "The verb is उपाचरेत्; the ओ comes from अ + उ."),
             ("प्रत्याख्याये + उपाचरेत्", "ए before उ gives अय् or अ, not ओ.")],
            "प्रत्याख्याय (having refused) + उपाचरेत् (one should treat): अ + उ → ओ.",
            "अ + उ → ओ."),
        mcq("apply", 4, "By unit 80, what is done with one pierced in a srotas before he is treated?",
            ("He is first refused (प्रत्याख्याय)", "प्रत्याख्यायोपाचरेत्: having refused, one should treat."),
            [("His dart is left in (शल्य)", "Unit 80 says nothing about leaving a dart in; line 2 is about one whose dart is extracted."),
             ("He is given a purge (विरेचन)", "No purge is named in unit 80."),
             ("He is made to fast (लङ्घन)", "No fasting is named in unit 80.")],
            "Having refused (declined the case as hopeless), one should treat him.",
            "प्रत्याख्याय + उपाचरेत्."),
        mcq("transfer", 5, "By the rule of सद्यः + व्रण → सद्योव्रण, how is मनः + बलम् joined in a new example?",
            ("मनोबलम्", "अः before a voiced consonant becomes ओ, as सद्यः + व्रण → सद्योव्रण."),
            [("मनाबलम्", "अः before a voiced consonant gives ओ, not आ."),
             ("मनर्बलम्", "र् comes from a visarga after vowels other than अ or आ."),
             ("मनस्बलम्", "स् comes before त or थ, not before ब.")],
            "मनः + बलम् = मनोबलम्, like सद्यः + व्रण = सद्योव्रण.",
            "अः + voiced consonant → ओ.",
            teaches="अः before a voiced consonant becomes ओ: सद्यः + व्रण → सद्योव्रण."),
    ],
}

# ---------------------------------------------------------------- unit 81
AUTHORED["81"] = {
    "title": "तत्र स्रोतसामेवविशेषाः",
    "question": "By unit 81, how are sirā and dhamanī related to the srotas?",
    "rule": ("Among these (तत्र), the sirā (vessels, probably veins) and the dhamanī (pulsating vessels, probably "
             "arteries) are particular forms (विशेषाः) of the srotas only (स्रोतसाम् एव)."),
    "limits": ("Prose; the copula is understood. Vein and artery are probable equivalents, not exact. The line gives no "
               "reason; unit 82 reports others who hold a difference."),
    "explain_hi": ("यह गद्य-पंक्ति कहती है कि उनमें सिराएँ और धमनियाँ स्रोतसों के ही (एव) विशेष रूप हैं। "
                   "सिरा = वाहिका, सम्भवतः शिरा (नस); धमनी = स्पन्दन करने वाली वाहिका, सम्भवतः आधुनिक अर्थ की धमनी; दोनों पहचान "
                   "सम्भावित हैं, सटीक नहीं। "
                   "‘हैं’ क्रिया छपी नहीं, समझी जाती है। "
                   "छपा ‘सिरा’ बहुवचन सिराः है; घोष ध से पहले आः का विसर्ग लुप्त हुआ। "
                   "अगली इकाई ८२ में दूसरे आचार्य भिन्नता मानते हैं।"),
    "hook": "सिरा और धमनी: स्रोतस् के ही विशेष रूप।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 81, what are sirā and dhamanī?",
            ("Particular forms of the srotas", "स्रोतसामेव विशेषाः: particular forms of the srotas only."),
            [("Particular forms of the doṣas", "The doṣas are not named in unit 81."),
             ("Particular forms of the malas", "The malas are not named in unit 81."),
             ("Particular forms of the heart", "The heart is not named in unit 81.")],
            "Sirā and dhamanī are particular forms of the srotas.",
            "स्रोतसामेव विशेषाः सिरा धमन्यः."),
        match(1, "Match each word of unit 81 to its meaning.",
              [["तत्र", "among these, there"], ["स्रोतसाम्", "of the srotas"], ["एव", "only"],
               ["विशेषाः", "particular kinds"]],
              "Among these, of the srotas only, particular kinds: sirā and dhamanī.",
              "तत्र, स्रोतसाम्, एव, विशेषाः."),
        fill(2, "In unit 81 'particular kinds' is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("विशेषाः", None, "विशेष"),
             "विशेषाः = particular kinds, special forms (m. nom. pl.).",
             "विशेष = a particular kind; sirā and dhamanī are विशेषाः of the srotas.",
             "स्रोतसामेव विशेषाः."),
        mcq("discriminate", 3, "Why is सिरा printed without a visarga in unit 81?",
            ("आः loses its visarga before the voiced ध", "सिराः + धमन्यः → सिरा धमन्यः (data note)."),
            [("अः turned to ओ before the voiced ध", "ओ comes from अः; सिराः ends in आः."),
             ("The visarga turned to र् before ध", "र् comes from a visarga after vowels other than अ or आ."),
             ("The visarga turned to स् before ध", "स् comes before त or थ, not before ध.")],
            "सिराः (vessels) + धमन्यः: आः before a voiced sound drops the visarga.",
            "आः + voiced sound → आ."),
        multi("apply", 4, "Which statements fit unit 81?",
              [("Sirā and dhamanī are called forms of the srotas", "Right: स्रोतसामेव विशेषाः."),
               ("The line gives a reason for this view", "No reason is given in unit 81."),
               ("Dhamanī is probably the artery (probable)", "Right: the data labels this probable."),
               ("The verb 'are' is printed in the line", "The copula is understood, not printed.")],
              [0, 2],
              "Sirā and dhamanī are forms of the srotas; vein and artery are probable equivalents; no verb.",
              "तत्र स्रोतसामेव विशेषाः सिरा धमन्यः."),
        mcq("transfer", 5, "By the rule of स्रोतसाम् + एव → स्रोतसामेव, how is गृहम् + एव joined in a new example?",
            ("गृहमेव", "Final म् before a vowel stays म् and joins it, as स्रोतसाम् + एव → स्रोतसामेव."),
            [("गृहं एव", "म् becomes ं only before a consonant, not before a vowel."),
             ("गृहैव", "म् does not drop; ऐ would need अ + ए."),
             ("गृहमैव", "ऐ needs अ + ए; here म् meets ए directly.")],
            "गृहम् + एव = गृहमेव, like स्रोतसाम् + एव = स्रोतसामेव.",
            "Final म् + vowel → म joined to the vowel.",
            teaches="A final म् before a vowel stays म् and joins it: स्रोतसाम् + एव → स्रोतसामेव."),
    ],
}

# ---------------------------------------------------------------- unit 82
AUTHORED["82"] = {
    "title": "अन्येत्वन्यत्वमिच्छंति",
    "question": "By unit 82, what do the 'others' (anye) maintain?",
    "rule": ("But others (अन्ये तु) maintain (इच्छन्ति) a difference (अन्यत्वम्, otherness); the data understands sirā, "
             "dhamanī and srotas as what differs."),
    "limits": ("Prose, one printed word-group. What differs from what is not printed (the data understands sirā, dhamanī "
               "and srotas). Who the 'others' are is not said. No reason is given in this line."),
    "explain_hi": ("यह छोटी गद्य-पंक्ति इकाई ८१ के मत के सामने दूसरा मत रखती है: परन्तु (तु) दूसरे (अन्ये) अन्यता यानी भिन्नता मानते हैं (इच्छन्ति)। "
                   "क्या किससे भिन्न है, यह छपा नहीं; डेटा सिरा, धमनी और स्रोतस् को समझता है। "
                   "‘अन्ये’ कौन हैं, पंक्ति नहीं बताती। "
                   "‘अन्यत्व’ = अन्य (दूसरा) + -त्व (भाव): दूसरापन, भिन्नता। "
                   "सन्धि: तु + अन्यत्वम् → त्वन्यत्वम् (उ + भिन्न स्वर → व्)।"),
    "hook": "पर दूसरे कहते हैं: ये अलग-अलग हैं।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 82, what do the 'others' (anye) maintain?",
            ("A difference", "अन्यत्वमिच्छन्ति: they maintain a difference (otherness)."),
            [("A sameness", "Sameness is the opposite of अन्यत्व."),
             ("A common root", "No root is named in unit 82."),
             ("A fixed count", "No number is given in unit 82.")],
            "Others maintain a difference (अन्यत्वम्).",
            "अन्ये तु अन्यत्वम् इच्छन्ति."),
        match(1, "Match each word of unit 82 to its meaning.",
              [["अन्ये", "others"], ["तु", "but"], ["अन्यत्वम्", "difference, otherness"], ["इच्छन्ति", "they hold, maintain"]],
              "But others maintain a difference.",
              "अन्ये, तु, अन्यत्वम्, इच्छन्ति."),
        mcq("extend", 2, "How is the word अन्यत्व built?",
            ("अन्य + त्व: 'other' + '-ness'", "-त्व makes an abstract noun: otherness, difference."),
            [("अन्न + त्व: 'food' + '-ness'", "अन्न (food) has no य; the word is अन्य, other."),
             ("अन्य + त्वम्: 'other' + 'you'", "त्वम् (you) makes no sense here; -त्व is the suffix."),
             ("अन + यत्व: 'not' + 'effort'", "The word is अन्य (other) with -त्व, not अन + यत्व.")],
            "अन्यत्व = अन्य (other) + -त्व (-ness).",
            "-त्व on a word = the state of being that.",
            teaches="-त्व makes an abstract noun: अन्य (other) → अन्यत्व (otherness)."),
        mcq("discriminate", 3, "Which split of त्वन्यत्वम् in unit 82 is right?",
            ("तु + अन्यत्वम्", "उ before a different vowel becomes व्: तु + अन्यत्वम् → त्वन्यत्वम्."),
            [("त्व + अन्यत्वम्", "अ + अ would give आ: त्वान्यत्वम्."),
             ("ते + अन्यत्वम्", "ए before अ would give तेऽन्यत्वम्, with ए kept."),
             ("तुम् + अन्यत्वम्", "म् before a vowel would give तुमन्यत्वम्.")],
            "तु (but) + अन्यत्वम् (difference): उ + अ → व.",
            "उ + a different vowel → व् + that vowel."),
        order(4, "Put the words of unit 82 in the printed order.",
              ["अन्ये", "तु", "अन्यत्वम्", "इच्छंति"],
              "Others, but, a difference, maintain: अन्येत्वन्यत्वमिच्छंति.",
              "अन्ये → तु → अन्यत्वम् → इच्छंति.", role="apply"),
        mcq("transfer", 5, "By the rule of तु + अन्यत्वम् → त्वन्यत्वम्, how is मधु + अत्र joined in a new example?",
            ("मध्वत्र", "उ before a different vowel becomes व्, as तु + अन्यत्वम् → त्वन्यत्वम्."),
            [("मधोत्र", "ओ comes from अ + उ, with अ first; here उ comes first."),
             ("मधूत्र", "ऊ comes from उ + उ, not उ + अ."),
             ("मधुत्र", "The अ does not vanish; the उ becomes व्.")],
            "मधु + अत्र = मध्वत्र, like तु + अन्यत्वम् = त्वन्यत्वम्.",
            "उ + अ → व.",
            teaches="उ before a different vowel becomes व्: तु + अन्यत्वम् → त्वन्यत्वम्."),
    ],
}

# ---------------------------------------------------------------- unit 83
AUTHORED["83"] = {
    "title": "सिराधमनीस्रोतसां केवलं ...",
    "question": "By unit 83, why do sirā, dhamanī and srotas seem not distinct?",
    "rule": ("Merely (केवलम्) through mutual proximity (परस्परसन्निकर्षात्), similarity of function (सदृशकर्मत्वात्) and "
             "fineness (सौक्ष्म्यात्), a non-distinction as it were (अविभाग इव) is perceived (लक्ष्यते) among them, though "
             "their functions are distinct (विभक्तकर्मणाम्)."),
    "limits": ("Prose; it reports a view (data note; compare units 82 and 84). The line does not say what the distinct "
               "functions are. केवलम् is taken with the three reasons (data). The printed अविभागइव is read अविभाग इव."),
    "explain_hi": ("यह गद्य-पंक्ति बताती है कि सिरा, धमनी और स्रोतस् एक-से क्यों दिखते हैं: केवल तीन कारणों से। "
                   "पहला, परस्पर सन्निकर्ष (एक-दूसरे के पास होना); दूसरा, सदृश कर्मत्व (मिलता-जुलता काम); तीसरा, सौक्ष्म्य (सूक्ष्मता)। "
                   "इनके कारण, भिन्न कर्म वाले (विभक्तकर्मणाम्) होते हुए भी, मानो (इव) अभेद दिखाई देता है (लक्ष्यते)। "
                   "‘इव’ बताता है कि अभेद केवल दिखावटी है। "
                   "तीनों कारण पञ्चमी (-आत्, ‘के कारण’) में हैं।"),
    "hook": "पास-पास, मिलते काम, बहुत सूक्ष्म: इसलिए एक-से दिखते हैं, हैं अलग।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 83, which is one reason the three seem alike?",
            ("Their fineness (सौक्ष्म्य)", "सौक्ष्म्याच्च: and from fineness."),
            [("Their colour (वर्ण)", "Colour is not named in unit 83."),
             ("Their length (दैर्घ्य)", "Length is not named in unit 83."),
             ("Their number (संख्या)", "Number is not named in unit 83.")],
            "Proximity, similar function and fineness make them seem alike.",
            "परस्परसन्निकर्षात् सदृशकर्मत्वात् सौक्ष्म्याच्च."),
        order(1, "Put these parts of unit 83 in the printed order.",
              ["सिराधमनीस्रोतसां केवलं", "परस्परसन्निकर्षात्", "सदृशकर्मत्वात्", "सौक्ष्म्याच्च",
               "विभक्तकर्मणामप्यविभागइव", "लक्ष्यते"],
              "Of the three, merely; from proximity, similar function and fineness; non-distinction as it were; is seen.",
              "सिराधमनीस्रोतसां केवलं → परस्परसन्निकर्षात् → सदृशकर्मत्वात् → सौक्ष्म्याच्च → "
              "विभक्तकर्मणामप्यविभागइव → लक्ष्यते."),
        match(2, "Match each word of unit 83 to its meaning.",
              [["परस्पर", "mutual"], ["सन्निकर्ष", "proximity"], ["सदृश", "similar"], ["सौक्ष्म्य", "fineness"],
               ["विभक्त", "distinct, divided"], ["अविभाग", "non-distinction"]],
              "Mutual proximity, similar function, fineness; distinct functions, yet a non-distinction as it were.",
              "परस्पर, सन्निकर्ष, सदृश, सौक्ष्म्य, विभक्त, अविभाग.", role="extend",
              teaches="The three reasons stand in the ablative (-आत्), 'from, because of'."),
        mcq("discriminate", 3, "Which split of सौक्ष्म्याच्च in unit 83 is right?",
            ("सौक्ष्म्यात् + च", "त् before च becomes च्: सौक्ष्म्यात् + च → सौक्ष्म्याच्च."),
            [("सौक्ष्म्या + च्च", "च्च is not a word; the first च् comes from त्."),
             ("सौक्ष्म्याः + च", "आः before च would give सौक्ष्म्याश्च."),
             ("सौक्ष्म्यम् + च", "म् before च would give सौक्ष्म्यं च.")],
            "सौक्ष्म्यात् (from fineness) + च (and): त् + च → च्च.",
            "त् before च → च्."),
        multi("apply", 4, "Which does unit 83 state?",
              [("The three lie far from one another", "No: परस्परसन्निकर्ष is mutual proximity."),
               ("The three are truly one channel", "No: the non-distinction is only 'as it were' (इव)."),
               ("Their functions are distinct", "Right: विभक्तकर्मणाम्, of distinct functions."),
               ("The non-distinction is only apparent", "Right: अविभाग इव लक्ष्यते, seen as it were.")],
              [2, 3],
              "Their functions are distinct; they only seem undivided.",
              "विभक्तकर्मणामप्यविभाग इव लक्ष्यते."),
        mcq("transfer", 5, "By the rule of सौक्ष्म्यात् + च → सौक्ष्म्याच्च, how is तस्मात् + च joined in a new example?",
            ("तस्माच्च", "त् before च becomes च्, as सौक्ष्म्यात् + च → सौक्ष्म्याच्च."),
            [("तस्माद्च", "द् comes before a voiced sound; च is not voiced."),
             ("तस्मात्च", "त् does not stay before च; it becomes च्."),
             ("तस्माश्च", "श् comes from a visarga, not from त्.")],
            "तस्मात् + च = तस्माच्च, like सौक्ष्म्यात् + च = सौक्ष्म्याच्च.",
            "त् + च → च्च.",
            teaches="A final त् before च becomes च्: सौक्ष्म्यात् + च → सौक्ष्म्याच्च."),
    ],
}

# ---------------------------------------------------------------- unit 84
AUTHORED["84"] = {
    "title": "अपरे पुनराहुः",
    "question": "What does unit 84 say, and how is पुनराहुः formed?",
    "rule": ("Others (अपरे), again (पुनः), say (आहुः): the line opens a further view."),
    "limits": ("Prose, three words. What they say is not in this line (grouping note). Who the 'others' are is not said. "
               "आहुः is a perfect form (data), rendered 'they say'."),
    "explain_hi": ("यह तीन शब्दों की गद्य-पंक्ति है: दूसरे (अपरे) फिर (पुनः) कहते हैं (आहुः)। "
                   "यह एक और मत खोलती है; वह मत इस पंक्ति में नहीं, अगली छपी पंक्ति में है। "
                   "‘अपरे’ कौन हैं, पंक्ति नहीं बताती। "
                   "‘आहुः’ √अह् का परोक्ष भूत (perfect) रूप है, जिसका अनुवाद ‘कहते हैं’ है। "
                   "सन्धि: पुनः असल में पुनर् है; स्वर से पहले उसका र् दिखता है: पुनर् + आहुः → पुनराहुः।"),
    "hook": "अपरे पुनराहुः: और लोग फिर कहते हैं।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 84, what does आहुः mean?",
            ("They say", "आहुः = they say (√अह्)."),
            [("They saw", "Seeing would be from √दृश्, not आहुः."),
             ("They went", "Going would be from √गम्, not आहुः."),
             ("They ate", "Eating would be from √भुज्, not आहुः.")],
            "आहुः = they say.",
            "अपरे पुनराहुः: others again say."),
        match(1, "Match each word of unit 84 to its meaning.",
              [["अपरे", "others"], ["पुनः", "again"], ["आहुः", "they say"]],
              "Others, again, say.",
              "अपरे, पुनः, आहुः."),
        fill(2, "In unit 84 'again' is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("पुनः", None, "पुनर्", "punar", "puna"),
             "पुनः (again) stands for पुनर्; before a vowel the र् shows: पुनराहुः.",
             "पुनः = again; its र् shows before a vowel or a voiced sound.",
             "अपरे पुनः आहुः.", role="extend"),
        mcq("discriminate", 3, "Which split of पुनराहुः in unit 84 is right?",
            ("पुनः + आहुः", "पुनः stands for पुनर्; its र् shows before the vowel आ."),
            [("पुन + राहुः", "राहुः is not 'they say'; the र् belongs to पुनर्."),
             ("पुनम् + आहुः", "म् before a vowel would give पुनमाहुः."),
             ("पुनि + आहुः", "इ + आ would give पुन्याहुः.")],
            "पुनः (again) + आहुः (they say) → पुनराहुः.",
            "पुनः = पुनर्; र् shows before a vowel."),
        multi("apply", 4, "Which statements fit unit 84?",
              [("The line has no verb", "No: आहुः (they say) is the verb."),
               ("Others, again, say", "Right: अपरे पुनराहुः."),
               ("पुनः here means 'again'", "Right: पुनः = again."),
               ("The line names the others", "No names are given in unit 84.")],
              [1, 2],
              "Others, again, say; पुनः = again; the others are not named.",
              "अपरे पुनराहुः."),
        mcq("transfer", 5, "By the rule of पुनः + आहुः → पुनराहुः, how is पुनः + अपि (again too) joined?",
            ("पुनरपि", "पुनः stands for पुनर्; its र् shows before a vowel, as in पुनराहुः."),
            [("पुनोऽपि", "ओ comes from अः of an अस् ending; पुनः stands for पुनर्."),
             ("पुनपि", "The र् of पुनर् does not drop before a vowel."),
             ("पुनर्पि", "The अ of अपि does not vanish after र्.")],
            "पुनः + अपि = पुनरपि, like पुनः + आहुः = पुनराहुः.",
            "पुनः (= पुनर्) + vowel → पुनर् + vowel.",
            teaches="पुनः stands for पुनर्, whose र् shows before a vowel: पुनः + आहुः → पुनराहुः."),
    ],
}

# ---------------------------------------------------------------- unit 85
AUTHORED["85"] = {
    "title": "स्रोतांसि सिरा धमन्यो ... नामानीति",
    "question": "By unit 85, which names are given to the spaces of the dhātus in the body?",
    "rule": ("Srotas, sirā, dhamanī, carriers of rasa, nāḍī, paths, routes, ways, openings of the body (closed and open), "
             "places, seats (āśaya), abodes, dwellings: these are names (नामानि) of the spaces of the dhātus "
             "(धात्ववकाशानाम्), perceptible and imperceptible (लक्ष्यालक्ष्याणाम्)."),
    "limits": ("Prose; the view opened by unit 84. संवृतासंवृतानि (closed and open) is read with the openings of the body; "
               "it could also be a separate name, so the number of names is left open: no counting question. क्षयाः here "
               "means abodes. The closing इति ends the list of names."),
    "explain_hi": ("यह गद्य-पंक्ति इकाई ८४ में खुले मत को देती है: स्रोतस्, सिरा, धमनी, रसवाहिनी, नाड़ी, पन्थ, अयन, मार्ग, शरीर के छिद्र "
                   "(बन्द और खुले), स्थान, आशय, क्षय (निवास) और निकेत (आवास): ये सब शरीर में धातुओं के अवकाशों के नाम हैं। "
                   "ये अवकाश कुछ दिखाई देने वाले (लक्ष्य) और कुछ न दिखाई देने वाले (अलक्ष्य) हैं। "
                   "‘संवृतासंवृतानि’ (बन्द और खुले) डेटा में ‘शरीरच्छिद्राणि’ के साथ पढ़ा गया है, पर यह अलग नाम भी हो सकता है; इसलिए "
                   "नामों की गिनती खुली है। "
                   "यहाँ ‘क्षय’ का अर्थ निवास है, घटाव (कमी) नहीं।"),
    "hook": "स्रोतस् से निकेत तक: एक ही चीज़ के अनेक नाम, धातुओं के अवकाश।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 85, what are srotas, sirā, dhamanī and the rest?",
            ("Names of the spaces of the dhātus", "धात्ववकाशानां ... नामानि: names of the spaces of the dhātus."),
            [("Names of the kinds of the doṣas", "The doṣas are not the subject of unit 85."),
             ("Names of the seats of the agni", "Agni is not named in unit 85."),
             ("Names of the parts of the heart", "The heart is not named in unit 85.")],
            "All are names, in the body, of the spaces of the dhātus.",
            "शरीरे धात्ववकाशानां लक्ष्यालक्ष्याणां नामानीति."),
        order(1, "Put the first five names of unit 85 in the printed order.",
              ["स्रोतांसि", "सिरा", "धमन्यो", "रसवाहिन्यो", "नाड्यः"],
              "Srotas, sirā, dhamanī, carriers of rasa, nāḍī.",
              "स्रोतांसि → सिरा → धमन्यो → रसवाहिन्यो → नाड्यः."),
        match(2, "Match each word of unit 85 to its meaning.",
              [["संवृत", "closed"], ["असंवृत", "open"], ["लक्ष्य", "perceptible"], ["अलक्ष्य", "imperceptible"],
               ["अवकाश", "space"], ["छिद्र", "opening"]],
              "Openings closed and open; spaces perceptible and imperceptible.",
              "संवृत, असंवृत, लक्ष्य, अलक्ष्य, अवकाश, छिद्र.", role="extend",
              teaches="अ- before a word negates it: संवृत / असंवृत, लक्ष्य / अलक्ष्य."),
        mcq("discriminate", 3, "Which split of पंथानोऽयनानि in unit 85 is right?",
            ("पन्थानः + अयनानि", "अः before अ becomes ओ and the अ is elided (ऽ): पन्थानोऽयनानि."),
            [("पन्थानो + यनानि", "यनानि is not a word; the word is अयनानि (routes)."),
             ("पन्थानौ + अयनानि", "औ before a vowel would give पन्थानावयनानि."),
             ("पन्थाने + अयनानि", "ए before अ would give पन्थानेऽयनानि, with ए.")],
            "पन्थानः (paths) + अयनानि (routes): अः + अ → ओऽ.",
            "अः before अ → ओ, and the अ is elided (ऽ)."),
        multi("apply", 4, "Which are among the names listed in unit 85?",
              [("नाड्यः (nāḍī)", "Right: नाड्यः is in the list."),
               ("मर्माणि (marma)", "Marma is not in the list of unit 85."),
               ("कण्डराः (kaṇḍarā)", "Kaṇḍarā is not in the list of unit 85."),
               ("निकेताः (dwellings)", "Right: निकेताश्च, and dwellings.")],
              [0, 3],
              "Nāḍī and dwellings (निकेत) are among the names; marma and kaṇḍarā are not.",
              "...नाड्यः ... क्षया निकेताश्चेति."),
        mcq("transfer", 5, "By the rule of स्थानानि + आशयाः → स्थानान्याशयाः, how is अस्ति + आत्मा joined in a new example?",
            ("अस्त्यात्मा", "इ before a different vowel becomes य्, as स्थानानि + आशयाः → स्थानान्याशयाः."),
            [("अस्तात्मा", "The इ is not lost; it becomes य्."),
             ("अस्तीत्मा", "ई comes from इ + इ, not इ + आ."),
             ("अस्त्यत्मा", "The vowel after य् stays long: आ.")],
            "अस्ति + आत्मा = अस्त्यात्मा, like स्थानानि + आशयाः = स्थानान्याशयाः.",
            "इ + आ → या.",
            teaches="इ before a different vowel becomes य्: स्थानानि + आशयाः → स्थानान्याशयाः."),
    ],
}

# ---------------------------------------------------------------- unit 86
AUTHORED["86"] = {
    "title": "तेचावकाशाः",
    "question": "What does unit 86 name, and how is तेचावकाशाः split?",
    "rule": ("And these (ते च) spaces (अवकाशाः): the subject; the verb comes in the next line (grouping note)."),
    "limits": ("Prose, three words; no verb in this line (the sentence runs on into unit 87). ते (these) probably takes up "
               "the spaces of the dhātus of unit 85; the line itself does not say."),
    "explain_hi": ("यह तीन शब्दों की गद्य-पंक्ति है: और वे (ते च) अवकाश (अवकाशाः)। "
                   "यह वाक्य का कर्ता है; क्रिया इस पंक्ति में नहीं, वाक्य अगली इकाई ८७ में आगे चलता है। "
                   "‘ते’ सम्भवतः इकाई ८५ के धातु-अवकाशों की ओर संकेत करता है; पंक्ति स्वयं यह नहीं कहती। "
                   "‘अवकाशाः’ पुंलिंग प्रथमा बहुवचन है। "
                   "सन्धि: च + अवकाशाः → चावकाशाः (अ + अ → आ)।"),
    "hook": "ते च अवकाशाः: और वे अवकाश (आगे क्या करते हैं, अगली पंक्ति में)।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 86, what does अवकाशाः mean?",
            ("Spaces", "अवकाशाः = spaces (m. nom. pl.)."),
            [("Signs", "Signs would be लक्षणानि; अवकाश is space."),
             ("Roots", "Roots would be मूलानि; अवकाश is space."),
             ("Seasons", "Seasons would be ऋतवः; अवकाश is space.")],
            "अवकाशाः = spaces.",
            "ते च अवकाशाः."),
        match(1, "Match each word of unit 86 to its meaning.",
              [["ते", "these, they"], ["च", "and"], ["अवकाशाः", "spaces"]],
              "And these spaces.",
              "ते, च, अवकाशाः."),
        mcq("extend", 2, "In unit 86, what case and number is अवकाशाः?",
            ("Nominative plural", "-आः on a masculine अ-stem: nominative plural, the subject."),
            [("Accusative singular", "That would be अवकाशम्."),
             ("Genitive plural", "That would be अवकाशानाम्."),
             ("Locative singular", "That would be अवकाशे.")],
            "अवकाशाः = nominative plural: 'the spaces', the subject.",
            "Masculine अ-stem, nominative plural: -आः.",
            teaches="-आः on a masculine अ-stem marks the nominative plural: अवकाश → अवकाशाः."),
        mcq("discriminate", 3, "Which split of तेचावकाशाः in unit 86 is right?",
            ("ते + च + अवकाशाः", "अ + अ → आ: च + अवकाशाः → चावकाशाः."),
            [("ते + चा + वकाशाः", "वकाशाः is not a word; the word is अवकाशाः."),
             ("ते + च + आकाशाः", "आकाश is another word (sky); the print has व: चावकाशाः."),
             ("तेच + वकाशाः", "Neither तेच nor वकाशाः is a word here.")],
            "ते (these) + च (and) + अवकाशाः (spaces): अ + अ → आ.",
            "अ + अ → आ."),
        multi("apply", 4, "Which statements fit unit 86?",
              [("The line names spaces", "Right: अवकाशाः."),
               ("The line has a printed verb", "No verb is printed in unit 86."),
               ("अवकाशाः is singular", "-आः here is plural."),
               ("च means 'and'", "Right: ते च, and these.")],
              [0, 3],
              "The line names the spaces; च = and; no verb; plural.",
              "ते च अवकाशाः."),
        mcq("transfer", 5, "By the rule of च + अवकाशाः → चावकाशाः, how is न + अस्ति joined in a new example?",
            ("नास्ति", "अ + अ → आ, as च + अवकाशाः → चावकाशाः."),
            [("नेस्ति", "ए comes from अ + इ, not अ + अ."),
             ("नोस्ति", "ओ comes from अ + उ, not अ + अ."),
             ("नस्ति", "The two अ give a long आ, not a short अ.")],
            "न + अस्ति = नास्ति, like च + अवकाशाः = चावकाशाः.",
            "अ + अ → आ.",
            teaches="Two short अ merge into a long आ: च + अवकाशाः → चावकाशाः."),
    ],
}

# ---------------------------------------------------------------- unit 87
AUTHORED["87"] = {
    "title": "प्रकुपिताःस्थानस्थानमार्गस्थांश्च धातून्प्रकोपयंति",
    "question": "By unit 87, what do the agitated spaces do to the dhātus?",
    "rule": ("Agitated (प्रकुपिताः), they (the spaces of unit 86) agitate (प्रकोपयन्ति) the dhātus (धातून्): on the plainer "
             "reading, those standing in their seats and those on their paths."),
    "limits": ("Prose; the subject is in unit 86 (grouping note). The printed स्थानस्थानमार्गस्थान् is flagged: 'sthāna' "
               "may be repeated by a print slip, or it may read 'in place and not on their path': no question on how the "
               "repeated 'sthāna' is read; the closing ...स्थान् + च → ...स्थांश्च is the same under both readings. Which dhātus is not said."),
    "explain_hi": ("इकाई ८६ का वाक्य यहाँ पूरा होता है: वे अवकाश प्रकुपित होकर (प्रकुपिताः) धातुओं को प्रकुपित करते हैं (प्रकोपयन्ति)। "
                   "सरल पाठ में: अपने स्थान में स्थित और मार्ग में स्थित धातुओं को। "
                   "छपे ‘स्थानस्थानमार्गस्थान्’ में ‘स्थान’ दो बार है; यह छपाई की भूल हो सकती है, या ‘स्थान में स्थित, मार्ग में नहीं’ भी "
                   "पढ़ा जा सकता है; इसलिए इस पद पर कोई प्रश्न नहीं। "
                   "‘प्रकुपित’ और ‘प्रकोपयन्ति’ दोनों प्र-√कुप् से हैं: एक कृदन्त (प्रकुपित हुए), दूसरा णिजन्त (प्रकुपित करते हैं)।"),
    "hook": "खुद भड़के अवकाश, धातुओं को भी भड़काते हैं।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 87, what do the agitated ones do to the dhātus?",
            ("They agitate them", "धातून् प्रकोपयन्ति: they agitate the dhātus."),
            [("They nourish them", "Nourishing is not said; the verb is प्रकोपयन्ति."),
             ("They cleanse them", "Cleansing is not said; the verb is प्रकोपयन्ति."),
             ("They dry them up", "Drying is not said; the verb is प्रकोपयन्ति.")],
            "Agitated, they agitate the dhātus.",
            "प्रकुपिताः ... धातून् प्रकोपयन्ति."),
        match(1, "Match each word of unit 87 to its meaning.",
              [["प्रकुपिताः", "agitated"], ["धातून्", "the dhātus (tissues)"], ["प्रकोपयन्ति", "they agitate"],
               ["च", "and"]],
              "Agitated, they agitate the dhātus.",
              "प्रकुपिताः, धातून्, प्रकोपयन्ति, च."),
        mcq("extend", 2, "How are प्रकुपित and प्रकोपयन्ति related?",
            ("Both from प्र-√कुप्: 'agitated', 'they agitate'", "प्रकुपित is the past participle; प्रकोपयन्ति the causative."),
            [("Both are past participles of one root", "प्रकोपयन्ति is a present verb, not a participle."),
             ("Both are nouns that mean 'anger' itself", "Neither is a noun here: one participle, one verb."),
             ("They come from two different roots", "Both come from the one root √कुप् with प्र.")],
            "प्रकुपित = agitated; प्रकोपयन्ति = they make agitated: one root, two forms.",
            "√कुप् + प्र: प्रकुपित (ppp), प्रकोपयन्ति (causative).",
            teaches="प्रकुपित is the past participle (agitated); प्रकोपयन्ति is the causative present, 'they make agitated'."),
        mcq("discriminate", 3, "Which split of ...मार्गस्थांश्च in unit 87 is right?",
            ("...मार्गस्थान् + च", "न् before च becomes ंश्: ...स्थान् + च → ...स्थांश्च."),
            [("...मार्गस्थाः + च", "आः before च would give ...स्थाश्च, with no anusvāra."),
             ("...मार्गस्थाम् + च", "म् before च would give ...स्थां च, with no श्."),
             ("...मार्गस्थे + च", "ए stays before च: ...स्थे च.")],
            "...मार्गस्थान् (those on the paths, acc. pl.) + च: न् + च → ंश्च.",
            "न् before च → ंश्."),
        multi("apply", 4, "Which statements fit unit 87?",
              [("The line names which dhātus", "No dhātu is named."),
               ("The dhātus are the object of the verb", "Right: धातून्, accusative plural."),
               ("The verb is printed in this line", "Right: प्रकोपयन्ति."),
               ("प्रकुपिताः is accusative", "प्रकुपिताः is nominative plural, with the subject.")],
              [1, 2],
              "धातून् is the object of the printed verb प्रकोपयन्ति; no dhātu is named.",
              "प्रकुपिताः ... धातून् प्रकोपयन्ति."),
        mcq("transfer", 5, "By the rule of ...स्थान् + च → ...स्थांश्च, how is तान् + च joined in a new example?",
            ("तांश्च", "न् before च becomes ंश्, as ...स्थान् + च → ...स्थांश्च."),
            [("तान्च", "न् does not stay plain before च."),
             ("ताञ्च", "न् before च gives ंश्, not ञ्."),
             ("तानश्च", "No vowel is added; न् gives ंश्.")],
            "तान् + च = तांश्च, like ...स्थान् + च = ...स्थांश्च.",
            "न् + च → ंश्च.",
            teaches="A final न् before च becomes ंश्: मार्गस्थान् + च → मार्गस्थांश्च."),
    ],
}

# ---------------------------------------------------------------- unit 88
AUTHORED["88"] = {
    "title": "तेऽपि तान् स्रोतांसि च",
    "question": "What does unit 88 add, and which verb is understood?",
    "rule": ("They too (ते अपि) (agitate, carried from unit 87) those (तान्, the dhātus, understood) and the srotas "
             "(स्रोतांसि)."),
    "limits": ("Prose, elliptical: no verb printed; 'agitate' is carried from unit 87 (data). Who 'they' are is not "
               "printed: no question on it. तान् = those dhātus (understood, data)."),
    "explain_hi": ("यह गद्य-पंक्ति अधूरी है: वे भी (ते अपि) उन्हें (तान्) और स्रोतसों को (स्रोतांसि च)। "
                   "क्रिया छपी नहीं; इकाई ८७ की ‘प्रकोपयन्ति’ (प्रकुपित करते हैं) समझी जाती है। "
                   "डेटा के अनुसार ‘तान्’ = उन धातुओं को। "
                   "‘ते’ कौन हैं, यह छपा नहीं; इसलिए इस पर कोई प्रश्न नहीं। "
                   "सन्धि: ते + अपि → तेऽपि (ए के बाद अ लुप्त, ऽ चिह्न)।"),
    "hook": "वे भी उन्हें और स्रोतसों को भड़काते हैं।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 88, which verb is understood from unit 87?",
            ("Agitate", "The data carries प्रकोपयन्ति (they agitate) from unit 87."),
            [("Nourish", "No nourishing verb is in unit 87."),
             ("Carry", "The verb of unit 87 is प्रकोपयन्ति, not 'carry'."),
             ("Cleanse", "No cleansing verb is in unit 87.")],
            "They too (agitate) those and the srotas.",
            "तेऽपि तान् स्रोतांसि च (प्रकोपयन्ति)."),
        match(1, "Match each word of unit 88 to its meaning.",
              [["ते", "they"], ["अपि", "also, too"], ["तान्", "those (m. acc. pl.)"], ["स्रोतांसि", "the srotas, channels"]],
              "They too (agitate) those and the srotas.",
              "ते, अपि, तान्, स्रोतांसि."),
        fill(2, "In unit 88 the word for too or also is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("अपि"),
             "अपि = also, too; printed तेऽपि with its अ elided after ए.",
             "अपि = also; after ए its अ is elided (ऽ).",
             "ते + अपि → तेऽपि.", role="extend"),
        mcq("discriminate", 3, "Which split of तेऽपि in unit 88 is right?",
            ("ते + अपि", "ए before अ stays, and the अ is elided (ऽ): तेऽपि."),
            [("ते + पि", "पि is not a word; ऽ marks a lost अ."),
             ("तौ + अपि", "औ before a vowel would give तावपि."),
             ("तम् + अपि", "म् before a vowel would give तमपि.")],
            "ते (they) + अपि (too): ए + अ → एऽ.",
            "ए + अ → एऽ (अ elided)."),
        multi("apply", 4, "Which are printed in unit 88?",
              [("A verb", "No verb is printed; 'agitate' is understood."),
               ("The word for the srotas", "Right: स्रोतांसि."),
               ("A word for 'those'", "Right: तान्."),
               ("The word दोष", "No doṣa is named in unit 88.")],
              [1, 2],
              "स्रोतांसि and तान् are printed; the verb is understood.",
              "तेऽपि तान् स्रोतांसि च."),
        mcq("transfer", 5, "By the rule of ते + अपि → तेऽपि, how is वने + अस्मिन् joined in a new example?",
            ("वनेऽस्मिन्", "ए before अ stays and the अ is elided, as ते + अपि → तेऽपि."),
            [("वनास्मिन्", "आ comes from अ + अ; here ए meets अ."),
             ("वनयस्मिन्", "अय् comes from ए before vowels other than अ."),
             ("वनोऽस्मिन्", "ओ comes from अः, not from ए.")],
            "वने + अस्मिन् = वनेऽस्मिन्, like ते + अपि = तेऽपि.",
            "ए + अ → एऽ.",
            teaches="ए before अ stays, and the अ is elided (marked ऽ): ते + अपि → तेऽपि."),
    ],
}

# ---------------------------------------------------------------- unit 89
AUTHORED["89"] = {
    "title": "स्रोतांसि धातवश्च धातून्",
    "question": "By unit 89, what do the srotas and the dhātus (agitate)?",
    "rule": ("The srotas (स्रोतांसि) and the dhātus (धातवः) (agitate, carried from unit 87) the dhātus (धातून्)."),
    "limits": ("Prose, elliptical: no verb printed; 'agitate' is carried from unit 87 (data). Which dhātus is not said."),
    "explain_hi": ("यह गद्य-पंक्ति भी अधूरी है: स्रोतस् और धातु धातुओं को। "
                   "क्रिया छपी नहीं; इकाई ८७ की ‘प्रकोपयन्ति’ (प्रकुपित करते हैं) समझी जाती है। "
                   "एक ही शब्द धातु दो रूपों में है: ‘धातवः’ प्रथमा बहुवचन (कर्ता) और ‘धातून्’ द्वितीया बहुवचन (कर्म)। "
                   "इकाई ८६-८९ मिलकर प्रकोप की एक कड़ी बनाती हैं: प्रकुपित अवकाश धातुओं को प्रकुपित करते हैं; फिर स्रोतस् और धातु भी धातुओं को (क्रिया इकाई ८७ से समझी)। "
                   "सन्धि: धातवः + च → धातवश्च (च से पहले विसर्ग → श्)।"),
    "hook": "स्रोतस् और धातु, धातुओं को भड़काते हैं।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 89, what do the srotas and the dhātus (agitate)?",
            ("The dhātus", "धातून्: the dhātus (acc. pl.)."),
            [("The doṣas", "No doṣa is named in unit 89."),
             ("The malas", "No mala is named in unit 89."),
             ("The senses", "No sense organ is named in unit 89.")],
            "The srotas and the dhātus (agitate) the dhātus.",
            "स्रोतांसि धातवश्च धातून्."),
        order(1, "Put the words of unit 89 in the printed order.",
              ["स्रोतांसि", "धातवश्च", "धातून्"],
              "The srotas, and the dhātus, (agitate) the dhātus.",
              "स्रोतांसि → धातवश्च → धातून्."),
        match(2, "Match each form in unit 89 to its meaning.",
              [["धातवः", "the dhātus (subject, nom. pl.)"], ["धातून्", "the dhātus (object, acc. pl.)"],
               ["स्रोतांसि", "the srotas"], ["च", "and"]],
              "The srotas and the dhātus (agitate) the dhātus.",
              "धातवः, धातून्, स्रोतांसि, च.", role="extend",
              teaches="धातु: -अवः marks the nominative plural (subject), -ऊन् the accusative plural (object)."),
        mcq("discriminate", 3, "Which form of धातु in unit 89 is the accusative plural (the object)?",
            ("धातून्", "-ऊन्: accusative plural of the masculine उ-stem."),
            [("धातवः", "धातवः is the nominative plural, the subject."),
             ("धातूनाम्", "धातूनाम् is the genitive plural, and not printed here."),
             ("धातौ", "धातौ is the locative singular, and not printed here.")],
            "धातून् = the dhātus as object; धातवः = the dhātus as subject.",
            "Masculine उ-stem: nom. pl. -अवः, acc. pl. -ऊन्."),
        mcq("apply", 4, "Which split of धातवश्च in unit 89 is right?",
            ("धातवः + च", "A visarga before च becomes श्: धातवश्च."),
            [("धातवम् + च", "म् before च would give धातवं च."),
             ("धातवे + च", "ए stays before च: धातवे च."),
             ("धातवत् + च", "त् before च would give धातवच्च.")],
            "धातवः (the dhātus) + च (and): visarga before च → श्.",
            "Visarga before च → श्."),
        mcq("transfer", 5, "By the rule of धातवः + च → धातवश्च, how is वृक्षाः + च joined in a new example?",
            ("वृक्षाश्च", "A visarga before च becomes श्, as धातवः + च → धातवश्च."),
            [("वृक्षा च", "The visarga after आ drops before a voiced sound; च is not voiced."),
             ("वृक्षास्च", "स् comes before त or थ, not before च."),
             ("वृक्षोच", "ओ comes from अः before a voiced consonant, not from आः.")],
            "वृक्षाः + च = वृक्षाश्च, like धातवः + च = धातवश्च.",
            "Visarga + च → श्च.",
            teaches="A visarga before च becomes श्: धातवः + च → धातवश्च."),
    ],
}

# ---------------------------------------------------------------- unit 90
AUTHORED["90"] = {
    "title": "तेषां सर्वेषामैव दूषयितारो दुष्टा दोषाः",
    "question": "By unit 90, what vitiates all these?",
    "rule": ("The vitiators (दूषयितारः) of all these (तेषां सर्वेषाम्) indeed are the vitiated (दुष्टाः) doṣas (दोषाः)."),
    "limits": ("Prose; the copula is understood. The printed सर्वेषामैव is flagged: read सर्वेषाम् एव ('ai' a print slip), "
               "or perhaps सर्वेषां चैव: no question on how that word is read "
               "(the order question uses only its printed position). 'All these' are not named in the line, and the doṣas "
               "are not named one by one."),
    "explain_hi": ("यह गद्य-पंक्ति कहती है: इन सबके ही दूषित करने वाले (दूषयितारः) दूषित (दुष्टाः) दोष हैं। "
                   "यानी जो दोष स्वयं बिगड़े हुए हैं, वही इन सबको बिगाड़ते हैं। "
                   "‘इन सब’ में कौन हैं, पंक्ति में नहीं गिनाया; दोषों के नाम भी अलग-अलग नहीं दिए। "
                   "छपा ‘सर्वेषामैव’ ठीक सन्धि नहीं बनता (म् + एव से ‘मेव’ होता); डेटा ‘सर्वेषाम् एव’ पढ़ता है, ‘सर्वेषां चैव’ भी सम्भव है। "
                   "‘दुष्ट’ और ‘दूषयितृ’ दोनों √दुष् से हैं।"),
    "hook": "बिगड़े दोष ही सबको बिगाड़ते हैं।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 90, what are the vitiators of all these?",
            ("The vitiated doṣas", "दूषयितारो दुष्टा दोषाः: the vitiated doṣas."),
            [("The changing seasons", "Seasons are not named in unit 90."),
             ("The pierced srotas", "Pierced srotas are not named in unit 90."),
             ("The organs of sense", "Sense organs are not named in unit 90.")],
            "The vitiators of all these are the vitiated doṣas.",
            "तेषां सर्वेषाम् एव दूषयितारो दुष्टा दोषाः."),
        order(1, "Put the words of unit 90 in the printed order.",
              ["तेषां", "सर्वेषामैव", "दूषयितारो", "दुष्टा", "दोषाः"],
              "Of these, of all indeed, the vitiators, vitiated, the doṣas.",
              "तेषां → सर्वेषामैव → दूषयितारो → दुष्टा → दोषाः."),
        match(2, "Match each word of unit 90 to its meaning.",
              [["तेषाम्", "of these"], ["सर्वेषाम्", "of all"], ["दूषयितारः", "vitiators"], ["दुष्टाः", "vitiated"],
               ["दोषाः", "the doṣas"]],
              "Of all these, the vitiators are the vitiated doṣas.",
              "तेषाम्, सर्वेषाम्, दूषयितारः, दुष्टाः, दोषाः.", role="extend",
              teaches="दुष्ट (vitiated) and दूषयितृ (vitiator) both come from √दुष्: the doṣas are spoiled and they spoil."),
        mcq("discriminate", 3, "Which split of दूषयितारो दुष्टा in unit 90 is right?",
            ("दूषयितारः + दुष्टाः", "अः before the voiced द becomes ओ: दूषयितारो दुष्टाः."),
            [("दूषयितारौ + दुष्टाः", "औ stays औ before a consonant; the print has ओ."),
             ("दूषयितारम् + दुष्टाः", "म् before द would be written ं: दूषयितारं."),
             ("दूषयितारे + दुष्टाः", "ए stays ए before a consonant; the print has ओ.")],
            "दूषयितारः (vitiators) + दुष्टाः (vitiated): अः + voiced consonant → ओ.",
            "अः before a voiced consonant → ओ."),
        multi("apply", 4, "Which statements fit unit 90?",
              [("The doṣas are named one by one", "No: only दोषाः, with no names."),
               ("The line has a printed verb", "No: the copula is understood."),
               ("The doṣas are called the vitiators", "Right: दूषयितारो ... दोषाः."),
               ("The vitiating doṣas are themselves vitiated", "Right: दुष्टाः दोषाः.")],
              [2, 3],
              "The vitiated doṣas are the vitiators; no names and no verb are printed.",
              "दूषयितारो दुष्टा दोषाः."),
        mcq("transfer", 5, "By the rule of दूषयितारः + दुष्टाः → दूषयितारो दुष्टाः, how is बालः + गच्छति joined in a new example?",
            ("बालो गच्छति", "अः before a voiced consonant becomes ओ, as दूषयितारः + दुष्टाः → दूषयितारो दुष्टाः."),
            [("बालर् गच्छति", "र् comes from a visarga after vowels other than अ or आ."),
             ("बालस् गच्छति", "स् comes before त or थ, not before ग."),
             ("बालश् गच्छति", "श् comes before च, छ or श, not before ग.")],
            "बालः + गच्छति = बालो गच्छति, like दूषयितारः + दुष्टाः = दूषयितारो दुष्टाः.",
            "अः + voiced consonant → ओ.",
            teaches="अः before a voiced consonant becomes ओ: दूषयितारः + दुष्टाः → दूषयितारो दुष्टाः."),
    ],
}


# ===================================================================== NOTES_HI
NOTES_HI = {
    "78": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। वाक्य-रचना ढीली (डेटा): ‘दोषादिविज्ञानीयात्’ = दोषादि + विज्ञानीयात्; ‘दोष आदि से "
           "जानना’ सरल पाठ है, ‘दोष आदि को जानना’ विकल्प; यह रूप ‘दोषादिविज्ञानीय’ नाम के अध्याय का पञ्चमी रूप भी हो सकता है (वि-√ज्ञा का विधिलिङ् सामान्यतः विजानीयात् होता है); इस पर कोई प्रश्न नहीं। ‘विविधम्’ दूषण के साथ या आहार-विहार के साथ, "
           "दोनों पढ़े जा सकते हैं। ‘यथास्वम्’ अन्तिम क्रिया के साथ लिया गया। सन्धि जाँची: विज्ञानीयात् + यथास्वम् → "
           "विज्ञानीयाद्यथास्वम् (घोष य से पहले त् → द्); विविधम् + अहित → विविधमहित (स्वर से पहले म्); अहित + आहार → अहिताहार "
           "(अ + आ → आ); विहारम् + उपद्रवान् → विहारमुपद्रवान्।"),
    "79": ("गद्य; विश्वास कम (क्षतिग्रस्त छपाई)। पाठ-चिह्न (सम्भावित): ‘...ज्वरानिरुधिरश्रुति...’ में ‘अनि’ का अर्थ नहीं बनता; "
           "‘ज्वररुधिरश्रुति’ सुझाया गया; रुधिरश्रुति = रक्त का बहना, केवल अनुमानित पाठ; ‘अनि’ अस्पष्ट छोड़ा गया; इस अंश पर कोई प्रश्न "
           "नहीं। मोह = मूर्छा या भ्रान्ति। क्रिया नहीं, ‘होते हैं’ समझा जाता है। स्रोतस् शास्त्रीय शब्द (शरीर की नलिका) रखा गया। "
           "सन्धि जाँची: प्रलाप + आध्मान → प्रलापाध्मान (अ + आ → आ); शूल + अरुचि → शूलारुचि (अ + अ → आ); रोधाः + मरणम् → रोधा "
           "मरणं (घोष म से पहले आः का विसर्ग लुप्त); छपा कंप = कम्प।"),
    "80": ("गद्य; विश्वास मध्यम; दो छपी पंक्तियाँ (०२.०६.८९, ०२.०६.९०)। पाठ-चिह्न (सम्भावित): छपा ‘स्रोतौविद्धं’; स्रोतस् + विद्ध से "
           "‘स्रोतोविद्धम्’ बनता है, ‘औ’ छपाई की भूल लगती है; दूसरा सुझाव ‘स्रोतसि विद्धम्’ (अर्थ वही); इस रूप पर कोई प्रश्न नहीं। "
           "‘प्रत्याख्याय’ = अस्वीकार करके (रोग को असाध्य कहकर); फिर उपचार करना, जैसा छपा। दूसरी पंक्ति में क्रिया नहीं, पहली की "
           "‘उपाचरेत्’ समझी जाती है; समूह-टिप्पणी: दूसरी छपी पंक्ति (०२.०६.९०) पहली (०२.०६.८९) को आगे बढ़ाती दिखती है; दोनों इसी इकाई ८० में। सन्धि जाँची: प्रत्याख्याय + उपाचरेत् → "
           "प्रत्याख्यायोपाचरेत् (अ + उ → ओ); सद्यः + व्रण → सद्योव्रण (अः + घोष व्यंजन → ओ); तस्मात् + स्रो... में स से पहले त् अपरिवर्तित।"),
    "81": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। सिरा = वाहिका, सम्भवतः शिरा; धमनी = स्पन्दन वाली वाहिका, सम्भवतः धमनी; दोनों "
           "आधुनिक पहचान सम्भावित, सटीक नहीं। क्रिया ‘हैं’ समझी जाती है। छपा ‘सिरा’ = सिराः (बहुवचन, धमन्यः की तरह); घोष ध से पहले "
           "आः का विसर्ग लुप्त, नियमित सन्धि। सन्धि जाँची: स्रोतसाम् + एव → स्रोतसामेव (स्वर से पहले म्); छपाई में ‘एवविशेषाः’ जुड़ा।"),
    "82": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। क्या किससे भिन्न है, यह छपा नहीं; डेटा सिरा, धमनी और स्रोतस् को समझता है। ‘अन्ये’ "
           "कौन हैं, नहीं बताया। सन्धि जाँची: अन्ये + तु (व्यंजन से पहले ए अपरिवर्तित, छपाई में जुड़ा); तु + अन्यत्वम् → त्वन्यत्वम् "
           "(उ + भिन्न स्वर → व्); अन्यत्वम् + इच्छन्ति → अन्यत्वमिच्छन्ति (स्वर से पहले म्); छपा इच्छंति = इच्छन्ति।"),
    "83": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। छपा ‘अविभागइव’ = अविभागः + इव: अः के बाद अ से भिन्न स्वर आने पर विसर्ग लुप्त होकर "
           "अ रहता है और आगे सन्धि नहीं होती (अविभाग इव); देवनागरी में स्वर अलग छपे हैं, केवल जगह छूटी। ‘केवलम्’ तीनों कारणों के "
           "साथ लिया गया। यह एक मत का कथन है (देखें इकाई ८२, ८४)। सन्धि जाँची: सौक्ष्म्यात् + च → सौक्ष्म्याच्च (च से पहले त् → च्); "
           "सन्निकर्षात् + सदृश (स से पहले त् अपरिवर्तित); विभक्तकर्मणाम् + अपि → ...कर्मणामपि (स्वर से पहले म्); अपि + अविभागः → "
           "अप्यविभागः (इ + भिन्न स्वर → य्)।"),
    "84": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। समूह-टिप्पणी: यह अगला मत खोलती है; कहा गया मत अगली छपी पंक्ति (इकाई ८५) में है। "
           "आहुः = √अह्, डेटा में परोक्ष भूत (perfect) का रूप, अनुवाद ‘कहते हैं’। सन्धि जाँची: पुनः (= पुनर्) + आहुः → पुनराहुः "
           "(स्वर से पहले र्)।"),
    "85": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। ‘संवृतासंवृतानि’ (बन्द और खुले) ‘शरीरच्छिद्राणि’ के साथ पढ़ा गया; यह सूची का अलग "
           "नाम भी हो सकता है, इसलिए गिनती पर कोई प्रश्न नहीं। रसवाहिन्यः = रस को वहन करने वाली (स्त्रीलिंग बहुवचन, वाहिकाएँ)। क्षयाः = "
           "निवास। अन्त का ‘इति’ नामों की सूची बन्द करता है। सन्धि जाँची: धमन्यः + रस... → धमन्यो रस... और रसवाहिन्यः + नाड्यः → "
           "रसवाहिन्यो नाड्यः (अः + घोष व्यंजन → ओ); पन्थानः + अयनानि → पन्थानोऽयनानि (अः + अ → ओऽ); स्थानानि + आशयाः → "
           "स्थानान्याशयाः (इ + भिन्न स्वर → य्); क्षयाः + निकेताः → क्षया निकेताः (घोष से पहले आः का विसर्ग लुप्त); निकेताः + च → "
           "निकेताश्च; च + इति → चेति (अ + इ → ए); धातु + अवकाश → धात्ववकाश (उ + अ → व); लक्ष्य + अलक्ष्य → लक्ष्यालक्ष्य; संवृत + "
           "असंवृत → संवृतासंवृत (अ + अ → आ); नामानि + इति → नामानीति (इ + इ → ई); छपा पंथानो = पन्थानः।"),
    "86": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। समूह-टिप्पणी: यह इकाई ८७ का कर्ता है; क्रिया अगली पंक्ति में। ‘ते’ सम्भवतः इकाई ८५ "
           "के धातु-अवकाश; पंक्ति स्वयं नहीं कहती। सन्धि जाँची: ते + च (व्यंजन से पहले ए अपरिवर्तित); च + अवकाशाः → चावकाशाः "
           "(अ + अ → आ)।"),
    "87": ("गद्य; विश्वास मध्यम। पाठ-चिह्न (सम्भावित): छपे ‘स्थानस्थानमार्गस्थान्’ में ‘स्थान’ दो बार; सरल पाठ स्थानस्थान् + मार्गस्थान् "
           "(स्थान में स्थित और मार्ग में स्थित), ‘स्थान’ की पुनरावृत्ति छपाई की भूल हो सकती है; विकल्प स्थानस्थान् + अमार्गस्थान् (स्थान "
           "में, मार्ग में नहीं), जो छपाई को ज्यों-का-त्यों रखता है; इस पद पर कोई प्रश्न नहीं। कर्ता इकाई ८६ में। छपा ‘प्रकुपिताःस्थान’: "
           "स से पहले विसर्ग रखना या स् करना, दोनों मान्य। सन्धि जाँची: ...स्थान् + च → ...स्थांश्च (च से पहले न् → ंश्); धातून् + "
           "प्रकोपयन्ति (अपरिवर्तित, छपाई में जुड़ा); छपा प्रकोपयंति = प्रकोपयन्ति।"),
    "88": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। अधूरा वाक्य: क्रिया ‘प्रकुपित करते हैं’ पंक्ति ९७ (इकाई ८७) से समझी जाती है। "
           "‘तान्’ = उन धातुओं को (समझा गया)। ‘ते’ कौन, छपा नहीं। सन्धि जाँची: ते + अपि → तेऽपि (ए + अ → ए, अ का लोप, ऽ)।"),
    "89": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। अधूरा वाक्य: क्रिया ‘प्रकुपित करते हैं’ पंक्ति ९७ (इकाई ८७) से समझी जाती है। "
           "धातवः प्रथमा बहुवचन, धातून् द्वितीया बहुवचन। सन्धि जाँची: धातवः + च → धातवश्च (च से पहले विसर्ग → श्)।"),
    "90": ("गद्य; विश्वास मध्यम। पाठ-चिह्न (सम्भावित): छपा ‘सर्वेषामैव’; -म् + एव से ‘मेव’ बनता है, ‘ऐ’ नहीं; ‘सर्वेषाम् एव’ पढ़ा गया, "
           "‘ऐ’ छपाई की भूल; विकल्प ‘सर्वेषां चैव’ (च छूटा); इस शब्द पर कोई प्रश्न नहीं। क्रिया ‘हैं’ समझी जाती है। सन्धि जाँची: "
           "दूषयितारः + दुष्टाः → दूषयितारो दुष्टाः (अः + घोष व्यंजन → ओ); दुष्टाः + दोषाः → दुष्टा दोषाः (घोष से पहले आः का विसर्ग "
           "लुप्त)।"),
}


# ===================================================================== AIDS
AIDS = {
    "78": {
        "diagram": {"groups": [
            {"label": "तेषाम्: जानने योग्य, छपे क्रम में", "items": ["१ दूषण (बिगाड़)", "२ अहित आहार-विहार",
                                                             "३ उपद्रव", "४ साधन (चिकित्सा)"]},
            {"label": "पहचान", "items": ["यथास्वम्: हर एक अपने अनुसार", "वृद्धि और क्षय के लक्षण से"]}]},
        "chunks": "तेषां दूषणं | विविधमहिताहारविहारमुपद्रवान् | साधनं च | दोषादिविज्ञानीयाद्यथास्वं | वृद्धिक्षयलक्षणेन लक्षयेत्",
        "sandhi": ("घोष य से पहले त् → द्: विज्ञानीयात् + यथास्वम् → विज्ञानीयाद्यथास्वम् · अ + आ → आ: अहित + आहार → अहिताहार · "
                   "स्वर से पहले म्: विविधम् + अहित → विविधमहित।"),
        "letters": "चार बातें क्रम से: दू-अ-उ-सा (दूषण, अहित आहार-विहार, उपद्रव, साधन)। (मेरी याद-पद्धति)",
    },
    "79": {
        "diagram": {"groups": [
            {"label": "स्रोतस्-वेध के परिणाम, छपे क्रम में (१-१०)", "items": ["१ भ्रम (चक्कर)", "२ मोह (मूर्छा या भ्रान्ति)",
                                                                       "३ कम्प", "४ प्रलाप", "५ आध्मान (पेट फूलना)",
                                                                       "६ शूल", "७ अरुचि", "८ तृष् (प्यास)",
                                                                       "९ छर्दि (वमन)", "१० ज्वर"]},
            {"label": "आगे", "items": ["अस्पष्ट अंश (अनुमानित: रुधिरश्रुति, रक्त बहना)", "मूत्र-पुरीष-रोध",
                                      "मरण (मृत्यु)"]}]},
        "chunks": "व्यधे तु स्रोतसां | भ्रममोहकंप | प्रलापाध्मानशूलारुचि | तृच्छर्दिज्वरानिरुधिरश्रुति | मूत्रपुरीषरोधा | मरणं च",
        "sandhi": ("अ + आ → आ: प्रलाप + आध्मान → प्रलापाध्मान · अ + अ → आ: शूल + अरुचि → शूलारुचि · घोष से पहले आः का विसर्ग लुप्त: "
                   "रोधाः + मरणम् → रोधा मरणं।"),
        "frame": "कब: व्यधे (वेध होने पर) → किसके: स्रोतसाम् → क्या: लम्बी सूची, अन्त में मरणं च।",
    },
    "80": {
        "contrast": {"groups": [
            {"label": "स्रोतस् में विद्ध (पंक्ति १)", "items": ["प्रत्याख्याय: अस्वीकार करके (असाध्य कहकर)",
                                                          "उपाचरेत्: उपचार करे"]},
            {"label": "उद्धृतशल्य (पंक्ति २)", "items": ["शल्य निकाला जा चुका", "सद्योव्रण की विधि से",
                                                       "क्रिया पंक्ति १ से समझी"]}]},
        "chunks": "तस्मात्स्रोतौविद्धं | प्रत्याख्यायोपाचरेत् || उद्धृतशल्यं च | सद्योव्रणविधानेन",
        "sandhi": ("अ + उ → ओ: प्रत्याख्याय + उपाचरेत् → प्रत्याख्यायोपाचरेत् · अः + घोष व्यंजन → ओ: सद्यः + व्रण → सद्योव्रण।"),
        "frame": "क्यों: तस्मात् (इसलिए) → किसे: स्रोतस् में विद्ध को → कैसे: प्रत्याख्याय, फिर उपाचरेत्।",
    },
    "81": {
        "diagram": {"groups": [
            {"label": "स्रोतसामेव विशेषाः (स्रोतसों के ही विशेष रूप)", "items": ["सिरा (वाहिका, सम्भवतः शिरा)",
                                                                           "धमनी (स्पन्दन वाली, सम्भवतः धमनी)"]}]},
        "chunks": "तत्र | स्रोतसामेवविशेषाः | सिरा धमन्यः",
        "sandhi": "स्वर से पहले म्: स्रोतसाम् + एव → स्रोतसामेव · घोष ध से पहले आः का विसर्ग लुप्त: सिराः + धमन्यः → सिरा धमन्यः।",
    },
    "82": {
        "sandhi": ("उ + भिन्न स्वर → व्: तु + अन्यत्वम् → त्वन्यत्वम् · स्वर से पहले म्: अन्यत्वम् + इच्छन्ति → अन्यत्वमिच्छन्ति।"),
        "frame": "कौन: अन्ये (दूसरे) → तु (परन्तु) → क्या मानते: अन्यत्वम् (भिन्नता) → इच्छन्ति (मानते हैं)।",
        "anchors": "अन्य = दूसरा; अन्यत्व = दूसरापन, जैसे हिन्दी ‘अन्यथा’ में ‘अन्य’। (मेरी याद-पद्धति, शब्द-साम्य पर)",
    },
    "83": {
        "diagram": {"groups": [
            {"label": "तीन कारण (पञ्चमी -आत्), छपे क्रम में", "items": ["१ परस्परसन्निकर्ष (पास-पास होना)",
                                                                  "२ सदृशकर्मत्व (मिलता काम)",
                                                                  "३ सौक्ष्म्य (सूक्ष्मता)"]},
            {"label": "फल", "items": ["विभक्त कर्म होते हुए भी", "अविभाग इव लक्ष्यते: मानो अभेद दिखता है"]}]},
        "seesaw": "विभक्तकर्मणाम् (कर्म भिन्न) ↔ अविभाग इव (मानो अभेद): काम अलग, फिर भी एक-से दिखते हैं।",
        "chunks": "सिराधमनीस्रोतसां केवलं | परस्परसन्निकर्षात् | सदृशकर्मत्वात् | सौक्ष्म्याच्च | विभक्तकर्मणामप्यविभागइव | लक्ष्यते",
        "sandhi": ("च से पहले त् → च्: सौक्ष्म्यात् + च → सौक्ष्म्याच्च · इ + भिन्न स्वर → य्: अपि + अविभागः → अप्यविभागः · "
                   "अः + अ से भिन्न स्वर → अ: अविभागः + इव → अविभाग इव।"),
    },
    "84": {
        "chunks": "अपरे | पुनराहुः",
        "sandhi": "पुनः असल में पुनर्: स्वर से पहले र् दिखता है: पुनः + आहुः → पुनराहुः।",
        "frame": "कौन: अपरे (दूसरे) → पुनः (फिर) → क्या करते: आहुः (कहते हैं); मत अगली पंक्ति में।",
    },
    "85": {
        "diagram": {"groups": [
            {"label": "नाम, छपे क्रम में (भाग १)", "items": ["स्रोतांसि", "सिराः", "धमन्यः", "रसवाहिन्यः", "नाड्यः",
                                                         "पन्थानः", "अयनानि"]},
            {"label": "नाम, छपे क्रम में (भाग २)", "items": ["मार्गाः", "शरीरच्छिद्राणि", "संवृतासंवृतानि (छिद्रों के साथ, या अलग नाम)",
                                                         "स्थानानि", "आशयाः", "क्षयाः (निवास)", "निकेताः"]}]},
        "seesaw": "लक्ष्य (दिखने वाले) ↔ अलक्ष्य (न दिखने वाले); संवृत (बन्द) ↔ असंवृत (खुले): दोनों जोड़े इसी पंक्ति में।",
        "chunks": ("स्रोतांसि सिरा धमन्यो रसवाहिन्यो नाड्यः | पंथानोऽयनानि मार्गाः | शरीरच्छिद्राणि संवृतासंवृतानि | "
                   "स्थानान्याशयाः क्षया निकेताश्चेति | शरीरे धात्ववकाशानां लक्ष्यालक्ष्याणां नामानीति"),
        "sandhi": ("अः + घोष व्यंजन → ओ: धमन्यः + रस... → धमन्यो रस... · अः + अ → ओऽ: पन्थानः + अयनानि → पन्थानोऽयनानि · इ + आ → या: "
                   "स्थानानि + आशयाः → स्थानान्याशयाः · उ + अ → व: धातु + अवकाश → धात्ववकाश।"),
        "frame": "क्या: अनेक नाम (गिनती खुली) → किसके नाम: शरीरे धातु-अवकाशों के → कैसे अवकाश: लक्ष्य और अलक्ष्य।",
    },
    "86": {
        "chunks": "तेचावकाशाः",
        "sandhi": "अ + अ → आ: च + अवकाशाः → चावकाशाः।",
        "frame": "कौन: ते च अवकाशाः (और वे अवकाश) → क्रिया: अगली पंक्ति (इकाई ८७) में।",
    },
    "87": {
        "chain": {"steps": ["ते च अवकाशाः (इकाई ८६)", "प्रकुपिताः: स्वयं प्रकुपित होकर",
                            "स्थानस्थ और मार्गस्थ धातुओं को (सरल पाठ)", "प्रकोपयन्ति: प्रकुपित करते हैं"]},
        "chunks": "प्रकुपिताःस्थानस्थानमार्गस्थांश्च | धातून्प्रकोपयंति",
        "sandhi": "च से पहले न् → ंश्: ...मार्गस्थान् + च → ...मार्गस्थांश्च।",
        "frame": "कौन: अवकाश (इकाई ८६) → कैसे: प्रकुपिताः → किसे: धातून् → क्या करते: प्रकोपयन्ति।",
    },
    "88": {
        "chunks": "तेऽपि | तान् | स्रोतांसि च",
        "sandhi": "ए + अ → एऽ: ते + अपि → तेऽपि।",
        "frame": "कौन: ते अपि (वे भी) → किसे: तान् (उन धातुओं को) और स्रोतांसि → क्रिया: प्रकोपयन्ति, इकाई ८७ से समझी।",
    },
    "89": {
        "chain": {"steps": ["८६: ते च अवकाशाः (वे अवकाश)", "८७: प्रकुपित होकर धातुओं को प्रकुपित करते हैं",
                            "८८: ते अपि: वे भी उन्हें और स्रोतसों को", "८९: स्रोतस् और धातु, धातुओं को"]},
        "chunks": "स्रोतांसि | धातवश्च | धातून्",
        "sandhi": "च से पहले विसर्ग → श्: धातवः + च → धातवश्च।",
        "contrast": "धातवः (प्रथमा, कर्ता: धातु प्रकुपित करते हैं) ↔ धातून् (द्वितीया, कर्म: धातुओं को)।",
    },
    "90": {
        "frame": "किनके: तेषां सर्वेषाम् (इन सबके) → कौन: दूषयितारः (बिगाड़ने वाले) → क्या: दुष्टाः दोषाः (बिगड़े दोष)।",
        "chunks": "तेषां | सर्वेषामैव | दूषयितारो | दुष्टा दोषाः",
        "sandhi": "अः + घोष व्यंजन → ओ: दूषयितारः + दुष्टाः → दूषयितारो दुष्टाः · घोष से पहले आः का विसर्ग लुप्त: दुष्टाः + दोषाः → दुष्टा दोषाः।",
        "anchors": "दुष्ट, दूषण, दूषयिता, दोष: सब एक धातु-परिवार (√दुष्, बिगड़ना) के शब्द-जैसे लगते हैं। (मेरी याद-पद्धति)",
    },
}


# ===================================================================== IMAGE_SPECS
IMAGE_SPECS = {
    ("78", "diagram"): {
        "file": "sh6-jneya-78.svg",
        "alt": ("Table of unit 78, numbered in the printed order: 1 vitiation (dūṣaṇa), 2 unwholesome food and conduct, "
                "3 complications (upadrava), 4 treatment (sādhana); each discerned by the signs of increase and decrease."),
        "type": "table",
        "title": "इकाई ७८: क्या जानें, कैसे पहचानें",
        "heads": ["क्रम", "जानने योग्य"],
        "rows": [["१", "दूषण (बिगाड़)"], ["२", "अहित आहार-विहार"], ["३", "उपद्रव"], ["४", "साधन (चिकित्सा)"],
                 ["पहचान", "वृद्धि-क्षय के लक्षण से"]],
    },
    ("80", "contrast"): {
        "file": "sh6-viddha-80.svg",
        "alt": ("Two columns of unit 80. One pierced in a srotas: having refused (pratyākhyāya), one should treat. One "
                "whose dart is extracted: by the procedure for a fresh wound; the verb is carried from line 1."),
        "type": "split",
        "title": "इकाई ८०: दो स्थितियाँ",
        "cols": [["स्रोतस् में विद्ध", ["प्रत्याख्याय: अस्वीकार करके", "उपाचरेत्: उपचार करे"]],
                 ["उद्धृतशल्य", ["सद्योव्रण की विधि से", "क्रिया पंक्ति १ से"]]],
    },
    ("83", "diagram"): {
        "file": "sh6-avibhaga-83.svg",
        "alt": ("Flowchart of unit 83: three numbered reasons, 1 mutual proximity, 2 similar function, 3 fineness, lead "
                "to 'non-distinction as it were is seen'; a dotted link notes that their functions are distinct."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"१ परस्पर सन्निकर्ष\"] --> D[\"अविभाग इव लक्ष्यते\"]\n"
                 "  B[\"२ सदृश कर्मत्व\"] --> D\n"
                 "  C[\"३ सौक्ष्म्य\"] --> D\n"
                 "  E[\"पर कर्म विभक्त\"] -.-> D\n"),
    },
    ("85", "diagram"): {
        "file": "sh6-avakasha-nama-85.svg",
        "alt": ("Table of the names in unit 85 in printed order with meanings: srotas, sirā, dhamanī, carriers of rasa, "
                "nāḍī, paths, routes, ways, openings of the body (closed and open), places, seats, abodes, dwellings: "
                "names of the spaces of the dhātus."),
        "type": "table",
        "title": "इकाई ८५: धातु-अवकाशों के नाम (छपे क्रम में)",
        "heads": ["नाम", "अर्थ"],
        "rows": [["स्रोतांसि", "स्रोतस्, नलिकाएँ"], ["सिराः", "सिराएँ"], ["धमन्यः", "धमनियाँ"],
                 ["रसवाहिन्यः", "रस-वाहिनियाँ"], ["नाड्‌यः", "नाड़ियाँ"], ["पन्थानः", "पथ"], ["अयनानि", "अयन, रास्ते"],
                 ["मार्गाः", "मार्ग"], ["शरीरच्छिद्राणि", "शरीर के छिद्र"], ["संवृतासंवृतानि", "बन्द और खुले (छिद्रों के साथ, या अलग नाम)"],
                 ["स्थानानि", "स्थान"], ["आशयाः", "आशय, आधार"], ["क्षयाः", "निवास"], ["निकेताः", "आवास"]],
    },
    ("89", "chain"): {
        "file": "sh6-prakopa-86-89.svg",
        "alt": ("Chain of units 86 to 89: these spaces; agitated, they agitate the dhātus; they too agitate those and "
                "the srotas; the srotas and dhātus agitate the dhātus. The verb is carried from unit 87."),
        "type": "chain",
        "title": "इकाई ८६-८९: प्रकोप की कड़ी",
        "steps": ["८६: ते च अवकाशाः", "८७: प्रकुपित होकर धातुओं को प्रकुपित करते हैं",
                  "८८: वे भी उन्हें और स्रोतसों को", "८९: स्रोतस् और धातु, धातुओं को"],
    },
}
