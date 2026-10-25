from helpers import mcq, match, order, fill, multi, accepts


def T(q, teaches):
    q["teaches"] = teaches
    return q


AUTHORED = {}

# ---------------------------------------------------------------- unit 76
AUTHORED["76"] = {
    "title": "यदा तु कार्त्स्न्येनोपहंति",
    "question": "What two cases does unit 76 name for the unstated subject?",
    "rule": ("When it wholly damages (कार्त्स्न्येन उपहन्ति), or, without damaging, simply closes the mouth of the channel "
             "(स्रोतोमुखं पिधत्ते): this appears to be the 'when' half of a sentence whose 'then' comes in unit 77."),
    "limits": ("The subject is not printed in this line; it is carried from earlier context and the card does not name it. "
               "The line does not say which channel, nor what follows; the result is in unit 77. "
               "The printed उपहंति is the usual spelling उपहन्ति."),
    "explain_hi": ("यह एक गद्य-पंक्ति है और सम्भवतः ‘यदा … तदा’ वाले वाक्य का पहला आधा भाग है; ‘तदा’ वाला भाग सम्भवतः इकाई ७७ में है। "
                   "यहाँ दो विकल्प हैं: या तो वह पूरी तरह हानि पहुँचाता है, या हानि पहुँचाए बिना केवल स्रोत (वाहिनी) का मुख ढक देता है। "
                   "कर्ता इस पंक्ति में छपा नहीं है; वह पहले के प्रसंग से आता है, इसलिए कार्ड उसका नाम नहीं लेता। "
                   "‘अनुपघ्नन्’ वर्तमान कृदन्त है: ‘हानि न पहुँचाते हुए’।"),
    "hook": "या पूरा घात, या बिना घात केवल स्रोत का मुँह बंद।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 76, what is closed in the second case?",
            ("The mouth of the channel (srotas)", "स्रोतोमुखं पिधत्ते: it closes the mouth of the channel."),
            [("The mouth of the uterus (garbhāśaya)", "The uterus is not named in this line."),
             ("The eyes of the embryo in the womb", "No eyes are named in this line."),
             ("The way of the breath", "Breath is not named in this line.")],
            "The second case: without damaging, it simply closes the mouth of the channel (स्रोतोमुख).",
            "स्रोतः + मुखम् = the mouth of the channel; पिधत्ते = closes."),
        order(1, "Put these phrases of unit 76 in their printed order.",
              ["यदा तु", "कार्त्स्न्येनोपहंति", "अनुपघ्नन्नेव वा", "स्रोतोमुखं", "पिधत्ते"],
              "When, however, (it) wholly damages, or without damaging simply, the mouth of the channel, closes.",
              "यदा तु → कार्त्स्न्येनोपहंति → अनुपघ्नन्नेव वा → स्रोतोमुखं → पिधत्ते."),
        T(match(2, "Match each word of unit 76 to its meaning on the card.",
                [["कार्त्स्न्येन", "wholly, completely"], ["उपहन्ति", "damages"], ["अनुपघ्नन्", "not damaging"],
                 ["स्रोतोमुख", "mouth of the channel"], ["पिधत्ते", "closes, covers"]],
                "Five words carry the two cases: whole damage, or closing without damage.",
                "उपहन्ति = damages; अनुपघ्नन् = an + upa-√han, not damaging; पिधत्ते = closes.", role="extend"),
          "अनुपघ्नन् is the negated present participle of उप-√हन्: 'while not damaging'."),
        mcq("discriminate", 3, "Which split of अनुपघ्नन्नेव is right?",
            ("अनुपघ्नन् + एव", "A final न् after a short vowel is doubled before a vowel: अनुपघ्नन्न् + एव."),
            [("अनुपघ्नन्न + एव", "अ + ए would join as ऐ: अनुपघ्नन्नैव."),
             ("अनुपघ्नन् + नैव", "न्न् + ऐ would print अनुपघ्नन्नैव, with ऐ, not ए."),
             ("अनुपघ्नम् + एव", "म् before a vowel would give अनुपघ्नमेव.")],
            "अनुपघ्नन् (not damaging) + एव (just): the न् is doubled because a short vowel stands before it.",
            "Short vowel + न् + vowel → न्न् + vowel."),
        multi("apply", 4, "Which two cases does unit 76 name?",
              [("It wholly damages", "Right: कार्त्स्न्येनोपहंति."),
               ("It opens the channel wide", "The line says it closes (पिधत्ते) the mouth, not opens it."),
               ("Without damaging, it closes the channel's mouth", "Right: अनुपघ्नन्नेव वा स्रोतोमुखं पिधत्ते."),
               ("It damages only half of it", "कार्त्स्न्येन means wholly, not half.")],
              [0, 2],
              "The two cases joined by वा (or): whole damage, or closing the mouth of the channel without damage.",
              "कार्त्स्न्येन उपहन्ति वा अनुपघ्नन् एव स्रोतोमुखं पिधत्ते."),
        T(mcq("transfer", 5, "By the rule of स्रोतोमुखम्, how is तपः + वनम् written when joined?",
              ("तपोवनम्", "अः before a voiced consonant (here व) becomes ओ."),
              [("तपस्वनम्", "Visarga becomes स् only before त or थ, not before व."),
               ("तपावनम्", "अः does not become आ before व."),
               ("तपर्वनम्", "Visarga after अ does not become र्.")],
              "स्रोतः + मुखम् → स्रोतोमुखम्; so तपः + वनम् → तपोवनम्.",
              "अः + voiced consonant → ओ + consonant."),
          "A visarga after short अ becomes ओ before a voiced consonant."),
    ],
}

# ---------------------------------------------------------------- unit 77
AUTHORED["77"] = {
    "title": "तदा संस्कारबाह्यं भवति",
    "question": "What does unit 77 say (it) then becomes, and which treatment (saṃskāra) does it list?",
    "rule": ("Then (it) becomes outside refining treatment (संस्कारबाह्य). There the treatment is: aphrodisiac (वाजीकर) enemas "
             "(बस्ति), eating (अभ्यवहार) and mind-gladdening (ones)."),
    "limits": ("The subject is not stated; the line does not say which case of unit 76 is beyond treatment, so no question asks it. "
               "चेतोहर्ष णानि is possibly one word, चेतोहर्षणानि, split by a stray space (the data flags it as possible); no question rests on it."),
    "explain_hi": ("यह इकाई ७६ के ‘यदा’ वाक्य का ‘तदा’ भाग है: तब वह संस्कार (शोधक उपचार) से बाहर हो जाता है। "
                   "फिर ‘तत्र संस्कारः’ से उपचार की सूची आती है: वाजीकर (पौरुष बढ़ाने वाली) बस्तियाँ यानी एनिमा, अभ्यवहार यानी खाना, और चित्त को हर्षित करने वाले। "
                   "कौन-सी दशा उपचार से बाहर है और किसमें उपचार है, यह पंक्ति साफ़ नहीं कहती। "
                   "छपा ‘चेतोहर्ष णानि’ सम्भवतः एक ही शब्द ‘चेतोहर्षणानि’ है, जिसमें बीच में भूल से जगह छूटी है।"),
    "hook": "तब संस्कार से बाहर; फिर संस्कार: वाजीकर बस्ति, भोजन, मन का हर्ष।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 77, what does (it) then become?",
            ("Outside refining treatment", "संस्कारबाह्यं भवति: it becomes outside saṃskāra."),
            [("Cured by fasting alone, in a few days", "Fasting is not named in this line."),
             ("Firm and full of strength", "The line says nothing of firmness here."),
             ("A disease of the eyes", "No eye disease is named in this line.")],
            "तदा संस्कारबाह्यं भवति: then (it) becomes outside (the scope of) refining treatment.",
            "बाह्य = outside; संस्कारबाह्य = outside saṃskāra."),
        order(1, "Put these phrases of unit 77 in their printed order.",
              ["तदा संस्कारबाह्यं भवति", "तत्र संस्कारः", "वाजीकरा बस्तयः", "अभ्यवहारः", "चेतोहर्ष णानि च"],
              "First the 'then' clause, then 'there the treatment is', then its three items: enemas, eating, gladdening ones.",
              "संस्कारबाह्य → तत्र संस्कारः → बस्ति → अभ्यवहार → चेतोहर्ष…"),
        T(match(2, "Match each word of unit 77 to its meaning on the card.",
                [["संस्कार", "refining treatment"], ["बाह्य", "outside"], ["वाजीकर", "aphrodisiac"],
                 ["बस्ति", "enema"], ["अभ्यवहार", "eating, swallowing"]],
                "These words carry the 'then' clause and two items of the treatment list.",
                "संस्कार = treatment; बाह्य = outside; वाजीकर = aphrodisiac; बस्ति = enema; अभ्यवहार = eating.", role="extend"),
          "संस्कारबाह्य is a tatpuruṣa: 'outside treatment'."),
        mcq("discriminate", 3, "Which split of बस्तयोऽभ्यवहारः is right?",
            ("बस्तयः + अभ्यवहारः", "अः + अ → ओऽ: the अ of अभ्यवहारः is shown by the avagraha."),
            [("बस्तयो + भ्यवहारः", "भ्यवहारः is not a word of the card."),
             ("बस्तय + अभ्यवहारः", "अ + अ would join as आ: बस्तयाभ्यवहारः."),
             ("बस्तयम् + अभ्यवहारः", "म् before a vowel would give बस्तयमभ्यवहारः.")],
            "बस्तयः (enemas) + अभ्यवहारः (eating): the visarga with अ becomes ओ and the next अ is dropped (ऽ).",
            "अः + अ → ओऽ."),
        multi("apply", 4, "Which two of these does unit 77 list in the treatment?",
              [("Bloodletting (रक्तमोक्षण)", "Bloodletting is not named in this line."),
               ("Aphrodisiac enemas (वाजीकरा बस्तयः)", "Right: वाजीकरा बस्तयः."),
               ("Fasting (उपवास)", "Fasting is not named in this line."),
               ("Eating, swallowing (अभ्यवहार)", "Right: अभ्यवहारः.")],
              [1, 3],
              "After तत्र संस्कारः the line names aphrodisiac enemas, eating, and gladdening (ones).",
              "वाजीकरा बस्तयः, अभ्यवहारः, चेतोहर्ष…"),
        T(mcq("transfer", 5, "By the rule of अभ्यवहारश्चेतो, how is रामः + चलति written when joined?",
              ("रामश्चलति", "Visarga before च becomes श्."),
              [("रामोचलति", "ओ comes only before a voiced sound; च is unvoiced."),
               ("रामचलति", "The visarga is not simply dropped before च."),
               ("रामस्चलति", "Before च the visarga becomes श्, not स्.")],
              "अभ्यवहारः + चेतः → अभ्यवहारश्चेतः; so रामः + चलति → रामश्चलति.",
              "Visarga + च/छ → श् + च/छ."),
          "A visarga before च or छ becomes श्."),
    ],
}

# ---------------------------------------------------------------- unit 78
AUTHORED["78"] = {
    "title": "तानि हि शुक्रे बलमादधानानि",
    "question": "Why, by unit 78, do 'these' (तानि) help: what do they put into the semen and what do they nourish?",
    "rule": ("For these (the treatments just listed), putting strength into the semen (शुक्र), nourish its channels (srotas)."),
    "limits": ("तानि (these) refers to the things listed in unit 77, as the data notes. अस्य most naturally means 'its' "
               "(of the semen) but could mean 'his', so no question rests on whose channels. The closing इति is not translated."),
    "explain_hi": ("‘हि’ (क्योंकि) से यह इकाई कारण बताती है: वे (इकाई ७७ के उपचार) शुक्र यानी वीर्य में बल डालते हुए उसके स्रोतों (वाहिनियों) को पुष्ट करते हैं। "
                   "‘आदधानानि’ आ-√धा का आत्मनेपद वर्तमान कृदन्त है: ‘रखते हुए, देते हुए’। "
                   "‘अस्य’ का अर्थ ‘इसका’ (शुक्र का) सबसे स्वाभाविक है, पर ‘उसका’ भी हो सकता है। "
                   "अन्त का ‘इति’ कथन को बंद करता है।"),
    "hook": "शुक्र में बल, स्रोतों को पोषण: इसीलिए वे उपचार।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 78, into what do 'these' put strength?",
            ("Into the semen (शुक्र)", "शुक्रे बलमादधानानि: putting strength into the semen."),
            [("Into the blood (śoṇita)", "Blood is not named in this line."),
             ("Into the bones (asthi)", "Bones are not named in this line."),
             ("Into the digestive fire (agni)", "Digestion is not named in this line.")],
            "शुक्रे (locative: in the semen) बलम् (strength) आदधानानि (putting).",
            "शुक्रे = in the semen; बलम् आदधानानि = putting strength."),
        order(1, "Put these pieces of unit 78 in their printed order.",
              ["तानि हि", "शुक्रे", "बलमादधानानि", "स्रोतांस्यस्य", "आप्याययंतीति"],
              "For these, in the semen, putting strength, its channels, nourish (iti).",
              "तानि हि → शुक्रे → बलमादधानानि → स्रोतांस्यस्य → आप्याययंतीति."),
        T(fill(2, "The word for semen in unit 78 (stem form) is ____ (type it in Devanagari or in English letters, e.g. dharma).",
               accepts("शुक्र", None, "शुक्रे"),
               "शुक्र = semen (standard); the line has the locative शुक्रे, 'in the semen'.",
               "शुक्र is semen; शुक्रे is its locative.", "शुक्र = semen."),
          "शुक्र means semen; the locative शुक्रे means 'in the semen'."),
        mcq("discriminate", 3, "Which split of स्रोतांस्यस्य is right?",
            ("स्रोतांसि + अस्य", "इ before a different vowel becomes य्: स्रोतांस्य् + अस्य."),
            [("स्रोतः + अस्य", "अः + अ would give स्रोतोऽस्य."),
             ("स्रोतांसि + यस्य", "That would stay स्रोतांसियस्य; यस्य is not on the card."),
             ("स्रोतांस्य + अस्य", "अ + अ would join as आ: स्रोतांस्यास्य.")],
            "स्रोतांसि (channels, acc. pl.) + अस्य (its): इ + अ → य.",
            "इ + a different vowel → य् + that vowel."),
        multi("apply", 4, "Which two does unit 78 say 'these' do?",
              [("Put strength into the semen", "Right: शुक्रे बलमादधानानि."),
               ("Nourish the channels (srotas)", "Right: स्रोतांसि … आप्याययन्ति."),
               ("Close the channels", "Closing the channel's mouth is unit 76's harm, not this help."),
               ("Dry up the semen", "The line says they give the semen strength.")],
              [0, 1],
              "They put strength into the semen and nourish the channels (srotas).",
              "बलम् आदधानानि; स्रोतांसि आप्याययन्ति."),
        T(mcq("transfer", 5, "By the rule of स्रोतांस्यस्य, how is अति + अन्तम् written when joined?",
              ("अत्यन्तम्", "इ before अ becomes य्."),
              [("अतीन्तम्", "इ + अ does not give ई."),
               ("अत्यान्तम्", "Only the य् is added; the अ stays short."),
               ("अतेन्तम्", "इ + अ does not give ए.")],
              "स्रोतांसि + अस्य → स्रोतांस्यस्य; so अति + अन्तम् → अत्यन्तम्.",
              "इ + अ → य."),
          "A final इ before a different vowel becomes य्."),
    ],
}

# ---------------------------------------------------------------- unit 79
AUTHORED["79"] = {
    "title": "यदाऽल्पबीजोऽल्पबलः पुमान्",
    "question": "Which man does unit 79 describe, and what does he cause?",
    "rule": ("When a man of little seed, little strength, agitated, with aversion to women, or desiring another, causes an "
             "obstruction of intercourse with the woman, or (on the possible reading तद्विधा for printed तद्दिधा) the woman is of that kind towards the man: the 'when' half."),
    "limits": ("The 'then' result is in unit 80. The printed तद्दिधा is not a word (possibly तद्विधा, 'of that kind'; the data flags it as possible); "
               "no question rests on it. The last clause is elliptical: 'is' is supplied and पुंसः is read 'towards the man'."),
    "explain_hi": ("यह गद्य-पंक्ति ‘यदा’ वाला भाग है; ‘तदा’ वाला फल इकाई ८० में आता है। "
                   "पुरुष के पाँच विशेषण हैं: अल्प बीज वाला, अल्प बल वाला, उद्विग्न, स्त्री से द्वेष रखने वाला, या किसी अन्य की कामना करने वाला। "
                   "ऐसा पुरुष स्त्री के साथ मैथुन में रुकावट करता है; या (सम्भावित पाठ ‘तद्विधा’ पर) स्त्री भी पुरुष के प्रति वैसी ही हो। "
                   "‘अल्पबीज’, ‘अल्पबल’, ‘अन्यकाम’ बहुव्रीहि हैं: जिसका बीज अल्प हो, आदि।"),
    "hook": "कम बीज, कम बल, उद्वेग, स्त्री-द्वेष, अन्य-काम: मैथुन में रुकावट।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 79, what does such a man cause?",
            ("An obstruction of intercourse", "व्यवायप्रतिघातं करोति: he causes an obstruction of intercourse."),
            [("A quarrel over the household property", "Property is not named in this line."),
             ("An early conception", "The line speaks of obstruction, not conception."),
             ("A fever in the woman", "No fever is named in this line.")],
            "नार्या व्यवायप्रतिघातं करोति: he causes an obstruction (प्रतिघात) of intercourse (व्यवाय).",
            "व्यवाय = intercourse; प्रतिघात = obstruction."),
        order(1, "Put the man's qualities in unit 79's printed order.",
              ["अल्पबीजः", "अल्पबलः", "उद्वेगः", "स्त्रीद्वेषयुक्तः", "अन्यकामः"],
              "Little seed, little strength, agitated, with aversion to women, or desiring another.",
              "बीज → बल → उद्वेग → स्त्रीद्वेष → अन्यकाम."),
        T(match(2, "Match each quality of unit 79 to its meaning.",
                [["अल्पबीज", "of little seed"], ["अल्पबल", "of little strength"], ["उद्वेग", "agitated, anxious"],
                 ["स्त्रीद्वेषयुक्त", "with aversion to women"], ["अन्यकाम", "desiring another"]],
                "The five qualities of the man, as the card glosses them.",
                "अल्प = little; द्वेष = aversion; अन्य = other; काम = desire.", role="extend"),
          "अल्पबीज is a bahuvrīhi: 'he whose seed is little'."),
        mcq("discriminate", 3, "Which split of अल्पबीजोऽल्पबलः is right?",
            ("अल्पबीजः + अल्पबलः", "अः + अ → ओऽ: the second अ is dropped and shown by ऽ."),
            [("अल्पबीजो + अल्पबलः", "ओ is the result of the join, not the word's own ending."),
             ("अल्पबीज + अल्पबलः", "अ + अ would join as आ: अल्पबीजाल्पबलः."),
             ("अल्पबीजम् + अल्पबलः", "म् before a vowel would give अल्पबीजमल्पबलः.")],
            "अल्पबीजः (of little seed) + अल्पबलः (of little strength).",
            "अः + अ → ओऽ."),
        multi("apply", 4, "Which two qualities of the man does unit 79 name?",
              [("Of great seed", "The line says अल्पबीज, of little seed."),
               ("Of little strength", "Right: अल्पबलः."),
               ("Very old in years", "Age is not named in this line."),
               ("With aversion to women", "Right: स्त्रीद्वेषयुक्तः.")],
              [1, 3],
              "Among the five: little seed, little strength, agitated, aversion to women, desiring another.",
              "अल्पबलः; स्त्रीद्वेषयुक्तः."),
        T(mcq("transfer", 5, "By the rule of अल्पबीजोऽल्पबलः, how is कः + अपि written when joined?",
              ("कोऽपि", "अः + अ → ओऽ."),
              [("कापि", "अः + अ does not give आ."),
               ("कअपि", "The two sounds must join; अः + अ gives ओऽ."),
               ("करपि", "Visarga after अ does not become र् here.")],
              "अल्पबीजः + अल्पबलः → अल्पबीजोऽल्पबलः; so कः + अपि → कोऽपि.",
              "अः + अ → ओऽ."),
          "A visarga after अ, before अ, gives ओ and the next अ is dropped (ऽ)."),
    ],
}

# ---------------------------------------------------------------- unit 80
AUTHORED["80"] = {
    "title": "तदाऽऽसेक्यं स्त्रीपुंसौ",
    "question": "What does unit 80 say of the man and woman, and of the vakradhvaja?",
    "rule": ("Then āsekya (a name the line does not define). The woman and the man become of that kind. Then he becomes "
             "vakradhvaja (with a bent dhvaja, the penis); his dhvaja is not made stiff at all."),
    "limits": ("Low confidence. आसेक्य is left untranslated: the line does not define it and its case is unclear, so no "
               "question rests on it. That it names a kind of ṣaṇḍha is only probable, from parallel works. The clauses have no stated subject."),
    "explain_hi": ("विश्वास कम। यह सम्भवतः इकाई ७९ के ‘यदा’ वाक्य का ‘तदा’ भाग है। ‘आसेक्य’ एक पारिभाषिक नाम लगता है, पर पंक्ति इसे समझाती नहीं, इसलिए यह बिना अनुवाद रखा गया है; "
                   "यह षण्ढ (नपुंसक) का एक प्रकार है, यह केवल दूसरे ग्रन्थों की समान सूचियों से सम्भावित है। "
                   "फिर: स्त्री और पुरुष वैसे ही हो जाते हैं। तब वह वक्रध्वज यानी टेढ़े ध्वज (शिश्न) वाला होता है; उसका ध्वज बिलकुल कड़ा नहीं होता। "
                   "‘ध्वज’ (झंडा) शिश्न के लिए प्रयुक्त शिष्ट शब्द है।"),
    "hook": "वक्रध्वज: ध्वज टेढ़ा, और कड़ा नहीं।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 80, what is said of his dhvaja (penis)?",
            ("It is not made stiff at all", "नैव ध्वजस्तभ्यते: his dhvaja is not made stiff at all."),
            [("It is made stiff by eating rich food", "Eating is not named in this line."),
             ("It is stiff only at night", "No time is named in this line."),
             ("It is cut off in the embryo", "No cutting is named in this line.")],
            "तस्य नैव ध्वजः स्तभ्यते: his dhvaja is not made stiff at all.",
            "स्तभ्यते = is made stiff; न एव = not at all."),
        order(1, "Put these clauses of unit 80 in their printed order.",
              ["तदाऽऽसेक्यं", "स्त्रीपुंसौ तद्विधौ भवतः", "तदा वक्रध्वजो भवति", "तस्य नैव ध्वजस्तभ्यते"],
              "Then āsekya; the woman and man become of that kind; then he becomes vakradhvaja; his dhvaja is not stiffened.",
              "आसेक्य → स्त्रीपुंसौ → वक्रध्वज → नैव स्तभ्यते."),
        T(match(2, "Match each word of unit 80 to its meaning on the card.",
                [["स्त्रीपुंसौ", "woman and man"], ["तद्विध", "of that kind"], ["वक्र", "bent"],
                 ["ध्वज", "banner, i.e. the penis"], ["स्तभ्यते", "is made stiff"]],
                "These five words carry the sure clauses of the unit.",
                "स्त्रीपुंसौ (dvandva, dual); तद्विध; वक्र; ध्वज; स्तभ्यते.", role="extend"),
          "स्त्रीपुंसौ is a dvandva in the dual: 'the woman and the man'."),
        mcq("discriminate", 3, "Which split of नैव is right?",
            ("न + एव", "अ + ए → ऐ: न + एव → नैव."),
            [("न + इव", "अ + इ would give ए: नेव."),
             ("नै + व", "नै and व are not words of the card."),
             ("ने + एव", "ए + ए would not give ऐ.")],
            "न (not) + एव (indeed): 'not at all'.",
            "अ + ए → ऐ."),
        mcq("apply", 4, "On the card, what does the bahuvrīhi वक्रध्वज describe?",
            ("One whose dhvaja is bent", "A bahuvrīhi names the owner: 'he whose dhvaja is bent'."),
            [("A bent banner on a pole", "Here ध्वज is the euphemism for the penis, and the word names a person."),
             ("A woman of that kind", "The line says 'he becomes' vakradhvaja."),
             ("A cure for a bent dhvaja given to the man", "No cure is named in this line.")],
            "वक्र (bent) + ध्वज (penis), read as a bahuvrīhi naming a type of man.",
            "Bahuvrīhi = 'one who has X': वक्रध्वज = one with a bent dhvaja."),
        T(mcq("transfer", 5, "By the rule of नैव, how is तत्र + एव written when joined?",
              ("तत्रैव", "अ + ए → ऐ."),
              [("तत्रेव", "अ + ए does not give ए."),
               ("तत्रयेव", "No य् is put in after अ."),
               ("तत्राएव", "अ + ए is not written as आ + ए.")],
              "न + एव → नैव; so तत्र + एव → तत्रैव.",
              "अ/आ + ए/ऐ → ऐ."),
          "अ or आ before ए merges into ऐ."),
    ],
}

# ---------------------------------------------------------------- unit 81
AUTHORED["81"] = {
    "title": "यदा पूतियोन्याः",
    "question": "Of which woman does unit 81 say an embryo (garbha) arises?",
    "rule": ("When an embryo (गर्भ) arises of a woman with a putrid (पूति) vagina (योनि): the 'when' half; the result is in unit 82."),
    "limits": ("Printed स्त्रिया before गर्भो may be the genitive स्त्रियाः by regular sandhi (आः + voiced consonant → आ) or an "
               "instrumental; the card follows the genitive, beside पूतियोन्याः, and no question rests on the case. "
               "पूति means putrid or foul-smelling; the line does not say which."),
    "explain_hi": ("यह छोटी गद्य-पंक्ति ‘यदा’ वाला भाग है; इसका फल इकाई ८२ में है। "
                   "जब पूतियोनि (दुर्गन्धयुक्त या सड़ी योनि वाली) स्त्री का गर्भ होता है। "
                   "‘पूतियोनि’ बहुव्रीहि है: जिसकी योनि पूति हो। "
                   "छपा ‘स्त्रिया’ (गर्भो से पहले) नियमित सन्धि से षष्ठी ‘स्त्रियाः’ हो सकता है (आः + घोष व्यंजन → आ), तृतीया भी; अनुवाद षष्ठी मानता है।"),
    "hook": "पूतियोनि स्त्री का गर्भ: फल अगली पंक्ति में।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 81, what is said of the woman's yoni?",
            ("It is putrid, foul", "पूतियोन्याः: of one whose yoni is putrid."),
            [("It is dry and closed at the mouth", "Dryness is not named in this line."),
             ("It bleeds heavily each month", "Bleeding is not named in this line."),
             ("It is wide and open", "Width is not named in this line.")],
            "पूति = putrid or foul-smelling; the line does not say which.",
            "पूतियोनि = she whose yoni is putrid."),
        order(1, "Put the words of unit 81 in their printed order.",
              ["यदा", "पूतियोन्याः", "स्त्रिया", "गर्भो", "भवति"],
              "When, of the putrid-yoni, woman, an embryo, arises.",
              "यदा → पूतियोन्याः → स्त्रिया → गर्भो → भवति."),
        T(fill(2, "The word for embryo in unit 81 (stem form) is ____ (type it in Devanagari or in English letters, e.g. dharma).",
               accepts("गर्भ", None, "गर्भः", "गर्भो"),
               "गर्भ = embryo, fetus; printed गर्भो before भवति.",
               "गर्भ is the embryo.", "गर्भ = embryo."),
          "गर्भ means the embryo or fetus."),
        match(3, "Match each word of unit 81 to its meaning on the card.",
              [["यदा", "when"], ["पूति", "putrid, foul"], ["योनि", "vagina"], ["गर्भ", "embryo"], ["भवति", "arises"]],
              "Five words carry the 'when' clause.",
              "यदा; पूति; योनि; गर्भ; भवति.", role="discriminate"),
        mcq("apply", 4, "Which split of गर्भो भवति is right?",
            ("गर्भः + भवति", "अः before a voiced consonant (भ) becomes ओ."),
            [("गर्भा + भवति", "गर्भा is not the form; आ would not turn into ओ."),
             ("गर्भम् + भवति", "म् before भ would give गर्भं भवति."),
             ("गर्भे + भवति", "ए before a consonant stays ए.")],
            "गर्भः (embryo, nom. sg.) + भवति (arises).",
            "अः + voiced consonant → ओ."),
        T(mcq("transfer", 5, "By the rule of गर्भो भवति, how is बालः + गच्छति written?",
              ("बालो गच्छति", "अः before the voiced ग becomes ओ."),
              [("बालस् गच्छति", "Visarga becomes स् only before त or थ."),
               ("बालर् गच्छति", "Visarga after अ does not become र्."),
               ("बाला गच्छति", "अः does not become आ before ग.")],
              "गर्भः + भवति → गर्भो भवति; so बालः + गच्छति → बालो गच्छति.",
              "अः + voiced consonant → ओ."),
          "A visarga after short अ becomes ओ before a voiced consonant."),
    ],
}

# ---------------------------------------------------------------- unit 82
AUTHORED["82"] = {
    "title": "तच्छुक्रास्वादात्",
    "question": "From what, by unit 82, does he get the raising of the dhvaja (penis)?",
    "rule": "From tasting that semen (शुक्र) he gets the raising (उच्छ्राय) of the dhvaja (penis): this appears to be the result of unit 81.",
    "limits": ("The subject 'he' is not stated, and 'that' semen is not explained in the line. उच्छ्राय as erection is "
               "probable. The print keeps आस्वादात् unjoined before ध्वज (a print habit)."),
    "explain_hi": ("यह सम्भवतः इकाई ८१ के वाक्य का फल है: उस शुक्र के आस्वाद से वह ध्वज (शिश्न) का उठना पाता है। "
                   "कर्ता ‘वह’ छपा नहीं है, और ‘उस’ शुक्र से क्या अभिप्रेत है, यह पंक्ति नहीं बताती। "
                   "‘उच्छ्राय’ यानी उठना; उत्थान अर्थ सम्भावित है। "
                   "छपाई ने ‘आस्वादात् ध्वज’ में त् को द् नहीं किया; नियम से ‘आस्वादाद्ध्वज’ होता।"),
    "hook": "उस शुक्र का आस्वाद, तब ध्वज का उठना।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 82, from what does he get the raising of the dhvaja?",
            ("From tasting that semen", "तच्छुक्रास्वादात्: from the tasting of that semen."),
            [("From the smell of flowers", "Smell is not named in this line."),
             ("From eating rich food", "Food is not named in this line."),
             ("From long sleep", "Sleep is not named in this line.")],
            "तत् (that) शुक्र (semen) आस्वादात् (from tasting), ablative of cause.",
            "आस्वादात् = from tasting."),
        order(1, "Put the parts of unit 82 in their printed order.",
              ["तत्", "शुक्र", "आस्वादात्", "ध्वजोच्छ्रायम्", "लभते"],
              "That, semen, from tasting, raising of the dhvaja, he obtains.",
              "तत् → शुक्र → आस्वादात् → ध्वजोच्छ्रायम् → लभते."),
        T(match(2, "Match each word of unit 82 to its meaning on the card.",
                [["आस्वाद", "tasting"], ["शुक्र", "semen"], ["ध्वज", "banner, i.e. the penis"],
                 ["उच्छ्राय", "raising (erection, probable)"], ["लभते", "obtains"]],
                "Five words carry the whole line.",
                "आस्वाद; शुक्र; ध्वज; उच्छ्राय; लभते.", role="extend"),
          "आस्वादात् is ablative: 'from tasting', the cause."),
        mcq("discriminate", 3, "Which split of तच्छुक्र is right?",
            ("तत् + शुक्र", "त् + श → च्श, optionally च्छ before a vowel or semivowel (the print has च्छ): तत् + शुक्र → तच्छुक्र."),
            [("तच् + छुक्र", "छुक्र is not a word of the card."),
             ("तत् + छुक्र", "छुक्र is not a word of the card."),
             ("तम् + शुक्र", "म् before श would give तंशुक्र.")],
            "तत् (that) + शुक्र (semen): त् before श becomes च्, and श after it may become छ (before a vowel or semivowel).",
            "त् + श → च्श, optionally च्छ before a vowel or semivowel (the print has च्छ)."),
        mcq("apply", 4, "The print leaves आस्वादात् ध्वज unjoined; what would the regular join be?",
            ("आस्वादाद्ध्वज", "त् before a voiced consonant (ध) becomes द्."),
            [("आस्वादान्ध्वज", "त् may become न् (optionally) only before a nasal."),
             ("आस्वादाच्ध्वज", "त् becomes च् only before च/छ/श."),
             ("आस्वादाध्वज", "The त् does not simply drop.")],
            "The data notes the final t was not changed to d; regular sandhi gives आस्वादाद्ध्वज.",
            "त् + voiced consonant → द्."),
        T(mcq("transfer", 5, "By the rule of ध्वजोच्छ्राय, how is सूर्य + उदयः written when joined?",
              ("सूर्योदयः", "अ + उ → ओ."),
              [("सूर्यौदयः", "अ + उ gives ओ, not औ."),
               ("सूर्युदयः", "The अ does not drop before उ."),
               ("सूर्यवुदयः", "No व् is put in after अ.")],
              "ध्वज + उच्छ्रायम् → ध्वजोच्छ्रायम्; so सूर्य + उदयः → सूर्योदयः.",
              "अ + उ → ओ."),
          "अ or आ before उ or ऊ merges into ओ."),
    ],
}

# ---------------------------------------------------------------- unit 83
AUTHORED["83"] = {
    "title": "योनिध्वजगंधेन बलं लभते",
    "question": "In the sure part of unit 83, from what does he obtain strength?",
    "rule": ("From the smell of yoni and dhvaja (योनिध्वजगन्धेन; read as 'of the yoni and the dhvaja', 'of the dhvaja of the "
             "yoni' also possible) he obtains strength (बलम्). The two printed words before it are unclear."),
    "limits": ("Low confidence. पुमुरुभावपि and तत्सौगंधिकारण्यं are doubtful in print; no question rests on them. "
               "The compound may be a dvandva or not, so no question asks it. बल is strength, not erection. "
               "Saugandhika as a ṣaṇḍha kind is only probable."),
    "explain_hi": ("विश्वास कम। इस पंक्ति के दूसरे और तीसरे छपे शब्द (पुमुरुभावपि, तत्सौगंधिकारण्यं) अस्पष्ट हैं; उन पर कोई पक्का पाठ नहीं बनाया गया। "
                   "पक्का भाग है: योनि और ध्वज (शिश्न) की गन्ध से वह बल पाता है। "
                   "छपे अक्षरों में ‘सौगन्धिक’ दिखता है, जो दूसरे ग्रन्थों में षण्ढ का एक प्रकार है; यहाँ यह केवल सम्भावित पहचान है। "
                   "‘बल’ का अर्थ यहाँ बल ही है; पंक्ति ‘उत्थान’ नहीं कहती।"),
    "hook": "गन्ध से बल: पक्का भाग इतना ही।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By the sure part of unit 83, what does he obtain?",
            ("Strength", "बलं लभते: he obtains strength."),
            [("The raising of the dhvaja", "That is unit 82's result; this line says बल, strength."),
             ("A son", "No son is named in this line."),
             ("Freedom from fever", "No fever is named in this line.")],
            "योनिध्वजगन्धेन बलं लभते: from the smell he obtains strength; the line does not say erection.",
            "बलम् = strength; लभते = obtains."),
        order(1, "Put these words of unit 83 in their printed order (the two unclear words are left out).",
              ["यदा", "योनिध्वजगंधेन", "बलं", "लभते"],
              "When … from the smell of yoni and dhvaja, strength, he obtains.",
              "यदा → योनिध्वजगंधेन → बलं → लभते."),
        T(match(2, "Match each word of unit 83's sure part to its meaning.",
                [["योनि", "vagina"], ["ध्वज", "banner, i.e. the penis"], ["गन्ध", "smell"], ["बल", "strength"],
                 ["लभते", "obtains"]],
                "These five words make the sure part of the line.",
                "योनि; ध्वज; गन्ध; बल; लभते.", role="extend"),
          "ध्वज (banner) is a standard euphemism for the penis."),
        mcq("discriminate", 3, "Which words of unit 83 does the card call doubtful in print?",
            ("पुमुरुभावपि and तत्सौगंधिकारण्यं", "The second and third words are doubtful; no firm reading is built on them."),
            [("योनिध्वजगंधेन and बलं", "These are the sure part of the line."),
             ("यदा and लभते", "These are clear: 'when' and 'obtains'."),
             ("बलं and लभते", "These are clear: 'strength' and 'obtains'.")],
            "Only पुमुरुभावपि and तत्सौगंधिकारण्यं are unclear; the rest of the line is sure.",
            "Doubtful: words 2 and 3; sure: यदा … योनिध्वजगन्धेन बलं लभते."),
        mcq("apply", 4, "In योनिध्वजगन्धेन, what does the ending -एन show?",
            ("Instrumental: by, from (the smell)", "-एन is the instrumental singular of an अ-stem."),
            [("Locative: in, within (the smell)", "The locative singular would be गन्धे."),
             ("Genitive: of (the smell)", "The genitive singular would be गन्धस्य."),
             ("Dative: for (the smell)", "The dative singular would be गन्धाय.")],
            "गन्धेन = by/from the smell: the smell is the means of the strength.",
            "अ-stem: -एन instrumental, -स्य genitive, -ए locative, -आय dative."),
        T(mcq("transfer", 5, "By the rule of गन्धेन, which form of औषध means by the medicine?",
              ("औषधेन", "-एन is the instrumental singular of an अ-stem."),
              [("औषधस्य", "That is the genitive: 'of the medicine'."),
               ("औषधे", "That is the locative: 'in the medicine'."),
               ("औषधाय", "That is the dative: 'for the medicine'.")],
              "गन्ध → गन्धेन (by the smell); so औषध → औषधेन (by the medicine).",
              "अ-stem + -एन = instrumental singular."),
          "An अ-stem noun takes -एन in the instrumental singular ('by, with, from')."),
    ],
}

# ---------------------------------------------------------------- unit 84
AUTHORED["84"] = {
    "title": "यदा त्वीर्ष्याभिभूतौ",
    "question": "When, by unit 84, does the name īrṣyālu apply, and what brings on his engagement in intercourse?",
    "rule": ("When the two, overcome by jealousy and of little delight, are joined, then the name īrṣyālu (jealous one); "
             "his engagement in intercourse arises on seeing another coupled."),
    "limits": ("Two printed lines; the first has no verb after संज्ञाम्. पर may mean another or merely, so no question rests on it. "
               "That line 2 describes the īrṣyālu is the data's reading. īrṣyālu as a ṣaṇḍha kind is only probable."),
    "explain_hi": ("इस इकाई में दो छपी पंक्तियाँ हैं। पहली: जब ईर्ष्या से अभिभूत और मन्द हर्ष वाले दोनों संयुक्त होते हैं, तब ‘ईर्ष्यालु’ यह संज्ञा; "
                   "‘संज्ञाम्’ के बाद कोई क्रिया नहीं छपी। "
                   "दूसरी: उसकी, दूसरे को मिथुन बना हुआ (संयुक्त) देखकर, मैथुन में प्रवृत्ति होती है। "
                   "‘परम्’ को ‘दूसरे को’ पढ़ा गया है; ‘केवल’ अर्थ भी असम्भव नहीं। ‘दृष्ट्वा’ (देखकर) √दृश् का क्त्वा-रूप है।"),
    "hook": "ईर्ष्या, मन्द हर्ष: ईर्ष्यालु; दूसरे को मिथुन देखकर प्रवृत्ति।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 84, what name is given?",
            ("Īrṣyālu", "तदेर्ष्यालुरिति संज्ञां: then the name 'īrṣyālu'."),
            [("Vakradhvaja", "Vakradhvaja is named in unit 80, not here."),
             ("Vāyupiṇḍaka", "Vāyupiṇḍaka is named in unit 85."),
             ("Āsekya", "Āsekya is printed in unit 80.")],
            "The name is ईर्ष्यालु, 'the jealous one', from ईर्ष्या (jealousy).",
            "ईर्ष्या = jealousy; ईर्ष्यालु = jealous one."),
        order(1, "Put these phrases of unit 84 in their printed order.",
              ["यदा त्वीर्ष्याभिभूतौ", "मंदहर्षौ संसृज्येते", "तदेर्ष्यालुरिति संज्ञां", "तस्य परं मिथुनीभूतं दृष्ट्वा",
               "मैथुनप्रवृत्तिर्भवति"],
              "Overcome by jealousy, of little delight, are joined; then the name īrṣyālu; on seeing (one) coupled, engagement arises.",
              "ईर्ष्याभिभूतौ → मन्दहर्षौ → ईर्ष्यालु → दृष्ट्वा → प्रवृत्ति."),
        T(match(2, "Match each word of unit 84 to its meaning on the card.",
                [["ईर्ष्या", "jealousy"], ["अभिभूत", "overcome"], ["मन्दहर्ष", "of little delight"],
                 ["संसृज्येते", "(the two) are joined"], ["दृष्ट्वा", "having seen"]],
                "These five words carry the two lines.",
                "ईर्ष्या; अभिभूत; मन्दहर्ष; संसृज्येते (dual passive); दृष्ट्वा (absolutive).", role="extend"),
          "दृष्ट्वा is the absolutive of √दृश्: 'having seen'."),
        mcq("discriminate", 3, "Which split of तदेर्ष्यालुः is right?",
            ("तदा + ईर्ष्यालुः", "आ + ई → ए."),
            [("तदा + एर्ष्यालुः", "आ + ए would give ऐ: तदैर्ष्यालुः."),
             ("तद् + एर्ष्यालुः", "एर्ष्यालुः is not a word of the card."),
             ("तदे + ईर्ष्यालुः", "तदे is not a word of the card.")],
            "तदा (then) + ईर्ष्यालुः (jealous one): आ and ई merge into ए.",
            "अ/आ + इ/ई → ए."),
        multi("apply", 4, "Which two does unit 84 say of the two who are joined?",
              [("Overcome by jealousy", "Right: ईर्ष्याभिभूतौ."),
               ("Full of great joy", "The line says मन्दहर्षौ, of little delight."),
               ("Kept apart from each other", "The line says they are joined (संसृज्येते)."),
               ("Of little delight", "Right: मन्दहर्षौ.")],
              [0, 3],
              "The two are overcome by jealousy (ईर्ष्याभिभूतौ) and of little delight (मन्दहर्षौ).",
              "ईर्ष्याभिभूतौ; मन्दहर्षौ (both dual)."),
        T(mcq("transfer", 5, "By the rule of तदेर्ष्यालुः, how is महा + ईशः written when joined?",
              ("महेशः", "आ + ई → ए."),
              [("महैशः", "आ + ई gives ए, not ऐ."),
               ("महीशः", "The आ does not drop before ई."),
               ("महाईशः", "The two vowels must merge.")],
              "तदा + ईर्ष्यालुः → तदेर्ष्यालुः; so महा + ईशः → महेशः.",
              "आ + ई → ए."),
          "अ or आ before इ or ई merges into ए."),
    ],
}

# ---------------------------------------------------------------- unit 85
AUTHORED["85"] = {
    "title": "यदा पुरुषस्य गर्भस्य",
    "question": "What, by unit 85, destroys the testes of the male embryo, and what is the result called?",
    "rule": ("When the testes (वृषण) of the male embryo are destroyed through the fault of wind (vāyu) and fire (agni), "
             "then (it) becomes the one called vāyupiṇḍaka."),
    "limits": ("दोष is read 'fault' here, not the humour, because it is compounded with vāyu and agni. Whether one or both "
               "testes is not marked in the compound. वायुपिण्डक is a type name, left untranslated; the subject of भवति is not stated."),
    "explain_hi": ("जब पुरुष गर्भ (नर गर्भ) के वृषण यानी अण्डकोष वायु और अग्नि के दोष से नष्ट हो जाते हैं, तब वह ‘वायुपिण्डक’ नाम वाला होता है। "
                   "यहाँ ‘दोष’ का अर्थ ‘दोष, खराबी’ लिया गया है, त्रिदोष वाला अर्थ नहीं, क्योंकि यह वायु और अग्नि के साथ समास में है। "
                   "‘वायुपिण्डक’ एक प्रकार का नाम है, इसका अनुवाद नहीं किया गया। "
                   "‘दोषात्’ पञ्चमी है: कारण बताती है।"),
    "hook": "वायु-अग्नि का दोष, वृषण-नाश: वायुपिण्डक।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 85, what is destroyed in the male embryo?",
            ("The testes (वृषण)", "वृषणनाशः: destruction of the testes."),
            [("The heart (hṛdaya)", "The heart is not named in this line."),
             ("The eyes", "The eyes are not named in this line."),
             ("The navel cord (nābhi-nāḍī)", "The navel cord is not named in this line.")],
            "वृषण = testis (standard); नाश = destruction.",
            "वृषणनाश = destruction of the testes."),
        order(1, "Put these pieces of unit 85 in their printed order.",
              ["यदा पुरुषस्य गर्भस्य", "वाय्वग्निदोषात्", "वृषणनाशः", "तदा", "वायुपिंडकाख्यं भवति"],
              "When, of the male embryo, through the fault of wind and fire, destruction of the testes, then, (it) becomes the one called vāyupiṇḍaka.",
              "गर्भस्य → वाय्वग्निदोषात् → वृषणनाशः → तदा → वायुपिण्डकाख्यम्."),
        T(match(2, "Match each word of unit 85 to its meaning on the card.",
                [["वायु", "wind"], ["अग्नि", "fire"], ["दोष", "fault (here)"], ["वृषण", "testis"], ["नाश", "destruction"]],
                "Five words carry the cause and the harm.",
                "वायु; अग्नि; दोष (fault); वृषण; नाश.", role="extend"),
          "Here दोष, compounded with vāyu and agni, is read 'fault', not the humour."),
        mcq("discriminate", 3, "Which split of वाय्वग्नि is right?",
            ("वायु + अग्नि", "उ before a different vowel becomes व्."),
            [("वायुः + अग्नि", "उः + अ would give वायुरग्नि."),
             ("वाय्व + अग्नि", "अ + अ would join as आ: वाय्वाग्नि."),
             ("वाय् + वग्नि", "वग्नि is not a word of the card.")],
            "वायु (wind) + अग्नि (fire): उ + अ → व.",
            "उ + a different vowel → व् + that vowel."),
        mcq("apply", 4, "By unit 85, whose testes are destroyed?",
            ("Those of the male embryo", "पुरुषस्य गर्भस्य: of the male embryo."),
            [("Those of the father", "The line speaks of the embryo, not the father."),
             ("Those of an old man", "Age is not named in this line."),
             ("Those of the vāyupiṇḍaka's son", "No son is named in this line.")],
            "पुरुषस्य गर्भस्य is read 'of the male embryo'; the genitive carries 'in'.",
            "पुरुष गर्भ = male embryo."),
        T(mcq("transfer", 5, "By the rule of वाय्वग्नि, how is सु + आगतम् written when joined?",
              ("स्वागतम्", "उ before आ becomes व्."),
              [("सुआगतम्", "The two vowels must join."),
               ("सोगतम्", "उ + आ does not give ओ."),
               ("सूगतम्", "उ + आ does not give ऊ.")],
              "वायु + अग्नि → वाय्वग्नि; so सु + आगतम् → स्वागतम्.",
              "उ + a different vowel → व्."),
          "A final उ before a different vowel becomes व्."),
    ],
}

# ---------------------------------------------------------------- unit 86
AUTHORED["86"] = {
    "title": "एताः कर्मवैचित्र्यादष्टौ",
    "question": "How many ṣaṇḍha-yonis does unit 86 count, and from what cause are they said to be mixed?",
    "rule": "These eight kinds (योनि) of ṣaṇḍha (the impotent), because of the variety of action (कर्म), are said to be mixed (संकीर्ण).",
    "limits": ("The unit does not list the eight; which earlier types make up the eight is not stated here, so no question "
               "rests on it. संकीर्ण may also mean 'miscellaneous'. योनि is read 'kind, origin' here."),
    "explain_hi": ("यह गद्य-पंक्ति सार बताती है: ये आठ षण्ढ-योनियाँ, यानी नपुंसकों की आठ प्रकार की उत्पत्तियाँ, कर्म की विचित्रता से संकीर्ण (मिश्रित) कही गई हैं। "
                   "आठ कौन-से हैं, यह यहाँ गिनाया नहीं गया। "
                   "‘अष्टौ’ के अन्त में ‘-औ’ है, फिर भी यह द्विवचन नहीं: यह ‘आठ’ संख्या का प्रथमा रूप है। "
                   "‘संकीर्ण’ का अर्थ ‘फुटकर, विविध’ भी हो सकता है।"),
    "hook": "आठ षण्ढ-योनियाँ: कर्म की विचित्रता से मिश्रित।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 86, how many ṣaṇḍha-yonis are there?",
            ("Eight (अष्टौ)", "अष्टौ षण्ढयोनयः: eight kinds of ṣaṇḍha."),
            [("Five (पञ्च)", "The line says अष्टौ, eight."),
             ("Six (षट्)", "The line says अष्टौ, eight."),
             ("Ten (दश)", "The line says अष्टौ, eight.")],
            "एताः … अष्टौ षण्ढयोनयः: these eight kinds of ṣaṇḍha.",
            "अष्टौ = eight."),
        order(1, "Put the words of unit 86 in their printed order.",
              ["एताः", "कर्मवैचित्र्यात्", "अष्टौ", "षंढयोनयः", "संकीर्णाः", "कथिताः"],
              "These, from the variety of action, eight, ṣaṇḍha-kinds, mixed, are said.",
              "एताः → कर्मवैचित्र्यात् → अष्टौ → षण्ढयोनयः → संकीर्णाः → कथिताः."),
        T(match(2, "Match each word of unit 86 to its meaning on the card.",
                [["कर्म", "action"], ["वैचित्र्य", "variety"], ["षण्ढ", "the impotent"], ["संकीर्ण", "mixed"],
                 ["कथित", "said, declared"]],
                "Five words carry the summary.",
                "कर्म; वैचित्र्य; षण्ढ; संकीर्ण; कथित.", role="extend"),
          "षण्ढयोनि = a kind (origin) of ṣaṇḍha, the impotent."),
        mcq("discriminate", 3, "अष्टौ ends in -औ; what is it on the card?",
            ("The numeral 'eight', nominative", "The gram label is num. nom. pl.: 'eight', not a dual."),
            [("A dual noun meaning 'the two of them', a pair", "-औ is not always dual; अष्टौ is the numeral eight."),
             ("A verb meaning 'they said'", "The verb-like word here is कथिताः, a participle."),
             ("A locative 'in eight places'", "The gram label is nominative, not locative.")],
            "अष्टौ is the nominative of the numeral 'eight'; its -औ is no dual ending.",
            "-औ is not always dual: अष्टौ = eight."),
        mcq("apply", 4, "By unit 86, what cause does the ablative कर्मवैचित्र्यात् give?",
            ("The variety of action", "वैचित्र्यात्: from the variety of action."),
            [("The anger of the gods or of the ancestors", "Gods are not named in this line."),
             ("The fault of wind and fire", "That is the cause in unit 85."),
             ("The mother's diet", "Diet is not named in this line.")],
            "कर्म (action) + वैचित्र्यात् (from variety): the ablative gives the cause.",
            "-आत् ablative = from, because of."),
        T(mcq("transfer", 5, "By the rule of वैचित्र्यादष्टौ, how is वनात् + आगतः written when joined?",
              ("वनादागतः", "त् before a vowel becomes द्."),
              [("वनातागतः", "त् does not stay unvoiced before a vowel."),
               ("वनानागतः", "त् may become न् (optionally) only before a nasal."),
               ("वनागतः", "The त् does not simply drop.")],
              "वैचित्र्यात् + अष्टौ → वैचित्र्यादष्टौ; so वनात् + आगतः → वनादागतः.",
              "त् + vowel → द् + vowel."),
          "A final त् before a vowel becomes द्."),
    ],
}

# ---------------------------------------------------------------- unit 87
AUTHORED["87"] = {
    "title": "यदा तु स्त्रियाः शोणितगर्भाशयौ",
    "question": "By unit 87, how does a deformity (vikṛti) come to enter a part of the embryo?",
    "rule": ("When the doṣas slightly vitiate the woman's blood and uterus, then, in the embryo, whichever mother-born part "
             "has its doṣa provoked in the seed (बीज) or seed-portion (बीजांश), deformity enters that very part."),
    "limits": ("The line names no particular part, doṣa or deformity. 'Mother-born' (मातृज) is the line's word; it does not list "
               "which parts are mother-born."),
    "explain_hi": ("जब दोष स्त्री के शोणित (रक्त) और गर्भाशय को थोड़ा दूषित करते हैं, तब जो गर्भ होता है, उसके माता से उत्पन्न (मातृज) जिस-जिस अवयव के बीज या बीजांश में दोष प्रकुपित होता है, "
                   "उस-उस अवयव में विकृति प्रवेश करती है। "
                   "‘यस्य यस्य … तं तम्’ दोहराव से बँटवारा बताता है: हर ऐसा अवयव। "
                   "दूषण ‘किंचित्’, यानी थोड़ा है। पंक्ति कोई विशेष अवयव, दोष या विकृति नहीं गिनाती।"),
    "hook": "जिस-जिस अवयव के बीज में दोष, उस-उस अवयव में विकृति।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 87, what enters the part whose seed has the provoked doṣa?",
            ("A deformity (विकृति)", "तं तमवयवं विकृतिराविशति: deformity enters that very part."),
            [("Strength (बल) of the semen", "Strength belongs to unit 78; here it is विकृति."),
             ("Life (जीव)", "Life is not named in this line."),
             ("A fever (ज्वर) in the mother", "Fever is not named in this line.")],
            "विकृति (deformity) आविशति (enters) तं तम् अवयवम् (that very part).",
            "विकृति = deformity; आविशति = enters."),
        order(1, "Put these clauses of unit 87 in their printed order.",
              ["शोणितगर्भाशयौ दोषाः किंचित् प्रदूषयंति", "तदा यो गर्भो भवति", "यस्य यस्य मातृजस्यावयवस्य",
               "बीजे बीजांशे वा दोषः प्रकोपमापद्यते", "तं तमवयवं विकृतिराविशति"],
              "Blood and uterus slightly vitiated, the embryo arises, whichever mother-born part, doṣa provoked in seed or seed-portion, deformity enters that part.",
              "दूषण → गर्भ → अवयव → बीज/बीजांश में प्रकोप → विकृति."),
        T(match(2, "Match each word of unit 87 to its meaning on the card.",
                [["शोणित", "blood"], ["गर्भाशय", "uterus"], ["मातृज", "mother-born"], ["अवयव", "part, limb"],
                 ["विकृति", "deformity"]],
                "Five words carry the chain from mother to deformed part.",
                "शोणित; गर्भाशय; मातृज; अवयव; विकृति.", role="extend"),
          "मातृज = born of the mother: the parts of the embryo that come from her."),
        mcq("discriminate", 3, "What does the repetition यस्य यस्य … तं तम् show?",
            ("Each such part: whichever part, that very part", "The doubled relative and pronoun are distributive."),
            [("Exactly two parts of the embryo are always harmed", "The doubling does not count two; it means each one."),
             ("Only the head is harmed", "No part is named in this line."),
             ("A printing slip to be removed", "The data reads it as a regular distributive construction.")],
            "यस्य यस्य … तं तम्: whichever part has the provoked doṣa, into that very part deformity enters.",
            "Doubled yaḥ … saḥ = distributive 'each such'."),
        multi("apply", 4, "In which two does unit 87 say the doṣa reaches provocation?",
              [("In the father's semen (शुक्र)", "The line speaks of the mother-born part's seed."),
               ("In the seed (बीज)", "Right: बीजे."),
               ("In the seed-portion (बीजांश)", "Right: बीजांशे वा."),
               ("In the breast milk (स्तन्य)", "Breast milk is not named in this line.")],
              [1, 2],
              "बीजे बीजांशे वा: in the seed or in the seed-portion of the mother-born part.",
              "बीज = seed; बीजांश = seed-portion."),
        T(mcq("transfer", 5, "By the rule of विकृतिराविशति, how is हरिः + आगच्छति written when joined?",
              ("हरिरागच्छति", "इः before a vowel becomes इर्."),
              [("हरिआगच्छति", "The visarga does not drop before a vowel here."),
               ("हरोऽगच्छति", "ओऽ comes only from अः + अ."),
               ("हरिसागच्छति", "The visarga does not become स् before a vowel.")],
              "विकृतिः + आविशति → विकृतिराविशति; so हरिः + आगच्छति → हरिरागच्छति.",
              "Visarga after इ/उ + vowel or voiced sound → र्."),
          "A visarga after a vowel other than अ/आ becomes र् before a vowel."),
    ],
}

# ---------------------------------------------------------------- unit 88
AUTHORED["88"] = {
    "title": "यदा ह्यस्याः",
    "question": "By unit 88, what is vitiated in the seed situated in the uterus, and what is then produced?",
    "rule": ("When, in her seed situated in the uterus, the forming seed (निर्वर्तकं बीजम्) is vitiated, then it produces a "
             "barren one (वन्ध्या)."),
    "limits": ("The printed शोणितारख्ये is probably शोणिताख्ये ('called blood', an inserted र); no question rests on that "
               "word. The subject of जनयति is not stated. वन्ध्या is feminine as printed; the noun 'woman' is not in the text."),
    "explain_hi": ("जब इसके (स्त्री के) गर्भाशय में स्थित बीज में निर्वर्तक (शरीर बनाने वाला) बीज दूषित होता है, तब वह बन्ध्या को उत्पन्न करता है। "
                   "छपा ‘शोणितारख्ये’ सम्भवतः ‘शोणिताख्ये’ (शोणित नामक) है, बीच में ‘र’ भूल से आया लगता है। "
                   "‘वंध्याम्’ स्त्रीलिंग है; ‘स्त्री’ संज्ञा पंक्ति में नहीं छपी। "
                   "‘जनयति’ का कर्ता छपा नहीं; अनुवाद ‘वह’ (दूषित बीज) मानता है।"),
    "hook": "निर्वर्तक बीज दूषित: बन्ध्या उत्पन्न।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 88, what is then produced?",
            ("A barren one", "तदा वंध्यां जनयति: then it produces a barren one."),
            [("Twins", "Twins are not named in this line."),
             ("A strong son", "No son is named in this line."),
             ("A child with bent limbs", "No limb is named in this line.")],
            "वन्ध्याम् (a barren one, feminine) जनयति (produces).",
            "वन्ध्या = barren (one); जनयति = produces."),
        order(1, "Put these pieces of unit 88 in their printed order.",
              ["यदा ह्यस्याः", "बीजे गर्भाशयस्थे", "निर्वर्तकं बीजं", "प्रदुष्यति", "तदा वंध्यां जनयति"],
              "When indeed of her, in the seed situated in the uterus, the forming seed, is vitiated, then produces a barren one.",
              "ह्यस्याः → बीजे गर्भाशयस्थे → निर्वर्तकं बीजं → प्रदुष्यति → वंध्यां जनयति."),
        T(match(2, "Match each word of unit 88 to its meaning on the card.",
                [["गर्भाशयस्थ", "situated in the uterus"], ["निर्वर्तक", "forming, producing"],
                 ["प्रदुष्यति", "is vitiated"], ["वन्ध्या", "barren (one)"], ["जनयति", "produces"]],
                "Five words carry the cause and the result.",
                "गर्भाशयस्थ; निर्वर्तक; प्रदुष्यति; वन्ध्या; जनयति.", role="extend"),
          "निर्वर्तक = that which brings about or forms."),
        mcq("discriminate", 3, "Which split of ह्यस्याः is right?",
            ("हि + अस्याः", "इ before a different vowel becomes य्."),
            [("ह्य + अस्याः", "अ + अ would join as आ: ह्यास्याः."),
             ("हि + यस्याः", "That would stay हियस्याः; यस्याः is not on the card."),
             ("ह्यस् + याः", "ह्यस् and याः are not words of the card.")],
            "हि (indeed) + अस्याः (her): इ + अ → य.",
            "इ + a different vowel → य् + that vowel."),
        mcq("apply", 4, "What does the card say about वंध्यां in unit 88?",
            ("Feminine 'barren one'; 'woman' is not printed", "The note: the feminine is as printed; the noun 'woman' is not in the text."),
            [("Masculine 'barren man', the father of the child", "The form वन्ध्याम् is feminine accusative."),
             ("A plural 'barren ones'", "The gram label is singular: f. acc. sg."),
             ("A verb 'makes barren'", "The verb is जनयति; वन्ध्याम् is its object.")],
            "वन्ध्याम्: f. acc. sg., the object of जनयति; the card supplies no noun 'woman'.",
            "वन्ध्याम् = f. acc. sg., object of जनयति."),
        T(mcq("transfer", 5, "By the rule of ह्यस्याः, how is प्रति + अक्षम् written when joined?",
              ("प्रत्यक्षम्", "इ before अ becomes य्."),
              [("प्रतीक्षम्", "इ + अ does not give ई."),
               ("प्रत्याक्षम्", "Only य् is added; the अ stays short."),
               ("प्रतेक्षम्", "इ + अ does not give ए.")],
              "हि + अस्याः → ह्यस्याः; so प्रति + अक्षम् → प्रत्यक्षम्.",
              "इ + अ → य."),
          "A final इ before a different vowel becomes य्."),
    ],
}

# ===================================================================== NOTES_HI
NOTES_HI = {
    "76": ("कर्ता इस पंक्ति में नहीं छपा; पहले के प्रसंग से आता है। ‘यदा … तदा’ वाक्य इकाई ७७ में पूरा होता है। "
           "छपा ‘उपहंति’ = उपहन्ति (अनुस्वार-लेखन)। सन्धियाँ: कार्त्स्न्येन + उपहन्ति → कार्त्स्न्येनोपहन्ति (अ + उ → ओ); "
           "अनुपघ्नन् + एव → अनुपघ्नन्नेव (ह्रस्व स्वर के बाद न् स्वर से पहले द्वित्व); स्रोतः + मुखम् → स्रोतोमुखम् (अः + घोष व्यंजन → ओ)।"),
    "77": ("इकाई ७६ का ‘तदा’ भाग। ‘भवति’ का कर्ता नहीं छपा। ‘संस्कार’ का अर्थ ‘उपचार’ ‘तत्र संस्कारः’ से लिया गया। "
           "पाठ-सूचना: छपा ‘चेतोहर्ष णानि’ सम्भवतः एक शब्द ‘चेतोहर्षणानि’ है (बीच की जगह भूल से)। "
           "सन्धियाँ: संस्कारः + वाजीकराः → संस्कारो वाजीकराः; वाजीकराः + बस्तयः → वाजीकरा बस्तयः (आः + घोष व्यंजन → आ, विसर्ग लोप); "
           "बस्तयः + अभ्यवहारः → बस्तयोऽभ्यवहारः (अः + अ → ओऽ); अभ्यवहारः + चेतः → अभ्यवहारश्चेतः (ः + च → श्च)।"),
    "78": ("‘तानि’ इकाई ७७ में गिनाई गई वस्तुओं की ओर संकेत करता है। ‘अस्य’ सबसे स्वाभाविक रूप से शुक्र के साथ (इसका), पर ‘उसका’ भी सम्भव। "
           "अन्त का ‘इति’ अनूदित नहीं। सन्धियाँ: बलम् + आदधानानि → बलमादधानानि; स्रोतांसि + अस्य → स्रोतांस्यस्य (इ + अ → य); "
           "अस्य + आप्याययन्ति → अस्याप्याययन्ति (अ + आ → आ); आप्याययन्ति + इति → आप्याययन्तीति (इ + इ → ई)।"),
    "79": ("पाठ-सूचना: छपा ‘तद्दिधा’ कोई शब्द नहीं; सम्भवतः ‘तद्विधा’ (वैसी), जो इकाई ८० के ‘तद्विधौ’ से मेल खाता है। "
           "अन्तिम खण्ड अधूरा: ‘है’ जोड़ा गया, ‘पुंसः’ को ‘पुरुष के प्रति’ पढ़ा गया। ‘नार्या’ तृतीया: ‘स्त्री के साथ’। "
           "वाक्य इकाई ८० में पूरा होता है। सन्धियाँ: अल्पबीजः + अल्पबलः → अल्पबीजोऽल्पबलः; पुमान् + उद्वेगः → पुमानुद्वेगः; "
           "स्त्रीद्वेषयुक्तः + अन्यकामः → स्त्रीद्वेषयुक्तोऽन्यकामः (अः + अ → ओऽ); अन्यकामः + वा → अन्यकामो वा।"),
    "80": ("विश्वास कम। छपा ‘तदाऽऽसेक्यं’ (दोहरा अवग्रह जैसा छपा) = तदा + आसेक्यम्; ‘आसेक्य’ पारिभाषिक नाम लगता है, पर पंक्ति परिभाषा नहीं देती "
           "और इसकी विभक्ति अस्पष्ट है। यह षण्ढ का एक प्रकार है, यह केवल दूसरे ग्रन्थों से सम्भावित। ‘ध्वज’ शिश्न के लिए शिष्ट शब्द (मानक)। "
           "सन्धियाँ: न + एव → नैव (अ + ए → ऐ); वक्रध्वजः + भवति → वक्रध्वजो भवति; छपा ‘ध्वजस्तभ्यते’ = ध्वजः + स्तभ्यते; स् + कठोर व्यंजन से पहले विसर्ग का लोप वैकल्पिक नियमित सन्धि है।"),
    "81": ("पाठ-सूचना: छपा ‘स्त्रिया’ गर्भो से पहले नियमित सन्धि से षष्ठी ‘स्त्रियाः’ भी हो सकता है (आः + घोष → आ), तृतीया भी; अनुवाद षष्ठी पर चलता है। "
           "‘पूति’ = सड़ा या दुर्गन्धयुक्त; पंक्ति नहीं बताती कौन-सा। वाक्य इकाई ८२ में पूरा होता है। सन्धि: गर्भः + भवति → गर्भो भवति।"),
    "82": ("छपा ‘आस्वादात्ध्वज’ में त् को द् नहीं किया गया (छपाई की आदत; नियम से आस्वादाद्ध्वज)। कर्ता ‘वह’ नहीं छपा। "
           "‘उच्छ्राय’ = उठना, उत्थान (सम्भावित)। सन्धियाँ: तत् + शुक्र → तच्छुक्र (त् + श → च्श, विकल्प से च्छ (श के बाद स्वर या य/व/र हो तो; छपा च्छ)); शुक्र + आस्वादात् → शुक्रास्वादात्; "
           "ध्वज + उच्छ्रायम् → ध्वजोच्छ्रायम् (अ + उ → ओ)।"),
    "83": ("विश्वास कम। छपे ‘पुमुरुभावपि’ और ‘तत्सौगंधिकारण्यं’ अस्पष्ट हैं: ‘पुमान् उभौ अपि’ और ‘तत् सौगन्धिकाख्यम्’ केवल अनुमान हैं, पक्के नहीं। "
           "‘योनिध्वजगन्धेन’ को द्वन्द्व (योनि और ध्वज की गन्ध) पढ़ा गया; ‘योनि के ध्वज की गन्ध’ भी सम्भव। "
           "‘सौगन्धिक’ षण्ढ का प्रकार है, यह दूसरे ग्रन्थों से सम्भावित पहचान है। ‘बल’ = बल; उत्थान नहीं कहा।"),
    "84": ("दो छपी पंक्तियाँ (०२.०२.८६, ०२.०२.८७)। पहली अधूरी: ‘संज्ञाम्’ के बाद क्रिया नहीं। ‘मंदहर्षौसंसृज्येते’ एक साथ छपा = मन्दहर्षौ + संसृज्येते। "
           "‘परम्’ = दूसरे को; ‘केवल’ अर्थ भी वर्जित नहीं। ‘तस्य’ प्रवृत्ति के साथ। "
           "सन्धियाँ: तु + ईर्ष्या → त्वीर्ष्या (उ + ई → वी); तदा + ईर्ष्यालुः → तदेर्ष्यालुः (आ + ई → ए); "
           "ईर्ष्यालुः + इति → ईर्ष्यालुरिति; मैथुनप्रवृत्तिः + भवति → मैथुनप्रवृत्तिर्भवति (इः/उः + स्वर या घोष → र्)।"),
    "85": ("‘पुरुषस्य गर्भस्य’ = नर गर्भ का। ‘दोष’ यहाँ ‘खराबी’ पढ़ा गया, त्रिदोष नहीं, क्योंकि वायु-अग्नि के साथ समास में है। "
           "वृषण = अण्डकोष (मानक); समास में एक या दो, यह चिह्नित नहीं। ‘वायुपिण्डक’ प्रकार का नाम, अनूदित नहीं; छपा ‘पिंडक’ = पिण्डक। "
           "सन्धियाँ: वायु + अग्नि → वाय्वग्नि (उ + अ → व); दोषात् + वृषण → दोषाद्वृषण (त् + घोष → द्); पिण्डक + आख्यम् → पिण्डकाख्यम्।"),
    "86": ("छपा ‘षंढ’ = षण्ढ (लेखन-भेद)। ‘संकीर्णाःकथिताः’ बिना जगह छपा = संकीर्णाः कथिताः। ‘योनि’ = प्रकार, उत्पत्ति। "
           "‘संकीर्ण’ = मिश्रित, या ‘फुटकर’। आठ यहाँ गिनाए नहीं गए। ‘अष्टौ’ संख्या का प्रथमा रूप, द्विवचन नहीं। "
           "सन्धि: वैचित्र्यात् + अष्टौ → वैचित्र्यादष्टौ (त् + स्वर → द्)।"),
    "87": ("‘मातृजस्यावयवस्य’ = मातृजस्य + अवयवस्य (अ + अ → आ), षष्ठी: बीज या बीजांश का स्वामी। ‘यस्य यस्य … तं तम्’ बँटवारे का प्रयोग। "
           "गर्भाशय = गर्भाशय, uterus (मानक)। सन्धियाँ: यः + गर्भः → यो गर्भः; प्रकोपम् + आपद्यते → प्रकोपमापद्यते; "
           "तम् + अवयवम् → तमवयवम्; विकृतिः + आविशति → विकृतिराविशति (इः + स्वर → र्)।"),
    "88": ("पाठ-सूचना: छपा ‘शोणितारख्ये’ सम्भवतः ‘शोणिताख्ये’ (शोणित नामक) है; बीच में ‘र’ जुड़ा लगता है (वही भूल आगे भी दिखती है)। "
           "‘जनयति’ का कर्ता नहीं छपा। ‘वंध्यां’ स्त्रीलिंग; ‘स्त्री’ संज्ञा नहीं छपी। ‘बीज’ दो बार दो अर्थों में, जैसा छपा। "
           "सन्धि: हि + अस्याः → ह्यस्याः (इ + अ → य)।"),
}

# ===================================================================== AIDS
AIDS = {
    "76": {
        "seesaw": "उपहन्ति (पूरा घात करता) ↔ अनुपघ्नन् (घात न करते हुए, केवल स्रोत का मुख ढकता)।",
        "chunks": "यदा तु | कार्त्स्न्येनोपहंति | अनुपघ्नन्नेव वा | स्रोतोमुखं पिधत्ते",
        "sandhi": ("अ + उ → ओ: कार्त्स्न्येन + उपहन्ति → कार्त्स्न्येनोपहन्ति · ह्रस्व + न् + स्वर → न्न्: अनुपघ्नन् + एव → अनुपघ्नन्नेव · "
                   "अः + म → ओ: स्रोतः + मुखम् → स्रोतोमुखम्।"),
        "frame": "‘यदा’ (जब) यहाँ; ‘तदा’ (तब) इकाई ७७ में।",
    },
    "77": {
        "diagram": {"groups": [
            {"label": "तदा", "items": ["संस्कारबाह्य (उपचार से बाहर)"]},
            {"label": "तत्र संस्कारः", "items": ["वाजीकर बस्तियाँ", "अभ्यवहार (खाना)", "चित्त-हर्षक (पाठ सम्भावित)"]}]},
        "sandhi": ("अः + अ → ओऽ: बस्तयः + अभ्यवहारः → बस्तयोऽभ्यवहारः · ः + च → श्च: अभ्यवहारः + चेतः → अभ्यवहारश्चेतः · "
                   "आः + ब → आ ब: वाजीकराः + बस्तयः → वाजीकरा बस्तयः।"),
        "letters": "उपचार के तीन: ब-अ-चे (बस्ति, अभ्यवहार, चेतोहर्षण: अन्तिम का पाठ सम्भावित)।",
    },
    "78": {
        "chain": {"steps": ["वे (इकाई ७७ के उपचार)", "शुक्र में बल देते", "उसके स्रोतों को पुष्ट करते"]},
        "sandhi": ("इ + अ → य: स्रोतांसि + अस्य → स्रोतांस्यस्य · अ + आ → आ: अस्य + आप्याययन्ति → अस्याप्याययन्ति · "
                   "इ + इ → ई: आप्याययन्ति + इति → आप्याययन्तीति।"),
        "frame": "‘हि’ (क्योंकि): इकाई ७७ के उपचार का कारण।",
    },
    "79": {
        "diagram": {"groups": [
            {"label": "पुरुष (छपे क्रम में)", "items": ["१ अल्पबीज", "२ अल्पबल", "३ उद्विग्न", "४ स्त्री-द्वेषी", "५ अन्य-कामी"]},
            {"label": "फल", "items": ["स्त्री से मैथुन में रुकावट"]},
            {"label": "या", "items": ["स्त्री वैसी (पाठ सम्भावित), पुरुष के प्रति"]}]},
        "sandhi": ("अः + अ → ओऽ: अल्पबीजः + अल्पबलः → अल्पबीजोऽल्पबलः · अः + व → ओ: अन्यकामः + वा → अन्यकामो वा · "
                   "न् + स्वर: पुमान् + उद्वेगः → पुमानुद्वेगः।"),
        "letters": "पाँच विशेषण: बी-ब-उ-द्वे-अ (बीज, बल, उद्वेग, द्वेष, अन्यकाम)।",
        "frame": "‘यदा’ यहाँ; ‘तदा’ वाला फल इकाई ८० में।",
    },
    "80": {
        "chunks": "तदाऽऽसेक्यं | स्त्रीपुंसौ तद्विधौ भवतः | तदा वक्रध्वजो भवति | तस्य नैव ध्वजस्तभ्यते",
        "sandhi": "अ + ए → ऐ: न + एव → नैव · अः + भ → ओ: वक्रध्वजः + भवति → वक्रध्वजो भवति।",
        "frame": "सम्भवतः इकाई ७९ का ‘तदा’ भाग। ‘आसेक्य’ अनूदित: पंक्ति इसे नहीं समझाती।",
    },
    "81": {
        "frame": "‘यदा’ यहाँ (पूतियोनि स्त्री का गर्भ); फल इकाई ८२ में।",
        "sandhi": "अः + भ → ओ: गर्भः + भवति → गर्भो भवति।",
        "anchors": "पूति = सड़ा/दुर्गन्ध; ‘पूतियोनि’ = जिसकी योनि पूति हो (बहुव्रीहि)।",
    },
    "82": {
        "chain": {"steps": ["उस शुक्र का आस्वाद", "ध्वज का उठना पाता है"]},
        "sandhi": ("त् + श → च्श, विकल्प से च्छ (श के बाद स्वर या य/व/र हो तो; छपा च्छ): तत् + शुक्र → तच्छुक्र · अ + उ → ओ: ध्वज + उच्छ्रायम् → ध्वजोच्छ्रायम् · "
                   "नियम से त् + ध → द्ध: आस्वादात् + ध्वज → आस्वादाद्ध्वज (छपाई में बिना जोड़)।"),
        "frame": "सम्भवतः इकाई ८१ के ‘यदा’ का फल।",
    },
    "83": {
        "frame": "पक्का भाग: ‘योनिध्वजगंधेन बलं लभते’; बीच के दो छपे शब्द अस्पष्ट।",
        "anchors": "गन्धेन = गन्ध से (तृतीया, ‘-एन’)।",
        "contrast": "इसी पंक्ति में: अस्पष्ट (पुमुरुभावपि, तत्सौगंधिकारण्यं) ↔ पक्का (योनिध्वजगंधेन बलं लभते)।",
    },
    "84": {
        "chain": {"steps": ["ईर्ष्या से अभिभूत", "मन्द हर्ष वाले दोनों", "संयुक्त होते हैं", "संज्ञा: ईर्ष्यालु",
                            "दूसरे को मिथुन देखकर", "मैथुन में प्रवृत्ति"]},
        "sandhi": ("उ + ई → वी: तु + ईर्ष्या → त्वीर्ष्या · आ + ई → ए: तदा + ईर्ष्यालुः → तदेर्ष्यालुः · "
                   "उः + इ → उरि: ईर्ष्यालुः + इति → ईर्ष्यालुरिति।"),
        "puns": "मेरी बनाई, केवल सुनने की सहायता: ‘ईर्ष्या’ से ‘ईर्ष्यालु’, जैसे ‘दया’ से ‘दयालु’।",
    },
    "85": {
        "diagram": {"groups": [
            {"label": "कारण", "items": ["वायु और अग्नि का दोष"]},
            {"label": "हानि", "items": ["नर गर्भ के वृषण का नाश"]},
            {"label": "नाम", "items": ["वायुपिण्डक"]}]},
        "sandhi": "उ + अ → व: वायु + अग्नि → वाय्वग्नि · त् + व → द्व: दोषात् + वृषण → दोषाद्वृषण · अ + आ → आ: पिण्डक + आख्यम् → पिण्डकाख्यम्।",
        "anchors": "दोष यहाँ ‘खराबी’, त्रिदोष नहीं।",
    },
    "86": {
        "anchors": "अष्टौ = आठ; ‘-औ’ है पर द्विवचन नहीं।",
        "sandhi": "त् + अ → द: वैचित्र्यात् + अष्टौ → वैचित्र्यादष्टौ।",
        "chunks": "एताः | कर्मवैचित्र्यात् | अष्टौ षंढयोनयः | संकीर्णाः कथिताः",
    },
    "87": {
        "diagram": {"groups": [
            {"label": "१ कारण", "items": ["दोष स्त्री के शोणित और गर्भाशय को थोड़ा दूषित करते"]},
            {"label": "२ गर्भ", "items": ["तब गर्भ होता"]},
            {"label": "३ प्रकोप", "items": ["मातृज अवयव के बीज या बीजांश में दोष-प्रकोप"]},
            {"label": "४ फल", "items": ["उसी अवयव में विकृति"]}]},
        "sandhi": ("अ + अ → आ: मातृजस्य + अवयवस्य → मातृजस्यावयवस्य · इः + आ → इरा: विकृतिः + आविशति → विकृतिराविशति · "
                   "म् + स्वर: प्रकोपम् + आपद्यते → प्रकोपमापद्यते।"),
        "anchors": "‘यस्य यस्य … तं तम्’ = जिस-जिस … उस-उस।",
    },
    "88": {
        "chain": {"steps": ["गर्भाशय में स्थित बीज में", "निर्वर्तक बीज दूषित", "बन्ध्या उत्पन्न"]},
        "sandhi": "इ + अ → य: हि + अस्याः → ह्यस्याः।",
        "frame": "‘शोणितारख्ये’ का पाठ सम्भावित (शोणिताख्ये); उस पर प्रश्न नहीं।",
    },
}

# ===================================================================== IMAGE_SPECS
IMAGE_SPECS = {
    ("76", "seesaw"): {
        "file": "sh2-srotomukha-76.svg",
        "alt": ("Split of unit 76: the two cases joined by 'or': it wholly damages; or, without damaging, it simply closes "
                "the mouth of the channel (srotas)."),
        "type": "split",
        "title": "दो विकल्प (इकाई ७६)",
        "cols": [["उपहन्ति", ["कार्त्स्न्येन: पूरी तरह", "घात करता"]],
                 ["अनुपघ्नन्", ["घात न करते हुए", "केवल स्रोत का मुख ढकता"]]],
    },
    ("77", "diagram"): {
        "file": "sh2-samskara-77.svg",
        "alt": ("Flowchart of unit 77: then (it) becomes outside treatment; there the treatment is three items: aphrodisiac "
                "enemas, eating, and mind-gladdening (ones), the last on a probable reading."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"तदा: संस्कारबाह्य\"] --> B[\"तत्र संस्कारः\"]\n"
                 "  B --> C[\"१ वाजीकर<br/>बस्तियाँ\"]\n"
                 "  B --> D[\"२ अभ्यवहार<br/>(खाना)\"]\n"
                 "  B --> E[\"३ चित्त-हर्षक<br/>(सम्भावित)\"]\n"),
    },
    ("79", "diagram"): {
        "file": "sh2-alpabija-79.svg",
        "alt": ("Split of unit 79: the man's five qualities in printed order (little seed, little strength, agitated, "
                "aversion to women, desiring another); what happens: obstruction of intercourse with the woman, or the "
                "woman (probable reading) is of that kind towards the man."),
        "type": "split",
        "title": "इकाई ७९: जब …",
        "cols": [["पुरुष (छपे क्रम में)", ["१ अल्पबीज", "२ अल्पबल", "३ उद्विग्न", "४ स्त्री-द्वेषी", "५ अन्य-कामी"]],
                 ["क्या होता", ["स्त्री से मैथुन में रुकावट", "या स्त्री वैसी (पाठ सम्भावित), पुरुष के प्रति"]]],
    },
    ("84", "chain"): {
        "file": "sh2-irshyalu-84.svg",
        "alt": ("Chain of unit 84: overcome by jealousy; the two of little delight; are joined; the name irshyalu; on "
                "seeing another coupled; engagement in intercourse."),
        "type": "chain",
        "title": "ईर्ष्यालु (इकाई ८४)",
        "steps": ["ईर्ष्या से अभिभूत", "मन्द हर्ष वाले दोनों", "संयुक्त होते हैं", "संज्ञा: ईर्ष्यालु",
                  "दूसरे को मिथुन देखकर", "मैथुन में प्रवृत्ति"],
    },
    ("85", "diagram"): {
        "file": "sh2-vayupindaka-85.svg",
        "alt": ("Flowchart of unit 85: the fault of wind and fire destroys the testes of the male embryo; then it is called "
                "vayupindaka."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"वायु और अग्नि का दोष\"] --> B[\"नर गर्भ के वृषण का नाश\"]\n"
                 "  B --> C[\"नाम: वायुपिण्डक\"]\n"),
    },
    ("87", "diagram"): {
        "file": "sh2-avayava-vikriti-87.svg",
        "alt": ("Flowchart of unit 87 in four steps: the doshas slightly vitiate the woman's blood and uterus; the embryo "
                "arises; the dosha is provoked in the seed or seed-portion of a mother-born part; deformity enters that part."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"१ शोणित, गर्भाशय थोड़ा दूषित\"] --> B[\"२ तब गर्भ होता\"]\n"
                 "  B --> C[\"३ मातृज अवयव के बीज या बीजांश में\"]\n"
                 "  C --> D[\"दोष-प्रकोप\"]\n"
                 "  D --> E[\"४ उसी अवयव में विकृति\"]\n"),
    },
}
