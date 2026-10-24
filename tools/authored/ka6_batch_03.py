from helpers import mcq, match, order, fill, multi, accepts

AUTHORED = {}

# ---------------------------------------------------------------- unit 25
AUTHORED["25"] = {
    "title": "वेगसंरोधं पीडितो वा",
    "question": "Which faulty bastis does verse 25 name at the start of the statement on the basti thrown upward?",
    "rule": ("Verse 25 names the faults: holding back of the urge (vegasaṃrodha), excess quantity (atimātrā), "
             "a basti lacking unctuousness, salt and heat (reading not firm), small, with little drug. "
             "The verb, comes out, is in 05.06.51."),
    "limits": ("No verb here; the result follows in 05.06.50-51. Which urge, and who is pressed, are not stated. "
               "Flagged print: कुँर्वंतो (kurvan or kurvantaḥ, open) and अग्निग्ध (read asnigdha, not unctuous); "
               "how far a- reaches is not firm. No question rests on these."),
    "explain_hi": ("यह श्लोक एक लम्बे कथन (05.06.48-51) का आरम्भ है: वह बस्ति जो ऊपर फेंकी जाकर मुख-नासिका से निकलती है। "
                   "पहली पंक्ति में दो कारण हैं: वेग का संरोध यानी स्वाभाविक वेग को रोकना, और अतिमात्रा यानी "
                   "अधिक मात्रा से पीड़ित (डेटा का पाठ: अधिक मात्रा से दबाई गई बस्ति; रोगी का पीड़ित होना भी सम्भव)। "
                   "दूसरी पंक्ति में बस्ति के दोष हैं: अनुमानित पाठ पर स्नेह, लवण और उष्णता से रहित, अल्प यानी "
                   "थोड़ी, और अल्पभेषज यानी कम औषध वाली। "
                   "कौन-सा वेग रुका, यह नहीं कहा; क्रिया ‘निरेति’ 05.06.51 में आती है।"),
    "hook": "वेग का संरोध, अधिक मात्रा, या थोड़ी और कम औषध वाली बस्ति: वह ऊपर उठेगी।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "Which basti does line 2 of verse 25 name among the faulty ones?",
            ("A small basti with little drug",
             "बस्तिरल्पोऽल्पभेषजः: बस्तिः अल्पः अल्पभेषजः, small and with little drug."),
            [("A large basti with plenty of drug",
              "The verse says अल्प (small) and अल्पभेषज (little drug), not large or plentiful."),
             ("A basti given after a heavy meal",
              "No meal is named in verse 25."),
             ("A basti too hot and too sharp",
              "Verse 25 names no sharp basti; too hot and sharp is the atiyoga basti of 05.06.69.")],
            "Line 2 ends with बस्तिः अल्पः अल्पभेषजः: small, with little drug.",
            "अल्प = small, little; भेषज = drug."),
        match(1, "Match each word of verse 25 to its meaning.",
              [["वेग", "urge"], ["संरोध", "holding back"], ["अतिमात्रा", "excess quantity"],
               ["अल्प", "small, little"], ["भेषज", "drug"]],
              "These words name the faults that open the statement of 05.06.48-51.",
              "वेग = urge; संरोध = holding back; अतिमात्रा = excess quantity; अल्प = small; भेषज = drug."),
        order(2, "Put these words of verse 25 in the verse's order.",
              ["वेगसंरोधं", "अतिमात्रया", "बस्तिः अल्पः", "अल्पभेषजः"],
              "Line 1: holding back the urge, then excess quantity; line 2 ends: the basti small, with little drug.",
              "वेगसंरोधं · अतिमात्रया ‖ बस्तिरल्पो · ऽल्पभेषजः.",
              role="extend",
              teaches="Verse 25 lists faults: the urge held back, excess quantity, and a small basti with little drug."),
        mcq("discriminate", 3, "Which split of बस्तिरल्पो is right?",
            ("बस्तिः + अल्पः",
             "ः after इ becomes र् before a vowel: बस्तिर् अल्पः; -अः then becomes -ओ before the next अ (ऽल्प)."),
            [("बस्ति + रल्पः",
              "रल्प is not a word; the र् is the changed visarga of बस्तिः."),
             ("बस्तिः + अल्पम्",
              "अल्पम् before the vowel of the next word would print अल्पमल्प, not अल्पो ऽल्प."),
             ("बस्ती + अल्पः",
              "ई before अ would become य्: बस्त्यल्प; and बस्ती is not the nominative here.")],
            "बस्तिः (the basti) + अल्पः (small); then अल्पः + अल्पभेषजः → अल्पोऽल्पभेषजः.",
            "-इः + vowel → -इर्; -अः + अ → -ओऽ."),
        multi("apply", 4,
              "A physician reviews a basti that rose up. Which faults are named in verse 25?",
              [("The urge was held back", "Right: वेगसंरोधं."),
               ("An excess quantity (अतिमात्रा) is named", "Right: पीडितो वा ऽतिमात्रया names excess quantity."),
               ("It was small and had little drug", "Right: बस्तिरल्पो ऽल्पभेषजः."),
               ("It was given on an empty stomach", "No empty stomach is named in verse 25."),
               ("It was given at night", "No time of day is named in verse 25.")],
              [0, 1, 2],
              "Verse 25 names the held urge, the excess quantity and the small basti with little drug.",
              "वेगसंरोध · अतिमात्रा · अल्प, अल्पभेषज."),
        mcq("transfer", 5,
            "By the pattern of अतिमात्रया (by excess quantity), what does the new word अल्पमात्रया mean?",
            ("By a small quantity",
             "-मात्रया is f. instrumental singular: 'by, with' the quantity; अल्प = small."),
            [("A small quantity (as subject)",
              "The subject form would be अल्पमात्रा, without -या."),
             ("Of a small quantity",
              "'Of' needs the genitive अल्पमात्रायाः."),
             ("In small quantities",
              "'In' needs the locative, and -या here is singular.")],
            "मात्रा (f.) → instrumental मात्रया, 'by the quantity'.",
            "f. -आ stem: instrumental sg -अया.",
            teaches="अतिमात्रया is the feminine instrumental singular of अतिमात्रा: 'by excess quantity'."),
    ],
}

# ---------------------------------------------------------------- unit 26
AUTHORED["26"] = {
    "title": "मुखनासिकात् निरेति",
    "question": "By which way does the faulty basti come out, and what does it produce?",
    "rule": ("Or a mild basti, thrown upward by the wind, comes out from the mouth and nose, producing "
             "fainting (mūrcchā), nausea (hṛllāsa), thirst, burning (dāha) and the others."),
    "limits": ("The subject is the basti of 05.06.49; the verse appears to complete the statement of 05.06.48-51. "
               "The symptom compound is printed with an extra a (तृडदाह for तृड्दाह), a flagged slip; no "
               "question rests on its spelling. The others (ādi) are not listed."),
    "explain_hi": ("यह श्लोक 05.06.48 से चले कथन को पूरा करता है; कर्ता 05.06.49 की बस्ति है। "
                   "अथवा मृदु बस्ति, वायु से ऊपर फेंकी जाकर, मुख और नासिका से बाहर निकलती है। "
                   "निकलते हुए वह मूर्च्छा यानी बेहोशी, हृल्लास यानी मिचली, तृष्णा यानी प्यास और दाह यानी जलन आदि उत्पन्न करती है। "
                   "‘आदि’ के अन्य लक्षण नहीं गिनाए।"),
    "hook": "वायु ने ऊपर फेंका, बस्ति मुँह-नाक से निकली: बेहोशी, मिचली, प्यास, जलन।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By which way does the basti come out, according to verse 26?",
            ("From the mouth and nose",
             "मुखनासिकात् निरेति: it comes out from the mouth and nose."),
            [("From the anus with the stool",
              "Verse 26 says the basti is thrown upward and leaves by mouth and nose."),
             ("From the skin as sweat",
              "Sweat is not named in verse 26."),
             ("By the urinary passage",
              "The urinary passage is not named in verse 26.")],
            "मुख-नासिकात् is an ablative: 'from the mouth and nose'.",
            "मुखनासिकात् = from mouth and nose; निरेति = comes out."),
        order(1, "Put these words of verse 26 in the verse's order.",
              ["मृदुर्वा", "मारुतेनोर्ध्वं", "विक्षिप्तो", "मुखनासिकात्", "निरेति"],
              "Or mild, by the wind upward thrown, from mouth and nose, comes out.",
              "मृदुर्वा · मारुतेनोर्ध्वं · विक्षिप्तो · मुखनासिकात् ‖ निरेति."),
        match(2, "Match each word of verse 26 to its meaning.",
              [["मारुत", "wind"], ["ऊर्ध्वम्", "upward"], ["मूर्च्छा", "fainting"],
               ["हृल्लास", "nausea"], ["दाह", "burning"]],
              "The first two words say how the basti moves; the last three are signs it produces.",
              "मारुत = wind; ऊर्ध्वम् = upward; मूर्च्छा = fainting; हृल्लास = nausea; दाह = burning.",
              role="extend",
              teaches="Verse 26: thrown upward by the wind (मारुत), the basti produces मूर्च्छा, हृल्लास, thirst and दाह."),
        mcq("discriminate", 3, "Which split of मारुतेनोर्ध्वं is right?",
            ("मारुतेन + ऊर्ध्वम्",
             "अ + ऊ → ओ: मारुतेन + ऊर्ध्वम् → मारुतेनोर्ध्वम्; final म् shows as anusvara."),
            [("मारुतेना + ऊर्ध्वम्",
              "मारुतेना is not a form; the instrumental of मारुत is मारुतेन."),
             ("मारुतेन + ओर्ध्वम्",
              "ओर्ध्वम् is not a word, and अ + ओ would give औ."),
             ("मारुतेनः + ऊर्ध्वम्",
              "मारुतेनः is not a form; and -अः before ऊ would drop the visarga, giving मारुतेन ऊर्ध्वम्.")],
            "मारुतेन (by the wind) + ऊर्ध्वम् (upward).",
            "अ + उ/ऊ → ओ."),
        mcq("apply", 4, "A basti has come out through a patient's mouth. What does verse 26 say moved it?",
            ("The wind threw it upward",
             "मारुतेनोर्ध्वं विक्षिप्तः: thrown upward by the wind."),
            [("The patient's straining pushed it",
              "Straining is not named in verse 26."),
             ("Its own heat lifted it up",
              "Verse 26 names the wind, not heat, as what threw it."),
             ("A fit of vomiting drew it up",
              "Vomiting is not named in verse 26.")],
            "विक्षिप्तः (thrown) with the instrumental मारुतेन (by the wind) and ऊर्ध्वम् (upward).",
            "मारुतेन ऊर्ध्वं विक्षिप्तः = thrown upward by the wind."),
        mcq("transfer", 5,
            "Like मुखनासिकात् निरेति (comes out from mouth and nose), what does the new sentence वायुः गुदात् निरेति mean?",
            ("The wind comes out from the anus",
             "गुदात् is ablative, 'from the anus'; निरेति = comes out; वायुः is the subject."),
            [("The wind goes into the anus",
              "'Into' would need an accusative or locative, and निरेति means comes out."),
             ("The wind of the anus comes out",
              "'Of the anus' would need the genitive गुदस्य."),
             ("The wind will come out of the anus",
              "निरेति is present, not future.")],
            "-आत् ablative = 'from'; निः + √इ = to come out.",
            "गुदात् = from the anus; निरेति = comes out (present).",
            teaches="मुखनासिकात् is an ablative ('from mouth and nose'); निरेति (niḥ-√i) means 'comes out'."),
    ],
}

# ---------------------------------------------------------------- unit 27
AUTHORED["27"] = {
    "title": "सिञ्चेच्छीताम्बुना मुखम्",
    "question": "What is done first when the basti has risen and fainting is seen?",
    "rule": ("Seeing his fainting, one should sprinkle his face with cold water, fan (him) until the "
             "exhaustion is gone, and make (him) do prāṇāyāma (breath control)."),
    "limits": ("Two reviewer points are open: āklamanāśāt may be ā + klama-nāśāt ('until the end of fatigue'), "
               "and vyajet is probably the potential of vi-√aj, not a denominative; the sense 'fan' stays. "
               "No question rests on these. Who fans is not named."),
    "explain_hi": ("श्लोक २६ में बस्ति ऊपर निकलती है और मूर्च्छा आदि होती है; यहाँ से उपचार शुरू होता है। "
                   "मूर्च्छा का विकार देखकर उसके मुख पर शीतल जल सींचे। "
                   "फिर थकावट मिटने तक पंखा झले, और उससे प्राणायाम यानी श्वास का नियमन कराए। "
                   "पंखा कौन झले, यह नहीं कहा।"),
    "hook": "मूर्च्छा दिखी: मुँह पर ठंडा पानी, पंखा, फिर प्राणायाम।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "When the fainting is seen, what is done to the face, by verse 27?",
            ("It is sprinkled with cold water",
             "सिञ्चेत् शीताम्बुना मुखम्: sprinkle the face with cold water."),
            [("It is rubbed with warm oil and salt",
              "Verse 27 names cold water, not warm oil and salt."),
             ("It is covered with mustard paste",
              "Mustard is used on the head in 05.06.68, not on the face here."),
             ("It is held down toward the floor",
              "Face downward belongs to 05.06.54, the next verse.")],
            "शीत-अम्बुना (with cold water), मुखम् (the face), सिञ्चेत् (should sprinkle).",
            "शीताम्बु = cold water; सिञ्चेत् = should sprinkle."),
        order(1, "Put the steps of verse 27 in the text's order.",
              ["मूर्च्छा का विकार देखना", "शीतल जल से मुख सींचना", "पंखा झलना", "प्राणायाम कराना"],
              "Seeing the fainting, sprinkle the face, fan, and make him do prāṇāyāma.",
              "दृष्ट्वा · सिञ्चेत् ‖ व्यजेत् · प्राणायामं कारयेत्."),
        match(2, "Match each word of verse 27 to its meaning.",
              [["दृष्ट्वा", "having seen"], ["सिञ्चेत्", "should sprinkle"], ["शीताम्बु", "cold water"],
               ["मुखम्", "face"], ["कारयेत्", "should make (him) do"]],
              "One absolutive and two potentials carry the steps; शीताम्बु and मुखम् say with what and on what.",
              "दृष्ट्वा = having seen; सिञ्चेत् = should sprinkle; शीताम्बु = cold water; मुख = face; कारयेत् = should make do.",
              role="extend",
              teaches="Verse 27 links its steps with the absolutive दृष्ट्वा and the potentials सिञ्चेत् and कारयेत्."),
        mcq("discriminate", 3, "Which split of सिंचेच्छीतांबुना is right?",
            ("सिञ्चेत् + शीताम्बुना",
             "त् + श → च्छ: सिञ्चेत् + शीताम्बुना → सिञ्चेच्छीताम्बुना."),
            [("सिञ्चे + च्छीताम्बुना",
              "च्छीताम्बुना is not a word; the च्छ comes from त् + श."),
             ("सिञ्चेत् + छीताम्बुना",
              "छीत is not a word; the छ is the changed श of शीत."),
             ("सिञ्चेः + शीताम्बुना",
              "सिञ्चेः would be 2nd person, and ः + श does not give च्छ.")],
            "सिञ्चेत् (should sprinkle) + शीत-अम्बुना (with cold water).",
            "त् + श → च्छ."),
        multi("apply", 4, "A patient faints after the basti comes up. Which measures does verse 27 itself order?",
              [("Sprinkling the face with cold water", "Right: सिञ्चेच्छीताम्बुना मुखं."),
               ("Fanning him", "Right: व्यजेत्, should fan."),
               ("Making him do prāṇāyāma", "Right: प्राणायामं च कारयेत्."),
               ("Kneading the belly with hot hands", "That comes in 05.06.54, the next verse."),
               ("Pressing the throat with cloths", "That comes in 05.06.57, not in verse 27.")],
              [0, 1, 2],
              "Verse 27 has three measures: cold water on the face, fanning, prāṇāyāma.",
              "सिञ्चेत् · व्यजेत् · प्राणायामं कारयेत्."),
        mcq("transfer", 5,
            "By the pattern of दृष्ट्वा (having seen), what does the new sentence रोगिणं दृष्ट्वा वैद्यः बस्तिं ददाति mean?",
            ("Having seen the patient, the physician gives a basti",
             "दृष्ट्वा is an absolutive: the seeing comes first; वैद्यः is the subject of ददाति."),
            [("The patient, having seen the physician, gives a basti",
              "रोगिणम् is accusative, the one seen; the subject is वैद्यः."),
             ("The physician will see the patient after the basti",
              "दृष्ट्वा is not future, and the seeing comes before the giving."),
             ("Seeing the basti, the patient gives it to the physician",
              "बस्तिम् is the object of ददाति, and the patient is the one seen.")],
            "-त्वा absolutive = 'having done': दृष्ट्वा = having seen.",
            "दृष्ट्वा (√दृश्, absolutive) = having seen.",
            teaches="दृष्ट्वा is the absolutive of √दृश्: 'having seen', an action finished before the main verb."),
    ],
}

# ---------------------------------------------------------------- unit 28
AUTHORED["28"] = {
    "title": "पृष्ठपार्श्वोदरं मृद्यात्",
    "question": "Which further measures does verse 28 order for the patient whose basti has risen?",
    "rule": ("Knead the back, sides and belly with hot hands, (him) face downward; pull (him) by the hair "
             "and shake (him); frighten (him) with vyāla (snakes or savage beasts) and fanged (ones)."),
    "limits": ("The person is not named; the verse continues the treatment of 05.06.52-53, and the list of "
               "frightening things goes on in 05.06.56. अधोमुखं is taken as the person (face downward). "
               "The print writes ळ for ल in व्याळ, a print habit."),
    "explain_hi": ("यह श्लोक 05.06.52-53 के उपचार को आगे बढ़ाता है; रोगी का नाम नहीं लिया गया। "
                   "रोगी को अधोमुख यानी मुँह नीचे करके उसकी पीठ, पार्श्व यानी बगलें और उदर गरम हाथों से मसले। "
                   "फिर बालों से खींचकर उसे हिलाए। "
                   "और व्याल यानी साँप या हिंसक पशु, तथा दाढ़ वाले पशुओं से उसे डराए; डराने की सूची 05.06.56 में चलती है।"),
    "hook": "मुँह नीचे, गरम हाथों से मालिश, बाल पकड़ कर झटका, फिर साँप और दाढ़ वाले पशुओं का डर।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "With what are the back, sides and belly kneaded, by verse 28?",
            ("With hot hands",
             "करैः उष्णैः मृद्यात्: knead with hot hands."),
            [("With warm oil and salt",
              "Oil and salt are not named in verse 28."),
             ("With cloths soaked in cold water",
              "Cold water is used on the face in 05.06.52, not for kneading."),
             ("With a paste of mustard",
              "Mustard belongs to the head in 05.06.68.")],
            "करैः उष्णैः: both instrumental plural, 'with hot hands'.",
            "कर = hand; उष्ण = hot; मृद्यात् = should knead."),
        match(1, "Match each word of verse 28 to its meaning.",
              [["पृष्ठ", "back"], ["पार्श्व", "side"], ["उदर", "belly"],
               ["केश", "hair"], ["अधोमुख", "face downward"]],
              "Three parts are kneaded; the hair is pulled; the patient lies face downward.",
              "पृष्ठ = back; पार्श्व = side; उदर = belly; केश = hair; अधोमुख = face down."),
        order(2, "Put these words of verse 28 in the verse's order.",
              ["पृष्ठपार्श्वोदरं", "मृद्यात्", "करैः उष्णैः", "केशेषु आक्षिप्य", "धुन्वीत", "भीषयेत्"],
              "Knead the back, sides, belly with hot hands; pull by the hair, shake; frighten.",
              "पृष्ठपार्श्वोदरं · मृद्यात् · करैरुष्णैः ‖ केशेष्वाक्षिप्य · धुन्वीत · भीषयेत्.",
              role="extend",
              teaches="Verse 28 has three acts in order: kneading (मृद्यात्), shaking by the hair (धुन्वीत), frightening (भीषयेत्)."),
        mcq("discriminate", 3, "Which split of केशेष्वाक्षिप्य is right?",
            ("केशेषु + आक्षिप्य",
             "उ before a different vowel becomes व्: केशेषु + आक्षिप्य → केशेष्वाक्षिप्य."),
            [("केशेषु + अक्षिप्य",
              "Short अ would print केशेष्वक्षिप्य; the print has वा, from long आ."),
             ("केशेष्व + आक्षिप्य",
              "केशेष्व is not a word; the व् is the changed उ of केशेषु."),
             ("केशेषू + आक्षिप्य",
              "The locative plural is केशेषु with short उ.")],
            "केशेषु (in the hair, loc. pl.) + आक्षिप्य (having pulled).",
            "उ + unlike vowel → व्."),
        mcq("apply", 4, "Verse 28 says the patient is to be frightened. With what?",
            ("Snakes or savage beasts, and fanged (ones)",
             "भीषयेद् व्यालदंष्ट्रिभिः: with vyāla and daṃṣṭrin."),
            [("Loud drums, conches and sudden shouting",
              "No sound is named in verse 28."),
             ("A threat that a stronger basti will follow",
              "No such threat is named in verse 28."),
             ("A dark, locked room with no lamp",
              "Darkness is not named in verse 28.")],
            "व्याल = snake or savage beast; दंष्ट्रिन् = fanged (animal).",
            "भीषयेत् व्यालदंष्ट्रिभिः = frighten with vyāla and fanged (ones)."),
        mcq("transfer", 5,
            "Like करैः उष्णैः मृद्यात् (knead with hot hands), what does the new sentence हस्तैः शीतैः मृद्यात् mean?",
            ("One should knead with cold hands",
             "हस्तैः शीतैः: noun and adjective both instrumental plural, 'with cold hands'."),
            [("One should knead the cold hands",
              "'The hands' as object would need the accusative हस्तान्."),
             ("The cold hands should knead",
              "The subject would be nominative हस्ताः शीताः."),
             ("One should knead the hands in the cold",
              "शीतैः agrees with हस्तैः; it is not a locative 'in the cold'.")],
            "Adjective agrees with its noun in case and number: करैः उष्णैः, हस्तैः शीतैः.",
            "-ऐः = instrumental plural, 'with'.",
            teaches="करैः उष्णैः shows an adjective agreeing with its noun in the instrumental plural: 'with hot hands'."),
    ],
}

# ---------------------------------------------------------------- unit 29
AUTHORED["29"] = {
    "title": "बस्तिरेति तथा ह्यधः",
    "question": "With what else is the patient frightened, why, and what is done to the throat?",
    "rule": ("(Frighten him) with weapons, firebrands (ulkā) and the king's men: for thus the basti goes "
             "downward. And one should make pressure on the throat with the hands and cloths, as if he were dying."),
    "limits": ("The verb 'frighten' is carried from 05.06.55. म्रियते यथा is taken as 'as if he were dying'; "
               "the literal 'so that he dies' is not intended (data note). The verse does not say how long "
               "or how hard the throat is pressed."),
    "explain_hi": ("क्रिया ‘भीषयेत्’ 05.06.55 से आती है: शस्त्रों, उल्का यानी जलती लकड़ी या मशाल, और राजपुरुषों यानी "
                   "राजा के सिपाहियों से रोगी को डराए। "
                   "कारण भी कहा है: इस प्रकार बस्ति नीचे जाती है। "
                   "फिर हाथों और वस्त्रों से गले पर दबाव करे, मानो वह मर रहा हो। "
                   "‘म्रियते यथा’ का यह अर्थ डेटा की व्याख्या है; दबाव कितना और कितनी देर, नहीं कहा।"),
    "hook": "हथियार, मशाल, सिपाही से डर; गला दबाओ: बस्ति नीचे चली।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "With what is pressure made on the throat, by verse 29?",
            ("With the hands and cloths",
             "पाणिवस्त्रैः गलापीडं कुर्यात्: with hands and cloths."),
            [("With a rope and a stick",
              "Rope and stick are not named in verse 29."),
             ("With hot hands and oil",
              "Hot hands knead the back and belly in 05.06.54; no oil here."),
             ("With mustard and a cloth",
              "Mustard is not named in verse 29.")],
            "पाणि-वस्त्रैः: a dvandva in the instrumental plural, 'with hands and cloths'.",
            "पाणि = hand; वस्त्र = cloth; गलापीड = pressure on the throat."),
        match(1, "Match each word of verse 29 to its meaning.",
              [["शस्त्र", "weapon"], ["उल्का", "firebrand"], ["राजपुरुष", "king's man"],
               ["पाणि", "hand"], ["गल", "throat"]],
              "Three things frighten; hands and cloths press the throat.",
              "शस्त्र = weapon; उल्का = firebrand; राजपुरुष = king's man; पाणि = hand; गल = throat."),
        order(2, "Put these phrases of verse 29 in the verse's order.",
              ["शस्त्रोल्काराजपुरुषैः", "बस्तिरेति तथा ह्यधः", "पाणिवस्त्रैः", "गलापीडं कुर्यात्"],
              "First the frightening things and the reason; then the throat pressure with hands and cloths.",
              "शस्त्रोल्काराजपुरुषैः · बस्तिरेति तथा ह्यधः ‖ पाणिवस्त्रैः · गलापीडं कुर्यात्.",
              role="extend",
              teaches="Verse 29 gives a reason inside the list: तथा हि अधः एति, 'for thus the basti goes downward'."),
        mcq("discriminate", 3, "Which split of ह्यधः is right?",
            ("हि + अधः",
             "इ before a different vowel becomes य्: हि + अधः → ह्यधः."),
            [("ह्य + अधः",
              "ह्य is not a word, and अ + अ would give a long आ (ह्याधः)."),
             ("हि + आधः",
              "हि + आ would print ह्याधः, with a long आ."),
             ("हि + धः",
              "हि + धः would print हिधः; and धः is not a word.")],
            "हि (for) + अधः (downward).",
            "इ + unlike vowel → य्."),
        mcq("apply", 4, "A patient is frightened with weapons and firebrands. What does verse 29 say this does to the basti?",
            ("The basti goes downward",
             "बस्तिरेति तथा ह्यधः: for thus the basti goes downward."),
            [("It comes out through the nose",
              "That is the fault of 05.06.50-51, not the effect of frightening."),
             ("It is absorbed by the body",
              "Absorption is not named in verse 29."),
             ("It rises up to the head",
              "Verse 29 says downward (अधः), not to the head.")],
            "अधः एति = goes downward; हि gives the reason.",
            "बस्तिः अधः एति = the basti goes down."),
        mcq("transfer", 5,
            "By the pattern of पाणिवस्त्रैः (with hands and cloths), what does the new word तैलघृतैः mean?",
            ("With oil and ghee",
             "A dvandva with the instrumental plural -ऐः: 'with oil and ghee'."),
            [("Oil cooked in ghee",
              "A dvandva joins equals; no cooking is stated."),
             ("Of oil and ghee",
              "'Of' needs the genitive -आनाम्, not -ऐः."),
             ("Oil and ghee (as subject)",
              "The subject form would be तैलघृतानि.")],
            "dvandva + -ऐः = 'with X and Y'.",
            "पाणिवस्त्रैः = with hands and cloths; तैलघृतैः = with oil and ghee.",
            teaches="पाणिवस्त्रैः is a dvandva (hand and cloth) in the instrumental plural: 'with hands and cloths'."),
    ],
}

# ---------------------------------------------------------------- unit 30
AUTHORED["30"] = {
    "title": "प्राणोदाननिरोधाद्धि",
    "question": "What does verse 30 give as the working of the measures: which winds are obstructed and which draws the basti away?",
    "rule": ("From the obstruction of prāṇa and udāna, the apāna wind, whose course is the more fully "
             "established, quickly draws that basti away."),
    "limits": ("सुप्रसिद्धतरायणः is rendered literally ('whose course is more fully established'); that apāna's "
               "downward course is freed is an interpretation (probable), not in the words. अपकर्षति means "
               "draws away; 'down' is not in the word. The verse does not name the measures it explains."),
    "explain_hi": ("‘हि’ (क्योंकि) से यह श्लोक कारण देता है। "
                   "प्राण और उदान वायु के निरोध यानी रुकने से, अपान वायु, जिसका मार्ग और अधिक भली-भाँति स्थापित है, "
                   "उस बस्ति को शीघ्र ही खींच ले जाता है। "
                   "‘सुप्रसिद्धतरायण’ का अर्थ शब्दशः रखा है; अपान का नीचे का मार्ग खुलता है, यह केवल सम्भावित व्याख्या है। "
                   "‘अपकर्षति’ = खींच ले जाता है; ‘नीचे’ शब्द में नहीं है।"),
    "hook": "प्राण-उदान रुके, अपान का रास्ता पक्का: अपान बस्ति को झट खींच ले।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "Which wind draws the basti away, by verse 30?",
            ("Apāna",
             "अपानः पवनः बस्तिं तम् आशु एव अपकर्षति."),
            [("Prāṇa",
              "Prāṇa is obstructed in verse 30; it does not draw the basti."),
             ("Udāna",
              "Udāna is obstructed with prāṇa; it does not draw the basti."),
             ("Samāna",
              "Samāna is not named in verse 30.")],
            "The subject of अपकर्षति is अपानः पवनः.",
            "अपान draws the basti away."),
        match(1, "Match each word of verse 30 to its meaning.",
              [["निरोध", "obstruction"], ["अयन", "course"], ["पवन", "wind"],
               ["आशु", "quickly"], ["अपकर्षति", "draws away"]],
              "These words carry the cause (obstruction) and the result (the wind draws the basti away quickly).",
              "निरोध = obstruction; अयन = course; पवन = wind; आशु = quickly; अपकर्षति = draws away."),
        order(2, "Put these words of verse 30 in the verse's order.",
              ["प्राणोदाननिरोधात्", "सुप्रसिद्धतरायणः", "अपानः पवनः", "बस्तिं तम्", "आशु एव अपकर्षति"],
              "Cause first (the obstruction), then the wind described, then what it does to the basti.",
              "प्राणोदाननिरोधाद्धि · सुप्रसिद्धतरायणः ‖ अपानः पवनो · बस्तिं तम् · आश्वेवापकर्षति.",
              role="extend",
              teaches="Verse 30 runs from cause (ablative निरोधात्) to the wind (अपानः) to its act (अपकर्षति)."),
        mcq("discriminate", 3, "Which split of प्राणोदान is right?",
            ("प्राण + उदान",
             "अ + उ → ओ: प्राण + उदान → प्राणोदान."),
            [("प्राणः + उदान",
              "-अः before उ drops the visarga and does not merge: प्राण उदान."),
             ("प्राण + ओदान",
              "ओदान is not a word, and अ + ओ would give औ."),
             ("प्राणो + दान",
              "प्राणो is not a stem; दान is not the second wind.")],
            "प्राण and उदान, two winds, joined in a dvandva.",
            "अ + उ → ओ."),
        mcq("apply", 4, "A physician wants apāna to draw a risen basti away. By verse 30, which winds must be obstructed?",
            ("Prāṇa and udāna",
             "प्राणोदाननिरोधात्: from the obstruction of prāṇa and udāna."),
            [("Apāna and vyāna",
              "Apāna is the one that draws; vyāna is not named."),
             ("Prāṇa and apāna",
              "Apāna draws the basti; it is not obstructed."),
             ("Udāna and apāna",
              "Apāna draws the basti; only udāna of this pair is obstructed.")],
            "Obstructed: prāṇa and udāna; drawing: apāna.",
            "प्राण + उदान रुके → अपान खींचे."),
        mcq("transfer", 5,
            "Like प्राणोदाननिरोधात् (from the obstruction of prāṇa and udāna), what does the new sentence वेगनिरोधात् शूलं भवति mean?",
            ("Pain arises from holding back the urge",
             "-आत् is an ablative of cause: 'from (because of) the obstruction of the urge'."),
            [("Holding back the urge arises from pain",
              "शूलम् is the subject that arises; the ablative names the cause."),
             ("Pain holds back the urge",
              "There is no verb 'holds back'; भवति = arises, is."),
             ("In holding back the urge there is pain",
              "'In' would need the locative निरोधे.")],
            "Ablative -आत् of a cause = 'from, because of'.",
            "निरोधात् = from obstruction.",
            teaches="निरोधात् is an ablative of cause: 'from (because of) the obstruction'."),
    ],
}

# ---------------------------------------------------------------- unit 31
AUTHORED["31"] = {
    "title": "कुष्ठक्रमुककल्कम्",
    "question": "Which paste does verse 31 give to drink, and why does it work?",
    "rule": ("Make (him) drink a paste of kuṣṭha (costus) and kramuka (probably areca nut) joined with sour; "
             "from heat, sharpness and flowing nature it too brings the basti into the natural direction."),
    "limits": ("Which sour (amla) substance is not said. kuṣṭha here is the drug costus (standard), not the skin "
               "disease; kramuka = areca nut is probable. No dose is given. 'saḥ' (it) is the paste."),
    "explain_hi": ("कुष्ठ यानी कूठ और क्रमुक यानी सम्भवतः सुपारी का कल्क यानी पिसी लुगदी, अम्ल से युक्त, रोगी को पिलाए। "
                   "यहाँ कुष्ठ औषध है, कोढ़ रोग नहीं। "
                   "कारण दूसरी पंक्ति में है: उष्णता, तीक्ष्णता और सरत्व यानी बहने वाले गुण से यह कल्क भी बस्ति को "
                   "अनुलोम यानी स्वाभाविक दिशा में ले आता है। "
                   "कौन-सा अम्ल, और कितनी मात्रा, यह नहीं कहा।"),
    "hook": "कूठ-सुपारी की खट्टी लुगदी: गरम, तीखी, बहने वाली, बस्ति को सही दिशा दे।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "With what is the paste of verse 31 joined?",
            ("With something sour",
             "अम्लसंयुतम्: joined with sour (amla); the sour item is not named."),
            [("With honey",
              "Honey is not named in verse 31."),
             ("With ghee",
              "Ghee is not named in verse 31."),
             ("With milk",
              "Milk is not named in verse 31.")],
            "अम्ल-संयुत = joined with sour.",
            "अम्ल = sour; संयुत = joined with."),
        match(1, "Match each word of verse 31 to its meaning.",
              [["कुष्ठ", "costus (a drug)"], ["क्रमुक", "probably areca nut"], ["कल्क", "paste"],
               ["अम्ल", "sour"], ["तैक्ष्ण्य", "sharpness"]],
              "Two drugs make the paste; it is joined with sour and works by its qualities.",
              "कुष्ठ = costus; क्रमुक = areca nut (probable); कल्क = paste; अम्ल = sour; तैक्ष्ण्य = sharpness."),
        order(2, "Put these words of verse 31 in the verse's order.",
              ["कुष्ठक्रमुककल्कं", "अम्लसंयुतं", "औष्ण्यात्", "तैक्ष्ण्यात्", "सरत्वात्", "अनुलोमयेत्"],
              "The paste and what it is joined with; then the three qualities; then what it does.",
              "कुष्ठक्रमुककल्कं · अम्लसंयुतं ‖ औष्ण्यात् · तैक्ष्ण्यात् · सरत्वात् · अनुलोमयेत्.",
              role="extend",
              teaches="Verse 31 gives three causes in the ablative: heat (औष्ण्यात्), sharpness (तैक्ष्ण्यात्), flowing nature (सरत्वात्)."),
        mcq("discriminate", 3, "What does कुष्ठ name in verse 31, by the card?",
            ("The drug costus",
             "Here kuṣṭha is a drug in the paste (costus, standard), not the disease."),
            [("The skin disease of that name",
              "The word also names a skin disease, but here it is a drug in a paste."),
             ("A kind of sour drink",
              "The sour is अम्ल, a separate word."),
             ("The areca nut",
              "Areca nut (probable) is kramuka, the second drug.")],
            "Same word, two senses: here the drug, since it forms a kalka with kramuka.",
            "कुष्ठ (औषध) = costus."),
        multi("apply", 4, "Why does the paste of verse 31 bring the basti into the natural direction? Choose all the reasons it gives.",
              [("Its heat", "Right: औष्ण्यात्."),
               ("Its sharpness", "Right: तैक्ष्ण्यात्."),
               ("Its flowing nature", "Right: सरत्वात्."),
               ("Its coldness", "Coldness is not named; heat is."),
               ("Its heaviness", "Heaviness is not named in verse 31.")],
              [0, 1, 2],
              "Three ablatives of cause: औष्ण्य, तैक्ष्ण्य, सरत्व.",
              "उष्ण · तीक्ष्ण · सर → अनुलोमन."),
        mcq("transfer", 5,
            "By the pattern of सरत्वात् (from flowing nature), what does the new word गुरुत्वात् mean?",
            ("From heaviness",
             "-त्व makes an abstract noun (गुरु heavy → गुरुत्व heaviness); -आत् is the ablative 'from'."),
            [("Heavy (ones)",
              "That would be the adjective गुरवः, not an abstract noun."),
             ("Into heaviness",
              "'Into' would not be an ablative."),
             ("Of the heavy one",
              "'Of' would need the genitive गुरोः.")],
            "Adjective + -त्व = quality; + -आत् = 'from, because of'.",
            "सरत्वात् = from flowing nature; गुरुत्वात् = from heaviness.",
            teaches="सरत्वात् is the ablative of सरत्व (abstract noun from सर, flowing): 'from flowing nature'."),
    ],
}

# ---------------------------------------------------------------- unit 32
AUTHORED["32"] = {
    "title": "त्रिवृत्पथ्याकल्कम्",
    "question": "What second downward remedy does verse 32 give, and which basti for the pakvāśaya?",
    "rule": ("Or a paste of trivṛt (turpeth) and pathyā (chebulic myrobalan) with cow's urine, a downward "
             "anulomana. When (it) is in the pakvāśaya, in one who has been sweated: a nirūha of the daśamūla."),
    "limits": ("Line 1 has no verb; whether it carries 'make drink' from 05.06.60 is an open question. "
               "The ten roots are not listed. What is situated in the pakvāśaya is not stated. "
               "The nirūha sentence goes on in 05.06.64."),
    "explain_hi": ("पहली पंक्ति एक और उपाय देती है: गोमूत्र के साथ त्रिवृत् यानी निशोथ और पथ्या यानी हरड़ का कल्क, "
                   "जो नीचे की ओर अनुलोमन करता है। यहाँ पथ्या औषध का नाम है, ‘हितकर’ अर्थ नहीं। "
                   "दूसरी पंक्ति स्थान के अनुसार उपाय शुरू करती है: पक्वाशय यानी बड़ी आँत में स्थित होने पर, स्वेदित रोगी को, "
                   "दशमूल का निरूह। "
                   "दशमूल की दस जड़ें पाठ में नहीं गिनाईं; वाक्य 05.06.64 में चलता है।"),
    "hook": "गोमूत्र में निशोथ-हरड़ नीचे सरकाए; पक्वाशय में हो तो दशमूल का निरूह।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "With what is the trivṛt and pathyā paste given, by verse 32?",
            ("With cow's urine",
             "गोमूत्रेण त्रिवृत्पथ्याकल्कम्: the paste with cow's urine."),
            [("With something sour",
              "Sour goes with the costus paste of 05.06.60, not this one."),
             ("With honey",
              "Honey is not named in verse 32."),
             ("With warm milk",
              "Milk is not named in verse 32.")],
            "गो-मूत्रेण: instrumental, 'with cow's urine'.",
            "गोमूत्र = cow's urine."),
        match(1, "Match each word of verse 32 to its meaning.",
              [["त्रिवृत्", "turpeth"], ["पथ्या", "chebulic myrobalan"], ["गोमूत्र", "cow's urine"],
               ["पक्वाशय", "large intestine"], ["दाशमूलिक", "of the ten roots"]],
              "Two drugs and a liquid in line 1; a seat and a basti in line 2.",
              "त्रिवृत् = turpeth; पथ्या = chebulic myrobalan; गोमूत्र = cow's urine; पक्वाशय = large intestine; दाशमूलिक = of daśamūla."),
        order(2, "Put these words of verse 32 in the verse's order.",
              ["गोमूत्रेण", "त्रिवृत्पथ्याकल्कं", "अधोऽनुलोमनं", "पक्वाशयस्थिते", "स्विन्ने", "निरूहो दाशमूलिकः"],
              "Line 1: the paste with cow's urine, a downward anulomana; line 2: seat, sweating, the nirūha.",
              "गोमूत्रेण · त्रिवृत्पथ्याकल्कं · अधोऽनुलोमनं ‖ पक्वाशयस्थिते · स्विन्ने · निरूहो दाशमूलिकः.",
              role="extend",
              teaches="Verse 32 line 2 opens the remedies by seat: for the pakvāśaya, a daśamūla nirūha to one sweated."),
        mcq("discriminate", 3, "What does पथ्या name in verse 32, by the card?",
            ("The drug chebulic myrobalan",
             "पथ्या is taken as the drug (haritakī, हरड़), standard."),
            [("Wholesome food in general",
              "That is the plain meaning of the word, not used here."),
             ("A kind of sour gruel",
              "No gruel is named in verse 32."),
             ("One of the ten roots",
              "The ten roots are not listed; pathyā is in the paste of line 1.")],
            "In a kalka with trivṛt, पथ्या is a drug name.",
            "पथ्या (औषध) = chebulic myrobalan."),
        mcq("apply", 4, "When (it) is situated in the pakvāśaya and the patient has been sweated, which basti does verse 32 name?",
            ("A nirūha of the daśamūla",
             "पक्वाशयस्थिते स्विन्ने निरूहो दाशमूलिकः."),
            [("A paste of costus and areca nut",
              "That paste is drunk (05.06.60); it is not the pakvāśaya basti."),
             ("Nasal medication and smoke",
              "Those are for the head (05.06.68)."),
             ("An oil basti with rock salt",
              "Oil and rock salt belong to the chest basti of 05.06.67.")],
            "Seat pakvāśaya → daśamūla nirūha, after sweating.",
            "पक्वाशय → दाशमूलिक निरूह."),
        mcq("transfer", 5,
            "Like पक्वाशयस्थिते (when situated in the pakvāśaya), what does the new word कण्ठस्थिते mean?",
            ("When (it) is situated in the throat",
             "-स्थिते is a locative: 'when (it) is situated in'; कण्ठ = throat."),
            [("From the place of the throat",
              "'From' would need an ablative, not -स्थिते."),
             ("The throat that stands (subject)",
              "स्थित means 'situated', not 'stands', and -स्थिते is a locative, not a subject form (that would be कण्ठस्थितः, 'situated in the throat')."),
             ("Having placed the throat",
              "स्थित is a past participle 'situated', not 'having placed'.")],
            "X-स्थिते (locative) = 'when (it) is situated in X'.",
            "पक्वाशयस्थिते = situated in the pakvāśaya.",
            teaches="पक्वाशयस्थिते is a locative tat-puruṣa: 'when (it) is situated in the pakvāśaya'."),
    ],
}

# ---------------------------------------------------------------- unit 33
AUTHORED["33"] = {
    "title": "यवकोलकुलत्थैश्च",
    "question": "With which drugs is the pakvāśaya nirūha prepared, and what is the second basti?",
    "rule": ("The nirūha is to be given with yava (barley), kola (probably jujube) and kulattha (horse gram) "
             "prepared in urine; or a basti with shoots of vaṃśa (probably bamboo) with amṛtā (probably giloy), "
             "cooked in cow's urine."),
    "limits": ("Which animal's urine for the first basti is not said. The second list goes on in 05.06.66. "
               "kola, vaṃśa and amṛtā are probable identifications (amṛtā is used for other drugs too). No measures given."),
    "explain_hi": ("यह 05.06.63 का वाक्य पूरा करता है: दशमूल का निरूह, मूत्र में साधित यव, कोल यानी सम्भवतः बेर और "
                   "कुलत्थ यानी कुलथी के साथ देना चाहिए। "
                   "दूसरा विकल्प: गोमूत्र में पकाए, अमृता यानी सम्भवतः गिलोय सहित वंश यानी सम्भवतः बाँस के पल्लवों "
                   "(कोमल अंकुरों) वाली बस्ति। "
                   "पहली बस्ति में किसका मूत्र, यह नहीं कहा; दूसरी सूची 05.06.66 में आगे चलती है।"),
    "hook": "मूत्र में यव-बेर-कुलथी; या गोमूत्र में गिलोय और बाँस के अंकुर।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In what are yava, kola and kulattha prepared, by verse 33?",
            ("In urine",
             "मूत्रसाधितैः: prepared in urine."),
            [("In milk",
              "Milk is not named in verse 33."),
             ("In oil",
              "Oil is not named in verse 33."),
             ("In sour gruel",
              "No gruel is named in verse 33.")],
            "मूत्र-साधित = prepared in urine (the animal is not named here).",
            "साधित = prepared."),
        match(1, "Match each drug of verse 33 to its identification on the card.",
              [["यव", "barley"], ["कोल", "probably jujube"], ["कुलत्थ", "horse gram"],
               ["वंश", "probably bamboo"], ["अमृता", "probably giloy"]],
              "Three drugs of the first basti, two of the second.",
              "यव = barley; कोल = jujube (probable); कुलत्थ = horse gram; वंश = bamboo (probable); अमृता = giloy (probable)."),
        order(2, "Put these words of verse 33 in the verse's order.",
              ["यवकोलकुलत्थैः", "विधेयः", "मूत्रसाधितैः", "बस्तिः", "गोमूत्रसिद्धैः", "सामृतावंशपल्लवैः"],
              "Line 1: the three drugs, to be given, prepared in urine; line 2: a basti, cooked in cow's urine, with amṛtā and bamboo shoots.",
              "यवकोलकुलत्थैश्च · विधेयो · मूत्रसाधितैः ‖ बस्तिर् · गौमूत्रसिद्धैर्वा · सामृतावंशपल्लवैः.",
              role="extend",
              teaches="Verse 33 gives two bastis joined by वा: yava, kola and kulattha prepared in urine, or shoots cooked in cow's urine."),
        mcq("discriminate", 3, "Which drug does verse 33 join with amṛtā (sa-amṛtā)?",
            ("Shoots of vaṃśa (probably bamboo)",
             "सामृतावंशपल्लवैः: shoots of vaṃśa with amṛtā."),
            [("Kulattha (horse gram)",
              "Kulattha belongs to the first basti, with yava and kola."),
             ("Pathyā (chebulic myrobalan)",
              "Pathyā is in the paste of 05.06.62, not here."),
             ("Kramuka (probably areca nut)",
              "Kramuka is in the paste of 05.06.60.")],
            "स (with) + अमृता + वंश-पल्लवैः: amṛtā goes with the bamboo shoots.",
            "सामृता = स + अमृता, 'with amṛtā'."),
        multi("apply", 4, "A physician makes the first basti of verse 33 (prepared in urine). Which drugs go in?",
              [("Yava (barley)", "Right: यव."),
               ("Kola (probably jujube)", "Right: कोल."),
               ("Kulattha (horse gram)", "Right: कुलत्थ."),
               ("Amṛtā (probably giloy)", "Amṛtā is in the second basti, cooked in cow's urine."),
               ("Shoots of vaṃśa", "The bamboo shoots are in the second basti.")],
              [0, 1, 2],
              "First basti: yava, kola, kulattha in urine; second: amṛtā and vaṃśa shoots in cow's urine.",
              "यव-कोल-कुलत्थ ‖ अमृता-वंशपल्लव."),
        mcq("transfer", 5,
            "By the pattern of विधेयः (is to be administered), what does the new sentence स्वेदः विधेयः mean?",
            ("Sweating is to be administered",
             "विधेय is a gerundive: 'is to be done/administered'; it agrees with स्वेदः."),
            [("Sweating was administered",
              "A gerundive is not a past form."),
             ("Sweating administers (it)",
              "विधेयः is passive in sense: the sweating is what is administered."),
             ("Sweating will not be given",
              "There is no negative and no future in the sentence.")],
            "Gerundive -य/-तव्य/-अनीय = 'is to be done'.",
            "विधेयः = is to be administered.",
            teaches="विधेयः is a gerundive of vi-√dhā: 'is to be administered', agreeing with its noun."),
    ],
}

# ---------------------------------------------------------------- unit 34
AUTHORED["34"] = {
    "title": "पूतीकरञ्जत्वक्पत्र",
    "question": "Which further drugs does unit 34 add to the basti cooked in cow's urine?",
    "rule": ("The list of 05.06.65 goes on: with the bark and leaf of pūtīkarañja, śaṭhī, devāhva (on a "
             "conjectural reading) and rohiṣa."),
    "limits": ("The printed देवान्व is not a word; devāhva (probably devadāru) is a conjecture. pūtīkarañja and "
               "śaṭhī are of disputed identity; rohiṣa is probably palmarosa grass. Bark and leaf may also be read "
               "as separate items. No question rests on devāhva or on the identity of the disputed drugs."),
    "explain_hi": ("यह इकाई 05.06.65 की बस्ति (गोमूत्र में पकाई) के द्रव्यों की सूची आगे बढ़ाती है। "
                   "पूतिकरंज की छाल और पत्ते (पहचान विवादित; कंजा एक सुझाव), शठी (पहचान विवादित), "
                   "अनुमानित पाठ पर देवाह्व यानी सम्भवतः देवदारु, और रोहिष यानी सम्भवतः रूसा घास। "
                   "छपा शब्द ‘देवान्व’ कोई शब्द नहीं, इसलिए देवाह्व केवल अनुमान है। "
                   "सब शब्द एक समास में तृतीया बहुवचन ‘-ऐः’ (से) में हैं।"),
    "hook": "पूतिकरंज की छाल-पत्ते, शठी, देवदारु (अनुमानित पाठ), रूसा घास: गोमूत्र वाली बस्ति में।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "Unit 34 continues a list from 05.06.65. What is it a list of?",
            ("Drugs of the basti cooked in cow's urine",
             "It adds ingredients to the basti of 05.06.65 (amṛtā and bamboo shoots)."),
            [("Signs of the basti thrown upward",
              "The signs (fainting, nausea) are in 05.06.51."),
             ("Foods for the patient after the basti",
              "No food is named in unit 34."),
             ("Drugs for nasal medication of the head",
              "Nasal medication for the head comes in 05.06.68.")],
            "The instrumental plural -ऐः ties the unit to the basti of 05.06.65.",
            "Unit 34 = more drugs for the cow's-urine basti."),
        match(1, "Match each word of unit 34 to its meaning on the card.",
              [["त्वक्", "bark"], ["पत्र", "leaf"], ["रोहिष", "probably palmarosa grass"],
               ["शठी", "a drug of disputed identity"]],
              "Bark and leaf are of pūtīkarañja; śaṭhī is disputed; rohiṣa is a scented grass (probable).",
              "त्वक् = bark; पत्र = leaf; रोहिष = palmarosa (probable); शठी = disputed."),
        fill(2, "After त्वक् (bark), unit 34 names ____ (leaf). Type it in Devanagari or in English letters (e.g. dharma).",
             accepts("पत्र", None, "पत्रम्"),
             "त्वक्पत्र = त्वक् (bark) + पत्र (leaf), here of pūtīkarañja.",
             "पत्र = leaf; with त्वक् it names the bark and leaf of pūtīkarañja.",
             "पत्र = leaf."),
        mcq("discriminate", 3, "How does the card label the identity of pūtīkarañja and śaṭhī?",
            ("Both disputed",
             "The data marks both 'identity disputed'."),
            [("Both standard",
              "Neither has a standard identification on the card."),
             ("Pūtīkarañja probable, śaṭhī standard",
              "Both are disputed, not probable or standard."),
             ("Both unidentified",
              "Proposals exist for both, so they are disputed, not unidentified.")],
            "Disputed: proposals exist but scholars differ.",
            "पूतीकरञ्ज, शठी = विवादित पहचान."),
        order(4, "Put these items of unit 34 in the text's order.",
              ["पूतीकरञ्ज", "त्वक्", "पत्र", "शठी", "रोहिष"],
              "The compound runs pūtīkarañja, bark, leaf, śaṭhī, (devāhva,) rohiṣa.",
              "पूतीकरञ्ज · त्वक् · पत्र · शठी · (देवाह्व, अनुमानित) · रोहिष.",
              role="apply",
              teaches="Unit 34's compound lists pūtīkarañja's bark and leaf, then śaṭhī, devāhva (conjectural) and rohiṣa."),
        mcq("transfer", 5,
            "Like the ending -ऐः of unit 34 (with ...), what does the new word निम्बपत्रैः mean (निम्ब = neem)?",
            ("With neem leaves",
             "-ऐः is the instrumental plural, 'with'; निम्ब-पत्र = neem leaf."),
            [("Neem leaves (as subject)",
              "The subject form would be निम्बपत्राणि."),
             ("Of neem leaves",
              "'Of' would need the genitive निम्बपत्राणाम्."),
             ("In neem leaves",
              "'In' would need the locative निम्बपत्रेषु.")],
            "The whole drug list of unit 34 stands in the instrumental plural -ऐः.",
            "-ऐः = with (instrumental plural).",
            teaches="Unit 34's whole compound ends in -ऐः, the instrumental plural: 'with' these drugs."),
    ],
}

# ---------------------------------------------------------------- unit 35
AUTHORED["35"] = {
    "title": "बस्तिरुरःस्थिते",
    "question": "Which basti does unit 35 give when (it) is situated in the chest?",
    "rule": ("A basti with oil, jaggery and sindhūttha (rock salt), having a paste of purgative drugs, cooked "
             "with the five roots beginning with bilva (bael): when (it) is situated in the chest."),
    "limits": ("The five roots and the purgative drugs are not listed in the text. The oil is not specified. "
               "What is situated in the chest is not said. No measures are given."),
    "explain_hi": ("स्थान के अनुसार उपायों में यह छाती की बारी है। "
                   "छाती में स्थित होने पर ऐसी बस्ति दें: तेल, गुड़ और सिन्धूत्थ यानी सेंधा नमक वाली, विरेचन की औषधों के "
                   "कल्क से युक्त, और बिल्व यानी बेल आदि पाँच मूलों से पकाई हुई। "
                   "पाँच मूल और विरेचन की औषधें पाठ में नहीं गिनाई गईं; परम्परा में बिल्व-आदि पंचमूल प्रसिद्ध है, "
                   "पर यहाँ उसके नाम नहीं दिए।"),
    "hook": "छाती में: तेल-गुड़-सेंधा, विरेचक लुगदी, बेल आदि पंचमूल में पकी बस्ति।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "For which seat is the basti of unit 35 given?",
            ("When (it) is situated in the chest",
             "उरःस्थिते: when situated in the chest."),
            [("When (it) is situated in the head",
              "The head comes in 05.06.68 with nasal medication and smoke."),
             ("When (it) is in the pakvāśaya",
              "The pakvāśaya has the daśamūla nirūha of 05.06.63."),
             ("When (it) is held in the throat",
              "The throat is not a seat named in unit 35.")],
            "उरः-स्थिते: locative, 'when (it) is situated in the chest'.",
            "उरस् = chest."),
        match(1, "Match each word of unit 35 to its meaning.",
              [["तैल", "oil"], ["गुड", "jaggery"], ["सिन्धूत्थ", "rock salt"],
               ["विरेक", "purgation"], ["उरः", "chest"]],
              "Three additions, the purgative paste, and the seat.",
              "तैल = oil; गुड = jaggery; सिन्धूत्थ = rock salt; विरेक = purgation; उरः = chest."),
        order(2, "Put these words of unit 35 in the text's order.",
              ["सतैलगुडसिंधूत्थः", "विरेकौषधकल्कवान्", "बिल्वादिपंचमूलेन", "सिद्धः", "बस्तिः", "उरःस्थिते"],
              "First half: with oil, jaggery, rock salt; with the purgative paste. Second half: cooked with the bilva five roots, the basti, in the chest.",
              "सतैलगुडसिंधूत्थो · विरेकौषधकल्कवान् ‖ बिल्वादिपंचमूलेन · सिद्धो · बस्तिर् · उरःस्थिते.",
              role="extend",
              teaches="Unit 35 describes the basti first and names the seat (उरःस्थिते) last."),
        mcq("discriminate", 3, "With what is the chest basti of unit 35 cooked?",
            ("The five roots beginning with bilva",
             "बिल्वादिपञ्चमूलेन सिद्धः: cooked with the bilva five roots."),
            [("The ten roots (daśamūla)",
              "The daśamūla nirūha is for the pakvāśaya (05.06.63)."),
             ("Bamboo shoots with amṛtā",
              "Those are cooked in cow's urine in 05.06.65."),
             ("A paste of costus and areca",
              "That paste is drunk in 05.06.60.")],
            "बिल्व-आदि पञ्च-मूल = the five roots of which bilva (bael) is the first; the other four are not named.",
            "बिल्वादि पञ्चमूल → उरःस्थ बस्ति."),
        multi("apply", 4, "A physician prepares the chest basti of unit 35. Which does the text put in it?",
              [("Oil", "Right: स-तैल."),
               ("Jaggery", "Right: गुड."),
               ("Rock salt", "Right: सिन्धूत्थ."),
               ("A paste of purgative drugs", "Right: विरेकौषधकल्कवान्."),
               ("Cow's urine", "Cow's urine is not named in unit 35."),
               ("Mustard", "Mustard is for the head (05.06.68).")],
              [0, 1, 2, 3],
              "स-तैल-गुड-सिन्धूत्थ + विरेक-औषध-कल्क, cooked with the bilva five roots.",
              "तेल · गुड़ · सेंधा · विरेचक कल्क."),
        mcq("transfer", 5,
            "By the pattern of कल्कवान् (having a paste), what does the new phrase घृतवान् बस्तिः mean?",
            ("A basti having ghee",
             "-वत् (nom. -वान्) means 'having, possessing'; it agrees with बस्तिः."),
            [("Ghee having a basti",
              "घृतवान् describes बस्तिः; the basti is the one that has."),
             ("A basti without ghee",
              "-वत् means having; 'without' would be a- or nir-."),
             ("A basti cooked like ghee",
              "-वान् means 'having'; nothing in घृतवान् says 'like' or 'cooked'.")],
            "X-वान् = having X.",
            "कल्कवान् = having a paste; घृतवान् = having ghee.",
            teaches="कल्कवान् is the possessive -वत् (nom. -वान्): 'having a paste'."),
    ],
}

# ---------------------------------------------------------------- unit 36
AUTHORED["36"] = {
    "title": "शिरःस्थे नावनं धूमः",
    "question": "What does verse 36 give for the head, and which basti does line 2 begin to describe?",
    "rule": ("When (it) is in the head: nāvana (nasal medication), smoke; the head is to be covered with "
             "sarṣapa (mustard). Line 2 begins a new statement: a basti too hot, sharp, sour, thick, or of one "
             "excessively sweated."),
    "limits": ("The form of mustard (seed, paste) is not said. Line 2 begins the atiyoga statement of "
               "05.06.69-71; its result (verb bhavet) is in 05.06.71, outside this unit. 'Of one excessively "
               "sweated' has no governing noun; the construction is loose."),
    "explain_hi": ("पहली पंक्ति स्थान-क्रम पूरा करती है: सिर में स्थित होने पर नावन यानी नस्य और धूम यानी धुआँ; और सिर को "
                   "सर्षप यानी सम्भवतः सरसों से ढकना चाहिए। सरसों किस रूप में, यह नहीं कहा। "
                   "दूसरी पंक्ति नया कथन शुरू करती है: अति-उष्ण, तीक्ष्ण, अम्ल और घन यानी गाढ़ी बस्ति, अथवा अति-स्वेदित रोगी की। "
                   "इसका परिणाम 05.06.71 में आता है, इस इकाई में नहीं।"),
    "hook": "सिर में: नस्य, धुआँ, सरसों से ढका सिर। फिर नया विषय: बहुत गरम-तीखी-खट्टी-गाढ़ी बस्ति।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "With what is the head to be covered, by verse 36?",
            ("With sarṣapa (mustard)",
             "प्रच्छाद्यं सर्षपैः शिरः: the head to be covered with mustard."),
            [("With a cloth soaked in cold water",
              "Cold water is used on the face in 05.06.52."),
             ("With leaves of pūtīkarañja",
              "Pūtīkarañja is a basti drug in 05.06.66."),
             ("With warm oil and rock salt",
              "Oil and rock salt go in the chest basti of 05.06.67.")],
            "सर्षपैः: instrumental plural, 'with mustard'.",
            "सर्षप = mustard (probable)."),
        match(1, "Match each word of verse 36 to its meaning.",
              [["नावन", "nasal medication"], ["धूम", "smoke"], ["सर्षप", "mustard"],
               ["प्रच्छाद्य", "to be covered"], ["घन", "thick"]],
              "Line 1 has the head measures; घन is one of the faults of the basti in line 2.",
              "नावन = nasal medication; धूम = smoke; सर्षप = mustard; प्रच्छाद्य = to be covered; घन = thick."),
        order(2, "Put the qualities of the basti in line 2 of verse 36 in the verse's order.",
              ["अत्युष्ण", "तीक्ष्ण", "अम्ल", "घन", "अतिस्वेदितस्य"],
              "Too hot, sharp, sour, thick; or (given to) one excessively sweated.",
              "बस्तिः अति-उष्ण-तीक्ष्ण-अम्ल-घनः · अतिस्वेदितस्य वा.",
              role="extend",
              teaches="Line 2 of verse 36 begins the over-application (atiyoga) statement; it goes on to 05.06.71."),
        mcq("discriminate", 3, "Which basti does line 2 of verse 36 describe?",
            ("One too hot, sharp, sour and thick",
             "बस्तिरत्युष्णतीक्ष्णाम्लघनः."),
            [("One cold, small and with little drug",
              "Cold and small bastis are faults of 05.06.36 and 05.06.49."),
             ("One thin and mild, for a harsh koṣṭha",
              "Thin and mild is the basti of 05.06.35, not this line."),
             ("One cooked with the bilva five roots",
              "That is the chest basti of 05.06.67, a remedy.")],
            "बस्तिरत्युष्णतीक्ष्णाम्लघनः: a basti too hot, sharp, sour, thick.",
            "अत्युष्ण · तीक्ष्ण · अम्ल · घन."),
        mcq("apply", 4, "A patient's trouble is situated in the head. Which pair of measures does verse 36 give, besides covering the head?",
            ("Nasal medication and smoke",
             "शिरःस्थे नावनं धूमः."),
            [("Fanning and prāṇāyāma",
              "Those are for fainting (05.06.53)."),
             ("Weapons and firebrands",
              "Those frighten the patient (05.06.56)."),
             ("A daśamūla nirūha and sweating",
              "That is for the pakvāśaya (05.06.63).")],
            "Head: nāvana and dhūma, and the head covered with mustard.",
            "शिरःस्थ → नावन, धूम, सर्षप."),
        mcq("transfer", 5,
            "Like अत्युष्ण (too hot, अति + उष्ण), what does the new phrase अतिशीतः बस्तिः mean?",
            ("A basti that is too cold",
             "अति- = too, excessively; शीत = cold."),
            [("A basti that is not cold",
              "'Not' would be अ-: अशीत."),
             ("A slightly cold basti",
              "अति- means too much, not slightly."),
             ("A basti given after the cold",
              "अतिशीतः is an adjective agreeing with बस्तिः, not a time.")],
            "अति + vowel: इ → य् (अत्युष्ण); before a consonant it stays अति (अतिशीत).",
            "अति- = too, excessively.",
            teaches="अत्युष्ण = अति + उष्ण: अति- means 'too, excessively' (इ → य् before उ)."),
    ],
}

# ================================================================ NOTES_HI
NOTES_HI = {
    "25": ("विश्वास: मध्यम। 05.06.48-51 एक कथन; कर्ता 05.06.49 की ‘बस्तिः’, क्रिया ‘निरेति’ 05.06.51 में। "
           "टेक्स्ट-फ़्लैग: छपा ‘कुँर्वंतो’ में अतिरिक्त चन्द्रबिन्दु; खुला प्रश्न (05.06.48): व्याकरण से ‘कुर्वन्’, "
           "छन्द से ‘कुर्वन्तः’ (१६ अक्षर); स्वामी तय करेंगे। खुला प्रश्न (05.06.48): ‘पीडित’ = दबाई गई (बस्ति) या पीड़ित (रोगी), "
           "और हिन्दी में बस्ति का लिंग। टेक्स्ट-फ़्लैग: ‘अग्निग्ध’ कोई शब्द नहीं, ‘अस्निग्ध’ अनुमानित (स/ग का भ्रम); "
           "अ- तीनों (स्निग्ध, लवण, उष्ण) पर लगे या केवल स्निग्ध पर, पक्का नहीं। इन पर प्रश्न नहीं। "
           "संधि जाँची: बस्तिरल्पो ऽल्पभेषजः = बस्तिः + अल्पः + अल्पभेषजः (ः → र्; -अः + अ → -ओऽ); "
           "पीडितो वा = पीडितः + वा।"),
    "26": ("विश्वास: मध्यम। 05.06.48-51 का कथन यहाँ पूरा होता प्रतीत होता है। टेक्स्ट-फ़्लैग: छपा ‘तृडदाह’ में अतिरिक्त अ "
           "(तृट् + दाह = तृड्दाह), अर्ध-पंक्ति १७ अक्षर की हो जाती है; इस वर्तनी पर प्रश्न नहीं। "
           "छपा ‘प्रवर्त्तयन्’ = प्रवर्तयन् (दोहरा त् सामान्य किया)। संधि जाँची: मृदुर्वा = मृदुः + वा; "
           "मारुतेनोर्ध्वं = मारुतेन + ऊर्ध्वम् (अ + ऊ → ओ); विक्षिप्तो मुख… = विक्षिप्तः + मुख… (-अः + घोष → -ओ)। "
           "मूर्च्छा, हृल्लास, दाह के आधुनिक अर्थ मानक।"),
    "27": ("विश्वास: मध्यम। ‘अस्य’ = उसकी (मूर्च्छा और मुख दोनों से)। खुला प्रश्न (05.06.53): ‘आक्लमनाशात्’ शायद "
           "आ + क्लम-नाशात् (थकावट मिटने तक) है, ‘आक्लम’ संज्ञा संदिग्ध। खुला प्रश्न (05.06.53): ‘व्यजेत्’ सम्भवतः "
           "वि-√अज् का विधिलिङ्, नामधातु नहीं; अर्थ ‘पंखा झले’ वही। इन पर प्रश्न नहीं। पंखा झलने वाला नहीं बताया। "
           "संधि जाँची: दृष्ट्वाऽस्य = दृष्ट्वा + अस्य (अवग्रह छपाई की आदत); सिंचेच्छीतांबुना = सिञ्चेत् + शीताम्बुना (त् + श → च्छ); "
           "व्यजेदा… = व्यजेत् + आ…।"),
    "28": ("विश्वास: मध्यम। रोगी का नाम नहीं; 05.06.52-53 का उपचार चलता है। ‘अधोमुखं’ को रोगी का विशेषण (मुँह नीचे) पढ़ा, "
           "नपुंसक ‘उदरम्’ से उसका अर्थपूर्ण अन्वय नहीं बनता। छपा ‘व्याळ’ में ळ = ल (छपाई की आदत)। "
           "‘व्याल’ = साँप या हिंसक पशु; ‘दंष्ट्रिन्’ = दाढ़ वाला पशु; द्वन्द्व पढ़ा गया। "
           "संधि जाँची: पृष्ठपार्श्वोदरं = पृष्ठ + पार्श्व + उदरम् (अ + उ → ओ); करैरुष्णैरधोमुखं = करैः + उष्णैः + अधोमुखम्; "
           "केशेष्वाक्षिप्य = केशेषु + आक्षिप्य (उ → व्); भीषयेद्व्याल… = भीषयेत् + व्याल…।"),
    "29": ("विश्वास: मध्यम। क्रिया ‘भीषयेत्’ 05.06.55 से। ‘उल्का’ = जलती लकड़ी या मशाल (उल्का-पिण्ड भी अर्थ, यहाँ नहीं)। "
           "‘राजपुरुष’ = राजा का आदमी, अधिकारी या सिपाही। ‘म्रियते यथा’ = मानो वह मर रहा हो; शब्दशः ‘जिससे वह मरे’ अभिप्रेत नहीं "
           "(डेटा की टिप्पणी)। संधि जाँची: …पुरुषैर्बस्तिरेति = पुरुषैः + बस्तिः + एति (ः → र्); ह्यधः = हि + अधः (इ → य्); "
           "पाणिवस्त्रैर्गलापीडं = पाणिवस्त्रैः + गल-आपीडम् (अ + आ → आ); कुर्याच्च = कुर्यात् + च।"),
    "30": ("विश्वास: मध्यम। 05.06.58-59 एक कथन; बहुव्रीहि ‘सुप्रसिद्धतरायणः’ (पुं.) ‘अपानः पवनः’ से अन्वित। "
           "‘सुप्रसिद्ध’ शब्दशः ‘भली-भाँति स्थापित’; अपान का नीचे का मार्ग खुलता है, यह सम्भावित व्याख्या है, अनुवाद में नहीं। "
           "‘अपकर्षति’ = खींच ले जाता है; ‘नीचे’ नहीं जोड़ा। संधि जाँची: प्राणोदान = प्राण + उदान (अ + उ → ओ); "
           "निरोधाद्धि = निरोधात् + हि (त् + ह → द्ध); -तर + अयन → -तरायण (र् के बाद ण्); "
           "आश्वेवापकर्षति = आशु + एव + अपकर्षति (उ → व्; अ + अ → आ)। हिन्दी डेटा में ‘अपान वायु … खींच लेती है’ "
           "स्त्रीलिंग है, शब्दावली के अनुसार वायु पुंलिंग।"),
    "31": ("विश्वास: मध्यम। 05.06.60-61 एक कथन; ‘सः’ = 05.06.60 का कल्क। पहचान: कुष्ठ = कूठ, Saussurea costus (मानक; "
           "यहाँ औषध, त्वचा-रोग नहीं); क्रमुक = पूग, सुपारी, Areca catechu (सम्भावित)। ‘अम्ल’ कौन-सा, नहीं कहा। "
           "‘सर’ = बहने वाला गुण, शब्दशः रखा। संधि जाँची: पाययेताम्ल… = पाययेत् + अम्ल…; "
           "औष्ण्यात्तैक्ष्ण्यात्सरत्वाच्च = औष्ण्यात् + तैक्ष्ण्यात् + सरत्वात् + च; सोप्यनुलोमयेत् = सः + अपि + अनुलोमयेत् "
           "(छपाई में अवग्रह नहीं: सोऽपि)।"),
    "32": ("विश्वास: मध्यम। पंक्ति १ बिना क्रिया का वाक्यांश। खुला प्रश्न (05.06.62): ‘-कल्कं’ पुंलिंग हो तो केवल द्वितीया; "
           "तब 05.06.60 का ‘पाययेत्’ यहाँ भी लग सकता है; अनुवाद वही रहता है; इस पर प्रश्न नहीं। ‘पथ्या’ = हरड़ "
           "(हरीतकी का पर्याय), ‘हितकर’ अर्थ नहीं। पहचान: त्रिवृत् = निशोथ, Operculina turpethum (मानक); पथ्या = Terminalia chebula (मानक)। "
           "05.06.63-64 एक कथन (क्रिया ‘विधेयः’ 05.06.64 में); ‘स्थिते’ का कर्ता नहीं कहा। दशमूल के नाम पाठ में नहीं। "
           "संधि जाँची: वा ऽधोऽनुलोमनं = वा + अधः + अनुलोमनम् (अवग्रह; -अः + अ → -ओऽ)।"),
    "33": ("विश्वास: मध्यम। 05.06.63 का निरूह यहाँ कर्ता। ‘मूत्र’ किस पशु का, यहाँ नहीं कहा (गोमूत्र 05.06.62 और 05.06.65 में)। "
           "पंक्ति २ बिना क्रिया की; ‘गौमूत्रसिद्धैः’ = ‘पल्लवैः’ का विशेषण; छपा ‘गौ’ (गो का वृद्धि-रूप)। पहचान: यव = जौ, कुलत्थ = कुलथी "
           "(मानक); कोल = बेर, वंश = बाँस, अमृता = गुडूची/गिलोय (सम्भावित; अमृता दूसरे द्रव्यों का नाम भी)। "
           "संधि जाँची: …कुलत्थैश्च = …कुलत्थैः + च; विधेयो मूत्र… = विधेयः + मूत्र…; सामृता = स + अमृता (अ + अ → आ)।"),
    "34": ("विश्वास: मध्यम। 05.06.65 की सूची चलती है। टेक्स्ट-फ़्लैग: छपा ‘देवान्व’ कोई शब्द नहीं; ‘देवाह्व’ (देवदारु) अनुमानित "
           "(न्व/ह्व का भ्रम); इस पर प्रश्न नहीं। ‘त्वक्पत्र’ को पूतिकरंज की छाल और पत्ता पढ़ा; अलग द्रव्य भी पढ़ा जा सकता है। "
           "पहचान: पूतिकरंज विवादित (Caesalpinia bonduc सुझाव; Holoptelea integrifolia, Pongamia pinnata भी); शठी विवादित "
           "(कपूर कचरी या कचूर, खुला सुझाव); रोहिष = रूसा घास, Cymbopogon martinii (सम्भावित)। संधि: करञ्ज + त्वक् + पत्र … "
           "एक लम्बा समास, अन्त ‘-रोहिषैः’ (तृतीया बहुवचन)।"),
    "35": ("विश्वास: मध्यम। एक छपी पंक्ति में ३२ अक्षर (दो १६-अक्षर अर्ध)। ‘तैल’ कौन-सा, नहीं कहा। बिल्वादि पंचमूल के सदस्य "
           "पाठ में नहीं (परम्परा में बिल्व, अग्निमन्थ, श्योनाक, पाटला, गम्भारी)। ‘उरःस्थिते’ का कर्ता नहीं कहा; "
           "स्थान-क्रम 05.06.68 (सिर) में चलता है। शब्दावली के अनुसार बिल्व = बेल (bael); डेटा के अंग्रेज़ी में "
           "‘wood-apple’ लिखा है जो कपित्थ है। संधि जाँची: …सिंधूत्थो विरेक… = …सिन्धूत्थः + विरेक…; "
           "विरेकौषध = विरेक + औषध (अ + औ → औ); बस्तिरुरःस्थिते = बस्तिः + उरःस्थिते (ः → र्)।"),
    "36": ("विश्वास: मध्यम। पंक्ति १ बिना क्रिया की (तुलना 05.06.67)। ‘प्रच्छाद्यम्’ कृत्य-प्रत्यय (ढकना चाहिए); सरसों किस रूप में, "
           "नहीं कहा। सर्षप = सरसों, Brassica (सम्भावित)। पंक्ति २ से 05.06.69-71 का अतियोग-कथन शुरू (क्रिया ‘भवेत्’ 05.06.71 में)। "
           "‘अतिस्वेदितस्य’ षष्ठी, शासक संज्ञा नहीं, रचना ढीली। संधि जाँची: बस्तिरत्युष्ण… = बस्तिः + अति + उष्ण… (ः → र्; इ → य्); "
           "…तीक्ष्णाम्ल… = तीक्ष्ण + अम्ल (अ + अ → आ); …घनो ऽतिस्वेदितस्य = घनः + अतिस्वेदितस्य (-अः + अ → -ओऽ)।"),
}

# ================================================================ AIDS
AIDS = {
    "25": {
        "frame": "कथन 05.06.48-51 · यहाँ: बस्ति के दोष · क्रिया ‘निरेति’ 05.06.51 में · परिणाम श्लोक २६ में।",
        "chunks": "कुँर्वंतो (फ़्लैग) वेगसंरोधं | पीडितो वा ऽतिमात्रया ‖ अग्निग्ध (अनुमानित: अस्निग्ध) लवणोष्णो वा | बस्तिरल्पो ऽल्पभेषजः",
        "sandhi": "ः → र् स्वर से पहले, फिर -अः + अ → -ओऽ: बस्तिः + अल्पः + अल्पभेषजः → बस्तिरल्पोऽल्पभेषजः।",
        "anchors": "वेग = स्वाभाविक वेग · संरोध = रोकना · अतिमात्रा = अधिक मात्रा · अल्प = थोड़ा · भेषज = औषध।",
    },
    "26": {
        "chain": {"steps": ["दोषयुक्त (श्लोक २५) या मृदु बस्ति", "वायु ने ऊपर फेंकी", "मुख-नासिका से निकली", "मूर्च्छा, हृल्लास, तृष्णा, दाह आदि"]},
        "chunks": "मृदुर्वा मारुतेनोर्ध्वं | विक्षिप्तो मुखनासिकात् ‖ निरेति मूर्च्छाहृल्लास | तृडदाहादीन्प्रवर्त्तयन्",
        "sandhi": "अ + ऊ → ओ: मारुतेन + ऊर्ध्वम् → मारुतेनोर्ध्वम्; -उः → -उर् घोष से पहले: मृदुः + वा → मृदुर्वा।",
        "anchors": "मारुत = वायु · ऊर्ध्वम् = ऊपर · निरेति = निकलती है · मूर्च्छा = बेहोशी · हृल्लास = मिचली · दाह = जलन।",
    },
    "27": {
        "chain": {"steps": ["मूर्च्छा का विकार देखा", "शीतल जल से मुख सींचे", "थकावट मिटने तक पंखा झले", "प्राणायाम कराए"]},
        "chunks": "मूर्च्छाविकारं दृष्ट्वाऽस्य | सिंचेच्छीतांबुना मुखं ‖ व्यजेदाक्लमनाशाच्च | प्राणायामं च कारयेत्",
        "sandhi": "त् + श → च्छ: सिञ्चेत् + शीताम्बुना → सिञ्चेच्छीताम्बुना।",
    },
    "28": {
        "diagram": {"groups": [{"label": "मसलना (गरम हाथ)", "items": ["पृष्ठ", "पार्श्व", "उदर"]},
                               {"label": "झटकना", "items": ["बालों से खींचकर हिलाना"]},
                               {"label": "डराना", "items": ["व्याल", "दंष्ट्री"]}]},
        "chunks": "पृष्ठपार्श्वोदरं मृद्या | त्करैरुष्णैरधोमुखं ‖ केशेष्वाक्षिप्य धुन्वीत | भीषयेद्व्याळदंष्ट्रिभिः",
        "sandhi": "उ → व् भिन्न स्वर से पहले: केशेषु + आक्षिप्य → केशेष्वाक्षिप्य; अ + उ → ओ: पार्श्व + उदरम् → पार्श्वोदरम्।",
        "pegs": "मेरा बनाया चित्र: औंधा लेटा रोगी, पीठ पर गरम हथेलियाँ; कोई उसके बाल पकड़कर झटके; दरवाज़े पर साँप और दाँत दिखाता बाघ।",
    },
    "29": {
        "diagram": {"groups": [{"label": "डराने वाले", "items": ["शस्त्र", "उल्का (मशाल)", "राजपुरुष"]},
                               {"label": "कारण", "items": ["इससे बस्ति नीचे जाती है"]},
                               {"label": "गले पर दबाव", "items": ["हाथ", "वस्त्र"]}]},
        "chunks": "शस्त्रोल्काराजपुरुषै | र्बस्तिरेति तथा ह्यधः ‖ पाणिवस्त्रैर्गलापीडं | कुर्याच्च म्रियते यथा",
        "sandhi": "इ → य् भिन्न स्वर से पहले: हि + अधः → ह्यधः; ः → र्: पुरुषैः + बस्तिः → पुरुषैर्बस्तिः।",
        "anchors": "शस्त्र = हथियार · उल्का = जलती लकड़ी · राजपुरुष = राजा का सिपाही · पाणि = हाथ · गल = गला · आपीड = दबाव।",
    },
    "30": {
        "chain": {"steps": ["प्राण और उदान का निरोध", "अपान, मार्ग सुप्रसिद्धतर", "अपान बस्ति को शीघ्र खींच ले जाता है"]},
        "chunks": "प्राणोदाननिरोधाद्धि | सुप्रसिद्धतरायणः ‖ अपानः पवनो बस्तिं | तमाश्वेवापकर्षति",
        "sandhi": "अ + उ → ओ: प्राण + उदान → प्राणोदान; त् + ह → द्ध: निरोधात् + हि → निरोधाद्धि; उ → व्: आशु + एव → आश्वेव।",
        "contrast": "रुके: प्राण, उदान · खींचे: अपान।",
    },
    "31": {
        "chain": {"steps": ["कुष्ठ और क्रमुक का कल्क, अम्ल सहित", "उष्णता, तीक्ष्णता, सरत्व", "बस्ति अनुलोम (स्वाभाविक दिशा)"]},
        "chunks": "कुष्ठक्रमुककल्कं च | पाययेताम्लसंयुतं ‖ औष्ण्यात्तैक्ष्ण्यात्सरत्वाच्च | बस्तिं सोप्यनुलोमयेत्",
        "anchors": "कुष्ठ = कूठ (औषध) · क्रमुक = सम्भवतः सुपारी · कल्क = लुगदी · अम्ल = खट्टा · सर = बहने वाला।",
        "contrast": "कुष्ठ (औषध, कूठ) ⟷ कुष्ठ (त्वचा-रोग): यहाँ लुगदी में, इसलिए औषध।",
    },
    "32": {
        "frame": "पंक्ति १: गोमूत्र + निशोथ-हरड़ का कल्क = अधो-अनुलोमन · पंक्ति २: स्थान पक्वाशय, स्वेदित रोगी → दशमूल निरूह (वाक्य 05.06.64 तक)।",
        "chunks": "गोमूत्रेण त्रिवृत्पथ्या | कल्कं वा ऽधोऽनुलोमनं ‖ पक्वाशयस्थिते स्विन्ने | निरूहो दाशमूलिकः",
        "anchors": "त्रिवृत् = निशोथ · पथ्या = हरड़ · पक्वाशय = बड़ी आँत · स्विन्न = स्वेदित · दाशमूलिक = दशमूल का।",
    },
    "33": {
        "contrast": {"groups": [{"label": "पहली बस्ति: मूत्र में साधित", "items": ["यव", "कोल", "कुलत्थ"]},
                                {"label": "दूसरी: गोमूत्र में पकाई", "items": ["अमृता", "वंश के पल्लव", "(सूची 05.06.66 में आगे)"]}]},
        "chunks": "यवकोलकुलत्थैश्च | विधेयो मूत्रसाधितैः ‖ बस्तिर्गौमूत्रसिद्धैर्वा | सामृतावंशपल्लवैः",
        "sandhi": "अ + अ → आ: स + अमृता → सामृता।",
        "anchors": "यव = जौ · कोल = सम्भवतः बेर · कुलत्थ = कुलथी · वंश = सम्भवतः बाँस · पल्लव = कोमल अंकुर · अमृता = सम्भवतः गिलोय।",
    },
    "34": {
        "chunks": "पूतीकरंज | त्वक्पत्र | शठी | देवान्व (अनुमानित: देवाह्व) | रोहिषैः",
        "anchors": "त्वक् = छाल · पत्र = पत्ता · शठी = विवादित पहचान · देवाह्व = सम्भवतः देवदारु (अनुमानित पाठ) · रोहिष = सम्भवतः रूसा घास।",
        "pegs": "मेरा बनाया चित्र: गोमूत्र की हाँडी में एक-एक कर डाले जाते हैं: पूतिकरंज की छाल, उसके पत्ते, शठी, देवाह्व (अनुमानित, सम्भवतः देवदारु), रूसा घास।",
    },
    "35": {
        "diagram": {"groups": [{"label": "सहित", "items": ["तैल", "गुड", "सिन्धूत्थ (सेंधा)"]},
                               {"label": "कल्क", "items": ["विरेचन की औषधें"]},
                               {"label": "किससे पकी", "items": ["बिल्व आदि पंचमूल"]},
                               {"label": "कब", "items": ["उरःस्थिते (छाती में)"]}]},
        "chunks": "सतैलगुडसिंधूत्थो | विरेकौषधकल्कवान् ‖ बिल्वादिपंचमूलेन | सिद्धो बस्तिरुरःस्थिते",
        "anchors": "तैल = तेल · गुड = गुड़ · सिन्धूत्थ = सेंधा नमक · विरेक = विरेचन · बिल्व = बेल · उरः = छाती।",
    },
    "36": {
        "contrast": {"groups": [{"label": "पंक्ति १: सिर में", "items": ["नावन (नस्य)", "धूम", "सिर सरसों से ढका"]},
                                {"label": "पंक्ति २: नया कथन", "items": ["अति-उष्ण", "तीक्ष्ण", "अम्ल", "घन", "या अति-स्वेदित का"]}]},
        "chunks": "शिरःस्थे नावनं धूमः | प्रच्छाद्यं सर्षपैः शिरः ‖ बस्तिरत्युष्णतीक्ष्णाम्ल | घनो ऽतिस्वेदितस्य वा",
        "sandhi": "इ → य् भिन्न स्वर से पहले: अति + उष्ण → अत्युष्ण; अ + अ → आ: तीक्ष्ण + अम्ल → तीक्ष्णाम्ल।",
        "frame": "स्थान-क्रम: पक्वाशय (05.06.63) → उर (05.06.67) → सिर (05.06.68)।",
    },
}

# ================================================================ IMAGE_SPECS
IMAGE_SPECS = {
    ("26", "chain"): {
        "file": "ka6-urdhva-basti-26.svg",
        "alt": "Flowchart of verse 26: a faulty or mild basti, thrown upward by the wind, comes out from the mouth and nose, producing fainting, nausea, thirst and burning",
        "type": "mermaid",
        "code": ('flowchart TD\n  A["दोषयुक्त या मृदु बस्ति"] --> B["वायु ने ऊपर फेंकी"]\n  B --> C["मुख-नासिका से निकली"]\n'
                 '  C --> D["मूर्च्छा"]\n  C --> E["हृल्लास"]\n  C --> F["तृष्णा"]\n  C --> G["दाह"]\n'),
    },
    ("27", "chain"): {
        "file": "ka6-murccha-upaya-27.svg",
        "alt": "Chain of verse 27: on seeing the fainting, sprinkle the face with cold water, fan until the exhaustion goes, make him do pranayama",
        "type": "chain",
        "title": "श्लोक २७: मूर्च्छा का उपचार",
        "steps": ["मूर्च्छा देखी", "मुख पर शीतल जल", "पंखा झलना", "प्राणायाम"],
    },
    ("29", "diagram"): {
        "file": "ka6-bhishana-29.svg",
        "alt": "Flowchart of verse 29: weapons, firebrands and king's men frighten the patient so the basti goes downward; throat pressure with hands and cloths",
        "type": "mermaid",
        "code": ('flowchart TD\n  A["शस्त्र"] --> D["भय"]\n  B["उल्का"] --> D\n  C["राजपुरुष"] --> D\n'
                 '  D --> E["बस्ति नीचे जाती है"]\n  F["हाथ, वस्त्र"] --> G["गले पर दबाव"]\n'),
    },
    ("30", "chain"): {
        "file": "ka6-apana-30.svg",
        "alt": "Flowchart of verse 30: obstruction of prana and udana; apana, whose course is more established, quickly draws the basti away",
        "type": "mermaid",
        "code": ('flowchart TD\n  A["प्राण रुका"] --> C["अपान, मार्ग सुप्रसिद्धतर"]\n  B["उदान रुका"] --> C\n'
                 '  C --> D["अपान शीघ्र बस्ति खींचे"]\n'),
    },
    ("31", "chain"): {
        "file": "ka6-kushtha-kalka-31.svg",
        "alt": "Flowchart of verse 31: a paste of costus and areca nut with sour; by heat, sharpness and flowing nature it brings the basti into the natural direction",
        "type": "mermaid",
        "code": ('flowchart TD\n  A["अम्लयुक्त कुष्ठ-क्रमुक कल्क"] --> B["उष्णता"]\n  A --> C["तीक्ष्णता"]\n'
                 '  A --> D["सरत्व"]\n  B --> E["बस्ति अनुलोम"]\n  C --> E\n  D --> E\n'),
    },
    ("33", "contrast"): {
        "file": "ka6-do-basti-33.svg",
        "alt": "Two columns of verse 33: first basti with barley, jujube and horse gram prepared in urine; second with giloy and bamboo shoots cooked in cow's urine",
        "type": "split",
        "title": "श्लोक ३३: दो बस्तियाँ",
        "cols": [["मूत्र में साधित", ["यव", "कोल", "कुलत्थ"]],
                 ["गोमूत्र में पकाई", ["अमृता", "वंश के पल्लव"]]],
    },
    ("35", "diagram"): {
        "file": "ka6-urahstha-basti-35.svg",
        "alt": "Table of unit 35: the chest basti has oil, jaggery and rock salt, a paste of purgative drugs, and is cooked with the five roots beginning with bilva",
        "type": "table",
        "title": "इकाई ३५: छाती की बस्ति",
        "heads": ["भाग", "द्रव्य"],
        "rows": [["सहित", "तैल, गुड, सेंधा नमक"], ["कल्क", "विरेचन की औषधें"],
                 ["किससे पकी", "बिल्व आदि पंचमूल"], ["कब", "छाती में स्थित होने पर"]],
    },
    ("36", "contrast"): {
        "file": "ka6-shiras-atiyoga-36.svg",
        "alt": "Two columns of verse 36: for the head, nasal medication, smoke and covering with mustard; line 2, a basti too hot, sharp, sour and thick",
        "type": "split",
        "title": "श्लोक ३६: सिर, और नया कथन",
        "cols": [["सिर में", ["नावन (नस्य)", "धूम", "सरसों से ढका सिर"]],
                 ["पंक्ति २: बस्ति", ["अति-उष्ण", "तीक्ष्ण", "अम्ल", "घन"]]],
    },
}
