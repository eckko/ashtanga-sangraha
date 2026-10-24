from helpers import mcq, match, order, fill, multi, accepts


AUTHORED = {}

# ---------------------------------------------------------------- unit 27
AUTHORED["27"] = {
    "title": "तासामधो द्वे रसवेदिन्यौ",
    "question": "By unit 27, what do the four sirās counted below the tongue's sixteen do?",
    "rule": ("Below them (तासाम् अधः: the sixteen of the tongue, unit 26), two perceive taste (रसवेदिन्यौ) and two set "
             "speech in motion (वाक्प्रवर्तिन्यौ); those are four (ताश्चतस्रः)."),
    "limits": ("Prose; copula understood; continues unit 26 (the tongue). 'Below them' may also be read 'of them, "
               "underneath'. Why these four are counted apart is not stated; their link to the fifty of unit 9 is only "
               "the data's sum check, so no question rests on it."),
    "explain_hi": ("यह गद्य-पंक्ति इकाई २६ (जीभ में सोलह सिराएँ) को आगे बढ़ाती है। "
                   "उनके नीचे (तासाम् अधः) दो सिराएँ रस यानी स्वाद का बोध कराती हैं और दो वाणी को प्रवृत्त करती हैं; ये चार हैं। "
                   "‘तासामधो’ को ‘उनमें से, नीचे की ओर’ भी पढ़ा जा सकता है। "
                   "ये चार अलग क्यों गिनी गईं, यह पंक्ति नहीं कहती; इकाई ९ के ‘पचास’ से इनका सम्बन्ध केवल डेटा का जोड़ है, छपा नहीं। "
                   "‘हैं’ क्रिया समझी जाती है।"),
    "hook": "जीभ के नीचे चार: दो स्वाद पहचानें, दो वाणी चलाएँ।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 27, two sirās below the tongue's sixteen perceive taste; what do the other two do?",
            ("They set speech in motion", "द्वे वाक्प्रवर्तिन्यौ: two setting speech (वाक्) in motion."),
            [("They perceive smell", "Perceiving smell belongs to two of the nose's sirās (unit 29), not the tongue's."),
             ("They keep the mouth moist", "No such task is printed in unit 27."),
             ("They move food to the throat", "No such task is printed in unit 27.")],
            "Below them: two perceive taste, two set speech in motion.",
            "द्वे रसवेदिन्यौ, द्वे वाक्प्रवर्तिन्यौ."),
        order(1, "Put the printed phrases of unit 27 in the line's order.",
              ["तासामधो", "द्वे रसवेदिन्यौ", "द्वेवाक्प्रवर्तिन्यौ", "ताश्चतस्रः"],
              "Below them; two taste-perceiving; two speech-moving; those are four.",
              "तासामधो → द्वे रसवेदिन्यौ → द्वेवाक्प्रवर्तिन्यौ → ताश्चतस्रः."),
        match(2, "Match each word part of unit 27 to its meaning.",
              [["अधः", "below"], ["रस", "taste"], ["वेदिनी", "perceiving"], ["वाक्", "speech"],
               ["प्रवर्तिनी", "setting in motion"]],
              "रस-वेदिनी = taste-perceiving; वाक्-प्रवर्तिनी = speech-moving; अधः = below.",
              "अधः, रस, वेदिनी, वाक्, प्रवर्तिनी.", role="extend",
              teaches="Each pair is named by a tat-puruṣa in the feminine dual (-इन्यौ): what it perceives or sets going."),
        mcq("discriminate", 3, "Why is अधः printed अधो before द्वे in unit 27?",
            ("अः before a voiced consonant becomes ओ", "द is a voiced consonant: अधः + द्वे → अधो द्वे."),
            [("अः before every consonant becomes ओ", "Not every consonant: before त the visarga becomes स्, before च श्."),
             ("ओ is a case ending of the word अधः", "अधः is an indeclinable (gram: ind.); it takes no case ending."),
             ("द्वे begins with a vowel, so अः → ओ", "द्वे begins with the consonant द, not a vowel.")],
            "अधः + द्वे: अः before the voiced consonant द → ओ.",
            "अः + voiced consonant → ओ."),
        multi("apply", 4, "Which statements fit unit 27?",
              [("Two sirās perceive taste (rasa)", "Right: द्वे रसवेदिन्यौ."),
               ("Two sirās set speech in motion", "Right: द्वे वाक्प्रवर्तिन्यौ."),
               ("The line says why the four are counted apart", "No reason is printed; the card leaves it open."),
               ("Those named are four in all", "Right: ताश्चतस्रः, those are four.")],
              [0, 1, 3],
              "Two perceive taste, two set speech going: four; no reason is given for counting them apart.",
              "द्वे रसवेदिन्यौ द्वे वाक्प्रवर्तिन्यौ ताश्चतस्रः."),
        mcq("transfer", 5, "By the rule of ताश्चतस्रः, how is बालाः + च (and the boys) joined in a new example?",
            ("बालाश्च", "Visarga before च becomes श्, as ताः + चतस्रः → ताश्चतस्रः."),
            [("बालास्च", "स् comes before त or थ, not before च."),
             ("बाला च", "After आ the visarga drops before a voiced sound; च is not voiced."),
             ("बालो च", "ओ comes from अः before a voiced consonant, not from आः.")],
            "बालाः + च = बालाश्च, like ताः + चतस्रः = ताश्चतस्रः.",
            "Visarga + च → श्च.",
            teaches="A visarga before च becomes श्: ताः + चतस्रः → ताश्चतस्रः."),
    ],
}

# ---------------------------------------------------------------- unit 28
AUTHORED["28"] = {
    "title": "चतुर्विंशतिर्नासायां",
    "question": "By unit 28, how many sirās are in the nose (nāsā)?",
    "rule": ("Twenty-four (चतुर्विंशतिः) are in the nose (नासायाम्). The visarga after इ becomes र् before the voiced "
             "न: चतुर्विंशतिर्नासायाम्."),
    "limits": ("Prose, one printed word; the copula is understood and the counted noun (sirās, the chapter's topic) is "
               "not printed. Only the number is given; the tasks of some of them follow in unit 29."),
    "explain_hi": ("यह छोटी गद्य-पंक्ति कहती है: नासा यानी नाक में चौबीस। "
                   "गिनी गई वस्तु, सिराएँ, अध्याय के विषय से समझी जाती हैं; ‘हैं’ क्रिया भी छपी नहीं। "
                   "चतुर्विंशति = चतुर् (चार) + विंशति (बीस)। "
                   "‘चतुर्विंशतिर्नासायां’ में इ के बाद का विसर्ग घोष व्यंजन न से पहले र् बना है। "
                   "अगली इकाई २९ इन चौबीस में से तीन का काम और स्थान बताती है।"),
    "hook": "नाक में चौबीस: चार और बीस।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 28, how many sirās are in the nose?",
            ("Twenty-four", "चतुर्विंशतिः = twenty-four, नासायाम् = in the nose."),
            [("Twenty-eight", "चतुर्विंशति is four and twenty, not eight and twenty."),
             ("Sixteen", "Sixteen is the count of the tongue (unit 26), not the nose."),
             ("Fifty-six", "Fifty-six is the count of the two eyes (unit 30).")],
            "Twenty-four in the nose.",
            "चतुर्विंशतिर्नासायाम्."),
        match(1, "Match each part of unit 28 to its meaning.",
              [["चतुर्", "four"], ["विंशति", "twenty"], ["चतुर्विंशति", "twenty-four"], ["नासा", "nose"]],
              "चतुर्-विंशति = 4 + 20 = 24; नासा = nose.",
              "चतुर्, विंशति, चतुर्विंशति, नासा."),
        fill(2, "Unit 28: चतुर्विंशतिः ____ (in the nose). Type it in Devanagari or in English letters (e.g. dharma).",
             accepts("नासायाम्", None, "nasayam"),
             "नासायाम् (in the nose): चतुर्विंशतिर्नासायां.",
             "नासायाम् is the locative singular of the ā-stem नासा: 'in the nose'.",
             "चतुर्विंशतिः नासायाम्."),
        mcq("discriminate", 3, "Which split of चतुर्विंशतिर्नासायां in unit 28 is right?",
            ("चतुर्विंशतिः + नासायाम्", "इ + visarga before the voiced न → र्."),
            [("चतुर्विंशती + नासायाम्", "A word ending in ई with no visarga would not produce र्."),
             ("चतुर्विंशति + रनासायाम्", "रनासायाम् is not a word; the र् comes from the visarga."),
             ("चतुर्विंशतिम् + नासायाम्", "म् before न would be written ं or न्, never र्.")],
            "चतुर्विंशतिः (twenty-four) + नासायाम् (in the nose): इः before न → इर्.",
            "इ/उ + visarga before a voiced sound → र्."),
        mcq("apply", 4, "In चतुर्विंशतिर्नासायां, why does the visarga become र्?",
            ("It follows इ and stands before a voiced न", "After a vowel other than अ/आ, visarga + voiced sound → र्."),
            [("It follows अ and stands before a voiced न", "The vowel before the visarga is इ (-ति), not अ; अः would give ओ."),
             ("Every visarga becomes र् before any consonant", "Before त it becomes स्, before च श्; so not every consonant."),
             ("It is the last word of the sentence", "At a pause the visarga stays ः; here the next word follows.")],
            "चतुर्विंशतिः ends in इः; before the voiced न it becomes इर्.",
            "इः / उः + voiced sound → इर् / उर्."),
        mcq("transfer", 5, "By the rule of चतुर्विंशतिर्नासायां, how is हरिः + गच्छति (Hari goes) joined in a new example?",
            ("हरिर्गच्छति", "इ + visarga before the voiced ग → र्, as in चतुर्विंशतिर्नासायाम्."),
            [("हरिस्गच्छति", "स् comes before त or थ, not before ग."),
             ("हरि गच्छति", "The visarga drops before a voiced sound after आ, not after इ."),
             ("हरिश्गच्छति", "श् comes before च, छ or श, not before ग.")],
            "हरिः + गच्छति = हरिर्गच्छति, like चतुर्विंशतिः + नासायाम्.",
            "इः + voiced sound → इर्.",
            teaches="After इ or उ a visarga becomes र् before a voiced sound: चतुर्विंशतिः + नासायाम् → चतुर्विंशतिर्नासायाम्."),
    ],
}

# ---------------------------------------------------------------- unit 29
AUTHORED["29"] = {
    "title": "तासां द्वे गंधवेदिन्यौ",
    "question": "By unit 29, which three of the nose's sirās are named, and what is said of them?",
    "rule": ("Of them (apparently the 24 of the nose, unit 28), two perceive smell (गन्धवेदिन्यौ); and of those very ones "
             "(तासामेव) one is in the palate (तालुनि); thus three (इति तिस्रः)."),
    "limits": ("Prose and elliptical: एकाम् is an accusative with no verb, and none is supplied, so no question rests on its "
               "case. That तासाम् means the nose's 24 is the data's reading (appears); the sentence continues unit 28. "
               "Why these three are counted apart is not stated."),
    "explain_hi": ("यह पंक्ति इकाई २८ (नाक में चौबीस) को आगे बढ़ाती दिखती है। "
                   "उनमें दो सिराएँ गन्ध का बोध कराती हैं, और उन्हीं में से एक तालु में है; इस प्रकार तीन। "
                   "‘एकाम्’ द्वितीया है पर इसकी कोई क्रिया छपी नहीं; डेटा कोई क्रिया नहीं जोड़ता। "
                   "ये तीन अलग क्यों गिनी गईं, यह यहाँ नहीं कहा गया। "
                   "‘तालुन्येकाम्’ में तालुनि का इ अगले ए से पहले य् बना है।"),
    "hook": "नाक की चौबीस में: दो गन्ध पहचानें, एक तालु में, कुल तीन।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 29, what do two of the nose's sirās perceive?",
            ("Smell (gandha)", "द्वे गन्धवेदिन्यौ: two perceiving smell."),
            [("Taste (rasa)", "Taste is perceived by two sirās below the tongue (unit 27)."),
             ("Sound (śabda)", "Sound is carried by two sirās of the ears (unit 34)."),
             ("Touch (sparśa)", "Touch is not named in unit 29.")],
            "Of them, two perceive smell.",
            "तासां द्वे गंधवेदिन्यौ."),
        order(1, "Put the printed phrases of unit 29 in the line's order.",
              ["तासां", "द्वे गंधवेदिन्यौ", "तासामेव च", "तालुन्येकामिति तिस्रः"],
              "Of them; two smell-perceiving; and of those very ones; one in the palate, thus three.",
              "तासां → द्वे गंधवेदिन्यौ → तासामेव च → तालुन्येकामिति तिस्रः."),
        match(2, "Match each word of unit 29 to its meaning.",
              [["गन्ध", "smell"], ["वेदिनी", "perceiving"], ["तालु", "palate"], ["एव", "very, indeed"],
               ["तिस्रः", "three (feminine)"]],
              "गन्ध-वेदिनी = smell-perceiving; तालु = palate; तासामेव = of those very ones; तिस्रः = three.",
              "गन्ध, वेदिनी, तालु, एव, तिस्रः.", role="extend",
              teaches="तिस्रः is the feminine of 'three', agreeing with the feminine सिरा understood."),
        mcq("discriminate", 3, "Which split of तालुन्येकामिति in unit 29 is right?",
            ("तालुनि + एकाम् + इति", "इ before ए → य्: तालुन्ये-; एकाम् + इति → एकामिति."),
            [("तालु + न्येकाम् + इति", "न्येकाम् is not a word; the न्य् comes from तालुनि."),
             ("तालुनि + एकम् + इति", "एकम् + इति would give एकमिति; the print has -कामिति."),
             ("तालुनि + एका + मिति", "मिति is not a word; the म् belongs to एकाम्.")],
            "तालुनि (in the palate) + एकाम् (one) + इति (thus).",
            "इ + a different vowel → य्; म् joins a following vowel."),
        multi("apply", 4, "Which statements fit unit 29?",
              [("The line supplies a verb for एकाम्", "No verb is printed or supplied for एकाम्."),
               ("Two of the sirās perceive smell", "Right: द्वे गन्धवेदिन्यौ."),
               ("Three of them perceive taste", "Taste is not named in unit 29."),
               ("One of them is in the palate (tālu)", "Right: तालुनि ... एकाम्.")],
              [1, 3],
              "Two perceive smell, one is in the palate: three; एकाम् has no verb.",
              "द्वे गन्धवेदिन्यौ ... तालुन्येकामिति तिस्रः."),
        mcq("transfer", 5, "By the rule of तालुन्येकाम्, how is अस्ति + एव (it is indeed) joined in a new example?",
            ("अस्त्येव", "इ before a different vowel becomes य्, as तालुनि + एकाम् → तालुन्येकाम्."),
            [("अस्तेव", "The इ does not simply drop before ए."),
             ("अस्तैव", "ऐ comes from अ + ए, not from इ + ए."),
             ("अस्तीव", "ई comes from इ + इ, not from इ + ए.")],
            "अस्ति + एव = अस्त्येव, like तालुनि + एकाम् = तालुन्येकाम्.",
            "इ + ए → य्ए.",
            teaches="इ before a different vowel becomes य्: तालुनि + एकाम् → तालुन्येकाम्."),
    ],
}

# ---------------------------------------------------------------- unit 30
AUTHORED["30"] = {
    "title": "षट्पंचाशन्नेत्रयोः",
    "question": "By unit 30, how many sirās are in the two eyes (netra)?",
    "rule": ("Fifty-six (षट्पञ्चाशत्: six and fifty) are in the two eyes (नेत्रयोः, locative dual). The final त् is "
             "written न् before the न of नेत्रयोः."),
    "limits": ("Prose, one printed word; the copula and the counted noun are understood. The line does not split the 56 "
               "between the two eyes; the tasks of six of them follow in unit 31."),
    "explain_hi": ("यह गद्य-पंक्ति कहती है: दोनों नेत्रों में छप्पन। "
                   "षट्पञ्चाशत् = षट् (छह) + पञ्चाशत् (पचास)। "
                   "‘नेत्रयोः’ द्विवचन है, यहाँ सप्तमी: दोनों आँखों में। "
                   "छपे ‘षट्पंचाशन्नेत्रयोः’ में पञ्चाशत् का त् अगले न से पहले न् लिखा गया है; डेटा इसे नियमित सन्धि कहता है। "
                   "छप्पन दोनों आँखों में कैसे बँटीं, यह नहीं बताया गया।"),
    "hook": "दोनों आँखों में छप्पन: छह और पचास।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 30, how many sirās are in the two eyes?",
            ("Fifty-six", "षट्पञ्चाशत् = six and fifty = 56."),
            [("Sixty-five", "षट् is six and पञ्चाशत् fifty: 56, not 65."),
             ("Twenty-six", "पञ्चाशत् is fifty, not twenty."),
             ("Thirty-six", "पञ्चाशत् is fifty, not thirty.")],
            "Fifty-six in the two eyes.",
            "षट्पंचाशन्नेत्रयोः."),
        match(1, "Match each part of unit 30 to its meaning.",
              [["षट्", "six"], ["पञ्चाशत्", "fifty"], ["नेत्र", "eye"], ["नेत्रयोः", "in the two eyes"]],
              "षट्-पञ्चाशत् = 6 + 50 = 56; नेत्रयोः = in the two eyes.",
              "षट्, पञ्चाशत्, नेत्र, नेत्रयोः."),
        fill(2, "Unit 30: षट्पञ्चाशत् ____ (in the two eyes). Type it in Devanagari or in English letters (e.g. dharma).",
             accepts("नेत्रयोः", None, "netrayoh", "netrayo"),
             "नेत्रयोः (in the two eyes): षट्पञ्चाशन्नेत्रयोः.",
             "-योः is the genitive/locative dual; here the data reads it as locative: in the two eyes.",
             "षट्पञ्चाशत् नेत्रयोः."),
        mcq("discriminate", 3, "Which split of षट्पंचाशन्नेत्रयोः in unit 30 is right?",
            ("षट्पञ्चाशत् + नेत्रयोः", "The numeral is षट्पञ्चाशत्; its त् is written न् before न."),
            [("षट्पञ्चाशन् + नेत्रयोः", "There is no numeral पञ्चाशन्; the न् comes from the त् of पञ्चाशत्."),
             ("षट्पञ्च + आशन्नेत्रयोः", "आशन्नेत्रयोः is not a word; पञ्चाशत् is one numeral."),
             ("षट्पञ्चाशः + नेत्रयोः", "A visarga before न would not give न्न.")],
            "षट्पञ्चाशत् (fifty-six) + नेत्रयोः (in the two eyes).",
            "त् before न is written न् here (regular)."),
        mcq("apply", 4, "In षट्पंचाशन्नेत्रयोः, what does the print do with the त् of षट्पञ्चाशत्?",
            ("Writes न् before न", "The print shows -शन्ने-: त् is written न् before the न of नेत्रयोः."),
            [("Drops it before न", "Nothing is dropped: the print shows two न (-न्ने-)."),
             ("Writes च् before न", "च् comes from त् before च or छ, not before न."),
             ("Writes स् before न", "स् does not come from त् in this place.")],
            "षट्पञ्चाशत् + नेत्रयोः → षट्पञ्चाशन्नेत्रयोः: the त् is written न् before न.",
            "त् + न → न्न (as printed)."),
        mcq("transfer", 5, "By the pattern of नेत्रयोः, which form of हस्त (hand) means in the two hands, in a new example?",
            ("हस्तयोः", "-योः is the locative dual of an a-stem, as नेत्र → नेत्रयोः."),
            [("हस्तेषु", "-एषु is the locative plural: in the hands (more than two)."),
             ("हस्ते", "हस्ते is singular: in the hand."),
             ("हस्तौ", "हस्तौ is the nominative/accusative dual: the two hands.")],
            "हस्तयोः = in the two hands, like नेत्रयोः = in the two eyes.",
            "a-stem, locative dual: -योः.",
            teaches="-योः gives the locative (and genitive) dual of a-stems: नेत्र → नेत्रयोः, कर्ण → कर्णयोः (unit 34)."),
    ],
}

# ---------------------------------------------------------------- unit 31
AUTHORED["31"] = {
    "title": "तयोरुन्मेषनिमेषक्रिये",
    "question": "By unit 31, which actions and which places are named for six of the eyes' sirās?",
    "rule": ("Of those two (the eyes): for the actions of opening (उन्मेष) and closing (निमेष), two and two; and two in "
             "the two apāṅgas (outer corners of the eye); thus six (इति षट्)."),
    "limits": ("Prose, elliptical; continues unit 30. The split of the six is not firm: the data reads 2 + 2 + 2, but "
               "the dual क्रिये could go with the first द्वे; no question asks how the six are made up. Apāṅga is also "
               "a marma name (probable)."),
    "explain_hi": ("यह पंक्ति इकाई ३० (दोनों नेत्रों में छप्पन) को आगे बढ़ाती है। "
                   "उन दोनों में उन्मेष (आँख खोलना) और निमेष (आँख मूँदना) की क्रियाओं के लिए दो-दो, और दो दोनों अपाङ्गों यानी आँख के बाहरी कोनों में; इस प्रकार छह। "
                   "छह का बँटवारा पक्का नहीं: डेटा २ + २ + २ पढ़ता है, पर द्विवचन ‘क्रिये’ पहले ‘द्वे’ से भी जुड़ सकता है। "
                   "अपाङ्ग इस परम्परा में एक मर्म का नाम भी है (सम्भावित)। "
                   "‘तयोरुन्मेष’ में ओ के बाद का विसर्ग स्वर से पहले र् बना है।"),
    "hook": "खोलना-मूँदना और आँख के कोने: कुल छह।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 31, which two actions are linked with sirās of the eyes?",
            ("Opening and closing", "उन्मेष-निमेष-क्रिये: the actions of opening and closing."),
            [("Seeing and weeping", "Neither seeing nor weeping is named in unit 31."),
             ("Moving and turning", "Neither moving nor turning is named in unit 31."),
             ("Seeing colour and form", "Colour and form are not named in unit 31.")],
            "उन्मेष = opening, निमेष = closing (of the eyes).",
            "तयोरुन्मेषनिमेषक्रिये."),
        order(1, "Put the parts of unit 31 in the line's order.",
              ["तयोः", "उन्मेषनिमेषक्रिये", "द्वे द्वे द्वे", "चापांगयोरिति", "षट्"],
              "Of those two; the actions of opening and closing; two, two, two; and in the apāṅgas, thus; six.",
              "तयोः → उन्मेषनिमेषक्रिये → द्वे द्वे द्वे → चापांगयोरिति → षट्."),
        match(2, "Match each word of unit 31 to its meaning.",
              [["उन्मेष", "opening (of the eyes)"], ["निमेष", "closing (of the eyes)"], ["क्रिया", "action"],
               ["अपाङ्ग", "outer corner of the eye"], ["षट्", "six"]],
              "उन्मेष-निमेष-क्रिया = the action of opening and closing; अपाङ्ग = outer corner of the eye.",
              "उन्मेष, निमेष, क्रिया, अपाङ्ग, षट्.", role="extend",
              teaches="उन्मेष and निमेष are a pair of opposites joined in one dvandva, then tied to क्रिया (action)."),
        mcq("discriminate", 3, "Which split of चापांगयोरिति in unit 31 is right?",
            ("च + अपाङ्गयोः + इति", "अ + अ → आ (चा-); ओः before इ → ओर् (-योरिति)."),
            [("च + अपाङ्गयः + इति", "अः before इ would give अपाङ्गय इति, with no र्."),
             ("चा + पाङ्गयोः + इति", "Neither चा nor पाङ्गयोः is a word here."),
             ("च + अपाङ्गयोः + रिति", "रिति is not a word; the र् comes from the visarga.")],
            "च (and) + अपाङ्गयोः (in the two apāṅgas) + इति (thus).",
            "अ + अ → आ; ओः + vowel → ओर्."),
        mcq("apply", 4, "By unit 31, where are the last two sirās of the six?",
            ("In the apāṅgas (eye-corners)", "द्वे चापाङ्गयोः: two in the two apāṅgas."),
            [("In the eyelids (eye-covers)", "No eyelid is named in unit 31."),
             ("In the temples (śaṅkhas)", "The temples are not named in unit 31."),
             ("In the pupils of the eyes", "No pupil is named in unit 31.")],
            "The last two are in the two apāṅgas, the outer corners of the eye.",
            "द्वे चापाङ्गयोः."),
        mcq("transfer", 5, "By the rule of चापांगयोः (च + अपाङ्गयोः), how is न + अस्ति joined in a new example?",
            ("नास्ति", "अ + अ → आ, as च + अपाङ्गयोः → चापाङ्गयोः."),
            [("नस्ति", "Two अ do not merge into a short अ; they give आ."),
             ("नेस्ति", "ए comes from अ + इ, not from अ + अ."),
             ("नयस्ति", "No य् comes between two अ.")],
            "न + अस्ति = नास्ति, like च + अपाङ्गयोः = चापाङ्गयोः.",
            "अ + अ → आ.",
            teaches="Two like vowels merge into the long one: अ + अ → आ (च + अपाङ्गयोः → चापाङ्गयोः)."),
    ],
}

# ---------------------------------------------------------------- unit 32
AUTHORED["32"] = {
    "title": "नासानेत्रगतास्तुललाटे षष्टिः",
    "question": "By unit 32, how many sirās are in the forehead (lalāṭa), and where do they go?",
    "rule": ("Those going to the nose and eyes (नासानेत्रगताः), however (तु), are sixty (षष्टिः) in the forehead "
             "(ललाटे)."),
    "limits": ("Prose; the copula is understood and the sentence continues unit 31. The line states no relation between "
               "these sixty and the nose's 24 or the eyes' 56; the data's sum check suggests they are not additional, but "
               "that is not stated, so no question rests on it."),
    "explain_hi": ("यह गद्य-पंक्ति ललाट यानी माथे की सिराएँ गिनती है: जो नासा और नेत्रों तक जाती हैं, वे ललाट में साठ हैं। "
                   "‘तु’ (तो) से नई बात आरम्भ होती है। "
                   "ये साठ नाक की चौबीस और आँखों की छप्पन से अलग हैं या उन्हीं का भाग, यह पंक्ति नहीं कहती; डेटा का जोड़ इन्हें अतिरिक्त नहीं मानता, पर यह अनुमान है। "
                   "‘नासानेत्रगतास्तु’ में विसर्ग त से पहले स् बना है।"),
    "hook": "माथे में साठ: जो नाक और आँख तक जाती हैं।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 32, how many sirās are in the forehead (lalāṭa)?",
            ("Sixty", "ललाटे षष्टिः: sixty in the forehead."),
            [("Sixteen", "Sixteen is षोडश; the line has षष्टिः, sixty."),
             ("Six", "Six is षट्; षष्टि is sixty."),
             ("Seventy", "Seventy is सप्तति; the line has षष्टिः.")],
            "Sixty in the forehead.",
            "ललाटे षष्टिः."),
        match(1, "Match each word part of unit 32 to its meaning.",
              [["नासा", "nose"], ["नेत्र", "eye"], ["गत", "gone to"], ["ललाट", "forehead"], ["षष्टि", "sixty"]],
              "नासा-नेत्र-गताः = gone to the nose and eyes; ललाटे षष्टिः = sixty in the forehead.",
              "नासा, नेत्र, गत, ललाट, षष्टि."),
        order(2, "Put the words of unit 32 in the line's order.",
              ["नासानेत्रगताः", "तु", "ललाटे", "षष्टिः"],
              "Those going to the nose and eyes, however, in the forehead, sixty.",
              "नासानेत्रगताः → तु → ललाटे → षष्टिः.", role="extend",
              teaches="नासानेत्रगताः is a tat-puruṣa: the dvandva नासा-नेत्र + गत (gone to), feminine plural for the sirās."),
        mcq("discriminate", 3, "Which split of नासानेत्रगतास्तु in unit 32 is right?",
            ("नासानेत्रगताः + तु", "आः before त: the visarga becomes स्, giving -गतास्तु."),
            [("नासानेत्रगतात् + तु", "त् + त would give -गतात्तु, not -गतास्तु."),
             ("नासानेत्रगतम् + तु", "म् before त would be written ं or न्, not स्."),
             ("नासानेत्रगते + स्तु", "स्तु is not a word; the स् comes from the visarga.")],
            "नासानेत्रगताः (gone to the nose and eyes) + तु (however).",
            "Visarga before त → स्."),
        mcq("apply", 4, "By unit 32, which sirās are the sixty in the forehead?",
            ("Those going to the nose and eyes", "नासानेत्रगताः: gone to the nose and eyes."),
            [("Those going to the ears and temples", "Ears and temples are not named in unit 32."),
             ("Those going to the tongue and palate", "Tongue and palate are not named in unit 32."),
             ("Those going to the hair and the crown", "Hair and crown are not named in unit 32.")],
            "The sixty in the forehead are those going to the nose and eyes.",
            "नासानेत्रगतास्तु ललाटे षष्टिः."),
        mcq("transfer", 5, "By the rule of नासानेत्रगतास्तु, how is जनाः + तत्र (the people there) joined in a new example?",
            ("जनास्तत्र", "Visarga before त becomes स्, as नासानेत्रगताः + तु → नासानेत्रगतास्तु."),
            [("जनाश्तत्र", "श् comes before च, छ or श, not before त."),
             ("जना तत्र", "After आ the visarga drops before a voiced sound; त is not voiced."),
             ("जनो तत्र", "ओ comes from अः before a voiced consonant, not from आः.")],
            "जनाः + तत्र = जनास्तत्र, like नासानेत्रगताः + तु.",
            "Visarga + त → स्त.",
            teaches="A visarga before त becomes स्: नासानेत्रगताः + तु → नासानेत्रगतास्तु."),
    ],
}

# ---------------------------------------------------------------- unit 33
AUTHORED["33"] = {
    "title": "तासां केशांतनुगताश्चतस्रो",
    "question": "By unit 33, which seven sirās are named, and in which places?",
    "rule": ("Of them (apparently the forehead's sixty, unit 32): four going along to the keśānta (end of the hair, "
             "probably the hair-line), two in the two āvartas, one in the sthapanī; thus seven (इति सप्त)."),
    "limits": ("Prose; continues unit 32. Printed केशांतनुगताः has a short -a- where the join should be long (flagged "
               "as possible); no question rests on its form. Keśānta = hair-line is probable; āvarta and sthapanī are "
               "marma names (probable). Why seven are counted apart is not stated."),
    "explain_hi": ("यह पंक्ति इकाई ३२ (ललाट में साठ) को आगे बढ़ाती दिखती है। "
                   "उनमें चार केशान्त तक जाती हैं (केशान्त = केशों का अन्त, सम्भवतः केश-रेखा), दो दोनों आवर्तों में और एक स्थपनी में; इस प्रकार सात। "
                   "आवर्त और स्थपनी नामित स्थान हैं, इस परम्परा में मर्मों के नाम (सम्भावित)। "
                   "छपे ‘केशांतनुगताः’ में अ + अ का दीर्घ आ नहीं दिखता; डेटा इसे सम्भावित भूल मानता है, अर्थ वही रहता है। "
                   "ये सात अलग क्यों गिनी गईं, यह नहीं कहा गया।"),
    "hook": "माथे में सात: चार केश-रेखा तक, दो आवर्त में, एक स्थपनी में।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 33, how many sirās are in the sthapanī?",
            ("One", "एका च स्थपन्याम्: and one in the sthapanī."),
            [("Two", "Two are in the two āvartas, not in the sthapanī."),
             ("Four", "Four go along to the keśānta (hair-line, probable)."),
             ("Three", "No group of three is named in unit 33.")],
            "One in the sthapanī.",
            "एका च स्थपन्याम्."),
        order(1, "Put the printed phrases of unit 33 in the line's order.",
              ["तासां", "केशांतनुगताश्चतस्रो", "द्वे आवर्तयोरेका च", "स्थपन्यामिति सप्त"],
              "Of them; four going to the keśānta; two in the āvartas, and one; in the sthapanī, thus seven.",
              "तासां → केशांतनुगताश्चतस्रो → द्वे आवर्तयोरेका च → स्थपन्यामिति सप्त."),
        match(2, "Match each place of unit 33 to the number printed for it.",
              [["केशान्त (hair-line, probable)", "four"], ["आवर्त (the two āvartas)", "two"],
               ["स्थपनी", "one"], ["इति सप्त", "seven in all"]],
              "Four to the keśānta, two in the āvartas, one in the sthapanī: seven.",
              "चतस्रः, द्वे, एका; इति सप्त.", role="extend",
              teaches="इति closes the list and सप्त gives its total: 4 + 2 + 1 = 7, as printed."),
        mcq("discriminate", 3, "Which split of आवर्तयोरेका in unit 33 is right?",
            ("आवर्तयोः + एका", "ओः before a vowel → ओर्: आवर्तयोः + एका → आवर्तयोरेका."),
            [("आवर्तयो + रेका", "रेका is not a word; the र् comes from the visarga."),
             ("आवर्तयोः + अका", "ओः + अ would give -योरका; the print has -योरेका."),
             ("आवर्तयत् + एका", "त् before ए would give -यदेका, not -योरेका.")],
            "आवर्तयोः (in the two āvartas) + एका (one).",
            "ओः + vowel → ओर्."),
        multi("apply", 4, "Which places have sirās named in unit 33?",
              [("The eyebrows (bhrū)", "No eyebrow is named in unit 33."),
               ("The keśānta (hair-line, probable)", "Right: केशान्त ... चतस्रः, four."),
               ("The sthapanī", "Right: एका च स्थपन्याम्, one."),
               ("The lips (oṣṭha)", "No lip is named in unit 33.")],
              [1, 2],
              "Keśānta (four), āvartas (two), sthapanī (one).",
              "केशान्त, आवर्त, स्थपनी."),
        mcq("transfer", 5, "By the rule of आवर्तयोरेका, how is नेत्रयोः + अपि (in the two eyes too) joined in a new example?",
            ("नेत्रयोरपि", "ओः before a vowel → ओर्, as आवर्तयोः + एका → आवर्तयोरेका."),
            [("नेत्रयोऽपि", "ओ + अ → ओऽ holds for a final ओ, not for ओः with a visarga."),
             ("नेत्रयवपि", "अव् comes from a final ओ with no visarga."),
             ("नेत्रयो अपि", "After ओ the visarga is not dropped; it becomes र्.")],
            "नेत्रयोः + अपि = नेत्रयोरपि, like आवर्तयोः + एका = आवर्तयोरेका.",
            "ओः + vowel → ओर्.",
            teaches="After a vowel other than अ/आ (here ओ), a visarga becomes र् before a voiced sound: आवर्तयोः + एका → आवर्तयोरेका."),
    ],
}

# ---------------------------------------------------------------- unit 34
AUTHORED["34"] = {
    "title": "कर्णयोः षोडश",
    "question": "By unit 34, how many sirās are in the ears, and which of them are named?",
    "rule": ("In the two ears (कर्णयोः), sixteen; of them two carry sound (शब्दवाहिन्यौ); those very two (ते एव) are also "
             "in the two temples (शङ्खयोः); of them two are gone to the temple joint (शङ्खसन्धिगते)."),
    "limits": ("Prose, partly elliptical; continues unit 33. How 'those very two' relate to the temples is not "
               "explained; that they are not two extra ones is the data's inference from a sum: no question rests on "
               "it. Śaṅkha = temple (standard; also means conch)."),
    "explain_hi": ("यह पंक्ति कानों की सिराएँ बताती है: दोनों कर्णों में सोलह। "
                   "उनमें दो शब्द यानी ध्वनि का वहन करती हैं; वही दोनों शंखों यानी कनपटियों में भी हैं; और उनमें दो शंख की सन्धि तक जाती हैं। "
                   "‘वही दोनों’ का शंखों से सम्बन्ध पंक्ति में आगे नहीं समझाया गया; डेटा जोड़ से अनुमान करता है कि ये अतिरिक्त दो नहीं, पर यह छपा नहीं। "
                   "शंख का अर्थ यहाँ कनपटी है (मानक); यही शब्द शंख (समुद्री) भी है। "
                   "‘ते एव’ अलग रहते हैं: ए पर समाप्त द्विवचन के बाद स्वर-सन्धि नहीं होती।"),
    "hook": "कान में सोलह: दो शब्द-वाहिनी, वही शंख में; दो शंख-सन्धि तक।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 34, what do two of the ears' sirās carry?",
            ("Sound (śabda)", "शब्दवाहिन्यौ द्वे: two carrying sound."),
            [("Smell (gandha)", "Smell is perceived by two of the nose's sirās (unit 29)."),
             ("Taste (rasa)", "Taste is perceived by two sirās below the tongue (unit 27)."),
             ("Speech (vāk)", "Speech is set going by two sirās below the tongue (unit 27).")],
            "Of the ears' sixteen, two carry sound.",
            "तासां शब्दवाहिन्यौ द्वे."),
        order(1, "Put the printed clauses of unit 34 in the line's order.",
              ["कर्णयोः षोडश", "तासां शब्दवाहिन्यौ द्वे", "ते एवच शंखयोः", "तासां शंखसंधिगते द्वे"],
              "Sixteen in the ears; two sound-carriers; those very two also in the temples; two gone to the temple joint.",
              "कर्णयोः षोडश → तासां शब्दवाहिन्यौ द्वे → ते एवच शंखयोः → तासां शंखसंधिगते द्वे."),
        match(2, "Match each word of unit 34 to its meaning.",
              [["कर्ण", "ear"], ["शब्द", "sound"], ["वाहिनी", "carrying"], ["शङ्ख", "temple (of the head)"],
               ["सन्धि", "joint"]],
              "शब्द-वाहिनी = sound-carrying; शङ्ख-सन्धि-गत = gone to the joint of the temple.",
              "कर्ण, शब्द, वाहिनी, शङ्ख, सन्धि.", role="extend",
              teaches="शङ्खसन्धिगते is a tat-puruṣa in the feminine dual: gone (गत) to the joint (सन्धि) of the temple (शङ्ख)."),
        mcq("discriminate", 3, "Why do ते and एव stay apart in unit 34?",
            ("ते is dual; a dual in ए keeps its vowel", "A dual ending in ए (here ते, f. nom. du.) takes no vowel sandhi."),
            [("ते is a verb; verbs never join vowels", "ते here is a pronoun (those two), not a verb."),
             ("एव never joins a word before it", "एव does join: तासाम् + एव → तासामेव (unit 29)."),
             ("The printer left out a join", "Nothing is left out; the gap is regular for a dual in ए.")],
            "ते (those two, dual) + एव: a dual ending in ए stays unchanged before a vowel.",
            "Dual in ई/ऊ/ए + vowel: no sandhi."),
        mcq("apply", 4, "By unit 34, to where are the last two sirās gone?",
            ("The joint of the temple", "शङ्खसन्धिगते द्वे: two gone to the joint of the temple."),
            [("The joint of the neck", "No joint of the neck is named in unit 34."),
             ("The joint of the shoulder", "No shoulder is named in unit 34."),
             ("The root of the tongue", "The tongue is not named in unit 34.")],
            "The last two are gone to the joint of the temple (śaṅkha).",
            "तासां शंखसंधिगते द्वे."),
        mcq("transfer", 5, "By the rule of ते एव, how are फले + इमे (these two fruits) written together in a new example?",
            ("फले इमे", "फले is a dual in ए, so it stays unchanged before इ, as ते एव."),
            [("फलयिमे", "अय् from ए applies to a non-dual ए; a dual ए stays."),
             ("फल इमे", "Dropping to अ applies to a non-dual ए; a dual ए stays."),
             ("फलाविमे", "आव् comes from औ before a vowel; there is no औ here.")],
            "फले इमे stay apart, like ते एव: a dual in ए takes no vowel sandhi.",
            "Dual in ए + vowel: no sandhi.",
            teaches="A dual ending in ई, ऊ or ए does not join a following vowel: ते एव (unit 34), द्वे आवर्तयोः (unit 33)."),
    ],
}

# ---------------------------------------------------------------- unit 35
AUTHORED["35"] = {
    "title": "द्वादश मूर्द्धनि",
    "question": "By unit 35, how many sirās are in the head (mūrdhan)?",
    "rule": ("Twelve (द्वादश) are in the head (मूर्धनि, locative singular of मूर्धन्); the print spells it मूर्द्धनि."),
    "limits": ("Prose, two words; the copula and the counted noun are understood. The printed -र्द्ध- is a spelling of "
               "-र्ध-. The places of eight of the twelve follow in unit 36."),
    "explain_hi": ("यह दो शब्दों की गद्य-पंक्ति है: सिर (मूर्धा) में बारह। "
                   "द्वादश = द्वा (दो) + दश (दस)। "
                   "‘मूर्धनि’ मूर्धन् शब्द की सप्तमी एकवचन है: सिर में। "
                   "छपाई ‘मूर्द्धनि’ में द दोहरा लिखा है; यह केवल वर्तनी है। "
                   "अगली इकाई ३६ इन बारह में से आठ के स्थान बताती है।"),
    "hook": "सिर में बारह: दो और दस।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 35, how many sirās are in the head?",
            ("Twelve", "द्वादश = twelve, मूर्धनि = in the head."),
            [("Twenty", "Twenty is विंशति; द्वादश is two and ten."),
             ("Sixteen", "Sixteen is षोडश; द्वादश is twelve."),
             ("Ten", "Ten is दश alone; द्वा-दश adds two.")],
            "Twelve in the head.",
            "द्वादश मूर्द्धनि."),
        match(1, "Match each part of unit 35 to its meaning.",
              [["द्वा", "two"], ["दश", "ten"], ["द्वादश", "twelve"], ["मूर्धन्", "head"]],
              "द्वा-दश = 2 + 10 = 12; मूर्धनि = in the head.",
              "द्वा, दश, द्वादश, मूर्धन्."),
        fill(2, "Unit 35: द्वादश ____ (in the head). Type it in Devanagari or in English letters (e.g. dharma).",
             accepts("मूर्धनि", None, "मूर्द्धनि", "murdhani", "murddhani"),
             "मूर्धनि (in the head), printed मूर्द्धनि.",
             "मूर्धनि is the locative singular of मूर्धन् (head).",
             "द्वादश मूर्धनि."),
        mcq("discriminate", 3, "In unit 35, what form is मूर्द्धनि (मूर्धनि)?",
            ("Locative singular: in the head", "The data labels it m. loc. sg.: in the head."),
            [("Nominative singular: the head", "The nominative is मूर्धा."),
             ("Locative plural: in the heads", "The locative plural would be मूर्धसु."),
             ("Instrumental singular: by the head", "The instrumental is मूर्ध्ना.")],
            "मूर्धनि = locative singular of मूर्धन्: in the head.",
            "मूर्धन् → मूर्धनि (loc. sg.)."),
        multi("apply", 4, "Which statements fit unit 35?",
              [("Twelve sirās are counted in the head", "Right: द्वादश मूर्द्धनि."),
               ("The line names the tasks of the twelve", "No task is named in unit 35."),
               ("The line prints a verb", "No verb is printed; the copula is understood."),
               ("The print spells the word मूर्द्धनि", "Right: -र्द्ध- is printed for -र्ध-.")],
              [0, 3],
              "Twelve in the head; no verb, no tasks; the print spells मूर्द्धनि.",
              "द्वादश मूर्द्धनि."),
        mcq("transfer", 5, "By the pattern of द्वादश (two + ten = twelve), what does अष्टादश mean in a new example?",
            ("Eighteen", "अष्ट (eight) + दश (ten) = 18, as द्वा + दश = 12."),
            [("Eighty", "Eighty is अशीति; -दश adds ten."),
             ("Twenty-eight", "-दश adds ten, not twenty."),
             ("Eight", "Eight is अष्ट alone; -दश adds ten.")],
            "अष्टादश = 8 + 10 = 18, like द्वादश = 2 + 10 = 12.",
            "Unit-number + दश = that number plus ten.",
            teaches="Numbers 11 to 19 are a unit-number joined to दश: द्वा-दश = 12, षो-डश = 16, अष्टा-दश = 18."),
    ],
}

# ---------------------------------------------------------------- unit 36
AUTHORED["36"] = {
    "title": "तासामुत्क्षेपयोर्द्वे",
    "question": "By unit 36, which eight of the head's sirās are named, and what should one do with them?",
    "rule": ("Of them (the head's twelve, unit 35): two in the two utkṣepas, one each in the sīmantas, one in the "
             "adhipati; thus eight (इत्यष्टौ). One should avoid them with the knife (शस्त्रेण परिहरेत्)."),
    "limits": ("Prose; continues unit 35. एकैकाम् and एकाम् are accusatives with no verb; none is supplied. The total "
               "eight needs five sīmantas, which the line does not state: no question on their number. Utkṣepa, "
               "sīmanta and adhipati are marma names (probable)."),
    "explain_hi": ("यह पंक्ति इकाई ३५ (सिर में बारह) को आगे बढ़ाती है। "
                   "उनमें दो दोनों उत्क्षेपों में, एक-एक सीमन्तों में और एक अधिपति में; इस प्रकार आठ; इन्हें शस्त्र से बचाना चाहिए (परिहरेत्, विधिलिङ्)। "
                   "उत्क्षेप, सीमन्त और अधिपति नामित स्थान हैं, इस परम्परा में मर्मों के नाम (सम्भावित)। "
                   "आठ का जोड़ तभी बनता है जब सीमन्त पाँच हों, पर पंक्ति उनकी संख्या नहीं देती। "
                   "‘एकैकाम्’ और ‘एकाम्’ द्वितीया हैं, उनकी कोई क्रिया छपी नहीं।"),
    "hook": "सिर में आठ बचाओ: उत्क्षेप, सीमन्त, अधिपति।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 36, what should one do with these eight sirās?",
            ("Avoid them with the knife", "शस्त्रेण परिहरेत्: one should avoid them with the knife."),
            [("Pierce them with the knife", "परिहरेत् means avoid, not pierce."),
             ("Press them with the hand", "No pressing by hand is named in unit 36."),
             ("Heat them with fire", "No fire is named in unit 36.")],
            "The eight are to be avoided with the knife.",
            "इत्यष्टौ शस्त्रेण परिहरेत्."),
        order(1, "Put the places of unit 36 and its last words in the line's order.",
              ["उत्क्षेपयोः", "सीमन्तेषु", "अधिपतौ", "शस्त्रेण परिहरेत्"],
              "Utkṣepas, sīmantas, adhipati; then: avoid with the knife.",
              "उत्क्षेपयोः → सीमन्तेषु → अधिपतौ → शस्त्रेण परिहरेत्."),
        match(2, "Match each place of unit 36 to the count printed with it.",
              [["उत्क्षेपयोः", "two (द्वे)"], ["सीमन्तेषु", "one each (एकैकाम्)"], ["अधिपतौ", "one (एकाम्)"],
               ["इति", "eight in all (अष्टौ)"]],
              "Two in the utkṣepas, one each in the sīmantas, one in the adhipati: eight.",
              "द्वे, एकैकाम्, एकाम्; इत्यष्टौ.", role="extend",
              teaches="एकैक (एक + एक) means 'one each': one in every sīmanta."),
        mcq("discriminate", 3, "Which split of अधिपताविति in unit 36 is right?",
            ("अधिपतौ + इति", "औ before a vowel → आव्: अधिपतौ + इति → अधिपताविति."),
            [("अधिपता + विति", "विति is not a word; the व् comes from औ."),
             ("अधिपतेः + इति", "एः before इ would give अधिपतेरिति."),
             ("अधिपतिः + इति", "इः before इ would give अधिपतिरिति.")],
            "अधिपतौ (in the adhipati) + इति (thus): औ + vowel → आव्.",
            "औ + vowel → आव्."),
        mcq("apply", 4, "In unit 36, what kind of form is परिहरेत्?",
            ("Optative, 'one should avoid'", "The data labels it 3 sg. opt. of pari-√hṛ."),
            [("Future tense, 'one will avoid'", "A future would be परिहरिष्यति."),
             ("Past tense, 'one avoided them'", "A past form would be पर्यहरत्."),
             ("Imperative, 'avoid (them)!'", "The imperative 2 sg. would be परिहर.")],
            "परिहरेत् = optative: one should avoid; it gives the rule for these sirās.",
            "परिहरेत् = 3 sg. optative: one should avoid."),
        mcq("transfer", 5, "By the rule of अधिपताविति, how is गुरौ + अपि (in the teacher too) joined in a new example?",
            ("गुरावपि", "औ before a vowel → आव्, as अधिपतौ + इति → अधिपताविति."),
            [("गुरवपि", "अव् comes from ओ before a vowel, not from औ."),
             ("गुरायपि", "आय् comes from ऐ before a vowel, not from औ."),
             ("गुरौऽपि", "The avagraha join belongs to ए/ओ before अ, not to औ.")],
            "गुरौ + अपि = गुरावपि, like अधिपतौ + इति = अधिपताविति.",
            "औ + vowel → आव्.",
            teaches="A final औ before a vowel becomes आव्: अधिपतौ + इति → अधिपताविति."),
    ],
}

# ---------------------------------------------------------------- unit 37
AUTHORED["37"] = {
    "title": "क्षुद्रिकाः कुटिलाः संकीर्णा ग्रथिताः",
    "question": "By unit 37, which further sirās are not to be treated with the knife?",
    "rule": ("Small (क्षुद्रिकाः), crooked (कुटिलाः), intermingled (संकीर्णाः), knotted (ग्रथिताः) ones, and those in the "
             "joints (सन्धिषु): these are not to be done with the knife (अशस्त्रकृत्याः)."),
    "limits": ("Low confidence. The first printed word नतथा is doubtful: 'likewise' (तथा) is a conjecture, since न तथा would "
               "clash with the following negative; no question rests on it. The noun (sirās) and the copula are "
               "understood. The sentence continues unit 36."),
    "explain_hi": ("यह पंक्ति आगे की सिराएँ बताती है जिन पर शस्त्र-कर्म नहीं करना चाहिए: छोटी, टेढ़ी, मिली हुई, गुँथी हुई, और जोड़ों में स्थित। "
                   "पहला छपा शब्द ‘नतथा’ संदिग्ध है: ‘न तथा’ पढ़ें तो आगे के ‘अशस्त्रकृत्याः’ के साथ दोहरा निषेध बनता है, इसलिए ‘तथा’ (इसी प्रकार) अनुमानित पाठ है। "
                   "डेटा का विश्वास निम्न है; प्रश्न केवल पक्के भाग पर हैं। "
                   "‘संकीर्णा ग्रथिताः’ में आ के बाद का विसर्ग घोष व्यंजन ग से पहले लुप्त हुआ है। "
                   "अशस्त्रकृत्य = जो शस्त्र से करने योग्य नहीं।"),
    "hook": "छोटी, टेढ़ी, उलझी, गाँठदार और जोड़ वाली: शस्त्र नहीं।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 37, how are the listed sirās to be treated?",
            ("Not to be done with the knife", "अशस्त्रकृत्याः: not to be done with the knife (śastra)."),
            [("To be pierced before others", "अशस्त्रकृत्य rules the knife out."),
             ("To be cut only in the joints", "Those in the joints are among the ones ruled out."),
             ("To be pressed before piercing", "No pressing is named in unit 37.")],
            "The listed ones are not to be dealt with by the knife.",
            "... संधिषु चाशस्त्रकृत्याः."),
        order(1, "Put the listed kinds of unit 37 in the line's order.",
              ["क्षुद्रिकाः", "कुटिलाः", "संकीर्णा", "ग्रथिताः", "संधिषु"],
              "Small, crooked, intermingled, knotted, in the joints.",
              "क्षुद्रिकाः → कुटिलाः → संकीर्णा → ग्रथिताः → संधिषु."),
        match(2, "Match each word of unit 37 to its meaning.",
              [["क्षुद्रिका", "small"], ["कुटिल", "crooked"], ["संकीर्ण", "intermingled"], ["ग्रथित", "knotted"],
               ["सन्धि", "joint"]],
              "Small, crooked, intermingled, knotted, and in the joints: not for the knife.",
              "क्षुद्रिका, कुटिल, संकीर्ण, ग्रथित, सन्धि.", role="extend",
              teaches="ग्रथित (knotted) is a recognised variant of ग्रन्थित; अ-शस्त्र-कृत्य = not to be done with the knife."),
        mcq("discriminate", 3, "Why is संकीर्णाः printed संकीर्णा before ग्रथिताः in unit 37?",
            ("After आ the visarga drops before a voiced sound", "ग is voiced: संकीर्णाः + ग्रथिताः → संकीर्णा ग्रथिताः."),
            [("After आ the visarga drops before any consonant", "Before त it becomes स्, before च श्; so not any consonant."),
             ("The visarga became ओ and was then lost", "ओ comes from अः, not from आः."),
             ("The printer left out the visarga", "The data calls the dropped visarga regular sandhi.")],
            "आः before the voiced ग: the visarga drops.",
            "आः + voiced sound → आ."),
        multi("apply", 4, "Which kinds does unit 37 name among those not for the knife?",
              [("The crooked ones", "Right: कुटिलाः."),
               ("The thick ones", "No thick ones are named in unit 37."),
               ("Those in the joints", "Right: संधिषु."),
               ("The straight ones", "Straight ones are not named; crooked ones are.")],
              [0, 2],
              "Small, crooked, intermingled, knotted, and in the joints.",
              "क्षुद्रिकाः कुटिलाः संकीर्णा ग्रथिताः संधिषु."),
        mcq("transfer", 5, "By the rule of संकीर्णा ग्रथिताः, how is बालाः + गच्छन्ति (the boys go) joined in a new example?",
            ("बाला गच्छन्ति", "After आ the visarga drops before the voiced ग, as संकीर्णाः + ग्रथिताः."),
            [("बालो गच्छन्ति", "ओ comes from अः before a voiced consonant, not from आः."),
             ("बालार्गच्छन्ति", "र् comes after vowels other than अ/आ, not after आ."),
             ("बालास्गच्छन्ति", "स् comes before त or थ, not before ग.")],
            "बालाः + गच्छन्ति = बाला गच्छन्ति, like संकीर्णाः + ग्रथिताः = संकीर्णा ग्रथिताः.",
            "आः + voiced sound → आ.",
            teaches="After आ a visarga drops before a voiced sound: संकीर्णाः + ग्रथिताः → संकीर्णा ग्रथिताः."),
    ],
}

# ---------------------------------------------------------------- unit 38
AUTHORED["38"] = {
    "title": "पंचसप्तत्यधिकं शतकमनिलरक्तं वहति",
    "question": "By unit 38, how many sirās carry anila-rakta (Vāta and blood), and by what division?",
    "rule": ("Of them (the sirās), each according to its own (यथास्वम्), by a division into fourth parts "
             "(तुर्यांशविभागेन), a set of a hundred plus seventy-five (175) carries anila-rakta (Vāta and blood)."),
    "limits": ("Prose. 175 as a quarter of the 700 of unit 4 is the data's arithmetic note. अनिलरक्तम् is read as a "
               "dvandva (Vāta and blood); one compound, blood with Vāta, is possible and undecided: no question rests "
               "on it. Unit 39 extends the division to Pitta, Kapha and pure blood."),
    "explain_hi": ("यह गद्य-पंक्ति दोष-वाही सिराओं का विभाग आरम्भ करती है। "
                   "उनमें, अपने-अपने अनुसार, चौथे अंश के विभाग से, पचहत्तर अधिक सौ (१७५) का समूह अनिल यानी वात और रक्त का वहन करता है। "
                   "डेटा की टिप्पणी: १७५ इकाई ४ की सात सौ सिराओं का चौथा भाग है। "
                   "‘अनिलरक्तम्’ को द्वन्द्व (वात और रक्त) पढ़ा गया है; ‘वात-युक्त रक्त’ भी सम्भव है, निर्णय नहीं किया गया। "
                   "अगली इकाई ३९ यही विभाग पित्त, कफ और शुद्ध रक्त में भी बताती है।"),
    "hook": "सात सौ का चौथाई, एक सौ पचहत्तर: वात और रक्त का वहन।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 38, how many sirās carry anila-rakta?",
            ("175", "पञ्चसप्तत्यधिकं शतकम्: a hundred plus seventy-five."),
            [("150", "पञ्चसप्तति is seventy-five, not fifty."),
             ("75", "शतकम् adds a hundred to the seventy-five."),
             ("125", "पञ्चसप्तति is seventy-five, not twenty-five.")],
            "A set of 100 + 75 = 175 carries anila-rakta.",
            "पंचसप्तत्यधिकं शतकमनिलरक्तं वहति."),
        order(1, "Put the printed words of unit 38 in the line's order.",
              ["तासां", "यथास्वं", "तुर्यांशविभागेन", "पंचसप्तत्यधिकं", "शतकमनिलरक्तं", "वहति"],
              "Of them; each by its own; by a division into fourths; with seventy-five more; a hundred, Vāta and blood; carries.",
              "तासां → यथास्वं → तुर्यांशविभागेन → पंचसप्तत्यधिकं → शतकमनिलरक्तं → वहति."),
        match(2, "Match each word part of unit 38 to its meaning.",
              [["तुर्य", "fourth"], ["अंश", "part"], ["विभाग", "division"], ["पञ्चसप्तति", "seventy-five"],
               ["अधिक", "in excess"], ["वहति", "carries"]],
              "तुर्य-अंश-विभाग = division into fourth parts; पञ्चसप्तति-अधिकं शतकम् = 175.",
              "तुर्य, अंश, विभाग, पञ्चसप्तति, अधिक, वहति.", role="extend",
              teaches="X-अधिकं शतम्/शतकम् = a hundred with X in excess: पञ्चसप्तत्यधिकं शतकम् = 175."),
        mcq("discriminate", 3, "Which split of पंचसप्तत्यधिकं in unit 38 is right?",
            ("पञ्चसप्तति + अधिकम्", "इ before a different vowel → य्: -सप्तत्यधिकम्."),
            [("पञ्चसप्तत् + यधिकम्", "यधिकम् is not a word; the word is अधिकम् (in excess)."),
             ("पञ्चसप्तती + धिकम्", "धिकम् is not a word; अ- belongs to अधिकम्."),
             ("पञ्चसप्तते + अधिकम्", "ए + अ would give -सप्ततेऽधिकम्, with ए kept.")],
            "पञ्चसप्तति (seventy-five) + अधिकम् (in excess): इ + अ → य.",
            "इ + a different vowel → य् + that vowel."),
        mcq("apply", 4, "By the data's note, how does 175 relate to the sirās of unit 4?",
            ("It is a fourth of the 700", "तुर्यांश = a fourth part; 700 ÷ 4 = 175 (data note)."),
            [("It is a third of the 525", "No 525 is given; the whole in unit 4 is 700."),
             ("It is a half of the 350", "No 350 is given; the whole in unit 4 is 700."),
             ("It is a fifth of the 875", "No 875 is given; the whole in unit 4 is 700.")],
            "175 = a quarter of the 700 sirās of unit 4.",
            "तुर्यांशविभागेन: 700 ÷ 4 = 175."),
        mcq("transfer", 5, "By the pattern of पञ्चसप्तत्यधिकं शतकम्, what does विंशत्यधिकं शतम् mean in a new example?",
            ("120", "शतम् = 100; विंशति-अधिकम् = twenty in excess: 120."),
            [("2,000", "अधिक adds; it does not multiply."),
             ("80", "अधिक means in excess, not less."),
             ("102", "विंशति is twenty, not two.")],
            "विंशत्यधिकं शतम् = 100 + 20 = 120, as पञ्चसप्तत्यधिकं शतकम् = 175.",
            "X-अधिकं शतम् = 100 + X.",
            teaches="X-अधिकं शतम् means a hundred with X in excess: पञ्चसप्तत्यधिकं शतकम् = 175."),
    ],
}


# ================================================================= NOTES_HI
NOTES_HI = {
    "27": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। ‘तासामधो’ = ‘उनके नीचे’; ‘उनमें से, नीचे की ओर’ भी सम्भव। अन्तिम वाक्य में "
           "क्रिया समझी जाती है। समूह-टिप्पणी: इकाई २६ (जीभ) को आगे बढ़ाती दिखती है। छपाई ‘द्वेवाक्प्रवर्तिन्यौ’ में द्वे और "
           "वाक्प्रवर्तिन्यौ बिना अन्तर के जुड़े हैं (केवल छपाई)। सन्धि जाँची: तासाम् + अधः → तासामधः (स्वर से पहले म्); अधः + द्वे → "
           "अधो द्वे (अः + घोष व्यंजन → ओ); ताः + चतस्रः → ताश्चतस्रः (च से पहले विसर्ग → श्)।"),
    "28": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। क्रिया समझी जाती है; गिनी गई वस्तु (सिराएँ) छपी नहीं। सन्धि जाँची: "
           "चतुर्विंशतिः + नासायाम् → चतुर्विंशतिर्नासायाम् (इ के बाद विसर्ग + घोष व्यंजन → र्); पंक्ति के अन्त में छपा ‘नासायां’ (ं)।"),
    "29": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। अधूरा वाक्य: ‘एकाम्’ द्वितीया है, क्रिया नहीं छपी, कोई जोड़ी नहीं गई। "
           "‘तासामेव’ = उन्हीं में से (सम्भवतः नाक की २४)। समूह-टिप्पणी: इकाई २८ को आगे बढ़ाती दिखती है। तालु = तालु (मानक)। "
           "सन्धि जाँची: तालुनि + एकाम् → तालुन्येकाम् (इ + भिन्न स्वर → य्); एकाम् + इति → एकामिति; तासाम् + एव → तासामेव; छपा "
           "गंध = गन्ध।"),
    "30": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। क्रिया समझी जाती है। सन्धि जाँची: षट्पञ्चाशत् + नेत्रयोः → "
           "षट्पञ्चाशन्नेत्रयोः (न से पहले त् → न्, डेटा के अनुसार नियमित); छपा पंच = पञ्च। नेत्रयोः सप्तमी द्विवचन।"),
    "31": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। अधूरा वाक्य, और छह का बँटवारा पक्का नहीं: डेटा उन्मेष-क्रिया के लिए दो, "
           "निमेष-क्रिया के लिए दो, अपाङ्गों में दो पढ़ता है; द्विवचन ‘क्रिये’ पहले ‘द्वे’ से भी जुड़ सकता है; इस पर कोई प्रश्न नहीं। "
           "अपाङ्ग = आँख का बाहरी कोना (मानक), इस परम्परा में मर्म का नाम भी (सम्भावित)। समूह-टिप्पणी: इकाई ३० को आगे बढ़ाती है। "
           "सन्धि जाँची: तयोः + उन्मेष → तयोरुन्मेष (ओ के बाद विसर्ग + स्वर → र्); च + अपाङ्गयोः → चापाङ्गयोः (अ + अ → आ); "
           "अपाङ्गयोः + इति → अपाङ्गयोरिति।"),
    "32": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। क्रिया समझी जाती है। ये साठ नाक की २४ और आँखों की ५६ से अलग हैं या नहीं, "
           "पंक्ति नहीं कहती; डेटा का जोड़ (इकाई ९ के १६४) इन्हें अतिरिक्त नहीं मानता, पर यह अनुमान है, इस पर कोई प्रश्न नहीं। "
           "समूह-टिप्पणी: इकाई ३१ को आगे बढ़ाती है। छपाई ‘नासानेत्रगतास्तुललाटे’ में तु और ललाटे बिना अन्तर के जुड़े। सन्धि जाँची: "
           "नासानेत्रगताः + तु → नासानेत्रगतास्तु (त से पहले विसर्ग → स्)।"),
    "33": ("गद्य; विश्वास मध्यम। पाठ-चिह्न (सम्भावित): छपा ‘केशांतनुगताः’; केशान्त + अनुगताः से ‘केशान्तानुगताः’ (दीर्घ आ) बनना चाहिए, "
           "या ‘केशान्तम् अनुगताः’ में म् लुप्त है; अर्थ वही; इस शब्द के रूप पर कोई प्रश्न नहीं। केशान्त = केश-रेखा (सम्भावित); आवर्त और "
           "स्थपनी मर्म-नाम (सम्भावित)। समूह-टिप्पणी: इकाई ३२ को आगे बढ़ाती है। सन्धि जाँची: चतस्रः + द्वे → चतस्रो द्वे (अः + घोष "
           "व्यंजन → ओ); द्वे आवर्तयोः अलग (ए पर समाप्त द्विवचन, सन्धि नहीं); आवर्तयोः + एका → आवर्तयोरेका; स्थपन्याम् + इति → "
           "स्थपन्यामिति।"),
    "34": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। छपा ‘एवच’ = एव + च (केवल अन्तर की भूल)। दूसरे-तीसरे वाक्यांश अधूरे; क्रिया "
           "समझी जाती है। ‘ते एव’ = वही दोनों (शब्दवाहिनी); डेटा जोड़ से (इकाई ९ के पचास) अनुमान करता है कि ये अतिरिक्त नहीं; यह छपा नहीं, "
           "इस पर कोई प्रश्न नहीं। शंख = कनपटी (मानक), शब्द का दूसरा अर्थ शंख। सन्धि जाँची: ते एव अलग (ए पर समाप्त द्विवचन के बाद "
           "स्वर-सन्धि नहीं); छपे शंख, संधि में ं = ङ्/न्।"),
    "35": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। छपा ‘मूर्द्धनि’ (-र्द्ध-) शब्द-सूची में मूर्धनि लिखा गया; केवल वर्तनी। क्रिया "
           "समझी जाती है। कोई सन्धि-परिवर्तन नहीं।"),
    "36": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। ‘एकैकाम्’ और ‘एकाम्’ द्वितीया, उनकी कोई क्रिया नहीं; कोई जोड़ी नहीं गई। "
           "२ + ? + १ = ८ तभी जब सीमन्त पाँच हों; पंक्ति संख्या नहीं देती, इस पर कोई प्रश्न नहीं। उत्क्षेप, सीमन्त, अधिपति मर्म-नाम "
           "(सम्भावित)। समूह-टिप्पणी: इकाई ३५ (सिर) को आगे बढ़ाती है। परिहरेत् = विधिलिङ् प्रथम पुरुष एकवचन। सन्धि जाँची: "
           "तासाम् + उत्क्षेपयोः → तासामुत्क्षेपयोः; उत्क्षेपयोः + द्वे → उत्क्षेपयोर्द्वे (ओ के बाद विसर्ग + घोष → र्); सीमन्तेषु + एकैकाम् → "
           "सीमन्तेष्वेकैकाम् (उ + भिन्न स्वर → व्); एक + एक → एकैक (अ + ए → ऐ); अधिपतौ + इति → अधिपताविति (औ + स्वर → आव्); "
           "इति + अष्टौ → इत्यष्टौ (इ + अ → य)।"),
    "37": ("गद्य; विश्वास निम्न। पाठ-चिह्न (सम्भावित): छपा ‘नतथा’; ‘न तथा’ आगे के निषेध ‘अशस्त्रकृत्याः’ से दोहरा निषेध बनाता, "
           "इसलिए ‘तथा’ (इसी प्रकार) अनुमानित पाठ है, न सम्भवतः अतिरिक्त रेखा; इस पर कोई प्रश्न नहीं। संज्ञा (सिराएँ) छपी नहीं। ग्रथित = "
           "ग्रन्थित का मान्य रूप। समूह-टिप्पणी: इकाई ३६ को आगे बढ़ाती है। सन्धि जाँची: संकीर्णाः + ग्रथिताः → संकीर्णा ग्रथिताः (आ के बाद "
           "विसर्ग घोष से पहले लुप्त); च + अशस्त्र → चाशस्त्र (अ + अ → आ)।"),
    "38": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। १७५ इकाई ४ के ७०० का चौथा भाग (डेटा की टिप्पणी)। ‘अनिलरक्तम्’ द्वन्द्व (वात "
           "और रक्त) पढ़ा गया; एक समास ‘वात-युक्त रक्त’ भी सम्भव, निर्णय नहीं; इस पर कोई प्रश्न नहीं। अनिल = वायु, यहाँ वात। वाक्य छपे "
           "से आगे नहीं बढ़ाया गया। सन्धि जाँची: पञ्चसप्तति + अधिकम् → पञ्चसप्तत्यधिकम् (इ + अ → य); शतकम् + अनिल → शतकमनिल; "
           "तुर्य + अंश → तुर्यांश (अ + अ → आ)।"),
}


# ===================================================================== AIDS
AIDS = {
    "27": {
        "diagram": {"groups": [
            {"label": "जीभ की सोलह (इकाई २६), उनके नीचे", "items": ["२ रसवेदिनी: स्वाद का बोध", "२ वाक्प्रवर्तिनी: वाणी को चलाती",
                                                                "ताश्चतस्रः: कुल चार"]}]},
        "chunks": "तासामधो | द्वे रसवेदिन्यौ | द्वेवाक्प्रवर्तिन्यौ | ताश्चतस्रः",
        "sandhi": ("अः + घोष व्यंजन → ओ: अधः + द्वे → अधो द्वे · च से पहले विसर्ग → श्: ताः + चतस्रः → ताश्चतस्रः · "
                   "स्वर से पहले म् जुड़ता है: तासाम् + अधः → तासामधः।"),
    },
    "28": {
        "frame": "कितनी: चतुर्विंशतिः (२४) → कहाँ: नासायाम् (नाक में) → क्रिया: ‘हैं’ समझी जाती है।",
        "sandhi": "इ के बाद विसर्ग + घोष व्यंजन → र्: चतुर्विंशतिः + नासायाम् → चतुर्विंशतिर्नासायाम्।",
        "anchors": "चतुर् + विंशति = ४ + २० = २४। (मेरी याद-पद्धति: ‘चार-बीस’ बोलकर याद करें)",
    },
    "29": {
        "diagram": {"groups": [
            {"label": "नाक की चौबीस में (तासाम्)", "items": ["२ गन्धवेदिनी: गन्ध का बोध", "उन्हीं में से १ तालु में",
                                                        "इति तिस्रः: कुल तीन"]}]},
        "chunks": "तासां | द्वे गंधवेदिन्यौ | तासामेव च | तालुन्येकामिति | तिस्रः",
        "sandhi": "इ + भिन्न स्वर → य्: तालुनि + एकाम् → तालुन्येकाम् · स्वर से पहले म् जुड़ता है: एकाम् + इति → एकामिति।",
    },
    "30": {
        "frame": "कितनी: षट्पञ्चाशत् (५६) → कहाँ: नेत्रयोः (दोनों आँखों में) → क्रिया: ‘हैं’ समझी जाती है।",
        "sandhi": "न से पहले त् → न्: षट्पञ्चाशत् + नेत्रयोः → षट्पञ्चाशन्नेत्रयोः (छपे अनुसार, नियमित)।",
        "anchors": "षट् + पञ्चाशत् = ६ + ५० = ५६; ‘-योः’ = दोनों में। (मेरी याद-पद्धति)",
    },
    "31": {
        "seesaw": "उन्मेष (आँख खोलना) ⇄ निमेष (आँख मूँदना): दोनों इसी पंक्ति में, एक ही समास में।",
        "chunks": "तयोरुन्मेषनिमेषक्रिये | द्वे द्वे | द्वे चापांगयोरिति | षट्",
        "frame": "किनमें: तयोः (दोनों नेत्रों में) → किस काम के लिए: उन्मेष-निमेष-क्रिये → और कहाँ: अपाङ्गयोः (आँख के बाहरी कोने) → कुल: षट्।",
        "sandhi": "ओ के बाद विसर्ग + स्वर → र्: तयोः + उन्मेष → तयोरुन्मेष · अ + अ → आ: च + अपाङ्गयोः → चापाङ्गयोः।",
    },
    "32": {
        "chunks": "नासानेत्रगतास्तुललाटे | षष्टिः",
        "frame": "कौन: नासानेत्रगताः (नाक और आँख तक जाने वाली) → कहाँ: ललाटे (माथे में) → कितनी: षष्टिः (६०)।",
        "sandhi": "त से पहले विसर्ग → स्: नासानेत्रगताः + तु → नासानेत्रगतास्तु।",
    },
    "33": {
        "diagram": {"groups": [
            {"label": "उनमें (तासाम्), इति सप्त", "items": ["४ केशान्त तक (सम्भवतः केश-रेखा)", "२ दोनों आवर्तों में (सम्भावित मर्म-नाम)",
                                                       "१ स्थपनी में (सम्भावित मर्म-नाम)", "कुल ७"]}]},
        "chunks": "तासां | केशांतनुगताश्चतस्रो | द्वे आवर्तयोरेका च | स्थपन्यामिति सप्त",
        "sandhi": ("ओ के बाद विसर्ग + स्वर → र्: आवर्तयोः + एका → आवर्तयोरेका · ए पर समाप्त द्विवचन के बाद सन्धि नहीं: द्वे आवर्तयोः · "
                   "स्वर से पहले म्: स्थपन्याम् + इति → स्थपन्यामिति।"),
    },
    "34": {
        "chain": {"steps": ["कर्णयोः: दोनों कानों में १६", "उनमें २ शब्दवाहिनी", "वही (ते एव) दोनों शंखों में भी",
                            "उनमें २ शंख-सन्धि तक"]},
        "chunks": "कर्णयोः षोडश | तासां शब्दवाहिन्यौ द्वे | ते एवच शंखयोः | तासां शंखसंधिगते द्वे",
        "sandhi": "ए पर समाप्त द्विवचन के बाद स्वर-सन्धि नहीं: ते एव (अलग रहते हैं)।",
    },
    "35": {
        "frame": "कितनी: द्वादश (१२) → कहाँ: मूर्धनि (सिर में) → क्रिया: ‘हैं’ समझी जाती है।",
        "chunks": "द्वादश | मूर्द्धनि",
        "anchors": "द्वा + दश = २ + १० = १२; षोडश (१६) भी इसी ढंग का है। (मेरी याद-पद्धति)",
    },
    "36": {
        "diagram": {"groups": [
            {"label": "सिर की बारह में (तासाम्), इत्यष्टौ", "items": ["दोनों उत्क्षेपों में २", "सीमन्तों में एक-एक", "अधिपति में १",
                                                               "कुल ८: शस्त्र से बचाएँ"]}]},
        "chunks": "तासामुत्क्षेपयोर्द्वे | सीमंतेष्वेकैकामेकामधिपतावित्यष्टौ | शस्त्रेण परिहरेत्",
        "sandhi": ("औ + स्वर → आव्: अधिपतौ + इति → अधिपताविति · उ + भिन्न स्वर → व्: सीमन्तेषु + एकैकाम् → सीमन्तेष्वेकैकाम् · "
                   "इ + अ → य: इति + अष्टौ → इत्यष्टौ।"),
    },
    "37": {
        "diagram": {"groups": [
            {"label": "शस्त्र-कर्म के योग्य नहीं (अशस्त्रकृत्याः)", "items": ["१ क्षुद्रिकाः: छोटी", "२ कुटिलाः: टेढ़ी",
                                                                       "३ संकीर्णा: मिली हुई", "४ ग्रथिताः: गुँथी हुई",
                                                                       "५ संधिषु: जोड़ों में"]}]},
        "chunks": "नतथा | क्षुद्रिकाः | कुटिलाः | संकीर्णा | ग्रथिताः | संधिषु | चाशस्त्रकृत्याः",
        "sandhi": "आ के बाद विसर्ग घोष से पहले लुप्त: संकीर्णाः + ग्रथिताः → संकीर्णा ग्रथिताः · अ + अ → आ: च + अशस्त्र → चाशस्त्र।",
    },
    "38": {
        "chain": {"steps": ["सब सिराएँ: ७०० (इकाई ४)", "तुर्यांश: चौथा भाग (डेटा की गणना)", "पञ्चसप्तत्यधिकं शतकम्: १७५",
                            "अनिलरक्त: वात और रक्त का वहन"]},
        "chunks": "तासां | यथास्वं | तुर्यांशविभागेन | पंचसप्तत्यधिकं | शतकमनिलरक्तं | वहति",
        "sandhi": "इ + अ → य: पञ्चसप्तति + अधिकम् → पञ्चसप्तत्यधिकम् · स्वर से पहले म्: शतकम् + अनिल → शतकमनिल।",
    },
}


# ============================================================== IMAGE_SPECS
IMAGE_SPECS = {
    ("27", "diagram"): {
        "file": "sh6-jihva-chatasrah-27.svg",
        "alt": ("Flowchart of unit 27: the tongue's sixteen (unit 26); below them two perceiving taste and two setting "
                "speech in motion; four in all."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"जिह्वा में १६ (इकाई २६)\"] --> B[\"उनके नीचे\"]\n"
                 "  B --> C[\"२ रसवेदिनी: स्वाद-बोध\"]\n"
                 "  B --> D[\"२ वाक्प्रवर्तिनी: वाणी\"]\n"
                 "  C --> E[\"ताश्चतस्रः: कुल ४\"]\n"
                 "  D --> E\n"),
    },
    ("29", "diagram"): {
        "file": "sh6-nasa-tisrah-29.svg",
        "alt": ("Flowchart of unit 29: the nose's twenty-four (unit 28); of them two perceiving smell and one in the "
                "palate; three in all."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"नासा में २४ (इकाई २८)\"] --> B[\"२ गन्धवेदिनी: गन्ध-बोध\"]\n"
                 "  A --> C[\"१ तालु में\"]\n"
                 "  B --> D[\"इति तिस्रः: कुल ३\"]\n"
                 "  C --> D\n"),
    },
    ("33", "diagram"): {
        "file": "sh6-lalata-sapta-33.svg",
        "alt": ("Table of unit 33: four going to the keśānta (probably the hair-line); two in the two āvartas (probable "
                "marma name); one in the sthapanī (probable marma name); seven in all."),
        "type": "table",
        "title": "इकाई ३३: इति सप्त",
        "heads": ["कहाँ", "संख्या"],
        "rows": [["केशान्त तक (सम्भवतः केश-रेखा)", "४"], ["दोनों आवर्त (सम्भावित मर्म-नाम)", "२"],
                 ["स्थपनी (सम्भावित मर्म-नाम)", "१"], ["कुल (इति सप्त)", "७"]],
    },
    ("34", "chain"): {
        "file": "sh6-karna-shankha-34.svg",
        "alt": ("Chain of unit 34 in line order: sixteen in the two ears; of them two carrying sound; those very two "
                "also in the two temples; of them two gone to the temple joint."),
        "type": "chain",
        "title": "इकाई ३४: कानों की सिराएँ",
        "steps": ["कर्णयोः: दोनों कानों में १६", "उनमें २ शब्दवाहिनी", "वही (ते एव) दोनों शंखों में भी",
                  "उनमें २ शंख-सन्धि तक"],
    },
    ("36", "diagram"): {
        "file": "sh6-murdha-ashtau-36.svg",
        "alt": ("Table of unit 36: two in the two utkṣepas; one each in the sīmantas; one in the adhipati (all probable "
                "marma names); eight in all, to be avoided with the knife."),
        "type": "table",
        "title": "इकाई ३६: इत्यष्टौ, शस्त्र से बचाएँ",
        "heads": ["कहाँ", "संख्या"],
        "rows": [["दोनों उत्क्षेप", "२"], ["सीमन्त", "एक-एक"], ["अधिपति", "१"],
                 ["कुल (इत्यष्टौ)", "८: शस्त्रेण परिहरेत्"]],
    },
    ("37", "diagram"): {
        "file": "sh6-ashastra-37.svg",
        "alt": ("Table of unit 37, numbered in line order: 1 small, 2 crooked, 3 intermingled, 4 knotted, 5 in the "
                "joints; all not to be done with the knife."),
        "type": "table",
        "title": "इकाई ३७: शस्त्र-कर्म के योग्य नहीं",
        "heads": ["छपा शब्द", "अर्थ"],
        "rows": [["१ क्षुद्रिकाः", "छोटी"], ["२ कुटिलाः", "टेढ़ी"], ["३ संकीर्णा", "मिली हुई"],
                 ["४ ग्रथिताः", "गुँथी हुई"], ["५ संधिषु", "जोड़ों में"]],
    },
    ("38", "chain"): {
        "file": "sh6-turyamsha-38.svg",
        "alt": ("Chain of unit 38: all sirās 700 (unit 4); a fourth part (data's arithmetic); a hundred plus "
                "seventy-five, 175; carries anila-rakta, Vāta and blood."),
        "type": "chain",
        "title": "इकाई ३८: चौथा भाग, १७५",
        "steps": ["सब सिराएँ: ७०० (इकाई ४)", "तुर्यांश: चौथा भाग (डेटा की गणना)", "पञ्चसप्तत्यधिकं शतकम्: १७५",
                  "अनिलरक्त: वात और रक्त का वहन"],
    },
}
