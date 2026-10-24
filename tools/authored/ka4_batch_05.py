from helpers import mcq, match, order, fill, multi, accepts

# Kalpasthāna chapter 4 (Bastikalpa), units 52-58 (study-text lines 05.04.100-108), the last batch of the chapter.
# Section (sections_kalpa.py KA4): 52-58 rules for applying bastis, and the colophon.
# Cross-references name study-text line ids (05.04.L), not quiz unit numbers.

AUTHORED = {}

# ---------------------------------------------------------------- unit 52
AUTHORED["52"] = {
    "title": "बलकालदेशसात्म्यप्रकृतीः",
    "question": "What must be distinguished before a basti is applied, according to unit 52?",
    "rule": ("A basti is applied after distinguishing five things: strength (bala), time or season (kāla), region (deśa), "
             "sātmya (what suits by habit) and constitutions (prakṛti). The sentence continues in line 05.04.101."),
    "limits": ("No verb in this unit: what the basti then does (nivartayati) is in line 05.04.101. Kāla may be time or season; "
               "both fit. The unit does not say how each factor changes the basti."),
    "explain_hi": ("यह इकाई बस्ति-प्रयोग का नियम खोलती है: बल, काल, देश, सात्म्य और प्रकृतियों को भली-भाँति अलग-अलग पहचानकर प्रयुक्त की गई बस्ति। "
                   "सात्म्य = जो आदत से अनुकूल पड़ता है; काल = समय या ऋतु, दोनों अर्थ बैठते हैं। "
                   "‘प्रविभज्य’ = अलग-अलग करके, भेद पहचानकर (उपसर्ग वाला पूर्वकालिक रूप)। "
                   "वाक्य यहाँ पूरा नहीं होता: ऐसी बस्ति क्या करती है, यह अगली पंक्ति ०५.०४.१०१ में है। "
                   "हर कारक बस्ति को कैसे बदलता है, यह इकाई नहीं बताती।"),
    "hook": "बल-काल-देश-सात्म्य-प्रकृति: पाँच को परखो, तब बस्ति दो।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "What does सात्म्य mean in unit 52?",
            ("What suits by habit",
             "सात्म्य = what is agreeable or suitable by habit."),
            [("The patient's bodily strength", "Strength is बल, the first member of the list."),
             ("The region where one lives", "Region is देश, the third member."),
             ("The heat of the drug", "No heat of drugs is named in unit 52.")],
            "The fourth member, सात्म्य, is what suits a person by habit.",
            "सात्म्य = what suits by habit."),
        match(1, "Match each factor of unit 52 to its meaning as the card gives it.",
              [["बल", "strength"], ["काल", "time or season"], ["देश", "region"],
               ["सात्म्य", "what suits by habit"], ["प्रकृति", "constitution"]],
              "One dvandva compound names the five factors to be distinguished.",
              "बल = strength; काल = time/season; देश = region; सात्म्य = what suits by habit; प्रकृति = constitution."),
        order(2, "Put the five factors of unit 52 in the text's order.",
              ["बल", "काल", "देश", "सात्म्य", "प्रकृति"],
              "बल-काल-देश-सात्म्य-प्रकृतीः: strength, time, region, habit-suitability, constitutions.",
              "बल · काल · देश · सात्म्य · प्रकृति.",
              role="extend",
              teaches="Unit 52: a basti is applied after distinguishing strength, time, region, sātmya and constitutions, in that order."),
        mcq("discriminate", 3, "Which noun of unit 52 is the subject of the sentence that continues into line 05.04.101?",
            ("बस्तिः",
             "बस्तिः is masculine nominative singular: the basti that, once applied, removes the diseases."),
            [("प्रकृतीः", "प्रकृतीः is the end of the accusative dvandva: what is distinguished."),
             ("बल", "बल is only the first member of the accusative compound."),
             ("देश", "देश is a member inside the same accusative compound.")],
            "The five factors are the object of प्रविभज्य; the basti is the subject.",
            "Subject = बस्तिः (nom.); object of distinguishing = the five factors (acc.)."),
        mcq("apply", 4, "A physician gives every patient the same basti without asking about habit or season. What does unit 52 require instead?",
            ("First distinguish strength, time, region, habit-suitability, constitution",
             "This is the unit's own list of what must be distinguished."),
            [("First find which disease the patient's family has had", "Family history is not in unit 52."),
             ("First give the patient a day's fast before any basti", "No fast is named in unit 52."),
             ("First check the season alone and ignore the rest", "Season is one of five; all five are to be distinguished.")],
            "प्रविभज्य: the basti is applied after the five factors are told apart.",
            "Apply a basti after weighing bala, kāla, deśa, sātmya, prakṛti."),
        mcq("transfer", 5, "प्र-वि + √भज् gives प्रविभज्य, having distinguished. Which is the absolutive of invented सम् + √युज्, having joined?",
            ("संयुज्य",
             "With a prefix the absolutive takes -य: सम् + युज् + य = संयुज्य."),
            [("संयुक्त्वा", "-त्वा is used without a prefix; with सम् the ending is -य."),
             ("संयोजितः", "That is a past participle (joined), like योजितः, not an absolutive."),
             ("संयुनक्ति", "That is a present verb (he joins), not an absolutive.")],
            "Prefixed root + -य = absolutive (प्रविभज्य, संयुज्य).",
            "With a prefix: -य; without: -त्वा.",
            teaches="An absolutive of a prefixed root ends in -य (प्रविभज्य; invented संयुज्य), not -त्वा."),
    ],
}

# ---------------------------------------------------------------- unit 53
AUTHORED["53"] = {
    "title": "स्वैः स्वैरौषधवर्गैः",
    "question": "How does the basti of line 05.04.100 remove diseases, and which bastis suit heat and cold?",
    "rule": ("The basti removes each disease with that disease's own group of drugs. For those afflicted by heat, cool (bastis); "
             "for those afflicted by cold, pleasantly warm ones. The object bastīn and the verb come in line 05.04.103."),
    "limits": ("Line 1 appears to complete line 05.04.100; line 2 gives accusatives that qualify the bastis of line 05.04.103. "
               "No drug group is named here."),
    "explain_hi": ("पहली पंक्ति पिछली पंक्ति की बस्ति का वाक्य पूरा करती लगती है: वह अपने-अपने औषध-समूहों से अपने-अपने रोगों को निवृत्त करती है, यानी लौटा देती है। "
                   "‘स्वैः स्वैः’ और ‘स्वान् स्वान्’ की आवृत्ति का अर्थ है ‘हर एक का अपना’। "
                   "दूसरी पंक्ति गर्मी और सर्दी का जोड़ा देती है: गर्मी से पीड़ितों के लिए ठंडी, और सर्दी से पीड़ितों के लिए सुखद गरम बस्तियाँ। "
                   "ये द्वितीया रूप हैं; इनकी क्रिया ‘युञ्जीत’ अगली पंक्ति ०५.०४.१०३ में है। कोई औषध-समूह यहाँ नाम से नहीं गिनाया गया।"),
    "hook": "हर रोग का अपना औषध-वर्ग; गर्मी में ठंडी, ठंड में सुखद गरम बस्ति।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "For those afflicted by heat, which bastis does verse 53 name?",
            ("Cool ones (शीतान्)",
             "उष्णार्तानां शीतान्: for the heat-afflicted, cool ones."),
            [("Pleasantly warm ones (सुखोष्णान्)", "Pleasantly warm ones are for those afflicted by cold."),
             ("Sharp ones (तीक्ष्णान्)", "Sharp bastis are not named in verse 53."),
             ("Oily ones (स्निग्धान्)", "Oily bastis are not named in verse 53.")],
            "Line 2 pairs heat with cool and cold with pleasantly warm.",
            "उष्णार्त → शीत; शीतार्त → सुखोष्ण."),
        match(1, "Match each word of verse 53 to its meaning as the card gives it.",
              [["औषधवर्ग", "group of drugs"], ["निवर्तयति", "causes to turn back"], ["उष्णार्त", "afflicted by heat"],
               ["शीतार्त", "afflicted by cold"], ["सुखोष्ण", "pleasantly warm"]],
              "Line 1 gives how diseases are removed; line 2 the heat and cold pair.",
              "औषधवर्ग = drug-group; निवर्तयति = causes to turn back; उष्णार्त = heat-afflicted; शीतार्त = cold-afflicted; सुखोष्ण = pleasantly warm."),
        order(2, "Put these phrases of verse 53 in the verse's order.",
              ["स्वैः स्वैः औषधवर्गैः", "स्वान् स्वान् रोगान्", "निवर्तयति", "उष्णार्तानां शीतान्", "शीतार्तानां सुखोष्णान्"],
              "By their own drug groups, their own diseases, it turns back; for heat, cool; for cold, pleasantly warm.",
              "स्वैः स्वैः औषधवर्गैः · स्वान् स्वान् रोगान् · निवर्तयति · उष्णार्तानां शीतान् · शीतार्तानां सुखोष्णान्.",
              role="extend",
              teaches="Verse 53: each disease is turned back by its own drug group; cool bastis for the heat-afflicted, pleasantly warm for the cold-afflicted."),
        mcq("discriminate", 3, "Which split of शीतांश्छीतार्त्तानां in verse 53 is right?",
            ("शीतान् + शीतार्तानाम्",
             "Final न् before श is printed here as ंश् and the श after it as छ (standard spelling शीताञ्छीत-): शीतान् + शीतार्तानाम्."),
            [("शीतम् + शीतार्तानाम्", "म् before श gives only anusvara: शीतं शीतार्तानाम्, with no छ."),
             ("शीताः + शीतार्तानाम्", "A visarga before श gives शीताः शीत- or शीताश्शीत-, with no anusvara."),
             ("शीतान् + छीतार्तानाम्", "छीतार्त is no word; the छ comes from श by sandhi.")],
            "शीतान् (cool ones) + शीतार्तानाम् (for those afflicted by cold).",
            "-न् + श- → -ञ्छ- (printed here -ंश्छ-)."),
        mcq("apply", 4, "A physician uses one fixed drug mixture in the basti for every disease. Which teaching of verse 53 does he ignore?",
            ("Each disease is turned back by its own drug group",
             "स्वैः स्वैरौषधवर्गैः स्वान् स्वान् रोगान्: each by its own group."),
            [("Every basti must be given cool to all", "Cool is only for the heat-afflicted; the cold-afflicted get warm."),
             ("A basti must never contain any drugs", "Verse 53 names drug groups in the basti."),
             ("Only diseases of heat may get bastis", "Verse 53 gives bastis for heat and for cold alike.")],
            "The repetition स्वैः स्वैः … स्वान् स्वान् matches each disease to its own drugs.",
            "Own drug group for own disease."),
        mcq("transfer", 5, "Verse 53 repeats स्वैः स्वैः for each one's own. What does invented गृहे गृहे mean?",
            ("In every house",
             "A repeated word gives the sense each or every: गृहे गृहे = in house after house."),
            [("In two houses", "Two houses would be the dual गृहयोः."),
             ("In a large house", "Large would need a word like महति; repetition does not mean size."),
             ("In a house within a house", "Repetition gives distribution, not one inside another.")],
            "Repeating a word distributes it: each, every, respective (स्वैः स्वैः, स्वान् स्वान्).",
            "Repeated word = each / every.",
            teaches="A word said twice gives the sense each or respective (स्वैः स्वैः; invented गृहे गृहे = in every house)."),
    ],
}

# ---------------------------------------------------------------- unit 54
AUTHORED["54"] = {
    "title": "तद्योग्यौषधयुक्तान् बस्तीन्",
    "question": "What does verse 54 say about the bastis for heat and cold, and what does its second line add?",
    "rule": ("Line 1: one should apply bastis joined with drugs suitable to that (the heat or cold of line 05.04.102). "
             "Line 2: and one should give bastis, as printed nourishing ones, in diseases fit to be cleansed."),
    "limits": ("Low confidence. संतर्क्स is no form; read conjecturally as संतर्क्य, having considered. The printed pairing of "
               "nourishing bastis with diseases fit to be cleansed is an open question (either word may be corrupt); no question uses it."),
    "explain_hi": ("पहली पंक्ति पिछली पंक्ति की ठंडी और सुखद गरम बस्तियों का वाक्य पूरा करती लगती है: उसके योग्य औषधों से युक्त बस्तियाँ प्रयुक्त करे। "
                   "‘तद्’ = वह, यानी पंक्ति ०५.०४.१०२ की गर्मी या सर्दी। छपा ‘संतर्क्स’ कोई रूप नहीं; अनुमानित पाठ पर ‘संतर्क्य’ यानी विचार करके। "
                   "दूसरी पंक्ति में छपा है कि बृंहणीय यानी पोषण करने वाली बस्तियाँ विशोधन के योग्य रोगों में दे; यह जोड़ा उलटा लगता है और खुला प्रश्न है। "
                   "‘युञ्जीत’ और ‘दद्यात्’ दोनों विधिलिङ् हैं: ‘करे’, ‘दे’।"),
    "hook": "जैसा ताप, वैसी औषध: उसके योग्य औषध वाली बस्ति लगाओ।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What does युञ्जीत (printed युंजीत) mean in verse 54?",
            ("One should apply",
             "Optative 3rd singular middle of √युज्: one should apply."),
            [("One has applied", "A past form would be different; the gram label says optative."),
             ("It will be applied", "That would be a future passive, not an optative."),
             ("Applying", "That would be a present participle, not a finite verb.")],
            "युञ्जीत governs the bastis of line 1.",
            "युञ्जीत = should apply (opt.)."),
        match(1, "Match each word of verse 54 line 1, and one of line 2, to its meaning.",
              [["तद्", "that (the heat or cold)"], ["योग्य", "suitable"], ["औषध", "drugs"],
               ["युक्त", "joined with"], ["व्याधिषु", "in diseases"]],
              "Line 1: bastis joined with drugs suitable to that; line 2: in diseases.",
              "तद् = that; योग्य = suitable; औषध = drugs; युक्त = joined with; व्याधिषु = in diseases."),
        order(2, "Put the members of the compound तद्योग्यौषधयुक्तान् in their order.",
              ["तद्", "योग्य", "औषध", "युक्त"],
              "तद्-योग्य-औषध-युक्तान्: joined with drugs suitable to that.",
              "तद् · योग्य · औषध · युक्त.",
              role="extend",
              teaches="Verse 54 line 1: bastis joined with drugs suitable to that (heat or cold) are to be applied."),
        mcq("discriminate", 3, "Which split of बस्तीञ्च in verse 54 is right?",
            ("बस्तीन् + च",
             "बस्तीन् + च: the print writes the न् as ञ् before च (the standard sandhi gives बस्तींश्च, as in सुखोष्णांश्च of line 05.04.102)."),
            [("बस्तीः + च", "A visarga before च becomes श्: it would give बस्तीश्च."),
             ("बस्ती + ञ्च", "ञ्च is no word; the ञ् comes from न् by sandhi."),
             ("बस्तिम् + च", "बस्तिम् has a short इ; it would give बस्तिं च, not बस्तीञ्च.")],
            "बस्तीन् (bastis, acc. pl.) + च (and).",
            "बस्तीन् + च: printed -ञ्च, standard -ंश्च."),
        mcq("apply", 4, "In verse 54 line 1, what does तद् (that) refer to?",
            ("The heat or cold of line 05.04.102",
             "The notes: तद् refers to the heat or cold in the line before."),
            [("The strength and region of line 05.04.100", "Those factors were to be distinguished; तद् points to heat or cold."),
             ("The kuṣṭha and meha of line 05.04.105", "That line comes later and is not what तद् points back to."),
             ("The oil inside the basti itself", "No oil is named in verse 54.")],
            "Bastis are joined with drugs suited to the heat or cold to be treated.",
            "तद् = the heat or cold of 05.04.102."),
        mcq("transfer", 5, "दद्यात् in verse 54 means one should give. Which invented phrase means one should give a basti?",
            ("बस्तिं दद्यात्",
             "दद्यात् is the optative: should give."),
            [("बस्तिं ददौ", "ददौ is the perfect: he gave."),
             ("बस्तिं दास्यति", "दास्यति is the future: he will give."),
             ("बस्तिं दत्तवान्", "दत्तवान् is a past active participle: he has given.")],
            "The optative (दद्यात्, युञ्जीत) gives the rule: one should do it.",
            "Optative = should.",
            teaches="An optative such as दद्यात् or युञ्जीत states what one should do (invented बस्तिं दद्यात्, one should give a basti)."),
    ],
}

# ---------------------------------------------------------------- unit 55
AUTHORED["55"] = {
    "title": "मेदस्विनो विशोध्या",
    "question": "Which people does unit 55 name?",
    "rule": ("Unit 55 names: the fat (medasvin), those to be cleansed, and the men afflicted by kuṣṭha (skin disease) and "
             "meha (urinary disorder). The verb they belong to is not in this unit."),
    "limits": ("No verb and no stated treatment here; the passage 05.04.104-107 is joined. Whether 'the fat' and 'to be cleansed' "
               "are two groups or one (the fat who are to be cleansed) is two-way; no question uses the grouping."),
    "explain_hi": ("यह इकाई लोगों की एक सूची देती है: मेदस्वी यानी अधिक मेद वाले (मोटे), विशोध्य यानी शोधन के योग्य, और वे मनुष्य जो कुष्ठ यानी त्वचा-रोग और मेह यानी मूत्र-विकार से पीड़ित हैं। "
                   "मेह वही समूह है जो पंक्ति ०५.०४.८८ में प्रमेह है। "
                   "इस इकाई में क्रिया नहीं है; इन्हें क्या दिया जाए, यह पंक्ति ०५.०४.१०४ से १०७ के अंश से जुड़ा है। "
                   "‘मेदस्विनो विशोध्याः’ को ‘शोधन-योग्य मोटे लोग’ भी पढ़ा जा सकता है।"),
    "hook": "मोटे, शोधन-योग्य, और कुष्ठ-मेह के रोगी: पंक्ति १०५ के लोग।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What does मेदस्विन् mean in unit 55?",
            ("Fat, rich in medas",
             "मेदस्विन् = having much medas (fat tissue): fat, obese."),
            [("Wise, quick of mind", "That is मेधाविन्, from मेधा; here it is मेदस्, fat."),
             ("Thin and wasted", "Thin and wasted people come in line 05.04.106."),
             ("Burning with fever", "No fever is named in unit 55.")],
            "मेदस् + -विन् = one who has much fat.",
            "मेदस्विन् = fat."),
        match(1, "Match each word of unit 55 to its meaning as the card gives it.",
              [["मेदस्विन्", "fat"], ["विशोध्य", "to be cleansed"], ["नर", "man"],
               ["कुष्ठ", "skin disease"], ["मेह", "urinary disorder"]],
              "The unit names the fat, those to be cleansed, and men with kuṣṭha and meha.",
              "मेदस्विन् = fat; विशोध्य = to be cleansed; नर = man; कुष्ठ = skin disease; मेह = urinary disorder."),
        order(2, "Put these parts of unit 55 in the text's order.",
              ["मेदस्विनः", "विशोध्याः", "ये च नराः", "कुष्ठमेहार्ताः"],
              "The fat, those to be cleansed, and the men who are afflicted by kuṣṭha and meha.",
              "मेदस्विनः · विशोध्याः · ये च नराः · कुष्ठमेहार्ताः.",
              role="extend",
              teaches="Unit 55 names the fat, those to be cleansed, and men afflicted by kuṣṭha (skin disease) and meha (urinary disorder)."),
        mcq("discriminate", 3, "Which split of कुष्ठमेहार्त्ताः in unit 55 is right?",
            ("कुष्ठ + मेह + आर्ताः",
             "अ + आ → आ: मेह + आर्ताः = मेहार्ताः."),
            [("कुष्ठ + मेहे + आर्ताः", "ए + आ would give अया: मेहयार्ताः."),
             ("कुष्ठ + मेहः + आर्ताः", "-अः before आ drops the visarga with no merging: मेह आर्ताः."),
             ("कुष्ठ + मेहा + र्ताः", "र्ताः is no word; the र् belongs to आर्त.")],
            "कुष्ठ (skin disease) + मेह (urinary disorder) + आर्ताः (afflicted).",
            "अ + आ → आ."),
        multi("apply", 4, "Five people come to the clinic. Which of them does unit 55 itself name?",
              [("A fat (obese) man", "Right: मेदस्विनः."),
               ("A man afflicted by kuṣṭha", "Right: कुष्ठ-आर्ताः."),
               ("A man afflicted by meha", "Right: मेह-आर्ताः."),
               ("A man who has fainted", "Fainted (मूर्च्छित) is in line 05.04.106, not here."),
               ("A man who is thin and dried-up", "Thin and dried-up (कृश, शुष्क) are in line 05.04.106.")],
              [0, 1, 2],
              "Unit 55 names the fat, those to be cleansed, and men with kuṣṭha and meha.",
              "Unit 55: मेदस्विन्, विशोध्य, कुष्ठ- and मेह-आर्त."),
        mcq("transfer", 5, "Like विशोध्याः + ये → विशोध्या ये, how does invented नराः + गच्छन्ति (the men go) join?",
            ("नरा गच्छन्ति",
             "-आः before a voiced sound (ग) drops its visarga, as in विशोध्या ये."),
            [("नरो गच्छन्ति", "-ओ comes from -अः, not from -आः."),
             ("नरार्गच्छन्ति", "र् comes from -इः/-उः before voiced sounds, not from -आः."),
             ("नराश्गच्छन्ति", "श् stands only before च/छ/श, not before ग.")],
            "-आः + voiced consonant or vowel → -आ (visarga lost).",
            "-आः + voiced → -आ.",
            teaches="A visarga after -आ is dropped before a voiced sound (विशोध्याः + ये → विशोध्या ये; invented नरा गच्छन्ति)."),
    ],
}

# ---------------------------------------------------------------- unit 56
AUTHORED["56"] = {
    "title": "न क्षीणक्षतदुर्बल",
    "question": "Which people does unit 56 list after its opening न (not)?",
    "rule": ("Not of those with wasted, injured, weak, fainted, thin, dried-up and purified bodies. "
             "The unit has no verb; it appears to run on into line 05.04.107."),
    "limits": ("No verb, so what is denied them is not in this unit. Śuddha is purified, probably by earlier evacuation, "
               "but the text does not say. Kṣata may also mean chest wound. The printed space after मूर्च्छित is possibly a stray space (text flag)."),
    "explain_hi": ("यह इकाई ‘न’ यानी नहीं से शुरू होती है और सात तरह के लोगों के नाम देती है: क्षीण, क्षत यानी घायल, दुर्बल, मूर्च्छित, कृश यानी पतले, सूखे शरीर वाले, और शुद्ध यानी जिनका शोधन हो चुका। "
                   "अन्तिम ‘देहानाम्’ षष्ठी बहुवचन है: ऐसे शरीर वालों का। "
                   "इकाई में क्रिया नहीं; वाक्य पंक्ति ०५.०४.१०७ में चलता लगता है, इसलिए इन्हें क्या न दिया जाए, वह वहीं देखें। "
                   "‘शुद्ध’ सम्भवतः पहले के शोधन से शुद्ध है, पर पाठ यह नहीं कहता।"),
    "hook": "क्षीण, क्षत, दुर्बल, मूर्च्छित, कृश, शुष्क, शुद्ध: सात पर ‘न’।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What does कृश mean in unit 56?",
            ("Thin",
             "कृश = thin, lean."),
            [("Fat", "Fat is मेदस्विन्, in line 05.04.105."),
             ("Swollen", "No swelling is named in unit 56."),
             ("Strong", "Strong would be the opposite of दुर्बल, which is in the list.")],
            "कृश stands in the second compound: thin, dried-up, purified bodies.",
            "कृश = thin."),
        match(1, "Match each word of unit 56 to its meaning as the card gives it.",
              [["क्षीण", "wasted"], ["क्षत", "injured"], ["दुर्बल", "weak"],
               ["मूर्च्छित", "fainted"], ["शुष्क", "dried-up"]],
              "All are states of the body named after न.",
              "क्षीण = wasted; क्षत = injured; दुर्बल = weak; मूर्च्छित = fainted; शुष्क = dried-up."),
        order(2, "Put these states of unit 56 in the text's order.",
              ["क्षीण", "क्षत", "दुर्बल", "मूर्च्छित", "कृश", "शुष्क"],
              "क्षीण-क्षत-दुर्बल-मूर्च्छित, then कृश-शुष्क-शुद्ध-देहानाम्.",
              "क्षीण · क्षत · दुर्बल · मूर्च्छित · कृश · शुष्क.",
              role="extend",
              teaches="Unit 56 lists, after न: wasted, injured, weak, fainted, thin, dried-up and purified bodies."),
        mcq("discriminate", 3, "In unit 56, what does the ending of देहानाम् show?",
            ("Genitive plural: of those with such bodies",
             "-आनाम् is the genitive plural; the compound is a bahuvrīhi: of those whose bodies are thin and the rest."),
            [("Nominative plural: these bodies are", "The nominative plural would be देहाः."),
             ("Accusative plural: such bodies as object", "The accusative plural would be देहान्."),
             ("Locative plural: in such bodies", "The locative plural would be देहेषु.")],
            "न … देहानाम्: not of those with … bodies.",
            "-आनाम् = genitive plural."),
        mcq("apply", 4, "A patient is weak and has fainted. Does unit 56 by itself state the treatment he gets?",
            ("No: it opens with न and has no verb",
             "The unit only lists the people under न; the verb comes in line 05.04.107."),
            [("Yes: it gives him a nourishing basti", "No basti kind is named in unit 56."),
             ("Yes: it gives him a cool basti", "Cool is said for the heat-afflicted in line 05.04.102."),
             ("Yes: it orders a day's fasting", "No fasting is named in unit 56.")],
            "Keep to what the unit contains: a list after न, no verb.",
            "Unit 56: no verb, only a list after न."),
        mcq("transfer", 5, "Like कृशदेह (one whose body is thin), what does invented दृढदेहः mean?",
            ("One whose body is firm",
             "A bahuvrīhi: firm (दृढ) + body (देह) describes the person who has it."),
            [("The firmness of the body", "That would be an abstract noun like देहदार्ढ्यम्."),
             ("A firm part of a body", "A bahuvrīhi describes the owner, not a part."),
             ("The body makes things firm", "No verb or action is in the compound.")],
            "In a bahuvrīhi the compound describes someone else: the person with such a body.",
            "Adjective + देह (bahuvrīhi) = one whose body is …",
            teaches="Adjective + देह makes a bahuvrīhi: one whose body is so (कृशदेह; invented दृढदेहः, one whose body is firm)."),
    ],
}

# ---------------------------------------------------------------- unit 57
AUTHORED["57"] = {
    "title": "दद्याद्विशोधनीयान्",
    "question": "What do the words of unit 57 say, and how does it hang on line 05.04.106?",
    "rule": ("Printed: one should give cleansing (bastis), and those whose life is bound up in the doṣas. It appears to "
             "continue line 05.04.106, which opens with न."),
    "limits": ("Low confidence. Whether the न of line 05.04.106 turns this into a prohibition is an open question; no question "
               "uses it. The nominative दोषनिबद्धायुषो ये does not match the genitive of line 05.04.106, and the end dangles."),
    "explain_hi": ("छपे पाठ में: शोधन करने वाली बस्तियाँ दे, और वे जिनकी आयु दोषों से बँधी है। "
                   "‘दोषनिबद्धायुस्’ बहुव्रीहि है: जिसकी आयु दोषों से बँधी है। "
                   "यह इकाई पिछली पंक्ति ०५.०४.१०६ का वाक्य आगे बढ़ाती लगती है, जो ‘न’ से शुरू होती है; तब पूरा वाक्य सम्भवतः निषेध है, पर यह खुला प्रश्न है। "
                   "व्याकरण भी पूरा नहीं जुड़ता: यहाँ प्रथमा है, वहाँ षष्ठी।"),
    "hook": "दद्यात्: दे; दोषनिबद्धायु: जिनकी आयु दोषों से बँधी।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What does दद्यात् mean in unit 57?",
            ("One should give",
             "Optative 3rd singular of √दा: one should give."),
            [("He gave long ago", "A past form would be ददौ or अददात्."),
             ("He will give", "The future would be दास्यति."),
             ("Having given", "Having given would be दत्त्वा.")],
            "दद्यात् opens the unit and governs विशोधनीयान्.",
            "दद्यात् = should give."),
        match(1, "Match each word of unit 57 to its meaning as the card gives it.",
              [["दद्यात्", "should give"], ["विशोधनीय", "cleansing"], ["दोष", "doṣa"],
               ["निबद्ध", "bound"], ["आयुस्", "life"]],
              "The unit gives a verb, its object and a bahuvrīhi about life bound up in the doṣas.",
              "दद्यात् = should give; विशोधनीय = cleansing; दोष = doṣa; निबद्ध = bound; आयुस् = life."),
        order(2, "Put the words of unit 57 in the text's order, after the split.",
              ["दद्यात्", "विशोधनीयान्", "दोषनिबद्धायुषः", "ये", "च"],
              "Should give, cleansing ones, life-bound-in-doṣas, who, and.",
              "दद्यात् · विशोधनीयान् · दोषनिबद्धायुषः · ये · च.",
              role="extend",
              teaches="Unit 57 reads: dadyāt viśodhanīyān doṣanibaddhāyuṣaḥ ye ca, one should give cleansing ones, and those whose life is bound up in the doṣas."),
        mcq("discriminate", 3, "Which split of दद्याद्विशोधनीयान् in unit 57 is right?",
            ("दद्यात् + विशोधनीयान्",
             "Final त् before a voiced sound (व) becomes द्."),
            [("दद्या + द्विशोधनीयान्", "द्विशोधनीय is no word; the द् is the changed त्."),
             ("दद्याम् + विशोधनीयान्", "म् before व would give दद्यां विशोधनीयान्."),
             ("दद्यात + विशोधनीयान्", "A final अ would stay: दद्यातविशोधनीयान्.")],
            "दद्यात् (should give) + विशोधनीयान् (cleansing ones).",
            "-त् + voiced → -द्."),
        mcq("apply", 4, "Whom does the bahuvrīhi दोषनिबद्धायुः describe?",
            ("A person whose life is bound up in the doṣas",
             "Doṣa + bound + life: the one whose life is bound up with the doṣas."),
            [("A doṣa that is held fast by life", "The head is life (आयुस्), and it describes a person."),
             ("A life that is free of all doṣas", "निबद्ध is bound, not freed."),
             ("A basti that binds the doṣas fast", "No basti is named inside the compound.")],
            "Bahuvrīhi: the compound describes its owner, here people (ये).",
            "दोषनिबद्धायुः = one whose life is bound up in the doṣas."),
        mcq("transfer", 5, "Like दद्यात् + विशोधनीयान् → दद्याद्विशोधनीयान्, how does invented पिबेत् + दुग्धम् (he should drink milk) join?",
            ("पिबेद्दुग्धम्",
             "Final त् before a voiced द becomes द्."),
            [("पिबेन्दुग्धम्", "त् becomes न् only before a nasal."),
             ("पिबेच्दुग्धम्", "त् becomes च् only before च/छ."),
             ("पिबेल्दुग्धम्", "त् becomes ल् only before ल.")],
            "-त् + voiced consonant → -द्.",
            "-त् + voiced → -द्.",
            teaches="Final त् becomes द् before a voiced sound (दद्याद्विशोधनीयान्; invented पिबेद्दुग्धम्)."),
    ],
}

# ---------------------------------------------------------------- unit 58
AUTHORED["58"] = {
    "title": "इति बस्तिकल्पो नाम",
    "question": "What is the name and number of the chapter that unit 58 closes?",
    "rule": "Thus the fourth chapter, named Bastikalpa: the basti preparations.",
    "limits": "A colophon, not a verse. It names the chapter; it states no teaching.",
    "explain_hi": ("यह अध्याय का समापन-वाक्य है: इस प्रकार बस्तिकल्प नामक चतुर्थ अध्याय। "
                   "‘बस्तिकल्प’ = बस्ति के कल्प, यानी बस्ति बनाने की विधियाँ। "
                   "इस अध्याय में अलग-अलग रोगों की बस्तियाँ, उनके द्रव्य और मात्राएँ, तीक्ष्णता-मृदुता और प्रयोग के नियम बताए गए। "
                   "‘चतुर्थोऽध्यायः’ = चतुर्थः + अध्यायः।"),
    "hook": "चौथा अध्याय: बस्तिकल्प, बस्तियाँ बनाने की विधियाँ।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "Which number is the chapter that unit 58 closes?",
            ("Fourth", "चतुर्थः = fourth."),
            [("Third", "Third would be तृतीयः."),
             ("Fifth", "Fifth would be पञ्चमः."),
             ("Fortieth", "Fortieth would be चत्वारिंशः; चतुर्थ is fourth.")],
            "चतुर्थोऽध्यायः = the fourth chapter.",
            "चतुर्थ = fourth."),
        match(1, "Match each word of unit 58 to its meaning.",
              [["इति", "thus"], ["बस्ति", "basti (enema)"], ["कल्प", "preparation"],
               ["नाम", "named"], ["अध्याय", "chapter"]],
              "इति बस्तिकल्पो नाम चतुर्थोऽध्यायः.",
              "इति = thus; बस्ति = basti; कल्प = preparation; नाम = named; अध्याय = chapter."),
        order(2, "Put the words of unit 58 in the text's order, after the split.",
              ["इति", "बस्तिकल्पः", "नाम", "चतुर्थः", "अध्यायः"],
              "Thus, Bastikalpa, named, fourth, chapter.",
              "इति · बस्तिकल्पः · नाम · चतुर्थः · अध्यायः.",
              role="extend",
              teaches="The colophon: iti bastikalpo nāma caturtho 'dhyāyaḥ, thus the fourth chapter, named Bastikalpa."),
        mcq("discriminate", 3, "Which split is right for चतुर्थोऽध्यायः?",
            ("चतुर्थः + अध्यायः", "-अः before अ gives -ओ and the अ is shown by ऽ."),
            [("चतुर्थ + अध्यायः", "अ + अ would merge to आ: चतुर्थाध्यायः."),
             ("चतुर्थो + ध्यायः", "ध्यायः is not the word; the chapter is अध्यायः."),
             ("चतुर्थम् + अध्यायः", "म् before a vowel would give चतुर्थमध्यायः.")],
            "चतुर्थः (fourth) + अध्यायः (chapter).",
            "-अः + अ- → -ओऽ."),
        mcq("apply", 4, "A student asks what the chapter title Bastikalpa names. What does the card say?",
            ("The basti preparations", "बस्ति-कल्प: the preparations of bastis."),
            [("The complications of a basti", "Complications (व्यापद्) are not in this title."),
             ("The parts of the body", "The title names bastis, not body parts."),
             ("The seasons for collecting drugs", "The title names no season or collecting.")],
            "बस्तिकल्पः is a tat-puruṣa: kalpa (preparation) of basti.",
            "बस्तिकल्प = basti preparations."),
        mcq("transfer", 5, "Like बस्तिकल्पः + नाम → बस्तिकल्पो नाम, how does invented वमनकल्पः + नाम join?",
            ("वमनकल्पो नाम", "-अः before a voiced sound (न) becomes -ओ."),
            [("वमनकल्पा नाम", "-आ comes from -आः, not from -अः."),
             ("वमनकल्पर्नाम", "र् comes from -इः/-उः before voiced sounds, not from -अः."),
             ("वमनकल्पस्नाम", "स् stands only before त/थ, not before न.")],
            "-अः + voiced consonant → -ओ.",
            "-अः + voiced → -ओ.",
            teaches="-अः before a voiced consonant becomes -ओ (बस्तिकल्पो नाम; invented वमनकल्पो नाम)."),
    ],
}

NOTES_HI = {
    "52": ("विश्वास: उच्च। पंक्ति ०५.०४.१००; वाक्य पंक्ति ०५.०४.१०१ की क्रिया ‘निवर्तयति’ तक चलता लगता है। "
           "बलकालदेशसात्म्यप्रकृतीः = बल + काल + देश + सात्म्य + प्रकृतीः (द्वन्द्व, स्त्रीलिङ्ग द्वितीया बहुवचन, ‘प्रविभज्य’ का कर्म)। "
           "‘काल’ समय या ऋतु, दोनों अर्थ बैठते हैं। संधि जाँची: योजितो बस्तिः = योजितः + बस्तिः (अः + घोष → ओ)। कोई text_flag नहीं।"),
    "53": ("विश्वास: उच्च। पंक्तियाँ ०५.०४.१०१-१०२। पहली पंक्ति पंक्ति १०० का वाक्य पूरा करती लगती है; दूसरी पंक्ति की द्वितीया बहुवचन विशेषण "
           "पंक्ति १०३ की ‘बस्तीन्’ और ‘युञ्जीत’ से जुड़ते लगते हैं। वर्तनी-सामान्यीकरण: छपा ‘निवर्त्तयति’ = निवर्तयति, ‘आर्त्तानां’ = आर्तानाम्। "
           "संधि जाँची: स्वैरौषध = स्वैः + औषध; स्वांस्वान्रोगान्निवर्त्तयति = स्वान् + स्वान् + रोगान् + निवर्तयति; "
           "शीतांश्छीतार्त्तानां = शीतान् + शीतार्तानाम् (न् + श → ञ्छ, छपाई में ंश्छ; श → छ वैकल्पिक); सुखोष्णांश्च = सुखोष्णान् + च।"),
    "54": ("विश्वास: निम्न। पंक्तियाँ ०५.०४.१०३-१०४। ‘तद्’ पंक्ति १०२ की गर्मी या सर्दी की ओर है। "
           "text_flag: छपा ‘संतर्क्स’ कोई रूप नहीं; अनुमानित पाठ पर ‘संतर्क्य’ (विचार करके), क्य/क्स छपाई में मिलते हैं; इस पर प्रश्न नहीं। "
           "text_flag और खुला प्रश्न (OPEN ०५.०४.१०४): ‘बृंहणीयान्’ बस्तियाँ ‘विशोधनीयेषु’ रोगों में, यह जोड़ा उलटा लगता है; "
           "सुझाव ‘विशोधनीयान्’ है, पर उतना ही सम्भव है कि ‘विशोधनीयेषु’ ही बिगड़ा हो (बृंहणीयेषु)। अनुवाद छपे पाठ पर; इन दोनों शब्दों पर प्रश्न नहीं। "
           "उसी छपे टुकड़े के ‘दद्यात्’ और ‘व्याधिषु’ साफ़ हैं। संधि जाँची: बस्तीञ्च = बस्तीन् + च; युंजीत = युञ्जीत।"),
    "55": ("विश्वास: मध्यम। पंक्ति ०५.०४.१०५; पंक्ति १०४-१०७ का अंश; क्रिया ‘दद्यात्’ पंक्ति १०४ में, इस इकाई में नहीं। "
           "दो-तरफ़ा पाठ: ‘मेदस्विनो विशोध्याः’ = ‘मोटे, और शोधन-योग्य’ (दो समूह) या ‘शोधन-योग्य मोटे’ (एक समूह); इस पर प्रश्न नहीं। "
           "मेह = पंक्ति ०५.०४.८८ का प्रमेह-समूह। संधि जाँची: मेदस्विनो विशोध्या = मेदस्विनः + विशोध्याः (अः + घोष → ओ); "
           "विशोध्या ये = विशोध्याः + ये (आः का विसर्ग घोष से पहले लुप्त); कुष्ठमेहार्त्ताः = कुष्ठ + मेह + आर्ताः।"),
    "56": ("विश्वास: मध्यम। पंक्ति ०५.०४.१०६; पंक्ति १०६-१०७ एक वाक्य लगता है, ‘न … देहानाम्’ पंक्ति १०७ के ‘दद्यात् विशोधनीयान्’ तक। "
           "text_flag: ‘मूर्च्छित’ के बाद छपा खाली स्थान सम्भवतः फालतू है; ‘मूर्च्छित’ आगे के ‘कृश-’ वाले समास से जुड़ता है; इस पर प्रश्न नहीं। "
           "‘शुद्ध’ सम्भवतः पहले के शोधन से शुद्ध, पाठ यह नहीं कहता; ‘क्षत’ = घायल, ‘छाती का घाव’ भी सम्भव। "
           "कृशशुष्कशुद्धदेहानाम् = बहुव्रीहि, षष्ठी बहुवचन।"),
    "57": ("विश्वास: निम्न। पंक्ति ०५.०४.१०७; पंक्ति १०६ का वाक्य आगे बढ़ाती लगती है। "
           "खुला प्रश्न (OPEN ०५.०४.१०७): अकेले पढ़ने पर यह ‘दे’ (विधि) है; पंक्ति १०६ का ‘न’ इस पर लगे तो पूरा वाक्य निषेध बनता है, "
           "यानी क्षीण आदि को और जिनकी आयु दोषों पर टिकी है उन्हें शोधन बस्ति न दे; यह तय नहीं, इसलिए इस पर प्रश्न नहीं। "
           "‘दोषनिबद्धायुषः’ प्रथमा बहुवचन (या षष्ठी एकवचन) और ‘ये’ प्रथमा बहुवचन है और पंक्ति १०६ की षष्ठी ‘देहानाम्’ से मेल नहीं खाता; अन्त अधूरा। "
           "संधि जाँची: दद्याद्विशोधनीयान् = दद्यात् + विशोधनीयान्; दोषनिबद्धायुषो ये = दोषनिबद्धायुषः + ये।"),
    "58": ("विश्वास: उच्च। पंक्ति ०५.०४.१०८, अध्याय का समापन-वाक्य (कोलोफ़न), श्लोक नहीं; ‘इति’ समापन का चिह्न है। "
           "संधि जाँची: बस्तिकल्पो नाम = बस्तिकल्पः + नाम; चतुर्थोऽध्यायः = चतुर्थः + अध्यायः (अः + अ → ओऽ)। कोई text_flag नहीं।"),
}

AIDS = {
    "52": {
        "chain": {"steps": ["बल", "काल (समय/ऋतु)", "देश", "सात्म्य", "प्रकृति", "इन्हें अलग-अलग पहचानकर", "प्रयुक्त बस्ति (आगे पंक्ति १०१)"]},
        "anchors": "बल = ताक़त · काल = समय या ऋतु · देश = प्रदेश · सात्म्य = आदत से अनुकूल · प्रकृति = शरीर की प्रकृति · प्रविभज्य = अलग-अलग करके।",
        "chunks": "बल | काल | देश | सात्म्य | प्रकृतीः ‖ प्रविभज्य | योजितो | बस्तिः।",
        "pegs": "मेरा बनाया चित्र: पाँच उँगलियाँ, हर उँगली एक कारक: अँगूठा बल, फिर काल, देश, सात्म्य, और छोटी उँगली प्रकृति; मुट्ठी बँधी तो बस्ति तैयार।",
    },
    "53": {
        "seesaw": "उष्ण ↔ शीत: गर्मी से पीड़ित को ठंडी बस्तियाँ; सर्दी से पीड़ित को सुखद गरम बस्तियाँ।",
        "diagram": {"groups": [{"label": "पंक्ति १: हर रोग का अपना", "items": ["अपने-अपने औषध-वर्ग", "अपने-अपने रोग", "निवृत्त करती है"]},
                               {"label": "पंक्ति २: ताप के अनुसार", "items": ["गर्मी से पीड़ित: ठंडी", "सर्दी से पीड़ित: सुखद गरम"]}]},
        "chunks": "स्वैः | स्वैः | औषधवर्गैः | स्वान् | स्वान् | रोगान् | निवर्तयति ‖ उष्णार्तानां | शीतान् | शीतार्तानां | तथा | सुखोष्णान् | च।",
        "sandhi": "न् + श → ञ्छ (यहाँ छपा ंश्छ): शीतान् + शीतार्तानाम् → शीतांश्छीतार्तानाम्; ऐः + स्वर → ऐर्: स्वैः + औषध → स्वैरौषध; न् + च → ंश्च: सुखोष्णान् + च → सुखोष्णांश्च।",
    },
    "54": {
        "chunks": "तद्योग्यौषधयुक्तान् | बस्तीन् | संतर्क्स (अनुमानित संतर्क्य) | युंजीत ‖ बस्तीञ्च | बृंहणीयान् (पाठ खुला) | दद्याद् | व्याधिषु | विशोधनीयेषु।",
        "chain": {"steps": ["तद्: पंक्ति १०२ की गर्मी या सर्दी", "उसके योग्य औषध", "उनसे युक्त बस्तियाँ", "युञ्जीत: प्रयुक्त करे"]},
        "anchors": "तद् = वह · योग्य = उपयुक्त · औषध = दवाएँ · युक्त = से जुड़ा · युञ्जीत = प्रयुक्त करे · दद्यात् = दे · व्याधिषु = रोगों में।",
        "sandhi": "न् + च: छपा बस्तीञ्च (मानक संधि बस्तींश्च, जैसे पंक्ति १०२ का सुखोष्णांश्च) = बस्तीन् + च; अ + औ → औ: योग्य + औषध → योग्यौषध।",
    },
    "55": {
        "chunks": "मेदस्विनो | विशोध्या | ये | च | नराः | कुष्ठमेहार्त्ताः।",
        "anchors": "मेदस्विन् = अधिक मेद वाला, मोटा · विशोध्य = शोधन-योग्य · नर = मनुष्य · कुष्ठ = त्वचा-रोग · मेह = मूत्र-विकार (प्रमेह-समूह) · आर्त = पीड़ित।",
        "sandhi": "अः + घोष → ओ: मेदस्विनः + विशोध्याः → मेदस्विनो विशोध्याः; आः + घोष → आ: विशोध्याः + ये → विशोध्या ये; अ + आ → आ: मेह + आर्ताः → मेहार्ताः।",
    },
    "56": {
        "diagram": {"groups": [{"label": "न: इन शरीर वालों का नहीं", "items": ["क्षीण", "क्षत", "दुर्बल", "मूर्च्छित", "कृश", "शुष्क", "शुद्ध"]}]},
        "chunks": "न | क्षीण | क्षत | दुर्बल | मूर्च्छित ‖ कृश | शुष्क | शुद्ध | देहानाम्।",
        "anchors": "क्षीण = क्षय पाया · क्षत = घायल · दुर्बल = कमज़ोर · मूर्च्छित = बेहोश · कृश = पतला · शुष्क = सूखा · शुद्ध = जिसका शोधन हो चुका।",
        "puns": "केवल सुनने की सहायता: ‘क्षी-क्ष-दु-मू, कृ-शु-शु’, सात नामों के पहले अक्षर, दो साँसों में।",
    },
    "57": {
        "chunks": "दद्याद् | विशोधनीयान् | दोषनिबद्धायुषो | ये | च।",
        "anchors": "दद्यात् = दे · विशोधनीय = शोधन करने वाली · दोष = दोष · निबद्ध = बँधा · आयुस् = आयु।",
        "sandhi": "त् + घोष → द्: दद्यात् + विशोधनीयान् → दद्याद्विशोधनीयान्; अः + घोष → ओ: दोषनिबद्धायुषः + ये → दोषनिबद्धायुषो ये।",
    },
    "58": {
        "chunks": "इति | बस्तिकल्पो | नाम | चतुर्थोऽध्यायः।",
        "anchors": "इति = इस प्रकार · बस्ति = बस्ति · कल्प = विधि, निर्माण · नाम = नामक · चतुर्थ = चौथा · अध्याय = अध्याय।",
        "sandhi": "अः + घोष → ओ: बस्तिकल्पः + नाम → बस्तिकल्पो नाम; अः + अ → ओऽ: चतुर्थः + अध्यायः → चतुर्थोऽध्यायः।",
    },
}

IMAGE_SPECS = {
    ("52", "chain"): {
        "file": "ka4-pravibhajya-52.svg",
        "alt": ("Flowchart for unit 52: five factors, strength, time, region, satmya and constitution, are distinguished; "
                "then the basti is applied, continued in line 05.04.101"),
        "type": "mermaid",
        "code": ('flowchart TD\n'
                 '  A["बल"] --> F["अलग-अलग पहचानकर"]\n'
                 '  B["काल"] --> F\n'
                 '  C["देश"] --> F\n'
                 '  D["सात्म्य"] --> F\n'
                 '  E["प्रकृति"] --> F\n'
                 '  F --> G["प्रयुक्त बस्ति<br/>आगे पंक्ति १०१"]\n'),
    },
    ("53", "seesaw"): {
        "file": "ka4-ushnashita-53.svg",
        "alt": ("Table for verse 53 with two rows: those afflicted by heat get cool bastis; "
                "those afflicted by cold get pleasantly warm bastis"),
        "type": "table",
        "title": "श्लोक ५३: ताप के अनुसार बस्ति",
        "heads": ["पीड़ा", "बस्ति"],
        "rows": [["गर्मी से पीड़ित", "ठंडी"], ["सर्दी से पीड़ित", "सुखद गरम"]],
    },
    ("54", "chain"): {
        "file": "ka4-tadyogya-54.svg",
        "alt": ("Chain of four steps for verse 54 line 1: that, the heat or cold of line 102; drugs suitable to it; "
                "bastis joined with them; one should apply them"),
        "type": "chain",
        "title": "श्लोक ५४: उसके योग्य औषध",
        "steps": ["तद्: गर्मी या सर्दी (पंक्ति १०२)", "उसके योग्य औषध", "उनसे युक्त बस्तियाँ", "युञ्जीत: प्रयुक्त करे"],
    },
    ("56", "diagram"): {
        "file": "ka4-kshina-56.svg",
        "alt": ("Flowchart for unit 56: after 'not', seven kinds of body in the text's order: wasted, injured, weak, fainted, thin, dried-up, purified"),
        "type": "mermaid",
        "code": ('flowchart LR\n'
                 '  N["न: इन शरीर वालों का नहीं"] --> A["क्षीण"]\n'
                 '  A --> B["क्षत"]\n'
                 '  B --> C["दुर्बल"]\n'
                 '  C --> D["मूर्च्छित"]\n'
                 '  D --> E["कृश"]\n'
                 '  E --> F["शुष्क"]\n'
                 '  F --> G["शुद्ध"]\n'),
    },
}
