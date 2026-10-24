from helpers import mcq, match, order, fill, multi, accepts

# Kalpasthana chapter 5 (Siddhabastikalpa), units 30-46.
# 30-35: excess of yapana and its use without restrictions (lines 05.05.58-69);
# 36-46: the sahacaradi sneha-basti without restrictions (lines 05.05.70-91),
# one long recipe whose verb comes only in 05.05.77 (ksipet) and 05.05.84 (dadyat).

AUTHORED = {}

# ---------------------------------------------------------------- unit 30
AUTHORED["30"] = {
    "title": "निरूहा लेखनाः प्रायो",
    "question": "What does verse 30 say nirūha and sneha enemas do, and why is anuvāsana not wanted in yāpana?",
    "rule": ("For the most part, nirūha enemas are lekhana (scraping, thinning) and sneha enemas "
             "bṛṃhaṇa (nourishing). In the yāpana enemas there is both; therefore anuvāsana (oil enema) is "
             "not desired in them."),
    "limits": ("prāyaḥ (mostly) may qualify either half of line 1. What ubhayam (both) names is not "
               "stated: presumably the two effects of line 05.05.58. Whether 'enemas' should be "
               "supplied after yāpana is an open point (OPEN 05.05.59): no question uses it."),
    "explain_hi": ("यह श्लोक दो प्रकार की बस्तियों का स्वभाव बताता है: निरूह बस्तियाँ प्रायः लेखन यानी खुरचने और पतला करने वाली हैं, स्नेहबस्तियाँ बृंहण यानी पोषण करने वाली। "
                   "यापन बस्तियों में ‘उभयम्’ यानी दोनों हैं। "
                   "‘तस्मात्’ यानी इसलिए उनमें अनुवासन यानी स्नेह-बस्ति इष्ट नहीं है। "
                   "‘दोनों’ से ठीक क्या अभिप्रेत है, पाठ स्वयं नहीं कहता; सम्भवतः लेखन और बृंहण के दो प्रभाव।"),
    "hook": "निरूह खुरचे, स्नेह पोषे; यापन में दोनों, इसलिए अनुवासन नहीं।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "What does verse 30 say nirūha enemas are?",
            ("Lekhana: scraping, thinning", "निरूहा लेखनाः = nirūha enemas are scraping (lekhana)."),
            [("Bṛṃhaṇa: nourishing", "Nourishing (bṛṃhaṇa) is said of the sneha enemas."),
             ("Dīpana: kindling fire", "Kindling comes in verse 33, as a treatment, not here."),
             ("Stambhana: checking, retaining", "Checking is not said of nirūha in verse 30.")],
            "Line 1 pairs nirūha with lekhana and sneha-basti with bṛṃhaṇa.",
            "निरूह = लेखन; स्नेहबस्ति = बृंहण (प्रायः)."),
        match(1, "Match each word of verse 30 to its meaning on the card.",
              [["लेखन", "scraping, thinning"], ["बृंहण", "nourishing, bulk-building"],
               ["प्रायः", "mostly"], ["नेष्टम्", "not desired"]],
              "Two effects, the word that softens them, and the verdict on anuvāsana.",
              "लेखन = scraping; बृंहण = nourishing; प्रायः = mostly; न इष्टम् = not desired."),
        order(2, "Put the phrases of verse 30 in their order.",
              ["निरूहा लेखनाः", "प्रायो बृंहणाः स्नेहबस्तयः", "यापनेषूभयं", "तस्मान्नेष्टं तेष्वनुवासनं"],
              "Two kinds, then yāpana having both, then the conclusion with तस्मात्.",
              "निरूह लेखन · स्नेहबस्ति बृंहण · यापन में दोनों · इसलिए अनुवासन नहीं.",
              role="extend",
              teaches="Verse 30 argues in steps: nirūha scrapes, sneha nourishes, yāpana has both, therefore no anuvāsana in yāpana."),
        mcq("discriminate", 3, "Which split of यापनेषूभयं is right?",
            ("यापनेषु + उभयम्", "उ + उ → ऊ: यापनेषु (in the yāpana) + उभयम् (both)."),
            [("यापनेषु + अभयम्", "उ + अ would give व: यापनेष्वभयम्, not ऊ."),
             ("यापनेषू + भयम्", "यापनेषू is no form; the locative plural ends in -एषु."),
             ("यापने + षूभयम्", "षूभयम् is not a word; the ending -षु belongs to यापनेषु.")],
            "The long ऊ comes from two short उ: -एषु + उभयम्.",
            "उ + उ → ऊ: यापनेषु + उभयम् = यापनेषूभयम्."),
        mcq("apply", 4, "Why, by verse 30, is anuvāsana not desired in the yāpana enemas?",
            ("Because yāpana already has both", "यापनेषूभयं तस्मात्: there is both in yāpana; therefore not."),
            [("Because yāpana is too sharp", "Sharpness is not the reason the verse gives."),
             ("Because the patient is weak", "The verse says nothing about the patient here."),
             ("Because the season forbids it", "No season is named in verse 30.")],
            "तस्मात् (therefore) ties the verdict to the line before it: in yāpana there is both.",
            "उभयम् … तस्मात् न इष्टम् = both are there, hence not desired."),
        mcq("transfer", 5,
            "Like नेष्टम् (न + इष्टम्), how do न + इच्छति (wishes) join?",
            ("नेच्छति", "अ + इ → ए: न + इच्छति = नेच्छति, as न + इष्टम् = नेष्टम्."),
            [("नैच्छति", "ऐ comes from अ + ए, not from अ + इ."),
             ("नीच्छति", "अ + इ does not give ई; the guṇa vowel is ए."),
             ("नयिच्छति", "No य is inserted; the two vowels merge to ए.")],
            "अ + इ → ए is the same join as in नेष्टम्.",
            "अ + इ → ए.",
            teaches="अ + इ joins to ए: न + इष्टम् = नेष्टम्, न + इच्छति = नेच्छति."),
    ],
}

# ---------------------------------------------------------------- unit 31
AUTHORED["31"] = {
    "title": "मृदुत्वान्न निवर्त्तेरन्",
    "question": "What does verse 31 prescribe when the mild yāpana enemas do not come back?",
    "rule": ("If, because of their mildness, these (enemas) do not return in someone: 'having given "
             "an āsthāpana (nirūha) with sharp enemas together with urine, he quickly indeed ...' "
             "(the main verb is missing)."),
    "limits": ("Low confidence. The main verb is missing: the sentence of 05.05.60-61 may continue "
               "in the next unit or a clause is lost. 'Return' is literal; 'not expelled' is only "
               "presumed. Who gives the āsthāpana and who saḥ (he) is are not both clear."),
    "explain_hi": ("यह श्लोक एक कठिनाई बताता है: जिस रोगी में दी गई ये बस्तियाँ मृदु होने के कारण वापस न लौटें। "
                   "दूसरी पंक्ति: ‘मूत्र सहित तीक्ष्ण बस्तियों से आस्थापन यानी निरूह करके, वह शीघ्र ही ...’; आस्थापन कौन करे और ‘सः’ कौन है, दोनों स्पष्ट नहीं। "
                   "‘न लौटें’ शाब्दिक है; ‘बाहर न निकलें’ केवल अनुमान है। "
                   "दूसरी पंक्ति में मुख्य क्रिया नहीं है, इसलिए वाक्य अधूरा है।"),
    "hook": "मृदु बस्ति न लौटे तो तीक्ष्ण, मूत्र-युक्त आस्थापन, जल्दी।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Why might the enemas of verse 31 not return?",
            ("Because of their mildness", "मृदुत्वात् = because of mildness (ablative of cause)."),
            [("Because of their sharpness", "Sharp enemas are the remedy in line 2, not the cause."),
             ("Because of too much urine", "Urine goes into the remedy enemas, not the cause."),
             ("Because they were too warm", "Warmth is not named in verse 31.")],
            "The ablative मृदुत्वात् gives the reason: mildness.",
            "मृदुत्वात् न निवर्तेरन् = they may not return because of mildness."),
        match(1, "Match each word of verse 31 to its meaning on the card.",
              [["मृदुत्वात्", "because of mildness"], ["समूत्रैः", "together with urine"],
               ["तीक्ष्णैः", "sharp, strong"], ["क्षिप्रम्", "quickly"]],
              "The cause in line 1 and the features of the remedy in line 2.",
              "मृदुत्वात् = from mildness; समूत्र = with urine; तीक्ष्ण = sharp; क्षिप्रम् = quickly."),
        order(2, "Put the phrases of verse 31 in their order.",
              ["मृदुत्वान्न निवर्त्तेरन्", "यस्य त्वेते प्रयोजिताः", "समूत्रैर्बस्तिभिस्तीक्ष्णैः", "आस्थाप्य क्षिप्रमेव सः"],
              "First the trouble (not returning), the person, then the sharp urine enemas and the āsthāpana.",
              "न निवर्तेरन् · यस्य प्रयोजिताः · समूत्रैः तीक्ष्णैः · आस्थाप्य क्षिप्रम्.",
              role="extend",
              teaches="Verse 31 states the trouble first (mild enemas not returning) and then the remedy: a sharp āsthāpana with urine."),
        mcq("discriminate", 3, "With which enemas is the āsthāpana given in line 2 of verse 31?",
            ("Sharp ones, together with urine", "समूत्रैः बस्तिभिः तीक्ष्णैः = with sharp enemas with urine."),
            [("Mild ones, together with milk", "Mildness is the trouble; milk is not named here."),
             ("Oily ones, together with ghee", "No oil or ghee is named in verse 31."),
             ("Mild ones, together with honey", "Honey is not named; the remedy is sharp, not mild.")],
            "The remedy is the opposite of the cause: sharp against mild.",
            "मृदु (cause) ↔ तीक्ष्ण, समूत्र (remedy)."),
        mcq("apply", 4, "Does verse 31 itself say what then happens to him (सः)?",
            ("No; the line has no main verb", "The card: the verb is missing, the sentence continues or is lost."),
            [("Yes; he recovers at once", "No recovery is stated in verse 31."),
             ("Yes; he gets an anuvāsana next", "No anuvāsana is prescribed in this verse."),
             ("Yes; he must fast for a day", "No fasting is named in verse 31.")],
            "सः stands without a verb; build nothing on the missing clause.",
            "An absolutive (आस्थाप्य) needs a main verb, which this unit lacks."),
        mcq("transfer", 5,
            "Like आस्थाप्य (prefix आ- with -य), which invented form means having come, from आ + √गम्?",
            ("आगम्य", "With a prefix the absolutive takes -य: आ + गम् + य = आगम्य."),
            [("आगत्वा", "-त्वा is used without a prefix; with आ- the form takes -य."),
             ("आगमिष्यति", "This is a future verb, 'will come', not 'having come'."),
             ("आगच्छति", "This is a present verb, 'comes', not an absolutive.")],
            "Prefix + root takes -य (आस्थाप्य, आगम्य); a bare root takes -त्वा.",
            "Prefixed absolutive = -य.",
            teaches="With a prefix the absolutive ends in -य (आस्थाप्य, आगम्य); without one it ends in -त्वा."),
    ],
}
# ---------------------------------------------------------------- unit 32
AUTHORED["32"] = {
    "title": "शोफाग्निनाशपाण्डुत्व",
    "question": "Which troubles does verse 32 say come from excessive use of yāpana?",
    "rule": ("From excessive use of yāpana there may occur swelling (śopha), loss of the digestive "
             "fire, pallor, colic pain (śūla), haemorrhoids, cutting pains (parikartikā), fever "
             "and diarrhoea (atisāra)."),
    "limits": ("The verse gives no remedy here (it follows in verse 33). The arśaḥ member of the "
               "printed compound is irregular (text flag) and the Hindi word for pāṇḍutva is an open "
               "point (OPEN 05.05.62): no question uses either."),
    "explain_hi": ("यह श्लोक यापन बस्ति के अत्यधिक सेवन के दुष्परिणाम गिनाता है। "
                   "शोफ यानी सूजन, अग्नि का नाश यानी पाचक अग्नि का नष्ट होना, पाण्डुत्व यानी पाण्डुता (इसके हिन्दी शब्द पर खुला अवलोकन है), शूल यानी पेट की पीड़ा, अर्श यानी बवासीर और परिकर्तिका यानी काटने जैसी पीड़ा। "
                   "दूसरी पंक्ति ज्वर और अतिसार यानी दस्त जोड़ती है। "
                   "‘स्युः’ यानी हो सकते हैं: पूरी सूची इसी क्रिया का कर्ता है।"),
    "hook": "यापन ज़्यादा तो: सूजन, अग्नि-नाश, शूल, काटती पीड़ा, ज्वर, दस्त।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "From what does verse 32 say these troubles arise?",
            ("From excessive use of yāpana", "यापनात्यर्थसेवनात् = from excessive use of yāpana."),
            [("From too little yāpana", "अत्यर्थ means excessive, not too little."),
             ("From sharp enemas with urine", "Those are the remedy of verse 31, not this cause."),
             ("From anuvāsana given in yāpana", "Verse 30 calls that undesired but names no troubles.")],
            "The ablative at the end of the verse gives the cause.",
            "यापना-अत्यर्थ-सेवनात् = from excessive use of yāpana."),
        match(1, "Match each trouble of verse 32 to its meaning on the card.",
              [["शोफ", "swelling"], ["अग्निनाश", "loss of the digestive fire"],
               ["परिकर्तिका", "cutting pains"], ["अतिसार", "diarrhoea"]],
              "Four of the troubles, with the senses the data gives.",
              "शोफ = swelling; अग्निनाश = loss of agni; परिकर्तिका = cutting pain; अतिसार = diarrhoea."),
        order(2, "Put these troubles in the order of verse 32.",
              ["शोफ", "अग्निनाश", "शूल", "परिकर्तिका", "ज्वर", "अतिसार"],
              "Line 1 runs śopha, agni-nāśa, (pallor), śūla, (arśas), parikartikā; line 2 adds fever and diarrhoea.",
              "शोफ · अग्निनाश · पाण्डुत्व · शूल · अर्शः · परिकर्तिका ‖ ज्वर · अतिसार.",
              role="extend",
              teaches="Excess of yāpana: śopha, agni-nāśa, pallor, śūla, arśas, parikartikā, then fever and diarrhoea."),
        multi("discriminate", 3, "Which of these does verse 32 name as results of excessive yāpana?",
              [("शोफ (swelling)", "Named first in line 1."),
               ("ज्वर (fever)", "Named in line 2: ज्वरश्च."),
               ("अतिसार (diarrhoea)", "Named in line 2: अतिसारश्च."),
               ("कास (cough)", "Cough is not in verse 32."),
               ("छर्दि (vomiting)", "Vomiting is not in verse 32.")],
              [0, 1, 2],
              "Only items printed in the verse count: śopha, fever and diarrhoea are; cough and vomiting are not.",
              "Count as listed only what the verse names."),
        mcq("apply", 4, "Which split of ज्वरश्चातिसारश्च is right?",
            ("ज्वरः + च + अतिसारः + च", "ः → श् before च; च + अ → चा: fever and diarrhoea."),
            [("ज्वरः + चाति + सारः + च", "चाति is not a word; च joins with अतिसार."),
             ("ज्वरः + च + आतिसारः + च", "आतिसार is not a word; the noun is अतिसार."),
             ("ज्वरश्च + अति + सारः + च", "The noun is the one word अतिसार, not अति + सार here.")],
            "Visarga before च becomes श्; च + अतिसारः gives चातिसारः.",
            "ज्वरः च → ज्वरश्च; च + अतिसारः → चातिसारः."),
        mcq("transfer", 5,
            "With the same ending as सेवनात् (from use), which invented form says from excessive eating?",
            ("अत्यर्थभोजनात्", "-आत् is the ablative, 'from', as in सेवनात्."),
            [("अत्यर्थभोजने", "-ए is the locative, 'in eating'."),
             ("अत्यर्थभोजनस्य", "-अस्य is the genitive, 'of eating'."),
             ("अत्यर्थभोजनम्", "-अम् is nominative or accusative, not 'from'.")],
            "The ablative -आत् names the cause: from excessive use, from excessive eating.",
            "-आत् = ablative singular of an -अ stem: 'from'.",
            teaches="The ablative -आत् names a cause: यापनात्यर्थसेवनात् (from excessive use of yāpana), अत्यर्थभोजनात् (from excessive eating)."),
    ],
}

# ---------------------------------------------------------------- unit 33
AUTHORED["33"] = {
    "title": "अरिष्टक्षारसीध्वाद्यैः",
    "question": "What treatment does verse 33 want for the troubles of excess yāpana, and how is yāpana to be used?",
    "rule": ("In that case a kindling treatment (dīpanī kriyā) with ariṣṭa, kṣāra, sīdhu and so "
             "forth is desired. Therefore one should use yāpana too, with judgement (yuktyā) and as "
             "occasion arises (prasaṅgataḥ)."),
    "limits": ("ariṣṭa and sīdhu are drink names; no further identification is made. The sense of "
               "prasaṅgataḥ varies ('as occasion arises' or 'by continuation'): no question uses it. "
               "tatra refers to the troubles of 05.05.62-63."),
    "explain_hi": ("जब यापन के अत्यधिक सेवन से सूजन, मन्द अग्नि आदि हों, तब ‘दीपनी क्रिया’ यानी अग्नि को प्रदीप्त करने वाला उपचार इष्ट है। "
                   "उसके साधन हैं: अरिष्ट यानी किण्वित औषध-पेय, क्षार और सीधु यानी गन्ने के रस की मदिरा, आदि। "
                   "इसलिए यापन का सेवन भी युक्ति यानी विवेक से और प्रसंग के अनुसार करे। "
                   "‘प्रसङ्गतः’ का अर्थ निश्चित नहीं है।"),
    "hook": "अग्नि मन्द तो अरिष्ट, क्षार, सीधु से दीपन; यापन युक्ति से।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "What kind of treatment does verse 33 say is desired in that case?",
            ("A kindling one (dīpanī kriyā)", "दीपनी क्रिया = a treatment kindling the digestive fire."),
            [("A scraping one (lekhana)", "Lekhana is said of nirūha in verse 30."),
             ("A nourishing one (bṛṃhaṇa)", "Bṛṃhaṇa is said of sneha enemas in verse 30."),
             ("A sharp urine enema", "That is the remedy of verse 31, a different trouble.")],
            "After loss of the digestive fire, the treatment kindles it.",
            "दीपनी क्रिया = kindling treatment."),
        match(1, "Match each word of verse 33 to its meaning on the card.",
              [["अरिष्ट", "a fermented medicinal drink"], ["सीधु", "a fermented sugarcane drink"],
               ["दीपनी", "kindling the digestive fire"], ["युक्त्या", "with judgement"]],
              "Two drinks, the kind of treatment, and the manner of using yāpana.",
              "अरिष्ट, सीधु = fermented drinks; दीपनी = kindling; युक्त्या = with judgement."),
        order(2, "Put the phrases of verse 33 in their order.",
              ["अरिष्टक्षारसीध्वाद्यैः", "तत्रेष्टा दीपनी क्रिया", "युक्त्या तस्मान्निषेवेत", "यापनांच प्रसंगतः"],
              "The means, the treatment, then the advice on using yāpana.",
              "अरिष्ट-क्षार-सीधु आदि · दीपनी क्रिया इष्ट · युक्ति से सेवन · यापन भी.",
              role="extend",
              teaches="Verse 33 first names the kindling treatment (ariṣṭa, kṣāra, sīdhu) and then says to use yāpana with judgement."),
        mcq("discriminate", 3, "To what does तत्र (in that case) refer in verse 33, by the card?",
            ("The troubles of excess yāpana", "The card: tatra refers to the troubles of 05.05.62-63."),
            [("The enemas that do not return", "That case had its own remedy in verse 31."),
             ("The anuvāsana given in yāpana", "Verse 30 only calls that undesired."),
             ("The cooking of the decoction", "No decoction is being cooked in these lines.")],
            "The kindling treatment answers loss of agni and the other troubles just listed.",
            "तत्र = in that case (the troubles of verse 32)."),
        mcq("apply", 4, "Which split of सीध्वाद्यैः is right?",
            ("सीधु + आद्यैः", "उ + आ → वा: सीधु + आद्यैः = सीध्वाद्यैः."),
            [("सीधुः + आद्यैः", "A visarga after उ before a vowel gives र्: सीधुराद्यैः."),
             ("सीधु + अद्यैः", "उ + अ gives व, so the result would be सीध्वद्यैः."),
             ("सीध्वा + आद्यैः", "सीध्वा is no form; the drink's stem is सीधु.")],
            "The long आ after व् shows the second word begins with आ: आद्यैः.",
            "उ + आ → वा."),
        mcq("transfer", 5,
            "Like अरिष्टक्षारसीध्वाद्यैः, what does an invented घृततैलाद्यैः mean?",
            ("With ghee, oil and so forth", "-आद्यैः = with X and the rest, as in verse 33."),
            [("Without any ghee and without oil", "Nothing in -आद्यैः negates; it adds 'and so forth'."),
             ("Ghee taken before oil", "-आद्य is 'and the rest', not 'before'."),
             ("The first of ghee and oil", "आदि here means 'and so forth', not 'first part'.")],
            "-आद्यैः (instrumental plural) closes a list: with these and the like.",
            "X-आद्यैः = with X and so forth.",
            teaches="-आद्यैः closes an open list in the instrumental: with ariṣṭa, kṣāra, sīdhu and so forth; with ghee, oil and so forth."),
    ],
}

# ---------------------------------------------------------------- unit 34
AUTHORED["34"] = {
    "title": "मृद्वल्पौषधसंयोगात्",
    "question": "For which three reasons does verse 34 say yāpana enemas need no restrictions?",
    "rule": ("Because of the combination with mild and little medicine, because of a quantity "
             "reduced by a quarter, and because of use for a short time, there is no need of "
             "avoidance (niṣparihāratā) in the yāpana enemas."),
    "limits": ("Whether mṛdvalpa is 'mild and little' or 'mild little' is not decided. parihāra is "
               "avoidance or restraint (of food, regimen); the text does not list the "
               "restrictions. teṣu refers to the yāpana enemas."),
    "explain_hi": ("यह श्लोक बताता है कि यापन बस्तियों में परिहार यानी परहेज़ की आवश्यकता क्यों नहीं। "
                   "तीन कारण हैं: मृदु और अल्प औषध का संयोग, एक-चौथाई कम मात्रा, और थोड़े समय तक प्रयोग। "
                   "‘पादहीन’ का अर्थ है चौथाई घटाई हुई, यानी तीन-चौथाई; केवल चौथाई नहीं। "
                   "कौन से परहेज़ छूटते हैं, पाठ नहीं गिनाता।"),
    "hook": "मृदु-अल्प औषध, पौन मात्रा, थोड़ा समय: इसलिए परहेज़ नहीं।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "What does verse 34 say there is in the yāpana enemas?",
            ("No need of avoidance", "निष्परिहारता = absence of avoidance, no restrictions."),
            [("A strict list of avoidances", "The word is निः-परिहार: without avoidance."),
             ("A need for anuvāsana after", "No anuvāsana is named in verse 34."),
             ("A risk of fever and swelling", "Those come from excess, in verse 32.")],
            "निः (without) + परिहार (avoidance) + ता (-ness).",
            "निष्परिहारता = no restrictions."),
        order(1, "Put the three reasons of verse 34 in their order.",
              ["मृद्वल्पौषधसंयोगात्", "पादहीनप्रमाणतः", "अल्पकालोपयोगाच्च"],
              "Drug, quantity, then time: each reason in the ablative.",
              "औषध (मृदु, अल्प) · मात्रा (पादहीन) · काल (अल्प)."),
        match(2, "Match each word of verse 34 to its meaning on the card.",
              [["पाद", "one quarter"], ["हीन", "reduced"], ["अल्पकाल", "a short time"],
               ["परिहार", "avoidance, restraint"]],
              "The parts of the three reasons and the key noun.",
              "पाद = quarter; हीन = reduced; अल्पकाल = short time; परिहार = avoidance.",
              role="extend",
              teaches="पादहीन = reduced by a quarter; अल्पकाल = short time; परिहार = avoidance (of food, regimen)."),
        mcq("discriminate", 3, "What does पादहीनप्रमाणतः mean on the card?",
            ("A quantity less by a quarter", "पाद (quarter) + हीन (reduced): three quarters remain."),
            [("A quarter of the quantity", "That would leave a quarter; हीन says a quarter is taken off."),
             ("A quantity more by a quarter", "हीन means reduced, not increased."),
             ("A quantity measured by foot", "पाद here is one quarter, not the foot.")],
            "X-हीन = lacking X: the quantity lacks a quarter.",
            "पादहीन = reduced by a quarter."),
        mcq("apply", 4, "Does verse 34 list which restrictions (परिहार) are dropped?",
            ("No; it does not list them", "The card: the text does not list the restrictions."),
            [("Yes; day sleep and travel", "No such list is in verse 34."),
             ("Yes; meat and sour food", "No food is named in verse 34."),
             ("Yes; anger and loud speech", "No conduct is named in verse 34.")],
            "Only the general word परिहार stands; its members are not given here.",
            "Read no list into a general term."),
        mcq("transfer", 5,
            "Like निष्परिहारता (absence of avoidance), what does an invented मृदुता mean (मृदु = mild)?",
            ("Mildness", "-ता makes an abstract noun: मृदु → मृदुता, mildness."),
            [("A mild person", "A person would be the adjective itself, not -ता."),
             ("Made mild", "A past participle would be needed for 'made'."),
             ("Mildest", "The superlative is -तम: मृदुतम.")],
            "-ता turns an adjective into a '-ness' noun, like -त्व in मृदुत्व (verse 31).",
            "X-ता = X-ness.",
            teaches="The suffix -ता makes an abstract noun: निष्परिहारता (freedom from avoidance), मृदुता (mildness)."),
    ],
}

# ---------------------------------------------------------------- unit 35
AUTHORED["35"] = {
    "title": "द्रव्येषु यापनार्थेषु",
    "question": "How does verse 35 say enemas free from restrictions are to be applied with the yāpana drugs?",
    "rule": ("In the drugs meant for yāpana, from cooked sneha, separately each, or in all of them, "
             "one should apply enemas free from restrictions (parihāra-vivarjita)."),
    "limits": ("Low confidence. The syntax of the ablative siddhāsnehāt is not certain (possibly "
               "'apart from the cooked sneha'); its long ā is flagged. sarveṣu is read as 'in all "
               "the drugs'. No question uses the flagged word or the ablative's sense."),
    "explain_hi": ("यह श्लोक श्लोक ३४ का निष्कर्ष व्यवहार में बताता है। "
                   "यापन के प्रयोजन वाले द्रव्यों में, सिद्ध स्नेह से, अलग-अलग, या सब द्रव्यों में, परिहार-रहित बस्तियाँ दे। "
                   "‘परिहारविवर्जित’ यानी परहेज़ से मुक्त। "
                   "‘सिद्धास्नेहात्’ की वाक्य-रचना अनिश्चित है, इसलिए विश्वास निम्न है।"),
    "hook": "यापन-द्रव्य अलग-अलग या सब में: बस्ति बिना परहेज़।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "What kind of enemas does verse 35 say one should apply?",
            ("Ones free from restrictions", "परिहारविवर्जितान् = free from restrictions."),
            [("Ones with strict restrictions", "विवर्जित means free from, not bound by."),
             ("Sharp ones with urine", "Those are the remedy of verse 31."),
             ("Ones of honey alone", "No honey is named in verse 35.")],
            "The verse ends with the enemas' quality: without restrictions.",
            "परिहार-विवर्जित = free from restrictions."),
        match(1, "Match each word of verse 35 to its meaning on the card.",
              [["द्रव्येषु", "in the drugs"], ["यापनार्थेषु", "meant for yāpana"],
               ["युञ्ज्यात्", "one should apply"], ["विवर्जित", "free from"]],
              "The setting, the verb and the quality of the enemas.",
              "द्रव्येषु = in the drugs; यापनार्थ = meant for yāpana; युञ्ज्यात् = should apply; विवर्जित = free from."),
        order(2, "Put these parts of verse 35 in their order.",
              ["द्रव्येषु", "यापनार्थेषु", "बस्तीन्सर्वेषु वा", "युंज्यात्परिहारविवर्जितान्"],
              "The drugs come first, the enemas and the verb in line 2.",
              "द्रव्येषु यापनार्थेषु · … · बस्तीन् सर्वेषु वा · युञ्ज्यात् परिहारविवर्जितान्.",
              role="extend",
              teaches="Verse 35 names the yāpana drugs in line 1 and in line 2 the enemas free from restrictions with the verb युञ्ज्यात्."),
        mcq("discriminate", 3, "What case is बस्तीन् in verse 35, and why?",
            ("Accusative plural: the object", "बस्तीन् is what one should apply (युञ्ज्यात्)."),
            [("Nominative plural: the subject", "The nominative plural would be बस्तयः."),
             ("Locative plural: 'in enemas'", "The locative plural would be बस्तिषु."),
             ("Instrumental plural: 'with'", "The instrumental plural would be बस्तिभिः.")],
            "-ईन् is the accusative plural of a masculine -इ stem.",
            "बस्ति → बस्तीन् (acc. pl.), object of युञ्ज्यात्."),
        mcq("apply", 4, "Which word of verse 35 carries on the point of verse 34 (no restrictions)?",
            ("परिहारविवर्जितान्", "Free from parihāra: the same point as निष्परिहारता."),
            [("यापनार्थेषु", "This names the drugs' purpose, not freedom from restriction."),
             ("द्रव्येषु", "This only says 'in the drugs'."),
             ("सर्वेषु", "This says 'in all', not 'without restrictions'.")],
            "निष्परिहारता (verse 34) and परिहारविवर्जित (verse 35) say the same thing.",
            "परिहार-विवर्जित = निष्परिहार."),
        mcq("transfer", 5,
            "Like यापनार्थेषु (meant for yāpana), what does an invented वमनार्थेषु द्रव्येषु mean?",
            ("In the drugs meant for emesis", "-अर्थ = meant for: वमन-अर्थ = meant for emesis."),
            [("In the drugs free of emesis", "Freedom would need विवर्जित or निः-, not -अर्थ."),
             ("In the drugs caused by emesis", "-अर्थ gives purpose, not cause."),
             ("In the drugs after emesis", "-अर्थ says nothing about time.")],
            "X-अर्थ at the end of a compound = for the purpose of X.",
            "X-अर्थ = meant for X.",
            teaches="-अर्थ at the end of a compound gives purpose: यापनार्थ (meant for yāpana), वमनार्थ (meant for emesis)."),
    ],
}

# ---------------------------------------------------------------- unit 36
AUTHORED["36"] = {
    "title": "सहाचराभीरुबला",
    "question": "Which drugs begin the sahācarādi recipe of verse 36, and how are they boiled?",
    "rule": ("Of sahācara, abhīru, balā, rāsnā and gokṣuraka, separately, a tulā (of each) is taken, "
             "in a hundred droṇas of water, until five droṇas remain."),
    "limits": ("No verb: the boiling is understood, and the decoction is used in 05.05.72 (strained "
               "and cooled). sahācara and abhīru are probable identifications, rāsnā disputed, "
               "gokṣuraka standard; balā has no identification in the gloss. tulā and droṇa stay as "
               "measures."),
    "explain_hi": ("यहाँ से सहचरादि स्नेह-बस्ति का नुस्खा आरम्भ होता है। "
                   "सहाचर यानी सम्भवतः कटसरैया, अभीरु यानी सम्भवतः शतावरी, बला, रास्ना जिसकी पहचान विवादित है, और गोक्षुरक यानी गोखरू: इनमें से अलग-अलग एक-एक तुला। "
                   "इन्हें सौ द्रोण जल में, पाँच द्रोण शेष रहने तक (पकाया जाए; क्रिया पाठ में नहीं)। "
                   "तुला और द्रोण मान हैं, इन्हें बदला नहीं गया।"),
    "hook": "पाँच द्रव्य, प्रत्येक तुला; सौ द्रोण जल, पाँच द्रोण बचे।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "How much of each drug does verse 36 take?",
            ("A tulā (of each)", "तुलाम्, with पृथक् (separately): a tulā of each."),
            [("A prastha of each", "A prastha comes in 05.05.77, not here."),
             ("A pala of each", "No pala is named in verse 36."),
             ("A droṇa of each", "Droṇas measure the water, not the drugs.")],
            "पृथक् … तुलाम् = separately, a tulā (of each).",
            "तुला = the measure of each drug here."),
        match(1, "Match each drug of verse 36 to its identification on the card.",
              [["सहाचर", "probably Barleria prionitis"], ["अभीरु", "probably Asparagus racemosus"],
               ["गोक्षुरक", "puncture vine (Tribulus terrestris)"], ["रास्ना", "identity disputed"]],
              "Four drugs with the confidence words of the data.",
              "सहाचर, अभीरु = probable; गोक्षुरक = standard; रास्ना = disputed."),
        order(2, "Put the drugs of verse 36 in their order.",
              ["सहाचर", "अभीरु", "बला", "रास्ना", "गोक्षुरक"],
              "The compound opens with sahācara and closes with gokṣuraka in the ablative.",
              "सहाचर · अभीरु · बला · रास्ना · गोक्षुरक.",
              role="extend",
              teaches="The list of verse 36: sahācara, abhīru, balā, rāsnā, gokṣuraka."),
        mcq("discriminate", 3, "How much water does verse 36 use, and to what is it reduced?",
            ("A hundred droṇas, to five droṇas", "जलद्रोणशते … पञ्चद्रोणावशेषिते."),
            [("Five droṇas, to a hundred palas", "The hundred droṇas are the water; five droṇas remain."),
             ("A hundred droṇas, to a quarter", "The remainder is five droṇas, not a quarter."),
             ("A hundred prasthas, to five", "The unit is droṇa, not prastha.")],
            "Start: a hundred droṇas; end: five droṇas remain.",
            "जल-द्रोण-शत → पञ्च-द्रोण-अवशेष."),
        mcq("apply", 4, "Which split of पञ्चद्रोणावशेषिते is right?",
            ("पञ्चद्रोण + अवशेषिते", "अ + अ → आ: द्रोण + अवशेषिते (remaining)."),
            [("पञ्चद्रोणा + वशेषिते", "वशेषित is no word; the word is अवशेषित."),
             ("पञ्चद्रोणः + अवशेषिते", "A visarga would give द्रोणोऽवशेषिते; this is inside a compound."),
             ("पञ्च + द्रोणावशे + षिते", "षिते is no word; the participle is अवशेषिते.")],
            "Inside the compound the stem द्रोण meets अवशेषित: अ + अ → आ.",
            "अ + अ → आ: द्रोण + अवशेषित."),
        mcq("transfer", 5,
            "Like पञ्चद्रोणावशेषिते (when five droṇas remain), what does an invented पादावशेषिते mean?",
            ("When a quarter remains", "पाद (quarter) + अवशेषिते (remaining), locative: 'when'."),
            [("When a quarter is added", "अवशेषित means remaining, not added."),
             ("A quarter of the rest is drunk", "Nothing about drinking is in the form."),
             ("Before a quarter boils away", "The locative of अवशेषित marks what remains.")],
            "X-अवशेषिते (locative) = when X remains.",
            "X-अवशेषिते = when X remains.",
            teaches="X-अवशेषिते (locative) marks the boiling-down point: पञ्चद्रोणावशेषिते (five droṇas left), पादावशेषिते (a quarter left)."),
    ],
}

# ---------------------------------------------------------------- unit 37
AUTHORED["37"] = {
    "title": "पूतशीते बिसद्राक्षा",
    "question": "What is done to the decoction in verse 37, and which clear drugs follow?",
    "rule": ("When (the decoction) is strained and cooled, the paste drugs follow: bisa (lotus "
             "stalk), drākṣā (grape or raisin), nata, an unclear vakṣīrī, nidigdhikā (yellow-berried "
             "nightshade); line 2 is a garbled list."),
    "limits": ("Low confidence. vakṣīrī is not a known plant (perhaps vaṃśakṣīrī), the nata split "
               "is unsure (OPEN 05.05.72) and line 2 cannot be divided safely; no question uses "
               "them. The drugs are put into the decoction in 05.05.77."),
    "explain_hi": ("जब श्लोक ३६ का क्वाथ छानकर ठण्डा हो जाए, तब कल्क के द्रव्यों की सूची आती है। "
                   "स्पष्ट नाम: बिस यानी कमलनाल, द्राक्षा यानी अंगूर या मुनक्का, और निदिग्धिका यानी कटेरी। "
                   "‘नत’ का विभाजन अनिश्चित है और ‘वक्षीरी’ पहचाना हुआ नाम नहीं, सम्भवतः वंशक्षीरी। "
                   "दूसरी पंक्ति का छपा समास बिगड़ा है; उसमें महासहा और सम्भवतः यष्टी हो सकते हैं, पर विभाजन सुरक्षित नहीं।"),
    "hook": "छानो, ठण्डा करो; फिर बिस, द्राक्षा, निदिग्धिका।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "What has happened to the decoction when the drugs of verse 37 come in?",
            ("It is strained and cooled", "पूतशीते = when strained and cooled."),
            [("It is boiled a second time", "No second boiling is named in verse 37."),
             ("It is mixed with honey", "No honey is named in verse 37."),
             ("It is kept overnight", "No time of keeping is named in verse 37.")],
            "पूत (strained) + शीत (cooled), in the locative: 'when'.",
            "पूत-शीते = when strained and cooled."),
        match(1, "Match each word of line 1 of verse 37 to its meaning on the card.",
              [["पूत", "strained"], ["बिस", "lotus stalk"], ["द्राक्षा", "grape or raisin"],
               ["निदिग्धिका", "yellow-berried nightshade"]],
              "The clear words of line 1 only.",
              "पूत = strained; बिस = lotus stalk; द्राक्षा = grape; निदिग्धिका = yellow-berried nightshade."),
        order(2, "Put these clear drugs in the order of line 1 of verse 37.",
              ["बिस", "द्राक्षा", "निदिग्धिका"],
              "Bisa opens the compound, drākṣā follows, nidigdhikā closes it (with the unclear words between).",
              "बिस · द्राक्षा · (नत, वक्षीरी: अनिश्चित) · निदिग्धिका.",
              role="extend",
              teaches="The paste list opens with bisa and drākṣā and line 1 closes with nidigdhikā."),
        mcq("discriminate", 3, "What does the card say about line 2 of verse 37?",
            ("It is garbled; nothing is built on it", "The card: the compound cannot be divided safely."),
            [("It names five certain drugs", "The division is not safe, so no drug is certain."),
             ("It gives the water measure", "The measures are in verse 36, not line 2 here."),
             ("It holds the verb of the recipe", "The verb comes in 05.05.77 (क्षिपेत्).")],
            "A garbled line stays unsplit and unused.",
            "Damaged print: no identification is built on it."),
        multi("apply", 4, "Which of these drugs does line 1 of verse 37 name?",
              [("बिस", "Named first in the compound."),
               ("द्राक्षा", "Named second in the compound."),
               ("निदिग्धिका", "Closes the compound of line 1."),
               ("सहाचर", "Sahācara heads verse 36, not verse 37."),
               ("चन्दन", "Candana comes in verse 38.")],
              [0, 1, 2],
              "Bisa, drākṣā and nidigdhikā are in line 1; sahācara and candana belong to the neighbouring verses.",
              "Keep each list to its own verse."),
        mcq("transfer", 5,
            "Like पूतशीते (when strained and cooled), what does an invented पक्वशीते mean (पक्व = cooked)?",
            ("When cooked and cooled", "Two participles in a locative compound: 'when X-ed and Y-ed'."),
            [("When cooked in cold water", "शीत here is 'cooled', a state, not cold water."),
             ("Cooked before it is cold", "The compound says both have happened, not 'before'."),
             ("Cooled, then cooked again", "The order of the compound is cooked, then cooled.")],
            "X-Y-ए (locative) = when X-ed and Y-ed.",
            "पूत-शीते, पक्व-शीते: locative of time.",
            teaches="A compound of two past participles in the locative marks the moment: पूतशीते (when strained and cooled), पक्वशीते (when cooked and cooled)."),
    ],
}

# ---------------------------------------------------------------- unit 38
AUTHORED["38"] = {
    "title": "जीवकर्षभकोदीच्य",
    "question": "Which further drugs does verse 38 add to the paste of the sahācarādi enema?",
    "rule": ("The list goes on: jīvaka, ṛṣabhaka, udīcya (probably hrīvera), mṛṇāla (lotus fibre), "
             "utpala (blue lotus) and candana (sandalwood); kharjūra (date), the kernel of tāla "
             "(palmyra), ātmaguptā, āmalakī and kaṇā (probably long pepper)."),
    "limits": ("jīvaka and ṛṣabhaka are aṣṭavarga drugs of disputed identity. The printed "
               "ātmaguptānāmalakī has an extra n (text flag): no question uses ātmaguptā or "
               "āmalakī. No verb: the list is put into the decoction in 05.05.77."),
    "explain_hi": ("सूची आगे चलती है। पहली पंक्ति: जीवक और ऋषभक (अष्टवर्ग के द्रव्य, पहचान विवादित), उदीच्य यानी सम्भवतः सुगन्धबाला, मृणाल यानी कमलनाल, उत्पल यानी नीलकमल, और चन्दन। "
                   "दूसरी पंक्ति: खर्जूर यानी खजूर, ताल की मज्जा यानी ताड़ की गिरी, आत्मगुप्ता यानी केवाँच, आमलकी यानी आँवला, और कणा यानी सम्भवतः पीपर। "
                   "छपे ‘आत्मगुप्तानामलकी’ में एक ‘न’ अधिक है। "
                   "यह सब कल्क बनकर क्वाथ में डाला जाएगा।"),
    "hook": "जीवक-ऋषभक, कमल-परिवार, चन्दन; खजूर, ताड़ की गिरी, आँवला, पीपर।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Which of these drugs does verse 38 name?",
            ("Candana (sandalwood)", "चन्दनम् closes line 1 of verse 38."),
            [("Gokṣuraka (puncture vine)", "Gokṣuraka is in verse 36."),
             ("Drākṣā (grape or raisin)", "Drākṣā is in verse 37."),
             ("Paṭola (pointed gourd)", "Paṭola opens verse 39.")],
            "Line 1 ends with candana.",
            "चन्दन = sandalwood (standard)."),
        match(1, "Match each drug of verse 38 to its meaning on the card.",
              [["मृणाल", "lotus fibre or stalk"], ["उत्पल", "blue lotus or water lily"],
               ["चन्दन", "sandalwood"], ["खर्जूर", "date"]],
              "Four drugs whose sense the data gives as plain or standard.",
              "मृणाल = lotus fibre; उत्पल = blue lotus; चन्दन = sandalwood; खर्जूर = date."),
        order(2, "Put the drugs of line 1 of verse 38 in their order.",
              ["जीवक", "ऋषभक", "उदीच्य", "मृणाल", "उत्पल", "चन्दन"],
              "Two aṣṭavarga drugs, udīcya, the two lotus items, then sandalwood.",
              "जीवक · ऋषभक · उदीच्य · मृणाल · उत्पल · चन्दन.",
              role="extend",
              teaches="Line 1 of verse 38: jīvaka, ṛṣabhaka, udīcya, mṛṇāla, utpala, candana."),
        mcq("discriminate", 3, "What does तालमज्जा mean on the card?",
            ("The kernel of tāla (palmyra)", "ताल = palmyra palm; मज्जा = kernel (majjā)."),
            [("The bark of the palmyra", "Bark would be त्वक्; मज्जा is the kernel."),
             ("The juice or sap of the palmyra tree", "Juice would be रस; मज्जा is the kernel."),
             ("The leaf of the palmyra", "Leaf would be पत्र; मज्जा is the kernel.")],
            "मज्जा is rendered 'kernel (majjā)' in this book.",
            "ताल-मज्जा = palmyra kernel."),
        mcq("apply", 4, "Which split of जीवकर्षभक is right?",
            ("जीवक + ऋषभक", "अ + ऋ → अर्: जीवक + ऋषभक = जीवकर्षभक."),
            [("जीव + कर्षभक", "कर्षभक is no drug name; the second drug is ऋषभक."),
             ("जीवक + अर्षभक", "अर्षभक is no word; अर् comes from अ + ऋ."),
             ("जीवकर् + षभक", "Neither part is a word; the drugs are जीवक, ऋषभक.")],
            "The र् before ष shows a hidden ऋ: अ + ऋ → अर्.",
            "अ + ऋ → अर्."),
        mcq("transfer", 5,
            "Like जीवकर्षभक (जीवक + ऋषभक), how do देव + ऋषि join?",
            ("देवर्षि", "अ + ऋ → अर्: देव + ऋषि = देवर्षि."),
            [("देवार्षि", "अ + ऋ gives short अर्, not आर्."),
             ("देव्रषि", "The vowel ऋ does not turn into र् + अ here."),
             ("देवरिषि", "रि is a spelling of ऋ alone; the join gives अर्.")],
            "Same join as in the drug names: अ + ऋ → अर्.",
            "अ + ऋ → अर्.",
            teaches="अ + ऋ joins to अर्: जीवक + ऋषभक = जीवकर्षभक, देव + ऋषि = देवर्षि."),
    ],
}

# ---------------------------------------------------------------- unit 39
AUTHORED["39"] = {
    "title": "पटोलमेदात्वक्पत्र",
    "question": "Which last paste drugs does verse 39 name, and what is done with the whole paste?",
    "rule": ("Paṭola (pointed gourd), medā, bark and leaf (tvak, patra), śītapākī and those named "
             "odana: having made them into a paste (kalka), one should put them into that "
             "(decoction), and separately (an item) measured by a prastha."),
    "limits": ("Low confidence. medā is disputed; śītapākī and odana are unidentified (OPEN "
               "05.05.76). tvak-patra as the cinnamon pair is probable only. -āvhayāḥ is flagged. "
               "The item 'measured by a prastha' is named only in 05.05.78."),
    "explain_hi": ("यह श्लोक कल्क-सूची पूरी करता है: पटोल यानी परवल, मेदा नामक द्रव्य (पहचान विवादित), त्वक् और पत्र, शीतपाकी और ‘ओदन’ नाम वाले (दोनों अज्ञात)। "
                   "फिर क्रिया आती है: इन्हें कल्क यानी पिसी लुगदी बनाकर ‘उसमें’ यानी छने और ठण्डे क्वाथ में डाले। "
                   "और अलग से एक प्रस्थ-मापा द्रव्य भी, जिसका नाम अगली पंक्ति में है। "
                   "श्लोक ३६ से चला लम्बा वाक्य यहाँ अपनी पहली क्रिया ‘क्षिपेत्’ पाता है।"),
    "hook": "परवल, मेदा, त्वक्-पत्र; सबका कल्क बनाकर क्वाथ में डालो।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "What is done with the drugs of the list in verse 39?",
            ("Made into a paste, put in", "कल्कीकृत्य क्षिपेत् तस्मिन् = made into a paste, put into that."),
            [("Boiled in milk and drunk", "No milk or drinking is named in verse 39."),
             ("Burnt and the ash kept", "No burning is named in verse 39."),
             ("Dried and kept in a jar", "No drying is named in verse 39.")],
            "The absolutive कल्कीकृत्य comes before the verb क्षिपेत्.",
            "कल्कीकृत्य क्षिपेत् = make a paste, then put it in."),
        match(1, "Match each word of verse 39 to its meaning on the card.",
              [["पटोल", "pointed gourd"], ["कल्कीकृत्य", "having made into a paste"],
               ["क्षिपेत्", "one should put"], ["तस्मिन्", "into that"]],
              "One clear drug and the three words of the procedure.",
              "पटोल = pointed gourd; कल्कीकृत्य = making a paste; क्षिपेत् = should put; तस्मिन् = into that."),
        order(2, "Put the words of line 2 of verse 39 in their order.",
              ["कल्कीकृत्य", "क्षिपेत्", "तस्मिन्", "पृथक् च", "प्रस्थसंमितम्"],
              "Make the paste, put it in that, and separately a prastha-measured item.",
              "कल्कीकृत्य · क्षिपेत् · तस्मिन् · पृथक् च · प्रस्थसंमितम्.",
              role="extend",
              teaches="Line 2 of verse 39 is the step: make a kalka, put it into the decoction, and separately add a prastha-measured item."),
        mcq("discriminate", 3, "Into what is the paste put (तस्मिन्), by the card?",
            ("The strained, cooled decoction", "The card: tasmin is the decoction of 05.05.72."),
            [("The two āḍhakas of cow's milk", "The milk is named later, in verse 41."),
             ("The oil and ghee of verse 40", "Those are further items, not 'that'."),
             ("The paste of the previous verse", "The paste is what is put in, not where.")],
            "तस्मिन् points back to the decoction strained and cooled in verse 37.",
            "तस्मिन् = into that decoction."),
        mcq("apply", 4, "What does the card say about मेदा in verse 39?",
            ("A drug of disputed identity", "The data: medā is disputed; Hindi writes 'मेदा नामक द्रव्य'."),
            [("Wheat flour, as in Hindi", "मेदा here is a drug, not flour."),
             ("Body fat (medas)", "The drug medā is a different word from medas."),
             ("Asparagus, a standard name", "Asparagus is the probable abhīru of verse 36.")],
            "A disputed drug keeps its Sanskrit name with the word 'disputed'.",
            "मेदा = drug name (identity disputed)."),
        mcq("transfer", 5,
            "Like कल्कीकृत्य (having made into a paste), what does an invented चूर्णीकृत्य mean (चूर्ण = powder)?",
            ("Having made into powder", "X-ी + कृत्य = having turned into X."),
            [("Having taken out the powder", "The -ी + कृ pattern makes, it does not remove."),
             ("Having mixed with powder", "Mixing would be a different verb or 'with'."),
             ("One should make a powder", "That would be an optative; -य marks 'having done'.")],
            "Noun with -ी + कृत्य = having made (something) into that noun.",
            "कल्की-कृत्य, चूर्णी-कृत्य.",
            teaches="Noun + -ी + कृत्य = having made into that: कल्कीकृत्य (into a paste), चूर्णीकृत्य (into powder)."),
    ],
}

# ---------------------------------------------------------------- unit 40
AUTHORED["40"] = {
    "title": "रसं वराहमहिष",
    "question": "Which animal products does verse 40 add to the sahācarādi enema?",
    "rule": ("The juice (rasa) arising from the testes of the boar, buffalo and he-goat; likewise "
             "oil and ghee (taila, sarpis), arising from the eggs of the peacock, the cock and the "
             "swan (how they relate is not stated)."),
    "limits": ("No verb in this unit (it may lie in 05.05.84, dadyāt). The Sanskrit does not say "
               "whether the oil and ghee come from the eggs or are prepared with them. A male "
               "buffalo is meant by context only. Whether each animal gives a prastha is not stated."),
    "explain_hi": ("इस श्लोक में और द्रव्य आते हैं। पहले रस: वराह यानी सूअर, महिष यानी भैंसा और बस्त यानी बकरा, इनके मुष्क यानी अण्डकोशों से उत्पन्न। "
                   "फिर शिखी यानी मोर, कुक्कुट यानी मुर्गा और हंस, इनके अण्डों से उत्पन्न, और तेल और घी। "
                   "तेल-घी अण्डों से बनें या उनके साथ पकें, संस्कृत स्पष्ट नहीं करती। "
                   "यहाँ ‘बस्त’ बकरा है, बस्ति नहीं।"),
    "hook": "सूअर, भैंसा, बकरा के मुष्क-रस; मोर, मुर्गा, हंस के अण्डे; तेल-घी।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "From the testes of which animals is the juice of verse 40?",
            ("Boar, buffalo and he-goat", "वराह-महिष-बस्त-मुष्क-उद्भवम्."),
            [("Peacock, cock and swan", "These three give eggs in line 2, not testes."),
             ("Deer, hare and quail", "None of these is named in verse 40."),
             ("Elephant, horse and bull", "None of these is named in verse 40.")],
            "Line 1 names three mammals; line 2 three birds.",
            "वराह, महिष, बस्त → मुष्क-रस."),
        match(1, "Match each word of verse 40 to its meaning on the card.",
              [["वराह", "boar"], ["महिष", "buffalo"], ["बस्त", "he-goat"], ["मुष्क", "testis"]],
              "The three animals of line 1 and the organ.",
              "वराह = boar; महिष = buffalo; बस्त = he-goat; मुष्क = testis."),
        order(2, "Put the animals of verse 40 in their order.",
              ["वराह", "महिष", "बस्त", "शिखी", "कुक्कुट", "हंस"],
              "Three mammals in line 1, three birds in line 2.",
              "वराह · महिष · बस्त ‖ शिखी · कुक्कुट · हंस.",
              role="extend",
              teaches="Verse 40: boar, buffalo, he-goat (testes juice), then peacock, cock, swan (eggs)."),
        mcq("discriminate", 3, "What does बस्त mean in verse 40?",
            ("A he-goat", "बस्त = he-goat, one of three animals of line 1."),
            [("An enema", "The enema is बस्ति; बस्त is the goat."),
             ("The bladder", "The bladder sense belongs to बस्ति, not बस्त."),
             ("The enema bag", "बस्त is the goat; no device is meant here.")],
            "Do not confuse बस्त (goat) with बस्ति (enema, bladder).",
            "बस्त = he-goat ≠ बस्ति."),
        mcq("apply", 4, "What does the card say about the oil, ghee and eggs of line 2?",
            ("It is not said how they relate", "The data: whether from the eggs or cooked with them is not stated."),
            [("The oil is pressed from the eggs", "That is one reading; the Sanskrit does not decide."),
             ("The eggs replace oil and ghee", "Nothing says the eggs replace them."),
             ("The eggs must be left out", "The eggs are named, not excluded.")],
            "The loose agreement (सम्भवम् singular, तैलसर्पिषी dual) leaves the relation open.",
            "Keep the literal 'arising from'; decide nothing more."),
        mcq("transfer", 5,
            "Like मुष्कोद्भवम् (arising from the testes), what does an invented जलोद्भवम् mean?",
            ("Arising from water", "-उद्भव = born of, arising from."),
            [("Producing or giving out water", "-उद्भव names the source, not the product."),
             ("Mixed with water", "Mixing would need सह or a 'with' word."),
             ("Free of water", "Freedom would need निः- or विवर्जित.")],
            "X-उद्भव = arising from X; अ + उ → ओ in the join.",
            "X-उद्भव = born of X.",
            teaches="X-उद्भव (with अ + उ → ओ) means arising from X: मुष्कोद्भवम् (from testes), जलोद्भवम् (from water)."),
    ],
}

# ---------------------------------------------------------------- unit 41
AUTHORED["41"] = {
    "title": "धात्रीविदारीस्वरसं",
    "question": "Which juice and milk does verse 41 add, and with what sounds is the mixture prepared?",
    "rule": ("The expressed juice (svarasa) of dhātrī (emblic myrobalan) and vidārī (probably "
             "Pueraria tuberosa), two āḍhakas of cow's milk; and that which is prepared with the "
             "sounds of brahma, bherī (kettledrum) and mṛdaṅga (drum)."),
    "limits": ("The sense of brahma at the head of the compound is not sure (sacred recitation or a "
               "drum name): no question uses it. The thing prepared is not named (neuter yat). No "
               "verb of giving in this unit."),
    "explain_hi": ("अब द्रव पदार्थ आते हैं: धात्री यानी आँवला और विदारी यानी सम्भवतः विदारीकन्द का स्वरस, और गाय के दूध के दो आढक। "
                   "दूसरी पंक्ति एक अनोखी विधि बताती है: जो ब्रह्म, भेरी यानी नगाड़ा और मृदंग की ध्वनियों के बीच तैयार किया गया हो। "
                   "‘ब्रह्म’ का अर्थ यहाँ निश्चित नहीं: पवित्र पाठ भी हो सकता है या किसी वाद्य का नाम। "
                   "तैयार की गई वस्तु का नाम इस इकाई में नहीं है।"),
    "hook": "आँवला-विदारी का स्वरस, दो आढक गोदुग्ध; नगाड़े-मृदंग की ध्वनि में तैयार।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Of which two drugs is the expressed juice in verse 41?",
            ("Dhātrī and vidārī", "धात्री-विदारी-स्वरसम्."),
            [("Drākṣā and bisa", "These are paste drugs of verse 37."),
             ("Kharjūra and tāla", "These are paste drugs of verse 38."),
             ("Paṭola and medā", "These are paste drugs of verse 39.")],
            "The svarasa is of dhātrī (emblic myrobalan) and vidārī.",
            "स्वरस = expressed juice."),
        match(1, "Match each word of verse 41 to its meaning on the card.",
              [["धात्री", "emblic myrobalan"], ["स्वरस", "expressed juice"],
               ["भेरी", "kettledrum"], ["निनाद", "sound"]],
              "A drug, the form of preparation, an instrument and the word for sound.",
              "धात्री = emblic myrobalan; स्वरस = expressed juice; भेरी = kettledrum; निनाद = sound."),
        order(2, "Put the phrases of verse 41 in their order.",
              ["धात्रीविदारीस्वरसं", "गव्यक्षीराढकद्वयं", "ब्रह्मभेरीमृदंगानां", "निनादैः", "साधितं च यत्"],
              "Juice, milk, then the instruments, their sounds and 'which is prepared'.",
              "स्वरस · दो आढक दूध · वाद्य · ध्वनियों से · तैयार.",
              role="extend",
              teaches="Verse 41: svarasa of dhātrī and vidārī, two āḍhakas of cow's milk, prepared with the sounds of drums."),
        mcq("discriminate", 3, "How much cow's milk does verse 41 name?",
            ("Two āḍhakas", "गव्य-क्षीर-आढक-द्वयम् = a pair of āḍhakas of cow's milk."),
            [("Two prasthas", "The measure is āḍhaka, not prastha."),
             ("One āḍhaka", "द्वयम् makes it a pair, two."),
             ("A hundred droṇas", "A hundred droṇas is the water of verse 36.")],
            "-द्वयम् = a pair: two āḍhakas.",
            "आढक-द्वयम् = two āḍhakas."),
        mcq("apply", 4, "What does निनादैः साधितम् say about the preparation?",
            ("Prepared with drum sounds", "निनादैः (instrumental) = with the sounds; साधितम् = prepared."),
            [("Prepared in silence", "The verse names sounds, not silence."),
             ("Boiled in drum-shaped pots", "निनाद is sound, not a vessel."),
             ("Prepared only at night", "No time of day is named in verse 41.")],
            "The instrumental निनादैः gives the accompaniment.",
            "निनादैः साधितम् = prepared with sounds."),
        mcq("transfer", 5,
            "Like आढकद्वयम् (two āḍhakas), what does an invented पलद्वयम् mean?",
            ("Two palas", "-द्वयम् = a pair of: two palas."),
            [("Half a pala", "Half would be अर्ध-पल."),
             ("A pala and a half", "That would be सार्ध-पल or अध्यर्ध-पल."),
             ("The second pala", "The second would be द्वितीय.")],
            "-द्वय at the end of a compound counts two.",
            "X-द्वयम् = two X.",
            teaches="X-द्वयम् means a pair of X: आढकद्वयम् (two āḍhakas), पलद्वयम् (two palas)."),
    ],
}

# ---------------------------------------------------------------- unit 42
AUTHORED["42"] = {
    "title": "सितच्छत्रकृतच्छायं",
    "question": "How is the prepared substance honoured in verse 42?",
    "rule": ("It is shaded by a white umbrella, covered with a white cloth, placed on the shoulder "
             "of an elephant; and 'having worshipped Vṛṣadhvaja (the bull-bannered one, Śiva)', "
             "whose main verb is not in this unit."),
    "limits": ("No noun is stated: the neuter adjectives describe the substance of 05.05.81. "
               "Vṛṣadhvaja as Śiva is the usual epithet (standard), but the line itself does not "
               "say Śiva. The agent of the worship is not named. skandha is shoulder or back."),
    "explain_hi": ("यह श्लोक तैयार किए गए द्रव्य के सम्मान का वर्णन करता है। "
                   "उस पर श्वेत छत्र से छाया हो, वह श्वेत वस्त्र से ढका हो, और हाथी के कन्धे पर रखा जाए। "
                   "फिर ‘वृषध्वज यानी वृषभ-ध्वज वाले शिव की पूजा करके’ आता है; इसकी मुख्य क्रिया इस इकाई में नहीं। "
                   "पूजा कौन करे, पाठ नहीं कहता; अगले श्लोक में स्वस्त्ययन और बस्ति आती है।"),
    "hook": "सफ़ेद छत्र, सफ़ेद वस्त्र, हाथी का कन्धा, शिव-पूजा।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Where is the prepared substance placed in verse 42?",
            ("On an elephant's shoulder", "आरोपितं गजस्कन्धे = placed on the shoulder of an elephant."),
            [("On a white cloth on the ground", "The white cloth covers it; it is not on the ground."),
             ("In a temple of Vṛṣadhvaja", "Vṛṣadhvaja is worshipped; no temple is named."),
             ("Under a tree in the shade", "The shade comes from a white umbrella, not a tree.")],
            "गज-स्कन्धे (locative) = on the elephant's shoulder.",
            "गजस्कन्ध = elephant's shoulder or back."),
        match(1, "Match each word of verse 42 to its meaning on the card.",
              [["सित", "white"], ["छत्र", "umbrella"], ["अवगुण्ठित", "covered"], ["आरोपित", "placed, mounted"]],
              "The four describing words of the honouring.",
              "सित = white; छत्र = umbrella; अवगुण्ठित = covered; आरोपित = placed."),
        order(2, "Put the phrases of verse 42 in their order.",
              ["सितच्छत्रकृतच्छायं", "सितवस्त्रावगुंठितं", "आरोपितं गजस्कंधे", "पूजयित्वा वृषध्वजं"],
              "Umbrella, cloth, elephant, worship.",
              "छत्र · वस्त्र · गज · वृषध्वज.",
              role="extend",
              teaches="Verse 42 runs: white umbrella shade, white cloth cover, placed on an elephant, Vṛṣadhvaja worshipped."),
        mcq("discriminate", 3, "What does वृषध्वज mean on the card?",
            ("Bull-bannered one, usually Śiva", "Literally 'having a bull as banner'; the usual epithet of Śiva."),
            [("A bull-shaped flag on the elephant", "It is the accusative object of worship, a deity."),
             ("The giver of virility to men", "वृष here is the bull of the banner, not virility."),
             ("The bull that carries the drug", "The elephant carries it; no bull carries anything.")],
            "A bahuvrīhi: one whose banner (ध्वज) is a bull (वृष).",
            "वृषध्वज = bull-bannered (Śiva, standard)."),
        mcq("apply", 4, "Which split of सितवस्त्रावगुंठितं is right?",
            ("सितवस्त्र + अवगुण्ठितम्", "अ + अ → आ: वस्त्र + अवगुण्ठितम् (covered)."),
            [("सितवस्त्रा + वगुण्ठितम्", "वगुण्ठित is no word; the participle is अवगुण्ठित."),
             ("सितवस्त्रः + अवगुण्ठितम्", "A visarga would give वस्त्रोऽवगुण्ठितम्; this is inside a compound."),
             ("सित + वस्त्राव + गुण्ठितम्", "वस्त्राव is no word; the stem is वस्त्र.")],
            "Same join as द्रोण + अवशेषित in verse 36: अ + अ → आ.",
            "अ + अ → आ."),
        mcq("transfer", 5,
            "Like पूजयित्वा (having worshipped, no prefix), which invented form means having eaten, from √भुज्?",
            ("भुक्त्वा", "A bare root takes -त्वा: भुज् + त्वा = भुक्त्वा."),
            [("भुज्य", "-य is used after a prefix; the bare root takes -त्वा."),
             ("भोक्ष्यति", "This is a future verb, 'will eat'."),
             ("भुङ्क्ते", "This is a present verb, 'eats'.")],
            "No prefix → -त्वा (पूजयित्वा, भुक्त्वा); prefix → -य (आस्थाप्य).",
            "Bare root absolutive = -त्वा.",
            teaches="Without a prefix the absolutive ends in -त्वा: पूजयित्वा, भुक्त्वा; with a prefix in -य: आस्थाप्य."),
    ],
}

# ---------------------------------------------------------------- unit 43
AUTHORED["43"] = {
    "title": "कृत्वा स्वस्त्ययनं दद्यात्",
    "question": "What does verse 43 say is done after the honouring, and what is the promised result?",
    "rule": ("Having performed the svastyayana (auspicious rite), one should give the sneha-basti "
             "without restriction (ayantraṇam). Having obtained excessive virility (ativṛṣatā) by "
             "it, he would exhaust a hundred women."),
    "limits": ("Line 2 rests on two conjectures (text flags): prāptes read as prāptaḥ, dhanitā as "
               "vanitā (OPEN 05.05.85); no question uses those words or the hundred women. What is "
               "left unrestricted (diet, conduct) is not stated; the giver is unnamed."),
    "explain_hi": ("सम्मान के बाद स्वस्त्ययन यानी मंगल-विधि करके यह स्नेहबस्ति ‘अयन्त्रणम्’ यानी बिना नियन्त्रण के दे। "
                   "‘अयन्त्रणम्’ नपुंसक है और बस्ति पुंलिङ्ग, इसलिए इसे क्रिया-विशेषण पढ़ा गया है; क्या अनियन्त्रित है, पाठ नहीं कहता। "
                   "दूसरी पंक्ति फल बताती है: उससे अतिवृषता यानी अत्यधिक पौरुष पाकर वह सौ स्त्रियों को थका दे। "
                   "यह पंक्ति दो अनुमानित सुधारों पर टिकी है (‘प्राप्तः’, ‘वनिता’)।"),
    "hook": "स्वस्त्ययन करके स्नेहबस्ति, बिना नियन्त्रण; फल: अतिवृषता।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "What is performed before the enema is given in verse 43?",
            ("The svastyayana (auspicious rite)", "कृत्वा स्वस्त्ययनम् = having performed the svastyayana."),
            [("A fast of one day", "No fast is named in verse 43."),
             ("A sharp nirūha enema", "No nirūha is named here; the enema is a sneha-basti."),
             ("A massage with oil", "No massage is named in verse 43.")],
            "The absolutive कृत्वा comes before the main verb दद्यात्.",
            "कृत्वा स्वस्त्ययनं दद्यात् = after the rite, give."),
        match(1, "Match each word of verse 43 to its meaning on the card.",
              [["स्वस्त्ययन", "auspicious rite"], ["दद्यात्", "should give"],
               ["अयन्त्रणम्", "without restriction"], ["अतिवृषता", "excessive virility"]],
              "The rite, the verb, its manner and the result.",
              "स्वस्त्ययन = auspicious rite; दद्यात् = should give; अयन्त्रणम् = unrestrained; अतिवृषता = excess virility."),
        order(2, "Put the words of line 1 of verse 43 in their order.",
              ["कृत्वा", "स्वस्त्ययनम्", "दद्यात्", "स्नेहबस्तिम्", "अयन्त्रणम्"],
              "Having done, the rite, should give, the sneha-basti, without restriction.",
              "कृत्वा · स्वस्त्ययनं · दद्यात् · स्नेहबस्तिम् · अयन्त्रणम्.",
              role="extend",
              teaches="Line 1 of verse 43 is the recipe's main command: after the svastyayana, give the sneha-basti without restriction."),
        mcq("discriminate", 3, "Why does the card read अयन्त्रणम् as an adverb?",
            ("It is neuter, but basti is masculine", "Gender disagrees with स्नेहबस्तिम्, so it modifies the giving."),
            [("Every word ending in -म् is an adverb", "-म् is also the accusative of many nouns."),
             ("It is a verb in the optative", "The optative verb is दद्यात्."),
             ("It is dual, and adverbs are dual", "It is singular; adverbs are not dual.")],
            "An adjective must agree with its noun; अयन्त्रणम् (n.) cannot agree with बस्तिम् (m.).",
            "Gender mismatch → read as adverb."),
        mcq("apply", 4, "Which kind of enema does verse 43 say is given?",
            ("A sneha-basti (unctuous enema)", "स्नेहबस्तिम् = the sneha-basti."),
            [("A nirūha with urine", "Urine enemas belong to verse 31."),
             ("A milk enema (kṣīra-basti)", "No milk enema is named in verse 43."),
             ("A sharp āsthāpana enema", "The āsthāpana belongs to verse 31.")],
            "The whole recipe from verse 36 ends in a sneha-basti.",
            "दद्यात् स्नेहबस्तिम् = give the sneha-basti."),
        mcq("transfer", 5,
            "Like दद्यात् (he should give), which invented form means he should drink, from √पा?",
            ("पिबेत्", "Optative 3rd singular: 'should drink', like दद्यात्."),
            [("पिबति", "This is the present: 'drinks'."),
             ("पीत्वा", "This is the absolutive: 'having drunk'."),
             ("पास्यति", "This is the future: 'will drink'.")],
            "The optative gives the instruction: दद्यात्, पिबेत्.",
            "Optative 3 sg. = should do.",
            teaches="Recipes give orders in the optative: दद्यात् (should give), क्षिपेत् (should put), पिबेत् (should drink)."),
    ],
}

# ---------------------------------------------------------------- unit 44
AUTHORED["44"] = {
    "title": "निर्वलीपलितः कान्तः",
    "question": "What does verse 44 promise the man, and for whom is the enema beneficial?",
    "rule": ("He would become free of wrinkles and grey hair, handsome and long-lived. It is "
             "beneficial for those whose semen is lost, the injured, the wasted, and those with "
             "irregular fever (viṣamajvara)."),
    "limits": ("The printed nirvalīpulitaḥ is read with the conjecture palita (text flag): no "
               "question uses that word. kṣata-kṣīṇa may also be one compound ('wasted through "
               "injury'). viṣamajvara as intermittent fever is probable. The subject 'it' is not "
               "stated."),
    "explain_hi": ("यह श्लोक बस्ति का फल बताता है: वह झुर्रियों और सफ़ेद बालों से रहित, कान्त यानी सुन्दर और चिरंजीवी हो जाएगा। "
                   "‘पलित’ (सफ़ेद बाल) छपे ‘पुलित’ का अनुमानित सुधार है। "
                   "दूसरी पंक्ति कहती है कि यह नष्ट-शुक्र, क्षत, क्षीण और विषमज्वर यानी अनियमित बुखार वालों के लिए हितकर है। "
                   "‘क्षत-क्षीण’ को एक समास भी पढ़ा जा सकता है: चोट से क्षीण।"),
    "hook": "झुर्री-रहित, सुन्दर, चिरंजीवी; क्षीण और विषमज्वर वालों का हित।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "What does line 1 of verse 44 say he would become, besides free of wrinkles?",
            ("Handsome and long-lived", "कान्तः चिरंजीवी = handsome, long-lived."),
            [("Strong, fat and free of disease", "Neither strength nor fat is named in verse 44."),
             ("Wise and calm", "Neither wisdom nor calm is named in verse 44."),
             ("Fair and slim", "Neither is named in verse 44.")],
            "Two nominatives follow the wrinkle word: कान्तः and चिरंजीवी.",
            "कान्त = handsome; चिरंजीवी = long-lived."),
        match(1, "Match each word of verse 44 to its meaning on the card.",
              [["कान्त", "handsome"], ["चिरंजीवी", "long-lived"], ["हित", "beneficial"],
               ["क्षीण", "wasted, depleted"]],
              "The promised qualities and the key words of line 2.",
              "कान्त = handsome; चिरंजीवी = long-lived; हित = beneficial; क्षीण = wasted."),
        order(2, "Put the words of line 2 of verse 44 in their order.",
              ["नष्टशुक्र", "क्षत", "क्षीण", "विषमज्वरिन्"],
              "The compound runs: lost semen, injured, wasted, irregular fever.",
              "नष्टशुक्र · क्षत · क्षीण · विषमज्वरी.",
              role="extend",
              teaches="Line 2 of verse 44: beneficial for those with lost semen, the injured, the wasted and those with viṣamajvara."),
        mcq("discriminate", 3, "What does विषमज्वर mean on the card?",
            ("Irregular (intermittent) fever", "विषम = irregular; the data: intermittent fever, probable."),
            [("Fever from poison", "विषम is 'irregular', not विष (poison)."),
             ("A very high fever", "विषम means uneven, not high."),
             ("A fever with cough", "No cough is in the word.")],
            "विषम (irregular) + ज्वर (fever): do not read विष (poison) into it.",
            "विषमज्वर = irregular fever (probable: intermittent)."),
        multi("apply", 4, "For whom does verse 44 say it is beneficial?",
              [("Those whose semen is lost", "नष्टशुक्र is named first."),
               ("The wasted (क्षीण)", "क्षीण is named in line 2."),
               ("Those with irregular fever", "विषमज्वरिणाम् closes the list."),
               ("The obese", "Obesity is not named in verse 44."),
               ("Small children", "Children are named in verse 20, not here.")],
              [0, 1, 2],
              "Line 2 lists lost semen, injured, wasted, irregular fever; nothing else.",
              "हितः + genitive plural = beneficial for those."),
        mcq("transfer", 5,
            "Like ज्वरिणाम् (of those having fever, from ज्वरिन्), what does an invented शूलिनाम् mean?",
            ("Of those who have colic", "-इन् = having; -इनाम् = of those having."),
            [("Of the colic itself, as a disease", "The colic itself would be शूलस्य."),
             ("Free from colic", "Freedom would need निः-: निःशूल."),
             ("Causing colic", "Causing would need a word like -कर.")],
            "-इन् makes a possessor; the genitive plural -इनाम् says 'for/of those having'.",
            "X-इन् = one having X.",
            teaches="-इन् makes 'one who has X': ज्वरिन् (feverish), शूलिन् (one with colic); genitive plural -इनाम्."),
    ],
}

# ---------------------------------------------------------------- unit 45
AUTHORED["45"] = {
    "title": "पुत्रदाता रसायनं",
    "question": "What two titles does verse 45 give the enema, and what does it say about other bastis?",
    "rule": ("For those whose menstrual blood and semen are spoiled it is a giver of sons and a "
             "rasāyana (rejuvenating tonic). In this way other bastis too are to be devised and "
             "cooked, in many ways (naikaśaḥ)."),
    "limits": ("The first word is misprinted (śuqāṇām for śukrāṇām, text flag): no question uses it. "
               "No verb in line 1; the subject 'it' is understood. Line 2 gives no further recipes."),
    "explain_hi": ("पहली पंक्ति कहती है कि जिनका आर्तव और शुक्र बिगड़ गया है, उनके लिए यह पुत्र देने वाला और रसायन यानी कायाकल्प करने वाला है। "
                   "छपे ‘शुक़ाणां’ में ‘शुक्राणां’ अभिप्रेत है। "
                   "दूसरी पंक्ति एक सामान्य नियम देती है: इसी प्रकार अन्य बस्तियाँ भी ‘कल्प्याः’ यानी बनाई जानी चाहिए और ‘पाक्याः’ यानी पकाई जानी चाहिए, ‘नैकशः’ यानी अनेक प्रकार से।"),
    "hook": "पुत्रदाता, रसायन; ऐसे ही और बस्तियाँ, अनेक प्रकार से।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Which two titles does line 1 of verse 45 give the enema?",
            ("Giver of sons; a rasāyana", "पुत्रदाता रसायनम्."),
            [("King of yāpanas; good for eyes", "Those titles belong to the mustādi yāpana of verse 18."),
             ("Scraping; nourishing", "These are the effects of verse 30."),
             ("Kindling; without restriction", "These come in verses 33 and 43.")],
            "Two nominatives: पुत्रदाता and रसायनम्.",
            "पुत्रदाता = giver of sons; रसायन = rejuvenating tonic."),
        match(1, "Match each word of verse 45 to its meaning on the card.",
              [["पुत्रदाता", "giver of a son"], ["रसायन", "rejuvenating tonic"],
               ["कल्प्याः", "to be devised"], ["नैकशः", "in many ways"]],
              "Two titles and the two key words of the closing rule.",
              "पुत्रदाता = giver of a son; रसायन = rejuvenating tonic; कल्प्य = to be devised; नैकशः = in many ways."),
        order(2, "Put the words of line 2 of verse 45 in their order.",
              ["एवं च", "बस्तयोऽन्येऽपि", "कल्प्याः", "पाक्याश्च", "नैकशः"],
              "Thus, other bastis also, to be devised, and cooked, in many ways.",
              "एवं च · बस्तयोऽन्येऽपि · कल्प्याः · पाक्याश्च · नैकशः.",
              role="extend",
              teaches="Line 2 of verse 45 turns the recipe into a pattern: other bastis are to be devised and cooked in many ways."),
        mcq("discriminate", 3, "Which split of नैकशः is right?",
            ("न + एकशः", "अ + ए → ऐ: न + एकशः, 'not singly'."),
            [("न + इकशः", "अ + इ would give ए: नेकशः, not नैकशः."),
             ("नै + कशः", "नै and कशः are not words here."),
             ("न + ऐकशः", "ऐकशः is no word; the adverb is एकशः.")],
            "ऐ comes from अ + ए (or अ + ऐ); here न + एकशः.",
            "अ + ए → ऐ."),
        mcq("apply", 4, "What does verse 45 say about other bastis?",
            ("Devised and cooked in many ways", "कल्प्याः पाक्याश्च नैकशः."),
            [("They are forbidden for these men", "Nothing is forbidden in verse 45."),
             ("They are made in one fixed way", "नैकशः means not singly: many ways."),
             ("They are made of milk only", "No milk is named in verse 45.")],
            "एवम् (in this way) makes the recipe a model for others.",
            "एवं … अन्ये अपि कल्प्याः = others too are to be devised thus."),
        mcq("transfer", 5,
            "Like कल्प्याः, पाक्याः (to be devised, to be cooked), which invented form means to be drunk, from √पा?",
            ("पेय", "Gerundive in -य: पा → पेय, 'to be drunk'."),
            [("पीत", "पीत is the past participle, 'drunk'."),
             ("पीत्वा", "पीत्वा is the absolutive, 'having drunk'."),
             ("पिबेत्", "पिबेत् is the optative, 'should drink'.")],
            "The gerundive -य says 'to be X-ed': कल्प्य, पाक्य, पेय.",
            "Gerundive -य = to be done.",
            teaches="The gerundive in -य means 'to be X-ed': कल्प्य (to be devised), पाक्य (to be cooked), पेय (to be drunk)."),
    ],
}

# ---------------------------------------------------------------- unit 46
AUTHORED["46"] = {
    "title": "शतं वारान्सहस्रं वा",
    "question": "How often does verse 46 say it should be cooked, and what does it announce next?",
    "rule": ("One should have it cooked a hundred or a thousand times, when it is possible "
             "(saṃbhave sati). Sneha-bastis that destroy the doṣas will be described (vakṣyante), "
             "with their precautions."),
    "limits": ("The object of pācayet (what is cooked) is not stated. The long ī of saparīhārā is "
               "flagged (sense unaffected): no question uses that word. The recipes themselves "
               "begin in the next unit."),
    "explain_hi": ("सम्भव होने पर इसे सौ बार या हज़ार बार पकवाए। "
                   "क्या पकाया जाए, पाठ स्पष्ट नहीं कहता। "
                   "दूसरी पंक्ति आगे का विषय बताती है: दोषघ्न यानी दोषों का नाश करने वाली स्नेहबस्तियाँ, परिहार सहित, ‘वक्ष्यन्ते’ यानी कही जाएँगी। "
                   "‘सम्भवे सति’ सति-सप्तमी है: सम्भव होने पर।"),
    "hook": "सौ या हज़ार बार पकाओ, यदि सम्भव; आगे दोषघ्न स्नेहबस्तियाँ।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "How many times does verse 46 say one should have it cooked?",
            ("A hundred or a thousand times", "शतं वारान् सहस्रं वा."),
            [("Once only, then strained and kept", "The verse speaks of many cookings."),
             ("Seven times each day", "No seven and no day are named."),
             ("Until five droṇas remain", "That is the boiling of verse 36.")],
            "शतम् … सहस्रं वा = a hundred or a thousand (times).",
            "शतं वारान् = a hundred times."),
        match(1, "Match each word of verse 46 to its meaning on the card.",
              [["पाचयेत्", "should have cooked"], ["सम्भवे सति", "when possible"],
               ["दोषघ्न", "destroying the doṣas"], ["वक्ष्यन्ते", "will be told"]],
              "The verb, its condition, and the announcement of line 2.",
              "पाचयेत् = should have cooked; सम्भवे सति = when possible; दोषघ्न = doṣa-destroying; वक्ष्यन्ते = will be told."),
        order(2, "Put the words of line 1 of verse 46 in their order.",
              ["शतं वारान्", "सहस्रं वा", "पाचयेत्", "संभवे सति"],
              "A hundred times, or a thousand, should have cooked, when possible.",
              "शतं वारान् · सहस्रं वा · पाचयेत् · संभवे सति.",
              role="extend",
              teaches="Line 1 of verse 46: a hundred or a thousand times, one should have it cooked, when possible."),
        mcq("discriminate", 3, "What tense and voice is वक्ष्यन्ते?",
            ("Future passive: will be told", "The data: 3 pl. future passive of √वच्."),
            [("Past passive: were told", "A past would be उक्ताः; वक्ष्य- is future."),
             ("Present passive: are told", "The present passive would be उच्यन्ते."),
             ("Optative passive: should be told", "The optative passive would be उच्येरन्.")],
            "-ष्य- marks the future; वक्ष्यन्ते looks ahead to the next recipes.",
            "वक्ष्यन्ते = will be told."),
        mcq("apply", 4, "What does line 2 of verse 46 say will be described next?",
            ("Sneha-bastis that destroy doṣas", "दोषघ्नाः … वक्ष्यन्ते स्नेहबस्तयः."),
            [("Nirūha enemas with urine", "Line 2 names sneha-bastis, not nirūha."),
             ("The complications of bastis", "Complications are not announced here."),
             ("Yāpana enemas for old and weak men", "Yāpana is not named in line 2.")],
            "The chapter turns from this recipe to doṣa-destroying sneha-bastis.",
            "दोषघ्न स्नेहबस्ति = the next topic."),
        mcq("transfer", 5,
            "Like सम्भवे सति (when it is possible), what does an invented काले सति mean?",
            ("When there is time", "Locative + सति = 'when X is (there)'."),
            [("At the wrong time", "Wrong time would need अकाले."),
             ("Without any time", "Without would need विना or निः-."),
             ("For a long time, whatever happens", "Duration would need चिरम् or an accusative.")],
            "The locative absolute: noun in -ए + सति = when there is that.",
            "X-े सति = when there is X.",
            teaches="A locative with सति is a locative absolute: सम्भवे सति (when possible), काले सति (when there is time)."),
    ],
}


NOTES_HI = {
    "30": ("विश्वास: मध्यम। ‘प्रायः’ दोनों अर्धों में से किसी पर भी लग सकता है; यहाँ दूसरे के साथ लिया गया। ‘उभयम्’ (दोनों) पंक्ति 05.05.58 के लेखन-बृंहण की ओर संकेत करता होगा, पर पाठ नहीं कहता। "
           "खुला अवलोकन (05.05.59): ‘यापनेषु’ के बाद ‘बस्तियों’ जोड़ना है या नहीं, स्वामी तय करेंगे; इस पर प्रश्न नहीं बना। "
           "संधि जाँची: निरूहा = निरूहाः (सघोष ल से पहले विसर्ग लोप); प्रायो = प्रायः (सघोष ब से पहले ओ); यापनेषूभयं = यापनेषु + उभयम्; तस्मान्नेष्टं = तस्मात् + न + इष्टम्; तेष्वनुवासनं = तेषु + अनुवासनम्।"),
    "31": ("विश्वास: निम्न। छपा ‘निवर्त्तेरन्’ = निवर्तेरन् (दोहरा र्त्त सामान्यीकृत)। ‘लौटें’ शाब्दिक है; ‘बाहर न निकलें’ केवल अनुमान। "
           "पंक्तियाँ 05.05.60-61 एक वाक्य हैं, पर 05.05.61 में मुख्य क्रिया नहीं: वाक्य आगे चलता है या कोई अंश लुप्त है। ‘आस्थाप्य’ का कर्ता (वैद्य) और ‘सः’ दोनों स्पष्ट नहीं। "
           "संधि जाँची: मृदुत्वान्न = मृदुत्वात् + न (त् + न → न्न); त्वेते = तु + एते; समूत्रैर्बस्तिभिस्तीक्ष्णैरास्थाप्य = समूत्रैः + बस्तिभिः + तीक्ष्णैः + आस्थाप्य; क्षिप्रमेव = क्षिप्रम् + एव।"),
    "32": ("विश्वास: मध्यम। पंक्तियाँ 05.05.62-63 एक वाक्य हैं; ‘स्युः’ पूरी सूची पर लागू है। छपा ‘परिकर्त्तिका’ = परिकर्तिका (र्त्त सामान्यीकृत)। "
           "text_flags: समास के भीतर ‘अर्शः’ का विसर्ग प के पहले अनियमित है (अर्थ अपरिवर्तित); इस सदस्य पर प्रश्न नहीं बना। "
           "खुला अवलोकन (05.05.62): data के हिन्दी में ‘पाण्डुता यानी फीकापन’ ठीक नहीं; पाण्डु = pale, ‘पीला’ नहीं (शब्दावली में पाण्डु = रक्ताल्पता); शब्द स्वामी तय करेंगे, इस पर प्रश्न नहीं। "
           "संधि जाँची: ज्वरश्चातिसारश्च = ज्वरः + च + अतिसारः + च; यापनात्यर्थ = यापना + अति + अर्थ।"),
    "33": ("विश्वास: मध्यम। ‘तत्र’ पंक्तियों 05.05.62-63 के उपद्रवों की ओर संकेत करता है। अरिष्ट और सीधु पेयों के नाम हैं; आगे पहचान नहीं की गई। क्षार ‘क्षार’ ही रखा गया। "
           "छपा ‘यापनांच’ = यापनाम् + च (बिना स्थान)। ‘प्रसङ्गतः’ का अर्थ ‘प्रसंग के अनुसार’ या ‘निरन्तरता से’, अनिश्चित; इस पर प्रश्न नहीं। "
           "संधि जाँची: सीध्वाद्यैः = सीधु + आद्यैः (उ + आ → वा); तत्रेष्टा = तत्र + इष्टा (अ + इ → ए); तस्मान्निषेवेत = तस्मात् + निषेवेत।"),
    "34": ("विश्वास: मध्यम। ‘मृद्वल्प’ को ‘मृदु और अल्प’ पढ़ें या ‘मृदु-अल्प’, तय नहीं। पाद = चौथाई (मानक); ‘पादहीन’ = चौथाई कम। "
           "परिहार = आहार-विहार का परहेज़; पाठ उसके सदस्य नहीं गिनाता। ‘तेषु’ = यापन बस्तियों में। क्रिया ‘है’ अनुक्त। "
           "संधि जाँची: मृद्वल्पौषध = मृदु + अल्प + औषध (उ + अ → व; अ + औ → औ); अल्पकालोपयोगाच्च = अल्पकाल + उपयोगात् + च (अ + उ → ओ; त् + च → च्च); निष्परिहारता = निः + परिहार + ता।"),
    "35": ("विश्वास: निम्न। text_flags: ‘सिद्धास्नेहात्’ का दीर्घ आ सम्भवतः छपाई की भूल; ‘सिद्धस्नेहात्’ पढ़ा गया। अपादान की वाक्य-रचना अनिश्चित: ‘पृथक्’ उसे शासित करे तो अर्थ ‘सिद्ध स्नेह से अलग’ होगा; इस पर प्रश्न नहीं। "
           "‘सर्वेषु’ = सब द्रव्यों में (पठन)। छपा ‘बस्तीन्सर्वेषु’ दो शब्द जुड़े हुए हैं। "
           "संधि जाँची: यापनार्थेषु = यापन + अर्थेषु; युंज्यात्परिहार = युञ्ज्यात् + परिहार।"),
    "36": ("विश्वास: मध्यम। अन्तिम सदस्य पर अपादान पूरी सूची पर लागू माना गया; ‘पृथक्’ से ‘प्रत्येक की एक तुला’। क्रिया (पकाना) पाठ में नहीं। "
           "पहचान: सहाचर = कटसरैया, अभीरु = शतावरी (सम्भावित); रास्ना विवादित (Pluchea lanceolata या Alpinia galanga); गोक्षुरक = गोखरू (मानक); बला की पहचान gloss में नहीं दी गई। "
           "तुला और द्रोण मान हैं; ग्राम में नहीं बदले। "
           "संधि जाँची: सहाचराभीरु = सहाचर + अभीरु; बलारास्ना = बला + रास्ना; पञ्चद्रोणावशेषिते = पञ्च + द्रोण + अवशेषिते।"),
    "37": ("विश्वास: निम्न। text_flags: ‘वक्षीरी’ पहचाना नाम नहीं, सम्भवतः ‘वंशक्षीरी’; पंक्ति 05.05.73 का समास बिगड़ा है (‘हष्टी’ सम्भवतः ‘यष्टी’), बिना विभाजन छोड़ा गया। "
           "खुला अवलोकन (05.05.72): ‘नत-वक्षीरी’ का विभाजन स्वयं अनिश्चित, इसलिए नत = तगर भी अस्थिर; इन पर प्रश्न नहीं। सम्भावित (निश्चित नहीं): ‘अंशुद्रसहा’ = ‘क्षुद्रसहा’ का विकार, जिससे महासहा-क्षुद्रसहा का जोड़ा बने। "
           "स्पष्ट: पूतशीते = छानकर ठण्डा होने पर; बिस = कमलनाल; द्राक्षा = अंगूर/मुनक्का (मानक); निदिग्धिका = कटेरी (मानक)। ये द्रव्य 05.05.77 में क्वाथ में डाले जाते हैं।"),
    "38": ("विश्वास: मध्यम। text_flags: छपे ‘आत्मगुप्तानामलकी’ में अतिरिक्त ‘न’; आत्मगुप्ता + आमलकी पढ़ा गया; इन दोनों पर प्रश्न नहीं बना। "
           "पहचान: जीवक, ऋषभक अष्टवर्ग के द्रव्य, विवादित; उदीच्य = ह्रीवेर, सुगन्धबाला (सम्भावित); चन्दन = Santalum album, खर्जूर = खजूर, ताल = ताड़ (मानक); कणा = पीपर (सम्भावित)। मज्जा = गिरी (शब्दावली के अनुसार)। "
           "संधि जाँची: जीवकर्षभक = जीवक + ऋषभक (अ + ऋ → अर्); ऋषभकोदीच्य = ऋषभक + उदीच्य (अ + उ → ओ); मृणालोत्पल = मृणाल + उत्पल; तालमज्जात्मगुप्ता = तालमज्जा + आत्मगुप्ता।"),
    "39": ("विश्वास: निम्न। text_flags: छपा ‘-आव्हयाः’ सामान्य ‘-आह्वयाः’ (नाम वाले) के लिए। ‘त्वक्पत्र’ = त्वक् और पत्र; दालचीनी-तेजपात का जोड़ा सम्भावित, पौधे का नाम पाठ में नहीं। "
           "खुला अवलोकन (05.05.76): शीतपाकी और ओदन अज्ञात; ‘ओदन’ को पौधा मानना केवल सूची से अनुमान। मेदा = ‘मेदा नामक द्रव्य’, विवादित (आटा नहीं)। "
           "‘तस्मिन्’ = 05.05.72 का छना-ठण्डा क्वाथ; ‘प्रस्थ-संमित’ द्रव्य 05.05.78 में है। "
           "संधि जाँची: क्षिपेत्तस्मिन्पृथक्च = क्षिपेत् + तस्मिन् + पृथक् + च; प्रस्थसंमितं में अन्त का ं = म्।"),
    "40": ("विश्वास: मध्यम। इस इकाई में क्रिया नहीं; वह 05.05.84 के ‘दद्यात्’ में हो सकती है, वाक्य 05.05.79-84 तक चल सकता है। "
           "‘सम्भवम्’ एकवचन नपुंसक और ‘तैलसर्पिषी’ द्विवचन: अन्वय ढीला; तेल-घी अण्डों से बने या उनके साथ पके, संस्कृत नहीं कहती, इसलिए शाब्दिक ‘उत्पन्न’ रखा। "
           "महिष = भैंसा (पुरुष पशु केवल प्रसंग से); शिखी = मोर (अन्य कलगीदार भी हो सकता है); हंस = हंस या कलहंस। बस्त = बकरा, बस्ति नहीं। "
           "संधि जाँची: मुष्कोद्भवं = मुष्क + उद्भवम् (अ + उ → ओ); हंसाण्ड = हंस + अण्ड।"),
    "41": ("विश्वास: मध्यम। पहचान: धात्री = आँवला, Phyllanthus emblica (मानक); विदारी = विदारीकन्द, Pueraria tuberosa (सम्भावित; Ipomoea digitata भी कही जाती है)। आढक आयतन का मान है। "
           "‘ब्रह्म’ का अर्थ समास के आरम्भ में निश्चित नहीं: पवित्र पाठ या किसी ढोल का नाम; उसे बढ़ाया नहीं गया, उस पर प्रश्न नहीं। भेरी = नगाड़ा, मृदङ्ग = ढोल (मानक)। "
           "तैयार की गई वस्तु (‘यत्’, नपुंसक) इस इकाई में नामित नहीं। "
           "संधि जाँची: गव्यक्षीराढकद्वयं = गव्य + क्षीर + आढक + द्वयम् (अ + आ → आ)।"),
    "42": ("विश्वास: उच्च। नपुंसक विशेषण पिछली इकाई में तैयार किए गए द्रव्य का वर्णन करते हैं; कोई संज्ञा नहीं जोड़ी गई। "
           "‘सितच्छत्र’ = सित + छत्र (छ से पहले च् का आगम)। वृषध्वज = जिसकी ध्वजा पर वृषभ, शिव का सामान्य विशेषण (मानक), पर पंक्ति स्वयं शिव नहीं कहती। पूजा का कर्ता नामित नहीं। स्कन्ध = कन्धा या पीठ। "
           "संधि जाँची: कृतच्छायं = कृत + छायम्; सितवस्त्रावगुंठितं = सित + वस्त्र + अवगुण्ठितम्।"),
    "43": ("विश्वास: मध्यम। ‘अयन्त्रणम्’ नपुंसक है, बस्ति पुंलिङ्ग, इसलिए क्रिया-विशेषण ‘बिना नियन्त्रण’ पढ़ा; क्या अनियन्त्रित (आहार, आचरण) है, नहीं कहा। देने वाला अनामित। "
           "text_flags (05.05.85): ‘प्राप्तेस्’ को ‘प्राप्तः’ (त से पहले प्राप्तस्) और ‘धनिता’ को ‘वनिता’ पढ़ा गया; खुला अवलोकन: दोनों अनुमान सम्भव, अनुवाद दोनों पर टिका है। दूसरी पंक्ति के इन शब्दों पर प्रश्न नहीं बना। "
           "संधि जाँची: दद्यात्स्नेहबस्तिमयंत्रणं = दद्यात् + स्नेहबस्तिम् + अयन्त्रणम्; तेनातिवृषतां = तेन + अतिवृषताम्।"),
    "44": ("विश्वास: मध्यम। text_flags: छपा ‘पुलित’ कोई शब्द नहीं; ‘पलित’ (सफ़ेद बाल) वली (झुर्री) का सामान्य जोड़ा है; इस शब्द पर प्रश्न नहीं बना। "
           "‘क्षत-क्षीण’ एक समास ‘चोट से क्षीण’ भी हो सकता है; यहाँ अलग सदस्य माने गए। विषमज्वर = अनियमित, अन्तराल पर लौटने वाला ज्वर (सम्भावित)। कर्ता ‘यह’ अनुक्त। "
           "संधि जाँची: कान्तश्चिरंजीवी = कान्तः + चिरंजीवी (ः → श् च से पहले); भवेत्स = भवेत् + सः।"),
    "45": ("विश्वास: मध्यम। text_flags: छपा ‘शुक़ाणां’ (नुक़्ता वाला क, र नहीं) शब्द नहीं; ‘शुक्राणाम्’ अभिप्रेत; ‘आर्त्तव’ = आर्तव (सामान्यीकरण)। इस शब्द पर प्रश्न नहीं बना। "
           "पहली पंक्ति में क्रिया नहीं, कर्ता ‘यह’ अनुक्त। रसायन = कायाकल्प की शाखा, यहाँ कायाकल्प करने वाली औषध। "
           "संधि जाँची: बस्तयोऽन्येऽपि = बस्तयः + अन्ये + अपि (अः → ओ, ए + अ → एऽ); पाक्याश्च = पाक्याः + च; नैकशः = न + एकशः (अ + ए → ऐ)।"),
    "46": ("विश्वास: उच्च। ‘सम्भवे सति’ सति-सप्तमी है। ‘सहस्रम्’ ‘वारान्’ के साथ: हज़ार बार। ‘पाचयेत्’ णिजन्त: पकवाए; क्या पकाया जाए, कहा नहीं। "
           "text_flags: ‘सपरीहारा’ में दीर्घ ई ‘परिहार’ की सामान्य वर्तनी नहीं (अर्थ अपरिवर्तित); इस शब्द पर प्रश्न नहीं बना। ‘वक्ष्यन्ते’ कर्मवाच्य भविष्यत्। "
           "संधि जाँची: शतंवारान्सहस्रं = शतम् + वारान् + सहस्रम्; सपरीहारा = सपरिहाराः (सघोष व से पहले विसर्ग लोप)।"),
}


AIDS = {
    "30": {
        "seesaw": "लेखन ↔ बृंहण: निरूह खुरचता-पतला करता है, स्नेहबस्ति पोषण करती है; यापन में दोनों।",
        "chain": {"steps": ["निरूह: लेखन", "स्नेहबस्ति: बृंहण", "यापन में दोनों", "इसलिए अनुवासन इष्ट नहीं"]},
        "sandhi": "उ + उ → ऊ: यापनेषु + उभयम् → यापनेषूभयम्; त् + न → न्न, अ + इ → ए: तस्मात् + न + इष्टम् → तस्मान्नेष्टम्।",
        "anchors": "लेखन = खुरचना, पतला करना · बृंहण = पोषण · प्रायः = अधिकतर · उभय = दोनों · इष्ट = चाहा हुआ।",
    },
    "31": {
        "frame": "समस्या: मृदु होने से बस्तियाँ न लौटें · उपाय: मूत्र-युक्त तीक्ष्ण बस्तियों से आस्थापन, शीघ्र · मुख्य क्रिया: नहीं (वाक्य अधूरा)।",
        "contrast": "मृदु (कारण) ↔ तीक्ष्ण (उपाय): मृदुता से बस्ति न लौटे, तो तीक्ष्ण और मूत्र-युक्त बस्ति।",
        "sandhi": "त् + न → न्न: मृदुत्वात् + न → मृदुत्वान्न; उ + ए → वे: तु + एते → त्वेते; ऐः → ऐर्: तीक्ष्णैः + आस्थाप्य → तीक्ष्णैरास्थाप्य।",
        "anchors": "निवर्तन = लौटना · प्रयोजित = दिया गया · स- = सहित · तीक्ष्ण = तेज़ · आस्थापन = निरूह · क्षिप्रम् = जल्दी।",
    },
    "32": {
        "diagram": {"groups": [{"label": "कारण", "items": ["यापन का अत्यधिक सेवन"]},
                               {"label": "पंक्ति १", "items": ["शोफ", "अग्निनाश", "पाण्डुत्व", "शूल", "अर्श", "परिकर्तिका"]},
                               {"label": "पंक्ति २", "items": ["ज्वर", "अतिसार"]}]},
        "pegs": "मेरा बनाया क्रम-संकेत (श्लोक का दावा नहीं): ‘सूजन से शुरू, दस्त पर ख़त्म’: शोफ … अतिसार।",
        "sandhi": "ः → श् च से पहले: ज्वरः + च → ज्वरश्च; अ + अ → आ: च + अतिसारः → चातिसारः; आ + अ → आ: यापना + अत्यर्थ → यापनात्यर्थ।",
        "anchors": "शोफ = सूजन · अग्नि = पाचक अग्नि · शूल = पीड़ा · परिकर्तिका = काटती पीड़ा · अतिसार = दस्त · अत्यर्थ = अत्यधिक।",
    },
    "33": {
        "frame": "कब: यापन के अतियोग के उपद्रवों में (तत्र) · क्या: दीपनी क्रिया · किससे: अरिष्ट, क्षार, सीधु आदि · फिर: यापन भी युक्ति से।",
        "chunks": "अरिष्टक्षारसीध्वाद्यै- | स्तत्रेष्टा दीपनी क्रिया ‖ युक्त्या तस्मान्निषेवेत | यापनांच प्रसंगतः।",
        "sandhi": "उ + आ → वा: सीधु + आद्यैः → सीध्वाद्यैः; ऐः + त → ऐस्त: आद्यैः + तत्र → आद्यैस्तत्र; अ + इ → ए: तत्र + इष्टा → तत्रेष्टा।",
        "anchors": "अरिष्ट = किण्वित औषध-पेय · सीधु = गन्ने की मदिरा · दीपन = अग्नि जगाना · युक्ति = विवेक · निषेवेत = सेवन करे।",
    },
    "34": {
        "chain": {"steps": ["मृदु, अल्प औषध का संयोग", "चौथाई कम मात्रा", "थोड़े समय तक प्रयोग", "इसलिए परहेज़ नहीं"]},
        "contrast": "पादहीन ↔ पाद-मात्र: पादहीन = चौथाई घटाकर (तीन-चौथाई बचे); केवल पाद = चौथाई भर।",
        "sandhi": "उ + अ → व: मृदु + अल्प → मृद्वल्प; अ + उ → ओ: काल + उपयोगात् → कालोपयोगात्; त् + च → च्च: उपयोगात् + च → उपयोगाच्च।",
        "anchors": "संयोग = मेल · पाद = चौथाई · हीन = कम · प्रमाण = मात्रा · परिहार = परहेज़ · -ता = -पन।",
    },
    "35": {
        "frame": "किनमें: यापन के द्रव्यों में · कैसे: अलग-अलग, या सब में · क्या: बस्तियाँ · कैसी: परिहार-रहित · क्रिया: युञ्ज्यात् (लगाए)।",
        "chunks": "द्रव्येषु यापनार्थेषु | सिद्धास्नेहात्पृथक् पृथक् ‖ बस्तीन्सर्वेषु वा युंज्या- | त्परिहारविवर्जितान्।",
        "anchors": "द्रव्य = औषध-द्रव्य · -अर्थ = के लिए · पृथक् = अलग · सर्व = सब · युञ्ज्यात् = लगाए · विवर्जित = रहित।",
    },
    "36": {
        "chain": {"steps": ["सहाचर, अभीरु, बला, रास्ना, गोक्षुरक", "प्रत्येक एक तुला", "सौ द्रोण जल में", "पाँच द्रोण शेष रहें"]},
        "sandhi": "अ + अ → आ: सहाचर + अभीरु → सहाचराभीरु; द्रोण + अवशेषिते → द्रोणावशेषिते।",
        "pegs": "मेरा बनाया संकेत (श्लोक का दावा नहीं): ‘सौ में से पाँच’: जल बीसवाँ भाग रह जाए।",
        "anchors": "तुला, द्रोण = मान · पृथक् = अलग-अलग · शत = सौ · पञ्च = पाँच · अवशेषित = शेष रहा।",
    },
    "37": {
        "frame": "समय: क्वाथ छानकर ठण्डा होने पर · स्पष्ट द्रव्य: बिस, द्राक्षा, निदिग्धिका · अनिश्चित: नत, वक्षीरी · पंक्ति २: बिगड़ा समास।",
        "anchors": "पूत = छना हुआ · शीत = ठण्डा · बिस = कमलनाल · द्राक्षा = अंगूर/मुनक्का · निदिग्धिका = कटेरी।",
        "contrast": "स्पष्ट ↔ अस्पष्ट: बिस, द्राक्षा, निदिग्धिका स्पष्ट; वक्षीरी और पंक्ति २ का समास अस्पष्ट, उन पर कुछ नहीं बनाया।",
    },
    "38": {
        "diagram": {"groups": [{"label": "पंक्ति १", "items": ["जीवक", "ऋषभक", "उदीच्य", "मृणाल", "उत्पल", "चन्दन"]},
                               {"label": "पंक्ति २", "items": ["खर्जूर", "ताल-मज्जा", "आत्मगुप्ता", "आमलकी", "कणा"]}]},
        "sandhi": "अ + ऋ → अर्: जीवक + ऋषभक → जीवकर्षभक; अ + उ → ओ: ऋषभक + उदीच्य → ऋषभकोदीच्य, मृणाल + उत्पल → मृणालोत्पल।",
        "anchors": "मृणाल = कमलनाल · उत्पल = नीलकमल · चन्दन = चन्दन · खर्जूर = खजूर · मज्जा = गिरी · कणा = पीपर (सम्भावित)।",
    },
    "39": {
        "chain": {"steps": ["पटोल, मेदा, त्वक्-पत्र, शीतपाकी, ओदन", "कल्क बनाए", "उस क्वाथ में डाले", "अलग से प्रस्थ-मापा द्रव्य"]},
        "sandhi": "त् + त → त्त: क्षिपेत् + तस्मिन् → क्षिपेत्तस्मिन्; क् + च → क्च: पृथक् + च → पृथक्च।",
        "anchors": "पटोल = परवल · कल्क = पिसी लुगदी · क्षिपेत् = डाले · तस्मिन् = उसमें · प्रस्थ = मान · संमित = मापा हुआ।",
    },
    "40": {
        "diagram": {"groups": [{"label": "मुष्क-रस (पंक्ति १)", "items": ["वराह", "महिष", "बस्त"]},
                               {"label": "अण्डे (पंक्ति २)", "items": ["शिखी", "कुक्कुट", "हंस"]},
                               {"label": "साथ में", "items": ["तैल", "सर्पिस्"]}]},
        "contrast": "बस्त ↔ बस्ति: बस्त = बकरा (यहाँ); बस्ति = एनीमा या मूत्राशय।",
        "sandhi": "अ + उ → ओ: मुष्क + उद्भवम् → मुष्कोद्भवम्; अ + अ → आ: हंस + अण्ड → हंसाण्ड।",
        "anchors": "वराह = सूअर · महिष = भैंसा · बस्त = बकरा · मुष्क = अण्डकोश · शिखी = मोर · सर्पिस् = घी।",
    },
    "41": {
        "frame": "द्रव: धात्री और विदारी का स्वरस · दूध: गाय का, दो आढक · विधि: ब्रह्म, भेरी, मृदंग की ध्वनियों से तैयार।",
        "chunks": "धात्रीविदारीस्वरसं | गव्यक्षीराढकद्वयं ‖ ब्रह्मभेरीमृदंगानां | निनादैः साधितं च यत्।",
        "anchors": "धात्री = आँवला · स्वरस = निचोड़ा रस · गव्य = गाय का · आढक = मान · भेरी = नगाड़ा · निनाद = ध्वनि।",
    },
    "42": {
        "chain": {"steps": ["श्वेत छत्र की छाया", "श्वेत वस्त्र से ढका", "हाथी के कन्धे पर रखा", "वृषध्वज की पूजा करके"]},
        "story": "मेरा बनाया दृश्य (श्लोक का दावा नहीं): एक शोभा-यात्रा सोचें: सफ़ेद छाते के नीचे, सफ़ेद कपड़े में ढका द्रव्य हाथी पर, और आगे शिव-पूजा।",
        "sandhi": "च्छ: सित + छत्र → सितच्छत्र, कृत + छाया → कृतच्छाय; अ + अ → आ: वस्त्र + अवगुण्ठित → वस्त्रावगुण्ठित।",
        "anchors": "सित = श्वेत · छत्र = छाता · अवगुण्ठित = ढका · गज = हाथी · स्कन्ध = कन्धा · वृषध्वज = शिव।",
    },
    "43": {
        "frame": "पहले: स्वस्त्ययन · फिर: स्नेहबस्ति दे, बिना नियन्त्रण · फल (अनुमानित पाठ): अतिवृषता।",
        "sandhi": "त् + स → त्स: दद्यात् + स्नेहबस्तिम् → दद्यात्स्नेहबस्तिम्; म् + अ → म: बस्तिम् + अयन्त्रणम् → बस्तिमयन्त्रणम्; अ + अ → आ: तेन + अतिवृषताम् → तेनातिवृषताम्।",
        "anchors": "स्वस्त्ययन = मंगल-विधि · दद्यात् = दे · अयन्त्रण = बिना नियन्त्रण · अतिवृषता = अत्यधिक पौरुष।",
    },
    "44": {
        "diagram": {"groups": [{"label": "वह होगा", "items": ["झुर्री-रहित", "सफ़ेद बाल-रहित (अनुमानित)", "कान्त", "चिरंजीवी"]},
                               {"label": "किसके लिए हित", "items": ["नष्टशुक्र", "क्षत", "क्षीण", "विषमज्वरी"]}]},
        "contrast": "विषम ↔ विष: विषमज्वर = अनियमित ज्वर; ‘विष’ (ज़हर) से इसका सम्बन्ध नहीं।",
        "sandhi": "ः → श् च से पहले: कान्तः + चिरंजीवी → कान्तश्चिरंजीवी; त् + स → त्स: भवेत् + सः → भवेत्स।",
        "anchors": "वली = झुर्री · कान्त = सुन्दर · चिरंजीवी = दीर्घायु · क्षत = घायल · क्षीण = दुर्बल · हित = लाभकारी।",
    },
    "45": {
        "frame": "किसके लिए: बिगड़े आर्तव-शुक्र वालों के लिए · उपाधियाँ: पुत्रदाता, रसायन · नियम: अन्य बस्तियाँ भी अनेक प्रकार से।",
        "sandhi": "अः + अ → ओऽ: बस्तयः + अन्ये → बस्तयोऽन्ये; ए + अ → एऽ: अन्ये + अपि → अन्येऽपि; अ + ए → ऐ: न + एकशः → नैकशः।",
        "anchors": "पुत्रदाता = पुत्र देने वाला · रसायन = कायाकल्प करने वाला · कल्प्य = बनाने योग्य · पाक्य = पकाने योग्य · नैकशः = अनेक प्रकार से।",
    },
    "46": {
        "frame": "पंक्ति १: सौ या हज़ार बार पकवाए, सम्भव हो तो · पंक्ति २: आगे दोषघ्न स्नेहबस्तियाँ, परिहार सहित, कही जाएँगी।",
        "chunks": "शतंवारान्सहस्रं वा | पाचयेत्संभवे सति ‖ दोषघ्नाः सपरीहारा | वक्ष्यंते स्नेहबस्तयः।",
        "anchors": "शत = सौ · सहस्र = हज़ार · वार = बार · पाचयेत् = पकवाए · सम्भव = सम्भावना · दोषघ्न = दोष-नाशक · वक्ष्यन्ते = कहे जाएँगे।",
    },
}


IMAGE_SPECS = {
    ("30", "seesaw"): {
        "file": "ka5-lekhana-brimhana-30.svg",
        "alt": "Split picture of verse 30: nirūha scraping (lekhana) on one side, sneha enema nourishing (brimhana) on the other",
        "type": "split",
        "title": "श्लोक ३०: लेखन और बृंहण",
        "cols": [["निरूह", ["लेखन", "खुरचना, पतला करना"]],
                 ["स्नेहबस्ति", ["बृंहण", "पोषण"]]],
    },
    ("32", "diagram"): {
        "file": "ka5-yapana-atiyoga-32.svg",
        "alt": "Mind map of verse 32: excessive use of yapana causes eight troubles: swelling, loss of digestive fire, pallor, colic pain, piles, cutting pains, fever, diarrhoea",
        "type": "mermaid",
        "code": ('mindmap\n  यापन का अतियोग\n    पंक्ति एक\n      शोफ\n      अग्निनाश\n      पाण्डुत्व\n      शूल\n      अर्श\n      परिकर्तिका\n'
                 '    पंक्ति दो\n      ज्वर\n      अतिसार\n'),
    },
    ("34", "chain"): {
        "file": "ka5-nishpariharata-34.svg",
        "alt": "Flowchart of verse 34: three reasons, mild and little medicine, a quantity reduced by a quarter, and use for a short time, lead to no need of restrictions in yapana",
        "type": "mermaid",
        "code": ('flowchart TD\n  A["मृदु, अल्प औषध"] --> D["यापन में परहेज़ नहीं"]\n'
                 '  B["चौथाई कम मात्रा"] --> D\n  C["थोड़े समय तक प्रयोग"] --> D\n'),
    },
    ("36", "chain"): {
        "file": "ka5-sahacaradi-kvatha-36.svg",
        "alt": "Flowchart of verse 36: five drugs (sahacara, abhiru, bala, rasna, gokshuraka), a tula of each, in a hundred dronas of water, until five dronas remain",
        "type": "mermaid",
        "code": ('flowchart TD\n  A["सहाचर, अभीरु, बला,<br/>रास्ना, गोक्षुरक"] --> B["प्रत्येक एक तुला"]\n'
                 '  B --> C["सौ द्रोण जल में"]\n  C --> D["पाँच द्रोण शेष रहें"]\n'),
    },
    ("38", "diagram"): {
        "file": "ka5-jivakadi-kalka-38.svg",
        "alt": "Table of verse 38: line 1 has six drugs (jivaka, rishabhaka, udicya, mrinala, utpala, candana); line 2 has five (date, palmyra kernel, atmagupta, amalaki, kana)",
        "type": "table",
        "title": "श्लोक ३८: कल्क के द्रव्य",
        "heads": ["पंक्ति", "द्रव्य"],
        "rows": [["पंक्ति १", "जीवक, ऋषभक, उदीच्य"], ["पंक्ति १", "मृणाल, उत्पल, चन्दन"],
                 ["पंक्ति २", "खर्जूर, ताल-मज्जा, आत्मगुप्ता"], ["पंक्ति २", "आमलकी, कणा"]],
    },
    ("39", "chain"): {
        "file": "ka5-kalka-kshepa-39.svg",
        "alt": "Flowchart of verse 39: the last paste drugs (patola, meda, bark and leaf and others) are made into a paste, put into the strained decoction, and separately a prastha-measured item is added",
        "type": "mermaid",
        "code": ('flowchart TD\n  A["पटोल, मेदा, त्वक्-पत्र<br/>आदि द्रव्य"] --> B["कल्क बनाए"]\n'
                 '  B --> C["छने क्वाथ में डाले"]\n  C --> D["अलग से प्रस्थ-मापा द्रव्य"]\n'),
    },
    ("40", "diagram"): {
        "file": "ka5-mushka-anda-40.svg",
        "alt": "Mind map of verse 40: juice from the testes of boar, buffalo, he-goat; eggs of peacock, cock, swan; with oil and ghee",
        "type": "mermaid",
        "code": ('mindmap\n  श्लोक ४० के द्रव्य\n    मुष्क-रस\n      वराह\n      महिष\n      बस्त\n'
                 '    अण्डे\n      शिखी\n      कुक्कुट\n      हंस\n    तैल और घी\n'),
    },
    ("42", "chain"): {
        "file": "ka5-gaja-skandha-42.svg",
        "alt": "The four phrases of verse 42 in the verse's order: shaded by a white umbrella, covered with white cloth, placed on an elephant's shoulder, after worshipping Vrishadhvaja",
        "type": "chain",
        "title": "श्लोक ४२: द्रव्य का सम्मान",
        "steps": ["श्वेत छत्र की छाया", "श्वेत वस्त्र से ढका", "हाथी के कन्धे पर रखा", "वृषध्वज की पूजा करके"],
    },
    ("44", "diagram"): {
        "file": "ka5-ciranjivi-hita-44.svg",
        "alt": "Split picture of verse 44: he becomes free of wrinkles, handsome, long-lived; beneficial for those with lost semen, the injured, the wasted and those with irregular fever",
        "type": "split",
        "title": "श्लोक ४४: फल और हित",
        "cols": [["वह होगा", ["झुर्री-रहित", "कान्त", "चिरंजीवी"]],
                 ["किसके लिए हित", ["नष्टशुक्र", "क्षत", "क्षीण", "विषमज्वरी"]]],
    },
}
