from helpers import mcq, match, order, fill, multi, accepts


AUTHORED = {}

# ---------------------------------------------------------------- unit 179
AUTHORED["179"] = {
    "title": "तत्रैकैकस्मिन् सक्थिनि",
    "question": "By unit 179, how many peśī (muscles) are given in each toe of a lower limb?",
    "rule": ("In each single lower limb (सक्थि), in each toe (पादाङ्गुली), three (तिस्रः). The feminine तिस्रः shows "
             "that the counted items are the feminine peśī (muscles) of unit 175."),
    "limits": ("Prose; no verb and no noun for the counted item are printed. सक्थि may mean the thigh or the whole lower "
               "limb; 'lower limb' is the data's choice because the toes are counted under it. Unit 180 gives 'those are "
               "fifteen' without the arithmetic: no question here on a total."),
    "explain_hi": ("यह गद्य-पंक्ति पेशियों (मांसपेशियों) की गिनती में निचले अंग पर आती है। "
                   "वहाँ, एक-एक सक्थि (निचले अंग) में, पाँव की हर अँगुली में तीन-तीन पेशियाँ बताई गई हैं। "
                   "‘तिस्रः’ स्त्रीलिंग है, इससे पता चलता है कि गिनी गई वस्तु स्त्रीलिंग ‘पेशी’ है (इकाई १७५ में आरम्भ)। "
                   "‘सक्थि’ जाँघ या पूरा निचला अंग हो सकता है; यहाँ पूरा निचला अंग लिया गया, क्योंकि अँगुलियाँ उसी में गिनी गई हैं। "
                   "‘तत्रैकैकस्मिन्’ = तत्र + एकैकस्मिन् (अ + ए → ऐ)।"),
    "hook": "हर पादांगुली में तीन पेशियाँ: तिस्रः, स्त्रीलिंग।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 179, how many peśī (muscles) are in each toe?",
            ("Three (तिस्रः)", "पादाङ्गुल्यां प्रत्येकं तिस्रः: three in each toe."),
            [("Thirty (त्रिंशत्)", "The line says three (तिस्रः), not thirty."),
             ("Five (पञ्च)", "The line says three (तिस्रः), not five."),
             ("Four (चतस्रः)", "The line says three (तिस्रः), not four.")],
            "Three in each toe of each lower limb.",
            "प्रत्येकं तिस्रः = three in each."),
        order(1, "Put the printed words of unit 179 in the line's order.",
              ["तत्रैकैकस्मिन्", "सक्थिनि", "पादांगुल्यां", "प्रत्येकं", "तिस्रः"],
              "There, in each single lower limb, in the toe, in each, three.",
              "तत्रैकैकस्मिन् → सक्थिनि → पादांगुल्यां → प्रत्येकं → तिस्रः."),
        match(2, "Match each word of unit 179 to its meaning.",
              [["तत्र", "there"], ["सक्थि", "lower limb (here)"], ["पादाङ्गुली", "toe"], ["प्रत्येकम्", "in each"],
               ["तिस्रः", "three (feminine)"]],
              "There, in each lower limb, in each toe, three.",
              "तत्र, सक्थि, पादाङ्गुली, प्रत्येकम्, तिस्रः.", role="extend",
              teaches="पादाङ्गुली = पाद (foot) + अङ्गुली (finger): a toe."),
        mcq("discriminate", 3, "Which split of तत्रैकैकस्मिन् in unit 179 is right?",
            ("तत्र + एकैकस्मिन्", "अ + ए → ऐ: तत्र + एकैकस्मिन् → तत्रैकैकस्मिन्."),
            [("तत्रै + कैकस्मिन्", "तत्रै and कैकस्मिन् are not words; the words are तत्र and एकैकस्मिन्."),
             ("तत् + रैकैकस्मिन्", "रैकैकस्मिन् is not a word; तत्र (there) is one word."),
             ("तत्रे + कैकस्मिन्", "तत्रे and कैकस्मिन् are not words; the words are तत्र and एकैकस्मिन्.")],
            "तत्र (there) + एकैकस्मिन् (in each single): अ + ए → ऐ.",
            "अ + ए → ऐ."),
        mcq("apply", 4, "Which word of unit 179 shows that the counted items are feminine?",
            ("तिस्रः (three)", "The data: tisraḥ is f. nom. pl., so the counted items (peśī) are feminine."),
            [("सक्थिनि (in the limb)", "सक्थिनि is the place (n. loc. sg.); it does not agree with the counted items."),
             ("प्रत्येकं (in each)", "प्रत्येकम् is an indeclinable; it has no gender to show."),
             ("तत्र (there)", "तत्र is an indeclinable; it has no gender to show.")],
            "Only the number word agrees with the counted items: तिस्रः is feminine.",
            "तिस्रः = three, feminine (masc. त्रयः, neut. त्रीणि)."),
        mcq("transfer", 5, "By the rule of तत्र + एकैकस्मिन्, how is अत्र + एव (here itself) written when joined?",
            ("अत्रैव", "अ + ए → ऐ, as तत्र + एकैकस्मिन् → तत्रैकैकस्मिन्."),
            [("अत्रेव", "ए comes from अ + इ; अ + ए gives ऐ."),
             ("अत्रौव", "औ comes from अ + ओ or अ + औ, not from अ + ए."),
             ("अत्रयेव", "अय् comes from ए before a vowel; अत्र ends in अ.")],
            "अत्र + एव = अत्रैव, like तत्र + एकैकस्मिन् = तत्रैकैकस्मिन्.",
            "अ + ए → ऐ.",
            teaches="Short अ before ए joins as ऐ: तत्र + एकैकस्मिन् → तत्रैकैकस्मिन्."),
    ],
}

# ---------------------------------------------------------------- unit 180
AUTHORED["180"] = {
    "title": "ताः पंचदश",
    "question": "By unit 180, what number follows the toe count?",
    "rule": ("'Those are fifteen' (ताः पञ्चदश). ताः is feminine plural, like the feminine peśī counted before; "
             "पञ्चदश = पञ्च (five) + दश (ten)."),
    "limits": ("Prose, two words; the copula is understood. The Sanskrit does not give the arithmetic or say exactly "
               "which items make the fifteen: questions ask only that this is left unstated, never how it is reached."),
    "explain_hi": ("यह दो शब्दों की गद्य-पंक्ति है: ‘ताः पंचदश’, वे पन्द्रह हैं। "
                   "‘ताः’ स्त्रीलिंग बहुवचन है, जो स्त्रीलिंग पेशियों से मेल खाता है। "
                   "‘पञ्चदश’ = पञ्च (पाँच) + दश (दस), यानी पन्द्रह। "
                   "पन्द्रह कैसे बने, यह संस्कृत नहीं बताती; डेटा संख्या को छपे रूप में ही रखता है। "
                   "क्रिया ‘हैं’ समझी जाती है।"),
    "hook": "पाँच और दस: पञ्चदश, पन्द्रह।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What number does unit 180 give?",
            ("Fifteen (पञ्चदश)", "ताः पंचदश: those are fifteen."),
            [("Fifty (पञ्चाशत्)", "Fifty would be पञ्चाशत्; the line has पंचदश."),
             ("Twelve (द्वादश)", "Twelve would be द्वादश; the line has पंचदश."),
             ("Eleven (एकादश)", "Eleven would be एकादश; the line has पंचदश.")],
            "Those are fifteen.",
            "पञ्चदश = fifteen."),
        match(1, "Match each part of unit 180 to its meaning.",
              [["ताः", "those (feminine)"], ["पञ्च", "five"], ["दश", "ten"], ["पञ्चदश", "fifteen"]],
              "ताः पञ्चदश = those are fifteen; पञ्च + दश = fifteen.",
              "ताः, पञ्च, दश, पञ्चदश."),
        fill(2, "In unit 180 the number 'fifteen' is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("पञ्चदश", "pañcadaśa", "पंचदश", "panchadasha", "panchadasa"),
             "पञ्चदश = पञ्च (five) + दश (ten): fifteen.",
             "पञ्चदश = fifteen.",
             "ताः पंचदश."),
        mcq("discriminate", 3, "Which of these does unit 180 leave unstated?",
            ("How the fifteen is reached", "The note: the Sanskrit does not give the arithmetic."),
            [("That the number is fifteen", "The number is printed: पंचदश."),
             ("That 'those' is a plural", "ताः is printed, a nominative plural."),
             ("That 'those' is feminine", "ताः is a feminine form (f. nom. pl.).")],
            "The number is printed; how it is reached is not.",
            "ताः पंचदश: number given, arithmetic not."),
        mcq("apply", 4, "Unit 102 counts bones with तानि पंचदश. Why does unit 180 have ताः instead?",
            ("ताः is feminine, for the feminine peśī", "ताः is f. nom. pl.; the counted peśī is feminine."),
            [("ताः is neuter, for the neuter bones", "Bones (अस्थि) are neuter, hence तानि in unit 102; ताः is feminine."),
             ("ताः is singular, for one single limb", "ताः is plural (f. nom. pl.), not singular."),
             ("ताः is masculine, for the toes", "ताः is feminine; the masculine would be ते.")],
            "Neuter तानि for bones (unit 102), feminine ताः for peśī.",
            "तद् in nom. pl.: ते (m.), ताः (f.), तानि (n.)."),
        mcq("transfer", 5, "By पञ्च + दश = पञ्चदश (fifteen), what does सप्तदश mean in a new example?",
            ("Seventeen", "सप्त (seven) + दश (ten) = seventeen, as पञ्च + दश = fifteen."),
            [("Seventy", "Seventy is सप्तति, not सप्तदश."),
             ("Seven tens", "A unit before दश adds to ten: seven + ten, not seven tens."),
             ("Seven each", "'Seven each' would be सप्त सप्त; दश here is ten.")],
            "सप्तदश = seventeen, like पञ्चदश = fifteen.",
            "Number + दश = that number plus ten.",
            teaches="पञ्चदश = पञ्च + दश: a unit before दश is added to ten (fifteen)."),
    ],
}

# ---------------------------------------------------------------- unit 181
AUTHORED["181"] = {
    "title": "दश दश प्रपदे पादतले गुल्फे च",
    "question": "By unit 181, which parts of the foot get ten each, and what is said of the kūrma?",
    "rule": ("Ten each (दश दश, distributive) in the forepart of the foot (प्रपद), the sole (पादतल) and the ankle (गुल्फ). "
             "Likewise, (ones) situated above the foot, in the kūrma (probably a tortoise-shaped part of the foot)."),
    "limits": ("Prose, two printed lines; no noun or verb (peśī carried from unit 175). Whether 'ten each' is per leg is "
               "not stated. No numeral is printed for the kūrma, and none is supplied. Kūrma as a foot part is probable "
               "only: no question on what it is."),
    "explain_hi": ("यह दो छपी पंक्तियों की गद्य-इकाई है। "
                   "पहली पंक्ति: प्रपद (पैर का अगला भाग), पादतल (तलवा) और गुल्फ (टखना) में दस-दस पेशियाँ; ‘दश दश’ का दोहराव ‘दस-दस’ का अर्थ देता है। "
                   "दूसरी पंक्ति: वैसे ही पैर के ऊपर कूर्म में स्थित; कूर्म शब्दशः कछुआ है, यहाँ सम्भवतः पैर का कछुए की पीठ जैसा ऊपरी भाग। "
                   "कूर्म के लिए कोई संख्या नहीं छपी; डेटा कोई संख्या नहीं जोड़ता। "
                   "दस-दस हर पैर में हैं या नहीं, यह नहीं कहा गया।"),
    "hook": "आगे, तले, टखने में दस-दस; ऊपर कूर्म।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 181, how many are given in the prapada, the sole and the ankle?",
            ("Ten in each of the three", "दश दश: the doubled number means ten each."),
            [("Ten in all three together", "The doubled दश दश means ten each, not ten in all."),
             ("Twenty in each of the three", "The line has दश (ten), not विंशति (twenty)."),
             ("Three in each of the three", "The line has दश (ten), not तिस्रः (three).")],
            "Ten each in the forepart, the sole and the ankle.",
            "दश दश = ten each."),
        order(1, "Put the printed parts of unit 181 in the line's order.",
              ["दश दश", "प्रपदे", "पादतले", "गुल्फे च", "तथा पादस्योपरि", "कूर्म्मे सन्निविष्टाः"],
              "Ten each in the forepart, the sole and the ankle; likewise, above the foot, situated in the kūrma.",
              "दश दश → प्रपदे → पादतले → गुल्फे च → तथा पादस्योपरि → कूर्म्मे सन्निविष्टाः."),
        match(2, "Match each word of unit 181 to its meaning.",
              [["प्रपद", "forepart of the foot"], ["पादतल", "sole of the foot"], ["गुल्फ", "ankle"],
               ["उपरि", "above"], ["दश दश", "ten each"]],
              "Ten each in the forepart, the sole and the ankle; then above the foot.",
              "प्रपद, पादतल, गुल्फ, उपरि, दश दश.", role="extend",
              teaches="पादतल = पाद (foot) + तल (surface, bottom): the sole of the foot."),
        mcq("discriminate", 3, "Which split of पादस्योपरि in unit 181 is right?",
            ("पादस्य + उपरि", "अ + उ → ओ: पादस्य + उपरि → पादस्योपरि."),
            [("पादस्य + ओपरि", "ओपरि is not a word, and अ + ओ would give औ, not ओ."),
             ("पादस्यो + परि", "पादस्यो is not a form; the genitive is पादस्य."),
             ("पादः + स्योपरि", "स्योपरि is not a word; the words are पादस्य and उपरि.")],
            "पादस्य (of the foot) + उपरि (above): अ + उ → ओ.",
            "अ + उ → ओ."),
        multi("apply", 4, "Which statements fit unit 181?",
              [("दश दश means ten each", "Right: the doubled number is distributive."),
               ("It says the ten each is per leg", "The note: per leg is not stated."),
               ("It prints no numeral for the kūrma", "Right: no numeral is printed in the second line."),
               ("It prints the word peśī again", "No noun is printed; peśī is carried from unit 175.")],
              [0, 2],
              "Ten each in three places; the kūrma line has no numeral.",
              "दश दश प्रपदे पादतले गुल्फे च; तथा पादस्योपरि कूर्म्मे सन्निविष्टाः."),
        mcq("transfer", 5, "By the pattern of दश दश (ten each), what does पञ्च पञ्च mean in a new example?",
            ("Five each", "A doubled number is distributive: पञ्च पञ्च = five each, as दश दश = ten each."),
            [("Ten in all", "Doubling does not add the numbers; it means 'each'."),
             ("Fifty-five", "Fifty-five is पञ्चपञ्चाशत्, not पञ्च पञ्च."),
             ("Five tens", "Doubling does not multiply; it means 'each'.")],
            "पञ्च पञ्च = five each, like दश दश = ten each.",
            "Doubled number = so many each.",
            teaches="A number said twice is distributive: दश दश = ten each."),
    ],
}

# ---------------------------------------------------------------- unit 182
AUTHORED["182"] = {
    "title": "विंशतिर्जंघायां",
    "question": "By unit 182, what number is given for the jaṅghā (lower leg)?",
    "rule": ("Twenty (विंशतिः) in the jaṅghā, the leg below the knee. विंशतिः + जङ्घायाम् → विंशतिर्जङ्घायाम्: a visarga "
             "after इ becomes र् before a voiced sound."),
    "limits": ("Prose, one printed word; no noun or verb (peśī carried from unit 175). In Hindi जाँघ/जंघा usually means "
               "the thigh; the Sanskrit जङ्घा here is the lower leg. Per leg or in all is not said."),
    "explain_hi": ("यह एक छपे शब्द की गद्य-पंक्ति है: जङ्घा में बीस। "
                   "संस्कृत ‘जङ्घा’ घुटने के नीचे की टाँग है; हिन्दी में ‘जाँघ’ प्रायः घुटने के ऊपर का भाग है, इसलिए भ्रम न हो। "
                   "जाँघ के लिए संस्कृत शब्द ‘ऊरु’ है (इकाई १८४)। "
                   "‘विंशतिर्जंघायां’ = विंशतिः + जङ्घायाम्; घोष व्यंजन ज से पहले इ के बाद का विसर्ग र् बना। "
                   "गिनी गई वस्तु (पेशी) और क्रिया छपी नहीं।"),
    "hook": "जङ्घा = घुटने के नीचे; वहाँ बीस।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 182, what number is given for the jaṅghā (lower leg)?",
            ("Twenty (विंशतिः)", "विंशतिर्जंघायां: twenty in the jaṅghā."),
            [("Thirty (त्रिंशत्)", "The line has विंशतिः (twenty), not thirty."),
             ("Five (पञ्च)", "The line has विंशतिः (twenty), not five."),
             ("Ten (दश)", "The line has विंशतिः (twenty), not ten.")],
            "Twenty in the lower leg.",
            "विंशतिः = twenty."),
        match(1, "Match each part of unit 182 to its meaning.",
              [["विंशतिः", "twenty"], ["जङ्घा", "lower leg"], ["जङ्घायाम्", "in the lower leg"]],
              "विंशतिः जङ्घायाम् = twenty in the lower leg.",
              "विंशतिः, जङ्घा, जङ्घायाम्."),
        fill(2, "In unit 182 the leg below the knee is called ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("जङ्घा", "jaṅghā", "जंघा", "जङ्घायाम्", "jangha"),
             "जङ्घा = the leg below the knee; जङ्घायाम् = in it.",
             "जङ्घा = lower leg (standard).",
             "विंशतिर्जङ्घायाम्."),
        mcq("discriminate", 3, "In unit 182, which part of the leg is the jaṅghā?",
            ("The leg below the knee", "The data: jaṅghā = lower leg, below the knee."),
            [("The leg above the knee", "Above the knee is the thigh (ऊरु), not the jaṅghā."),
             ("The knee joint itself", "The knee is जानु, not the jaṅghā."),
             ("The sole of the foot", "The sole is पादतल, not the jaṅghā.")],
            "Sanskrit जङ्घा = lower leg; Hindi जाँघ (thigh) is a false friend.",
            "जङ्घा = lower leg; ऊरु = thigh."),
        mcq("apply", 4, "Which split of विंशतिर्जंघायां in unit 182 is right?",
            ("विंशतिः + जङ्घायाम्", "A visarga after इ becomes र् before the voiced ज."),
            [("विंशति + र्जङ्घायाम्", "र्जङ्घायाम् is not a word; the र् is the changed visarga."),
             ("विंशतिम् + जङ्घायाम्", "म् before ज becomes ं or ञ्, never र्."),
             ("विंशतिर + जङ्घायाम्", "विंशतिर is not a form; the number is विंशतिः.")],
            "विंशतिः (twenty) + जङ्घायाम् (in the lower leg): इः + voiced consonant → इर्.",
            "इः + voiced consonant → इर्."),
        mcq("transfer", 5, "By the rule of विंशतिर्जङ्घायाम्, how is मुनिः + गच्छति (the sage goes) joined?",
            ("मुनिर्गच्छति", "A visarga after इ becomes र् before a voiced sound, as विंशतिः + जङ्घायाम्."),
            [("मुनो गच्छति", "ओ comes from अः before a voiced consonant, not from इः."),
             ("मुनिस्गच्छति", "स् does not come before a voiced ग; the visarga after इ becomes र्."),
             ("मुनि गच्छति", "After इ the visarga is not dropped before a voiced sound; it becomes र्.")],
            "मुनिः + गच्छति = मुनिर्गच्छति, like विंशतिः + जङ्घायाम् = विंशतिर्जङ्घायाम्.",
            "इः + voiced consonant → इर्.",
            teaches="A visarga after a vowel other than अ/आ becomes र् before a voiced sound: विंशतिः + जङ्घायाम् → विंशतिर्जङ्घायाम्."),
    ],
}

# ---------------------------------------------------------------- unit 183
AUTHORED["183"] = {
    "title": "पंच जानुनि",
    "question": "By unit 183, what number is given for the knee (jānu)?",
    "rule": ("Five (पञ्च) in the knee (जानुनि, locative singular of the neuter u-stem जानु). Number and place are printed; "
             "the counted peśī and the verb are understood."),
    "limits": ("Prose, two words; no noun or verb (peśī carried from unit 175). Per leg or in all is not said."),
    "explain_hi": ("यह दो शब्दों की गद्य-पंक्ति है: जानु यानी घुटने में पाँच। "
                   "‘जानुनि’ उकारान्त नपुंसकलिंग ‘जानु’ का सप्तमी एकवचन है: घुटने में। "
                   "छपे क्रम में यह जङ्घा (इकाई १८२) के बाद और ऊरु (इकाई १८४) से पहले आता है। "
                   "गिनी गई वस्तु (पेशी) और क्रिया छपी नहीं।"),
    "hook": "घुटने में पाँच: पंच जानुनि।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 183, what number is given for the knee?",
            ("Five (पञ्च)", "पंच जानुनि: five in the knee."),
            [("Ten (दश)", "The line has पञ्च (five), not ten."),
             ("Twenty (विंशतिः)", "The line has पञ्च (five), not twenty."),
             ("Six (षट्)", "The line has पञ्च (five), not six.")],
            "Five in the knee.",
            "पञ्च = five; जानुनि = in the knee."),
        match(1, "Match each part of unit 183 to its meaning.",
              [["पञ्च", "five"], ["जानु", "knee"], ["जानुनि", "in the knee"]],
              "पञ्च जानुनि = five in the knee.",
              "पञ्च, जानु, जानुनि."),
        fill(2, "In unit 183 the knee is called ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("जानु", "jānu", "जानुनि", "janu"),
             "जानु = knee; जानुनि = in the knee.",
             "जानु = knee (standard).",
             "पंच जानुनि."),
        mcq("discriminate", 3, "Which form is जानुनि in unit 183?",
            ("Locative singular: in the knee", "The data: n. loc. sg."),
            [("Nominative dual: two knees", "The nominative dual is जानुनी, with long ई."),
             ("Genitive singular: of the knee", "The genitive singular is जानुनः."),
             ("Instrumental singular: by the knee", "The instrumental singular is जानुना.")],
            "जानुनि = in the knee (neuter u-stem, locative singular).",
            "Neuter उ-stem + -नि = locative singular."),
        mcq("apply", 4, "In unit 183, what is printed and what is understood?",
            ("Number and place printed; noun and verb understood", "पञ्च and जानुनि are printed; peśī and 'are' are not."),
            [("Number and noun printed; place and verb understood", "The place जानुनि is printed; no noun is."),
             ("Place and verb printed; number and noun understood", "The number पञ्च is printed; no verb is."),
             ("Noun and verb printed; number and place understood", "Neither noun nor verb is printed.")],
            "Number + place printed; noun (peśī) and verb understood.",
            "पंच जानुनि: number + place."),
        mcq("transfer", 5, "By the pattern of जानु → जानुनि (in the knee), how is वस्तु (n., thing) put in the locative singular?",
            ("वस्तुनि", "A neuter उ-stem takes -नि in the locative singular, as जानु → जानुनि."),
            [("वस्तुना", "-ना is the instrumental, 'by the thing'."),
             ("वस्तुनः", "-नः is the genitive/ablative, 'of/from the thing'."),
             ("वस्तूनि", "वस्तूनि is the nominative/accusative plural, 'things'.")],
            "वस्तुनि = in the thing, like जानुनि = in the knee.",
            "Neuter उ-stem + -नि = locative singular.",
            teaches="जानुनि is the locative singular of the neuter u-stem जानु: -उनि means 'in'."),
    ],
}

# ---------------------------------------------------------------- unit 184
AUTHORED["184"] = {
    "title": "ऊरु में बीस",
    "question": "By unit 184, what number is given for the thigh (ūru)?",
    "rule": ("Twenty (विंशतिः) in the thigh (ऊरौ, locative of ऊरु). Read विंशतिरूरौ = विंशतिः + ऊरौ: a visarga after इ "
             "becomes र् before a vowel."),
    "limits": ("Prose, one word; no noun or verb (peśī carried from unit 175). The printed Devanagari (विंशतिरू्रौ) is "
               "garbled; the reading विंशतिरूरौ is the data's, without difficulty. Per leg or in all is not said."),
    "explain_hi": ("यह एक शब्द की गद्य-पंक्ति है: ऊरु यानी जाँघ में बीस। "
                   "छपी देवनागरी ‘विंशतिरू्रौ’ बिगड़ी हुई है; डेटा इसे बिना कठिनाई ‘विंशतिरूरौ’ = विंशतिः + ऊरौ पढ़ता है। "
                   "स्वर ऊ से पहले इ के बाद का विसर्ग र् बना। "
                   "‘ऊरौ’ उकारान्त पुंलिंग ‘ऊरु’ का सप्तमी एकवचन है। "
                   "ऊरु घुटने के ऊपर की जाँघ है, जबकि जङ्घा (इकाई १८२) घुटने के नीचे का भाग।"),
    "hook": "ऊरु = जाँघ, घुटने के ऊपर; वहाँ बीस।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 184, what number is given for the thigh (ūru)?",
            ("Twenty (विंशतिः)", "विंशतिरूरौ: twenty in the thigh."),
            [("Forty (चत्वारिंशत्)", "The line has विंशतिः (twenty), not forty."),
             ("Five (पञ्च)", "The line has विंशतिः (twenty), not five."),
             ("Ten (दश)", "The line has विंशतिः (twenty), not ten.")],
            "Twenty in the thigh.",
            "विंशतिः = twenty; ऊरौ = in the thigh."),
        match(1, "Match each part of unit 184 to its meaning.",
              [["विंशतिः", "twenty"], ["ऊरु", "thigh"], ["ऊरौ", "in the thigh"]],
              "विंशतिः ऊरौ = twenty in the thigh.",
              "विंशतिः, ऊरु, ऊरौ."),
        fill(2, "In unit 184 the thigh is called ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("ऊरु", "ūru", "ऊरौ", "uru"),
             "ऊरु = thigh; ऊरौ = in the thigh.",
             "ऊरु = thigh (standard).",
             "विंशतिरूरौ = विंशतिः ऊरौ."),
        mcq("discriminate", 3, "In unit 184, which part of the leg is the ūru?",
            ("The leg above the knee", "The data: ūru = thigh."),
            [("The leg below the knee", "Below the knee is the jaṅghā, not the ūru."),
             ("The knee joint itself", "The knee is जानु, not the ūru."),
             ("The ankle of the foot", "The ankle is गुल्फ, not the ūru.")],
            "ऊरु = thigh, above the knee.",
            "ऊरु = thigh; जङ्घा = lower leg."),
        mcq("apply", 4, "The data reads unit 184 as विंशतिरूरौ. Which split is right?",
            ("विंशतिः + ऊरौ", "A visarga after इ becomes र् before a vowel."),
            [("विंशती + ऊरौ", "ई + ऊ would give य्: विंशत्यूरौ, with no र्."),
             ("विंशतिम् + ऊरौ", "म् before a vowel stays म्: विंशतिमूरौ."),
             ("विंशति + रूरौ", "रूरौ is not a word; the र् is the changed visarga.")],
            "विंशतिः (twenty) + ऊरौ (in the thigh): इः + vowel → इर्.",
            "इः + vowel → इर् + that vowel."),
        mcq("transfer", 5, "By the rule of विंशतिः + ऊरौ, how is मुनिः + अयम् (this sage) joined?",
            ("मुनिरयम्", "A visarga after इ becomes र् before a vowel, as विंशतिः + ऊरौ → विंशतिरूरौ."),
            [("मुन्ययम्", "य् comes from इ with no visarga; here the visarga becomes र्."),
             ("मुनोऽयम्", "ओऽ comes from अः before अ, not from इः."),
             ("मुनि अयम्", "After इ the visarga is not dropped before a vowel; it becomes र्.")],
            "मुनिः + अयम् = मुनिरयम्, like विंशतिः + ऊरौ = विंशतिरूरौ.",
            "इः + vowel → इर्.",
            teaches="A visarga after a vowel other than अ/आ becomes र् before a voiced sound (vowels included): विंशतिः + ऊरौ → विंशतिरूरौ."),
    ],
}

# ---------------------------------------------------------------- unit 185
AUTHORED["185"] = {
    "title": "एकैका मेंद्रसेवन्योः",
    "question": "By unit 185, how many are given in each of the two named sites?",
    "rule": ("One each (एकैका, feminine like peśī) in the two sites named by one dual compound: the meḍhra (penis; printed मेंद्र, a possible reading) and the "
             "sevanī (probably the seam, the raphe). The dual -योः shows two sites."),
    "limits": ("Prose; no noun or verb (peśī carried from unit 175). Printed मेंद्र is read मेढ्र (a possible reading, as in "
               "unit 156); sevanī = raphe is probable only. No question on either reading; questions use एकैका and the dual."),
    "explain_hi": ("यह गद्य-पंक्ति कहती है: मेढ्र (लिंग) और सेवनी (सम्भवतः सीवन, यानी मध्य रेखा) में एक-एक पेशी। "
                   "छपा ‘मेंद्र’ कोई शब्द नहीं; डेटा इसे ‘मेढ्र’ पढ़ता है (ढ्र का ‘ंद्र’ पढ़ा जाना सम्भव), जैसा इकाई १५६ में। "
                   "‘एकैका’ = एक + एक → एकैक (अ + ए → ऐ), स्त्रीलिंग रूप, क्योंकि गिनी गई पेशी स्त्रीलिंग है। "
                   "समास के अन्त में द्विवचन ‘-योः’ है, क्योंकि दो स्थान गिनाए गए हैं। "
                   "वर्णन चिकित्सा-ग्रन्थ की शरीर-रचना है, सीधे शब्दों में।"),
    "hook": "दो स्थान, एक-एक पेशी: एकैका।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 185, how many are given in each of the two named sites?",
            ("One in each (एकैका)", "एकैका: one each."),
            [("Two in each (द्वे द्वे)", "The line has एकैका, one each."),
             ("Ten in each (दश दश)", "The line has एकैका, one each."),
             ("Three in each (तिस्रः)", "The line has एकैका, one each.")],
            "One each in the two sites.",
            "एकैका = one each."),
        match(1, "Match each sure part of unit 185 to its meaning.",
              [["एक", "one"], ["एकैका", "one each"], ["-योः", "in the two (locative dual)"],
               ["-आ (in एकैका)", "feminine ending"]],
              "One each in the two sites; -योः marks the two.",
              "एक, एकैका, -योः, -आ."),
        fill(2, "In unit 185 'one each' is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("एकैका", "ekaikā", "ekaika"),
             "एकैका = one each: एक + एक → एकैक, feminine एकैका.",
             "एकैका = one each.",
             "एकैका मेंद्रसेवन्योः."),
        mcq("discriminate", 3, "Why does the compound of unit 185 end in the dual -योः?",
            ("It joins two named sites", "The note: the dual is used because two sites are named."),
            [("It counts two in each site", "The number is एकैका, one each, not two."),
             ("It is a plural of respect", "-योः is a dual ending, not a plural one."),
             ("It is a singular, 'in the seam'", "In the seam alone would be सेवन्याम्, singular.")],
            "Two sites in one dvandva, so the ending is dual.",
            "Here the dvandva names two sites, so it is dual."),
        mcq("apply", 4, "How is एकैका of unit 185 formed?",
            ("एक + एक → एकैक, made feminine", "अ + ए → ऐ; the feminine -आ agrees with peśī."),
            [("एक + ऐक → एकैक, made neuter", "ऐक is not a word, and एकैका is feminine, not neuter."),
             ("एके + एक → एकैक, made feminine", "एके is not the first part; एक + एक gives एकैक."),
             ("एक + एका → एकैक, made plural", "एकैका is singular (f. nom. sg.), not plural.")],
            "एक + एक → एकैक (अ + ए → ऐ), feminine एकैका.",
            "अ + ए → ऐ."),
        mcq("transfer", 5, "By the pattern of सेवनी → सेवन्योः (in the two), how is नदी (river) put in the locative dual?",
            ("नद्योः", "An ई-stem takes -योः in the locative dual: ई → य्, as सेवनी → सेवन्योः."),
            [("नदीषु", "-षु is the locative plural, in three or more."),
             ("नद्याम्", "नद्याम् is the locative singular, 'in the river'."),
             ("नदीभ्याम्", "-भ्याम् is never a locative; 'in the two' is -योः.")],
            "नद्योः = in the two rivers, like सेवन्योः = in the two (sites).",
            "ई-stem + -योः = locative dual.",
            teaches="सेवन्योः ends a dvandva in the locative dual: ई-stem + -योः."),
    ],
}

# ---------------------------------------------------------------- unit 186
AUTHORED["186"] = {
    "title": "द्वे वृषणयोः",
    "question": "By unit 186, what number is given for the two testicles (vṛṣaṇa)?",
    "rule": ("Two (द्वे) in the two testicles (वृषणयोः, locative dual of वृषण). द्वे is the feminine/neuter 'two'; "
             "the masculine is द्वौ."),
    "limits": ("Prose, two words; no noun or verb (peśī carried from unit 175). The line does not say whether the two "
               "are one in each testicle or two in each: no question on that."),
    "explain_hi": ("यह दो शब्दों की गद्य-पंक्ति है: दोनों वृषणों (अण्ड-ग्रन्थियों) में दो। "
                   "‘वृषणयोः’ अकारान्त पुंलिंग ‘वृषण’ का सप्तमी द्विवचन है: दोनों वृषणों में। "
                   "‘द्वे’ स्त्रीलिंग/नपुंसकलिंग का ‘दो’ है; स्त्रीलिंग पेशी के लिए यही रूप आता है (पुंलिंग में ‘द्वौ’)। "
                   "दो पेशियाँ हर वृषण में एक-एक हैं या कुल, यह पंक्ति नहीं बताती। "
                   "गिनी गई वस्तु और क्रिया छपी नहीं।"),
    "hook": "दो वृषण, दो पेशियाँ: द्वे वृषणयोः।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 186, what number is given for the vṛṣaṇas (testicles)?",
            ("Two (द्वे)", "द्वे वृषणयोः: two in the two testicles."),
            [("Twelve (द्वादश)", "The line has द्वे (two), not twelve."),
             ("One (एका)", "The line has द्वे (two), not one."),
             ("Six (षट्)", "The line has द्वे (two), not six.")],
            "Two in the two testicles.",
            "द्वे = two."),
        match(1, "Match each part of unit 186 to its meaning.",
              [["द्वे", "two"], ["वृषण", "testicle"], ["वृषणयोः", "in the two testicles"]],
              "द्वे वृषणयोः = two in the two testicles.",
              "द्वे, वृषण, वृषणयोः."),
        mcq("extend", 2, "In unit 186, what is the vṛṣaṇa?",
            ("The testicle", "The data: vṛṣaṇa = testicle (standard)."),
            [("The bladder", "The bladder is बस्ति, not vṛṣaṇa."),
             ("The buttock", "The buttock is स्फिज्, not vṛṣaṇa."),
             ("The navel", "The navel is नाभि, not vṛṣaṇa.")],
            "वृषण = testicle; वृषणयोः = in the two testicles.",
            "वृषण = testicle (standard).",
            teaches="वृषण = testicle; the locative dual वृषणयोः = in the two testicles."),
        mcq("discriminate", 3, "Which form of वृषण means 'in the two testicles'?",
            ("वृषणयोः", "-योः on an अ-stem is the locative dual."),
            [("वृषणेषु", "-एषु is the locative plural, in three or more."),
             ("वृषणे", "-ए on an अ-stem is the locative singular."),
             ("वृषणाभ्याम्", "-आभ्याम् is never a locative; 'in the two' is -योः.")],
            "वृषणयोः = in the two testicles (locative dual).",
            "अ-stem + -योः = locative dual."),
        multi("apply", 4, "Which statements fit unit 186?",
              [("Its verb 'are' is printed", "No verb is printed; it is understood."),
               ("द्वे is the feminine/neuter 'two'", "Right: the masculine would be द्वौ."),
               ("It prints the noun peśī", "No noun is printed; peśī is carried from unit 175."),
               ("वृषणयोः is a locative dual", "Right: the data labels it m. loc. du.")],
              [1, 3],
              "Feminine/neuter द्वे and the locative dual वृषणयोः; no verb printed.",
              "द्वे वृषणयोः."),
        mcq("transfer", 5, "By the pattern of वृषण → वृषणयोः, how is नेत्र (eye) put in the locative dual?",
            ("नेत्रयोः", "An अ-stem takes -योः for the locative dual, as वृषण → वृषणयोः."),
            [("नेत्रेषु", "-एषु is the locative plural, in three or more."),
             ("नेत्रे", "Here -ए would be 'in the eye', singular."),
             ("नेत्राभ्याम्", "-आभ्याम् is never a locative; 'in the two' is -योः.")],
            "नेत्रयोः = in the two eyes, like वृषणयोः = in the two testicles.",
            "अ-stem + -योः = locative dual.",
            teaches="वृषणयोः is a locative dual: -योः on an अ-stem means 'in the two'."),
    ],
}

# ---------------------------------------------------------------- unit 187
AUTHORED["187"] = {
    "title": "दश स्फिजोः",
    "question": "By unit 187, what number is given for the two buttocks (sphij)?",
    "rule": ("Ten (दश) in the two buttocks (स्फिजोः, locative dual of the consonant-stem स्फिज्, feminine)."),
    "limits": ("Prose, two words; no noun or verb (peśī carried from unit 175). Five per side or ten each is not stated: "
               "no question on how the ten are shared."),
    "explain_hi": ("यह दो शब्दों की गद्य-पंक्ति है: दोनों स्फिज् यानी नितम्बों में दस। "
                   "‘स्फिजोः’ व्यंजनान्त स्त्रीलिंग ‘स्फिज्’ का सप्तमी द्विवचन है: दोनों नितम्बों में। "
                   "व्यंजनान्त शब्द में सप्तमी (और षष्ठी) द्विवचन का अन्त ‘-ओः’ होता है (अकारान्त में ‘-अयोः’)। "
                   "दस हर ओर हैं या कुल, यह पंक्ति नहीं बताती। "
                   "गिनी गई वस्तु और क्रिया छपी नहीं।"),
    "hook": "दोनों नितम्बों में दस: दश स्फिजोः।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 187, what number is given for the sphij (buttocks)?",
            ("Ten (दश)", "दश स्फिजोः: ten in the two buttocks."),
            [("Two (द्वे)", "The line has दश (ten), not two."),
             ("Five (पञ्च)", "The line has दश (ten), not five."),
             ("Four (चतस्रः)", "The line has दश (ten), not four.")],
            "Ten in the two buttocks.",
            "दश = ten."),
        match(1, "Match each part of unit 187 to its meaning.",
              [["दश", "ten"], ["स्फिज्", "buttock"], ["स्फिजोः", "in the two buttocks"]],
              "दश स्फिजोः = ten in the two buttocks.",
              "दश, स्फिज्, स्फिजोः."),
        fill(2, "In unit 187 the number 'ten' is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("दश", "daśa", "dasha", "dasa"),
             "दश = ten; स्फिजोः = in the two buttocks.",
             "दश = ten.",
             "दश स्फिजोः."),
        mcq("discriminate", 3, "In unit 187, what is the sphij?",
            ("The buttock", "The data: sphij = buttock (standard)."),
            [("The lower leg", "The lower leg is जङ्घा, not sphij."),
             ("The anus", "The anus is गुद, not sphij."),
             ("The knee", "The knee is जानु, not sphij.")],
            "स्फिज् = buttock; स्फिजोः = in the two buttocks.",
            "स्फिज् = buttock (standard)."),
        mcq("apply", 4, "Which form of स्फिज् means 'in the two buttocks'?",
            ("स्फिजोः", "A consonant stem takes -ओः in the locative dual."),
            [("स्फिजौ", "-औ is the nominative/accusative dual, 'two buttocks'."),
             ("स्फिजि", "-इ is the locative singular, 'in the buttock'."),
             ("स्फिजा", "-आ is the instrumental singular, 'by the buttock'.")],
            "स्फिजोः = in the two buttocks (locative dual).",
            "Consonant stem + -ओः = locative dual."),
        mcq("transfer", 5, "By the pattern of स्फिज् → स्फिजोः, how is दिश् (f., direction) put in the locative dual?",
            ("दिशोः", "A consonant stem takes -ओः in the locative dual, as स्फिज् → स्फिजोः."),
            [("दिक्षु", "-सु (here क्षु) is the locative plural, in three or more."),
             ("दिशि", "दिशि is the locative singular, 'in the direction'."),
             ("दिशौ", "दिशौ is the nominative/accusative dual, 'two directions'.")],
            "दिशोः = in the two directions, like स्फिजोः = in the two buttocks.",
            "Consonant stem + -ओः = locative dual.",
            teaches="स्फिजोः is the locative dual of a consonant stem: -ओः means 'in the two'."),
    ],
}

# ---------------------------------------------------------------- unit 188
AUTHORED["188"] = {
    "title": "तिस्रो गुदे तास्तु वलीसंज्ञाः",
    "question": "By unit 188, how many are given in the anus (guda), and what are they called?",
    "rule": ("Three (तिस्रः) in the anus (गुदे); but those (ताः तु) are called valī, folds (वलीसंज्ञाः). Sandhi: तिस्रः + गुदे "
             "→ तिस्रो गुदे (अः before a voiced consonant → ओ); ताः + तु → तास्तु (visarga before त → स्)."),
    "limits": ("Prose; no noun or verb for the count (peśī carried from unit 175). The line names them valī but does not "
               "describe them further. v/b spellings interchange in this print."),
    "explain_hi": ("यह गद्य-पंक्ति कहती है: गुद यानी मलद्वार में तीन पेशियाँ; परन्तु वे ‘वली’ यानी सिलवट नाम वाली हैं। "
                   "‘तु’ (परन्तु) बताता है कि इन तीन का अपना नाम है: वली। "
                   "‘तिस्रो गुदे’ = तिस्रः + गुदे: घोष व्यंजन ग से पहले अः का ओ हुआ। "
                   "‘तास्तु’ = ताः + तु: त से पहले विसर्ग स् बना। "
                   "यह इकाई नए खण्ड ‘पेशियाँ: गुदा से वक्ष तक’ को आरम्भ करती है।"),
    "hook": "गुद में तीन: नाम वली।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 188, how many are given in the guda (anus)?",
            ("Three (तिस्रः)", "तिस्रो गुदे: three in the anus."),
            [("Two (द्वे)", "The line has तिस्रः (three), not two."),
             ("Four (चतस्रः)", "The line has तिस्रः (three), not four."),
             ("Thirty (त्रिंशत्)", "The line has तिस्रः (three), not thirty.")],
            "Three in the anus.",
            "तिस्रः = three (feminine)."),
        order(1, "Put the printed words of unit 188 in the line's order.",
              ["तिस्रो", "गुदे", "तास्तु", "वलीसंज्ञाः"],
              "Three in the anus; but those are called valī.",
              "तिस्रो → गुदे → तास्तु → वलीसंज्ञाः."),
        match(2, "Match each word of unit 188 to its meaning.",
              [["तिस्रः", "three (feminine)"], ["गुद", "anus"], ["तु", "but"], ["वली", "fold"], ["संज्ञा", "name"]],
              "Three in the anus; but those are called valī (folds).",
              "तिस्रः, गुद, तु, वली, संज्ञा.", role="extend",
              teaches="वलीसंज्ञाः = वली (fold) + संज्ञा (name): 'having the name valī', called folds."),
        mcq("discriminate", 3, "Why is तिस्रः printed तिस्रो before गुदे in unit 188?",
            ("अः before a voiced consonant becomes ओ", "ग is a voiced consonant: तिस्रः + गुदे → तिस्रो गुदे."),
            [("अः before any consonant becomes ओ", "Before a voiceless consonant like त, अः becomes अस्, not ओ."),
             ("आः before a voiced consonant becomes ओ", "After आ the visarga drops; and the vowel here is अ."),
             ("तिस्रो is the plain form of 'three'", "The plain feminine form is तिस्रः; ओ is from sandhi.")],
            "तिस्रः (three) + गुदे (in the anus): अः + voiced consonant → ओ.",
            "अः + voiced consonant → ओ."),
        mcq("apply", 4, "Which split of तास्तु in unit 188 is right?",
            ("ताः + तु", "A visarga before त becomes स्: ताः + तु → तास्तु."),
            [("ता + स्तु", "स्तु is not the word here; the words are ताः and तु."),
             ("तासु + तु", "तासु + तु would stay तासु तु; no vowel is lost."),
             ("तत् + स्तु", "तत् and स्तु do not give तास्तु; the word is ताः.")],
            "ताः (those) + तु (but): visarga before त → स्.",
            "Visarga before त → स्."),
        mcq("transfer", 5, "By the rule of तिस्रः + गुदे, how is बालः + गच्छति (the boy goes) joined?",
            ("बालो गच्छति", "अः before a voiced consonant becomes ओ, as तिस्रः + गुदे → तिस्रो गुदे."),
            [("बालर्गच्छति", "र् comes from a visarga after vowels other than अ/आ."),
             ("बाल गच्छति", "अः drops to अ before vowels other than अ, not before ग."),
             ("बालस्गच्छति", "स् comes before त/थ, not before a voiced ग.")],
            "बालः + गच्छति = बालो गच्छति, like तिस्रः + गुदे = तिस्रो गुदे.",
            "अः + voiced consonant → ओ.",
            teaches="अः before a voiced consonant becomes ओ: तिस्रः + गुदे → तिस्रो गुदे."),
    ],
}

# ---------------------------------------------------------------- unit 189
AUTHORED["189"] = {
    "title": "द्वे बस्तिशिरसि",
    "question": "By unit 189, what number is given for the head of the bladder (bastiśiras)?",
    "rule": ("Two (द्वे) in the head of the bladder (बस्तिशिरसि: बस्ति + शिरस्, 'the head of the bladder', locative "
             "singular)."),
    "limits": ("Prose, two words; no noun or verb (peśī carried from unit 175). Bastiśiras is kept literal; which exact "
               "part of the bladder it is, is not stated: questions ask only that this is left open, never which part it is."),
    "explain_hi": ("यह दो शब्दों की गद्य-पंक्ति है: बस्ति के शिर में, यानी मूत्राशय के सिर में, दो। "
                   "‘बस्तिशिरसि’ तत्पुरुष समास है: बस्ति (मूत्राशय) का शिर (सिर); अन्त में शिरस् का सप्तमी एकवचन ‘-शिरसि’। "
                   "‘बस्ति का सिर’ ठीक-ठीक कौन-सा भाग है, यह पंक्ति नहीं बताती; डेटा इसे शब्दशः रखता है। "
                   "गिनी गई वस्तु और क्रिया छपी नहीं।"),
    "hook": "मूत्राशय के सिर में दो।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 189, what number is given for the head of the bladder?",
            ("Two (द्वे)", "द्वे बस्तिशिरसि: two in the head of the bladder."),
            [("Four (चतस्रः)", "The line has द्वे (two), not four."),
             ("Ten (दश)", "The line has द्वे (two), not ten."),
             ("Three (तिस्रः)", "The line has द्वे (two), not three.")],
            "Two in the head of the bladder.",
            "द्वे = two."),
        match(1, "Match each part of unit 189 to its meaning.",
              [["द्वे", "two"], ["बस्ति", "bladder"], ["शिरस्", "head"], ["बस्तिशिरसि", "in the head of the bladder"]],
              "द्वे बस्तिशिरसि = two in the head of the bladder.",
              "द्वे, बस्ति, शिरस्, बस्तिशिरसि."),
        fill(2, "In unit 189 the bladder is called ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("बस्ति", "basti", "वस्ति", "vasti"),
             "बस्ति = bladder; बस्तिशिरसि = in the head of the bladder.",
             "बस्ति = bladder (standard).",
             "द्वे बस्तिशिरसि."),
        mcq("discriminate", 3, "Which of these does unit 189 leave unstated?",
            ("Which exact part the 'head' is", "The note: its exact part is not stated."),
            [("How many are given there", "The number is printed: द्वे, two."),
             ("Which organ the 'head' is of", "The organ is printed: बस्ति, the bladder."),
             ("That the place is a locative", "-शिरसि is printed, a locative 'in'.")],
            "Number, organ and case are printed; the exact part is not.",
            "बस्तिशिरस् kept literal."),
        mcq("apply", 4, "How does the card read the compound बस्तिशिरसि of unit 189?",
            ("In the head of the bladder", "The data: tatpuruṣa, 'the head of the bladder'."),
            [("In the bladder and the head", "The data reads a tatpuruṣa; the line names one place, not two."),
             ("In the bladder of the head", "The head is the last member: the head of the bladder."),
             ("In a bladder-shaped head", "No likeness is meant; it is the head of the bladder.")],
            "बस्ति (of the bladder) + शिरस् (head): the head of the bladder.",
            "Tatpuruṣa: first member qualifies the last."),
        mcq("transfer", 5, "By the pattern of शिरस् → शिरसि (in the head), how is मनस् (mind) put in the locative singular?",
            ("मनसि", "An अस्-stem takes -इ in the locative singular, as शिरस् → शिरसि."),
            [("मनसा", "मनसा is the instrumental, 'by the mind'."),
             ("मनसः", "मनसः is genitive/ablative, 'of/from the mind'."),
             ("मनांसि", "मनांसि is the nominative/accusative plural, 'minds'.")],
            "मनसि = in the mind, like शिरसि = in the head.",
            "अस्-stem + -इ = locative singular.",
            teaches="शिरसि is the locative singular of शिरस्: an अस्-stem + -इ means 'in'."),
    ],
}

# ---------------------------------------------------------------- unit 190
AUTHORED["190"] = {
    "title": "चतस्र उदरे",
    "question": "By unit 190, what number is given for the belly (udara)?",
    "rule": ("Four (चतस्रः, feminine) in the belly (उदरे). चतस्रः + उदरे → चतस्र उदरे: अः before a vowel other than अ "
             "loses its visarga, and the two vowels then stay apart."),
    "limits": ("Prose, two words; no noun or verb (peśī carried from unit 175). The line does not name parts of the "
               "belly."),
    "explain_hi": ("यह दो शब्दों की गद्य-पंक्ति है: उदर यानी पेट में चार। "
                   "‘चतस्रः’ ‘चार’ का स्त्रीलिंग रूप है (पुंलिंग चत्वारः, नपुंसक चत्वारि), क्योंकि गिनी गई पेशी स्त्रीलिंग है। "
                   "‘चतस्र उदरे’ = चतस्रः + उदरे: अ के अतिरिक्त किसी स्वर से पहले अः का विसर्ग लुप्त होता है, और फिर स्वर आपस में नहीं जुड़ते। "
                   "उदर नपुंसकलिंग है; ‘उदरे’ उसका सप्तमी एकवचन। "
                   "गिनी गई वस्तु और क्रिया छपी नहीं।"),
    "hook": "पेट में चार: चतस्र उदरे।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 190, what number is given for the udara (belly)?",
            ("Four (चतस्रः)", "चतस्र उदरे: four in the belly."),
            [("Three (तिस्रः)", "The line has चतस्रः (four), not three."),
             ("Ten (दश)", "The line has चतस्रः (four), not ten."),
             ("Two (द्वे)", "The line has चतस्रः (four), not two.")],
            "Four in the belly.",
            "चतस्रः = four (feminine)."),
        match(1, "Match each part of unit 190 to its meaning.",
              [["चतस्रः", "four (feminine)"], ["उदर", "belly"], ["उदरे", "in the belly"]],
              "चतस्रः उदरे = four in the belly.",
              "चतस्रः, उदर, उदरे."),
        mcq("extend", 2, "Why is the feminine चतस्रः used in unit 190?",
            ("The counted peśī is feminine", "The number agrees with the feminine peśī of unit 175."),
            [("The word उदर is feminine", "उदर is neuter (the data: n. loc. sg.)."),
             ("Four is feminine in all uses", "Four also has चत्वारः (m.) and चत्वारि (n.)."),
             ("The print misspells चत्वारि", "No print error is noted; चतस्रः is regular.")],
            "चतस्रः is feminine because it agrees with the feminine peśī.",
            "Four: चत्वारः (m.), चतस्रः (f.), चत्वारि (n.).",
            teaches="चतस्रः is the feminine of 'four'; the number agrees with the counted noun."),
        mcq("discriminate", 3, "Why does unit 190 print चतस्र उदरे, with no visarga and no vowel join?",
            ("अः drops its visarga before उ; no further join", "Before a vowel other than अ, अः becomes अ, and the vowels stay apart."),
            [("अः before उ becomes ओ, then is dropped", "ओ comes from अः before a voiced consonant, not before उ."),
             ("चतस्र is the full form of the number four", "The full feminine form is चतस्रः; the visarga dropped."),
             ("The print has lost one letter in error", "No print error is noted; this is regular sandhi.")],
            "चतस्रः + उदरे = चतस्र उदरे: the visarga drops, the vowels stay apart.",
            "अः + vowel other than अ → अ (with a gap)."),
        multi("apply", 4, "Which statements fit unit 190?",
              [("चतस्रः is the feminine 'four'", "Right: masc. चत्वारः, neut. चत्वारि."),
               ("उदरे is a locative, 'in the belly'", "Right: the data labels it n. loc. sg."),
               ("उदर is a feminine noun", "उदर is neuter."),
               ("The print joins चतस्र and उदरे as चतस्रोदरे", "The print keeps them apart: चतस्र उदरे.")],
              [0, 1],
              "Feminine four, in the belly; the words stay apart in print.",
              "चतस्र उदरे."),
        mcq("transfer", 5, "By the rule of चतस्रः + उदरे, how is बालः + उवाच (the boy said) joined?",
            ("बाल उवाच", "अः before a vowel other than अ loses its visarga, and the vowels stay apart."),
            [("बालोवाच", "ओ comes from अः before a voiced consonant, not before उ."),
             ("बालरुवाच", "र् comes from a visarga after vowels other than अ/आ."),
             ("बालौवाच", "औ comes from अ + ओ or अ + औ; there is no such join here.")],
            "बालः + उवाच = बाल उवाच, like चतस्रः + उदरे = चतस्र उदरे.",
            "अः + vowel other than अ → अ (with a gap).",
            teaches="अः before a vowel other than अ becomes अ, and no further join follows: चतस्रः + उदरे → चतस्र उदरे."),
    ],
}


# ===================================================================== NOTES_HI
NOTES_HI = {
    "179": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं, कोई अस्पष्ट पंक्ति नहीं। संज्ञा और क्रिया छपी नहीं; गिनी गई वस्तु पेशी (इकाई १७५ से)। "
            "‘तिस्रः’ स्त्रीलिंग, इससे पेशी (स्त्रीलिंग) का संकेत। सक्थि = जाँघ या पूरा निचला अंग; यहाँ निचला अंग चुना गया। "
            "छपा ‘पादांगुल्यां’, ‘प्रत्येकं’ अनुस्वार सहित। सन्धि जाँची: तत्र + एकैकस्मिन् → तत्रैकैकस्मिन् (अ + ए → ऐ); "
            "एक + एक → एकैक (अ + ए → ऐ)।"),
    "180": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। क्रिया समझी जाती है। पन्द्रह का हिसाब संस्कृत में नहीं दिया; संख्या छपे रूप में। "
            "‘ताः’ स्त्रीलिंग बहुवचन (अस्थियों के लिए इकाई १०२ में नपुंसक ‘तानि’)। छपा ‘पंचदश’ = पञ्चदश (पञ्च + दश, कोई ध्वनि-परिवर्तन नहीं)।"),
    "181": ("गद्य; दो छपी पंक्तियाँ जुड़ी हैं; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। [पहली पंक्ति] ‘दश दश’ = दस-दस; हर पैर में या नहीं, अनकहा। "
            "[दूसरी पंक्ति] कोई संख्या छपी नहीं, कोई जोड़ी नहीं गई (पिछली ‘दश दश’ लागू हो सकती है या संख्या छूट गई हो)। "
            "छपा ‘कूर्म्मे’ (म का द्वित्व) = कूर्मे; कूर्म = पैर का कछुए जैसा भाग, सम्भावित। प्रपद, गुल्फ मानक। "
            "सन्धि जाँची: पादस्य + उपरि → पादस्योपरि (अ + उ → ओ)।"),
    "182": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। गिनी गई वस्तु पेशी (इकाई १७५ से), क्रिया समझी जाती है। जङ्घा = घुटने के नीचे की टाँग "
            "(मानक); हिन्दी ‘जंघा/जाँघ’ प्रायः ऊपर की जाँघ, इसलिए सावधानी। छपा ‘जंघायां’ अनुस्वार सहित = जङ्घायाम्। सन्धि जाँची: "
            "विंशतिः + जङ्घायाम् → विंशतिर्जङ्घायाम् (इ के बाद विसर्ग, घोष ध्वनि से पहले → र्)।"),
    "183": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। गिनी गई वस्तु पेशी (इकाई १७५ से), क्रिया समझी जाती है। जानु = घुटना (मानक); ‘जानुनि’ "
            "नपुंसक उकारान्त का सप्तमी एकवचन। छपा ‘पंच’ = पञ्च। दो शब्द अलग, कोई सन्धि नहीं।"),
    "184": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। छपी देवनागरी ‘विंशतिरू्रौ’ बिगड़ी है; लिप्यन्तरण ‘विंशतिरूरौ’ बिना कठिनाई = विंशतिः + ऊरौ। "
            "ऊरु = जाँघ (मानक)। गिनी गई वस्तु पेशी (इकाई १७५ से)। सन्धि जाँची: विंशतिः + ऊरौ → विंशतिरूरौ (इ के बाद विसर्ग, स्वर से पहले → र्)।"),
    "185": ("गद्य; विश्वास मध्यम। पाठ-चिह्न: छपा ‘मेंद्र’ कोई शब्द नहीं; सम्भावित पाठ ‘मेढ्र’ (लिंग), ढ का ‘ंद’ पढ़ा जाना सम्भव, इकाई १५६ जैसा। "
            "सेवनी = सीवन (राफे), सम्भावित। इन पाठों पर कोई प्रश्न नहीं। द्विवचन क्योंकि दो स्थान। सन्धि जाँची: एक + एक → एकैक "
            "(अ + ए → ऐ), स्त्रीलिंग एकैका।"),
    "186": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। गिनी गई वस्तु पेशी (इकाई १७५ से), क्रिया समझी जाती है। वृषण = अण्ड-ग्रन्थि (मानक); "
            "‘वृषणयोः’ सप्तमी द्विवचन। दो पेशियाँ कैसे बँटीं (एक-एक या कुल), अनकहा। दो शब्द अलग, कोई सन्धि नहीं।"),
    "187": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। गिनी गई वस्तु पेशी (इकाई १७५ से), क्रिया समझी जाती है। स्फिज् = नितम्ब (मानक); "
            "‘स्फिजोः’ व्यंजनान्त स्त्रीलिंग का सप्तमी द्विवचन। दस का बँटवारा अनकहा। दो शब्द अलग, कोई सन्धि नहीं।"),
    "188": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। गिनी गई वस्तु पेशी (इकाई १७५ से)। गुद = मलद्वार (मानक); वली = सिलवट (इस छपाई में "
            "व/ब का अदल-बदल)। सन्धि जाँची: तिस्रः + गुदे → तिस्रो गुदे (अः + घोष व्यंजन → ओ); ताः + तु → तास्तु (त से पहले विसर्ग → स्)।"),
    "189": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। गिनी गई वस्तु पेशी (इकाई १७५ से)। बस्ति = मूत्राशय (मानक); ‘बस्तिशिरस्’ शब्दशः "
            "‘मूत्राशय का सिर’ रखा, ठीक भाग अनकहा। समास: बस्ति + शिरस् (कोई ध्वनि-परिवर्तन नहीं), तत्पुरुष।"),
    "190": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। गिनी गई वस्तु पेशी (इकाई १७५ से)। सन्धि जाँची: चतस्रः + उदरे → चतस्र उदरे "
            "(अ के अतिरिक्त स्वर से पहले अः → अ, विसर्ग लुप्त, आगे कोई सन्धि नहीं)। उदर नपुंसक।"),
}


# ===================================================================== AIDS
AIDS = {
    "179": {
        "diagram": {"groups": [
            {"label": "एक सक्थि (निचला अंग) में, क्रम से", "items": ["तत्रैकैकस्मिन् सक्थिनि = हर निचले अंग में",
                                                              "पादांगुल्यां प्रत्येकं = हर पादांगुली में", "तिस्रः = तीन (पेशियाँ)"]}]},
        "chunks": "तत्रैकैकस्मिन् | सक्थिनि | पादांगुल्यां | प्रत्येकं | तिस्रः",
        "sandhi": "अ + ए → ऐ: तत्र + एकैकस्मिन् → तत्रैकैकस्मिन् · एक + एक → एकैक।",
    },
    "180": {
        "chunks": "ताः | पंचदश",
        "letters": "पञ्च-दश: ‘पाँच-दस’ = पन्द्रह; इसी ढंग से सप्त-दश = सत्रह। (मेरी याद-पद्धति)",
        "frame": "वस्तु: ताः (वे, स्त्रीलिंग) → संख्या: पञ्चदश (पन्द्रह) → हिसाब: संस्कृत में नहीं दिया।",
    },
    "181": {
        "diagram": {"groups": [
            {"label": "पहली पंक्ति: दश दश (दस-दस)", "items": ["प्रपद (पैर का अगला भाग)", "पादतल (तलवा)", "गुल्फ (टखना)"]},
            {"label": "दूसरी पंक्ति: तथा, पैर के ऊपर", "items": ["कूर्म (सम्भवतः पैर का ऊपरी भाग): संख्या छपी नहीं"]}]},
        "chunks": "दश दश | प्रपदे | पादतले | गुल्फे च | तथा पादस्योपरि | कूर्म्मे सन्निविष्टाः",
        "sandhi": "अ + उ → ओ: पादस्य + उपरि → पादस्योपरि।",
        "pegs": "आगे से पीछे, नीचे से ऊपर: पंजे का अगला भाग → तलवा → टखना → पैर की पीठ (कूर्म, सम्भवतः कछुए की पीठ जैसा भाग)। (मेरी याद-पद्धति)",
    },
    "182": {
        "chunks": "विंशतिर्जंघायां",
        "sandhi": "इ के बाद विसर्ग, घोष ध्वनि से पहले → र्: विंशतिः + जङ्घायाम् → विंशतिर्जङ्घायाम्।",
        "anchors": "संस्कृत जङ्घा = घुटने के नीचे की टाँग; हिन्दी जाँघ = घुटने के ऊपर (संस्कृत ऊरु)। नाम मिलते-जुलते, भाग अलग।",
    },
    "183": {
        "chunks": "पंच | जानुनि",
        "frame": "संख्या: पञ्च (पाँच) → स्थान: जानुनि (घुटने में) → वस्तु और क्रिया: छपी नहीं (पेशी)।",
        "anchors": "छपे क्रम में नीचे से ऊपर: जङ्घा (घुटने के नीचे, २०) → जानु (घुटना, ५) → ऊरु (जाँघ, २०)।",
    },
    "184": {
        "chain": {"steps": ["इकाई १७९: हर पादांगुली में ३", "इकाई १८१: प्रपद, तल, गुल्फ में १०-१०",
                            "इकाई १८१: कूर्म (संख्या नहीं छपी)", "इकाई १८२: जङ्घा में २०", "इकाई १८३: जानु में ५",
                            "इकाई १८४: ऊरु में २०"]},
        "chunks": "विंशतिरू्रौ (छपी देवनागरी बिगड़ी; पढ़ा: विंशतिरूरौ)",
        "sandhi": "इ के बाद विसर्ग, स्वर से पहले → र्: विंशतिः + ऊरौ → विंशतिरूरौ।",
    },
    "185": {
        "chunks": "एकैका | मेंद्रसेवन्योः (छपा रूप; पढ़ा: मेढ्र, सेवनी)",
        "sandhi": "अ + ए → ऐ: एक + एक → एकैक, स्त्रीलिंग एकैका।",
        "frame": "संख्या: एकैका (एक-एक) → स्थान: दो, एक द्वन्द्व में (मेढ्र; सेवनी, सम्भवतः सीवन) → अन्त: द्विवचन -योः।",
    },
    "186": {
        "chunks": "द्वे | वृषणयोः",
        "frame": "संख्या: द्वे (दो, स्त्री./नपुं.) → स्थान: वृषणयोः (दोनों वृषणों में) → बँटवारा: अनकहा।",
        "letters": "द्वे और द्वि-वचन: दो के लिए दोनों जगह ‘द्व’। (मेरी याद-पद्धति)",
    },
    "187": {
        "chain": {"steps": ["इकाई १८५: मेंद्र (पढ़ा: मेढ्र), सेवनी (सम्भवतः सीवन) में एक-एक",
                            "इकाई १८६: दोनों वृषणों में दो", "इकाई १८७: दोनों स्फिज् (नितम्बों) में दस"]},
        "chunks": "दश | स्फिजोः",
        "frame": "संख्या: दश (दस) → स्थान: स्फिजोः (दोनों नितम्बों में) → बँटवारा: अनकहा।",
    },
    "188": {
        "chain": {"steps": ["तिस्रो गुदे = गुद में तीन", "तास्तु = परन्तु वे", "वलीसंज्ञाः = वली (सिलवट) नाम वाली"]},
        "chunks": "तिस्रो | गुदे | तास्तु | वलीसंज्ञाः",
        "sandhi": "अः + घोष व्यंजन → ओ: तिस्रः + गुदे → तिस्रो गुदे · त से पहले विसर्ग → स्: ताः + तु → तास्तु।",
    },
    "189": {
        "chunks": "द्वे | बस्तिशिरसि",
        "frame": "संख्या: द्वे (दो) → स्थान: बस्ति का शिर (मूत्राशय का सिर; ठीक भाग अनकहा)।",
        "pegs": "बस्ति को एक थैली सोचें जिसका ऊपर का ‘सिर’ है, और उस सिर पर दो पेशियाँ। (मेरा बनाया चित्र, केवल याद की सहायता)",
    },
    "190": {
        "chain": {"steps": ["इकाई १८८: गुद में तीन (वली नाम)", "इकाई १८९: बस्ति के शिर में दो",
                            "इकाई १९०: उदर में चार"]},
        "chunks": "चतस्र | उदरे",
        "sandhi": "अ के अतिरिक्त स्वर से पहले अः → अ (विसर्ग लुप्त, आगे जोड़ नहीं): चतस्रः + उदरे → चतस्र उदरे।",
    },
}


# ===================================================================== IMAGE_SPECS
IMAGE_SPECS = {
    ("179", "diagram"): {
        "file": "sh5-padanguli-179.svg",
        "alt": ("Table of unit 179 in line order: in each single lower limb (sakthi); in each toe; three (feminine, the "
                "peśī counted)."),
        "type": "table",
        "title": "इकाई १७९: हर पादांगुली में",
        "heads": ["छपा अंश", "अर्थ"],
        "rows": [["तत्रैकैकस्मिन् सक्थिनि", "वहाँ, हर एक निचले अंग में"], ["पादांगुल्यां प्रत्येकं", "हर पादांगुली में"],
                 ["तिस्रः", "तीन (स्त्रीलिंग: पेशियाँ)"]],
    },
    ("181", "diagram"): {
        "file": "sh5-prapada-kurma-181.svg",
        "alt": ("Table of unit 181 in line order: forepart of the foot (prapada) ten, sole (pādatala) ten, ankle (gulpha) "
                "ten; kūrma above the foot (probably a tortoise-shaped part of the foot), no numeral printed."),
        "type": "table",
        "title": "इकाई १८१: पैर में दस-दस",
        "heads": ["स्थान (क्रम से)", "संख्या"],
        "rows": [["प्रपद (पैर का अगला भाग)", "दस"], ["पादतल (तलवा)", "दस"], ["गुल्फ (टखना)", "दस"],
                 ["कूर्म, पैर के ऊपर (सम्भावित)", "छपी नहीं"]],
    },
    ("184", "chain"): {
        "file": "sh5-pada-uru-184.svg",
        "alt": ("Chain of the peśī counts of units 179-184 in print order: 3 in each toe; 10 each in forepart, sole and "
                "ankle; kūrma (no numeral printed); 20 in the lower leg (jaṅghā); 5 in the knee (jānu); 20 in the thigh (ūru)."),
        "type": "chain",
        "title": "इकाई १७९-१८४: छपा क्रम",
        "steps": ["१७९: हर पादांगुली में ३", "१८१: प्रपद, तल, गुल्फ में १०-१०", "१८१: कूर्म (संख्या नहीं छपी)",
                  "१८२: जङ्घा में २०", "१८३: जानु में ५", "१८४: ऊरु में २०"],
    },
    ("187", "chain"): {
        "file": "sh5-medhra-sphij-187.svg",
        "alt": ("Table of units 185-187 in print order: meḍhra (printed meṃdra, a possible reading) and sevanī (probably "
                "the raphe) one each; the two testicles two; the two buttocks (sphij) ten."),
        "type": "table",
        "title": "इकाई १८५-१८७: छपा क्रम",
        "heads": ["स्थान", "संख्या"],
        "rows": [["मेंद्र (पढ़ा: मेढ्र), सेवनी (सम्भावित)", "एक-एक"], ["दोनों वृषण", "दो"], ["दोनों स्फिज् (नितम्ब)", "दस"]],
    },
    ("188", "chain"): {
        "file": "sh5-guda-vali-188.svg",
        "alt": ("Chain of unit 188: three in the anus (guda); but those; are called valī (folds)."),
        "type": "chain",
        "title": "इकाई १८८: गुद की वली",
        "steps": ["तिस्रो गुदे = गुद में तीन", "तास्तु = परन्तु वे", "वलीसंज्ञाः = वली नाम वाली"],
    },
    ("190", "chain"): {
        "file": "sh5-guda-udara-190.svg",
        "alt": ("Table of units 188-190 in print order: anus (guda) three, called valī; head of the bladder two; "
                "belly (udara) four."),
        "type": "table",
        "title": "इकाई १८८-१९०: छपा क्रम",
        "heads": ["स्थान", "संख्या"],
        "rows": [["गुद (वली नाम)", "तीन"], ["बस्ति का शिर", "दो"], ["उदर", "चार"]],
    },
}
