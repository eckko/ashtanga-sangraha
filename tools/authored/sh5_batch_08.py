from helpers import mcq, match, order, fill, multi, accepts


AUTHORED = {}

# ---------------------------------------------------------------- unit 90
AUTHORED["90"] = {
    "title": "दश प्राणायतनानि",
    "question": "By unit 90, which ten seats of life (prāṇāyatana) are named?",
    "rule": ("There are ten seats of life (प्राणायतन): the head (मूर्धन्), the jihvābandhana (tongue-binding), the throat, "
             "the heart, the navel, the bladder (बस्ति), the gūda (anus, rectum), śukra (semen), ojas and blood."),
    "limits": ("A prose line. What जिह्वाबन्धन is (root of the tongue or the frenulum) is not settled, and कण्ठ may be throat "
               "or neck: no question asks what either one is. Ojas is kept as a doctrinal term. The line does not say why "
               "these are seats of life."),
    "explain_hi": ("यह गद्य-पंक्ति प्राण के दस आयतन यानी आश्रय-स्थान गिनाती है। "
                   "क्रम से: मूर्धा (सिर), जिह्वाबन्धन (जीभ का बन्धन), कण्ठ, हृदय, नाभि, बस्ति (मूत्राशय), गूद (गुदा; छपा और डेटा का रूप ‘गूद’, सामान्य शब्द ‘गुद’), "
                   "शुक्र (वीर्य), ओज और रक्त। "
                   "जिह्वाबन्धन का ठीक अर्थ (जीभ की जड़ या जीभ के नीचे का बन्धन) तय नहीं, और कण्ठ गला या गर्दन हो सकता है। "
                   "ओज शास्त्रीय शब्द है, इसका कोई आधुनिक पर्याय नहीं रखा गया। "
                   "अगली इकाई (९१) बताती है कि इनमें पहले सात महामर्म कहलाते हैं।"),
    "hook": "सिर से रक्त तक: प्राण के दस घर।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 90, how many seats of life (prāṇāyatana) are there?",
            ("Ten (दश)", "दश प्राणायतनानि: ten seats of life."),
            [("Seven (सप्त)", "Seven is the number of the first ones called mahāmarma in unit 91, not of all the seats."),
             ("Sixteen (षोडश)", "Sixteen is the count of the kaṇḍarās in unit 92."),
             ("Fourteen (चतुर्दश)", "Fourteen is the count of the bone assemblages in unit 98.")],
            "The line opens: दश प्राणायतनानि, ten seats of life.",
            "दश प्राणायतनानि = ten seats of life."),
        order(1, "Put the first six seats of life of unit 90 in the line's order.",
              ["मूर्धा", "जिह्वाबन्धन", "कण्ठ", "हृदय", "नाभि", "बस्ति"],
              "Head, tongue-binding, throat, heart, navel, bladder; then gūda, śukra, ojas and blood follow.",
              "मूर्धा → जिह्वाबन्धन → कण्ठ → हृदय → नाभि → बस्ति."),
        match(2, "Match each seat of life of unit 90 to its meaning.",
              [["मूर्धन्", "head"], ["नाभि", "navel"], ["बस्ति", "bladder"], ["गूद", "anus, rectum"], ["शुक्र", "semen"]],
              "Five of the ten seats: head, navel, bladder, gūda (anus, rectum), śukra (semen).",
              "मूर्धन्, नाभि, बस्ति, गूद, शुक्र.", role="extend",
              teaches="प्राणायतन = प्राण (life) + आयतन (seat, abode): a seat of life."),
        mcq("discriminate", 3, "Which split of नाभिर्बस्तिर्गूदः is right?",
            ("नाभिः + बस्तिः + गूदः", "Each visarga after इ becomes र् before the voiced consonants ब and ग."),
            [("नाभी + बस्ती + गूदः", "A long ई before a consonant gives no र्; the र् shows a visarga after short इ."),
             ("नाभिः + र्बस्तिः + र्गूदः", "र्बस्तिः is not a word; the र् is the changed visarga of the word before."),
             ("नाभि + अस्तिः + गूदः", "अस्ति is not one of the seats, and no ब would appear from इ + अ.")],
            "नाभिः (navel) + बस्तिः (bladder) + गूदः (anus): इः + voiced consonant → इर्.",
            "इः + voiced consonant → इर्."),
        multi("apply", 4, "Which of these does unit 90 name among the ten seats of life?",
              [("Blood (रक्त)", "Right: रक्तम् is the last of the ten."),
               ("Liver (यकृत्)", "The liver is not in the list of unit 90."),
               ("Navel (नाभि)", "Right: नाभिः is the fifth of the ten."),
               ("Kidney (वृक्क)", "The kidney is not in the list of unit 90.")],
              [0, 2],
              "The ten are head, tongue-binding, throat, heart, navel, bladder, gūda, śukra, ojas and blood.",
              "मूर्धा जिह्वाबन्धनं कण्ठो हृदयं नाभिर्बस्तिर्गूदः शुक्रमोजो रक्तम्."),
        mcq("transfer", 5, "By the rule of नाभिर्बस्तिः, how is अग्निः + दहति (fire burns) joined?",
            ("अग्निर्दहति", "A visarga after इ before a voiced consonant becomes र्, as नाभिः + बस्तिः."),
            [("अग्नो दहति", "ओ comes from अः before a voiced consonant, not from इः."),
             ("अग्निश्दहति", "द is voiced; before it the visarga after इ becomes र्, not श्."),
             ("अग्निः दहति", "Before a voiced consonant the visarga after इ does not stay; it becomes र्.")],
            "अग्निः + दहति = अग्निर्दहति, like नाभिः + बस्तिः = नाभिर्बस्तिः.",
            "इः + voiced consonant → इर्.",
            teaches="A visarga after a vowel other than अ/आ becomes र् before a voiced sound: नाभिः + बस्तिः → नाभिर्बस्तिः."),
    ],
}

# ---------------------------------------------------------------- unit 91
AUTHORED["91"] = {
    "title": "एषामाद्यानि सप्त पुनर्महामर्मसंज्ञानि",
    "question": "By unit 91, what are the first seven seats of life called?",
    "rule": ("Of these (एषाम्), the first (आद्यानि) seven, again (पुनः), are named mahāmarma (महामर्मसंज्ञानि): great "
             "marmas, marma being a vital point of the body."),
    "limits": ("A prose line; the copula is understood. Which seven are 'first' follows the order of unit 90 (head to gūda); "
               "the data calls this the reader's inference, so no question asks whether a given item is a mahāmarma. "
               "Marma is kept as a doctrinal term."),
    "explain_hi": ("यह गद्य-पंक्ति इकाई ९० के दस प्राणायतनों पर एक बात जोड़ती है। "
                   "इनमें (एषाम्) पहले (आद्यानि) सात फिर (पुनः) महामर्म नाम वाले (महामर्मसंज्ञानि) हैं। "
                   "मर्म शरीर का प्राण-स्थान यानी नाज़ुक बिन्दु है; यह शास्त्रीय शब्द वैसे ही रखा गया है। "
                   "इकाई ९० के क्रम से पहले सात मूर्धा से गूद तक होंगे, पर यह पाठक का अनुमान है; पंक्ति स्वयं नाम नहीं गिनाती।"),
    "hook": "दस में पहले सात: महामर्म।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 91, what are the first seven of the ten called?",
            ("Mahāmarma, the great marmas", "महामर्मसंज्ञानि: named mahāmarma."),
            [("Kaṇḍarā, the large tendons", "The kaṇḍarās are counted in unit 92; they are not these seven."),
             ("Jāla, the nets or meshes", "The jālas are described in unit 93."),
             ("Sīvanī, the probable sutures", "The sīvanīs are counted in unit 96.")],
            "The first seven are named mahāmarma.",
            "एषाम् आद्यानि सप्त महामर्मसंज्ञानि."),
        order(1, "Put the words of unit 91 in the line's order.",
              ["एषाम्", "आद्यानि", "सप्त", "पुनः", "महामर्मसंज्ञानि"],
              "Of these, the first seven, again, are named mahāmarma.",
              "एषाम् → आद्यानि → सप्त → पुनः → महामर्मसंज्ञानि."),
        match(2, "Match each word of unit 91 to its meaning.",
              [["एषाम्", "of these"], ["आद्य", "first"], ["सप्त", "seven"], ["पुनः", "again"],
               ["संज्ञा", "name (in -संज्ञानि, named)"]],
              "Of these, the first seven, again, are named mahāmarma.",
              "एषाम्, आद्य, सप्त, पुनः, संज्ञा.", role="extend",
              teaches="-संज्ञ at the end of a compound means 'having the name': महामर्मसंज्ञानि = named mahāmarma."),
        mcq("discriminate", 3, "Which split of एषामाद्यानि is right?",
            ("एषाम् + आद्यानि", "The final म् simply joins the following vowel: एषाम् + आद्यानि → एषामाद्यानि."),
            [("एषा + माद्यानि", "माद्यानि is not the word; the word is आद्यानि (first)."),
             ("एषाम् + अद्यानि", "म् + अ would give एषामद्यानि, with a short अ, not मा."),
             ("एषामा + आद्यानि", "एषामा is not a form; the pronoun is एषाम् (of these).")],
            "एषाम् (of these) + आद्यानि (first): म् + आ → मा.",
            "Final म् + vowel → the म् joins the vowel."),
        mcq("apply", 4, "By unit 91, what does एषाम् (of these) refer to?",
            ("The ten seats of life of unit 90", "Right after the ten seats of life: of these, the first seven."),
            [("The sixteen kaṇḍarās of unit 92", "The kaṇḍarās come after unit 91, not before it."),
             ("The seven sīvanīs of unit 96", "The sīvanīs come later, in unit 96."),
             ("The fourteen bone groups of unit 98", "The bone groups come later, in unit 98.")],
            "एषाम् points back to the ten prāṇāyatanas just listed in unit 90.",
            "एषाम् = of these (the ten of unit 90)."),
        mcq("transfer", 5, "By the rule of एषामाद्यानि, how is फलम् + अस्ति (there is a fruit) joined?",
            ("फलमस्ति", "Final म् joins the following vowel, as एषाम् + आद्यानि."),
            [("फलंस्ति", "The anusvāra stands for म् only before a consonant, not before a vowel."),
             ("फलमास्ति", "म् + अ keeps the short अ; nothing lengthens it."),
             ("फलोऽस्ति", "ओऽ comes from अः + अ, not from अम् + अ.")],
            "फलम् + अस्ति = फलमस्ति, like एषाम् + आद्यानि = एषामाद्यानि.",
            "Final म् + vowel → the म् joins the vowel.",
            teaches="A final म् before a vowel is not changed; it joins that vowel: एषाम् + आद्यानि → एषामाद्यानि."),
    ],
}

# ---------------------------------------------------------------- unit 92
AUTHORED["92"] = {
    "title": "षोडश कंडराः",
    "question": "By unit 92, how many kaṇḍarās are there, and where are they placed?",
    "rule": ("There are sixteen kaṇḍarās (कण्डरा, large tendons, standard); of them two each (द्वे द्वे) in the hands and "
             "feet (करचरणेषु), and four, separately (पृथक्), in the neck and the back."),
    "limits": ("A prose line; the copula is understood. Whether 'four' means four in each of neck and back (which makes "
               "sixteen) or four in both together is not stated: no question rests on it or on the sum. The printed "
               "पृथकग्रीवा is kept."),
    "explain_hi": ("यह गद्य-पंक्ति बताती है कि कण्डराएँ (बड़े टेण्डन, मानक पहचान) सोलह हैं। "
                   "उनमें से हाथों और पैरों में दो-दो (द्वे द्वे; संख्या को दोहराना ‘हर एक में’ का भाव देता है)। "
                   "गर्दन और पीठ में चार हैं, अलग-अलग (चतस्रः पृथक्)। "
                   "यह चार गर्दन और पीठ प्रत्येक में है या दोनों में मिलाकर, पंक्ति स्पष्ट नहीं कहती; प्रत्येक में चार मानें तभी "
                   "जोड़ सोलह बनता है। इसलिए इस जोड़ पर कोई प्रश्न नहीं।"),
    "hook": "सोलह कण्डरा: हाथ-पैर में दो-दो, गर्दन-पीठ में चार।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 92, how many kaṇḍarās (large tendons) are there?",
            ("Sixteen (षोडश)", "षोडश कण्डराः: sixteen kaṇḍarās."),
            [("Fourteen (चतुर्दश)", "Fourteen is the count of the bone assemblages in unit 98."),
             ("Six (षट्)", "Six is the count of the kūrcas in unit 94."),
             ("Seven (सप्त)", "Seven is the count of the sīvanīs in unit 96.")],
            "The line opens: षोडश कण्डराः, sixteen kaṇḍarās.",
            "षोडश कण्डराः = sixteen kaṇḍarās."),
        order(1, "Put these phrases of unit 92 in the line's order.",
              ["षोडश कंडराः", "तासां", "द्वे द्वे करचरणेषु", "चतस्रः पृथक", "ग्रीवापृष्ठयोः"],
              "Sixteen kaṇḍarās; of them, two each in the hands and feet; four, separately, in the neck and the back.",
              "षोडश कंडराः → तासां → द्वे द्वे करचरणेषु → चतस्रः पृथक → ग्रीवापृष्ठयोः."),
        match(2, "Match each word of unit 92 to its meaning.",
              [["कर", "hand"], ["चरण", "foot"], ["ग्रीवा", "neck"], ["पृष्ठ", "back"], ["पृथक्", "separately"]],
              "Two each in the hands and feet; four, separately, in the neck and the back.",
              "कर, चरण, ग्रीवा, पृष्ठ, पृथक्.", role="extend",
              teaches="करचरणेषु is a dvandva in the locative plural: in the hands and feet."),
        mcq("discriminate", 3, "In unit 92, what does the repeated द्वे द्वे express?",
            ("Two each, in every hand and foot", "A repeated numeral is distributive: two each."),
            [("Two in all, for hands and feet", "Repeating the numeral gives 'two each', not one total of two."),
             ("Two in the hands, two in the neck", "द्वे द्वे goes with करचरणेषु; the neck has its own number, four."),
             ("Twice as many as in the back", "No comparison with the back is made; द्वे द्वे means two each.")],
            "द्वे द्वे करचरणेषु = two each in the hands and feet.",
            "Repeated numeral = distributive (each)."),
        mcq("apply", 4, "By unit 92, where are the four (चतस्रः) kaṇḍarās placed?",
            ("In the neck and the back", "चतस्रः पृथक् ग्रीवापृष्ठयोः: four, separately, in the neck and the back."),
            [("In the hands and the feet", "The hands and feet have two each (द्वे द्वे)."),
             ("In the head and the tongue", "The head and tongue are places of the sīvanīs in unit 96."),
             ("In the ankle and the wrist", "The ankle and wrist are places of the jālas in unit 93.")],
            "Four, separately, are in the neck and the back.",
            "चतस्रः पृथक् ग्रीवापृष्ठयोः."),
        mcq("transfer", 5, "By the pattern of द्वे द्वे, what does a new example पञ्च पञ्च फलानि ददाति mean?",
            ("He gives five fruits to each", "A repeated numeral is distributive, as द्वे द्वे = two each."),
            [("He gives fifty fruits in all", "Repeating पञ्च does not make fifty; that would be पञ्चाशत्."),
             ("He gives only five fruits once", "The repetition adds 'each'; it does not stress 'only once'."),
             ("He gives the fifth fruit only", "The fifth would be the ordinal पञ्चम, not the repeated पञ्च.")],
            "पञ्च पञ्च = five each, like द्वे द्वे = two each.",
            "Repeated numeral = distributive (each).",
            teaches="A numeral said twice is distributive: द्वे द्वे करचरणेषु = two each in the hands and feet."),
    ],
}

# ---------------------------------------------------------------- unit 93
AUTHORED["93"] = {
    "title": "षोडश जालानि",
    "question": "By unit 93, of what are the jālas (nets) born, and where do they lie?",
    "rule": ("There are sixteen jālas (जाल, nets, meshes): born of flesh, vessel (सिरा), snāyu (ligament) and bone, four in "
             "each single place (एकैकत्र), at the ankle (गुल्फ) and the wrist (मणिबन्ध), lying mutually latticed."),
    "limits": ("A prose line. Jāla has no firm modern equivalent. That the four kinds are the four at each site, and that four "
               "sites make sixteen, is the data's reading, not stated: no question asks the sum. 'Latticed' "
               "(परस्परगवाक्षित) is kept literal."),
    "explain_hi": ("यह गद्य-पंक्ति सोलह जालों (जाल, यानी जाली जैसी रचना) का वर्णन करती है। "
                   "वे मांस, सिरा, स्नायु और अस्थि से उत्पन्न हैं, और हर एक स्थान पर (एकैकत्र) चार हैं: "
                   "गुल्फ यानी टखने में और मणिबन्ध यानी कलाई में। "
                   "वे परस्पर गवाक्षित, यानी झरोखे की जाली की तरह आपस में गुँथे हुए, स्थित हैं। "
                   "चार प्रकार ही हर स्थान के चार हैं, और दो टखने व दो कलाइयाँ मिलकर सोलह बनाते हैं: यह डेटा का अर्थ-निर्णय है, "
                   "पंक्ति में जोड़ नहीं लिखा।"),
    "hook": "टखने-कलाई में चार-चार जाल, झरोखे-सी बुनावट।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 93, where are the jālas (nets) situated?",
            ("At the ankle and the wrist", "गुल्फे मणिबन्धे च: at the ankle and the wrist."),
            [("At the neck and the back", "The neck and back hold the four kaṇḍarās of unit 92."),
             ("At the head and the tongue", "The head and tongue hold sīvanīs in unit 96."),
             ("At the knee and the groin", "The knee and groin are places of bone groups in unit 98.")],
            "The jālas lie at the ankle and the wrist.",
            "गुल्फे मणिबन्धे च."),
        order(1, "Put the four sources of the jālas in the order of मांससिरास्नाय्वस्थिजानि.",
              ["मांस", "सिरा", "स्नायु", "अस्थि"],
              "Born of flesh, vessel, snāyu and bone.",
              "मांस → सिरा → स्नायु → अस्थि."),
        match(2, "Match each word of unit 93 to its meaning.",
              [["जाल", "net, mesh"], ["गुल्फ", "ankle"], ["मणिबन्ध", "wrist"], ["परस्पर", "mutually"],
               ["गवाक्ष", "window lattice (in गवाक्षित)"]],
              "Nets at the ankle and wrist, lying mutually latticed.",
              "जाल, गुल्फ, मणिबन्ध, परस्पर, गवाक्ष.", role="extend",
              teaches="गवाक्षित = made like a gavākṣa (window lattice): interlaced."),
        mcq("discriminate", 3, "In unit 93, what does परस्परगवाक्षितानि say about the jālas?",
            ("They lie interlaced like a lattice", "गवाक्षित = made like a window lattice; परस्पर = mutually."),
            [("They lie apart and never touch", "परस्पर (mutually) with गवाक्षित means they are interwoven."),
             ("They are hollow like a lotus bud", "The lotus-bud likeness is said of the heart in unit 73."),
             ("They bind the muscles to the spine", "Binding the muscles is the work of the flesh-cords in unit 95.")],
            "The jālas are situated mutually latticed, i.e. interlaced.",
            "परस्पर-गवाक्षित = mutually latticed."),
        multi("apply", 4, "Which does unit 93 name as sources of the jālas?",
              [("Fat (मेदस्)", "Fat is not among the four sources of unit 93."),
               ("Flesh (मांस)", "Right: मांस is the first of the four."),
               ("Skin (त्वच्)", "Skin is not among the four sources of unit 93."),
               ("Bone (अस्थि)", "Right: अस्थि is the last of the four.")],
              [1, 3],
              "The four sources are flesh, vessel, snāyu and bone.",
              "मांस-सिरा-स्नायु-अस्थि-जानि."),
        mcq("transfer", 5, "By the rule of स्नायु + अस्थि → स्नाय्वस्थि, how is मधु + अत्र (honey here) joined?",
            ("मध्वत्र", "उ before a different vowel becomes व्, as स्नायु + अस्थि."),
            [("मधूत्र", "उ + उ would give ऊ; here a different vowel, अ, follows."),
             ("मधोऽत्र", "ओऽ needs a word ending in ओ or अः; मधु ends in उ."),
             ("मधुत्र", "The अ of अत्र is not simply lost; उ + अ gives व.")],
            "मधु + अत्र = मध्वत्र, like स्नायु + अस्थि = स्नाय्वस्थि.",
            "उ + a different vowel → व् + that vowel.",
            teaches="उ before a different vowel becomes व्: स्नायु + अस्थि → स्नाय्वस्थि."),
    ],
}

# ---------------------------------------------------------------- unit 94
AUTHORED["94"] = {
    "title": "षट् कूर्च्चाहस्तपादग्रीवामेढ्रेषु",
    "question": "By unit 94, in which places are the six kūrcas?",
    "rule": ("There are six kūrcas (कूर्च, bundles; sense uncertain), in the hands, feet, neck and meḍhra (मेढ्र, penis, "
             "standard)."),
    "limits": ("A prose line; the copula is understood. As a body part kūrca is not firmly identified: no question asks what "
               "it is. The line does not say how the six are shared among the places: no question on that."),
    "explain_hi": ("यह छोटी गद्य-पंक्ति कहती है कि कूर्च छह हैं, और वे हाथों, पैरों, गर्दन और मेढ्र यानी शिश्न में हैं। "
                   "कूर्च का शब्दार्थ गुच्छा या पूला है; शरीर के अंग के रूप में इसकी पहचान पक्की नहीं। "
                   "छह कूर्च इन स्थानों में कैसे बँटे हैं, पंक्ति नहीं बताती। "
                   "छपाई में ‘कूर्च्चा’ और ‘हस्त...’ जुड़े हुए छपे हैं; ‘कूर्चाः’ का विसर्ग घोष व्यंजन ह से पहले लुप्त है।"),
    "hook": "छह कूर्च: हाथ, पैर, गर्दन, मेढ्र।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 94, how many kūrcas are there?",
            ("Six", "षट् कूर्चाः: six kūrcas."),
            [("Ten", "Ten is the count of the seats of life in unit 90."),
             ("Seven", "Seven is the count of the sīvanīs in unit 96."),
             ("Sixteen", "Sixteen is the count of the kaṇḍarās and of the jālas.")],
            "The line opens: षट्, six.",
            "षट् कूर्चाः = six kūrcas."),
        order(1, "Put the places of the kūrcas in the order of हस्तपादग्रीवामेढ्रेषु.",
              ["हस्त", "पाद", "ग्रीवा", "मेढ्र"],
              "In the hands, feet, neck and meḍhra.",
              "हस्त → पाद → ग्रीवा → मेढ्र."),
        match(2, "Match each place of unit 94 to its meaning.",
              [["हस्त", "hand"], ["पाद", "foot"], ["ग्रीवा", "neck"], ["मेढ्र", "penis"]],
              "The kūrcas are in the hands, feet, neck and meḍhra (penis, standard).",
              "हस्त, पाद, ग्रीवा, मेढ्र.", role="extend",
              teaches="मेढ्र = penis (standard); unit 96 uses मेहन for the same organ."),
        mcq("discriminate", 3, "In unit 94, what does the ending -एषु of ...मेढ्रेषु show?",
            ("Locative plural: in those places", "-एषु is the locative plural of an अ-stem: in the hands, feet, neck, meḍhra."),
            [("Genitive plural: of those places", "The genitive plural of an अ-stem ends in -आणाम्/-आनाम्, not -एषु."),
             ("Nominative plural: those places", "The nominative plural of an अ-stem ends in -आः or -आणि, not -एषु."),
             ("Instrumental plural: with those places", "The instrumental plural of an अ-stem ends in -ऐः, not -एषु.")],
            "हस्तपादग्रीवामेढ्रेषु = in the hands, feet, neck and meḍhra.",
            "-एषु = locative plural."),
        mcq("apply", 4, "Which place is NOT among the kūrca places of unit 94?",
            ("The head", "The head is not named in unit 94."),
            [("The neck", "ग्रीवा, the neck, is named."),
             ("The feet", "पाद, the foot, is named."),
             ("The hands", "हस्त, the hand, is named.")],
            "Unit 94 names hands, feet, neck and meḍhra; the head is not one of them.",
            "हस्त-पाद-ग्रीवा-मेढ्रेषु."),
        mcq("transfer", 5, "By the rule of कूर्चाः + हस्त..., how is अश्वाः + धावन्ति (horses run) joined?",
            ("अश्वा धावन्ति", "आः drops its visarga before a voiced consonant, as कूर्चाः + हस्त..."),
            [("अश्वो धावन्ति", "ओ comes from अः, not from आः."),
             ("अश्वार्धावन्ति", "र् comes from a visarga after vowels other than अ/आ."),
             ("अश्वाः धावन्ति", "Before a voiced consonant the visarga after आ does not stay; it drops.")],
            "अश्वाः + धावन्ति = अश्वा धावन्ति, like कूर्चाः + हस्त... = कूर्चा हस्त...",
            "आः + voiced consonant → आ (visarga dropped).",
            teaches="After आ, a visarga drops before a voiced consonant: कूर्चाः + हस्त... → कूर्चा हस्त..."),
    ],
}

# ---------------------------------------------------------------- unit 95
AUTHORED["95"] = {
    "title": "चतस्रो मांसरज्जवः",
    "question": "By unit 95, where are the four flesh-cords, and what are they for?",
    "rule": ("Four flesh-cords (मांसरज्जु) lie on both sides (उभयतः) of the spine (पृष्ठवंश), for binding the peśīs "
             "(muscles, standard); of them two are outer (बाह्ये) and two lie inside (अभ्यन्तरस्थिते)."),
    "limits": ("A prose line; the copula is understood. How many cords lie on each side of the spine is not stated: no "
               "question on it."),
    "explain_hi": ("यह गद्य-पंक्ति चार मांसरज्जुओं यानी मांस की रस्सियों का वर्णन करती है। "
                   "वे पृष्ठवंश यानी रीढ़ के दोनों ओर (उभयतः) हैं, और उनका प्रयोजन पेशियों (मांसपेशियाँ, मानक) को बाँधना है "
                   "(पेशीनिबन्धनार्थे)। "
                   "उनमें दो बाहरी (बाह्ये) हैं और दो भीतर स्थित (अभ्यन्तरस्थिते)। "
                   "हर ओर कितनी हैं, यह नहीं बताया। ‘उभयतः’ के साथ द्वितीया विभक्ति (पृष्ठवंशम्) आती है।"),
    "hook": "रीढ़ के दोनों ओर चार रस्सियाँ: दो बाहर, दो भीतर।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 95, what are the flesh-cords for?",
            ("For binding the muscles", "पेशीनिबन्धनार्थे: for the purpose of binding the peśīs (muscles)."),
            [("For carrying blood and Kapha", "Carrying Kapha and blood is said of channels (srotas) in unit 75."),
             ("For moving the tongue and eyes", "No movement of tongue or eyes is named in unit 95."),
             ("For holding the head's bones", "No bones of the head are named in unit 95.")],
            "They are there for binding the muscles.",
            "पेशीनिबन्धनार्थे = for binding the peśīs."),
        order(1, "Put these phrases of unit 95 in the line's order.",
              ["चतस्रो मांसरज्जवः", "पृष्ठवंशमुभयतः", "पेशीनिबंधनार्थे", "तासां द्वे बाह्ये", "द्वे चाभ्यंतरस्थिते"],
              "Four flesh-cords, on both sides of the spine, for binding the muscles; of them two outer, and two inside.",
              "चतस्रो मांसरज्जवः → पृष्ठवंशमुभयतः → पेशीनिबंधनार्थे → तासां द्वे बाह्ये → द्वे चाभ्यंतरस्थिते."),
        match(2, "Match each word of unit 95 to its meaning.",
              [["रज्जु", "cord, rope"], ["पृष्ठवंश", "spine"], ["उभयतः", "on both sides"], ["पेशी", "muscle"],
               ["बाह्य", "outer"]],
              "Four cords on both sides of the spine bind the muscles; two are outer.",
              "रज्जु, पृष्ठवंश, उभयतः, पेशी, बाह्य.", role="extend",
              teaches="उभयतः (on both sides) takes the accusative: पृष्ठवंशम् उभयतः = on both sides of the spine."),
        mcq("discriminate", 3, "Which split of चाभ्यंतरस्थिते is right?",
            ("च + अभ्यन्तरस्थिते", "अ + अ → आ: च + अभ्यन्तर → चाभ्यन्तर."),
            [("चे + अभ्यन्तरस्थिते", "ए + अ would give चेऽभ्यन्तर, with ए kept and ऽ."),
             ("चः + अभ्यन्तरस्थिते", "च has no visarga, and अः + अ would give चोऽभ्यन्तर."),
             ("चा + भ्यन्तरस्थिते", "भ्यन्तर is not a word; the word is अभ्यन्तर (inner).")],
            "च (and) + अभ्यन्तरस्थिते (situated inside): अ + अ → आ.",
            "अ + अ → आ."),
        mcq("apply", 4, "By unit 95, how are the four cords divided?",
            ("Two outer and two inner", "तासां द्वे बाह्ये द्वे चाभ्यन्तरस्थिते."),
            [("Two on the neck, two on the back", "Neck and back are the places of four kaṇḍarās in unit 92."),
             ("Three outer and one inner", "The line says two and two: द्वे ... द्वे."),
             ("All four inside the spine", "Two are outer (बाह्ये); they lie on both sides of the spine.")],
            "Of them, two are outer and two are situated inside.",
            "द्वे बाह्ये, द्वे अभ्यन्तरस्थिते."),
        mcq("transfer", 5, "By the rule of चतस्रो मांसरज्जवः, how is बालः + गच्छति (the boy goes) joined?",
            ("बालो गच्छति", "अः before a voiced consonant becomes ओ, as चतस्रः + मांस..."),
            [("बाला गच्छति", "The visarga drops this way after आः, but बालः ends in अः."),
             ("बालर्गच्छति", "र् comes from a visarga after vowels other than अ/आ."),
             ("बालः गच्छति", "Before a voiced consonant the visarga after अ does not stay; अः becomes ओ.")],
            "बालः + गच्छति = बालो गच्छति, like चतस्रः + मांसरज्जवः = चतस्रो मांसरज्जवः.",
            "अः + voiced consonant → ओ.",
            teaches="अः before a voiced consonant becomes ओ: चतस्रः + मांसरज्जवः → चतस्रो मांसरज्जवः."),
    ],
}

# ---------------------------------------------------------------- unit 96
AUTHORED["96"] = {
    "title": "सप्त सीवन्यः",
    "question": "By unit 96, how are the seven sīvanīs (seams) distributed?",
    "rule": ("There are seven sīvanīs (सीवनी, seams; probably sutures); of them five are in the head (शिरसि), and one each "
             "(एकैका) in the tongue and the mehana (मेहन, penis, standard): 5 + 1 + 1 = 7."),
    "limits": ("A prose line; the copula is understood. 'Suture' is a probable reading of sīvanī and stays labelled probable. "
               "The printed जिव्हा is read जिह्वा (a near-certain letter reversal); no question rests on that spelling. "
               "The sentence appears to run on into unit 97."),
    "explain_hi": ("यह गद्य-पंक्ति सात सीवनियों यानी सिलाई जैसी रेखाओं (सम्भवतः सीवन-रेखाएँ) को गिनाती है। "
                   "उनमें पाँच सिर में हैं, और जीभ तथा मेहन यानी शिश्न में एक-एक (एकैका)। "
                   "पाँच, एक और एक मिलकर सात होते हैं, जो कुल संख्या से मेल खाता है। "
                   "छपा ‘जिव्हा’ अक्षरों के उलटने की भूल है, पढ़ा ‘जिह्वा’। "
                   "अगली इकाई (९७) ‘शस्त्र से परिहार्य’ कहती है, जो डेटा के अनुसार सम्भवतः इसी वाक्य को आगे बढ़ाती है।"),
    "hook": "सात सीवनी: पाँच सिर में, एक जीभ में, एक मेहन में।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 96, how many sīvanīs (seams) are in the head?",
            ("Five", "ताः पञ्च शिरसि: of them five in the head."),
            [("Seven", "Seven is the total of all the sīvanīs, not those in the head."),
             ("One", "One each is in the tongue and the mehana, not in the head."),
             ("Four", "The line says पञ्च, five, for the head.")],
            "Five of the seven are in the head.",
            "ताः पञ्च शिरसि."),
        order(1, "Put these phrases of unit 96 in the line's order.",
              ["सप्त सीवन्यः", "ताः पंच शिरसि", "जिव्हामेहनयोः", "एकैका"],
              "Seven sīvanīs; of them five in the head; in the tongue and the mehana, one each.",
              "सप्त सीवन्यः → ताः पंच शिरसि → जिव्हामेहनयोः → एकैका."),
        match(2, "Match each word of unit 96 to its meaning.",
              [["सीवनी", "seam (probably a suture)"], ["शिरस्", "head"], ["जिह्वा", "tongue"], ["मेहन", "penis"],
               ["एकैका", "one each"]],
              "Seven seams: five in the head, one each in the tongue and the mehana.",
              "सीवनी, शिरस्, जिह्वा, मेहन, एकैका.", role="extend",
              teaches="एकैका = एक + एक → एकैक (अ + ए → ऐ), in the feminine एकैका to agree with सीवनी: 'one each'."),
        mcq("discriminate", 3, "Which split of जिव्हामेहनयोरेकैका (जिह्वामेहनयोरेकैका) is right?",
            ("जिह्वामेहनयोः + एकैका", "A visarga after ओ becomes र् before a vowel: -योः + ए → -योरे."),
            [("जिह्वामेहनयो + रेकैका", "रेकैका is not a word; the word is एकैका (one each)."),
             ("जिह्वामेहनयोर + एकैका", "-योर is not an ending; the locative dual ending is -योः."),
             ("जिह्वामेहनयौ + एकैका", "औ + ए would give -यावेकैका, with आव्, not -योरे.")],
            "जिह्वामेहनयोः (in the tongue and the mehana) + एकैका (one each).",
            "ओः + vowel → ओर्."),
        fill(4, "In unit 96, five sīvanīs are in the head: पंच ____. Type the printed word in Devanagari or in English "
                "letters (e.g. dharma).",
             accepts("शिरसि"),
             "पंच शिरसि: five in the head (शिरसि, locative of शिरस्).",
             "शिरसि is the locative singular of शिरस् (head): 'in the head'.",
             "शिरस् → शिरसि (locative: in the head).", role="apply"),
        mcq("transfer", 5, "By the rule of एक + एक → एकैक (in एकैका), how is तत्र + एव (there indeed) joined?",
            ("तत्रैव", "अ + ए → ऐ, as एक + एक → एकैक."),
            [("तत्रेव", "ए comes from अ + इ, not from अ + ए."),
             ("तत्रौव", "औ comes from अ + ओ or औ, not from अ + ए."),
             ("तत्राव", "The ए is not lost; अ + ए gives ऐ.")],
            "तत्र + एव = तत्रैव, like एक + एक = एकैक (एकैका).",
            "अ + ए → ऐ.",
            teaches="अ followed by ए joins as ऐ: एक + एक → एकैक, feminine एकैका."),
    ],
}

# ---------------------------------------------------------------- unit 97
AUTHORED["97"] = {
    "title": "परिहार्य्याश्च शस्त्रेण",
    "question": "By unit 97, with what is something to be spared (परिहार्य), and what form is परिहार्य?",
    "rule": ("And (they are) to be avoided (परिहार्याः, a gerundive of परि-√हृ) with the śastra (शस्त्रेण: blade, surgical "
             "instrument). The subject is not named here; the line appears to continue unit 96."),
    "limits": ("A prose fragment. The subject is not stated in this unit; the data presumes the sīvanīs of unit 96 and does "
               "not supply it: no question asks what is to be avoided. 'Spared from the cut' is the natural sense."),
    "explain_hi": ("यह छोटा गद्य-अंश कहता है: और शस्त्र से परिहार्य, यानी बचाने योग्य। "
                   "‘परिहार्याः’ परि-√हृ का कृत्य-रूप है: जिसे टालना या बचाना चाहिए। "
                   "‘शस्त्रेण’ तृतीया है: शस्त्र से, यानी धार या शल्य-उपकरण से। "
                   "कर्ता इस इकाई में नहीं दिया; डेटा के अनुसार यह सम्भवतः इकाई ९६ का वाक्य आगे बढ़ाता है और सीवनियों के लिए है। "
                   "इसलिए किसे बचाना है, इस पर कोई प्रश्न नहीं।"),
    "hook": "शस्त्र से बचाकर रखो: परिहार्य।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 97, with what is something to be avoided?",
            ("With the śastra, the blade", "शस्त्रेण: with the śastra (blade, surgical instrument)."),
            [("With fire, by cautery", "No fire or cautery is named in unit 97."),
             ("With the hand, by pressing", "No hand or pressing is named in unit 97."),
             ("With oil, by rubbing", "No oil or rubbing is named in unit 97.")],
            "It is to be avoided with the śastra, the blade.",
            "परिहार्याः शस्त्रेण."),
        order(1, "Put the words of unit 97 in the line's order.",
              ["परिहार्याः", "च", "शस्त्रेण"],
              "And to be avoided with the blade.",
              "परिहार्याः → च → शस्त्रेण."),
        match(2, "Match each word of unit 97 to its meaning.",
              [["परिहार्य", "to be avoided, spared"], ["शस्त्र", "blade, surgical instrument"], ["च", "and"]],
              "And to be avoided with the śastra.",
              "परिहार्य, शस्त्र, च.", role="extend",
              teaches="परिहार्य is a gerundive of परि-√हृ: 'to be avoided'."),
        mcq("discriminate", 3, "Which split of परिहार्य्याश्च is right?",
            ("परिहार्याः + च", "A visarga before च becomes श्: परिहार्याः + च → परिहार्याश्च (the print doubles the य)."),
            [("परिहार्या + श्च", "श्च is not a word; the word is च (and)."),
             ("परिहार्यः + च", "अः + च would give परिहार्यश्च, with a short अ, not या."),
             ("परिहार्ये + च", "ए before च stays ए: परिहार्ये च, with no श्.")],
            "परिहार्याः (to be avoided) + च (and): ः + च → श्च.",
            "ः + च → श्च."),
        mcq("apply", 4, "In unit 97, what case is शस्त्रेण, and what sense does it give?",
            ("Instrumental: with the blade", "-एण is the instrumental singular of an अ-stem: with the blade."),
            [("Ablative: away from the blade", "The ablative would be शस्त्रात्."),
             ("Locative: in the blade", "The locative would be शस्त्रे."),
             ("Genitive: of the blade", "The genitive would be शस्त्रस्य.")],
            "शस्त्रेण = with the śastra: instrumental singular.",
            "-एण (after र/ष) = instrumental singular of an अ-stem."),
        mcq("transfer", 5, "By the rule of परिहार्याश्च, how is देवाः + च (and the gods) joined?",
            ("देवाश्च", "A visarga before च becomes श्, as परिहार्याः + च."),
            [("देवाच", "The visarga does not drop before च; it becomes श्."),
             ("देवार्च", "र् comes from a visarga after vowels other than अ/आ, and only before voiced sounds."),
             ("देवोच", "ओ comes from अः before a voiced consonant; च is voiceless and देवाः ends in आः.")],
            "देवाः + च = देवाश्च, like परिहार्याः + च = परिहार्याश्च.",
            "ः + च → श्च.",
            teaches="A visarga before च becomes श्: परिहार्याः + च → परिहार्याश्च."),
    ],
}

# ---------------------------------------------------------------- unit 98
AUTHORED["98"] = {
    "title": "चतुर्दशास्थिसंघाताः",
    "question": "By the sure part of unit 98, where do the fourteen bone assemblages lie?",
    "rule": ("There are fourteen asthi-saṃghātas (bone assemblages); of them one each (एकैकः) in the ankle, knee, groin "
             "(वङ्क्षण), wrist, elbow (कूर्पर) and armpit (कक्षा); the end of the line rests on a conjecture."),
    "limits": ("Low confidence. The ending त्रिकजशिरसोश्च is read on a conjectural correction (trika, probably the sacral "
               "region, and the head): no question rests on it, nor on the sum 12 + 1 + 1 = 14, which is evidence, not text. "
               "'One each' at paired places is the data's reading."),
    "explain_hi": ("यह गद्य-पंक्ति चौदह अस्थि-संघातों यानी हड्डियों के समूहों को गिनाती है। "
                   "उनमें से एक-एक (एकैकः) गुल्फ (टखना), जानु (घुटना), वङ्क्षण (जाँघ और पेट के बीच का भाग), मणिबन्ध (कलाई), "
                   "कूर्पर (कोहनी) और कक्षा (बगल) में है। "
                   "अन्तिम शब्द ‘त्रिकजशिरसोश्च’ अनुमानित सुधार पर ‘त्रिक (सम्भवतः त्रिकास्थि का क्षेत्र) और सिर में’ पढ़ा गया है; "
                   "इसलिए इस अंश पर कोई प्रश्न नहीं। "
                   "12 + 1 + 1 = 14 का जोड़ केवल सुधार के प्रमाण के रूप में दिया गया है, पंक्ति में नहीं लिखा।"),
    "hook": "टखने से बगल तक छह जोड़-स्थान: अस्थि-संघात।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 98, how many asthi-saṃghātas (bone assemblages) are there?",
            ("Fourteen", "चतुर्दश अस्थिसंघाताः: fourteen bone assemblages."),
            [("Sixteen", "Sixteen is the count of the kaṇḍarās and of the jālas."),
             ("Eighteen", "Eighteen is the total of the sīmantas in unit 99."),
             ("Seven", "Seven is the count of the sīvanīs in unit 96.")],
            "The line opens: चतुर्दश, fourteen.",
            "चतुर्दश अस्थिसंघाताः."),
        order(1, "Put the places of unit 98 in the order of गुल्फजानुवंक्षणमणिबंधकूर्परकक्षासु.",
              ["गुल्फ", "जानु", "वंक्षण", "मणिबंध", "कूर्पर", "कक्षा"],
              "Ankle, knee, groin, wrist, elbow, armpit.",
              "गुल्फ → जानु → वंक्षण → मणिबंध → कूर्पर → कक्षा."),
        match(2, "Match each place of unit 98 to its meaning.",
              [["गुल्फ", "ankle"], ["जानु", "knee"], ["वङ्क्षण", "groin"], ["कूर्पर", "elbow"], ["कक्षा", "armpit"]],
              "The sure places: ankle, knee, groin, wrist, elbow and armpit.",
              "गुल्फ, जानु, वङ्क्षण, कूर्पर, कक्षा.", role="extend",
              teaches="अस्थिसंघात = अस्थि (bone) + संघात (assemblage, group): a group of bones."),
        mcq("discriminate", 3, "Which split of चतुर्दशास्थिसंघाताः is right?",
            ("चतुर्दश + अस्थिसंघाताः", "अ + अ → आ: चतुर्दश + अस्थि → चतुर्दशास्थि."),
            [("चतुर्दशा + स्थिसंघाताः", "स्थिसंघाताः is not a word; the word is अस्थिसंघाताः."),
             ("चतुर्दशे + अस्थिसंघाताः", "ए + अ would give चतुर्दशेऽस्थि, with ए kept and ऽ."),
             ("चतुर्दशः + अस्थिसंघाताः", "अः + अ would give चतुर्दशोऽस्थि, with ओऽ.")],
            "चतुर्दश (fourteen) + अस्थिसंघाताः (bone assemblages): अ + अ → आ.",
            "अ + अ → आ."),
        multi("apply", 4, "Which places does the sure part of unit 98 name for the bone assemblages?",
              [("The knee (जानु)", "Right: जानु is the second place."),
               ("The navel (नाभि)", "The navel is not named in unit 98."),
               ("The neck (ग्रीवा)", "The neck is not named in unit 98."),
               ("The elbow (कूर्पर)", "Right: कूर्पर is the fifth place.")],
              [0, 3],
              "The sure places are ankle, knee, groin, wrist, elbow and armpit.",
              "गुल्फ-जानु-वङ्क्षण-मणिबन्ध-कूर्पर-कक्षासु."),
        mcq("transfer", 5, "By the rule of चतुर्दश + अस्थि → चतुर्दशास्थि, how is अत्र + अपि (here too) joined?",
            ("अत्रापि", "अ + अ → आ, as चतुर्दश + अस्थि."),
            [("अत्रोपि", "ओ comes from अ + उ, not from अ + अ."),
             ("अत्रेपि", "ए comes from अ + इ, not from अ + अ."),
             ("अत्रपि", "The two अ merge into a long आ; neither is simply lost.")],
            "अत्र + अपि = अत्रापि, like चतुर्दश + अस्थि = चतुर्दशास्थि.",
            "अ + अ → आ.",
            teaches="A short अ followed by a short अ joins as long आ: चतुर्दश + अस्थि → चतुर्दशास्थि."),
    ],
}

# ---------------------------------------------------------------- unit 99
AUTHORED["99"] = {
    "title": "तद्वत्सीमंताः",
    "question": "By unit 99, how many sīmantas are in the head, and what total is given?",
    "rule": ("Likewise (तद्वत्) the sīmantas (सीमन्त, partings; here probably sutures of bone); they, however (ते तु), are "
             "five in the head (पञ्च शिरसि): thus (इति) eighteen (अष्टादश)."),
    "limits": ("A prose line; the copula is understood. 'Likewise' refers to the places of unit 98; how eighteen is made up "
               "(twelve limb places + trika + five in the head) is a reading, not stated: no question asks how the total "
               "is reached."),
    "explain_hi": ("यह गद्य-पंक्ति सीमन्तों की बात करती है। "
                   "सीमन्त का सामान्य अर्थ बालों की माँग है; अस्थियों के प्रसंग में सम्भवतः सीवन-रेखा (सम्भावित)। "
                   "‘तद्वत्’ यानी उसी प्रकार: पिछली इकाई (९८) के स्थानों की तरह। "
                   "पर सिर में ये पाँच हैं (ते तु पञ्च शिरसि), और इस प्रकार (इति) कुल अठारह (अष्टादश)। "
                   "अठारह कैसे बनते हैं, पंक्ति नहीं बताती; डेटा का अनुमान है: बारह अंग-स्थान, त्रिक और सिर के पाँच।"),
    "hook": "सीमन्त भी वैसे ही, पर सिर में पाँच: कुल अठारह।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 99, what total of sīmantas does the line give?",
            ("Eighteen (अष्टादश)", "इत्यष्टादश: thus eighteen."),
            [("Fourteen (चतुर्दश)", "Fourteen is the count of the bone assemblages in unit 98."),
             ("Sixteen (षोडश)", "Sixteen is the count of the kaṇḍarās and of the jālas."),
             ("Seven (सप्त)", "Seven is the count of the sīvanīs in unit 96.")],
            "The line ends: इति अष्टादश, thus eighteen.",
            "इति अष्टादश = thus eighteen."),
        order(1, "Put these phrases of unit 99 in the line's order.",
              ["तद्वत्सीमंताः", "ते तु", "पंच शिरसि", "इति", "अष्टादश"],
              "Likewise the sīmantas; they, however, five in the head; thus eighteen.",
              "तद्वत्सीमंताः → ते तु → पंच शिरसि → इति → अष्टादश."),
        match(2, "Match each word of unit 99 to its meaning.",
              [["तद्वत्", "likewise"], ["सीमन्त", "parting (probably a bone suture)"], ["शिरसि", "in the head"],
               ["अष्टादश", "eighteen"], ["तु", "however"]],
              "Likewise the sīmantas; they, however, are five in the head: thus eighteen.",
              "तद्वत्, सीमन्त, शिरसि, अष्टादश, तु.", role="extend",
              teaches="तद्वत् = तत् + वत्, 'like that, likewise': त् becomes द् before the voiced व."),
        mcq("discriminate", 3, "Which split of शिरसीत्यष्टादश is right?",
            ("शिरसि + इति + अष्टादश", "इ + इ → ई (शिरसीति), then इ + अ → य (इत्यष्टादश)."),
            [("शिरसि + ति + अष्टादश", "ति is not a word; the particle is इति."),
             ("शिरसि + इत्य + अष्टादश", "इत्य is not a word; the particle is इति."),
             ("शिरसि + इति + यष्टादश", "यष्टादश is not a word; the number is अष्टादश.")],
            "शिरसि (in the head) + इति (thus) + अष्टादश (eighteen).",
            "इ + इ → ई; इ + a different vowel → य्."),
        fill(4, "In unit 99 the sīmantas in the head are ____ (five). Type the number word in Devanagari or in English "
                "letters (e.g. dharma).",
             accepts("पञ्च", None, "pancha"),
             "ते तु पञ्च शिरसि: they, however, are five in the head.",
             "पञ्च (printed पंच) = five.",
             "पञ्च = five.", role="apply"),
        mcq("transfer", 5, "By the rule of इति + अष्टादश → इत्यष्टादश, how is इति + अपि (thus too) joined?",
            ("इत्यपि", "इ before a different vowel becomes य्, as इति + अष्टादश."),
            [("इतेपि", "ए comes from अ + इ, not from इ + अ."),
             ("इतीपि", "ई comes from इ + इ; here अ follows."),
             ("इतयपि", "इ becomes य्, not अय्; अय् comes from ए before a vowel.")],
            "इति + अपि = इत्यपि, like इति + अष्टादश = इत्यष्टादश.",
            "इ + a different vowel → य् + that vowel.",
            teaches="इ before a different vowel becomes य्: इति + अष्टादश → इत्यष्टादश."),
    ],
}

# ---------------------------------------------------------------- unit 100
AUTHORED["100"] = {
    "title": "त्रीणि षष्ठ्याऽधिकान्यस्थिशतानि",
    "question": "By unit 100, how many bones does the text count?",
    "rule": ("Three hundreds of bones (त्रीणि ... अस्थिशतानि), exceeding (अधिकानि) by sixty (षष्ठ्या, instrumental): that is, "
             "three hundred and sixty bones."),
    "limits": ("A prose line; the count is as printed. The line names no bone and gives no division; the division follows "
               "in unit 101. The avagraha in षष्ठ्याऽधिकानि is a print habit. No question rests on the printed form षष्ठ्या."),
    "explain_hi": ("यह गद्य-पंक्ति अस्थियों की कुल संख्या देती है। "
                   "‘त्रीणि ... अस्थिशतानि’ = हड्डियों के तीन सौ, और ‘षष्ठ्या अधिकानि’ = साठ से अधिक; यानी तीन सौ साठ। "
                   "‘षष्ठ्या’ तृतीया है: साठ से (जितना अधिक)। "
                   "यहाँ किसी हड्डी का नाम नहीं; बँटवारा अगली इकाई (१०१) में है। "
                   "छपा अवग्रह (ऽ) छपाई की आदत है।"),
    "hook": "तीन सौ, ऊपर साठ: तीन सौ साठ अस्थियाँ।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 100, how many bones are counted in all?",
            ("Three hundred and sixty", "त्रीणि षष्ठ्याधिकानि अस्थिशतानि: three hundred, exceeding by sixty."),
            [("Three hundred and six", "The excess is sixty (षष्ठ्या), not six."),
             ("Two hundred and sixty", "The hundreds are three (त्रीणि), not two."),
             ("Three hundred and sixteen", "The excess is sixty, not sixteen (षोडश).")],
            "300 exceeding by 60 = 360.",
            "त्रीणि शतानि + षष्ठ्या अधिकानि = 360."),
        order(1, "Put the words of unit 100 in the line's order.",
              ["त्रीणि", "षष्ठ्या", "अधिकानि", "अस्थिशतानि"],
              "Three, by sixty, exceeding, hundreds of bones.",
              "त्रीणि → षष्ठ्या → अधिकानि → अस्थिशतानि."),
        match(2, "Match each word of unit 100 to its meaning.",
              [["त्रीणि", "three"], ["अधिक", "exceeding, in excess"], ["शत", "hundred"], ["अस्थि", "bone"]],
              "Three hundreds of bones, exceeding by sixty.",
              "त्रीणि, अधिक, शत, अस्थि.", role="extend",
              teaches="A number with -अधिक is added to the hundreds: त्रीणि ... अधिकानि शतानि = three hundred plus."),
        mcq("discriminate", 3, "Which split of अधिकान्यस्थिशतानि is right?",
            ("अधिकानि + अस्थिशतानि", "इ before a different vowel becomes य्: अधिकानि + अस्थि → अधिकान्यस्थि."),
            [("अधिकान्य + अस्थिशतानि", "अधिकान्य is not a form; the word is अधिकानि."),
             ("अधिकाने + अस्थिशतानि", "ए + अ would give अधिकानेऽस्थि, with ए kept and ऽ."),
             ("अधिकान् + यस्थिशतानि", "यस्थि is not a word; the word is अस्थि (bone).")],
            "अधिकानि (exceeding) + अस्थिशतानि (hundreds of bones): इ + अ → य.",
            "इ + a different vowel → य् + that vowel."),
        mcq("apply", 4, "In unit 100, what does अधिकानि tell about the sixty?",
            ("Sixty is added to three hundred", "अधिक = exceeding: three hundred, and sixty more."),
            [("Sixty is taken away from three hundred", "अधिक means in excess, not less."),
             ("Three hundred is multiplied by sixty", "Nothing is multiplied; sixty is the excess."),
             ("Sixty bones are left out of the count", "Nothing is left out; the sixty are counted in.")],
            "Three hundred exceeding by sixty: 300 + 60.",
            "-अधिक = in excess by."),
        mcq("transfer", 5, "By the pattern of unit 100, what does a new example द्वे दशाधिके शते mean?",
            ("Two hundred and ten", "द्वे शते = two hundreds; दशाधिके = exceeding by ten."),
            [("One hundred and ninety", "अधिक adds the ten; it does not take it away."),
             ("Twelve hundred", "The ten is added to the hundreds, not multiplied."),
             ("Two hundred and twenty", "The excess is दश, ten, not twenty.")],
            "द्वे दशाधिके शते = 200 + 10 = 210, like त्रीणि षष्ठ्याधिकानि शतानि = 360.",
            "N शतानि with M-अधिक = N hundred + M.",
            teaches="Hundreds with an -अधिक word add that number: त्रीणि षष्ठ्याऽधिकानि अस्थिशतानि = 360 bones."),
    ],
}

# ---------------------------------------------------------------- unit 101
AUTHORED["101"] = {
    "title": "तेषां च त्वारिंशच्छतं शाखासु",
    "question": "By unit 101, how are the 360 bones divided?",
    "rule": ("And of them a hundred and forty are in the limbs (शाखा), a hundred and twenty in the antarādhi (probably the "
             "trunk), a hundred in the head (मूर्ध्नि); two of the numbers rest on restored readings."),
    "limits": ("The initial च- of चत्वारिंशत् is restored (near certain), and सविंशशतम् अन्तराधौ is read across a spacing slip "
               "(possible): no question rests on these two numbers or on what antarādhi is. Sure: a hundred in the head; "
               "140 + 120 + 100 = 360 is the data's evidence."),
    "explain_hi": ("यह गद्य-पंक्ति इकाई १०० की तीन सौ साठ अस्थियों को तीन भागों में बाँटती है। "
                   "एक सौ चालीस शाखाओं यानी हाथ-पैरों में, एक सौ बीस अन्तराधि यानी सम्भवतः धड़ में, और सौ मूर्धा यानी सिर में। "
                   "छपे ‘त्वारिंशच्छतं’ में आरम्भ का ‘च’ छूटा है (लगभग निश्चित सुधार), और ‘स विंशशत मंतराधौ’ में ‘शतम्’ का म् "
                   "अगले शब्द के साथ छपा है (सम्भावित सुधार: सविंशशतम् अन्तराधौ)। "
                   "तीनों का जोड़ ३६० इकाई १०० से मेल खाता है; यही इन सुधारों का प्रमाण माना गया है।"),
    "hook": "३६० का बँटवारा: शाखा १४०, अन्तराधि (सम्भवतः धड़) १२०, सिर १०० (पहली दो संख्याएँ सुधरे पाठ पर)।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 101, how many bones are in the head (मूर्धन्)?",
            ("A hundred", "शतं मूर्ध्नि: a hundred in the head."),
            [("A hundred and forty", "That is the number given for the limbs (शाखा)."),
             ("Sixty", "Sixty is the excess over three hundred in unit 100."),
             ("Three hundred and sixty", "That is the total of all the bones in unit 100.")],
            "शतं मूर्ध्नि: a hundred in the head.",
            "शतम् मूर्ध्नि इति."),
        order(1, "Put these printed phrases of unit 101 in the line's order.",
              ["तेषां च", "त्वारिंशच्छतं शाखासु", "स विंशशत मंतराधौ", "शतं मूर्द्ध्नीति"],
              "And of them: a hundred and forty in the limbs; a hundred and twenty in the trunk (probable); a hundred in "
              "the head.",
              "तेषां च → त्वारिंशच्छतं शाखासु → स विंशशत मंतराधौ → शतं मूर्द्ध्नीति."),
        match(2, "Match each word of unit 101 to its meaning.",
              [["शाखा", "limb (literally branch)"], ["मूर्धन्", "head"], ["शत", "hundred"], ["इति", "thus"]],
              "The bones in the limbs, the trunk and the head; a hundred in the head, thus.",
              "शाखा, मूर्धन्, शत, इति.", role="extend",
              teaches="शाखा, literally 'branch', names the limbs: शाखासु = in the limbs."),
        mcq("discriminate", 3, "Which split of मूर्द्ध्नीति (मूर्ध्नीति) is right?",
            ("मूर्ध्नि + इति", "इ + इ → ई: मूर्ध्नि + इति → मूर्ध्नीति."),
            [("मूर्ध्नी + ति", "ति is not a word; the particle is इति."),
             ("मूर्ध्ने + इति", "ए before इ would give मूर्ध्न इति (or मूर्ध्नयिति), not ई."),
             ("मूर्ध्नः + इति", "अः before इ drops the visarga: मूर्ध्न इति, with no ई.")],
            "मूर्ध्नि (in the head) + इति (thus): इ + इ → ई.",
            "इ + इ → ई."),
        mcq("apply", 4, "By unit 101, of what are these counts a division?",
            ("Of the 360 bones of unit 100", "तेषाम् (of them) points back to the bones just counted; the counts here run to hundreds (शतं मूर्ध्नि)."),
            [("Of the fourteen bone groups of unit 98", "The bone groups are fourteen in all; these counts run to hundreds."),
             ("Of the sixteen jālas of unit 93", "The jālas are sixteen in all; these counts run to hundreds."),
             ("Of the seven sīvanīs of unit 96", "The sīvanīs are seven in all; these counts run to hundreds.")],
            "तेषाम् points back to the 360 bones of unit 100.",
            "तेषाम् = of them (the bones of unit 100)."),
        mcq("transfer", 5, "By the rule of मूर्ध्नि + इति, how is अस्ति + इति (‘is’, thus) joined?",
            ("अस्तीति", "इ + इ → ई, as मूर्ध्नि + इति → मूर्ध्नीति."),
            [("अस्त्यिति", "इ becomes य् only before a different vowel; here इ meets इ."),
             ("अस्तेति", "ए comes from अ + इ, not from इ + इ."),
             ("अस्तिति", "The two इ merge into a long ई; neither is simply lost.")],
            "अस्ति + इति = अस्तीति, like मूर्ध्नि + इति = मूर्ध्नीति.",
            "इ + इ → ई.",
            teaches="Two short इ join as a long ई: मूर्ध्नि + इति → मूर्ध्नीति."),
    ],
}


# ===================================================================== NOTES_HI
NOTES_HI = {
    "90": ("गद्य-पंक्ति; विश्वास उच्च; पाठ-चिह्न नहीं। छपा ‘मूर्द्धा’ = मूर्धा (द का द्वित्व छपाई की आदत)। ‘जिह्वाबन्धन’ "
           "शब्दशः ‘जीभ का बन्धन’ रखा; जीभ की जड़ या जीभ के नीचे का बन्धन, तय नहीं। ‘कण्ठ’ = गला या गर्दन। ‘गूद’ डेटा का रूप "
           "(दीर्घ ऊ) रखा; सामान्य शब्द ‘गुद’ ह्रस्व उ वाला है। ओज शास्त्रीय शब्द, आधुनिक पर्याय नहीं। सन्धि जाँची: प्राण + आयतनानि → "
           "प्राणायतनानि (अ + आ → आ); कण्ठः + हृदयम् → कण्ठो हृदयम् (अः + घोष व्यंजन → ओ); नाभिः + बस्तिः + गूदः → "
           "नाभिर्बस्तिर्गूदः (इः + घोष व्यंजन → इर्); शुक्रम् + ओजः → शुक्रमोजः; ओजः + रक्तम् → ओजो रक्तम् (अः + घोष व्यंजन → ओ)।"),
    "91": ("गद्य-पंक्ति; विश्वास उच्च; पाठ-चिह्न नहीं। ‘पहले सात’ इकाई ९० के क्रम से मूर्धा, जिह्वाबन्धन, कण्ठ, हृदय, नाभि, बस्ति, "
           "गूद होंगे; यह क्रम से निकाला अनुमान है, पंक्ति में नाम नहीं; इस पर प्रश्न नहीं। क्रिया ‘हैं’ समझी जाती है। मर्म शास्त्रीय "
           "शब्द रखा। सन्धि जाँची: एषाम् + आद्यानि → एषामाद्यानि (म् स्वर से मिलता है); पुनः (मूल पुनर्) + महा... → पुनर्महा... "
           "(घोष व्यंजन से पहले र्); महत् समास में महा: महा + मर्म + संज्ञानि → महामर्मसंज्ञानि।"),
    "92": ("गद्य-पंक्ति; विश्वास मध्यम; पाठ-चिह्न नहीं। ‘द्वे द्वे’ वितरणार्थक: दो-दो। ‘चतस्रः पृथक्’: गर्दन और पीठ में चार, "
           "अलग-अलग; प्रत्येक में चार मानें तो 8 + 4 + 4 = 16, पर ‘प्रत्येक’ शब्द पंक्ति में नहीं; इस जोड़ पर प्रश्न नहीं। छपाई में "
           "सन्धि नहीं लगी: ‘कंडराः तासां’ (नियम से कण्डरास्तासाम्, विसर्ग + त → स्) और ‘पृथकग्रीवा’ (नियम से पृथग्ग्रीवा, "
           "क् + घोष व्यंजन → ग्); छपे रूप रखे। ‘कंडराः’ = कण्डराः (अनुस्वार = ण्)। क्रिया समझी जाती है।"),
    "93": ("गद्य-पंक्ति; विश्वास मध्यम; पाठ-चिह्न नहीं। चार प्रकार ही हर स्थान के चार हैं, और चार स्थान (दो टखने, दो कलाई) "
           "मिलकर सोलह, यह डेटा का अर्थ-निर्णय है; जोड़ छपा नहीं, इस पर प्रश्न नहीं। जाल का कोई पक्का आधुनिक पर्याय नहीं। "
           "‘गवाक्षित’ = झरोखे (गवाक्ष) जैसा बना, यानी गुँथा हुआ; शब्दशः रखा। छपा ‘चत्वार्य्येकैकत्र’ में य का द्वित्व छपाई की आदत। "
           "सन्धि जाँची: स्नायु + अस्थि → स्नाय्वस्थि (उ + भिन्न स्वर → व्); चत्वारि + एकैकत्र → चत्वार्येकैकत्र (इ + भिन्न स्वर → य्); "
           "एक + एक → एकैक (अ + ए → ऐ); ‘मणिबंधे’ = मणिबन्धे।"),
    "94": ("गद्य-पंक्ति; विश्वास मध्यम; पाठ-चिह्न नहीं। ‘कूर्च’ = गुच्छा, पूला; शरीर-अंग के रूप में पहचान पक्की नहीं (यही शब्द "
           "आगे की एक पंक्ति में पैर के एक भाग के लिए भी आता है)। छह कूर्च स्थानों में कैसे बँटे, नहीं बताया; इस पर प्रश्न नहीं। "
           "छपा ‘कूर्च्चा’ में च का द्वित्व छपाई की आदत। क्रिया समझी जाती है। सन्धि जाँची: कूर्चाः + हस्त... → कूर्चा हस्त... "
           "(आः + घोष व्यंजन → आ, विसर्ग लोप); छपाई में दोनों शब्द जुड़े छपे हैं।"),
    "95": ("गद्य-पंक्ति; विश्वास उच्च; पाठ-चिह्न नहीं। पेशी = मांसपेशी (मानक)। रज्जुएँ रीढ़ के दोनों ओर हैं; हर ओर कितनी, नहीं "
           "बताया; इस पर प्रश्न नहीं। ‘उभयतः’ के साथ द्वितीया: पृष्ठवंशम् उभयतः। ‘पेशीनिबन्धनार्थे’ सप्तमी, अव्यय की तरह "
           "(प्रयोजन: बाँधने के लिए)। सन्धि जाँची: चतस्रः + मांस... → चतस्रो मांस... (अः + घोष व्यंजन → ओ); पृष्ठवंशम् + उभयतः → "
           "पृष्ठवंशमुभयतः; च + अभ्यन्तर... → चाभ्यन्तर... (अ + अ → आ); ‘निबंधन’, ‘अभ्यंतर’ = निबन्धन, अभ्यन्तर।"),
    "96": ("गद्य-पंक्ति; विश्वास उच्च। पाठ-चिह्न: छपा ‘जिव्हा’ → ‘जिह्वा’ (लगभग निश्चित; ह्व/व्ह अक्षरों का उलटना, इकाई ८९ में भी)। "
           "सीवनी = सेवनी, सिलाई; ‘सीवन-रेखा (suture)’ सम्भावित अर्थ। 5 + 1 + 1 = 7 कुल से मेल खाता है। छपाई में ‘सीवन्यः ताः’ "
           "सन्धि बिना (नियम से सीवन्यस्ताः, विसर्ग + त → स्)। वाक्य सम्भवतः इकाई ९७ में आगे चलता है। सन्धि जाँची: "
           "जिह्वामेहनयोः + एकैका → जिह्वामेहनयोरेकैका (ओः + स्वर → ओर्); एक + एक → एकैक (अ + ए → ऐ), स्त्रीलिङ्ग एकैका; ‘पंच’ = पञ्च।"),
    "97": ("गद्य-अंश; विश्वास मध्यम; पाठ-चिह्न नहीं। कर्ता इस इकाई में नहीं; डेटा के अनुसार यह सम्भवतः इकाई ९६ (सीवनियाँ) का "
           "वाक्य आगे बढ़ाता है, पर कर्ता जोड़ा नहीं गया; इस पर प्रश्न नहीं। ‘परिहार्य’ = टालने योग्य; ‘शस्त्र से बचाने योग्य’ "
           "स्वाभाविक अर्थ। छपा ‘परिहार्य्याः’ में य का द्वित्व छपाई की आदत। सन्धि जाँची: परिहार्याः + च → परिहार्याश्च "
           "(विसर्ग + च → श्)।"),
    "98": ("गद्य-पंक्ति; विश्वास निम्न। पाठ-चिह्न: छपा ‘त्रिकजशिरसोश्च’ → सम्भावित ‘त्रिकशिरसोश्च’ (‘ज’ जोड़ा हुआ अक्षर लगता है); "
           "तब छह अंग-स्थान दोनों ओर (12) + त्रिक + सिर = 14; यह जोड़ प्रमाण है, पंक्ति में नहीं। इस अंश पर और जोड़ पर प्रश्न नहीं। "
           "त्रिक = सम्भवतः त्रिकास्थि का क्षेत्र (सम्भावित)। ‘एकैकः’ को ‘एक-एक’ पढ़ा गया। सन्धि जाँची: चतुर्दश + अस्थि → "
           "चतुर्दशास्थि (अ + अ → आ); तेषाम् + एकैकः → तेषामेकैकः; एकैकः + गुल्फ... → एकैको गुल्फ... (अः + घोष व्यंजन → ओ); "
           "त्रिकशिरसोः + च → त्रिकशिरसोश्च (विसर्ग + च → श्)।"),
    "99": ("गद्य-पंक्ति; विश्वास मध्यम; पाठ-चिह्न नहीं। ‘तद्वत्’ इकाई ९८ के स्थानों की ओर संकेत करता है; अठारह सम्भवतः बारह "
           "अंग-स्थान + त्रिक + सिर के पाँच, पर यह पढ़त है, पंक्ति में नहीं; इस पर प्रश्न नहीं। सीमन्त = माँग; अस्थि-प्रसंग में "
           "सीवन-रेखा (सम्भावित)। क्रिया समझी जाती है। सन्धि जाँची: तत् + वत् → तद्वत् (त् + घोष व्यंजन → द्); शिरसि + इति → "
           "शिरसीति (इ + इ → ई); इति + अष्टादश → इत्यष्टादश (इ + भिन्न स्वर → य्); ‘सीमंताः’ = सीमन्ताः।"),
    "100": ("गद्य-पंक्ति; विश्वास उच्च; पाठ-चिह्न नहीं। संख्या छपे अनुसार: 300 + 60 = 360। छपा अवग्रह ‘षष्ठ्याऽधिकानि’ छपाई की "
            "आदत। ‘साठ’ (षष्टि) की तृतीया का सामान्य रूप ‘षष्ट्या’ (ट) है; छपा ‘षष्ठ्या’ (ठ) डेटा में ‘साठ से’ पढ़ा गया है, फ्लैग नहीं; "
            "इस रूप पर प्रश्न नहीं। सन्धि जाँची: षष्ठ्या + अधिकानि → षष्ठ्याधिकानि (आ + अ → आ); अधिकानि + अस्थि... → "
            "अधिकान्यस्थि... (इ + भिन्न स्वर → य्)।"),
    "101": ("गद्य-पंक्ति; विश्वास मध्यम। पाठ-चिह्न: (१) छपा ‘त्वारिंशच्छतं’ → ‘चत्वारिंशच्छतं’ (लगभग निश्चित; आरम्भ का च छूटा; "
            "चत्वारिंशत्-शतम् = 140); (२) छपा ‘स विंशशत मंतराधौ’ → ‘सविंशशतम् अन्तराधौ’ (सम्भावित; म् अगले शब्द के साथ छपा)। "
            "140 + 120 + 100 = 360, इकाई १०० से मेल, जो इन सुधारों का प्रमाण है। अन्तराधि = सम्भवतः धड़ (सम्भावित)। इन दो संख्याओं "
            "और अन्तराधि पर प्रश्न नहीं। सन्धि जाँची: मूर्ध्नि + इति → मूर्ध्नीति (इ + इ → ई); छपा ‘मूर्द्ध्नीति’ = मूर्ध्नीति (द का "
            "द्वित्व छपाई की आदत)।"),
}


# ===================================================================== AIDS
AIDS = {
    "90": {
        "diagram": {"groups": [
            {"label": "प्राण के दस आयतन (पंक्ति के क्रम में)",
             "items": ["१ मूर्धा (सिर)", "२ जिह्वाबन्धन", "३ कण्ठ", "४ हृदय", "५ नाभि", "६ बस्ति (मूत्राशय)", "७ गूद (गुदा)",
                       "८ शुक्र (वीर्य)", "९ ओज", "१० रक्त"]}]},
        "chunks": "दश प्राणायतनानि | मूर्द्धा जिह्वाबंधनं कंठो हृदयं | नाभिर्बस्तिर्गूदः | शुक्रमोजो रक्तं",
        "sandhi": ("इः + घोष व्यंजन → इर्: नाभिः + बस्तिः → नाभिर्बस्तिः · अः + घोष व्यंजन → ओ: कण्ठः + हृदयम् → कण्ठो हृदयम्; "
                   "ओजः + रक्तम् → ओजो रक्तम्।"),
        "letters": "पहले अक्षर क्रम से: मू-जि-क-हृ-ना-ब-गू-शु-ओ-र (मूर्धा … रक्त)। (मेरी याद-पद्धति)",
    },
    "91": {
        "chunks": "एषामाद्यानि | सप्त | पुनर्महामर्मसंज्ञानि",
        "frame": "किनमें से: एषाम् (इकाई ९० के दस) → कितने: आद्यानि सप्त (पहले सात) → नाम: महामर्मसंज्ञानि (महामर्म कहलाते)।",
        "sandhi": "म् + स्वर → मिलकर: एषाम् + आद्यानि → एषामाद्यानि · पुनः (मूल पुनर्) + घोष व्यंजन → पुनर्: पुनर्महा...।",
    },
    "92": {
        "diagram": {"groups": [
            {"label": "हाथ और पैर (करचरणेषु)", "items": ["दो-दो (द्वे द्वे)"]},
            {"label": "गर्दन और पीठ (ग्रीवापृष्ठयोः)", "items": ["चार, अलग-अलग (चतस्रः पृथक्)"]}]},
        "chunks": "षोडश कंडराः | तासां | द्वे द्वे करचरणेषु | चतस्रः पृथक | ग्रीवापृष्ठयोः",
        "frame": "कुल: षोडश कण्डराः → तासाम् (उनमें) → करचरणेषु द्वे द्वे → ग्रीवापृष्ठयोः चतस्रः पृथक्।",
        "sandhi": ("छपाई में सन्धि नहीं लगी: कण्डराः तासाम् (नियम से कण्डरास्तासाम्, विसर्ग + त → स्) · पृथक ग्रीवा "
                   "(नियम से पृथग्ग्रीवा, क् + घोष व्यंजन → ग्)।"),
    },
    "93": {
        "diagram": {"groups": [
            {"label": "चार प्रकार (जिनसे उत्पन्न)", "items": ["मांस", "सिरा", "स्नायु", "अस्थि"]},
            {"label": "स्थान (हर एक पर चार)", "items": ["गुल्फ (टखना)", "मणिबन्ध (कलाई)"]}]},
        "chunks": "षोडश जालानि | तेषां मांससिरास्नाय्वस्थिजानि | चत्वार्य्येकैकत्र | गुल्फे मणिबंधे च | परस्परगवाक्षितानि स्थितानि",
        "sandhi": ("उ + भिन्न स्वर → व्: स्नायु + अस्थि → स्नाय्वस्थि · इ + भिन्न स्वर → य्: चत्वारि + एकैकत्र → चत्वार्येकैकत्र "
                   "(छपा य्य) · अ + ए → ऐ: एक + एक → एकैक।"),
        "story": ("मेरा बनाया चित्र: टखने और कलाई पर झरोखे की जाली जैसी बुनावट, जिसके धागे मांस, सिरा, स्नायु और अस्थि के हैं। "
                  "(केवल याद की सहायता)"),
    },
    "94": {
        "chunks": "षट् | कूर्च्चा | हस्तपादग्रीवामेढ्रेषु (छपा जुड़ा: कूर्च्चाहस्तपादग्रीवामेढ्रेषु)",
        "sandhi": "आः + घोष व्यंजन → आ (विसर्ग लोप): कूर्चाः + हस्त... → कूर्चा हस्त... (छपाई में जुड़ा)।",
        "letters": "स्थानों के पहले अक्षर क्रम से: ह-पा-ग्री-मे (हस्त, पाद, ग्रीवा, मेढ्र)। (मेरी याद-पद्धति)",
    },
    "95": {
        "chain": {"steps": ["चार मांसरज्जु", "पृष्ठवंश (रीढ़) के दोनों ओर", "प्रयोजन: पेशियों को बाँधना",
                            "उनमें दो बाहरी", "और दो भीतर स्थित"]},
        "chunks": "चतस्रो मांसरज्जवः | पृष्ठवंशमुभयतः | पेशीनिबंधनार्थे | तासां द्वे बाह्ये | द्वे चाभ्यंतरस्थिते",
        "sandhi": "अः + घोष व्यंजन → ओ: चतस्रः + मांस... → चतस्रो मांस... · अ + अ → आ: च + अभ्यन्तर → चाभ्यन्तर।",
        "frame": "कितनी: चार → कहाँ: रीढ़ के दोनों ओर → किसलिए: पेशियाँ बाँधने → बँटवारा: दो बाहर, दो भीतर।",
    },
    "96": {
        "diagram": {"groups": [
            {"label": "सात सीवनियाँ (सम्भवतः सीवन-रेखाएँ)", "items": ["सिर में: पाँच", "जिह्वा में: एक", "मेहन (शिश्न) में: एक"]}]},
        "chunks": "सप्त सीवन्यः | ताः पंच शिरसि | जिव्हामेहनयोरेकैका",
        "sandhi": "ओः + स्वर → ओर्: जिह्वामेहनयोः + एकैका → जिह्वामेहनयोरेकैका · अ + ए → ऐ: एक + एक → एकैक (स्त्रीलिङ्ग एकैका)।",
        "pegs": "पाँच + एक + एक = सात: सिर में हाथ की पाँच उँगलियाँ, बाकी दो अकेले। (मेरी याद-पद्धति)",
    },
    "97": {
        "chunks": "परिहार्य्याश्च | शस्त्रेण",
        "frame": "कौन: (इस इकाई में नहीं; डेटा के अनुसार सम्भवतः इकाई ९६ की सीवनियाँ) → क्या: परिहार्याः (बचाने योग्य) → किससे: शस्त्रेण।",
        "sandhi": "विसर्ग + च → श्: परिहार्याः + च → परिहार्याश्च।",
    },
    "98": {
        "diagram": {"groups": [
            {"label": "निश्चित अंश: एक-एक", "items": ["गुल्फ (टखना)", "जानु (घुटना)", "वङ्क्षण (जाँघ-पेट का जोड़)",
                                                 "मणिबन्ध (कलाई)", "कूर्पर (कोहनी)", "कक्षा (बगल)"]},
            {"label": "अनुमानित पाठ पर", "items": ["त्रिक (सम्भवतः त्रिकास्थि क्षेत्र)", "सिर"]}]},
        "chunks": "चतुर्दशास्थिसंघाताः | तेषामेकैको | गुल्फजानुवंक्षणमणिबंधकूर्परकक्षासु | त्रिकजशिरसोश्च (पढ़त अनुमानित)",
        "sandhi": ("अ + अ → आ: चतुर्दश + अस्थि → चतुर्दशास्थि · अः + घोष व्यंजन → ओ: एकैकः + गुल्फ... → एकैको गुल्फ...।"),
        "letters": "छह स्थानों के पहले अक्षर क्रम से: गु-जा-वं-म-कू-क। (मेरी याद-पद्धति)",
    },
    "99": {
        "chunks": "तद्वत्सीमंताः | ते तु | पंच शिरसि | इत्यष्टादश",
        "sandhi": ("त् + घोष व्यंजन → द्: तत् + वत् → तद्वत् · इ + इ → ई: शिरसि + इति → शिरसीति · इ + भिन्न स्वर → य्: "
                   "इति + अष्टादश → इत्यष्टादश।"),
        "frame": "क्या: सीमन्त (सम्भवतः अस्थि-सीवन) → कैसे: तद्वत् (इकाई ९८ जैसे) → पर सिर में: पाँच → कुल: अठारह।",
    },
    "100": {
        "chunks": "त्रीणि | षष्ठ्याऽधिकान्यस्थिशतानि",
        "frame": "त्रीणि अस्थिशतानि (तीन सौ हड्डियाँ) + षष्ठ्या अधिकानि (साठ अधिक) = तीन सौ साठ।",
        "sandhi": "आ + अ → आ: षष्ठ्या + अधिकानि → षष्ठ्याधिकानि (छपा अवग्रह छपाई की आदत) · इ + भिन्न स्वर → य्: अधिकानि + अस्थि → अधिकान्यस्थि।",
    },
    "101": {
        "diagram": {"groups": [
            {"label": "तीन सौ साठ अस्थियों का बँटवारा", "items": ["शाखाओं (हाथ-पैर) में: एक सौ चालीस (सुधरे पाठ पर)",
                                                                "अन्तराधि (सम्भवतः धड़) में: एक सौ बीस (सम्भावित पाठ पर)",
                                                                "मूर्धा (सिर) में: सौ"]}]},
        "chunks": "तेषां च | त्वारिंशच्छतं शाखासु | स विंशशत मंतराधौ | शतं मूर्द्ध्नीति",
        "sandhi": "इ + इ → ई: मूर्ध्नि + इति → मूर्ध्नीति।",
        "frame": "कुल ३६० (इकाई १००) → शाखाएँ → अन्तराधि → मूर्धा; जोड़ १४० + १२० + १०० = ३६०।",
    },
}


# ===================================================================== IMAGE_SPECS
IMAGE_SPECS = {
    ("90", "diagram"): {
        "file": "sh5-pranayatana-90.svg",
        "alt": ("Numbered table of unit 90, the ten seats of life in line order: 1 head, 2 tongue-binding, 3 throat, "
                "4 heart, 5 navel, 6 bladder, 7 gūda (anus), 8 śukra (semen), 9 ojas, 10 blood."),
        "type": "table",
        "title": "इकाई ९०: प्राण के दस आयतन",
        "heads": ["क्रम", "प्राणायतन"],
        "rows": [["१", "मूर्धा (सिर)"], ["२", "जिह्वाबन्धन (जीभ का बन्धन)"], ["३", "कण्ठ (गला या गर्दन)"], ["४", "हृदय"],
                 ["५", "नाभि"], ["६", "बस्ति (मूत्राशय)"], ["७", "गूद (गुदा)"], ["८", "शुक्र (वीर्य)"], ["९", "ओज"],
                 ["१०", "रक्त"]],
    },
    ("92", "diagram"): {
        "file": "sh5-kandara-92.svg",
        "alt": ("Table of unit 92, sixteen kaṇḍarās (large tendons): two each in the hands and feet; four, separately, in "
                "the neck and the back, as printed."),
        "type": "table",
        "title": "इकाई ९२: सोलह कण्डराएँ",
        "heads": ["स्थान", "कण्डराएँ (छपे अनुसार)"],
        "rows": [["हाथ और पैर", "दो-दो"], ["गर्दन और पीठ", "चार, अलग-अलग"], ["कुल", "सोलह"]],
    },
    ("93", "diagram"): {
        "file": "sh5-jala-93.svg",
        "alt": ("Two columns of unit 93 on the sixteen jālas (nets): born of four kinds, flesh, vessel, snāyu and bone; "
                "placed four at each site, at the ankle and the wrist."),
        "type": "split",
        "title": "इकाई ९३: सोलह जाल",
        "cols": [["जिनसे उत्पन्न", ["मांस", "सिरा", "स्नायु", "अस्थि"]],
                 ["स्थान (हर एक पर चार)", ["गुल्फ (टखना)", "मणिबन्ध (कलाई)"]]],
    },
    ("95", "chain"): {
        "file": "sh5-mamsarajju-95.svg",
        "alt": ("Chain of unit 95, five points in line order: four flesh-cords; on both sides of the spine; purpose: "
                "binding the muscles; of them two outer; and two situated inside."),
        "type": "chain",
        "title": "इकाई ९५: चार मांसरज्जु (पंक्ति के क्रम में)",
        "steps": ["चार मांसरज्जु", "पृष्ठवंश (रीढ़) के दोनों ओर", "प्रयोजन: पेशियों को बाँधना", "उनमें दो बाहरी",
                  "और दो भीतर स्थित"],
    },
    ("96", "diagram"): {
        "file": "sh5-sivani-96.svg",
        "alt": ("Table of unit 96, seven sīvanīs (seams, probably sutures): five in the head, one in the tongue, one in the "
                "mehana (penis); total seven."),
        "type": "table",
        "title": "इकाई ९६: सात सीवनियाँ (सम्भवतः सीवन-रेखाएँ)",
        "heads": ["स्थान", "सीवनी"],
        "rows": [["सिर", "पाँच"], ["जिह्वा", "एक"], ["मेहन (शिश्न)", "एक"], ["कुल", "सात"]],
    },
    ("98", "diagram"): {
        "file": "sh5-asthisanghata-98.svg",
        "alt": ("Table of unit 98, fourteen bone assemblages: sure places, one each, ankle, knee, groin, wrist, elbow, "
                "armpit; on a conjectural reading also trika (probably the sacral region) and the head."),
        "type": "table",
        "title": "इकाई ९८: चौदह अस्थि-संघात",
        "heads": ["स्थान", "अर्थ"],
        "rows": [["गुल्फ", "टखना"], ["जानु", "घुटना"], ["वङ्क्षण", "जाँघ और पेट का जोड़"], ["मणिबन्ध", "कलाई"],
                 ["कूर्पर", "कोहनी"], ["कक्षा", "बगल"], ["अनुमानित पाठ पर: त्रिक, सिर", "त्रिक सम्भवतः त्रिकास्थि क्षेत्र"]],
    },
    ("101", "diagram"): {
        "file": "sh5-asthi-vibhaga-101.svg",
        "alt": ("Table of unit 101, division of the 360 bones: limbs 140 (on a restored reading), antarādhi, probably the "
                "trunk, 120 (on a possible reading), head 100; total 360 as in unit 100."),
        "type": "table",
        "title": "इकाई १०१: तीन सौ साठ अस्थियों का बँटवारा",
        "heads": ["स्थान", "अस्थियाँ"],
        "rows": [["शाखाएँ (हाथ-पैर)", "१४० (सुधरे पाठ पर)"], ["अन्तराधि (सम्भवतः धड़)", "१२० (सम्भावित पाठ पर)"],
                 ["मूर्धा (सिर)", "१००"], ["कुल (इकाई १००)", "३६०"]],
    },
}
