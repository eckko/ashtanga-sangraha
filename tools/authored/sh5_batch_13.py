from helpers import mcq, match, order, fill, multi, accepts


AUTHORED = {}

# ---------------------------------------------------------------- unit 153
AUTHORED["153"] = {
    "title": "चत्वारिंशदूरौ",
    "question": "By unit 153, what count is given for the thigh (ūru)?",
    "rule": ("Forty (चत्वारिंशत्) in the thigh (ऊरौ, locative singular of ऊरु). Printed as one word: final त् before "
             "a vowel becomes द्."),
    "limits": ("Prose, one printed word; no verb and no counted noun are printed. The line stands in the snāyu "
               "(ligament) counts begun at card 144 (nine hundred), and the data's per-limb check at card 145 counts this "
               "forty in one limb's 150; the line itself names nothing it counts."),
    "explain_hi": ("यह एक छपे शब्द की गद्य-पंक्ति है: चालीस, ऊरु यानी जाँघ में। "
                   "‘चत्वारिंशदूरौ’ = चत्वारिंशत् (चालीस) + ऊरौ (जाँघ में); स्वर से पहले त् का द् हुआ है। "
                   "‘ऊरौ’ उकारान्त ऊरु का सप्तमी एकवचन है, द्विवचन नहीं। "
                   "पंक्ति इकाई १४४ से चली स्नायु-गिनती (नौ सौ) के बीच है; डेटा की इकाई १४५ वाली जाँच इस चालीस को एक शाखा के १५० में गिनती है। "
                   "गिनी गई वस्तु और क्रिया इस पंक्ति में छपी नहीं।"),
    "hook": "जाँघ में चालीस: चत्वारिंशत् + ऊरौ।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 153, what count is given for the thigh (ūru)?",
            ("Forty", "चत्वारिंशदूरौ: forty in the thigh."),
            [("Thirty", "चत्वारिंशत् is forty, not thirty."),
             ("Fifty", "चत्वारिंशत् is forty, not fifty."),
             ("Sixty", "चत्वारिंशत् is forty, not sixty.")],
            "Forty in the thigh.",
            "चत्वारिंशत् = forty; ऊरौ = in the thigh."),
        match(1, "Match each part of unit 153 to its meaning.",
              [["चत्वारिंशत्", "forty"], ["ऊरु", "thigh"], ["ऊरौ", "in the thigh"]],
              "चत्वारिंशत् + ऊरौ = चत्वारिंशदूरौ: forty in the thigh.",
              "चत्वारिंशत्, ऊरु, ऊरौ."),
        fill(2, "In unit 153 'in the thigh' is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("ऊरौ", "ūrau", "urau"),
             "ऊरौ = in the thigh, the locative singular of ऊरु.",
             "ऊरौ is the locative singular of ऊरु (thigh): -उ stem + -औ = 'in'.",
             "चत्वारिंशत् + ऊरौ → चत्वारिंशदूरौ."),
        mcq("discriminate", 3, "Which split of चत्वारिंशदूरौ in unit 153 is right?",
            ("चत्वारिंशत् + ऊरौ", "त् before a vowel becomes द्: चत्वारिंशत् + ऊरौ → चत्वारिंशदूरौ."),
            [("चत्वारिंश + दूरौ", "चत्वारिंश is not the number; the number is चत्वारिंशत्."),
             ("चत्वारिंशत् + दूरौ", "That would give two द: चत्वारिंशद्दूरौ."),
             ("चत्वारिंशदू + रौ", "चत्वारिंशदू and रौ are not words of the line.")],
            "चत्वारिंशत् (forty) + ऊरौ (in the thigh): त् + ऊ → दू.",
            "Final त् + vowel → द् + vowel."),
        mcq("apply", 4, "ऊरौ comes from ऊरु (thigh). What does the form mean in unit 153?",
            ("In the thigh", "The data: ऊरौ is the locative singular, 'in the thigh'."),
            [("The two thighs", "The dual of ऊरु is ऊरू; ऊरौ is the locative singular."),
             ("From the thigh", "'From the thigh' would be ऊरोः, not ऊरौ."),
             ("By the thigh", "'By the thigh' would be ऊरुणा, not ऊरौ.")],
            "ऊरौ = in the thigh: -औ here is not a dual.",
            "उ-stem (masc.) + -औ = locative singular."),
        mcq("transfer", 5, "By the rule of चत्वारिंशत् + ऊरौ, how are सत् + आचारः (good conduct) joined?",
            ("सदाचारः", "Final त् before a vowel becomes द्, as चत्वारिंशत् + ऊरौ → चत्वारिंशदूरौ."),
            [("सताचारः", "Before a vowel the final त् becomes द्; it does not stay त्."),
             ("सन्नाचारः", "न् would come before a nasal, not before a vowel."),
             ("सच्चाचारः", "च्च comes from त् before च, not before a vowel.")],
            "सत् + आचारः = सदाचारः, like चत्वारिंशत् + ऊरौ = चत्वारिंशदूरौ.",
            "Final त् + vowel → द्.",
            teaches="Final त् before a vowel becomes द्: चत्वारिंशत् + ऊरौ → चत्वारिंशदूरौ."),
    ],
}

# ---------------------------------------------------------------- unit 154
AUTHORED["154"] = {
    "title": "दश वंक्षणे",
    "question": "By unit 154, what count is given for the groin (vaṅkṣaṇa)?",
    "rule": ("Ten (दश) in the groin (वङ्क्षणे, printed वंक्षणे). In the data's per-limb check at card 145 (30 + 30 + 30 + "
             "10 + 40 + 10 = 150) this ten is the last item."),
    "limits": ("Prose, two words; no verb and no counted noun are printed (the snāyu run of card 144). 'Per limb' comes from "
               "card 148 ('in each single sakthi'), not from this line. The ं of वंक्षणे stands for ङ्."),
    "explain_hi": ("यह दो शब्दों की गद्य-पंक्ति है: दस, वंक्षण यानी जाँघ के मूल (ऊरुसन्धि) में। "
                   "‘वंक्षणे’ में अनुस्वार क से पहले ङ् का स्थान लेता है: वङ्क्षणे। "
                   "डेटा की इकाई १४५ वाली जाँच एक शाखा की स्नायु इस क्रम से जोड़ती है: अंगुलियाँ ३०, पादतल-कूर्च-गुल्फ ३०, जंघा ३०, जानु १०, ऊरु ४०, वंक्षण १०; योग १५०, और चार शाखाओं में ६००। "
                   "यह दस उस सूची की अन्तिम संख्या है। "
                   "गिनी गई वस्तु और क्रिया इस पंक्ति में छपी नहीं।"),
    "hook": "शाखा की सूची का अन्त: वंक्षण में दस।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 154, what count is given for the groin (vaṅkṣaṇa)?",
            ("Ten", "दश वंक्षणे: ten in the groin."),
            [("Twenty", "दश is ten, not twenty."),
             ("Forty", "दश is ten, not forty."),
             ("Eight", "दश is ten, not eight.")],
            "Ten in the groin.",
            "दश = ten; वंक्षणे = in the groin."),
        order(1, "Put the sites of one limb (cards 150-154) in the text's order.",
              ["पादतल, कूर्च, गुल्फ", "जङ्घा", "जानु", "ऊरु", "वङ्क्षण"],
              "Sole, kūrca and ankle (ten each); shank 30; knee 10; thigh 40; groin 10.",
              "पादतल-कूर्च-गुल्फ → जङ्घा → जानु → ऊरु → वङ्क्षण."),
        match(2, "Match each site of the limb run to its printed count.",
              [["वङ्क्षण (groin)", "ten"], ["ऊरु (thigh)", "forty"], ["जङ्घा (shank)", "thirty"],
               ["पादाङ्गुली (each toe)", "six each"]],
              "Groin 10 (card 154), thigh 40 (153), shank 30 (151), six in each toe (148).",
              "वङ्क्षण 10, ऊरु 40, जङ्घा 30, पादाङ्गुली six each.", role="extend",
              teaches="One limb, by the data's check at card 145: 30 + 30 + 30 + 10 + 40 + 10 = 150; four limbs = 600."),
        mcq("discriminate", 3, "Inside the word वंक्षणे (unit 154), what does the ं before क stand for?",
            ("ङ्", "Inside a word ं before a क-row consonant stands for ङ्: वंक्षणे = वङ्क्षणे."),
            [("न्", "Inside a word the nasal before क is that of its row, ङ्, not न्."),
             ("म्", "ं stands for म् at a word end; inside this word it is ङ्."),
             ("ण्", "ण् is the nasal of the ट-row, not of the क-row.")],
            "वंक्षणे = वङ्क्षणे: क्ष begins with क, so the anusvāra stands for ङ्.",
            "Inside a word: ं before क, ख, ग, घ = ङ्."),
        multi("apply", 4, "Which statements fit unit 154?",
              [("It gives ten for the groin", "Right: दश वंक्षणे."),
               ("It prints the word for what it counts", "No counted noun is printed in the line."),
               ("Its वंक्षणे means 'in the groin'", "Right: the data reads a locative singular."),
               ("It gives forty for the groin", "दश is ten; forty is the thigh's count (unit 153).")],
              [0, 2],
              "Ten in the groin; the counted noun is not printed.",
              "दश वंक्षणे = ten in the groin."),
        mcq("transfer", 5, "By the rule of वंक्षणे = वङ्क्षणे, how may अंकः (a mark) also be written?",
            ("अङ्कः", "ं before क stands for ङ्, as वंक्षणे = वङ्क्षणे."),
            [("अन्कः", "Before क the nasal is ङ्, not न्."),
             ("अम्कः", "Before क the nasal is ङ्, not म्."),
             ("अण्कः", "ण् belongs before ट, ठ, ड, ढ, not before क.")],
            "अंकः = अङ्कः, like वंक्षणे = वङ्क्षणे.",
            "ं before a क-row consonant = ङ्.",
            teaches="Inside a word the anusvāra before क may be written ङ्: वंक्षणे = वङ्क्षणे."),
    ],
}

# ---------------------------------------------------------------- unit 155
AUTHORED["155"] = {
    "title": "चत्वारिंशत्कट्यां",
    "question": "By unit 155, what count is given for the hip (kaṭi)?",
    "rule": ("Forty (चत्वारिंशत्) in the hip or waist (कट्याम्, locative of कटि). Final त् stays before the unvoiced क. "
             "The data's trunk check at card 160 starts with this forty."),
    "limits": ("Prose, one printed word; no verb and no counted noun are printed (the snāyu run of card 144). कटि = hip or "
               "waist (data). That the hip opens the trunk comes from the data's check at card 160, not from this line."),
    "explain_hi": ("यह एक छपे शब्द की गद्य-पंक्ति है: चालीस, कटि यानी कमर में। "
                   "‘चत्वारिंशत्कट्यां’ = चत्वारिंशत् + कट्याम्; अघोष क से पहले त् जैसा का तैसा रहता है (इकाई १५३ में स्वर से पहले द् हुआ था)। "
                   "‘कट्याम्’ स्त्रीलिंग इकारान्त कटि का सप्तमी एकवचन है; पंक्ति के अन्त में म् छपाई में ं लिखा है। "
                   "डेटा की इकाई १६० वाली धड़ की जाँच इसी चालीस से आरम्भ होती है। "
                   "गिनी गई वस्तु और क्रिया छपी नहीं।"),
    "hook": "कमर में चालीस: त् क से पहले नहीं बदलता।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 155, which place gets forty?",
            ("The hip (kaṭi)", "चत्वारिंशत्कट्यां: forty in the hip."),
            [("The back (pṛṣṭha)", "The back gets eighty (unit 157), not forty."),
             ("The neck (grīvā)", "The neck gets thirty (unit 163), not forty."),
             ("The groin (vaṅkṣaṇa)", "The groin gets ten (unit 154), not forty.")],
            "Forty in the hip.",
            "चत्वारिंशत् = forty; कट्याम् = in the hip."),
        match(1, "Match each part of unit 155 to its meaning.",
              [["चत्वारिंशत्", "forty"], ["कटि", "hip or waist"], ["कट्याम्", "in the hip"]],
              "चत्वारिंशत् + कट्याम् = forty in the hip.",
              "चत्वारिंशत्, कटि, कट्याम्."),
        mcq("extend", 2, "Where does the data's trunk check (card 160) put the forty of unit 155?",
            ("First in the trunk sum", "Card 160: 40 + 20 + 80 + 60 + 18 + 4; the hip's forty comes first."),
            [("Last in the limb sum", "The limb sum (card 145) ends with the groin's ten, not the hip."),
             ("Under the head and neck", "The head and neck are 'above' (card 147), not the hip."),
             ("Outside every data sum", "The trunk check at card 160 includes it.")],
            "The hip's forty opens the trunk sum of the data.",
            "Trunk check: कटि 40 + 20 + 80 + 60 + 18 + 4.",
            teaches="After the limb (cards 148-154) the data's check counts the trunk from the hip (card 155)."),
        mcq("discriminate", 3, "Why does त् stay त् in चत्वारिंशत्कट्यां (unit 155)?",
            ("क is unvoiced", "त् changes before a vowel or a voiced sound (द् before ग, द, ब; also ल्, ज् before ल, ज, and optionally न् before a nasal); क is unvoiced, so त् stays."),
            [("क is a nasal", "क is not a nasal; the nasal of its row is ङ."),
             ("त् never changes", "It does change: before a vowel it becomes द् (unit 153)."),
             ("क is a vowel", "क is a consonant; before a vowel त् would become द्.")],
            "चत्वारिंशत् + कट्याम्: before unvoiced क the त् stays.",
            "त् + unvoiced consonant → त् stays."),
        multi("apply", 4, "Which statements fit unit 155?",
              [("It gives forty for the back", "The back gets eighty (unit 157); unit 155 names the hip."),
               ("Its कट्याम् means 'from the hip'", "कट्याम् is the locative singular, 'in the hip'."),
               ("It gives forty for the hip", "Right: चत्वारिंशत्कट्यां."),
               ("Its त् stays before क", "Right: क is unvoiced, so चत्वारिंशत् keeps its त्.")],
              [2, 3],
              "Forty in the hip; त् stays before the unvoiced क.",
              "चत्वारिंशत्कट्यां = चत्वारिंशत् कट्याम्."),
        mcq("transfer", 5, "By the rule of चत्वारिंशत् + कट्याम्, how are तत् + कालम् (that time) joined?",
            ("तत्कालम्", "त् stays before the unvoiced क, as in चत्वारिंशत्कट्यां."),
            [("तद्कालम्", "द् comes before a vowel or a voiced consonant such as ग; क is unvoiced."),
             ("तन्कालम्", "न् may come (optionally) only before a nasal; क is not a nasal."),
             ("तच्कालम्", "च् comes from त् before च, छ or श, not before क.")],
            "तत् + कालम् = तत्कालम्, like चत्वारिंशत् + कट्याम् = चत्वारिंशत्कट्याम्.",
            "त् + unvoiced consonant (क) → त् stays.",
            teaches="Final त् before an unvoiced consonant like क stays त्: चत्वारिंशत्कट्यां."),
    ],
}

# ---------------------------------------------------------------- unit 156
AUTHORED["156"] = {
    "title": "विंशतिर्मुष्कमेंद्रबस्त्यंत्रेषु",
    "question": "By unit 156, what count is given for muṣka, basti, antra and the printed मेंद्र?",
    "rule": ("Twenty (विंशतिः) in the muṣka (scrotum or testes), the printed मेंद्र (read meḍhra, penis, as possible), "
             "the basti (bladder) and the antra (intestines): one dvandva in the locative plural. इः before म → इर्."),
    "limits": ("Prose. मेंद्र is not a word; the data's reading meḍhra is only possible: no question rests on that member. "
               "How the twenty are shared among the four is not said. No counted noun is printed (snāyu run)."),
    "explain_hi": ("यह गद्य-पंक्ति कहती है: बीस, मुष्क (अण्डकोष), मेंद्र, बस्ति (मूत्राशय) और अन्त्र (आँतों) में। "
                   "छपा ‘मेंद्र’ कोई शब्द नहीं; डेटा इसे सम्भवतः ‘मेढ्र’ (लिंग) पढ़ता है, पर यह केवल सम्भावित पाठ है। "
                   "चारों शब्द एक द्वन्द्व समास हैं; अन्त का ‘-एषु’ (सप्तमी बहुवचन) चारों पर लगता है। "
                   "‘विंशतिर्’ में घोष म से पहले इः का इर् हुआ है; ‘बस्त्यन्त्र’ में इ + अ → य। "
                   "बीस चारों में कैसे बँटे, यह नहीं कहा गया।"),
    "hook": "बीस: अण्डकोष, (मेंद्र), मूत्राशय, आँतें।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 156, what count is given for the muṣka, basti and antra group?",
            ("Twenty", "विंशतिर्मुष्क...: twenty in these places."),
            [("Eighty", "विंशतिः is twenty, not eighty."),
             ("Ten", "विंशतिः is twenty, not ten."),
             ("Forty", "विंशतिः is twenty, not forty.")],
            "Twenty for the group.",
            "विंशतिः = twenty."),
        match(1, "Match each word of unit 156 to its meaning.",
              [["विंशति", "twenty"], ["मुष्क", "scrotum or testes"], ["बस्ति", "bladder"], ["अन्त्र", "intestines"]],
              "Twenty in the muṣka, (the printed मेंद्र), the basti and the antra.",
              "विंशति, मुष्क, बस्ति, अन्त्र."),
        mcq("extend", 2, "The compound of unit 156 ends in -एषु (locative plural). Where does that 'in' reach?",
            ("To all its members", "In a dvandva one ending at the end serves every member: in the muṣka, ..., basti and antra."),
            [("To the antra only", "The ending stands on the last member but serves the whole dvandva."),
             ("To the muṣka only", "The first member has no ending of its own; the final -एषु serves all."),
             ("To none: it means 'of'", "-एषु is the locative plural, 'in', not 'of'.")],
            "One -एषु at the end: 'in' all the members of the compound.",
            "Dvandva + one final ending = that case for every member.",
            teaches="A dvandva takes one case ending at its end, and it serves every member."),
        mcq("discriminate", 3, "Which split of बस्त्यंत्रेषु in unit 156 is right?",
            ("बस्ति + अन्त्रेषु", "इ before a different vowel becomes य्: बस्ति + अन्त्रेषु → बस्त्यन्त्रेषु."),
            [("बस्त्य + अन्त्रेषु", "बस्त्य is not the word; the word is बस्ति, bladder."),
             ("बस्ति + यन्त्रेषु", "That would give बस्तियन्त्रेषु; the य् comes from the इ."),
             ("बस्त + यन्त्रेषु", "बस्त is not the word; the word is बस्ति.")],
            "बस्ति (bladder) + अन्त्रेषु (in the intestines): इ + अ → य.",
            "इ + अ → य."),
        multi("apply", 4, "Which places does unit 156 name?",
              [("The heart (hṛdaya)", "The heart is not named in unit 156."),
               ("The bladder (basti)", "Right: बस्ति."),
               ("The palate (tālu)", "The palate is named in unit 162, not here."),
               ("The intestines (antra)", "Right: अन्त्र.")],
              [1, 3],
              "Bladder and intestines are among its four places.",
              "मुष्क-मेंद्र-बस्ति-अन्त्रेषु."),
        mcq("transfer", 5, "By the rule of विंशतिः + मुष्क..., how are मतिः + मम (my mind) joined?",
            ("मतिर्मम", "इः before a voiced sound (other than र) becomes इर्, as विंशतिः + मुष्क → विंशतिर्मुष्क."),
            [("मतिः मम", "Before the voiced म the visarga after इ does not stay; it becomes र्."),
             ("मतिस्मम", "स् comes before त or थ, not before म."),
             ("मतिम्मम", "A visarga does not become म्.")],
            "मतिः + मम = मतिर्मम, like विंशतिः + मुष्क = विंशतिर्मुष्क.",
            "इः + voiced sound (not र) → इर्.",
            teaches="A visarga after इ before a voiced sound other than र becomes र्: विंशतिः + मुष्क → विंशतिर्मुष्क."),
    ],
}

# ---------------------------------------------------------------- unit 157
AUTHORED["157"] = {
    "title": "अशीतिः पृष्ठे",
    "question": "By unit 157, what count is given for the back (pṛṣṭha)?",
    "rule": ("Eighty (अशीतिः) in the back (पृष्ठे). In the data's trunk check at card 160 (40 + 20 + 80 + 60 + 18 + 4) "
             "it is the largest count. The visarga stays before the unvoiced प."),
    "limits": ("Prose, two words; no verb and no counted noun are printed (the snāyu run of card 144). Card 107 gives thirty "
               "for the back in the bone count: another list, not this one."),
    "explain_hi": ("यह दो शब्दों की गद्य-पंक्ति है: अस्सी, पृष्ठ यानी पीठ में। "
                   "डेटा की इकाई १६० वाली धड़ की जाँच (४० + २० + ८० + ६० + १८ + ४) में यह सबसे बड़ी संख्या है। "
                   "‘अशीतिः’ का विसर्ग अघोष प से पहले विसर्ग ही रहता है; घोष ध्वनि से पहले वह र् बनता (जैसे इकाई १५६ में विंशतिर्)। "
                   "इकाई १०७ में पीठ में तीस अस्थियाँ थीं; वह दूसरी गिनती है। "
                   "गिनी गई वस्तु और क्रिया इस पंक्ति में छपी नहीं।"),
    "hook": "पीठ में अस्सी: धड़ की सबसे बड़ी संख्या।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 157, what count is given for the back?",
            ("Eighty", "अशीतिः पृष्ठे: eighty in the back."),
            [("Thirty", "अशीतिः is eighty, not thirty."),
             ("Sixty", "अशीतिः is eighty, not sixty."),
             ("Eighteen", "अशीतिः is eighty, not eighteen.")],
            "Eighty in the back.",
            "अशीतिः = eighty; पृष्ठे = in the back."),
        match(1, "Match each part of unit 157 to its meaning.",
              [["अशीति", "eighty"], ["पृष्ठ", "back"], ["पृष्ठे", "in the back"]],
              "अशीतिः पृष्ठे = eighty in the back.",
              "अशीति, पृष्ठ, पृष्ठे."),
        fill(2, "In unit 157 the number 'eighty' is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("अशीतिः", "aśītiḥ", "अशीति", "ashiti"),
             "अशीतिः = eighty; पृष्ठे = in the back.",
             "अशीति = eighty (not अष्टौ, eight, nor अष्टादश, eighteen).",
             "अशीतिः पृष्ठे."),
        mcq("discriminate", 3, "Why does अशीतिः keep its visarga before पृष्ठे in unit 157?",
            ("प is an unvoiced consonant", "After इ the visarga becomes र् only before a voiced sound; प is unvoiced."),
            [("पृष्ठे starts with a vowel", "पृष्ठे starts with प, a consonant."),
             ("A visarga after इ never changes", "It does: before a voiced sound it becomes र् (unit 156)."),
             ("प is a voiced consonant", "प is unvoiced; before a voiced sound the visarga would be र्.")],
            "अशीतिः + पृष्ठे: before unvoiced प the visarga stays.",
            "Visarga before क, ख, प, फ stays a visarga."),
        mcq("apply", 4, "In the data's trunk check (card 160), which site has the largest count?",
            ("The back (pṛṣṭha)", "Eighty for the back (unit 157) is the largest of 40, 20, 80, 60, 18, 4."),
            [("The flanks (pārśva)", "The two flanks get sixty (unit 158), less than eighty."),
             ("The hip (kaṭi)", "The hip gets forty (unit 155), less than eighty."),
             ("The chest (uras)", "The chest gets eighteen (unit 159), less than eighty.")],
            "The back's eighty is the largest trunk count.",
            "40 + 20 + 80 + 60 + 18 + 4: the 80 is the back's."),
        mcq("transfer", 5, "By the rule of अशीतिः पृष्ठे, how are हरिः + पठति (Hari reads) written in a sentence?",
            ("हरिः पठति", "Visarga before the unvoiced प stays, as in अशीतिः पृष्ठे."),
            [("हरिर्पठति", "र् comes before a voiced sound; प is unvoiced."),
             ("हरिस्पठति", "स् comes before त or थ, not before प."),
             ("हरी पठति", "Before प the visarga is not dropped and the vowel is not lengthened.")],
            "हरिः पठति, like अशीतिः पृष्ठे.",
            "इः + unvoiced प → visarga stays.",
            teaches="A visarga before an unvoiced प stays a visarga: अशीतिः पृष्ठे."),
    ],
}

# ---------------------------------------------------------------- unit 158
AUTHORED["158"] = {
    "title": "षष्टिः पार्श्वयोः",
    "question": "By unit 158, what count is given for the two flanks (pārśva)?",
    "rule": ("Sixty (षष्टिः) in the two flanks (पार्श्वयोः, locative dual). The line does not say whether it is sixty in "
             "all or for each flank."),
    "limits": ("Prose, two words; no verb and no counted noun are printed (the snāyu run of card 144). Per side or in all is "
               "not said: questions only ask that it is left open. -योः is also a genitive dual; the data reads it as locative."),
    "explain_hi": ("यह दो शब्दों की गद्य-पंक्ति है: साठ, दोनों पार्श्वों (बगलों) में। "
                   "‘पार्श्वयोः’ द्विवचन है: दो पार्श्व; डेटा इसे सप्तमी पढ़ता है, ‘में’। "
                   "साठ दोनों में मिलकर हैं या हर ओर साठ, यह पंक्ति नहीं कहती। "
                   "‘षष्टिः’ का विसर्ग अघोष प से पहले विसर्ग ही रहता है। "
                   "गिनी गई वस्तु और क्रिया छपी नहीं।"),
    "hook": "दोनों बगलों में साठ।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 158, what count is given for the two flanks (pārśva)?",
            ("Sixty", "षष्टिः पार्श्वयोः: sixty in the two flanks."),
            [("Eighty", "षष्टिः is sixty, not eighty."),
             ("Twenty", "षष्टिः is sixty, not twenty."),
             ("Forty", "षष्टिः is sixty, not forty.")],
            "Sixty in the two flanks.",
            "षष्टिः = sixty; पार्श्वयोः = in the two flanks."),
        match(1, "Match each part of unit 158 to its meaning.",
              [["षष्टि", "sixty"], ["पार्श्व", "flank, side"], ["पार्श्वयोः", "in the two flanks"]],
              "षष्टिः पार्श्वयोः = sixty in the two flanks.",
              "षष्टि, पार्श्व, पार्श्वयोः."),
        mcq("extend", 2, "What does the ending -योः of पार्श्वयोः tell in unit 158?",
            ("There are two flanks: dual", "-योः is a dual ending: the two flanks."),
            [("There are many flanks: plural", "The locative plural would be पार्श्वेषु."),
             ("There is one flank: singular", "The locative singular would be पार्श्वे."),
             ("The flanks are the subject", "-योः is never a nominative ending.")],
            "पार्श्वयोः = in the two flanks: a dual.",
            "अ-stem + -योः = dual (here read as locative).",
            teaches="-योः on an अ-stem is a dual ending (genitive or locative); here: in the two flanks."),
        mcq("discriminate", 3, "What does unit 158 say about how the sixty are shared?",
            ("Nothing: only sixty for the pair", "The line gives sixty for the two flanks and no share for each."),
            [("Thirty for each flank, as stated", "No 'thirty each' is printed in the line."),
             ("Sixty for each flank, as stated", "No 'each' (प्रत्येकम्) is printed in the line."),
             ("Sixty for the left flank only", "Neither left nor right is named in the line.")],
            "Sixty in the two flanks; the share of each is left open.",
            "षष्टिः पार्श्वयोः: number + dual place, no 'each'."),
        multi("apply", 4, "Which statements fit unit 158?",
              [("It gives sixty", "Right: षष्टिः."),
               ("It prints the counted noun", "No counted noun is printed in the line."),
               ("Its place word is singular", "पार्श्वयोः is a dual, not a singular."),
               ("It names the flanks (pārśva)", "Right: पार्श्वयोः.")],
              [0, 3],
              "Sixty in the two flanks; no counted noun.",
              "षष्टिः पार्श्वयोः."),
        mcq("transfer", 5, "By the pattern of पार्श्वयोः (in the two flanks), how is in the two ponds said from तडाग?",
            ("तडागयोः", "अ-stem + -योः = dual, as पार्श्व → पार्श्वयोः."),
            [("तडागेषु", "तडागेषु is the locative plural, 'in the ponds' (many)."),
             ("तडागे", "तडागे is the locative singular, 'in the pond'."),
             ("तडागौ", "तडागौ is the nominative or accusative dual, not 'in'.")],
            "तडागयोः = in the two ponds, like पार्श्वयोः = in the two flanks.",
            "अ-stem + -योः = genitive/locative dual.",
            teaches="पार्श्वयोः is a dual of an अ-stem: -योः marks two (genitive or locative)."),
    ],
}

# ---------------------------------------------------------------- unit 159
AUTHORED["159"] = {
    "title": "अष्टादशोरसि",
    "question": "By unit 159, what count is given for the chest (uras)?",
    "rule": ("Eighteen (अष्टादश) in the chest (उरसि, locative of उरस्). Printed as one word: अ + उ → ओ."),
    "limits": ("Prose, one printed word; no verb and no counted noun are printed (the snāyu run of card 144). Eight in the "
               "chest at cards 108 and 128 belongs to other lists (bones, joints)."),
    "explain_hi": ("यह एक छपे शब्द की गद्य-पंक्ति है: अठारह, उरस् यानी छाती में। "
                   "‘अष्टादशोरसि’ = अष्टादश + उरसि; अ + उ → ओ। "
                   "‘उरसि’ सकारान्त उरस् का सप्तमी एकवचन है। "
                   "ध्यान दें: अष्टादश अठारह है; अष्टौ आठ और अशीति अस्सी। "
                   "इकाई १०८ और १२८ में छाती के आठ दूसरी सूचियों (अस्थि, सन्धि) के हैं।"),
    "hook": "छाती में अठारह: अष्टादश + उरसि।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 159, what count is given for the chest?",
            ("Eighteen", "अष्टादशोरसि: eighteen in the chest."),
            [("Eight", "अष्टादश is eighteen; eight is अष्टौ."),
             ("Eighty", "अष्टादश is eighteen; eighty is अशीति."),
             ("Thirteen", "अष्टादश is eighteen; thirteen is त्रयोदश.")],
            "Eighteen in the chest.",
            "अष्टादश = eighteen; उरसि = in the chest."),
        match(1, "Match each number word to its value.",
              [["अष्टौ", "eight"], ["अष्टादश", "eighteen"], ["अशीति", "eighty"], ["दश", "ten"]],
              "अष्टौ 8, अष्टादश 18 (unit 159), अशीति 80 (unit 157), दश 10 (unit 154).",
              "अष्टौ, अष्टादश, अशीति, दश."),
        fill(2, "In unit 159 'in the chest' is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("उरसि", "urasi"),
             "उरसि = in the chest, the locative singular of उरस्.",
             "उरसि is the locative singular of उरस् (chest).",
             "अष्टादश + उरसि → अष्टादशोरसि."),
        mcq("discriminate", 3, "Which split of अष्टादशोरसि in unit 159 is right?",
            ("अष्टादश + उरसि", "अ + उ → ओ: अष्टादश + उरसि → अष्टादशोरसि."),
            [("अष्टादश + ओरसि", "ओरसि is not a word, and अ + ओ would give औ."),
             ("अष्टादशो + रसि", "अष्टादशो and रसि are not the words of the line."),
             ("अष्टादशः + उरसि", "अष्टादश has no visarga; अः + उ would drop it and leave the two apart.")],
            "अष्टादश (eighteen) + उरसि (in the chest): अ + उ → ओ.",
            "अ + उ → ओ."),
        mcq("apply", 4, "A learner reads अष्टादशोरसि as 'eight in the chest'. What is the slip?",
            ("अष्टादश is eighteen", "अष्टादश = eighteen; eight would be अष्टौ (printed अष्टाव् before a vowel)."),
            [("उरसि means the back", "उरसि is 'in the chest'; 'in the back' is पृष्ठे."),
             ("अष्टादश is eighty", "Eighty is अशीति (unit 157), not अष्टादश."),
             ("There is no slip", "अष्टादश is eighteen, so 'eight' is wrong.")],
            "Eighteen, not eight, in the chest.",
            "अष्टादश = 18; अष्टौ = 8; अशीति = 80."),
        mcq("transfer", 5, "By the rule of अष्टादश + उरसि, how are वीर + उचितम् (befitting a hero) joined?",
            ("वीरोचितम्", "अ + उ → ओ, as अष्टादश + उरसि → अष्टादशोरसि."),
            [("वीरौचितम्", "औ comes from अ + ओ or औ, not from अ + उ."),
             ("वीराचितम्", "आ comes from अ + अ, not from अ + उ."),
             ("वीरुचितम्", "अ before उ is not dropped; the two join as ओ.")],
            "वीर + उचितम् = वीरोचितम्, like अष्टादश + उरसि = अष्टादशोरसि.",
            "अ + उ → ओ.",
            teaches="Short अ followed by उ joins as ओ: अष्टादश + उरसि → अष्टादशोरसि."),
    ],
}

# ---------------------------------------------------------------- unit 160
AUTHORED["160"] = {
    "title": "चत्वार्यक्षकयोः",
    "question": "By unit 160, what count is given for the two collarbones (akṣaka), and where does the trunk sum stand?",
    "rule": ("Four (चत्वारि) in the two collarbones (अक्षकयोः): इ + अ → य. The data adds the trunk lines 155-160: "
             "40 + 20 + 80 + 60 + 18 + 4 = 222, short of the 230 of card 146."),
    "limits": ("Prose; no verb or counted noun printed. The data says only that more trunk sites may follow; which line "
               "makes up 230 is not asked. Unit 164's jatru is also glossed collar-bone; the text does not explain the two."),
    "explain_hi": ("यह एक छपे शब्द की गद्य-पंक्ति है: चार, दोनों अक्षकों यानी हँसली की हड्डियों में। "
                   "‘चत्वार्यक्षकयोः’ = चत्वारि + अक्षकयोः; इ + अ → य। "
                   "डेटा धड़ की छपी संख्याएँ जोड़ता है: ४० + २० + ८० + ६० + १८ + ४ = २२२, जबकि इकाई १४६ में धड़ के लिए २३० कहा गया है। "
                   "डेटा के अनुसार आगे और स्थान आ सकते हैं; कौन-सी पंक्ति कमी पूरी करती है, यह पाठ नहीं कहता। "
                   "इकाई १६४ में जत्रु (वह भी हँसली) के तीन हैं; दोनों शब्दों का भेद पाठ नहीं बताता।"),
    "hook": "हँसली में चार; धड़ का छपा जोड़ २२२।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 160, what count is given for the two collarbones (akṣaka)?",
            ("Four", "चत्वार्यक्षकयोः: four in the two collarbones."),
            [("Eight", "चत्वारि is four, not eight."),
             ("Two", "चत्वारि is four, not two."),
             ("Three", "चत्वारि is four, not three.")],
            "Four in the two collarbones.",
            "चत्वारि = four; अक्षकयोः = in the two collarbones."),
        order(1, "Put the trunk sites of units 155-160 in the text's order.",
              ["कटि (40)", "मुष्क, बस्ति, अन्त्र आदि (20)", "पृष्ठ (80)", "पार्श्व (60)", "उरस् (18)", "अक्षक (4)"],
              "Hip 40, the muṣka group 20, back 80, flanks 60, chest 18, collarbones 4.",
              "कटि → मुष्क... → पृष्ठ → पार्श्व → उरस् → अक्षक."),
        match(2, "Match each number word of units 155-160 to its value.",
              [["चत्वारिंशत्", "40"], ["विंशति", "20"], ["अशीति", "80"], ["षष्टि", "60"], ["अष्टादश", "18"],
               ["चत्वारि", "4"]],
              "The trunk numbers in order: 40, 20, 80, 60, 18, 4.",
              "चत्वारिंशत्, विंशति, अशीति, षष्टि, अष्टादश, चत्वारि.", role="extend",
              teaches="चत्वारि = 4 but चत्वारिंशत् = 40; अष्टादश = 18 but अशीति = 80."),
        mcq("discriminate", 3, "Which split of चत्वार्यक्षकयोः in unit 160 is right?",
            ("चत्वारि + अक्षकयोः", "इ before a different vowel becomes य्: चत्वारि + अक्षकयोः → चत्वार्यक्षकयोः."),
            [("चत्वार्य + अक्षकयोः", "चत्वार्य is not the number; the number is चत्वारि."),
             ("चत्वारि + यक्षकयोः", "That would give चत्वारियक्षकयोः; the य् comes from the इ."),
             ("चत्वारः + अक्षकयोः", "अः + अ would give चत्वारोऽक्षकयोः, not चत्वार्य....")],
            "चत्वारि (four) + अक्षकयोः (in the two collarbones): इ + अ → य.",
            "इ + अ → य."),
        mcq("apply", 4, "The data adds the trunk counts of units 155-160. What does it get, against card 146's 230?",
            ("222, eight short of 230", "40 + 20 + 80 + 60 + 18 + 4 = 222."),
            [("230, the stated sum", "The six counts add to 222, not 230."),
             ("240, ten more than 230", "The six counts add to 222, not 240."),
             ("200, thirty short of 230", "The six counts add to 222, not 200.")],
            "222: the printed trunk lines so far fall eight short of 230.",
            "40 + 20 + 80 + 60 + 18 + 4 = 222."),
        mcq("transfer", 5, "By the rule of चत्वारि + अक्षकयोः, how are प्रति + अहम् (every day) joined?",
            ("प्रत्यहम्", "इ before a different vowel becomes य्, as चत्वारि + अक्षकयोः → चत्वार्यक्षकयोः."),
            [("प्रतेहम्", "ए comes from अ + इ, not from इ + अ."),
             ("प्रतीहम्", "ई comes from इ + इ, not from इ + अ."),
             ("प्रतिहम्", "The अ is not lost; इ + अ joins as य.")],
            "प्रति + अहम् = प्रत्यहम्, like चत्वारि + अक्षकयोः = चत्वार्यक्षकयोः.",
            "इ + अ → य.",
            teaches="इ before a different vowel becomes य्: चत्वारि + अक्षकयोः → चत्वार्यक्षकयोः."),
    ],
}

# ---------------------------------------------------------------- unit 161
AUTHORED["161"] = {
    "title": "अष्टावंसयोः",
    "question": "By unit 161, what count is given for the two shoulders (aṃsa)?",
    "rule": ("Eight (अष्टौ) in the two shoulders (अंसयोः, locative dual). Printed as one word: औ before a vowel becomes आव्."),
    "limits": ("Prose, one printed word; no noun or verb is printed: the data carries the counted item, snāyu, from the run "
               "begun at card 144. Whether the shoulders belong to the trunk sum of card 146 is not said: no question on it. "
               "Per side or in all is not said."),
    "explain_hi": ("यह एक छपे शब्द की गद्य-पंक्ति है: आठ, दोनों अंसों यानी कन्धों में। "
                   "‘अष्टावंसयोः’ = अष्टौ + अंसयोः; स्वर से पहले औ का आव् हुआ है। "
                   "डेटा के अनुसार गिनी गई वस्तु, स्नायु, इकाई १४४ से चली आ रही है; यहाँ छपी नहीं। "
                   "इकाई १६० तक धड़ का छपा जोड़ २२२ था; २२२ + ८ = २३० होता है, पर पाठ स्वयं नहीं कहता कि कन्धे धड़ में गिने गए। "
                   "आठ दोनों में मिलकर हैं या हर ओर, यह भी नहीं कहा।"),
    "hook": "दोनों कन्धों में आठ: अष्टौ + अंसयोः।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 161, what count is given for the two shoulders?",
            ("Eight", "अष्टावंसयोः: eight in the two shoulders."),
            [("Four", "अष्टौ is eight, not four."),
             ("Eighteen", "अष्टौ is eight, not eighteen."),
             ("Six", "अष्टौ is eight, not six.")],
            "Eight in the two shoulders.",
            "अष्टौ = eight; अंसयोः = in the two shoulders."),
        match(1, "Match each part of unit 161 to its meaning.",
              [["अष्टौ", "eight"], ["अंस", "shoulder"], ["अंसयोः", "in the two shoulders"]],
              "अष्टौ + अंसयोः = अष्टावंसयोः: eight in the two shoulders.",
              "अष्टौ, अंस, अंसयोः."),
        mcq("extend", 2, "By the data, what does unit 161 carry over from the lines before it?",
            ("The counted item, snāyu", "The data: no noun is printed; snāyu is carried from the run begun at card 144."),
            [("The number, eight", "The number is printed: अष्टौ."),
             ("The place, the shoulders", "The place is printed: अंसयोः."),
             ("The word 'each' (प्रत्येकम्)", "No 'each' is printed here; the data carries over only the counted item, snāyu.")],
            "Number and place are printed; the counted item, snāyu, is understood.",
            "ELLIPSIS: snāyu, carried from card 144.",
            teaches="These short lines print only number + place; the counted item (snāyu) is carried over."),
        mcq("discriminate", 3, "Why is अष्टौ printed अष्टाव् before अंसयोः in unit 161?",
            ("औ before a vowel becomes आव्", "अष्टौ + अंसयोः → अष्टावंसयोः."),
            [("ओ before a vowel becomes अव्", "अष्टौ ends in औ, not ओ; औ gives आव्."),
             ("A visarga of अष्टः becomes व्", "अष्टौ has no visarga; the व् comes from its औ."),
             ("अष्टाव is the plain word", "The word is अष्टौ; अष्टाव् is its form before a vowel.")],
            "अष्टौ (eight) + अंसयोः: औ + अ → आव.",
            "औ + vowel → आव् + that vowel."),
        multi("apply", 4, "Which statements fit unit 161?",
              [("It says four in each shoulder", "No 'each' is printed; the line gives eight."),
               ("Its अंसयोः is a dual", "Right: the two shoulders."),
               ("It gives eight", "Right: अष्टौ."),
               ("It prints the word स्नायु", "No noun is printed; snāyu is carried over.")],
              [1, 2],
              "Eight in the two shoulders; the counted noun is understood.",
              "अष्टावंसयोः = अष्टौ अंसयोः."),
        mcq("transfer", 5, "By the rule of अष्टौ + अंसयोः, how are गजौ + अपि (the two elephants too) joined?",
            ("गजावपि", "औ before a vowel becomes आव्, as अष्टौ + अंसयोः → अष्टावंसयोः."),
            [("गजवपि", "अव् comes from ओ before a vowel, not from औ."),
             ("गजायपि", "आय् comes from ऐ before a vowel, not from औ."),
             ("गजोपि", "औ before a vowel does not become ओ; it becomes आव्.")],
            "गजौ + अपि = गजावपि, like अष्टौ + अंसयोः = अष्टावंसयोः.",
            "औ + vowel → आव्.",
            teaches="औ before a vowel becomes आव्: अष्टौ + अंसयोः → अष्टावंसयोः."),
    ],
}

# ---------------------------------------------------------------- unit 162
AUTHORED["162"] = {
    "title": "द्वे द्वे मन्याऽवटुनेत्रौष्ठतालुषु",
    "question": "By unit 162, which five places get 'two each'?",
    "rule": ("Two each (द्वे द्वे) in the manyā (probably the side of the neck), the avaṭu (probably the hollow at the "
             "nape), the eyes (नेत्र), the lips (ओष्ठ) and the palate (तालु): one dvandva, locative plural."),
    "limits": ("Prose; snāyu is carried, not printed. Manyā and avaṭu are probable only: not asked. The ऽ after मन्या "
               "is a print habit (data). Two per side is not said. Before ओष्ठ in a compound अ + ओ may also give ओ "
               "(नेत्रोष्ठ is also valid); the print has औ."),
    "explain_hi": ("यह गद्य-पंक्ति कहती है: दो-दो, पाँच स्थानों में: मन्या (सम्भवतः गर्दन का पार्श्व), अवटु (सम्भवतः गर्दन के पीछे का गड्ढा), नेत्र, ओष्ठ और तालु। "
                   "मन्या और अवटु की पहचान केवल सम्भावित है। "
                   "‘द्वे द्वे’ = दो-दो, यानी हर स्थान में दो; हर ओर दो हैं या नहीं, पाठ नहीं कहता। "
                   "‘नेत्रौष्ठ’ = नेत्र + ओष्ठ, अ + ओ → औ। "
                   "‘मन्याऽवटु’ का ऽ डेटा के अनुसार छपाई की आदत है, लोप का चिह्न नहीं। "
                   "गिनी गई वस्तु, स्नायु, पिछली पंक्तियों से चली आ रही है। "
                   "(समास में ओष्ठ से पहले अ + ओ → ओ भी विकल्प से होता है, जैसे बिम्बोष्ठ; यहाँ छपा औ है।)"),
    "hook": "दो-दो: मन्या, अवटु, आँख, होंठ, तालु।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 162, how many are given for each of its five places?",
            ("Two each", "द्वे द्वे: two each."),
            [("One each", "द्वे द्वे means two each, not one each."),
             ("Five in all", "द्वे द्वे gives two for each place; five is the number of places."),
             ("Four each", "द्वे द्वे means two each, not four each.")],
            "Two each in the five places.",
            "द्वे द्वे = two each."),
        order(1, "Put the places of unit 162 in the line's order.",
              ["मन्या", "अवटु", "नेत्र", "ओष्ठ", "तालु"],
              "Manyā, avaṭu, eyes, lips, palate.",
              "मन्या → अवटु → नेत्र → ओष्ठ → तालु."),
        match(2, "Match each word of unit 162 to its meaning.",
              [["द्वे द्वे", "two each"], ["नेत्र", "eye"], ["ओष्ठ", "lip"], ["तालु", "palate"]],
              "Two each in the eyes, lips and palate (and in the manyā and avaṭu).",
              "द्वे द्वे, नेत्र, ओष्ठ, तालु.", role="extend",
              teaches="A number said twice (द्वे द्वे) means 'two each', one count for every place named."),
        mcq("discriminate", 3, "Which split of नेत्रौष्ठ in unit 162 is right?",
            ("नेत्र + ओष्ठ", "अ + ओ → औ: नेत्र + ओष्ठ → नेत्रौष्ठ."),
            [("नेत्रौ + ष्ठ", "ष्ठ is not a word; the word is ओष्ठ, lip."),
             ("नेत्रे + ओष्ठ", "ए + ओ would not give औ."),
             ("नेत्रा + उष्ठ", "उष्ठ is not the word, and आ + उ would give ओ, not औ.")],
            "नेत्र (eye) + ओष्ठ (lip): अ + ओ → औ.",
            "अ + ओ → औ."),
        multi("apply", 4, "Which places get 'two each' in unit 162?",
              [("The eyes (netra)", "Right: नेत्र."),
               ("The tongue (jihvā)", "The tongue is not named in unit 162."),
               ("The palate (tālu)", "Right: तालु."),
               ("The jaws (hanu)", "The jaws are not named in unit 162; they come in unit 165.")],
              [0, 2],
              "Eyes and palate are among the five places.",
              "मन्याऽवटुनेत्रौष्ठतालुषु."),
        mcq("transfer", 5, "By the rule of नेत्र + ओष्ठ, how are वन + ओषधिः (forest herbs) joined?",
            ("वनौषधिः", "अ + ओ → औ, as नेत्र + ओष्ठ → नेत्रौष्ठ."),
            [("वनोषधिः", "अ before ओ is not dropped; the two join as औ."),
             ("वनवोषधिः", "व् comes from उ or ओ/औ before a vowel, not from अ."),
             ("वनाषधिः", "आ comes from अ + अ, not from अ + ओ.")],
            "वन + ओषधिः = वनौषधिः, like नेत्र + ओष्ठ = नेत्रौष्ठ.",
            "अ + ओ → औ.",
            teaches="Short अ followed by ओ joins as औ: नेत्र + ओष्ठ → नेत्रौष्ठ."),
    ],
}

# ---------------------------------------------------------------- unit 163
AUTHORED["163"] = {
    "title": "त्रिंशद्ग्रीवायां",
    "question": "By unit 163, what count is given for the neck (grīvā)?",
    "rule": ("Thirty (त्रिंशत्) in the neck (ग्रीवायाम्). Printed as one word: त् before the voiced ग becomes द्."),
    "limits": ("Prose, one printed word; no noun or verb is printed: the data carries the counted item, snāyu. Thirteen in "
               "the neck (card 113) and eight (card 129) belong to other lists (bones, joints)."),
    "explain_hi": ("यह एक छपे शब्द की गद्य-पंक्ति है: तीस, ग्रीवा यानी गर्दन में। "
                   "‘त्रिंशद्ग्रीवायां’ = त्रिंशत् + ग्रीवायाम्; घोष ग से पहले त् का द् हुआ है (इकाई १५५ में अघोष क से पहले त् रहा था)। "
                   "‘ग्रीवायाम्’ आकारान्त स्त्रीलिंग ग्रीवा का सप्तमी एकवचन है। "
                   "गिनी गई वस्तु, स्नायु, पिछली पंक्तियों से चली आ रही है। "
                   "इकाई ११३ (अस्थि, तेरह) और १२९ (सन्धि, आठ) की गर्दन वाली संख्याएँ दूसरी सूचियों की हैं।"),
    "hook": "गर्दन में तीस: त् + ग → द्ग।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 163, what count is given for the neck?",
            ("Thirty", "त्रिंशद्ग्रीवायां: thirty in the neck."),
            [("Thirteen", "त्रिंशत् is thirty; thirteen is त्रयोदश."),
             ("Eight", "त्रिंशत् is thirty, not eight."),
             ("Three", "त्रिंशत् is thirty; three is त्रीणि.")],
            "Thirty in the neck.",
            "त्रिंशत् = thirty; ग्रीवायाम् = in the neck."),
        match(1, "Match each part of unit 163 to its meaning.",
              [["त्रिंशत्", "thirty"], ["ग्रीवा", "neck"], ["ग्रीवायाम्", "in the neck"]],
              "त्रिंशत् + ग्रीवायाम् = thirty in the neck.",
              "त्रिंशत्, ग्रीवा, ग्रीवायाम्."),
        fill(2, "In unit 163 'in the neck' is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("ग्रीवायाम्", "grīvāyām", "grivayam"),
             "ग्रीवायाम् (printed ग्रीवायां) = in the neck.",
             "ग्रीवायाम् is the locative singular of ग्रीवा (neck): आ-stem + -आयाम्.",
             "त्रिंशत् + ग्रीवायाम् → त्रिंशद्ग्रीवायाम्."),
        mcq("discriminate", 3, "Which split of त्रिंशद्ग्रीवायां in unit 163 is right?",
            ("त्रिंशत् + ग्रीवायाम्", "त् before the voiced ग becomes द्."),
            [("त्रिंशद + ग्रीवायाम्", "त्रिंशद is not the number; the number is त्रिंशत्."),
             ("त्रिंश + द्ग्रीवायाम्", "द्ग्रीवायाम् is not a word; the word is ग्रीवायाम्."),
             ("त्रिंशत् + द्ग्रीवायाम्", "द्ग्रीवायाम् is not a word; the द् comes from त्.")],
            "त्रिंशत् (thirty) + ग्रीवायाम् (in the neck): त् + ग → द्ग.",
            "त् + voiced consonant → द्."),
        mcq("apply", 4, "What does the ending -आयाम् of ग्रीवायाम् mark in unit 163?",
            ("In: locative singular", "The data: ग्रीवायाम् is the locative singular, 'in the neck'."),
            [("From: ablative singular", "The ablative of ग्रीवा is ग्रीवायाः, not ग्रीवायाम्."),
             ("By: instrumental singular", "The instrumental of ग्रीवा is ग्रीवया."),
             ("To: accusative singular", "The accusative of ग्रीवा is ग्रीवाम्.")],
            "ग्रीवायाम् = in the neck.",
            "आ-stem (fem.) + -आयाम् = locative singular."),
        mcq("transfer", 5, "By the rule of त्रिंशत् + ग्रीवायाम्, how are सत् + गतिः (a good end) joined?",
            ("सद्गतिः", "त् before the voiced ग becomes द्, as त्रिंशत् + ग्रीवायाम् → त्रिंशद्ग्रीवायाम्."),
            [("सत्गतिः", "Before a voiced ग the final त् becomes द्; it does not stay त्."),
             ("सन्गतिः", "न् may come (optionally) only before a nasal; ग is not a nasal."),
             ("सच्गतिः", "च् comes from त् before च, छ or श, not before ग.")],
            "सत् + गतिः = सद्गतिः, like त्रिंशत् + ग्रीवायाम् = त्रिंशद्ग्रीवायाम्.",
            "त् + voiced consonant (ग) → द्.",
            teaches="Final त् before a voiced consonant like ग becomes द्: त्रिंशत् + ग्रीवायाम् → त्रिंशद्ग्रीवायाम्."),
    ],
}

# ---------------------------------------------------------------- unit 164
AUTHORED["164"] = {
    "title": "त्रीणि जत्रुणि",
    "question": "By unit 164, what count is given for the jatru (collar-bone)?",
    "rule": ("Three (त्रीणि) in the jatru (collar-bone, standard). The data reads जत्रुणि as a locative singular but leaves "
             "its number uncertain."),
    "limits": ("Prose; the counted item (snāyu) is carried, not printed. Medium confidence: whether जत्रुणि is singular or "
               "plural is open, so no question on its case or number. Unit 160 gives four for the akṣaka, also glossed "
               "collar-bone; the text does not say how the two differ."),
    "explain_hi": ("यह दो शब्दों की गद्य-पंक्ति है: तीन, जत्रु यानी हँसली में। "
                   "डेटा ‘जत्रुणि’ को सप्तमी एकवचन पढ़ता है, पर दो हँसलियों के लिए द्विवचन (जत्र्वोः) अपेक्षित होता; इसलिए वचन अनिश्चित है। "
                   "इकाई १६० में अक्षक (वह भी हँसली) के चार थे; पाठ दोनों शब्दों का भेद नहीं बताता। "
                   "‘त्रीणि’ में र् के बाद न का ण हुआ है। "
                   "गिनी गई वस्तु, स्नायु, पिछली पंक्तियों से चली आ रही है।"),
    "hook": "जत्रु में तीन, अक्षक में चार।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 164, what count is given for the jatru?",
            ("Three", "त्रीणि जत्रुणि: three in the jatru."),
            [("Thirty", "त्रीणि is three; thirty is त्रिंशत्."),
             ("Four", "त्रीणि is three, not four."),
             ("Thirteen", "त्रीणि is three; thirteen is त्रयोदश.")],
            "Three in the jatru.",
            "त्रीणि = three."),
        match(1, "Match each number word to its value.",
              [["त्रीणि", "three"], ["त्रिंशत्", "thirty"], ["चत्वारि", "four"], ["चत्वारिंशत्", "forty"]],
              "त्रीणि 3 (unit 164), त्रिंशत् 30 (163), चत्वारि 4 (160, 165), चत्वारिंशत् 40 (153, 155).",
              "त्रीणि, त्रिंशत्, चत्वारि, चत्वारिंशत्."),
        fill(2, "In unit 164 the number 'three' is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("त्रीणि", "trīṇi", "trini"),
             "त्रीणि = three; जत्रुणि = in the jatru.",
             "त्रीणि = three (the form standing before जत्रुणि); त्रिंशत् is thirty.",
             "त्रीणि जत्रुणि."),
        mcq("discriminate", 3, "The data glosses both जत्रु (unit 164) and अक्षक (unit 160) as collar-bone. What count does each get?",
            ("Jatru 3, akṣaka 4", "त्रीणि जत्रुणि (164); चत्वार्यक्षकयोः (160)."),
            [("Jatru 4, akṣaka 3", "The counts are the other way round: jatru three, akṣaka four."),
             ("Jatru 3, akṣaka 8", "Eight is the shoulders' count (unit 161), not the akṣaka's."),
             ("Jatru 30, akṣaka 4", "Thirty is the neck's count (unit 163), not the jatru's.")],
            "Jatru three, akṣaka four: two words, two counts.",
            "त्रीणि जत्रुणि; चत्वारि अक्षकयोः."),
        multi("apply", 4, "Which statements fit unit 164?",
              [("It gives four for the jatru", "त्रीणि is three; four is the akṣaka's count (unit 160)."),
               ("It gives three for the jatru", "Right: त्रीणि जत्रुणि."),
               ("Its counted item is not printed", "Right: snāyu is carried from the lines before."),
               ("It says jatru and akṣaka are one bone", "The line says nothing about the akṣaka.")],
              [1, 2],
              "Three in the jatru; the counted item is carried, not printed.",
              "त्रीणि जत्रुणि."),
        mcq("transfer", 5, "In त्रीणि, न became ण after र with only a vowel between. By that rule, how is गुरु + ना (by the teacher) written?",
            ("गुरुणा", "र, then only the vowel उ, then न: the न becomes ण, as in त्रीणि."),
            [("गुरुना", "After र with only a vowel between, न becomes ण; it does not stay न."),
             ("गुरूना", "The vowel is not lengthened, and the न should become ण."),
             ("गुरुन्ना", "No न is doubled; the single न becomes ण.")],
            "गुरु + ना = गुरुणा, like त्री + नि = त्रीणि.",
            "र + (vowels only) + न → ण.",
            teaches="न after र in the same word, with only vowels between, becomes ण: त्रीणि."),
    ],
}

# ---------------------------------------------------------------- unit 165
AUTHORED["165"] = {
    "title": "चत्वारिहन्वोः",
    "question": "By unit 165, what count is given for the two jaws (hanu)?",
    "rule": ("Four (चत्वारि) in the two jaws (हन्वोः, dual of हनु: उ before ओ becomes व्). Printed run together, but no "
             "sandhi joins चत्वारि to हन्वोः."),
    "limits": ("Prose; the counted item (snāyu) is carried, not printed. The data reads हन्वोः as locative dual; -ओः is also a "
               "genitive dual: no question on its case. Per side or in all is not said."),
    "explain_hi": ("यह गद्य-पंक्ति कहती है: चार, हनु यानी दोनों जबड़ों में। "
                   "छपा ‘चत्वारिहन्वोः’ दो शब्द हैं जो साथ छप गए: चत्वारि हन्वोः; इनमें कोई सन्धि नहीं, क्योंकि इ का य् केवल स्वर से पहले होता है और ह व्यंजन है। "
                   "‘हन्वोः’ = हनु + ओः; स्वर से पहले उ का व् हुआ है। "
                   "डेटा इसे सप्तमी द्विवचन पढ़ता है। "
                   "गिनी गई वस्तु, स्नायु, पिछली पंक्तियों से चली आ रही है।"),
    "hook": "दोनों जबड़ों में चार।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 165, what count is given for the two jaws (hanu)?",
            ("Four", "चत्वारिहन्वोः: four in the two jaws."),
            [("Eight", "चत्वारि is four, not eight."),
             ("Two", "चत्वारि is four, not two."),
             ("Twelve", "चत्वारि is four, not twelve.")],
            "Four in the two jaws.",
            "चत्वारि = four; हन्वोः = in the two jaws."),
        match(1, "Match each part of unit 165 to its meaning.",
              [["चत्वारि", "four"], ["हनु", "jaw"], ["हन्वोः", "in the two jaws"]],
              "चत्वारि हन्वोः = four in the two jaws.",
              "चत्वारि, हनु, हन्वोः."),
        mcq("extend", 2, "Why is चत्वारि not changed before हन्वोः in unit 165?",
            ("ह is not a vowel", "इ becomes य् only before a vowel; ह is a consonant, so चत्वारि stays."),
            [("ह is an unvoiced sound", "ह is voiced, and voicing does not matter here; only a vowel would change इ."),
             ("चत्वारि can never change", "It does change before a vowel: चत्वार्यक्षकयोः (unit 160)."),
             ("The print drops a य", "The data: two words run together, no sandhi involved.")],
            "चत्वारि + हन्वोः: before a consonant the final इ stays.",
            "इ + vowel → य्; इ + consonant → no change.",
            teaches="Final इ changes to य् only before a different vowel: चत्वार्यक्षकयोः, but चत्वारि हन्वोः."),
        mcq("discriminate", 3, "Which split of हन्वोः in unit 165 is right?",
            ("हनु + ओः", "उ before a different vowel becomes व्: हनु + ओः → हन्वोः."),
            [("हन् + वोः", "हन् is not the stem here, and वोः is not an ending; the word is हनु."),
             ("हन्व + ओः", "अ + ओ would give औ: हन्वौः, not हन्वोः."),
             ("हनु + वोः", "That would give हनुवोः; the व् comes from the उ.")],
            "हनु (jaw) + ओः (dual ending): उ + ओ → व्ओ.",
            "उ + different vowel → व्."),
        order(4, "Put the counts of units 162-165 in the text's order.",
              ["द्वे द्वे मन्या... तालुषु", "त्रिंशद्ग्रीवायां", "त्रीणि जत्रुणि", "चत्वारिहन्वोः"],
              "Two each in five places; thirty in the neck; three in the jatru; four in the two jaws.",
              "द्वे द्वे → त्रिंशत् → त्रीणि → चत्वारि.", role="apply"),
        mcq("transfer", 5, "By the rule of हनु + ओः, how are धेनु (cow) + ओः (dual ending) joined?",
            ("धेन्वोः", "उ before a different vowel becomes व्, as हनु + ओः → हन्वोः."),
            [("धेनुवोः", "The उ does not stay beside an added व्; the उ itself becomes व्."),
             ("धेनौः", "उ + ओ does not give औ; the उ becomes व्."),
             ("धेन्वौः", "The ending is ओः; nothing turns it into औः.")],
            "धेनु + ओः = धेन्वोः, like हनु + ओः = हन्वोः.",
            "उ + different vowel → व्.",
            teaches="उ before a different vowel becomes व्: हनु + ओः → हन्वोः."),
    ],
}


# ===================================================================== NOTES_HI
NOTES_HI = {
    "153": ("छपा ‘चत्वारिंशदूरौ’ = चत्वारिंशत् + ऊरौ (स्वर से पहले त् → द्)। ‘ऊरौ’ = ऊरु का सप्तमी एकवचन। "
            "डेटा का विश्वास उच्च; कोई text_flag नहीं, कोई अस्पष्ट पंक्ति नहीं। गिनी गई वस्तु छपी नहीं।"),
    "154": ("छपा ‘वंक्षणे’ = वङ्क्षणे (क से पहले अनुस्वार = ङ्)। डेटा लिंग ‘पुं./नपुं.’ दोनों सम्भव बताता है। "
            "डेटा का विश्वास उच्च; कोई text_flag नहीं। गिनी गई वस्तु छपी नहीं।"),
    "155": ("छपा ‘चत्वारिंशत्कट्यां’ = चत्वारिंशत् + कट्याम् (अघोष क से पहले त् अपरिवर्तित)। पंक्ति-अन्त का ं = म् (छपाई)। "
            "कटि = कूल्हा या कमर (डेटा)। डेटा का विश्वास उच्च; कोई text_flag नहीं।"),
    "156": ("text_flag (सम्भावित): छपा ‘मेंद्र’ कोई शब्द नहीं; डेटा ‘मेढ्र’ (लिंग) पढ़ने का सुझाव देता है, क्योंकि ढ का ‘ंद’ पढ़ा जाना "
            "सम्भव है। यह केवल सम्भावित पाठ है; इस पर कोई प्रश्न नहीं। विश्वास मध्यम। समास: मुष्क-मेढ्र-बस्ति-अन्त्रेषु (द्वन्द्व, सप्तमी "
            "बहुवचन)। सन्धि: विंशतिः + मुष्क → विंशतिर्मुष्क (इः + घोष, र के सिवा → इर्); बस्ति + अन्त्र → बस्त्यन्त्र (इ + अ → य)। "
            "मुष्क, बस्ति, अन्त्र की पहचान मानक।"),
    "157": ("‘अशीतिः पृष्ठे’: अघोष प से पहले विसर्ग बना रहता है। डेटा का विश्वास उच्च; कोई text_flag नहीं। गिनी गई वस्तु छपी नहीं।"),
    "158": ("‘षष्टिः पार्श्वयोः’: अघोष प से पहले विसर्ग बना रहता है। ‘पार्श्वयोः’ द्विवचन; -योः षष्ठी या सप्तमी दोनों हो सकता है, "
            "डेटा सप्तमी पढ़ता है। डेटा का विश्वास उच्च; कोई text_flag नहीं।"),
    "159": ("छपा ‘अष्टादशोरसि’ = अष्टादश + उरसि (अ + उ → ओ)। ‘उरसि’ = उरस् का सप्तमी एकवचन। "
            "डेटा का विश्वास उच्च; कोई text_flag नहीं।"),
    "160": ("छपा ‘चत्वार्यक्षकयोः’ = चत्वारि + अक्षकयोः (इ + अ → य)। अक्षक = हँसली (मानक)। डेटा की टिप्पणी: इस खण्ड में धड़ का छपा "
            "जोड़ ४० + २० + ८० + ६० + १८ + ४ = २२२, इकाई १४६ के २३० से कम; आगे और स्थान आ सकते हैं। विश्वास उच्च।"),
    "161": ("छपा ‘अष्टावंसयोः’ = अष्टौ + अंसयोः (स्वर से पहले औ → आव्)। डेटा: संज्ञा व क्रिया छपी नहीं; गिनी गई वस्तु (स्नायु) इकाई १४४ "
            "से चली आ रही है; पंक्ति स्नायु-गिनती को आगे बढ़ाती प्रतीत होती है। विश्वास उच्च; कोई text_flag नहीं।"),
    "162": ("डेटा: मन्या (सम्भवतः गर्दन का पार्श्व) और अवटु (सम्भवतः गर्दन के पीछे का गड्ढा) की पहचान केवल सम्भावित; दोनों शब्द गर्दन/ग्रीवा-पृष्ठ "
            "के भाग भी पढ़े गए हैं। ‘मन्याऽवटु’ का ऽ छपाई की आदत है, लोप नहीं। सन्धि: नेत्र + ओष्ठ → नेत्रौष्ठ (अ + ओ → औ)। "
            "पाठ यह नहीं कहता कि हर स्थान में हर ओर दो हैं या नहीं। विश्वास मध्यम।"),
    "163": ("छपा ‘त्रिंशद्ग्रीवायां’ = त्रिंशत् + ग्रीवायाम् (घोष ग से पहले त् → द्); अन्त का ं = म् (छपाई)। ग्रीवा = गर्दन (मानक)। "
            "डेटा: गिनी गई वस्तु (स्नायु) पिछली पंक्तियों से। विश्वास उच्च; कोई text_flag नहीं।"),
    "164": ("डेटा: ‘जत्रुणि’ को जत्रु (नपुं.) का सप्तमी एकवचन पढ़ा गया; दो हँसलियों के लिए द्विवचन ‘जत्र्वोः’ अपेक्षित होता, इसलिए वचन "
            "अनिश्चित है (ह्रस्व स्वर वाला नपुं. बहुवचन ‘जत्रूणि’ भी सम्भव माना गया)। संख्या छपे अनुसार। विश्वास मध्यम; इसके वचन या "
            "विभक्ति पर कोई प्रश्न नहीं। ‘त्रीणि’ में र् के बाद न → ण।"),
    "165": ("छपा ‘चत्वारिहन्वोः’ दो शब्द हैं जो साथ छपे (चत्वारि हन्वोः); डेटा के अनुसार कोई सन्धि नहीं। हन्वोः = हनु + ओः (उ → व्), "
            "सप्तमी द्विवचन (डेटा)। हनु = जबड़ा (मानक)। विश्वास उच्च; कोई text_flag नहीं।"),
}


# ===================================================================== AIDS
_RUN = ("स्नायु-गिनती (इकाई १४४): कुल ९०० → शाखाओं में ६०० (१४५) → धड़ में २३० (१४६) → ऊपर ७० (१४७)।")

AIDS = {
    "153": {
        "chunks": "चत्वारिंशदूरौ (= चत्वारिंशत् | ऊरौ)",
        "sandhi": "स्वर से पहले त् → द्: चत्वारिंशत् + ऊरौ → चत्वारिंशदूरौ।",
        "chain": {"steps": ["कुल ९०० स्नायु (इकाई १४४)", "शाखाओं में ६०० (१४५)", "एक शाखा में १५० (डेटा की जाँच)",
                            "उस सूची में: ऊरु में ४० (१५३)"]},
    },
    "154": {
        "chunks": "दश | वंक्षणे",
        "sandhi": "अनुस्वार क-वर्ग से पहले = ङ्: वंक्षणे = वङ्क्षणे।",
        "diagram": {"groups": [
            {"label": "एक शाखा (डेटा की जाँच, इकाई १४५)", "items": ["हर पादांगुली में छह (३०)", "पादतल, कूर्च, गुल्फ में दस-दस",
                                                               "जंघा ३०", "जानु १०", "ऊरु ४०", "वंक्षण १०", "योग १५०"]}]},
        "frame": _RUN + " इकाई १४८-१५४ एक शाखा की सूची है; यह पंक्ति उसकी अन्तिम संख्या है।",
    },
    "155": {
        "chunks": "चत्वारिंशत्कट्यां (= चत्वारिंशत् | कट्याम्)",
        "sandhi": "अघोष क से पहले त् अपरिवर्तित: चत्वारिंशत् + कट्याम् → चत्वारिंशत्कट्याम् (इकाई १५३ से तुलना: स्वर से पहले द्)।",
        "frame": _RUN + " डेटा की इकाई १६० वाली धड़ की जाँच कटि के ४० से आरम्भ होती है।",
    },
    "156": {
        "chunks": "विंशतिर्मुष्कमेंद्रबस्त्यंत्रेषु (= विंशतिः | मुष्क-मेंद्र(?)-बस्ति-अन्त्रेषु)",
        "sandhi": "इः + घोष ध्वनि (र के सिवा) → इर्: विंशतिः + मुष्क → विंशतिर्मुष्क · इ + अ → य: बस्ति + अन्त्रेषु → बस्त्यन्त्रेषु।",
        "anchors": "याद-सूत्र (मेरी याद-पद्धति): पंक्ति के क्रम में चार: मुष्क → मेंद्र (छपा) → बस्ति → अन्त्र; बीस चारों के लिए मिलाकर।",
    },
    "157": {
        "chunks": "अशीतिः | पृष्ठे",
        "sandhi": "अघोष प से पहले विसर्ग बना रहता है: अशीतिः पृष्ठे (घोष से पहले होता तो अशीतिर्)।",
        "pegs": "मेरा बनाया संकेत (केवल सुनने की सहायता): ‘अशीति’ और ‘अस्सी’ की ध्वनि मिलती-जुलती है; डेटा की धड़ वाली जाँच में यही सबसे बड़ी संख्या (८०) है।",
    },
    "158": {
        "chunks": "षष्टिः | पार्श्वयोः",
        "sandhi": "अघोष प से पहले विसर्ग बना रहता है: षष्टिः पार्श्वयोः।",
        "contrast": "षष्टि (साठ) और पार्श्वयोः (दो पार्श्व): संख्या एक, स्थान दो; हर ओर कितने, पंक्ति नहीं कहती।",
    },
    "159": {
        "chunks": "अष्टादशोरसि (= अष्टादश | उरसि)",
        "sandhi": "अ + उ → ओ: अष्टादश + उरसि → अष्टादशोरसि।",
        "pegs": "केवल सुनने की सहायता (मेरी): अष्टा-दश = आठ और दस = अठारह; अष्टौ = आठ; अशीति = अस्सी।",
    },
    "160": {
        "chunks": "चत्वार्यक्षकयोः (= चत्वारि | अक्षकयोः)",
        "sandhi": "इ + अ → य: चत्वारि + अक्षकयोः → चत्वार्यक्षकयोः।",
        "diagram": {"groups": [
            {"label": "धड़ (इकाई १५५-१६०, क्रम से)", "items": ["कटि ४०", "मुष्क, मेंद्र (छपा), बस्ति, अन्त्र २०", "पृष्ठ ८०",
                                                           "पार्श्व (दोनों) ६०", "उरस् १८", "अक्षक (दोनों) ४"]},
            {"label": "जोड़", "items": ["छपा जोड़ (डेटा): २२२", "धड़ का कुल (इकाई १४६): २३०"]}]},
    },
    "161": {
        "chunks": "अष्टावंसयोः (= अष्टौ | अंसयोः)",
        "sandhi": "औ + स्वर → आव्: अष्टौ + अंसयोः → अष्टावंसयोः।",
        "frame": "डेटा: संज्ञा व क्रिया छपी नहीं; गिनी गई वस्तु (स्नायु) इकाई १४४ से चली आ रही है। यहाँ केवल संख्या + स्थान।",
    },
    "162": {
        "chunks": "द्वे द्वे | मन्याऽवटुनेत्रौष्ठतालुषु",
        "sandhi": "अ + ओ → औ: नेत्र + ओष्ठ → नेत्रौष्ठ · आ + अ → आ: मन्या + अवटु → मन्यावटु (छपा ऽ केवल छपाई की आदत)।",
        "diagram": {"groups": [
            {"label": "दो-दो (क्रम से)", "items": ["१ मन्या (सम्भावित: गर्दन का पार्श्व)", "२ अवटु (सम्भावित: गर्दन के पीछे का गड्ढा)",
                                                  "३ नेत्र", "४ ओष्ठ", "५ तालु"]}]},
    },
    "163": {
        "chunks": "त्रिंशद्ग्रीवायां (= त्रिंशत् | ग्रीवायाम्)",
        "sandhi": "घोष व्यंजन ग से पहले त् → द्: त्रिंशत् + ग्रीवायाम् → त्रिंशद्ग्रीवायाम्।",
    },
    "164": {
        "chunks": "त्रीणि | जत्रुणि",
        "sandhi": "र् के बाद, बीच में केवल स्वर हो तो, न → ण: त्री + नि → त्रीणि।",
        "anchors": "याद-सूत्र (मेरी याद-पद्धति): दो शब्द, दोनों ‘हँसली’: अक्षक में चार (इकाई १६०), जत्रु में तीन (इकाई १६४)।",
    },
    "165": {
        "chunks": "चत्वारिहन्वोः (= चत्वारि | हन्वोः; साथ छपे, सन्धि नहीं)",
        "sandhi": "उ + भिन्न स्वर → व्: हनु + ओः → हन्वोः · व्यंजन ह से पहले इ अपरिवर्तित: चत्वारि हन्वोः।",
        "diagram": {"groups": [
            {"label": "इकाई १६१-१६५ (क्रम से)", "items": ["अंस (दोनों) ८", "मन्या, अवटु, नेत्र, ओष्ठ, तालु: दो-दो", "ग्रीवा ३०",
                                                       "जत्रु ३", "हनु (दोनों) ४"]}]},
    },
}


# ===================================================================== IMAGE_SPECS
IMAGE_SPECS = {
    ("153", "chain"): {
        "file": "sh5-snayu-ganana-153.svg",
        "alt": ("Chain of the snāyu (ligament) count: 900 in all (card 144), 600 in the four limbs (145), 150 in one limb "
                "by the data's check, and in that list forty in the thigh (153)."),
        "type": "chain",
        "title": "स्नायु की गिनती",
        "steps": ["कुल ९०० (इकाई १४४)", "शाखाओं में ६०० (१४५)", "एक शाखा में १५० (डेटा की जाँच)",
                  "उस सूची में: ऊरु ४० (१५३)"],
    },
    ("154", "diagram"): {
        "file": "sh5-snayu-shakha-154.svg",
        "alt": ("Table of one limb's snāyu by the data's check at card 145: six in each toe (30), ten each in the sole, kūrca "
                "and ankle, shank 30, knee 10, thigh 40, groin 10; total 150."),
        "type": "table",
        "title": "एक शाखा की स्नायु (इकाई १४८-१५४)",
        "heads": ["स्थान", "संख्या"],
        "rows": [["हर पादांगुली", "छह-छह (३०)"], ["पादतल, कूर्च, गुल्फ", "दस-दस (३०)"], ["जंघा", "३०"], ["जानु", "१०"],
                 ["ऊरु", "४०"], ["वंक्षण", "१०"], ["योग (डेटा की जाँच)", "१५०"]],
    },
    ("160", "diagram"): {
        "file": "sh5-snayu-antaradhi-160.svg",
        "alt": ("Table of the trunk counts of units 155-160 in text order: hip 40; muṣka, printed meṃdra, basti, antra 20; back "
                "80; the two flanks 60; chest 18; the two collarbones 4; printed sum 222 against the trunk total of 230 (card 146)."),
        "type": "table",
        "title": "धड़ की स्नायु (इकाई १५५-१६०)",
        "heads": ["स्थान", "संख्या"],
        "rows": [["कटि", "४०"], ["मुष्क, मेंद्र (छपा), बस्ति, अन्त्र", "२०"], ["पृष्ठ", "८०"], ["पार्श्व (दोनों)", "६०"],
                 ["उरस्", "१८"], ["अक्षक (दोनों)", "४"], ["छपा जोड़ (डेटा)", "२२२"], ["धड़ का कुल (इकाई १४६)", "२३०"]],
    },
    ("162", "diagram"): {
        "file": "sh5-dve-dve-162.svg",
        "alt": ("Table of unit 162: two each in five numbered places in line order: manyā (probable: side of the neck), "
                "avaṭu (probable: hollow at the nape), eye, lip, palate."),
        "type": "table",
        "title": "इकाई १६२: दो-दो",
        "heads": ["क्रम व स्थान", "संख्या"],
        "rows": [["१ मन्या (सम्भावित: गर्दन का पार्श्व)", "दो"], ["२ अवटु (सम्भावित: गर्दन के पीछे का गड्ढा)", "दो"],
                 ["३ नेत्र", "दो"], ["४ ओष्ठ", "दो"], ["५ तालु", "दो"]],
    },
    ("165", "diagram"): {
        "file": "sh5-griva-hanu-165.svg",
        "alt": ("Table of units 161-165 in text order: the two shoulders 8; manyā, avaṭu, eye, lip, palate two each; neck 30; "
                "jatru 3; the two jaws 4."),
        "type": "table",
        "title": "इकाई १६१-१६५ की गिनती",
        "heads": ["स्थान", "संख्या"],
        "rows": [["अंस (दोनों)", "८"], ["मन्या, अवटु, नेत्र, ओष्ठ, तालु", "दो-दो"], ["ग्रीवा", "३०"], ["जत्रु", "३"],
                 ["हनु (दोनों)", "४"]],
    },
}
