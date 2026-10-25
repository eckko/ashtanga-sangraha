from helpers import mcq, match, order, fill, multi, accepts


def T(q, teaches):
    q["teaches"] = teaches
    return q


AUTHORED = {}

# ---------------------------------------------------------------- unit 1
AUTHORED["1"] = {
    "title": "अथातो दूतादिविज्ञानीयं",
    "question": "What does the opening line of card 1 announce?",
    "rule": ("अथ अतः ... व्याख्यास्यामः: 'Now, therefore, we shall expound' the Dūtādivijñānīya, the chapter on knowing the "
             "messenger (दूत) and the rest. अतः + दूता- → अतो दूता- (अः before a voiced consonant → ओ)."),
    "limits": ("Prose, the opening formula of a chapter. The noun that शारीरम् agrees with is not printed and none is supplied. "
               "The data's word split lists only अथ for the printed अथातो; अतः (therefore) is not glossed separately, though the "
               "Hindi and English render it."),
    "explain_hi": ("यह शारीरस्थान के बारहवें अध्याय की आरम्भिक पंक्ति है: ‘अब, इसलिए, हम शारीर (शरीर-सम्बन्धी) दूतादिविज्ञानीय का व्याख्यान करेंगे।’ "
                   "दूतादिविज्ञानीय का अर्थ है दूत आदि के विषय में जानने योग्य बातें। "
                   "‘शारीरम्’ किस संज्ञा का विशेषण है, यह छपा नहीं। "
                   "व्याख्यास्यामः भविष्यत् काल, उत्तम पुरुष बहुवचन है: ‘हम कहेंगे’। "
                   "‘अथातो’ में अथ + अतः है: अ + अ → आ, और अः घोष व्यंजन द से पहले ओ बनता है।"),
    "hook": "अथातो ... व्याख्यास्यामः: अब दूत आदि को जानने का अध्याय।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 1, what does व्याख्यास्यामः mean?",
            ("We shall expound", "Future, first person plural of vi-ā-√khyā: we shall expound."),
            [("They will expound", "They will expound would be व्याख्यास्यन्ति; -स्यामः is 'we'."),
             ("We have expounded", "The -स्य- marks the future here, not a past."),
             ("Let him expound", "Let him expound would be an imperative such as व्याख्यातु.")],
            "व्याख्यास्यामः = we shall expound (future, 1st person plural).",
            "-स्यामः = future, 'we'."),
        match(1, "Match each word of card 1 to its meaning.",
              [["अथ", "now"], ["दूत", "messenger"], ["आदि", "and the rest"], ["शारीरम्", "belonging to the body"],
               ["व्याख्यास्यामः", "we shall expound"]],
              "अथ = now, दूत = messenger, आदि = and the rest, शारीरम् = belonging to the body, व्याख्यास्यामः = we shall expound.",
              "अथ, दूत, आदि, शारीरम्, व्याख्यास्यामः."),
        order(2, "Put the printed words of card 1 in order.",
              ["अथातो", "दूतादिविज्ञानीयं", "शारीरं", "व्याख्यास्यामः"],
              "Now therefore; the Dūtādivijñānīya; belonging to the body; we shall expound.",
              "अथातो → दूतादिविज्ञानीयं → शारीरं → व्याख्यास्यामः.",
              role="extend",
              teaches="The opening formula names the chapter (दूतादिविज्ञानीय) first; the verb व्याख्यास्यामः closes the line."),
        mcq("discriminate", 3, "Which split of the printed अथातो in card 1 is right?",
            ("अथ + अतः", "अ + अ → आ, and अः before the voiced द → ओ: अथातो दूता-."),
            [("अथ + इतः", "अ + इ gives ए: that would print अथेतो."),
             ("अथ + उत", "अ + उ gives ओ with no आ: that would print अथोत."),
             ("अथा + तः", "Neither अथा nor तः is a word here; the आ comes from अ + अ.")],
            "अथ (now) + अतः (therefore).",
            "अ + अ → आ."),
        mcq("apply", 4, "Why is the visarga of अतः printed as ओ before दूता- in card 1?",
            ("अः before a voiced consonant → ओ", "द is a voiced consonant, so अतः + दूता- → अतो दूता-."),
            [("अः before any consonant → ओ", "Not before a voiceless one: before त it gives स्, as in ततस्ततः."),
             ("अः before every vowel → ओ", "Before vowels other than अ, the visarga of अः drops and अ stays."),
             ("ओ belongs to the stem अतो", "The word is अतः; the ओ comes only from sandhi.")],
            "अतः + दूता-: अः before the voiced द → ओ.",
            "अः before a voiced consonant → ओ."),
        mcq("transfer", 5, "By the pattern of अतः + दूता- → अतो दूता-, how are बालः + धावति (the boy runs) joined in a new example?",
            ("बालो धावति", "अः before the voiced consonant ध → ओ."),
            [("बालर्धावति", "र् comes from a visarga after vowels other than अ or आ, not after अ."),
             ("बालस्धावति", "स् comes from a visarga before त or थ, not before ध."),
             ("बाला धावति", "आ is not the result; अः before a voiced consonant gives ओ.")],
            "बालः + धावति = बालो धावति, like अतः + दूता- = अतो दूता-.",
            "अः before a voiced consonant → ओ.",
            teaches="अः before a voiced consonant becomes ओ: अतः + दूता- → अतो दूता-."),
    ],
}

# ---------------------------------------------------------------- unit 2
AUTHORED["2"] = {
    "title": "निर्दिष्टं रिष्टमातुराश्रयं",
    "question": "What does card 2 say has already been indicated?",
    "rule": ("रिष्टम् (riṣṭa, a sign of approaching death; standard) resting on the patient (आतुराश्रयम्) has been indicated "
             "(निर्दिष्टम्). रिष्टम् + आतुर- → रिष्टमातुर-; आतुर + आश्रयम् → आतुराश्रयम् (अ + आ → आ)."),
    "limits": ("Prose, medium confidence. आतुराश्रयम् is read as one bahuvrīhi qualifying रिष्टम्; a separate noun 'the patient's "
               "support' is another reading: no question on its parse. No auxiliary is printed, and where the riṣṭa was indicated "
               "is not said. The line names no sign and gives no prognosis."),
    "explain_hi": ("यह पंक्ति कहती है कि रोगी पर आश्रित रिष्ट, यानी मृत्यु के निकट होने का लक्षण (मानक अर्थ), बताया जा चुका है। "
                   "‘निर्दिष्टम्’ निर्-√दिश् का भूत कृदन्त है: बताया गया; कोई सहायक क्रिया नहीं छपी। "
                   "‘आतुराश्रयम्’ को रिष्ट का विशेषण (बहुव्रीहि, रोगी पर टिका) पढ़ा गया; इसे अलग संज्ञा ‘रोगी का आश्रय’ भी पढ़ा जा सकता है। "
                   "रिष्ट कहाँ बताया गया, यह पंक्ति नहीं कहती; यह कोई लक्षण या फल भी नहीं गिनाती। "
                   "छपा ‘रिष्टमातुराश्रयं’ एक ही शब्द-खण्ड है: रिष्टम् + आतुराश्रयम्।"),
    "hook": "रिष्ट = मृत्यु के निकट होने का लक्षण, रोगी पर आश्रित: यह बताया जा चुका।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 2, what is रिष्टम्?",
            ("A sign of approaching death", "रिष्ट = a sign that death is near (standard)."),
            [("A remedy for a long illness", "रिष्ट is a sign, not a remedy."),
             ("A message sent by the patient", "A messenger is दूत; रिष्ट is a sign of approaching death."),
             ("A sign of a quick recovery", "रिष्ट points to approaching death, not to recovery.")],
            "रिष्टम् = a sign of approaching death.",
            "रिष्ट = sign of approaching death."),
        match(1, "Match each word of card 2 to its meaning.",
              [["निर्दिष्टम्", "indicated, pointed out"], ["रिष्टम्", "sign of approaching death"], ["आतुर", "the patient"],
               ["आतुराश्रयम्", "resting on the patient"]],
              "निर्दिष्टम् = indicated, रिष्टम् = sign of approaching death, आतुर = the patient, आतुराश्रयम् = resting on the patient.",
              "निर्दिष्टम्, रिष्टम्, आतुर, आतुराश्रयम्."),
        fill(2, "In card 2, the word for a sign of approaching death is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("रिष्टम्", "riṣṭam", "रिष्ट", "rishtam", "rishta"),
             "रिष्टम् = a sign of approaching death; here it rests on the patient (आतुराश्रयम्).",
             "रिष्ट names a sign of approaching death; in card 2 it is said to rest on the patient.",
             "रिष्टम् = sign of approaching death."),
        mcq("discriminate", 3, "Which split of the printed रिष्टमातुराश्रयं in card 2 is right?",
            ("रिष्टम् + आतुराश्रयम्", "Final म् joins the next vowel: रिष्टम् + आतुर- → रिष्टमातुर-."),
            [("रिष्टम् + अतुराश्रयम्", "That would print रिष्टमतुर-, with म, not मा."),
             ("रिष्टमा + तुराश्रयम्", "Neither रिष्टमा nor तुराश्रयम् is a word here."),
             ("रिष्टम् + आतुरः + आश्रयम्", "आतुरः + आश्रयम् would print आतुर आश्रयम्, with a gap, not आतुराश्रयम्.")],
            "रिष्टम् (sign of approaching death) + आतुराश्रयम् (resting on the patient).",
            "Final म् + vowel: they join."),
        mcq("apply", 4, "In आतुराश्रयम् of card 2, which vowel sandhi joins आतुर + आश्रयम्?",
            ("अ + आ → आ", "आतुर + आश्रयम् → आतुराश्रयम्: अ and आ merge into आ."),
            [("अ + आ → ऐ", "ऐ comes from अ or आ before ए or ऐ, not before आ."),
             ("अ + आ → औ", "औ comes from अ or आ before ओ or औ, not before आ."),
             ("अ + आ → या", "य् arises from इ or ई before a vowel, not from अ.")],
            "आतुर + आश्रयम् = आतुराश्रयम् (अ + आ → आ).",
            "अ + आ → आ."),
        mcq("transfer", 5, "By the pattern of आतुर + आश्रयम् → आतुराश्रयम्, how is सूर्य + आलोकः (sunlight) joined in a new example?",
            ("सूर्यालोकः", "अ + आ → आ: सूर्य + आलोकः → सूर्यालोकः."),
            [("सूर्यैलोकः", "ऐ would need ए or ऐ after अ."),
             ("सूर्यौलोकः", "औ would need ओ or औ after अ."),
             ("सूर्ययालोकः", "No य् is inserted between अ and आ; they merge.")],
            "सूर्य + आलोकः = सूर्यालोकः, like आतुर + आश्रयम् = आतुराश्रयम्.",
            "अ + आ → आ.",
            teaches="अ before आ merges into आ: आतुर + आश्रयम् → आतुराश्रयम्."),
    ],
}

# ---------------------------------------------------------------- unit 3
AUTHORED["3"] = {
    "title": "दूतस्यापि तु जातिवेषभाषा",
    "question": "By card 3, which features of the messenger, of the physician's journey and of other things indicate good and bad?",
    "rule": ("Of the messenger: kind (जाति), dress, speech, behaviour, place, time; of the physician: meeting him, intention, "
             "setting out, going, entering; also planetary movement, a previous occurrence and dream-sights: these indicate "
             "the auspicious and inauspicious (शुभाशुभम्)."),
    "limits": ("Prose, medium confidence. ग्रहचारो is flagged (ग्रहचारः expected before प); पूर्वसंभवः (previous occurrence) is "
               "uncertain in sense; जाति may also mean birth or caste. The data reads रोगिणः with the dream-sights. No question on these."),
    "explain_hi": ("यह इकाई बताती है कि शुभ और अशुभ की सूचना किन बातों से मिलती है (सूचयन्ति)। "
                   "दूत की जाति, वेश, भाषा, चेष्टा, स्थान और समय; वैद्य का उस दूत से मिलना (तत्संगम, तत् = दूत), संकल्प, प्रस्थान, गमन और प्रवेश; "
                   "ग्रहों की चाल, ‘पूर्वसंभव’ और स्वप्न-दर्शन: ये सब शुभाशुभ बताते हैं। "
                   "‘पूर्वसंभवः’ (पहले की घटना) का अर्थ अनिश्चित है, और छपा ‘ग्रहचारो’ सन्धि के अनुसार नहीं बैठता (ग्रहचारः अपेक्षित)। "
                   "‘दूतस्यापि’ में दूतस्य + अपि है (अ + अ → आ)।"),
    "hook": "दूत की छह बातें, वैद्य की पाँच: सब शुभाशुभ बताती हैं।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By card 3, what do all these features indicate (सूचयन्ति)?",
            ("The auspicious and inauspicious", "शुभाशुभं सूचयन्ति: they indicate the auspicious and the inauspicious."),
            [("The medicine the patient must take", "No medicine is named in card 3."),
             ("The fee the physician is to receive", "No fee is named in card 3."),
             ("The day on which the illness began", "No day of falling ill is named in card 3.")],
            "शुभाशुभम् = the auspicious and the inauspicious.",
            "... शुभाशुभं सूचयन्ति."),
        order(1, "Put the messenger's features named in card 3 in the printed order.",
              ["जाति", "वेष", "भाषा", "चेष्टित", "देश", "काल"],
              "The messenger's compound: जाति-वेष-भाषा-चेष्टित-देश-कालाः (kind, dress, speech, behaviour, place, time).",
              "जाति → वेष → भाषा → चेष्टित → देश → काल."),
        match(2, "Match each word of card 3 to its meaning.",
              [["वेष", "dress"], ["भाषा", "speech"], ["चेष्टित", "behaviour"], ["संकल्प", "intention"],
               ["प्रस्थान", "setting out"], ["प्रवेश", "entering"]],
              "वेष = dress, भाषा = speech, चेष्टित = behaviour, संकल्प = intention, प्रस्थान = setting out, प्रवेश = entering.",
              "वेष, भाषा, चेष्टित (messenger); संकल्प, प्रस्थान, प्रवेश (physician).",
              role="extend",
              teaches="Not only the messenger: the physician's own steps (meeting, intention, setting out, going, entering) count as signs too."),
        multi("discriminate", 3, "By card 3, which of these belong to the physician (वैद्यस्य), not to the messenger?",
              [("Dress (वेष)", "No: वेष is in the messenger's list."),
               ("Intention (संकल्प)", "Yes: संकल्प is in the physician's list."),
               ("Speech (भाषा)", "No: भाषा is in the messenger's list."),
               ("Entering (प्रवेश)", "Yes: प्रवेश is in the physician's list."),
               ("Setting out (प्रस्थान)", "Yes: प्रस्थान is in the physician's list.")],
              [1, 3, 4],
              "Physician: तत्संगम, संकल्प, प्रस्थान, प्रयाण, प्रवेश. Messenger: जाति, वेष, भाषा, चेष्टित, देश, काल.",
              "वैद्यस्य च तत्संगमसंकल्पप्रस्थानप्रयाणप्रवेशाः."),
        mcq("apply", 4, "Which split of दूतस्यापि in card 3 is right?",
            ("दूतस्य + अपि", "अ + अ → आ: दूतस्य + अपि → दूतस्यापि."),
            [("दूतस्या + पि", "Neither दूतस्या nor पि is a word here."),
             ("दूतस्य + आपि", "आपि is not a word; the आ comes from अ + अ."),
             ("दूतः + स्यापि", "स्यापि is not a word; दूतस्य is the genitive.")],
            "दूतस्य (of the messenger) + अपि (also).",
            "अ + अ → आ."),
        mcq("transfer", 5, "By the pattern of दूतस्य + अपि → दूतस्यापि, how is अत्र + अस्ति (here is) joined in a new example?",
            ("अत्रास्ति", "अ + अ → आ: अत्र + अस्ति → अत्रास्ति."),
            [("अत्रेस्ति", "ए would need इ after अ."),
             ("अत्रोस्ति", "ओ would need उ after अ."),
             ("अत्र्यस्ति", "य् comes from इ before a vowel, not from अ.")],
            "अत्र + अस्ति = अत्रास्ति, like दूतस्य + अपि = दूतस्यापि.",
            "अ + अ → आ.",
            teaches="अ before अ merges into आ: दूतस्य + अपि → दूतस्यापि."),
    ],
}

# ---------------------------------------------------------------- unit 4
AUTHORED["4"] = {
    "title": "दूतो वैद्यमुपसर्पन्नशुभः",
    "question": "By card 4, what marks make a messenger who approaches the physician inauspicious?",
    "rule": ("A messenger approaching the physician (दूतो वैद्यमुपसर्पन्) is inauspicious if, among other marks, he rides a donkey, "
             "camel or buffalo, is agitated, panting, weeping, harsh, calls from afar, or comes at a place or time like the disease."),
    "limits": ("Prose, low confidence; one sentence, दूतः near its end. Conjectural: charcoal, saline soil, vyādhino, aneka and "
               "ārdra, pakka; spṛk is unclear; body parts in a list of things borne (-धरः) and 'releasing the ground' are unexplained. "
               "No question on these; only some items are asked."),
    "explain_hi": ("यह एक लम्बा वाक्य है जिसका कर्ता ‘दूतः’ अन्त के पास आता है: ऐसा दूत वैद्य के पास आता हुआ अशुभ है। "
                   "लक्षणों में हैं: गधे, ऊँट या भैंसे पर सवारी; घबराना, हाँफना, रोना, कठोर होना, अमंगल बोलना और दूर से पुकारना; "
                   "पुराना, बदरंग, मैला, फटा एक वस्त्र; कीचड़ और तेल से लिपटा होना; रोग के समान गुण वाले स्थान या समय में आना। "
                   "बीच का बहुत लम्बा समास वस्तुओं और शरीर-अंगों की सूची है जो ‘-धरः’ (धारण करने वाला) पर समाप्त होता है; "
                   "शरीर-अंगों का इसमें होना स्पष्ट नहीं, और कई पाठ अनुमानित हैं। "
                   "इसलिए प्रश्न केवल पक्के अंशों पर हैं।"),
    "hook": "गधा, ऊँट, भैंसा सवारी; रोता, हाँफता, दूर से पुकारता दूत: अशुभ।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By card 4, which animals as the messenger's mount (वाहन) mark him as inauspicious?",
            ("Donkey, camel or buffalo", "खरोष्ट्रमहिषवाहनः: riding a donkey (खर), camel (उष्ट्र) or buffalo (महिष)."),
            [("A horse, a bull or a swan", "Card 10 lists horses, a bull and a swan among auspicious sights; card 4 names donkey, camel, buffalo."),
             ("A lion, a cow or a fish", "Card 10 lists a lion, a cow and fish among auspicious sights; none is a mount in card 4."),
             ("A horse or a yoked vehicle", "Card 10 lists horses and harnessed vehicles among auspicious sights; card 4 names donkey, camel, buffalo.")],
            "खर (donkey), उष्ट्र (camel), महिष (buffalo) as वाहन.",
            "खरोष्ट्रमहिषवाहनो ... अशुभः."),
        match(1, "Match each word describing the messenger in card 4 to its meaning.",
              [["विह्वलः", "agitated"], ["श्वसन्", "panting"], ["रुदन्", "weeping"], ["निष्ठुरः", "harsh"],
               ["अमङ्गलाभिधायी", "speaking inauspicious things"]],
              "विह्वलः = agitated, श्वसन् = panting, रुदन् = weeping, निष्ठुरः = harsh, अमङ्गलाभिधायी = speaking inauspicious things.",
              "विह्वलः, श्वसन्, रुदन्, निष्ठुरः, अमङ्गलाभिधायी."),
        order(2, "Put these marks of the messenger in card 4 in the printed order (words as split in the data).",
              ["खरोष्ट्रमहिषवाहनः", "विह्वलः", "श्वसन्", "रुदन्", "निष्ठुरः", "दूरादाह्वयमानः"],
              "Riding a donkey, camel or buffalo; agitated; panting; weeping; harsh; calling from afar.",
              "खरोष्ट्रमहिषवाहनः → विह्वलः → श्वसन् → रुदन् → निष्ठुरः → दूरादाह्वयमानः.",
              role="extend",
              teaches="Card 4 is one sentence: the marks pile up as words describing दूतः, which comes only near the end."),
        multi("discriminate", 3, "By card 4, which words describe the messenger's single garment?",
              [("Old (जीर्ण)", "Yes: जीर्ण is printed in the garment compound."),
               ("New (नव)", "No: the garment is old (जीर्ण), not new."),
               ("Dirty (मलिन)", "Yes: मलिन is printed in the garment compound."),
               ("White (शुक्ल)", "No: the garment is discoloured (विवर्ण); white is not named."),
               ("Torn (छिन्न)", "Yes: छिन्न is printed in the garment compound.")],
              [0, 2, 4],
              "The garment is जीर्ण (old), विवर्ण (discoloured), मलिन (dirty), छिन्न (torn).",
              "...जीर्णविवर्णमलिनच्छिन्न...वसनः."),
        mcq("apply", 4, "By card 4, at what kind of place or time is the messenger's coming inauspicious?",
            ("One alike in quality to the disease", "विकारतुल्यगुणे देशे काले वा: a place or time similar in quality to the disease."),
            [("One opposite in quality to the disease", "Card 4 says similar (तुल्य), not opposite."),
             ("One chosen beforehand by the physician", "Card 4 says nothing of a place chosen by the physician."),
             ("One far from the patient's own house", "Card 4 says nothing of distance from the house.")],
            "विकार-तुल्य-गुणे: similar in quality to the disease.",
            "विकारतुल्यगुणे च देशे काले वा."),
        mcq("transfer", 5, "By the pattern of दूरात् + आह्वयमानः → दूरादाह्वयमानः, how is ग्रामात् + आगतः (come from the village) joined in a new example?",
            ("ग्रामादागतः", "Final त् before a vowel → द्: ग्रामात् + आगतः → ग्रामादागतः."),
            [("ग्रामातागतः", "Final त् does not stay before a vowel; it becomes द्."),
             ("ग्रामानागतः", "न् can come from त् only before a nasal, not before a vowel."),
             ("ग्रामाच्चागतः", "च्च comes from त् + च, not from त् before a vowel.")],
            "ग्रामात् + आगतः = ग्रामादागतः, like दूरात् + आह्वयमानः = दूरादाह्वयमानः.",
            "Final त् before a vowel → द्.",
            teaches="Final त् becomes द् before a vowel: दूरात् + आह्वयमानः → दूरादाह्वयमानः."),
    ],
}

# ---------------------------------------------------------------- unit 5
AUTHORED["5"] = {
    "title": "तद्यथा",
    "question": "What does तद्यथा in card 5 do, and how is it joined?",
    "rule": "तद्यथा = तत् (that) + यथा (as, namely): 'that is as follows'; examples follow in the next cards. त् before the voiced य → द्.",
    "limits": "Prose, a formula of two words; no verb is printed. The card asks nothing about the examples that follow.",
    "explain_hi": ("‘तद्यथा’ एक छोटा जोड़ने वाला सूत्र है: ‘वह इस प्रकार है’, यानी आगे उदाहरण आते हैं। "
                   "इसमें तत् (वह) + यथा (जैसे, अर्थात्) है। "
                   "तत् का त् घोष व्यंजन य से पहले द् बनता है: तत् + यथा → तद्यथा। "
                   "कोई क्रिया नहीं छपी।"),
    "hook": "तद्यथा: ‘जैसे कि’; अब उदाहरण।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 5, what does तद्यथा mean?",
            ("That is as follows", "तत् (that) + यथा (as, namely): that is as follows."),
            [("That is not at all so", "Nothing in तद्यथा denies; there is no न."),
             ("And therefore it ends", "तद्यथा opens examples; it does not end anything."),
             ("As it was before", "यथा here means 'namely', introducing what follows.")],
            "तद्यथा = that is as follows, namely.",
            "तत् + यथा = 'that is as follows'."),
        multi("warmup", 1, "Which statements fit card 5 as printed?",
              [("It names a sign of death", "No: it names nothing; it only introduces what follows."),
               ("It prints no verb", "Yes: only तत् and यथा are printed."),
               ("It joins two words, तत् and यथा", "Yes: तत् + यथा → तद्यथा."),
               ("It lists the messenger's dress", "No: dress (वेष) is named in card 3, not card 5.")],
              [1, 2],
              "Two words, तत् + यथा, and no verb.",
              "तद्यथा = तत् + यथा."),
        fill(2, "In card 5, the word for 'as, namely' is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("यथा", None, "yatha"),
             "यथा = as, namely: तत् + यथा → तद्यथा.",
             "यथा (as, namely) after तत् introduces examples.",
             "यथा = as, namely."),
        mcq("discriminate", 3, "Why is तत् printed with द् before यथा in card 5?",
            ("त् before a voiced sound → द्", "य is voiced, so तत् + यथा → तद्यथा."),
            [("त् before any consonant → द्", "Not before a voiceless one: तत् + कालम् stays तत्कालम्."),
             ("तद् is the nominative form", "The nominative neuter is तत्; the द् comes from sandhi here."),
             ("य turns every stop into a nasal", "No nasal appears here; the print has द्.")],
            "तत् + यथा: त् before the voiced य → द्.",
            "त् before a voiced sound → द्."),
        mcq("apply", 4, "By card 5, what comes after तद्यथा?",
            ("Examples, in the cards that follow", "The data: the following units give examples."),
            [("The close of the whole chapter", "The chapter goes on; card 5 is near its start."),
             ("A list of medicines for the patient", "Card 5 names no medicines; it introduces examples."),
             ("A question put by a pupil", "No pupil or question is printed; तद्यथा introduces examples.")],
            "तद्यथा introduces examples.",
            "तद्यथा = namely: examples follow."),
        mcq("transfer", 5, "By the pattern of तत् + यथा → तद्यथा, how is एतत् + गृहम् (this house) joined in a new example?",
            ("एतद्गृहम्", "त् before the voiced ग → द्: एतत् + गृहम् → एतद्गृहम्."),
            [("एतत्गृहम्", "Final त् does not stay before the voiced ग; it becomes द्."),
             ("एतग्गृहम्", "त् is not assimilated to ग; it becomes द्."),
             ("एतन्गृहम्", "न् from त् is possible only before a nasal; ग is not a nasal.")],
            "एतत् + गृहम् = एतद्गृहम्, like तत् + यथा = तद्यथा.",
            "त् before a voiced consonant → द्.",
            teaches="Final त् becomes द् before a voiced consonant: तत् + यथा → तद्यथा."),
    ],
}

# ---------------------------------------------------------------- unit 6
AUTHORED["6"] = {
    "title": "श्लेष्मामयेऽशुभः पित्तामये तु शुभः",
    "question": "By card 6, in which disease is the dawn sign inauspicious and in which auspicious?",
    "rule": ("At dawn (प्रत्यूषसि), one very cold and stiff (अतिशीतस्तब्धः), standing near liquids on a conjectural reading, is "
             "inauspicious in a Kapha disease (श्लेष्मामये) but auspicious in a Pitta disease (पित्तामये)."),
    "limits": ("Prose, low confidence. The first printed word is damaged: 'drava' (liquid) for द्व is a conjecture, and its -म् "
               "ending does not agree with what follows, so who is meant (presumably the messenger) is unclear: no question on "
               "the liquids or on the subject. Vāta disease is not named."),
    "explain_hi": ("यह इकाई एक ही चिह्न के दो रोगों में उलटे फल बताती है। "
                   "भोर के समय (प्रत्यूषसि) अत्यन्त ठंडा और अकड़ा हुआ, अनुमानित पाठ पर घी, जल आदि द्रवों के पास खड़ा, "
                   "कफ के रोग (श्लेष्मामय) में अशुभ है, पर पित्त के रोग में शुभ है। "
                   "पहला छपा शब्द क्षतिग्रस्त है: ‘द्व’ को ‘द्रव’ पढ़ना अनुमान है, और उसका -म् अन्त आगे के प्रथमा शब्दों से मेल नहीं खाता; "
                   "कर्ता (सम्भवतः दूत) स्पष्ट नहीं। "
                   "‘तु’ (परन्तु) दोनों फलों को आमने-सामने रखता है; ‘श्लेष्मामयेऽशुभः’ में ए + अ → एऽ की सन्धि है।"),
    "hook": "भोर में ठंडा और अकड़ा: कफ में अशुभ, पित्त में शुभ।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By card 6, in which disease is the sign auspicious (शुभः)?",
            ("In a Pitta disease", "पित्तामये तु शुभः: but auspicious in a Pitta disease."),
            [("In a Kapha disease", "In a Kapha disease (श्लेष्मामये) it is inauspicious."),
             ("In every disease alike", "Card 6 gives two opposite results, not one for all."),
             ("In no disease at all", "Card 6 does call it auspicious in a Pitta disease.")],
            "Kapha disease: अशुभः; Pitta disease: शुभः.",
            "श्लेष्मामयेऽशुभः पित्तामये तु शुभः."),
        match(1, "Match each word of card 6 to its meaning.",
              [["प्रत्यूषसि", "at dawn"], ["अतिशीत", "very cold"], ["स्तब्धः", "stiff"],
               ["श्लेष्मामये", "in a Kapha disease"], ["पित्तामये", "in a Pitta disease"]],
              "प्रत्यूषसि = at dawn, अतिशीत = very cold, स्तब्धः = stiff, श्लेष्मामये = in a Kapha disease, पित्तामये = in a Pitta disease.",
              "प्रत्यूषसि, अतिशीत, स्तब्धः, श्लेष्मामये, पित्तामये."),
        order(2, "Put these sure parts of card 6 in the printed order.",
              ["प्रत्यूषसि", "श्लेष्मामयेऽशुभः", "पित्तामये तु", "शुभः"],
              "At dawn; inauspicious in a Kapha disease; but in a Pitta disease; auspicious.",
              "प्रत्यूषसि → श्लेष्मामयेऽशुभः → पित्तामये तु → शुभः.",
              role="extend",
              teaches="तु (but) sets the Pitta result against the Kapha result: one sign, two opposite readings."),
        mcq("discriminate", 3, "Which split of श्लेष्मामयेऽशुभः in card 6 is right?",
            ("श्लेष्मामये + अशुभः", "ए + अ → ए; the dropped अ is shown by ऽ."),
            [("श्लेष्मामये + शुभः", "That would print श्लेष्मामये शुभः with no ऽ, and clash with 'but auspicious' for Pitta."),
             ("श्लेष्मामय + अशुभः", "अ + अ gives आ: that would print श्लेष्मामयाशुभः."),
             ("श्लेष्मा + मयेऽशुभः", "मये is not a word here; the compound is श्लेष्म + आमय.")],
            "श्लेष्मामये (in a Kapha disease) + अशुभः (inauspicious).",
            "ए + अ → एऽ."),
        mcq("apply", 4, "In श्लेष्मामयेऽशुभः of card 6, what does the sign ऽ show?",
            ("A dropped अ after ए", "ए + अ → ए; the dropped अ of अशुभः is marked ऽ."),
            [("A dropped visarga", "No visarga is lost here; ऽ marks the lost अ."),
             ("A long pause in reading", "ऽ is a sandhi sign here, not a pause mark."),
             ("A doubled vowel ए", "No vowel is doubled; the अ after ए is dropped.")],
            "ऽ (avagraha) marks the अ dropped after ए.",
            "ए + अ → एऽ."),
        mcq("transfer", 5, "By the pattern of श्लेष्मामये + अशुभः, how is वने + अस्ति (is in the forest) joined in a new example?",
            ("वनेऽस्ति", "ए + अ → ए, and the अ drops (ऽ): वनेऽस्ति."),
            [("वनैस्ति", "ऐ comes from अ or आ before ए, not from ए before अ."),
             ("वनयस्ति", "ए becomes अय् (or अ) only before vowels other than अ; before अ it stays ए and the अ drops."),
             ("वनास्ति", "आ would need अ + अ; here the first vowel is ए.")],
            "वने + अस्ति = वनेऽस्ति, like श्लेष्मामये + अशुभः = श्लेष्मामयेऽशुभः.",
            "ए + अ → एऽ.",
            teaches="Final ए before अ stays, and the अ is dropped (written ऽ): श्लेष्मामये + अशुभः → श्लेष्मामयेऽशुभः."),
    ],
}

# ---------------------------------------------------------------- unit 7
AUTHORED["7"] = {
    "title": "तथा सेतुभंगे",
    "question": "By card 7, how do the breaking and the building of a dam differ as omens?",
    "rule": ("At the breaking of a dam or bridge (सेतुभङ्गे) it is inauspicious in vomiting (chardi), meha (urinary disorders; "
             "probable), diarrhoea (atisāra) and the like; at the building of one (सेतुबन्धे) it is auspicious."),
    "limits": ("Prose, medium confidence; elliptical: the sight of a messenger at such an event is understood, no subject is printed. "
               "Whether the building is auspicious only in the same diseases is not said. setu may be a dam or a bridge."),
    "explain_hi": ("‘तथा’ (इसी प्रकार) पिछली इकाई की शैली आगे बढ़ाता है। "
                   "सेतु (बाँध या पुल) के टूटने (भङ्ग) पर छर्दि यानी उलटी, मेह यानी मूत्र के रोग (प्रमेह वर्ग, सम्भावित पहचान) "
                   "और अतिसार यानी दस्त आदि में अशुभ है; पर सेतु बाँधने (बन्ध) पर शुभ है। "
                   "कर्ता नहीं छपा: ऐसी घटना पर दूत का दिखना समझा जाता है। "
                   "‘-आदिष्वशुभः’ में आदिषु + अशुभः है: उ भिन्न स्वर अ से पहले व् बनता है।"),
    "hook": "सेतु टूटे: उलटी, दस्त, मेह में अशुभ; सेतु बँधे: शुभ।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By card 7, at which event is it auspicious?",
            ("At the building of a dam", "सेतुबन्धे तु शुभः: but at the building of a dam, auspicious."),
            [("At the breaking of a dam", "At the breaking (सेतुभङ्ग) it is inauspicious."),
             ("At the crossing of a river", "Card 7 names no crossing of a river."),
             ("At the flooding of a field", "Card 7 names no flooding of a field.")],
            "सेतुभङ्ग: अशुभ; सेतुबन्ध: शुभ.",
            "सेतुबंधे तु शुभः."),
        match(1, "Match each word of card 7 to its meaning.",
              [["छर्दि", "vomiting (standard)"], ["अतिसार", "diarrhoea (standard)"], ["मेह", "urinary disorders (probable)"],
               ["सेतुभङ्ग", "breaking of a dam or bridge"], ["सेतुबन्ध", "building of a dam or bridge"]],
              "छर्दि = vomiting, अतिसार = diarrhoea (both standard), मेह = urinary disorders (probable), सेतुभङ्ग = breaking, सेतुबन्ध = building of a dam.",
              "छर्दि, अतिसार, मेह; सेतुभङ्ग ⇄ सेतुबन्ध."),
        order(2, "Put the printed parts of card 7 in order.",
              ["तथा", "सेतुभंगे", "छर्दिमेहातिसारादिष्वशुभः", "सेतुबंधे तु", "शुभः"],
              "Likewise; at the breaking of a dam; inauspicious in vomiting, meha, diarrhoea and the like; but at the building of a dam; auspicious.",
              "तथा → सेतुभंगे → छर्दिमेहातिसारादिष्वशुभः → सेतुबंधे तु → शुभः.",
              role="extend",
              teaches="Card 7 sets two opposite events, breaking (भङ्ग) and building (बन्ध), against each other with तु (but)."),
        mcq("discriminate", 3, "Which split of the printed -आदिष्वशुभः in card 7 is right?",
            ("-आदिषु + अशुभः", "उ before the unlike vowel अ → व्: आदिषु + अशुभः → आदिष्वशुभः."),
            [("-आदिषु + शुभः", "That would print आदिषु शुभः, with no व्."),
             ("-आदिष्व + शुभः", "आदिष्व is not a form; the locative plural is आदिषु."),
             ("-आदिषू + अशुभः", "आदिषू is not a form; the locative plural ends in short -षु.")],
            "-आदिषु (in ... and the like) + अशुभः (inauspicious).",
            "उ + unlike vowel → व्."),
        mcq("apply", 4, "Which pair of opposites does card 7 set against each other?",
            ("Breaking and building", "भङ्ग (breaking) ⇄ बन्ध (building) of a सेतु."),
            [("Vomiting and diarrhoea", "Both are diseases in the same list, not opposites."),
             ("Dawn and the evening", "Card 7 names no time of day."),
             ("Kapha and Pitta disease", "Those two stand in card 6, not card 7.")],
            "सेतुभङ्ग ⇄ सेतुबन्ध, with अशुभ ⇄ शुभ.",
            "भङ्ग ⇄ बन्ध."),
        mcq("transfer", 5, "By the pattern of आदिषु + अशुभः → आदिष्वशुभः, how is किन्तु + अहम् (but I) joined in a new example?",
            ("किन्त्वहम्", "उ before the unlike vowel अ → व्: किन्तु + अहम् → किन्त्वहम्."),
            [("किन्तोहम्", "ओ would need अ before उ; here उ comes first."),
             ("किन्त्यहम्", "य् comes from इ or ई, not from उ."),
             ("किन्तूहम्", "ऊ would need उ + उ; अ is unlike उ.")],
            "किन्तु + अहम् = किन्त्वहम्, like आदिषु + अशुभः = आदिष्वशुभः.",
            "उ + unlike vowel → व्.",
            teaches="उ before an unlike vowel becomes व्: आदिषु + अशुभः → आदिष्वशुभः."),
    ],
}

# ---------------------------------------------------------------- unit 8
AUTHORED["8"] = {
    "title": "अशुभ काल, नक्षत्र और वैद्य की दशा",
    "question": "By card 8, which times, lunar days and nakṣatras are inauspicious, and when should the physician not follow the messenger?",
    "rule": ("Inauspicious: both twilights, the 4th, 6th and 9th lunar days, parva days and the nakṣatras Bharaṇī to Pūrvā; also a "
             "messenger who comes when the physician is asleep, naked, oiled or facing south. On an ill sign the physician should not follow him."),
    "limits": ("Prose, low confidence. Midday (printed मध्यान्ह) and midnight (printed आर्द्रारात्रि) rest on corrections; यश्च ... "
               "and यो वा ... print no predicate; the Pūrvā nakṣatras are unspecified; अशस्तम् and vyādhitāśraya can be read two ways. "
               "No question on these."),
    "explain_hi": ("यह लम्बी इकाई तीन बातें कहती है। "
                   "पहले अशुभ समय: दोनों सन्ध्याएँ, चतुर्थी, षष्ठी और नवमी तिथियाँ, पर्व के दिन, ग्रह के उपराग (ग्रहण) या उत्पात का दर्शन, "
                   "और भरणी, कृत्तिका, आर्द्रा, आश्लेषा, मघा, मूल और पूर्वा नक्षत्र; छपे ‘मध्यान्ह’ को मध्याह्न (दोपहर) और ‘आर्द्रारात्रि’ को अर्धरात्रि (आधी रात) पढ़ना सुधार पर टिका है। "
                   "फिर वह दूत जो वैद्य के पास तब आता है जब वैद्य सोया, नंगा, भूमि पर लेटा, तेल लगाए, खुले बाल, दक्षिण की ओर मुख किए हो; "
                   "या जो दक्षिण दिशा की ओर अंजलि करके एक पैर पर खड़ा हो। "
                   "अन्त में: दूत जब बता रहा हो और वैद्य कोई अशुभ इन्द्रिय-विषय देखे या उसकी कल्पना करे, तो वह उसके पीछे न जाए (नानुयायात्)। "
                   "‘यश्च’ और ‘यो वा’ वाले वाक्यों की क्रिया नहीं छपी।"),
    "hook": "दोनों सन्ध्याएँ, चौथ-छठ-नवमी, भरणी से मूल और पूर्वा नक्षत्र अशुभ; अशुभ दिखे तो दूत के पीछे न जाए।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By card 8, which direction is named both for the physician's face and for the messenger's añjali?",
            ("South", "दक्षिणाभिमुखम् (facing south) and दिशं याम्याम् (the southern direction)."),
            [("North", "Card 8 names the south (दक्षिण, याम्या), not the north."),
             ("East", "Card 8 names the south (दक्षिण, याम्या), not the east."),
             ("West", "Card 8 names the south (दक्षिण, याम्या), not the west.")],
            "दक्षिण / याम्या = south.",
            "दक्षिणाभिमुखं; दिशं याम्यां प्रति."),
        order(1, "Put the nakṣatras named in card 8 in the printed order.",
              ["भरणी", "कृत्तिका", "आर्द्रा", "आश्लेषा", "मघा", "मूल"],
              "भरणी, कृत्तिका, आर्द्रा, आश्लेषा, मघा, मूल (then the Pūrvā ones).",
              "भरणी → कृत्तिका → आर्द्रा → आश्लेषा → मघा → मूल."),
        match(2, "Match each word for the physician's state in card 8 to its meaning.",
              [["सुप्तम्", "asleep"], ["नग्नम्", "naked"], ["अभ्यक्तम्", "anointed with oil"], ["मुक्तकेशम्", "with loosened hair"],
               ["दक्षिणाभिमुखम्", "facing south"]],
              "सुप्तम् = asleep, नग्नम् = naked, अभ्यक्तम् = anointed with oil, मुक्तकेशम् = with loosened hair, दक्षिणाभिमुखम् = facing south.",
              "सुप्तम्, नग्नम्, अभ्यक्तम्, मुक्तकेशम्, दक्षिणाभिमुखम्.",
              role="extend",
              teaches="These accusatives agree with वैद्यम्: they describe the physician as the ill-omened messenger finds him."),
        multi("discriminate", 3, "By card 8, which lunar days (तिथि) are named as inauspicious?",
              [("The second (द्वितीया)", "No: द्वितीया is not named."),
               ("The fourth (चतुर्थी)", "Yes: चतुर्थी is named."),
               ("The sixth (षष्ठी)", "Yes: षष्ठी is named."),
               ("The eighth (अष्टमी)", "No: अष्टमी is not named."),
               ("The ninth (नवमी)", "Yes: नवमी is named.")],
              [1, 2, 4],
              "चतुर्थी, षष्ठी, नवमी, and the parva days.",
              "...चतुर्थीषष्ठीनवमीपर्वदिनेषु."),
        mcq("apply", 4, "By card 8, what should the physician do if, while the messenger is speaking, he notices an ill-omened sense-object?",
            ("Not follow the messenger", "तं च नानुयायात्: he should not follow him."),
            [("Follow him without delay", "Card 8 says the opposite: न अनुयायात्."),
             ("Wait until the next dawn", "Card 8 names no waiting for dawn."),
             ("Send for a second messenger", "Card 8 names no second messenger.")],
            "अशुभम् इन्द्रियार्थम् उपलक्षयेत् ... तं च नानुयायात्.",
            "न + अनुयायात् = should not follow."),
        mcq("transfer", 5, "By the pattern of च + उपतिष्ठति → चोपतिष्ठति in card 8, how is न + उपविशति (does not sit) joined in a new example?",
            ("नोपविशति", "अ + उ → ओ: न + उपविशति → नोपविशति."),
            [("नौपविशति", "औ comes from अ + ओ or औ, not from अ + उ."),
             ("नूपविशति", "ऊ comes from उ + उ, not from अ + उ."),
             ("न्वुपविशति", "व् comes from उ before an unlike vowel; here अ comes first.")],
            "न + उपविशति = नोपविशति, like च + उपतिष्ठति = चोपतिष्ठति.",
            "अ + उ → ओ.",
            teaches="अ before उ gives ओ: च + उपतिष्ठति → चोपतिष्ठति."),
    ],
}

# ---------------------------------------------------------------- unit 9
AUTHORED["9"] = {
    "title": "अतोऽन्यथा पुनः",
    "question": "By card 9, what is to be done for the patient when the omens are otherwise?",
    "rule": ("In the contrary case (अतोऽन्यथा), one like mother and father to the patient, with a mind soft with compassion and "
             "cheerful, is to hold out complete health (अत्यन्तम् आरोग्यम्) to him by comforting (आश्वासनेन)."),
    "limits": ("Prose, medium confidence. The agent is not named (the physician is understood; none is supplied). The printed "
               "मनसासौमनस्यवता is read मनसा + सौमनस्यवता (a missing space): no question on that reading. प्रधातव्यम् may also be "
               "'put forward, assured'. 'Otherwise' = when the omens are not as just described."),
    "explain_hi": ("‘अतोऽन्यथा’ = इससे अन्यथा, यानी जब शकुन ऊपर बताए अनुसार न हों। "
                   "तब करुणा से कोमल और प्रसन्न मन से, रोगी के लिए माता-पिता के समान बनकर, आश्वासन द्वारा पूर्ण आरोग्य का भरोसा दिया जाना चाहिए (प्रधातव्यम्)। "
                   "करने वाले का नाम नहीं छपा; वैद्य समझा जाता है। "
                   "छपे ‘मनसासौमनस्यवता’ को मनसा + सौमनस्यवता पढ़ा गया (रिक्त स्थान छूटा); ‘असौमनस्य’ (उदासी) अर्थ के विरुद्ध होता। "
                   "‘अतोऽन्यथा’ में अतः + अन्यथा है: अः + अ → ओऽ।"),
    "hook": "शकुन ठीक हों तो माता-पिता जैसा बनकर रोगी को आरोग्य का भरोसा दो।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By card 9, the one who reassures the patient is to be like whom?",
            ("Mother and father", "मातापितृसमेन: equal to mother and father."),
            [("A king and a judge", "Card 9 names no king or judge."),
             ("A teacher and a pupil", "Card 9 names no teacher or pupil."),
             ("A friend and a guest", "Card 9 names no friend or guest.")],
            "मातापितृसम = like mother and father.",
            "मातापितृसमेनातुरस्य."),
        match(1, "Match each word of card 9 to its meaning.",
              [["करुणा", "compassion"], ["सौमनस्य", "cheerfulness"], ["आश्वासन", "comforting, reassurance"],
               ["आरोग्य", "health"], ["अत्यन्तम्", "complete, utmost"]],
              "करुणा = compassion, सौमनस्य = cheerfulness, आश्वासन = comforting, आरोग्य = health, अत्यन्तम् = complete.",
              "करुणा, सौमनस्य, आश्वासन, आरोग्य, अत्यन्तम्."),
        order(2, "Put the printed parts of card 9 in order.",
              ["अतोऽन्यथा पुनः", "करुणापेशलेन", "मनसासौमनस्यवता", "मातापितृसमेनातुरस्यात्यंतमारोग्यमाश्वासनेन", "प्रधातव्यं"],
              "Otherwise, however; soft with compassion; with a cheerful mind; by one like mother and father, complete health to the patient by comforting; is to be held out.",
              "अतोऽन्यथा पुनः → करुणापेशलेन → मनसासौमनस्यवता → मातापितृसमेन... → प्रधातव्यं.",
              role="extend",
              teaches="The instrumentals give the agent and his manner; the gerundive प्रधातव्यम् (is to be held out) closes the sentence."),
        mcq("discriminate", 3, "By card 9, when is complete health to be held out to the patient?",
            ("When the omens are not as described", "अतोऽन्यथा: otherwise than this, i.e. when the omens are not as just described."),
            [("Only when the messenger is a brāhmaṇa", "Card 9 sets no condition on the messenger's class."),
             ("Only after the patient's dreams are told", "Card 9 sets no condition on dreams."),
             ("Only once the fee has been agreed upon", "Card 9 names no fee.")],
            "अतोऽन्यथा = in the contrary case.",
            "अतोऽन्यथा पुनः ... प्रधातव्यम्."),
        mcq("apply", 4, "Which split of अतोऽन्यथा in card 9 is right?",
            ("अतः + अन्यथा", "अः + अ → ओ, and the अ drops (ऽ): अतोऽन्यथा."),
            [("अतो + न्यथा", "न्यथा is not a word; ऽ marks a dropped अ."),
             ("अतः + नयथा", "नयथा is not a word here."),
             ("अत + अन्यथा", "अत is not a word here; the form is अतः.")],
            "अतः (than this) + अन्यथा (otherwise).",
            "अः + अ → ओऽ."),
        mcq("transfer", 5, "By the pattern of अतः + अन्यथा → अतोऽन्यथा, how is शिष्यः + अयम् (this is the pupil) joined in a new example?",
            ("शिष्योऽयम्", "अः + अ → ओ, and the अ drops (ऽ)."),
            [("शिष्यायम्", "आ would need अ + अ with no visarga; अः + अ gives ओऽ."),
             ("शिष्यरयम्", "र् comes from a visarga after vowels other than अ or आ."),
             ("शिष्य अयम्", "अः leaves अ with a gap only before vowels other than अ.")],
            "शिष्यः + अयम् = शिष्योऽयम्, like अतः + अन्यथा = अतोऽन्यथा.",
            "अः + अ → ओऽ.",
            teaches="अः before अ becomes ओ and the अ drops (ऽ): अतः + अन्यथा → अतोऽन्यथा."),
    ],
}

# ---------------------------------------------------------------- unit 10
AUTHORED["10"] = {
    "title": "प्रस्थानगमनप्रवेशेषु",
    "question": "By card 10, what do the hundred and eight auspicious things do, and by what means?",
    "rule": ("At setting out, going and entering (प्रस्थानगमनप्रवेशेषु), the hundred and eight auspicious things (अष्टोत्तरं "
             "मङ्गलानां शतम्), such as curd, honey, ghee and flowers, by sight, touch and mention remove the inauspicious and bestow the highest success."),
    "limits": ("Prose, low confidence; one long list, not checked to add up to 108: no question on counts. No question on the "
               "conjectural readings (mirror, cloud, fresh meat), the unclear वंरुण, the epithets, or the probable or disputed "
               "identifications (cāṣa, kīcaka, rocanā, siddhārthaka, priyaṅgu)."),
    "explain_hi": ("यह बहुत लम्बी सूची ‘प्रस्थान, गमन और प्रवेश के समय’ से आरम्भ होती है और इस सार पर समाप्त होती है: "
                   "‘मंगलों का यह एक सौ आठ का समूह देखने, छूने और नाम लेने से अशुभों को हटाकर उत्तम अर्थसिद्धि देता है।’ "
                   "सूची में खाने की वस्तुएँ (दही, मधु, घी, लाजा), वनस्पतियाँ (उदुम्बर यानी गूलर, अश्वत्थ यानी पीपल, हरिद्रा यानी हल्दी, वचा यानी बच: मानक पहचान), "
                   "पशु-पक्षी, देवता, नदियाँ, शास्त्र और शुभ शब्द (स्वस्ति, वषट्कार, ओंकार) हैं। "
                   "सूची के शब्द गिनकर १०८ से मिलाए नहीं गए हैं, और कई पाठ अनुमानित हैं (जैसे ‘दर्श’ को आदर्श यानी दर्पण, ‘अबुदः’ को अम्बुदः यानी मेघ पढ़ना); ‘वंरुण’ अस्पष्ट है। "
                   "चाष (सम्भवतः नीलकण्ठ), रोचना (सम्भवतः गोरोचन), सिद्धार्थक (सम्भवतः सफेद सरसों) और प्रियङ्गु (सम्भावित, विवादित) की पहचान पक्की नहीं।"),
    "hook": "१०८ मंगल: देखो, छुओ या नाम लो; अशुभ हटे, उत्तम सिद्धि मिले।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By card 10, how does the closing phrase number the auspicious things?",
            ("A hundred and eight", "अष्टोत्तरं मङ्गलानां शतम्: a hundred with eight over."),
            [("One hundred, no more", "शतम् has अष्टोत्तरम् (eight over) with it: 108."),
             ("One thousand in all", "सहस्रम् appears only in 'a thousand men', one item of the list."),
             ("Only eight in all", "अष्ट (eight) is added over शतम् (a hundred).")],
            "अष्टोत्तरं शतम् = 108.",
            "एतदष्टोत्तरं मंगलानांशतं."),
        order(1, "Put the first items of card 10's list in the printed order.",
              ["दधि", "मधु", "घृत", "लाज", "पुष्प", "अक्षत"],
              "Curd, honey, ghee, parched grain, flowers, unbroken rice.",
              "दधि → मधु → घृत → लाज → पुष्प → अक्षत."),
        match(2, "Match each item of card 10 to its meaning.",
              [["दधि", "curd"], ["उदुम्बर", "cluster fig (Ficus racemosa; standard)"],
               ["अश्वत्थ", "peepal (Ficus religiosa; standard)"], ["हरिद्रा", "turmeric (Curcuma longa; standard)"],
               ["वचा", "sweet flag (Acorus calamus; standard)"]],
              "दधि = curd; उदुम्बर = cluster fig, अश्वत्थ = peepal, हरिद्रा = turmeric, वचा = sweet flag (all standard).",
              "दधि, उदुम्बर, अश्वत्थ, हरिद्रा, वचा.",
              role="extend",
              teaches="The list mixes foods, plants, animals, gods, places and words; the plant names keep the data's identifications."),
        multi("discriminate", 3, "By card 10, by which means do the auspicious things remove the inauspicious?",
              [("By sight (दर्शन)", "Yes: दर्शनात्."),
               ("By eating (भक्षण)", "No: eating is not named; the three are sight, touch and mention."),
               ("By touch (स्पर्शन)", "Yes: स्पर्शनात्."),
               ("By mention (कीर्तन)", "Yes: कीर्तनात्."),
               ("By wearing (धारण)", "No: wearing is not named.")],
              [0, 2, 3],
              "दर्शनात् स्पर्शनात् कीर्तनात्: by sight, touch and mention.",
              "दर्शन, स्पर्शन, कीर्तन."),
        mcq("apply", 4, "By card 10, on which occasions are these auspicious things met?",
            ("Setting out, going and entering", "प्रस्थानगमनप्रवेशेषु: at setting out, going and entering."),
            [("Eating, bathing and sleeping", "Card 10 names no meals, baths or sleep."),
             ("Birth, marriage and funeral rites", "Card 10 names none of these occasions."),
             ("Sowing, reaping and storing grain", "Crops (सस्यानि) are an item of the list, not an occasion.")],
            "प्रस्थान, गमन, प्रवेश.",
            "प्रस्थानगमनप्रवेशेषु."),
        mcq("transfer", 5, "By the pattern of धन्वन्तरिः + वामनः → धन्वन्तरिर्वामनः in card 10, how is मुनिः + वदति (the sage speaks) joined in a new example?",
            ("मुनिर्वदति", "इः before a voiced sound → इर्: मुनिः + वदति → मुनिर्वदति."),
            [("मुनि वदति", "After इ the visarga is not dropped before a voiced sound; it becomes र्."),
             ("मुनिस्वदति", "स् comes from a visarga before त or थ, not before व."),
             ("मुनिश्वदति", "श् comes from a visarga before च or छ, not before व.")],
            "मुनिः + वदति = मुनिर्वदति, like धन्वन्तरिः + वामनः = धन्वन्तरिर्वामनः.",
            "Visarga after इ, before a voiced sound → र्.",
            teaches="A visarga after a vowel other than अ or आ becomes र् before a voiced sound: धन्वन्तरिः + वामनः → धन्वन्तरिर्वामनः."),
    ],
}

# ---------------------------------------------------------------- unit 11
AUTHORED["11"] = {
    "title": "अपिच",
    "question": "What does card 11 add, and how are its two words printed?",
    "rule": ("अपि च = 'and further' (अपि also, च and): a connecting formula. The print joins the two words with no space, "
             "though no sandhi joins them."),
    "limits": "Prose, a connecting formula of two words; no verb is printed. What it connects is not stated in the line.",
    "explain_hi": ("‘अपि च’ का अर्थ है ‘और भी’: अपि (भी) + च (और)। "
                   "यह एक जोड़ने वाला सूत्र है; पंक्ति में कोई क्रिया नहीं। "
                   "छपाई में दोनों शब्द बिना रिक्त स्थान के ‘अपिच’ छपे हैं, जबकि यहाँ कोई सन्धि नहीं होती (इ के बाद व्यंजन च है)। "
                   "इस अध्याय के ऐसे और जोड़ने वाले शब्द: अथ (अब, कार्ड १), तद्यथा (वह इस प्रकार है, कार्ड ५), तथा (इसी प्रकार, कार्ड ७)।"),
    "hook": "अपि च: ‘और भी’।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 11, what does अपि च mean?",
            ("And further", "अपि (also) + च (and): and further."),
            [("Not at all", "That would need न; अपि च adds, it does not deny."),
             ("Therefore", "Therefore would be अतः; अपि च means 'and further'."),
             ("That is as follows", "That is तद्यथा (card 5); अपि च means 'and further'.")],
            "अपि च = and further.",
            "अपि + च."),
        match(1, "Match each connecting word of this chapter (listed on card 11) to its meaning.",
              [["अथ", "now (card 1)"], ["तद्यथा", "that is as follows (card 5)"], ["तथा", "likewise (card 7)"],
               ["अपि च", "and further (card 11)"]],
              "अथ = now, तद्यथा = that is as follows, तथा = likewise, अपि च = and further.",
              "अथ, तद्यथा, तथा, अपि च."),
        fill(2, "In card 11, the word for 'and' is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("च", None, "ca", "cha"),
             "च = and: अपि च = also and, 'and further'.",
             "च (and) follows the word it joins: अपि च = 'and further'.",
             "च = and."),
        mcq("discriminate", 3, "Why is the printed अपिच read as two words?",
            ("A space is missing; no sandhi applies", "इ before the consonant च makes no sandhi: अपि च."),
            [("It is a single verb that means 'covers'", "अपिच is not a verb; it is अपि + च."),
             ("इ and च merge into one new sound", "A vowel before a consonant does not merge with it."),
             ("The च is a case ending added to अपि", "अपि is an indeclinable; it takes no case ending.")],
            "अपिच = अपि + च, printed without a space.",
            "अपि च: two words."),
        mcq("apply", 4, "What kind of words make up card 11?",
            ("A connecting formula", "अपि च = 'and further': a connecting formula."),
            [("A list of good omens", "Card 11 names no omen."),
             ("A rule for treatment", "Card 11 names no treatment."),
             ("A chapter heading", "The heading is card 1 (अथातो ... व्याख्यास्यामः).")],
            "Card 11 is only अपि च, 'and further'.",
            "अपि च = connecting formula."),
        mcq("transfer", 5, "By the sense of अपि (also) in card 11, what does सोऽपि गच्छति mean in a new example?",
            ("He too goes", "अपि = also, too: सः + अपि → सोऽपि, he too."),
            [("He never goes", "'Never' needs a negative such as न; अपि alone means 'too'."),
             ("He goes alone", "'Alone, only' would be एव; अपि means 'too'."),
             ("He does not go", "'Not' would need न; अपि means 'too'.")],
            "सोऽपि गच्छति = he too goes.",
            "अपि = also, too.",
            teaches="अपि after a word means 'also, too'; with च it gives अपि च, 'and further'."),
    ],
}

# ---------------------------------------------------------------- unit 12
AUTHORED["12"] = {
    "title": "पुन्नामानः पक्षिणो वामाः शुभाः",
    "question": "By card 12, on which side are male-named birds and female-named creatures auspicious, and what changes at entering?",
    "rule": ("Birds with male names (पुन्नामानः) are auspicious on the left (वामाः); those with female names (स्त्रीनामानः) on the "
             "right (प्रदक्षिणाः); at entering (प्रवेशे) these are reversed (विपरीताः)."),
    "limits": ("Prose, low confidence, partly damaged: displaced vowel signs and an unclear रला in the female-named list; the न "
               "clause (peacock, bear, dog; elephant, goat, payas) is unsettled; the dog-and-jackal rule rests on a conjecture. "
               "No question on these, nor on what 'reversed' turns into."),
    "explain_hi": ("यह इकाई दिशा का नियम देती है: पुरुष नाम वाले पक्षी बाईं ओर (वामाः) शुभ हैं; स्त्री नाम वाले दाहिनी ओर (प्रदक्षिणाः) शुभ हैं। "
                   "स्त्री नाम वालों की सूची में शिवा (सम्भवतः सियारिन), कोकिला (सम्भवतः कोयल), छुछुन्दरी (छछूंदर, मानक), सूकरी (मादा सूअर), "
                   "गृहगोधिका (सम्भवतः घर की छिपकली) और एक खुर वाले पशु हैं; छपाई में मात्राएँ खिसकी हैं और ‘रला’ अस्पष्ट है। "
                   "प्रवेश के समय ये विपरीत (उलटे) हैं। "
                   "‘न’ वाला अंश (मोर, भालू, श्रीकण्ठ, कुत्ता; हाथी, बकरा, पयस्) स्पष्ट नहीं, और कुत्ते-सियार वाला नियम अनुमानित पाठ पर टिका है। "
                   "‘पक्षिणो वामाः’ में पक्षिणः + वामाः है: अः घोष व्यंजन से पहले ओ बनता है।"),
    "hook": "पुरुष-नाम पक्षी बाएँ, स्त्री-नाम दाएँ शुभ; प्रवेश में उलटा।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By card 12, on which side are birds with male names auspicious?",
            ("On the left", "पुन्नामानः पक्षिणो वामाः शुभाः: on the left."),
            [("On the right", "The right (प्रदक्षिणाः) is said of the female-named ones."),
             ("Straight ahead", "Card 12 names no 'ahead'; it names left and right."),
             ("Overhead", "Card 12 names no 'overhead'; it names left and right.")],
            "पुन्नामानः → वामाः (left).",
            "पुन्नामानः पक्षिणो वामाः शुभाः."),
        match(1, "Match each word of card 12 to its meaning.",
              [["पुन्नामानः", "having male names"], ["स्त्रीनामानः", "having female names"], ["वामाः", "on the left"],
               ["प्रदक्षिणाः", "on the right"], ["विपरीताः", "reversed"]],
              "पुन्नामानः = having male names, स्त्रीनामानः = having female names, वामाः = on the left, प्रदक्षिणाः = on the right, विपरीताः = reversed.",
              "पुन्नामानः → वामाः; स्त्रीनामानः → प्रदक्षिणाः; प्रवेशे → विपरीताः."),
        order(2, "Put these sure parts of card 12 in the printed order.",
              ["पुन्नामानः पक्षिणो", "वामाः शुभाः", "स्त्रीनामानः प्रदक्षिणाः", "प्रवेशे तु विपरीताः"],
              "Male-named birds; on the left auspicious; female-named, on the right; but at entering reversed.",
              "पुन्नामानः पक्षिणो → वामाः शुभाः → स्त्रीनामानः प्रदक्षिणाः → प्रवेशे तु विपरीताः.",
              role="extend",
              teaches="Card 12 gives a rule (male-named left, female-named right) and then its exception at entering (प्रवेशे तु)."),
        mcq("discriminate", 3, "By card 12, what happens to these side rules at entering (प्रवेशे)?",
            ("They are reversed", "प्रवेशे तु विपरीताः: but at entering they are reversed."),
            [("They stay the same", "Card 12 says reversed (विपरीताः), not the same."),
             ("All become inauspicious", "Card 12 says reversed, not that all become inauspicious."),
             ("All become auspicious", "Card 12 says reversed, not that all become auspicious.")],
            "प्रवेशे = at entering; विपरीताः = reversed.",
            "प्रवेशे तु विपरीताः."),
        mcq("apply", 4, "A student says: by card 12, male-named birds are auspicious on the right. What is wrong?",
            ("Card 12 puts them on the left", "पुन्नामानः पक्षिणो वामाः शुभाः: on the left."),
            [("Card 12 names no birds at all", "It does: पक्षिणः (birds) with male names."),
             ("Card 12 calls such birds always bad", "It calls them auspicious (शुभाः) on the left."),
             ("Card 12 speaks only of beasts", "It speaks of birds (पक्षिणः) with male names.")],
            "Male-named birds: left; female-named: right.",
            "वाम = left; प्रदक्षिण = right."),
        mcq("transfer", 5, "By the sense of वाम (left) in card 12, what does वामे हस्ते mean in a new example?",
            ("In the left hand", "वाम = left: वामे हस्ते, in the left hand."),
            [("In the right hand", "The right would be दक्षिणे; वाम here is left."),
             ("In both the hands", "Both hands would be the dual हस्तयोः; वामे हस्ते is one hand."),
             ("In the raised hand", "Raised would be उद्यते or similar; वाम here is left.")],
            "वामे हस्ते = in the left hand.",
            "वाम = left.",
            teaches="वाम = left, as in पक्षिणो वामाः शुभाः; the right side is दक्षिण / प्रदक्षिण."),
    ],
}

# ---------------------------------------------------------------- unit 13
AUTHORED["13"] = {
    "title": "सर्वथा ऽपि दर्शनं",
    "question": "By card 13, the sight of which four creatures is named, and what does the line leave unsaid?",
    "rule": ("सर्वथा अपि दर्शनम्: 'in every way, also, the sight' of the bharadvāja (probably the skylark), cāṣa (probably the "
             "Indian roller), bhāsa (probably the vulture) and mongooses (नकुल; standard). No predicate is printed."),
    "limits": ("Prose, medium confidence. No predicate is printed and none is supplied. That the sight is favourable is only "
               "suggested by the contrast with card 14 ('mention desired, not sight'), not stated: no question on whether it is good or bad."),
    "explain_hi": ("यह पंक्ति कहती है: ‘हर प्रकार से भी, भरद्वाज (सम्भवतः भरत पक्षी), चाष (सम्भवतः नीलकण्ठ), भास (सम्भवतः गिद्ध) और नकुल (नेवला, मानक) का दर्शन।’ "
                   "इसके आगे कोई विधेय नहीं छपा, इसलिए दर्शन शुभ है या अशुभ, यह इस पंक्ति में नहीं कहा गया। "
                   "डेटा के अनुसार कार्ड १४ के ‘नाम लेना इष्ट, दर्शन नहीं’ से विरोध यह संकेत देता है कि यहाँ दर्शन शुभ माना गया है, पर यह कहा नहीं गया। "
                   "‘-नकुलानाम्’ षष्ठी बहुवचन है: इन चारों का दर्शन। चारों नाम एक द्वन्द्व समास में हैं।"),
    "hook": "भरद्वाज, चाष, भास, नकुल: इनका दर्शन; फल छपा नहीं।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 13, what does दर्शनम् mean?",
            ("Sight", "दर्शनम् = sight, seeing."),
            [("Touch", "Touch would be स्पर्शन (as in card 10); दर्शनम् is sight."),
             ("Mention", "Mention would be कीर्तन (as in card 10); दर्शनम् is sight."),
             ("Hearing", "Hearing would be श्रवण; दर्शनम् is sight.")],
            "दर्शनम् = sight.",
            "दर्शन = sight."),
        match(1, "Match each word of card 13 to its meaning.",
              [["सर्वथा", "in every way"], ["भरद्वाज", "probably the skylark"], ["चाष", "probably the Indian roller"],
               ["भास", "probably the vulture"], ["नकुल", "mongoose (standard)"]],
              "सर्वथा = in every way; भरद्वाज, चाष, भास: probable identifications; नकुल = mongoose (standard).",
              "सर्वथा, भरद्वाज, चाष, भास, नकुल."),
        order(2, "Put the four creatures of card 13 in the printed order.",
              ["भरद्वाज", "चाष", "भास", "नकुल"],
              "भरद्वाज-चाष-भास-नकुलानाम्: bharadvāja, cāṣa, bhāsa, mongoose.",
              "भरद्वाज → चाष → भास → नकुल.",
              role="extend",
              teaches="A dvandva lists its members in order and puts the case ending only at the end: -नकुलानाम्."),
        mcq("discriminate", 3, "In card 13, what case and number is भरद्वाजचाषभासनकुलानां?",
            ("Genitive plural", "-आनाम् = genitive plural: the sight 'of' the four."),
            [("Nominative plural", "The nominative plural would end in -आः (नकुलाः)."),
             ("Accusative singular", "The accusative singular would end in -म् (नकुलम्)."),
             ("Locative plural", "The locative plural would end in -एषु (नकुलेषु).")],
            "-नकुलानाम् = genitive plural.",
            "-आनाम् = genitive plural."),
        multi("apply", 4, "Which statements fit card 13 as printed?",
              [("It names the mongoose (नकुल)", "Yes: नकुल is the last member of the compound."),
               ("It says this sight is favourable", "No: no predicate is printed; the result is not stated."),
               ("It names the musk shrew (छुछुन्दरी)", "No: the musk shrew is in card 12, not card 13."),
               ("Its four names form one compound", "Yes: भरद्वाज-चाष-भास-नकुलानाम्, one dvandva.")],
              [0, 3],
              "Four names in one dvandva, the sight of them; no predicate.",
              "सर्वथा ऽपि दर्शनं ...नकुलानां (no predicate)."),
        mcq("transfer", 5, "By the pattern of -नकुलानां दर्शनं, what does अश्वगजानां दर्शनम् mean in a new example?",
            ("The sight of horses and elephants", "-आनाम् = genitive plural: the sight of horses and elephants."),
            [("The horses see the elephants", "दर्शनम् is a noun, 'sight'; no verb 'see' is used."),
             ("The sight from horses and elephants", "'From' would be the ablative; -आनाम् is genitive."),
             ("The sight of one horse only", "-आनाम् is plural, and the compound names two kinds.")],
            "अश्वगजानां दर्शनम् = the sight of horses and elephants.",
            "dvandva + -आनाम् = 'of A and B'.",
            teaches="A dvandva in the genitive plural (-आनाम्) means 'of A, B ...': भरद्वाजचाषभासनकुलानां दर्शनम्."),
    ],
}

# ================================================================ NOTES_HI
NOTES_HI = {
    "1": ("गद्य; विश्वास उच्च; एक छपी पंक्ति (०२.१२.१); कोई पाठ-चिह्न नहीं। अध्याय का आरम्भिक सूत्र। ‘शारीरम्’ किस संज्ञा का विशेषण है, यह छपा नहीं। "
          "डेटा के शब्द-विभाग में ‘अथातो’ के लिए केवल अथ दिया है, अतः अलग से नहीं; हिन्दी और अंग्रेज़ी अनुवाद में ‘इसलिए’ है। "
          "सन्धि जाँची: अथ + अतः → अथातः (अ + अ → आ); अतः + दूत- → अतो दूत- (अः घोष व्यंजन से पहले → ओ); "
          "दूतादिविज्ञानीयम् + शारीरम् → दूतादिविज्ञानीयं शारीरं (व्यंजन से पहले म् → ं)।"),
    "2": ("गद्य; विश्वास मध्यम; एक छपी पंक्ति (०२.१२.२); कोई पाठ-चिह्न नहीं। रिष्ट = मृत्यु के निकट होने का लक्षण (मानक)। "
          "‘आतुराश्रयम्’ को रिष्ट का विशेषण (बहुव्रीहि) पढ़ा गया; अलग संज्ञा ‘रोगी का आश्रय’ भी सम्भव है। ‘निर्दिष्टम्’ के साथ कोई सहायक क्रिया नहीं छपी। "
          "‘रिष्टमातुराश्रयं’ बिना रिक्त स्थान के छपा। सन्धि जाँची: रिष्टम् + आतुर- → रिष्टमातुर-; आतुर + आश्रयम् → आतुराश्रयम् (अ + आ → आ)।"),
    "3": ("गद्य; विश्वास मध्यम; एक छपी पंक्ति (०२.१२.३)। पाठ-चिह्न (सम्भव): छपा ‘ग्रहचारो’ प से पहले सन्धि-रूप नहीं; ग्रहचारः अपेक्षित, या कोई अक्षर/शब्द छूटा है। "
          "‘पूर्वसंभवः’ (पहले की घटना) का अर्थ अनिश्चित है। जाति = प्रकार (जन्म या जाति भी सम्भव)। ‘तत्संगम’ में तत् = दूत। "
          "सन्धि जाँची: दूतस्य + अपि → दूतस्यापि (अ + अ → आ); -कालाः और -प्रवेशाः घोष व्यंजन से पहले विसर्ग खोते हैं (आः का नियम): कालाः + वैद्यस्य → काला वैद्यस्य।"),
    "4": ("गद्य; विश्वास कम; एक छपी पंक्ति (०२.१२.४), एक लम्बा वाक्य, कर्ता ‘दूतः’ अन्त के पास। पाठ-चिह्न (सम्भव): ‘व्याधिनो’ नियमित रूप नहीं (व्याधितः अपेक्षित); "
          "वस्त्र-समास में ‘नेको’ का ओ और ‘द्रै’ (आर्द्र के लिए) छपाई की भूल लगते हैं; ‘लोष्टुपांगार’ को लोष्ट + अङ्गार और ‘मार्जनोशस्त्र’ को मार्जन + ऊष + शस्त्र पढ़ना अनुमान है; "
          "‘स्पृक्’ अस्पष्ट है; ‘पक्कं’ = पक्वं (प्राकृत जैसी वर्तनी)। ‘-धरः’ (धारण करने वाला) के साथ शरीर-अंग अटपटे हैं; ‘पादाभ्यां भुवं मुञ्चन्’ का अर्थ अस्पष्ट। "
          "पक्के रिक्त-स्थान-दोष: ‘रुदन्निष्ठुरो’, ‘विलिखन्गृहीत्वा’, ‘देशेकाले’। सन्धि जाँची: दूरात् + आह्वयमानः → दूरादाह्वयमानः (स्वर से पहले त् → द्); "
          "निष्ठुरः + अमङ्गल- → निष्ठुरोऽमङ्गल- (अः + अ → ओऽ); वैद्यम् + उपसर्पन् → वैद्यमुपसर्पन्; उपसर्पन् + अशुभः → उपसर्पन्नशुभः (ह्रस्व स्वर के बाद अन्त्य न् स्वर से पहले द्वित्व)।"),
    "5": ("गद्य; विश्वास उच्च; एक छपी पंक्ति (०२.१२.५); कोई पाठ-चिह्न नहीं। आगे के उदाहरणों का परिचय-सूत्र। "
          "सन्धि जाँची: तत् + यथा → तद्यथा (घोष य से पहले त् → द्)।"),
    "6": ("गद्य; विश्वास कम; एक छपी पंक्ति (०२.१२.६)। पाठ-चिह्न (सम्भव): पहले शब्द का ‘द्व’ सम्भवतः ‘द्र’ (द्रव, तरल) की भूल है; ‘-स्थम्’ का द्वितीया अन्त आगे के प्रथमा शब्दों से मेल नहीं खाता, "
          "इसलिए कर्ता (सम्भवतः दूत) और वाक्य-रचना अस्पष्ट। श्लेष्मामय = कफ का रोग (मानक)। "
          "सन्धि जाँची: श्लेष्मामये + अशुभः → श्लेष्मामयेऽशुभः (ए + अ → एऽ); श्लेष्म + आमय → श्लेष्मामय, पित्त + आमय → पित्तामय (अ + आ → आ)।"),
    "7": ("गद्य; विश्वास मध्यम; एक छपी पंक्ति (०२.१२.७); कोई पाठ-चिह्न नहीं। अपूर्ण वाक्य: कर्ता नहीं छपा। पहचान: छर्दि = उलटी (मानक); मेह = मूत्र के रोग, प्रमेह वर्ग (सम्भावित); "
          "अतिसार = दस्त (मानक)। सेतु = बाँध या पुल। सन्धि जाँची: -आदिषु + अशुभः → -आदिष्वशुभः (उ + भिन्न स्वर → व्); मेह + अतिसार → मेहातिसार (अ + अ → आ)।"),
    "8": ("गद्य; विश्वास कम; एक छपी पंक्ति (०२.१२.८)। पाठ-चिह्न (सम्भव): ‘मध्यान्ह’ = मध्याह्न (अक्षरों का उलटफेर); ‘आर्द्रारात्रि’ को अर्धरात्रि पढ़ना अनुमान है (आर्द्रा नक्षत्र अगले शब्द में अलग है); "
          "‘तथा’ बिना रिक्त स्थान के जुड़ा। पक्के रिक्त-स्थान-दोष: ‘वैद्यंसुप्तं’, ‘विक्ळवंछिंदंतं’। ‘यश्च ...’ और ‘यो वा ...’ की क्रिया नहीं छपी; "
          "‘अशस्तम्’ अग्नि-पितृ-कार्य के साथ भी जा सकता है; ‘व्याधिताश्रय’ रोगी का घर या रोगग्रस्त अंग हो सकता है; पूर्वा नक्षत्र स्पष्ट नहीं किए गए। "
          "सन्धि जाँची: च + उपतिष्ठति → चोपतिष्ठति (अ + उ → ओ); न + अनुयायात् → नानुयायात् (अ + अ → आ); कृत्वा + अञ्जलिम् → कृत्वाऽञ्जलिम् (आ + अ → आ, छपाई में ऽ)।"),
    "9": ("गद्य; विश्वास मध्यम; एक छपी पंक्ति (०२.१२.९)। पाठ-चिह्न (सम्भव): ‘मनसासौमनस्यवता’ में रिक्त स्थान छूटा; मनसा + सौमनस्यवता पढ़ा गया (असौमनस्य अर्थ के विरुद्ध)। "
          "कर्ता का नाम नहीं (वैद्य समझा जाता है)। ‘प्रधातव्यम्’ = प्रस्तुत/आश्वस्त किया जाना चाहिए, कई अर्थ सम्भव। "
          "सन्धि जाँची: अतः + अन्यथा → अतोऽन्यथा (अः + अ → ओऽ); मातापितृसमेन + आतुरस्य → मातापितृसमेनातुरस्य (अ + आ → आ); आतुरस्य + अत्यन्तम् → आतुरस्यात्यन्तम् (अ + अ → आ)।"),
    "10": ("गद्य; विश्वास कम; एक छपी पंक्ति (०२.१२.१०), एक लम्बी सूची। पाठ-चिह्न (सम्भव): ‘कुशदर्श’ को कुश + आदर्श (दर्पण) पढ़ना; ‘वंरुण’ अस्पष्ट; ‘मद्सिक्त’ = मदसिक्त, ‘अबुदः’ = अम्बुदः; "
           "‘फलान्यार्द्रे’ को फलानि + आर्द्रम् (ताज़ा, मांस के साथ) पढ़ना; ‘धर्मार्थकामामाश्रितं’ में फालतू ‘मा’; ‘रुंधती’ = अरुन्धती; ‘अपत्यक्षमा’ = अपत्यम्, क्षमा। "
           "पक्के रिक्त-स्थान-दोष: ‘भूमिरभ्युद्धृतासिद्धमन्नं’, ‘सहस्रंनराणां’, ‘मंगलानांशतं’, ‘दर्शनात्स्पर्शनात्कीर्तनाचाशुभानि’ (कीर्तनाच् च अपेक्षित)। "
           "शब्दों की गिनती १०८ से मिलाई नहीं गई। पहचान: उदुम्बर, अश्वत्थ, हरिद्रा, वचा (मानक); सिद्धार्थक, रोचना, चाष, कीचक (सम्भावित); प्रियङ्गु (सम्भावित, विवादित)। "
           "सन्धि जाँची: धन्वन्तरिः + वामनः → धन्वन्तरिर्वामनः (इः घोष वर्ण से पहले → इर्); हयाः + हंसः → हया हंसः (आः घोष से पहले विसर्ग खोता है)।"),
    "11": ("गद्य; विश्वास उच्च; एक छपी पंक्ति (०२.१२.११)। पक्का रिक्त-स्थान-दोष: ‘अपिच’ = अपि च; यहाँ कोई सन्धि नहीं (इ के बाद व्यंजन)। जोड़ने वाला सूत्र।"),
    "12": ("गद्य; विश्वास कम; एक छपी पंक्ति (०२.१२.१२), अंशतः क्षतिग्रस्त। पाठ-चिह्न (सम्भव): ‘श्यामािपंगला’ और ‘गृहगोधिकाैकशफाः’ में मात्राएँ खिसकी हैं (श्यामा-पिङ्गला, गृहगोधिका + एकशफाः पढ़ा गया); "
           "‘रला’ अस्पष्ट; ‘दक्षिणाद्वा मगमनम्’ को दक्षिणाद् वामगमनम् पढ़ना अनुमान है। ‘शिखि... श्वेति न गजाजक पयश्च’ का ‘न’ अपवाद है या कुछ और, तय नहीं। "
           "श्रीकण्ठ अज्ञात; पयस् = दूध या जल। पहचान: छुछुन्दरी (मानक), गृहगोधिका, शिवा, कोकिला (सम्भावित)। "
           "सन्धि जाँची: पक्षिणः + वामाः → पक्षिणो वामाः (अः घोष व्यंजन से पहले → ओ)।"),
    "13": ("गद्य; विश्वास मध्यम; एक छपी पंक्ति (०२.१२.१३); कोई पाठ-चिह्न नहीं। कोई विधेय नहीं छपा; कार्ड १४ (‘नाम लेना इष्ट, दर्शन नहीं’) से विरोध के कारण दर्शन शुभ माना गया लगता है, पर कहा नहीं गया। "
           "पहचान: भरद्वाज (सम्भवतः भरत पक्षी), चाष (सम्भवतः नीलकण्ठ, कार्ड १० भी), भास (सम्भवतः गिद्ध), नकुल = नेवला (मानक)। "
           "‘सर्वथा ऽपि’ का ऽ और रिक्त स्थान छपे रूप में रखे गए; दर्शनम् + भरद्वाज- → दर्शनं भरद्वाज- (व्यंजन से पहले म् → ं)।"),
}

# ================================================================ AIDS
AIDS = {
    "1": {
        "frame": "कब: अथ (अब) → क्यों: अतः (इसलिए) → क्या: दूतादिविज्ञानीय (दूत आदि का ज्ञान), शारीर → क्रिया: व्याख्यास्यामः (हम कहेंगे)।",
        "chunks": "अथातो | दूतादिविज्ञानीयं | शारीरं | व्याख्यास्यामः",
        "sandhi": "अ + अ → आ: अथ + अतः → अथातः · अः घोष व्यंजन से पहले → ओ: अतः + दूत- → अतो दूत-।",
    },
    "2": {
        "frame": "क्या: रिष्टम् (मृत्यु के निकट होने का लक्षण) → किस पर: आतुराश्रयम् (रोगी पर टिका) → स्थिति: निर्दिष्टम् (बताया जा चुका)।",
        "chunks": "निर्दिष्टं | रिष्टमातुराश्रयं",
        "sandhi": "अन्त्य म् + स्वर → जुड़ता है: रिष्टम् + आतुर- → रिष्टमातुर- · अ + आ → आ: आतुर + आश्रयम् → आतुराश्रयम्।",
    },
    "3": {
        "diagram": {"groups": [
            {"label": "दूत की (छपे क्रम में)", "items": ["१ जाति", "२ वेष", "३ भाषा", "४ चेष्टित", "५ देश", "६ काल"]},
            {"label": "वैद्य की (छपे क्रम में)", "items": ["१ तत्संगम: दूत से मिलना", "२ संकल्प", "३ प्रस्थान", "४ प्रयाण", "५ प्रवेश"]},
            {"label": "और", "items": ["ग्रहचार (छपा ‘ग्रहचारो’)", "पूर्वसंभव (अर्थ अनिश्चित)", "स्वप्नदर्शन"]}]},
        "chunks": ("दूतस्यापि तु | जातिवेषभाषाचेष्टितदेशकाला | वैद्यस्य च | तत्संगमसंकल्पप्रस्थानप्रयाणप्रवेशा | ग्रहचारो | पूर्वसंभवः | "
                   "स्वप्नदर्शनानि च | रोगिणः | शुभाशुभं सूचयन्ति"),
        "sandhi": "अ + अ → आ: दूतस्य + अपि → दूतस्यापि · आः घोष व्यंजन से पहले विसर्ग खोता है: -कालाः + वैद्यस्य → -काला वैद्यस्य।",
        "anchors": "पक्का: दूत की छह बातें, वैद्य की पाँच, और स्वप्नदर्शन। अनिश्चित: ग्रहचारो का रूप, पूर्वसंभव का अर्थ। (मेरी याद-पद्धति)",
    },
    "4": {
        "diagram": {"groups": [
            {"label": "सवारी", "items": ["खर: गधा", "उष्ट्र: ऊँट", "महिष: भैंसा"]},
            {"label": "दशा और वाणी (छपे क्रम में)", "items": ["विह्वलः = घबराया", "श्वसन् = हाँफता", "रुदन् = रोता", "निष्ठुरः = कठोर",
                                                      "अमङ्गलाभिधायी = अमंगल बोलता", "दूरादाह्वयमानः = दूर से पुकारता"]},
            {"label": "वस्त्र", "items": ["जीर्ण: पुराना", "विवर्ण: बदरंग", "मलिन: मैला", "छिन्न: फटा"]},
            {"label": "स्थान या समय", "items": ["विकारतुल्यगुण: रोग के समान गुण वाला"]}]},
        "sandhi": ("स्वर से पहले त् → द्: दूरात् + आह्वयमानः → दूरादाह्वयमानः · अः + अ → ओऽ: निष्ठुरः + अमङ्गल- → निष्ठुरोऽमङ्गल- · "
                   "अः घोष व्यंजन से पहले → ओ: दूतः + वैद्यम् → दूतो वैद्यम्।"),
        "anchors": "पक्का: सवारी, दशा-वाणी, वस्त्र के चार शब्द, रोग-समान स्थान/समय। अनुमानित या अस्पष्ट: अङ्गार, ऊष, स्पृक्, व्याधिनो, शरीर-अंगों का ‘धारण’। (मेरी याद-पद्धति)",
    },
    "5": {
        "frame": "तत् (वह) + यथा (जैसे, अर्थात्) = ‘वह इस प्रकार है’ → आगे उदाहरण।",
        "chunks": "तद्यथा",
        "sandhi": "घोष व्यंजन से पहले त् → द्: तत् + यथा → तद्यथा।",
    },
    "6": {
        "seesaw": "श्लेष्मामये अशुभः (कफ के रोग में अशुभ) ⇄ पित्तामये शुभः (पित्त के रोग में शुभ): दोनों इसी इकाई में, ‘तु’ से जुड़े।",
        "chunks": "घृतोदकादिद्वसमीपस्थमतिशीतस्तब्धः | प्रत्यूषसि | श्लेष्मामयेऽशुभः | पित्तामये तु शुभः",
        "sandhi": "ए + अ → एऽ: श्लेष्मामये + अशुभः → श्लेष्मामयेऽशुभः · अ + आ → आ: पित्त + आमये → पित्तामये।",
    },
    "7": {
        "seesaw": "सेतुभङ्गे अशुभः (बाँध टूटे: अशुभ) ⇄ सेतुबन्धे शुभः (बाँध बँधे: शुभ): दोनों इसी इकाई में।",
        "chunks": "तथा सेतुभंगे | छर्दिमेहातिसारादिष्वशुभः | सेतुबंधे तु शुभः",
        "sandhi": "उ + भिन्न स्वर → व्: -आदिषु + अशुभः → -आदिष्वशुभः · अ + अ → आ: मेह + अतिसार → मेहातिसार।",
    },
    "8": {
        "diagram": {"groups": [
            {"label": "अशुभ समय (पक्के)", "items": ["दोनों सन्ध्याएँ", "चतुर्थी, षष्ठी, नवमी", "पर्व के दिन", "ग्रहण या उत्पात का दर्शन"]},
            {"label": "नक्षत्र (छपे क्रम में)", "items": ["१ भरणी", "२ कृत्तिका", "३ आर्द्रा", "४ आश्लेषा", "५ मघा", "६ मूल", "७ पूर्वा"]},
            {"label": "वैद्य की दशा", "items": ["सोया", "नंगा", "भूमि पर लेटा", "तेल लगाए", "खुले बाल", "दक्षिण की ओर मुख"]}]},
        "chain": {"steps": ["दूत रोगी के बारे में बताता है", "वैद्य अशुभ इन्द्रिय-विषय देखे या कल्पना करे", "तं च नानुयायात्: उसके पीछे न जाए"]},
        "sandhi": "अ + उ → ओ: च + उपतिष्ठति → चोपतिष्ठति · अ + अ → आ: न + अनुयायात् → नानुयायात्।",
        "anchors": "अनुमानित: मध्याह्न (छपा मध्यान्ह), अर्धरात्रि (छपा आर्द्रारात्रि); इन पर प्रश्न नहीं। (मेरी याद-पद्धति)",
    },
    "9": {
        "frame": "कब: अतोऽन्यथा (शकुन इसके विपरीत) → कैसे मन से: करुणापेशल, सौमनस्यवत् → कैसा बनकर: मातापितृसम → क्या: अत्यन्त आरोग्य → किससे: आश्वासन → प्रधातव्यम्।",
        "chunks": "अतोऽन्यथा पुनः | करुणापेशलेन | मनसासौमनस्यवता | मातापितृसमेनातुरस्यात्यंतमारोग्यमाश्वासनेन | प्रधातव्यं",
        "sandhi": "अः + अ → ओऽ: अतः + अन्यथा → अतोऽन्यथा · अ + आ → आ: -समेन + आतुरस्य → -समेनातुरस्य।",
    },
    "10": {
        "chain": {"steps": ["कब: प्रस्थान, गमन, प्रवेश", "क्या: मंगलों का अष्टोत्तर शत (१०८)", "कैसे: दर्शन, स्पर्शन, कीर्तन",
                            "फल: अशुभ हटें, उत्तम अर्थसिद्धि"]},
        "diagram": {"groups": [
            {"label": "सूची का आरम्भ (छपे क्रम में)", "items": ["१ दधि: दही", "२ मधु", "३ घृत: घी", "४ लाज: भुना अन्न", "५ पुष्प", "६ अक्षत: अखण्ड चावल"]},
            {"label": "मानक पहचान वाली वनस्पतियाँ", "items": ["उदुम्बर: गूलर", "अश्वत्थ: पीपल", "हरिद्रा: हल्दी", "वचा: बच"]}]},
        "sandhi": "इः घोष वर्ण से पहले → इर्: धन्वन्तरिः + वामनः → धन्वन्तरिर्वामनः · आः घोष वर्ण से पहले विसर्ग खोता है: हयाः + हंसः → हया हंसः।",
        "anchors": "पक्का: तीन अवसर, तीन साधन, संख्या का नाम (अष्टोत्तर शत)। गिनती १०८ से मिलाई नहीं गई; दर्पण, मेघ, ताज़ा मांस अनुमानित पाठ। (मेरी याद-पद्धति)",
    },
    "11": {
        "frame": "अपि (भी) + च (और) = ‘और भी’: जोड़ने वाला सूत्र।",
        "anchors": "इस अध्याय के जोड़ने वाले शब्द: अथ (अब, कार्ड १), तद्यथा (वह इस प्रकार है, कार्ड ५), तथा (इसी प्रकार, कार्ड ७), अपि च (और भी, कार्ड ११)। (मेरी याद-पद्धति)",
        "sandhi": "कोई सन्धि नहीं: इ के बाद व्यंजन च; छपा ‘अपिच’ = अपि च (रिक्त स्थान छूटा)।",
    },
    "12": {
        "contrast": "पुन्नामानः पक्षिणः → वामाः शुभाः (बाएँ शुभ) · स्त्रीनामानः → प्रदक्षिणाः (दाएँ शुभ) · प्रवेशे तु → विपरीताः (उलटे): तीनों इसी इकाई में।",
        "chunks": "पुन्नामानः पक्षिणो | वामाः शुभाः | ... | स्त्रीनामानः प्रदक्षिणाः | ... | प्रवेशे तु विपरीताः",
        "sandhi": "अः घोष व्यंजन से पहले → ओ: पक्षिणः + वामाः → पक्षिणो वामाः।",
    },
    "13": {
        "diagram": {"groups": [
            {"label": "दर्शन किनका (छपे क्रम में)", "items": ["१ भरद्वाज: सम्भवतः भरत पक्षी", "२ चाष: सम्भवतः नीलकण्ठ",
                                                    "३ भास: सम्भवतः गिद्ध", "४ नकुल: नेवला (मानक)"]},
            {"label": "विधेय", "items": ["छपा नहीं: शुभ या अशुभ नहीं कहा"]}]},
        "chunks": "सर्वथा ऽपि | दर्शनं | भरद्वाजचाषभासनकुलानां",
        "sandhi": "व्यंजन से पहले म् → ं: दर्शनम् + भरद्वाज- → दर्शनं भरद्वाज-।",
    },
}

# ================================================================ IMAGE_SPECS
IMAGE_SPECS = {
    ("3", "diagram"): {
        "file": "sh12-duta-vaidya-3.svg",
        "alt": ("Split of card 3 in printed order: the messenger's six features (kind, dress, speech, behaviour, place, time) and "
                "the physician's five (meeting him, intention, setting out, going, entering); all indicate good and bad."),
        "type": "split",
        "title": "कार्ड ३: शुभाशुभ के सूचक",
        "cols": [["दूत की", ["१ जाति", "२ वेष", "३ भाषा", "४ चेष्टित", "५ देश", "६ काल"]],
                 ["वैद्य की", ["१ दूत से मिलना", "२ संकल्प", "३ प्रस्थान", "४ प्रयाण", "५ प्रवेश"]]],
    },
    ("4", "diagram"): {
        "file": "sh12-ashubha-duta-4.svg",
        "alt": ("Table of sure marks of an inauspicious messenger in card 4: riding a donkey, camel or buffalo; agitated, panting, "
                "weeping, harsh, calling from afar; an old, discoloured, dirty, torn garment; a place or time like the disease."),
        "type": "table",
        "title": "कार्ड ४: अशुभ दूत (पक्के अंश)",
        "heads": ["विषय", "छपा शब्द = अर्थ"],
        "rows": [["सवारी", "खर, उष्ट्र, महिष"], ["दशा", "विह्वलः = घबराया"], ["दशा", "श्वसन् = हाँफता"], ["दशा", "रुदन् = रोता"],
                 ["वाणी", "निष्ठुरः = कठोर"], ["वाणी", "दूरादाह्वयमानः"], ["वस्त्र", "जीर्ण, विवर्ण, मलिन, छिन्न"],
                 ["स्थान, समय", "विकारतुल्यगुण"]],
    },
    ("6", "seesaw"): {
        "file": "sh12-kapha-pitta-6.svg",
        "alt": ("Split of card 6: the same dawn sign is inauspicious in a Kapha disease and auspicious in a Pitta disease; "
                "the liquids in the first word rest on a conjectural reading."),
        "type": "split",
        "title": "कार्ड ६: भोर में ठंडा, अकड़ा",
        "cols": [["कफ का रोग", ["श्लेष्मामये", "अशुभः"]],
                 ["पित्त का रोग", ["पित्तामये तु", "शुभः"]]],
    },
    ("7", "seesaw"): {
        "file": "sh12-setu-7.svg",
        "alt": ("Split of card 7: at the breaking of a dam it is inauspicious in vomiting, meha (urinary disorders, probable) and "
                "diarrhoea; at the building of a dam it is auspicious."),
        "type": "split",
        "title": "कार्ड ७: सेतु टूटे या बँधे",
        "cols": [["सेतुभङ्ग: टूटना", ["अशुभ", "छर्दि: उलटी", "मेह (सम्भावित)", "अतिसार: दस्त"]],
                 ["सेतुबन्ध: बाँधना", ["शुभ"]]],
    },
    ("8", "diagram"): {
        "file": "sh12-nakshatra-8.svg",
        "alt": ("Numbered table of card 8: the inauspicious nakṣatras in printed order, Bharaṇī, Kṛttikā, Ārdrā, Āśleṣā, "
                "Maghā, Mūla and the Pūrvā ones (not specified), and the lunar days four, six and nine."),
        "type": "table",
        "title": "कार्ड ८: अशुभ नक्षत्र और तिथियाँ",
        "heads": ["क्रम", "छपा नाम"],
        "rows": [["१", "भरणी"], ["२", "कृत्तिका"], ["३", "आर्द्रा"], ["४", "आश्लेषा"], ["५", "मघा"], ["६", "मूल"],
                 ["७", "पूर्वा (स्पष्ट नहीं)"], ["तिथि", "चतुर्थी, षष्ठी, नवमी"]],
    },
    ("10", "chain"): {
        "file": "sh12-mangala-10.svg",
        "alt": ("Chain of card 10: at setting out, going and entering, the hundred and eight auspicious things, by sight, touch "
                "and mention, remove the inauspicious and give the highest success."),
        "type": "chain",
        "title": "कार्ड १०: १०८ मंगल",
        "steps": ["प्रस्थान, गमन, प्रवेश में", "मंगलों का अष्टोत्तर शत", "दर्शन, स्पर्शन, कीर्तन से", "अशुभ हटें, उत्तम सिद्धि"],
    },
    ("12", "contrast"): {
        "file": "sh12-vama-dakshina-12.svg",
        "alt": ("Table of card 12: birds with male names are auspicious on the left, those with female names on the right; "
                "at entering these are reversed."),
        "type": "table",
        "title": "कार्ड १२: बाएँ और दाएँ",
        "heads": ["कौन, कब", "नियम"],
        "rows": [["पुरुष नाम वाले पक्षी", "बाईं ओर शुभ (वामाः)"], ["स्त्री नाम वाले", "दाहिनी ओर शुभ (प्रदक्षिणाः)"],
                 ["प्रवेश के समय", "उलटे (विपरीताः)"]],
    },
}
