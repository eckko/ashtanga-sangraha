from helpers import mcq, match, order, fill, multi, accepts


AUTHORED = {}

# ---------------------------------------------------------------- unit 65
AUTHORED["65"] = {
    "title": "तान्यामभया... दुष्यंति ततोऽतितृष्णा",
    "question": "By unit 65, by what are the water-carrying srotas vitiated, and which signs follow?",
    "rule": ("They (तानि, the water-carrying srotas of card 64) become vitiated (दुष्यन्ति) by āma, fear, excessive "
             "drinking, heat, dry food and the like; then (ततः) excessive thirst, dry mouth, ringing in the ears, seeing darkness."),
    "limits": ("Prose; the signs have no verb. Āma's sense here is uncertain; the printed तृष्णिग्रह is read 'holding "
               "back of thirst' only by conjecture: no question on either. The drink is not named. Kṣveḍana as "
               "tinnitus-type ringing is probable."),
    "explain_hi": ("यह गद्य-पंक्ति इकाई ६४ के उदकवह (जल वहन करने वाले) स्रोतस की दुष्टि बताती है: ‘तानि’ यानी वे स्रोतस। "
                   "कारण: आम (यहाँ अर्थ अनिश्चित), भय, अतिपान (अधिक पीना; क्या, यह छपा नहीं), उष्ण, सूखा अन्न, और छपा ‘तृष्णिग्रह’, जिसे अनुमान से ‘तृष्णा-निग्रह’ यानी प्यास रोकना पढ़ा गया है; ‘आदि’ से सूची खुली है। "
                   "तब (ततः) लक्षण: अत्यधिक प्यास, मुख का सूखना, कानों में भनभनाहट (कर्णक्ष्वेडन, सम्भवतः टिनिटस जैसा) और अँधेरा दिखना। "
                   "लक्षणों के साथ कोई क्रिया छपी नहीं। "
                   "सन्धि: तमस् + दर्शनम् → तमोदर्शनम् (अस् + घोष व्यंजन → ओ)।"),
    "hook": "जलवह दूषित: प्यास, सूखा मुँह, कान में भनभन, आँखों में अँधेरा।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 65, which is a sign once the water-carrying srotas are vitiated?",
            ("Excessive thirst", "ततोऽतितृष्णा: then excessive thirst."),
            [("Pain in the left side", "The left side is a root of the food-carrying ones (unit 67), not a sign here."),
             ("Breathing with sound", "Noisy breathing belongs to the prāṇa-carrying ones (unit 62)."),
             ("Yellow eyes", "No yellow colour is named in unit 65.")],
            "Then come excessive thirst, dry mouth, ringing in the ears and seeing darkness.",
            "ततोऽतितृष्णा मुखशोषः कर्णक्ष्वेडनं तमोदर्शनं च."),
        order(1, "Put the signs in the order of unit 65.",
              ["अतितृष्णा", "मुखशोषः", "कर्णक्ष्वेडनं", "तमोदर्शनं"],
              "Excessive thirst, dryness of the mouth, ringing in the ears, seeing darkness.",
              "अतितृष्णा → मुखशोषः → कर्णक्ष्वेडनं → तमोदर्शनं."),
        match(2, "Match each word of unit 65 to its meaning.",
              [["अतितृष्णा", "excessive thirst"], ["मुखशोष", "dryness of the mouth"],
               ["कर्णक्ष्वेडन", "ringing in the ears (probable)"], ["तमोदर्शन", "seeing darkness"],
               ["भय", "fear"], ["अतिपान", "excessive drinking"]],
              "Causes include fear and excessive drinking; the signs are thirst, dry mouth, ear-ringing, darkness.",
              "अतितृष्णा, मुखशोष, कर्णक्ष्वेडन, तमोदर्शन, भय, अतिपान.", role="extend",
              teaches="मुखशोष = मुख (mouth) + शोष (drying): a tatpuruṣa, 'drying of the mouth'."),
        mcq("discriminate", 3, "Which split of तमोदर्शनं in unit 65 is right?",
            ("तमस् + दर्शनम्", "अस् before a voiced consonant (द) becomes ओ: तमोदर्शनम्."),
            [("तमा + दर्शनम्", "आ before a consonant stays आ: तमादर्शनम्."),
             ("तमम् + दर्शनम्", "म् before a consonant would be written ं: तमंदर्शनम्."),
             ("तमौ + दर्शनम्", "औ before a consonant stays औ: तमौदर्शनम्.")],
            "तमस् (darkness) + दर्शनम् (seeing): अस् → ओ before a voiced consonant.",
            "अस् / अः before a voiced consonant → ओ."),
        multi("apply", 4, "Which statements fit unit 65?",
              [("A verb is printed with the signs", "The signs have no verb (data note)."),
               ("Fear is named among the causes", "Right: भय."),
               ("Seeing darkness is named among the signs", "Right: तमोदर्शनम्."),
               ("The line says what is drunk to excess", "अतिपान does not say what is drunk.")],
              [1, 2],
              "Fear is a cause and seeing darkness a sign; āma and the drink are left unclear.",
              "...भयातिपान... ततोऽतितृष्णा ... तमोदर्शनं च."),
        mcq("transfer", 5, "By the rule of अतिपान + उष्ण → अतिपानोष्ण, how is हित + उपदेशः joined in a new example?",
            ("हितोपदेशः", "अ + उ → ओ, as अतिपान + उष्ण → अतिपानोष्ण."),
            [("हितौपदेशः", "औ comes from अ + ओ/औ, not from अ + उ."),
             ("हितुपदेशः", "अ does not drop before उ; the two merge into ओ."),
             ("हितापदेशः", "आ comes from अ + अ/आ, not from अ + उ.")],
            "हित + उपदेशः = हितोपदेशः, like अतिपान + उष्ण = अतिपानोष्ण.",
            "अ + उ → ओ.",
            teaches="अ before उ merges into ओ: अतिपान + उष्ण → अतिपानोष्ण."),
    ],
}

# ---------------------------------------------------------------- unit 66
AUTHORED["66"] = {
    "title": "तत्र तृष्णोक्तमौषधं",
    "question": "By unit 66, which medicine is to be used for the vitiated water-carrying srotas?",
    "rule": ("There (तत्र), the medicine (औषधम्) is the one stated for thirst (तृष्णा-उक्तम्): the text points to a "
             "treatment given elsewhere."),
    "limits": ("Prose, elliptical: no verb. The medicine for thirst is not repeated here and the line does not say where "
               "it is stated; no remedy or dose is given."),
    "explain_hi": ("यह छोटी गद्य-पंक्ति इकाई ६५ के लक्षणों के बाद आती है: वहाँ तृष्णा (प्यास) में कही गई औषध। "
                   "औषध का विवरण यहाँ नहीं दोहराया गया; पाठ कहीं और बताए गए तृष्णा के उपचार की ओर संकेत करता है। "
                   "कहाँ बताया गया, यह पंक्ति नहीं कहती। "
                   "कोई क्रिया छपी नहीं। "
                   "सन्धि: तृष्णा + उक्तम् → तृष्णोक्तम् (आ + उ → ओ); उक्तम् + औषधम् → उक्तमौषधम्।"),
    "hook": "जलवह की दवा: तृष्णा वाली।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 66, which medicine applies in this case?",
            ("The one stated for thirst", "तृष्णोक्तमौषधम्: the medicine stated for thirst."),
            [("The one stated for fever", "Fever is not named in unit 66."),
             ("The one stated for cough", "Cough is not named in unit 66."),
             ("The one stated for śvāsa", "Śvāsa's treatment is pointed to for the prāṇa-carrying ones (unit 63).")],
            "There, the medicine is the one stated for thirst.",
            "तत्र तृष्णोक्तमौषधम्."),
        order(1, "Put the words of unit 66 in the line's order.",
              ["तत्र", "तृष्णा", "उक्तम्", "औषधम्"],
              "There, thirst, stated, medicine: the medicine stated for thirst.",
              "तत्र → तृष्णा → उक्तम् → औषधम्."),
        match(2, "Match each word of unit 66 to its meaning.",
              [["तत्र", "there, in this case"], ["तृष्णा", "thirst"], ["उक्त", "said, stated"], ["औषध", "medicine"]],
              "There, the medicine stated for thirst.",
              "तत्र, तृष्णा, उक्त, औषध.", role="extend",
              teaches="तृष्णोक्त = तृष्णा (thirst) + उक्त (stated): 'stated for thirst'."),
        mcq("discriminate", 3, "Which split of तृष्णोक्तम् in unit 66 is right?",
            ("तृष्णा + उक्तम्", "आ + उ → ओ: तृष्णा + उक्तम् → तृष्णोक्तम्."),
            [("तृष्णः + उक्तम्", "अः before a vowel other than अ becomes अ with no join: तृष्ण उक्तम्."),
             ("तृष्णे + उक्तम्", "ए before उ would give अय् or अ with a gap, not ओ."),
             ("तृष्णौ + उक्तम्", "औ before उ would give आव्: तृष्णावुक्तम्.")],
            "तृष्णा (thirst) + उक्तम् (stated): आ + उ → ओ.",
            "आ + उ → ओ."),
        fill(4, "In unit 66 the medicine is the one stated for ____ (thirst). Type it in Devanagari or in English letters (e.g. dharma).",
             accepts("तृष्णा", None, "trishna", "trshna"),
             "तृष्णा = thirst: तृष्णोक्तमौषधम्.",
             "तृष्णा = thirst.",
             "तत्र तृष्णोक्तमौषधम्.", role="apply"),
        mcq("transfer", 5, "By the rule of तृष्णा + उक्तम् → तृष्णोक्तम्, how is महा + उत्सवः joined in a new example?",
            ("महोत्सवः", "आ + उ → ओ, as तृष्णा + उक्तम् → तृष्णोक्तम्."),
            [("महौत्सवः", "औ comes from अ/आ + ओ/औ, not from आ + उ."),
             ("महात्सवः", "आ does not swallow the उ; the two merge into ओ."),
             ("महुत्सवः", "आ does not drop before उ; the two merge into ओ.")],
            "महा + उत्सवः = महोत्सवः, like तृष्णा + उक्तम् = तृष्णोक्तम्.",
            "आ + उ → ओ.",
            teaches="आ before उ merges into ओ: तृष्णा + उक्तम् → तृष्णोक्तम्."),
    ],
}

# ---------------------------------------------------------------- unit 67
AUTHORED["67"] = {
    "title": "अन्नवाहिनामामाशयो मूलं वामपार्श्वं च",
    "question": "By unit 67, what is the root of the food-carrying (srotas)?",
    "rule": ("Of the food-carrying (ones) (अन्नवाहिनाम्), the root is the āmāśaya and the left side (वामपार्श्वम्); in "
             "their vitiation one should understand all as stated in the Mātrāśitīya (मात्राशितीयोक्तम्)."),
    "limits": ("Two printed lines. Āmāśaya as the stomach is probable. The left side is not further specified. The "
               "Mātrāśitīya is taken as the name of a chapter; the line does not say which, and the card does not guess."),
    "explain_hi": ("इस इकाई में दो छपी पंक्तियाँ हैं। "
                   "पहली: अन्न वहन करने वालों (स्रोतस) का मूल आमाशय, यानी आम (कच्चे, अपचे अन्न) का आशय, सम्भवतः जठर (सम्भावित), और वाम पार्श्व यानी बायाँ बगल-भाग है। "
                   "दूसरी: उनके दूषित होने पर (दुष्टौ) सब कुछ ‘मात्राशितीय’ में कहे अनुसार समझना चाहिए। "
                   "मात्राशितीय किसी अध्याय का नाम माना गया है (शब्दार्थ: खाए हुए की मात्रा वाला); कौन-सा अध्याय, यह पंक्ति नहीं बताती। "
                   "‘अवगच्छेत्’ विधिलिङ् है: ‘समझना चाहिए’।"),
    "hook": "अन्नवह का मूल: आमाशय और बायाँ पार्श्व; दुष्टि: मात्राशितीय देखो।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 67, what is the root of the food-carrying (srotas)?",
            ("The āmāśaya and the left side", "अन्नवाहिनामामाशयो मूलं वामपार्श्वं च."),
            [("The palate and the kloma organ", "Palate and kloma are the roots of the water-carrying ones (unit 64)."),
             ("The heart and the ten vessels", "Heart and ten dhamanīs are the roots of the rasa-carrying ones (unit 68)."),
             ("The liver and the spleen", "Liver and spleen belong to the blood-carrying ones (unit 69).")],
            "Of the food-carrying ones, the root is the āmāśaya and the left side.",
            "अन्नवाहिनामामाशयो मूलं वामपार्श्वं च."),
        order(1, "Put the printed pieces of unit 67 in the order of its two lines.",
              ["अन्नवाहिनामामाशयो", "मूलं", "वामपार्श्वं च", "तेषां दुष्टौ", "सर्वं", "मात्राशितीयोक्तमवगच्छेत्"],
              "Of the food-carrying, the āmāśaya, the root, and the left side; in their vitiation, all, as the Mātrāśitīya states, one should understand.",
              "अन्नवाहिनामामाशयो → मूलं → वामपार्श्वं च → तेषां दुष्टौ → सर्वं → मात्राशितीयोक्तमवगच्छेत्."),
        match(2, "Match each word of unit 67 to its meaning.",
              [["अन्न", "food"], ["आमाशय", "seat of undigested food (probably the stomach)"], ["वाम", "left"],
               ["पार्श्व", "side, flank"], ["दुष्टि", "vitiation"], ["अवगच्छेत्", "one should understand"]],
              "Food-carrying: root āmāśaya and left side; in vitiation, one should understand all from the Mātrāśitīya.",
              "अन्न, आमाशय, वाम, पार्श्व, दुष्टि, अवगच्छेत्.", role="extend",
              teaches="आमाशय = आम (undigested) + आशय (seat), with अ + आ → आ."),
        mcq("discriminate", 3, "Which split of आमाशयो मूलं in unit 67 is right?",
            ("आमाशयः + मूलम्", "अः before a voiced consonant (म) becomes ओ: आमाशयो मूलम्."),
            [("आमाशये + मूलम्", "ए before a consonant stays ए: आमाशये मूलम्."),
             ("आमाशयम् + मूलम्", "म् before a consonant would be written ं: आमाशयं मूलम्."),
             ("आमाशयौ + मूलम्", "औ before a consonant stays औ: आमाशयौ मूलम्.")],
            "आमाशयः (the āmāśaya) + मूलम् (root): अः → ओ before a voiced consonant.",
            "अः before a voiced consonant → ओ."),
        mcq("apply", 4, "By unit 67, which side is named as a root of the food-carrying ones?",
            ("The left side", "वामपार्श्वं: वाम = left."),
            [("The right side", "Unit 67 names the left (वाम) side, not the right."),
             ("Both the sides", "Only one side, the left (वाम), is named."),
             ("The navel", "The navel is not named in unit 67.")],
            "The roots are the āmāśaya and the left side.",
            "अन्नवाहिनामामाशयो मूलं वामपार्श्वं च."),
        mcq("transfer", 5, "By the pattern of अवगच्छेत् (one should understand), which form of √पठ् means one should read?",
            ("पठेत्", "Verbs with a stem in अ (गच्छ, पठ) take -एत् in the 3rd singular optative."),
            [("पठति", "पठति is the present: reads."),
             ("पठितुम्", "पठितुम् is the infinitive: to read."),
             ("पठित्वा", "पठित्वा is the absolutive: having read.")],
            "पठेत् = one should read, like अवगच्छेत् = one should understand.",
            "Stem in अ + ईत् → -एत् (optative, 3rd sg).",
            teaches="For verbs whose present stem ends in अ, the 3rd singular optative ends in -एत्: गच्छ → गच्छेत्, पठ → पठेत्."),
    ],
}

# ---------------------------------------------------------------- unit 68
AUTHORED["68"] = {
    "title": "रसवाहिनां हृदयं मूलं दशधमन्यश्च",
    "question": "By unit 68, what is the root of the rasa-carrying (srotas)?",
    "rule": ("Of the rasa-carrying (ones) (रसवाहिनाम्), the root (मूलम्) is the heart (हृदयम्) and the ten dhamanīs "
             "(दश धमन्यः, vessels)."),
    "limits": ("Prose. The line does not say which ten dhamanīs; probably the upward ten that reach the heart (cards 47 "
               "and 48), but that is not stated: no question on it. Rasa is the nutrient fluid (a dhātu)."),
    "explain_hi": ("यहाँ से धातुओं के स्रोतस आरम्भ होते हैं: रस (पोषक द्रव, एक धातु) को वहन करने वालों का मूल हृदय और दस धमनियाँ हैं। "
                   "कौन-सी दस धमनियाँ, यह पंक्ति नहीं कहती; सम्भवतः इकाई ४७-४८ की ऊपर जाने वाली दस, जो हृदय तक पहुँचती हैं। "
                   "इकाई ६० में हृदय प्राणवह का भी मूल कहा गया था; दस धमनियाँ केवल यहाँ हैं। "
                   "‘मूलम्’ यहाँ छपा है; आगे की इकाइयों (६९-७७) में यह छपा नहीं, यहीं से समझा जाता है। "
                   "सन्धि: धमन्यः + च → धमन्यश्च (च से पहले विसर्ग → श्)।"),
    "hook": "रसवह का मूल: हृदय और दस धमनियाँ।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 68, what is the root of the rasa-carrying (srotas)?",
            ("The heart and the ten dhamanīs", "रसवाहिनां हृदयं मूलं दशधमन्यश्च."),
            [("The liver and also the spleen", "Liver and spleen belong to the blood-carrying ones (unit 69)."),
             ("The palate and the kloma organ", "Palate and kloma belong to the water-carrying ones (unit 64)."),
             ("The bladder and the two groins", "Bladder and groins belong to the urine-carrying ones (unit 75).")],
            "Of the rasa-carrying ones, the root is the heart and the ten dhamanīs.",
            "रसवाहिनां हृदयं मूलं दशधमन्यश्च."),
        order(1, "Put the printed words of unit 68 in the line's order.",
              ["रसवाहिनां", "हृदयं", "मूलं", "दशधमन्यश्च"],
              "Of the rasa-carrying, the heart, the root, and the ten dhamanīs.",
              "रसवाहिनां → हृदयं → मूलं → दशधमन्यश्च."),
        match(2, "Match each word of unit 68 to its meaning.",
              [["रस", "rasa, the nutrient fluid"], ["हृदय", "heart"], ["मूल", "root, origin"], ["दश", "ten"],
               ["धमनी", "dhamanī, vessel"]],
              "Of the rasa-carrying ones, the root is the heart and the ten dhamanīs.",
              "रस, हृदय, मूल, दश, धमनी.", role="extend",
              teaches="मूलम् is printed here; in units 69 to 77 it is understood from this unit."),
        mcq("discriminate", 3, "Which root is named for the rasa-carrying ones (unit 68) but not for the prāṇa-carrying ones (unit 60)?",
            ("The ten dhamanīs", "The ten dhamanīs are named only in unit 68."),
            [("The heart", "The heart is named in both units 60 and 68."),
             ("The great channel", "The great channel is named in unit 60, not unit 68."),
             ("The palate", "The palate is a root of the water-carrying ones (unit 64).")],
            "Both share the heart; the ten dhamanīs belong to rasa, the great channel to prāṇa.",
            "रसवाहिनां हृदयं मूलं दशधमन्यश्च · प्राणवाहिनां हृदयं मूलं महास्रोतश्च."),
        multi("apply", 4, "Which statements fit unit 68?",
              [("The heart is named as a root", "Right: हृदयं मूलम्."),
               ("The liver is named in this unit", "The liver is named for the blood-carrying ones (unit 69)."),
               ("मूलम् is printed in this unit", "Right: हृदयं मूलम्."),
               ("The great channel is named in this unit", "The great channel is in unit 60, not here.")],
              [0, 2],
              "Heart and ten dhamanīs; मूलम् printed; which ten is not stated.",
              "रसवाहिनां हृदयं मूलं दशधमन्यश्च."),
        mcq("transfer", 5, "By the pattern of धमनी → धमन्यः (vessels), what is the nominative plural of देवी (goddess)?",
            ("देव्यः", "A feminine ई-stem takes -यः in the nominative plural, as धमनी → धमन्यः."),
            [("देव्याः", "देव्याः is the genitive/ablative singular: of the goddess."),
             ("देवीषु", "देवीषु is the locative plural: in the goddesses."),
             ("देवीम्", "देवीम् is the accusative singular: the goddess.")],
            "देव्यः = goddesses, like धमन्यः = vessels.",
            "Feminine ई-stem, nominative plural: -यः.",
            teaches="A feminine ई-stem takes -यः in the nominative plural: धमनी → धमन्यः."),
    ],
}

# ---------------------------------------------------------------- unit 69
AUTHORED["69"] = {
    "title": "रक्तवाहिनां यकृत्प्लीहा च",
    "question": "By unit 69, what are named for the blood-carrying (srotas)?",
    "rule": ("Of the blood-carrying (ones) (रक्तवाहिनाम्): the liver (यकृत्) and the spleen (प्लीहा); 'root' (मूलम्) is "
             "understood from unit 68."),
    "limits": ("Prose, elliptical: मूलम् is not printed but carried over from card 68; 'srotas' is also unstated. "
               "यकृत् and प्लीहा are two words (nominatives), printed together."),
    "explain_hi": ("यह गद्य-पंक्ति रक्त वहन करने वालों (स्रोतस) के मूल बताती है: यकृत् यानी लीवर और प्लीहा यानी तिल्ली (दोनों मानक)। "
                   "‘मूलम्’ शब्द यहाँ छपा नहीं; इकाई ६८ से समझा जाता है। "
                   "छपा ‘यकृत्प्लीहा’ दो शब्द हैं: यकृत् (नपुंसक) और प्लीहा (प्लीहन्, पुंलिंग प्रथमा)। "
                   "यकृत् का त् प से पहले नहीं बदलता, क्योंकि प अघोष है।"),
    "hook": "रक्तवह का मूल: यकृत् और प्लीहा।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 69, what are named for the blood-carrying (srotas)?",
            ("The liver and the spleen", "रक्तवाहिनां यकृत्प्लीहा च."),
            [("The heart and ten dhamanīs", "Those are the roots of the rasa-carrying ones (unit 68)."),
             ("The kidneys and the flesh", "Those are named for the fat-carrying ones (unit 71)."),
             ("The joints and the bones", "Those are named for the marrow-carrying ones (unit 73).")],
            "Of the blood-carrying ones: the liver and the spleen.",
            "रक्तवाहिनां यकृत्प्लीहा च."),
        order(1, "Put the words of unit 69 in the line's order.",
              ["रक्तवाहिनां", "यकृत्", "प्लीहा", "च"],
              "Of the blood-carrying, the liver, the spleen, and.",
              "रक्तवाहिनां → यकृत् → प्लीहा → च."),
        match(2, "Match each word of unit 69 to its meaning.",
              [["रक्त", "blood"], ["वाहिन्", "carrying"], ["यकृत्", "liver"], ["प्लीहन्", "spleen"]],
              "Of the blood-carrying ones: the liver and the spleen.",
              "रक्त, वाहिन्, यकृत्, प्लीहन्.", role="extend",
              teaches="प्लीहा is the nominative singular of the masculine stem प्लीहन् (spleen)."),
        mcq("discriminate", 3, "In unit 69, why does यकृत् keep its त् before प्लीहा?",
            ("प is unvoiced, so त् stays", "A final त् stays before an unvoiced consonant such as प."),
            [("त् never changes in sandhi", "It does change: before a voiced sound त् → द् (शकृद्वाहिनाम्, unit 76)."),
             ("प्लीहा starts a new line", "Both words stand in the one printed line."),
             ("The print left out a vowel", "No flag is noted; यकृत् + प्लीहा is regular.")],
            "यकृत् + प्लीहा: त् stays before the unvoiced प.",
            "Final त् before an unvoiced consonant stays त्."),
        mcq("apply", 4, "In unit 69, which word is understood but not printed?",
            ("मूलम् (root), from unit 68", "Data: मूलम् is carried over from card 68 and not supplied."),
            [("हृदयम् (heart), from unit 68", "The heart is named for the rasa- (and prāṇa-) carrying ones; it is not carried over."),
             ("दश धमन्यः (ten vessels), from unit 68", "The ten dhamanīs belong to unit 68 only."),
             ("दुष्यन्ति (are vitiated), from unit 65", "No vitiation is spoken of in unit 69.")],
            "Liver and spleen are (the root) of the blood-carrying ones.",
            "रक्तवाहिनां (मूलं) यकृत्प्लीहा च."),
        mcq("transfer", 5, "By the rule of यकृत् + प्लीहा (त् stays), how is सत् + पुरुषः joined in a new example?",
            ("सत्पुरुषः", "Final त् stays before the unvoiced प, as यकृत्प्लीहा."),
            [("सद्पुरुषः", "द् comes from त् before a voiced sound; प is unvoiced."),
             ("सच्पुरुषः", "च् comes from त् before च/छ/श, not before प."),
             ("सन्पुरुषः", "न् comes (optionally) from त् before a nasal, not before प.")],
            "सत् + पुरुषः = सत्पुरुषः, like यकृत् + प्लीहा = यकृत्प्लीहा.",
            "Final त् before an unvoiced consonant stays.",
            teaches="A final त् stays त् before an unvoiced consonant such as प: यकृत्प्लीहा, सत्पुरुषः."),
    ],
}

# ---------------------------------------------------------------- unit 70
AUTHORED["70"] = {
    "title": "मांसवाहिनां स्नावानि त्वक्च",
    "question": "By unit 70, what are named for the flesh-carrying (srotas)?",
    "rule": ("Of the flesh-carrying (ones) (मांसवाहिनाम्): the sinews (स्नावानि, probably tendons or ligaments) and "
             "the skin (त्वक्); 'root' is understood from unit 68."),
    "limits": ("Prose, elliptical: मूलम् is carried over from card 68. Snāva as tendon or ligament (the same as "
               "snāyu) is probable, not certain. त्वक्च is printed joined for त्वक् च."),
    "explain_hi": ("यह गद्य-पंक्ति मांस वहन करने वालों (स्रोतस) के मूल बताती है: स्नाव और त्वचा। "
                   "स्नाव छपा रूप है; यह सम्भवतः स्नायु ही है, यानी कण्डरा या स्नायुबन्ध (सम्भावित पहचान)। "
                   "त्वक् = त्वचा (मानक); शब्द का मूल रूप त्वच् है, और शब्द के अन्त में च् → क् हो जाता है। "
                   "‘मूलम्’ इकाई ६८ से समझा जाता है।"),
    "hook": "मांसवह का मूल: स्नाव और त्वचा।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 70, what are named for the flesh-carrying (srotas)?",
            ("The sinews and the skin", "मांसवाहिनां स्नावानि त्वक्च."),
            [("The liver and the spleen", "Those belong to the blood-carrying ones (unit 69)."),
             ("The kidneys and the fat", "Kidneys and flesh, not fat, are named for the fat-carrying ones (unit 71)."),
             ("The palate and the kloma", "Those belong to the water-carrying ones (unit 64).")],
            "Of the flesh-carrying ones: the sinews and the skin.",
            "मांसवाहिनां स्नावानि त्वक्च."),
        order(1, "Put the words of unit 70 in the line's order.",
              ["मांसवाहिनां", "स्नावानि", "त्वक्", "च"],
              "Of the flesh-carrying, the sinews, the skin, and.",
              "मांसवाहिनां → स्नावानि → त्वक् → च."),
        match(2, "Match each word of unit 70 to its meaning.",
              [["मांस", "flesh"], ["स्नाव", "sinew (probably tendon, ligament)"], ["त्वच्", "skin"], ["वाहिन्", "carrying"]],
              "Of the flesh-carrying ones: the sinews and the skin.",
              "मांस, स्नाव, त्वच्, वाहिन्.", role="extend",
              teaches="स्नावानि is the neuter nominative plural of स्नाव (sinew)."),
        mcq("discriminate", 3, "In unit 70, why is the skin written त्वक्?",
            ("The stem त्वच् ends in च्, which turns to क् at word end", "Data: त्वक् from the stem त्वच्."),
            [("The stem is त्वक, and its final अ has been dropped", "The stem is त्वच्, not an अ-stem."),
             ("The क् is a print slip for च्, and no more than that", "No flag is noted; त्वक् is the regular form."),
             ("The क् comes from sandhi with the च (and) after it", "क् is the word's own final form, before any sandhi.")],
            "त्वच् → त्वक् at word end.",
            "A final च् of a stem becomes क् at word end."),
        multi("apply", 4, "Which statements fit unit 70?",
              [("Snāva as tendon is certain", "It is probable, not certain."),
               ("The sinews are named", "Right: स्नावानि."),
               ("मूलम् is printed in this unit", "It is carried over from card 68."),
               ("The skin is named", "Right: त्वक्.")],
              [1, 3],
              "Sinews (probably tendons, ligaments) and skin; मूलम् is understood.",
              "मांसवाहिनां स्नावानि त्वक्च."),
        mcq("transfer", 5, "By the pattern of त्वच् → त्वक्, what is the nominative singular of वाच् (speech) in a new example?",
            ("वाक्", "The final च् becomes क् at word end, as त्वच् → त्वक्."),
            [("वाचा", "वाचा is the instrumental singular: by speech."),
             ("वाचम्", "वाचम् is the accusative singular."),
             ("वाचः", "वाचः is the genitive/ablative singular or the plural.")],
            "वाच् → वाक्, like त्वच् → त्वक्.",
            "Stem-final च् → क् in the nominative singular.",
            teaches="A stem ending in च् shows क् at word end: त्वच् → त्वक्, वाच् → वाक्."),
    ],
}

# ---------------------------------------------------------------- unit 71
AUTHORED["71"] = {
    "title": "मेदोवाहिनांवृक्कौ मांसं च",
    "question": "By unit 71, what are named for the fat-carrying (srotas)?",
    "rule": ("Of the fat-carrying (ones) (मेदोवाहिनाम्): the two kidneys (वृक्कौ) and the flesh (मांसम्); 'root' is "
             "understood from unit 68."),
    "limits": ("Prose, elliptical: मूलम् is carried over from card 68. मेदोवाहिनांवृक्कौ is printed run together (a "
               "spacing slip). That the flesh is also the substance carried in unit 70 is an observation, not stated."),
    "explain_hi": ("यह गद्य-पंक्ति मेद यानी वसा (चर्बी) वहन करने वालों (स्रोतस) के मूल बताती है: दोनों वृक्क यानी गुर्दे (मानक) और मांस। "
                   "‘वृक्कौ’ द्विवचन है: दो गुर्दे। "
                   "छपाई में ‘मेदोवाहिनांवृक्कौ’ जुड़ा है; ये दो शब्द हैं। "
                   "ध्यान दें: अन्तिम मूल ‘मांस’ वही है जिसके वाहक इकाई ७० में थे (यह क्रम का अवलोकन है, पाठ स्वयं नहीं कहता)। "
                   "सन्धि: मेदस् + वाहिनाम् → मेदोवाहिनाम् (अस् + घोष व्यंजन → ओ)।"),
    "hook": "मेदोवह का मूल: दो गुर्दे और मांस।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 71, what are named for the fat-carrying (srotas)?",
            ("The two kidneys and the flesh", "मेदोवाहिनां वृक्कौ मांसं च."),
            [("The two groins and the bladder", "Those belong to the urine-carrying ones (unit 75)."),
             ("The heart and the ten dhamanīs", "Those belong to the rasa-carrying ones (unit 68)."),
             ("The palate and the kloma organ", "Those belong to the water-carrying ones (unit 64).")],
            "Of the fat-carrying ones: the two kidneys and the flesh.",
            "मेदोवाहिनां वृक्कौ मांसं च."),
        order(1, "Put the words of unit 71 in the line's order.",
              ["मेदोवाहिनाम्", "वृक्कौ", "मांसं", "च"],
              "Of the fat-carrying, the two kidneys, the flesh, and.",
              "मेदोवाहिनाम् → वृक्कौ → मांसं → च."),
        match(2, "Match each word of unit 71 to its meaning.",
              [["मेदस्", "fat"], ["वृक्कौ", "the two kidneys"], ["मांस", "flesh"], ["वाहिन्", "carrying"]],
              "Of the fat-carrying ones: the two kidneys and the flesh.",
              "मेदस्, वृक्कौ, मांस, वाहिन्.", role="extend",
              teaches="वृक्कौ is the masculine nominative dual of वृक्क: the two kidneys."),
        mcq("discriminate", 3, "Which split of मेदोवाहिनाम् in unit 71 is right?",
            ("मेदस् + वाहिनाम्", "अस् before a voiced consonant (व) becomes ओ: मेदोवाहिनाम्."),
            [("मेदा + वाहिनाम्", "आ before a consonant stays आ: मेदावाहिनाम्."),
             ("मेदम् + वाहिनाम्", "म् before a consonant would be written ं: मेदंवाहिनाम्."),
             ("मेदे + वाहिनाम्", "ए before a consonant stays ए: मेदेवाहिनाम्.")],
            "मेदस् (fat) + वाहिनाम् (of the carrying): अस् → ओ before a voiced consonant.",
            "अस् before a voiced consonant → ओ."),
        mcq("apply", 4, "Which root named in unit 71 is the substance carried in unit 70?",
            ("The flesh (māṃsa)", "Unit 70 names the flesh-carrying ones; unit 71 names the flesh as a root."),
            [("The kidneys (vṛkka)", "The kidneys are not carried by any srotas in units 68 to 77."),
             ("The skin (tvac)", "The skin is a root in unit 70; it is not named in unit 71."),
             ("The fat (medas)", "Fat is what unit 71's srotas carry, not a root named here.")],
            "Flesh: carried in unit 70, a root in unit 71.",
            "मांसवाहिनां ... (७०) · मेदोवाहिनां वृक्कौ मांसं च (७१)."),
        mcq("transfer", 5, "By the rule of मेदस् + वाहिनाम् → मेदोवाहिनाम्, how is मनस् + वेगः joined in a new example?",
            ("मनोवेगः", "अस् before a voiced consonant (व) becomes ओ, as मेदोवाहिनाम्."),
            [("मनावेगः", "आ does not come from अस् before a consonant."),
             ("मनर्वेगः", "र् comes from a visarga after vowels other than अ/आ."),
             ("मनस्वेगः", "स् does not stay before the voiced व; अस् → ओ.")],
            "मनस् + वेगः = मनोवेगः, like मेदस् + वाहिनाम् = मेदोवाहिनाम्.",
            "अस् before a voiced consonant → ओ.",
            teaches="A final अस् (अः) becomes ओ before a voiced consonant: मेदस् + वाहिनाम् → मेदोवाहिनाम्."),
    ],
}

# ---------------------------------------------------------------- unit 72
AUTHORED["72"] = {
    "title": "अस्थिवाहिनां जघनं मेदश्च",
    "question": "By unit 72, what are named for the bone-carrying (srotas)?",
    "rule": ("Of the bone-carrying (ones) (अस्थिवाहिनाम्): the jaghana (जघनम्, hips or loins region, probable) and "
             "fat (मेदः); 'root' is understood from unit 68."),
    "limits": ("Prose, elliptical: मूलम् is carried over from card 68. Jaghana is the hip or loin region; which part "
               "exactly is not stated (probable). Confidence medium."),
    "explain_hi": ("यह गद्य-पंक्ति अस्थि वहन करने वालों (स्रोतस) के मूल बताती है: जघन और मेद (वसा)। "
                   "जघन सम्भवतः कूल्हे या कमर का क्षेत्र है; ठीक कौन-सा भाग, यह नहीं बताया गया (सम्भावित पहचान)। "
                   "अन्तिम मूल ‘मेद’ वही है जिसके वाहक इकाई ७१ में थे (क्रम का अवलोकन)। "
                   "मेदः = मेदस् (नपुंसक) की प्रथमा एकवचन। "
                   "सन्धि: मेदः + च → मेदश्च (च से पहले विसर्ग → श्)।"),
    "hook": "अस्थिवह का मूल: जघन और मेद।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 72, what are named for the bone-carrying (srotas)?",
            ("The jaghana and the fat", "अस्थिवाहिनां जघनं मेदश्च."),
            [("The kidneys and the flesh", "Those belong to the fat-carrying ones (unit 71)."),
             ("The joints and the bones", "Those belong to the marrow-carrying ones (unit 73)."),
             ("The sinews and the skin", "Those belong to the flesh-carrying ones (unit 70).")],
            "Of the bone-carrying ones: the jaghana and fat.",
            "अस्थिवाहिनां जघनं मेदश्च."),
        order(1, "Put the printed words of unit 72 in the line's order.",
              ["अस्थिवाहिनां", "जघनं", "मेदश्च"],
              "Of the bone-carrying, the jaghana, and fat.",
              "अस्थिवाहिनां → जघनं → मेदश्च."),
        match(2, "Match each word of unit 72 to its meaning.",
              [["अस्थि", "bone"], ["जघन", "hip or loin region (probable)"], ["मेदस्", "fat"], ["वाहिन्", "carrying"]],
              "Of the bone-carrying ones: the jaghana and fat.",
              "अस्थि, जघन, मेदस्, वाहिन्.", role="extend",
              teaches="मेदः is the nominative singular of the neuter अस्-stem मेदस् (fat)."),
        mcq("discriminate", 3, "Which split of मेदश्च in unit 72 is right?",
            ("मेदः + च", "Visarga before च → श्: मेदश्च."),
            [("मेदम् + च", "म् before a consonant would be written ं: मेदं च."),
             ("मेदे + च", "ए before a consonant stays ए: मेदे च."),
             ("मेदत् + च", "त् before च would give च्: मेदच्च.")],
            "मेदः (fat) + च (and): visarga → श् before च.",
            "Visarga before च → श्."),
        multi("apply", 4, "Which statements fit unit 72?",
              [("Jaghana is named as the hip bone", "Jaghana is a region, probably hips or loins; which part is not stated."),
               ("मूलम् is printed in this unit", "It is carried over from card 68."),
               ("Fat is named here", "Right: मेदः."),
               ("The unit is about bone-carrying ones", "Right: अस्थिवाहिनाम्.")],
              [2, 3],
              "Bone-carrying: jaghana (probable) and fat; मूलम् understood.",
              "अस्थिवाहिनां जघनं मेदश्च."),
        mcq("transfer", 5, "By the pattern of मेदस् → मेदः, what is the nominative singular of the neuter मनस् (mind)?",
            ("मनः", "A neuter अस्-stem has -अः in the nominative singular, as मेदस् → मेदः."),
            [("मनांसि", "मनांसि is the nominative plural."),
             ("मनसा", "मनसा is the instrumental singular: by the mind."),
             ("मनसः", "मनसः is the genitive/ablative singular.")],
            "मनस् → मनः, like मेदस् → मेदः.",
            "Neuter अस्-stem, nominative singular: -अः.",
            teaches="A neuter अस्-stem takes -अः in the nominative singular: मेदस् → मेदः, मनस् → मनः."),
    ],
}

# ---------------------------------------------------------------- unit 73
AUTHORED["73"] = {
    "title": "मज्जवाहिनां पर्वाण्यस्थीनि च",
    "question": "By unit 73, what are named for the marrow-carrying (srotas)?",
    "rule": ("Of the marrow-carrying (ones) (मज्जवाहिनाम्): the joints (पर्वाणि) and the bones (अस्थीनि); 'root' is "
             "understood from unit 68."),
    "limits": ("Prose, elliptical: मूलम् is carried over from card 68. The picture of units 68 to 73 only puts the "
               "printed lines side by side; it adds nothing to them."),
    "explain_hi": ("यह गद्य-पंक्ति मज्जा वहन करने वालों (स्रोतस) के मूल बताती है: पर्व यानी जोड़ और अस्थियाँ। "
                   "समास में ‘मज्जा’ का रूप ‘मज्ज-’ है। "
                   "अन्तिम मूल ‘अस्थि’ वही है जिसके वाहक इकाई ७२ में थे (क्रम का अवलोकन)। "
                   "इकाई ६८ से ७३ तक रस, रक्त, मांस, मेद, अस्थि, मज्जा के वाहक इसी क्रम में आए हैं। "
                   "सन्धि: पर्वाणि + अस्थीनि → पर्वाण्यस्थीनि (इ + अ → य)।"),
    "hook": "मज्जवह का मूल: जोड़ और हड्डियाँ।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 73, what are named for the marrow-carrying (srotas)?",
            ("The joints and the bones", "मज्जवाहिनां पर्वाण्यस्थीनि च."),
            [("The jaghana and the fat", "Those belong to the bone-carrying ones (unit 72)."),
             ("The kidneys and the flesh", "Those belong to the fat-carrying ones (unit 71)."),
             ("The liver and the spleen", "Those belong to the blood-carrying ones (unit 69).")],
            "Of the marrow-carrying ones: the joints and the bones.",
            "मज्जवाहिनां पर्वाण्यस्थीनि च."),
        order(1, "Put the words of unit 73 in the line's order.",
              ["मज्जवाहिनां", "पर्वाणि", "अस्थीनि", "च"],
              "Of the marrow-carrying, the joints, the bones, and.",
              "मज्जवाहिनां → पर्वाणि → अस्थीनि → च."),
        match(2, "Match each word of unit 73 to its meaning.",
              [["मज्जा", "marrow"], ["पर्वन्", "joint"], ["अस्थि", "bone"], ["वाहिन्", "carrying"]],
              "Of the marrow-carrying ones: the joints and the bones.",
              "मज्जा, पर्वन्, अस्थि, वाहिन्.", role="extend",
              teaches="पर्वाणि and अस्थीनि are neuter nominative plurals of पर्वन् (joint) and अस्थि (bone)."),
        mcq("discriminate", 3, "Which split of पर्वाण्यस्थीनि in unit 73 is right?",
            ("पर्वाणि + अस्थीनि", "इ before अ becomes य्: पर्वाण्यस्थीनि."),
            [("पर्वाण + अस्थीनि", "अ + अ would give आ: पर्वाणास्थीनि."),
             ("पर्वाणे + अस्थीनि", "ए + अ would give एऽ: पर्वाणेऽस्थीनि."),
             ("पर्वाणु + अस्थीनि", "उ + अ would give व्: पर्वाण्वस्थीनि.")],
            "पर्वाणि (joints) + अस्थीनि (bones): इ + अ → य.",
            "इ before a different vowel → य्."),
        multi("apply", 4, "Which statements fit unit 73?",
              [("The joints are named", "Right: पर्वाणि."),
               ("The heart is named for the marrow-carrying ones", "No unit names the heart for marrow."),
               ("मूलम् is printed in this unit", "It is carried over from card 68."),
               ("The bones are named", "Right: अस्थीनि.")],
              [0, 3],
              "Marrow-carrying: joints and bones; मूलम् understood.",
              "मज्जवाहिनां पर्वाण्यस्थीनि च."),
        mcq("transfer", 5, "By the rule of पर्वाणि + अस्थीनि → पर्वाण्यस्थीनि, how is इति + अपि joined in a new example?",
            ("इत्यपि", "इ before अ becomes य्, as पर्वाणि + अस्थीनि → पर्वाण्यस्थीनि."),
            [("इतीपि", "ई comes from इ + इ, not from इ + अ."),
             ("इतापि", "आ comes from अ + अ, not from इ + अ."),
             ("इतेपि", "ए comes from अ + इ, not from इ + अ.")],
            "इति + अपि = इत्यपि, like पर्वाणि + अस्थीनि = पर्वाण्यस्थीनि.",
            "इ + अ → य.",
            teaches="इ before a different vowel becomes य्: पर्वाणि + अस्थीनि → पर्वाण्यस्थीनि."),
    ],
}

# ---------------------------------------------------------------- unit 74
AUTHORED["74"] = {
    "title": "शुकवाहिनां स्तनौ मुष्कौ मज्जा च",
    "question": "By unit 74, which three are named after शुकवाहिनां?",
    "rule": ("After शुकवाहिनां (read as śukra-vāhinām, 'of the semen-carrying'): the two breasts (स्तनौ), the two "
             "testicles (मुष्कौ) and the marrow (मज्जा); 'root' is understood from unit 68."),
    "limits": ("Prose. The printed शुक- lacks the r of śukra (a possible print slip, flagged): no question rests on that "
               "reading; the questions ask about the printed list. मूलम् and 'srotas' are carried over (cards 68 to 73). "
               "The breasts are listed as printed, not corrected."),
    "explain_hi": ("यह गद्य-पंक्ति छपे ‘शुकवाहिनां’ (सम्भवतः शुक्र यानी वीर्य वहन करने वाले) के मूल बताती है: दोनों स्तन, दोनों मुष्क यानी अण्डकोश (मानक) और मज्जा। "
                   "छपा ‘शुकवाहिनां’ है; ‘शुक्र’ का र् छपाई में छूटा लगता है (सम्भावित भूल)। "
                   "स्तनों का नाम छपे अनुसार इसी सूची में है; डेटा ने इसे नहीं बदला। "
                   "‘मूलम्’ और ‘स्रोतस’ इकाई ६८-७३ से समझे जाते हैं। "
                   "अन्तिम मूल ‘मज्जा’ वही है जिसके वाहक इकाई ७३ में थे (क्रम का अवलोकन)।"),
    "hook": "शुकवह (शुक्रवह) का मूल: दो स्तन, दो मुष्क, मज्जा।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 74, which three are named after शुकवाहिनां?",
            ("The breasts, the testicles and the marrow", "स्तनौ मुष्कौ मज्जा च."),
            [("The bladder, the two groins and the fat", "No such list is printed; bladder and groins are in unit 75."),
             ("The kidneys, the flesh and the hair-pores", "No such list is printed; kidneys and flesh are in unit 71."),
             ("The liver, the spleen and the ten vessels", "No such list is printed; liver and spleen are in unit 69.")],
            "Two breasts, two testicles and the marrow.",
            "शुकवाहिनां स्तनौ मुष्कौ मज्जा च."),
        order(1, "Put the words of unit 74 in the line's order.",
              ["शुकवाहिनां", "स्तनौ", "मुष्कौ", "मज्जा", "च"],
              "Of the (śukra)-carrying, the two breasts, the two testicles, the marrow, and.",
              "शुकवाहिनां → स्तनौ → मुष्कौ → मज्जा → च."),
        match(2, "Match each word of unit 74 to its meaning.",
              [["स्तनौ", "the two breasts"], ["मुष्कौ", "the two testicles"], ["मज्जा", "marrow"], ["वाहिन्", "carrying"]],
              "Two breasts, two testicles and the marrow.",
              "स्तनौ, मुष्कौ, मज्जा, वाहिन्.", role="extend",
              teaches="स्तनौ and मुष्कौ are masculine nominative duals: two each."),
        mcq("discriminate", 3, "Which of these is named in unit 74 but not in unit 73?",
            ("The testicles (muṣka)", "मुष्कौ is named only in unit 74."),
            [("The marrow (majjā)", "Marrow is named in both: carried in 73, a root in 74."),
             ("The bones (asthi)", "Bones are named in unit 73, not in 74."),
             ("The joints (parvan)", "Joints are named in unit 73, not in 74.")],
            "Unit 74 adds breasts and testicles; marrow links it to unit 73.",
            "मज्जवाहिनां पर्वाण्यस्थीनि (७३) · स्तनौ मुष्कौ मज्जा (७४)."),
        multi("apply", 4, "Which statements fit unit 74?",
              [("The breasts are listed, as printed", "Right: स्तनौ, not corrected by the data."),
               ("The kidneys are named here", "Kidneys are named in unit 71."),
               ("मूलम् is printed in this unit", "It is carried over (cards 68 to 73)."),
               ("Marrow is the last item named", "Right: ... मज्जा च.")],
              [0, 3],
              "Breasts, testicles, marrow; मूलम् understood.",
              "शुकवाहिनां स्तनौ मुष्कौ मज्जा च."),
        mcq("transfer", 5, "By the pattern of स्तन → स्तनौ (the two breasts), what is the nominative dual of the masculine वृक्ष (tree)?",
            ("वृक्षौ", "A masculine अ-stem takes -औ in the nominative dual, as स्तन → स्तनौ."),
            [("वृक्षाः", "वृक्षाः is the nominative plural: trees, more than two."),
             ("वृक्षम्", "वृक्षम् is the accusative singular: the tree."),
             ("वृक्षेण", "वृक्षेण is the instrumental singular: by the tree.")],
            "वृक्षौ = the two trees, like स्तनौ = the two breasts.",
            "Masculine अ-stem, nominative dual: -औ.",
            teaches="A masculine अ-stem takes -औ in the nominative dual: स्तन → स्तनौ, मुष्क → मुष्कौ."),
    ],
}

# ---------------------------------------------------------------- unit 75
AUTHORED["75"] = {
    "title": "मूत्रवाहिनांबस्तिर्वंक्षणौ च",
    "question": "By unit 75, what are named for the urine-carrying (srotas)?",
    "rule": ("Of the urine-carrying (ones) (मूत्रवाहिनाम्): the bladder (बस्तिः) and the two groins (वंक्षणौ); 'root' "
             "is understood (cards 68 to 73)."),
    "limits": ("Prose, elliptical: मूलम् is carried over. मूत्रवाहिनांबस्तिः is printed run together (a spacing slip). "
               "Basti here is the bladder, by the data; no question on the word's other senses."),
    "explain_hi": ("यह गद्य-पंक्ति मल-वर्ग का पहला स्रोतस लेती है: मूत्र वहन करने वालों के मूल बस्ति यानी मूत्राशय और दोनों वंक्षण यानी जाँघ के जोड़ (ग्रोइन)। "
                   "डेटा के अनुसार यहाँ बस्ति मूत्राशय है। "
                   "छपाई में ‘मूत्रवाहिनांबस्तिः’ जुड़ा है; ये दो शब्द हैं। "
                   "‘वंक्षणौ’ द्विवचन है: दोनों वंक्षण। "
                   "सन्धि: बस्तिः + वंक्षणौ → बस्तिर्वंक्षणौ (इ के बाद विसर्ग, घोष व्यंजन से पहले र्)।"),
    "hook": "मूत्रवह का मूल: बस्ति और दोनों वंक्षण।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 75, what are named for the urine-carrying (srotas)?",
            ("The bladder and the two groins", "मूत्रवाहिनां बस्तिर्वंक्षणौ च."),
            [("The two kidneys and the flesh", "Those belong to the fat-carrying ones (unit 71)."),
             ("The fat and the hair-pores too", "Those belong to the sweat-carrying ones (unit 77)."),
             ("The pakvāśaya and sthūlāntra", "Those belong to the stool-carrying ones (unit 76).")],
            "Of the urine-carrying ones: the bladder and the two groins.",
            "मूत्रवाहिनां बस्तिर्वंक्षणौ च."),
        order(1, "Put the words of unit 75 in the line's order.",
              ["मूत्रवाहिनाम्", "बस्तिः", "वंक्षणौ", "च"],
              "Of the urine-carrying, the bladder, the two groins, and.",
              "मूत्रवाहिनाम् → बस्तिः → वंक्षणौ → च."),
        match(2, "Match each word of unit 75 to its meaning.",
              [["मूत्र", "urine"], ["बस्ति", "bladder (here)"], ["वंक्षण", "groin"], ["वाहिन्", "carrying"]],
              "Of the urine-carrying ones: the bladder and the two groins.",
              "मूत्र, बस्ति, वंक्षण, वाहिन्.", role="extend",
              teaches="वंक्षणौ is the masculine nominative dual of वंक्षण: the two groins."),
        mcq("discriminate", 3, "Which split of बस्तिर्वंक्षणौ in unit 75 is right?",
            ("बस्तिः + वंक्षणौ", "After इ, a visarga before a voiced consonant (व) becomes र्."),
            [("बस्ती + वंक्षणौ", "ई before a consonant stays ई: बस्तीवंक्षणौ."),
             ("बस्तिम् + वंक्षणौ", "म् before a consonant would be written ं: बस्तिं वंक्षणौ."),
             ("बस्तेः + वंक्षणौ", "That would give बस्तेर्वंक्षणौ, with ए.")],
            "बस्तिः (bladder) + वंक्षणौ (two groins): इः → इर् before a voiced consonant.",
            "A visarga after इ before a voiced sound → र्."),
        multi("apply", 4, "Which statements fit unit 75?",
              [("The kidneys are named here", "Kidneys are named for the fat-carrying ones (unit 71)."),
               ("मूलम् is printed in this unit", "It is carried over."),
               ("The bladder is named", "Right: बस्तिः."),
               ("Two groins are named (a dual)", "Right: वंक्षणौ.")],
              [2, 3],
              "Urine-carrying: bladder and the two groins; मूलम् understood.",
              "मूत्रवाहिनां बस्तिर्वंक्षणौ च."),
        mcq("transfer", 5, "By the rule of बस्तिः + वंक्षणौ → बस्तिर्वंक्षणौ, how is मुनिः + वदति joined in a new example?",
            ("मुनिर्वदति", "After इ, a visarga before a voiced consonant becomes र्."),
            [("मुनिवदति", "The visarga after इ does not drop here; it becomes र्."),
             ("मुनिस्वदति", "स् comes from a visarga before त/थ, not before व."),
             ("मुनी वदति", "Lengthening with loss of र् happens only before र, not before व.")],
            "मुनिः + वदति = मुनिर्वदति, like बस्तिः + वंक्षणौ = बस्तिर्वंक्षणौ.",
            "इः before a voiced sound → इर्.",
            teaches="A visarga after इ becomes र् before a voiced sound: बस्तिः + वंक्षणौ → बस्तिर्वंक्षणौ."),
    ],
}

# ---------------------------------------------------------------- unit 76
AUTHORED["76"] = {
    "title": "शकृद्वाहिनां पक्वाशयः स्थूलांत्रं च",
    "question": "By unit 76, what are named for the stool-carrying (srotas)?",
    "rule": ("Of the stool-carrying (ones) (शकृद्वाहिनाम्): the pakvāśaya (पक्वाशयः, seat of the digested) and the "
             "thick intestine (स्थूलान्त्रम्); 'root' is understood (cards 68 to 73)."),
    "limits": ("Prose, elliptical: मूलम् is carried over. Pakvāśaya as the large-bowel region and sthūlāntra as the "
               "large intestine are probable identifications, not certain. Confidence medium."),
    "explain_hi": ("यह गद्य-पंक्ति शकृत् यानी मल वहन करने वालों के मूल बताती है: पक्वाशय और स्थूलान्त्र। "
                   "पक्वाशय = पक्व (पचा हुआ) + आशय (स्थान); इसे सम्भवतः बड़ी आँत का क्षेत्र माना गया है (सम्भावित)। "
                   "स्थूलान्त्र = स्थूल (मोटी) + अन्त्र (आँत), सम्भवतः बड़ी आँत (सम्भावित)। "
                   "इकाई ५२ में भी नीचे जाने वाली (सम्भवतः धमनियाँ; पंक्ति नाम नहीं लेती) पक्वाशय में स्थित कही गई थीं। "
                   "सन्धि: शकृत् + वाहिनाम् → शकृद्वाहिनाम् (घोष व्यंजन से पहले त् → द्)।"),
    "hook": "मलवह का मूल: पक्वाशय और स्थूल आँत।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 76, what are named for the stool-carrying (srotas)?",
            ("The pakvāśaya and the sthūlāntra", "शकृद्वाहिनां पक्वाशयः स्थूलांत्रं च."),
            [("The āmāśaya and the left-hand side", "Those are the roots of the food-carrying ones (unit 67)."),
             ("The bladder and the two groins", "Those belong to the urine-carrying ones (unit 75)."),
             ("The palate and the kloma organ", "Those belong to the water-carrying ones (unit 64).")],
            "Of the stool-carrying ones: the pakvāśaya and the thick intestine.",
            "शकृद्वाहिनां पक्वाशयः स्थूलांत्रं च."),
        order(1, "Put the words of unit 76 in the line's order.",
              ["शकृद्वाहिनां", "पक्वाशयः", "स्थूलांत्रं", "च"],
              "Of the stool-carrying, the pakvāśaya, the thick intestine, and.",
              "शकृद्वाहिनां → पक्वाशयः → स्थूलांत्रं → च."),
        match(2, "Match each word part of unit 76 to its meaning.",
              [["शकृत्", "stool, dung"], ["पक्व", "digested"], ["आशय", "seat"], ["स्थूल", "thick, large"],
               ["अन्त्र", "intestine"]],
              "शकृत् = stool; पक्व-आशय = seat of the digested; स्थूल-अन्त्र = thick intestine.",
              "शकृत्, पक्व, आशय, स्थूल, अन्त्र.", role="extend",
              teaches="पक्वाशय = पक्व + आशय and स्थूलान्त्र = स्थूल + अन्त्र: अ + आ / अ + अ → आ."),
        mcq("discriminate", 3, "Which split of शकृद्वाहिनां in unit 76 is right?",
            ("शकृत् + वाहिनाम्", "त् before a voiced consonant (व) becomes द्: शकृद्वाहिनाम्."),
            [("शकृः + वाहिनाम्", "A visarga after ऋ before व would give र्: शकृर्वाहिनाम्."),
             ("शकृन् + वाहिनाम्", "न् before व stays न्: शकृन्वाहिनाम्."),
             ("शकृम् + वाहिनाम्", "म् before a consonant would be written ं: शकृंवाहिनाम्.")],
            "शकृत् (stool) + वाहिनाम् (of the carrying): त् → द् before a voiced consonant.",
            "Final त् before a voiced consonant → द्."),
        multi("apply", 4, "Which statements fit unit 76?",
              [("Pakvāśaya is certainly the colon", "Large-bowel region is probable, not certain."),
               ("Sthūlāntra as large intestine is probable", "Right: the data labels it probable."),
               ("Two roots are named for stool", "Right: पक्वाशयः and स्थूलान्त्रम्."),
               ("The āmāśaya is named here", "The āmāśaya is in unit 67, for the food-carrying ones.")],
              [1, 2],
              "Stool-carrying: pakvāśaya and sthūlāntra, both probable identifications.",
              "शकृद्वाहिनां पक्वाशयः स्थूलांत्रं च."),
        mcq("transfer", 5, "By the rule of शकृत् + वाहिनाम् → शकृद्वाहिनाम्, how is मरुत् + गणः joined in a new example?",
            ("मरुद्गणः", "त् before a voiced consonant (ग) becomes द्, as शकृद्वाहिनाम्."),
            [("मरुत्गणः", "त् does not stay before a voiced consonant."),
             ("मरुच्गणः", "च् comes from त् before च/छ, not before ग."),
             ("मरुन्गणः", "न् comes (optionally) from त् before a nasal, not before ग.")],
            "मरुत् + गणः = मरुद्गणः, like शकृत् + वाहिनाम् = शकृद्वाहिनाम्.",
            "Final त् before a voiced consonant → द्.",
            teaches="A final त् becomes द् before a voiced consonant: शकृत् + वाहिनाम् → शकृद्वाहिनाम्."),
    ],
}

# ---------------------------------------------------------------- unit 77
AUTHORED["77"] = {
    "title": "स्वेदवाहिनांमेदो रोमकूपाश्च",
    "question": "By unit 77, what are named for the sweat-carrying (srotas)?",
    "rule": ("Of the sweat-carrying (ones) (स्वेदवाहिनाम्): fat (मेदः) and the hair-pores (रोमकूपाः); 'root' is "
             "understood (cards 68 to 73)."),
    "limits": ("Prose, elliptical: मूलम् is carried over. स्वेदवाहिनांमेदो is printed run together. Fat is also named "
               "for the bone-carrying ones (unit 72); questions keep to unit 77."),
    "explain_hi": ("यह गद्य-पंक्ति स्वेद यानी पसीना वहन करने वालों के मूल बताती है: मेद (चर्बी) और रोमकूप यानी रोमों के छिद्र। "
                   "इकाई ७५-७७ में मूत्र, शकृत् (मल) और स्वेद के वाहक इसी क्रम में आए हैं। "
                   "मेद इकाई ७२ में अस्थिवह का भी मूल कहा गया था। "
                   "छपाई में ‘स्वेदवाहिनांमेदो’ जुड़ा है; ये दो शब्द हैं। "
                   "सन्धि: मेदः + रोमकूपाः → मेदो रोमकूपाः (अः + घोष व्यंजन → ओ); रोमकूपाः + च → रोमकूपाश्च।"),
    "hook": "स्वेदवह का मूल: मेद और रोमकूप।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 77, what are named for the sweat-carrying (srotas)?",
            ("The fat and the hair-pores", "स्वेदवाहिनां मेदो रोमकूपाश्च."),
            [("The bladder and the groins", "Those belong to the urine-carrying ones (unit 75)."),
             ("The liver and the spleen", "Those belong to the blood-carrying ones (unit 69)."),
             ("The joints and the bones", "Those belong to the marrow-carrying ones (unit 73).")],
            "Of the sweat-carrying ones: fat and the hair-pores.",
            "स्वेदवाहिनां मेदो रोमकूपाश्च."),
        order(1, "Put the words of unit 77 in the line's order.",
              ["स्वेदवाहिनाम्", "मेदः", "रोमकूपाः", "च"],
              "Of the sweat-carrying, fat, the hair-pores, and.",
              "स्वेदवाहिनाम् → मेदः → रोमकूपाः → च."),
        match(2, "Match each word part of unit 77 to its meaning.",
              [["स्वेद", "sweat"], ["मेदस्", "fat"], ["रोम", "body hair"], ["कूप", "pit, pore"]],
              "Of the sweat-carrying ones: fat and the hair-pores (रोम-कूप).",
              "स्वेद, मेदस्, रोम, कूप.", role="extend",
              teaches="रोमकूप = रोम (hair) + कूप (pit): the pores of the body hair."),
        mcq("discriminate", 3, "Which split of मेदो रोमकूपाः in unit 77 is right?",
            ("मेदः + रोमकूपाः", "अः before a voiced consonant (र) becomes ओ: मेदो रोमकूपाः."),
            [("मेदे + रोमकूपाः", "ए before a consonant stays ए: मेदे रोमकूपाः."),
             ("मेदम् + रोमकूपाः", "म् before a consonant would be written ं: मेदं रोमकूपाः."),
             ("मेदाः + रोमकूपाः", "आः before a voiced sound drops the visarga: मेदा रोमकूपाः.")],
            "मेदः (fat) + रोमकूपाः (hair-pores): अः → ओ before a voiced consonant.",
            "अः before a voiced consonant → ओ."),
        mcq("apply", 4, "In unit 77, how are रोमकूपाः + च joined?",
            ("रोमकूपाश्च", "Visarga before च → श्."),
            [("रोमकूपास्च", "स् comes from a visarga before त/थ, not before च."),
             ("रोमकूपाच", "The visarga after आ drops only before a voiced sound; च is unvoiced."),
             ("रोमकूपार्च", "र् comes from a visarga after vowels other than अ/आ.")],
            "रोमकूपाः + च = रोमकूपाश्च.",
            "Visarga before च → श्."),
        mcq("transfer", 5, "By the rule of मेदः + रोमकूपाः → मेदो रोमकूपाः, how is बालः + रोदिति (the boy cries) written in a new example?",
            ("बालो रोदिति", "अः before a voiced consonant (र) becomes ओ, as मेदो रोमकूपाः."),
            [("बालर् रोदिति", "र् comes from a visarga after vowels other than अ/आ."),
             ("बालस् रोदिति", "स् comes from a visarga before त/थ, not before र."),
             ("बालः रोदिति", "Before a voiced consonant this visarga does not stay; अः → ओ.")],
            "बालः + रोदिति = बालो रोदिति, like मेदः + रोमकूपाः = मेदो रोमकूपाः.",
            "अः before a voiced consonant → ओ.",
            teaches="अः before a voiced consonant becomes ओ: मेदः + रोमकूपाः → मेदो रोमकूपाः."),
    ],
}


# ===================================================================== NOTES_HI
NOTES_HI = {
    "65": ("गद्य; विश्वास मध्यम। ‘तानि’ = इकाई ६४ के उदकवह स्रोतस। ‘आम’ का अर्थ यहाँ अनिश्चित (अपक्व पदार्थ या कच्चा), इस पर "
           "कोई प्रश्न नहीं। पाठ-चिह्न (सम्भावित): छपा ‘तृष्णिग्रह’ नियमित समास नहीं; ‘तृष्णानिग्रह’ (प्यास रोकना) अनुमानित पाठ, "
           "‘आन’ छूटना सम्भव; इस पर कोई प्रश्न नहीं। ‘अतिपान’ में क्या पिया, यह छपा नहीं। कर्णक्ष्वेडन = कानों में भनभनाहट, टिनिटस "
           "जैसा अर्थ सम्भावित। लक्षणों के साथ क्रिया नहीं। सन्धि जाँची: तानि + आम... → तान्याम... (इ + आ → या); भय + अतिपान → "
           "भयातिपान; अतिपान + उष्ण → अतिपानोष्ण (अ + उ → ओ); शुष्क + अन्न → शुष्कान्न; आदिभिः + दुष्यन्ति → आदिभिर्दुष्यन्ति; ततः + "
           "अतितृष्णा → ततोऽतितृष्णा (अः + अ → ओऽ); तमस् + दर्शनम् → तमोदर्शनम्; छपा दुष्यंति = दुष्यन्ति।"),
    "66": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। क्रिया नहीं; ‘तृष्णा में कही औषध’ कहीं और दिए उपचार की ओर संकेत, यहाँ "
           "दोहराया नहीं; कहाँ, यह नहीं कहा। सन्धि जाँची: तृष्णा + उक्तम् → तृष्णोक्तम् (आ + उ → ओ); उक्तम् + औषधम् → उक्तमौषधम् "
           "(स्वर से पहले म्)।"),
    "67": ("गद्य; दो छपी पंक्तियाँ (०२.०६.७५-७६); विश्वास उच्च; कोई पाठ-चिह्न नहीं। आमाशय = आम "
           "का आशय, सम्भवतः जठर (सम्भावित)। वामपार्श्व = बायाँ पार्श्व, आगे स्पष्ट नहीं। ‘मात्राशितीय’ को अध्याय का नाम माना गया; कौन-सा, "
           "यह नहीं जाँचा गया। दुष्टौ = दुष्टि की सप्तमी। सन्धि जाँची: अन्नवाहिनाम् + आमाशयः → अन्नवाहिनामामाशयः; आमाशयः + मूलम् → "
           "आमाशयो मूलम् (अः + घोष व्यंजन → ओ); आम + आशय → आमाशय (अ + आ → आ); मात्राशितीय + उक्तम् → मात्राशितीयोक्तम् (अ + उ → ओ); "
           "उक्तम् + अवगच्छेत् → उक्तमवगच्छेत्।"),
    "68": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। दस धमनियाँ सम्भवतः इकाई ४७-४८ की ऊपर जाने वाली दस (जो हृदय तक पहुँचती हैं), "
           "पर पंक्ति यह नहीं कहती; इस पर कोई प्रश्न नहीं। रस = पोषक द्रव (धातु)। हृदय (मानक)। सन्धि जाँची: रसवाहिनाम् + हृदयम् → "
           "रसवाहिनां हृदयं; हृदयम् + मूलम् → हृदयं मूलं; धमन्यः + च → धमन्यश्च (च से पहले विसर्ग → श्)।"),
    "69": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। ‘मूलम्’ इकाई ६८ से समझा जाता है, जोड़ा नहीं गया। ‘यकृत्प्लीहा’ दो शब्द: यकृत् "
           "(नपुंसक, मानक) और प्लीहा (प्लीहन्, पुंलिंग प्रथमा, मानक)। सन्धि जाँची: यकृत् + प्लीहा → यकृत्प्लीहा (अघोष प से पहले त् "
           "अपरिवर्तित); रक्तवाहिनाम् + यकृत् → रक्तवाहिनां यकृत्।"),
    "70": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। ‘मूलम्’ इकाई ६८ से। स्नाव (नपुंसक) छपा रूप; सम्भवतः स्नायु ही, यानी कण्डरा या "
           "स्नायुबन्ध (सम्भावित)। त्वक् = त्वच् (स्त्रीलिंग, मानक), अन्त में च् → क्। छपा ‘त्वक्च’ = त्वक् च। सन्धि जाँची: मांसवाहिनाम् "
           "+ स्नावानि → मांसवाहिनां स्नावानि।"),
    "71": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। ‘मूलम्’ इकाई ६८ से। छपा ‘मेदोवाहिनांवृक्कौ’ दो शब्द (रिक्त-स्थान की भूल)। मेदस् = "
           "वसा (मानक); वृक्क = गुर्दा (मानक), ‘वृक्कौ’ द्विवचन। सन्धि जाँची: मेदस् + वाहिनाम् → मेदोवाहिनाम् (अस् + घोष व्यंजन → ओ); "
           "वाहिनाम् + वृक्कौ → वाहिनां वृक्कौ; मांसम् + च → मांसं च।"),
    "72": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। ‘मूलम्’ इकाई ६८ से। जघन = कूल्हे या कमर का क्षेत्र, ठीक भाग नहीं बताया "
           "(सम्भावित)। मेदः = मेदस् (नपुंसक) प्रथमा एकवचन (मानक)। सन्धि जाँची: अस्थिवाहिनाम् + जघनम् → अस्थिवाहिनां जघनं; जघनम् + "
           "मेदः → जघनं मेदः; मेदः + च → मेदश्च (च से पहले विसर्ग → श्)।"),
    "73": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। ‘मूलम्’ इकाई ६८ से। समास में मज्जा का रूप ‘मज्ज-’। पर्वन् = जोड़ (मानक)। डेटा "
           "की टिप्पणी कहती है कि यह इकाई इस खण्ड की सूची समाप्त करती है; शुक्र और मल के वाहक आगे (इकाई ७४-७७)। सन्धि जाँची: "
           "पर्वाणि + अस्थीनि → पर्वाण्यस्थीनि (इ + अ → य); मज्जवाहिनाम् + पर्वाणि → मज्जवाहिनां पर्वाणि।"),
    "74": ("गद्य; विश्वास मध्यम। पाठ-चिह्न (सम्भावित): छपा ‘शुकवाहिनां’, शुक्र-वाहिन् का र् छूटा लगता है; ‘शुक्रवाहिनां’ सुझाया गया; "
           "इस पर कोई प्रश्न नहीं। ‘स्रोतस’ और ‘मूलम्’ इकाई ६८-७३ से समझे जाते हैं। स्तनों का नाम शुक्रवाहकों में छपे अनुसार, बदला "
           "नहीं गया। मुष्क = अण्डकोश (मानक); स्तनौ, मुष्कौ पुंलिंग द्विवचन। सन्धि जाँची: शुकवाहिनाम् + स्तनौ → शुकवाहिनां स्तनौ; "
           "मज्जा + च → मज्जा च।"),
    "75": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। छपा ‘मूत्रवाहिनांबस्तिः’ दो शब्द (रिक्त-स्थान की भूल)। बस्ति यहाँ मूत्राशय, "
           "एनिमा का उपकरण नहीं (डेटा)। ‘मूलम्’ इकाई ६८-७३ से। सन्धि जाँची: बस्तिः + वंक्षणौ → बस्तिर्वंक्षणौ (इ के बाद विसर्ग, घोष "
           "व्यंजन से पहले र्); छपा वंक्षणौ = वङ्क्षणौ।"),
    "76": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। पक्वाशय = बड़ी आँत का क्षेत्र, स्थूलान्त्र = बड़ी आँत: दोनों पहचान सम्भावित। "
           "‘मूलम्’ इकाई ६८-७३ से। सन्धि जाँची: शकृत् + वाहिनाम् → शकृद्वाहिनाम् (घोष व्यंजन से पहले त् → द्); पक्व + आशयः → "
           "पक्वाशयः (अ + आ → आ); स्थूल + अन्त्रम् → स्थूलान्त्रम् (अ + अ → आ); छपा स्थूलांत्रं = स्थूलान्त्रम्।"),
    "77": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। छपा ‘स्वेदवाहिनांमेदो’ दो शब्द (वाहिनाम् + मेदः)। रोमकूप = रोमों के छिद्र। "
           "‘मूलम्’ इकाई ६८-७३ से। सन्धि जाँची: मेदः + रोमकूपाः → मेदो रोमकूपाः (अः + घोष व्यंजन → ओ); रोमकूपाः + च → रोमकूपाश्च "
           "(च से पहले विसर्ग → श्)।"),
}


# ===================================================================== AIDS
AIDS = {
    "65": {
        "chain": {"steps": ["कारण: आम (अर्थ अनिश्चित), भय, अतिपान, उष्ण, शुष्क अन्न, छपा तृष्णिग्रह (पाठ अनुमानित), आदि",
                            "उदकवह स्रोतस (इकाई ६४) दूषित", "ततः १ अतितृष्णा", "२ मुखशोष", "३ कर्णक्ष्वेडन",
                            "४ तमोदर्शन"]},
        "chunks": "तान्यामभयातिपानोष्णशुष्कान्नतृष्णिग्रहादिभिर्दुष्यंति || ततोऽतितृष्णा | मुखशोषः | कर्णक्ष्वेडनं | तमोदर्शनं च",
        "sandhi": ("अ + उ → ओ: अतिपान + उष्ण → अतिपानोष्ण · अः + अ → ओऽ: ततः + अतितृष्णा → ततोऽतितृष्णा · अस् + घोष व्यंजन → ओ: "
                   "तमस् + दर्शनम् → तमोदर्शनम्।"),
        "frame": "किनका: तानि (उदकवह स्रोतस) → किससे: भय, अतिपान, उष्ण, शुष्क अन्न आदि → तब: प्यास, मुख-शोष, कान में भनभन, अँधेरा दिखना।",
    },
    "66": {
        "chunks": "तत्र | तृष्णोक्तमौषधं",
        "sandhi": "आ + उ → ओ: तृष्णा + उक्तम् → तृष्णोक्तम्।",
        "anchors": "संकेत-शैली: इकाई ६३ ‘श्वासवत्साधनम्’ (प्राणवह के लिए), इकाई ६६ ‘तृष्णोक्तमौषधम्’ (उदकवह के लिए)।",
    },
    "67": {
        "diagram": {"groups": [
            {"label": "अन्नवह स्रोतस", "items": ["मूल: आमाशय (सम्भवतः जठर)", "मूल: वामपार्श्व (बायाँ पार्श्व)",
                                              "दुष्टि में: सब कुछ मात्राशितीय में कहे अनुसार"]}]},
        "chunks": "अन्नवाहिनामामाशयो | मूलं | वामपार्श्वं च || तेषां दुष्टौ | सर्वं | मात्राशितीयोक्तमवगच्छेत्",
        "sandhi": "अः + घोष व्यंजन → ओ: आमाशयः + मूलम् → आमाशयो मूलम् · अ + आ → आ: आम + आशय → आमाशय · अ + उ → ओ: मात्राशितीय + उक्तम् → मात्राशितीयोक्तम्।",
        "frame": "कौन: अन्नवाहिनाम् → मूल: आमाशय + वामपार्श्व → दुष्टि में: मात्राशितीय में कहा सब समझें (अवगच्छेत्)।",
    },
    "68": {
        "diagram": {"groups": [
            {"label": "रसवह स्रोतस का मूल", "items": ["हृदय", "दस धमनियाँ (कौन-सी, छपा नहीं)"]}]},
        "chunks": "रसवाहिनां | हृदयं | मूलं | दशधमन्यश्च",
        "anchors": "ढाँचा: [क्या]-वाहिनाम् + [मूल]; ‘मूलम्’ यहाँ छपा, इकाई ६९-७७ में यहीं से समझा जाता है। याद रखें: इकाई ६० (प्राणवह) में भी हृदय मूल है, वहाँ साथ में महास्रोतस।",
    },
    "69": {
        "chunks": "रक्तवाहिनां | यकृत्प्लीहा च",
        "frame": "कौन: रक्तवाहिनाम् → (मूल, इकाई ६८ से): यकृत् (लीवर) + प्लीहा (तिल्ली)।",
        "sandhi": "अघोष प से पहले त् नहीं बदलता: यकृत् + प्लीहा → यकृत्प्लीहा।",
    },
    "70": {
        "chunks": "मांसवाहिनां | स्नावानि | त्वक्च",
        "frame": "कौन: मांसवाहिनाम् → (मूल): स्नाव (सम्भवतः कण्डरा, स्नायुबन्ध) + त्वक् (त्वचा)।",
        "anchors": "त्वच् → त्वक्: शब्द के अन्त में च् → क् (वाच् → वाक् भी)।",
    },
    "71": {
        "chunks": "मेदोवाहिनां | वृक्कौ | मांसं च",
        "frame": "कौन: मेदोवाहिनाम् → (मूल): दो वृक्क (गुर्दे) + मांस।",
        "sandhi": "अस् + घोष व्यंजन → ओ: मेदस् + वाहिनाम् → मेदोवाहिनाम्।",
        "anchors": "अन्तिम मूल ‘मांस’ = इकाई ७० में वहन होने वाला (छपे क्रम का अवलोकन, पाठ का कथन नहीं)।",
    },
    "72": {
        "chunks": "अस्थिवाहिनां | जघनं | मेदश्च",
        "frame": "कौन: अस्थिवाहिनाम् → (मूल): जघन (सम्भवतः कूल्हा या कमर) + मेद।",
        "sandhi": "च से पहले विसर्ग → श्: मेदः + च → मेदश्च।",
        "anchors": "अन्तिम मूल ‘मेद’ = इकाई ७१ में वहन होने वाला (छपे क्रम का अवलोकन)।",
    },
    "73": {
        "diagram": {"groups": [
            {"label": "इकाई ६८-७३: वाहक और मूल, छपे क्रम से", "items": [
                "६८ रसवह: हृदय, दस धमनियाँ", "६९ रक्तवह: यकृत्, प्लीहा",
                "७० मांसवह: स्नाव (सम्भवतः कण्डरा), त्वचा", "७१ मेदोवह: दो वृक्क, मांस",
                "७२ अस्थिवह: जघन (सम्भावित), मेद", "७३ मज्जवह: पर्व (जोड़), अस्थियाँ"]}]},
        "chunks": "मज्जवाहिनां | पर्वाण्यस्थीनि च",
        "sandhi": "इ + अ → य: पर्वाणि + अस्थीनि → पर्वाण्यस्थीनि।",
        "letters": "वाहकों का क्रम, पहले अक्षर: र-र-मां-मे-अ-म (रस, रक्त, मांस, मेद, अस्थि, मज्जा)। (मेरी याद-पद्धति)",
    },
    "74": {
        "chain": {"steps": ["७० मांसवह", "७१ मेदोवह: अन्तिम मूल मांस", "७२ अस्थिवह: अन्तिम मूल मेद",
                            "७३ मज्जवह: अन्तिम मूल अस्थियाँ", "७४ शुकवह: अन्तिम मूल मज्जा"]},
        "chunks": "शुकवाहिनां | स्तनौ | मुष्कौ | मज्जा च",
        "frame": "कौन: शुकवाहिनाम् (शुक्र, सम्भावित पाठ) → (मूल): दो स्तन + दो मुष्क + मज्जा।",
        "anchors": "इकाई ७१-७४: हर इकाई का अन्तिम मूल पिछली इकाई में वहन होने वाला है (छपे क्रम का अवलोकन, पाठ का कथन नहीं)।",
    },
    "75": {
        "chunks": "मूत्रवाहिनां | बस्तिर्वंक्षणौ च",
        "frame": "कौन: मूत्रवाहिनाम् → (मूल): बस्ति (मूत्राशय) + दो वंक्षण।",
        "sandhi": "इ के बाद विसर्ग, घोष व्यंजन से पहले र्: बस्तिः + वंक्षणौ → बस्तिर्वंक्षणौ।",
    },
    "76": {
        "chunks": "शकृद्वाहिनां | पक्वाशयः | स्थूलांत्रं च",
        "frame": "कौन: शकृद्वाहिनाम् (मल) → (मूल): पक्वाशय + स्थूलान्त्र (दोनों पहचान सम्भावित)।",
        "sandhi": "घोष व्यंजन से पहले त् → द्: शकृत् + वाहिनाम् → शकृद्वाहिनाम् · अ + आ → आ: पक्व + आशय → पक्वाशय।",
    },
    "77": {
        "diagram": {"groups": [
            {"label": "इकाई ७५-७७: वाहक और मूल, छपे क्रम से", "items": [
                "७५ मूत्रवह: बस्ति (मूत्राशय), दो वंक्षण", "७६ शकृद्वह: पक्वाशय, स्थूलान्त्र (सम्भावित)",
                "७७ स्वेदवह: मेद, रोमकूप"]}]},
        "chunks": "स्वेदवाहिनां | मेदो | रोमकूपाश्च",
        "sandhi": "अः + घोष व्यंजन → ओ: मेदः + रोमकूपाः → मेदो रोमकूपाः · च से पहले विसर्ग → श्: रोमकूपाः + च → रोमकूपाश्च।",
        "frame": "कौन: स्वेदवाहिनाम् → (मूल): मेद + रोमकूप (रोमों के छिद्र)।",
    },
}


# ===================================================================== IMAGE_SPECS
IMAGE_SPECS = {
    ("65", "chain"): {
        "file": "sh6-udakavaha-dushti-65.svg",
        "alt": ("Flowchart of unit 65: causes (āma, sense uncertain; fear; excessive drinking; heat; dry food; the printed tṛṣṇigraha, conjectural; and the like), boxed in rows of two, vitiate the water-carrying srotas; then four signs in printed order: excessive thirst, dry mouth, ringing in the ears, seeing darkness."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  subgraph CS[\" \"]\n"
                 "    direction LR\n"
                 "    C1[\"आम<br/>(अर्थ अनिश्चित)\"] ~~~ C2[\"भय\"]\n"
                 "    C3[\"अतिपान\"] ~~~ C4[\"उष्ण\"]\n"
                 "    C5[\"शुष्क अन्न\"] ~~~ C6[\"छपा तृष्णिग्रह<br/>(पाठ अनुमानित)\"]\n"
                 "    C7[\"आदि\"]\n"
                 "  end\n"
                 "  CS --> D[\"उदकवह स्रोतस दूषित\"]\n"
                 "  D --> S1[\"१ अतितृष्णा\"]\n"
                 "  D --> S2[\"२ मुखशोष\"]\n"
                 "  S1 ~~~ S3\n"
                 "  S2 ~~~ S4\n"
                 "  D --> S3[\"३ कर्णक्ष्वेडन\"]\n"
                 "  D --> S4[\"४ तमोदर्शन\"]\n"),
    },
    ("67", "diagram"): {
        "file": "sh6-annavaha-67.svg",
        "alt": ("Table of unit 67, food-carrying srotas: roots are the āmāśaya (probably the stomach) and the left side; "
                "in their vitiation, all as the Mātrāśitīya states."),
        "type": "table",
        "title": "इकाई ६७: अन्नवह स्रोतस",
        "heads": ["विषय", "पाठ"],
        "rows": [["मूल", "आमाशय (सम्भवतः जठर)"], ["मूल", "वामपार्श्व (बायाँ पार्श्व)"],
                 ["दुष्टि में", "सब कुछ मात्राशितीय में कहे अनुसार"]],
    },
    ("68", "diagram"): {
        "file": "sh6-rasavaha-68.svg",
        "alt": "Flowchart of unit 68: the root of the rasa-carrying srotas is the heart and the ten dhamanīs (which ten is not stated).",
        "type": "mermaid",
        "code": ('flowchart TD\n'
                 '  A["रसवह स्रोतस"] --> M["मूल"]\n'
                 '  M --> H["हृदय"]\n'
                 '  M --> D["दस धमनियाँ"]\n'),
    },
    ("73", "diagram"): {
        "file": "sh6-dhatuvaha-68-73.svg",
        "alt": ("Table of units 68 to 73 in printed order, carriers and roots: rasa, heart and ten dhamanīs; blood, liver "
                "and spleen; flesh, sinews (probably tendons) and skin; fat, two kidneys and flesh; bone, jaghana "
                "(probable) and fat; marrow, joints and bones."),
        "type": "table",
        "title": "इकाई ६८-७३: वाहक और मूल",
        "heads": ["वाहक (इकाई)", "मूल"],
        "rows": [["६८ रसवह", "हृदय, दस धमनियाँ"], ["६९ रक्तवह", "यकृत्, प्लीहा"],
                 ["७० मांसवह", "स्नाव (सम्भवतः कण्डरा), त्वचा"], ["७१ मेदोवह", "दो वृक्क, मांस"],
                 ["७२ अस्थिवह", "जघन (सम्भावित), मेद"], ["७३ मज्जवह", "पर्व (जोड़), अस्थियाँ"]],
    },
    ("74", "chain"): {
        "file": "sh6-antima-mula-74.svg",
        "alt": ("Chain of units 70 to 74: flesh-carrying (70); fat-carrying, last root flesh (71); bone-carrying, last root "
                "fat (72); marrow-carrying, last root bones (73); printed śuka-carrying, last root marrow (74)."),
        "type": "chain",
        "title": "अन्तिम मूल = पिछला वाहक (अवलोकन)",
        "steps": ["७० मांसवह", "७१ मेदोवह: अन्तिम मूल मांस", "७२ अस्थिवह: अन्तिम मूल मेद",
                  "७३ मज्जवह: अन्तिम मूल अस्थियाँ", "७४ शुकवह: अन्तिम मूल मज्जा"],
    },
    ("77", "diagram"): {
        "file": "sh6-malavaha-75-77.svg",
        "alt": ("Table of units 75 to 77 in printed order: urine-carrying, bladder and two groins; stool-carrying, "
                "pakvāśaya and sthūlāntra (probable); sweat-carrying, fat and hair-pores."),
        "type": "table",
        "title": "इकाई ७५-७७: वाहक और मूल",
        "heads": ["वाहक (इकाई)", "मूल"],
        "rows": [["७५ मूत्रवह", "बस्ति (मूत्राशय), दो वंक्षण"], ["७६ शकृद्वह", "पक्वाशय, स्थूलान्त्र (सम्भावित)"],
                 ["७७ स्वेदवह", "मेद, रोमकूप"]],
    },
}
