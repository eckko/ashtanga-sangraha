from helpers import mcq, match, order, fill, multi, accepts

AUTHORED = {}
NOTES_HI = {}
AIDS = {}
IMAGE_SPECS = {}

# ---------------------------------------------------------------- unit 54
AUTHORED["54"] = {
    "title": "भिन्नेंद्रनीलनीलाभ्र",
    "question": "What does line 1 say about the sky?",
    "rule": ("Line 1 describes the sky (नभः) as dimmed by clouds blue like cut "
             "sapphire. Line 2 is unclear in the print and is not used."),
    "limits": ("Line 2 (दीर्घिका ... पंक्तयः) is unclear: the compound is "
               "possibly corrupt and its relation to the rest is uncertain, so "
               "nothing is taught from it. The sentence runs on into unit 55. "
               "The sense of मंदमंद ('gently') is a reading."),
    "explain_hi": ("यह इकाई एक लंबे वर्णन का आरंभ है, पर इसकी दूसरी पंक्ति छपाई में स्पष्ट नहीं है, "
                   "इसलिए केवल पहली पंक्ति पर भरोसा किया गया है। पहली पंक्ति में आकाश (नभः) का चित्र है: "
                   "वह कटे हुए इंद्रनील मणि जैसे नीले बादलों से धुँधला हुआ है। शब्द एक लंबे समास में जुड़े हैं, "
                   "इसलिए उन्हें टुकड़ों में पहचानना ज़रूरी है। वाक्य अगली इकाई में भी चलता है।"),
    "hook": "इंद्रनील जैसे नीले बादल, धुँधला आकाश।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In line 1, what is said to be dimmed by clouds blue like cut sapphire?",
            ("The sky (नभः)", "नभः is the noun of line 1: the sky."),
            [("The river in the valley", "No river is named in line 1."),
             ("The sun above the hills", "No sun is named in line 1."),
             ("The forest on the slope", "No forest is named in line 1.")],
            "The last word of line 1, नभः, is the sky; the long compound before it describes it.",
            "नभः = sky; the clouds are blue like cut sapphire."),
        match(1, "Match each word of line 1 to its meaning.",
              [["इंद्रनील", "sapphire"], ["नील", "blue"], ["अभ्र", "cloud"], ["नभः", "sky"]],
              "These pieces carry the picture: blue clouds, sapphire-like, over the sky.",
              "इंद्रनील = sapphire; नील = blue; अभ्र = cloud; नभः = sky."),
        fill(2, "The word for 'sky' in line 1 is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("नभः", "nabhaḥ", "नभ", "nabhah"),
             "नभः is the sky, the thing that the compound describes.",
             "नभः is a neuter noun, nominative singular; the long compound before it describes it.",
             "नभः = sky."),
        mcq("discriminate", 3, "Which is the right translation of line 1?",
            ("The sky dimmed by clouds blue like cut sapphire",
             "भिन्नेंद्रनील = like cut sapphire; नीलाभ्र = blue clouds; आविल = dimmed."),
            [("The sky brightened by white clouds like moonstone", "The clouds are blue (नील), not white."),
             ("The earth dimmed by clouds blue like cut sapphire", "The noun is नभः, sky, not earth."),
             ("The sky dimmed by clouds red like cut ruby", "The stone is इंद्रनील, sapphire, and the clouds are blue.")],
            "Sky (नभः), dimmed (आविलं), by clouds that are blue like cut sapphire.",
            "नभः + आविल + नीलाभ्र: the dimmed sky has blue clouds."),
        order(4, "Put these pieces of the line 1 compound in the order of the verse.",
              ["भिन्न", "इंद्रनील", "नील", "अभ्र"],
              "The compound runs: cut, sapphire, blue, cloud.",
              "भिन्न · इंद्रनील · नील · अभ्र.", role="apply"),
        mcq("transfer", 5, "Which is the correct joined form of नील + अंबुज (blue lotus)?",
            ("नीलांबुज", "अ + अ gives आ: नील + अंबुज = नीलांबुज, as in नील + अभ्र = नीलाभ्र."),
            [("नीलअंबुज", "Two vowels meeting inside a compound are joined, not left apart."),
             ("नीलोंबुज", "अ + अ does not give ओ."),
             ("नीलैंबुज", "अ + अ does not give ऐ.")],
            "The same rule joins नील + अभ्र into नीलाभ्र: a short अ meeting अ gives a long आ.",
            "अ + अ → आ.",
            teaches="When a word ending in अ is joined to a word beginning with अ, they merge into long आ (नील + अभ्र = नीलाभ्र)."),
    ],
}
NOTES_HI["54"] = ("विश्वास: कम। दूसरी पंक्ति (दीर्घिका नववार्योघनभःसोपानपंक्तयः) अस्पष्ट है: ‘दीर्घिका’ एकवचन है और ‘पंक्तयः’ बहुवचन; ‘नभः-सोपान’ का संबंध अनिश्चित है (संभव है समास बिगड़ा हो), "
                  "इसलिए उस पर कोई प्रश्न नहीं बना। पहली पंक्ति: ‘मंदमंद’ को ‘धीरे-धीरे’ पढ़ा गया है (पठन-निर्णय)। संधि जाँची: नील + अभ्र → नीलाभ्र; भिन्न + इंद्र → भिन्नेंद्र (अ + इ → ए)। "
                  "वाक्य अगली इकाई में चलता है; पंक्ति-युग्म छपाई का है (पहली पंक्ति पिछले श्लोक से जुड़ती है)।")
AIDS["54"] = {
    "chunks": "भिन्नेंद्रनील | नीलाभ्र | मंदमंदाविलं नभः ‖ (दूसरी पंक्ति अस्पष्ट)",
    "sandhi": "अ + अ → आ: नील + अभ्र → नीलाभ्र। अ + इ → ए: भिन्न + इंद्र → भिन्नेंद्र।",
    "anchors": "इंद्रनील = नीलम जैसा नीला रत्न · अभ्र = बादल · नभः = आकाश · आविल = धुँधला।",
}

# ---------------------------------------------------------------- unit 55
AUTHORED["55"] = {
    "title": "वारिधाराभृशाघात",
    "question": "What do the rivers and the earth look like here?",
    "rule": ("The rivers are ocean-shaped (सागराकाराः) and the earth (भूः) has water and "
             "land indistinct (अव्यक्तजलस्थला); आकार = shape. Line 1 speaks of lotuses and heavy streams of water."),
    "limits": ("There is no verb. In line 1 the sense of आशित ('ruined') is a reading "
               "(असित 'dark' is a suggestion), so no question rests on it. The season "
               "is not named in this unit."),
    "explain_hi": ("यहाँ पूरा वर्णन बिना क्रिया के है। पहली पंक्ति में जल की धाराओं की चोट और कमलों का उल्लेख है; "
                   "‘आशित’ का अर्थ अनिश्चित है, इसलिए कमलों के हाल पर प्रश्न नहीं बने। दूसरी पंक्ति साफ़ है: "
                   "नदियाँ समुद्र के आकार की हैं और पृथ्वी पर जल और स्थल का भेद साफ़ नहीं दिखता। "
                   "‘भूः’ अगली इकाइयों का भी विषय बना रहता है।"),
    "hook": "नदियाँ समुद्र जैसी, जल-स्थल का भेद धुँधला।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "Which is said to be ocean-shaped in line 2?",
            ("The rivers (सरितः)", "सरितः सागराकाराः: the rivers are ocean-shaped."),
            [("The lotus ponds (कमल)", "Lotuses belong to line 1 and are not called ocean-shaped."),
             ("The dark clouds (मेघ)", "No clouds are named in this unit."),
             ("The high hills (गिरि)", "No hills are named in this unit.")],
            "Line 2 begins सरितः सागराकारा: the rivers are ocean-shaped.",
            "सरितः = rivers; सागराकाराः = ocean-shaped."),
        match(1, "Match each word of line 2 to its meaning.",
              [["सरितः", "rivers"], ["सागर", "ocean"], ["भूः", "earth"], ["अव्यक्त", "indistinct"]],
              "These four words carry the whole of line 2.",
              "सरितः = rivers; सागर = ocean; भूः = earth; अव्यक्त = indistinct."),
        mcq("extend", 2, "Which is the right sandhi result of भूः + अव्यक्त?",
            ("भूरव्यक्त", "A visarga after ऊ before a vowel becomes र्."),
            [("भूअव्यक्त", "The visarga does not simply vanish here."),
             ("भूसव्यक्त", "A visarga before a vowel does not become स्."),
             ("भूओव्यक्त", "ओ appears only after अ + visarga, not after ऊ.")],
            "भूः + अव्यक्त joins as भूरव्यक्त: the visarga after ऊ turns to र् before a vowel.",
            "Visarga after a vowel other than अ/आ + vowel → र्.",
            teaches="A visarga after a vowel other than अ or आ turns into र् before a vowel (भूः + अ… = भूर्…)."),
        mcq("discriminate", 3, "Which is the right translation of line 2?",
            ("Rivers look like oceans; earth shows no clear water-land line",
             "Both parts follow the words सागराकाराः and अव्यक्तजलस्थला."),
            [("The rivers are dry; the earth has water and land clear", "Neither part matches: अव्यक्त is indistinct."),
             ("The rivers are ocean-shaped; the earth has only dry land everywhere", "जलस्थला names water and land together, indistinct."),
             ("The oceans are river-shaped; the earth has water and land clear", "सागर is in the comparison: rivers look like oceans.")],
            "Line 2 says the rivers look like oceans and the earth has no clear line between water and land.",
            "सागराकाराः (rivers) · अव्यक्तजलस्थला (earth)."),
        order(4, "Put these parts of line 2 in the order of the verse.",
              ["सरितः", "सागराकारा", "भूः", "अव्यक्तजलस्थला"],
              "Line 2 runs: rivers, ocean-shaped, earth, with water and land indistinct.",
              "सरितः · सागराकारा · भूः · अव्यक्तजलस्थला.", role="apply"),
        mcq("transfer", 5, "In an invented phrase पर्वताकारः गजः, what is the elephant like?",
            ("It is shaped like a mountain", "X-आकार at the end of a compound means shaped like X."),
            [("It lives on a mountain", "The word says shape, not dwelling."),
             ("It is the lord of mountains", "Nothing in -आकार means lord."),
             ("It is far from the mountain", "Nothing in the word speaks of distance.")],
            "सागराकाराः (ocean-shaped) is सागर + आकार; the same pattern gives पर्वताकार, mountain-shaped.",
            "X-आकार = shaped like X.",
            teaches="A compound ending in -आकार means 'shaped like' the first part (सागराकाराः, पर्वताकारः)."),
    ],
}
NOTES_HI["55"] = ("विश्वास: मध्यम। पूरा वाक्य क्रियारहित है। पहली पंक्ति में ‘आशित’ का अर्थ ‘नष्ट’ पढ़ा गया है, पर यह अनिश्चित है (सुझाव ‘असित’, काला, जिससे अर्थ बदलेगा); इसलिए कमलों के हाल पर प्रश्न नहीं बना। "
                  "संधि जाँची: सागर + आकाराः → सागराकाराः (भ् से पहले विसर्ग छूटा: ‘सागराकारा’); भूः + अव्यक्त → भूरव्यक्त। दूसरी पंक्ति का कर्ता ‘भूः’ है और वही अगली इकाइयों (५६-५७) का भी है।")
AIDS["55"] = {
    "chunks": "वारिधाराभृशाघात | विकाराशितसरोरुहाः ‖ सरितः सागराकारा | भूरव्यक्तजलस्थला।",
    "sandhi": "अ + आ → आ: सागर + आकाराः → सागराकाराः (विसर्ग भ् जैसी घोष ध्वनि से पहले छूटा)। भूः + अव्यक्त → भूरव्यक्त (विसर्ग → र् स्वर से पहले)।",
    "frame": "दूसरी पंक्ति: नदियाँ कैसी (समुद्र जैसी) · पृथ्वी कैसी (जल-स्थल अस्पष्ट)।",
    "anchors": "सरित् = नदी · सागर = समुद्र · आकार = रूप · अव्यक्त = अस्पष्ट · स्थल = ज़मीन।",
}

# ---------------------------------------------------------------- unit 56
AUTHORED["56"] = {
    "title": "मंद्रस्तनितजीमूत",
    "question": "What sounds fill the earth and what lights it up?",
    "rule": ("The earth resounds (नादिता) with deep thunder of clouds, peacocks and frogs, "
             "and is lit (दीपिता) by indragopa insects, bow-fragments and lightning flashes."),
    "limits": ("The two participles are feminine singular and go with भूः of the previous "
               "unit. धनुःखंड is literally pieces of a bow; reading them as pieces of the "
               "rainbow is an interpretation. इंद्रगोप is an insect name only."),
    "explain_hi": ("दोनों पंक्तियाँ पिछली इकाई की ‘भूः’ के बारे में हैं। पहली पंक्ति में पृथ्वी ‘नादिता’ है यानी गूँजती है: "
                   "बादलों की गहरी गर्जना, मोरों और मेंढकों की आवाज़ से। दूसरी पंक्ति में वह ‘दीपिता’ है यानी "
                   "प्रकाशित: इंद्रगोप कीट, धनुष के खंड और बिजली की चमक से। दोनों में तीन-तीन चीज़ें गिनाई गई हैं, "
                   "इसलिए क्रम याद रखना आसान है।"),
    "hook": "पहली पंक्ति में आवाज़ें, दूसरी में चमक: तीन और तीन।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By which three does line 1 say the earth resounds?",
            ("Clouds, peacocks and frogs", "जीमूत, शिखी, दर्दुर: clouds, peacocks, frogs."),
            [("Rivers, swans and fish alike", "None of these is named in line 1."),
             ("Bees, cuckoos and cranes together", "None of these is named in line 1."),
             ("Winds, drums and bells together", "None of these is named in line 1.")],
            "Line 1 names the deep thunder of clouds and the sounds of peacocks and frogs.",
            "जीमूत (cloud) · शिखी (peacock) · दर्दुर (frog) sound; the earth is नादिता."),
        match(1, "Match each word of the unit to its meaning.",
              [["जीमूत", "cloud"], ["मंद्र", "deep"], ["दर्दुर", "frog"], ["विद्युत्", "lightning"]],
              "मंद्र (deep) and the cloud and frog belong to line 1; lightning is the last item of line 2.",
              "जीमूत = cloud; मंद्र = deep; दर्दुर = frog; विद्युत् = lightning."),
        fill(2, "The word for 'peacock' in line 1 is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("शिखी", "शिखि", "shikhi"),
             "शिखी is the peacock, the second sound-maker of line 1.",
             "शिखी names the peacock; with the cloud and the frog it makes the three sound-makers.",
             "शिखी = peacock."),
        multi("discriminate", 3, "Which three does line 2 say light up the earth?",
              [("peacocks (शिखी)", "Peacocks belong to line 1 and are among the sounds."),
               ("indragopa insects (इंद्रगोप)", "Right: the first item of line 2."),
               ("frogs (दर्दुर)", "Frogs belong to line 1 and are among the sounds."),
               ("fragments of the bow (धनुःखंड)", "Right: the second item of line 2."),
               ("flashes of lightning (विद्युदुद्योत)", "Right: the third item of line 2.")],
              [1, 3, 4],
              "Line 2 lists indragopa insects, bow-fragments and lightning flashes as what lights the earth.",
              "दीपिता (lit) by इंद्रगोप · धनुःखंड · विद्युदुद्योत."),
        order(4, "Put the three things that light the earth in the order of line 2.",
              ["इंद्रगोप", "धनुःखंड", "विद्युदुद्योत"],
              "Line 2 runs: indragopa, bow-fragments, lightning flashes.",
              "इंद्रगोप · धनुःखंड · विद्युदुद्योत.", role="apply"),
        mcq("transfer", 5, "In an invented phrase भ्रमरनादिता वनभूः, what does the forest ground do?",
            ("It resounds with bees", "-नादिता is feminine, 'resounding with', like मंद्र…नादिता."),
            [("It is lit up by the bees", "Lit would be -दीपिता, as in line 2."),
             ("It is stung by many bees", "Nothing in -नादिता means stung."),
             ("It is entirely free from bees", "Free from would be -वर्जिता or -रहिता.")],
            "नादिता means resounding; the first part of the compound names what makes the sound, as दर्दुर does.",
            "X-नादिता = resounding with X; X-दीपिता = lit by X.",
            teaches="A feminine compound ending in -नादिता means 'resounding with' the first part, and -दीपिता means 'lit by' it."),
    ],
}
NOTES_HI["56"] = ("विश्वास: उच्च। दोनों विशेषण (नादिता, दीपिता) स्त्रीलिंग एकवचन हैं और पिछली इकाई की ‘भूः’ से जुड़ते हैं। ‘धनुःखंड’ का शाब्दिक अर्थ धनुष के टुकड़े है; ‘इंद्रधनुष के टुकड़े’ पढ़ना व्याख्या है, इसलिए प्रश्न शाब्दिक अर्थ पर ही हैं। "
                  "‘इंद्रगोप’ कीट का नाम है, पहचान नहीं बताई गई। संधि जाँची: विद्युत् + उद्योत → विद्युदुद्योत (त् → द् स्वर से पहले); मंद्र + स्तनित में विसर्ग नहीं, समास है।")
AIDS["56"] = {
    "diagram": {"groups": [
        {"label": "गूँजती है (नादिता)", "items": ["जीमूत", "शिखी", "दर्दुर"]},
        {"label": "प्रकाशित (दीपिता)", "items": ["इंद्रगोप", "धनुःखंड", "विद्युत्"]}]},
    "chunks": "मंद्रस्तनितजीमूत | शिखिदर्दुरनादिता ‖ इंद्रगोपधनुःखंड | विद्युदुद्योतदीपिता।",
    "sandhi": "त् → द् (स्वर से पहले): विद्युत् + उद्योत → विद्युदुद्योत।",
    "contrast": "नादिता (आवाज़ से भरी, पहली पंक्ति) ↔ दीपिता (चमक से प्रकाशित, दूसरी पंक्ति)।",
}
IMAGE_SPECS[("56", "diagram")] = {
    "file": "ch4b05-sounds-lights-56.svg",
    "alt": "Two columns for unit 56: the earth resounds with cloud, peacock, frog (3); it is lit by indragopa, bow-fragments, lightning (3).",
    "type": "split",
    "title": "श्लोक ५६: पृथ्वी",
    "cols": [["गूँजती है (नादिता)", ["जीमूत", "शिखी", "दर्दुर"]],
             ["प्रकाशित (दीपिता)", ["इंद्रगोप", "धनुःखंड", "विद्युत्"]]],
}

# ---------------------------------------------------------------- unit 57
AUTHORED["57"] = {
    "title": "परितः श्यामलतृणा",
    "question": "How is the earth described, and what starts line 2?",
    "rule": ("Line 1: the earth has dark-green grass all around and is bright with "
             "śilīndhra and kuṭaja. Line 2 starts a new clause: at that time (तदा), then "
             "body weak, fire dull and afflicted, again (पुनः); the nouns and participles "
             "देहे, मंदेऽग्नौ, बाधिते (and आदानाबले) are locatives."),
    "limits": ("Line 2 is not a complete sentence: it goes on in unit 58. ‘आदान’ is "
               "not explained here. शिलींध्र and कुटज are names only."),
    "explain_hi": ("पहली पंक्ति पृथ्वी का वर्णन पूरा करती है: चारों ओर गहरी हरी घास, और शिलींध्र तथा कुटज से उज्ज्वल। "
                   "दूसरी पंक्ति नया वाक्य खोलती है: ‘तदा’ (उस समय), जब शरीर आदान के कारण निर्बल हो, अग्नि मंद हो "
                   "और फिर बाधित हो। देहे, मंदे-अग्नौ और बाधिते सप्तमी में हैं, और मुख्य क्रिया अगली इकाई में आती है। "
                   "इसलिए इस इकाई से केवल इन्हीं बातों पर प्रश्न बने हैं।"),
    "hook": "हरी घास की धरती; फिर ‘उस समय’ की शर्तें शुरू।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What grass does line 1 say the earth has all around?",
            ("Dark-green grass (श्यामलतृणा)", "श्यामल = dark-green, तृण = grass."),
            [("Dry yellow grass of summer", "श्यामल is dark-green, not yellow or dry."),
             ("No grass anywhere at all", "तृणा names grass the earth has."),
             ("White flowering grass in bloom", "No white flowers are mentioned here.")],
            "परितः श्यामलतृणा: all around, with dark-green grass.",
            "परितः = all around; श्यामल = dark-green; तृण = grass."),
        match(1, "Match each word of line 1 to its meaning.",
              [["परितः", "all around"], ["श्यामल", "dark-green"], ["तृण", "grass"], ["उज्ज्वल", "bright"]],
              "These four words build line 1.",
              "परितः = all around; श्यामल = dark-green; तृण = grass; उज्ज्वल = bright."),
        mcq("extend", 2, "In line 2, which group contains only locative forms?",
            ("देहे, मंदेऽग्नौ, बाधिते", "Each ends in a locative sign (-ए, -औ): in the body, the fire dull, afflicted."),
            [("तदा, पुनः, देहे", "तदा and पुनः are indeclinables, not locative forms."),
             ("आदानाबले, पुनः, तदा", "पुनः and तदा are indeclinables."),
             ("मंदेऽग्नौ, तदा, पुनः", "तदा and पुनः are indeclinables.")],
            "देहे (in the body), मंदे and अग्नौ (in the fire, dull), बाधिते (afflicted) are locative, and so is आदानाबले; तदा and पुनः are indeclinables.",
            "Locative absolute: noun + participle both locative = 'when X is Y'.",
            teaches="Two or more words in the locative can together mean 'when X is Y' (a locative absolute); the main verb comes later."),
        mcq("discriminate", 3, "Which is the right sandhi result of मंदे + अग्नौ?",
            ("मंदेऽग्नौ", "-ए before अ keeps ए and drops the अ, marked by ऽ."),
            [("मंदयग्नौ", "Final ए before a short अ keeps ए (the अ is dropped and marked ऽ); it is not changed to य्."),
             ("मंदाग्नौ", "ए + अ does not give long आ."),
             ("मंदैग्नौ", "ए + अ does not give ऐ.")],
            "Final -ए followed by a short अ stays ए, and the अ is shown by the avagraha mark ऽ.",
            "ए + अ → एऽ."),
        order(4, "Put these parts of line 2 in the order of the verse.",
              ["तदा", "आदानाबले", "देहे", "मंदेऽग्नौ", "बाधिते", "पुनः"],
              "Line 2 runs: at that time, weak from ādāna, in the body, in the dull fire, afflicted, again.",
              "तदा · आदानाबले · देहे · मंदेऽग्नौ · बाधिते · पुनः.", role="apply"),
        mcq("transfer", 5, "Which invented phrase means: when the sun has risen?",
            ("सूर्ये उदिते", "Noun and participle both in the locative: 'the sun being risen'."),
            [("सूर्यः उदितः", "Both nominative: 'the sun has risen', a plain statement."),
             ("सूर्यम् उदितम्", "Both accusative: a different construction."),
             ("सूर्येण उदितेन", "Both instrumental: 'by the risen sun'.")],
            "Like देहे ... बाधिते in line 2, two locatives together give 'when ... being ...'.",
            "Locative + locative participle = 'when X has done/been Y'.",
            teaches="A noun and a past participle both in the locative state a circumstance: सूर्ये उदिते = 'when the sun has risen'."),
    ],
}
NOTES_HI["57"] = ("विश्वास: उच्च। दूसरी पंक्ति का वाक्य अगली इकाई (५८) में पूरा होता है: देहे, मंदेऽग्नौ, बाधिते सप्तमी में हैं और मुख्य क्रिया ‘निषेवेत’ ५८ में है। ‘आदानाबले’ = आदान + अबले (‘आदान के कारण निर्बल’); "
                  "‘आदान’ की व्याख्या इस इकाई में नहीं है। शिलींध्र, कुटज: पौधों के नाम, पहचाने नहीं गए। संधि जाँची: तदाऽऽदान = तदा + आदान (आ + आ → आ, ऽ चिह्न के साथ छपा); मंदे + अग्नौ → मंदेऽग्नौ।")
AIDS["57"] = {
    "chunks": "परितः श्यामलतृणा | शिलींध्रकुटजोज्ज्वला ‖ तदाऽऽदानाबले देहे | मंदेऽग्नौ बाधिते पुनः।",
    "sandhi": "ए + अ → एऽ: मंदे + अग्नौ → मंदेऽग्नौ। अ + उ → ओ: कुटज + उज्ज्वला → कुटजोज्ज्वला।",
    "frame": "पंक्ति १: पृथ्वी (हरी घास, चमकती) · पंक्ति २: तदा · शरीर निर्बल (आदान से) · अग्नि मंद · फिर बाधित (वाक्य आगे चलता है)।",
}

# ---------------------------------------------------------------- unit 58
AUTHORED["58"] = {
    "title": "वृष्टिभूबाष्पतोयाम्ल",
    "question": "What does the verse say one should resort to, and after what?",
    "rule": ("Having completed the course of cleansing (कृतसंशोधनक्रमः), one should resort to "
             "the basti procedure (बस्तिकर्म निषेवेत). The clause completes unit 57."),
    "limits": ("The verse says only this; it gives no dose, method or other advice. ‘चल’ is "
               "taken as Vāta and ‘आदि’ as the other doṣas. The first line completes "
               "the 'afflicted' of unit 57."),
    "explain_hi": ("यह इकाई पिछली इकाई का वाक्य पूरा करती है। पहली पंक्ति कहती है कि वर्षा, भूमि की भाप और जल के खट्टे परिवर्तन से "
                   "दूषित हुए चल (वात) आदि दोषों के द्वारा बाधित होने पर। दूसरी पंक्ति में निर्देश है: बस्ति कर्म का "
                   "सेवन करना चाहिए, और वह भी शोधन का क्रम पूरा कर लेने के बाद। श्लोक इससे अधिक कुछ नहीं कहता: "
                   "न मात्रा, न विधि।"),
    "hook": "पहले शोधन का क्रम पूरा, फिर बस्तिकर्म का सेवन।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "Which procedure does line 2 say one should resort to?",
            ("The basti procedure (बस्तिकर्म)", "बस्तिकर्म निषेवेत: one should resort to the basti procedure."),
            [("The oil massage (अभ्यंग)", "Not named in line 2."),
             ("The fasting course (उपवास)", "Not named in line 2."),
             ("The sweating procedure (स्वेदन)", "Not named in line 2.")],
            "Line 2 gives the instruction बस्तिकर्म निषेवेत.",
            "बस्तिकर्म + निषेवेत = one should resort to the basti procedure."),
        match(1, "Match each word of line 2 to its meaning.",
              [["बस्तिकर्म", "basti procedure"], ["निषेवेत", "should resort to"],
               ["कृत", "completed"], ["संशोधन", "cleansing"]],
              "The words of line 2 say what to resort to and what must be done first.",
              "बस्तिकर्म = basti procedure; निषेवेत = should resort to; कृत = completed; संशोधन = cleansing."),
        mcq("extend", 2, "Which word means one should dwell?",
            ("वसेत्", "-एत् marks 'should', as -एत in निषेवेत."),
            [("वसति", "This is the plain present: 'dwells'."),
             ("अवसत्", "This is a past form: 'dwelt'."),
             ("वासः", "This is a noun: 'a dwelling'.")],
            "निषेवेत is a 'should' form (3rd person singular optative); वसेत् is built the same way.",
            "-एत् / -एत = optative 'should'.",
            teaches="A verb ending in -एत् (or -एत in the middle voice) says what one should do (निषेवेत, वसेत्)."),
        mcq("discriminate", 3, "Which is the right translation of line 2?",
            ("One should resort to basti, having completed the course of cleansing",
             "बस्तिकर्म निषेवेत; कृतसंशोधनक्रमः = one who has completed the course of cleansing."),
            [("One should avoid the basti procedure, having completed the whole course of cleansing",
              "निषेवेत means resort to, not avoid."),
             ("One should resort to cleansing, having completed the basti procedure",
              "The completed course is the cleansing, and basti is what follows."),
             ("One should resort to the basti procedure before any cleansing",
              "कृत says the cleansing is already completed.")],
            "The order given is: cleansing completed first, then the basti procedure.",
            "कृतसंशोधनक्रमः (completed cleansing) → बस्तिकर्म निषेवेत."),
        order(4, "Put these parts of line 2 in the order of the verse.",
              ["बस्तिकर्म", "निषेवेत", "कृतसंशोधनक्रमः"],
              "Line 2 runs: basti procedure, should resort to, one who has completed the course of cleansing.",
              "बस्तिकर्म · निषेवेत · कृतसंशोधनक्रमः.", role="apply"),
        mcq("transfer", 5, "Which phrase means one should read the book?",
            ("ग्रंथं पठेत्", "An accusative object plus a -एत् verb: 'should read the book'."),
            [("ग्रंथं पठति", "This is the plain present: 'reads the book'."),
             ("ग्रंथम् अपठत्", "This is a past form: 'read the book'."),
             ("ग्रंथः पाठः", "Two nouns: 'book, reading', no verb.")],
            "Like बस्तिकर्म निषेवेत, the object stands in the accusative and the verb ends in -एत्.",
            "Object (accusative) + -एत् verb = 'should do X'.",
            teaches="A command in the verse is an object plus a verb in -एत्: ग्रंथं पठेत् = 'one should read the book'."),
    ],
}
NOTES_HI["58"] = ("विश्वास: उच्च। यह इकाई ५७ का वाक्य पूरा करती है (अग्नि ‘बाधित’ चल आदि दोषों से; मुख्य क्रिया निषेवेत)। ‘चल’ का अर्थ वात लिया गया है, ‘आदि’ से शेष दोष। ‘अम्लपाक’ = जल का खट्टा परिवर्तन, शाब्दिक रखा गया। "
                  "‘निषेवेत’ = लट् नहीं, विधिलिङ् (आत्मनेपद, प्रथम पुरुष एकवचन) — डेटा के अनुसार। श्लोक में मात्रा या विधि नहीं है, इसलिए कोई प्रश्न उस पर नहीं बना। "
                  "संधि जाँची: कृतसंशोधनक्रमः बहुव्रीहि है (जिसने शोधन का क्रम पूरा किया); वृष्टिभू... दुष्टैः + चलादिभिः अलग पद हैं।")
AIDS["58"] = {
    "chain": {"steps": ["शोधन का क्रम पूरा हुआ (कृतसंशोधनक्रमः)", "फिर बस्तिकर्म का सेवन करना चाहिए (निषेवेत)"]},
    "chunks": "वृष्टिभूबाष्पतोयाम्ल | पाकदुष्टैश्चलादिभिः ‖ बस्तिकर्म निषेवेत | कृतसंशोधनक्रमः।",
    "frame": "पंक्ति १: किनसे बाधित (वर्षा आदि से दूषित चल आदि) · पंक्ति २: क्या करे (बस्तिकर्म निषेवेत) · कब (शोधन के बाद)।",
    "anchors": "निषेवेत = सेवन करे · कृत = पूरा किया · संशोधन = शुद्धि · क्रम = क्रम, चरण।",
}
IMAGE_SPECS[("58", "chain")] = {
    "file": "ch4b05-basti-after-cleansing-58.svg",
    "alt": "Two-step chain for unit 58 in time order (not verse order): the course of cleansing is completed, then one should resort to the basti procedure.",
    "type": "chain",
    "title": "श्लोक ५८: समय का क्रम",
    "steps": ["शोधन का क्रम पूरा", "फिर बस्तिकर्म का सेवन"],
}

# ---------------------------------------------------------------- unit 59
AUTHORED["59"] = {
    "title": "पुराणशालि गोधूमयवान्",
    "question": "Which grains and which drinks does the unit list?",
    "rule": ("Old śāli rice, wheat and barley, with prepared yūṣas and broths; madirā, "
             "ariṣṭa and mārdvīka (निर्गदं \"harmless\", attachment uncertain), or else a very small amount of water."),
    "limits": ("There is no verb: ‘one should take’ is understood from a nearby unit. "
               "निर्गदं may go with the drinks or stand alone as ‘harmless’. The verse "
               "names drinks and gives no dose or reason."),
    "explain_hi": ("इस इकाई में कोई क्रिया नहीं है; ‘लेना चाहिए’ आस-पास की इकाई से समझा जाता है। पहली पंक्ति अन्न गिनाती है: "
                   "पुराना शालि चावल, गेहूँ और जौ, तैयार किए यूष और रसों के साथ। दूसरी पंक्ति पेय गिनाती है: "
                   "मदिरा (निर्गदं: संभवतः उनका विशेषण), अरिष्ट और मार्द्वीक, अथवा बहुत थोड़ा जल। श्लोक केवल नाम और क्रम देता है, कोई मात्रा नहीं।"),
    "hook": "पहली पंक्ति में अन्न, दूसरी में पेय या थोड़ा जल।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "Which three grains does line 1 list?",
            ("Old śāli rice, wheat and barley", "पुराणशालि, गोधूम, यव."),
            [("Millet, maize and oats", "None of these is named in the unit."),
             ("Old śāli rice, lentils and sesame", "Lentils and sesame are not named in line 1."),
             ("Wheat, barley and mustard", "Mustard is not named in line 1.")],
            "Line 1 names old śāli rice, wheat and barley.",
            "पुराणशालि · गोधूम · यव."),
        match(1, "Match each word to its meaning.",
              [["शालि", "rice"], ["गोधूम", "wheat"], ["यव", "barley"], ["अंबु", "water"]],
              "Three words name the grains; अंबु is the water of the last words.",
              "शालि = rice; गोधूम = wheat; यव = barley; अंबु = water."),
        fill(2, "The word for 'barley' in line 1 is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("यव", "yava", "यवान्", "yavan"),
             "यव is barley, the third grain of the list.",
             "In the printed गोधूमयवान् the two grains are joined as a pair (wheat and barley).",
             "यव = barley."),
        multi("discriminate", 3, "Which three prepared drinks does line 2 name, not counting the water at the end?",
              [("madirā (मदिरा)", "Right: the first drink of line 2."),
               ("yūṣa (यूष)", "Yūṣa is taken with the grains in line 1."),
               ("ariṣṭa (अरिष्ट)", "Right: the second drink of line 2."),
               ("rasa (रस)", "Rasa (broth) is taken with the grains in line 1."),
               ("mārdvīka (मार्द्वीक)", "Right: the third drink of line 2.")],
              [0, 2, 4],
              "Line 2 lists madirā, ariṣṭa and mārdvīka, and then 'or a very small amount of water'.",
              "Drinks: मदिरा · अरिष्ट · मार्द्वीक."),
        order(4, "Put the three prepared drinks in the order of line 2.",
              ["मदिरा", "अरिष्ट", "मार्द्वीक"],
              "Line 2 runs: madirā, ariṣṭa, mārdvīka, then a small amount of water.",
              "मदिरा · अरिष्ट · मार्द्वीक.", role="apply"),
        mcq("transfer", 5, "In an invented phrase तिलमुद्गान्, what are the two items?",
            ("Sesame and mung beans", "Two items joined in one word form a pair, as in गोधूमयवान्."),
            [("Sesame, of mung beans", "A pair-compound lists items; it does not mean 'of'."),
             ("Sesame that is mung bean", "The two items stay separate."),
             ("Sesame without mung beans", "Nothing in the compound means 'without'.")],
            "गोधूमयवान् is 'wheat and barley'; a compound of this kind (dvandva) means 'A and B'.",
            "Dvandva compound = 'A and B'.",
            teaches="Items joined in one word, each in the same case, mean 'A and B' (गोधूमयवान् = wheat and barley)."),
    ],
}
NOTES_HI["59"] = ("विश्वास: मध्यम। कोई क्रिया नहीं है; ‘निषेवेत’ (५८) या ‘भजेत्’ (६१) समझा जाता है। ‘पुराणशालि’ का -इ एकवचन-समूह है या -न् का लोप — दोनों संभव; अर्थ ‘पुराना शालि’ ही है। "
                  "‘निर्गदं’ मदिरा-आदि का विशेषण भी हो सकता है और अलग भी; डेटा में पेयों के साथ लिया गया है। यूष और रस को संस्कृत में ही रखा। संधि जाँची: गोधूम + यवान् एक द्वंद्व पद (गोधूमयवान्); मदिरा + अरिष्ट → मदिरारिष्ट (आ + अ → आ); मार्द्वीकं + स्वल्प में अनुस्वार वैसा ही।")
AIDS["59"] = {
    "diagram": {"groups": [
        {"label": "अन्न (पंक्ति १)", "items": ["पुराणशालि", "गोधूम", "यव"]},
        {"label": "पेय (पंक्ति २; अंत में: जल)", "items": ["मदिरा", "अरिष्ट", "मार्द्वीक", "बहुत थोड़ा जल"]}]},
    "chunks": "पुराणशालि गोधूमयवान् | यूषरसैः कृतैः ‖ निर्गदं मदिरारिष्टमार्द्वीकं | स्वल्पमंबु वा।",
    "frame": "अन्न: शालि · गोधूम · यव (यूष-रस के साथ) · पेय: मदिरा · अरिष्ट · मार्द्वीक, या बहुत थोड़ा जल।",
}
IMAGE_SPECS[("59", "diagram")] = {
    "file": "ch4b05-grains-drinks-59.svg",
    "alt": "Two columns for unit 59: grains (old shali rice, wheat, barley) and drinks (madira, arishta, mardvika, a very small amount of water).",
    "type": "split",
    "title": "श्लोक ५९: अन्न और पेय",
    "cols": [["अन्न (पंक्ति १)", ["पुराणशालि", "गोधूम", "यव"]],
             ["पेय (पंक्ति २; अंत में: जल)", ["मदिरा", "अरिष्ट", "मार्द्वीक", "बहुत थोड़ा जल"]]],
}

# ---------------------------------------------------------------- unit 60
AUTHORED["60"] = {
    "title": "दिव्यं कथितकूपोत्थं",
    "question": "Which waters are named, and what should the food do on a rainy windy day?",
    "rule": ("Waters: rainwater (दिव्य), boiled well-water, cauṇḍya, lake water. On a day "
             "troubled by rain and wind the food is to be one that overcomes dampness "
             "(क्लेद) and Vāta."),
    "limits": ("चौंड्य is obscure (perhaps water of a small pool), so no question rests on its "
               "meaning. The verb is not stated. The printed ‘सारसमेववा’ is odd but kept."),
    "explain_hi": ("पहली पंक्ति जलों के नाम गिनाती है: दिव्य (आकाश से, यानी वर्षा का), उबाला हुआ कुएँ का जल, चौण्ड्य "
                   "और सरोवर का जल। ‘चौण्ड्य’ का अर्थ अस्पष्ट है। दूसरी पंक्ति कहती है कि वर्षा और वायु से व्याकुल दिन में "
                   "भोजन क्लेद और वात को जीतने वाला हो। श्लोक कारण या मात्रा नहीं देता।"),
    "hook": "चार जल; और वर्षा-वायु के दिन का भोजन क्लेद-वात-जित्।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What does line 2 say the food should overcome?",
            ("Dampness (क्लेद) and Vāta", "भोजनं क्लेदवातजित्: food overcoming kleda and Vāta."),
            [("Hunger and thirst together", "These are not named in the line."),
             ("Heat and sunlight together", "These are not named in the line."),
             ("Dust and smoke together", "These are not named in the line.")],
            "Line 2 says the food is क्लेदवातजित्: overcoming dampness and Vāta.",
            "क्लेद-वात-जित् = overcoming dampness and Vāta."),
        match(1, "Match each word of line 1 to its meaning.",
              [["दिव्यम्", "rainwater, from the sky"], ["कथित", "boiled"],
               ["कूप", "well"], ["सारसम्", "of a lake"]],
              "Each word tells where the water comes from or how it is treated.",
              "दिव्यम् = from the sky; कथित = boiled; कूप = well; सारसम् = of a lake."),
        mcq("extend", 2, "Which is the right sandhi result of तु + अह्नि?",
            ("त्वह्नि", "उ before a different vowel turns into व्."),
            [("तुअह्नि", "The vowels are not left apart."),
             ("तोह्नि", "उ + अ does not give ओ."),
             ("ताह्नि", "उ + अ does not give आ.")],
            "तु + अह्नि = त्वह्नि: a short उ before a different vowel becomes व्.",
            "उ + different vowel → व् + vowel.",
            teaches="A final उ before a different vowel turns into व् (तु + अह्नि = त्वह्नि)."),
        mcq("discriminate", 3, "Which phrase describes the day in line 2?",
            ("Troubled by rain and wind", "वृष्टिवाताकुले: troubled by rain and wind."),
            [("Hot and dry with no rain at all", "Nothing in the words speaks of heat or dryness."),
             ("Cold and dark with heavy frost", "Nothing in the words speaks of cold or darkness."),
             ("Clear and calm all day long", "आकुल means troubled, the opposite of calm.")],
            "वृष्टिवाताकुले अह्नि is 'on a day troubled by rain and wind'.",
            "आकुल = troubled; वृष्टि = rain; वात = wind."),
        order(4, "Put these waters in the order of line 1.",
              ["दिव्यम्", "कथितकूपोत्थम्", "चौंड्यम्", "सारसम्"],
              "Line 1 runs: rainwater, boiled well-water, cauṇḍya, lake water.",
              "दिव्यम् · कथितकूपोत्थम् · चौंड्यम् · सारसम्.", role="apply"),
        mcq("transfer", 5, "In an invented phrase शत्रुजित् नृपः, what does the king do?",
            ("He conquers enemies", "-जित् at the end means overcoming the first part."),
            [("He is born of enemies", "'Born of' would be -ज."),
             ("He is loved by enemies", "Nothing in -जित् means loved."),
             ("He fears enemies", "Nothing in -जित् means fearing.")],
            "क्लेदवातजित् is क्लेद-वात-जित्, overcoming dampness and Vāta; शत्रुजित् is overcoming enemies.",
            "X-जित् = overcoming X.",
            teaches="A compound ending in -जित् means 'overcoming' the first part (क्लेदवातजित्, शत्रुजित्)."),
    ],
}
NOTES_HI["60"] = ("विश्वास: मध्यम। ‘चौंड्य’ अस्पष्ट है (संभवतः चुण्ड/चुण्डी, छोटे ताल का जल; पुस्तक ‘तालाब का जल’ कहती है), इसलिए उसके अर्थ पर प्रश्न नहीं। ‘दिव्य’ = आकाश से, यानी वर्षा का जल। क्रिया नहीं है। "
                  "‘सारसमेववा’ में ‘एव’ ‘वा’ से पहले अटपटा है पर जैसा छपा है वैसा रखा। संधि जाँची: तु + अह्नि → त्वह्नि; वृष्टि + वात + आकुले → वृष्टिवाताकुले (अ + आ → आ); कथित + कूप + उत्थं → कथितकूपोत्थं (अ + उ → ओ)।")
AIDS["60"] = {
    "chunks": "दिव्यं कथितकूपोत्थं | चौंड्यं सारसमेववा ‖ वृष्टिवाताकुले त्वह्नि | भोजनं क्लेदवातजित्।",
    "sandhi": "उ + भिन्न स्वर → व्: तु + अह्नि → त्वह्नि। अ + उ → ओ: कूप + उत्थं → कूपोत्थं।",
    "frame": "पंक्ति १: जल के चार प्रकार · पंक्ति २: वर्षा-वायु से व्याकुल दिन में भोजन क्लेद और वात को जीतने वाला। त्वह्नि = तु (परंतु) + अह्नि (दिन में)।",
}

# ---------------------------------------------------------------- unit 61
AUTHORED["61"] = {
    "title": "परिशुष्कं लघु स्निग्धम्",
    "question": "What qualities of food does line 1 list?",
    "rule": ("Line 1: food well dried, light, unctuous, hot, sour and salty, to be taken. "
             "Line 2: food and drink with honey, when dense clouds rise (प्रायः, 'mostly', may belong to line 1)."),
    "limits": ("संस्रुत in line 2 is uncertain (‘strained’ is a reading; the book says "
               "‘thick’), so no question rests on it. प्रायः could also go with line 1. "
               "The verse gives no dose or reason."),
    "explain_hi": ("पहली पंक्ति भोजन के छह गुण गिनाती है: अच्छी तरह सूखा, हल्का, स्निग्ध, गरम, खट्टा और नमकीन; "
                   "और कहती है कि यह लेना चाहिए। दूसरी पंक्ति में घने बादल उठने पर अन्न-पान शहद के साथ होने की बात है (‘प्रायः’ किसके साथ है, अनिश्चित)। "
                   "‘संस्रुत’ का अर्थ अनिश्चित है, इसलिए उस पर प्रश्न नहीं बने।"),
    "hook": "सूखा, हल्का, स्निग्ध, गरम, खट्टा, नमकीन: छह गुण।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "With what does line 2 say food and drink are taken when dense clouds rise?",
            ("With honey (सक्षौद्रम्)", "सक्षौद्रं: with honey."),
            [("With milk and boiled rice", "Not named in the line."),
             ("With ghee and rock salt", "Not named in the line."),
             ("With sugar and thick curd", "Not named in the line.")],
            "Line 2 says अन्नपानं सक्षौद्रम्: food and drink with honey.",
            "स + क्षौद्र = with honey."),
        match(1, "Match each quality of line 1 to its meaning.",
              [["परिशुष्क", "well dried"], ["लघु", "light"], ["उष्ण", "hot"], ["लवण", "salty"]],
              "Line 1 lists six qualities; these are four of them.",
              "परिशुष्क = well dried; लघु = light; उष्ण = hot; लवण = salty."),
        fill(2, "The word for 'unctuous' in line 1 is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("स्निग्ध", "स्निग्धम्"),
             "स्निग्ध is unctuous, the third quality of line 1.",
             "स्निग्ध is neuter accusative singular (printed स्निग्धम्), agreeing with the understood 'food' (भोजन) of line 1.",
             "स्निग्ध = unctuous."),
        multi("discriminate", 3, "Which three of these does line 1 name among the qualities?",
              [("sweet (मधुर)", "Sweet is not named in line 1."),
               ("light (लघु)", "Right: named in line 1."),
               ("sour (अम्ल)", "Right: named in line 1."),
               ("bitter (तिक्त)", "Bitter is not named in line 1."),
               ("unctuous (स्निग्ध)", "Right: named in line 1.")],
              [1, 2, 4],
              "Line 1 names well dried, light, unctuous, hot, sour and salty; light, sour and unctuous are among them.",
              "लघु · अम्ल · स्निग्ध."),
        order(4, "Put the six qualities in the order of line 1.",
              ["परिशुष्कम्", "लघु", "स्निग्धम्", "उष्ण", "अम्ल", "लवणम्"],
              "Line 1 runs: well dried, light, unctuous, hot, sour, salty.",
              "परिशुष्कम् · लघु · स्निग्धम् · उष्ण · अम्ल · लवणम्.", role="apply"),
        mcq("transfer", 5, "Which is the correct joined form of नील + उत्पल (blue lotus)?",
            ("नीलोत्पल", "अ + उ gives ओ, as in घन + उदये = घनोदये."),
            [("नीलुत्पल", "अ + उ is not simply shortened to उ."),
             ("नीलौत्पल", "अ + उ does not give औ."),
             ("नीलात्पल", "अ + उ does not give आ.")],
            "घन + उदये joins as घनोदये: a short अ meeting उ gives ओ.",
            "अ + उ → ओ.",
            teaches="A final अ before उ merges into ओ (घन + उदये = घनोदये, नील + उत्पल = नीलोत्पल)."),
    ],
}
NOTES_HI["61"] = ("विश्वास: मध्यम; डेटा की अनिश्चित सूची में ‘संस्रुत’ है (पुस्तक का ‘गाढ़ा’ शायद ‘छाना हुआ’ है), इसलिए उस पर प्रश्न नहीं बना। ‘प्रायः’ पहली अर्ध-पंक्ति से भी जुड़ सकता है। "
                  "‘घनोदये’ का अर्थ ‘घने बादल उठने पर’ या ‘बादल घने होने के समय’ दोनों संभव। उष्ण-अम्ल-लवण एक द्वंद्व है। संधि जाँची: उष्ण + अम्ल → उष्णाम्ल (अ + अ → आ); घन + उदये → घनोदये; अन्न + पानं में समास है।")
AIDS["61"] = {
    "diagram": {"groups": [
        {"label": "भोजन के गुण (पंक्ति १)",
         "items": ["परिशुष्क", "लघु", "स्निग्ध", "उष्ण", "अम्ल", "लवण"]}]},
    "chunks": "परिशुष्कं लघु स्निग्धम् | उष्णाम्ललवणं भजेत् ‖ प्रायोन्नपानं सक्षौद्रं | (संस्रुतं अनिश्चित) च घनोदये।",
    "sandhi": "अ + उ → ओ: घन + उदये → घनोदये। अ + अ → आ: उष्ण + अम्ल → उष्णाम्ल।",
    "frame": "पंक्ति १: छह गुण वाला भोजन लेना चाहिए · पंक्ति २: घने बादल उठने पर शहद सहित अन्न-पान (प्रायः का संबंध अनिश्चित)।",
}
IMAGE_SPECS[("61", "diagram")] = {
    "file": "ch4b05-food-qualities-61.svg",
    "alt": "List for unit 61: the six qualities of the food named in line 1, top to bottom in the verse's order: well dried, light, unctuous, hot, sour, salty.",
    "type": "split",
    "title": "श्लोक ६१: भोजन के गुण",
    "cols": [["भोजन के गुण (पंक्ति १)", ["परिशुष्क", "लघु", "स्निग्ध", "उष्ण", "अम्ल", "लवण"]]],
}

# ---------------------------------------------------------------- unit 62
AUTHORED["62"] = {
    "title": "असरीसृपभूबाष्प",
    "question": "What is said about the dwelling in line 2?",
    "rule": ("Line 2 describes a dwelling (भवनम्) with साग्नियान (meaning uncertain) and free from "
             "biting flies, mosquitoes and rats. निर्दंश is read for the printed निर्दश. Line 1 is a list of things it is free from."),
    "limits": ("There is no verb. Whether the negative in line 1 covers the whole list or only "
               "the first word is uncertain, and सागनियान is obscure (‘portable fire’ is "
               "a reading), so no question rests on those. निर्दश is printed for निर्दंश."),
    "explain_hi": ("इस इकाई में एक भवन (घर) का वर्णन है, क्रिया के बिना। पहली पंक्ति के समास में रेंगने वाले जीव, भूमि की भाप, "
                   "ठंडी हवा और फुहार हैं; ‘अ-’ पूरी सूची पर लगता है या नहीं, यह निश्चित नहीं, इसलिए उसपर प्रश्न नहीं बने। "
                   "दूसरी पंक्ति में भवन ‘साग्नियान’ (आग वाले साधन से युक्त; शब्द अस्पष्ट) है और डाँस, मच्छर तथा चूहों से रहित है। "
                   "‘सहित’ और ‘रहित’ का यह आमने-सामने का प्रयोग याद रखने लायक है।"),
    "hook": "घर: डाँस, मच्छर, चूहों से रहित; ‘साग्नियान’ (अर्थ अनिश्चित) से सहित।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "Which three does line 2 say the dwelling is free from?",
            ("Biting flies, mosquitoes and rats", "निर्दंश-मशक-उन्दुर: free from these three."),
            [("Venomous snakes, scorpions and wasps", "These are not named in line 2."),
             ("Heavy dust, smoke and loud noise", "These are not named in line 2."),
             ("Cold rain, hail and strong winds", "These are not named in line 2.")],
            "Line 2 ends with the compound read as निर्दंशमशकोन्दुरं (printed निर्दशमशकोंदुरं): free from biting flies, mosquitoes and rats.",
            "निः (without) + दंश (biting fly) · मशक (mosquito) · उन्दुर (rat)."),
        match(1, "Match each word to its meaning.",
              [["भवनम्", "dwelling"], ["दंश", "biting fly"], ["मशक", "mosquito"], ["उन्दुर", "rat"]],
              "Line 2 names the dwelling and the three things it is free from.",
              "भवनम् = dwelling; दंश = biting fly; मशक = mosquito; उन्दुर = rat."),
        mcq("extend", 2, "Which is the right sandhi result of निः + दंश (printed निर्दश)?",
            ("निर्दंश", "A visarga before a voiced consonant turns into र् after इ."),
            [("निदंश", "The visarga does not simply vanish."),
             ("निःदंश", "The visarga is not kept before द."),
             ("निसदंश", "A visarga before द does not become स्.")],
            "निः + दंश = निर्दंश: after इ the visarga becomes र् before the voiced द.",
            "Visarga after इ/उ + voiced sound → र्.",
            teaches="A visarga after इ or उ turns into र् before a voiced sound (निः + दंश = निर्दंश)."),
        mcq("discriminate", 3, "Which pair of words in line 2 stand as opposites, with and without?",
            ("साग्नियानं and निर्दंश…", "स- means with and निर्- means without, whatever अग्नियान exactly is."),
            [("भवनं and च side by side", "Neither word means with or without."),
             ("मशक and उन्दुर side by side", "Both are things the dwelling is free from."),
             ("च and उन्दुर side by side", "च means 'and'; उन्दुर is rat.")],
            "स- (with) + अग्नियान begin the first compound; निर्- (without) begins the second.",
            "स- = with; निर्- = without."),
        order(4, "Put the three things the dwelling is free from in the order of line 2.",
              ["दंश", "मशक", "उन्दुर"],
              "Line 2 ends: biting flies, mosquitoes, rats.",
              "दंश · मशक · उन्दुर.", role="apply"),
        mcq("transfer", 5, "In an invented phrase निर्जलं सरः, what is the lake?",
            ("Without water", "निर्- at the start means without, as in निर्दंश…"),
            [("Full of water", "Full of would be a word like जलपूर्ण."),
             ("Beside water", "Nothing in निर्- means beside."),
             ("Made of water", "Nothing in निर्- means made of.")],
            "निर्- (from निः) means without: निर्जल = without water, as निर्दंश… = without biting flies.",
            "निः/निर् + X = without X.",
            teaches="The prefix निः / निर् means 'without' (निर्दंश…, निर्जलम्)."),
    ],
}
NOTES_HI["62"] = ("विश्वास: मध्यम। डेटा की अनिश्चित सूची में ‘अग्नियान’ है: पुस्तक का हिंदी ‘आग और वाहन’ पढ़ता है, डेटा ‘आग ले जाने का साधन (अँगीठी)’ लेता है — इसलिए अर्थ पर प्रश्न नहीं बना। पहली पंक्ति में ‘अ-’ की पहुँच (केवल ‘सरीसृप’ पर या पूरी सूची पर) अनिश्चित; "
                  "डेटा ने पूरी सूची ली है, पर इस पर भी प्रश्न नहीं बना। ‘निर्दशमशकोंदुरं’ का ‘निर्दश’ संभवतः ‘निर्दंश’ है (अनुस्वार छूटा); प्रश्न ‘निर्दंश’ पर बने हैं। कोई क्रिया नहीं। "
                  "संधि जाँची: निः + दंश → निर्दंश; मशक + उन्दुर → मशकोन्दुर (अ + उ → ओ)।")
AIDS["62"] = {
    "chunks": "असरीसृपभूबाष्प | शीतमारुतशीकरं (पंक्ति १; ‘अ-’ की पहुँच अनिश्चित) ‖ साग्नियानं च भवनं | निर्दश[निर्दंश]मशकोंदुरं।",
    "sandhi": "विसर्ग (इ के बाद) + घोष → र्: निः + दंश → निर्दंश। अ + उ → ओ: मशक + उन्दुर → मशकोन्दुर।",
    "contrast": "स- (सहित: साग्नियानं) ↔ निर्- (रहित: निर्दंश…), दोनों दूसरी पंक्ति में।",
}

# ---------------------------------------------------------------- unit 63
AUTHORED["63"] = {
    "title": "प्रघर्षोद्वर्तनस्नान",
    "question": "What is the person fond of, and how does he go?",
    "rule": ("The person is fond of rubbing, ointment-rubbing, bathing, smoke and the scent of "
             "agaru; he should go with the foremost she-elephants, adorned with colourful clothes."),
    "limits": ("The verse does not say what is being ridden, nor the season; it says "
               "‘go with’ the she-elephants. धूमगंधागुरु may also be ‘fragrant smoke of agaru’; "
               "agaru is a drug name only."),
    "explain_hi": ("पहली पंक्ति में प्रेम के विषय गिनाए गए हैं: प्रघर्ष (रगड़ना), उद्वर्तन (उबटन), स्नान, धूम और अगरु की गंध। "
                   "दूसरी पंक्ति में क्रिया है: ‘यायात्’ (चले), श्रेष्ठ हथिनियों के साथ और रंग-बिरंगे वस्त्रों से सजा हुआ। "
                   "‘साथ चले’ शाब्दिक है; सवारी का उल्लेख श्लोक में नहीं है। ‘अगरु’ केवल नाम है।"),
    "hook": "रगड़ना, उबटन, स्नान, धूम, गंध; फिर हथिनियों के साथ, सजे वस्त्रों में।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "With whom does line 2 say the person should go?",
            ("With the foremost she-elephants", "यायात् करेणुमुख्याभिः: should go with the foremost she-elephants."),
            [("With the foremost horses of the guard", "Horses are not named in line 2."),
             ("With the foremost servants of the house", "Servants are not named in line 2."),
             ("With the foremost teachers of the school", "Teachers are not named in line 2.")],
            "Line 2 says यायात् करेणुमुख्याभिः: should go with the foremost she-elephants.",
            "करेणु = she-elephant; मुख्या = foremost; यायात् = should go."),
        match(1, "Match each word of the unit to its meaning.",
              [["स्नान", "bathing"], ["उद्वर्तन", "ointment-rubbing"],
               ["करेणु", "she-elephant"], ["चित्रवस्त्र", "colourful clothes"]],
              "These words give the person's tastes and dress.",
              "स्नान = bathing; उद्वर्तन = ointment-rubbing; करेणु = she-elephant; चित्रवस्त्र = colourful clothes."),
        mcq("extend", 2, "Which phrase means one should go to the village?",
            ("ग्रामं यायात्", "यायात् is the 'should go' form of the verb √या."),
            [("ग्रामं याति", "This is the plain present: 'goes to the village'."),
             ("ग्रामं ययौ", "This is a past form: 'went to the village'."),
             ("ग्रामं यातः", "यातः is a participle, 'gone'; it is not a 'should' form.")],
            "यायात् in line 2 is 'should go', so ग्रामं यायात् is 'should go to the village'.",
            "√या + optative → यायात् = should go.",
            teaches="The 'should go' form of √या is यायात्; the plain present is याति."),
        mcq("discriminate", 3, "Which list is the person said to be fond of in line 1?",
            ("Rubbing, ointment-rubbing, bathing and smoke-scent-agaru",
             "प्रघर्ष, उद्वर्तन, स्नान and धूमगंधागुरु are the items of line 1."),
            [("Singing, dancing, dice-play, wine-drinking and music-making", "None of these is in line 1."),
             ("Hunting, riding, archery, wrestling and other sports", "None of these is in line 1."),
             ("Reading, writing, speech, silence and daily prayers", "None of these is in line 1.")],
            "Line 1 ends with …प्रियः, 'fond of', after the list of tastes.",
            "प्रिय = fond of."),
        order(4, "Put these four parts of line 1 in the order of the verse.",
              ["प्रघर्ष", "उद्वर्तन", "स्नान", "धूमगंधागुरु"],
              "Line 1 runs: rubbing, ointment-rubbing, bathing, smoke-scent-agaru.",
              "प्रघर्ष · उद्वर्तन · स्नान · धूमगंधागुरु.", role="apply"),
        mcq("transfer", 5, "In an invented phrase वनविहारप्रियः, what is the person?",
            ("Fond of walking in the forest", "-प्रिय at the end means fond of the first part."),
            [("Dear to the forest and its trees", "Here the person is the one who is fond, not the one who is dear to it."),
             ("Afraid of the forest and its beasts", "Nothing in -प्रिय means afraid."),
             ("Lord of the forest and its trees", "Nothing in -प्रिय means lord.")],
            "…गंधागुरुप्रियः is 'fond of … agaru scent'; वनविहारप्रियः is 'fond of forest walks'.",
            "X-प्रिय (describing a person) = fond of X.",
            teaches="A compound ending in -प्रियः, describing a person, means 'fond of' the first part (…अगुरुप्रियः, वनविहारप्रियः)."),
    ],
}
NOTES_HI["63"] = ("विश्वास: उच्च। ‘धूमगंधागुरु’ को सूची की तरह (धूम, गंध, अगरु) लिया गया है; ‘अगरु का सुगंधित धूम’ भी संभव है। ‘यायात् करेणुमुख्याभिः’ शाब्दिक रूप से ‘श्रेष्ठ हथिनियों के साथ चले’ है; सवारी का उल्लेख नहीं। अगरु औषधि/काष्ठ का नाम है। "
                  "संधि जाँची: प्रघर्ष + उद्वर्तन → प्रघर्षोद्वर्तन (अ + उ → ओ); गंध + अगरु → गंधागुरु (अ + अ → आ); यायात् + करेणु में त् क् से पहले जैसा है।")
AIDS["63"] = {
    "chunks": "प्रघर्षोद्वर्तनस्नान | धूमगंधागुरुप्रियः ‖ यायात्करेणुमुख्याभिः | चित्रवस्त्रविभूषितः।",
    "sandhi": "अ + उ → ओ: प्रघर्ष + उद्वर्तन → प्रघर्षोद्वर्तन। अ + अ → आ: गंध + अगरु → गंधागुरु।",
    "frame": "पंक्ति १: किसका प्रेमी (रगड़, उबटन, स्नान, धूम, गंध, अगरु) · पंक्ति २: कैसे चले (हथिनियों के साथ, रंगीन वस्त्रों से सजा)।",
    "pegs": "मेरा बनाया चित्र: स्नान-उबटन-धूम के शौकीन व्यक्ति रंगीन वस्त्रों में हथिनियों के साथ चलते हैं। केवल याद के लिए।",
}

# ---------------------------------------------------------------- unit 64
AUTHORED["64"] = {
    "title": "नदीजलोदमंथाः",
    "question": "Which things does line 2 say to avoid?",
    "rule": ("Line 2 says one should avoid (त्यजेत्) frost, exercise and the sun's rays, "
             "among the listed items. Line 1 appears to name further things (its reading is "
             "conjectural)."),
    "limits": ("Line 1 is read as a list only after an assumed missing word, so no question "
               "depends on its construction; only line 2 is used. ‘पादचरण’ (going on foot) is uncertain and is not used. The verse "
               "gives no reason or dose."),
    "explain_hi": ("यह इकाई त्यागने योग्य बातों की सूची है। पहली पंक्ति में कुछ नाम दिखते हैं (नदीजल, उदमन्थ, मैथुन आदि), पर पाठ अनिश्चित है; "
                   "उसका समास-पाठ अनिश्चित है (छपाई में एक शब्द छूटा लगता है), इसलिए उसके ढाँचे पर प्रश्न नहीं बने। "
                   "दूसरी पंक्ति में पाला, व्यायाम और सूर्य की किरणों के साथ ‘त्यजेत्’ आता है, जिसका अर्थ है ‘छोड़ दे’। "
                   "‘पादचरण’ का अर्थ भी अनिश्चित है।"),
    "hook": "छोड़ने की सूची: पाला, व्यायाम, सूर्य की किरणें … त्यजेत्।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What does the verb त्यजेत् at the end of line 2 mean?",
            ("One should avoid", "त्यजेत् is the 'should' form of त्यज्: abandon, avoid."),
            [("One should praise", "त्यज् does not mean praise."),
             ("One should collect", "त्यज् does not mean collect."),
             ("One should measure", "त्यज् does not mean measure.")],
            "Line 2 ends with त्यजेत्, 'should avoid', which governs the items before it.",
            "त्यजेत् = should avoid."),
        match(1, "Match each word of line 2 to its meaning.",
              [["तुषार", "frost"], ["व्यायाम", "exercise"], ["अर्ककर", "sun's rays"], ["त्यजेत्", "should avoid"]],
              "Three items and the verb that governs them.",
              "तुषार = frost; व्यायाम = exercise; अर्ककर = sun's ray; त्यजेत् = should avoid."),
        mcq("extend", 2, "Which is the right split of अर्ककरांस्त्यजेत्?",
            ("अर्ककरान् + त्यजेत्", "न् + त् is written ंस्त्: a nasal and स् appear between."),
            [("अर्ककराः + त्यजेत्", "That would be written अर्ककरास्त्यजेत्, with no anusvara."),
             ("अर्ककरां + स्त्यजेत्", "स्त्यजेत् is not a word."),
             ("अर्ककर + स्त्यजेत्", "स्त्यजेत् is not a word.")],
            "अर्ककरान् (the sun's rays, accusative plural) + त्यजेत् (should avoid).",
            "-ान् + त् → -ांस्त्.",
            teaches="A final -न् before त् gives ंस्त् (अर्ककरान् + त्यजेत् = अर्ककरांस्त्यजेत्)."),
        multi("discriminate", 3, "Which three of these does line 2 say to avoid, leaving out the unclear word?",
              [("food (अन्न)", "Not named in this unit."),
               ("frost (तुषार)", "Right: the first item of line 2."),
               ("water (जल)", "Water belongs to line 1, not line 2."),
               ("exercise (व्यायाम)", "Right: an item of line 2."),
               ("the sun's rays (अर्ककर)", "Right: the last item of line 2.")],
              [1, 3, 4],
              "Line 2 names frost, exercise and the sun's rays before the verb त्यजेत्.",
              "तुषार · व्यायाम · अर्ककर → त्यजेत्."),
        order(4, "Put these words of line 2 in the order of the verse (the unclear middle word is left out).",
              ["तुषार", "व्यायाम", "अर्ककर", "त्यजेत्"],
              "Line 2 runs: frost, exercise, the sun's rays, should avoid.",
              "तुषार · व्यायाम · अर्ककर · त्यजेत्.", role="apply"),
        mcq("transfer", 5, "Which phrase means one should conquer anger?",
            ("क्रोधं जयेत्", "An accusative object plus a -एत् verb: 'should conquer anger'."),
            [("क्रोधं जयति", "This is the plain present: 'conquers anger'."),
             ("क्रोधमजयत्", "This is a past form: 'conquered anger'."),
             ("क्रोधः जयः", "Two nouns: 'anger, victory', no verb.")],
            "Like अर्ककरान् … त्यजेत्, the object is in the accusative and the verb ends in -एत्.",
            "Accusative object + -एत् verb = 'should do X'.",
            teaches="A command is an accusative object plus a verb in -एत्: क्रोधं जयेत् = 'one should conquer anger'."),
    ],
}
NOTES_HI["64"] = ("विश्वास: मध्यम। पहली पंक्ति (नदीजलोदमंथाःस्वप्नातिद्रवमैथुनं) में १५ अक्षर और एक अकेला विसर्ग है: ‘मंथाः स्वप्न’ का कोई स्पष्ट अन्वय नहीं बनता, इसलिए सुझाव है ‘अहःस्वप्न’ (दिन की नींद) जोड़कर द्वंद्व पढ़ा जाए (१६ अक्षर पूरे होते हैं)। यह सुधार अनुमान है, इसलिए पंक्ति १ की बनावट पर प्रश्न नहीं बना। "
                  "‘पादचरण’ पुस्तक में ‘ओस में भीगे पैर’ जैसा पढ़ा गया है, पर शब्दों में केवल ‘पैदल चलना’ है — अनिश्चित, प्रयोग नहीं हुआ। ‘तुषार’ = पाला/कुहरा। संधि जाँची: अर्ककरान् + त्यजेत् → अर्ककरांस्त्यजेत्; व्यायाम + अर्क → व्यायामार्क (अ + अ → आ)।")
AIDS["64"] = {
    "chunks": "नदीजलोदमंथाःस्वप्नातिद्रवमैथुनं (पंक्ति १ अनिश्चित) ‖ तुषारपादचरण | व्यायामार्ककरांस्त्यजेत्।",
    "sandhi": "न् + त् → ंस्त्: अर्ककरान् + त्यजेत् → अर्ककरांस्त्यजेत्। अ + अ → आ: व्यायाम + अर्क → व्यायामार्क।",
    "frame": "दूसरी पंक्ति: क्या छोड़े (पाला, [पादचरण: अनिश्चित], व्यायाम, सूर्य की किरणें) · कैसे कहा (त्यजेत्: छोड़ना चाहिए)।",
}

# ---------------------------------------------------------------- unit 65
AUTHORED["65"] = {
    "title": "शरदि व्योम शुभ्राभ्रं",
    "question": "How do the sky and the earth look in autumn?",
    "rule": ("In autumn (शरदि) the sky has white clouds and the earth is marked with a little "
             "mud, with conspicuous kāśa, saptāhva and kumuda, and rich in śāli rice."),
    "limits": ("The verse describes only; it gives no regimen. काश, सप्ताह्व are plant "
               "names, not identified; प्रकाश could also be a separate first member."),
    "explain_hi": ("यहाँ से शरद ऋतु का वर्णन शुरू होता है। पहली पंक्ति में आकाश श्वेत बादलों वाला है और पृथ्वी थोड़े कीचड़ से चिह्नित है। "
                   "दूसरी पंक्ति में पृथ्वी प्रकट काश, सप्ताह्व और कुमुद वाली तथा शालि धान से भरपूर है। "
                   "पहली पंक्ति आकाश और धरती का हाल देती है, दूसरी पंक्ति धरती के पौधों का। "
                   "काश और सप्ताह्व केवल नाम हैं।"),
    "hook": "शरद: श्वेत बादल, थोड़ा कीचड़, काश-कुमुद, शालि की भरमार।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "What kind of clouds does the sky have in autumn, according to line 1?",
            ("White clouds (शुभ्राभ्र)", "शुभ्र = white, अभ्र = cloud."),
            [("Black clouds of the storm", "शुभ्र means white, not black."),
             ("No clouds at all in the sky", "The compound names clouds the sky has."),
             ("Red clouds at sunset", "शुभ्र means white, not red.")],
            "शरदि व्योम शुभ्राभ्रं: in autumn the sky has white clouds.",
            "शुभ्र + अभ्र = white clouds."),
        match(1, "Match each word of line 1 to its meaning.",
              [["शरदि", "in autumn"], ["व्योम", "sky"], ["पंक", "mud"], ["मही", "earth"]],
              "These four words carry the picture of line 1.",
              "शरदि = in autumn; व्योम = sky; पंक = mud; मही = earth."),
        fill(2, "The word for 'earth' at the end of line 1 is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("मही", "mahī", "mahi"),
             "मही is the earth, the subject of both lines.",
             "मही is feminine, nominative singular; the participle किंचित्पंकांकिता before it agrees with it.",
             "मही = earth."),
        mcq("discriminate", 3, "Which sandhi result is right for शुभ्र + अभ्रं?",
            ("शुभ्राभ्रं", "अ + अ gives आ."),
            [("शुभ्रभ्रं", "The vowels do not simply drop."),
             ("शुभ्रोभ्रं", "अ + अ does not give ओ."),
             ("शुभ्रैभ्रं", "अ + अ does not give ऐ.")],
            "A short अ meeting अ merges into long आ: शुभ्राभ्रं.",
            "अ + अ → आ."),
        order(4, "Put these parts of line 1 in the order of the verse.",
              ["शरदि", "व्योम", "शुभ्राभ्रम्", "किंचित्पंकांकिता", "मही"],
              "Line 1 runs: in autumn, sky, with white clouds, marked with a little mud, earth.",
              "शरदि · व्योम · शुभ्राभ्रम् · किंचित्पंकांकिता · मही.", role="apply"),
        mcq("transfer", 5, "What does an invented phrase श्वेतपुष्पा लता mean?",
            ("A creeper with white flowers", "A feminine compound ending in the noun is 'having X', like शुभ्राभ्रं 'with white clouds'."),
            [("A white flower that is a creeper", "The compound describes the creeper, not a flower."),
             ("A creeper beside a white flower", "Nothing in the compound means beside."),
             ("A creeper that is not flowering", "Nothing in the compound means without flowers.")],
            "शुभ्राभ्रं (sky) = 'with white clouds'; श्वेतपुष्पा (creeper) = 'with white flowers'.",
            "Bahuvrīhi: adjective + noun, describes the noun it agrees with.",
            teaches="A compound of colour + noun can describe a noun as 'having' that thing (शुभ्राभ्रं व्योम, श्वेतपुष्पा लता)."),
    ],
}
NOTES_HI["65"] = ("विश्वास: उच्च। ‘प्रकाश’ को ‘प्रकट, स्पष्ट’ लेकर तीनों पौधों (काश, सप्ताह्व, कुमुद) का विशेषण माना गया है; वह अलग पहला पद भी हो सकता है। काश, सप्ताह्व पौधों के नाम हैं, पहचाने नहीं गए। "
                  "संधि जाँची: शुभ्र + अभ्रं → शुभ्राभ्रं (अ + अ → आ); पंक + अंकिता → पंकांकिता; किंचित् + पंक में त् प् से पहले वैसा ही रहता है। कोई पाठभेद नहीं।")
AIDS["65"] = {
    "diagram": {"groups": [
        {"label": "आकाश", "items": ["श्वेत बादल"]},
        {"label": "पृथ्वी", "items": ["थोड़ा कीचड़", "काश", "सप्ताह्व", "कुमुद", "शालि की भरमार"]}]},
    "chunks": "शरदि व्योम शुभ्राभ्रं | किंचित्पंकांकिता मही ‖ प्रकाशकाशसप्ताह्व- | कुमुदा शालिशालिनी।",
    "sandhi": "अ + अ → आ: शुभ्र + अभ्रं → शुभ्राभ्रं; पंक + अंकिता → पंकांकिता।",
    "frame": "ऋतु: शरद · आकाश: श्वेत बादल · धरती: थोड़ा कीचड़, काश, सप्ताह्व, कुमुद, शालि। शुभ्र + अभ्र = \"श्वेत बादलों वाला\" (बहुव्रीहि: जिसके पास वह)।",
}
IMAGE_SPECS[("65", "diagram")] = {
    "file": "ch4b05-autumn-65.svg",
    "alt": "Two columns for unit 65, autumn: the sky has white clouds; the earth has a little mud, kasha, saptahva, kumuda and abounds in shali rice.",
    "type": "split",
    "title": "श्लोक ६५: शरद",
    "cols": [["आकाश", ["श्वेत बादल"]],
             ["पृथ्वी", ["थोड़ा कीचड़", "काश", "सप्ताह्व", "कुमुद", "शालि की भरमार"]]],
}

# ---------------------------------------------------------------- unit 66
AUTHORED["66"] = {
    "title": "विक्षिप्ततीक्ष्णकिरणो",
    "question": "What follows from the departure of the cloud masses?",
    "rule": ("From the departure of the masses of clouds (मेघौघविगमात्) the sun scatters "
             "sharp rays; the directions are very clear and crowded with lines of krauñca birds."),
    "limits": ("‘बभ्रुवर्णो’ is disputed: it may describe the sun (tawny) or, if emended to "
               "बभ्रुवर्णा, the directions, so no question rests on it. क्रौंच is a bird "
               "name only."),
    "explain_hi": ("पहली पंक्ति में कारण और फल है: बादलों के समूह के हट जाने से (पंचमी: ‘विगमात्’) सूर्य तीखी किरणें बिखेरता है। "
                   "दूसरी पंक्ति में दिशाएँ अत्यंत निर्मल हैं और क्रौंच पक्षियों की पंक्तियों से भरी हैं। "
                   "‘बभ्रुवर्णो’ किसका विशेषण है, यह विवादित है (सूर्य का या दिशाओं का), इसलिए उस पर प्रश्न नहीं बना।"),
    "hook": "बादल हटे → सूर्य की तीखी किरणें; दिशाएँ निर्मल, क्रौंचों से भरी।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "Because of what does the sun scatter sharp rays, according to line 1?",
            ("The departure of the masses of clouds", "मेघौघविगमात्: from the departure of the cloud masses."),
            [("The arrival of the heavy masses of clouds", "विगम is departure, not arrival."),
             ("The rising of the river water", "No river is named in line 1."),
             ("The blowing of the cold wind", "No wind is named in line 1.")],
            "Line 1 gives the cause in the ablative: मेघौघविगमात्, then the effect: the sun scatters sharp rays.",
            "मेघौघविगमात् (from the departure of cloud masses) → रविः विक्षिप्ततीक्ष्णकिरणः."),
        match(1, "Match each word of the unit to its meaning.",
              [["रविः", "sun"], ["दिशः", "directions"], ["विमल", "clear"], ["क्रौंच", "krauñca bird"]],
              "These four words carry the two pictures of the unit.",
              "रविः = sun; दिशः = directions; विमल = clear; क्रौंच = krauñca bird."),
        mcq("extend", 2, "Which is the right sandhi result of विगमात् + रविः?",
            ("विगमाद्रविः", "A final त् before a voiced sound becomes द्."),
            [("विगमात्रविः", "The त् does not stay before the voiced र."),
             ("विगमाःरविः", "त् does not turn into a visarga here."),
             ("विगमान्रविः", "त् does not turn into न् here.")],
            "विगमात् + रविः joins as विगमाद्रविः: the final त् voices to द् before र.",
            "त् + voiced sound → द्.",
            teaches="A final त् before a voiced sound becomes द् (विगमात् + रविः = विगमाद्रविः)."),
        mcq("discriminate", 3, "Which phrase describes the directions in line 2?",
            ("Very clear, crowded with lines of krauñca birds",
             "अतिविमलाः क्रौंचमालाकुलाः दिशः."),
            [("Very dark and quite empty of any high flying birds", "विमल is clear, not dark."),
             ("Very clear and quite empty of birds and clouds", "आकुल means crowded with, not empty of."),
             ("Very dark and crowded with heavy rain clouds", "Neither dark nor clouds is in line 2.")],
            "Line 2 says the directions are very clear (अतिविमलाः) and crowded with lines of krauñca birds.",
            "अतिविमल + क्रौंचमालाकुल = very clear, crowded with krauñca lines."),
        order(4, "Put these words of the verse in order (words not listed are left out).",
              ["मेघौघविगमात्", "रविः", "अतिविमलाः", "क्रौंचमालाकुलाः", "दिशः"],
              "The verse runs: from the departure of cloud masses, the sun; very clear, crowded with krauñca lines, the directions.",
              "मेघौघविगमात् · रविः · अतिविमलाः · क्रौंचमालाकुलाः · दिशः.", role="apply"),
        mcq("transfer", 5, "Which invented phrase means: from the departure of winter?",
            ("शीतविगमात्", "-आत् is the ablative ending: 'from, because of'."),
            [("शीतविगमः", "This is the nominative: 'the departure of winter'."),
             ("शीतविगमे", "This is the locative: 'in the departure'."),
             ("शीतविगमम्", "This is the accusative: 'the departure' as an object.")],
            "मेघौघविगमात् is 'from the departure of the cloud masses'; the same -आत् ending gives शीतविगमात्.",
            "Ablative -आत् = 'from / because of'.",
            teaches="The ending -आत् (ablative singular of an -अ noun) gives the 'from / because of' sense (मेघौघविगमात्, शीतविगमात्)."),
    ],
}
NOTES_HI["66"] = ("विश्वास: मध्यम। डेटा की अनिश्चित सूची: ‘बभ्रुवर्णोऽतिविमलाः’ में एकवचन और बहुवचन का मेल नहीं बैठता। जैसा छपा है, ‘बभ्रुवर्णः’ सूर्य (रविः) का विशेषण है; "
                  "सुझाव ‘बभ्रुवर्णा अतिविमलाः’ (दिशाओं का) अलग पाठ होगा। इसलिए उस शब्द पर प्रश्न नहीं बना। ‘आकुला दिशः’ = ‘आकुलाः दिशः’ (विसर्ग घोष से पहले छूटा)। "
                  "संधि जाँची: मेघ + ओघ → मेघौघ (अ + ओ → औ); विगमात् + रविः → विगमाद्रविः; बभ्रुवर्णः + अति → बभ्रुवर्णोऽति।")
AIDS["66"] = {
    "diagram": {"groups": [
        {"label": "कारण → फल", "items": ["बादल हटे", "सूर्य की तीखी किरणें"]},
        {"label": "दिशाएँ", "items": ["अत्यंत निर्मल", "क्रौंच-पंक्तियों से भरी"]}]},
    "chunks": "विक्षिप्ततीक्ष्णकिरणो | मेघौघविगमाद्रविः ‖ (बभ्रुवर्णो विवादित) | अतिविमलाः क्रौंचमालाकुला दिशः।",
    "sandhi": "त् → द्: विगमात् + रविः → विगमाद्रविः। अ + ओ → औ: मेघ + ओघ → मेघौघ।",
    "frame": "कारण: बादल हटे · फल: सूर्य की तीखी किरणें · दिशाएँ: अत्यंत निर्मल, क्रौंच-पंक्तियों से भरी।",
}
IMAGE_SPECS[("66", "diagram")] = {
    "file": "ch4b05-clouds-depart-66.svg",
    "alt": "Two columns for unit 66: cause then effect (the clouds depart, then the sun's sharp rays); and the directions (very clear, crowded with krauncha lines).",
    "type": "split",
    "title": "श्लोक ६६: बादल हटे",
    "cols": [["कारण → फल", ["बादल हटे", "सूर्य की तीखी किरणें"]],
             ["दिशाएँ", ["अत्यंत निर्मल", "क्रौंच-पंक्तियों से भरी"]]],
}

# ---------------------------------------------------------------- unit 67
AUTHORED["67"] = {
    "title": "कमलांतरसल्हीन",
    "question": "What makes the lakes look the way they do here?",
    "rule": ("By the jostling of fish and flocks of swans among the lotuses the lakes (सरांसि) "
             "are high with breaking waves, and clear."),
    "limits": ("The printed word सल्हीन is a corrupt print for संलीन or सल्लीन ('hidden'), so "
               "nothing rests on it; whether it goes with the fish only or also the swans is open. "
               "तरंगभंगतुंग can also be 'raised high by the breaking of waves'."),
    "explain_hi": ("इस इकाई में सरोवरों का वर्णन है। पहली पंक्ति में कारण है: कमलों के बीच की मछलियों और हंसों के झुंडों की टकराहट (‘घट्टनैः’, तृतीया बहुवचन)। "
                   "दूसरी पंक्ति में फल है: सरोवर लहरों के टूटने से ऊँचे उठे हुए और निर्मल हैं (‘सरांसि’, नपुंसक बहुवचन)। "
                   "छपा ‘सल्हीन’ बिगड़ा शब्द है, इसलिए उस पर प्रश्न नहीं बना।"),
    "hook": "मछली और हंसों की टकराहट से लहरें, सरोवर निर्मल।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "Which two does line 1 name as jostling?",
            ("Fish and flocks of swans", "मीन and हंसौघ: fish and flocks of swans."),
            [("Frogs and flocks of cranes", "These are not named in line 1."),
             ("Bees and flocks of parrots", "These are not named in line 1."),
             ("Snakes and flocks of crows", "These are not named in line 1.")],
            "Line 1 ends with the jostling (घट्टनैः) of fish (मीन) and flocks of swans (हंसौघ).",
            "मीन = fish; हंस + ओघ = flock of swans; घट्टन = jostling."),
        match(1, "Match each word to its meaning.",
              [["कमल", "lotus"], ["मीन", "fish"], ["हंस", "swan"], ["सरस्", "lake"]],
              "Four plain words build the picture of the unit.",
              "कमल = lotus; मीन = fish; हंस = swan; सरस् = lake."),
        fill(2, "The word for 'swan' in line 1 is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("हंस"),
             "हंस is the swan, joined with ओघ in हंसौघ ('flock of swans').",
             "हंस + ओघ = हंसौघ: अ + ओ gives औ.",
             "हंस = swan."),
        mcq("discriminate", 3, "What does the ending of घट्टनैः tell us?",
            ("By the jostlings (instrumental plural)", "-ऐः is the instrumental plural ending of an -अ noun."),
            [("Of the many jostlings: genitive plural", "The genitive plural would end in -आनाम्."),
             ("In the many jostlings: locative plural", "The locative plural would end in -एषु."),
             ("The many jostlings: nominative plural", "The nominative plural would end in -आः or -आनि.")],
            "घट्टनैः means 'by the jostlings': the cause that makes the waves in line 2.",
            "-ऐः = instrumental plural = 'by'."),
        order(4, "Put these parts of line 1 in the order of the verse (the damaged word is left out).",
              ["कमलांतर", "मीन", "हंसौघ", "घट्टनैः"],
              "Line 1 runs: among the lotuses, fish, flocks of swans, by the jostling.",
              "कमलांतर · मीन · हंसौघ · घट्टनैः.", role="apply"),
        mcq("transfer", 5, "Which word agrees with the neuter plural पद्मानि (lotuses)?",
            ("विमलानि", "A neuter plural noun takes an adjective in -आनि, as सरांसि takes विमलानि."),
            [("विमलः", "This is masculine singular."),
             ("विमला", "This is feminine singular."),
             ("विमलम्", "This is neuter singular.")],
            "सरांसि (neuter plural) goes with विमलानि; पद्मानि (neuter plural) takes the same ending.",
            "Adjective agrees: neuter plural -आनि.",
            teaches="An adjective agrees with its noun in gender and number; for a neuter plural noun it ends in -आनि (सरांसि विमलानि)."),
    ],
}
NOTES_HI["67"] = ("विश्वास: मध्यम। छपा ‘सल्हीन’ शब्द नहीं है; संभवतः ‘संलीन’ या ‘सल्लीन’ (छिपा हुआ) है (ल्ह का भ्रम) — इसलिए उस पर प्रश्न नहीं बना। ‘संलीन’ केवल मछलियों का विशेषण है या हंसों का भी, खुला है; डेटा ने मछलियों के साथ लिया है। "
                  "‘तरंगभंगतुंग’ का दूसरा अर्थ ‘लहरों के टूटने से ऊँचे उठे’ भी संभव है। संधि जाँची: हंस + ओघ → हंसौघ (अ + ओ → औ); कमल + अंतर → कमलांतर; सरस् का नपुंसक बहुवचन सरांसि।")
AIDS["67"] = {
    "chunks": "कमलांतर… (सल्हीन दूषित) | मीनहंसौघघट्टनैः ‖ तरंगभंगतुंगानि | सरांसि विमलानि च।",
    "sandhi": "अ + ओ → औ: हंस + ओघ → हंसौघ। सरस् का नपुंसक बहुवचन: सरांसि। घट्टनैः = तृतीया बहुवचन (-ऐः): ‘से’।",
    "frame": "सरांसि (नपुंसक बहुवचन) → विमलानि (-आनि)। कारण (पंक्ति १): कमलों के बीच मछलियों और हंसों के झुंडों की टकराहट · फल (पंक्ति २): सरोवर लहरों से ऊँचे और निर्मल।",
}
