from helpers import mcq, match, order, fill, multi, accepts


AUTHORED = {}

# ---------------------------------------------------------------- unit 115
AUTHORED["115"] = {
    "title": "दशनास्तु रुचकाः",
    "question": "By unit 115, to which class of bone do the teeth belong?",
    "rule": ("The teeth (दशनाः), however (तु), are rucakas (रुचकाः): the second named class of bone, after the kapālas "
             "of unit 114."),
    "limits": ("Prose, two words; the copula is understood. रुचक is a class name and is kept untranslated; the unit does "
               "not explain it. The number of the teeth is not given here."),
    "explain_hi": ("यह दो शब्दों की गद्य-पंक्ति है: दाँत तो रुचक हैं। "
                   "इकाई ११४ में कपाल नाम की अस्थियाँ बताई गईं; यहाँ ‘तु’ (तो) से दूसरा वर्ग आरम्भ होता है। "
                   "‘रुचक’ अस्थियों के पाँच वर्गों में से एक का नाम है; डेटा इसका अनुवाद नहीं करता और इसकी कोई व्याख्या नहीं देता। "
                   "‘है’ क्रिया छपी नहीं, समझी जाती है। "
                   "‘दशनास्तु’ में दशनाः का विसर्ग त से पहले स् बना है।"),
    "hook": "दाँत: रुचक वर्ग।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 115, to which class of bone do the teeth belong?",
            ("Rucaka", "दशनास्तु रुचकाः: the teeth are rucakas."),
            [("Kapāla", "Kapāla is the class of unit 114 (knees, hips, head ...), not the teeth."),
             ("Nalaka", "Nalaka is the class of the remaining bones (unit 117)."),
             ("Valaya", "Valaya is the class of hands, feet, sides and back (unit 116).")],
            "The teeth, however, are rucakas.",
            "दशनास्तु रुचकाः."),
        match(1, "Match each part of unit 115 to its meaning.",
              [["दशनाः", "teeth"], ["तु", "but, however"], ["रुचकाः", "rucakas, a class of bone"],
               ["दशनास्तु", "the teeth, however"]],
              "दशनाः + तु = दशनास्तु; रुचकाः names their class.",
              "दशनाः, तु, रुचकाः, दशनास्तु."),
        mcq("extend", 2, "In this passage, what is रुचक?",
            ("The name of one class of bone", "The data reads rucaka as one of the classes of bone and keeps it untranslated."),
            [("The name of a disease of the teeth", "No disease is named; rucaka is a class of bone."),
             ("The name of the sockets of the teeth", "The sockets are not named here; rucaka is a class of bone."),
             ("The name of a joint of the jaw", "No joint is named here; rucaka is a class of bone.")],
            "रुचक = a class of bone; the teeth belong to it.",
            "दशनाः रुचकाः: the teeth are of the rucaka class.",
            teaches="रुचक is one of the five classes of bone (unit 118); the data keeps the name untranslated."),
        mcq("discriminate", 3, "Which split of दशनास्तु in unit 115 is right?",
            ("दशनाः + तु", "आः before त: the visarga becomes स्, giving दशनास्तु."),
            [("दशनाः + अस्तु", "आः before a vowel drops its visarga with no join: दशना अस्तु."),
             ("दशनात् + तु", "त् + त would give दशनात्तु, not दशनास्तु."),
             ("दशना + स्तु", "स्तु is not a word here; the स् comes from the visarga.")],
            "दशनाः (teeth) + तु (however): visarga before त → स्.",
            "Visarga before त → स्."),
        multi("apply", 4, "Which statements fit unit 115?",
              [("The teeth are named rucakas", "Right: दशनास्तु रुचकाः."),
               ("Unit 115 gives the number of the teeth", "No number is printed in unit 115."),
               ("No verb is printed; 'are' is understood", "Right: the copula is understood (data note)."),
               ("The data translates रुचक as 'tube'", "Rucaka is kept untranslated; 'tube' is nalaka (unit 117).")],
              [0, 2],
              "The teeth are rucakas; the copula is understood; rucaka is kept untranslated.",
              "दशनास्तु रुचकाः."),
        mcq("transfer", 5, "By the rule of दशनास्तु, how is वृक्षाः + तु (the trees, however) joined in a new example?",
            ("वृक्षास्तु", "Visarga before त becomes स्, as दशनाः + तु → दशनास्तु."),
            [("वृक्षा तु", "The visarga after आ drops before a voiced sound; त is not voiced."),
             ("वृक्षो तु", "ओ comes from अः before a voiced consonant, not from आः."),
             ("वृक्षाश्तु", "श् comes before च/छ/श, not before त.")],
            "वृक्षाः + तु = वृक्षास्तु, like दशनाः + तु = दशनास्तु.",
            "Visarga + त → स्त.",
            teaches="A visarga before त becomes स्: दशनाः + तु → दशनास्तु."),
    ],
}

# ---------------------------------------------------------------- unit 116
AUTHORED["116"] = {
    "title": "तरुणानि · वलयानि",
    "question": "By unit 116, where are the taruṇa bones and where are the valaya bones?",
    "rule": ("In the nose, ears, neck and eye-sockets (अक्षिकोष, probable) are the taruṇas ('tender ones', usually taken as "
             "cartilage, probable); in the hands, feet, sides and back are the valayas ('rings')."),
    "limits": ("Two printed lines, prose; the copula is understood. Cartilage for taruṇa and eye-socket for akṣikoṣa are "
               "probable, not certain. Valaya is named after its shape; no more is explained. No number is given."),
    "explain_hi": ("इस इकाई में दो छपी पंक्तियाँ हैं, और दोनों में अस्थियों का एक-एक वर्ग है। "
                   "नाक (घ्राण), कान (कर्ण), गर्दन (ग्रीवा) और आँख के कोष (अक्षिकोष, सम्भवतः आँख का गड्ढा) में ‘तरुण’ यानी कोमल अस्थियाँ हैं; "
                   "इन्हें सामान्यतः उपास्थि (कार्टिलेज) माना जाता है, जो सम्भावित पहचान है। "
                   "हाथ (पाणि), पैर (पाद), बगल (पार्श्व) और पीठ (पृष्ठ) में ‘वलय’ यानी छल्ले हैं; यह नाम आकार से है। "
                   "दोनों स्थान-सूचियाँ द्वन्द्व समास हैं, सप्तमी बहुवचन (-एषु) में।"),
    "hook": "नाक-कान-गर्दन-आँख में कोमल तरुण; हाथ-पैर-बगल-पीठ में छल्ले जैसे वलय।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 116, which class of bone is in the hands, feet, sides and back?",
            ("Valaya (rings)", "पाणिपादपार्श्वपृष्ठेषु वलयानि: in hands, feet, sides and back are the valayas."),
            [("Taruṇa (tender)", "Taruṇas are in the nose, ears, neck and eye-sockets."),
             ("Rucaka (teeth)", "Rucaka is the class of the teeth (unit 115)."),
             ("Nalaka (tubes)", "Nalaka is the class of the remaining bones (unit 117).")],
            "In the hands, feet, sides and back are the valayas.",
            "पाणिपादपार्श्वपृष्ठेषु वलयानि."),
        order(1, "Put the places of the taruṇas in the order of unit 116.",
              ["घ्राण", "कर्ण", "ग्रीवा", "अक्षिकोष"],
              "Nose, ear, neck, eye-socket: the taruṇas.",
              "घ्राण → कर्ण → ग्रीवा → अक्षिकोष."),
        match(2, "Match each place word of unit 116 to its meaning.",
              [["घ्राण", "nose"], ["कर्ण", "ear"], ["ग्रीवा", "neck"], ["पाणि", "hand"], ["पाद", "foot"],
               ["पृष्ठ", "back"]],
              "Nose, ear, neck (taruṇa); hand, foot, back (valaya).",
              "घ्राण, कर्ण, ग्रीवा; पाणि, पाद, पृष्ठ.", role="extend",
              teaches="Each line lists its places as one dvandva compound in the locative plural, then names the class."),
        mcq("discriminate", 3, "By unit 116, which place has valayas, not taruṇas?",
            ("The sides (पार्श्व)", "पार्श्व is in the valaya line."),
            [("The ears (कर्ण)", "The ears are in the taruṇa line."),
             ("The neck (ग्रीवा)", "The neck is in the taruṇa line."),
             ("The nose (घ्राण)", "The nose is in the taruṇa line.")],
            "Sides go with the valayas; nose, ears and neck with the taruṇas.",
            "घ्राणकर्णग्रीवाऽक्षिकोषेषु तरुणानि; पाणिपादपार्श्वपृष्ठेषु वलयानि."),
        multi("apply", 4, "Which places have taruṇas by unit 116?",
              [("The hands", "The hands have valayas."),
               ("The ears", "Right: कर्ण is in the taruṇa line."),
               ("The back", "The back has valayas."),
               ("The eye-sockets", "Right: अक्षिकोष (eye-socket, probable) is in the taruṇa line.")],
              [1, 3],
              "Taruṇas: nose, ears, neck, eye-sockets.",
              "घ्राणकर्णग्रीवाऽक्षिकोषेषु तरुणानि."),
        mcq("transfer", 5, "By the pattern of -कोषेषु (in the sockets), how is वृक्ष (tree) put in the locative plural in a new example?",
            ("वृक्षेषु", "An अ-stem takes -एषु in the locative plural, as कोष → कोषेषु."),
            [("वृक्षाणि", "वृक्षाणि is a nominative/accusative plural form, not locative."),
             ("वृक्षैः", "वृक्षैः is the instrumental plural (by the trees)."),
             ("वृक्षे", "वृक्षे is singular: in the tree.")],
            "वृक्षेषु = in the trees, like कोषेषु = in the sockets.",
            "अ-stem, locative plural: -एषु.",
            teaches="-एषु marks the locative plural of अ-stems: कोष → कोषेषु, पृष्ठ → पृष्ठेषु."),
    ],
}

# ---------------------------------------------------------------- unit 117
AUTHORED["117"] = {
    "title": "शेषाणि नलकानीति",
    "question": "By unit 117, what are the remaining bones called?",
    "rule": ("The remaining (शेषाणि) bones are nalakas (नलकानि, 'tubes'); इति closes the classification of the bones."),
    "limits": ("Prose; the copula is understood. 'Tubular bones' is the usual reading of nalaka (probable). The unit does "
               "not list which bones are 'remaining'. इति is not translated."),
    "explain_hi": ("यह गद्य-पंक्ति अस्थि-वर्गों की सूची पूरी करती है: बची हुई अस्थियाँ ‘नलक’ यानी नलियाँ हैं। "
                   "नलक का अर्थ छोटी नली या सरकंडा है; इसे नली जैसी अस्थियों का वर्ग पढ़ना सामान्य, पर सम्भावित, अर्थ है। "
                   "कौन-सी अस्थियाँ ‘शेष’ हैं, यह यहाँ नहीं गिनाया गया। "
                   "अन्त का ‘इति’ वर्गीकरण की समाप्ति दिखाता है; अनुवाद में इसे नहीं लिया गया। "
                   "‘नलकानीति’ = नलकानि + इति, इ + इ मिलकर ई।"),
    "hook": "बाकी सब: नलक, नलियाँ।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 117, what are the remaining bones called?",
            ("Nalaka (tubes)", "शेषाणि नलकानि: the remaining ones are nalakas."),
            [("Kapāla (plates)", "Kapāla is the class of unit 114."),
             ("Valaya (rings)", "Valaya is the class of unit 116."),
             ("Rucaka (teeth)", "Rucaka is the class of the teeth (unit 115).")],
            "The remaining ones are nalakas.",
            "शेषाणि नलकानीति."),
        match(1, "Match each word of unit 117 to its meaning.",
              [["शेषाणि", "the remaining"], ["नलकानि", "tubes"], ["इति", "thus (closing)"]],
              "The remaining ones are tubes; thus (the list ends).",
              "शेषाणि, नलकानि, इति."),
        fill(2, "By unit 117 the remaining bones are ____ (tubes). Type it in Devanagari or in English letters (e.g. dharma).",
             accepts("नलकानि", None, "नलक", "tubes"),
             "नलकानि (tubes): शेषाणि नलकानीति.",
             "नलक = a small tube, reed: the last class of bone.",
             "शेषाणि नलकानि."),
        mcq("discriminate", 3, "Which split of नलकानीति in unit 117 is right?",
            ("नलकानि + इति", "इ + इ → ई: नलकानि + इति → नलकानीति."),
            [("नलकाः + इति", "आः before a vowel would give नलका इति, with no join."),
             ("नलकानि + एति", "इ + ए would give य: नलकान्येति."),
             ("नलकाने + इति", "ए before इ becomes अय् (or अ), not ई.")],
            "नलकानि (tubes) + इति (thus): इ + इ → ई.",
            "इ + इ → ई."),
        mcq("apply", 4, "What does इति do at the end of unit 117?",
            ("It closes the list of classes", "Data note: the closing iti marks the end of the classification."),
            [("It names one more class of bone", "No further class is named; nalaka is the last."),
             ("It gives the number of the nalakas", "No number is printed in unit 117."),
             ("It means 'the remaining' bones", "'The remaining' is शेषाणि, not इति.")],
            "इति marks the end of the classification and is not translated.",
            "...नलकानि + इति: the list ends."),
        mcq("transfer", 5, "By the rule of नलकानीति, how is अस्ति + इति joined in a new example?",
            ("अस्तीति", "इ + इ → ई, as नलकानि + इति → नलकानीति."),
            [("अस्तेति", "ए comes from अ + इ, not from इ + इ."),
             ("अस्त्यिति", "य् comes from इ before a different vowel, not before इ."),
             ("अस्तयिति", "अय् comes from ए before a vowel; there is no ए here.")],
            "अस्ति + इति = अस्तीति, like नलकानि + इति = नलकानीति.",
            "इ + इ → ई.",
            teaches="Two like vowels merge into the long one: इ + इ → ई (नलकानि + इति → नलकानीति)."),
    ],
}

# ---------------------------------------------------------------- unit 118
AUTHORED["118"] = {
    "title": "पंच विधान्यस्थीनि · तेषु हि ... मांसानि",
    "question": "By unit 118, how many kinds of bone are there, and what is bound in them?",
    "rule": ("The bones are of five kinds (पञ्च विधानि), each following its name; for in them the fleshes (मांसानि) are "
             "bound (निबद्धानि) by vessels (सिरा) and snāyus (ligaments, sinews)."),
    "limits": ("Two printed lines, prose. The first word नामानुगतामूनीनि is not a word as printed; 'following their names' "
               "rests on a conjectural reading: no question on it. The five classes are inferred from units 114-117, not "
               "named here. मांसानि may be masses of flesh, perhaps muscles: kept as 'fleshes'."),
    "explain_hi": ("पहली पंक्ति कहती है कि अस्थियाँ पाँच प्रकार की हैं। "
                   "छपा पहला शब्द ‘नामानुगतामूनीनि’ ठीक शब्द नहीं है; ‘नामानुगतान्यमूनि’ (ये, नाम के अनुसार) अनुमानित पाठ है, यानी हर वर्ग का स्वभाव उसके नाम से मेल खाता है। "
                   "पाँचों वर्ग इकाई ११४-११७ से लिए गए हैं: कपाल, रुचक, तरुण, वलय, नलक; यहाँ उनके नाम छपे नहीं। "
                   "दूसरी पंक्ति कहती है: क्योंकि उनमें (अस्थियों में) सिराओं और स्नायुओं से मांस बँधे हुए हैं। "
                   "सिरा = शिरा या रक्तवाहिनी, स्नायु = स्नायुबन्ध (दोनों मानक); ‘मांसानि’ मांस-पिण्ड हैं, सम्भवतः पेशियाँ।"),
    "hook": "पाँच वर्ग की अस्थियाँ; उन पर सिरा-स्नायु से बँधा मांस।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 118, of how many kinds are the bones?",
            ("Five", "पंच विधान्यस्थीनि: bones of five kinds."),
            [("Three", "पञ्च is five, not three."),
             ("Seven", "पञ्च is five, not seven."),
             ("Eight", "पञ्च is five, not eight.")],
            "The bones are of five kinds.",
            "पंच विधान्यस्थीनि."),
        order(1, "Put the five bone classes in the order units 114-117 give them (the data's list for unit 118).",
              ["कपाल", "रुचक", "तरुण", "वलय", "नलक"],
              "Kapāla (114), rucaka (115), taruṇa and valaya (116), nalaka (117).",
              "कपाल → रुचक → तरुण → वलय → नलक."),
        match(2, "Match each word of the second line of unit 118 to its meaning.",
              [["तेषु", "in them"], ["सिराभिः", "by vessels (sirā)"], ["स्नायुभिः", "by snāyus (ligaments, sinews)"],
               ["निबद्धानि", "bound"], ["मांसानि", "fleshes, masses of flesh"]],
              "In them, the fleshes are bound by vessels and snāyus.",
              "तेषु हि सिराभिः स्नायुभिश्च निबद्धानि मांसानि.", role="extend",
              teaches="तेषु (in them) refers to the bones; the instrumentals सिराभिः, स्नायुभिः say by what the flesh is bound."),
        mcq("discriminate", 3, "Which split of विधान्यस्थीनि in unit 118 is right?",
            ("विधानि + अस्थीनि", "इ before a different vowel becomes य्: विधानि + अस्थीनि → विधान्यस्थीनि."),
            [("विधाने + अस्थीनि", "ए + अ would give विधानेऽस्थीनि, with ए kept."),
             ("विधान् + यस्थीनि", "यस्थीनि is not a word; the word is अस्थीनि (bones)."),
             ("विधाः + अस्थीनि", "आः before a vowel would give विधा अस्थीनि, with no join.")],
            "विधानि (kinds) + अस्थीनि (bones): इ + अ → य.",
            "इ + a different vowel → य् + that vowel."),
        mcq("apply", 4, "By unit 118, by what are the fleshes bound in the bones?",
            ("By vessels and snāyus", "सिराभिः स्नायुभिश्च निबद्धानि: bound by sirās and snāyus."),
            [("By marrow and fat", "Marrow and fat are not named in unit 118."),
             ("By skin and nails", "Skin and nails are not named in unit 118."),
             ("By hair and blood", "Hair and blood are not named in unit 118.")],
            "In the bones the fleshes are bound by vessels (sirā) and snāyus (ligaments).",
            "तेषु हि सिराभिः स्नायुभिश्च निबद्धानि मांसानि."),
        mcq("transfer", 5, "By the rule of विधान्यस्थीनि, how is फलानि + अत्र (the fruits here) joined in a new example?",
            ("फलान्यत्र", "इ before a different vowel becomes य्, as विधानि + अस्थीनि → विधान्यस्थीनि."),
            [("फलानेत्र", "ए comes from अ + इ, not from इ + अ."),
             ("फलानीत्र", "ई comes from इ + इ; here इ meets अ."),
             ("फलानत्र", "The इ does not simply drop; it becomes य्.")],
            "फलानि + अत्र = फलान्यत्र, like विधानि + अस्थीनि = विधान्यस्थीनि.",
            "इ + अ → य.",
            teaches="इ before a different vowel becomes य्: विधानि + अस्थीनि → विधान्यस्थीनि."),
    ],
}

# ---------------------------------------------------------------- unit 119
AUTHORED["119"] = {
    "title": "दशोत्तरं शतद्वयमस्थिसंधीनां",
    "question": "By unit 119, how many joints of bones (asthi-sandhi) are there?",
    "rule": ("Of the joints of bones (अस्थिसन्धीनाम्): two hundred, in excess by ten (दशोत्तरं शतद्वयम्), that is 210."),
    "limits": ("Prose; no verb, and 'number' is not in the Sanskrit (the genitive gives 'of the joints'). The count is as "
               "printed. The split of 210 follows in units 120-122 (grouping note); its printed parts make 207 (see unit 122)."),
    "explain_hi": ("यह गद्य-पंक्ति अस्थि-सन्धियों, यानी हड्डियों के जोड़ों, की गिनती देती है। "
                   "‘शतद्वयम्’ = दो सौ, और ‘दशोत्तरम्’ = दस अधिक; मिलाकर दो सौ दस। "
                   "‘अस्थिसन्धीनाम्’ षष्ठी बहुवचन है: अस्थि-सन्धियों का (यह संख्या)। क्रिया छपी नहीं। "
                   "आगे की इकाइयाँ (१२०-१२२) इन्हें शाखाओं, धड़ और ऊपर के भाग में बाँटती हैं। "
                   "सन्धि: दश + उत्तरम् में अ + उ मिलकर ओ बना।"),
    "hook": "दो सौ और दस: २१० अस्थि-सन्धियाँ।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 119, the number given is of what?",
            ("The joints of bones", "अस्थिसंधीनाम्: of the joints of bones (asthi-sandhi)."),
            [("The bones themselves", "Unit 119 counts the joints of bones, not the bones."),
             ("The vessels of flesh", "Vessels are not counted in unit 119."),
             ("The snāyus of limbs", "Snāyus are not counted in unit 119.")],
            "Unit 119 gives the number of the joints of bones.",
            "...अस्थिसंधीनाम्: of the joints of bones."),
        order(1, "Put the words of unit 119 in the line's order.",
              ["दशोत्तरं", "शतद्वयम्", "अस्थिसंधीनां"],
              "Ten in excess, two hundred, of the joints of bones.",
              "दशोत्तरं → शतद्वयम् → अस्थिसंधीनां."),
        match(2, "Match each word part of unit 119 to its meaning.",
              [["दश", "ten"], ["उत्तर", "in excess"], ["शत", "hundred"], ["द्वय", "a pair, two"], ["अस्थि", "bone"],
               ["सन्धि", "joint"]],
              "दश-उत्तरं शत-द्वयम् = two hundred plus ten; अस्थि-सन्धि = joint of bones.",
              "दश, उत्तर, शत, द्वय, अस्थि, सन्धि.", role="extend",
              teaches="X-उत्तरम् = 'in excess by X': दशोत्तरं शतद्वयम् = 200 + 10."),
        mcq("discriminate", 3, "Which split of दशोत्तरं in unit 119 is right?",
            ("दश + उत्तरम्", "अ + उ → ओ: दश + उत्तरम् → दशोत्तरम्."),
            [("दशः + उत्तरम्", "अः before a vowel other than अ would give दश उत्तरम्, with no join."),
             ("दश + ओत्तरम्", "ओत्तरम् is not a word; and अ + ओ would give औ."),
             ("दशे + उत्तरम्", "ए before उ would not give ओ.")],
            "दश (ten) + उत्तरम् (in excess): अ + उ → ओ.",
            "अ + उ → ओ."),
        mcq("apply", 4, "What total does दशोत्तरं शतद्वयम् give?",
            ("210", "शतद्वयम् = 200; दशोत्तरम् = ten in excess: 210."),
            [("190", "उत्तर adds ten; it does not take ten away."),
             ("2,000", "The words are added, not multiplied."),
             ("120", "शतद्वय is two hundreds, not one.")],
            "Two hundred plus ten = 210.",
            "दशोत्तरं शतद्वयम् = 200 + 10 = 210."),
        mcq("transfer", 5, "By the pattern of दशोत्तरं शतद्वयम्, what does पञ्चोत्तरं शतम् mean in a new example?",
            ("105", "शतम् = 100; पञ्चोत्तरम् = five in excess: 105."),
            [("500", "उत्तर adds; it does not multiply."),
             ("95", "उत्तर means in excess, not less."),
             ("150", "पञ्च is five, not fifty.")],
            "पञ्चोत्तरं शतम् = 100 + 5 = 105, as दशोत्तरं शतद्वयम् = 200 + 10.",
            "X-उत्तरम् + number = that number plus X.",
            teaches="X-उत्तरम् with a number means 'that number plus X': दशोत्तरं शतद्वयम् = 210."),
    ],
}

# ---------------------------------------------------------------- unit 120
AUTHORED["120"] = {
    "title": "तेषामष्टषष्टिःशाखासु",
    "question": "By unit 120, how many of the joints are in the limbs (śākhā)?",
    "rule": ("Of them (तेषाम्, the 210 of unit 119), sixty-eight (अष्टषष्टिः) are in the limbs (शाखासु: arms and legs)."),
    "limits": ("Prose; no verb, and the counted noun is not printed (probably the bone-joints, from unit 119). Units "
               "120-122 appear to form one statement with unit 119 (grouping note)."),
    "explain_hi": ("यह गद्य-पंक्ति इकाई ११९ के २१० में से पहला भाग बताती है: उनमें से अड़सठ शाखाओं में। "
                   "शाखा का अर्थ यहाँ हाथ-पैर, यानी भुजाएँ और टाँगें (मानक) है। "
                   "‘तेषाम्’ (उनमें से) उन २१० की ओर संकेत करता है; गिनी गई वस्तु छपी नहीं, इकाई ११९ से सम्भवतः अस्थि-सन्धियाँ हैं। "
                   "इकाई १२०-१२२ मिलकर इकाई ११९ का बँटवारा करती दिखती हैं। "
                   "छपे ‘षष्टिःशा’ में श से पहले विसर्ग रखा गया है, जो नियमित है।"),
    "hook": "२१० में से ६८ हाथ-पैरों में।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 120, how many are in the limbs (śākhā)?",
            ("Sixty-eight", "अष्टषष्टिः शाखासु: sixty-eight in the limbs."),
            [("Fifty-nine", "Fifty-nine is the trunk's number (unit 121)."),
             ("Eighty-six", "अष्टषष्टि is sixty-eight, not eighty-six."),
             ("Forty-eight", "षष्टि is sixty, so अष्टषष्टि is sixty-eight.")],
            "Of them, sixty-eight are in the limbs.",
            "तेषामष्टषष्टिः शाखासु."),
        match(1, "Match each word part of unit 120 to its meaning.",
              [["तेषाम्", "of them"], ["अष्ट", "eight"], ["षष्टि", "sixty"], ["शाखा", "limb"]],
              "Of them, eight-and-sixty in the limbs.",
              "तेषाम्, अष्ट, षष्टि, शाखा."),
        mcq("extend", 2, "In unit 120, what does तेषाम् (of them) point back to?",
            ("The 210 joints of unit 119", "Data note: teṣām = of those 210 (asthi-sandhi)."),
            [("The five bone classes of unit 118", "The classes are not counted; तेषाम् takes up the 210."),
             ("The teeth of the earlier unit 115", "The teeth are not the 210; तेषाम् takes up unit 119."),
             ("The fleshes bound in unit 118", "The fleshes are not counted; तेषाम् takes up unit 119.")],
            "तेषाम् = of those 210 joints of bones.",
            "तेषाम् (gen. pl.) = of them: a part of a whole.",
            teaches="A genitive like तेषाम् can mark the whole of which a part is counted: 'of them, sixty-eight'."),
        mcq("discriminate", 3, "Which split of तेषामष्टषष्टिः in unit 120 is right?",
            ("तेषाम् + अष्टषष्टिः", "म् before a vowel stays म्: तेषाम् + अष्ट... → तेषामष्ट...."),
            [("तेषा + मष्टषष्टिः", "मष्टषष्टि is not a word; the म् ends तेषाम्."),
             ("तेषु + अष्टषष्टिः", "उ + अ would give व्: तेष्वष्टषष्टिः."),
             ("तेषाः + अष्टषष्टिः", "तेषाः is not a form; the word is तेषाम् (of them).")],
            "तेषाम् (of them) + अष्टषष्टिः (sixty-eight).",
            "Final म् before a vowel stays म् and joins it."),
        multi("apply", 4, "Which statements fit unit 120?",
              [("The counted noun is printed in the line", "It is not printed; probably the bone-joints, from unit 119."),
               ("The line has a verb of its own", "No verb is printed; the line is elliptical."),
               ("Sixty-eight are in the limbs", "Right: अष्टषष्टिः शाखासु."),
               ("शाखा here means the limbs, arms and legs", "Right: śākhā = the limbs (standard).")],
              [2, 3],
              "Sixty-eight in the limbs (arms and legs); no verb and no counted noun are printed.",
              "तेषामष्टषष्टिः शाखासु."),
        mcq("transfer", 5, "By the pattern of शाखा → शाखासु (in the limbs), how is लता (creeper) put in the locative plural?",
            ("लतासु", "A feminine आ-stem takes -आसु in the locative plural, as शाखा → शाखासु."),
            [("लतेषु", "-एषु is the locative plural of अ-stems (वृक्षेषु), not of feminine आ-stems."),
             ("लतायाम्", "लतायाम् is singular: in the creeper."),
             ("लताभिः", "लताभिः is the instrumental plural: by the creepers.")],
            "लतासु = in the creepers, like शाखासु = in the limbs.",
            "Feminine आ-stem, locative plural: -आसु.",
            teaches="Feminine आ-stems take -आसु in the locative plural: शाखा → शाखासु."),
    ],
}

# ---------------------------------------------------------------- unit 121
AUTHORED["121"] = {
    "title": "एकोनषष्टिरंतराधौ",
    "question": "By unit 121, how many are in the trunk (antarādhi)?",
    "rule": ("Fifty-nine (एकोनषष्टिः, 'sixty less one') are in the trunk (अन्तराधौ), the middle part of the body."),
    "limits": ("Prose; no verb and no counted noun (probably the bone-joints, as in unit 120). Which places make up the "
               "59 is not said in this unit."),
    "explain_hi": ("यह गद्य-पंक्ति इकाई ११९ के २१० का दूसरा भाग देती है: उनसठ अन्तराधि में। "
                   "अन्तराधि यानी धड़, शरीर का बीच का भाग (मानक)। "
                   "‘एकोनषष्टि’ = एक + ऊन + षष्टि: साठ में एक कम, यानी उनसठ। "
                   "गिनी गई वस्तु छपी नहीं; इकाई १२० की तरह सम्भवतः अस्थि-सन्धियाँ। "
                   "सन्धि: एकोनषष्टिः + अन्तराधौ में इ के बाद का विसर्ग स्वर से पहले र् बना।"),
    "hook": "साठ में एक कम: ५९ धड़ में।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 121, how many are in the trunk (antarādhi)?",
            ("Fifty-nine", "एकोनषष्टिः अन्तराधौ: fifty-nine in the trunk."),
            [("Sixty-one", "ऊन means less, so it is sixty less one."),
             ("Sixty-eight", "Sixty-eight is the limbs' number (unit 120)."),
             ("Sixty", "एकोन takes one away from sixty.")],
            "Fifty-nine in the trunk.",
            "एकोनषष्टिः अन्तराधौ."),
        match(1, "Match each word part of unit 121 to its meaning.",
              [["एक", "one"], ["ऊन", "less, lacking"], ["षष्टि", "sixty"], ["अन्तराधि", "trunk"]],
              "एक-ऊन-षष्टि = sixty less one; अन्तराधौ = in the trunk.",
              "एक, ऊन, षष्टि, अन्तराधि."),
        mcq("extend", 2, "How is the number एकोनषष्टि built?",
            ("Sixty less one", "एक + ऊन + षष्टि: sixty lacking one = fifty-nine."),
            [("Sixty and one more", "ऊन means lacking; it takes one away."),
             ("Sixty times one", "Nothing in एकोन multiplies."),
             ("One less than six", "षष्टि is sixty, not six.")],
            "एकोनषष्टि = sixty less one = 59.",
            "एकोन- before a number = that number less one.",
            teaches="एक + ऊन (less) before a tens number makes it one less: एकोनषष्टि = 59."),
        mcq("discriminate", 3, "Which split of एकोनषष्टिरंतराधौ in unit 121 is right?",
            ("एकोनषष्टिः + अन्तराधौ", "After इ, a visarga before a vowel becomes र्."),
            [("एकोनषष्टि + रन्तराधौ", "रन्तराधौ is not a word; the र् comes from the visarga."),
             ("एकोनषष्टिम् + अन्तराधौ", "म् before a vowel would give एकोनषष्टिमन्तराधौ."),
             ("एकोनषष्टे + अन्तराधौ", "ए before अ would give एकोनषष्टेऽन्तराधौ.")],
            "एकोनषष्टिः (fifty-nine) + अन्तराधौ (in the trunk): इः + vowel → इर्.",
            "A visarga after इ → र् before a vowel."),
        fill(4, "In unit 121 'in the trunk' is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("अन्तराधौ", None, "antaradhau"),
             "अन्तराधौ = in the trunk, the locative singular of अन्तराधि.",
             "अन्तराधौ = in the trunk.",
             "एकोनषष्टिः अन्तराधौ.", role="apply"),
        mcq("transfer", 5, "By the pattern of एकोनषष्टि, what does एकोनविंशति mean in a new example?",
            ("Nineteen", "एक + ऊन + विंशति: twenty less one."),
            [("Twenty-one", "ऊन takes one away; it does not add."),
             ("Eleven", "विंशति is twenty, not ten."),
             ("Twenty", "एकोन takes one away from twenty.")],
            "एकोनविंशति = 19, as एकोनषष्टि = 59.",
            "एकोन- + number = that number less one.",
            teaches="एकोन- before a number takes one away: एकोनषष्टि = 59, एकोनविंशति = 19."),
    ],
}

# ---------------------------------------------------------------- unit 122
AUTHORED["122"] = {
    "title": "अशीति रूर्ध्वं",
    "question": "By unit 122, what number is printed for the part above (ūrdhvam), and why does the data flag it?",
    "rule": ("Eighty (अशीतिः) above (ऊर्ध्वम्), as printed. The print divides 'अशीतिरूर्ध्वं' as अशीति रूर्ध्वं; "
             "the र् belongs to अशीतिर्. The printed parts 68 + 59 + 80 make 207, not the 210 of unit 119."),
    "limits": ("Prose; no verb, no counted noun. The data flags अशीति: the sites of units 129-134 add up to 83, and "
               "त्र्यशीतिः (eighty-three) is a possible reading; the translation keeps 'eighty'. No question asks which "
               "number is right. ऊर्ध्वम् is probably the region above the trunk (neck and head, probable)."),
    "explain_hi": ("यह गद्य-पंक्ति २१० का तीसरा भाग देती है: अस्सी ऊपर। "
                   "‘ऊर्ध्वम्’ यानी ऊपर; सम्भवतः धड़ के ऊपर का भाग, गर्दन और सिर (सम्भावित); पाठ इससे अधिक नहीं कहता। "
                   "छपे अनुसार ६८ + ५९ + ८० = २०७ होते हैं, इकाई ११९ के २१० नहीं। "
                   "इकाई १२९-१३४ के स्थान जोड़ने पर ८३ आते हैं, इसलिए ‘त्र्यशीतिः’ (तिरासी) सम्भावित पाठ बताया गया है; अनुवाद छपा ‘अस्सी’ ही रखता है। "
                   "छपाई ‘अशीति रूर्ध्वं’ में अशीतिर् का र् अगले शब्द से जुड़ा दिखता है; यह नियमित सन्धि है।"),
    "hook": "ऊपर अस्सी, पर जोड़ २०७: पाठ पर प्रश्नचिह्न।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 122, what does ऊर्ध्वम् mean?",
            ("Above", "ऊर्ध्वम् = above (data)."),
            [("Below", "Below would be अधः; ऊर्ध्वम् is above."),
             ("Within", "Within would be अन्तः; ऊर्ध्वम् is above."),
             ("Behind", "Behind would be पश्चात्; ऊर्ध्वम् is above.")],
            "ऊर्ध्वम् = above.",
            "अशीतिः ऊर्ध्वम्: eighty above."),
        fill(1, "In unit 122 'above' is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("ऊर्ध्वम्", None, "urdhvam", "urdhva"),
             "ऊर्ध्वम् = above; printed रूर्ध्वं with the र् of अशीतिर्.",
             "ऊर्ध्वम् = above.",
             "अशीतिः + ऊर्ध्वम्.", role="warmup"),
        mcq("extend", 2, "Why does the data flag the printed अशीति (eighty) in unit 122?",
            ("As printed, the parts make 207, not 210", "68 + 59 + 80 = 207, against the total of unit 119."),
            [("अशीति is not a Sanskrit number word", "अशीति is a number word: eighty."),
             ("The line is too damaged to be read", "The line is read; confidence is medium."),
             ("Unit 119 gives no total for the joints", "Unit 119 gives 210 (दशोत्तरं शतद्वयम्).")],
            "The printed parts 68 + 59 + 80 make 207, not 210; the data notes a possible 83.",
            "Totals check: 68 + 59 + 80 = 207 ≠ 210.",
            teaches="When a total and its parts disagree, the data flags the reading and keeps the printed word."),
        mcq("discriminate", 3, "The print divides अशीति रूर्ध्वं. How does the data restore the words?",
            ("अशीतिः + ऊर्ध्वम्", "After इ, a visarga before a vowel becomes र्; the print put that र् on the next word."),
            [("अशीति + रूर्ध्वम्", "रूर्ध्वम् is not a word; the र् is from the visarga of अशीतिः."),
             ("अशीतिर् + रूर्ध्वम्", "There is only one र्, from the visarga; the word is ऊर्ध्वम्."),
             ("अशीतिम् + ऊर्ध्वम्", "म् before a vowel would give अशीतिमूर्ध्वम्.")],
            "अशीतिः (eighty) + ऊर्ध्वम् (above) → अशीतिरूर्ध्वम्.",
            "A visarga after इ → र् before a vowel."),
        multi("apply", 4, "Which statements fit unit 122 and its data?",
              [("The translation keeps the printed 'eighty'", "Right: the translation keeps eighty as printed."),
               ("The data changes the word to eighty-three", "Eighty-three is only a possible reading; the word list keeps अशीतिः."),
               ("The line itself names the neck and head", "It says only 'above'; neck and head is a probable reading."),
               ("The counted noun is not printed", "Right: the line is elliptical, as units 120-121.")],
              [0, 3],
              "Eighty is kept as printed; the counted noun is unstated; 'above' is not explained further.",
              "अशीति रूर्ध्वं: eighty above."),
        mcq("transfer", 5, "By the rule of अशीतिः + ऊर्ध्वम्, how is मतिः + एव (the mind itself) joined in a new example?",
            ("मतिरेव", "After इ, a visarga before a vowel becomes र्, as अशीतिः + ऊर्ध्वम् → अशीतिरूर्ध्वम्."),
            [("मतिरेवः", "The visarga is used up as र्; no visarga is added at the end."),
             ("मत्येव", "इ + ए → ये only with no visarga; here the visarga gives र्."),
             ("मतिः एव", "Before a vowel this visarga does not stay; it becomes र्.")],
            "मतिः + एव = मतिरेव, like अशीतिः + ऊर्ध्वम् = अशीतिरूर्ध्वम्.",
            "इः + vowel → इर्.",
            teaches="A visarga after इ becomes र् before a vowel: अशीतिः + ऊर्ध्वम् → अशीतिरूर्ध्वम्."),
    ],
}

# ---------------------------------------------------------------- unit 123
AUTHORED["123"] = {
    "title": "तत्रैकैकस्मिन् सक्थि ... द्वावंगुष्ठे",
    "question": "By unit 123, how many are counted in each toe and in the great toe?",
    "rule": ("There, in each single sakthi (probably each limb): three in each toe (पादाङ्गुलौ प्रत्येकं त्रयः), two in "
             "the great toe (द्वावङ्गुष्ठे)."),
    "limits": ("Prose. The counted noun is not printed (probably the bone-joints, from unit 119). The printed locative "
               "सक्थि is flagged (सक्थ्नि expected) and its sense 'each limb' is probable: no question on sakthi. The "
               "total of this line is given in unit 124."),
    "explain_hi": ("यह गद्य-पंक्ति शाखाओं की ६८ की गिनती खोलना शुरू करती है। "
                   "वहाँ हर एक सक्थि में (सक्थि का शब्दार्थ जाँघ या टाँग है; यहाँ सम्भवतः हर शाखा): पैर की हर अंगुली में तीन, और अँगूठे में दो। "
                   "गिनी गई वस्तु छपी नहीं; सम्भवतः अस्थि-सन्धियाँ। "
                   "‘अङ्गुलौ’ स्त्रीलिंग अङ्गुलि का वैकल्पिक -औ वाला सप्तमी रूप है; ‘प्रत्येकम्’ के साथ इसका अर्थ है ‘हर अंगुली में’। "
                   "इसका जोड़ अगली इकाई १२४ में है: वे चौदह।"),
    "hook": "हर अंगुली में तीन, अँगूठे में दो।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 123, what is counted in the toes and the great toe?",
            ("Three in each toe, two in the great toe", "पादांगुलौ प्रत्येकं त्रयः, द्वावंगुष्ठे."),
            [("Two in each toe, three in the great toe", "The numbers are the other way round: three, then two."),
             ("Three in each toe, three in the great toe", "The great toe has two (द्वौ)."),
             ("Two in each toe, one in the great toe", "Each toe has three (त्रयः), the great toe two.")],
            "Three in each toe, two in the great toe.",
            "पादांगुलौ प्रत्येकं त्रयः द्वावंगुष्ठे."),
        order(1, "Put these phrases of unit 123 in the line's order.",
              ["तत्रैकैकस्मिन् सक्थि", "पादांगुलौ", "प्रत्येकं त्रयः", "द्वावंगुष्ठे"],
              "There in each limb: in the toe, three in each; two in the great toe.",
              "तत्रैकैकस्मिन् सक्थि → पादांगुलौ → प्रत्येकं त्रयः → द्वावंगुष्ठे."),
        match(2, "Match each word of unit 123 to its meaning.",
              [["प्रत्येकम्", "in each, severally"], ["त्रयः", "three"], ["द्वौ", "two"], ["पाद", "foot"],
               ["अङ्गुष्ठ", "great toe, thumb"]],
              "In each toe three, two in the great toe.",
              "प्रत्येकम्, त्रयः, द्वौ, पाद, अङ्गुष्ठ.", role="extend",
              teaches="प्रत्येकम् makes the count distributive: three in each toe, not three in all."),
        mcq("discriminate", 3, "Which split of द्वावंगुष्ठे in unit 123 is right?",
            ("द्वौ + अङ्गुष्ठे", "औ before a vowel becomes आव्: द्वौ + अङ्गुष्ठे → द्वावङ्गुष्ठे."),
            [("द्वे + अङ्गुष्ठे", "ए + अ would give द्वेऽङ्गुष्ठे, with ए kept."),
             ("द्वा + वङ्गुष्ठे", "वङ्गुष्ठे is not a word; the व् comes from औ."),
             ("द्वौ + वङ्गुष्ठे", "There is no वङ्गुष्ठ; the word is अङ्गुष्ठ (great toe).")],
            "द्वौ (two) + अङ्गुष्ठे (in the great toe): औ + vowel → आव्.",
            "औ + a vowel → आव् + that vowel."),
        multi("apply", 4, "Which statements fit unit 123?",
              [("The great toe has two", "Right: द्वावंगुष्ठे."),
               ("The fingers of the hand are named", "The line names the toes of the foot (पादाङ्गुलि)."),
               ("The counted noun is printed", "It is not printed; probably the bone-joints."),
               ("Each toe has three", "Right: पादांगुलौ प्रत्येकं त्रयः.")],
              [0, 3],
              "Three in each toe, two in the great toe; the counted noun is unstated.",
              "पादांगुलौ प्रत्येकं त्रयः द्वावंगुष्ठे."),
        mcq("transfer", 5, "By the rule of तत्र + एकैकस्मिन् → तत्रैकैकस्मिन्, how is तत्र + एव (there itself) joined?",
            ("तत्रैव", "अ + ए → ऐ, as तत्र + एकैकस्मिन् → तत्रैकैकस्मिन्."),
            [("तत्रेव", "ए comes from अ + इ, not from अ + ए."),
             ("तत्रोव", "ओ comes from अ + उ, not from अ + ए."),
             ("तत्र्येव", "य् comes from इ before a vowel; तत्र ends in अ.")],
            "तत्र + एव = तत्रैव, like तत्र + एकैकस्मिन् = तत्रैकैकस्मिन्.",
            "अ + ए → ऐ.",
            teaches="अ before ए gives ऐ: तत्र + एकैकस्मिन् → तत्रैकैकस्मिन् (and एक + एक → एकैक)."),
    ],
}

# ---------------------------------------------------------------- unit 124
AUTHORED["124"] = {
    "title": "ते चतुर्दश",
    "question": "By unit 124, what total closes the count of unit 123?",
    "rule": ("Those (ते) are fourteen (चतुर्दश): three in each of the four toes and two in the great toe of unit 123 "
             "(3 × 4 + 2 = 14, data check)."),
    "limits": ("Prose, two words; the copula is understood. The counted noun is not printed. 'Four toes' besides the "
               "great toe is the data's check, not printed in unit 123."),
    "explain_hi": ("यह दो शब्दों की गद्य-पंक्ति है: वे चौदह हैं। "
                   "‘ते’ (वे) इकाई १२३ में गिनी गई वस्तुओं की ओर संकेत करता है। "
                   "डेटा की जाँच: चार अंगुलियों में तीन-तीन (१२) और अँगूठे में दो, मिलाकर १४, एक पैर में। "
                   "‘चतुर्दश’ = चतुर् (चार) + दश (दस)। क्रिया ‘हैं’ समझी जाती है।"),
    "hook": "३ × ४ + २ = १४।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 124, what total is given?",
            ("Fourteen", "ते चतुर्दश: those are fourteen."),
            [("Forty", "चतुर्दश is fourteen; forty is चत्वारिंशत्."),
             ("Twelve", "Twelve would be द्वादश; the line says चतुर्दश."),
             ("Sixteen", "Sixteen would be षोडश; the line says चतुर्दश.")],
            "Those are fourteen.",
            "ते चतुर्दश."),
        match(1, "Match each word part of unit 124 to its meaning.",
              [["ते", "those"], ["चतुर्", "four"], ["दश", "ten"], ["चतुर्दश", "fourteen"]],
              "ते चतुर्दश: those are four-and-ten.",
              "ते, चतुर्, दश, चतुर्दश."),
        mcq("extend", 2, "By the data's check, how is the fourteen of unit 124 reached?",
            ("Three in each of four toes, plus two", "3 × 4 + 2 (great toe) = 14 (data note)."),
            [("Three in each of five toes, less one", "The great toe is counted apart, with two."),
             ("Two in each of seven places of the leg", "The count is of the toes and the great toe (unit 123)."),
             ("Four in each of three toes, plus two", "Each toe has three, not four (unit 123).")],
            "Four toes × 3 = 12, plus 2 in the great toe = 14.",
            "ते चतुर्दश totals unit 123.",
            teaches="ते (those) takes up the items of the line before and gives their total."),
        mcq("discriminate", 3, "In unit 124, what does ते (those) refer to?",
            ("The ones counted in unit 123", "Data note: 'those are fourteen' totals unit 123."),
            [("The 210 joints of unit 119", "210 is the whole; ते takes up only unit 123."),
             ("The 68 in the limbs of unit 120", "68 is the limbs' total, not fourteen."),
             ("The five bone classes of unit 118", "The classes are not counted here.")],
            "ते = those counted in the toes and great toe (unit 123).",
            "ते चतुर्दश = those (of unit 123) are fourteen."),
        fill(4, "In unit 124 'fourteen' is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("चतुर्दश", None, "fourteen"),
             "चतुर्दश = fourteen (चतुर् + दश).",
             "चतुर्दश = fourteen.",
             "ते चतुर्दश.", role="apply"),
        mcq("transfer", 5, "By the pattern of चतुर्दश (four + ten), what does पञ्चदश mean in a new example?",
            ("Fifteen", "पञ्च (five) + दश (ten) = fifteen, as चतुर् + दश = fourteen."),
            [("Fifty", "Fifty is पञ्चाशत्; पञ्चदश is five plus ten."),
             ("Five tens", "The parts are added, not multiplied."),
             ("Ten less five", "Nothing takes away; the parts are added.")],
            "पञ्चदश = 15, as चतुर्दश = 14.",
            "unit number + दश = that number plus ten.",
            teaches="A unit number before दश is added to ten: चतुर्दश = 4 + 10."),
    ],
}

# ---------------------------------------------------------------- unit 125
AUTHORED["125"] = {
    "title": "एकैको गुल्फजानुवंक्षणेषु",
    "question": "By unit 125, how many are in the ankle, knee and groin, and what follows?",
    "rule": ("One each (एकैकः) in the ankles (गुल्फ), knees (जानु) and groins (वङ्क्षण); then three in the "
             "कतिकपाल (hip kapālas, on a conjectural reading)."),
    "limits": ("Prose. The counted noun is not printed. The printed कतिकपालेषु is flagged (कटिकपालेषु, hip bone-plates, "
               "is a possible reading): no question on that place. The data's check: 14 + 3 = 17 per limb, × 4 = 68 "
               "(unit 120), on the probable reading of sakthi as each limb."),
    "explain_hi": ("यह गद्य-पंक्ति दो भाग रखती है। "
                   "पहला: गुल्फ (टखना), जानु (घुटना) और वंक्षण (जाँघ का मूल) में एक-एक; ये तीनों मानक पहचान हैं। "
                   "इससे एक शाखा की गिनती पूरी होती है: पैर के १४ + ३ = १७, और चार शाखाओं में ६८ (डेटा की जाँच, सम्भावित)। "
                   "दूसरा: छपे ‘कतिकपालेषु’ में तीन; ‘कति’ (कितने) का अर्थ नहीं बनता, इसलिए ‘कटिकपाल’ (कमर के कपाल) अनुमानित पाठ है। "
                   "‘एकैको गुल्फ’ में एकैकः का विसर्ग घोष व्यंजन ग से पहले ओ बना।"),
    "hook": "टखना, घुटना, वंक्षण: एक-एक; एक शाखा में सत्रह।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 125, where is there one each?",
            ("Ankle, knee and groin", "एकैको गुल्फजानुवंक्षणेषु: one each in ankles, knees, groins."),
            [("Wrist, elbow and armpit", "These are not in unit 125."),
             ("Neck, jaw and the head", "These are not in unit 125."),
             ("Spine, flank and chest", "These are not in unit 125.")],
            "One each in the ankles, knees and groins.",
            "एकैको गुल्फजानुवंक्षणेषु."),
        order(1, "Put the places of 'one each' in the order of unit 125.",
              ["गुल्फ", "जानु", "वङ्क्षण"],
              "Ankle, knee, groin: up the leg.",
              "गुल्फ → जानु → वङ्क्षण."),
        match(2, "Match each word of unit 125 to its meaning.",
              [["एकैकः", "one each"], ["गुल्फ", "ankle"], ["जानु", "knee"], ["वङ्क्षण", "groin"], ["त्रयः", "three"]],
              "One each in ankle, knee, groin; three (in the place that follows).",
              "एकैकः, गुल्फ, जानु, वङ्क्षण, त्रयः.", role="extend",
              teaches="गुल्फ, जानु, वङ्क्षण rise up the leg from the foot: they finish one limb's count."),
        mcq("discriminate", 3, "Why is एकैकः printed एकैको before गुल्फ in unit 125?",
            ("अः becomes ओ before a voiced consonant", "ग is a voiced consonant: एकैकः + गुल्फ... → एकैको गुल्फ...."),
            [("अः becomes ओ before every consonant", "Before an unvoiced consonant it does not become ओ."),
             ("ओ is the dual ending of एकैक", "The form is एकैकः (nom. sg.); the ओ comes from sandhi."),
             ("The visarga always drops after अ", "After अ it becomes ओ here; it does not simply drop.")],
            "एकैकः + गुल्फ... = एकैको गुल्फ...: अः before a voiced consonant → ओ.",
            "अः + voiced consonant → ओ."),
        mcq("apply", 4, "Unit 124 gave fourteen in the foot. With one each in ankle, knee and groin, what does one limb hold?",
            ("Seventeen", "14 + 1 + 1 + 1 = 17 per limb (data check)."),
            [("Fifteen", "Three places add three, not one."),
             ("Sixteen", "Three places add three, not two."),
             ("Twenty", "Each place adds one, so three in all.")],
            "14 + 3 = 17 per limb; × 4 = 68 (unit 120).",
            "14 (foot) + गुल्फ + जानु + वङ्क्षण = 17."),
        mcq("transfer", 5, "एकैकः (one each) repeats एक. In a new example, what does पञ्च पञ्च mean?",
            ("Five each", "A repeated number is distributive, as एक + एक → एकैकः, one each."),
            [("Fifty-five", "The words are not a compound number."),
             ("Five times five", "The repetition does not multiply."),
             ("Five or more", "The repetition does not mean 'or more'.")],
            "पञ्च पञ्च = five each, like एकैकः = one each.",
            "A repeated number = so many each.",
            teaches="Repeating a number makes it distributive: एकैकः = one each (एक + एक, अ + ए → ऐ)."),
    ],
}

# ---------------------------------------------------------------- unit 126
AUTHORED["126"] = {
    "title": "चतुर्विंशतिःपृष्ठवंशे",
    "question": "By unit 126, how many are in the spine (pṛṣṭhavaṃśa)?",
    "rule": ("Twenty-four (चतुर्विंशतिः) in the spine (पृष्ठवंशे, literally 'back-ridge', standard): part of the trunk count."),
    "limits": ("Prose; no verb, no counted noun. Whether the 24 are in one line or spread is not said."),
    "explain_hi": ("यह गद्य-पंक्ति धड़ की गिनती आगे बढ़ाती है: चौबीस पृष्ठवंश में। "
                   "पृष्ठवंश का शब्दार्थ है पीठ की धार (पृष्ठ = पीठ, वंश = बाँस जैसी धार); यह रीढ़ है (मानक)। "
                   "‘चतुर्विंशति’ = चतुर् (चार) + विंशति (बीस)। "
                   "छपाई में दोनों शब्द जुड़े हैं और प से पहले विसर्ग वैसा ही रहा है। "
                   "गिनी गई वस्तु छपी नहीं।"),
    "hook": "रीढ़ में चौबीस।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 126, how many are in the spine?",
            ("Twenty-four", "चतुर्विंशतिः पृष्ठवंशे: twenty-four in the spine."),
            [("Forty-two", "विंशति is twenty and चतुर् four: twenty-four."),
             ("Thirty-two", "Thirty-two is not the spine's number here."),
             ("Fourteen", "Fourteen is the foot's total (unit 124).")],
            "Twenty-four in the spine.",
            "चतुर्विंशतिः पृष्ठवंशे."),
        match(1, "Match each word part of unit 126 to its meaning.",
              [["चतुर्", "four"], ["विंशति", "twenty"], ["पृष्ठ", "back"], ["पृष्ठवंश", "spine"]],
              "Four-and-twenty in the back-ridge, the spine.",
              "चतुर्, विंशति, पृष्ठ, पृष्ठवंश."),
        fill(2, "In unit 126 'in the spine' is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("पृष्ठवंशे"),
             "पृष्ठवंशे = in the spine, locative singular of पृष्ठवंश.",
             "पृष्ठवंश = the spine (literally back-ridge).",
             "चतुर्विंशतिः पृष्ठवंशे."),
        mcq("discriminate", 3, "In the print चतुर्विंशतिःपृष्ठवंशे, what happens to the visarga before प?",
            ("It stays as visarga", "Before प the visarga stays: चतुर्विंशतिः पृष्ठवंशे."),
            [("It becomes ओ", "ओ comes from अः before a voiced consonant; here इः meets unvoiced प."),
             ("It becomes र्", "र् comes before a vowel or a voiced sound; प is unvoiced."),
             ("It becomes स्", "स् comes before त or थ, not before प.")],
            "Visarga before प stays as ः.",
            "Visarga before क/प (unvoiced) stays."),
        multi("apply", 4, "Which statements fit unit 126?",
              [("पृष्ठवंश literally means 'back-ridge'", "Right: data note, the spine."),
               ("The 24 are said to be for each side", "No side is named in unit 126."),
               ("Twenty-four are in the spine", "Right: चतुर्विंशतिः पृष्ठवंशे."),
               ("The counted noun is printed here", "It is not printed in unit 126.")],
              [0, 2],
              "Twenty-four in the spine (back-ridge); no side and no counted noun are printed.",
              "चतुर्विंशतिः पृष्ठवंशे."),
        mcq("transfer", 5, "By the pattern of चतुर्विंशति (four + twenty), what does पञ्चविंशति mean in a new example?",
            ("Twenty-five", "पञ्च (five) + विंशति (twenty) = twenty-five."),
            [("Forty-five", "विंशति is twenty, not forty."),
             ("One hundred", "The parts are added, not multiplied."),
             ("Fifteen", "Fifteen is पञ्चदश; विंशति is twenty.")],
            "पञ्चविंशति = 25, as चतुर्विंशति = 24.",
            "unit number + विंशति = twenty plus that number.",
            teaches="A unit number before विंशति is added to twenty: चतुर्विंशति = 24."),
    ],
}

# ---------------------------------------------------------------- unit 127
AUTHORED["127"] = {
    "title": "तद्वत्पार्श्वयोः",
    "question": "By unit 127, what is said of the two flanks (pārśva)?",
    "rule": ("Likewise (तद्वत्, 'like that') in the two flanks (पार्श्वयोः): the count of the line before is repeated; "
             "no number is printed."),
    "limits": ("Prose, one printed word-run. The number is not printed; presumably the 24 of unit 126, but the "
               "translation does not supply it. Whether it is per flank or for both is not said."),
    "explain_hi": ("यह गद्य-पंक्ति कहती है: वैसे ही दोनों पार्श्वों, यानी बगलों, में। "
                   "‘तद्वत्’ = उसकी तरह, यानी पिछली गिनती जैसी; संख्या छपी नहीं, सम्भवतः इकाई १२६ के चौबीस। "
                   "अनुवाद यह संख्या नहीं जोड़ता। "
                   "‘पार्श्वयोः’ पार्श्व (शरीर की बगल, मानक) का सप्तमी द्विवचन है: दोनों बगलों में। "
                   "छपाई में तद्वत् और पार्श्वयोः जुड़े हैं; प से पहले त् नहीं बदलता।"),
    "hook": "तद्वत्: जितने रीढ़ में, उतने बगलों में (सम्भवतः)।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 127, what does तद्वत् mean?",
            ("Likewise, like that", "तद्वत् = like that: the count before is repeated."),
            [("Therefore, so", "Therefore would be अतः; तद्वत् means like that."),
             ("Twice, doubled", "Nothing in तद्वत् doubles; it means like that."),
             ("Except, but not", "तद्वत् adds no exception; it means like that.")],
            "तद्वत् = likewise.",
            "तत् + वत् = like that."),
        match(1, "Match each part of unit 127 to its meaning.",
              [["तत्", "that"], ["-वत्", "like"], ["पार्श्व", "flank, side"], ["पार्श्वयोः", "in the two flanks"]],
              "Like that, in the two flanks.",
              "तत्, -वत्, पार्श्व, पार्श्वयोः."),
        mcq("extend", 2, "Which statement about the number in unit 127 is right?",
            ("It is not printed; तद्वत् points back", "The data: presumably the number of unit 126; not supplied."),
            [("It is printed as eight for each flank", "No number is printed in unit 127."),
             ("The translation supplies twenty-four", "The translation does not supply the number."),
             ("It is printed as fifty-nine for both", "Fifty-nine is the trunk total (unit 121), not printed here.")],
            "No number is printed; तद्वत् repeats the count before, presumably 24.",
            "तद्वत् = as many as before.",
            teaches="तद्वत् carries a number over from the line before instead of repeating it."),
        mcq("discriminate", 3, "Which split of तद्वत्पार्श्वयोः in unit 127 is right?",
            ("तद्वत् + पार्श्वयोः", "त् before the unvoiced प stays त्; the words are only printed together."),
            [("तद् + वत्पार्श्वयोः", "वत्पार्श्व is not a word; -वत् belongs to तद्."),
             ("तद्व + त्पार्श्वयोः", "त्पार्श्वयोः is not a word; the word is पार्श्वयोः."),
             ("तद्वत्पार्श्व + योः", "योः alone is an ending, not a word.")],
            "तद्वत् (likewise) + पार्श्वयोः (in the two flanks).",
            "त् before an unvoiced consonant such as प stays त्."),
        fill(4, "In unit 127 'in the two flanks' is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("पार्श्वयोः"),
             "पार्श्वयोः = in the two flanks (loc. du. of पार्श्व).",
             "पार्श्वयोः = in the two flanks.",
             "तद्वत् पार्श्वयोः.", role="apply"),
        mcq("transfer", 5, "By the pattern of पार्श्वयोः (in the two flanks), how is हस्त (hand) put in the locative dual?",
            ("हस्तयोः", "-योः marks the locative dual of अ-stems, as पार्श्व → पार्श्वयोः."),
            [("हस्तेषु", "-एषु is plural: in the hands (more than two)."),
             ("हस्ते", "हस्ते is singular: in the hand."),
             ("हस्तौ", "हस्तौ is the nominative/accusative dual, not locative.")],
            "हस्तयोः = in the two hands, like पार्श्वयोः = in the two flanks.",
            "अ-stem, locative dual: -योः.",
            teaches="The locative dual of अ-stems ends in -योः: पार्श्व → पार्श्वयोः."),
    ],
}


# ===================================================================== NOTES_HI
NOTES_HI = {
    "115": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। ‘रुचक’ अस्थि-वर्ग का नाम है, अनुवाद नहीं किया गया (देखें इकाई ११८)। "
            "क्रिया ‘हैं’ समझी जाती है। सन्धि जाँची: दशनाः + तु → दशनास्तु (त से पहले विसर्ग → स्)।"),
    "116": ("गद्य; विश्वास मध्यम; दो छपी पंक्तियाँ (०२.०५.१२४, ०२.०५.१२५); कोई पाठ-चिह्न नहीं। छपे ‘ग्रीवाऽक्षि’ में आ के बाद "
            "अवग्रह छपाई की आदत है: ग्रीवा + अक्षि → ग्रीवाक्षि (आ + अ → आ)। तरुण = कोमल, उपास्थि (सम्भावित); अक्षिकोष = आँख का "
            "गड्ढा (सम्भावित); वलय = छल्ला, आकार से नाम। दोनों स्थान-सूचियाँ द्वन्द्व, सप्तमी बहुवचन (-एषु)।"),
    "117": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। नलक = छोटी नली, सरकंडा; नली जैसी अस्थियों का वर्ग सामान्य पाठ (सम्भावित)। "
            "अन्त का ‘इति’ वर्गीकरण की समाप्ति दिखाता है, अनुवाद में नहीं लिया गया। सन्धि जाँची: नलकानि + इति → नलकानीति "
            "(इ + इ → ई)।"),
    "118": ("गद्य; विश्वास मध्यम; दो छपी पंक्तियाँ (०२.०५.१२७, ०२.०५.१२८)। पाठ-चिह्न (सम्भावित): छपा ‘नामानुगतामूनीनि’ "
            "शब्द नहीं बनता; ‘नामानुगतान्यमूनि’ (नामानुगतानि + अमूनि) सुझाया गया; ‘नाम के अनुसार’ इसी अनुमानित पाठ पर है, इस पर कोई "
            "प्रश्न नहीं। पाँच वर्गों की सूची (कपाल, रुचक, तरुण, वलय, नलक) इकाई ११४-११७ से निकाली गई है, यहाँ छपी नहीं। ‘मांसानि’ "
            "बहुवचन, मांस-पिण्ड (सम्भवतः पेशियाँ)। सन्धि जाँची: विधानि + अस्थीनि → विधान्यस्थीनि (इ + भिन्न स्वर → य्); स्नायुभिः + च "
            "→ स्नायुभिश्च (च से पहले विसर्ग → श्); छपा पंच = पञ्च।"),
    "119": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। गिनती छपे अनुसार: २०० + १० = २१०। क्रिया नहीं; ‘संख्या’ शब्द संस्कृत में नहीं, "
            "षष्ठी (अस्थिसन्धीनाम्) से समझा जाता है। सन्धि जाँची: दश + उत्तरम् → दशोत्तरम् (अ + उ → ओ), व्यंजन से पहले छपा "
            "दशोत्तरं (ं); शतद्वयम् + अस्थि → शतद्वयमस्थि (स्वर से पहले म्)।"),
    "120": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। समूह-टिप्पणी: इकाई १२०-१२२ इकाई ११९ के २१० का बँटवारा करती दिखती हैं। "
            "गिनी गई वस्तु छपी नहीं, सम्भवतः अस्थि-सन्धियाँ। शाखा = हाथ-पैर (मानक)। सन्धि जाँची: तेषाम् + अष्टषष्टिः → "
            "तेषामष्टषष्टिः; श से पहले छपा विसर्ग (‘षष्टिःशा’) नियमित है।"),
    "121": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। अन्तराधि = धड़ (मानक)। एकोनषष्टि = एक + ऊन + षष्टि (अ + ऊ → ओ), साठ में एक कम। "
            "सन्धि जाँची: एकोनषष्टिः + अन्तराधौ → एकोनषष्टिरन्तराधौ (इ के बाद विसर्ग + स्वर → र्); छपा ‘अंतराधौ’ = अन्तराधौ।"),
    "122": ("गद्य; विश्वास मध्यम। पाठ-चिह्न (सम्भावित): छपा ‘अशीति’ (अस्सी); इकाई १२९-१३४ के स्थानों का जोड़ ८३ है और ६८ + ५९ + ८३ = २१०, "
            "इसलिए ‘त्र्यशीतिः’ (तिरासी) सुझाया गया; छपे अनुसार ६८ + ५९ + ८० = २०७। अनुवाद और शब्द-सूची छपा ‘अशीतिः’ रखते हैं; "
            "कौन-सी संख्या ठीक है, इस पर कोई प्रश्न नहीं। ऊर्ध्वम् = ऊपर, सम्भवतः गर्दन और सिर (सम्भावित)। छपाई ‘अशीति रूर्ध्वं’ = "
            "अशीतिः + ऊर्ध्वम् → अशीतिरूर्ध्वम् (इ के बाद विसर्ग + स्वर → र्), र् अगले शब्द से जुड़ा छपा।"),
    "123": ("गद्य; विश्वास मध्यम। पाठ-चिह्न (सम्भावित): छपा सप्तमी ‘सक्थि’, अपेक्षित ‘सक्थ्नि’ (या सक्थिनि); यही छपा रूप इकाई १४८ में भी, "
            "सम्भवतः संस्करण की आदत; इस पर कोई प्रश्न नहीं। सक्थि = जाँघ या टाँग, यहाँ हर शाखा (सम्भावित, क्योंकि ६८ = ४ × १७)। "
            "अङ्गुलौ = स्त्रीलिंग अङ्गुलि का वैकल्पिक -औ सप्तमी। गिनी गई वस्तु छपी नहीं। सन्धि जाँची: तत्र + एकैकस्मिन् → "
            "तत्रैकैकस्मिन् (अ + ए → ऐ); द्वौ + अङ्गुष्ठे → द्वावङ्गुष्ठे (औ + स्वर → आव्); छपे पादांगुलौ, अंगुष्ठे में ं = ङ्।"),
    "124": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। क्रिया समझी जाती है। जाँच: ३ × ४ अंगुलियाँ + २ (अँगूठा) = १४, इकाई १२३ के अनुसार "
            "एक पैर में। कोई सन्धि-परिवर्तन नहीं।"),
    "125": ("गद्य; विश्वास मध्यम। पाठ-चिह्न (सम्भावित): छपा ‘कतिकपालेषु’, ‘कति’ (कितने) का अर्थ नहीं बनता; ‘कटिकपालेषु’ (कमर के "
            "कपाल) सुझाया गया; यही वर्तनी इकाई १३८ में भी; इस स्थान पर कोई प्रश्न नहीं। गुल्फ = टखना, जानु = घुटना, वंक्षण = जाँघ का "
            "मूल (सभी मानक)। जाँच: १४ + ३ = १७ प्रति शाखा, × ४ = ६८ (इकाई १२०)। सन्धि जाँची: एकैकः + गुल्फ... → एकैको गुल्फ... "
            "(अः + घोष व्यंजन → ओ); एक + एक → एकैक (अ + ए → ऐ)।"),
    "126": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। पृष्ठवंश = पीठ की धार, रीढ़ (मानक)। छपाई में दोनों शब्द जुड़े; प से पहले विसर्ग "
            "रहता है (‘चतुर्विंशतिःपृष्ठ’)।"),
    "127": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। तद्वत् = उसकी तरह; संख्या छपी नहीं, सम्भवतः इकाई १२६ के २४; अनुवाद संख्या नहीं "
            "जोड़ता। पार्श्व = शरीर की बगल (मानक); पार्श्वयोः सप्तमी द्विवचन। छपाई में तद्वत्पार्श्वयोः जुड़ा; प से पहले त् नहीं बदलता।"),
}


# ===================================================================== AIDS
AIDS = {
    "115": {
        "chunks": "दशनास्तु | रुचकाः",
        "sandhi": "त से पहले विसर्ग → स्: दशनाः + तु → दशनास्तु।",
        "frame": "क्या: दशनाः (दाँत) → किस वर्ग के: रुचकाः → क्रिया: ‘हैं’ समझी जाती है।",
    },
    "116": {
        "diagram": {"groups": [
            {"label": "तरुण (कोमल; सम्भवतः उपास्थि)", "items": ["घ्राण (नाक)", "कर्ण (कान)", "ग्रीवा (गर्दन)",
                                                         "अक्षिकोष (आँख का गड्ढा, सम्भावित)"]},
            {"label": "वलय (छल्ले)", "items": ["पाणि (हाथ)", "पाद (पैर)", "पार्श्व (बगल)", "पृष्ठ (पीठ)"]}]},
        "chunks": "घ्राणकर्णग्रीवाऽक्षिकोषेषु | तरुणानि || पाणिपादपार्श्वपृष्ठेषु | वलयानि",
        "contrast": "तरुण: सिर-गर्दन के कोमल भाग (नाक, कान, गर्दन, आँख) ↔ वलय: धड़-शाखाओं के भाग (हाथ, पैर, बगल, पीठ)।",
        "letters": "पहले अक्षर क्रम से: घ्रा-क-ग्री-अ (तरुण), पा-पा-पा-पृ (वलय)। (मेरी याद-पद्धति)",
    },
    "117": {
        "chunks": "शेषाणि | नलकानीति",
        "sandhi": "इ + इ → ई: नलकानि + इति → नलकानीति।",
        "anchors": "नलक ~ नल (नली, नल): लम्बी नली जैसी अस्थियाँ। (मेरी याद-पद्धति, शब्द-साम्य पर)",
    },
    "118": {
        "diagram": {"groups": [
            {"label": "पाँच वर्ग (इकाई ११४-११७ से)", "items": ["१ कपाल", "२ रुचक", "३ तरुण", "४ वलय", "५ नलक"]},
            {"label": "उनमें (तेषु)", "items": ["मांस बँधे हैं", "सिराओं से", "स्नायुओं से"]}]},
        "chunks": "नामानुगतामूनीनि (अनुमानित पाठ: नामानुगतान्यमूनि) | पंच विधान्यस्थीनि || तेषु हि | सिराभिः स्नायुभिश्च | "
                  "निबद्धानि मांसानि",
        "sandhi": "इ + भिन्न स्वर → य्: विधानि + अस्थीनि → विधान्यस्थीनि · च से पहले विसर्ग → श्: स्नायुभिः + च → स्नायुभिश्च।",
        "letters": "पाँच वर्ग क्रम से: क-रु-त-व-न (कपाल, रुचक, तरुण, वलय, नलक)। (मेरी याद-पद्धति)",
    },
    "119": {
        "chunks": "दशोत्तरं | शतद्वयम् | अस्थिसंधीनां",
        "sandhi": "अ + उ → ओ: दश + उत्तरम् → दशोत्तरम् · स्वर से पहले म्: शतद्वयम् + अस्थि → शतद्वयमस्थि।",
        "frame": "कितने: शतद्वयम् (२००) + दशोत्तरम् (१० अधिक) = २१० → किसके: अस्थिसन्धीनाम् (हड्डियों के जोड़ों के)।",
    },
    "120": {
        "chunks": "तेषाम् | अष्टषष्टिः | शाखासु",
        "frame": "किसमें से: तेषाम् (उन २१० में से) → कितने: अष्टषष्टिः (६८) → कहाँ: शाखासु (हाथ-पैरों में)।",
        "anchors": "शाखा = पेड़ की डाल; शरीर की डालें = हाथ-पैर। (मेरी याद-पद्धति)",
    },
    "121": {
        "chunks": "एकोनषष्टिः | अंतराधौ",
        "sandhi": "इ के बाद विसर्ग + स्वर → र्: एकोनषष्टिः + अन्तराधौ → एकोनषष्टिरन्तराधौ।",
        "frame": "कितने: एक-ऊन-षष्टि (साठ में एक कम = ५९) → कहाँ: अन्तराधौ (धड़ में)।",
    },
    "122": {
        "diagram": {"groups": [
            {"label": "छपे अनुसार २१० का बँटवारा", "items": ["शाखाएँ (इकाई १२०): ६८", "अन्तराधि (इकाई १२१): ५९",
                                                       "ऊर्ध्व (इकाई १२२): ८० छपा", "जोड़: २०७"]},
            {"label": "पाठ-चिह्न", "items": ["इकाई ११९ का कुल: २१०", "स्थानों का जोड़ (इकाई १२९-१३४): ८३",
                                            "सम्भावित पाठ: त्र्यशीतिः (८३)"]}]},
        "chunks": "अशीति | रूर्ध्वं",
        "sandhi": "इ के बाद विसर्ग + स्वर → र्: अशीतिः + ऊर्ध्वम् → अशीतिरूर्ध्वम् (छपाई में र् अगले शब्द से जुड़ा)।",
    },
    "123": {
        "diagram": {"groups": [
            {"label": "एक पैर में (इकाई १२३)", "items": ["हर पादाङ्गुलि में: ३", "अङ्गुष्ठ (अँगूठा) में: २"]},
            {"label": "जोड़ (इकाई १२४)", "items": ["४ अंगुलियाँ × ३ = १२ (डेटा की जाँच)", "+ २ = १४: ते चतुर्दश"]}]},
        "chunks": "तत्रैकैकस्मिन् सक्थि | पादांगुलौ | प्रत्येकं त्रयः | द्वावंगुष्ठे",
        "sandhi": "अ + ए → ऐ: तत्र + एकैकस्मिन् → तत्रैकैकस्मिन् · औ + स्वर → आव्: द्वौ + अङ्गुष्ठे → द्वावङ्गुष्ठे।",
        "pegs": "मेरा बनाया चित्र: पैर की चार अंगुलियों पर ‘३’ और अँगूठे पर ‘२’ लिखा सोचें; जोड़ १४। (केवल याद की सहायता)",
    },
    "124": {
        "chunks": "ते | चतुर्दश",
        "frame": "कौन: ते (इकाई १२३ में गिने) → कितने: चतुर्दश (४ + १० = १४)।",
    },
    "125": {
        "chain": {"steps": ["पैर में: १४ (इकाई १२४)", "गुल्फ (टखना): १", "जानु (घुटना): १", "वङ्क्षण (जाँघ का मूल): १",
                            "एक शाखा में: १७", "चार शाखाओं में: ६८ (इकाई १२०; सम्भावित)"]},
        "chunks": "एकैको | गुल्फजानुवंक्षणेषु | त्रयः | कतिकपालेषु",
        "sandhi": "अः + घोष व्यंजन → ओ: एकैकः + गुल्फ... → एकैको गुल्फ... · अ + ए → ऐ: एक + एक → एकैक।",
        "frame": "भाग १: एक-एक, टखना-घुटना-वंक्षण (शाखा पूरी) → भाग २: तीन, छपा ‘कतिकपालेषु’ (अनुमानित पाठ: कटिकपाल)।",
    },
    "126": {
        "chunks": "चतुर्विंशतिः | पृष्ठवंशे",
        "frame": "कितने: चतुर्-विंशति (४ + २० = २४) → कहाँ: पृष्ठ-वंश (पीठ की धार, रीढ़)।",
        "anchors": "वंश = बाँस: रीढ़ बाँस की तरह गाँठों वाली सीधी धार। (मेरी याद-पद्धति)",
    },
    "127": {
        "chain": {"steps": ["इकाई १२६: पृष्ठवंश में २४", "तद्वत्: वैसे ही", "दोनों पार्श्वों (बगलों) में",
                            "संख्या छपी नहीं (सम्भवतः २४)"]},
        "chunks": "तद्वत् | पार्श्वयोः",
        "frame": "कितने: तद्वत् (पिछले जितने) → कहाँ: पार्श्वयोः (दोनों बगलों में, सप्तमी द्विवचन)।",
    },
}


# ===================================================================== IMAGE_SPECS
IMAGE_SPECS = {
    ("116", "diagram"): {
        "file": "sh5-taruna-valaya-116.svg",
        "alt": ("Two columns of unit 116. Taruṇa (tender ones, probably cartilage): nose, ear, neck, eye-socket "
                "(probable). Valaya (rings): hand, foot, side, back."),
        "type": "split",
        "title": "इकाई ११६: तरुण और वलय",
        "cols": [["तरुण (सम्भवतः उपास्थि)", ["घ्राण (नाक)", "कर्ण (कान)", "ग्रीवा (गर्दन)", "अक्षिकोष (सम्भावित: आँख का गड्ढा)"]],
                 ["वलय (छल्ले)", ["पाणि (हाथ)", "पाद (पैर)", "पार्श्व (बगल)", "पृष्ठ (पीठ)"]]],
    },
    ("118", "diagram"): {
        "file": "sh5-pancha-vidha-118.svg",
        "alt": ("Table of the five bone classes behind unit 118, numbered in the order of units 114-117: 1 kapāla (knee, "
                "hip, shoulder, head and others), 2 rucaka (teeth), 3 taruṇa (nose, ear, neck, eye-socket), 4 valaya "
                "(hand, foot, side, back), 5 nalaka (the remaining). The list is inferred from those units."),
        "type": "table",
        "title": "इकाई ११८: अस्थियों के पाँच प्रकार (इकाई ११४-११७ से)",
        "heads": ["वर्ग (इकाई)", "कहाँ"],
        "rows": [["१ कपाल (११४)", "जानु, नितम्ब, अंस, सिर आदि"], ["२ रुचक (११५)", "दाँत"],
                 ["३ तरुण (११६)", "नाक, कान, गर्दन, आँख का कोष"], ["४ वलय (११६)", "हाथ, पैर, बगल, पीठ"],
                 ["५ नलक (११७)", "शेष अस्थियाँ"]],
    },
    ("122", "diagram"): {
        "file": "sh5-sandhi-total-122.svg",
        "alt": ("Table of the split of the 210 bone-joints of unit 119 as printed: limbs 68 (unit 120), trunk 59 (unit "
                "121), above 80 as printed (unit 122; 83 is a possible reading); printed sum 207 against the total 210."),
        "type": "table",
        "title": "इकाई ११९-१२२: २१० का बँटवारा (छपे अनुसार)",
        "heads": ["कहाँ (इकाई)", "संख्या"],
        "rows": [["शाखाएँ (१२०)", "६८"], ["अन्तराधि, धड़ (१२१)", "५९"], ["ऊर्ध्व, ऊपर (१२२)", "८० छपा (सम्भावित पाठ ८३)"],
                 ["छपा जोड़", "२०७"], ["इकाई ११९ का कुल", "२१०"]],
    },
    ("123", "diagram"): {
        "file": "sh5-padanguli-123.svg",
        "alt": ("Table of the foot count of units 123-124: three in each toe; two in the great toe; four toes times "
                "three make twelve (data check); with the great toe, fourteen (unit 124)."),
        "type": "table",
        "title": "इकाई १२३-१२४: एक पैर की गिनती",
        "heads": ["कहाँ", "संख्या"],
        "rows": [["हर पादाङ्गुलि (प्रत्येकम्)", "३"], ["अङ्गुष्ठ (अँगूठा)", "२"],
                 ["चार अंगुलियाँ मिलाकर (डेटा की जाँच)", "१२"], ["ते चतुर्दश (इकाई १२४)", "१४"]],
    },
    ("125", "chain"): {
        "file": "sh5-shakha-17-125.svg",
        "alt": ("Chain of the limb count by the data's check: foot 14 (unit 124); ankle 1; knee 1; groin 1; one limb "
                "17; four limbs 68 (unit 120, probable reading of sakthi as each limb)."),
        "type": "chain",
        "title": "इकाई १२५: एक शाखा की गिनती (डेटा की जाँच)",
        "steps": ["पैर में: १४ (इकाई १२४)", "गुल्फ (टखना): १", "जानु (घुटना): १", "वङ्क्षण (जाँघ का मूल): १",
                  "एक शाखा में: १७", "चार शाखाओं में: ६८ (सम्भावित)"],
    },
    ("127", "chain"): {
        "file": "sh5-tadvat-parshva-127.svg",
        "alt": ("Chain of unit 127: unit 126 gives twenty-four in the spine; tadvat, likewise; in the two flanks; the "
                "number is not printed (presumably twenty-four)."),
        "type": "chain",
        "title": "इकाई १२७: तद्वत् (वैसे ही)",
        "steps": ["इकाई १२६: पृष्ठवंश में २४", "तद्वत्: वैसे ही", "दोनों पार्श्वों (बगलों) में", "संख्या छपी नहीं (सम्भवतः २४)"],
    },
}
