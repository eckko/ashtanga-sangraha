from helpers import mcq, match, order, fill, multi, accepts


def T(q, teaches):
    q["teaches"] = teaches
    return q


AUTHORED = {}

# ---------------------------------------------------------------- unit 40
AUTHORED["40"] = {
    "title": "पद्मिनीपत्रवत्तोयं",
    "question": "By unit 40, what sign of water on the body does the verse name, and what life span does it give?",
    "rule": ("In whose body (शरीरे) water (तोयम्) floats (प्लवते) like a lotus leaf (पद्मिनीपत्रवत्; पद्मिनी = Nelumbo "
             "nucifera, standard identification), his life (तस्य जीवितम्) is six months (षण्मासाः)."),
    "limits": ("The verse only says 'like a lotus leaf'; how the water behaves on such a leaf is understood, not stated. "
               "प्लवमानस्य (of one floating) may refer to the water or to the person: no question on it. Two printed lines "
               "joined in one card."),
    "explain_hi": ("यह श्लोक दो छपी पंक्तियों (०२.०९.४७ और ०२.०९.४८) से बना है और एक ही वाक्य है। "
                   "जिस देहधारी के शरीर में जल पद्मिनी (कमलिनी; मानक पहचान: नेलुम्बो न्यूसीफ़ेरा) के पत्ते की तरह तैरता है, उसका जीवन छह मास है। "
                   "‘-वत्’ का अर्थ है ‘की तरह’; पत्ते पर जल कैसा रहता है, यह श्लोक में कहा नहीं गया, केवल समझा जाता है। "
                   "‘प्लवमानस्य’ (तैरने वाले का) जल के लिए है या व्यक्ति के लिए, यह निश्चित नहीं। "
                   "‘षण्मासास्तस्य’ में त से पहले विसर्ग स् बना है।"),
    "hook": "कमल-पत्र जैसा तैरता जल: छह मास।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 40, how long is the life of one in whose body water floats like a lotus leaf?",
            ("Six months", "षण्मासाः तस्य जीवितम्: his life is six months."),
            [("Six years", "The verse says मासाः (months), not years."),
             ("Three days", "No days are named; the verse says six months."),
             ("Nine weeks", "No weeks are named; the verse says six months.")],
            "षट् (six) + मासाः (months): षण्मासाः.",
            "षण्मासाः = six months."),
        order(1, "Put these words of unit 40 in the printed order.",
              ["पद्मिनीपत्रवत्", "तोयं", "शरीरे", "देहिनः", "प्लवते"],
              "Like a lotus leaf; water; in the body; of the embodied being; floats.",
              "पद्मिनीपत्रवत् → तोयं → शरीरे → देहिनः → प्लवते."),
        match(2, "Match each word of unit 40 to its meaning.",
              [["पद्मिनी", "lotus plant (Nelumbo nucifera, standard)"], ["पत्र", "leaf"], ["तोय", "water"],
               ["देहिन्", "embodied being"], ["प्लवते", "floats"], ["जीवित", "life"]],
              "पद्मिनी = lotus plant, पत्र = leaf, तोय = water, देहिन् = embodied being, प्लवते = floats, जीवित = life.",
              "पद्मिनी, पत्र, तोय, देहिन्, प्लवते, जीवित.", role="extend",
              teaches="देहिन् (one who has a body) is a common word for a living person; देहिनः is its genitive singular."),
        mcq("discriminate", 3, "In unit 40, what does the ending -वत् add to पद्मिनीपत्र (lotus leaf)?",
            ("The sense 'like'", "पद्मिनीपत्रवत् = like a lotus leaf; the data glosses -वत् as 'like'."),
            [("The sense 'of'", "'Of' would need a genitive such as पद्मिनीपत्रस्य."),
             ("The sense 'in'", "'In' would need a locative such as पद्मिनीपत्रे."),
             ("The sense 'from'", "'From' would need an ablative such as पद्मिनीपत्रात्.")],
            "-वत् here makes a comparison: like a lotus leaf.",
            "-वत् = like."),
        mcq("apply", 4, "Why is षण्मासाः printed षण्मासास् before तस्य in unit 40?",
            ("Visarga before त becomes स्", "त is a voiceless dental: षण्मासाः + तस्य → षण्मासास्तस्य."),
            [("Visarga before त becomes श्", "श् comes before च, छ or श, not before त."),
             ("Visarga before त becomes र्", "र् comes after a vowel other than अ/आ before a voiced sound; त is voiceless."),
             ("Visarga before any letter is स्", "Not any: before च it becomes श्, and before a voiced sound आः drops it.")],
            "षण्मासाः + तस्य: visarga before त → स्.",
            "ः + त → स्त."),
        mcq("transfer", 5, "By the pattern of षण्मासाः + तस्य → षण्मासास्तस्य, how is नराः + तत्र (the men there) joined in a new example?",
            ("नरास्तत्र", "Visarga before त becomes स्: नराः + तत्र → नरास्तत्र."),
            [("नरा तत्र", "आः drops its visarga only before a voiced sound; त is voiceless."),
             ("नराश्तत्र", "श् comes before च, छ or श, not before त."),
             ("नरोतत्र", "ओ comes from अः before a voiced consonant; here the vowel is आ and त is voiceless.")],
            "नराः + तत्र = नरास्तत्र, like षण्मासाः + तस्य = षण्मासास्तस्य.",
            "ः + त → स्त.",
            teaches="A visarga before त or थ becomes स्: षण्मासाः + तस्य → षण्मासास्तस्य."),
    ],
}

# ---------------------------------------------------------------- unit 41
AUTHORED["41"] = {
    "title": "हरिताभाः सिरा यस्य",
    "question": "By unit 41, which three signs show that a man will meet death from Pitta?",
    "rule": ("He whose veins (सिराः) look greenish (हरिताभाः) and whose hair pores (रोमकूपाः) are closed (संवृताः), that man, "
             "craving the sour (अम्लाभिलाषी), meets death from Pitta (पित्तात्)."),
    "limits": ("संवृत can mean closed or covered; 'closed' is the data's choice. हरित = green or yellowish-green. The verse names "
               "no time span and no treatment. 'यस्यरोमकूपाश्च' is printed without spaces (no letter changed)."),
    "explain_hi": ("यह श्लोक दो छपी पंक्तियों (०२.०९.४९ और ०२.०९.५०) का एक वाक्य है। "
                   "जिसकी सिराएँ हरी-सी आभा वाली हों और रोमकूप बन्द हों, वह खट्टे (अम्ल) की इच्छा करने वाला पुरुष पित्त से मृत्यु को प्राप्त होता है। "
                   "‘पित्तात्’ पञ्चमी है: पित्त के कारण। "
                   "‘संवृत’ का अर्थ बन्द या ढका हुआ हो सकता है; डेटा ‘बन्द’ लेता है। "
                   "‘सोऽम्लाभिलाषी’ में सः + अम्ल की सन्धि है: अः + अ → ओऽ।"),
    "hook": "हरी सिराएँ, बन्द रोमकूप, खट्टे की चाह: पित्त से मृत्यु।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 41, from which doṣa does the man with these signs meet death?",
            ("From Pitta", "पित्तान्मरणमश्नुते: he attains death from Pitta (पित्तात्, ablative)."),
            [("From Vāta", "The verse says पित्तात्, not वातात्."),
             ("From Kapha", "The verse says पित्तात्, not कफात्."),
             ("From all three", "Only one doṣa is named: पित्तात्.")],
            "पित्तात् = from Pitta.",
            "पित्तात् (ablative) = from Pitta."),
        order(1, "Put the signs and the outcome of unit 41 in the printed order.",
              ["हरिताभाः सिरा", "रोमकूपाश्च संवृताः", "अम्लाभिलाषी", "पित्तान्मरणमश्नुते"],
              "Greenish veins; closed hair pores; craving the sour; he attains death from Pitta.",
              "सिराः → रोमकूपाः → अम्लाभिलाषी → पित्तात् मरणम्."),
        match(2, "Match each word of unit 41 to its meaning.",
              [["हरित", "greenish"], ["सिरा", "vein"], ["रोमकूप", "hair pore"], ["संवृत", "closed, covered"],
               ["अम्ल", "sour"], ["अश्नुते", "attains"]],
              "हरित = greenish, सिरा = vein, रोमकूप = hair pore, संवृत = closed, अम्ल = sour, अश्नुते = attains.",
              "हरित, सिरा, रोमकूप, संवृत, अम्ल, अश्नुते.", role="extend",
              teaches="हरिताभाः is a bahuvrīhi: 'whose appearance (आभा) is greenish', said of the veins."),
        mcq("discriminate", 3, "Which split of सोऽम्लाभिलाषी in unit 41 is right?",
            ("सः + अम्ल + अभिलाषी", "अः + अ → ओऽ; अ + अ → आ: सोऽम्लाभिलाषी."),
            [("सो + अम्ल + अभिलाषी", "सो is not a word; the ओ comes from the visarga of सः before अ."),
             ("सः + म्ला + अभिलाषी", "म्ला is not a word; the अ of अम्ल is shown by the avagraha ऽ."),
             ("सः + अम्ला + भिलाषी", "भिलाषी is not a word; the word is अभिलाषी (craving).")],
            "सः (that) + अम्ल (sour) + अभिलाषी (craving).",
            "अः + अ → ओऽ."),
        multi("apply", 4, "Which signs does unit 41 name for the man who dies from Pitta?",
              [("Veins of greenish appearance", "Named: हरिताभाः सिराः."),
               ("A craving for sweet food", "Not named: the craving is for the sour (अम्ल)."),
               ("Hair pores that are closed", "Named: रोमकूपाः संवृताः."),
               ("A craving for the sour", "Named: अम्लाभिलाषी."),
               ("Hair pores wide open", "Not named: the pores are closed, संवृताः.")],
              [0, 2, 3],
              "Three signs: greenish veins, closed hair pores, craving the sour.",
              "हरिताभाः सिराः, रोमकूपाः संवृताः, अम्लाभिलाषी."),
        mcq("transfer", 5, "By the pattern of सः + अम्ल- → सोऽम्ल-, how is रामः + अपि (Rāma too) joined in a new example?",
            ("रामोऽपि", "अः before अ → ओ, and the अ is shown by ऽ: रामः + अपि → रामोऽपि."),
            [("रामरपि", "र् comes from a visarga after a vowel other than अ/आ; here the vowel is अ."),
             ("रामापि", "The visarga does not vanish into a long आ; अः + अ gives ओऽ."),
             ("राम अपि", "अः drops to अ only before vowels other than अ; before अ it gives ओऽ.")],
            "रामः + अपि = रामोऽपि, like सः + अम्ल- = सोऽम्ल-.",
            "अः + अ → ओऽ.",
            teaches="अः before अ becomes ओ and the अ is marked by avagraha (ऽ): सः + अम्ल- → सोऽम्ल-."),
    ],
}

# ---------------------------------------------------------------- unit 42
AUTHORED["42"] = {
    "title": "यस्य गोमयचूर्णाभं",
    "question": "By unit 42, what signs on the head or the face does the verse name?",
    "rule": ("He on whose head (मूर्ध्नि), or even on the face (मुखेऽपि वा), there is powder like cow-dung powder "
             "(गोमयचूर्णाभं चूर्ण), or oily smoke (सस्नेहं धूमः) on the head: the verse then gives his span of life."),
    "limits": ("Printed चूर्ण is probably चूर्णम् (final म् dropped). वामासांतं = वा + मासान्तम् ('up to the end of a month') is "
               "the data's reading and another division is possible: no question on the life span. सस्नेहं is taken as an adverb."),
    "explain_hi": ("यह श्लोक दो छपी पंक्तियों (०२.०९.५१ और ०२.०९.५२) का एक वाक्य है। "
                   "जिसके सिर पर अथवा मुख पर भी गोबर के चूर्ण जैसा चूर्ण दिखे, या सिर पर चिकनाई वाला धुआँ, उसके जीवन की अवधि श्लोक बताता है। "
                   "डेटा ‘वामासांतं’ को वा + मासान्तम् (मास के अन्त तक) पढ़ता है, पर दूसरा विभाजन भी सम्भव है; इसलिए अवधि पर प्रश्न नहीं। "
                   "छपा ‘चूर्ण’ सम्भवतः ‘चूर्णम्’ है। "
                   "‘मुखेऽपि’ में ए + अ → एऽ और ‘धूमो’ में घोष व्यंजन व से पहले अः → ओ।"),
    "hook": "सिर-मुख पर गोबर-सा चूर्ण, या सिर पर चिकना धुआँ।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 42, what does the powder on the head or face look like?",
            ("Cow-dung powder", "गोमयचूर्णाभम्: resembling powder of cow dung (गोमय)."),
            [("Burnt wood ash", "No ash is named; the verse says गोमय, cow dung."),
             ("Fine white sand", "No sand is named; the verse says गोमय, cow dung."),
             ("Ground red clay", "No clay is named; the verse says गोमय, cow dung.")],
            "गोमय (cow dung) + चूर्ण (powder) + आभ (resembling).",
            "गोमयचूर्णाभ = like cow-dung powder."),
        order(1, "Put these phrases of unit 42 in the printed order.",
              ["यस्य गोमयचूर्णाभं", "चूर्ण मूर्ध्नि", "मुखेऽपि वा", "सस्नेहं मूर्ध्नि धूमो", "तस्य जीवितं"],
              "Of whom, resembling cow-dung powder; powder on the head; or even on the face; oily smoke on the head; his life.",
              "गोमयचूर्णाभं → चूर्ण → मुखेऽपि वा → सस्नेहं धूमः → तस्य जीवितं."),
        match(2, "Match each word of unit 42 to its meaning.",
              [["गोमय", "cow dung"], ["चूर्ण", "powder"], ["मूर्धन्", "head"], ["मुख", "face"],
               ["स्नेह", "oiliness"], ["धूम", "smoke"]],
              "गोमय = cow dung, चूर्ण = powder, मूर्धन् = head, मुख = face, स्नेह = oiliness, धूम = smoke.",
              "गोमय, चूर्ण, मूर्धन्, मुख, स्नेह, धूम.", role="extend",
              teaches="मूर्ध्नि is the locative singular of मूर्धन् (head): 'on the head'."),
        mcq("discriminate", 3, "Which split of मुखेऽपि in unit 42 is right?",
            ("मुखे + अपि", "ए + अ → ए, the अ marked by ऽ: मुखे + अपि → मुखेऽपि."),
            [("मुख + इपि", "इपि is not a word, and अ + इ would give ए without ऽ."),
             ("मुखा + अपि", "आ + अ would give मुखापि, with no ए."),
             ("मुखो + अपि", "मुखो is not a form here, and it would give ओऽ, not एऽ.")],
            "मुखे (on the face) + अपि (even).",
            "ए + अ → एऽ."),
        mcq("apply", 4, "Why is धूमः printed धूमो in unit 42?",
            ("अः before a voiced consonant → ओ", "The next letter व is a voiced consonant: धूमः + व... → धूमो."),
            [("Visarga before any consonant → ओ", "Not any: before त it becomes स् (षण्मासास्तस्य, unit 40)."),
             ("आः before a voiced consonant → ओ", "आः drops its visarga before a voiced sound; and धूमः ends in अः."),
             ("ओ is the noun's own ending", "धूमः is the nominative; ओ comes only from sandhi.")],
            "धूमः before व: अः before a voiced consonant → ओ.",
            "अः + voiced consonant → ओ."),
        mcq("transfer", 5, "By the pattern of मुखे + अपि → मुखेऽपि, how is वने + अस्ति (it is in the forest) joined in a new example?",
            ("वनेऽस्ति", "A final ए before अ stays, and the अ is marked by ऽ: वनेऽस्ति."),
            [("वनयस्ति", "ए → अय् comes before vowels other than अ; before अ it stays ए with ऽ."),
             ("वनास्ति", "आ would come from अ + अ; here the first vowel is ए."),
             ("वनोऽस्ति", "ओऽ comes from अः + अ; here the word ends in ए.")],
            "वने + अस्ति = वनेऽस्ति, like मुखे + अपि = मुखेऽपि.",
            "ए + अ → एऽ.",
            teaches="A word-final ए before अ stays ए, and the lost अ is marked by avagraha: मुखे + अपि → मुखेऽपि."),
    ],
}

# ---------------------------------------------------------------- unit 43
AUTHORED["43"] = {
    "title": "मूर्ध्नि भ्रुवोर्वा कुर्वंति",
    "question": "By unit 43, where do the new marks appear, and for whom does the unit give two different times?",
    "rule": ("New marks (सीमंतावर्तका नवाः) on the head (मूर्ध्नि) or on the two eyebrows (भ्रुवोः) bring death (मृत्युं "
             "कुर्वन्ति); the unit sets one time for a healthy person (स्वस्थस्य) and another for a sick one (आतुरस्य)."),
    "limits": ("Low confidence; prose by the data. The numbers rest on the flagged 'षडरात्रान्' (ṣaḍrātrāt is a conjecture): no "
               "question on the nights. सीमन्तावर्तक ('partings and whorls') is not firm: no question on its sense. Which "
               "night counts is not stated."),
    "explain_hi": ("यह गद्य इकाई (डेटा के अनुसार) दो छपी पंक्तियों (०२.०९.५३ और ०२.०९.५४) का एक वाक्य है; विश्वास कम। "
                   "सिर पर अथवा दोनों भौंहों पर नए सीमन्तावर्तक (डेटा: माँग और भँवर जैसे चिह्न, अर्थ पक्का नहीं) मृत्यु करते हैं। "
                   "स्वस्थ व्यक्ति के लिए एक अवधि और रोगी (आतुर) के लिए दूसरी अवधि कही गई है; डेटा इन्हें छह रात और तीन रात पढ़ता है, पर छपा ‘षडरात्रान्’ अनुमानित सुधार माँगता है, इसलिए रातों पर प्रश्न नहीं। "
                   "‘भ्रुवोर्वा’ में भ्रुवोः + वा: अ/आ के अलावा स्वर के बाद विसर्ग घोष व्यंजन से पहले र् बनता है।"),
    "hook": "सिर या भौंहों पर नए चिह्न: स्वस्थ और आतुर की अलग अवधि।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 43, what does आतुर mean?",
            ("A sick person", "आतुरस्य = of a sick person; it is set against स्वस्थस्य."),
            [("A healthy person", "That is स्वस्थ, the other person of this unit."),
             ("A young child", "A child would be बाल; आतुर means sick."),
             ("A wise doctor", "A doctor would be वैद्य or भिषक्; आतुर means sick.")],
            "आतुर = sick; स्वस्थ = healthy.",
            "आतुर = a sick person."),
        order(1, "Put these printed words of unit 43 in the printed order.",
              ["मूर्ध्नि", "भ्रुवोर्वा", "कुर्वंति", "नवाः", "मृत्युं"],
              "On the head; or on the two eyebrows; make; new (marks); death.",
              "मूर्ध्नि → भ्रुवोर्वा → कुर्वंति → नवाः → मृत्युं."),
        match(2, "Match each sure word of unit 43 to its meaning.",
              [["मूर्धन्", "head"], ["भ्रू", "eyebrow"], ["नव", "new"], ["मृत्यु", "death"],
               ["स्वस्थ", "healthy person"], ["आतुर", "sick person"]],
              "मूर्धन् = head, भ्रू = eyebrow, नव = new, मृत्यु = death, स्वस्थ = healthy, आतुर = sick.",
              "मूर्धन्, भ्रू, नव, मृत्यु, स्वस्थ, आतुर.", role="extend",
              teaches="मृत्युं is the object of कुर्वन्ति in the first printed line: the marks 'make death'."),
        mcq("discriminate", 3, "Why is भ्रुवोः printed भ्रुवोर् before वा in unit 43?",
            ("After ओ, visarga before व → र्", "After a vowel other than अ/आ, a visarga before a voiced sound becomes र्."),
            [("After ओ, visarga before व → स्", "स् comes before त or थ; व is voiced and gives र् here."),
             ("र् is part of the stem भ्रुवोर्", "The stem is भ्रू; the र् comes only from sandhi."),
             ("After ओ, visarga before व drops", "It drops after आ before a voiced sound; after ओ it gives र्.")],
            "भ्रुवोः + वा → भ्रुवोर्वा: ओ + ः before the voiced व → ओर्.",
            "Vowel other than अ/आ + ः before a voiced sound → र्."),
        mcq("apply", 4, "By unit 43, where do the new marks appear?",
            ("On the head or the eyebrows", "मूर्ध्नि भ्रुवोर्वा: on the head or on the two eyebrows."),
            [("On the chest or the shoulders", "Chest and shoulders are not named in this unit."),
             ("On the palms or the soles", "Palms and soles are not named in this unit."),
             ("On the lips or the chin", "Lips and chin are not named in this unit.")],
            "मूर्ध्नि (on the head) भ्रुवोः (on the two eyebrows) वा (or).",
            "मूर्ध्नि भ्रुवोर्वा."),
        mcq("transfer", 5, "By the pattern of भ्रुवोः + वा → भ्रुवोर्वा, how is गुरोः + वचनम् (the teacher's word) joined in a new example?",
            ("गुरोर्वचनम्", "After ओ, a visarga before the voiced व becomes र्."),
            [("गुरोस्वचनम्", "स् comes from a visarga before त or थ, not before व."),
             ("गुरोश्वचनम्", "श् comes from a visarga before च, छ or श, not before व."),
             ("गुरो वचनम्", "The visarga drops before a voiced sound only after आ; after ओ it gives र्.")],
            "गुरोः + वचनम् = गुरोर्वचनम्, like भ्रुवोः + वा = भ्रुवोर्वा.",
            "Vowel other than अ/आ + ः before a voiced sound → र्.",
            teaches="After a vowel other than अ or आ, a visarga before a vowel or a voiced consonant becomes र्: भ्रुवोः + वा → भ्रुवोर्वा."),
    ],
}

# ---------------------------------------------------------------- unit 44
AUTHORED["44"] = {
    "title": "यस्य स्नातानुलिप्तस्य",
    "question": "By unit 44, what happens to the chest after bathing and anointing, and what does it foretell?",
    "rule": ("He whose chest (उरः) dries up first (पूर्वं) and greatly (भृशं) when he has bathed and been anointed "
             "(स्नातानुलिप्तस्य) does not live half a month (अर्द्धमासं न जीवति)."),
    "limits": ("'While all the limbs are wet' rests on the conjecture ārdreṣu for the printed आर्द्वेषु: no question on 'wet'. "
               "पूर्वम् = first (also possibly 'ahead'). The verse names no cause and no treatment."),
    "explain_hi": ("यह श्लोक दो छपी पंक्तियों (०२.०९.५५ और ०२.०९.५६) का एक वाक्य है। "
                   "जिसकी छाती स्नान करने और लेप लगाने के बाद सबसे पहले और बहुत सूख जाती है, वह आधा मास नहीं जीता। "
                   "छपा ‘आर्द्वेषु’ कोई शब्द नहीं; ‘आर्द्रेषु’ (गीले रहते) अनुमानित पाठ है, इसलिए ‘गीले अंग’ पर प्रश्न नहीं। "
                   "‘शुष्यत्युरो’ में शुष्यति + उरः: इ + उ → यु, और भ से पहले अः → ओ। "
                   "‘सोऽर्द्धमासं’ में छपाई ‘र्द्ध’ लिखती है, जो ‘र्ध’ ही है।"),
    "hook": "नहाने-लेप के बाद छाती पहले सूखे: आधा मास भी नहीं।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 44, which part dries first after bathing and anointing?",
            ("The chest", "शुष्यत्युरः: the chest (उरः) dries up first and greatly."),
            [("The scalp", "The verse names उरः, the chest, not the head."),
             ("The palms", "The verse names उरः, the chest, not the hands."),
             ("The soles", "The verse names उरः, the chest, not the feet.")],
            "उरः = chest; शुष्यति = dries.",
            "उरस् = chest."),
        order(1, "Put these words of unit 44 in the printed order.",
              ["स्नातानुलिप्तस्य", "पूर्वं", "शुष्यत्युरो", "भृशं", "सर्वगात्रेषु"],
              "Of one bathed and anointed; first; the chest dries; greatly; in all the limbs.",
              "स्नातानुलिप्तस्य → पूर्वं → शुष्यत्युरो → भृशं → सर्वगात्रेषु."),
        match(2, "Match each word of unit 44 to its meaning.",
              [["स्नात", "bathed"], ["अनुलिप्त", "anointed"], ["उरस्", "chest"], ["भृशम्", "greatly"],
               ["सर्वगात्र", "all the limbs"], ["अर्धमास", "half a month"]],
              "स्नात = bathed, अनुलिप्त = anointed, उरस् = chest, भृशम् = greatly, सर्वगात्र = all the limbs, अर्धमास = half a month.",
              "स्नात, अनुलिप्त, उरस्, भृशम्, सर्वगात्र, अर्धमास.", role="extend",
              teaches="स्नातानुलिप्त joins two past participles: one who has bathed and then been anointed."),
        mcq("discriminate", 3, "Which split of शुष्यत्युरो in unit 44 is right?",
            ("शुष्यति + उरः", "इ before a different vowel → य्: शुष्यति + उरः → शुष्यत्युरः, and before भ → उरो."),
            [("शुष्यत् + युरः", "युरः is not a word; the य् comes from the इ of शुष्यति."),
             ("शुष्य + त्युरः", "त्युरः is not a word; शुष्यति is one verb."),
             ("शुष्यते + उरः", "ए + उ would give अयु (शुष्यतयुरः), not यु.")],
            "शुष्यति (dries) + उरः (chest).",
            "इ + unlike vowel → य्."),
        mcq("apply", 4, "By unit 44, what does the verse foretell for him?",
            ("He does not live half a month", "सोऽर्द्धमासं न जीवति: he does not live half a month."),
            [("He lives on for a full half-year", "No half year is named; the verse says half a month, with न."),
             ("He recovers in half a month", "The verse says न जीवति, he does not live."),
             ("He dies on the very same day", "No same-day death is named; the span is half a month.")],
            "अर्द्धमासं न जीवति: not (even) half a month.",
            "न जीवति = does not live."),
        mcq("transfer", 5, "By the pattern of शुष्यति + उरः → शुष्यत्युरः, how is इति + उक्तम् (thus said) joined in a new example?",
            ("इत्युक्तम्", "इ before a different vowel → य्: इति + उक्तम् → इत्युक्तम्."),
            [("इतोक्तम्", "ओ comes from अ + उ; here the first vowel is इ."),
             ("इतीक्तम्", "ई comes from इ + इ; here the second vowel is उ."),
             ("इतियुक्तम्", "The इ itself becomes य्; it does not stay with an added य्.")],
            "इति + उक्तम् = इत्युक्तम्, like शुष्यति + उरः = शुष्यत्युरः.",
            "इ + unlike vowel → य्.",
            teaches="इ before a different vowel becomes य्: शुष्यति + उरः → शुष्यत्युरः."),
    ],
}

# ---------------------------------------------------------------- unit 45
AUTHORED["45"] = {
    "title": "उरस्यूष्मा भवेद्यस्य",
    "question": "By unit 45, which opposite signs of chest and belly, with what else, make a man 'like a departed one'?",
    "rule": ("He in whose chest there is heat (उरसि ऊष्मा) and in the belly excessive coldness (जठरे अतिशीतता), with "
             "broken stool (भिन्नं पुरीषं; probably loose) and thirst (तृष्णा): as a departed one (प्रेतः), so is he."),
    "limits": ("भिन्न पुरीष is kept literal ('broken' stool); 'loose' is probable, not stated. प्रेत = a departed one, a dead "
               "person. The verse gives no time span. Printed जठरे अतिशीतता is not joined by sandhi."),
    "explain_hi": ("यह श्लोक दो छपी पंक्तियों (०२.०९.५७ और ०२.०९.५८) का एक वाक्य है। "
                   "जिसकी छाती में गर्मी और जठर (पेट) में अत्यन्त ठण्डक हो, मल भिन्न (टूटा हुआ, सम्भवतः ढीला) हो और प्यास हो, वह जैसे प्रेत, वैसे ही है। "
                   "छाती की गर्मी और पेट की ठण्डक इसी श्लोक की विपरीत जोड़ी है। "
                   "‘उरस्यूष्मा’ में इ + ऊ → यू, ‘भवेद्यस्य’ में घोष य से पहले त् → द्, और ‘तथैव’ में आ + ए → ऐ।"),
    "hook": "छाती गर्म, पेट ठण्डा, मल भिन्न, प्यास: प्रेत-समान।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 45, where is the heat (ऊष्मा) of this sign?",
            ("In the chest", "उरसि ऊष्मा: heat in the chest."),
            [("In the belly", "The belly (जठर) has excessive coldness, not heat."),
             ("In the feet", "The feet are not named; the heat is in उरस्."),
             ("In the hands", "The hands are not named; the heat is in उरस्.")],
            "उरसि = in the chest; ऊष्मा = heat.",
            "उरस्यूष्मा = heat in the chest."),
        order(1, "Put the signs of unit 45 in the printed order.",
              ["उरस्यूष्मा", "जठरे अतिशीतता", "भिन्नं पुरीषं", "तृष्णा", "यथा प्रेतः"],
              "Heat in the chest; excessive coldness in the belly; broken stool; thirst; as a departed one.",
              "ऊष्मा → अतिशीतता → भिन्नं पुरीषं → तृष्णा → यथा प्रेतः."),
        match(2, "Match each word of unit 45 to its meaning.",
              [["उरस्", "chest"], ["ऊष्मन्", "heat"], ["जठर", "belly"], ["शीतता", "coldness"],
               ["पुरीष", "stool"], ["तृष्णा", "thirst"]],
              "उरस् = chest, ऊष्मन् = heat, जठर = belly, शीतता = coldness, पुरीष = stool, तृष्णा = thirst.",
              "उरस्, ऊष्मन्, जठर, शीतता, पुरीष, तृष्णा.", role="extend",
              teaches="यथा ... तथा एव sets up a comparison: 'as a departed one, just so is he'."),
        mcq("discriminate", 3, "Which split of उरस्यूष्मा in unit 45 is right?",
            ("उरसि + ऊष्मा", "इ before a different vowel → य्: उरसि + ऊष्मा → उरस्यूष्मा."),
            [("उरस् + यूष्मा", "यूष्मा is not a word; the य् comes from the इ of उरसि."),
             ("उरसा + ऊष्मा", "आ + ऊ would give ओ (उरसोष्मा), not यू."),
             ("उरस्य + ऊष्मा", "अ + ऊ would give ओ (उरस्योष्मा), not यू.")],
            "उरसि (in the chest) + ऊष्मा (heat).",
            "इ + unlike vowel → य्."),
        mcq("apply", 4, "By unit 45, what does यथा प्रेतस्तथैव सः say of the man?",
            ("He is like a departed one", "यथा प्रेतः तथा एव सः: as a departed one, so indeed is he."),
            [("He has seen a departed one", "No seeing is stated; it is a comparison, यथा ... तथा."),
             ("He must keep off the dead", "No avoiding is stated here; it is a comparison."),
             ("He will be reborn a preta", "No rebirth is stated; it is a comparison.")],
            "यथा ... तथैव: as ..., just so.",
            "यथा प्रेतः तथा एव सः."),
        mcq("transfer", 5, "By the pattern of तथा + एव → तथैव, how is न + एव (not at all) joined in a new example?",
            ("नैव", "अ + ए → ऐ: न + एव → नैव."),
            [("नौव", "औ comes from अ/आ + ओ or औ; here the second vowel is ए."),
             ("नयेव", "No य् is put between अ and ए; they merge into ऐ."),
             ("नोव", "ओ comes from अ/आ + उ; here the second vowel is ए.")],
            "न + एव = नैव, like तथा + एव = तथैव.",
            "अ/आ + ए → ऐ.",
            teaches="अ or आ before ए or ऐ gives ऐ: तथा + एव → तथैव."),
    ],
}

# ---------------------------------------------------------------- unit 46
AUTHORED["46"] = {
    "title": "मूत्रं पुरीषं निष्ठ्यूतं",
    "question": "By unit 46, which four things sink in water, and what is the second sign about sputum?",
    "rule": ("When urine, stool, sputum and semen (मूत्रं पुरीषं निष्ठ्यूतं शुक्रं) sink in water (अप्सु निमज्जति), or "
             "when one's sputum is of many colours (बहुवर्णं), he perishes (नश्यति)."),
    "limits": ("Printed मासान्स is read māsān saḥ ('in months', no number); māsāt saḥ ('after a month') is also possible: "
               "no question on the time. Whose excreta are meant is not said; the sense is of the person described."),
    "explain_hi": ("यह श्लोक दो छपी पंक्तियों (०२.०९.५९ और ०२.०९.६०) से बना है। "
                   "मूत्र, मल, निष्ठ्यूत (थूक) और शुक्र (वीर्य) पानी में डूबें, या जिसका थूक अनेक रंगों का हो, वह नष्ट होता है। "
                   "चार नपुंसक कर्ता एक एकवचन क्रिया ‘निमज्जति’ के साथ एक समूह की तरह लिए गए हैं। "
                   "समय: छपा ‘मासान्स’ (मासों में, संख्या नहीं) और ‘मासात् सः’ (एक मास के बाद) दोनों सम्भव हैं, इसलिए समय पर प्रश्न नहीं। "
                   "‘चाप्सु’ में च + अप्सु: अ + अ → आ।"),
    "hook": "चारों पानी में डूबें, या थूक रंग-बिरंगा: नाश।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 46, what happens to urine, stool, sputum and semen in water?",
            ("They sink", "अप्सु निमज्जति: they sink in water."),
            [("They float", "The verb is निमज्जति, sinks, not floats."),
             ("They melt", "The verb is निमज्जति, sinks, not melts."),
             ("They foam", "The verb is निमज्जति, sinks, not foams.")],
            "निमज्जति = sinks; अप्सु = in water.",
            "अप्सु निमज्जति = sinks in water."),
        order(1, "Put the four things of unit 46 that sink in water in the printed order.",
              ["मूत्रं", "पुरीषं", "निष्ठ्यूतं", "शुक्रं"],
              "Urine; stool; sputum; semen.",
              "मूत्रं → पुरीषं → निष्ठ्यूतं → शुक्रं."),
        match(2, "Match each word of unit 46 to its meaning.",
              [["मूत्र", "urine"], ["पुरीष", "stool"], ["निष्ठ्यूत", "sputum, spittle"], ["शुक्र", "semen"],
               ["अप्सु", "in water"], ["निमज्जति", "sinks"]],
              "मूत्र = urine, पुरीष = stool, निष्ठ्यूत = sputum, शुक्र = semen, अप्सु = in water, निमज्जति = sinks.",
              "मूत्र, पुरीष, निष्ठ्यूत, शुक्र, अप्सु, निमज्जति.", role="extend",
              teaches="अप्सु is the locative plural of अप् (water), a noun used in the plural: 'in water'."),
        mcq("discriminate", 3, "Which split of चाप्सु in unit 46 is right?",
            ("च + अप्सु", "अ + अ → आ: च + अप्सु → चाप्सु."),
            [("चा + प्सु", "चा and प्सु are not words; the word is अप्सु."),
             ("च + आप्सु", "आप्सु is not a form; the locative plural of अप् is अप्सु."),
             ("चाप् + सु", "चाप् is not the word here; च (and) + अप्सु (in water).")],
            "च (and) + अप्सु (in water).",
            "अ + अ → आ."),
        mcq("apply", 4, "By unit 46, what is the second sign, about the sputum?",
            ("It is of many colours", "निष्ठ्यूतं बहुवर्णं वा: or the sputum is of many colours."),
            [("It is thick and sticky", "Thickness is not named; the word is बहुवर्ण."),
             ("It smells foul", "No smell is named; the word is बहुवर्ण."),
             ("It is very hot", "No heat is named; the word is बहुवर्ण.")],
            "बहु (many) + वर्ण (colour): of many colours.",
            "बहुवर्ण = many-coloured."),
        mcq("transfer", 5, "By the pattern of च + अप्सु → चाप्सु, how is न + अस्ति (is not) joined in a new example?",
            ("नास्ति", "अ + अ → आ: न + अस्ति → नास्ति."),
            [("नेस्ति", "ए comes from अ + इ; here the second vowel is अ."),
             ("नोस्ति", "ओ comes from अ + उ; here the second vowel is अ."),
             ("नयस्ति", "अय् comes from ए before a vowel; here the first vowel is अ.")],
            "न + अस्ति = नास्ति, like च + अप्सु = चाप्सु.",
            "अ + अ → आ.",
            teaches="अ + अ gives the long आ: च + अप्सु → चाप्सु."),
    ],
}

# ---------------------------------------------------------------- unit 47
AUTHORED["47"] = {
    "title": "स्वरस्य दुर्बलीभावं",
    "question": "By unit 47, having seen which signs should one foretell death?",
    "rule": ("Having seen (दृष्ट्वा) the weakening of the voice (स्वरस्य दुर्बलीभावं), the loss of strength and colour "
             "(हानिं बलवर्णयोः) and the increase of disease without reason (रोगवृद्धिम् अयुक्त्या), one should foretell death."),
    "limits": ("अयुक्त्या = 'without reason'; 'by improper means' is also possible: no question rests on its exact sense. "
               "वर्ण = colour or complexion. Who foretells is not stated ('one')."),
    "explain_hi": ("यह श्लोक दो छपी पंक्तियों (०२.०९.६१ और ०२.०९.६२) का एक वाक्य है। "
                   "स्वर की दुर्बलता, बल और वर्ण (रंग) की हानि, और बिना युक्ति के रोग की वृद्धि देखकर मृत्यु बता दे। "
                   "‘अयुक्त्या’ का अर्थ ‘बिना कारण’ है; ‘अनुचित उपाय से’ भी सम्भव है। "
                   "‘दृष्ट्वा’ क्त्वा-प्रत्यय वाला रूप है (देखकर), और ‘आदिशेत्’ विधिलिङ् (बताए)।"),
    "hook": "स्वर कमज़ोर, बल-वर्ण घटे, रोग बढ़े: मृत्यु बताए।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 47, what has happened to the voice?",
            ("It has weakened", "स्वरस्य दुर्बलीभावम्: the weakening of the voice."),
            [("It has become loud", "Loudness is not named; the voice has become weak."),
             ("It is sweeter", "Sweetness is not named; the voice has become weak."),
             ("It is higher", "Pitch is not named; the voice has become weak.")],
            "दुर्बल (weak) + भाव (state): weakening.",
            "दुर्बलीभाव = weakening."),
        order(1, "Put these phrases of unit 47 in the printed order.",
              ["स्वरस्य दुर्बलीभावं", "हानिं च बलवर्णयोः", "रोगवृद्धिमयुक्त्या च", "दृष्ट्वा", "मरणमादिशेत्"],
              "Weakening of the voice; loss of strength and colour; increase of disease without reason; having seen; should foretell death.",
              "स्वर → बल-वर्ण → रोगवृद्धि → दृष्ट्वा → मरणम् आदिशेत्."),
        match(2, "Match each word of unit 47 to its meaning.",
              [["स्वर", "voice"], ["दुर्बलीभाव", "weakening"], ["हानि", "loss"], ["बल", "strength"],
               ["वर्ण", "colour"], ["आदिशेत्", "should foretell"]],
              "स्वर = voice, दुर्बलीभाव = weakening, हानि = loss, बल = strength, वर्ण = colour, आदिशेत् = should foretell.",
              "स्वर, दुर्बलीभाव, हानि, बल, वर्ण, आदिशेत्.", role="extend",
              teaches="बलवर्णयोः is a dvandva in the genitive dual: 'of strength and colour'."),
        mcq("discriminate", 3, "In unit 47, what form is दृष्ट्वा?",
            ("Absolutive: having seen", "दृष्ट्वा (-त्वा) = having seen; the seeing comes before the foretelling."),
            [("Infinitive: to see", "The infinitive would be द्रष्टुम्."),
             ("Past participle: seen", "The past participle would be दृष्ट."),
             ("Optative: should see", "An optative would be पश्येत्; the optative here is आदिशेत्.")],
            "दृष्ट्वा = having seen.",
            "-त्वा = having done."),
        multi("apply", 4, "Which signs does unit 47 list before one foretells death?",
              [("Loss of hearing", "Not listed: hearing is not named in this unit."),
               ("Weakening of the voice", "Listed: स्वरस्य दुर्बलीभावम्."),
               ("Loss of strength and colour", "Listed: हानिं बलवर्णयोः."),
               ("Loss of sleep", "Not listed: sleep is not named in this unit."),
               ("Increase of disease", "Listed: रोगवृद्धिम्.")],
              [1, 2, 4],
              "Three signs: weak voice, loss of strength and colour, increase of disease.",
              "स्वर, बल-वर्ण, रोगवृद्धि."),
        mcq("transfer", 5, "By the pattern of दृष्ट्वा (having seen), what does श्रुत्वा mean in a new example?",
            ("Having heard", "-त्वा = having done: श्रुत्वा = having heard."),
            [("To hear", "'To hear' would be the infinitive श्रोतुम्."),
             ("One who hears", "'One who hears' would be श्रोतृ."),
             ("Was heard", "'Was heard' would be a passive such as श्रुतः.")],
            "श्रुत्वा = having heard, like दृष्ट्वा = having seen.",
            "-त्वा = having done.",
            teaches="The absolutive in -त्वा means 'having done': दृष्ट्वा = having seen."),
    ],
}

# ---------------------------------------------------------------- unit 48
AUTHORED["48"] = {
    "title": "अपस्वरं भाषमाणं",
    "question": "By unit 48, which sure words describe the one speaking, and how is one told to keep away?",
    "rule": ("One speaking (भाषमाणं) in a faulty voice (अपस्वरं) ... one should avoid from afar (दूरतः परिवर्जयेत्); the "
             "hearer (श्रोतारं) of his sound is also named."),
    "limits": ("Low confidence. That परिवर्जयेत् governs the accusatives of the first line is probable, not stated. प्राप्तं may "
               "go with the person or with मरणम्: no question on it. चास्यशब्दस्य divides two ways (asya / āsya): no "
               "question on it. Who 'the hearer' is is unclear."),
    "explain_hi": ("यह श्लोक दो छपी पंक्तियों (०२.०९.६३ और ०२.०९.६४) से बना है; विश्वास कम। "
                   "बिगड़े स्वर (अपस्वर) में बोलने वाले को, और उसके शब्द के श्रोता को, दूर से त्याग दे, यह डेटा का सम्भावित पाठ है। "
                   "‘प्राप्तं मरणमात्मनः’ का व्याकरण पक्का नहीं: ‘प्राप्तं’ व्यक्ति के साथ या ‘मरणम्’ के साथ जा सकता है। "
                   "‘चास्यशब्दस्य’ को च + अस्य + शब्दस्य या च + आस्य-शब्दस्य (मुख का शब्द) दोनों तरह पढ़ा जा सकता है। "
                   "पक्के शब्द: अपस्वर, भाषमाण (बोलता हुआ), दूरतः (दूर से), परिवर्जयेत् (त्याग दे)।"),
    "hook": "बिगड़ा स्वर: दूर से ही परिवर्जन।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 48, what does अपस्वर mean?",
            ("A faulty voice", "अप- (bad, away) + स्वर (voice): a faulty voice."),
            [("A pleasant voice", "Pleasant would be मधुर; अप- marks something faulty."),
             ("A clear voice", "Clear would be स्पष्ट; अप- marks something faulty."),
             ("A soft voice", "Soft would be मृदु; अप- marks something faulty.")],
            "अपस्वर = faulty voice.",
            "अप- + स्वर = faulty voice."),
        order(1, "Put these printed words of unit 48 in the printed order.",
              ["अपस्वरं", "भाषमाणं", "श्रोतारं", "दूरतः", "परिवर्जयेत्"],
              "In a faulty voice; speaking; the hearer; from afar; should avoid.",
              "अपस्वरं → भाषमाणं → श्रोतारं → दूरतः → परिवर्जयेत्."),
        match(2, "Match each sure word of unit 48 to its meaning.",
              [["अपस्वर", "faulty voice"], ["भाषमाण", "speaking"], ["मरण", "death"], ["श्रोतृ", "hearer"],
               ["दूरतः", "from afar"], ["परिवर्जयेत्", "should avoid"]],
              "अपस्वर = faulty voice, भाषमाण = speaking, मरण = death, श्रोतृ = hearer, दूरतः = from afar, परिवर्जयेत् = should avoid.",
              "अपस्वर, भाषमाण, मरण, श्रोतृ, दूरतः, परिवर्जयेत्.", role="extend",
              teaches="श्रोतारम् is the accusative of श्रोतृ (hearer); the -तृ noun names the doer."),
        mcq("discriminate", 3, "In unit 48, what form is भाषमाणम्?",
            ("Present participle: speaking", "-मान (here -माण) = -ing: भाषमाण = speaking."),
            [("Absolutive: having spoken", "An absolutive would be भाषित्वा."),
             ("Past participle: spoken", "The past participle would be भाषित."),
             ("Optative: should speak", "An optative would be भाषेत.")],
            "भाषमाणम् = speaking (present participle, accusative).",
            "-मान / -माण = -ing."),
        mcq("apply", 4, "By unit 48, how is one told to keep away?",
            ("From afar", "दूरतः परिवर्जयेत्: one should avoid from afar."),
            [("For a month", "No month is named; the word is दूरतः, from afar."),
             ("By night", "No night is named; the word is दूरतः, from afar."),
             ("By bathing", "No bath is named; the word is दूरतः, from afar.")],
            "दूरतः = from afar.",
            "दूरतः परिवर्जयेत्."),
        mcq("transfer", 5, "By the pattern of परिवर्जयेत् (one should avoid), what does गच्छेत् mean in a new example?",
            ("One should go", "गच्छेत् is the optative of √गम्: one should go, like परिवर्जयेत्."),
            [("One went", "'Went' would be a past form such as अगच्छत्."),
             ("One will go", "'Will go' would be the future गमिष्यति."),
             ("Having gone", "'Having gone' would be the absolutive गत्वा.")],
            "गच्छेत् = one should go, like परिवर्जयेत् = one should avoid.",
            "Optative = should.",
            teaches="The optative states what one should do: परिवर्जयेत् = one should avoid."),
    ],
}

# ---------------------------------------------------------------- unit 49
AUTHORED["49"] = {
    "title": "ऊर्ध्वश्वासं गतोष्माणं",
    "question": "By unit 49, which four kinds of patient should the intelligent one avoid?",
    "rule": ("The intelligent one (बुद्धिमान्) should avoid (परिवर्जयेत्) one with upward breath (ऊर्ध्वश्वासं), whose "
             "warmth has gone (गतोष्माणं), whose groins are afflicted by pain (शूलोपहतवंक्षणं), and who finds no comfort "
             "(शर्म अनधिगच्छन्तं)."),
    "limits": ("ऊर्ध्वश्वास is literally 'upward breath'; no modern term is fixed. Who the intelligent one is is not said. "
               "वङ्क्षण = groin (standard). The verse gives no time span."),
    "explain_hi": ("यह श्लोक दो छपी पंक्तियों (०२.०९.६५ और ०२.०९.६६) का एक वाक्य है। "
                   "जिसकी साँस ऊपर की ओर चढ़ती हो, जिसकी गर्मी चली गई हो, जिसके वंक्षण (जाँघ का जोड़) पीड़ा से पीड़ित हों और जो सुख न पाए, उसे बुद्धिमान् त्याग दे। "
                   "चारों पद द्वितीया में हैं और ‘परिवर्जयेत्’ के कर्म हैं। "
                   "‘गतोष्माणं’ और ‘शूलोपहत’ में अ + उ → ओ, और ‘चानधिगच्छंतं’ में अ + अ → आ।"),
    "hook": "ऊपर साँस, गर्मी गई, वंक्षण में शूल, सुख नहीं: त्याज्य।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 49, which way does the breath of this patient go?",
            ("Upward", "ऊर्ध्वश्वासम्: one whose breath goes upward."),
            [("Inward", "The word is ऊर्ध्व, upward, not inward."),
             ("Sideways", "The word is ऊर्ध्व, upward, not sideways."),
             ("Downward", "Downward would be अधः; the word is ऊर्ध्व.")],
            "ऊर्ध्व = upward; श्वास = breath.",
            "ऊर्ध्वश्वास = upward breath."),
        order(1, "Put the four signs of unit 49 and the instruction in the printed order.",
              ["ऊर्ध्वश्वासं", "गतोष्माणं", "शूलोपहतवंक्षणं", "शर्म चानधिगच्छंतं", "बुद्धिमान् परिवर्जयेत्"],
              "Upward breath; warmth gone; groins afflicted by pain; finding no comfort; the intelligent one should avoid.",
              "श्वास → उष्मा → वंक्षण → शर्म → परिवर्जयेत्."),
        match(2, "Match each word of unit 49 to its meaning.",
              [["ऊर्ध्व", "upward"], ["श्वास", "breath"], ["उष्मन्", "warmth"], ["शूल", "pain"],
               ["वङ्क्षण", "groin"], ["शर्मन्", "comfort"]],
              "ऊर्ध्व = upward, श्वास = breath, उष्मन् = warmth, शूल = pain, वङ्क्षण = groin, शर्मन् = comfort.",
              "ऊर्ध्व, श्वास, उष्मन्, शूल, वङ्क्षण, शर्मन्.", role="extend",
              teaches="गतोष्माणम् is a bahuvrīhi: 'one whose warmth (उष्मन्) has gone (गत)'."),
        mcq("discriminate", 3, "Which split of गतोष्माणं in unit 49 is right?",
            ("गत + उष्माणम्", "अ + उ → ओ: गत + उष्माणम् → गतोष्माणम्."),
            [("गतो + ष्माणम्", "ष्माणम् is not a word; the ओ comes from अ + उ."),
             ("गत + ओष्माणम्", "अ + ओ would give औ (गतौष्माणम्), not ओ."),
             ("गत् + ओष्माणम्", "गत् is not the word here; the past participle is गत.")],
            "गत (gone) + उष्माणम् (warmth).",
            "अ + उ → ओ."),
        mcq("apply", 4, "By unit 49, who should avoid such a patient?",
            ("The intelligent one", "बुद्धिमान् परिवर्जयेत्: the intelligent one should avoid."),
            [("The patient's kin", "No kin are named; the subject is बुद्धिमान्."),
             ("The king's own envoy", "No envoy is named; the subject is बुद्धिमान्."),
             ("The young pupil", "No pupil is named; the subject is बुद्धिमान्.")],
            "बुद्धिमान् = the intelligent one (not further named).",
            "बुद्धिमान् परिवर्जयेत्."),
        mcq("transfer", 5, "By the pattern of शूल + उपहत → शूलोपहत, how is सूर्य + उदयः (sunrise) joined in a new example?",
            ("सूर्योदयः", "अ + उ → ओ: सूर्य + उदयः → सूर्योदयः."),
            [("सूर्यौदयः", "औ comes from अ + ओ or औ; here the second vowel is उ."),
             ("सूर्युदयः", "The अ does not vanish; अ + उ merge into ओ."),
             ("सूर्यवदयः", "अव् comes from ओ before a vowel; here the vowels are अ + उ.")],
            "सूर्य + उदयः = सूर्योदयः, like शूल + उपहत = शूलोपहत.",
            "अ + उ → ओ.",
            teaches="अ or आ before उ or ऊ gives ओ: शूल + उपहत → शूलोपहत."),
    ],
}

# ---------------------------------------------------------------- unit 50
AUTHORED["50"] = {
    "title": "यो जातशीतपिटकः",
    "question": "By unit 50, which sure signs of cold and heat are named, and within whose range is such a man?",
    "rule": ("He in whom cold pustules (शीतपिटक) have arisen, or who is cold-limbed (शीताङ्गः), hating heat (उष्णद्वेषी) "
             "and afflicted by cold (शीतार्तः), is within the range of the lord of the departed (प्रेताधिपगोचरः)."),
    "limits": ("Low confidence; prose by the data. The printed verb विद्ह्यते is damaged: vidahyate (burns) is a conjecture, "
               "vidhyate (is pierced) another: no question on the verb. The lord of the departed is probably Yama (probable)."),
    "explain_hi": ("यह गद्य इकाई (डेटा के अनुसार) दो छपी पंक्तियों (०२.०९.६७ और ०२.०९.६८) का एक वाक्य है; विश्वास कम। "
                   "जिसके ठण्डी फुंसियाँ (शीत पिटक) उठी हों, या जिसके अंग ठण्डे हों, जो गर्मी से द्वेष करे और ठण्ड से पीड़ित हो, वह प्रेतों के अधिपति (सम्भवतः यम) की पहुँच में है। "
                   "छपा ‘विद्ह्यते’ शब्द नहीं; ‘विदह्यते’ (जलता है) अनुमानित पाठ है और ‘विध्यते’ (बिंधता है) दूसरा; इसलिए क्रिया पर प्रश्न नहीं। "
                   "‘स प्रेताधिप-’ में सः का विसर्ग व्यंजन से पहले लुप्त है।"),
    "hook": "ठण्डी फुंसियाँ, ठण्डे अंग, गर्मी से द्वेष: प्रेताधिप की पहुँच में।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 50, what does उष्णद्वेषी mean?",
            ("Hating heat", "उष्ण (heat) + द्वेषिन् (hating): hating heat."),
            [("Craving heat", "Craving would be अभिलाषी; द्वेषी means hating."),
             ("Free of heat", "Free of would be a word with -रहित; द्वेषी means hating."),
             ("Hot to touch", "That would be उष्णस्पर्श; द्वेषी means hating.")],
            "उष्णद्वेषी = one who hates heat.",
            "द्वेषिन् = hating."),
        order(1, "Put these sure words of unit 50 in the printed order.",
              ["जातशीतपिटकः", "शीतांगो", "उष्णद्वेषी", "शीतार्तः", "प्रेताधिपगोचरः"],
              "Cold pustules arisen; cold-limbed; hating heat; afflicted by cold; within the range of the lord of the departed.",
              "पिटक → शीताङ्ग → उष्णद्वेषी → शीतार्त → प्रेताधिपगोचर."),
        match(2, "Match each sure word of unit 50 to its meaning.",
              [["शीत", "cold"], ["पिटक", "pustule"], ["अङ्ग", "limb"], ["उष्ण", "heat"],
               ["आर्त", "afflicted"], ["गोचर", "range, domain"]],
              "शीत = cold, पिटक = pustule, अङ्ग = limb, उष्ण = heat, आर्त = afflicted, गोचर = range.",
              "शीत, पिटक, अङ्ग, उष्ण, आर्त, गोचर.", role="extend",
              teaches="शीताङ्गः is a bahuvrīhi: 'one whose limbs (अङ्ग) are cold (शीत)'."),
        multi("discriminate", 3, "Which signs does unit 50 name on its sure words?",
              [("Cold limbs", "Named: शीताङ्गः, cold-limbed."),
               ("Craving cold water", "Not named: he is afflicted by cold, not craving it."),
               ("Hating heat", "Named: उष्णद्वेषी."),
               ("Hot, burning limbs", "Not named: the limbs are cold, शीताङ्गः."),
               ("Afflicted by cold", "Named: शीतार्तः.")],
              [0, 2, 4],
              "Cold limbs, hating heat, afflicted by cold (and cold pustules).",
              "शीताङ्गः, उष्णद्वेषी, शीतार्तः."),
        mcq("apply", 4, "By unit 50, within whose range (गोचर) is such a man?",
            ("The lord of the departed", "प्रेताधिपगोचरः: within the range of the lord of the departed (probably Yama)."),
            [("The lord of the healers", "No healer is named; the compound is प्रेत-अधिप."),
             ("The lord of the waters", "No waters are named; the compound is प्रेत-अधिप."),
             ("The lord of the mountains", "No mountain is named; the compound is प्रेत-अधिप.")],
            "प्रेत (departed) + अधिप (lord) + गोचर (range).",
            "प्रेताधिपगोचर = in the range of the lord of the departed."),
        mcq("transfer", 5, "By the pattern of सः + प्रेताधिप- → स प्रेताधिप-, how is सः + गच्छति (he goes) joined in a new example?",
            ("स गच्छति", "सः loses its visarga before a consonant: सः + गच्छति → स गच्छति."),
            [("सो गच्छति", "The ओ rule does not apply to सः before a consonant; it becomes स."),
             ("सर्गच्छति", "र् comes after a vowel other than अ/आ; here the vowel is अ."),
             ("सस्गच्छति", "स् comes from a visarga before त or थ; here it is ग.")],
            "सः + गच्छति = स गच्छति, like सः + प्रेताधिप- = स प्रेताधिप-.",
            "सः + consonant → स.",
            teaches="The pronoun सः (and एषः) drops its visarga before any consonant: सः + प्रेताधिप- → स प्रेताधिप-."),
    ],
}

# ---------------------------------------------------------------- unit 51
AUTHORED["51"] = {
    "title": "यस्य रज्जुरिव छाया",
    "question": "By unit 51, what is seen on the neck, and what surely happens to that living being?",
    "rule": ("He on whose neck (कंठे) a shadow like a rope (रज्जुरिव छाया) is seen attached (सक्ता उपलक्ष्यते): that "
             "living being (जंतुः) is surely (अवश्यं) dragged away soon (अचिरात् कृष्यते) by Yama's servants (यमकिंकरैः)."),
    "limits": ("छाया = shadow (also 'lustre'); 'shadow' is the plain rendering. The verse gives no number of days, only "
               "'soon', and names no cause or treatment."),
    "explain_hi": ("यह श्लोक दो छपी पंक्तियों (०२.०९.६९ और ०२.०९.७०) का एक वाक्य है। "
                   "जिसके कण्ठ पर रस्सी जैसी छाया लगी हुई दिखाई दे, वह प्राणी निश्चय ही शीघ्र यम के सेवकों द्वारा खींच लिया जाता है। "
                   "‘कृष्यते’ कर्मवाच्य है (खींचा जाता है) और ‘यमकिंकरैः’ तृतीया (सेवकों द्वारा)। "
                   "‘रज्जुरिव’ में उः + स्वर → उर्, ‘सक्तोपलक्ष्यते’ में आ + उ → ओ, और ‘सोऽचिराद्’ में अः + अ → ओऽ।"),
    "hook": "गले पर रस्सी-सी छाया: यम के दूत शीघ्र खींचें।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 51, what is seen on the neck?",
            ("A shadow like a rope", "रज्जुरिव छाया: a shadow like a rope, seen attached to the neck."),
            [("A stain like ash", "No ash is named; the verse says रज्जुः इव छाया."),
             ("A lump like a small seed", "No lump is named; the verse says रज्जुः इव छाया."),
             ("A rash like fire", "No rash is named; the verse says रज्जुः इव छाया.")],
            "रज्जुः (rope) इव (like) छाया (shadow).",
            "रज्जुरिव छाया = a rope-like shadow."),
        order(1, "Put these words of unit 51 in the printed order.",
              ["रज्जुरिव", "छाया", "कंठे", "सक्तोपलक्ष्यते", "अवश्यं", "कृष्यते"],
              "Like a rope; a shadow; on the neck; is seen attached; surely; is dragged.",
              "रज्जुरिव → छाया → कंठे → सक्तोपलक्ष्यते → अवश्यं → कृष्यते."),
        match(2, "Match each word of unit 51 to its meaning.",
              [["रज्जु", "rope"], ["छाया", "shadow"], ["कण्ठ", "neck"], ["अवश्यम्", "surely"],
               ["अचिरात्", "soon"], ["किङ्कर", "servant"]],
              "रज्जु = rope, छाया = shadow, कण्ठ = neck, अवश्यम् = surely, अचिरात् = soon, किङ्कर = servant.",
              "रज्जु, छाया, कण्ठ, अवश्यम्, अचिरात्, किङ्कर.", role="extend",
              teaches="कृष्यते is a passive (is dragged); the agent stands in the instrumental, यमकिंकरैः (by Yama's servants)."),
        mcq("discriminate", 3, "Which split of सक्तोपलक्ष्यते in unit 51 is right?",
            ("सक्ता + उपलक्ष्यते", "आ + उ → ओ: सक्ता + उपलक्ष्यते → सक्तोपलक्ष्यते."),
            [("सक्तो + पलक्ष्यते", "पलक्ष्यते is not a word; the ओ comes from आ + उ."),
             ("सक्ता + ओपलक्ष्यते", "ओपलक्ष्यते is not a word, and आ + ओ would give औ."),
             ("सक्तः + उपलक्ष्यते", "अः before उ would give सक्त उपलक्ष्यते, with no ओ.")],
            "सक्ता (attached) + उपलक्ष्यते (is seen).",
            "आ + उ → ओ."),
        mcq("apply", 4, "By unit 51, by whom is that living being dragged away?",
            ("By Yama's servants", "यमकिंकरैः: by the servants (किंकर) of Yama."),
            [("By his own kinsmen", "No kinsmen are named; the agent is यमकिंकरैः."),
             ("By a river's current", "No river is named; the agent is यमकिंकरैः."),
             ("By the wild beasts", "No beasts are named; the agent is यमकिंकरैः.")],
            "यम (Yama) + किंकर (servant), instrumental plural.",
            "यमकिंकरैः = by Yama's servants."),
        mcq("transfer", 5, "By the pattern of रज्जुः + इव → रज्जुरिव, how is गुरुः + अपि (the teacher too) joined in a new example?",
            ("गुरुरपि", "After उ, a visarga before a vowel becomes र्: गुरुः + अपि → गुरुरपि."),
            [("गुरोऽपि", "ओऽ comes from अः + अ; here the vowel before the visarga is उ."),
             ("गुर्वपि", "व् comes from a bare उ before a vowel; here the visarga stands between."),
             ("गुरुस्पि", "स् comes from a visarga before त or थ; here a vowel follows.")],
            "गुरुः + अपि = गुरुरपि, like रज्जुः + इव = रज्जुरिव.",
            "Vowel other than अ/आ + ः before a vowel → र्.",
            teaches="After a vowel other than अ or आ, a visarga before a vowel or a voiced consonant becomes र्: रज्जुः + इव → रज्जुरिव."),
    ],
}

# ---------------------------------------------------------------- unit 52
AUTHORED["52"] = {
    "title": "इति विकृतांगविज्ञानीयो",
    "question": "By unit 52, what is the name and number of the chapter that ends here?",
    "rule": ("Thus (इति) ends the ninth chapter (नवमोऽध्यायः) named (नाम) Vikṛtāṅgavijñānīya (विकृताङ्गविज्ञानीयः): "
             "the chapter concerned with knowing abnormal limbs or parts."),
    "limits": ("Colophon, prose. The name is analysed by the data as vikṛta (abnormal) + aṅga (limb or part) + vijñānīya "
               "(concerning knowledge). 'नामनवमो' is printed without a space. The leading ॥ is kept as printed."),
    "explain_hi": ("यह अध्याय की समाप्ति-पंक्ति (पुष्पिका) है, एक छपी पंक्ति (०२.०९.७१)। "
                   "‘इति’ = इस प्रकार; ‘विकृताङ्गविज्ञानीय नामक नवम अध्याय’ यहाँ पूरा होता है। "
                   "नाम के अंश: विकृत (विकारयुक्त), अङ्ग (अंग या भाग), विज्ञानीय (ज्ञान से सम्बन्धित)। "
                   "‘नवमोऽध्यायः’ में अः + अ → ओऽ, और ‘-ज्ञानीयो नाम’ में घोष न से पहले अः → ओ।"),
    "hook": "इति: नवम अध्याय, विकृत अंगों का ज्ञान, समाप्त।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 52, what does नवम mean?",
            ("Ninth", "नवमः = ninth: the ninth chapter."),
            [("New", "New is नव (as in नवाः, unit 43); नवम is the ordinal ninth."),
             ("Tenth", "Tenth would be दशम."),
             ("Seventh", "Seventh would be सप्तम.")],
            "नव (nine) → नवम (ninth).",
            "नवम = ninth."),
        order(1, "Put the words of unit 52 in the printed order.",
              ["इति", "विकृतांगविज्ञानीयो", "नाम", "नवमो", "अध्यायः"],
              "Thus; Vikṛtāṅgavijñānīya; named; ninth; chapter.",
              "इति → विकृतांगविज्ञानीयो → नाम → नवमो → अध्यायः."),
        match(2, "Match each part of the colophon of unit 52 to its meaning.",
              [["इति", "thus"], ["विकृत", "abnormal"], ["अङ्ग", "limb, part"], ["विज्ञानीय", "concerning knowledge"],
               ["अध्याय", "chapter"]],
              "इति = thus, विकृत = abnormal, अङ्ग = limb or part, विज्ञानीय = concerning knowledge, अध्याय = chapter.",
              "इति, विकृत, अङ्ग, विज्ञानीय, अध्याय.", role="extend",
              teaches="A colophon names the chapter by its title word in -ईय: विकृताङ्गविज्ञानीयः, 'the one about knowing abnormal limbs'."),
        mcq("discriminate", 3, "Which split of नवमोऽध्यायः in unit 52 is right?",
            ("नवमः + अध्यायः", "अः + अ → ओऽ: नवमः + अध्यायः → नवमोऽध्यायः."),
            [("नवमो + ध्यायः", "ध्यायः is not the word here; the ऽ marks the lost अ of अध्यायः."),
             ("नवमा + उध्यायः", "उध्यायः is not a word, and आ + उ would give ओ without ऽ."),
             ("नवम + अध्यायः", "अ + अ would give आ (नवमाध्यायः), not ओऽ.")],
            "नवमः (ninth) + अध्यायः (chapter).",
            "अः + अ → ओऽ."),
        mcq("apply", 4, "By the parts of its name in unit 52, what is this chapter about?",
            ("Knowing abnormal limbs or parts", "विकृत (abnormal) + अङ्ग (limb, part) + विज्ञानीय (concerning knowledge)."),
            [("Treating fevers of the head", "No fever or head is in the name; it is विकृत-अङ्ग-विज्ञानीय."),
             ("The rules for one's daily conduct", "No conduct is in the name; it is विकृत-अङ्ग-विज्ञानीय."),
             ("The growth of the embryo", "No embryo is in the name; it is विकृत-अङ्ग-विज्ञानीय.")],
            "विकृताङ्गविज्ञानीय = concerning the knowledge of abnormal limbs or parts.",
            "विकृत + अङ्ग + विज्ञानीय."),
        mcq("transfer", 5, "By the pattern of नव (nine) → नवम (ninth), what does दशम mean in a new example?",
            ("Tenth", "दश (ten) → दशम (tenth), like नव → नवम."),
            [("Ten", "Ten is the numeral दश; दशम is the ordinal."),
             ("Tenfold", "Tenfold would be दशगुण or दशविध."),
             ("Ten each", "Ten each would be the repeated दश दश.")],
            "दशम = tenth, like नवम = ninth.",
            "-म after नव / दश makes the ordinal.",
            teaches="The ordinals नवम (ninth) and दशम (tenth) add -म to the numeral: नव → नवम."),
    ],
}

# ================================================================ NOTES_HI
NOTES_HI = {
    "40": ("श्लोक; विश्वास मध्यम; दो छपी पंक्तियाँ (०२.०९.४७ और ०२.०९.४८) एक इकाई में; कोई पाठ-चिह्न नहीं। क्रिया ‘प्लवते’ दूसरी "
           "पंक्ति में है। ‘पद्मिनीपत्रवत्’ = कमलिनी के पत्ते की तरह (पद्मिनी: नेलुम्बो न्यूसीफ़ेरा, मानक पहचान); पत्ते पर जल का व्यवहार "
           "समझा जाता है, कहा नहीं गया। ‘प्लवमानस्य’ जल के लिए है या व्यक्ति के लिए, निश्चित नहीं। सन्धि जाँची: -वत् + तोयम् → "
           "-वत्तोयं; षण्मासाः + तस्य → षण्मासास्तस्य (त से पहले विसर्ग → स्)। ‘है’ समझा जाता है।"),
    "41": ("श्लोक; विश्वास उच्च; दो छपी पंक्तियाँ (०२.०९.४९ और ०२.०९.५०) एक वाक्य। पाठ-चिह्न (सम्भव): ‘यस्यरोमकूपाश्च’ = यस्य "
           "रोमकूपाः च, केवल स्थान छूटा, कोई अक्षर नहीं बदला। ‘संवृत’ = बन्द या ढका; ‘बन्द’ चुना गया। ‘हरित’ = हरा या पीला-हरा। "
           "सन्धि जाँची: सिराः + यस्य → सिरा यस्य (आः घोष से पहले विसर्ग खोता है); सः + अम्ल → सोऽम्ल (अः + अ → ओऽ); पित्तात् + मरणम् "
           "→ पित्तान्मरणम् (अनुनासिक से पहले त् → न् वैकल्पिक; द् भी सही); मरणम् + अश्नुते → मरणमश्नुते।"),
    "42": ("श्लोक; विश्वास मध्यम; दो छपी पंक्तियाँ (०२.०९.५१ और ०२.०९.५२) एक वाक्य। पाठ-चिह्न (सम्भव): छपा ‘चूर्ण’ सम्भवतः ‘चूर्णम्’ "
           "(नपुंसक प्रथमा का म् छूटा)। ‘वामासांतं’ = वा + मासान्तम् डेटा का पाठ है, दूसरा विभाजन सम्भव; इसलिए अवधि पर प्रश्न नहीं। "
           "‘सस्नेहं’ नपुंसक है जबकि ‘धूम’ पुल्लिंग, इसलिए क्रियाविशेषण माना गया। सन्धि जाँची: मुखे + अपि → मुखेऽपि (ए + अ → एऽ); "
           "धूमः + व- → धूमो (घोष व्यंजन से पहले अः → ओ)।"),
    "43": ("डेटा में ‘गद्य’ (छन्द जैसी लगने पर भी गद्य ही रखा गया); विश्वास कम; दो छपी पंक्तियाँ (०२.०९.५३ और ०२.०९.५४) एक वाक्य: "
           "‘कुर्वन्ति’ का कर्म ‘मृत्युम्’ दूसरी पंक्ति में। पाठ-चिह्न (सम्भव): छपा ‘षडरात्रान्त्रिरात्रादातुरस्य’ → सुझाव षड्रात्रात् "
           "त्रिरात्राद् आतुरस्य (अतिरिक्त अ और त/न की भूल); यह अनुमान है, इसलिए रातों पर प्रश्न नहीं। ‘सीमन्तावर्तक’ द्वन्द्व (माँग और "
           "भँवर) या एक शब्द हो सकता है; अर्थ पक्का नहीं। पञ्चमी का अर्थ ‘के बाद’ लिया गया, ‘के भीतर’ नहीं कहा गया। सन्धि जाँची: भ्रुवोः "
           "+ वा → भ्रुवोर्वा (अ/आ के अलावा स्वर के बाद, घोष से पहले विसर्ग → र्)।"),
    "44": ("श्लोक; विश्वास मध्यम; दो छपी पंक्तियाँ (०२.०९.५५ और ०२.०९.५६) एक वाक्य। पाठ-चिह्न (सम्भव): छपा ‘आर्द्वेषु’ कोई शब्द नहीं; "
           "‘आर्द्रेषु’ (गीले) अनुमानित पाठ (द्र/द्व की भूल); इस पर प्रश्न नहीं। ‘र्द्ध’ छपाई की वर्तनी है = ‘र्ध’। ‘पूर्वम्’ = पहले "
           "(‘आगे’ भी सम्भव)। सन्धि जाँची: शुष्यति + उरः → शुष्यत्युरः (इ + भिन्न स्वर → य्); उरः + भृशम् → उरो भृशं (घोष व्यंजन से "
           "पहले अः → ओ); सः + अर्द्धमासम् → सोऽर्द्धमासं (अः + अ → ओऽ)।"),
    "45": ("श्लोक; विश्वास मध्यम; दो छपी पंक्तियाँ (०२.०९.५७ और ०२.०९.५८) एक वाक्य। पाठ-चिह्न (सम्भव): ‘तृष्णाच’ = तृष्णा च, केवल "
           "स्थान छूटा। ‘भिन्न पुरीष’ शाब्दिक (टूटा मल); ‘ढीला मल’ सम्भावित अर्थ, कहा नहीं गया। ‘भवेत्’ एक बार है, ‘जठरे अतिशीतता’ भी उसी "
           "से जुड़ता है। छपाई में ‘जठरे अतिशीतता’ बिना सन्धि के है। सन्धि जाँची: उरसि + ऊष्मा → उरस्यूष्मा (इ + भिन्न स्वर → य्); "
           "भवेत् + यस्य → भवेद्यस्य (घोष य से पहले त् → द्); प्रेतः + तथा → प्रेतस्तथा; तथा + एव → तथैव (आ + ए → ऐ)।"),
    "46": ("श्लोक; विश्वास मध्यम; दो छपी पंक्तियाँ (०२.०९.५९ और ०२.०९.६०)। पाठ-चिह्न (सम्भव): ‘मासान्स’ = मासान् सः (मासों में, संख्या "
           "नहीं); ‘मासात् सः’ (एक मास के बाद) भी सम्भव और छन्द में ठीक; छपा पाठ रखा गया; समय पर प्रश्न नहीं। चार नपुंसक कर्ता, एक "
           "एकवचन क्रिया। किसके मल-मूत्र, यह पंक्ति नहीं कहती। सन्धि जाँची: च + अप्सु → चाप्सु (अ + अ → आ); ‘अप्सु’ अप् की सप्तमी बहुवचन।"),
    "47": ("श्लोक; विश्वास मध्यम; दो छपी पंक्तियाँ (०२.०९.६१ और ०२.०९.६२) एक वाक्य: पहली पंक्ति ‘दृष्ट्वा’ का कर्म। कोई पाठ-चिह्न नहीं। "
           "‘वर्ण’ = रंग या कान्ति। ‘अयुक्त्या’ = बिना कारण; ‘अनुचित उपाय से’ भी सम्भव। ‘आदिशेत्’ का कर्ता छपा नहीं। सन्धि जाँची: "
           "रोगवृद्धिम् + अयुक्त्या → रोगवृद्धिमयुक्त्या; मरणम् + आदिशेत् → मरणमादिशेत् (स्वर से पहले म् जुड़कर लिखा जाता है)।"),
    "48": ("श्लोक; विश्वास कम; दो छपी पंक्तियाँ (०२.०९.६३ और ०२.०९.६४), सम्भवतः एक वाक्य (‘परिवर्जयेत्’ पहली पंक्ति के द्वितीया पदों "
           "को भी ले, यह सम्भावित है, निश्चित नहीं)। ‘प्राप्तं’ व्यक्ति (द्वितीया) या ‘मरणम्’ के साथ जा सकता है। ‘चास्यशब्दस्य’ = च + "
           "अस्य + शब्दस्य, या च + आस्य-शब्दस्य (मुख का शब्द): दोनों से वही अक्षर बनते हैं। ‘श्रोता’ कौन, स्पष्ट नहीं। इन पर कोई प्रश्न "
           "नहीं। सन्धि जाँची: मरणम् + आत्मनः → मरणमात्मनः।"),
    "49": ("श्लोक; विश्वास उच्च; दो छपी पंक्तियाँ (०२.०९.६५ और ०२.०९.६६) एक वाक्य: चार द्वितीया पद ‘परिवर्जयेत्’ के कर्म। कोई पाठ-चिह्न "
           "नहीं। ‘ऊर्ध्वश्वास’ शाब्दिक ‘ऊपर की साँस’, आधुनिक नाम तय नहीं; ‘वङ्क्षण’ = जाँघ का जोड़ (मानक)। ‘बुद्धिमान्’ कौन, नहीं कहा। "
           "सन्धि जाँची: गत + उष्माणम् → गतोष्माणं, शूल + उपहत → शूलोपहत (अ + उ → ओ); च + अनधिगच्छन्तम् → चानधिगच्छंतं (अ + अ → आ)।"),
    "50": ("डेटा में ‘गद्य’ (छन्द जैसी लगने पर भी गद्य ही रखा गया); विश्वास कम; दो छपी पंक्तियाँ (०२.०९.६७ और ०२.०९.६८) एक वाक्य। "
           "पाठ-चिह्न (सम्भव): छपा ‘विद्ह्यते’ मान्य शब्द नहीं; ‘विदह्यते’ (जलता है) अनुमानित पाठ, ‘विध्यते’ (बिंधता है) दूसरी सम्भावना; "
           "क्रिया पर प्रश्न नहीं। ‘प्रेताधिप’ = प्रेतों का स्वामी, सामान्यतः यम (सम्भावित)। सन्धि जाँची: यः + जात- → यो जात- (घोष व्यंजन "
           "से पहले अः → ओ); शीताङ्गः + वा → शीतांगो वा; सः + प्रेत- → स प्रेत- (सः का विसर्ग व्यंजन से पहले लुप्त)।"),
    "51": ("श्लोक; विश्वास उच्च; दो छपी पंक्तियाँ (०२.०९.६९ और ०२.०९.७०) एक वाक्य। कोई पाठ-चिह्न नहीं; छपाई में ‘कृष्यतेजंतुः’ बिना "
           "स्थान के। ‘छाया’ = छाया (कान्ति भी)। सन्धि जाँची: रज्जुः + इव → रज्जुरिव (उ के बाद, स्वर से पहले विसर्ग → र्); सक्ता + "
           "उपलक्ष्यते → सक्तोपलक्ष्यते (आ + उ → ओ); सः + अचिरात् → सोऽचिरात् (अः + अ → ओऽ); अचिरात् + यम- → अचिराद्यम- (घोष य से "
           "पहले त् → द्)।"),
    "52": ("गद्य (पुष्पिका); विश्वास उच्च; एक छपी पंक्ति (०२.०९.७१); कोई पाठ-चिह्न नहीं। आरम्भ का ‘॥’ छपे रूप में रखा गया। ‘नामनवमो’ "
           "बिना स्थान के छपा = नाम नवमः। सन्धि जाँची: -ज्ञानीयः + नाम → -ज्ञानीयो नाम (घोष व्यंजन से पहले अः → ओ); नवमः + अध्यायः → "
           "नवमोऽध्यायः (अः + अ → ओऽ)।"),
}

# ================================================================ AIDS
AIDS = {
    "40": {
        "chain": {"steps": ["शरीरे: शरीर में", "तोयं प्लवते: जल तैरे", "पद्मिनीपत्रवत्: कमलिनी-पत्र की तरह (मानक पहचान)",
                            "षण्मासाः तस्य जीवितं: जीवन छह मास"]},
        "chunks": "पद्मिनीपत्रवत्तोयं | शरीरे यस्य देहिनः || प्लवते प्लवमानस्य | षण्मासास्तस्य जीवितं",
        "sandhi": "त से पहले विसर्ग → स्: षण्मासाः + तस्य → षण्मासास्तस्य · त् + त → त्त: -वत् + तोयम् → -वत्तोयं।",
    },
    "41": {
        "chain": {"steps": ["१ हरिताभाः सिराः: हरी-सी सिराएँ", "२ रोमकूपाः संवृताः: रोमकूप बन्द",
                            "३ अम्लाभिलाषी: खट्टे की चाह", "पित्तात् मरणम्: पित्त से मृत्यु"]},
        "chunks": "हरिताभाः सिरा | यस्यरोमकूपाश्च संवृताः || सोऽम्लाभिलाषी पुरुषः | पित्तान्मरणमश्नुते",
        "sandhi": ("अः + अ → ओऽ: सः + अम्ल- → सोऽम्ल- · आः घोष से पहले विसर्ग खोता है: सिराः + यस्य → सिरा यस्य · अनुनासिक से पहले त् → "
                   "न् (वैकल्पिक, द् भी सही): पित्तात् + मरणम् → पित्तान्मरणम्।"),
        "pegs": "ह-रो-अ: हरी सिरा, रोमकूप, अम्ल; तीन लक्षणों के पहले अक्षर, फिर पित्त। (मेरा बनाया स्मरण-सूत्र)",
    },
    "42": {
        "diagram": {"groups": [
            {"label": "मूर्ध्नि मुखेऽपि वा: सिर पर या मुख पर भी", "items": ["गोमयचूर्णाभं चूर्ण: गोबर-चूर्ण जैसा चूर्ण"]},
            {"label": "मूर्ध्नि: सिर पर", "items": ["सस्नेहं धूमः: चिकना धुआँ"]}]},
        "chunks": "यस्य गोमयचूर्णाभं | चूर्ण मूर्ध्नि मुखेऽपि वा || सस्नेहं मूर्ध्नि धूमो | वामासांतं तस्य जीवितं",
        "sandhi": "ए + अ → एऽ: मुखे + अपि → मुखेऽपि · घोष व्यंजन से पहले अः → ओ: धूमः + व- → धूमो।",
    },
    "43": {
        "seesaw": "स्वस्थस्य (स्वस्थ का) ⇄ आतुरस्य (रोगी का): दोनों इसी इकाई में; दोनों के लिए अलग अवधि (संख्या अनुमानित पाठ पर)।",
        "chunks": "मूर्ध्नि भ्रुवोर्वा | कुर्वंति सीमंतावर्तका नवाः || मृत्युं स्वस्थस्य | षडरात्रान्त्रिरात्रादातुरस्य तु",
        "sandhi": "अ/आ के अलावा स्वर के बाद, घोष व्यंजन से पहले विसर्ग → र्: भ्रुवोः + वा → भ्रुवोर्वा।",
        "anchors": "पक्का: सिर या भौंहें, नए चिह्न, स्वस्थ और आतुर। अनिश्चित: रातों की संख्या, सीमन्तावर्तक का अर्थ। (मेरी याद-पद्धति)",
    },
    "44": {
        "chain": {"steps": ["स्नातानुलिप्तस्य: नहाने और लेप के बाद", "पूर्वं शुष्यति उरः भृशं: छाती पहले, बहुत सूखे",
                            "सोऽर्द्धमासं न जीवति: आधा मास नहीं जीता"]},
        "chunks": "यस्य स्नातानुलिप्तस्य | पूर्वं शुष्यत्युरो भृशं || आर्द्वेषु सर्वगात्रेषु | सोऽर्द्धमासं न जीवति",
        "sandhi": ("इ + भिन्न स्वर → य्: शुष्यति + उरः → शुष्यत्युरः · घोष व्यंजन से पहले अः → ओ: उरः + भृशम् → उरो भृशं · अः + अ → ओऽ: "
                   "सः + अर्द्धमासम् → सोऽर्द्धमासं।"),
    },
    "45": {
        "seesaw": "उरसि ऊष्मा (छाती में गर्मी) ⇄ जठरे अतिशीतता (पेट में अति ठण्डक): दोनों इसी श्लोक में।",
        "chunks": "उरस्यूष्मा भवेद्यस्य | जठरे अतिशीतता || भिन्नं पुरीषं तृष्णाच | यथा प्रेतस्तथैव सः",
        "sandhi": ("इ + भिन्न स्वर → य्: उरसि + ऊष्मा → उरस्यूष्मा · घोष य से पहले त् → द्: भवेत् + यस्य → भवेद्यस्य · आ + ए → ऐ: "
                   "तथा + एव → तथैव।"),
        "frame": "कहाँ गर्मी: उरसि → कहाँ ठण्डक: जठरे → और: भिन्न पुरीष (सम्भवतः ढीला), तृष्णा → तुलना: यथा प्रेतः तथैव सः।",
    },
    "46": {
        "diagram": {"groups": [
            {"label": "अप्सु निमज्जति: पानी में डूबें", "items": ["१ मूत्र", "२ पुरीष: मल", "३ निष्ठ्यूत: थूक", "४ शुक्र: वीर्य"]},
            {"label": "वा: या", "items": ["निष्ठ्यूतं बहुवर्णं: थूक अनेक रंग का"]}]},
        "chunks": "मूत्रं पुरीषं निष्ठ्यूतं | शुक्रं चाप्सु निमज्जति || निष्ठ्यूतं बहुवर्णं वा | यस्य मासान्स नश्यति",
        "sandhi": "अ + अ → आ: च + अप्सु → चाप्सु।",
        "pegs": "मू-पु-नि-शु: चार चीज़ों के पहले अक्षर, छपे क्रम में। (मेरा बनाया स्मरण-सूत्र)",
    },
    "47": {
        "chain": {"steps": ["१ स्वरस्य दुर्बलीभावं: स्वर की दुर्बलता", "२ हानिं बलवर्णयोः: बल और वर्ण की हानि",
                            "३ रोगवृद्धिम् अयुक्त्या: बिना युक्ति रोग-वृद्धि", "दृष्ट्वा मरणमादिशेत्: देखकर मृत्यु बताए"]},
        "chunks": "स्वरस्य दुर्बलीभावं | हानिं च बलवर्णयोः || रोगवृद्धिमयुक्त्या च | दृष्ट्वा मरणमादिशेत्",
        "frame": "क्या देखे: तीन लक्षण → कैसे: दृष्ट्वा (देखकर) → क्या करे: मरणम् आदिशेत् (मृत्यु बताए); कर्ता छपा नहीं।",
    },
    "48": {
        "chunks": "अपस्वरं भाषमाणं | प्राप्तं मरणमात्मनः || श्रोतारं चास्यशब्दस्य | दूरतः परिवर्जयेत्",
        "anchors": "पक्का: अपस्वर, भाषमाण, श्रोता, दूरतः परिवर्जयेत्। अनिश्चित: ‘प्राप्तं’ किससे जुड़ता है, ‘चास्य’ में अस्य या आस्य। (मेरी याद-पद्धति)",
        "sandhi": "स्वर से पहले म् जुड़कर लिखा जाता है: मरणम् + आत्मनः → मरणमात्मनः।",
    },
    "49": {
        "diagram": {"groups": [
            {"label": "बुद्धिमान् परिवर्जयेत्: बुद्धिमान् त्याग दे", "items": [
                "१ ऊर्ध्वश्वासं: ऊपर की साँस", "२ गतोष्माणं: गर्मी चली गई", "३ शूलोपहतवंक्षणं: वंक्षण में शूल",
                "४ शर्म अनधिगच्छंतं: सुख न पाए"]}]},
        "chunks": "ऊर्ध्वश्वासं गतोष्माणं | शूलोपहतवंक्षणं || शर्म चानधिगच्छंतं | बुद्धिमान् परिवर्जयेत्",
        "sandhi": "अ + उ → ओ: गत + उष्माणम् → गतोष्माणं, शूल + उपहत → शूलोपहत · अ + अ → आ: च + अनधिगच्छन्तम् → चानधिगच्छंतं।",
    },
    "50": {
        "chunks": "यो जातशीतपिटकः | शीतांगो वा विद्ह्यते || उष्णद्वेषी च शीतार्तः | स प्रेताधिपगोचरः",
        "sandhi": ("घोष व्यंजन से पहले अः → ओ: यः + जात- → यो जात-, शीताङ्गः + वा → शीतांगो वा · सः का विसर्ग व्यंजन से पहले लुप्त: "
                   "सः + प्रेत- → स प्रेत-।"),
        "anchors": "पक्का: शीत पिटक, शीत अंग, उष्णद्वेषी, शीतार्त, प्रेताधिप (सम्भवतः यम)। अनुमान: ‘विद्ह्यते’ की क्रिया। (मेरी याद-पद्धति)",
    },
    "51": {
        "chain": {"steps": ["कंठे रज्जुरिव छाया: गले पर रस्सी-सी छाया", "सक्ता उपलक्ष्यते: लगी दिखे",
                            "अवश्यं अचिरात्: निश्चय ही, शीघ्र", "यमकिंकरैः कृष्यते: यम के सेवक खींचें"]},
        "chunks": "यस्य रज्जुरिव छाया | कंठे सक्तोपलक्ष्यते || अवश्यं कृष्यतेजंतुः | सोऽचिराद्यमकिंकरैः",
        "sandhi": ("उ के बाद, स्वर से पहले विसर्ग → र्: रज्जुः + इव → रज्जुरिव · आ + उ → ओ: सक्ता + उपलक्ष्यते → सक्तोपलक्ष्यते · "
                   "अः + अ → ओऽ: सः + अचिरात् → सोऽचिरात्।"),
    },
    "52": {
        "diagram": {"groups": [
            {"label": "अध्याय का नाम", "items": ["विकृत: विकारयुक्त", "अङ्ग: अंग, भाग", "विज्ञानीय: ज्ञान-सम्बन्धी"]},
            {"label": "क्रम", "items": ["नवमः: नौवाँ अध्याय"]}]},
        "chunks": "॥ इति | विकृतांगविज्ञानीयो | नामनवमोऽध्यायः",
        "sandhi": "अः + अ → ओऽ: नवमः + अध्यायः → नवमोऽध्यायः · घोष व्यंजन से पहले अः → ओ: -ज्ञानीयः + नाम → -ज्ञानीयो नाम।",
    },
}

# ================================================================ IMAGE_SPECS
IMAGE_SPECS = {
    ("40", "chain"): {
        "file": "sh9-padminipatra-40.svg",
        "alt": ("Chain of card 40: water floats in the body like on a lotus leaf (padminī, Nelumbo nucifera, standard); "
                "his life is six months."),
        "type": "chain",
        "title": "कार्ड ४०: कमलिनी-पत्र जैसा जल",
        "steps": ["शरीर में जल तैरे", "पद्मिनी-पत्र की तरह (मानक पहचान)", "जीवन: छह मास"],
    },
    ("41", "chain"): {
        "file": "sh9-pitta-marana-41.svg",
        "alt": ("Flowchart of card 41: three signs, greenish veins, closed hair pores and craving the sour, lead to "
                "death from Pitta."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"१ हरी-सी आभा वाली सिराएँ\"] --> D[\"पित्त से मृत्यु\"]\n"
                 "  B[\"२ रोमकूप बन्द\"] --> D\n"
                 "  C[\"३ खट्टे की इच्छा\"] --> D\n"),
    },
    ("45", "seesaw"): {
        "file": "sh9-ura-jathara-45.svg",
        "alt": ("Split of card 45: heat in the chest against excessive coldness in the belly; with broken (probably loose) "
                "stool and thirst he is like a departed one."),
        "type": "split",
        "title": "कार्ड ४५: छाती गर्म, पेट ठण्डा",
        "cols": [["उरसि: छाती में", ["ऊष्मा: गर्मी"]],
                 ["जठरे: पेट में", ["अतिशीतता: अति ठण्डक"]]],
    },
    ("46", "diagram"): {
        "file": "sh9-apsu-nimajjana-46.svg",
        "alt": ("Flowchart of card 46 in printed order: urine, stool, sputum and semen sink in water, or sputum is of "
                "many colours: he perishes."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"१ मूत्र\"] --> E[\"पानी में डूबें\"]\n"
                 "  B[\"२ मल\"] --> E\n"
                 "  C[\"३ थूक\"] --> E\n"
                 "  D[\"४ वीर्य\"] --> E\n"
                 "  E --> G[\"वह नष्ट होता है\"]\n"
                 "  F[\"या: थूक अनेक रंग का\"] --> G\n"),
    },
    ("47", "chain"): {
        "file": "sh9-svara-bala-47.svg",
        "alt": ("Chain of card 47 in printed order: weakening of the voice, loss of strength and colour, increase of "
                "disease without reason; having seen these, one should foretell death."),
        "type": "chain",
        "title": "कार्ड ४७: देखकर मृत्यु बताए",
        "steps": ["१ स्वर की दुर्बलता", "२ बल और वर्ण की हानि", "३ अयुक्त्या रोग-वृद्धि", "देखकर: मृत्यु बताए"],
    },
    ("49", "diagram"): {
        "file": "sh9-parivarjana-49.svg",
        "alt": ("Flowchart of card 49 in printed order: upward breath, warmth gone, groins afflicted by pain, no comfort "
                "found: the intelligent one should avoid such a patient."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"१ ऊपर की साँस\"] --> E[\"बुद्धिमान् त्याग दे\"]\n"
                 "  B[\"२ गर्मी चली गई\"] --> E\n"
                 "  C[\"३ वंक्षण में शूल\"] --> E\n"
                 "  D[\"४ सुख न पाए\"] --> E\n"),
    },
    ("51", "chain"): {
        "file": "sh9-rajju-chaya-51.svg",
        "alt": ("Chain of card 51: a rope-like shadow is seen attached on the neck; surely and soon that being is "
                "dragged away by Yama's servants."),
        "type": "chain",
        "title": "कार्ड ५१: गले पर रस्सी-सी छाया",
        "steps": ["गले पर रस्सी-सी छाया", "लगी हुई दिखे", "निश्चय ही, शीघ्र", "यम के सेवक खींचें"],
    },
    ("52", "diagram"): {
        "file": "sh9-pushpika-52.svg",
        "alt": ("Table of card 52: the colophon's parts, iti thus, vikṛta abnormal, aṅga limb or part, vijñānīya "
                "concerning knowledge, navama ninth, adhyāya chapter."),
        "type": "table",
        "title": "कार्ड ५२: अध्याय की पुष्पिका",
        "heads": ["अंश", "अर्थ"],
        "rows": [["इति", "इस प्रकार"], ["विकृत", "विकारयुक्त"], ["अङ्ग", "अंग, भाग"], ["विज्ञानीय", "ज्ञान-सम्बन्धी"],
                 ["नवमः", "नौवाँ"], ["अध्यायः", "अध्याय"]],
    },
}
