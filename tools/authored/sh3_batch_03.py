from helpers import mcq, match, order, fill, multi, accepts


AUTHORED = {}

# ---------------------------------------------------------------- unit 27
AUTHORED["27"] = {
    "title": "तैलेनानुवासयेदनुलोमनाय वायोः",
    "question": "By unit 27, with what oil is an anuvāsana given, and for what purpose?",
    "rule": ("One should give an anuvāsana (oil enema) with oil cooked with sweet medicines beginning with madhuka "
             "(probably licorice), for the anulomana (downward movement) of vāyu, the wind (Vāta)."),
    "limits": ("Low confidence. The badly printed first word ('for cleansing the old stool') is a conjecture; no "
               "question rests on it. The other sweet medicines are not named; madhuka is probably licorice. No month, "
               "dose or timing is printed. Prose."),
    "explain_hi": ("यह गद्य-पंक्ति अनुवासन (तेल की बस्ति) का विधान करती है: मधुक (सम्भवतः मुलेठी) आदि मधुर औषधों से पकाए तेल से "
                   "अनुवासन दे, वायु के अनुलोमन (नीचे की ओर, ठीक दिशा में चलाने) के लिए। "
                   "पहला शब्द छपाई में बिगड़ा है; ‘पुराने मल की शुद्धि के लिए’ केवल अनुमानित पाठ है, इसलिए उस पर प्रश्न नहीं। "
                   "‘मधुकादि’ में ‘आदि’ से बाकी मधुर औषध खुले छोड़े गए हैं, उनके नाम नहीं दिए। "
                   "‘अनुलोमनाय’ चतुर्थी है: प्रयोजन बताती है (‘के लिए’)। "
                   "कर्ता (वैद्य) लिखा नहीं, समझा जाता है।"),
    "hook": "मधुर औषधों का तेल → अनुवासन → वायु अनुलोम।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 27, which kind of enema is given with the cooked oil?",
            ("An anuvāsana, the oil enema", "तैलेनानुवासयेत्: one should give an anuvāsana with the oil."),
            [("An āsthāpana, the decoction enema", "The āsthāpana with jujube water is unit 26; here the verb is अनुवासयेत्."),
             ("A picu, a cotton swab in the yoni", "The picu comes in unit 31, in the ninth (month)."),
             ("A daily bath with a cooled decoction", "The daily bath is unit 36.")],
            "The oil cooked with sweet medicines is given as an anuvāsana.",
            "तैलेन अनुवासयेत् = should give an oil enema with the oil."),
        order(1, "Put these words of unit 27 in the line's order.",
              ["मधुकादिमधुरौषधसिद्धेन", "च", "तैलेन", "अनुवासयेत्", "अनुलोमनाय", "वायोः"],
              "With oil cooked with madhuka and the other sweet medicines, one should give an anuvāsana, for the "
              "anulomana of vāyu. The damaged first word is left out.",
              "मधुकादि… सिद्धेन → च → तैलेन → अनुवासयेत् → अनुलोमनाय → वायोः."),
        match(2, "Match each word of unit 27 to its meaning.",
              [["मधुक", "madhuka (probably licorice)"], ["मधुर", "sweet"], ["औषध", "medicine"],
               ["सिद्ध", "cooked"], ["अनुलोमन", "moving downward, setting in order"]],
              "These words name the oil and the purpose of the enema.",
              "मधुक, मधुर, औषध, सिद्ध, अनुलोमन.", role="extend",
              teaches="-आदि = beginning with: madhuka heads a group of sweet medicines that the line does not name."),
        mcq("discriminate", 3, "Which split of तैलेनानुवासयेत् is right?",
            ("तैलेन + अनुवासयेत्", "अ + अ → आ: तैलेन + अनुवासयेत् = तैलेनानुवासयेत्."),
            [("तैलेना + नुवासयेत्", "नुवासयेत् is not a word; the verb is अनुवासयेत्."),
             ("तैलेनः + अनुवासयेत्", "अः before अ would give तैलेनोऽनुवासयेत्."),
             ("तैलेनम् + अनुवासयेत्", "A final म् would give तैलेनमनुवासयेत्.")],
            "तैलेन (with oil) + अनुवासयेत् (should give an oil enema): अ + अ → आ.",
            "अ + अ → आ."),
        mcq("apply", 4, "In unit 27, what purpose does the dative अनुलोमनाय वायोः state?",
            ("The downward movement of the wind", "अनुलोमनाय वायोः: for the anulomana of vāyu."),
            [("The oiling of the embryo's passage", "That purpose belongs to the picu of unit 31."),
             ("The softening of belly and back", "Softening is the result stated in unit 32."),
             ("A cooling of the woman's skin", "No cooling of the skin is named in unit 27.")],
            "The sure purpose of the line: to make vāyu move downward.",
            "अनुलोमनाय वायोः = for the downward movement of the wind."),
        mcq("transfer", 5, "By the dative of अनुलोमनाय (for anulomana), what does रक्षणाय mean?",
            ("For protection", "-आय is the dative singular of an अ-stem: for, for the purpose of."),
            [("By protection", "By protection would be the instrumental रक्षणेन."),
             ("From protection", "From protection would be the ablative रक्षणात्."),
             ("Of protection", "Of protection would be the genitive रक्षणस्य.")],
            "रक्षण + आय = for protection, like अनुलोमन + आय = for anulomana.",
            "-आय (dative) = for, for the purpose of.",
            teaches="The dative of an अ-stem ends in -आय and states a purpose: अनुलोमनाय = for the downward movement."),
    ],
}

# ---------------------------------------------------------------- unit 28
AUTHORED["28"] = {
    "title": "अनुलोमे हिमारुते सुखमनुपद्रवा प्रसूते",
    "question": "By unit 28, why does the downward wind matter, and how is the enema given to the pregnant woman?",
    "rule": ("For (हि) when the wind (मारुत) moves downward (अनुलोम), she gives birth easily (सुखम्) and free of "
             "complications (अनुपद्रवा). The pregnant woman, face down (न्युब्जा), is given an āsthāpana or an anuvāsana."),
    "limits": ("Two printed lines joined. हिमारुते is printed as one word: हि + मारुते. The posture न्युब्ज (face down) "
               "is not described further, nor when to choose which enema (वा = or). The data's note takes the line as "
               "continuing the enema rules of units 26-27."),
    "explain_hi": ("पहला वाक्य कारण देता है: क्योंकि (हि) वायु के अनुलोम होने पर वह सुख से और उपद्रव (जटिलता) से रहित प्रसव करती है। "
                   "‘अनुलोमे मारुते’ सप्तमी में है: ‘वायु के अनुलोम होने पर’। "
                   "दूसरा वाक्य विधि है: गर्भिणी को न्युब्जा (औंधी, आगे झुकी) स्थिति में आस्थापन या अनुवासन दे। "
                   "आसन का पूरा वर्णन नहीं है, और कब कौन-सी बस्ति, यह भी नहीं कहा। "
                   "‘अनुपद्रवा’ में अन् (नहीं) + उपद्रवा है: स्वर से पहले निषेध ‘अन्’ बनता है।"),
    "hook": "वायु अनुलोम → सुख-प्रसव; औंधी गर्भिणी को बस्ति।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 28, how does she give birth when the wind moves downward?",
            ("Easily and free of complications", "सुखमनुपद्रवा प्रसूते: easily, without complications."),
            [("Slowly, after a long labour", "सुखम् means easily; no long labour is named."),
             ("Early, before the due time", "No time of birth is named in unit 28."),
             ("With pain, though safely", "No pain is named; सुखम् means easily.")],
            "With the wind moving downward, the birth is easy and free of complications.",
            "अनुलोमे हि मारुते सुखम् अनुपद्रवा प्रसूते."),
        order(1, "Put the words of the first sentence of unit 28 in the line's order.",
              ["अनुलोमे", "हि", "मारुते", "सुखम्", "अनुपद्रवा", "प्रसूते"],
              "For when the wind is downward, easily, free of complications, she gives birth.",
              "अनुलोमे → हि → मारुते → सुखम् → अनुपद्रवा → प्रसूते."),
        match(2, "Match each word of unit 28 to its meaning.",
              [["अनुलोम", "moving downward"], ["मारुत", "wind"], ["उपद्रव", "complication"],
               ["आस्थापयेत्", "should give a decoction enema"], ["अनुवासयेत्", "should give an oil enema"]],
              "The condition, the result, and the two enemas of the second sentence.",
              "अनुलोम, मारुत, उपद्रव, आस्थापयेत्, अनुवासयेत्.", role="extend",
              teaches="Before a vowel the negative prefix is अन्-: अन् + उपद्रवा = अनुपद्रवा, without complications."),
        mcq("discriminate", 3, "Which split of सुखमनुपद्रवा is right?",
            ("सुखम् + अनुपद्रवा", "A final म् before a vowel joins to it: सुखमनुपद्रवा."),
            [("सुखः + अनुपद्रवा", "अः before अ would give सुखोऽनुपद्रवा."),
             ("सुख + मनुपद्रवा", "मनुपद्रवा is not a word."),
             ("सुखमनु + पद्रवा", "पद्रवा is not a word; the word is अनुपद्रवा.")],
            "सुखम् (easily) + अनुपद्रवा (free of complications).",
            "Final म् + vowel → म joined to the vowel."),
        mcq("apply", 4, "By unit 28, how is the pregnant woman placed for the enema?",
            ("Face down, bent over (न्युब्जा)", "गर्भिणीं तु न्युब्जाम्: face down, prone."),
            [("Lying on her back, face up", "न्युब्ज is face down, the opposite."),
             ("Sitting upright on a seat", "No seat is named; the word is न्युब्जा."),
             ("Lying on her left side", "No side is named; the word is न्युब्जा.")],
            "न्युब्जा: the woman is face down for the enema; the posture is not described further.",
            "न्युब्जाम् आस्थापयेत् अनुवासयेद्वा."),
        mcq("transfer", 5, "By the rule of अनुपद्रवा (अन् + उपद्रवा), how is the negative of आदि (beginning) formed?",
            ("अनादि", "Before a vowel the negative is अन्-: अन् + आदि = अनादि."),
            [("अआदि", "अ- is the negative only before a consonant."),
             ("अनोदि", "No ओ arises; अन् simply joins the vowel."),
             ("अन्यादि", "That is अन्य + आदि, 'the other and so on', not a negative.")],
            "अन् + आदि = अनादि, like अन् + उपद्रवा = अनुपद्रवा.",
            "Negative before a vowel → अन्-.",
            teaches="The negative prefix is अ- before a consonant and अन्- before a vowel: अन् + उपद्रवा → अनुपद्रवा."),
    ],
}

# ---------------------------------------------------------------- unit 29
AUTHORED["29"] = {
    "title": "तथा ऽस्या विवृतमार्गतया",
    "question": "By unit 29, why does the medicine enter properly?",
    "rule": ("In that way (तथा), because her passage is open (विवृतमार्गतया), the medicine (औषध) enters properly "
             "(सम्यक् अनुप्रविशति)."),
    "limits": ("Printed ऽस्या is taken as अस्याः (of her), the visarga lost in print: a suggested reading, and no question "
               "rests on its case. The passage (मार्ग) is not defined. तथा points back to the posture of unit 28 by "
               "context; the line does not name it."),
    "explain_hi": ("यह पंक्ति पिछली विधि का कारण बताती है: उस प्रकार (तथा) उसके मार्ग के खुले होने से औषध ठीक से भीतर प्रवेश करता है। "
                   "‘विवृतमार्गतया’ में ‘-ता’ भाववाचक है और तृतीया ‘कारण’ बताती है: मार्ग खुला होने के कारण। "
                   "छपा ‘ऽस्या’ सम्भवतः ‘अस्याः’ (उसका) है, विसर्ग छपाई में छूटा; इस पर प्रश्न नहीं। "
                   "‘मार्ग’ की परिभाषा नहीं दी गई। "
                   "सन्धि: सम्यक् + औषधम् → सम्यगौषधम् (क् → ग् स्वर से पहले)।"),
    "hook": "मार्ग खुला → औषध ठीक से भीतर।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 29, what follows from her passage being open?",
            ("The medicine enters properly", "सम्यगौषधमनुप्रविशति: the medicine enters properly."),
            [("The wind becomes anuloma", "That is stated in unit 33."),
             ("Urine and stool become natural", "That is stated in unit 34."),
             ("Belly and back become soft", "That is stated in unit 32.")],
            "Because the passage is open, the medicine enters properly.",
            "विवृतमार्गतया सम्यक् औषधम् अनुप्रविशति."),
        order(1, "Put these words of unit 29 in the line's order.",
              ["तथा", "ऽस्या", "विवृतमार्गतया", "सम्यगौषधम्", "अनुप्रविशति"],
              "In that way, her, because of the open passage, the medicine properly, enters.",
              "तथा → ऽस्या → विवृतमार्गतया → सम्यगौषधम् → अनुप्रविशति."),
        match(2, "Match each word of unit 29 to its meaning.",
              [["विवृत", "opened"], ["मार्ग", "passage"], ["सम्यक्", "properly"], ["औषध", "medicine"],
               ["अनुप्रविशति", "enters"]],
              "Five words carry the reason and the result.",
              "विवृत, मार्ग, सम्यक्, औषध, अनुप्रविशति.", role="extend",
              teaches="विवृतमार्गतया: -ता makes the abstract noun (having an open passage); the instrumental gives the reason."),
        mcq("discriminate", 3, "Which split of सम्यगौषधम् is right?",
            ("सम्यक् + औषधम्", "क् → ग् before a vowel: सम्यक् + औषधम् = सम्यगौषधम्."),
            [("सम्य + गौषधम्", "गौषधम् is not a word."),
             ("सम्यक् + ओषधम्", "That would give सम्यगोषधम्, with ओ; the print has औ."),
             ("सम्यः + औषधम्", "A visarga would not give ग्; सम्यः is not the word.")],
            "सम्यक् (properly) + औषधम् (medicine): क् → ग् before a vowel.",
            "Final क् → ग् before a vowel."),
        multi("apply", 4, "Which statements does unit 29 make?",
              [("The medicine is given by mouth", "No mouth is named; the medicine enters the open passage."),
               ("Her passage is open", "Right: विवृतमार्गतया."),
               ("The passage is defined as the uterus", "The passage is not defined in unit 29."),
               ("The medicine enters properly", "Right: सम्यगौषधमनुप्रविशति.")],
              [1, 3],
              "Open passage, so the medicine enters properly; the passage is not defined.",
              "विवृतमार्गतया सम्यगौषधमनुप्रविशति."),
        mcq("transfer", 5, "By the pattern of विवृतमार्गतया, what does दुर्बलतया (from दुर्बल, weak) mean?",
            ("Because of weakness", "-ता makes the abstract noun; the instrumental gives the reason."),
            [("For the sake of weakness", "That would be the dative दुर्बलतायै."),
             ("Without any weakness", "No negative is in the word."),
             ("More weak than before", "The comparative would be दुर्बलतर.")],
            "दुर्बल + ता + instrumental = because of weakness, like विवृतमार्गतया = because of the open passage.",
            "-तया = because of being ….",
            teaches="An abstract noun in -ता in the instrumental gives a reason: विवृतमार्गतया = because the passage is open."),
    ],
}

# ---------------------------------------------------------------- unit 30
AUTHORED["30"] = {
    "title": "अतऊर्ध्वं स्निग्धाभिर्यवागूभिः",
    "question": "By unit 30, how is she treated from now until delivery, and whose view is it?",
    "rule": ("After this (अतः ऊर्ध्वम्), until the time of delivery (आप्रसवकालात्), she is treated with unctuous gruels "
             "(स्निग्ध यवागू) and broths of jāṅgala (dry-land) animals: so says the venerable Dhanvantari."),
    "limits": ("The animals are not named. The verb of speaking for Dhanvantari is not printed (इति … धन्वन्तरिः). The "
               "woman as object is understood. 'After this' points back by context; the line names no month. The print "
               "has उपाचरेत् (should treat)."),
    "explain_hi": ("इसके बाद (अतः ऊर्ध्वम्) प्रसव के समय तक चिकनी (स्निग्ध) यवागुओं और जाङ्गल (सूखी भूमि के) जीवों के रसों, "
                   "यानी शोरबे से उपचार करे: ऐसा भगवान् धन्वन्तरि का मत है। "
                   "‘आप्रसवकालात्’ में ‘आ’ पञ्चमी के साथ ‘तक’ का अर्थ देता है। "
                   "कौन-से जाङ्गल जीव, नाम नहीं दिए; ‘कहते हैं’ वाली क्रिया भी छपी नहीं। "
                   "छपा ‘अतऊर्ध्वं’ = अतः + ऊर्ध्वम्: अ के बाद विसर्ग, अ से भिन्न स्वर से पहले, लुप्त हो जाता है।"),
    "hook": "अब से प्रसव तक: चिकनी यवागू + जाङ्गल रस — धन्वन्तरि।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 30, whose view closes the line?",
            ("The venerable Dhanvantari", "इति भगवान् धन्वन्तरिः."),
            [("The venerable Ātreya", "Ātreya's name closes unit 25, not unit 30."),
             ("The venerable Suśruta", "No Suśruta is named in unit 30."),
             ("The venerable Kāśyapa", "No Kāśyapa is named in unit 30.")],
            "The line ends: so (says) the venerable Dhanvantari.",
            "इति भगवान् धन्वन्तरिः."),
        order(1, "Put these parts of unit 30 in the line's order.",
              ["अतः ऊर्ध्वम्", "स्निग्धाभिः यवागूभिः", "जाङ्गलरसैः च", "उपाचरेत्", "आप्रसवकालात्",
               "इति भगवान् धन्वन्तरिः"],
              "After this, with unctuous gruels and dry-land broths, one should treat, until delivery: so Dhanvantari.",
              "अतः ऊर्ध्वम् → यवागूभिः → जाङ्गलरसैः → उपाचरेत् → आप्रसवकालात् → धन्वन्तरिः."),
        match(2, "Match each word of unit 30 to its meaning.",
              [["स्निग्ध", "unctuous"], ["यवागू", "gruel"], ["जाङ्गल", "of dry-land animals"],
               ["रस", "broth, juice"], ["उपाचरेत्", "should treat"]],
              "The two foods of the treatment and the verb.",
              "स्निग्ध, यवागू, जाङ्गल, रस, उपाचरेत्.", role="extend",
              teaches="आ with the ablative means up to, until: आप्रसवकालात् = until the time of delivery."),
        mcq("discriminate", 3, "Why is अतः printed without its visarga in अतऊर्ध्वं?",
            ("After अ, a visarga drops before a vowel other than अ", "अतः + ऊर्ध्वम् → अत ऊर्ध्वम्."),
            [("A visarga drops before every vowel", "Before अ it gives ओऽ: अतः + अत्र → अतोऽत्र."),
             ("The visarga became the ऊ of ऊर्ध्वम्", "ऊ is the first letter of ऊर्ध्वम् itself."),
             ("ऊर्ध्वम् begins with a consonant", "ऊर्ध्वम् begins with the vowel ऊ.")],
            "अतः + ऊर्ध्वम्: after अ, the visarga drops before ऊ, and no further join follows.",
            "अः + vowel other than अ → अ (visarga drops)."),
        mcq("apply", 4, "By unit 30, until when does this treatment continue?",
            ("Until the time of delivery", "आप्रसवकालात्: up to the time of delivery."),
            [("Until the ninth month begins", "The line says until delivery, not until the ninth."),
             ("For seven days only", "No count of days is named."),
             ("Until the skin stops itching", "Itching is not named in unit 30.")],
            "आ + प्रसवकालात् = until the time of delivery.",
            "आप्रसवकालात् = until delivery."),
        mcq("transfer", 5, "By the rule of आप्रसवकालात्, what does आमरणात् mean?",
            ("Until death", "आ with the ablative = up to, until."),
            [("After death", "After death would be मरणात् परम्."),
             ("Because of death", "आ- here is 'until', not a cause."),
             ("Without death", "Without would need a negative such as अ- or विना.")],
            "आ + मरणात् = until death, like आ + प्रसवकालात् = until delivery.",
            "आ + ablative = until.",
            teaches="आ with an ablative marks a limit, up to: आप्रसवकालात् = until the time of delivery."),
    ],
}

# ---------------------------------------------------------------- unit 31
AUTHORED["31"] = {
    "title": "नवमे तु ... पिचुं योनौ प्रणयेत्",
    "question": "By unit 31, what is done in the ninth (month), with what, and for what?",
    "rule": ("In the ninth (month), a picu (cotton swab) of that same anuvāsana oil is inserted into the yoni (vagina), "
             "for oiling the passage of the embryo and the āśaya (receptacle, probably the uterus)."),
    "limits": ("Printed स्नेहनाथंमिति is read स्नेहनार्थम् इति (for oiling), the र् lost in print: a suggested reading, so "
               "no question rests on it. āśaya = probably the uterus (probable). The compound can be read 'the embryo's "
               "passage and receptacle' or 'the garbha-mārga and the āśaya'. 'Month' is understood."),
    "explain_hi": ("नवें (मास) में उसी अनुवासन वाले तेल का पिचु (रुई का फाहा) योनि में रखे। "
                   "प्रयोजन: गर्भ के मार्ग और आशय (सम्भवतः गर्भाशय) का स्नेहन, यानी तेल से चिकना करना। "
                   "छपा ‘स्नेहनाथंमिति’ सम्भवतः ‘स्नेहनार्थम् इति’ है (र् छूटा), इसलिए इस शब्द पर प्रश्न नहीं। "
                   "‘तत एव’ = उसी से: वही तेल जो अनुवासन में लगा (डेटा की टिप्पणी: इकाई 27 का तेल)। "
                   "‘योनौ’ इ-अन्त शब्द ‘योनि’ की सप्तमी है।"),
    "hook": "नवें में: वही अनुवासन-तेल, पिचु बनकर योनि में।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 31, what is placed in the yoni in the ninth (month)?",
            ("A picu of the anuvāsana oil", "पिचुं योनौ प्रणयेत्: a cotton swab of that oil."),
            [("A phalavarti, a suppository", "Phalavartis are unit 39, for obstruction of stool and urine."),
             ("A cooled decoction of bilva", "That decoction is for the bath of unit 36."),
             ("Milk gruel with added ghee", "Milk gruel with ghee is drunk, in unit 23.")],
            "In the ninth, a picu of the same anuvāsana oil.",
            "नवमे … पिचुं योनौ प्रणयेत्."),
        order(1, "Put these parts of unit 31 in the line's order.",
              ["नवमे तु", "तत एवानुवासनतैलात्", "पिचुं", "योनौ", "प्रणयेत्"],
              "In the ninth, from that same anuvāsana oil, a picu, into the yoni, one should insert.",
              "नवमे तु → तत एवानुवासनतैलात् → पिचुं → योनौ → प्रणयेत्."),
        match(2, "Match each word of unit 31 to its meaning.",
              [["नवमे", "in the ninth"], ["पिचु", "cotton swab"], ["योनौ", "into the yoni (vagina)"],
               ["प्रणयेत्", "should insert"], ["आशय", "receptacle (probably the uterus)"]],
              "When, what, where, the verb, and one of the two parts oiled.",
              "नवमे, पिचु, योनौ, प्रणयेत्, आशय.", role="extend",
              teaches="तत एव = from that very (oil): the picu uses the oil already used for the anuvāsana."),
        mcq("discriminate", 3, "Which split of एवानुवासन- (in तत एवानुवासनतैलात्) is right?",
            ("एव + अनुवासन", "अ + अ → आ: एव + अनुवासन = एवानुवासन."),
            [("एवा + नुवासन", "नुवासन is not a word."),
             ("एवम् + अनुवासन", "A final म् would give एवमनुवासन."),
             ("एवः + अनुवासन", "अः before अ would give एवोऽनुवासन.")],
            "एव (very) + अनुवासन (oil enema): अ + अ → आ.",
            "अ + अ → आ."),
        mcq("apply", 4, "By unit 31, which oil is used for the picu?",
            ("The same oil used for the anuvāsana", "तत एव अनुवासनतैलात्: from that very anuvāsana oil."),
            [("Oil cooked with karavīra leaves", "That oil is for the massage of unit 18."),
             ("Ghee mixed with honey and milk", "Ghee, honey and milk join the āsthāpana of unit 26."),
             ("Water of all fragrant substances", "That water is for the bath of unit 36.")],
            "The picu takes the anuvāsana oil itself.",
            "तत एव अनुवासनतैलात्."),
        mcq("transfer", 5, "By the form योनौ (in the yoni), what is the locative singular of अग्नि (fire)?",
            ("अग्नौ", "An इ-stem can take -औ in the locative singular; masculine अग्नि has अग्नौ."),
            [("अग्निषु", "अग्निषु is the locative plural, in the fires."),
             ("अग्नेः", "अग्नेः is the genitive or ablative singular."),
             ("अग्निना", "अग्निना is the instrumental singular, by fire.")],
            "अग्नि → अग्नौ, like योनि → योनौ.",
            "इ-stem, locative singular → -औ.",
            teaches="Nouns ending in इ form the locative singular in -औ: योनि → योनौ (in the yoni), अग्नि → अग्नौ."),
    ],
}

# ---------------------------------------------------------------- unit 32
AUTHORED["32"] = {
    "title": "अनेन प्रथममासादारभ्य क्रमेण",
    "question": "By unit 32, which parts become soft at delivery, and since when has this worked?",
    "rule": ("By this (regimen), beginning from the first month and step by step (क्रमेण), at the time of delivery the "
             "embryo-bearing belly (कुक्षि), the waist (कटी), the flank (पार्श्व) and the back (पृष्ठ) become soft (मृदु)."),
    "limits": ("What अनेन (by this) refers to is not stated; by context it is the regimen of the preceding units. "
               "गर्भधारिणी is taken as qualifying the belly; it could also be a separate item, so no question rests on it. "
               "The four parts are a dvandva taken as one (collective singular)."),
    "explain_hi": ("इसके द्वारा (अनेन), पहले मास से आरम्भ करके क्रम से, प्रसव के समय गर्भिणी की गर्भ धारण करने वाली कुक्षि (पेट), "
                   "कटि (कमर), पार्श्व (बगल) और पृष्ठ (पीठ) मृदु हो जाते हैं। "
                   "‘अनेन’ किसे कहता है, लिखा नहीं; सन्दर्भ से पिछली इकाइयों की चर्या है। "
                   "‘गर्भधारिणी’ को कुक्षि का विशेषण माना गया; अलग अंग भी हो सकता है, इसलिए उस पर प्रश्न नहीं। "
                   "‘आरभ्य’ पञ्चमी के साथ ‘से आरम्भ करके’ है: प्रथममासात् आरभ्य।"),
    "hook": "पहले मास से क्रम से → प्रसव पर कुक्षि-कटि-पार्श्व-पीठ मृदु।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 32, which parts become soft at the time of delivery?",
            ("Belly, waist, flank and back", "कुक्षिकटीपार्श्वपृष्ठं मृदु भवति."),
            [("Eyes, heart and groin", "Pain in heart and groin is a sign in unit 40, not softening."),
             ("Breasts and the nipples", "No breasts are named in unit 32."),
             ("Hands, feet and head", "No hands, feet or head are named.")],
            "The four parts named: कुक्षि, कटी, पार्श्व, पृष्ठ.",
            "कुक्षि-कटी-पार्श्व-पृष्ठम् मृदु भवति."),
        order(1, "Put the four parts named in unit 32 in the line's order.",
              ["कुक्षि", "कटी", "पार्श्व", "पृष्ठम्"],
              "Belly, waist, flank, back.",
              "कुक्षि → कटी → पार्श्व → पृष्ठम्."),
        match(2, "Match each word of unit 32 to its meaning.",
              [["कुक्षि", "belly"], ["कटी", "waist, hip"], ["पार्श्व", "flank, side"], ["पृष्ठ", "back"],
               ["मृदु", "soft"]],
              "The four parts and what they become.",
              "कुक्षि, कटी, पार्श्व, पृष्ठ, मृदु.", role="extend",
              teaches="आरभ्य with an ablative = beginning from: प्रथममासात् आरभ्य = from the first month on."),
        mcq("discriminate", 3, "Which split of प्रथममासादारभ्य is right?",
            ("प्रथममासात् + आरभ्य", "त् → द् before a vowel: प्रथममासात् + आरभ्य = प्रथममासादारभ्य."),
            [("प्रथममासा + दारभ्य", "दारभ्य is not a word; the word is आरभ्य."),
             ("प्रथममासाः + आरभ्य", "आः before a vowel drops its visarga: प्रथममासा आरभ्य, with no द्."),
             ("प्रथममासम् + आरभ्य", "A final म् would give प्रथममासमारभ्य.")],
            "प्रथममासात् (from the first month) + आरभ्य (beginning): त् → द् before a vowel.",
            "Final त् → द् before a vowel."),
        multi("apply", 4, "Which statements does unit 32 make?",
              [("The regimen starts from the first month", "Right: प्रथममासादारभ्य."),
               ("The parts are soft already in the first month", "They become soft at the time of delivery (प्रसवकाले)."),
               ("The softening comes step by step", "Right: क्रमेण."),
               ("Only the back becomes soft", "Four parts are named: belly, waist, flank and back.")],
              [0, 2],
              "From the first month, step by step, the four parts are soft at delivery.",
              "प्रथममासादारभ्य क्रमेण … प्रसवकाले … मृदु भवति."),
        mcq("transfer", 5, "By the rule of प्रथममासादारभ्य, how is ग्रामात् + आगच्छति (comes from the village) joined?",
            ("ग्रामादागच्छति", "त् → द् before a vowel, as प्रथममासात् + आरभ्य."),
            [("ग्रामातागच्छति", "Before a vowel the त् does not stay त्."),
             ("ग्रामानागच्छति", "त् → न् only before a nasal."),
             ("ग्रामागच्छति", "The त् is not dropped.")],
            "ग्रामात् + आगच्छति = ग्रामादागच्छति, like प्रथममासात् + आरभ्य = प्रथममासादारभ्य.",
            "Final त् → द् before a vowel.",
            teaches="A final त् becomes द् before a vowel: प्रथममासात् + आरभ्य → प्रथममासादारभ्य."),
    ],
}

# ---------------------------------------------------------------- unit 33
AUTHORED["33"] = {
    "title": "वायुश्चानुलोमः संपद्यते",
    "question": "By unit 33, what further result is stated for the wind?",
    "rule": ("And the wind (वायु, the Vāta in the body) becomes anuloma (संपद्यते): it moves in its proper, downward "
             "direction."),
    "limits": ("The line names no cause; च (and) joins it by context to the result stated in unit 32 (अनेन, by this). "
               "It does not say how the downward movement shows. A prose line."),
    "explain_hi": ("और वायु अनुलोम हो जाता है, यानी अपनी ठीक, नीचे की दिशा में चलने लगता है। "
                   "यहाँ वायु = शरीर का वात। "
                   "‘च’ इसे सन्दर्भ से पिछली इकाई के फल (‘अनेन’, इसके द्वारा) से जोड़ता है; कारण इस पंक्ति में नहीं लिखा। "
                   "‘संपद्यते’ (सम् + √पद्, आत्मनेपद) = हो जाता है। "
                   "सन्धि: वायुः + च → वायुश्च (विसर्ग → श् च से पहले); च + अनुलोमः → चानुलोमः (अ + अ → आ)।"),
    "hook": "वायु अनुलोम हो जाता है।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 33, what becomes anuloma?",
            ("The wind (vāyu)", "वायुश्चानुलोमः संपद्यते."),
            [("Urine and stool", "They become natural (प्रकृतिभूत), in unit 34."),
             ("The afterbirth", "The jarāyu goes to the passage, in unit 34."),
             ("The belly", "The belly becomes soft, in unit 32.")],
            "The wind becomes anuloma.",
            "वायुः अनुलोमः संपद्यते."),
        order(1, "Put the words of unit 33 in the line's order.",
              ["वायुः", "च", "अनुलोमः", "संपद्यते"],
              "The wind, and, downward-moving, becomes.",
              "वायुः → च → अनुलोमः → संपद्यते."),
        fill(2, "And the wind becomes downward-moving: वायुश्च ____ संपद्यते (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("अनुलोमः", None, "अनुलोम"),
             "अनुलोमः = moving in the proper, downward direction; printed joined as वायुश्चानुलोमः.",
             "अनुलोम = moving downward, in the proper direction: the state the regimen brings about for the wind.",
             "वायुः च अनुलोमः संपद्यते."),
        mcq("discriminate", 3, "Which split of वायुश्चानुलोमः is right?",
            ("वायुः + च + अनुलोमः", "Visarga → श् before च; अ + अ → आ."),
            [("वायु + च + अनुलोमः", "Without a visarga no श् arises: it would be वायुचानुलोमः."),
             ("वायुः + चा + नुलोमः", "नुलोमः is not a word; the word is अनुलोमः."),
             ("वायुः + चन + उलोमः", "चन and उलोमः are not the words here.")],
            "वायुः (wind) + च (and) + अनुलोमः (downward-moving).",
            "ः + च → श्च; अ + अ → आ."),
        mcq("apply", 4, "In unit 33, what does अनुलोम say about the wind?",
            ("It moves in its proper, downward direction", "अनुलोमः: moving downward, in the proper direction."),
            [("It moves upward, against its course", "That is the opposite of अनुलोम."),
             ("It stops moving altogether", "अनुलोम is a direction of movement, not a stop."),
             ("It increases greatly in amount", "No increase is named in unit 33.")],
            "अनुलोम = in the proper, downward direction.",
            "वायुः अनुलोमः = the wind moves downward."),
        mcq("transfer", 5, "By the rule of वायुश्च, how is रामः + च joined?",
            ("रामश्च", "A visarga before च becomes श्."),
            [("रामोच", "ओ arises before a voiced sound; च is unvoiced."),
             ("रामच", "The visarga is not dropped before च."),
             ("रामस्च", "Before च the visarga becomes श्, not स्.")],
            "रामः + च = रामश्च, like वायुः + च = वायुश्च.",
            "ः + च → श्च.",
            teaches="A visarga before च or छ becomes श्: वायुः + च → वायुश्च."),
    ],
}

# ---------------------------------------------------------------- unit 34
AUTHORED["34"] = {
    "title": "मूत्रपुरीषं च प्रकृतिभूतं",
    "question": "By unit 34, what happens to urine and stool, and to the jarāyu?",
    "rule": ("Urine and stool (मूत्रपुरीष) become natural (प्रकृतिभूत), and the jarāyu (afterbirth: placenta with "
             "membranes) goes to the passage (मार्ग)."),
    "limits": ("Printed मार्ग lacks its anusvāra; the accusative मार्गम् is suggested, and no question rests on its form. "
               "The text does not say whether the jarāyu comes out, nor does it define the passage. The verb for urine "
               "and stool is understood."),
    "explain_hi": ("और मूत्र तथा मल प्रकृतिस्थ, यानी स्वाभाविक हो जाते हैं, और जरायु (गर्भ की झिल्ली सहित अपरा) मार्ग को प्राप्त होता है। "
                   "‘मूत्रपुरीषम्’ द्वन्द्व है, एकवचन में समूह के रूप में। "
                   "जरायु बाहर निकलता है या नहीं, ग्रन्थ यहाँ नहीं कहता; ‘मार्ग’ की परिभाषा भी नहीं। "
                   "छपा ‘मार्ग’ सम्भवतः ‘मार्गम्’ है (अनुस्वार छूटा); इस पर प्रश्न नहीं। "
                   "सन्धि: जरायुः + च → जरायुश्च।"),
    "hook": "मूत्र-मल स्वाभाविक; जरायु मार्ग पर।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 34, what goes to the passage?",
            ("The jarāyu, the afterbirth", "जरायुश्च मार्ग प्रतिपद्यते."),
            [("Urine and stool", "They become natural; they are not said to go to the passage."),
             ("The medicine", "The medicine enters, in unit 29."),
             ("The wind", "The wind becomes anuloma, in unit 33.")],
            "The jarāyu goes to the passage.",
            "जरायुः मार्गं प्रतिपद्यते."),
        order(1, "Put these words of unit 34 in the line's order.",
              ["मूत्रपुरीषं च", "प्रकृतिभूतं", "जरायुश्च", "मार्ग", "प्रतिपद्यते"],
              "Urine and stool, become natural; and the jarāyu, the passage, goes to.",
              "मूत्रपुरीषं च → प्रकृतिभूतं → जरायुश्च → मार्ग → प्रतिपद्यते."),
        match(2, "Match each word of unit 34 to its meaning.",
              [["मूत्र", "urine"], ["पुरीष", "stool"], ["प्रकृतिभूत", "become natural"],
               ["जरायु", "afterbirth (placenta with membranes)"], ["प्रतिपद्यते", "goes to, enters"]],
              "The two results of the line.",
              "मूत्र, पुरीष, प्रकृतिभूत, जरायु, प्रतिपद्यते.", role="extend",
              teaches="मूत्रपुरीषम् is a dvandva taken as one thing: urine-and-stool, in the neuter singular."),
        mcq("discriminate", 3, "By unit 34, what does प्रकृतिभूतम् say of urine and stool?",
            ("They become natural, as they normally are", "प्रकृतिभूत = become natural, normal."),
            [("They stop altogether", "Natural is not stopped; no stopping is named."),
             ("They mix with the afterbirth", "The jarāyu is a separate statement."),
             ("They become much more abundant", "Abundance is a sign in unit 40, not this line.")],
            "प्रकृति (nature) + भूत (become): back to the natural state.",
            "प्रकृतिभूतम् = become natural."),
        multi("apply", 4, "Which statements does unit 34 make?",
              [("The text says the jarāyu comes out here", "It says only that the jarāyu goes to the passage."),
               ("Urine and stool become natural", "Right: मूत्रपुरीषं च प्रकृतिभूतम्."),
               ("The jarāyu goes to the passage", "Right: जरायुश्च मार्ग प्रतिपद्यते."),
               ("The passage is defined as the vagina", "The passage is not defined in unit 34.")],
              [1, 2],
              "Two statements: urine and stool natural; the jarāyu to the passage.",
              "मूत्रपुरीषं प्रकृतिभूतम्; जरायुः मार्गं प्रतिपद्यते."),
        mcq("transfer", 5, "By the dvandva मूत्रपुरीषम्, what does पाणिपादम् mean?",
            ("Hands and feet, taken together", "A dvandva joins two things as one: hands-and-feet."),
            [("The hand of the foot", "That would be a genitive tatpuruṣa, not a dvandva."),
             ("One whose hands are feet", "That would be a bahuvrīhi reading, not this pattern."),
             ("Feet but no hands", "A dvandva joins both members; it excludes neither.")],
            "पाणि + पाद = hands and feet, like मूत्र + पुरीष = urine and stool.",
            "Dvandva = A and B, taken together.",
            teaches="A dvandva compound joins its members with 'and', and can stand as one neuter singular: मूत्रपुरीषम्."),
    ],
}

# ---------------------------------------------------------------- unit 35
AUTHORED["35"] = {
    "title": "पुत्रं चेष्टं कल्यमायुष्मंतं",
    "question": "By unit 35, what kind of son does the strong woman bear, and how?",
    "rule": ("The strong woman (बलवती) gives birth at the (due) time (काले), easily (सुखेन), to a desired (इष्ट), "
             "healthy (कल्य), long-lived (आयुष्मत्) and happy (सुखिन्) son."),
    "limits": ("पुत्रम् is son, as printed, not child. बलवती is read as the strong woman, the subject. काले = at the due "
               "time of delivery. The line states an outcome of the regimen already described; it adds no new rule."),
    "explain_hi": ("और वह बलवती (बल वाली) स्त्री समय पर (काले), सुख से (सुखेन), इष्ट (चाहे हुए), कल्य (स्वस्थ), आयुष्मान् "
                   "(दीर्घायु) और सुखी पुत्र को जन्म देती है। "
                   "छपा शब्द ‘पुत्रम्’ है, यानी पुत्र; ‘सन्तान’ नहीं। "
                   "‘आयुष्मत्’ और ‘बलवती’ में ‘-मत्/-वत्’ प्रत्यय ‘वाला’ का अर्थ देता है। "
                   "सन्धि: च + इष्टम् → चेष्टम् (अ + इ → ए)।"),
    "hook": "बलवती, समय पर, सुख से: इष्ट, स्वस्थ, दीर्घायु, सुखी पुत्र।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 35, how does the strong woman give birth?",
            ("Easily and at the due time", "सुखेन काले प्रसूते."),
            [("Early, before her time", "काले means at the (due) time."),
             ("With great difficulty", "सुखेन means easily."),
             ("Late, after the due time", "काले means at the (due) time.")],
            "At the time, easily.",
            "सुखेन काले बलवती प्रसूते."),
        order(1, "Put the words describing the son in unit 35 in the line's order.",
              ["पुत्रम्", "च इष्टम्", "कल्यम्", "आयुष्मन्तम्", "सुखिनम्"],
              "A son, and desired, healthy, long-lived, happy.",
              "पुत्रम् → च इष्टम् → कल्यम् → आयुष्मन्तम् → सुखिनम्."),
        match(2, "Match each word of unit 35 to its meaning.",
              [["इष्ट", "desired"], ["कल्य", "healthy"], ["आयुष्मत्", "long-lived"], ["सुखिन्", "happy"],
               ["बलवती", "strong (woman)"]],
              "Four words for the son and one for the mother.",
              "इष्ट, कल्य, आयुष्मत्, सुखिन्, बलवती.", role="extend",
              teaches="-मत् / -वत् mean possessing: आयुष्मत् (having life: long-lived), बलवती (having strength)."),
        mcq("discriminate", 3, "Which split of चेष्टं (चेष्टम्) is right?",
            ("च + इष्टम्", "अ + इ → ए: च + इष्टम् = चेष्टम्."),
            [("च + एष्टम्", "अ + ए would give ऐ: चैष्टम्."),
             ("चः + इष्टम्", "After अ the visarga drops before इ, leaving च इष्टम् unjoined."),
             ("चे + ष्टम्", "ष्टम् is not a word.")],
            "च (and) + इष्टम् (desired): अ + इ → ए.",
            "अ + इ → ए."),
        mcq("apply", 4, "In unit 35, which word says the son will be long-lived?",
            ("आयुष्मन्तम्", "आयुष्मत् = having life: long-lived."),
            [("कल्यम्", "कल्य means healthy."),
             ("सुखिनम्", "सुखिन् means happy."),
             ("इष्टम्", "इष्ट means desired.")],
            "आयुष्मन्तम् = long-lived.",
            "आयुष्मत् = long-lived."),
        mcq("transfer", 5, "By the rule of चेष्टम् (च + इष्टम्), how is न + इति joined?",
            ("नेति", "अ + इ → ए, as च + इष्टम् → चेष्टम्."),
            [("नैति", "ऐ comes from अ + ए or ऐ, not from अ + इ."),
             ("न्यति", "य comes from इ before a vowel; here अ comes first."),
             ("नीति", "The अ is not dropped before इ.")],
            "न + इति = नेति, like च + इष्टम् = चेष्टम्.",
            "अ + इ → ए.",
            teaches="अ and इ meet as ए: च + इष्टम् → चेष्टम्."),
    ],
}

# ---------------------------------------------------------------- unit 36
AUTHORED["36"] = {
    "title": "गर्भिण्याः प्रत्यहं स्नानमुपदिशेत्",
    "question": "By unit 36, with what is the pregnant woman's daily bath prepared?",
    "rule": ("One should prescribe a daily bath (प्रत्यहं स्नानम्) for the pregnant woman with a cooled decoction (शीत "
             "क्वाथ) of a list of plants (bilva, kārpāsī, pāṭalī, picumanda and others), or with water of all fragrant "
             "substances (सर्वगन्धोदक)."),
    "limits": ("Low confidence. फंफेणा is unidentified and पत्रभंग unclear; no question rests on them. Labels: bilva "
               "bael, kārpāsī cotton, pāṭalī Stereospermum suaveolens, picumanda neem (standard); agnimantha Premna, "
               "māṃsī spikenard (probable); vardhamānaka (disputed). The fragrant substances are not listed."),
    "explain_hi": ("गर्भिणी के लिए प्रतिदिन स्नान का उपदेश करे: द्रव्यों की एक सूची के ठण्डे किए काढ़े (शीत क्वाथ) से, अथवा "
                   "सब सुगन्धित द्रव्यों के जल (सर्वगन्धोदक) से। "
                   "सूची: बिल्व (बेल), कार्पासी (कपास), पाटली (पाढ़ल), पिचुमन्द (नीम) — मानक; अग्निमन्थ (प्रेम्ना, अरणी) और मांसी "
                   "(जटामांसी) — सम्भावित; वर्धमानक — पहचान विवादित (शायद अरण्ड)। "
                   "‘फंफेणा’ अज्ञात और ‘पत्रभंग’ अस्पष्ट हैं; इन पर प्रश्न नहीं। "
                   "कौन-से सुगन्धित द्रव्य, नहीं गिनाए गए। "
                   "सन्धि: सर्वगन्ध + उदकेन → सर्वगन्धोदकेन (अ + उ → ओ)।"),
    "hook": "रोज़ स्नान: बेल-कपास-नीम आदि का ठण्डा काढ़ा, या सुगन्धित जल।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 36, how often is the bath prescribed?",
            ("Daily (प्रत्यहम्)", "गर्भिण्याः प्रत्यहं स्नानमुपदिशेत्."),
            [("Once a month", "The word is प्रत्यहम्, every day."),
             ("Every third day", "The word is प्रत्यहम्, every day."),
             ("Only on the day of delivery", "The word is प्रत्यहम्, every day.")],
            "प्रत्यहम् = every day.",
            "प्रत्यहं स्नानम् = a daily bath."),
        order(1, "Put these plants of unit 36 in the compound's order (unclear words left out).",
              ["बिल्व", "कार्पासी", "पाटली", "पिचुमन्द", "अग्निमन्थ", "मांसी"],
              "Bilva, kārpāsī, (फंफेणा, unclear), pāṭalī, picumanda, agnimantha, māṃsī.",
              "बिल्व → कार्पासी → पाटली → पिचुमन्द → अग्निमन्थ → मांसी."),
        match(2, "Match each plant of unit 36 to the identification the data gives.",
              [["बिल्व", "bael (standard)"], ["कार्पासी", "cotton (standard)"], ["पिचुमन्द", "neem (standard)"],
               ["मांसी", "spikenard (probable)"], ["अग्निमन्थ", "Premna (probable)"]],
              "The identifications keep the data's labels: standard or probable.",
              "बिल्व, कार्पासी, पिचुमन्द, मांसी, अग्निमन्थ.", role="extend",
              teaches="Plant names keep the data's label: standard (bael, cotton, neem), probable (spikenard, Premna)."),
        mcq("discriminate", 3, "Which split of सर्वगंधोदकेन is right?",
            ("सर्वगन्ध + उदकेन", "अ + उ → ओ: सर्वगन्ध + उदकेन = सर्वगन्धोदकेन."),
            [("सर्वगन्धः + उदकेन", "After अ a visarga drops before उ: सर्वगन्ध उदकेन, unjoined."),
             ("सर्वगन्धो + दकेन", "दकेन is not a word; the word is उदकेन."),
             ("सर्वगन्ध + ओदकेन", "अ + ओ would give औ, and ओदक is not the word.")],
            "सर्वगन्ध (all fragrant substances) + उदकेन (with water): अ + उ → ओ.",
            "अ + उ → ओ."),
        mcq("apply", 4, "By unit 36, what may be used instead of the cooled decoction?",
            ("Water of all fragrant substances", "सर्वगन्धोदकेन वा: or with water of all fragrant substances."),
            [("Hot water mixed with ghee", "No hot water or ghee is named in unit 36."),
             ("Water cooked with jujube", "Jujube water is for the āsthāpana of unit 26."),
             ("The anuvāsana oil itself", "That oil is for the enema and the picu.")],
            "वा (or): the decoction, or the fragrant water.",
            "क्वाथेन शीतेन सर्वगन्धोदकेन वा."),
        mcq("transfer", 5, "By the rule of सर्वगन्धोदक, how is गङ्गा + उदकम् (Gaṅgā water) joined?",
            ("गङ्गोदकम्", "आ + उ → ओ, as अ + उ → ओ in सर्वगन्ध + उदक."),
            [("गङ्गौदकम्", "औ comes from अ/आ + ओ or औ, not + उ."),
             ("गङ्गादकम्", "The उ is not dropped."),
             ("गङ्गूदकम्", "The आ does not simply turn into ऊ.")],
            "गङ्गा + उदकम् = गङ्गोदकम्, like सर्वगन्ध + उदक = सर्वगन्धोदक.",
            "अ/आ + उ → ओ.",
            teaches="अ or आ before उ joins as ओ: सर्वगन्ध + उदकेन → सर्वगन्धोदकेन."),
    ],
}

# ---------------------------------------------------------------- unit 37
AUTHORED["37"] = {
    "title": "सूतिकागारं कारयेत्",
    "question": "By unit 37, when and where is the delivery chamber built, and what is it like?",
    "rule": ("Even before her ninth month, one should have a delivery chamber (सूतिकागार) built in an approved place, "
             "approved by the science of building sites (वास्तुविद्या), comfortable in all seasons, with fire at hand, "
             "and with a door to the east or to the north."),
    "limits": ("Low confidence. अपृतता and उपृतत् are unclear; 'free of bones, gravel and potsherds' and 'furnished with "
               "all equipment' rest on the conjectural readings अपहृत and उपहृत, so no question asks about them. ऽस्या/"
               "चैवास्या is taken as अस्याः (her). The rules of वास्तुविद्या are not given here."),
    "explain_hi": ("उसके नवें मास से पहले ही सूतिकागार (प्रसव-कक्ष) बनवाए: प्रशस्त स्थान में, वास्तुविद्या से प्रशस्त, सब ऋतुओं में "
                   "सुखद, जिसमें अग्नि पास हो, और जिसका द्वार पूर्व या उत्तर की ओर हो। "
                   "‘हड्डी, कंकड़, ठीकरे हटे’ और ‘सब उपकरणों से युक्त’ अनुमानित पाठ (अपहृत, उपहृत) पर टिके हैं; इन पर प्रश्न नहीं। "
                   "‘प्राक्’ इस पंक्ति में दो अर्थ में आता है: पञ्चमी के साथ ‘पहले’ (प्राक् … नवमान्मासात्), और ‘प्राग्द्वार’ में ‘पूर्व दिशा’। "
                   "‘कारयेत्’ णिजन्त है: बनवाए।"),
    "hook": "नवें से पहले: प्रशस्त स्थान, सब ऋतु सुखद, अग्नि पास, पूर्व/उत्तर द्वार।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 37, when is the delivery chamber to be made?",
            ("Before her ninth month", "प्राक् … नवमान्मासात्: before the ninth month."),
            [("In the first month", "No first month is named in unit 37."),
             ("After the delivery", "It is made before, for the delivery."),
             ("On the day labour begins", "The line says before the ninth month.")],
            "प्राक् with the ablative नवमात् मासात् = before the ninth month.",
            "प्राक् नवमात् मासात् = before the ninth month."),
        order(1, "Put these parts of unit 37 in the line's order.",
              ["प्राक् चैवास्या नवमान्मासात्", "प्रशस्ते देशे", "वास्तुविद्याप्रशस्तम्", "सर्वर्तुसुखम्",
               "प्राग्द्वारमुदग्द्वारं वा", "सूतिकागारं कारयेत्"],
              "Before the ninth month; in an approved place; approved by vāstu-vidyā; pleasant in all seasons; east or "
              "north door; one should have the chamber made.",
              "प्राक् → देशे → वास्तुविद्या → सर्वर्तुसुखम् → द्वार → सूतिकागारं कारयेत्."),
        match(2, "Match each word of unit 37 to its meaning.",
              [["सूतिकागार", "delivery chamber"], ["वास्तुविद्या", "science of building sites"],
               ["सर्वर्तुसुख", "comfortable in all seasons"], ["सन्निहितज्वलन", "with fire kept at hand"],
               ["उदग्द्वार", "with a door to the north"]],
              "Words of the chamber's description from the sure parts of the line.",
              "सूतिकागार, वास्तुविद्या, सर्वर्तुसुख, सन्निहितज्वलन, उदग्द्वार.", role="extend",
              teaches="प्राक् with an ablative means before (प्राक् नवमात् मासात्); in प्राग्द्वार it means east."),
        mcq("discriminate", 3, "Which split of सर्वर्तुसुखम् is right?",
            ("सर्व + ऋतु + सुखम्", "अ + ऋ → अर्: सर्व + ऋतु = सर्वर्तु."),
            [("सर्वर् + तुसुखम्", "तुसुखम् is not a word; the word is ऋतु."),
             ("सर्व + अर्तुसुखम्", "अ + अ would give आ: सर्वार्तु."),
             ("सर्वः + ऋतुसुखम्", "A compound member has no visarga, and it would not give र्.")],
            "सर्व (all) + ऋतु (season) + सुखम् (comfortable): अ + ऋ → अर्.",
            "अ + ऋ → अर्."),
        mcq("apply", 4, "By unit 37, which way does the chamber's door face?",
            ("East or north", "प्राग्द्वारमुदग्द्वारं वा: east-door or north-door."),
            [("South or west", "The line names east (प्राक्) and north (उदक्)."),
             ("East only", "वा (or) adds the north as the other choice."),
             ("North only", "वा (or) gives the east as the other choice.")],
            "प्राग्द्वारम् or उदग्द्वारम्: either is allowed.",
            "प्राक् = east, उदक् = north, वा = or."),
        mcq("transfer", 5, "By the rule of प्राग्द्वारम्, how is वाक् + देवी (goddess of speech) joined?",
            ("वाग्देवी", "क् → ग् before a voiced sound, as प्राक् + द्वारम् → प्राग्द्वारम्."),
            [("वाक्देवी", "Before the voiced द the क् does not stay क्."),
             ("वाङ्देवी", "क् → ङ् only before a nasal."),
             ("वाचोदेवी", "ओ arises from a visarga, not from क्.")],
            "वाक् + देवी = वाग्देवी, like प्राक् + द्वारम् = प्राग्द्वारम्.",
            "Final क् → ग् before a voiced sound.",
            teaches="A final क् becomes ग् before a voiced sound: प्राक् + द्वारम् → प्राग्द्वारम्, उदक् + द्वारम् → उदग्द्वारम्."),
    ],
}

# ---------------------------------------------------------------- unit 38
AUTHORED["38"] = {
    "title": "प्रसवकालमुदीक्षेत",
    "question": "By unit 38, under what conditions does she enter and await delivery?",
    "rule": ("There, when the stars and the rest are favourable, with the utterance of puṇyāha (auspicious-day formula), "
             "she enters; attended by women who have given birth and can bear hardship, devoted to auspicious rites "
             "(स्वस्त्ययन), she awaits the time of delivery."),
    "limits": ("Low confidence. No question rests on: अनुक्ताभिः, अविपादाभिः (unclear), तु + आवर्तमाना (circling "
               "cows, brahmins and elders: not firm), where बहुशः belongs, परितृता read परिवृता, or the food-and-conduct "
               "phrase (printed नेरा, म्त्र). The link to unit 37's chamber is by context."),
    "explain_hi": ("वहाँ, नक्षत्र आदि अनुकूल होने पर, पुण्याह (शुभ दिन के वचन) के शब्द के साथ वह प्रवेश करती है; प्रसव कर चुकी, "
                   "क्लेश सहने वाली स्त्रियाँ उसके साथ रहती हैं; स्वस्त्ययन (मंगल-कर्म) में लगी हुई वह प्रसव के समय की प्रतीक्षा करती है। "
                   "छपाई बिगड़ी है: ‘अनुक्ताभिः’, ‘अविपादाभिः’ अस्पष्ट हैं; गाय-ब्राह्मण-वृद्धों की प्रदक्षिणा वाला अंश अनिश्चित है; "
                   "‘परितृता’ को ‘परिवृता’ (घिरी हुई) और आहार-विहार वाले अंश को सुझाए पाठ से पढ़ा गया — इन पर प्रश्न नहीं। "
                   "सूतिकागार (इकाई 37) से जोड़ ‘तत्र’ (वहाँ) से, सन्दर्भ द्वारा है।"),
    "hook": "शुभ नक्षत्र, पुण्याह-वचन, प्रवेश, अनुभवी परिचारिकाएँ, प्रतीक्षा।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 38, what does she do at the end of the line?",
            ("She awaits the time of delivery", "प्रसवकालमुदीक्षेत: she should await the time of delivery."),
            [("She drinks gruel with ghee", "Gruel with ghee is unit 42."),
             ("She has the chamber built", "The chamber is to be built in unit 37 (कारयेत्)."),
             ("She takes her daily bath", "The daily bath is unit 36.")],
            "The line ends with the waiting for delivery.",
            "प्रसवकालम् उदीक्षेत."),
        order(1, "Put these parts of unit 38 in the line's order.",
              ["तत्रानुकूलेषु नक्षत्रादिषु", "पुण्याहशब्देन", "प्रविश्य", "क्लेशक्षमाभिः", "स्वस्त्ययनपरा",
               "प्रसवकालमुदीक्षेत"],
              "Favourable stars, the puṇyāha utterance, entering, hardship-bearing attendants, devoted to rites, awaiting.",
              "नक्षत्रादिषु → पुण्याहशब्देन → प्रविश्य → क्लेशक्षमाभिः → स्वस्त्ययनपरा → उदीक्षेत."),
        match(2, "Match each word of unit 38 to its meaning.",
              [["अनुकूल", "favourable"], ["पुण्याह", "auspicious-day formula"], ["क्लेशक्षमा", "able to bear hardship"],
               ["स्वस्त्ययन", "auspicious rites"], ["उदीक्षेत", "should await"]],
              "Words from the sure parts of the long sentence.",
              "अनुकूल, पुण्याह, क्लेशक्षमा, स्वस्त्ययन, उदीक्षेत.", role="extend",
              teaches="-परा at the end of a compound means devoted to: स्वस्त्ययनपरा = devoted to auspicious rites."),
        mcq("discriminate", 3, "Which split of स्वस्त्ययन is right?",
            ("स्वस्ति + अयन", "इ + अ → य: स्वस्ति + अयन = स्वस्त्ययन."),
            [("स्वस्त्य + अयन", "अ + अ would give आ: स्वस्त्यायन."),
             ("स्वस्त + ययन", "स्वस्त and ययन are not the words here."),
             ("स्वस्तिः + अयन", "A visarga after इ before a vowel would give र्: स्वस्तिरयन.")],
            "स्वस्ति (well-being) + अयन (going, rite): इ + अ → य.",
            "इ + a different vowel → य्."),
        multi("apply", 4, "Which statements does unit 38 make, on its sure words?",
              [("She drinks gruel before entering", "No gruel is named in unit 38."),
               ("The stars and the rest are favourable", "Right: अनुकूलेषु नक्षत्रादिषु."),
               ("Her attendants have never given birth", "They are women who have given birth (प्रसूताभिः)."),
               ("The puṇyāha formula is uttered", "Right: पुण्याहशब्देन.")],
              [1, 3],
              "Favourable stars and the puṇyāha utterance; the attendants have given birth.",
              "अनुकूलेषु नक्षत्रादिषु पुण्याहशब्देन … प्रसूताभिः."),
        mcq("transfer", 5, "By the rule of स्वस्त्ययनपरा, what does धर्मपरः mean?",
            ("Devoted to dharma", "-पर at the end of a compound = devoted to, intent on."),
            [("Against dharma", "-पर does not mean against."),
             ("Without dharma", "-पर is not a negative."),
             ("Afraid of dharma", "Fear would need a word such as भीत.")],
            "धर्म + पर = devoted to dharma, like स्वस्त्ययन + परा = devoted to auspicious rites.",
            "-पर (end of compound) = devoted to.",
            teaches="-पर / -परा at the end of a compound means devoted to: स्वस्त्ययनपरा."),
    ],
}

# ===================================================================== NOTES_HI
NOTES_HI = {
    "27": ("गद्य; विश्वास निम्न। पाठ-चिह्न: पहला शब्द ‘पुराणविद्विश्शुत्त्यर्थं’ कोई शब्द नहीं; ‘पुराणविड्विशुद्ध्यर्थम्’ (पुराने मल की शुद्धि हेतु) "
           "अनुमानित पाठ है (द → ड्, श्श → श, त्त → द्ध) — इस पर प्रश्न नहीं। मधुक = सम्भवतः मुलेठी (सम्भावित)। कर्ता (वैद्य) अलिखित। "
           "सन्धि जाँची: मधुक + आदि → मधुकादि (अ + आ → आ); मधुर + औषध → मधुरौषध (अ + औ → औ); तैलेन + अनुवासयेत् → तैलेनानुवासयेत् "
           "(अ + अ → आ); अनुवासयेत् + अनुलोमनाय → अनुवासयेदनुलोमनाय (त् → द् स्वर से पहले)।"),
    "28": ("गद्य; विश्वास मध्यम; दो छपी पंक्तियाँ (02.03.30, 02.03.31) जुड़ी हैं; कोई पाठ-चिह्न नहीं। छपा ‘हिमारुते’ दो शब्द हैं: हि मारुते। "
           "‘न्युब्ज’ = औंधा/आगे झुका; आसन का पूरा वर्णन नहीं। डेटा की टिप्पणी इसे इकाई 26-27 की विधि का क्रम मानती है। "
           "सन्धि जाँची: सुखम् + अनुपद्रवा → सुखमनुपद्रवा; अन् + उपद्रवा → अनुपद्रवा; न्युब्जाम् + आस्थापयेत् → न्युब्जामास्थापयेत्; "
           "आस्थापयेत् + अनुवासयेत् → आस्थापयेदनुवासयेत् (त् → द्); अनुवासयेत् + वा → अनुवासयेद्वा (त् → द् घोष व से पहले)।"),
    "29": ("गद्य; विश्वास मध्यम। पाठ-चिह्न: छपा ‘ऽस्या’ = अस्याः (षष्ठी, विसर्ग छपाई में छूटा; तृतीया ‘अस्या’ अर्थ में नहीं बैठती) — "
           "इस पर प्रश्न नहीं। ‘मार्ग’ अपरिभाषित (तुलना: इकाई 31 का गर्भमार्ग)। "
           "सन्धि जाँची: तथा + अस्याः → तथाऽस्याः (आ + अ → आ, ऽ मिले अ का चिह्न); सम्यक् + औषधम् → सम्यगौषधम् (क् → ग् स्वर से पहले); "
           "औषधम् + अनुप्रविशति → औषधमनुप्रविशति।"),
    "30": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। जाङ्गल जीवों के नाम नहीं; धन्वन्तरि के लिए ‘कहते हैं’ क्रिया अलिखित; कर्म (गर्भिणी) समझा जाता है। "
           "छपा रूप ‘उपाचरेत्’ (चोपाचरेद्) है, जबकि डेटा का शब्द-विभाग ‘उपचरेत्’ (उप-√चर्) देता है — इस पर प्रश्न नहीं। "
           "सन्धि जाँची: अतः + ऊर्ध्वम् → अत ऊर्ध्वम् (अ के बाद विसर्ग, अ से भिन्न स्वर से पहले, लुप्त; छपा ‘अतऊर्ध्वं’); "
           "स्निग्धाभिः + यवागूभिः → स्निग्धाभिर्यवागूभिः (इ के बाद विसर्ग → र् घोष से पहले); यवागूभिः + जाङ्गल → यवागूभिर्जाङ्गल; "
           "रसैः + च → रसैश्च; च + उपाचरेत् → चोपाचरेत् (अ + उ → ओ); कालात् + इति → कालादिति (त् → द्)।"),
    "31": ("गद्य; विश्वास मध्यम। पाठ-चिह्न: छपा ‘स्नेहनाथंमिति’ = सम्भवतः स्नेहनार्थम् इति (र् छूटा) — इस पर प्रश्न नहीं। "
           "छपा ‘गर्भमार्गाशाययोः’ में ‘शा’ दीर्घ है, शब्द ‘आशय’ है (डेटा ‘गर्भमार्गाशययोः’ लेता है)। समास दो तरह पढ़ा जा सकता है; "
           "आशय = सम्भवतः गर्भाशय (सम्भावित)। पिचु = रुई का फाहा (तौल का माप भी, यहाँ नहीं)। योनि = यहाँ योनि-मार्ग। "
           "सन्धि जाँची: ततः + एव → तत एव (छपा ‘ततएव’); एव + अनुवासन → एवानुवासन (अ + अ → आ); तैलात् + पिचुम् → तैलात्पिचुम्; "
           "पिचुम् + योनौ → पिचुं योनौ।"),
    "32": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। ‘अनेन’ का संदर्भ अलिखित (पिछली चर्या)। ‘गर्भधारिणी’ कुक्षि का विशेषण माना गया, "
           "अलग अंग भी सम्भव — इस पर प्रश्न नहीं। द्वन्द्व समाहार एकवचन (पृष्ठम्)। "
           "सन्धि जाँची: प्रथममासात् + आरभ्य → प्रथममासादारभ्य (त् → द् स्वर से पहले); छपा ‘मृदुभवति’ = मृदु भवति (अन्तराल नहीं)।"),
    "33": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। वायु = शरीर का वात (पारिभाषिक)। "
           "सन्धि जाँची: वायुः + च → वायुश्च (विसर्ग → श् च से पहले); च + अनुलोमः → चानुलोमः (अ + अ → आ)।"),
    "34": ("गद्य; विश्वास मध्यम। पाठ-चिह्न: छपा ‘मार्ग’ = मार्गम् (अनुस्वार छूटा; ‘प्रतिपद्यते’ के साथ द्वितीया चाहिए) — इस पर प्रश्न नहीं। "
           "जरायु = गर्भ की झिल्लियाँ/अपरा (मानक); बाहर आता है या नहीं, नहीं कहा। "
           "सन्धि जाँची: मूत्रपुरीषम् + च → मूत्रपुरीषं च; जरायुः + च → जरायुश्च।"),
    "35": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। ‘पुत्रम्’ = पुत्र (सन्तान नहीं)। बलवती = बल वाली स्त्री, कर्ता। काले = प्रसव का उचित समय। "
           "सन्धि जाँची: च + इष्टम् → चेष्टम् (अ + इ → ए); कल्यम् + आयुष्मन्तम् → कल्यमायुष्मन्तम्; छपा ‘आयुष्मंतं’ = आयुष्मन्तम्।"),
    "36": ("गद्य; विश्वास निम्न। लम्बे समास में ‘फंफेणा’ अविभक्त और अज्ञात; ‘पत्रभंग’ अस्पष्ट (टूटे पत्ते, या भङ्गा = भाँग; कोई पक्का पाठ नहीं) — "
           "इन पर प्रश्न नहीं। पहचान डेटा के अनुसार: बिल्व = बेल, कार्पासी = कपास, पाटली = पाढ़ल, पिचुमन्द = नीम (मानक); "
           "अग्निमन्थ = प्रेम्ना (सम्भावित); मांसी = जटामांसी (सम्भावित); वर्धमानक = विवादित (शायद अरण्ड)। "
           "‘गर्भिण्याः’ षष्ठी, ‘के लिए’ के अर्थ में। सन्धि जाँची: सर्वगन्ध + उदकेन → सर्वगन्धोदकेन (अ + उ → ओ); "
           "स्नानम् + उपदिशेत् → स्नानमुपदिशेत्।"),
    "37": ("गद्य; विश्वास निम्न। पाठ-चिह्न: ‘चैवास्या’ = चैवास्याः (विसर्ग छूटा, जैसा इकाई 29 में); ‘अपृतता’ कोई शब्द नहीं, ‘अपहृत’ "
           "(हटाए गए) अनुमानित; ‘उपृतत्’ कोई शब्द नहीं, ‘उपहृत’ (लाए गए) अनुमानित — इन पर प्रश्न नहीं। द्वार पूर्व या उत्तर, जैसा छपा। "
           "सन्धि जाँची: च + एव → चैव (अ + ए → ऐ); एव + अस्याः → एवास्याः; नवमात् + मासात् → नवमान्मासात् (त् → न् अनुनासिक से पहले, "
           "विकल्प से; यहाँ न् छपा); सर्व + ऋतु → सर्वर्तु (अ + ऋ → अर्); सर्व + उपकरण → सर्वोपकरण (अ + उ → ओ); "
           "प्राक् + द्वारम् → प्राग्द्वारम्, उदक् + द्वारम् → उदग्द्वारम् (क् → ग् घोष से पहले); सूतिका + अगार → सूतिकागार (आ + अ → आ)।"),
    "38": ("गद्य; विश्वास निम्न; लम्बा, बिगड़ा वाक्य। पाठ-चिह्न: ‘वृद्धान्त्वाऽऽवर्तमाना’ = वृद्धान् तु आवर्तमाना (अर्थ पक्का नहीं); "
           "‘परितृता’ = सम्भवतः परिवृता (त्र/व्र भ्रम); ‘नेरा’ = नैरा, ‘म्त्र’ = मूत्र (सुझाया पाठ); ‘अनुक्ताभिः’, ‘अविपादाभिः’ अस्पष्ट "
           "(शायद अनुरक्ताभिः, अविपन्नाभिः) — इन सब पर प्रश्न नहीं। ‘बहुशः’ छपाई में ‘प्रविश्य’ से सटा है, डेटा इसे ‘प्रसूताभिः’ से जोड़ता है। "
           "सन्धि जाँची: तत्र + अनुकूलेषु → तत्रानुकूलेषु (अ + अ → आ); स्वस्ति + अयन → स्वस्त्ययन (इ + अ → य); "
           "प्रसवकालम् + उदीक्षेत → प्रसवकालमुदीक्षेत।"),
}

# ===================================================================== AIDS
AIDS = {
    "27": {
        "chain": {"steps": ["मधुक आदि मधुर औषध", "उनसे पका तेल", "अनुवासन (तेल की बस्ति)", "वायु का अनुलोमन"]},
        "chunks": "पुराणविद्विश्शुत्त्यर्थं (?) | मधुकादिमधुरौषधसिद्धेन च | तैलेनानुवासयेत् | अनुलोमनाय वायोः",
        "sandhi": ("अ + औ → औ: मधुर + औषध → मधुरौषध · अ + अ → आ: तैलेन + अनुवासयेत् → तैलेनानुवासयेत् · "
                   "त् → द् स्वर से पहले: अनुवासयेत् + अनुलोमनाय → अनुवासयेदनुलोमनाय।"),
        "frame": "किससे (मधुकादि-सिद्ध तैलेन) → क्रिया (अनुवासयेत्) → किसलिए (अनुलोमनाय वायोः, चतुर्थी)।",
    },
    "28": {
        "chain": {"steps": ["वायु अनुलोम", "सुख से, उपद्रव-रहित प्रसव"]},
        "chunks": "अनुलोमे हि मारुते | सुखमनुपद्रवा प्रसूते | गर्भिणीं तु न्युब्जाम् | आस्थापयेद् अनुवासयेद्वा",
        "sandhi": ("म् + स्वर: सुखम् + अनुपद्रवा → सुखमनुपद्रवा · त् → द्: आस्थापयेत् + अनुवासयेत् → आस्थापयेदनुवासयेत्, "
                   "अनुवासयेत् + वा → अनुवासयेद्वा।"),
        "frame": "कारण (हि: वायु अनुलोम हो तो सुख-प्रसव) → विधि (गर्भिणी न्युब्जा → आस्थापन या अनुवासन)।",
    },
    "29": {
        "chunks": "तथा ऽस्या | विवृतमार्गतया | सम्यगौषधम् | अनुप्रविशति",
        "sandhi": ("आ + अ → आ (ऽ चिह्न): तथा + अस्याः → तथाऽस्याः · क् → ग् स्वर से पहले: सम्यक् + औषधम् → सम्यगौषधम्।"),
        "frame": "कारण (विवृतमार्गतया, तृतीया) → फल (औषध सम्यक् अनुप्रविशति)।",
    },
    "30": {
        "diagram": {"groups": [
            {"label": "कब", "items": ["इसके बाद (अतः ऊर्ध्वम्)", "प्रसव के समय तक"]},
            {"label": "किससे", "items": ["स्निग्ध यवागू", "जाङ्गल जीवों का रस"]},
            {"label": "मत", "items": ["भगवान् धन्वन्तरि"]}]},
        "chunks": "अतऊर्ध्वं | स्निग्धाभिर्यवागूभिः | जाङ्गलरसैश्च | उपाचरेत् | आप्रसवकालात् | इति भगवान् धन्वन्तरिः",
        "sandhi": ("अः → अ (अ से भिन्न स्वर से पहले): अतः + ऊर्ध्वम् → अत ऊर्ध्वम् · इः/ऊः → इर्/ऊर् घोष से पहले: "
                   "स्निग्धाभिः + यवागूभिः → स्निग्धाभिर्यवागूभिः · ः + च → श्च: रसैः + च → रसैश्च · त् → द्: कालात् + इति → कालादिति।"),
    },
    "31": {
        "chain": {"steps": ["नवाँ मास", "वही अनुवासन-तेल", "पिचु (रुई का फाहा)", "योनि में रखे",
                            "गर्भमार्ग व आशय का स्नेहन (सुझाया पाठ)"]},
        "chunks": "नवमे तु | तत एवानुवासनतैलात् | पिचुं योनौ प्रणयेत् | गर्भमार्गाशाययोः | स्नेहनाथंमिति (= स्नेहनार्थम् इति?)",
        "sandhi": ("अः → अ: ततः + एव → तत एव · अ + अ → आ: एव + अनुवासन → एवानुवासन · म् → ं व्यञ्जन से पहले: पिचुम् + योनौ → पिचुं योनौ।"),
        "anchors": "याद-सूत्र: आठवें में बस्ति, नवें में पिचु — तेल वही। (मेरी याद-पद्धति)",
    },
    "32": {
        "diagram": {"groups": [
            {"label": "कब से, कैसे", "items": ["पहले मास से आरम्भ", "क्रम से"]},
            {"label": "प्रसव काल में मृदु (क्रम से)", "items": ["कुक्षि", "कटी", "पार्श्व", "पृष्ठ"]}]},
        "chunks": "अनेन | प्रथममासादारभ्य | क्रमेण | गर्भिण्याः प्रसवकाले | गर्भधारिणीकुक्षिकटीपार्श्वपृष्ठं | मृदु भवति",
        "sandhi": "त् → द् स्वर से पहले: प्रथममासात् + आरभ्य → प्रथममासादारभ्य।",
        "pegs": "मेरा बनाया चित्र: नीचे से ऊपर हाथ फेरें — पेट (कुक्षि), कमर (कटी), बगल (पार्श्व), पीठ (पृष्ठ), सब नरम। (केवल याद के लिए, ग्रन्थ का दावा नहीं)",
    },
    "33": {
        "chunks": "वायुश्चानुलोमः | संपद्यते",
        "sandhi": "ः + च → श्च: वायुः + च → वायुश्च · अ + अ → आ: च + अनुलोमः → चानुलोमः।",
        "frame": "कर्ता (वायुः) + विधेय (अनुलोमः) + क्रिया (संपद्यते, हो जाता है); ‘च’ पिछले फल से जोड़ता है।",
    },
    "34": {
        "chunks": "मूत्रपुरीषं च | प्रकृतिभूतं | जरायुश्च | मार्ग (= मार्गम्?) | प्रतिपद्यते",
        "sandhi": "ः + च → श्च: जरायुः + च → जरायुश्च · म् → ं व्यञ्जन से पहले: मूत्रपुरीषम् + च → मूत्रपुरीषं च।",
        "frame": "दो फल: (१) मूत्रपुरीषम् — प्रकृतिभूतम् (क्रिया समझी जाती है); (२) जरायुः — मार्गं प्रतिपद्यते।",
    },
    "35": {
        "chunks": "पुत्रं चेष्टं कल्यमायुष्मंतं सुखिनं | सुखेन काले | बलवती प्रसूते",
        "sandhi": "अ + इ → ए: च + इष्टम् → चेष्टम् · म् + स्वर: कल्यम् + आयुष्मन्तम् → कल्यमायुष्मन्तम्।",
        "frame": "कर्म (पुत्रम् + चार विशेषण) → कैसे (सुखेन) → कब (काले) → कर्ता (बलवती) → क्रिया (प्रसूते)।",
        "letters": "पुत्र के चार गुण, पहले अक्षर: इ-क-आ-सु (इष्ट, कल्य, आयुष्मान्, सुखी)। (केवल सुनने की सहायता)",
    },
    "36": {
        "diagram": {"groups": [
            {"label": "शीत क्वाथ के द्रव्य (क्रम से)", "items": ["बिल्व (बेल, मानक)", "कार्पासी (कपास, मानक)", "फंफेणा (अज्ञात)",
                                                       "पाटली (पाढ़ल, मानक)", "पिचुमन्द (नीम, मानक)",
                                                       "अग्निमन्थ (प्रेम्ना, सम्भावित)", "मांसी (जटामांसी, सम्भावित)",
                                                       "वर्धमानक (विवादित)", "पत्रभंग (अस्पष्ट)"]},
            {"label": "या", "items": ["सर्वगन्धोदक (सब सुगन्धित द्रव्यों का जल)"]}]},
        "chunks": "बिल्व… पत्रभंगक्वाथेन | शीतेन | सर्वगंधोदकेन वा | गर्भिण्याः | प्रत्यहं | स्नानमुपदिशेत्",
        "sandhi": "अ + उ → ओ: सर्वगन्ध + उदकेन → सर्वगन्धोदकेन · म् + स्वर: स्नानम् + उपदिशेत् → स्नानमुपदिशेत्।",
    },
    "37": {
        "diagram": {"groups": [
            {"label": "कब", "items": ["नवें मास से पहले"]},
            {"label": "स्थान", "items": ["प्रशस्त देश", "हड्डी-कंकड़-ठीकरे हटे (अनुमानित पाठ)"]},
            {"label": "सूतिकागार", "items": ["वास्तुविद्या से प्रशस्त", "सब ऋतुओं में सुखद", "सब उपकरण (अनुमानित पाठ)",
                                         "अग्नि पास में", "पूर्व या उत्तर द्वार"]}]},
        "chunks": ("प्राक् चैवास्या नवमान्मासात् | अपृतता(?)स्थिशर्कराकपाले प्रशस्ते देशे | वास्तुविद्याप्रशस्तं | सर्वर्तुसुखम् | "
                   "उपृतत्(?)सर्वोपकरणं | सन्निहितज्वलनं | प्राग्द्वारमुदग्द्वारं वा | सूतिकागारं कारयेत्"),
        "sandhi": ("अ + ए → ऐ: च + एव → चैव · अ + ऋ → अर्: सर्व + ऋतु → सर्वर्तु · क् → ग् घोष से पहले: प्राक् + द्वारम् → "
                   "प्राग्द्वारम्, उदक् + द्वारम् → उदग्द्वारम् · आ + अ → आ: सूतिका + अगार → सूतिकागार।"),
        "contrast": "‘प्राक्’ दो बार, दो अर्थ: पञ्चमी के साथ ‘पहले’ (प्राक् नवमान्मासात्) — समास में ‘पूर्व दिशा’ (प्राग्द्वारम्)।",
    },
    "38": {
        "chain": {"steps": ["१ नक्षत्र आदि अनुकूल", "२ पुण्याह-वचन", "३ प्रवेश", "४ अनुभवी, क्लेश-सहिष्णु स्त्रियाँ साथ",
                            "५ स्वस्त्ययन में लगी", "६ प्रसव-काल की प्रतीक्षा"]},
        "chunks": ("तत्रानुकूलेषु नक्षत्रादिषु | पुण्याहशब्देन | गोब्राह्मणवृद्धांत्वाऽऽवर्तमाना (?) प्रदक्षिणं | प्रविश्य | बहुशः प्रसूताभिः | "
                   "अनुक्ताभिरविपादाभिः (?) | क्लेशक्षमाभिः परितृता (= परिवृता?) | स्वस्त्ययनपरा | "
                   "अनुलोमनैराहारविहारैः (सुझाया) अनुलोमितवातमूत्रपुरीषा | प्रसवकालमुदीक्षेत"),
        "sandhi": "अ + अ → आ: तत्र + अनुकूलेषु → तत्रानुकूलेषु · इ + अ → य: स्वस्ति + अयन → स्वस्त्ययन · म् + स्वर: प्रसवकालम् + उदीक्षेत → प्रसवकालमुदीक्षेत।",
    },
}

# ===================================================================== IMAGE_SPECS
IMAGE_SPECS = {
    ("28", "chain"): {
        "file": "sh3-anuloma-prasava-28.svg",
        "alt": ("Two small flowcharts of unit 28: when the wind moves downward, she gives birth easily and free of "
                "complications; the pregnant woman, face down, is given an āsthāpana or an anuvāsana."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"वायु अनुलोम\"] --> B[\"सुख से, उपद्रव-रहित प्रसव\"]\n"
                 "  C[\"गर्भिणी न्युब्जा (औंधी)\"] --> D[\"आस्थापन\"]\n"
                 "  C -->|\"या\"| E[\"अनुवासन\"]\n"),
    },
    ("30", "diagram"): {
        "file": "sh3-yavagu-jangala-30.svg",
        "alt": ("Table of unit 30: from after this until the time of delivery, treatment with unctuous gruels and with "
                "broths of dry-land (jāṅgala) animals; the view of the venerable Dhanvantari."),
        "type": "table",
        "title": "प्रसव तक का उपचार (इकाई ३०)",
        "heads": ["प्रश्न", "पाठ का उत्तर"],
        "rows": [["कब से", "इसके बाद (अतः ऊर्ध्वम्)"], ["कब तक", "प्रसव के समय तक"],
                 ["उपचार १", "स्निग्ध यवागू"], ["उपचार २", "जाङ्गल जीवों का रस"], ["मत", "भगवान् धन्वन्तरि"]],
    },
    ("31", "chain"): {
        "file": "sh3-picu-navame-31.svg",
        "alt": ("Flowchart of unit 31: in the ninth month, the same anuvāsana oil, a picu (cotton swab), placed in the "
                "yoni, for oiling the embryo's passage and the āśaya (suggested reading)."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"नवाँ मास\"] --> B[\"वही अनुवासन-तेल\"]\n"
                 "  B --> C[\"पिचु (रुई का फाहा)\"]\n"
                 "  C --> D[\"योनि में रखे\"]\n"
                 "  D --> E[\"मार्ग-आशय का स्नेहन (?)\"]\n"),
    },
    ("32", "diagram"): {
        "file": "sh3-mridu-anga-32.svg",
        "alt": ("Flowchart of unit 32: beginning from the first month, step by step, at the time of delivery four parts "
                "become soft, numbered in the text's order: 1 belly, 2 waist, 3 flank, 4 back."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"पहले मास से आरम्भ\"] --> B[\"क्रम से\"]\n"
                 "  B --> C[\"प्रसव काल में मृदु\"]\n"
                 "  C --> D[\"१ कुक्षि\"]\n"
                 "  C --> E[\"२ कटी\"]\n"
                 "  C --> F[\"३ पार्श्व\"]\n"
                 "  C --> G[\"४ पृष्ठ\"]\n"),
    },
    ("36", "diagram"): {
        "file": "sh3-snana-kvatha-36.svg",
        "alt": ("Table of unit 36: the nine items of the cooled decoction in the compound's order with the data's labels "
                "(bilva bael, kārpāsī cotton, pāṭalī, picumanda neem: standard; phaṃpheṇā unidentified; agnimantha "
                "Premna and māṃsī spikenard: probable; vardhamānaka disputed; patrabhaṅga unclear), or water of all "
                "fragrant substances, for a daily bath."),
        "type": "table",
        "title": "प्रतिदिन स्नान: शीत क्वाथ (इकाई ३६)",
        "heads": ["द्रव्य (क्रम से)", "पहचान (डेटा का लेबल)"],
        "rows": [["बिल्व", "बेल (मानक)"], ["कार्पासी", "कपास (मानक)"], ["फंफेणा", "अज्ञात"],
                 ["पाटली", "पाढ़ल (मानक)"], ["पिचुमन्द", "नीम (मानक)"], ["अग्निमन्थ", "प्रेम्ना, अरणी (सम्भावित)"],
                 ["मांसी", "जटामांसी (सम्भावित)"], ["वर्धमानक", "विवादित (शायद अरण्ड)"], ["पत्रभंग", "अस्पष्ट"],
                 ["या: सर्वगन्धोदक", "सब सुगन्धित द्रव्यों का जल"]],
    },
    ("37", "diagram"): {
        "file": "sh3-sutikagara-37.svg",
        "alt": ("Two columns for unit 37, built before the ninth month: the place (approved; free of bones, gravel and "
                "potsherds on a conjectural reading) and the delivery chamber (approved by vāstu-vidyā, comfortable in "
                "all seasons, all equipment on a conjectural reading, fire at hand, east or north door)."),
        "type": "split",
        "title": "नवें मास से पहले: सूतिकागार (इकाई ३७)",
        "cols": [["स्थान", ["प्रशस्त देश", "हड्डी-कंकड़-ठीकरे हटे (अनुमानित)"]],
                 ["सूतिकागार", ["वास्तुविद्या से प्रशस्त", "सब ऋतुओं में सुखद", "सब उपकरण (अनुमानित)",
                                 "अग्नि पास में", "पूर्व या उत्तर द्वार"]]],
    },
}
