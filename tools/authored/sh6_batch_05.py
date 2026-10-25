from helpers import mcq, match, order, fill, multi, accepts


AUTHORED = {}

# ---------------------------------------------------------------- unit 52
AUTHORED["52"] = {
    "title": "अधोगमाः पक्वाशयस्था",
    "question": "By unit 52, where are the downward-going ones situated, and what do they come to be?",
    "rule": ("The downward-going (ones) (अधोगमाः), situated in the pakvāśaya (पक्वाशयस्थाः), likewise (एवम्) come to be "
             "threefold (त्रिधा जायन्ते)."),
    "limits": ("Prose. The line does not name the 'ones'; they are presumably the ten downward dhamanīs of card 47. "
               "Pakvāśaya as the large-intestine region is probable. The three kinds are not named here. जायन्ते is a "
               "middle form, 'come to be', not a passive."),
    "explain_hi": ("यह गद्य-पंक्ति नीचे जाने वाली (धमनियों) की बात करती है: वे पक्वाशय में स्थित हैं और इसी प्रकार तीन प्रकार की हो जाती हैं। "
                   "पक्वाशय का अर्थ है पके या पचे (अन्न, मल) का आशय; इसे सम्भवतः बड़ी आँत का क्षेत्र माना गया है (सम्भावित)। "
                   "पंक्ति स्वयं ‘धमनी’ शब्द नहीं कहती; सम्भवतः ये इकाई ४७ की दस नीचे जाने वाली धमनियाँ हैं। "
                   "इकाई ४८ में ऊपर जाने वाली के लिए भी ‘त्रिधा जायन्ते’ छपा है; ‘एवम्’ (इसी प्रकार) इसी से मेल दिखाता है। "
                   "‘जायन्ते’ √जन् का आत्मनेपद वर्तमान है: ‘हो जाती हैं’, कर्मवाच्य नहीं।"),
    "hook": "नीचे वाली: पक्वाशय में, वे भी तीन-तीन।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 52, where are the downward-going ones situated?",
            ("In the pakvāśaya (ripened-food seat)", "पक्वाशयस्थाः: situated in the pakvāśaya."),
            [("In the hṛdaya (the heart of the body)", "The heart is reached by the upward-going ones (card 48), not these."),
             ("In the śiras (the head of the body)", "No head is named in unit 52; the place is the pakvāśaya."),
             ("In the grīvā (the neck of the body)", "No neck is named in unit 52; the place is the pakvāśaya.")],
            "The downward-going ones are situated in the pakvāśaya (probably the large-intestine region).",
            "अधोगमाः पक्वाशयस्थाः."),
        order(1, "Put the words of unit 52 in the line's order.",
              ["अधोगमाः", "पक्वाशयस्था", "एवं", "त्रिधा", "जायंते"],
              "Downward-going, situated in the pakvāśaya, likewise, threefold, come to be.",
              "अधोगमाः → पक्वाशयस्था → एवं → त्रिधा → जायंते."),
        match(2, "Match each word part of unit 52 to its meaning.",
              [["अधः", "downward"], ["गम", "going"], ["पक्व", "ripened, digested"], ["आशय", "seat"],
               ["स्थ", "situated in"], ["त्रिधा", "threefold"]],
              "अधः-गमाः = downward-going; पक्व-आशय-स्थाः = situated in the seat of the digested; त्रिधा = threefold.",
              "अधः, गम, पक्व, आशय, स्थ, त्रिधा.", role="extend",
              teaches="पक्वाशय = पक्व (digested) + आशय (seat), with अ + आ → आ."),
        mcq("discriminate", 3, "Which split of अधोगमाः in unit 52 is right?",
            ("अधः + गमाः", "अः before a voiced consonant (ग) becomes ओ: अधः + गमाः → अधोगमाः."),
            [("अधम् + गमाः", "म् before a consonant would be written ं: अधंगमाः."),
             ("अधे + गमाः", "ए before a consonant stays ए: अधेगमाः."),
             ("अधौ + गमाः", "औ before a consonant stays औ: अधौगमाः.")],
            "अधः (downward) + गमाः (going): अः before a voiced consonant → ओ.",
            "अः before a voiced consonant → ओ."),
        multi("apply", 4, "Which statements fit unit 52?",
              [("The line itself names them as dhamanīs", "The line does not name them; dhamanīs is a presumption from card 47."),
               ("They are situated in the pakvāśaya", "Right: पक्वाशयस्थाः."),
               ("जायन्ते here is a passive form", "जायन्ते is a middle present of √जन्: 'come to be', not passive."),
               ("They come to be threefold", "Right: एवं त्रिधा जायन्ते.")],
              [1, 3],
              "In the pakvāśaya, likewise threefold; the line does not name the 'ones'.",
              "अधोगमाः पक्वाशयस्था एवं त्रिधा जायन्ते."),
        mcq("transfer", 5, "By the rule of अधः + गमाः → अधोगमाः, how is मनः + हरम् (charming) joined in a new example?",
            ("मनोहरम्", "अः before a voiced consonant (ह) becomes ओ, as अधः + गमाः → अधोगमाः."),
            [("मनाहरम्", "आ does not come from अः before a consonant."),
             ("मनर्हरम्", "र् comes from a visarga after vowels other than अ/आ, not after अ."),
             ("मनःहरम्", "Before a voiced consonant this visarga does not stay; अः → ओ.")],
            "मनः + हरम् = मनोहरम्, like अधः + गमाः = अधोगमाः.",
            "अः before a voiced consonant → ओ.",
            teaches="अः before a voiced consonant becomes ओ: अधः + गमाः → अधोगमाः."),
    ],
}

# ---------------------------------------------------------------- unit 53
AUTHORED["53"] = {
    "title": "तत्र दशाद्याः पूर्ववत्",
    "question": "What do the three words of unit 53 say, and why is the line hard to read?",
    "rule": ("There (तत्र), the first ten (दश आद्याः, the data's reading): as before (पूर्ववत्). The line is elliptical; "
             "what the ten are and what 'before' points to are not stated."),
    "limits": ("Prose, three words, low confidence. Neither referent is stated; daśādyāḥ may also mean 'ten and so on'. "
               "No verb or noun is supplied. No question asks what the ten are or what 'as before' refers to."),
    "explain_hi": ("यह तीन शब्दों की गद्य-पंक्ति है: वहाँ पहली दस, पहले के समान। "
                   "पंक्ति अधूरी है: कौन-सी दस, और ‘पहले के समान’ किसके समान, यह छपा नहीं। "
                   "डेटा का अनुमान है कि ये नीचे वाले वर्ग से बनी तीस में से पहली दस हो सकती हैं (इकाई ५२), और ‘पूर्ववत्’ ऊपर वाले वर्ग की तरह; यह निश्चित नहीं। "
                   "‘दशाद्याः’ का दूसरा अर्थ ‘दस आदि’ भी हो सकता है; इसलिए विश्वास कम है। "
                   "सन्धि: दश + आद्याः में अ + आ मिलकर आ बना।"),
    "hook": "पहली दस: पहले जैसी; बाकी अस्पष्ट।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 53, what does पूर्ववत् mean?",
            ("As before", "पूर्ववत् = as before (data gloss)."),
            [("After this", "After this would be ततः or अनन्तरम्; पूर्ववत् is as before."),
             ("From below", "From below would be अधस्तात्; पूर्ववत् is as before."),
             ("Not so", "Not so would be न तथा; पूर्ववत् is as before.")],
            "पूर्ववत् = as before.",
            "पूर्व + वत् = as before."),
        order(1, "Put the words of unit 53 in the line's order.",
              ["तत्र", "दशाद्याः", "पूर्ववत्"],
              "There, the first ten, as before.",
              "तत्र → दशाद्याः → पूर्ववत्."),
        match(2, "Match each word part of unit 53 to its meaning.",
              [["तत्र", "there, among these"], ["दश", "ten"], ["आद्य", "first, beginning"], ["पूर्ववत्", "as before"]],
              "तत्र = there; दश-आद्याः = the first ten (or 'ten and so on'); पूर्ववत् = as before.",
              "तत्र, दश, आद्य, पूर्ववत्.", role="extend",
              teaches="-वत् after a word as an indeclinable means 'like, as': पूर्ववत् = as before."),
        mcq("discriminate", 3, "Which split of दशाद्याः in unit 53 is right?",
            ("दश + आद्याः", "अ + आ → आ: दश + आद्याः → दशाद्याः."),
            [("दशः + आद्याः", "अः before a vowel other than अ becomes अ with no join: दश आद्याः."),
             ("दशे + आद्याः", "ए before आ would give दशयाद्याः or दश आद्याः, not दशाद्याः."),
             ("दशौ + आद्याः", "औ before आ would give दशावाद्याः.")],
            "दश (ten) + आद्याः (first): अ + आ → आ.",
            "अ + आ → आ."),
        multi("apply", 4, "Which statements fit unit 53 and its data?",
              [("No verb is printed in the line", "Right: the line is elliptical; no verb is supplied."),
               ("The line names what the ten are", "It does not; the referent is only presumed."),
               ("दशाद्याः may also mean 'ten and so on'", "Right: the data notes this second reading."),
               ("पूर्ववत् names the passage it points to", "It does not; what 'before' refers to is not stated.")],
              [0, 2],
              "Elliptical: no verb, no stated referents; दशाद्याः can be read two ways.",
              "तत्र दशाद्याः पूर्ववत्."),
        mcq("transfer", 5, "By the rule of दश + आद्याः → दशाद्याः, how is न + आगच्छति (does not come) joined in a new example?",
            ("नागच्छति", "अ + आ → आ, as दश + आद्याः → दशाद्याः."),
            [("नेगच्छति", "ए comes from अ + इ, not from अ + आ."),
             ("नोगच्छति", "ओ comes from अ + उ, not from अ + आ."),
             ("नौगच्छति", "औ comes from अ + ओ/औ, not from अ + आ.")],
            "न + आगच्छति = नागच्छति, like दश + आद्याः = दशाद्याः.",
            "अ + आ → आ.",
            teaches="अ before आ merges into आ: दश + आद्याः → दशाद्याः."),
    ],
}

# ---------------------------------------------------------------- unit 54
AUTHORED["54"] = {
    "title": "द्वे वहतोऽन्नम् ... द्वे च मुंचतः",
    "question": "By unit 54, what do the five pairs carry or do?",
    "rule": ("Two carry food (अन्नम्), with the intestines as their resting-place (अन्त्राश्रयेण); two, water (तोयम्); two, "
             "urine (मूत्रम्); two carry semen (शुक्रम्); and two release (मुञ्चतः)."),
    "limits": ("Prose. For the water and urine pairs the verb वहतः is carried over, not printed. The object of मुञ्चतः is "
               "not stated: no question on what is released. अन्त्राश्रयेण may qualify the food pair only."),
    "explain_hi": ("यह गद्य-पंक्ति दो-दो के पाँच जोड़े गिनाती है: दो अन्न वहन करती हैं, आँतों (अन्त्र) के आश्रय से; दो जल (तोय); दो मूत्र; दो शुक्र यानी वीर्य; और दो छोड़ती हैं। "
                   "जल और मूत्र वाले जोड़ों के साथ ‘वहतः’ छपा नहीं, पिछले से समझा जाता है। "
                   "‘मुञ्चतः’ (छोड़ती हैं) का कर्म छपा नहीं; क्या छोड़ती हैं, यह पंक्ति नहीं बताती। "
                   "‘वहतः’ और ‘मुञ्चतः’ प्रथम पुरुष द्विवचन वर्तमान हैं, ‘द्वे’ (दो) के साथ। "
                   "यह पंक्ति इकाई ५२-५३ को आगे बढ़ाती दिखती है (समूह-टिप्पणी)।"),
    "hook": "अन्न, जल, मूत्र, शुक्र: वहन; अन्त में दो छोड़ती हैं।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 54, what does the first pair carry?",
            ("Food (anna)", "द्वे वहतोऽन्नम्: two carry food."),
            [("Water (toya)", "Water is carried by the second pair."),
             ("Urine (mūtra)", "Urine is carried by the third pair."),
             ("Semen (śukra)", "Śukra is carried by the fourth pair.")],
            "The first pair carries food, with the intestines as resting-place.",
            "द्वे वहतोऽन्नमन्त्राश्रयेण."),
        order(1, "Put the items of unit 54 in the line's order.",
              ["अन्नम्", "तोयं", "मूत्रं", "शुक्रं", "मुंचतः"],
              "Food, water, urine, semen; and two release.",
              "अन्नम् → तोयं → मूत्रं → शुक्रं → मुंचतः."),
        match(2, "Match each word of unit 54 to its meaning.",
              [["अन्न", "food"], ["तोय", "water"], ["मूत्र", "urine"], ["शुक्र", "semen (śukra)"],
               ["वहतः", "the two carry"], ["मुञ्चतः", "the two release"]],
              "Two carry food, water, urine, śukra; and two release.",
              "अन्न, तोय, मूत्र, शुक्र; वहतः, मुञ्चतः.", role="extend",
              teaches="वहतः and मुञ्चतः are 3rd person dual present: 'the two carry / release', agreeing with द्वे."),
        mcq("discriminate", 3, "Which split of वहतोऽन्नम् in unit 54 is right?",
            ("वहतः + अन्नम्", "अः before अ becomes ओ and the अ drops (ऽ): वहतोऽन्नम्."),
            [("वहत + अन्नम्", "अ + अ would give आ: वहतान्नम्."),
             ("वहते + अन्नम्", "ए + अ would give वहतेऽन्नम्, with ए kept."),
             ("वहतौ + अन्नम्", "औ + अ would give आव्: वहतावन्नम्.")],
            "वहतः (the two carry) + अन्नम् (food): अः + अ → ओऽ.",
            "अः before अ → ओ, with the अ shown as ऽ."),
        multi("apply", 4, "Which statements fit unit 54?",
              [("One pair carries water", "Right: द्वे तोयम्."),
               ("The line states what is released", "The object of मुञ्चतः is not stated."),
               ("Eight carry the water", "Water is carried by two (द्वे तोयम्), not eight."),
               ("Each named task has two", "Right: every item has द्वे (two).")],
              [0, 3],
              "Pairs for food, water, urine, śukra, and a releasing pair; what is released is unstated.",
              "द्वे ... द्वे ... द्वे ... द्वे ... द्वे च मुञ्चतः."),
        mcq("transfer", 5, "By the rule of वहतः + अन्नम् → वहतोऽन्नम्, how is नरः + अयम् (this man) joined in a new example?",
            ("नरोऽयम्", "अः before अ becomes ओ and the अ drops (ऽ), as वहतः + अन्नम् → वहतोऽन्नम्."),
            [("नरायम्", "आ comes from अ + अ with no visarga; here अः meets अ."),
             ("नर अयम्", "अः drops to अ only before vowels other than अ."),
             ("नरर्यम्", "र् comes from a visarga after vowels other than अ/आ.")],
            "नरः + अयम् = नरोऽयम्, like वहतः + अन्नम् = वहतोऽन्नम्.",
            "अः + अ → ओऽ.",
            teaches="अः before अ becomes ओ and the अ is elided (ऽ): वहतः + अन्नम् → वहतोऽन्नम्."),
    ],
}

# ---------------------------------------------------------------- unit 55
AUTHORED["55"] = {
    "title": "ते एव नारीणामार्तवं",
    "question": "By unit 55, what is named for women, and why do ते and एव stay apart?",
    "rule": ("Those very two (ते एव): of women (नारीणाम्), ārtava (आर्तवम्, menstrual blood). ते is a dual in ए, which "
             "takes no sandhi before a vowel."),
    "limits": ("Prose. The verb (carry) is carried over from card 54 and not printed. Which pair ते refers to is not "
               "stated (probably the śukra pair of card 54): no question on it."),
    "explain_hi": ("यह गद्य-पंक्ति कहती है: वे ही दोनों, नारियों का आर्तव यानी रजोरक्त (वहन करती हैं)। "
                   "क्रिया ‘वहन करती हैं’ इकाई ५४ से समझी जाती है, यहाँ छपी नहीं। "
                   "‘ते’ सम्भवतः इकाई ५४ के शुक्र वाले जोड़े की ओर है (इकाई ५१ से मेल), पर पंक्ति यह नहीं कहती। "
                   "‘ते’ यहाँ स्त्रीलिंग द्विवचन है; द्विवचन का -ए स्वर से पहले सन्धि नहीं करता, इसलिए ‘ते एव’ अलग रहे। "
                   "नारीणाम् + आर्तवम् में स्वर से पहले म् जुड़ गया।"),
    "hook": "वही दो: स्त्रियों में आर्तव।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 55, what is named for women?",
            ("Ārtava (menstrual blood)", "नारीणामार्तवम्: of women, ārtava."),
            [("Śukra (semen of a man)", "Śukra is named for a man (नरस्य, card 51), not for women; unit 55 names ārtava."),
             ("Sveda (sweat of the body)", "Sveda is not named in unit 55."),
             ("Mūtra (the urine)", "Mūtra is not named in unit 55.")],
            "Those very two: of women, ārtava.",
            "ते एव नारीणामार्तवम्."),
        order(1, "Put the words of unit 55 in the line's order.",
              ["ते", "एव", "नारीणाम्", "आर्तवं"],
              "Those two, very, of women, ārtava.",
              "ते → एव → नारीणाम् → आर्तवं."),
        match(2, "Match each word of unit 55 to its meaning.",
              [["ते", "those two"], ["एव", "very, alone"], ["नारीणाम्", "of women"], ["आर्तवम्", "ārtava (menstrual blood)"]],
              "Those very two: of women, ārtava.",
              "ते, एव, नारीणाम्, आर्तवम्.", role="extend",
              teaches="नारीणाम् is the genitive plural of नारी: 'of women'."),
        mcq("discriminate", 3, "Why are ते and एव not joined in unit 55?",
            ("ते is a dual in ए, which takes no sandhi", "Dual endings in ए stay unjoined before a vowel (data: ते = f. nom. du.)."),
            [("Sandhi is never made before the word एव", "Sandhi is made before एव (तत्र + एव → तत्रैव)."),
             ("ते ends in a consonant, so no vowel joins", "ते ends in the vowel ए."),
             ("The print dropped a letter between the two", "No flag is noted; the separation is regular.")],
            "ते (dual) + एव: a dual in ए stays unjoined.",
            "A dual ending in ई, ऊ or ए takes no sandhi before a vowel."),
        mcq("apply", 4, "Which verb is understood in unit 55?",
            ("Carry, carried over from unit 54", "Data: the verb (carry) is carried from unit 54 and not supplied."),
            [("Satiate, taken over from unit 56", "अभितर्पयन्ति belongs to the remaining eight of unit 56."),
             ("Are grasped, taken over from unit 50", "गृह्यन्ते is said of the sense-objects in unit 50."),
             ("Sleeps, taken over from unit 51", "स्वपिति is one of the acts of unit 51.")],
            "Those very two (carry) ārtava in women.",
            "ते एव नारीणामार्तवं (वहतः)."),
        mcq("transfer", 5, "By the rule of ते एव, how is फले + अत्र (the two fruits here) written in a new example?",
            ("फले अत्र", "The dual in ए stays unjoined, as ते एव."),
            [("फलेऽत्र", "ए + अ → एऽ is for an ए that is not a dual ending."),
             ("फलयत्र", "अय् comes from ए before a vowel, but not from a dual ए."),
             ("फला अत्र", "The dual ए does not turn into आ; it stays: फले अत्र.")],
            "फले (two fruits) + अत्र stays फले अत्र, like ते एव.",
            "Dual -ए before a vowel: no sandhi.",
            teaches="Dual forms ending in ई, ऊ or ए take no sandhi before a vowel: ते एव, फले अत्र."),
    ],
}

# ---------------------------------------------------------------- unit 56
AUTHORED["56"] = {
    "title": "द्वे ... स्थूलांत्रप्रतिबद्धे · शेषास्त्वष्टौ",
    "question": "By unit 56, what is said of the next pair and of the remaining eight?",
    "rule": ("Two (द्वे), bound to the large intestine (स्थूलान्त्रप्रतिबद्धे), expel stool (on a conjectural reading); "
             "but the remaining eight (शेषास्त्वष्टौ), running crosswise (तिरश्चीनाः), satiate the sweat (स्वेदम् अभितर्पयन्ति)."),
    "limits": ("Prose. The printed वज्र्रोनिरसन्यौ is read as 'expelling stool' only by conjecture: no question on what "
               "the pair expels. The 'remaining eight' presumably complete a count not given in this line."),
    "explain_hi": ("इस गद्य-पंक्ति के दो भाग हैं। "
                   "पहला: दो, स्थूल आँत (बड़ी आँत) से बँधी; छपा ‘वज्र्रोनिरसन्यौ’ अर्थ नहीं देता, उसे अनुमानित पाठ ‘वर्चोनिरसन्यौ’ (मल निकालने वाली) पढ़ा गया है। "
                   "दूसरा: शेष आठ तिरछी जाने वाली हैं और स्वेद (पसीने) को तृप्त करती हैं; ‘अभितर्पयन्ति’ का अंग्रेज़ी भाव ‘पोषण करती हैं’ है। "
                   "‘शेष आठ’ किस गिनती को पूरा करती हैं, यह इस पंक्ति में नहीं। "
                   "सन्धि: शेषाः + तु → शेषास्तु, तु + अष्टौ → त्वष्टौ।"),
    "hook": "दो बड़ी आँत से बँधी; बाकी आठ तिरछी, पसीने को तृप्त।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 56, what do the remaining eight do?",
            ("They satiate sweat (sveda)", "शेषास्त्वष्टौ ... स्वेदमभितर्पयन्ति."),
            [("They carry the tears (aśru)", "Tears are not named in unit 56."),
             ("They carry the urine (mūtra)", "Urine is not named in unit 56."),
             ("They carry the food (anna)", "Food is carried by two (unit 54), not by the remaining eight.")],
            "The remaining eight, running crosswise, satiate the sweat.",
            "शेषास्त्वष्टौ तिरश्चीनाः स्वेदमभितर्पयन्ति."),
        order(1, "Put the printed words of unit 56 in the line's order.",
              ["द्वे", "वज्र्रोनिरसन्यौ", "स्थूलांत्रप्रतिबद्धे", "शेषास्त्वष्टौ", "तिरश्चीनाः", "स्वेदमभितर्पयंति"],
              "Two, (expelling, conjectural), bound to the large intestine; the remaining eight, crosswise, satiate the sweat.",
              "द्वे → वज्र्रोनिरसन्यौ → स्थूलांत्रप्रतिबद्धे → शेषास्त्वष्टौ → तिरश्चीनाः → स्वेदमभितर्पयंति."),
        match(2, "Match each word part of unit 56 to its meaning.",
              [["स्थूल", "thick, large"], ["अन्त्र", "intestine"], ["प्रतिबद्ध", "bound to"], ["शेष", "remaining"],
               ["तिरश्चीन", "running crosswise"], ["स्वेद", "sweat"]],
              "स्थूल-अन्त्र-प्रतिबद्धे = bound to the large intestine; शेषाः तिरश्चीनाः = the remaining, crosswise; स्वेद = sweat.",
              "स्थूल, अन्त्र, प्रतिबद्ध, शेष, तिरश्चीन, स्वेद.", role="extend",
              teaches="स्थूलान्त्र = स्थूल (large) + अन्त्र (intestine), with अ + अ → आ."),
        mcq("discriminate", 3, "Which split of शेषास्त्वष्टौ in unit 56 is right?",
            ("शेषाः + तु + अष्टौ", "Visarga before त → स्; उ before अ → व्: शेषास्त्वष्टौ."),
            [("शेषात् + तु + अष्टौ", "त् + त would give शेषात्तु, not शेषास्तु."),
             ("शेषाः + तौ + अष्टौ", "औ before अ would give आव्: तावष्टौ."),
             ("शेषाः + त्वा + अष्टौ", "आ + अ would give आ: त्वाष्टौ.")],
            "शेषाः (remaining) + तु (but) + अष्टौ (eight).",
            "Visarga before त → स्; उ + a different vowel → व्."),
        multi("apply", 4, "Which statements fit unit 56?",
              [("The reading 'expelling stool' is certain", "It is conjectural: the printed word gives no sense."),
               ("Two are bound to the large intestine", "Right: स्थूलान्त्रप्रतिबद्धे (f. nom. du.)."),
               ("The remaining eight carry śukra", "Śukra is not named in unit 56; they satiate the sweat."),
               ("The remaining eight run crosswise", "Right: तिरश्चीनाः.")],
              [1, 3],
              "Two bound to the large intestine; eight crosswise that satiate the sweat.",
              "स्थूलान्त्रप्रतिबद्धे; शेषास्त्वष्टौ तिरश्चीनाः."),
        mcq("transfer", 5, "By the rule of तु + अष्टौ → त्वष्टौ, how is तु + अत्र (but here) joined in a new example?",
            ("त्वत्र", "उ before a different vowel becomes व्, as तु + अष्टौ → त्वष्टौ."),
            [("तोत्र", "ओ comes from अ + उ, not from उ + अ."),
             ("त्वात्र", "त्वा- would need आ; here उ meets a short अ."),
             ("तूत्र", "ऊ comes from उ + उ; here उ meets अ.")],
            "तु + अत्र = त्वत्र, like तु + अष्टौ = त्वष्टौ.",
            "उ + a different vowel → व्.",
            teaches="उ before a different vowel becomes व्: तु + अष्टौ → त्वष्टौ."),
    ],
}

# ---------------------------------------------------------------- unit 57
AUTHORED["57"] = {
    "title": "तिर्यग्गामिन्यश्चतस्रो",
    "question": "By unit 57, what becomes of the four that go crosswise?",
    "rule": ("The four that go crosswise (तिर्यग्गामिन्यश्चतस्रः), being divided (भिद्यमानाः), become very manifold "
             "(सुबहुधा); this was stated before (इत्युक्तं प्राक्)."),
    "limits": ("Prose. The printed singular भवति beside a plural subject is flagged (भवन्ति possible): no question on the "
               "verb's number. What 'before' points to is not settled (probably card 47; perhaps an earlier chapter)."),
    "explain_hi": ("यह गद्य-पंक्ति तिरछी जाने वाली चार की बात करती है: वे बँटती हुई बहुत प्रकार की हो जाती हैं, यह पहले कहा जा चुका है। "
                   "‘प्राक्’ (पहले) सम्भवतः इकाई ४७ के ‘चतस्रस्तिर्यक्’ की ओर है, पर किसी पिछले अध्याय की ओर भी हो सकता है। "
                   "छपा ‘भवति’ एकवचन है, जबकि कर्ता बहुवचन है; ‘भवन्ति’ सम्भावित सुधार है। "
                   "सन्धि: तिर्यक् + गामिन्यः → तिर्यग्गामिन्यः (घोष व्यंजन से पहले क् → ग्), गामिन्यः + चतस्रः → -न्यश्चतस्रः, चतस्रः + भिद्यमानाः → चतस्रो भिद्यमानाः।"),
    "hook": "तिरछी चार: बँटकर बहुत-सी।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 57, what happens to the four that go crosswise?",
            ("Dividing, they become very manifold", "भिद्यमानाः सुबहुधा: being divided, very manifold."),
            [("Reaching the heart, they become three", "That is said of the upward-going ones (card 48)."),
             ("They stay single and are not divided", "भिद्यमानाः says they are being divided."),
             ("They carry the food and the water", "Food and water pairs are in unit 54, not these four.")],
            "The four crosswise ones, being divided, become very manifold.",
            "तिर्यग्गामिन्यश्चतस्रो भिद्यमानाः सुबहुधा."),
        order(1, "Put the printed words of unit 57 in the line's order.",
              ["तिर्यग्गामिन्यश्चतस्रो", "भिद्यमानाः", "सुबहुधा", "भवतीत्युक्तं", "प्राक्"],
              "Crosswise-going four, being divided, very manifold, become: thus said, before.",
              "तिर्यग्गामिन्यश्चतस्रो → भिद्यमानाः → सुबहुधा → भवतीत्युक्तं → प्राक्."),
        match(2, "Match each word part of unit 57 to its meaning.",
              [["तिर्यक्", "crosswise"], ["गामिनी", "going"], ["चतस्रः", "four"], ["भिद्यमान", "being split, dividing"],
               ["सुबहुधा", "in very many ways"], ["प्राक्", "before, earlier"]],
              "The four crosswise-going ones, dividing, become very manifold; said before.",
              "तिर्यक्, गामिनी, चतस्रः, भिद्यमान, सुबहुधा, प्राक्.", role="extend",
              teaches="भिद्यमान is a present passive participle of √भिद्: 'being split'."),
        mcq("discriminate", 3, "Which split of तिर्यग्गामिन्यः in unit 57 is right?",
            ("तिर्यक् + गामिन्यः", "क् before a voiced consonant (ग) becomes ग्: तिर्यग्गामिन्यः."),
            [("तिर्यत् + गामिन्यः", "त् before ग would give द्: तिर्यद्गामिन्यः."),
             ("तिर्यम् + गामिन्यः", "म् before a consonant would be written ं: तिर्यंगामिन्यः."),
             ("तिर्यः + गामिन्यः", "अः before a voiced consonant would give ओ: तिर्योगामिन्यः.")],
            "तिर्यक् (crosswise) + गामिन्यः (going): क् → ग् before ग.",
            "A final क् before a voiced consonant → ग्."),
        mcq("apply", 4, "In unit 57, how are चतस्रः + भिद्यमानाः joined?",
            ("चतस्रो भिद्यमानाः", "अः before a voiced consonant (भ) becomes ओ."),
            [("चतस्रा भिद्यमानाः", "आ does not come from अः before a consonant."),
             ("चतस्रर्भिद्यमानाः", "र् comes from a visarga after vowels other than अ/आ."),
             ("चतस्रस्भिद्यमानाः", "स् comes from a visarga before त/थ, not before भ.")],
            "चतस्रः + भिद्यमानाः = चतस्रो भिद्यमानाः.",
            "अः before a voiced consonant → ओ."),
        mcq("transfer", 5, "By the rule of तिर्यक् + गामिन्यः → तिर्यग्गामिन्यः, how is वाक् + देवी joined in a new example?",
            ("वाग्देवी", "क् before a voiced consonant (द) becomes ग्, as in तिर्यग्गामिन्यः."),
            [("वाक्देवी", "क् does not stay before a voiced consonant."),
             ("वाच्देवी", "च् is not the sandhi form of क् before द."),
             ("वाख्देवी", "ख् is not voiced; before द the क् becomes ग्.")],
            "वाक् + देवी = वाग्देवी, like तिर्यक् + गामिन्यः = तिर्यग्गामिन्यः.",
            "Final क् before a voiced consonant → ग्.",
            teaches="A final क् becomes ग् before a voiced consonant: तिर्यक् + गामिन्यः → तिर्यग्गामिन्यः."),
    ],
}

# ---------------------------------------------------------------- unit 58
AUTHORED["58"] = {
    "title": "स्रोतांसि पुंसां नव",
    "question": "By unit 58, which are the nine srotas (openings) of men, and which three are added for women?",
    "rule": ("The srotas of men are nine: two ears, two eyes, two nostrils, mouth, anus (पायु) and urinary passage; "
             "women have three others: the two breasts and the blood-passage (रक्तपथ)."),
    "limits": ("Prose; the copula is understood. The nine are counted as listed (2 + 2 + 2 + 1 + 1 + 1). रक्तपथ is not "
               "explained in the line; 'passage of the menstrual blood' is probable, not certain. Srotas is kept as a term."),
    "explain_hi": ("यह गद्य-पंक्ति शरीर के बाहरी स्रोतस यानी मार्ग या द्वार गिनाती है। "
                   "पुरुषों के नौ: दो कान, दो नेत्र, दो नासापुट (नथुने), मुख, पायु (गुदा) और मूत्रमार्ग; २ + २ + २ + १ + १ + १ = ९। "
                   "स्त्रियों के तीन अन्य: दोनों स्तन और रक्तपथ, यानी सम्भवतः रजोरक्त का मार्ग (सम्भावित)। "
                   "कर्णौ, नासापुटौ, स्तनौ (पुंलिंग) और नेत्रे (नपुंसकलिंग) द्विवचन हैं। "
                   "यह इकाई स्रोतस वाले नए खण्ड का आरम्भ है।"),
    "hook": "नौ द्वार सबके; स्त्रियों के तीन और: दो स्तन, रक्तपथ।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 58, how many srotas (openings) do men have?",
            ("Nine", "स्रोतांसि पुंसां नव: the srotas of men are nine."),
            [("Three", "Three are the others added for women."),
             ("Twelve", "Nine for men; twelve would add the women's three."),
             ("Thirteen", "Thirteen is the count of the inner srotas (unit 59).")],
            "The srotas of men are nine.",
            "स्रोतांसि पुंसां नव."),
        order(1, "Put the men's openings in the order of unit 58.",
              ["कर्णौ", "नेत्रे", "नासापुटौ", "मुखं", "पायुः", "मूत्रपथः"],
              "Ears, eyes, nostrils, mouth, anus, urinary passage.",
              "कर्णौ → नेत्रे → नासापुटौ → मुखं → पायुः → मूत्रपथः."),
        match(2, "Match each word of unit 58 to its meaning.",
              [["कर्णौ", "two ears"], ["नेत्रे", "two eyes"], ["नासापुटौ", "two nostrils"], ["मुखम्", "mouth"],
               ["पायुः", "anus"], ["स्तनौ", "two breasts"]],
              "Ears, eyes, nostrils, mouth, anus; the breasts for women.",
              "कर्णौ, नेत्रे, नासापुटौ, मुखम्, पायुः, स्तनौ.", role="extend",
              teaches="The duals count two each: कर्णौ, नासापुटौ, स्तनौ (m. -औ) and नेत्रे (n. -ए)."),
        mcq("discriminate", 3, "By unit 58, which is one of the women's three others, not of the men's nine?",
            ("The two breasts (stanau)", "स्त्रीणां स्तनौ: the breasts are among the women's three."),
            [("The mouth (mukha)", "The mouth is among the men's nine."),
             ("The anus (pāyu)", "The anus is among the men's nine."),
             ("The urinary passage (mūtrapatha)", "The urinary passage is among the men's nine.")],
            "Women's three others: two breasts and the blood-passage.",
            "अन्यानि च त्रीणि स्त्रीणां स्तनौ रक्तपथश्च."),
        multi("apply", 4, "Which are among the men's nine by unit 58?",
              [("The two nostrils", "Right: नासापुटौ."),
               ("The blood-passage", "रक्तपथ is among the women's three others."),
               ("The urinary passage", "Right: मूत्रपथः."),
               ("The two breasts", "स्तनौ are among the women's three others.")],
              [0, 2],
              "Men's nine: ears, eyes, nostrils, mouth, anus, urinary passage.",
              "कर्णौ नेत्रे नासापुटौ मुखं पायुर्मूत्रपथः."),
        mcq("transfer", 5, "By the pattern of कर्ण → कर्णौ (the two ears), what is the nominative dual of the masculine हस्त (hand)?",
            ("हस्तौ", "A masculine अ-stem takes -औ in the nominative dual, as कर्ण → कर्णौ."),
            [("हस्ताः", "हस्ताः is the nominative plural: hands, more than two."),
             ("हस्ते", "For masculine हस्त, हस्ते is the locative singular: in the hand."),
             ("हस्तम्", "हस्तम् is the accusative singular: the hand.")],
            "हस्तौ = the two hands, like कर्णौ = the two ears.",
            "Masculine अ-stem, nominative dual: -औ.",
            teaches="A masculine अ-stem takes -औ in the nominative dual: कर्ण → कर्णौ, नासापुट → नासापुटौ."),
    ],
}

# ---------------------------------------------------------------- unit 59
AUTHORED["59"] = {
    "title": "तथाऽपराण्यंतःस्रोतांसि",
    "question": "By unit 59, how many are the other inner srotas, and of what are they the seats?",
    "rule": ("Other inner srotas (अपराणि अन्तःस्रोतांसि): seats of life (जीवितायतनानि), thirteen (त्रयोदश); seats of "
             "prāṇa, water, food, the dhātus and the malas."),
    "limits": ("Prose; the copula is understood. The thirteen are not listed in this line (cards 60 to 73 name some). "
               "The two predicates are read as describing the same srotas. Dhātu and mala are kept as terms."),
    "explain_hi": ("यह गद्य-पंक्ति शरीर के भीतरी स्रोतस की बात करती है: ये तेरह हैं और जीवन के आयतन यानी आश्रय हैं। "
                   "ये प्राण, उदक (जल), अन्न, धातु और मल के आयतन हैं; ये पाँच इसी क्रम में छपे हैं। "
                   "तेरह के नाम यहाँ नहीं गिनाए गए; आगे की इकाइयाँ (६० से ७३) उनमें से कुछ बताती हैं। "
                   "धातु और मल शास्त्रीय शब्द हैं, इनका कोई आधुनिक नाम नहीं दिया गया। "
                   "सन्धि: प्राण + उदक → प्राणोदक (अ + उ → ओ), उदक + अन्न → उदकान्न (अ + अ → आ)।"),
    "hook": "भीतर तेरह: प्राण, जल, अन्न, धातु, मल के घर।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 59, how many are the other inner srotas?",
            ("Thirteen", "त्रयोदश: thirteen."),
            [("Nine", "Nine are the men's outer openings (unit 58)."),
             ("Three", "Three are the women's added openings (unit 58)."),
             ("Twenty-four", "Twenty-four is not the count of the inner srotas.")],
            "The other inner srotas, seats of life, are thirteen.",
            "अपराण्यन्तःस्रोतांसि जीवितायतनानि त्रयोदश."),
        order(1, "Put the five of whom the srotas are seats in the order of unit 59.",
              ["प्राण", "उदक", "अन्न", "धातु", "मल"],
              "Prāṇa, water, food, dhātu, mala.",
              "प्राण → उदक → अन्न → धातु → मल."),
        match(2, "Match each word of unit 59 to its meaning.",
              [["अपर", "other"], ["अन्तः", "inner, within"], ["जीवित", "life"], ["आयतन", "seat, abode"],
               ["त्रयोदश", "thirteen"], ["उदक", "water"]],
              "Other inner srotas: seats of life, thirteen; seats of prāṇa, water ...",
              "अपर, अन्तः, जीवित, आयतन, त्रयोदश, उदक.", role="extend",
              teaches="आयतन = seat, abode: the srotas are called seats of life and of prāṇa, water, food, dhātu, mala."),
        mcq("discriminate", 3, "Which split of प्राणोदक in unit 59 is right?",
            ("प्राण + उदक", "अ + उ → ओ: प्राण + उदक → प्राणोदक."),
            [("प्राणः + उदक", "अः before a vowel other than अ becomes अ with no join: प्राण उदक."),
             ("प्राणे + उदक", "ए before उ would give अयु or अ उ, not ओ."),
             ("प्राणौ + उदक", "औ before उ would give आवु: प्राणावुदक.")],
            "प्राण (vital breath) + उदक (water): अ + उ → ओ.",
            "अ + उ → ओ."),
        mcq("apply", 4, "What does unit 59 leave unlisted?",
            ("The names of the thirteen", "The line gives the count, not the list (cards 60 to 73 name some)."),
            [("The number of the inner srotas", "The number is printed: त्रयोदश."),
             ("That the srotas are seats of life", "Printed: जीवितायतनानि."),
             ("That the srotas are seats of food", "Printed: अन्न is among the five.")],
            "Count and function are given; the thirteen are not listed here.",
            "त्रयोदश ... आयतनानि: no list."),
        mcq("transfer", 5, "By the rule of प्राण + उदक → प्राणोदक, how is सूर्य + उदयः (sunrise) joined in a new example?",
            ("सूर्योदयः", "अ + उ → ओ, as प्राण + उदक → प्राणोदक."),
            [("सूर्यौदयः", "औ comes from अ + ओ/औ, not from अ + उ."),
             ("सूर्युदयः", "अ does not drop before उ; the two merge into ओ."),
             ("सूर्यादयः", "आ comes from अ + अ/आ, not from अ + उ.")],
            "सूर्य + उदयः = सूर्योदयः, like प्राण + उदक = प्राणोदक.",
            "अ + उ → ओ.",
            teaches="अ before उ merges into ओ: प्राण + उदक → प्राणोदक."),
    ],
}

# ---------------------------------------------------------------- unit 60
AUTHORED["60"] = {
    "title": "तत्र प्राणवाहिनां हृदयं मूलं",
    "question": "By unit 60, what is the root (mūla) of the prāṇa-carrying (srotas)?",
    "rule": ("There, of the prāṇa-carrying (ones) (प्राणवाहिनाम्), the root (मूलम्) is the heart (हृदयम्) and the great "
             "channel (महास्रोतः)."),
    "limits": ("Prose. 'Srotas' is not printed: the 'ones' are the prāṇa-carrying srotas of card 59. Mahāsrotas is kept "
               "as 'great channel'; its identity is disputed (alimentary tract, or the large vessels at the heart): no "
               "question on what it is."),
    "explain_hi": ("यह गद्य-पंक्ति पहला भीतरी स्रोतस लेती है: प्राण को वहन करने वालों का मूल हृदय और महास्रोतस है। "
                   "‘वहन करने वाले’ के साथ ‘स्रोतस’ शब्द छपा नहीं; ये इकाई ५९ के स्रोतस हैं। "
                   "महास्रोतस का शब्दार्थ ‘बड़ा मार्ग’ है; इसकी पहचान विवादित है: चरक-परम्परा में आहार-मार्ग (कोष्ठ), कुछ टीकाकार हृदय की बड़ी वाहिकाएँ मानते हैं। "
                   "हृदय (मानक) यहाँ मूल है। "
                   "सन्धि: महास्रोतः + च → महास्रोतश्च (च से पहले विसर्ग → श्)।"),
    "hook": "प्राणवह का मूल: हृदय और महास्रोतस।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 60, what is the root of the prāṇa-carrying (srotas)?",
            ("The heart and the great channel", "हृदयं मूलं महास्रोतश्च."),
            [("The palate and the kloma organ", "Palate and kloma are the roots of the water-carrying ones (unit 64)."),
             ("The navel and the large intestine", "Navel and intestine are not named in unit 60."),
             ("The neck and the two nostrils", "Neck and nostrils are not named in unit 60.")],
            "Of the prāṇa-carrying ones, the root is the heart and the great channel.",
            "प्राणवाहिनां हृदयं मूलं महास्रोतश्च."),
        match(1, "Match each word of unit 60 to its meaning.",
              [["तत्र", "there, among these"], ["प्राण", "vital breath"], ["वाहिन्", "carrying"], ["हृदय", "heart"],
               ["मूल", "root, origin"]],
              "There, of the prāṇa-carrying ones, the root is the heart ...",
              "तत्र, प्राण, वाहिन्, हृदय, मूल."),
        order(2, "Put the printed words of unit 60 in the line's order.",
              ["तत्र", "प्राणवाहिनां", "हृदयंमूलं", "महास्रोतश्च"],
              "There, of the prāṇa-carrying, the heart the root, and the great channel.",
              "तत्र → प्राणवाहिनां → हृदयंमूलं → महास्रोतश्च.", role="extend",
              teaches="Each srotas entry names its carriers in the genitive plural (-वाहिनाम्), then its root (मूलम्)."),
        mcq("discriminate", 3, "Which split of महास्रोतश्च in unit 60 is right?",
            ("महास्रोतः + च", "Visarga before च → श्: महास्रोतश्च."),
            [("महास्रोतम् + च", "म् before a consonant would be written ं: महास्रोतं च."),
             ("महास्रोतत् + च", "त् before च would give च्: महास्रोतच्च."),
             ("महास्रोते + च", "ए before a consonant stays ए: महास्रोते च.")],
            "महास्रोतः (great channel) + च (and): visarga → श् before च.",
            "Visarga before च → श्."),
        multi("apply", 4, "Which statements fit unit 60?",
              [("The line identifies the great channel", "It does not; the identity of mahāsrotas is disputed."),
               ("The palate is named as a root", "The palate is the root of the water-carrying ones (unit 64)."),
               ("The heart is named as a root", "Right: हृदयं मूलम्."),
               ("The root is given for the prāṇa-carrying ones", "Right: प्राणवाहिनाम्.")],
              [2, 3],
              "Of the prāṇa-carrying ones: heart and great channel; the great channel is not identified.",
              "प्राणवाहिनां हृदयं मूलं महास्रोतश्च."),
        mcq("transfer", 5, "By the pattern of प्राणवाहिन् → प्राणवाहिनाम् (of the carrying ones), what is the genitive plural of बलिन् (strong)?",
            ("बलिनाम्", "An इन्-stem takes -इनाम् in the genitive plural, as वाहिन् → वाहिनाम्."),
            [("बलिनः", "बलिनः is nominative/accusative plural or genitive/ablative singular, not genitive plural."),
             ("बलिभिः", "बलिभिः is the instrumental plural: by the strong."),
             ("बलिने", "बलिने is the dative singular: for the strong one.")],
            "बलिनाम् = of the strong, like प्राणवाहिनाम् = of the prāṇa-carrying.",
            "इन्-stem, genitive plural: -इनाम्.",
            teaches="An इन्-stem takes -इनाम् in the genitive plural: प्राणवाहिन् → प्राणवाहिनाम्."),
    ],
}

# ---------------------------------------------------------------- unit 61
AUTHORED["61"] = {
    "title": "तानि क्षयरौक्ष्य ... दुष्यंति",
    "question": "By unit 61, by what causes do the prāṇa-carrying srotas become vitiated?",
    "rule": ("They (तानि) become vitiated (दुष्यन्ति) by wasting (क्षय), dryness (रौक्ष्य), thirst (पिपासा), hunger (क्षुध्), "
             "exertion (व्यायाम), holding back of urges (वेगधारण) and the like (आदिभिः)."),
    "limits": ("Prose. 'And the like' leaves the list open. क्षय here is wasting, loss, as a cause, not a disease name. "
               "The print breaks व्यायाम across two tokens (a spacing slip)."),
    "explain_hi": ("यह गद्य-पंक्ति बताती है कि प्राणवह स्रोतस (इकाई ६०) किन कारणों से दूषित होते हैं। "
                   "कारण इस क्रम में हैं: क्षय (क्षीणता), रूक्षता, प्यास (पिपासा), भूख (क्षुध्), व्यायाम, और वेगों को रोकना (वेगधारण); ‘आदि’ से सूची खुली रहती है। "
                   "यहाँ क्षय का अर्थ क्षीणता या हानि है, किसी रोग का नाम नहीं। "
                   "छपाई में ‘व्याया मवेग’ अलग-अलग छपा है; यह शब्द व्यायाम ही है। "
                   "सन्धि: आदिभिः + दुष्यन्ति → आदिभिर्दुष्यन्ति (इ के बाद विसर्ग, घोष व्यंजन से पहले र्)।"),
    "hook": "क्षय, रूखापन, प्यास, भूख, व्यायाम, वेग रोकना: प्राणवह दूषित।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 61, what happens to the prāṇa-carrying srotas through these causes?",
            ("They become vitiated (duṣyanti)", "दुष्यन्ति: they become vitiated, spoiled."),
            [("They become very manifold (bahudhā)", "Becoming manifold is said of the crosswise four (unit 57)."),
             ("They are nourished (tarpita)", "Nourishing is not what unit 61 says; दुष्यन्ति = vitiated."),
             ("They are bound (pratibaddha)", "Bound is said in unit 56; unit 61 says दुष्यन्ति.")],
            "By these causes they become vitiated.",
            "तानि ... आदिभिर्दुष्यन्ति."),
        order(1, "Put the causes in the order of unit 61.",
              ["क्षय", "रौक्ष्य", "पिपासा", "क्षुद्", "व्यायाम", "वेगधारण"],
              "Wasting, dryness, thirst, hunger, exertion, holding back of urges.",
              "क्षय → रौक्ष्य → पिपासा → क्षुद् → व्यायाम → वेगधारण."),
        match(2, "Match each cause of unit 61 to its meaning.",
              [["क्षय", "wasting, loss"], ["रौक्ष्य", "dryness"], ["पिपासा", "thirst"], ["क्षुध्", "hunger"],
               ["व्यायाम", "exertion"], ["वेगधारण", "holding back of urges"]],
              "Wasting, dryness, thirst, hunger, exertion, holding back of urges.",
              "क्षय, रौक्ष्य, पिपासा, क्षुध्, व्यायाम, वेगधारण.", role="extend",
              teaches="वेगधारण = वेग (natural urge) + धारण (holding back)."),
        mcq("discriminate", 3, "In unit 61, which word means thirst, not hunger?",
            ("पिपासा", "पिपासा = thirst."),
            [("क्षुद्", "क्षुध् = hunger."),
             ("क्षय", "क्षय = wasting, loss."),
             ("रौक्ष्य", "रौक्ष्य = dryness.")],
            "पिपासा is thirst; क्षुध् is hunger.",
            "पिपासा = thirst; क्षुध् = hunger."),
        mcq("apply", 4, "Which split of आदिभिर्दुष्यंति in unit 61 is right?",
            ("आदिभिः + दुष्यन्ति", "After इ, a visarga before a voiced consonant (द) becomes र्."),
            [("आदिभिम् + दुष्यन्ति", "म् before a consonant would be written ं: आदिभिं दुष्यन्ति."),
             ("आदिभ्यः + दुष्यन्ति", "-भ्यः before द would give आदिभ्यो दुष्यन्ति."),
             ("आदिभे + दुष्यन्ति", "ए before a consonant stays ए: आदिभे दुष्यन्ति.")],
            "आदिभिः (by ... and the like) + दुष्यन्ति (become vitiated): इः → इर् before द.",
            "A visarga after इ before a voiced sound → र्."),
        mcq("transfer", 5, "By the rule of आदिभिः + दुष्यन्ति → आदिभिर्दुष्यन्ति, how is हरिः + गच्छति joined in a new example?",
            ("हरिर्गच्छति", "After इ, a visarga before a voiced consonant becomes र्."),
            [("हरिगच्छति", "The visarga after इ does not drop here; it becomes र्."),
             ("हरिस्गच्छति", "स् comes from a visarga before त/थ, not before ग."),
             ("हरी गच्छति", "Lengthening with loss of र् happens only before र, not before ग.")],
            "हरिः + गच्छति = हरिर्गच्छति, like आदिभिः + दुष्यन्ति = आदिभिर्दुष्यन्ति.",
            "इः before a voiced sound → इर्.",
            teaches="A visarga after इ becomes र् before a voiced sound: आदिभिः + दुष्यन्ति → आदिभिर्दुष्यन्ति."),
    ],
}

# ---------------------------------------------------------------- unit 62
AUTHORED["62"] = {
    "title": "ततोऽतिसृष्टं प्रतिबद्धं ... उच्छ्वसनं",
    "question": "By unit 62, what kinds of breathing follow when the prāṇa-carrying srotas are vitiated?",
    "rule": ("Then (ततः) the breathing (उच्छ्वसनम्) is excessively released, obstructed, agitated, scanty or frequent, "
             "with sound and pain (सशब्दशूलम्)."),
    "limits": ("Prose; no finite verb. The single वा follows 'scanty ... frequent'; whether 'or' runs through the earlier "
               "terms is not settled. सशब्दशूल may also be read 'with noisy pain'."),
    "explain_hi": ("यह गद्य-पंक्ति इकाई ६१ के बाद आती है: तब (ततः) उच्छ्वसन यानी साँस ऐसी होती है। "
                   "रूप इस क्रम में हैं: अतिसृष्ट (अधिक छूटती), प्रतिबद्ध (रुकी हुई), कुपित (क्षुब्ध), अल्पाल्प (थोड़ी-थोड़ी) या अभीक्ष्ण (बार-बार), और शब्द तथा पीड़ा सहित। "
                   "सभी विशेषण नपुंसकलिंग हैं और ‘उच्छ्वसनम्’ से मेल खाते हैं; कोई क्रिया छपी नहीं। "
                   "‘वा’ (या) एक ही बार, अन्तिम जोड़े के बाद आया है; पहले के शब्दों तक भी ‘या’ है या नहीं, यह शब्दों से तय नहीं। "
                   "सन्धि: ततः + अतिसृष्टम् → ततोऽतिसृष्टम् (अः + अ → ओऽ)।"),
    "hook": "साँस: अधिक छूटे, रुके, क्षुब्ध, थोड़ी या बार-बार, शब्द-पीड़ा सहित।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 62, what does the list of features describe?",
            ("The breathing (ucchvasana)", "All the adjectives agree with उच्छ्वसनम्, breathing."),
            [("The thirst (pipāsā)", "Thirst is a cause in unit 61, not what unit 62 describes."),
             ("The holding of urges (vega)", "Holding back urges is a cause in unit 61, not what unit 62 describes."),
             ("The sweat (sveda)", "Sweat is not named in unit 62.")],
            "Unit 62 describes the breathing.",
            "... सशब्दशूलमुच्छ्वसनम्."),
        order(1, "Put the features of the breathing in the order of unit 62.",
              ["अतिसृष्टं", "प्रतिबद्धं", "कुपितम्", "अल्पाल्पम्", "अभीक्ष्णं", "सशब्दशूलम्"],
              "Excessively released, obstructed, agitated, scanty, frequent, with sound and pain.",
              "अतिसृष्टं → प्रतिबद्धं → कुपितम् → अल्पाल्पम् → अभीक्ष्णं → सशब्दशूलम्."),
        match(2, "Match each word of unit 62 to its meaning.",
              [["अतिसृष्ट", "excessively released"], ["प्रतिबद्ध", "obstructed, checked"], ["कुपित", "agitated"],
               ["अल्पाल्प", "scanty, little by little"], ["अभीक्ष्ण", "frequent"], ["उच्छ्वसन", "breathing"]],
              "The breathing: excessively released, obstructed, agitated, scanty or frequent.",
              "अतिसृष्ट, प्रतिबद्ध, कुपित, अल्पाल्प, अभीक्ष्ण, उच्छ्वसन.", role="extend",
              teaches="All the adjectives are neuter, agreeing with उच्छ्वसनम् (breathing)."),
        mcq("discriminate", 3, "In unit 62, which word means 'obstructed, checked'?",
            ("प्रतिबद्धं", "प्रतिबद्ध = obstructed, checked."),
            [("अतिसृष्टं", "अतिसृष्ट = excessively released."),
             ("कुपितम्", "कुपित = agitated, disturbed."),
             ("अभीक्ष्णं", "अभीक्ष्ण = frequent.")],
            "प्रतिबद्ध = obstructed; अतिसृष्ट = excessively released.",
            "प्रतिबद्धम् = obstructed."),
        multi("apply", 4, "Which statements fit unit 62?",
              [("No finite verb is printed", "Right: the line has adjectives and a noun only."),
               ("The line names the disease śvāsa", "Śvāsa is named in unit 63, not here."),
               ("वा certainly links every term", "Not settled: वा follows only the last pair."),
               ("The adjectives agree with उच्छ्वसनम्", "Right: they are neuter, like उच्छ्वसनम्.")],
              [0, 3],
              "No verb; the neuter adjectives describe the breathing; the reach of वा is open.",
              "ततोऽतिसृष्टं ... वा सशब्दशूलमुच्छ्वसनम्."),
        mcq("transfer", 5, "By the rule of अल्प + अल्प → अल्पाल्प, how is न + अस्ति (is not) joined in a new example?",
            ("नास्ति", "अ + अ → आ, as अल्प + अल्प → अल्पाल्प."),
            [("नेस्ति", "ए comes from अ + इ, not from अ + अ."),
             ("नोस्ति", "ओ comes from अ + उ, not from अ + अ."),
             ("नौस्ति", "औ comes from अ + ओ/औ, not from अ + अ.")],
            "न + अस्ति = नास्ति, like अल्प + अल्प = अल्पाल्प.",
            "अ + अ → आ.",
            teaches="अ before अ merges into आ: अल्प + अल्प → अल्पाल्प."),
    ],
}

# ---------------------------------------------------------------- unit 63
AUTHORED["63"] = {
    "title": "तत्र श्वासवत्साधनं",
    "question": "By unit 63, how is the vitiation of the prāṇa-carrying srotas to be treated?",
    "rule": ("There (तत्र), the treatment (साधनम्) is as in śvāsa (श्वासवत्, breathlessness): the text points to the "
             "treatment given elsewhere for śvāsa."),
    "limits": ("Prose; the copula is understood. Śvāsa as the breathlessness disorder (dyspnoea of the asthma type) is "
               "probable. The treatment itself is not repeated here; no dose or remedy is given."),
    "explain_hi": ("यह गद्य-पंक्ति चिकित्सा का संकेत देती है: वहाँ साधन यानी उपचार श्वास के समान है। "
                   "श्वास का अर्थ है कठिनाई से साँस लेना; इसे साँस फूलने का रोग, सम्भवतः दमा जैसा, पढ़ना सम्भावित है। "
                   "उपचार यहाँ दोहराया नहीं गया; पाठ कहीं और बताए गए श्वास के उपचार की ओर संकेत करता है। "
                   "‘-वत्’ का अर्थ है ‘के समान’: श्वासवत् = श्वास के समान। "
                   "छपे ‘श्वासवत्साधनं’ में स से पहले त् नहीं बदलता।"),
    "hook": "उपचार: श्वास जैसा।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 63, the treatment is as in which disorder?",
            ("Śvāsa (breathlessness)", "श्वासवत्साधनम्: treatment as in śvāsa."),
            [("Jvara (the fever)", "Fever is not named in unit 63."),
             ("Tṛṣṇā (the thirst)", "Thirst is not named in unit 63."),
             ("Kāsa (the cough)", "Cough is not named in unit 63.")],
            "There, the treatment is as in śvāsa.",
            "तत्र श्वासवत्साधनम्."),
        match(1, "Match each word part of unit 63 to its meaning.",
              [["तत्र", "there, in this case"], ["श्वास", "breathlessness (śvāsa)"], ["वत्", "like, as in"],
               ["साधन", "treatment"]],
              "There, the treatment is as in śvāsa.",
              "तत्र, श्वास, वत्, साधन."),
        mcq("extend", 2, "What does unit 63 leave unsaid about the treatment?",
            ("Its details: it points to śvāsa's treatment", "The treatment is given elsewhere and not repeated."),
            [("Whether there is any treatment at all", "A treatment is named: साधनम्, as in śvāsa."),
             ("Which disorder's treatment it follows", "The disorder is named: श्वासवत्, as in śvāsa."),
             ("In which case the treatment is applied", "तत्र (there) ties it to the case of the prāṇa-carrying srotas.")],
            "The line names the model (śvāsa) but gives no details.",
            "श्वासवत् = as in śvāsa.",
            teaches="-वत् after a noun as an indeclinable means 'as in, like': श्वासवत् = as in śvāsa."),
        mcq("discriminate", 3, "Which split of श्वासवत्साधनं in unit 63 is right?",
            ("श्वासवत् + साधनम्", "त् before स stays त्: श्वासवत्साधनम्."),
            [("श्वासवः + साधनम्", "A visarga before स stays ः or becomes स्: श्वासवः साधनम्."),
             ("श्वासवन् + साधनम्", "न् before स stays न्; it does not become त्."),
             ("श्वासवते + साधनम्", "ए before a consonant stays ए: श्वासवते साधनम्.")],
            "श्वासवत् (as in śvāsa) + साधनम् (treatment).",
            "Final त् before स stays त्."),
        fill(4, "In unit 63 the treatment follows that of ____ (breathlessness). Type it in Devanagari or in English letters (e.g. dharma).",
             accepts("श्वास", None, "shvasa", "swasa"),
             "श्वास = breathlessness: श्वासवत्साधनम्.",
             "श्वास = breathlessness (probably dyspnoea of the asthma type).",
             "तत्र श्वासवत्साधनम्.", role="apply"),
        mcq("transfer", 5, "By the pattern of श्वासवत् (as in śvāsa), what does ज्वरवत् mean in a new example?",
            ("As in fever", "-वत् = like, as in: ज्वरवत् = as in fever."),
            [("After the fever", "-वत् does not mean after."),
             ("Without the fever", "-वत् does not mean without."),
             ("Caused by fever", "-वत् does not mean caused by.")],
            "ज्वरवत् = as in fever, like श्वासवत् = as in śvāsa.",
            "Noun + वत् = as in, like that noun.",
            teaches="-वत् after a noun as an indeclinable means 'as in, like': श्वासवत्, ज्वरवत्."),
    ],
}

# ---------------------------------------------------------------- unit 64
AUTHORED["64"] = {
    "title": "उदकवाहिनां तालु मूलं क्लोम च",
    "question": "By unit 64, what are the roots of the water-carrying (srotas)?",
    "rule": ("Of the water-carrying (ones) (उदकवाहिनाम्), the root (मूलम्) is the palate (तालु) and the kloma (क्लोम, "
             "identity disputed)."),
    "limits": ("Prose. 'Srotas' is not printed. Kloma is not identified in the line (pancreas, right lung and "
               "trachea/throat have been proposed: disputed): no question on what it is."),
    "explain_hi": ("यह गद्य-पंक्ति दूसरा भीतरी स्रोतस लेती है: जल को वहन करने वालों का मूल तालु और क्लोम है। "
                   "तालु यानी मुँह की छत। "
                   "क्लोम की पहचान विवादित है: अग्न्याशय, दायाँ फेफड़ा और श्वासनली या कण्ठ, सबके सुझाव हैं; इसलिए इसे ‘क्लोम’ ही रखा गया। "
                   "‘स्रोतस’ शब्द छपा नहीं, इकाई ६० की तरह समझा जाता है। "
                   "छपाई में ‘क्लोमच’ जुड़ा है, यानी क्लोम च।"),
    "hook": "जलवह का मूल: तालु और क्लोम।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 64, what is the root of the water-carrying (srotas)?",
            ("The palate and the kloma", "उदकवाहिनां तालु मूलं क्लोम च."),
            [("The heart and the great channel", "Those are the roots of the prāṇa-carrying ones (unit 60)."),
             ("The tongue and the two jaws", "Tongue and jaws are not named in unit 64."),
             ("The navel and the large bowel", "Navel and bowel are not named in unit 64.")],
            "Of the water-carrying ones, the root is the palate and the kloma.",
            "उदकवाहिनां तालु मूलं क्लोम च."),
        order(1, "Put the printed words of unit 64 in the line's order.",
              ["उदकवाहिनां", "तालु", "मूलं", "क्लोमच"],
              "Of the water-carrying, the palate, the root, and the kloma.",
              "उदकवाहिनां → तालु → मूलं → क्लोमच."),
        match(2, "Match each word part of unit 64 to its meaning.",
              [["उदक", "water"], ["वाहिन्", "carrying"], ["तालु", "palate"], ["मूल", "root, origin"]],
              "Of the water-carrying ones, the root is the palate ...",
              "उदक, वाहिन्, तालु, मूल.", role="extend",
              teaches="उदकवाहिनाम् = उदक (water) + वाहिन् (carrying), genitive plural: of the water-carrying ones."),
        mcq("discriminate", 3, "In unit 64, which word means 'palate'?",
            ("तालु", "तालु = palate."),
            [("मूलं", "मूल = root, origin."),
             ("उदक", "उदक = water."),
             ("वाहिनां", "वाहिन् = carrying; वाहिनाम् = of the carrying ones.")],
            "तालु is the palate; मूलम् is the root.",
            "तालु = palate."),
        multi("apply", 4, "Which statements fit unit 64?",
              [("The word 'srotas' is printed", "It is not printed; the 'ones' are understood."),
               ("The palate is named as a root", "Right: तालु मूलम्."),
               ("क्लोमच is printed run together for क्लोम च", "Right: data note."),
               ("The heart is named as a root", "The heart is the root of the prāṇa-carrying ones (unit 60).")],
              [1, 2],
              "Palate and kloma are the roots; 'srotas' is understood; क्लोम च is printed joined.",
              "उदकवाहिनां तालु मूलं क्लोमच."),
        mcq("transfer", 5, "By the rule of मूलम् + क्लोम → मूलं क्लोम, how is फलम् + खादति (eats the fruit) written in a new example?",
            ("फलं खादति", "Final म् before a consonant in a sentence is written ं, as मूलं क्लोम."),
            [("फल खादति", "The म् does not drop; it is written as ं."),
             ("फलो खादति", "ओ comes from अः before a voiced consonant, not from अम्."),
             ("फलः खादति", "फलः changes the word; the ending -म् stays as ं.")],
            "फलम् + खादति = फलं खादति, like मूलम् + क्लोम = मूलं क्लोम.",
            "Final म् before a consonant → ं.",
            teaches="Final म् before a consonant inside a sentence is written as anusvāra: मूलं क्लोम, फलं खादति."),
    ],
}


# ===================================================================== NOTES_HI
NOTES_HI = {
    "52": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। पंक्ति ‘धमनी’ शब्द नहीं कहती; सम्भवतः इकाई ४७ की दस नीचे जाने वाली धमनियाँ। "
           "पक्वाशय = पचे (अन्न, मल) का आशय, सम्भवतः बड़ी आँत का क्षेत्र (सम्भावित)। तीन प्रकार यहाँ नाम से नहीं। जायन्ते = √जन्, "
           "आत्मनेपद वर्तमान, कर्मवाच्य नहीं। सन्धि जाँची: अधः + गमाः → अधोगमाः (अः + घोष व्यंजन → ओ); पक्वाशयस्थाः + एवम् → "
           "पक्वाशयस्था एवम् (आः स्वर से पहले विसर्ग खोता है); एवम् + त्रिधा → एवं त्रिधा; छपा जायंते = जायन्ते।"),
    "53": ("गद्य; विश्वास कम; कोई पाठ-चिह्न नहीं, पर पंक्ति अधूरी और अस्पष्ट है। ‘दशाद्याः’ = दश आद्याः (पहली दस), या ‘दस आदि’; "
           "सम्भवतः इकाई ५२ के नीचे वाले वर्ग की तीस में से पहली दस; ‘पूर्ववत्’ सम्भवतः ऊपर वाले वर्ग की तरह; दोनों संकेत छपे नहीं, "
           "इसलिए कोई क्रिया या संज्ञा नहीं जोड़ी गई; इन पर कोई प्रश्न नहीं। सन्धि जाँची: दश + आद्याः → दशाद्याः (अ + आ → आ)।"),
    "54": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। समूह-टिप्पणी: इकाई ५२-५३ को आगे बढ़ाती दिखती है। जल और मूत्र वाले जोड़ों के "
           "साथ ‘वहतः’ समझा जाता है। ‘मुञ्चतः’ का कर्म छपा नहीं, जोड़ा नहीं गया। ‘अन्त्राश्रयेण’ (तृतीया) सम्भवतः केवल अन्न वाले जोड़े "
           "के लिए। सन्धि जाँची: वहतः + अन्नम् → वहतोऽन्नम् (अः + अ → ओऽ); अन्नम् + अन्त्र... → अन्नमन्त्र...; अन्त्र + आश्रयेण → "
           "अन्त्राश्रयेण (अ + आ → आ); वहतः + द्वे → वहतो द्वे (अः + घोष व्यंजन → ओ); छपे मंत्रा, मुंचतः = मन्त्रा, मुञ्चतः।"),
    "55": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। क्रिया (वहन करती हैं) इकाई ५४ से समझी जाती है। ‘ते’ सम्भवतः इकाई ५४ के शुक्र "
           "वाले जोड़े की ओर (इकाई ५१ से मेल), पर पंक्ति यह नहीं कहती; इस पर कोई प्रश्न नहीं। आर्तव = रजोरक्त (मानक)। सन्धि जाँची: "
           "ते (स्त्रीलिंग द्विवचन) + एव: द्विवचन का -ए प्रगृह्य है, सन्धि नहीं; नारीणाम् + आर्तवम् → नारीणामार्तवम्।"),
    "56": ("गद्य; विश्वास मध्यम। पाठ-चिह्न (सम्भावित): छपा ‘वज्र्रोनिरसन्यौ’ अर्थ नहीं देता (वज्र = वज्र यानी बिजली/इन्द्र का अस्त्र, यहाँ अर्थ नहीं बनता); ‘वर्चोनिरसन्यौ’ "
           "(मल निकालने वाली) अनुमानित पाठ है, र्च/ज्र की भूल सम्भव; इस पर कोई प्रश्न नहीं। ‘शेष आठ’ किसी ऐसी गिनती को पूरा करती "
           "दिखती हैं जो इस पंक्ति में नहीं। ‘अभितर्पयन्ति’ = तृप्त करती हैं (अंग्रेज़ी भाव: पोषण)। सन्धि जाँची: शेषाः + तु → शेषास्तु "
           "(त से पहले विसर्ग → स्); तु + अष्टौ → त्वष्टौ (उ + भिन्न स्वर → व्); स्वेदम् + अभि... → स्वेदमभि...; स्थूल + अन्त्र → "
           "स्थूलान्त्र (अ + अ → आ)।"),
    "57": ("गद्य; विश्वास मध्यम। पाठ-चिह्न (सम्भावित): छपा ‘भवति’ एकवचन, कर्ता बहुवचन; ‘भवन्ति’ सम्भावित; इस पर कोई प्रश्न नहीं। "
           "समूह-टिप्पणी: इकाई ५६ को आगे बढ़ाती दिखती है। ‘प्राक्’ सम्भवतः इकाई ४७ के तिरछी चार की ओर, या किसी पिछले अध्याय की ओर; "
           "तय नहीं। सन्धि जाँची: तिर्यक् + गामिन्यः → तिर्यग्गामिन्यः (घोष व्यंजन से पहले क् → ग्); गामिन्यः + चतस्रः → "
           "गामिन्यश्चतस्रः (च से पहले विसर्ग → श्); चतस्रः + भिद्यमानाः → चतस्रो भिद्यमानाः (अः + घोष व्यंजन → ओ); भवति + इति → "
           "भवतीति (इ + इ → ई); इति + उक्तम् → इत्युक्तम् (इ + उ → यु)।"),
    "58": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। नौ की गिनती छपे क्रम से: २ + २ + २ + १ + १ + १। ‘अन्यानि त्रीणि’ स्त्रियों के: दो "
           "स्तन और रक्तपथ। रक्तपथ = सम्भवतः रजोरक्त का मार्ग (सम्भावित)। पायु = गुदा (मानक)। सन्धि जाँची: पुंसाम् + नव → पुंसां नव "
           "(छपाई में जुड़ा ‘पुंसांनव’); पायुः + मूत्र... → पायुर्मूत्र... (उ के बाद विसर्ग, घोष व्यंजन से पहले र्); मूत्रपथः + अन्यानि → "
           "मूत्रपथोऽन्यानि (अः + अ → ओऽ; छपाई में ‘पथो ऽन्यानि’ अलग); स्त्रीणाम् + स्तनौ → स्त्रीणां स्तनौ; रक्तपथः + च → रक्तपथश्च।"),
    "59": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। ‘त्रयोदश’ छपे अनुसार; तेरह की सूची यहाँ नहीं (इकाई ६० से ७३ कुछ बताती हैं)। दोनों "
           "विधेय एक ही स्रोतस के लिए पढ़े गए। सन्धि जाँची: तथा + अपराणि → तथापराणि (आ + अ → आ; छपा अवग्रह छपाई की आदत); अपराणि + "
           "अन्तः → अपराण्यन्तः (इ + अ → य); प्राण + उदक → प्राणोदक (अ + उ → ओ); उदक + अन्न → उदकान्न (अ + अ → आ); जीवित + आयतन → "
           "जीवितायतन; मलानाम् + आयतनानि → मलानामायतनानि।"),
    "60": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। ‘प्राणवाहिनाम्’ के साथ ‘स्रोतसाम्’ छपा नहीं, इकाई ५९ के स्रोतस। महास्रोतस (विवादित): "
           "चरक-परम्परा में आहार-मार्ग (कोष्ठ), कुछ टीकाकार हृदय की बड़ी वाहिकाएँ; यहाँ तय नहीं, इस पर कोई प्रश्न नहीं। सन्धि जाँची: "
           "हृदयम् + मूलम् → हृदयं मूलम् (छपाई में जुड़ा ‘हृदयंमूलं’); महास्रोतः + च → महास्रोतश्च (च से पहले विसर्ग → श्)।"),
    "61": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। छपाई ‘व्याया | मवेग’ में शब्द टूटा है (रिक्त-स्थान की भूल); म पहले शब्द का, यानी "
           "व्यायाम। ‘तानि’ = इकाई ६० के प्राणवह स्रोतस। क्षय = क्षीणता, हानि (कारणों की सूची में, रोग-नाम नहीं)। वेगधारण = प्राकृत "
           "वेगों को रोकना। सन्धि जाँची: क्षुध् + व्यायाम → क्षुद्व्यायाम (घोष से पहले द्); आदिभिः + दुष्यन्ति → आदिभिर्दुष्यन्ति (इ के बाद "
           "विसर्ग, घोष व्यंजन से पहले र्)।"),
    "62": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। क्रिया नहीं; सभी विशेषण नपुंसकलिंग, ‘उच्छ्वसनम्’ से मेल। एक ही ‘वा’ अन्तिम जोड़े "
           "(अल्पाल्प, अभीक्ष्ण) के बाद; पहले के शब्दों तक ‘या’ है या नहीं, तय नहीं। ‘सशब्दशूल’ = शब्द और पीड़ा सहित, या ‘शब्द वाली पीड़ा’। "
           "सन्धि जाँची: ततः + अतिसृष्टम् → ततोऽतिसृष्टम् (अः + अ → ओऽ); कुपितम् + अल्पाल्पम् + अभीक्ष्णम् → कुपितमल्पाल्पमभीक्ष्णम्; "
           "अल्प + अल्प → अल्पाल्प (अ + अ → आ); सशब्दशूलम् + उच्छ्वसनम् → सशब्दशूलमुच्छ्वसनम्।"),
    "63": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। श्वास = कठिन साँस; साँस फूलने का रोग (दमा जैसा) पढ़ना सम्भावित। उपचार कहीं और "
           "बताया गया है, यहाँ दोहराया नहीं। साधन = साधने का उपाय, चिकित्सा। सन्धि जाँची: श्वासवत् + साधनम् → श्वासवत्साधनम् (स से पहले "
           "त् अपरिवर्तित)।"),
    "64": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। क्लोम (क्लोमन्) की पहचान विवादित: अग्न्याशय, दायाँ फेफड़ा, श्वासनली या कण्ठ; इसलिए "
           "‘क्लोम’ ही रखा; इस पर कोई प्रश्न नहीं। ‘स्रोतस’ छपा नहीं। सन्धि जाँची: उदकवाहिनाम् + तालु → उदकवाहिनां तालु; मूलम् + क्लोम "
           "→ मूलं क्लोम; ‘क्लोमच’ = क्लोम च, छपाई में जुड़ा।"),
}


# ===================================================================== AIDS
AIDS = {
    "52": {
        "diagram": {"groups": [
            {"label": "इकाई ५२ के शब्द (शब्द: अर्थ)", "items": ["अधोगमाः: नीचे जाने वाली",
                                                          "पक्वाशयस्थाः: पक्वाशय में स्थित (सम्भवतः बड़ी आँत का क्षेत्र)",
                                                          "एवम्: इसी प्रकार", "त्रिधा जायन्ते: तीन प्रकार की हो जाती हैं"]}]},
        "chunks": "अधोगमाः | पक्वाशयस्था | एवं | त्रिधा | जायंते",
        "sandhi": "अः + घोष व्यंजन → ओ: अधः + गमाः → अधोगमाः · आः स्वर से पहले विसर्ग खोता है: पक्वाशयस्थाः + एवम् → पक्वाशयस्था एवम्।",
        "frame": "कौन: अधोगमाः (नीचे जाने वाली) → कहाँ: पक्वाशयस्थाः → क्या होता है: एवं त्रिधा जायन्ते (इसी प्रकार तीन प्रकार की)।",
    },
    "53": {
        "chunks": "तत्र | दशाद्याः | पूर्ववत्",
        "sandhi": "अ + आ → आ: दश + आद्याः → दशाद्याः।",
        "frame": "कहाँ: तत्र (वहाँ) → कौन: दशाद्याः (पहली दस, या ‘दस आदि’) → कैसे: पूर्ववत् (पहले के समान); किसकी, यह छपा नहीं।",
    },
    "54": {
        "diagram": {"groups": [
            {"label": "पाँच जोड़े, छपे क्रम से (कितनी: क्या)", "items": ["१ दो: अन्न वहन (आँतों के आश्रय से)", "२ दो: तोय (जल)",
                                                                  "३ दो: मूत्र", "४ दो: शुक्र (वीर्य) वहन",
                                                                  "५ दो: छोड़ती हैं (क्या, छपा नहीं)"]}]},
        "chunks": "द्वे वहतोऽन्नमंत्राश्रयेण | द्वे तोयं | द्वे मूत्रं | द्वे शुक्रंवहतो | द्वे च मुंचतः",
        "sandhi": "अः + अ → ओऽ: वहतः + अन्नम् → वहतोऽन्नम् · अ + आ → आ: अन्त्र + आश्रयेण → अन्त्राश्रयेण · अः + घोष व्यंजन → ओ: वहतः + द्वे → वहतो द्वे।",
        "letters": "क्रम के पहले अक्षर: अ-तो-मू-शु-मु (अन्न, तोय, मूत्र, शुक्र, मुञ्चतः)। (मेरी याद-पद्धति)",
    },
    "55": {
        "chunks": "ते एव | नारीणामार्तवं",
        "sandhi": "द्विवचन का -ए स्वर से पहले सन्धि नहीं करता: ते + एव → ते एव · स्वर से पहले म्: नारीणाम् + आर्तवम् → नारीणामार्तवम्।",
        "frame": "कौन: ते एव (वे ही दोनों) → किनका: नारीणाम् (स्त्रियों का) → क्या: आर्तवम् (रजोरक्त); क्रिया ‘वहन’ इकाई ५४ से।",
    },
    "56": {
        "diagram": {"groups": [
            {"label": "दो (द्वे)", "items": ["मल निकालने वाली (अनुमानित पाठ)", "स्थूल आँत से बँधी"]},
            {"label": "शेष आठ", "items": ["तिरछी जाने वाली", "स्वेद को तृप्त करती हैं"]}]},
        "chunks": "द्वे | वज्र्रोनिरसन्यौ | स्थूलांत्रप्रतिबद्धे || शेषास्त्वष्टौ | तिरश्चीनाः | स्वेदमभितर्पयंति",
        "sandhi": "त से पहले विसर्ग → स्: शेषाः + तु → शेषास्तु · उ + भिन्न स्वर → व्: तु + अष्टौ → त्वष्टौ।",
        "frame": "भाग १: दो, स्थूल आँत से बँधी (मल निकालने वाली, अनुमानित) → भाग २: तु (पर) शेष आठ, तिरछी, स्वेद को तृप्त करती हैं।",
    },
    "57": {
        "chunks": "तिर्यग्गामिन्यश्चतस्रो | भिद्यमानाः | सुबहुधा | भवतीत्युक्तं | प्राक्",
        "sandhi": ("घोष व्यंजन से पहले क् → ग्: तिर्यक् + गामिन्यः → तिर्यग्गामिन्यः · च से पहले विसर्ग → श्: गामिन्यः + चतस्रः → "
                   "गामिन्यश्चतस्रः · अः + घोष व्यंजन → ओ: चतस्रः + भिद्यमानाः → चतस्रो भिद्यमानाः।"),
        "frame": "कौन: तिर्यग्गामिन्यः चतस्रः (तिरछी चार) → कैसे: भिद्यमानाः (बँटती हुई) → क्या: सुबहुधा (बहुत प्रकार की) → इत्युक्तं प्राक् (यह पहले कहा)।",
    },
    "58": {
        "diagram": {"groups": [
            {"label": "पुरुषों के नौ", "items": ["दो कान", "दो नेत्र", "दो नासापुट", "मुख", "पायु (गुदा)", "मूत्रमार्ग"]},
            {"label": "स्त्रियों के तीन अन्य", "items": ["दो स्तन", "रक्तपथ (सम्भावित: रजोरक्त का मार्ग)"]}]},
        "chunks": "स्रोतांसि पुंसांनव | कर्णौ नेत्रे नासापुटौ | मुखं पायुर्मूत्रपथो || ऽन्यानि च त्रीणि | स्त्रीणांस्तनौ रक्तपथश्च",
        "sandhi": ("उ के बाद विसर्ग, घोष व्यंजन से पहले र्: पायुः + मूत्र... → पायुर्मूत्र... · अः + अ → ओऽ: मूत्रपथः + अन्यानि → "
                   "मूत्रपथोऽन्यानि · च से पहले विसर्ग → श्: रक्तपथः + च → रक्तपथश्च।"),
        "pegs": "मेरा बनाया चित्र: सिर पर ऊपर से नीचे गिनें: कान २, आँख २, नाक २, मुँह १ (= ७), फिर नीचे के २ द्वार (= ९)। (केवल याद की सहायता)",
    },
    "59": {
        "diagram": {"groups": [
            {"label": "अन्य भीतरी स्रोतस: तेरह, जीवन के आयतन", "items": ["१ प्राण", "२ उदक (जल)", "३ अन्न", "४ धातु", "५ मल"]}]},
        "chunks": "तथाऽपराण्यंतःस्रोतांसि | जीवितायतनानि | त्रयोदश | प्राणोदकान्नधातुमलानामायतनानि",
        "sandhi": "अ + उ → ओ: प्राण + उदक → प्राणोदक · अ + अ → आ: उदक + अन्न → उदकान्न · इ + अ → य: अपराणि + अन्तः → अपराण्यन्तः।",
        "letters": "पाँचों के पहले अक्षर: प्रा-उ-अ-धा-म (प्राण, उदक, अन्न, धातु, मल)। (मेरी याद-पद्धति)",
    },
    "60": {
        "chunks": "तत्र | प्राणवाहिनां | हृदयंमूलं | महास्रोतश्च",
        "frame": "कौन: प्राणवाहिनाम् (प्राण वहन करने वाले स्रोतस का) → मूल: हृदयम् (हृदय) + महास्रोतः (बड़ा मार्ग, पहचान विवादित)।",
        "sandhi": "च से पहले विसर्ग → श्: महास्रोतः + च → महास्रोतश्च।",
    },
    "61": {
        "chain": {"steps": ["१ क्षय (क्षीणता)", "२ रौक्ष्य (रूखापन)", "३ पिपासा (प्यास)", "४ क्षुध् (भूख)", "५ व्यायाम",
                            "६ वेगधारण (वेग रोकना)", "आदि से: प्राणवह स्रोतस दूषित"]},
        "chunks": "तानि | क्षयरौक्ष्यपिपासाक्षुद्व्याया | मवेगधारणादिभिर्दुष्यंति",
        "sandhi": "इ के बाद विसर्ग, घोष व्यंजन से पहले र्: आदिभिः + दुष्यन्ति → आदिभिर्दुष्यन्ति।",
        "contrast": "पिपासा = प्यास, क्षुध् = भूख: दोनों इसी सूची में, साथ-साथ।",
    },
    "62": {
        "diagram": {"groups": [
            {"label": "ततः उच्छ्वसन (साँस), छपे क्रम से", "items": ["१ अतिसृष्ट: अधिक छूटती", "२ प्रतिबद्ध: रुकी हुई",
                                                                "३ कुपित: क्षुब्ध", "४ अल्पाल्प: थोड़ी-थोड़ी",
                                                                "५ अभीक्ष्ण: बार-बार", "६ सशब्दशूल: शब्द और पीड़ा सहित"]}]},
        "chunks": "ततोऽतिसृष्टं | प्रतिबद्धं | कुपितमल्पाल्पमभीक्ष्णं वा | सशब्दशूलमुच्छ्वसनं",
        "sandhi": "अः + अ → ओऽ: ततः + अतिसृष्टम् → ततोऽतिसृष्टम् · अ + अ → आ: अल्प + अल्प → अल्पाल्प।",
        "seesaw": "अतिसृष्ट (अधिक छूटती) ↔ प्रतिबद्ध (रुकी हुई): दोनों इसी पंक्ति में, एक-दूसरे के बाद।",
    },
    "63": {
        "chunks": "तत्र | श्वासवत्साधनं",
        "frame": "कहाँ: तत्र (इस स्थिति में) → क्या: साधनम् (उपचार) → कैसा: श्वासवत् (श्वास के समान; विवरण कहीं और)।",
        "anchors": "-वत् = ‘के समान’: पूर्ववत् (इकाई ५३), श्वासवत् (इकाई ६३)।",
    },
    "64": {
        "chunks": "उदकवाहिनां | तालु | मूलं | क्लोमच",
        "frame": "कौन: उदकवाहिनाम् (जल वहन करने वाले स्रोतस का) → मूल: तालु (मुँह की छत) + क्लोम (पहचान विवादित)।",
        "anchors": "इकाई ६० का ढाँचा दोहराया: [क्या]-वाहिनाम् + [अंग] मूलम्। प्राण → हृदय; उदक → तालु। (मेरी याद-पद्धति)",
    },
}


# ===================================================================== IMAGE_SPECS
IMAGE_SPECS = {
    ("52", "diagram"): {
        "file": "sh6-adhogama-52.svg",
        "alt": ("Table of the words of unit 52: adhogamāḥ, downward-going; pakvāśayasthāḥ, situated in the pakvāśaya "
                "(probably the large-intestine region); evam, likewise; tridhā jāyante, come to be threefold."),
        "type": "table",
        "title": "इकाई ५२: नीचे जाने वाली",
        "heads": ["शब्द", "अर्थ"],
        "rows": [["अधोगमाः", "नीचे जाने वाली"], ["पक्वाशयस्थाः", "पक्वाशय में स्थित (सम्भवतः बड़ी आँत का क्षेत्र)"],
                 ["एवम्", "इसी प्रकार"], ["त्रिधा जायन्ते", "तीन प्रकार की हो जाती हैं"]],
    },
    ("54", "diagram"): {
        "file": "sh6-pancha-yugma-54.svg",
        "alt": ("Table of the five pairs of unit 54 in printed order: two carry food (resting on the intestines); two, "
                "water; two, urine; two carry semen (śukra); two release (what is not stated)."),
        "type": "table",
        "title": "इकाई ५४: दो-दो के पाँच जोड़े",
        "heads": ["कितनी", "क्या"],
        "rows": [["१ दो", "अन्न वहन (आँतों के आश्रय से)"], ["२ दो", "तोय (जल)"], ["३ दो", "मूत्र"],
                 ["४ दो", "शुक्र (वीर्य) वहन"], ["५ दो", "छोड़ती हैं (क्या, छपा नहीं)"]],
    },
    ("56", "diagram"): {
        "file": "sh6-sthulantra-sveda-56.svg",
        "alt": ("Two columns of unit 56. Two: expelling stool (conjectural reading), bound to the large intestine. The "
                "remaining eight: running crosswise, satiating the sweat."),
        "type": "split",
        "title": "इकाई ५६: दो और शेष आठ",
        "cols": [["दो (द्वे)", ["मल निकालने वाली (अनुमानित पाठ)", "स्थूल आँत से बँधी"]],
                 ["शेष आठ", ["तिरछी जाने वाली", "स्वेद को तृप्त करती हैं"]]],
    },
    ("58", "diagram"): {
        "file": "sh6-nava-srotamsi-58.svg",
        "alt": ("Two columns of unit 58. Men's nine srotas: two ears, two eyes, two nostrils, mouth, anus, urinary "
                "passage. Women's three others: two breasts, blood-passage (probably of the menstrual blood)."),
        "type": "split",
        "title": "इकाई ५८: बाहरी स्रोतस",
        "cols": [["पुरुषों के नौ", ["दो कान", "दो नेत्र", "दो नासापुट", "मुख", "पायु (गुदा)", "मूत्रमार्ग"]],
                 ["स्त्रियों के तीन अन्य", ["दो स्तन", "रक्तपथ (सम्भावित: रजोरक्त का मार्ग)"]]],
    },
    ("59", "diagram"): {
        "file": "sh6-antah-srotamsi-59.svg",
        "alt": ("Flowchart of unit 59: the other inner srotas, thirteen, are seats of life, and seats of five, numbered "
                "in printed order: 1 prāṇa, 2 water, 3 food, 4 dhātu, 5 mala."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"अन्य भीतरी<br/>स्रोतस: तेरह\"] --> B[\"जीवन के आयतन\"]\n"
                 "  A --> C[\"इनके आयतन\"]\n"
                 "  C --> P1[\"१ प्राण\"]\n"
                 "  C --> P2[\"२ उदक (जल)\"]\n"
                 "  P1 ~~~ P3[\"३ अन्न\"] ~~~ P5[\"५ मल\"]\n"
                 "  P2 ~~~ P4[\"४ धातु\"]\n"
                 "  C --> P3\n"
                 "  C --> P4\n"
                 "  C --> P5\n"),
    },
    ("61", "chain"): {
        "file": "sh6-pranavaha-dushti-61.svg",
        "alt": ("Flowchart of unit 61: six causes numbered in printed order, wasting, dryness, thirst, hunger, exertion, "
                "holding back of urges, and the like, lead to the vitiation of the prāṇa-carrying srotas."),
        "type": "mermaid",
        "code": ('flowchart LR\n'
                 '  C1["१ क्षय (क्षीणता)"] --> D["प्राणवह स्रोतस दूषित"]\n'
                 '  C2["२ रौक्ष्य (रूखापन)"] --> D\n'
                 '  C3["३ पिपासा (प्यास)"] --> D\n'
                 '  C4["४ क्षुध् (भूख)"] --> D\n'
                 '  C5["५ व्यायाम"] --> D\n'
                 '  C6["६ वेगधारण (वेग रोकना)"] --> D\n'
                 '  C7["आदि (इत्यादि)"] --> D\n'),
    },
    ("62", "diagram"): {
        "file": "sh6-ucchvasana-62.svg",
        "alt": ("Table of unit 62: then the breathing is, in printed order, 1 excessively released, 2 obstructed, "
                "3 agitated, 4 scanty, 5 frequent, 6 with sound and pain."),
        "type": "table",
        "title": "इकाई ६२: ततः उच्छ्वसन (साँस)",
        "heads": ["शब्द", "अर्थ"],
        "rows": [["१ अतिसृष्ट", "अधिक छूटती"], ["२ प्रतिबद्ध", "रुकी हुई"], ["३ कुपित", "क्षुब्ध"],
                 ["४ अल्पाल्प", "थोड़ी-थोड़ी"], ["५ अभीक्ष्ण", "बार-बार"], ["६ सशब्दशूल", "शब्द और पीड़ा सहित"]],
    },
}
