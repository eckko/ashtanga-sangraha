from helpers import mcq, match, order, fill, multi, accepts


def T(q, teaches):
    q["teaches"] = teaches
    return q


AUTHORED = {}

# ---------------------------------------------------------------- unit 14
AUTHORED["14"] = {
    "title": "वातकफावृतमार्गाणाम्",
    "question": "What does unit 14 say a woman who resorts to Vāta-increasing things may come to show, and what treatment is to be looked to?",
    "rule": ("In a woman who resorts to Vāta-increasing things, something lifeless shows the signs of pregnancy "
             "(गुल्मी भवति, sense undecided); in that case one looks to the treatment of gulma (an abdominal lump)."),
    "limits": ("Low confidence: the syntax is not certain; the unstated subject is taken as the ārtava of unit 11. "
               "The printed अशुकं (possibly अशुक्रम्) and the sense of गुल्मी भवति are undecided, so no question rests on them. "
               "No remedy is named."),
    "explain_hi": ("यह एक लम्बा, ढीला गद्य-वाक्य है और इसकी वाक्य-रचना पक्की नहीं है; अनुवाद छपे क्रम में चलता है। "
                   "जिनके मार्ग वात और कफ से ढके हों, वहाँ (सम्भवतः आर्तव) नहीं बहता; पित्त बढ़ाने वाले उपचारों से वह बहने लगता है। "
                   "वात बढ़ाने वाली चीज़ों का सेवन करती स्त्री में वह जीवरहित होकर भी गर्भ के लक्षण दिखाता है; ‘गुल्मी भवति’ (गुल्म वाला हो जाता है) का अर्थ तय नहीं। "
                   "गुल्म यानी पेट की गाँठ (मानक अर्थ)। ऐसी दशा में गुल्म की चिकित्सा देखनी चाहिए।"),
    "hook": "गर्भ के लक्षण, पर जीव नहीं: गुल्म-चिकित्सा देखो।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In unit 14, what is one told to look to in that case?",
            ("The treatment of gulma", "तत्र गुल्मचिकित्सितम् ईक्षेत: look to the treatment of gulma."),
            [("The treatment of fever", "Fever is not named in this unit."),
             ("The care of a pregnancy", "The thing is जीवरहित, devoid of life, so it is no pregnancy."),
             ("The treatment of cough", "Cough is not named in this unit.")],
            "The unit ends: in that case one should look to the treatment of gulma (an abdominal lump).",
            "गुल्मचिकित्सितम् ईक्षेत = look to the treatment of gulma."),
        order(1, "Put these phrases of unit 14 in their printed order.",
              ["वातकफावृतमार्गाणाम्", "पित्तलैरुपचारैः", "जीवरहितम्", "गर्भलिङ्गानि दर्शयत्", "गुल्मचिकित्सितमीक्षेत"],
              "The line moves from the covered passages, to the Pitta-increasing measures, to the lifeless thing that shows "
              "signs of pregnancy, and ends with the treatment of gulma.",
              "Covered passages → Pitta measures → lifeless → signs of pregnancy → gulma treatment."),
        T(match(2, "Match each word of unit 14 to its meaning on the card.",
                [["वातकफावृतमार्ग", "passages covered by Vāta and Kapha"], ["पित्तल", "Pitta-increasing"],
                 ["जीवरहित", "devoid of life"], ["गर्भलिङ्ग", "signs of pregnancy"], ["ईक्षेत", "should look to"]],
                "These five words carry the sure parts of the long sentence.",
                "आवृत = covered; पित्तल = Pitta-increasing; जीवरहित = lifeless; लिङ्ग = sign; ईक्षेत = should look to.",
                role="extend"),
          "The thing shows the signs of pregnancy yet is devoid of life (जीवरहित)."),
        mcq("discriminate", 3, "Which split of पित्तलैरुपचारैः is right?",
            ("पित्तलैः + उपचारैः", "A visarga after ऐ becomes र् before a vowel: पित्तलैर् + उपचारैः."),
            [("पित्तलै + रुपचारैः", "रुपचारैः is not a word of the card."),
             ("पित्तलैर + उपचारैः", "पित्तलैर is not a full word; the ending is -ऐः."),
             ("पित्तलम् + उपचारैः", "म् before a vowel would give पित्तलमुपचारैः.")],
            "पित्तलैः (by Pitta-increasing) + उपचारैः (by measures).",
            "Visarga after a vowel other than अ/आ → र् before a vowel or voiced sound."),
        multi("apply", 4, "Which two does unit 14 name?",
              [("Vāta-increasing (ones) that a woman resorts to", "Right: वातलान्यासेवमानाया योषितः."),
               ("The signs of pregnancy (गर्भलिङ्गानि)", "Right: गर्भलिङ्गानि दर्शयत्."),
               ("A true embryo that will be born", "जीवरहित denies life, so no true embryo is named."),
               ("Kapha-pacifying measures", "Only Pitta-increasing measures are named.")],
              [0, 1],
              "The unit names a woman who resorts to Vāta-increasing (ones) and the signs of pregnancy.",
              "वातलानि आसेवमानायाः; गर्भलिङ्गानि."),
        T(mcq("transfer", 5, "By the rule of पित्तलैरुपचारैः, how is देवैः + उक्तम् written when joined?",
              ("देवैरुक्तम्", "Visarga after ऐ becomes र् before the vowel उ."),
              [("देवैउक्तम्", "The visarga cannot simply drop before a vowel here."),
               ("देवैोक्तम्", "That is not a possible spelling."),
               ("देवैसुक्तम्", "Visarga becomes स् only before त/थ, not before a vowel.")],
              "पित्तलैः + उपचारैः → पित्तलैरुपचारैः; so देवैः + उक्तम् → देवैरुक्तम्.",
              "Visarga after ऐ + vowel → र् + vowel."),
          "A visarga after ऐ (or any vowel but अ/आ) becomes र् before a vowel."),
    ],
}

# ---------------------------------------------------------------- unit 15
AUTHORED["15"] = {
    "title": "कदाचिद्वा गर्भइव",
    "question": "What does unit 15 say sometimes occurs, and with what does it subside?",
    "rule": "Sometimes vātodara (Vāta-belly, probably abdominal swelling from Vāta) occurs; it subsides with Vāta-pacifying (ones).",
    "limits": ("Low confidence. The printed गर्भइव is read by the card as गर्भा एव (in a pregnant woman indeed); the note leaves "
               "गर्भ एव (the embryo itself) open, so no question rests on it. वातोदर as abdominal distension is a probable "
               "identification. The noun that Vāta-pacifying qualifies is not stated."),
    "explain_hi": ("यह छोटी गद्य-पंक्ति बताती है: कभी वातोदर हो जाता है, यानी सम्भवतः वात से पेट का फूलना। "
                   "छपा ‘गर्भइव’ अस्पष्ट है; कार्ड इसे ‘गर्भा एव’ (गर्भवती स्त्री में भी) पढ़ता है, पर ‘गर्भ एव’ भी सम्भव माना गया है। "
                   "वह वातोदर वात को शान्त करने वालों से शान्त हो जाता है। "
                   "किन वस्तुओं से, यह पंक्ति नहीं बताती; ‘वातौपशमन’ के साथ संज्ञा छोड़ दी गई है।"),
    "hook": "वात से पेट फूला? वात-शामक से शान्त।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 15, with what does the vātodara subside?",
            ("With Vāta-pacifying ones", "वातौपशमनैः उपशाम्यति: it subsides with Vāta-pacifying (ones)."),
            [("With Pitta-increasing measures", "Pitta-increasing measures belong to unit 14."),
             ("With the treatment of gulma", "The gulma treatment is the advice of unit 14."),
             ("With Kapha-increasing foods", "No Kapha remedy is named here.")],
            "That (vātodara) subsides with Vāta-pacifying (ones).",
            "उपशाम्यति = subsides; वातौपशमन = Vāta-pacifying."),
        order(1, "Put these words of unit 15 in their printed order.",
              ["कदाचित्", "वातोदरम्", "भवति", "वातौपशमनैः", "उपशाम्यति"],
              "Sometimes … vātodara occurs; that subsides with Vāta-pacifying (ones).",
              "कदाचित् → वातोदरम् → भवति → वातौपशमनैः → उपशाम्यति."),
        T(match(2, "Match each word of unit 15 to its meaning on the card.",
                [["कदाचित्", "sometimes"], ["वातोदर", "Vāta-belly (probably swelling from Vāta)"],
                 ["औपशमन", "pacifying"], ["उपशाम्यति", "subsides"]],
                "Four words carry the two clauses: what occurs, and how it subsides.",
                "कदाचित्, वातोदर, औपशमन, उपशाम्यति.", role="extend"),
          "वातोदर = वात + उदर: a belly (swelling) from Vāta, a probable identification."),
        mcq("discriminate", 3, "Which split of वातौपशमनैः is right?",
            ("वात + औपशमनैः", "अ + औ gives औ: वात + औपशमनैः → वातौपशमनैः."),
            [("वातो + पशमनैः", "पशमनैः is not a word of the card."),
             ("वात + उपशमनैः", "अ + उ would give ओ: वातोपशमनैः."),
             ("वाता + उपशमनैः", "आ + उ would give ओ, not औ.")],
            "वात (Vāta) + औपशमनैः (by pacifying ones).",
            "अ/आ + औ → औ."),
        multi("apply", 4, "Which does unit 15 state?",
              [("Vātodara sometimes occurs", "Right: कदाचित् … वातोदरं भवति."),
               ("It subsides with Vāta-pacifying (ones)", "Right: वातौपशमनैः उपशाम्यति."),
               ("It needs the treatment of gulma", "That is unit 14's advice for the lifeless thing."),
               ("It is caused by Pitta", "The unit names Vāta, not Pitta.")],
              [0, 1],
              "The unit says vātodara sometimes occurs and subsides with Vāta-pacifying (ones).",
              "कदाचित् वातोदरम्; वातौपशमनैः उपशाम्यति."),
        T(mcq("transfer", 5, "By the rule of वातौपशमन, how is वन + औषधि written when joined?",
              ("वनौषधि", "अ + औ → औ, as in वात + औपशमन."),
              [("वनोषधि", "अ + औ does not give ओ."),
               ("वनवौषधि", "No व् is inserted after अ."),
               ("वनाउषधि", "अ + औ does not split into आ + उ.")],
              "वात + औपशमन → वातौपशमन; so वन + औषधि → वनौषधि.",
              "अ + औ → औ."),
          "अ or आ before औ merges into औ (वृद्धि vowel stays)."),
    ],
}

# ---------------------------------------------------------------- unit 16
AUTHORED["16"] = {
    "title": "तदेव कदाचिदार्तवम्",
    "question": "What does unit 16 say held-back ārtava sometimes does to the belly?",
    "rule": ("That very ārtava, held back by gentle, bulk-promoting (bṛṃhaṇa) diets and regimens, increases the belly, "
             "free of complications, as if it were occupied by an embryo."),
    "limits": ("The grouping of the adjectives is not certain: स्तम्भित is taken with the ārtava and अनुपद्रव with the belly. "
               "The printed वर्द्वयति is read as वर्धयति (a print confusion). The unit names no particular food."),
    "explain_hi": ("वही आर्तव कभी सौम्य और बृंहण (पुष्टि करने वाले) स्वभाव के आहार-विहार से रुक जाता है। "
                   "रुका हुआ आर्तव पेट को बढ़ा देता है, बिना किसी उपद्रव के, मानो उसमें गर्भ बैठा हो। "
                   "‘इव’ यानी ‘मानो’: पेट केवल गर्भ जैसा दिखता है। "
                   "विशेषणों का बँटवारा पक्का नहीं है; छपा ‘वर्द्वयति’ ‘वर्धयति’ पढ़ा गया है।"),
    "hook": "रुका आर्तव, बढ़ा पेट: मानो गर्भ, पर गर्भ नहीं।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 16, how does the belly look when the held-back ārtava increases it?",
            ("As if occupied by an embryo", "गर्भाधिष्ठितम् इव: as if an embryo were in it."),
            [("As if struck by a blow", "No blow is named in the unit."),
             ("As if filled with pus", "Pus is not named in this unit."),
             ("As if swollen from poison", "No poison is named in this unit.")],
            "It increases the belly, free of complications, as if occupied by an embryo.",
            "इव = as if; गर्भाधिष्ठित = occupied by an embryo."),
        order(1, "Put these phrases of unit 16 in their printed order.",
              ["तदेव कदाचिदार्तवम्", "सौम्यैर्बृंहणात्मभिराहारविहारैः", "स्तम्भितम्", "अनुपद्रवमेवोदरम्", "गर्भाधिष्ठितमिव"],
              "Subject, then the cause of holding back, then held back, then the belly, then 'as if occupied by an embryo'.",
              "आर्तव → आहारविहार → स्तम्भित → उदर → गर्भाधिष्ठित इव."),
        T(match(2, "Match each word of unit 16 to its meaning on the card.",
                [["सौम्य", "gentle"], ["बृंहण", "bulk-promoting"], ["आहारविहार", "diets and regimens"],
                 ["स्तम्भित", "held back"], ["अनुपद्रव", "without complications"]],
                "Three words describe the cause (gentle, bulk-promoting diets and regimens); two describe the result.",
                "सौम्य, बृंहण, आहारविहार, स्तम्भित, अनुपद्रव.", role="extend"),
          "बृंहण means bulk-promoting, nourishing: such diets and regimens hold the ārtava back."),
        mcq("discriminate", 3, "In unit 16, what holds the ārtava back?",
            ("Gentle, bulk-promoting diets and regimens", "सौम्यैः बृंहणात्मभिः आहारविहारैः स्तम्भितम्."),
            [("Pitta-increasing measures and remedies", "In unit 14 these make it flow, not stop."),
             ("Vāta-pacifying foods given at night", "Vāta-pacifying (ones) belong to unit 15."),
             ("Contrary measures or pure chance", "Those make the blood flow in unit 18.")],
            "The ārtava is held back by gentle diets and regimens of a bulk-promoting nature.",
            "स्तम्भित by सौम्य बृंहण आहारविहार."),
        mcq("apply", 4, "What does the word इव tell us about the belly in unit 16?",
            ("It only looks occupied by an embryo", "इव = as if: the likeness is in looks only."),
            [("It truly holds a living embryo", "इव marks a likeness, not a fact."),
             ("It holds two embryos at once", "Nothing of the kind is said."),
             ("It shrinks after a few days", "The verb says it grows (वर्धयति).")],
            "गर्भाधिष्ठितम् इव: as if occupied by an embryo, so not truly.",
            "इव = as if, like."),
        T(mcq("transfer", 5, "An invented line reads बालः सिंह इव गर्जति. What does it say?",
              ("The boy roars like a lion", "इव after सिंह = like a lion."),
              [("The lion roars like a boy", "इव follows सिंह, so the lion is the likeness."),
               ("The boy is a lion who roars", "इव makes it a likeness, not an identity."),
               ("The boy roars at a lion", "No 'at' (object) is expressed.")],
              "As गर्भाधिष्ठितम् इव = as if occupied by an embryo, सिंह इव = like a lion.",
              "X इव = like X, as if X."),
          "इव follows the word it compares with: X इव = like X."),
    ],
}

# ---------------------------------------------------------------- unit 17
AUTHORED["17"] = {
    "title": "येन तामगर्भी गर्भिणीमाहुः",
    "question": "What does unit 17 say the deluded do because of that appearance?",
    "rule": "Because of which (the swollen belly of unit 16) the deluded call her, who is not pregnant, pregnant.",
    "limits": ("The printed तामगर्भी is read as ताम् अगर्भिणीम् (a possible loss of letters); no question rests on its form. "
               "येन is taken as 'because of which', pointing back to unit 16."),
    "explain_hi": ("यह पंक्ति पिछली इकाई का परिणाम बताती है। पेट मानो गर्भ से भरा दिखता है, इसी कारण मूढ़ लोग उस अगर्भिणी "
                   "स्त्री को गर्भिणी कह देते हैं। ‘येन’ यानी जिसके कारण, यह इकाई १६ के दिखावे की ओर संकेत करता है। "
                   "छपा ‘तामगर्भी’ सम्भवतः ‘ताम् अगर्भिणीम्’ है, कुछ अक्षर छूटे लगते हैं।"),
    "hook": "पेट बढ़ा देखकर मूढ़ बोले: गर्भिणी! पर है अगर्भिणी।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 17, who call the woman pregnant?",
            ("The deluded (मूढाः)", "मूढाः आहुः: the deluded say so."),
            [("The physicians (वैद्याः)", "No physician is named in this line."),
             ("The midwives (धात्र्यः)", "No midwife is named in this line."),
             ("Her parents (पितरौ)", "No parent is named in this line.")],
            "The deluded call her pregnant though she is not.",
            "मूढाः = the deluded."),
        order(1, "Put the printed words of unit 17 in their order.",
              ["येन", "तामगर्भी", "गर्भिणीमाहुः", "मूढाः"],
              "Because of which, her (not pregnant), pregnant they call, the deluded.",
              "येन → तामगर्भी → गर्भिणीमाहुः → मूढाः."),
        T(match(2, "Match each word of unit 17 to its meaning on the card.",
                [["येन", "because of which"], ["गर्भिणी", "pregnant"], ["आहुः", "they call"], ["मूढाः", "the deluded"]],
                "The four words make the line: because of which the deluded call her pregnant.",
                "येन, गर्भिणी, आहुः, मूढाः.", role="extend"),
          "आहुः is a plural verb: they say, they call; its subject here is मूढाः."),
        mcq("discriminate", 3, "Which split of आहुर्मूढाः is right?",
            ("आहुः + मूढाः", "Visarga after उ becomes र् before the voiced म."),
            [("आहुर + मूढाः", "आहुर is not the verb form; it is आहुः."),
             ("आहु + र्मूढाः", "र्मूढाः is not a word."),
             ("आहुम् + मूढाः", "म् + म would stay म्म, not र्म.")],
            "आहुः (they call) + मूढाः (the deluded).",
            "Visarga after उ → र् before a voiced sound."),
        mcq("apply", 4, "In unit 17, what does येन (because of which) point back to?",
            ("The belly grown as if pregnant", "Unit 16's swollen belly is what misleads them."),
            [("The treatment of gulma", "That is advice in unit 14, not a cause of the mistake."),
             ("The Vāta-pacifying measures", "Those calm the vātodara in unit 15."),
             ("The flow of the blood", "The blood flows later, in unit 18.")],
            "The card takes येन as the appearance of unit 16: the belly grows as if occupied by an embryo.",
            "येन = by which / because of which (unit 16)."),
        T(mcq("transfer", 5, "By the rule of आहुर्मूढाः, how is गुरुः + वदति written when joined?",
              ("गुरुर्वदति", "Visarga after उ → र् before the voiced व."),
              [("गुरुो वदति", "That is not a possible spelling."),
               ("गुरुस्वदति", "Visarga becomes स् only before त/थ."),
               ("गुरु वदति", "The visarga does not drop after उ.")],
              "आहुः + मूढाः → आहुर्मूढाः; so गुरुः + वदति → गुरुर्वदति.",
              "उः + voiced consonant → उर्."),
          "A visarga after उ (or इ, ए ...) becomes र् before a voiced consonant."),
    ],
}

# ---------------------------------------------------------------- unit 18
AUTHORED["18"] = {
    "title": "ततो विपरीतैर्यदृच्छया वा",
    "question": "What do the ignorant say in unit 18 when the blood flows and no embryo's body is seen?",
    "rule": ("Then, when the blood flows through contrary (ones) or by chance, not seeing the body of the embryo, "
             "the ignorant say: carried off by beings (bhūta)."),
    "limits": ("विपरीतैः has no stated noun; it probably means measures opposite to those of unit 16 (not certain). "
               "भूत is kept literal (being, spirit). The unit reports what the ignorant say; it does not agree with it."),
    "explain_hi": ("फिर, विपरीत (उपायों) से या संयोग से, रक्त बहने लगता है। गर्भ का शरीर तो दिखता नहीं, इसलिए अज्ञ लोग कहते हैं: "
                   "‘भूतों ने हर लिया’। ‘विपरीतैः’ की संज्ञा नहीं दी गई; सम्भवतः इकाई १६ के उल्टे उपाय। "
                   "‘प्रवृत्ते रक्ते’ यानी रक्त के बहने पर, यह सप्तमी में कहा गया समय है। "
                   "यह अज्ञों का कथन है; अगली इकाइयाँ इसका खंडन करती हैं।"),
    "hook": "रक्त बहा, शरीर दिखा नहीं, अज्ञ बोले: भूत ले गए!",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 18, what do the ignorant say when they do not see the embryo's body?",
            ("It was carried off by beings", "भूतहृतम् इति अज्ञाः ब्रुवते."),
            [("It was dissolved by Vāta", "The ignorant say nothing of Vāta here."),
             ("It was never there at all", "The ignorant do not say this; they blame beings (भूत)."),
             ("It moved into the belly", "No such claim is made.")],
            "The ignorant say: carried off by beings (bhūta).",
            "भूतहृत = carried off by beings."),
        order(1, "Put these phrases of unit 18 in their printed order.",
              ["ततो विपरीतैर्यदृच्छया वा", "प्रवृत्ते रक्ते", "गर्भशरीरमपश्यन्तः", "भूतहृतमिति", "अज्ञा ब्रुवते"],
              "Cause of the flow, the flow, not seeing the body, the claim, the speakers.",
              "विपरीतैः/यदृच्छया → प्रवृत्ते रक्ते → अपश्यन्तः → भूतहृतम् इति → अज्ञाः ब्रुवते."),
        T(match(2, "Match each word of unit 18 to its meaning on the card.",
                [["यदृच्छया", "by chance"], ["अपश्यन्तः", "not seeing"], ["भूतहृत", "carried off by beings"],
                 ["अज्ञाः", "the ignorant"], ["ब्रुवते", "they say"]],
                "These five words make up the claim and who makes it.",
                "यदृच्छया, अपश्यन्तः, भूतहृत, अज्ञाः, ब्रुवते.", role="extend"),
          "अपश्यन्तः = not seeing (present participle, plural), describing the ignorant."),
        mcq("discriminate", 3, "Which split of भूतहृतमित्यज्ञाः is right?",
            ("भूतहृतम् + इति + अज्ञाः", "म् joins the vowel; इ + अ → य: इत्यज्ञाः."),
            [("भूतहृतम् + इत्य + ज्ञाः", "इत्य and ज्ञाः are not the card's words."),
             ("भूतहृतमि + ति + अज्ञाः", "भूतहृतमि is not a word."),
             ("भूतहृतम् + इति + यज्ञाः", "यज्ञाः would mean sacrifices; the word is अज्ञाः.")],
            "भूतहृतम् (carried off by beings) + इति (thus) + अज्ञाः (the ignorant).",
            "इ + a different vowel → य् + that vowel."),
        multi("apply", 4, "By unit 18, how may the blood come to flow?",
              [("Through contrary (ones)", "Right: विपरीतैः."),
               ("By chance", "Right: यदृच्छया."),
               ("Through Vāta-pacifying (ones)", "Those calm the vātodara in unit 15."),
               ("Through gentle, bulk-promoting diets", "Those held the ārtava back in unit 16.")],
              [0, 1],
              "The blood flows through contrary (ones) or by chance (वा = or).",
              "विपरीतैः यदृच्छया वा."),
        T(mcq("transfer", 5, "Built like प्रवृत्ते रक्ते, what does उदिते सूर्ये mean?",
              ("When the sun has risen", "Two locatives together give the time: when X has happened."),
              [("In the risen sun's light", "The pair gives a time, not a place in the light."),
               ("The sun is going to rise", "The participle उदित is past, not future."),
               ("By means of the rising sun", "That would need an instrumental, not a locative.")],
              "प्रवृत्ते रक्ते = when the blood flows; उदिते सूर्ये = when the sun has risen.",
              "Noun + participle both in the locative = when (that happens)."),
          "A noun and a participle together in the locative tell when something happens."),
    ],
}

# ---------------------------------------------------------------- unit 19
AUTHORED["19"] = {
    "title": "यस्मात्सम्भवत्योजसोऽपहरणम्",
    "question": "What does unit 19 say rakṣas can take away, and what not?",
    "rule": ("The taking away of ojas (vital essence) by rakṣas (demons) can occur, but not of the body, from "
             "undesirability or incapacity."),
    "limits": ("Elliptical: 'taking away' is carried over to 'of the body'. Whose undesirability or incapacity is meant is not "
               "stated, and अशक्तेः rests on a possible restoration of a lost अ; no question rests on it. It continues the "
               "argument of unit 18 (यस्मात् gives the reason)."),
    "explain_hi": ("यहाँ भूत-हरण की बात का खंडन शुरू होता है। ‘यस्मात्’ यानी क्योंकि: राक्षसों द्वारा ओज का अपहरण सम्भव है, "
                   "पर शरीर का नहीं। कारण: अनिष्ट होने से या असमर्थता से; किसकी, यह नहीं कहा गया। "
                   "ओज यानी जीवन-सार (शास्त्रीय शब्द)। ‘अशक्तेः’ का आरम्भिक अ छपाई में छूटा लगता है।"),
    "hook": "राक्षस ओज ले सकते हैं, शरीर नहीं।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 19, what can rakṣas (demons) take away?",
            ("Ojas, the vital essence", "ओजसः अपहरणं रक्षोभिः सम्भवति."),
            [("The whole body of the embryo", "The unit says: not of the body."),
             ("The mother's breast milk", "Breast milk is not named here."),
             ("The father's semen", "Semen is not named in this unit.")],
            "The taking away of ojas by rakṣas occurs, but not of the body.",
            "ओजस् yes; काय (body) no."),
        order(1, "Put these phrases of unit 19 in their printed order.",
              ["यस्मात्", "सम्भवति", "ओजसोऽपहरणम्", "रक्षोभिः", "न तु कायस्य"],
              "Since … occurs … the taking away of ojas … by rakṣas … but not of the body.",
              "यस्मात् → सम्भवति → ओजसः अपहरणम् → रक्षोभिः → न तु कायस्य."),
        T(match(2, "Match each word of unit 19 to its meaning on the card.",
                [["यस्मात्", "since"], ["ओजस्", "vital essence"], ["अपहरण", "taking away"],
                 ["रक्षस्", "demon"], ["काय", "body"]],
                "These five words carry the claim: ojas may be taken by demons, the body not.",
                "यस्मात्, ओजस्, अपहरण, रक्षस्, काय.", role="extend"),
          "यस्मात् = since: the unit gives the reason against the claim of unit 18."),
        mcq("discriminate", 3, "Which split of ओजसोऽपहरणम् is right?",
            ("ओजसः + अपहरणम्", "अः + अ → ओ, and the second अ is shown by ऽ."),
            [("ओजसो + पहरणम्", "पहरणम् is not a word of the card."),
             ("ओजस् + उपहरणम्", "That would give ओज उपहरणम्, and उपहरणम् is not the card's word."),
             ("ओजसा + अपहरणम्", "आ + अ would give ओजसापहरणम्.")],
            "ओजसः (of ojas) + अपहरणम् (taking away) → ओजसोऽपहरणम्.",
            "अः + अ → ओऽ."),
        mcq("apply", 4, "In unit 19, what role does the word यस्मात् play?",
            ("It gives the reason against unit 18", "Since …: it begins the argument against 'carried off by beings'."),
            [("It names the demons who act", "The demons are रक्षोभिः."),
             ("It closes the whole chapter", "The argument goes on in the next units."),
             ("It states the remedy for the loss", "No remedy is given here.")],
            "यस्मात् (since) opens the reason why the body is not carried off.",
            "यस्मात् = since, because."),
        T(mcq("transfer", 5, "By the rule of ओजसोऽपहरणम्, how is रामः + अपि written when joined?",
              ("रामोऽपि", "अः + अ → ओ, and the lost अ is marked ऽ."),
              [("रामापि", "अः + अ does not give आ."),
               ("रामरपि", "र् comes after a vowel other than अ/आ."),
               ("रामः अपि", "The visarga does not stay before अ here.")],
              "ओजसः + अपहरणम् → ओजसोऽपहरणम्; so रामः + अपि → रामोऽपि.",
              "अः + अ → ओऽ."),
          "Final अः before अ becomes ओ and the अ is dropped, written ऽ."),
    ],
}

# ---------------------------------------------------------------- unit 20
AUTHORED["20"] = {
    "title": "इच्छाशक्तयोर्हि",
    "question": "What does the clear second half of unit 20 say is not seen?",
    "rule": ("For there is no perception of the activity of desire and power, and the removal of anyone's body by humans "
             "is not seen."),
    "limits": ("Low confidence. The first clause rests on a print-spacing correction (प्रवृत्तेः उपलब्धिः) and its argument is not "
               "firm, so no question rests on it. It continues unit 19 (हि = for)."),
    "explain_hi": ("यह खंडन आगे बढ़ाती है। पहला भाग छपाई की दूरी सुधारकर पढ़ा गया है: इच्छा और शक्ति की प्रवृत्ति की उपलब्धि नहीं होती; "
                   "यह पाठ पक्का नहीं है। दूसरा भाग स्पष्ट है: किसी के देह का मनुष्यों द्वारा अपहरण नहीं देखा जाता। "
                   "‘हि’ यानी क्योंकि, यह इकाई १९ के तर्क को जोड़ता है।"),
    "hook": "देह-हरण किसी ने देखा? नहीं।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 20, what is not seen?",
            ("The removal of anyone's body by humans", "न च दृश्यते कस्यचिन्मानुषैर्देहापहारः."),
            [("The flow of blood from the woman", "The flow is seen; unit 18 speaks of it."),
             ("The swelling of the woman's belly", "The swelling is seen; unit 16 speaks of it."),
             ("The taking of ojas by rakṣas", "Unit 19 says that can occur.")],
            "The removal of anyone's body by humans is not seen.",
            "देहापहार = removal of the body."),
        order(1, "Put these words of the clear clause of unit 20 in their printed order.",
              ["न च", "दृश्यते", "कस्यचित्", "मानुषैः", "देहापहारः"],
              "And not is seen, of anyone, by humans, removal of the body.",
              "न च → दृश्यते → कस्यचित् → मानुषैः → देहापहारः."),
        T(match(2, "Match each word of unit 20 to its meaning on the card.",
                [["हि", "for"], ["दृश्यते", "is seen"], ["कस्यचित्", "of anyone"], ["मानुषैः", "by humans"],
                 ["देहापहार", "removal of the body"]],
                "These words make the clear part of the unit and link it to unit 19.",
                "हि, दृश्यते, कस्यचित्, मानुषैः, देहापहार.", role="extend"),
          "दृश्यते is passive: is seen; the thing seen (देहापहारः) is in the nominative."),
        mcq("discriminate", 3, "Which split of कस्यचिन्मानुषैः is right?",
            ("कस्यचित् + मानुषैः", "त् before a nasal (म) becomes न्."),
            [("कस्यचिन् + आनुषैः", "आनुषैः is not a word of the card."),
             ("कस्य + चिन्मानुषैः", "चिन्मानुषैः is not a word."),
             ("कस्यचिम् + मानुषैः", "म् + म would give म्म, not न्म.")],
            "कस्यचित् (of anyone) + मानुषैः (by humans).",
            "Final त् + nasal → न् + nasal."),
        multi("apply", 4, "Which are in unit 20 as the card reads it?",
              [("The removal of a body by humans is not seen", "Right: न च दृश्यते … देहापहारः."),
               ("The word हि (for) links it to the reason in unit 19", "Right: हि = for; the card reads this unit as continuing unit 19."),
               ("Demons are often seen carrying bodies away", "The unit says no removal of a body is seen."),
               ("Ojas is taken away by humans", "Unit 19 speaks of rakṣas, not humans, taking ojas.")],
              [0, 1],
              "No removal of anyone's body by humans is seen; हि ties this to unit 19.",
              "हि …; न च दृश्यते देहापहारः."),
        T(mcq("transfer", 5, "By the rule of कस्यचिन्मानुषैः, how is तत् + मात्रम् written when joined?",
              ("तन्मात्रम्", "त् before म becomes न्."),
              [("तण्मात्रम्", "Before म the त् becomes न्, not the retroflex ण्."),
               ("तम्मात्रम्", "त् does not become म्."),
               ("तत्मात्रम्", "In sandhi the त् does not stay before म.")],
              "कस्यचित् + मानुषैः → कस्यचिन्मानुषैः; so तत् + मात्रम् → तन्मात्रम्.",
              "त् + म → न्म."),
          "A final त् before a nasal consonant becomes न्."),
    ],
}

# ---------------------------------------------------------------- unit 21
AUTHORED["21"] = {
    "title": "यदि च दृष्टमपि समुल्लङ्घ्य",
    "question": "What supposition does unit 21 make, and what does it ask?",
    "rule": ("If some, endowed with excessive power, passing even beyond what is seen, proceed to cast off the embryo's body, "
             "then how would they neglect its mothers? (The word प्राप्तविशराः is unclear.)"),
    "limits": ("Low confidence. प्राप्तविशराः is unclear, kept unsplit, and its sense is a conjecture: no question rests on it. "
               "The unit continues the argument of units 19-20; it gives the supposition and the question, nothing more."),
    "explain_hi": ("यह खंडन का अगला तर्क है, ‘यदि … तदा कथम् इव’ के ढाँचे में। यदि कुछ अत्यधिक शक्ति वाले, देखे हुए को भी "
                   "लाँघकर, गर्भ का शरीर फेंकने में लगते हैं, तो वे उसकी माताओं की उपेक्षा कैसे करेंगे? "
                   "बीच का शब्द ‘प्राप्तविशराः’ अस्पष्ट है, उसका अर्थ केवल अनुमान है। "
                   "‘तज्जननीः’ = तत् + जननीः, यानी उसकी माताएँ।"),
    "hook": "यदि शरीर ले जा सकते, तो माता को क्यों छोड़ते?",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In the supposition of unit 21, what do some powerful ones proceed to do?",
            ("Cast off the embryo's body", "गर्भस्य शरीराक्षेपे प्रवर्तन्ते."),
            [("Take away the mother's ojas", "Ojas belongs to unit 19."),
             ("Make the blood flow by chance", "The chance flow belongs to unit 18."),
             ("Swell the woman's belly", "The swelling belongs to unit 16.")],
            "If some proceed to cast off the body of the embryo …",
            "शरीराक्षेप = casting off the body."),
        order(1, "Put these phrases of unit 21 in their printed order.",
              ["यदि च दृष्टमपि समुल्लङ्घ्य", "केचिदतिशयशक्तियुक्ताः", "गर्भस्य शरीराक्षेपे प्रवर्तन्ते", "तदा कथमिव",
               "तज्जननीरुपेक्षेरन्"],
              "If … some powerful ones … proceed to cast off the embryo's body, then how … would neglect its mothers?",
              "यदि → केचित् → शरीराक्षेपे प्रवर्तन्ते → तदा कथम् इव → उपेक्षेरन्."),
        T(match(2, "Match each word of unit 21 to its meaning on the card.",
                [["यदि", "if"], ["तदा", "then"], ["अतिशयशक्तियुक्त", "endowed with excessive power"],
                 ["आक्षेप", "casting off"], ["उपेक्षेरन्", "would neglect"]],
                "यदि … तदा frames the argument; the other words fill it.",
                "यदि, तदा, अतिशयशक्तियुक्त, आक्षेप, उपेक्षेरन्.", role="extend"),
          "यदि … तदा = if … then: a supposition followed by its consequence."),
        mcq("discriminate", 3, "Which split of तज्जननीः is right?",
            ("तत् + जननीः", "त् before ज becomes ज्: तज्जननीः."),
            [("तज् + जननीः", "तज् is not a word; the pronoun is तत्."),
             ("तत् + ज्जननीः", "ज्जननीः is not a word."),
             ("तः + जननीः", "A visarga before ज would not give ज्ज.")],
            "तत् (its) + जननीः (mothers).",
            "त् + ज → ज्ज."),
        mcq("apply", 4, "In the clear part of unit 21, whom would they neglect?",
            ("Its mothers (जननीः)", "तज्जननीः उपेक्षेरन्: would neglect its mothers."),
            [("Its fathers (जनकान्)", "No father is named in the unit."),
             ("The physicians (वैद्यान्)", "No physician is named in the unit."),
             ("The ignorant (अज्ञान्)", "The ignorant are in unit 18, as speakers.")],
            "The question asks how they would neglect its mothers.",
            "तत् + जननीः = its mothers."),
        T(mcq("transfer", 5, "By the rule of तज्जननीः, how is तत् + जलम् written when joined?",
              ("तज्जलम्", "त् before ज becomes ज्."),
              [("तद्जलम्", "Before ज the त् goes on to ज्."),
               ("तच्जलम्", "च् appears before च/छ, not before ज."),
               ("तत्जलम्", "In sandhi the त् does not stay before ज.")],
              "तत् + जननीः → तज्जननीः; so तत् + जलम् → तज्जलम्.",
              "त् + ज → ज्ज."),
          "A final त् before ज (or झ) becomes ज्."),
    ],
}

# ---------------------------------------------------------------- unit 22
AUTHORED["22"] = {
    "title": "आर्तवं पुनः शशरुधिरलाक्षारसोपमम्",
    "question": "By unit 22, what ārtava is called pure?",
    "rule": ("Ārtava (menstrual blood) that resembles hare's blood and lac (lākṣā) juice and, when washed, loses its colour, "
             "they call pure."),
    "limits": ("शशरुधिर-लाक्षारस is read as 'hare's blood and lac-juice', a reading not decided. The unit gives the signs of pure "
               "ārtava only; it says nothing of its amount or of the days."),
    "explain_hi": ("अब शुद्ध आर्तव के लक्षण। जो खरगोश के रक्त और लाक्षा (लाख, लाख-कीट का रंग; मानक) के रस के समान हो, "
                   "और धोने पर रंग छोड़ता जाए, उसे शुद्ध कहते हैं। "
                   "यानी दो पहचानें: रंग की उपमा, और धोने पर दाग न रहना। "
                   "‘रसोपमम्’ में रस + उपमम् की सन्धि है (अ + उ → ओ)।"),
    "hook": "खरगोश-रक्त और लाख-रस जैसा, धोने पर रंग छूटे: शुद्ध आर्तव।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 22, pure ārtava resembles what?",
            ("Hare's blood and lac juice", "शशरुधिर-लाक्षारस-उपमम्."),
            [("Ghee, oil or honey in colour", "Those colours describe śukra in unit 10."),
             ("Milk mixed with sugarcane juice", "Milk and cane juice belong to unit 10's simile (ghee in milk, jaggery in cane juice)."),
             ("Pus and corpse-smelling fluid", "Neither is named in this unit.")],
            "Pure ārtava resembles hare's blood and lac juice.",
            "शश = hare; रुधिर = blood; लाक्षा = lac."),
        order(1, "Put these words of unit 22 in their printed order.",
              ["आर्तवम्", "शशरुधिरलाक्षारसोपमम्", "धौतम्", "विरज्यमानम्", "शुद्धमाहुः"],
              "Ārtava, resembling hare's blood and lac juice, washed, losing colour, they call pure.",
              "आर्तवम् → उपमम् → धौतम् → विरज्यमानम् → शुद्धम् आहुः."),
        T(match(2, "Match each word of unit 22 to its meaning on the card.",
                [["शशरुधिर", "hare's blood"], ["लाक्षा", "lac"], ["धौत", "washed"], ["विरज्यमान", "losing colour"],
                 ["शुद्ध", "pure"]],
                "Two words give the colour simile, two the washing test, and one the verdict.",
                "शशरुधिर, लाक्षा, धौत, विरज्यमान, शुद्ध.", role="extend"),
          "Pure ārtava is known by its colour and by losing that colour when washed."),
        mcq("discriminate", 3, "By unit 22, what happens to pure ārtava when it is washed?",
            ("It loses its colour", "धौतं विरज्यमानम्: washed, it loses its colour."),
            [("It leaves a lasting stain", "That is the opposite of विरज्यमान."),
             ("It turns a darker shade", "The word says it loses colour."),
             ("It gives off a smell", "No smell is named in this unit.")],
            "Washed, pure ārtava loses its colour.",
            "विरज्यमान = losing colour."),
        fill(4, "Ārtava of this kind they call ____, pure (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("शुद्धम्", None, "शुद्ध"),
             "शुद्धम् आहुः: they call it pure.",
             "शुद्ध = pure; here neuter accusative शुद्धम्, agreeing with आर्तवम्.",
             "शुद्ध = pure.", role="apply"),
        T(mcq("transfer", 5, "By the rule of रसोपमम्, how is चन्द्र + उपमम् written when joined?",
              ("चन्द्रोपमम्", "अ + उ → ओ, as in रस + उपमम्."),
              [("चन्द्रौपमम्", "अ + उ gives ओ, not औ."),
               ("चन्द्रूपमम्", "अ + उ does not give ऊ."),
               ("चन्द्रुपमम्", "The अ cannot simply vanish.")],
              "रस + उपमम् → रसोपमम्; so चन्द्र + उपमम् → चन्द्रोपमम् (resembling the moon).",
              "अ + उ → ओ."),
          "अ or आ before उ or ऊ merges into ओ (गुण)."),
    ],
}

# ---------------------------------------------------------------- unit 23
AUTHORED["23"] = {
    "title": "यथा च बालस्य जीर्णस्य वा तरोः",
    "question": "What simile does unit 23 give, and at what ages does it say semen emission is not found in a man?",
    "rule": ("Just as a young or an old tree has no flower and fruit (or their smell), so a man under sixteen or past seventy "
             "has no emission of semen and the rest."),
    "limits": ("Elliptical: 'is not found' is carried to the last clause. The unit gives the two age limits for a man only; "
               "the woman's follow in unit 24. It does not say what happens between the limits beyond the simile."),
    "explain_hi": ("एक उपमा: जैसे बहुत छोटे (बाल) या बहुत पुराने (जीर्ण) वृक्ष पर फूल-फल नहीं मिलते, या वैसे फूल-फल की गन्ध नहीं मिलती, "
                   "वैसे ही सोलह वर्ष से कम या सत्तर वर्ष पार कर चुके पुरुष में शुक्रसेक आदि नहीं होते। "
                   "‘ऊनषोडश’ = सोलह से कम, ‘अतीतसप्तति’ = सत्तर पार। "
                   "‘नोपलभ्यते’ = न + उपलभ्यते (अ + उ → ओ)। स्त्री की आयु-सीमा अगली इकाई में है।"),
    "hook": "बाल या बूढ़ा पेड़ = फल नहीं; १६ से कम या ७० पार पुरुष = शुक्रसेक नहीं।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 23, a man of which ages has no emission of semen and the rest?",
            ("Under sixteen or past seventy", "ऊनषोडश-अतीतसप्तति-वर्षस्य पुंसः."),
            [("Under twelve or past fifty", "Those are the woman's limits in unit 24."),
             ("Under twenty or past sixty", "These numbers are not in the unit."),
             ("Under eighteen or past eighty", "These numbers are not in the unit.")],
            "Under sixteen or past seventy years.",
            "ऊन = less than; अतीत = past."),
        order(1, "Put these phrases of unit 23 in their printed order.",
              ["बालस्य जीर्णस्य वा तरोः", "पुष्पफलम्", "गन्धो नोपलभ्यते", "तथैव", "शुक्रसेकादयः"],
              "First the tree simile, then तथैव (so indeed), then the man and his śukra-emission.",
              "Tree → flower-fruit → smell not found → so → śukra emission."),
        T(match(2, "Match each word of unit 23 to its meaning on the card.",
                [["बाल", "young"], ["जीर्ण", "old"], ["तरु", "tree"], ["ऊनषोडश", "less than sixteen"],
                 ["अतीतसप्तति", "past seventy"]],
                "Three words build the simile; two give the man's age limits.",
                "बाल, जीर्ण, तरु, ऊनषोडश, अतीतसप्तति.", role="extend"),
          "Young and old trees stand for the man too young or too old."),
        mcq("discriminate", 3, "In the simile of unit 23, which tree has no flower and fruit?",
            ("A young or an old one", "बालस्य जीर्णस्य वा तरोः."),
            [("A tree in a dry season", "No season is named in the simile."),
             ("A tree on poor soil", "No soil is named in the simile."),
             ("A tree cut at its root", "No cutting is named in the simile.")],
            "The young (बाल) or old (जीर्ण) tree is the likeness of the man too young or too old.",
            "बाल = young; जीर्ण = old."),
        mcq("apply", 4, "By unit 23, what holds for a man of seventy-five?",
            ("Semen emission and the rest are not found", "He is past seventy (अतीतसप्तति)."),
            [("Only the smell of semen is lost", "Smell belongs to the tree simile."),
             ("He is in the best age to beget", "Past seventy he falls outside, by the unit."),
             ("The rule applies only to women", "The unit speaks of a man (पुंसः).")],
            "A man past seventy is one of whom the unit says śukra emission and the rest are not found.",
            "अतीतसप्तति = past seventy."),
        T(mcq("transfer", 5, "By the rule of नोपलभ्यते, how is न + उक्तम् written when joined?",
              ("नोक्तम्", "अ + उ → ओ, as in न + उपलभ्यते."),
              [("नुक्तम्", "The अ cannot simply vanish."),
               ("नौक्तम्", "अ + उ gives ओ, not औ."),
               ("नवुक्तम्", "No व् is inserted.")],
              "न + उपलभ्यते → नोपलभ्यते; so न + उक्तम् → नोक्तम् (not said).",
              "अ + उ → ओ."),
          "न before a word in उ merges: अ + उ → ओ."),
    ],
}

# ---------------------------------------------------------------- unit 24
AUTHORED["24"] = {
    "title": "योषिच्चोनद्वादशातीतपञ्चाशद्वर्षायाः",
    "question": "By unit 24, in a woman of which ages are rajas, breast milk and the rest not found?",
    "rule": "Of a woman under twelve or past fifty years, the rajas (menses), breast milk (stanya) and the rest (are not found).",
    "limits": ("Elliptical: 'are not found' is carried from unit 23, which this unit completes. योषित् (nominative) does not agree "
               "with वर्षायाः (genitive); the printed forms are kept. आदयइति is read as आदयः इति (possible)."),
    "explain_hi": ("यह इकाई २३ के कथन को पूरा करती है। बारह वर्ष से कम या पचास वर्ष पार कर चुकी स्त्री में रजस् (मासिक स्राव) "
                   "और स्तन्य (स्तन का दूध) आदि नहीं मिलते; ‘नहीं मिलते’ क्रिया इकाई २३ से ली गई है। "
                   "‘योषित्’ प्रथमा और ‘वर्षायाः’ षष्ठी का मेल नहीं बैठता; छपे रूप रखे गए हैं। "
                   "अन्त का ‘इति’ कथन की समाप्ति बताता है।"),
    "hook": "पुरुष १६–७०, स्त्री १२–५०: इनके बाहर शुक्रसेक, रजस्, स्तन्य आदि नहीं।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 24, a woman of which ages has no rajas, breast milk and the rest?",
            ("Under twelve or past fifty", "ऊनद्वादश-अतीतपञ्चाशद्-वर्षायाः."),
            [("Under sixteen or past seventy", "Those are the man's limits in unit 23."),
             ("Under fourteen or past forty", "These numbers are not in the unit."),
             ("Under ten or past sixty", "These numbers are not in the unit.")],
            "Under twelve or past fifty years.",
            "ऊनद्वादश = under twelve; अतीतपञ्चाशत् = past fifty."),
        order(1, "Put these parts of unit 24 in their printed order.",
              ["योषिच्च", "ऊनद्वादश", "अतीतपञ्चाशत्", "वर्षायाः", "रजःस्तन्यादयः"],
              "Woman, under twelve, past fifty, years, rajas, breast milk and the rest.",
              "योषित् च → ऊनद्वादश → अतीतपञ्चाशत् → वर्षायाः → रजःस्तन्यादयः."),
        T(match(2, "Match each word of unit 24 to its meaning on the card.",
                [["योषित्", "woman"], ["ऊनद्वादश", "less than twelve"], ["अतीतपञ्चाशत्", "past fifty"],
                 ["रजस्", "menses"], ["स्तन्य", "breast milk"]],
                "Two words give the age limits, two name what is not found, and one names the woman.",
                "योषित्, ऊनद्वादश, अतीतपञ्चाशत्, रजस्, स्तन्य.", role="extend"),
          "ऊन (less than) and अतीत (past) frame the woman's limits as they did the man's."),
        mcq("discriminate", 3, "Which pair of limits belongs to the woman, not the man?",
            ("Twelve and fifty", "Unit 24: ऊनद्वादश, अतीतपञ्चाशत्."),
            [("Sixteen and seventy", "Those belong to the man, unit 23."),
             ("Sixteen and fifty", "That mixes the man's lower and the woman's upper limit."),
             ("Twelve and seventy", "That mixes the woman's lower and the man's upper limit.")],
            "Woman: twelve and fifty; man: sixteen and seventy.",
            "स्त्री १२–५०; पुरुष १६–७०."),
        multi("apply", 4, "Which does unit 24 name as not found in a woman outside those ages?",
              [("Rajas (menses)", "Right: रजः."),
               ("Breast milk (stanya)", "Right: स्तन्य."),
               ("Emission of semen", "That is the man's, in unit 23."),
               ("Smell of flower and fruit", "That is part of the tree simile of unit 23.")],
              [0, 1],
              "Rajas, breast milk and the rest (आदयः).",
              "रजः, स्तन्य, आदयः."),
        T(mcq("transfer", 5, "By the rule of योषिच्च, how is तत् + च written when joined?",
              ("तच्च", "त् before च becomes च्."),
              [("तद्च", "Before च the त् becomes च्, not द्."),
               ("तत्च", "In sandhi the त् does not stay before च."),
               ("तञ्च", "Before च the त् becomes च्, not the nasal ञ्.")],
              "योषित् + च → योषिच्च; so तत् + च → तच्च.",
              "त् + च → च्च."),
          "A final त् before च or छ becomes च्."),
    ],
}

# ---------------------------------------------------------------- unit 25
AUTHORED["25"] = {
    "title": "अथ शुद्धशुक्रार्तवमरोगम्",
    "question": "By unit 25, what couple is to be treated, and with which two enemas?",
    "rule": ("A couple with pure semen (śukra) and ārtava, free of disease and mutually attached, is oleated and cleansed as "
             "prescribed, then treated with āsthāpana (decoction enema) and anuvāsana (oil enema)."),
    "limits": ("The printed उपस्नेय is read as उपस्नेह्य (having oleated; possible). The subject of उपाचरेत् is unstated (one). "
               "The unit names no dose, no drugs and no days."),
    "explain_hi": ("अब संतान की तैयारी। जिस जोड़े के शुक्र और आर्तव शुद्ध हों, जो निरोग हो और परस्पर अनुरक्त हो, उसका स्नेहन करके "
                   "और विधि के अनुसार शोधन करके, आस्थापन (काढ़े की बस्ति) और अनुवासन (तेल की बस्ति) से उपचार करे। "
                   "छपा ‘उपस्नेय’ सम्भवतः ‘उपस्नेह्य’ है। "
                   "‘मिथोऽनुरक्तम्’ = मिथः + अनुरक्तम् (अः + अ → ओऽ)।"),
    "hook": "शुद्ध, निरोग, परस्पर अनुरक्त जोड़ा: स्नेहन, शोधन, फिर दो बस्तियाँ।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 25, with which two enemas is the couple treated?",
            ("Āsthāpana and anuvāsana", "आस्थापन-अनुवासनाभ्याम् उपाचरेत्."),
            [("Nasya and gaṇḍūṣa", "These are not named in this unit."),
             ("Vamana and virecana", "These are not named in this unit."),
             ("Añjana and lepa", "These are not named in this unit.")],
            "The couple is treated with āsthāpana and anuvāsana.",
            "आस्थापन = decoction enema; अनुवासन = oil enema."),
        order(1, "Put the four words describing the couple in unit 25 in their printed order.",
              ["शुद्धशुक्रार्तवम्", "अरोगम्", "मिथोऽनुरक्तम्", "मिथुनम्"],
              "Pure semen and ārtava, free of disease, mutually attached, the couple.",
              "शुद्धशुक्रार्तवम् → अरोगम् → मिथोऽनुरक्तम् → मिथुनम्."),
        T(match(2, "Match each word of unit 25 to its meaning on the card.",
                [["मिथुन", "couple"], ["अरोग", "free of disease"], ["मिथोऽनुरक्त", "mutually attached"],
                 ["आस्थापन", "decoction enema"], ["अनुवासन", "oil enema"]],
                "Three words describe the couple; two name the enemas.",
                "मिथुन, अरोग, मिथोऽनुरक्त, आस्थापन, अनुवासन.", role="extend"),
          "Āsthāpana is the decoction enema and anuvāsana the oil enema (both standard)."),
        mcq("discriminate", 3, "On the card, which of the two enemas of unit 25 is the oil type?",
            ("Anuvāsana (अनुवासन)", "The card glosses anuvāsana as an oil enema."),
            [("Āsthāpana (आस्थापन)", "Āsthāpana is the decoction type."),
             ("Both of them equally", "The card gives each its own type."),
             ("Neither of the two", "The card names anuvāsana as the oil type.")],
            "Āsthāpana = decoction enema; anuvāsana = oil enema.",
            "अनुवासन = oil; आस्थापन = decoction."),
        multi("apply", 4, "Which qualities of the couple does unit 25 state?",
              [("Pure semen and ārtava", "Right: शुद्धशुक्रार्तवम्."),
               ("Free of disease", "Right: अरोगम्."),
               ("Mutually attached", "Right: मिथोऽनुरक्तम्."),
               ("Of the same age", "No age is named in this unit."),
               ("Already parents of a son", "Nothing of the kind is said.")],
              [0, 1, 2],
              "Three qualities: pure semen and ārtava, free of disease, mutually attached.",
              "शुद्धशुक्रार्तव, अरोग, मिथोऽनुरक्त."),
        T(mcq("transfer", 5, "Built like आस्थापन-अनुवासनाभ्याम् (with the two), what does हस्ताभ्याम् mean?",
              ("With the two hands", "-आभ्याम् is instrumental dual: with the two."),
              [("In one hand", "That would be locative singular, हस्ते."),
               ("Of many hands", "That would be genitive plural, हस्तानाम्."),
               ("To a single hand", "That would be dative singular, हस्ताय.")],
              "आस्थापन-अनुवासनाभ्याम् = with the two (enemas); हस्ताभ्याम् = with the two hands.",
              "-आभ्याम् = instrumental (or dative/ablative) dual; here 'with the two'."),
          "The ending -आभ्याम् on an अ-stem marks the dual; with उपाचरेत् it means 'with the two'."),
    ],
}

# ---------------------------------------------------------------- unit 26
AUTHORED["26"] = {
    "title": "विशेषतस्तु घृतक्षीरवद्भिः",
    "question": "By unit 26, how are the man and the woman especially treated?",
    "rule": ("Especially: the man with preparations of sweet medicines containing ghee and milk; the woman with oil; "
             "and with Pitta-increasing meats."),
    "limits": ("Elliptical: उपाचरेत् of unit 25 is carried. The endings do not mark how the means are shared: oil may be for "
               "the woman only, and the meats for either or both. No question rests on the meats; no dose is given."),
    "explain_hi": ("इकाई २५ का ‘उपाचरेत्’ यहाँ भी समझा जाता है। विशेष रूप से: पुरुष को घी-दूध वाले मधुर औषधों के संस्कारों से, "
                   "नारी को तेल से, और पित्त बढ़ाने वाले मांसों से। "
                   "मांस किसके लिए है, पुरुष, नारी या दोनों, विभक्तियाँ यह नहीं बतातीं। "
                   "‘घृतक्षीरवत्’ में ‘-वत्’ का अर्थ है ‘वाला’।"),
    "hook": "पुरुष: घी-दूध वाले मधुर; नारी: तेल; और पित्तल मांस।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In the card's reading of unit 26, the man is treated with what?",
            ("Sweet medicines with ghee and milk", "घृतक्षीरवद्भिः मधुरौषधसंस्कारैः पुरुषम्."),
            [("Oil alone, rubbed on the body", "Oil comes with नारीम्, the woman, in the card's order."),
             ("Bitter medicines with honey", "Bitter medicines and honey are not named."),
             ("Cold water and fasting", "Neither is named in this unit.")],
            "With preparations of sweet medicines containing ghee and milk, the man.",
            "घृत = ghee; क्षीर = milk; मधुर = sweet."),
        order(1, "Put these phrases of unit 26 in their printed order.",
              ["विशेषतस्तु", "घृतक्षीरवद्भिर्मधुरौषधसंस्कारैः", "पुरुषम्", "तैलेन नारीम्", "पित्तलैश्च मांसैः"],
              "Especially: the ghee-milk preparations, the man; with oil, the woman; and with Pitta-increasing meats.",
              "विशेषतः → घृतक्षीर… → पुरुषम् → तैलेन नारीम् → पित्तलैः मांसैः."),
        T(match(2, "Match each word of unit 26 to its meaning on the card.",
                [["घृत", "ghee"], ["क्षीर", "milk"], ["मधुर", "sweet"], ["तैल", "oil"], ["मांस", "meat"]],
                "These five words name the substances of the unit.",
                "घृत, क्षीर, मधुर, तैल, मांस.", role="extend"),
          "The unit names ghee, milk, sweet medicines, oil and Pitta-increasing meats."),
        mcq("discriminate", 3, "In the printed order of unit 26, which word stands right before नारीम् (the woman)?",
            ("तैलेन, with oil", "तैलेन नारीम्: with oil, the woman."),
            [("मांसैः, with meats", "मांसैः comes at the end, after नारीम्."),
             ("पुरुषम्, the man", "पुरुषम् comes before तैलेन, not just before नारीम्."),
             ("घृतक्षीरवद्भिः, with ghee and milk", "That stands before पुरुषम्.")],
            "The printed order is: … पुरुषम्, तैलेन नारीम्, पित्तलैश्च मांसैः.",
            "तैलेन नारीम्."),
        mcq("apply", 4, "Which verb must be supplied from unit 25 to complete unit 26?",
            ("उपाचरेत्, one should treat", "Unit 26 has no verb; उपाचरेत् of unit 25 is carried."),
            [("उपशाम्यति, it subsides", "That verb is in unit 15."),
             ("ईक्षेत, one should look to", "That verb is in unit 14."),
             ("ब्रुवते, they say", "That verb is in unit 18.")],
            "The man and the woman are the objects of उपाचरेत्, carried over from unit 25.",
            "Elliptical: उपाचरेत् carried."),
        T(mcq("transfer", 5, "Built like घृतक्षीरवत् (containing ghee and milk), what does धनवत् mean?",
              ("Possessing wealth", "-वत् added to a noun = possessing it."),
              [("Seeking wealth", "Seeking would be -काम, as धनकाम."),
               ("Without wealth", "Without would need निर्- or अ-."),
               ("Giver of wealth", "Giver would be -द, as धनद.")],
              "घृतक्षीरवत् = possessing ghee and milk; धनवत् = possessing wealth.",
              "noun + -वत् = possessing it."),
          "The suffix -वत् on a noun makes an adjective: possessing that thing."),
    ],
}

# ---------------------------------------------------------------- unit 27
AUTHORED["27"] = {
    "title": "एवं हि समानगुणतया",
    "question": "By unit 27, why are semen and ārtava nourished by this treatment?",
    "rule": "Thus indeed, by the likeness of qualities, the semen (śukra) and ārtava are nourished.",
    "limits": ("The unit states the reason only in general (similar qualities); it does not list which qualities match, "
               "and it gives no further treatment."),
    "explain_hi": ("यह इकाई २५-२६ के उपचार का कारण बताती है। इस प्रकार, समान गुण होने से, शुक्र और आर्तव पुष्ट होते हैं। "
                   "‘समानगुणता’ यानी समान गुणों वाला होना: समान से समान बढ़ता है, यह सिद्धान्त है। "
                   "‘शुक्रार्तवम्’ = शुक्र + आर्तवम् (अ + आ → आ)।"),
    "hook": "समान गुण, समान पुष्टि: शुक्र-आर्तव बढ़ते हैं।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 27, by what are semen and ārtava nourished?",
            ("By likeness of qualities", "समानगुणतया: by having similar qualities."),
            [("By opposition of qualities", "The word is समान, similar, not opposite."),
             ("By fasting for some days", "No fasting is named here."),
             ("By the passing of time", "No time is named here.")],
            "Thus, by the likeness of qualities, śukra and ārtava are nourished.",
            "समानगुणता = likeness of qualities."),
        order(1, "Put the words of unit 27 in their printed order.",
              ["एवम्", "हि", "समानगुणतया", "शुक्रार्तवम्", "आप्यायते"],
              "Thus, indeed, by likeness of qualities, semen and ārtava are nourished.",
              "एवम् → हि → समानगुणतया → शुक्रार्तवम् → आप्यायते."),
        T(fill(2, "The word for similar in समानगुणतया is ____ (type it in Devanagari or in English letters, e.g. dharma).",
               accepts("समान", None, "samana"),
               "समान = similar; गुण = quality; -ता = the state of.",
               "समान means similar, alike.", "समान = similar."),
          "समान means similar; समानगुणता is the state of having similar qualities."),
        mcq("discriminate", 3, "Which split of शुक्रार्तवम् is right?",
            ("शुक्र + आर्तवम्", "अ + आ → आ: शुक्रार्तवम्."),
            [("शुक्रा + र्तवम्", "र्तवम् is not a word."),
             ("शुक्र + अर्तवम्", "The word is आर्तव, with a long आ."),
             ("शुक्रः + आर्तवम्", "A visarga would not vanish into आ here.")],
            "शुक्र (semen) + आर्तवम् (ārtava), a dvandva: semen and ārtava.",
            "अ + आ → आ."),
        match(4, "Match each word of unit 27 to its meaning on the card.",
              [["एवम्", "thus"], ["समान", "similar"], ["गुण", "quality"], ["आप्यायते", "is nourished"]],
              "Four words carry the whole statement.",
              "एवम्, समान, गुण, आप्यायते.", role="apply"),
        T(mcq("transfer", 5, "Built like समानगुणता, what does लघुता mean?",
              ("Lightness", "-ता makes an abstract noun: लघु (light) → लघुता."),
              [("A light thing", "-ता gives the quality, not the thing."),
               ("Making light", "That would need a verb or -करण."),
               ("Very light", "-ता does not intensify.")],
              "समानगुण + ता = the state of having similar qualities; लघु + ता = lightness.",
              "-ता = the state or quality of."),
          "-ता added to a word makes an abstract noun: the state or quality of it."),
    ],
}

# ===================================================================== NOTES_HI
NOTES_HI = {
    "14": ("विश्वास कम। छपा ‘संशुक्रमशुकं’ को ‘संशुक्रम् अशुक्रम्’ पढ़ा गया है (‘अशुकम्’ कोई शब्द नहीं; सुधार सम्भावित)। "
           "वाक्य-रचना अनिश्चित: बिना कहा कर्ता सम्भवतः इकाई ११ का आर्तव है। ‘गुल्मी भवति’ का अर्थ (गुल्म वाला हो जाता है) तय नहीं। "
           "सन्धियाँ: पित्तलैः + उपचारैः → पित्तलैरुपचारैः; दर्शयत् + गुल्मी → दर्शयद्गुल्मी; गुल्मचिकित्सितम् + ईक्षेत → गुल्मचिकित्सितमीक्षेत।"),
    "15": ("विश्वास कम। छपा ‘गर्भइव’ दो तरह पढ़ा जा सकता है: ‘गर्भा एव’ (गर्भवती में भी; यहाँ लिया गया) या ‘गर्भ एव’ (स्वयं गर्भ)। "
           "‘वातोदरंभवति’ में छपाई में शब्द जुड़े हैं: वातोदरम् भवति। ‘वातौपशमनैः’ की संज्ञा नहीं दी गई। "
           "वातोदर का आधुनिक अर्थ (पेट का फूलना) सम्भावित है।"),
    "16": ("छपा ‘वर्द्वयति’ को ‘वर्धयति’ पढ़ा गया है (ध के स्थान पर द्व: छपाई/OCR की भूल)। "
           "विशेषणों का बँटवारा पक्का नहीं: स्तम्भित आर्तव के साथ, अनुपद्रव उदर के साथ लिया गया। "
           "सन्धियाँ: सौम्यैः + बृंहण → सौम्यैर्बृंहण; अनुपद्रवम् + एव + उदरम् → अनुपद्रवमेवोदरम् (अ + उ → ओ)।"),
    "17": ("छपा ‘तामगर्भी’ सम्भवतः ‘ताम् अगर्भिणीम्’ है; अन्त का म् और ‘णी’ छूटे लगते हैं (‘अगर्भीम्’ भी सम्भव)। "
           "‘येन’ = जिससे / जिसके कारण, इकाई १६ के दिखावे की ओर। सन्धि: आहुः + मूढाः → आहुर्मूढाः।"),
    "18": ("‘विपरीतैः’ की संज्ञा नहीं दी गई; सम्भवतः इकाई १६ के उल्टे उपाय (निश्चित नहीं)। ‘भूत’ = प्राणी, आत्मा; शाब्दिक रखा गया। "
           "छपा ‘वाप्रवृत्ते’ = वा + प्रवृत्ते। सन्धि: भूतहृतम् + इति + अज्ञाः → भूतहृतमित्यज्ञाः; अपश्यन्तः + भूत → अपश्यन्तो भूत (अः + घोष व्यंजन → ओ)।"),
    "19": ("छपा ‘कायस्यानिष्टत्वाद्शक्तेर्वा’ में ‘अशक्तेः’ का आरम्भिक अ छूटा लगता है (सम्भावित सुधार)। "
           "वाक्य अधूरा: ‘अपहरणम्’ ‘कायस्य’ के साथ भी समझा जाता है। किसकी अनिष्टता या असमर्थता, यह नहीं कहा। "
           "सन्धि: ओजसः + अपहरणम् → ओजसोऽपहरणम्। इकाई १८ का तर्क आगे बढ़ता है।"),
    "20": ("विश्वास कम। छपा ‘प्रवृत्ते रुपलब्धिर्न’ छपाई की दूरी सुधारकर ‘प्रवृत्तेः उपलब्धिः न’ पढ़ा गया है: र् पिछले शब्द का विसर्ग है। "
           "तर्क पक्का नहीं। सन्धि: कस्यचित् + मानुषैः → कस्यचिन्मानुषैः। इकाई १९ से जुड़ा (हि)।"),
    "21": ("विश्वास कम। ‘प्राप्तविशराः’ अस्पष्ट शब्द है, बिना विभाजन रखा गया; इसका अर्थ केवल अनुमान है। "
           "‘केचिदतिशयशक्तियुक्ता’ में अन्त का विसर्ग छूटा लगता है। छपा ‘प्रवर्त्तन्ते’ (द्वित्व) सामान्य ‘प्रवर्तन्ते’ किया गया। "
           "सन्धि: तत् + जननीः → तज्जननीः। इकाई १९-२० का तर्क आगे।"),
    "22": ("‘शशरुधिरलाक्षारसोपमम्’ को द्वन्द्व (खरगोश-रक्त और लाक्षा-रस) पढ़ा गया, यह तय नहीं। लाक्षा = लाख, लाख-कीट का रंग (मानक)। "
           "सन्धि: रस + उपमम् → रसोपमम् (अ + उ → ओ); शुद्धम् + आहुः → शुद्धमाहुः।"),
    "23": ("वाक्य अधूरा: ‘न उपलभ्यते’ पहले खण्ड और अन्तिम खण्ड दोनों में समझा जाता है। "
           "छपा ‘नोनषोडश’ = न + ऊनषोडश (अ + ऊ → ओ)। छपा ‘यथाच’ = यथा च। सन्धि: न + उपलभ्यते → नोपलभ्यते; तथा + एव → तथैव।"),
    "24": ("इकाई २३ का कथन पूरा करती है। ‘योषित्’ प्रथमा, ‘वर्षायाः’ षष्ठी: मेल नहीं; सम्भवतः ‘योषितः’ अभिप्रेत, छपे रूप रखे गए। "
           "छपा ‘रजस्तन्यादयइति’ सम्भवतः ‘रजःस्तन्यादयः इति’ है। सन्धि: योषित् + च → योषिच्च; च + ऊन → चोन।"),
    "25": ("छपा ‘उपस्नेय’ सम्भवतः ‘उपस्नेह्य’ है (ह छूटा)। छपा ‘संशोद्ध्य’ (द्वित्व) सामान्य ‘संशोध्य’ किया गया। "
           "‘आस्थापन अनुवासनाभ्याम्’ छपी दूरी के पार एक ही द्वन्द्व (तृतीया द्विवचन) है। सन्धि: मिथः + अनुरक्तम् → मिथोऽनुरक्तम्।"),
    "26": ("‘उपाचरेत्’ इकाई २५ से समझा जाता है। विभक्तियाँ यह नहीं बतातीं कि तैल केवल नारी के लिए है या नहीं, और पित्तल मांस किसके लिए। "
           "सन्धियाँ: विशेषतः + तु → विशेषतस्तु; पित्तलैः + च → पित्तलैश्च; मधुर + औषध → मधुरौषध।"),
    "27": ("विश्वास ऊँचा। छपा ‘हिसमानगुणतया’ = हि समानगुणतया (छपाई में जुड़ा)। "
           "सन्धि: शुक्र + आर्तवम् → शुक्रार्तवम्; शुक्रार्तवम् + आप्यायते → शुक्रार्तवमाप्यायते।"),
}

# ===================================================================== AIDS
AIDS = {
    "14": {
        "chain": {"steps": ["वात-कफ से ढके मार्ग: न बहता", "पित्तल उपचारों से: बहता", "जीवरहित", "वातल सेवन करती स्त्री में",
                            "गर्भ-लक्षण दिखाता: गुल्मी", "गुल्म-चिकित्सा देखे"]},
        "sandhi": ("ऐः + स्वर → ऐर्: पित्तलैः + उपचारैः → पित्तलैरुपचारैः · त् + ग → द्ग: दर्शयत् + गुल्मी → दर्शयद्गुल्मी · "
                   "म् + स्वर: गुल्मचिकित्सितम् + ईक्षेत → गुल्मचिकित्सितमीक्षेत।"),
        "contrast": "दिखता: गर्भ के लक्षण ↔ है: जीवरहित; उपाय: गुल्म-चिकित्सा देखे।",
        "frame": "वाक्य ढीला है; अनुवाद छपे क्रम में चलता है। पक्का अन्त: ‘तत्र गुल्मचिकित्सितमीक्षेत’।",
    },
    "15": {
        "frame": "कदाचित् → वातोदरम् भवति → तत् वातौपशमनैः उपशाम्यति: होता है, फिर शान्त होता है।",
        "sandhi": "अ + औ → औ: वात + औपशमनैः → वातौपशमनैः · ऐः + उ → ऐरु: वातौपशमनैः + उपशाम्यति → वातौपशमनैरुपशाम्यति · त् + व → द्व: तत् + वात → तद्वात।",
        "puns": "मेरी बनाई, केवल सुनने की सहायता: ‘वात-उदर’ को ‘वात का उदर’ बोलें; ‘वात-औपशमन’ से वही वात शान्त।",
    },
    "16": {
        "diagram": {"groups": [
            {"label": "कारण", "items": ["सौम्य", "बृंहणात्मक", "आहार-विहार"]},
            {"label": "आर्तव", "items": ["स्तम्भित (रुका)"]},
            {"label": "परिणाम", "items": ["उदर बढ़ता", "अनुपद्रव", "मानो गर्भाधिष्ठित"]}]},
        "chunks": "तदेव कदाचिदार्तवं | सौम्यैर्बृंहणात्मभिराहारविहारैः | स्तम्भितम् | अनुपद्रवमेवोदरं | गर्भाधिष्ठितमिव वर्धयति।",
        "sandhi": "ऐः + ब → ऐर्ब: सौम्यैः + बृंहण → सौम्यैर्बृंहण · अ + उ → ओ: एव + उदरम् → एवोदरम् · त् + ए → दे: तत् + एव → तदेव।",
        "pegs": "मेरा बनाया चित्र: एक गुब्बारे-सा फूला पेट, ऊपर प्रश्नचिह्न: ‘मानो गर्भ?’ (केवल याद के लिए)",
    },
    "17": {
        "frame": "येन (इकाई १६ के दिखावे से) → मूढाः → अगर्भिणी को → गर्भिणी कहते हैं।",
        "sandhi": "उः + म → उर्म: आहुः + मूढाः → आहुर्मूढाः · म् + स्वर: गर्भिणीम् + आहुः → गर्भिणीमाहुः।",
        "seesaw": "है: अगर्भिणी ↔ कहते हैं: गर्भिणी।",
    },
    "18": {
        "chain": {"steps": ["विपरीतों से या संयोग से", "रक्त बहता है", "गर्भ-शरीर नहीं दिखता", "अज्ञ कहते: भूत ले गए"]},
        "sandhi": "ऐः + य → ऐर्य: विपरीतैः + यदृच्छया → विपरीतैर्यदृच्छया · इ + अ → य: इति + अज्ञाः → इत्यज्ञाः · अः + व → ओ व: ततः + विपरीतैः → ततो विपरीतैः।",
        "frame": "यह अज्ञों का मत है; इकाई १९ से खंडन आरम्भ।",
        "story": "मेरी बनाई कथा: पेट बढ़ा, सब ने गर्भ समझा; फिर रक्त बहा और शिशु कहीं न दिखा। लोग बोले: ‘भूत ले गए!’ (केवल याद के लिए)",
    },
    "19": {
        "seesaw": "राक्षसों द्वारा अपहरण सम्भव: ओज ↔ सम्भव नहीं: काय (शरीर)।",
        "sandhi": "अः + अ → ओऽ: ओजसः + अपहरणम् → ओजसोऽपहरणम् · इ + ओ → यो: सम्भवति + ओजसः → सम्भवत्योजसः · त् + स → त्स: यस्मात् + सम्भवति।",
        "frame": "यस्मात् (क्योंकि) → कारण: अनिष्टत्वात् या अशक्तेः (किसकी, नहीं कहा)।",
    },
    "20": {
        "frame": "हि (क्योंकि) → इच्छा-शक्ति की प्रवृत्ति नहीं दिखती (पाठ अनिश्चित) → और मनुष्यों द्वारा देह-हरण नहीं देखा जाता।",
        "sandhi": "त् + म → न्म: कस्यचित् + मानुषैः → कस्यचिन्मानुषैः · ऐः + द → ऐर्द: मानुषैः + देह → मानुषैर्देह।",
        "chunks": "इच्छाशक्तयोर्हि प्रवृत्तेः | उपलब्धिर्न | च दृश्यते | कस्यचिन्मानुषैः | देहापहारः।",
    },
    "21": {
        "frame": "यदि (कुछ शक्तिशाली गर्भ-शरीर फेंकें) → तदा कथम् इव (तो कैसे) → तज्जननीः उपेक्षेरन् (उसकी माताओं की उपेक्षा करें)?",
        "sandhi": "त् + ज → ज्ज: तत् + जननीः → तज्जननीः · ईः + उ → ईरु: जननीः + उपेक्षेरन् → जननीरुपेक्षेरन् · म् + स्वर: कथम् + इव → कथमिव।",
        "chunks": "यदि च दृष्टमपि समुल्लङ्घ्य | केचिदतिशयशक्तियुक्ताः | गर्भस्य शरीराक्षेपे प्रवर्तन्ते | तदा कथमिव | प्राप्तविशराः (अस्पष्ट) | तज्जननीरुपेक्षेरन्।",
    },
    "22": {
        "diagram": {"groups": [
            {"label": "रंग की उपमा", "items": ["शश-रुधिर (खरगोश का रक्त)", "लाक्षा-रस (लाख का रस)"]},
            {"label": "धोने की परख", "items": ["धौतम्", "विरज्यमानम्"]},
            {"label": "निर्णय", "items": ["शुद्धम् आहुः"]}]},
        "sandhi": "अ + उ → ओ: रस + उपमम् → रसोपमम् · म् + स्वर: शुद्धम् + आहुः → शुद्धमाहुः।",
        "pegs": "मेरा बनाया चित्र: एक सफ़ेद कपड़ा जिस पर लाख-लाल धब्बा, धोते ही फीका पड़ता हुआ। (केवल याद के लिए)",
    },
    "23": {
        "contrast": "उपमान: बाल या जीर्ण वृक्ष → पुष्प-फल, गन्ध नहीं ↔ उपमेय: १६ से कम या ७० पार पुरुष → शुक्रसेक आदि नहीं।",
        "sandhi": "अ + उ → ओ: न + उपलभ्यते → नोपलभ्यते · अ + ऊ → ओ: न + ऊनषोडश → नोनषोडश · आ + ए → ऐ: तथा + एव → तथैव।",
        "anchors": "१६ और ७०: ‘सोलह में शुरू, सत्तर पर विराम’ (मेरी याद-पद्धति)।",
        "chunks": "यथा च बालस्य जीर्णस्य वा तरोः पुष्पफलम् | पुष्पफलस्य वा तद्विधस्य गन्धो नोपलभ्यते | तथैव | नोनषोडशातीतसप्ततिवर्षस्य पुंसः | शुक्रसेकादयः।",
    },
    "24": {
        "contrast": "पुरुष (इकाई २३): १६ से कम, ७० पार → शुक्रसेक आदि नहीं ↔ स्त्री (इकाई २४): १२ से कम, ५० पार → रजस्, स्तन्य आदि नहीं।",
        "sandhi": "त् + च → च्च: योषित् + च → योषिच्च · अ + ऊ → ओ: च + ऊन → चोन · त् + व → द्व: पञ्चाशत् + वर्षायाः → पञ्चाशद्वर्षायाः।",
        "anchors": "स्त्री: १२ और ५० · पुरुष: १६ और ७० (मेरी याद-पद्धति: स्त्री के दोनों अंक छोटे)।",
    },
    "25": {
        "chain": {"steps": ["जोड़ा: शुद्ध शुक्र-आर्तव, निरोग, परस्पर अनुरक्त", "उपस्नेह्य: स्नेहन (पाठ सम्भावित)", "विधिवत् संशोध्य: शोधन",
                            "आस्थापन और अनुवासन (काढ़े और तेल की बस्ति)"]},
        "sandhi": "अः + अ → ओऽ: मिथः + अनुरक्तम् → मिथोऽनुरक्तम् · अ + आ → आ: शुक्र + आर्तवम् → शुक्रार्तवम् · त् + स → त्स: विधिवत् + संशोध्य।",
        "letters": "जोड़े के तीन गुण: शु-अ-मि (शुद्धशुक्रार्तव, अरोग, मिथोऽनुरक्त)।",
    },
    "27": {
        "frame": "एवम् (इस प्रकार, इकाई २५-२६ के उपचार से) → समानगुणतया (समान गुण से) → शुक्रार्तवम् आप्यायते (पुष्ट होते हैं)।",
        "sandhi": "अ + आ → आ: शुक्र + आर्तवम् → शुक्रार्तवम् · म् + स्वर: शुक्रार्तवम् + आप्यायते → शुक्रार्तवमाप्यायते।",
        "puns": "मेरी बनाई, केवल सुनने की सहायता: ‘समान से समान’: समान गुण, समान पुष्टि।",
    },
}

AIDS["26"] = {
    "diagram": {"groups": [
        {"label": "पुरुषम्", "items": ["घृत-क्षीर वाले", "मधुर औषध-संस्कार"]},
        {"label": "नारीम्", "items": ["तैलेन"]},
        {"label": "और (किसके लिए, अनिश्चित)", "items": ["पित्तल मांस"]}]},
    "sandhi": "अः + त → स्त: विशेषतः + तु → विशेषतस्तु · ऐः + च → ऐश्च: पित्तलैः + च → पित्तलैश्च · अ + औ → औ: मधुर + औषध → मधुरौषध।",
    "frame": "उपाचरेत् (इकाई २५ से) · विशेषतः: पुरुष, नारी, फिर मांस।",
}

# ===================================================================== IMAGE_SPECS
IMAGE_SPECS = {
    ("14", "chain"): {
        "file": "sh1-gulma-14.svg",
        "alt": ("Chain of unit 14 in printed order: not flowing where passages are covered by Vata and Kapha; flowing with "
                "Pitta-increasing measures; lifeless; in a woman who resorts to Vata-increasing things; showing signs of "
                "pregnancy, 'gulmi' (sense undecided); look to the gulma treatment."),
        "type": "chain",
        "title": "इकाई १४: छपे क्रम में (पाठ अनिश्चित)",
        "steps": ["वात-कफ से ढके मार्ग: न बहता", "पित्तल उपचारों से: बहता", "जीवरहित", "वातल सेवन करती स्त्री में",
                  "गर्भ-लक्षण दिखाता: गुल्मी", "गुल्म-चिकित्सा देखे"],
    },
    ("16", "diagram"): {
        "file": "sh1-stambhita-artava-16.svg",
        "alt": ("Flowchart of unit 16: gentle, bulk-promoting diets and regimens hold back the artava; the held-back artava "
                "increases the belly, free of complications, as if occupied by an embryo."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"सौम्य, बृंहण<br/>आहार-विहार\"] --> B[\"आर्तव स्तम्भित<br/>(रुका)\"]\n"
                 "  B --> C[\"उदर बढ़ता<br/>अनुपद्रव\"]\n"
                 "  C --> D[\"मानो गर्भ से<br/>अधिष्ठित\"]\n"),
    },
    ("18", "chain"): {
        "file": "sh1-bhutahrta-18.svg",
        "alt": ("Chain of unit 18: through contrary (ones) or by chance the blood flows; the body of the embryo is not seen; "
                "the ignorant say it was carried off by beings."),
        "type": "chain",
        "title": "अज्ञों का मत (इकाई १८)",
        "steps": ["विपरीतों से या संयोग से", "रक्त बहता है", "गर्भ-शरीर नहीं दिखता", "अज्ञ कहते: भूत ले गए"],
    },
    ("19", "seesaw"): {
        "file": "sh1-ojas-kaya-19.svg",
        "alt": "Split of unit 19: what rakshas can take away (ojas) against what they cannot (the body), for undesirability or incapacity.",
        "type": "split",
        "title": "राक्षस क्या हर सकते हैं? (इकाई १९)",
        "cols": [["सम्भव", ["ओज (जीवन-सार)"]],
                 ["सम्भव नहीं", ["काय (शरीर)", "कारण: अनिष्टता", "या असमर्थता (पाठ सम्भावित)"]]],
    },
    ("22", "diagram"): {
        "file": "sh1-shuddha-artava-22.svg",
        "alt": ("Mindmap of unit 22: pure artava resembles hare's blood and lac juice, and when washed it loses its colour."),
        "type": "mermaid",
        "code": ("mindmap\n"
                 "  शुद्ध आर्तव\n"
                 "    रंग की उपमा\n"
                 "      खरगोश का रक्त\n"
                 "      लाक्षा का रस\n"
                 "    धोने पर\n"
                 "      रंग छूट जाए\n"),
    },
    ("23", "contrast"): {
        "file": "sh1-taru-upama-23.svg",
        "alt": ("Table of the simile of unit 23: a young or old tree has no flower, fruit or their smell; a man under sixteen "
                "or past seventy has no emission of semen and the rest."),
        "type": "table",
        "title": "उपमा (इकाई २३)",
        "heads": ["वृक्ष (उपमान)", "पुरुष (उपमेय)"],
        "rows": [["बाल (छोटा) वृक्ष", "१६ से कम वर्ष"],
                 ["जीर्ण (पुराना) वृक्ष", "७० से अधिक वर्ष"],
                 ["पुष्प-फल, गन्ध नहीं", "शुक्रसेक आदि नहीं"]],
    },
    ("24", "contrast"): {
        "file": "sh1-ayu-sima-24.svg",
        "alt": ("Table joining units 23 and 24: a man under sixteen or past seventy has no semen emission and the rest; a woman "
                "under twelve or past fifty has no menses, breast milk and the rest."),
        "type": "table",
        "title": "आयु-सीमा (इकाई २३-२४)",
        "heads": ["पुरुष (इकाई २३)", "स्त्री (इकाई २४)"],
        "rows": [["१६ से कम", "१२ से कम"],
                 ["७० से अधिक", "५० से अधिक"],
                 ["शुक्रसेक आदि नहीं", "रजस्, स्तन्य आदि नहीं"]],
    },
    ("25", "chain"): {
        "file": "sh1-mithuna-shodhana-25.svg",
        "alt": ("Chain of unit 25: a couple with pure semen and artava, free of disease and mutually attached; oleation "
                "(probable reading); cleansing as prescribed; asthapana and anuvasana enemas together (decoction; oil)."),
        "type": "chain",
        "title": "दंपती का शोधन (इकाई २५)",
        "steps": ["शुद्ध शुक्र-आर्तव, निरोग, अनुरक्त जोड़ा", "स्नेहन (पाठ सम्भावित)", "विधिवत् शोधन",
                  "आस्थापन और अनुवासन बस्ति (काढ़ा; तेल)"],
    },
}
