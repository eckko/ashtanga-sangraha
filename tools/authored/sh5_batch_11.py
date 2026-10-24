from helpers import mcq, match, order, fill, multi, accepts


AUTHORED = {}

# ---------------------------------------------------------------- unit 128
AUTHORED["128"] = {
    "title": "अष्टावुरसि",
    "question": "By unit 128, what count is given for the chest, and how does it close the trunk total?",
    "rule": ("Eight (अष्टौ) in the chest (उरसि). With 3 (unit 125, hip kapālas on a conjectural reading), 24 (unit 126) and the flanks 'likewise' (unit 127, "
             "presumably 24) it makes 59, the trunk total of unit 121."),
    "limits": ("Prose, one printed word; no verb and no counted noun are printed (probably the bone-joints, from unit 119). "
               "The flanks' 24 is presumed from तद्वत् (unit 127), not printed."),
    "explain_hi": ("यह एक छपे शब्द की गद्य-पंक्ति है: अष्टौ (आठ) + उरसि (छाती में)। "
                   "गिनी गई वस्तु छपी नहीं; इकाई ११९ से सम्भवतः अस्थि-सन्धियाँ, पर ‘सन्धि’ शब्द इस पंक्ति में छपा नहीं। "
                   "धड़ की गिनती इसी से पूरी होती है: कटिकपाल (अनुमानित पाठ; छपा कति) में ३ (इकाई १२५), रीढ़ में २४ (इकाई १२६), "
                   "पार्श्वों में ‘तद्वत्’ यानी सम्भवतः २४ (इकाई १२७) और छाती में ८। "
                   "इनका जोड़ ५९ है, जो इकाई १२१ के धड़ वाले योग से मिलता है। "
                   "स्वर उ से पहले अष्टौ का औ आव् बना है।"),
    "hook": "छाती के आठ से धड़ के उनसठ पूरे।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "Unit 128 gives eight for which part of the trunk?",
            ("The chest (उरस्)", "अष्टावुरसि = अष्टौ उरसि: eight in the chest."),
            [("The spine (पृष्ठवंश)", "The spine has twenty-four (unit 126), not eight."),
             ("The flanks (पार्श्व)", "The flanks have 'likewise' (unit 127), presumably twenty-four."),
             ("The hips (कटिकपाल, conjectural)", "Unit 125 gives three for the hip kapālas (conjectural reading), not eight.")],
            "Eight in the chest.",
            "अष्टौ = eight; उरसि = in the chest."),
        order(1, "Arrange the trunk counts of units 125-128 in the text's order.",
              ["३ कटिकपालों में (अनुमानित पाठ)", "२४ रीढ़ में", "तद्वत् पार्श्वों में", "८ छाती में"],
              "Hips 3 (conjectural reading), spine 24, flanks likewise, chest 8: unit 128 closes the trunk count.",
              "१२५ → १२६ → १२७ → १२८."),
        match(2, "Match each form of unit 128 to its meaning.",
              [["अष्टौ", "eight"], ["उरस्", "chest"], ["उरसि", "in the chest"]],
              "अष्टौ + उरसि, printed अष्टावुरसि: eight in the chest.",
              "अष्टौ, उरस्, उरसि.", role="extend",
              teaches="उरसि is the locative singular of उरस् (chest): 'in the chest'."),
        mcq("discriminate", 3, "Which split of the printed अष्टावुरसि is right?",
            ("अष्टौ + उरसि", "औ before a vowel becomes आव्: अष्टौ + उरसि → अष्टावुरसि."),
            [("अष्टा + वुरसि", "वुरसि is not a word; the व् comes from the औ of अष्टौ."),
             ("अष्टाव + उरसि", "अष्टाव is not a form; the numeral is अष्टौ."),
             ("अष्टः + उरसि", "अष्टः is not a form, and अः + उ would drop the visarga.")],
            "अष्टौ (eight) + उरसि (in the chest): औ + उ → आवु.",
            "औ + vowel → आव् + that vowel."),
        mcq("apply", 4, "By unit 128's data, what do 3 + 24 + 24 (flanks, presumed) + 8 make?",
            ("59, the trunk total of unit 121", "3 + 24 + 24 + 8 = 59, the एकोनषष्टि of unit 121."),
            [("68, the limb total of unit 120", "68 is the limbs' total; the trunk sum is 59."),
             ("80, the upper total of unit 122", "80 is printed for above; the trunk sum is 59."),
             ("57, two short of unit 121", "3 + 24 + 24 + 8 is 59, not 57.")],
            "3 + 24 + 24 + 8 = 59, matching the trunk total (unit 121).",
            "Hips 3 (conjectural reading) + spine 24 + flanks 24 + chest 8 = 59."),
        mcq("transfer", 5, "By the rule of अष्टावुरसि, how are उभौ + अपि (both, too) joined?",
            ("उभावपि", "औ before a vowel becomes आव्, as अष्टौ + उरसि → अष्टावुरसि."),
            [("उभोऽपि", "ओऽ comes from ओ (or अः) before अ, not from औ."),
             ("उभयपि", "अय् comes from ए before a vowel, not from औ."),
             ("उभौपि", "औ does not swallow the next vowel; it becomes आव्.")],
            "उभौ + अपि = उभावपि, like अष्टौ + उरसि = अष्टावुरसि.",
            "औ + vowel → आव्.",
            teaches="औ before a vowel becomes आव्: अष्टौ + उरसि → अष्टावुरसि."),
    ],
}

# ---------------------------------------------------------------- unit 129
AUTHORED["129"] = {
    "title": "अष्टौ ग्रीवायां",
    "question": "By unit 129, how many are counted for the neck?",
    "rule": ("Eight (अष्टौ) in the neck (ग्रीवायाम्, locative singular of ग्रीवा). By the data's check (unit 134) this "
             "opens the count of the region above the trunk."),
    "limits": ("Prose, two words; no verb and no counted noun are printed (probably the bone-joints, from unit 119). Whether eight is "
               "the neck's sum or per part is not said."),
    "explain_hi": ("यह दो शब्दों की गद्य-पंक्ति है: आठ, गर्दन में। "
                   "‘ग्रीवायाम्’ ग्रीवा (गर्दन, आकारान्त स्त्रीलिंग) का सप्तमी एकवचन है; छपाई में अन्त का म् अनुस्वार (ं) से लिखा है। "
                   "डेटा की जाँच (इकाई १३४) के अनुसार ऊपर वाले भाग (गर्दन और सिर) की गिनती यहीं से शुरू होती है। "
                   "गिनी गई वस्तु और क्रिया छपी नहीं; इकाई ११९ से सम्भवतः अस्थि-सन्धियाँ।"),
    "hook": "छाती में आठ, गर्दन में भी आठ।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 129, how many are counted in the neck?",
            ("Eight", "अष्टौ ग्रीवायाम्: eight in the neck."),
            [("Six", "अष्टौ is eight, not six."),
             ("Ten", "अष्टौ is eight, not ten."),
             ("Twenty-four", "Twenty-four is the spine's count (unit 126).")],
            "Eight in the neck.",
            "अष्टौ = eight; ग्रीवायाम् = in the neck."),
        match(1, "Match each form of unit 129 to its meaning.",
              [["अष्टौ", "eight"], ["ग्रीवा", "neck"], ["ग्रीवायाम्", "in the neck"]],
              "अष्टौ ग्रीवायाम् = eight in the neck.",
              "अष्टौ, ग्रीवा, ग्रीवायाम्."),
        fill(2, "In unit 129 'in the neck' is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("ग्रीवायाम्", "grīvāyām", "grivayam"),
             "ग्रीवायाम् = in the neck; the print writes it ग्रीवायां.",
             "ग्रीवायाम् is the locative singular of ग्रीवा (neck).",
             "ग्रीवा → ग्रीवायाम् (in)."),
        mcq("discriminate", 3, "What form is ग्रीवायाम् in unit 129?",
            ("Locative singular: in the neck", "Data: f. loc. sg.; -आयाम् is the locative of an आ-stem."),
            [("Genitive singular: of the neck", "The genitive of ग्रीवा is ग्रीवायाः, not ग्रीवायाम्."),
             ("Dative singular: to the neck", "The dative of ग्रीवा is ग्रीवायै, not ग्रीवायाम्."),
             ("Nominative plural: the necks", "The nominative plural is ग्रीवाः, not ग्रीवायाम्.")],
            "ग्रीवायाम् = in the neck (locative singular).",
            "आ-stem feminine: locative singular -आयाम्."),
        mcq("apply", 4, "In अष्टौ ग्रीवायाम्, which word tells the place?",
            ("ग्रीवायाम्, the locative", "The locative ग्रीवायाम् gives the place: in the neck."),
            [("अष्टौ, the numeral", "अष्टौ gives how many (eight), not where."),
             ("Neither; place is unstated", "The place is printed: ग्रीवायाम्, in the neck."),
             ("Both words read as one", "They are two words: a number and a place.")],
            "अष्टौ = how many; ग्रीवायाम् = where.",
            "Number + locative place: अष्टौ ग्रीवायाम्."),
        mcq("transfer", 5, "By the pattern of ग्रीवायाम् (in the neck), which form of नासा (nose) means in the nose, a new example?",
            ("नासायाम्", "आ-stem feminine + -याम् = 'in', as ग्रीवा → ग्रीवायाम्."),
            [("नासायाः", "नासायाः is the genitive or ablative: of or from the nose."),
             ("नासाम्", "नासाम् is the accusative singular, not 'in'."),
             ("नासे", "नासे is the vocative singular or the nominative/accusative dual, not 'in'.")],
            "नासा → नासायाम् (in the nose), like ग्रीवा → ग्रीवायाम्.",
            "आ-stem feminine: locative singular -आयाम्.",
            teaches="Feminine आ-stems take -आयाम् for 'in': ग्रीवा → ग्रीवायाम्."),
    ],
}

# ---------------------------------------------------------------- unit 130
AUTHORED["130"] = {
    "title": "त्रयःकंठनाड्यां",
    "question": "By unit 130, how many are counted in the kaṇṭhanāḍī, and what is it probably?",
    "rule": ("Three (त्रयः) in the kaṇṭhanāḍī, the throat-channel: probably the windpipe (probable; the gullet is the "
             "alternative). The visarga of त्रयः stays before the unvoiced क."),
    "limits": ("Prose, confidence medium. The identification windpipe is only probable (data; the gullet is the "
               "alternative): questions give it only with that label, never as certain. No verb or counted noun is "
               "printed (probably the bone-joints, from unit 119)."),
    "explain_hi": ("यह गद्य-पंक्ति कहती है: तीन, कण्ठनाड़ी में। "
                   "कण्ठनाड़ी का शब्दार्थ है गले की नली; डेटा के अनुसार यह सम्भवतः श्वासनली है, दूसरा सम्भव अर्थ अन्ननली। "
                   "‘कण्ठनाड्याम्’ नाडी का सप्तमी एकवचन है: ई + आ → या। "
                   "‘त्रयः’ का विसर्ग अघोष क से पहले बना रहता है; छपाई में दोनों शब्द जुड़े हैं। "
                   "गिनी गई वस्तु (सम्भवतः अस्थि-सन्धियाँ, इकाई ११९ से) इस पंक्ति में छपी नहीं।"),
    "hook": "गले की नली में तीन।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 130, how many are counted in the kaṇṭhanāḍī?",
            ("Three", "त्रयः कण्ठनाड्याम्: three in the kaṇṭhanāḍī."),
            [("Two", "त्रयः is three, not two."),
             ("Six", "त्रयः is three, not six."),
             ("Ten", "त्रयः is three, not ten.")],
            "Three in the kaṇṭhanāḍī.",
            "त्रयः = three."),
        match(1, "Match each part of unit 130 to its meaning.",
              [["त्रयः", "three"], ["कण्ठ", "throat"], ["नाडी", "channel, tube"],
               ["कण्ठनाडी", "throat-channel, probably the windpipe (probable)"]],
              "त्रयः कण्ठनाड्याम् = three in the throat-channel, probably the windpipe.",
              "त्रयः, कण्ठ, नाडी, कण्ठनाडी."),
        mcq("extend", 2, "Why does the visarga of त्रयः stay before कंठ in unit 130?",
            ("क is unvoiced, so it stays", "Before an unvoiced क the visarga stays: त्रयः कण्ठ-."),
            [("क is voiced, so it stays", "क is unvoiced; before a voiced consonant अः becomes ओ."),
             ("Before क it becomes स्", "स् comes before त or थ, not before क."),
             ("Before क it becomes श्", "श् comes before च or छ, not before क.")],
            "त्रयः + कण्ठ-: the visarga stays before the unvoiced क.",
            "Visarga + क/ख/प/फ → stays.",
            teaches="A visarga stays before the unvoiced क, ख, प, फ: त्रयः कण्ठनाड्याम्."),
        mcq("discriminate", 3, "Which is the locative singular of नाडी, as in unit 130?",
            ("नाड्याम्", "ई + आ → या: नाडी + आम् → नाड्याम्, 'in the channel'."),
            [("नाड्याः", "नाड्याः is the genitive or ablative singular."),
             ("नाडीम्", "नाडीम् is the accusative singular."),
             ("नाडीषु", "नाडीषु is the locative plural, 'in the channels'.")],
            "नाड्याम् = in the channel (locative singular).",
            "ई-stem feminine: locative singular -याम्."),
        multi("apply", 4, "Which statements fit unit 130 and its data?",
              [("It prints the counted noun in the line", "No counted noun is printed; probably the bone-joints, from unit 119."),
               ("It gives three for the kaṇṭhanāḍī", "Right: त्रयः, three."),
               ("It names the gullet for certain", "The data gives windpipe as probable; nothing is certain."),
               ("Its kaṇṭhanāḍī is probably the windpipe", "Right: probable, by the data.")],
              [1, 3],
              "Three in the kaṇṭhanāḍī, probably the windpipe; the counted noun is not printed.",
              "त्रयः कण्ठनाड्याम्."),
        mcq("transfer", 5, "By the rule of त्रयःकंठ, how are शिष्यः + कथयति (the pupil tells) joined?",
            ("शिष्यः कथयति", "Before the unvoiced क the visarga stays, as त्रयः कण्ठ-."),
            [("शिष्यो कथयति", "अः becomes ओ only before a voiced consonant; क is unvoiced."),
             ("शिष्यस्कथयति", "स् comes before त or थ, not before क."),
             ("शिष्य कथयति", "The visarga after अ is not dropped before a consonant like क.")],
            "शिष्यः + कथयति = शिष्यः कथयति, like त्रयः + कण्ठ-.",
            "Visarga before क stays.",
            teaches="Before the unvoiced क the visarga stays: त्रयः + कण्ठनाड्याम्."),
    ],
}

# ---------------------------------------------------------------- unit 131
AUTHORED["131"] = {
    "title": "अष्टादश कंठनाडीनिबद्धा",
    "question": "By unit 131, how many are bound to the kaṇṭhanāḍī, and in which places?",
    "rule": ("Eighteen (अष्टादश), bound to the kaṇṭhanāḍī, in the heart (हृदय), liver (यकृत्), kloma (identity "
             "disputed) and channels (नाडी)."),
    "limits": ("Prose, confidence medium. Printed निबद्धा does not agree with the plural (text flag: possibly निबद्धाः). "
               "The last compound may also read 'in the channels of heart, liver and kloma'. kloma's identity is disputed. "
               "No question rests on these. The counted noun is unprinted (probably the bone-joints, from unit 119)."),
    "explain_hi": ("यह गद्य-पंक्ति अठारह (गिनी गई वस्तु छपी नहीं; सम्भवतः अस्थि-सन्धियाँ, इकाई ११९ से) बताती है, जो कण्ठनाड़ी से बँधी हैं (निबद्ध)। "
                   "स्थान हैं: हृदय, यकृत (जिगर), क्लोम (पहचान विवादित; फेफड़ा, अग्न्याशय आदि सुझाए गए) और नाड़ियाँ। "
                   "अन्तिम समास को चार सदस्यों का द्वन्द्व पढ़ा गया; दूसरा पाठ है ‘हृदय, यकृत और क्लोम की नाड़ियों में’। "
                   "छपा ‘निबद्धा’ बहुवचन संख्या से मेल नहीं खाता; सम्भवतः विसर्ग छूटा है (निबद्धाः)। "
                   "‘अष्टादश’ = अष्टन् (आठ; दश से पहले अष्टा-) + दश (दस) = अठारह।"),
    "hook": "कण्ठनाड़ी से बँधी अठारह: हृदय, यकृत, क्लोम, नाड़ियाँ।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 131, how many are bound to the kaṇṭhanāḍī?",
            ("Eighteen", "अष्टादश कंठनाडीनिबद्धा (as printed): eighteen bound to the kaṇṭhanāḍī."),
            [("Twelve", "अष्टादश is eighteen, not twelve."),
             ("Sixteen", "अष्टादश is eighteen, not sixteen."),
             ("Twenty-eight", "अष्टादश is eighteen, not twenty-eight.")],
            "Eighteen, bound to the kaṇṭhanāḍī.",
            "अष्टादश = eighteen."),
        order(1, "Put these printed parts of unit 131 in the line's order.",
              ["अष्टादश", "कंठनाडीनिबद्धा", "हृदय", "यकृत्", "क्लोम", "नाडीषु"],
              "Eighteen, bound to the kaṇṭhanāḍī, in heart, liver, kloma and channels.",
              "अष्टादश → कंठनाडीनिबद्धा → हृदय → यकृत् → क्लोम → नाडीषु."),
        match(2, "Match each word of unit 131 to its meaning.",
              [["अष्टादश", "eighteen"], ["निबद्ध", "bound"], ["हृदय", "heart"], ["यकृत्", "liver"]],
              "Eighteen, bound to the kaṇṭhanāḍī, in the heart, the liver and the rest.",
              "अष्टादश, निबद्ध, हृदय, यकृत्.", role="extend",
              teaches="निबद्ध = bound, fastened: these eighteen are bound to the kaṇṭhanāḍī."),
        mcq("discriminate", 3, "How is the number अष्टादश built?",
            ("Eight plus ten: eighteen", "अष्टन् (eight, अष्टा- before दश) + दश (ten) = अष्टादश, eighteen."),
            [("Eight times ten: eighty", "Eighty is अशीति (unit 122), not अष्टादश."),
             ("Ten less eight: two", "Nothing is taken away; दश is added to अष्ट."),
             ("Eight hundreds: 800", "Hundreds would use शत; अष्टादश has दश, ten.")],
            "अष्टा- (eight) + दश (ten) = 18.",
            "अष्टन् → अष्टा- + दश = अष्टादश (18)."),
        multi("apply", 4, "Which places does unit 131 name for its eighteen?",
              [("The heart (हृदय)", "Right: हृदय is named."),
               ("The tooth-roots (दन्तमूल)", "The tooth-roots come in unit 132."),
               ("The liver (यकृत्)", "Right: यकृत् is named."),
               ("The nose (नासा)", "The nose comes in unit 133."),
               ("The channels (नाडी)", "Right: नाडीषु, in the channels.")],
              [0, 2, 4],
              "Heart, liver, kloma and channels.",
              "हृदययकृत्क्लोमनाडीषु."),
        mcq("transfer", 5, "By the pattern of कण्ठनाडीनिबद्ध, what does स्नायुनिबद्ध mean, a new example?",
            ("Bound to the ligaments", "X-निबद्ध = bound to X, as कण्ठनाडी-निबद्ध."),
            [("Binding the ligaments", "निबद्ध is 'bound' (passive), not 'binding'."),
             ("Cut from the ligaments", "निबद्ध means bound, not cut off."),
             ("Free of the ligaments", "निबद्ध means bound, the opposite of free.")],
            "स्नायुनिबद्ध = bound to the ligaments, like कण्ठनाडीनिबद्ध.",
            "X + निबद्ध = bound to X.",
            teaches="निबद्ध (bound) closes a compound: कण्ठनाडीनिबद्ध = bound to the kaṇṭhanāḍī."),
    ],
}

# ---------------------------------------------------------------- unit 132
AUTHORED["132"] = {
    "title": "द्वात्रिंशद्दंतमूलेषु",
    "question": "By unit 132, how many are counted in the tooth-roots?",
    "rule": ("Thirty-two (द्वात्रिंशत्) in the tooth-roots (दन्तमूलेषु). Final त् becomes द् before the voiced द: "
             "द्वात्रिंशद्दन्त-."),
    "limits": ("Prose, confidence high. No verb or counted noun is printed (probably the bone-joints, from unit 119). The line does "
               "not say one per root."),
    "explain_hi": ("यह गद्य-पंक्ति कहती है: बत्तीस, दाँतों की जड़ों में। "
                   "‘दन्तमूलेषु’ = दन्त (दाँत) + मूल (जड़), सप्तमी बहुवचन: जड़ों में। "
                   "‘द्वात्रिंशत्’ का त् घोष द से पहले द् बना है, इसलिए छपा रूप द्वात्रिंशद्दंत है। "
                   "गिनी गई वस्तु (सम्भवतः अस्थि-सन्धियाँ, इकाई ११९ से) और क्रिया छपी नहीं।"),
    "hook": "दाँतों की जड़ों में बत्तीस।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 132, how many are counted in the tooth-roots?",
            ("Thirty-two", "द्वात्रिंशद्दन्तमूलेषु: thirty-two in the tooth-roots."),
            [("Twelve", "द्वात्रिंशत् is thirty-two, not twelve."),
             ("Eighteen", "द्वात्रिंशत् is thirty-two, not eighteen."),
             ("Twenty-two", "द्वात्रिंशत् is thirty-two, not twenty-two.")],
            "Thirty-two in the tooth-roots.",
            "द्वात्रिंशत् = thirty-two."),
        match(1, "Match each part of unit 132 to its meaning.",
              [["द्वात्रिंशत्", "thirty-two"], ["दन्त", "tooth"], ["मूल", "root"], ["मूलेषु", "in the roots"]],
              "द्वात्रिंशत् दन्तमूलेषु = thirty-two in the tooth-roots.",
              "द्वात्रिंशत्, दन्त, मूल, मूलेषु."),
        fill(2, "In unit 132 the word for tooth is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("दन्त", "danta"),
             "दन्त = tooth; दन्तमूल = tooth-root.",
             "दन्त + मूल = tooth-root.",
             "दन्त (tooth) + मूलेषु (in the roots)."),
        mcq("discriminate", 3, "Which split of द्वात्रिंशद्दंतमूलेषु is right?",
            ("द्वात्रिंशत् + दन्तमूलेषु", "त् before the voiced द becomes द्: द्वात्रिंशद्दन्त-."),
            [("द्वात्रिंशः + दन्तमूलेषु", "अः before the voiced द would give ओ, not द्द."),
             ("द्वात्रिंशन् + दन्तमूलेषु", "The numeral ends in त्; न् is not its final."),
             ("द्वात्रिंशद्द + अन्तमूलेषु", "अन्तमूल is not the word; the word is दन्तमूल.")],
            "द्वात्रिंशत् (32) + दन्तमूलेषु (in the tooth-roots).",
            "त् + voiced consonant → द्."),
        multi("apply", 4, "Which statements fit unit 132?",
              [("The thirty-two are in the tooth-roots", "Right: दन्तमूलेषु."),
               ("The counted noun is printed", "No counted noun is printed; probably the bone-joints, from unit 119."),
               ("The thirty-two are in the eyelids", "The eyelids come in unit 134, two each."),
               ("मूलेषु is locative plural: in the roots", "Right: data, n. loc. pl.")],
              [0, 3],
              "Thirty-two in the tooth-roots; the counted noun is not printed.",
              "द्वात्रिंशत् + दन्तमूलेषु."),
        mcq("transfer", 5, "By the rule of द्वात्रिंशद्दन्त, how are त्रिंशत् + दिनानि (thirty days) joined?",
            ("त्रिंशद्दिनानि", "त् before the voiced द becomes द्, as द्वात्रिंशत् + दन्त-."),
            [("त्रिंशत्दिनानि", "Before a voiced consonant त् does not stay unvoiced."),
             ("त्रिंशन्दिनानि", "त् becomes न् only before a nasal; द is not a nasal."),
             ("त्रिंशच्दिनानि", "त् becomes च् before च, छ or श, not before द.")],
            "त्रिंशत् + दिनानि = त्रिंशद्दिनानि.",
            "त् + voiced consonant → द्.",
            teaches="A final त् becomes द् before a voiced consonant: द्वात्रिंशत् + दन्त → द्वात्रिंशद्दन्त."),
    ],
}

# ---------------------------------------------------------------- unit 133
AUTHORED["133"] = {
    "title": "एकैकः काकलनासामूर्द्धसु",
    "question": "By unit 133, how many are counted in the kākala, the nose and the head?",
    "rule": ("One each (एकैकः) in the kākala (a throat part, identity disputed), the nose (नासा) and the head (मूर्धन्). "
             "एकैक = एक + एक (अ + ए → ऐ)."),
    "limits": ("Prose, confidence medium. kākala's identity is disputed (uvula or larynx prominence proposed): no question "
               "on it. Printed मूर्द्धसु (doubled ध्) is normalised to मूर्धसु. No counted noun is printed (probably the bone-joints, from unit 119)."),
    "explain_hi": ("यह गद्य-पंक्ति कहती है: एक-एक, काकल, नाक और मूर्धा (सिर) में। "
                   "काकल गले का एक भाग है जिसकी पहचान विवादित है (कौआ या कण्ठ का उभार सुझाए गए)। "
                   "‘एकैकः’ = एक + एक, अ + ए → ऐ; अर्थ: एक-एक। "
                   "‘मूर्धसु’ मूर्धन् का सप्तमी बहुवचन है; पूरे द्वन्द्व पर यही विभक्ति लगी है। "
                   "छपाई का ‘मूर्द्धसु’ (दोहरा ध) केवल लिखावट का भेद है।"),
    "hook": "काकल, नाक, सिर: एक-एक।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 133, how many are counted in each of its three places?",
            ("One each", "एकैकः = one each."),
            [("Two each", "Two each is unit 134; एकैकः is one each."),
             ("Three each", "एकैकः is one each, not three."),
             ("Eight each", "एकैकः is one each, not eight.")],
            "One each in kākala, nose and head.",
            "एकैकः = one each."),
        order(1, "Put these printed parts of unit 133 in the line's order.",
              ["एकैकः", "काकल", "नासा", "मूर्द्धसु"],
              "One each in the kākala, the nose and the head.",
              "एकैकः → काकल → नासा → मूर्द्धसु."),
        match(2, "Match each word of unit 133 to its meaning.",
              [["एकैकः", "one each"], ["नासा", "nose"], ["मूर्धन्", "head, crown"]],
              "एकैकः ... नासा, मूर्धन्: one each in the nose and the head (and the kākala).",
              "एकैकः, नासा, मूर्धन्.", role="extend",
              teaches="एकैक = एक + एक: a repeated one, 'one each'."),
        mcq("discriminate", 3, "Which split of एकैकः is right?",
            ("एक + एकः", "अ + ए → ऐ: एक + एकः → एकैकः."),
            [("एक + इकः", "अ + इ gives ए, not ऐ; and इक is not the word."),
             ("एकः + एकः", "अः before ए drops the visarga: एक एकः, unjoined."),
             ("एके + एकः", "ए before a vowel becomes अय् (or अ), not ऐ.")],
            "एक + एकः = एकैकः (one each).",
            "अ + ए → ऐ."),
        mcq("apply", 4, "What does the ending -सु of काकलनासामूर्धसु mark?",
            ("In: the locative plural", "Data: loc. pl.; -सु = 'in' (the plural)."),
            [("Of: the genitive plural", "The genitive plural of मूर्धन् is मूर्ध्नाम्."),
             ("By: the instrumental plural", "The instrumental plural is मूर्धभिः."),
             ("From: the ablative plural", "The ablative plural is मूर्धभ्यः.")],
            "-सु marks the locative plural: in the kākala, nose and head.",
            "-सु = locative plural, 'in'."),
        mcq("transfer", 5, "By the rule of एकैकः, how are तत्र + एव (there itself) joined?",
            ("तत्रैव", "अ + ए → ऐ, as एक + एकः → एकैकः."),
            [("तत्रेव", "ए comes from अ + इ, not from अ + ए."),
             ("तत्रयेव", "अय् comes from ए before a vowel, not from अ + ए."),
             ("तत्रोव", "ओ comes from अ + उ, not from अ + ए.")],
            "तत्र + एव = तत्रैव, like एक + एकः = एकैकः.",
            "अ + ए → ऐ.",
            teaches="अ + ए → ऐ: एक + एकः → एकैकः."),
    ],
}

# ---------------------------------------------------------------- unit 134
AUTHORED["134"] = {
    "title": "द्वौ द्वौ गंडकर्ण... पंच शिरःकपालेषु",
    "question": "By unit 134, how many joints are in the six face joints, above the eyebrows and in the head kapālas?",
    "rule": ("Two each (द्वौ द्वौ) in the joints of cheek, ear, temple, eyelid, eye and jaw; two above the eyebrows; five "
             "in the head kapālas. Units 129-134 then sum to 83, not unit 122's printed 80."),
    "limits": ("Two printed lines, prose. सन्धि, last in the compound, is read as governing all six. The 83 against 80 "
               "rests on the data's check; which number the text meant is open (unit 122's flag): no question on it."),
    "explain_hi": ("इस इकाई में दो छपी पंक्तियाँ हैं। "
                   "पहली: गण्ड (गाल), कर्ण (कान), शंख (कनपटी), वर्त्म (पलक), नेत्र (आँख) और हनु (जबड़ा) की सन्धियों में दो-दो; "
                   "समास के अन्त का ‘सन्धि’ छहों पर लगता है। "
                   "दूसरी: दोनों भौंहों के ऊपर दो, और सिर के कपालों में पाँच। "
                   "डेटा की जाँच: इकाई १२९ से १३४ तक ८ + ३ + १८ + ३२ + ३ + १२ + २ + ५ = ८३, जबकि इकाई १२२ में ‘अस्सी’ छपा है। "
                   "मूल में कौन-सी संख्या थी, यह खुला प्रश्न है।"),
    "hook": "चेहरे के छह जोड़ दो-दो, भौंह पर दो, कपाल में पाँच।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 134, how many joints are in the head kapālas?",
            ("Five", "पञ्च शिरःकपालेषु: five in the kapālas of the head."),
            [("Two", "Two is above the eyebrows; the head kapālas have five."),
             ("Three", "Three is unit 125's kapāla count (hip, on a conjectural reading), not the head."),
             ("Eight", "Eight is the neck (unit 129), not the head kapālas.")],
            "Five in the head kapālas.",
            "पञ्च शिरःकपालेषु."),
        order(1, "Put the six places of the first line of unit 134 in the compound's order.",
              ["गण्ड", "कर्ण", "शङ्ख", "वर्त्म", "नेत्र", "हनु"],
              "Cheek, ear, temple, eyelid, eye, jaw: two joints each.",
              "गण्ड → कर्ण → शङ्ख → वर्त्म → नेत्र → हनु."),
        match(2, "Match each word of unit 134 to its meaning.",
              [["गण्ड", "cheek"], ["शङ्ख", "temple"], ["वर्त्म", "eyelid"], ["हनु", "jaw"], ["भ्रू", "eyebrow"]],
              "Cheek, temple, eyelid, jaw; above the eyebrows.",
              "गण्ड, शङ्ख, वर्त्म, हनु, भ्रू.", role="extend",
              teaches="सन्धि, the last member of the long compound, is read with all six: the joints of cheek, ear and so on."),
        mcq("discriminate", 3, "Which split of द्वावुपरिष्टाद्भ्रुवोः is right?",
            ("द्वौ + उपरिष्टात् + भ्रुवोः", "औ + उ → आवु; त् before the voiced भ → द्."),
            [("द्वा + उपरिष्टात् + भ्रुवोः", "आ + उ would give ओ: द्वोपरिष्टात्."),
             ("द्वौ + उपरिष्टः + भ्रुवोः", "अः before the voiced भ would give ओ, not द्भ."),
             ("द्वाव + उपरिष्टा + द्भ्रुवोः", "द्वाव and द्भ्रुवोः are not words.")],
            "द्वौ (two) + उपरिष्टात् (above) + भ्रुवोः (of the two eyebrows).",
            "औ + vowel → आव्; त् + voiced consonant → द्."),
        mcq("apply", 4, "By the data's check, what do the upper counts of units 129-134 add up to?",
            ("83, three more than eighty", "8 + 3 + 18 + 32 + 3 + 12 + 2 + 5 = 83."),
            [("80, the same as unit 122", "The sites add up to 83; unit 122 prints 80."),
             ("77, three fewer than eighty", "8 + 3 + 18 + 32 + 3 + 12 + 2 + 5 is 83, not 77."),
             ("86, six more than eighty", "8 + 3 + 18 + 32 + 3 + 12 + 2 + 5 is 83, not 86.")],
            "The sites sum to 83, against the printed 80 of unit 122.",
            "Neck 8 + 3 + 18 + 32 + 3 + 12 + 2 + 5 = 83."),
        mcq("transfer", 5, "By the pattern of द्वौ द्वौ (two each), what does पञ्च पञ्च mean in a new example?",
            ("Five each", "A repeated numeral means 'each': द्वौ द्वौ = two each."),
            [("Ten in all", "The repetition is not added: it means 'each'."),
             ("Twenty-five", "The repetition is not multiplied: it means 'each'."),
             ("Only five", "The repetition gives 'each', not 'only'.")],
            "पञ्च पञ्च = five each, like द्वौ द्वौ = two each.",
            "Numeral repeated = 'X each'.",
            teaches="A numeral said twice means 'each': द्वौ द्वौ = two each."),
    ],
}

# ---------------------------------------------------------------- unit 135
AUTHORED["135"] = {
    "title": "...गुल्फजानुमणिबंधकूर्परेषु कोरसंज्ञाः",
    "question": "By unit 135, which joints are named kora (bud) and which ulūkhala (mortar)?",
    "rule": ("Kora (bud) joints: in the fingers or toes (conjectural), ankles, knees, wrists and elbows. Ulūkhala (mortar) "
             "joints: in the armpits, groins and tooth-roots. These open the eight kinds summed in unit 142."),
    "limits": ("Two printed lines, prose, confidence medium. The first member मेंगुलि is not a word; अङ्गुलि is a "
               "conjecture (text flag): no question rests on it. The noun 'joints' is unstated, shown as '(ones)'."),
    "explain_hi": ("इस इकाई से अस्थि-सन्धियों के आठ प्रकार शुरू होते हैं (योग इकाई १४२ में)। "
                   "पहली पंक्ति: (अनुमानित पाठ पर) उँगलियों, गुल्फ (टखने), जानु (घुटने), मणिबन्ध (कलाई) और कूर्पर (कुहनी) की सन्धियाँ ‘कोर’ यानी कली नामक हैं। "
                   "दूसरी पंक्ति: कक्षा (काँख), वंक्षण और दाँतों की जड़ों की सन्धियाँ ‘उलूखल’ यानी ओखली नामक हैं। "
                   "छपा ‘मेंगुलि’ कोई शब्द नहीं; ‘अङ्गुलि’ केवल अनुमान है। "
                   "‘मूलेषूलूखल’ में उ + उ → ऊ हुआ है।"),
    "hook": "अंगों के जोड़ कली, काँख-दाँत के ओखली।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 135, what name do the joints of armpits, groins and tooth-roots get?",
            ("Ulūkhala (mortar)", "कक्षावङ्क्षणदन्तमूलेषूलूखलसंज्ञाः: named ulūkhala."),
            [("Kora (bud)", "Kora is the name of the limb joints in the first line."),
             ("Sāmudga (casket)", "Sāmudga is named in unit 136, for other sites."),
             ("Pratara (a kind)", "Pratara is the neck and spine (unit 137).")],
            "Armpits, groins, tooth-roots: ulūkhala.",
            "कक्षा, वङ्क्षण, दन्तमूल → उलूखल."),
        match(1, "Match each word of unit 135 to its meaning.",
              [["कोर", "bud"], ["उलूखल", "mortar"], ["गुल्फ", "ankle"], ["मणिबन्ध", "wrist"], ["कूर्पर", "elbow"],
               ["कक्षा", "armpit"]],
              "Kora (bud) at ankle, wrist, elbow; ulūkhala (mortar) at the armpit.",
              "कोर, उलूखल, गुल्फ, मणिबन्ध, कूर्पर, कक्षा."),
        order(2, "Put the sure kora sites of unit 135 in the line's order.",
              ["गुल्फ", "जानु", "मणिबन्ध", "कूर्पर"],
              "Ankle, knee, wrist, elbow (after the conjectural first member).",
              "गुल्फ → जानु → मणिबन्ध → कूर्पर.", role="extend",
              teaches="X-संज्ञ (a bahuvrīhi) = named X: कोरसंज्ञाः = (ones) named kora."),
        mcq("discriminate", 3, "Which split of the printed मूलेषूलूखल is right?",
            ("मूलेषु + उलूखल", "उ + उ → ऊ: मूलेषु + उलूखल → मूलेषूलूखल."),
            [("मूलेषू + लूखल", "लूखल is not a word; the word is उलूखल."),
             ("मूले + षूलूखल", "षूलूखल is not a word; the ending is -एषु."),
             ("मूलेषः + उलूखल", "अः before उ would drop the visarga: मूलेष उलूखल.")],
            "मूलेषु (in the roots) + उलूखल (mortar): उ + उ → ऊ.",
            "उ + उ → ऊ."),
        mcq("apply", 4, "By unit 135, what kind of joint is in the wrist?",
            ("Kora (bud)", "मणिबन्ध is in the kora list."),
            [("Ulūkhala (mortar)", "Ulūkhala is the armpit, groin and tooth-roots."),
             ("Maṇḍala (circle)", "Maṇḍala is throat, eyes, heart and so on (unit 140)."),
             ("Sāmudga (casket)", "Sāmudga is named in unit 136, not for the wrist.")],
            "The wrist (मणिबन्ध) has kora joints.",
            "गुल्फ, जानु, मणिबन्ध, कूर्पर → कोर."),
        mcq("transfer", 5, "By the rule of मूलेषूलूखल, how are साधु + उक्तम् (well said) joined?",
            ("साधूक्तम्", "उ + उ → ऊ, as मूलेषु + उलूखल → मूलेषूलूखल."),
            [("साध्वुक्तम्", "उ → व् only before a different vowel; here both are उ."),
             ("साधोक्तम्", "ओ comes from अ + उ, not from उ + उ."),
             ("साधुक्तम्", "Two उ make a long ऊ; the length is not lost.")],
            "साधु + उक्तम् = साधूक्तम्.",
            "उ + उ → ऊ.",
            teaches="Two like vowels merge into the long vowel: उ + उ → ऊ (मूलेषु + उलूखल)."),
    ],
}

# ---------------------------------------------------------------- unit 136
AUTHORED["136"] = {
    "title": "अंसपीठ... सामुद्गाः",
    "question": "By unit 136, which joints are of the sāmudga (casket) kind?",
    "rule": ("Sāmudga (casket-type) joints: in the aṃsapīṭha (probably the shoulder-blade region), the anus (गुद), the "
             "bhaga (female genital organ) and, on a conjectural reading, the hips. सामुद्ग is from समुद्ग, a lidded box."),
    "limits": ("Prose, confidence medium. Printed तितंब is not a word; नितम्ब (hip) is a conjecture: no question on it. "
               "aṃsapīṭha is probable only. The noun 'joints' is unstated."),
    "explain_hi": ("यह गद्य-पंक्ति एक और सन्धि-प्रकार बताती है: सामुद्ग, यानी डिब्बी (समुद्ग, ढक्कन वाली डिब्बी) जैसी। "
                   "स्थान: अंसपीठ (सम्भवतः कन्धे के फलक का क्षेत्र), गुद (गुदा), भग (स्त्री-जननांग) और अनुमानित पाठ पर नितम्ब। "
                   "छपा ‘तितंब’ कोई शब्द नहीं; ‘नितम्ब’ केवल अनुमान है। "
                   "छपा ‘गुद्भग’ = गुद-भग, अर्थ वही। "
                   "‘-एषु’ सप्तमी बहुवचन है: इन स्थानों में।"),
    "hook": "डिब्बी जैसे जोड़: अंसपीठ, गुद, भग।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 136, what kind of joint does it name?",
            ("Sāmudga (casket)", "सामुद्गाः: of the sāmudga (casket) kind."),
            [("Kora (bud)", "Kora is named in unit 135, for the limb joints."),
             ("Ulūkhala (mortar)", "Ulūkhala is named in unit 135, for armpit etc."),
             ("Maṇḍala (circle)", "Maṇḍala is named in unit 140, for throat etc.")],
            "Unit 136 names the sāmudga joints.",
            "... सामुद्गाः."),
        match(1, "Match each word of unit 136 to its meaning.",
              [["अंसपीठ", "shoulder-seat, probably the shoulder-blade region (probable)"], ["गुद", "anus"],
               ["भग", "female genital organ"], ["सामुद्ग", "of the casket kind"]],
              "Shoulder-seat, anus, bhaga: sāmudga joints.",
              "अंसपीठ, गुद, भग, सामुद्ग."),
        mcq("extend", 2, "By the data, what word is सामुद्ग formed from?",
            ("समुद्ग, a lidded box", "Data: sāmudga is from samudga, a casket or lidded box."),
            [("समुद्र, the ocean", "The word has द्ग, not द्र: it is from समुद्ग."),
             ("मुद्ग, a kind of bean", "The data derives it from समुद्ग, a casket."),
             ("मुद्रा, a seal or mark", "The data derives it from समुद्ग, a casket.")],
            "सामुद्ग ← समुद्ग (casket).",
            "सामुद्ग = of the casket (समुद्ग) kind.",
            teaches="सामुद्ग is derived from समुद्ग (a casket, lidded box): a casket-type joint."),
        mcq("discriminate", 3, "Which place is NOT a sāmudga site in unit 136?",
            ("The knee (जानु)", "The knee has kora joints (unit 135)."),
            [("The anus (गुद)", "गुद is a sāmudga site in unit 136."),
             ("The bhaga (भग)", "भग is a sāmudga site in unit 136."),
             ("The aṃsapīṭha (अंसपीठ)", "अंसपीठ is a sāmudga site in unit 136.")],
            "Knee is kora; aṃsapīṭha, anus and bhaga are sāmudga.",
            "अंसपीठ, गुद, भग (...) → सामुद्ग."),
        multi("apply", 4, "Which statements fit unit 136 and its data?",
              [("It gives a number for each place", "No number is printed in unit 136."),
               ("Its kind is named sāmudga", "Right: सामुद्गाः."),
               ("It names the eyes among its places", "The eyes are maṇḍala (unit 140)."),
               ("The word for joints is not printed", "Right: the noun is unstated, shown as '(ones)'.")],
              [1, 3],
              "Sāmudga kind; no numbers; the noun is unstated.",
              "... सामुद्गाः."),
        mcq("transfer", 5, "By the ending -एषु (in the ...), which form of वृक्ष (tree) means in the trees, a new example?",
            ("वृक्षेषु", "An अ-stem takes -एषु for the locative plural, as the compound of unit 136."),
            [("वृक्षाः", "वृक्षाः is the nominative plural, 'the trees'."),
             ("वृक्षैः", "वृक्षैः is the instrumental plural, 'by the trees'."),
             ("वृक्षे", "वृक्षे is the locative singular, 'in the tree'.")],
            "वृक्षेषु = in the trees.",
            "अ-stem: locative plural -एषु.",
            teaches="अ-stems take -एषु for 'in' (plural): unit 136's place compound ends in -एषु, in the (places)."),
    ],
}

# ---------------------------------------------------------------- unit 137
AUTHORED["137"] = {
    "title": "ग्रीवापृष्ठवंशयोःप्रतराः",
    "question": "By unit 137, what kind of joint is in the neck and the spine?",
    "rule": ("Pratara joints are in the neck (ग्रीवा) and the spine (पृष्ठवंश). The two-member dvandva takes the dual: "
             "ग्रीवापृष्ठवंशयोः, 'in neck and spine'."),
    "limits": ("Prose, confidence high. pratara is a name; its literal sense is left untranslated by the data. No number "
               "is given. The noun 'joints' is unstated."),
    "explain_hi": ("यह गद्य-पंक्ति कहती है: ग्रीवा (गर्दन) और पृष्ठवंश (रीढ़) में ‘प्रतर’ नामक सन्धियाँ। "
                   "प्रतर एक प्रकार का नाम है; डेटा ने उसका शब्दार्थ नहीं दिया। "
                   "‘ग्रीवापृष्ठवंशयोः’ दो सदस्यों का द्वन्द्व है, इसलिए द्विवचन (सप्तमी): गर्दन और रीढ़ में। "
                   "‘-योः’ का विसर्ग अघोष प से पहले बना रहा है।"),
    "hook": "गर्दन और रीढ़: प्रतर।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 137, what kind of joint is in the neck and spine?",
            ("Pratara", "ग्रीवापृष्ठवंशयोः प्रतराः."),
            [("Maṇḍala", "Maṇḍala is throat, eyes, heart and so on (unit 140)."),
             ("Sāmudga", "Sāmudga is aṃsapīṭha, anus and so on (unit 136)."),
             ("Kora", "Kora is ankle, knee, wrist and so on (unit 135).")],
            "Neck and spine: pratara.",
            "ग्रीवा, पृष्ठवंश → प्रतर."),
        order(1, "Put the parts of unit 137 in the line's order.",
              ["ग्रीवा", "पृष्ठवंशयोः", "प्रतराः"],
              "Neck, spine: pratara (ones).",
              "ग्रीवा → पृष्ठवंशयोः → प्रतराः."),
        match(2, "Match each word of unit 137 to its meaning.",
              [["ग्रीवा", "neck"], ["पृष्ठवंश", "spine"], ["प्रतर", "the name of a kind of joint"]],
              "Neck and spine: pratara joints.",
              "ग्रीवा, पृष्ठवंश, प्रतर.", role="extend",
              teaches="पृष्ठवंश = back-ridge, the spine (data, standard)."),
        mcq("discriminate", 3, "Why is ग्रीवापृष्ठवंशयोः in the dual in unit 137?",
            ("The dvandva joins two places", "Neck + spine = two members, so the dual."),
            [("Each place has two joints", "No number is given in unit 137."),
             ("The spine is taken as two sides", "The data reads two places, neck and spine."),
             ("The dual shows respect here", "The dual counts the two members, neck and spine.")],
            "Two members (neck, spine) → dual.",
            "Dvandva of two → dual ending."),
        mcq("apply", 4, "Which word of unit 137 names what is found, not where?",
            ("प्रतराः", "The nominative प्रतराः names the kind of joint."),
            [("पृष्ठवंशयोः", "This locative dual gives the place: in neck and spine."),
             ("ग्रीवा-", "ग्रीवा is the first member of the place compound."),
             ("None: all name places", "प्रतराः is not a place; it names the joints' kind.")],
            "प्रतराः = what; ग्रीवापृष्ठवंशयोः = where.",
            "Locative = place; nominative = the thing named."),
        mcq("transfer", 5, "By the pattern of -वंशयोः, which form of हस्त (hand) means in the two hands, a new example?",
            ("हस्तयोः", "अ-stem + -योः = locative (also genitive) dual, as पृष्ठवंशयोः."),
            [("हस्ताभ्याम्", "-आभ्याम् is instrumental, dative or ablative dual, not 'in'."),
             ("हस्तेषु", "हस्तेषु is the locative plural, 'in the hands' (more than two)."),
             ("हस्ते", "हस्ते is the locative singular (or nom./acc. dual), not 'in the two hands'.")],
            "हस्तयोः = in the two hands.",
            "अ-stem: locative dual -योः.",
            teaches="अ-stems take -योः in the locative dual: पृष्ठवंश → पृष्ठवंशयोः."),
    ],
}

# ---------------------------------------------------------------- unit 138
AUTHORED["138"] = {
    "title": "शिरःकतिकपालेषु तूनसेवनीसंज्ञाः",
    "question": "By unit 138, what is said of the joints in the head kapālas, and how sure is the reading?",
    "rule": ("In the head (and, on a conjectural reading, hip) kapālas: joints named tunnasevanī (also conjectural). "
             "सेवनी, printed, means a seam or suture."),
    "limits": ("Prose, confidence LOW. Two conjectures: कति → कटि (hip) and तून → तुन्न: no question on either. Only the "
               "sure parts are asked: शिरः, कपाल, सेवनी, संज्ञाः."),
    "explain_hi": ("यह गद्य-पंक्ति कम विश्वास वाली है, क्योंकि दो छपे शब्द अर्थ नहीं देते। "
                   "छपा ‘कति’ (कितने) यहाँ अर्थ नहीं देता; अनुमानित पाठ ‘कटि’ (कमर) है, जैसे इकाई १२५ में। "
                   "छपा ‘तून’ कोई ज्ञात शब्द नहीं; ज्ञात नाम ‘तुन्नसेवनी’ है, पर यह भी अनुमान है। "
                   "पक्का भाग: शिरः (सिर), कपाल (खपरे जैसी अस्थि), सेवनी (सिलाई, सीवन) और संज्ञाः (नामक)। "
                   "अर्थ: सिर (और अनुमानित पाठ पर कमर) के कपालों में सीवन-जैसी नामक सन्धियाँ।"),
    "hook": "सिर के कपाल: सिलाई जैसे जोड़।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What does सेवनी, the printed last part of the name in unit 138, mean?",
            ("A seam, a suture", "Data: sevanī = a seam, suture."),
            [("A bud", "Bud is कोर (unit 135), not सेवनी."),
             ("A mortar", "Mortar is उलूखल (unit 135), not सेवनी."),
             ("A circle", "Circle is मण्डल (unit 140), not सेवनी.")],
            "सेवनी = seam, suture.",
            "सेवनी = seam."),
        match(1, "Match each sure word of unit 138 to its meaning.",
              [["शिरः", "head"], ["कपाल", "bone-plate"], ["सेवनी", "seam, suture"], ["संज्ञाः", "named"]],
              "Head, bone-plate, seam, named.",
              "शिरः, कपाल, सेवनी, संज्ञाः."),
        mcq("extend", 2, "Why does unit 138 carry low confidence in its data?",
            ("Two printed words give no sense", "कति and तून give no sense; both are read by conjecture."),
            [("The whole line is lost in the scan", "The line is printed; two of its words are doubtful."),
             ("It gives an impossible number", "No number is printed in unit 138."),
             ("Its places are all in the limbs", "Its sure place is the head, not the limbs.")],
            "Two conjectures (कटि, तुन्न) make the reading low in confidence.",
            "Low confidence = conjectural readings.",
            teaches="When printed words give no sense the data conjectures a reading and marks the unit low."),
        mcq("discriminate", 3, "Which part of unit 138 gives where the joints are?",
            ("The first word, ending -कपालेषु", "The locative -कपालेषु gives the place: in the kapālas."),
            [("The last word, ending -संज्ञाः", "-संज्ञाः is nominative: it names the joints."),
             ("सेवनी alone, the seam", "सेवनी is part of the name, not the place."),
             ("Neither: no place is printed", "The place is printed: (head) kapālas.")],
            "Place = the locative -कपालेषु.",
            "Locative -एषु = where."),
        multi("apply", 4, "Which statements fit unit 138 and its data?",
              [("Its data confidence is low", "Right: two conjectural readings."),
               ("It gives three joints in the head", "No number is printed in unit 138."),
               ("It names the knee among its places", "The knee is a kora site (unit 135)."),
               ("सेवनी in it means a seam", "Right: data, sevanī = a seam, suture.")],
              [0, 3],
              "Low confidence; सेवनी = seam; no number.",
              "शिरः... कपालेषु ... सेवनीसंज्ञाः."),
        mcq("transfer", 5, "By the pattern of -संज्ञाः ((ones) named ...), what does कमलसंज्ञाः mean in a new example?",
            ("(Ones) named kamala", "X-संज्ञ = having X as name, as ...सेवनीसंज्ञाः."),
            [("(Ones) giving names to kamala", "-संज्ञ here means 'named', not 'naming'."),
             ("(Ones) without the name kamala", "Nothing in -संज्ञ makes a negative."),
             ("(Ones) larger than a kamala", "-संज्ञ says the name, not a size.")],
            "कमलसंज्ञाः = (ones) named kamala.",
            "X-संज्ञ = named X.",
            teaches="A bahuvrīhi ending in -संज्ञ means 'named X': सेवनीसंज्ञाः = (ones) named ...sevanī."),
    ],
}

# ---------------------------------------------------------------- unit 139
AUTHORED["139"] = {
    "title": "हनूभयतो वायसतुंडाः",
    "question": "By unit 139, what joints are on both sides of the jaws?",
    "rule": ("On both sides (उभयतः) of the two jaws (हनू, accusative dual, governed by उभयतः): joints named vāyasatuṇḍa, "
             "'crow-beak' (वायस crow + तुण्ड beak)."),
    "limits": ("Prose, confidence medium. No number is given. The noun 'joints' is unstated. Why the name 'crow-beak' "
               "fits is not said."),
    "explain_hi": ("यह गद्य-पंक्ति कहती है: दोनों जबड़ों के दोनों ओर ‘वायसतुण्ड’ यानी कौए की चोंच नामक सन्धियाँ। "
                   "‘हनू’ द्वितीया द्विवचन है, क्योंकि ‘उभयतः’ (दोनों ओर) द्वितीया लेता है; इसलिए कोई सुधार नहीं। "
                   "सन्धि: हनू + उभयतः → हनूभयतः (ऊ + उ → ऊ); उभयतः + वायस → उभयतो वायस (अः + घोष व्यंजन → ओ)। "
                   "यह नाम क्यों पड़ा, पंक्ति नहीं बताती।"),
    "hook": "जबड़े के दोनों ओर कौए की चोंच।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 139, what are the joints on both sides of the jaws called?",
            ("Vāyasatuṇḍa (crow-beak)", "हनूभयतो वायसतुण्डाः."),
            [("Ulūkhala (mortar)", "Ulūkhala is armpit, groin and tooth-roots (unit 135)."),
             ("Kora (bud)", "Kora is ankle, knee, wrist and elbow (unit 135)."),
             ("Pratara (a kind)", "Pratara is the neck and spine (unit 137).")],
            "Both sides of the jaws: vāyasatuṇḍa.",
            "हनू उभयतः → वायसतुण्ड."),
        match(1, "Match each word of unit 139 to its meaning.",
              [["हनु", "jaw"], ["उभयतः", "on both sides"], ["वायस", "crow"], ["तुण्ड", "beak"]],
              "On both sides of the jaws: crow-beak joints.",
              "हनु, उभयतः, वायस, तुण्ड."),
        mcq("extend", 2, "By the data, why is हनू in the accusative in unit 139?",
            ("उभयतः governs the accusative", "'On both sides of' takes the accusative: हनू उभयतः."),
            [("It is the subject of the line", "The subject is वायसतुण्डाः, the joints named."),
             ("It means 'by the jaws'", "'By' would be the instrumental, हनुभ्याम्."),
             ("The print made an error", "The data: a regular construction, nothing emended.")],
            "उभयतः + accusative: on both sides of the two jaws.",
            "उभयतः takes the accusative.",
            teaches="उभयतः (on both sides of) governs the accusative: हनू उभयतः."),
        mcq("discriminate", 3, "Which split of हनूभयतो is right?",
            ("हनू + उभयतः", "ऊ + उ → ऊ; अः before the voiced व → ओ."),
            [("हनु + भयतः", "That gives हनुभयतः, with a short उ; the print has ऊ."),
             ("हनौ + उभयतः", "औ + उ would give हनावुभयतः."),
             ("हनुः + उभयतः", "उः before a vowel would give हनुरुभयतः.")],
            "हनू (the two jaws) + उभयतः (on both sides).",
            "ऊ + उ → ऊ."),
        multi("apply", 4, "Which statements about उभयतो वायस in unit 139 are right?",
              [("अः before any consonant becomes ओ", "Before unvoiced consonants it does not become ओ."),
               ("The word itself is उभयतः", "Right: ओ comes from sandhi, not from the word."),
               ("व is a voiced consonant", "Right: so अः before it becomes ओ."),
               ("ओ is a dual ending here", "ओ comes from sandhi of अः, not from a case ending.")],
              [1, 2],
              "उभयतः + वायस = उभयतो वायस: अः before the voiced व becomes ओ.",
              "अः + voiced consonant → ओ."),
        mcq("transfer", 5, "By the rule of उभयतो वायस, how are ततः + गच्छति (then he goes) joined?",
            ("ततो गच्छति", "अः before the voiced ग becomes ओ, as उभयतो वायस."),
            [("ततर्गच्छति", "र् comes from a visarga after vowels other than अ and आ."),
             ("तता गच्छति", "No such change: अः before a voiced consonant gives ओ."),
             ("ततः गच्छति", "Before a voiced consonant the visarga after अ does not stay.")],
            "ततः + गच्छति = ततो गच्छति.",
            "अः + voiced consonant → ओ.",
            teaches="A visarga after अ becomes ओ before a voiced consonant: उभयतः + वायस → उभयतो वायस."),
    ],
}

# ---------------------------------------------------------------- unit 140
AUTHORED["140"] = {
    "title": "कंठनेत्रहृदय... मंडलसंज्ञाः",
    "question": "By unit 140, where are the joints named maṇḍala (circle)?",
    "rule": ("Maṇḍala (circle) joints are in the throat (कण्ठ), eyes (नेत्र), heart, liver, kloma (identity disputed) and "
             "channels (नाडी)."),
    "limits": ("Prose, confidence medium. Read as a dvandva of six; it may also read 'in the channels of throat, eyes, "
               "heart, liver and kloma' (data): no question on the parse. kloma's identity is disputed: no question on it."),
    "explain_hi": ("यह गद्य-पंक्ति एक और सन्धि-प्रकार बताती है: ‘मण्डल’ यानी गोल घेरा नामक। "
                   "स्थान: कण्ठ (गला), नेत्र (आँखें), हृदय, यकृत (जिगर), क्लोम (पहचान विवादित) और नाड़ियाँ। "
                   "इसे छह सदस्यों का द्वन्द्व पढ़ा गया; दूसरा पाठ ‘इन अंगों की नाड़ियों में’ भी सम्भव है (तुलना करें इकाई १३१)। "
                   "‘नाडीषु’ में ई के बाद सप्तमी बहुवचन का स् ष् बना है।"),
    "hook": "गले, आँख, हृदय की गोल सन्धियाँ: मण्डल।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 140, what name do the joints of throat, eyes and heart get?",
            ("Maṇḍala (circle)", "...नाडीषु मण्डलसंज्ञाः."),
            [("Pratara (a kind)", "Pratara is the neck and spine (unit 137)."),
             ("Sāmudga (casket)", "Sāmudga is aṃsapīṭha, anus and so on (unit 136)."),
             ("Vāyasatuṇḍa (beak)", "Vāyasatuṇḍa is both sides of the jaws (unit 139).")],
            "Throat, eyes, heart, liver, kloma, channels: maṇḍala.",
            "... मण्डलसंज्ञाः."),
        order(1, "Put the printed places of unit 140 in the line's order.",
              ["कंठ", "नेत्र", "हृदय", "यकृत्", "क्लोम", "नाडीषु"],
              "Throat, eyes, heart, liver, kloma, channels: maṇḍala joints.",
              "कंठ → नेत्र → हृदय → यकृत् → क्लोम → नाडीषु."),
        match(2, "Match each word of unit 140 to its meaning.",
              [["मण्डल", "circle"], ["कण्ठ", "throat"], ["नेत्र", "eye"], ["हृदय", "heart"], ["यकृत्", "liver"]],
              "Circle joints in throat, eyes, heart, liver and the rest.",
              "मण्डल, कण्ठ, नेत्र, हृदय, यकृत्.", role="extend",
              teaches="मण्डलसंज्ञाः = (ones) named maṇḍala, circle."),
        mcq("discriminate", 3, "Which place is NOT a maṇḍala site in unit 140?",
            ("The ear (श्रोत्र)", "The ear's joints are not in unit 140's list."),
            [("The eye (नेत्र)", "नेत्र is a maṇḍala site in unit 140."),
             ("The heart (हृदय)", "हृदय is a maṇḍala site in unit 140."),
             ("The liver (यकृत्)", "यकृत् is a maṇḍala site in unit 140.")],
            "Throat, eyes, heart, liver, kloma, channels; not the ear.",
            "कण्ठ, नेत्र, हृदय, यकृत्, क्लोम, नाडी → मण्डल."),
        multi("apply", 4, "Which of these places does unit 140 name in its maṇḍala list?",
              [("The wrist (मणिबन्ध)", "The wrist is kora (unit 135)."),
               ("The throat (कण्ठ)", "Right: कण्ठ is first in the list."),
               ("The spine (पृष्ठवंश)", "The spine is pratara (unit 137)."),
               ("The eye (नेत्र)", "Right: नेत्र is named."),
               ("The heart (हृदय)", "Right: हृदय is named.")],
              [1, 3, 4],
              "Throat, eye, heart are maṇḍala; wrist is kora, spine pratara.",
              "कण्ठनेत्रहृदय... मण्डलसंज्ञाः."),
        mcq("transfer", 5, "By the pattern of नाडीषु (in the channels), which form of नदी (river) means in the rivers, a new example?",
            ("नदीषु", "After ई the स् of -सु becomes ष्, as नाडी → नाडीषु."),
            [("नदीसु", "After ई the स् of -सु turns into ष्."),
             ("नद्याम्", "नद्याम् is the locative singular, 'in the river'."),
             ("नदीः", "नदीः is the accusative plural, not 'in'.")],
            "नदी → नदीषु, like नाडी → नाडीषु.",
            "ई-stem: locative plural -ईषु.",
            teaches="Locative plural -सु becomes -षु after ई: नाडी → नाडीषु."),
    ],
}


# ===================================================================== NOTES_HI
NOTES_HI = {
    "128": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। छपा एक शब्द ‘अष्टावुरसि’ = अष्टौ उरसि। गिनी गई वस्तु (सम्भवतः अस्थि-सन्धियाँ, इकाई ११९ से) "
            "और क्रिया छपी नहीं। डेटा की धड़-जाँच: ३ (इकाई १२५, कटिकपाल अनुमानित पाठ) + २४ (इकाई १२६) + तद्वत् (इकाई १२७, सम्भवतः २४) + ८ = ५९, इकाई १२१ से मेल। "
            "सन्धि जाँची: अष्टौ + उरसि → अष्टावुरसि (औ + स्वर → आव्)।"),
    "129": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं; डेटा में कोई टिप्पणी नहीं। छपा ‘ग्रीवायां’ = ग्रीवायाम् (अन्त का म् अनुस्वार से लिखा)। "
            "गिनी गई वस्तु और क्रिया छपी नहीं। इकाई १३४ की डेटा-जाँच ऊपर वाले भाग की गिनती यहीं से (गर्दन ८) आरम्भ करती है।"),
    "130": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। कण्ठनाडी = सम्भवतः श्वासनली (सम्भावित); दूसरा विकल्प अन्ननली। छपाई में ‘त्रयःकंठनाड्यां’ "
            "जुड़ा है = त्रयः कण्ठनाड्याम्। सन्धि जाँची: अघोष क से पहले विसर्ग बना रहा; नाडी + आम् → नाड्याम् (ई + आ → या)।"),
    "131": ("गद्य; विश्वास मध्यम। पाठ-चिह्न (सम्भावित): छपा ‘निबद्धा’ (स्त्री. एकवचन) बहुवचन ‘अष्टादश’ से मेल नहीं खाता; छूटे विसर्ग से "
            "‘निबद्धाः’ पढ़ा गया; इस रूप पर कोई प्रश्न नहीं। अन्तिम समास चार सदस्यों का द्वन्द्व पढ़ा गया; विकल्प: ‘हृदय, यकृत, क्लोम की नाड़ियों में’। "
            "हृदय, यकृत मानक; क्लोम की पहचान विवादित (फेफड़ा, अग्न्याशय आदि सुझाए गए)। सन्धि जाँची: यकृत् + क्लोम → यकृत्क्लोम "
            "(अघोष क से पहले त् बना रहा)।"),
    "132": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। छपा ‘दंत’ = दन्त (अनुस्वार = वर्ग का नासिक्य)। सन्धि जाँची: द्वात्रिंशत् + दन्त → "
            "द्वात्रिंशद्दन्त (घोष द से पहले त् → द्)। गिनी गई वस्तु और क्रिया छपी नहीं।"),
    "133": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। काकल की पहचान विवादित (कौआ यानी उपजिह्वा या कण्ठ का उभार सुझाए गए); इस पर कोई प्रश्न नहीं। "
            "छपा ‘मूर्द्धसु’ (र के बाद दोहरा ध) लिखावट का भेद है, मूर्धसु माना गया। मूर्धन् = सिर या शिखर। सन्धि जाँची: एक + एकः → एकैकः (अ + ए → ऐ)।"),
    "134": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं; दो छपी पंक्तियाँ (०२.०५.१४४-१४५)। गण्ड = गाल, शंख = कनपटी, वर्त्म = पलक (मानक)। "
            "समास के अन्त का ‘सन्धि’ छहों सदस्यों पर लगता है; द्वौ द्वौ = दो-दो। डेटा की जाँच: ८ + ३ + १८ + ३२ + ३ + १२ + २ + ५ = ८३, "
            "इकाई १२२ के छपे ८० से भिन्न (वहाँ का पाठ-चिह्न देखें); कौन-सी संख्या मूल है, यह खुला है। सन्धि जाँची: द्वौ + उपरिष्टात् → "
            "द्वावुपरिष्टात् (औ + स्वर → आव्); उपरिष्टात् + भ्रुवोः → उपरिष्टाद्भ्रुवोः (घोष भ से पहले त् → द्)।"),
    "135": ("गद्य; विश्वास मध्यम; दो छपी पंक्तियाँ (०२.०५.१४६-१४७)। पाठ-चिह्न (सम्भावित): छपा ‘मेंगुलि’ कोई शब्द नहीं; अनुमानित पाठ ‘अङ्गुलि’ "
            "(उँगली या पैर की उँगली); इस पर कोई प्रश्न नहीं। मणिबन्ध = कलाई, कूर्पर = कुहनी, कक्षा = काँख (मानक); कोर = कली, उलूखल = ओखली। "
            "‘(ones)’ = अनकहा संज्ञा-शब्द, प्रसंग से अस्थि-सन्धियाँ (इकाई १४२)। सन्धि जाँची: मूलेषु + उलूखल → मूलेषूलूखल (उ + उ → ऊ)।"),
    "136": ("गद्य; विश्वास मध्यम। पाठ-चिह्न (सम्भावित): छपा ‘तितंब’ कोई शब्द नहीं; अनुमानित पाठ ‘नितम्ब’ (नितम्ब, कूल्हा); छपा ‘गुद्भग’ में "
            "सम्भवतः गुद का अ छूटा (अर्थ वही); नितम्ब पर कोई प्रश्न नहीं। अंसपीठ = सम्भवतः कन्धे के फलक का क्षेत्र (सम्भावित); गुद = गुदा, "
            "भग = स्त्री-जननांग (मानक)। सामुद्ग ← समुद्ग (डिब्बी, ढक्कन वाला पात्र)। संज्ञा-शब्द अनकहा।"),
    "137": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। प्रतर एक सन्धि-प्रकार का नाम है; डेटा ने शब्दार्थ नहीं दिया। छपाई में "
            "‘ग्रीवापृष्ठवंशयोःप्रतराः’ जुड़ा है; अघोष प से पहले विसर्ग बना रहा। ग्रीवापृष्ठवंशयोः = दो सदस्यों का द्वन्द्व, सप्तमी द्विवचन।"),
    "138": ("गद्य; विश्वास निम्न। दो पाठ-चिह्न (सम्भावित): छपा ‘कति’ (कितने) अर्थ नहीं देता, अनुमानित ‘कटि’ (कमर; इकाई १२५ में भी ‘कति’ ही छपा); "
            "छपा ‘तून’ ज्ञात शब्द नहीं, ज्ञात नाम ‘तुन्नसेवनी’। दोनों अनुमानों पर कोई प्रश्न नहीं। सेवनी = सीवन, सिलाई। संज्ञा-शब्द अनकहा। "
            "सन्धि: शिरस् + क... → शिरःक... (अघोष क से पहले स् → विसर्ग)।"),
    "139": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। हनू = द्वितीया द्विवचन, ‘उभयतः’ (दोनों ओर) के कारण; नियमित रचना, कोई सुधार नहीं। "
            "सन्धि जाँची: हनू + उभयतः → हनूभयतः (ऊ + उ → ऊ); उभयतः + वायस → उभयतो वायस (अः + घोष व्यंजन → ओ); छपा ‘तुंड’ = तुण्ड।"),
    "140": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। छह सदस्यों का सीधा द्वन्द्व पढ़ा गया; विकल्प: ‘कण्ठ, नेत्र, हृदय, यकृत, क्लोम की नाड़ियों में’ "
            "(तुलना इकाई १३१); इस पर कोई प्रश्न नहीं। क्लोम की पहचान विवादित। छपा ‘कंठ’, ‘मंडल’ = कण्ठ, मण्डल। "
            "नाडीषु: ई के बाद -सु का स् → ष्।"),
}


# ===================================================================== AIDS
AIDS = {
    "128": {
        "chain": {"steps": ["कटिकपालों में ३ (इकाई १२५, अनुमानित पाठ; छपा कति)", "रीढ़ में २४ (इकाई १२६)", "पार्श्वों में तद्वत्, सम्भवतः २४ (इकाई १२७)",
                            "छाती में ८ (इकाई १२८)", "योग ५९ = इकाई १२१ का धड़-योग"]},
        "chunks": "अष्टाव् | उरसि",
        "sandhi": "औ + स्वर → आव्: अष्टौ + उरसि → अष्टावुरसि।",
    },
    "129": {
        "chunks": "अष्टौ | ग्रीवायां",
        "frame": "संख्या: अष्टौ (आठ) → स्थान: ग्रीवायाम् (गर्दन में) → वस्तु और क्रिया: छपी नहीं।",
        "anchors": "छाती में आठ (इकाई १२८), गर्दन में भी आठ (इकाई १२९): दो लगातार ‘अष्टौ’। (मेरी याद-पद्धति)",
    },
    "130": {
        "chunks": "त्रयः | कंठनाड्यां",
        "sandhi": "अघोष क से पहले विसर्ग बना रहता है: त्रयः + कण्ठ... → त्रयः कण्ठ...",
        "frame": "संख्या: त्रयः (तीन) → स्थान: कण्ठनाड्याम् (गले की नली में, सम्भवतः श्वासनली)।",
    },
    "131": {
        "diagram": {"groups": [
            {"label": "संख्या और बन्धन", "items": ["अष्टादश (अठारह)", "कण्ठनाड़ी से बँधी"]},
            {"label": "स्थान (क्रम से)", "items": ["१ हृदय", "२ यकृत", "३ क्लोम (पहचान विवादित)", "४ नाड़ियाँ"]}]},
        "chunks": "अष्टादश | कंठनाडीनिबद्धा | हृदययकृत्क्लोमनाडीषु",
        "letters": "स्थानों के पहले अक्षर क्रम से: हृ-य-क्लो-ना (हृदय, यकृत, क्लोम, नाड़ी)। (मेरी याद-पद्धति)",
    },
    "132": {
        "chunks": "द्वात्रिंशद् | दंतमूलेषु",
        "sandhi": "घोष द से पहले त् → द्: द्वात्रिंशत् + दन्त → द्वात्रिंशद्दन्त।",
        "pegs": "बत्तीस दाँत, हर जड़ पर एक जोड़ सोचें: बत्तीस। (मेरी याद-पद्धति, पंक्ति ‘एक-एक’ नहीं कहती)",
    },
    "133": {
        "chunks": "एकैकः | काकलनासामूर्द्धसु",
        "sandhi": "अ + ए → ऐ: एक + एकः → एकैकः।",
        "frame": "संख्या: एकैकः (एक-एक) → स्थान: काकल (पहचान विवादित), नासा (नाक), मूर्धा (सिर)।",
    },
    "134": {
        "diagram": {"groups": [
            {"label": "पहली पंक्ति: दो-दो, इनकी सन्धियों में", "items": ["गण्ड (गाल)", "कर्ण (कान)", "शंख (कनपटी)",
                                                                       "वर्त्म (पलक)", "नेत्र (आँख)", "हनु (जबड़ा)"]},
            {"label": "दूसरी पंक्ति", "items": ["भौंहों के ऊपर दो", "सिर के कपालों में पाँच"]}]},
        "chain": {"steps": ["गर्दन ८", "कण्ठनाड़ी ३", "कण्ठनाड़ी से बँधी १८", "दाँत-जड़ें ३२", "काकल, नाक, सिर ३",
                            "चेहरे के छह जोड़ १२", "भौंहों के ऊपर २, कपाल ५", "योग ८३ (इकाई १२२ में छपा ८०)"]},
        "chunks": "द्वौ द्वौ | गंडकर्णशंखवर्त्मनेत्रहनुसंधिषु | द्वावुपरिष्टाद्भ्रुवोः | पंच | शिरःकपालेषु",
        "sandhi": "औ + स्वर → आव्: द्वौ + उपरिष्टात् → द्वावुपरिष्टात् · घोष भ से पहले त् → द्: उपरिष्टात् + भ्रुवोः → उपरिष्टाद्भ्रुवोः।",
    },
    "135": {
        "diagram": {"groups": [
            {"label": "कोर (कली) नामक", "items": ["मेंगुलि (छपा; अनुमानित पाठ अङ्गुलि)", "गुल्फ (टखना)", "जानु (घुटना)",
                                                 "मणिबन्ध (कलाई)", "कूर्पर (कुहनी)"]},
            {"label": "उलूखल (ओखली) नामक", "items": ["कक्षा (काँख)", "वंक्षण (जाँघ का जोड़)", "दन्तमूल (दाँत की जड़)"]}]},
        "contrast": "कोर = कली (हाथ-पैर के जोड़) बनाम उलूखल = ओखली (काँख, वंक्षण, दाँत-जड़): दोनों इसी इकाई में।",
        "chunks": "मेंगुलिगुल्फजानुमणिबंधकूर्परेषु | कोरसंज्ञाः | कक्षावंक्षणदंतमूलेषूलूखलसंज्ञाः",
        "sandhi": "उ + उ → ऊ: मूलेषु + उलूखल → मूलेषूलूखल।",
    },
    "136": {
        "diagram": {"groups": [
            {"label": "सामुद्ग (डिब्बी) नामक", "items": ["अंसपीठ (सम्भवतः कन्धे का फलक)", "गुद (गुदा)",
                                                       "भग (स्त्री-जननांग)", "नितम्ब (अनुमानित पाठ; छपा तितंब)"]}]},
        "chunks": "अंसपीठगुद्भगतितंबेषु | सामुद्गाः",
        "pegs": "ढक्कन वाली डिब्बी की तरह बन्द होता जोड़ सोचें: सामुद्ग। (मेरी याद-पद्धति)",
    },
    "137": {
        "chunks": "ग्रीवापृष्ठवंशयोः | प्रतराः",
        "frame": "स्थान: ग्रीवा + पृष्ठवंश (द्विवचन, दो स्थान) → नाम: प्रतर।",
        "sandhi": "अघोष प से पहले विसर्ग बना रहता है: पृष्ठवंशयोः + प्रतराः।",
    },
    "138": {
        "chunks": "शिरःकतिकपालेषु | तूनसेवनीसंज्ञाः",
        "frame": "पक्का: शिरः (सिर), कपाल, सेवनी (सीवन), संज्ञाः (नामक) · अनुमानित: कति → कटि, तून → तुन्न।",
        "pegs": "खोपड़ी के कपाल कपड़े की सिलाई जैसे जुड़े सोचें: सेवनी। (मेरी याद-पद्धति)",
    },
    "139": {
        "chunks": "हनूभयतो | वायसतुंडाः",
        "sandhi": "ऊ + उ → ऊ: हनू + उभयतः → हनूभयतः · अः + घोष व्यंजन → ओ: उभयतः + वायस → उभयतो वायस।",
        "pegs": "जबड़े के दोनों ओर खुलती-बन्द होती कौए की चोंच सोचें। (मेरी याद-पद्धति)",
    },
    "140": {
        "diagram": {"groups": [
            {"label": "मण्डल (गोल घेरा) नामक, क्रम से", "items": ["१ कण्ठ", "२ नेत्र", "३ हृदय", "४ यकृत",
                                                              "५ क्लोम (पहचान विवादित)", "६ नाड़ियाँ"]}]},
        "chunks": "कंठनेत्रहृदययकृत्क्लोमनाडीषु | मंडलसंज्ञाः",
        "letters": "स्थानों के पहले अक्षर क्रम से: क-ने-हृ-य-क्लो-ना। (मेरी याद-पद्धति)",
    },
}


# ===================================================================== IMAGE_SPECS
IMAGE_SPECS = {
    ("128", "chain"): {
        "file": "sh5-dhad-sandhi-128.svg",
        "alt": ("Chain of the trunk joint count ending in unit 128: hip kapālas (conjectural reading) 3 (unit 125); spine 24 (unit 126); flanks "
                "likewise, presumably 24 (unit 127); chest 8 (unit 128); total 59, the trunk total of unit 121."),
        "type": "chain",
        "title": "इकाई १२८: धड़ की सन्धियाँ",
        "steps": ["कटिकपाल (अनुमानित) ३ (इकाई १२५)", "रीढ़ २४ (इकाई १२६)", "पार्श्व तद्वत्, सम्भवतः २४", "छाती ८ (इकाई १२८)",
                  "योग ५९ (इकाई १२१)"],
    },
    ("131", "diagram"): {
        "file": "sh5-kanthanadi-nibaddha-131.svg",
        "alt": ("Two columns of unit 131: number and binding (eighteen, bound to the kaṇṭhanāḍī); places in line order "
                "(heart, liver, kloma of disputed identity, channels)."),
        "type": "split",
        "title": "इकाई १३१: कण्ठनाड़ी से बँधी अठारह",
        "cols": [["संख्या और बन्धन", ["अष्टादश (अठारह)", "कण्ठनाड़ी से बँधी"]],
                 ["स्थान (क्रम से)", ["१ हृदय", "२ यकृत", "३ क्लोम (विवादित)", "४ नाड़ियाँ"]]],
    },
    ("134", "diagram"): {
        "file": "sh5-mukha-sandhi-134.svg",
        "alt": ("Table of unit 134 in line order: two each in the joints of cheek, ear, temple, eyelid, eye and jaw; two "
                "above the eyebrows; five in the head kapālas."),
        "type": "table",
        "title": "इकाई १३४: चेहरा और सिर",
        "heads": ["स्थान (क्रम से)", "संख्या"],
        "rows": [["गण्ड (गाल)", "दो"], ["कर्ण (कान)", "दो"], ["शंख (कनपटी)", "दो"], ["वर्त्म (पलक)", "दो"],
                 ["नेत्र (आँख)", "दो"], ["हनु (जबड़ा)", "दो"], ["भौंहों के ऊपर", "दो"], ["सिर के कपाल", "पाँच"]],
    },
    ("134", "chain"): {
        "file": "sh5-urdhva-sandhi-134.svg",
        "alt": ("Table of the data's check of the upper joint count, units 129-134: neck 8; kaṇṭhanāḍī 3; bound to it 18; "
                "tooth-roots 32; kākala, nose, head 3; six face joints 12; above eyebrows 2; head kapālas 5; sum 83, "
                "against the printed 80 of unit 122."),
        "type": "table",
        "title": "ऊपर की सन्धियाँ: डेटा की जाँच",
        "heads": ["स्थान (इकाई)", "संख्या"],
        "rows": [["गर्दन (१२९)", "८"], ["कण्ठनाड़ी (१३०)", "३"], ["उससे बँधी (१३१)", "१८"], ["दाँत-जड़ें (१३२)", "३२"],
                 ["काकल, नाक, सिर (१३३)", "३"], ["चेहरे के छह जोड़ (१३४)", "१२"], ["भौंहों के ऊपर (१३४)", "२"],
                 ["सिर के कपाल (१३४)", "५"], ["योग (इकाई १२२ में छपा ८०)", "८३"]],
    },
    ("135", "diagram"): {
        "file": "sh5-kora-ulukhala-135.svg",
        "alt": ("Two columns of unit 135: kora (bud) joints in the printed meṃguli (conjectured as fingers or toes, aṅguli), ankle, knee, wrist, "
                "elbow; ulūkhala (mortar) joints in armpit, groin, tooth-roots."),
        "type": "split",
        "title": "इकाई १३५: कोर और उलूखल",
        "cols": [["कोर (कली)", ["मेंगुलि (छपा; अनुमानित अङ्गुलि)", "गुल्फ (टखना)", "जानु (घुटना)", "मणिबन्ध (कलाई)", "कूर्पर (कुहनी)"]],
                 ["उलूखल (ओखली)", ["कक्षा (काँख)", "वंक्षण (जाँघ का जोड़)", "दन्तमूल (दाँत-जड़)"]]],
    },
    ("136", "diagram"): {
        "file": "sh5-samudga-136.svg",
        "alt": ("Flowchart of unit 136: sāmudga (casket) joints, numbered in line order: 1 aṃsapīṭha (probably the "
                "shoulder-blade region), 2 anus, 3 bhaga, 4 printed titamba (conjectured as nitamba, hips)."),
        "type": "mermaid",
        "code": ("flowchart LR\n"
                 "  A[\"सामुद्ग (डिब्बी) नामक\"] --> B[\"१ अंसपीठ (सम्भावित)\"]\n"
                 "  A --> C[\"२ गुद\"]\n"
                 "  A --> D[\"३ भग\"]\n"
                 "  A --> E[\"४ तितंब (छपा; अनुमानित नितम्ब)\"]\n"),
    },
    ("140", "diagram"): {
        "file": "sh5-mandala-140.svg",
        "alt": ("Flowchart of unit 140: maṇḍala (circle) joints, numbered in line order: 1 throat, 2 eyes, 3 heart, "
                "4 liver, 5 kloma (identity disputed), 6 channels."),
        "type": "mermaid",
        "code": ("flowchart LR\n"
                 "  A[\"मण्डल (गोल घेरा) नामक\"] --> B[\"१ कण्ठ\"]\n"
                 "  A --> C[\"२ नेत्र\"]\n"
                 "  A --> D[\"३ हृदय\"]\n"
                 "  A --> E[\"४ यकृत\"]\n"
                 "  A --> F[\"५ क्लोम (विवादित)\"]\n"
                 "  A --> G[\"६ नाड़ियाँ\"]\n"),
    },
}
