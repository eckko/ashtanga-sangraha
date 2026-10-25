from helpers import mcq, match, order, fill, multi, accepts


def T(q, teaches):
    q["teaches"] = teaches
    return q


AUTHORED = {}

# ---------------------------------------------------------------- unit 14
AUTHORED["14"] = {
    "title": "तयोर्विशेषः",
    "question": "What does the short heading of card 14 announce, and how is it joined?",
    "rule": ("तयोः विशेषः: the distinction (विशेषः) of the two (तयोः). The heading names neither item and prints no verb; "
             "तयोः + विशेषः → तयोर्विशेषः (ओः before a voiced sound → ओर्)."),
    "limits": ("Prose heading, elliptical. The two are not named: by position the data takes them as chāyā and prabhā "
               "(card 15), but the line does not say so; no question asks who the two are. तयोः can be genitive or "
               "locative dual: no question on its case."),
    "explain_hi": ("यह इकाई केवल एक शीर्षक जैसा वाक्यांश है: ‘उन दोनों का भेद’। "
                   "दोनों कौन हैं, यह यहाँ छपा नहीं; स्थान के आधार पर डेटा इन्हें छाया और प्रभा (कार्ड १५) मानता है, पर पंक्ति यह नहीं कहती। "
                   "कोई क्रिया नहीं छपी। "
                   "‘तयोर्विशेषः’ में तयोः + विशेषः की सन्धि है: ओ के बाद का विसर्ग घोष वर्ण (व) से पहले र् बनता है।"),
    "hook": "तयोर्विशेषः: दो चीज़ों का भेद आगे आने वाला है।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 14, what does विशेषः mean?",
            ("Distinction", "विशेषः = distinction, difference: तयोर्विशेषः, the distinction of the two."),
            [("Likeness", "Likeness would be सादृश्य; विशेष is a difference."),
             ("Origin", "Origin would be उत्पत्ति; विशेष is a difference."),
             ("Resemblance", "Resemblance would be साम्य; विशेष is a difference.")],
            "विशेषः = distinction.",
            "विशेष = distinction."),
        T(multi("warmup", 1, "Which statements fit card 14 as printed?",
                [("It names the two things it compares", "No: the two are not named in the line."),
                 ("It prints no verb", "Right: the line is two words, with no verb."),
                 ("It lists seven colours of radiance", "No: the line has only तयोः and विशेषः."),
                 ("तयोः is a dual form, of or in the two", "Right: तयोः is dual; the data takes it as genitive.")],
                [1, 3],
                "Two words, no verb, the two items unnamed; तयोः is dual.",
                "तयोः (dual) + विशेषः (distinction)."),
          "An elliptical heading can announce a topic without naming its items or giving a verb."),
        fill(2, "The word for 'distinction' in card 14 is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("विशेषः", "viśeṣaḥ", "विशेष"),
             "विशेषः = distinction: तयोर्विशेषः, the distinction of the two.",
             "विशेष means distinction, difference; in तयोर्विशेषः it is the nominative singular.",
             "विशेषः = distinction."),
        mcq("discriminate", 3, "Which split of तयोर्विशेषः in card 14 is right?",
            ("तयोः + विशेषः", "ओः before the voiced व → ओर्: तयोः + विशेषः → तयोर्विशेषः."),
            [("तयोः + अविशेषः", "That would print तयोरविशेषः, with रवि; the print has र्वि."),
             ("तयो + र्विशेषः", "र्विशेषः is not a word; the र् comes from the visarga."),
             ("तयोर्वि + शेषः", "तयोर्वि is not a word; तयोः and विशेषः are the two words.")],
            "तयोः (of the two) + विशेषः (distinction).",
            "ओः + voiced sound → ओर्."),
        mcq("apply", 4, "Why does the visarga of तयोः become र् before विशेषः in card 14?",
            ("After ओ, ः before a voiced sound → र्", "The visarga follows ओ (not अ or आ), and व is voiced: so र्."),
            [("Every ः before a consonant → र्", "Not every: before त a visarga becomes स् (अतिरूक्षास्ताम्राः, card 23)."),
             ("र् is part of the stem तयोर्", "The form is तयोः; the र् comes only from sandhi."),
             ("After ओ, ः before any sound drops", "It does not drop here; after ओ it gives र् before a voiced sound.")],
            "तयोः + विशेषः: visarga after ओ before the voiced व → र्.",
            "Visarga after a vowel other than अ/आ, before a voiced sound → र्."),
        mcq("transfer", 5, "By the pattern of तयोर्विशेषः, how is गुरोः + वचनम् (the teacher's word) joined in a new example?",
            ("गुरोर्वचनम्", "Visarga after ओ before the voiced व → र्: गुरोः + वचनम् → गुरोर्वचनम्."),
            [("गुरो वचनम्", "After ओ the visarga is not dropped before a voiced sound; it gives र्."),
             ("गुरोस्वचनम्", "स् comes from a visarga before त or थ, not before व."),
             ("गुरोश्वचनम्", "श् comes from a visarga before च, छ or श, not before व.")],
            "गुरोः + वचनम् = गुरोर्वचनम्, like तयोः + विशेषः = तयोर्विशेषः.",
            "ओः + voiced sound → ओर्.",
            teaches="A visarga after a vowel other than अ/आ becomes र् before a voiced sound: तयोः + विशेषः → तयोर्विशेषः."),
    ],
}

# ---------------------------------------------------------------- unit 15
AUTHORED["15"] = {
    "title": "छाया वर्णमाक्रामति",
    "question": "By card 15, how does chāyā differ from prabhā in what it does to colour, in distance and in make-up?",
    "rule": ("Chāyā overspreads the colour (वर्णम् आक्रामति), is near (आसन्ना; 'perceived' rests on a conjecture) and consists of the five elements "
             "(पञ्चभूतात्मिका); prabhā illuminates the colour (वर्णं प्रकाशयति), is perceived from afar and is the "
             "radiance of tejas (तेजःप्रभा)."),
    "limits": ("Medium confidence. Printed चलच्यते is no word; 'ca lakṣyate' (is perceived) is a conjecture: no question "
               "on how chāyā is perceived. तेजःप्रभैव may also be read तेजः, प्रभा एव; either way prabhā goes with "
               "tejas. Two printed lines joined."),
    "explain_hi": ("यह इकाई दो छपी पंक्तियाँ जोड़ती है और कार्ड १४ के ‘भेद’ को खोलती है। "
                   "छाया वर्ण पर छा जाती है (वर्णमाक्रामति), अनुमानित पाठ पर समीप (आसन्ना) दिखती है और पाँच भूतों से बनी (पञ्चभूतात्मिका) है। "
                   "प्रभा तो वर्ण को प्रकाशित करती है (वर्णं प्रकाशयति), दूर से दिखाई देती है (विप्रकृष्टा लक्ष्यते) और तेजस् की प्रभा ही है। "
                   "छपा ‘चलच्यते’ कोई शब्द नहीं; ‘च लक्ष्यते’ (दिखाई देती है) अनुमानित पाठ है, इसलिए छाया कैसे दिखती है, इस पर प्रश्न नहीं। "
                   "‘प्रभैव’ में प्रभा + एव की सन्धि है (आ + ए → ऐ)।"),
    "hook": "छाया ढकती है, पास है, पंचभूत की; प्रभा चमकाती है, दूर से दिखे, तेज की।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By card 15, what does प्रभा do to the colour?",
            ("It illuminates it", "प्रभा तु वर्णं प्रकाशयति: prabhā illuminates the colour."),
            [("It overspreads it", "Overspreading the colour (आक्रामति) is said of chāyā, not prabhā."),
             ("It hides it fully", "Nothing in card 15 says prabhā hides the colour."),
             ("It turns it dark", "Nothing in card 15 says prabhā darkens the colour.")],
            "प्रकाशयति = illuminates.",
            "प्रभा → वर्णं प्रकाशयति."),
        match(1, "Match each word of card 15 to its meaning.",
              [["आक्रामति", "overspreads"], ["प्रकाशयति", "illuminates"], ["विप्रकृष्टा", "distant"],
               ["पञ्चभूतात्मिका", "made of the five elements"], ["तेजः", "fire (tejas)"]],
              "आक्रामति = overspreads, प्रकाशयति = illuminates, विप्रकृष्टा = distant, पञ्चभूतात्मिका = made of the five bhūtas, तेजः = fire.",
              "आक्रामति, प्रकाशयति, विप्रकृष्टा, पञ्चभूतात्मिका, तेजः."),
        order(2, "Put these sure parts of card 15 in the printed order.",
              ["छाया", "वर्णमाक्रामत्यासन्ना", "पंचभूतात्मिका", "प्रभा तु", "वर्णं प्रकाशयति", "तेजःप्रभैव"],
              "Line 1 is about chāyā (overspreads the colour, of five elements); line 2 about prabhā (illuminates the colour, radiance of tejas).",
              "छाया → वर्णमाक्रामत्यासन्ना → पंचभूतात्मिका → प्रभा तु → वर्णं प्रकाशयति → तेजःप्रभैव.",
              role="extend",
              teaches="तु (but) opens line 2 and sets prabhā against chāyā point by point."),
        mcq("discriminate", 3, "By card 15, which of these is said of chāyā, not of prabhā?",
            ("It is made of the five elements", "छाया ... पंचभूतात्मिका: chāyā consists of the five bhūtas."),
            [("It is seen from far away", "Being seen from afar (विप्रकृष्टा लक्ष्यते) is said of prabhā."),
             ("It makes the colour shine", "Illuminating the colour (प्रकाशयति) is said of prabhā."),
             ("It is the radiance of fire", "The radiance of tejas (तेजःप्रभा) is said of prabhā.")],
            "Chāyā: overspreads, near, five elements. Prabhā: illuminates, from afar, tejas.",
            "पंचभूतात्मिका belongs to छाया."),
        mcq("apply", 4, "Which split of प्रभैव in card 15 is right?",
            ("प्रभा + एव", "आ + ए → ऐ: प्रभा + एव → प्रभैव."),
            [("प्रभा + इव", "आ + इ gives ए: that would print प्रभेव."),
             ("प्रभे + एव", "प्रभे is not the nominative; the subject is प्रभा."),
             ("प्रभ + ऐव", "ऐव is not a word; the ऐ comes from आ + ए.")],
            "प्रभा (radiance) + एव (just): आ + ए → ऐ.",
            "आ + ए → ऐ."),
        mcq("transfer", 5, "By the pattern of प्रभा + एव → प्रभैव, how is सा + एव (she alone) joined in a new example?",
            ("सैव", "आ + ए → ऐ: सा + एव → सैव."),
            [("सेव", "ए comes from आ + इ (सा + इव → सेव), not from आ + ए."),
             ("सौव", "औ comes from आ + ओ or आ + औ, not from आ + ए."),
             ("सायेव", "No य् is inserted between आ and ए; they merge into ऐ.")],
            "सा + एव = सैव, like प्रभा + एव = प्रभैव.",
            "आ + ए → ऐ.",
            teaches="अ or आ before ए or ऐ gives ऐ: प्रभा + एव → प्रभैव."),
    ],
}

# ---------------------------------------------------------------- unit 16
AUTHORED["16"] = {
    "title": "यस्य दृष्टौ प्रतिच्छायमयी कुमारिका",
    "question": "By card 16, what is not seen in the eye of one who is called parāsu?",
    "rule": ("He in whose eye (दृष्टौ) the kumārikā (literally 'little girl'; probably the small figure seen in the pupil) made of reflection (प्रतिच्छायमयी कुमारिका) is not seen is "
             "parāsu (परासुः), one whose life-breath has gone."),
    "limits": ("Prose. कुमारिका is literally 'little girl'; that it is the small figure seen in the pupil is only "
               "probable (data's label): no question rests on what it is. दृष्टि is taken as the eye. 'Is' is understood."),
    "explain_hi": ("जिसकी दृष्टि (आँख) में प्रतिबिम्ब से बनी कुमारिका नहीं दिखाई देती, वह परासु है, यानी जिसके प्राण चले गए। "
                   "कुमारिका का शब्दार्थ ‘छोटी कन्या’ है; यह सम्भवतः पुतली में दिखने वाली छोटी आकृति है (सम्भावित, डेटा का लेबल)। "
                   "परासु = परा (दूर गए) + असु (प्राण): बहुव्रीहि। "
                   "‘सपरासुः’ में सः + परासुः है: सः व्यंजन से पहले विसर्ग खो देता है। क्रिया ‘है’ समझी जाती है।"),
    "hook": "आँख में प्रतिच्छायमयी कुमारिका (सम्भवतः पुतली की छोटी आकृति) न दिखे: परासु।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 16, what does परासुः mean?",
            ("One whose life-breath has gone", "परा (gone away) + असु (life-breath): one whose breath has gone."),
            [("One whose strength has grown greatly", "परासु names breath gone away, not strength grown."),
             ("One who sleeps very deeply", "Nothing in परासु names sleep; असु is life-breath."),
             ("One who sees all things well", "परासु says nothing of sight; it names breath gone.")],
            "परासुः = one whose asu (life-breath) has gone.",
            "परा + असु = परासु."),
        match(1, "Match each word of card 16 to its meaning.",
              [["दृष्टौ", "in the eye"], ["प्रतिच्छाय", "reflection"], ["न", "not"], ["दृश्यते", "is seen"],
               ["परासुः", "one whose life-breath has gone"]],
              "दृष्टौ = in the eye (sight), प्रतिच्छाय = reflection, न = not, दृश्यते = is seen, परासुः = one whose breath has gone.",
              "दृष्टौ, प्रतिच्छाय, न, दृश्यते, परासुः."),
        order(2, "Put the words of card 16 in the printed order.",
              ["यस्य", "दृष्टौ", "प्रतिच्छायमयी", "कुमारिका", "न दृश्यते", "सपरासुः"],
              "Whose; in the eye; made of reflection; the little figure; is not seen; he is parāsu.",
              "यस्य → दृष्टौ → प्रतिच्छायमयी → कुमारिका → न दृश्यते → सपरासुः.",
              role="extend",
              teaches="यस्य (whose) ... सः (he): the relative clause comes first and सः picks it up."),
        mcq("discriminate", 3, "Why is सः printed स before परासुः in card 16?",
            ("सः drops its visarga before a consonant", "The pronoun सः loses its visarga before a consonant: स परासुः."),
            [("Every अः drops ः before a consonant", "Not every: other words keep it or change it (अधरोष्ठो याति, card 22)."),
             ("स is here the feminine pronoun", "The feminine is सा; स here is the masculine सः."),
             ("ः before प always becomes स्", "The print has no स्; the visarga of सः is simply dropped.")],
            "सः + परासुः → स परासुः (printed as one token).",
            "सः / एषः lose the visarga before a consonant."),
        mcq("apply", 4, "In प्रतिच्छायमयी of card 16, what does -मयी add?",
            ("Made of", "-मय (feminine -मयी) = made of, consisting of: made of reflection."),
            [("Without", "Without would be a prefix such as निर्- or अ-, not -मयी."),
             ("Like", "Like would be -वत् or इव, not -मयी."),
             ("Seen by", "Seen by would need a passive participle, not -मयी.")],
            "प्रतिच्छाय-मयी: made of reflection; feminine, agreeing with कुमारिका.",
            "-मय / -मयी = made of."),
        mcq("transfer", 5, "By the pattern of प्रतिच्छायमयी (made of reflection), what does काष्ठमयी mean in a new example?",
            ("Made of wood", "-मयी = made of: काष्ठ (wood) + मयी = made of wood."),
            [("Without wood", "Without would need a prefix like निर्-; -मयी means made of."),
             ("Like wood", "Like would be काष्ठवत्; -मयी means made of."),
             ("For wood", "For would be the dative काष्ठाय; -मयी means made of.")],
            "काष्ठमयी = made of wood, like प्रतिच्छायमयी = made of reflection.",
            "-मय / -मयी = made of.",
            teaches="The suffix -मय (feminine -मयी) means 'made of, consisting of': प्रतिच्छायमयी = made of reflection."),
    ],
}

# ---------------------------------------------------------------- unit 17
AUTHORED["17"] = {
    "title": "यस्यातपदर्शादिष्वकस्मात्प्रतिच्छाया",
    "question": "By card 17, in what ways may a person's reflection suddenly be seen changed?",
    "rule": ("He whose reflection (प्रतिच्छाया) in sunlight and the like is suddenly (अकस्मात्) seen cut, split, deficient, "
             "in excess, confused, lost, with head downward, headless, two-headed, spread out, otherwise or distorted."),
    "limits": ("Medium confidence. ādarśa (mirror) and jihmā (crooked) are conjectures for printed आतपदर्श- and जिह्या: no "
               "question on either. No main clause here; the data's notes suggest cards 17 to 21 form one series that ends with स "
               "गतायुः (card 21)."),
    "explain_hi": ("जिसकी प्रतिच्छाया धूप आदि में अचानक (अकस्मात्) कटी, फटी, हीन, अधिक, व्याकुल, नष्ट, नीचे सिर वाली, सिरहीन, दो सिर वाली, फैली हुई, "
                   "अन्य प्रकार की या विकृत दिखाई दे। "
                   "‘आदर्श’ (दर्पण) और ‘जिह्मा’ (टेढ़ी) अनुमानित पाठ हैं (छपा ‘आतपदर्श’ और ‘जिह्या’), इसलिए उन पर प्रश्न नहीं। "
                   "इस इकाई में मुख्य वाक्य नहीं है; डेटा के नोट्स के अनुसार कार्ड १७ से २१ सम्भवतः एक ही शृंखला हैं, जिसका मुख्य वाक्य ‘स गतायुः’ कार्ड २१ में है। "
                   "‘-आदिष्वकस्मात्’ में -आदिषु + अकस्मात् की सन्धि है (उ + अ → व)।"),
    "hook": "प्रतिच्छाया अचानक कटी, बिना सिर या दो सिर की दिखे: शृंखला का एक लक्षण।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In card 17, what does अकस्मात् mean?",
            ("Suddenly", "अकस्मात् = suddenly, without a cause seen."),
            [("Slowly", "Slowly would be शनैः; अकस्मात् = suddenly."),
             ("Always", "Always would be सदा; अकस्मात् = suddenly."),
             ("Gradually", "Gradually would be क्रमशः; अकस्मात् = suddenly.")],
            "अकस्मात् = suddenly.",
            "अकस्मात् = suddenly."),
        order(1, "Put these sure words of card 17 in the printed order.",
              ["छिन्ना", "भिन्ना", "नष्टा", "विशिरा", "द्विशिरा", "विकृता"],
              "Cut, split, lost, headless, two-headed, distorted: six of the printed list, in order.",
              "छिन्ना → भिन्ना → नष्टा → विशिरा → द्विशिरा → विकृता."),
        match(2, "Match each word of card 17 to its meaning.",
              [["छिन्ना", "cut"], ["भिन्ना", "split"], ["नष्टा", "lost"], ["अवाक्शिरा", "with head downward"],
               ["विशिरा", "headless"], ["द्विशिरा", "two-headed"]],
              "छिन्ना = cut, भिन्ना = split, नष्टा = lost, अवाक्शिरा = head downward, विशिरा = headless, द्विशिरा = two-headed.",
              "छिन्ना, भिन्ना, नष्टा, अवाक्शिरा, विशिरा, द्विशिरा.", role="extend",
              teaches="विशिरा, द्विशिरा, अवाक्शिरा are bahuvrīhis ending in शिरस् (head), feminine to agree with प्रतिच्छाया."),
        mcq("discriminate", 3, "Which split of -आदिष्वकस्मात् in card 17 is right?",
            ("-आदिषु + अकस्मात्", "उ before a different vowel → व्: -आदिषु + अकस्मात् → -आदिष्वकस्मात्."),
            [("-आदिष्व + कस्मात्", "-आदिष्व is not a form; the व् comes from the उ of -आदिषु."),
             ("-आदिषु + कस्मात्", "With कस्मात् no join happens: it would print -आदिषु कस्मात्."),
             ("-आदिषः + अकस्मात्", "-आदिषः is not the locative plural; that is -आदिषु.")],
            "-आदिषु (in ... and the like) + अकस्मात् (suddenly): उ + अ → व.",
            "उ + unlike vowel → व्."),
        mcq("apply", 4, "A person's reflection in sunlight suddenly looks headless. Which word of card 17 names this?",
            ("विशिरा", "वि-शिरा = without a head: headless."),
            [("द्विशिरा", "द्वि-शिरा = two-headed, not headless."),
             ("अवाक्शिरा", "अवाक्-शिरा = with head downward, not headless."),
             ("विस्तृता", "विस्तृता = spread out; it names no head.")],
            "वि- (without) + शिरस् (head) = विशिरा.",
            "विशिरा = headless."),
        mcq("transfer", 5, "By the pattern of द्विशिरा (two-headed), what does त्रिशिरा mean in a new example?",
            ("Three-headed", "त्रि (three) + शिरा (head), a bahuvrīhi: having three heads."),
            [("Headless", "Headless is विशिरा; त्रि means three."),
             ("Head-down", "Head downward is अवाक्शिरा; त्रि means three."),
             ("Split-headed", "Split would be भिन्न; त्रि means three.")],
            "त्रिशिरा = three-headed, like द्विशिरा = two-headed.",
            "Number + शिरस् as bahuvrīhi = having that many heads.",
            teaches="A numeral + शिरस् (head) forms a bahuvrīhi: द्विशिरा = having two heads."),
    ],
}

# ---------------------------------------------------------------- unit 18
AUTHORED["18"] = {
    "title": "यस्य ललाटं न स्विद्यति",
    "question": "By card 18, what is said of the forehead?",
    "rule": "He whose forehead (ललाटम्) does not sweat (न स्विद्यति).",
    "limits": ("Prose, one relative clause; the main clause is not in this card. The data's notes (cards 20, 21) suggest it belongs to the series "
               "of cards 17 to 21 that ends with स गतायुः (card 21). Nothing says when or how long."),
    "explain_hi": ("जिसका ललाट (माथा) पसीजता नहीं। "
                   "यह केवल ‘यस्य’ वाला उपवाक्य है; मुख्य वाक्य यहाँ नहीं, डेटा के अनुसार यह सम्भवतः कार्ड १७ से २१ की शृंखला का भाग है। "
                   "‘स्विद्यति’ √स्विद् का वर्तमान, कर्तृवाच्य रूप है (पसीजता है); -यति होने से यह कर्मवाच्य नहीं हो जाता। "
                   "‘ललाटं न’ में ललाटम् का म् व्यंजन न से पहले अनुस्वार लिखा गया।"),
    "hook": "माथे पर पसीना न आए: शृंखला का एक लक्षण।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 18, what does ललाट mean?",
            ("Forehead", "ललाट = forehead."),
            [("Chin", "Chin would be चिबुक; ललाट = forehead."),
             ("Neck", "Neck would be ग्रीवा; ललाट = forehead."),
             ("Shoulder", "Shoulder would be अंस; ललाट = forehead.")],
            "ललाट = forehead.",
            "ललाट = forehead."),
        match(1, "Match each word of card 18 to its meaning.",
              [["यस्य", "whose"], ["ललाटम्", "forehead"], ["न", "not"], ["स्विद्यति", "sweats"]],
              "यस्य = whose, ललाटम् = forehead, न = not, स्विद्यति = sweats.",
              "यस्य, ललाटम्, न, स्विद्यति."),
        fill(2, "The verb meaning 'sweats' in card 18 is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("स्विद्यति", "svidyati"),
             "स्विद्यति = sweats (√स्विद्, present, third person singular).",
             "स्विद्यति is the present of √स्विद् (to sweat); with न it means 'does not sweat'.",
             "स्विद्यति = sweats."),
        mcq("discriminate", 3, "Is स्विद्यति in card 18 a passive form?",
            ("No: active present, he sweats", "√स्विद् takes -य- in its present; स्विद्यति is active (the passive would end in -यते)."),
            [("Yes: any verb with -य- is passive", "Not any: verbs like √स्विद् have -य- in the active present."),
             ("No: it is an optative form", "The optative would be स्विद्येत्; स्विद्यति is present."),
             ("No: it is a future form", "The future would have -इष्य- or -स्य-; स्विद्यति is present.")],
            "स्विद्यति: active present, third person singular.",
            "-यति is not a passive mark; the passive ends in -यते."),
        mcq("apply", 4, "Why is ललाटम् printed ललाटं before न in card 18?",
            ("म् before a consonant is written ं", "Final म् before a consonant in a sentence is written as anusvāra: ललाटं न."),
            [("म् before a vowel is written ं", "Before a vowel म् stays and joins (पिण्डमास्यस्थं, card 26)."),
             ("ं is the neuter's own ending", "The ending is म्; ं appears only before a consonant."),
             ("म् before any letter is dropped", "It is not dropped; it is written as ं.")],
            "ललाटम् + न → ललाटं न.",
            "Final म् + consonant → ं."),
        mcq("transfer", 5, "By the pattern of ललाटं न, how is जलम् + पिबति (he drinks water) written in a new example?",
            ("जलं पिबति", "Final म् before the consonant प is written ं: जलं पिबति."),
            [("जलो पिबति", "ओ comes from अः before a voiced consonant, not from म्."),
             ("जलः पिबति", "The accusative ends in म्; it never turns into a visarga."),
             ("जला पिबति", "म् is not dropped with a long आ; it becomes ं.")],
            "जलम् + पिबति = जलं पिबति, like ललाटम् + न = ललाटं न.",
            "Final म् + consonant → ं.",
            teaches="Inside a sentence a final म् before a consonant is written as anusvāra: ललाटम् + न → ललाटं न."),
    ],
}

# ---------------------------------------------------------------- unit 19
AUTHORED["19"] = {
    "title": "यस्य केशलोमान्यनभ्यक्तानि",
    "question": "By card 19, how do the hair of the head and body look?",
    "rule": ("He whose head-hair and body-hair (केशलोमानि), though unanointed (अनभ्यक्तानि), are seen as if anointed "
             "(अभ्यक्तवत् दृश्यन्ते)."),
    "limits": ("Prose, one relative clause; the main clause is not here (the data's notes suggest a series of cards 17 to 21). "
               "अभ्यक्त = anointed with oil or ointment; the line does not say which."),
    "explain_hi": ("जिसके सिर के केश और शरीर के रोम तेल न लगे होने पर भी तेल लगे हुए जैसे दिखाई दें। "
                   "अभ्यक्त = तेल या लेप लगा हुआ; कौन-सा, यह पंक्ति नहीं कहती। "
                   "मुख्य वाक्य यहाँ नहीं; डेटा के अनुसार यह सम्भवतः कार्ड १७ से २१ की शृंखला का भाग है। "
                   "छपाई में ‘यस्य’ के बाद रिक्त स्थान छूटा है। सन्धियाँ: लोमानि + अनभ्यक्तानि (इ + अ → य), अभ्यक्तवत् + दृश्यन्ते (त् + द → द्द)।"),
    "hook": "बिना तेल के भी बाल तेल लगे जैसे दिखें।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 19, what does अभ्यक्त mean?",
            ("Anointed with oil", "अभ्यक्त = anointed, with oil or ointment."),
            [("Washed with water", "Washing would be from √क्षल् or √स्ना; अभ्यक्त = anointed."),
             ("Cut very short", "Cutting would be छिन्न; अभ्यक्त = anointed."),
             ("Turned pure white", "White would be शुक्ल or सित; अभ्यक्त = anointed.")],
            "अभ्यक्त = anointed.",
            "अभ्यक्त = anointed."),
        order(1, "Put the words of card 19 in the printed order.",
              ["यस्य", "केशलोमानि", "अनभ्यक्तानि", "अभ्यक्तवत्", "दृश्यन्ते"],
              "Whose; head-hair and body-hair; unanointed; as if anointed; are seen.",
              "यस्य → केशलोमानि → अनभ्यक्तानि → अभ्यक्तवत् → दृश्यन्ते."),
        match(2, "Match each word of card 19 to its meaning.",
              [["केश", "head-hair"], ["लोमन्", "body-hair"], ["अनभ्यक्त", "unanointed"], ["-वत्", "like, as if"],
               ["दृश्यन्ते", "are seen"]],
              "केश = head-hair, लोमन् = body-hair, अनभ्यक्त = unanointed, -वत् = like, दृश्यन्ते = are seen.",
              "केश, लोमन्, अनभ्यक्त, -वत्, दृश्यन्ते.", role="extend",
              teaches="अन्- before a vowel negates: अन् + अभ्यक्त = not anointed."),
        mcq("discriminate", 3, "Which split of लोमान्यनभ्यक्तान्यभ्यक्तवद् in card 19 is right?",
            ("लोमानि + अनभ्यक्तानि + अभ्यक्तवत्", "इ + अ → य twice; त् before the voiced द → द्."),
            [("लोमानि + अभ्यक्तानि + अभ्यक्तवत्", "That would print लोमान्यभ्यक्तानि, without the न of अन्-."),
             ("लोमान्य + अनभ्यक्तान्य + अभ्यक्तवत्", "लोमान्य is not a form; the य् comes from the इ of लोमानि."),
             ("लोमा + अन्यनभ्यक्तानि + अभ्यक्तवत्", "अन्यनभ्यक्तानि is not a word; लोमानि ends in इ.")],
            "लोमानि (body-hairs) + अनभ्यक्तानि (unanointed) + अभ्यक्तवत् (as if anointed).",
            "इ + अ → य; त् + द → द्द."),
        mcq("apply", 4, "Why is अभ्यक्तवत् printed अभ्यक्तवद् before दृश्यन्ते in card 19?",
            ("त् before the voiced द → द्", "द is voiced: अभ्यक्तवत् + दृश्यन्ते → अभ्यक्तवद्दृश्यन्ते."),
            [("त् before any consonant → द्", "Not any: before प it stays त् (अकस्मात्प्रतिच्छाया, card 17)."),
             ("द् is the suffix's own form", "The suffix is -वत्; द् comes only from sandhi."),
             ("दृ begins with a vowel", "दृ begins with the consonant द, not a vowel.")],
            "-वत् + द- → -वद्द-.",
            "त् + voiced consonant → द्."),
        mcq("transfer", 5, "By the pattern of अभ्यक्तवत् (as if anointed), what does सिंहवत् mean in a new example?",
            ("Like a lion", "-वत् = like: सिंह (lion) + वत् = like a lion."),
            [("Without a lion", "Without would need a prefix like निर्-; -वत् means like."),
             ("Of the lion", "Of the lion would be the genitive सिंहस्य."),
             ("For the lion", "For the lion would be the dative सिंहाय.")],
            "सिंहवत् = like a lion, like अभ्यक्तवत् = like anointed ones.",
            "-वत् (comparison) = like, as if.",
            teaches="-वत् added to a noun can mean 'like': अभ्यक्तवत् = as if anointed."),
    ],
}

# ---------------------------------------------------------------- unit 20
AUTHORED["20"] = {
    "title": "नयने चातिप्रविष्टे",
    "question": "By card 20, which changes of the two eyes are listed, and which ones form opposite pairs?",
    "rule": ("The two eyes (नयने) sunk in too deep or protruding, widened or contracted, with contracted or bent brows, uneven (विषमे), "
             "with ceased or deficient sight, like a mongoose or a pigeon, of firebrand colour or of abnormal colour (blue and the like), very unsteady, stiff and drooping (a reading), "
             "discharging, too open, too shut, or with lost lashes."),
    "limits": ("Medium confidence. Printed जिह्वे is read jihme (crooked), a conjecture: no question on it. विश्रान्त is "
               "kept as printed (alt. vibhrānta). स्तब्धस्रस्ते as 'stiff and drooping' is a reading: no "
               "question. Nakula = mongoose (standard). No verb; appears to belong to the series of cards 17-21."),
    "explain_hi": ("दोनों आँखें (नयने, नपुंसक द्विवचन) बहुत भीतर धँसी या बाहर निकली, फैली या सिकुड़ी, सिकुड़ी या झुकी भौंहों वाली, ऊँची-नीची (विषमे), रुकी या क्षीण दृष्टि वाली, "
                   "नकुल (नेवला, मानक) या कपोत (कबूतर) जैसी, जलती लकड़ी के रंग की या नील आदि विकृत रंग की, बहुत चंचल, बहती हुई, बहुत खुली, बहुत मिची, या झड़ी पलकों वाली। "
                   "छपा ‘जिह्वे’ (दो जीभें) यहाँ नहीं बैठता; ‘जिह्मे’ (टेढ़ी) अनुमानित पाठ है, इस पर प्रश्न नहीं। "
                   "‘स्तब्धस्रस्ते’ का ‘कड़ी और ढीली’ अर्थ एक व्याख्या है। "
                   "इस इकाई में न ‘यस्य’ है न क्रिया; डेटा के अनुसार यह सम्भवतः कार्ड १८-१९ के बाद की शृंखला है, जो कार्ड २१ में पूरी होती है।"),
    "hook": "धँसी या उभरी, फैली या सिकुड़ी, बहुत खुली या बहुत मिची: आँखों के उलटे जोड़े।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In card 20, what does नयने mean?",
            ("The two eyes", "नयने = the two eyes: नयन (eye), neuter, nominative dual."),
            [("The two ears", "Ears would be कर्णौ; नयन = eye."),
             ("The two brows", "Brows are भ्रू, in -भ्रुणी; नयन = eye."),
             ("The two lips", "Lips would be ओष्ठौ; नयन = eye.")],
            "नयने = the two eyes.",
            "नयन = eye; -ए = neuter dual."),
        order(1, "Put the first four eye changes of card 20 in the printed order.",
              ["अतिप्रविष्टे", "निर्गते", "विस्तृते", "संक्षिप्ते"],
              "Sunk in too deep, protruding, widened, contracted: two opposite pairs, in order.",
              "अतिप्रविष्टे → निर्गते → विस्तृते → संक्षिप्ते."),
        match(2, "Match each word of card 20 to its meaning.",
              [["नकुलाभे", "like a mongoose"], ["कपोताभे", "like a pigeon"], ["अलातवर्णे", "of firebrand colour"],
               ["प्रस्रुते", "discharging"], ["लुप्तपक्ष्मणी", "with lost eyelashes"]],
              "नकुल (mongoose, standard) + आभ; कपोत (pigeon) + आभ; अलात (firebrand) + वर्ण; प्रस्रुत = discharging; लुप्त-पक्ष्मन् = lost lashes.",
              "नकुलाभे, कपोताभे, अलातवर्णे, प्रस्रुते, लुप्तपक्ष्मणी.", role="extend",
              teaches="-आभ at the end of a compound means 'resembling': नकुलाभ = resembling a mongoose."),
        mcq("discriminate", 3, "Which split of अत्युन्मिषिते in card 20 is right?",
            ("अति + उन्मिषिते", "इ before a different vowel → य्: अति + उन्मिषिते → अत्युन्मिषिते."),
            [("अत्य + उन्मिषिते", "अ + उ would give ओ: that would print अत्योन्मिषिते."),
             ("अति + युन्मिषिते", "युन्मिषिते is not a word; the य् comes from the इ of अति."),
             ("अत्यु + न्मिषिते", "न्मिषिते is not a word; उन्मिषिते (opened) is.")],
            "अति (excessively) + उन्मिषिते (opened): इ + उ → यु.",
            "इ + unlike vowel → य्."),
        mcq("apply", 4, "A patient's two eyes have sunk in far too deep. Which word of card 20 names this?",
            ("अतिप्रविष्टे", "अति-प्रविष्टे = entered too far in: sunk too deep."),
            [("निर्गते", "निर्गते = protruding, the opposite of sunk in."),
             ("विस्तृते", "विस्तृते = widened; it says nothing of sinking."),
             ("अतिचले", "अतिचले = very unsteady; it says nothing of sinking.")],
            "अति (too much) + प्रविष्ट (entered in) = sunk too deep.",
            "अतिप्रविष्टे ⇄ निर्गते."),
        mcq("transfer", 5, "By the pattern of नयने (the two eyes, neuter dual), what is the nominative dual of नेत्र (eye, neuter) in a new example?",
            ("नेत्रे", "Neuter अ-stems take -ए in the nominative dual: नेत्र → नेत्रे, like नयन → नयने."),
            [("नेत्रौ", "-औ is the masculine dual; नेत्र is neuter."),
             ("नेत्राणि", "-आणि is the neuter plural, not the dual."),
             ("नेत्रम्", "-म् is the singular, not the dual.")],
            "नेत्रे = the two eyes, like नयने.",
            "Neuter अ-stem, nominative dual → -ए.",
            teaches="Neuter अ-stems form the nominative dual in -ए: नयन → नयने; the adjectives agree (अतिप्रविष्टे)."),
    ],
}

# ---------------------------------------------------------------- unit 21
AUTHORED["21"] = {
    "title": "नासिका वाऽतिविवृता",
    "question": "By card 21, which changes of the nose are listed, and what is said of such a person?",
    "rule": ("Or the nose (नासिका) too wide open, too closed, crooked, cracked, covered with small boils (पिटिकाचिता) or "
             "dry: he is gatāyu (स गतायुः), one whose life-span has gone."),
    "limits": ("Prose, high confidence. स गतायुः is the only main clause; the data's notes suggest it closes the series of "
               "cards 17 to 21, but the line itself names only the nose. piṭikā = small boil or pustule (data); no "
               "cause, time or treatment is given."),
    "explain_hi": ("या नाक बहुत खुली, बहुत बन्द, टेढ़ी, फटी, पिटिका (छोटी फुंसियों) से ढकी या सूखी हो: वह गतायु है, यानी जिसकी आयु जा चुकी। "
                   "डेटा के अनुसार ‘स गतायुः’ सम्भवतः कार्ड १७ से २१ की पूरी शृंखला का मुख्य वाक्य है। "
                   "गतायु = गत (गई हुई) + आयु: बहुव्रीहि, कार्ड १६ के ‘परासु’ जैसा। "
                   "‘वा ऽतिविवृता’ में वा + अति है; ऽ छपाई की आदत है।"),
    "hook": "नाक बहुत खुली या बहुत बन्द, फटी या सूखी: स गतायुः।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In card 21, what does गतायुः mean?",
            ("One whose life-span has gone", "गत (gone) + आयुस् (life-span): one whose life-span has gone."),
            [("One whose health has returned", "गत means gone, not returned."),
             ("One who has gone on a journey", "आयुस् is life-span, not a journey."),
             ("One who will live a long time", "गत means gone; the life-span is gone, not long.")],
            "गतायुः = one whose life-span has gone.",
            "गत + आयुः = गतायुः."),
        order(1, "Put the nose changes of card 21 in the printed order.",
              ["अतिविवृता", "अतिसंवृता", "कुटिला", "स्फुटिता", "पिटिकाचिता", "शुष्का"],
              "Too wide open, too closed, crooked, cracked, covered with small boils, dry.",
              "अतिविवृता → अतिसंवृता → कुटिला → स्फुटिता → पिटिकाचिता → शुष्का."),
        match(2, "Match each word of card 21 to its meaning.",
              [["अतिविवृता", "too wide open"], ["अतिसंवृता", "too closed"], ["कुटिला", "crooked"],
               ["स्फुटिता", "cracked"], ["शुष्का", "dry"]],
              "अति-विवृता = too open, अति-संवृता = too closed, कुटिला = crooked, स्फुटिता = cracked, शुष्का = dry.",
              "अतिविवृता, अतिसंवृता, कुटिला, स्फुटिता, शुष्का.", role="extend",
              teaches="वि-वृत (opened) and सं-वृत (closed) share √वृ; the prefixes वि- and सं- give opposite senses."),
        mcq("discriminate", 3, "Which split of गतायुः in card 21 is right?",
            ("गत + आयुः", "अ + आ → आ: गत + आयुः → गतायुः."),
            [("गतः + आयुः", "अः before आ gives अ with a gap: it would print गत आयुः."),
             ("गती + आयुः", "ई before आ gives या: it would print गत्यायुः."),
             ("गत + यायुः", "यायुः is not a word; आयुः (life-span) is.")],
            "गत (gone) + आयुः (life-span).",
            "अ + आ → आ."),
        mcq("apply", 4, "A patient's nose is covered with small boils. Which word of card 21 names this?",
            ("पिटिकाचिता", "पिटिका (small boil) + आचिता (covered): covered with small boils."),
            [("स्फुटिता", "स्फुटिता = cracked, not covered with boils."),
             ("कुटिला", "कुटिला = crooked, not covered with boils."),
             ("अतिसंवृता", "अतिसंवृता = too closed, not covered with boils.")],
            "पिटिका + आचिता → पिटिकाचिता (आ + आ → आ).",
            "पिटिकाचिता = covered with piṭikās."),
        mcq("transfer", 5, "By the pattern of गतायुः (one whose life-span has gone), what does गतभयः mean in a new example?",
            ("One whose fear has gone", "Bahuvrīhi: गत (gone) + भय (fear) = one whose fear has gone."),
            [("One whose fear has grown", "गत means gone, not grown."),
             ("One who brings fear to all", "Bringing fear would be भयंकर; गत means gone."),
             ("One who is full of great fear", "Full of fear would be भयपूर्ण; गत means gone.")],
            "गतभयः = one whose fear has gone, like गतायुः = one whose life-span has gone.",
            "गत + noun as bahuvrīhi = one whose ... has gone.",
            teaches="गत + a noun can form a bahuvrīhi describing a person: गतायुः = one whose life-span has gone."),
    ],
}

# ---------------------------------------------------------------- unit 22
AUTHORED["22"] = {
    "title": "यस्याधोऽधरोष्ठो याति",
    "question": "By card 22, which lip changes can be read with certainty, and which joins does the line show?",
    "rule": ("Sure words: whose (यस्य) lower lip (अधरोष्ठः) goes (याति) downward (अधः), and the upper lip (उत्तरोष्ठः); "
             "facing upward (ऊर्ध्वमुखौ); blue (नीलौ) like ripe jambū (Syzygium cumini, standard)."),
    "limits": ("Low confidence. How the words join is uncertain: whether याति governs both lips, and what ऊर्ध्वमुखौ and "
               "नीलौ describe (probably the two lips, unstated). No question on the construction; questions ask words "
               "and joins only."),
    "explain_hi": ("जिसका निचला होंठ (अधरोष्ठः) नीचे (अधः) जाता है (याति) और ऊपरी होंठ (उत्तरोष्ठः), या दोनों ऊपर की ओर मुख वाले (ऊर्ध्वमुखौ), "
                   "या पके जामुन (जम्बू, Syzygium cumini, मानक) जैसे नीले (नीलौ)। "
                   "वाक्य-रचना अनिश्चित है: ‘याति’ दोनों होंठों पर लगता है या नहीं, और द्विवचन ‘ऊर्ध्वमुखौ’, ‘नीलौ’ किसके विशेषण हैं (सम्भवतः दोनों होंठ, जो छपे नहीं)। "
                   "इसलिए रचना पर कोई प्रश्न नहीं, केवल शब्द और सन्धियाँ। "
                   "सन्धियाँ: अधः + अधरोष्ठः → अधोऽधरोष्ठः (अः + अ → ओऽ), अधरोष्ठः + याति → अधरोष्ठो याति (अः + घोष व्यंजन → ओ)।"),
    "hook": "अधरोष्ठ नीचे जाए; ऊर्ध्वमुखौ, जामुन जैसे नीलौ: रचना अनिश्चित।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 22, what does ओष्ठ mean?",
            ("Lip", "ओष्ठ = lip: अधर-ओष्ठ lower lip, उत्तर-ओष्ठ upper lip."),
            [("Tooth", "Tooth is दन्त (card 23); ओष्ठ = lip."),
             ("Cheek", "Cheek is गण्ड (card 25); ओष्ठ = lip."),
             ("Chin", "Chin would be चिबुक; ओष्ठ = lip.")],
            "ओष्ठ = lip.",
            "ओष्ठ = lip."),
        order(1, "Put the first words of card 22 in the printed order.",
              ["यस्य", "अधः", "अधरोष्ठः", "याति", "उत्तरोष्ठः", "च"],
              "Whose; downward; the lower lip; goes; the upper lip; and.",
              "यस्य → अधः → अधरोष्ठः → याति → उत्तरोष्ठः → च."),
        match(2, "Match each word of card 22 to its meaning.",
              [["अधरोष्ठ", "lower lip"], ["उत्तरोष्ठ", "upper lip"], ["ऊर्ध्वमुख", "facing upward"], ["पक्व", "ripe"],
               ["नील", "blue"]],
              "अधर-ओष्ठ = lower lip, उत्तर-ओष्ठ = upper lip, ऊर्ध्व-मुख = facing upward, पक्व = ripe, नील = blue.",
              "अधरोष्ठ, उत्तरोष्ठ, ऊर्ध्वमुख, पक्व, नील.", role="extend",
              teaches="अधर (lower) and उत्तर (upper) form a pair of opposites before ओष्ठ."),
        mcq("discriminate", 3, "Which split of अधोऽधरोष्ठो in card 22 is right?",
            ("अधः + अधरोष्ठः", "अः + अ → ओऽ: अधः + अधरोष्ठः → अधोऽधरोष्ठः."),
            [("अधः + धरोष्ठः", "No अ would be dropped then: it would print अधोधरोष्ठः, without ऽ."),
             ("अधः + उधरोष्ठः", "उधरोष्ठः is not a word, and अः before उ would print अध उ-, not अधोऽ."),
             ("अध + ऽधरोष्ठः", "अध is not a word; the adverb is अधः (downward).")],
            "अधः (downward) + अधरोष्ठः (lower lip): अः + अ → ओऽ.",
            "अः + अ → ओऽ."),
        mcq("apply", 4, "Why is अधरोष्ठः printed अधरोष्ठो before याति in card 22?",
            ("अः before a voiced consonant → ओ", "य is a voiced consonant: अधरोष्ठः + याति → अधरोष्ठो याति."),
            [("आः before a voiced consonant → ओ", "आः drops its visarga before a voiced sound; and the ending here is अः."),
             ("ः before any consonant → ओ", "Not any: before च it becomes श् (उत्तरोष्ठश्च, same card)."),
             ("ओ is the nominative's own ending", "The nominative is अधरोष्ठः; ओ comes only from sandhi.")],
            "अधरोष्ठः + याति: अः before the voiced consonant य → ओ.",
            "अः + voiced consonant → ओ."),
        mcq("transfer", 5, "By the pattern of अधरोष्ठो याति, how is रामः + याति (Rāma goes) joined in a new example?",
            ("रामो याति", "अः before the voiced consonant य → ओ: रामो याति."),
            [("राम याति", "Dropping the visarga before a consonant is for सः and एषः, not for रामः."),
             ("रामर्याति", "र् comes from a visarga after a vowel other than अ/आ; here it follows अ."),
             ("रामश्याति", "श् comes from a visarga before च, छ or श, not before य.")],
            "रामः + याति = रामो याति, like अधरोष्ठः + याति = अधरोष्ठो याति.",
            "अः + voiced consonant → ओ.",
            teaches="अः before a voiced consonant becomes ओ: अधरोष्ठः + याति → अधरोष्ठो याति."),
    ],
}

# ---------------------------------------------------------------- unit 23
AUTHORED["23"] = {
    "title": "दंता वाऽतिरूक्षास्ताम्राः",
    "question": "By card 23, which changes of the teeth are listed, and what may happen to them suddenly?",
    "rule": ("Or the teeth (दन्ताः) very dry, copper-coloured, dusky, muddy, flowered (पुष्पिताः), with grit (सशर्कराः), "
             "or they suddenly (सहसा) fall out (पतन्ति)."),
    "limits": ("Medium confidence. पुष्पित (flowered) is kept literal; its sense is not stated. शर्करा = grit (tartar is "
               "possible, not stated): no question on either sense. The first half has no verb; पतन्ति belongs to the last "
               "alternative only."),
    "explain_hi": ("या दाँत बहुत रूखे, ताम्र (ताँबे के रंग के), श्याम, कीचड़ वाले, पुष्पित, शर्करा (कंकड़ी के कणों) वाले हों, या अचानक (सहसा) गिर जाएँ (पतन्ति)। "
                   "‘पुष्पित’ शब्दशः ‘फूलों वाले’ (पुष्पित) रखा गया, इसका अर्थ पंक्ति नहीं बताती; ‘शर्करा’ से टार्टर भी सम्भव है, पर कहा नहीं गया। "
                   "पहले भाग में क्रिया नहीं; ‘पतन्ति’ केवल अन्तिम विकल्प की क्रिया है। "
                   "सन्धियाँ: दन्ताः + वा → दन्ता वा (आः घोष से पहले विसर्ग खोता है), अतिरूक्षाः + ताम्राः → अतिरूक्षास्ताम्राः (त से पहले ः → स्)।"),
    "hook": "रूखे, ताम्र, श्याम दाँत, या अचानक गिरें।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 23, what does सहसा mean?",
            ("Suddenly", "सहसा = suddenly: सहसा वा पतन्ति, or they suddenly fall."),
            [("Slowly", "Slowly would be शनैः; सहसा = suddenly."),
             ("Partly", "Partly would be अंशतः; सहसा = suddenly."),
             ("Gradually", "Gradually would be क्रमशः; सहसा = suddenly.")],
            "सहसा = suddenly.",
            "सहसा = suddenly."),
        order(1, "Put these tooth changes of card 23 in the printed order.",
              ["अतिरूक्षाः", "ताम्राः", "श्यामाः", "पंकिलाः", "सशर्कराः"],
              "Very dry, copper-coloured, dusky, muddy, (flowered,) with grit.",
              "अतिरूक्षाः → ताम्राः → श्यामाः → पंकिलाः → सशर्कराः."),
        match(2, "Match each word of card 23 to its meaning.",
              [["अतिरूक्ष", "very dry"], ["ताम्र", "copper-coloured"], ["श्याम", "dusky"], ["पङ्किल", "muddy"],
               ["पतन्ति", "they fall"]],
              "अति-रूक्ष = very dry, ताम्र = copper-coloured, श्याम = dusky, पङ्किल = muddy, पतन्ति = they fall.",
              "अतिरूक्ष, ताम्र, श्याम, पङ्किल, पतन्ति.", role="extend",
              teaches="पङ्किल = पङ्क (mud) + -इल (having): muddy."),
        mcq("discriminate", 3, "Why is दन्ताः printed दन्ता (दंता) before वा in card 23?",
            ("आः drops its visarga before a voiced sound", "व is voiced: दन्ताः + वा → दन्ता वा."),
            [("अः before a voiced consonant → ओ", "That holds for अः; दन्ताः ends in आः, which drops the visarga."),
             ("ः before व always becomes स्", "स् arises before त or थ, not before व."),
             ("दन्ता is the dual form", "The dual would be दन्तौ; दन्ताः is plural.")],
            "दन्ताः + वा: आः before a voiced sound → आ.",
            "आः + voiced sound → आ."),
        mcq("apply", 4, "By card 23, what may happen suddenly (सहसा) to the teeth?",
            ("They fall out", "सहसा वा पतन्ति: or they suddenly fall out."),
            [("They turn white", "No whitening is named; the colours are copper and dusky."),
             ("They grow long", "Nothing in card 23 speaks of the teeth growing."),
             ("They start to bleed", "Nothing in card 23 speaks of the teeth bleeding.")],
            "पतन्ति = they fall: the last alternative.",
            "सहसा पतन्ति = suddenly fall out."),
        mcq("transfer", 5, "By the pattern of दन्ता वा, how is बालाः + गच्छन्ति (the boys go) joined in a new example?",
            ("बाला गच्छन्ति", "आः before the voiced ग drops its visarga: बाला गच्छन्ति."),
            [("बालो गच्छन्ति", "ओ comes from अः, not from आः."),
             ("बालार्गच्छन्ति", "र् comes after a vowel other than अ/आ; here it follows आ."),
             ("बालास्गच्छन्ति", "स् comes before त or थ, not before ग.")],
            "बालाः + गच्छन्ति = बाला गच्छन्ति, like दन्ताः + वा = दन्ता वा.",
            "आः + voiced sound → आ.",
            teaches="आः drops its visarga before a voiced sound: दन्ताः + वा → दन्ता वा."),
    ],
}

# ---------------------------------------------------------------- unit 24
AUTHORED["24"] = {
    "title": "जिह्वा वा जिह्मा",
    "question": "By card 24, which changes of the tongue are listed?",
    "rule": ("Or the tongue (जिह्वा) crooked (जिह्मा), stiff, on a conjectural reading numb, coated, heavy (गुर्वी), dark brown, swollen, dry, "
             "spreading (विसर्पिणी), or as if covered with thorns (कण्टकाचिता इव)."),
    "limits": ("Medium confidence. Printed स्तब्धासुप्ता could give a-suptā (not numb); suptā (numb) is a conjecture: no "
               "question on it. विसर्पिणी means spreading only; it is not read as the disease visarpa. No main clause."),
    "explain_hi": ("या जीभ (जिह्वा) टेढ़ी (जिह्मा), कड़ी, अनुमानित पाठ पर सुन्न, लिपी हुई, भारी (गुर्वी), श्याव, सूजी, सूखी, फैलने वाली, या मानो काँटों से ढकी हो। "
                   "छपा ‘स्तब्धासुप्ता’ से ‘असुप्ता’ (सुन्न नहीं) भी बन सकता है; ‘सुप्ता’ (सुन्न) अनुमानित पाठ है, इस पर प्रश्न नहीं। "
                   "‘विसर्पिणी’ का अर्थ केवल ‘फैलने वाली’ लिया गया, रोग ‘विसर्प’ नहीं। "
                   "‘गुर्वी’ गुरु का स्त्रीलिंग है, जिह्वा से मेल खाता है; ‘कण्टकाचितेव’ में कण्टकाचिता + इव (आ + इ → ए)।"),
    "hook": "जिह्वा जिह्मा: जीभ टेढ़ी, भारी, सूजी, काँटों जैसी।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 24, what does जिह्मा mean?",
            ("Crooked", "जिह्मा = crooked: जिह्वा वा जिह्मा, or the tongue crooked."),
            [("Tongue", "Tongue is जिह्वा, the noun; जिह्मा is its adjective, crooked."),
             ("Heavy", "Heavy is गुर्वी; जिह्मा = crooked."),
             ("Bitter-tasting", "Bitter would be तिक्ता; जिह्मा = crooked.")],
            "जिह्वा = tongue; जिह्मा = crooked.",
            "जिह्मा = crooked."),
        order(1, "Put these tongue changes of card 24 in the printed order.",
              ["गुर्वी", "श्यावा", "शूना", "शुष्का", "विसर्पिणी"],
              "Heavy, dark brown, swollen, dry, spreading.",
              "गुर्वी → श्यावा → शूना → शुष्का → विसर्पिणी."),
        match(2, "Match each word of card 24 to its meaning.",
              [["स्तब्धा", "stiff"], ["गुर्वी", "heavy"], ["शूना", "swollen"], ["शुष्का", "dry"],
               ["कण्टकाचिता", "covered with thorns"]],
              "स्तब्धा = stiff, गुर्वी = heavy, शूना = swollen, शुष्का = dry, कण्टक-आचिता = covered with thorns.",
              "स्तब्धा, गुर्वी, शूना, शुष्का, कण्टकाचिता.", role="extend",
              teaches="All adjectives are feminine singular, agreeing with जिह्वा."),
        mcq("discriminate", 3, "Which split of कण्टकाचितेव (कंटकाचितेव) in card 24 is right?",
            ("कण्टकाचिता + इव", "आ + इ → ए: कण्टकाचिता + इव → कण्टकाचितेव."),
            [("कण्टकाचिता + एव", "आ + ए gives ऐ: that would print कण्टकाचितैव."),
             ("कण्टकाचिते + इव", "ए before इ would give अय् or अ: not -तेव."),
             ("कण्टक + आचितेव", "आचितेव is not a word; the ए comes from आ + इ.")],
            "कण्टकाचिता (covered with thorns) + इव (as if): आ + इ → ए.",
            "आ + इ → ए."),
        mcq("apply", 4, "Why does card 24 print गुर्वी, not गुरुः, for heavy?",
            ("It is feminine, agreeing with जिह्वा", "गुरु forms the feminine गुर्वी; जिह्वा is feminine."),
            [("It is the dual form of गुरु", "The dual would be गुरू; गुर्वी is feminine singular."),
             ("It is the comparative degree", "The comparative would be गरीयस्; गुर्वी is the plain feminine."),
             ("It is the plural form of गुरु", "The plural would be गुरवः; गुर्वी is feminine singular.")],
            "गुरु (heavy) → feminine गुर्वी, agreeing with जिह्वा.",
            "Adjective agrees with its noun in gender."),
        mcq("transfer", 5, "By the pattern of कण्टकाचिता + इव → कण्टकाचितेव, how is माला + इव (like a garland) joined in a new example?",
            ("मालेव", "आ + इ → ए: माला + इव → मालेव."),
            [("मालैव", "ऐ comes from आ + ए; here the second vowel is इ."),
             ("मालीव", "ई comes from इ + इ; here the first vowel is आ."),
             ("माल्यिव", "य् comes from इ before a vowel; here the first vowel is आ.")],
            "माला + इव = मालेव, like कण्टकाचिता + इव = कण्टकाचितेव.",
            "आ + इ → ए.",
            teaches="अ or आ before इ or ई gives ए: कण्टकाचिता + इव → कण्टकाचितेव."),
    ],
}

# ---------------------------------------------------------------- unit 25
AUTHORED["25"] = {
    "title": "यस्य गंडेललाटहनुबंधनानि",
    "question": "By card 25, what is said of the attachments of the face, and which half of the line is uncertain?",
    "rule": ("He whose attachments (बन्धनानि) of cheek, forehead and jaw are slack (स्रस्तानि) as if fallen from their "
             "place (printed स्थानाच्चुतानीव, read स्थानात् च्युतानि इव; the य of च्युत is not printed); the second half, on a conjectural reading, says head, neck or back does not "
             "bear its own weight."),
    "limits": ("Low confidence. Second half conjectural (dhatte for printed धन्ते; cases of शिरोधरां, "
               "स्वभारं unclear): no question on its sense. गंडे- may be compound gaṇḍa- or locative "
               "gaṇḍe: no question on that. Printed स्थानाच्चुतानीव lacks the य of च्युतानि (unflagged): no question on that word or its joins."),
    "explain_hi": ("जिसके गाल, ललाट और हनु (जबड़े) के बन्धन मानो अपने स्थान से च्युत होकर ढीले (स्रस्तानि) हों। छपा ‘स्थानाच्चुतानीव’ है; च्युत का य नहीं छपा, इसलिए इस शब्द और इसकी सन्धि पर प्रश्न नहीं। "
                   "दूसरा भाग अनिश्चित है: छपा ‘धन्ते’ नियमित रूप नहीं, ‘धत्ते’ (धारण करता है) अनुमानित पाठ है; उस पर ‘सिर, गर्दन या पीठ अपना भार नहीं सहती’। "
                   "‘गंडे-’ समास का ‘गण्ड-’ है या सप्तमी ‘गण्डे’, यह भी निश्चित नहीं। इसलिए प्रश्न केवल पहले भाग के पक्के शब्दों और सन्धियों पर। "
                   "‘शिरोधरा’ (गर्दन) में शिरस् + धरा है (अस् घोष व्यंजन से पहले → ओ)।"),
    "hook": "चेहरे के बन्धन ढीले, मानो जगह से खिसक गए।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 25, what does स्रस्त mean?",
            ("Slack, loosened", "स्रस्त (from √स्रंस्) = slack, loosened."),
            [("Tight, firm", "That is the opposite of स्रस्त."),
             ("Swollen, raised", "Swollen would be शून or उत्सिक्त; स्रस्त = slack."),
             ("Burnt, scorched", "Burnt would be दग्ध; स्रस्त = slack.")],
            "स्रस्त = slack.",
            "स्रस्त = slack."),
        match(1, "Match each sure word of the first half of card 25 to its meaning.",
              [["यस्य", "whose"], ["ललाट", "forehead"], ["हनु", "jaw"], ["बन्धन", "attachment"], ["स्रस्त", "slack"]],
              "यस्य = whose, ललाट = forehead, हनु = jaw, बन्धन = attachment, स्रस्त = slack.",
              "यस्य, ललाट, हनु, बन्धन, स्रस्त."),
        order(2, "Put these sure printed parts of the first half of card 25 in the printed order.",
              ["यस्य", "ललाट", "हनु", "बंधनानि", "स्रस्तानि"],
              "Whose; forehead; jaw; attachments; slack (गंडे- before ललाट and स्थानाच्चुतानीव before स्रस्तानि are left out).",
              "यस्य → ललाट → हनु → बंधनानि → स्रस्तानि.",
              role="extend",
              teaches="In गंडेललाटहनुबंधनानि the body parts come first and बन्धनानि (attachments) last: the last member is the head of the compound."),
        mcq("discriminate", 3, "Which split of शिरोधरा (neck) in card 25 is right?",
            ("शिरस् + धरा", "अस् before the voiced consonant ध → ओ: शिरस् + धरा → शिरोधरा."),
            [("शिरा + धरा", "That would print शिराधरा; the print has शिरो-."),
             ("शिरः + उधरा", "उधरा is not a word; धरा (bearer) is."),
             ("शिर + ओधरा", "ओधरा is not a word; the ओ belongs to शिरस्.")],
            "शिरस् (head) + धरा (bearer): the head-bearer, the neck.",
            "अस् + voiced consonant → ओ."),
        mcq("apply", 4, "In card 25, what does the ending -आनि of स्रस्तानि show?",
            ("Neuter plural, as in बन्धनानि", "-आनि is the neuter plural ending: स्रस्तानि agrees with बन्धनानि (attachments)."),
            [("Feminine singular, as in नासिका", "The feminine singular would be स्रस्ता, like नासिका (card 21)."),
             ("Masculine plural, as in दन्ताः", "The masculine plural would be स्रस्ताः, like दन्ताः (card 23)."),
             ("Neuter dual, as in नयने", "The neuter dual would be स्रस्ते, like नयने (card 20).")],
            "स्रस्तानि (neuter plural) agrees with बन्धनानि.",
            "-आनि = neuter plural."),
        mcq("transfer", 5, "By the pattern of स्रस्तानि (neuter plural, agreeing with बन्धनानि), what is the nominative plural of वन (forest, neuter) in a new example?",
            ("वनानि", "Neuter अ-stems take -आनि in the nominative plural: वन → वनानि, like बन्धनानि."),
            [("वनाः", "-आः is the masculine plural; वन is neuter."),
             ("वने", "-ए is the neuter dual (two forests), not the plural."),
             ("वनम्", "-म् is the singular, not the plural.")],
            "वनानि = forests, like बन्धनानि = attachments.",
            "Neuter अ-stem, nominative plural → -आनि.",
            teaches="Neuter अ-stems form the nominative plural in -आनि and adjectives agree: बन्धनानि ... स्रस्तानि."),
    ],
}

# ---------------------------------------------------------------- unit 26
AUTHORED["26"] = {
    "title": "हनू वा पिंडमास्यस्थं",
    "question": "Which words does card 26 print, and what does it leave unsaid?",
    "rule": ("Or the two jaws (हनू), a lump (पिण्डम्) staying in the mouth (आस्यस्थम्). No verb is printed."),
    "limits": ("Low confidence, typed prose. Elliptical: a verb such as 'do not hold' may be carried over from card 25, "
               "but none is printed or supplied: no question on what the jaws do. Questions ask words and joins only."),
    "explain_hi": ("या दोनों हनु (जबड़े), मुख में स्थित पिण्ड (कौर)। "
                   "इस इकाई में क्रिया नहीं छपी; डेटा के अनुसार यह कार्ड २५ को आगे बढ़ाती है और कोई क्रिया (जैसे ‘नहीं थामते’) वहाँ से आ सकती है, पर अनुवाद कोई क्रिया नहीं जोड़ता। "
                   "इसलिए जबड़े क्या करते हैं, इस पर प्रश्न नहीं। "
                   "‘पिंडमास्यस्थं’ में पिण्डम् + आस्यस्थम् है: म् स्वर से पहले जुड़ जाता है।"),
    "hook": "हनू और मुँह में रखा कौर: क्रिया छपी नहीं।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 26, what does पिण्ड mean?",
            ("Lump, morsel", "पिण्ड = lump, morsel: पिण्डम् आस्यस्थम्, a lump in the mouth."),
            [("Tooth, fang", "Tooth is दन्त; पिण्ड = lump."),
             ("Breath, the air", "Breath would be श्वास; पिण्ड = lump."),
             ("Drop, drip", "Drop would be बिन्दु; पिण्ड = lump.")],
            "पिण्ड = lump.",
            "पिण्ड = lump, morsel."),
        match(1, "Match each word of card 26 to its meaning.",
              [["हनू", "the two jaws"], ["पिण्ड", "lump"], ["आस्य", "mouth"], ["-स्थ", "staying in"]],
              "हनू = the two jaws, पिण्ड = lump, आस्य = mouth, -स्थ = staying in.",
              "हनू, पिण्ड, आस्य, -स्थ."),
        T(multi("extend", 2, "Which statements fit card 26 as printed?",
                [("It prints no verb", "Right: no verb is printed or supplied."),
                 ("It says the jaws are swollen", "No: no quality of the jaws is printed."),
                 ("आस्यस्थम् means staying in the mouth", "Right: आस्य (mouth) + स्थ (staying)."),
                 ("It names a medicine for the mouth", "No: पिण्ड here is a lump staying in the mouth.")],
                [0, 2],
                "Three words and वा; no verb; आस्यस्थम् = staying in the mouth.",
                "हनू वा पिण्डम् आस्यस्थम्."),
          "An elliptical line may lean on the line before for its verb; the card says only what is printed."),
        mcq("discriminate", 3, "Which split of पिंडमास्यस्थं in card 26 is right?",
            ("पिण्डम् + आस्यस्थम्", "Final म् before a vowel joins it: पिण्डम् + आस्य- → पिण्डमास्य-."),
            [("पिण्ड + मास्यस्थम्", "मास्यस्थम् is not a word; the म् belongs to पिण्डम्."),
             ("पिण्डमा + स्यस्थम्", "Neither पिण्डमा nor स्यस्थम् is a word."),
             ("पिण्डम् + अस्यस्थम्", "That would print पिण्डमस्य-, with a short अ; the print has मा.")],
            "पिण्डम् (lump) + आस्यस्थम् (staying in the mouth).",
            "म् + vowel → joined."),
        mcq("apply", 4, "In आस्यस्थ of card 26, what does -स्थ add?",
            ("Staying, being in", "-स्थ (from √स्था) = standing, staying in: staying in the mouth."),
            [("Coming out of", "Coming out would be निःसृत; -स्थ means staying."),
             ("Made out of", "Made of would be -मय; -स्थ means staying."),
             ("Looking like", "Like would be -वत् or -आभ; -स्थ means staying.")],
            "आस्य (mouth) + स्थ (staying) = staying in the mouth.",
            "-स्थ = staying in."),
        mcq("transfer", 5, "By the pattern of आस्यस्थ (staying in the mouth), what does गृहस्थ mean in a new example?",
            ("One staying in the house", "-स्थ = staying in: गृह (house) + स्थ = one staying in the house."),
            [("One who leaves the house", "Leaving would need a word like त्यक्त; -स्थ means staying."),
             ("One who builds a house", "Building would be -कार or -कृत्; -स्थ means staying."),
             ("One who looks like a house", "Like would be -वत्; -स्थ means staying.")],
            "गृहस्थ = staying in the house, like आस्यस्थ = staying in the mouth.",
            "-स्थ = staying in.",
            teaches="-स्थ (from √स्था) at the end of a compound means 'staying in': आस्यस्थ = staying in the mouth."),
    ],
}

# ================================================================ NOTES_HI
NOTES_HI = {
    "14": ("गद्य; विश्वास उच्च; एक छपी पंक्ति (०२.०९.१७); कोई पाठ-चिह्न नहीं। अपूर्ण शीर्षक: ‘दोनों’ के नाम नहीं छपे, क्रिया भी नहीं। "
           "स्थान के आधार पर डेटा इन्हें छाया और प्रभा (कार्ड १५, छपी पंक्तियाँ १८-१९) मानता है, पर यह कहा नहीं गया। "
           "‘तयोः’ षष्ठी या सप्तमी द्विवचन दोनों हो सकता है; डेटा षष्ठी लेता है, इसलिए विभक्ति पर प्रश्न नहीं। "
           "सन्धि जाँची: तयोः + विशेषः → तयोर्विशेषः (ओ के बाद विसर्ग, घोष व से पहले → र्)।"),
    "15": ("गद्य; विश्वास मध्यम; दो छपी पंक्तियाँ (०२.०९.१८ और ०२.०९.१९) जोड़ी गईं। पाठ-चिह्न (सम्भव): छपा ‘चलच्यते’ कोई शब्द नहीं; "
           "दूसरी पंक्ति के ‘विप्रकृष्टा लक्ष्यते’ के आधार पर ‘च लक्ष्यते’ अनुमानित पाठ है (क्ष को च पढ़ा गया)। "
           "‘तेजःप्रभैव’ को ‘तेजः, प्रभा एव’ भी पढ़ा जा सकता है; समास वाला पाठ लिया गया। लम्बे शब्द में रिक्त स्थान छूटे हैं। "
           "सन्धि जाँची: वर्णम् + आक्रामति → वर्णमाक्रामति; आक्रामति + आसन्ना → आक्रामत्यासन्ना (इ + आ → या); प्रभा + एव → प्रभैव (आ + ए → ऐ)।"),
    "16": ("गद्य; विश्वास मध्यम; एक छपी पंक्ति (०२.०९.२०); कोई पाठ-चिह्न नहीं। ‘कुमारिका’ शब्दशः छोटी कन्या; पुतली में दिखने वाली आकृति "
           "होना सम्भावित (डेटा का लेबल) है। दृष्टि = आँख लिया गया। ‘सपरासुः’ एक शब्द-खण्ड में छपा: सः + परासुः (सः व्यंजन से पहले विसर्ग खोता है)। "
           "परासु = परा + असु (आ + अ → आ), बहुव्रीहि।"),
    "17": ("गद्य; विश्वास मध्यम; एक छपी पंक्ति (०२.०९.२१)। पाठ-चिह्न (सम्भव): छपा ‘आतपदर्शादिषु’ में एक आ कम है; ‘आतपादर्श’ (धूप, दर्पण) सुझाया गया, "
           "पर ‘आतप-दर्श-आदिषु’ (धूप देखने आदि में) भी सम्भव है। छपा ‘जिह्या’ कोई शब्द नहीं; ‘जिह्मा’ (टेढ़ी) अनुमानित पाठ है (कार्ड २४ में यही शब्द छपा)। "
           "दोनों पर प्रश्न नहीं। ‘हीनाऽधिकाऽऽकुला’ और ‘विस्तृताऽन्यथा’ में ऽ छपाई की आदत है (आ + अ → आ)। "
           "सन्धि जाँची: -आदिषु + अकस्मात् → -आदिष्वकस्मात् (उ + अ → व)। मुख्य वाक्य नहीं; डेटा के अनुसार शृंखला सम्भवतः कार्ड २१ में पूरी।"),
    "18": ("गद्य; विश्वास उच्च; एक छपी पंक्ति (०२.०९.२२); कोई पाठ-चिह्न नहीं। केवल ‘यस्य’ वाला उपवाक्य, मुख्य वाक्य इस इकाई में नहीं। "
           "‘स्विद्यति’ √स्विद् का वर्तमान, कर्तृवाच्य। सन्धि जाँची: ललाटम् + न → ललाटं न (व्यंजन से पहले म् → ं)।"),
    "19": ("गद्य; विश्वास उच्च; एक छपी पंक्ति (०२.०९.२३); कोई पाठ-चिह्न नहीं। ‘यस्य’ के बाद रिक्त स्थान छूटा है, पूरी पंक्ति एक खण्ड में छपी। "
           "अभ्यक्त = तेल या लेप लगा हुआ। छपा ‘दृश्यंते’ = दृश्यन्ते (अनुस्वार)। "
           "सन्धि जाँची: लोमानि + अनभ्यक्तानि → लोमान्यनभ्यक्तानि (इ + अ → य); अनभ्यक्तानि + अभ्यक्तवत् → -न्यभ्यक्तवत्; "
           "अभ्यक्तवत् + दृश्यन्ते → अभ्यक्तवद्दृश्यन्ते (घोष द से पहले त् → द्)।"),
    "20": ("गद्य; विश्वास मध्यम; एक छपी पंक्ति (०२.०९.२४)। पाठ-चिह्न (सम्भव): छपा ‘जिह्वे’ (दो जीभें) नेत्र-सूची में नहीं बैठता; नपुंसक द्विवचन ‘जिह्मे’ (टेढ़ी) "
           "अनुमानित पाठ है; इस पर प्रश्न नहीं। ‘विश्रान्त’ छपे रूप में रखा गया, ‘विभ्रान्त’ (भ्रमित) विकल्प है। ‘स्तब्धस्रस्ते’ को द्वन्द्व (कड़ी और ढीली) पढ़ा गया। "
           "नकुल = नेवला (मानक); ‘संक्षिप्तभ्रुणी’, ‘विनतभ्रुणी’ भ्रू का नियमित नपुंसक द्विवचन। कुछ शब्द रिक्त स्थान के बिना छपे (‘निर्गतेविस्तृते’, ‘लुप्तपक्ष्मणीवा’)। "
           "सन्धि जाँची: च + अति- → चाति- (अ + अ → आ); अति + उन्मिषिते → अत्युन्मिषिते (इ + उ → यु)। न ‘यस्य’ न क्रिया: डेटा के अनुसार शृंखला सम्भवतः कार्ड २१ में पूरी।"),
    "21": ("गद्य; विश्वास उच्च; एक छपी पंक्ति (०२.०९.२५); कोई पाठ-चिह्न नहीं। ‘स गतायुः’ इस शृंखला का एकमात्र मुख्य वाक्य है; डेटा के नोट्स के अनुसार कार्ड १७ से २१ सम्भवतः एक शृंखला हैं। "
           "आरम्भ का ‘वा ऽतिविवृता’ = वा + अति (ऽ छपाई की आदत)। पिटिका = छोटी फुंसी। "
           "सन्धि जाँची: गत + आयुः → गतायुः (अ + आ → आ); पिटिका + आचिता → पिटिकाचिता (आ + आ → आ); सः + गतायुः → स गतायुः (सः व्यंजन से पहले विसर्ग खोता है)।"),
    "22": ("गद्य; विश्वास कम; एक छपी पंक्ति (०२.०९.२६); कोई पाठ-चिह्न नहीं, पर वाक्य-रचना अनिश्चित: ‘याति’ दोनों होंठों पर लगे (निचला नीचे, ऊपरी ऊपर) या नहीं, "
           "और ‘ऊर्ध्वमुखौ’, ‘नीलौ’ अनकहे ‘दोनों होंठ’ के विशेषण हैं, यह डेटा की व्याख्या है। जम्बू (जामुन) = Syzygium cumini (मानक)। "
           "सन्धि जाँची: यस्य + अधः → यस्याधः; अधः + अधरोष्ठः → अधोऽधरोष्ठः (अः + अ → ओऽ); अधरोष्ठः + याति → अधरोष्ठो याति (अः + घोष व्यंजन → ओ); "
           "याति + उत्तर- → यात्युत्तर- (इ + उ → यु); उत्तरोष्ठः + च → उत्तरोष्ठश्च (च से पहले ः → श्); च + ऊर्ध्व- → चोर्ध्व- (अ + ऊ → ओ)। "
           "‘अधर + ओष्ठ’ में ओ और औ दोनों रूप मान्य हैं, इसलिए उस पर प्रश्न नहीं।"),
    "23": ("गद्य; विश्वास मध्यम; एक छपी पंक्ति (०२.०९.२७); कोई पाठ-चिह्न नहीं। ‘पुष्पित’ शब्दशः रखा गया, अर्थ नहीं बताया गया; ‘शर्करा’ = कंकड़ी/कण, टार्टर सम्भव पर कहा नहीं। "
           "पहले भाग में क्रिया नहीं; ‘पतन्ति’ अन्तिम विकल्प की। छपा ‘पंकिलाःपुष्पिताः’ बिना रिक्त स्थान। "
           "सन्धि जाँची: दन्ताः + वा → दन्ता वा (आः घोष से पहले विसर्ग खोता है); वा + अति- → वाऽति- (ऽ छपाई की आदत); "
           "अतिरूक्षाः + ताम्राः → अतिरूक्षास्ताम्राः (त से पहले ः → स्); सशर्कराः + वा → सशर्करा वा।"),
    "24": ("गद्य; विश्वास मध्यम; एक छपी पंक्ति (०२.०९.२८)। पाठ-चिह्न (सम्भव): छपा ‘स्तब्धासुप्ता’ से ‘स्तब्धा असुप्ता’ (सुन्न नहीं) बनता; दोषों की सूची में "
           "‘सुप्ता’ (सुन्न, रिक्त स्थान छूटा) अनुमानित पाठ है; इस पर प्रश्न नहीं। ‘विसर्पिणी’ = फैलने वाली, रोग विसर्प नहीं। "
           "सन्धि जाँची: कण्टकाचिता + इव → कण्टकाचितेव (आ + इ → ए); छपा ‘कंटकाचितेववा’ = कण्टकाचिता इव वा, बिना रिक्त स्थान।"),
    "25": ("गद्य; विश्वास कम; एक छपी पंक्ति (०२.०९.२९)। पाठ-चिह्न (सम्भव): छपा ‘धन्ते’ नियमित रूप नहीं, ‘धत्ते’ (धारण करता है) अनुमान; ‘शिरोधरां’ का ं "
           "छपाई की भूल या कर्म का चिह्न हो सकता है; ‘गंडे-’ समास का ‘गण्ड-’ या सप्तमी ‘गण्डे’। दूसरा भाग अनिश्चित: उस पर प्रश्न नहीं। "
           "‘यस्यन’ = यस्य न (रिक्त स्थान छूटा)। छपा ‘स्थानाच्चुतानीव’ में च्युतानि का य नहीं छपा; डेटा बिना चिह्न के ‘च्युतानि’ पढ़ता है। "
           "‘स्थानाच्चुतानीव’ और उसकी सन्धियों पर इसलिए प्रश्न नहीं। सन्धि जाँची: शिरस् + धरा → शिरोधरा "
           "(अस् + घोष व्यंजन → ओ)। डेटा के अनुसार कार्ड २६ (छपी पंक्ति ३०) वाक्य को आगे बढ़ाता है।"),
    "26": ("गद्य; विश्वास कम; एक छपी पंक्ति (०२.०९.३०); कोई पाठ-चिह्न नहीं। डेटा इसे गद्य मानता है; अपूर्ण: डेटा के अनुसार कार्ड २५ (छपी पंक्ति २९) से कोई "
           "क्रिया (जैसे ‘नहीं थामते’) आ सकती है, पर अनुवाद कोई क्रिया नहीं जोड़ता। हनू = दोनों जबड़े (डेटा: स्त्री. प्रथमा द्विवचन)। "
           "छपा ‘आस्यस्थं’ पंक्ति के अन्त में अनुस्वार के साथ = आस्यस्थम्। सन्धि जाँची: पिण्डम् + आस्यस्थम् → पिण्डमास्यस्थम् (म् स्वर से पहले जुड़ता है)।"),
}

# ================================================================ AIDS
AIDS = {
    "14": {
        "frame": "किनका: तयोः (दोनों का; नाम नहीं छपे) → क्या: विशेषः (भेद) → क्रिया: नहीं छपी।",
        "chunks": "तयोर्विशेषः",
        "sandhi": "ओ के बाद विसर्ग, घोष वर्ण से पहले → र्: तयोः + विशेषः → तयोर्विशेषः।",
    },
    "15": {
        "contrast": ("छाया: वर्ण पर छा जाती है, आसन्ना (समीप; ‘दिखती है’ अनुमानित पाठ), पाँच भूतों से बनी ⇄ प्रभा: वर्ण को प्रकाशित करती है, "
                     "दूर से दिखती है, तेजस् की प्रभा। दोनों इसी इकाई में।"),
        "chunks": "छाया | वर्णमाक्रामत्यासन्ना | चलच्यते | पंचभूतात्मिका च || प्रभा तु | वर्णं प्रकाशयति | विप्रकृष्टालक्ष्यते | तेजःप्रभैव च",
        "sandhi": ("म् + स्वर → जुड़ता है: वर्णम् + आक्रामति → वर्णमाक्रामति · इ + आ → या: आक्रामति + आसन्ना → आक्रामत्यासन्ना · "
                   "आ + ए → ऐ: प्रभा + एव → प्रभैव।"),
        "anchors": "छाया = पंचभूत, प्रभा = तेज। ढकना ⇄ चमकाना। (मेरी याद-पद्धति)",
    },
    "16": {
        "frame": "किसकी: यस्य → कहाँ: दृष्टौ (आँख में) → क्या: प्रतिच्छायमयी कुमारिका (सम्भवतः पुतली की आकृति) → न दृश्यते → फल: स परासुः।",
        "chunks": "यस्य दृष्टौ | प्रतिच्छायमयी कुमारिका | न दृश्यते | सपरासुः",
        "sandhi": "सः व्यंजन से पहले विसर्ग खोता है: सः + परासुः → स परासुः · आ + अ → आ: परा + असु → परासु।",
    },
    "17": {
        "diagram": {"groups": [
            {"label": "प्रतिच्छाया अचानक (छपे क्रम में)",
             "items": ["१ छिन्ना", "२ भिन्ना", "३ हीना", "४ अधिका", "५ आकुला", "६ नष्टा", "७ जिह्या (अनुमान: जिह्मा)",
                       "८ अवाक्शिरा", "९ विशिरा", "१० द्विशिरा", "११ विस्तृता", "१२ अन्यथा, विकृता"]}]},
        "chunks": ("यस्यातपदर्शादिष्वकस्मात्प्रतिच्छाया | छिन्ना भिन्ना | हीनाऽधिकाऽऽकुला नष्टा | जिह्याऽवाक्शिरा | विशिरा द्विशिरा | "
                   "विस्तृताऽन्यथा वा विकृता वा | दृश्यते"),
        "sandhi": "उ + भिन्न स्वर → व्: -आदिषु + अकस्मात् → -आदिष्वकस्मात् · आ + अ → आ: हीना + अधिका → हीनाधिका (छपाई में ऽ)।",
        "pegs": "सिर के तीन रूप: अवाक्-शिरा (उलटा), वि-शिरा (बिना), द्वि-शिरा (दो)। (मेरा बनाया स्मरण-सूत्र)",
    },
    "18": {
        "chunks": "यस्य | ललाटं | न स्विद्यति",
        "sandhi": "व्यंजन से पहले अन्तिम म् → ं: ललाटम् + न → ललाटं न।",
        "anchors": "स्विद्यति: -यति वाला कर्तृवाच्य वर्तमान; कर्मवाच्य होता तो -यते। (मेरी याद-पद्धति)",
    },
    "19": {
        "chain": {"steps": ["यस्य: जिसके", "केशलोमानि: केश और रोम", "अनभ्यक्तानि: तेल न लगे", "अभ्यक्तवत्: तेल लगे जैसे",
                            "दृश्यन्ते: दिखते हैं"]},
        "chunks": "यस्य | केशलोमान्यनभ्यक्तान्यभ्यक्तवद्दृश्यंते",
        "sandhi": "इ + अ → य: लोमानि + अनभ्यक्तानि → लोमान्यनभ्यक्तानि · घोष द से पहले त् → द्: अभ्यक्तवत् + दृश्यन्ते → अभ्यक्तवद्दृश्यन्ते।",
    },
    "20": {
        "seesaw": ("अतिप्रविष्टे (बहुत धँसी) ⇄ निर्गते (बाहर निकली) · विस्तृते (फैली) ⇄ संक्षिप्ते (सिकुड़ी) · "
                   "अत्युन्मिषिते (बहुत खुली) ⇄ अतिनिमिषिते (बहुत मिची): तीनों जोड़े इसी इकाई में।"),
        "chunks": ("नयने चातिप्रविष्टे | निर्गतेविस्तृते संक्षिप्ते | संक्षिप्तभ्रुणी विनतभ्रुणी | जिह्वे विषमे | विश्रांतदर्शनेहीनदर्शने | "
                   "नकुलाभे कपोताभे | अलातवर्णे नीलादिविकृतवर्णे | अतिचले स्तब्धस्रस्ते प्रस्रुते | अत्युन्मिषिते अतिनिमिषिते | लुप्तपक्ष्मणीवा"),
        "sandhi": "अ + अ → आ: च + अति- → चाति- · इ + उ → यु: अति + उन्मिषिते → अत्युन्मिषिते · अ + आ → आ: नकुल + आभे → नकुलाभे।",
        "letters": "नयने, निर्गते, विस्तृते ... अ-अन्त शब्द -ए में, -भ्रुणी, -पक्ष्मणी -ई में: सब नपुंसक द्विवचन, ‘दोनों आँखें’। (मेरी याद-पद्धति)",
    },
    "21": {
        "diagram": {"groups": [
            {"label": "डेटा के अनुसार एक शृंखला (सम्भवतः)",
             "items": ["कार्ड १७: प्रतिच्छाया विकृत", "कार्ड १८: ललाट न पसीजे", "कार्ड १९: केश-लोम तेल लगे जैसे",
                       "कार्ड २०: दोनों आँखें", "कार्ड २१: नासिका", "मुख्य वाक्य: स गतायुः"]}]},
        "chunks": "नासिका वा | ऽतिविवृताऽतिसंवृता | कुटिला स्फुटिता | पिटिकाचिता | शुष्का वा | स गतायुः",
        "seesaw": "अतिविवृता (बहुत खुली) ⇄ अतिसंवृता (बहुत बन्द): दोनों इसी इकाई में।",
        "sandhi": "अ + आ → आ: गत + आयुः → गतायुः · आ + आ → आ: पिटिका + आचिता → पिटिकाचिता · सः व्यंजन से पहले विसर्ग खोता है: सः + गतायुः → स गतायुः।",
    },
    "22": {
        "chunks": "यस्याधोऽधरोष्ठो | यात्युत्तरोष्ठश्चोर्ध्वमुखौ | वा | पक्वजंबू नीलौ",
        "sandhi": ("अः + अ → ओऽ: अधः + अधरोष्ठः → अधोऽधरोष्ठः · अः + घोष व्यंजन → ओ: अधरोष्ठः + याति → अधरोष्ठो याति · इ + उ → यु: "
                   "याति + उत्तर- → यात्युत्तर- · च से पहले ः → श्: उत्तरोष्ठः + च → उत्तरोष्ठश्च · अ + ऊ → ओ: च + ऊर्ध्व- → चोर्ध्व-।"),
        "seesaw": "अधर (निचला) ⇄ उत्तर (ऊपरी); अधः (नीचे) ⇄ ऊर्ध्व (ऊपर): चारों शब्द इसी इकाई में।",
    },
    "23": {
        "diagram": {"groups": [
            {"label": "दाँत (छपे क्रम में)",
             "items": ["१ अतिरूक्षाः: बहुत रूखे", "२ ताम्राः: ताँबे के रंग के", "३ श्यामाः: साँवले", "४ पंकिलाः: कीचड़ वाले",
                       "५ पुष्पिताः: पुष्पित (अर्थ नहीं बताया)", "६ सशर्करा: कणों वाले", "७ सहसा पतंति: अचानक गिरें"]}]},
        "chunks": "दंता वाऽतिरूक्षास्ताम्राः | श्यामाः | पंकिलाःपुष्पिताः | सशर्करा वा | सहसा वा पतंति",
        "sandhi": ("आः घोष वर्ण से पहले विसर्ग खोता है: दन्ताः + वा → दन्ता वा, सशर्कराः + वा → सशर्करा वा · त से पहले ः → स्: "
                   "अतिरूक्षाः + ताम्राः → अतिरूक्षास्ताम्राः।"),
    },
    "24": {
        "diagram": {"groups": [
            {"label": "जीभ (छपे क्रम में)",
             "items": ["१ जिह्मा: टेढ़ी", "२ स्तब्धासुप्ता: कड़ी, सुन्न (सुप्ता अनुमानित)", "३ अवलिप्ता: लिपी", "४ गुर्वी: भारी",
                       "५ श्यावा: श्याव", "६ शूना: सूजी", "७ शुष्का: सूखी", "८ विसर्पिणी: फैलने वाली", "९ कंटकाचिता इव: काँटों जैसी"]}]},
        "chunks": "जिह्वा वा जिह्मा | स्तब्धासुप्ताऽवलिप्ता | गुर्वी श्यावा | शूना शुष्का | विसर्पिणी | कंटकाचितेववा",
        "sandhi": "आ + इ → ए: कण्टकाचिता + इव → कण्टकाचितेव।",
        "puns": "जिह्वा जिह्मा: व और म का अन्तर, जीभ और टेढ़ी। केवल सुनने की सहायता। (मेरा बनाया स्मरण-सूत्र)",
    },
    "25": {
        "chunks": "यस्य | गंडेललाटहनुबंधनानि | स्थानाच्चुतानीव | स्रस्तानि || यस्यन धन्ते | शिरः शिरोधरां पृष्ठं वा | स्वभारं",
        "sandhi": "अस् + घोष व्यंजन → ओ: शिरस् + धरा → शिरोधरा · छपा ‘स्थानाच्चुतानीव’: च्युत का य नहीं छपा, सन्धि पर प्रश्न नहीं।",
        "anchors": "पक्का: बन्धन ढीले (स्रस्तानि); ‘मानो स्थान से च्युत’ छपे ‘चुतानीव’ से पढ़ा गया। अनुमान: ‘धन्ते’ → धत्ते और सिर-गर्दन-पीठ का भार। (मेरी याद-पद्धति)",
    },
    "26": {
        "chunks": "हनू वा | पिंडमास्यस्थं",
        "sandhi": "म् + स्वर → जुड़ता है: पिण्डम् + आस्यस्थम् → पिण्डमास्यस्थम्।",
        "anchors": "पक्का: हनू (दोनों जबड़े), पिण्ड (कौर), आस्यस्थ (मुख में स्थित)। क्रिया: छपी नहीं। (मेरी याद-पद्धति)",
    },
}

# ================================================================ IMAGE_SPECS
IMAGE_SPECS = {
    ("15", "contrast"): {
        "file": "sh9-chhaya-prabha-15.svg",
        "alt": ("Split of card 15: chāyā overspreads the colour, is near (perceived: conjectural reading), and is made of "
                "the five elements; prabhā illuminates the colour, is seen from afar, and is the radiance of tejas."),
        "type": "split",
        "title": "कार्ड १५: छाया और प्रभा",
        "cols": [["छाया", ["वर्ण पर छा जाती", "आसन्ना: समीप (‘दिखती’ अनुमान)", "पाँच भूतों से बनी"]],
                 ["प्रभा", ["वर्ण को प्रकाशित करती", "दूर से दिखती", "तेजस् की प्रभा"]]],
    },
    ("17", "diagram"): {
        "file": "sh9-praticchaya-17.svg",
        "alt": ("Table of card 17 in printed order: the reflection seen cut, split, deficient, in excess, confused, lost, "
                "jihyā (conjecture: crooked), head downward, headless, two-headed, spread out, otherwise or distorted."),
        "type": "table",
        "title": "कार्ड १७: प्रतिच्छाया के विकार",
        "heads": ["क्रम", "छपा शब्द: अर्थ"],
        "rows": [["१", "छिन्ना: कटी"], ["२", "भिन्ना: फटी"], ["३", "हीना: हीन"], ["४", "अधिका: अधिक"], ["५", "आकुला: व्याकुल"],
                 ["६", "नष्टा: नष्ट"], ["७", "जिह्या: अनुमान टेढ़ी"], ["८", "अवाक्शिरा: नीचे सिर"], ["९", "विशिरा: सिरहीन"],
                 ["१०", "द्विशिरा: दो सिर"], ["११", "विस्तृता: फैली"], ["१२", "अन्यथा, विकृता"]],
    },
    ("20", "seesaw"): {
        "file": "sh9-nayana-20.svg",
        "alt": ("Table of card 20: three opposite pairs of eye changes: sunk too deep and protruding; widened and "
                "contracted; excessively open and excessively shut."),
        "type": "table",
        "title": "कार्ड २०: आँखों के उलटे जोड़े",
        "heads": ["एक ओर", "विपरीत"],
        "rows": [["अतिप्रविष्टे: बहुत धँसी", "निर्गते: बाहर निकली"], ["विस्तृते: फैली", "संक्षिप्ते: सिकुड़ी"],
                 ["अत्युन्मिषिते: बहुत खुली", "अतिनिमिषिते: बहुत मिची"]],
    },
    ("21", "diagram"): {
        "file": "sh9-gatayu-21.svg",
        "alt": ("Table of cards 17 to 21, which the data probably takes as one series: reflection, forehead not sweating, "
                "hair as if anointed, the two eyes, the nose; its main clause is sa gatāyuḥ in card 21."),
        "type": "table",
        "title": "कार्ड १७-२१: एक शृंखला (सम्भवतः)",
        "heads": ["कार्ड", "लक्षण"],
        "rows": [["१७", "प्रतिच्छाया विकृत"], ["१८", "ललाट न पसीजे"], ["१९", "केश-लोम तेल लगे जैसे"], ["२०", "दोनों आँखों के विकार"],
                 ["२१", "नासिका के विकार"], ["२१", "मुख्य वाक्य: स गतायुः"]],
    },
    ("23", "diagram"): {
        "file": "sh9-danta-23.svg",
        "alt": ("Table of card 23 in printed order: teeth very dry, copper-coloured, dusky, muddy, flowered (sense not "
                "stated), with grit, or suddenly falling out."),
        "type": "table",
        "title": "कार्ड २३: दाँतों के विकार",
        "heads": ["क्रम", "छपा शब्द = अर्थ"],
        "rows": [["१", "अतिरूक्षाः = बहुत रूखे"], ["२", "ताम्राः = ताँबे के रंग"], ["३", "श्यामाः = साँवले"], ["४", "पंकिलाः = कीचड़ वाले"],
                 ["५", "पुष्पिताः = अर्थ नहीं बताया"], ["६", "सशर्करा = कणों वाले"], ["७", "सहसा पतंति = अचानक गिरें"]],
    },
    ("24", "diagram"): {
        "file": "sh9-jihva-24.svg",
        "alt": ("Table of card 24 in printed order: tongue crooked, stiff and numb (printed stabdhāsuptā; numb is a conjectural reading), coated, heavy, dark "
                "brown, swollen, dry, spreading, as if covered with thorns."),
        "type": "table",
        "title": "कार्ड २४: जीभ के विकार",
        "heads": ["क्रम", "छपा शब्द: अर्थ"],
        "rows": [["१", "जिह्मा: टेढ़ी"], ["२", "स्तब्धासुप्ता: कड़ी, सुन्न (सुप्ता अनुमान)"], ["३", "अवलिप्ता: लिपी"],
                 ["४", "गुर्वी: भारी"], ["५", "श्यावा: श्याव"], ["६", "शूना: सूजी"], ["७", "शुष्का: सूखी"],
                 ["८", "विसर्पिणी: फैलने वाली"], ["९", "कंटकाचिता इव: काँटों जैसी"]],
    },
}
