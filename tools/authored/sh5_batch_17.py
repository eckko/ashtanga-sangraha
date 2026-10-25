from helpers import mcq, match, order, fill, multi, accepts


AUTHORED = {}

# ---------------------------------------------------------------- unit 204
AUTHORED["204"] = {
    "title": "स्त्रीणां तु विंशतिरधिका",
    "question": "By unit 204, what does the text add for women?",
    "rule": ("In women (स्त्रीणाम्), however (तु), twenty (विंशतिः) more (अधिका). No verb and no counted noun are "
             "printed; the count is probably of peśī (muscles), carried from the preceding count."),
    "limits": ("Prose, elliptical. The counted noun (probably peśī, muscles) is neither printed nor supplied, so no "
               "question asks what is counted. The line does not restate the total to which the twenty are added."),
    "explain_hi": ("यह छोटी गद्य-पंक्ति कहती है: स्त्रियों में तो बीस अधिक। "
                   "‘तु’ (तो, परन्तु) पिछली गिनती से अन्तर दिखाता है। "
                   "गिनी गई वस्तु और क्रिया छपी नहीं; पिछली गिनती से सम्भवतः पेशियाँ (मांसपेशियाँ) समझी जाती हैं, पर यह शब्द जोड़ा नहीं गया। "
                   "‘विंशतिरधिका’ = विंशतिः + अधिका: इ के बाद का विसर्ग स्वर से पहले र् बना। "
                   "इकाई २०५ ‘तत्र’ (उनमें) कहकर आगे बढ़ती है।"),
    "hook": "स्त्रियों में बीस अधिक।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 204, how many more are counted in women?",
            ("Twenty", "विंशतिः is twenty: स्त्रीणां तु विंशतिरधिका."),
            [("Ten", "The line says विंशतिः, twenty, not ten."),
             ("Thirty", "The line says विंशतिः, twenty, not thirty."),
             ("Five", "The line says विंशतिः, twenty, not five.")],
            "In women, however, twenty more.",
            "विंशतिः = twenty; अधिका = more."),
        order(1, "Put the words of unit 204 in the line's order (the joined word is shown split).",
              ["स्त्रीणाम्", "तु", "विंशतिः", "अधिका"],
              "स्त्रीणां तु विंशतिरधिका: in women, however, twenty more.",
              "स्त्रीणाम् → तु → विंशतिः → अधिका."),
        match(2, "Match each word of unit 204 to its meaning.",
              [["स्त्री", "woman"], ["तु", "however"], ["विंशति", "twenty"], ["अधिक", "more, in excess"]],
              "In women (स्त्रीणाम्), however (तु), twenty (विंशतिः) more (अधिका).",
              "स्त्री, तु, विंशति, अधिक.", role="extend",
              teaches="अधिका is feminine, agreeing with the feminine number word विंशतिः."),
        mcq("discriminate", 3, "Which split of विंशतिरधिका in unit 204 is right?",
            ("विंशतिः + अधिका", "After इ a visarga becomes र् before a vowel: विंशतिः + अधिका → विंशतिरधिका."),
            [("विंशति + रधिका", "रधिका is not a word; the word is अधिका (more)."),
             ("विंशती + अधिका", "ई before अ would give य्: विंशत्यधिका, not विंशतिरधिका."),
             ("विंशतिर + धिका", "Neither विंशतिर nor धिका is a word; र् is the visarga's form.")],
            "विंशतिः (twenty) + अधिका (more): इः before a vowel → इर्.",
            "Visarga after a vowel other than अ/आ → र् before a voiced sound."),
        multi("apply", 4, "Which statements fit unit 204?",
              [("It speaks of women (स्त्रीणाम्)", "Right: स्त्रीणाम् = of / in women."),
               ("It prints the word for muscles (पेशी)", "No word for muscles is printed; peśī is only probable."),
               ("It gives the number twenty (विंशतिः)", "Right: विंशतिः अधिका, twenty more."),
               ("It prints a verb (भवन्ति)", "No verb is printed; the line is elliptical.")],
              [0, 2],
              "Women and the number twenty are printed; the counted noun and the verb are not.",
              "स्त्रीणां तु विंशतिरधिका."),
        mcq("transfer", 5, "By the rule of विंशतिः + अधिका, how is हरिः + अत्र (Hari here) joined in a new example?",
            ("हरिरत्र", "After इ a visarga becomes र् before a vowel, as विंशतिः + अधिका → विंशतिरधिका."),
            [("हरोऽत्र", "ओऽ comes from अः before अ; here the vowel before the visarga is इ."),
             ("हर्यत्र", "य् comes from a bare इ before a vowel; हरिः has a visarga, which becomes र्."),
             ("हरिस्त्र", "स् comes from a visarga before त or थ, not before a vowel.")],
            "हरिः + अत्र = हरिरत्र, like विंशतिः + अधिका = विंशतिरधिका.",
            "इः + vowel → इर्.",
            teaches="After a vowel other than अ/आ, a visarga becomes र् before a voiced sound: विंशतिः + अधिका → विंशतिरधिका."),
    ],
}

# ---------------------------------------------------------------- unit 205
AUTHORED["205"] = {
    "title": "तत्र दशस्तनयोः",
    "question": "By unit 205, where are ten placed, and when does the increase take place?",
    "rule": ("Among these (तत्र), ten are in the two breasts (स्तनयोः). Their (तासाम्) increase (परिवृद्धिः) takes "
             "place (भवति) in youth (यौवने)."),
    "limits": ("Prose. The counted noun is not printed (probably peśī). Whose increase तासाम् means (the ten of the "
               "breasts, or the peśī generally) is not stated: no question on it. स्तनयोः is read 'in the two breasts' "
               "as the data has it; no question turns on its case."),
    "explain_hi": ("यह गद्य-पंक्ति ‘तत्र’ (उनमें) से शुरू होती है और कहती है: दस दोनों स्तनों में हैं। "
                   "फिर दूसरा वाक्य: उनकी परिवृद्धि (बढ़ना) यौवन में होती है। "
                   "‘तासाम्’ (उनकी) किसकी ओर है, यह नहीं कहा गया: स्तनों वाली दस की ओर, या सामान्य रूप से पेशियों की ओर। "
                   "छपाई में ‘दशस्तनयोः’ एक साथ है, पर ये दो शब्द हैं: दश स्तनयोः। "
                   "‘परिवृद्धिर्भवति’ में घोष व्यंजन भ से पहले इ के बाद का विसर्ग र् बना।"),
    "hook": "स्तनों में दस; बढ़त यौवन में।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 205, how many are placed in the two breasts?",
            ("Ten", "दश स्तनयोः: ten in the two breasts."),
            [("Twenty", "The line says दश, ten, in the breasts, not twenty."),
             ("Three", "The line says दश, ten, not three."),
             ("Two", "स्तनयोः is dual (two breasts); the number is दश, ten.")],
            "Ten are in the two breasts.",
            "दश = ten; स्तनयोः = in the two breasts."),
        order(1, "Put the printed words of unit 205 in the line's order.",
              ["तत्र", "दशस्तनयोः", "तासां", "यौवने", "परिवृद्धिर्भवति"],
              "Among these, ten in the two breasts; their increase takes place in youth.",
              "तत्र → दशस्तनयोः → तासाम् → यौवने → परिवृद्धिर्भवति."),
        match(2, "Match each word of unit 205 to its meaning.",
              [["तत्र", "among these"], ["स्तन", "breast"], ["यौवन", "youth"], ["परिवृद्धि", "increase"],
               ["भवति", "takes place"]],
              "Among these, ten in the two breasts; their increase takes place in youth.",
              "तत्र, स्तन, यौवन, परिवृद्धि, भवति.", role="extend",
              teaches="यौवने is the locative singular of यौवन (youth): 'in youth'."),
        mcq("discriminate", 3, "By unit 205, when does the increase (परिवृद्धि) take place?",
            ("In youth", "तासां यौवने परिवृद्धिर्भवति: their increase takes place in youth."),
            [("In childhood", "The line says यौवने, in youth, not in childhood."),
             ("In old age", "The line says यौवने, in youth, not in old age."),
             ("At birth", "The line says यौवने, in youth, not at birth.")],
            "The increase takes place in youth (यौवने).",
            "यौवने = in youth."),
        mcq("apply", 4, "Which split of परिवृद्धिर्भवति in unit 205 is right?",
            ("परिवृद्धिः + भवति", "After इ a visarga becomes र् before a voiced consonant such as भ."),
            [("परिवृद्धि + र्भवति", "र्भवति is not a word; the verb is भवति."),
             ("परिवृद्धिर + भवति", "परिवृद्धिर is not a word; the noun is परिवृद्धिः."),
             ("परिवृद्धिम् + भवति", "म् before भ would be written ं (परिवृद्धिं भवति), not र्.")],
            "परिवृद्धिः (increase) + भवति (takes place): इः before भ → इर्.",
            "Visarga after a vowel other than अ/आ → र् before a voiced sound."),
        mcq("transfer", 5, "By the pattern of यौवने (in youth, from यौवन), how is in old age said from वार्धक्य?",
            ("वार्धक्ये", "An अ-stem takes -ए for 'in': यौवन → यौवने, वार्धक्य → वार्धक्ये."),
            [("वार्धक्यम्", "वार्धक्यम् is the nominative/accusative, not 'in old age'."),
             ("वार्धक्येन", "वार्धक्येन is the instrumental, 'by old age'."),
             ("वार्धक्यात्", "वार्धक्यात् is the ablative, 'from old age'.")],
            "वार्धक्ये = in old age, like यौवने = in youth.",
            "अ-stem + -ए = locative singular, 'in'.",
            teaches="यौवने is the locative singular of यौवन: -ए on an अ-stem means 'in, at (a time)'."),
    ],
}

# ---------------------------------------------------------------- unit 206
AUTHORED["206"] = {
    "title": "दश योनौ",
    "question": "By unit 206, how many are placed in the yoni?",
    "rule": ("Ten (दश) in the yoni (योनौ; yoni = female genital tract, probable). No verb and no counted noun are "
             "printed."),
    "limits": ("Prose, two words, elliptical. The counted noun (probably peśī) is neither printed nor supplied. "
               "yoni = female genital tract, probably including the vagina (probable); the card keeps the Sanskrit term."),
    "explain_hi": ("यह दो शब्दों की गद्य-पंक्ति है: दस, योनि में। "
                   "योनि = सम्भवतः स्त्री का जननमार्ग, सम्भवतः योनि-नलिका सहित (सम्भावित पहचान); इसलिए संस्कृत शब्द ही रखा गया। "
                   "‘योनौ’ इकारान्त स्त्रीलिंग ‘योनि’ का सप्तमी एकवचन है: योनि में। "
                   "गिनी गई वस्तु और क्रिया छपी नहीं; पिछली गिनती से सम्भवतः पेशियाँ। "
                   "इकाई २०५ के स्तनों वाले दस के बाद यहाँ दूसरे दस आते हैं।"),
    "hook": "दस योनि में।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 206, how many are placed in the yoni?",
            ("Ten", "दश योनौ: ten in the yoni."),
            [("Three", "The line says दश, ten, not three."),
             ("Twenty", "The line says दश, ten, not twenty."),
             ("Two", "The line says दश, ten, not two.")],
            "Ten in the yoni.",
            "दश = ten; योनौ = in the yoni."),
        match(1, "Match each word of unit 206 to its meaning.",
              [["दश", "ten"], ["योनि", "yoni (female genital tract, probable)"], ["योनौ", "in the yoni"]],
              "दश योनौ = ten in the yoni.",
              "दश, योनि, योनौ."),
        fill(2, "In unit 206 the number 'ten' is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("दश", "daśa"),
             "दश = ten; योनौ = in the yoni.",
             "दश = ten.",
             "दश योनौ."),
        mcq("discriminate", 3, "Which form is योनौ in unit 206?",
            ("Locative singular: in the yoni", "An इ-stem like योनि takes -औ in the locative singular."),
            [("Nominative singular: the yoni", "The nominative singular is योनिः."),
             ("Genitive singular: of the yoni", "The genitive singular is योनेः (or योन्याः)."),
             ("Nominative dual: two yonis", "The nominative dual is योनी.")],
            "योनौ = in the yoni, locative singular of योनि.",
            "इ-stem + -औ = locative singular."),
        multi("apply", 4, "Which statements fit unit 206?",
              [("It prints the counted noun peśī", "No counted noun is printed; peśī is only probable."),
               ("It names a number: ten", "Right: दश."),
               ("It prints the verb 'are'", "No verb is printed; the line is elliptical."),
               ("It names the place in the locative", "Right: योनौ, in the yoni.")],
              [1, 3],
              "A number and a place are printed; the counted noun and the verb are not.",
              "दश योनौ: number + place."),
        mcq("transfer", 5, "By the pattern of योनौ (in the yoni, from योनि), how is on the ground said from भूमि?",
            ("भूमौ", "An इ-stem takes -औ in the locative singular: योनि → योनौ, भूमि → भूमौ."),
            [("भूमिम्", "भूमिम् is the accusative, 'the ground' as object."),
             ("भूमेः", "भूमेः is the genitive or ablative, 'of / from the ground'."),
             ("भूमे", "भूमे is the vocative, 'O earth'.")],
            "भूमौ = on the ground, like योनौ = in the yoni.",
            "इ-stem + -औ = locative singular.",
            teaches="योनौ is the locative singular of the इ-stem योनि: -औ means 'in, on'."),
    ],
}

# ---------------------------------------------------------------- unit 207
AUTHORED["207"] = {
    "title": "अभ्यंतराश्रिते द्वे मुखाश्रिते",
    "question": "By unit 207, how are two groups of 'those' described?",
    "rule": ("Of those (तासाम्): two resting inside (अभ्यन्तराश्रिते द्वे); resting at the mouth (मुखाश्रिते), round "
             "(वृत्ते), two (द्वे)."),
    "limits": ("Low confidence. Printed counts (2 + 2 here, 3 in unit 208) give seven against the ten of unit 206; a "
               "द्वे may be lost: no question on counts, nor on whether वृत्ते (round) describes the ones at the mouth. "
               "Owner and counted noun are not printed."),
    "explain_hi": ("यह गद्य-पंक्ति कम विश्वास वाली है। "
                   "छपा पाठ: ‘उनमें दो भीतर टिकी हुई; मुख पर टिकी हुई, गोल, दो’। "
                   "‘तासाम्’ (उनमें) किसकी ओर है, यह पंक्ति में नहीं कहा गया; डेटा इन गिनतियों को इकाई २०६ के दस से मिलाकर देखता है। "
                   "गिनती छपे रूप में ही रखी गई: यहाँ २ + २, इकाई २०८ में ३; यह दस से कम है, और इकाई २०९ शायद एक और देती है, या स्कैन से कोई ‘द्वे’ छूट गया हो। "
                   "इसलिए गिनती पर कोई प्रश्न नहीं। "
                   "‘अभ्यन्तराश्रिते’ = अभ्यन्तर (भीतर) + आश्रिते (टिकी हुई): अ + आ → आ।"),
    "hook": "भीतर टिकी दो; मुख पर टिकी, गोल, दो (छपे पाठ में)।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "Which of these words is printed in unit 207?",
            ("वृत्ते (round)", "वृत्त = round; the line prints वृत्ते."),
            [("श्वेते (white)", "श्वेत is a colour and is not printed in unit 207."),
             ("कृष्णे (dark)", "कृष्ण is a colour and is not printed in unit 207."),
             ("चतुरस्रे (square)", "चतुरस्र (square) is not printed; the word is वृत्ते, round.")],
            "The line prints वृत्ते, round.",
            "वृत्त = round."),
        order(1, "Put the printed parts of unit 207 in the line's order.",
              ["तासाम्", "अभ्यंतराश्रिते द्वे", "मुखाश्रिते", "वृत्ते द्वे"],
              "Of those: two resting inside; resting at the mouth, round, two.",
              "तासाम् → अभ्यन्तराश्रिते द्वे → मुखाश्रिते → वृत्ते द्वे."),
        match(2, "Match each word of unit 207 to its meaning.",
              [["अभ्यन्तर", "inside"], ["मुख", "mouth"], ["आश्रित", "resting on, lodged at"], ["वृत्त", "round"],
               ["द्वे", "two"]],
              "Two resting inside; resting at the mouth, round, two.",
              "अभ्यन्तर, मुख, आश्रित, वृत्त, द्वे.", role="extend",
              teaches="आश्रित after a place word makes 'resting at that place': मुखाश्रिते = resting at the mouth."),
        mcq("discriminate", 3, "Which split of मुखाश्रिते in unit 207 is right?",
            ("मुख + आश्रिते", "अ + आ → आ: मुख + आश्रिते → मुखाश्रिते."),
            [("मुखा + श्रिते", "मुखा is not the word, and श्रिते has lost the आ of आश्रिते."),
             ("मुख + श्रिते", "With no आ the join would be मुखश्रिते, a short अ."),
             ("मुखे + आश्रिते", "ए before आ does not merge into आ.")],
            "मुख (mouth) + आश्रिते (resting at): अ + आ → आ.",
            "अ + आ → आ."),
        multi("apply", 4, "Which statements fit unit 207 as the card reads it?",
              [("It prints the word दीर्घे (long)", "No word for long is printed in unit 207."),
               ("Two rest inside (अभ्यन्तर)", "Right: अभ्यन्तराश्रिते द्वे."),
               ("It prints the word वृत्ते (round)", "Right: वृत्ते is printed after मुखाश्रिते."),
               ("Two rest in the breasts (स्तन)", "Unit 207 does not name the breasts.")],
              [1, 2],
              "Two rest inside, and the word वृत्ते (round) is printed after मुखाश्रिते.",
              "अभ्यन्तराश्रिते द्वे; मुखाश्रिते वृत्ते द्वे."),
        mcq("transfer", 5, "By the rule of मुख + आश्रिते, how is हिम + आलयः (abode of snow) joined in a new example?",
            ("हिमालयः", "अ + आ → आ, as मुख + आश्रिते → मुखाश्रिते."),
            [("हिमआलयः", "Two vowels side by side inside a word must join; अ + आ gives आ."),
             ("हिमेलयः", "ए comes from अ + इ, not from अ + आ."),
             ("हिमौलयः", "औ comes from अ + ओ or औ, not from अ + आ.")],
            "हिम + आलयः = हिमालयः, like मुख + आश्रिते = मुखाश्रिते.",
            "अ + आ → आ.",
            teaches="अ + आ → आ: मुख + आश्रिते → मुखाश्रिते; अभ्यन्तर + आश्रिते → अभ्यन्तराश्रिते."),
    ],
}

# ---------------------------------------------------------------- unit 208
AUTHORED["208"] = {
    "title": "तिस्रो गर्भमार्गाश्रयाः",
    "question": "By unit 208, where do the three rest?",
    "rule": ("Three (तिस्रः) resting on the path of the fetus (गर्भमार्ग-आश्रयाः); garbhamārga is probably the birth "
             "passage. तिस्रः is feminine, consistent with peśī."),
    "limits": ("Prose, elliptical: the counted noun is not printed (feminine तिस्रः fits peśī; nothing supplied). "
               "'Birth passage' for garbhamārga is probable only. How these three fit the ten of unit 206 is left open "
               "(see unit 207): no question on totals."),
    "explain_hi": ("यह दो शब्दों की गद्य-पंक्ति है: तीन, गर्भ के मार्ग पर टिकी हुई। "
                   "गर्भमार्ग = गर्भ का मार्ग, सम्भवतः प्रसव-मार्ग (सम्भावित)। "
                   "‘तिस्रः’ स्त्रीलिंग है, जो स्त्रीलिंग ‘पेशी’ से मेल खाता है; पर संज्ञा छपी नहीं। "
                   "‘तिस्रो’: घोष व्यंजन ग से पहले अः का ओ हुआ (तिस्रः + गर्भ... → तिस्रो गर्भ...)। "
                   "यह गिनती इकाई २०६ के दस में कैसे बैठती है, यह खुला है (देखें इकाई २०७)।"),
    "hook": "तीन गर्भ-मार्ग पर।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 208, how many rest on the path of the fetus?",
            ("Three", "तिस्रो गर्भमार्गाश्रयाः: three resting on the path of the fetus."),
            [("Two", "The line says तिस्रः, three, not two."),
             ("Ten", "The line says तिस्रः, three, not ten."),
             ("Twenty", "The line says तिस्रः, three, not twenty.")],
            "Three rest on the path of the fetus.",
            "तिस्रः = three (feminine)."),
        match(1, "Match each part of unit 208 to its meaning.",
              [["तिस्रः", "three"], ["गर्भ", "fetus"], ["मार्ग", "path"], ["आश्रय", "resting on"]],
              "तिस्रो गर्भमार्गाश्रयाः: three resting on the path of the fetus.",
              "तिस्रः, गर्भ, मार्ग, आश्रय."),
        fill(2, "In unit 208 the word for 'path' is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("मार्ग", "mārga", "marga"),
             "मार्ग = path; गर्भमार्ग = the path of the fetus (probably the birth passage).",
             "मार्ग = path, way; गर्भमार्ग = the path of the fetus, probably the birth passage (probable).",
             "गर्भ + मार्ग + आश्रय."),
        mcq("discriminate", 3, "Why is तिस्रः printed तिस्रो before गर्भ in unit 208?",
            ("अः before a voiced consonant becomes ओ", "ग is a voiced consonant: तिस्रः + गर्भ... → तिस्रो गर्भ..."),
            [("अः before any consonant becomes ओ", "Before an unvoiced consonant it does not: तिस्रः + तत्र → तिस्रस्तत्र."),
             ("ओ is the plain ending of 'three'", "The word is तिस्रः; ओ is its form before ग."),
             ("A final म् before ग becomes ओ", "म् before a consonant gives ं, never ओ.")],
            "तिस्रः + गर्भ...: अः before the voiced consonant ग → ओ.",
            "अः + voiced consonant → ओ."),
        mcq("apply", 4, "In unit 208, which reading of गर्भमार्ग does the card give?",
            ("The path of the fetus, probably the birth passage", "मार्ग = path; the data: probably the birth passage."),
            [("The bed of the fetus, probably the uterus", "That is गर्भशय्या (unit 210); मार्ग means path."),
             ("The food of the fetus, probably what the mother eats", "मार्ग means path, not food."),
             ("The cover of the fetus, probably its membranes", "मार्ग means path, not cover.")],
            "गर्भमार्ग = the path of the fetus, probably the birth passage (probable).",
            "गर्भ + मार्ग = path of the fetus."),
        mcq("transfer", 5, "By the rule of तिस्रः + गर्भ, how is पुत्रः + हसति (the son laughs) joined in a new example?",
            ("पुत्रो हसति", "अः before a voiced consonant becomes ओ, as तिस्रः + गर्भ... → तिस्रो गर्भ..."),
            [("पुत्रर्हसति", "र् comes from a visarga after vowels other than अ/आ; here it is अः."),
             ("पुत्रस्हसति", "स् comes from a visarga before त or थ, not before ह."),
             ("पुत्र हसति", "अः drops to अ before vowels other than अ, not before a consonant.")],
            "पुत्रः + हसति = पुत्रो हसति, like तिस्रः + गर्भ... = तिस्रो गर्भ...",
            "अः + voiced consonant → ओ.",
            teaches="अः before a voiced consonant becomes ओ: तिस्रः + गर्भमार्गाश्रयाः → तिस्रो गर्भमार्गाश्रयाः."),
    ],
}

# ---------------------------------------------------------------- unit 209
AUTHORED["209"] = {
    "title": "यस्यांगर्भ स्तिष्ठति",
    "question": "By unit 209, what is said to stay in the place this clause describes?",
    "rule": ("In which (यस्याम्, feminine) the fetus (गर्भः) stays (तिष्ठति). A relative clause with no antecedent "
             "and no main clause in the unit."),
    "limits": ("Low confidence. A bare relative clause: it may continue unit 208 or describe a further member of the count "
               "(a numeral may be missing; nothing supplied). No question asks what 'in which' refers to. The print "
               "divides the words wrongly: यस्यांगर्भ स्तिष्ठति = यस्यां गर्भस्तिष्ठति."),
    "explain_hi": ("यह एक छोटा सम्बन्धवाचक वाक्य है: ‘जिसमें गर्भ ठहरता है’। "
                   "‘यस्याम्’ स्त्रीलिंग सप्तमी एकवचन है (जिसमें), पर ‘जिस’ किसकी ओर है, यह पंक्ति में नहीं; यह इकाई २०८ से जुड़ सकता है, "
                   "या गिनती का एक और सदस्य बताता हो (कोई संख्या छूटी हो सकती है)। इसलिए इस पर कोई प्रश्न नहीं। "
                   "छपाई में शब्द-विभाजन गलत जगह है: ‘यस्यांगर्भ स्तिष्ठति’ = यस्यां गर्भस्तिष्ठति; त से पहले विसर्ग स् बना। "
                   "‘तिष्ठति’ √स्था का वर्तमान काल है: ठहरता है।"),
    "hook": "जिसमें गर्भ ठहरता है।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 209, what stays (तिष्ठति) in the place the clause describes?",
            ("The fetus", "यस्यां गर्भस्तिष्ठति: in which the fetus (गर्भः) stays."),
            [("The semen", "The subject is गर्भः, the fetus, not semen."),
             ("The menstrual blood", "The subject is गर्भः, the fetus, not menstrual blood."),
             ("The breast milk", "The subject is गर्भः, the fetus, not milk.")],
            "In which the fetus stays.",
            "गर्भः तिष्ठति = the fetus stays."),
        order(1, "Put the words of unit 209 (split as the card reads them) in the line's order.",
              ["यस्याम्", "गर्भः", "तिष्ठति"],
              "यस्यां गर्भस्तिष्ठति: in which the fetus stays.",
              "यस्याम् → गर्भः → तिष्ठति."),
        match(2, "Match each word of unit 209 to its meaning.",
              [["यस्याम्", "in which"], ["गर्भ", "fetus"], ["तिष्ठति", "stays"]],
              "यस्यां गर्भस्तिष्ठति = in which the fetus stays.",
              "यस्याम्, गर्भ, तिष्ठति.", role="extend",
              teaches="तिष्ठति = stays, stands: the present tense of √स्था."),
        mcq("discriminate", 3, "The print has गर्भ स्तिष्ठति. How does the card read it?",
            ("गर्भः तिष्ठति: visarga before त becomes स्", "गर्भः + तिष्ठति → गर्भस्तिष्ठति; the print puts the space after गर्भ."),
            [("गर्भ स्तिष्ठति: a verb form स्तिष्ठति", "There is no verb स्तिष्ठति; the verb is तिष्ठति."),
             ("गर्भम् + तिष्ठति: an accusative गर्भम्", "म् before त is written ं (गर्भं तिष्ठति); it never gives स्."),
             ("गर्भे + तिष्ठति: in the fetus it stays", "ए before त stays ए; it would not give स्.")],
            "गर्भः (the fetus) + तिष्ठति (stays): visarga before त → स्.",
            "Visarga before त/थ → स्."),
        multi("apply", 4, "Which statements fit unit 209 as the card reads it?",
              [("It names what 'in which' refers to", "No antecedent is printed in the unit."),
               ("It prints a numeral for a count", "No numeral is printed; one may be missing."),
               ("It has a relative word, यस्याम्", "Right: यस्याम्, in which (feminine)."),
               ("Its verb तिष्ठति means 'stays'", "Right: √स्था, stays.")],
              [2, 3],
              "A relative clause: in which the fetus stays; no antecedent and no numeral.",
              "यस्यां गर्भस्तिष्ठति."),
        mcq("transfer", 5, "By the pattern of यस्याम् + गर्भः → यस्यां गर्भः, how is फलम् + खादति (eats the fruit) written in a sentence?",
            ("फलं खादति", "Final म् before a consonant inside a sentence is written ं, as यस्यां गर्भः."),
            [("फलो खादति", "ओ comes from अः before a voiced consonant; here the word ends in म्."),
             ("फलः खादति", "There is no visarga in फलम्; its म् becomes ं."),
             ("फलन्खादति", "न् is not the nasal of क; the म् is written ं.")],
            "फलम् + खादति = फलं खादति, like यस्याम् + गर्भः = यस्यां गर्भः.",
            "Final म् + consonant (in a sentence) → ं.",
            teaches="A final म् before a consonant inside a sentence is written ं: यस्याम् + गर्भः → यस्यां गर्भः."),
    ],
}

# ---------------------------------------------------------------- unit 210
AUTHORED["210"] = {
    "title": "योनि का आकार और गर्भशय्या",
    "question": "By unit 210, what shape is the yoni, and where and of what shape is the garbhaśayyā?",
    "rule": ("The yoni is shaped like a conch's navel (शङ्खनाभ्याकृतिः). In its third whorl (तृतीये आवर्ते), between "
             "pitta and the pakvāśaya, lies the garbhaśayyā (probably the uterus), shaped like a rohita fish's mouth."),
    "limits": ("Low confidence. Printed उद्यावर्त्ता is not a word; 'three-whorled' (त्र्यावर्ता) is a conjecture: no "
               "question on it. 'pitta' may stand for the seat of pitta; kept as printed. yoni (female genital tract), "
               "pakvāśaya (large intestine region) and garbhaśayyā (uterus) are probable; rohita = rohu carp is standard."),
    "explain_hi": ("यह गद्य-पंक्ति योनि और गर्भशय्या का वर्णन करती है। "
                   "योनि (सम्भवतः स्त्री का जननमार्ग) शंख की नाभि जैसे आकार की है। "
                   "छपा ‘उद्यावर्त्ता’ कोई शब्द नहीं; आगे ‘तीसरा आवर्त’ आने से अनुमानित पाठ ‘त्र्यावर्ता’ (तीन आवर्तों वाली) है, यह केवल अनुमान है। "
                   "उसके तीसरे आवर्त (चक्कर) में, पित्त और पक्वाशय (सम्भवतः बड़ी आँत का क्षेत्र) के बीच, गर्भशय्या (गर्भ की शय्या, सम्भवतः गर्भाशय) है, "
                   "जिसका आकार रोहित मछली (रोहू, मानक पहचान) के मुख जैसा है। "
                   "‘पित्त’ शायद पित्त के आशय के लिए है; छपा रूप ही रखा गया।"),
    "hook": "शंख-नाभि जैसी योनि; तीसरे आवर्त में रोहित-मुख जैसी गर्भशय्या।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 210, the garbhaśayyā is shaped like the mouth of which creature?",
            ("A rohita fish", "रोहितमत्स्यमुखाकारा: shaped like the mouth of a rohita fish (rohu carp)."),
            [("A water snake", "No snake is named; the line names the rohita fish."),
             ("A river turtle", "No turtle is named; the line names the rohita fish."),
             ("A pond frog", "No frog is named; the line names the rohita fish.")],
            "The garbhaśayyā is shaped like the mouth of a rohita fish (rohu carp, standard).",
            "रोहित + मत्स्य + मुख + आकारा."),
        order(1, "Put these printed parts of unit 210 in the line's order (the doubtful word is left out).",
              ["योनिस्तु", "तस्यास्तृतीय", "आवर्त्तेपित्तपक्वाशयांतरे", "रोहितमत्स्यमुखाकारा", "गर्भशय्या"],
              "The yoni ... in its third whorl, between pitta and the pakvāśaya, is the garbhaśayyā shaped like a rohita fish's mouth.",
              "योनिस्तु → तस्यास्तृतीय → आवर्त्ते... → रोहितमत्स्यमुखाकारा → गर्भशय्या."),
        match(2, "Match each word of unit 210 to its meaning.",
              [["शङ्खनाभि", "a conch's navel"], ["आवर्त", "whorl"], ["तृतीय", "third"],
               ["रोहित", "rohu carp (standard)"], ["गर्भशय्या", "bed of the fetus (probably the uterus)"]],
              "Shaped like a conch's navel; in its third whorl lies the garbhaśayyā, shaped like a rohita fish's mouth.",
              "शङ्खनाभि, आवर्त, तृतीय, रोहित, गर्भशय्या.", role="extend",
              teaches=("आकृति and आकार both mean shape: शङ्खनाभ्याकृतिः = shaped like a conch's navel; "
                       "रोहितमत्स्यमुखाकारा = shaped like a rohita fish's mouth.")),
        mcq("discriminate", 3, "By unit 210, where does the garbhaśayyā lie?",
            ("In the third whorl, between pitta and pakvāśaya", "तृतीये आवर्ते पित्तपक्वाशयान्तरे."),
            [("In the first whorl, between pitta and pakvāśaya", "The line says the third (तृतीये) whorl."),
             ("In the second whorl, between pitta and pakvāśaya", "The line says the third (तृतीये) whorl."),
             ("Outside the whorls, below the pakvāśaya, apart", "The line places it in the third whorl, in the interval.")],
            "In its third whorl, between pitta and the pakvāśaya, is the garbhaśayyā.",
            "तृतीये आवर्ते + पित्त-पक्वाशय-अन्तरे."),
        mcq("apply", 4, "The data reads printed तृतीय आवर्त्ते as तृतीये आवर्ते. Which rule gives the printed form?",
            ("ए becomes अय्; the य् drops and a gap is left", "तृतीये + आवर्ते → तृतीय आवर्ते (the य् may also be kept)."),
            [("ए and the next आ merge into one long आ", "That would give तृतीयावर्ते; the print keeps two words."),
             ("ए before a vowel turns into the vowel ई", "That would give तृतीयी; the print has तृतीय."),
             ("ए stays and the next vowel drops, shown by the ऽ sign", "That happens only before अ (एऽ); here आ stays.")],
            "तृतीये (in the third) + आवर्ते (whorl): ए + vowel → अय्, य् dropped, gap left.",
            "ए + vowel → अ(य्) + vowel."),
        mcq("transfer", 5, "By the same rule, how is वने + आस्ते (sits in the forest) joined in a new example?",
            ("वन आस्ते", "ए before a vowel → अय्, the य् dropped: वन आस्ते (वनयास्ते, keeping य्, is also right)."),
            [("वनास्ते", "After the य् drops the two vowels do not merge again."),
             ("वनेऽस्ते", "ऽ marks a dropped अ, but आस्ते begins with आ, which stays."),
             ("वनैस्ते", "ऐ comes from अ + ए or ऐ, not from ए + आ.")],
            "वने + आस्ते = वन आस्ते, like तृतीये + आवर्ते = तृतीय आवर्ते.",
            "ए + vowel → अ(य्) + vowel.",
            teaches="ए before a vowel becomes अय्; the य् is commonly dropped, leaving a gap: तृतीये + आवर्ते → तृतीय आवर्ते."),
    ],
}

# ---------------------------------------------------------------- unit 211
AUTHORED["211"] = {
    "title": "तस्यां शुक्रार्त्तवप्रवेशिन्यस्तिस्रः पेश्यः",
    "question": "By unit 211, how many peśī are in it, and with which two fluids are they linked?",
    "rule": ("In it (तस्याम्) are three peśī (muscles) entering (प्रवेशिन्यः; or admitting) śukra (semen) and ārtava (menstrual "
             "blood, probable)."),
    "limits": ("Prose. What 'it' (तस्याम्, feminine) refers to is not stated: no question on it. प्रवेशिनी is rendered "
               "'entering'; 'admitting, receiving' is an alternative sense, and no question turns on it. ārtava = "
               "menstrual blood is probable."),
    "explain_hi": ("इस गद्य-पंक्ति में गिनी गई वस्तु स्पष्ट छपी है: ‘पेश्यः’, पेशियाँ (मांसपेशियाँ)। "
                   "उसमें तीन पेशियाँ हैं जो शुक्र (वीर्य) और आर्तव (सम्भवतः मासिक धर्म का रक्त) में प्रवेश करने वाली हैं। "
                   "‘प्रवेशिनी’ का शब्दार्थ ‘प्रवेश करने वाली’ है; ‘ग्रहण करने वाली’ अर्थ भी सम्भव है। "
                   "‘तस्याम्’ (उसमें) किसकी ओर है, यह डेटा नहीं बताता। "
                   "प्रवेशिन्यः + तिस्रः → प्रवेशिन्यस्तिस्रः: त से पहले विसर्ग स् बना।"),
    "hook": "उसमें तीन पेशियाँ, शुक्र-आर्तव में प्रवेश करने वाली।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 211, how many peśī (muscles) are named in it?",
            ("Three", "तिस्रः पेश्यः: three peśī."),
            [("Two", "The line says तिस्रः, three, not two."),
             ("Ten", "The line says तिस्रः, three, not ten."),
             ("Seven", "The line says तिस्रः, three, not seven.")],
            "Three peśī are named.",
            "तिस्रः पेश्यः = three muscles."),
        order(1, "Put the words of unit 211 in the line's order (the joined word is shown split).",
              ["तस्यां", "शुक्रार्त्तवप्रवेशिन्यः", "तिस्रः", "पेश्यः"],
              "In it are three peśī entering śukra and ārtava.",
              "तस्याम् → शुक्रार्तवप्रवेशिन्यः → तिस्रः → पेश्यः."),
        match(2, "Match each word of unit 211 to its meaning.",
              [["शुक्र", "semen"], ["आर्तव", "menstrual blood (probable)"], ["प्रवेशिनी", "entering (or admitting)"],
               ["पेशी", "muscle"], ["तिस्रः", "three"]],
              "Three peśī entering śukra (semen) and ārtava (menstrual blood, probable).",
              "शुक्र, आर्तव, प्रवेशिनी, पेशी, तिस्रः.", role="extend",
              teaches="पेशी = muscle (also 'strand of flesh'); its nominative plural is पेश्यः."),
        mcq("discriminate", 3, "Which split of प्रवेशिन्यस्तिस्रः in unit 211 is right?",
            ("प्रवेशिन्यः + तिस्रः", "Visarga before त becomes स्: प्रवेशिन्यः + तिस्रः → प्रवेशिन्यस्तिस्रः."),
            [("प्रवेशिन्य + स्तिस्रः", "स्तिस्रः is not a word; the number is तिस्रः."),
             ("प्रवेशिनी + अस्तिस्रः", "अस्तिस्रः is not a word; the number is तिस्रः."),
             ("प्रवेशिनी + स्तिस्रः", "स्तिस्रः is not a word, and प्रवेशिनी is singular; the line needs the plural प्रवेशिन्यः.")],
            "प्रवेशिन्यः (entering) + तिस्रः (three): visarga before त → स्.",
            "Visarga before त/थ → स्."),
        multi("apply", 4, "Which statements fit unit 211?",
              [("It names śukra and ārtava in one compound (शुक्रार्तव-)", "Right: शुक्रार्त्तवप्रवेशिन्यः names both."),
               ("They are four in number", "The line says तिस्रः, three."),
               ("The line names the breasts (स्तन)", "The breasts are not named in unit 211."),
               ("The counted noun peśī is printed", "Right: पेश्यः is printed.")],
              [0, 3],
              "Three peśī, printed as such; śukra and ārtava are named in one compound.",
              "तस्यां शुक्रार्तवप्रवेशिन्यस्तिस्रः पेश्यः."),
        mcq("transfer", 5, "By the rule of प्रवेशिन्यः + तिस्रः, how is देव्यः + तत्र (the goddesses there) joined in a new example?",
            ("देव्यस्तत्र", "Visarga before त becomes स्, as प्रवेशिन्यः + तिस्रः → प्रवेशिन्यस्तिस्रः."),
            [("देव्यो तत्र", "ओ comes from अः before a voiced consonant; त is unvoiced."),
             ("देव्यर्तत्र", "र् comes from a visarga after vowels other than अ/आ; here it is अः."),
             ("देव्य तत्र", "अः drops to अ only before vowels other than अ, not before त.")],
            "देव्यः + तत्र = देव्यस्तत्र, like प्रवेशिन्यः + तिस्रः = प्रवेशिन्यस्तिस्रः.",
            "Visarga + त → स्त.",
            teaches="A visarga before त or थ becomes स्: प्रवेशिन्यः + तिस्रः → प्रवेशिन्यस्तिस्रः."),
    ],
}

# ---------------------------------------------------------------- unit 212
AUTHORED["212"] = {
    "title": "ताभिर्हि शरीरे",
    "question": "By unit 212, what qualities are given to 'those', and what do they cover?",
    "rule": ("For by those (ताभिः, probably the peśī of unit 211), thin, dense, large, minute, broad, round, short, "
             "long, firm, soft, smooth and rough, the joints, bones, sirā and snāva in the body are covered."),
    "limits": ("Prose. That ताभिः means the peśī of unit 211 is probable, not stated. sirā (vessels) and snāva (sinews) "
               "are probable identifications. The line does not say which peśī has which quality. bahala (dense) and "
               "sthūla (large) are two separate members."),
    "explain_hi": ("यह गद्य-पंक्ति बताती है कि ‘उनसे’ (ताभिः, सम्भवतः इकाई २११ की पेशियाँ) शरीर में सन्धियाँ, अस्थियाँ, सिराएँ और स्नायु ढके हुए हैं। "
                   "उनके बारह गुण एक लम्बे समास में क्रम से हैं: तनु (पतली), बहल (घनी), स्थूल (बड़ी), अणु (सूक्ष्म), पृथु (चौड़ी), वृत्त (गोल), "
                   "ह्रस्व (छोटी), दीर्घ (लम्बी), स्थिर (दृढ़), मृदु (कोमल), श्लक्ष्ण (चिकनी), कर्कश (खुरदुरी)। "
                   "कौन-सी पेशी किस गुण की है, यह नहीं कहा गया। "
                   "‘हि’ का अनुवाद ‘क्योंकि’ किया गया है। "
                   "सिरा = वाहिनी और स्नाव = स्नायु (कण्डरा, स्नायु-बन्धन), दोनों सम्भावित पहचान।"),
    "hook": "बारह रूपों वाली ‘वे’ सन्धि, अस्थि, सिरा, स्नायु को ढकती हैं।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 212, what is covered (प्रच्छादितानि) in the body?",
            ("Joints, bones, sirā and snāva", "संध्यस्थिसिरास्नावानि प्रच्छादितानि."),
            [("Skin, hair, nails and teeth", "None of these is named in the list of unit 212."),
             ("Eyes, ears, nose and the tongue", "None of these is named in the list of unit 212."),
             ("Bones of the trunk and four limbs", "The list is joints, bones, sirā and snāva, not limbs and trunk.")],
            "The joints, bones, sirā and snāva in the body are covered.",
            "सन्धि + अस्थि + सिरा + स्नाव."),
        order(1, "Put the first six qualities of the long compound of unit 212 in the line's order.",
              ["तनु", "बहल", "स्थूल", "अणु", "पृथु", "वृत्त"],
              "Thin, dense, large, minute, broad, round: the first six of the twelve.",
              "तनु → बहल → स्थूल → अणु → पृथु → वृत्त."),
        match(2, "Match each quality of unit 212 to its meaning.",
              [["तनु", "thin"], ["बहल", "dense"], ["अणु", "minute"], ["ह्रस्व", "short"], ["श्लक्ष्ण", "smooth"],
               ["कर्कश", "rough"]],
              "Twelve qualities: thin, dense, large, minute, broad, round, short, long, firm, soft, smooth, rough.",
              "तनु, बहल, अणु, ह्रस्व, श्लक्ष्ण, कर्कश.", role="extend",
              teaches="बहल = dense, thick; it stands beside स्थूल (large) as a separate member of the list."),
        mcq("discriminate", 3, "Which split of संध्यस्थि in unit 212 is right?",
            ("सन्धि + अस्थि", "इ before an unlike vowel becomes य्: सन्धि + अस्थि → सन्ध्यस्थि."),
            [("सन्ध्य + अस्थि", "सन्ध्य is not the word, and अ + अ would give आ: सन्ध्यास्थि."),
             ("सन्धे + अस्थि", "ए + अ would give सन्धेऽस्थि, not सन्ध्यस्थि."),
             ("सन्धिः + अस्थि", "A first member has no ending; इः before a vowel would give सन्धिरस्थि.")],
            "सन्धि (joint) + अस्थि (bone): इ + अ → य.",
            "इ + unlike vowel → य् + that vowel."),
        multi("apply", 4, "Which of these qualities does unit 212 name?",
              [("Hot (उष्ण)", "उष्ण is not in the list."),
               ("Firm (स्थिर)", "Right: स्थिर is the ninth member."),
               ("Heavy (गुरु)", "गुरु is not in the list."),
               ("Long (दीर्घ)", "Right: दीर्घ is the eighth member.")],
              [1, 3],
              "Firm and long are in the list; hot and heavy are not.",
              "...ह्रस्व-दीर्घ-स्थिर-मृदु..."),
        mcq("transfer", 5, "By the rule of सन्धि + अस्थि, how is प्रति + अङ्गम् (each limb) joined in a new example?",
            ("प्रत्यङ्गम्", "इ before अ becomes य्, as सन्धि + अस्थि → सन्ध्यस्थि."),
            [("प्रतेङ्गम्", "ए comes from अ + इ, not from इ + अ."),
             ("प्रतीङ्गम्", "ई comes from इ + इ, not from इ + अ."),
             ("प्रत्याङ्गम्", "या would come from इ + आ, but अङ्गम् begins with a short अ.")],
            "प्रति + अङ्गम् = प्रत्यङ्गम्, like सन्धि + अस्थि = सन्ध्यस्थि.",
            "इ + अ → य.",
            teaches="इ before an unlike vowel becomes य्: सन्धि + अस्थि → सन्ध्यस्थि."),
    ],
}

# ---------------------------------------------------------------- unit 213
AUTHORED["213"] = {
    "title": "सिराधमनीमुखानां त्वणुशो",
    "question": "By unit 213, how many openings of the sirā and dhamanī are counted when divided minutely?",
    "rule": ("The openings (मुख) of the sirā and dhamanī (vessels), divided minutely (अणुशः), are twenty-nine "
             "hundred-thousands and nine hundred and fifty-six: 2,900,956 as printed."),
    "limits": ("Prose. The number is kept exactly as printed; another witness may read 29,956 (not applied): questions "
               "ask only for the printed figure. sirā and dhamanī are vessels with no firm modern split (probable: veins "
               "and arteries, or vessels generally). The openings are counted, not the vessels."),
    "explain_hi": ("यह गद्य-पंक्ति सिरा और धमनी के मुखों (छिद्रों) की गिनती देती है, जब उन्हें सूक्ष्म रूप से (अणुशः) बाँटा जाए। "
                   "संख्या: एकोनत्रिंशत् (उनतीस) शतसहस्र (लाख) = उनतीस लाख, और ‘नव शतानि षट्पञ्चाशानि’ = नौ सौ छप्पन; छपे रूप में कुल २९,००,९५६। "
                   "डेटा के अनुसार एक अन्य प्रति २९,९५६ पढ़ सकती है, पर वह पाठ लागू नहीं किया गया। "
                   "गिने गए हैं वाहिनियों के मुख, स्वयं वाहिनियाँ नहीं। "
                   "‘एकोनत्रिंशत्’ = एक + ऊन (कम) + त्रिंशत् (तीस): तीस में एक कम।"),
    "hook": "उनतीस लाख नौ सौ छप्पन मुख (छपे रूप में)।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 213, what is counted?",
            ("The openings of the sirā and dhamanī", "सिराधमनीमुखानाम्: of the openings of the sirā and dhamanī."),
            [("The joints of the bones and sinews", "Unit 213 counts the openings (मुख) of vessels, not joints."),
             ("The muscles of the limbs and trunk", "Unit 213 counts the openings (मुख) of vessels, not muscles."),
             ("The bones of the trunk and the four limbs", "Unit 213 counts the openings (मुख) of vessels, not bones.")],
            "The openings (mouths) of the sirā and dhamanī are counted.",
            "सिरा-धमनी-मुख = openings of the vessels."),
        order(1, "Put the parts of unit 213 in the line's order (one joined word is shown split).",
              ["सिराधमनीमुखानां", "त्वणुशो", "विभज्यमानानाम्", "एकोनत्रिंशच्छतसहस्राणि", "नव च शतानि षट्पंचाशानि",
               "भवंति"],
              "Of the openings of the vessels, divided minutely, there are 29 hundred-thousands and 956.",
              "मुखानाम् → अणुशः → विभज्यमानानाम् → एकोनत्रिंशच्छतसहस्राणि → नव च शतानि षट्पञ्चाशानि → भवन्ति."),
        match(2, "Match each word of unit 213 to its meaning.",
              [["एकोनत्रिंशत्", "twenty-nine"], ["शतसहस्र", "hundred-thousand"], ["नव", "nine"],
               ["अणुशः", "minutely"], ["मुख", "opening, mouth"]],
              "Of the openings, divided minutely: twenty-nine hundred-thousands and nine hundred and fifty-six.",
              "एकोनत्रिंशत्, शतसहस्र, नव, अणुशः, मुख.", role="extend",
              teaches="एकोनत्रिंशत् = एक + ऊन + त्रिंशत्, 'thirty less one' = twenty-nine (अ + ऊ → ओ)."),
        mcq("discriminate", 3, "Which split of त्वणुशो in unit 213 is right?",
            ("तु + अणुशः", "उ before अ becomes व्; अणुशः before the voiced व of विभज्य... becomes अणुशो."),
            [("तु + वणुशः", "वणुशः is not a word; the word is अणुशः (minutely)."),
             ("त्व + अणुशः", "त्व is not the word here; the particle is तु, and अ + अ would give आ."),
             ("तो + अणुशः", "ओ + अ would give तोऽणुशः, not त्वणुशो.")],
            "तु (however) + अणुशः (minutely): उ + अ → व.",
            "उ + unlike vowel → व् + that vowel."),
        mcq("apply", 4, "Written in figures, what total does unit 213 give as printed?",
            ("2,900,956", "29 × 100,000 = 2,900,000, plus nine hundred and fifty-six."),
            [("2,900,596", "The tail is nine hundred and fifty-six (956), not 596."),
             ("2,909,560", "The tail is 956 after 2,900,000; nothing is multiplied by ten."),
             ("290,956", "एकोनत्रिंशत् शतसहस्र is 29 hundred-thousands, 2,900,000, not 290,000.")],
            "As printed: 2,900,000 + 956 = 2,900,956.",
            "एकोनत्रिंशत् × शतसहस्र + नव शतानि षट्पञ्चाशानि."),
        mcq("transfer", 5, "By the rule of तु + अणुशः, how is सु + अल्पम् (very little) joined in a new example?",
            ("स्वल्पम्", "उ before अ becomes व्, as तु + अणुशः → त्वणुशः."),
            [("सोल्पम्", "ओ comes from अ + उ, not from उ + अ."),
             ("सूल्पम्", "ऊ comes from उ + उ, not from उ + अ."),
             ("स्वाल्पम्", "वा would come from उ + आ, but अल्पम् begins with a short अ.")],
            "सु + अल्पम् = स्वल्पम्, like तु + अणुशः = त्वणुशः.",
            "उ + अ → व.",
            teaches="उ before an unlike vowel becomes व्: तु + अणुशः → त्वणुशः."),
    ],
}

# ---------------------------------------------------------------- unit 214
AUTHORED["214"] = {
    "title": "ताभिरिदं शरीरंगवाक्षितं",
    "question": "By unit 214, what three things are said of the body?",
    "rule": ("By those (ताभिः, probably the sirā and dhamanī of unit 213) this body is latticed (गवाक्षितम्), bound "
             "round (पिनद्धम्) and stretched out (आततम्)."),
    "limits": ("Prose. ताभिः is feminine; that it means the sirā and dhamanī is probable, not stated: no question asks "
               "what it refers to."),
    "explain_hi": ("यह गद्य-पंक्ति कहती है कि ‘उनसे’ (ताभिः, सम्भवतः इकाई २१३ की सिराएँ और धमनियाँ) यह शरीर तीन तरह का है: "
                   "गवाक्षित (जालीदार), पिनद्ध (बँधा हुआ) और आतत (फैला हुआ)। "
                   "‘गवाक्षित’ गवाक्ष (झरोखा, जाली) से बना है: झरोखे की जाली जैसा बना हुआ। "
                   "‘पिनद्ध’ अपि-√नह् का कृदन्त है, जिसमें अपि का अ गिर गया; ‘आतत’ आ-√तन् से: फैला हुआ। "
                   "‘ताभिः’ स्त्रीलिंग तृतीया बहुवचन है, पर किसकी ओर, यह पंक्ति में नहीं।"),
    "hook": "जालीदार, बँधा, फैला: यह शरीर।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 214, the body is गवाक्षित. What does that mean?",
            ("Latticed, like a window-lattice", "गवाक्ष = window, lattice; गवाक्षित = latticed."),
            [("Hollow, like an empty pot", "गवाक्षित comes from गवाक्ष, window-lattice, not a pot."),
             ("Layered, like an onion skin", "गवाक्षित comes from गवाक्ष, window-lattice, not layers."),
             ("Coiled, like a sleeping snake", "गवाक्षित comes from गवाक्ष, window-lattice, not coils.")],
            "गवाक्षितम् = latticed, made like a window-lattice.",
            "गवाक्ष → गवाक्षित."),
        order(1, "Put the three things said of the body in unit 214 in the line's order.",
              ["गवाक्षितं", "पिनद्धम्", "आततं च"],
              "Latticed, bound round and stretched out.",
              "गवाक्षितम् → पिनद्धम् → आततम्."),
        match(2, "Match each word of unit 214 to its meaning.",
              [["गवाक्ष", "window, lattice"], ["पिनद्ध", "bound round"], ["आतत", "stretched out"], ["शरीर", "body"],
               ["इदम्", "this"]],
              "By those this body is latticed, bound round and stretched out.",
              "गवाक्ष, पिनद्ध, आतत, शरीर, इदम्.", role="extend",
              teaches="पिनद्ध = 'bound round', from अपि-√नह् with the अ of अपि lost."),
        mcq("discriminate", 3, "Which split of पिनद्धमाततं in unit 214 is right?",
            ("पिनद्धम् + आततम्", "म् before a vowel simply joins it: पिनद्धम् + आततम् → पिनद्धमाततम्."),
            [("पिनद्ध + माततम्", "माततम् is not a word; the word is आततम् (stretched)."),
             ("पिनद्धमा + ततम्", "पिनद्धमा is not a form; the word is पिनद्धम्."),
             ("पिनद्धः + आततम्", "अः before आ would give पिनद्ध आततम्; and the neuter form is पिनद्धम्.")],
            "पिनद्धम् (bound round) + आततम् (stretched out).",
            "Final म् + vowel → joined, no change."),
        mcq("apply", 4, "In unit 214, which form is ताभिः?",
            ("Instrumental plural: by those", "ताभिः = by those (feminine instrumental plural)."),
            [("Accusative plural: those, as object", "The feminine accusative plural is ताः."),
             ("Genitive plural: of those", "The feminine genitive plural is तासाम्."),
             ("Locative plural: in those", "The feminine locative plural is तासु.")],
            "ताभिः = by those: the body is latticed by those.",
            "-भिः = instrumental plural."),
        mcq("transfer", 5, "By the pattern of गवाक्ष → गवाक्षित, what does पुष्पित (from पुष्प, flower) mean in a new example?",
            ("Full of flowers, blossomed", "-इत on a noun: furnished with it, as गवाक्षित = latticed."),
            [("One who picks the flowers", "-इत does not make a doer; that would be another form."),
             ("Having lost all its flowers", "-इत means furnished with, not deprived of."),
             ("Given away as a flower gift", "-इत on a noun does not mean given as that thing.")],
            "पुष्पित = full of flowers, like गवाक्षित = latticed.",
            "Noun + -इत = furnished with / made into that.",
            teaches="गवाक्षित is a participle made from the noun गवाक्ष: 'furnished with a lattice', latticed."),
    ],
}

# ---------------------------------------------------------------- unit 215
AUTHORED["215"] = {
    "title": "तावंति च केशश्मश्रुलोमानि",
    "question": "By unit 215, which hairs are said to be 'that many', and what is said of their nourishment?",
    "rule": ("And that many (तावन्ति) are the head-hairs (केश), beard-hairs (श्मश्रु) and body-hairs (लोमन्). For their "
             "openings are bound to them; therefore they are nourished (आप्यायन्ते) by those."),
    "limits": ("Low confidence. 'That many' is probably as many as the openings of unit 213 (not stated). What 'those' "
               "(तासाम्, ताभिः; probably the vessels) and 'bound to that' refer to is unclear: no question asks it. "
               "Read: hairs nourished by the vessels."),
    "explain_hi": ("यह कम विश्वास वाली गद्य-पंक्ति है। "
                   "पहला वाक्य: उतने ही केश (सिर के बाल), श्मश्रु (दाढ़ी-मूँछ के बाल) और लोम (शरीर के रोम) हैं; ‘उतने’ सम्भवतः इकाई २१३ के मुखों जितने, पर यह कहा नहीं गया। "
                   "दूसरा: ‘उनके मुख उनसे बँधे हैं, इसलिए वे उनसे पोषण पाते हैं’। "
                   "‘तासाम्’ और ‘ताभिः’ स्त्रीलिंग हैं, सम्भवतः सिरा-धमनी की ओर; ‘तत्प्रतिबद्ध’ किससे बँधा, यह अस्पष्ट है। "
                   "डेटा का पठन: बाल वाहिनियों से पोषित होते हैं। ‘आप्यायन्ते’ = पोषित होते हैं (आत्मनेपद)।"),
    "hook": "केश, श्मश्रु, लोम: उतने ही, और पोषित।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 215, which three kinds of hair are named?",
            ("Head, beard and body hair", "केशश्मश्रुलोमानि: केश (head), श्मश्रु (beard), लोमन् (body)."),
            [("Head, eyebrow and eyelash hair", "Eyebrows and eyelashes are not named; श्मश्रु and लोमन् are."),
             ("Beard, eyebrow and nostril hair", "Eyebrow and nostril hair are not named; केश and लोमन् are."),
             ("Head, eyelash and armpit hair", "Eyelash and armpit hair are not named; श्मश्रु and लोमन् are.")],
            "Head-hair (केश), beard-hair (श्मश्रु) and body-hair (लोमन्).",
            "केश + श्मश्रु + लोमन्."),
        order(1, "Put the parts of unit 215 in the line's order (joined words are shown split).",
              ["तावंति च", "केशश्मश्रुलोमानि", "तासां हिमुखानि", "तत्प्रतिबद्धानि", "अतस्तानि", "ताभिराप्यायंते"],
              "That many hairs; for their openings are bound to that; therefore those are nourished by those.",
              "तावन्ति → केशश्मश्रुलोमानि → तासां हि मुखानि → तत्प्रतिबद्धानि → अतस्तानि → ताभिराप्यायन्ते."),
        match(2, "Match each word of unit 215 to its meaning.",
              [["केश", "head-hair"], ["श्मश्रु", "beard-hair"], ["लोमन्", "body-hair"], ["अतः", "therefore"],
               ["आप्यायन्ते", "are nourished"]],
              "Head-, beard- and body-hair; therefore they are nourished.",
              "केश, श्मश्रु, लोमन्, अतः, आप्यायन्ते.", role="extend",
              teaches="आप्यायन्ते (आ-√प्याय्, ātmanepada) = are nourished, swell with fluid."),
        mcq("discriminate", 3, "Which split of प्रतिबद्धान्यतस्तानि in unit 215 is right?",
            ("प्रतिबद्धानि + अतः + तानि", "इ + अ → य; visarga before त → स्."),
            [("प्रतिबद्धानि + यतः + तानि", "A word beginning with य does not fuse with इ; it would stay प्रतिबद्धानि यतः."),
             ("प्रतिबद्धाने + अतः + तानि", "ए + अ would give प्रतिबद्धानेऽतः, not -न्यतः."),
             ("प्रतिबद्धानि + अतः + स्तानि", "स्तानि is not a word; the स् is the visarga of अतः.")],
            "प्रतिबद्धानि (bound) + अतः (therefore) + तानि (those).",
            "इ + अ → य; visarga + त → स्त."),
        multi("apply", 4, "Which statements fit unit 215 as the card reads it?",
              [("It names head-, beard- and body-hair", "Right: केशश्मश्रुलोमानि."),
               ("It states plainly what 'that many' refers to", "It does not; the reference is only probable."),
               ("It names the sirā and dhamanī as 'those'", "They are not named in the unit; that reading is probable."),
               ("Its verb आप्यायन्ते means 'are nourished'", "Right: आ-√प्याय्, are nourished.")],
              [0, 3],
              "Three kinds of hair are named and said to be nourished; the references stay open.",
              "केशश्मश्रुलोमानि ... आप्यायन्ते."),
        mcq("transfer", 5, "By the pattern of केशश्मश्रुलोमानि, what does फलपुष्पपत्राणि mean in a new example?",
            ("Fruits, flowers and leaves", "A dvandva lists its members; plural, neuter after the last (पत्र)."),
            [("Flowers growing out of fruits", "A dvandva does not make one member grow from another."),
             ("Leaves that hold fruit-flowers", "A dvandva is a list, not 'X that holds Y'."),
             ("Fruit and flowers, without leaves", "पत्र is the last member of the list, not left out.")],
            "फलपुष्पपत्राणि = fruits, flowers and leaves, like केशश्मश्रुलोमानि = head-, beard- and body-hairs.",
            "Dvandva = a list joined into one word.",
            teaches=("केशश्मश्रुलोमानि is a dvandva: a list joined into one word, plural, taking the gender of its "
                     "last member (लोमन्, neuter).")),
    ],
}

# ---------------------------------------------------------------- unit 216
AUTHORED["216"] = {
    "title": "तैश्च ताः स्वेदमभिवहंति",
    "question": "By unit 216, what do 'those' carry?",
    "rule": ("And by those (तैः, masculine/neuter) those (ताः, feminine) carry (अभिवहन्ति) the sweat (स्वेदम्). Neither "
             "group is named in the unit."),
    "limits": ("Low confidence. तैः probably means the hairs or their pores (unit 215) and ताः probably the vessels; "
               "neither is named: no question asks what they refer to. The direction of 'carry' is not stated."),
    "explain_hi": ("यह छोटा, कम विश्वास वाला गद्य-वाक्य है: ‘और उनसे वे पसीने को ले जाती हैं’। "
                   "‘तैः’ पुल्लिंग/नपुंसक तृतीया बहुवचन है (सम्भवतः इकाई २१५ के बाल या उनके छिद्र), और ‘ताः’ स्त्रीलिंग प्रथमा बहुवचन (सम्भवतः वाहिनियाँ); "
                   "दोनों का नाम पंक्ति में नहीं। "
                   "‘अभिवहन्ति’ = ले जाती हैं, पहुँचाती हैं; किस ओर, यह नहीं कहा गया। "
                   "‘तैश्च’: च से पहले विसर्ग श् बना।"),
    "hook": "और उनसे वे स्वेद ढोती हैं।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 216, what do 'those' (ताः) carry?",
            ("Sweat", "स्वेदमभिवहन्ति: carry the sweat (स्वेद)."),
            [("Urine", "The line names स्वेद, sweat, not urine."),
             ("Tears", "The line names स्वेद, sweat, not tears."),
             ("Ear wax", "The line names स्वेद, sweat, not ear wax.")],
            "Those carry the sweat.",
            "स्वेद = sweat."),
        order(1, "Put the words of unit 216 in the line's order (joined words are shown split).",
              ["तैश्च", "ताः", "स्वेदम्", "अभिवहंति"],
              "And by those, those carry the sweat.",
              "तैश्च → ताः → स्वेदम् → अभिवहन्ति."),
        fill(2, "In unit 216 the word for 'sweat' is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("स्वेद", "sveda", "स्वेदम्"),
             "स्वेदम् (sweat, accusative) + अभिवहन्ति (carry).",
             "स्वेद = sweat.",
             "स्वेदम् + अभिवहन्ति → स्वेदमभिवहन्ति."),
        mcq("discriminate", 3, "Why is तैः printed तैश् before च in unit 216?",
            ("Visarga before च becomes श्", "तैः + च → तैश्च."),
            [("Visarga before च becomes स्", "स् comes from a visarga before त or थ, not before च."),
             ("Visarga before च becomes र्", "र् comes before a voiced sound; च is unvoiced."),
             ("Visarga before च becomes ओ", "ओ comes from अः before a voiced consonant; here it is ऐः before च.")],
            "तैः (by those) + च (and): visarga before च → श्.",
            "Visarga before च/छ → श्."),
        match(4, "Match each word of unit 216 to its meaning.",
              [["तैः", "by those"], ["ताः", "those (feminine)"], ["स्वेद", "sweat"], ["अभिवहन्ति", "carry"]],
              "And by those, those carry the sweat.",
              "तैः, ताः, स्वेद, अभिवहन्ति.", role="apply"),
        mcq("transfer", 5, "By the rule of तैः + च, how is पुष्पैः + च (and with flowers) joined in a new example?",
            ("पुष्पैश्च", "Visarga before च becomes श्, as तैः + च → तैश्च."),
            [("पुष्पै च", "The visarga is not dropped before च; it becomes श्."),
             ("पुष्पैस्च", "स् comes from a visarga before त or थ, not before च."),
             ("पुष्पैर्च", "र् comes from the visarga after ऐ only before a voiced sound; च is unvoiced.")],
            "पुष्पैः + च = पुष्पैश्च, like तैः + च = तैश्च.",
            "Visarga + च → श्च.",
            teaches="A visarga before च or छ becomes श्: तैः + च → तैश्च."),
    ],
}


# ===================================================================== NOTES_HI
NOTES_HI = {
    "204": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। अपूर्ण वाक्य: क्रिया और गिनी गई संज्ञा नहीं छपी, जोड़ी नहीं गई; संज्ञा सम्भवतः "
            "‘पेशी’ (पिछली गिनती से)। सन्धि जाँची: विंशतिः + अधिका → विंशतिरधिका (इ के बाद विसर्ग, स्वर से पहले → र्); "
            "छपा स्त्रीणां = स्त्रीणाम् (व्यंजन से पहले म् → ं)।"),
    "205": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। छपा ‘दशस्तनयोः’ = दश स्तनयोः (दो शब्द)। ‘तासाम्’ (उनकी) किसकी ओर, यह नहीं कहा "
            "गया: स्तनों वाली दस या सामान्य रूप से पेशियाँ; दूसरा वाक्य अलग कथन माना गया। गिनी गई संज्ञा नहीं छपी। ‘स्तनयोः’ का अर्थ "
            "डेटा के अनुसार ‘दोनों स्तनों में’। सन्धि जाँची: परिवृद्धिः + भवति → परिवृद्धिर्भवति (घोष भ से पहले इ के बाद विसर्ग → र्)।"),
    "206": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। अपूर्ण: क्रिया और गिनी गई संज्ञा नहीं। योनि = स्त्री का जननमार्ग, सम्भवतः "
            "योनि-नलिका सहित (सम्भावित); संस्कृत शब्द दोनों अनुवादों में रखा गया। ‘योनौ’ इकारान्त स्त्रीलिंग का सप्तमी एकवचन "
            "(‘योन्याम्’ भी सम्भव रूप होता)।"),
    "207": ("गद्य; विश्वास निम्न। छपा ‘तासाम्अभ्यंतराश्रिते’ एक टुकड़ा है (तासाम् + अभ्यन्तराश्रिते; सामान्य लेखन तासामभ्यन्तराश्रिते)। "
            "छपे पाठ में केवल दो ‘द्वे’ हैं: ‘अभ्यंतराश्रिते द्वे’ और ‘मुखाश्रिते वृत्ते द्वे’; गिनती २ + २ यहाँ और ३ इकाई २०८ में, यानी "
            "इकाई २०६ के दस के सामने सात; इकाई २०९ शायद एक और देती है। गिनती छपे रूप में रखी गई, सुधारी नहीं; स्कैन से ‘द्वे’ छूटा हो तो "
            "निर्णय स्वामी का। गिनती पर कोई प्रश्न नहीं। सन्धि जाँची: अभ्यन्तर + आश्रिते → अभ्यन्तराश्रिते, मुख + आश्रिते → मुखाश्रिते (अ + आ → आ); "
            "छपा अभ्यंतर = अभ्यन्तर।"),
    "208": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। गर्भमार्ग = गर्भ का मार्ग, सम्भवतः प्रसव-मार्ग (सम्भावित)। गिनी गई संज्ञा नहीं छपी; "
            "स्त्रीलिंग ‘तिस्रः’ पेशी से मेल खाता है। सन्धि जाँची: तिस्रः + गर्भ... → तिस्रो गर्भ... (अः, घोष व्यंजन से पहले → ओ); "
            "गर्भ + मार्ग + आश्रयाः → गर्भमार्गाश्रयाः (अ + आ → आ)।"),
    "209": ("गद्य; विश्वास निम्न; कोई पाठ-चिह्न नहीं। समूह-टिप्पणी: बिना पूर्ववर्ती संज्ञा (जिसकी ओर ‘यस्याम्’ है) और मुख्य वाक्य का सम्बन्धवाचक वाक्य; सम्भवतः इकाई २०८ "
            "को आगे बढ़ाता है, या गिनती का एक और सदस्य बताता है (कोई संख्या, जैसे ‘एक’, छूटी हो सकती है; कुछ जोड़ा नहीं गया)। "
            "छपा ‘यस्यांगर्भ स्तिष्ठति’ = यस्यां गर्भस्तिष्ठति: शब्द-विभाजन गलत जगह छपा। सन्धि जाँची: गर्भः + तिष्ठति → गर्भस्तिष्ठति "
            "(त से पहले विसर्ग → स्); यस्याम् + गर्भः → यस्यां गर्भः (व्यंजन से पहले म् → ं)।"),
    "210": ("गद्य; विश्वास निम्न। पाठ-चिह्न (सम्भावित, अनुमानित): छपा ‘उद्यावर्त्ता’ कोई शब्द नहीं; आगे ‘तस्यास्तृतीय आवर्ते’ (उसके तीसरे "
            "आवर्त में) से ‘त्र्यावर्ता’ (तीन आवर्तों वाली) सुझाया गया; उ-द और त-र की स्कैन-भूल सम्भव। यह पाठ अनुवादों में अपनाया गया, "
            "पर इस पर कोई प्रश्न नहीं। ‘पित्त’ शायद पित्ताशय (पित्त का स्थान) के लिए; छपा रूप रखा। रोहित = रोहू मछली (Labeo rohita, मानक); "
            "पक्वाशय = पचे अन्न का स्थान, बड़ी आँत का क्षेत्र (सम्भावित); गर्भशय्या = गर्भाशय (सम्भावित)। सन्धि जाँची: योनिः + तु → योनिस्तु "
            "(त से पहले विसर्ग → स्); तस्याः + तृतीये → तस्यास्तृतीये; तृतीये + आवर्ते → तृतीय आवर्ते (ए + स्वर → अय्, य् का लोप, बीच में अन्तर); "
            "छपा आवर्त्ते (दोहरा त्त) = आवर्ते।"),
    "211": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। पेशी = मांसपेशी (मानक; ‘मांस की लड़ी’ भी)। शुक्र = वीर्य (मानक); आर्तव = मासिक धर्म "
            "का रक्त (सम्भावित, ‘स्त्री का जनन-द्रव’)। ‘प्रवेशिनी’ का शब्दार्थ ‘प्रवेश करने वाली’; ‘ग्रहण करने वाली’ भी सम्भव। ‘तस्याम्’ "
            "किसकी ओर, डेटा नहीं बताता। सन्धि जाँची: प्रवेशिन्यः + तिस्रः → प्रवेशिन्यस्तिस्रः (त से पहले विसर्ग → स्); शुक्र + आर्तव → "
            "शुक्रार्तव (अ + आ → आ); छपा आर्त्तव (दोहरा त्त) = आर्तव।"),
    "212": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। ‘ताभिः’ स्त्रीलिंग, सम्भवतः इकाई २११ की पेशियों की ओर; कुछ जोड़ा नहीं गया। "
            "सिरा = वाहिनी (सम्भावित), स्नाव/स्नायु = कण्डरा, स्नायु-बन्धन (सम्भावित)। बहल (घना) और स्थूल (बड़ा) दो अलग सदस्य। "
            "सन्धि जाँची: ताभिः + हि → ताभिर्हि (घोष ह से पहले इ के बाद विसर्ग → र्); स्थूल + अणु → स्थूलाणु (अ + अ → आ); "
            "सन्धि + अस्थि → सन्ध्यस्थि (इ + अ → य); छपा संध्य = सन्ध्य।"),
    "213": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। संख्या छपे रूप में: एकोनत्रिंशत् शतसहस्र = २९ × १,००,०००; ‘नव शतानि "
            "षट्पञ्चाशानि’ = नौ सौ छप्पन; कुल २९,००,९५६। एक अन्य प्रति २९,९५६ पढ़ सकती है; वह लागू नहीं किया गया। सिरा और धमनी: "
            "वाहिनियाँ, आधुनिक भेद पक्का नहीं। गिने गए हैं मुख। सन्धि जाँची: तु + अणुशः → त्वणुशः (उ + अ → व); अणुशः + वि... → अणुशो वि... "
            "(अः, घोष व्यंजन से पहले → ओ); एकोनत्रिंशत् + शत → एकोनत्रिंशच्छत, नियम: त् + श → च्श, विकल्प से च्छ (श के बाद स्वर या य/व/र हो तो; छपा च्छ); "
            "विभज्यमानानाम् + एकोन... → विभज्यमानानामेकोन...; एक + ऊन → एकोन (अ + ऊ → ओ)।"),
    "214": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। ‘ताभिः’ स्त्रीलिंग, सम्भवतः इकाई २१३ की सिरा-धमनी की ओर (कहा नहीं गया)। "
            "गवाक्षित = गवाक्ष (झरोखा, जाली) से नाम-धातु कृदन्त। पिनद्ध = अपि-√नह्, अपि का अ लुप्त। छपा ‘शरीरंगवाक्षितं’ दो शब्द जोड़ता है "
            "(शरीरं गवाक्षितम्)। सन्धि जाँची: ताभिः + इदम् → ताभिरिदम् (इ के बाद विसर्ग, स्वर से पहले → र्); पिनद्धम् + आततम् → पिनद्धमाततम्।"),
    "215": ("गद्य; विश्वास निम्न; कोई पाठ-चिह्न नहीं। ‘तावन्ति’ सम्भवतः इकाई २१३ के मुखों जितने (कहा नहीं गया)। ‘तासाम्’ और ‘ताभिः’ "
            "स्त्रीलिंग, सम्भवतः सिरा-धमनी; ‘तत्प्रतिबद्ध’ का पूर्वपद अस्पष्ट (मुख बालों से बँधे, या वाहिनियों से)। पठन: बाल वाहिनियों से पोषित। "
            "छपा ‘हिमुखानि’ = हि मुखानि। सन्धि जाँची: तत्प्रतिबद्धानि + अतः → तत्प्रतिबद्धान्यतः (इ + अ → य); अतः + तानि → अतस्तानि "
            "(त से पहले विसर्ग → स्); ताभिः + आप्यायन्ते → ताभिराप्यायन्ते (इ के बाद विसर्ग, स्वर से पहले → र्)।"),
    "216": ("गद्य; विश्वास निम्न; कोई पाठ-चिह्न नहीं। ‘तैः’ पुल्लिंग/नपुंसक (सम्भवतः इकाई २१५ के बाल या उनके छिद्र), ‘ताः’ स्त्रीलिंग "
            "(सम्भवतः वाहिनियाँ); दोनों का नाम नहीं। ‘अभिवहन्ति’ की दिशा नहीं कही गई। सन्धि जाँची: तैः + च → तैश्च (च से पहले विसर्ग → श्); "
            "स्वेदम् + अभिवहन्ति → स्वेदमभिवहन्ति; छपा वहंति = वहन्ति।"),
}


# ===================================================================== AIDS
AIDS = {
    "204": {
        "chunks": "स्त्रीणां | तु | विंशतिरधिका",
        "sandhi": "इ के बाद का विसर्ग, स्वर से पहले → र्: विंशतिः + अधिका → विंशतिरधिका।",
        "frame": "किनमें: स्त्रीणाम् (स्त्रियों में) → कितनी: विंशतिः (बीस) → क्या: अधिका (अधिक) → वस्तु: छपी नहीं (सम्भवतः पेशियाँ)।",
    },
    "205": {
        "chunks": "तत्र | दशस्तनयोः | तासां यौवने | परिवृद्धिर्भवति",
        "sandhi": "इ के बाद का विसर्ग, घोष व्यंजन से पहले → र्: परिवृद्धिः + भवति → परिवृद्धिर्भवति।",
        "frame": "पहला वाक्य: तत्र (उनमें) → दश (दस) → स्तनयोः (दोनों स्तनों में)। दूसरा: तासाम् (उनकी) → यौवने (यौवन में) → परिवृद्धिः भवति (वृद्धि होती है)।",
    },
    "206": {
        "chunks": "दश | योनौ",
        "frame": "संख्या: दश (दस) → स्थान: योनौ (योनि में; सम्भवतः स्त्री का जननमार्ग) → वस्तु और क्रिया: छपी नहीं।",
        "anchors": "दस स्तनों में (इकाई २०५), दस योनि में (इकाई २०६): दस और दस। (मेरी याद-पद्धति)",
    },
    "207": {
        "diagram": {"groups": [
            {"label": "छपा पाठ, क्रम से", "items": ["अभ्यंतराश्रिते द्वे: भीतर टिकी दो", "मुखाश्रिते वृत्ते द्वे: मुख पर टिकी, गोल, दो"]},
            {"label": "खुला प्रश्न", "items": ["कुल गिनती दस से कम छपी; कोई ‘द्वे’ छूटा हो सकता है"]}]},
        "chunks": "तासाम्अभ्यंतराश्रिते | द्वे | मुखाश्रिते | वृत्ते | द्वे",
        "sandhi": "अ + आ → आ: अभ्यन्तर + आश्रिते → अभ्यन्तराश्रिते · मुख + आश्रिते → मुखाश्रिते।",
    },
    "208": {
        "chunks": "तिस्रो | गर्भमार्गाश्रयाः",
        "sandhi": "अः, घोष व्यंजन से पहले → ओ: तिस्रः + गर्भ... → तिस्रो गर्भ... · अ + आ → आ: मार्ग + आश्रयाः → मार्गाश्रयाः।",
        "frame": "संख्या: तिस्रः (तीन, स्त्रीलिंग) → कहाँ: गर्भमार्ग (गर्भ का मार्ग, सम्भवतः प्रसव-मार्ग) → कैसे: आश्रयाः (टिकी हुई)।",
    },
    "209": {
        "chunks": "यस्यांगर्भ | स्तिष्ठति (पढ़ा: यस्यां गर्भस्तिष्ठति)",
        "sandhi": "त से पहले विसर्ग → स्: गर्भः + तिष्ठति → गर्भस्तिष्ठति · व्यंजन से पहले म् → ं: यस्याम् + गर्भः → यस्यां गर्भः।",
        "frame": "कहाँ: यस्याम् (जिसमें; किसकी ओर, अनकहा) → कौन: गर्भः → क्या करता: तिष्ठति (ठहरता है)।",
    },
    "210": {
        "chain": {"steps": ["योनि: शंख की नाभि जैसा आकार", "उसका तीसरा आवर्त", "पित्त और पक्वाशय के बीच",
                            "गर्भशय्या (सम्भवतः गर्भाशय)", "आकार: रोहित मछली के मुख जैसा"]},
        "chunks": "योनिस्तु | शंखनाभ्याकृतिरुद्यावर्त्ता | तस्यास्तृतीय | आवर्त्तेपित्तपक्वाशयांतरे | रोहितमत्स्यमुखाकारा | गर्भशय्या",
        "sandhi": "ए + स्वर → अय्, य् का लोप: तृतीये + आवर्ते → तृतीय आवर्ते · त से पहले विसर्ग → स्: योनिः + तु → योनिस्तु।",
        "contrast": "दो उपमाएँ, इसी पंक्ति में: योनि का आकार शंख की नाभि जैसा; गर्भशय्या का आकार रोहित मछली के मुख जैसा।",
    },
    "211": {
        "chunks": "तस्यां | शुक्रार्त्तवप्रवेशिन्यस्तिस्रः | पेश्यः",
        "sandhi": "त से पहले विसर्ग → स्: प्रवेशिन्यः + तिस्रः → प्रवेशिन्यस्तिस्रः · अ + आ → आ: शुक्र + आर्तव → शुक्रार्तव।",
        "frame": "कहाँ: तस्याम् (उसमें; किसकी ओर, अनकहा) → कितनी: तिस्रः (तीन) → क्या: पेश्यः (पेशियाँ) → कैसी: शुक्र और आर्तव में प्रवेश करने वाली।",
    },
    "212": {
        "diagram": {"groups": [
            {"label": "बारह गुण, क्रम से", "items": ["तनु", "बहल", "स्थूल", "अणु", "पृथु", "वृत्त", "ह्रस्व", "दीर्घ",
                                                 "स्थिर", "मृदु", "श्लक्ष्ण", "कर्कश"]},
            {"label": "ढके हुए", "items": ["सन्धि", "अस्थि", "सिरा", "स्नाव (स्नायु)"]}]},
        "seesaw": "इसी सूची के पड़ोसी शब्दों में विपरीत जोड़े: तनु ↔ बहल (पतली ↔ घनी), स्थूल ↔ अणु (बड़ी ↔ सूक्ष्म), ह्रस्व ↔ दीर्घ (छोटी ↔ लम्बी), श्लक्ष्ण ↔ कर्कश (चिकनी ↔ खुरदुरी)।",
        "chunks": "ताभिर्हि शरीरे | तनुबहलस्थूलाणुपृथुवृत्तह्रस्वदीर्घस्थिरमृदुश्लक्ष्णकर्कशाभिः | संध्यस्थिसिरास्नावानि | प्रच्छादितानि",
        "sandhi": "इ + अ → य: सन्धि + अस्थि → सन्ध्यस्थि · अ + अ → आ: स्थूल + अणु → स्थूलाणु।",
    },
    "213": {
        "diagram": {"groups": [
            {"label": "छपी संख्या के दो भाग", "items": ["एकोनत्रिंशत् शतसहस्र = उनतीस लाख", "नव शतानि षट्पञ्चाशानि = नौ सौ छप्पन",
                                                      "कुल (छपे रूप में) २९,००,९५६"]}]},
        "chunks": "सिराधमनीमुखानां | त्वणुशो | विभज्यमानानामेकोनत्रिंशच्छतसहस्राणि | नव च शतानि षट्पंचाशानि | भवंति",
        "sandhi": "उ + अ → व: तु + अणुशः → त्वणुशः · त् + श → च्श, विकल्प से च्छ (श के बाद स्वर या य/व/र हो तो; छपा च्छ): एकोनत्रिंशत् + शत → एकोनत्रिंशच्छत।",
        "letters": "एक-ऊन-त्रिंशत्: ‘एक कम तीस’ = उनतीस; हिन्दी ‘उन-तीस’ में भी ‘ऊन’ (कम) छिपा है। (मेरी याद-पद्धति)",
    },
    "214": {
        "chain": {"steps": ["ताभिः: उनसे", "इदं शरीरम्: यह शरीर", "१ गवाक्षितम्: जालीदार", "२ पिनद्धम्: बँधा हुआ", "३ आततम्: फैला हुआ"]},
        "chunks": "ताभिरिदं | शरीरंगवाक्षितं | पिनद्धमाततं च",
        "sandhi": "इ के बाद का विसर्ग, स्वर से पहले → र्: ताभिः + इदम् → ताभिरिदम् · पिनद्धम् + आततम् → पिनद्धमाततम्।",
        "pegs": "झरोखे की जाली सोचिए: जाली (गवाक्षित), उसे बाँधी रस्सी (पिनद्ध), और खिंचा परदा (आतत)। (मेरा बनाया चित्र, केवल याद की सहायता)",
    },
    "215": {
        "diagram": {"groups": [
            {"label": "छपे में स्पष्ट", "items": ["केश: सिर के बाल", "श्मश्रु: दाढ़ी-मूँछ के बाल", "लोम: शरीर के रोम",
                                             "अतः आप्यायन्ते: इसलिए पोषित होते हैं"]},
            {"label": "अनकहा या अस्पष्ट", "items": ["‘उतने’: सम्भवतः इकाई २१३ के मुखों जितने", "‘उन’: सम्भवतः सिरा-धमनी",
                                                 "‘तत्प्रतिबद्ध’: किससे बँधे"]}]},
        "chunks": "तावंति च | केशश्मश्रुलोमानि | तासां हिमुखानि | तत्प्रतिबद्धान्यतस्तानि | ताभिराप्यायंते",
        "sandhi": "इ + अ → य: प्रतिबद्धानि + अतः → प्रतिबद्धान्यतः · त से पहले विसर्ग → स्: अतः + तानि → अतस्तानि।",
    },
    "216": {
        "chunks": "तैश्च | ताः | स्वेदमभिवहंति",
        "sandhi": "च से पहले विसर्ग → श्: तैः + च → तैश्च · स्वेदम् + अभिवहन्ति → स्वेदमभिवहन्ति।",
        "frame": "किनसे: तैः (पुल्लिंग/नपुंसक; अनकहा) → कौन: ताः (स्त्रीलिंग; अनकहा) → क्या: स्वेदम् (पसीना) → क्या करती: अभिवहन्ति (ले जाती हैं)।",
    },
}


# ===================================================================== IMAGE_SPECS
IMAGE_SPECS = {
    ("207", "diagram"): {
        "file": "sh5-abhyantara-mukha-207.svg",
        "alt": ("Table of unit 207 as printed: 'abhyantarāśrite dve', two resting inside; 'mukhāśrite vṛtte dve', resting "
                "at the mouth, round, two. The total is left open (a dve may be missing)."),
        "type": "table",
        "title": "इकाई २०७: छपा पाठ",
        "heads": ["छपा अंश", "अर्थ"],
        "rows": [["अभ्यंतराश्रिते द्वे", "भीतर टिकी दो"], ["मुखाश्रिते वृत्ते द्वे", "मुख पर टिकी, गोल, दो"],
                 ["कुल", "खुला (कोई द्वे छूटा हो सकता है)"]],
    },
    ("210", "chain"): {
        "file": "sh5-garbhashayya-210.svg",
        "alt": ("Flowchart of unit 210: the yoni, shaped like a conch's navel; its third whorl; between pitta and the "
                "pakvāśaya; the garbhaśayyā (probably the uterus), shaped like a rohita fish's mouth."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"योनि\"] --> B[\"आकार: शंख की नाभि जैसा\"]\n"
                 "  A --> C[\"उसका तीसरा आवर्त\"]\n"
                 "  C --> D[\"पित्त और पक्वाशय के बीच\"]\n"
                 "  D --> E[\"गर्भशय्या\"]\n"
                 "  E --> F[\"आकार: रोहित मछली का मुख\"]\n"),
    },
    ("212", "diagram"): {
        "file": "sh5-peshi-guna-212.svg",
        "alt": ("Table of unit 212: the twelve qualities in line order (thin, dense, large, minute, broad, round, short, "
                "long, firm, soft, smooth, rough) of those that cover the joints, bones, sirā and snāva."),
        "type": "table",
        "title": "इकाई २१२: बारह गुण (क्रम से)",
        "heads": ["छपा शब्द", "अर्थ"],
        "rows": [["१ तनु", "पतली"], ["२ बहल", "घनी"], ["३ स्थूल", "बड़ी"], ["४ अणु", "सूक्ष्म"], ["५ पृथु", "चौड़ी"],
                 ["६ वृत्त", "गोल"], ["७ ह्रस्व", "छोटी"], ["८ दीर्घ", "लम्बी"], ["९ स्थिर", "दृढ़"], ["१० मृदु", "कोमल"],
                 ["११ श्लक्ष्ण", "चिकनी"], ["१२ कर्कश", "खुरदुरी"],
                 ["संध्यस्थिसिरास्नावानि (ढके हुए)", "सन्धि, अस्थि, सिरा, स्नाव"]],
    },
    ("213", "diagram"): {
        "file": "sh5-sira-mukha-213.svg",
        "alt": ("Table of unit 213: the openings of the sirā and dhamanī, divided minutely: twenty-nine hundred-thousands "
                "(2,900,000) and nine hundred and fifty-six; 2,900,956 as printed."),
        "type": "table",
        "title": "इकाई २१३: सिरा-धमनी के मुख",
        "heads": ["छपा अंश", "संख्या"],
        "rows": [["एकोनत्रिंशच्छतसहस्राणि", "२९,००,००० (उनतीस लाख)"], ["नव च शतानि षट्पंचाशानि", "९५६ (नौ सौ छप्पन)"],
                 ["कुल, छपे रूप में", "२९,००,९५६"]],
    },
    ("214", "chain"): {
        "file": "sh5-gavakshita-214.svg",
        "alt": ("Flowchart of unit 214: by those, this body is 1 latticed (gavākṣita), 2 bound round (pinaddha), "
                "3 stretched out (ātata)."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"ताभिः: उनसे\"] --> B[\"इदं शरीरम्: यह शरीर\"]\n"
                 "  B --> C[\"१ गवाक्षितम्:<br/>जालीदार\"]\n"
                 "  B --> D[\"२ पिनद्धम्:<br/>बँधा हुआ\"]\n"
                 "  B --> E[\"३ आततम्:<br/>फैला हुआ\"]\n"),
    },
    ("215", "diagram"): {
        "file": "sh5-kesha-loma-215.svg",
        "alt": ("Two columns of unit 215. Printed plainly: head-hair (keśa), beard-hair (śmaśru), body-hair (loman); "
                "therefore they are nourished. Unstated or unclear: 'that many' (probably as many as the openings of unit "
                "213), 'those' (probably sirā and dhamanī), and to what they are bound."),
        "type": "split",
        "title": "इकाई २१५: स्पष्ट और अस्पष्ट",
        "cols": [["छपे में स्पष्ट", ["केश: सिर के बाल", "श्मश्रु: दाढ़ी-मूँछ", "लोम: शरीर के रोम", "पोषित होते हैं"]],
                 ["अनकहा या अस्पष्ट", ["उतने: किसके जितने", "उन: सम्भवतः सिरा-धमनी", "किससे बँधे"]]],
    },
}
