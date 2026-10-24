from helpers import mcq, match, order, fill, multi, accepts


AUTHORED = {}

# ---------------------------------------------------------------- unit 26
AUTHORED["26"] = {
    "title": "तत्र सत्वं मनः",
    "question": "By unit 26, what is sattva said to be?",
    "rule": "Among these, sattva is the mind (मनस्). The verb 'is' is not written; it is understood.",
    "limits": ("A short prose line with no verb. It does not say what 'these' (तत्र) are, nor how sattva and the mind "
               "relate beyond naming one as the other. The print writes सत्वं; the data reads सत्त्वम्."),
    "explain_hi": ("यह छोटी गद्य-पंक्ति कहती है: उनमें सत्त्व मन है (तत्र सत्त्वं मनः)। "
                   "‘है’ क्रिया लिखी नहीं गई, समझी जाती है। "
                   "छपाई में ‘सत्वं’ है; data इसे सत्त्वम् पढ़ता है। "
                   "‘तत्र’ (उनमें) किन्हें कहता है, यह पंक्ति स्वयं नहीं बताती। "
                   "अगली इकाई (२७) इसी सत्त्व के उपप्लव की बात करती है।"),
    "hook": "सत्त्व = मन: तीन शब्द, एक पहचान।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 26, what is sattva said to be?",
            ("The mind (manas)", "तत्र सत्त्वं मनः: among these, sattva is the mind."),
            [("The body (deha)", "Unit 26 does not name the body; unit 28 calls the body bhūtātmaka."),
             ("The skin (tvac)", "The skins come later, from unit 31; unit 26 does not name them."),
             ("The life-breath (prāṇa)", "Prāṇa is not named in unit 26.")],
            "Sattva is the mind: सत्त्वं मनः.",
            "तत्र सत्त्वं मनः = among these, sattva is the mind."),
        order(1, "Put the words of unit 26 in the line's order.",
              ["तत्र", "सत्वं", "मनः"],
              "Among these, sattva, (is) the mind.",
              "तत्र → सत्वं → मनः."),
        fill(2, "तत्र सत्वं ____: type the word for 'mind' in Devanagari or in English letters (e.g. dharma).",
             accepts("मनः", None, "मनस्"),
             "तत्र सत्त्वं मनः: the last word, मनः, is the mind (nominative of मनस्).",
             "मनस् (n.) = mind; its nominative singular is मनः. Unit 26 names sattva as the mind.",
             "सत्त्वम् = मनः."),
        mcq("discriminate", 3, "In unit 26, how is the verb 'is' given?",
            ("It is not written but understood", "The data notes: copula understood."),
            [("By तत्र, which here means 'is'", "तत्र is an indeclinable: 'among these'."),
             ("By मनः, which is a verb form", "मनः is a noun, the mind, neuter nominative singular."),
             ("By सत्वं, a present-tense verb", "सत्त्वम् is a noun, neuter nominative singular.")],
            "No verb is written; 'is' is understood between सत्त्वम् and मनः.",
            "Sanskrit often leaves 'is' unwritten: सत्त्वं मनः = sattva (is) the mind."),
        multi("apply", 4, "Which statements about unit 26 are right by the card?",
              [("Sattva is named as the mind", "Right: सत्त्वं मनः."),
               ("Rajas is named as the mind", "Unit 26 names sattva, not rajas."),
               ("It says the mind is made of the elements", "Unit 26 says nothing about what the mind is made of."),
               ("The verb 'is' is understood, not written", "Right: the data notes the copula is understood.")],
              [0, 3],
              "Sattva is the mind; the verb is understood.",
              "तत्र सत्त्वं मनः."),
        mcq("transfer", 5, "By the rule of सत्वं मनः, how is फलम् + ददाति (gives fruit) written in a new example?",
            ("फलं ददाति", "Inside a sentence a final म् before a consonant is written ं, as सत्त्वम् + मनः → सत्त्वं मनः."),
            [("फलो ददाति", "ओ comes from a visarga after अ, not from a final म्."),
             ("फला ददाति", "A final म् is not simply dropped before a consonant."),
             ("फलर्ददाति", "र् comes from a visarga after vowels other than अ/आ, not from म्.")],
            "फलम् + ददाति = फलं ददाति, like सत्त्वम् + मनः = सत्त्वं मनः.",
            "Final म् + consonant (inside a sentence) → ं.",
            teaches="Inside a sentence a word-final म् before a consonant is written as anusvāra: सत्त्वम् + मनः → सत्त्वं मनः."),
    ],
}

# ---------------------------------------------------------------- unit 27
AUTHORED["27"] = {
    "title": "तस्योपप्लवो रजस्तमश्चेति",
    "question": "By unit 27, what is the disturbance (upaplava) of sattva, the mind?",
    "rule": ("Its (sattva's, the mind's) disturbance or affliction (उपप्लव) is rajas and tamas. "
             "The closing इति marks the end of the statement."),
    "limits": ("A short prose line; the verb is understood. It does not say how rajas and tamas disturb the mind or what "
               "follows from it. 'Its' (तस्य) refers to sattva, the mind of unit 26, by the data's notes."),
    "explain_hi": ("यह गद्य-पंक्ति कहती है: उसका उपप्लव यानी उपद्रव रजस् और तमस् है। "
                   "‘तस्य’ (उसका) इकाई २६ के सत्त्व यानी मन की ओर संकेत करता है। "
                   "रजस् और तमस् वे दो गुण हैं जिनसे जुड़े भाव इकाई २४ और २५ में गिनाए गए। "
                   "अन्त का ‘इति’ कथन की समाप्ति दिखाता है; अनुवाद में नहीं आता। "
                   "रजस्-तमस् मन को कैसे बिगाड़ते हैं, यह पंक्ति नहीं बताती।"),
    "hook": "मन सत्त्व है; रजस्-तमस् उसके उपद्रव।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 27, what is the disturbance (upaplava) of sattva, the mind?",
            ("Rajas and tamas", "रजस्तमश्च: rajas and tamas."),
            [("Vāta and kapha", "These are doṣas of the body; unit 27 names rajas and tamas."),
             ("Space and wind", "These are elements; unit 27 does not name them."),
             ("Sattva and rajas", "Sattva is the mind itself; its disturbance is rajas and tamas.")],
            "Its disturbance is rajas and tamas.",
            "तस्य उपप्लवः रजः तमः च."),
        order(1, "Put the words of unit 27 in the line's order.",
              ["तस्य", "उपप्लवः", "रजः", "तमः", "च इति"],
              "Its disturbance (is) rajas and tamas: thus.",
              "तस्य → उपप्लवः → रजः → तमः → च इति."),
        match(2, "Match each word of unit 27 to its meaning.",
              [["तस्य", "of it (of sattva, the mind)"], ["उपप्लव", "disturbance, affliction"],
               ["च", "and"], ["इति", "thus (ends the statement)"]],
              "Of it, the disturbance, rajas and tamas, and, thus.",
              "तस्य, उपप्लव, च, इति.", role="extend",
              teaches="उपप्लव = disturbance or affliction; unit 27 gives rajas and tamas as that of sattva, the mind."),
        mcq("discriminate", 3, "Which split of तस्योपप्लवो is right?",
            ("तस्य + उपप्लवः", "अ + उ → ओ: तस्य + उपप्लवः → तस्योपप्लवः."),
            [("तस्य + ओपप्लवः", "ओपप्लव is not a word; the word is उपप्लव."),
             ("तस्यो + पप्लवः", "तस्यो and पप्लव are not words here."),
             ("तस्याः + उपप्लवः", "तस्याः + उ would stay apart as तस्या उपप्लवः.")],
            "तस्य (of it) + उपप्लवः (disturbance): अ + उ → ओ.",
            "अ + उ → ओ."),
        mcq("apply", 4, "Why is उपप्लवः written उपप्लवो before रजः in unit 27?",
            ("अः before a voiced sound becomes ओ", "र is voiced: उपप्लवः + रजः → उपप्लवो रजः."),
            [("अः before any consonant becomes ओ", "Before an unvoiced sound such as त or प it does not become ओ."),
             ("ओ is the ending of a dual noun", "उपप्लवः is singular; ओ comes from the visarga rule."),
             ("अः before a vowel becomes ओ here", "रजः begins with र, a consonant, not a vowel.")],
            "अः + voiced sound → ओ: उपप्लवो रजः.",
            "अः + voiced sound → ओ."),
        mcq("transfer", 5, "By the rule of तमश्च, how is रामः + च (and Rāma) joined in a new example?",
            ("रामश्च", "A visarga before च becomes श्, as तमः + च → तमश्च."),
            [("रामो च", "ओ comes before a voiced sound; च is unvoiced."),
             ("रामस्च", "स् comes before त or थ, not before च."),
             ("रामर्च", "र् comes after vowels other than अ/आ, and only before a voiced sound.")],
            "रामः + च = रामश्च, like तमः + च = तमश्च.",
            "Visarga + च → श्च.",
            teaches="A visarga before च or छ becomes श्: तमः + च → तमश्च."),
    ],
}

# ---------------------------------------------------------------- unit 28
AUTHORED["28"] = {
    "title": "एवं भूतात्मकं देहमाहुः",
    "question": "By unit 28, what do they call the body?",
    "rule": "Thus they call the body (देह) bhūtātmaka: consisting of the elements (भूत). आहुः = they say, they call.",
    "limits": ("A prose line. 'They' are not named. It gives no list of the elements here; bhūta means the elements "
               "as in unit 4, by the data's notes."),
    "explain_hi": ("यह गद्य-पंक्ति कहती है: इस प्रकार वे देह को भूतात्मक यानी भूतों से बना हुआ कहते हैं। "
                   "‘भूत’ यहाँ फिर महाभूतों के अर्थ में है, जैसे इकाई ४ में। "
                   "‘भूतात्मकम्’ बहुव्रीहि है: भूत जिसका आत्मा यानी स्वरूप है; यह ‘देहम्’ का विशेषण है। "
                   "‘आहुः’ का अर्थ ‘वे कहते हैं’; ‘वे’ कौन हैं, पाठ नहीं बताता।"),
    "hook": "देह भूतों से बना: भूतात्मक।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 28, what do they call the body (deha)?",
            ("Consisting of the elements", "भूतात्मकं देहम्: the body consisting of the elements (bhūta)."),
            [("Consisting of the mind alone", "Unit 28 says the body consists of the elements, not the mind."),
             ("Consisting of sattva alone", "Sattva is named the mind in unit 26; unit 28 speaks of the elements."),
             ("Free of all the elements", "The opposite: the body consists of the elements.")],
            "They call the body bhūtātmaka.",
            "भूतात्मकं देहमाहुः."),
        order(1, "Put the words of unit 28 in the line's order.",
              ["एवं", "भूतात्मकं", "देहम्", "आहुः"],
              "Thus, consisting of the elements, the body, they call.",
              "एवं → भूतात्मकं → देहम् → आहुः."),
        match(2, "Match each word of unit 28 to its meaning.",
              [["एवम्", "thus"], ["भूत", "element"], ["आत्मक", "consisting of, having as its nature"],
               ["देह", "body"], ["आहुः", "they say, they call"]],
              "Thus they call the body consisting of the elements.",
              "एवम्, भूत, आत्मक, देह, आहुः.", role="extend",
              teaches="भूतात्मक (bahuvrīhi) = having the elements as its nature, consisting of the elements."),
        mcq("discriminate", 3, "Which split of भूतात्मकं is right?",
            ("भूत + आत्मकम्", "अ + आ → आ: भूत + आत्मकम् → भूतात्मकम्."),
            [("भूति + आत्मकम्", "इ + आ would give या: भूत्यात्मकम्."),
             ("भूतः + आत्मकम्", "A visarga after अ drops before आ and the words stay apart: भूत आत्मकम्."),
             ("भूतम् + आत्मकम्", "म् before a vowel joins it: भूतमात्मकम्.")],
            "भूत (element) + आत्मकम् (consisting of): अ + आ → आ.",
            "अ + आ → आ."),
        multi("apply", 4, "Which statements about unit 28 are right by the card?",
              [("The author speaks in the first person", "आहुः is third person plural: they say."),
               ("'They' who say it are not named", "Right: the data notes that 'they' is unspecified."),
               ("देहम् is the object of आहुः", "Right: देहम् is accusative: they call the body ..."),
               ("The body is called free of the elements", "It is called भूतात्मक, consisting of the elements.")],
              [1, 2],
              "Unnamed 'they' call the body (accusative) bhūtātmaka.",
              "एवं भूतात्मकं देहमाहुः."),
        mcq("transfer", 5, "By the rule of देहमाहुः, how is गृहम् + आगच्छति (comes home) joined in a new example?",
            ("गृहमागच्छति", "Before a vowel a final म् stays म् and joins it, as देहम् + आहुः → देहमाहुः."),
            [("गृहं आगच्छति", "The anusvāra stands for म् only before a consonant, not before a vowel."),
             ("गृहोगच्छति", "ओ comes from a visarga after अ, not from म्."),
             ("गृहागच्छति", "The म् is not dropped before a vowel.")],
            "गृहम् + आगच्छति = गृहमागच्छति, like देहम् + आहुः = देहमाहुः.",
            "Final म् + vowel → म् joined to the vowel.",
            teaches="A final म् before a vowel stays म् and joins the vowel: देहम् + आहुः → देहमाहुः."),
    ],
}

# ---------------------------------------------------------------- unit 29
AUTHORED["29"] = {
    "title": "तस्य पुनः प्रविभागः",
    "question": "By unit 29, what is announced for the body?",
    "rule": "Again (पुनः), its (the body's) division (प्रविभाग). A short fragment without a verb.",
    "limits": ("A verbless prose fragment. By the data's notes it seems to run on into unit 30, which gives the list "
               "of the division; questions here stay inside unit 29. तस्य refers to the body (देह) of unit 28."),
    "explain_hi": ("यह क्रिया-रहित गद्य-खण्ड है: फिर उसका प्रविभाग। "
                   "‘तस्य’ (उसका) इकाई २८ के देह की ओर संकेत करता है। "
                   "‘प्रविभाग’ का अर्थ विभाग या वर्गीकरण है। "
                   "data के अनुसार यह खण्ड इकाई ३० में चलता लगता है, जहाँ विभाग की लम्बी सूची है।"),
    "hook": "देह का फिर से बँटवारा: प्रविभाग।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 29, what of the body is announced again?",
            ("Its division (pravibhāga)", "तस्य पुनः प्रविभागः: again, its division."),
            [("Its disturbance (upaplava)", "Upaplava is said of sattva, the mind, in unit 27."),
             ("Its healing (cikitsā)", "No healing is named in unit 29."),
             ("Its death (maraṇa)", "No death is named in unit 29.")],
            "Again, its division.",
            "तस्य पुनः प्रविभागः."),
        order(1, "Put the words of unit 29 in the line's order.",
              ["तस्य", "पुनः", "प्रविभागः"],
              "Of it, again, the division.",
              "तस्य → पुनः → प्रविभागः."),
        match(2, "Match each word of unit 29 to its meaning.",
              [["तस्य", "of it (of the body)"], ["पुनः", "again, further"], ["प्रविभाग", "division, classification"]],
              "Again, the division of it, the body.",
              "तस्य, पुनः, प्रविभाग.", role="extend",
              teaches="प्रविभाग = division or classification; तस्य here points back to the body (देह) of unit 28."),
        mcq("discriminate", 3, "By the card, what does तस्य (of it) in unit 29 refer to?",
            ("The body (deha) of unit 28", "The data notes: तस्य refers to the body of line 29 (card 28)."),
            [("The mind (sattva) of unit 26", "That is the तस्य of unit 27; here it is the body."),
             ("The blood (asṛj) of unit 31", "Blood is named only later; तस्य points back, to the body."),
             ("The skin (tvac) of unit 33", "The skins come later; तस्य points back, to the body.")],
            "तस्य = of the body (देह), named in unit 28.",
            "तस्य पुनः प्रविभागः = again, the division of the body."),
        mcq("apply", 4, "Unit 29 has no verb. How is it read by the card?",
            ("As a fragment: 'again, its division'", "The data calls it an elliptical fragment without a verb."),
            [("As a sentence whose verb is पुनः", "पुनः is an indeclinable, 'again', not a verb."),
             ("As a question about the division", "Nothing in unit 29 marks a question."),
             ("As the close of the list of skins", "The skins are named later; unit 29 names none.")],
            "A verbless fragment: तस्य पुनः प्रविभागः.",
            "No verb: again, its division."),
        mcq("transfer", 5, "By the rule of पुनः प्रविभागः, how is बालः + पठति (the boy reads) written in a new example?",
            ("बालः पठति", "Before प the visarga stays, as पुनः + प्रविभागः → पुनः प्रविभागः."),
            [("बालो पठति", "ओ comes only before a voiced sound; प is unvoiced."),
             ("बालर्पठति", "र् does not come from a visarga after अ."),
             ("बालस्पठति", "स् comes before त or थ, not before प.")],
            "बालः + पठति = बालः पठति, like पुनः प्रविभागः.",
            "Visarga + प → visarga stays.",
            teaches="Before क, ख, प, फ the visarga stays as it is: पुनः + प्रविभागः → पुनः प्रविभागः."),
    ],
}

# ---------------------------------------------------------------- unit 30
AUTHORED["30"] = {
    "title": "त्वचः कला दोषा धातवो मला ...",
    "question": "By unit 30, which items make up the division of the body?",
    "rule": ("A bare list: skins (त्वच्), kalās, doṣas, dhātus, malas, sense organs and their seats, organs of action, "
             "receptacles, abodes of prāṇa, vessels, bones, joints, muscles, channels, vital spots, hair, and divisions of prakṛti and vikṛti."),
    "limits": ("Prose list; confidence medium. Agni (fires) is a conjecture for printed ह्यूष्माणो; कर्मेन्द्रियण्य- is a "
               "near-certain correction: no question on either. Atīndriya is probably the mind; the unit does not say. "
               "Peśī = muscle is standard, other identifications probable; kūrca, jāla have none."),
    "explain_hi": ("यह गद्य-पंक्ति शरीर के प्रविभाग की सूची है: त्वचाएँ, कलाएँ, दोष, धातु, मल, ज्ञानेन्द्रियाँ और उनके अधिष्ठान, "
                   "कर्मेन्द्रियाँ, अतीन्द्रिय, आशय, प्राणायतन, कण्डरा, जाल, कूर्च, रज्जुक-सीवनी, अस्थिसंघात, सीमन्त, अस्थियाँ, "
                   "अस्थिसन्धियाँ, स्नायु, पेशियाँ, सिरा, धमनी, स्रोतस्, ऊष्माएँ, मर्म, केश-श्मश्रु-रोम और प्रकृति-विकृति के भेद। "
                   "पेशी = मांसपेशी (मानक); कला, कण्डरा, स्नायु, सिरा, धमनी, सीमन्त की पहचान सम्भावित है; कूर्च और जाल का पक्का आधुनिक नाम नहीं। "
                   "‘अग्नि’ (अग्नयः) अनुमानित पाठ है, इस पर कोई प्रश्न नहीं। "
                   "अतीन्द्रिय सम्भवतः मन है, पर पंक्ति यह नहीं कहती।"),
    "hook": "त्वचा से प्रकृति-विकृति तक: पूरे शरीर का नक्शा।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 30, which item opens the list of the body's division?",
            ("The skins (tvac)", "त्वचः is the first word of the list."),
            [("The bones (asthi)", "Bones are named in the list, but much later."),
             ("The vital spots (marma)", "Marma comes near the end of the list."),
             ("The hair (keśa)", "Hair comes near the end of the list.")],
            "The list opens with त्वचः, the skins.",
            "त्वचः कला दोषा धातवो मलाः ..."),
        order(1, "Put the first five items of unit 30 in the line's order.",
              ["त्वचः", "कलाः", "दोषाः", "धातवः", "मलाः"],
              "Skins, kalās, doṣas, dhātus, malas: the list's opening.",
              "त्वचः → कलाः → दोषाः → धातवः → मलाः."),
        match(2, "Match each body term of unit 30 to the card's identification.",
              [["पेशी", "muscle (standard)"], ["सिरा", "vessel, probably vein"], ["धमनी", "vessel, probably artery"],
               ["कण्डरा", "probably tendon"], ["स्नायु", "sinew, probably ligament"]],
              "Only peśī as muscle is standard; the others are probable.",
              "पेशी, सिरा, धमनी, कण्डरा, स्नायु.", role="extend",
              teaches="The data keeps labels: peśī = muscle (standard); sirā, dhamanī, kaṇḍarā, snāyu (probable)."),
        mcq("discriminate", 3, "Which identification in unit 30 is labelled standard on the card?",
            ("Peśī as muscle", "The data labels peśī = muscle standard."),
            [("Sirā as vein", "Sirā as vein is labelled probable."),
             ("Kaṇḍarā as tendon", "Kaṇḍarā as tendon is labelled probable."),
             ("Snāyu as ligament", "Snāyu as ligament is labelled probable.")],
            "Peśī = muscle is the one standard identification.",
            "Keep the data's labels: standard or probable."),
        multi("apply", 4, "Which of these does the list of unit 30 name?",
              [("नखाः (nails)", "Nails are not in the list; it names hair of the head, beard and body hair."),
               ("दन्ताः (teeth)", "Teeth are not in the list."),
               ("मर्माणि (vital spots)", "Right: मर्माणि is in the list."),
               ("पेश्यः (muscles)", "Right: पेश्यः is in the list.")],
              [2, 3],
              "Marma and peśī are named; nails and teeth are not.",
              "Only the items the list names belong to it."),
        mcq("transfer", 5, "By the rule of अस्थीन्यस्थिसंधयः, how is फलानि + अत्र (fruits here) joined in a new example?",
            ("फलान्यत्र", "इ before a different vowel becomes य्, as अस्थीनि + अस्थि → अस्थीन्यस्थि."),
            [("फलानेत्र", "ए comes from अ + इ, not from इ + अ."),
             ("फलानित्र", "The अ of अत्र is not lost; इ becomes य्."),
             ("फलान्यात्र", "इ + अ keeps a short अ: न्य, not न्या.")],
            "फलानि + अत्र = फलान्यत्र, like अस्थीनि + अस्थिसंधयः = अस्थीन्यस्थिसंधयः.",
            "इ + अ → य.",
            teaches="इ before a different vowel becomes य्: अस्थीनि + अस्थिसंधयः → अस्थीन्यस्थिसंधयः."),
    ],
}

# ---------------------------------------------------------------- unit 31
AUTHORED["31"] = {
    "title": "तत्रासृजः पच्यमानस्य ... षट् त्वचो भवंति",
    "question": "By unit 31, how do the skins come into being?",
    "rule": ("Among these, six skins (त्वच्) come into being from blood (असृज्) being cooked, like the films (सन्तानिका) "
             "of milk."),
    "limits": ("Prose; confidence medium. असृजः may be genitive or ablative, and पच्यमानस्य may go with blood or with "
               "milk: the unit does not settle it, and no question rests on it. Other teachers count seven skins (unit 40); "
               "unit 31 says six."),
    "explain_hi": ("यह गद्य-पंक्ति कहती है: उनमें पकते हुए रक्त से छः त्वचाएँ बनती हैं, दूध की सन्तानिकाओं यानी मलाई की परतों की तरह। "
                   "उपमा दूध की परतों से है (क्षीरस्य इव)। "
                   "‘पच्यमानस्य’ (पकते हुए) रक्त से जुड़ता है या दूध से, यह पंक्ति तय नहीं करती; ‘असृजः’ षष्ठी भी हो सकता है, पंचमी भी। "
                   "इसलिए इन बातों पर कोई प्रश्न नहीं। "
                   "आगे इकाई ३३ से ३८ तक इन छह त्वचाओं के नाम आते हैं।"),
    "hook": "उबलते दूध पर मलाई की परतें: वैसे ही छह त्वचाएँ।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 31, how many skins (tvac) come into being?",
            ("Six skins", "षट् त्वचो भवन्ति: six skins come into being."),
            [("Five skins", "The line says षट्, six."),
             ("Three skins", "The line says षट्, six."),
             ("Eight skins", "The line says षट्, six.")],
            "षट् = six.",
            "षट् त्वचो भवन्ति."),
        order(1, "Put the phrases of unit 31 in the line's order.",
              ["तत्रासृजः", "पच्यमानस्य", "क्षीरस्येव", "संतानिकाः", "षट् त्वचो भवंति"],
              "Among these, from blood, being cooked, like milk's, films, six skins come into being.",
              "तत्रासृजः → पच्यमानस्य → क्षीरस्येव → संतानिकाः → षट् त्वचो भवंति."),
        match(2, "Match each word of unit 31 to its meaning.",
              [["असृज्", "blood"], ["पच्यमान", "being cooked, being heated"], ["क्षीर", "milk"],
               ["सन्तानिका", "film, creamy layer"], ["इव", "like"]],
              "Blood being cooked; like the films of milk.",
              "असृज्, पच्यमान, क्षीर, सन्तानिका, इव.", role="extend",
              teaches="सन्तानिका = the creamy film or layer that forms on milk; unit 31 likens the skins to it."),
        mcq("discriminate", 3, "Which split of क्षीरस्येव is right?",
            ("क्षीरस्य + इव", "अ + इ → ए: क्षीरस्य + इव → क्षीरस्येव (like ... of milk)."),
            [("क्षीरस्य + एव", "अ + ए would give ऐ: क्षीरस्यैव."),
             ("क्षीरस्ये + इव", "क्षीरस्ये is not a form of क्षीर."),
             ("क्षीर + स्येव", "स्येव is not a word.")],
            "क्षीरस्य (of milk) + इव (like): अ + इ → ए.",
            "अ + इ → ए."),
        mcq("apply", 4, "In 'six skins come into being from blood being cooked, like the films of water', which word is wrong?",
            ("water: the line says milk (क्षीर)", "क्षीरस्येव = like ... of milk, not water."),
            [("six: the line says five (पञ्च)", "षट् is six; 'six' is right."),
             ("blood: the line says flesh (मांस)", "असृज् is blood; 'blood' is right."),
             ("films: the line says foam (फेन)", "सन्तानिका is film; 'films' is right.")],
            "The comparison is with the films of milk.",
            "क्षीरस्येव संतानिकाः = like the films of milk."),
        mcq("transfer", 5, "By the rule of तत्रासृजः, how is अत्र + अस्ति (is here) joined in a new example?",
            ("अत्रास्ति", "अ + अ → आ, as तत्र + असृजः → तत्रासृजः."),
            [("अत्रेस्ति", "ए comes from अ + इ, not from अ + अ."),
             ("अत्रोस्ति", "ओ comes from अ + उ, not from अ + अ."),
             ("अत्रस्ति", "Two short अ join into a long आ, not a short अ.")],
            "अत्र + अस्ति = अत्रास्ति, like तत्र + असृजः = तत्रासृजः.",
            "अ + अ → आ.",
            teaches="Two short अ join into long आ: तत्र + असृजः → तत्रासृजः."),
    ],
}

# ---------------------------------------------------------------- unit 32
AUTHORED["32"] = {
    "title": "त्वक्प्रसादाद्रक्तस्य प्रसादः",
    "question": "By unit 32, what follows from the clarity of the skin?",
    "rule": "From the clarity (प्रसाद) of the skin (त्वच्), the clarity of the blood (रक्त). No verb is written.",
    "limits": ("Prose, no verb; confidence medium. The ablative is read as the blood's clarity depending on the skin's; "
               "the unit says no more, and does not say how. प्रसाद may also mean 'essence'."),
    "explain_hi": ("यह क्रिया-रहित गद्य-पंक्ति कहती है: त्वचा की निर्मलता से रक्त की निर्मलता। "
                   "‘प्रसादात्’ पंचमी है (से), ‘प्रसादः’ प्रथमा। "
                   "data इसे ऐसे पढ़ता है कि रक्त का प्रसाद त्वचा के प्रसाद पर टिका है; इससे अधिक पंक्ति नहीं कहती। "
                   "‘प्रसाद’ का अर्थ ‘सार’ भी हो सकता है।"),
    "hook": "त्वचा साफ़, तो रक्त साफ़।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 32, the clarity (prasāda) of what follows from the clarity of the skin?",
            ("Of the blood (rakta)", "त्वक्प्रसादाद्रक्तस्य प्रसादः: of the blood."),
            [("Of the mind (manas)", "The mind is not named in unit 32."),
             ("Of the milk (kṣīra)", "Milk is a comparison in unit 31; unit 32 names blood."),
             ("Of the bones (asthi)", "Bones are not named in unit 32.")],
            "From the skin's clarity, the blood's clarity.",
            "त्वक्प्रसादात् रक्तस्य प्रसादः."),
        order(1, "Put the words of unit 32 in the line's order.",
              ["त्वक्प्रसादात्", "रक्तस्य", "प्रसादः"],
              "From the skin's clarity, of the blood, the clarity.",
              "त्वक्प्रसादात् → रक्तस्य → प्रसादः."),
        match(2, "Match each word of unit 32 to its meaning.",
              [["त्वच्", "skin"], ["प्रसादात्", "from the clarity"], ["रक्तस्य", "of the blood"],
               ["प्रसादः", "clarity (the subject)"]],
              "From the clarity of the skin, the clarity of the blood.",
              "त्वच्, प्रसादात्, रक्तस्य, प्रसादः.", role="extend",
              teaches="प्रसाद = clarity, purity (perhaps 'essence'); -आत् marks the ablative, 'from'."),
        mcq("discriminate", 3, "Which split of त्वक्प्रसादाद्रक्तस्य is right?",
            ("त्वक्प्रसादात् + रक्तस्य", "त् becomes द् before the voiced र: प्रसादात् + रक्तस्य → प्रसादाद्रक्तस्य."),
            [("त्वक्प्रसादः + रक्तस्य", "अः before र would give ओ: प्रसादो रक्तस्य."),
             ("त्वक्प्रसादम् + रक्तस्य", "म् before र would be written ं: प्रसादं रक्तस्य."),
             ("त्वक्प्रसादा + द्रक्तस्य", "द्रक्तस्य is not a word.")],
            "त्वक्प्रसादात् (from the skin's clarity) + रक्तस्य (of the blood).",
            "Final त् + voiced sound → द्."),
        mcq("apply", 4, "Why is the skin-word त्वक् and not त्वच् in त्वक्प्रसाद?",
            ("Final च् becomes क् before the consonant प", "At the end of a compound member च् becomes क् before प."),
            [("त्वक् is a word meaning 'from'", "त्वक् is the skin; 'from' is the ablative ending of प्रसादात्."),
             ("च् becomes क् before every vowel", "Before a vowel च् stays: त्वचः, त्वचो."),
             ("The print has misspelled त्वच् here", "No flag: त्वक् is the regular form before प.")],
            "त्वच् + प्रसाद → त्वक्प्रसाद: च् → क् before a consonant.",
            "Final च् before a consonant → क्."),
        mcq("transfer", 5, "By the rule of प्रसादाद्रक्तस्य, how is तस्मात् + गच्छति (therefore goes) joined in a new example?",
            ("तस्माद्गच्छति", "त् before the voiced ग becomes द्, as प्रसादात् + रक्तस्य → प्रसादाद्रक्तस्य."),
            [("तस्मात्गच्छति", "Before a voiced sound त् does not stay त्."),
             ("तस्मार्गच्छति", "त् does not become र्."),
             ("तस्मान्गच्छति", "त् becomes न् only before a nasal; ग is not a nasal.")],
            "तस्मात् + गच्छति = तस्माद्गच्छति, like प्रसादात् + रक्तस्य = प्रसादाद्रक्तस्य.",
            "Final त् + voiced consonant → द्.",
            teaches="A final त् becomes द् before a voiced consonant such as र or ग: प्रसादात् + रक्तस्य → प्रसादाद्रक्तस्य."),
    ],
}

# ---------------------------------------------------------------- unit 33
AUTHORED["33"] = {
    "title": "तासामुदकधरा चाद्या",
    "question": "By unit 33, what is the first skin called?",
    "rule": "And of these (the skins), the first (आद्या) is udakadharā (उदकधरा), 'water-bearing'.",
    "limits": ("A prose line; the verb is understood. It gives only the name: it does not say where this skin lies or what "
               "it does. 'These' are the skins, by the data's notes."),
    "explain_hi": ("यह गद्य-पंक्ति कहती है: और उनमें पहली उदकधरा यानी जल धारण करने वाली है। "
                   "‘तासाम्’ (उनमें) त्वचाओं की ओर संकेत करता है; स्त्रीलिंग है क्योंकि त्वच् स्त्रीलिंग है। "
                   "‘आद्या’ = पहली। "
                   "पंक्ति केवल नाम देती है; त्वचा कहाँ है या क्या करती है, यह नहीं बताती।"),
    "hook": "पहली त्वचा: उदकधरा, जल धारण करने वाली।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 33, what is the first skin called?",
            ("Udakadharā, 'water-bearing'", "तासामुदकधरा चाद्या: the first is udakadharā."),
            [("Asṛgdharā, 'blood-bearing'", "Asṛgdharā is the second skin (unit 34)."),
             ("Prāṇadharā, 'life-bearing'", "Prāṇadharā is the sixth skin (unit 38)."),
             ("The one that seats all kuṣṭha", "That is the fourth skin (unit 36).")],
            "The first skin is udakadharā.",
            "तासाम् उदकधरा च आद्या."),
        order(1, "Put the words of unit 33 in the line's order.",
              ["तासाम्", "उदकधरा", "च", "आद्या"],
              "Of these, udakadharā, and, the first.",
              "तासाम् → उदकधरा → च → आद्या."),
        match(2, "Match each word of unit 33 to its meaning.",
              [["तासाम्", "of these (the skins)"], ["उदक", "water"], ["धरा", "bearing, holding"], ["आद्या", "first"]],
              "Of these, the first is the water-bearing one.",
              "तासाम्, उदक, धरा, आद्या.", role="extend",
              teaches="उदकधरा = water-bearing (उदक water + धरा bearing), the name of the first skin."),
        mcq("discriminate", 3, "Which split of चाद्या is right?",
            ("च + आद्या", "अ + आ → आ: च + आद्या → चाद्या."),
            [("चम् + आद्या", "म् before a vowel joins it: चमाद्या."),
             ("चः + आद्या", "A visarga after अ drops before आ and the words stay apart: च आद्या."),
             ("चाद् + या", "चाद् and या are not the words here.")],
            "च (and) + आद्या (first): अ + आ → आ.",
            "अ + आ → आ."),
        mcq("apply", 4, "By the card, what does तासाम् (of these) in unit 33 refer to?",
            ("The skins (tvac)", "The data notes: the six (or seven) skins are meant."),
            [("The waters (udaka)", "उदक is part of the first skin's name, and it is neuter; तासाम् is feminine."),
             ("The elements (bhūta)", "The elements are not meant here; the list is of skins."),
             ("The doṣas (doṣa)", "The doṣas are not meant here; the list is of skins.")],
            "तासाम् = of these skins.",
            "तासाम् (f. gen. pl.) → the skins."),
        mcq("transfer", 5, "By the rule of चाद्या, how is न + आगच्छति (does not come) joined in a new example?",
            ("नागच्छति", "अ + आ → आ, as च + आद्या → चाद्या."),
            [("नेगच्छति", "ए comes from अ + इ, not from अ + आ."),
             ("नोगच्छति", "ओ comes from अ + उ, not from अ + आ."),
             ("नगच्छति", "अ + आ gives a long आ, not a short अ.")],
            "न + आगच्छति = नागच्छति, like च + आद्या = चाद्या.",
            "अ + आ → आ.",
            teaches="अ followed by आ joins into one long आ: च + आद्या → चाद्या."),
    ],
}

# ---------------------------------------------------------------- unit 34
AUTHORED["34"] = {
    "title": "द्वितीयाऽसृग्धरा",
    "question": "By unit 34, what is the second skin called?",
    "rule": "The second (द्वितीया) is asṛgdharā (असृग्धरा), 'blood-bearing': असृज् (blood) + धरा (bearing).",
    "limits": ("A two-word prose line; the verb is understood. It gives only the name. The ऽ printed after आ is a print "
               "habit, not a flag."),
    "explain_hi": ("यह गद्य-पंक्ति कहती है: दूसरी असृग्धरा यानी रक्त धारण करने वाली है। "
                   "असृग्धरा = असृज् (रक्त) + धरा (धारण करने वाली); ज् घोष ध से पहले ग् बनता है। "
                   "छपाई में आ के बाद ऽ है (द्वितीयाऽसृग्धरा); यह छपाई की आदत है, क्योंकि आ + अ से आ ही बनता है। "
                   "पंक्ति केवल नाम देती है।"),
    "hook": "दूसरी त्वचा: असृग्धरा, रक्त धारण करने वाली।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 34, what is the second skin called?",
            ("Asṛgdharā, 'blood-bearing'", "द्वितीयाऽसृग्धरा: the second is asṛgdharā."),
            [("Udakadharā, 'water-bearing'", "Udakadharā is the first skin (unit 33)."),
             ("Prāṇadharā, 'life-bearing'", "Prāṇadharā is the sixth skin (unit 38)."),
             ("The seat of sidhma and kilāsa", "That is the third skin (unit 35).")],
            "The second skin is asṛgdharā.",
            "द्वितीया असृग्धरा."),
        match(1, "Match each word of unit 34 to its meaning.",
              [["द्वितीया", "second"], ["असृज्", "blood"], ["धरा", "bearing, holding"]],
              "The second is the blood-bearing one.",
              "द्वितीया, असृज्, धरा."),
        fill(2, "असृग्धरा = ____ + धरा: type the word for 'blood' in Devanagari or in English letters (e.g. dharma).",
             accepts("असृज्", None, "असृक्", "असृग्"),
             "असृज् (blood) + धरा (bearing) = असृग्धरा: ज् becomes ग् before the voiced ध.",
             "असृज् = blood (as असृजः in unit 31); in a compound before ध it is written असृग्.",
             "असृज् + धरा → असृग्धरा."),
        mcq("discriminate", 3, "Why does the print show ऽ in द्वितीयाऽसृग्धरा?",
            ("A print habit: आ + अ already gives आ", "The data notes the ऽ after -आ as a print habit; no flag."),
            [("It marks a lost अ after ए or ओ here", "The vowel before it is आ, not ए or ओ."),
             ("It marks a long pause in the reading", "The ऽ is not a pause mark."),
             ("It shows that असृग्धरा is negated", "Nothing is negated; no न or अ- of negation.")],
            "द्वितीया + असृग्धरा → द्वितीयासृग्धरा; the ऽ is only the printer's habit.",
            "आ + अ → आ; the printed ऽ adds nothing."),
        mcq("apply", 4, "How do द्वितीया + असृग्धरा join by the vowel rule?",
            ("द्वितीयासृग्धरा (आ + अ → आ)", "आ and अ join into one long आ."),
            [("द्वितीयोसृग्धरा (आ + अ → ओ)", "ओ comes from अ + उ, not from आ + अ."),
             ("द्वितीयेसृग्धरा (आ + अ → ए)", "ए comes from अ + इ, not from आ + अ."),
             ("द्वितीयसृग्धरा (आ + अ → अ)", "आ + अ gives a long आ, not a short अ.")],
            "द्वितीया + असृग्धरा = द्वितीयासृग्धरा.",
            "आ + अ → आ."),
        mcq("transfer", 5, "By the rule of असृग्धरा, how is वाच् + देवी (goddess of speech) joined in a new example?",
            ("वाग्देवी", "Final च् becomes क्, and before the voiced द it is voiced ग्, as असृज् + धरा → असृग्धरा."),
            [("वाच्देवी", "A final च् does not stay before a consonant."),
             ("वाक्देवी", "Before the voiced द the क् must be voiced: ग्."),
             ("वाज्देवी", "A final च् does not become ज्.")],
            "वाच् + देवी = वाग्देवी, like असृज् + धरा = असृग्धरा.",
            "Final च्/ज् + voiced consonant → ग्.",
            teaches="A final च् or ज् of a compound member becomes ग् before a voiced consonant: असृज् + धरा → असृग्धरा."),
    ],
}

# ---------------------------------------------------------------- unit 35
AUTHORED["35"] = {
    "title": "तृतीयासिध्मकिलासाधिष्ठाना",
    "question": "By unit 35, of which diseases is the third skin the seat?",
    "rule": ("The third (तृतीया) is the seat (अधिष्ठान) of sidhma (a patchy skin disease; identity disputed) and kilāsa "
             "(probably vitiligo)."),
    "limits": ("A prose line; the verb is understood. Sidhma as pityriasis versicolor is disputed; kilāsa as vitiligo is "
               "probable. It names no treatment and no cause."),
    "explain_hi": ("यह गद्य-पंक्ति कहती है: तीसरी त्वचा सिध्म और किलास का अधिष्ठान है। "
                   "सिध्म एक चकत्तेदार त्वचा-रोग है, सम्भवतः छीप; यह पहचान विवादित है। "
                   "किलास सम्भवतः सफ़ेद दाग (विटिलिगो) है; यह पहचान सम्भावित है। "
                   "‘-अधिष्ठाना’ स्त्रीलिंग बहुव्रीहि है, त्वचा से मेल खाता है। "
                   "पंक्ति न कारण बताती है, न उपचार।"),
    "hook": "तीसरी त्वचा: सिध्म और किलास का घर।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 35, the third skin is the seat of which diseases?",
            ("Sidhma and kilāsa", "सिध्मकिलासाधिष्ठाना: the seat of sidhma and kilāsa."),
            [("Alajī and vidradhi", "Those belong to the fifth skin (unit 37)."),
             ("All the kuṣṭhas", "That is the fourth skin (unit 36)."),
             ("Sores at the joints", "Sores (arus) at the joints are tied to the sixth skin (unit 39).")],
            "The third skin seats sidhma and kilāsa.",
            "तृतीया सिध्मकिलासाधिष्ठाना."),
        order(1, "Put the parts of unit 35 in the line's order.",
              ["तृतीया", "सिध्म", "किलास", "अधिष्ठाना"],
              "Third; sidhma, kilāsa; seat.",
              "तृतीया → सिध्म → किलास → अधिष्ठाना."),
        match(2, "Match each word of unit 35 to the card's meaning.",
              [["तृतीया", "third"], ["सिध्म", "patchy skin disease (identity disputed)"],
               ["किलास", "probably vitiligo"], ["अधिष्ठान", "seat"]],
              "The third is the seat of sidhma and kilāsa.",
              "तृतीया, सिध्म, किलास, अधिष्ठान.", role="extend",
              teaches="सिध्म = a patchy skin disease, probably pityriasis versicolor (disputed); किलास = probably vitiligo."),
        mcq("discriminate", 3, "How does the card label the identification of kilāsa as vitiligo?",
            ("Probable", "The data tags kilāsa probable."),
            [("Standard", "Standard is not the tag for kilāsa."),
             ("Disputed", "Disputed is the tag for sidhma, not kilāsa."),
             ("Unidentified", "Kilāsa is given a probable identification.")],
            "Kilāsa = vitiligo, probable; sidhma, disputed.",
            "Keep the data's labels: kilāsa probable, sidhma disputed."),
        multi("apply", 4, "Which statements about unit 35 are right by the card?",
              [("Kilāsa is certainly vitiligo", "Kilāsa as vitiligo is only probable."),
               ("The third skin is a seat of kilāsa", "Right: सिध्मकिलासाधिष्ठाना."),
               ("Unit 35 gives a treatment for sidhma", "No treatment is named in unit 35."),
               ("The identity of sidhma is disputed", "Right: the data tags sidhma disputed.")],
              [1, 3],
              "The third skin seats sidhma (disputed identity) and kilāsa (probably vitiligo).",
              "तृतीया सिध्मकिलासाधिष्ठाना."),
        mcq("transfer", 5, "By the rule of किलासाधिष्ठाना, how is ज्वर + अधिष्ठाना (seat of fever) joined in a new example?",
            ("ज्वराधिष्ठाना", "अ + अ → आ, as किलास + अधिष्ठाना → किलासाधिष्ठाना."),
            [("ज्वरेधिष्ठाना", "ए comes from अ + इ, not from अ + अ."),
             ("ज्वरोधिष्ठाना", "ओ comes from अ + उ, not from अ + अ."),
             ("ज्वरधिष्ठाना", "Two short अ give a long आ, not a short अ.")],
            "ज्वर + अधिष्ठाना = ज्वराधिष्ठाना, like किलास + अधिष्ठाना = किलासाधिष्ठाना.",
            "अ + अ → आ.",
            teaches="Two short अ join into long आ: किलास + अधिष्ठाना → किलासाधिष्ठाना."),
    ],
}

# ---------------------------------------------------------------- unit 36
AUTHORED["36"] = {
    "title": "चतुर्थी सर्वकुष्ठाधिष्ठाना",
    "question": "By unit 36, of what is the fourth skin the seat?",
    "rule": ("The fourth (चतुर्थी) is the seat of all kuṣṭha (सर्वकुष्ठ): the group of chronic skin diseases, "
             "leprosy among them (standard)."),
    "limits": "A prose line; the verb is understood. It does not list the kuṣṭhas, nor give a cause or treatment.",
    "explain_hi": ("यह गद्य-पंक्ति कहती है: चौथी त्वचा सभी कुष्ठों का अधिष्ठान है। "
                   "कुष्ठ = पुराने त्वचा-रोगों का समूह, जिसमें कोढ़ भी है (मानक पहचान)। "
                   "‘सर्व’ (सभी) बताता है कि केवल एक नहीं, सब कुष्ठ यहाँ टिकते हैं। "
                   "कुष्ठों की गिनती या उपचार पंक्ति में नहीं है।"),
    "hook": "चौथी त्वचा: सब कुष्ठों का घर।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 36, the fourth skin is the seat of what?",
            ("All the kuṣṭhas", "सर्वकुष्ठाधिष्ठाना: the seat of all kuṣṭha."),
            [("Only one kuṣṭha", "सर्व means all, not one."),
             ("Sidhma and kilāsa", "Those belong to the third skin (unit 35)."),
             ("Alajī and vidradhi", "Those belong to the fifth skin (unit 37).")],
            "The fourth skin seats all kuṣṭhas.",
            "चतुर्थी सर्वकुष्ठाधिष्ठाना."),
        order(1, "Put the parts of unit 36 in the line's order.",
              ["चतुर्थी", "सर्व", "कुष्ठ", "अधिष्ठाना"],
              "Fourth; all; kuṣṭha; seat.",
              "चतुर्थी → सर्व → कुष्ठ → अधिष्ठाना."),
        match(2, "Match each word of unit 36 to its meaning.",
              [["चतुर्थी", "fourth"], ["सर्व", "all"], ["कुष्ठ", "chronic skin diseases, leprosy among them"],
               ["अधिष्ठान", "seat"]],
              "The fourth is the seat of all kuṣṭha.",
              "चतुर्थी, सर्व, कुष्ठ, अधिष्ठान.", role="extend",
              teaches="कुष्ठ = the group of chronic skin diseases, leprosy among them (standard identification)."),
        mcq("discriminate", 3, "In the translation: the fourth is the seat of some kuṣṭhas, which word is wrong?",
            ("some: सर्व means all", "सर्वकुष्ठ = all kuṣṭha."),
            [("fourth: it should be fifth", "चतुर्थी is the fourth; 'fourth' is right."),
             ("seat: it should be cure", "अधिष्ठान is the seat; 'seat' is right."),
             ("kuṣṭhas: it should be fevers", "कुष्ठ is named; 'kuṣṭhas' is right.")],
            "The fourth is the seat of all kuṣṭhas.",
            "सर्व = all."),
        fill(4, "चतुर्थी ____कुष्ठाधिष्ठाना: type the word for 'all' in Devanagari or in English letters (e.g. dharma).",
             accepts("सर्व"),
             "चतुर्थी सर्वकुष्ठाधिष्ठाना: the seat of all kuṣṭha.",
             "सर्व = all; it opens the compound सर्वकुष्ठाधिष्ठाना.",
             "सर्व + कुष्ठ + अधिष्ठाना.", role="apply"),
        mcq("transfer", 5, "In a new example, which bahuvrīhi agrees with one feminine skin (त्वक्) as seat of all diseases (रोग)?",
            ("सर्वरोगाधिष्ठाना", "Feminine singular in -आ, as सर्वकुष्ठाधिष्ठाना agrees with the feminine skin."),
            [("सर्वरोगाधिष्ठानः", "Masculine singular; the skin is feminine."),
             ("सर्वरोगाधिष्ठाने", "Feminine dual; only one skin is meant."),
             ("सर्वरोगाधिष्ठानाः", "Feminine plural; only one skin is meant.")],
            "One feminine skin: सर्वरोगाधिष्ठाना, like चतुर्थी सर्वकुष्ठाधिष्ठाना.",
            "A bahuvrīhi takes the gender and number of what it describes.",
            teaches="A bahuvrīhi agrees with its noun: सर्वकुष्ठाधिष्ठाना is feminine singular for one skin (त्वच्, f.)."),
    ],
}

# ---------------------------------------------------------------- unit 37
AUTHORED["37"] = {
    "title": "पंचमी पुनरल्जीविद्रध्यधिष्ठाना",
    "question": "By unit 37, of which diseases is the fifth skin the seat?",
    "rule": ("The fifth (पञ्चमी), again, is the seat of alajī (a skin eruption; identity uncertain) and vidradhi "
             "(abscess, standard)."),
    "limits": ("Prose; confidence medium. Printed अल्जी is read अलजी (a near-certain correction); alajī's identity is "
               "uncertain: no question rests on alajī. Vidradhi = abscess is standard. No cause or treatment is named."),
    "explain_hi": ("यह गद्य-पंक्ति कहती है: पाँचवीं फिर अलजी और विद्रधि का अधिष्ठान है। "
                   "विद्रधि = फोड़ा (मानक पहचान)। "
                   "छपा ‘अल्जी’ लगभग निश्चित रूप से ‘अलजी’ है, एक त्वचा-विस्फोट जिसकी पहचान अनिश्चित है; इस पर कोई प्रश्न नहीं। "
                   "‘पुनर्’ (फिर) का र् स्वर से पहले दिखता है: पुनरल्जी। "
                   "विद्रधि + अधिष्ठाना → विद्रध्यधिष्ठाना (इ + अ → य)।"),
    "hook": "पाँचवीं त्वचा: फोड़े (विद्रधि) का घर।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 37, which disease of sure identity has the fifth skin as its seat?",
            ("Vidradhi, an abscess", "विद्रध्यधिष्ठाना: the seat of vidradhi (abscess, standard)."),
            [("Kilāsa, probably vitiligo", "Kilāsa belongs to the third skin (unit 35)."),
             ("Kuṣṭha, the skin diseases", "Kuṣṭha belongs to the fourth skin (unit 36)."),
             ("Sidhma, a patchy disease", "Sidhma belongs to the third skin (unit 35).")],
            "The fifth skin seats vidradhi (and alajī).",
            "पञ्चमी ... विद्रध्यधिष्ठाना."),
        match(1, "Match each word of unit 37 to its meaning.",
              [["पञ्चमी", "fifth"], ["पुनर्", "again, further"], ["विद्रधि", "abscess"], ["अधिष्ठान", "seat"]],
              "The fifth, again, is the seat of vidradhi (and alajī).",
              "पञ्चमी, पुनर्, विद्रधि, अधिष्ठान."),
        mcq("extend", 2, "Which split of विद्रध्यधिष्ठाना is right?",
            ("विद्रधि + अधिष्ठाना", "इ before a different vowel becomes य्: विद्रधि + अधिष्ठाना → विद्रध्यधिष्ठाना."),
            [("विद्रध्य + धिष्ठाना", "धिष्ठाना is not a word; the word is अधिष्ठाना."),
             ("विद्रधे + अधिष्ठाना", "ए + अ would give एऽ: विद्रधेऽधिष्ठाना."),
             ("विद्रधिः + अधिष्ठाना", "इः before a vowel would give इर्: विद्रधिरधिष्ठाना.")],
            "विद्रधि (abscess) + अधिष्ठाना (seat): इ + अ → य.",
            "इ + a different vowel → य् + that vowel.",
            teaches="इ before a different vowel becomes य्: विद्रधि + अधिष्ठाना → विद्रध्यधिष्ठाना."),
        mcq("discriminate", 3, "Why does पुनः appear as पुनर् in पुनरल्जी?",
            ("Its र् shows before a vowel", "पुनर् keeps its र् before a vowel; here before अ."),
            [("र् is a misprint for ः", "No flag marks पुनर्; it is the regular form before a vowel."),
             ("पुनर् is a word for 'fifth'", "पुनर् means again; the fifth is पञ्चमी."),
             ("र् comes only before consonants", "Before an unvoiced consonant it is ः, as पुनः प्रविभागः.")],
            "पुनर् + vowel → पुनर; before प it is पुनः (unit 29).",
            "पुनः/पुनर् before a vowel → पुनर्."),
        multi("apply", 4, "Which statements about unit 37 are right by the card?",
              [("The fifth skin is a seat of vidradhi", "Right: विद्रध्यधिष्ठाना."),
               ("The fifth skin is called prāṇadharā", "Prāṇadharā is the sixth skin (unit 38)."),
               ("Vidradhi is identified as an abscess", "Right: vidradhi = abscess, standard."),
               ("Unit 37 gives a treatment for abscess", "No treatment is named in unit 37.")],
              [0, 2],
              "The fifth skin seats vidradhi, an abscess.",
              "पञ्चमी ... विद्रध्यधिष्ठाना."),
        mcq("transfer", 5, "By the rule of पुनरल्जी, how is पुनः + आगच्छति (comes again) joined in a new example?",
            ("पुनरागच्छति", "पुनर् keeps its र् before a vowel, as in पुनरल्जी."),
            [("पुनोगच्छति", "ओ comes from अः before a voiced sound, not from पुनर्."),
             ("पुनागच्छति", "The र् of पुनर् is not dropped before a vowel."),
             ("पुनश्गच्छति", "श् comes before च, छ or श, not before a vowel.")],
            "पुनः + आगच्छति = पुनरागच्छति, like पुनर् + अल्जी = पुनरल्जी.",
            "पुनर् + vowel → पुनर्.",
            teaches="पुनः (from पुनर्) shows its र् before a vowel: पुनरल्जी, पुनरागच्छति."),
    ],
}

# ---------------------------------------------------------------- unit 38
AUTHORED["38"] = {
    "title": "षष्ठी तु प्राणधरा",
    "question": "By unit 38, what is the sixth skin called?",
    "rule": "The sixth (षष्ठी), however (तु), is prāṇadharā (प्राणधरा), 'life-bearing'.",
    "limits": ("A prose line; the verb is understood. It gives only the name; unit 39 goes on to describe this skin. "
               "Questions stay inside unit 38."),
    "explain_hi": ("यह गद्य-पंक्ति कहती है: छठी तो प्राणधरा यानी प्राण धारण करने वाली है। "
                   "‘तु’ = तो, किन्तु। "
                   "प्राणधरा = प्राण + धरा (धारण करने वाली)। "
                   "इस त्वचा का वर्णन इकाई ३९ में आगे चलता है।"),
    "hook": "छठी त्वचा: प्राणधरा, प्राण धारण करने वाली।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 38, what is the sixth skin called?",
            ("Prāṇadharā, 'life-bearing'", "षष्ठी तु प्राणधरा: the sixth is prāṇadharā."),
            [("Udakadharā, 'water-bearing'", "Udakadharā is the first skin (unit 33)."),
             ("Asṛgdharā, 'blood-bearing'", "Asṛgdharā is the second skin (unit 34)."),
             ("The seat of all the kuṣṭhas", "That is the fourth skin (unit 36).")],
            "The sixth skin is prāṇadharā.",
            "षष्ठी तु प्राणधरा."),
        order(1, "Put the words of unit 38 in the line's order.",
              ["षष्ठी", "तु", "प्राणधरा"],
              "The sixth, however, life-bearing.",
              "षष्ठी → तु → प्राणधरा."),
        match(2, "Match each word of unit 38 to its meaning.",
              [["षष्ठी", "sixth"], ["तु", "but, however"], ["प्राण", "life-breath"], ["धरा", "bearing, holding"]],
              "The sixth, however, is the life-bearing one.",
              "षष्ठी, तु, प्राण, धरा.", role="extend",
              teaches="प्राणधरा = life-bearing (प्राण life-breath + धरा bearing), the name of the sixth skin."),
        mcq("discriminate", 3, "What does तु mean in षष्ठी तु प्राणधरा?",
            ("but, however", "The data glosses तु as 'but, however'."),
            [("you (the reader)", "'You' is त्वम्; तु is an indeclinable."),
             ("and, also", "'And' is च; तु is 'but, however'."),
             ("is, exists", "No verb is written; तु is not a verb.")],
            "तु = but, however.",
            "षष्ठी तु = the sixth, however."),
        fill(4, "____ तु प्राणधरा: type the word for 'sixth' (feminine) in Devanagari or in English letters (e.g. dharma).",
             accepts("षष्ठी"),
             "षष्ठी तु प्राणधरा: the sixth, however, is prāṇadharā.",
             "षष्ठी = sixth, feminine (of षष्ठ), agreeing with the feminine skin.",
             "षष्ठी = sixth (f.).", role="apply"),
        mcq("transfer", 5, "By the rule of षष्ठी, which form means the eighth night (रात्रिः, feminine) in a new example?",
            ("अष्टमी रात्रिः", "Ordinals from the fourth on make the feminine in -ई, as षष्ठ → षष्ठी."),
            [("अष्टमो रात्रिः", "अष्टमः is masculine; रात्रि is feminine."),
             ("अष्टमा रात्रिः", "The feminine of अष्टम is अष्टमी, not अष्टमा."),
             ("अष्टमं रात्रिः", "अष्टमम् is neuter; रात्रि is feminine.")],
            "अष्टम → अष्टमी (f.), like षष्ठ → षष्ठी.",
            "Ordinals from चतुर्थ on: feminine in -ई.",
            teaches="Ordinals from the fourth on form the feminine in -ई (चतुर्थी, पञ्चमी, षष्ठी); प्रथमा, द्वितीया, तृतीया take -आ."),
    ],
}


NOTES_HI = {
    "26": ("गद्य-पंक्ति; विश्वास उच्च। छपा ‘सत्वं’ data में सत्त्वम् पढ़ा गया (इस छपाई में ‘सत्व’ बार-बार, जैसे इकाई ६ का "
           "‘सत्वबहुलम्’)। क्रिया ‘है’ लिखी नहीं, समझी जाती है। सन्धि जाँची: सत्त्वम् + मनः → सत्त्वं मनः (वाक्य के भीतर व्यंजन से "
           "पहले अन्त्य म् → ं)। कोई पाठ-चिह्न नहीं, कोई अस्पष्ट अंश नहीं।"),
    "27": ("गद्य-पंक्ति; विश्वास उच्च। data के अनुसार ‘तस्य’ इकाई २६ के सत्त्व यानी मन की ओर है। अन्त का ‘इति’ कथन की समाप्ति "
           "दिखाता है, अनुवाद में नहीं आता। क्रिया समझी जाती है। सन्धि जाँची: तस्य + उपप्लवः → तस्योपप्लवः (अ + उ → ओ); "
           "उपप्लवः + रजः → उपप्लवो रजः (अः + घोष → ओ); रजः + तमः → रजस्तमः (विसर्ग + त → स्); तमः + च → तमश्च "
           "(विसर्ग + च → श्); च + इति → चेति (अ + इ → ए)। कोई पाठ-चिह्न नहीं।"),
    "28": ("गद्य-पंक्ति; विश्वास उच्च। ‘वे’ (आहुः का कर्ता) पाठ में नहीं बताए गए। ‘भूत’ यहाँ फिर महाभूत (इकाई ४ देखें)। "
           "‘भूतात्मकम्’ बहुव्रीहि, पुं. द्वितीया एकवचन, ‘देहम्’ का विशेषण। ‘आहुः’ = √अह्, लिट् प्रथम पुरुष बहुवचन (वे कहते हैं)। "
           "सन्धि जाँची: एवम् + भूत... → एवं भूत... (व्यंजन से पहले ं); भूत + आत्मकम् → भूतात्मकम् (अ + आ → आ); "
           "भूतात्मकम् + देहम् → भूतात्मकं देहम्; देहम् + आहुः → देहमाहुः (स्वर से पहले म् जुड़ता है)। कोई पाठ-चिह्न नहीं।"),
    "29": ("गद्य-खण्ड; विश्वास मध्यम। क्रिया नहीं (अधूरा कथन)। data की टिप्पणी (GROUPING): यह इकाई ३० में चलता लगता है, जहाँ "
           "विभाग की सूची है। ‘तस्य’ (पुं. षष्ठी) इकाई २८ के देह की ओर। सन्धि जाँची: पुनः + प्रविभागः → पुनः प्रविभागः "
           "(प से पहले विसर्ग बना रहता है)। कोई पाठ-चिह्न नहीं।"),
    "30": ("गद्य-सूची; विश्वास मध्यम। पाठ-चिह्न: (१) छपा ‘कर्मेन्द्रियण्य-’ → कर्मेन्द्रियाण्य- (लगभग निश्चित; आ की मात्रा छूटी); "
           "(२) छपा ‘स्रोतांस्यह्यूष्माणो’ में ‘अह्यूष्माणः’ का अर्थ नहीं बनता; सम्भावित सुधार ‘स्रोतांस्यग्नय ऊष्माणो’ (अग्नयः + ऊष्माणः; "
           "ग्न का ह्य पढ़ा जाना) — अनुमान, इस पर प्रश्न नहीं। ‘रज्जुक’ रूप अनिश्चित (रज्जवः की जगह); ‘रज्जुकसीवन्यः’ जोड़ी के रूप में पढ़ा। "
           "‘केशाश्मश्रु-’ = केशाः + श्मश्रु (केशाश् श्मश्रु का दोहरा श छपाई में एक)। पहचान: पेशी = मांसपेशी (मानक); कला, कण्डरा, "
           "स्नायु, सिरा, धमनी, सीमन्त (सम्भावित); कूर्च, जाल का पक्का आधुनिक नाम नहीं; अतीन्द्रिय सम्भवतः मन, पर पंक्ति नहीं कहती। "
           "‘आशयाःप्राणा-’, ‘संघाताःसीमन्ता’ में रिक्त स्थान छूटे हैं (केवल छपाई)। सन्धि जाँची: अस्थीनि + अस्थिसंधयः → "
           "अस्थीन्यस्थिसंधयः (इ + अ → य); धातवः + मलाः → धातवो मलाः (अः + घोष → ओ); रज्जुकसीवन्यः + अस्थि... → "
           "रज्जुकसीवन्योऽस्थि... (अः + अ → ओऽ)।"),
    "31": ("गद्य-पंक्ति; विश्वास मध्यम। वाक्य-रचना दो तरह: ‘असृजः’ षष्ठी (रक्त का) या पंचमी (रक्त से) — data ने ‘से’ चुना; "
           "‘पच्यमानस्य’ रक्त के साथ लिया गया, पर दूध (क्षीरस्य) के साथ भी जा सकता है; पंक्ति तय नहीं करती। इन पर प्रश्न नहीं। "
           "छपा ‘संतानिकाः’ = सन्तानिकाः, ‘भवंति’ = भवन्ति। सन्धि जाँची: तत्र + असृजः → तत्रासृजः (अ + अ → आ); "
           "क्षीरस्य + इव → क्षीरस्येव (अ + इ → ए); त्वचः + भवन्ति → त्वचो भवन्ति (अः + घोष → ओ)। कोई पाठ-चिह्न नहीं।"),
    "32": ("गद्य-पंक्ति; विश्वास मध्यम। क्रिया नहीं। पंचमी (प्रसादात्) को data ने निर्भरता के रूप में पढ़ा: रक्त का प्रसाद त्वचा के "
           "प्रसाद से; पंक्ति इससे अधिक नहीं कहती। ‘प्रसाद’ = निर्मलता, या ‘सार’ भी। सन्धि जाँची: त्वच् + प्रसाद → त्वक्प्रसाद "
           "(व्यंजन से पहले च् → क्); प्रसादात् + रक्तस्य → प्रसादाद्रक्तस्य (घोष र से पहले त् → द्)। कोई पाठ-चिह्न नहीं।"),
    "33": ("गद्य-पंक्ति; विश्वास उच्च। ‘तासाम्’ (स्त्री. षष्ठी बहुवचन) = इन छह (या सात) त्वचाओं में। क्रिया समझी जाती है। "
           "सन्धि जाँची: तासाम् + उदकधरा → तासामुदकधरा (स्वर से पहले म् जुड़ता है); च + आद्या → चाद्या (अ + आ → आ)। "
           "कोई पाठ-चिह्न नहीं।"),
    "34": ("गद्य-पंक्ति; विश्वास उच्च। छपा ‘द्वितीयाऽसृग्धरा’ में आ के बाद ऽ छपाई की आदत है (आ + अ → आ); कोई पाठ-चिह्न नहीं। "
           "क्रिया समझी जाती है। सन्धि जाँची: द्वितीया + असृग्धरा → द्वितीयासृग्धरा (आ + अ → आ); असृज् + धरा → असृग्धरा "
           "(अन्त्य ज् घोष ध से पहले ग्)।"),
    "35": ("गद्य-पंक्ति; विश्वास उच्च। पहचान: सिध्म (सम्भवतः छीप, pityriasis versicolor) विवादित; किलास (सम्भवतः सफ़ेद दाग, "
           "विटिलिगो) सम्भावित। ‘तृतीया’ और ‘सिध्म...’ छपाई में साथ लिखे हैं, पर अलग शब्द हैं (आ के बाद स: कोई सन्धि-परिवर्तन नहीं)। "
           "सन्धि जाँची: किलास + अधिष्ठाना → किलासाधिष्ठाना (अ + अ → आ)। ‘-अधिष्ठाना’ द्वन्द्व + बहुव्रीहि, स्त्री. प्रथमा एकवचन। "
           "कोई पाठ-चिह्न नहीं।"),
    "36": ("गद्य-पंक्ति; विश्वास उच्च। पहचान: कुष्ठ = पुराने त्वचा-रोगों का समूह, कोढ़ सहित (मानक)। ‘सर्वकुष्ठाधिष्ठाना’ बहुव्रीहि, "
           "स्त्री. प्रथमा एकवचन। सन्धि जाँची: कुष्ठ + अधिष्ठाना → कुष्ठाधिष्ठाना (अ + अ → आ)। कोई पाठ-चिह्न नहीं।"),
    "37": ("गद्य-पंक्ति; विश्वास मध्यम। पाठ-चिह्न: छपा ‘अल्जी’ → ‘अलजी’ (लगभग निश्चित; अ की मात्रा छूटी)। अलजी क्षुद्र रोगों की "
           "सूची में एक त्वचा-विस्फोट है, पहचान अनिश्चित (विवादित); इस पर प्रश्न नहीं। विद्रधि = फोड़ा (मानक)। छपा ‘पंचमी’ = पञ्चमी। "
           "सन्धि जाँची: पुनर् + अलजी → पुनरलजी (स्वर से पहले र्); विद्रधि + अधिष्ठाना → विद्रध्यधिष्ठाना (इ + अ → य)।"),
    "38": ("गद्य-पंक्ति; विश्वास उच्च। क्रिया समझी जाती है। ‘तु’ = किन्तु, तो। प्राणधरा = प्राण + धरा (तत्पुरुष)। इकाई ३९ के "
           "दोनों सम्बन्ध-वाक्य (यस्यां छिन्नायां..., यां चाधिष्ठाय...) data के अनुसार इसी छठी त्वचा के बारे में हैं। "
           "कोई पाठ-चिह्न नहीं, कोई सन्धि-परिवर्तन नहीं।"),
}


AIDS = {
    "26": {
        "chunks": "तत्र | सत्वं | मनः",
        "sandhi": "अन्त्य म् + व्यंजन → ं: सत्त्वम् + मनः → सत्त्वं मनः।",
        "anchors": "‘सत्त्वं मनः’: दो संज्ञाएँ, बीच में ‘है’ अनलिखा।",
    },
    "27": {
        "diagram": {"groups": [
            {"label": "किसका", "items": ["तस्य: सत्त्व यानी मन का (इकाई २६)"]},
            {"label": "उपप्लव (उपद्रव)", "items": ["रजस्", "तमस्"]}]},
        "chunks": "तस्योपप्लवो | रजस्तमश्चेति",
        "sandhi": "अ + उ → ओ: तस्य + उपप्लवः → तस्योपप्लवः · अः + घोष → ओ: उपप्लवः + रजः → उपप्लवो रजः · "
                  "विसर्ग + च → श्: तमः + च → तमश्च · अ + इ → ए: च + इति → चेति।",
        "frame": "मन = सत्त्व (इकाई २६) → उसका उपद्रव = रजस् और तमस् (इकाई २७)।",
    },
    "28": {
        "chunks": "एवं | भूतात्मकं | देहमाहुः",
        "sandhi": "अ + आ → आ: भूत + आत्मकम् → भूतात्मकम् · स्वर से पहले म् जुड़ता है: देहम् + आहुः → देहमाहुः।",
        "anchors": "भूत + आत्मक = भूतों से बना; ‘आहुः’ = वे कहते हैं (कौन, पाठ में नहीं)।",
    },
    "29": {
        "chunks": "तस्य | पुनः | प्रविभागः",
        "frame": "किसका: तस्य = देह का (इकाई २८) → क्या: पुनः प्रविभागः (फिर विभाग) → सूची: data के अनुसार इकाई ३० में।",
        "sandhi": "प से पहले विसर्ग बना रहता है: पुनः + प्रविभागः → पुनः प्रविभागः।",
    },
    "30": {
        "diagram": {"groups": [
            {"label": "१ से १२", "items": ["१ त्वचाएँ", "२ कलाएँ", "३ दोष", "४ धातु", "५ मल", "६ ज्ञानेन्द्रियाँ",
                                         "७ उनके अधिष्ठान", "८ कर्मेन्द्रियाँ", "९ अतीन्द्रिय", "१० आशय", "११ प्राणायतन",
                                         "१२ कण्डरा"]},
            {"label": "१३ से २८", "items": ["१३ जाल, १४ कूर्च", "१५ रज्जुक-सीवनी", "१६ अस्थिसंघात", "१७ सीमन्त",
                                          "१८ अस्थियाँ, १९ अस्थिसन्धियाँ", "२० स्नायु, २१ पेशियाँ", "२२ सिरा, २३ धमनी",
                                          "२४ स्रोतस्", "२५ (अनुमानित: अग्नि) ऊष्माएँ", "२६ मर्म", "२७ केश, श्मश्रु, रोम",
                                          "२८ प्रकृति-विकृति के भेद"]}]},
        "chunks": "त्वचः कला दोषा धातवो मला | बुद्धींद्रियाणि तदधिष्ठानानि | कर्मेन्द्रियण्यतींद्रियमाशयाःप्राणायतनानि | "
                  "कंडरा जालानि कूर्च्चा रज्जुकसीवन्यो | ऽस्थिसंघाताःसीमंता अस्थीन्यस्थिसंधयः | स्नायूनि पेश्यः सिरा धमन्यः | "
                  "स्रोतांस्यह्यूष्माणो मर्माणि | केशाश्मश्रुलोमानि प्रकृतिविकृतिभेदाश्च",
        "sandhi": "अः + घोष → ओ: धातवः + मलाः → धातवो मलाः · इ + अ → य: अस्थीनि + अस्थिसंधयः → अस्थीन्यस्थिसंधयः · "
                  "अः + अ → ओऽ: रज्जुकसीवन्यः + अस्थि... → रज्जुकसीवन्योऽस्थि...।",
        "pegs": "मेरा बनाया क्रम-सूत्र (केवल याद रखने की सहायता): ‘त्वचा से शुरू, प्रकृति-विकृति पर अन्त’ — पहले पाँच: "
                "त्वचा, कला, दोष, धातु, मल।",
    },
    "31": {
        "chain": {"steps": ["रक्त (असृज्)", "पकता हुआ (रक्त या दूध: तय नहीं)", "दूध की मलाई की परतों जैसा",
                            "छह त्वचाएँ बनती हैं"]},
        "chunks": "तत्रासृजः | पच्यमानस्य | क्षीरस्येव संतानिकाः | षट् त्वचो भवंति",
        "sandhi": "अ + अ → आ: तत्र + असृजः → तत्रासृजः · अ + इ → ए: क्षीरस्य + इव → क्षीरस्येव · अः + घोष → ओ: "
                  "त्वचः + भवन्ति → त्वचो भवन्ति।",
        "anchors": "उपमा: उबलते दूध पर परत-दर-परत मलाई; वैसे ही छह त्वचाएँ।",
    },
    "32": {
        "chain": {"steps": ["त्वचा का प्रसाद (निर्मलता)", "उससे (पंचमी: प्रसादात्)", "रक्त का प्रसाद"]},
        "chunks": "त्वक्प्रसादाद्रक्तस्य | प्रसादः",
        "sandhi": "व्यंजन से पहले च् → क्: त्वच् + प्रसाद → त्वक्प्रसाद · घोष से पहले त् → द्: प्रसादात् + रक्तस्य → "
                  "प्रसादाद्रक्तस्य।",
    },
    "33": {
        "chunks": "तासामुदकधरा | चाद्या",
        "sandhi": "स्वर से पहले म् जुड़ता है: तासाम् + उदकधरा → तासामुदकधरा · अ + आ → आ: च + आद्या → चाद्या।",
        "letters": "उदक-धरा: ‘उ’ से उदक (जल) — पहली त्वचा जल धारण करती है।",
    },
    "34": {
        "chunks": "द्वितीयाऽसृग्धरा",
        "sandhi": "आ + अ → आ: द्वितीया + असृग्धरा → द्वितीयासृग्धरा (ऽ केवल छपाई) · घोष ध से पहले ज् → ग्: असृज् + धरा → असृग्धरा।",
        "anchors": "असृज् = रक्त (इकाई ३१ का ‘असृजः’); दूसरी त्वचा रक्त धारण करती है।",
    },
    "35": {
        "diagram": {"groups": [
            {"label": "तीसरी त्वचा: अधिष्ठान", "items": ["सिध्म: चकत्तेदार त्वचा-रोग, सम्भवतः छीप (विवादित)",
                                                     "किलास: सम्भवतः सफ़ेद दाग (सम्भावित)"]}]},
        "chunks": "तृतीया | सिध्म | किलास | अधिष्ठाना",
        "sandhi": "अ + अ → आ: किलास + अधिष्ठाना → किलासाधिष्ठाना।",
    },
    "36": {
        "chunks": "चतुर्थी | सर्वकुष्ठाधिष्ठाना",
        "sandhi": "अ + अ → आ: कुष्ठ + अधिष्ठाना → कुष्ठाधिष्ठाना।",
        "anchors": "‘सर्व’ पर ध्यान: एक नहीं, सब कुष्ठ (पुराने त्वचा-रोग, कोढ़ सहित) चौथी त्वचा में।",
    },
    "37": {
        "diagram": {"groups": [
            {"label": "पाँचवीं त्वचा: अधिष्ठान", "items": ["अलजी (छपा: अल्जी): त्वचा-विस्फोट, पहचान अनिश्चित",
                                                       "विद्रधि: फोड़ा (मानक)"]}]},
        "chunks": "पंचमी | पुनरल्जी | विद्रध्यधिष्ठाना",
        "sandhi": "स्वर से पहले पुनर् का र्: पुनर् + अल्जी → पुनरल्जी · इ + अ → य: विद्रधि + अधिष्ठाना → विद्रध्यधिष्ठाना।",
    },
    "38": {
        "chunks": "षष्ठी | तु | प्राणधरा",
        "anchors": "प्राण + धरा = प्राण धारण करने वाली; इसका वर्णन इकाई ३९ में आगे।",
    },
}


IMAGE_SPECS = {
    ("27", "diagram"): {
        "file": "sh5-upaplava-27.svg",
        "alt": ("Flowchart of unit 27: of it (sattva, the mind of unit 26) the disturbance (upaplava) is two: "
                "rajas and tamas."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"सत्त्व यानी मन (इकाई २६)\"] --> B[\"उसका उपप्लव (उपद्रव)\"]\n"
                 "  B --> C[\"रजस्\"]\n"
                 "  B --> D[\"तमस्\"]\n"),
    },
    ("30", "diagram"): {
        "file": "sh5-pravibhaga-30.svg",
        "alt": ("Numbered table of the 28 items of the body's division in unit 30, in line order: skins, kalās, doṣas, "
                "dhātus, malas, sense organs, their seats, organs of action, atīndriya, receptacles, abodes of prāṇa, "
                "kaṇḍarā, nets, kūrca, cords and sutures, bone-groupings, sīmanta, bones, bone-joints, snāyu, muscles, "
                "sirā, dhamanī, srotas, (conjectural agni and) heats, marma, hair of head, beard and body, and the "
                "divisions of prakṛti and vikṛti."),
        "type": "split",
        "title": "इकाई ३०: शरीर का प्रविभाग (क्रम से)",
        "cols": [["१ से १४", ["१ त्वचाएँ", "२ कलाएँ", "३ दोष", "४ धातु", "५ मल", "६ ज्ञानेन्द्रियाँ",
                              "७ उनके अधिष्ठान", "८ कर्मेन्द्रियाँ", "९ अतीन्द्रिय", "१० आशय", "११ प्राणायतन",
                              "१२ कण्डरा", "१३ जाल", "१४ कूर्च"]],
                 ["१५ से २८", ["१५ रज्जुक-सीवनी", "१६ अस्थिसंघात", "१७ सीमन्त", "१८ अस्थियाँ", "१९ अस्थिसन्धियाँ",
                               "२० स्नायु", "२१ पेशियाँ", "२२ सिरा", "२३ धमनी", "२४ स्रोतस्",
                               "२५ (अनुमानित: अग्नि) ऊष्माएँ", "२६ मर्म", "२७ केश, श्मश्रु, रोम",
                               "२८ प्रकृति-विकृति के भेद"]]],
    },
    ("31", "chain"): {
        "file": "sh5-santanika-31.svg",
        "alt": ("Chain of unit 31: blood (asṛj); being cooked (whether this goes with blood or milk is not settled); "
                "like the creamy films of milk; six skins come into being."),
        "type": "chain",
        "title": "इकाई ३१: छह त्वचाएँ कैसे बनती हैं",
        "steps": ["रक्त (असृज्)", "पकता हुआ (रक्त या दूध: तय नहीं)", "दूध की मलाई की परतों जैसा",
                  "छह त्वचाएँ बनती हैं"],
    },
    ("32", "chain"): {
        "file": "sh5-tvakprasada-32.svg",
        "alt": "Chain of unit 32: the clarity (prasāda) of the skin; from it (ablative); the clarity of the blood.",
        "type": "chain",
        "title": "इकाई ३२: त्वचा और रक्त का प्रसाद",
        "steps": ["त्वचा का प्रसाद (निर्मलता)", "उससे (पंचमी: प्रसादात्)", "रक्त का प्रसाद"],
    },
    ("35", "diagram"): {
        "file": "sh5-sidhma-kilasa-35.svg",
        "alt": ("Table of unit 35: the third skin is the seat of sidhma (a patchy skin disease, probably pityriasis "
                "versicolor; disputed) and kilāsa (probably vitiligo; probable)."),
        "type": "table",
        "title": "इकाई ३५: तीसरी त्वचा का अधिष्ठान",
        "heads": ["रोग", "पहचान (चिह्न सहित)"],
        "rows": [["सिध्म", "चकत्तेदार त्वचा-रोग, सम्भवतः छीप (विवादित)"],
                 ["किलास", "सम्भवतः सफ़ेद दाग (सम्भावित)"]],
    },
    ("37", "diagram"): {
        "file": "sh5-vidradhi-37.svg",
        "alt": ("Table of unit 37: the fifth skin is the seat of alajī (printed aljī; a skin eruption, identity uncertain) "
                "and vidradhi (abscess; standard)."),
        "type": "table",
        "title": "इकाई ३७: पाँचवीं त्वचा का अधिष्ठान",
        "heads": ["रोग", "पहचान (चिह्न सहित)"],
        "rows": [["अलजी (छपा: अल्जी)", "त्वचा-विस्फोट, पहचान अनिश्चित"],
                 ["विद्रधि", "फोड़ा (मानक)"]],
    },
}
