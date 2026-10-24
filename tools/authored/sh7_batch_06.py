from helpers import mcq, match, order, fill, multi, accepts


AUTHORED = {}

# ---------------------------------------------------------------- unit 68
AUTHORED["68"] = {
    "title": "सोमस्तु",
    "question": "What is certain in unit 68, and why is the rest of its sense only a conjecture?",
    "rule": ("Unit 68 opens 'But Soma' (सोमस्तु = सोमः + तु). The rest is damaged; the data reads it by conjecture as "
             "प्राणान् अवलम्बते इत्युक्तम्: 'upholds the life-breaths; thus it has been said'."),
    "limits": ("Prose, low confidence. वलंबत (no verb form) and हत्युक्तं are read by conjecture as अवलम्बते and "
               "इत्युक्तं: no question rests on the verb, on इति or on the sense. Only सोमस्तु and the state of the reading "
               "are asked. Data: the sense agrees with card 65."),
    "explain_hi": ("यह इकाई ‘सोमस्तु’ (किन्तु सोम) से आरम्भ होती है; यह भाग साफ़ छपा है: सोमः + तु, त से पहले विसर्ग स् बना। "
                   "आगे का अंश बिगड़ा है: ‘वलंबत’ कोई क्रिया-रूप नहीं, इसलिए डेटा अनुमान से ‘प्राणान् अवलम्बते इत्युक्तम्’ पढ़ता है: "
                   "सोम प्राणों को सहारा देता है, ऐसा कहा गया है। "
                   "डेटा के अनुसार यह अर्थ कार्ड ६५ से मेल खाता है, जहाँ सोम स्थिरता और शीतलता से प्राणों को धारण करता है। "
                   "यह अनुमानित पाठ है, इसलिए प्रश्न केवल ‘सोमस्तु’ और पाठ की स्थिति पर हैं। "
                   "डेटा के अनुसार यह इकाई परिणाम के अनुसार मर्म-भेदों का प्रसंग समाप्त करती है।"),
    "hook": "सोमस्तु पक्का; आगे का पाठ अनुमान।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In सोमस्तु of unit 68, what does तु mean?",
            ("but, however", "तु = but, however (gram: ind.)."),
            [("and, also", "'And' is च, not तु."),
             ("not, never", "'Not' is न, not तु."),
             ("or, else", "'Or' is वा, not तु.")],
            "सोमस्तु = सोमः (Soma) + तु (but).",
            "तु = but, however."),
        match(1, "Match each particle to its meaning (तु is the one printed in unit 68).",
              [["तु", "but, however"], ["च", "and"], ["वा", "or"], ["हि", "for, indeed"]],
              "तु = but; च = and; वा = or; हि = for, indeed.",
              "तु, च, वा, हि."),
        mcq("extend", 2, "Which split of सोमस्तु in unit 68 is right?",
            ("सोमः + तु", "Visarga before त becomes स्: सोमः + तु → सोमस्तु."),
            [("सोम + स्तु", "स्तु is not a word here; the स् comes from the visarga."),
             ("सोमम् + तु", "सोमम् + तु would be written सोमं तु."),
             ("सोमः + अस्तु", "अः + अ would give ओऽ: सोमोऽस्तु.")],
            "सोमः (Soma, nom. sg.) + तु (but).",
            "ः + त → स्त.",
            teaches="A visarga before त becomes स्: सोमः + तु → सोमस्तु."),
        multi("discriminate", 3, "Which statements fit unit 68 by the data?",
              [("Its confidence is high", "The data gives low confidence."),
               ("It is a metrical verse line", "type: prose."),
               ("सोमस्तु is printed without a flag", "Right: सोमः + तु is sure."),
               ("It joins two printed lines", "The unit is a single printed line."),
               ("The words after सोमस्तु are read by conjecture", "Right: the data flags them and gives low confidence.")],
              [2, 4],
              "सोमस्तु is sure; the verb is restored by conjecture.",
              "Doubtful print: ask only the sure part."),
        mcq("apply", 4, "Why does the visarga of सोमः appear as स् before तु?",
            ("Visarga before त becomes स्", "Right: before त (and थ) the visarga becomes स्."),
            [("Visarga before any voiceless consonant becomes स्",
              "Not before every one: before च it becomes श्, before क or प it stays."),
             ("स् is the last letter of the stem सोम", "The stem is सोम; the स् comes from the visarga."),
             ("Visarga before a voiced consonant becomes स्", "त is voiceless; after अ, a voiced consonant gives ओ.")],
            "सोमः + तु → सोमस्तु: visarga before त → स्.",
            "ः + त → स्त."),
        mcq("transfer", 5, "By the join of सोमः + तु, how is नरः + तु (but the man) joined in a new example?",
            ("नरस्तु", "Visarga before त becomes स्: नरः + तु → नरस्तु."),
            [("नरो तु", "ओ comes before a voiced consonant; त is voiceless."),
             ("नरर्तु", "र् comes after vowels other than अ/आ; here the vowel is अ."),
             ("नरश्तु", "श् comes before च/छ, not before त.")],
            "नरः + तु = नरस्तु, like सोमः + तु = सोमस्तु.",
            "ः + त → स्त.",
            teaches="A visarga before त becomes स्: सोमः + तु → सोमस्तु, नरः + तु → नरस्तु."),
    ],
}

# ---------------------------------------------------------------- unit 69
AUTHORED["69"] = {
    "title": "अन्ये त्वाहुः",
    "question": "What does unit 69 say, and how is त्वाहुः joined?",
    "rule": ("'Others, however, say': अन्ये (others) + तु (however) + आहुः (they say; perfect in form, present in sense). "
             "तु + आहुः → त्वाहुः (उ + आ → वा)."),
    "limits": ("Two words of prose. What the others say is not in this unit (data: it appears to introduce the views from "
               "card 70 onward); no question asks which statements belong to them."),
    "explain_hi": ("यह दो शब्दों की गद्य-पंक्ति है: ‘दूसरे तो कहते हैं’। "
                   "‘अन्ये’ पुंलिंग प्रथमा बहुवचन है: दूसरे लोग। "
                   "‘आहुः’ √अह् का लिट् (परोक्ष भूत) रूप है, पर अर्थ वर्तमान का है: वे कहते हैं। "
                   "‘त्वाहुः’ में तु + आहुः है: उ के बाद आ आने पर उ व् बनता है (उ + आ → वा)। "
                   "डेटा के अनुसार यह कार्ड ७० से आगे दूसरे आचार्यों के मत का परिचय देती दिखती है।"),
    "hook": "अन्ये त्वाहुः: अब दूसरों का मत।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 69, what does अन्ये mean?",
            ("others", "अन्ये = others (m. nom. pl.)."),
            [("these ones", "'These' would be इमे or एते."),
             ("all men", "'All' would be सर्वे."),
             ("the two", "'The two' would be उभौ or द्वौ.")],
            "अन्ये त्वाहुः = others, however, say.",
            "अन्य = other."),
        order(1, "Put the parts of unit 69, split, in the printed order.",
              ["अन्ये", "तु", "आहुः"],
              "अन्ये (others) → तु (however) → आहुः (they say).",
              "अन्ये → तु → आहुः."),
        fill(2, "In unit 69 the word meaning 'they say' is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("आहुः", "āhuḥ", "ahuh", "aahuh"),
             "आहुः = they say; joined with तु as त्वाहुः.",
             "आहुः is a perfect form of √अह् used with present sense: they say.",
             "आहुः = they say."),
        mcq("discriminate", 3, "Which split of त्वाहुः in unit 69 is right?",
            ("तु + आहुः", "उ + आ → वा: तु + आहुः → त्वाहुः."),
            [("ति + आहुः", "इ + आ would give या: त्याहुः."),
             ("तो + आहुः", "ओ + आ would give अवा: तवाहुः."),
             ("तु + अहुः", "उ + अ would give व with a short अ: त्वहुः.")],
            "तु (however) + आहुः (they say).",
            "उ + आ → वा."),
        mcq("apply", 4, "What does the data say of the form आहुः?",
            ("Perfect form with a present sense", "Right: gram 3 pl. pf. √अह्, with present sense: they say."),
            [("Future form: 'they will say'", "The data labels it perfect, not future."),
             ("An optative form: 'they should say'", "The data labels it perfect, not optative."),
             ("Imperative: 'let them say'", "The data labels it perfect, not imperative.")],
            "आहुः: perfect in form, present in sense.",
            "आहुः = they say."),
        mcq("transfer", 5, "By तु + आहुः → त्वाहुः, how is रामः + तु + आगच्छति (but Rāma comes) joined in a new example?",
            ("रामस्त्वागच्छति", "रामः + तु → रामस्तु; तु + आ → त्वा: रामस्त्वागच्छति."),
            [("रामस्तागच्छति", "The उ of तु cannot vanish; before आ it becomes व्."),
             ("रामस्तोगच्छति", "उ + आ does not give ओ."),
             ("रामस्तूगच्छति", "उ + आ does not give ऊ.")],
            "रामस्त्वागच्छति, like अन्ये त्वाहुः.",
            "उ + आ → वा.",
            teaches="A final उ before a different vowel becomes व्: तु + आहुः → त्वाहुः, तु + आगच्छति → त्वागच्छति."),
    ],
}

# ---------------------------------------------------------------- unit 70
AUTHORED["70"] = {
    "title": "मांसादीनां पंचानमपि",
    "question": "From what does unit 70 say the viśalyaghna (ones) come?",
    "rule": ("Viśalyaghna (ones; usual sense: those that kill when the dart is removed) through the coming together "
             "(समवायात्) of even the five, flesh and the rest (मांसादीनाम्), greatly increased (विवृद्धानाम्)."),
    "limits": ("No verb; the noun of विशल्यघ्नानि is unstated. The five are not named. विवृद्धानाम् may go with the five "
               "or with समवाय: no question rests on it. पंचानम् is printed for पञ्चानाम् (possible). 'Killing when the dart "
               "is removed' is the usual sense, not spelled out here."),
    "explain_hi": ("डेटा के अनुसार यह कार्ड ६९ में बताए ‘दूसरों’ का पहला कथन लगता है। "
                   "इसमें विशल्यघ्न (प्रचलित अर्थ: वे जो शल्य निकालने पर मारते हैं; यह इकाई स्वयं नहीं कहती) को मांस आदि पाँचों के, अत्यन्त बढ़े हुओं के, समवाय यानी मेल से जोड़ा गया है। "
                   "पाँचों के नाम यहाँ नहीं दिए; केवल ‘मांस आदि’ कहा है। "
                   "कोई क्रिया नहीं, और ‘विशल्यघ्नानि’ नपुंसक बहुवचन किसी अनकही संज्ञा के लिए है; ‘विवृद्धानाम्’ पाँचों का विशेषण भी हो सकता है और समवाय से भी जुड़ सकता है। "
                   "‘समवायाद्विशल्य’ में घोष व्यंजन व से पहले त् द् बना है।"),
    "hook": "मांस आदि पाँच, बढ़े और मिले: विशल्यघ्न।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 70, what does मांसादि (māṃsa-ādi) mean?",
            ("flesh and the rest", "मांस-आदि = flesh and the rest (the others not named)."),
            [("flesh alone", "आदि (and the rest) adds the others."),
             ("blood and the rest", "मांस is flesh, not blood (रक्त)."),
             ("bone and the rest", "मांस is flesh, not bone (अस्थि).")],
            "मांसादीनाम् = of flesh and the rest.",
            "X-आदि = X and the rest."),
        order(1, "Put the words of unit 70 in the printed order.",
              ["मांसादीनां", "पंचानमपि", "विवृद्धानां", "समवायाद्", "विशल्यघ्नानि"],
              "Of flesh and the rest; of even the five; greatly increased; from the coming together; viśalyaghna (ones).",
              "मांसादीनां → पंचानमपि → विवृद्धानां → समवायाद् → विशल्यघ्नानि."),
        match(2, "Match each word of unit 70 to its meaning.",
              [["मांस", "flesh"], ["पञ्च", "five"], ["विवृद्ध", "greatly increased"],
               ["समवाय", "coming together, combination"],
               ["विशल्यघ्न", "killing when the dart is removed (usual sense)"]],
              "Flesh and the rest, five, greatly increased, their coming together: viśalyaghna.",
              "मांस, पञ्च, विवृद्ध, समवाय, विशल्यघ्न.", role="extend",
              teaches="समवाय = coming together; समवायात् (ablative) = from, through the coming together."),
        mcq("discriminate", 3, "By unit 70, which is true of the five?",
            ("Only the first, flesh, is named", "Right: मांस-आदि names flesh; the others are 'the rest'."),
            [("All five are named one by one", "Only मांस (flesh) is printed; the rest are आदि."),
             ("They are the five kinds of marma by effect", "Flesh is no kind by effect; the kinds by effect are not meant."),
             ("They are five marmas of the leg", "No marma name is printed in unit 70.")],
            "The five: flesh and the rest; only flesh is named.",
            "X-आदि names only the first."),
        mcq("apply", 4, "Why is समवायात् printed समवायाद् before विशल्यघ्नानि?",
            ("त् before a voiced sound becomes द्", "Right: व is voiced: समवायात् + वि → समवायाद्वि."),
            [("त् before every consonant becomes द्", "Not before a voiceless one: before स, क, प it stays त्."),
             ("त् before व becomes न्", "त् becomes न् only (optionally) before a nasal; व is no nasal."),
             ("द् marks the plural ablative", "समवायात् is singular; the द् is a sandhi change.")],
            "समवायात् + विशल्यघ्नानि → समवायाद्विशल्यघ्नानि.",
            "त् + voiced sound → द्."),
        mcq("transfer", 5, "By समवायात् + विशल्यघ्नानि, how is वृक्षात् + वानरः (a monkey from the tree) joined in a new example?",
            ("वृक्षाद्वानरः", "त् before the voiced व becomes द्."),
            [("वृक्षान्वानरः", "न् comes (optionally) before a nasal; व is no nasal."),
             ("वृक्षाच्वानरः", "च् comes before च/छ or श, not before व."),
             ("वृक्षोवानरः", "The त् does not turn into ओ.")],
            "वृक्षात् + वानरः = वृक्षाद्वानरः, like समवायाद्विशल्यघ्नानि.",
            "त् + voiced sound → द्.",
            teaches="A final त् before a voiced sound becomes द्: समवायात् + विशल्यघ्नानि → समवायाद्विशल्यघ्नानि."),
    ],
}

# ---------------------------------------------------------------- unit 71
AUTHORED["71"] = {
    "title": "एकैकहीनानामल्पानां च",
    "question": "What can be read with certainty in unit 71?",
    "rule": ("With no verb: of those reduced by one each (एकैकहीन) and of the small ones (अल्प), in order (क्रमात्), the "
             "other (ones) (इतराणि); 'by nature alone' (स्वभावत एव); 'and others say' (चान्ये वदंति). Which clause "
             "स्वभावत एव belongs to is open."),
    "limits": ("Low confidence. What is reduced is not named (perhaps the five of card 70; the unit does not say). "
               "स्वभावतः एव may go with इतराणि or with चान्ये वदन्ति: no question rests on that join or on what the 'other "
               "(ones)' are; questions ask word meanings, sandhi and order."),
    "explain_hi": ("यह इकाई भी बिना क्रिया की है और इसका अर्थ निश्चित नहीं (विश्वास निम्न)। "
                   "पहले भाग में ‘एक-एक से घटे हुए’ और ‘अल्प’ के क्रम से ‘इतर’ (अन्य) कहे गए हैं; किसमें से घटे, यह नहीं बताया (सम्भवतः कार्ड ७० के पाँच)। "
                   "फिर ‘चान्ये वदंति’: और दूसरे लोग कहते हैं; ‘स्वभावत एव’ (स्वभाव से ही) इसी कथन का भाग है या ‘इतराणि’ से जुड़ता है, यह खुला है। "
                   "सन्धियाँ साफ़ हैं: एक + एक → एकैक (अ + ए → ऐ), च + अन्ये → चान्ये (अ + अ → आ), स्वभावतः + एव → स्वभावत एव। "
                   "इसलिए प्रश्न शब्दार्थ, सन्धि और शब्द-क्रम पर हैं।"),
    "hook": "एक-एक घटे, अल्प, क्रम से, इतर; स्वभावत एव; और दूसरे कहते हैं।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In चान्ये वदंति of unit 71, what does वदन्ति mean?",
            ("they say", "वदन्ति = they say (3 pl. pres. √वद्)."),
            [("he says", "'He says' would be वदति (singular)."),
             ("they said", "'They said' would be a past form, e.g. अवदन्."),
             ("we say", "'We say' would be वदामः.")],
            "चान्ये वदंति = and others say.",
            "वदन्ति = they say."),
        order(1, "Put the printed words of unit 71 in order.",
              ["एकैकहीनानामल्पानां", "च", "क्रमादितराणिस्वभावतएव", "चान्ये", "वदंति"],
              "Of those reduced by one each and the small; and; in order the others, by nature alone; and others; say.",
              "एकैकहीनानामल्पानां → च → क्रमादितराणिस्वभावतएव → चान्ये → वदंति."),
        match(2, "Match each sure word of unit 71 to its meaning.",
              [["एकैक", "one each, one by one"], ["हीन", "reduced, lacking"], ["अल्प", "small, few"],
               ["क्रमात्", "in order"], ["स्वभावतः", "by nature"]],
              "एकैक = one each; हीन = reduced; अल्प = small; क्रमात् = in order; स्वभावतः = by nature.",
              "एकैक, हीन, अल्प, क्रमात्, स्वभावतः.", role="extend",
              teaches="एकैक (एक + एक) = one each; एकैकहीन = reduced by one each."),
        mcq("discriminate", 3, "Which split of चान्ये in unit 71 is right?",
            ("च + अन्ये", "अ + अ → आ: च + अन्ये → चान्ये."),
            [("चा + न्ये", "Neither चा nor न्ये is a word here."),
             ("च + आन्ये", "आन्ये is not a word; अन्ये means others."),
             ("चः + अन्ये", "च has no visarga; अः + अ would give ओऽ.")],
            "च (and) + अन्ये (others).",
            "अ + अ → आ."),
        mcq("apply", 4, "Why is क्रमात् printed क्रमाद् before इतराणि in unit 71?",
            ("त् before a vowel becomes द्", "Right: इ is a vowel: क्रमात् + इतराणि → क्रमादितराणि."),
            [("त् before every sound becomes द्", "Not before a voiceless consonant: before स, क, प it stays त्."),
             ("त् before इ becomes न्", "त् becomes न् only (optionally) before a nasal; इ is a vowel."),
             ("द् is the ending of the ablative", "The ablative ends in -आत्; the द् is a sandhi change.")],
            "क्रमात् + इतराणि → क्रमादितराणि.",
            "त् + vowel → द्."),
        mcq("transfer", 5, "By एक + एक → एकैक, how is तत्र + एव (there itself) joined in a new example?",
            ("तत्रैव", "अ + ए → ऐ: तत्र + एव → तत्रैव."),
            [("तत्रेव", "अ + ए gives ऐ, not ए."),
             ("तत्रयेव", "No य् is added between अ and ए."),
             ("तत्रौव", "ऐ, not औ: औ comes from अ + ओ.")],
            "तत्र + एव = तत्रैव, like एक + एक = एकैक.",
            "अ + ए → ऐ.",
            teaches="अ + ए → ऐ: एक + एक → एकैक, तत्र + एव → तत्रैव."),
    ],
}

# ---------------------------------------------------------------- unit 72
AUTHORED["72"] = {
    "title": "प्रतिनियतकर्माणि",
    "question": "What comparison does unit 72 give, and what does it say of cutting off the hands and feet?",
    "rule": ("Each with its own fixed function (प्रतिनियतकर्माणि), like the unions of the candra, sūrya and ayaskānta "
             "stones with water, fire and iron; likewise, when hands and feet, though having many marmas, are cut off: by "
             "nature itself, no death."),
    "limits": ("Which stone goes with water, fire or iron is not stated (the order makes a pairing natural): no question "
               "rests on the pairing. Candra and sūrya stones: probably moonstone and sunstone (probable; identity "
               "disputed); ayaskānta = lodestone (standard). No verb for न मृत्युः. Data: appears to continue cards 70-71."),
    "explain_hi": ("यह तुलना की इकाई है: हर एक का अपना नियत कर्म होता है, जैसे चन्द्र और सूर्य पत्थर (सम्भवतः चन्द्रकान्त और सूर्यकान्त; पहचान विवादित) "
                   "तथा अयस्कान्त यानी चुम्बक पत्थर (मानक) का जल, अग्नि और लोहे से मेल। "
                   "कौन पत्थर किससे जुड़ता है, यह क्रम से स्वाभाविक लगता है पर छपा नहीं। "
                   "फिर वही बात शरीर पर: हाथ-पैर में बहुत मर्म हैं, फिर भी उनके कट जाने पर स्वभाव से ही मृत्यु नहीं। "
                   "‘छिन्नेषु … पाणिपादेषु’ सति-सप्तमी है, और ‘न मृत्युः’ के साथ कोई क्रिया नहीं। "
                   "‘बहुमर्मस्वपि’ में बहुमर्मसु + अपि है (उ + अ → व)।"),
    "hook": "पत्थरों का अपना कर्म; हाथ-पैर कटें, फिर भी स्वभाव से मृत्यु नहीं।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 72, what follows by nature when the hands and feet are cut off?",
            ("No death", "स्वभावत एव न मृत्युः: by nature itself, no death."),
            [("Death at once", "The unit says न मृत्युः: no death."),
             ("Death after an interval", "The unit says न मृत्युः: no death."),
             ("Death from loss of blood", "The unit says no death; no cause of death is given.")],
            "छिन्नेषु … पाणिपादेषु स्वभावत एव न मृत्युः.",
            "न मृत्युः = no death."),
        order(1, "Put the parts of unit 72 in the printed order.",
              ["प्रतिनियतकर्माणि", "चंद्रसूर्यायस्कंतोपलानामिवांबुवन्हिलोहसंश्लेषाः", "तथा च",
               "छिन्नेषु बहुमर्मस्वपि पाणिपादेषु", "स्वभावत एव न मृत्युः"],
              "Fixed functions; like the stones' unions with water, fire, iron; likewise; when hands and feet are cut off; no death.",
              "Example first (stones), then the body (hands and feet)."),
        match(2, "Match each word of unit 72 to its meaning.",
              [["प्रतिनियतकर्मन्", "each with its own fixed function"], ["अयस्कान्त", "lodestone (standard)"],
               ["संश्लेष", "union, clinging"], ["छिन्न", "cut off"], ["पाणिपाद", "hands and feet"]],
              "Each has its fixed function, like the lodestone's union with iron; hands and feet cut off: no death.",
              "प्रतिनियतकर्मन्, अयस्कान्त, संश्लेष, छिन्न, पाणिपाद.", role="extend",
              teaches="प्रतिनियत = fixed for each one: प्रतिनियतकर्मन् = each having its own fixed function."),
        mcq("discriminate", 3, "Which rendering of छिन्नेषु बहुमर्मस्वपि पाणिपादेषु is right?",
            ("When the hands and feet, though having many marmas, are cut off",
             "Right: बहु = many, छिन्न = cut off, पाणिपाद = hands and feet."),
            [("When the hands and feet, though having few marmas, are cut off", "बहु means many, not few."),
             ("When the hands and feet, though having many marmas, are pierced", "छिन्न means cut off, not pierced."),
             ("When the trunk, though having many marmas, is cut off", "पाणिपादेषु names the hands and feet.")],
            "A locative absolute: when the hands and feet, having many marmas, are cut off.",
            "छिन्नेषु … पाणिपादेषु = when hands and feet are cut off."),
        multi("apply", 4, "Which are named in unit 72 as what the stones unite with?",
              [("रक्त: blood", "रक्त is not printed in unit 72."),
               ("अम्बु: water", "Right: अम्बु is printed in the compound."),
               ("वन्हि: fire", "Right: printed वन्हि, an older spelling of वह्नि."),
               ("वायु: wind", "वायु is not printed in unit 72."),
               ("लोह: iron", "Right: लोह is printed in the compound.")],
              [1, 2, 4],
              "अम्बु-वन्हि-लोह-संश्लेषाः: unions with water, fire and iron.",
              "Water, fire, iron."),
        mcq("transfer", 5, "By बहुमर्मसु + अपि → बहुमर्मस्वपि, how is वनेषु + अपि (even in the forests) joined in a new example?",
            ("वनेष्वपि", "उ + अ → व: वनेषु + अपि → वनेष्वपि."),
            [("वनेषूपि", "उ + अ does not give ऊ."),
             ("वनेषोपि", "उ + अ does not give ओ."),
             ("वनेषापि", "The उ cannot vanish; it becomes व्.")],
            "वनेषु + अपि = वनेष्वपि, like बहुमर्मस्वपि.",
            "उ + अ → व.",
            teaches="A final उ before a different vowel becomes व्: बहुमर्मसु + अपि → बहुमर्मस्वपि."),
    ],
}

# ---------------------------------------------------------------- unit 73
AUTHORED["73"] = {
    "title": "अपरे पुनरत्रापि हेतुमाहुः",
    "question": "What does unit 73 say the other authorities state?",
    "rule": ("'Others again state a reason here also': अपरे (others), पुनः (again), अत्र (here), अपि (also), हेतुम् "
             "(a reason, object), आहुः (they say)."),
    "limits": ("The reason itself is not in this unit (data: appears to introduce card 74). No question asks what the "
               "reason is or where it is given."),
    "explain_hi": ("यह एक और मत का परिचय है: ‘दूसरे फिर यहाँ भी कारण बताते हैं’। "
                   "‘अपरे’ = दूसरे लोग, ‘हेतुम्’ = कारण (द्वितीया, आहुः का कर्म), ‘आहुः’ = कहते हैं। "
                   "कारण स्वयं इस इकाई में नहीं है; डेटा के अनुसार वह कार्ड ७४ में आता दिखता है। "
                   "सन्धि: पुनः (मूल रूप पुनर्) + अत्र → पुनरत्र; अत्र + अपि → अत्रापि (अ + अ → आ); हेतुम् + आहुः → हेतुमाहुः।"),
    "hook": "अपरे … हेतुमाहुः: अब कारण।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 73, what does हेतु mean?",
            ("reason, cause", "हेतु = reason, cause; हेतुम् is its accusative."),
            [("remedy, cure", "A remedy would be चिकित्सा or औषध."),
             ("place, region", "A place would be देश or स्थान."),
             ("time, season", "Time would be काल.")],
            "हेतुमाहुः = they state a reason.",
            "हेतु = reason."),
        order(1, "Put the printed words of unit 73 in order.",
              ["अपरे", "पुनरत्रापि", "हेतुमाहुः"],
              "Others; again here also; state a reason.",
              "अपरे → पुनरत्रापि → हेतुमाहुः."),
        match(2, "Match each word of unit 73 to its meaning.",
              [["अपरे", "others"], ["पुनः", "again"], ["अत्र", "here, in this matter"], ["अपि", "also"],
               ["हेतुम्", "a reason (object)"]],
              "अपरे = others; पुनः = again; अत्र = here; अपि = also; हेतुम् = a reason.",
              "अपरे, पुनः, अत्र, अपि, हेतुम्.", role="extend",
              teaches="हेतुम् is accusative: the object of आहुः, 'they state a reason'."),
        mcq("discriminate", 3, "Which split of पुनरत्रापि in unit 73 is right?",
            ("पुनः + अत्र + अपि", "पुनर् before a vowel shows र्; अ + अ → आ."),
            [("पुनः + अत्रा + अपि", "अत्रा is not a word; the word is अत्र."),
             ("पुन + रत्र + अपि", "Neither पुन nor रत्र is a word here."),
             ("पुनः + त्र + आपि", "Neither त्र nor आपि is a word here.")],
            "पुनः (again) + अत्र (here) + अपि (also).",
            "पुनर् + vowel → पुनर्; अ + अ → आ."),
        multi("apply", 4, "Which statements fit unit 73?",
              [("It names the reason itself", "Only हेतुम्, 'a reason', is said; no reason is named."),
               ("Its verb आहुः means 'they say'", "Right: आहुः = they say."),
               ("पुनः means 'never'", "पुनः means again."),
               ("हेतुम् is the object of आहुः", "Right: हेतुम् is accusative."),
               ("It has no verb at all", "आहुः is its verb.")],
              [1, 3],
              "They (others) say (आहुः) a reason (हेतुम्).",
              "अपरे … हेतुम् आहुः."),
        mcq("transfer", 5, "By पुनः (पुनर्) + अत्र → पुनरत्र, how is अन्तः (अन्तर्) + अत्र (inside here) joined in a new example?",
            ("अन्तरत्र", "अन्तः has an original र्, which shows before a vowel: अन्तरत्र."),
            [("अन्तोऽत्र", "ओऽ comes from a visarga that stands for स्; अन्तः stands for अन्तर्."),
             ("अन्तत्र", "The र् and the अ cannot both vanish."),
             ("अन्तस्त्र", "स् comes before त, not before a vowel.")],
            "अन्तः + अत्र = अन्तरत्र, like पुनः + अत्र = पुनरत्र.",
            "Original र् + vowel → र्.",
            teaches="Words with an original र् (पुनर्, अन्तर्, प्रातर्) show र् before a vowel even after अ: पुनः + अत्र → पुनरत्र, अन्तः + अत्र → अन्तरत्र."),
    ],
}

# ---------------------------------------------------------------- unit 74
AUTHORED["74"] = {
    "title": "पाणिपादच्छेदे हि सिराः",
    "question": "By unit 74, why does one live when hands and feet are cut off, but die when a marma is pierced?",
    "rule": ("On cutting off hands and feet the sirās (vessels; probably veins) contract, so little blood flows: life. On "
             "piercing a marma, from excessive flow of blood and from abnormality of vāyu (wind): death."),
    "limits": ("जीवितम् and मरणम् have no verb. सिरा = vessel; 'veins' is probable only. Whether vāyu means the doṣa Vāta "
               "is not stated. The printed अल्पास्रक् and अतिरक्तस्रुतिंतो are read by possible corrections; questions use "
               "only the sense 'flow of blood'. Data: appears to complete the reason announced in card 73."),
    "explain_hi": ("यह इकाई कारण देती है और दो स्थितियों की तुलना करती है। "
                   "हाथ-पैर कटने पर सिराएँ (वाहिकाएँ; सम्भवतः शिराएँ) सिकुड़ जाती हैं, इसलिए रक्त थोड़ा बहता है: जीवन। "
                   "पर मर्म के बिंधने पर रक्त के अत्यधिक बहने से और वायु की विकृति से: मरण। "
                   "‘वायु’ से दोष वात अभिप्रेत है या नहीं, यह नहीं कहा गया। "
                   "‘ततोऽल्प’ में ततः + अल्प है: अः + अ → ओऽ। ‘जीवितम्’ और ‘मरणम्’ के साथ कोई क्रिया नहीं।"),
    "hook": "सिराएँ सिकुड़ीं: जीवन; रक्त बहुत बहा और वायु बिगड़ी: मरण।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 74, what happens to the sirās (vessels) when hands and feet are cut off?",
            ("They contract", "सिराः सङ्कोचम् आयान्ति: the sirās contract."),
            [("They burst open", "The unit says they contract."),
             ("They dry up", "The unit says they contract, not that they dry."),
             ("They fill with wind", "The unit says they contract; vāyu is named only for the marma.")],
            "सिराः संकोचमायांति: the sirās contract.",
            "सङ्कोच = contraction."),
        order(1, "Put the parts of unit 74 in the printed order.",
              ["पाणिपादच्छेदे हि", "सिराः संकोचमायांति", "ततोऽल्पास्रक्प्रस्रुतेर्जीवितं", "मर्मव्यधे",
               "त्वतिरक्तस्रुतिंतो वायुवैकृतेन च मरणं"],
              "Cutting of hands and feet; sirās contract; hence little blood flows: life; piercing of a marma; much blood and vāyu: death.",
              "Limb cut → contraction → life; marma pierced → death."),
        match(2, "Match each word of unit 74 to its meaning.",
              [["सङ्कोच", "contraction"], ["अल्प", "little, slight"], ["प्रस्रुति", "flowing out"],
               ["व्यध", "piercing"], ["वैकृत", "abnormality"]],
              "Contraction, slight flowing out of blood: life; piercing, abnormality of vāyu: death.",
              "सङ्कोच, अल्प, प्रस्रुति, व्यध, वैकृत.", role="extend",
              teaches="अल्प (little) ⇄ अति (excessive): in unit 74 slight flow of blood goes with life; excessive flow, with abnormal vāyu, with death."),
        mcq("discriminate", 3, "Which rendering of the second half of unit 74 is right?",
            ("On piercing a marma, death from excess flow of blood and abnormal vāyu",
             "Right: अतिरक्तस्रुति = excess flow of blood; वायुवैकृत = abnormality of vāyu; मरणम् = death."),
            [("On piercing a marma, life from excess flow of blood and abnormal vāyu", "The second half ends in मरणम्, death."),
             ("On piercing a marma, death from slight flow of blood and abnormal vāyu", "अति means excessive, not slight."),
             ("On piercing a marma, death from contraction of sirās and abnormal vāyu",
              "Contraction belongs to the cut limb, not to the pierced marma.")],
            "मर्मव्यधे … अतिरक्तस्रुतितो वायुवैकृतेन च मरणम्.",
            "Marma pierced: much blood + abnormal vāyu → death."),
        mcq("apply", 4, "By unit 74, why does one live after hands and feet are cut off?",
            ("The sirās contract, so little blood flows", "Right: सङ्कोचम् आयान्ति, ततः अल्प-असृक्-प्रस्रुतेः जीवितम्."),
            [("The sirās widen, so the blood flows freely", "They contract; the flow is slight."),
             ("Vāyu becomes abnormal and holds the blood", "Abnormal vāyu is named as a cause of death."),
             ("Much blood flows out and cleans the wound", "Excess flow is named as a cause of death.")],
            "Contraction → slight flow of blood → life.",
            "Little blood lost → life."),
        mcq("transfer", 5, "By ततः + अल्प → ततोऽल्प, how is देवः + अत्र (the god here) joined in a new example?",
            ("देवोऽत्र", "अः + अ → ओऽ: देवः + अत्र → देवोऽत्र."),
            [("देवात्र", "अः + अ does not give आ."),
             ("देवरत्र", "र् comes after vowels other than अ/आ."),
             ("देव अत्र", "अः → अ only before vowels other than अ.")],
            "देवः + अत्र = देवोऽत्र, like ततः + अल्प = ततोऽल्प.",
            "अः + अ → ओऽ.",
            teaches="अः before अ becomes ओ and the अ is dropped (marked ऽ): ततः + अल्प → ततोऽल्प."),
    ],
}

# ---------------------------------------------------------------- unit 75
AUTHORED["75"] = {
    "title": "तस्मान्मर्माभिहतस्य",
    "question": "By unit 75, what is to be done with the limb of one struck on a marma, and where?",
    "rule": ("Therefore (तस्मात्), of one struck on a marma (मर्माभिहतस्य), that limb (तदङ्गम्) should be cut off "
             "(छेदनीयम्) quickly (आशु) at the place of a joint (सन्धिदेशात्)."),
    "limits": ("The text's own instruction; nothing is added about how, for which marma, or with what result. "
               "सन्धिदेशात् (ablative) is rendered 'at the place of a joint'. Data: appears to follow card 74 as its "
               "conclusion; no question rests on that link."),
    "explain_hi": ("डेटा के अनुसार यह इकाई पिछली बात का निष्कर्ष लगती है: ‘तस्मात्’ यानी इसलिए। "
                   "जिसके मर्म पर चोट लगी हो, उसका वह अंग शीघ्र सन्धि के स्थान पर काट देना चाहिए; यह पाठ का अपना कथन है, इसमें कोई और विधि या परिणाम नहीं जोड़ा गया। "
                   "‘छेदनीयम्’ अनीय प्रत्यय (कृत्य) का रूप है: काटा जाना चाहिए। "
                   "सन्धि: तस्मात् + मर्म → तस्मान्मर्म (म से पहले त् → न्, वैकल्पिक; द् भी सही), तत् + अङ्गम् → तदङ्गम् (स्वर से पहले त् → द्), "
                   "सन्धिदेशात् + छेदनीयम् → सन्धिदेशाच्छेदनीयम् (छ से पहले त् → च्)।"),
    "hook": "मर्म पर चोट: वह अंग शीघ्र, सन्धि पर, काटना।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 75, where should the struck limb be cut off?",
            ("At the place of a joint", "सन्धिदेशात्: at the place of a joint."),
            [("At the marma itself", "The unit names the place of a joint, not the marma."),
             ("In the middle of the bone", "The unit names a joint, not a bone."),
             ("Below the wound itself", "The unit names a joint, not the wound.")],
            "तदङ्गम् आशु सन्धिदेशात् छेदनीयम्.",
            "सन्धि = joint."),
        order(1, "Put the words of unit 75, split, in the printed order.",
              ["तस्मात्", "मर्माभिहतस्य", "तदङ्गम्", "आशु", "सन्धिदेशात्", "छेदनीयम्"],
              "Therefore; of one struck on a marma; that limb; quickly; at the place of a joint; should be cut off.",
              "तस्मात् → मर्माभिहतस्य → तदङ्गम् → आशु → सन्धिदेशात् → छेदनीयम्."),
        match(2, "Match each word of unit 75 to its meaning.",
              [["तस्मात्", "therefore"], ["अभिहत", "struck"], ["अङ्ग", "limb"], ["आशु", "quickly"],
               ["सन्धि", "joint"]],
              "Therefore, that struck limb, quickly, at a joint, should be cut off.",
              "तस्मात्, अभिहत, अङ्ग, आशु, सन्धि.", role="extend",
              teaches="मर्माभिहत (मर्म + अभिहत) = struck on a marma; the genitive मर्माभिहतस्य = of one struck on a marma."),
        mcq("discriminate", 3, "What kind of form is छेदनीयम् in unit 75?",
            ("A gerundive: it should be cut off", "Right: gram: gerundive √छिद्, 'to be cut off'."),
            [("A past participle: it was cut off", "The past participle is छिन्न (as in card 72)."),
             ("A present verb: he cuts it off", "A present verb would be छिनत्ति."),
             ("A gerund: having cut it off", "A gerund would be छित्त्वा.")],
            "छेदनीयम् = (it) should be cut off.",
            "-अनीय = should be done."),
        mcq("apply", 4, "Which split of संधिदेशाच्छेदनीयं in unit 75 is right?",
            ("सन्धिदेशात् + छेदनीयम्", "त् before छ becomes च्: -देशात् + छेदनीयम् → -देशाच्छेदनीयम्."),
            [("सन्धिदेशः + छेदनीयम्", "Visarga before छ would give श्छ: सन्धिदेशश्छेदनीयम्."),
             ("सन्धिदेशात् + शेदनीयम्", "शेदनीयम् is not a word; the word is छेदनीयम्."),
             ("सन्धिदेशाम् + छेदनीयम्", "म् before छ would be written ं: सन्धिदेशां छेदनीयम्.")],
            "सन्धिदेशात् (at the place of a joint) + छेदनीयम् (to be cut off).",
            "त् + छ → च्छ."),
        mcq("transfer", 5, "By छेदनीयम् (should be cut off), what does पठनीयम् mean in a new example?",
            ("It should be read", "-अनीय makes a gerundive: पठनीयम् = (it) should be read."),
            [("It was read", "That would be a past form, पठितम्."),
             ("Having read it", "That would be a gerund, पठित्वा."),
             ("It is being read now", "That would be a present passive, पठ्यते.")],
            "पठनीयम् = should be read, like छेदनीयम् = should be cut off.",
            "-अनीय = should be done.",
            teaches="The suffix -अनीय makes a gerundive, 'should be done': छेदनीयम् = should be cut off, पठनीयम् = should be read."),
    ],
}

# ---------------------------------------------------------------- unit 76
AUTHORED["76"] = {
    "title": "अतिहतानां तु मर्मणां",
    "question": "What can be read with certainty in the obscure unit 76?",
    "rule": ("Of marmas severely struck (अतिहतानाम्), each according to its own (यथास्वम्), the action (कर्म): each "
             "preceding one (पूर्वं पूर्वम्); of those struck (हतानाम्), only the latter (उत्तरम् एव). ईषदंते is unclear."),
    "limits": ("Obscure, low confidence, no verb. What the preceding and latter items are is not stated; ईषदंते may be "
               "ईषत् + अन्ते or a damaged form. No question rests on the sense of the whole, on ईषदंते, or on what "
               "'preceding' and 'latter' refer to. Data: appears to continue card 75."),
    "explain_hi": ("यह अस्पष्ट इकाई है (विश्वास निम्न) और इसमें कोई क्रिया नहीं। "
                   "डेटा का सीधा पाठ: अत्यन्त चोट खाए मर्मों का, अपने-अपने अनुसार, कर्म पूर्व-पूर्व वाला; और चोट खाए हुओं का केवल बाद वाला। "
                   "‘पूर्व’ और ‘उत्तर’ किन बातों के लिए हैं, यह इस इकाई में नहीं बताया। "
                   "‘ईषदंते’ स्पष्ट नहीं: ईषत् + अन्ते (थोड़ा, अन्त में) हो सकता है या बिगड़ा रूप। "
                   "‘पूर्वं पूर्वं’ की आवृत्ति वीप्सा है: हर पिछला। इसलिए प्रश्न केवल शब्दार्थ, आवृत्ति और शब्द-क्रम पर हैं।"),
    "hook": "अतिहत: पूर्व-पूर्व; हत: केवल उत्तर।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 76, what does अतिहत mean?",
            ("severely struck", "अति (very much) + हत (struck)."),
            [("lightly struck", "अति means very much, not lightly."),
             ("struck long ago", "अति adds degree, not time."),
             ("struck once only", "अति adds degree, not a count.")],
            "अतिहतानाम् = of the severely struck (marmas).",
            "अति = very much."),
        order(1, "Put the parts of unit 76 in the printed order.",
              ["अतिहतानां तु मर्मणां", "यथास्वं", "पूर्वं पूर्वं च कर्म", "ईषदंते वा", "हतानामुत्तरमेव"],
              "Of severely struck marmas; each by its own; each preceding action; or (unclear); of the struck, only the latter.",
              "अतिहतानां … → यथास्वं → पूर्वं पूर्वं च कर्म → ईषदंते वा → हतानामुत्तरमेव."),
        match(2, "Match each sure word of unit 76 to its meaning.",
              [["अति", "very much"], ["मर्मणाम्", "of the marmas"], ["यथास्वम्", "each according to its own"],
               ["उत्तरम्", "the latter"], ["एव", "only"]],
              "अति = very much; मर्मणाम् = of the marmas; यथास्वम् = each by its own; उत्तरम् = the latter; एव = only.",
              "अति, मर्मणाम्, यथास्वम्, उत्तरम्, एव.", role="extend",
              teaches="यथास्वम् (यथा + स्वम्) = each according to its own."),
        mcq("discriminate", 3, "What does the repeated पूर्वं पूर्वं express in unit 76?",
            ("Each preceding one", "Right: a distributive repetition: each preceding (item)."),
            [("The very first one only", "A repeated word distributes ('each'); it does not single out one."),
             ("Both before and after", "उत्तरम् (the latter) is a separate word; पूर्वं पूर्वं is one sense."),
             ("Long ago, in the past", "Here पूर्वम् means the preceding (item), not a time.")],
            "पूर्वं पूर्वं = each preceding one.",
            "Repeated word = each."),
        multi("apply", 4, "Which statements fit unit 76 by the data?",
              [("अति means 'lightly'", "अति means very much."),
               ("No verb is printed or supplied", "Right: the unit is verbless."),
               ("It is a metrical verse line", "type: prose."),
               ("Its confidence is high", "The data gives low confidence."),
               ("यथास्वम् means 'each according to its own'", "Right: यथा + स्वम्.")],
              [1, 4],
              "Verbless, obscure; ईषदंते unclear; the items are not named.",
              "Obscure prose: ask only the sure words."),
        mcq("transfer", 5, "By पूर्वं पूर्वं (each preceding), what does गृहे गृहे mean in a new example?",
            ("In each house", "A repeated word distributes: in each house, house after house."),
            [("In two houses", "The repetition means 'each', not 'two'."),
             ("In a big house", "The repetition means 'each', not size."),
             ("In no house", "There is no न; the repetition means 'each'.")],
            "गृहे गृहे = in each house, like पूर्वं पूर्वं = each preceding.",
            "Repeated word = each.",
            teaches="A word said twice means 'each, one after another': पूर्वं पूर्वम् = each preceding, गृहे गृहे = in each house."),
    ],
}

# ---------------------------------------------------------------- unit 77
AUTHORED["77"] = {
    "title": "पुनश्च पंचधा भिद्यते",
    "question": "What does unit 77 announce?",
    "rule": ("'And again, (it) is divided fivefold': पुनः च (and again), पञ्चधा (in five ways), भिद्यते (is divided, "
             "passive). The subject is not printed; from the chapter, the marmas."),
    "limits": ("The subject is not printed (data: the marmas). Data: appears to introduce the division by measure in "
               "cards 78 to 82; no question asks what the five groups are. Card 59 opens with the same words for another "
               "fivefold division."),
    "explain_hi": ("यह छोटी गद्य-पंक्ति एक और पाँच-प्रकार के विभाजन की घोषणा है: ‘और फिर पाँच प्रकार से विभाजित किया जाता है’। "
                   "कर्ता छपा नहीं; डेटा के अनुसार अध्याय का विषय, यानी मर्म। "
                   "‘भिद्यते’ कर्मवाच्य (√भिद्) है, और ‘पञ्चधा’ में -धा प्रत्यय ‘प्रकार से’ बताता है। "
                   "डेटा के अनुसार आगे कार्ड ७८ से ८२ में यह विभाजन माप के अनुसार दिया गया लगता है; कार्ड ५९ भी इन्हीं शब्दों ‘पुनश्च पंचधा’ से दूसरा विभाजन खोलता है। "
                   "सन्धि: पुनः + च → पुनश्च (च से पहले विसर्ग → श्)।"),
    "hook": "पुनश्च पंचधा: फिर पाँच भाग।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 77, what does पञ्चधा mean?",
            ("in five ways", "-धा = in ... ways: पञ्चधा = fivefold."),
            [("for five days", "Days would be दिन or अहन्; -धा means 'ways'."),
             ("the fifth one", "The fifth would be पञ्चम."),
             ("fifty times", "Fifty is पञ्चाशत्; -धा means 'ways'.")],
            "पंचधा भिद्यते = is divided in five ways.",
            "-धा = in ... ways."),
        order(1, "Put the printed words of unit 77 in order.",
              ["पुनश्च", "पंचधा", "भिद्यते"],
              "And again; fivefold; is divided.",
              "पुनश्च → पंचधा → भिद्यते."),
        fill(2, "In unit 77 the verb meaning 'is divided' is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("भिद्यते", "bhidyate"),
             "भिद्यते = is divided (3 sg. passive of √भिद्).",
             "भिद्यते is the passive of √भिद्, labelled so in the data: is divided.",
             "भिद्यते = is divided."),
        mcq("discriminate", 3, "Which split of पुनश्च in unit 77 is right?",
            ("पुनः + च", "Visarga before च becomes श्: पुनः + च → पुनश्च."),
            [("पुन + श्च", "Neither पुन nor श्च is a word."),
             ("पुनः + श्च", "श्च is not a word; the word is च."),
             ("पुनः + अश्च", "अश्च is not a word, and पुनः + अ would give पुनर.")],
            "पुनः (again) + च (and).",
            "ः + च → श्च."),
        mcq("apply", 4, "Why is the visarga of पुनः printed श् before च?",
            ("Visarga before च becomes श्", "Right: before च/छ the visarga becomes श्."),
            [("Visarga before any voiceless consonant becomes श्", "Not every one: before त it becomes स्."),
             ("Visarga before a voiced consonant becomes श्", "च is voiceless; before a voiced sound पुनः shows र्."),
             ("श् is the last letter of the word पुन", "The word is पुनः (पुनर्); there is no word पुन.")],
            "पुनः + च → पुनश्च.",
            "ः + च → श्च."),
        mcq("transfer", 5, "By पुनः + च → पुनश्च, how is अश्वः + च (and the horse) joined in a new example?",
            ("अश्वश्च", "Visarga before च becomes श्."),
            [("अश्वोच", "ओ comes before a voiced consonant; च is voiceless."),
             ("अश्वर्च", "र् comes after vowels other than अ/आ."),
             ("अश्वाच", "The visarga does not lengthen the अ.")],
            "अश्वः + च = अश्वश्च, like पुनः + च = पुनश्च.",
            "ः + च → श्च.",
            teaches="A visarga before च (or छ) becomes श्: पुनः + च → पुनश्च, अश्वः + च → अश्वश्च."),
    ],
}

# ---------------------------------------------------------------- unit 78
AUTHORED["78"] = {
    "title": "तद्यथा",
    "question": "What does the formula तद्यथा of unit 78 do?",
    "rule": "तद्यथा (तत् + यथा) = 'namely': a formula that opens a list. तत् before the voiced य becomes तद्.",
    "limits": "One word. Data: appears to introduce the list of cards 79 to 82; no question asks which list follows.",
    "explain_hi": ("यह एक शब्द की परिचय-पंक्ति है: ‘वह इस प्रकार’, यानी ‘जैसे कि’। "
                   "‘तद्यथा’ सूची या उदाहरण खोलने का सामान्य सूत्र है। "
                   "सन्धि: तत् + यथा → तद्यथा, क्योंकि घोष व्यंजन य से पहले त् द् बनता है। "
                   "डेटा के अनुसार आगे कार्ड ७९ से ८२ की सूची आती दिखती है।"),
    "hook": "तद्यथा: अब सूची।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What does तद्यथा mean in unit 78?",
            ("namely, as follows", "तत् + यथा = 'that, as': namely."),
            [("therefore, for that reason", "That would be तस्मात् or अतः."),
             ("but, however", "That would be तु."),
             ("and again", "That would be पुनश्च.")],
            "तद्यथा = namely.",
            "तद्यथा opens a list."),
        match(1, "Match each word to its meaning (तत् and यथा are joined in unit 78).",
              [["तत्", "that"], ["यथा", "as"], ["तथा", "likewise, so"], ["च", "and"]],
              "तत् = that; यथा = as; तथा = likewise; च = and.",
              "तत्, यथा, तथा, च."),
        fill(2, "In unit 78 the second word of the formula, meaning 'as', is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("यथा", "yathā", "yatha"),
             "तद्यथा = तत् + यथा; यथा = as.",
             "यथा = as; with तत् it makes the formula 'namely'.",
             "यथा = as."),
        mcq("discriminate", 3, "Which split of तद्यथा in unit 78 is right?",
            ("तत् + यथा", "त् before the voiced य becomes द्."),
            [("तदा + यथा", "तदा + यथा would be written तदा यथा."),
             ("तत् + अथा", "तत् + अथा would give तदथा; अथा is not a word."),
             ("तद्य + था", "Neither तद्य nor था is a word here.")],
            "तत् (that) + यथा (as).",
            "त् + voiced sound → द्."),
        mcq("apply", 4, "Which is true of तद्यथा by the data?",
            ("A formula that opens a list", "Right: an introductory formula (tad yathā)."),
            [("A verb meaning 'he divides'", "It is तत् + यथा; there is no verb."),
             ("A marma named in the list", "It is a formula, not a marma name."),
             ("A damaged word of this print", "Confidence is high; no flag is given.")],
            "तद्यथा: an introductory formula.",
            "तद्यथा = namely."),
        mcq("transfer", 5, "By तत् + यथा → तद्यथा, how is एतत् + वनम् (this forest) joined in a new example?",
            ("एतद्वनम्", "त् before the voiced व becomes द्."),
            [("एतन्वनम्", "न् comes (optionally) before a nasal; व is no nasal."),
             ("एतच्वनम्", "च् comes before च/छ or श, not before व."),
             ("एतस्वनम्", "त् does not become स्.")],
            "एतत् + वनम् = एतद्वनम्, like तत् + यथा = तद्यथा.",
            "त् + voiced sound → द्.",
            teaches="A final त् before a voiced sound becomes द्: तत् + यथा → तद्यथा, एतत् + वनम् → एतद्वनम्."),
    ],
}

# ---------------------------------------------------------------- unit 79
AUTHORED["79"] = {
    "title": "ऊर्व्यः कूर्चशिरांसि",
    "question": "Which marmas does unit 79 group as twelve, and by what measure?",
    "rule": ("Ūrvī (plural), kūrcaśiras (plural), the two viṭapa and the two kakṣādhara: twelve (द्वादश), measured by "
             "one's own aṅgula, the person's own finger-breadth (स्वाङ्गुलोन्मितानि)."),
    "limits": ("No verb; 'marma' is not printed. विटपे and कक्षाधरे are read as duals (probable; they could be locatives). "
               "The count of each within the twelve is not given; no question rests on it. No number stands before "
               "स्वाङ्गुल: no question asks how many finger-breadths."),
    "explain_hi": ("ये नाम मर्मों के हैं, जो अध्याय का विषय है; इकाई में ‘मर्म’ शब्द नहीं छपा और कोई क्रिया नहीं। "
                   "ऊर्वी (बहुवचन), कूर्चशिरस् (बहुवचन), दो विटप और दो कक्षाधर: ये बारह ‘स्वाङ्गुलोन्मित’ हैं, यानी व्यक्ति के अपने अंगुल से नापे हुए। "
                   "अंगुल से पहले कोई संख्या नहीं छपी, और बारह में से हर एक की संख्या नहीं दी गई। "
                   "‘विटपे’ और ‘कक्षाधरे’ को द्विवचन पढ़ा गया है (सम्भावित; सप्तमी भी हो सकते हैं)। "
                   "सन्धि: स्व + अङ्गुल → स्वाङ्गुल (अ + अ → आ), अङ्गुल + उन्मित → अङ्गुलोन्मित (अ + उ → ओ)।"),
    "hook": "ऊर्वी, कूर्चशिर, विटप, कक्षाधर: बारह, अपने अंगुल से।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 79, how many marmas are measured by one's own aṅgula?",
            ("Twelve", "द्वादश = twelve."),
            [("Ten", "Ten would be दश; the unit prints द्वादश."),
             ("Twenty", "Twenty would be विंशतिः; the unit prints द्वादश."),
             ("Eight", "Eight would be अष्ट; the unit prints द्वादश.")],
            "द्वादश स्वांगुलोन्मितानि: twelve, measured by one's own aṅgula.",
            "द्वादश = twelve."),
        order(1, "Put the parts of unit 79 in the printed order.",
              ["ऊर्व्यः", "कूर्चशिरांसि", "विटपे", "कक्षाधरे च", "द्वादश स्वांगुलोन्मितानि"],
              "Ūrvī; kūrcaśiras; the two viṭapa; and the two kakṣādhara; twelve, measured by one's own aṅgula.",
              "ऊर्व्यः → कूर्चशिरांसि → विटपे → कक्षाधरे च → द्वादश स्वांगुलोन्मितानि."),
        match(2, "Match each word of unit 79 to its meaning.",
              [["कूर्चशिरस्", "'tuft-head' (literal sense)"], ["कक्षाधर", "'armpit-holder' (literal sense)"],
               ["द्वादश", "twelve"], ["स्वाङ्गुल", "one's own finger-breadth"], ["उन्मित", "measured"]],
              "The names have literal senses; twelve of them are measured by one's own finger-breadth.",
              "कूर्चशिरस्, कक्षाधर, द्वादश, स्वाङ्गुल, उन्मित.", role="extend",
              teaches="स्वाङ्गुल = the person's own aṅgula (finger-breadth): the measure is taken from one's own body."),
        mcq("discriminate", 3, "Which split of स्वांगुलोन्मितानि in unit 79 is right?",
            ("स्व + अङ्गुल + उन्मितानि", "अ + अ → आ (स्वाङ्गुल); अ + उ → ओ (अङ्गुलोन्मित)."),
            [("सु + अङ्गुल + उन्मितानि", "सु + अ would give स्व with a short अ: स्वङ्गुल, not the printed स्वां."),
             ("स्व + अङ्गुलः + मितानि", "अः + म would give ओ with no न्: स्वाङ्गुलो मितानि."),
             ("स्वा + अङ्गुलो + न्मितानि", "Neither स्वा nor न्मितानि is a word here.")],
            "स्व (own) + अङ्गुल (finger-breadth) + उन्मितानि (measured).",
            "अ + अ → आ; अ + उ → ओ."),
        multi("apply", 4, "Which are named in unit 79 among the twelve?",
              [("ऊर्वी", "Right: printed ऊर्व्यः."),
               ("गुल्फ", "Gulpha is in card 80, of two aṅgulas."),
               ("विटप", "Right: printed विटपे."),
               ("नाभि", "Nābhi is in card 81, of a palm's measure."),
               ("कक्षाधर", "Right: printed कक्षाधरे.")],
              [0, 2, 4],
              "ऊर्व्यः, कूर्चशिरांसि, विटपे, कक्षाधरे: twelve.",
              "Ūrvī, kūrcaśiras, viṭapa, kakṣādhara."),
        mcq("transfer", 5, "By अङ्गुल + उन्मित → अङ्गुलोन्मित, how is सूर्य + उदयः (sunrise) joined in a new example?",
            ("सूर्योदयः", "अ + उ → ओ: सूर्य + उदयः → सूर्योदयः."),
            [("सूर्यौदयः", "औ comes from अ + ओ or औ, not from अ + उ."),
             ("सूर्युदयः", "The अ cannot vanish before उ."),
             ("सूर्यादयः", "अ + उ does not give आ.")],
            "सूर्य + उदयः = सूर्योदयः, like अङ्गुल + उन्मित = अङ्गुलोन्मित.",
            "अ + उ → ओ.",
            teaches="अ + उ → ओ: अङ्गुल + उन्मित → अङ्गुलोन्मित, सूर्य + उदयः → सूर्योदयः."),
    ],
}

# ---------------------------------------------------------------- unit 80
AUTHORED["80"] = {
    "title": "गुल्फौ मणिबंधौ स्तनमूले",
    "question": "Which marmas does unit 80 give as of two finger-breadths, and which as of three?",
    "rule": ("Two gulpha (ankle), two maṇibandha (wrist), two stanamūla (base of the breast): six, of two aṅgulas "
             "(द्व्यङ्गुलानि). Two jānu (knee), two kūrpara (elbow): four, of three aṅgulas (त्र्यङ्गुलानि)."),
    "limits": ("Two printed lines, no verb. स्तनमूले is read as a dual (it could be a locative singular). चषट् is printed "
               "run together (च षट्). The body-part meanings are standard; the measures are the text's own."),
    "explain_hi": ("इस इकाई की दो छपी पंक्तियाँ दो माप-समूह देती हैं। "
                   "पहली: दो गुल्फ (टखने), दो मणिबन्ध (कलाई) और दो स्तनमूल (स्तन का आधार), ये छह दो अंगुल के। "
                   "दूसरी: दो जानु (घुटने) और दो कूर्पर (कोहनी), ये चार तीन अंगुल के। "
                   "‘स्तनमूले’ को द्विवचन पढ़ा गया है (सप्तमी एकवचन भी सम्भव); ‘चषट्’ छपाई में जुड़ा है: च षट्। "
                   "सन्धि: द्वि + अङ्गुल → द्व्यङ्गुल, त्रि + अङ्गुल → त्र्यङ्गुल (इ + अ → य)।"),
    "hook": "टखना, कलाई, स्तनमूल: दो अंगुल; घुटना, कोहनी: तीन अंगुल।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 80, what is the measure of the two jānu (knee) marmas?",
            ("Three finger-breadths", "जानुनी कूर्परे च चत्वारि त्र्यंगुलानि: of three aṅgulas."),
            [("Two finger-breadths", "Two aṅgulas is the measure of gulpha, maṇibandha and stanamūla."),
             ("Four finger-breadths", "चत्वारि (four) is the count of these marmas, not their measure."),
             ("The breadth of one palm", "The palm is not the measure given in unit 80.")],
            "Jānu and kūrpara: four, of three aṅgulas.",
            "त्र्यङ्गुल = of three aṅgulas."),
        order(1, "Put the parts of unit 80 in the printed order.",
              ["गुल्फौ", "मणिबंधौ", "स्तनमूले", "चषट् द्व्यंगुलानि", "जानुनी कूर्परे च", "चत्वारि त्र्यंगुलानि"],
              "Ankles, wrists, bases of the breast: six of two aṅgulas; knees and elbows: four of three aṅgulas.",
              "गुल्फौ → मणिबंधौ → स्तनमूले → चषट् द्व्यंगुलानि → जानुनी कूर्परे च → चत्वारि त्र्यंगुलानि."),
        match(2, "Match each marma name of unit 80 to the body part it names (standard).",
              [["गुल्फ", "ankle"], ["मणिबन्ध", "wrist"], ["स्तनमूल", "base of the breast"], ["जानु", "knee"],
               ["कूर्पर", "elbow"]],
              "Gulpha = ankle; maṇibandha = wrist; stanamūla = base of the breast; jānu = knee; kūrpara = elbow.",
              "गुल्फ, मणिबन्ध, स्तनमूल, जानु, कूर्पर.", role="extend",
              teaches="These marma names are also names of body parts (standard): gulpha ankle, maṇibandha wrist, jānu knee, kūrpara elbow."),
        mcq("discriminate", 3, "Which marmas of unit 80 measure three finger-breadths?",
            ("jānu and kūrpara", "Right: जानुनी कूर्परे च … त्र्यंगुलानि."),
            [("gulpha and maṇibandha", "These are of two aṅgulas."),
             ("maṇibandha and stanamūla", "These are of two aṅgulas."),
             ("gulpha and jānu", "Gulpha is of two aṅgulas; only jānu is of three.")],
            "Two aṅgulas: gulpha, maṇibandha, stanamūla. Three aṅgulas: jānu, kūrpara.",
            "Line 1: two aṅgulas; line 2: three aṅgulas."),
        mcq("apply", 4, "Which split of द्व्यंगुलानि in unit 80 is right?",
            ("द्वि + अङ्गुलानि", "इ + अ → य: द्वि + अङ्गुलानि → द्व्यङ्गुलानि."),
            [("द्व + यङ्गुलानि", "Neither द्व nor यङ्गुलानि is a word."),
             ("द्वे + अङ्गुलानि", "ए + अ would give एऽ: द्वेऽङ्गुलानि."),
             ("द्वौ + अङ्गुलानि", "औ + अ would give आव: द्वावङ्गुलानि.")],
            "द्वि (two) + अङ्गुलानि (finger-breadths).",
            "इ + अ → य."),
        mcq("transfer", 5, "By द्वि + अङ्गुल → द्व्यङ्गुल, how is इति + अपि (thus too) joined in a new example?",
            ("इत्यपि", "इ + अ → य: इति + अपि → इत्यपि."),
            [("इत्यापि", "इ + अ gives य with a short अ, not या."),
             ("इतीपि", "इ + अ does not give ई."),
             ("इतेपि", "इ + अ does not give ए.")],
            "इति + अपि = इत्यपि, like द्वि + अङ्गुल = द्व्यङ्गुल.",
            "इ + अ → य.",
            teaches="A final इ before a different vowel becomes य्: द्वि + अङ्गुल → द्व्यङ्गुल, इति + अपि → इत्यपि."),
    ],
}

# ---------------------------------------------------------------- unit 81
AUTHORED["81"] = {
    "title": "कूर्चा गुदोबस्तिर्नाभिर्हृदयं",
    "question": "Which marmas does unit 81 group as twenty-nine, and by what measure?",
    "rule": ("Kūrca (pl.), guda (anus), basti (bladder), nābhi (navel), hṛdaya (heart), two nīlā, two manyā, mātṛkā, "
             "sīmanta, śṛṅgāṭaka (pl.): twenty-nine (एकोनत्रिंशत्), measured by the palm (पाणितलसंमितानि)."),
    "limits": ("No verb. The count of each within the twenty-nine is not given; no question rests on it. नीले मन्ये are "
               "read as duals. बस्ति here is the bladder (standard), not the enema. सीमन्त and शृङ्गाटक are kept as names; "
               "their literal senses are no claim about the structure."),
    "explain_hi": ("यह एक और माप-समूह है: हथेली (पाणितल) के माप के उनतीस मर्म। "
                   "नाम: कूर्च (बहुवचन), गुद (मलद्वार), बस्ति (मूत्राशय), नाभि, हृदय, दो नीला, दो मन्या, मातृकाएँ, सीमन्त और शृंगाटक; हर एक की संख्या नहीं दी गई। "
                   "‘एकोनत्रिंशत्’ = एक कम तीस, यानी उनतीस (एक + ऊन + त्रिंशत्)। "
                   "सन्धि: कूर्चाः + गुदः → कूर्चा गुदः (आः का विसर्ग घोष से पहले लुप्त), गुदः + बस्तिः → गुदो बस्तिः (अः + घोष व्यंजन → ओ), "
                   "बस्तिः + नाभिः → बस्तिर्नाभिः (इ के बाद विसर्ग + घोष → र्), च + एकोन → चैकोन (अ + ए → ऐ)।"),
    "hook": "कूर्च से शृंगाटक तक: उनतीस, हथेली भर के।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 81, what is the measure of the twenty-nine marmas?",
            ("The palm of the hand", "पाणितलसंमितानि: measured by the palm of the hand."),
            [("One's own finger-breadth", "That is the measure of the twelve in card 79."),
             ("Two finger-breadths", "That is the measure of the six in card 80."),
             ("Three finger-breadths", "That is the measure of the four in card 80.")],
            "एकोनत्रिंशत् पाणितलसंमितानि: twenty-nine, measured by the palm.",
            "पाणितल = palm of the hand."),
        order(1, "Put the parts of unit 81 in the printed order.",
              ["कूर्चा", "गुदोबस्तिर्नाभिर्हृदयं", "नीले मन्ये", "मातृकाः सीमंताः", "शृंगाटकानि",
               "चैकोनत्रिंशत्पाणितलसंमितानि"],
              "Kūrca; guda, basti, nābhi, hṛdaya; nīlā, manyā; mātṛkā, sīmanta; śṛṅgāṭaka; and twenty-nine, palm-measured.",
              "कूर्चा → गुदो… → नीले मन्ये → मातृकाः सीमंताः → शृंगाटकानि → चैकोनत्रिंशत्…"),
        match(2, "Match each marma name of unit 81 to the body part it names (standard).",
              [["गुद", "anus"], ["बस्ति", "bladder"], ["नाभि", "navel"], ["हृदय", "heart"]],
              "Guda = anus; basti = bladder; nābhi = navel; hṛdaya = heart.",
              "गुद, बस्ति, नाभि, हृदय.", role="extend",
              teaches="बस्ति here names the bladder (the body part), not the enema."),
        mcq("discriminate", 3, "What number does एकोनत्रिंशत् give in unit 81?",
            ("Twenty-nine", "एक-ऊन-त्रिंशत् = thirty less one = 29."),
            [("Thirty-one", "Thirty-one would be एकत्रिंशत्; ऊन means 'less'."),
             ("Thirty", "Thirty is त्रिंशत् alone; एकोन takes one away."),
             ("Nineteen", "Nineteen would be एकोनविंशतिः, from विंशतिः (twenty).")],
            "एकोनत्रिंशत् = one less than thirty = twenty-nine.",
            "एकोन- = one less than."),
        mcq("apply", 4, "Why is बस्तिः printed बस्तिर् before नाभिः in unit 81?",
            ("After इ, visarga before a voiced sound → र्", "Right: न is voiced; the vowel before the visarga is इ."),
            [("After any vowel, visarga before a voiced sound → र्", "Not after अ or आ: गुदः gives गुदो, कूर्चाः gives कूर्चा."),
             ("Visarga before न always becomes स्", "स् comes before त/थ; न is voiced."),
             ("र् is part of the word बस्तिर्", "The word is बस्तिः; the र् comes from the visarga.")],
            "बस्तिः + नाभिः → बस्तिर्नाभिः.",
            "इः + voiced sound → इर्."),
        mcq("transfer", 5, "By कूर्चाः + गुदः → कूर्चा गुदः, how is बालाः + गच्छन्ति (the boys go) joined in a new example?",
            ("बाला गच्छन्ति", "आः before a voiced sound loses its visarga."),
            [("बालो गच्छन्ति", "ओ comes from अः, not from आः."),
             ("बालार्गच्छन्ति", "र् comes after vowels other than अ/आ."),
             ("बालास्गच्छन्ति", "स् comes before त/थ; ग is voiced.")],
            "बालाः + गच्छन्ति = बाला गच्छन्ति, like कूर्चाः + गुदः = कूर्चा गुदः.",
            "आः + voiced sound → आ.",
            teaches="आः before a voiced sound drops its visarga: कूर्चाः + गुदः → कूर्चा गुदः, बालाः + गच्छन्ति → बाला गच्छन्ति."),
    ],
}


# ================================================================== NOTES_HI
NOTES_HI = {
    "68": ("गद्य; विश्वास निम्न। पाठ-चिह्न (सम्भव): छपा ‘वलंबत’ कोई क्रिया-रूप नहीं; ‘अवलम्बते’ (सहारा देता है) अनुमानित पाठ, "
           "आरम्भ का अ छूटा और -ते के स्थान पर -त; ‘हत्युक्तं’ में ह को इ की भूल मानकर ‘इत्युक्तं’ पढ़ा गया। ‘प्राणान् अवलम्बते’ की "
           "सन्धि ‘प्राणानवलम्बते’ होती; छपाई में अ का न होना क्षति का संकेत। डेटा: अर्थ छपी पंक्ति ६८ (कार्ड ६५: सोम प्राणों को धारण "
           "करता है) से मिलता है। अनुमानित भाग पर कोई प्रश्न नहीं। सन्धि जाँची: सोमः + तु → सोमस्तु (त से पहले विसर्ग → स्)।"),
    "69": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। ‘आहुः’ लिट् रूप, वर्तमान अर्थ में। समूह-टिप्पणी (डेटा): छपी पंक्ति ७४ से आगे, "
           "यानी कार्ड ७० से आगे के कथनों का परिचय देती दिखती है। सन्धि जाँची: तु + आहुः → त्वाहुः (उ + आ → वा)।"),
    "70": ("गद्य; विश्वास मध्यम। पाठ-चिह्न (सम्भव): छपा ‘पंचानम्’ = पञ्चानाम् (षष्ठी बहुवचन), अन्त का दीर्घ आ छूटा लगता है। "
           "क्रिया नहीं; ‘विशल्यघ्नानि’ अनकही संज्ञा के लिए। पाँचों के नाम नहीं (मांस-आदि)। ‘विवृद्ध’ पाँचों का विशेषण या समवाय से, दोनों "
           "सम्भव; इस पर कोई प्रश्न नहीं। विशल्यघ्न = शल्य निकालने पर मारने वाला (प्रचलित अर्थ; इकाई स्वयं नहीं कहती)। समूह-टिप्पणी: छपी "
           "पंक्ति ७३ (कार्ड ६९) के ‘दूसरों’ का पहला कथन, आगे कार्ड ७१-७२ में। सन्धि जाँची: पञ्चानाम् + अपि → पञ्चानामपि; विवृद्धानाम् + "
           "समवायात् → विवृद्धानां समवायात् (व्यंजन से पहले म् → ं; छपाई जुड़ी); समवायात् + विशल्यघ्नानि → समवायाद्विशल्यघ्नानि (घोष से "
           "पहले त् → द्)।"),
    "71": ("गद्य; विश्वास निम्न; कोई पाठ-चिह्न नहीं, पर जोड़ अनिश्चित: ‘स्वभावतः एव’ ‘इतराणि’ से भी जुड़ सकता है, तब ‘च अन्ये "
           "वदन्ति’ = और दूसरे कहते हैं। क्या घटा है, यह नहीं कहा (सम्भवतः छपी पंक्ति ७४ = कार्ड ७० के पाँच)। ‘इतराणि’ अनकही संज्ञा के "
           "लिए। समूह-टिप्पणी: कार्ड ७० को आगे बढ़ाती दिखती है। सन्धि जाँची: एक + एक → एकैक (अ + ए → ऐ); हीनानाम् + अल्पानाम् → "
           "हीनानामल्पानाम्; क्रमात् + इतराणि → क्रमादितराणि (स्वर से पहले त् → द्); स्वभावतः + एव → स्वभावत एव (अः + अ से भिन्न स्वर → अ); "
           "च + अन्ये → चान्ये (अ + अ → आ)।"),
    "72": ("गद्य; विश्वास मध्यम। पाठ-चिह्न (सम्भव): छपा ‘अयस्कंत’ = अयस्कान्त (दीर्घ आ छूटा); ‘वन्हि’ वह्नि की पुरानी वर्तनी। "
           "पहचान: अयस्कान्त = चुम्बक पत्थर (मानक); चन्द्र और सूर्य पत्थर = सम्भवतः चन्द्रकान्त और सूर्यकान्त (सम्भावित; आधुनिक "
           "moonstone/sunstone भिन्न खनिज हैं, इसलिए पहचान विवादित)। तीन पत्थरों का जल, अग्नि, लोहे से क्रमशः मेल स्वाभाविक है पर छपा "
           "नहीं; इस पर कोई प्रश्न नहीं। ‘छिन्नेषु … पाणिपादेषु’ सति-सप्तमी; ‘न मृत्युः’ बिना क्रिया। समूह-टिप्पणी: छपी पंक्तियाँ ७४-७५ "
           "(कार्ड ७०-७१) को आगे बढ़ाती दिखती है। सन्धि जाँची: उपलानाम् + इव → उपलानामिव; इव + अम्बु → इवाम्बु (अ + अ → आ); बहुमर्मसु + "
           "अपि → बहुमर्मस्वपि (उ + अ → व)।"),
    "73": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। समूह-टिप्पणी (डेटा): छपी पंक्ति ७८, यानी कार्ड ७४ के कारण का परिचय। सन्धि "
           "जाँची: पुनः (मूल रूप पुनर्) + अत्र → पुनरत्र (मूल र् स्वर से पहले बना रहता है); अत्र + अपि → अत्रापि (अ + अ → आ); हेतुम् + आहुः → "
           "हेतुमाहुः।"),
    "74": ("गद्य; विश्वास मध्यम। पाठ-चिह्न (सम्भव): (१) छपा ‘अल्पास्रक्’: समास अल्प-असृक्-प्रस्रुति, ऋ का र बनना छपाई की भूल लगती "
           "है; (२) छपा ‘अतिरक्तस्रुतिंतो’: -तस् वाला पञ्चमी रूप अतिरक्तस्रुतितः, अनुस्वार भटका चिह्न लगता है। अर्थ केवल ‘रक्त के बहने से’ "
           "पर टिका है। सिरा = वाहिका; ‘शिरा (vein)’ केवल सम्भावित। वायु = हवा; दोष वात अभिप्रेत है या नहीं, नहीं कहा। जीवितम्, मरणम् "
           "बिना क्रिया। समूह-टिप्पणी: छपी पंक्ति ७७ (कार्ड ७३) में घोषित कारण पूरा करती दिखती है। सन्धि जाँची: पाणिपाद + छेदे → "
           "पाणिपादच्छेदे (समास में छ से पहले च्, छपा च्छ); सङ्कोचम् + आयान्ति → सङ्कोचमायान्ति; ततः + अल्प → ततोऽल्प (अः + अ → ओऽ); "
           "प्रस्रुतेः + जीवितम् → प्रस्रुतेर्जीवितम् (ए के बाद विसर्ग + घोष → र्); तु + अति → त्वति (उ + अ → व)।"),
    "75": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। ‘सन्धिदेशात्’ पञ्चमी, अनुवाद ‘सन्धि के स्थान पर’। ‘तदङ्गम्’ = वह (चोट खाया) "
           "अंग। समूह-टिप्पणी: छपी पंक्ति ७८ (कार्ड ७४) का निष्कर्ष लगती है। सन्धि जाँची: तस्मात् + मर्म → तस्मान्मर्म (म से पहले त् → न्, "
           "वैकल्पिक; द् भी सही; छपा न्); मर्म + अभिहत → मर्माभिहत (अ + अ → आ); तत् + अङ्गम् → तदङ्गम् (स्वर से पहले त् → द्); अङ्गम् + "
           "आशु → अङ्गमाशु; सन्धिदेशात् + छेदनीयम् → सन्धिदेशाच्छेदनीयम् (छ से पहले त् → च्)।"),
    "76": ("गद्य; विश्वास निम्न; कोई पाठ-चिह्न नहीं, पर अर्थ अस्पष्ट। ‘ईषदंते’ स्पष्ट नहीं: ईषत् + अन्ते या बिगड़ा रूप; दोनों "
           "अनुवादों में अस्पष्ट छोड़ा गया। ‘पूर्व’ और ‘उत्तर’ किन बातों के लिए हैं, नहीं कहा। ‘पूर्वं पूर्वं’ वीप्सा (हर पिछला)। कोई "
           "क्रिया नहीं। समूह-टिप्पणी: छपी पंक्ति ७९ (कार्ड ७५) को आगे बढ़ाती दिखती है। सन्धि जाँची: हतानाम् + उत्तरम् + एव → "
           "हतानामुत्तरमेव; ईषत् + अन्ते → ईषदन्ते (स्वर से पहले त् → द्), यदि यही विभाजन हो।"),
    "77": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। कर्ता छपा नहीं (डेटा: मर्म)। समूह-टिप्पणी: छपी पंक्ति ८२ (कार्ड ७८) और छपी "
           "पंक्तियाँ ८३-८७ (कार्ड ७९-८२, माप के पाँच समूह) का परिचय देती दिखती है। ‘पुनश्च पंचधा’ कार्ड ५९ में भी। सन्धि जाँची: पुनः + "
           "च → पुनश्च (च से पहले विसर्ग → श्)।"),
    "78": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। परिचय-सूत्र ‘तद्यथा’। समूह-टिप्पणी: छपी पंक्तियाँ ८३-८७ (कार्ड ७९-८२) की सूची "
           "खोलती दिखती है। सन्धि जाँची: तत् + यथा → तद्यथा (घोष व्यंजन से पहले त् → द्)।"),
    "79": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। मर्मों के नाम; ‘मर्म’ शब्द और क्रिया छपे नहीं। ‘विटपे’, ‘कक्षाधरे’ द्विवचन "
           "पढ़े गए (सम्भावित; सप्तमी भी सम्भव)। बारह के भीतर की संख्याएँ नहीं दी गईं; बहुवचन ऊर्वी और कूर्चशिरस् चार-चार हों तभी जोड़ "
           "बैठता है, जो पाठ नहीं कहता। ‘स्वाङ्गुल’ से पहले कोई संख्या नहीं। सन्धि जाँची: स्व + अङ्गुल → स्वाङ्गुल (अ + अ → आ); अङ्गुल + "
           "उन्मित → अङ्गुलोन्मित (अ + उ → ओ)।"),
    "80": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। दो छपी पंक्तियाँ ([02.07.84], [02.07.85])। ‘चषट्’ छपाई में जुड़ा (च षट्)। "
           "‘स्तनमूले’ द्विवचन पढ़ा गया (सप्तमी एकवचन भी सम्भव)। द्विवचन अन्त -ई, -े से पढ़े गए। अर्थ मानक: गुल्फ टखना, मणिबन्ध कलाई, "
           "स्तनमूल स्तन का आधार, जानु घुटना, कूर्पर कोहनी। सन्धि जाँची: द्वि + अङ्गुल → द्व्यङ्गुल, त्रि + अङ्गुल → त्र्यङ्गुल (इ + अ → य)।"),
    "81": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। मर्मों के नाम, कुछ अंगों के नाम भी (मानक: गुद मलद्वार, बस्ति मूत्राशय, नाभि, "
           "हृदय)। बस्ति यहाँ अंग है, बस्ति-कर्म नहीं। ‘नीले मन्ये’ द्विवचन पढ़े गए। सीमन्त (‘माँग’) और शृङ्गाटक (‘चौराहा’) केवल नाम; "
           "शब्दार्थ संरचना का दावा नहीं। उनतीस के भीतर की संख्याएँ नहीं दी गईं। सन्धि जाँची: कूर्चाः + गुदः → कूर्चा गुदः (आः का विसर्ग घोष "
           "से पहले लुप्त); गुदः + बस्तिः → गुदो बस्तिः (अः + घोष व्यंजन → ओ); बस्तिः + नाभिः → बस्तिर्नाभिः और नाभिः + हृदयम् → "
           "नाभिर्हृदयम् (इ के बाद विसर्ग + घोष → र्); च + एकोन → चैकोन (अ + ए → ऐ); एक + ऊन → एकोन (अ + ऊ → ओ)।"),
}


# ===================================================================== AIDS
AIDS = {
    "68": {
        "chunks": "सोमस्तु | प्राणान्वलंबतहत्युक्तं",
        "frame": ("पक्का: सोमस्तु (किन्तु सोम) → संदिग्ध: ‘वलंबत’ (अनुमान: अवलम्बते, सहारा देता है) → संदिग्ध: ‘हत्युक्तं’ "
                  "(अनुमान: इत्युक्तम्, ऐसा कहा गया)।"),
        "sandhi": "त से पहले विसर्ग → स्: सोमः + तु → सोमस्तु।",
    },
    "69": {
        "chunks": "अन्ये | त्वाहुः",
        "sandhi": "उ + आ → वा: तु + आहुः → त्वाहुः।",
        "anchors": "अन्ये (दूसरे) + तु (तो) + आहुः (कहते हैं): दूसरे मत का द्वार। (मेरी याद-पद्धति)",
    },
    "70": {
        "chain": {"steps": ["मांसादि: मांस आदि", "पञ्च: पाँचों के भी", "विवृद्ध: अत्यन्त बढ़े हुए", "समवाय: मेल से",
                            "विशल्यघ्न"]},
        "chunks": "मांसादीनां | पंचानमपि | विवृद्धानांसमवायाद्विशल्यघ्नानि",
        "sandhi": "घोष व्यंजन से पहले त् → द्: समवायात् + विशल्यघ्नानि → समवायाद्विशल्यघ्नानि।",
    },
    "71": {
        "chunks": "एकैकहीनानामल्पानां | च | क्रमादितराणिस्वभावतएव | चान्ये | वदंति",
        "frame": ("पक्का: एक-एक से घटे, अल्प, क्रम से, अन्य; और दूसरे कहते हैं → खुला: किससे घटे; ‘स्वभावत एव’ किस भाग से "
                  "जुड़ता है।"),
        "sandhi": ("अ + ए → ऐ: एक + एक → एकैक · अ + अ → आ: च + अन्ये → चान्ये · अः + अ से भिन्न स्वर → अ: स्वभावतः + एव → "
                   "स्वभावत एव · स्वर से पहले त् → द्: क्रमात् + इतराणि → क्रमादितराणि।"),
    },
    "72": {
        "diagram": {"groups": [
            {"label": "उदाहरण: प्रतिनियत कर्म", "items": ["चन्द्र, सूर्य पत्थर (पहचान सम्भावित)", "अयस्कंत (= अयस्कान्त): चुम्बक पत्थर (मानक)",
                                                       "जल, अग्नि, लोहे से मेल"]},
            {"label": "तथा च: शरीर में", "items": ["बहुत मर्मों वाले हाथ-पैर", "कट जाने पर भी", "स्वभाव से ही मृत्यु नहीं"]}]},
        "chunks": ("प्रतिनियतकर्माणि | चंद्रसूर्यायस्कंतोपलानामिवांबुवन्हिलोहसंश्लेषाः | तथा च | छिन्नेषु बहुमर्मस्वपि पाणिपादेषु | "
                   "स्वभावत एव न मृत्युः"),
        "sandhi": "अ + अ → आ: इव + अम्बु → इवाम्बु · उ + अ → व: बहुमर्मसु + अपि → बहुमर्मस्वपि।",
    },
    "73": {
        "chunks": "अपरे | पुनरत्रापि | हेतुमाहुः",
        "sandhi": ("पुनः का मूल र् (पुनर्) स्वर से पहले बना रहता है: पुनः + अत्र → पुनरत्र · अ + अ → आ: अत्र + अपि → अत्रापि · "
                   "म् + स्वर: हेतुम् + आहुः → हेतुमाहुः।"),
    },
    "74": {
        "seesaw": ("हाथ-पैर कटे → सिराएँ सिकुड़ीं → थोड़ा रक्त बहा → जीवन ⇄ मर्म बिंधा → रक्त अत्यधिक बहा + वायु की विकृति → "
                   "मरण।"),
        "chunks": ("पाणिपादच्छेदे हि | सिराः संकोचमायांति | ततोऽल्पास्रक्प्रस्रुतेर्जीवितं | मर्मव्यधे | "
                   "त्वतिरक्तस्रुतिंतो वायुवैकृतेन च मरणं"),
        "sandhi": ("अः + अ → ओऽ: ततः + अल्प → ततोऽल्प · ए के बाद विसर्ग + घोष → र्: प्रस्रुतेः + जीवितम् → प्रस्रुतेर्जीवितम् · "
                   "उ + अ → व: तु + अति → त्वति।"),
    },
    "75": {
        "chain": {"steps": ["तस्मात्: इसलिए", "मर्म पर चोट खाए का", "वह अंग", "आशु: शीघ्र", "सन्धि के स्थान पर",
                            "छेदनीयम्: काटना चाहिए"]},
        "chunks": "तस्मान्मर्माभिहतस्य | तदंगमाशु | संधिदेशाच्छेदनीयं",
        "sandhi": ("म से पहले त् → न्, वैकल्पिक (द् भी सही; छपा न्): तस्मात् + मर्म → तस्मान्मर्म · स्वर से पहले त् → द्: "
                   "तत् + अङ्गम् → तदङ्गम् · छ से पहले त् → च्: सन्धिदेशात् + छेदनीयम् → सन्धिदेशाच्छेदनीयम्।"),
    },
    "76": {
        "chunks": "अतिहतानां तु मर्मणां | यथास्वं | पूर्वं पूर्वं च कर्म | ईषदंते वा | हतानामुत्तरमेव",
        "frame": ("किनका: अतिहत मर्मों का → कैसे: यथास्वम् (अपने-अपने अनुसार) → क्या: पूर्व-पूर्व कर्म → अस्पष्ट: ईषदंते वा → "
                  "हत का: केवल उत्तर।"),
    },
    "77": {
        "chunks": "पुनश्च | पंचधा | भिद्यते",
        "sandhi": "च से पहले विसर्ग → श्: पुनः + च → पुनश्च।",
        "anchors": "‘पुनश्च पंचधा’ कार्ड ५९ में भी: वहाँ एक पाँच-भेद, यहाँ फिर पाँच। (मेरी याद-पद्धति)",
    },
    "78": {
        "sandhi": "घोष व्यंजन य से पहले त् → द्: तत् + यथा → तद्यथा।",
        "anchors": "तद्यथा = ‘जैसे कि’: सूची का द्वार। (मेरी याद-पद्धति)",
    },
    "79": {
        "diagram": {"groups": [
            {"label": "द्वादश: अपने अंगुल से नापे", "items": ["ऊर्व्यः (बहुवचन)", "कूर्चशिरांसि (बहुवचन)",
                                                         "विटपे (द्विवचन, सम्भावित)", "कक्षाधरे (द्विवचन, सम्भावित)"]}]},
        "chunks": "ऊर्व्यः | कूर्चशिरांसि | विटपे | कक्षाधरे च | द्वादश स्वांगुलोन्मितानि",
        "sandhi": "अ + अ → आ: स्व + अङ्गुल → स्वाङ्गुल · अ + उ → ओ: अङ्गुल + उन्मित → अङ्गुलोन्मित।",
    },
    "80": {
        "diagram": {"groups": [
            {"label": "षट्: दो अंगुल के", "items": ["गुल्फौ: दो टखने", "मणिबंधौ: दो कलाई", "स्तनमूले: दो स्तनमूल"]},
            {"label": "चत्वारि: तीन अंगुल के", "items": ["जानुनी: दो घुटने", "कूर्परे: दो कोहनी"]}]},
        "chunks": "गुल्फौ | मणिबंधौ | स्तनमूले | चषट् द्व्यंगुलानि || जानुनी | कूर्परे च | चत्वारि त्र्यंगुलानि",
        "sandhi": "इ + अ → य: द्वि + अङ्गुल → द्व्यङ्गुल, त्रि + अङ्गुल → त्र्यङ्गुल।",
        "pegs": "छोटे जोड़ टखना, कलाई, और साथ में स्तनमूल: दो अंगुल; बड़े जोड़ घुटना, कोहनी: तीन अंगुल। (मेरी याद-पद्धति; पाठ यह कारण नहीं बताता)",
    },
    "81": {
        "diagram": {"groups": [
            {"label": "एकोनत्रिंशत्: हथेली के माप के", "items": ["कूर्चा", "गुदो: मलद्वार", "बस्तिर्: मूत्राशय", "नाभिर्",
                                                              "हृदयं", "नीले", "मन्ये", "मातृकाः", "सीमंताः", "शृंगाटकानि"]}]},
        "chunks": "कूर्चा | गुदोबस्तिर्नाभिर्हृदयं | नीले मन्ये | मातृकाः सीमंताः | शृंगाटकानि | चैकोनत्रिंशत्पाणितलसंमितानि",
        "sandhi": ("आः का विसर्ग घोष से पहले लुप्त: कूर्चाः + गुदः → कूर्चा गुदः · अः + घोष व्यंजन → ओ: गुदः + बस्तिः → गुदो "
                   "बस्तिः · इ के बाद विसर्ग + घोष → र्: बस्तिः + नाभिः → बस्तिर्नाभिः · अ + ए → ऐ: च + एकोन → चैकोन।"),
    },
}


# ============================================================== IMAGE_SPECS
IMAGE_SPECS = {
    ("70", "chain"): {
        "file": "sh7-vishalyaghna-70.svg",
        "alt": ("Chain of unit 70 in printed order: of flesh and the rest; of even the five; greatly increased; from "
                "their coming together; viśalyaghna (ones)."),
        "type": "chain",
        "title": "इकाई ७०: सम्भवतः दूसरों का मत",
        "steps": ["मांसादि: मांस आदि", "पञ्च: पाँचों के भी", "विवृद्ध: अत्यन्त बढ़े हुए", "समवाय: मेल से", "विशल्यघ्न"],
    },
    ("72", "diagram"): {
        "file": "sh7-pratiniyata-72.svg",
        "alt": ("Flowchart of unit 72: each has its own fixed function; example: the candra, sūrya and ayaskānta stones "
                "(candra and sūrya stones probably moonstone and sunstone, probable; ayaskānta lodestone, standard) in "
                "union with water, fire and iron; likewise, hands and feet cut off; by nature, no death."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"प्रत्येक का नियत कर्म\"] --> B[\"उदाहरण: तीन पत्थर\"]\n"
                 "  B --> C[\"चन्द्र, सूर्य पत्थर (पहचान सम्भावित)\"]\n"
                 "  B --> G[\"अयस्कंत: चुम्बक पत्थर\"]\n"
                 "  C --> D[\"जल, अग्नि, लोहे से मेल\"]\n"
                 "  G --> D\n"
                 "  A --> E[\"वैसे ही: बहुत मर्मों वाले हाथ-पैर कटे\"]\n"
                 "  E --> F[\"स्वभाव से मृत्यु नहीं\"]\n"),
    },
    ("74", "seesaw"): {
        "file": "sh7-chheda-vyadha-74.svg",
        "alt": ("Two columns of unit 74: hands and feet cut off: the sirās contract, little blood flows, life; marma "
                "pierced: excessive flow of blood, abnormality of vāyu, death."),
        "type": "split",
        "title": "इकाई ७४: जीवन ⇄ मरण",
        "cols": [["हाथ-पैर कटे", ["सिराएँ सिकुड़ती हैं", "थोड़ा रक्त बहता है", "जीवन"]],
                 ["मर्म बिंधा", ["रक्त अत्यधिक बहता है", "वायु की विकृति", "मरण"]]],
    },
    ("75", "chain"): {
        "file": "sh7-chhedaniya-75.svg",
        "alt": ("Chain of unit 75 in printed order: therefore; of one struck on a marma; that limb; quickly; at the place "
                "of a joint; should be cut off."),
        "type": "chain",
        "title": "इकाई ७५: अंग-छेदन",
        "steps": ["तस्मात्: इसलिए", "मर्म पर चोट खाए का", "वह अंग", "आशु: शीघ्र", "सन्धि के स्थान पर",
                  "छेदनीयम्: काटना चाहिए"],
    },
    ("79", "diagram"): {
        "file": "sh7-svangula-79.svg",
        "alt": ("Table of unit 79 in printed order: ūrvī (plural), kūrcaśiras (plural), viṭapa (dual, probable), "
                "kakṣādhara (dual, probable): twelve, measured by one's own aṅgula."),
        "type": "table",
        "title": "इकाई ७९: बारह, अपने अंगुल से",
        "heads": ["नाम (छपा क्रम)", "वचन"],
        "rows": [["ऊर्व्यः", "बहुवचन"], ["कूर्चशिरांसि", "बहुवचन"], ["विटपे", "द्विवचन (सम्भावित)"],
                 ["कक्षाधरे", "द्विवचन (सम्भावित)"]],
    },
    ("80", "diagram"): {
        "file": "sh7-dvyangula-tryangula-80.svg",
        "alt": ("Table of unit 80: two gulpha (ankles), two maṇibandha (wrists), two stanamūla (bases of the breast): "
                "two aṅgulas; two jānu (knees), two kūrpara (elbows): three aṅgulas."),
        "type": "table",
        "title": "इकाई ८०: छह दो अंगुल के, चार तीन अंगुल के",
        "heads": ["मर्म", "माप"],
        "rows": [["गुल्फौ: दो टखने", "दो अंगुल"], ["मणिबंधौ: दो कलाई", "दो अंगुल"],
                 ["स्तनमूले: दो स्तनमूल", "दो अंगुल"], ["जानुनी: दो घुटने", "तीन अंगुल"],
                 ["कूर्परे: दो कोहनी", "तीन अंगुल"]],
    },
    ("81", "diagram"): {
        "file": "sh7-panitala-81.svg",
        "alt": ("Table of unit 81 in printed order: kūrca, guda (anus), basti (bladder), nābhi (navel), hṛdaya (heart), "
                "nīlā (two), manyā (two), mātṛkā, sīmanta, śṛṅgāṭaka: twenty-nine, measured by the palm."),
        "type": "table",
        "title": "इकाई ८१: उनतीस, हथेली के माप के",
        "heads": ["नाम (छपा रूप)", "अर्थ या वचन"],
        "rows": [["कूर्चा", "नाम, बहुवचन"], ["गुदो", "मलद्वार"], ["बस्तिर्", "मूत्राशय"], ["नाभिर्", "नाभि"],
                 ["हृदयं", "हृदय"], ["नीले", "नाम, दो"], ["मन्ये", "नाम, दो"], ["मातृकाः", "नाम, बहुवचन"],
                 ["सीमंताः", "नाम, बहुवचन"], ["शृंगाटकानि", "नाम, बहुवचन"]],
    },
}
