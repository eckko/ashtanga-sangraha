from helpers import mcq, match, order, fill, multi, accepts


AUTHORED = {}

# ---------------------------------------------------------------- unit 55
AUTHORED["55"] = {
    "title": "पित्ते मधुकविदारीनिर्यूहसिद्धं पयः",
    "question": "By unit 55, what should be drunk in Pitta?",
    "rule": ("In Pitta (पित्ते), one should drink milk (पयः) cooked (सिद्ध) with a decoction (निर्यूह) of madhuka "
             "(probably licorice) and vidārī (probably Indian kudzu)."),
    "limits": ("Prose. madhuka = licorice is probable only (it can also mean mahua); vidārī = Indian kudzu is probable. "
               "No amount, time or drinker is named. No question rests on the form of the printed verb पिबेत."),
    "explain_hi": ("यह गद्य-पंक्ति पित्त की अवस्था का उपाय बताती है: मधुक और विदारी के निर्यूह, यानी काढ़े, से पकाया हुआ दूध पिए। "
                   "मधुक की पहचान मुलेठी सम्भावित है; यह शब्द महुआ वृक्ष के लिए भी आता है। "
                   "विदारी सम्भवतः विदारीकन्द है। "
                   "‘निर्यूहसिद्धं पयः’ का अर्थ है काढ़े के साथ सिद्ध किया हुआ दूध; पीया दूध जाता है, केवल काढ़ा नहीं। "
                   "मात्रा, समय और कितने दिन, यह नहीं कहा गया।"),
    "hook": "पित्त में: मधुक-विदारी के काढ़े में पका दूध।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 55, what should one drink in Pitta?",
            ("Milk cooked with a madhuka-vidārī decoction", "पित्ते मधुकविदारीनिर्यूहसिद्धं पयः पिबेत."),
            [("Clear surā with meat as its relish, three nights", "That is the Kapha remedy of unit 62."),
             ("Grape wine (mārdvīka) with meat as relish", "Mārdvīka comes in unit 70, not in the Pitta line."),
             ("Cold water after a milk enema with rock salt", "The milk enema with rock salt is for Vāta in unit 52; "
                                                               "no water is drunk there.")],
            "In Pitta the drink is milk cooked with a decoction of madhuka and vidārī.",
            "पित्ते ... निर्यूहसिद्धं पयः पिबेत."),
        order(1, "Put these parts of unit 55 in the line's order.",
              ["पित्ते", "मधुक", "विदारी", "निर्यूहसिद्धम्", "पयः पिबेत"],
              "In Pitta, madhuka, vidārī, cooked with the decoction, milk one should drink.",
              "पित्ते → मधुक → विदारी → निर्यूहसिद्धम् → पयः पिबेत."),
        match(2, "Match each word of unit 55 to its meaning.",
              [["पित्ते", "in Pitta"], ["मधुक", "probably licorice"], ["विदारी", "probably Indian kudzu"],
               ["निर्यूह", "decoction"], ["सिद्ध", "cooked"]],
              "Two plants, their decoction, and the milk cooked with it.",
              "पित्ते, मधुक, विदारी, निर्यूह, सिद्ध.", role="extend",
              teaches="-सिद्ध at the end of a compound = cooked with: निर्यूहसिद्धं पयः = milk cooked with a decoction."),
        mcq("discriminate", 3, "Why does पयः keep its visarga before पिबेत in unit 55?",
            ("प is an unvoiced sound", "अः becomes ओ only before a voiced sound; before the unvoiced प the visarga stays."),
            [("A visarga stays before every consonant", "Before a voiced consonant अः becomes ओ."),
             ("पयः is the last member of a compound", "पयः is a separate noun, n. acc. sg."),
             ("The verb पिबेत begins with a vowel", "पिबेत begins with the consonant प.")],
            "पयः + पिबेत = पयः पिबेत: प is unvoiced, so the visarga stays.",
            "अः + voiced sound → ओ; before an unvoiced consonant the visarga stays."),
        mcq("apply", 4, "A learner writes: in Pitta, drink a decoction of madhuka and vidārī. What does unit 55 add?",
            ("Milk is cooked with it, and the milk is drunk", "निर्यूहसिद्धं पयः: milk cooked with the decoction is drunk."),
            [("Ghee is cooked with it, and the ghee is eaten", "No ghee is named in unit 55."),
             ("Rock salt is added to it before it is drunk", "Rock salt (saindhava) is in the Vāta enema of unit 52."),
             ("Goat ghee is mixed in before it is given", "Goat ghee is in the gruel of unit 57.")],
            "The decoction is not drunk by itself: milk is cooked with it, and that milk is drunk.",
            "निर्यूहसिद्धं पयः = milk cooked with the decoction."),
        mcq("transfer", 5, "By the rule of सिद्धम् + पयः → सिद्धं पयः, how is फलम् + खादति (he eats a fruit) written in a sentence?",
            ("फलं खादति", "A word-final म् before a consonant becomes anusvāra, as सिद्धम् + पयः → सिद्धं पयः."),
            [("फलो खादति", "ओ comes from अः before a voiced sound, not from म्."),
             ("फलः खादति", "म् does not turn into a visarga."),
             ("फलमा खादति", "No vowel is added after म्.")],
            "फलम् + खादति = फलं खादति, like सिद्धम् + पयः = सिद्धं पयः.",
            "Word-final म् + consonant → anusvāra.",
            teaches="A word-final म् before a consonant is written as anusvāra: सिद्धम् + पयः → सिद्धं पयः."),
    ],
}

# ---------------------------------------------------------------- unit 56
AUTHORED["56"] = {
    "title": "तिस्रः स्थूलकुक्कुटीर्निस्तुषमाषाढकं च",
    "question": "By unit 56, what preparation is given for upaviṣṭaka and upaśuṣkaka?",
    "rule": ("Crush three large hens and an āḍhaka of husked māṣa (black gram, standard) with milk and water in a mortar; "
             "with that juice and ghee cook the broth of tittiri (probably partridge) or kapiñjala (disputed); she drinks it "
             "for upaviṣṭaka and upaśuṣkaka."),
    "limits": ("Prose. The grammar is loose: the crushed mass may be cooked with the bird broth too. kukkuṭī = hen as the "
               "data reads it. The āḍhaka's size is not given. tittiri probable, kapiñjala disputed. Printed संक्षुध्य, "
               "अन्यातर, वृद्व्य are corrected; no question tests them."),
    "explain_hi": ("यह लम्बा गद्य-वाक्य उपविष्टक और उपशुष्कक, दोनों की वृद्धि के लिए एक योग देता है। "
                   "तीन मोटी कुक्कुटियाँ (मुर्गियाँ, डेटा के अनुसार) और आढक भर छिलका-रहित माष (उड़द, मानक) दूध और जल के साथ "
                   "ओखली में कूटे जाते हैं। "
                   "उस रस और घी के साथ तित्तिरि (सम्भवतः तीतर) या कपिञ्जल (पहचान विवादित) में से किसी एक का रस पकाकर पिलाया जाता है। "
                   "वाक्य का बीच का भाग ढीला है: कुटा हुआ द्रव्य भी साथ पकता हो, यह सम्भव है। "
                   "आढक एक माप है, पर उसका परिमाण यहाँ नहीं दिया गया। "
                   "उपविष्टक और उपशुष्कक गर्भ की वे अवस्थाएँ हैं जिनके कारण और लक्षण इकाई 45 से आगे बताए गए हैं।"),
    "hook": "तीन मुर्गियाँ, आढक उड़द, ओखली में कूटो; उस रस और घी से पक्षी का रस।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 56, for which conditions is the preparation given?",
            ("Upaviṣṭaka and upaśuṣkaka", "उपविष्टकविवर्द्धनार्थम् उपशुष्ककवृद्ध्यर्थं च."),
            [("Udāvarta and constipation", "Those are treated in unit 74."),
             ("A placenta that does not fall", "Placenta-expelling drugs come in unit 66."),
             ("Bleeding before the third month", "That is the topic of units 28 to 37.")],
            "The drink is for the growth in upaviṣṭaka and upaśuṣkaka.",
            "... पाययेदुपविष्टकविवर्द्धनार्थमुपशुष्ककवृद्ध्यर्थं च."),
        order(1, "Put these parts of unit 56 in the line's order.",
              ["तिस्रः स्थूलकुक्कुटीः", "निस्तुषमाषाढकं च", "क्षीरोदकेनोदूखले", "तद्रसेन सर्पिषा च",
               "साधयित्वा पाययेत्", "उपविष्टकविवर्द्धनार्थम्"],
              "Three large hens, an āḍhaka of husked black gram, with milk and water in a mortar, with that juice and "
              "ghee, having prepared, make her drink, for the increase of upaviṣṭaka.",
              "तिस्रः स्थूलकुक्कुटीः → निस्तुषमाषाढकं च → क्षीरोदकेनोदूखले → तद्रसेन सर्पिषा च → साधयित्वा पाययेत् → "
              "उपविष्टकविवर्द्धनार्थम्."),
        match(2, "Match each word of unit 56 to its meaning.",
              [["स्थूलकुक्कुटी", "large hen"], ["निस्तुष", "husked, without husk"], ["माष", "black gram (standard)"],
               ["आढक", "a measure (size not given)"], ["उदूखल", "mortar"]],
              "The things crushed, the measure, and the vessel they are crushed in.",
              "स्थूलकुक्कुटी, निस्तुष, माष, आढक, उदूखल.", role="extend",
              teaches="निस्- = without: निस्तुष = without husk (तुष); निस्तुषमाष = husked black gram."),
        mcq("discriminate", 3, "Which split of क्षीरोदकेनोदूखले is right?",
            ("क्षीरोदकेन + उदूखले", "अ + उ → ओ: क्षीरोदकेन + उदूखले → क्षीरोदकेनोदूखले."),
            [("क्षीरोदकेनः + उदूखले", "अः before उ loses the visarga and leaves a gap; it does not give ओ."),
             ("क्षीरोदके + नोदूखले", "नोदूखले is not a word; the word is उदूखले, in a mortar."),
             ("क्षीरोदकेनो + दूखले", "दूखले is not a word.")],
            "क्षीरोदकेन (with milk and water) + उदूखले (in a mortar): अ + उ → ओ.",
            "अ + उ → ओ."),
        multi("apply", 4, "Which statements does unit 56 make?",
              [("Three large hens are named", "Right: तिस्रः स्थूलकुक्कुटीः."),
               ("The size of the āḍhaka is given", "The note: its size is not given here."),
               ("Milk and water are used in the crushing", "Right: क्षीरोदकेनोदूखले संक्षुध्य, crushed in a mortar "
                                                            "with milk and water."),
               ("Kapiñjala is identified with certainty", "Its identity is disputed in the data.")],
              [0, 2],
              "Three hens and black gram are crushed with milk and water; the āḍhaka's size and kapiñjala's identity are open.",
              "तिस्रः स्थूलकुक्कुटीः ... क्षीरोदकेनोदूखले."),
        mcq("transfer", 5, "By the rule of तत् + रसेन → तद्रसेन, how is तत् + वचनम् (that word) joined?",
            ("तद्वचनम्", "त् before a voiced sound becomes द्, as तत् + रसेन → तद्रसेन."),
            [("तत्वचनम्", "त् does not stay unvoiced before the voiced व."),
             ("तच्वचनम्", "त् becomes च् before च or छ (च्छ with श), not before व."),
             ("तन्वचनम्", "त् may become न् only before a nasal such as न or म, not before व.")],
            "तत् + वचनम् = तद्वचनम्, like तत् + रसेन = तद्रसेन.",
            "त् + voiced sound → द्.",
            teaches="A word-final त् before a voiced sound becomes द्: तत् + रसेन → तद्रसेन."),
    ],
}

# ---------------------------------------------------------------- unit 57
AUTHORED["57"] = {
    "title": "अजासर्पिषा क्षीरेण ... यवागूं पिबेत",
    "question": "By unit 57, what gruel is drunk, and with what is it prepared?",
    "rule": ("One should drink a yavāgū (thick gruel) prepared (संस्कृता) with goat ghee (अजासर्पिस्), with milk "
             "(क्षीर), and with the jīvanīya (life-promoting) drugs."),
    "limits": ("Prose. jīvanīya rests on joining the printed जीवनी यैश्च into जीवनीयैश्च (a possible reading); no question "
               "rests on it. The jīvanīya drugs are not listed here. No amount is given. GROUPING: it seems to continue the "
               "remedies of unit 56; the condition is not restated."),
    "explain_hi": ("इस गद्य-पंक्ति में यवागू, यानी गाढ़ी लपसी, पीने को कहा गया है। "
                   "वह बकरी के घी (अजासर्पिस्), दूध और जीवनीय, यानी जीवन देने वाले द्रव्यों से तैयार (संस्कृत) हो। "
                   "जीवनीय द्रव्यों की सूची यहाँ नहीं दी गई। "
                   "छपाई में ‘जीवनी यैश्च’ अलग छपा है; डेटा इसे जोड़कर जीवनीयैश्च पढ़ता है, जो सम्भावित पाठ है। "
                   "‘संस्कृतां’ स्त्रीलिंग है क्योंकि यवागू स्त्रीलिंग शब्द है।"),
    "hook": "बकरी का घी, दूध, जीवनीय: उनसे बनी यवागू पिओ।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 57, what should one drink?",
            ("A thick gruel", "यवागूं पिबेत: one should drink a yavāgū."),
            [("Clear surā with meat", "Surā with a meat relish is the Kapha drink of unit 62."),
             ("A broth of black gram", "A black-gram soup (yūṣa) is in unit 68, with rice."),
             ("Cold water after food", "No cold water is named in unit 57.")],
            "The drink of unit 57 is a yavāgū, a thick gruel.",
            "संस्कृतां यवागूं पिबेत."),
        order(1, "Put these words of unit 57 in the line's order (the jīvanīya word is left out).",
              ["अजासर्पिषा", "क्षीरेण", "संस्कृताम्", "यवागूम्", "पिबेत"],
              "With goat ghee, with milk, prepared, the gruel, one should drink.",
              "अजासर्पिषा → क्षीरेण → संस्कृताम् → यवागूम् → पिबेत."),
        match(2, "Match each word of unit 57 to its meaning.",
              [["अजा", "she-goat"], ["सर्पिस्", "ghee"], ["क्षीर", "milk"], ["संस्कृत", "prepared, processed"],
               ["यवागू", "thick gruel"]],
              "Goat ghee and milk prepare the gruel that is drunk.",
              "अजा, सर्पिस्, क्षीर, संस्कृत, यवागू.", role="extend",
              teaches="अजासर्पिस् = ghee of the she-goat: the first member names whose ghee it is."),
        mcq("discriminate", 3, "Which case is सर्पिषा in अजासर्पिषा?",
            ("Instrumental singular: with ghee", "The data: n. inst. sg., with goat ghee."),
            [("Nominative singular: the ghee itself", "The nominative is सर्पिः."),
             ("Genitive singular: of the ghee", "The genitive is सर्पिषः."),
             ("Locative singular: in the ghee", "The locative is सर्पिषि.")],
            "अजासर्पिषा = with goat ghee, instrumental, like क्षीरेण (with milk).",
            "सर्पिस्: nom. सर्पिः, inst. सर्पिषा, loc. सर्पिषि."),
        mcq("apply", 4, "Why is संस्कृतां feminine accusative in unit 57?",
            ("It agrees with यवागूम्", "यवागू is feminine; संस्कृताम् describes it, f. acc. sg."),
            [("It agrees with अजा (goat)", "अजा is inside the instrumental compound अजासर्पिषा, not accusative."),
             ("It agrees with क्षीरेण", "क्षीरेण is neuter instrumental."),
             ("It is an adverb of manner", "The data labels it a participle, f. acc. sg.")],
            "संस्कृतां यवागूम्: the participle takes the gender and case of the gruel.",
            "Adjective = gender, case and number of its noun."),
        mcq("transfer", 5, "Built like संस्कृतां यवागूम्, which form fits ____ यवागूम् (cold gruel), शीत meaning cold?",
            ("शीताम्", "f. acc. sg., to agree with यवागूम्, as संस्कृताम् does."),
            [("शीतम्", "शीतम् is masculine or neuter; यवागू is feminine."),
             ("शीतेन", "शीतेन is instrumental, not accusative."),
             ("शीता", "शीता is nominative, not accusative.")],
            "शीतां यवागूम् = cold gruel, like संस्कृतां यवागूम्.",
            "Adjective = gender, case and number of its noun.",
            teaches="An adjective takes the gender, case and number of its noun: संस्कृताम् यवागूम् (f. acc. sg.)."),
    ],
}

# ---------------------------------------------------------------- unit 58
AUTHORED["58"] = {
    "title": "पयस्या काकोलीद्वयसुनिषण्णककल्केन",
    "question": "By unit 58, with what paste and liquid is ghee cooked?",
    "rule": ("Cook ghee (सर्पिः) with milk (पयसा) and with a paste (कल्क) of payasyā (identity disputed), the pair of "
             "kākolī (disputed) and suniṣaṇṇaka (probably Marsilea)."),
    "limits": ("Prose. payasyā and kākolī are disputed; suniṣaṇṇaka = Marsilea is probable. The two members of the kākolī "
               "pair are not named in this line. No amounts. GROUPING: it seems to continue unit 57; what the ghee is for "
               "is not restated here."),
    "explain_hi": ("इस गद्य-पंक्ति में घी (सर्पिः) पकाने का योग है: दूध के साथ और तीन नामों (काकोली-जोड़ा एक नाम) की लुगदी (कल्क) के साथ। "
                   "पयस्या की पहचान विवादित है; क्षीरविदारी या विदारीकन्द उसके सम्भावित उम्मीदवार हैं। "
                   "काकोलीद्वय यानी काकोली का जोड़ा, जिसकी पहचान भी विवादित है; जोड़े के दो नाम यहाँ नहीं दिए गए। "
                   "सुनिषण्णक सम्भवतः चौपतिया है। "
                   "‘सर्पिर्विपचेत्’ में सर्पिः का विसर्ग इ के बाद घोष व से पहले र् बना है।"),
    "hook": "पयस्या, दो काकोली, सुनिषण्णक की लुगदी + दूध: घी पकाओ।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 58, what is cooked with the paste and the milk?",
            ("Ghee (सर्पिः)", "सर्पिर्विपचेत्: one should cook ghee."),
            [("Oil (तैल)", "Oil is cooked in unit 75, not here."),
             ("Gruel (यवागू)", "The gruel is unit 57."),
             ("Rice (ओदन)", "Rice is fed in unit 68.")],
            "Ghee is cooked with the paste and with milk.",
            "... कल्केन पयसा च सर्पिर्विपचेत्."),
        order(1, "Put these words of unit 58 in the line's order.",
              ["पयस्या", "काकोलीद्वय", "सुनिषण्णक", "कल्केन", "पयसा च", "सर्पिर्विपचेत्"],
              "Payasyā, the pair of kākolī, suniṣaṇṇaka, with a paste, and with milk, ghee one should cook.",
              "पयस्या → काकोलीद्वय → सुनिषण्णक → कल्केन → पयसा च → सर्पिर्विपचेत्."),
        match(2, "Match each word of unit 58 to its meaning.",
              [["पयस्या", "a plant, identity disputed"], ["काकोलीद्वय", "the pair of kākolī"],
               ["सुनिषण्णक", "probably Marsilea"], ["कल्क", "paste"], ["विपचेत्", "should cook"]],
              "Three names (the kākolī pair as one) made into a paste; ghee is cooked with it.",
              "पयस्या, काकोलीद्वय, सुनिषण्णक, कल्क, विपचेत्.", role="extend",
              teaches="द्वय = pair: काकोलीद्वय = the pair of kākolī; कल्क = paste."),
        mcq("discriminate", 3, "Why is सर्पिः printed सर्पिर् before विपचेत्?",
            ("After इ, ः before voiced व → र्", "A visarga after a vowel other than अ/आ becomes र् before a voiced sound."),
            [("Visarga becomes र् before every consonant", "Before an unvoiced consonant, as in पयः पिबेत (unit 55), it does not."),
             ("After अ, visarga before व becomes र्", "After अ it becomes ओ before a voiced sound."),
             ("र् is the accusative ending of सर्पिस्", "The accusative is सर्पिः; र् comes from sandhi.")],
            "सर्पिः + विपचेत् = सर्पिर्विपचेत्: इ + ः before the voiced व → इर्.",
            "Visarga after a vowel other than अ/आ, before a voiced sound → र्."),
        mcq("apply", 4, "Which plant of unit 58 carries the label probable, not disputed?",
            ("Suniṣaṇṇaka", "The data: Marsilea minuta or M. quadrifolia, probable."),
            [("Payasyā", "Disputed: candidates include Ipomoea digitata and Pueraria tuberosa."),
             ("Kākolī", "Disputed: candidates include Roscoea purpurea and Fritillaria roylei."),
             ("None; all three are standard", "None of the three is standard here.")],
            "Only suniṣaṇṇaka is probable; payasyā and kākolī are disputed.",
            "payasyā disputed, kākolī disputed, suniṣaṇṇaka probable."),
        mcq("transfer", 5, "By the rule of सर्पिर्विपचेत्, how is हविः + ददाति (gives the oblation) joined?",
            ("हविर्ददाति", "After इ, a visarga before the voiced द becomes र्."),
            [("हविः ददाति", "Before a voiced sound the visarga after इ does not stay."),
             ("हवि ददाति", "After इ, a visarga before a voiced sound becomes र्; it is not dropped."),
             ("हविद्ददाति", "A visarga does not become द्.")],
            "हविः + ददाति = हविर्ददाति, like सर्पिः + विपचेत् = सर्पिर्विपचेत्.",
            "इः + voiced sound → इर्.",
            teaches="A visarga after इ becomes र् before a voiced sound: सर्पिः + विपचेत् → सर्पिर्विपचेत्."),
    ],
}

# ---------------------------------------------------------------- unit 59
AUTHORED["59"] = {
    "title": "तेन क्षीरानुपानमुपयुंजीत",
    "question": "By unit 59, how should that be taken?",
    "rule": ("With that (तेन), one should take (it) (उपयुञ्जीत), with milk (क्षीर) as the after-drink (अनुपान): a liquid "
             "taken after the dose."),
    "limits": ("Prose. The object of उपयुञ्जीत is not stated; the data takes तेन as the ghee of unit 58 (GROUPING), which "
               "the line itself does not say. No amount, time or number of days."),
    "explain_hi": ("यह छोटी गद्य-पंक्ति कहती है: उससे, दूध को अनुपान बनाकर, उपयोग करे। "
                   "अनुपान वह द्रव है जो औषध के बाद लिया जाता है। "
                   "डेटा ‘तेन’ को पिछली इकाई (58) का घी मानता है; पंक्ति स्वयं यह नहीं कहती, और क्या लिया जाए, यह भी नहीं लिखा। "
                   "‘क्षीरानुपानम्’ में क्षीर + अनुपानम् है (अ + अ → आ)।"),
    "hook": "उसे लो, ऊपर से दूध।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 59, what is taken as the after-drink?",
            ("Milk (क्षीर)", "क्षीरानुपानम्: milk as the after-drink."),
            [("Clear surā (सुरा)", "Surā is the Kapha drink of unit 62, not an after-drink here."),
             ("Hot water (उष्णोदक)", "No hot water is named in unit 59."),
             ("Meat broth (मांसरस)", "No meat broth is named in unit 59.")],
            "Milk is the after-drink.",
            "तेन क्षीरानुपानमुपयुञ्जीत."),
        match(1, "Match each word of unit 59 to its meaning.",
              [["तेन", "with that"], ["क्षीर", "milk"], ["अनुपान", "after-drink"], ["उपयुञ्जीत", "should take, should use"]],
              "With that, milk as the after-drink, one should take.",
              "तेन, क्षीर, अनुपान, उपयुञ्जीत."),
        fill(2, "A liquid taken after a dose is called ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("अनुपान", None, "अनुपानम्", "anupana", "anupanam"),
             "अनुपान = after-drink; in unit 59 it is milk: क्षीरानुपानम्.",
             "अनुपान = a liquid taken after the dose: क्षीरानुपान = with milk as the after-drink.",
             "क्षीर + अनुपान = क्षीरानुपान."),
        mcq("discriminate", 3, "Which split of क्षीरानुपानम् is right?",
            ("क्षीर + अनुपानम्", "अ + अ → आ: क्षीर + अनुपानम् → क्षीरानुपानम्."),
            [("क्षीरम् + अनुपानम्", "म् before a vowel stays: it would be क्षीरमनुपानम्."),
             ("क्षीरः + अनुपानम्", "अः + अ gives ओऽ: क्षीरोऽनुपानम्."),
             ("क्षीरा + नुपानम्", "नुपानम् is not a word; the word is अनुपान.")],
            "क्षीर (milk) + अनुपानम् (after-drink): अ + अ → आ.",
            "अ + अ → आ."),
        multi("apply", 4, "Which statements about unit 59 are right?",
              [("A dose and a time of day are given", "No amount or time is given."),
               ("The object of उपयुञ्जीत is not stated", "Right: the data notes that the object is not stated."),
               ("It is a metrical verse line", "It is a prose unit."),
               ("Milk is taken after the dose", "Right: क्षीरानुपानम्, milk as the after-drink.")],
              [1, 3],
              "Milk is the after-drink; what is taken, how much and when are not stated.",
              "तेन क्षीरानुपानमुपयुञ्जीत."),
        mcq("transfer", 5, "By the rule of क्षीर + अनुपान → क्षीरानुपान, how is शीत + अम्बु (cold water) joined?",
            ("शीताम्बु", "अ + अ → आ, as क्षीर + अनुपान → क्षीरानुपान."),
            [("शीतम्बु", "The two अ do not shrink to one short अ."),
             ("शीतोम्बु", "ओ comes from अ + उ, not from अ + अ."),
             ("शीतेम्बु", "ए comes from अ + इ, not from अ + अ.")],
            "शीत + अम्बु = शीताम्बु, like क्षीर + अनुपान = क्षीरानुपान.",
            "अ + अ → आ.",
            teaches="A short अ followed by a short अ joins as आ: क्षीर + अनुपान → क्षीरानुपान."),
    ],
}

# ---------------------------------------------------------------- unit 60
AUTHORED["60"] = {
    "title": "आमगर्भरासेन वाऽश्नीयात्",
    "question": "By unit 60, what further option is given?",
    "rule": ("Or (वा) one should eat (अश्नीयात्) with the rasa (broth) of āmagarbha, literally raw fetus; its exact sense "
             "is uncertain. अश्नीयात् is optative: should eat."),
    "limits": ("Prose. The exact sense of āmagarbha is uncertain (raw embryos of animals, or eggs, are possible; not stated); "
               "no question rests on it. Printed रासेन is read रसेन (near certain). The food that is eaten is not stated. "
               "GROUPING: a further remedy after units 57 to 59."),
    "explain_hi": ("यह गद्य-पंक्ति एक और विकल्प देती है: या आमगर्भ के रस के साथ खाए। "
                   "आमगर्भ का शाब्दिक अर्थ कच्चा गर्भ है; ठीक अर्थ अनिश्चित है (पशुओं के कच्चे भ्रूण या अण्डे हो सकते हैं, कहा नहीं गया)। "
                   "क्या खाया जाए, यह भी नहीं लिखा। "
                   "छपा ‘रासेन’ यहाँ कोई शब्द नहीं; ‘रसेन’ लगभग निश्चित पाठ है। "
                   "‘वाऽश्नीयात्’ = वा + अश्नीयात्; छपाई ने लुप्त अ को ऽ से दिखाया है।"),
    "hook": "या: आमगर्भ के रस के साथ खाओ।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 60, whose rasa is named?",
            ("आमगर्भ (sense uncertain)", "आमगर्भरासेन, read आमगर्भरसेन: with the rasa of āmagarbha."),
            [("तित्तिरि (probably partridge)", "Partridge broth is in units 56 and 68, not here."),
             ("मधुक (probably licorice)", "Madhuka is in the decoction of unit 55."),
             ("बदर (jujube, standard)", "Badara powder is unit 65.")],
            "The rasa is that of āmagarbha, whose exact sense is uncertain.",
            "आमगर्भरसेन वा अश्नीयात्."),
        order(1, "Put the words of unit 60 in the line's order.",
              ["आमगर्भ", "रासेन (read रसेन)", "वा", "अश्नीयात्"],
              "Āmagarbha, with the rasa, or, one should eat.",
              "आमगर्भ → रासेन (read रसेन) → वा → अश्नीयात्."),
        match(2, "Match each word of unit 60 to its meaning.",
              [["आम", "raw, unripe"], ["गर्भ", "fetus, embryo"], ["रस", "broth, juice"], ["वा", "or"],
               ["अश्नीयात्", "should eat"]],
              "Or, with the broth of the raw fetus, one should eat.",
              "आम, गर्भ, रस, वा, अश्नीयात्.", role="extend",
              teaches="आमगर्भ = literally raw fetus; its exact sense here is uncertain."),
        mcq("discriminate", 3, "Which split of वाऽश्नीयात् is right?",
            ("वा + अश्नीयात्", "आ + अ → आ; the print marks the lost अ with ऽ."),
            [("वे + अश्नीयात्", "ए + अ would keep the ए: वेऽश्नीयात्."),
             ("वा + इश्नीयात्", "आ + इ would give ए, and इश्नीयात् is not a word."),
             ("वाः + श्नीयात्", "श्नीयात् is not a word; the verb is अश्नीयात्.")],
            "वा (or) + अश्नीयात् (should eat).",
            "आ + अ → आ."),
        multi("apply", 4, "Which statements about unit 60 are right?",
              [("The unit names the food that is eaten", "The food is not stated."),
               ("It defines āmagarbha as eggs", "Eggs are only one possibility; the line does not say."),
               ("The exact sense of āmagarbha is uncertain", "Right: the data leaves it open."),
               ("वा marks this as another option", "Right: वा = or.")],
              [2, 3],
              "Another option, with the broth of āmagarbha; its sense and the food are not stated.",
              "आमगर्भरसेन वा अश्नीयात्."),
        mcq("transfer", 5, "अश्नीयात् is optative: one should eat. Which of these forms means one should give?",
            ("दद्यात्", "Optative of √दा, should give; like अश्नीयात् it ends in -यात्."),
            [("ददाति", "Present: he gives."),
             ("दत्त्वा", "Absolutive: having given."),
             ("ददातु", "Imperative: let him give.")],
            "दद्यात् = one should give, an optative like अश्नीयात्.",
            "Optative = should: अश्नीयात्, दद्यात्, पिबेत्.",
            teaches="The optative (should) has more than one shape: अश्नीयात्, दद्यात् end in -यात्; पिबेत्, विपचेत् end in -एत्."),
    ],
}

# ---------------------------------------------------------------- unit 61
AUTHORED["61"] = {
    "title": "तानेव च तत्र",
    "question": "By unit 61, what can be read with certainty in this damaged line?",
    "rule": ("And those very (ones) (तान् एव) there (तत्र); then, in a damaged compound, the line names vulture (गृध्र, "
             "on a conjectural reading) and the flesh of water-movers (जलचरमांसानि)."),
    "limits": ("Low confidence. The compound after गृध्र- is damaged, अभ्यें unclear, vulture conjectural: no question rests "
               "on them. तान् एव has no clear antecedent here. What is done with these is not stated. GROUPING: it seems "
               "to continue units 57 to 60."),
    "explain_hi": ("यह पंक्ति छपाई में क्षतिग्रस्त है, इसलिए इसका केवल स्पष्ट भाग पढ़ा जाता है। "
                   "‘तानेव च तत्र’: और वहाँ उन्हीं को; ‘तान्’ किसकी ओर संकेत करता है, यह इस इकाई में स्पष्ट नहीं। "
                   "आगे ‘गृध्र-’ (गिद्ध, अनुमानित पाठ), एक अस्पष्ट शब्द ‘अभ्यें’, और ‘जलचरमांसानि’ यानी जल में चलने वाले जीवों के मांस। "
                   "जलचर जल-जीवों का सामान्य शब्द है। "
                   "इन मांसों का क्या किया जाए, यह नहीं कहा गया।"),
    "hook": "टूटी पंक्ति: वही, वहाँ, और जलचरों के मांस।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "Unit 61 is damaged. Which part of it does the data list among its legible parts?",
            ("जलचरमांसानि, flesh of water-movers", "The data shows जलचरमांसानि among the clear parts, after the damaged fragment."),
            [("अभ्यें, the name of a known drug", "अभ्यें is unclear in the data."),
             ("A full list of named fish species", "No fish names are given."),
             ("The amount of flesh and its time", "No amount or time is given.")],
            "Only the plain parts are sure: तानेव च तत्र and जलचरमांसानि च.",
            "तानेव च तत्र ... जलचरमांसानि च."),
        order(1, "Put these printed parts of unit 61 in the line's order.",
              ["तानेव च", "तत्र", "गृध्र-", "जलचरमांसानि च"],
              "And those very (ones), there, gṛdhra-, and flesh of water-movers.",
              "तानेव च → तत्र → गृध्र- → जलचरमांसानि च."),
        match(2, "Match each word of unit 61 to its meaning.",
              [["तान्", "those (m. acc. pl.)"], ["एव", "very, just"], ["तत्र", "there, in that case"],
               ["जलचर", "water-mover, water animal"], ["मांस", "flesh"]],
              "The sure words of the damaged line.",
              "तान्, एव, तत्र, जलचर, मांस.", role="extend",
              teaches="जलचर = जल (water) + चर (moving): a general word for water animals."),
        mcq("discriminate", 3, "Which split of तानेव is right?",
            ("तान् + एव", "A final consonant and a vowel simply join: तान् + एव → तानेव."),
            [("तानि + एव", "इ + ए would give य: तान्येव."),
             ("ताः + एव", "आः before a vowel drops the visarga, unjoined: ता एव."),
             ("तान् + इव", "न् + इ would give नि: तानिव.")],
            "तान् (those) + एव (very): the न् joins the ए.",
            "Consonant + vowel: written together, no change."),
        multi("apply", 4, "Which statements about unit 61 are right?",
              [("The compound after गृध्र- is damaged", "Right: the data marks it damaged and incomplete."),
               ("जलचर is a general word for water animals", "Right: the data's note."),
               ("तान् एव has a clear antecedent in this unit", "The note: no clear antecedent here."),
               ("अभ्यें is a known word with a firm sense", "अभ्यें is unclear.")],
              [0, 1],
              "Damaged: only तानेव च तत्र and जलचरमांसानि are sure.",
              "तानेव च तत्र गृध्र- (क्षत) जलचरमांसानि च."),
        mcq("transfer", 5, "Built like जलचर (moving in water), what does वनचर (वन = forest) mean?",
            ("One that moves in the forest", "चर = moving: वनचर = a mover in the forest, as जलचर in water."),
            [("Water that is found in a forest", "That would need उदक or जल; चर means moving."),
             ("One who cuts down the forest", "चर means moving, not cutting."),
             ("A path that leads out of a forest", "चर means a mover in, not a way out.")],
            "वनचर = forest-mover, like जलचर = water-mover.",
            "-चर at the end of a compound = moving in.",
            teaches="-चर at the end of a compound = moving in: जलचर (in water), वनचर (in the forest)."),
    ],
}

# ---------------------------------------------------------------- unit 62
AUTHORED["62"] = {
    "title": "कफे ... अच्छसुरां त्रिरात्रं",
    "question": "By unit 62, what should be drunk in Kapha?",
    "rule": ("In Kapha, however (कफे तु), one should drink clear surā (अच्छसुरा, an intoxicating drink), with meat "
             "(पिशित) as its relish (उपदंश), for three nights, or for other periods partly lost in the print."),
    "limits": ("Low confidence. आम्रोदक is unclear and untranslated; the numeral before -रात्रं is lost; seven nights rests "
               "on a conjectural reading of समरात्रं. No question rests on these. Only three nights is clearly printed. "
               "No amount is given."),
    "explain_hi": ("पित्त के बाद अब कफ: कफ में तो साफ सुरा (अच्छसुरा), यानी मादक पेय, पिए, मांस (पिशित) को साथ खाने की वस्तु "
                   "(उपदंश) बनाकर। "
                   "अवधि में त्रिरात्र, यानी तीन रात, स्पष्ट छपा है; उसके बाद एक रात-संख्या लुप्त है, और ‘समरात्रं’ को सात रात "
                   "(सप्तरात्रं) पढ़ना केवल अनुमान है। "
                   "‘आम्रोदक’ शब्द अस्पष्ट है और छोड़ा गया है। "
                   "‘पिशितोपदंशा’ बहुव्रीहि है: जिसका उपदंश मांस हो।"),
    "hook": "कफ में: साफ सुरा, साथ में मांस, तीन रात।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 62, what is drunk in Kapha?",
            ("Clear surā with meat as relish", "पिशितोपदंशाम् अच्छसुरां ... पिबेत्."),
            [("Milk cooked with madhuka and vidārī", "That is the Pitta remedy of unit 55."),
             ("Gruel made with goat ghee and milk", "The gruel is unit 57."),
             ("Grape wine with fatty meat as relish", "Mārdvīka, grape wine, comes in unit 70.")],
            "In Kapha the drink is clear surā, with meat as its relish.",
            "कफे तु ... पिशितोपदंशामच्छसुरां ... पिबेत्."),
        order(1, "Put these words of unit 62 in the line's order.",
              ["कफे", "पिशितोपदंशाम्", "अच्छसुराम्", "त्रिरात्रम्", "पिबेत्"],
              "In Kapha, with meat as relish, clear surā, for three nights, one should drink.",
              "कफे → पिशितोपदंशाम् → अच्छसुराम् → त्रिरात्रम् → पिबेत्."),
        match(2, "Match each word of unit 62 to its meaning.",
              [["कफे", "in Kapha"], ["पिशित", "meat"], ["उपदंश", "relish, accompaniment"], ["अच्छ", "clear"],
               ["त्रिरात्र", "three nights"]],
              "The sure words of the Kapha remedy.",
              "कफे, पिशित, उपदंश, अच्छ, त्रिरात्र.", role="extend",
              teaches="पिशितोपदंशा is a bahuvrīhi: (surā) having meat as its relish."),
        mcq("discriminate", 3, "Which split of पिशितोपदंशाम् is right?",
            ("पिशित + उपदंशाम्", "अ + उ → ओ: पिशित + उपदंशाम् → पिशितोपदंशाम्."),
            [("पिशितः + उपदंशाम्", "अः before उ loses the visarga and leaves a gap; it gives no ओ."),
             ("पिशितो + पदंशाम्", "पदंशा is not a word; the word is उपदंश."),
             ("पिशित + ओपदंशाम्", "ओपदंश is not a word, and अ + ओ would give औ.")],
            "पिशित (meat) + उपदंश (relish): अ + उ → ओ.",
            "अ + उ → ओ."),
        mcq("apply", 4, "Which period in unit 62 is printed undamaged?",
            ("Three nights (त्रिरात्रम्)", "त्रिरात्रं is clear in the print."),
            [("Five nights (पञ्चरात्रम्)", "Not printed in the line."),
             ("Ten nights (दशरात्रम्)", "Not printed in the line."),
             ("One month (मासम्)", "Not printed; the line counts nights.")],
            "Only three nights is clear; the other periods are damaged.",
            "त्रिरात्रं (clear) -रात्रं (numeral lost) समरात्रं (doubtful)."),
        mcq("transfer", 5, "By the rule of पिशित + उपदंश, how is सूर्य + उदयः (sunrise) joined?",
            ("सूर्योदयः", "अ + उ → ओ, as पिशित + उपदंश → पिशितोपदंश."),
            [("सूर्यौदयः", "औ comes from अ + ओ or औ, not from अ + उ."),
             ("सूर्युदयः", "The अ is not simply dropped before उ."),
             ("सूर्येदयः", "ए comes from अ + इ.")],
            "सूर्य + उदयः = सूर्योदयः, like पिशित + उपदंश = पिशितोपदंश.",
            "अ + उ → ओ.",
            teaches="A short अ followed by उ joins as ओ: पिशित + उपदंश → पिशितोपदंश."),
    ],
}

# ---------------------------------------------------------------- unit 63
AUTHORED["63"] = {
    "title": "तिलमुद्गमाषलवणबिल्वपत्रैः पंचभिः",
    "question": "By unit 63, what is combined with the ghee, and how is it kept?",
    "rule": ("Combine a pātra (vessel-full) of ghee with five things: sesame, mung bean, black gram, salt and bilva (bael) "
             "leaves; then have it put away, well guarded (स्वनुगुप्तम्)."),
    "limits": ("Prose. Whether pātra is a fixed measure is not stated. पञ्चभिः (five) is why बिल्वपत्र is read as one "
               "item. How long it is kept, and for which condition, are not stated in this line."),
    "explain_hi": ("इस गद्य-पंक्ति में घी के एक पात्र को पाँच द्रव्यों के साथ मिलाया जाता है: तिल, मूँग (मुद्ग), उड़द (माष), "
                   "लवण और बेल (बिल्व) के पत्ते। "
                   "फिर उसे भली-भाँति सुरक्षित (स्वनुगुप्त) रखवाया जाता है। "
                   "‘पञ्चभिः’ (पाँच से) तभी मेल खाता है जब बिल्वपत्र एक ही द्रव्य गिना जाए। "
                   "पात्र कोई निश्चित माप है या नहीं, यह नहीं कहा गया। "
                   "तिल, मुद्ग, बिल्व की पहचान मानक है।"),
    "hook": "घी का पात्र + तिल, मूँग, उड़द, नमक, बेलपत्र: मिलाकर सँभालकर रखो।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 63, what is combined with the five things?",
            ("A vessel-full of ghee (घृतपात्र)", "पञ्चभिर्घृतपात्रं संयोज्य."),
            [("A vessel-full of milk (क्षीरपात्र)", "The line names ghee: घृतपात्रम्."),
             ("A vessel-full of oil (तैलपात्र)", "No oil is named in unit 63."),
             ("A vessel-full of surā (सुरापात्र)", "Surā is the Kapha drink of unit 62.")],
            "A pātra of ghee is combined with the five.",
            "पञ्चभिः घृतपात्रं संयोज्य."),
        order(1, "Put the five things of unit 63 in the line's order.",
              ["तिल", "मुद्ग", "माष", "लवण", "बिल्वपत्र"],
              "Sesame, mung bean, black gram, salt, bilva leaves.",
              "तिल → मुद्ग → माष → लवण → बिल्वपत्र."),
        match(2, "Match each of the five things of unit 63 to its meaning.",
              [["तिल", "sesame (standard)"], ["मुद्ग", "mung bean (standard)"], ["माष", "black gram (standard)"],
               ["लवण", "salt"], ["बिल्वपत्र", "bael leaves (bilva, standard)"]],
              "The five things combined with the ghee.",
              "तिल, मुद्ग, माष, लवण, बिल्वपत्र.", role="extend",
              teaches="पत्र = leaf: बिल्वपत्र = leaf of the bilva (bael); पात्र, with आ, is the vessel."),
        mcq("discriminate", 3, "Which split of स्वनुगुप्तम् is right?",
            ("सु + अनुगुप्तम्", "उ before a different vowel becomes व्: सु + अनुगुप्तम् → स्वनुगुप्तम्."),
            [("स्व + अनुगुप्तम्", "अ + अ would give आ: स्वानुगुप्तम्."),
             ("सु + नुगुप्तम्", "नुगुप्त is not a word; the word is अनुगुप्त."),
             ("स्वन् + उगुप्तम्", "उगुप्त is not a word; the data reads सु + अनुगुप्त.")],
            "सु (well) + अनुगुप्तम् (guarded): उ + अ → व.",
            "उ + a different vowel → व्."),
        mcq("apply", 4, "Why does the data read बिल्वपत्र as one item, not two?",
            ("The count word पञ्चभिः fits only then", "तिल, मुद्ग, माष, लवण, बिल्वपत्र = five."),
            [("बिल्व is not a plant name", "बिल्व is bael, standard."),
             ("पत्र here means a vessel", "पत्र = leaf; the vessel is पात्र."),
             ("The print sets a hyphen there", "No hyphen is printed in this compound.")],
            "The number word पञ्चभिः (with five) makes बिल्वपत्र one item.",
            "पञ्चभिः = with five: तिल, मुद्ग, माष, लवण, बिल्वपत्र."),
        mcq("transfer", 5, "By the rule of सु + अनुगुप्तम् → स्वनुगुप्तम्, how is अनु + अयः joined?",
            ("अन्वयः", "उ + अ → व, as सु + अनुगुप्तम् → स्वनुगुप्तम्."),
            [("अनुअयः", "उ and अ are not left side by side."),
             ("अनोयः", "उ + अ does not give ओ."),
             ("अनवयः", "The उ becomes व्, with no अ after न.")],
            "अनु + अयः = अन्वयः, like सु + अनुगुप्तम् = स्वनुगुप्तम्.",
            "उ + a different vowel → व्.",
            teaches="A final उ before a different vowel becomes व्: सु + अनुगुप्तम् → स्वनुगुप्तम्."),
    ],
}

# ---------------------------------------------------------------- unit 64
AUTHORED["64"] = {
    "title": "ततः प्रातः पिंडं बिल्वमात्रं",
    "question": "By unit 64, what is eaten, when, and with what after-drink?",
    "rule": ("Then (ततः), in the morning (प्रातः), one should eat a lump (पिण्ड) the size of a bilva (bael), with "
             "boiled, cooled goat's milk (शृतशीत छागदुग्ध) as the after-drink (अनुपान)."),
    "limits": ("Prose. What the lump is made of is not stated; the data presumes the ghee mixture of unit 63 (GROUPING), "
               "which the line does not say. bilvamātra = the size of a bilva fruit; no weight is given. The number of days "
               "is not stated."),
    "explain_hi": ("फिर सुबह (प्रातः) बेल के आकार का एक पिण्ड खाए। "
                   "उसके बाद अनुपान के रूप में उबालकर ठंडा किया हुआ बकरी का दूध (शृतशीत छागदुग्ध) ले। "
                   "पिण्ड किस चीज़ का है, यह पंक्ति नहीं कहती; डेटा इसे सम्भवतः पिछली इकाई (63) का घी-मिश्रण मानता है। "
                   "‘बिल्वमात्र’ का अर्थ है बेल फल के माप का; तौल नहीं दी गई। "
                   "‘शीतच्छाग’ में ह्रस्व अ के बाद छ दोहरा होकर च्छ बना है।"),
    "hook": "सुबह बेल-भर पिण्ड, ऊपर से उबला-ठंडा बकरी का दूध।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 64, when is the lump eaten?",
            ("In the morning (प्रातः)", "ततः प्रातः ... प्राश्नीयात्."),
            [("In the evening (सायम्)", "Evening is named in unit 77, not here."),
             ("At night (रात्रौ)", "No night is named in unit 64."),
             ("At noon (मध्याह्ने)", "No noon is named in unit 64.")],
            "The lump is eaten in the morning.",
            "ततः प्रातः पिण्डं ... प्राश्नीयात्."),
        order(1, "Put the words of unit 64 in the line's order.",
              ["ततः", "प्रातः", "पिण्डम्", "बिल्वमात्रम्", "शृतशीतच्छागदुग्धानुपानम्", "प्राश्नीयात्"],
              "Then, in the morning, a lump, the size of a bilva, with boiled cooled goat's milk as after-drink, one should eat.",
              "ततः → प्रातः → पिण्डम् → बिल्वमात्रम् → शृतशीतच्छागदुग्धानुपानम् → प्राश्नीयात्."),
        match(2, "Match each part of शृतशीतच्छागदुग्धानुपानम् to its meaning.",
              [["शृत", "boiled"], ["शीत", "cooled, cold"], ["छाग", "goat"], ["दुग्ध", "milk"], ["अनुपान", "after-drink"]],
              "Boiled, cooled goat's milk is the after-drink.",
              "शृत, शीत, छाग, दुग्ध, अनुपान.", role="extend",
              teaches="शृतशीत दुग्ध = milk boiled and cooled; the whole compound is a bahuvrīhi: having that milk as after-drink."),
        mcq("discriminate", 3, "Why is छाग printed च्छाग in शृतशीतच्छाग...?",
            ("After a short vowel छ is doubled to च्छ", "शीत ends in short अ, so छ → च्छ."),
            [("च्छाग is a different word from छाग", "It is छाग (goat), with the sandhi doubling."),
             ("छ is doubled only after a long vowel", "After a short vowel, as here, the doubling is the rule."),
             ("The doubling marks a dual number", "The doubling is sandhi, not a number ending.")],
            "शीत + छाग = शीतच्छाग: after a short vowel छ becomes च्छ.",
            "Short vowel + छ → च्छ."),
        mcq("apply", 4, "By unit 64, how big is the lump that is eaten?",
            ("The size of a bilva (bael)", "पिण्डं बिल्वमात्रम्: of the measure of a bilva."),
            [("The size of a badara (jujube)", "Badara powder is unit 65; the lump is bilva-sized."),
             ("One āḍhaka in measure", "āḍhaka is the measure of black gram in unit 56."),
             ("The size of a thumb-tip", "No thumb measure is named.")],
            "The lump is as big as a bilva fruit.",
            "बिल्वमात्र = of the size of a bilva."),
        mcq("transfer", 5, "By the rule of शीत + छाग → शीतच्छाग, how is वृक्ष + छाया (shade of a tree) joined?",
            ("वृक्षच्छाया", "After the short अ of वृक्ष, छ is doubled to च्छ."),
            [("वृक्षछाया", "After a short vowel छ must be doubled to च्छ."),
             ("वृक्षश्छाया", "There is no visarga here to become श्."),
             ("वृक्षोछाया", "No ओ arises: वृक्ष ends in अ, with no visarga.")],
            "वृक्ष + छाया = वृक्षच्छाया, like शीत + छाग = शीतच्छाग.",
            "Short vowel + छ → च्छ.",
            teaches="After a short vowel, छ is doubled to च्छ: शीत + छाग → शीतच्छाग."),
    ],
}

# ---------------------------------------------------------------- unit 65
AUTHORED["65"] = {
    "title": "अत्रैव वा बदरचूर्णपात्रमपि",
    "question": "By unit 65, what further thing is named here?",
    "rule": ("Or (वा), right here (अत्रैव), also (अपि) a pātra (vessel-full) of badara (jujube) powder is to be put in; "
             "the verb rests on the corrected reading निदध्यात्."),
    "limits": ("Prose. Printed निदष्यात् is not a form; the reading निदध्यात् (should put in) is possible only, so no question "
               "tests the verb. अत्र एव (right here) does not name its noun (this mixture or this case). pātra is the "
               "measure word of unit 63; its size is not stated."),
    "explain_hi": ("यह गद्य-पंक्ति एक विकल्प जोड़ती है: या यहीं बेर (बदर, मानक) के चूर्ण का एक पात्र भी। "
                   "‘अत्रैव’ = अत्र + एव, यहीं; किस मिश्रण या अवस्था में, यह नाम नहीं दिया गया। "
                   "छपा ‘निदष्यात्’ कोई रूप नहीं; ‘निदध्यात्’ (रखे, डाले) सम्भावित पाठ है, इसलिए क्रिया पर प्रश्न नहीं। "
                   "पात्र वही माप-शब्द है जो इकाई 63 में आया; उसका परिमाण नहीं कहा गया।"),
    "hook": "या यहीं बेर-चूर्ण का पात्र भी।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 65, the powder of which fruit is named?",
            ("Badara (jujube)", "बदरचूर्णपात्रम्: a pātra of badara powder."),
            [("Bilva (bael)", "Bilva leaves are in unit 63, and bilva gives the size in unit 64."),
             ("Tila (sesame)", "Sesame is one of the five of unit 63."),
             ("Mudga (mung)", "Mung bean is one of the five of unit 63.")],
            "The powder is of badara, jujube (standard).",
            "बदर = jujube; चूर्ण = powder."),
        order(1, "Put the words of unit 65 in the line's order (the verb is left out).",
              ["अत्र", "एव", "वा", "बदरचूर्णपात्रम्", "अपि"],
              "Here, right, or, a pātra of badara powder, also.",
              "अत्र → एव → वा → बदरचूर्णपात्रम् → अपि."),
        match(2, "Match each word of unit 65 to its meaning.",
              [["अत्र", "here"], ["बदर", "jujube (standard)"], ["चूर्ण", "powder"], ["पात्र", "vessel-full"],
               ["अपि", "also"]],
              "Here, also, a vessel-full of jujube powder.",
              "अत्र, बदर, चूर्ण, पात्र, अपि.", role="extend",
              teaches="चूर्ण = powder: बदरचूर्ण = jujube powder; बदरचूर्णपात्र = a vessel-full of it."),
        mcq("discriminate", 3, "Which split of अत्रैव is right?",
            ("अत्र + एव", "अ + ए → ऐ: अत्र + एव → अत्रैव."),
            [("अत्र + इव", "अ + इ would give ए: अत्रेव."),
             ("अत्रे + एव", "ए + ए does not give ऐ, and अत्रे is not the word."),
             ("अत्रै + व", "अत्रै and व are not the words here.")],
            "अत्र (here) + एव (just): अ + ए → ऐ.",
            "अ + ए → ऐ."),
        multi("apply", 4, "Which statements about unit 65 are right?",
              [("Badara is labelled disputed in the data", "Badara is jujube, standard."),
               ("वा marks this as another option", "Right: वा = or."),
               ("The noun of अत्र एव is not stated", "Right: the data notes the noun is not stated."),
               ("The size of the pātra is given", "Its size is not stated.")],
              [1, 2],
              "Another option, right here; the noun and the pātra's size are not stated.",
              "अत्रैव वा बदरचूर्णपात्रमपि."),
        mcq("transfer", 5, "By the rule of अत्र + एव → अत्रैव, how is तत्र + एव (right there) joined?",
            ("तत्रैव", "अ + ए → ऐ, as अत्र + एव → अत्रैव."),
            [("तत्रेव", "That is तत्र + इव, where अ + इ → ए."),
             ("तत्रयेव", "अ + ए does not put a य between them."),
             ("तत्राएव", "The two vowels merge into ऐ; they do not stand apart.")],
            "तत्र + एव = तत्रैव, like अत्र + एव = अत्रैव.",
            "अ + ए → ऐ.",
            teaches="A short अ followed by ए joins as ऐ: अत्र + एव → अत्रैव."),
    ],
}

# ---------------------------------------------------------------- unit 66
AUTHORED["66"] = {
    "title": "एवमवृद्धौ तीक्ष्णैर्विरेचयेत्",
    "question": "By unit 66, what is done when there is no growth?",
    "rule": ("Thus, when there is no growth (अवृद्धौ), one should purge (विरेचयेत्) with sharp (तीक्ष्ण) ones, and cause "
             "(it) to fall (पातयेत्) with those that make the aparā (placenta) fall."),
    "limits": ("Prose. The nouns of तीक्ष्णैः and the names of the placenta-expelling drugs are not given; the object of "
               "पातयेत् is not stated. GROUPING: it seems to close the remedies of units 56 to 65; whose growth is meant "
               "is not restated."),
    "explain_hi": ("इस प्रकार वृद्धि न होने पर (अवृद्धौ) दो काम कहे गए हैं; डेटा के अनुसार यह सम्भवतः पिछले उपायों का समापन है। "
                   "पहला, तीक्ष्ण, यानी तेज़, द्रव्यों से विरेचन कराए। "
                   "दूसरा, अपरा (जेर, मानक) को गिराने वाले द्रव्यों से गिराए; किसे गिराए, यह पंक्ति नहीं कहती। "
                   "न तीक्ष्ण द्रव्यों के नाम दिए गए हैं, न अपरा-पातनीय द्रव्यों के। "
                   "‘विरेचयेदपरा’ में त् स्वर से पहले द् बना है।"),
    "hook": "वृद्धि नहीं: तीक्ष्ण से विरेचन, अपरा-पातनीय से पातन।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 66, with what should one purge when there is no growth?",
            ("With sharp ones", "तीक्ष्णैर्विरेचयेत्: one should purge with sharp ones."),
            [("With sweet, nourishing ones", "Sweet, nourishing drugs serve growth in unit 48; here it is तीक्ष्णैः."),
             ("With cold water and milk", "No water or milk is named in unit 66."),
             ("With goat's milk and ghee", "No goat's milk or ghee is named in unit 66.")],
            "When there is no growth, the purge is with sharp ones.",
            "एवमवृद्धौ तीक्ष्णैर्विरेचयेत्."),
        order(1, "Put the words of unit 66 in the line's order.",
              ["एवम्", "अवृद्धौ", "तीक्ष्णैः", "विरेचयेत्", "अपरापातनीयैः", "पातयेत्"],
              "Thus, in no growth, with sharp ones, one should purge, with placenta-expelling ones, cause to fall.",
              "एवम् → अवृद्धौ → तीक्ष्णैः → विरेचयेत् → अपरापातनीयैः → पातयेत्."),
        match(2, "Match each word of unit 66 to its meaning.",
              [["अवृद्धि", "no growth"], ["तीक्ष्ण", "sharp, strong"], ["विरेचयेत्", "should purge"],
               ["अपरा", "placenta (standard)"], ["पातयेत्", "should cause to fall"]],
              "No growth: purge with sharp ones, and cause to fall.",
              "अवृद्धि, तीक्ष्ण, विरेचयेत्, अपरा, पातयेत्.", role="extend",
              teaches="अपरापातनीय = what causes the aparā (placenta) to fall."),
        mcq("discriminate", 3, "In विरेचयेदपरा..., why does त् become द्?",
            ("त् before a vowel becomes द्", "A vowel is voiced: विरेचयेत् + अपरा → विरेचयेदपरा."),
            [("त् becomes द् before every sound", "Before an unvoiced sound it stays त्."),
             ("द् is the optative ending", "The optative ending is -एत्; द् comes from sandhi."),
             ("It is a print slip for त्", "It is regular sandhi, not a slip.")],
            "विरेचयेत् + अपरा = विरेचयेदपरा: त् → द् before a vowel.",
            "त् + voiced sound (vowels included) → द्."),
        multi("apply", 4, "Which statements about unit 66 are right?",
              [("The object of पातयेत् is not stated", "Right: the data notes the object is not stated."),
               ("The placenta-expelling drugs are named", "The Sanskrit gives no names."),
               ("It says the fetus has grown well", "The case is अवृद्धि, no growth."),
               ("The nouns of तीक्ष्णैः are not given", "Right: only sharp ones; the nouns are not stated.")],
              [0, 3],
              "Two actions for no growth; no drug names and no object are given.",
              "एवमवृद्धौ तीक्ष्णैर्विरेचयेदपरापातनीयैश्च पातयेत्."),
        mcq("transfer", 5, "Built like अवृद्धि (no growth), what does अनिद्रा (निद्रा = sleep) mean?",
            ("Lack of sleep", "अ- negates, as in अवृद्धि."),
            [("Deep sleep", "अ- negates; it does not deepen."),
             ("Time for sleep", "अ- adds no time."),
             ("Sleep again", "अ- does not mean again.")],
            "अनिद्रा = lack of sleep, like अवृद्धि = lack of growth.",
            "अ- before a consonant = not, lack of.",
            teaches="अ- before a consonant negates: अवृद्धि (no growth), अनिद्रा (no sleep)."),
    ],
}

# ---------------------------------------------------------------- unit 67
AUTHORED["67"] = {
    "title": "संलीनो गर्भः ... तं लीनमित्याहुः",
    "question": "By unit 67, what condition is called līna?",
    "rule": ("When a woman's channels (स्रोतस्) are afflicted by Vāta (वातोपसृष्ट), the fetus clings (संलीन) and does not "
             "move (न स्पन्दते): that they call līna (लीन)."),
    "limits": ("Prose. प्रमुमः is unclear; stupefied rests on the conjectural reading प्रमूढः, so no question rests on it. "
               "Printed स्रोतासि is read स्रोतांसि (possible). Whether तम् names the fetus or the condition is not stated. "
               "No treatment is given in this line."),
    "explain_hi": ("यहाँ से लीनगर्भ का प्रसंग आरम्भ होता है। "
                   "जिस स्त्री के स्रोतस, यानी शरीर के मार्ग, वात से ग्रस्त (उपसृष्ट) हों, उसका गर्भ चिपका हुआ (संलीन) रहता है "
                   "और हिलता नहीं (न स्पन्दते); उसे लीन कहते हैं। "
                   "छपा ‘प्रमुमो’ अस्पष्ट है; ‘प्रमूढ’ (जड़) केवल अनुमानित पाठ है, इसलिए उस पर प्रश्न नहीं। "
                   "‘तम्’ गर्भ को कहता है या अवस्था को, यह स्पष्ट नहीं। "
                   "उपचार अगली इकाइयों में है।"),
    "hook": "वात से रुके स्रोतस, गर्भ चिपका, हिले नहीं: लीन।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 67, what name is given when the fetus clings and does not move?",
            ("Līna (लीन)", "तं लीनमित्याहुः: that they call līna."),
            [("Āmagarbha (आमगर्भ)", "Āmagarbha is named in units 49 and 60, not as this condition."),
             ("Mūḍhagarbha (मूढगर्भ)", "Mūḍhagarbha comes later, in the section of units 78 to 88."),
             ("Upaviṣṭaka (उपविष्टक)", "Upaviṣṭaka is a different condition, named in units 45 and 56.")],
            "A clinging fetus that does not move is called līna.",
            "संलीनो गर्भः ... न स्पन्दते, तं लीनमित्याहुः."),
        order(1, "Put these parts of unit 67 in the line's order.",
              ["यस्याः पुनः", "संलीनो गर्भः", "न स्पन्दते", "तं लीनम्", "इत्याहुः"],
              "Of her however, the fetus clinging, does not move, that līna, thus they call.",
              "यस्याः पुनः → संलीनो गर्भः → न स्पन्दते → तं लीनम् → इत्याहुः."),
        match(2, "Match each word of unit 67 to its meaning.",
              [["उपसृष्ट", "afflicted, touched"], ["स्रोतस्", "body channel"], ["संलीन", "clinging, hidden"],
               ["स्पन्दते", "moves"], ["आहुः", "they call, they say"]],
              "Vāta-afflicted channels, a clinging fetus that does not move: they call it līna.",
              "उपसृष्ट, स्रोतस्, संलीन, स्पन्दते, आहुः.", role="extend",
              teaches="लीन = clinging, hidden: the name the text gives to a fetus that clings and does not move."),
        mcq("discriminate", 3, "Which split of इत्याहुः is right?",
            ("इति + आहुः", "इ before a different vowel becomes य्: इति + आहुः → इत्याहुः."),
            [("इति + याहुः", "याहुः is not a word, and इ before य would not drop."),
             ("इतः + आहुः", "अः before आ drops the visarga, unjoined: इत आहुः."),
             ("इति + अहुः", "इ + अ would give य: इत्यहुः, with short अ.")],
            "इति (thus) + आहुः (they call): इ + आ → या.",
            "इ + a different vowel → य् + that vowel."),
        mcq("apply", 4, "A woman's channels are afflicted, and her fetus clings and does not move. By unit 67, which doṣa is at work?",
            ("Vāta (वात)", "वातोपसृष्टस्रोतांसि: channels afflicted by Vāta."),
            [("Pitta (पित्त)", "Pitta is not named in unit 67."),
             ("Kapha (कफ)", "Kapha is not named in unit 67."),
             ("Pitta and Kapha (पित्तकफ)", "Neither is named; the line names Vāta.")],
            "The channels are afflicted by Vāta.",
            "वात + उपसृष्ट = वातोपसृष्ट, afflicted by Vāta."),
        mcq("transfer", 5, "By the rule of संलीनः + गर्भः → संलीनो गर्भः, how is वृक्षः + भवति written?",
            ("वृक्षो भवति", "अः before the voiced भ becomes ओ."),
            [("वृक्षा भवति", "That is the pattern of आः, not अः."),
             ("वृक्षर्भवति", "र् comes after vowels other than अ and आ."),
             ("वृक्षः भवति", "Before a voiced sound the visarga after अ does not stay.")],
            "वृक्षः + भवति = वृक्षो भवति, like संलीनः + गर्भः = संलीनो गर्भः.",
            "अः + voiced consonant → ओ.",
            teaches="A visarga after अ becomes ओ before a voiced consonant: संलीनः + गर्भः → संलीनो गर्भः."),
    ],
}

# ---------------------------------------------------------------- unit 68
AUTHORED["68"] = {
    "title": "तत्र श्येनोत्क्रोश... रक्तशाल्योदनं भोजयेत्",
    "question": "By unit 68, with what is red śāli rice fed, apparently in the līna case?",
    "rule": ("In that case (तत्र), feed red śāli rice (रक्तशाल्योदन) with the rasa (broth) of any one (अन्यतम) of eight "
             "animals, with plenty of ghee, or with a soup (यूष) of māṣa (black gram) or mūlaka (radish) rich in ghee."),
    "limits": ("Prose. go = cow, the plain sense. śyena, utkrośa, tittirī probable; godha, śikhin, mūlaka, śāli standard. "
               "Which liquid each ghee word qualifies is the plain reading only. The woman fed is not named. GROUPING: it "
               "appears to continue unit 67 (the līna case)."),
    "explain_hi": ("सम्भवतः लीन गर्भ की अवस्था में (तत्र) लाल शालि का भात (रक्तशाल्योदन) खिलाया जाता है। "
                   "उसके साथ आठ में से किसी एक (अन्यतम) का बहुत घी वाला रस: श्येन (सम्भवतः बाज), उत्क्रोश (सम्भवतः कुरर), गाय, "
                   "मछली, गोधा (गोह, मानक), शिखी (मोर, मानक), कुक्कुट (मुर्गा) और तित्तिरि (सम्भवतः तीतर)। "
                   "या फिर घी से भरपूर माष (उड़द) का यूष या मूलक (मूली, मानक) का यूष। "
                   "‘गो’ को गाय का सरल अर्थ लिया गया है। "
                   "कौन-सा घी-विशेषण किस द्रव से जुड़ता है, यह केवल सरल पाठ है।"),
    "hook": "लीन में: लाल शालि-भात, आठ में से एक का घी-रस, या घी-भरा उड़द/मूली यूष।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 68, which food is fed with the broth or soup?",
            ("Red śāli rice", "रक्तशाल्योदनं भोजयेत्."),
            [("Saktu, roasted-grain flour", "Saktu comes in unit 69."),
             ("Wheat cakes with honey", "No wheat or honey is named in unit 68."),
             ("Yavāgū, a thick gruel", "Yavāgū is the gruel of unit 57.")],
            "The food is boiled red śāli rice.",
            "रक्तशाल्योदनं भोजयेत्."),
        order(1, "Put these parts of unit 68 in the line's order.",
              ["श्येनोत्क्रोश...तित्तिरीणाम्", "अन्यतमस्य रसेन", "भूरिसर्पिष्केण", "माषयूषेण", "मूलकयूषेण वा",
               "रक्तशाल्योदनं भोजयेत्"],
              "Of hawk ... partridge, with the broth of any one, with plenty of ghee, with black-gram soup, or with radish "
              "soup, red śāli rice one should feed.",
              "श्येनोत्क्रोश...तित्तिरीणाम् → अन्यतमस्य रसेन → भूरिसर्पिष्केण → माषयूषेण → मूलकयूषेण वा → रक्तशाल्योदनं भोजयेत्."),
        match(2, "Match each word of unit 68 to its meaning.",
              [["श्येन", "probably hawk"], ["उत्क्रोश", "probably osprey"], ["गोध", "monitor lizard (standard)"],
               ["शिखिन्", "peacock (standard)"], ["मूलक", "radish (standard)"], ["यूष", "strained soup"]],
              "Four of the eight animals, the radish, and the soup.",
              "श्येन, उत्क्रोश, गोध, शिखिन्, मूलक, यूष.", role="extend",
              teaches="अन्यतम = any one of several: तित्तिरीणाम् अन्यतमस्य रसेन = with the broth of any one of them."),
        mcq("discriminate", 3, "Which split of शाल्योदनम् is right?",
            ("शालि + ओदनम्", "इ before a different vowel becomes य्: शालि + ओदनम् → शाल्योदनम्."),
            [("शाल + ओदनम्", "अ + ओ would give औ: शालौदनम्."),
             ("शाल्यः + ओदनम्", "अः before ओ drops the visarga, unjoined: शाल्य ओदनम्."),
             ("शाल्यो + दनम्", "दनम् is not a word; the word is ओदन, boiled rice.")],
            "शालि (śāli rice) + ओदनम् (boiled rice): इ + ओ → यो.",
            "इ + a different vowel → य् + that vowel."),
        multi("apply", 4, "Which statements does unit 68 make?",
              [("The broth of any one animal is used", "Right: अन्यतमस्य रसेन, with the broth of any one."),
               ("The broths of all eight are mixed", "अन्यतमस्य = any one, not all mixed."),
               ("A soup of māṣa or mūlaka may be used", "Right: माषयूषेण मूलकयूषेण वा."),
               ("The rice named is red śāli", "Right: रक्तशाल्योदनम्, red śāli rice.")],
              [0, 2, 3],
              "Red śāli rice with one animal's broth, or with a black-gram or radish soup.",
              "अन्यतमस्य रसेन ... माषयूषेण मूलकयूषेण वा ... रक्तशाल्योदनं भोजयेत्."),
        mcq("transfer", 5, "Built like तित्तिरीणाम् अन्यतमस्य (of any one of them), what does फलानाम् अन्यतमम् mean?",
            ("Any one of the fruits", "अन्यतम with a genitive plural = any one of them."),
            [("All of the fruits", "अन्यतम picks one, not all."),
             ("The last of the fruits", "अन्यतम does not mean last."),
             ("A fruit other than these", "अन्यतम is one of these, not another outside them.")],
            "फलानाम् अन्यतमम् = any one of the fruits, like तित्तिरीणाम् अन्यतमस्य.",
            "अन्यतम + genitive plural = any one of them.",
            teaches="अन्यतम with a genitive plural = any one of them: ...तित्तिरीणाम् अन्यतमस्य = of any one of those animals."),
    ],
}


# ===================================================================== NOTES_HI
NOTES_HI = {
    "55": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। मधुक = मुलेठी (सम्भावित); यह शब्द महुआ वृक्ष भी हो सकता है, इसलिए पहचान "
           "सावधानी से। विदारी = विदारीकन्द (सम्भावित, इकाई 53 में)। निर्यूह = काढ़ा; सिद्ध = पकाया हुआ। छपा ‘पिबेत’ हलन्त के बिना है; "
           "डेटा इसे आत्मनेपद विधिलिङ् मानता है, जबकि सामान्य रूप पिबेत् है; रूप पर प्रश्न नहीं। सन्धि जाँची: सिद्धम् + पयः → सिद्धं पयः "
           "(पद-अन्त म् व्यंजन से पहले अनुस्वार); पयः + पिबेत → पयः पिबेत (अघोष प से पहले विसर्ग बना रहता है)।"),
    "56": ("गद्य; विश्वास मध्यम। पाठ-चिह्न: ‘संक्षुध्य’ → सम्भावित संक्षुद्य (√क्षुद्, कूटना); ‘अन्यातर’ → अन्यतर (लगभग निश्चित); "
           "‘वृद्व्यर्थं’ → वृद्ध्यर्थं (लगभग निश्चित)। इन रूपों पर प्रश्न नहीं। वाक्य का बीच का भाग ढीला: कुटा द्रव्य भी साथ पकता हो, यह सम्भव। "
           "कुक्कुटी = मुर्गी (डेटा का पाठ); आढक का परिमाण नहीं दिया; उदूखल = उलूखल का स्वीकृत रूप। पहचान: माष = उड़द (मानक), "
           "तित्तिरि = तीतर (सम्भावित), कपिञ्जल विवादित। सन्धि जाँची: स्थूलकुक्कुटीः + निस्तुष → स्थूलकुक्कुटीर्निस्तुष (ई के बाद विसर्ग, "
           "घोष न से पहले → र्); माष + आढकम् → माषाढकम्; क्षीर + उदकेन → क्षीरोदकेन; क्षीरोदकेन + उदूखले → क्षीरोदकेनोदूखले (अ + उ → ओ); "
           "तत् + रसेन → तद्रसेन (त् घोष से पहले → द्); पाययेत् + उप → पाययेदुप; वृद्धि + अर्थम् → वृद्ध्यर्थम्।"),
    "57": ("गद्य; विश्वास मध्यम। पाठ-चिह्न: छपा ‘जीवनी यैश्च’ बीच में रिक्त स्थान से टूटा है; डेटा इसे जीवनीयैः + च पढ़ता है (सम्भावित), "
           "इसलिए इस पर प्रश्न नहीं। जीवनीय द्रव्य यहाँ गिनाए नहीं गए। GROUPING: पिछली इकाई (56) के उपायों का क्रम। छपा ‘पिबेत’ हलन्त "
           "के बिना (इकाई 55 जैसा)। सन्धि जाँची: जीवनीयैः + च → जीवनीयैश्च (च से पहले विसर्ग → श्); संस्कृताम् + यवागूम् → संस्कृतां यवागूम्; "
           "यवागूम् + पिबेत → यवागूं पिबेत (म् → अनुस्वार)।"),
    "58": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। पहचान: पयस्या विवादित (क्षीरविदारी, Ipomoea digitata, Pueraria tuberosa उम्मीदवार); "
           "काकोली विवादित, और जोड़े के दो सदस्य यहाँ नामित नहीं; सुनिषण्णक = चौपतिया (सम्भावित)। ‘पयस्या’ को सूची का पहला सदस्य "
           "माना गया, अलग कर्ता नहीं। GROUPING: इकाई 57 का क्रम। सन्धि जाँची: सर्पिः + विपचेत् → सर्पिर्विपचेत् (इ के बाद विसर्ग, घोष व "
           "से पहले → र्)।"),
    "59": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। GROUPING: डेटा ‘तेन’ को इकाई 58 का घी मानता है; उपयुञ्जीत का कर्म नहीं लिखा। "
           "‘क्षीरानुपानम्’ क्रिया-विशेषण की तरह: दूध को अनुपान बनाकर। छपा ‘उपयुंजीत’ = उपयुञ्जीत (अनुस्वार वर्गीय ञ् के लिए)। "
           "सन्धि जाँची: क्षीर + अनुपानम् → क्षीरानुपानम् (अ + अ → आ); क्षीरानुपानम् + उपयुञ्जीत → क्षीरानुपानमुपयुञ्जीत।"),
    "60": ("गद्य; विश्वास मध्यम। पाठ-चिह्न: ‘आमगर्भरासेन’ → आमगर्भरसेन (लगभग निश्चित; ‘रास’ यहाँ शब्द नहीं)। आमगर्भ का ठीक अर्थ "
           "अनिश्चित (पशुओं के कच्चे भ्रूण या अण्डे, कहा नहीं गया); इस पर प्रश्न नहीं। खाया जाने वाला भोजन नहीं लिखा। GROUPING: "
           "इकाई 57 से 59 के बाद एक और उपाय। सन्धि जाँची: वा + अश्नीयात् → वाश्नीयात् (आ + अ → आ); छपाई ने लुप्त अ को ऽ से दिखाया है।"),
    "61": ("गद्य; विश्वास निम्न। पाठ-चिह्न: ‘गृध्र- अभ्येंजलचरमांसानि’ क्षतिग्रस्त; ‘अभ्यें’ अस्पष्ट, बीच का भाग अपुनर्निर्मेय; गृध्र (गिद्ध) "
           "केवल अनुमानित। इन पर प्रश्न नहीं। ‘तान् एव’ (पुंलिंग बहुवचन) का पूर्ववर्ती इस इकाई में स्पष्ट नहीं; सम्भवतः पिछली इकाइयों के रस "
           "या मांस। GROUPING: इकाई 57 से 60 का क्रम। सन्धि जाँची: तान् + एव → तानेव (व्यंजन + स्वर, बिना परिवर्तन)।"),
    "62": ("गद्य; विश्वास निम्न। पाठ-चिह्न: ‘त्वाम्रोदक’ = तु + आम्रोदक, पर ‘आम्रोदक’ अस्पष्ट (शायद आम्र-उदक, अर्थ पक्का नहीं), "
           "अस्पष्ट छोड़ा गया; ‘-रात्रं’ से पहले की संख्या लुप्त; ‘समरात्रं’ → सम्भावित सप्तरात्रं (सात रात, अनुमानित)। इन पर प्रश्न नहीं; "
           "केवल त्रिरात्र स्पष्ट। ‘पिशितोप दंशाम्’ में रिक्त स्थान छपाई की चूक, पिशितोपदंशाम् पढ़ा गया। सन्धि जाँची: पिशित + उपदंशाम् → "
           "पिशितोपदंशाम् (अ + उ → ओ); उपदंशाम् + अच्छसुराम् → उपदंशामच्छसुराम्; त्रिरात्रम् + (व्यंजन) → त्रिरात्रं।"),
    "63": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। ‘पञ्चभिः’ पाँच द्रव्यों से मेल खाता है, इसलिए बिल्वपत्र एक द्रव्य। पात्र निश्चित माप है "
           "या नहीं, नहीं कहा (इकाई 65 में फिर)। पहचान: तिल, मुद्ग, बिल्व मानक; माष = उड़द (मानक, इकाई 56)। छपा ‘पंचभिः’ = पञ्चभिः। "
           "सन्धि जाँची: पत्रैः + पञ्चभिः → पत्रैः पञ्चभिः (अघोष प से पहले विसर्ग); पञ्चभिः + घृत → पञ्चभिर्घृत (इ के बाद विसर्ग, घोष घ से "
           "पहले → र्); घृतपात्रम् + संयोज्य → घृतपात्रं संयोज्य; सु + अनुगुप्तम् → स्वनुगुप्तम् (उ + अ → व)।"),
    "64": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। GROUPING: पिण्ड सम्भवतः इकाई 63 का मिश्रण, कहा नहीं गया। बिल्वमात्र = बेल फल के "
           "माप का। छपा ‘पिंडं’ = पिण्डम्। सन्धि जाँची: ततः + प्रातः → ततः प्रातः; प्रातः + पिण्डम् → प्रातः पिण्डम् (अघोष प से पहले विसर्ग); "
           "शीत + छाग → शीतच्छाग (ह्रस्व स्वर के बाद छ → च्छ); दुग्ध + अनुपानम् → दुग्धानुपानम् (अ + अ → आ)।"),
    "65": ("गद्य; विश्वास मध्यम। पाठ-चिह्न: ‘निदष्यात्’ कोई रूप नहीं → सम्भावित निदध्यात् (नि-√धा, रखे); इसलिए क्रिया पर प्रश्न नहीं। "
           "‘अत्र एव’ का संज्ञा-शब्द नहीं लिखा। पात्र वही माप-शब्द जो इकाई 63 में; परिमाण नहीं। पहचान: बदर = बेर (मानक)। सन्धि जाँची: "
           "अत्र + एव → अत्रैव (अ + ए → ऐ); पात्रम् + अपि → पात्रमपि।"),
    "66": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। GROUPING: इकाई 56 से 65 के उपायों का समापन, वृद्धि न होने पर। तीक्ष्ण द्रव्यों और "
           "अपरा-पातनीय द्रव्यों के नाम नहीं; पातयेत् का कर्म नहीं लिखा। अपरा = जेर (मानक)। सन्धि जाँची: एवम् + अवृद्धौ → एवमवृद्धौ; "
           "तीक्ष्णैः + विरेचयेत् → तीक्ष्णैर्विरेचयेत् (ऐ के बाद विसर्ग, घोष व से पहले → र्); विरेचयेत् + अपरा → विरेचयेदपरा (त् स्वर से पहले → "
           "द्); अपरापातनीयैः + च → अपरापातनीयैश्च।"),
    "67": ("गद्य; विश्वास मध्यम। पाठ-चिह्न: ‘स्रोतासि’ → सम्भावित स्रोतांसि (अनुस्वार छूटा); ‘प्रमुमो’ अस्पष्ट → अनुमानित प्रमूढो (जड़); "
           "इन पर प्रश्न नहीं। ‘तम्’ (पुंलिंग) गर्भ या अवस्था, किसे लीन कहा, स्पष्ट नहीं। सन्धि जाँची: पुनर् का र् घोष व से पहले बना रहता "
           "है (पुनर्वात); वात + उपसृष्ट → वातोपसृष्ट; संलीनः + गर्भः → संलीनो गर्भः (अः + घोष → ओ); तम् + लीनम् → तं लीनम्; लीनम् + इति "
           "→ लीनमिति; इति + आहुः → इत्याहुः (इ + आ → या)।"),
    "68": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। GROUPING: इकाई 67 (लीन) का उपचार। आठ नाम: श्येन (बाज, सम्भावित), उत्क्रोश "
           "(कुरर/ऑस्प्रे, सम्भावित), गो (गाय, सरल अर्थ), मत्स्य, गोध (गोह, मानक; छपा ‘गोध’, सामान्य रूप गोधा), शिखिन् (मोर, मानक), कुक्कुट, "
           "तित्तिरि (तीतर, सम्भावित)। मूलक = मूली, शालि (मानक)। ‘भूरिसर्पिष्क’ रस से और ‘घृताढ्य’ यूषों से, यह सरल पाठ है; दोनों सब से भी "
           "जुड़ सकते हैं। सन्धि जाँची: श्येन + उत्क्रोश → श्येनोत्क्रोश; तित्तिरीणाम् + अन्यतमस्य → तित्तिरीणामन्यतमस्य; घृत + आढ्येन → "
           "घृताढ्येन; शालि + ओदनम् → शाल्योदनम् (इ + ओ → यो)।"),
}


# ===================================================================== AIDS
AIDS = {
    "55": {
        "chunks": "पित्ते | मधुकविदारीनिर्यूहसिद्धं | पयः पिबेत",
        "frame": ("कब: पित्ते (पित्त में) → क्या: पयः (दूध) → कैसा: मधुक (सम्भवतः मुलेठी) और विदारी (सम्भवतः विदारीकन्द) के "
                  "निर्यूह (काढ़े) से सिद्ध → क्रिया: पिबेत (पिए)।"),
        "sandhi": "पद-अन्त म् + व्यंजन → अनुस्वार: सिद्धम् + पयः → सिद्धं पयः · अघोष प से पहले विसर्ग बना रहता है: पयः पिबेत।",
    },
    "56": {
        "chain": {"steps": ["तीन मोटी मुर्गियाँ और आढक भर छिलका-रहित उड़द", "दूध-जल के साथ ओखली में कूटना",
                            "उस रस और घी से तीतर (सम्भावित) या कपिञ्जल (विवादित) का रस पकाना",
                            "पिलाना: उपविष्टक और उपशुष्कक की वृद्धि के लिए"]},
        "chunks": ("तिस्रः स्थूलकुक्कुटीर्निस्तुषमाषाढकं च | क्षीरोदकेनोदूखले संक्षुध्य | तद्रसेन सर्पिषा च | "
                   "तित्तिरिकपिंजलान्यातररसं साधयित्वा | पाययेदुपविष्टकविवर्द्धनार्थमुपशुष्ककवृद्व्यर्थं च"),
        "sandhi": ("अ + उ → ओ: क्षीरोदकेन + उदूखले → क्षीरोदकेनोदूखले · त् + घोष → द्: तत् + रसेन → तद्रसेन · ई के बाद विसर्ग, "
                   "घोष से पहले → र्: स्थूलकुक्कुटीः + निस्तुष → स्थूलकुक्कुटीर्निस्तुष · अ + आ → आ: माष + आढकम् → माषाढकम्।"),
        "frame": ("क्या कूटें: तीन कुक्कुटी, आढक माष → किसके साथ: क्षीरोदकेन, उदूखले → किससे पकाएँ: तद्रसेन सर्पिषा च → क्या पकाएँ: "
                  "पक्षी का रस → क्रिया: पाययेत् → किसलिए: उपविष्टक, उपशुष्कक।"),
    },
    "57": {
        "diagram": {"groups": [
            {"label": "किससे संस्कृत (क्रम से)", "items": ["बकरी का घी (अजासर्पिस्)", "दूध (क्षीर)",
                                                        "जीवनीय द्रव्य (जोड़ा हुआ पाठ)"]},
            {"label": "क्या पिए", "items": ["यवागू (गाढ़ी लपसी)"]}]},
        "chunks": "अजासर्पिषा | क्षीरेण | जीवनी यैश्च | संस्कृतां यवागूं पिबेत",
        "sandhi": "पद-अन्त म् + व्यंजन → अनुस्वार: संस्कृताम् + यवागूम् → संस्कृतां यवागूम् · च से पहले विसर्ग → श्: जीवनीयैः + च → जीवनीयैश्च।",
    },
    "58": {
        "diagram": {"groups": [
            {"label": "कल्क के द्रव्य (क्रम से)", "items": ["पयस्या (विवादित)", "काकोली का जोड़ा (विवादित)",
                                                         "सुनिषण्णक: चौपतिया (सम्भावित)"]},
            {"label": "पकाना", "items": ["कल्क + दूध के साथ", "घी पकाए (सर्पिर्विपचेत्)"]}]},
        "chunks": "पयस्या | काकोलीद्वयसुनिषण्णककल्केन | पयसा च | सर्पिर्विपचेत्",
        "sandhi": "इ के बाद विसर्ग, घोष से पहले → र्: सर्पिः + विपचेत् → सर्पिर्विपचेत्।",
    },
    "59": {
        "chunks": "तेन | क्षीरानुपानम् | उपयुंजीत",
        "sandhi": "अ + अ → आ: क्षीर + अनुपानम् → क्षीरानुपानम् · स्वर से पहले म् बना रहता है: क्षीरानुपानम् + उपयुञ्जीत → क्षीरानुपानमुपयुञ्जीत।",
        "frame": "साधन: तेन (उससे; डेटा: इकाई 58 का घी) → कैसे: क्षीरानुपानम् (दूध अनुपान बनाकर) → क्रिया: उपयुञ्जीत (उपयोग करे); कर्म नहीं लिखा।",
    },
    "60": {
        "chunks": "आमगर्भरासेन | वाऽश्नीयात्",
        "sandhi": "आ + अ → आ: वा + अश्नीयात् → वाश्नीयात् (छपाई में लुप्त अ का चिह्न ऽ)।",
        "frame": "विकल्प: वा (या) → साधन: आमगर्भरसेन (आमगर्भ के रस से; अर्थ अनिश्चित) → क्रिया: अश्नीयात् (खाए); भोजन नहीं लिखा।",
    },
    "61": {
        "chunks": "तानेव च | तत्र | गृध्र- (क्षत) अभ्यें (अस्पष्ट) | जलचरमांसानि च",
        "sandhi": "व्यंजन + स्वर, बिना परिवर्तन: तान् + एव → तानेव।",
        "anchors": "याद-सूत्र: पंक्ति टूटी है; सबसे स्पष्ट ‘तानेव च तत्र’ और ‘जलचरमांसानि’। (मेरी याद-पद्धति)",
    },
    "62": {
        "chunks": "कफे त्वाम्रोदक (अस्पष्ट) | पिशितोप दंशामच्छसुरां | त्रिरात्रं -रात्रं समरात्रं वा | पिबेत्",
        "sandhi": "अ + उ → ओ: पिशित + उपदंशाम् → पिशितोपदंशाम् · स्वर से पहले म् बना रहता है: उपदंशाम् + अच्छसुराम् → उपदंशामच्छसुराम्।",
        "frame": ("कब: कफे तु (कफ में तो) → क्या: अच्छसुरा (साफ सुरा) → साथ में: पिशित (मांस) उपदंश → कितने दिन: त्रिरात्र (स्पष्ट); "
                  "बाकी अवधियाँ क्षत → क्रिया: पिबेत्।"),
    },
    "63": {
        "diagram": {"groups": [
            {"label": "पाँच द्रव्य (क्रम से)", "items": ["तिल (मानक)", "मुद्ग: मूँग (मानक)", "माष: उड़द (मानक)", "लवण: नमक",
                                                      "बिल्वपत्र: बेल के पत्ते (मानक)"]},
            {"label": "क्रिया", "items": ["घी के पात्र से मिलाए", "भली-भाँति सुरक्षित रखवाए"]}]},
        "chunks": "तिलमुद्गमाषलवणबिल्वपत्रैः पंचभिः | घृतपात्रं संयोज्य | स्वनुगुप्तं निधापयेत्",
        "sandhi": ("इ के बाद विसर्ग, घोष से पहले → र्: पञ्चभिः + घृत → पञ्चभिर्घृत · उ + अ → व: सु + अनुगुप्तम् → स्वनुगुप्तम्।"),
        "letters": "पाँच द्रव्यों के पहले अक्षर क्रम से: ति-मु-मा-ल-बि (तिल, मुद्ग, माष, लवण, बिल्वपत्र)। (मेरी याद-पद्धति)",
    },
    "64": {
        "chain": {"steps": ["ततः, प्रातः (फिर, सुबह)", "बिल्व के आकार का पिण्ड", "अनुपान: उबाला-ठंडा बकरी का दूध",
                            "खाए (प्राश्नीयात्)"]},
        "chunks": "ततः प्रातः | पिंडं बिल्वमात्रं | शृतशीतच्छागदुग्धानुपानं | प्राश्नीयात्",
        "sandhi": "ह्रस्व स्वर के बाद छ → च्छ: शीत + छाग → शीतच्छाग · अ + अ → आ: दुग्ध + अनुपानम् → दुग्धानुपानम्।",
    },
    "65": {
        "chunks": "अत्रैव वा | बदरचूर्णपात्रमपि | निदष्यात् (सुधार: निदध्यात्, सम्भावित)",
        "sandhi": "अ + ए → ऐ: अत्र + एव → अत्रैव · स्वर से पहले म् बना रहता है: पात्रम् + अपि → पात्रमपि।",
        "frame": "विकल्प: वा → कहाँ: अत्रैव (यहीं) → क्या: बदरचूर्णपात्र (बेर-चूर्ण का पात्र) → अपि (भी) → क्रिया: निदध्यात् (सम्भावित पाठ)।",
    },
    "66": {
        "diagram": {"groups": [
            {"label": "अवस्था", "items": ["अवृद्धि (वृद्धि न हो)"]},
            {"label": "दो काम (क्रम से)", "items": ["तीक्ष्णों से विरेचन", "अपरा-पातनीयों से पातन"]}]},
        "chunks": "एवमवृद्धौ | तीक्ष्णैर्विरेचयेत् | अपरापातनीयैश्च पातयेत्",
        "sandhi": ("ऐ के बाद विसर्ग, घोष से पहले → र्: तीक्ष्णैः + विरेचयेत् → तीक्ष्णैर्विरेचयेत् · त् स्वर से पहले → द्: "
                   "विरेचयेत् + अपरा → विरेचयेदपरा।"),
        "frame": "अवस्था: एवम् अवृद्धौ (इस प्रकार वृद्धि न होने पर) → १ साधन: तीक्ष्णैः, क्रिया: विरेचयेत् → २ साधन: अपरापातनीयैः, क्रिया: पातयेत् (कर्म नहीं लिखा)।",
    },
    "67": {
        "diagram": {"groups": [
            {"label": "स्थिति", "items": ["स्रोतस वात से ग्रस्त", "गर्भ संलीन (चिपका)", "गर्भ हिलता नहीं"]},
            {"label": "नाम", "items": ["लीन"]}]},
        "chunks": "यस्याः पुनर्वातोपसृष्टस्रोतासि | संलीनो गर्भः प्रमुमो (अस्पष्ट) न स्पंदते | तं लीनमित्याहुः",
        "sandhi": ("अः + घोष → ओ: संलीनः + गर्भः → संलीनो गर्भः · अ + उ → ओ: वात + उपसृष्ट → वातोपसृष्ट · इ + आ → या: "
                   "इति + आहुः → इत्याहुः।"),
        "anchors": "याद-सूत्र: लीन = चिपका, छिपा; जो गर्भ चिपककर हिले नहीं, वही लीन। (मेरी याद-पद्धति)",
    },
    "68": {
        "diagram": {"groups": [
            {"label": "रस: किसी एक का, बहुत घी सहित", "items": ["श्येन: बाज (सम्भावित)", "उत्क्रोश: कुरर (सम्भावित)",
                                                              "गो: गाय", "मत्स्य: मछली", "गोध: गोह (मानक)",
                                                              "शिखी: मोर (मानक)", "कुक्कुट: मुर्गा",
                                                              "तित्तिरि: तीतर (सम्भावित)"]},
            {"label": "या घी-भरपूर यूष", "items": ["माष (उड़द) का यूष", "मूलक (मूली, मानक) का यूष"]}]},
        "chunks": ("तत्र | श्येनोत्क्रोशगोमत्स्यगोधशिखिकुक्कुटतित्तिरीणामन्यतमस्य | रसेन भूरिसर्पिष्केण | "
                   "माषयूषेण मूलकयूषेण वा घृताढ्येन | रक्तशाल्योदनं भोजयेत्"),
        "sandhi": ("इ + ओ → यो: शालि + ओदनम् → शाल्योदनम् · अ + उ → ओ: श्येन + उत्क्रोश → श्येनोत्क्रोश · अ + आ → आ: "
                   "घृत + आढ्येन → घृताढ्येन।"),
        "letters": "आठ जीवों के पहले अक्षर क्रम से: श्ये-उ-गो-म-गो-शि-कु-ति। (मेरी याद-पद्धति)",
    },
}


# ===================================================================== IMAGE_SPECS
IMAGE_SPECS = {
    ("56", "chain"): {
        "file": "sh4-kukkuti-rasa-56.svg",
        "alt": ("Chain of unit 56 in four steps: three large hens and an āḍhaka of husked black gram; crushed with milk and "
                "water in a mortar; with that juice and ghee, the broth of partridge (probable) or kapiñjala (disputed) is "
                "prepared; she is made to drink it for the growth in upaviṣṭaka and upaśuṣkaka."),
        "type": "chain",
        "title": "इकाई ५६: उपविष्टक-उपशुष्कक का योग",
        "steps": ["तीन मोटी मुर्गियाँ और आढक भर छिलका-रहित उड़द", "दूध-जल के साथ ओखली में कूटना",
                  "उस रस और घी से तीतर (सम्भावित) या कपिञ्जल (विवादित) का रस पकाना",
                  "पिलाना: उपविष्टक और उपशुष्कक की वृद्धि के लिए"],
    },
    ("58", "diagram"): {
        "file": "sh4-payasya-ghrita-58.svg",
        "alt": ("Table of unit 58 in line order: payasyā (identity disputed), the pair of kākolī (disputed), suniṣaṇṇaka "
                "(probably Marsilea), made into a paste; with that paste and with milk, ghee is cooked."),
        "type": "table",
        "title": "इकाई ५८: कल्क और दूध से घी",
        "heads": ["छपा शब्द", "अर्थ"],
        "rows": [["पयस्या", "एक वनस्पति, पहचान विवादित"], ["काकोलीद्वय", "काकोली का जोड़ा, विवादित"],
                 ["सुनिषण्णक", "चौपतिया (सम्भावित)"], ["कल्केन", "इनकी लुगदी से"], ["पयसा च", "और दूध से"],
                 ["सर्पिर्विपचेत्", "घी पकाए"]],
    },
    ("63", "diagram"): {
        "file": "sh4-ghritapatra-63.svg",
        "alt": ("Table of unit 63: the five things in line order with their labels: sesame (standard), mung bean "
                "(standard), black gram (standard), salt, bael leaves (standard); combined with a vessel-full of ghee and "
                "put away, well guarded."),
        "type": "table",
        "title": "इकाई ६३: घृतपात्र और पाँच द्रव्य",
        "heads": ["द्रव्य (क्रम से)", "पहचान"],
        "rows": [["१ तिल", "तिल (मानक)"], ["२ मुद्ग", "मूँग (मानक)"], ["३ माष", "उड़द (मानक)"], ["४ लवण", "नमक"],
                 ["५ बिल्वपत्र", "बेल के पत्ते (मानक)"], ["घृतपात्र", "इन पाँच से मिलाकर सुरक्षित रखवाए"]],
    },
    ("64", "chain"): {
        "file": "sh4-bilvamatra-pinda-64.svg",
        "alt": ("Chain of unit 64: then, in the morning; a lump the size of a bilva (bael); with boiled, cooled goat's milk "
                "as the after-drink; one should eat it."),
        "type": "chain",
        "title": "इकाई ६४: प्रातः पिण्ड",
        "steps": ["ततः, प्रातः (फिर, सुबह)", "बिल्व के आकार का पिण्ड", "अनुपान: उबाला-ठंडा बकरी का दूध",
                  "खाए (प्राश्नीयात्)"],
    },
    ("66", "diagram"): {
        "file": "sh4-avriddhi-66.svg",
        "alt": ("Flowchart of unit 66: when there is no growth, two actions in order: one, purge with sharp ones; two, "
                "cause to fall with placenta-expelling ones."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"अवृद्धि: वृद्धि न हो\"] --> B[\"१ तीक्ष्णों से विरेचन\"]\n"
                 "  A --> C[\"२ अपरापातनीयों से पातन\"]\n"),
    },
    ("67", "diagram"): {
        "file": "sh4-lina-garbha-67.svg",
        "alt": ("Flowchart of unit 67: the channels afflicted by Vāta; the fetus clings; the fetus does not move; this is "
                "called līna."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"स्रोतस वात से ग्रस्त\"] --> B[\"गर्भ संलीन: चिपका\"]\n"
                 "  B --> C[\"गर्भ हिलता नहीं\"]\n"
                 "  C --> D[\"नाम: लीन\"]\n"),
    },
    ("68", "diagram"): {
        "file": "sh4-lina-bhojana-68.svg",
        "alt": ("Two columns of unit 68, what red śāli rice is fed with. Broth of any one of eight, with much ghee: hawk "
                "(probable), osprey (probable), cow, fish, monitor lizard (standard), peacock (standard), fowl, partridge "
                "(probable). Or a soup rich in ghee: of black gram, or of radish (standard)."),
        "type": "split",
        "title": "इकाई ६८: लाल शालि-भात किसके साथ",
        "cols": [["किसी एक का घी-भरा रस",
                  ["१ श्येन: बाज (सम्भावित)", "२ उत्क्रोश: कुरर (सम्भावित)", "३ गो: गाय", "४ मत्स्य: मछली",
                   "५ गोध: गोह (मानक)", "६ शिखी: मोर (मानक)", "७ कुक्कुट: मुर्गा", "८ तित्तिरि: तीतर (सम्भावित)"]],
                 ["या घी-भरपूर यूष", ["माष (उड़द) का यूष", "मूलक (मूली, मानक) का यूष"]]],
    },
}
