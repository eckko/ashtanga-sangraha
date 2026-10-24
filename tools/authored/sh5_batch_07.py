from helpers import mcq, match, order, fill, multi, accepts


AUTHORED = {}

# ---------------------------------------------------------------- unit 77
AUTHORED["77"] = {
    "title": "असृजः कृष्णमंडलं तन्मातृजं",
    "question": "By unit 77, from what does the black circle of the eye come, and what is the circle of sight?",
    "rule": ("From blood (असृज्) comes the kṛṣṇa-maṇḍala (black circle, probably the dark part of the eye); it is born from "
             "the mother (मातृज). In the middle is the dṛṣṭi-maṇḍala (circle of sight, probably the pupil region); it has the "
             "nature of both (उभयात्मक)."),
    "limits": ("Prose; the verb 'arises' is carried over, not printed. The modern equivalents are probable only. 'Both' presumably "
               "means father- and mother-born; the line does not say: no question on it. असृजः may be 'of' or 'from' blood: "
               "no question on its case."),
    "explain_hi": ("यह गद्य-पंक्ति आँख के दो और मण्डल बताती है। "
                   "रक्त (असृज्) से कृष्णमण्डल, यानी सम्भवतः आँख का काला भाग, बनता है; वह मातृज, यानी माता से उत्पन्न, है। "
                   "बीच में (मध्ये) दृष्टिमण्डल है, यानी सम्भवतः पुतली का क्षेत्र; वह उभयात्मक, यानी दोनों के स्वभाव वाला, है। "
                   "‘दोनों’ सम्भवतः पिता और माता से उत्पन्न भाग हैं, पर पंक्ति यह स्पष्ट नहीं कहती। "
                   "क्रिया ‘बनता है’ पिछली इकाइयों से समझी जाती है।"),
    "hook": "रक्त से काला मण्डल, माँ से; बीच में दृष्टि, दोनों से।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 77, from what does the kṛṣṇa-maṇḍala (black circle) of the eye come?",
            ("From blood (असृज्)", "असृजः कृष्णमंडलम्: the black circle comes from blood."),
            [("From fat (मेदस्)", "Fat is not named in unit 77; the black circle comes from blood."),
             ("From bone (अस्थि)", "Bone is not named in unit 77; the black circle comes from blood."),
             ("From marrow (मज्जा)", "Marrow is not named in unit 77; the black circle comes from blood.")],
            "The kṛṣṇa-maṇḍala comes from blood and is mother-born.",
            "असृजः कृष्णमंडलं तन्मातृजम्."),
        order(1, "Put these phrases of unit 77 in the line's order.",
              ["असृजः कृष्णमंडलं", "तन्मातृजं", "मध्ये दृष्टिमंडलं", "तदुभयात्मकं"],
              "From blood the black circle; that is mother-born; in the middle the circle of sight; that has the nature of both.",
              "असृजः कृष्णमंडलं → तन्मातृजं → मध्ये दृष्टिमंडलं → तदुभयात्मकं."),
        match(2, "Match each word of unit 77 to its meaning.",
              [["असृज्", "blood"], ["कृष्ण", "black"], ["मातृज", "born from the mother"], ["मध्ये", "in the middle"],
               ["उभयात्मक", "having the nature of both"]],
              "From blood the black circle, mother-born; in the middle the circle of sight, of both natures.",
              "असृज्, कृष्ण, मातृज, मध्ये, उभयात्मक.", role="extend",
              teaches="मातृज = मातृ (mother) + ज (born): born from the mother; उभयात्मक = having the nature of both."),
        mcq("discriminate", 3, "Which split of तन्मातृजं in unit 77 is right?",
            ("तत् + मातृजम्", "त् before the nasal म is written न् here: तत् + मातृजम् → तन्मातृजम्."),
            [("तम् + मातृजम्", "म् + म would give तम्मातृजम् or तंमातृजम्, and the data reads तत् (that, neuter)."),
             ("तन्मा + तृजम्", "तन्मा and तृजम् are not words; the words are तत् and मातृजम्."),
             ("तन्म + आतृजम्", "तन्म and आतृजम् are not words; the words are तत् and मातृजम्.")],
            "तत् (that) + मातृजम् (mother-born): before म the त् appears as न्.",
            "तत् + मातृजम् → तन्मातृजम्."),
        multi("apply", 4, "Which statements fit unit 77?",
              [("The circle of sight lies at the outer edge", "It lies in the middle: मध्ये दृष्टिमंडलम्."),
               ("The black circle comes from blood", "Right: असृजः कृष्णमंडलम्."),
               ("The black circle is born from the mother", "Right: तन्मातृजम्."),
               ("The circle of sight is born from the mother only", "It has the nature of both: तदुभयात्मकम्.")],
              [1, 2],
              "From blood the black circle, mother-born; the circle of sight in the middle has the nature of both.",
              "असृजः कृष्णमंडलं तन्मातृजं मध्ये दृष्टिमंडलं तदुभयात्मकम्."),
        mcq("transfer", 5, "By the rule of तदुभयात्मकं (तत् + उभय...), how is एतत् + उक्तम् (this is said) joined?",
            ("एतदुक्तम्", "त् before a vowel becomes द्, as तत् + उभयात्मकम् → तदुभयात्मकम्."),
            [("एततुक्तम्", "Before a vowel the final त् does not stay unvoiced; it becomes द्."),
             ("एतनुक्तम्", "न् is not taken before a vowel; त् becomes द्."),
             ("एतदोक्तम्", "उ does not change to ओ here; only त् changes to द्.")],
            "एतत् + उक्तम् = एतदुक्तम्, like तत् + उभयात्मकम् = तदुभयात्मकम्.",
            "A final त् before a vowel → द्.",
            teaches="A final त् becomes द् before a vowel: तत् + उभयात्मकम् → तदुभयात्मकम्."),
    ],
}

# ---------------------------------------------------------------- unit 78
AUTHORED["78"] = {
    "title": "पक्ष्मवर्त्मशुक्लकृष्णदृष्ट्यास्यानि पंच मंडलानि",
    "question": "By unit 78, which are the five maṇḍalas (circles) of the eye?",
    "rule": ("The five maṇḍalas (circles) are named, in order: pakṣma (eyelashes), vartma (eyelid), śukla (white), "
             "kṛṣṇa (black) and dṛṣṭi (sight)."),
    "limits": ("A prose line. The last part of the compound is printed आस्यानि (mouths), which gives no sense; it is read "
               "आख्यानि (named) on a conjecture: no question rests on that word. The copula is understood."),
    "explain_hi": ("यह गद्य-पंक्ति आँख के पाँच मण्डल क्रम से गिनाती है: पक्ष्म (पलक के बाल), वर्त्म (पलक), शुक्ल (सफेद), "
                   "कृष्ण (काला) और दृष्टि। "
                   "छपा ‘आस्यानि’ (मुख) अर्थ नहीं देता और छठा नाम जोड़ देता; इसलिए अनुमानित पाठ ‘आख्यानि’ (नाम वाले) लिया गया है। "
                   "उस शब्द पर कोई प्रश्न नहीं। "
                   "शुक्ल, कृष्ण और दृष्टि मण्डल पिछली इकाइयों में भी आए हैं।"),
    "hook": "पक्ष्म, वर्त्म, शुक्ल, कृष्ण, दृष्टि: बाहर से भीतर पाँच मण्डल।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 78, what are the five things named in this line?",
            ("The five maṇḍalas, the circles", "पंच मंडलानि: the five maṇḍalas (circles)."),
            [("The five seats of the senses", "The seats of the senses are another topic; this line names maṇḍalas."),
             ("The five layers of the skin", "The skin's layers are another topic; this line names maṇḍalas."),
             ("The five organs of action", "The organs of action are another topic; this line names maṇḍalas.")],
            "The line names the five maṇḍalas (circles) of the eye.",
            "पक्ष्म... दृष्टि... पंच मंडलानि."),
        order(1, "Put the five maṇḍalas of unit 78 in the line's order.",
              ["पक्ष्म", "वर्त्म", "शुक्ल", "कृष्ण", "दृष्टि"],
              "Eyelashes, eyelid, white, black, sight.",
              "पक्ष्म → वर्त्म → शुक्ल → कृष्ण → दृष्टि."),
        match(2, "Match each maṇḍala of unit 78 to its meaning.",
              [["पक्ष्म", "eyelashes"], ["वर्त्म", "eyelid"], ["शुक्ल", "white"], ["कृष्ण", "black"], ["दृष्टि", "sight"]],
              "The five maṇḍalas: eyelashes, eyelid, white, black, sight.",
              "पक्ष्म, वर्त्म, शुक्ल, कृष्ण, दृष्टि.", role="extend",
              teaches="पक्ष्म = eyelashes and वर्त्म = eyelid are counted as maṇḍalas too, beside the white, black and sight circles."),
        multi("discriminate", 3, "Which of these are among the five maṇḍalas of unit 78?",
              [("वर्त्म (eyelid)", "Right: the second maṇḍala."),
               ("अपाङ्ग (outer corner)", "Not a maṇḍala in unit 78; the outer corner is named in unit 80."),
               ("पटल (layer)", "Not a maṇḍala; the six paṭalas are a separate count (unit 82)."),
               ("कृष्ण (black)", "Right: the fourth maṇḍala.")],
              [0, 3],
              "The five are pakṣma, vartma, śukla, kṛṣṇa and dṛṣṭi.",
              "पक्ष्मवर्त्मशुक्लकृष्णदृष्टि... पंच मंडलानि."),
        mcq("apply", 4, "By unit 78, which maṇḍala is named right after वर्त्म (eyelid)?",
            ("शुक्ल (white)", "The order is पक्ष्म, वर्त्म, शुक्ल, कृष्ण, दृष्टि."),
            [("दृष्टि (sight)", "दृष्टि comes last, after कृष्ण."),
             ("कृष्ण (black)", "कृष्ण comes after शुक्ल, not straight after वर्त्म."),
             ("पक्ष्म (eyelashes)", "पक्ष्म comes first, before वर्त्म.")],
            "After the eyelid comes the white circle, then the black, then sight.",
            "पक्ष्म → वर्त्म → शुक्ल → कृष्ण → दृष्टि."),
        mcq("transfer", 5, "In unit 78, दृष्टि before the following आ is written दृष्ट्या... By that rule, how is इति + आह (thus he says) joined?",
            ("इत्याह", "इ before a different vowel becomes य्: इति + आह → इत्याह."),
            [("इतेह", "ए comes from अ + इ, not from इ + आ."),
             ("इताह", "The इ does not drop; it becomes य्."),
             ("इतीआह", "The इ does not lengthen; it becomes य् before आ.")],
            "इति + आह = इत्याह, as दृष्टि + आ... → दृष्ट्या...",
            "इ + a different vowel → य् + that vowel.",
            teaches="A final इ before a different vowel becomes य्: दृष्टि + आ... → दृष्ट्या..."),
    ],
}

# ---------------------------------------------------------------- unit 79
AUTHORED["79"] = {
    "title": "तत्संधयश्चत्वारः",
    "question": "By unit 79, how many are the junctions (sandhi) of the five maṇḍalas?",
    "rule": ("Their (तत्, the five maṇḍalas') junctions (सन्धि) are four (चत्वारः). सन्धयः + चत्वारः → सन्धयश्चत्वारः: "
             "a visarga before च becomes श्."),
    "limits": ("A prose line of one printed word group. Here सन्धि means a junction between the maṇḍalas, not a word-join. "
               "The junctions are not named in this unit; the copula is understood."),
    "explain_hi": ("यह छोटी गद्य-पंक्ति कहती है: उनकी, यानी पाँच मण्डलों की, सन्धियाँ चार हैं। "
                   "यहाँ ‘सन्धि’ का अर्थ मण्डलों के बीच का जोड़ है, शब्दों की सन्धि नहीं। "
                   "‘तत्’ इकाई ७८ के पाँच मण्डलों को कहता है। "
                   "सन्धयः + चत्वारः में च से पहले विसर्ग श् बना है: सन्धयश्चत्वारः। "
                   "कौन-सी चार सन्धियाँ हैं, यह इस इकाई में नहीं कहा गया।"),
    "hook": "पाँच मण्डल, उनके बीच चार जोड़।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 79, how many are the junctions (sandhi) of the maṇḍalas?",
            ("Four (चत्वारः)", "तत्संधयश्चत्वारः: their junctions are four."),
            [("Twelve (द्वादश)", "The line says चत्वारः, four."),
             ("Five (पञ्च)", "Five is the count of the maṇḍalas, not of their junctions."),
             ("Eight (अष्टौ)", "The line says चत्वारः, four.")],
            "The junctions of the five maṇḍalas are four.",
            "तत्सन्धयः चत्वारः."),
        match(1, "Match each part of unit 79 to its meaning.",
              [["तत्", "their (of the maṇḍalas)"], ["सन्धयः", "junctions"], ["चत्वारः", "four"]],
              "Their junctions are four.",
              "तत्, सन्धयः, चत्वारः."),
        fill(2, "Their junctions are four: तत्सन्धयः ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("चत्वारः", None, "chatvarah", "chatvara"),
             "चत्वारः = four (masculine, agreeing with सन्धयः).",
             "चत्वारः = four, masculine nominative plural, agreeing with सन्धयः (junctions).",
             "तत्सन्धयः चत्वारः = their junctions are four."),
        mcq("discriminate", 3, "Which split of सन्धयश्चत्वारः is right?",
            ("सन्धयः + चत्वारः", "The visarga before च becomes श्: सन्धयः + चत्वारः → सन्धयश्चत्वारः."),
            [("सन्धय + श्चत्वारः", "श्चत्वारः is not a word; the श् comes from the visarga of सन्धयः."),
             ("सन्धयो + चत्वारः", "सन्धयो is not the word here; ओ comes from अः only before a voiced sound."),
             ("सन्धि + अश्चत्वारः", "अश्चत्वारः is not a word, and the form is सन्धयः, the plural.")],
            "सन्धयः (junctions) + चत्वारः (four): ः before च → श्.",
            "Visarga before च or छ → श्."),
        mcq("apply", 4, "In unit 79, what does तत् in तत्सन्धयः refer to?",
            ("The five maṇḍalas of the eye", "The data: tat- refers to the five maṇḍalas of unit 78."),
            [("The six paṭalas (layers) of the eye", "The paṭalas come later, in unit 82; tat- points back to the maṇḍalas."),
             ("The two corners of the eye", "The corners are named in unit 80; tat- points back to the maṇḍalas."),
             ("The five organs of action", "Those are another topic; tat- points back to the maṇḍalas.")],
            "Their junctions = the junctions of the five maṇḍalas.",
            "तत्- = of those (the five maṇḍalas)."),
        mcq("transfer", 5, "By the rule of सन्धयश्चत्वारः, how is रामः + चलति (Rāma moves) joined?",
            ("रामश्चलति", "The visarga before च becomes श्, as सन्धयः + चत्वारः."),
            [("रामो चलति", "ओ comes from अः only before a voiced sound; च is unvoiced."),
             ("रामस्चलति", "Before च the visarga becomes श्, not स्."),
             ("राम चलति", "Before च the visarga is not dropped; it becomes श्.")],
            "रामः + चलति = रामश्चलति, like सन्धयः + चत्वारः = सन्धयश्चत्वारः.",
            "Visarga before च or छ → श्.",
            teaches="A visarga before च or छ becomes श्: सन्धयः + चत्वारः → सन्धयश्चत्वारः."),
    ],
}

# ---------------------------------------------------------------- unit 80
AUTHORED["80"] = {
    "title": "द्वौ चापांगकनीनयोः",
    "question": "By unit 80, where are the two further ones placed?",
    "rule": ("And two (द्वौ च), at the apāṅga (outer corner of the eye) and the kanīna (probably the inner corner of the eye). "
             "च + अपाङ्ग → चापाङ्ग: अ + अ → आ."),
    "limits": ("A prose line. The noun counted is not named in this unit and is not supplied. Kanīna = inner corner is "
               "probable only (it may also mean the pupil). The dual -नयोः is taken as locative; genitive is possible: no "
               "question on its case."),
    "explain_hi": ("यह छोटी गद्य-पंक्ति कहती है: और दो, अपांग यानी आँख के बाहरी कोने में और कनीन यानी सम्भवतः भीतरी कोने में। "
                   "गिनी जा रही वस्तु का नाम इस इकाई में नहीं है; वह सम्भवतः पिछली इकाई से चलता है। "
                   "कनीन का अर्थ भीतरी कोना सम्भावित है; पुतली भी हो सकता है। "
                   "‘-नयोः’ को सप्तमी (में) लिया गया है, षष्ठी भी सम्भव है। "
                   "च + अपांग में अ + अ से आ बना है: चापांग।"),
    "hook": "दो और: बाहरी कोना और (सम्भवतः) भीतरी कोना।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 80, at which places are the two placed?",
            ("At the apāṅga and the kanīna", "चापांगकनीनयोः: at the outer corner and (probably) the inner corner."),
            [("At the upper and the lower eyelids", "The line names the apāṅga and kanīna, not the eyelids."),
             ("At the root and the tip of the tongue", "The tongue is not named; the line names the eye's corners."),
             ("At the two ears and the two nostrils", "Ears and nostrils are not named; the line names the eye's corners.")],
            "Two are placed at the apāṅga and the kanīna.",
            "द्वौ च अपाङ्गकनीनयोः."),
        match(1, "Match each word of unit 80 to its meaning.",
              [["द्वौ", "two"], ["च", "and"], ["अपाङ्ग", "outer corner of the eye"],
               ["कनीन", "probably the inner corner of the eye"]],
              "And two, at the outer corner and (probably) the inner corner.",
              "द्वौ, च, अपाङ्ग, कनीन."),
        fill(2, "च + अपाङ्ग is joined as ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("चापाङ्ग", None, "चापांग", "chapanga"),
             "च + अपाङ्ग = चापाङ्ग: अ + अ → आ.",
             "A short अ followed by a short अ joins as long आ: च + अपाङ्ग → चापाङ्ग.",
             "च + अपाङ्ग → चापाङ्ग."),
        mcq("discriminate", 3, "Which split of चापांग in unit 80 is right?",
            ("च + अपाङ्ग", "अ + अ → आ: च (and) + अपाङ्ग (outer corner)."),
            [("चाप + अङ्ग", "चाप (bow) and अङ्ग give no sense here, and the line then loses its च (and)."),
             ("चे + अपाङ्ग", "ए + अ would give चेऽपाङ्ग, with ए kept and ऽ."),
             ("चा + पाङ्ग", "चा and पाङ्ग are not words; the words are च and अपाङ्ग.")],
            "च (and) + अपाङ्ग (outer corner of the eye) = चापाङ्ग.",
            "अ + अ → आ."),
        multi("apply", 4, "Which statements about unit 80 are right by the card?",
              [("The noun counted is named in this unit", "The data: the noun counted is not stated here."),
               ("Kanīna is certainly the pupil", "Kanīna is probably the inner corner; the sense is not firm."),
               ("Apāṅga is the outer corner of the eye", "Right: so the data glosses it."),
               ("Two are placed at the apāṅga and kanīna", "Right: द्वौ च अपाङ्गकनीनयोः.")],
              [2, 3],
              "Two at the apāṅga (outer corner) and kanīna (probably inner corner); the noun is not named here.",
              "द्वौ चापाङ्गकनीनयोः."),
        mcq("transfer", 5, "By the rule of चापांग (च + अपाङ्ग), how is च + अपि (and also) joined?",
            ("चापि", "अ + अ → आ, as च + अपाङ्ग → चापाङ्ग."),
            [("चोपि", "ओ comes from अ + उ, not from अ + अ."),
             ("चेपि", "ए comes from अ + इ, not from अ + अ."),
             ("चऽपि", "The avagraha marks an अ dropped after ए or ओ, not after अ.")],
            "च + अपि = चापि, like च + अपाङ्ग = चापाङ्ग.",
            "अ + अ → आ.",
            teaches="A short अ followed by a short अ joins as long आ: च + अपाङ्ग → चापाङ्ग."),
    ],
}

# ---------------------------------------------------------------- unit 81
AUTHORED["81"] = {
    "title": "इति ते षट्",
    "question": "What does unit 81 sum up?",
    "rule": ("इति ते षट्: thus these are six. ते (they, these) points back to the items counted before (apparently the four of "
             "unit 79 and the two of unit 80), which this unit does not name."),
    "limits": ("A prose line; the copula is understood. The items are not named here; that the six are the four plus two "
               "of units 79 and 80 is how the data reads it ('appears to complete the count')."),
    "explain_hi": ("यह छोटी गद्य-पंक्ति गिनती पूरी करती है: इस प्रकार (इति) वे (ते) छह (षट्) हैं। "
                   "‘ते’ पिछली इकाइयों में गिनी वस्तुओं की ओर संकेत करता है: इकाई ७९ की चार और इकाई ८० की दो। "
                   "इस इकाई में उनका नाम नहीं है। "
                   "‘है’ क्रिया समझी जाती है।"),
    "hook": "चार और दो: इति ते षट्।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What does इति do in unit 81 (इति ते षट्)?",
            ("It sums up a count: thus", "इति ते षट्: thus these are six."),
            [("It asks a question: whether", "इति does not ask here; it closes the count."),
             ("It gives a cause: because", "No cause is given; इति closes the count."),
             ("It opens a new list: namely", "No new list follows in this unit; इति closes the count.")],
            "इति = thus: it rounds off the count.",
            "इति ते षट् = thus these are six."),
        match(1, "Match each word of unit 81 to its meaning.",
              [["इति", "thus"], ["ते", "they, these"], ["षट्", "six"]],
              "Thus these are six.",
              "इति, ते, षट्."),
        fill(2, "Thus these are six: इति ते ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("षट्", None, "shat", "shad"),
             "षट् = six.",
             "षट् = six; इति ते षट् = thus these are six.",
             "इति ते षट्."),
        mcq("discriminate", 3, "One word of this translation of unit 81 is wrong: Thus these are seven. Which?",
            ("seven", "षट् is six, not seven."),
            [("thus", "इति = thus: right."),
             ("these", "ते = they, these: right."),
             ("are", "The copula 'are' is understood: right.")],
            "इति ते षट् = thus these are six.",
            "षट् = six."),
        mcq("apply", 4, "In unit 81, to what does ते (they) point?",
            ("To items counted earlier, unnamed here", "The data: te points back to the items counted before."),
            [("To the six paṭalas named in this unit", "No paṭala is named in unit 81; they come in unit 82."),
             ("To the five maṇḍalas of unit 78", "Five is not six; ते points to the six items counted earlier."),
             ("To the two eyelids of unit 83", "Those come later; ते points back to earlier items.")],
            "ते points back to the items counted earlier; this unit names none.",
            "ते = they (the items counted before)."),
        mcq("transfer", 5, "By the use of ते in unit 81 (they, masc. nom. pl.), what does ते वृक्षाः mean (वृक्ष = tree)?",
            ("These trees", "ते, masc. nom. pl., goes with the masc. nom. pl. वृक्षाः: these (those) trees."),
            [("Of the tree", "That would need the genitive वृक्षस्य; ते वृक्षाः is nominative plural."),
             ("By the tree", "That would need the instrumental वृक्षेण; ते वृक्षाः is nominative plural."),
             ("That one tree", "One tree would be सः वृक्षः; ते वृक्षाः is plural.")],
            "ते वृक्षाः = these (those) trees, like ते in इति ते षट्.",
            "ते = they, these (masc. nom. pl.).",
            teaches="ते is the masculine nominative plural of तत्: they, these, those."),
    ],
}

# ---------------------------------------------------------------- unit 82
AUTHORED["82"] = {
    "title": "षट् च पटलानि",
    "question": "By unit 82, what new count is given?",
    "rule": ("And six paṭalas (पटल: layers, coats). The eye is not named in the line; from the context of the units "
             "around it the layers are those of the eye."),
    "limits": ("A prose line with no verb; the copula is understood. The layers are not listed in this unit. That they are "
               "the eye's layers comes from the context, not from this line."),
    "explain_hi": ("यह छोटी गद्य-पंक्ति एक नई गिनती देती है: और छह पटल यानी परतें। "
                   "पंक्ति में आँख का नाम नहीं है; आसपास की इकाइयों के प्रसंग से ये आँख के पटल माने गए हैं। "
                   "इस इकाई में पटलों के नाम नहीं हैं। "
                   "षट् + च में कोई बदलाव नहीं होता, क्योंकि च अघोष है।"),
    "hook": "और छह परतें: षट् पटलानि।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 82, what are said to be six?",
            ("The paṭalas, the layers", "षट् च पटलानि: and six paṭalas (layers)."),
            [("The junctions of the maṇḍalas", "The junctions are counted in unit 79; this line counts paṭalas."),
             ("The binding strands", "The binding strands come in unit 85; this line counts paṭalas."),
             ("The circles of the eye", "The circles (maṇḍala) are five, in unit 78; this line counts paṭalas.")],
            "Unit 82 counts six paṭalas, layers.",
            "षट् च पटलानि."),
        match(1, "Match each word of unit 82 to its meaning.",
              [["षट्", "six"], ["च", "and"], ["पटल", "layer, coat"]],
              "And six layers.",
              "षट्, च, पटल."),
        fill(2, "And six layers: षट् च ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("पटलानि", None, "patalani"),
             "पटलानि = layers (neuter nominative plural of पटल).",
             "पटलानि = layers, neuter nominative plural of पटल.",
             "षट् च पटलानि."),
        mcq("discriminate", 3, "Why does षट् stay unchanged before च in unit 82?",
            ("च is unvoiced, so ट् stays as it is", "ट् would become ड् only before a voiced sound."),
            [("ट् never changes in any sandhi", "It does: before a vowel or voiced sound ट् becomes ड् (षडङ्ग)."),
             ("The print leaves out a due sandhi", "No sandhi is due; ट् stays before the unvoiced च."),
             ("च always makes the sound before it voiced", "च is unvoiced; it does not make ट् voiced.")],
            "Before the unvoiced च, ट् stays: षट् च.",
            "ट् stays before an unvoiced consonant; it becomes ड् before a vowel or voiced sound."),
        mcq("apply", 4, "By the card, whose layers are the six paṭalas, and does the line say so?",
            ("The eye's; known from the context", "The data: of the eye, from the context; the eye is not named in this line."),
            [("The eye's; the line names the eye", "The line does not name the eye; the context shows it."),
             ("The skin's; the line names the skin", "The skin is not named; the context is the eye."),
             ("The heart's; known from the context", "The context of these units is the eye, not the heart.")],
            "The six paṭalas are the eye's layers by context; the line names no organ.",
            "षट् च पटलानि (the eye from context)."),
        mcq("transfer", 5, "By the rule behind षट् च, how is षट् + अङ्गानि (six limbs) joined, the next word starting with a vowel?",
            ("षडङ्गानि", "Before a vowel ट् becomes ड्; before the unvoiced च it stayed ट्."),
            [("षटङ्गानि", "Before a vowel ट् does not stay unvoiced; it becomes ड्."),
             ("षडाङ्गानि", "The vowel अ does not lengthen; only ट् changes to ड्."),
             ("षण्णङ्गानि", "ण् is not taken before a vowel; ट् becomes ड्.")],
            "षट् + अङ्गानि = षडङ्गानि; षट् + च = षट् च.",
            "ट् before a vowel or voiced sound → ड्; before an unvoiced sound it stays.",
            teaches="A final ट् stays before an unvoiced sound (षट् च) and becomes ड् before a vowel or voiced sound (षडङ्गानि)."),
    ],
}

# ---------------------------------------------------------------- unit 83
AUTHORED["83"] = {
    "title": "द्वे वर्त्मनी",
    "question": "By unit 83, what two things are named?",
    "rule": ("Two vartmans (वर्त्मन्: eyelids, standard in this eye section). द्वे वर्त्मनी are both neuter nominative dual; "
             "वर्त्मन् also means path in other places."),
    "limits": ("A prose line with no verb; the copula is understood. The line does not say how the two eyelids relate to "
               "the six paṭalas of unit 82, and the card does not decide it."),
    "explain_hi": ("यह छोटी गद्य-पंक्ति दो वर्त्म, यानी पलकें, बताती है। "
                   "‘वर्त्मन्’ का अर्थ ‘मार्ग’ भी होता है, पर इस नेत्र-प्रसंग में यह पलक है (मानक)। "
                   "‘द्वे’ और ‘वर्त्मनी’ दोनों नपुंसक, प्रथमा, द्विवचन हैं। "
                   "छह पटलों से इन पलकों का सम्बन्ध पंक्ति स्पष्ट नहीं कहती।"),
    "hook": "दो पलकें: द्वे वर्त्मनी।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 83, what two things are named?",
            ("Two eyelids (वर्त्मनी)", "द्वे वर्त्मनी: two vartmans, eyelids."),
            [("Two nostrils (नासिके)", "Nostrils are not named in unit 83; it names eyelids."),
             ("Two ears (कर्णौ)", "Ears are not named in unit 83; it names eyelids."),
             ("Two testes (वृषणौ)", "Testes are not named in unit 83; it names eyelids.")],
            "Unit 83 names two vartmans, the eyelids.",
            "द्वे वर्त्मनी."),
        multi("warmup", 1, "Which statements about unit 83 are right by the card?",
              [("वर्त्मन् here means eyelid", "Right: so in the eye section (standard)."),
               ("The line has its own verb", "No verb is stated; the copula is understood."),
               ("वर्त्मन् can also mean path", "Right: the data notes the sense path."),
               ("The line names the eye itself", "The eye is not named in this line.")],
              [0, 2],
              "Two eyelids; vartman also means path; no verb; the eye is not named.",
              "द्वे वर्त्मनी."),
        fill(2, "Two eyelids: द्वे ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("वर्त्मनी", None, "vartmani"),
             "वर्त्मनी = two eyelids (neuter nominative dual of वर्त्मन्).",
             "वर्त्मनी is the neuter nominative dual of वर्त्मन् (eyelid).",
             "द्वे वर्त्मनी."),
        mcq("discriminate", 3, "Why is the number word द्वे, not द्वौ, in unit 83?",
            ("वर्त्मन् is neuter; द्वे is the neuter dual", "द्वे is the neuter (or feminine) dual of द्वि; द्वौ is masculine."),
            [("द्वे is the plural form of the word two", "द्वि is dual by nature; द्वे is a dual form, not a plural."),
             ("द्वे is the masculine dual of the word two", "The masculine dual is द्वौ; द्वे is neuter or feminine."),
             ("द्वे means second here, not the number two", "Second is द्वितीय; द्वे is the number two.")],
            "द्वे agrees with the neuter वर्त्मनी; with a masculine noun it would be द्वौ.",
            "द्वि: masc. du. द्वौ; neut./fem. du. द्वे."),
        mcq("apply", 4, "In unit 83, why is वर्त्मन् read as eyelid and not as path?",
            ("It stands in the section on the eye", "The data: vartman = eyelid in the eye section (standard)."),
            [("वर्त्मन् never means path anywhere", "It does mean path elsewhere; the context decides."),
             ("The line itself says नेत्र (the eye)", "The line names no organ; the context decides."),
             ("A dual can only ever mean eyelids", "Number does not decide the sense; the context does.")],
            "The eye section makes वर्त्मन् the eyelid here.",
            "वर्त्मन् = eyelid (eye section) / path (elsewhere)."),
        mcq("transfer", 5, "By द्वे वर्त्मनी (neuter dual), how is two fruits said, फल being neuter?",
            ("द्वे फले", "Neuter dual: द्वे with फले, as द्वे with वर्त्मनी."),
            [("द्वौ फलौ", "द्वौ and -औ are masculine dual forms; फल is neuter."),
             ("द्वे फलानि", "फलानि is plural; two needs the dual फले."),
             ("द्वौ फले", "द्वौ is masculine; with the neuter फले the number is द्वे.")],
            "द्वे फले = two fruits, like द्वे वर्त्मनी = two eyelids.",
            "Neuter nominative dual: द्वे + noun in the dual.",
            teaches="With a neuter noun, two is द्वे and the noun takes the dual: द्वे वर्त्मनी, द्वे फले."),
    ],
}

# ---------------------------------------------------------------- unit 84
AUTHORED["84"] = {
    "title": "बाह्यं चाश्रितमग्न्यंभसी द्वितीयं मांसं",
    "question": "By unit 84, which items are named as third and fourth, and what is left unsettled?",
    "rule": ("A compressed series: the outer one, resting on fire and water (reading not settled); second flesh (मांस), "
             "third fat (मेदस्), fourth bone (अस्थि); their thickness (बहुलता) is by a fifth part of sight (दृष्टि)."),
    "limits": ("Low confidence. The noun is not stated (probably paṭala). The first part (बाह्यं च आश्रितम् अग्न्यम्भसी) and "
               "its split are not settled; दृष्टेः पञ्चमांशेन is kept literal: no question on either. Questions rest on the "
               "sure words तृतीयं मेदः, चतुर्थम् अस्थि."),
    "explain_hi": ("यह गद्य-पंक्ति कठिन और संक्षिप्त है; विश्वास कम है। "
                   "गिनी जा रही संज्ञा नहीं दी गई; वह सम्भवतः पटल (इकाई ८२) है। "
                   "पहला अंश ‘बाहरी, और अग्नि तथा जल पर आश्रित’ अनिश्चित है, और उसका पद-विभाग भी केवल सम्भावित है। "
                   "आगे की क्रमिक सूची स्पष्ट है: दूसरा मांस, तीसरा मेद यानी चर्बी, चौथा अस्थि यानी हड्डी। "
                   "‘उनकी मोटाई दृष्टि के पाँचवें अंश से’ का शब्दार्थ ही रखा गया है; उसकी व्याख्या नहीं की गई।"),
    "hook": "दूसरा मांस, तीसरा मेद, चौथा अस्थि।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 84, what is named as the third?",
            ("Fat (मेदस्)", "तृतीयं मेदः: the third is fat."),
            [("Bone (अस्थि)", "Bone is named fourth: चतुर्थम् अस्थि."),
             ("Blood (रक्त)", "Blood is not named in unit 84."),
             ("Skin (त्वक्)", "Skin is not named in unit 84.")],
            "The third is medas, fat; the fourth is bone.",
            "तृतीयं मेदः."),
        order(1, "Put these printed words of unit 84 in the line's order.",
              ["मांसं", "तृतीयं", "मेदः", "चतुर्थम्", "अस्थि"],
              "Flesh; third, fat; fourth, bone.",
              "मांसं → तृतीयं → मेदः → चतुर्थम् → अस्थि."),
        match(2, "Match each word of unit 84 to its meaning.",
              [["तृतीय", "third"], ["चतुर्थ", "fourth"], ["मेदस्", "fat"], ["अस्थि", "bone"], ["बहुलता", "thickness, abundance"]],
              "Third fat, fourth bone; their thickness is stated in a part of sight.",
              "तृतीय, चतुर्थ, मेदस्, अस्थि, बहुलता.", role="extend",
              teaches="तृतीय = third, चतुर्थ = fourth: ordinal numbers that agree with the unnamed noun (neuter here)."),
        mcq("discriminate", 3, "Which split of चतुर्थमस्थि in unit 84 is right?",
            ("चतुर्थम् + अस्थि", "म् before a vowel stays म् and joins it: चतुर्थम् + अस्थि → चतुर्थमस्थि."),
            [("चतुर्थ + मस्थि", "मस्थि is not a word; the word is अस्थि (bone)."),
             ("चतुर्थः + अस्थि", "अः + अ would give चतुर्थोऽस्थि; the data reads चतुर्थम्."),
             ("चतुर्थम + स्थि", "चतुर्थम and स्थि are not words; the words are चतुर्थम् and अस्थि.")],
            "चतुर्थम् (fourth) + अस्थि (bone) = चतुर्थमस्थि.",
            "Final म् before a vowel → stays म्, joined to the vowel."),
        multi("apply", 4, "Which statements about unit 84 are right by the card?",
              [("The noun counted is printed in the line", "The data: the noun is not stated (probably paṭala)."),
               ("Bone is named fourth", "Right: चतुर्थम् अस्थि."),
               ("दृष्टेः पञ्चमांशेन has a settled meaning", "The data keeps it literal and does not interpret it."),
               ("The reading of the first part is not settled", "Right: the data calls it hard and not settled.")],
              [1, 3],
              "Fat third, bone fourth are sure; the first part and the fifth-part phrase are not settled.",
              "तृतीयं मेदः चतुर्थम् अस्थि."),
        mcq("transfer", 5, "By the rule of चतुर्थमस्थि, how is फलम् + अस्ति (there is a fruit) joined?",
            ("फलमस्ति", "म् before a vowel stays म् and joins it, as चतुर्थम् + अस्थि."),
            [("फलंस्ति", "Anusvāra stands for म् only before a consonant, not before a vowel."),
             ("फलास्ति", "The म् is not lost; it stays before the vowel."),
             ("फलमास्ति", "The vowel अ does not lengthen; the म् joins it.")],
            "फलम् + अस्ति = फलमस्ति, like चतुर्थम् + अस्थि = चतुर्थमस्थि.",
            "Final म् + vowel → म् joined to the vowel.",
            teaches="A final म् before a vowel stays म् and joins it: चतुर्थम् + अस्थि → चतुर्थमस्थि."),
    ],
}

# ---------------------------------------------------------------- unit 85
AUTHORED["85"] = {
    "title": "बंधनगुणास्तु चत्वारः सिराकंडरामेदःकफात्मकाः",
    "question": "By unit 85, how many binding strands are there, and of what nature?",
    "rule": ("The binding strands (बन्धनगुण) are four, having the nature of sirā (vein, vessel), kaṇḍarā (large tendon), "
             "medas (fat) and Kapha. गुणाः + तु → गुणास्तु: a visarga before त becomes स्."),
    "limits": ("A prose line. गुण is read as strand, cord (that which binds); the sense quality is possible and is not adopted: "
               "no question on the sense of गुण. What the strands bind is not named in this unit (the eye, from the context)."),
    "explain_hi": ("यह गद्य-पंक्ति बन्धन के चार गुण, यानी बाँधने वाली रज्जुएँ, बताती है। "
                   "उनका स्वरूप क्रम से है: सिरा (नस, वाहिका), कण्डरा (मोटा स्नायु-रज्जु), मेद (चर्बी) और कफ। "
                   "यहाँ ‘गुण’ को ‘रज्जु, डोरी’ पढ़ा गया है; ‘गुण’ (विशेषता) अर्थ भी सम्भव है, पर नहीं अपनाया गया। "
                   "गुणाः + तु में त से पहले विसर्ग स् बना है: गुणास्तु। "
                   "‘तु’ (पर, तो) पिछली बात से भेद दिखाता है।"),
    "hook": "चार बन्धन: सिरा, कण्डरा, मेद, कफ।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 85, of what nature are the binding strands?",
            ("Sirā, kaṇḍarā, fat and Kapha", "सिराकंडरामेदःकफात्मकाः: having the nature of these four."),
            [("Flesh, blood, Kapha and fat", "That is the list for the testes in unit 89, not the binding strands."),
             ("Skin, flesh, fat and bone", "Skin and bone are not in the list; it is sirā, kaṇḍarā, fat, Kapha."),
             ("Vāta, Pitta, Kapha and blood", "Vāta, Pitta and blood are not in the list of unit 85.")],
            "The four binding strands have the nature of sirā, kaṇḍarā, medas and Kapha.",
            "बन्धनगुणाः चत्वारः सिराकण्डरामेदःकफात्मकाः."),
        order(1, "Put the four natures of the binding strands in the line's order.",
              ["सिरा", "कण्डरा", "मेदस्", "कफ"],
              "Sirā, kaṇḍarā, medas, Kapha.",
              "सिरा → कण्डरा → मेदस् → कफ."),
        match(2, "Match each word of unit 85 to its meaning.",
              [["बन्धन", "binding"], ["सिरा", "vein, vessel"], ["कण्डरा", "large tendon"], ["मेदस्", "fat"],
               ["आत्मक", "having the nature of"]],
              "Four binding strands having the nature of sirā, kaṇḍarā, fat and Kapha.",
              "बन्धन, सिरा, कण्डरा, मेदस्, आत्मक.", role="extend",
              teaches="-आत्मक at the end of a compound = having the nature of, consisting of: सिरा...कफात्मक."),
        mcq("discriminate", 3, "Which split of बन्धनगुणास्तु is right?",
            ("बन्धनगुणाः + तु", "The visarga before त becomes स्: गुणाः + तु → गुणास्तु."),
            [("बन्धनगुणः + अस्तु", "अः + अ would give गुणोऽस्तु, and अस्तु (let it be) does not fit."),
             ("बन्धनगुणा + स्तु", "स्तु is not a word; the स् comes from the visarga."),
             ("बन्धनगुण + आस्तु", "आस्तु is not a word; the word is the particle तु.")],
            "बन्धनगुणाः (binding strands) + तु (however): ः before त → स्.",
            "Visarga before त or थ → स्."),
        multi("apply", 4, "Which of these are among the four natures of the binding strands in unit 85?",
              [("Flesh (मांस)", "Flesh is not in the list of unit 85."),
               ("Bone (अस्थि)", "Bone is not in the list of unit 85."),
               ("Sirā (vein, vessel)", "Right: the first of the four."),
               ("Kapha", "Right: the fourth of the four.")],
              [2, 3],
              "The four are sirā, kaṇḍarā, medas and Kapha.",
              "सिराकण्डरामेदःकफात्मकाः."),
        mcq("transfer", 5, "By the rule of गुणास्तु, how is देवाः + तत्र (the gods there) joined?",
            ("देवास्तत्र", "The visarga before त becomes स्, as गुणाः + तु → गुणास्तु."),
            [("देवा तत्र", "आः drops its visarga only before a voiced sound; त is unvoiced."),
             ("देवाश्तत्र", "श् is taken before च or छ, not before त."),
             ("देवोस्तत्र", "आ does not change to ओ; only the visarga changes.")],
            "देवाः + तत्र = देवास्तत्र, like गुणाः + तु = गुणास्तु.",
            "Visarga before त or थ → स्.",
            teaches="A visarga before त or थ becomes स्: बन्धनगुणाः + तु → बन्धनगुणास्तु."),
    ],
}

# ---------------------------------------------------------------- unit 86
AUTHORED["86"] = {
    "title": "श्लेष्मा तु परं सर्वसंधिबंधनम्",
    "question": "By unit 86, what is called the binder of all joints?",
    "rule": ("Śleṣman (Kapha), however, is the highest (परम्) binder of all joints (सर्वसन्धिबन्धनम्); thus it was said "
             "before (इत्युक्तं प्राक्)."),
    "limits": ("A prose line; the copula is understood. परम् is read as highest, chief; further is possible: no question on "
               "the sense of परम्. Where it was said before is not located here. Here सन्धि means a joint of the body."),
    "explain_hi": ("यह गद्य-पंक्ति कहती है: श्लेष्मा यानी कफ तो सभी सन्धियों का परम बन्धन है; ऐसा पहले कहा गया है (इत्युक्तं प्राक्)। "
                   "यहाँ ‘सन्धि’ शरीर का जोड़ है। "
                   "‘परम्’ को ‘सबसे बड़ा, मुख्य’ पढ़ा गया है; ‘आगे’ अर्थ भी सम्भव है। "
                   "पहले यह कहाँ कहा गया, यह इस इकाई में नहीं बताया गया। "
                   "छपाई में ‘परं’ और ‘सर्व’ जुड़े छपे हैं।"),
    "hook": "सब जोड़ों को बाँधे कफ: यह पहले कहा गया।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 86, what is the binder of all joints?",
            ("Śleṣman, that is Kapha", "श्लेष्मा ... सर्वसन्धिबन्धनम्: Kapha binds all joints."),
            [("Vāta, the moving doṣa", "Vāta is not named in unit 86; it names śleṣman."),
             ("Pitta, the hot doṣa", "Pitta is not named in unit 86; it names śleṣman."),
             ("Rakta, that is blood", "Blood is not named in unit 86; it names śleṣman.")],
            "Śleṣman (Kapha) is the chief binder of all joints.",
            "श्लेष्मा तु परं सर्वसन्धिबन्धनम्."),
        order(1, "Put these words of unit 86 in the line's order.",
              ["श्लेष्मा तु", "परं", "सर्वसंधिबंधनम्", "इत्युक्तं", "प्राक्"],
              "Śleṣman however, the highest, binder of all joints, thus said, before.",
              "श्लेष्मा तु → परं → सर्वसंधिबंधनम् → इत्युक्तं → प्राक्."),
        match(2, "Match each word of unit 86 to its meaning.",
              [["श्लेष्मन्", "Kapha"], ["सर्व", "all"], ["सन्धि", "joint"], ["बन्धन", "binder"], ["उक्त", "said"],
               ["प्राक्", "before, earlier"]],
              "Śleṣman is the binder of all joints; thus it was said before.",
              "श्लेष्मन्, सर्व, सन्धि, बन्धन, उक्त, प्राक्.", role="extend",
              teaches="श्लेष्मन् is another name of Kapha; सन्धि here is a joint of the body."),
        mcq("discriminate", 3, "Which split of इत्युक्तं in unit 86 is right?",
            ("इति + उक्तम्", "इ before a different vowel becomes य्: इति + उक्तम् → इत्युक्तम्."),
            [("इति + युक्तम्", "इति + युक्तम् would be written इति युक्तम्, with no य् from sandhi."),
             ("इत्य + उक्तम्", "इत्य is not a word; the particle is इति."),
             ("इतः + युक्तम्", "इतः + य would give इतो युक्तम्, and युक्तम् (joined) does not fit.")],
            "इति (thus) + उक्तम् (said): इ + उ → यु.",
            "इ + a different vowel → य् + that vowel."),
        mcq("apply", 4, "By unit 86, how is this statement about śleṣman presented?",
            ("As a thing said before", "इत्युक्तं प्राक्: thus it was said before."),
            [("As said here the first time", "प्राक् shows it was said before, not first here."),
             ("As to be explained later", "उक्तं प्राक् looks back, not forward."),
             ("As the view of other teachers", "No other teachers are named; it was said before.")],
            "The line recalls an earlier statement: thus it was said before.",
            "इति उक्तं प्राक् = thus it was said before."),
        mcq("transfer", 5, "By the rule of इत्युक्तम् (इति + उक्तम्), how is प्रति + उत्तरम् (a reply) joined?",
            ("प्रत्युत्तरम्", "इ before उ becomes य्, as इति + उक्तम् → इत्युक्तम्."),
            [("प्रत्योत्तरम्", "उ does not change to ओ; only इ changes to य्."),
             ("प्रतूत्तरम्", "ऊ comes from उ + उ, not from इ + उ."),
             ("प्रतेउत्तरम्", "ए comes from अ + इ; here इ becomes य्.")],
            "प्रति + उत्तरम् = प्रत्युत्तरम्, like इति + उक्तम् = इत्युक्तम्.",
            "इ + a different vowel → य् + that vowel.",
            teaches="A final इ before a different vowel becomes य्: इति + उक्तम् → इत्युक्तम्."),
    ],
}

# ---------------------------------------------------------------- unit 87
AUTHORED["87"] = {
    "title": "नेत्राश्रितं तु तेजो बाह्यतेजसा",
    "question": "By unit 87, how does the tejas in the eye become fit for its work, and what harms it?",
    "rule": ("The tejas (fire, radiance) resting in the eye becomes fit for its work (कर्मण्य) through union (योग) with the "
             "outer tejas, its own source, as a weapon (शस्त्र) does with a stone (अश्मन्); through excessive union "
             "(अतियोग) it is harmed (उपहन्यते)."),
    "limits": ("Prose: two sentences run together in the print (a visarga after भवति stands for a full stop). The stone is "
               "probably a whetstone, but the Sanskrit says only stone: no question on the kind of stone. What counts as "
               "excess is not stated."),
    "explain_hi": ("यह गद्य-पंक्ति आँख के तेज की बात करती है। "
                   "आँख में आश्रित तेज अपने उद्गम, बाहरी तेज, के योग से कर्म के योग्य (कर्मण्य) होता है, जैसे शस्त्र पत्थर से। "
                   "पर अतियोग, यानी बहुत अधिक योग, से वह क्षति पाता है (उपहन्यते)। "
                   "पत्थर सम्भवतः सान का पत्थर है, पर संस्कृत केवल ‘पत्थर’ कहती है। "
                   "छपाई में ‘भवति’ के बाद का विसर्ग सम्भवतः दण्ड है; दो वाक्य जुड़े छपे हैं।"),
    "hook": "बाहरी तेज से योग: धार; अतियोग: हानि।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 87, through union with what does the eye's tejas become fit for its work?",
            ("The outer tejas, its source", "बाह्यतेजसा स्वयोनिना योगात्: through union with the outer tejas."),
            [("The cool water of the eye", "No water is named in unit 87; the union is with the outer tejas."),
             ("The Kapha of the eyelids", "Kapha is not named in unit 87; the union is with the outer tejas."),
             ("The blood of the black circle", "Blood is not named in unit 87; the union is with the outer tejas.")],
            "The eye's tejas works through union with the outer tejas, its own source.",
            "बाह्यतेजसा स्वयोनिना योगात् कर्मण्यं भवति."),
        order(1, "Put these phrases of unit 87 in the line's order.",
              ["नेत्राश्रितं तु तेजो", "बाह्यतेजसा स्वयोनिना", "योगाच्छस्त्रमिवाश्मना", "कर्मण्यं भवति", "अतियोगादुपहन्यते"],
              "The tejas in the eye, with the outer tejas its own source, through union, like a weapon with a stone, becomes fit; through excess it is harmed.",
              "नेत्राश्रितं तु तेजो → बाह्यतेजसा स्वयोनिना → योगाच्छस्त्रमिवाश्मना → कर्मण्यं भवति → अतियोगादुपहन्यते."),
        match(2, "Match each word of unit 87 to its meaning.",
              [["बाह्य", "outer"], ["स्वयोनि", "its own source"], ["शस्त्र", "weapon"], ["अश्मन्", "stone"],
               ["कर्मण्य", "fit for its work"], ["उपहन्यते", "is harmed"]],
              "Union with the outer tejas makes it fit, like a weapon with a stone; excess harms it.",
              "बाह्य, स्वयोनि, शस्त्र, अश्मन्, कर्मण्य, उपहन्यते.", role="extend",
              teaches="योग = union, proper contact; अतियोग = excessive union: the same contact that helps, in excess, harms."),
        mcq("discriminate", 3, "Which split of योगाच्छस्त्रम् in unit 87 is right?",
            ("योगात् + शस्त्रम्", "त् before श becomes च्, and श after it is written छ: योगाच्छस्त्रम्."),
            [("योगाः + शस्त्रम्", "A visarga before श would give योगाः शस्त्रम् or योगाश्शस्त्रम्, not च्छ."),
             ("योगम् + शस्त्रम्", "म् before श would give योगं शस्त्रम्, not च्छ."),
             ("योगात् + छस्त्रम्", "छस्त्रम् is not a word; the word is शस्त्रम् (weapon).")],
            "योगात् (through union) + शस्त्रम् (weapon) = योगाच्छस्त्रम्.",
            "त् + श → च्छ (the usual written form)."),
        multi("apply", 4, "Which statements about unit 87 are right by the card?",
              [("The eye's tejas rests in the eye", "Right: नेत्राश्रितं तेजः."),
               ("The stone is known to be a whetstone", "The data: probably a whetstone, but the Sanskrit says only stone."),
               ("Excessive union harms the tejas", "Right: अतियोगादुपहन्यते."),
               ("Union with the outer tejas makes it fit", "Right: बाह्यतेजसा ... योगात् कर्मण्यं भवति.")],
              [0, 2, 3],
              "Union with its source makes the eye's tejas fit; excess harms it; the stone is only a stone.",
              "योगात् कर्मण्यं भवति; अतियोगादुपहन्यते."),
        mcq("transfer", 5, "By the rule of योगाच्छस्त्रम्, how is तत् + शरीरम् (that body) usually written?",
            ("तच्छरीरम्", "त् before श becomes च् and the श is written छ, as योगात् + शस्त्रम्."),
            [("तद्शरीरम्", "द् is taken before a voiced sound; श is unvoiced."),
             ("तत्शरीरम्", "Before श the त् does not stay; it becomes च्."),
             ("तश्शरीरम्", "श् comes from a visarga, not from त्.")],
            "तत् + शरीरम् = तच्छरीरम्, like योगात् + शस्त्रम् = योगाच्छस्त्रम्.",
            "त् + श → च्छ (usual form).",
            teaches="A final त् before श becomes च्, and the श after it is usually written छ: योगात् + शस्त्रम् → योगाच्छस्त्रम्."),
    ],
}

# ---------------------------------------------------------------- unit 88
AUTHORED["88"] = {
    "title": "तच्च वैद्युतवद्वडवामुखवच्च",
    "question": "By unit 88, why does the eye's tejas keep its fiery nature even in water?",
    "rule": ("That (tejas), like lightning (वैद्युत) and like the vaḍavāmukha (the submarine fire), even when in the midst of "
             "water (अम्भोमध्यग), does not abandon its fiery nature (तेजस्त्व), because of the excellence of its vīrya "
             "(potency, वीर्योत्कर्ष)."),
    "limits": ("A prose line. तत् is taken as the tejas of unit 87. What water surrounds the eye's tejas is not stated. "
               "The vaḍavāmukha is the fire said in Sanskrit literature to burn under the ocean; no more is claimed."),
    "explain_hi": ("यह गद्य-पंक्ति कहती है: वह तेज, बिजली की तरह और वड़वामुख यानी समुद्र के भीतर जलने वाली अग्नि की तरह, "
                   "जल के बीच में रहकर भी अपना तेजत्व नहीं छोड़ता। "
                   "कारण है वीर्य, यानी शक्ति, की प्रबलता (वीर्योत्कर्ष)। "
                   "‘तत्’ इकाई ८७ के नेत्र-तेज को कहता है। "
                   "छपा ‘वीर्य्यो’ में दोहरा य् छपाई की आदत है।"),
    "hook": "बिजली और वड़वाग्नि जैसा: जल में भी तेज बना रहे।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 88, why does the tejas not abandon its fiery nature in water?",
            ("The excellence of its vīrya", "वीर्योत्कर्षात्: because of the excellence of its potency."),
            [("Because it stays far from all water", "It is even in the midst of water: अम्भोमध्यगमपि."),
             ("Because Kapha shields it from water", "Kapha is not named in unit 88; the cause is vīrya."),
             ("Because the mind keeps it burning", "The mind is not named in unit 88; the cause is vīrya.")],
            "Its potency (vīrya) is so strong that it keeps its fiery nature.",
            "वीर्योत्कर्षात् तेजस्त्वं न जहाति."),
        order(1, "Put these phrases of unit 88 in the line's order.",
              ["तच्च", "वैद्युतवद्", "वडवामुखवच्च", "अम्भोमध्यगमपि", "वीर्योत्कर्षात्", "तेजस्त्वं न जहाति"],
              "And that, like lightning, and like the vaḍavāmukha, even in the midst of water, from the excellence of vīrya, does not abandon its fiery nature.",
              "तच्च → वैद्युतवद् → वडवामुखवच्च → अम्भोमध्यगमपि → वीर्योत्कर्षात् → तेजस्त्वं न जहाति."),
        match(2, "Match each word of unit 88 to its meaning.",
              [["वैद्युत", "of lightning"], ["वडवामुख", "the submarine fire"], ["अम्भस्", "water"], ["वीर्य", "potency"],
               ["जहाति", "abandons"]],
              "Like lightning and the submarine fire, even in water it keeps its fire by the strength of its vīrya.",
              "वैद्युत, वडवामुख, अम्भस्, वीर्य, जहाति.", role="extend",
              teaches="-वत् = like: वैद्युतवत् = like lightning, वडवामुखवत् = like the submarine fire."),
        mcq("discriminate", 3, "Which split of वीर्योत्कर्षात् in unit 88 is right?",
            ("वीर्य + उत्कर्षात्", "अ + उ → ओ: वीर्य + उत्कर्षात् → वीर्योत्कर्षात्."),
            [("वीर्यः + उत्कर्षात्", "अः before उ loses its visarga and the vowels stay apart: वीर्य उत्कर्षात्."),
             ("वीर्यो + त्कर्षात्", "त्कर्षात् is not a word; the word is उत्कर्षात् (from excellence)."),
             ("वीर्य + ओत्कर्षात्", "ओत्कर्षात् is not a word, and अ + ओ would give औ.")],
            "वीर्य (potency) + उत्कर्षात् (from the excellence): अ + उ → ओ.",
            "अ + उ → ओ."),
        mcq("apply", 4, "By unit 88, what do lightning and the vaḍavāmukha share with the eye's tejas?",
            ("They stay fire amid water", "Like them, even in the midst of water, it does not abandon its fiery nature."),
            [("Water puts them out at once", "The point is the opposite: they keep their fire in water."),
             ("They burn only in dry places", "They are fires in the midst of water: अम्भोमध्यगम् अपि."),
             ("They give light only by day", "Day and night are not named in unit 88.")],
            "Lightning, the submarine fire and the eye's tejas: fire that keeps its nature amid water.",
            "अम्भोमध्यगम् अपि तेजस्त्वं न जहाति."),
        mcq("transfer", 5, "By the rule of वीर्योत्कर्षात् (वीर्य + उत्कर्षात्), how is हित + उपदेशः (good advice) joined?",
            ("हितोपदेशः", "अ + उ → ओ, as वीर्य + उत्कर्षात् → वीर्योत्कर्षात्."),
            [("हितौपदेशः", "औ comes from अ + ओ or औ, not from अ + उ."),
             ("हितूपदेशः", "ऊ comes from उ + उ, not from अ + उ."),
             ("हितेपदेशः", "ए comes from अ + इ, not from अ + उ.")],
            "हित + उपदेशः = हितोपदेशः, like वीर्य + उत्कर्षात् = वीर्योत्कर्षात्.",
            "अ + उ → ओ.",
            teaches="A short अ followed by उ joins as ओ: वीर्य + उत्कर्षात् → वीर्योत्कर्षात्."),
    ],
}

# ---------------------------------------------------------------- unit 89
AUTHORED["89"] = {
    "title": "मांसासृक्कफप्रसादात्तु जिव्हा जायते",
    "question": "By unit 89, from what do the tongue and the testes arise?",
    "rule": ("From the clear essence (प्रसाद) of flesh, blood and Kapha the tongue (जिह्वा) arises; from the clear essence "
             "of flesh, blood, Kapha and fat (मेदस्), the two testes (वृषण)."),
    "limits": ("Two prose lines. The verb arise (जायेते) for the testes is carried from the first line and not printed. "
               "Printed जिव्हा is the letter-reversed spelling of जिह्वा. प्रसाद is kept literal (the clear, finest part); "
               "no amount or proportion is given."),
    "explain_hi": ("ये दो गद्य-पंक्तियाँ बताती हैं: मांस, रक्त और कफ के प्रसाद, यानी स्वच्छ सार अंश, से जिह्वा उत्पन्न होती है। "
                   "मांस, रक्त, कफ और मेद के प्रसाद से दोनों वृषण, यानी अण्डकोश के गोलक, बनते हैं। "
                   "दोनों सूचियों में अन्तर केवल मेद का है, जो वृषणों की सूची में अधिक है। "
                   "दूसरी पंक्ति में क्रिया पहली पंक्ति से समझी जाती है। "
                   "छपा ‘जिव्हा’ ‘जिह्वा’ का उलटे अक्षरों वाला रूप है।"),
    "hook": "मांस-रक्त-कफ से जीभ; उसमें मेद जोड़ो तो वृषण।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 89, from the clear essence of what does the tongue arise?",
            ("Flesh, blood and Kapha", "मांसासृक्कफप्रसादात् जिह्वा जायते."),
            [("Flesh, blood, Kapha and fat", "That longer list, with fat, is for the testes."),
             ("Pitta, Vāta and bone", "None of these is named for the tongue in unit 89."),
             ("Kapha and fat alone", "Fat is not in the tongue's list; flesh and blood are.")],
            "The tongue arises from the prasāda of flesh, blood and Kapha.",
            "मांसासृक्कफप्रसादात् तु जिह्वा जायते."),
        order(1, "Put the four sources of the testes in unit 89 in the line's order.",
              ["मांस", "असृक्", "कफ", "मेदस्"],
              "Flesh, blood, Kapha, fat.",
              "मांस → असृक् → कफ → मेदस्."),
        match(2, "Match each word of unit 89 to its meaning.",
              [["मांस", "flesh"], ["असृज्", "blood"], ["प्रसाद", "clear essence"], ["जिह्वा", "tongue"],
               ["वृषण", "testis"], ["जायते", "arises, is born"]],
              "From the clear essence of flesh, blood and Kapha the tongue arises; with fat added, the testes.",
              "मांस, असृज्, प्रसाद, जिह्वा, वृषण, जायते.", role="extend",
              teaches="प्रसाद = the clear, finest part of a substance; organs are said to arise from the prasāda of tissues."),
        mcq("discriminate", 3, "By unit 89, which source is in the testes' list but not in the tongue's?",
            ("Fat (मेदस्)", "The testes' list adds मेदः: मांसासृक्कफमेदःप्रसादात्."),
            [("Flesh (मांस)", "Flesh is in both lists."),
             ("Blood (असृज्)", "Blood is in both lists."),
             ("Kapha (कफ)", "Kapha is in both lists.")],
            "The only difference between the two lists is fat (medas).",
            "जिह्वा: मांस, असृक्, कफ · वृषणौ: + मेदस्."),
        mcq("apply", 4, "Which split of वृषणाविति in unit 89 is right?",
            ("वृषणौ + इति", "औ before a vowel becomes आव्: वृषणौ + इति → वृषणाविति."),
            [("वृषणा + विति", "विति is not a word; the व् comes from the औ of वृषणौ."),
             ("वृषणः + इति", "अः + इ would give वृषण इति, and the data reads the dual वृषणौ."),
             ("वृषणम् + इति", "म् + इ would give वृषणमिति, with म्, not व्.")],
            "वृषणौ (the two testes) + इति (thus): औ + vowel → आव्.",
            "औ + vowel → आव्."),
        mcq("transfer", 5, "By the rule of वृषणाविति, how is बालौ + इति (the two boys, thus) joined in one word?",
            ("बालाविति", "औ before a vowel becomes आव्, as वृषणौ + इति → वृषणाविति."),
            [("बालौति", "औ is not kept before a vowel; it becomes आव्."),
             ("बालेति", "ए comes from अ/आ + इ; here the vowel is औ."),
             ("बालविति", "औ gives आव् with long आ; अव् comes from ओ.")],
            "बालौ + इति = बालाविति, like वृषणौ + इति = वृषणाविति.",
            "औ + vowel → आव्.",
            teaches="A final औ before a vowel becomes आव्: वृषणौ + इति → वृषणाविति."),
    ],
}


# ===================================================================== NOTES_HI
NOTES_HI = {
    "77": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। क्रिया ‘बनता है’ पिछली इकाइयों से समझी जाती है। कृष्णमण्डल = आँख का काला भाग और "
           "दृष्टिमण्डल = पुतली का क्षेत्र, दोनों सम्भावित। ‘उभय’ = सम्भवतः पितृज और मातृज, पर पंक्ति स्पष्ट नहीं कहती। ‘असृजः’ षष्ठी "
           "(रक्त का) या पंचमी (रक्त से) दोनों रूपों में एक-सा है; आँकड़ों में षष्ठी लिखा है, अनुवाद ‘रक्त से’। सन्धि जाँची: तत् + मातृजम् → "
           "तन्मातृजम् (म से पहले त् का न्); तत् + उभयात्मकम् → तदुभयात्मकम् (स्वर से पहले त् → द्); उभय + आत्मक → उभयात्मक (अ + आ → आ); "
           "मण्डलम् का म् व्यंजन से पहले ं।"),
    "78": ("गद्य; विश्वास मध्यम। पाठ-चिह्न: छपा ‘दृष्ट्यास्यानि’ (मुख) अर्थ नहीं देता और छठा नाम बना देता; अनुमानित पाठ ‘दृष्ट्याख्यानि’ "
           "(नाम वाले) लिया गया (ख/स की छपाई-भूल सम्भव)। इस शब्द पर कोई प्रश्न नहीं। सन्धि जाँची: दृष्टि + आ... → दृष्ट्या... (इ + भिन्न "
           "स्वर → य्), जो दोनों पाठों में एक-सा है। ‘है’ क्रिया समझी जाती है।"),
    "79": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। ‘तत्-’ इकाई ७८ के पाँच मण्डलों को कहता है। ‘सन्धि’ यहाँ मण्डलों का जोड़ है। "
           "छपाई में ‘तत्संधयश्चत्वारः’ एक साथ। सन्धि जाँची: तत् + सन्धयः → तत्सन्धयः (अघोष स से पहले त् बना रहता); सन्धयः + चत्वारः → "
           "सन्धयश्चत्वारः (च से पहले विसर्ग → श्)।"),
    "80": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। गिनी जा रही संज्ञा इस इकाई में नहीं है और जोड़ी नहीं गई; आँकड़ों के अनुसार यह "
           "पिछली इकाई (७९) को आगे बढ़ाती लगती है। कनीन = भीतरी कोना (सम्भावित; पुतली भी सम्भव)। ‘-नयोः’ सप्तमी लिया गया, षष्ठी भी "
           "सम्भव; इस पर प्रश्न नहीं। सन्धि जाँची: च + अपाङ्ग → चापाङ्ग (अ + अ → आ); छपा ‘चापांग’ में ं = ङ्।"),
    "81": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। ‘ते’ (पुं. प्रथमा बहुवचन) इकाई ७९-८० में गिनी वस्तुओं की ओर संकेत करता है; "
           "आँकड़ों के अनुसार यह गिनती (चार + दो = छह) पूरी करती लगती है। ‘हैं’ क्रिया समझी जाती है। कोई सन्धि-परिवर्तन नहीं।"),
    "82": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। क्रिया नहीं दी गई। पटल = परत; आँख का नाम इस पंक्ति में नहीं, प्रसंग से आँख के पटल। "
           "सन्धि जाँची: षट् + च → षट् च (अघोष च से पहले ट् बना रहता)।"),
    "83": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। क्रिया नहीं दी गई। वर्त्मन् = पलक (नेत्र-प्रसंग में मानक); इसका अर्थ ‘मार्ग’ भी है। "
           "द्वे, वर्त्मनी: नपुंसक प्रथमा द्विवचन। छह पटलों से सम्बन्ध पंक्ति में नहीं कहा गया। कोई सन्धि-परिवर्तन नहीं।"),
    "84": ("गद्य; विश्वास कम। पाठ-चिह्न: ‘मांसं.तृतीयं’ का बिन्दु सम्भवतः रिक्त स्थान या लुप्त विराम है। संज्ञा नहीं दी गई (सम्भवतः पटल)। "
           "पहला अंश ‘बाह्यं चाश्रितमग्न्यंभसीद्वितीयं’ = च आश्रितम् अग्नि-अम्भसी द्वितीयम्, विभाग केवल सम्भावित, और अर्थ (एक वस्तु के दो "
           "वर्णन या दो वस्तुएँ) तय नहीं; इस पर कोई प्रश्न नहीं। ‘दृष्टेः पञ्चमांशेन’ शाब्दिक रखा गया, व्याख्या नहीं। सन्धि जाँची: च + आश्रितम् "
           "→ चाश्रितम् (अ + आ → आ); अग्नि + अम्भसी → अग्न्यम्भसी (इ + अ → य); मेदः + चतुर्थम् → मेदश्चतुर्थम् (च से पहले विसर्ग → श्); "
           "चतुर्थम् + अस्थि → चतुर्थमस्थि; पञ्चम + अंशेन → पञ्चमांशेन (अ + अ → आ)।"),
    "85": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। ‘गुण’ = रज्जु, डोरी पढ़ा गया; ‘विशेषता’ अर्थ सम्भव पर नहीं अपनाया; इस पर प्रश्न नहीं। "
           "सिरा = नस, वाहिका (मानक); कण्डरा = मोटा स्नायु-रज्जु (मानक)। सन्धि जाँची: बन्धनगुणाः + तु → बन्धनगुणास्तु (त से पहले विसर्ग → स्); "
           "कफ + आत्मकाः → कफात्मकाः (अ + आ → आ); समास में ‘मेदः’ का विसर्ग क से पहले छपा रहा।"),
    "86": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। छपा ‘परंसर्वसंधिबंधनम्’ में परम् और सर्व जुड़े छपे हैं (रिक्त स्थान की चूक)। ‘परम्’ = "
           "परम, मुख्य; ‘आगे’ अर्थ भी सम्भव; इस पर प्रश्न नहीं। पहले कहाँ कहा गया, यह यहाँ नहीं मिलता। सन्धि जाँची: बन्धनम् + इति → "
           "बन्धनमिति; इति + उक्तम् → इत्युक्तम् (इ + उ → यु); उक्तम् + प्राक् → उक्तं प्राक् (व्यंजन से पहले म् → ं)।"),
    "87": ("गद्य; विश्वास मध्यम। पाठ-चिह्न: ‘भवतिःअतियोगा...’ में भवति के बाद का विसर्ग सम्भवतः दण्ड की छपाई-भूल है; दो वाक्य जुड़े छपे हैं। "
           "पत्थर (अश्मन्) सम्भवतः सान का पत्थर, पर संस्कृत केवल ‘पत्थर’ कहती है। सन्धि जाँची: नेत्र + आश्रितम् → नेत्राश्रितम् (अ + आ → आ); "
           "तेजः + बाह्य → तेजो बाह्य (अः + घोष व्यंजन → ओ); योगात् + शस्त्रम् → योगाच्छस्त्रम् (त् + श → च्छ); शस्त्रम् + इव → शस्त्रमिव; "
           "इव + अश्मना → इवाश्मना (अ + अ → आ); अतियोगात् + उपहन्यते → अतियोगादुपहन्यते (स्वर से पहले त् → द्)।"),
    "88": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। ‘तत्’ = इकाई ८७ का नेत्र-तेज। वड़वामुख = समुद्र के नीचे जलने वाली अग्नि (संस्कृत "
           "साहित्य में मानक)। छपा ‘वीर्य्यो’ में दोहरा य् छपाई की आदत। सन्धि जाँची: तत् + च → तच्च (च से पहले त् → च्); वैद्युतवत् + "
           "वडवा... → वैद्युतवद्वडवा... (घोष व से पहले त् → द्); ...वत् + च → ...वच्च; च + अम्भः → चाम्भः (अ + अ → आ); अम्भः + मध्य "
           "→ अम्भोमध्य (अः + घोष → ओ); वीर्य + उत्कर्षात् → वीर्योत्कर्षात् (अ + उ → ओ)।"),
    "89": ("गद्य, दो पंक्तियाँ; विश्वास उच्च। पाठ-चिह्न: छपा ‘जिव्हा’ = जिह्वा (ह्व/व्ह अक्षर-उलट, लगभग निश्चित)। दूसरी पंक्ति में क्रिया "
           "(जायेते) पहली से समझी जाती है; अन्तिम ‘इति’ कथन का अन्त दिखाता है। सन्धि जाँची: मांस + असृक् → मांसासृक् (अ + अ → आ); "
           "असृज् + कफ → असृक्कफ (अघोष क से पहले ज् → क्); प्रसादात् + तु → प्रसादात्तु; प्रसादात् + वृषणौ → प्रसादाद्वृषणौ (घोष व से पहले "
           "त् → द्); वृषणौ + इति → वृषणाविति (औ + स्वर → आव्)।"),
}


# ===================================================================== AIDS
AIDS = {
    "77": {
        "diagram": {"groups": [
            {"label": "कृष्णमण्डल (सम्भवतः काला भाग)", "items": ["रक्त (असृज्) से", "मातृज: माता से उत्पन्न"]},
            {"label": "दृष्टिमण्डल (सम्भवतः पुतली-क्षेत्र)", "items": ["बीच में (मध्ये)", "उभयात्मक: दोनों के स्वभाव वाला"]}]},
        "chunks": "असृजः कृष्णमंडलं | तन्मातृजं | मध्ये दृष्टिमंडलं | तदुभयात्मकं",
        "sandhi": "म से पहले त् का न्: तत् + मातृजम् → तन्मातृजम् · स्वर से पहले त् → द्: तत् + उभयात्मकम् → तदुभयात्मकम्।",
    },
    "78": {
        "chain": {"steps": ["१ पक्ष्म (पलक के बाल)", "२ वर्त्म (पलक)", "३ शुक्ल (सफेद)", "४ कृष्ण (काला)", "५ दृष्टि"]},
        "chunks": "पक्ष्म | वर्त्म | शुक्ल | कृष्ण | दृष्ट्यास्यानि (अनुमानित: दृष्ट्याख्यानि) | पंच मंडलानि",
        "letters": "पहले अक्षर क्रम से: प-व-शु-कृ-दृ (पक्ष्म, वर्त्म, शुक्ल, कृष्ण, दृष्टि)। (मेरी याद-पद्धति)",
    },
    "79": {
        "sandhi": "च से पहले विसर्ग → श्: सन्धयः + चत्वारः → सन्धयश्चत्वारः।",
        "frame": "किसकी: तत् (पाँच मण्डलों की) → क्या: सन्धयः (जोड़) → कितनी: चत्वारः (चार)।",
        "anchors": "याद-सूत्र: पाँच मण्डल, बीच में चार जोड़, जैसे पाँच उँगलियों के बीच चार खाँचे। (मेरा बनाया चित्र, पाठ का दावा नहीं)",
    },
    "80": {
        "sandhi": "अ + अ → आ: च + अपाङ्ग → चापाङ्ग।",
        "frame": "कितने: द्वौ (दो) → कहाँ: अपाङ्ग (बाहरी कोना) और कनीन (सम्भवतः भीतरी कोना) → क्या: नाम इस इकाई में नहीं।",
        "anchors": "याद-सूत्र: आँख के दोनों सिरों पर एक-एक: अपांग बाहर, कनीन (सम्भवतः) भीतर। (मेरी याद-पद्धति)",
    },
    "81": {
        "frame": "इति (इस प्रकार) → ते (वे, पहले गिनी वस्तुएँ) → षट् (छह)।",
        "anchors": "याद-सूत्र: इकाई ७९ की चार + इकाई ८० की दो = इति ते षट्। (आँकड़ों का पाठ: ‘गिनती पूरी करती लगती है’)",
    },
    "82": {
        "frame": "कितने: षट् (छह) → और: च → क्या: पटलानि (परतें; प्रसंग से आँख की)।",
        "sandhi": "अघोष च से पहले ट् बना रहता: षट् च · स्वर या घोष से पहले ट् → ड्: षडङ्गानि (नया उदाहरण)।",
    },
    "83": {
        "frame": "कितनी: द्वे (दो, नपुंसक) → क्या: वर्त्मनी (पलकें, नपुंसक द्विवचन)।",
        "contrast": "वर्त्मन् के दो अर्थ: नेत्र-प्रसंग में पलक; अन्यत्र मार्ग। यहाँ पलक।",
        "anchors": "याद-सूत्र: वर्त्म = मार्ग भी; पलक आँख का द्वार-मार्ग। (मेरी याद-पद्धति, पाठ का दावा नहीं)",
    },
    "84": {
        "chain": {"steps": ["(पहला अंश: बाहरी, अग्नि-जल पर आश्रित; अनिश्चित)", "द्वितीय: मांस", "तृतीय: मेद (चर्बी)",
                            "चतुर्थ: अस्थि (हड्डी)"]},
        "chunks": "बाह्यं चाश्रितमग्न्यंभसी | द्वितीयं मांसं | तृतीयं मेदः | चतुर्थमस्थि | तेषां बहुलता दृष्टेः पंचमांशेन",
        "sandhi": "च से पहले विसर्ग → श्: मेदः + चतुर्थम् → मेदश्चतुर्थम् · स्वर से पहले म्: चतुर्थम् + अस्थि → चतुर्थमस्थि।",
    },
    "85": {
        "diagram": {"groups": [
            {"label": "चार बन्धनगुण, स्वरूप (क्रम से)", "items": ["१ सिरा (नस, वाहिका)", "२ कण्डरा (मोटा स्नायु-रज्जु)",
                                                            "३ मेद (चर्बी)", "४ कफ"]}]},
        "chunks": "बंधनगुणास्तु चत्वारः | सिराकंडरामेदःकफात्मकाः",
        "sandhi": "त से पहले विसर्ग → स्: बन्धनगुणाः + तु → बन्धनगुणास्तु।",
        "letters": "पहले अक्षर क्रम से: सि-क-मे-क (सिरा, कण्डरा, मेद, कफ)। (मेरी याद-पद्धति)",
    },
    "86": {
        "chunks": "श्लेष्मा तु | परं सर्वसंधिबंधनम् | इत्युक्तं प्राक्",
        "sandhi": "इ + भिन्न स्वर → य्: इति + उक्तम् → इत्युक्तम्।",
        "frame": "कौन: श्लेष्मा (कफ) → क्या: परं सर्वसन्धिबन्धनम् (सब जोड़ों का मुख्य बन्धन) → स्रोत: इत्युक्तं प्राक् (पहले कहा गया)।",
    },
    "87": {
        "chain": {"steps": ["नेत्र में आश्रित तेज", "बाहरी तेज (अपना उद्गम) से योग", "कर्म के योग्य (जैसे शस्त्र पत्थर से)",
                            "अतियोग से क्षति"]},
        "contrast": "योग ↔ अतियोग: बाहरी तेज से उचित योग आँख के तेज को कर्मण्य बनाता है; अतियोग उसे उपहत करता है।",
        "sandhi": "त् + श → च्छ: योगात् + शस्त्रम् → योगाच्छस्त्रम् · अ + अ → आ: इव + अश्मना → इवाश्मना।",
        "story": "शस्त्र पत्थर पर घिसकर काम का बनता है; बहुत घिसो तो धार ही घिस जाती है। (मेरा बनाया चित्र; पाठ केवल शस्त्र और पत्थर कहता है)",
    },
    "88": {
        "chunks": "तच्च | वैद्युतवद् | वडवामुखवच्च | अम्भोमध्यगमपि | वीर्योत्कर्षात् | तेजस्त्वं न जहाति",
        "sandhi": "अ + उ → ओ: वीर्य + उत्कर्षात् → वीर्योत्कर्षात् · घोष व से पहले त् → द्: वैद्युतवत् + वडवा → वैद्युतवद्वडवा।",
        "frame": "उपमा: बिजली, वड़वामुख → स्थिति: जल के बीच में भी → कारण: वीर्य की प्रबलता → फल: तेजत्व नहीं छोड़ता।",
    },
    "89": {
        "contrast": "जिह्वा: मांस, रक्त, कफ का प्रसाद ↔ वृषण: मांस, रक्त, कफ और मेद का प्रसाद। अन्तर केवल मेद।",
        "chunks": "मांसासृक्कफप्रसादात्तु | जिव्हा जायते | मांसासृक्कफमेदःप्रसादाद् | वृषणाविति",
        "sandhi": "औ + स्वर → आव्: वृषणौ + इति → वृषणाविति · घोष व से पहले त् → द्: प्रसादात् + वृषणौ → प्रसादाद्वृषणौ।",
    },
}


# ===================================================================== IMAGE_SPECS
IMAGE_SPECS = {
    ("77", "diagram"): {
        "file": "sh5-krishna-drishti-mandala-77.svg",
        "alt": ("Table of unit 77: kṛṣṇa-maṇḍala (black circle, probably the dark part of the eye) comes from blood and is "
                "born from the mother; dṛṣṭi-maṇḍala (circle of sight, probably the pupil region) lies in the middle and has "
                "the nature of both."),
        "type": "table",
        "title": "इकाई ७७: दो मण्डल",
        "heads": ["मण्डल", "पाठ क्या कहता है"],
        "rows": [["कृष्णमण्डल (सम्भवतः काला भाग)", "रक्त से; माता से उत्पन्न"],
                 ["दृष्टिमण्डल (सम्भवतः पुतली-क्षेत्र)", "बीच में; दोनों के स्वभाव वाला"]],
    },
    ("78", "chain"): {
        "file": "sh5-pancha-mandala-78.svg",
        "alt": ("Numbered chain of unit 78, the five maṇḍalas of the eye in line order: 1 pakṣma (eyelashes), 2 vartma "
                "(eyelid), 3 śukla (white), 4 kṛṣṇa (black), 5 dṛṣṭi (sight)."),
        "type": "chain",
        "title": "इकाई ७८: पाँच मण्डल (क्रम से)",
        "steps": ["१ पक्ष्म (पलक के बाल)", "२ वर्त्म (पलक)", "३ शुक्ल (सफेद)", "४ कृष्ण (काला)", "५ दृष्टि"],
    },
    ("85", "diagram"): {
        "file": "sh5-bandhana-guna-85.svg",
        "alt": ("Numbered table of unit 85, the four binding strands by nature in line order: 1 sirā (vein, vessel), "
                "2 kaṇḍarā (large tendon), 3 medas (fat), 4 Kapha."),
        "type": "table",
        "title": "इकाई ८५: चार बन्धनगुण",
        "heads": ["क्रम", "स्वरूप"],
        "rows": [["१", "सिरा (नस, वाहिका)"], ["२", "कण्डरा (मोटा स्नायु-रज्जु)"], ["३", "मेद (चर्बी)"], ["४", "कफ"]],
    },
    ("87", "chain"): {
        "file": "sh5-netra-tejas-87.svg",
        "alt": ("Flowchart of unit 87: the tejas resting in the eye, through union with the outer tejas (its own source), "
                "becomes fit for its work, like a weapon with a stone; through excessive union it is harmed."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"नेत्र में आश्रित तेज\"] --> B[\"बाहरी तेज से योग\"]\n"
                 "  A --> C[\"बाहरी तेज से अतियोग\"]\n"
                 "  B --> D[\"कर्म के योग्य\"]\n"
                 "  C --> E[\"क्षति (उपहत)\"]\n"
                 "  D -.- F[\"जैसे शस्त्र पत्थर से\"]\n"),
    },
    ("89", "contrast"): {
        "file": "sh5-jihva-vrishana-89.svg",
        "alt": ("Two columns of unit 89. Tongue (jihvā): from the clear essence of flesh, blood, Kapha. Two testes (vṛṣaṇa): "
                "from the clear essence of flesh, blood, Kapha and fat; fat is the only difference."),
        "type": "split",
        "title": "इकाई ८९: प्रसाद से अंग",
        "cols": [["जिह्वा", ["मांस", "रक्त", "कफ"]],
                 ["दोनों वृषण", ["मांस", "रक्त", "कफ", "मेद (केवल यहाँ)"]]],
    },
}
