from helpers import mcq, match, order, fill, multi, accepts

AUTHORED = {}

# ---------------------------------------------------------------- unit 68
AUTHORED["68"] = {
    "title": "वर्षाशीतोचितांगानां",
    "question": "When does the Pitta accumulated earlier become aggravated, according to this verse?",
    "rule": ("In those whose bodies are used to the cold of the rains, when the "
             "sun's rays suddenly heat them, the Pitta accumulated earlier then "
             "becomes aggravated (प्रकुप्यति)."),
    "limits": ("The verse names one condition (a sudden change from the cold of "
               "the rains to the sun's heat) and one result (the earlier-accumulated "
               "Pitta is aggravated). It gives no remedy, no timing in days and "
               "no other dosha here."),
    "explain_hi": ("यह श्लोक वर्षा के बाद के बदलाव का वर्णन करता है। जिन लोगों के शरीर वर्षा की "
                   "शीतलता के अभ्यस्त हैं, वे जब सहसा ही सूर्य की किरणों से तप जाते हैं, तब "
                   "‘तदा’ (उस समय) पहले से संचित पित्त कुपित हो जाता है। यहाँ तीन बातें साफ़ हैं: "
                   "शीत का अभ्यास, अचानक ताप (‘सहसा’), और पहले से जमा हुआ पित्त। श्लोक इससे आगे कोई "
                   "उपाय या मात्रा नहीं बताता।"),
    "hook": "वर्षा की ठंडक में ढला शरीर, अचानक सूरज की किरणें — जमा पित्त कुपित।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "In this verse, when does the earlier-accumulated Pitta become aggravated?",
            ("When bodies used to the rains' cold are suddenly heated by the sun",
             "That is the condition in the verse: शीत का अभ्यास, then सहसा heat by the sun's rays."),
            [("When bodies used to the sun's heat are suddenly chilled by the rain",
              "The verse has it the other way round: used to cold, then heated."),
             ("When bodies used to the rains' cold are slowly warmed, step by step",
              "सहसा means suddenly, not slowly."),
             ("When bodies used to the rains' cold stay in the cold for long",
              "The verse speaks of heating by the sun's rays, not of staying in the cold.")],
            "The verse joins वर्षाशीतोचितांगानाम् with सहसा … अर्करश्मिभिः तप्तानाम्: used to the rains' cold, suddenly heated by the sun's rays.",
            "Used to the rains' cold + suddenly heated by sun-rays → earlier-accumulated Pitta is aggravated."),
        match(1, "Match each word of the verse to its meaning.",
              [["सहसा", "suddenly"], ["तप्तानाम्", "of those heated"],
               ["संचितम्", "accumulated"], ["प्रकुप्यति", "becomes aggravated"]],
              "These four words carry the whole event: sudden, heated, accumulated, aggravated.",
              "सहसा = suddenly; तप्तानाम् = of those heated; संचितम् = accumulated; प्रकुप्यति = becomes aggravated."),
        fill(2, "The dosha that the verse says becomes aggravated is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("पित्तम्"),
             "पित्तम् is the subject of प्रकुप्यति: it is the Pitta that was accumulated earlier.",
             "In this verse the aggravated dosha is पित्तम् (neuter nominative singular), qualified by संचितम् 'accumulated'.",
             "पित्तम् = Pitta, the subject of प्रकुप्यति."),
        mcq("discriminate", 3, "Which is the right split of सहसैव?",
            ("सहसा + एव",
             "आ + ए → ऐ, so सहसा + एव is written सहसैव."),
            [("सहसा + अव", "आ + अ would give सहसाव, not सहसैव."),
             ("सहसि + एव", "इ + ए would give सहस्येव."),
             ("सहसो + एव", "ओ + ए would give सहसवेव.")],
            "सहसा 'suddenly' + एव 'just': the two join as ऐ.",
            "आ + ए → ऐ (सहसा + एव = सहसैव)."),
        order(4, "Put these phrases of the verse in the order in which they stand.",
              ["वर्षाशीतोचितांगानां", "सहसैवार्करश्मिभिः", "तप्तानां",
               "संचितं पूर्वं", "तदा पित्तं प्रकुप्यति"],
              "The verse runs: those used to the rains' cold, suddenly by the sun's rays, heated, accumulated earlier, then Pitta is aggravated.",
              "वर्षाशीतोचितांगानाम् · सहसैवार्करश्मिभिः · तप्तानाम् · संचितं पूर्वम् · तदा पित्तं प्रकुप्यति.",
              role="apply"),
        mcq("transfer", 5,
            "An invented phrase says ग्रीष्मोचितांगानाम्. What does it mean?",
            ("Of those whose bodies are used to summer",
             "X-उचित-अंग names bodies used to X, as in वर्षाशीतोचितांगानाम्."),
            [("Of those whose bodies are hurt by summer",
              "उचित means suited or used to, not hurt."),
             ("Of those who have left summer behind",
              "Nothing in the compound means leaving behind."),
             ("Of those who measure summer",
              "Nothing in the compound means measuring.")],
            "ग्रीष्म + उचित → ग्रीष्मोचित (अ + उ → ओ): used to summer; then अंग 'body' and the genitive plural.",
            "शीत + उचित = शीतोचित (अ + उ → ओ); X-उचित-अंग = (those) whose bodies are used to X.",
            teaches="A compound X-उचितांग names those whose bodies are used to X: वर्षाशीतोचितांग, and the invented ग्रीष्मोचितांग; अ + उ joins as ओ."),
    ],
}

# ---------------------------------------------------------------- unit 69
AUTHORED["69"] = {
    "title": "शस्तं तिक्तैर्हविःपानं",
    "question": "Which procedures and foods does this unit call recommended?",
    "rule": ("Recommended (शस्तम्) are purgation (विरेक), the flow of blood "
             "(अस्रश्रुति), cold and light food and drink, and what is astringent, "
             "sweet and bitter."),
    "limits": ("The first item (तिक्तैहविःपानम्) is misprinted; reading it as ghee "
               "prepared with bitters is an inference, so no question rests on it. "
               "Whether सदा 'always' belongs to the first or second half is open. "
               "The verse gives no dose and no condition for any item."),
    "explain_hi": ("इस श्लोक में ‘शस्तम्’ (प्रशस्त) कहकर कुछ बातें गिनाई गई हैं। पहली पंक्ति में "
                   "विरेचन (विरेक) और रक्त का निकलना (अस्रश्रुति) हैं; पंक्ति का पहला सामासिक "
                   "शब्द (तिक्तैहविःपानम्) छपाई में बिगड़ा है, इसलिए उस पर प्रश्न नहीं बने। "
                   "दूसरी पंक्ति में शीतल और हल्का अन्न-पान है, और कषाय, मधुर तथा तिक्त पदार्थ। "
                   "श्लोक न मात्रा बताता है, न यह कि किसके लिए, इसलिए केवल यही कहा गया है कि ये प्रशस्त हैं।"),
    "hook": "प्रशस्त: विरेक, रक्त-स्राव, शीतल-हल्का अन्न-पान; कषाय-मधुर-तिक्त।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Which of these does the unit name among the recommended things?",
            ("Purgation (विरेक)",
             "विरेकः is named in the first line with शस्तम्."),
            [("Steaming (स्वेद)", "Steaming is not named in this unit."),
             ("Oil massage (अभ्यंग)", "Oil massage is not named in this unit."),
             ("Fasting (उपवास)", "Fasting is not named in this unit.")],
            "The first line names the flow of blood and विरेकः, purgation, as recommended.",
            "शस्तम् (recommended) governs: विरेक, अस्रश्रुति, शीतं लघ्वन्नपानम्, कषायस्वादुतिक्तकम्."),
        match(1, "Match each word to its meaning.",
              [["शस्तम्", "recommended"], ["विरेकः", "purgation"],
               ["अस्रश्रुतिः", "flow of blood"], ["लघु", "light"],
               ["शीतम्", "cold"]],
              "Five words of the list carry its meaning.",
              "शस्तम् = recommended; विरेकः = purgation; अस्रश्रुतिः = flow of blood; लघु = light; शीतम् = cold."),
        fill(2, "The word for 'purgation' is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("विरेकः"),
             "विरेकः (purgation) is the second item of the first line.",
             "विरेकः is a masculine nominative singular, 'purgation', one of the things called recommended.",
             "विरेकः = purgation."),
        mcq("discriminate", 3, "Which is the right split of विरेकोऽस्रश्रुतिः?",
            ("विरेकः + अस्रश्रुतिः",
             "अः + अ → ओऽ (visarga becomes उ, joins अ to make ओ, and अ is dropped as ऽ)."),
            [("विरेकः + स्रश्रुतिः", "Then the second word would lack its first letter."),
             ("विरेको + ओस्रश्रुतिः", "ओऽ is one sign for both words; there is no extra ओ."),
             ("विरेकोः + अस्रश्रुतिः", "विरेकोः is not a form; the word is विरेकः.")],
            "विरेकः 'purgation' + अस्रश्रुतिः 'flow of blood'.",
            "अः + अ → ओऽ (विरेकः + अस्रश्रुतिः = विरेकोऽस्रश्रुतिः)."),
        order(4, "Put these items in the order of the verse (leaving out the first, misprinted item).",
              ["विरेकः", "अस्रश्रुतिः", "शीतं", "लघ्वन्नपानं", "कषायस्वादुतिक्तकं"],
              "After the misprinted first item the verse lists purgation, flow of blood, cold, light food and drink, then astringent-sweet-bitter.",
              "विरेकः · अस्रश्रुतिः · शीतम् · लघ्वन्नपानम् · कषायस्वादुतिक्तकम्.",
              role="apply"),
        mcq("transfer", 5,
            "An invented phrase says मृद्वन्नम्, on the pattern of लघ्वन्नम्. What does it mean?",
            ("Soft food",
             "A describing word first, then the noun: soft + food."),
            [("Food of the soft", "That would put मृदु in the genitive; here it stands as a plain first part."),
             ("No food", "Nothing in the word means 'no'."),
             ("Food that softens", "Nothing in the word means 'that makes'.")],
            "मृदु + अन्नम् → मृद्वन्नम् (उ + अ → व् + अ): soft food, as लघु + अन्न = लघ्वन्न 'light food'.",
            "Adjective + noun make one word (लघु + अन्न = लघ्वन्न 'light food'); उ before a different vowel → व्.",
            teaches="An adjective can join its noun in one word, with उ + अ → व्+अ: लघ्वन्न 'light food', the invented मृद्वन्न 'soft food'."),
    ],
}

# ---------------------------------------------------------------- unit 70
AUTHORED["70"] = {
    "title": "शालिषष्टिकगोधूम",
    "question": "Which foods does this list name?",
    "rule": ("A list: śāli and ṣaṣṭika rice, wheat, barley, mudga, sugar, honey; "
             "paṭola, āmalaka, grapes, and the flesh of dry-land animals."),
    "limits": ("The verse is a bare list; the word 'recommended' (शस्तम्) of "
               "unit 69 is understood. Whether 'bhṛśam' goes only with "
               "kṣudvatām ('very hungry') is open, so no question rests on "
               "it. Paṭola and āmalaka are kept as names; the verse says "
               "no more about them."),
    "explain_hi": ("यह श्लोक केवल एक सूची है, जो पिछली इकाई के ‘शस्तम्’ (प्रशस्त) से जुड़ती है। "
                   "पहली पंक्ति में शालि और षष्टिक चावल, गेहूँ, जौ, मूँग, सिता (शर्करा) और मधु हैं। "
                   "दूसरी पंक्ति में पटोल, आमलक (ये केवल नाम हैं), द्राक्षा और जांगल पशुओं का मांस है। "
                   "‘भृशम्’ संभवतः ‘क्षुद्वताम्’ के साथ है (बहुत भूखे लोगों के लिए), पर यह खुला है। "
                   "श्लोक किसी के गुण या मात्रा का वर्णन नहीं करता।"),
    "hook": "शालि-षष्टिक, गेहूँ, जौ, मूँग, सिता, मधु; पटोल, आमलक, द्राक्षा, जांगल।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Which of these foods does the unit name in its list?",
            ("Barley (यव)",
             "यव is in the first line, after गोधूम."),
            [("Sesame (तिल)", "Sesame is not named in this unit."),
             ("Mustard (सर्षप)", "Mustard is not named in this unit."),
             ("Black pepper (मरिच)", "Black pepper is not named in this unit.")],
            "The first line lists śāli, ṣaṣṭika, godhūma, yava (barley), mudga, sitā and madhu.",
            "First line: शालि, षष्टिक, गोधूम, यव, मुद्ग, सिता, मधु."),
        match(1, "Match each word of the list to its meaning.",
              [["गोधूम", "wheat"], ["यव", "barley"], ["सिता", "sugar"],
               ["मधु", "honey"], ["द्राक्षा", "grapes"]],
              "Five items of the list have clear meanings.",
              "गोधूम = wheat; यव = barley; सिता = sugar; मधु = honey; द्राक्षा = grapes."),
        fill(2, "The word for 'barley' is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("यव"),
             "यव is the fourth item of the first line.",
             "यव (barley) is one of the grains in the list, between गोधूम and मुद्ग.",
             "यव = barley."),
        mcq("discriminate", 3, "Which is the right translation of line 1?",
            ("Śāli and ṣaṣṭika rice, wheat, barley, mudga, sugar and honey",
             "Each word agrees with the glosses on the card."),
            [("Śāli and ṣaṣṭika rice, maize, barley, mudga, sugar and honey",
              "गोधूम is wheat, not maize."),
             ("Śāli and ṣaṣṭika rice, wheat, barley, mudga, salt and honey",
              "सिता is sugar, not salt."),
             ("Śāli and ṣaṣṭika rice, wheat, barley, mudga, sugar and milk",
              "मधु is honey, not milk.")],
            "Only one word differs in each wrong option: the right one keeps wheat, sugar and honey.",
            "गोधूम = wheat; सिता = sugar; मधु = honey."),
        order(4, "Put these five items in the order of the verse.",
              ["गोधूम", "यव", "मुद्ग", "सिता", "मधु"],
              "The first line runs godhūma, yava, mudga, sitā, madhu.",
              "गोधूम · यव · मुद्ग · सिता · मधु.", role="apply"),
        mcq("transfer", 5,
            "Which is the joined form of द्राक्षा + आमलकम् (invented list), on the pattern of पटोल + आमलक?",
            ("द्राक्षामलकम्",
             "आ + आ joins as one long आ, as अ + आ in पटोलामलक."),
            [("द्राक्षायामलकम्", "No य joins the two; the vowels merge."),
             ("द्राक्षेमलकम्", "आ + आ does not give ए."),
             ("द्राक्षाआमलकम्", "The vowels must merge, not stand side by side.")],
            "पटोल + आमलक → पटोलामलक; likewise द्राक्षा + आमलकम् → द्राक्षामलकम्.",
            "अ/आ + आ → आ (पटोल + आमलक = पटोलामलक).",
            teaches="अ or आ followed by आ joins as one long आ: पटोल + आमलक = पटोलामलक; the invented द्राक्षा + आमलकम् = द्राक्षामलकम्."),
    ],
}

# ---------------------------------------------------------------- unit 71
AUTHORED["71"] = {
    "title": "दिवा दिवाकरकरैः",
    "question": "What happens to the water by day and by night in this unit?",
    "rule": ("Water heated by the sun's rays by day, made cool by the moon's "
             "rays at night, and freed of poison by Agastya; the sentence "
             "goes on in unit 72."),
    "limits": ("The sentence has no verb here; it goes on in unit 72 (clear, "
               "pure, matured by time). 'ल्हादितम्' is probably 'ह्लादितम्', "
               "and 'अगस्तेन' is probably 'अगस्त्येन'; the verse says nothing "
               "more about Agastya, so no question rests on him."),
    "explain_hi": ("इस युग्म में एक जल का वर्णन शुरू होता है। दिन में वह सूर्य की किरणों से तपा हुआ है "
                   "(‘दिवा दिवाकरकरैः’) और रात में चंद्रमा की किरणों से शीतल किया हुआ "
                   "(‘निशाकरकरैर्निशि’)। इसके बाद कहा गया है कि वह अगस्त्य द्वारा विषरहित "
                   "किया गया है; अगस्त्य के बारे में श्लोक और कुछ नहीं कहता। वाक्य यहाँ पूरा नहीं होता, "
                   "अगली इकाई में जल के निर्मल, शुद्ध आदि गुण आते हैं।"),
    "hook": "दिन में सूर्य-किरणों से तपा, रात में चंद्र-किरणों से शीतल — वही जल।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Which rays does the unit name for the night?",
            ("The moon's rays",
             "निशाकरकरैः is 'by the moon's rays', with निशि 'at night'."),
            [("The sun's rays", "These are named for the day (दिवा)."),
             ("The stars' rays", "No stars are named."),
             ("The lamp's rays", "No lamp is named.")],
            "रात (निशि) goes with निशाकर, the moon, and its rays.",
            "दिवा = by day with the sun's rays; निशि = at night with the moon's rays."),
        match(1, "Match each word of the first line to its meaning.",
              [["दिवा", "by day"], ["निशि", "at night"],
               ["दिवाकरकरैः", "by the sun's rays"],
               ["निशाकरकरैः", "by the moon's rays"],
               ["तोयम्", "water"]],
              "Day pairs with the sun's rays, night with the moon's.",
              "दिवा = by day; निशि = at night; दिवाकरकरैः = by the sun's rays; निशाकरकरैः = by the moon's rays; तोयम् = water."),
        fill(2, "The word for 'water' in this unit is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("तोयम्"),
             "तोयम् is the subject of the sentence: the water that is heated, cooled and freed of poison.",
             "तोयम् is a neuter word for water; संतप्तम् and the other describing words agree with it.",
             "तोयम् = water."),
        mcq("discriminate", 3, "Which is the right split of निशाकरकरैर्निशि?",
            ("निशाकरकरैः + निशि",
             "ऐः before a soft consonant (here न) becomes ऐर्."),
            [("निशाकरकराः + निशि", "The word is in the instrumental plural -ऐः, not -आः."),
             ("निशाकरकरैर् + अनिशि", "There is no अनिशि; निशि stands as it is."),
             ("निशाकरकरैस् + निशि", "A visarga before a soft consonant becomes र्, not स्.")],
            "निशाकर-करैः 'by the moon's rays' + निशि 'at night'. The print puts a stray space after the earlier करै.",
            "ऐः + soft consonant → ऐर् (करैः + निशि = करैर्निशि)."),
        order(4, "Put these words in the order of the verse.",
              ["दिवा", "दिवाकरकरैः", "निशाकरकरैः", "निशि", "संतप्तं", "तोयं"],
              "The verse says: by day, by the sun's rays, by the moon's rays, at night, heated, water.",
              "दिवा · दिवाकरकरैः · निशाकरकरैः · निशि · संतप्तम् · तोयम्.", role="apply"),
        mcq("transfer", 5,
            "On the pattern of दिवाकर (sun) and निशाकर (moon), which word means the maker of the day, the sun?",
            ("दिनकरः",
             "X-कर 'maker of X': दिन 'day' + कर, as दिवा + कर in दिवाकर."),
            [("दिनान्तः", "This means the end of the day."),
             ("दिनभक्तः", "This would mean one devoted to the day."),
             ("दिनमासः", "This would join day and month.")],
            "दिवाकर and निशाकर show the pattern 'maker of the day / of the night'; दिनकर follows it.",
            "-कर at the end of a name: the maker of the first part (दिवाकर sun, निशाकर moon).",
            teaches="A name ending in -कर means 'maker of' the first part: दिवाकर 'day-maker' is the sun, निशाकर 'night-maker' the moon; the invented दिनकर follows the pattern."),
    ],
}

# ---------------------------------------------------------------- unit 72
AUTHORED["72"] = {
    "title": "निर्मलं शुचि कालेन",
    "question": "What four things does the first line say of the water?",
    "rule": ("The water is clear (निर्मल), pure (शुचि), matured by time "
             "(कालेन पक्व) and, to drink, like nectar (अमृतोपम)."),
    "limits": ("The sentence runs on from unit 71 into unit 73. Line 2 is one "
               "long locative word describing the lakes of unit 73; 'भ्रमद्ध्रमर' "
               "is a misprint of 'भ्रमद्भ्रमर'."),
    "explain_hi": ("यह इकाई पिछली इकाई का वाक्य आगे बढ़ाती है। पहली पंक्ति में जल के चार गुण हैं: "
                   "निर्मल (साफ़), शुचि (शुद्ध), कालेन पक्व (समय से परिपक्व) और पीने में अमृत के "
                   "समान। दूसरी पंक्ति एक लंबा सप्तमी शब्द है: जहाँ हंसों के झुंड के पंख फड़फड़ाने से "
                   "भौंरों की पंक्तियाँ मँडराती हैं; यह अगली इकाई के सरोवरों का विशेषण है।"),
    "hook": "निर्मल, शुचि, समय से पका, पीने में अमृत-सम — हंसों और भौंरों वाले सरोवरों का जल।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "How does the first line describe this water to drink?",
            ("Like nectar",
             "पाने ऽमृतोपमम् is 'in drinking, like nectar'."),
            [("Bitter as a bitter drug", "Nothing like this is said."),
             ("Sweet as honey", "The comparison is with nectar, not honey."),
             ("Salty as the sea", "Nothing like this is said.")],
            "अमृत-उपमम् means like nectar; पाने means in drinking.",
            "पाने अमृतोपमम् = like nectar to drink."),
        match(1, "Match each word of the first line to its meaning.",
              [["निर्मलम्", "clear"], ["शुचि", "pure"],
               ["कालेन", "by time"], ["पक्वम्", "matured"],
               ["अमृतोपमम्", "like nectar"]],
              "The first line is a string of five describing words.",
              "निर्मलम् = clear; शुचि = pure; कालेन = by time; पक्वम् = matured; अमृतोपमम् = like nectar."),
        order(2, "Put these four descriptions of the water in the order of the verse.",
              ["निर्मलं", "शुचि", "कालेन पक्वं", "पानेऽमृतोपमं"],
              "The line runs: clear, pure, matured by time, like nectar to drink.",
              "निर्मलम् · शुचि · कालेन पक्वम् · पानेऽमृतोपमम्.", role="extend",
              teaches="The water's four descriptions come in a fixed order: clear, pure, matured by time, like nectar to drink."),
        mcq("discriminate", 3, "Which is the right split of पानेऽमृतोपमम्?",
            ("पाने + अमृतोपमम्",
             "ए + अ keeps ए, and the lost अ is shown by ऽ."),
            [("पानो + अमृतोपमम्", "ओ is not the ending of पाने (locative of पान)."),
             ("पान + अमृतोपमम्", "This would be written पानामृतोपमम्."),
             ("पाने + मृतोपमम्", "मृत would change the sense to 'dead'.")],
            "पाने 'in drinking' + अमृतोपमम् 'like nectar'.",
            "ए + अ → ए, with the avagraha ऽ for the dropped अ."),
        multi("apply", 4, "Which TWO things does the first line say of the water?",
              [("It is pure (शुचि)", "Right: शुचि is named."),
               ("It is matured by time (कालेन पक्वम्)", "Right: कालेन पक्वम्."),
               ("It is boiled with spices", "Nothing is said of spices."),
               ("It is sweet as honey", "The line says like nectar, not like honey."),
               ("It is salty", "Nothing is said of salt.")],
              [0, 1],
              "Pure (शुचि) and matured by time (कालेन पक्वम्) are both in the line.",
              "The first line: clear, pure, matured by time, like nectar."),
        mcq("transfer", 5,
            "Which joined form of पद्म + उपमम् (invented) means like a lotus?",
            ("पद्मोपमम्",
             "अ + उ → ओ, as in अमृतोपमम्."),
            [("पद्मौपमम्", "औ would come from अ + औ."),
             ("पद्मुपमम्", "The अ would not simply vanish."),
             ("पद्मूपमम्", "अ + उ does not give ऊ.")],
            "अमृत + उपम → अमृतोपम; so पद्म + उपम → पद्मोपम.",
            "अ + उ → ओ (अमृत + उपम = अमृतोपम).",
            teaches="अ followed by उ joins as ओ: अमृत + उपम = अमृतोपम; the invented पद्म + उपम = पद्मोपम 'like a lotus'."),
    ],
}

# ---------------------------------------------------------------- unit 73
AUTHORED["73"] = {
    "title": "सरसीषु प्लवेत",
    "question": "How is one dressed and anointed, according to this unit?",
    "rule": ("One should swim in lakes, wearing light, clean clothes and a "
             "garland, and anointed with cool uśīra."),
    "limits": ("The first phrase (सुसरोरुहसेन्यासु, probably सेव्यासु) is "
               "uncertain, and प्लुवेत is probably प्लवेत; so questions use only "
               "'in lakes' and the second line. Uśīra is a name; the verse says "
               "no more about it."),
    "explain_hi": ("यह इकाई पिछली इकाइयों के जल और सरोवरों से जुड़ी है। पहली पंक्ति कहती है कि "
                   "सरोवरों में तैरना चाहिए (‘प्लवेत’ का रूप छपाई में बिगड़ा है, कमलों वाला अंश "
                   "भी अनिश्चित है)। दूसरी पंक्ति साफ़ है: वह व्यक्ति हल्के, शुद्ध वस्त्र और माला "
                   "धारण किए हो और शीतल उशीर का लेप लगाए हो। उशीर केवल नाम है।"),
    "hook": "सरोवर में तैरना; हल्के शुद्ध वस्त्र, माला, शीतल उशीर का लेप।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "With what is the person anointed, according to the second line?",
            ("Cool uśīra",
             "शीतोशीरविलेपनः is 'anointed with cool uśīra'."),
            [("Warm oil", "The anointing is cool, not warm."),
             ("Dry ash", "Ash is not named."),
             ("Plain water", "Water is not named for anointing.")],
            "शीत-उशीर-विलेपन: anointing with cool uśīra.",
            "शीतोशीरविलेपनः = anointed with cool uśīra."),
        match(1, "Match each word to its meaning.",
              [["सरसीषु", "in lakes"], ["लघु", "light"], ["शुद्ध", "clean"],
               ["स्रग्वी", "wearing a garland"], ["विलेपन", "anointing"]],
              "These words make up the two lines.",
              "सरसीषु = in lakes; लघु = light; शुद्ध = clean; स्रग्वी = wearing a garland; विलेपन = anointing."),
        order(2, "Put these phrases in the order of the verse (leaving out the unclear first phrase and the verb).",
              ["सरसीषु", "लघुशुद्धांबरस्रग्वी", "शीतोशीरविलेपनः"],
              "The verse goes: in lakes, with light clean clothes and a garland, anointed with cool uśīra.",
              "सरसीषु · लघुशुद्धांबरस्रग्वी · शीतोशीरविलेपनः.", role="extend",
              teaches="The verse's sequence is: in lakes, then light clean clothes and a garland, then the cool uśīra anointing."),
        mcq("discriminate", 3, "Which is the right split of शीतोशीर-?",
            ("शीत + उशीर",
             "अ + उ → ओ, so शीत + उशीर is written शीतोशीर."),
            [("शीतो + उशीर", "ओ + उ would give शीतवुशीर."),
             ("शीत + ओशीर", "There is no ओशीर here."),
             ("शीता + उशीर", "आ + उ also gives ओ, but शीता is not the word here.")],
            "शीत 'cool' + उशीर: the two vowels join as ओ.",
            "अ + उ → ओ (शीत + उशीर = शीतोशीर)."),
        multi("apply", 4, "Which TWO things does the second line say about the person's dress?",
              [("Light, clean clothes", "Right: लघुशुद्धांबर."),
               ("A garland", "Right: स्रग्वी."),
               ("Thick woollen cloth", "Not said."),
               ("No ornament at all", "A garland is named."),
               ("Dark-coloured clothes", "Colour is not said.")],
              [0, 1],
              "The compound लघुशुद्धांबरस्रग्वी gives light clean clothes and a garland.",
              "लघु-शुद्ध-अंबर-स्रग्वी = with light, clean clothes and a garland."),
        mcq("transfer", 5,
            "An invented word शीतचन्दनविलेपनः, on the pattern of शीतोशीरविलेपनः, means which?",
            ("One anointed with cool sandal paste",
             "-विलेपनः describes a person anointed with the first part."),
            [("One who sells sandal paste", "Nothing in the word means selling."),
             ("One who dislikes cool paste", "Nothing in the word means dislike."),
             ("One who made the sandal paste", "Nothing in the word means making.")],
            "The compound names the person by his anointing: cool + sandal + anointing.",
            "X-विलेपनः (a describing compound) = anointed with X.",
            teaches="A describing compound ending in -विलेपनः names a person anointed with the first part: शीतोशीरविलेपन, the invented शीतचन्दनविलेपन."),
    ],
}

# ---------------------------------------------------------------- unit 74
AUTHORED["74"] = {
    "title": "सेवेत चंद्रकिरणान्",
    "question": "What does the first line say one should do at nightfall?",
    "rule": ("At nightfall one should enjoy the moon's rays (सेवेत "
             "चंद्रकिरणान्), having resorted to the mansion (सौधमाश्रितः)."),
    "limits": ("The second line is a list of objects whose reading is "
               "doubtful (तृप्तिंदध्यातप…), and its verb 'avoid' is in unit 75. "
               "No question rests on that list. 'सौध' as a roof is an "
               "inference; the verse says mansion."),
    "explain_hi": ("पहली पंक्ति सीधी है: रात के आरंभ (प्रदोष) में सौध (महल) का आश्रय लेकर "
                   "चंद्रमा की किरणों का सेवन करना चाहिए (‘सेवेत’ विधिलिङ्)। दूसरी पंक्ति में "
                   "तृप्ति, दही, धूप, क्षार, चर्बी, तेल और पूर्व की हवाओं की सूची है, जिसकी क्रिया अगली "
                   "इकाई में है; उसका पाठ अनिश्चित है, इसलिए प्रश्न केवल पहली पंक्ति पर बने हैं।"),
    "hook": "प्रदोष में महल का आश्रय लेकर चंद्रकिरणों का सेवन।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "What does the first line say one should enjoy at nightfall?",
            ("The moon's rays",
             "सेवेत चंद्रकिरणान् प्रदोषे: should enjoy the moon-rays at nightfall."),
            [("The sun's rays", "The line speaks of the moon, not the sun."),
             ("The night's darkness", "Darkness is not named."),
             ("The lamp's light", "No lamp is named.")],
            "चंद्र-किरणान् is the object of सेवेत.",
            "सेवेत = should enjoy; चंद्रकिरणान् = the moon-rays; प्रदोषे = at nightfall."),
        match(1, "Match each word of the first line to its meaning.",
              [["सेवेत", "should enjoy"], ["चंद्रकिरणान्", "the moon's rays"],
               ["प्रदोषे", "at nightfall"], ["सौधम्", "mansion"],
               ["आश्रितः", "having resorted to"]],
              "Five words carry the line.",
              "सेवेत = should enjoy; चंद्रकिरणान् = the moon's rays; प्रदोषे = at nightfall; सौधम् = mansion; आश्रितः = having resorted to."),
        fill(2, "The word for 'at nightfall' is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("प्रदोषे"),
             "प्रदोषे is the locative: at the start of the night.",
             "प्रदोषे is a masculine locative singular, giving the time at which the rays are to be enjoyed.",
             "प्रदोषे = at nightfall."),
        mcq("discriminate", 3, "Which is the right split of सौधमाश्रितः?",
            ("सौधम् + आश्रितः",
             "A final म् simply carries onto the next vowel: म् + आ → मा."),
            [("सौध + माश्रितः", "माश्रित is not a word."),
             ("सौधमा + आश्रितः", "सौधमा is not a word."),
             ("सौधः + आश्रितः", "A visarga would give सौधाश्रितः or सौधो.")],
            "सौधम् 'mansion' + आश्रितः 'having resorted to'.",
            "म् + vowel → म with that vowel (सौधम् + आश्रितः = सौधमाश्रितः)."),
        order(4, "Put these phrases of line 1 in the order of the verse.",
              ["सेवेत", "चंद्रकिरणान्", "प्रदोषे", "सौधमाश्रितः"],
              "The line runs: should enjoy, the moon-rays, at nightfall, having resorted to the mansion.",
              "सेवेत · चंद्रकिरणान् · प्रदोषे · सौधमाश्रितः.", role="apply"),
        mcq("transfer", 5,
            "On the pattern of सेवेत 'should enjoy', what does लभेत (from लभ्) mean?",
            ("Should obtain",
             "-एत on a verb stem: the 'should' form, as सेवेत."),
            [("Obtained", "-एत does not make a past."),
             ("Will obtain", "-एत does not make a future."),
             ("Obtaining", "-एत does not make a participle.")],
            "सेवेत is a 3rd person singular optative middle; लभेत is the same kind of form.",
            "-एत (3rd sing. optative, middle) = 'should / may do'.",
            teaches="A verb stem + -एत gives the 'should' form (3rd singular, optative, middle): सेवेत 'should enjoy'; the invented लभेत 'should obtain'."),
    ],
}

# ---------------------------------------------------------------- unit 75
AUTHORED["75"] = {
    "title": "नित्यं सर्वरसाभ्यासः",
    "question": "What practice does the second line speak of?",
    "rule": ("Always there is practice of all the tastes (नित्यं "
             "सर्वरसाभ्यासः), with each taste's own predominance in each "
             "season (ऋतौ ऋतौ)."),
    "limits": ("Line 1 (तीक्ष्णमद्य… ‘should avoid’) is damaged: 'अनुषारान्' is "
               "probably 'तुषारान्', so no question uses it. Whether the "
               "predominance is each taste in its own season, or each season's "
               "own taste, is open; questions ask neither."),
    "explain_hi": ("पहली पंक्ति (तीक्ष्ण मद्य, दिन की नींद और पाला को छोड़ देना, ‘विवर्जयेत्’) "
                   "का पाठ बिगड़ा है, इसलिए उस पर प्रश्न नहीं बने। दूसरी पंक्ति साफ़ है: सदा सभी रसों का "
                   "अभ्यास हो (‘नित्यं सर्वरसाभ्यासः’), और ‘ऋतौ ऋतौ’ अर्थात् प्रत्येक ऋतु में "
                   "अपने-अपने रस की अधिकता रहे। ‘किस ऋतु में कौन-सा रस’ यह श्लोक यहाँ नहीं कहता।"),
    "hook": "सदा सब रसों का अभ्यास; हर ऋतु में अपने-अपने रस की प्रधानता।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "What is to be practised at all times, according to the second line?",
            ("All the tastes",
             "सर्वरसाभ्यासः is the practice of all the tastes."),
            [("Only the sweet taste", "The line says all the tastes."),
             ("Only the bitter taste", "The line says all the tastes."),
             ("No taste at all", "The line asks for practice, not for giving them up.")],
            "सर्व-रस-अभ्यासः = practice of all the tastes, नित्यम् always.",
            "नित्यं सर्वरसाभ्यासः = always practice of all the tastes."),
        match(1, "Match each word of line 2 to its meaning.",
              [["नित्यम्", "always"], ["सर्व", "all"], ["रस", "taste"],
               ["अभ्यासः", "practice"], ["ऋतौ", "in the season"]],
              "These words carry the second line.",
              "नित्यम् = always; सर्व = all; रस = taste; अभ्यासः = practice; ऋतौ = in the season."),
        fill(2, "The first word of line 2, meaning constantly, is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("नित्यम्"),
             "नित्यम् opens the second line.",
             "नित्यम् is an indeclinable word, 'always'; it is the first word of the line.",
             "नित्यम् = always."),
        mcq("discriminate", 3, "Which split fits सर्वरसाभ्यासः (all + taste + practice)?",
            ("सर्व + रस + अभ्यासः",
             "अ + अ → आ: रस + अभ्यास is written रसाभ्यास."),
            [("सर्व + रसा + भ्यासः", "भ्यासः is not a word."),
             ("सर्व + रसाभ + यासः", "यासः would not give practice."),
            ("सर्वर + साभ्यासः", "सर्वर is not a word.")],
            "Three words join: सर्व 'all', रस 'taste', अभ्यास 'practice'.",
            "अ + अ → आ (रस + अभ्यास = रसाभ्यास)."),
        order(4, "Put these phrases of line 2 in the order of the verse.",
              ["नित्यं", "सर्वरसाभ्यासः", "स्वस्वाधिक्यं", "ऋतावृतौ"],
              "The line runs: always, practice of all tastes, each one's own predominance, in each season.",
              "नित्यम् · सर्वरसाभ्यासः · स्वस्वाधिक्यम् · ऋतावृतौ.", role="apply"),
        mcq("transfer", 5,
            "On the pattern of ऋतौ ऋतौ, what does the invented दिने दिने mean?",
            ("Each day, day by day",
             "Saying the word twice means 'in each'."),
            [("In one day only", "Doubling does not mean 'only'."),
             ("At the end of the day", "Doubling does not mean 'end'."),
             ("In two days", "Doubling does not mean two.")],
            "ऋतौ ऋतौ is 'in each season'; so दिने दिने is 'in each day'.",
            "A word said twice (ऋतौ ऋतौ) = 'in each'.",
            teaches="Saying a word twice gives 'each / every': ऋतौ ऋतौ 'in each season'; the invented दिने दिने 'each day'."),
    ],
}

# ---------------------------------------------------------------- unit 76
AUTHORED["76"] = {
    "title": "ऋत्वोरंत्यादिसप्ताहात्",
    "question": "What is the ṛtusaṃdhi, and what happens to the regimen there?",
    "rule": ("The last seven days of one season and the first seven days of the "
             "next are the ṛtusaṃdhi; there the former regimen is to be given up "
             "and the latter taken up, step by step (क्रमात्)."),
    "limits": ("The verse says 'given up' and 'taken up' in due order; it does "
               "not say how long each step lasts nor what the regimens are. The "
               "ablative in अंत्यादिसप्ताहात् is loose."),
    "explain_hi": ("यहाँ ‘ऋतुसंधि’ की परिभाषा है: दो ऋतुओं के अंतिम और आरंभिक सात-सात दिन ऋतुसंधि "
                   "कहे गए हैं। दूसरी पंक्ति बताती है कि वहाँ पूर्व (पहली ऋतु की) विधि छोड़नी "
                   "चाहिए (‘त्याज्यः’) और बाद वाली अपनानी चाहिए (‘सेवनीयः’), और यह ‘क्रमात्’ "
                   "यानी क्रम से हो। श्लोक यह नहीं बताता कि कौन-सी विधियाँ हैं या हर चरण कितना लंबा है।"),
    "hook": "दो ऋतुओं के अंतिम-आरंभिक सात-सात दिन: ऋतुसंधि; पूर्व विधि छोड़ो, उत्तर क्रम से अपनाओ।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "What does this unit call the ṛtusaṃdhi?",
            ("The last seven days of one season and the first seven of the next",
             "ऋत्वोः अंत्यादिसप्ताहात्: from the last and first seven days of the two seasons."),
            [("The first seven days of each season only",
              "Both the last and the first days are counted."),
             ("The whole month that lies between two seasons",
              "The unit counts seven days, not a month."),
             ("The seven middle days of one season",
              "The days named are at the end and the start.")],
            "अंत्य and आदि fix the last and the first seven days of two seasons.",
            "ऋतुसंधि = last seven days of one season + first seven days of the next."),
        match(1, "Match each word of the verse to its meaning.",
              [["ऋतुसंधिः", "junction of seasons"], ["स्मृतः", "is called"],
               ["पूर्वः", "former"], ["अपरः", "latter"],
               ["क्रमात्", "in due order"]],
              "Five words carry the definition and the rule.",
              "ऋतुसंधिः = junction of seasons; स्मृतः = is called; पूर्वः = former; अपरः = latter; क्रमात् = in due order."),
        order(2, "Put these phrases of line 2 in the order of the verse.",
              ["तत्र", "पूर्वो विधिस्त्याज्यः", "सेवनीयोऽपरः", "क्रमात्"],
              "Line 2: there, the former regimen to be given up, the latter to be taken up, in order.",
              "तत्र · पूर्वो विधिस्त्याज्यः · सेवनीयोऽपरः · क्रमात्.", role="extend",
              teaches="At the junction, the former regimen is given up first and the latter taken up, in due order."),
        mcq("discriminate", 3, "Which is the right split of सप्ताहादृतुसंधिः?",
            ("सप्ताहात् + ऋतुसंधिः",
             "A final त् before a vowel becomes द्, so सप्ताहात् + ऋतु is written सप्ताहादृतु."),
            [("सप्ताहाद् + दृतुसंधिः", "दृतु is not a word."),
             ("सप्ताहाः + ऋतुसंधिः", "A visarga would not give द्."),
             ("सप्ताहा + दृतुसंधिः", "दृतु is not a word.")],
            "सप्ताहात् 'from the seven days' + ऋतुसंधिः.",
            "Final त् + vowel → द् (सप्ताहात् + ऋतु = सप्ताहादृतु)."),
        multi("apply", 4, "Which TWO statements does this unit make?",
              [("The former season's regimen is to be given up", "Right: पूर्वो विधिस्त्याज्यः."),
               ("The latter regimen is to be taken up in due order", "Right: सेवनीयोऽपरः क्रमात्."),
               ("The latter regimen is to be given up", "It is the former that is given up."),
               ("The junction lasts a whole month", "Seven days at each end are named."),
               ("The junction is the middle of a season", "It is the end of one and the start of the next.")],
              [0, 1],
              "The second line gives up the former and takes up the latter, in order.",
              "पूर्वः विधिः त्याज्यः; अपरः सेवनीयः क्रमात्."),
        mcq("transfer", 5,
            "On the pattern of सेवनीयः 'to be taken up', what does the invented पठनीयः mean?",
            ("To be read",
             "-अनीय makes a 'should be done' word."),
            [("A reader", "A person who reads would end in -क."),
             ("Having read", "'Having read' would end in -त्वा."),
             ("Reading", "-अनीय does not make 'reading'.")],
            "सेवनीय and त्याज्य both say 'ought to be done'; पठनीय says 'ought to be read'.",
            "-अनीय or -य on a verb = 'to be done' (सेवनीयः, त्याज्यः).",
            teaches="A verb stem + -अनीय (or -य) gives 'to be done': सेवनीयः 'to be taken up', त्याज्यः 'to be given up'; the invented पठनीयः 'to be read'."),
    ],
}

# ---------------------------------------------------------------- unit 77
AUTHORED["77"] = {
    "title": "असात्म्यजा हि रोगाः",
    "question": "From what may diseases born of unsuitability arise, according to this unit?",
    "rule": ("Diseases born of unsuitability (असात्म्य) may arise from "
             "abruptly abandoning and taking up (सहसा त्यागशीलनात्); in "
             "seasons of such a kind this is the regimen for health."),
    "limits": ("The verse says 'may be' (स्युः): it does not name the diseases. "
               "'In seasons of such a kind' is contrasted with 'those of another "
               "form' only in unit 78, whose text is damaged, so no question "
               "uses that contrast."),
    "explain_hi": ("यह श्लोक पिछली इकाई के नियम का कारण देता है। ‘हि’ (क्योंकि) के साथ कहा गया है कि "
                   "सहसा त्याग और ग्रहण (‘त्यागशीलनात्’) से असात्म्य से उत्पन्न रोग हो सकते "
                   "हैं (‘स्युः’)। दूसरी पंक्ति कहती है कि इस प्रकार की ऋतुओं में ही देहधारियों के "
                   "स्वास्थ्य के लिए यह विधि है। रोग कौन-से हैं, यह श्लोक नहीं बताता।"),
    "hook": "क्योंकि अचानक छोड़ने-अपनाने से असात्म्य-जन्य रोग हो सकते हैं।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "From what may diseases born of unsuitability arise, according to this verse?",
            ("From abruptly abandoning and taking up",
             "सहसा त्यागशीलनात् is 'from abandoning and taking up, suddenly'."),
            [("From changing slowly, step by step",
              "सहसा means suddenly; the step by step change is in unit 76."),
             ("From keeping to one regimen unchanged",
              "The verse speaks of abandoning and taking up, not of keeping on."),
             ("From eating at the wrong hour",
              "The verse says nothing about the hour of eating.")],
            "त्याग-शीलन is abandoning and taking up; सहसा makes it abrupt.",
            "असात्म्यजाः रोगाः (diseases born of unsuitability) स्युः सहसा त्यागशीलनात्."),
        match(1, "Match each word to its meaning.",
              [["असात्म्यजाः", "born of unsuitability"], ["रोगाः", "diseases"],
               ["सहसा", "suddenly"], ["त्यागशीलनात्", "from abandoning and taking up"],
               ["देहिनाम्", "of embodied beings"]],
              "Five words carry the verse.",
              "असात्म्यजाः = born of unsuitability; रोगाः = diseases; सहसा = suddenly; त्यागशीलनात् = from abandoning and taking up; देहिनाम् = of embodied beings."),
        fill(2, "The word for 'suddenly' is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("सहसा"),
             "सहसा is in line 1, before त्यागशीलनात्.",
             "सहसा is an indeclinable word, 'suddenly'; it says how the abandoning and taking up is done.",
             "सहसा = suddenly."),
        mcq("discriminate", 3, "Which is the right split of ऋतुष्वेवंविधेष्वेव?",
            ("ऋतुषु + एवंविधेषु + एव",
             "उ before a different vowel becomes व्: ऋतुषु + एवं → ऋतुष्वेवं."),
            [("ऋतुष्व + एवंविधेष्व + एव", "These pieces are not words."),
             ("ऋतुषो + एवंविधेषो + एव", "ओ before ए would give अव, not व्."),
             ("ऋतुष + एवंविध + एव", "The locative plural -षु would be lost.")],
            "ऋतुषु 'in the seasons', एवंविधेषु 'of such a kind', एव 'indeed'.",
            "उ + different vowel → व् + vowel (ऋतुषु + एवं = ऋतुष्वेवं)."),
        order(4, "Put these phrases in the order of the verse.",
              ["असात्म्यजा हि रोगाः स्युः", "सहसा त्यागशीलनात्",
               "ऋतुष्वेवंविधेष्वेव", "विधिः स्वास्थ्ये च देहिनां"],
              "The verse gives the disease first, its cause, then the seasons of such a kind, then the regimen for health.",
              "असात्म्यजा हि रोगाः स्युः · सहसा त्यागशीलनात् · ऋतुष्वेवंविधेष्वेव · विधिः स्वास्थ्ये च देहिनाम्.",
              role="apply"),
        mcq("transfer", 5,
            "On the pattern of असात्म्यजाः, what does the invented जलजाः mean?",
            ("Born of water",
             "-ज at the end of a compound means 'born of' the first part."),
            [("Dwelling in water", "'Dwelling' would be a different ending."),
             ("Giving water", "'Giving' would be a different ending."),
             ("Without water", "'Without' would be a different word.")],
            "असात्म्य-जाः is 'born of unsuitability'; जल-जाः is 'born of water'.",
            "X-ज = born of X (असात्म्यज).",
            teaches="A word ending in -ज names what is born of the first part: असात्म्यजाः 'born of unsuitability'; the invented जलजाः 'born of water'."),
    ],
}

# ---------------------------------------------------------------- unit 78
AUTHORED["78"] = {
    "title": "निर्दिश्यतेऽन्यरूपेषु",
    "question": "What does line 1 say is prescribed, and in which seasons?",
    "rule": ("Line 1: a regimen (विधिः) is prescribed (निर्दिश्यते) in those of "
             "another form (अन्यरूपेषु). The word between is unclear, and "
             "line 2 is damaged."),
    "limits": ("Low confidence. The word 'विरुद्धज्ञानिक' is unexplained, and "
               "line 2 (मासराशिखरूपारुथ…) is garbled; the editors' reading "
               "'month, rāśi and own form, the triad of marks of the season' is "
               "only a suggestion. Questions use only the clear words निर्दिश्यते, "
               "अन्यरूपेषु and विधिः. The sentence runs on into unit 79."),
    "explain_hi": ("यह इकाई गहरी क्षतिग्रस्त है, इसलिए यहाँ केवल साफ़ शब्दों को लिया गया है। पहली "
                   "पंक्ति में ‘निर्दिश्यते’ (बताई जाती है), ‘अन्यरूपेषु’ (अन्य रूप वालों में) और "
                   "‘विधिः’ (विधि) साफ़ हैं। बीच का शब्द ‘विरुद्धज्ञानिकः’ समझ में नहीं आता। दूसरी "
                   "पंक्ति में ‘लक्षणत्रयम्’ (तीन लक्षण) जैसे टुकड़े दिखते हैं, पर पूरा पाठ संपादकों का "
                   "सुझाव ही है। वाक्य अगली इकाई तक चलता है।"),
    "hook": "(अस्पष्ट इकाई) साफ़ शब्द: निर्दिश्यते · अन्यरूपेषु · विधिः।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "What does the verb निर्दिश्यते in line 1 mean?",
            ("Is prescribed",
             "A present passive, third person singular: it is prescribed."),
            [("Was prescribed", "The form is present, not past."),
             ("Will prescribe", "The form is passive, not future."),
             ("Prescribes", "The form is passive: it is prescribed, not 'he prescribes'.")],
            "निर्दिश्यते is a 3rd sing. present passive of निस्-दिश्: 'is prescribed'.",
            "-यते on a verb stem makes the present passive: निर्दिश्यते = is prescribed."),
        match(1, "Match each clear word of line 1 to its meaning.",
              [["निर्दिश्यते", "is prescribed"],
               ["अन्यरूपेषु", "in those of another form"],
               ["विधिः", "regimen"], ["अन्य", "other"]],
              "These four are the clear words of line 1.",
              "निर्दिश्यते = is prescribed; अन्यरूपेषु = in those of another form; विधिः = regimen; अन्य = other."),
        fill(2, "The word for 'regimen' in line 1 is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("विधिः"),
             "विधिः is the subject of निर्दिश्यते.",
             "विधिः (regimen, masculine nominative singular) is what is prescribed.",
             "विधिः = regimen."),
        mcq("discriminate", 3, "Which is the right split of निर्दिश्यतेऽन्यरूपेषु?",
            ("निर्दिश्यते + अन्यरूपेषु",
             "ए + अ keeps ए, and ऽ shows the dropped अ."),
            [("निर्दिश्यतो + अन्यरूपेषु", "ओ is not the ending of the verb."),
             ("निर्दिश्यत + अन्यरूपेषु", "The verb ends in -ते."),
             ("निर्दिश्यते + न्यरूपेषु", "न्यरूप is not a word.")],
            "The verb निर्दिश्यते + अन्यरूपेषु 'in those of another form'.",
            "ए + अ → ए, with the avagraha ऽ for the dropped अ."),
        order(4, "Put these clear words of line 1 in the order of the verse (leaving out the unclear word).",
              ["निर्दिश्यते", "अन्यरूपेषु", "विधिः"],
              "Line 1 runs: is prescribed, in those of another form, (unclear word), regimen.",
              "निर्दिश्यते · अन्यरूपेषु · विधिः.", role="apply"),
        mcq("transfer", 5,
            "On the pattern of निर्दिश्यते 'is prescribed', which invented form means 'is read'?",
            ("पठ्यते",
             "-यते on the stem gives the 'is done' (present passive) form."),
            [("पठति", "This is the active: he reads."),
             ("पठेत", "This is the 'should' form: should read."),
             ("अपठत्", "This is a past: he read.")],
            "निर्दिश्यते is a present passive; पठ्यते (from पठ्) is the same kind.",
            "Present passive: stem + -यते (निर्दिश्यते, पठ्यते).",
            teaches="A present passive ends in -यते: निर्दिश्यते 'is prescribed'; the invented पठ्यते 'is read'."),
    ],
}

# ---------------------------------------------------------------- unit 79
AUTHORED["79"] = {
    "title": "यथोत्तरं भजेच्चर्यां",
    "question": "What is one to follow in succession?",
    "rule": ("One should follow the regimen (चर्याम्) in order of succession "
             "(यथोत्तरम्); 'there, because of its strength'."),
    "limits": ("The sentence completes unit 78, whose text is damaged. What "
               "'तस्य' (of that) refers to, and so what the strength belongs to, "
               "is not clear from the lines; no question rests on it."),
    "explain_hi": ("यह इकाई पिछली इकाई का वाक्य पूरा करती है। ‘यथोत्तरम्’ का अर्थ है उत्तरोत्तर "
                   "क्रम से; ‘भजेत् चर्याम्’ का अर्थ है चर्या का पालन करना चाहिए। ‘तत्र तस्य "
                   "बलात्’ (वहाँ उसके बल के कारण) में ‘तस्य’ किसके लिए है, यह इन पंक्तियों से साफ़ "
                   "नहीं होता; इसलिए उस पर प्रश्न नहीं बने।"),
    "hook": "उत्तरोत्तर क्रम से चर्या का पालन — वाक्य पिछली इकाई से आता है।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "What does the verse say one should follow in succession?",
            ("The regimen (चर्या)",
             "भजेत् चर्याम्: should follow the regimen."),
            [("The medicine (औषध)", "The word is चर्याम्, regimen."),
             ("The junction of seasons", "The junction is in unit 76; here it is the regimen."),
             ("The strength of the body", "बलात् is 'by strength', not what is followed.")],
            "भजेत् 'should follow' has चर्याम् 'regimen' as its object.",
            "यथोत्तरं भजेत् चर्याम् = one should follow the regimen in succession."),
        match(1, "Match each word of the verse to its meaning.",
              [["यथोत्तरम्", "in order of succession"],
               ["भजेत्", "should follow"], ["चर्याम्", "regimen"],
               ["तत्र", "there"], ["बलात्", "by strength"]],
              "Five words carry the verse.",
              "यथोत्तरम् = in order of succession; भजेत् = should follow; चर्याम् = regimen; तत्र = there; बलात् = by strength."),
        fill(2, "The word for 'regimen' in this verse is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("चर्याम्"),
             "चर्याम् is the object of भजेत्.",
             "चर्याम् is the feminine accusative singular of चर्या, 'regimen'.",
             "चर्याम् = regimen (accusative)."),
        mcq("discriminate", 3, "Which is the right split of भजेच्चर्याम्?",
            ("भजेत् + चर्याम्",
             "A final त् before च becomes च्, so भजेत् + चर्याम् is written भजेच्चर्याम्."),
            [("भजे + चर्याम्", "This would be written भजेचर्याम्, with one च."),
             ("भजेः + चर्याम्", "A visarga would not make च्च."),
             ("भजेच + र्याम्", "र्याम् is not a word.")],
            "भजेत् 'should follow' + चर्याम् 'regimen'.",
            "त् + च → च्च (भजेत् + चर्याम् = भजेच्चर्याम्)."),
        order(4, "Put these parts of the verse in order.",
              ["यथोत्तरं", "भजेच्चर्यां", "तत्र", "तस्य", "बलादिति"],
              "The verse runs: in succession, should follow the regimen, there, of that, by strength, thus.",
              "यथोत्तरम् · भजेच्चर्याम् · तत्र · तस्य · बलादिति.", role="apply"),
        mcq("transfer", 5,
            "Which is the joined form of यथा + उक्तम् (invented), on the pattern of यथोत्तरम्?",
            ("यथोक्तम्",
             "आ + उ joins as ओ, as in यथा + उत्तरम्."),
            [("यथूक्तम्", "आ + उ does not give ऊ."),
             ("यथौक्तम्", "औ would come from आ + औ."),
            ("यथाउक्तम्", "The vowels must join.")],
            "यथा + उत्तरम् → यथोत्तरम्; likewise यथा + उक्तम् → यथोक्तम्.",
            "अ/आ + उ → ओ (यथा + उत्तरम् = यथोत्तरम्).",
            teaches="अ or आ followed by उ joins as ओ: यथा + उत्तरम् = यथोत्तरम्; the invented यथा + उक्तम् = यथोक्तम् 'as said'."),
    ],
}

# ---------------------------------------------------------------- unit 80
AUTHORED["80"] = {
    "title": "इति ऋतुचर्यानाम",
    "question": "What does the closing line say about the chapter?",
    "rule": ("Closing line: 'Thus the fourth chapter, named Ṛtucaryā.' (इति "
             "ऋतुचर्यानाम चतुर्थोऽध्यायः)."),
    "limits": "The colophon only names the chapter and its number.",
    "explain_hi": ("यह अध्याय का समापन-वाक्य है: ‘इस प्रकार ऋतुचर्या नामक चौथा अध्याय’। "
                   "इसमें केवल अध्याय का नाम (ऋतुचर्या) और क्रम (चौथा) बताया गया है।"),
    "hook": "इति ऋतुचर्या नाम चौथा अध्याय।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "What does the closing line say the chapter is?",
            ("The fourth chapter, named Ṛtucaryā",
             "ऋतुचर्यानाम चतुर्थोऽध्यायः is exactly that."),
            [("The third chapter, named Ṛtucaryā", "चतुर्थ is fourth, not third."),
             ("The fourth chapter, named Dinacaryā", "The name in the line is ऋतुचर्या."),
             ("The fifth chapter, named Ṛtucaryā", "चतुर्थ is fourth, not fifth.")],
            "The colophon gives the name ऋतुचर्या and the number चतुर्थ.",
            "इति ऋतुचर्यानाम चतुर्थोऽध्यायः = Thus the fourth chapter, named Ṛtucaryā."),
        match(1, "Match each word of the closing line to its meaning.",
              [["इति", "thus"], ["नाम", "named"], ["चतुर्थः", "fourth"],
               ["अध्यायः", "chapter"]],
              "Four words make up the closing line, with the name.",
              "इति = thus; नाम = named; चतुर्थः = fourth; अध्यायः = chapter."),
        fill(2, "The word for 'chapter' is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("अध्यायः"),
             "अध्यायः is the last word before the number.",
             "अध्यायः (masculine nominative singular) is 'chapter'.",
             "अध्यायः = chapter."),
        mcq("discriminate", 3, "Which is the right split of चतुर्थोऽध्यायः?",
            ("चतुर्थः + अध्यायः",
             "अः + अ → ओऽ."),
            [("चतुर्थ + ओध्यायः", "ओध्यायः is not a word."),
             ("चतुर्थो + अध्यायः", "Then the ऽ would not stand."),
             ("चतुर्थाः + अध्यायः", "The ending would then give चतुर्था अध्यायः.")],
            "चतुर्थः 'fourth' + अध्यायः 'chapter'.",
            "अः + अ → ओऽ (चतुर्थः + अध्यायः = चतुर्थोऽध्यायः)."),
        order(4, "Put these parts of the closing line in order.",
              ["इति", "ऋतुचर्यानाम", "चतुर्थोऽध्यायः"],
              "The line runs: thus, named Ṛtucaryā, the fourth chapter.",
              "इति · ऋतुचर्यानाम · चतुर्थोऽध्यायः.", role="apply"),
        mcq("transfer", 5,
            "What is the joined form of तृतीयः + अध्यायः (third chapter)?",
            ("तृतीयोऽध्यायः",
             "अः + अ → ओऽ, as in चतुर्थोऽध्यायः."),
            [("तृतीयाध्यायः", "This drops the visarga without the ओऽ rule."),
             ("तृतीयेऽध्यायः", "ए is not the join of अः + अ."),
             ("तृतीयःअध्यायः", "The two words must join.")],
            "चतुर्थः + अध्यायः → चतुर्थोऽध्यायः; the same for तृतीयः.",
            "अः + अ → ओऽ.",
            teaches="A word in -अः followed by अ joins as ओऽ: चतुर्थः + अध्यायः = चतुर्थोऽध्यायः; the invented तृतीयः + अध्यायः = तृतीयोऽध्यायः."),
    ],
}

NOTES_HI = {
    "68": "विश्वास: उच्च। संधि जाँची: वर्षाशीतोचितांगानाम् = वर्षा + शीत + उचित + अंग (अ + उ → ओ); सहसैव = सहसा + एव (आ + ए → ऐ)। ‘प्रकुप्यति’ वर्तमान, परस्मैपद। कोई पाठभेद या पाठ-दोष नहीं।",
    "69": "विश्वास: मध्यम। पहला समस्त शब्द ‘तिक्तैहविःपानम्’ बिगड़ा है (सुझाव: तिक्तैर्हविःपानम् या तिक्तकहविः); इसलिए उस पर प्रश्न नहीं। ‘सदा’ पहले या दूसरे अर्ध से जुड़ सकता है। अंतिम समास का प्रधान संज्ञा-शब्द स्पष्ट नहीं। संधि जाँची: विरेकः + अस्रश्रुतिः → विरेकोऽस्रश्रुतिः; लघु + अन्न → लघ्वन्न।",
    "70": "विश्वास: मध्यम। केवल सूची है; पिछली इकाई का ‘शस्तम्’ यहाँ समझा जाता है। ‘भृशम्’ ‘क्षुद्वताम्’ के साथ लिया गया, पर पूरी सूची से भी जुड़ सकता है। जांगल, पटोल, आमलक केवल नाम। संधि: पटोल + आमलक → पटोलामलक (अ + आ → आ)।",
    "71": "विश्वास: मध्यम। छपाई में ‘दिवाकरकरै र्निशाकरकरैर्निशि’ में स्पेस गलत है (करैः + निशाकर…)। ‘ल्हादितम्’ संभवतः ‘ह्लादितम्’ है; ‘अगस्तेन’ संभवतः ‘अगस्त्येन’ है। वाक्य अगली इकाई में चलता है; अगस्त्य के बारे में श्लोक कुछ और नहीं कहता।",
    "72": "विश्वास: मध्यम। ‘भ्रमद्ध्रमर’ छपाई-दोष है, सही रूप ‘भ्रमद्भ्रमर’ (संभावित)। दूसरी पंक्ति एक सप्तमी समास है जो अगली इकाई के सरोवरों का विशेषण है; वाक्य पिछली और अगली दोनों इकाइयों से जुड़ता है। संधि जाँची: पाने + अमृत + उपम → पानेऽमृतोपमम् (ए + अ → ए ऽ; अ + उ → ओ)।",
    "73": "विश्वास: मध्यम। ‘सुसरोरुहसेन्यासु’ अनिश्चित है (सुझाव ‘सेव्यासु’); ‘प्लुवेत’ संभवतः ‘प्लवेत’ है। इसलिए प्रश्न ‘सरसीषु’ और दूसरी पंक्ति पर बने। संधि: शीत + उशीर → शीतोशीर (अ + उ → ओ)। उशीर औषधि का नाम है।",
    "74": "विश्वास: मध्यम। संपादकों की टिप्पणी: ‘तृप्तिंदध्यातप…’ वाली पंक्ति (४.१२७) पूरी तरह जाँची नहीं जा सकती, इसलिए प्रश्न केवल पहली पंक्ति पर हैं। उस सूची की क्रिया ‘विवर्जयेत्’ अगली इकाई में है। संधि: सौधम् + आश्रितः → सौधमाश्रितः। ‘सौध’ का छत अर्थ अनुमान है।",
    "75": "विश्वास: मध्यम। पहली पंक्ति (४.१२८) में ‘मनुषारांश्च / अनुषारान्’ संभवतः ‘तुषारान्’ है (संपादकीय सुझाव); इसलिए उस पंक्ति पर प्रश्न नहीं। ‘स्वस्वाधिक्यम्…ऋतौ ऋतौ’ दोनों तरह पढ़ा जा सकता है (हर रस अपनी ऋतु में, या हर ऋतु में अपना रस); प्रश्न दोनों से अलग हैं। संधि: सर्व + रस + अभ्यास → सर्वरसाभ्यासः; ऋतौ + ऋतौ → ऋतावृतौ।",
    "76": "विश्वास: उच्च। ‘अंत्यादिसप्ताहात्’ का पंचमी रूप ढीला है; अर्थ ‘अंतिम और आरंभिक सात दिन’ लिया गया। ‘क्रमात्’ दोनों क्रियाओं से जुड़ता है। संधि जाँची: सप्ताहात् + ऋतु → सप्ताहादृतु (त् → द्); पूर्वः + विधिः → पूर्वो विधिः; सेवनीयः + अपरः → सेवनीयोऽपरः।",
    "77": "विश्वास: उच्च। ‘असात्म्य’ को ‘अनुपयुक्तता’ रखा गया। ‘त्यागशीलनात्’ = छोड़ना और अपनाना। ‘ऋतुषु एवंविधेषु एव’ अगली इकाई के ‘अन्यरूपेषु’ से भिन्न है, पर वह इकाई क्षतिग्रस्त है। संधि: ऋतुषु + एवं → ऋतुष्वेवं।",
    "78": "विश्वास: कम। पहली पंक्ति में ‘विरुद्धज्ञानिको’ अस्पष्ट है (कोई सुधार नहीं मिला)। दूसरी पंक्ति ‘मासराशिखरूपारुथमृतोर्यरुलक्षणत्रयं’ बिगड़ी है; संपादकों का सुझाव ‘मासराशिस्वरूपाख्यमृतोर्यल्लक्षणत्रयं’ है, जिसमें ‘आरुथ’ को ‘आख्य’ पढ़ना अनिश्चित है। इसलिए प्रश्न केवल साफ़ शब्दों पर बने। वाक्य अगली इकाई तक चलता है। संधि: निर्दिश्यते + अन्यरूपेषु → निर्दिश्यतेऽन्यरूपेषु।",
    "79": "विश्वास: मध्यम। ‘तस्य बलात्’ में ‘तस्य’ किसका है, यह पंक्तियों से स्पष्ट नहीं; ‘यथोत्तरम्’ के दो अर्थ संभव (उत्तरोत्तर, या बाद वाले के अनुसार)। वाक्य इकाई ७८ से चलकर यहाँ पूरा होता है। संधि: भजेत् + चर्याम् → भजेच्चर्याम्; बलात् + इति → बलादिति; यथा + उत्तरम् → यथोत्तरम्।",
    "80": "विश्वास: उच्च। समापन-वाक्य। संधि: चतुर्थः + अध्यायः → चतुर्थोऽध्यायः। ‘४’ अध्याय की संख्या है।",
}

AIDS = {
    "68": {
        "chain": {"steps": ["वर्षा की शीतलता के अभ्यस्त शरीर",
                            "सहसा सूर्य की किरणों से तपना",
                            "तब पहले से संचित पित्त कुपित होता है"]},
        "chunks": "वर्षाशीतोचितांगानां | सहसैवार्करश्मिभिः ‖ तप्तानां संचितं पूर्वं | तदा पित्तं प्रकुप्यति।",
        "sandhi": "आ + ए → ऐ: सहसा + एव → सहसैव। अ + उ → ओ: शीत + उचित → शीतोचित।",
        "frame": "किसमें: वर्षा की शीत के अभ्यस्त शरीर · कैसे: सहसा सूर्य की किरणों से तपना · क्या: पूर्व-संचित पित्त कुपित।",
    },
    "69": {
        "chunks": "शस्तं (तिक्तैहविःपानं, पाठ अनिश्चित) विरेकोऽस्रश्रुतिः सदा ‖ शीतं लघ्वन्नपानं च | कषायस्वादुतिक्तकं।",
        "sandhi": "अः + अ → ओऽ: विरेकः + अस्रश्रुतिः → विरेकोऽस्रश्रुतिः। उ + अ → व्+अ: लघु + अन्न → लघ्वन्न।",
        "anchors": "शस्त = प्रशस्त · विरेक = विरेचन · अस्र = रक्त · श्रुति = बहना · कषाय-स्वादु-तिक्त = तीन रस, इसी क्रम में।",
    },
    "70": {
        "diagram": {"groups": [
            {"label": "पहली पंक्ति",
             "items": ["शालि", "षष्टिक", "गोधूम", "यव", "मुद्ग", "सिता", "मधु"]},
            {"label": "दूसरी पंक्ति",
             "items": ["पटोल", "आमलक", "द्राक्षा", "जांगल (क्षुद्वताम्)"]}]},
        "chunks": "शालिषष्टिकगोधूमयवमुद्गसितामधु ‖ पटोलामलकं द्राक्षा | जांगलं क्षुद्वतां भृशं।",
        "sandhi": "अ + आ → आ: पटोल + आमलक → पटोलामलक।",
    },
    "71": {
        "contrast": "दिन में: सूर्य की किरणों से तपा ↔ रात में: चंद्र की किरणों से शीतल किया हुआ (एक ही जल)।",
        "chunks": "दिवा दिवाकरकरैः | निशाकरकरैर्निशि ‖ संतप्तं ल्हादितं तोयम् | अगस्तेनाविषीकृतं।",
        "sandhi": "ऐः + निशि → ऐर्निशि: करैः + निशि → करैर्निशि (मुद्रण में स्पेस गलत है)।",
        "anchors": "दिवाकर = सूर्य (दिन करने वाला) · निशाकर = चंद्र (रात करने वाला) · कर (किरण) = रश्मि · तोय = जल।",
    },
    "72": {
        "diagram": {"groups": [
            {"label": "जल के गुण",
             "items": ["निर्मलं", "शुचि", "कालेन पक्वं", "पानेऽमृतोपमं"]}]},
        "chunks": "निर्मलं शुचि कालेन | पक्वं पानेऽमृतोपमं ‖ हंसौघपक्षविक्षेप | भ्रमद्भ्रमरपंक्तिषु।",
        "sandhi": "ए + अ → ए ऽ: पाने + अमृत → पानेऽमृत। अ + उ → ओ: अमृत + उपम → अमृतोपम।",
        "pegs": "मेरा बनाया चित्र: साफ़, उजला पानी, जिस पर हंस पंख फड़फड़ाते हैं और भौंरे मँडराते हैं। केवल याद के लिए।",
    },
    "73": {
        "chunks": "सरसीषु (…) प्लवेत ‖ लघुशुद्धांबरस्रग्वी | शीतोशीरविलेपनः।",
        "sandhi": "अ + उ → ओ: शीत + उशीर → शीतोशीर।",
        "frame": "कहाँ: सरोवरों में · वेश: हल्के शुद्ध वस्त्र, माला · लेप: शीतल उशीर।",
    },
    "74": {
        "chunks": "सेवेत चंद्रकिरणान् | प्रदोषे सौधमाश्रितः ‖ (दूसरी पंक्ति की सूची, पाठ अनिश्चित)",
        "frame": "क्या: चंद्रकिरणों का सेवन · कब: प्रदोष में · कैसे: सौध (महल) का आश्रय लेकर।",
        "sandhi": "म् + आ: सौधम् + आश्रितः → सौधमाश्रितः।",
    },
    "75": {
        "chunks": "(पहली पंक्ति अनिश्चित) विवर्जयेत् ‖ नित्यं सर्वरसाभ्यासः | स्वस्वाधिक्यमृतावृतौ।",
        "sandhi": "अ + अ → आ: रस + अभ्यास → रसाभ्यास; स्व + स्व + आधिक्य → स्वस्वाधिक्य। औ + ऋ → आव्+ऋ: ऋतौ + ऋतौ → ऋतावृतौ।",
        "anchors": "नित्यम् = सदा · सर्व-रस = सभी रस · अभ्यास = लगातार प्रयोग · ऋतौ ऋतौ = हर ऋतु में।",
    },
    "76": {
        "diagram": {"groups": [
            {"label": "ऋतुसंधि",
             "items": ["अंत्य सप्ताह", "आदि सप्ताह"]},
            {"label": "वहाँ क्रम से",
             "items": ["पूर्व विधि त्याज्य", "अपर विधि सेवनीय"]}]},
        "chunks": "ऋत्वोरंत्यादिसप्ताहात् | ऋतुसंधिरिति स्मृतः ‖ तत्र पूर्वो विधिस्त्याज्यः | सेवनीयोऽपरः क्रमात्।",
        "sandhi": "त् → द् (स्वर से पहले): सप्ताहात् + ऋतु → सप्ताहादृतु। अः + घोष → ओ: पूर्वः + विधिः → पूर्वो विधिः।",
        "contrast": "पूर्व (त्याज्य: छोड़ना) ↔ अपर (सेवनीय: अपनाना)।",
        "seesaw": "त्याज्यः ↔ सेवनीयः: पूर्व विधि छोड़ी जाती है, बाद वाली अपनाई जाती है।",
    },
    "77": {
        "chain": {"steps": ["सहसा त्याग और ग्रहण (त्यागशीलनात्)",
                            "असात्म्य से उत्पन्न रोग हो सकते हैं"]},
        "chunks": "असात्म्यजा हि रोगाः स्युः | सहसा त्यागशीलनात् ‖ ऋतुष्वेवंविधेष्वेव | विधिः स्वास्थ्ये च देहिनां।",
        "sandhi": "उ + ए → व्+ए: ऋतुषु + एवं → ऋतुष्वेवं।",
        "anchors": "असात्म्य = अनुकूल न होना · सहसा = अचानक · त्याग = छोड़ना · शीलन = अपनाना · देहिन् = देहधारी।",
    },
    "78": {
        "chunks": "निर्दिश्यतेऽन्यरूपेषु | (विरुद्धज्ञानिको, अस्पष्ट) विधिः ‖ (दूसरी पंक्ति बिगड़ी हुई)",
        "sandhi": "ए + अ → ए ऽ: निर्दिश्यते + अन्यरूपेषु → निर्दिश्यतेऽन्यरूपेषु।",
        "anchors": "निर्दिश्यते = बताई जाती है · अन्यरूप = दूसरे रूप वाले · विधि = विधि, नियम।",
    },
    "79": {
        "chunks": "यथोत्तरं भजेच्चर्यां | तत्र तस्य बलादिति।",
        "sandhi": "त् + च → च्च: भजेत् + चर्याम् → भजेच्चर्याम्। त् → द्: बलात् + इति → बलादिति।",
        "frame": "कैसे: यथोत्तरम् (क्रम से) · क्या: चर्या का पालन · वहाँ: तत्र (तस्य बलात्, संदर्भ अस्पष्ट)।",
    },
    "80": {
        "chunks": "इति ऋतुचर्यानाम | चतुर्थोऽध्यायः।",
        "sandhi": "अः + अ → ओऽ: चतुर्थः + अध्यायः → चतुर्थोऽध्यायः।",
    },
}

IMAGE_SPECS = {
    ("68", "chain"): {
        "file": "ch4b06-pitta-68.svg",
        "alt": "Flowchart in three steps: bodies used to the rains' cold, suddenly heated by the sun's rays, then the Pitta accumulated earlier is aggravated",
        "type": "mermaid",
        "code": ('flowchart TD\n  A["वर्षा की शीत के<br/>अभ्यस्त शरीर"] --> B["सहसा सूर्य की<br/>किरणों से तपे"]\n'
                 '  B --> C["पहले संचित पित्त<br/>तब कुपित होता है"]\n'),
    },
    ("71", "contrast"): {
        "file": "ch4b06-water-71.svg",
        "alt": "Table: by day the water is heated by the sun's rays; at night it is made cool by the moon's rays",
        "type": "table",
        "title": "श्लोक ७१: जल पर किरणें",
        "heads": ["समय", "किरणें"],
        "rows": [["दिन में", "सूर्य की किरणों से तपा"],
                 ["रात में", "चंद्र की किरणों से शीतल"]],
    },
    ("72", "diagram"): {
        "file": "ch4b06-water-72.svg",
        "alt": "Mind map: four descriptions of the water: clear, pure, matured by time, like nectar to drink",
        "type": "mermaid",
        "code": 'mindmap\n  जल के गुण\n    निर्मल\n    शुचि\n    कालेन पक्व\n    पीने में अमृत-सम\n',
    },
    ("76", "diagram"): {
        "file": "ch4b06-ritusandhi-76.svg",
        "alt": "Flowchart: ritusandhi is the last seven days of one season and the first seven of the next; there the former regimen is given up and the latter taken up in order",
        "type": "mermaid",
        "code": ('flowchart TD\n  A["ऋतुसंधि: दो ऋतुओं के<br/>अंतिम और आरंभिक सात दिन"] --> B["पूर्व विधि<br/>छोड़नी चाहिए"]\n'
                 '  A --> C["बाद वाली विधि<br/>क्रम से अपनानी चाहिए"]\n'),
    },
    ("77", "chain"): {
        "file": "ch4b06-asatmya-77.svg",
        "alt": "Chain of two steps: abrupt abandoning and taking up, then diseases born of unsuitability may arise",
        "type": "chain",
        "title": "श्लोक ७७: असात्म्य से रोग",
        "steps": ["सहसा त्याग और ग्रहण", "असात्म्य से रोग हो सकते हैं"],
    },
}
