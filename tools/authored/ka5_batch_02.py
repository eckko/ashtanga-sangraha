from helpers import mcq, match, order, fill, multi, accepts

# Kalpasthana chapter 5 (Siddhabastikalpa), units 12-29.
# 12-18: the mustadi yapana (one long sentence, lines 05.05.22-35);
# 19-29: milk enemas and the aphrodisiac (vrsya) enemas.

AUTHORED = {}

# ---------------------------------------------------------------- unit 12
AUTHORED["12"] = {
    "title": "शुक्रानिलविबन्धेषु पूजितः",
    "question": "In which conditions is the enema of verse 12 esteemed, and which drugs begin the new list?",
    "rule": ("Line 1 ends the sentence of verse 11: the enema is esteemed in obstructions of "
             "semen and of wind and in āṭopa (rumbling distension) of the bladder region. Line 2 "
             "opens a drug list: musta, pāṭhā, amṛtā, eraṇḍa, balā, rāsnā, punarnavā."),
    "limits": ("Line 2 has no verb; its drugs are cooked in 05.05.26 (verse 14). basti in "
               "bastyāṭopa is the bladder region, not the enema; āṭopa as rumbling distension "
               "is probable. balā as Sida cordifolia is probable. The printed space inside "
               "amṛta-eraṇḍa is a print break."),
    "explain_hi": ("पहली पंक्ति श्लोक ११ के वाक्य को पूरा करती है: यह बस्ति शुक्र और अनिल यानी वायु की रुकावटों में तथा बस्ति-प्रदेश के आटोप यानी गुड़गुड़ाहट वाले फुलाव में पूजित यानी प्रशंसित है। "
                   "यहाँ ‘बस्ति’ मूत्राशय का प्रदेश है, एनीमा नहीं। "
                   "दूसरी पंक्ति एक नई द्रव्य-सूची शुरू करती है: मुस्ता यानी नागरमोथा, पाठा, अमृता यानी गिलोय, एरण्ड यानी अरंडी, बला यानी सम्भवतः बरियार, रास्ना और पुनर्नवा यानी गदहपूर्णा। "
                   "इन्हें आगे श्लोक १४ में पकाया जाता है।"),
    "hook": "शुक्र-वायु की रुकावट, बस्ति का आटोप; फिर मुस्ता से पुनर्नवा तक सात द्रव्य।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "In which conditions does line 1 of verse 12 say the enema is esteemed?",
            ("Blocked semen and wind; bladder āṭopa",
             "शुक्रानिलविबन्धेषु बस्त्याटोपेषु = in obstructions of semen and wind, in āṭopa of the bladder region."),
            [("Fever, cough and swelling of the feet",
              "None of these is named in verse 12."),
             ("Worms, gulma and intestinal hernia",
              "These are in verse 4, not here."),
             ("Pain of the head, ear and the nape",
              "Head and ear pains come in verse 17.")],
            "Two locatives name the conditions: obstructions (of semen and wind) and āṭopa of the bladder region.",
            "शुक्र-अनिल-विबन्धेषु · बस्ति-आटोपेषु · पूजितः."),
        match(1, "Match each drug of verse 12 to its identification on the card.",
              [["मुस्त", "nut-grass (Cyperus rotundus)"], ["अमृता", "guḍūcī, giloy (Tinospora cordifolia)"],
               ["एरण्ड", "castor"], ["पुनर्नवा", "Boerhavia diffusa"]],
              "Four drugs of line 2 with the identifications the data marks standard.",
              "मुस्त = nut-grass; अमृता = guḍūcī; एरण्ड = castor; पुनर्नवा = Boerhavia diffusa."),
        order(2, "Put these drugs of line 2 in the order of verse 12.",
              ["पाठा", "अमृता", "एरण्ड", "बला", "रास्ना", "पुनर्नवा"],
              "After musta the compound runs pāṭhā, amṛtā, eraṇḍa, balā, rāsnā and ends with punarnavā.",
              "मुस्त · पाठा · अमृता · एरण्ड · बला · रास्ना · पुनर्नवा.",
              role="extend",
              teaches="Line 2 of verse 12 lists musta, pāṭhā, amṛtā, eraṇḍa, balā, rāsnā, punarnavā, in that order."),
        mcq("discriminate", 3, "Which split of शुक्रानिल is right?",
            ("शुक्र + अनिल", "अ + अ → आ: शुक्र (semen) + अनिल (wind)."),
            [("शुक्रः + अनिल", "A visarga after अ before अ would give शुक्रोऽनिल."),
             ("शुक्रान् + इल", "इल is not a word here; the second member is अनिल (wind)."),
             ("शुक्रा + निल", "निल is not a word; the stem is शुक्र, not शुक्रा.")],
            "Inside the compound, शुक्र + अनिल join with अ + अ → आ.",
            "अ + अ → आ: शुक्र + अनिल = शुक्रानिल."),
        mcq("apply", 4, "What does the card say बस्ति means inside बस्त्याटोपेषु?",
            ("The bladder region",
             "The data reads basti here as the bladder region: āṭopa of the bladder region."),
            [("The enema being given",
              "Elsewhere basti is the enema, but here it names the place of the āṭopa."),
             ("The enema bag (device)",
              "The bag sense belongs to other chapters; here it is a body region."),
             ("The yāpana enema of 05.05.35",
              "The yāpana is the subject of the sentence, not the place of the āṭopa.")],
            "बस्ति-आटोप = rumbling distension of the bladder region; the enema is the subject (पूजितः).",
            "बस्त्याटोप = basti (bladder region) + āṭopa (rumbling distension)."),
        mcq("transfer", 5,
            "Like विबन्धेषु (in obstructions), which invented form means in fevers (ज्वर)?",
            ("ज्वरेषु", "-एषु is the locative plural of an -अ stem: 'in'."),
            [("ज्वरैः", "-ऐः is the instrumental plural: 'with fevers'."),
             ("ज्वराणाम्", "-आणाम् is the genitive plural: 'of fevers'."),
             ("ज्वरान्", "-आन् is the accusative plural: fevers as object.")],
            "Same ending as विबन्धेषु and बस्त्याटोपेषु: -एषु = in.",
            "-एषु = locative plural of an -अ stem.",
            teaches="The ending -एषु marks the locative plural of an -अ stem, 'in X': विबन्धेषु, आटोपेषु, ज्वरेषु."),
    ],
}

# ---------------------------------------------------------------- unit 13
AUTHORED["13"] = {
    "title": "मञ्जिष्ठारग्वधोशीर",
    "question": "Which further drugs and which root group does verse 13 add to the list?",
    "rule": ("The list goes on: mañjiṣṭhā (Indian madder), āragvadha (Indian laburnum), uśīra "
             "(vetiver), trāyamāṇā, and at the end of line 1 a conjectural akṣa and rohiṇī; then "
             "the lesser pañcamūla, of a pala, and a set of eight madana."),
    "limits": ("Low confidence. akṣa + rohiṇī at the end of line 1 is conjectural; no question "
               "uses them. trāyamāṇā and rohiṇī are disputed, madana probable. Whether pālikam "
               "covers the pañcamūla alone or all is open. The five roots are not listed."),
    "explain_hi": ("सूची आगे चलती है: मञ्जिष्ठा यानी मंजीठ, आरग्वध यानी अमलतास, उशीर यानी खस और त्रायमाणा, जिसकी पहचान विवादित है। "
                   "पंक्ति के अन्त को अनुमानित पाठ पर अक्ष यानी सम्भवतः बहेड़ा और रोहिणी पढ़ा गया है। "
                   "दूसरी पंक्ति में कनीयः पञ्चमूल यानी छोटा पंचमूल आता है, ‘पालिक’ यानी पल के मान का, और मदनाष्टक यानी आठ मदन, सम्भवतः मैनफल। "
                   "पंचमूल की पाँच जड़ें यहाँ नहीं गिनाई गईं।"),
    "hook": "मंजीठ, अमलतास, खस, त्रायमाणा; छोटा पंचमूल और आठ मदन।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Which pañcamūla (group of five roots) does verse 13 name?",
            ("The lesser one (kanīyaḥ)", "कनीयः पञ्चमूलम् = the lesser pañcamūla."),
            [("The greater one (bṛhat)", "The verse says कनीयः, smaller, not the greater group."),
             ("Two of them (ten roots)", "Two pañcamūlas are in verse 10, not here."),
             ("One without gokṣura", "The pañcamūla without gokṣura comes in verse 19.")],
            "कनीयः (smaller, lesser) qualifies पञ्चमूलम्.",
            "कनीयः पञ्चमूलम् = the lesser group of five roots."),
        match(1, "Match each word of verse 13 to its meaning on the card.",
              [["मञ्जिष्ठा", "Indian madder"], ["आरग्वध", "Indian laburnum"],
               ["उशीर", "vetiver"], ["कनीयः", "smaller, lesser"]],
              "Three drugs of line 1 (standard identifications) and the word that names the root group.",
              "मञ्जिष्ठा = Indian madder; आरग्वध = Indian laburnum; उशीर = vetiver; कनीयः = lesser."),
        order(2, "Put these four drugs in the order of line 1 of verse 13.",
              ["मञ्जिष्ठा", "आरग्वध", "उशीर", "त्रायमाणा"],
              "The compound opens mañjiṣṭhā, āragvadha, uśīra, trāyamāṇā; the end of the line is conjectural.",
              "मञ्जिष्ठा · आरग्वध · उशीर · त्रायमाणा · (अनुमानित: अक्ष, रोहिणी).",
              role="extend",
              teaches="Line 1 of verse 13 runs mañjiṣṭhā, āragvadha, uśīra, trāyamāṇā before its doubtful end."),
        mcq("discriminate", 3, "What does मदनाष्टकम् mean on the card?",
            ("A set of eight madana",
             "मदन + अष्टक: अष्टक = a set of eight."),
            [("Madana with eight other drugs",
              "The compound counts madana itself: a group of eight of them."),
             ("An eighth part of one madana",
              "An eighth part would be अष्टमांश, not अष्टक."),
             ("Madana boiled down to an eighth",
              "No boiling is in the word; अष्टक counts eight items.")],
            "-अष्टक names a group of eight, here of madana (probably emetic nut).",
            "X-अष्टक = a set of eight X."),
        mcq("apply", 4, "Does verse 13 list the five roots of the lesser pañcamūla?",
            ("No; it names the group only",
             "The card says the text does not list the members."),
            [("Yes; it lists them after madana",
              "Nothing follows madana in this verse."),
             ("Yes; they are the drugs of line 1",
              "Line 1 holds mañjiṣṭhā and others, not the five roots."),
             ("Yes; it names bṛhatī and four more",
              "Bṛhatī heads a pañcamūla in verse 22, not here.")],
            "Only the group name stands in the text: कनीयः पञ्चमूलम्.",
            "A group name (पञ्चमूल) can stand without its members."),
        mcq("transfer", 5,
            "Like मदनाष्टकम् (a set of eight madana), what does an invented ओषधिपञ्चकम् mean (ओषधि = herb)?",
            ("A set of five herbs", "-पञ्चक names a group of five, as -अष्टक a group of eight."),
            [("The fifth herb of a list", "The fifth would be पञ्चम, not पञ्चक."),
             ("A herb five times as strong", "The suffix counts members; it does not intensify."),
             ("Five portions of one herb", "The word names a group of herbs, not portions.")],
            "Number + -क names a set: अष्टक (eight), पञ्चक (five).",
            "X-पञ्चक = a set of five X.",
            teaches="A number word with -क names a set of that many: मदनाष्टकम् (eight madana), ओषधिपञ्चकम् (five herbs)."),
    ],
}

# ---------------------------------------------------------------- unit 14
AUTHORED["14"] = {
    "title": "जलाढके पचेत्तच्च",
    "question": "How does verse 14 cook the drugs of verses 12-13, step by step?",
    "rule": ("Cook that (the drug list) in an āḍhaka of water down to a quarter, strain it; join "
             "it with two prasthas of milk and cook it again until the milk alone remains."),
    "limits": ("āḍhaka and prastha are measures of volume, kept as given. 'Until the milk remains' "
               "is the data's reading of kṣīraśeṣam (the water boiled away). 'That' is the drug "
               "list of 05.05.23-25; the additions follow in verse 15."),
    "explain_hi": ("यह श्लोक पकाने की विधि देता है। पहले उन द्रव्यों को जल के एक आढक में पकाए, जब तक चौथाई शेष रहे, और छान ले (परिस्रुत)। "
                   "फिर उसमें दो प्रस्थ दूध मिलाकर दोबारा पकाए, जब तक केवल दूध शेष रहे, यानी जल उड़ जाए। "
                   "आढक और प्रस्थ आयतन के मान हैं। "
                   "दोनों बार क्रिया ‘पचेत्’ है: पकाए।"),
    "hook": "आढक जल → चौथाई → छानो → दो प्रस्थ दूध → दूध बचे तक फिर पकाओ।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "In what is the drug list first cooked in verse 14?",
            ("In an āḍhaka of water", "जलाढके = in an āḍhaka of water."),
            [("In two prasthas of milk", "The two prasthas of milk are added in line 2."),
             ("In four prasthas of urine", "No urine is named in this verse."),
             ("In an āḍhaka of meat juice", "No meat juice is named in this verse.")],
            "Line 1 opens with जलाढके: water first, milk later.",
            "जल-आढके पचेत् = cook in an āḍhaka of water."),
        match(1, "Match each word of verse 14 to its meaning.",
              [["जलाढक", "an āḍhaka of water"], ["पादशेष", "with a quarter remaining"],
               ["परिस्रुत", "strained"], ["क्षीरशेष", "until the milk remains"]],
              "Four words carry the whole procedure.",
              "पाद = a quarter; शेष = remaining; परिस्रुत = strained."),
        order(2, "Put the steps of verse 14 in the order of the text.",
              ["Cook in an āḍhaka of water", "Reduce to a quarter", "Strain it",
               "Join two prasthas of milk", "Cook again till milk remains"],
              "Water cooking, reduction to a quarter, straining, then milk and a second cooking.",
              "जलाढक · पादशेष · परिस्रुत · क्षीरद्विप्रस्थ · क्षीरशेष.",
              role="extend",
              teaches="Verse 14: cook in water to a quarter, strain, add two prasthas of milk, cook again till milk remains."),
        mcq("discriminate", 3, "Which split of पचेत्तच्च is right?",
            ("पचेत् + तत् + च", "पचेत् (one should cook) + तत् (that) + च (and); त् before च becomes च्."),
            [("पचेत + तत् + च", "पचेत would join as पचेततच्च; the card reads पचेत् with final त्."),
             ("पचेत् + तः + च", "तः is not a word here, and -अः + च would give -अश्च."),
             ("पचे + त्तत् + च", "त्तत् is not a word.")],
            "Three words: पचेत् · तत् · च; तत् + च → तच्च.",
            "Final त् + च → च्च: तत् + च = तच्च."),
        mcq("apply", 4, "Until when is the milk mixture cooked the second time?",
            ("Until only the milk is left",
             "क्षीरशेषम् = until the milk remains, the water having boiled away."),
            [("Until a quarter of it is left",
              "The quarter belongs to the first cooking in water."),
             ("Until it thickens into a paste",
              "No paste is named in verse 14."),
             ("Until half of the milk is left",
              "No half is named; the text says the milk remains.")],
            "First cooking: पादशेष (a quarter); second cooking: क्षीरशेष (milk remains).",
            "क्षीरशेषं पुनः पचेत् = cook again until the milk remains."),
        mcq("transfer", 5,
            "Join an invented तत् + चूर्णम् (that powder) by the rule of तच्च. Which is right?",
            ("तच्चूर्णम्", "Final त् becomes च् before च: तत् + चूर्णम् → तच्चूर्णम्."),
            [("तत्चूर्णम्", "त् does not stay before च; it takes the place of च."),
             ("तद्चूर्णम्", "त् → द् happens before voiced sounds; च is unvoiced."),
             ("तज्चूर्णम्", "त् → ज् happens before ज, not before च.")],
            "Same rule as तत् + च = तच्च in verse 14.",
            "Final त् + च → च्च.",
            teaches="Final त् becomes च् before च: तत् + च → तच्च; तत् + चूर्णम् → तच्चूर्णम्."),
    ],
}

# ---------------------------------------------------------------- unit 15
AUTHORED["15"] = {
    "title": "सपादजाङ्गलरसः",
    "question": "What is added to the cooked milk in line 1 of verse 15, and which ground drugs follow?",
    "rule": ("The preparation takes jāṅgala-rasa (juice of dry-land animals), one and a quarter "
             "(the unit not stated), with ghee, honey and rock salt; then ground drugs: licorice, "
             "probably dill (miśi), śyāmā, kaliṅga, an unclear kara, and añjana."),
    "limits": ("Low confidence. What sapāda counts is not stated. jāṅgala is 'of dry-land "
               "animals'; the line does not say meat. kara in line 2 is unclear (karañja is only "
               "a guess); śyāmā and kaliṅga are disputed. No question rests on line 2's list."),
    "explain_hi": ("पहली पंक्ति कहती है कि इसमें सपाद यानी सवा भाग जाङ्गल-रस हो, यानी सूखे प्रदेश के प्राणियों का रस; मात्रा का मान नहीं बताया। "
                   "साथ में सर्पिः यानी घी, मधु और सैन्धव यानी सेंधा नमक (‘स-’ = सहित)। "
                   "दूसरी पंक्ति पिसे हुए द्रव्य गिनाती है: यष्टी यानी मुलेठी, मिशि यानी सम्भवतः सोया, श्यामा, कलिङ्ग, एक अस्पष्ट शब्द ‘कर’ और अञ्जन। "
                   "इस पंक्ति का पाठ अनिश्चित है।"),
    "hook": "सवा जाङ्गल-रस + घी, मधु, सेंधा नमक; फिर पिसे द्रव्य।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Which three substances come with the prefix स- (with) in line 1 of verse 15?",
            ("Ghee, honey and rock salt", "स-सर्पिः-मधु-सैन्धवः = with ghee, honey and rock salt."),
            [("Oil, honey and kṣāra too", "Oil and kṣāra are not in this line."),
             ("Ghee, milk and the sugar", "Milk and sugar are not in this compound."),
             ("Honey, oil and some fat", "Oil and fat are not named here.")],
            "The bahuvrīhi ससर्पिर्मधुसैन्धवः lists ghee, honey, rock salt.",
            "स- + सर्पिस् + मधु + सैन्धव = with ghee, honey, rock salt."),
        match(1, "Match each word of line 1 of verse 15 to its meaning.",
              [["सपाद", "one and a quarter"], ["जाङ्गल", "of dry-land animals"],
               ["रस", "juice"], ["सर्पिस्", "ghee"]],
              "These words make up the first half of line 1.",
              "स-पाद = with a quarter more; जाङ्गल = of dry land; सर्पिस् = ghee."),
        order(2, "Put these parts of line 1 in the order of verse 15.",
              ["सपादजाङ्गलरसः", "सर्पिः", "मधु", "सैन्धवः"],
              "First the juice, then the स- compound: ghee, honey, rock salt.",
              "सपादजाङ्गलरसः · स-सर्पिः-मधु-सैन्धवः.",
              role="extend",
              teaches="Line 1 of verse 15 gives the jāṅgala juice, then ghee, honey and rock salt."),
        mcq("discriminate", 3, "Which split of ससर्पिर्मधु is right?",
            ("स + सर्पिः + मधु", "-इः before a voiced sound (म) becomes -इर्: सर्पिः + मधु → सर्पिर्मधु."),
            [("स + सर्प + इर्मधु", "सर्प is 'snake' and इर्मधु is not a word."),
             ("सस + अर्पिः + मधु", "सस and अर्पिः are not the words; the stem is सर्पिस् (ghee)."),
             ("स + सर्पिर्म + धु", "धु is not a word; मधु (honey) is whole.")],
            "स- (with) + सर्पिः (ghee) + मधु (honey); the visarga turns to र्.",
            "-इः + voiced consonant → -इर्."),
        mcq("apply", 4, "Does verse 15 say what unit the sapāda (one and a quarter) counts?",
            ("No; the unit is not stated", "The card says what sapāda counts is not stated."),
            [("Yes: one and a quarter prastha", "No prastha is named in this verse."),
             ("Yes: one and a quarter pala", "No pala is named in this verse."),
             ("Yes: one and a quarter āḍhaka", "No āḍhaka is named in this verse.")],
            "सपाद means 'with a quarter more', but no measure follows it.",
            "सपाद = one and a quarter (of an unstated unit)."),
        mcq("transfer", 5,
            "Join the invented pair सर्पिः + दधि (ghee, curd) by the rule of ससर्पिर्मधु. Which is right?",
            ("सर्पिर्दधि", "-इः before a voiced consonant (द) becomes -इर्."),
            [("सर्पिस्दधि", "स् stands before त/थ, which are unvoiced; द is voiced."),
             ("सर्पिदधि", "The visarga is not dropped after इ; it turns to र्."),
             ("सर्पिष्दधि", "ष् stands before ट/ठ, not before द.")],
            "Same rule as सर्पिः + मधु = सर्पिर्मधु.",
            "-इः + voiced consonant → -इर्.",
            teaches="A visarga after इ becomes र् before a voiced consonant: सर्पिः + मधु → सर्पिर्मधु; सर्पिः + दधि → सर्पिर्दधि."),
    ],
}

# ---------------------------------------------------------------- unit 16
AUTHORED["16"] = {
    "title": "बस्तिः सुखोष्णो",
    "question": "What does the warm enema of verse 16 increase, and what does its second line begin?",
    "rule": ("The enema, comfortably warm, increases flesh, the digestive fire, strength and "
             "semen. Line 2 begins the long list of disorders it destroys (हन्यात्, 05.05.34): "
             "vātāsṛk, meha, fat, arśas, gulma, retention of stool and urine."),
    "limits": ("No verb in the verse: 'is' is supplied. meha is a conjecture for printed neha "
               "(flagged), so no question uses it. vātāsṛk as gout and medas as obesity are "
               "probable. The list runs on through verses 17-18."),
    "explain_hi": ("यह बस्ति सुखोष्ण यानी सुहाती गर्म है, और मांस, अग्नि यानी पाचक अग्नि, बल और शुक्र को बढ़ाने वाली (विवर्धन) है। "
                   "दूसरी पंक्ति उन रोगों की लम्बी सूची शुरू करती है जिन्हें यह नष्ट करती है; क्रिया ‘हन्यात्’ श्लोक १८ में आती है। "
                   "सूची में वातास्र यानी वातरक्त, मेह (छपा ‘नेह’), मेदस् यानी चर्बी, अर्श यानी बवासीर, गुल्म और मल-मूत्र का रुकना हैं।"),
    "hook": "सुहाती गर्म बस्ति: मांस, अग्नि, बल, शुक्र बढ़ाए।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "Which four things does the warm enema of verse 16 increase?",
            ("Flesh, digestive fire, strength, semen", "मांस-अग्नि-बल-शुक्र-विवर्धनः."),
            [("Fat, blood, marrow and the semen too", "Fat, blood and marrow are not in this compound."),
             ("Strength, voice, sleep and the skin", "Voice, sleep and skin are not named."),
             ("Flesh, fat, bone and also marrow", "Only flesh of these is named.")],
            "The compound ending in -विवर्धनः lists four: flesh, agni, strength, semen.",
            "मांस · अग्नि · बल · शुक्र + विवर्धनः = increasing."),
        match(1, "Match each word of line 1 of verse 16 to its meaning.",
              [["सुखोष्ण", "comfortably warm"], ["मांस", "flesh"],
               ["अग्नि", "digestive fire"], ["विवर्धन", "increasing"]],
              "These words describe the enema in line 1.",
              "सुख-उष्ण = comfortably warm; विवर्धन = increasing."),
        order(2, "Put the four things increased in the order of verse 16.",
              ["मांस", "अग्नि", "बल", "शुक्र"],
              "The compound runs flesh, digestive fire, strength, semen, then -विवर्धनः.",
              "मांस · अग्नि · बल · शुक्र.",
              role="extend",
              teaches="The warm enema increases flesh, agni, strength and semen, in that order."),
        mcq("discriminate", 3, "Which split of सुखोष्णो is right?",
            ("सुख + उष्णः", "अ + उ → ओ; -अः before the voiced म becomes -ओ."),
            [("सुखः + उष्णः", "A visarga after अ before उ would be dropped: सुख उष्णः."),
             ("सु + खोष्णः", "खोष्ण is not a word."),
             ("सुखम् + उष्णः", "म् before a vowel stays: सुखमुष्णः.")],
            "सुख (comfortably) + उष्ण (warm), joined with अ + उ → ओ.",
            "अ + उ → ओ: सुख + उष्ण = सुखोष्ण."),
        mcq("apply", 4, "Which verb governs the disorders that start in line 2 of verse 16?",
            ("हन्यात् in verse 18", "The card: line 2 begins the list of what it destroys (हन्यात्, 05.05.34)."),
            [("पचेत् in verse 14", "पचेत् governs the cooking, not the disorders."),
             ("पूजितः in verse 12", "पूजितः closes the earlier sentence of verse 11-12."),
             ("विवर्धनः in line 1", "विवर्धनः governs flesh, agni, strength and semen.")],
            "Line 2 starts a list in the accusative that runs to हन्यात् in verse 18.",
            "Disorders of 05.05.31-34 = objects of हन्यात् (it may destroy)."),
        mcq("transfer", 5,
            "Join an invented मधुर + उदकम् (sweet water) by the rule of सुखोष्ण. Which is right?",
            ("मधुरोदकम्", "अ + उ → ओ, as in सुख + उष्ण = सुखोष्ण."),
            [("मधुरूदकम्", "अ + उ does not give ऊ."),
             ("मधुरउदकम्", "The vowels join; they do not stand side by side."),
             ("मधुरौदकम्", "औ comes from अ + ओ/औ, not from अ + उ.")],
            "अ + उ joins as ओ (guṇa).",
            "अ + उ → ओ.",
            teaches="अ/आ + उ/ऊ → ओ: सुख + उष्ण → सुखोष्ण; मधुर + उदकम् → मधुरोदकम्."),
    ],
}

# ---------------------------------------------------------------- unit 17
AUTHORED["17"] = {
    "title": "विषमज्वर आध्मानप्रवाहिकाः",
    "question": "Which further disorders and pains does verse 17 add to the list of what the enema destroys?",
    "rule": ("More objects of हन्यात्: irregular fever, vīsarpa (spreading inflammation), an unclear "
             "word, bloating and pravāhikā (dysentery with straining); then pains (रुजः) of groin, "
             "thigh, waist, flank, nape, ear and head."),
    "limits": ("Low confidence. Printed सर्ष is read vīsarpa, and ध्म is unclear (dhmāna only a "
               "weak guess); printed mandyā is read manyā (nape): no question uses these. "
               "pravāhikā, viṣamajvara and vīsarpa are probable identifications. The verb is in "
               "verse 18."),
    "explain_hi": ("यह श्लोक नष्ट होने वाले रोगों की सूची आगे बढ़ाता है: विषम ज्वर यानी अनियमित बुखार, विसर्प, एक अस्पष्ट शब्द, आध्मान यानी अफारा और प्रवाहिका यानी मरोड़ के साथ दस्त। "
                   "दूसरी पंक्ति एक समास है जो ‘रुजः’ यानी पीड़ाओं पर समाप्त होता है: वंक्षण यानी जाँघ का जोड़, ऊरु यानी जाँघ, कटि, कुक्षि, मन्या, कान और सिर की पीड़ा। "
                   "छपे ‘सर्ष’ और ‘मन्द्या’ अनुमान से पढ़े गए हैं।"),
    "hook": "ज्वर, विसर्प, अफारा, प्रवाहिका; जाँघ-जोड़ से सिर तक की पीड़ा।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "What does रुजः at the end of line 2 of verse 17 mean?",
            ("Pains (of each part named)", "रुजः = pains; it governs every body part before it."),
            [("Swellings of each part named", "Swelling (शोफ) is in verse 18, not रुजः."),
             ("Wounds of each part named", "No wound is named; रुजः means pains."),
             ("Fevers of each part named", "Fever is in line 1; रुजः means pains.")],
            "The compound ends in रुजः: pains of groin, thigh, waist and the rest.",
            "X-Y-Z-रुजः = the pains of X, Y, Z."),
        match(1, "Match each word of verse 17 to its meaning on the card.",
              [["आध्मान", "bloating"], ["प्रवाहिका", "dysentery with straining"],
               ["विषमज्वर", "irregular fever"], ["श्रोत्र", "ear"]],
              "Clear words of the two lines.",
              "आध्मान = bloating; प्रवाहिका = dysentery with straining; विषमज्वर = irregular fever; श्रोत्र = ear."),
        order(2, "Put these body parts in the order of line 2 of verse 17.",
              ["वङ्क्षण", "ऊरु", "कटी", "कुक्षि"],
              "The pain compound opens groin, thigh, waist, flank.",
              "वङ्क्षण · ऊरु · कटी · कुक्षि · … · श्रोत्र · शिरः + रुजः.",
              role="extend",
              teaches="The pain list of verse 17 opens with groin, thigh, waist and flank."),
        mcq("discriminate", 3, "Which split of वङ्क्षणोरु is right?",
            ("वङ्क्षण + ऊरु", "अ + ऊ → ओ: वङ्क्षण (groin) + ऊरु (thigh)."),
            [("वङ्क्षणः + ऊरु", "A visarga after अ before ऊ would be dropped: वङ्क्षण ऊरु."),
             ("वङ्क्षणो + रु", "रु is not a word; the thigh is ऊरु."),
             ("वङ्क्ष + णोरु", "Neither part is a word.")],
            "Inside the compound, अ + ऊ joins as ओ.",
            "अ + ऊ → ओ: वङ्क्षण + ऊरु = वङ्क्षणोरु."),
        multi("apply", 4,
              "Which body parts does line 2 of verse 17 name for pain?",
              [("Groin", "वङ्क्षण = groin."),
               ("Knee", "The knee (जानु) is in verse 5, not here."),
               ("Waist", "कटी = waist, hip."),
               ("Chest", "No chest is named."),
               ("Head", "शिरः = head, in शिरोरुजः."),
               ("Eyes", "No eyes are named in verse 17.")],
              [0, 2, 4],
              "Groin, thigh, waist, flank, (nape), ear and head carry the pains.",
              "वङ्क्षण · ऊरु · कटी · कुक्षि · (मन्या) · श्रोत्र · शिरः."),
        mcq("transfer", 5,
            "शिरोरुजः joins शिरः + रुजः. Join an invented शिरः + वेदना (head pain) the same way. Which is right?",
            ("शिरोवेदना", "-अः before a voiced consonant (व) becomes -ओ."),
            [("शिरवेदना", "The visarga does not drop to bare -अ here."),
             ("शिरर्वेदना", "र् replaces a visarga after vowels other than अ/आ."),
             ("शिरस्वेदना", "स् stands before त/थ, not before व.")],
            "Same rule as शिरः + रुजः = शिरोरुजः.",
            "-अः + voiced consonant → -ओ.",
            teaches="-अः becomes -ओ before a voiced consonant: शिरः + रुजः → शिरोरुजः; शिरः + वेदना → शिरोवेदना."),
    ],
}

# ---------------------------------------------------------------- unit 18
AUTHORED["18"] = {
    "title": "राजा यापनानां रसायनम्",
    "question": "Which disorders does verse 18 add, and which titles does it give the enema?",
    "rule": ("हन्यात्, it may destroy, ends the list: asṛgdara (abnormal menstrual bleeding), "
             "insanity, swelling, cough and an unclear last word. The enema is good for the eyes, "
             "gives sons, is the king of the yāpanas and a rasāyana."),
    "limits": ("Low confidence. अश्मकुण्डलान् is not a known disease name and is not interpreted; "
               "no question uses it. asṛgdara is a probable identification. The subject is the "
               "enema of 05.05.30 (verse 16); line 2 has no verb."),
    "explain_hi": ("‘हन्यात्’ यानी नष्ट करे: यही क्रिया श्लोक १६ से चली रोग-सूची को पूरा करती है। "
                   "इस पंक्ति में असृग्दर यानी असामान्य मासिक रक्तस्राव, उन्माद, शोफ यानी सूजन, कास यानी खाँसी और एक अस्पष्ट शब्द ‘अश्मकुण्डल’ है। "
                   "दूसरी पंक्ति बस्ति के विशेषण देती है: चक्षुष्य यानी आँखों के लिए हितकर, पुत्रद यानी पुत्र देने वाली, यापनों का राजा और रसायन।"),
    "hook": "हन्यात्: रोग-सूची पूरी; आँखों का हित, पुत्रद, यापनों का राजा, रसायन।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "What title does verse 18 give this enema among the yāpanas?",
            ("The king of the yāpanas", "राजा यापनानाम् = the king of the yāpanas."),
            [("The best of the nirūhas", "Nirūhas are not named in this verse."),
             ("The lord of oil enemas", "Oil enemas are not named here."),
             ("The chief of purgatives", "No purgative is named here.")],
            "यापनानाम् (genitive plural) depends on राजा: king of the yāpanas.",
            "राजा यापनानाम् = king of the yāpanas."),
        match(1, "Match each word of line 2 of verse 18 to its meaning.",
              [["चक्षुष्य", "good for the eyes"], ["पुत्रद", "giver of sons"],
               ["राजा", "king"], ["रसायन", "rejuvenative"]],
              "The four titles of the enema.",
              "चक्षुष्य = good for the eyes; पुत्र-द = son-giving; रसायन = rejuvenative."),
        order(2, "Put the words of line 2 of verse 18 in the order of the verse.",
              ["चक्षुष्यः", "पुत्रदः", "राजा", "यापनानाम्", "रसायनम्"],
              "Line 2: good for the eyes, giver of sons, king of the yāpanas, rasāyana.",
              "चक्षुष्यः · पुत्रदो · राजा · यापनानां · रसायनम्.",
              role="extend",
              teaches="Verse 18 calls the enema चक्षुष्य, पुत्रद, king of the yāpanas and रसायन, in that order."),
        mcq("discriminate", 3, "What form is हन्यात्, as the card gives it?",
            ("3 sg optative: it may destroy", "√हन्, 3 sg optative: it would / may destroy."),
            [("3 sg present: it destroys", "The present would be हन्ति."),
             ("Past participle: destroyed", "The past participle would be हत."),
             ("Absolutive: having destroyed", "The absolutive would be हत्वा.")],
            "-यात् marks the optative of √हन्.",
            "हन्यात् = it may destroy (optative)."),
        multi("apply", 4,
              "Which disorders does line 1 of verse 18 name, apart from its unclear last word?",
              [("Abnormal menstrual bleeding", "असृग्दर (probable identification)."),
               ("Insanity", "उन्माद = insanity."),
               ("Worms", "Worms (कृमि) are in verse 4."),
               ("Cough", "कास = cough."),
               ("Eye disease", "The eyes are praised in line 2; no eye disease is named."),
               ("Hiccup", "No hiccup is named.")],
              [0, 1, 3],
              "Line 1: asṛgdara, unmāda, śopha, kāsa, then an unclear word.",
              "असृग्दर · उन्माद · शोफ · कास · (अस्पष्ट)."),
        mcq("transfer", 5,
            "Like पुत्रदः (giver of sons), what does an invented बलदः mean (बल = strength)?",
            ("Giving strength", "-द at the end of a compound means 'giving X'."),
            [("Born of strength", "That would be बलज, with -ज (born)."),
             ("Conquering strength", "That would be बलजित्, with -जित्."),
             ("Having strength", "That would be बलवान्, with -वत्.")],
            "Same build as पुत्रद: X + -द = giving X.",
            "X-द = giving X.",
            teaches="A compound ending in -द means 'giving X': पुत्रद (giving sons), बलद (giving strength)."),
    ],
}

# ---------------------------------------------------------------- unit 19
AUTHORED["19"] = {
    "title": "पृथक्पलांशं विपचेत्",
    "question": "How does verse 19 prepare its pañcamūla with milk?",
    "rule": ("One should cook the pañcamūla without gokṣura, separately in pala portions, in an "
             "āḍhaka of milk; four prasthas, joined with the ground drugs beginning with licorice "
             "(yaṣṭi)."),
    "limits": ("Which pañcamūla is meant is not stated, and 'without gokṣura' is an open point "
               "(possible corruption): no question rests on it. What the four prasthas measure is "
               "not named. The licorice group (yaṣṭyādi) is not listed. The verse continues in 20."),
    "explain_hi": ("यह श्लोक एक नई दूध वाली बस्ति शुरू करता है: गोक्षुर यानी गोखरू के बिना पंचमूल को, अलग-अलग पल के अंशों में, पकाए (विपचेत्)। "
                   "पकाना आढक भर दूध में है। "
                   "दूसरी पंक्ति में ‘चार प्रस्थ’ और पिसे हुए यष्टि यानी मुलेठी आदि द्रव्यों से युक्त होना आता है; चार प्रस्थ किसके हैं, यह नहीं कहा। "
                   "कौन-सा पंचमूल है, यह भी स्पष्ट नहीं।"),
    "hook": "पंचमूल (गोखरू बिना), पल-पल अलग; आढक दूध; मुलेठी आदि पिसे।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "In what liquid is the pañcamūla of verse 19 cooked?",
            ("In an āḍhaka of milk", "क्षीराढके = in an āḍhaka of milk."),
            [("In an āḍhaka of water", "Water is the liquid of verse 14."),
             ("In cow's urine (gomūtra)", "Cow's urine is the liquid of verse 10."),
             ("In the juice of meat", "No meat juice is named in verse 19.")],
            "क्षीर-आढके: the roots are cooked in milk.",
            "क्षीराढके विपचेत् = cook in an āḍhaka of milk."),
        match(1, "Match each word of verse 19 to its meaning.",
              [["पृथक्", "separately"], ["पलांश", "a pala portion"],
               ["विपचेत्", "one should cook"], ["यष्ट्यादि", "beginning with licorice"]],
              "These words give the measure, the action and the added group.",
              "पृथक् = separately; पल-अंश = portion of a pala; विपचेत् = one should cook."),
        order(2, "Put these words of line 2 in the order of verse 19.",
              ["क्षीराढके", "चतुःप्रस्थम्", "पिष्टैः", "यष्ट्यादिभिः", "युतम्"],
              "Line 2: in an āḍhaka of milk, four prasthas, with the ground ones beginning with licorice, joined.",
              "क्षीराढके · चतुःप्रस्थं · पिष्टैर् · यष्ट्यादिभिर् · युतम्.",
              role="extend",
              teaches="Line 2 of verse 19 gives the milk, four prasthas, and the ground licorice group, in that order."),
        mcq("discriminate", 3, "Which split of यष्ट्यादिभिः is right?",
            ("यष्टि + आदिभिः", "इ + आ → या: यष्टि (licorice) + आदिभिः (beginning with)."),
            [("यष्ट्य + आदिभिः", "यष्ट्य is not a word; the stem is यष्टि."),
             ("यष्टिः + आदिभिः", "A visarga after इ before a vowel would give यष्टिरादिभिः."),
             ("यष्ट्या + दिभिः", "दिभिः is not a word; the second member is आदि.")],
            "Before a different vowel, इ becomes य्: यष्टि + आदि → यष्ट्यादि.",
            "इ + आ → या."),
        mcq("apply", 4, "How does verse 19 measure the roots of its pañcamūla?",
            ("Separately, in pala portions", "पृथक्पलांशम् = separately, in portions of a pala."),
            [("Together, two palas in all", "No total of two palas is given; the text says separately."),
             ("By the prasṛta, all mixed", "No prasṛta is named; the roots are taken separately."),
             ("By the handful, unweighed", "The measure is the pala, a weight.")],
            "पृथक् (separately) + पल-अंश (pala portion).",
            "पृथक्पलांशम् = separately, pala portions."),
        mcq("transfer", 5,
            "Like चतुःप्रस्थम् (four prasthas), what does an invented त्रिप्रस्थम् mean?",
            ("Three prasthas", "Number + measure (dvigu) = that many of the measure."),
            [("The third prastha", "The third would be तृतीय प्रस्थ."),
             ("A third of a prastha", "A third would be प्रस्थ-त्रिभाग."),
             ("A prastha cooked thrice", "No cooking is in the word.")],
            "Same build as चतुःप्रस्थ and द्विप्रस्थ (verse 14): number + measure.",
            "Number + measure = that many units (dvigu).",
            teaches="A number joined to a measure counts that measure: चतुःप्रस्थम् (four prasthas), त्रिप्रस्थम् (three prasthas)."),
    ],
}

# ---------------------------------------------------------------- unit 20
AUTHORED["20"] = {
    "title": "बस्तिः सुपूजितः विशेषाद्बाल",
    "question": "With what is the milk enema of verses 19-20 joined, and for whom is it especially esteemed?",
    "rule": ("Joined with honey, oil, ghee and rock salt (sindhūttha), the enema is well "
             "esteemed, especially for children, the old, women, the delicate and those of a "
             "comfortable nature."),
    "limits": ("Printed -युक्तं is neuter beside masculine बस्तिः (flagged); the printed space in "
               "सु पूजितः is read सुपूजितः. No question rests on either. विशेषात् is 'especially', "
               "not 'only'. Printed वाल is read बाल. The genitive is rendered 'for'."),
    "explain_hi": ("मधु, तैल, घी और सिन्धूत्थ यानी सेंधा नमक से युक्त यह बस्ति भलीभाँति प्रशंसित है। "
                   "‘विशेषात्’ यानी विशेष रूप से: बालकों, वृद्धों, स्त्रियों, सुकुमार लोगों और सुखी स्वभाव वालों के लिए। "
                   "‘विशेषात्’ दूसरों को रोकता नहीं, केवल ज़ोर देता है। "
                   "छपा ‘वाल’ यहाँ ‘बाल’ पढ़ा गया है (व/ब की छपाई-आदत)।"),
    "hook": "मधु-तैल-घी-सेंधा: बच्चे, बूढ़े, स्त्री, सुकुमार, सुखी के लिए विशेष।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "For whom especially does verse 20 esteem this enema?",
            ("Children, the old, women, the delicate",
             "बाल-वृद्ध-स्त्री-सुकुमार-सुखात्मनाम्."),
            [("Warriors, workers and the athletes",
              "None of these is named in the verse."),
             ("People with a strong digestive fire",
              "No digestive fire is named in verse 20."),
             ("Kings, their ministers and priests",
              "No king or minister is named here.")],
            "The genitive compound lists children, the old, women, the delicate, the comfort-natured.",
            "विशेषात् बाल-वृद्ध-स्त्री-सुकुमार-सुखात्मनाम्."),
        match(1, "Match each word of line 2 of verse 20 to its meaning.",
              [["बाल", "child"], ["वृद्ध", "old person"],
               ["स्त्री", "woman"], ["सुकुमार", "delicate person"]],
              "Four of the five groups of line 2.",
              "बाल = child; वृद्ध = old; स्त्री = woman; सुकुमार = delicate."),
        order(2, "Put these groups in the order of line 2 of verse 20.",
              ["बाल", "वृद्ध", "स्त्री", "सुकुमार", "सुखात्मन्"],
              "Children, the old, women, the delicate, the comfort-natured.",
              "बाल · वृद्ध · स्त्री · सुकुमार · सुखात्मन्.",
              role="extend",
              teaches="Verse 20 names, in order, children, the old, women, the delicate and those of comfortable nature."),
        mcq("discriminate", 3, "Which case is सुखात्मनाम्, and how does the card render it?",
            ("Genitive plural, rendered 'for'", "-नाम् is the genitive plural; the data renders it 'for'."),
            [("Locative plural, rendered 'in'", "The locative plural would end in -सु."),
             ("Instrumental plural, 'with'", "The instrumental plural would end in -भिः."),
             ("Accusative plural, the object", "The accusative plural would be -आत्मनः.")],
            "The whole compound stands in the genitive plural: for (of) these people.",
            "-नाम् = genitive plural."),
        mcq("apply", 4, "What does विशेषात् add to the praise in verse 20?",
            ("Especially, for these people", "विशेषात् = especially; it stresses, it does not exclude."),
            [("Only, for these people", "The card: 'especially', not 'only'."),
             ("Except, for these people", "No exception is stated."),
             ("After, these people are fed", "No feeding or time is named.")],
            "The enema is esteemed for all; these groups are stressed.",
            "विशेषात् = especially (ablative as adverb)."),
        mcq("transfer", 5,
            "सुखात्मन् joins सुख + आत्मन्. Join an invented हित + आहार (wholesome food) the same way. Which is right?",
            ("हिताहार", "अ + आ → आ, as in सुख + आत्मन् = सुखात्मन्."),
            [("हितहार", "The long आ of आहार does not vanish."),
             ("हितेहार", "ए comes from अ + इ, not from अ + आ."),
             ("हितौहार", "औ comes from अ + ओ/औ, not from अ + आ.")],
            "Like vowels join long: अ + आ → आ.",
            "अ + आ → आ.",
            teaches="अ + आ joins as आ: सुख + आत्मन् → सुखात्मन्; हित + आहार → हिताहार."),
    ],
}

# ---------------------------------------------------------------- unit 21
AUTHORED["21"] = {
    "title": "क्षीरबस्तिस्तथा",
    "question": "With which plants are the preparation and the milk enema of verse 21 made?",
    "rule": ("Likewise, a preparation made with sahācara, balā, sārivā and darbha; and likewise a "
             "milk enema (kṣīrabasti) with abhīru, guḍūcī and the pair of bṛhatī. The milk "
             "cooking follows in verse 22."),
    "limits": ("The noun prepared in line 1 is not stated. sahācara (printed sāhacara), darbha, "
               "abhīru (śatāvarī) and the bṛhatī pair (with kaṇṭakārī) are probable; the second "
               "bṛhatī is not named. The space before ऽभीरु is a print slip."),
    "explain_hi": ("पहली पंक्ति कहती है: उसी प्रकार (तद्वत्) सहाचर यानी सम्भवतः कटसरैया, बला यानी बरियार, सारिवा यानी अनन्तमूल और दर्भ यानी सम्भवतः कुश से साधित यानी तैयार किया हुआ; क्या तैयार हुआ, यह नहीं कहा। "
                   "दूसरी पंक्ति क्षीरबस्ति यानी दूध की बस्ति का नाम लेती है: अभीरु यानी सम्भवतः शतावरी, गुडूची यानी गिलोय और बृहती-द्वय यानी दो बृहती के साथ। "
                   "दूध पकाने की बात श्लोक २२ में है।"),
    "hook": "तद्वत्: सहाचर-बला-सारिवा-दर्भ; क्षीरबस्ति: अभीरु-गुडूची-दो बृहती।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "What kind of enema does line 2 of verse 21 name?",
            ("A milk enema (kṣīrabasti)", "क्षीरबस्तिः = milk enema."),
            [("A cow's-urine enema", "Cow's urine is in verse 10, not here."),
             ("An enema of meat juice", "No meat juice is named in verse 21."),
             ("An oil enema (anuvāsana)", "No oil enema is named here.")],
            "क्षीर (milk) + बस्ति (enema): the kṣīrabasti.",
            "क्षीरबस्ति = milk enema."),
        match(1, "Match each word of verse 21 to its meaning on the card.",
              [["तद्वत्", "likewise"], ["साधित", "prepared"],
               ["गुडूची", "giloy (Tinospora cordifolia)"], ["सारिवा", "Indian sarsaparilla"]],
              "Two structure words and two plants (standard identifications).",
              "तद्वत् = likewise; साधित = prepared; गुडूची = giloy; सारिवा = Indian sarsaparilla."),
        order(2, "Put the plants of the milk enema in the order of line 2 of verse 21.",
              ["अभीरु", "गुडूची", "बृहतीद्वय"],
              "Line 2: abhīru, guḍūcī, the pair of bṛhatī.",
              "क्षीरबस्तिस्तथा · अभीरु · गुडूची · बृहतीद्वयैः.",
              role="extend",
              teaches="The milk enema of verse 21 takes abhīru, guḍūcī and the bṛhatī pair, in that order."),
        mcq("discriminate", 3, "Which split of क्षीरबस्तिस्तथा is right?",
            ("क्षीरबस्तिः + तथा", "A visarga before त becomes स्: बस्तिः + तथा → बस्तिस्तथा."),
            [("क्षीरबस्ति + स्तथा", "स्तथा is not a word; the स् comes from the visarga."),
             ("क्षीरबस्तिम् + तथा", "म् before त would give क्षीरबस्तिं तथा."),
             ("क्षीरबस्तिस् + अथा", "अथा is not a word; the word is तथा (likewise).")],
            "क्षीरबस्तिः (nom.) + तथा (likewise).",
            "ः + त → स्त."),
        mcq("apply", 4, "What does बृहतीद्वय mean on the card?",
            ("A pair of bṛhatī; the second is unnamed",
             "द्वय = pair; the usual partner kaṇṭakārī is probable, not named."),
            [("Two palas of the bṛhatī root, weighed",
              "द्वय counts plants, not palas."),
             ("Bṛhatī root cooked down twice in milk",
              "No cooking is in the word."),
             ("Bṛhatī joined with guḍūcī as one drug",
              "Guḍūcī is a separate member of the list.")],
            "-द्वय = a pair; the text does not name the second plant.",
            "X-द्वय = the pair of X."),
        mcq("transfer", 5,
            "Like बृहतीद्वय (the pair of bṛhatī), what does an invented पञ्चमूलद्वयम् mean?",
            ("The pair of pañcamūlas", "-द्वय after a noun names a pair of that thing."),
            [("The second pañcamūla", "The second would be द्वितीय पञ्चमूल."),
             ("Half of a pañcamūla", "Half would be अर्ध-पञ्चमूल."),
             ("Two roots of a pañcamūla", "The pair is of whole groups, not of roots.")],
            "Same build as बृहतीद्वय: X + द्वय = the pair of X.",
            "X-द्वय = the pair of X.",
            teaches="-द्वय after a noun means 'the pair of X': बृहतीद्वय, पञ्चमूलद्वयम्."),
    ],
}

# ---------------------------------------------------------------- unit 22
AUTHORED["22"] = {
    "title": "सिद्धं पयो मागधिका",
    "question": "With what paste is the milk cooked in verse 22, and how is its pañcamūla measured?",
    "rule": ("Milk cooked with a paste (kalka) of māgadhikā (long pepper) and yaṣṭīmadhuka "
             "(licorice); the pañcamūla beginning with bṛhatī, each drug measured at a pala."),
    "limits": ("Line 2 has no verb, and the link of प्रतिद्रव्यम् with पलोन्मितम् is not certain. "
               "The bṛhatī group is probably the lesser pañcamūla; the text does not list it. "
               "कल्कवत् can also mean 'like a paste'."),
    "explain_hi": ("पहली पंक्ति कहती है: दूध सिद्ध यानी पकाया हुआ हो, मागधिका यानी पीपर और यष्टीमधु यानी मुलेठी के कल्क यानी लुगदी के साथ। "
                   "‘-वत्’ यहाँ ‘वाला’ है: कल्क वाला। "
                   "दूसरी पंक्ति बृहती से आरम्भ होने वाले पंचमूल की बात करती है, जिसका प्रत्येक द्रव्य पल से मापा हुआ है (पलोन्मित)। "
                   "पाँच जड़ों के नाम पाठ में नहीं हैं।"),
    "hook": "पीपर-मुलेठी का कल्क, दूध में; बृहती वाला पंचमूल, हर द्रव्य पल भर।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "With the paste of which two drugs is the milk of verse 22 cooked?",
            ("Long pepper and licorice", "मागधिका-यष्टीमधुक-कल्कवत्."),
            [("Guḍūcī and Indian sarsaparilla", "These are in verse 21."),
             ("Rock salt and some honey", "Neither is named in verse 22."),
             ("Vacā and the castor root", "Neither is named in verse 22.")],
            "The paste is of māgadhikā (long pepper) and yaṣṭīmadhuka (licorice).",
            "मागधिका = long pepper; यष्टीमधुक = licorice; कल्क = paste."),
        match(1, "Match each word of verse 22 to its meaning.",
              [["मागधिका", "long pepper"], ["यष्टीमधुक", "licorice"],
               ["कल्क", "paste"], ["पलोन्मित", "measured by a pala"]],
              "The two drugs, the paste and the measure.",
              "मागधिका = long pepper; यष्टीमधुक = licorice; कल्क = paste; पल-उन्मित = measured by a pala."),
        order(2, "Put these words of line 1 in the order of verse 22.",
              ["सिद्धम्", "पयः", "मागधिका", "यष्टीमधुक", "कल्कवत्"],
              "Line 1: cooked, milk, long pepper, licorice, having the paste.",
              "सिद्धं · पयो · मागधिका-यष्टीमधुक-कल्कवत्.",
              role="extend",
              teaches="Verse 22 opens 'cooked milk' and then names the paste of long pepper and licorice."),
        mcq("discriminate", 3, "Which split of पलोन्मितम् is right?",
            ("पल + उन्मितम्", "अ + उ → ओ: पल + उन्मित (measured)."),
            [("पलो + न्मितम्", "न्मितम् is not a word."),
             ("पलः + उन्मितम्", "A visarga after अ before उ would be dropped: पल उन्मितम्."),
             ("पलम् + उन्मितम्", "म् before a vowel stays: पलमुन्मितम्.")],
            "Inside the compound, पल + उन्मित joins as पलोन्मित.",
            "अ + उ → ओ."),
        mcq("apply", 4, "Which pañcamūla does line 2 of verse 22 name?",
            ("The one beginning with bṛhatī", "बृहत्यादि पञ्चमूलम् = the pañcamūla headed by bṛhatī."),
            [("The one beginning with bilva", "Bilva is not named in verse 22."),
             ("The one beginning with musta", "Musta heads the list of verse 12."),
             ("The one with castor at its head", "Castor is not named in verse 22.")],
            "बृहती-आदि = beginning with bṛhatī; the members are not listed.",
            "X-आदि = beginning with X."),
        mcq("transfer", 5,
            "Like प्रतिद्रव्यम् (for each drug), what does an invented प्रतिदिनम् mean?",
            ("Every day", "प्रति- before a noun (avyayībhāva) = for each, every."),
            [("Against the day", "प्रति here distributes; it does not oppose."),
             ("Before the day", "Before would be प्राक्."),
             ("For one day only", "प्रति- means each one, not one only.")],
            "Same build as प्रतिद्रव्यम्: प्रति + noun = each / every.",
            "प्रति + noun (avyayībhāva) = for each.",
            teaches="प्रति- before a noun as an indeclinable compound means 'for each': प्रतिद्रव्यम् (each drug), प्रतिदिनम् (every day)."),
    ],
}

# ---------------------------------------------------------------- unit 23
AUTHORED["23"] = {
    "title": "द्विपलं शालिगोधूम",
    "question": "Which grains and which milk does verse 23 bring into the preparation?",
    "rule": ("Two palas of śāli rice, wheat, barley and black gram, with yaṣṭikā (probably "
             "licorice); goat's milk cooked with those; the fluid of a fowl's egg; and sitā "
             "(crystallised sugar)."),
    "limits": ("Whether two palas is for each grain or for all is not decided. The verse has no "
               "verb. कुकुट is a spelling of कुक्कुट (fowl); cock or hen is not stated. तैः (by "
               "those) points back to the drugs and grains before it."),
    "explain_hi": ("पहली पंक्ति अन्न गिनाती है: द्विपल यानी दो पल शालि यानी अगहनी चावल, गोधूम यानी गेहूँ, यव और माष यानी उड़द, यष्टिका यानी सम्भवतः मुलेठी सहित। "
                   "दो पल प्रत्येक के हैं या सबके, यह नहीं कहा। "
                   "दूसरी पंक्ति में ‘तैः सिद्धम्’ यानी उनसे पकाया हुआ छागल यानी बकरी का दूध, कुक्कुट के अण्डे का रस और सिता यानी मिश्री आते हैं।"),
    "hook": "चावल, गेहूँ, यव, उड़द (दो पल) + मुलेठी; उनसे बकरी का दूध; अण्डा-रस, मिश्री।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Which milk is cooked with the grains in verse 23?",
            ("Goat's milk (chāgala)", "छागलं क्षीरम् = goat's milk."),
            [("Cow's milk (gavya)", "The verse says छागल, of a goat."),
             ("Buffalo's milk (māhiṣa)", "No buffalo is named in the verse."),
             ("Sheep's milk", "No sheep is named in the verse.")],
            "छागल = of a goat; क्षीर = milk.",
            "छागलं क्षीरम् = goat's milk."),
        match(1, "Match each word of verse 23 to its meaning on the card.",
              [["शालि", "winter rice"], ["गोधूम", "wheat"],
               ["माष", "black gram"], ["सिता", "crystallised sugar"]],
              "Three grains of line 1 and the sugar of line 2.",
              "शालि = winter rice; गोधूम = wheat; माष = black gram; सिता = crystallised sugar."),
        order(2, "Put the grains in the order of line 1 of verse 23.",
              ["शालि", "गोधूम", "यव", "माष"],
              "Line 1: śāli rice, wheat, barley, black gram, then सयष्टिकम्.",
              "द्विपलं · शालि · गोधूम · यव · माषं · सयष्टिकम्.",
              role="extend",
              teaches="The grains of verse 23 are śāli rice, wheat, barley and black gram, in that order."),
        mcq("discriminate", 3, "What does तैः in तैः सिद्धम् point to, on the card?",
            ("The grains and drugs named before it", "तैः = by those: the ingredients just listed."),
            [("The two salts that follow later on", "The salts come in verse 24, after this."),
             ("The egg fluid named after the milk", "The egg fluid follows; तैः looks back."),
             ("The children and women of verse 20", "Those people are not ingredients.")],
            "तैः is instrumental plural: the milk is cooked with those ingredients.",
            "तैः = with / by those (instrumental plural of तद्)."),
        mcq("apply", 4, "Does verse 23 say whether the two palas are for each grain?",
            ("No; it leaves that open", "The card: each grain or all together is not decided."),
            [("Yes; two palas of each", "The text gives no 'each'."),
             ("Yes; two palas in total", "The text does not say 'in total' either."),
             ("Yes; two palas of rice only", "द्विपलम् stands before the whole list.")],
            "द्विपलम् is given once; its scope is not stated.",
            "द्विपलम् = two palas (scope not stated)."),
        mcq("transfer", 5,
            "Which invented phrase means cooked with those drugs, built like तैः सिद्धम्?",
            ("तैर्द्रव्यैः सिद्धम्", "तैः and द्रव्यैः are both instrumental plural: with those drugs."),
            [("तेषु द्रव्येषु सिद्धम्", "This is the locative: cooked in those drugs."),
             ("तेषां द्रव्याणां सिद्धम्", "This is the genitive: cooked of those drugs."),
             ("तानि द्रव्याणि सिद्धम्", "This is the accusative, not 'with'.")],
            "The instrumental gives 'with / by': तैः, द्रव्यैः.",
            "तैः = instrumental plural of तद्: with those.",
            teaches="तैः (with those) is the instrumental plural of तद्, and its noun takes the same case: तैर्द्रव्यैः सिद्धम्."),
    ],
}

# ---------------------------------------------------------------- unit 24
AUTHORED["24"] = {
    "title": "बस्तिः शुक्रकृत्परम्",
    "question": "What does the enema of verse 24 do, and to which other fluids does the formula extend?",
    "rule": ("With ghee, honey and two salts, an enema made with those is a maker of semen, "
             "supremely. This formula (kalpa) holds also for the egg fluids of the peacock, "
             "gonarda, fish and the like."),
    "limits": ("The two salts are not named. परम् may be 'supremely' or 'best'. gonarda is an "
               "unidentified creature, and the printed space in शिखिगो नर्द is a print break: no "
               "question uses either. 'Is' is supplied."),
    "explain_hi": ("घी, शहद और दो लवणों के साथ, उन (पिछले द्रव्यों) से बनी बस्ति अत्यन्त शुक्रकृत् यानी शुक्र उत्पन्न करने वाली है। "
                   "दो लवण कौन-से हैं, यह नहीं कहा। "
                   "दूसरी पंक्ति कहती है कि यही कल्प यानी विधि मोर, गोनर्द, मछली आदि के अण्डों के रसों में भी है (‘अपि’ = भी)। "
                   "गोनर्द की पहचान नहीं है।"),
    "hook": "घी, शहद, दो लवण: शुक्रकृत्; यही विधि मोर, मछली आदि के अण्डा-रस में भी।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "What does verse 24 say the enema makes, supremely?",
            ("Semen (śukra)", "शुक्रकृत् = maker of semen; परम् = supremely."),
            [("Fat and flesh", "Neither is named in verse 24."),
             ("Sound sleep", "Sleep is not named in verse 24."),
             ("Clear eyes", "The eyes are praised in verse 18, not here.")],
            "शुक्र + -कृत् (making) = maker of semen.",
            "शुक्रकृत् = maker of semen."),
        match(1, "Match each word of verse 24 to its meaning.",
              [["आज्य", "ghee"], ["क्षौद्र", "honey"],
               ["शुक्रकृत्", "maker of semen"], ["कल्प", "formula, preparation"]],
              "Two additives, the effect and the word for the formula.",
              "आज्य = ghee; क्षौद्र = honey; शुक्रकृत् = maker of semen; कल्प = formula."),
        order(2, "Put these words of line 1 in the order of verse 24.",
              ["साज्यक्षौद्रद्विलवणैः", "तैः", "बस्तिः", "शुक्रकृत्", "परम्"],
              "Line 1: with ghee, honey, two salts; by those; the enema; maker of semen; supremely.",
              "साज्यक्षौद्रद्विलवणैस् · तैर् · बस्तिः · शुक्रकृत् · परम्.",
              role="extend",
              teaches="Line 1 of verse 24 runs: additives, तैः, बस्तिः, शुक्रकृत्, परम्."),
        mcq("discriminate", 3, "Which split of the end of मत्स्याद्यण्डरसेष्वपि is right?",
            ("रसेषु + अपि", "उ + अ → व: रसेषु (in the fluids) + अपि (also)."),
            [("रसेष्व + अपि", "रसेष्व is not a form; the locative plural is रसेषु."),
             ("रसेषु + वपि", "वपि is not a word; the word is अपि."),
             ("रसेषः + अपि", "रसेषः is not a form of रस.")],
            "Before a different vowel, उ becomes व्: रसेषु + अपि → रसेष्वपि.",
            "उ + अ → व."),
        mcq("apply", 4, "Where else does verse 24 say this formula (kalpa) holds?",
            ("In the egg fluids of other creatures", "मत्स्याद्यण्डरसेषु अपि = also in egg fluids of fish and the like."),
            [("In the meat juices of dry-land beasts", "Jāṅgala juice is in verse 15, not here."),
             ("In the milk of goats, sheep and cows", "Goat's milk is in verse 23; no extension to milks is made."),
             ("In decoctions of cow's urine and roots", "No cow's urine is named in verse 24.")],
            "Line 2 extends the formula to egg fluids (peacock, gonarda, fish and the like).",
            "कल्पो ऽयं … अण्डरसेषु अपि = this formula also in egg fluids."),
        mcq("transfer", 5,
            "कल्पो ऽयम् joins कल्पः + अयम्. Join an invented योगः + अयम् (this formula) the same way. Which is right?",
            ("योगोऽयम्", "-अः + अ → -ओ ऽ: the अ of अयम् is elided (avagraha)."),
            [("योगायम्", "अ + अ → आ applies to bare vowels, not to -अः."),
             ("योगरयम्", "र् replaces a visarga after vowels other than अ/आ."),
             ("योगयम्", "The visarga does not vanish without a trace here.")],
            "Same rule as कल्पः + अयम् = कल्पोऽयम्.",
            "-अः + अ → -ओऽ.",
            teaches="-अः before अ becomes -ओ and the अ is elided (ऽ): कल्पः + अयम् → कल्पोऽयम्; योगः + अयम् → योगोऽयम्."),
    ],
}

# ---------------------------------------------------------------- unit 25
AUTHORED["25"] = {
    "title": "रसः कुलीरमांसस्य",
    "question": "Which juice and additions make the enema of verse 25 the most aphrodisiac?",
    "rule": ("The juice of crab flesh, joined with the fluid of sparrow eggs; with sugar, ghee and "
             "honey, the enema is considered the most aphrodisiac (vṛṣatama, 'most bull-like')."),
    "limits": ("The verse gives no measure or method. aṇḍa can be one egg or eggs in general. The "
               "printed space in मधु र्बस्तिर् is a break inside मधुः बस्तिः; no question uses it."),
    "explain_hi": ("कुलीर यानी केकड़े के मांस का रस, चटक यानी गौरैया के अण्डे के रस से युक्त (अन्वित)। "
                   "शर्करा, घी और शहद के साथ यह बस्ति वृषतम यानी सबसे अधिक वृष्य (पौरुष बढ़ाने वाली) मानी गई है (मतः)। "
                   "‘-तम’ उत्तम-अवस्था का प्रत्यय है: सबसे अधिक। "
                   "मात्रा या विधि नहीं दी गई।"),
    "hook": "केकड़ा-रस + गौरैया-अण्डा-रस + शक्कर, घी, शहद = वृषतम बस्ति।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "Whose flesh gives the juice in verse 25?",
            ("The crab (kulīra)", "रसः कुलीरमांसस्य = the juice of crab flesh."),
            [("The goat (basta)", "Goat testes come in verse 26."),
             ("The peacock (śikhin)", "The peacock's eggs are in verse 24."),
             ("The fish (matsya)", "Fish eggs are in verse 24.")],
            "कुलीर = crab; मांस = flesh; रस = juice.",
            "कुलीरमांसस्य रसः = juice of crab flesh."),
        match(1, "Match each word of verse 25 to its meaning.",
              [["कुलीर", "crab"], ["चटक", "sparrow"],
               ["शर्करा", "sugar"], ["मत", "considered"]],
              "Two creatures, an additive and the closing word.",
              "कुलीर = crab; चटक = sparrow; शर्करा = sugar; मत = considered."),
        order(2, "Put these words in the order of verse 25.",
              ["रसः", "कुलीरमांसस्य", "चटकाण्डरसान्वितः", "वृषतमः", "मतः"],
              "The juice, of crab flesh, joined with sparrow-egg fluid; then the enema, most aphrodisiac, considered.",
              "रसः · कुलीरमांसस्य · चटकाण्डरसान्वितः ‖ … बस्तिर् · वृषतमो · मतः.",
              role="extend",
              teaches="Verse 25 names the crab juice and the sparrow-egg fluid, then calls the enema वृषतम."),
        mcq("discriminate", 3, "What does the suffix -तम add in वृषतमः?",
            ("Most: the superlative", "-तम marks the superlative: most bull-like, most aphrodisiac."),
            [("More: the comparative", "The comparative suffix is -तर."),
             ("Like: a comparison", "Likeness is -वत् or इव."),
             ("Not: a negation", "Negation is अ- / न-, before the word.")],
            "वृष (bull) + -तम (most) = most bull-like.",
            "-तम = superlative; -तर = comparative."),
        mcq("apply", 4, "In verse 25, what is the crab juice joined with?",
            ("The fluid of sparrow eggs", "चटक-अण्ड-रस-अन्वितः = joined with sparrow-egg fluid."),
            [("The fluid of a fowl's egg", "The fowl's egg is in verse 23."),
             ("The milk of a she-goat", "Goat's milk is in verse 23."),
             ("The fluid of peacock eggs", "Peacock eggs are in verse 24.")],
            "Line 1 joins crab juice with sparrow-egg fluid; line 2 adds sugar, ghee, honey.",
            "चटकाण्डरसान्वितः = joined with sparrow-egg fluid."),
        mcq("transfer", 5,
            "Beside वृषतमः (most aphrodisiac), which form means more aphrodisiac (the comparative)?",
            ("वृषतरः", "-तर marks the comparative: more."),
            [("वृषवत्", "-वत् means 'like' (like a bull)."),
             ("वृषत्वम्", "-त्व makes an abstract noun: bull-ness."),
             ("वृषतमः", "This is the superlative of the verse: most.")],
            "-तर (more) and -तम (most) build the comparison of adjectives.",
            "-तर = more; -तम = most.",
            teaches="-तर marks the comparative and -तम the superlative: वृषतरः (more), वृषतमः (most aphrodisiac)."),
    ],
}

# ---------------------------------------------------------------- unit 26
AUTHORED["26"] = {
    "title": "सिद्धं पयो बस्तमुष्क",
    "question": "With which animal parts and plants is the milk of verse 26 cooked?",
    "rule": ("With testes of the he-goat and (conjecturally) the boar, and with the flesh of crab "
             "and sparrow; milk cooked with a he-goat's testis, uccaṭā and ikṣuraka (probably "
             "kokilākṣa), and honey."),
    "limits": ("Printed मूकर is read सूकर (boar) only as a conjecture (flagged): no question uses "
               "it. uccaṭā is unidentified; ikṣuraka is probable. The case of the line 2 items is "
               "not clear in the print. No verb; how line 1 links to the milk is not stated."),
    "explain_hi": ("पहली पंक्ति तृतीया में द्रव्य गिनाती है: बस्त यानी बकरे और (अनुमानित पाठ पर) सूअर से उत्पन्न मुष्क यानी अण्डकोश, तथा कुलीर यानी केकड़े और चटक यानी गौरैया का आमिष यानी मांस। "
                   "दूसरी पंक्ति कहती है: दूध सिद्ध यानी पकाया हुआ, बकरे के मुष्क, उच्चटा और इक्षुरक यानी सम्भवतः तालमखाना के साथ, और शहद। "
                   "उच्चटा की पहचान नहीं है।"),
    "hook": "बकरे का मुष्क, केकड़ा-गौरैया का मांस; दूध + उच्चटा, तालमखाना, शहद।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "What is cooked (सिद्धम्) in line 2 of verse 26?",
            ("Milk (payas)", "सिद्धं पयः = cooked milk."),
            [("Meat juice", "The meat is in line 1; line 2 cooks milk."),
             ("Pure ghee", "Ghee is not named in verse 26."),
             ("Cow's urine", "Cow's urine is not named here.")],
            "सिद्धम् agrees with पयः: milk, cooked.",
            "सिद्धं पयः = cooked milk."),
        match(1, "Match each word of verse 26 to its meaning.",
              [["मुष्क", "testis"], ["बस्त", "he-goat"],
               ["आमिष", "flesh"], ["मधु", "honey"]],
              "Words of the animal items and the last additive.",
              "मुष्क = testis; बस्त = he-goat; आमिष = flesh; मधु = honey."),
        order(2, "Put the items with the milk in the order of line 2 of verse 26.",
              ["बस्तमुष्क", "उच्चटा", "इक्षुरक", "मधु"],
              "Line 2: he-goat's testis, uccaṭā, ikṣuraka, honey.",
              "सिद्धं पयो · बस्तमुष्क · उच्चटा · इक्षुरकं · मधु.",
              role="extend",
              teaches="The milk of verse 26 goes with he-goat's testis, uccaṭā, ikṣuraka and honey, in that order."),
        mcq("discriminate", 3, "Which split of उच्चटेक्षुरकम् is right?",
            ("उच्चटा + इक्षुरकम्", "आ + इ → ए: उच्चटा + इक्षुरक."),
            [("उच्चट + एक्षुरकम्", "एक्षुरक is not a word, and अ + ए would give ऐ."),
             ("उच्चटाः + इक्षुरकम्", "-आः before a vowel drops the visarga with no join."),
             ("उच्चटम् + इक्षुरकम्", "म् before a vowel stays: उच्चटमिक्षुरकम्.")],
            "आ/अ + इ joins as ए.",
            "आ + इ → ए."),
        mcq("apply", 4, "Whose flesh (आमिष) does line 1 of verse 26 name?",
            ("Crab and sparrow", "कुलीर-चटक-आमिषैः = with the flesh of crab and sparrow."),
            [("Goat and fowl", "The goat gives testes here; no fowl is named."),
             ("Peacock and fish", "These are in verse 24."),
             ("Deer and quail", "Neither is named in verse 26.")],
            "The second word of line 1 names crab and sparrow flesh.",
            "कुलीरचटकामिषैः = with crab and sparrow flesh."),
        mcq("transfer", 5,
            "Join an invented शर्करा + इक्षु (sugar, sugarcane) by the rule of उच्चटेक्षुरक. Which is right?",
            ("शर्करेक्षु", "आ + इ → ए, as in उच्चटा + इक्षुरक."),
            [("शर्करैक्षु", "ऐ comes from अ/आ + ए/ऐ, not + इ."),
             ("शर्कराक्षु", "The इ does not vanish."),
             ("शर्करीक्षु", "आ + इ does not give ई.")],
            "आ + इ joins as ए (guṇa).",
            "आ + इ → ए.",
            teaches="अ/आ + इ/ई → ए: उच्चटा + इक्षुरक → उच्चटेक्षुरक; शर्करा + इक्षु → शर्करेक्षु."),
    ],
}

# ---------------------------------------------------------------- unit 27
AUTHORED["27"] = {
    "title": "बस्तिर्वृषतमः परः",
    "question": "What enema does verse 27 praise, and what food does it add?",
    "rule": ("On a conjectural reading, an enema rich in ghee and with little salt is the most "
             "aphrodisiac, supreme. Food is taken with milk cooked with ātmaguptā (cowhage), "
             "uccaṭā and ikṣura."),
    "limits": ("Low confidence. Printed निर्घृताढ्यो would mean 'rich in no ghee'; 'rich in ghee' is a "
               "conjecture (open point), so no question uses it. The verb for the food is not "
               "stated. uccaṭā is unidentified, ikṣura probable."),
    "explain_hi": ("अनुमानित पाठ पर, घी से भरपूर और अल्प लवण वाली बस्ति वृषतम यानी सबसे अधिक वृष्य और पर यानी उत्तम है। "
                   "छपा ‘निर्घृताढ्यो’ अपने में विरोधी है, इसलिए यह पाठ अनिश्चित है। "
                   "दूसरी पंक्ति भोज्य यानी भोजन की बात करती है: सिद्ध दूध के साथ, जो आत्मगुप्ता यानी केवाँच, उच्चटा और इक्षुर यानी सम्भवतः तालमखाना से पकाया गया हो।"),
    "hook": "(अनुमानित) घी भरपूर, नमक कम: वृषतम; भोजन केवाँच वाले दूध से।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "With which plants is the milk of line 2 of verse 27 cooked?",
            ("Ātmaguptā, uccaṭā and ikṣura", "आत्मगुप्ता-उच्चटा-इक्षुरैः."),
            [("Musta, pāṭhā and amṛtā", "These open the list of verse 12."),
             ("Balā, sārivā and darbha", "These are in verse 21."),
             ("Māgadhikā and yaṣṭīmadhu", "These make the paste of verse 22.")],
            "The milk is cooked with cowhage, uccaṭā and ikṣura.",
            "आत्मगुप्ता = cowhage; उच्चटा (unidentified); इक्षुर (probable)."),
        match(1, "Match each word of verse 27 to its meaning.",
              [["आत्मगुप्ता", "cowhage"], ["भोज्य", "food, to be eaten"],
               ["पयस्", "milk"], ["परः", "supreme"]],
              "A plant, the food, the milk and the praise word.",
              "आत्मगुप्ता = cowhage; भोज्य = food; पयस् = milk; पर = supreme."),
        order(2, "Put these words of line 2 in the order of verse 27.",
              ["सिद्धेन", "पयसा", "भोज्यम्", "आत्मगुप्ता", "उच्चटा", "इक्षुरैः"],
              "Line 2: with cooked milk, food, then the three plants.",
              "सिद्धेन · पयसा · भोज्यम् · आत्मगुप्ता · उच्चटा · इक्षुरैः.",
              role="extend",
              teaches="Line 2 of verse 27 runs: with cooked milk, food, cowhage, uccaṭā, ikṣura."),
        mcq("discriminate", 3, "What form is भोज्यम्, as the card gives it?",
            ("A gerundive: to be eaten, food", "√भुज् + -य: what is to be eaten, food."),
            [("A past participle: eaten", "The past participle would be भुक्त."),
             ("An absolutive: having eaten", "The absolutive would be भुक्त्वा."),
             ("A present verb: he eats", "The present would be भुङ्क्ते.")],
            "-य after the root makes a gerundive: to be eaten.",
            "भोज्य = to be eaten, food."),
        mcq("apply", 4, "With what is the food of verse 27 taken?",
            ("With milk cooked with the plants", "सिद्धेन पयसा = with the cooked milk."),
            [("With the juice of crab flesh and sugar", "Crab juice is in verse 25."),
             ("With ghee and the two unnamed salts", "These are in verse 24."),
             ("With a decoction made in cow's urine", "No cow's urine is named.")],
            "The instrumental सिद्धेन पयसा gives 'with cooked milk'.",
            "सिद्धेन पयसा भोज्यम् = food with cooked milk."),
        mcq("transfer", 5,
            "Like सिद्धेन पयसा (with cooked milk), which invented phrase means with cooked ghee (घृत)?",
            ("सिद्धेन घृतेन", "Adjective and noun both in the instrumental singular."),
            [("सिद्धं घृतेन", "सिद्धम् is nominative / accusative; it must agree with घृतेन."),
             ("सिद्धेन घृतम्", "घृतम् is not instrumental; 'with' needs घृतेन."),
             ("सिद्धस्य घृतेन", "सिद्धस्य is genitive; it does not agree.")],
            "An adjective takes the case of its noun: सिद्धेन पयसा, सिद्धेन घृतेन.",
            "Adjective agrees with its noun in case, number, gender.",
            teaches="An adjective agrees with its noun: सिद्धेन पयसा (with cooked milk), सिद्धेन घृतेन (with cooked ghee)."),
    ],
}

# ---------------------------------------------------------------- unit 28
AUTHORED["28"] = {
    "title": "अतो दशदशाहेन",
    "question": "What does verse 28 promise to the man who takes these enemas at ten-day intervals?",
    "rule": ("He who thereafter uses the enemas at ten-ten days, nourished like a stallion, goes "
             "to a hundred women; one word (सदृषो) is unclear."),
    "limits": ("Low confidence. सदृषो is not a word and is left unread: no question uses it. "
               "Whether 'ten-ten days' means a ten-day course or a course every ten days is not "
               "decided by the Sanskrit. गच्छति is literally 'goes to'."),
    "explain_hi": ("इसके बाद (अतः) जो दस-दस दिन (दशदशाह) के क्रम से इन बस्तियों का सेवन करता है (निषेवते), उसका फल दूसरी पंक्ति में है। "
                   "वह वाजी यानी घोड़े की तरह पुष्ट होकर सौ स्त्रियों के पास जाता है। "
                   "बीच का छपा ‘सदृषो’ कोई शब्द नहीं है, इसलिए नहीं पढ़ा गया। "
                   "‘दस-दस दिन’ का अर्थ दस दिन का क्रम है या हर दसवें दिन, यह संस्कृत से तय नहीं होता।"),
    "hook": "दस-दस दिन बस्ति: घोड़े-सा पुष्ट, सौ स्त्रियाँ।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Which word of verse 28 gives the timing of the enemas?",
            ("दशदशाहेन", "दश-दश-अहेन = by ten-ten days."),
            [("प्रमदाशतम्", "This is 'a hundred women', the result."),
             ("निषेवते", "This is the verb 'uses'."),
             ("पुष्टः", "This is 'nourished'.")],
            "Line 1 gives the timing: दशदशाहेन.",
            "दशदशाहेन = at ten-ten days."),
        match(1, "Match each word of verse 28 to its meaning.",
              [["वाजी", "stallion"], ["इव", "like"],
               ["पुष्ट", "nourished"], ["प्रमदा", "woman"]],
              "The comparison and the result.",
              "वाजी = stallion; इव = like; पुष्ट = nourished; प्रमदा = woman."),
        order(2, "Put these words of line 1 in the order of verse 28.",
              ["अतः", "दशदशाहेन", "यः तु", "बस्तीन्", "निषेवते"],
              "Line 1: thereafter, at ten-ten days, he who, the enemas, uses.",
              "अतो · दशदशाहेन · यस्तु · बस्तीन् · निषेवते.",
              role="extend",
              teaches="Line 1 of verse 28 runs अतः, दशदशाहेन, यः तु, बस्तीन्, निषेवते."),
        mcq("discriminate", 3, "Which split of बस्तीन्निषेवते is right?",
            ("बस्तीन् + निषेवते", "बस्तीन् (the enemas, acc. pl.) + निषेवते (uses)."),
            [("बस्ती + न्निषेवते", "न्निषेवते is not a word."),
             ("बस्तिं + निषेवते", "That would be singular and stay two words: बस्तिं निषेवते."),
             ("बस्ति + न + निषेवते", "न 'not' would deny the use the verse promises.")],
            "The accusative plural बस्तीन् is the object of निषेवते.",
            "-ईन् = masculine accusative plural of an -इ stem."),
        mcq("apply", 4, "In verse 28, who goes to a hundred women?",
            ("The man who uses these enemas", "यस्तु बस्तीन्निषेवते … गच्छति: he who uses them."),
            [("The physician who gives them", "No physician is named."),
             ("The stallion of the simile", "The stallion is only the comparison (इव)."),
             ("The king of the yāpanas", "That is a title of the enema in verse 18.")],
            "यः (who) in line 1 is the subject of गच्छति in line 2.",
            "यः … निषेवते … गच्छति = he who uses … goes."),
        mcq("transfer", 5,
            "वाजीव joins वाजी + इव. Join an invented नदी + इव (like a river) the same way. Which is right?",
            ("नदीव", "ई + इ → ई: like vowels join long."),
            [("नद्यिव", "ई → य् happens before an unlike vowel, not before इ."),
             ("नदेव", "ए comes from अ + इ, not from ई + इ."),
             ("नदीयिव", "No य् is inserted between like vowels.")],
            "Same rule as वाजी + इव = वाजीव.",
            "ई + इ → ई.",
            teaches="Like vowels join long: वाजी + इव → वाजीव; नदी + इव → नदीव."),
    ],
}

# ---------------------------------------------------------------- unit 29
AUTHORED["29"] = {
    "title": "एते माक्षिकसंयुक्ताः",
    "question": "What do these preparations do with honey, and what do they not bring about?",
    "rule": ("These, joined with honey (mākṣika), make a man exceedingly potent (ativṛṣa). They "
             "bring about neither atiyoga (excess) nor ayoga (lack)."),
    "limits": ("Low confidence. Who 'they' are and the sense of stambhin (checking, retaining) "
               "are open points: no question uses them. mākṣika is honey here, not the mineral. "
               "ete refers to the preparations just described."),
    "explain_hi": ("ये (पिछली तैयारियाँ) माक्षिक यानी शहद से संयुक्त होकर मनुष्य को अतिवृष यानी अत्यन्त पौरुषयुक्त बनाती हैं। "
                   "दूसरी पंक्ति कहती है कि वे न अतियोग यानी अधिक क्रिया करती हैं और न अयोग यानी कम क्रिया। "
                   "‘स्तम्भिनः’ यानी रोकने वाले का अर्थ और ‘वे’ कौन हैं, यह खुला प्रश्न है। "
                   "यहाँ माक्षिक शहद है, खनिज नहीं।"),
    "hook": "शहद के साथ अतिवृष; न अतियोग, न अयोग।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "With what are these preparations joined in verse 29?",
            ("Honey (mākṣika)", "माक्षिकसंयुक्ताः = joined with honey."),
            [("Rock salt (saindhava)", "No salt is named in verse 29."),
             ("Cow's urine (gomūtra)", "No urine is named in verse 29."),
             ("Pure ghee (ghṛta)", "No ghee is named in verse 29.")],
            "माक्षिक = bee-honey in this context.",
            "माक्षिक-संयुक्त = joined with honey."),
        match(1, "Match each word of verse 29 to its meaning.",
              [["माक्षिक", "honey"], ["अतिवृष", "exceedingly potent"],
               ["अतियोग", "excess"], ["अयोग", "lack"]],
              "The additive, the effect and the pair of opposites.",
              "माक्षिक = honey; अतिवृष = exceedingly potent; अतियोग = excess; अयोग = lack."),
        order(2, "Put the words of line 1 in the order of verse 29.",
              ["एते", "माक्षिकसंयुक्ताः", "कुर्वन्ति", "अतिवृषम्", "नरम्"],
              "Line 1: these, joined with honey, make, exceedingly potent, a man.",
              "एते · माक्षिकसंयुक्ताः · कुर्वन्त्य् · अतिवृषं · नरम्.",
              role="extend",
              teaches="Line 1 of verse 29 runs एते, माक्षिकसंयुक्ताः, कुर्वन्ति, अतिवृषम्, नरम्."),
        mcq("discriminate", 3, "Which split of नातियोगम् is right?",
            ("न + अतियोगम्", "अ + अ → आ: न (not) + अतियोगम् (excess)."),
            [("नः + अतियोगम्", "A visarga after अ before अ would give नोऽतियोगम्."),
             ("न + आतियोगम्", "आतियोग is not a word; the word is अतियोग."),
             ("नात् + इयोगम्", "Neither part is a word.")],
            "न + अतियोगम् join with अ + अ → आ.",
            "अ + अ → आ: न + अतियोगम् = नातियोगम्."),
        mcq("apply", 4, "What does line 2 of verse 29 say is brought about?",
            ("Neither excess nor lack", "नातियोगं न चायोगम् = neither atiyoga nor ayoga."),
            [("Both excess and lack", "Each is denied with न."),
             ("Excess, but not lack", "Atiyoga is denied too."),
             ("Lack, but not excess", "Ayoga is denied too.")],
            "Two negatives: न अतियोगम्, न च अयोगम्.",
            "न … न च … = neither … nor."),
        mcq("transfer", 5,
            "कुर्वन्त्यतिवृषम् joins कुर्वन्ति + अतिवृषम्. Join an invented भवन्ति + अत्र (they are here) the same way. Which is right?",
            ("भवन्त्यत्र", "इ before an unlike vowel becomes य्."),
            [("भवन्तीत्र", "ई would need इ + इ; the next vowel is अ."),
             ("भवन्तेत्र", "ए comes from अ + इ, not from इ + अ."),
             ("भवन्तियत्र", "The इ itself becomes य्; no य् is added after it.")],
            "Same rule as कुर्वन्ति + अतिवृषम् = कुर्वन्त्यतिवृषम्.",
            "इ + unlike vowel → य्.",
            teaches="इ/ई before an unlike vowel becomes य्: कुर्वन्ति + अति → कुर्वन्त्यति; भवन्ति + अत्र → भवन्त्यत्र."),
    ],
}


NOTES_HI = {
    "12": ("विश्वास: मध्यम। पंक्ति 05.05.22 पिछली पंक्ति 05.05.21 का वाक्य पूरा करती है (‘पूजितः’)। ‘बस्त्याटोप’ में बस्ति = मूत्राशय-प्रदेश; आटोप = गुड़गुड़ाहट वाला फुलाव (सम्भावित)। "
           "text_flags: छपा ‘मुस्तपाठामृ तैरंड…’ में स्थान ‘अमृत + एरण्ड’ (अमृतैरण्ड) के बीच पड़ा है, दोनों टुकड़े एक शब्द हैं; इस पर प्रश्न नहीं बना। "
           "पहचान: मुस्त = नागरमोथा, अमृता = गिलोय, पुनर्नवा = गदहपूर्णा (मानक); बला = बरियार (सम्भावित)। "
           "संधि जाँची: शुक्रानिल = शुक्र + अनिल; बस्त्याटोप = बस्ति + आटोप (इ → य्); अमृतैरण्ड = अमृत + एरण्ड (अ + ए → ऐ)।"),
    "13": ("विश्वास: निम्न। पंक्ति 05.05.24 के अन्त का ‘अक्ष + रोहिणी’ विभाजन अनुमानित है; अन्त एक शब्द भी हो सकता है। छपा अवग्रह ‘मंजिष्ठाऽरग्वधो’ छपाई की विचित्रता है (मञ्जिष्ठा + आरग्वध = आ)। "
           "पहचान: मञ्जिष्ठा = मंजीठ, आरग्वध = अमलतास, उशीर = खस (मानक); त्रायमाणा, रोहिणी विवादित; अक्ष = बहेड़ा, मदन = मैनफल (सम्भावित)। "
           "‘पालिकम्’ केवल पंचमूल पर लागू है या सब पर, तय नहीं। कनीयः पंचमूल के सदस्य पाठ में नहीं हैं (मानक तालिकाएँ: शालपर्णी, पृश्निपर्णी, बृहती, कण्टकारी, गोक्षुर)। "
           "संधि जाँची: आरग्वधोशीर = आरग्वध + उशीर (अ + उ → ओ); मदनाष्टकम् = मदन + अष्टकम्।"),
    "14": ("विश्वास: उच्च। ‘तत्’ पंक्तियों 05.05.23-25 की द्रव्य-सूची को दर्शाता है। ‘परिस्रुतम्’ (शाब्दिक: बहा हुआ) = छाना हुआ। ‘क्षीरशेषम्’ = जब तक केवल दूध बचे (जल उड़ जाए)। "
           "आढक और प्रस्थ आयतन के मान हैं; ग्राम में नहीं बदले। पाठभेद या flag नहीं। "
           "संधि जाँची: जलाढके = जल + आढके; पचेत्तच्च = पचेत् + तत् + च (त् + च → च्च); पादशेषं, क्षीरशेषं में अन्त का ं = म्।"),
    "15": ("विश्वास: निम्न। ‘सपाद’ = सवा; किस मान का, नहीं कहा। ‘जाङ्गल’ = सूखे प्रदेश के प्राणियों का; पंक्ति ‘मांस’ नहीं कहती। "
           "text_flags (05.05.29): ‘कर’ किसी द्रव्य का नाम नहीं; ‘करञ्ज’ केवल अनुमान है। खुला अवलोकन: छपी पंक्ति ठीक १६ अक्षर की है, ‘करञ्ज’ से १७ हो जाते, जो इसके विरुद्ध है; इसलिए पंक्ति २ की सूची पर प्रश्न नहीं बना। "
           "पहचान: यष्टी = मुलेठी (मानक), मिशि = सोया (विवादित), श्यामा विवादित, कलिङ्ग = इन्द्रयव/कुटज-बीज (सम्भावित)। "
           "संधि जाँची: ससर्पिर्मधु = स + सर्पिः + मधु (इः → इर्); पिष्टैर्यष्टी = पिष्टैः + यष्टी (ऐः → ऐर्)।"),
    "16": ("विश्वास: मध्यम। छपा ‘विवर्द्धनः’ = विवर्धनः (दोहरा द्ध सामान्यीकृत)। कोई क्रिया नहीं; ‘है’ जोड़ा गया। "
           "text_flags: छपा ‘नेह’ सम्भवतः ‘मेह’ (म/न की भूल); अनुवादों में ‘मेह’ लिया गया है, इसलिए इस पर प्रश्न नहीं बना। "
           "पंक्ति 05.05.31 की सूची 05.05.34 के ‘हन्यात्’ का कर्म है। पहचान: वातास्र = वातरक्त/गठिया (सम्भावित), मेदस् = मोटापा (सम्भावित), अर्श = बवासीर (मानक)। "
           "संधि जाँची: सुखोष्णो = सुख + उष्णः, फिर अः → ओ (म से पहले); मेदोऽर्शो = मेदः + अर्शः (अः + अ → ओऽ)।"),
    "17": ("विश्वास: निम्न। दो text_flags: छपा ‘वीसर्ष’ सम्भवतः ‘वीसर्प’ और अन्त का ‘ध्म’ अस्पष्ट; खुला अवलोकन: ‘ध्मान’ से पंक्ति १७ अक्षर की होती और अगला ‘आध्मान’ दोहराता, इसलिए यह अनुमान कमज़ोर है। "
           "छपा ‘मन्द्या’ सम्भवतः ‘मन्या’ (गर्दन का पिछला भाग)। इन तीनों पर प्रश्न नहीं बना। "
           "‘रुजः’ समास के सब सदस्यों पर लागू है। पहचान: विषमज्वर, विसर्प, प्रवाहिका (सम्भावित)। "
           "संधि जाँची: वङ्क्षणोरु = वङ्क्षण + ऊरु (अ + ऊ → ओ); शिरोरुजः = शिरः + रुजः (अः → ओ)।"),
    "18": ("विश्वास: निम्न। ‘हन्यात्’ पंक्तियों 05.05.31-33 की सूची का क्रियापद है; कर्ता 05.05.30 की बस्ति। "
           "text_flags: ‘अश्मकुण्डलान्’ कोई रोग-नाम नहीं (शायद अश्मरी का दूषित रूप); अविभक्त और अव्याख्यात रखा गया, इस पर प्रश्न नहीं बना। "
           "पहचान: असृग्दर = असामान्य गर्भाशय रक्तस्राव (सम्भावित)। पंक्ति 05.05.35 में क्रिया नहीं, केवल विशेषण। "
           "संधि जाँची: हन्यादसृग्दर = हन्यात् + असृग्दर (त् → द् स्वर से पहले); असृग्दरोन्माद = असृग्दर + उन्माद (अ + उ → ओ); पुत्रदो राजा = पुत्रदः + राजा।"),
    "19": ("विश्वास: मध्यम। ‘पृथक्पलांशम्’ = अलग-अलग, पल के अंशों में; डेटा का ‘प्रत्येक’ शब्द पाठ में नहीं है। "
           "खुला अवलोकन (05.05.36): गोक्षुर छोटे पंचमूल में है, बड़े में नहीं; इसलिए ‘गोक्षुर-रहित पंचमूल’ या तो व्यर्थ है या चार जड़ें छोड़ता है; सम्भव दूषित पाठ। इस पर प्रश्न नहीं बना। "
           "पंक्ति 05.05.37 अधूरी है: ‘चार प्रस्थ’ किसका, नहीं कहा; ‘यष्ट्यादि’ समूह नहीं गिनाया। "
           "संधि जाँची: विपचेत्पंचमूलमगोक्षुरं = विपचेत् + पञ्चमूलम् + अगोक्षुरम्; पिष्टैर्यष्ट्यादिभिर्युतं = पिष्टैः + यष्टि-आदिभिः + युतम्।"),
    "20": ("विश्वास: उच्च। text_flags: ‘…युक्तं’ नपुंसक है पर ‘बस्तिः’ पुंलिंग; सम्भवतः ‘युक्तो’ (05.05.21 के ‘युक्तो बस्तिः’ जैसा)। छपा ‘सु पूजितः’ = सुपूजितः। इन पर प्रश्न नहीं बना। "
           "छपा ‘वाल’ = बाल (व/ब सामान्यीकरण)। षष्ठी बहुवचन ‘के लिए’ अनुवादित। सिन्धूत्थ = सेंधा नमक (मानक)। "
           "संधि जाँची: क्षौद्रतैलाज्य = क्षौद्र + तैल + आज्य (अ + आ → आ); विशेषाद्वाल = विशेषात् + बाल (त् → द्); सुखात्मनां = सुख + आत्मनाम्।"),
    "21": ("विश्वास: मध्यम। पंक्ति 05.05.40 में तैयार होने वाली वस्तु का नाम नहीं; अनुवाद में कुछ जोड़ा नहीं गया। text_flags: छपा ‘साहचर’ = सहाचर (05.05.70 जैसा)। "
           "‘तथा ऽभीरु’ में अवग्रह से पहले छपा स्थान छपाई की भूल है। पहचान: बला = बरियार, सारिवा = अनन्तमूल, गुडूची = गिलोय (मानक); सहाचर = कटसरैया, दर्भ = कुश, अभीरु = शतावरी, बृहती-द्वय = बृहती और कण्टकारी (सम्भावित)। "
           "संधि जाँची: तद्वत्साहचर = तद्वत् + सहाचर; क्षीरबस्तिस्तथा = क्षीरबस्तिः + तथा (ः → स्); तथाऽभीरु = तथा + अभीरु (आ + अ → आ)। वाक्य 05.05.42 में चलता है।"),
    "22": ("विश्वास: मध्यम। ‘कल्कवत्’ = कल्क वाला; ‘कल्क की तरह’ भी सम्भव। पंक्ति 05.05.41-42 एक वाक्य हो सकती हैं (दावा नहीं)। "
           "‘बृहत्यादि पंचमूल’ सम्भवतः छोटा पंचमूल; पाठ सदस्य नहीं गिनाता। ‘प्रतिद्रव्यम्’ और ‘पलोन्मितम्’ का व्याकरणिक सम्बन्ध निश्चित नहीं। "
           "पहचान: मागधिका = पीपर, यष्टीमधुक = मुलेठी (मानक)। "
           "संधि जाँची: पयो मागधिका = पयः + मागधिका (अः → ओ); बृहत्यादि = बृहती + आदि (ई → य्); पलोन्मितं = पल + उन्मितम् (अ + उ → ओ)।"),
    "23": ("विश्वास: मध्यम। ‘द्विपलम्’ प्रत्येक अन्न पर या सब पर, पाठ तय नहीं करता। कोई क्रिया नहीं। "
           "text_flags: छपा ‘कुकुट’ = कुक्कुट (वर्तनी-भेद, अर्थ वही); मुर्गा या मुर्गी, नहीं कहा; इस पर प्रश्न नहीं बना। ‘तैः’ पंक्तियों 05.05.43-44 के द्रव्यों और अन्नों को दर्शाता है। "
           "पहचान: शालि = अगहनी चावल, गोधूम = गेहूँ, यव, माष = उड़द, सिता = मिश्री (मानक); यष्टिका = मुलेठी (सम्भावित)। "
           "संधि जाँची: गोधूमयवमाषं = गोधूम + यव + माषम्; तैः सिद्धं में विसर्ग स से पहले बना रहता है।"),
    "24": ("विश्वास: मध्यम। ‘द्विलवण’ के दो लवण पाठ में नहीं; खुला अवलोकन: सूचियों में प्रायः सैन्धव और एक अन्य, पर पाठ नहीं कहता; पहचान नहीं की गई। "
           "‘परम्’ = अत्यन्त (क्रियाविशेषण) या ‘श्रेष्ठ’। text_flags: छपा ‘शिखिगो नर्द’ एक नाम (शिखि-गोनर्द) है; गोनर्द अज्ञात प्राणी। इन पर प्रश्न नहीं बना। "
           "संधि जाँची: …लवणैस्तैर्बस्तिः = …लवणैः + तैः + बस्तिः (ः → स् त से पहले; ः → र् ब से पहले); कल्पो ऽयं = कल्पः + अयम्; रसेष्वपि = रसेषु + अपि (उ → व्)।"),
    "25": ("विश्वास: उच्च। कुलीर = केकड़ा, चटक = गौरैया, शर्करा = शक्कर (मानक; ग्लॉसरी में एक जगह कुलीर ‘सम्भवतः केकड़ा’)। कोई क्रिया नहीं पंक्ति 05.05.48 में। "
           "‘अण्ड’ एकवचन है, पर एक अण्डा या अण्डे सामान्य, दोनों सम्भव। छपा ‘मधु र्बस्तिर्’ में स्थान ‘मधुः बस्तिः’ के बीच की छपाई-भूल है; इस पर प्रश्न नहीं बना। "
           "संधि जाँची: चटकाण्डरसान्वितः = चटक + अण्ड + रस + अन्वितः (अ + अ → आ); बस्तिर्वृषतमो = बस्तिः + वृषतमः (इः → इर्; अः → ओ)।"),
    "26": ("विश्वास: मध्यम। text_flags: छपा ‘मूकर’ कोई शब्द नहीं; ‘सूकर’ (सूअर) केवल अनुमान है। डेटा के अनुवाद इस अनुमान को बिना चिह्न के लेते हैं; यहाँ कार्ड पर ‘अनुमानित पाठ पर’ कहा गया, और इस पर प्रश्न नहीं बना। "
           "पंक्ति 05.05.51 में ‘बस्तमुष्कम्’ और ‘इक्षुरकम्’ का कारक छपाई से स्पष्ट नहीं। पहचान: मुष्क = अण्डकोश (मानक), इक्षुरक = तालमखाना/कोकिलाक्ष (सम्भावित), उच्चटा अज्ञात। "
           "संधि जाँची: …जैर्मुष्कैः = …जैः + मुष्कैः; पयो बस्त… = पयः + बस्त…; उच्चटेक्षुरकं = उच्चटा + इक्षुरकम् (आ + इ → ए)।"),
    "27": ("विश्वास: निम्न। text_flags और खुला अवलोकन (05.05.52): छपा ‘निर्घृताढ्यो’ का शाब्दिक अर्थ ‘बिना-घी से भरपूर’ विरोधी है; ‘घृताढ्य’ अनुमान है, स्कैन से जाँच बाकी। इस पर प्रश्न नहीं बना। "
           "पंक्ति 05.05.53 में भोजन की क्रिया नहीं छपी। पहचान: आत्मगुप्ता = केवाँच (मानक), इक्षुर = तालमखाना (सम्भावित), उच्चटा अज्ञात। "
           "संधि जाँची: …ढ्योऽल्प = …ढ्यः + अल्प (अः + अ → ओऽ); बस्तिर्वृषतमः = बस्तिः + वृषतमः; भोज्यमात्मगुप्तो… = भोज्यम् + आत्मगुप्ता + उच्चटा (आ + उ → ओ) + इक्षुरैः (आ + इ → ए)।"),
    "28": ("विश्वास: निम्न। text_flags: ‘सदृषो’ कोई शब्द नहीं; सदृशः, स-दृढः, स-हृष्टः सम्भव, कोई निश्चित नहीं; अविभक्त छोड़ा गया, इस पर प्रश्न नहीं बना। "
           "‘दशदशाहेन’ = दस-दस दिन से; दस दिन का क्रम या हर दस दिन, संस्कृत तय नहीं करती। ‘गच्छति’ शाब्दिक ‘जाता है’। "
           "संधि जाँची: अतो दश = अतः + दश (अः → ओ); यस्तु = यः + तु (ः → स्); बस्तीन्निषेवते = बस्तीन् + निषेवते; वाजीव = वाजी + इव (ई + इ → ई)।"),
    "29": ("विश्वास: निम्न। खुला अवलोकन (05.05.57): ‘स्तम्भिनः’ का अर्थ और ‘ते’ (वे) कौन, तय नहीं; ‘च … च’ दो वाक्य जोड़ते हैं या नहीं, यह भी खुला है। इस पर प्रश्न नहीं बना। "
           "‘माक्षिक’ यहाँ मधु है (अन्यत्र यही शब्द एक खनिज का नाम है, यहाँ नहीं)। ‘एते’ = अभी बताई गई तैयारियाँ। "
           "संधि जाँची: कुर्वन्त्यतिवृषं = कुर्वन्ति + अतिवृषम् (इ → य्); नातियोगं = न + अतियोगम्; चायोगं = च + अयोगम्; स्तंभिनस्ते = स्तम्भिनः + ते (ः → स्)।"),
}

AIDS = {
    "12": {
        "diagram": {"groups": [{"label": "प्रशंसित किसमें", "items": ["शुक्र-अनिल की रुकावट", "बस्ति-प्रदेश का आटोप"]},
                               {"label": "नई द्रव्य-सूची", "items": ["मुस्त", "पाठा", "अमृता", "एरण्ड", "बला", "रास्ना", "पुनर्नवा"]}]},
        "chunks": "शुक्रानिलविबंधेषु | बस्त्याटोपेषु पूजितः ‖ मुस्तपाठामृ तैरंड- | बलारास्नापुनर्नवं।",
        "sandhi": "अ + अ → आ: शुक्र + अनिल → शुक्रानिल; इ + आ → या: बस्ति + आटोप → बस्त्याटोप; अ + ए → ऐ: अमृत + एरण्ड → अमृतैरण्ड।",
        "anchors": "अनिल = वायु · विबन्ध = रुकावट · आटोप = गुड़गुड़ाहट वाला फुलाव · पूजित = प्रशंसित · मुस्त = नागरमोथा · अमृता = गिलोय।",
    },
    "13": {
        "frame": "क्या: द्रव्य-सूची आगे · पंक्ति १: मञ्जिष्ठा, आरग्वध, उशीर, त्रायमाणा, (अनुमानित: अक्ष, रोहिणी) · पंक्ति २: छोटा पंचमूल, पालिक, आठ मदन।",
        "chunks": "मंजिष्ठाऽरग्वधोशीर- | त्रायमाणाक्षरोहिणी ‖ कनीयः पंचमूलं च | पालिकं मदनाष्टकं।",
        "anchors": "मञ्जिष्ठा = मंजीठ · आरग्वध = अमलतास · उशीर = खस · कनीयः = छोटा · पालिक = पल भर का · अष्टक = आठ का समूह।",
    },
    "14": {
        "chain": {"steps": ["आढक भर जल में पकाए", "चौथाई शेष रहे", "छान ले (परिस्रुत)",
                            "दो प्रस्थ दूध मिलाए", "फिर पकाए, दूध शेष रहे"]},
        "sandhi": "त् + च → च्च: पचेत् + तत् + च → पचेत्तच्च।",
        "contrast": "श्लोक १४ ↔ १९: १४ में पहले जल का आढक, फिर दो प्रस्थ दूध; १९ में सीधे दूध का आढक।",
        "anchors": "आढक, प्रस्थ = आयतन के मान · पाद = चौथाई · शेष = बचा हुआ · परिस्रुत = छाना हुआ · पुनः = फिर।",
    },
    "15": {
        "frame": "पंक्ति १: सवा जाङ्गल-रस + घी, मधु, सैन्धव · पंक्ति २ (पाठ अनिश्चित): पिसे यष्टी, मिशि, श्यामा, कलिङ्ग, ‘कर’ (अस्पष्ट), अञ्जन।",
        "sandhi": "इः → इर् सघोष से पहले: सर्पिः + मधु → सर्पिर्मधु; ऐः → ऐर्: पिष्टैः + यष्टी → पिष्टैर्यष्टी।",
        "anchors": "सपाद = सवा · जाङ्गल = सूखे प्रदेश का · रस = रस, द्रव · सर्पिस् = घी · स- = सहित · पिष्ट = पिसा हुआ।",
    },
    "16": {
        "diagram": {"groups": [{"label": "बस्ति", "items": ["सुखोष्ण"]},
                               {"label": "बढ़ाती है", "items": ["मांस", "अग्नि", "बल", "शुक्र"]},
                               {"label": "नष्ट करे (श्लोक १८ की क्रिया)", "items": ["वातास्र", "मेह (छपा नेह)", "मेदस्", "अर्श", "गुल्म", "मल-मूत्र का रुकना"]}]},
        "chunks": "बस्तिः सुखोष्णो | मांसाग्निबलशुक्रविवर्द्धनः ‖ वातासृग्नेहमेदोऽर्शो- | गुल्मविण्मूत्रसंग्रहं।",
        "sandhi": "अ + उ → ओ: सुख + उष्ण → सुखोष्ण; अः + अ → ओऽ: मेदः + अर्शः → मेदोऽर्शः।",
        "anchors": "सुखोष्ण = सुहाता गर्म · अग्नि = पाचक अग्नि · विवर्धन = बढ़ाने वाला · संग्रह = रुकना।",
    },
    "17": {
        "frame": "पंक्ति १ के रोग: विषमज्वर, विसर्प (अनुमानित), एक अस्पष्ट शब्द, आध्मान, प्रवाहिका · पंक्ति २ की पीड़ा (रुजः): वंक्षण, ऊरु, कटी, कुक्षि, मन्या (अनुमानित), श्रोत्र, शिर।",
        "sandhi": "अ + ऊ → ओ: वङ्क्षण + ऊरु → वङ्क्षणोरु; अः → ओ: शिरः + रुजः → शिरोरुजः।",
        "pegs": "मेरा बनाया चित्र (श्लोक का दावा नहीं): पीड़ा नीचे से ऊपर चढ़ती सोचें: जाँघ-जोड़, जाँघ, कमर, बगल, गर्दन, कान, सिर।",
        "anchors": "विषम = अनियमित · आध्मान = अफारा · प्रवाहिका = मरोड़ वाले दस्त · वङ्क्षण = जाँघ का जोड़ · कुक्षि = पेट का बगल · रुज् = पीड़ा।",
    },
    "18": {
        "diagram": {"groups": [{"label": "हन्यात्: नष्ट करे", "items": ["असृग्दर", "उन्माद", "शोफ", "कास", "(अस्पष्ट शब्द)"]},
                               {"label": "बस्ति के विशेषण", "items": ["चक्षुष्य", "पुत्रद", "यापनों का राजा", "रसायन"]}]},
        "chunks": "हन्यादसृग्दरोन्माद- | शोफकासाश्मकुंडलान् ‖ चक्षुष्यः पुत्रदो राजा | यापनानां रसायनं।",
        "anchors": "हन्यात् = नष्ट करे · असृग्दर = असामान्य मासिक रक्तस्राव · शोफ = सूजन · कास = खाँसी · पुत्रद = पुत्र देने वाला · रसायन = कायाकल्प करने वाला।",
    },
    "19": {
        "chain": {"steps": ["पंचमूल (गोक्षुर के बिना)", "अलग-अलग पल के अंश", "आढक भर दूध में पकाए",
                            "चार प्रस्थ (किसका, नहीं कहा)", "पिसे यष्टि आदि से युक्त"]},
        "sandhi": "इ + आ → या: यष्टि + आदिभिः → यष्ट्यादिभिः; ऐः → ऐर्: पिष्टैः + यष्टि → पिष्टैर्यष्टि।",
        "anchors": "पृथक् = अलग · अंश = भाग · विपचेत् = पकाए · अ- = बिना · चतुः = चार · युत = युक्त।",
    },
    "20": {
        "diagram": {"groups": [{"label": "बस्ति में", "items": ["शहद", "तैल", "घी", "सेंधा नमक"]},
                               {"label": "विशेष रूप से किसके लिए", "items": ["बाल", "वृद्ध", "स्त्री", "सुकुमार", "सुखी स्वभाव वाले"]}]},
        "chunks": "क्षौद्रतैलाज्यसिंधूत्थ- | युक्तं बस्तिः सु पूजितः ‖ विशेषाद्वालवृद्धस्त्री- | सुकुमारसुखात्मनां।",
        "sandhi": "अ + आ → आ: सुख + आत्मनाम् → सुखात्मनाम्; त् → द् सघोष से पहले: विशेषात् + बाल → विशेषाद्बाल।",
        "anchors": "सिन्धूत्थ = सिन्ध से उत्पन्न, सेंधा नमक · विशेषात् = विशेष रूप से · सुकुमार = कोमल · -नाम् = के लिए।",
    },
    "21": {
        "diagram": {"groups": [{"label": "तद्वत् साधित", "items": ["सहाचर", "बला", "सारिवा", "दर्भ"]},
                               {"label": "क्षीरबस्ति", "items": ["अभीरु", "गुडूची", "बृहती-द्वय"]}]},
        "sandhi": "ः → स् त से पहले: क्षीरबस्तिः + तथा → क्षीरबस्तिस्तथा; आ + अ → आ (ऽ): तथा + अभीरु → तथाऽभीरु।",
        "anchors": "तद्वत् = उसी प्रकार · साधित = तैयार किया हुआ · गुडूची = गिलोय · सारिवा = अनन्तमूल · द्वय = जोड़ा।",
    },
    "22": {
        "diagram": {"groups": [{"label": "पंक्ति १", "items": ["सिद्ध दूध", "पीपर का कल्क", "मुलेठी का कल्क"]},
                               {"label": "पंक्ति २", "items": ["बृहती आदि पंचमूल", "प्रत्येक द्रव्य पल भर"]}]},
        "chunks": "सिद्धं पयो मागधिका- | यष्टीमधुककल्कवत् ‖ पंचमूलं बृहत्यादि- | प्रतिद्रव्यं पलोन्मितं।",
        "sandhi": "अ + उ → ओ: पल + उन्मितम् → पलोन्मितम्; ई + आ → या: बृहती + आदि → बृहत्यादि।",
        "anchors": "मागधिका = पीपर · यष्टीमधुक = मुलेठी · कल्क = लुगदी · प्रति- = प्रत्येक · उन्मित = मापा हुआ।",
    },
    "23": {
        "diagram": {"groups": [{"label": "दो पल", "items": ["शालि", "गोधूम", "यव", "माष", "यष्टिका सहित"]},
                               {"label": "पंक्ति २", "items": ["उनसे पका बकरी का दूध", "कुक्कुट-अण्डे का रस", "सिता"]}]},
        "chunks": "द्विपलं शालि गोधूम- | यवमाषं सयष्टिकं ‖ तैः सिद्धं छागलं क्षीरं | कुकुटांडरसः सिता।",
        "anchors": "शालि = अगहनी चावल · गोधूम = गेहूँ · माष = उड़द · छागल = बकरी का · सिता = मिश्री · तैः = उनसे।",
    },
    "24": {
        "frame": "साथ: घी, शहद, दो लवण · उनसे बनी बस्ति: अत्यन्त शुक्रकृत् · यही कल्प: मोर, गोनर्द, मछली आदि के अण्डा-रसों में भी।",
        "chunks": "साज्यक्षौद्रद्विलवणैस् | तैर्बस्तिः शुक्रकृत्परं ‖ कल्पो ऽयं शिखिगो नर्द | मत्स्याद्यंडरसेष्वपि।",
        "sandhi": "अः + अ → ओऽ: कल्पः + अयम् → कल्पोऽयम्; उ + अ → व: रसेषु + अपि → रसेष्वपि।",
        "anchors": "आज्य = घी · द्वि = दो · -कृत् = करने वाला · कल्प = विधि · शिखी = मोर · अपि = भी।",
    },
    "25": {
        "diagram": {"groups": [{"label": "रस", "items": ["केकड़े के मांस का रस", "गौरैया-अण्डे का रस"]},
                               {"label": "साथ", "items": ["शर्करा", "घी", "मधु"]},
                               {"label": "फल", "items": ["वृषतम बस्ति"]}]},
        "chunks": "रसः कुलीरमांसस्य | चटकांडरसान्वितः ‖ सशर्कराघृतमधु | र्बस्तिर्वृषतमो मतः।",
        "contrast": "श्लोक २५ ↔ २७: दोनों बस्तियाँ ‘वृषतम’ कही गईं; २५ में केकड़ा-रस और गौरैया-अण्डा, २७ में (अनुमानित) घी भरपूर, नमक कम।",
        "anchors": "कुलीर = केकड़ा · चटक = गौरैया · अन्वित = युक्त · -तम = सबसे अधिक · मत = माना गया।",
    },
    "26": {
        "frame": "पंक्ति १ (तृतीया): बकरे और (अनुमानित) सूअर के मुष्क, केकड़ा और गौरैया का मांस · पंक्ति २: सिद्ध दूध + बकरे का मुष्क, उच्चटा, इक्षुरक, मधु।",
        "sandhi": "आ + इ → ए: उच्चटा + इक्षुरकम् → उच्चटेक्षुरकम्; अः → ओ: पयः + बस्त → पयो बस्त।",
        "anchors": "बस्त = बकरा · मुष्क = अण्डकोश · आमिष = मांस · इक्षुरक = सम्भवतः तालमखाना · पयस् = दूध।",
    },
    "27": {
        "frame": "पंक्ति १ (अनुमानित पाठ पर): घी भरपूर, अल्प लवण बस्ति = वृषतम, पर · पंक्ति २: भोजन, सिद्ध दूध से, जो केवाँच, उच्चटा, इक्षुर से पका हो।",
        "sandhi": "इः → इर्: बस्तिः + वृषतमः → बस्तिर्वृषतमः; आ + उ → ओ: आत्मगुप्ता + उच्चटा → आत्मगुप्तोच्चटा।",
        "anchors": "आढ्य = भरपूर · अल्प = थोड़ा · पर = उत्तम · भोज्य = भोजन · आत्मगुप्ता = केवाँच।",
    },
    "28": {
        "chain": {"steps": ["दस-दस दिन के क्रम से", "बस्तियों का सेवन करे", "घोड़े की तरह पुष्ट",
                            "सौ स्त्रियों के पास जाता है"]},
        "chunks": "अतो दशदशाहेन | यस्तु बस्तीन्निषेवते ‖ वाजीव पुष्टः सदृषो (अस्पष्ट) | गच्छति प्रमदाशतं।",
        "sandhi": "ई + इ → ई: वाजी + इव → वाजीव; ः → स् त से पहले: यः + तु → यस्तु।",
        "anchors": "अहन् = दिन · निषेवते = सेवन करता है · वाजी = घोड़ा · इव = की तरह · प्रमदा = स्त्री · शत = सौ।",
    },
    "29": {
        "seesaw": "अतियोग (अधिक क्रिया) ↔ अयोग (कम क्रिया): श्लोक कहता है कि ये तैयारियाँ दोनों में से कोई नहीं करतीं।",
        "chunks": "एते माक्षिकसंयुक्ताः | कुर्वन्त्यतिवृषं नरं ‖ नातियोगं न चायोगं | स्तंभिनस्ते च कुर्वते।",
        "sandhi": "इ + अ → य: कुर्वन्ति + अतिवृषम् → कुर्वन्त्यतिवृषम्; अ + अ → आ: न + अतियोगम् → नातियोगम्, च + अयोगम् → चायोगम्।",
        "anchors": "माक्षिक = शहद · संयुक्त = मिला हुआ · अतिवृष = अत्यन्त पौरुषयुक्त · अति- = अधिक · अ- = अभाव।",
    },
}

IMAGE_SPECS = {
    ("12", "diagram"): {
        "file": "ka5-mustadi-dravya-12.svg",
        "alt": "Mind map of verse 12: esteemed in obstructions of semen and wind and in bladder-region distension; new drug list of seven: musta, patha, amrita, castor, bala, rasna, punarnava",
        "type": "mermaid",
        "code": ('mindmap\n  श्लोक बारह\n    प्रशंसित\n      शुक्र-वायु की रुकावट\n      बस्ति-प्रदेश का आटोप\n'
                 '    नई द्रव्य-सूची\n      मुस्त\n      पाठा\n      अमृता\n      एरण्ड\n      बला\n      रास्ना\n      पुनर्नवा\n'),
    },
    ("14", "chain"): {
        "file": "ka5-jala-kshira-paka-14.svg",
        "alt": "Flowchart of five steps: cook in an adhaka of water, until a quarter remains, strain, add two prasthas of milk, cook again until the milk remains",
        "type": "mermaid",
        "code": ('flowchart TD\n  A["आढक भर जल में पकाए"] --> B["चौथाई शेष रहे"]\n  B --> C["छान ले"]\n'
                 '  C --> D["दो प्रस्थ दूध मिलाए"]\n  D --> E["फिर पकाए, दूध शेष रहे"]\n'),
    },
    ("16", "diagram"): {
        "file": "ka5-sukhoshna-basti-16.svg",
        "alt": "Mind map of verse 16: the comfortably warm enema increases four things: flesh, digestive fire, strength, semen",
        "type": "mermaid",
        "code": ('mindmap\n  सुखोष्ण बस्ति\n    बढ़ाती है\n      मांस\n      अग्नि\n      बल\n      शुक्र\n'),
    },
    ("18", "diagram"): {
        "file": "ka5-yapana-raja-18.svg",
        "alt": "Mind map of verse 18: destroys abnormal menstrual bleeding, insanity, swelling, cough and an unclear item; four titles: good for the eyes, giver of sons, king of the yapanas, rasayana",
        "type": "mermaid",
        "code": ('mindmap\n  श्लोक अठारह\n    नष्ट करे\n      असृग्दर\n      उन्माद\n      शोफ\n      कास\n      एक अस्पष्ट शब्द\n'
                 '    विशेषण\n      आँखों का हित\n      पुत्र देने वाली\n      यापनों का राजा\n      रसायन\n'),
    },
    ("19", "chain"): {
        "file": "ka5-kshira-panchamula-19.svg",
        "alt": "Chain of five items of verse 19: five roots without gokshura, separately in pala portions, cooked in an adhaka of milk, four prasthas (of what not stated), with ground licorice group",
        "type": "chain",
        "title": "श्लोक १९: दूध में पंचमूल",
        "steps": ["पंचमूल, गोक्षुर के बिना", "अलग-अलग पल के अंश", "आढक भर दूध में पकाए",
                  "चार प्रस्थ (किसका, नहीं कहा)", "पिसे यष्टि आदि से युक्त"],
    },
    ("20", "diagram"): {
        "file": "ka5-bala-vriddha-20.svg",
        "alt": "Mind map of verse 20: enema with honey, oil, ghee and rock salt; especially for five groups: children, the old, women, the delicate, the comfort-natured",
        "type": "mermaid",
        "code": ('mindmap\n  सुपूजित बस्ति\n    युक्त\n      शहद\n      तैल\n      घी\n      सेंधा नमक\n'
                 '    विशेषकर किसके लिए\n      बालक\n      वृद्ध\n      स्त्री\n      सुकुमार\n      सुखी स्वभाव\n'),
    },
    ("22", "diagram"): {
        "file": "ka5-kalka-payas-22.svg",
        "alt": "Table of verse 22: milk cooked with a paste of long pepper and licorice; five roots headed by brihati, each drug a pala",
        "type": "table",
        "title": "श्लोक २२: दूध और पंचमूल",
        "heads": ["क्या", "किसके साथ / कितना"],
        "rows": [["सिद्ध दूध", "पीपर और मुलेठी का कल्क"], ["बृहती आदि पंचमूल", "प्रत्येक द्रव्य पल भर"]],
    },
    ("23", "diagram"): {
        "file": "ka5-anna-chagala-23.svg",
        "alt": "Table of verse 23: two palas of shali rice, wheat, barley and black gram with yashtika; goat's milk cooked with those; fowl's egg fluid; crystallised sugar",
        "type": "table",
        "title": "श्लोक २३: अन्न और बकरी का दूध",
        "heads": ["पंक्ति", "द्रव्य"],
        "rows": [["पंक्ति १ (दो पल)", "शालि, गेहूँ, यव, उड़द, यष्टिका सहित"],
                 ["पंक्ति २", "उनसे पका बकरी का दूध"], ["पंक्ति २", "कुक्कुट-अण्डे का रस, सिता"]],
    },
    ("25", "diagram"): {
        "file": "ka5-kulira-vrishatama-25.svg",
        "alt": "Flowchart of verse 25: crab-flesh juice with sparrow-egg fluid, plus sugar, ghee and honey, gives the enema considered most aphrodisiac",
        "type": "mermaid",
        "code": ('flowchart TD\n  A["केकड़े के मांस का रस"] --> C["बस्ति"]\n  B["गौरैया-अण्डे का रस"] --> C\n'
                 '  D["शर्करा, घी, मधु"] --> C\n  C --> E["वृषतम मानी गई"]\n'),
    },
    ("29", "seesaw"): {
        "file": "ka5-atiyoga-ayoga-29.svg",
        "alt": "Split picture of verse 29: excess (atiyoga) on one side and lack (ayoga) on the other; the verse says these preparations bring about neither",
        "type": "split",
        "title": "श्लोक २९: न अतियोग, न अयोग",
        "cols": [["अतियोग", ["अधिक क्रिया", "नहीं होता"]], ["अयोग", ["कम क्रिया", "नहीं होता"]]],
    },
}
