from helpers import mcq, match, order, fill, multi, accepts


def T(q, teaches):
    q["teaches"] = teaches
    return q


AUTHORED = {}

# ---------------------------------------------------------------- unit 88
AUTHORED["88"] = {
    "title": "द्वादशांगुलौ पाणी",
    "question": "By unit 88, how long are the hands, the middle finger, and the index and ring fingers?",
    "rule": ("The two hands (पाणी) are twelve aṅgulas; in them the middle finger (मध्यमाङ्गुलिः) is five aṅgulas; the "
             "index finger (प्रदेशिनी) and ring finger (अनामिका) are half an aṅgula less than that (ततः)."),
    "limits": ("Prose, two printed lines joined (02.08.102 and 02.08.103); copula understood. ततः = the middle finger's "
               "five aṅgulas (data's note). तत्र अपि may also mean 'even there, in each hand': no question on that nuance. "
               "Which dimension of the hand is meant is not stated."),
    "explain_hi": ("यह इकाई हाथ और अंगुलियों का माप देती है; दो छपी पंक्तियाँ जोड़ी गई हैं। "
                   "दोनों हाथ (पाणी) बारह अंगुल के हैं; उनमें भी मध्यमा अंगुली पाँच अंगुल की है। "
                   "उससे (ततः, यानी मध्यमा के पाँच अंगुल से) आधा अंगुल कम प्रदेशिनी (तर्जनी) और अनामिका हैं। "
                   "अनामिका का शब्दार्थ है ‘बिना नाम वाली’, यानी अंगूठी वाली अंगुली। "
                   "‘ततोऽर्द्धांगुलहीने’ में ततः + अर्ध की सन्धि है: अः + अ → ओऽ।"),
    "hook": "हाथ बारह, मध्यमा पाँच, उसके दोनों पड़ोसी आधा कम।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In unit 88, what does पाणि mean?",
            ("The hand", "पाणी = the two hands: द्वादशाङ्गुलौ पाणी."),
            [("The foot", "The foot would be पाद; पाणि is the hand."),
             ("The shoulder", "The shoulder would be स्कन्ध or अंस; पाणि is the hand."),
             ("The upper arm", "The arm would be बाहु; पाणि is the hand.")],
            "पाणि = hand; पाणी is its dual: the two hands.",
            "पाणि = hand."),
        order(1, "Put the parts of unit 88 in the printed order.",
              ["द्वादशांगुलौ पाणी", "तत्रापि", "पंचांगुला मध्यमांगुलिः", "ततोऽर्द्धांगुलहीने", "प्रदेशिन्यनामिके"],
              "Hands twelve aṅgulas; in them also; the middle finger five aṅgulas; half an aṅgula less than that; the index "
              "and ring fingers.",
              "पाणी → तत्रापि → मध्यमाङ्गुलिः → ततोऽर्धाङ्गुलहीने → प्रदेशिन्यनामिके."),
        match(2, "Match each word of unit 88 to its meaning.",
              [["पाणि", "hand"], ["मध्यमाङ्गुलि", "middle finger"], ["प्रदेशिनी", "index finger"],
               ["अनामिका", "ring finger"], ["हीन", "less, diminished"]],
              "पाणि = hand, मध्यमाङ्गुलि = middle finger, प्रदेशिनी = index finger, अनामिका = ring finger, हीन = less.",
              "पाणि, मध्यमाङ्गुलि, प्रदेशिनी, अनामिका, हीन.", role="extend",
              teaches="अनामिका, literally 'the nameless one', is the ring finger; प्रदेशिनी, 'the pointer', is the index finger."),
        mcq("discriminate", 3, "By unit 88, how long are the index and ring fingers?",
            ("Half an aṅgula less than the middle finger",
             "ततोऽर्धाङ्गुलहीने: ततः = than the middle finger's five aṅgulas."),
            [("Half an aṅgula more than the middle finger", "The word is हीन, less, not more."),
             ("Exactly as long as the middle finger is", "They are हीन, diminished by half an aṅgula."),
             ("Half an aṅgula less than the whole hand", "ततः points to the middle finger's five aṅgulas, not the hand.")],
            "Middle finger five aṅgulas; index and ring fingers half an aṅgula less than that.",
            "ततः (than that) + अर्धाङ्गुलहीने (less by half an aṅgula)."),
        mcq("apply", 4, "Why is ततः printed ततो before अर्द्ध- in unit 88?",
            ("अः before अ → ओ, and that अ is elided","ततः + अर्ध- → ततोऽर्ध-: the avagraha marks the elided अ."),
            [("अः before any vowel at all → ओ", "Not any: before a vowel other than अ, अः becomes अ."),
             ("आः before the vowel अ → ओ", "ततः ends in अः, and आः only drops its visarga before a voiced sound."),
             ("ततो is the stem form of the word", "The adverb is ततः; the ओ comes only from sandhi.")],
            "ततः + अर्धाङ्गुलहीने → ततोऽर्धाङ्गुलहीने.",
            "अः + अ → ओऽ."),
        mcq("transfer", 5, "By the pattern of प्रदेशिनी + अनामिके → प्रदेशिन्यनामिके, how is देवी + अपि joined in a new example?",
            ("देव्यपि", "ई before a different vowel → य्: देवी + अपि → देव्यपि."),
            [("देवीपि", "The अ of अपि cannot simply vanish."),
             ("देवेपि", "ई + अ does not give ए."),
             ("देवीयपि", "ई is replaced by य्; it does not stay beside it.")],
            "देवी + अपि = देव्यपि, like प्रदेशिनी + अनामिके = प्रदेशिन्यनामिके.",
            "ई + unlike vowel → य्.",
            teaches="इ/ई before a different vowel becomes य्: प्रदेशिनी + अनामिके → प्रदेशिन्यनामिके."),
    ],
}

# ---------------------------------------------------------------- unit 89
AUTHORED["89"] = {
    "title": "सार्द्धत्र्यंगुलौ कनिष्ठिकांगुष्ठौ",
    "question": "By unit 89, how long are the little finger and the thumb?",
    "rule": "The little finger (कनिष्ठिका) and the thumb (अङ्गुष्ठ) are three and a half aṅgulas (सार्धत्र्यङ्गुलौ).",
    "limits": ("Prose, one printed line, no verb (copula understood). Printed सार्द्ध = सार्ध (doubling after r, a print "
               "habit). The dimension (length) is understood, not printed."),
    "explain_hi": ("यह इकाई बाकी दो अंगुलियों का माप देती है: कनिष्ठिका (छोटी अंगुली) और अंगुष्ठ (अँगूठा) साढ़े तीन अंगुल के हैं। "
                   "‘सार्ध’ = स + अर्ध, यानी आधे के साथ; ‘सार्धत्र्यङ्गुल’ = साढ़े तीन अंगुल। "
                   "‘कनिष्ठिकाङ्गुष्ठौ’ दो अंगुलियों का द्वन्द्व समास है, इसलिए द्विवचन। "
                   "छपा ‘सार्द्ध’ र के बाद द्वित्व की छपाई-आदत है, शब्द ‘सार्ध’ है।"),
    "hook": "छोटी अंगुली और अँगूठा: साढ़े तीन-साढ़े तीन।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 89, what does अङ्गुष्ठ mean?",
            ("The thumb", "अङ्गुष्ठ = thumb: कनिष्ठिका-अङ्गुष्ठौ."),
            [("The little finger", "The little finger is कनिष्ठिका, the other member."),
             ("The ring finger", "The ring finger is अनामिका, not अङ्गुष्ठ."),
             ("The fingernail", "A nail would be नख; अङ्गुष्ठ is the thumb.")],
            "अङ्गुष्ठ = thumb.",
            "अङ्गुष्ठ = thumb."),
        match(1, "Match each part of unit 89 to its meaning.",
              [["कनिष्ठिका", "little finger"], ["अङ्गुष्ठ", "thumb"], ["सार्ध", "with a half"],
               ["अङ्गुल", "finger-breadth"]],
              "कनिष्ठिका = little finger, अङ्गुष्ठ = thumb, सार्ध = with a half, अङ्गुल = finger-breadth.",
              "कनिष्ठिका, अङ्गुष्ठ, सार्ध, अङ्गुल."),
        fill(2, "The numeral meaning 'three' inside the first word of unit 89 is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("त्रि"),
             "त्रि = three: सार्ध + त्रि + अङ्गुलौ → सार्धत्र्यङ्गुलौ, three and a half aṅgulas.",
             "Before a vowel the final इ of त्रि becomes य्: त्रि + अङ्गुल → त्र्यङ्गुल.",
             "त्रि = three."),
        mcq("discriminate", 3, "By unit 89, what measure is given for the little finger and the thumb?",
            ("Three and a half aṅgulas", "सार्धत्र्यङ्गुलौ: with a half, three aṅgulas."),
            [("Two and a half aṅgulas", "The numeral is त्रि, three, not two."),
             ("Four and a half aṅgulas", "The numeral is त्रि, three, not four."),
             ("Three aṅgulas, no half", "सार्ध adds a half: three and a half.")],
            "सार्ध (with a half) + त्रि (three) + अङ्गुलौ.",
            "सार्धत्र्यङ्गुल = 3½ aṅgulas."),
        mcq("apply", 4, "Why is त्रि + अङ्गुलौ printed त्र्यंगुलौ in unit 89?",
            ("इ before a different vowel → य्", "त्रि + अङ्गुलौ → त्र्यङ्गुलौ: the इ becomes the semivowel य्."),
            [("इ before any consonant → य्", "Before a consonant इ stays; य् arises only before a vowel."),
             ("इ + अ → ए in a compound", "That is अ + इ → ए; here इ stands first, so it gives य्."),
             ("इ is dropped before the अ", "इ is not dropped; it becomes the semivowel य्.")],
            "त्रि + अङ्गुलौ: इ before a different vowel → य्.",
            "इ + unlike vowel → य्."),
        mcq("transfer", 5, "By the pattern of त्रि + अङ्गुलौ → त्र्यङ्गुलौ, how is इति + आदि joined in a new example?",
            ("इत्यादि", "इ before a different vowel → य्: इति + आदि → इत्यादि."),
            [("इतादि", "The इ is not dropped; it becomes य्."),
             ("इतेदि", "इ + आ does not give ए."),
             ("इतियादि", "इ is replaced by य्; it does not stay beside it.")],
            "इति + आदि = इत्यादि, like त्रि + अङ्गुलौ = त्र्यङ्गुलौ.",
            "इ + unlike vowel → य्.",
            teaches="इ before a different vowel becomes य्: त्रि + अङ्गुलौ → त्र्यङ्गुलौ."),
    ],
}

# ---------------------------------------------------------------- unit 90
AUTHORED["90"] = {
    "title": "चतुरुत्सेधा द्वाविंशतिपरिणाहा शिरोधरा",
    "question": "By unit 90, what are the height and girth of the neck and of the face?",
    "rule": ("The neck (शिरोधरा) is four in height (उत्सेध) and twenty-two in girth (परिणाह); the face (आनन) is twelve "
             "in height and twenty-four in girth."),
    "limits": ("Prose, two printed lines joined (02.08.105 and 02.08.106); copula understood. Only numerals are printed: "
               "the unit aṅgula is understood (data's note). आनन = face; the mouth (आस्य) comes in unit 91."),
    "explain_hi": ("शिरोधरा (गर्दन, शब्दार्थ ‘सिर को धारण करने वाली’) ऊँचाई (उत्सेध) में चार और घेरे (परिणाह) में बाईस है। "
                   "आनन (चेहरा) ऊँचाई में बारह और घेरे में चौबीस है। "
                   "यहाँ केवल संख्याएँ छपी हैं; इकाई ‘अंगुल’ समझी जाती है। "
                   "शिरोधरा स्त्रीलिंग है, इसलिए विशेषण -उत्सेधा, -परिणाहा; आनन नपुंसक है, इसलिए -उत्सेधम्, -परिणाहम्। "
                   "‘द्वादशोत्सेधं’ में द्वादश + उत्सेधम् (अ + उ → ओ) है।"),
    "hook": "गर्दन ४ ऊँची, २२ घेरा; चेहरा १२ ऊँचा, २४ घेरा।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 90, what does शिरोधरा mean?",
            ("The neck", "शिरोधरा, the 'head-bearer', is the neck (standard)."),
            [("The head", "The head is शिरस्; शिरोधरा is what bears it."),
             ("The forehead", "The forehead is ललाट, not शिरोधरा."),
             ("The jaw", "The jaw is हनु, not शिरोधरा.")],
            "शिरस् (head) + धरा (bearing): the neck.",
            "शिरोधरा = neck."),
        order(1, "Put the words of unit 90 in the printed order.",
              ["चतुरुत्सेधा", "द्वाविंशतिपरिणाहा", "शिरोधरा", "द्वादशोत्सेधं", "चतुर्विंशतिपरिणाहम्", "आननं"],
              "Four in height, twenty-two in girth, the neck; twelve in height, twenty-four in girth, the face.",
              "Each line: height → girth → the body part."),
        match(2, "Match each word of unit 90 to its meaning.",
              [["उत्सेध", "height"], ["परिणाह", "girth"], ["शिरोधरा", "neck"], ["आनन", "face"],
               ["द्वाविंशति", "twenty-two"]],
              "उत्सेध = height, परिणाह = girth, शिरोधरा = neck, आनन = face, द्वाविंशति = twenty-two.",
              "उत्सेध, परिणाह, शिरोधरा, आनन, द्वाविंशति.", role="extend",
              teaches="उत्सेध is height and परिणाह is girth (circumference): each line of unit 90 gives both."),
        mcq("discriminate", 3, "By unit 90, what are the height and girth of the face (आनन)?",
            ("Twelve and twenty-four", "द्वादशोत्सेधं चतुर्विंशतिपरिणाहमाननं."),
            [("Four and twenty-two", "Four and twenty-two belong to the neck."),
             ("Twelve and twenty-two", "Twenty-two is the girth of the neck, not the face."),
             ("Four and twenty-four", "Four is the height of the neck, not the face.")],
            "Face: twelve in height, twenty-four in girth.",
            "आनन: उत्सेध १२, परिणाह २४."),
        mcq("apply", 4, "Why does unit 90 print -उत्सेधा with शिरोधरा but -उत्सेधं with आननं?",
            ("Each adjective takes its noun's gender", "शिरोधरा is feminine (-आ), आनन is neuter (-म्)."),
            [("The neck is plural, the face is singular", "Both nouns are singular here."),
             ("The -आ marks height, the -म् marks girth", "Both lines have both endings by gender, not by dimension."),
             ("The -आ is a sandhi form before श", "-आ is the feminine ending, not a sandhi change.")],
            "-उत्सेधा agrees with feminine शिरोधरा; -उत्सेधम् with neuter आननम्.",
            "A bahuvrīhi adjective takes the gender of its noun."),
        mcq("transfer", 5, "By the pattern of द्वादश + उत्सेधम् → द्वादशोत्सेधम्, how is सूर्य + उदयः joined in a new example?",
            ("सूर्योदयः", "अ + उ → ओ: सूर्य + उदयः → सूर्योदयः."),
            [("सूर्यौदयः", "औ comes from अ + ओ or औ, not from अ + उ."),
             ("सूर्युदयः", "The अ does not vanish; अ + उ gives ओ."),
             ("सूर्यवुदयः", "व् comes from उ before a vowel; here अ stands first.")],
            "सूर्य + उदयः = सूर्योदयः, like द्वादश + उत्सेधम् = द्वादशोत्सेधम्.",
            "अ + उ → ओ.",
            teaches="अ/आ + उ/ऊ → ओ: द्वादश + उत्सेधम् → द्वादशोत्सेधम्."),
    ],
}

# ---------------------------------------------------------------- unit 91
AUTHORED["91"] = {
    "title": "पंचांगुलमास्यं",
    "question": "By unit 91, what measure is given for the mouth?",
    "rule": "The mouth (आस्य) is of five aṅgulas (पञ्चाङ्गुलम्).",
    "limits": ("Prose, one short printed line, no verb (copula understood). Which dimension of the mouth (opening, width) "
               "is not stated: no question on it. The face (आनन) was measured in unit 90."),
    "explain_hi": ("यह छोटी इकाई केवल इतना कहती है: आस्य (मुँह) पाँच अंगुल का है। "
                   "कौन-सा माप (खुलाव या चौड़ाई) है, यह नहीं कहा गया। "
                   "‘पंचांगुल’ में पञ्च + अङ्गुल (अ + अ → आ) है, और अङ्गुलम् + आस्यम् में म् स्वर से जुड़ गया: पंचांगुलमास्यं। "
                   "यहाँ इकाई ‘अंगुल’ छपी हुई है।"),
    "hook": "मुँह: पाँच अंगुल।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 91, what does आस्य mean?",
            ("The mouth", "आस्य = mouth: पञ्चाङ्गुलम् आस्यम्."),
            [("The eye", "The eye would be नेत्र; आस्य is the mouth."),
             ("The ear", "The ear would be कर्ण; आस्य is the mouth."),
             ("The neck", "The neck would be शिरोधरा; आस्य is the mouth.")],
            "आस्य = mouth.",
            "आस्य = mouth."),
        match(1, "Match each part of unit 91 to its meaning.",
              [["पञ्च", "five"], ["अङ्गुल", "finger-breadth"], ["आस्य", "mouth"]],
              "पञ्च = five, अङ्गुल = finger-breadth, आस्य = mouth.",
              "पञ्च, अङ्गुल, आस्य."),
        T(multi("extend", 2, "Which statements fit unit 91?",
                [("It gives the girth of the mouth", "No: no dimension is named, so not girth."),
                 ("It gives five aṅgulas for the mouth", "Yes: पञ्चाङ्गुलम् आस्यम्."),
                 ("It prints the unit aṅgula itself", "Yes: अङ्गुल is printed inside पंचांगुलम्."),
                 ("It says the mouth equals the face", "No: the face (आनन) has its own measures in unit 90.")],
                [1, 2],
                "Five aṅgulas for the mouth, the unit printed, the dimension unstated.",
                "पंचांगुलमास्यं: mouth = five aṅgulas."),
          "When the dimension is not printed, the card does not supply one: unit 91 gives only 'five aṅgulas'."),
        mcq("discriminate", 3, "Which split of पंचांगुलमास्यं in unit 91 is right?",
            ("पञ्च + अङ्गुलम् + आस्यम्", "अ + अ → आ; the म् of अङ्गुलम् joins the vowel of आस्यम्."),
            [("पञ्चा + अङ्गुलम् + आस्यम्", "पञ्चा is not a form; the numeral is पञ्च."),
             ("पञ्च + अङ्गुलमा + अस्यम्", "अङ्गुलमा is not a form; the word is अङ्गुलम्."),
             ("पञ्च + गुलम् + आस्यम्", "गुलम् is not the word; the unit is अङ्गुल.")],
            "पञ्च (five) + अङ्गुलम् (aṅgulas) + आस्यम् (mouth).",
            "अ + अ → आ; म् + vowel joins."),
        mcq("apply", 4, "Why is पञ्च + अङ्गुलम् printed पंचांगुलम् in unit 91?",
            ("अ + अ → आ", "Two short अ join into long आ: पञ्च + अङ्गुलम् → पञ्चाङ्गुलम्."),
            [("अ + अ → ए", "ए comes from अ + इ, not from अ + अ."),
             ("अ + अ → औ", "औ comes from अ + ओ or औ, not from अ + अ."),
             ("The first अ is lost", "Nothing is lost: the two अ become one long आ.")],
            "पञ्च + अङ्गुलम्: अ + अ → आ.",
            "अ + अ → आ."),
        mcq("transfer", 5, "By the pattern of पञ्च + अङ्गुलम् → पञ्चाङ्गुलम्, how is सप्त + अश्वाः joined in a new example?",
            ("सप्ताश्वाः", "अ + अ → आ: सप्त + अश्वाः → सप्ताश्वाः."),
            [("सप्तश्वाः", "The two अ give a long आ; one cannot simply vanish."),
             ("सप्तेश्वाः", "ए comes from अ + इ, not from अ + अ."),
             ("सप्तोश्वाः", "ओ comes from अ + उ, not from अ + अ.")],
            "सप्त + अश्वाः = सप्ताश्वाः, like पञ्च + अङ्गुलम् = पञ्चाङ्गुलम्.",
            "अ + अ → आ.",
            teaches="Two short अ across a join become one long आ: पञ्च + अङ्गुलम् → पञ्चाङ्गुलम्."),
    ],
}

# ---------------------------------------------------------------- unit 92
AUTHORED["92"] = {
    "title": "चतुरंगुलंपृथक्",
    "question": "By unit 92, which parts of the face are four aṅgulas each?",
    "rule": ("Four aṅgulas, separately (चतुरङ्गुलं पृथक्): the chin (चिबुक), the lip (ओष्ठ), the nose (नासा), probably "
             "the interval between the eyes (दृष्ट्यन्तर), the ear (कर्ण) and the forehead (ललाट)."),
    "limits": ("Text flag: the doubled द् in नासाद्दृष्ट्यंतर may be a slip or नासात् + दृष्ट्यन्तर; the eye interval is "
               "probable, and नासा-दृष्ट्यन्तर as one item is possible. No question on the nose, the eye interval or the "
               "number of items."),
    "explain_hi": ("‘चार अंगुल, अलग-अलग’: चिबुक (ठुड्डी), ओष्ठ (होंठ), नासा (नाक), सम्भवतः दृष्टि-अन्तर (आँखों के बीच की दूरी), "
                   "कर्ण (कान) और ललाट (माथा)। ‘पृथक्’ का अर्थ है कि हर एक अंग चार अंगुल का है, सब मिलकर नहीं। "
                   "छपे ‘नासाद्दृष्ट्यंतर’ में दोहरा द् है: यह भूल से द्वित्व हो सकता है या नासात् + दृष्ट्यन्तर, इसलिए नाक और "
                   "दृष्टि-अन्तर का भाग पक्का नहीं। ‘चिबुकौष्ठ’ में चिबुक + ओष्ठ (अ + ओ → औ) है।"),
    "hook": "ठुड्डी, होंठ, कान, माथा: हर एक चार अंगुल।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 92, what does ललाट mean?",
            ("The forehead", "ललाट = forehead (standard)."),
            [("The cheek", "The cheek would be कपोल or गण्ड; ललाट is the forehead."),
             ("The jaw", "The jaw would be हनु; ललाट is the forehead."),
             ("The scalp", "The scalp is not ललाट; ललाट is the forehead.")],
            "ललाट = forehead.",
            "ललाट = forehead."),
        order(1, "Put these sure items of unit 92 in the printed order.",
              ["चिबुक", "ओष्ठ", "कर्ण", "ललाट"],
              "The compound runs chin, lip, (nose, eye interval), ear, forehead; the four sure items keep that order.",
              "चिबुक → ओष्ठ → कर्ण → ललाट."),
        match(2, "Match each sure word of unit 92 to its meaning.",
              [["चिबुक", "chin"], ["ओष्ठ", "lip"], ["कर्ण", "ear"], ["ललाट", "forehead"], ["पृथक्", "separately"]],
              "चिबुक = chin, ओष्ठ = lip, कर्ण = ear, ललाट = forehead, पृथक् = separately.",
              "चिबुक, ओष्ठ, कर्ण, ललाट, पृथक्.", role="extend",
              teaches="पृथक् (separately) makes the measure apply to each member of the list, one by one."),
        mcq("discriminate", 3, "By unit 92, what does पृथक् tell about the four aṅgulas?",
            ("Each item is four aṅgulas", "पृथक् = separately: every member of the list has four aṅgulas."),
            [("All items together are four", "That would ignore पृथक्, which means separately."),
             ("Only the first item is four", "पृथक् spreads the measure to every item, not one."),
             ("Four is shared by each two", "The measure is not shared; each has four aṅgulas.")],
            "चतुरङ्गुलं पृथक्: four aṅgulas, each separately.",
            "पृथक् = separately, each."),
        mcq("apply", 4, "Why does चिबुक + ओष्ठ appear as चिबुकौष्ठ in unit 92?",
            ("अ + ओ → औ", "चिबुक + ओष्ठ → चिबुकौष्ठ, as printed."),
            [("अ + ओ → अव्", "अव् comes from ओ before a vowel; here अ stands first."),
             ("चिबुक ends in ओ", "The word is चिबुक, ending in अ."),
             ("अ + ओ → आ", "आ comes from अ + अ or आ, not from अ + ओ.")],
            "चिबुक + ओष्ठ: अ + ओ → औ (in a compound before ओष्ठ, चिबुकोष्ठ is also allowed; the print has औ).",
            "अ + ओ → औ."),
        mcq("transfer", 5, "By the pattern of चिबुक + ओष्ठ → चिबुकौष्ठ, how is वन + ओषधि joined in a new example?",
            ("वनौषधि", "अ + ओ → औ: वन + ओषधि → वनौषधि."),
            [("वनाषधि", "आ comes from अ + अ or आ, not from अ + ओ."),
             ("वनवोषधि", "व् comes from उ before a vowel; here the vowels are अ and ओ."),
             ("वनैषधि", "ऐ comes from अ + ए or ऐ, not from अ + ओ.")],
            "वन + ओषधि = वनौषधि, like चिबुक + ओष्ठ = चिबुकौष्ठ.",
            "अ + ओ → औ.",
            teaches="अ/आ + ओ/औ → औ: चिबुक + ओष्ठ → चिबुकौष्ठ."),
    ],
}

# ---------------------------------------------------------------- unit 93
AUTHORED["93"] = {
    "title": "त्रिभागांगुलविस्तारा नासापुटमर्यादा",
    "question": "By unit 93, what are the measures of the nostril border and of the eye?",
    "rule": ("The border of the nostril (नासापुटमर्यादा) is a third part of an aṅgula in breadth (त्रिभागाङ्गुलविस्तारा); "
             "the eye (नेत्र) is two aṅgulas long (द्व्यङ्गुलायतम्) and broad by the belly of the thumb (अङ्गुष्ठोदरविस्तृतम्)."),
    "limits": ("Prose, two printed lines joined (02.08.109 and 02.08.110). त्रिभाग is taken as a third part; 'three parts' "
               "is an alternative: no question on that value. अङ्गुष्ठोदर = the fleshy middle of the thumb; no further measure "
               "is given. Here उदर is a body part, not a disease."),
    "explain_hi": ("नासापुट (नथुना) की मर्यादा (किनारा) चौड़ाई में अंगुल का तिहाई भाग है; ‘त्रिभाग’ को ‘तीन भाग’ भी पढ़ा जा सकता है, "
                   "इसलिए उस संख्या पर प्रश्न नहीं। नेत्र (आँख) दो अंगुल लम्बी है और अँगूठे के उदर, यानी उसके मांसल बीच के भाग, जितनी चौड़ी है। "
                   "यहाँ ‘उदर’ अँगूठे का भाग है, न पेट, न रोग। "
                   "-विस्तारा स्त्रीलिंग मर्यादा से और -विस्तृतम् नपुंसक नेत्रम् से मेल खाते हैं।"),
    "hook": "आँख: दो अंगुल लम्बी, अँगूठे के पेट जितनी चौड़ी।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 93, what does नेत्र mean?",
            ("The eye", "नेत्र = eye: द्व्यङ्गुलायतम् ... नेत्रम्."),
            [("The nostril", "The nostril is नासापुट, the first line's word."),
             ("The eyebrow", "The eyebrow would be भ्रू; नेत्र is the eye."),
             ("The eyelid", "The eyelid would be वर्त्म; नेत्र is the eye.")],
            "नेत्र = eye.",
            "नेत्र = eye."),
        order(1, "Put the words of unit 93 in the printed order.",
              ["त्रिभागांगुलविस्तारा", "नासापुटमर्यादा", "द्व्यंगुलायतम्", "अंगुष्ठोदरविस्तृतं", "नेत्रं"],
              "Breadth of a third part of an aṅgula; the nostril border; two aṅgulas long; broad by the thumb's belly; the eye.",
              "Each line: measure(s) first, the part last."),
        match(2, "Match each word of unit 93 to its meaning.",
              [["नासापुट", "nostril"], ["मर्यादा", "border"], ["आयत", "long"], ["विस्तृत", "broad"],
               ["अङ्गुष्ठोदर", "the thumb's fleshy middle"]],
              "नासापुट = nostril, मर्यादा = border, आयत = long, विस्तृत = broad, अङ्गुष्ठोदर = the belly of the thumb.",
              "नासापुट, मर्यादा, आयत, विस्तृत, अङ्गुष्ठोदर.", role="extend",
              teaches="उदर, 'belly', can name the fleshy middle of a part: अङ्गुष्ठोदर is the belly of the thumb."),
        mcq("discriminate", 3, "By unit 93, how broad is the eye?",
            ("As broad as the belly of the thumb", "अङ्गुष्ठोदरविस्तृतम्: broad by the thumb's belly."),
            [("Two aṅgulas, the same as its length", "Two aṅgulas is the eye's length (आयत), not its breadth."),
             ("As broad as the nostril's border", "The nostril border has its own measure in line 1."),
             ("As broad as the middle finger is", "The middle finger is not named in this unit.")],
            "Eye: two aṅgulas long; broad by the belly of the thumb.",
            "आयत = long, विस्तृत = broad."),
        mcq("apply", 4, "In अङ्गुष्ठोदर of unit 93, what is उदर?",
            ("The fleshy middle of the thumb", "Here उदर is a body part of the thumb (data's note)."),
            [("The belly of the whole body", "The compound is अङ्गुष्ठ-उदर: the thumb's belly, not the body's."),
             ("A disease of the abdomen", "Here उदर is not a disease; it is part of the thumb."),
             ("The hard tip of the thumb", "उदर, belly, is the fleshy middle, not the tip.")],
            "अङ्गुष्ठ (thumb) + उदर (belly): the fleshy middle of the thumb.",
            "अङ्गुष्ठोदर = the thumb's belly."),
        mcq("transfer", 5, "By the pattern of -विस्तारा मर्यादा and -विस्तृतं नेत्रं, which form fits ____ मुखम् (a broad face) in a new example?",
            ("विस्तृतम्", "मुखम् is neuter singular, so the adjective is विस्तृतम्, like विस्तृतं नेत्रम्."),
            [("विस्तृता", "-आ is feminine, like -विस्तारा मर्यादा; मुखम् is neuter."),
             ("विस्तृतः", "-अः is masculine; मुखम् is neuter."),
             ("विस्तृताः", "-आः is plural; मुखम् is singular.")],
            "विस्तृतं मुखम्, like अङ्गुष्ठोदरविस्तृतं नेत्रम्.",
            "An adjective agrees with its noun in gender, number and case.",
            teaches="Adjectives agree with their noun: feminine मर्यादा takes -विस्तारा, neuter नेत्रम् takes -विस्तृतम्."),
    ],
}

# ---------------------------------------------------------------- unit 94
AUTHORED["94"] = {
    "title": "तत्र शुक्लतृतीयांशः कृष्णः",
    "question": "By unit 94, how are the white, the black and the dṛṣṭi of the eye related in size?",
    "rule": ("In it (तत्र), the black (कृष्णः) is a third portion of the white (शुक्लतृतीयांशः); the dṛṣṭi, probably the "
             "pupil, is a ninth portion of the black (कृष्णात् नवमांशा), of the size of a masūra-dala (मसूरदलमात्रा)."),
    "limits": ("Prose, one printed line. तृतीयांश = one third or 'the third portion' (data). दृष्टि = the seeing part, "
               "probably the pupil. masūra = lentil, Lens culinaris (standard); दल may be half-seed, split or leaf: no "
               "question on दल. तत्र = 'in it', read as the eye of unit 93."),
    "explain_hi": ("उसमें (आँख में) कृष्ण यानी काला भाग शुक्ल यानी सफेद भाग का तृतीयांश है। "
                   "कृष्ण का नवाँ अंश दृष्टि है, जो सम्भवतः पुतली है, और उसका माप मसूर के दल जितना है। "
                   "मसूर = मसूर (Lens culinaris, मानक); ‘दल’ का अर्थ आधा दाना, फाँक या पत्ता, अनिश्चित है। "
                   "क्रम याद रखें: शुक्ल → उसका तृतीयांश कृष्ण → उसका नवमांश दृष्टि। "
                   "‘नवमांशा’ का -आ स्त्रीलिंग दृष्टि से मेल खाता है।"),
    "hook": "सफेद का तिहाई काला, काले का नवाँ भाग दृष्टि।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In unit 94, what is शुक्ल in the eye?",
            ("The white part", "शुक्ल = white: the white part of the eye."),
            [("The black part", "The black part is कृष्ण, the other word."),
             ("The eyelid", "The eyelid is not named in this unit."),
             ("The eyelash", "The eyelash is not named in this unit.")],
            "शुक्ल = the white part; कृष्ण = the black part.",
            "शुक्ल = white."),
        order(1, "Put the words of unit 94 in the printed order.",
              ["तत्र", "शुक्लतृतीयांशः", "कृष्णः", "कृष्णान्नवमांशा", "मसूरदलमात्रा", "दृष्टिः"],
              "In it; a third portion of the white; the black; a ninth portion of the black; of masūra-dala size; the dṛṣṭi.",
              "तत्र → शुक्लतृतीयांशः → कृष्णः → कृष्णान्नवमांशा → मसूरदलमात्रा → दृष्टिः."),
        match(2, "Match each word of unit 94 to its meaning.",
              [["शुक्ल", "white"], ["कृष्ण", "black"], ["तृतीयांश", "a third portion"], ["नवमांश", "a ninth portion"],
               ["मसूर", "lentil"]],
              "शुक्ल = white, कृष्ण = black, तृतीयांश = a third portion, नवमांश = a ninth portion, मसूर = lentil.",
              "शुक्ल, कृष्ण, तृतीयांश, नवमांश, मसूर.", role="extend",
              teaches="तृतीय + अंश = a third portion, नवम + अंश = a ninth portion: ordinal + अंश names a fraction."),
        mcq("discriminate", 3, "By unit 94, the dṛṣṭi is what portion of the black?",
            ("A ninth portion", "कृष्णात् नवमांशा दृष्टिः: a ninth portion of the black."),
            [("A third portion", "A third portion is the black's share of the white."),
             ("A half portion", "Half would be अर्ध; the line says नवम, ninth."),
             ("A fourth portion", "Fourth would be चतुर्थ; the line says नवम, ninth.")],
            "White → black (a third portion) → dṛṣṭi (a ninth portion of the black).",
            "नवमांश = a ninth portion."),
        mcq("apply", 4, "By unit 94, the black is a third portion of what?",
            ("Of the white", "शुक्लतृतीयांशः कृष्णः: the black is a third portion of the white."),
            [("Of the dṛṣṭi", "The dṛṣṭi is the smaller one: a ninth of the black."),
             ("Of the eyebrow", "The eyebrow is not named in this unit."),
             ("Of the lentil", "The lentil gives the dṛṣṭi's size, not the black's.")],
            "शुक्ल-तृतीय-अंशः: a third portion of the white.",
            "शुक्लतृतीयांश = a third portion of the white."),
        mcq("transfer", 5, "By the pattern of तृतीय + अंशः → तृतीयांशः, how is चतुर्थ + अंशः joined in a new example?",
            ("चतुर्थांशः", "अ + अ → आ: चतुर्थ + अंशः → चतुर्थांशः, a fourth portion."),
            [("चतुर्थंशः", "The two अ give a long आ; one cannot simply vanish."),
             ("चतुर्थेंशः", "ए comes from अ + इ, not from अ + अ."),
             ("चतुर्थोंशः", "ओ comes from अ + उ, not from अ + अ.")],
            "चतुर्थ + अंशः = चतुर्थांशः, like तृतीय + अंशः = तृतीयांशः.",
            "अ + अ → आ.",
            teaches="Ordinal + अंश names a fraction, joined अ + अ → आ: तृतीय + अंशः → तृतीयांशः."),
    ],
}

# ---------------------------------------------------------------- unit 95
AUTHORED["95"] = {
    "title": "षडंगुलोत्सेधं द्वात्रिंशत्परिणाहं",
    "question": "By unit 95, what are the head's height and girth, and how many aṅgulas is the whole body?",
    "rule": ("Six aṅgulas in height (षडङ्गुलोत्सेधम्) and thirty-two in girth (द्वात्रिंशत्परिणाहम्): the head (शिरः). "
             "The whole body (सर्वं शरीरम्), again, is eighty-four aṅgulas (अङ्गुलानि चतुरशीतिः)."),
    "limits": ("Prose, two printed lines joined (02.08.112 and 02.08.113); no verb. Text flag: printed शिरइति is regularly "
               "शिर इति (spacing). The data's note marks a GROUPING with the unit before; no question on it. अङ्गुलानि "
               "(plural) and चतुरशीतिः (singular) differ in number: a measure equation (data)."),
    "explain_hi": ("सिर (शिरः) ऊँचाई में छह अंगुल और घेरे में बत्तीस है; ‘इति’ कथन को समाप्त करता है। "
                   "फिर, सारा शरीर चौरासी अंगुल है। डेटा की टिप्पणी इसे पिछली इकाई से जुड़ा (GROUPING) मानती है। "
                   "‘षडङ्गुल’ में षट् + अङ्गुल है: स्वर से पहले ट् → ड्। "
                   "छपा ‘शिरइति’ नियमित रूप से ‘शिर इति’ है (अः के बाद अ से भिन्न स्वर हो तो विसर्ग लुप्त, बीच की जगह बनी रहती है)। "
                   "अङ्गुलानि बहुवचन और चतुरशीतिः एकवचन हैं; यह माप का समीकरण है।"),
    "hook": "सिर: छह ऊँचा, बत्तीस घेरा; पूरा शरीर चौरासी अंगुल।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In unit 95, what does चतुरशीति mean?",
            ("Eighty-four", "चतुर् (four) + अशीति (eighty) = eighty-four."),
            [("Forty-eight", "Forty-eight would be अष्टचत्वारिंशत्."),
             ("Twenty-four", "Twenty-four would be चतुर्विंशति."),
             ("Fourteen", "Fourteen would be चतुर्दश.")],
            "चतुरशीति = 84.",
            "चतुरशीति = eighty-four."),
        order(1, "Put the parts of unit 95 in the printed order.",
              ["षडंगुलोत्सेधं", "द्वात्रिंशत्परिणाहं", "शिरइति", "सर्वं पुनः शरीरम्", "अंगुलानि चतुरशीतिः"],
              "Six in height, thirty-two in girth, the head; the whole body, again, eighty-four aṅgulas.",
              "Head's height → girth → head → whole body → eighty-four."),
        match(2, "Match each word of unit 95 to its meaning.",
              [["षट्", "six"], ["द्वात्रिंशत्", "thirty-two"], ["शिरस्", "head"], ["सर्व", "whole"],
               ["शरीर", "body"]],
              "षट् = six, द्वात्रिंशत् = thirty-two, शिरस् = head, सर्व = whole, शरीर = body.",
              "षट्, द्वात्रिंशत्, शिरस्, सर्व, शरीर.", role="extend",
              teaches="सर्वं शरीरम् = the whole body: सर्व here means 'entire', agreeing with neuter शरीरम्."),
        mcq("discriminate", 3, "By unit 95, which pair gives the head's height and girth?",
            ("Six and thirty-two", "षडङ्गुलोत्सेधं द्वात्रिंशत्परिणाहं शिरः."),
            [("Twelve and twenty-four", "Those are the face's measures (unit 90)."),
             ("Four and twenty-two", "Those are the neck's measures (unit 90)."),
             ("Six and twenty-four", "The head's girth is thirty-two, not twenty-four.")],
            "Head: six in height, thirty-two in girth.",
            "शिरः: उत्सेध ६, परिणाह ३२."),
        mcq("apply", 4, "Why is षट् printed षड् in षडंगुलोत्सेधं of unit 95?",
            ("ट् before a vowel → ड्", "षट् + अङ्गुल → षडङ्गुल: before the vowel अ, ट् becomes voiced ड्."),
            [("ट् before any sound → ड्", "Not any: before a voiceless sound it stays ट्."),
             ("ड् is the numeral's own stem", "The numeral is षष्; षट् / षड् come from sandhi."),
             ("ट् before a vowel is doubled", "It is not doubled; it becomes ड्.")],
            "षट् + अङ्गुल: ट् before a vowel → ड्.",
            "ट् + vowel → ड्."),
        mcq("transfer", 5, "By the pattern of षट् + अङ्गुल → षडङ्गुल, how is षट् + आननः (six-faced) joined in a new example?",
            ("षडाननः", "ट् before a vowel → ड्: षट् + आननः → षडाननः."),
            [("षटाननः", "Before a vowel ट् must become ड्."),
             ("षण्णाननः", "ण् would come before a nasal; आ is a vowel."),
             ("षष्ठाननः", "षष्ठ means sixth; the numeral six joins as षड्.")],
            "षट् + आननः = षडाननः, like षट् + अङ्गुल = षडङ्गुल.",
            "ट् + vowel → ड्.",
            teaches="A word-final ट् before a vowel becomes ड्: षट् + अङ्गुल → षडङ्गुल."),
    ],
}

# ---------------------------------------------------------------- unit 96
AUTHORED["96"] = {
    "title": "तदायामविस्तारसमं सममुच्यते",
    "question": "By unit 96, what is called सम?",
    "rule": "What is equal in (that) length and breadth (आयामविस्तारसमम्) is called सम, even or symmetrical (सममुच्यते).",
    "limits": ("Prose, one printed line. The parse of तद् is open: 'that (length and breadth)', a separate pronoun 'that', "
               "or तदा 'then' (data, open for the owner): no question on तद्. The unstated noun (the body) is not supplied."),
    "explain_hi": ("जो उस लम्बाई (आयाम) और चौड़ाई (विस्तार) में बराबर हो, उसे सम (बराबर, संतुलित) कहा जाता है। "
                   "‘तद्’ का अन्वय खुला है: ‘उस (माप) में’, अलग सर्वनाम ‘वह’, या ‘तदा’ (तब); डेटा इसे स्वामी के लिए खुला छोड़ता है। "
                   "किसका वर्णन है (शरीर), यह छपा नहीं। "
                   "उच्यते = कहा जाता है (√वच्, कर्मवाच्य वर्तमान); समम् + उच्यते → सममुच्यते।"),
    "hook": "लम्बाई-चौड़ाई में बराबर: सम।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 96, what does आयाम mean?",
            ("Length", "आयाम = length, paired with विस्तार, breadth."),
            [("Girth", "Girth is परिणाह, not आयाम."),
             ("Height", "Height is उत्सेध, not आयाम."),
             ("Weight", "Weight would be भार; आयाम is length.")],
            "आयाम = length; विस्तार = breadth.",
            "आयाम = length."),
        match(1, "Match each word of unit 96 to its meaning.",
              [["आयाम", "length"], ["विस्तार", "breadth"], ["सम", "equal, even"], ["उच्यते", "is called"]],
              "आयाम = length, विस्तार = breadth, सम = equal, even, उच्यते = is called.",
              "आयाम, विस्तार, सम, उच्यते."),
        order(2, "Put these words of unit 96 in the printed order.",
              ["आयाम", "विस्तार", "समं", "सममुच्यते"],
              "Length, breadth, equal (in them); is called even.",
              "आयाम → विस्तार → समं → सममुच्यते.", role="extend",
              teaches="आयाम-विस्तार-समम्: a compound 'equal in length and breadth', then सम as the name it receives."),
        mcq("discriminate", 3, "By unit 96, what is called सम?",
            ("What is equal in length and breadth", "आयामविस्तारसमं सममुच्यते."),
            [("What is long but very narrow", "Long but narrow is not equal in breadth."),
             ("What exceeds in length and breadth", "Exceeding is not being equal (सम)."),
             ("What has no length or breadth", "The line speaks of being equal in them, not lacking them.")],
            "Equal in length and breadth → called सम.",
            "आयामविस्तारसम → सम."),
        mcq("apply", 4, "In unit 96, what does उच्यते say about सम?",
            ("It is called so", "उच्यते = is called (√वच्, passive present)."),
            [("It is seen so", "Seen would be दृश्यते; उच्यते is from √वच्, speak."),
             ("It is made so", "Made would be क्रियते; उच्यते is from √वच्, speak."),
             ("It is wished so", "Wished would be इष्यते; उच्यते is from √वच्, speak.")],
            "सममुच्यते: it is called sama.",
            "उच्यते = is called."),
        mcq("transfer", 5, "By the pattern of समम् + उच्यते → सममुच्यते, how is फलम् + अस्ति joined in a new example?",
            ("फलमस्ति", "Final म् before a vowel joins it: फलम् + अस्ति → फलमस्ति."),
            [("फलोस्ति", "ओ arises from a visarga, not from म्."),
             ("फलास्ति", "The म् does not vanish before a vowel."),
             ("फलवस्ति", "व् comes from उ or ओ before a vowel; here the final is म्.")],
            "फलम् + अस्ति = फलमस्ति, like समम् + उच्यते = सममुच्यते.",
            "म् + vowel → म joined to the vowel.",
            teaches="A final म् before a vowel stays म् and joins the vowel: समम् + उच्यते → सममुच्यते."),
    ],
}

# ---------------------------------------------------------------- unit 97
AUTHORED["97"] = {
    "title": "तत्र यथोक्तपरिमाणमिष्टम्",
    "question": "By unit 97, which measure is desirable and which is undesirable?",
    "rule": ("Therein (तत्र), the measure as stated (यथोक्तपरिमाणम्) is desirable (इष्टम्); deficient (हीनम्) or "
             "excessive (अधिकम्) is undesirable (अनिष्टम्)."),
    "limits": ("Prose, one printed line; copula understood. The clause division (इष्टम् | अनिष्टं हीनमधिकं वा) is the natural "
               "reading; हीनम्/अधिकम् could also be read with the measure itself; the sense stays the same. What is measured "
               "is not named here."),
    "explain_hi": ("उनमें, जैसा कहा गया वैसा परिमाण (यथोक्तपरिमाणम्) इष्ट है; उससे हीन (कम) या अधिक (ज़्यादा) अनिष्ट है। "
                   "यानी पिछली इकाइयों में दिए अंगुल-माप ही आदर्श हैं, यह डेटा की स्वाभाविक व्याख्या है। "
                   "‘यथोक्त’ में यथा + उक्त (आ + उ → ओ) है। "
                   "‘अनिष्ट’ में स्वर से पहले निषेध का अन्- है: अन् + इष्ट।"),
    "hook": "जैसा कहा वैसा: इष्ट; कम या ज़्यादा: अनिष्ट।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In unit 97, what does अनिष्ट mean?",
            ("Undesirable", "अन् + इष्ट: not desirable."),
            [("Desirable", "Desirable is इष्ट; अन्- negates it."),
             ("Unmeasured", "Unmeasured is not the sense; अनिष्ट = not desired."),
             ("Unknown", "Unknown would be अज्ञात; अनिष्ट = undesirable.")],
            "इष्ट = desirable; अनिष्ट = undesirable.",
            "अनिष्ट = undesirable."),
        order(1, "Put the words of unit 97 in the printed order.",
              ["तत्र", "यथोक्तपरिमाणम्", "इष्टम्", "अनिष्टं", "हीनम्", "अधिकं वा"],
              "Therein; the measure as stated; desirable; undesirable; deficient; or excessive.",
              "तत्र → यथोक्तपरिमाणम् → इष्टम् → अनिष्टं → हीनम् → अधिकं वा."),
        match(2, "Match each word of unit 97 to its meaning.",
              [["इष्ट", "desirable"], ["अनिष्ट", "undesirable"], ["हीन", "deficient"], ["अधिक", "excessive"],
               ["यथोक्त", "as stated"], ["परिमाण", "measure"]],
              "इष्ट = desirable, अनिष्ट = undesirable, हीन = deficient, अधिक = excessive, यथोक्त = as stated, परिमाण = measure.",
              "इष्ट, अनिष्ट, हीन, अधिक, यथोक्त, परिमाण.", role="extend",
              teaches="यथा + उक्त → यथोक्त, 'as stated': the measure given earlier is the standard."),
        mcq("discriminate", 3, "By unit 97, which measure is desirable?",
            ("The measure as stated", "यथोक्तपरिमाणम् इष्टम्."),
            [("A measure a little above it", "Excessive (अधिक) is undesirable."),
             ("A measure a little below it", "Deficient (हीन) is undesirable."),
             ("Any measure that is given", "Only the stated measure is called इष्ट.")],
            "As stated → desirable; deficient or excessive → undesirable.",
            "यथोक्त = इष्ट."),
        multi("apply", 4, "By unit 97, which measures are called undesirable?",
              [("A deficient measure", "Yes: हीनम् ... अनिष्टम्."),
               ("The measure as stated", "No: that one is इष्टम्, desirable."),
               ("An excessive measure", "Yes: अधिकम् ... अनिष्टम्."),
               ("A measure that equals the stated one", "No: that is the stated measure itself, desirable.")],
              [0, 2],
              "Deficient or excessive (हीनम् अधिकं वा) is undesirable.",
              "हीन / अधिक = अनिष्ट."),
        mcq("transfer", 5, "By the pattern of इष्ट → अनिष्ट, what is the negative of उचित (fitting) in a new example?",
            ("अनुचित", "Before a vowel the negative prefix is अन्-: अन् + उचित → अनुचित."),
            [("अउचित", "Before a vowel the prefix is अन्-, not अ-."),
             ("अचित", "The उ of उचित cannot vanish."),
             ("अनोचित", "उ stays उ; it does not become ओ.")],
            "अन् + उचित = अनुचित, like अन् + इष्ट = अनिष्ट.",
            "Negative अन्- before a vowel.",
            teaches="The negative prefix is अन्- before a vowel (अनिष्ट) and अ- before a consonant."),
    ],
}

# ---------------------------------------------------------------- unit 98
AUTHORED["98"] = {
    "title": "तथाहि",
    "question": "By unit 98, what does the formula तथाहि do?",
    "rule": "तथाहि (तथा, thus + हि, indeed) is a formula that introduces what follows: 'Thus indeed:'.",
    "limits": ("Prose, one word. The unit itself does not say what follows (examples or a list): no question on what "
               "comes next."),
    "explain_hi": ("‘तथाहि’ = तथा (इस प्रकार) + हि (निश्चय ही, क्योंकि)। "
                   "यह आगे आने वाली बात को आरम्भ करने वाला सूत्र-वाक्यांश है: ‘इस प्रकार, निश्चय ही:’। "
                   "आगे क्या आता है (उदाहरण या सूची), यह इकाई स्वयं नहीं बताती। "
                   "यहाँ कोई सन्धि-परिवर्तन नहीं; दोनों शब्द छपाई में जुड़े लिखे हैं।"),
    "hook": "तथाहि: ‘ऐसे ही, देखो:’ आगे की बात का द्वार।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 98, what does तथा mean?",
            ("Thus, so", "तथा = thus, so."),
            [("Where", "Where would be यत्र or कुत्र."),
             ("When", "When would be यदा or कदा."),
             ("Never", "Never would be न कदापि.")],
            "तथा = thus.",
            "तथा = thus."),
        fill(1, "The particle meaning 'indeed, for' printed after तथा in unit 98 is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("हि"),
             "तथा + हि, printed together as तथाहि.",
             "This particle stresses or gives a reason: 'indeed, for'.",
             "तथाहि = तथा + the particle 'indeed'.", role="warmup"),
        T(multi("extend", 2, "Which statements fit unit 98?",
                [("It gives a measure in aṅgulas", "No: unit 98 is one formula word, with no measure."),
                 ("It introduces what follows", "Yes: 'Thus indeed:' opens what comes next."),
                 ("It says itself what follows", "No: the unit does not say what follows."),
                 ("Its two words are printed as one", "Yes: तथा and हि are written together.")],
                [1, 3],
                "One formula word, printed joined, that introduces what follows.",
                "तथाहि = 'Thus indeed:'."),
          "तथाहि is an introducing formula: it opens what follows without stating it."),
        mcq("discriminate", 3, "Which split of तथाहि in unit 98 is right?",
            ("तथा + हि", "तथा (thus) + हि (indeed); no sandhi change."),
            [("तत् + हि", "तत् + हि would give तद्धि, not तथाहि."),
             ("तथ + आहि", "Neither तथ nor आहि is the word here."),
             ("तथाह + इ", "तथाह is not a word; the adverb is तथा.")],
            "तथा + हि, written together.",
            "तथाहि = तथा + हि."),
        mcq("apply", 4, "By unit 98, what does तथाहि do in the text?",
            ("It opens what comes next", "A formula 'Thus indeed:' introducing what follows."),
            [("It closes the whole chapter", "It does not close: it introduces."),
             ("It names a part of the body", "It is a formula, not a body part."),
             ("It denies the line before it", "It has no negation; it introduces.")],
            "तथाहि introduces what follows.",
            "तथाहि = an introducing formula."),
        mcq("transfer", 5, "In a new example, सत्यं हि परमं बलम्, what does हि add?",
            ("Stress or reason: indeed, for", "हि = indeed, for: 'truth indeed is the highest strength'."),
            [("A doubt: perhaps it is truth", "Doubt would need किंस्वित् or स्यात्; हि stresses."),
             ("A denial: it is not truth", "A denial would need न; हि stresses."),
             ("A choice: truth or strength", "A choice would need वा; हि stresses.")],
            "हि stresses the word before it or gives a reason.",
            "हि = indeed, for.",
            teaches="हि after a word stresses it or gives a reason ('indeed, for'), as in तथाहि."),
    ],
}

# ---------------------------------------------------------------- unit 99
AUTHORED["99"] = {
    "title": "ह्रस्वदीर्घगौरकृष्णरोमारोमस्थूलकृशं",
    "question": "Which eight qualities does unit 99 list, and how do they fall into pairs?",
    "rule": ("One compound of eight qualities: short and tall (ह्रस्व, दीर्घ), fair and dark (गौर, कृष्ण), hairy and "
             "hairless (रोम, अरोम), stout and lean (स्थूल, कृश); closed by च इति."),
    "limits": ("Prose, one printed line. The data reads it as following तथाहि (unit 98) and giving instances of body forms, "
               "but the text does not say so; nor does it call them desirable or undesirable: no question on that. The "
               "pairing into opposites is by the words' meanings."),
    "explain_hi": ("यह इकाई आठ गुणों का एक द्वन्द्व समास है: ह्रस्व (छोटा), दीर्घ (लम्बा), गौर (गोरा), कृष्ण (काला), रोम (रोम वाला), "
                   "अरोम (रोम रहित), स्थूल (मोटा), कृश (दुबला)। अर्थ के अनुसार ये चार उलटे जोड़े हैं। "
                   "डेटा इसे ‘तथाहि’ (इकाई ९८) के बाद आए शरीर-रूपों के उदाहरण मानता है, पर पाठ यह नहीं कहता; ये इष्ट हैं या अनिष्ट, यह भी नहीं कहा। "
                   "‘रोमारोम’ = रोम + अरोम (अ + अ → आ), ‘चेति’ = च + इति (अ + इ → ए)।"),
    "hook": "छोटा-लम्बा, गोरा-काला, रोमिल-अरोम, मोटा-दुबला।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 99, what does कृश mean?",
            ("Lean", "कृश = lean, thin: the last member, paired with स्थूल."),
            [("Stout", "Stout is स्थूल, its opposite in the list."),
             ("Tall", "Tall is दीर्घ, not कृश."),
             ("Fair", "Fair is गौर, not कृश.")],
            "स्थूल = stout; कृश = lean.",
            "कृश = lean."),
        order(1, "Put the four pairs of unit 99 in the printed order.",
              ["ह्रस्व-दीर्घ", "गौर-कृष्ण", "रोम-अरोम", "स्थूल-कृश"],
              "Short-tall, fair-dark, hairy-hairless, stout-lean.",
              "ह्रस्वदीर्घ → गौरकृष्ण → रोमारोम → स्थूलकृश."),
        match(2, "Match each word of unit 99 to its meaning.",
              [["ह्रस्व", "short"], ["दीर्घ", "tall"], ["गौर", "fair"], ["अरोम", "hairless"],
               ["स्थूल", "stout"], ["कृश", "lean"]],
              "ह्रस्व = short, दीर्घ = tall, गौर = fair, अरोम = hairless, स्थूल = stout, कृश = lean.",
              "ह्रस्व, दीर्घ, गौर, अरोम, स्थूल, कृश.", role="extend",
              teaches="अ- before a consonant negates: रोम (hair) → अरोम (hairless)."),
        mcq("discriminate", 3, "Which split of रोमारोम in unit 99 is right?",
            ("रोम + अरोम", "अ + अ → आ: रोम + अरोम → रोमारोम, hairy and hairless."),
            [("रोमा + रोम", "रोमा is not the compound form; the member is रोम."),
             ("रोम + आरोम", "आरोम is not a word; the negative is अरोम."),
             ("रोमार + ओम", "Neither रोमार nor ओम fits; the members are रोम and अरोम.")],
            "रोम (hairy) + अरोम (hairless).",
            "अ + अ → आ."),
        mcq("apply", 4, "In unit 99, which quality pairs with गौर as its opposite?",
            ("कृष्ण", "गौर (fair) and कृष्ण (dark) stand side by side as a pair."),
            [("दीर्घ", "दीर्घ (tall) pairs with ह्रस्व (short)."),
             ("स्थूल", "स्थूल (stout) pairs with कृश (lean)."),
             ("अरोम", "अरोम (hairless) pairs with रोम (hairy).")],
            "Fair ⇄ dark: गौर ⇄ कृष्ण.",
            "गौर ⇄ कृष्ण."),
        mcq("transfer", 5, "By the pattern of च + इति → चेति, how is न + इति joined in a new example?",
            ("नेति", "अ + इ → ए: न + इति → नेति."),
            [("नइति", "Two vowels cannot stand apart inside the join; अ + इ gives ए."),
             ("नयिति", "य् comes from इ before a vowel; here अ stands first."),
             ("नाइति", "अ does not lengthen to आ before इ; अ + इ gives ए.")],
            "न + इति = नेति, like च + इति = चेति.",
            "अ + इ → ए.",
            teaches="अ/आ + इ/ई → ए: च + इति → चेति."),
    ],
}

# ================================================================ NOTES_HI
NOTES_HI = {
    "88": ("गद्य; विश्वास उच्च; दो छपी पंक्तियाँ (०२.०८.१०२ और ०२.०८.१०३) जोड़ी गईं; कोई पाठ-चिह्न नहीं। क्रिया समझी जाती है; "
           "केवल संख्या जहाँ छपी हो वहाँ ‘अंगुल’ समझा जाता है। छपा ‘पंचांगुलामध्यमांगुलिः’ = पञ्चाङ्गुला मध्यमाङ्गुलिः (बिना जगह)। "
           "‘तत्र अपि’ = ‘उनमें भी’, या ‘वहाँ भी (हर हाथ में)’। छपा ‘अर्द्ध’ = अर्ध (र के बाद द्वित्व, छपाई की आदत)। ‘ततः’ = मध्यमा के "
           "पाँच अंगुल (डेटा)। सन्धि जाँची: द्वादश + अङ्गुलौ → द्वादशाङ्गुलौ; तत्र + अपि → तत्रापि (अ + अ → आ); ततः + अर्ध → ततोऽर्ध "
           "(अः + अ → ओऽ); प्रदेशिनी + अनामिके → प्रदेशिन्यनामिके (ई + भिन्न स्वर → य्)। अनामिका = अंगूठी वाली अंगुली (मानक)।"),
    "89": ("गद्य; विश्वास उच्च; एक छपी पंक्ति (०२.०८.१०४); कोई पाठ-चिह्न नहीं। क्रिया समझी जाती है। छपा ‘सार्द्ध’ = सार्ध (र के बाद "
           "द्वित्व, छपाई की आदत)। सन्धि जाँची: स + अर्ध → सार्ध (अ + अ → आ); त्रि + अङ्गुलौ → त्र्यङ्गुलौ (इ + भिन्न स्वर → य्); "
           "कनिष्ठिका + अङ्गुष्ठौ → कनिष्ठिकाङ्गुष्ठौ (आ + अ → आ)। द्वन्द्व का लिंग अन्तिम पद अङ्गुष्ठ (पुं.) से, इसलिए पुं. द्विवचन।"),
    "90": ("गद्य; विश्वास उच्च; दो छपी पंक्तियाँ (०२.०८.१०५ और ०२.०८.१०६) जोड़ी गईं; कोई पाठ-चिह्न नहीं। केवल संख्याएँ छपी हैं, "
           "‘अंगुल’ समझा जाता है। शिरोधरा = गर्दन (मानक); आनन = चेहरा, जबकि आस्य (इकाई ९१) = मुँह। सन्धि जाँची: चतुर् + उत्सेधा → "
           "चतुरुत्सेधा (र् स्वर से जुड़ा); द्वादश + उत्सेधम् → द्वादशोत्सेधम् (अ + उ → ओ); -परिणाहम् + आननम् → -परिणाहमाननम्। "
           "लिंग-मेल: शिरोधरा (स्त्री.) के साथ -आ, आननम् (नपुं.) के साथ -म्।"),
    "91": ("गद्य; विश्वास उच्च; एक छपी पंक्ति (०२.०८.१०७); कोई पाठ-चिह्न नहीं। कौन-सा माप (खुलाव या चौड़ाई) है, यह नहीं कहा गया। "
           "सन्धि जाँची: पञ्च + अङ्गुलम् → पञ्चाङ्गुलम् (अ + अ → आ); पञ्चाङ्गुलम् + आस्यम् → पञ्चाङ्गुलमास्यम्। छपाई में अन्त का ‘आस्यं’ "
           "अनुस्वार के साथ।"),
    "92": ("गद्य; विश्वास मध्यम; एक छपी पंक्ति (०२.०८.१०८)। पाठ-चिह्न (सम्भव): ‘नासाद्दृष्ट्यंतर’ का दोहरा द् समास में आवश्यक नहीं; "
           "भूल से द्वित्व, या नासात् + दृष्ट्यन्तर (जिससे अर्थ बदलेगा)। ‘दृष्ट्यन्तर’ = आँखों के बीच की दूरी (सम्भावित); ‘नासा-दृष्ट्यन्तर’ "
           "एक ही पद (नाक से आँख तक) भी सम्भव। इसलिए नाक, दृष्टि-अन्तर और पदों की संख्या पर प्रश्न नहीं। चिबुक, ओष्ठ, कर्ण, ललाट मानक। "
           "समास नपुंसक एकवचन द्वन्द्व। सन्धि जाँची: चिबुक + ओष्ठ → चिबुकौष्ठ (अ + ओ → औ; समास में ओष्ठ से पहले विकल्प से ओ भी, "
           "जैसे बिम्बोष्ठ; छपा रूप औ); चतुरङ्गुलम् + पृथक् → चतुरङ्गुलं पृथक् (व्यंजन से पहले अन्तिम म् → ं; छपाई में बिना जगह)।"),
    "93": ("गद्य; विश्वास मध्यम; दो छपी पंक्तियाँ (०२.०८.१०९ और ०२.०८.११०) जोड़ी गईं; कोई पाठ-चिह्न नहीं। ‘त्रिभाग’ = तिहाई भाग; "
           "‘तीन भाग’ भी सम्भव, इसलिए उस संख्या पर प्रश्न नहीं। मर्यादा = किनारा, सीमा। ‘अङ्गुष्ठोदर’ = अँगूठे का मांसल बीच का भाग; "
           "आगे कोई माप नहीं दिया। यहाँ उदर शरीर का भाग है, रोग नहीं। सन्धि जाँची: त्रिभाग + अङ्गुल → त्रिभागाङ्गुल (अ + अ → आ); "
           "द्वि + अङ्गुल → द्व्यङ्गुल (इ + भिन्न स्वर → य्); -अङ्गुल + आयतम् → -अङ्गुलायतम्; -आयतम् + अङ्गुष्ठ → -आयतमङ्गुष्ठ; "
           "अङ्गुष्ठ + उदर → अङ्गुष्ठोदर (अ + उ → ओ)।"),
    "94": ("गद्य; विश्वास मध्यम; एक छपी पंक्ति (०२.०८.१११); कोई पाठ-चिह्न नहीं। ‘शुक्लतृतीयांशः’ = शुक्लस्य तृतीयांशः; तृतीयांश = "
           "एक-तिहाई या तीसरा अंश। दृष्टि = देखने वाला भाग, सम्भवतः पुतली। मसूर = Lens culinaris (मानक); ‘दल’ = आधा दाना, फाँक या "
           "पत्ता (अस्पष्ट), इसलिए उस पर प्रश्न नहीं। ‘नवमांशा’ का -आ स्त्रीलिंग दृष्टि से मेल। सन्धि जाँची: तृतीय + अंशः → तृतीयांशः "
           "और नवम + अंशा → नवमांशा (अ + अ → आ); कृष्णात् + नवम → कृष्णान्नवम (अनुनासिक से पहले त् → न्, विकल्प से; द् भी सही)।"),
    "95": ("गद्य; विश्वास मध्यम; दो छपी पंक्तियाँ (०२.०८.११२ और ०२.०८.११३) जोड़ी गईं। पाठ-चिह्न (सम्भव): छपा ‘शिरइति’ = ‘शिर इति’ "
           "(शिरः + इति: अः के बाद अ से भिन्न स्वर हो तो विसर्ग लुप्त, जगह बनी रहती है; छपाई में जगह छूटी)। डेटा की टिप्पणी पिछली इकाई "
           "से GROUPING बताती है, जबकि सिर (शिरः) इसी इकाई के अन्त में छपा है; इस पर प्रश्न नहीं। अङ्गुलानि (बहु.) और चतुरशीतिः (एक.) "
           "का वचन अलग, माप का समीकरण। सन्धि जाँची: षट् + अङ्गुल → षडङ्गुल (स्वर से पहले ट् → ड्); -अङ्गुल + उत्सेधम् → -अङ्गुलोत्सेधम् "
           "(अ + उ → ओ); शरीरम् + अङ्गुलानि → शरीरमङ्गुलानि; पुनः + शरीरम्: श से पहले विसर्ग वैसा ही रहे या विकल्प से श् बने, छपाई में ः।"),
    "96": ("गद्य; विश्वास मध्यम; एक छपी पंक्ति (०२.०८.११४); कोई पाठ-चिह्न नहीं। ‘तद्’ का अन्वय खुला: ‘उस (लम्बाई-चौड़ाई) में’, "
           "अलग सर्वनाम ‘वह’ (नपुं. एक.), या ‘तदा’ (तब); डेटा इसे स्वामी के लिए खुला रखता है; इस पर प्रश्न नहीं। अनकहा विशेष्य "
           "(शरीर) नहीं जोड़ा गया। सम = बराबर, संतुलित; पाठ इससे अधिक नहीं कहता। उच्यते = √वच्, कर्मवाच्य वर्तमान। सन्धि जाँची: "
           "समम् + उच्यते → सममुच्यते।"),
    "97": ("गद्य; विश्वास उच्च; एक छपी पंक्ति (०२.०८.११५); कोई पाठ-चिह्न नहीं। वाक्य-विभाग ‘इष्टम् | अनिष्टं हीनमधिकं वा’ स्वाभाविक "
           "पाठ; हीनम्/अधिकम् को सीधे परिमाण के साथ भी पढ़ा जा सकता है, अर्थ वही। सन्धि जाँची: यथा + उक्त → यथोक्त (आ + उ → ओ); "
           "-परिमाणम् + इष्टम् + अनिष्टम् → -परिमाणमिष्टमनिष्टम्; अनिष्टम् + हीनम् → अनिष्टं हीनम् (व्यंजन से पहले अन्तिम म् → ं); "
           "हीनम् + अधिकम् → हीनमधिकम्। अन् + इष्ट → अनिष्ट (स्वर से पहले निषेध अन्-)।"),
    "98": ("गद्य; विश्वास उच्च; एक छपी पंक्ति (०२.०८.११६); कोई पाठ-चिह्न नहीं। ‘तथाहि’ = तथा + हि, बिना सन्धि-परिवर्तन, जुड़ा "
           "लिखा। आगे की बात (उदाहरण या सूची) का आरम्भ-सूत्र; क्या आता है, यह इकाई नहीं कहती।"),
    "99": ("गद्य; विश्वास उच्च; एक छपी पंक्ति (०२.०८.११७); कोई पाठ-चिह्न नहीं। आठ गुणों का एक नपुंसक द्वन्द्व; अन्त का ‘इति’ "
           "अनुवाद में नहीं। डेटा के अनुसार यह ‘तथाहि’ (कार्ड ९८, छपी पंक्ति ११६) के बाद शरीर-रूपों के उदाहरण देता प्रतीत होता है; पाठ यह "
           "नहीं कहता। सन्धि जाँची: रोम + अरोम → रोमारोम (अ + अ → आ); च + इति → चेति (अ + इ → ए); -कृशम् + च → -कृशं च (व्यंजन से "
           "पहले अन्तिम म् → ं)। कृष्ण यहाँ रंग (काला/साँवला) है।"),
}

# ================================================================ AIDS
AIDS = {
    "88": {
        "diagram": {"groups": [
            {"label": "द्वादशांगुलौ पाणी", "items": ["पाणि: हाथ, १२ अंगुल"]},
            {"label": "तत्रापि", "items": ["मध्यमाङ्गुलि: ५ अंगुल", "प्रदेशिनी, अनामिका: उससे आधा अंगुल कम"]}]},
        "chunks": "द्वादशांगुलौ पाणी | तत्रापि | पंचांगुलामध्यमांगुलिः || ततोऽर्द्धांगुलहीने | प्रदेशिन्यनामिके",
        "sandhi": ("अः + अ → ओऽ: ततः + अर्ध → ततोऽर्ध · ई + भिन्न स्वर → य्: प्रदेशिनी + अनामिके → प्रदेशिन्यनामिके · अ + अ → आ: "
                   "तत्र + अपि → तत्रापि।"),
        "pegs": "बीच वाली ‘मध्यमा’ सबसे ऊँची, पाँच; उसके दोनों पड़ोसी आधा झुके। (मेरा बनाया चित्र)",
    },
    "89": {
        "chunks": "सार्द्धत्र्यंगुलौ | कनिष्ठिकांगुष्ठौ",
        "sandhi": "अ + अ → आ: स + अर्ध → सार्ध · इ + भिन्न स्वर → य्: त्रि + अङ्गुलौ → त्र्यङ्गुलौ · आ + अ → आ: कनिष्ठिका + अङ्गुष्ठौ → कनिष्ठिकाङ्गुष्ठौ।",
        "anchors": "हाथ के दोनों छोर, छोटी अंगुली और अँगूठा: दोनों साढ़े तीन। (मेरी याद-पद्धति)",
    },
    "90": {
        "diagram": {"groups": [
            {"label": "शिरोधरा", "items": ["चतुरुत्सेधा: ऊँचाई ४", "द्वाविंशतिपरिणाहा: घेरा २२"]},
            {"label": "आननं", "items": ["द्वादशोत्सेधं: ऊँचाई १२", "चतुर्विंशतिपरिणाहम्: घेरा २४"]}]},
        "chunks": "चतुरुत्सेधा | द्वाविंशतिपरिणाहा | शिरोधरा || द्वादशोत्सेधं | चतुर्विंशतिपरिणाहमाननं",
        "contrast": "शिरोधरा (स्त्री.) → -उत्सेधा, -परिणाहा ⇄ आनन (नपुं.) → -उत्सेधम्, -परिणाहम्: दोनों इसी इकाई में।",
        "sandhi": "अ + उ → ओ: द्वादश + उत्सेधम् → द्वादशोत्सेधम्।",
    },
    "91": {
        "chunks": "पंचांगुलम् | आस्यं",
        "sandhi": "अ + अ → आ: पञ्च + अङ्गुलम् → पञ्चाङ्गुलम् · म् + स्वर: पञ्चाङ्गुलम् + आस्यम् → पञ्चाङ्गुलमास्यम्।",
        "anchors": "मुँह: पाँच अंगुल; कौन-सा माप, यह नहीं कहा। (मेरी याद-पद्धति)",
    },
    "92": {
        "diagram": {"groups": [
            {"label": "चतुरंगुलं पृथक्: हर एक ४ अंगुल", "items": ["१ चिबुक", "२ ओष्ठ", "३ नासा (पाठ-चिह्न)",
                                                      "४ दृष्ट्यंतर (सम्भावित)", "५ कर्ण", "६ ललाट"]}]},
        "chunks": "चतुरंगुलंपृथक् | चिबुकौष्ठनासाद्दृष्ट्यंतरकर्णललाटं",
        "sandhi": "अ + ओ → औ: चिबुक + ओष्ठ → चिबुकौष्ठ (समास में ओष्ठ से पहले विकल्प से ओ भी; छपा रूप औ)।",
        "pegs": "चि-ओ-क-ल: ठुड्डी से माथे तक नीचे से ऊपर, हर एक चार। (मेरा बनाया स्मरण-सूत्र)",
    },
    "93": {
        "diagram": {"groups": [
            {"label": "नासापुटमर्यादा", "items": ["त्रिभागांगुलविस्तारा: चौड़ाई अंगुल का त्रिभाग"]},
            {"label": "नेत्रं", "items": ["द्व्यंगुलायतम्: लम्बाई २ अंगुल", "अंगुष्ठोदरविस्तृतं: अँगूठे के उदर जितना चौड़ा"]}]},
        "chunks": "त्रिभागांगुलविस्तारा | नासापुटमर्यादा || द्व्यंगुलायतम् | अंगुष्ठोदरविस्तृतं | नेत्रं",
        "sandhi": "इ + भिन्न स्वर → य्: द्वि + अङ्गुल → द्व्यङ्गुल · अ + उ → ओ: अङ्गुष्ठ + उदर → अङ्गुष्ठोदर।",
    },
    "94": {
        "chain": {"steps": ["शुक्ल: सफेद भाग", "कृष्णः: शुक्ल का तृतीयांश", "दृष्टिः: कृष्ण का नवमांश (सम्भवतः पुतली)",
                            "मसूरदलमात्रा: मसूर के दल जितनी"]},
        "chunks": "तत्र | शुक्लतृतीयांशः | कृष्णः | कृष्णान्नवमांशा | मसूरदलमात्रा | दृष्टिः",
        "sandhi": ("अ + अ → आ: तृतीय + अंशः → तृतीयांशः, नवम + अंशा → नवमांशा · अनुनासिक से पहले त् → न्, विकल्प से (द् भी सही): "
                   "कृष्णात् + नवम → कृष्णान्नवम।"),
        "pegs": "तीन से भाग, फिर नौ से भाग: सफेद → काला → दृष्टि, हर कदम छोटा। (मेरा बनाया चित्र)",
    },
    "95": {
        "diagram": {"groups": [
            {"label": "शिरः", "items": ["षडंगुलोत्सेधं: ऊँचाई ६", "द्वात्रिंशत्परिणाहं: घेरा ३२"]},
            {"label": "सर्वं पुनः शरीरम्", "items": ["अंगुलानि चतुरशीतिः: ८४ अंगुल"]}]},
        "chunks": "षडंगुलोत्सेधं | द्वात्रिंशत्परिणाहं | शिरइति || सर्वं पुनः | शरीरमंगुलानि | चतुरशीतिः",
        "sandhi": ("स्वर से पहले ट् → ड्: षट् + अङ्गुल → षडङ्गुल · अः + अ से भिन्न स्वर → अ (विसर्ग लुप्त): शिरः + इति → शिर इति "
                   "(छपा ‘शिरइति’)।"),
        "anchors": "छह और बत्तीस: सिर; चौरासी: पूरा शरीर। (मेरी याद-पद्धति)",
    },
    "96": {
        "frame": "किसमें: आयाम (लम्बाई) और विस्तार (चौड़ाई) → कैसा: समम् (बराबर) → नाम: सममुच्यते (सम कहा जाता है)।",
        "chunks": "तदायामविस्तारसमं | सममुच्यते",
        "sandhi": "म् + स्वर: समम् + उच्यते → सममुच्यते।",
    },
    "97": {
        "seesaw": "इष्टम्: यथोक्त परिमाण ⇄ अनिष्टम्: हीन या अधिक; और हीन ⇄ अधिक: दोनों जोड़े इसी इकाई में।",
        "chunks": "तत्र | यथोक्तपरिमाणम् | इष्टम् | अनिष्टं | हीनमधिकं वा",
        "sandhi": "आ + उ → ओ: यथा + उक्त → यथोक्त · व्यंजन से पहले अन्तिम म् → ं: अनिष्टम् + हीनम् → अनिष्टं हीनम्।",
    },
    "98": {
        "frame": "तथा (इस प्रकार) + हि (निश्चय ही) → आगे आने वाली बात का आरम्भ; क्या आता है, यह यहाँ नहीं कहा।",
        "anchors": "तथाहि = ‘ऐसे ही, देखो:’ (केवल सुनने की सहायता)",
    },
    "99": {
        "seesaw": "ह्रस्व ⇄ दीर्घ · गौर ⇄ कृष्ण · रोम ⇄ अरोम · स्थूल ⇄ कृश: चारों जोड़े इसी इकाई में, अर्थ में उलटे।",
        "chunks": "ह्रस्वदीर्घ | गौरकृष्ण | रोमारोम | स्थूलकृशं | चेति",
        "sandhi": "अ + अ → आ: रोम + अरोम → रोमारोम · अ + इ → ए: च + इति → चेति।",
    },
}

# ================================================================ IMAGE_SPECS
IMAGE_SPECS = {
    ("88", "diagram"): {
        "file": "sh8-pani-anguli-88.svg",
        "alt": ("Table of card 88: the hands twelve aṅgulas; the middle finger five aṅgulas; the index and ring fingers "
                "half an aṅgula less than the middle finger."),
        "type": "table",
        "title": "कार्ड ८८: हाथ और अंगुलियाँ",
        "heads": ["अंग", "माप"],
        "rows": [["पाणि: हाथ", "१२ अंगुल"], ["मध्यमा अंगुली", "५ अंगुल"],
                 ["प्रदेशिनी, अनामिका", "मध्यमा से आधा अंगुल कम"]],
    },
    ("90", "diagram"): {
        "file": "sh8-shirodhara-anana-90.svg",
        "alt": ("Table of card 90: the neck is four in height and twenty-two in girth; the face is twelve in height and "
                "twenty-four in girth."),
        "type": "table",
        "title": "कार्ड ९०: गर्दन और चेहरा",
        "heads": ["अंग", "ऊँचाई · घेरा"],
        "rows": [["शिरोधरा: गर्दन", "४ · २२"], ["आनन: चेहरा", "१२ · २४"]],
    },
    ("92", "diagram"): {
        "file": "sh8-chaturangula-92.svg",
        "alt": ("Table of card 92 in printed order: chin, lip, nose (text flag), interval between the eyes (probable), "
                "ear, forehead; each four aṅgulas separately."),
        "type": "table",
        "title": "कार्ड ९२: हर एक चार अंगुल",
        "heads": ["क्रम", "अंग"],
        "rows": [["१", "चिबुक: ठुड्डी"], ["२", "ओष्ठ: होंठ"], ["३", "नासा: नाक (पाठ-चिह्न)"],
                 ["४", "दृष्टि-अन्तर (सम्भावित)"], ["५", "कर्ण: कान"], ["६", "ललाट: माथा"]],
    },
    ("93", "diagram"): {
        "file": "sh8-netra-93.svg",
        "alt": ("Table of card 93: the nostril border is a third part of an aṅgula in breadth; the eye is two aṅgulas long "
                "and broad by the belly of the thumb."),
        "type": "table",
        "title": "कार्ड ९३: नथुने का किनारा और आँख",
        "heads": ["अंग", "माप"],
        "rows": [["नासापुटमर्यादा: चौड़ाई", "अंगुल का त्रिभाग"], ["नेत्र: लम्बाई", "२ अंगुल"],
                 ["नेत्र: चौड़ाई", "अँगूठे के उदर जितनी"]],
    },
    ("94", "chain"): {
        "file": "sh8-drishti-94.svg",
        "alt": ("Chain of card 94: the white; the black, a third portion of the white; the dṛṣṭi (probably the pupil), a "
                "ninth portion of the black; of the size of a masūra-dala."),
        "type": "chain",
        "title": "कार्ड ९४: शुक्ल, कृष्ण, दृष्टि",
        "steps": ["शुक्ल: सफेद भाग", "कृष्ण: शुक्ल का तृतीयांश", "दृष्टि: कृष्ण का नवमांश (सम्भवतः पुतली)",
                  "माप: मसूर के दल जितना"],
    },
    ("95", "diagram"): {
        "file": "sh8-shira-sharira-95.svg",
        "alt": "Table of card 95: the head is six aṅgulas in height and thirty-two in girth; the whole body is eighty-four aṅgulas.",
        "type": "table",
        "title": "कार्ड ९५: सिर और पूरा शरीर",
        "heads": ["अंग", "माप"],
        "rows": [["शिर की ऊँचाई", "६ अंगुल"], ["शिर का घेरा", "३२"], ["सारा शरीर", "८४ अंगुल"]],
    },
    ("97", "seesaw"): {
        "file": "sh8-ishta-anishta-97.svg",
        "alt": "Split of card 97: desirable, the measure as stated; undesirable, deficient or excessive.",
        "type": "split",
        "title": "कार्ड ९७: इष्ट और अनिष्ट परिमाण",
        "cols": [["इष्टम्", ["यथोक्त परिमाण", "जैसा कहा गया"]],
                 ["अनिष्टम्", ["हीनम्: कम", "अधिकम्: ज़्यादा"]]],
    },
    ("99", "seesaw"): {
        "file": "sh8-ashta-guna-99.svg",
        "alt": ("Table of card 99 in printed order: four pairs of opposite qualities: short and tall, fair and dark, hairy "
                "and hairless, stout and lean."),
        "type": "table",
        "title": "कार्ड ९९: आठ गुण, चार जोड़े",
        "heads": ["गुण", "उलटा गुण"],
        "rows": [["ह्रस्व: छोटा", "दीर्घ: लम्बा"], ["गौर: गोरा", "कृष्ण: काला"], ["रोम: रोम वाला", "अरोम: रोम रहित"],
                 ["स्थूल: मोटा", "कृश: दुबला"]],
    },
}
