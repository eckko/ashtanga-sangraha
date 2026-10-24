from helpers import mcq, match, order, fill, multi, accepts

# Kalpasthāna chapter 4 (Bastikalpa), units 38-51 (study-text lines 05.04.73-99).
# Sections (sections_kalpa.py KA4): 38-41 bastis in jīvādāna; 42-48 mild bastis measured by prasṛta;
# 49-51 sharpness and mildness in bastis.
# Cross-references name study-text line ids (05.04.L), not quiz unit numbers.

AUTHORED = {}

# ---------------------------------------------------------------- unit 38
AUTHORED["38"] = {
    "title": "बृहतीक्षीरकाकोलीपृश्निपर्णीशतावरी",
    "question": "Which drugs does verse 38 list, and what does the unit leave unsaid about them?",
    "rule": ("A verb-less list of nine drugs: bṛhatī, kṣīrakākolī, pṛśniparṇī, śatāvarī; then kāśmarya, badarī, mūrvā, "
             "and likewise uśīra and priyaṅgu. The unit itself states no use for them."),
    "limits": ("No verb and no use in the unit. Whether the list belongs with the four beginning with nyagrodha of line 05.04.72 "
               "is not stated. Kṣīrakākolī and priyaṅgu are disputed, mūrvā probable; the rest standard."),
    "explain_hi": ("यह श्लोक केवल द्रव्यों की सूची है; इसमें कोई क्रिया नहीं और इन द्रव्यों का प्रयोग भी नहीं बताया गया। "
                   "पहली पंक्ति में बृहती यानी बड़ी कटेरी, क्षीरकाकोली (अष्टवर्ग का द्रव्य, पहचान विवादित), पृश्निपर्णी यानी पिठवन और शतावरी यानी सतावर हैं। "
                   "दूसरी पंक्ति में काश्मर्य यानी गम्भारी, बदरी यानी बेर, मूर्वा यानी सम्भवतः मरोड़फली, और ‘तथा’ के बाद उशीर यानी खस और प्रियङ्गु (पहचान विवादित)। "
                   "पंक्ति ०५.०४.७२ ‘न्यग्रोध आदि चार’ पर रुकती है; यह सूची उसी समूह की है या नहीं, पाठ नहीं कहता। "
                   "अगली पंक्ति ०५.०४.७५ से जीवादान का विषय शुरू होता है।"),
    "hook": "कटेरी-क्षीरकाकोली-पिठवन-सतावर, फिर गम्भारी-बेर-मरोड़फली, तथा खस-प्रियङ्गु: नौ नाम, कोई क्रिया नहीं।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "Which drug of verse 38 is identified as wild asparagus (standard)?",
            ("Śatāvarī",
             "शतावरी = Asparagus racemosus, wild asparagus (standard)."),
            [("Bṛhatī", "Bṛhatī is Indian nightshade (Solanum indicum)."),
             ("Pṛśniparṇī", "Pṛśniparṇī is Uraria picta."),
             ("Uśīra", "Uśīra is vetiver.")],
            "Line 1 ends with शतावरी, wild asparagus.",
            "शतावरी = wild asparagus."),
        match(1, "Match each drug of verse 38 to its identification as the card gives it.",
              [["बृहती", "Indian nightshade"], ["काश्मर्य", "gmelina"], ["बदरी", "jujube"],
               ["उशीर", "vetiver"], ["शतावरी", "wild asparagus"]],
              "All five are standard identifications in the data.",
              "बृहती = Indian nightshade; काश्मर्य = gmelina; बदरी = jujube; उशीर = vetiver; शतावरी = wild asparagus."),
        order(2, "Put these drugs of verse 38 in the verse's order.",
              ["बृहती", "क्षीरकाकोली", "पृश्निपर्णी", "शतावरी", "काश्मर्य", "बदरी"],
              "Line 1 gives four names in one compound; line 2 opens with kāśmarya and badarī.",
              "बृहती · क्षीरकाकोली · पृश्निपर्णी · शतावरी · काश्मर्य · बदरी.",
              role="extend",
              teaches="Verse 38 lists bṛhatī, kṣīrakākolī, pṛśniparṇī, śatāvarī in line 1, then kāśmarya, badarī, mūrvā, uśīra, priyaṅgu."),
        mcq("discriminate", 3, "Which split of तथोशीरप्रियंगवः in verse 38 is right?",
            ("तथा + उशीर + प्रियङ्गवः",
             "आ + उ → ओ: तथा + उशीर = तथोशीर."),
            [("तथ + ओशीर + प्रियङ्गवः", "अ + ओ gives औ: it would read तथौशीर."),
             ("तथाः + उशीर + प्रियङ्गवः", "-आः before a vowel loses the visarga and does not merge: तथा उशीर."),
             ("तथे + उशीर + प्रियङ्गवः", "ए before उ does not give ओ; and तथे is no word.")],
            "तथा (likewise) + उशीर (vetiver) + प्रियङ्गवः (priyaṅgu, plural).",
            "आ + उ → ओ."),
        mcq("apply", 4, "A student says verse 38 states these drugs are for jīvādāna. What does the card say?",
            ("The unit names no use for them",
             "The notes say the unit has no verb and states no use."),
            [("They are said to serve jīvādāna", "Jīvādāna is first named in line 05.04.75, not here."),
             ("They are said to destroy Vāta", "No action is stated in verse 38."),
             ("They are said to be binding", "Binding (saṃgrāhika) was said of an earlier list.")],
            "Verse 38 is a bare list: nine names, no verb, no use.",
            "Supply no use the unit does not state."),
        mcq("transfer", 5, "Like मूर्वाः + तथा → मूर्वास्तथा, how does invented लताः + तथा join?",
            ("लतास्तथा",
             "-आः before त becomes -आस्, as in मूर्वास्तथा."),
            [("लता तथा", "The visarga after -आ drops before voiced sounds; त is unvoiced."),
             ("लताश्तथा", "श् appears before च/छ, not before त."),
             ("लतार्तथा", "र् comes from -इः/-उः before voiced sounds, not from -आः.")],
            "Before त/थ a visarga becomes the dental स्.",
            "-आः + त → -आस्त.",
            teaches="A visarga before त/थ becomes स् (मूर्वाः + तथा → मूर्वास्तथा; लताः + तथा → लतास्तथा)."),
    ],
}

# ---------------------------------------------------------------- unit 39
AUTHORED["39"] = {
    "title": "जीवादाने शृते क्षीरे",
    "question": "Which bastis does verse 39 prescribe in jīvādāna, and how are they to be given?",
    "rule": ("In jīvādāna (lit. taking away of life), two bastis in boiled milk, joined with ghee and añjana, are to be given "
             "by the physician cool, with honey and sugar."),
    "limits": ("Jīvādāna is not defined in the unit; a reading as severe blood loss is an open note, so no question uses it. "
               "Which añjana is meant, and what kind of sugar, is not stated."),
    "explain_hi": ("यहाँ जीवादान का विषय शुरू होता है; शब्दार्थ है ‘जीव का ले लिया जाना’, पर पाठ इसका अर्थ नहीं बताता। "
                   "दोनों पंक्तियाँ एक वाक्य लगती हैं: पहली पंक्ति का ‘द्वौ’ दूसरी पंक्ति की ‘बस्ती’ (द्विवचन) से जुड़ता है। "
                   "उबाले हुए दूध में, घी और अञ्जन से युक्त दो बस्तियाँ वैद्य को देनी चाहिए, ठंडी, मधु और शर्करा सहित। "
                   "अञ्जन कौन-सा है और शर्करा किस रूप की, यह नहीं कहा गया।"),
    "hook": "जीवादान में: उबला दूध, घी-अञ्जन, फिर ठंडी करके शहद-शक्कर; और बस्तियाँ दो।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In what state are the bastis of verse 39 to be given?",
            ("Cool (शीतौ)",
             "शीतौ: cool, agreeing with the dual बस्ती."),
            [("Warm (उष्णौ)", "Warm is not said in verse 39."),
             ("Slightly warm (कवोष्ण)", "Slightly warm is said in line 05.04.95, for ānāha."),
             ("At body heat", "No such measure of heat is in verse 39.")],
            "बस्ती प्रदेयौ … शीतौ: the two bastis are given cool.",
            "शीत = cool."),
        match(1, "Match each word of verse 39 to its meaning as the card gives it.",
              [["जीवादान", "lit. taking away of life"], ["शृत", "boiled"], ["अञ्जन", "a collyrium substance"],
               ["शर्करा", "sugar"], ["भिषज्", "physician"]],
              "The words name the condition, the milk, two additions and the giver.",
              "जीवादान = taking away of life (lit.); शृत = boiled; अञ्जन = collyrium substance; शर्करा = sugar; भिषज् = physician."),
        order(2, "Put these phrases of verse 39 in the verse's order.",
              ["जीवादाने", "शृते क्षीरे", "द्वौ घृतांजनसंयुतौ", "बस्ती प्रदेयौ भिषजा", "शीतौ समधुशर्करौ"],
              "Condition, medium, the two with their additions, the giving, and the manner.",
              "जीवादाने · शृते क्षीरे · द्वौ घृतांजनसंयुतौ · बस्ती प्रदेयौ भिषजा · शीतौ समधुशर्करौ.",
              role="extend",
              teaches="Verse 39 runs: in jīvādāna, in boiled milk, two (bastis) with ghee and añjana, to be given by the physician, cool, with honey and sugar."),
        mcq("discriminate", 3, "In verse 39, what does the form बस्ती show?",
            ("Two bastis, masculine dual",
             "Basti is an i-stem masculine; -ई is its dual, agreeing with द्वौ and प्रदेयौ."),
            [("One basti, feminine singular", "In Sanskrit basti is masculine; the dual agrees with द्वौ."),
             ("Many bastis, in the plural", "The plural would be बस्तयः."),
             ("A basti, in the locative case", "The locative singular would be बस्तौ.")],
            "द्वौ … बस्ती प्रदेयौ … शीतौ: every word is dual.",
            "बस्ती (i-stem, m.) = nominative dual."),
        multi("apply", 4, "Which does verse 39 say the bastis are given with?",
              [("Ghee (घृत)", "Right: घृताञ्जनसंयुतौ names ghee."),
               ("Añjana (अञ्जन)", "Right: añjana is in the same compound."),
               ("Honey (मधु)", "Right: स-मधु-शर्करौ names honey."),
               ("Sugar (शर्करा)", "Right: शर्करा is in the same compound."),
               ("Oil (तैल)", "Oil is not named in verse 39."),
               ("Rock salt (सैन्धव)", "Rock salt is not named in verse 39.")],
              [0, 1, 2, 3],
              "Ghee and añjana are joined; honey and sugar go with the cool bastis.",
              "Additions of verse 39: घृत, अञ्जन, मधु, शर्करा."),
        mcq("transfer", 5, "Like शीतौ बस्ती (two cool bastis), which invented phrase means two mild bastis?",
            ("मृदू बस्ती",
             "मृदु is a u-stem: its masculine dual is मृदू, beside the dual बस्ती."),
            [("मृदुः बस्तिः", "Singular: one mild basti."),
             ("मृदवः बस्तयः", "Plural: three or more."),
             ("मृदुं बस्तिम्", "Accusative singular, not a nominative dual.")],
            "Adjective and noun agree in the dual: a-stems take -औ (शीतौ), i/u-stems lengthen (बस्ती, मृदू).",
            "Masculine dual: -औ, -ई, -ऊ.",
            teaches="In the masculine nominative dual a-stems end in -औ (शीतौ), i-stems in -ई (बस्ती), u-stems in -ऊ (मृदू)."),
    ],
}

# ---------------------------------------------------------------- unit 40
AUTHORED["40"] = {
    "title": "अजामहिषीक्षीरैर्जीवनीययुतैरपि",
    "question": "Which milks and which bloods does verse 40 list for the jīvādāna basti of line 05.04.79?",
    "rule": ("With the milks of goat and she-buffalo (and cow, on an open reading), also joined with jīvanīya (life-promoting) "
             "drugs; and with the blood of hare, eṇa (antelope), cat, she-buffalo and others. The verb comes in line 05.04.79."),
    "limits": ("Low confidence. The split of गोऽपि is an open note; दक्ष is read as ṛkṣa (bear) only by conjecture; अन्यज is unclear. "
               "Jīvanīya members are not listed here. Questions keep to the clear words."),
    "explain_hi": ("यह श्लोक जीवादान की बस्ति के द्रव्य गिनाता है; वाक्य पंक्ति ०५.०४.७९ के ‘प्रशस्यते’ पर पूरा होता लगता है। "
                   "पहली पंक्ति में बकरी और भैंस के दूध हैं, जीवनीय यानी जीवन बढ़ाने वाले द्रव्यों से भी युक्त; ‘गो’ यानी गाय का पाठ खुला प्रश्न है। "
                   "दूसरी पंक्ति में रक्त है: खरगोश, एण यानी हिरण, बिल्ली और भैंस का; बीच का छपा ‘दक्ष’ अनुमानित पाठ पर भालू है, और अन्त का ‘अन्यज’ स्पष्ट नहीं। "
                   "जीवनीय गण के सदस्य यहाँ नहीं गिनाए गए।"),
    "hook": "दूध (बकरी, भैंस) जीवनीय के साथ; रक्त (खरगोश, हिरण, बिल्ली, भैंस) ताज़ा।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What does शोणित mean in verse 40?",
            ("Blood",
             "शोणित = blood; the line lists the animals whose blood is meant."),
            [("Milk", "Milk is क्षीर, in line 1."),
             ("Flesh", "Flesh (मांस) is not named in verse 40."),
             ("Fat", "Fat (वसा) is not named in verse 40.")],
            "…शोणितैः: with the bloods (of hare and the rest).",
            "शोणित = blood."),
        match(1, "Match each clear word of verse 40 to its meaning.",
              [["अजा", "goat"], ["महिषी", "she-buffalo"], ["शश", "hare"], ["मार्जार", "cat"], ["जीवनीय", "life-promoting"]],
              "These words are clear in the print; the doubtful ones are left out.",
              "अजा = goat; महिषी = she-buffalo; शश = hare; मार्जार = cat; जीवनीय = life-promoting."),
        order(2, "Put these clear animals of verse 40, line 2, in the verse's order.",
              ["शश (hare)", "एण (antelope)", "मार्जार (cat)", "महिषी (she-buffalo)"],
              "Hare and antelope open the compound; cat and she-buffalo follow (the doubtful दक्ष stands between).",
              "शश · एण · मार्जार · महिषी.",
              role="extend",
              teaches="The blood list of verse 40 runs hare, antelope, (a doubtful name), cat, she-buffalo, and an unclear last member."),
        mcq("discriminate", 3, "Which split of शशैण in verse 40 is right?",
            ("शश + एण",
             "अ + ए → ऐ: शश + एण = शशैण."),
            [("शश + इण", "अ + इ gives ए: it would read शशेण."),
             ("शशः + एण", "-अः before a vowel loses the visarga and does not merge: शश एण."),
             ("शशे + अण", "ए + अ gives ए with an avagraha: शशेऽण.")],
            "शश (hare) + एण (antelope).",
            "अ + ए → ऐ."),
        mcq("apply", 4, "What are the milks of verse 40 also joined with?",
            ("Jīvanīya drugs",
             "जीवनीययुतैः: joined with the jīvanīya (life-promoting) ones."),
            [("Honey and sugar", "Honey and sugar go with the bastis of verse 39."),
             ("Ghee and añjana", "Ghee and añjana are in verse 39."),
             ("Mustard paste", "Mustard paste is in line 05.04.87.")],
            "Line 1 ends: जीवनीययुतैरपि, also joined with life-promoting drugs.",
            "जीवनीय = life-promoting group."),
        mcq("transfer", 5, "Like the instrumental …शोणितैः (with bloods), which invented word means with the blood of a hare?",
            ("शशशोणितेन",
             "A tat-puruṣa शश-शोणित with the instrumental singular -एन."),
            [("शशशोणितम्", "Nominative or accusative, not with."),
             ("शशशोणितस्य", "Genitive: of the hare's blood."),
             ("शशशोणिते", "Locative: in the hare's blood.")],
            "With = instrumental; a neuter a-stem takes -एन in the singular, -ऐः in the plural.",
            "Instrumental: -एन (sg.), -ऐः (pl.).",
            teaches="Neuter a-stems in the instrumental take -एन (singular) and -ऐः (plural): शोणितैः, शशशोणितेन."),
    ],
}

# ---------------------------------------------------------------- unit 41
AUTHORED["41"] = {
    "title": "सद्यस्कैर्मृदितैर्बस्तिर्जीवादाने प्रशस्यते",
    "question": "What does verse 41 recommend in jīvādāna, and what new topic does it announce?",
    "rule": ("With fresh, crushed (ones) a basti is recommended in jīvādāna; this closes the sentence of lines 05.04.77-78. "
             "Then a new topic: these mild nirūhas of the delicate (sukumāra); the verb, I shall state, is in line 05.04.81."),
    "limits": ("Low confidence. एहनान् is read as स्नेहनान् (oily ones) only by conjecture: no question on it. Whether fresh and "
               "crushed go with the bloods or the milks is not settled; मृदित may also mean rubbed or mixed."),
    "explain_hi": ("पहली पंक्ति पंक्ति ०५.०४.७७ से चले वाक्य को पूरा करती लगती है: ताज़े और मसले हुए (द्रव्यों) से बस्ति जीवादान में प्रशस्त मानी जाती है। "
                   "‘सद्यस्क’ का शब्दार्थ है ‘उसी दिन का’, यानी ताज़ा। ये विशेषण पिछली पंक्ति के रक्तों से जुड़ते हैं या दूधों से, तय नहीं। "
                   "दूसरी पंक्ति ‘अथ’ से नया विषय खोलती है: सुकुमारों के ये मृदु निरूह; छपा ‘एहनान्’ अनुमानित पाठ पर ‘स्नेहनान्’ है। "
                   "क्रिया ‘वक्ष्यामि’ अगली पंक्ति में है।"),
    "hook": "ताज़ा और मसला: जीवादान में प्रशंसित; फिर ‘अथ’: सुकुमारों के मृदु निरूह।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In verse 41, where is the basti said to be recommended (प्रशस्यते)?",
            ("In jīvādāna",
             "बस्तिर्जीवादाने प्रशस्यते: in jīvādāna the basti is recommended."),
            [("In ānāha", "Ānāha is named in line 05.04.95."),
             ("In atiyoga", "Atiyoga was named in line 05.04.71."),
             ("In mūtrakṛcchra", "Mūtrakṛcchra is named in line 05.04.95.")],
            "Line 1 closes the jīvādāna recipe of lines 05.04.77-78.",
            "प्रशस्यते = is recommended."),
        match(1, "Match each clear word of verse 41 to its meaning.",
              [["सद्यस्क", "fresh (of the same day)"], ["मृदित", "crushed"], ["प्रशस्यते", "is recommended"],
               ["सुकुमार", "delicate"], ["मृदु", "mild"]],
              "The first three close the jīvādāna recipe; the last two open the new topic.",
              "सद्यस्क = fresh; मृदित = crushed; प्रशस्यते = is recommended; सुकुमार = delicate; मृदु = mild."),
        order(2, "Put these words of verse 41, line 1, in the verse's order.",
              ["सद्यस्कैः", "मृदितैः", "बस्तिः", "जीवादाने", "प्रशस्यते"],
              "Two adjectives, the subject, the condition, and the verb last.",
              "सद्यस्कैः · मृदितैः · बस्तिः · जीवादाने · प्रशस्यते.",
              role="extend",
              teaches="Line 1 of verse 41 reads: with fresh, crushed (ones), the basti in jīvādāna is recommended."),
        mcq("discriminate", 3, "Which split of अथेमान् in verse 41 is right?",
            ("अथ + इमान्",
             "अ + इ → ए: अथ + इमान् = अथेमान्."),
            [("अथ + एमान्", "अ + ए gives ऐ: it would read अथैमान्."),
             ("अथः + इमान्", "-अः before a vowel loses the visarga and does not merge: अथ इमान्."),
             ("अथो + इमान्", "ओ before इ becomes अव्: it would read अथविमान्.")],
            "अथ (now) + इमान् (these, accusative plural).",
            "अ + इ → ए."),
        mcq("apply", 4, "For whom are the mild nirūhas announced in verse 41?",
            ("The delicate (sukumāra)",
             "सुकुमाराणाम्: of the delicate, the mild nirūhas."),
            [("Those dulled by mild bastis", "They are named in line 05.04.96 and get a sharp basti."),
             ("Those with painful urination", "Mūtrakṛcchra is named in line 05.04.95."),
             ("Those depleted by sharp ones", "They are named in line 05.04.97.")],
            "अथ इमान् सुकुमाराणां निरूहान् … मृदून्: these mild nirūhas of the delicate.",
            "सुकुमार = delicate."),
        mcq("transfer", 5, "Like सद्यस्कैः + मृदितैः → सद्यस्कैर्मृदितैः, how does invented शीतैः + मधुरैः join?",
            ("शीतैर्मधुरैः",
             "-ऐः before a voiced sound becomes -ऐर्, as in सद्यस्कैर्मृदितैः."),
            [("शीतैमधुरैः", "The visarga after ऐ is not dropped; it becomes र् before voiced म."),
             ("शीतैस्मधुरैः", "स् appears before त/थ, not before म."),
             ("शीतोमधुरैः", "-ओ comes from -अः, not from -ऐः.")],
            "A visarga after a vowel other than अ/आ becomes र् before a voiced sound.",
            "-ऐः + voiced consonant → -ऐर्.",
            teaches="A visarga after ऐ (not अ/आ) becomes र् before a voiced sound: सद्यस्कैः + मृदितैः → सद्यस्कैर्मृदितैः; शीतैः + मधुरैः → शीतैर्मधुरैः."),
    ],
}

# ---------------------------------------------------------------- unit 42
AUTHORED["42"] = {
    "title": "कर्मणा विप्लुतानां च वक्ष्यामि",
    "question": "What does verse 42 promise to state, for whom, and by what measure?",
    "rule": ("For the delicate (line 05.04.80) and for those harmed by the action (karman), the author will state (bastis) "
             "separately, by prasṛtas (a palmful, about two pala). The recipe begins with prasṛtas from milk."),
    "limits": ("Low confidence. द्धौ is read as द्वौ (two) and मधुनैल as madhu-taila (honey, oil) only by conjecture: no question on "
               "the counts or the second half. Karman probably means the cleansing procedures; the text says only the action."),
    "explain_hi": ("पहली पंक्ति पिछले श्लोक से जुड़ी है: सुकुमारों के और कर्म से पीड़ित हुओं के मृदु निरूह मैं प्रसृतों से अलग-अलग कहूँगा। "
                   "‘कर्म’ सम्भवतः वमन, विरेचन जैसे शोधन-कर्म हैं, पर पाठ केवल ‘कर्म से’ कहता है। "
                   "प्रसृत हथेली-भर का माप है, लगभग दो पल। "
                   "दूसरी पंक्ति में दूध से प्रसृत बनाने की बात है; छपा ‘द्धौ’ अनुमानित पाठ पर ‘द्वौ’ (दो) और ‘मधुनैल’ अनुमानित पाठ पर मधु-तैल है, इसलिए गिनतियाँ पक्की नहीं।"),
    "hook": "सुकुमार और कर्म-पीड़ित: हर द्रव्य हथेली-भर प्रसृत से, अलग-अलग।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By what measure will the author state the bastis in verse 42?",
            ("By prasṛtas (palmfuls)",
             "प्रसृतैः पृथक्: by prasṛtas, separately."),
            [("By palas (weights)", "Pala is not the measure named in verse 42."),
             ("By añjalis (handfuls)", "Añjali is not named in verse 42."),
             ("By kuḍavas (cups)", "Kuḍava is not named in verse 42.")],
            "वक्ष्यामि प्रसृतैः पृथक्: I shall state by prasṛtas, separately.",
            "प्रसृत = a palmful (about two pala)."),
        match(1, "Match each word of verse 42, line 1, to its meaning.",
              [["कर्मणा", "by the action"], ["विप्लुत", "afflicted, harmed"], ["वक्ष्यामि", "I shall state"],
               ["पृथक्", "separately"], ["प्रसृत", "palmful measure"]],
              "Line 1 is clear; line 2 has two conjectural readings.",
              "कर्मणा = by the action; विप्लुत = harmed; वक्ष्यामि = I shall state; पृथक् = separately; प्रसृत = palmful."),
        order(2, "Put these words of verse 42, line 1, in the verse's order.",
              ["कर्मणा", "विप्लुतानां च", "वक्ष्यामि", "प्रसृतैः", "पृथक्"],
              "For whom, the verb, then the measure and the manner.",
              "कर्मणा · विप्लुतानां च · वक्ष्यामि · प्रसृतैः · पृथक्.",
              role="extend",
              teaches="Line 1 of verse 42: and of those harmed by the action, I shall state by prasṛtas, separately."),
        mcq("discriminate", 3, "What does the form वक्ष्यामि in verse 42 show?",
            ("Future, first person: I shall state",
             "The data's label: future, 1st singular of √वच्."),
            [("Present, first person: I state", "The present of √वच् is वच्मि; -ष्यामि marks the future."),
             ("Optative, third person: one should state", "-ष्यामि marks the future, not the optative."),
             ("Past, third person: he stated", "The past would be उवाच; -ष्यामि is the future.")],
            "वक्ष्यामि: the author promises what follows.",
            "-स्यामि / -ष्यामि = future, 1st singular."),
        mcq("apply", 4, "Whom does verse 42 add to the delicate of line 05.04.80?",
            ("Those harmed by the action",
             "कर्मणा विप्लुतानां च: and of those harmed by the action."),
            [("Those depleted by sharp bastis", "They are named in line 05.04.97."),
             ("Those who suffer jīvādāna", "Jīvādāna closed in line 05.04.79."),
             ("Those who have ānāha", "Ānāha is named in line 05.04.95.")],
            "च adds a second group to the delicate: those harmed by karman.",
            "विप्लुत = afflicted, harmed."),
        mcq("transfer", 5, "Like वक्ष्यामि (I shall state), which invented form means I shall give, from √दा?",
            ("दास्यामि",
             "Future 1st singular: दा + स्यामि."),
            [("ददामि", "Present: I give."),
             ("दद्याम्", "Optative: I would give."),
             ("दत्त्वा", "Absolutive: having given.")],
            "The future adds -स्य- (-ष्य- after some sounds) and the person ending -आमि.",
            "Future 1st singular: -स्यामि / -ष्यामि.",
            teaches="The future 1st singular ends in -स्यामि or -ष्यामि: वक्ष्यामि (I shall state), दास्यामि (I shall give)."),
    ],
}

# ---------------------------------------------------------------- unit 43
AUTHORED["43"] = {
    "title": "खजेन मथितो बस्तिर्वातघ्नो बलवर्णकृत्",
    "question": "What does the khaja-churned basti of verse 43 do, and which four items go in one prasṛta each?",
    "rule": ("The basti churned with a khaja (churning stick) destroys Vāta and makes strength and colour (complexion). "
             "A new recipe: one prasṛta each of oil, prasannā (probably clear liquor), honey and ghee; it goes on in line 05.04.85."),
    "limits": ("Line 1 appears to follow the measures of line 05.04.82, which are partly conjectural. Prasannā is probable only. "
               "The new recipe's use is stated only in line 05.04.85."),
    "explain_hi": ("पहली पंक्ति पिछले श्लोक की मात्राओं वाली बस्ति को पूरा करती लगती है: खज यानी मथानी से मथी हुई बस्ति वात का नाश करती है और बल तथा वर्ण यानी रंग-रूप देती है। "
                   "दूसरी पंक्ति एक नया नुस्खा शुरू करती है: तेल, प्रसन्ना यानी सम्भवतः मदिरा का निथरा भाग, मधु और घी, हर एक का एक-एक प्रसृत। "
                   "यह नुस्खा पंक्ति ०५.०४.८५ में आगे चलता है, जहाँ इसे वात को जीतने वाला कहा गया है।"),
    "hook": "मथानी से मथो: वात भागे, बल और रंग आए; फिर तेल-प्रसन्ना-मधु-घी, एक-एक प्रसृत।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "With what is the basti churned in verse 43?",
            ("A khaja (churning stick)",
             "खजेन मथितः: churned with the khaja."),
            [("A pestle and a stone mortar", "No pestle or mortar is named in verse 43."),
             ("The physician's own hands", "No hand is named; खजेन is the instrument."),
             ("A ladle of wood (darvī)", "No ladle is named in verse 43.")],
            "खज = churning stick; the instrumental खजेन names the tool.",
            "खज = churning stick."),
        match(1, "Match each word of verse 43 to its meaning as the card gives it.",
              [["खज", "churning stick"], ["वातघ्न", "Vāta-destroying"], ["बलवर्णकृत्", "making strength and colour"],
               ["प्रसन्ना", "probably clear liquor"], ["क्षौद्र", "honey"]],
              "Line 1 gives the tool and the effects; line 2 the new items.",
              "खज = churning stick; वातघ्न = Vāta-destroying; बलवर्णकृत् = strength- and colour-making; प्रसन्ना = clear liquor (probable); क्षौद्र = honey."),
        order(2, "Put the four one-prasṛta items of verse 43, line 2, in the verse's order.",
              ["तैल (oil)", "प्रसन्ना (clear liquor)", "क्षौद्र (honey)", "सर्पिस् (ghee)"],
              "The genitive compound runs oil, prasannā, honey, ghee.",
              "तैल · प्रसन्ना · क्षौद्र · सर्पिस्.",
              role="extend",
              teaches="Line 2 of verse 43: one prasṛta each of taila, prasannā, kṣaudra and sarpis (oil, clear liquor, honey, ghee)."),
        mcq("discriminate", 3, "Which rule turns मथितः into मथितो before बस्तिः in verse 43?",
            ("-अः before a voiced sound becomes -ओ",
             "ब is voiced, so मथितः + बस्तिः → मथितो बस्तिः."),
            [("-अः before any consonant becomes -ओ", "Before unvoiced sounds it becomes श्/ष्/स् or stays: अश्च, अस्त."),
             ("-इः before a voiced sound becomes -ओ", "-इः before a voiced sound becomes -इर्, as in बस्तिर्वातघ्नो."),
             ("The visarga drops and अ grows long", "That is not a sandhi rule; -आः loses the visarga, -अः gives -ओ.")],
            "The same rule gives वातघ्नो before बल.",
            "-अः + voiced consonant → -ओ."),
        multi("apply", 4, "Which does verse 43 say the khaja-churned basti does?",
              [("Destroys Vāta", "Right: वातघ्नः."),
               ("Makes strength", "Right: बल- in बलवर्णकृत्."),
               ("Makes colour (complexion)", "Right: वर्ण- in बलवर्णकृत्."),
               ("Destroys Kapha", "Kapha is not named in verse 43."),
               ("Destroys worms", "Worms are named in lines 05.04.88 and 05.04.91, not here.")],
              [0, 1, 2],
              "वातघ्नो बलवर्णकृत्: Vāta-destroying, strength- and colour-making.",
              "Effects of verse 43: वात-नाश, बल, वर्ण."),
        mcq("transfer", 5, "Like एक + एकः → एकैकः (one each), how does invented तत्र + एव join?",
            ("तत्रैव",
             "अ + ए → ऐ, as in एकैकः."),
            [("तत्रेव", "ए would come from अ + इ, not अ + ए."),
             ("तत्रोव", "ओ comes from अ + उ."),
             ("तत्रयेव", "अय् comes from ए before a vowel, not from अ.")],
            "अ/आ + ए/ऐ → ऐ.",
            "अ + ए → ऐ.",
            teaches="अ or आ before ए or ऐ gives ऐ: एक + एकः → एकैकः; तत्र + एव → तत्रैव."),
    ],
}

# ---------------------------------------------------------------- unit 44
AUTHORED["44"] = {
    "title": "बिल्वादिमूल और कौलत्थ; पटोल-निम्ब",
    "question": "Which decoctions complete the Vāta-conquering basti of verse 44, and which bitter drugs begin the next recipe?",
    "rule": ("With the one-prasṛta items of line 05.04.84 come (prasṛtas) from the decoction of roots beginning with bilva (bael) "
             "and from kaulattha (horse gram); that basti conquers Vāta. Then the water of paṭola, nimba, bhūtīka, rāsnā and a fifth drug."),
    "limits": ("काथ is read as क्वाथ, द्धौ as द्वौ (two) and समच्छद as saptacchada by conjecture: no question on the counts or the fifth drug. "
               "Which roots follow bilva is not listed. Bhūtīka and rāsnā are disputed."),
    "explain_hi": ("पहली पंक्ति पिछले नुस्खे को पूरा करती लगती है: बिल्व यानी बेल आदि की जड़ों के काढ़े से और कुलत्थ यानी कुलथी से (प्रसृत), और वह बस्ति वात को जीतती है। "
                   "बेल के साथ कौन-सी जड़ें हैं, पाठ नहीं गिनाता; छपा ‘काथ’ क्वाथ और ‘द्धौ’ अनुमानित पाठ पर ‘द्वौ’ (दो) है। "
                   "दूसरी पंक्ति नया नुस्खा खोलती है: पटोल यानी परवल, निम्ब यानी नीम, भूतीक, रास्ना और पाँचवाँ द्रव्य, जो अनुमानित पाठ पर सप्तच्छद यानी छतिवन है, इनका जल। "
                   "पाठ ‘जल’ कहता है, काढ़ा नहीं।"),
    "hook": "बेल-जड़ और कुलथी: वात जीतो; फिर परवल-नीम-भूतीक-रास्ना का जल।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What does verse 44 say the basti with bilva roots and kaulattha conquers?",
            ("Vāta",
             "स वातजित्: that (basti) conquers Vāta."),
            [("Kapha", "Kapha is not named in verse 44."),
             ("Pitta", "Pitta is not named in verse 44."),
             ("Worms", "Worms are named in line 05.04.88, not here.")],
            "वातजित् = Vāta-conquering.",
            "-जित् = conquering."),
        match(1, "Match each clear word of verse 44 to its meaning as the card gives it.",
              [["बिल्व", "bael"], ["कौलत्थ", "horse gram"], ["पटोल", "pointed gourd"], ["निम्ब", "neem"], ["अम्भस्", "water"]],
              "Bilva, kaulattha, paṭola and nimba are standard identifications.",
              "बिल्व = bael; कौलत्थ = horse gram; पटोल = pointed gourd; निम्ब = neem; अम्भस् = water."),
        order(2, "Put these drugs of verse 44, line 2, in the verse's order.",
              ["पटोल", "निम्ब", "भूतीक", "रास्ना"],
              "The compound runs paṭola, nimba, bhūtīka, rāsnā; the fifth name follows in the next token.",
              "पटोल · निम्ब · भूतीक · रास्ना.",
              role="extend",
              teaches="Line 2 of verse 44 names paṭola (pointed gourd), nimba (neem), bhūtīka and rāsnā, then a fifth drug, and their water."),
        mcq("discriminate", 3, "In स वातजित् of verse 44, why does सः lose its visarga?",
            ("सः drops it before a consonant",
             "The pronoun सः (and एषः) drops the visarga before any consonant: स वातजित्."),
            [("Any -अः drops it before व", "Other -अः words become -ओ before voiced sounds: मथितो बस्तिः (line 05.04.83)."),
             ("It is a print slip for सो", "No flag is raised; स before a consonant is regular."),
             ("स is a stem, not a pronoun", "स here is the pronoun that (basti), masculine nominative.")],
            "सः + वातजित् → स वातजित्.",
            "सः/एषः + consonant → स/एष."),
        mcq("apply", 4, "Of what preparation of paṭola and the rest does verse 44 speak?",
            ("Their water (अम्भस्)",
             "…अम्भसः: of the water; the notes say the text says water, not decoction."),
            [("Their decoction (क्वाथ)", "Decoction is named for bilva roots in line 1, not for paṭola."),
             ("Their paste (कल्क)", "No paste is named for them in verse 44."),
             ("Their juice (स्वरस)", "No juice is named in verse 44.")],
            "The text says ambhas, water; nothing is added.",
            "अम्भस् = water."),
        mcq("transfer", 5, "Like बिल्व + आदि → बिल्वादि, how does invented पटोल + आदि join?",
            ("पटोलादि",
             "अ + आ → आ, as in बिल्वादि."),
            [("पटोलेदि", "ए would come from अ + इ."),
             ("पटोलौदि", "औ would come from अ + ओ/औ."),
             ("पटोल्यादि", "य् comes from इ/ई before a vowel.")],
            "Like vowels merge into the long vowel: अ + आ → आ.",
            "अ + आ → आ.",
            teaches="अ or आ before अ or आ merges into आ: बिल्व + आदि → बिल्वादि; पटोल + आदि → पटोलादि."),
    ],
}

# ---------------------------------------------------------------- unit 45
AUTHORED["45"] = {
    "title": "बस्तिः सर्षपकल्कवान् सपञ्चतिक्तः",
    "question": "What goes into the basti of verse 45, and which disorders does it destroy?",
    "rule": ("A prasṛta (of each water of line 05.04.86) separately, and one from ghee; the basti has a paste of mustard and the five "
             "bitters (pañcatikta), and destroys abhiṣyanda, worms (kṛmi), kuṣṭha (skin disease) and prameha (urinary disorders)."),
    "limits": ("Whether the five bitters are the five drugs of line 05.04.86 is not stated. Abhiṣyanda (oozing, congestion) stays in Sanskrit; "
               "its eye sense is not stated here. Kṛmi and prameha are probable renderings, kuṣṭha standard."),
    "explain_hi": ("यह श्लोक पंक्ति ०५.०४.८६ से चले नुस्खे को पूरा करता लगता है: (हर जल का) एक प्रसृत अलग-अलग, और घी से भी। "
                   "बस्ति में सरसों का कल्क यानी लुगदी है और पञ्चतिक्त यानी पाँच तिक्त द्रव्य; ये वही पाँच हैं जो पंक्ति ०५.०४.८६ में गिने गए, पाठ यह नहीं कहता। "
                   "यह बस्ति अभिष्यन्द (बहना, जमाव), कृमि यानी कीड़े, कुष्ठ यानी त्वचा रोग (परम्परा से कोढ़) और प्रमेह यानी मूत्र-विकार (सम्भवतः मधुमेह से जुड़ा) का नाश करती है।"),
    "hook": "सरसों की लुगदी, पाँच तिक्त: अभिष्यन्द, कीड़े, कोढ़ और प्रमेह, चारों का नाश।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "A paste of which drug does the basti of verse 45 have?",
            ("Mustard (sarṣapa)",
             "सर्षपकल्कवान्: having a paste of mustard."),
            [("Long pepper (pippalī)", "Pippalī paste is in line 05.04.91."),
             ("Liquorice (madhuka)", "Liquorice is not named in verse 45."),
             ("Vetiver (uśīra)", "Uśīra is in line 05.04.74.")],
            "सर्षप-कल्क-वान्: having (-वान्) a paste (कल्क) of mustard (सर्षप).",
            "सर्षप = mustard."),
        match(1, "Match each word of verse 45 to its meaning as the card gives it.",
              [["अभिष्यन्द", "oozing, congestion"], ["कृमि", "worms"], ["कुष्ठ", "skin disease"],
               ["प्रमेह", "urinary disorders"], ["सर्षप", "mustard"]],
              "Four disorders destroyed and the drug of the paste.",
              "अभिष्यन्द = oozing; कृमि = worms; कुष्ठ = skin disease; प्रमेह = urinary disorders; सर्षप = mustard."),
        order(2, "Put the disorders that the basti of verse 45 destroys in the verse's order.",
              ["अभिष्यन्द", "कृमि", "कुष्ठ", "प्रमेह"],
              "The compound runs abhiṣyanda, kṛmi, kuṣṭha, prameha, then -हा (destroyer).",
              "अभिष्यन्द · कृमि · कुष्ठ · प्रमेह.",
              role="extend",
              teaches="Verse 45 ends: (the basti) destroying abhiṣyanda, kṛmi (worms), kuṣṭha (skin disease) and prameha (urinary disorders)."),
        mcq("discriminate", 3, "Which split of पृथगाज्याच्च in verse 45 is right?",
            ("पृथक् + आज्यात् + च",
             "क् before a vowel becomes ग्; त् before च becomes च्."),
            [("पृथक् + आज्यम् + च", "म् before च gives anusvara: आज्यं च."),
             ("पृथक् + आज्यः + च", "-अः before च gives -अश्: आज्यश्च."),
             ("पृथक् + आज्ये + च", "ए does not change before च: आज्ये च.")],
            "पृथक् (separately) + आज्यात् (from ghee) + च (and).",
            "क् + vowel → ग्; त् + च → च्च."),
        multi("apply", 4, "Which disorders does verse 45 say the basti destroys?",
              [("Abhiṣyanda", "Right: अभिष्यन्द- opens the compound."),
               ("Worms (kṛmi)", "Right: कृमि-."),
               ("Kuṣṭha (skin disease)", "Right: कुष्ठ-."),
               ("Prameha (urinary disorders)", "Right: प्रमेह-."),
               ("Ānāha (distension)", "Ānāha is named in line 05.04.95."),
               ("Mūtrakṛcchra (painful urination)", "Mūtrakṛcchra is named in line 05.04.95.")],
              [0, 1, 2, 3],
              "अभिष्यन्द-कृमि-कुष्ठ-प्रमेह-हा: destroyer of these four.",
              "Verse 45: four disorders, one compound ending in -हा."),
        mcq("transfer", 5, "Like सर्षपकल्कवान् (having mustard paste), which invented word says a basti has a paste of pippalī?",
            ("पिप्पलीकल्कवान्",
             "-वान् (masc. nom. sg.) = having; basti is masculine."),
            [("पिप्पलीकल्कवती", "Feminine; basti is masculine in Sanskrit."),
             ("पिप्पलीकल्कवन्तः", "Plural; one basti is meant."),
             ("पिप्पलीकल्कम्", "Only the paste itself, not having a paste.")],
            "The suffix -वत् (nom. sg. m. -वान्) means having.",
            "-वान् = having (m. nom. sg.).",
            teaches="-वत् (masculine nominative singular -वान्) makes a having-word: सर्षपकल्कवान्, पिप्पलीकल्कवान् बस्तिः."),
    ],
}

# ---------------------------------------------------------------- unit 46
AUTHORED["46"] = {
    "title": "विडङ्गत्रिफलाशिग्रुफलमुस्ता",
    "question": "Which drugs give the decoctions of verse 46, and how are the decoctions and oil combined?",
    "rule": ("Viḍaṅga, triphalā, śigru fruit, mustā and a fifth drug give decoctions (kaṣāya): five prasṛtas of decoctions and one "
             "from oil are churned together; the nirūha follows in line 05.04.91."),
    "limits": ("The fifth name, printed आखुकर्णिजाः, is read ākhukarṇikā by conjecture (identity disputed): no question on it. "
               "Triphalā counts as one item. Kaṣāya here is the preparation (decoction), not the astringent taste."),
    "explain_hi": ("यह श्लोक एक नया नुस्खा देता है। पहली पंक्ति में विडङ्ग यानी वायविडंग, त्रिफला (हरड़, बहेड़ा, आँवला; एक द्रव्य गिना गया), शिग्रु यानी सहजन का फल, मुस्ता यानी नागरमोथा और पाँचवाँ नाम, जो अनुमानित पाठ पर आखुकर्णिका है। "
                   "दूसरी पंक्ति कहती है: इन के काढ़े पाँच प्रसृत, तेल से एक; इन्हें मथकर। "
                   "यहाँ ‘कषाय’ काढ़ा है, कसैला रस नहीं। वाक्य पंक्ति ०५.०४.९१ के निरूह पर पूरा होता है।"),
    "hook": "वायविडंग, त्रिफला, सहजन-फल, मोथा: पाँच प्रसृत काढ़ा, एक तेल, मथ डालो।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What does कषायाः mean in verse 46?",
            ("Decoctions",
             "Here kaṣāya is the preparation, decoction, measured in prasṛtas."),
            [("Astringent tastes", "Kaṣāya as taste is not meant: the notes say preparation."),
             ("Pastes", "Paste is कल्क, not कषाय."),
             ("Powders", "Powder (चूर्ण) is not named in verse 46.")],
            "कषायाः प्रसृताः पञ्च: five prasṛtas of decoctions.",
            "कषाय (preparation) = decoction, काढ़ा."),
        match(1, "Match each clear drug of verse 46 to its identification as the card gives it.",
              [["विडङ्ग", "false black pepper"], ["त्रिफला", "the three fruits"], ["शिग्रुफल", "drumstick fruit"],
               ["मुस्ता", "nutgrass"]],
              "All four are standard identifications.",
              "विडङ्ग = false black pepper; त्रिफला = the three fruits; शिग्रुफल = drumstick fruit; मुस्ता = nutgrass."),
        order(2, "Put these drugs of verse 46 in the verse's order.",
              ["विडङ्ग", "त्रिफला", "शिग्रुफल", "मुस्ता"],
              "The compound runs viḍaṅga, triphalā, śigru fruit, mustā; a fifth (conjectural) name ends it.",
              "विडङ्ग · त्रिफला · शिग्रुफल · मुस्ता.",
              role="extend",
              teaches="Line 1 of verse 46 lists viḍaṅga, triphalā, the fruit of śigru, mustā and a fifth drug, whose decoctions are used."),
        mcq("discriminate", 3, "What does the form विमथ्य in verse 46 show?",
            ("An absolutive in -य: having churned",
             "With the prefix वि- the absolutive takes -य, not -त्वा."),
            [("A past participle: churned", "The participle is मथित (line 05.04.83), not विमथ्य."),
             ("An optative: one should churn", "An optative would end in -एत्/-ईयात्."),
             ("A future: one will churn", "A future would have -स्य-/-ष्य-.")],
            "विमथ्य तान्: having churned them.",
            "Prefix + root → absolutive in -य."),
        mcq("apply", 4, "What is done to the decoctions and oil in verse 46?",
            ("They are churned together",
             "विमथ्य तान्: having churned them."),
            [("They are boiled down by half", "No boiling down is said in verse 46."),
             ("They are cooled and strained", "No cooling or straining is said."),
             ("They are left to ferment", "No fermenting is said in verse 46.")],
            "Five prasṛtas of decoction and one of oil are churned.",
            "वि + √मथ् = churn."),
        mcq("transfer", 5, "Like वि + √मथ् → विमथ्य, which invented absolutive means having joined, from सम् + √युज्?",
            ("संयुज्य",
             "Prefix + root: the absolutive ends in -य."),
            [("संयुक्त्वा", "-त्वा is used without a prefix; with सम्- it is -य."),
             ("संयुक्तः", "Past participle: joined, not having joined."),
             ("संयोक्तुम्", "Infinitive: to join.")],
            "With a prefix the absolutive takes -य; without, -त्वा.",
            "Prefixed absolutive: -य.",
            teaches="With a prefix the absolutive ends in -य (विमथ्य, संयुज्य); without one it ends in -त्वा (कृत्वा)."),
    ],
}

# ---------------------------------------------------------------- unit 47
AUTHORED["47"] = {
    "title": "निरूहः कृमिहा",
    "question": "What does the nirūha of verse 47 destroy, which paste joins it, and which drugs begin the next list?",
    "rule": ("The churned decoctions give a nirūha that destroys worms (kṛmi), joined with a paste (kalka) of vella and pippalī "
             "(long pepper). Then a list: payasyā, ikṣu (sugarcane), sthirā, rāsnā, vidārī (Indian kudzu), honey and ghee."),
    "limits": ("Vella, payasyā, sthirā and rāsnā are disputed. The printed ending सर्पिषः may stand for सर्पिषाम् (an open note): "
               "no question on it. The use of the new list is stated in line 05.04.93."),
    "explain_hi": ("पहली पंक्ति पिछले श्लोक को पूरा करती लगती है: (मथे हुए काढ़ों से) निरूह बस्ति बनती है जो कृमि यानी कीड़ों का नाश करती है, वेल्ल और पिप्पली यानी पीपर के कल्क से युक्त। "
                   "वेल्ल की पहचान विवादित है (कभी विडङ्ग माना जाता है)। "
                   "दूसरी पंक्ति नई सूची खोलती है: पयस्या (विवादित), इक्षु यानी गन्ना, स्थिरा (विवादित), रास्ना, विदारी यानी विदारीकन्द, मधु और घी; "
                   "यह सूची पंक्ति ०५.०४.९३ में ‘एक-एक प्रसृत’ तक चलती है।"),
    "hook": "कीड़े भगाने वाला निरूह: वेल्ल-पीपर की लुगदी; फिर पयस्या से घी तक सात नाम।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What does the nirūha of verse 47 destroy?",
            ("Worms (kṛmi)",
             "निरूहः कृमिहा: the nirūha destroying worms."),
            [("Burning (dāha)", "Burning is not named in verse 47."),
             ("Vāta (वात)", "Vāta-conquering was the basti of line 05.04.85."),
             ("Distension (ānāha)", "Ānāha is named in line 05.04.95.")],
            "कृमि-हा: worm-destroying.",
            "कृमिहा = worm-destroying."),
        match(1, "Match each word of verse 47 to its meaning as the card gives it.",
              [["पिप्पली", "long pepper"], ["इक्षु", "sugarcane"], ["विदारी", "Indian kudzu"], ["कल्क", "paste"], ["क्षौद्र", "honey"]],
              "Pippalī, ikṣu and vidārī are standard identifications.",
              "पिप्पली = long pepper; इक्षु = sugarcane; विदारी = Indian kudzu; कल्क = paste; क्षौद्र = honey."),
        order(2, "Put these items of verse 47, line 2, in the verse's order.",
              ["पयस्या", "इक्षु", "स्थिरा", "रास्ना", "विदारी", "क्षौद्र"],
              "The compound runs payasyā, ikṣu, sthirā, rāsnā, vidārī, honey (and ghee last).",
              "पयस्या · इक्षु · स्थिरा · रास्ना · विदारी · क्षौद्र.",
              role="extend",
              teaches="Line 2 of verse 47 lists payasyā, ikṣu, sthirā, rāsnā, vidārī, kṣaudra (honey) and sarpis (ghee)."),
        mcq("discriminate", 3, "Which split of पयस्येक्षु in verse 47 is right?",
            ("पयस्या + इक्षु",
             "आ + इ → ए: पयस्या + इक्षु = पयस्येक्षु."),
            [("पयस्ये + इक्षु", "ए before इ becomes अय् or stays apart: पयस्य इक्षु."),
             ("पयस्य + ऐक्षु", "अ + ऐ gives ऐ: it would read पयस्यैक्षु."),
             ("पयसि + इक्षु", "इ + इ gives ई: it would read पयसीक्षु.")],
            "पयस्या (a disputed drug) + इक्षु (sugarcane).",
            "आ + इ → ए."),
        mcq("apply", 4, "Which two drugs make the paste of the nirūha in verse 47?",
            ("Vella and pippalī",
             "वेल्लपिप्पलीकल्कयोजितः: joined with a paste of vella and pippalī."),
            [("Mustard and the bitters", "That paste is in line 05.04.87-88."),
             ("Honey and the ghee", "Honey and ghee are in the new list of line 2."),
             ("Śigru fruit and mustā", "These gave decoctions in line 05.04.89.")],
            "The paste of verse 47: vella (disputed) and pippalī (long pepper).",
            "Paste: वेल्ल + पिप्पली."),
        mcq("transfer", 5, "Like कृमि + हन् → कृमिहा (worm-destroying), which invented word means Kapha-destroying in the same form?",
            ("कफहा",
             "Compounds in -हन् take the nominative singular -हा."),
            [("कफहः", "-हः is not the nominative of -हन्."),
             ("कफहन्", "That is the bare stem, not the nominative."),
             ("कफहम्", "-हम् is not a form of -हन्.")],
            "X-हन् (destroying X) gives the masculine nominative singular X-हा.",
            "-हन् → nom. sg. -हा.",
            teaches="Words in -हन् (destroying) have the masculine nominative singular -हा: कृमिहा, कफहा, प्रमेहहा."),
    ],
}

# ---------------------------------------------------------------- unit 48
AUTHORED["48"] = {
    "title": "एकैकः प्रसृतो बस्तिः",
    "question": "How much of each listed drug goes into the basti of verse 48, and what does that basti make?",
    "rule": ("One prasṛta each (of the list of line 05.04.92): the basti, with a paste of kṛṣṇā (long pepper) on a conjectural reading, "
             "makes virility (vṛṣatva). Then four (measures) from oil, cow's urine, dadhimaṇḍa (watery part of curd) and sour kāñjika."),
    "limits": ("Low confidence. कृष्णाकल्कौ is read as kalkāt by conjecture: no question on it. The noun counted by four is not stated; "
               "whether amla stands apart is open. The sentence runs on into line 05.04.95."),
    "explain_hi": ("पहली पंक्ति पिछली सूची को पूरा करती लगती है: (हर द्रव्य का) एक-एक प्रसृत; यह बस्ति, अनुमानित पाठ पर कृष्णा यानी पीपर के कल्क से, वृषत्व यानी पुंसत्व-शक्ति देती है। "
                   "दूसरी पंक्ति नया नुस्खा खोलती है: चार, तेल, गोमूत्र, दधिमण्ड यानी दही का पानी और खट्टी काँजी यानी खट्टा किण्वित पेय। "
                   "‘चार’ किसके हैं (प्रसृत?), पाठ नहीं कहता; वाक्य पंक्ति ०५.०४.९५ में आगे चलता है।"),
    "hook": "एक-एक प्रसृत: वृषत्व; फिर तेल, गोमूत्र, दही-पानी, खट्टी काँजी: चार।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What does the basti of verse 48 make, by the card?",
            ("Virility (vṛṣatva)",
             "वृषत्वकृत्: making virility."),
            [("Strength and colour", "Strength and colour were said in line 05.04.83."),
             ("Sharpness (tīkṣṇatva)", "Sharpness is the topic of line 05.04.98."),
             ("Mildness (mārdava)", "Mildness is the topic of line 05.04.99.")],
            "वृषत्व-कृत्: virility-making.",
            "वृषत्व = virility."),
        match(1, "Match each word of verse 48 to its meaning as the card gives it.",
              [["एकैकः", "one each"], ["वृषत्वकृत्", "virility-making"], ["गोमूत्र", "cow's urine"],
               ["दधिमण्ड", "watery part of curd"], ["काञ्जिक", "a fermented gruel"]],
              "These words are clear; the paste word is left out.",
              "एकैकः = one each; वृषत्वकृत् = virility-making; गोमूत्र = cow's urine; दधिमण्ड = curd water; काञ्जिक = fermented gruel."),
        order(2, "Put the items of verse 48, line 2, in the verse's order.",
              ["तैल", "गोमूत्र", "दधिमण्ड", "अम्लकाञ्जिक"],
              "The compound runs oil, cow's urine, dadhimaṇḍa, sour kāñjika.",
              "तैल · गोमूत्र · दधिमण्ड · अम्लकाञ्जिक.",
              role="extend",
              teaches="Line 2 of verse 48: four, from oil, cow's urine, dadhimaṇḍa (curd water) and sour kāñjika (fermented gruel)."),
        mcq("discriminate", 3, "Which split of चत्वारस्तैल in verse 48 is right?",
            ("चत्वारः + तैल-",
             "-अः before त becomes -अस्: चत्वारस्तैल."),
            [("चत्वाराः + तैल-", "A long आ would show in the print: चत्वारास्तैल."),
             ("चत्वारि + तैल-", "The neuter would read चत्वारि तैल-; no स् appears."),
             ("चत्वार + स्तैल-", "स्तैल is no word; the स् comes from the visarga.")],
            "चत्वारः (four, masc. nom.) + तैल- (oil).",
            "-अः + त → -अस्त."),
        mcq("apply", 4, "Which of these is NOT in the list of verse 48, line 2?",
            ("Honey (kṣaudra)",
             "Honey is in line 05.04.92, not in the list of four."),
            [("Oil (taila)", "Oil opens the list."),
             ("Cow's urine (gomūtra)", "Gomūtra is the second item."),
             ("Curd water (dadhimaṇḍa)", "Dadhimaṇḍa is the third item.")],
            "The four: oil, cow's urine, curd water, sour kāñjika.",
            "Line 2 of verse 48: तैल, गोमूत्र, दधिमण्ड, अम्लकाञ्जिक."),
        mcq("transfer", 5, "Like वृषत्वकृत् (virility-making), which invented word means strength-making?",
            ("बलकृत्",
             "-कृत् at the end of a compound means making."),
            [("बलकृत", "Past participle: made by strength."),
             ("बलं कृत्वा", "Absolutive: having made strength, not making."),
             ("बलकर्तुम्", "Infinitive: to make strength.")],
            "X-कृत् = X-making (an agent noun at the end of a compound).",
            "-कृत् = making.",
            teaches="-कृत् at the end of a compound makes an agent word: वृषत्वकृत् (virility-making), बलकृत् (strength-making)."),
    ],
}

# ---------------------------------------------------------------- unit 49
AUTHORED["49"] = {
    "title": "बस्तिः कवोष्णः सानाहे मूत्रकृच्छ्रे",
    "question": "Where is the slightly warm basti best in verse 49, and what is wanted when mild bastis dull a patient?",
    "rule": ("A slightly warm (kavoṣṇa) basti is held best in one with ānāha (belly distension with obstruction) and in mūtrakṛcchra "
             "(painful urination). In one dulled (jaḍībhūta) by mild bastis, another, sharp basti is desired."),
    "limits": ("The kavoṣṇa basti appears to be the one of line 05.04.94; the link is not stated outright. परः is read as best, not other. "
               "What makes a basti sharp is given in line 05.04.98."),
    "explain_hi": ("पहली पंक्ति पिछले नुस्खे की बस्ति को पूरा करती लगती है: थोड़ी गुनगुनी बस्ति सानाह यानी आनाह (पेट फूलना, मल-वायु का रुकना) वाले में और मूत्रकृच्छ्र यानी कष्ट से मूत्र आने में श्रेष्ठ मानी गई है। "
                   "दूसरी पंक्ति एक नियम देती है: जो मृदु बस्तियों से जड़ हो गया हो, यानी उन पर प्रतिक्रिया न दे, उसमें दूसरी, तीक्ष्ण बस्ति चाही जाती है। "
                   "‘परः’ को ‘श्रेष्ठ’ पढ़ा गया, क्योंकि ‘दूसरी’ के लिए आगे ‘अन्यः’ है।"),
    "hook": "पेट फूला या मूत्र अटका: गुनगुनी बस्ति; मृदु से सुस्त हुआ: तीक्ष्ण बस्ति।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "Which basti does verse 49 desire for one dulled by mild bastis?",
            ("A sharp one (tīkṣṇa)",
             "तीक्ष्णोऽन्यो बस्तिरिष्यते: another, sharp basti is desired."),
            [("A cool, sweet one", "Oily, sweet, cool is for one depleted by sharp ones (line 05.04.97)."),
             ("Another mild one", "Mild bastis are what dulled him."),
             ("No basti at all", "Verse 49 desires another basti.")],
            "मृदुबस्तिजडीभूते तीक्ष्णः: dulled by mild ones, give a sharp one.",
            "Dulled by mild → sharp."),
        match(1, "Match each word of verse 49 to its meaning.",
              [["कवोष्ण", "slightly warm"], ["आनाह", "belly distension with obstruction"], ["मूत्रकृच्छ्र", "painful urination"],
               ["जडीभूत", "become dull"], ["तीक्ष्ण", "sharp"]],
              "Two conditions for the slightly warm basti; one for the sharp one.",
              "कवोष्ण = slightly warm; आनाह = distension; मूत्रकृच्छ्र = painful urination; जडीभूत = dulled; तीक्ष्ण = sharp."),
        order(2, "Put these phrases of verse 49 in the verse's order.",
              ["बस्तिः कवोष्णः", "सानाहे", "मूत्रकृच्छ्रे परो मतः", "मृदुबस्तिजडीभूते", "तीक्ष्णो ऽन्यो बस्तिरिष्यते"],
              "The warm basti and its two conditions; then the dulled patient and the sharp basti.",
              "बस्तिः कवोष्णः · सानाहे · मूत्रकृच्छ्रे परो मतः · मृदुबस्तिजडीभूते · तीक्ष्णो ऽन्यो बस्तिरिष्यते.",
              role="extend",
              teaches="Verse 49: slightly warm basti, in ānāha and mūtrakṛcchra, held best; in one dulled by mild bastis, another, sharp basti."),
        mcq("discriminate", 3, "Which split of बस्तिरिष्यते in verse 49 is right?",
            ("बस्तिः + इष्यते",
             "-इः before a vowel becomes -इर्: बस्तिरिष्यते."),
            [("बस्तिः + एष्यते", "र् + ए would read बस्तिरेष्यते."),
             ("बस्ती + इष्यते", "ई + इ merges into ई: बस्तीष्यते."),
             ("बस्तिम् + इष्यते", "म् before a vowel stays: बस्तिमिष्यते.")],
            "बस्तिः (basti) + इष्यते (is desired).",
            "-इः + vowel → -इर्."),
        mcq("apply", 4, "A patient has ānāha. Which basti does verse 49 hold best?",
            ("A slightly warm one",
             "बस्तिः कवोष्णः सानाहे … परो मतः."),
            [("A sharp, strong one", "The sharp basti is for one dulled by mild bastis."),
             ("A cool one with honey", "Cool with honey and sugar is the jīvādāna basti of line 05.04.76."),
             ("An oily, mild one", "Oily and mild is for one depleted by sharp bastis (line 05.04.97).")],
            "Ānāha and mūtrakṛcchra: kavoṣṇa, slightly warm.",
            "कवोष्ण = slightly warm."),
        mcq("transfer", 5, "Like परः + मतः → परो मतः, how does invented हितः + मतः join?",
            ("हितो मतः",
             "-अः before a voiced sound becomes -ओ, as in परो मतः."),
            [("हितर्मतः", "र् comes from -इः/-उः, not from -अः."),
             ("हितस्मतः", "स् appears before त/थ, not before म."),
             ("हिता मतः", "Dropping to -आ happens with -आः, not -अः.")],
            "म is voiced, so -अः → -ओ.",
            "-अः + voiced consonant → -ओ.",
            teaches="-अः before a voiced consonant becomes -ओ: परः + मतः → परो मतः; हितः + मतः → हितो मतः."),
    ],
}

# ---------------------------------------------------------------- unit 50
AUTHORED["50"] = {
    "title": "तीक्ष्णैर्विकर्षिते स्निग्धः",
    "question": "What basti suits one depleted by sharp bastis in verse 50, and which drugs give sharpness?",
    "rule": ("In one drawn out (depleted) by sharp (bastis): an oily, sweet, cool, mild (basti). Sharpness comes by urine, "
             "bilva (bael), agni, salt, kṣāra and mustard."),
    "limits": ("Subject and verb are carried from line 05.04.96. Agni may be fire or the drug citraka (disputed); whose urine is not stated. "
               "Vikarṣita is literally drawn out; depleted is the likely sense."),
    "explain_hi": ("पहली पंक्ति पिछले नियम का उलटा देती है: जो तीक्ष्ण बस्तियों से खिंच गया यानी क्षीण हो गया हो, उसमें स्निग्ध, मधुर, शीतल और मृदु (बस्ति)। "
                   "‘बस्ति’ और ‘इष्यते’ पिछली पंक्ति से आते हैं। "
                   "दूसरी पंक्ति बताती है कि तीक्ष्णता किससे आती है: मूत्र, बिल्व यानी बेल, अग्नि, लवण, क्षार और सरसों से। "
                   "‘अग्नि’ आग भी हो सकता है और चित्रक नामक द्रव्य भी (विवादित); मूत्र किस पशु का, नहीं कहा।"),
    "hook": "तीक्ष्ण से थका: चिकना, मीठा, ठंडा, मृदु; तीखापन चाहिए: मूत्र, बेल, अग्नि, नमक, क्षार, सरसों।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What does तीक्ष्णत्वम् mean in verse 50?",
            ("Sharpness",
             "तीक्ष्ण (sharp) + -त्व (the quality): sharpness."),
            [("Mildness", "Mildness is मार्दव, line 05.04.99."),
             ("Oiliness", "Oiliness would be स्निग्धता or स्नेह."),
             ("Coolness", "Coolness would be शैत्य; शिशिर is the adjective cool.")],
            "तीक्ष्णत्वं मूत्र…सर्षपैः: sharpness by urine and the rest.",
            "-त्व = the quality of; तीक्ष्णत्व = sharpness."),
        match(1, "Match each word of verse 50, line 1, to its meaning.",
              [["स्निग्ध", "oily"], ["मधुर", "sweet"], ["शिशिर", "cool"], ["मृदु", "mild"], ["विकर्षित", "drawn out, depleted"]],
              "Four qualities of the basti for one depleted by sharp ones.",
              "स्निग्ध = oily; मधुर = sweet; शिशिर = cool; मृदु = mild; विकर्षित = drawn out."),
        order(2, "Put the sharpness drugs of verse 50 in the verse's order.",
              ["मूत्र", "बिल्व", "अग्नि", "लवण", "क्षार", "सर्षप"],
              "The compound runs urine, bilva, agni, salt, kṣāra, mustard.",
              "मूत्र · बिल्व · अग्नि · लवण · क्षार · सर्षप.",
              role="extend",
              teaches="Line 2 of verse 50: sharpness by mūtra (urine), bilva (bael), agni, lavaṇa (salt), kṣāra and sarṣapa (mustard)."),
        mcq("discriminate", 3, "Which of these is NOT among the sharpness drugs of verse 50?",
            ("Milk (kṣīra)",
             "Milk gives mildness, in line 05.04.99."),
            [("Salt (lavaṇa)", "Lavaṇa is the fourth sharpness item."),
             ("Kṣāra", "Kṣāra is the fifth sharpness item."),
             ("Mustard (sarṣapa)", "Sarṣapa closes the list.")],
            "The six: urine, bilva, agni, salt, kṣāra, mustard.",
            "Sharpness: मूत्र, बिल्व, अग्नि, लवण, क्षार, सर्षप."),
        mcq("apply", 4, "A patient was drawn out by sharp bastis. Which basti suits him, by verse 50?",
            ("Oily, sweet, cool, mild",
             "तीक्ष्णैर्विकर्षिते स्निग्धो मधुरः शिशिरो मृदुः."),
            [("Dry, sour, hot, sharp", "Sharp is what depleted him."),
             ("Warm, with salt, kṣāra", "Salt and kṣāra give sharpness."),
             ("Bitter, with mustard", "Mustard gives sharpness; bitter is not named.")],
            "Depleted by sharp → oily, sweet, cool, mild.",
            "Depleted by sharp → the opposite qualities."),
        mcq("transfer", 5, "Like तीक्ष्ण → तीक्ष्णत्वम् (sharpness), which invented -त्व word means mildness?",
            ("मृदुत्वम्",
             "-त्व nouns are neuter: nominative singular -त्वम्."),
            [("मृदुत्वः", "-त्व nouns are neuter, not masculine."),
             ("मृदुत्वा", "-त्वा is the absolutive ending, not the quality suffix."),
             ("मृदुत्वे", "Locative: in mildness, not the nominative.")],
            "Adjective + -त्व = the quality, neuter: तीक्ष्णत्वम्, मृदुत्वम्.",
            "-त्वम् = the quality (n. nom. sg.).",
            teaches="Adding -त्व to an adjective makes a neuter noun of the quality: तीक्ष्ण → तीक्ष्णत्वम् (sharpness), मृदु → मृदुत्वम् (mildness)."),
    ],
}

# ---------------------------------------------------------------- unit 51
AUTHORED["51"] = {
    "title": "क्षीराज्याद्यैस्तु मार्दवम्",
    "question": "By what, and when, is mildness to be produced in unit 51?",
    "rule": ("In contrast (tu) to the sharpness of line 05.04.98, mildness (mārdava) is to be produced, in due time, by milk, ghee and so on."),
    "limits": ("And so on is not listed. प्राप्तकालम् may also be read when the time has come. The unit does not say which patient "
               "needs mildness; line 05.04.100 starts a new sentence."),
    "explain_hi": ("यह गद्य-पंक्ति पिछली पंक्ति के उलटे पक्ष को कहती है। वहाँ तीक्ष्णता मूत्र, बेल, लवण आदि से आती थी; "
                   "यहाँ ‘तु’ (पर) से विरोध दिखाया गया है: मृदुता यानी मार्दव दूध, घी आदि से उत्पन्न करनी चाहिए। "
                   "‘प्राप्तकालम्’ का अर्थ ‘उचित समय पर’ या ‘समय आने पर’। ‘आदि’ में और कौन से द्रव्य हैं, नहीं गिनाया गया।"),
    "hook": "तीखापन मूत्र-नमक से; मृदुता दूध-घी से, समय पर।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By what does unit 51 say mildness is produced?",
            ("Milk, ghee and so on",
             "क्षीराज्याद्यैः: by milk, ghee and the rest."),
            [("Urine, salt and kṣāra", "These give sharpness, line 05.04.98."),
             ("Bilva and the mustard", "These give sharpness, line 05.04.98."),
             ("Agni and the kṣāra", "These give sharpness, line 05.04.98.")],
            "मार्दवं … क्षीराज्याद्यैः: mildness by milk, ghee and so on.",
            "Mildness: क्षीर, आज्य, आदि."),
        match(1, "Match each word of unit 51 to its meaning.",
              [["मार्दव", "mildness"], ["विधातव्य", "to be produced"], ["प्राप्तकालम्", "in due time"], ["तु", "but"], ["आज्य", "ghee"]],
              "The unit is one short sentence.",
              "मार्दव = mildness; विधातव्य = to be produced; प्राप्तकालम् = in due time; तु = but; आज्य = ghee."),
        order(2, "Put the words of unit 51 in the printed order.",
              ["प्राप्तकालं", "विधातव्यं", "क्षीराज्याद्यैस्तु", "मार्दवं"],
              "Time, the gerundive, the means with तु, and the subject last.",
              "प्राप्तकालं · विधातव्यं · क्षीराज्याद्यैस्तु · मार्दवं.",
              role="extend",
              teaches="Unit 51 reads: in due time is to be produced, by milk, ghee and the rest, but, mildness."),
        mcq("discriminate", 3, "Which split of क्षीराज्याद्यैस्तु in unit 51 is right?",
            ("क्षीर + आज्य + आद्यैः + तु",
             "-ऐः before त becomes -ऐस्: आद्यैस्तु."),
            [("क्षीर + आज्य + आद्यः + तु", "-अः before त gives -अस्: आद्यस्तु, with no ऐ."),
             ("क्षीर + आज्य + आद्ये + तु", "ए does not change before त: आद्ये तु."),
             ("क्षीर + आज्य + आद्यम् + तु", "म् before त gives anusvara: आद्यं तु.")],
            "क्षीर (milk) + आज्य (ghee) + आद्यैः (and the rest, instr. pl.) + तु (but).",
            "-ऐः + त → -ऐस्त."),
        mcq("apply", 4, "In unit 51, what does तु set mildness against?",
            ("The sharpness of line 05.04.98",
             "The notes: tu contrasts mildness with sharpness by urine and the rest."),
            [("The two cool jīvādāna bastis", "Jīvādāna closed at line 05.04.79."),
             ("The worm-destroying nirūha", "The nirūha of line 05.04.91 is not contrasted here."),
             ("The basti of the delicate one", "The delicate are named in line 05.04.80, not contrasted here.")],
            "Sharpness by urine and so on; but mildness by milk, ghee and so on.",
            "तु = but (contrast)."),
        mcq("transfer", 5, "Like वि + √धा → विधातव्यम् (to be produced), which invented gerundive means to be done, from √कृ?",
            ("कर्तव्यम्",
             "-तव्य is the gerundive: to be done."),
            [("कृत्वा", "Absolutive: having done."),
             ("कृतम्", "Past participle: done."),
             ("करोति", "Present: he does.")],
            "-तव्य added to the root (with guṇa) gives to be X-ed.",
            "-तव्य = to be (done).",
            teaches="The suffix -तव्य makes a gerundive, to be X-ed: विधातव्यम् (to be produced), कर्तव्यम् (to be done)."),
    ],
}


NOTES_HI = {
    "38": ("विश्वास: मध्यम। पंक्तियाँ ०५.०४.७३-७४; केवल द्रव्य-सूची, कोई क्रिया नहीं, प्रयोग नहीं कहा। पंक्ति ०५.०४.७२ ‘न्यग्रोधाद्यैश्चतुर्भिः’ पर रुकती है; "
           "यह सूची उसी से जुड़ी है या नहीं, पाठ नहीं बताता। ‘क्षीरकाकोली’ एक ही द्रव्य-नाम माना गया (क्षीर + काकोली दो नहीं)। "
           "छपाई: ‘मूर्व्वा’ में दोहरा व्, शब्द में मूर्वा लिखा (वर्तनी-सामान्यीकरण)। "
           "पहचान: बृहती, पृश्निपर्णी, शतावरी, काश्मर्य, बदरी, उशीर मानक; मूर्वा सम्भावित; क्षीरकाकोली, प्रियङ्गु विवादित। "
           "संधि जाँची: मूर्वास्तथोशीर = मूर्वाः + तथा + उशीर; प्रियंगवः = प्रियङ्गु का बहुवचन।"),
    "39": ("विश्वास: मध्यम। पंक्तियाँ ०५.०४.७५-७६, एक वाक्य लगता है (‘द्वौ’ और ‘बस्ती’ दोनों द्विवचन)। "
           "जीवादान का अर्थ यहाँ नहीं दिया गया; खुला प्रश्न (OPEN ०५.०४.७५): बाद की परम्परा और पंक्ति ७७-७९ के रक्त के आधार पर इसे सम्भवतः भारी रक्तस्राव माना जाता है, पर यह जाँचा नहीं गया, इसलिए इस पर प्रश्न नहीं। "
           "अञ्जन कौन-सा, और शर्करा किस रूप की, नहीं कहा। ‘शृते क्षीरे’ = उबाले हुए दूध में। "
           "संधि जाँची: घृतांजन = घृत + अञ्जन; समधुशर्करौ = स + मधु + शर्करा (बहुव्रीहि, द्विवचन)।"),
    "40": ("विश्वास: निम्न। पंक्तियाँ ०५.०४.७७-७८; ७७-७९ एक वाक्य लगता है (क्रिया ‘प्रशस्यते’ पंक्ति ७९ में)। "
           "खुला प्रश्न (OPEN ०५.०४.७७): ‘गो’ को अलग अविभक्त शब्द माना गया, जिससे पंक्ति में दो ‘अपि’ हो जाते हैं; छपा रूप सम्भवतः बिगड़ा है, इसलिए गाय वाले पाठ पर प्रश्न नहीं। "
           "text_flags: ‘दक्ष’ पशु नहीं, अनुमानित पाठ पर ऋक्ष (भालू); ‘अन्यज’ अस्पष्ट (अजा, बकरी, भी सम्भव, पर छन्द मेल नहीं खाता)। इनमें से किसी पर प्रश्न नहीं; शश, एण, मार्जार, महिषी, शोणित साफ़ हैं। "
           "जीवनीय गण के सदस्य यहाँ नहीं गिनाए गए। संधि जाँची: क्षीरैर्जीवनीय = क्षीरैः + जीवनीय; शशैण = शश + एण।"),
    "41": ("विश्वास: निम्न। पंक्तियाँ ०५.०४.७९-८०। पहली पंक्ति ७७-७८ का वाक्य पूरा करती लगती है; ‘सद्यस्कैः मृदितैः’ रक्तों से जुड़ते हैं या दूधों से, तय नहीं; ‘मृदित’ = मसला, या मला/मिलाया। "
           "दूसरी पंक्ति की क्रिया ‘वक्ष्यामि’ पंक्ति ८१ में। text_flag: छपा ‘एहनान्’ शब्द नहीं; अनुमानित पाठ पर ‘स्नेहनान्’ (स् छूटा), इस पर प्रश्न नहीं; निरूहान् और मृदून् साफ़ हैं। "
           "संधि जाँची: सद्यस्कैर्मृदितैर्बस्तिर्जीवादाने = सद्यस्कैः + मृदितैः + बस्तिः + जीवादाने; अथेमान् = अथ + इमान्।"),
    "42": ("विश्वास: निम्न। पंक्तियाँ ०५.०४.८१-८२। ‘वक्ष्यामि’ (भविष्य, उत्तम पुरुष एकवचन) पंक्ति ८० और ८१ दोनों पर लागू। "
           "‘कर्म’ सम्भवतः शोधन-कर्म (वमन, विरेचन आदि), पर पाठ केवल ‘कर्म से’ कहता है। प्रसृत = हथेली-भर, लगभग दो पल (मानक)। "
           "text_flags: ‘क्षीराद्धौ’ में ‘द्धौ’ अनुमानित पाठ पर ‘द्वौ’ (द्व/द्ध छपाई में मिलते हैं); ‘मधुनैल’ अनुमानित पाठ पर मधु-तैल (त/न), ‘एला’ भी सम्भव। "
           "इसलिए दूसरी पंक्ति की गिनतियों पर कोई प्रश्न नहीं। संधि जाँची: विप्लुतानां च = विप्लुतानाम् + च।"),
    "43": ("विश्वास: मध्यम। पंक्तियाँ ०५.०४.८३-८४। पहली पंक्ति पंक्ति ८२ की मात्राओं के बाद आती लगती है; दूसरी पंक्ति नया नुस्खा खोलती है जो पंक्ति ८५ में चलता है। "
           "खज = मथानी (मानक); वर्ण = रंग-रूप। प्रसन्ना = सम्भवतः किण्वित मदिरा का निथरा भाग। "
           "संधि जाँची: मथितो बस्तिः = मथितः + बस्तिः; बस्तिर्वातघ्नो = बस्तिः + वातघ्नः; वातघ्नो बल = वातघ्नः + बल; एकैकः = एक + एकः; प्रसृतस्तैल = प्रसृतः + तैल।"),
    "44": ("विश्वास: मध्यम। पंक्तियाँ ०५.०४.८५-८६। पहली पंक्ति पंक्ति ८४ का नुस्खा पूरा करती लगती है; ८६-८८ एक वाक्य लगता है। "
           "text_flags: ‘काथ’ = क्वाथ, ‘द्धौ’ = द्वौ (दोनों अनुमानित), ‘कौलत्थाद्धौ’ में भी वही; ‘समच्छद’ अनुमानित पाठ पर सप्तच्छद (छतिवन)। गिनतियों और पाँचवें द्रव्य पर प्रश्न नहीं। "
           "‘कौलत्थात्’ के साथ ‘काढ़ा’ समझा जाता है, जोड़ा नहीं गया। बिल्वादिमूल सम्भवतः बेल से शुरू पञ्चमूल, पर पाठ नहीं गिनाता। ‘अम्भसः’ = जल का/से; काढ़ा नहीं कहा। "
           "पहचान: पटोल, निम्ब मानक; रास्ना, भूतीक विवादित। संधि जाँची: स वातजित् = सः + वातजित्।"),
    "45": ("विश्वास: मध्यम। पंक्तियाँ ०५.०४.८७-८८; ८६ से चला वाक्य यहाँ पूरा होता लगता है। ‘आज्यात्’ = घी से (एक प्रसृत)। "
           "पञ्चतिक्त = पाँच तिक्त; पंक्ति ८६ के पाँच द्रव्य हो सकते हैं, पर पाठ यह नहीं कहता। अभिष्यन्द संस्कृत में रखा (बहना, जमाव); आँख का अर्थ यहाँ नहीं। "
           "पहचान: कुष्ठ मानक (त्वचा रोग, परम्परा से कोढ़); प्रमेह और कृमि सम्भावित। "
           "संधि जाँची: पृथगाज्याच्च = पृथक् + आज्यात् + च; सपंचतिक्तो ऽभिष्यंद = सपञ्चतिक्तः + अभिष्यन्द (छपाई में ऽ से पहले रिक्त स्थान)।"),
    "46": ("विश्वास: मध्यम। पंक्तियाँ ०५.०४.८९-९०; वाक्य पंक्ति ९१ के निरूह पर पूरा होता है। त्रिफला एक द्रव्य गिना गया, जैसा ‘पाँच काढ़े’ के लिए चाहिए। "
           "text_flag: छपा ‘आखुकर्णिजाः’; अनुमानित पाठ पर ‘आखुकर्णिकाः’ (पाँचवाँ द्रव्य), इस पर प्रश्न नहीं। ‘कषाय’ यहाँ काढ़ा है, कसैला रस नहीं। "
           "पहचान: विडङ्ग, त्रिफला, शिग्रु, मुस्ता मानक; आखुकर्णी/मूषाकर्णी विवादित। "
           "संधि जाँची: तैलादेको = तैलात् + एकः; विमथ्य = वि + √मथ् + य (उपसर्ग के साथ ल्यप्)।"),
    "47": ("विश्वास: मध्यम। पंक्तियाँ ०५.०४.९१-९२। पहली पंक्ति ८९-९० का वाक्य पूरा करती लगती है; दूसरी पंक्ति की सूची पंक्ति ९३ में ‘एकैकः प्रसृतः’ तक चलती है। "
           "text_flag और खुला प्रश्न (OPEN ०५.०४.९२): छपा ‘सर्पिषः’ एकवचन है, सम्भवतः ‘सर्पिषाम्’; समाहार-रूप में एकवचन भी ठीक हो सकता है; इस पर प्रश्न नहीं। "
           "पहचान: पिप्पली, इक्षु, विदारी मानक; वेल्ल (कभी विडङ्ग), पयस्या (क्षीरविदारी या क्षीरकाकोली), स्थिरा (प्रायः शालपर्णी), रास्ना विवादित। "
           "संधि जाँची: पयस्येक्षु = पयस्या + इक्षु; स्थिरारास्ना = स्थिरा + रास्ना।"),
    "48": ("विश्वास: निम्न। पंक्तियाँ ०५.०४.९३-९४। पहली पंक्ति पंक्ति ९२ की सूची पूरी करती लगती है। "
           "text_flag: छपा ‘कृष्णाकल्कौ’ (द्विवचन) का अर्थ नहीं बनता; अनुमानित पाठ पर ‘कल्कात्’ या ‘कल्कः’, इसलिए इस पर प्रश्न नहीं। कृष्णा = पिप्पली (मानक)। "
           "‘चत्वारः’ किसे गिनता है, नहीं कहा (प्रसृत सम्भव); ‘अम्ल’ अलग द्रव्य है या काञ्जिक का विशेषण, समास से तय नहीं। वाक्य पंक्ति ९५ में आगे। "
           "संधि जाँची: चत्वारस्तैल = चत्वारः + तैल; दधिमंडांम्ल = दधिमण्ड + अम्ल।"),
    "49": ("विश्वास: मध्यम। पंक्तियाँ ०५.०४.९५-९६। पहली पंक्ति पंक्ति ९४ की बस्ति को पूरा करती लगती है। ‘परः’ = श्रेष्ठ (‘दूसरा’ अर्थ कम सम्भव, क्योंकि आगे ‘अन्यः’ है)। "
           "पहचान: मूत्रकृच्छ्र (कष्ट से मूत्र) और आनाह (पेट फूलना, मल-वायु रुकना) मानक। ‘जडीभूत’ = सुस्त, यानी मृदु बस्ति पर प्रतिक्रिया न देना। "
           "छपाई: ‘तीक्ष्णो ऽन्यो’ में ऽ से पहले रिक्त स्थान। संधि जाँची: सानाहे = स + आनाहे; परो मतः = परः + मतः; तीक्ष्णोऽन्यो = तीक्ष्णः + अन्यः; बस्तिरिष्यते = बस्तिः + इष्यते।"),
    "50": ("विश्वास: मध्यम। पंक्तियाँ ०५.०४.९७-९८; दोनों अधूरे वाक्य: ‘बस्तिः’ और ‘इष्यते’ पंक्ति ९६ से, और ‘विधातव्यम्’ सम्भवतः पंक्ति ९९ से दोनों (तीक्ष्णत्व और मार्दव) पर लागू। "
           "‘विकर्षित’ = खींचा गया; ‘क्षीण’ सम्भावित अर्थ। ‘अग्नि’ आग या चित्रक (विवादित); मूत्र किस पशु का, नहीं कहा; क्षार संस्कृत में रखा। "
           "संधि जाँची: तीक्ष्णैर्विकर्षिते = तीक्ष्णैः + विकर्षिते; स्निग्धो मधुरः = स्निग्धः + मधुरः; शिशिरो मृदुः = शिशिरः + मृदुः; बिल्वाग्नि = बिल्व + अग्नि।"),
    "51": ("विश्वास: उच्च। पंक्ति ०५.०४.९९, गद्य। ‘तु’ मृदुता को पंक्ति ९८ की तीक्ष्णता से अलग करता है। "
           "‘प्राप्तकालम्’ = उचित समय पर, या ‘समय आने पर’; दोनों पठन सम्भव। ‘आदि’ के द्रव्य नहीं गिनाए। "
           "संधि जाँची: क्षीराज्याद्यैस्तु = क्षीर + आज्य + आद्यैः + तु; मार्दवं = मार्दवम् (म् → अनुस्वार)।"),
}

AIDS = {
    "38": {
        "diagram": {"groups": [{"label": "पंक्ति १", "items": ["बृहती", "क्षीरकाकोली", "पृश्निपर्णी", "शतावरी"]},
                               {"label": "पंक्ति २", "items": ["काश्मर्य", "बदरी", "मूर्वा", "तथा: उशीर", "प्रियङ्गु"]}]},
        "chunks": "बृहती | क्षीरकाकोली | पृश्निपर्णी | शतावरी ‖ काश्मर्य | बदरी | मूर्व्वास् | तथा | उशीर | प्रियंगवः।",
        "anchors": "बृहती = बड़ी कटेरी · पृश्निपर्णी = पिठवन · शतावरी = सतावर · काश्मर्य = गम्भारी · बदरी = बेर · मूर्वा = प्रायः मरोड़फली · उशीर = खस।",
        "sandhi": "आः + त → आस्त: मूर्वाः + तथा → मूर्वास्तथा; आ + उ → ओ: तथा + उशीर → तथोशीर।",
    },
    "39": {
        "chain": {"steps": ["जीवादान में", "उबाले हुए दूध में", "घी और अञ्जन से युक्त", "दो बस्तियाँ, वैद्य द्वारा", "ठंडी, मधु-शर्करा सहित"]},
        "chunks": "जीवादाने | शृते क्षीरे | द्वौ | घृतांजनसंयुतौ ‖ बस्ती | प्रदेयौ | भिषजा | शीतौ | समधुशर्करौ।",
        "anchors": "जीवादान = शब्दार्थ ‘जीव का ले लिया जाना’ · शृत = उबाला हुआ · अञ्जन = एक अञ्जन-द्रव्य · शर्करा = शक्कर · भिषज् = वैद्य।",
        "frame": "कब: जीवादान में · किसमें: उबले दूध में · किससे युक्त: घी, अञ्जन · कितनी: दो · कैसी: ठंडी, मधु-शर्करा सहित · कौन दे: वैद्य।",
    },
    "40": {
        "contrast": "पंक्ति १: दूध (बकरी, भैंस; गाय का पाठ खुला) जीवनीय सहित · पंक्ति २: रक्त (खरगोश, हिरण, बिल्ली, भैंस; एक नाम अनुमानित, अन्त अस्पष्ट)।",
        "chunks": "गोऽप्यजामहिषीक्षीरैः (आरम्भ संदिग्ध) | जीवनीययुतैरपि ‖ शश | एण | दक्ष (अनुमानित ऋक्ष) | मार्जार | महिषी | अन्यज (अस्पष्ट) | शोणितैः।",
        "anchors": "अजा = बकरी · महिषी = भैंस · जीवनीय = जीवन बढ़ाने वाला गण · शश = खरगोश · एण = हिरण · मार्जार = बिल्ली · शोणित = रक्त।",
    },
    "41": {
        "chunks": "सद्यस्कैः | मृदितैः | बस्तिः | जीवादाने | प्रशस्यते ‖ अथ | इमान् | सुकुमाराणां | निरूहान् | एहनान् (अनुमानित स्नेहनान्) | मृदून्।",
        "sandhi": "ऐः + घोष → ऐर्: सद्यस्कैः + मृदितैः → सद्यस्कैर्मृदितैः; इः + घोष → इर्: बस्तिः + जीवादाने → बस्तिर्जीवादाने; अ + इ → ए: अथ + इमान् → अथेमान्।",
        "anchors": "सद्यस्क = ताज़ा (उसी दिन का) · मृदित = मसला हुआ · प्रशस्यते = प्रशस्त माना जाता है · सुकुमार = कोमल · मृदु = हल्का।",
    },
    "42": {
        "chunks": "कर्मणा | विप्लुतानां च | वक्ष्यामि | प्रसृतैः | पृथक् ‖ क्षीराद्धौ (अनुमानित द्वौ) | प्रसृतौ | कार्यौ | मधुनैलघृतात् (अनुमानित) | त्रयः।",
        "frame": "किनके लिए: सुकुमार और कर्म से पीड़ित · क्या: (मृदु निरूह) कहूँगा · किस माप से: प्रसृत, अलग-अलग · आरम्भ: दूध से प्रसृत।",
        "anchors": "विप्लुत = पीड़ित, हानि पाया · वक्ष्यामि = कहूँगा · प्रसृत = हथेली-भर (लगभग दो पल) · पृथक् = अलग-अलग · कार्य = बनाने योग्य।",
    },
    "43": {
        "diagram": {"groups": [{"label": "पंक्ति १", "items": ["खज से मथी बस्ति", "वातघ्न", "बल-वर्णकारी"]},
                               {"label": "पंक्ति २: एक-एक प्रसृत", "items": ["तैल", "प्रसन्ना", "क्षौद्र", "सर्पिस्"]}]},
        "chunks": "खजेन | मथितो | बस्तिर् | वातघ्नो | बलवर्णकृत् ‖ एकैकः | प्रसृतस् | तैल | प्रसन्ना | क्षौद्र | सर्पिषां।",
        "sandhi": "अः + घोष → ओ: मथितः + बस्तिः → मथितो बस्तिः; इः + घोष → इर्: बस्तिः + वातघ्नः → बस्तिर्वातघ्नः; अ + ए → ऐ: एक + एकः → एकैकः।",
        "anchors": "खज = मथानी · वातघ्न = वात नाशक · वर्ण = रंग-रूप · प्रसन्ना = प्रायः मदिरा का निथरा भाग · क्षौद्र = मधु · सर्पिस् = घी।",
    },
    "44": {
        "contrast": "पंक्ति १: बेल-आदि जड़ों का काढ़ा और कुलथी → वातजित् (पिछला नुस्खा पूरा) · पंक्ति २: परवल, नीम, भूतीक, रास्ना और पाँचवाँ (अनुमानित) → इनका जल (नया नुस्खा)।",
        "chunks": "बिल्वादिमूलकाथाद्धौ (छपाई संदिग्ध) | कौलत्थाद्धौ | स वातजित् ‖ पटोल | निंब | भूतीक | रास्ना | समच्छद (अनुमानित सप्तच्छद) | अंभसः।",
        "anchors": "बिल्व = बेल · कौलत्थ = कुलथी · वातजित् = वात को जीतने वाला · पटोल = परवल · निम्ब = नीम · अम्भस् = जल।",
        "sandhi": "सः + व्यञ्जन → स: सः + वातजित् → स वातजित्; अ + आ → आ: बिल्व + आदि → बिल्वादि।",
    },
    "45": {
        "diagram": {"groups": [{"label": "बस्ति में", "items": ["जल: एक-एक प्रसृत", "घी से एक", "सरसों का कल्क", "पञ्चतिक्त"]},
                               {"label": "नाश करती है", "items": ["अभिष्यन्द", "कृमि", "कुष्ठ", "प्रमेह"]}]},
        "chunks": "प्रसृतः | पृथग् | आज्याच्च | बस्तिः | सर्षपकल्कवान् ‖ सपंचतिक्तो | ऽभिष्यंद | कृमि | कुष्ठ | प्रमेह | हा।",
        "anchors": "आज्य = घी · सर्षप = सरसों · कल्क = लुगदी · पञ्चतिक्त = पाँच तिक्त · कृमि = कीड़े · कुष्ठ = त्वचा रोग (कोढ़) · प्रमेह = मूत्र-विकार।",
        "letters": "चार रोगों के पहले अक्षर: अ-कृ-कु-प्र (अभिष्यन्द, कृमि, कुष्ठ, प्रमेह); केवल सुनने की सहायता।",
    },
    "46": {
        "chain": {"steps": ["विडङ्ग, त्रिफला, शिग्रु-फल, मुस्ता, पाँचवाँ (अनुमानित)", "इनके काढ़े: पाँच प्रसृत", "तेल से: एक प्रसृत", "सबको मथकर", "निरूह (पंक्ति ०५.०४.९१)"]},
        "chunks": "विडंग | त्रिफला | शिग्रुफल | मुस्ता | आखुकर्णिजाः (अनुमानित आखुकर्णिकाः) ‖ कषायाः | प्रसृताः पंच | तैलादेको | विमथ्य तान्।",
        "anchors": "विडङ्ग = वायविडंग · त्रिफला = हरड़, बहेड़ा, आँवला · शिग्रु = सहजन · मुस्ता = नागरमोथा · कषाय = काढ़ा · विमथ्य = मथकर।",
        "sandhi": "त् + स्वर → द्: तैलात् + एकः → तैलादेकः; अः + घोष → ओ: एकः + विमथ्य → एको विमथ्य।",
    },
    "47": {
        "chunks": "निरूहः | कृमिहा | वेल्ल | पिप्पली | कल्क | योजितः ‖ पयस्या | इक्षु | स्थिरा | रास्ना | विदारी | क्षौद्र | सर्पिषः (छपाई संदिग्ध)।",
        "anchors": "कृमिहा = कीड़ों का नाशक · वेल्ल = विवादित (कभी वायविडंग) · पिप्पली = पीपर · इक्षु = गन्ना · विदारी = विदारीकन्द · क्षौद्र = मधु।",
        "sandhi": "आ + इ → ए: पयस्या + इक्षु → पयस्येक्षु; ई + क्ष: विदारी + क्षौद्र में कोई बदलाव नहीं।",
        "frame": "पंक्ति १: क्या: निरूह · कर्म: कृमि-नाश · किससे युक्त: वेल्ल-पिप्पली का कल्क · पंक्ति २: नई सूची, पंक्ति ०५.०४.९३ में पूरी।",
    },
    "48": {
        "chunks": "एकैकः | प्रसृतो | बस्तिः | कृष्णाकल्कौ (अनुमानित कल्कात्) | वृषत्वकृत् ‖ चत्वारस् | तैल | गोमूत्र | दधिमंड | अम्ल | कांजिकात्।",
        "anchors": "एकैकः = एक-एक · वृषत्व = पुंसत्व-शक्ति · कृष्णा = पीपर · गोमूत्र = गाय का मूत्र · दधिमण्ड = दही का पानी · काञ्जिक = खट्टा किण्वित पेय।",
        "sandhi": "अः + त → अस्त: चत्वारः + तैल → चत्वारस्तैल; अः + घोष → ओ: प्रसृतः + बस्तिः → प्रसृतो बस्तिः।",
    },
    "49": {
        "seesaw": "मृदु ↔ तीक्ष्ण: मृदु बस्तियों से जो जड़ हो गया, उसके लिए दूसरी, तीक्ष्ण बस्ति।",
        "diagram": {"groups": [{"label": "कवोष्ण बस्ति श्रेष्ठ", "items": ["आनाह में", "मूत्रकृच्छ्र में"]},
                               {"label": "तीक्ष्ण बस्ति", "items": ["मृदु बस्तियों से जड़ हुए में"]}]},
        "chunks": "बस्तिः | कवोष्णः | सानाहे | मूत्रकृच्छ्रे | परो मतः ‖ मृदुबस्तिजडीभूते | तीक्ष्णो | ऽन्यो | बस्तिरिष्यते।",
        "anchors": "कवोष्ण = थोड़ा गुनगुना · आनाह = पेट फूलना, मल-वायु रुकना · मूत्रकृच्छ्र = कष्ट से मूत्र · परः = श्रेष्ठ · जडीभूत = सुस्त हुआ · इष्यते = चाहा जाता है।",
    },
    "50": {
        "contrast": "तीक्ष्णों से खिंचा (क्षीण) हो: स्निग्ध, मधुर, शीतल, मृदु बस्ति · तीक्ष्णता चाहिए: मूत्र, बिल्व, अग्नि, लवण, क्षार, सर्षप।",
        "seesaw": "तीक्ष्ण ↔ मृदु: तीक्ष्णों से खिंचे हुए के लिए मृदु (स्निग्ध, मधुर, शीतल) बस्ति।",
        "chunks": "तीक्ष्णैर् | विकर्षिते | स्निग्धो | मधुरः | शिशिरो | मृदुः ‖ तीक्ष्णत्वं | मूत्र | बिल्व | अग्नि | लवण | क्षार | सर्षपैः।",
        "anchors": "विकर्षित = खींचा गया, क्षीण · स्निग्ध = चिकना · शिशिर = ठंडा · तीक्ष्णत्व = तीक्ष्णता · बिल्व = बेल · अग्नि = आग या चित्रक (विवादित) · सर्षप = सरसों।",
    },
    "51": {
        "contrast": "पंक्ति ०५.०४.९८: तीक्ष्णता मूत्र, बिल्व, लवण, क्षार आदि से · यहाँ (‘तु’): मार्दव दूध, घी आदि से, उचित समय पर।",
        "chunks": "प्राप्तकालं | विधातव्यं | क्षीराज्याद्यैस्तु | मार्दवं।",
        "sandhi": "ऐः + त → ऐस्त: आद्यैः + तु → आद्यैस्तु; अ + आ → आ: क्षीर + आज्य → क्षीराज्य, आज्य + आद्यैः → आज्याद्यैः।",
    },
}

IMAGE_SPECS = {
    ("38", "diagram"): {
        "file": "ka4-brihati-38.svg",
        "alt": ("Two columns for verse 38: line 1 brihati, kshirakakoli, prishniparni, shatavari; "
                "line 2 kashmarya, badari, murva, then ushira and priyangu"),
        "type": "split",
        "title": "श्लोक ३८: द्रव्य-सूची",
        "cols": [["पंक्ति १", ["बृहती", "क्षीरकाकोली", "पृश्निपर्णी", "शतावरी"]],
                 ["पंक्ति २", ["काश्मर्य", "बदरी", "मूर्वा", "तथा: उशीर", "प्रियङ्गु"]]],
    },
    ("39", "chain"): {
        "file": "ka4-jivadana-39.svg",
        "alt": ("Chain of five steps for verse 39: in jivadana; in boiled milk; joined with ghee and anjana; "
                "two bastis given by the physician; cool, with honey and sugar"),
        "type": "chain",
        "title": "श्लोक ३९: जीवादान में",
        "steps": ["जीवादान में", "उबाले हुए दूध में", "घी और अञ्जन से युक्त", "दो बस्तियाँ, वैद्य द्वारा", "ठंडी, मधु-शर्करा सहित"],
    },
    ("43", "diagram"): {
        "file": "ka4-khaja-43.svg",
        "alt": ("Two columns for verse 43: line 1 the basti churned with a khaja, Vata-destroying, making strength and colour; "
                "line 2 one prasrita each of oil, prasanna, honey and ghee"),
        "type": "split",
        "title": "श्लोक ४३: मथी बस्ति, फिर नया नुस्खा",
        "cols": [["पंक्ति १", ["खज से मथी बस्ति", "वातघ्न", "बल-वर्णकारी"]],
                 ["पंक्ति २: एक-एक प्रसृत", ["तैल", "प्रसन्ना", "क्षौद्र", "सर्पिस्"]]],
    },
    ("45", "diagram"): {
        "file": "ka4-panchatikta-45.svg",
        "alt": ("Flowchart of verse 45: the basti with a prasrita of each water, one from ghee, mustard paste and the five bitters "
                "destroys abhishyanda, worms, kushtha and prameha"),
        "type": "mermaid",
        "code": ('flowchart TD\n'
                 '  A["जल: एक-एक प्रसृत<br/>घी से एक"] --> C["बस्ति"]\n'
                 '  B["सरसों का कल्क<br/>पञ्चतिक्त"] --> C\n'
                 '  C --> D["अभिष्यन्द"]\n'
                 '  C --> E["कृमि"]\n'
                 '  C --> F["कुष्ठ"]\n'
                 '  C --> G["प्रमेह"]\n'),
    },
    ("46", "chain"): {
        "file": "ka4-vimathya-46.svg",
        "alt": ("Chain of five steps for verse 46: vidanga, triphala, shigru fruit, musta and a conjectural fifth drug; "
                "their decoctions, five prasritas; one prasrita from oil; churn them all; the niruha of line 05.04.91"),
        "type": "chain",
        "title": "श्लोक ४६: मथकर निरूह",
        "steps": ["विडङ्ग, त्रिफला, शिग्रु-फल, मुस्ता, पाँचवाँ (अनुमानित)", "इनके काढ़े: पाँच प्रसृत", "तेल से: एक प्रसृत", "सबको मथकर", "निरूह (पंक्ति ९१)"],
    },
    ("49", "diagram"): {
        "file": "ka4-kavoshna-49.svg",
        "alt": ("Table for verse 49 with three rows: in anaha a slightly warm basti is best; in mutrakricchra a slightly warm basti is best; "
                "in one dulled by mild bastis a sharp basti is desired"),
        "type": "table",
        "title": "श्लोक ४९: स्थिति और बस्ति",
        "heads": ["स्थिति", "बस्ति"],
        "rows": [["आनाह (पेट फूलना)", "कवोष्ण, श्रेष्ठ"], ["मूत्रकृच्छ्र", "कवोष्ण, श्रेष्ठ"], ["मृदु बस्तियों से जड़", "दूसरी, तीक्ष्ण"]],
    },
    ("50", "contrast"): {
        "file": "ka4-tikshna-50.svg",
        "alt": ("Two columns for verse 50: for one depleted by sharp bastis an oily, sweet, cool, mild basti; "
                "sharpness comes from urine, bilva, agni, salt, kshara and mustard"),
        "type": "split",
        "title": "श्लोक ५०: तीक्ष्ण से क्षीण, और तीक्ष्णता",
        "cols": [["तीक्ष्णों से क्षीण हो तो", ["स्निग्ध", "मधुर", "शीतल", "मृदु"]],
                 ["तीक्ष्णता किससे", ["मूत्र", "बिल्व", "अग्नि", "लवण", "क्षार", "सर्षप"]]],
    },
}
