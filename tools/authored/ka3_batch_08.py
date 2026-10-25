from helpers import mcq, match, order, fill, multi, accepts

AUTHORED = {}

# ---------------------------------------------------------------- unit 89
AUTHORED["89"] = {
    "title": "तृणमोहभ्रममूर्च्छाद्याः स्युर्जीर्यति च भेषजे",
    "question": "Which signs may arise while the medicine is being digested, and which medicine does verse 89 recommend then?",
    "rule": ("While the medicine is being digested, delusion, giddiness, fainting and the like may arise (thirst too, on a "
             "conjectural reading); then a medicine that is Pitta-destroying, sweet and cool is recommended."),
    "limits": ("Medium confidence. Printed तृण ('grass') is flagged; 'thirst' is a conjecture: no question on it. "
               "No drug is named, only qualities. स्वादु may mean 'pleasant-tasting'; जीर्यति may also mean 'ages'."),
    "explain_hi": ("यह श्लोक औषध के पचते समय की एक व्यापद् बताता है: मोह, भ्रम यानी चक्कर, मूर्च्छा आदि हो सकते हैं। "
                   "समास का पहला सदस्य छपाई में ‘तृण’ (घास) है; ‘तृट्’ यानी प्यास पढ़ना केवल अनुमान है। "
                   "ऐसी अवस्था में औषध पित्तघ्न यानी पित्त को नष्ट करने वाली, स्वादु यानी मीठी और शीतल होनी चाहिए: ‘शस्यते’ = प्रशस्त है। "
                   "कोई द्रव्य नहीं गिनाया गया, केवल गुण। अगला श्लोक (05.03.102-103) इसका उलटा चित्र देता है: कफ के लक्षणों में तीक्ष्ण-उष्ण औषध।"),
    "hook": "दवा पचते समय चक्कर और मूर्च्छा: पित्त बुझाओ, मीठा और ठण्डा दो।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "In verse 89, what kind of medicine is recommended when delusion, giddiness and fainting arise?",
            ("Pitta-destroying, sweet and cool",
             "पित्तघ्नं स्वादुशीतं च भेषजं तत्र शस्यते: Pitta-destroying, sweet and cool."),
            [("Kapha-dispelling, sharp and hot", "That is the remedy of the next verse (05.03.103), for signs of Kapha."),
             ("Fatty and salty, given with dry food", "Fat and salt belong to 05.03.99, not to verse 89."),
             ("Astringent and making the body firm", "Making firm is the remedy for atiyoga (05.03.53), not this verse.")],
            "Verse 89 names three qualities of the medicine: पित्तघ्न, स्वादु, शीत.",
            "Signs while the medicine digests → Pitta-destroying, sweet, cool medicine."),
        match(1, "Match each word of verse 89 to its meaning.",
              [["मोह", "delusion"], ["भ्रम", "giddiness"], ["मूर्च्छा", "fainting"],
               ["पित्तघ्न", "Pitta-destroying"], ["शस्यते", "is recommended"]],
              "Three signs of the first line and two words of the remedy in the second, as the card glosses them.",
              "मोह = delusion; भ्रम = giddiness; मूर्च्छा = fainting; पित्तघ्न = Pitta-destroying; शस्यते = is recommended."),
        order(2, "Put the words of the second line of verse 89 in the order of the text.",
              ["पित्तघ्नं", "स्वादुशीतं", "च", "भेषजं", "तत्र", "शस्यते"],
              "पित्तघ्नं स्वादुशीतं च भेषजं तत्र शस्यते: the qualities first, then the medicine, then 'is recommended'.",
              "पित्तघ्नं · स्वादुशीतं · च · भेषजं · तत्र · शस्यते.",
              role="extend",
              teaches="The remedy line of verse 89 puts the qualities (Pitta-destroying, sweet-cool) before the noun भेषजम् and ends with the passive verb शस्यते."),
        mcq("discriminate", 3,
            "Which split of the printed स्युर्जीर्यति is right?",
            ("स्युः + जीर्यति",
             "A visarga after उ becomes र् before a voiced sound: स्युः + जीर्यति → स्युर्जीर्यति."),
            [("स्यु + र्जीर्यति", "र्जीर्यति is no word; the र् is the changed visarga of स्युः."),
             ("स्युत् + जीर्यति", "त् before ज would give ज्ज: स्युज्जीर्यति."),
             ("स्युम् + जीर्यति", "म् before a consonant would become anusvāra: स्युंजीर्यति.")],
            "स्युः (3 pl. optative of √अस्, 'may be') + जीर्यति (while being digested).",
            "उः before a voiced sound → उर्."),
        mcq("apply", 4,
            "A patient on a cleansing medicine grows giddy and faints. By verse 89, which medicine fits?",
            ("A sweet, cool, Pitta-destroying one",
             "Giddiness and fainting are named in verse 89; its remedy is Pitta-destroying, sweet and cool."),
            [("A sharp, hot, Kapha-dispelling one", "That suits the Kapha signs of 05.03.102-103, not giddiness and fainting."),
             ("A drink of hot water, taken at once", "Hot water is for a held-back doṣa (05.03.90), not for these signs."),
             ("A dry food, given after digestion", "Dry food belongs to 05.03.98, not to verse 89.")],
            "भ्रम and मूर्च्छा → the medicine of verse 89: पित्तघ्न, स्वादु, शीत.",
            "Verse 89: giddiness, fainting → sweet, cool, Pitta-destroying."),
        mcq("transfer", 5,
            "पित्तघ्नम् means 'Pitta-destroying'. By the same pattern, what does an invented कफघ्नम् mean?",
            ("Kapha-destroying",
             "-घ्न at the end of a compound means 'destroying' the first member: कफ + घ्न = Kapha-destroying."),
            [("Made by Kapha", "That would be कफज or कफकृत, not -घ्न."),
             ("Kapha-increasing", "Increasing is -वर्धन; -घ्न destroys."),
             ("Destroyed by Kapha", "-घ्न is active: it destroys, it is not destroyed.")],
            "Same pattern as पित्तघ्नम्: X-घ्न = X-destroying.",
            "X + घ्न → 'X-destroying'.",
            teaches="-घ्न (from √हन्) at the end of a compound means 'destroying' the first member: पित्तघ्न, कफघ्न."),
    ],
}

# ---------------------------------------------------------------- unit 90
AUTHORED["90"] = {
    "title": "लालाहल्लासविष्टंभरोमहर्षात्कफावृते",
    "question": "From which signs is the medicine known to be enveloped by Kapha, and which medicine does verse 90 then give?",
    "rule": ("From salivation, nausea, obstruction (viṣṭambha) and horripilation, when (it is) enveloped by Kapha, the medicine "
             "there is sharp and hot, pungent and the rest, Kapha-dispelling, beneficial."),
    "limits": ("Medium confidence. Printed हल्लास (for हृल्लास, nausea) and कद्वादि (for कट्वादि, pungent and the rest) are flagged: "
               "no question on those two members. The ablative is read as the signs by which the Kapha covering is known. "
               "No verb is printed; कट्वादि may also name a drug group."),
    "explain_hi": ("यहाँ कफ से ढके औषध की पहचान और उपाय है। लालास्राव, हृल्लास यानी मिचली, विष्टम्भ यानी रुकावट और रोमहर्ष यानी रोंगटे खड़े होना: "
                   "इन लक्षणों से जाना जाता है कि (औषध) कफ से आवृत है। तब औषध तीक्ष्ण और उष्ण, कटु आदि, कफनुत् यानी कफ को हटाने वाली और हितकर हो। "
                   "वाक्य में क्रिया नहीं छपी। ‘हल्लास’ और ‘कद्वादि’ छपाई में संदिग्ध हैं। "
                   "पिछले श्लोक (05.03.100-101) की मीठी-ठण्डी पित्तघ्न औषध से यह ठीक उलटी है।"),
    "hook": "मुँह में लार, रोंगटे खड़े: कफ ने ढका, तो तीखी-गरम कफनाशक दवा।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "In verse 90, by what is (the medicine) enveloped when salivation and horripilation appear?",
            ("By Kapha", "कफावृते: when enveloped by Kapha."),
            [("By Pitta", "Pitta belongs to verse 89's remedy (पित्तघ्न), not to this covering."),
             ("By Vāta", "Vāta is not named in verse 90."),
             ("By blood", "Blood is not named in verse 90.")],
            "कफ + आवृते: enveloped by Kapha.",
            "Verse 90: लाला, रोमहर्ष … → कफावृते."),
        match(1, "Match each word of verse 90 to its meaning.",
              [["लाला", "salivation"], ["विष्टम्भ", "obstruction"], ["रोमहर्ष", "horripilation"],
               ["तीक्ष्णोष्ण", "sharp and hot"], ["कफनुत्", "Kapha-dispelling"]],
              "Three signs and two qualities of the medicine, as the card glosses them.",
              "लाला = salivation; विष्टम्भ = obstruction; रोमहर्ष = horripilation; तीक्ष्णोष्ण = sharp and hot; कफनुत् = Kapha-dispelling."),
        order(2, "Put these words of verse 90 in the order of the text.",
              ["लाला", "विष्टंभ", "रोमहर्ष", "कफावृते", "तीक्ष्णोष्णं", "कफनुत्"],
              "The signs (लाला … विष्टंभ, रोमहर्ष), the cause (कफावृते), then the medicine: तीक्ष्णोष्णं … कफनुत्.",
              "Signs · Kapha covering · sharp-hot · Kapha-dispelling.",
              role="extend",
              teaches="Verse 90 runs signs → Kapha covering → qualities of the medicine, with the Kapha-dispelling quality near the end."),
        mcq("discriminate", 3,
            "Which split of the printed तीक्ष्णोष्णं is right?",
            ("तीक्ष्ण + उष्णम्",
             "अ + उ → ओ: तीक्ष्ण + उष्णम् → तीक्ष्णोष्णम्."),
            [("तीक्ष्णो + ष्णम्", "ष्णम् is no word; the ओ comes from अ + उ."),
             ("तीक्ष्णः + उष्णम्", "अः before a vowel other than अ loses its visarga: तीक्ष्ण उष्णम्, two words."),
             ("तीक्ष्ण + ओष्णम्", "अ + ओ would give औ: तीक्ष्णौष्णम्.")],
            "तीक्ष्ण (sharp) + उष्णम् (hot): the guṇa join अ + उ → ओ.",
            "अ + उ → ओ."),
        mcq("apply", 4,
            "After the medicine, a patient drools and his hair stands on end. Which medicine does verse 90 support?",
            ("Sharp, hot and Kapha-dispelling",
             "Salivation and horripilation show Kapha covering: the medicine is तीक्ष्णोष्ण, कफनुत्."),
            [("Sweet, cool and Pitta-destroying", "That is verse 89's remedy, for delusion, giddiness and fainting."),
             ("Cold, astringent and making firm", "Making firm is for atiyoga (05.03.53), not for Kapha covering."),
             ("Fatty, salty and drunk once more", "Fat and salt are for medicine held by Vāta (05.03.99).")],
            "लाला and रोमहर्ष → कफावृत → तीक्ष्ण, उष्ण, कफनुत् medicine.",
            "Kapha signs → sharp, hot, Kapha-dispelling medicine."),
        mcq("transfer", 5,
            "कफनुत् + हितम् gives कफनुद्धितम्. Join the invented pair वातनुत् + हितम् (Vāta-dispelling, beneficial) the same way. Which is right?",
            ("वातनुद्धितम्",
             "त् + ह → द्ध: वातनुत् + हितम् = वातनुद्धितम्, like कफनुद्धितम्."),
            [("वातनुत्हितम्", "त् cannot stand unchanged before ह; it becomes द् (and here ह becomes ध)."),
             ("वातनुत्धितम्", "The त् cannot stay voiceless before a voiced sound; it must become द्, giving द्ध."),
             ("वातनुधितम्", "The द् of the join cannot vanish; the form needs द्ध.")],
            "Same join as कफनुत् + हितम् → कफनुद्धितम्.",
            "त् + ह → द्ध.",
            teaches="A final त् before ह becomes द्, and the ह may become ध (as printed here): कफनुत् + हितम् → कफनुद्धितम्; वातनुत् + हितम् → वातनुद्धितम्."),
    ],
}

# ---------------------------------------------------------------- unit 91
AUTHORED["91"] = {
    "title": "प्रतिकूला गतिः पायोर्ग्रथितत्वं",
    "question": "Which complications open the closing list in verse 91?",
    "rule": ("A list without a verb: contrary movement (gati; of the anus, as the data reads पायोः), knottedness with heaviness, "
             "stirring up of the doṣa, severe distension (ādhmāna), cutting pain (parikarta), discharge (parisrava)."),
    "limits": ("Medium confidence. पायोः (of the anus) is taken with गतिः; it may go with ग्रथितत्वम्, and what is knotted "
               "is not said: no question on that link. The list runs on into verse 92; the twelve are not numbered."),
    "explain_hi": ("अध्याय के अन्त में व्यापदों की सूची शुरू होती है। इस श्लोक में: प्रतिकूल गति, ग्रथितत्व यानी गाँठदार होना भारीपन सहित, "
                   "दोष का उत्क्लेश, अत्यधिक आध्मान यानी पेट फूलना, परिकर्त यानी काटने जैसी पीड़ा, और परिस्रव यानी बहना। "
                   "क्रिया नहीं है; सूची अगले श्लोक (05.03.106-107) में पूरी होती है। "
                   "इनमें से कई नाम अध्याय में पहले आ चुके हैं, जैसे आध्मान 05.03.20-22 में और परिस्रव 05.03.33-36 में। "
                   "‘पायोः’ (गुदा का) गति से जुड़े या ग्रथितत्व से, यह दो-तरफ़ा है।"),
    "hook": "उलटी चाल, गाँठ और भार, दोष हिला, पेट फूला, काट और बहाव: सूची का पहला भाग।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "In verse 91, which complication is called 'severe' (भृश)?",
            ("Distension (ādhmāna)",
             "भृशाध्मानम्: severe distension."),
            [("Discharge (parisrava)", "परिस्रवः stands without भृश."),
             ("Cutting pain (parikarta)", "परिकर्तः stands without भृश."),
             ("Heaviness (gaurava)", "Heaviness comes as स-गौरवम्, 'with heaviness', not भृश.")],
            "भृश + आध्मानम् = severe distension.",
            "भृश qualifies आध्मान in verse 91."),
        match(1, "Match each word of verse 91 to its meaning.",
              [["गौरव", "heaviness"], ["उत्क्लेश", "stirring up"], ["आध्मान", "distension"],
               ["परिकर्त", "cutting pain"], ["परिस्रव", "discharge"]],
              "Five items of the list, as the card glosses them.",
              "गौरव = heaviness; उत्क्लेश = stirring up; आध्मान = distension; परिकर्त = cutting pain; परिस्रव = discharge."),
        order(2, "Put these complications of verse 91 in the order of the text.",
              ["प्रतिकूला गतिः", "ग्रथितत्वं", "दोषोत्क्लेशः", "भृशाध्मानं", "परिकर्तः", "परिस्रवः"],
              "Line 1: contrary movement, knottedness (with heaviness). Line 2: stirring up of the doṣa, severe distension, cutting pain, discharge.",
              "गति · ग्रथितत्व · उत्क्लेश · आध्मान · परिकर्त · परिस्रव.",
              role="extend",
              teaches="Verse 91 lists, in order: contrary movement, knottedness with heaviness, stirring up of the doṣa, severe distension, cutting pain, discharge."),
        mcq("discriminate", 3,
            "Which split of the printed पायोर्ग्रथितत्वं is right?",
            ("पायोः + ग्रथितत्वम्",
             "A visarga after ओ becomes र् before a voiced sound: पायोः + ग्रथितत्वम् → पायोर्ग्रथितत्वम्."),
            [("पायो + र्ग्रथितत्वम्", "र्ग्रथितत्वम् is no word; the र् is the changed visarga of पायोः."),
             ("पायुः + ग्रथितत्वम्", "That would print पायुर्ग्रथितत्वम्; the text has ओ, the genitive पायोः."),
             ("पायोत् + ग्रथितत्वम्", "त् before ग would give द्: पायोद्ग्रथितत्वम्.")],
            "पायोः (genitive of पायु, anus) + ग्रथितत्वम् (knottedness).",
            "ओः before a voiced sound → ओर्."),
        mcq("apply", 4,
            "After purgation, a patient feels a cutting pain. Which item of verse 91 names this?",
            ("परिकर्तः", "परिकर्त is glossed cutting pain."),
            [("परिस्रवः", "परिस्रव is discharge, a flowing out."),
             ("दोषोत्क्लेशः", "उत्क्लेश is stirring up of the doṣa."),
             ("ग्रथितत्वम्", "ग्रथितत्व is knottedness.")],
            "Cutting pain = परिकर्तः, an item of verse 91.",
            "परिकर्त = cutting pain."),
        mcq("transfer", 5,
            "सगौरवम् means 'with heaviness'. By the same pattern, what does an invented सशूलम् mean?",
            ("With pain",
             "स- at the head of a bahuvrīhi means 'with': स + शूल = with pain."),
            [("Without pain", "'Without' would be निः- or अ-: निःशूल, अशूल."),
             ("Pain alone", "स- adds 'with'; it does not mean 'only'."),
             ("After the pain", "स- is not a word of time.")],
            "Same pattern as सगौरवम्: स + X = with X.",
            "स- + noun → 'with' that noun.",
            teaches="स- at the head of a bahuvrīhi means 'together with': सगौरव = with heaviness, सशूल = with pain."),
    ],
}

# ---------------------------------------------------------------- unit 92
AUTHORED["92"] = {
    "title": "प्रवाहिकाहृद्ग्रहणं सर्वांगपरिग्रहः",
    "question": "Which complications close the list in verse 92, and how does the verse sum them up?",
    "rule": ("Pravāhikā (probably dysentery), seizing of the heart, gripping of the whole body, together with the flow of all "
             "the dhātus: these twelve are stated with their remedies (sasādhana)."),
    "limits": ("Medium confidence. हृद् may be 'heart' or 'chest'. The instrumental सर्वधातुस्रवेण is read 'together with', counting "
               "the flow of the dhātus in the twelve. The text does not number the twelve one by one here; the remedies are those given "
               "earlier in the chapter."),
    "explain_hi": ("यह श्लोक सूची पूरी करता है: प्रवाहिका यानी सम्भवतः पेचिश (बार-बार ज़ोर लगाकर पतला मल), हृद्ग्रहण यानी हृदय (या छाती) का जकड़ना, "
                   "सर्वाङ्गपरिग्रह यानी सारे शरीर का जकड़ जाना, और सर्वधातुस्रव यानी सब धातुओं का बहना। "
                   "फिर समेटता है: ये बारह (व्यापदें) उनके साधनों यानी उपायों सहित कही गई हैं। "
                   "उपाय इसी अध्याय में पहले आ चुके हैं; जैसे प्रवाहिका 05.03.39-41 में और धातुओं का बहना 05.03.52-53 में। "
                   "बारह की गिनती पाठ यहाँ एक-एक करके नहीं करता।"),
    "hook": "पेचिश, दिल की जकड़, पूरा शरीर जकड़ा, सब धातु बहे: ये बारह, उपाय सहित कही गईं।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "In verse 92, together with what are the twelve said to be stated?",
            ("With their remedies (sādhana)",
             "ससाधनाः: with their remedies."),
            [("With the doṣas that cause them", "No doṣa is named in the summing-up; स-साधन = with remedy."),
             ("With their causes (nidāna)", "Causes are not the word here; साधन means remedy."),
             ("With their signs (liṅga)", "Signs are not the word here; साधन means remedy.")],
            "द्वादशोक्ताः ससाधनाः: twelve are stated, with their remedies.",
            "ससाधन = with remedies."),
        match(1, "Match each item of verse 92 to its meaning.",
              [["प्रवाहिका", "dysentery with straining (probable)"], ["हृद्ग्रहण", "seizing of the heart"],
               ["सर्वाङ्गपरिग्रह", "gripping of the whole body"], ["सर्वधातुस्रव", "flow of all the dhātus"],
               ["ससाधन", "with remedies"]],
              "The four complications of the verse and its closing word.",
              "प्रवाहिका = dysentery (probable); हृद्ग्रहण = seizing of the heart; सर्वाङ्गपरिग्रह = whole-body gripping; सर्वधातुस्रव = flow of all dhātus; ससाधन = with remedies."),
        order(2, "Put these parts of verse 92 in the order of the text.",
              ["प्रवाहिका", "हृद्ग्रहणं", "सर्वांगपरिग्रहः", "सर्वधातुस्रवेण", "द्वादशोक्ताः ससाधनाः"],
              "Three complications, the flow of all dhātus, then the summing-up: twelve stated with remedies.",
              "प्रवाहिका · हृद्ग्रहण · सर्वाङ्गपरिग्रह · सर्वधातुस्रव · द्वादश उक्ताः ससाधनाः.",
              role="extend",
              teaches="Verse 92 ends the list with pravāhikā, seizing of the heart, gripping of the whole body and the flow of all dhātus, then sums up: twelve, with remedies."),
        mcq("discriminate", 3,
            "Which split of the printed सर्वधातुस्रवेणैता is right?",
            ("स्रवेण + एताः",
             "अ + ए → ऐ: स्रवेण + एताः → स्रवेणैता; the visarga of एताः drops before the voiced द of द्वादश."),
            [("स्रवेणा + इताः", "आ + इ would give ए (स्रवेणेता), not ऐ."),
             ("स्रवेण + इताः", "अ + इ gives ए, not ऐ."),
             ("स्रवेणै + ताः", "There is no form स्रवेणै; the ऐ is the join of अ and ए.")],
            "सर्वधातुस्रवेण (with the flow of all dhātus) + एताः (these): vṛddhi join अ + ए → ऐ.",
            "अ + ए → ऐ."),
        mcq("apply", 4,
            "After purgation, a patient strains often and passes loose stools. Which item of verse 92 fits?",
            ("प्रवाहिका",
             "Pravāhikā: straining with frequent loose stools, probably dysentery."),
            [("हृद्ग्रहणम्", "That is seizing of the heart, not straining at stool."),
             ("सर्वाङ्गपरिग्रहः", "That is gripping of the whole body."),
             ("सर्वधातुस्रवः", "That is the flow of all the dhātus, not straining with loose stools.")],
            "Straining with frequent loose stools = प्रवाहिका (probably dysentery).",
            "प्रवाहिका = straining, loose stools."),
        mcq("transfer", 5,
            "द्वादश + उक्ताः gives द्वादशोक्ताः. Which is the right join of the invented pair दश + उक्ताः (ten are stated)?",
            ("दशोक्ताः",
             "अ + उ → ओ: दश + उक्ताः = दशोक्ताः, like द्वादशोक्ताः."),
            [("दशाक्ताः", "अ + उ does not give आ."),
             ("दशौक्ताः", "औ comes from अ + ओ or अ + औ, not अ + उ."),
             ("दशुक्ताः", "The अ cannot simply drop before उ.")],
            "Same guṇa join as द्वादशोक्ताः.",
            "अ + उ → ओ.",
            teaches="Final अ + initial उ → ओ: द्वादश + उक्ताः → द्वादशोक्ताः; दश + उक्ताः → दशोक्ताः."),
    ],
}

# ---------------------------------------------------------------- unit 93
AUTHORED["93"] = {
    "title": "व्यापदो योगविभ्रंशात्",
    "question": "From what, according to unit 93, do complications (vyāpad) arise, even in purgation?",
    "rule": "Complications (vyāpad) arise from a lapse in the application (yoga), even in purgation of various kinds; the sentence runs on into the next verse.",
    "limits": ("High confidence, but no verb: the sentence continues in 05.03.109-110. योग may also mean 'combination (of the drug)'. "
               "A reviewer point is OPEN on विविधे ('of various kinds') against a possible द्विविधे ('twofold'): no question on that word's meaning."),
    "explain_hi": ("यह गद्य-पंक्ति समापन-श्लोक की भूमिका है। व्यापदें यानी उपद्रव योग के विभ्रंश से, यानी प्रयोग में चूक से, होती हैं; "
                   "विविध प्रकार के विरेचन में भी। ‘योग’ का दूसरा अर्थ ‘द्रव्यों का मेल’ भी हो सकता है। "
                   "वाक्य यहाँ पूरा नहीं होता; क्या करना है, यह अगले श्लोक (05.03.109-110) में है। "
                   "‘विविधे’ की जगह ‘द्विविधे’ (दो प्रकार का) पाठ भी सम्भव है; यह खुला प्रश्न है।"),
    "hook": "प्रयोग में चूक, तो व्यापद्: विरेचन भी अछूता नहीं।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "From what, according to unit 93, do the complications (vyāpad) arise?",
            ("From a lapse in the application",
             "योगविभ्रंशात्: from a slip, a lapse, in the application (yoga)."),
            [("From the patient's weak digestion", "Digestion is not named in unit 93."),
             ("From giving it in a cold season", "No season is named in unit 93."),
             ("From too little prior oiling", "Oiling is not named in unit 93.")],
            "योग (application) + विभ्रंशात् (from a lapse), in the ablative of cause.",
            "Unit 93: व्यापदः … योगविभ्रंशात्."),
        match(1, "Match each word of unit 93 to its meaning.",
              [["व्यापद्", "complication"], ["योग", "application"], ["विभ्रंश", "lapse, slip"], ["विरेचन", "purgation"]],
              "The four key words of the line, as the card glosses them.",
              "व्यापद् = complication; योग = application; विभ्रंश = lapse; विरेचन = purgation."),
        order(2, "Put the words of unit 93 in the order of the text.",
              ["व्यापदः", "योगविभ्रंशात्", "विविधेऽपि", "विरेचने"],
              "व्यापदो योगविभ्रंशाद्विविधेऽपि विरेचने: complications, from a lapse in application, even in various, purgation.",
              "व्यापदः · योगविभ्रंशात् · विविधेऽपि · विरेचने.",
              role="extend",
              teaches="Unit 93 names the result first (व्यापदः), then its cause in the ablative (योगविभ्रंशात्), then where it happens (विरेचने)."),
        mcq("discriminate", 3,
            "The printed व्यापदो योग… stands for which form before योग?",
            ("व्यापदः",
             "अः before a voiced sound becomes ओ: व्यापदः + योग… → व्यापदो योग…."),
            [("व्यापदा", "आ would stay आ before य: व्यापदा योग…."),
             ("व्यापदम्", "म् before य would become anusvāra: व्यापदं योग…."),
             ("व्यापदौ", "औ stays औ before a consonant: व्यापदौ योग….")],
            "व्यापदः, nominative plural: the visarga with अ becomes ओ before the voiced य.",
            "अः before a voiced consonant → ओ."),
        fill(4, "Unit 93: ____ (complications) arise from a lapse in the application. Type it in Devanagari or in English letters (e.g. dharma).",
             accepts("व्यापदः", "vyāpadaḥ", "व्यापद्", "व्यापदो", "vyāpad", "vyapado"),
             "व्यापदः (nom. pl. of व्यापद्), printed व्यापदो before योग.",
             "Unit 93 names the complications of cleansing व्यापद् and traces them to a lapse in the application.",
             "व्यापद् = complication.", role="apply"),
        mcq("transfer", 5,
            "योगविभ्रंशात् is ablative: from a lapse. Which invented form of अतियोग (excess) means from excess?",
            ("अतियोगात्",
             "-आत् is the ablative of an अ-stem: 'from'. अतियोग → अतियोगात्, like विभ्रंश → विभ्रंशात्."),
            [("अतियोगे", "-ए is the locative: 'in excess'."),
             ("अतियोगेन", "-एन is the instrumental: 'by excess'."),
             ("अतियोगस्य", "-स्य is the genitive: 'of excess'.")],
            "Ablative singular of अ-stems in -आत् marks the cause, 'from'.",
            "अ-stem + आत् → 'from'.",
            teaches="The ablative singular of an अ-stem ends in -आत् and can mark the cause: योगविभ्रंशात् 'from a lapse', अतियोगात् 'from excess'."),
    ],
}

# ---------------------------------------------------------------- unit 94
AUTHORED["94"] = {
    "title": "उत्पद्यमानासु च तासु तासु",
    "question": "What should the physician do in each complication of cleansing, and what reason does verse 94 give?",
    "rule": ("In each complication arising through a deviation in cleansing, he should strive quickly for the cure by this very "
             "direction; for the śāstra is the light of sound and unsound conduct (naya, durnaya)."),
    "limits": ("High confidence. 'This direction' is the guidance of the chapter; the verse names no single remedy. The sentence "
               "begins in 05.03.108. नय and दुर्नय are glossed 'right and wrong policy or method'; the verse does not list them."),
    "explain_hi": ("अध्याय का समापन-श्लोक। संशोधन (वमन-विरेचन) के विभ्रम से जो-जो व्यापदें उत्पन्न हों, उनमें इसी दिशा से, यानी इस अध्याय के निर्देश से, "
                   "शीघ्र सिद्धि के लिए प्रयत्न करे। कारण: शास्त्र नय और दुर्नय, यानी सही और गलत मार्ग, का ज्योति यानी प्रकाश है। "
                   "‘तासु तासु’ = उन-उन, यानी हर एक में। वाक्य 05.03.108 से चलता आया है। "
                   "छन्द ग्यारह अक्षरों का है, अनुष्टुप् नहीं।"),
    "hook": "हर व्यापद् में इसी राह से जल्दी इलाज: शास्त्र सही-गलत का दीया है।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "What does verse 94 call the śāstra?",
            ("The light of sound and unsound conduct",
             "ज्योतिर्हि शास्त्रं नयदुर्नयानाम्: the śāstra is the light of naya and durnaya."),
            [("The root of every remedy for the twelve", "No 'root' is named; the image is ज्योतिः, light."),
             ("A wall that keeps back every complication", "No wall is named; the image is light."),
             ("The memory of the earlier physicians", "Earlier physicians are not named; the image is light.")],
            "ज्योतिः = light; नय-दुर्नय = sound and unsound conduct.",
            "Verse 94: शास्त्रं ज्योतिः नयदुर्नयानाम्."),
        match(1, "Match each word of verse 94 to its meaning.",
              [["उत्पद्यमान", "arising"], ["दिशा", "by the direction"], ["आशु", "quickly"],
               ["सिद्धि", "cure"], ["ज्योतिः", "light"]],
              "Five key words of the verse, as the card glosses them.",
              "उत्पद्यमान = arising; दिशा = by the direction; आशु = quickly; सिद्धि = cure; ज्योतिः = light."),
        order(2, "Put these parts of verse 94 in the order of the text.",
              ["उत्पद्यमानासु च", "तासु तासु व्यापत्सु", "संशोधनविभ्रमेण", "दिशाऽनयैवाशु", "यतेत सिद्धौ", "ज्योतिर्हि शास्त्रं नयदुर्नयानां"],
              "Arising complications, through a deviation in cleansing; by this direction, quickly; strive for cure; for the śāstra is the light.",
              "उत्पद्यमानासु · तासु तासु व्यापत्सु · संशोधनविभ्रमेण · दिशाऽनयैवाशु · यतेत सिद्धौ · ज्योतिर्हि शास्त्रम्.",
              role="extend",
              teaches="Verse 94 sets the situation (complications arising from a deviation in cleansing), gives the command (strive quickly by this direction) and ends with the reason (हि: the śāstra is light)."),
        mcq("discriminate", 3,
            "Which split of the printed ज्योतिर्हि is right?",
            ("ज्योतिः + हि",
             "A visarga after इ becomes र् before a voiced sound: ज्योतिः + हि → ज्योतिर्हि."),
            [("ज्योति + र्हि", "र्हि is no word; the र् is the changed visarga of ज्योतिः."),
             ("ज्योतीः + हि", "A long ई would print ज्योतीर्हि; the text has short इ."),
             ("ज्योतिम् + हि", "म् before ह would become anusvāra: ज्योतिंहि.")],
            "ज्योतिः (light, n. nom. sg.) + हि (for): इः before a voiced sound → इर्.",
            "इः before a voiced sound → इर्."),
        mcq("apply", 4,
            "A complication arises from a deviation in cleansing. What does verse 94 tell the physician to do?",
            ("Strive quickly for cure by this direction",
             "दिशाऽनयैवाशु यतेत सिद्धौ: by this very direction he should quickly strive for the cure."),
            [("Stop all cleansing and wait for a season", "Verse 94 asks for quick effort, not waiting."),
             ("Give the same medicine again in double dose", "No dose is named; the guidance is 'this direction'."),
             ("Send the patient to another physician", "Verse 94 tells the physician himself to strive.")],
            "Situation: complications from a deviation in cleansing. Command: यतेत सिद्धौ, quickly, by this direction.",
            "Verse 94: आशु यतेत सिद्धौ."),
        mcq("transfer", 5,
            "दुर्- turns नय 'sound conduct' into दुर्नय 'unsound conduct'. By the same pattern, what does दुर्जन mean?",
            ("A bad person",
             "दुर्- means 'bad, ill': दुर् + जन = a bad person, as दुर् + नय = unsound conduct."),
            [("A good person", "'Good' would be सत्- or सु-: सज्जन."),
             ("Many people", "दुर्- marks badness, not number."),
             ("No person", "'No' would be अ- or निः-, not दुर्-.")],
            "Same prefix as दुर्नय: दुर्- = bad.",
            "दुर्- + noun → a bad (one).",
            teaches="The prefix दुर्- means 'bad, ill': नय → दुर्नय (unsound conduct), जन → दुर्जन (a bad person)."),
    ],
}

# ---------------------------------------------------------------- unit 95
AUTHORED["95"] = {
    "title": "इति वमनविरेचनव्यापत्सिद्धिर्नाम तृतीयोऽध्यायः",
    "question": "Which chapter does unit 95 close, and what does its name mean?",
    "rule": ("Thus the third chapter, named Vamana-virecana-vyāpat-siddhi: the cure of the complications of emesis and purgation. "
             "It closes Kalpasthāna chapter 3."),
    "limits": "A closing formula: it adds no complication or remedy. The opening || is a printed mark.",
    "explain_hi": ("यह तीसरे अध्याय की पुष्पिका है। नाम चार शब्दों से बना है: वमन, विरेचन, व्यापत् यानी उपद्रव, और सिद्धि यानी चिकित्सा। "
                   "अर्थ: वमन और विरेचन की व्यापदों की सिद्धि। "
                   "अध्याय की पहली पंक्ति (05.03.1) में यही नाम था: ‘वमनविरेचनव्यापत्सिद्धिं व्याख्यास्यामः’, अब वह व्याख्या पूरी हुई। "
                   "‘तृतीयः’ बताता है कि यह कल्पस्थान का तीसरा अध्याय है।"),
    "hook": "इति: वमन-विरेचन की व्यापदों का इलाज, तीसरा अध्याय पूरा।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "What is the name of the chapter closed by unit 95?",
            ("वमनविरेचनव्यापत्सिद्धि",
             "वमनविरेचनव्यापत्सिद्धिर्नाम: named the cure of the complications of emesis and purgation."),
            [("बस्तिव्यापत्सिद्धि", "Basti (enema) is not in this chapter's name."),
             ("वमनकल्प", "That is the name of the first chapter of Kalpasthāna."),
             ("नेत्रबस्तिव्यापत्सिद्धि-अध्याय", "No नेत्र or बस्ति is in this chapter's name.")],
            "The colophon names the chapter after its subject: the cure of vyāpad in vamana and virecana.",
            "वमन + विरेचन + व्यापत् + सिद्धि."),
        match(1, "Match each word of unit 95 to its meaning.",
              [["वमन", "emesis"], ["विरेचन", "purgation"], ["व्यापत्", "complication"], ["सिद्धि", "cure"], ["तृतीय", "third"]],
              "The four members of the chapter's name and its number.",
              "वमन = emesis; विरेचन = purgation; व्यापत् = complication; सिद्धि = cure; तृतीय = third."),
        order(2, "Put the members of the chapter's name in the order of the text.",
              ["वमन", "विरेचन", "व्यापत्", "सिद्धि"],
              "वमन-विरेचन-व्यापत्-सिद्धि: emesis, purgation, complication, cure.",
              "वमन · विरेचन · व्यापत् · सिद्धि.",
              role="extend",
              teaches="The chapter's name is read from the end: the cure (सिद्धि) of the complications (व्यापत्) of emesis and purgation."),
        mcq("discriminate", 3,
            "Which split of the printed सिद्धिर्नाम is right?",
            ("सिद्धिः + नाम",
             "A visarga after इ becomes र् before the voiced न: सिद्धिः + नाम → सिद्धिर्नाम."),
            [("सिद्धि + र्नाम", "र्नाम is no word; the र् is the changed visarga of सिद्धिः."),
             ("सिद्धिम् + नाम", "म् before न would become anusvāra: सिद्धिंनाम."),
             ("सिद्धिः + अनाम", "That would print सिद्धिरनाम, with an अ after र्.")],
            "सिद्धिः (nom. sg.) + नाम (named).",
            "इः before a voiced sound → इर्."),
        mcq("apply", 4,
            "The chapter's first line (05.03.1) promised to explain this same title. What does unit 95 mark?",
            ("That the promised explanation is complete",
             "इति … अध्यायः: thus (ends) the chapter that 05.03.1 announced."),
            [("A fresh list of the twelve complications", "The list was in 05.03.104-107; the colophon adds nothing."),
             ("A new remedy for vyāpad in enemas (basti)", "No remedy is given in a colophon."),
             ("The name of the fourth chapter to follow", "It names this, the third, chapter.")],
            "Opening line: व्याख्यास्यामः (we shall explain). Colophon: इति (thus), the chapter is done.",
            "A colophon closes the chapter its opening line announced."),
        mcq("transfer", 5,
            "तृतीयोऽध्यायः means the third chapter. Which invented form means the fourth chapter?",
            ("चतुर्थोऽध्यायः",
             "चतुर्थः (fourth) + अध्यायः: अः + अ → ओऽ, as in तृतीयोऽध्यायः."),
            [("चत्वारोऽध्यायाः", "That is plural: four chapters."),
             ("चतुर्थेऽध्याये", "That is locative: in the fourth chapter."),
             ("चतुर्धाध्यायः", "चतुर्धा means fourfold, not fourth.")],
            "Ordinal + अध्यायः, joined by अः + अ → ओऽ.",
            "Ordinal -अः + अध्यायः → -ओऽध्यायः.",
            teaches="Ordinals in -अः join अध्यायः as -ओऽध्यायः: तृतीयोऽध्यायः (third chapter), चतुर्थोऽध्यायः (fourth chapter)."),
    ],
}


NOTES_HI = {
    "89": ("विश्वास: मध्यम। text_flag: छपा ‘तृणमोह…’ में ‘तृण’ (घास) उचित नहीं; ‘तृण्’ (तृट्, प्यास) अपेक्षित, जैसे 05.03.77 के ‘तृण्मूर्च्छा’ में। "
           "flag केवल इस पहले सदस्य पर है; मोह, भ्रम, मूर्च्छा स्पष्ट हैं, ‘प्यास’ पर कोई प्रश्न नहीं। "
           "खुला समीक्षा-बिन्दु (05.03.100): ‘जीर्यति’ का अनुवाद ‘पचते समय’; ‘पुराना होना’ अर्थ भी सम्भव (शब्द-सूची में जीर्ण के दो अर्थ); इस पर प्रश्न नहीं। "
           "‘च’ वाला अंश (और औषध के पचते समय) एक अधूरा-सा सति-सप्तमी खण्ड है। स्वादु = मीठा, या ‘स्वादिष्ट’। "
           "संधि जाँची: स्युर्जीर्यति = स्युः + जीर्यति (उः → उर् घोष से पहले); मूर्च्छाद्याः = मूर्च्छा + आद्याः (आ + आ → आ)।"),
    "90": ("विश्वास: मध्यम। दो text_flag: (१) ‘हल्लास’ सम्भवतः ‘हृल्लास’ (मिचली) की भिन्न वर्तनी; (२) ‘कद्वादि’ में ‘कद्’ कोई शब्द नहीं, ‘कट्वादि’ "
           "(कटु आदि) अपेक्षित। इन दोनों सदस्यों पर प्रश्न नहीं; लाला, विष्टम्भ, रोमहर्ष, तीक्ष्णोष्ण, कफनुत् स्पष्ट हैं। "
           "पञ्चमी (…हर्षात्) को ‘इन लक्षणों से पहचान’ पढ़ा गया; कर्ता (औषध) अनुक्त। वाक्य बिना क्रिया का। ‘कट्वादि’ किसी द्रव्य-गण का नाम भी हो सकता है। "
           "संधि जाँची: कफावृते = कफ + आवृते (अ + आ → आ); तीक्ष्णोष्णम् = तीक्ष्ण + उष्णम् (अ + उ → ओ); "
           "कफनुद्धितम् = कफनुत् + हितम् (त् + ह → द्ध)।"),
    "91": ("विश्वास: मध्यम। सूची, क्रिया नहीं; अगले श्लोक में चलती है। डेटा ‘पायोः’ को ‘गतिः’ से जोड़ता है (गुदा की विपरीत गति); छपाई में "
           "‘पायोर्ग्रथितत्वं’ जुड़ा है, इसलिए ‘गुदा का ग्रथितत्व’ भी पढ़ा जा सकता है; क्या गाँठदार है, नहीं कहा। इस जोड़ पर प्रश्न नहीं। "
           "छपा ‘परिकर्त्तः’ = परिकर्तः (दोहरा त्त छपाई का)। "
           "संधि जाँची: पायोर्ग्रथितत्वम् = पायोः + ग्रथितत्वम् (ओः → ओर् घोष से पहले); दोषोत्क्लेशो = दोष + उत्क्लेशः, विसर्ग → ओ घोष भ से पहले; "
           "भृशाध्मानम् = भृश + आध्मानम्।"),
    "92": ("विश्वास: मध्यम। प्रवाहिका = पेचिश (सम्भावित)। हृद् = हृदय या छाती। तृतीया ‘सर्वधातुस्रवेण’ को ‘के साथ’ पढ़ा, यानी धातु-स्राव भी बारह में गिना; "
           "बारह की गिनती पाठ यहाँ नहीं देता, इसलिए गिनती पर प्रश्न नहीं। "
           "संधि जाँची: स्रवेणैता = स्रवेण + एताः (अ + ए → ऐ); ‘एता’ में विसर्ग का लोप नियमित है (आः घोष द से पहले → आ); "
           "द्वादशोक्ताः = द्वादश + उक्ताः (अ + उ → ओ); सर्वांग = सर्व + अङ्ग (अ + अ → आ)।"),
    "93": ("विश्वास: उच्च। यह और अगले श्लोक की दोनों पंक्तियाँ एक वाक्य हैं; यहाँ क्रिया नहीं। योग = प्रयोग, या ‘द्रव्यों का मेल’; विभ्रंश = चूक, फिसलन। "
           "खुला समीक्षा-बिन्दु (05.03.108): ‘विविधे’ की जगह ‘द्विविधे’ (दो प्रकार का, ऊर्ध्व और अधः; 05.03.81 का उभयतोभाग देखें) सम्भव; छपा पाठ रखा गया, "
           "इस पर प्रश्न नहीं। संधि जाँची: व्यापदो योग = व्यापदः + योग (अः → ओ घोष से पहले); विभ्रंशाद्विविधे = विभ्रंशात् + विविधे (त् → द् घोष से पहले); "
           "विविधेऽपि = विविधे + अपि (ए + अ → एऽ)।"),
    "94": ("विश्वास: उच्च। छन्द ग्यारह अक्षरों का (उपजाति प्रकार का), अनुष्टुप् नहीं। तासु तासु = उन-उन, हर एक में। छपा ‘ऽनयैवाशु’ = अनया + एव + आशु; "
           "अवग्रह आरम्भिक अ का सूचक है (दिशा + अनया, आ + अ → आ)। नय = सही नीति/विधि, दुर्नय = गलत। वाक्य 05.03.108 से आरम्भ। "
           "संधि जाँची: अनयैवाशु = अनया + एव (आ + ए → ऐ) + आशु (अ + आ → आ); ज्योतिर्हि = ज्योतिः + हि (इः → इर् घोष से पहले)।"),
    "95": ("विश्वास: उच्च। पुष्पिका। आरम्भ का ‘॥’ छपाई का चिह्न। अन्त का ‘इति’ पुष्पिका-सूत्र का भाग है। नाम: वमन-विरेचन-व्यापत्-सिद्धि, यानी वमन और विरेचन की "
           "व्यापदों की सिद्धि (चिकित्सा); यही नाम 05.03.1 में है। संधि जाँची: सिद्धिर्नाम = सिद्धिः + नाम (इः → इर् घोष से पहले); "
           "तृतीयोऽध्यायः = तृतीयः + अध्यायः (अः + अ → ओऽ)।"),
}


AIDS = {
    "89": {
        "chain": {"steps": ["औषध पचते समय", "मोह, भ्रम, मूर्च्छा आदि (प्यास: संदिग्ध पाठ)", "पित्तघ्न, मीठी, शीतल औषध प्रशस्त"]},
        "contrast": "05.03.100-101 ↔ 05.03.102-103: मोह, भ्रम, मूर्च्छा: पित्तघ्न, मीठी, ठण्डी औषध ↔ लार, रोमहर्ष, कफ से ढका: तीक्ष्ण, उष्ण, कफनाशक औषध।",
        "sandhi": "उः → उर् घोष से पहले: स्युः + जीर्यति → स्युर्जीर्यति।",
        "anchors": "मोह = मूढ़ता · भ्रम = चक्कर · मूर्च्छा = बेहोशी · पित्तघ्न = पित्तनाशक · शस्यते = प्रशस्त है।",
    },
    "90": {
        "chain": {"steps": ["लालास्राव, मिचली, विष्टम्भ, रोमहर्ष", "इनसे: कफ से ढका होना", "तीक्ष्ण, उष्ण, कटु आदि, कफनाशक, हितकर औषध"]},
        "sandhi": "त् + ह → द्ध: कफनुत् + हितम् → कफनुद्धितम्; अ + उ → ओ: तीक्ष्ण + उष्णम् → तीक्ष्णोष्णम्।",
        "anchors": "लाला = लार · विष्टम्भ = रुकावट · रोमहर्ष = रोंगटे खड़े होना · आवृत = ढका · कफनुत् = कफ हटाने वाला।",
    },
    "91": {
        "diagram": {"groups": [{"label": "पहली पंक्ति", "items": ["प्रतिकूल गति", "ग्रथितत्व, भारीपन सहित"]},
                               {"label": "दूसरी पंक्ति", "items": ["दोष का उत्क्लेश", "अत्यधिक आध्मान", "परिकर्त", "परिस्रव"]}]},
        "sandhi": "ओः → ओर् घोष से पहले: पायोः + ग्रथितत्वम् → पायोर्ग्रथितत्वम्; अ + उ → ओ: दोष + उत्क्लेशः → दोषोत्क्लेशः।",
        "anchors": "प्रतिकूल = उलटा · ग्रथित = गाँठदार · गौरव = भारीपन · उत्क्लेश = उभरना, हिलना · परिकर्त = काटने जैसी पीड़ा · परिस्रव = बहना।",
    },
    "92": {
        "diagram": {"groups": [{"label": "सूची का अन्त", "items": ["प्रवाहिका (पेचिश)", "हृद्ग्रहण", "सर्वाङ्गपरिग्रह", "सर्वधातुस्रव"]},
                               {"label": "समाहार", "items": ["ये बारह", "उपायों सहित कही गईं"]}]},
        "sandhi": "अ + ए → ऐ: स्रवेण + एताः → स्रवेणैता(ः); अ + उ → ओ: द्वादश + उक्ताः → द्वादशोक्ताः।",
        "anchors": "प्रवाहिका = ज़ोर लगाकर पतला मल · ग्रहण = जकड़ · परिग्रह = चारों ओर से जकड़ना · स्रव = बहाव · साधन = उपाय।",
    },
    "93": {
        "frame": "क्या: व्यापदें · किससे: योग (प्रयोग) के विभ्रंश से · कहाँ: विविध विरेचन में भी · क्रिया: अगले श्लोक (05.03.109-110) में।",
        "sandhi": "अः → ओ घोष से पहले: व्यापदः + योग… → व्यापदो योग…; त् → द् घोष से पहले: विभ्रंशात् + विविधे → विभ्रंशाद्विविधे।",
        "anchors": "व्यापद् = उपद्रव · योग = प्रयोग · विभ्रंश = चूक · विरेचन = दस्त कराने वाला शोधन।",
    },
    "94": {
        "chain": {"steps": ["संशोधन का विभ्रम", "उन-उन व्यापदों का उत्पन्न होना", "इसी निर्देश से शीघ्र सिद्धि का प्रयत्न",
                            "क्योंकि शास्त्र नय-दुर्नय का प्रकाश है"]},
        "seesaw": "नय (सही मार्ग) ↔ दुर्नय (गलत मार्ग): दोनों को शास्त्र का प्रकाश दिखाता है।",
        "chunks": "उत्पद्यमानासु च | तासु तासु व्यापत्सु | संशोधनविभ्रमेण | दिशाऽनयैवाशु | यतेत सिद्धौ | ज्योतिर्हि शास्त्रं | नयदुर्नयानां",
        "sandhi": "दिशा + अनया + एव + आशु → दिशाऽनयैवाशु (आ + अ → आ, आ + ए → ऐ, अ + आ → आ); इः → इर्: ज्योतिः + हि → ज्योतिर्हि।",
    },
    "95": {
        "chunks": "इति | वमनविरेचनव्यापत्सिद्धिर्नाम | तृतीयोऽध्यायः",
        "anchors": "वमन = उल्टी कराना · विरेचन = दस्त कराना · व्यापत् = उपद्रव · सिद्धि = चिकित्सा · तृतीय = तीसरा।",
        "sandhi": "इः → इर्: सिद्धिः + नाम → सिद्धिर्नाम; अः + अ → ओऽ: तृतीयः + अध्यायः → तृतीयोऽध्यायः।",
    },
}


IMAGE_SPECS = {
    ("89", "chain"): {
        "file": "ka3-pitta-signs-89.svg",
        "alt": "Flowchart of three steps: while the medicine is being digested; delusion, giddiness, fainting and the like (thirst on a doubtful reading); a Pitta-destroying, sweet and cool medicine is recommended",
        "type": "mermaid",
        "code": ('flowchart TD\n  A["औषध पचते समय"] --> B["मोह, भ्रम, मूर्च्छा आदि<br/>(प्यास: संदिग्ध पाठ)"]\n'
                 '  B --> C["पित्तघ्न, मीठी और<br/>शीतल औषध प्रशस्त"]\n'),
    },
    ("90", "chain"): {
        "file": "ka3-kapha-avrta-90.svg",
        "alt": "Flowchart of three steps: four signs (salivation, nausea, obstruction, horripilation) show that the medicine is enveloped by Kapha; then a sharp, hot, pungent, Kapha-dispelling and beneficial medicine",
        "type": "mermaid",
        "code": ('flowchart TD\n  A["लालास्राव, मिचली,<br/>विष्टम्भ, रोमहर्ष"] -- "इनसे पहचान" --> B["कफ से ढका होना"]\n'
                 '  B --> C["तीक्ष्ण, उष्ण, कटु आदि,<br/>कफनाशक, हितकर औषध"]\n'),
    },
    ("91", "diagram"): {
        "file": "ka3-vyapad-list-91.svg",
        "alt": "Mind map of the six items of verse 91: contrary movement, knottedness with heaviness, stirring up of the dosha, severe distension, cutting pain, discharge",
        "type": "mermaid",
        "code": ('mindmap\n  व्यापदों की सूची\n    प्रतिकूल गति\n    ग्रथितत्व, भारीपन सहित\n'
                 '    दोष का उत्क्लेश\n    अत्यधिक आध्मान\n    परिकर्त यानी काट\n    परिस्रव यानी बहना\n'),
    },
    ("94", "chain"): {
        "file": "ka3-sastra-jyoti-94.svg",
        "alt": "Flowchart: a deviation in cleansing gives rise to the various complications; in them one strives quickly for cure by this direction; a side box gives the reason: the shastra is the light of sound and unsound conduct",
        "type": "mermaid",
        "code": ('flowchart TD\n  A["संशोधन का विभ्रम"] --> B["उन-उन व्यापदों<br/>का उत्पन्न होना"]\n'
                 '  B --> C["इसी निर्देश से शीघ्र<br/>सिद्धि का प्रयत्न"]\n'
                 '  D["शास्त्र: नय और दुर्नय<br/>का प्रकाश"] -. "क्योंकि" .-> C\n'),
    },
}
