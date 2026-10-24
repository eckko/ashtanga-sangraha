from helpers import mcq, match, order, fill, multi, accepts


def T(q, teaches):
    q["teaches"] = teaches
    return q


AUTHORED = {}

# ---------------------------------------------------------------- unit 39
AUTHORED["39"] = {
    "title": "पंचमे मनः प्रबुद्धतरं भवति",
    "question": "By unit 39, what happens in the fifth (month)?",
    "rule": ("In the fifth (month), the mind (मनस्) becomes more awakened (प्रबुद्धतर) and flesh and blood "
             "increase (मांसशोणितोपचय). -तर is the comparative: more."),
    "limits": ("The word month is not printed after पंचमे; it is understood from the sequence. The line does not say "
               "how or why the mind becomes more awakened. A prose line, not a verse."),
    "explain_hi": ("यह गद्य-पंक्ति पाँचवें (मास) का वर्णन करती है: मन अधिक जागृत (प्रबुद्धतर) हो जाता है और मांस तथा "
                   "रक्त (शोणित) की वृद्धि (उपचय) होती है। "
                   "‘मास’ शब्द छपा नहीं है, क्रम से समझा जाता है। "
                   "‘प्रबुद्धतरम्’ में ‘-तर’ तुलनावाचक प्रत्यय है: प्रबुद्ध = जागा हुआ, प्रबुद्धतर = अधिक जागा हुआ। "
                   "‘भवति’ दूसरे वाक्यांश में भी समझा जाता है (‘होती है’)। "
                   "‘शोणितोपचय’ में शोणित + उपचय है (अ + उ → ओ)।"),
    "hook": "पाँचवें में: मन अधिक जागृत, मांस-रक्त बढ़ता।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 39, what becomes more awakened in the fifth (month)?",
            ("The mind (मनः)", "मनः प्रबुद्धतरं भवति: the mind becomes more awakened."),
            [("The strength (बल)", "Increase of strength is named in unit 40, not here."),
             ("The hair (केश)", "Hair becomes manifest in unit 40, the sixth."),
             ("The limbs (अङ्ग)", "Completeness of the limbs is unit 41, the seventh.")],
            "In the fifth, the mind becomes more awakened.",
            "पञ्चमे मनः प्रबुद्धतरं भवति."),
        order(1, "Put the words of unit 39 in the line's order.",
              ["पञ्चमे", "मनः", "प्रबुद्धतरम्", "भवति", "मांसशोणितोपचयः", "च"],
              "In the fifth, the mind, more awakened, becomes; and increase of flesh and blood.",
              "पञ्चमे → मनः → प्रबुद्धतरम् → भवति → मांसशोणितोपचयः → च."),
        match(2, "Match each word of unit 39 to its meaning.",
              [["मनः", "mind"], ["प्रबुद्धतरम्", "more awakened"], ["मांस", "flesh"],
               ["शोणित", "blood"], ["उपचय", "increase"]],
              "Five words carry the two statements of the fifth (month).",
              "मनः, प्रबुद्धतरम्, मांस, शोणित, उपचय.", role="extend",
              teaches="-तर is the comparative: प्रबुद्ध (awakened) → प्रबुद्धतर (more awakened)."),
        mcq("discriminate", 3, "Which split of शोणितोपचय is right?",
            ("शोणित + उपचय", "अ + उ → ओ: शोणित + उपचय = शोणितोपचय."),
            [("शोणितः + उपचय", "A compound member has no visarga, and अः before उ would not give ओ."),
             ("शोणितो + पचय", "पचय is not the word of the card; the word is उपचय (increase)."),
             ("शोणित + ओपचय", "अ + ओ would give औ, not ओ; and ओपचय is not a word.")],
            "शोणित (blood) + उपचय (increase): अ + उ → ओ.",
            "अ + उ → ओ."),
        mcq("apply", 4, "What does the ending -तर add in प्रबुद्धतरम्?",
            ("More: more awakened (comparative)", "-तर makes the comparative degree."),
            [("Most: the most awakened (superlative)", "The superlative ending is -तम, not -तर."),
             ("Not: not awakened (negation)", "Negation would be a prefix अ-, not the ending -तर."),
             ("Again: awakened once again", "-तर does not mean again; that would be पुनः.")],
            "प्रबुद्ध + तर = more awakened.",
            "-तर = comparative, more."),
        mcq("transfer", 5, "By the rule of शोणितोपचय, how is सूर्य + उदयः (sunrise) written when joined?",
            ("सूर्योदयः", "अ + उ → ओ, as in शोणित + उपचय."),
            [("सूर्यौदयः", "अ + उ does not give औ."),
             ("सूर्युदयः", "The अ is not simply dropped before उ."),
             ("सूर्येदयः", "अ + उ does not give ए; ए comes from अ + इ.")],
            "सूर्य + उदयः = सूर्योदयः, like शोणित + उपचय = शोणितोपचय.",
            "अ + उ → ओ.",
            teaches="A short अ followed by उ joins as ओ: शोणित + उपचय → शोणितोपचय."),
    ],
}

# ---------------------------------------------------------------- unit 40
AUTHORED["40"] = {
    "title": "षष्ठे केशरोमनखास्थिस्नायवादीन्यभिव्यक्तानि",
    "question": "By unit 40, what becomes manifest and what increases in the sixth (month)?",
    "rule": ("In the sixth (month), hair, body-hair, nails, bones (अस्थि), sinews (स्नायु) and so on become manifest "
             "(अभिव्यक्त), and strength and complexion (बल, वर्ण) increase."),
    "limits": ("स्नायु = sinew, probably tendon or ligament (probable; the word covers several fibrous structures). "
               "-आदि (and so on) leaves the list open. वर्ण here is complexion, the colour of the skin. The month is "
               "understood, not printed."),
    "explain_hi": ("छठे (मास) में केश, रोम (शरीर के बाल), नख, अस्थि, स्नायु आदि प्रकट (अभिव्यक्त) हो जाते हैं, और बल "
                   "तथा वर्ण (त्वचा का रंग) की वृद्धि होती है। "
                   "स्नायु का अर्थ डेटा ‘सम्भवतः कण्डरा या स्नायुबन्ध’ देता है (सम्भावित पहचान)। "
                   "‘आदि’ से सूची खुली रहती है, यानी ये ही सब नहीं। "
                   "‘आदीन्यभिव्यक्तानि’ में आदीनि + अभिव्यक्तानि है (इ + अ → य)।"),
    "hook": "छठे में: केश-रोम-नख-अस्थि-स्नायु प्रकट, बल-वर्ण बढ़ते।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 40, what becomes manifest in the sixth (month)?",
            ("Hair, body-hair, nails, bones, sinews and so on", "केशरोमनखास्थिस्नायवादीन्यभिव्यक्तानि."),
            [("The mind, becoming more awakened than before", "That is unit 39, the fifth."),
             ("The completeness of all the limbs, every one of them", "That is unit 41, the seventh."),
             ("An exchange of ojas between mother and embryo", "That is unit 42, the eighth.")],
            "In the sixth, hair, body-hair, nails, bones, sinews and so on become manifest.",
            "षष्ठे केश... अभिव्यक्तानि."),
        order(1, "Put the parts listed in unit 40 in the line's order.",
              ["केश", "रोम", "नख", "अस्थि", "स्नायु"],
              "Hair, body-hair, nails, bones, sinews, then आदि (and so on).",
              "केश → रोम → नख → अस्थि → स्नायु."),
        match(2, "Match each part named in unit 40 to its meaning.",
              [["केश", "hair"], ["रोम", "body-hair"], ["नख", "nails"], ["अस्थि", "bones"],
               ["स्नायु", "sinews (probably tendons or ligaments)"]],
              "Five parts are named, then -आदि (and so on).",
              "केश, रोम, नख, अस्थि, स्नायु.", role="extend",
              teaches="-आदि = and so on: the list of manifest parts is left open."),
        mcq("discriminate", 3, "Which split of आदीन्यभिव्यक्तानि is right?",
            ("आदीनि + अभिव्यक्तानि", "इ + अ → य: आदीनि + अभिव्यक्तानि."),
            [("आदीन् + अभिव्यक्तानि", "A final न् would give आदीनभिव्यक्तानि, with no य."),
             ("आदी + न्यभिव्यक्तानि", "न्यभिव्यक्तानि is not a word."),
             ("आदीनि + भिव्यक्तानि", "भिव्यक्तानि is not a word; the word is अभिव्यक्तानि (manifest).")],
            "आदीनि (and so on) + अभिव्यक्तानि (manifest): इ + अ → य.",
            "इ + a different vowel → य् + that vowel."),
        mcq("apply", 4, "In unit 40, what increases (उपचय) in the sixth (month)?",
            ("Strength and complexion (बल, वर्ण)", "बलवर्णोपचयश्च: increase of strength and complexion."),
            [("Flesh and blood (मांस, शोणित)", "Flesh and blood increase in unit 39, the fifth."),
             ("Mind and senses (मनस्, इन्द्रिय)", "No mind or senses are named in unit 40."),
             ("Ojas and rasa (ओजस्, रस)", "Ojas and rasa are named in unit 42, not here.")],
            "बल (strength) and वर्ण (complexion) increase.",
            "बलवर्णोपचयः = increase of strength and complexion."),
        mcq("transfer", 5, "By the rule of आदीन्यभिव्यक्तानि, how is इति + अर्थः (this is the meaning) written when joined?",
            ("इत्यर्थः", "इ + अ → य, as आदीनि + अभिव्यक्तानि."),
            [("इतेर्थः", "इ + अ does not give ए."),
             ("इतार्थः", "The इ is not dropped before अ."),
             ("इतीर्थः", "इ + अ does not give ई.")],
            "इति + अर्थः = इत्यर्थः, like आदीनि + अभिव्यक्तानि.",
            "इ + a different vowel → य्.",
            teaches="A final इ before a different vowel becomes य्: आदीनि + अभिव्यक्तानि → आदीन्यभिव्यक्तानि."),
    ],
}

# ---------------------------------------------------------------- unit 41
AUTHORED["41"] = {
    "title": "सप्तमे सर्वांगसंपूर्णता",
    "question": "By unit 41, what is reached in the seventh (month)?",
    "rule": ("In the seventh (month), completeness of all the limbs (सर्वाङ्गसंपूर्णता). सर्व + अङ्ग → सर्वाङ्ग; "
             "-ता makes an abstract noun: complete → completeness."),
    "limits": ("A nominal line with no verb; none is supplied. The month is understood from the sequence. The line "
               "does not list which limbs."),
    "explain_hi": ("सातवें (मास) में सब अंगों की पूर्णता होती है: ‘सप्तमे सर्वाङ्गसंपूर्णता’। "
                   "पंक्ति में कोई क्रिया नहीं है; ‘मास’ भी क्रम से समझा जाता है। "
                   "‘सर्वाङ्ग’ में सर्व + अङ्ग है (अ + अ → आ)। "
                   "‘संपूर्णता’ में ‘-ता’ भाववाचक प्रत्यय है: संपूर्ण = पूरा, संपूर्णता = पूर्णता। "
                   "कौन-कौन से अंग, यह नहीं गिनाया गया।"),
    "hook": "सातवें में सब अंग पूरे।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 41, what comes in the seventh (month)?",
            ("Completeness of all the limbs", "सप्तमे सर्वाङ्गसंपूर्णता."),
            [("Hair and nails becoming manifest", "That is unit 40, the sixth."),
             ("The mind becoming more awakened", "That is unit 39, the fifth."),
             ("Ojas taken from the mother", "That is unit 42, the eighth.")],
            "The seventh brings completeness of all the limbs.",
            "सप्तमे सर्वाङ्गसंपूर्णता."),
        match(1, "Match each word of unit 41 to its meaning.",
              [["सप्तमे", "in the seventh"], ["सर्व", "all"], ["अङ्ग", "limb"], ["संपूर्णता", "completeness"]],
              "Four members make the whole line.",
              "सप्तमे, सर्व, अङ्ग, संपूर्णता."),
        T(fill(2, "In unit 41, the word for limb is ____ (type it in Devanagari or in English letters, e.g. dharma).",
               accepts("अङ्ग"),
               "सर्वाङ्ग = सर्व (all) + अङ्ग (limb); printed सर्वांग.",
               "अङ्ग = limb.",
               "अङ्ग = limb."),
          "अङ्ग = limb; अंग and अङ्ग are two spellings of one word."),
        mcq("discriminate", 3, "Which split of सर्वांग (सर्वाङ्ग) is right?",
            ("सर्व + अङ्ग", "अ + अ → आ: सर्व + अङ्ग = सर्वाङ्ग."),
            [("सर्वः + अङ्ग", "A visarga before अ would give सर्वोऽङ्ग."),
             ("सर्वम् + अङ्ग", "A final म् would give सर्वमङ्ग."),
             ("सर्वे + अङ्ग", "ए before अ would give सर्वेऽङ्ग.")],
            "सर्व (all) + अङ्ग (limb): अ + अ → आ.",
            "अ + अ → आ."),
        mcq("apply", 4, "What does the ending -ता add in संपूर्णता?",
            ("It makes an abstract noun: complete → completeness", "-ता forms abstract nouns."),
            [("It makes a comparative: complete → more complete", "The comparative ending is -तर."),
             ("It marks a place: complete → in the complete one", "-ता is not a locative ending."),
             ("It makes a past form: complete → was completed", "-ता here is not a verb ending.")],
            "संपूर्ण + ता = completeness.",
            "-ता = -ness (abstract noun)."),
        mcq("transfer", 5, "By the -ता of संपूर्णता, what does मधुरता mean, from मधुर (sweet)?",
            ("Sweetness", "-ता makes the abstract noun: मधुर → मधुरता."),
            [("Sweeter", "That would need the comparative -तर: मधुरतर."),
             ("The sweetest", "That would need the superlative -तम: मधुरतम."),
             ("Made sweet", "-ता does not make a participle.")],
            "मधुर + ता = sweetness, like संपूर्ण + ता = completeness.",
            "-ता = -ness.",
            teaches="-ता added to an adjective makes an abstract noun: संपूर्ण → संपूर्णता, मधुर → मधुरता."),
    ],
}

# ---------------------------------------------------------------- unit 42
AUTHORED["42"] = {
    "title": "अष्टमे गर्भश्च ... गर्भतश्च माता ... ओजः परस्परमाददाते",
    "question": "By unit 42, what do the embryo and the mother exchange in the eighth (month), and how?",
    "rule": ("In the eighth (month), the embryo (गर्भ) and the mother repeatedly take ojas (ओजस्, vital essence) from "
             "each other (परस्परम्) through the channels (वाहिनी) that carry rasa (nutrient fluid). आददाते is dual: two subjects."),
    "limits": ("Medium confidence. The printed मातृंतो may have a stray anusvara (मातृतो); no question rests on that "
               "spelling. Ojas is kept as vital essence, with no modern equivalent; rasa here is the nutrient fluid (rasa dhātu)."),
    "explain_hi": ("आठवें (मास) में गर्भ माता से और माता गर्भ से, रस (पोषक द्रव) ले जाने वाली वाहिनियों के द्वारा, बार-बार "
                   "एक-दूसरे से ओज (जीवन-सार) ग्रहण करते हैं। "
                   "क्रिया ‘आददाते’ द्विवचन है, क्योंकि कर्ता दो हैं: गर्भ और माता। "
                   "‘परस्परम्’ से यह लेन-देन दोनों ओर का है। "
                   "छपा ‘मातृंतो’ में सम्भवतः अनुस्वार अनावश्यक है (मातृतो); इस वर्तनी पर कोई प्रश्न नहीं। "
                   "ओज का कोई आधुनिक समानार्थी नहीं थोपा गया।"),
    "hook": "आठवें में माता-गर्भ बार-बार एक-दूसरे से ओज लेते।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 42, what do the embryo and the mother take from each other in the eighth (month)?",
            ("Ojas, the vital essence (ओजः)", "ओजः परस्परमाददाते."),
            [("Flesh and blood (मांस, शोणित)", "Flesh and blood increase in unit 39; they are not exchanged here."),
             ("Strength and complexion (बल, वर्ण)", "These increase in unit 40."),
             ("Breath, breathing (उच्छ्वसन)", "Breathing is named in unit 47, not here.")],
            "The two take ojas from each other.",
            "ओजः परस्परम् आददाते."),
        order(1, "Put these words of unit 42 in the line's order.",
              ["अष्टमे", "गर्भः", "माता", "वाहिनीभिः", "ओजः", "आददाते"],
              "In the eighth, the embryo ... the mother, by the channels, ojas, the two take.",
              "अष्टमे → गर्भः → माता → वाहिनीभिः → ओजः → आददाते."),
        match(2, "Match each word of unit 42 to its meaning.",
              [["रसहारिणी", "carrying rasa (nutrient fluid)"], ["वाहिनी", "channel"], ["मुहुर्मुहुः", "repeatedly"],
               ["ओजः", "ojas, the vital essence"], ["परस्परम्", "from each other"]],
              "These words say by what, how often, what and between whom.",
              "रसहारिणी, वाहिनी, मुहुर्मुहुः, ओजः, परस्परम्.", role="extend",
              teaches="परस्परम् = from each other: the exchange of ojas runs both ways."),
        mcq("discriminate", 3, "Why does the verb आददाते have a dual ending in unit 42?",
            ("Its two subjects are the embryo and the mother", "The note: the verb is dual, with subjects garbha and mātā."),
            [("It agrees with the many channels (वाहिनीभिः)", "वाहिनीभिः is instrumental plural: by the channels, not the subject."),
             ("It agrees with ojas, the thing taken (ओजः)", "ओजः is the object (accusative), not the subject."),
             ("It agrees with मुहुः, which is said twice", "मुहुः is an indeclinable, repeated for repeatedly.")],
            "Two subjects, गर्भः and माता, take a dual verb.",
            "Two subjects → dual verb (आददाते)."),
        multi("apply", 4, "Which statements does unit 42 make?",
              [("The exchange happens repeatedly", "Right: मुहुर्मुहुः, repeatedly."),
               ("Only the mother gives; the embryo only receives", "परस्परम्: each takes from the other."),
               ("The exchange runs through channels that carry rasa", "Right: रसहारिणीभिर्वाहिनीभिः."),
               ("The exchange begins in the fifth month", "The unit speaks of the eighth (अष्टमे).")],
              [0, 2],
              "Repeated, two-way, through the rasa-carrying channels, in the eighth.",
              "अष्टमे ... मुहुर्मुहुरोजः परस्परमाददाते."),
        mcq("transfer", 5, "By the rule of रसहारिणीभिर्वाहिनीभिः, how is अग्निः + दहति (fire burns) written when joined?",
            ("अग्निर्दहति", "A visarga after इ before a voiced consonant becomes र्."),
            [("अग्निदहति", "The visarga is not simply dropped after इ."),
             ("अग्निस्दहति", "स् stays only before त/थ, not before द."),
             ("अग्नीदहति", "The इ is not lengthened; the visarga becomes र्.")],
            "अग्निः + दहति = अग्निर्दहति, like रसहारिणीभिः + वाहिनीभिः.",
            "इः/ईः + voiced sound → इर्/ईर्.",
            teaches="A visarga after a vowel other than अ/आ becomes र् before a voiced sound: रसहारिणीभिः + वाहिनीभिः → रसहारिणीभिर्वाहिनीभिः."),
    ],
}

# ---------------------------------------------------------------- unit 43
AUTHORED["43"] = {
    "title": "गर्भिणी मुहुर्मुदिता भवति मुहुर्म्लाना",
    "question": "By unit 43, how is the pregnant woman at that time, and what is said of the embryo?",
    "rule": ("Therefore (तस्मात्) at that time (तदा) the pregnant woman is at one moment glad (मुदिता), at another "
             "languid (म्लाना); likewise (तथा) the embryo. मुहुः ... मुहुः = at one moment ... at another."),
    "limits": ("तदा (then) is not named in this unit; by the sequence it follows the eighth (month) of unit 42, but the "
               "line does not say so. For the embryo the verb is carried over (तथा गर्भः), not printed."),
    "explain_hi": ("इसलिए उस समय गर्भवती स्त्री कभी प्रसन्न (मुदिता) होती है और कभी म्लान, यानी मुरझाई हुई; और वैसे ही गर्भ भी। "
                   "‘मुहुः ... मुहुः’ का अर्थ है ‘कभी ... कभी’। "
                   "‘तथा गर्भः’ में क्रिया नहीं छपी, पहले वाक्य से समझी जाती है। "
                   "‘तस्मात्’ (इसलिए) पिछली बात से जोड़ता है; ‘तदा’ किस समय को कहता है, यह पंक्ति स्वयं नहीं बताती। "
                   "‘मुहुर्मुदिता’ में मुहुः + मुदिता है (उ के बाद विसर्ग → र् घोष से पहले)।"),
    "hook": "कभी मुदिता, कभी म्लाना: वैसे ही गर्भ भी।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 43, how is the pregnant woman at that time?",
            ("At times glad, at times languid", "मुहुर्मुदिता भवति मुहुर्म्लाना."),
            [("Always glad and at ease", "The line says glad only at times (मुहुः)."),
             ("Always weary and faded", "The line says languid only at times (मुहुः)."),
             ("Glad only in the morning", "No time of day is named.")],
            "She swings between glad and languid.",
            "मुहुः मुदिता ... मुहुः म्लाना."),
        order(1, "Put the parts of unit 43 in the line's order.",
              ["तस्मात् तदा", "गर्भिणी", "मुहुः मुदिता", "भवति", "मुहुः म्लाना", "तथा गर्भः"],
              "Therefore then the pregnant woman, at times glad, is, at times languid; likewise the embryo.",
              "तस्मात् तदा → गर्भिणी → मुहुः मुदिता → भवति → मुहुः म्लाना → तथा गर्भः."),
        match(2, "Match each word of unit 43 to its meaning.",
              [["गर्भिणी", "pregnant woman"], ["मुदिता", "glad"], ["म्लाना", "languid, faded"],
               ["मुहुः", "at times"], ["तथा", "likewise"]],
              "The two states, the two subjects and the linking words.",
              "गर्भिणी, मुदिता, म्लाना, मुहुः, तथा.", role="extend",
              teaches="मुहुः ... मुहुः = at one moment ... at another."),
        mcq("discriminate", 3, "Which split of मुहुर्मुदिता is right?",
            ("मुहुः + मुदिता", "Visarga after उ before the voiced म becomes र्."),
            [("मुहुम् + मुदिता", "A final म् would give मुहुं मुदिता, with no र्."),
             ("मुहु + र्मुदिता", "र्मुदिता is not a word."),
             ("मुहुः + उदिता", "Before a vowel this would give मुहुरुदिता, with no म.")],
            "मुहुः (at times) + मुदिता (glad).",
            "उः + voiced sound → उर्."),
        mcq("apply", 4, "By unit 43, what is said of the embryo?",
            ("Likewise it is at times glad, at times languid", "तथा गर्भः: likewise the embryo, the verb carried over."),
            [("It stays calm whatever the mother feels", "तथा (likewise) ties it to the mother's states."),
             ("It grows stronger while the mother fades", "No growth of the embryo is named here."),
             ("It is not mentioned in unit 43 at all", "The line ends तथा गर्भः.")],
            "तथा गर्भः: the embryo too has the same changing states.",
            "तथा गर्भः = likewise the embryo."),
        mcq("transfer", 5, "By the rule of मुहुर्मुदिता, how is धेनुः + गच्छति (the cow goes) written when joined?",
            ("धेनुर्गच्छति", "Visarga after उ before the voiced ग becomes र्."),
            [("धेनुगच्छति", "The visarga is not simply dropped after उ."),
             ("धेनुस्गच्छति", "स् stays only before त/थ."),
             ("धेनोर्गच्छति", "The vowel उ does not change to ओ.")],
            "धेनुः + गच्छति = धेनुर्गच्छति, like मुहुः + मुदिता.",
            "उः + voiced sound → उर्.",
            teaches="A visarga after उ becomes र् before a voiced sound: मुहुः + मुदिता → मुहुर्मुदिता."),
    ],
}

# ---------------------------------------------------------------- unit 44
AUTHORED["44"] = {
    "title": "एवं गर्भस्य जन्म व्यापत्तिमत्",
    "question": "By unit 44, what is the birth of the embryo then accompanied by?",
    "rule": ("Thus (एवम्) the birth (जन्म) of the embryo is then (तदा) accompanied by calamity: व्यापत्तिमत्, "
             "having calamity (व्यापत्ति + -मत्), agrees with the neuter जन्म."),
    "limits": ("The line does not name the time; the data's note takes तदा as the eighth (month) of unit 42. It does not "
               "say what the calamity is; the reason given in unit 45 is joined to it by the note only tentatively."),
    "explain_hi": ("इस प्रकार तब गर्भ का जन्म विपत्ति (व्यापत्ति) से युक्त होता है। "
                   "‘व्यापत्तिमत्’ में ‘-मत्’ प्रत्यय ‘वाला, युक्त’ का अर्थ देता है, और यह नपुंसक ‘जन्म’ का विशेषण है। "
                   "‘तदा’ किस समय को कहता है, पंक्ति नहीं बताती; डेटा की टिप्पणी इसे इकाई 42 का आठवाँ (मास) मानती है। "
                   "विपत्ति का स्वरूप यहाँ नहीं बताया गया।"),
    "hook": "तब का जन्म = विपत्ति-युक्त।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 44, what is the birth of the embryo then accompanied by?",
            ("Calamity", "जन्म व्यापत्तिमत् तदा भवति."),
            [("Strength and good colour", "Strength and complexion increase in unit 40; not here."),
             ("A long life", "No long life is named in unit 44."),
             ("Gladness of the mother", "Gladness is in unit 43, not tied to the birth.")],
            "The birth then is accompanied by calamity.",
            "जन्म व्यापत्तिमत्."),
        order(1, "Put the words of unit 44 in the line's order.",
              ["एवम्", "गर्भस्य", "जन्म", "व्यापत्तिमत्", "तदा", "भवति"],
              "Thus, of the embryo, the birth, accompanied by calamity, then, is.",
              "एवम् → गर्भस्य → जन्म → व्यापत्तिमत् → तदा → भवति."),
        T(fill(2, "Thus the birth of the embryo: एवं गर्भस्य ____ (type it in Devanagari or in English letters, e.g. dharma).",
               accepts("जन्म"),
               "The line opens एवं गर्भस्य जन्म.",
               "जन्म = birth.",
               "जन्म = birth."),
          "जन्म = birth, a neuter noun; व्यापत्तिमत् agrees with it."),
        mcq("discriminate", 3, "What does the suffix -मत् add in व्यापत्तिमत्?",
            ("Having: having calamity, accompanied by it", "-मत् is a possessive suffix (matup)."),
            [("Without: free of any calamity", "Being free of something is not the sense of -मत्."),
             ("Causing: bringing calamity to others", "-मत् means having, not causing."),
             ("More: a greater calamity than before", "The comparative would be -तर.")],
            "व्यापत्ति + मत् = having calamity.",
            "-मत् = having."),
        mcq("apply", 4, "In unit 44, which word does व्यापत्तिमत् agree with?",
            ("जन्म (birth), a neuter", "The note: a neuter agreeing with janma."),
            [("गर्भस्य (of the embryo)", "गर्भस्य is genitive masculine; व्यापत्तिमत् is neuter nominative."),
             ("एवम् (thus)", "एवम् is an indeclinable; nothing agrees with it."),
             ("तदा (then)", "तदा is an indeclinable of time.")],
            "व्यापत्तिमत् describes जन्म: the birth is accompanied by calamity.",
            "व्यापत्तिमत् (n.) ↔ जन्म (n.)."),
        mcq("transfer", 5, "By the -मत् of व्यापत्तिमत्, what does बुद्धिमत्, from बुद्धि (intelligence), mean?",
            ("Having intelligence", "-मत् = having, as व्यापत्तिमत् = having calamity."),
            [("Lacking intelligence", "Lacking would need a negative, not -मत्."),
             ("Giving intelligence", "-मत् means having, not giving."),
             ("Made of intelligence", "Made of would be -मय.")],
            "बुद्धि + मत् = having intelligence.",
            "-मत् = having.",
            teaches="The suffix -मत् means having: व्यापत्ति → व्यापत्तिमत्, बुद्धि → बुद्धिमत्."),
    ],
}

# ---------------------------------------------------------------- unit 45
AUTHORED["45"] = {
    "title": "ओजसोऽनवस्थितत्वात्",
    "question": "By unit 45, what cause is named, and how is the word built?",
    "rule": ("Because of the unsteadiness of ojas (ओजसः अनवस्थितत्वात्). अन् (not) + अवस्थित (steady) + -त्व (-ness) "
             "+ -आत् (because of)."),
    "limits": ("A single dependent phrase with no verb. That it gives the reason for unit 44 is the note's tentative "
               "reading (appears to), not printed. Ojas is kept as vital essence; how it is unsteady is not said."),
    "explain_hi": ("यह एक ही पद है: ‘ओज के अस्थिर होने के कारण’। "
                   "‘अनवस्थितत्वात्’ = अन् (नहीं) + अवस्थित (स्थिर, टिका हुआ) + त्व (भाव) + आत् (पञ्चमी, ‘के कारण’)। "
                   "डेटा की टिप्पणी के अनुसार यह सम्भवतः इकाई 44 की विपत्ति का कारण बताता है; यह जोड़ छपा नहीं, अनुमान है। "
                   "‘ओजसोऽनवस्थितत्वात्’ में ओजसः + अनवस्थितत्वात् है (अः + अ → ओऽ)।"),
    "hook": "ओज टिकता नहीं: अन्-अवस्थित-त्व-आत्।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 45, the unsteadiness of what is named?",
            ("Of ojas, the vital essence", "ओजसः अनवस्थितत्वात्."),
            [("Of the mind (मनस्)", "The mind is in unit 39, not here."),
             ("Of the limbs (अङ्ग)", "The limbs are in unit 41."),
             ("Of the channels (वाहिनी)", "The channels are in unit 42.")],
            "The unsteadiness of ojas.",
            "ओजसोऽनवस्थितत्वात्."),
        match(1, "Match each piece of अनवस्थितत्वात् to its meaning.",
              [["अन्-", "not"], ["अवस्थित", "steady, settled"], ["-त्व", "-ness (abstract noun)"],
               ["-आत्", "because of (ablative)"]],
              "Four pieces build because of unsteadiness.",
              "अन् + अवस्थित + त्व + आत्."),
        order(2, "Put the pieces of unit 45 in the order of the printed word.",
              ["ओजसः", "अन्", "अवस्थित", "त्व", "आत्"],
              "Of ojas, not, steady, -ness, because of.",
              "ओजसः → अन् → अवस्थित → त्व → आत्.", role="extend",
              teaches="Before a vowel the negative is अन्-: अन् + अवस्थित → अनवस्थित (not steady)."),
        mcq("discriminate", 3, "Which split of ओजसोऽनवस्थितत्वात् is right?",
            ("ओजसः + अनवस्थितत्वात्", "अः + अ → ओ, and ऽ marks the lost अ."),
            [("ओजसः + नवस्थितत्वात्", "ऽ shows a lost अ; नवस्थित is not the word."),
             ("ओजसम् + अनवस्थितत्वात्", "A final म् would give ओजसमनवस्थितत्वात्."),
             ("ओजसा + अनवस्थितत्वात्", "आ + अ → आ would give ओजसानवस्थितत्वात्.")],
            "ओजसः (of ojas) + अनवस्थितत्वात् (because of unsteadiness).",
            "अः + अ → ओऽ."),
        mcq("apply", 4, "What sense does the ending -त्वात् give in unit 45?",
            ("Because of being: because of unsteadiness", "-त्व (-ness) + ablative -आत् = because of."),
            [("Toward: going into unsteadiness", "Motion toward is not the sense of the ablative here."),
             ("Together with: along with unsteadiness", "That would be an instrumental sense."),
             ("Inside: in the state of unsteadiness", "That would be a locative, -त्वे.")],
            "The ablative of an abstract noun gives the cause.",
            "-त्वात् = because of being."),
        mcq("transfer", 5, "By the rule of ओजसोऽनवस्थितत्वात्, how is मनसः + अपि (even of the mind) written when joined?",
            ("मनसोऽपि", "अः + अ → ओ, with ऽ for the lost अ."),
            [("मनसापि", "That would come from मनसा + अपि."),
             ("मनसरपि", "र् comes from a visarga after other vowels; after अ, अः + अ gives ओऽ."),
             ("मनसेऽपि", "अः + अ does not give ए.")],
            "मनसः + अपि = मनसोऽपि, like ओजसः + अनवस्थितत्वात्.",
            "अः + अ → ओऽ.",
            teaches="A visarga after अ before a short अ: अः + अ → ओ + ऽ (ओजसोऽनवस्थितत्वात्)."),
    ],
}

# ---------------------------------------------------------------- unit 46
AUTHORED["46"] = {
    "title": "तथा ह्यस्य निष्क्रमणोन्मुखस्य",
    "question": "By the sure words of unit 46, what does the one on the point of coming out experience, and from what is it separated?",
    "rule": ("For thus (तथा हि), in this one on the point of coming out (निष्क्रमणोन्मुख), experiencing turning round "
             "(परिवर्तन) and the like, this is the separation (वियोग) from ojas (ओजसा)."),
    "limits": ("Low confidence; read only in outline. Loose syntax (genitive अस्य ... उन्मुखस्य, nominative अनुभवन्); "
               "printed एषौजसा taken as एषः + ओजसा. No question rests on these points or on who this one is."),
    "explain_hi": ("यह कठिन पंक्ति है और इसका अर्थ केवल मोटे तौर पर पक्का है: क्योंकि इस निकलने को उन्मुख (के), जो पलटना आदि "
                   "अनुभव करता है, यह ओज से वियोग है। "
                   "वाक्य-रचना ढीली है: ‘अस्य ... उन्मुखस्य’ षष्ठी है पर ‘अनुभवन्’ प्रथमा; अनुवाद छपे रूपों के अनुसार है। "
                   "‘ओजसा वियोगः’ में तृतीया ठीक है (वियोग के साथ तृतीया आती है)। "
                   "‘ह्यस्य’ = हि + अस्य (इ + अ → य); ‘निष्क्रमणोन्मुख’ = निष्क्रमण + उन्मुख (अ + उ → ओ)।"),
    "hook": "निकलने को उन्मुख, पलटता हुआ: ओज से वियोग।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 46, separation (वियोग) from what is spoken of?",
            ("From ojas (ओजसा)", "ओजसा वियोगः: separation from ojas."),
            [("From rasa, the nutrient fluid", "Rasa is not named in unit 46."),
             ("From the channels (वाहिनी)", "The channels are not named in unit 46."),
             ("From the mind (मनस्)", "The mind is not named in unit 46.")],
            "The unit speaks of separation from ojas.",
            "ओजसा वियोगः."),
        order(1, "Put these words of unit 46 in the line's order.",
              ["तथा ह्यस्य", "निष्क्रमणोन्मुखस्य", "परिवर्तनादीनि", "अनुभवन्", "एषौजसा", "वियोगः"],
              "For thus of this one, on the point of coming out, turning round and the like, experiencing, this by ojas, separation.",
              "तथा ह्यस्य → निष्क्रमणोन्मुखस्य → परिवर्तनादीनि → अनुभवन् → एषौजसा → वियोगः."),
        match(2, "Match each word of unit 46 to its meaning.",
              [["निष्क्रमण", "coming out"], ["उन्मुख", "directed toward, on the point of"],
               ["परिवर्तन", "turning round"], ["अनुभवन्", "experiencing"], ["वियोग", "separation"]],
              "These are the sure words of the unit.",
              "निष्क्रमण, उन्मुख, परिवर्तन, अनुभवन्, वियोग.", role="extend",
              teaches="निष्क्रमण-उन्मुख = turned toward coming out: on the point of coming out."),
        mcq("discriminate", 3, "Which split of ह्यस्य is right?",
            ("हि + अस्य", "इ + अ → य: हि + अस्य = ह्यस्य."),
            [("ह + अस्य", "अ + अ would give हास्य, with no य."),
             ("हि + यस्य", "No vowel meets here; हि यस्य would stay apart, with no joined य्."),
             ("हिः + अस्य", "हिः is not a word; the particle is हि.")],
            "हि (for, indeed) + अस्य (of this one).",
            "इ + अ → य."),
        multi("apply", 4, "Which statements does unit 46 make?",
              [("It gives the mother's weariness", "The mother's weariness is unit 48."),
               ("It names turning round and the like", "Right: परिवर्तनादीनि अनुभवन्."),
               ("It allows breathing for some time", "Breathing for some time is unit 47."),
               ("It speaks of one on the point of coming out", "Right: निष्क्रमणोन्मुखस्य.")],
              [1, 3],
              "One on the point of coming out, experiencing turning round and the like; separation from ojas.",
              "निष्क्रमणोन्मुख, परिवर्तनादीनि, ओजसा वियोगः."),
        mcq("transfer", 5, "By the rule of ह्यस्य, how is अति + अन्तम् (exceedingly) written when joined?",
            ("अत्यन्तम्", "इ + अ → य, as हि + अस्य → ह्यस्य."),
            [("अतेन्तम्", "इ + अ does not give ए."),
             ("अतीन्तम्", "इ + अ does not give ई."),
             ("अतान्तम्", "The इ is not dropped before अ.")],
            "अति + अन्तम् = अत्यन्तम्, like हि + अस्य.",
            "इ + a different vowel → य्.",
            teaches="A final इ before a different vowel becomes य्: हि + अस्य → ह्यस्य."),
    ],
}

# ---------------------------------------------------------------- unit 47
AUTHORED["47"] = {
    "title": "यद्यपि च किंचित्कालमस्योच्छ्वसनं स्यात्",
    "question": "By unit 47, if there is breathing for some time, what is it made by, and what image is used?",
    "rule": ("Even if (यद्यपि) there may be breathing (उच्छ्वसन) of this one for some time, that is made by the continuation "
             "of the lingering impression of ojas (ओजःसंस्कारानुवृत्ति), like (इव) a severed limb (छिन्न अङ्ग)."),
    "limits": ("Medium confidence. The comparison with a severed limb may go with the whole phrase or read as in a severed "
               "limb; no question rests on that. Who this one is is not named in the unit. It continues the argument of "
               "units 45 and 46."),
    "explain_hi": ("और यदि इसका कुछ समय तक साँस लेना (उच्छ्वसन) हो भी, तो वह कटे हुए अंग की तरह, ओज के संस्कार (छाप, बचा "
                   "हुआ वेग) के बने रहने से किया हुआ है। "
                   "यह पिछली इकाइयों के तर्क को आगे बढ़ाता है। "
                   "उपमा ‘कटे अंग की तरह’ पूरे वाक्यांश से जुड़ सकती है या ‘कटे अंग में जैसे’ भी पढ़ी जा सकती है; इस पर प्रश्न नहीं। "
                   "सन्धि: यदि + अपि → यद्यपि; तत् + छिन्नस्य → तच्छिन्नस्य; अङ्गस्य + ओजः → अङ्गस्यौजः।"),
    "hook": "कटे अंग-सी साँस: ओज के संस्कार की अनुवृत्ति।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 47, if there is breathing for some time, what is it made by?",
            ("The continuing lingering impression of ojas", "ओजःसंस्कारानुवृत्तिकृतम्."),
            [("The rasa-carrying channels of the mother", "The channels are unit 42, not the cause here."),
             ("The growing strength of the limbs", "No strength of limbs is named in unit 47."),
             ("The turning round of the one coming out", "Turning round is unit 46, not the cause here.")],
            "The breathing is made by the continuation of the saṃskāra of ojas.",
            "ओजःसंस्कारानुवृत्तिकृतम्."),
        order(1, "Put these parts of unit 47 in the line's order.",
              ["यद्यपि च", "किंचित्कालम्", "उच्छ्वसनम्", "स्यात्", "छिन्नस्य इव अङ्गस्य", "ओजःसंस्कारानुवृत्तिकृतम्"],
              "Even if, for some time, breathing there may be, like a severed limb's, made by the continuation of the ojas impression.",
              "यद्यपि च → किंचित्कालम् → उच्छ्वसनम् → स्यात् → छिन्नस्य इव अङ्गस्य → ओजःसंस्कारानुवृत्तिकृतम्."),
        match(2, "Match each word of unit 47 to its meaning.",
              [["किंचित्कालम्", "for some time"], ["उच्छ्वसन", "breathing"], ["छिन्न", "severed, cut off"],
               ["संस्कार", "lingering impression"], ["अनुवृत्ति", "continuation"]],
              "These words say how long, what, the image and the cause.",
              "किंचित्कालम्, उच्छ्वसन, छिन्न, संस्कार, अनुवृत्ति.", role="extend",
              teaches="-कृत at the end of a compound = made by: ओजःसंस्कारानुवृत्तिकृत = made by the continuation of the ojas impression."),
        mcq("discriminate", 3, "Which split of तच्छिन्नस्य is right?",
            ("तत् + छिन्नस्य", "त् before छ becomes च्, written च्छ."),
            [("तम् + छिन्नस्य", "A final म् would give तं छिन्नस्य."),
             ("तच्छि + न्नस्य", "Neither piece is a word."),
             ("तत् + चिन्नस्य", "त् + च gives च्च; चिन्नस्य is not a word.")],
            "तत् (that) + छिन्नस्य (of one severed).",
            "त् + छ → च्छ."),
        mcq("apply", 4, "What image does unit 47 use for this breathing?",
            ("A severed limb", "छिन्नस्येवाङ्गस्य: like a severed limb."),
            [("A lamp after its oil is gone", "No lamp is named in unit 47."),
             ("A wheel that keeps on turning", "No wheel is named in unit 47."),
             ("A tree cut down at the root", "No tree is named in unit 47.")],
            "The image is a severed limb.",
            "छिन्नस्य इव अङ्गस्य."),
        mcq("transfer", 5, "By the rule of अङ्गस्यौजः, how is जल + ओघः (a flood of water) written when joined?",
            ("जलौघः", "अ + ओ → औ, as अङ्गस्य + ओजः → अङ्गस्यौजः."),
            [("जलोघः", "अ + ओ gives औ, not ओ."),
             ("जलेघः", "अ + ओ does not give ए."),
             ("जलवोघः", "No व् comes between अ and ओ.")],
            "जल + ओघः = जलौघः, like अङ्गस्य + ओजः.",
            "अ + ओ → औ.",
            teaches="A short अ before ओ joins as औ: अङ्गस्य + ओजः → अङ्गस्यौजः."),
    ],
}

# ---------------------------------------------------------------- unit 48
AUTHORED["48"] = {
    "title": "जनन्यास्तु स्थिरौजस्कतया",
    "question": "By unit 48, what does the mother suffer, and why only that?",
    "rule": ("But in the mother (जनन्याः तु), because her ojas is stable (स्थिरौजस्कतया), when rasa has passed over in "
             "one part (एकदेशेन रसे संक्रान्ते), there is only weariness (ग्लानिः एव)."),
    "limits": ("Medium confidence. The copula there is is understood. The closing इति ends the view stated in units 46 to 48; "
               "the line does not say whose view it is. Rasa is the nutrient fluid; weariness is not explained further."),
    "explain_hi": ("परन्तु माता में ओज स्थिर होने के कारण, जब रस एक अंश में संक्रान्त हो जाता है, तो केवल ग्लानि (थकान) ही होती है। "
                   "‘रसे संक्रान्ते’ सति-सप्तमी है: ‘रस के संक्रान्त हो जाने पर’। "
                   "‘एकदेशेन’ = एक भाग से, आंशिक रूप से। "
                   "अन्त का ‘इति’ इस मत को समाप्त करता है। "
                   "सन्धि: जनन्याः + तु → जनन्यास्तु; स्थिर + ओजस्कतया → स्थिरौजस्कतया; ग्लानिः + एव + इति → ग्लानिरेवेति।"),
    "hook": "माता का ओज स्थिर: उसे केवल ग्लानि।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 48, what does the mother have when rasa has passed over in one part?",
            ("Only weariness (ग्लानि)", "ग्लानिरेव: only weariness."),
            [("Death (मरण)", "Death is named for the embryo in unit 50, not for the mother here."),
             ("Lasting gladness", "Gladness is in unit 43; here it is weariness."),
             ("A loss of all ojas", "Her ojas is called stable (स्थिर).")],
            "For the mother, only weariness.",
            "जनन्याः ... ग्लानिरेव."),
        order(1, "Put the parts of unit 48 in the line's order.",
              ["जनन्याः तु", "स्थिरौजस्कतया", "एकदेशेन", "रसे संक्रान्ते", "ग्लानिः एव", "इति"],
              "But of the mother, because of stable ojas, in one part, when rasa has passed over, only weariness; thus.",
              "जनन्याः तु → स्थिरौजस्कतया → एकदेशेन → रसे संक्रान्ते → ग्लानिः एव → इति."),
        match(2, "Match each word of unit 48 to its meaning.",
              [["जननी", "mother"], ["स्थिर", "stable"], ["एकदेश", "one part"],
               ["संक्रान्त", "passed over"], ["ग्लानि", "weariness"]],
              "Who, why, how much, what happened, and the result.",
              "जननी, स्थिर, एकदेश, संक्रान्त, ग्लानि.", role="extend",
              teaches="रसे संक्रान्ते is a locative absolute: when rasa has passed over."),
        mcq("discriminate", 3, "Which split of जनन्यास्तु is right?",
            ("जनन्याः + तु", "Visarga before त becomes स्."),
            [("जनन्याम् + तु", "A final म् would give जनन्यां तु."),
             ("जनन्या + स्तु", "स्तु is not a word; the particle is तु."),
             ("जनन्यात् + तु", "A final त् would give जनन्यात्तु.")],
            "जनन्याः (of the mother) + तु (but).",
            "Visarga + त → स्त."),
        mcq("apply", 4, "By unit 48, why is it only weariness for the mother?",
            ("Because her ojas is stable", "स्थिरौजस्कतया: because of the stability of ojas."),
            [("Because she has no ojas at all", "Her ojas is called stable, not absent."),
             ("Because her channels are closed", "No closing of channels is named here."),
             ("Because the embryo returns the rasa", "No return of rasa is named here.")],
            "Stable ojas in the mother: only weariness.",
            "स्थिर-ओजस्कता → ग्लानिः एव."),
        mcq("transfer", 5, "By the rule of ग्लानिरेव, how is हरिः + अपि (even Hari) written when joined?",
            ("हरिरपि", "Visarga after इ before a vowel becomes र्."),
            [("हरोऽपि", "अः + अ → ओऽ needs अ before the visarga, not इ."),
             ("हर्यपि", "That is the rule for a final इ without visarga."),
             ("हरिपि", "The visarga is not simply dropped.")],
            "हरिः + अपि = हरिरपि, like ग्लानिः + एव = ग्लानिरेव.",
            "इः + vowel → इर्.",
            teaches="A visarga after इ becomes र् before a vowel: ग्लानिः + एव → ग्लानिरेव."),
    ],
}

# ---------------------------------------------------------------- unit 49
AUTHORED["49"] = {
    "title": "अन्ये पुनराहुः",
    "question": "What does the short formula of unit 49 introduce?",
    "rule": ("अन्ये पुनर् आहुः: others, however, say. It introduces another view, stated after it. आहुः is 3 pl. "
             "perfect of √अह्: they say."),
    "limits": ("Three printed words only (printed joined as अन्येपुनराहुः). The view itself is not stated in this unit, "
               "and the others are not named."),
    "explain_hi": ("यह छोटा सूत्र एक दूसरे मत की भूमिका है: ‘दूसरे लोग तो फिर कहते हैं’। "
                   "मत स्वयं इस इकाई में नहीं है, आगे आता है; ‘अन्ये’ कौन हैं, नाम नहीं दिया गया। "
                   "‘आहुः’ धातु अह् का परोक्ष (लिट्) प्रथम पुरुष बहुवचन है, अर्थ ‘कहते हैं’। "
                   "‘पुनराहुः’ में पुनर् + आहुः है (र् स्वर से पहले बना रहता है)।"),
    "hook": "अन्ये पुनराहुः = दूसरे तो कहते हैं।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "Who speaks, by unit 49?",
            ("Others", "अन्ये पुनराहुः: others, however, say."),
            [("Ātreya", "No name is given in unit 49."),
             ("The mother", "The mother is not the speaker here."),
             ("The physician", "No physician is named in unit 49.")],
            "Unnamed others give another view.",
            "अन्ये = others."),
        match(1, "Match each word of unit 49 to its meaning.",
              [["अन्ये", "others"], ["पुनर्", "however, again"], ["आहुः", "they say"]],
              "Three words make the whole formula.",
              "अन्ये, पुनर्, आहुः."),
        T(fill(2, "Others, however, say: अन्ये पुनर् ____ (type it in Devanagari or in English letters, e.g. dharma).",
               accepts("आहुः"),
               "The line is अन्ये पुनराहुः.",
               "आहुः = they say.",
               "आहुः = they say."),
          "आहुः = they say, the third person plural perfect of √अह्, used for a stated view."),
        mcq("discriminate", 3, "Which split of पुनराहुः is right?",
            ("पुनर् + आहुः", "र् stays before a vowel and joins it: पुनर् + आहुः."),
            [("पुन + आहुः", "अ + आ → आ would give पुनाहुः, with no र्."),
             ("पुनरा + हुः", "Neither piece is a word."),
             ("पुनम् + आहुः", "A final म् would give पुनमाहुः.")],
            "पुनर् (however) + आहुः (they say).",
            "पुनर् + vowel → पुनर्-."),
        mcq("apply", 4, "By the card, what form is आहुः?",
            ("Third person plural: they say", "Labelled 3 pl. pf. of √अह्."),
            [("Third person singular: he says", "The singular is आह."),
             ("First person plural: we say", "आहुः is not first person."),
             ("A command: say!", "आहुः is not a command form.")],
            "आहुः = they say: plural, because others speak.",
            "आहुः = 3 pl., they say."),
        mcq("transfer", 5, "By the rule of पुनराहुः, how is पुनर् + अपि (again too) written when joined?",
            ("पुनरपि", "र् stays and joins the vowel, as पुनर् + आहुः."),
            [("पुनोऽपि", "ओऽ comes from अः, not from पुनर्."),
             ("पुनापि", "The र् is not dropped before a vowel."),
             ("पुनश्पि", "श् comes before च/छ, not before a vowel.")],
            "पुनर् + अपि = पुनरपि, like पुनर् + आहुः = पुनराहुः.",
            "पुनर् + vowel: र् stays.",
            teaches="The र् of पुनर् stays before a vowel and joins it: पुनर् + आहुः → पुनराहुः."),
    ],
}

# ---------------------------------------------------------------- unit 50
AUTHORED["50"] = {
    "title": "तत्र गर्भस्य मरणम्",
    "question": "By the sure words of unit 50, what is spoken of, and which reading is doubtful?",
    "rule": ("There (तत्र), death (मरणम्) of the embryo (गर्भस्य). The reason, printed नैर्ऋतभागतवात्, is read "
             "conjecturally as नैर्ऋतभागत्वात्: because of being the Nairṛta share."),
    "limits": ("Low confidence. -भागत्वात् for printed -भागतवात् is a conjecture. Nairṛta = belonging to Nirṛti, deity of "
               "ruin and death (probable; also the south-west quarter). What the share is is not stated. No question rests on these."),
    "explain_hi": ("इस पंक्ति का अर्थ पक्का नहीं है। निश्चित भाग इतना है: ‘वहाँ गर्भ की मृत्यु’ (तत्र गर्भस्य मरणम्)। "
                   "कारण छपा है ‘नैर्ऋतभागतवात्’, जो नियमित रूप नहीं; अनुमानित पाठ ‘नैर्ऋतभागत्वात्’ है, यानी नैर्ऋत भाग होने के कारण। "
                   "नैर्ऋत = निर्ऋति (विनाश और मृत्यु की देवी) से सम्बन्धित, यह पहचान सम्भावित है; इसका अर्थ दक्षिण-पश्चिम दिशा भी हो सकता है। "
                   "‘भाग’ क्या है, नहीं बताया गया। पंक्ति में क्रिया नहीं है।"),
    "hook": "निश्चित भाग: तत्र गर्भस्य मरणम्।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By the sure words of unit 50, what is spoken of for the embryo?",
            ("Its death (मरणम्)", "गर्भस्य मरणम्: death of the embryo."),
            [("Its birth (जन्म)", "Birth is the word of unit 44, not of unit 50."),
             ("Its turning round", "Turning round is unit 46."),
             ("Its taking of ojas", "Taking ojas is unit 42.")],
            "The sure part is death of the embryo.",
            "गर्भस्य मरणम्."),
        order(1, "Put the printed words of unit 50 in the line's order.",
              ["नैर्ऋतभागतवात्", "तत्र", "गर्भस्य", "मरणम्"],
              "The reason (doubtful reading), there, of the embryo, death.",
              "नैर्ऋतभागतवात् → तत्र → गर्भस्य → मरणम्."),
        match(2, "Match each sure word of unit 50 to its meaning.",
              [["तत्र", "there, in that case"], ["गर्भस्य", "of the embryo"], ["मरणम्", "death"]],
              "These three words are the sure part of the line.",
              "तत्र, गर्भस्य, मरणम्.", role="extend",
              teaches="गर्भस्य is the genitive: -स्य = of; गर्भस्य मरणम् = death of the embryo."),
        mcq("discriminate", 3, "Which printed word of unit 50 does the card mark as a doubtful, conjectural reading?",
            ("नैर्ऋतभागतवात्", "The flag: भागतवात् is not a form; भागत्वात् is a conjecture."),
            [("तत्र", "तत्र is a sure word: there."),
             ("गर्भस्य", "गर्भस्य is a sure word: of the embryo."),
             ("मरणम्", "मरणम् is a sure word: death.")],
            "Only the first word is doubtful.",
            "नैर्ऋतभागतवात् → (conjecture) नैर्ऋतभागत्वात्."),
        multi("apply", 4, "Which statements about the sure words of unit 50 are right?",
              [("It has no verb", "Right: a nominal line."),
               ("It names the mother's weariness (ग्लानि)", "The mother's weariness is unit 48."),
               ("It names the birth (जन्म) of the embryo", "Birth is unit 44; here the word is मरणम्."),
               ("It names the death (मरणम्) of the embryo", "Right: गर्भस्य मरणम्.")],
              [0, 3],
              "A nominal line whose sure part is death of the embryo.",
              "तत्र गर्भस्य मरणम् (no verb)."),
        mcq("transfer", 5, "By the गर्भस्य of unit 50, how is the birth of the child (बाल) said in an invented phrase?",
            ("बालस्य जन्म", "-स्य = of, as गर्भस्य = of the embryo."),
            [("बालः जन्म", "बालः is nominative: the child, not of the child."),
             ("बालेन जन्म", "बालेन is instrumental: by the child."),
             ("बालाय जन्म", "बालाय is dative: to the child.")],
            "बालस्य जन्म = the birth of the child, like गर्भस्य मरणम्.",
            "a-stem genitive singular = -स्य.",
            teaches="The genitive singular of an a-stem ends in -स्य: गर्भ → गर्भस्य (of the embryo), बाल → बालस्य."),
    ],
}

# ===================================================================== NOTES_HI
NOTES_HI = {
    "39": ("गद्य-पंक्ति; विश्वास उच्च; कोई पाठ-चिह्न नहीं। ‘पंचमे’ के बाद ‘मास’ छपा नहीं, क्रम से समझा गया। "
           "‘भवति’ दूसरे वाक्यांश में भी समझा जाता है। छपा ‘पंचमे’ = पञ्चमे (अनुस्वार = ञ्)। शोणित = रक्त (मानक)। "
           "सन्धि जाँची: शोणित + उपचय → शोणितोपचय (अ + उ → ओ); उपचयः + च → उपचयश्च (विसर्ग → श्)।"),
    "40": ("गद्य-पंक्ति; विश्वास उच्च; कोई पाठ-चिह्न नहीं। स्नायु = कण्डरा/स्नायुबन्ध (सम्भावित)। वर्ण = त्वचा का रंग। "
           "छपा ‘स्नायवादीनि’ को डेटा स्नायु + आदीनि पढ़ता है (उ को अव् लिखा गया); नियमित यण्-सन्धि से स्नाय्वादीनि होता, "
           "इसलिए इस रूप पर प्रश्न नहीं। सन्धि जाँची: नख + अस्थि → नखास्थि (अ + अ → आ); आदीनि + अभिव्यक्तानि → "
           "आदीन्यभिव्यक्तानि (इ + अ → य); वर्ण + उपचय → वर्णोपचय (अ + उ → ओ)।"),
    "41": ("गद्य-पंक्ति; विश्वास उच्च; कोई पाठ-चिह्न नहीं; क्रिया नहीं और जोड़ी भी नहीं गई। ‘मास’ क्रम से समझा गया। "
           "छपा ‘सर्वांगसंपूर्णता’ = सर्वाङ्गसम्पूर्णता (अनुस्वार = ङ्, म्)। सन्धि जाँची: सर्व + अङ्ग → सर्वाङ्ग (अ + अ → आ)।"),
    "42": ("विश्वास मध्यम। पाठ-चिह्न: ‘मातृंतो’ → सम्भवतः मातृतो (अनावश्यक अनुस्वार; ‘-तः’ घोष ग से पहले ‘-तो’)। "
           "छपा ‘अष्टमेगर्भश्च’ एक टोकन = अष्टमे + गर्भः + च। क्रिया ‘आददाते’ द्विवचन, कर्ता गर्भ और माता। ओज = जीवन-सार "
           "(आधुनिक समानार्थी नहीं); रस = पोषक द्रव (रस धातु)। सन्धि जाँची: गर्भतः + च → गर्भतश्च; रसहारिणीभिः + वाहिनीभिः → "
           "रसहारिणीभिर्वाहिनीभिः (ई के बाद विसर्ग → र्); मुहुः + मुहुः → मुहुर्मुहुः; मुहुः + ओजः → मुहुरोजः।"),
    "43": ("विश्वास उच्च; कोई पाठ-चिह्न नहीं। छपा ‘भवतिमुहुर्म्लाना’ = भवति मुहुः म्लाना (केवल शब्द-विभाग, वर्तनी-दोष नहीं)। "
           "‘तथा गर्भः’ में क्रिया पहले से समझी जाती है। ‘तदा’ का समय पंक्ति में नामित नहीं। सन्धि जाँची: मुहुः + मुदिता → "
           "मुहुर्मुदिता; मुहुः + म्लाना → मुहुर्म्लाना (उ के बाद विसर्ग → र् घोष से पहले)।"),
    "44": ("विश्वास उच्च; कोई पाठ-चिह्न नहीं। ‘व्यापत्तिमत्’ = मतुप् प्रत्यय वाला नपुंसक, ‘जन्म’ का विशेषण। ‘तदा’ को डेटा की "
           "टिप्पणी इकाई 42 का आठवाँ (मास) मानती है; यहाँ नामित नहीं। सन्धि जाँची: व्यापत्तिमत् + तदा → व्यापत्तिमत्तदा "
           "(कोई परिवर्तन नहीं); छपा ‘एवं’ = एवम्।"),
    "45": ("विश्वास उच्च; कोई पाठ-चिह्न नहीं। एक ही टोकन, अवग्रह सहित। टिप्पणी के अनुसार यह आश्रित पञ्चमी-पद सम्भवतः इकाई 44 "
           "का कारण बताता है (‘appears to’ — पक्का नहीं)। सन्धि जाँची: ओजसः + अनवस्थितत्वात् → ओजसोऽनवस्थितत्वात् "
           "(अः + अ → ओऽ); अन् + अवस्थित → अनवस्थित।"),
    "46": ("विश्वास निम्न; अर्थ केवल रूपरेखा में। वाक्य-रचना ढीली: ‘अस्य ... उन्मुखस्य’ षष्ठी, ‘अनुभवन्’ प्रथमा; अनुवाद छपे रूपों "
           "पर। छपा ‘एषौजसा’ को एषः + ओजसा पढ़ा गया; सामान्य सन्धि से ‘एष ओजसा’ होता (एषः का विसर्ग लुप्त, फिर सन्धि नहीं), "
           "इसलिए इस रूप पर प्रश्न नहीं। छपा ‘निष्क्रमणोन्मुखस्यपरिवर्तनादीन्यनुभवन्’ में शब्दों के बीच स्थान नहीं। "
           "सन्धि जाँची: हि + अस्य → ह्यस्य (इ + अ → य); निष्क्रमण + उन्मुख → निष्क्रमणोन्मुख (अ + उ → ओ); "
           "परिवर्तनादीनि + अनुभवन् → परिवर्तनादीन्यनुभवन्।"),
    "47": ("विश्वास मध्यम; कोई पाठ-चिह्न नहीं। उपमा ‘कटे अंग की तरह’ पूरे वाक्यांश से जुड़ी है, या ‘कटे अंग में जैसे’ भी पढ़ी जा "
           "सकती है — तय नहीं। संस्कार = बची हुई छाप या वेग। छपा ‘किंचित्’, ‘अंग’ = किञ्चित्, अङ्ग। सन्धि जाँची: यदि + अपि → "
           "यद्यपि; किंचित्कालम् + अस्य → किंचित्कालमस्य; अस्य + उच्छ्वसनम् → अस्योच्छ्वसनम्; स्यात् + तत् → स्यात्तत्; तत् + छिन्नस्य → "
           "तच्छिन्नस्य; छिन्नस्य + इव → छिन्नस्येव; इव + अङ्गस्य → इवाङ्गस्य; अङ्गस्य + ओजः → अङ्गस्यौजः (अ + ओ → औ)।"),
    "48": ("विश्वास मध्यम; कोई पाठ-चिह्न नहीं। ‘रसे संक्रान्ते’ सति-सप्तमी; ‘है’ समझा गया (हिन्दी में नहीं जोड़ा गया)। अन्तिम ‘इति’ "
           "इस मत को समाप्त करता है। छपा ‘संक्रांते’ = संक्रान्ते। सन्धि जाँची: जनन्याः + तु → जनन्यास्तु (विसर्ग → स्); स्थिर + "
           "ओजस्कतया → स्थिरौजस्कतया (अ + ओ → औ); ओजस्कतया + एकदेशेन → ओजस्कतयैकदेशेन (आ + ए → ऐ); ग्लानिः + एव → "
           "ग्लानिरेव; एव + इति → एवेति (अ + इ → ए)।"),
    "49": ("विश्वास उच्च; कोई पाठ-चिह्न नहीं। छपा ‘अन्येपुनराहुः’ एक टोकन = अन्ये पुनर् आहुः। आगे आने वाले मत की भूमिका; मत इस "
           "इकाई में पूरा नहीं। ‘आहुः’ = √अह् लिट् प्रथम पुरुष बहुवचन। सन्धि जाँची: पुनर् + आहुः → पुनराहुः।"),
    "50": ("विश्वास निम्न। पाठ-चिह्न: ‘नैर्ऋतभागतवात्’ → सम्भवतः नैर्ऋतभागत्वात् (‘भागतवात्’ कोई रूप नहीं; अतिरिक्त ‘अ’)। "
           "नैर्ऋत = निर्ऋति से सम्बन्धित (सम्भावित; दक्षिण-पश्चिम दिशा भी)। ‘भाग’ क्या है, नहीं कहा गया; ‘तत्र’ = वहाँ, उस दशा में। "
           "क्रिया नहीं। अर्थ पक्का नहीं, इसलिए इन बिन्दुओं पर प्रश्न नहीं।"),
}

# ===================================================================== AIDS
AIDS = {
    "39": {
        "diagram": {"groups": [{"label": "पञ्चमे (पाँचवें में)", "items": ["मन अधिक प्रबुद्ध", "मांस-शोणित का उपचय"]}]},
        "chunks": "पंचमे | मनः प्रबुद्धतरं भवति | मांसशोणितोपचयश्च",
        "sandhi": "अ + उ → ओ: शोणित + उपचय → शोणितोपचय · विसर्ग + च → श्च: उपचयः + च → उपचयश्च।",
        "pegs": "मेरा बनाया चित्र (केवल याद के लिए): पाँच उँगलियों वाला हाथ माथे पर — मन जागता है; हाथ में मांस-रक्त की लाली।",
    },
    "40": {
        "diagram": {"groups": [
            {"label": "अभिव्यक्त होते हैं (क्रम से)", "items": ["केश", "रोम", "नख", "अस्थि", "स्नायु (सम्भावित: कण्डरा/स्नायुबन्ध)", "आदि"]},
            {"label": "उपचय", "items": ["बल", "वर्ण (त्वचा का रंग)"]}]},
        "chunks": "षष्ठे | केशरोमनखास्थिस्नायवादीन्यभिव्यक्तानि | बलवर्णोपचयश्च",
        "sandhi": "इ + अ → य: आदीनि + अभिव्यक्तानि → आदीन्यभिव्यक्तानि · अ + अ → आ: नख + अस्थि → नखास्थि।",
        "letters": "पाँच अंगों के पहले अक्षर क्रम से: के-रो-न-अ-स्ना (केश, रोम, नख, अस्थि, स्नायु)। (मेरी याद-पद्धति)",
    },
    "41": {
        "chunks": "सप्तमे | सर्वांगसंपूर्णता",
        "sandhi": "अ + अ → आ: सर्व + अङ्ग → सर्वाङ्ग।",
        "anchors": "याद-सूत्र: ‘स’ से ‘स’ — सप्तमे सर्वाङ्ग: सातवें में सब अंग पूरे। (मेरी याद-पद्धति)",
    },
    "42": {
        "diagram": {"groups": [
            {"label": "कौन", "items": ["गर्भ (माता से)", "माता (गर्भ से)"]},
            {"label": "क्या, कैसे", "items": ["ओज", "रसहारिणी वाहिनियों से", "बार-बार, परस्पर"]}]},
        "chunks": "अष्टमेगर्भश्च मातृंतो | गर्भतश्च माता | रसहारिणीभिर्वाहिनीभिः | मुहुर्मुहुरोजः | परस्परमाददाते",
        "sandhi": "ई के बाद विसर्ग → र् घोष से पहले: रसहारिणीभिः + वाहिनीभिः → रसहारिणीभिर्वाहिनीभिः · विसर्ग + च → श्च: गर्भतः + च → गर्भतश्च।",
        "frame": "दो कर्ता (गर्भः, माता) → द्विवचन क्रिया (आददाते); साधन तृतीया (वाहिनीभिः); कर्म (ओजः)।",
    },
    "43": {
        "seesaw": "मुहुः मुदिता (कभी प्रसन्न) ↔ मुहुः म्लाना (कभी मुरझाई) — गर्भिणी; ‘तथा गर्भः’: गर्भ भी वैसे ही।",
        "chunks": "तस्मात्तदा गर्भिणी | मुहुर्मुदिता भवति | मुहुर्म्लाना | तथा गर्भः",
        "sandhi": "उ के बाद विसर्ग → र् घोष से पहले: मुहुः + मुदिता → मुहुर्मुदिता · मुहुः + म्लाना → मुहुर्म्लाना।",
    },
    "44": {
        "chunks": "एवं गर्भस्य जन्म | व्यापत्तिमत्तदा भवति",
        "frame": "कर्ता: जन्म (गर्भस्य का) → विशेषण: व्यापत्तिमत् (नपुंसक, जन्म से मेल) → समय: तदा → क्रिया: भवति।",
        "sandhi": "त् + त → त्त (कोई परिवर्तन नहीं): व्यापत्तिमत् + तदा → व्यापत्तिमत्तदा।",
    },
    "45": {
        "chunks": "ओजसो | ऽनवस्थितत्वात्",
        "frame": "अन् (नहीं) + अवस्थित (स्थिर) + त्व (-ता) + आत् (के कारण) = अस्थिरता के कारण; किसकी? ओजसः (ओज की)।",
        "sandhi": "अः + अ → ओऽ: ओजसः + अनवस्थितत्वात् → ओजसोऽनवस्थितत्वात्।",
    },
    "46": {
        "chunks": "तथा ह्यस्य | निष्क्रमणोन्मुखस्य | परिवर्तनादीन्यनुभवन् | एषौजसा वियोगः",
        "frame": "किसका: अस्य निष्क्रमणोन्मुखस्य (निकलने को उन्मुख) → क्या अनुभव: परिवर्तन आदि → फल: ओजसा वियोगः। (वाक्य-रचना ढीली, अर्थ रूपरेखा में)",
        "sandhi": "इ + अ → य: हि + अस्य → ह्यस्य · अ + उ → ओ: निष्क्रमण + उन्मुख → निष्क्रमणोन्मुख।",
    },
    "47": {
        "diagram": {"groups": [
            {"label": "वाक्यांश (क्रम से)", "items": ["यद्यपि ... उच्छ्वसनं स्यात्", "छिन्नस्येवाङ्गस्य", "ओजःसंस्कारानुवृत्तिकृतम्"]},
            {"label": "अर्थ", "items": ["कुछ समय साँस हो भी", "कटे अंग की तरह (उपमा)", "ओज के संस्कार की अनुवृत्ति से"]}]},
        "chunks": "यद्यपि च | किंचित्कालमस्योच्छ्वसनं | स्यात्तच्छिन्नस्येवांगस्यौजःसंस्कारानुवृत्तिकृतं",
        "sandhi": "त् + छ → च्छ: तत् + छिन्नस्य → तच्छिन्नस्य · अ + ओ → औ: अङ्गस्य + ओजः → अङ्गस्यौजः · इ + अ → य: यदि + अपि → यद्यपि।",
    },
    "48": {
        "chain": {"steps": ["जननी (माता)", "स्थिर ओज के कारण", "रस एक अंश में संक्रान्त होने पर", "केवल ग्लानि"]},
        "chunks": "जनन्यास्तु | स्थिरौजस्कतयैकदेशेन | रसे संक्रांते | ग्लानिरेवेति",
        "sandhi": "विसर्ग + त → स्त: जनन्याः + तु → जनन्यास्तु · आ + ए → ऐ: ओजस्कतया + एकदेशेन → ओजस्कतयैकदेशेन · इ के बाद विसर्ग → र्: ग्लानिः + एव → ग्लानिरेव।",
    },
    "49": {
        "chunks": "अन्ये | पुनर् | आहुः",
        "sandhi": "र् स्वर से पहले बना रहता है: पुनर् + आहुः → पुनराहुः।",
        "anchors": "याद-सूत्र: ‘अन्ये पुनराहुः’ = अब दूसरा मत आने वाला है; मत इसके बाद की इकाई में। (मेरी याद-पद्धति)",
    },
    "50": {
        "chunks": "नैर्ऋतभागतवात् (?) | तत्र | गर्भस्य मरणं",
        "frame": "कारण (पञ्चमी, अनुमानित पाठ: नैर्ऋतभागत्वात्) → स्थान: तत्र → फल: गर्भस्य मरणम्। क्रिया नहीं।",
        "anchors": "याद-सूत्र: निश्चित भाग केवल ‘तत्र गर्भस्य मरणम्’; पहला शब्द संदिग्ध। (मेरी याद-पद्धति)",
    },
}

# ===================================================================== IMAGE_SPECS
IMAGE_SPECS = {
    ("39", "diagram"): {
        "file": "sh2-panchama-masa-39.svg",
        "alt": ("Flowchart of unit 39: in the fifth (month) two things happen: the mind becomes more awakened, and "
                "flesh and blood increase."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"पञ्चमे (पाँचवें में)\"] --> B[\"मन अधिक प्रबुद्ध\"]\n"
                 "  A --> C[\"मांस-शोणित का उपचय\"]\n"),
    },
    ("40", "diagram"): {
        "file": "sh2-shashtha-masa-40.svg",
        "alt": ("Two columns of unit 40, the sixth month: made manifest, in order: hair, body-hair, nails, bones, sinews "
                "(probably tendons or ligaments) and so on; increased: strength and complexion."),
        "type": "split",
        "title": "षष्ठे (छठे में) — इकाई ४०",
        "cols": [["अभिव्यक्त (क्रम से)", ["१ केश", "२ रोम", "३ नख", "४ अस्थि", "५ स्नायु (सम्भावित: कण्डरा/स्नायुबन्ध)", "आदि"]],
                 ["उपचय", ["बल", "वर्ण (त्वचा का रंग)"]]],
    },
    ("42", "diagram"): {
        "file": "sh2-oja-paraspara-42.svg",
        "alt": ("Flowchart of unit 42: in the eighth (month), through the channels that carry rasa, the embryo takes ojas "
                "from the mother and the mother from the embryo, repeatedly and mutually."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"अष्टमे (आठवें में)\"] --> V[\"रसहारिणी वाहिनियाँ\"]\n"
                 "  V --> G[\"गर्भ: माता से ओज\"]\n"
                 "  V --> M[\"माता: गर्भ से ओज\"]\n"
                 "  G <-->|\"बार-बार, परस्पर\"| M\n"),
    },
    ("43", "seesaw"): {
        "file": "sh2-mudita-mlana-43.svg",
        "alt": ("Flowchart of unit 43: then the pregnant woman is at times glad and at times languid; likewise the embryo "
                "has the same two states."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"तस्मात् तदा गर्भिणी\"] --> B[\"मुहुः मुदिता (कभी प्रसन्न)\"]\n"
                 "  A --> C[\"मुहुः म्लाना (कभी मुरझाई)\"]\n"
                 "  B -.-> D[\"तथा गर्भः (गर्भ भी वैसे ही)\"]\n"
                 "  C -.-> D\n"),
    },
    ("47", "diagram"): {
        "file": "sh2-ucchvasana-47.svg",
        "alt": ("Table of unit 47 in line order: even if there is breathing for some time; like a severed limb (a "
                "comparison); made by the continuation of the impression of ojas."),
        "type": "table",
        "title": "इकाई ४७: कुछ समय का उच्छ्वसन",
        "heads": ["वाक्यांश", "अर्थ"],
        "rows": [["यद्यपि ... उच्छ्वसनं स्यात्", "कुछ समय साँस हो भी"],
                 ["छिन्नस्येवाङ्गस्य", "कटे अंग की तरह (उपमा)"],
                 ["ओजःसंस्कारानुवृत्तिकृतम्", "ओज के संस्कार की अनुवृत्ति से"]],
    },
    ("48", "chain"): {
        "file": "sh2-janani-glani-48.svg",
        "alt": ("Chain of unit 48: the mother; because her ojas is stable; when rasa has passed over in one part; only "
                "weariness."),
        "type": "chain",
        "title": "इकाई ४८: माता में केवल ग्लानि",
        "steps": ["जननी (माता)", "स्थिर ओज के कारण", "रस एक अंश में संक्रान्त", "केवल ग्लानि"],
    },
}
