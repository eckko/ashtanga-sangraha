from helpers import mcq, match, order, fill, multi, accepts

# Kalpasthāna chapter 4 (Bastikalpa), units 25-37 (study-text lines 05.04.47-72).
# Sections (sections_kalpa.py KA4): 25-30 cleansing, binding and scraping drugs; 31-37 picchā basti and bastis in complications.
# Cross-references name study-text line ids (05.04.L), not quiz unit numbers.

AUTHORED = {}

# ---------------------------------------------------------------- unit 25
AUTHORED["25"] = {
    "title": "बस्तीनतश्चित्रान्प्रचक्षते",
    "question": "What does verse 25 call the bastis arranged half and half, and where does its drug list begin?",
    "rule": ("Bastis arranged half and half are declared citra (varied). Line 2 starts a drug list (kośātakī, phala, jīmūta, "
             "vatsaka and an unclear name) that runs to line 05.04.52."),
    "limits": ("What is halved is not stated; अर्द्धाद्र्ध is probably अर्द्धार्द्ध (flagged). द्व्येश्वाकु is unclear and unidentified; "
               "phala may be a separate item. The text does not say which list belongs to which basti. Questions keep to line 1."),
    "explain_hi": ("यहाँ एक नया विषय शुरू होता है। पहली पंक्ति कहती है कि आधे-आधे विधान से बनी बस्तियों को ‘चित्र’ यानी विविध कहा जाता है; "
                   "क्या आधा किया जाता है, यह नहीं बताया गया। ‘अतः’ का अर्थ ‘इसलिए’ या ‘यहाँ से आगे’ दोनों हो सकता है। "
                   "दूसरी पंक्ति से द्रव्यों की सूची शुरू होती है जो पंक्ति ०५.०४.५२ तक चलती है: कोशातकी यानी प्रायः तोरई, "
                   "एक अस्पष्ट नाम ‘द्व्येश्वाकु’, फल, जीमूत यानी प्रायः देवदाली और वत्सक यानी कुटज। "
                   "पाठ यह नहीं बताता कि कौन-सी सूची किस बस्ति की है।"),
    "hook": "आधा-आधा जोड़ो तो बस्ति बने ‘चित्र’ यानी विविध।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What name does verse 25 give to the bastis arranged half and half?",
            ("Citra (varied)",
             "चित्रान्: varied, the name they declare (प्रचक्षते)."),
            [("Picchila (slimy)", "Slimy is said later, in line 05.04.61, not in verse 25."),
             ("Lekhana (scraping)", "Scraping is said of triphalā juice in line 05.04.58."),
             ("Bṛṃhaṇa (nourishing)", "Nourishing is said in line 05.04.59, not here.")],
            "बस्तीन् … चित्रान् प्रचक्षते: they declare the bastis to be citra, varied.",
            "चित्र = varied."),
        match(1, "Match each clear word of verse 25, line 1, to its meaning.",
              [["बस्तीन्", "bastis (enemas)"], ["अतः", "hence"], ["चित्रान्", "varied"], ["प्रचक्षते", "they declare"]],
              "Line 1 is a full sentence: hence they declare the bastis (arranged half and half) to be varied.",
              "बस्तीन् = bastis; अतः = hence; चित्रान् = varied; प्रचक्षते = they declare."),
        order(2, "Put these clear words of verse 25, line 1, in the printed order.",
              ["बस्तीन्", "अतः", "चित्रान्", "प्रचक्षते"],
              "Object, the particle hence, the predicate varied, and the verb last.",
              "बस्तीन् · अतः · चित्रान् · प्रचक्षते.",
              role="extend",
              teaches="Line 1 of verse 25 names the bastis (accusative), then अतः, the name चित्रान्, and ends with the verb प्रचक्षते."),
        mcq("discriminate", 3, "Which split of बस्तीनतश्चित्रान् in verse 25 is right?",
            ("बस्तीन् + अतः + चित्रान्",
             "न् before a vowel joins it (बस्तीनतः); -अः before च becomes -अश् (अतश्चित्रान्)."),
            [("बस्तीन् + अतम् + चित्रान्", "म् before च becomes anusvara or ञ्, never श्."),
             ("बस्तीन् + आतः + चित्रान्", "With आतः the print would read बस्तीनातश्…, with a long आ."),
             ("बस्तीन् + अताः + चित्रान्", "-आः before च gives -आश्, a long vowel: …ताश्चित्रान्.")],
            "बस्तीन् (bastis) + अतः (hence) + चित्रान् (varied).",
            "-अः before च/छ → -अश्."),
        mcq("apply", 4, "A student says verse 25 tells which drug list goes with the citra bastis. What does the card say?",
            ("The text leaves the link unstated",
             "The notes say plainly that no list is tied to a basti."),
            [("Each one takes the kośātakī list", "Not stated: the card ties no list to a basti."),
             ("Each half is one of the drug lists", "The verse does not say what is halved."),
             ("Only the nirūha takes this list", "Nirūha is not named in verse 25.")],
            "Verse 25 names the citra bastis and starts a list, but never links the two.",
            "No list is assigned to a basti in the text."),
        mcq("transfer", 5, "Like अतः + चित्रान् → अतश्चित्रान्, how does invented ततः + चरेत् join?",
            ("ततश्चरेत्",
             "-अः before च becomes -अश्, as in अतश्चित्रान्."),
            [("ततोचरेत्", "-ओ arises only before voiced sounds; च is unvoiced."),
             ("ततर्चरेत्", "र् comes from -इः/-उः before voiced sounds, not from -अः before च."),
             ("ततस्चरेत्", "Before च the visarga becomes the palatal श्, not the dental स्.")],
            "The visarga takes the place of the following consonant: palatal च → श्.",
            "-अः + च → -अश्च.",
            teaches="A visarga before च/छ becomes श् (अतः + चित्रान् → अतश्चित्रान्; ततः + चरेत् → ततश्चरेत्)."),
    ],
}

# ---------------------------------------------------------------- unit 26
AUTHORED["26"] = {
    "title": "श्यामात्रिवृतोर्मूलं",
    "question": "Which drugs does verse 26 add to the list, and which part of śyāmā and trivṛt does it name?",
    "rule": ("The list goes on: the root of śyāmā and trivṛt (turpeth), (that) born of dantī and dravantī, prakīryā, "
             "udakīryā, kṣīriṇī, nīlinī (probably indigo) and fruit. No verb; the list ends in line 05.04.52."),
    "limits": ("What is born of dantī and dravantī is not stated, nor whose fruit फलं is. Śyāmā, dravantī, prakīryā, udakīryā "
               "and kṣīriṇī are disputed; dantī (wild croton) and nīlinī probable; trivṛt standard."),
    "explain_hi": ("यह श्लोक पिछली सूची को आगे बढ़ाता है; इसमें कोई क्रिया नहीं है। पहले श्यामा और त्रिवृत् यानी निशोथ का मूल आता है, "
                   "फिर ‘दन्ती और द्रवन्ती से उत्पन्न’; क्या उत्पन्न, यह नहीं कहा गया। "
                   "दूसरी पंक्ति में प्रकीर्या, उदकीर्या, क्षीरिणी, नीलिनी यानी प्रायः नील और अन्त में अकेला ‘फलं’ है, जिसका पौधा नहीं बताया गया। "
                   "त्रिवृत् की पहचान मानक है; दन्ती (प्रायः जंगली जमालगोटा) और नीलिनी सम्भावित; बाकी विवादित।"),
    "hook": "श्यामा-निशोथ की जड़, दन्ती-द्रवन्ती का अंश, फिर प्रकीर्या-उदकीर्या, क्षीरिणी-नील और फल।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "Which part of śyāmā and trivṛt does verse 26 name?",
            ("The root (मूलं)",
             "श्यामात्रिवृतोर्मूलं: the root of śyāmā and trivṛt."),
            [("The flower (पुष्पं)", "No flower is named in verse 26."),
             ("The bark (त्वक्)", "No bark is named in verse 26."),
             ("The leaf (पत्रं)", "No leaf is named in verse 26.")],
            "श्यामा-त्रिवृतोः (of the two) + मूलम् (root).",
            "मूल = root."),
        match(1, "Match each word of verse 26 to its meaning as the card gives it.",
              [["त्रिवृत्", "turpeth (standard)"], ["दन्ती", "probably wild croton"], ["नीलिनी", "probably indigo"],
               ["मूलं", "root"], ["-जं", "born of"]],
              "Trivṛt is a standard identification; dantī and nīlinī are probable.",
              "त्रिवृत् = turpeth; दन्ती = wild croton (probable); नीलिनी = indigo (probable); मूल = root; -ज = born of."),
        order(2, "Put these items of verse 26 in the verse's order.",
              ["श्यामात्रिवृतोर्मूलं", "दंतीद्रवंतिजं", "प्रकीर्या", "चोदकीर्या", "क्षीरिणी", "नीलिनी"],
              "Root of śyāmā and trivṛt, the dantī-dravantī item, then prakīryā, udakīryā, kṣīriṇī, nīlinī (and fruit last).",
              "श्यामात्रिवृतोर्मूलं · दंतीद्रवंतिजं · प्रकीर्या · चोदकीर्या · क्षीरिणी · नीलिनी.",
              role="extend",
              teaches="Verse 26 lists two root-drug items in line 1 and then prakīryā, udakīryā, kṣīriṇī, nīlinī and fruit in line 2."),
        mcq("discriminate", 3, "Which split of चोदकीर्या in verse 26 is right?",
            ("च + उदकीर्या",
             "अ + उ → ओ: च + उदकीर्या = चोदकीर्या."),
            [("च + ओदकीर्या", "अ + ओ gives औ: it would read चौदकीर्या."),
             ("च + इदकीर्या", "अ + इ gives ए: it would read चेदकीर्या."),
             ("चः + उदकीर्या", "-अः before उ loses the visarga and does not merge: च उदकीर्या.")],
            "च (and) + उदकीर्या (a drug name).",
            "अ + उ → ओ."),
        mcq("apply", 4, "Whose fruit is फलं at the end of verse 26, by the card?",
            ("The verse does not say",
             "The notes say no plant is supplied for फलं."),
            [("Nīlinī's, as the verse states", "The verse states no owner; nīlinī is only a possible reading."),
             ("The fruit of dantī, line 1", "Dantī stands in line 1; no fruit is tied to it."),
             ("The fruit of trivṛt, line 1", "Only the root of trivṛt is named.")],
            "फलम् stands alone; the text names no plant for it.",
            "Supply nothing the text does not state."),
        mcq("transfer", 5, "Like त्रिवृतोः + मूलं → त्रिवृतोर्मूलं, how does invented वृक्षयोः + मूलम् join?",
            ("वृक्षयोर्मूलम्",
             "-ओः before a voiced sound becomes -ओर्, as in त्रिवृतोर्मूलं."),
            [("वृक्षयोमूलम्", "The visarga after -ओ is not dropped; it becomes र् before voiced म."),
             ("वृक्षयोस्मूलम्", "स् appears before त/थ, not before म."),
             ("वृक्षयोऽमूलम्", "An avagraha marks a dropped अ; मूलम् has none to drop.")],
            "Visarga after a vowel other than अ/आ becomes र् before a voiced sound.",
            "-ओः + voiced consonant → -ओर्.",
            teaches="A visarga after ओ (not अ/आ) becomes र् before a voiced sound: त्रिवृतोः + मूलम् → त्रिवृतोर्मूलम्; वृक्षयोः + मूलम् → वृक्षयोर्मूलम्."),
    ],
}

# ---------------------------------------------------------------- unit 27
AUTHORED["27"] = {
    "title": "सकल्कसैंधवयुताः पक्वाशयविशोधनाः",
    "question": "How does verse 27 close the drug list, and what do the listed drugs cleanse?",
    "rule": ("The list of lines 05.04.48-52 ends with samalā, śaṅkhinī, rodhra and the fruit of kampillaka. Joined with paste (kalka) "
             "and rock salt, these drugs are cleansers of the pakvāśaya (seat of digested matter; the data: colon)."),
    "limits": ("रोधं is read as रोध्र, lodhra (flagged). Samalā is unidentified, śaṅkhinī disputed; kampillaka and rodhra standard. "
               "No verb is in the Sanskrit. The text gives no measure and does not say how the drugs are combined."),
    "explain_hi": ("यह श्लोक पंक्ति ०५.०४.४८ से चली सूची को पूरा करता है। पहली पंक्ति में समला, शङ्खिनी, रोध्र यानी लोध (छपा ‘रोधं’) "
                   "और कम्पिल्लक यानी कमीला का फल है। दूसरी पंक्ति बताती है कि ये द्रव्य कल्क यानी लुगदी और सैन्धव यानी सेंधा नमक से युक्त होकर "
                   "पक्वाशय को शुद्ध करने वाले हैं। पक्वाशय पचे हुए अन्न का स्थान है; डेटा इसे बड़ी आँत मानता है। ‘हैं’ क्रिया संस्कृत में नहीं है।"),
    "hook": "समला-शङ्खिनी-लोध-कमीला: लुगदी और सेंधा नमक के साथ, पक्वाशय की सफ़ाई।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "What do the listed drugs cleanse, according to verse 27?",
            ("The pakvāśaya",
             "पक्वाशयविशोधनाः: cleansers of the pakvāśaya, the seat of digested matter."),
            [("The āmāśaya (stomach)", "Āmāśaya is not named in verse 27."),
             ("The head and the eyes", "No head or eyes are named in verse 27."),
             ("The blood (rakta)", "Blood is not named in verse 27.")],
            "पक्वाशय + विशोधन: they cleanse the pakvāśaya.",
            "पक्वाशय = seat of digested matter (colon, as the data gives it)."),
        match(1, "Match each word of verse 27 to its meaning as the card gives it.",
              [["समला", "an unidentified drug"], ["कम्पिल्लक", "kamala tree"], ["सैन्धव", "rock salt"],
               ["कल्क", "paste"], ["विशोधन", "cleanser"]],
              "Kampillaka is a standard identification; samalā is unidentified.",
              "समला = unidentified; कम्पिल्लक = kamala tree; सैन्धव = rock salt; कल्क = paste; विशोधन = cleanser."),
        order(2, "Put these words of verse 27 in the verse's order.",
              ["समला", "शंखिनी", "फलं कंपिल्लकस्य", "सकल्कसैंधवयुताः", "पक्वाशयविशोधनाः"],
              "The last drugs of the list, then what they are joined with, then what they do.",
              "समला · शंखिनी · फलं कंपिल्लकस्य · सकल्कसैंधवयुताः · पक्वाशयविशोधनाः.",
              role="extend",
              teaches="Verse 27 closes the list (samalā, śaṅkhinī, rodhra, kampillaka fruit), adds paste and rock salt, and names the action: cleansing the pakvāśaya."),
        mcq("discriminate", 3, "In फलं कंपिल्लकस्य of verse 27, what does the ending -स्य show?",
            ("The fruit is that of kampillaka",
             "-स्य is genitive singular: of kampillaka."),
            [("Kampillaka is used with fruit", "That would need an instrumental, -एन."),
             ("The fruit is put in kampillaka", "That would need a locative, -ए."),
             ("Kampillaka is a second subject", "A subject is nominative; -स्य is genitive.")],
            "फलम् (fruit) + कम्पिल्लकस्य (of kampillaka).",
            "-स्य = genitive singular, of."),
        multi("apply", 4, "Which does verse 27 say the drugs are joined with?",
              [("Paste (कल्क)", "Right: स-कल्क- names the paste."),
               ("Rock salt (सैन्धव)", "Right: सैन्धव is in the same compound."),
               ("Honey (मधु)", "Honey is not named in verse 27."),
               ("Oil (तैल)", "Oil is not named in verse 27."),
               ("Milk (क्षीर)", "Milk is not named in verse 27.")],
              [0, 1],
              "स-कल्क-सैन्धव-युताः: joined with paste and rock salt.",
              "Additions of verse 27: कल्क and सैन्धव."),
        mcq("transfer", 5, "Like सकल्कसैंधवयुताः (masc. nom. pl.), which invented word says masculine plural drugs are joined with oil?",
            ("तैलयुताः",
             "-युताः is masculine nominative plural, like …सैंधवयुताः."),
            [("तैलयुतः", "Singular; the drugs are plural."),
             ("तैलयुतान्", "Accusative plural; the listed drugs are nominative."),
             ("तैलयुतम्", "Neuter singular; the drugs are masculine plural.")],
            "An adjective in -युत agrees with its noun: masculine plural nominative -युताः.",
            "-युताः = joined with (m. nom. pl.).",
            teaches="A compound ending in -युत (joined with) agrees with its noun; for masculine plural drugs in the nominative it ends -युताः."),
    ],
}

# ---------------------------------------------------------------- unit 28
AUTHORED["28"] = {
    "title": "प्रग्रहः खदिरी कुष्ठं शमीपिंडीतकायवाः",
    "question": "Which drugs open the binding list in verse 28, and which of them can be read with confidence?",
    "rule": ("A new list begins (lines 05.04.53-56, called saṃgrāhika, binding, in line 05.04.56): dhātakī flowers, an unclear word, "
             "jīvantī root, vatsaka; then pragraha, khadirī, kuṣṭha (costus), śamī, piṇḍītakā and yava (barley)."),
    "limits": ("Line 1 is damaged: धातुकी is read as धातकी; तक्रींर् is unreadable, with no restoration accepted. Pragraha may not be "
               "a drug name. Khadirī and piṇḍītakā are disputed, śamī probable. Questions keep to line 2."),
    "explain_hi": ("यहाँ से एक नई सूची शुरू होती है, जिसे पंक्ति ०५.०४.५६ में ‘संग्राहिक’ यानी बाँधने वाली कहा गया है। "
                   "पहली पंक्ति छपाई में बिगड़ी है: ‘धातुकी’ सम्भवतः धातकी यानी धाय के फूल है, ‘तक्रींर्’ पढ़ा नहीं जाता, फिर जीवन्ती यानी प्रायः डोडी की जड़ और वत्सक यानी कुटज। "
                   "दूसरी पंक्ति साफ़ है: प्रग्रह, खदिरी, कुष्ठ यानी कूट, शमी यानी प्रायः खेजड़ी, पिण्डीतका और यव। "
                   "‘प्रग्रह’ का दूसरा अर्थ ‘नियन्त्रण’ है, इसलिए यह द्रव्य-नाम है या नहीं, निश्चित नहीं। ‘यवाः’ बहुवचन है: यव के दाने।"),
    "hook": "बाँधने वाली सूची: धाय के फूल से शुरू, फिर कूट, खेजड़ी और यव।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What name does the list begun in verse 28 receive in line 05.04.56?",
            ("Saṃgrāhika (binding)",
             "संग्राहिका मताः: the list of lines 05.04.53-56 is considered binding."),
            [("Lekhana (scraping)", "Scraping is said of the triphalā juice in line 05.04.58."),
             ("Bṛṃhaṇa (nourishing)", "Nourishing is said in line 05.04.59."),
             ("Viśodhana (cleansing)", "Cleansers of the pakvāśaya closed the earlier list, line 05.04.52.")],
            "The list of lines 05.04.53-56 ends: इति संग्राहिका मताः.",
            "संग्राहिक = binding."),
        match(1, "Match each word of verse 28, line 2, to its meaning as the card gives it.",
              [["कुष्ठ", "costus root"], ["शमी", "probably the khejri tree"], ["यव", "barley"],
               ["प्रग्रह", "unidentified; elsewhere restraint"]],
              "Line 2 is clear; only pragraha is left unidentified.",
              "कुष्ठ = costus; शमी = khejri (probable); यव = barley; प्रग्रह = unidentified."),
        order(2, "Put these items of verse 28, line 2, in the verse's order.",
              ["प्रग्रहः", "खदिरी", "कुष्ठं", "शमी", "पिण्डीतका", "यवाः"],
              "Pragraha, khadirī, kuṣṭha, then the compound śamī-piṇḍītakā-yava.",
              "प्रग्रहः · खदिरी · कुष्ठं · शमी · पिण्डीतका · यवाः.",
              role="extend",
              teaches="Line 2 of verse 28 lists pragraha, khadirī, kuṣṭha, and a closing compound of śamī, piṇḍītakā and yava."),
        mcq("discriminate", 3, "Which item of verse 28, line 2, may not be a drug name at all?",
            ("प्रग्रहः",
             "It can mean restraint; the data leaves it unidentified."),
            [("कुष्ठं", "Kuṣṭha is costus root, a drug."),
             ("यवाः", "Yava is barley."),
             ("शमी", "Śamī is a tree, probably khejri.")],
            "Pragraha is the one word the data doubts as a drug name.",
            "प्रग्रह = unidentified (elsewhere: restraint)."),
        mcq("apply", 4, "What does the plural यवाः in verse 28 mean, by the card?",
            ("Barley grains",
             "यवाः is plural, so the grains of barley."),
            [("Two barley plants", "Dual would be यवौ; यवाः is plural."),
             ("A barley gruel", "No gruel is named in verse 28."),
             ("Barley flour", "No flour is named in verse 28.")],
            "यव = barley; the plural ending gives grains.",
            "यवाः = barley grains."),
        mcq("transfer", 5, "Like शमीपिंडीतकायवाः, which invented dvandva joins शमी and यव in the nominative plural?",
            ("शमीयवाः",
             "Dvandva: stems joined, the last member takes the ending -आः."),
            [("शमीयवः", "Singular; the list is plural."),
             ("शमीयवान्", "Accusative plural; a list of subjects is nominative."),
             ("शमीयवम्", "Neuter singular, not nominative plural.")],
            "Only the last member of a dvandva is declined: शमी-यवाः.",
            "Dvandva: last member carries case and number.",
            teaches="In a dvandva only the last member takes the ending: शमी-पिण्डीतका-यवाः, शमी-यवाः (nominative plural)."),
    ],
}

# ---------------------------------------------------------------- unit 29
AUTHORED["29"] = {
    "title": "इति संग्राहिका मताः",
    "question": "How does verse 29 close the binding list, and what name does it give the drugs?",
    "rule": ("The list of lines 05.04.53-56 ends: priyaṅgu, red root(s), bhairaṇī, jāti, yūthikā, vaṭa and the rest, kiṃśuka, "
             "rodhra; thus they are considered saṃgrāhika (binding)."),
    "limits": ("प्रियंगुरक्तमूले can be divided more than one way, so no question rests on it. Bhairaṇī is unidentified, priyaṅgu disputed, "
               "jāti and yūthikā probable. The vaṭa group's members are not given. रोधम् is read as रोध्र (flagged)."),
    "explain_hi": ("यह श्लोक बाँधने वाली सूची को बंद करता है। पहली पंक्ति में प्रियङ्गु और ‘रक्तमूल’ यानी लाल जड़ (पाठ अनिश्चित), "
                   "फिर भैरणी (अपहचानी), जाति यानी प्रायः चमेली और यूथिका यानी प्रायः जूही आती हैं। "
                   "दूसरी पंक्ति में वट यानी बरगद आदि, किंशुक यानी ढाक और रोध्र यानी लोध हैं। "
                   "‘इति संग्राहिका मताः’: इस प्रकार ये संग्राहिक यानी बाँधने वाले माने गए हैं। वट आदि गण के सदस्य यहाँ नहीं गिनाए गए।"),
    "hook": "चमेली-जूही, बरगद-ढाक-लोध: ‘इति संग्राहिकाः’, ये बाँधते हैं।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "Which tree of verse 29 stands with -आद्याः, and the rest?",
            ("Vaṭa (banyan)",
             "वटाद्याः: vaṭa and the rest."),
            [("Kiṃśuka (flame-of-the-forest)", "Kiṃśuka stands alone, without -आद्य."),
             ("Jāti (jasmine)", "Jāti is in the compound of line 1, without -आद्य."),
             ("Yūthikā (a jasmine)", "Yūthikā closes the line 1 compound, without -आद्य.")],
            "वट + आद्याः = vaṭa and the rest; the rest are not named.",
            "-आद्य = beginning with, and the rest."),
        match(1, "Match each word of verse 29 to its meaning as the card gives it.",
              [["जाति", "probably jasmine"], ["यूथिका", "probably Jasminum auriculatum"], ["वट", "banyan"],
               ["किंशुक", "flame-of-the-forest"], ["संग्राहिक", "binding"]],
              "Vaṭa and kiṃśuka are standard; jāti and yūthikā are probable.",
              "जाति = jasmine; यूथिका = a jasmine; वट = banyan; किंशुक = flame-of-the-forest; संग्राहिक = binding."),
        order(2, "Put these items of verse 29 in the verse's order.",
              ["भैरणी", "जाति", "यूथिका", "वटाद्याः", "किंशुकं", "संग्राहिका मताः"],
              "The line 1 compound bhairaṇī-jāti-yūthikā, then vaṭa and the rest, kiṃśuka, and the closing name.",
              "भैरणी · जाति · यूथिका · वटाद्याः · किंशुकं · संग्राहिका मताः.",
              role="extend",
              teaches="Verse 29 ends the list with jasmines, the vaṭa group and kiṃśuka, and closes with इति संग्राहिका मताः."),
        mcq("discriminate", 3, "What explains संग्राहिका without a visarga before मताः in verse 29?",
            ("-आः loses its visarga before voiced म",
             "Correct sandhi: -आः before a voiced consonant drops the visarga."),
            [("It is a feminine singular of the list", "It agrees with masculine plural मताः; the visarga is lost by sandhi."),
             ("The printer dropped the visarga here", "The data calls this correct sandhi, not a misprint."),
             ("-आः before म turns into -ओ instead", "-ओ arises from -अः, not -आः.")],
            "संग्राहिकाः + मताः → संग्राहिका मताः.",
            "-आः + voiced consonant → -आ."),
        mcq("apply", 4, "Does verse 29 list the members of the vaṭa group?",
            ("No; it says only vaṭa and the rest",
             "The data notes that the members are not given."),
            [("Yes: kiṃśuka and rodhra follow it", "They are separate items after the group."),
             ("Yes: jāti and yūthikā precede it", "They are jasmines named before the group."),
             ("Yes: bhairaṇī and priyaṅgu open it", "They belong to line 1, not to a vaṭa group.")],
            "वटाद्याः names the group by its first member only.",
            "-आद्य names a group without listing it."),
        mcq("transfer", 5, "Like वट + आद्याः → वटाद्याः, how does invented बिल्व + आद्याः join?",
            ("बिल्वाद्याः",
             "अ + आ → आ, as in वटाद्याः."),
            [("बिल्वेद्याः", "ए comes from अ + इ, not अ + आ."),
             ("बिल्वोद्याः", "ओ comes from अ + उ, not अ + आ."),
             ("बिल्वद्याः", "The two vowels merge into long आ; they are not lost.")],
            "Short अ and long आ merge into आ.",
            "अ + आ → आ.",
            teaches="-अ + आद्याः gives -आद्याः, a group named by its first member (वटाद्याः, बिल्वाद्याः)."),
    ],
}

# ---------------------------------------------------------------- unit 30
AUTHORED["30"] = {
    "title": "लेखनस्त्रिफलारसः",
    "question": "What does verse 30 name after the binding drugs, and what is called scraping (lekhana)?",
    "rule": ("In sequence, with decoctions and pastes of binding priyaṅgu, ambaṣṭhā and the rest; the additive (pratīvāpa) of uṣaka "
             "and the rest; and the scraping (lekhana) triphalā juice."),
    "limits": ("No noun such as basti is in the unit; a continuation of the kinds begun in line 05.04.47 is likely but not stated. "
               "काथ is read as क्वाथ (flagged). Uṣaka is probably a saline earth; ambaṣṭhā is disputed."),
    "explain_hi": ("इस श्लोक में न क्रिया है न ‘बस्ति’ शब्द; सम्भवतः यह पंक्ति ०५.०४.४७ से शुरू हुए प्रकारों का वर्णन आगे बढ़ाता है, पर पाठ यह नहीं कहता। "
                   "पहली पंक्ति: क्रम से, ग्राही यानी बाँधने वाले प्रियङ्गु, अम्बष्ठा आदि के क्वाथों (छपा ‘काथ’) और कल्कों से। "
                   "दूसरी पंक्ति: उषक यानी प्रायः खारी मिट्टी आदि का प्रतीवाप यानी ऊपर से डाला जाने वाला द्रव्य, और लेखन यानी खुरचने वाला त्रिफला का रस। "
                   "त्रिफला तीन फल हैं: हरड़, बहेड़ा और आँवला।"),
    "hook": "बाँधने वाले क्वाथ-कल्क के बाद: खारी मिट्टी ऊपर से, और त्रिफला-रस खुरचे।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What does verse 30 call the triphalā juice?",
            ("Lekhana (scraping)",
             "लेखनस्त्रिफलारसः: the scraping triphalā juice."),
            [("Bṛṃhaṇa (nourishing)", "Nourishing is said in line 05.04.59, not of triphalā."),
             ("Saṃgrāhika (binding)", "Binding closed the list of line 05.04.56."),
             ("Picchila (slimy)", "Slimy is said in line 05.04.61.")],
            "लेखनः qualifies त्रिफलारसः.",
            "लेखन = scraping."),
        match(1, "Match each word of verse 30 to its meaning as the card gives it.",
              [["लेखन", "scraping"], ["प्रतीवाप", "additive"], ["उषक", "probably a saline earth"],
               ["क्रमेण", "in sequence"], ["त्रिफला", "the three myrobalans"]],
              "These are the clear words of the unit.",
              "लेखन = scraping; प्रतीवाप = additive; उषक = saline earth (probable); क्रमेण = in sequence; त्रिफला = three myrobalans."),
        order(2, "Put these words of verse 30 in the verse's order.",
              ["क्रमेण च", "उषकादिप्रतीवापो", "लेखनः", "त्रिफलारसः"],
              "In sequence (end of line 1), the additive of uṣaka, then the scraping triphalā juice.",
              "क्रमेण च · उषकादिप्रतीवापो · लेखनः · त्रिफलारसः.",
              role="extend",
              teaches="After the binding decoctions and pastes, verse 30 names the uṣaka additive and ends with the scraping triphalā juice."),
        mcq("discriminate", 3, "Which split of लेखनस्त्रिफलारसः in verse 30 is right?",
            ("लेखनः + त्रिफलारसः",
             "-अः before त becomes -अस्: लेखनस्त्रि…."),
            [("लेखनम् + त्रिफलारसः", "म् before त becomes anusvara or न्, not स्."),
             ("लेखनाः + त्रिफलारसः", "That keeps a long आ: it would read लेखनास्त्रि…."),
             ("लेखन + स्त्रिफलारसः", "स्त्रिफला is no word; the juice is त्रिफलारसः.")],
            "लेखनः (scraping) + त्रिफलारसः (triphalā juice).",
            "-अः + त → -अस्त."),
        multi("apply", 4, "Which fruits make up triphalā, as the card names them?",
              [("Harītakī (हरड़)", "Right: one of the three myrobalans."),
               ("Bibhītaka (बहेड़ा)", "Right: one of the three myrobalans."),
               ("Āmalaka (आँवला)", "Right: one of the three myrobalans."),
               ("Pippalī (long pepper)", "Pippalī is not part of triphalā."),
               ("Bilva (बेल)", "Bilva is not part of triphalā.")],
              [0, 1, 2],
              "Triphalā = the three myrobalans: harītakī, bibhītaka, āmalaka.",
              "त्रिफला = हरड़, बहेड़ा, आँवला."),
        mcq("transfer", 5, "Like लेखनः + त्रिफलारसः → लेखनस्त्रिफलारसः, how does invented रसः + तथा join?",
            ("रसस्तथा",
             "-अः before त becomes -अस्."),
            [("रसोतथा", "-ओ arises only before voiced sounds; त is unvoiced."),
             ("रसश्तथा", "श् comes before च/छ, not before त."),
             ("रसतथा", "The visarga is not lost before त; it becomes स्.")],
            "The visarga takes the place of the following dental: त → स्.",
            "-अः + त → -अस्त.",
            teaches="A visarga before त/थ becomes स् (लेखनः + त्रिफलारसः → लेखनस्त्रिफलारसः; रसः + तथा → रसस्तथा)."),
    ],
}

# ---------------------------------------------------------------- unit 31
AUTHORED["31"] = {
    "title": "बदर्यैरावणीशैलूशाल्मलीधन्वनांकुराः",
    "question": "Which sprouts does verse 31 list, and what can be said of its damaged first line?",
    "rule": ("Line 1 (damaged) speaks of a nourishing (bṛṃhaṇa) kind, with madhuka paste and ghee with rasa. Line 2 lists the sprouts "
             "of badarī (jujube), airāvaṇī, śailū, śālmalī (silk-cotton tree) and dhanvana."),
    "limits": ("Line 1 is flagged: कल्कैन is read as कल्केन and a word may be lost; no questions on it. Airāvaṇī is unidentified; "
               "śailū and dhanvana probable. अङ्कुराः is taken with all the names. What the sprouts are, line 05.04.61 says."),
    "explain_hi": ("पहली पंक्ति बिगड़ी है: ‘मधुक कल्कैन’ सम्भवतः ‘मधुककल्केन’ है, यानी मधुक (प्रायः मुलेठी) के कल्क से, और रस सहित घी से, "
                   "एक बृंहण यानी पुष्ट करने वाला प्रकार; किसका, यह नहीं कहा गया। "
                   "दूसरी पंक्ति में वृक्षों के अंकुर गिनाए गए हैं: बदरी यानी बेर, ऐरावणी (अपहचानी), शैलू यानी प्रायः लसोड़ा, शाल्मली यानी सेमल और धन्वन यानी प्रायः धामिन। "
                   "‘अंकुराः’ सब नामों से जुड़ता है। ये अंकुर क्या माने गए, यह पंक्ति ०५.०४.६१ बताती है।"),
    "hook": "बेर, ऐरावणी, लसोड़ा, सेमल, धामिन: इन सबके अंकुर।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "Which part of badarī, śālmalī and the others does verse 31 name?",
            ("Sprouts (अङ्कुराः)",
             "…धन्वनांकुराः: the sprouts of all the trees named."),
            [("Stalks (वृन्त)", "Stalks come in line 05.04.64; here it is अङ्कुराः."),
             ("Roots (मूल)", "No root is named in verse 31, line 2."),
             ("Flowers (पुष्प)", "No flower is named in verse 31.")],
            "The compound ends in अङ्कुराः, sprouts.",
            "अङ्कुर = sprout, shoot."),
        match(1, "Match each tree of verse 31 to its identification as the card gives it.",
              [["बदरी", "jujube"], ["शाल्मली", "silk-cotton tree"], ["शैलू", "probably the Indian cherry"],
               ["धन्वन", "probably Grewia"], ["ऐरावणी", "unidentified"]],
              "Badarī and śālmalī are standard; śailū and dhanvana probable; airāvaṇī unidentified.",
              "बदरी = jujube; शाल्मली = silk-cotton; शैलू = Indian cherry (probable); धन्वन = Grewia (probable)."),
        order(2, "Put the members of the compound in verse 31, line 2, in order.",
              ["बदरी", "ऐरावणी", "शैलू", "शाल्मली", "धन्वन", "अङ्कुराः"],
              "Five tree names, and अङ्कुराः closes the compound.",
              "बदरी · ऐरावणी · शैलू · शाल्मली · धन्वन · अङ्कुराः.",
              role="extend",
              teaches="Line 2 of verse 31 is one compound: badarī, airāvaṇī, śailū, śālmalī, dhanvana, closed by अङ्कुराः (sprouts)."),
        mcq("discriminate", 3, "Which split of बदर्यैरावणी in verse 31 is right?",
            ("बदरी + ऐरावणी",
             "ई + ऐ → यै: बदर्यैरावणी."),
            [("बदरी + एरावणी", "ई + ए gives ये: it would read बदर्येरावणी."),
             ("बदर + ऐरावणी", "अ + ऐ gives ऐ: it would read बदरैरावणी."),
             ("बदरीः + ऐरावणी", "-ईः before a vowel becomes -ईर्: बदरीरैरावणी.")],
            "बदरी (jujube) + ऐरावणी (unidentified).",
            "ई + unlike vowel → य् + vowel."),
        mcq("apply", 4, "A reader takes अङ्कुराः in verse 31 with dhanvana only. What does the card take?",
            ("The sprouts of every tree named",
             "The notes take अङ्कुराः to govern all the names."),
            [("The sprouts of dhanvana alone", "The card takes अङ्कुराः with all the names."),
             ("The sprouts of badarī alone", "Badarī is first, but अङ्कुराः ends the whole compound."),
             ("The sprouts of none of these", "The verse names the trees whose sprouts are meant.")],
            "अङ्कुराः closes one dvandva and applies to each member.",
            "A word closing a dvandva goes with all its members."),
        mcq("transfer", 5, "Like बदरी + ऐरावणी → बदर्यैरावणी, how does invented नीलिनी + अङ्कुराः join?",
            ("नीलिन्यङ्कुराः",
             "ई before an unlike vowel becomes य्: नीलिन्यङ्कुराः."),
            [("नीलिनीङ्कुराः", "ई does not swallow a following अ; it becomes य्."),
             ("नीलिनेङ्कुराः", "ए arises from अ + इ, not from ई + अ."),
             ("नीलिन्याङ्कुराः", "या would need a long आ; अङ्कुराः begins with short अ.")],
            "ई + अ → य (the vowel after य् stays as it is).",
            "ई + unlike vowel → य् + vowel.",
            teaches="Final इ/ई before an unlike vowel becomes य् (बदरी + ऐरावणी → बदर्यैरावणी; नीलिनी + अङ्कुराः → नीलिन्यङ्कुराः)."),
    ],
}

# ---------------------------------------------------------------- unit 32
AUTHORED["32"] = {
    "title": "समाक्षिकाः क्षीरयुताः सासृजाः पिच्छिलाः स्मृताः",
    "question": "What are the sprouts joined with in verse 32, and what are they held to be?",
    "rule": ("The sprouts of line 05.04.60, with honey, joined with milk and with blood, are held to be picchila (slimy). "
             "Line 2 begins a new list: kola (jujube) with kataka, darbha, pāṭhā and others."),
    "limits": ("माक्षिक is taken as honey (it can also name a mineral). Whether picchila names a kind is not stated. Line 2's compound is "
               "flagged (एलवालु is conjectured) and kola can also be a measure; no questions on line 2."),
    "explain_hi": ("पिछली पंक्ति के अंकुर इस श्लोक का कर्ता हैं। वे माक्षिक यानी शहद सहित, दूध से युक्त और असृज् यानी रक्त सहित "
                   "‘पिच्छिल’ यानी चिपचिपे माने गए हैं। माक्षिक एक खनिज का नाम भी हो सकता है, पर यहाँ शहद लिया गया। "
                   "दूसरी पंक्ति एक नई सूची शुरू करती है: कोल यानी बेर, कतक यानी निर्मली, काण्डेक्षु, दर्भ यानी कुश, पाठा और अनुमानित एलवालु; "
                   "यह बात पंक्ति ०५.०४.६३ में पूरी होती है।"),
    "hook": "अंकुर + शहद + दूध + रक्त = पिच्छिल, चिपचिपा।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "What are the sprouts held to be in verse 32?",
            ("Picchila (slimy)",
             "पिच्छिलाः स्मृताः: they are held to be slimy."),
            [("Lekhana (scraping)", "Scraping was said of triphalā juice, line 05.04.58."),
             ("Saṃgrāhika (binding)", "Binding closed the list of line 05.04.56."),
             ("Dāhaghna (burning-removing)", "That is said in line 05.04.63, not here.")],
            "समाक्षिकाः क्षीरयुताः सासृजाः पिच्छिलाः स्मृताः.",
            "पिच्छिल = slimy."),
        match(1, "Match each word of verse 32, line 1, to its meaning.",
              [["माक्षिक", "honey"], ["क्षीर", "milk"], ["असृज्", "blood"],
               ["पिच्छिल", "slimy"], ["स्मृत", "held to be"]],
              "Line 1 names three additions and the result.",
              "माक्षिक = honey; क्षीर = milk; असृज् = blood; पिच्छिल = slimy; स्मृत = held to be."),
        order(2, "Put the words of verse 32, line 1, in the verse's order.",
              ["समाक्षिकाः", "क्षीरयुताः", "सासृजाः", "पिच्छिलाः", "स्मृताः"],
              "With honey, joined with milk, with blood, slimy, held to be.",
              "समाक्षिकाः · क्षीरयुताः · सासृजाः · पिच्छिलाः · स्मृताः.",
              role="extend",
              teaches="Line 1 of verse 32 adds honey, milk and blood to the sprouts and calls them picchila (slimy)."),
        mcq("discriminate", 3, "In समाक्षिकाः and सासृजाः of verse 32, what does the first part स- mean?",
            ("With, together with",
             "स- in a bahuvrīhi means having, with: with honey, with blood."),
            [("Without, lacking", "Without would be अ- or निर्-, not स-."),
             ("Very much, greatly", "Very would be अति-, not स-."),
             ("Good, well made", "Good would be सु-, not स-.")],
            "स-माक्षिक = with honey; स-असृज् = with blood (अ + अ → आ: सासृजाः).",
            "स- (bahuvrīhi) = with."),
        multi("apply", 4, "Which does verse 32 say the sprouts are with or joined with?",
              [("Honey (माक्षिक)", "Right: समाक्षिकाः, with honey."),
               ("Milk (क्षीर)", "Right: क्षीरयुताः, joined with milk."),
               ("Blood (असृज्)", "Right: सासृजाः, with blood."),
               ("Ghee (घृत)", "Ghee is not named in verse 32, line 1."),
               ("Oil (तैल)", "Oil is not named in verse 32.")],
              [0, 1, 2],
              "Three additions: honey, milk and blood.",
              "Picchila sprouts: with honey, milk, blood."),
        mcq("transfer", 5, "Like समाक्षिकाः (with honey), which invented word means with ghee, qualifying masculine plural sprouts?",
            ("सघृताः",
             "स- + घृत, masculine nominative plural -आः, like समाक्षिकाः."),
            [("सघृतः", "Singular; the sprouts are plural."),
             ("अघृताः", "अ- means without, not with."),
             ("सुघृताः", "सु- means good, not with.")],
            "स- (with) + noun, declined like the noun it qualifies.",
            "स- + noun = having, with.",
            teaches="A bahuvrīhi with स- means having/with and agrees with its noun: समाक्षिकाः (with honey), सघृताः (with ghee)."),
    ],
}

# ---------------------------------------------------------------- unit 33
AUTHORED["33"] = {
    "title": "दाहघ्नः सघृतक्षीरो द्वितीयश्चोत्पलादिभिः",
    "question": "Which two kinds against burning does verse 33 name, and what is cooked with śālmali stalks?",
    "rule": ("One destroying burning (dāha) is with ghee and milk; a second is with utpala and the rest. Then a fistful of śālmali "
             "stalks, cooked in milk, with ghee; that sentence runs on to line 05.04.65."),
    "limits": ("Second of what is not stated. मुष्टिं (accusative) does not agree with the nominatives सिद्धः, अन्वितः; the grammar is "
               "loose and the verb lies outside the unit. Utpala is probably the blue water lily."),
    "explain_hi": ("यह श्लोक जलन यानी दाह को नष्ट करने वाले दो प्रकार बताता है: पहला घी और दूध सहित, दूसरा उत्पल यानी प्रायः नीलकमल आदि के साथ। "
                   "‘द्वितीय’ किसका दूसरा है, यह नहीं कहा गया। "
                   "दूसरी पंक्ति में शाल्मली यानी सेमल के डंठलों की एक मुट्ठी है, दूध में पकाई हुई और घी से युक्त। "
                   "व्याकरण ढीला है: ‘मुष्टिं’ द्वितीया है, पर ‘सिद्धः’ और ‘अन्वितः’ प्रथमा; वाक्य पंक्ति ०५.०४.६५ के ‘हितः प्रवाहणे’ तक चलता है।"),
    "hook": "जलन में: घी-दूध वाला पहला, उत्पल वाला दूसरा; फिर मुट्ठी-भर सेमल-डंठल दूध में।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "What does the first kind of verse 33 destroy?",
            ("Burning (dāha)",
             "दाहघ्नः: destroying burning."),
            [("Pain (śūla)", "Śūla is not named in verse 33."),
             ("Swelling (śotha)", "Swelling is not named in verse 33."),
             ("Thirst (tṛṣṇā)", "Thirst is not named in verse 33.")],
            "दाह + घ्न = destroying burning.",
            "-घ्न = destroying."),
        match(1, "Match each word of verse 33 to its meaning as the card gives it.",
              [["दाहघ्न", "destroying burning"], ["उत्पल", "probably blue water lily"], ["मुष्टि", "fistful"],
               ["वृन्त", "stalk"], ["क्षीरसिद्ध", "cooked in milk"]],
              "Utpala is a probable identification; the rest are plain words.",
              "दाहघ्न = destroying burning; उत्पल = blue water lily (probable); मुष्टि = fistful; वृन्त = stalk; क्षीरसिद्ध = cooked in milk."),
        order(2, "Put these phrases of verse 33 in the verse's order.",
              ["दाहघ्नः", "सघृतक्षीरो", "द्वितीयश्चोत्पलादिभिः", "मुष्टिं", "शाल्मलिवृंतानां", "क्षीरसिद्धो घृतान्वितः"],
              "The first kind, its additions, the second kind; then the fistful, the stalks, and how it is cooked.",
              "दाहघ्नः · सघृतक्षीरो · द्वितीयश्चोत्पलादिभिः · मुष्टिं · शाल्मलिवृंतानां · क्षीरसिद्धो घृतान्वितः.",
              role="extend",
              teaches="Verse 33 gives two burning-removing kinds (with ghee and milk; with utpala) and then a fistful of śālmali stalks cooked in milk with ghee."),
        mcq("discriminate", 3, "Which split of द्वितीयश्चोत्पलादिभिः in verse 33 is right?",
            ("द्वितीयः + च + उत्पलादिभिः",
             "-अः before च → -अश्; अ + उ → ओ (चोत्पल…)."),
            [("द्वितीयः + च + ओत्पलादिभिः", "अ + ओ gives औ: it would read चौत्पल…."),
             ("द्वितीयम् + च + उत्पलादिभिः", "म् before च becomes anusvara or ञ्, not श्."),
             ("द्वितीयाः + च + उत्पलादिभिः", "-आः + च keeps a long आ: द्वितीयाश्चो….")],
            "द्वितीयः (the second) + च (and) + उत्पलादिभिः (with utpala and the rest).",
            "-अः + च → -अश्च; अ + उ → ओ."),
        mcq("apply", 4, "Which kind of verse 33 comes with utpala and the rest?",
            ("The second (द्वितीयः)",
             "द्वितीयश्चोत्पलादिभिः: and the second, with utpala and the rest."),
            [("The first, with ghee and milk", "The first is सघृतक्षीरः; utpala goes with the second."),
             ("The fistful of śālmali stalks", "The stalks are cooked in milk with ghee; utpala is not named with them."),
             ("None; utpala is a measure here", "Utpala is a plant, probably the blue water lily.")],
            "Two burning-removing kinds: the first with ghee and milk, the second with utpala.",
            "Second kind = with utpala and the rest."),
        mcq("transfer", 5, "Like दाहघ्नः (destroying burning), which invented word means destroying fever (ज्वर), for a masculine noun?",
            ("ज्वरघ्नः",
             "Noun + -घ्न, masculine nominative singular -अः, like दाहघ्नः."),
            [("ज्वरघ्ना", "Feminine; the noun is masculine."),
             ("ज्वरघ्नम्", "Neuter (or accusative); the noun is masculine nominative."),
             ("ज्वरहतः", "हत means struck, not destroying.")],
            "-घ्न (destroying) closes a tatpuruṣa and agrees with its noun.",
            "X-घ्न = destroying X.",
            teaches="A tatpuruṣa in -घ्न means destroying: दाहघ्नः (destroying burning), ज्वरघ्नः (destroying fever)."),
    ],
}

# ---------------------------------------------------------------- unit 34
AUTHORED["34"] = {
    "title": "हितः प्रवाहणे",
    "question": "In which condition is the preparation beneficial in verse 34, and what is prepared with milk?",
    "rule": ("Beneficial in pravāhaṇa (straining); likewise with the stalks of śālmalaka. Then karbudāra, āḍhakī, nīpa and vidula, "
             "prepared with milk; the unit does not say what these are for."),
    "limits": ("तद्वद्धृंतैः is read as तद्वद् वृन्तैः and आढकींनप as आढकी-नीप (both flagged). Śālmalaka is taken as the silk-cotton tree. "
               "Karbudāra and vidula are disputed. What is beneficial stands in line 05.04.64."),
    "explain_hi": ("यह श्लोक पंक्ति ०५.०४.६४ का वाक्य पूरा करता है: दूध में पकी, घी से युक्त सेमल-डंठलों की वह तैयारी प्रवाहण यानी जोर लगाने में हितकर है। "
                   "‘वैसे ही’ शाल्मलक के डंठलों से भी; शाल्मलक को सेमल ही माना गया है। "
                   "दूसरी पंक्ति में कर्बुदार, आढकी यानी अरहर, नीप यानी प्रायः कदम्ब और विदुल हैं, जो दूध के साथ तैयार किए जाते हैं; "
                   "ये किसके लिए हैं, यह इस पंक्ति में नहीं कहा गया। दो शब्द छपाई में बिगड़े हैं और उनका सुधार अनुमानित है।"),
    "hook": "प्रवाहण में सेमल के डंठल; फिर कर्बुदार-अरहर-कदम्ब-विदुल दूध में।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In which condition is the preparation beneficial, by verse 34?",
            ("Pravāhaṇa (straining)",
             "हितः प्रवाहणे: beneficial in straining."),
            [("Dāha (burning)", "Burning was the topic of line 05.04.63."),
             ("Atiyoga (excess)", "Excess comes in line 05.04.71."),
             ("Parikarta (cutting pain)", "Cutting pain comes in line 05.04.67.")],
            "प्रवाहणे is locative: in straining.",
            "प्रवाहण = straining."),
        match(1, "Match each clear word of verse 34 to its meaning.",
              [["हितः", "beneficial"], ["प्रवाहणे", "in straining"], ["शाल्मलक", "taken as the silk-cotton tree"],
               ["क्षीरसाधितैः", "prepared with milk"]],
              "These are the unflagged words of the unit.",
              "हितः = beneficial; प्रवाहणे = in straining; शाल्मलक = silk-cotton tree; क्षीरसाधित = prepared with milk."),
        order(2, "Put these clear words of verse 34 in the verse's order.",
              ["हितः", "प्रवाहणे", "शाल्मलकस्य च", "क्षीरसाधितैः"],
              "Beneficial, in straining, (stalks) of śālmalaka, then (drugs) prepared with milk at the end of line 2.",
              "हितः · प्रवाहणे · शाल्मलकस्य च · क्षीरसाधितैः.",
              role="extend",
              teaches="Verse 34 opens with the benefit (हितः प्रवाहणे), repeats the stalk remedy with śālmalaka, and closes with drugs prepared with milk."),
        mcq("discriminate", 3, "Which word of verse 34 is a locative that names the condition?",
            ("प्रवाहणे",
             "-ए locative singular: in straining."),
            [("हितः", "Nominative singular: beneficial."),
             ("क्षीरसाधितैः", "Instrumental plural: prepared with milk."),
             ("शाल्मलकस्य", "Genitive singular: of śālmalaka.")],
            "The condition stands in the locative: प्रवाहणे.",
            "Condition in the locative (-ए): in X."),
        mcq("apply", 4, "What does verse 34 say the milk-prepared drugs of line 2 are for?",
            ("The unit does not say",
             "Line 2 has no verb and no noun for a condition."),
            [("For straining, as line 2 says", "Straining is in line 1; line 2 names no condition."),
             ("For burning, as line 2 says", "Burning is not named in verse 34."),
             ("For excess, as line 2 says", "Excess is not named in verse 34.")],
            "The notes say the unit has no verb and no noun for the condition.",
            "Supply no use the text does not state."),
        mcq("transfer", 5, "Like प्रवाहणे (in straining), which invented form of दाह means in burning?",
            ("दाहे",
             "Locative singular -ए, like प्रवाहणे."),
            [("दाहेन", "Instrumental: by or with burning."),
             ("दाहात्", "Ablative: from burning."),
             ("दाहस्य", "Genitive: of burning.")],
            "The locative names the condition in which a remedy is beneficial.",
            "-ए (locative) = in.",
            teaches="Kalpasthāna names the condition in the locative: प्रवाहणे (in straining), दाहे (in burning)."),
    ],
}

# ---------------------------------------------------------------- unit 35
AUTHORED["35"] = {
    "title": "परिकर्त्ते तथा वृंतैः",
    "question": "Which remedy does verse 35 give for parikarta, and which for parisrava?",
    "rule": ("In parikarta (cutting pain): likewise with stalks born of śrīparṇī and kovidāra. In parisrava (flowing out): cooked milk; "
             "its drugs follow in line 05.04.69."),
    "limits": ("The last word, सदृशविपुनर्नवं, cannot be restored (it may contain punarnavā); no question on it. Śrīparṇī and kovidāra "
               "are probable. The text does not itself call these basti complications; the data adds that as reviewer context."),
    "explain_hi": ("यह श्लोक दो स्थितियाँ और उनके उपाय बताता है। परिकर्त यानी काटने जैसी पीड़ा में, वैसे ही श्रीपर्णी यानी प्रायः गम्भारी "
                   "और कोविदार यानी प्रायः कचनार से उत्पन्न डंठलों से। परिस्रव यानी बहने (स्राव) में सिद्ध किया हुआ दूध; "
                   "किन द्रव्यों के साथ, यह पंक्ति ०५.०४.६९ में है। अन्तिम शब्द ‘सदृशविपुनर्नवं’ पढ़ा नहीं जाता; उसमें पुनर्नवा का नाम लगता है। "
                   "ये नाम बस्ति के व्यापदों में भी आते हैं, पर यह पाठ स्वयं ऐसा नहीं कहता।"),
    "hook": "काटने-सी पीड़ा: गम्भारी-कचनार के डंठल; बहाव: पका दूध।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "Which remedy does verse 35 give in parisrava (flowing out)?",
            ("Cooked milk (पयः सिद्धं)",
             "परिस्रवे पयः सिद्धं: in parisrava, cooked milk."),
            [("Stalks of śrīparṇī and kovidāra", "Those are for parikarta, line 1."),
             ("Honey, añjana and ghee", "These come in line 05.04.71, not in verse 35."),
             ("Sprouts of badarī", "Sprouts were in line 05.04.60.")],
            "Line 2 pairs parisrava with milk, cooked.",
            "परिस्रव → सिद्ध पयः."),
        match(1, "Match each word of verse 35 to its meaning as the card gives it.",
              [["परिकर्त", "cutting pain"], ["परिस्रव", "flowing out, discharge"], ["श्रीपर्णी", "probably Gmelina"],
               ["कोविदार", "probably the orchid tree"], ["-ज", "born of"]],
              "Two conditions and the two trees whose stalks are used.",
              "परिकर्त = cutting pain; परिस्रव = flowing out; श्रीपर्णी = Gmelina (probable); कोविदार = orchid tree (probable); -ज = born of."),
        order(2, "Put these words of verse 35 in the verse's order.",
              ["परिकर्त्ते", "तथा", "वृंतैः", "श्रीपर्णीकोविदारजैः", "परिस्रवे", "पयः सिद्धं"],
              "Condition 1, likewise, stalks, their source; condition 2, cooked milk.",
              "परिकर्त्ते · तथा · वृंतैः · श्रीपर्णीकोविदारजैः · परिस्रवे · पयः सिद्धं.",
              role="extend",
              teaches="Each line of verse 35 opens with a condition in the locative and then gives its remedy: stalks for parikarta, cooked milk for parisrava."),
        mcq("discriminate", 3, "Which pairing of condition and remedy does verse 35 state?",
            ("Parikarta → stalks; parisrava → milk",
             "Line 1: परिकर्ते … वृन्तैः; line 2: परिस्रवे पयः सिद्धम्."),
            [("Parikarta → milk; parisrava → stalks", "Reversed: the stalks go with parikarta."),
             ("Both take stalks of śrīparṇī", "Parisrava takes cooked milk."),
             ("Both take the cooked milk", "Parikarta takes the stalks.")],
            "Each locative condition is followed by its own remedy.",
            "परिकर्त → डंठल; परिस्रव → दूध."),
        mcq("apply", 4, "What does -ज in श्रीपर्णीकोविदारजैः tell about the stalks?",
            ("They come from those two trees",
             "-ज = born of: stalks born of śrīparṇī and kovidāra."),
            [("They are mixed with those trees", "Joined or mixed would be -युत, not -ज."),
             ("They are cooked with those trees", "Cooked would be सिद्ध, not -ज."),
             ("They look like those two trees", "Like would be सदृश or -वत्, not -ज.")],
            "-ज (born of) names the source of the stalks.",
            "-ज = born of, from."),
        mcq("transfer", 5, "Like श्रीपर्णीकोविदारजैः (with stalks born of these), which invented word means with (stalks) born of śālmali?",
            ("शाल्मलिजैः",
             "Source + -ज, instrumental plural -ऐः, agreeing with वृन्तैः."),
            [("शाल्मलिजः", "Nominative singular; the stalks are instrumental plural."),
             ("शाल्मलिजान्", "Accusative plural; वृन्तैः is instrumental."),
             ("शाल्मलिजम्", "Neuter singular; वृन्तैः is plural.")],
            "-ज agrees with वृन्तैः in case and number.",
            "-जैः = born of (inst. pl.).",
            teaches="A compound in -ज (born of) agrees with its noun: वृन्तैः श्रीपर्णीकोविदारजैः, वृन्तैः शाल्मलिजैः."),
    ],
}

# ---------------------------------------------------------------- unit 36
AUTHORED["36"] = {
    "title": "आखुकर्णिकया तद्वत्",
    "question": "What is used likewise in verse 36, and which plants does its second line name?",
    "rule": ("With ākhukarṇikā, likewise, joined with taṇḍulīyaka (probably a spiny amaranth). Line 2 names aśvāvarohaka, kākanāsā and "
             "rājakaserukā (probably a kaserukā sedge), which are cooked in line 05.04.71."),
    "limits": ("The cooked milk of line 05.04.68 is carried over but not stated. Ākhukarṇikā and kākanāsā are disputed; aśvāvarohaka "
               "unidentified. राजकसेरुकाः may be one name or two items (rāja, kaserukā); no question rests on that."),
    "explain_hi": ("यह श्लोक बहुत संक्षिप्त है: पंक्ति ०५.०४.६८ का पका दूध मन में रखा जाता है, पर यहाँ कहा नहीं गया। "
                   "‘आखुकर्णिकया’ यानी आखुकर्णिका से (शब्दार्थ ‘चूहे का कान’), उसी प्रकार, जो तण्डुलीयक यानी प्रायः चौलाई से युक्त हो। "
                   "‘युक्तया’ स्त्रीलिंग तृतीया है और ‘आखुकर्णिकया’ से मेल खाता है। "
                   "दूसरी पंक्ति में अश्वावरोहक, काकनासा (शब्दार्थ ‘कौए की नाक’) और राजकसेरुका यानी प्रायः कसेरु की एक जाति हैं; ये पंक्ति ०५.०४.७१ के ‘सिद्धाः’ से जुड़ते हैं।"),
    "hook": "‘चूहे का कान’ चौलाई के साथ; फिर अश्वावरोहक, ‘कौए की नाक’ और राजकसेरु।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What is ākhukarṇikā joined with in verse 36?",
            ("Taṇḍulīyaka (amaranth)",
             "तंदुलीयकयुक्तया: joined with taṇḍulīyaka, probably a spiny amaranth."),
            [("Kākanāsā (crow-nose)", "Kākanāsā is in line 2, a separate item."),
             ("Aśvāvarohaka (unidentified)", "Aśvāvarohaka opens line 2, a separate item."),
             ("Kṣaudra (honey)", "Honey is not named in verse 36.")],
            "आखुकर्णिकया … तण्डुलीयकयुक्तया: with ākhukarṇikā joined with taṇḍulīyaka.",
            "तण्डुलीयक = probably a spiny amaranth."),
        match(1, "Match each plant name of verse 36 to the card's note on it.",
              [["आखुकर्णिका", "lit. mouse-ear; disputed"], ["तण्डुलीयक", "probably a spiny amaranth"],
               ["काकनासा", "lit. crow-nose; disputed"], ["अश्वावरोहक", "unidentified"]],
              "Two literal names, one probable identification, one unidentified.",
              "आखुकर्णिका = mouse-ear (disputed); तण्डुलीयक = amaranth (probable); काकनासा = crow-nose (disputed); अश्वावरोहक = unidentified."),
        order(2, "Put these words of verse 36 in the verse's order.",
              ["आखुकर्णिकया", "तद्वत्", "तंदुलीयकयुक्तया", "अश्वावरोहकः", "काकनासा", "राजकसेरुकाः"],
              "Line 1: the instrumental pair; line 2: three plant names in the nominative.",
              "आखुकर्णिकया · तद्वत् · तंदुलीयकयुक्तया · अश्वावरोहकः · काकनासा · राजकसेरुकाः.",
              role="extend",
              teaches="Line 1 of verse 36 is instrumental (with ākhukarṇikā, joined with taṇḍulīyaka); line 2 lists nominatives cooked in line 05.04.71."),
        mcq("discriminate", 3, "Which word does युक्तया (joined) agree with in verse 36?",
            ("आखुकर्णिकया",
             "Both are feminine instrumental singular."),
            [("अश्वावरोहकः", "Masculine nominative; युक्तया is feminine instrumental."),
             ("काकनासा", "Nominative; युक्तया is instrumental."),
             ("तद्वत्", "An indeclinable, likewise; it takes no agreement.")],
            "तण्डुलीयकयुक्तया qualifies आखुकर्णिकया.",
            "An adjective agrees in gender, case and number."),
        mcq("apply", 4, "What case is आखुकर्णिकया, and what does it mean in verse 36?",
            ("Instrumental: with ākhukarṇikā",
             "-अया is feminine instrumental singular."),
            [("Nominative: ākhukarṇikā itself", "Nominative would be आखुकर्णिका."),
             ("Genitive: of the ākhukarṇikā", "Genitive would be आखुकर्णिकायाः."),
             ("Locative: in the ākhukarṇikā", "Locative would be आखुकर्णिकायाम्.")],
            "आखुकर्णिकया = with ākhukarṇikā (f. inst. sg.).",
            "-आ stems: instrumental -अया."),
        mcq("transfer", 5, "Like आखुकर्णिकया … युक्तया, which invented phrase means with śatāvarī joined with honey?",
            ("शतावर्या मधुयुक्तया",
             "Both feminine instrumental singular, like आखुकर्णिकया … युक्तया."),
            [("शतावर्या मधुयुक्तेन", "-एन is masculine/neuter; शतावरी is feminine."),
             ("शतावरी मधुयुक्ता", "Nominative, not instrumental with."),
             ("शतावर्याः मधुयुक्तायाः", "Genitive/ablative, not instrumental.")],
            "Noun and adjective both in feminine instrumental singular.",
            "f. inst. sg. noun + f. inst. sg. -युक्तया.",
            teaches="A feminine noun in the instrumental takes a feminine instrumental adjective: आखुकर्णिकया … युक्तया, शतावर्या मधुयुक्तया."),
    ],
}

# ---------------------------------------------------------------- unit 37
AUTHORED["37"] = {
    "title": "सिद्धाः क्षीरेऽतियोगे स्युः",
    "question": "In atiyoga, what should be cooked in milk and what is it joined with, according to verse 37?",
    "rule": ("In atiyoga (excess), the drugs of line 05.04.70 should be cooked in milk, joined with honey, añjana and ghee. "
             "Another (preparation) by that very method uses the four beginning with nyagrodha."),
    "limits": ("Excess of what is not stated, nor which añjana. The four of the nyagrodha group are not named in the unit; "
               "चतुर्भिइच is read as चतुर्भिश्च (flagged). अपरः, another, does not say another what."),
    "explain_hi": ("पिछली पंक्ति के द्रव्य (अश्वावरोहक आदि) यहाँ कर्ता हैं: अतियोग यानी अधिकता होने पर वे दूध में सिद्ध किए जाने चाहिए "
                   "और शहद, अञ्जन तथा घी से युक्त हों। अतियोग किसका है और कौन-सा अञ्जन, यह नहीं कहा गया। "
                   "दूसरी पंक्ति: न्यग्रोध यानी बरगद से आरम्भ होने वाले चार द्रव्यों से, उसी विधि से, एक दूसरा। "
                   "चार के नाम इस श्लोक में नहीं हैं; ‘अपरः’ किसका दूसरा है, यह भी नहीं बताया गया।"),
    "hook": "अधिकता में: दूध में पकाओ, शहद-अञ्जन-घी से युक्त करो; बरगद-आदि चार से दूसरा।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In which condition does verse 37 have the drugs cooked in milk?",
            ("Atiyoga (excess)",
             "क्षीरेऽतियोगे: in milk, in atiyoga."),
            [("Pravāhaṇa (straining)", "Straining was named in line 05.04.65."),
             ("Parikarta (cutting pain)", "Cutting pain was named in line 05.04.67."),
             ("Dāha (burning)", "Burning was named in line 05.04.63.")],
            "अतियोगे is the locative of the condition.",
            "अतियोग = excess."),
        match(1, "Match each word of verse 37 to its meaning as the card gives it.",
              [["अतियोग", "excess"], ["क्षौद्र", "honey"], ["अञ्जन", "a collyrium substance"],
               ["घृत", "ghee"], ["अपरः", "another"]],
              "Which añjana is meant is not stated; the word names a collyrium substance.",
              "अतियोग = excess; क्षौद्र = honey; अञ्जन = collyrium substance; घृत = ghee; अपरः = another."),
        order(2, "Put the words of verse 37, line 1, in the verse's order.",
              ["सिद्धाः", "क्षीरे", "अतियोगे", "स्युः", "क्षौद्राञ्जनघृतैः", "युताः"],
              "Cooked, in milk, in excess, should be, with honey-añjana-ghee, joined.",
              "सिद्धाः · क्षीरे · अतियोगे · स्युः · क्षौद्राञ्जनघृतैः · युताः.",
              role="extend",
              teaches="Line 1 of verse 37 says the drugs should be cooked in milk in atiyoga and joined with honey, añjana and ghee."),
        mcq("discriminate", 3, "Which split of क्षीरेऽतियोगे in verse 37 is right?",
            ("क्षीरे + अतियोगे",
             "-ए + अ → -एऽ: the avagraha marks the dropped अ."),
            [("क्षीरः + अतियोगे", "-अः + अ gives -ओऽ: it would read क्षीरोऽतियोगे."),
             ("क्षीरम् + अतियोगे", "म् before a vowel stays: it would read क्षीरमतियोगे."),
             ("क्षीरे + इतियोगे", "-ए + इ gives -अ इ, with no avagraha: क्षीर इतियोगे.")],
            "क्षीरे (in milk) + अतियोगे (in excess).",
            "-ए + अ → -एऽ."),
        mcq("apply", 4, "What does स्युः add to सिद्धाः in verse 37?",
            ("Should be: they should be cooked",
             "स्युः is optative 3rd plural of √अस्."),
            [("Were: they were already cooked", "स्युः is optative, not past."),
             ("Will be: they will be cooked", "Not a future; the gram label is optative."),
             ("Are not: they are not cooked", "There is no negation in verse 37.")],
            "सिद्धाः स्युः = they should be cooked.",
            "स्युः = should be (opt. 3 pl.)."),
        mcq("transfer", 5, "Like तेन + एव → तेनैव in verse 37, how does invented सह + एव join?",
            ("सहैव",
             "अ + ए → ऐ, as in तेनैव."),
            [("सहेव", "अ + ए gives ऐ, not ए."),
             ("सहयेव", "य् comes from इ before a vowel, not from अ."),
             ("सहौव", "औ comes from अ + ओ/औ, not अ + ए.")],
            "Vṛddhi sandhi: अ/आ + ए/ऐ → ऐ.",
            "अ + ए → ऐ.",
            teaches="अ/आ + ए/ऐ becomes ऐ (तेन + एव → तेनैव; सह + एव → सहैव)."),
    ],
}


NOTES_HI = {
    "25": ("विश्वास: निम्न। पंक्तियाँ ०५.०४.४७-४८; पंक्ति ४८ से ५२ तक एक वाक्य (सूची)। text_flags: छपा ‘अर्द्धाद्र्ध’ सम्भवतः ‘अर्द्धार्द्ध’ (र्द्ध उलटा छपा); "
           "‘द्व्येश्वाकु’ ज्ञात शब्द नहीं, सम्भवतः ‘द्व्यैक्ष्वाकु’ (दो इक्ष्वाकु, कड़वी तूम्बी), पर निश्चित नहीं, इसलिए अविभक्त और अपहचाना। "
           "‘फल’ अलग द्रव्य है या उसी पौधे का फल, स्पष्ट नहीं। ‘अतः’ = इसलिए या यहाँ से आगे। "
           "पहचान: कोशातकी सम्भावित (तोरई), जीमूत सम्भावित (देवदाली), वत्सक = कुटज (मानक)। "
           "संधि जाँची: बस्तीनतः = बस्तीन् + अतः; अतश्चित्रान् = अतः + चित्रान्; चित्रान्प्रचक्षते = चित्रान् + प्रचक्षते।"),
    "26": ("विश्वास: मध्यम। पंक्तियाँ ०५.०४.४९-५०, पंक्ति ४८ की सूची जारी, क्रिया नहीं। ‘दन्तीद्रवन्तीजं’ = दन्ती और द्रवन्ती से उत्पन्न; "
           "क्या उत्पन्न, नहीं कहा गया (सम्भवतः मूल, पर जोड़ा नहीं गया)। अन्त का ‘फलं’ अकेला है, किसका फल, यह नहीं कहा। "
           "छपाई: ‘दंतीद्रवंतिजं’ में अनुस्वार और ह्रस्व इ (द्रवन्ती का ई समास में ह्रस्व छपा)। "
           "पहचान: त्रिवृत् मानक; श्यामा विवादित (परम्परा में काली त्रिवृत्, पर यहाँ त्रिवृत् के साथ अलग गिनी गई); दन्ती, नीलिनी सम्भावित; द्रवन्ती, प्रकीर्या, उदकीर्या, क्षीरिणी विवादित। "
           "संधि जाँची: श्यामात्रिवृतोर्मूलं = श्यामात्रिवृतोः + मूलम्; चोदकीर्या = च + उदकीर्या।"),
    "27": ("विश्वास: मध्यम। पंक्तियाँ ०५.०४.५१-५२; पंक्ति ४८ से चला वाक्य यहाँ बंद। text_flag: छपा ‘रोधं’ = रोध्र (संयुक्ताक्षर का र् छूटा), यही रूप पंक्ति ०५.०४.५६ में भी। "
           "‘हैं’ क्रिया संस्कृत में नहीं, पुल्लिंग बहुवचन प्रथमा पंक्ति ४८-५१ के द्रव्यों से जुड़ती है। "
           "पहचान: कम्पिल्लक (कमीला) और रोध्र (लोध) मानक; समला अपहचानी; शङ्खिनी विवादित। "
           "पक्वाशय: डेटा में ‘मानक, बड़ी आँत’, शब्दावली में इसे ‘सम्भवतः’ लिखने का नियम है; यहाँ ‘पचे अन्न का स्थान’ कहा। "
           "संधि जाँची: सकल्कसैंधवयुताः = स + कल्क + सैन्धव + युताः।"),
    "28": ("विश्वास: निम्न। पंक्तियाँ ०५.०४.५३-५४, नई सूची (५३-५६) जिसे पंक्ति ५६ में ‘संग्राहिक’ कहा गया। "
           "text_flags: छपा ‘धातुकी’ = धातकी (उ/अ की भूल); ‘तक्रींर्’ शब्द नहीं, पंक्ति में एक अक्षर कम है। "
           "खुला बिन्दु (OPEN ०५.०४.५३): ‘तक्राम्र’ जैसा सुधार केवल अक्षर-गिनती पर टिका है और ज्ञात द्रव्य नहीं; इसे सुधार न माना जाए। इस पर प्रश्न नहीं। "
           "‘मूल’ केवल जीवन्ती का है या और का भी, तय नहीं। प्रग्रह अपहचाना (अन्यत्र ‘नियन्त्रण’); खदिरी विवादित (खदिर जैसा, या लज्जालु का पर्याय); "
           "शमी सम्भावित; पिण्डीतका विवादित (मदन का भी नाम)। ‘यवाः’ बहुवचन: यव के दाने।"),
    "29": ("विश्वास: निम्न। पंक्तियाँ ०५.०४.५५-५६; पंक्ति ५३ से चली सूची यहाँ ‘इति’ से बंद। ‘प्रियङ्गुरक्तमूले’ अनिश्चित: ‘मूले’ द्विवचन या सप्तमी, विभाजन दो तरह; इस पर प्रश्न नहीं। "
           "text_flag: ‘रोधमिति’ में रोध = रोध्र (पंक्ति ०५.०४.५१ जैसा)। वट आदि गण के सदस्य पाठ में नहीं। "
           "पहचान: वट, किंशुक, रोध्र मानक; जाति, यूथिका सम्भावित; प्रियङ्गु विवादित; भैरणी अपहचानी। "
           "संधि जाँची: वटाद्याः = वट + आद्याः; संग्राहिका मताः = संग्राहिकाः + मताः (आः के बाद घोष व्यंजन, विसर्ग लोप)। आधी पंक्तियाँ आठ-आठ अक्षर की।"),
    "30": ("विश्वास: मध्यम। पंक्तियाँ ०५.०४.५७-५८। text_flag: छपा ‘काथ’ = क्वाथ (काढ़ा)। ‘ग्राहि’ विशेषण है या गण का नाम, तय नहीं। "
           "इकाई में ‘बस्ति’ जैसा कोई संज्ञा-शब्द नहीं; पंक्ति ०५.०४.४७ से चले प्रकारों की सूची सम्भावित पर अकथित। "
           "पहचान: उषक = खारी मिट्टी (सम्भावित); अम्बष्ठा विवादित (प्रायः पाठा); त्रिफला = हरड़, बहेड़ा, आँवला (मानक)। "
           "संधि जाँची: प्रियंग्वंबष्ठा = प्रियङ्गु + अम्बष्ठा; उषकादिप्रतीवापो = …प्रतीवापः + (ल); लेखनस्त्रिफलारसः = लेखनः + त्रिफलारसः।"),
    "31": ("विश्वास: निम्न। पंक्तियाँ ०५.०४.५९-६०। text_flags: ‘कल्कैन’ वैध रूप नहीं, ‘कल्केन’ पढ़ा; पर तब आधी पंक्ति में चौदह ही अक्षर, कोई शब्द खोया हो सकता है; "
           "पूरी पंक्ति proofread में ‘मधुककल्केन’ सुझाई गई। इसलिए पंक्ति १ पर प्रश्न नहीं। ‘रस’ = रस (शोरबा या रस, निर्दिष्ट नहीं)। "
           "पंक्ति ६० और ६१ एक कथन (‘अङ्कुराः … पिच्छिलाः स्मृताः’)। पहचान: बदरी, शाल्मली मानक; शैलू, धन्वन सम्भावित; ऐरावणी अपहचानी; मधुक सम्भावित मुलेठी (महुआ भी हो सकता)। "
           "संधि जाँची: बदर्यैरावणी = बदरी + ऐरावणी; धन्वनांकुराः = धन्वन + अङ्कुराः।"),
    "32": ("विश्वास: निम्न। पंक्तियाँ ०५.०४.६१-६२। कर्ता पंक्ति ६० के अंकुर। ‘माक्षिक’ शहद लिया (खनिज भी हो सकता)। ‘पिच्छिल’ किसी प्रकार का नाम है या नहीं, नहीं कहा। "
           "text_flag: ‘पाठेशुवालुभिः’ विभाजित नहीं होता; ‘पाठा + एलवालु’ अनुमानित सुधार। ‘कोल’ = बेर (फल), माप वाला अर्थ नहीं लिया। "
           "खुला बिन्दु (OPEN ०५.०४.६२): कतक का टैग ‘सम्भावित’ है पर अनुवाद बिना संकोच ‘निर्मली’; इस पर प्रश्न नहीं। पंक्ति ६२-६३ साथ हैं। "
           "संधि जाँची: सासृजाः = स + असृजाः; समाक्षिकाः = स + माक्षिकाः।"),
    "33": ("विश्वास: मध्यम। पंक्तियाँ ०५.०४.६३-६४। ‘द्वितीयः’ किसका दूसरा, अकथित (दो दाहनाशक प्रकार)। "
           "पंक्ति ६४-६५ एक वाक्य (‘हितः प्रवाहणे’ पंक्ति ६५ में)। ‘मुष्टिं’ द्वितीया, पर ‘सिद्धः’, ‘अन्वितः’ पुल्लिंग प्रथमा: मेल नहीं; व्याकरण ढीला, अनुवाद शब्दशः। "
           "पहचान: उत्पल सम्भावित (नीलकमल); शाल्मली मानक। "
           "संधि जाँची: सघृतक्षीरो = सघृतक्षीरः + (द); द्वितीयश्चोत्पलादिभिः = द्वितीयः + च + उत्पलादिभिः; क्षीरसिद्धो घृतान्वितः = क्षीरसिद्धः + घृत + अन्वितः।"),
    "34": ("विश्वास: मध्यम। पंक्तियाँ ०५.०४.६५-६६; पंक्ति ६४ का वाक्य यहाँ पूरा। text_flags: ‘तद्वद्धृंतैः’ = तद्वद् वृन्तैः (‘धृन्त’ शब्द नहीं); "
           "‘आढकींनप’ = आढकी + नीप (कर्बुदार-नीप-विदुल का गण ग्रन्थ में अन्यत्र भी)। इन पर प्रश्न नहीं। शाल्मलक = सेमल (सम्भावित)। प्रवाहण = मल-त्याग में जोर लगाना (मानक)। "
           "पंक्ति ६६ में न क्रिया, न रोग का नाम। पहचान: आढकी मानक (अरहर); नीप सम्भावित (कदम्ब); कर्बुदार, विदुल विवादित।"),
    "35": ("विश्वास: निम्न। पंक्तियाँ ०५.०४.६७-६८। सामान्यीकरण: छपा ‘परिकर्त्ते’ = परिकर्ते (र्त्त → र्त)। परिकर्त = काटने-सी पीड़ा (परिकर्तिका इसका सामान्य नाम)। "
           "text_flag: ‘सदृशविपुनर्नवं’ विभाजित नहीं होता, सम्भवतः ‘सदृश’ और पुनर्नवा का नाम; अविभक्त, अनूदित नहीं। इस पर प्रश्न नहीं। "
           "पंक्ति ६८-६९ साथ (उन द्रव्यों के साथ पका दूध)। पहचान: श्रीपर्णी (गम्भारी), कोविदार (कचनार) सम्भावित। "
           "समीक्षक-टिप्पणी: परिस्राव, परिकर्तिका बस्ति-व्यापद् के नाम हैं, पर पाठ स्वयं ऐसा नहीं कहता।"),
    "36": ("विश्वास: मध्यम। पंक्तियाँ ०५.०४.६९-७०। ‘युक्तया’ स्त्रीलिंग तृतीया, ‘आखुकर्णिकया’ से मेल। पंक्ति ६८ का पका दूध अनुवर्तित, कहा नहीं गया। "
           "पंक्ति ७०-७१ साथ (‘सिद्धाः … स्युः’)। ‘राजकसेरुकाः’ दो तरह पढ़ा जा सकता है: एक नाम राजकसेरुका, या ‘राज’ और ‘कसेरुका’ दो द्रव्य; अनुवाद पहला लेता है; इस पर प्रश्न नहीं। "
           "पहचान: तण्डुलीयक, कसेरुका सम्भावित; आखुकर्णिका, काकनासा विवादित; अश्वावरोहक अपहचाना। "
           "संधि जाँची: तद्वत्तंदुलीयक = तद्वत् + तण्डुलीयक।"),
    "37": ("विश्वास: मध्यम। पंक्तियाँ ०५.०४.७१-७२; कर्ता पंक्ति ७० के द्रव्य। ‘क्षीरे’ को ‘सिद्धाः’ के साथ लिया (दूध में पकाए)। अतियोग किसका, नहीं कहा; अञ्जन कौन-सा, विवादित। "
           "text_flag: ‘चतुर्भिइच’ = चतुर्भिश्च। चार न्यग्रोधादि द्रव्य इस इकाई में नहीं; वाक्य अगली पंक्ति (०५.०४.७३) की सूची में चलता है। ‘अपरः’ किसका दूसरा, नहीं कहा। "
           "संधि जाँची: क्षीरेऽतियोगे = क्षीरे + अतियोगे; तेनैव = तेन + एव; विधिनाऽपरः = विधिना + अपरः (छपाई का अवग्रह); …घृतैर्युताः = घृतैः + युताः।"),
}


AIDS = {
    "25": {
        "chunks": "अर्द्धाद्र्धविहितान् (छपाई संदिग्ध) | बस्तीनतश्चित्रान्प्रचक्षते ‖ कोशातकी | द्व्येश्वाकु (अस्पष्ट) | फल | जीमूत | वत्सकाः।",
        "anchors": "अर्ध = आधा · विहित = विधान किया · चित्र = विविध · प्रचक्षते = कहते हैं · कोशातकी = प्रायः तोरई · जीमूत = प्रायः देवदाली · वत्सक = कुटज।",
        "sandhi": "न् + स्वर → जुड़ता है: बस्तीन् + अतः → बस्तीनतः; अः + च → अश्च: अतः + चित्रान् → अतश्चित्रान्।",
    },
    "26": {
        "diagram": {"groups": [{"label": "पंक्ति १", "items": ["श्यामा और त्रिवृत् का मूल", "दन्ती-द्रवन्ती से उत्पन्न"]},
                               {"label": "पंक्ति २", "items": ["प्रकीर्या", "उदकीर्या", "क्षीरिणी", "नीलिनी", "फल"]}]},
        "chunks": "श्यामात्रिवृतोर्मूलं | तथा | दंतीद्रवंतिजं ‖ प्रकीर्या | चोदकीर्या च | क्षीरिणी | नीलिनी | फलं।",
        "sandhi": "ओः + घोष → ओर्: त्रिवृतोः + मूलम् → त्रिवृतोर्मूलम्; अ + उ → ओ: च + उदकीर्या → चोदकीर्या।",
        "anchors": "त्रिवृत् = निशोथ · दन्ती = प्रायः जंगली जमालगोटा · नीलिनी = प्रायः नील · क्षीरिणी = शब्दार्थ ‘दूध वाली’ · -ज = से उत्पन्न।",
    },
    "27": {
        "diagram": {"groups": [{"label": "सूची का अन्त", "items": ["समला", "शङ्खिनी", "रोध्र (छपा रोधं)", "कम्पिल्लक का फल"]},
                               {"label": "युक्त", "items": ["कल्क", "सैन्धव"]},
                               {"label": "कर्म", "items": ["पक्वाशय-शोधन"]}]},
        "chunks": "समला | शंखिनी | रोधं | फलं कंपिल्लकस्य च ‖ सकल्कसैंधवयुताः | पक्वाशयविशोधनाः।",
        "frame": "क्या: पंक्ति ०५.०४.४८-५१ के द्रव्य · किससे युक्त: कल्क और सैन्धव · कर्म: पक्वाशय का शोधन।",
        "anchors": "रोध्र = लोध · कम्पिल्लक = कमीला · कल्क = लुगदी · सैन्धव = सेंधा नमक · पक्वाशय = पचे अन्न का स्थान · विशोधन = शुद्ध करने वाला।",
    },
    "28": {
        "chunks": "धातुकीपुष्पतक्रींर्जीवंतीमूलवत्सकाः (बिगड़ा) ‖ प्रग्रहः | खदिरी | कुष्ठं | शमीपिंडीतकायवाः।",
        "anchors": "धातकी = धाय · जीवन्ती = प्रायः डोडी · वत्सक = कुटज · कुष्ठ = कूट · शमी = प्रायः खेजड़ी · यव = यव के दाने।",
        "frame": "पंक्ति १: बिगड़ी (धाय के फूल, अस्पष्ट शब्द, जीवन्ती की जड़, वत्सक) · पंक्ति २: साफ़ सूची · नाम: पंक्ति ०५.०४.५६ में ‘संग्राहिक’।",
    },
    "29": {
        "diagram": {"groups": [{"label": "पंक्ति १", "items": ["प्रियङ्गु", "रक्तमूल (अनिश्चित)", "भैरणी", "जाति", "यूथिका"]},
                               {"label": "पंक्ति २", "items": ["वट आदि", "किंशुक", "रोध्र"]},
                               {"label": "इति", "items": ["संग्राहिक माने गए"]}]},
        "chunks": "प्रियंगुरक्तमूले च | भैरणीजातियूथिकाः ‖ वटाद्याः | किंशुकं | रोधमिति | संग्राहिका मताः।",
        "sandhi": "अ + आ → आ: वट + आद्याः → वटाद्याः; आः + घोष → आ: संग्राहिकाः + मताः → संग्राहिका मताः।",
        "anchors": "जाति = प्रायः चमेली · यूथिका = प्रायः जूही · वट = बरगद · किंशुक = ढाक · रोध्र = लोध · संग्राहिक = बाँधने वाला।",
    },
    "30": {
        "chain": {"steps": ["क्रम से", "ग्राही प्रियङ्गु, अम्बष्ठा आदि के क्वाथ और कल्क", "उषक आदि का प्रतीवाप", "लेखन त्रिफला-रस"]},
        "chunks": "ग्राहिप्रियंग्वंबष्ठादिकाथकल्कैः | क्रमेण च ‖ उषकादिप्रतीवापो | लेखनस्त्रिफलारसः।",
        "sandhi": "उ + अ → व: प्रियङ्गु + अम्बष्ठा → प्रियङ्ग्वम्बष्ठा; अः + त → अस्त: लेखनः + त्रिफला → लेखनस्त्रिफला।",
        "anchors": "ग्राही = बाँधने वाला · क्वाथ = काढ़ा · कल्क = लुगदी · प्रतीवाप = ऊपर से डाला द्रव्य · उषक = प्रायः खारी मिट्टी · लेखन = खुरचने वाला।",
    },
    "31": {
        "chunks": "मधुक कल्कैन (बिगड़ा) | सरसाज्येन | बृंहणः ‖ बदर्यैरावणीशैलूशाल्मलीधन्वनांकुराः।",
        "sandhi": "ई + ऐ → यै: बदरी + ऐरावणी → बदर्यैरावणी; अ + अ → आ: धन्वन + अङ्कुराः → धन्वनाङ्कुराः।",
        "anchors": "बृंहण = पुष्ट करने वाला · आज्य = घी · बदरी = बेर · शैलू = प्रायः लसोड़ा · शाल्मली = सेमल · धन्वन = प्रायः धामिन · अङ्कुर = अंकुर।",
        "pegs": "मेरा बनाया चित्र: पाँच पेड़ों की कतार, हर पेड़ पर एक नन्हा अंकुर: बेर, ऐरावणी, लसोड़ा, सेमल, धामिन।",
    },
    "32": {
        "diagram": {"groups": [{"label": "कर्ता", "items": ["पंक्ति ०५.०४.६० के अंकुर"]},
                               {"label": "किसके साथ", "items": ["माक्षिक (शहद)", "क्षीर (दूध)", "असृज् (रक्त)"]},
                               {"label": "माने गए", "items": ["पिच्छिल"]}]},
        "chunks": "समाक्षिकाः | क्षीरयुताः | सासृजाः | पिच्छिलाः स्मृताः ‖ कोलं | कतककांडेक्षुदर्भपाठेशुवालुभिः (अंत संदिग्ध)।",
        "sandhi": "अ + अ → आ: स + असृजाः → सासृजाः; ‘स-’ = सहित: समाक्षिकाः = शहद सहित।",
        "anchors": "माक्षिक = शहद · क्षीर = दूध · असृज् = रक्त · पिच्छिल = चिपचिपा · स्मृत = माना गया · कोल = बेर · दर्भ = कुश।",
    },
    "33": {
        "diagram": {"groups": [{"label": "दाहघ्न: पहला", "items": ["घी सहित", "दूध सहित"]},
                               {"label": "दूसरा", "items": ["उत्पल आदि के साथ"]},
                               {"label": "फिर", "items": ["सेमल-डंठलों की मुट्ठी", "दूध में पकी", "घी से युक्त"]}]},
        "chunks": "दाहघ्नः | सघृतक्षीरो | द्वितीयश्चोत्पलादिभिः ‖ मुष्टिं | शाल्मलिवृंतानां | क्षीरसिद्धो | घृतान्वितः।",
        "sandhi": "अः + च → अश्च, अ + उ → ओ: द्वितीयः + च + उत्पल → द्वितीयश्चोत्पल; अ + अ → आ: घृत + अन्वितः → घृतान्वितः।",
        "contrast": "पहला: घी और दूध सहित · दूसरा: उत्पल आदि के साथ; दोनों दाह नाशक।",
    },
    "34": {
        "chunks": "हितः प्रवाहणे | तद्वद्धृंतैः (छपा) | शाल्मलकस्य च ‖ कर्बुदाराढकींनपविदुलैः (छपा) | क्षीरसाधितैः।",
        "frame": "किसमें हितकर: प्रवाहण (जोर लगाना) · वैसे ही: शाल्मलक के डंठल · फिर: कर्बुदार, आढकी, नीप, विदुल दूध के साथ · किसके लिए: नहीं कहा।",
        "anchors": "हित = हितकर · प्रवाहण = जोर लगाना · वृन्त = डंठल · आढकी = अरहर · नीप = प्रायः कदम्ब · साधित = तैयार किया।",
    },
    "35": {
        "diagram": {"groups": [{"label": "परिकर्त में", "items": ["श्रीपर्णी के डंठल", "कोविदार के डंठल"]},
                               {"label": "परिस्रव में", "items": ["सिद्ध दूध", "द्रव्य: पंक्ति ०५.०४.६९"]}]},
        "chunks": "परिकर्त्ते | तथा वृंतैः | श्रीपर्णीकोविदारजैः ‖ परिस्रवे | पयः सिद्धं | सदृशविपुनर्नवं (अस्पष्ट)।",
        "contrast": "परिकर्त (काटने-सी पीड़ा) → डंठल · परिस्रव (बहाव) → पका दूध।",
        "anchors": "परिकर्त = काटने-सी पीड़ा · परिस्रव = बहना, स्राव · श्रीपर्णी = प्रायः गम्भारी · कोविदार = प्रायः कचनार · पयः = दूध · -ज = से उत्पन्न।",
    },
    "36": {
        "chunks": "आखुकर्णिकया | तद्वत् | तंदुलीयकयुक्तया ‖ अश्वावरोहकः | काकनासा | राजकसेरुकाः।",
        "anchors": "आखु = चूहा · कर्ण = कान · तण्डुलीयक = प्रायः चौलाई · काक = कौआ · नासा = नाक · कसेरुका = प्रायः कसेरु।",
        "puns": "केवल सुनने की सहायता: ‘आखु-कर्ण’ चूहे का कान, ‘काक-नासा’ कौए की नाक: दो जानवर, दो अंग।",
        "frame": "पंक्ति १ (तृतीया): आखुकर्णिका से, तण्डुलीयक से युक्त · पंक्ति २ (प्रथमा): तीन नाम, जो पंक्ति ०५.०४.७१ में ‘सिद्धाः’।",
    },
    "37": {
        "chain": {"steps": ["अतियोग में", "पंक्ति ०५.०४.७० के द्रव्य", "दूध में सिद्ध", "शहद, अञ्जन, घी से युक्त", "उसी विधि से दूसरा: न्यग्रोध आदि चार"]},
        "chunks": "सिद्धाः | क्षीरेऽतियोगे | स्युः | क्षौद्रांजनघृतैर्युताः ‖ न्यग्रोधाद्यैश्चतुर्भिइच (छपा) | तेनैव विधिनाऽपरः।",
        "sandhi": "ए + अ → एऽ: क्षीरे + अतियोगे → क्षीरेऽतियोगे; अ + ए → ऐ: तेन + एव → तेनैव; ऐः + य → ऐर्य: घृतैः + युताः → घृतैर्युताः।",
        "anchors": "अतियोग = अधिकता · क्षौद्र = शहद · अञ्जन = अञ्जन द्रव्य (कौन-सा, अकथित) · न्यग्रोध = बरगद · अपर = दूसरा।",
    },
}


IMAGE_SPECS = {
    ("26", "diagram"): {
        "file": "ka4-trivrit-26.svg",
        "alt": ("Two columns for verse 26: line 1 the root of shyama and trivrit, and the item born of danti and dravanti; "
                "line 2 prakirya, udakirya, kshirini, nilini and fruit"),
        "type": "split",
        "title": "श्लोक २६: सूची आगे",
        "cols": [["पंक्ति १", ["श्यामा-त्रिवृत् का मूल", "दन्ती-द्रवन्ती से उत्पन्न"]],
                 ["पंक्ति २", ["प्रकीर्या", "उदकीर्या", "क्षीरिणी", "नीलिनी", "फल"]]],
    },
    ("27", "diagram"): {
        "file": "ka4-pakvashaya-27.svg",
        "alt": ("Flowchart of verse 27: the last drugs of the list (samala, shankhini, rodhra printed rodham, kampillaka fruit) "
                "are joined with paste and rock salt and become cleansers of the pakvashaya"),
        "type": "mermaid",
        "code": ('flowchart TD\n'
                 '  A["समला · शङ्खिनी"] --> D["कल्क और सैन्धव से युक्त"]\n'
                 '  B["रोध्र (छपा रोधं)"] --> D\n'
                 '  C["कम्पिल्लक का फल"] --> D\n'
                 '  D --> E["पक्वाशय-शोधक"]\n'),
    },
    ("29", "diagram"): {
        "file": "ka4-samgrahika-29.svg",
        "alt": ("Two columns for verse 29: line 1 priyangu, red root (uncertain), bhairani, jati, yuthika; line 2 vata and the rest, "
                "kimshuka, rodhra; all considered samgrahika (binding)"),
        "type": "split",
        "title": "श्लोक २९: इति संग्राहिकाः",
        "cols": [["पंक्ति १", ["प्रियङ्गु", "रक्तमूल (अनिश्चित)", "भैरणी", "जाति", "यूथिका"]],
                 ["पंक्ति २", ["वट आदि", "किंशुक", "रोध्र", "= संग्राहिक"]]],
    },
    ("30", "chain"): {
        "file": "ka4-lekhana-30.svg",
        "alt": ("Chain of four steps for verse 30: in sequence; decoctions and pastes of binding priyangu, ambashtha and the rest; "
                "the additive of ushaka and the rest; the scraping triphala juice"),
        "type": "chain",
        "title": "श्लोक ३०: क्रम से",
        "steps": ["क्रम से", "ग्राही प्रियङ्गु-अम्बष्ठा आदि: क्वाथ, कल्क", "उषक आदि का प्रतीवाप", "लेखन त्रिफला-रस"],
    },
    ("32", "diagram"): {
        "file": "ka4-picchila-32.svg",
        "alt": ("Flowchart of verse 32: the sprouts of line 05.04.60, with honey, joined with milk and with blood, "
                "are held to be picchila (slimy)"),
        "type": "mermaid",
        "code": ('flowchart TD\n'
                 '  A["अंकुर (पंक्ति ०५.०४.६०)"] --> B["शहद सहित"]\n'
                 '  A --> C["दूध से युक्त"]\n'
                 '  A --> D["रक्त सहित"]\n'
                 '  B --> E["पिच्छिल माने गए"]\n'
                 '  C --> E\n'
                 '  D --> E\n'),
    },
    ("33", "diagram"): {
        "file": "ka4-dahaghna-33.svg",
        "alt": ("Table for verse 33 with three rows: the first burning-destroying kind with ghee and milk; the second with utpala and the rest; "
                "a fistful of shalmali stalks cooked in milk, with ghee"),
        "type": "table",
        "title": "श्लोक ३३: दाह में",
        "heads": ["क्या", "किसके साथ"],
        "rows": [["दाहघ्न: पहला", "घी और दूध"], ["दूसरा", "उत्पल आदि"], ["सेमल-डंठलों की मुट्ठी", "दूध में पकी, घी से युक्त"]],
    },
    ("35", "diagram"): {
        "file": "ka4-parikarta-35.svg",
        "alt": ("Table for verse 35 with two rows: parikarta (cutting pain) takes stalks of shriparni and kovidara; "
                "parisrava (flowing out) takes cooked milk, its drugs following in line 05.04.69"),
        "type": "table",
        "title": "श्लोक ३५: स्थिति और उपाय",
        "heads": ["स्थिति", "उपाय"],
        "rows": [["परिकर्त (काटने-सी पीड़ा)", "श्रीपर्णी, कोविदार के डंठल"], ["परिस्रव (बहाव)", "सिद्ध दूध (द्रव्य आगे)"]],
    },
    ("37", "chain"): {
        "file": "ka4-atiyoga-37.svg",
        "alt": ("Chain of five steps for verse 37: in atiyoga; the drugs of line 05.04.70; cooked in milk; joined with honey, anjana and ghee; "
                "by the same method another, with the four beginning with nyagrodha"),
        "type": "chain",
        "title": "श्लोक ३७: अतियोग में",
        "steps": ["अतियोग में", "पंक्ति ०५.०४.७० के द्रव्य", "दूध में सिद्ध", "शहद, अञ्जन, घी से युक्त", "उसी विधि से दूसरा: न्यग्रोध आदि चार"],
    },
}
