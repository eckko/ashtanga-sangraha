from helpers import mcq, match, order, fill, multi, accepts

AUTHORED = {}

# ---------------------------------------------------------------- unit 1
AUTHORED["1"] = {
    "title": "श्रीगणेशाय नमः",
    "question": "To whom does the opening line of the Vamanakalpa chapter offer salutation?",
    "rule": ("The chapter opens with श्रीगणेशाय नमः, 'salutation to the revered Gaṇeśa'. "
             "गणेशाय is dative ('to Gaṇeśa'); नमः is 'salutation'; श्री marks respect."),
    "limits": ("A printed opening line of the edition; it teaches nothing about emesis. Whether श्री and "
               "गणेशाय should be printed as one compound is an open reviewer point, so no question rests on it."),
    "explain_hi": ("अध्याय एक मंगल-वाक्य से आरम्भ होता है: ‘श्रीगणेशाय नमः’, यानी श्रीगणेश को नमस्कार। "
                   "‘गणेशाय’ चतुर्थी विभक्ति एकवचन है, जिसका अर्थ है ‘गणेश को’ या ‘गणेश के लिए’। "
                   "‘नमः’ का अर्थ है नमस्कार, और ‘श्री’ आदर तथा मंगल का सूचक विशेषण है। "
                   "यह पंक्ति छपे संस्करण का आरम्भ है; इसमें वमन की कोई शिक्षा नहीं है।"),
    "hook": "पहले गणेश को नमः, फिर वमनकल्प।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "To whom does the opening line श्रीगणेशाय नमः offer salutation?",
            ("To the revered Gaṇeśa", "गणेशाय = to Gaṇeśa; श्री = revered."),
            [("To the sage Ātreya", "Ātreya is named in unit 3 as a speaker, not saluted here."),
             ("To the student", "No student is named in the line."),
             ("To the madana fruit", "The madana fruit appears from unit 4 on, not in this line.")],
            "श्रीगणेशाय नमः = salutation to the revered Gaṇeśa.",
            "Dative name + नमः = salutation to that one."),
        match(1, "Match each word of the opening line to its meaning.",
              [["श्री", "revered, auspicious"], ["गणेशाय", "to Gaṇeśa"], ["नमः", "salutation"]],
              "Three words: a mark of respect, the one honoured (dative), and the salutation.",
              "श्री = revered; गणेशाय = to Gaṇeśa; नमः = salutation."),
        mcq("extend", 2, "What does the ending -आय in गणेशाय show here?",
            ("The dative: 'to Gaṇeśa'", "Masculine -अ stems take -आय in the dative singular; with नमः it names the one honoured."),
            [("The genitive: 'of Gaṇeśa'", "The genitive would be गणेशस्य."),
             ("The locative: 'in Gaṇeśa'", "The locative would be गणेशे."),
             ("The subject: 'Gaṇeśa'", "The subject form would be गणेशः.")],
            "गणेशाय is m. dat. sg.: the salutation is offered to Gaṇeśa.",
            "With नमः the one honoured stands in the dative.",
            teaches="With नमः the one honoured stands in the dative: गणेशाय = to Gaṇeśa."),
        mcq("discriminate", 3, "Which English rendering of श्रीगणेशाय नमः has one wrong word?",
            ("Salutation from the revered Gaṇeśa", "Wrong: गणेशाय is dative, 'to', not 'from'."),
            [("Salutation to the revered Gaṇeśa", "Correct: this is the card's rendering."),
             ("Homage to the revered Gaṇeśa", "Correct: नमः can be rendered 'homage'."),
             ("To the revered Gaṇeśa, salutation", "Correct: only the word order differs.")],
            "The dative गणेशाय means 'to Gaṇeśa'; 'from' would need another case.",
            "-आय (dative) = to / for."),
        fill(4, "The word of the line that means 'salutation' is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("नमः"),
             "नमः = salutation, homage; it closes the line श्रीगणेशाय नमः.",
             "नमः means salutation; the one saluted stands before it in the dative.",
             "नमः = salutation.", role="apply"),
        mcq("transfer", 5, "On the pattern of गणेशाय नमः, which phrase means salutation to Śiva?",
            ("शिवाय नमः", "शिव is an -अ stem like गणेश; its dative is शिवाय."),
            [("शिवस्य नमः", "शिवस्य is the genitive, 'of Śiva'."),
             ("शिवे नमः", "शिवे is the locative, 'in Śiva'."),
             ("शिवः नमः", "शिवः is the subject form, not 'to Śiva'.")],
            "Same pattern: dative of the name + नमः.",
            "-अ stem dative singular = -आय (गणेशाय, शिवाय).",
            teaches="The dative singular of an -अ stem ends in -आय: गणेशाय, शिवाय; it goes with नमः."),
    ],
}

# ---------------------------------------------------------------- unit 2
AUTHORED["2"] = {
    "title": "अथातो वमनकल्पं व्याख्यास्यामः",
    "question": "What does the opening formula announce as the topic of this chapter?",
    "rule": ("Now, therefore, we shall explain the Vamanakalpa, the formulations for emesis (vamana). "
             "अथातो = अथ + अतः; व्याख्यास्यामः is 1st person plural future, 'we shall explain'."),
    "limits": ("The formula names the topic only: no drug, dose or method. It does not say who 'we' are; "
               "the next unit says that Ātreya and the other great sages spoke thus."),
    "explain_hi": ("यह अध्याय का आरम्भिक सूत्र है: ‘अथातो वमनकल्पं व्याख्यास्यामः’, यानी अब इसलिए हम वमनकल्प की व्याख्या करेंगे। "
                   "‘अथातो’ में दो शब्द हैं: अथ (अब) और अतः (इसलिए); अः के बाद घोष व्यंजन आने पर वह ओ बन जाता है। "
                   "‘वमनकल्प’ का अर्थ है वमन (उल्टी कराने की चिकित्सा) के कल्प, यानी योग। "
                   "‘व्याख्यास्यामः’ भविष्यत् काल, उत्तम पुरुष बहुवचन है: ‘हम व्याख्या करेंगे’। "
                   "इस पंक्ति में केवल विषय का नाम है, कोई द्रव्य या विधि नहीं।"),
    "hook": "अथ-अतः: अब, इसलिए; विषय: वमन के कल्प।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What topic does the opening formula of this chapter announce?",
            ("The formulations for emesis", "वमनकल्पम् = the Vamanakalpa, formulations (कल्प) for emesis (वमन)."),
            [("The formulations for purgation", "Purgation is not named; वमन is emesis."),
             ("The rules of the daily routine", "The daily routine is not the topic named here."),
             ("The signs of the six seasons", "No season is named in this line.")],
            "अथातो वमनकल्पं व्याख्यास्यामः = now, therefore, we shall explain the Vamanakalpa.",
            "वमनकल्प = formulations for emesis."),
        order(1, "Put these words of the formula in the order of the line.",
              ["अथ", "अतः", "वमनकल्पम्", "व्याख्यास्यामः"],
              "The line runs: now, therefore, the Vamanakalpa, we shall explain.",
              "अथ · अतः · वमनकल्पम् · व्याख्यास्यामः."),
        match(2, "Match each word of the formula to its meaning.",
              [["अथ", "now"], ["अतः", "therefore"], ["वमनकल्पम्", "the formulations for emesis"],
               ["व्याख्यास्यामः", "we shall explain"]],
              "Two particles, the topic (object) and the verb.",
              "अथ = now; अतः = therefore; वमनकल्पम् = emesis formulations; व्याख्यास्यामः = we shall explain.",
              role="extend",
              teaches="The opening formula has four parts: अथ (now), अतः (therefore), the topic, and व्याख्यास्यामः (we shall explain)."),
        mcq("discriminate", 3, "Which is the right split of अथातो, standing before वमनकल्पम्?",
            ("अथ + अतः", "अ + अ → आ (अथात-), and अः before a voiced consonant (व) becomes ओ."),
            [("अथा + तः", "Neither अथा nor तः is a word of the card."),
             ("अथ + अत", "A final -अ would stay -अ; the ओ comes from -अः."),
             ("अथः + तो", "These pieces are not the words अथ and अतः.")],
            "अथ (now) + अतः (therefore) = अथातः, written अथातो before व.",
            "-अः before a voiced consonant → -ओ."),
        mcq("apply", 4, "How does the card's data label the verb व्याख्यास्यामः?",
            ("Future, 1st plural: 'we shall explain'", "The data label is 1 pl. fut. of वि-आ-√ख्या."),
            [("Present, 1st plural: 'we explain'", "The -स्य- marks the future, not the present."),
             ("Past, 3rd plural: 'they explained'", "The ending -आमः is 1st person plural, 'we'."),
             ("Optative, 3rd sg: 'one should explain'", "An optative would end in -एत्.")],
            "व्याख्यास्यामः = we shall explain (future, 1st person plural).",
            "-स्यामः = 1st person plural future, 'we shall'."),
        mcq("transfer", 5, "Join a new example, ततः + वदति (then he speaks). Which is right?",
            ("ततो वदति", "-अः before a voiced consonant (व) becomes -ओ, as in अथातो वमन-."),
            [("ततः वदति", "The visarga after अ does not stay before a voiced consonant."),
             ("ततर् वदति", "The visarga becomes र् only after vowels other than अ/आ."),
             ("ततश् वदति", "श् comes before च, छ or श, not before व.")],
            "Same rule as अतः + वमन- = अतो वमन-.",
            "-अः + voiced consonant → -ओ.",
            teaches="-अः before a voiced consonant becomes -ओ: अतः + वमन- = अतो वमन-; ततः + वदति = ततो वदति."),
    ],
}

# ---------------------------------------------------------------- unit 3
AUTHORED["3"] = {
    "title": "इति ह स्माहुरात्रेयादयो महर्षयः",
    "question": "Whom does this line name as the speakers of what follows?",
    "rule": ("Thus indeed said Ātreya and the other great sages. स्माहुः = स्म + आहुः (स्म gives the past sense: "
             "'said'); महर्षयः = महा + ऋषयः, great sages."),
    "limits": ("The line names Ātreya and 'the others' (आदयः) without listing them. How आत्रेयादयः is labelled "
               "(one compound or two words) is an open reviewer point; no question uses that label."),
    "explain_hi": ("यह पंक्ति अध्याय की परम्परागत भूमिका है: ‘इति ह स्माहुरात्रेयादयो महर्षयः’, यानी ऐसा आत्रेय आदि महर्षियों ने कहा। "
                   "‘ह’ बल देता है, और ‘स्म’ के साथ ‘आहुः’ भूतकाल का अर्थ देता है: ‘कहा’। "
                   "‘आत्रेय’ एक ऋषि का नाम माना गया है; ‘आदयः’ का अर्थ है ‘आदि’, यानी और दूसरे। "
                   "‘महर्षयः’ में महा + ऋषयः की सन्धि है (आ + ऋ → अर्)।"),
    "hook": "इति ह स्म आहुः: ऐसा कहा था, आत्रेय आदि महर्षियों ने।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "Whom does the line name as having said this?",
            ("Ātreya and the other great sages", "आत्रेयादयो महर्षयः = Ātreya and the other great sages."),
            [("Gaṇeśa and the other deities", "Gaṇeśa is saluted in unit 1; he is not the speaker here."),
             ("The pupils of the physician", "No pupils are named in the line."),
             ("The kings of an earlier age", "No king is named in the line.")],
            "इति ह स्माहुः = thus indeed (they) said; the speakers are Ātreya and the other great sages.",
            "आत्रेय-आदयः महर्षयः = Ātreya and the other great sages."),
        match(1, "Match each word of the line to its meaning.",
              [["इति", "thus"], ["ह", "indeed"], ["आहुः", "said"], ["महर्षयः", "great sages"]],
              "इति and ह frame the report; आहुः is the verb; महर्षयः the speakers.",
              "इति = thus; ह = indeed; आहुः = said; महर्षयः = great sages."),
        order(2, "Put these words in the order of the line.",
              ["इति", "ह", "स्म", "आहुः", "आत्रेयादयः", "महर्षयः"],
              "The line runs: thus, indeed, (past), said, Ātreya and others, great sages.",
              "इति · ह · स्म · आहुः · आत्रेयादयः · महर्षयः.",
              role="extend",
              teaches="The formula is इति ह स्म आहुः followed by the speakers: Ātreya and the other great sages."),
        mcq("discriminate", 3, "Which is the right split of स्माहुरात्रेय-?",
            ("स्म + आहुः + आत्रेय-", "अ + आ → आ (स्माहु-); the visarga after उ becomes र् before a vowel."),
            [("स्मा + हुः + आत्रेय-", "स्मा and हुः are not words of the card."),
             ("स्म + आहु + रात्रेय-", "The name is आत्रेय; the र् is the visarga of आहुः."),
             ("स्मः + आहुः + आत्रेय-", "स्म is a particle with no visarga.")],
            "स्म (past sense) + आहुः (said) + आत्रेय (the sage's name).",
            "Visarga after इ/उ before a vowel → र्."),
        mcq("apply", 4, "What does the particle स्म add to आहुः in this line?",
            ("A past sense: 'said'", "The data glosses स्म as a particle with past sense."),
            [("A command: 'say!'", "A command would need an imperative form."),
             ("A future sense: 'will say'", "स्म points to the past, not the future."),
             ("A negation: 'did not say'", "Negation would need न.")],
            "ह स्म आहुः is a narrative formula: 'indeed (they) said'.",
            "स्म with a verb = past sense."),
        mcq("transfer", 5, "Join a new example, देव + ऋषिः (divine sage), as one word. Which is right?",
            ("देवर्षिः", "अ/आ + ऋ → अर्, as in महा + ऋषयः = महर्षयः."),
            [("देवऋषिः", "The two vowels are not left side by side."),
             ("देवार्षिः", "अ + ऋ does not give a long आर्."),
             ("देवोर्षिः", "ओ is not made from अ + ऋ.")],
            "Same rule as महा + ऋषयः = महर्षयः.",
            "अ/आ + ऋ → अर्.",
            teaches="अ or आ before ऋ becomes अर्: महा + ऋषयः = महर्षयः; देव + ऋषिः = देवर्षिः."),
    ],
}

# ---------------------------------------------------------------- unit 4
AUTHORED["4"] = {
    "title": "वमनद्रव्याणां श्रेष्ठानि",
    "question": "Which fruits does unit 4 call the best among the substances for emesis?",
    "rule": ("Among emetic substances the fruits of madana (emetic nut), jīmūtaka, ikṣvāku, kukkṛtikā, śātakī and "
             "kuṭaja (kurchi) are the best. The middle names are damaged in the scan."),
    "limits": ("Low confidence: ikṣvāku is a guess for printed कक्ष्वेवाकु; kukkṛtikā and śātakī are doubtful readings. "
               "Identifications: madana Randia spinosa, kuṭaja Holarrhena pubescens ('standard', firm); jīmūtaka Luffa "
               "echinata (probable); ikṣvāku disputed; the rest unidentified. No dose is given."),
    "explain_hi": ("यह इकाई वमन के श्रेष्ठ द्रव्यों की सूची देती है: इन पौधों के फल वमन के लिए सबसे अच्छे हैं। "
                   "सूची मदन यानी मैनफल से शुरू होती है और कुटज यानी कुड़ा पर समाप्त होती है; ये दोनों पहचानें मानक हैं। "
                   "जीमूतक की पहचान बन्दाल सम्भावित है। "
                   "बीच के नाम स्कैन में क्षतिग्रस्त हैं: ‘इक्ष्वाकु’ छपे ‘कक्ष्वेवाकु’ का अनुमानित पाठ है (पहचान कड़वी लौकी, विवादित), "
                   "और कुक्कृतिका तथा शातकी के पाठ भी संदिग्ध हैं, उनकी पहचान अज्ञात है। "
                   "यहाँ न मात्रा है, न विधि; केवल श्रेष्ठ फलों के नाम।"),
    "hook": "मदन से कुटज तक: वमन के श्रेष्ठ फल।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "Which part of the named plants does unit 4 call best for emesis?",
            ("Their fruits (फलानि)", "The long compound ends in -फलानि: the fruits of these plants."),
            [("Their roots (मूलानि)", "Roots are not named in the unit."),
             ("Their leaves (पत्राणि)", "Leaves are not named in the unit."),
             ("Their barks (त्वचः)", "Bark is not named in the unit.")],
            "मदन…कुटजफलानि च श्रेष्ठानि = the fruits of madana … kuṭaja are the best.",
            "-फलानि = fruits."),
        match(1, "Match each word of unit 4 to its meaning or identification on the card.",
              [["मदन", "emetic nut (standard)"], ["कुटज", "kurchi (standard)"],
               ["जीमूतक", "Luffa echinata (probable)"], ["श्रेष्ठानि", "the best"]],
              "Two firm identifications, one probable, and the predicate 'best'.",
              "मदन = emetic nut; कुटज = kurchi; जीमूतक = Luffa echinata (probable); श्रेष्ठानि = best."),
        order(2, "Put these clear words of unit 4 in the order of the text.",
              ["वमनद्रव्याणाम्", "मदन", "जीमूतक", "कुटज", "श्रेष्ठानि"],
              "The unit opens 'among emetic substances', lists madana first and kuṭaja last, and ends with 'best'.",
              "वमनद्रव्याणाम् · मदन · जीमूतक … कुटज · श्रेष्ठानि.",
              role="extend",
              teaches="The list of best emetic fruits begins with madana (then jīmūtaka) and ends with kuṭaja."),
        multi("discriminate", 3, "Which two identifications does the card mark as standard (firm)?",
              [("madana = emetic nut, Randia spinosa", "Right: tagged standard."),
               ("kuṭaja = kurchi, Holarrhena pubescens", "Right: tagged standard."),
               ("jīmūtaka = Luffa echinata", "Not standard: tagged probable."),
               ("ikṣvāku = bitter bottle gourd", "Not standard: disputed, and the reading itself is a guess.")],
              [0, 1],
              "Only madana and kuṭaja are firm; jīmūtaka is probable, ikṣvāku disputed, kukkṛtikā and śātakī unidentified.",
              "Standard: madana, kuṭaja. Probable: jīmūtaka. Disputed: ikṣvāku."),
        mcq("apply", 4, "A student says unit 4 gives the dose of each fruit. What does the unit state?",
            ("That these fruits are the best emetics", "The unit only ranks them: श्रेष्ठानि, the best."),
            [("The dose of each fruit, in pala", "No measure appears in the unit."),
             ("The month for gathering each fruit", "Gathering is described later (unit 9), not here."),
             ("How to dry the fruits in the sun", "Drying comes in unit 10, not here.")],
            "Unit 4 is a ranking: the best emetic fruits. Doses and methods are not in it.",
            "X-द्रव्याणाम् … श्रेष्ठानि = among X substances, these are the best."),
        mcq("transfer", 5, "In an invented sentence पुष्पाणां कमलं श्रेष्ठम्, what does पुष्पाणाम् mean, as वमनद्रव्याणाम् does here?",
            ("Among flowers", "A genitive plural with श्रेष्ठ picks the best out of a group."),
            [("With flowers", "'With' would need the instrumental (पुष्पैः)."),
             ("For the flowers", "'For' would need the dative (पुष्पेभ्यः)."),
             ("From the flowers", "'From' would need the ablative (पुष्पेभ्यः).")],
            "वमनद्रव्याणाम् = among emetic substances; पुष्पाणाम् = among flowers.",
            "Genitive plural + श्रेष्ठ = the best among …",
            teaches="A genitive plural beside श्रेष्ठ means 'among': वमनद्रव्याणाम् … श्रेष्ठानि = the best among emetic substances."),
    ],
}

# ---------------------------------------------------------------- unit 5
AUTHORED["5"] = {
    "title": "तेष्वपि मदनफलम्",
    "question": "Which single fruit does unit 5 pick out from the best emetic fruits?",
    "rule": ("Among these too (the best emetic fruits of unit 4), the madana (emetic nut) fruit. "
             "The unit has no verb: the sense 'best' carries over from unit 4."),
    "limits": ("Elliptical: the unit itself does not say 'best'; the data carries that sense over from unit 4. "
               "It gives no reason why madana is chosen and no dose."),
    "explain_hi": ("यह छोटी इकाई पिछली सूची से एक फल चुनती है: ‘तेष्वपि मदनफलम्’, यानी उनमें भी मदनफल यानी मैनफल। "
                   "‘तेषु’ (उनमें) पिछली इकाई के श्रेष्ठ फलों की ओर संकेत करता है, और ‘अपि’ का अर्थ है ‘भी’। "
                   "इस इकाई में कोई क्रिया नहीं है; ‘श्रेष्ठ’ का भाव पिछली इकाई से आता है। "
                   "मदनफल को क्यों चुना गया, इसका कारण यहाँ नहीं दिया गया।"),
    "hook": "श्रेष्ठों में भी श्रेष्ठ: मदनफल।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "Which fruit does unit 5 single out from the best emetic fruits?",
            ("मदनफल (emetic nut)", "मदनफलम् = the madana fruit."),
            [("कुटजफल (kurchi)", "Kuṭaja closes the list of unit 4; unit 5 names madana."),
             ("जीमूतक (Luffa echinata)", "Jīmūtaka is in the list, but unit 5 names madana."),
             ("शातकी (unidentified)", "Śātakī is a doubtful name of unit 4, not picked here.")],
            "तेष्वपि मदनफलम् = among these too, the madana fruit.",
            "तेषु (among these) अपि (too) मदनफलम्."),
        match(1, "Match each word of unit 5 to its meaning.",
              [["तेषु", "among these"], ["अपि", "too, even"], ["मदनफलम्", "the madana fruit"]],
              "तेषु points back to the list of unit 4; अपि marks 'even among them'.",
              "तेषु = among these; अपि = too; मदनफलम् = madana fruit."),
        fill(2, "तेषु + अपि join in unit 5 as ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("तेष्वपि"),
             "Final उ before a different vowel becomes व्: तेषु + अपि = तेष्वपि.",
             "Final उ before a different vowel becomes व्: तेषु + अपि = तेष्वपि.",
             "उ + different vowel → व् + vowel."),
        mcq("discriminate", 3, "Which is the right split of तेष्वपि?",
            ("तेषु + अपि", "उ before अ becomes व्: तेष्व + पि."),
            [("तेष + वपि", "वपि is not a word of the card."),
             ("तेषो + अपि", "ओ + अ would give तेषोऽपि."),
             ("तेषू + अपि", "A long ऊ would also become व्, but the locative plural is तेषु, with short उ.")],
            "तेषु (loc. pl., among these) + अपि (too).",
            "उ + different vowel → व्."),
        mcq("apply", 4, "Unit 5 has no verb. What sense does the data carry over from unit 4?",
            ("That madana fruit is the best", "Unit 4 ends with श्रेष्ठानि, the best; unit 5 narrows it to madana."),
            [("That madana fruit is harmful", "Harm is not mentioned in either unit."),
             ("That madana fruit must be boiled", "Boiling is not mentioned in either unit."),
             ("That madana fruit is hard to find", "Rarity is not mentioned in either unit.")],
            "The predicate 'best' of unit 4 is understood: among the best, madana fruit (is best).",
            "An elliptical unit takes its predicate from the unit before."),
        mcq("transfer", 5, "Join a new example, गुरुषु + अपि (even among teachers). Which is right?",
            ("गुरुष्वपि", "उ before a different vowel becomes व्, as in तेष्वपि."),
            [("गुरुषपि", "The उ cannot simply drop."),
             ("गुरुषोऽपि", "That would need -ओ, not -उ, before अपि."),
             ("गुरुषूपि", "उ + अ does not give ऊ.")],
            "Same rule as तेषु + अपि = तेष्वपि.",
            "उ + different vowel → व् + vowel.",
            teaches="Final उ before a different vowel becomes व्: तेषु + अपि = तेष्वपि; गुरुषु + अपि = गुरुष्वपि."),
    ],
}

# ---------------------------------------------------------------- unit 6
AUTHORED["6"] = {
    "title": "दोषदृष्यादिवशाच्चैषाम्",
    "question": "On what does unit 6 make the precedence among these drugs and preparations depend?",
    "rule": ("The precedence (प्राधान्यम्) among these drugs and among these preparations is according to "
             "(वशात्, 'by the sway of') doṣa, dūṣya (what is vitiated) and the like."),
    "limits": ("Printed दृष्य is read as दूष्य, a proofreading correction. 'The like' (आदि) is not spelled out. "
               "एषाम् as 'of these (drugs)' is the data's reading; the verb 'is' is supplied. The unit names no drug for any case."),
    "explain_hi": ("यह इकाई बताती है कि श्रेष्ठता स्थिर नहीं है। इन द्रव्यों में और इनसे बनाए गए योगों में किसकी प्रधानता हो, "
                   "यह दोष, दूष्य आदि के वश से तय होता है। ‘दूष्य’ का अर्थ है वह जो दूषित होता है; छपा ‘दृष्य’ यहाँ ‘दूष्य’ पढ़ा गया है। "
                   "‘वशात्’ का अर्थ है ‘के वश से’, यानी उनके अनुसार। "
                   "मूल में क्रिया नहीं है, ‘होता है’ जोड़ा गया है; कौन-सा द्रव्य किस स्थिति में पहला है, यह यहाँ नहीं कहा गया।"),
    "hook": "कौन प्रधान? दोष-दूष्य तय करते हैं।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "According to unit 6, what decides the precedence among these drugs and preparations?",
            ("Doṣa, dūṣya and the like", "दोष-दूष्य-आदि-वशात् = by the sway of doṣa, dūṣya and the like."),
            [("The price of each drug", "Price is not mentioned."),
             ("The colour of each fruit", "Colour is not mentioned in this unit."),
             ("The age of each plant", "The age of the plant is not mentioned.")],
            "…वशात् … प्राधान्यम् = the precedence is by the sway of doṣa, dūṣya and the like.",
            "Precedence follows doṣa, dūṣya and the like."),
        match(1, "Match each word of unit 6 to its meaning.",
              [["प्राधान्यम्", "precedence, primacy"], ["वशात्", "by the sway of"],
               ["एषाम्", "of these"], ["कल्पनानाम्", "of preparations"]],
              "The unit says whose precedence (of these, of preparations) and by what (the sway of doṣa etc.).",
              "प्राधान्यम् = precedence; वशात् = by the sway of; एषाम् = of these; कल्पनानाम् = of preparations."),
        order(2, "Put these words of unit 6 in the order of the text.",
              ["वशात्", "च", "एषाम्", "एतत्कल्पनानाम्", "प्राधान्यम्"],
              "The cause comes first (…वशात्), then whose precedence, then the word प्राधान्यम्.",
              "वशात् · च · एषाम् · एतत्कल्पनानाम् · प्राधान्यम्.",
              role="extend",
              teaches="Unit 6 puts the deciding factor first (…वशात्) and ends with प्राधान्यम्, precedence."),
        mcq("discriminate", 3, "Which is the right split of वशाच्चैषाम्?",
            ("वशात् + च + एषाम्", "त् before च becomes च् (च्च); अ + ए → ऐ (चैषाम्)."),
            [("वशा + च्च + एषाम्", "च्च is not a word."),
             ("वशात् + चै + षाम्", "चै and षाम् are not words of the card."),
             ("वशः + च + एषाम्", "A visarga before च would become श्: वशश्च.")],
            "वशात् (by the sway of) + च (and) + एषाम् (of these).",
            "त् + च → च्च; अ + ए → ऐ."),
        mcq("apply", 4, "A physician must choose between two emetic preparations. By unit 6, what should guide the choice?",
            ("The doṣa, dūṣya and the like in the case", "Precedence is by the sway of doṣa, dūṣya and the like."),
            [("Madana in every case, whatever the doṣa", "Unit 6 makes precedence depend on doṣa etc., not fixed."),
             ("Whichever preparation costs less", "Cost is not mentioned."),
             ("Whichever drug comes first in a list", "List order is not given as the rule.")],
            "Unit 6: precedence among drugs and preparations depends on doṣa, dūṣya and the like.",
            "दोष-दूष्य-आदि-वशात् प्राधान्यम्."),
        mcq("transfer", 5, "Join a new example, तस्मात् + च (and therefore). Which is right?",
            ("तस्माच्च", "त् before च becomes च्, as in वशात् + च = वशाच्च."),
            [("तस्मात्च", "त् does not stay before च."),
             ("तस्माद्च", "द् comes before voiced sounds, not before च."),
             ("तस्मान्च", "न् comes before a nasal, not before च.")],
            "Same rule as वशात् + च = वशाच्च.",
            "त् + च → च्च.",
            teaches="त् before च becomes च्: वशात् + च = वशाच्च; तस्मात् + च = तस्माच्च."),
    ],
}

# ---------------------------------------------------------------- unit 7
AUTHORED["7"] = {
    "title": "दोषादीनामेव चातिबहुवस्थाभेदात्",
    "question": "Why does unit 7 say the formulations, mishaps and means in emesis and the like are innumerable?",
    "rule": ("Because of the very many differences of state of doṣa and the rest, the formulations, mishaps "
             "(व्यापद्) and means (साधन) in emesis and the like are innumerable. The sentence continues in unit 8."),
    "limits": ("Printed कल्यानाम् is read as कल्पानाम्, 'of formulations'; no question rests on it. एव ('just') is kept in "
               "the Hindi but dropped in the English (open point). बहुवस्था may be a misprint. No state or mishap is named."),
    "explain_hi": ("यह इकाई एक वाक्य का पहला भाग है। दोष आदि की ही अवस्थाओं के बहुत अधिक भेद होते हैं, "
                   "इसलिए वमन आदि में कल्पों (योगों), व्यापदों (बिगड़ने या विफलता) और साधनों (उपायों) की गिनती नहीं हो सकती। "
                   "छपे ‘कल्यानाम्’ को ‘कल्पानाम्’ पढ़ा गया है। ‘असंख्येयत्वम्’ का अर्थ है असंख्यता, गिनती से परे होना। "
                   "वाक्य अगली इकाई में ‘अतः’ (इसलिए) से आगे बढ़ता है।"),
    "hook": "अवस्थाएँ अनगिनत, तो योग, व्यापद् और उपाय भी अनगिनत।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What does unit 7 give as the cause of the innumerable variety?",
            ("The many differences of state of doṣa and the rest", "अतिबहु-अवस्था-भेदात् = from the very many differences of state."),
            [("The many regions where the drugs grow", "Regions are not mentioned."),
             ("The many authors who wrote on emesis", "No authors are mentioned."),
             ("The many names given to each drug", "Names of drugs are not mentioned.")],
            "दोषादीनाम् … अवस्थाभेदात् = because of the differences of state of doṣa and the rest.",
            "Many states of doṣa → innumerable formulations, mishaps, means."),
        match(1, "Match each word of unit 7 to its meaning.",
              [["व्यापदाम्", "of mishaps, failures"], ["साधनानाम्", "of means, remedies"],
               ["असंख्येयत्वम्", "innumerability"], ["अवस्थाभेदात्", "from differences of state"]],
              "The cause (differences of state) and two of the three things that are innumerable.",
              "व्यापद् = mishap; साधन = means; असंख्येयत्व = innumerability; अवस्थाभेद = difference of state."),
        order(2, "Put these words of unit 7 in the order of the text.",
              ["दोषादीनाम्", "अवस्थाभेदात्", "वमनादिषु", "व्यापदाम्", "साधनानाम्", "असंख्येयत्वम्"],
              "Cause first (states of doṣa), then the field (emesis etc.), then the things, then 'innumerability'.",
              "दोषादीनाम् · अवस्थाभेदात् · वमनादिषु · व्यापदाम् · साधनानाम् · असंख्येयत्वम्.",
              role="extend",
              teaches="Unit 7 runs from cause (the many states of doṣa) to field (emesis and the like) to result (innumerable)."),
        mcq("discriminate", 3, "Which is the right split of वमनादिषु?",
            ("वमन + आदिषु", "अ + आ → आ: वमन + आदिषु = वमनादिषु, 'in emesis and the rest'."),
            [("वमना + दिषु", "दिषु is not a word."),
             ("वमनम् + आदिषु", "म् before a vowel would stay: वमनमादिषु."),
             ("वमने + आदिषु", "ए before आ would not give -ना-.")],
            "वमन (emesis) + आदिषु (in … and the rest, loc. pl.).",
            "अ + आ → आ."),
        mcq("apply", 4, "A reader asks for the full count of emetic formulations. By unit 7, what is the answer?",
            ("They cannot be counted", "असंख्येयत्वम्: they are innumerable."),
            [("Six, one for each best fruit", "Unit 7 gives no number; it says they are innumerable."),
             ("Twelve, as many as the mishaps", "No number of mishaps is given."),
             ("As many as the seasons", "Seasons are not mentioned.")],
            "Because the states of doṣa differ so much, formulations, mishaps and means are innumerable.",
            "असंख्येय = that cannot be counted."),
        mcq("transfer", 5, "Like असंख्येयत्वम् (innumerability), what does a new word लघुत्वम् mean?",
            ("Lightness", "-त्व makes an abstract noun: लघु (light) + त्व = lightness."),
            [("Light (an adjective)", "The adjective is लघु, without -त्व."),
             ("Very light", "'Very' would need a word like अति."),
             ("Made light", "That would be a participle, not a -त्व noun.")],
            "असंख्येय (innumerable) + त्व = innumerability; लघु + त्व = lightness.",
            "-त्व = -ness / -ity.",
            teaches="-त्व added to a word makes an abstract noun: असंख्येयत्वम् = innumerability; लघुत्वम् = lightness."),
    ],
}

# ---------------------------------------------------------------- unit 8
AUTHORED["8"] = {
    "title": "उदाहरणमात्रं कल्पसिद्धिस्थानम्",
    "question": "For what purpose, and in what form, does unit 8 say the Kalpasiddhi section is taught?",
    "rule": ("Therefore (अतः), to show the intelligent the path of variations, the Kalpasiddhisthāna is taught "
             "only as an example (उदाहरणमात्रम्). उपदेक्ष्यते is labelled future passive: 'will be taught'."),
    "limits": ("अतः points back to unit 7 (formulations are innumerable). The unit does not list what the section "
               "contains. The data's English says 'is taught'; the form is future, as the Hindi has it."),
    "explain_hi": ("पिछली इकाई ने कहा कि कल्प, व्यापद् और साधन अगणित हैं; ‘अतः’ (इसलिए) यह इकाई उसका निष्कर्ष देती है। "
                   "सब कुछ गिनाना सम्भव नहीं, इसलिए कल्पसिद्धिस्थान केवल उदाहरण के रूप में सिखाया जाएगा। "
                   "उद्देश्य है बुद्धिमानों को विकल्प का मार्ग दिखाना। "
                   "‘उपदेक्ष्यते’ भविष्यत् कर्मवाच्य है: ‘उपदेश किया जाएगा’। ‘कल्पसिद्धिस्थान’ इस भाग का नाम है।"),
    "hook": "सब नहीं गिना सकते, इसलिए उदाहरण: बुद्धिमान रास्ता समझ लें।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In what form does unit 8 say the Kalpasiddhi section will be taught?",
            ("As examples only (उदाहरणमात्रम्)", "उदाहरण-मात्रम् = a mere example."),
            [("As a complete list of recipes", "The unit says it gives examples, not everything."),
             ("As a secret for kings alone", "Kings are not mentioned."),
             ("As a summary of earlier books", "Earlier books are not mentioned.")],
            "उदाहरणमात्रं कल्पसिद्धिस्थानमुपदेक्ष्यते = the Kalpasiddhi section will be taught as a mere example.",
            "उदाहरणमात्र = only an example."),
        order(1, "Put these words of unit 8 in the order of the text.",
              ["अतः", "बुद्धिमताम्", "विकल्पमार्गदर्शनार्थम्", "उदाहरणमात्रम्", "कल्पसिद्धिस्थानम्", "उपदेक्ष्यते"],
              "Therefore · of the intelligent · to show the path of variations · a mere example · the Kalpasiddhi section · will be taught.",
              "अतः · बुद्धिमताम् · …दर्शनार्थम् · उदाहरणमात्रम् · कल्पसिद्धिस्थानम् · उपदेक्ष्यते."),
        match(2, "Match each word of unit 8 to its meaning.",
              [["बुद्धिमताम्", "of the intelligent"], ["विकल्पमार्ग", "the path of variations"],
               ["उदाहरणमात्रम्", "a mere example"], ["उपदेक्ष्यते", "will be taught"]],
              "For whom, to show what, in what form, and the verb.",
              "बुद्धिमताम् = of the intelligent; विकल्पमार्ग = path of variations; उदाहरणमात्रम् = mere example; उपदेक्ष्यते = will be taught.",
              role="extend",
              teaches="The section is taught as examples, to show the intelligent the path of variations."),
        mcq("discriminate", 3, "Which rendering of उदाहरणमात्रं कल्पसिद्धिस्थानमुपदेक्ष्यते has one wrong word?",
            ("The Kalpasiddhi section was taught as an example", "Wrong: उपदेक्ष्यते is future, 'will be taught', not past."),
            [("The Kalpasiddhi section will be taught as an example", "Correct: future passive."),
             ("As an example, the Kalpasiddhi section will be taught", "Correct: only the word order differs."),
             ("The Kalpasiddhi section will be taught, as a mere example", "Correct: मात्र rendered 'mere'.")],
            "उपदेक्ष्यते = 3 sg. future passive of उप-√दिश्: will be taught.",
            "-ष्यते (here -क्ष्यते) = future passive, 'will be …'."),
        mcq("apply", 4, "For whom, and to what end, does unit 8 say the section is taught?",
            ("To show the intelligent the path of variations", "बुद्धिमतां विकल्पमार्गदर्शनार्थम्."),
            [("To give beginners fixed recipes to copy", "The unit speaks of variations, not fixed recipes."),
             ("To show kings the cost of the drugs", "Kings and cost are not mentioned."),
             ("To warn the sick which drugs to avoid", "No warning to the sick is given.")],
            "-अर्थम् = for the purpose of: to show the path of variations to the intelligent.",
            "बुद्धिमताम् (for the intelligent) · विकल्पमार्गदर्शनार्थम् (to show the path of variations)."),
        mcq("transfer", 5, "Like विकल्पमार्गदर्शनार्थम् (for showing the path of variations), what does a new word ज्ञानार्थम् mean?",
            ("For the sake of knowledge", "-अर्थम् at the end of a compound = 'for the purpose of'."),
            [("By means of knowledge", "'By means of' would need the instrumental (ज्ञानेन)."),
             ("The meaning of knowledge", "As a compound ending, -अर्थम् here means purpose, as in the unit."),
             ("Coming from knowledge", "'From' would need the ablative (ज्ञानात्).")],
            "दर्शन + अर्थम् = for showing; ज्ञान + अर्थम् = for the sake of knowledge.",
            "X-अर्थम् = for the purpose of X.",
            teaches="-अर्थम् at the end of a compound means 'for the purpose of': विकल्पमार्गदर्शनार्थम्, ज्ञानार्थम्."),
    ],
}

# ---------------------------------------------------------------- unit 9
AUTHORED["9"] = {
    "title": "वसन्तग्रीष्मयोरन्तरे",
    "question": "When, according to unit 9, should madana fruits be collected, and which fruits?",
    "rule": ("Between spring and summer, on an auspicious day and at an auspicious moment (muhūrta), one should "
             "take madana fruits that are not very green or pale (न अति हरित-पाण्डु)."),
    "limits": ("प्रशस्ते may qualify the day only or also the muhūrta. हरित-पाण्डु may be two colours or one compound, "
               "and पाण्डु's rendering (pale or yellow) is an open point, so no question turns on the colour words. No number of fruits is given."),
    "explain_hi": ("अब मदनफल के संग्रह की विधि आरम्भ होती है। समय: वसन्त और ग्रीष्म के बीच (अन्तर में), शुभ दिन और शुभ मुहूर्त में। "
                   "कौन-से फल: मदन यानी मैनफल के वे फल जो न बहुत हरे हों, न बहुत पाण्डु (फीके) रंग के। "
                   "‘आददीत’ विधिलिङ् है: ‘ग्रहण करे’, यानी ले। "
                   "‘प्रशस्ते’ (शुभ) केवल दिन के साथ है या मुहूर्त के साथ भी, यह दोनों तरह पढ़ा जा सकता है।"),
    "hook": "वसन्त और ग्रीष्म के बीच, शुभ दिन-मुहूर्त में, न बहुत कच्चे रंग के फल।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "When does unit 9 say the madana fruits should be taken?",
            ("Between spring and summer", "वसन्त-ग्रीष्मयोः अन्तरे = in the interval of spring and summer."),
            [("Between summer and the rains", "The rains are not named."),
             ("In the middle of winter", "Winter is not named."),
             ("At the end of autumn", "Autumn is not named.")],
            "वसन्तग्रीष्मयोरन्तरे = between spring and summer.",
            "Collect madana fruits between spring and summer."),
        match(1, "Match each word of unit 9 to its meaning.",
              [["वसन्त", "spring"], ["ग्रीष्म", "summer"], ["अन्तरे", "in the interval"],
               ["अहनि", "on a day"], ["आददीत", "one should take"]],
              "The time words and the verb of the unit.",
              "वसन्त = spring; ग्रीष्म = summer; अन्तरे = in the interval; अहनि = on a day; आददीत = one should take."),
        order(2, "Put these phrases of unit 9 in the order of the text.",
              ["वसन्तग्रीष्मयोरन्तरे", "प्रशस्तेऽहनि", "मुहूर्त्ते च", "नातिहरितपाण्डूनि", "मदनफलान्याददीत"],
              "Season, day, moment, which fruits, then 'one should take madana fruits'.",
              "season · day · muhūrta · kind of fruit · take.",
              role="extend",
              teaches="Unit 9 gives the time (season, day, muhūrta) first, then which fruits, then the verb आददीत."),
        mcq("discriminate", 3, "Which is the right split of ग्रीष्मयोरन्तरे?",
            ("ग्रीष्मयोः + अन्तरे", "A visarga after ओ becomes र् before a vowel."),
            [("ग्रीष्मयो + रन्तरे", "रन्तरे is not a word; the र् is the visarga."),
             ("ग्रीष्मयोम् + अन्तरे", "म् before a vowel would stay म्: ग्रीष्मयोमन्तरे."),
             ("ग्रीष्मया + उरन्तरे", "These pieces are not words of the card.")],
            "ग्रीष्मयोः (gen. du., of [spring and] summer) + अन्तरे (in the interval).",
            "Visarga after a vowel other than अ/आ, before a vowel → र्."),
        mcq("apply", 4, "A collector finds madana fruits that are very green. By unit 9, should he take them?",
            ("No: the unit asks for fruits not very green", "न अति हरित: not very green."),
            [("Yes: any madana fruit will do", "The unit sets a condition on the fruits."),
             ("Yes, if it is midsummer", "The time is between spring and summer, and the colour rule still holds."),
             ("Yes, if he dries them first", "Drying (unit 10) does not change the rule for collecting.")],
            "नातिहरित… = not very green: very green fruits are not to be taken.",
            "न अति = not very."),
        mcq("transfer", 5, "Join a new example, न + अतिदीर्घम् (not very long). Which is right?",
            ("नातिदीर्घम्", "अ + अ → आ, as in न + अति = नाति in नातिहरित."),
            [("नअतिदीर्घम्", "The two vowels are not left side by side."),
             ("नेतिदीर्घम्", "ए comes from अ + इ, not अ + अ."),
             ("नोतिदीर्घम्", "ओ comes from अ + उ, not अ + अ.")],
            "Same rule as न + अति-हरित = नातिहरित.",
            "अ + अ → आ.",
            teaches="अ + अ → आ: न + अति = नाति (नातिहरित, नातिदीर्घम्)."),
    ],
}

# ---------------------------------------------------------------- unit 10
AUTHORED["10"] = {
    "title": "तानि प्रमृज्य कुशमूडके बध्वा",
    "question": "Through which steps does unit 10 take the collected fruits before drying them?",
    "rule": ("Wipe the fruits, tie them in a kuśa-grass bundle, smear with cow-dung, keep them eight nights in a heap "
             "of any one of barley, husk, black gram, śāli, vrīhi, horse gram or green gram, take out, dry in the sun."),
    "limits": ("'Bundle' for मूडक is uncertain. That the smeared bundle is what lies in the heap is inferred; the Sanskrit's "
               "object is the fruits. यवबुस may be one item, 'barley-husk'. बध्वा is printed for बद्ध्वा. No reason is given."),
    "explain_hi": ("मैनफल लेने के बाद उनका संस्कार इस क्रम में होता है: फलों को पोंछे, कुश के मूडक (गट्ठर; यह अर्थ अनिश्चित) में बाँधे, "
                   "गोबर से लीपे, और अनाज की राशि में आठ रात रखे। "
                   "राशि इनमें से किसी एक की हो: यव यानी जौ, बुस (भूसी), माष यानी उड़द, शालि यानी अगहनी धान, व्रीहि यानी धान, "
                   "कुलत्थ यानी कुलथी या मुद्ग यानी मूँग; ‘अन्यतम’ का अर्थ है इनमें से कोई एक, सब एक साथ नहीं। "
                   "फिर फलों को निकाले और धूप में सुखाए।"),
    "hook": "पोंछो, बाँधो, लीपो, आठ रात अनाज में, निकालो, धूप में सुखाओ।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "For how long does unit 10 keep the fruits in the grain heap?",
            ("Eight nights", "अष्टरात्रम् उषितानि = kept for eight nights."),
            [("Three nights", "The unit says eight (अष्ट)."),
             ("A full month", "No month is mentioned."),
             ("Until spring", "No season is named here.")],
            "अष्टरात्रम् = for eight nights.",
            "Eight nights in the grain heap."),
        order(1, "Put the steps of unit 10 in the order of the text.",
              ["पोंछना (प्रमृज्य)", "कुश में बाँधना (बद्ध्वा)", "गोबर से लीपना (आलिप्य)",
               "राशि में आठ रात", "निकालना (उद्धृत्य)", "धूप में सुखाना (शोषयेत्)"],
              "Wipe, tie, smear, keep eight nights, take out, dry in the sun.",
              "प्रमृज्य · बद्ध्वा · आलिप्य · अष्टरात्रम् उषितानि · उद्धृत्य · आतपे शोषयेत्."),
        match(2, "Match each grain named in unit 10 to its English name.",
              [["यव", "barley"], ["माष", "black gram"], ["कुलत्थ", "horse gram"], ["मुद्ग", "green gram"]],
              "Four of the grains of which the heap may be made (identifications standard in the data).",
              "यव = barley; माष = black gram; कुलत्थ = horse gram; मुद्ग = green gram.",
              role="extend",
              teaches="The heap may be of barley (यव), black gram (माष), horse gram (कुलत्थ) or green gram (मुद्ग), among others."),
        mcq("discriminate", 3, "How does the card read …मुद्गान्यतमराशौ, the heap in which the fruits are kept?",
            ("A heap of any one of these grains", "अन्यतम = any one of them."),
            [("A heap of all these grains mixed", "अन्यतम means one of them, not all together."),
             ("A heap of two of them, in pairs", "Nothing in the unit pairs the grains."),
             ("A heap of each grain in turn", "One heap of one grain is meant, not each in turn.")],
            "यव…मुद्ग-अन्यतम-राशौ = in a heap of any one of barley … green gram.",
            "अन्यतम = any one (of several)."),
        multi("apply", 4, "A helper has these heaps ready. Which may be used for the eight nights, by unit 10?",
              [("A heap of green gram (मुद्ग)", "Right: मुद्ग is named."),
               ("A heap of horse gram (कुलत्थ)", "Right: कुलत्थ is named."),
               ("A heap of śāli rice (शालि)", "Right: शालि is named."),
               ("A heap of sand", "Wrong: sand is not among the items named.")],
              [0, 1, 2],
              "Any one of the named grains will do; sand is not named.",
              "The heap: any one of यव, बुस, माष, शालि, व्रीहि, कुलत्थ, मुद्ग."),
        mcq("transfer", 5, "With a prefix the absolutive ends in -य (प्रमृज्य); without one, in -त्वा (बद्ध्वा). Which means having brought (आ + √नी)?",
            ("आनीय", "The root has the prefix आ-, so the ending is -य: आनीय."),
            [("आनीत्वा", "With a prefix, -त्वा is replaced by -य."),
             ("आनीतः", "This is the past participle, 'brought', not 'having brought'."),
             ("आनयति", "This is the present, 'he brings'.")],
            "प्र-√मृज् → प्रमृज्य; आ-√लिप् → आलिप्य; उद्-√हृ → उद्धृत्य; but √बन्ध् → बद्ध्वा.",
            "Prefixed root → -य; bare root → -त्वा.",
            teaches="An absolutive of a root with a prefix ends in -य (प्रमृज्य, आलिप्य, आनीय); of a bare root in -त्वा (बद्ध्वा)."),
    ],
}

# ---------------------------------------------------------------- unit 11
AUTHORED["11"] = {
    "title": "सुशुष्काणां पिप्पलीरुद्धृत्य",
    "question": "What is done with the dried fruit pieces in unit 11, and how are they stored?",
    "rule": ("From the well-dried fruits take out the pippalīs, rub them with curd, ghee, honey and palala, dry them "
             "again, fill a new, dust-free pot up to the neck and have it stored well guarded."),
    "limits": ("पिप्पली here is probably the dried madana fruit pieces (called फलपिप्पली in unit 12), not long pepper; "
               "probable, not checked against a commentary. पलल is kept as a name. That the pot is filled with these pieces is understood."),
    "explain_hi": ("सूखे फलों के साथ अगली क्रिया यह है: भली-भाँति सूखे फलों में से पिप्पलियाँ (यहाँ सम्भवतः मैनफल के सूखे टुकड़े, निश्चित नहीं) निकाले। "
                   "उन्हें दही, घी, शहद और पलल में मसले, और फिर सुखाए। "
                   "फिर एक नया और धूल-रहित कलश गले तक भरे और उसे अच्छी तरह सुरक्षित रखवाए; ‘निधापयेत्’ प्रेरणार्थक है, यानी रखवाए। "
                   "पलल को नाम ही रखा गया है; कुछ ग्रन्थ इसे तिल की पिसी लुगदी बताते हैं।"),
    "hook": "निकालो, चार चीज़ों में मसलो, फिर सुखाओ, नए कलश में गले तक भरकर सँभालो।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "What kind of pot does unit 11 ask for?",
            ("A new, dust-free pot, filled to the neck", "नवं कलशम् अरजस्कम् आकण्ठं पूरयित्वा."),
            [("An old pot once used for ghee", "The pot must be new (नवम्)."),
             ("A copper pot filled half-way", "Neither copper nor half-filling is mentioned."),
             ("Any pot, left open to the air", "It is stored well guarded (सुगुप्तम्).")],
            "नवं कलशमरजस्कमाकण्ठं पूरयित्वा = filling a new, dust-free pot up to the neck.",
            "नव (new) · अरजस्क (dust-free) · आकण्ठ (to the neck)."),
        match(1, "Match each substance in which the pieces are rubbed to its meaning.",
              [["दधि", "curd"], ["घृत", "ghee"], ["मधु", "honey"], ["पलल", "palala (kept as a name)"]],
              "The four substances of दधिघृतमधुपललविमृदिताः.",
              "दधि = curd; घृत = ghee; मधु = honey; पलल = palala."),
        order(2, "Put the steps of unit 11 in the order of the text.",
              ["पिप्पलियाँ निकालना", "दही, घी, शहद, पलल में मसलना", "फिर सुखाना",
               "नया कलश गले तक भरना", "सुरक्षित रखवाना"],
              "Take out, rub, dry again, fill the pot, have it stored.",
              "उद्धृत्य · विमृदिताः · पुनः शोषयित्वा · पूरयित्वा · निधापयेत्.",
              role="extend",
              teaches="Unit 11 runs: take out, rub with four substances, dry again, fill a new pot to the neck, store it guarded."),
        mcq("discriminate", 3, "Which is the right split of पिप्पलीरुद्धृत्य?",
            ("पिप्पलीः + उद्धृत्य", "A visarga after ई becomes र् before a vowel."),
            [("पिप्पली + रुद्धृत्य", "रुद्धृत्य is not a word; the र् is the visarga."),
             ("पिप्पलिः + उद्धृत्य", "The word here is पिप्पलीः, acc. pl. with long ई."),
             ("पिप्पलीर् + उद्धृत्य", "र् is the sandhi result; the word itself ends in -ईः.")],
            "पिप्पलीः (f. acc. pl.) + उद्धृत्य (having taken out).",
            "Visarga after ई before a vowel → र्."),
        mcq("apply", 4, "A helper rubs the pieces with curd, ghee, honey and palala and fills the pot at once. Which step is missing?",
            ("Drying them again (पुनः शोषयित्वा)", "After rubbing, the unit dries them again before filling the pot."),
            [("Boiling them in milk", "Boiling is not a step of this unit."),
             ("Wiping them with kuśa", "Kuśa appears in unit 10, not as a step here."),
             ("Grinding them to powder", "Grinding is not a step of this unit.")],
            "The order is rub, dry again (पुनः शोषयित्वा), then fill the pot.",
            "पुनः शोषयित्वा = having dried again."),
        mcq("transfer", 5, "आकण्ठम् means up to the neck (आ + कण्ठ). On this pattern, what does a new word आजानु mean?",
            ("Up to the knee", "आ- before a noun, as an indeclinable, can mean 'up to'."),
            [("Below the knee", "आ- here marks the limit reached, not 'below'."),
             ("Without a knee", "'Without' would be a negative like निर्- or अ-."),
             ("Away from the knee", "'Away from' would need the ablative.")],
            "आ + कण्ठ = up to the neck; आ + जानु = up to the knee.",
            "आ + noun (indeclinable) = up to …",
            teaches="आ- joined to a noun as an indeclinable can mean 'up to': आकण्ठम् (up to the neck), आजानु (up to the knee)."),
    ],
}


NOTES_HI = {
    "1": ("विश्वास: उच्च। आरम्भ का ‘॥’ छपा चिह्न है और टोकन के रूप में रखा गया है। "
          "खुला बिन्दु (05.01.1): ‘श्रीगणेशाय’ एक शब्द छपा है; समीक्षक इसे श्री-गणेशाय समास दिखाने का सुझाव देते हैं, जो अभी तय नहीं; इस पर प्रश्न नहीं बना। "
          "सन्धि नहीं; पाठभेद नहीं।"),
    "2": ("विश्वास: उच्च। सन्धि जाँची: अथातो = अथ + अतः (अ + अ → आ; अः + घोष व्यंजन व → ओ); "
          "वमनकल्पं = वमनकल्पम् (अन्त्य म् का अनुस्वार)। ‘व्याख्यास्यामः’ डेटा में १ बहुवचन भविष्यत् (वि-आ-√ख्या)। पाठभेद या चिह्नित दोष नहीं।"),
    "3": ("विश्वास: उच्च। डेटा में इकाई का प्रकार ‘श्लोक’ है, पर यह एक ही पंक्ति का कथन-सूत्र है। "
          "सन्धि जाँची: स्माहुरात्रेय = स्म + आहुः + आत्रेय (अ + आ → आ; उः + स्वर → उर्); आत्रेयादयो महर्षयः = …आदयः + महर्षयः (अः + घोष म → ओ); "
          "महर्षयः = महा + ऋषयः (आ + ऋ → अर्)। "
          "खुला बिन्दु (05.01.3): ‘आत्रेय’ को अलग शब्द ‘m. nom. sg.’ लिखा गया है, जबकि आत्रेयादयः एक समास है; इस लेबल पर प्रश्न नहीं बना।"),
    "4": ("विश्वास: निम्न। लम्बा समास स्कैन में क्षतिग्रस्त है: छपा ‘कक्ष्वेवाकु’ सम्भवतः ‘इक्ष्वाकु’ है (जीमूतक + इक्ष्वाकु → जीमूतकेक्ष्वाकु, सुझाव, जाँचा नहीं); "
          "‘कुक्कृतिका’ और ‘शातकी’ भी संदिग्ध हैं (दूसरे ग्रन्थों में शायद कृतवेधन / श्यातकी; अप्रमाणित)। "
          "पहचान: मदन और कुटज मानक, जीमूतक सम्भावित, इक्ष्वाकु विवादित, शेष अज्ञात। "
          "प्रश्न केवल स्पष्ट शब्दों (मदन, जीमूतक, कुटज, फलानि, श्रेष्ठानि) पर बने।"),
    "5": ("विश्वास: मध्यम। इकाई में क्रिया या विधेय नहीं; ‘श्रेष्ठ’ का भाव इकाई ४ से लिया गया है, जैसा डेटा पढ़ता है। "
          "सन्धि जाँची: तेष्वपि = तेषु + अपि (उ + भिन्न स्वर → व्)। मदनफलं = मदनफलम्।"),
    "6": ("विश्वास: मध्यम। छपा ‘दृष्य’ प्रूफ़-संशोधन में ‘दूष्य’ पढ़ा गया (दोषदूष्यादिवशात्)। डेटा में प्रकार ‘श्लोक’, पर यह एक पंक्ति का कथन है। "
          "‘एषाम् एतत्कल्पनानाम्’ को ‘इन (द्रव्यों) का और इन कल्पनाओं का’ पढ़ा गया; दूसरा पठन भी सम्भव है। क्रिया ‘है’ जोड़ी गई। "
          "सन्धि जाँची: वशाच्चैषाम् = वशात् + च + एषाम् (त् + च → च्च; अ + ए → ऐ)।"),
    "7": ("विश्वास: मध्यम। छपा ‘कल्यानां’ संशोधित पाठ ‘कल्पानाम्’ लिया गया (अर्थ और अध्याय के विषय से); इस पर प्रश्न नहीं बना। "
          "‘चातिबहुवस्था’ में बहु + अवस्था की सामान्य सन्धि ‘बह्ववस्था’ होती; सम्भव मुद्रण-दोष। "
          "खुला बिन्दु (05.01.7): ‘एव’ अंग्रेज़ी में छूटा है, हिन्दी में ‘ही’ है। वाक्य इकाई ८ में ‘अतः’ से आगे चलता है। "
          "सन्धि जाँची: वमनादिषु = वमन + आदिषु; यदसंख्येयत्वं = यत् + असंख्येयत्वम् (त् → द्)।"),
    "8": ("विश्वास: उच्च। ‘मात्र’ = केवल। ‘कल्पसिद्धिस्थान’ इस भाग का नाम (कल्प और सिद्धि)। "
          "‘उपदेक्ष्यते’ डेटा में ३ एकवचन भविष्यत् कर्मवाच्य है; अंग्रेज़ी अनुवाद ‘is taught’ वर्तमान लिखता है, हिन्दी ‘किया जाएगा’ सही भविष्यत् है। "
          "सन्धि जाँची: अतो बुद्धिमताम् = अतः + बुद्धिमताम् (अः + घोष → ओ); …मात्रं कल्प… = …मात्रम् + कल्प…; …स्थानमुपदेक्ष्यते = …स्थानम् + उपदेक्ष्यते।"),
    "9": ("विश्वास: मध्यम। ‘मुहूर्त्ते’ = मुहूर्ते का छपा रूप (त्त दोहराया)। ‘प्रशस्ते’ केवल ‘अहनि’ का विशेषण हो सकता है या ‘मुहूर्ते’ का भी; अनुवाद दोनों के साथ लेते हैं। "
          "‘हरितपाण्डु’ दो रंग या एक समास दोनों तरह पढ़ा जा सकता है। "
          "खुला बिन्दु (05.01.9): पाण्डु का हिन्दी ‘पीले’ और अंग्रेज़ी ‘pale’ मेल नहीं खाते; रंग-शब्दों पर प्रश्न नहीं बना। "
          "सन्धि जाँची: ग्रीष्मयोरन्तरे = ग्रीष्मयोः + अन्तरे; प्रशस्तेऽहनि = प्रशस्ते + अहनि (ए + अ → एऽ); नाति = न + अति; मदनफलान्याददीत = मदनफलानि + आददीत (इ → य्)।"),
    "10": ("विश्वास: मध्यम। ‘बध्वा’ छपा है, सामान्य रूप ‘बद्ध्वा’ (सम्भव मुद्रण-दोष)। ‘मूडक’ = गट्ठर, अनिश्चित (मराठी ‘मूढ’ से तुलना)। "
           "‘यवबुस’ को ‘जौ और भूसी’ या ‘जौ की भूसी’ दोनों पढ़ा जा सकता है। गोबर से लिपा गट्ठर ही राशि में रखा जाता है, यह अनुमान है; संस्कृत का कर्म ‘तानि’ (फल) है। "
           "खुला बिन्दु (05.01.10): अंग्रेज़ी का ‘it’ (गट्ठर) अनुमान है। "
           "सन्धि जाँची: गोमयेनालिप्य = गोमयेन + आलिप्य; …मुद्गान्यतम… = मुद्ग + अन्यतम; …राशावष्टरात्रम् = राशौ + अष्टरात्रम् (औ → आव्); उषितान्युद्धृत्यातपे = उषितानि + उद्धृत्य + आतपे।"),
    "11": ("विश्वास: मध्यम। ‘पिप्पली’ का सामान्य अर्थ पिप्पली (लम्बी मिर्च, मानक) है, पर इस अध्याय में सूखे मदनफल से निकाली और आगे ‘फलपिप्पली’ कही गई वस्तु सम्भवतः मैनफल के सूखे टुकड़े हैं (सम्भावित, टीका से जाँचा नहीं)। "
           "‘पलल’ नाम ही रखा गया (कुछ कोशों में तिल की लुगदी या मांस)। कलश में ये टुकड़े भरे जाते हैं, यह समझा गया है। "
           "सन्धि जाँची: पिप्पलीरुद्धृत्य = पिप्पलीः + उद्धृत्य (ईः + स्वर → ईर्); कलशमरजस्कमाकण्ठम् = कलशम् + अरजस्कम् + आकण्ठम्।"),
}


AIDS = {
    "1": {
        "frame": "किसको: गणेश (गणेशाय, चतुर्थी) · क्या: नमः (नमस्कार) · कैसे: श्री (आदर से)।",
        "contrast": "गणेशाय = गणेश को (चतुर्थी, नमः के साथ) · गणेशस्य = गणेश का (षष्ठी) · गणेशः = गणेश (कर्ता)।",
        "anchors": "श्री = आदरणीय, मंगल · गणेश = देवता का नाम · नमः = नमस्कार।",
    },
    "2": {
        "chunks": "अथातो | वमनकल्पं | व्याख्यास्यामः।",
        "sandhi": "अ + अ → आ: अथ + अतः → अथातः; अः + घोष व्यंजन → ओ: अतः + वमन… → अतो वमन…।",
        "anchors": "अथ = अब · अतः = इसलिए · वमन = उल्टी कराने की चिकित्सा · कल्प = योग · व्याख्यास्यामः = हम व्याख्या करेंगे।",
    },
    "3": {
        "chunks": "इति ह स्माहुः | आत्रेयादयो महर्षयः।",
        "sandhi": "अ + आ → आ: स्म + आहुः → स्माहुः; उः + स्वर → उर्: आहुः + आत्रेय → आहुरात्रेय; आ + ऋ → अर्: महा + ऋषयः → महर्षयः।",
        "anchors": "इति = ऐसा · ह = निश्चय ही · स्म आहुः = कहा था · आदयः = आदि, दूसरे · महर्षि = महान् ऋषि।",
    },
    "4": {
        "diagram": {"groups": [{"label": "पहचान मानक", "items": ["मदन यानी मैनफल", "कुटज यानी कुड़ा"]},
                               {"label": "पहचान सम्भावित", "items": ["जीमूतक (बन्दाल)"]},
                               {"label": "पाठ संदिग्ध", "items": ["इक्ष्वाकु (अनुमानित पाठ)", "कुक्कृतिका", "शातकी"]}]},
        "frame": "किनमें: वमन-द्रव्यों में · क्या: इनके फल · कैसे: श्रेष्ठ · सूची: मदन से आरम्भ, कुटज पर अन्त।",
        "anchors": "वमनद्रव्य = वमन कराने वाले द्रव्य · फलानि = फल · श्रेष्ठानि = सबसे अच्छे।",
    },
    "5": {
        "chain": {"steps": ["इकाई ४: वमन के श्रेष्ठ फल", "तेषु अपि: उनमें भी", "मदनफल (श्रेष्ठ, भाव इकाई ४ से)"]},
        "sandhi": "उ + भिन्न स्वर → व्: तेषु + अपि → तेष्वपि।",
        "anchors": "तेषु = उनमें · अपि = भी · मदनफल = मैनफल।",
    },
    "6": {
        "frame": "किसका प्राधान्य: इन द्रव्यों और इन योगों का · किसके वश से: दोष, दूष्य आदि · क्रिया: ‘है’ जोड़ी गई।",
        "sandhi": "त् + च → च्च: वशात् + च → वशाच्च; अ + ए → ऐ: च + एषाम् → चैषाम्।",
        "anchors": "दोष = दोष · दूष्य = जो दूषित होता है · वश = अधीनता · प्राधान्य = प्रधानता।",
    },
    "7": {
        "chain": {"steps": ["दोष आदि की बहुत अधिक अवस्थाएँ", "उन अवस्थाओं के भेद", "वमन आदि में कल्प, व्यापद् और साधन", "असंख्येय (गिने नहीं जा सकते)"]},
        "sandhi": "अ + आ → आ: वमन + आदिषु → वमनादिषु; त् + अ → द: यत् + असंख्येयत्वम् → यदसंख्येयत्वम्।",
        "anchors": "अवस्था = दशा · भेद = अन्तर · व्यापद् = बिगड़ना, विफलता · साधन = उपाय · असंख्येय = अगणित।",
    },
    "8": {
        "chunks": "अतो बुद्धिमतां | विकल्पमार्गदर्शनार्थम् | उदाहरणमात्रं | कल्पसिद्धिस्थानमुपदेक्ष्यते।",
        "frame": "क्यों: अतः (कल्प अगणित हैं) · किसके लिए: बुद्धिमानों के · किस हेतु: विकल्प का मार्ग दिखाने · कैसे: केवल उदाहरण · क्या: कल्पसिद्धिस्थान।",
        "anchors": "बुद्धिमत् = बुद्धिमान · विकल्प = भेद, विकल्प · मार्ग = रास्ता · दर्शन = दिखाना · मात्र = केवल · उपदेक्ष्यते = उपदेश किया जाएगा।",
    },
    "9": {
        "diagram": {"groups": [{"label": "कब", "items": ["वसन्त और ग्रीष्म के बीच", "शुभ दिन", "शुभ मुहूर्त"]},
                               {"label": "क्या", "items": ["मदनफल", "न बहुत हरे, न बहुत पाण्डु"]},
                               {"label": "क्रिया", "items": ["आददीत: ग्रहण करे"]}]},
        "sandhi": "ओः + स्वर → ओर्: ग्रीष्मयोः + अन्तरे → ग्रीष्मयोरन्तरे; अ + अ → आ: न + अति → नाति।",
        "anchors": "वसन्त = वसन्त ऋतु · ग्रीष्म = गर्मी की ऋतु · अन्तर = बीच का समय · प्रशस्त = शुभ · आददीत = ले।",
    },
    "10": {
        "chain": {"steps": ["पोंछे (प्रमृज्य)", "कुश के गट्ठर में बाँधे (बद्ध्वा)", "गोबर से लीपे (आलिप्य)",
                            "अनाज की राशि में आठ रात", "निकाले (उद्धृत्य)", "धूप में सुखाए (शोषयेत्)"]},
        "diagram": {"groups": [{"label": "राशि: इनमें से कोई एक", "items": ["यव यानी जौ", "बुस (भूसी)", "माष यानी उड़द", "शालि यानी अगहनी धान",
                                                                   "व्रीहि यानी धान", "कुलत्थ यानी कुलथी", "मुद्ग यानी मूँग"]}]},
        "sandhi": "उपसर्ग वाली धातु → -य: प्रमृज्य, आलिप्य, उद्धृत्य; बिना उपसर्ग → -त्वा: बद्ध्वा (छपा बध्वा)।",
        "anchors": "प्रमृज्य = पोंछकर · मूडक = गट्ठर (अनिश्चित) · गोमय = गोबर · राशि = ढेर · आतप = धूप।",
    },
    "11": {
        "chain": {"steps": ["सूखे फलों से पिप्पलियाँ निकाले", "दही, घी, शहद, पलल में मसले", "फिर सुखाए",
                            "नया, धूल-रहित कलश गले तक भरे", "अच्छी तरह सुरक्षित रखवाए"]},
        "frame": "कलश: नया (नव) · धूल-रहित (अरजस्क) · गले तक (आकण्ठ) · रखना: सुगुप्त, रखवाए (निधापयेत्)।",
        "anchors": "सुशुष्क = भली-भाँति सूखा · विमृदित = मसला हुआ · पुनः = फिर · कलश = घड़ा · आकण्ठम् = गले तक।",
    },
}


IMAGE_SPECS = {
    ("4", "diagram"): {
        "file": "ka1-best-emetics-4.svg",
        "alt": ("Table of the six best emetic fruits of unit 4 with the status of each: madana and kutaja standard, "
                "jimutaka probable, ikshvaku a conjectural reading and disputed, kukkritika and shataki doubtful and unidentified"),
        "type": "table",
        "title": "इकाई ४: वमन के श्रेष्ठ फल",
        "heads": ["नाम (सूची-क्रम)", "पहचान"],
        "rows": [["मदन", "मैनफल (मानक)"], ["जीमूतक", "बन्दाल (सम्भावित)"],
                 ["इक्ष्वाकु", "अनुमानित पाठ, विवादित"], ["कुक्कृतिका", "पाठ संदिग्ध, अज्ञात"],
                 ["शातकी", "पाठ संदिग्ध, अज्ञात"], ["कुटज", "कुड़ा (मानक)"]],
    },
    ("7", "chain"): {
        "file": "ka1-innumerable-7.svg",
        "alt": ("Flowchart of unit 7: the very many states of dosha and the rest, their differences, so the formulations, "
                "mishaps and means in emesis and the like are innumerable"),
        "type": "mermaid",
        "code": ('flowchart TD\n  A["दोष आदि की बहुत अवस्थाएँ"] --> B["अवस्थाओं के भेद"]\n'
                 '  B --> C["वमन आदि में"]\n  C --> D["कल्प"]\n  C --> E["व्यापद्"]\n  C --> F["साधन"]\n'
                 '  D --> G["असंख्येय"]\n  E --> G\n  F --> G\n'),
    },
    ("9", "diagram"): {
        "file": "ka1-collect-time-9.svg",
        "alt": ("Table for unit 9: when (between spring and summer, auspicious day and moment), which fruits "
                "(madana fruits not very green or pale) and the verb (one should take)"),
        "type": "table",
        "title": "इकाई ९: मदनफल का संग्रह",
        "heads": ["प्रश्न", "इकाई का उत्तर"],
        "rows": [["ऋतु", "वसन्त और ग्रीष्म के बीच"], ["दिन", "शुभ (प्रशस्त)"], ["समय", "शुभ मुहूर्त"],
                 ["कौन-से फल", "न बहुत हरे, न बहुत पाण्डु"], ["क्रिया", "ग्रहण करे (आददीत)"]],
    },
    ("10", "chain"): {
        "file": "ka1-cure-fruits-10.svg",
        "alt": ("Flowchart of the six steps of unit 10: wipe the fruits, tie in a kusha bundle, smear with cow-dung, "
                "keep eight nights in a heap of one grain, take out, dry in the sun"),
        "type": "mermaid",
        "code": ('flowchart TD\n  A["फल पोंछे"] --> B["कुश के गट्ठर में बाँधे"]\n'
                 '  B --> C["गोबर से लीपे"]\n  C --> D["एक अनाज की राशि में<br/>आठ रात"]\n'
                 '  D --> E["निकाले"]\n  E --> F["धूप में सुखाए"]\n'),
    },
    ("11", "chain"): {
        "file": "ka1-store-pot-11.svg",
        "alt": ("Flowchart of unit 11: take the pippalis out of the dried fruits, rub with curd, ghee, honey and palala, "
                "dry again, fill a new dust-free pot to the neck, store it well guarded"),
        "type": "mermaid",
        "code": ('flowchart TD\n  A["सूखे फलों से<br/>पिप्पलियाँ निकाले"] --> B["दही, घी, शहद, पलल में<br/>मसले"]\n'
                 '  B --> C["फिर सुखाए"]\n  C --> D["नया, धूल-रहित कलश<br/>गले तक भरे"]\n'
                 '  D --> E["सुरक्षित रखवाए"]\n'),
    },
}
