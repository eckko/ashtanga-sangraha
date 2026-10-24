from helpers import mcq, match, order, fill, multi, accepts


def T(q, teaches):
    q["teaches"] = teaches
    return q


AUTHORED = {}

FILL_TAIL = "(type it in Devanagari or in English letters, e.g. dharma)."

# ---------------------------------------------------------------- unit 54
AUTHORED["54"] = {
    "title": "प्रियंगुतिलकल्कं वा योनौ धारयेत्",
    "question": "What does unit 54 say is held in the yoni, and what is the wash?",
    "rule": ("Or one should hold a paste (kalka) of priyaṅgu and tila in the yoni; a decoction of sarala and "
             "mudgaparṇī is the wash (prakṣālana)."),
    "limits": ("Two printed lines joined. The unit names no doṣa; it stands after the Vāta-type ārtava measures begun in unit 52. "
               "priyaṅgu (Callicarpa macrophylla) and sarala (Pinus roxburghii) are probable identifications; mudgaparṇī is not "
               "identified. The text does not say what is washed (presumably the yoni). No amount is given."),
    "explain_hi": ("यह गद्य-इकाई दो छपी पंक्तियों को जोड़ती है। पहली: अथवा प्रियंगु (सम्भवतः फूलप्रियंगु) और तिल का कल्क "
                   "योनि में धारण करे। दूसरी एक नाम-वाक्य है, क्रिया नहीं: सरल (सम्भवतः चीड़) और मुद्गपर्णी का काढ़ा प्रक्षालन है। "
                   "किसका प्रक्षालन, यह पाठ नहीं कहता; सम्भवतः योनि का। "
                   "इकाई स्वयं दोष का नाम नहीं लेती; यह इकाई ५२ में आरम्भ हुई वातज आर्तवदोष की चिकित्सा के बाद आती है।"),
    "hook": "भीतर रखो प्रियंगु-तिल, धोओ सरल-मुद्गपर्णी से।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In unit 54, what is to be held in the yoni?",
            ("A paste of priyaṅgu and tila", "प्रियंगुतिलकल्कं … योनौ धारयेत्."),
            [("A decoction of sarala and mudgaparṇī", "That decoction is the wash (प्रक्षालनम्), not what is held."),
             ("Oil cooked with madhuka", "No oil is named in this unit."),
             ("Milk cooked with kāśmarya", "No milk is named in this unit.")],
            "Held in the yoni: the paste of priyaṅgu and tila; the wash: the decoction of sarala and mudgaparṇī.",
            "कल्क (paste) is held; कषाय (decoction) is the wash."),
        order(1, "Put these words of unit 54 in their printed order.",
              ["प्रियंगुतिलकल्कम्", "योनौ", "धारयेत्", "सरलमुद्गपर्णीकषायः", "प्रक्षालनम्"],
              "Line 1: the paste, in the yoni, should hold. Line 2: the decoction is the wash.",
              "कल्क → योनौ → धारयेत् · कषायः → प्रक्षालनम्."),
        T(match(2, "Match each word of unit 54 to its meaning on the card.",
                [["कल्क", "paste"], ["धारयेत्", "should hold, retain"], ["कषाय", "decoction"],
                 ["प्रक्षालन", "washing, rinsing"], ["तिल", "sesame"]],
                "Two preparations appear: a paste to hold and a decoction to wash with.",
                "कल्क = paste; कषाय = decoction; प्रक्षालन = wash.", role="extend"),
          "A कल्क is a paste; a कषाय is a decoction; प्रक्षालन is washing."),
        mcq("discriminate", 3, "In योनौ (from योनि), what does the ending -औ mark here?",
            ("Locative singular: in the yoni", "The gram label is f. loc. sg.: योनौ = in the yoni."),
            [("Nominative dual: two yonis", "-औ is dual in अ-stems, but योनि is an इ-stem; here it is loc. sg."),
             ("Instrumental singular: by the yoni", "The instrumental of योनि is योन्या."),
             ("Genitive plural: of the yonis", "The genitive plural is योनीनाम्.")],
            "For इ-stem nouns like योनि, -औ is the locative singular: योनौ = in the yoni.",
            "-औ is not always dual: इ-stem loc. sg. ends in -औ."),
        mcq("apply", 4, "Which statement about the second line of unit 54 is right?",
            ("It is a nominal sentence; what is washed is not stated", "No verb; the note says the yoni is only presumed."),
            [("It tells one to drink the decoction", "No verb of drinking stands in the line."),
             ("It names the yoni as what is washed", "The note: presumably the yoni, but the text does not say."),
             ("It gives the amount of the decoction", "No amount is given in this unit.")],
            "सरलमुद्गपर्णीकषायः प्रक्षालनम्: the decoction is the wash; the object of the wash is left unstated.",
            "Nominal sentence: X (nom.) is Y (nom.), no verb."),
        T(mcq("transfer", 5, "By the ending of योनौ, what does an invented अग्नौ (from अग्नि, fire) mean?",
              ("In the fire", "अग्नि is an इ-stem like योनि; -औ is the locative singular."),
              [("Two fires", "-औ marks a dual only in stems like देव (देवौ); not in इ-stems."),
               ("By the fire", "By the fire is अग्निना."),
               ("Of the fires", "Of the fires is अग्नीनाम्.")],
              "योनि → योनौ (in the yoni); so अग्नि → अग्नौ (in the fire).",
              "इ-stem + -औ = locative singular."),
          "Masculine and feminine इ-stems (अग्नि, योनि) form the locative singular in -औ."),
    ],
}

# ---------------------------------------------------------------- unit 55
AUTHORED["55"] = {
    "title": "पित्तजे काकोलीद्वय",
    "question": "In the Pitta-type (fault of ārtava), which three decoctions does unit 55 say one should drink?",
    "rule": ("In the Pitta-type one should drink three decoctions: of the kākolī pair and vidārī root, of utpala and padmaka, "
             "and of madhuka flower and kāśmarya fruit (as taken); vāsa and sugar are added, reach undecided."),
    "limits": ("Medium confidence. Whether 'with vāsa and sugar' goes with one decoction or all three is not decided; they could "
               "also be two more items drunk. The grouping 'madhuka flower, kāśmarya fruit' has an alternative. kākolī's identity "
               "is disputed; vāsa is read as vāsā (probably Adhatoda vasica), not certain. No amounts."),
    "explain_hi": ("यहाँ से पित्तज (आर्तवदोष) की चिकित्सा आरम्भ होती है: ‘पित्तजे’ = पित्तज में। "
                   "तीन क्वाथ गिनाए गए हैं: काकोली-द्वय और विदारी-मूल का, उत्पल और पद्मक का, तथा मधुक-पुष्प और काश्मर्य-फल का। "
                   "अन्त में ‘वासशर्करं’ है: वास (सम्भवतः अडूसा) और शर्करा; यह तीनों के साथ है या एक के साथ, संस्कृत से तय नहीं। "
                   "काकोली की पहचान विवादित है; उत्पल (नील कमल) और पद्मक सम्भावित, काश्मर्य (गम्भारी) मानक पहचान है।"),
    "hook": "पित्त में तीन क्वाथ: काकोली-विदारी, उत्पल-पद्मक, मधुक-काश्मर्य।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In unit 55, what is the form in which the drugs are to be taken?",
            ("As decoctions (क्वाथ), to be drunk", "क्वाथम् three times, and the verb पिबेत् (should drink)."),
            [("As pastes held in the yoni", "No paste and no धारयेत् appear in this unit."),
             ("As a powder to be licked", "No चूर्ण and no लिह्यात् appear in this unit."),
             ("As oil given in an enema", "No oil or enema is named in this unit.")],
            "Three decoctions (क्वाथ) are named, and the verb is पिबेत्, should drink.",
            "क्वाथ = decoction; पिबेत् = should drink."),
        order(1, "Put the three decoctions of unit 55 in their printed order.",
              ["काकोलीद्वय-विदारीमूल-क्वाथ", "उत्पल-पद्मक-क्वाथ", "मधुकपुष्प-काश्मर्यफल-क्वाथ"],
              "First the kākolī pair and vidārī root, then utpala and padmaka, then madhuka flower and kāśmarya fruit.",
              "काकोली-विदारी → उत्पल-पद्मक → मधुक-काश्मर्य."),
        T(match(2, "Match each word of unit 55 to its meaning on the card.",
                [["पित्तजे", "in the Pitta-type (one)"], ["द्वय", "pair"], ["क्वाथ", "decoction"],
                 ["शर्करा", "sugar"], ["पिबेत्", "should drink"]],
                "These words frame the unit: in the Pitta-type, decoctions, sugar, should drink.",
                "पित्तज = Pitta-type; क्वाथ = decoction; पिबेत् = should drink.", role="extend"),
          "पित्तजे is a locative: in the Pitta-type (fault)."),
        mcq("discriminate", 3, "Which split of क्वाथमुत्पलपद्मक is right?",
            ("क्वाथम् + उत्पल-पद्मक", "Final म् before a vowel joins it: क्वाथम् + उ → क्वाथमु."),
            [("क्वाथ + मुत्पल-पद्मक", "मुत्पल is not a word of the card; the plant is उत्पल."),
             ("क्वाथः + उत्पल-पद्मक", "अः + उ would give क्वाथ उत्पल, with no म्."),
             ("क्वाथे + उत्पल-पद्मक", "ए + उ would give क्वाथ उत्पल or क्वाथयुत्पल, not क्वाथमु.")],
            "क्वाथम् (decoction, acc.) + उत्पल-पद्मक-क्वाथम् (the decoction of utpala and padmaka).",
            "Final म् + vowel → म joined to the vowel."),
        mcq("apply", 4, "What does the card say about वासशर्करम् (with vāsa and sugar)?",
            ("Which decoction it goes with is not decided", "The note: one or all three, not decided by the Sanskrit."),
            [("It goes only with the third decoction", "That is one possibility only; the note leaves it open."),
             ("It is a fourth decoction to be drunk", "There is no क्वाथ in this word; that sense is not stated."),
             ("It is to be held in the yoni", "No धारयेत् appears in this unit.")],
            "The card keeps the reach of वासशर्करम् open: one decoction or all three, or two more items.",
            "Where the note leaves a reading open, the card does too."),
        T(mcq("transfer", 5, "By the rule of क्वाथमुत्पल, how is the invented जलम् + उष्णम् written when joined?",
              ("जलमुष्णम्", "Final म् before the vowel उ joins it: जलमु-."),
              [("जलं उष्णम्", "Anusvāra stands for म् only before a consonant."),
               ("जलोष्णम्", "That would be जल + उष्णम् (अ + उ → ओ), not जलम्."),
               ("जलरुष्णम्", "र् comes from a visarga, not from म्.")],
              "क्वाथम् + उत्पल → क्वाथमुत्पल; so जलम् + उष्णम् → जलमुष्णम्.",
              "म् + vowel → joined."),
          "A final म् before a vowel is written joined to it; before a consonant it may be written as anusvāra."),
    ],
}

# ---------------------------------------------------------------- unit 56
AUTHORED["56"] = {
    "title": "श्वेतचंदनक्वाथं वा सक्षौद्रं",
    "question": "What alternative does unit 56 give, and what is added to it?",
    "rule": "Or a decoction of white sandalwood, with honey (kṣaudra).",
    "limits": ("Elliptical: no verb is stated, and the unit names no doṣa; it follows the Pitta-type decoctions of unit 55. "
               "White sandalwood as Santalum album is a probable identification. No amount is given."),
    "explain_hi": ("यह बहुत छोटी गद्य-इकाई इकाई ५५ के बाद एक और विकल्प देती है: अथवा श्वेत चन्दन का क्वाथ, शहद सहित। "
                   "‘सक्षौद्रम्’ = स + क्षौद्र, यानी शहद के साथ; क्षौद्र का अर्थ शहद है। "
                   "इकाई में कोई क्रिया नहीं है, इसलिए वाक्य अधूरा-सा है। "
                   "श्वेत चन्दन की पहचान Santalum album सम्भावित है।"),
    "hook": "सफ़ेद चन्दन का काढ़ा, ऊपर से शहद।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 56, what is added to the white sandalwood decoction?",
            ("Honey (क्षौद्र)", "सक्षौद्रम् = with honey."),
            [("Sugar (शर्करा)", "Sugar is named in unit 55, not here."),
             ("Ghee (घृत)", "Ghee is not named in this unit."),
             ("Milk (क्षीर)", "Milk is not named in this unit.")],
            "Or a decoction of white sandalwood, with honey.",
            "क्षौद्र = honey; स- = with."),
        order(1, "Put the parts of unit 56 in their printed order.",
              ["श्वेत", "चन्दन", "क्वाथम्", "वा", "सक्षौद्रम्"],
              "White, sandalwood, decoction, or, with honey.",
              "श्वेत → चन्दन → क्वाथम् → वा → सक्षौद्रम्."),
        T(match(2, "Match each word of unit 56 to its meaning on the card.",
                [["श्वेत", "white"], ["चन्दन", "sandalwood"], ["क्वाथ", "decoction"], ["क्षौद्र", "honey"], ["वा", "or"]],
                "Every word of the short unit carries meaning: colour, wood, preparation, addition, alternative.",
                "श्वेत, चन्दन, क्वाथ, क्षौद्र, वा.", role="extend"),
          "क्षौद्र is a word for honey."),
        mcq("discriminate", 3, "What does the prefix स- add in सक्षौद्रम्?",
            ("With: together with honey", "स- in a bahuvrīhi = accompanied by."),
            [("Without: free of honey", "Without would be निः- or अ-, not स-."),
             ("Good: of good honey", "Good would be सु-, not स-."),
             ("Much: a lot of honey", "स- does not mean much; no amount is given.")],
            "स + क्षौद्र = having honey with it, i.e. with honey.",
            "स- (bahuvrīhi) = with."),
        mcq("apply", 4, "Which statement about unit 56 is right?",
            ("No verb is stated in it", "The note: elliptical; पिबेत् is not stated here."),
            [("It names the Kapha-type", "No doṣa is named; it follows unit 55's Pitta-type list."),
             ("It gives the dose of honey", "No amount is given."),
             ("It tells one to hold it in the yoni", "No धारयेत् appears in this unit.")],
            "The unit is elliptical: only the decoction and the honey are named.",
            "Elliptical unit: no verb."),
        T(mcq("transfer", 5, "By सक्षौद्रम्, what does the invented सपुत्रः राजा (पुत्र = son) mean?",
              ("The king with his son", "स + पुत्र = having the son along, with the son."),
              [("The king without a son", "Without would be अपुत्रः."),
               ("The good son of the king", "स- is not सु- (good)."),
               ("The son who is a king", "स- makes 'with', not an identity.")],
              "स + क्षौद्र = with honey; so स + पुत्र = with the son.",
              "स-X (bahuvrīhi) = with X."),
          "स- before a noun makes a bahuvrīhi meaning 'with X', 'accompanied by X'."),
    ],
}

# ---------------------------------------------------------------- unit 57
AUTHORED["57"] = {
    "title": "धवधातकीकल्कं वा",
    "question": "What further alternative does unit 57 give?",
    "rule": "Or a paste (kalka) of dhava and dhātakī.",
    "limits": ("Elliptical: no verb and no doṣa are stated; it follows the Pitta-type list of units 55-56. dhava as Anogeissus "
               "latifolia is probable; dhātakī as Woodfordia fruticosa is standard. The part of the plant used is not named."),
    "explain_hi": ("यह तीन शब्दों की इकाई एक और विकल्प देती है: अथवा धव (सम्भवतः धौ) और धातकी (धाय) का कल्क। "
                   "कल्क यानी पिसा हुआ गीला लेप। "
                   "पौधे का कौन-सा भाग लेना है और कल्क का क्या करना है, यह इकाई नहीं कहती। "
                   "धातकी की पहचान Woodfordia fruticosa मानक है, धव की Anogeissus latifolia सम्भावित।"),
    "hook": "धव और धाय: दोनों का कल्क।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 57, of which two plants is the paste made?",
            ("Dhava and dhātakī", "धवधातकीकल्कम्: the paste of dhava and dhātakī."),
            [("Priyaṅgu and tila", "That pair is the paste of unit 54."),
             ("Candana and payasyā", "That pair is the paste of unit 60."),
             ("Utpala and padmaka", "That pair makes a decoction in unit 55.")],
            "Or a paste of dhava and dhātakī.",
            "धव + धातकी + कल्क."),
        T(match(1, "Match each word of unit 57 to what the card gives for it.",
                [["धव", "Anogeissus latifolia (probable)"], ["धातकी", "Woodfordia fruticosa (standard)"],
                 ["कल्क", "paste"], ["वा", "or"]],
                "Two plants with their labelled identifications, the preparation and the alternative.",
                "धव (probable), धातकी (standard), कल्क = paste."),
          "The card labels each identification: standard or probable."),
        T(order(2, "Put the parts of धवधातकीकल्कं वा in their printed order.",
                ["धव", "धातकी", "कल्कम्", "वा"],
                "The two plant names come first, then the preparation, then 'or'.",
                "धव → धातकी → कल्कम् → वा.", role="extend"),
          "In धव-धातकी-कल्क the last member (कल्क) is the head: a paste of dhava and dhātakī."),
        mcq("discriminate", 3, "What does कल्क mean in unit 57?",
            ("A paste", "कल्क = paste."),
            [("A decoction", "A decoction is क्वाथ or कषाय."),
             ("A powder", "A powder is चूर्ण (unit 63)."),
             ("A medicated ghee", "Ghee is घृत or सर्पिः.")],
            "कल्क is a paste; this unit's preparation is a paste.",
            "कल्क = paste; क्वाथ/कषाय = decoction; चूर्ण = powder."),
        multi("apply", 4, "Which does unit 57 leave unstated?",
              [("The part of the plant used", "Right: the note says the part is not named."),
               ("What is to be done with the paste", "Right: no verb is stated."),
               ("The names of the two plants", "They are stated: dhava and dhātakī."),
               ("That the preparation is a paste", "It is stated: कल्कम्.")],
              [0, 1],
              "The unit names the plants and the paste, but neither the part used nor the verb.",
              "Elliptical: no verb; part not named."),
        T(mcq("transfer", 5, "By धवधातकीकल्कम्, what does an invented तिलधवचूर्णम् mean (चूर्ण = powder)?",
              ("A powder of tila and dhava", "The last member is the head: चूर्ण of तिल and धव."),
              [("A paste of tila and dhava", "The head is चूर्ण (powder), not कल्क."),
               ("Tila mixed into dhava decoction", "No decoction word is in it."),
               ("Dhava powder without tila", "तिल is a member of the compound.")],
              "धव-धातकी-कल्क = paste of dhava and dhātakī; so तिल-धव-चूर्ण = powder of tila and dhava.",
              "Dvandva of drugs + final preparation noun = that preparation of those drugs."),
          "A drug list followed by a preparation word means that preparation of all the listed drugs."),
    ],
}

# ---------------------------------------------------------------- unit 58
AUTHORED["58"] = {
    "title": "घृतेन वा मधुकमधुरसामृद्वीकाकल्कं",
    "question": "What paste does unit 58 give, and with what?",
    "rule": "Or, with ghee, a paste of madhuka, madhurasā and mṛdvīkā (grape or raisin).",
    "limits": ("Elliptical: no verb and no doṣa are stated; it follows the Pitta-type list. madhurasā's identity is disputed; "
               "mṛdvīkā as Vitis vinifera is standard; madhuka is not identified in this unit. No amount is given."),
    "explain_hi": ("अथवा घी के साथ मधुक, मधुरसा और मृद्वीका (मुनक्का, अंगूर) का कल्क। "
                   "‘घृतेन’ तृतीया विभक्ति है: घी से, घी के साथ। "
                   "मधुरसा की पहचान विवादित है (कई पौधे इस नाम से जाने जाते हैं); मृद्वीका Vitis vinifera मानक पहचान है। "
                   "इकाई में क्रिया नहीं है, न दोष का नाम।"),
    "hook": "घी के साथ: मधुक, मधुरसा, मुनक्का।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 58, with what is the paste of madhuka, madhurasā and mṛdvīkā combined?",
            ("With ghee", "घृतेन = with ghee."),
            [("With honey", "Honey is named in unit 56, not here."),
             ("With milk", "Milk is not named in this unit."),
             ("With oil", "Oil is not named in this unit.")],
            "Or, with ghee, a paste of madhuka, madhurasā and mṛdvīkā.",
            "घृतेन = with ghee (instrumental)."),
        order(1, "Put the members of the compound in unit 58 in their printed order.",
              ["मधुक", "मधुरसा", "मृद्वीका", "कल्कम्"],
              "Three drug names, then the head word कल्क (paste).",
              "मधुक → मधुरसा → मृद्वीका → कल्कम्."),
        T(match(2, "Match each word of unit 58 to its meaning on the card.",
                [["घृतेन", "with ghee"], ["मृद्वीका", "grape or raisin"], ["कल्क", "paste"], ["वा", "or"]],
                "One instrumental, one fruit, the preparation and the alternative.",
                "घृतेन, मृद्वीका, कल्क, वा.", role="extend"),
          "मृद्वीका is grape or raisin (Vitis vinifera, standard)."),
        mcq("discriminate", 3, "What case is घृतेन, and what does it mean?",
            ("Instrumental singular: with ghee", "The gram label: n. inst. sg."),
            [("Locative singular: in ghee", "The locative would be घृते."),
             ("Dative singular: for ghee", "The dative would be घृताय."),
             ("Genitive singular: of ghee", "The genitive would be घृतस्य.")],
            "घृत + एन = instrumental: by means of, together with ghee.",
            "अ-stem neuter: -एन = instrumental singular."),
        multi("apply", 4, "Which labels does the card give for the plants of unit 58?",
              [("mṛdvīkā = grape or raisin (standard)", "Right: Vitis vinifera, standard."),
               ("madhurasā = identity disputed", "Right: several plants carry the name."),
               ("madhurasā = licorice (standard)", "No such identification is given; it is disputed."),
               ("mṛdvīkā = identity disputed", "mṛdvīkā is labelled standard.")],
              [0, 1],
              "mṛdvīkā is a standard identification; madhurasā is disputed and left unidentified.",
              "Use the data's labels exactly: standard, probable, disputed."),
        T(mcq("transfer", 5, "By घृतेन, what does the invented तैलेन वा (तैल = oil) mean?",
              ("Or with oil", "तैल + एन = instrumental: with oil."),
              [("Or in oil", "In oil would be तैले (locative)."),
               ("Or of oil", "Of oil would be तैलस्य (genitive)."),
               ("Or for oil", "For oil would be तैलाय (dative).")],
              "घृत → घृतेन (with ghee); so तैल → तैलेन (with oil).",
              "-एन (अ-stem) = with, by."),
          "अ-stem nouns form the instrumental singular in -एन (-एण after a र् or ष् with no blocking letter)."),
    ],
}

# ---------------------------------------------------------------- unit 59
AUTHORED["59"] = {
    "title": "शम्याकगवाक्षीक्षीरं विरेकः",
    "question": "What does unit 59 name as the purgation (vireka)?",
    "rule": ("The compound of śamyāka, gavākṣī and kṣīra (milk) is named the purgation (vireka): a nominal sentence. "
             "Whether it is a list or 'the milk (latex) of śamyāka and gavākṣī' is left open."),
    "limits": ("The compound can be read as a list (śamyāka, gavākṣī and milk; taken here) or as 'milk (latex) of śamyāka and "
               "gavākṣī'; no question rests on this. śamyāka is probably Cassia fistula (disputed); gavākṣī is Citrullus "
               "colocynthis (probable). No doṣa is named; the unit stands in the Pitta-type list."),
    "explain_hi": ("यह नाम-वाक्य है: शम्याक, गवाक्षी और क्षीर विरेक (विरेचन) है। "
                   "समास दो तरह पढ़ा जा सकता है: तीन वस्तुओं की सूची (यहाँ लिया गया), या ‘शम्याक और गवाक्षी का क्षीर (दूध/रस)’। "
                   "शम्याक सम्भवतः अमलतास (विवादित), गवाक्षी सम्भवतः इन्द्रायण है। "
                   "इकाई दोष का नाम नहीं लेती; यह पित्तज क्रम में आती है।"),
    "hook": "पित्त-क्रम में शोधन: शम्याक-गवाक्षी-क्षीर से विरेक।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In unit 59, what kind of cleansing is named?",
            ("Purgation (विरेक)", "विरेकः = virecana, purgation."),
            [("Emesis (वमन)", "Emesis is named in unit 64, not here."),
             ("A wash (प्रक्षालन)", "The wash is named in units 54 and 61."),
             ("An oil enema (अनुवासन)", "No enema is named in this unit.")],
            "The unit names the compound of śamyāka, gavākṣī and kṣīra as the vireka (purgation).",
            "विरेक = purgation."),
        order(1, "Put the parts of unit 59 in their printed order.",
              ["शम्याक", "गवाक्षी", "क्षीरम्", "विरेकः"],
              "Two plant names, then milk, then the word for purgation.",
              "शम्याक → गवाक्षी → क्षीरम् → विरेकः."),
        T(fill(2, "Unit 59 calls the purgation ____ " + FILL_TAIL,
               accepts("विरेकः", None, "विरेक", "vireka"),
               "विरेकः (nom. sg.) = purgation, virecana.",
               "विरेक = purgation.", "विरेक = virecana, purgation."),
          "विरेक (virecana) is purgation, the downward cleansing."),
        match(3, "Match each word of unit 59 to what the card gives for it.",
              [["शम्याक", "probably Cassia fistula (disputed)"], ["गवाक्षी", "Citrullus colocynthis (probable)"],
               ["क्षीर", "milk (or latex)"], ["विरेक", "purgation"]],
              "Each identification keeps the data's label.",
              "शम्याक (disputed), गवाक्षी (probable), क्षीर, विरेक.", role="discriminate"),
        multi("apply", 4, "Which readings of शम्याकगवाक्षीक्षीरम् does the note allow?",
              [("Śamyāka, gavākṣī and milk (a list)", "Right: the reading taken on the card."),
               ("The milk (latex) of śamyāka and gavākṣī", "Right: the note allows this too."),
               ("Ghee cooked with śamyāka", "No ghee and no cooking are named."),
               ("A wash made of gavākṣī", "The unit calls it विरेकः, purgation, not a wash.")],
              [0, 1],
              "Both readings stand in the note; the card takes the list reading and builds nothing on the choice.",
              "Undecided compound: keep both readings."),
        T(mcq("transfer", 5, "By the pattern of unit 59, what does an invented त्रिफलाक्वाथः प्रक्षालनम् say (त्रिफला = the three fruits)?",
              ("The decoction of triphalā is the wash", "Two nominatives, no verb: X is Y."),
              [("One should drink the decoction of triphalā", "There is no verb such as पिबेत्."),
               ("The wash is made into a triphalā paste", "क्वाथ is a decoction, not a paste."),
               ("Triphalā is cooked in the wash water", "No cooking is stated.")],
              "शम्याकगवाक्षीक्षीरं विरेकः = that compound is the purgation; so त्रिफलाक्वाथः प्रक्षालनम् = the triphalā decoction is the wash.",
              "Nominal sentence: X (nom.) Y (nom.) = X is Y."),
          "A nominal sentence sets two nominatives side by side without a verb: X is Y."),
    ],
}

# ---------------------------------------------------------------- unit 60
AUTHORED["60"] = {
    "title": "चंदनपयस्याकल्कं योनौ धारयेत्",
    "question": "What paste does unit 60 say one should hold in the yoni?",
    "rule": "One should hold a paste (kalka) of candana (sandalwood) and payasyā in the yoni.",
    "limits": ("The text does not say white or red candana (unit 56 says white). payasyā's identity is disputed and not "
               "enriched. No doṣa is named; the unit stands in the Pitta-type list. No amount or duration is given."),
    "explain_hi": ("चन्दन और पयस्या का कल्क योनि में धारण करे। "
                   "यहाँ चन्दन का रंग नहीं बताया गया; इकाई ५६ में ‘श्वेत चन्दन’ कहा था। "
                   "पयस्या की पहचान विवादित है, इसलिए उसका कोई आधुनिक नाम नहीं दिया गया। "
                   "‘धारयेत्’ विधिलिङ् है: धारण करे, रखे रहे।"),
    "hook": "चन्दन-पयस्या का लेप, भीतर धारण।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 60, where is the paste of candana and payasyā to be held?",
            ("In the yoni", "योनौ धारयेत्: should hold in the yoni."),
            [("In the mouth", "The mouth is not named in this unit."),
             ("On the navel", "The navel is not named in this unit."),
             ("On the forehead", "The forehead is not named in this unit.")],
            "One should hold a paste of candana and payasyā in the yoni.",
            "योनौ = in the yoni; धारयेत् = should hold."),
        order(1, "Put the parts of unit 60 in their printed order.",
              ["चन्दन", "पयस्या", "कल्कम्", "योनौ", "धारयेत्"],
              "Two drugs, the paste, the place, the verb.",
              "चन्दन → पयस्या → कल्कम् → योनौ → धारयेत्."),
        T(match(2, "Match each word of unit 60 to its meaning on the card.",
                [["चन्दन", "sandalwood"], ["कल्क", "paste"], ["योनौ", "in the yoni"], ["धारयेत्", "should hold, retain"]],
                "Drug, preparation, place and action.",
                "चन्दन, कल्क, योनौ, धारयेत्.", role="extend"),
          "धारयेत् (optative, causative of √धृ) = should hold, retain."),
        mcq("discriminate", 3, "What does unit 60 say about the colour of the candana?",
            ("Nothing: white or red is not said", "The note: the text does not say white or red."),
            [("It is white, as in unit 56", "Unit 56 says श्वेत; unit 60 does not."),
             ("It is red sandalwood", "Red is not stated anywhere in the unit."),
             ("It is yellow sandalwood", "No colour is stated in the unit.")],
            "Unit 60 says only चन्दन; unit 56 had श्वेतचन्दन.",
            "Do not carry a word from one unit into another."),
        mcq("apply", 4, "What does the card give as the modern identification of payasyā?",
            ("None: its identity is disputed", "The note: payasyā identity disputed, not enriched."),
            [("Santalum album (standard)", "That is white sandalwood (probable), not payasyā."),
             ("Woodfordia fruticosa (standard)", "That is dhātakī, unit 57."),
             ("Vitis vinifera (standard)", "That is mṛdvīkā, unit 58.")],
            "payasyā is left unidentified because its identity is disputed.",
            "Disputed name: no modern name is given."),
        T(mcq("transfer", 5, "By धारयेत्, what does the invented लिखेत् (√लिख्, write) mean?",
              ("He should write", "-एत् = 3rd singular optative: should do."),
              [("He wrote", "A past form would be अलिखत् or लिलेख."),
               ("He will write", "The future is लेखिष्यति."),
               ("They should write", "The plural optative is लिखेयुः.")],
              "धारयेत् = he should hold; so लिखेत् = he should write.",
              "-एत् = optative 3 sg.: should."),
          "The optative 3rd singular ends in -एत् and gives the instruction 'one should ...'."),
    ],
}

# ---------------------------------------------------------------- unit 61
AUTHORED["61"] = {
    "title": "गैरिकारिष्टकषायः प्रक्षालनं",
    "question": "What does unit 61 name as the wash (prakṣālana)?",
    "rule": "A decoction of gairika (red ochre) and ariṣṭa is the wash (prakṣālana): a nominal sentence.",
    "limits": ("gairika is a mineral, so its 'decoction' is literal to the print only; the sense may be ariṣṭa decocted with "
               "gairika. ariṣṭa is probably neem (disputed; soapnut also proposed). What is washed and the doṣa are not named."),
    "explain_hi": ("गैरिक (लाल गेरू) और अरिष्ट का काढ़ा प्रक्षालन है। "
                   "गेरू एक खनिज है; इसलिए ‘उसका काढ़ा’ केवल छपे शब्दों के अनुसार है, अर्थ सम्भवतः गेरू सहित अरिष्ट का काढ़ा है। "
                   "अरिष्ट सम्भवतः नीम है (विवादित; रीठा भी सुझाया गया है)। "
                   "सन्धि: गैरिक + अरिष्ट → गैरिकारिष्ट (अ + अ → आ)।"),
    "hook": "गेरू और नीम(?) का काढ़ा: पित्त-क्रम का प्रक्षालन।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 61, what is the decoction of gairika and ariṣṭa used as?",
            ("The wash (प्रक्षालन)", "गैरिकारिष्टकषायः प्रक्षालनम्."),
            [("The purgation (विरेक)", "The purgation is named in unit 59."),
             ("The emesis (वमन)", "Emesis is named in unit 64."),
             ("A drink with honey", "No drinking or honey is named here.")],
            "The decoction of gairika and ariṣṭa is the wash.",
            "प्रक्षालन = washing, rinsing."),
        match(1, "Match each word of unit 61 to what the card gives for it.",
              [["गैरिक", "red ochre (a mineral)"], ["अरिष्ट", "probably neem (disputed)"],
               ["कषाय", "decoction"], ["प्रक्षालन", "washing, rinsing"]],
              "One mineral, one plant, the preparation and its use.",
              "गैरिक, अरिष्ट, कषाय, प्रक्षालन."),
        T(order(2, "Put the parts of unit 61 in their printed order.",
                ["गैरिक", "अरिष्ट", "कषायः", "प्रक्षालनम्"],
                "Mineral, plant, decoction, wash.",
                "गैरिक → अरिष्ट → कषायः → प्रक्षालनम्.", role="extend"),
          "The unit is a nominal sentence: the decoction (nom.) is the wash (nom.)."),
        mcq("discriminate", 3, "Which split of गैरिकारिष्ट is right?",
            ("गैरिक + अरिष्ट", "अ + अ → आ: गैरिक + अरिष्ट → गैरिकारिष्ट."),
            [("गैरिका + रिष्ट", "रिष्ट is not a word of the card."),
             ("गैरिकः + अरिष्ट", "अः + अ would give गैरिकोऽरिष्ट."),
             ("गैरि + कारिष्ट", "Neither गैरि nor कारिष्ट is a word of the card.")],
            "गैरिक (red ochre) + अरिष्ट (probably neem): the two अ merge into आ.",
            "अ + अ → आ."),
        mcq("apply", 4, "Why does the card hedge the 'decoction of gairika'?",
            ("Gairika is a mineral, not a plant", "The note: the sense may be a decoction of ariṣṭa with gairika."),
            [("Gairika's identity is disputed", "Gairika as red ochre is labelled standard."),
             ("The word कषाय is damaged in print", "No text flag marks this unit."),
             ("Gairika is named in another unit", "That is no reason; the hedge is about it being a mineral.")],
            "Red ochre is a mineral; boiling it is literal to the print, so the card keeps the alternative sense open.",
            "Hedge what the note hedges."),
        T(mcq("transfer", 5, "By the rule of गैरिकारिष्ट, how is the invented धर्म + अर्थ written when joined?",
              ("धर्मार्थ", "अ + अ → आ."),
              [("धर्मोर्थ", "अ + अ does not give ओ."),
               ("धर्मअर्थ", "Two vowels do not stand side by side inside a compound."),
               ("धर्मर्थ", "The second अ cannot simply drop.")],
              "गैरिक + अरिष्ट → गैरिकारिष्ट; so धर्म + अर्थ → धर्मार्थ.",
              "अ + अ → आ."),
          "Two short or long अ/आ meeting merge into one long आ."),
    ],
}

# ---------------------------------------------------------------- unit 62
AUTHORED["62"] = {
    "title": "श्लैष्मिके कुटजकटुकाऽश्वगंधाक्वाथं पिबेत्",
    "question": "In the Kapha-type, what decoction does unit 62 say one should drink?",
    "rule": ("In the Kapha-type one should drink a decoction of kuṭaja, kaṭukā and aśvagandhā; the second line, "
             "an alternative with honey, is damaged."),
    "limits": ("Low confidence. Line 2 is damaged: क्षीरिवृक्षभवालकाथं cannot be restored (perhaps a decoction of something of "
               "the milk-trees); nothing is built on it, nor on what समाक्षिकम् (with honey) goes with. kuṭaja and aśvagandhā "
               "are standard identifications, kaṭukā (Picrorhiza kurroa) probable."),
    "explain_hi": ("यहाँ से श्लैष्मिक (कफज) आर्तवदोष की चिकित्सा आरम्भ होती है। "
                   "कुटज (कुड़ा), कटुका (सम्भवतः कुटकी) और अश्वगन्धा का क्वाथ पीए। "
                   "दूसरी पंक्ति क्षतिग्रस्त है: ‘समाक्षिकं’ (शहद सहित) पढ़ा जाता है, पर ‘क्षीरिवृक्षभवालकाथं’ कोई शब्द नहीं; "
                   "सम्भवतः क्षीरी वृक्षों (दूधिया रस वाले पेड़) से जुड़ा कोई काढ़ा, पर बीच का भाग पुनः नहीं बनता। "
                   "इसलिए प्रश्न केवल पहली पंक्ति पर हैं।"),
    "hook": "कफ में कड़वा क्वाथ: कुटज, कुटकी, अश्वगन्धा।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In unit 62, which three drugs make the decoction for the Kapha-type?",
            ("Kuṭaja, kaṭukā and aśvagandhā", "कुटजकटुकाऽश्वगंधाक्वाथं पिबेत्."),
            [("Utpala, padmaka and kāśmarya", "These belong to the Pitta-type decoctions of unit 55."),
             ("Dhava, dhātakī and madhuka", "These are from the pastes of units 57-58."),
             ("Gairika, ariṣṭa and candana", "These are from units 60-61.")],
            "In the Kapha-type one should drink a decoction of kuṭaja, kaṭukā and aśvagandhā.",
            "श्लैष्मिके: कुटज, कटुका, अश्वगन्धा."),
        order(1, "Put these words of line 1 of unit 62 in their printed order.",
              ["श्लैष्मिके", "कुटज", "कटुका", "अश्वगन्धा", "क्वाथम्", "पिबेत्"],
              "The doṣa, three drugs, the decoction, the verb.",
              "श्लैष्मिके → कुटज → कटुका → अश्वगन्धा → क्वाथम् → पिबेत्."),
        T(match(2, "Match each word of unit 62 to what the card gives for it.",
                [["श्लैष्मिके", "in the Kapha-type (one)"], ["कुटज", "Holarrhena antidysenterica (standard)"],
                 ["कटुका", "Picrorhiza kurroa (probable)"], ["अश्वगन्धा", "Withania somnifera (standard)"]],
                "The doṣa word and the three drugs, each with its label.",
                "श्लैष्मिक = Kapha-type; कुटज, कटुका, अश्वगन्धा.", role="extend"),
          "श्लैष्मिक (from श्लेष्मन्, Kapha) = of the Kapha type."),
        mcq("discriminate", 3, "How is कटुकाऽश्वगंधा to be split, by the card?",
            ("कटुका + अश्वगन्धा; the ऽ is a print habit", "आ + अ → आ; the note: not an elision."),
            [("कटुके + अश्वगन्धा, with ए + अ → एऽ", "ए + अ would print कटुकेऽश्वगन्धा, with ए."),
             ("कटुकः + अश्वगन्धा, with अः + अ → ओऽ", "That would print कटुकोऽश्वगन्धा, with ओ."),
             ("कटुका + शवगन्धा, a separate word", "शवगन्धा is not a word of the card.")],
            "कटुका + अश्वगन्धा → कटुकाश्वगन्धा; the printed ऽ marks no elided letter here.",
            "आ + अ → आ; ऽ here is a print habit."),
        mcq("apply", 4, "Why does the card build no question on क्षीरिवृक्षभवालकाथं?",
            ("The print is damaged and cannot be restored", "The flag: 'bhavālakātha' is not a word."),
            [("It is a well-known standard drug", "It is not even a restorable word."),
             ("It repeats the first line", "Nothing shows it repeats line 1."),
             ("It belongs to the Pitta-type list", "It stands under श्लैष्मिके; the problem is damage.")],
            "Only the beginning looks like क्षीरिवृक्ष (milk-trees); the middle cannot be restored.",
            "Build no question on a damaged reading."),
        T(mcq("transfer", 5, "By the join of कटुका + अश्वगन्धा, how is the invented विद्या + अर्थी written?",
              ("विद्यार्थी", "आ + अ → आ."),
              [("विद्योर्थी", "आ + अ does not give ओ."),
               ("विद्यअर्थी", "The two vowels must merge."),
               ("विद्येर्थी", "आ + अ does not give ए.")],
              "कटुका + अश्वगन्धा → कटुकाश्वगन्धा; so विद्या + अर्थी → विद्यार्थी.",
              "आ + अ → आ."),
          "आ (or अ) followed by अ (or आ) merges into one आ."),
    ],
}

# ---------------------------------------------------------------- unit 63
AUTHORED["63"] = {
    "title": "एतेषामेव वा चूर्ण",
    "question": "What does unit 63 say one may do with the powder of these drugs?",
    "rule": "Or one should lick the powder of just these (the preceding Kapha-type drugs), with honey and ghee.",
    "limits": ("एतेषाम् (of these) points back to the preceding Kapha-type drugs; which ones is not stated. The printed चूर्ण "
               "probably lacks its anusvāra (चूर्णम्). No proportions of honey and ghee are given."),
    "explain_hi": ("अथवा इन्हीं (पिछली कफज औषधियों) का चूर्ण शहद और घी के साथ चाटे। "
                   "‘एतेषाम्’ किन औषधियों की ओर संकेत है, यह ठीक-ठीक नहीं कहा गया। "
                   "‘मधुघृताभ्याम्’ द्विवचन तृतीया है: शहद और घी, दो वस्तुओं के साथ; अनुपात नहीं दिया। "
                   "छपा ‘चूर्ण’ सम्भवतः ‘चूर्णं’ है (अनुस्वार छूटा)।"),
    "hook": "इन्हीं का चूर्ण, शहद-घी में चाटो।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 63, what is to be done with the powder?",
            ("It is licked with honey and ghee", "मधुघृताभ्यां लिह्यात्."),
            [("It is held in the yoni", "No धारयेत् appears in this unit."),
             ("It is boiled into a wash", "No wash is named in this unit."),
             ("It is drunk with milk", "Milk is not named; the verb is लिह्यात्, lick.")],
            "Or one should lick the powder of just these with honey and ghee.",
            "लिह्यात् = should lick."),
        order(1, "Put the words of unit 63 in their printed order.",
              ["एतेषामेव", "वा", "चूर्ण", "मधुघृताभ्यां", "लिह्यात्"],
              "Of just these, or, powder, with honey and ghee, should lick.",
              "एतेषामेव → वा → चूर्ण → मधुघृताभ्यां → लिह्यात्."),
        T(match(2, "Match each word of unit 63 to its meaning on the card.",
                [["एतेषाम्", "of these"], ["एव", "just, only"], ["चूर्ण", "powder"],
                 ["मधुघृताभ्याम्", "with honey and ghee"], ["लिह्यात्", "should lick"]],
                "Every word of the unit, from 'of these' to 'should lick'.",
                "एतेषाम्, एव, चूर्ण, मधुघृताभ्याम्, लिह्यात्.", role="extend"),
          "लिह्यात् (optative of √लिह्) = should lick."),
        mcq("discriminate", 3, "Why does मधुघृताभ्याम् have the dual ending -आभ्याम्?",
            ("It joins two things, honey and ghee", "A dvandva of two members takes the dual."),
            [("It is a genitive plural", "The genitive plural would end in -आनाम्."),
             ("It is a locative singular", "The locative singular would be मधुघृते."),
             ("It shows a large amount", "No amount is stated; the dual counts two items.")],
            "मधु + घृत, two items, in the dual instrumental: with honey and ghee.",
            "Dvandva of two = dual; -आभ्याम् = instrumental (or dative/ablative) dual."),
        multi("apply", 4, "Which does unit 63 leave unstated?",
              [("The proportions of honey and ghee", "Right: no proportions are given."),
               ("Exactly which drugs एतेषाम् means", "Right: the note says not stated which."),
               ("That the powder is licked", "It is stated: लिह्यात्."),
               ("That honey and ghee are used", "It is stated: मधुघृताभ्याम्.")],
              [0, 1],
              "Stated: powder, licked, with honey and ghee. Unstated: proportions and which drugs exactly.",
              "Separate what the unit says from what it leaves open."),
        T(mcq("transfer", 5, "By मधुघृताभ्याम्, what does the invented क्षीरघृताभ्याम् mean (क्षीर = milk)?",
              ("With milk and ghee", "Dvandva of two + -आभ्याम् = with the two."),
              [("Of milk and ghee", "Of the two would be क्षीरघृतयोः."),
               ("In milk and ghee", "In the two would also be क्षीरघृतयोः."),
               ("With milk, without ghee", "Both members are included.")],
              "मधुघृताभ्याम् = with honey and ghee; so क्षीरघृताभ्याम् = with milk and ghee.",
              "X-Y-आभ्याम् = with X and Y."),
          "A two-member dvandva in the instrumental dual means 'with X and Y'."),
    ],
}

# ---------------------------------------------------------------- unit 64
AUTHORED["64"] = {
    "title": "मदनफलकषायेण वमनं",
    "question": "With what does unit 64 say emesis (vamana) is done?",
    "rule": "Vamana (emesis) with a decoction of madanaphala.",
    "limits": ("Elliptical: no verb. madanaphala is identified at unit 50 as the fruit of madana, Randia dumetorum (standard). "
               "No doṣa is named; the unit stands in the Kapha-type list begun at unit 62. No amount is given."),
    "explain_hi": ("मदनफल के काढ़े से वमन। "
                   "मदनफल यानी मैनफल (Randia dumetorum, मानक पहचान, इकाई ५० में दी गई)। "
                   "‘कषायेण’ तृतीया है: काढ़े से, काढ़े के द्वारा। "
                   "इकाई में क्रिया नहीं है; यह कफज क्रम में आती है, जैसे पित्तज क्रम में विरेक (इकाई ५९) आया था।"),
    "hook": "कफ में ऊपर से निकालो: मैनफल का काढ़ा, वमन।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In unit 64, what is done with the decoction of madanaphala?",
            ("Emesis (वमन)", "मदनफलकषायेण वमनम्."),
            [("Purgation (विरेक)", "Purgation is named in unit 59."),
             ("A wash (प्रक्षालन)", "No wash is named in this unit."),
             ("A paste held in the yoni", "That comes in unit 65.")],
            "Vamana (emesis) with a decoction of madanaphala.",
            "वमन = emesis."),
        order(1, "Put the parts of unit 64 in their printed order.",
              ["मदन", "फल", "कषायेण", "वमनम्"],
              "The drug (madana fruit), the decoction, then emesis.",
              "मदन → फल → कषायेण → वमनम्."),
        T(fill(2, "Unit 64 names emesis as ____ " + FILL_TAIL,
               accepts("वमनम्", None, "वमन", "vamana"),
               "वमनम् = vamana, emesis.",
               "वमन = emesis.", "वमन = emesis."),
          "वमन (vamana) is emesis, the upward cleansing."),
        mcq("discriminate", 3, "How does वमन (unit 64) differ from विरेक (unit 59)?",
            ("वमन is emesis; विरेक is purgation", "The card glosses: वमन = emesis, विरेक = purgation."),
            [("वमन is purgation; विरेक is emesis", "The two are swapped."),
             ("Both are kinds of wash", "The wash is प्रक्षालन."),
             ("Both mean an oil enema", "An oil enema is अनुवासन, not named here.")],
            "Emesis (वमन) with madanaphala here; purgation (विरेक) in unit 59.",
            "वमन = emesis; विरेक = purgation."),
        match(4, "Match each part of unit 64 to its meaning on the card.",
              [["मदनफल", "fruit of madana (Randia dumetorum)"], ["कषाय", "decoction"],
               ["-एण in कषायेण", "with, by means of"], ["वमन", "emesis"]],
              "Drug, preparation, the instrumental ending and the procedure.",
              "मदनफल, कषाय, -एण (instrumental), वमन.", role="apply"),
        T(mcq("transfer", 5, "कषायेण has ण after ष. By the same rule, how is the instrumental of क्षीर (milk) spelt?",
              ("क्षीरेण", "र् followed only by a vowel before न turns it into ण."),
              [("क्षीरेन", "After र् with no blocking letter, न must become ण."),
               ("क्षीरैण", "The ending is -एण, not -ऐण."),
               ("क्षीराण", "The instrumental singular is not -आण.")],
              "In कषायेण, ष turns the न of -एन into ण; so क्षीर + एन → क्षीरेण.",
              "ऋ, र्, ष् turn a following न into ण unless a blocking letter intervenes."),
          "After ऋ, र् or ष् in the same word, न becomes ण unless a dental, palatal or retroflex consonant (or श, स, ल) comes between."),
    ],
}

# ---------------------------------------------------------------- unit 65
AUTHORED["65"] = {
    "title": "तत्कल्कमेव च योनौ धारयेत्",
    "question": "Whose paste does unit 65 say one should hold in the yoni?",
    "rule": "And one should hold just its paste (of madanaphala, on the plain reading) in the yoni.",
    "limits": ("Medium confidence. तत् is taken as madanaphala of unit 64, the nearest drug; this is the plain reading, not stated "
               "in the unit. No amount or duration is given."),
    "explain_hi": ("और उसी का कल्क योनि में धारण करे। "
                   "‘तत्’ यानी वह: सबसे पास की औषधि, इकाई ६४ का मदनफल; यह सीधा अर्थ है, इकाई स्वयं नाम नहीं लेती। "
                   "‘एव’ जोर देता है: उसी का कल्क। "
                   "इस तरह एक ही मदनफल काढ़े के रूप में वमन के लिए और कल्क के रूप में योनि-धारण के लिए आता है।"),
    "hook": "वही मैनफल: काढ़ा वमन में, कल्क भीतर।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "On the card's plain reading, whose paste is तत्कल्कम् in unit 65?",
            ("Madanaphala's, from unit 64", "The note: तत् = madanaphala, the nearest drug."),
            [("Candana's, from unit 60", "Candana is not the nearest drug."),
             ("Kuṭaja's, from unit 62", "Kuṭaja is not the nearest drug."),
             ("Dhātakī's, from unit 57", "Dhātakī is far back, in the Pitta-type list.")],
            "तत् points to the nearest drug, the madanaphala of unit 64.",
            "तत् = that, its: the nearest drug."),
        order(1, "Put the words of unit 65 in their printed order.",
              ["तत्कल्कम्", "एव", "च", "योनौ", "धारयेत्"],
              "Its paste, just, and, in the yoni, should hold.",
              "तत्कल्कम् → एव → च → योनौ → धारयेत्."),
        T(match(2, "Match each word of unit 65 to its meaning on the card.",
                [["तत्", "that (its)"], ["कल्क", "paste"], ["एव", "just, only"], ["च", "and"], ["धारयेत्", "should hold"]],
                "The whole unit, word by word.",
                "तत्, कल्क, एव, च, धारयेत्.", role="extend"),
          "तत्कल्क is a tatpuruṣa: the paste of that (drug)."),
        mcq("discriminate", 3, "Which split of तत्कल्कमेव is right?",
            ("तत्कल्कम् + एव", "Final म् joins the vowel ए: तत्कल्कमेव."),
            [("तत्कल्कमे + व", "तत्कल्कमे and व are not words of the card."),
             ("तत्कल्कः + एव", "अः + ए would give तत्कल्क एव."),
             ("तत्कल्क + मेव", "मेव is not a word; एव is.")],
            "तत्कल्कम् (its paste, acc.) + एव (just).",
            "म् + vowel → joined."),
        mcq("apply", 4, "A student translates unit 65 as: one should drink its paste. What is wrong?",
            ("धारयेत् means should hold, in the yoni", "The verb is धारयेत् with योनौ, not पिबेत्."),
            [("तत् means honey, not madanaphala", "तत् is a pronoun, that; it does not mean honey."),
             ("कल्क means a decoction", "कल्क is a paste."),
             ("Nothing; drinking is right", "The unit has no verb of drinking.")],
            "The paste is held in the yoni (योनौ धारयेत्); nothing is drunk in this unit.",
            "धारयेत् = should hold; पिबेत् = should drink."),
        T(mcq("transfer", 5, "How is the invented तत् + चूर्णम् (its powder) written when joined?",
              ("तच्चूर्णम्", "त् before च becomes च्: तच्च."),
              [("तत्चूर्णम्", "त् does not stay before च."),
               ("तद्चूर्णम्", "द् comes before voiced sounds, not before च."),
               ("तञ्चूर्णम्", "त् turns nasal only before a nasal (as in न्म), not before च.")],
              "In तत्कल्कम्, त् stays before क; before च it becomes च्: तच्चूर्णम्.",
              "त् + च → च्च."),
          "Final त् stays before क, but before च/छ it becomes च्."),
    ],
}

# ---------------------------------------------------------------- unit 66
AUTHORED["66"] = {
    "title": "प्रक्षालनं बस्तमेषमूत्रं वा",
    "question": "What does unit 66 name as the wash, and what is its alternative?",
    "rule": ("A decoction of an unclear compound is the wash (prakṣālana), or the urine of he-goat and sheep."),
    "limits": ("Low confidence. रोधार्तिदुक is damaged, no known drug; lodhra + tinduka is a possible reading only, not adopted; "
               "nothing is built on it. बस्त could mean bladder; मेष beside it makes animals the sense. No condition or doṣa is named."),
    "explain_hi": ("अनुमानित पाठ पर, किसी अस्पष्ट पद ‘रोधार्तिदुक’ का काढ़ा प्रक्षालन है, अथवा बकरे और भेड़ का मूत्र। "
                   "‘रोधार्तिदुक’ कोई ज्ञात औषधि नहीं; लोध्र + तिन्दुक एक सम्भव पाठ है, पर अपनाया नहीं गया। "
                   "‘बस्त’ का अर्थ मूत्राशय भी हो सकता है, पर साथ में ‘मेष’ (भेड़) होने से यहाँ बकरा ही अर्थ है। "
                   "प्रश्न केवल पक्के भाग पर हैं: प्रक्षालन और बस्त-मेष-मूत्र।"),
    "hook": "धोने को: एक अस्पष्ट काढ़ा, या बकरे-भेड़ का मूत्र।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 66, whose urine is named?",
            ("Of he-goat and sheep", "बस्तमेषमूत्रम्: basta = he-goat, meṣa = sheep."),
            [("Of cow and buffalo", "Neither is named in this unit."),
             ("Of horse and donkey", "Neither is named in this unit."),
             ("Of camel and elephant", "Neither is named in this unit.")],
            "The alternative is the urine of he-goat and sheep.",
            "बस्त = he-goat; मेष = sheep; मूत्र = urine."),
        order(1, "Put these words of unit 66 in their printed order.",
              ["प्रक्षालनम्", "बस्त", "मेष", "मूत्रम्", "वा"],
              "The wash, then he-goat, sheep, urine, or.",
              "प्रक्षालनम् → बस्त → मेष → मूत्रम् → वा."),
        T(match(2, "Match each word of unit 66 to its meaning on the card.",
                [["प्रक्षालन", "washing, rinsing"], ["बस्त", "he-goat"], ["मेष", "sheep"], ["मूत्र", "urine"], ["वा", "or"]],
                "The sure words of the unit.",
                "प्रक्षालन, बस्त, मेष, मूत्र, वा.", role="extend"),
          "मेष = sheep (ram); बस्त = he-goat."),
        mcq("discriminate", 3, "Why does the card take बस्त as he-goat rather than bladder?",
            ("Because मेष (sheep) stands beside it", "The note: मेष beside it makes animals the sense."),
            [("Because बस्त never means bladder", "The note says it can mean bladder."),
             ("Because the print spells it बस्ति", "The print has बस्त."),
             ("Because urine needs no animal", "That gives no reason for he-goat.")],
            "बस्त can mean bladder, but beside मेष (sheep) the sense is the animal.",
            "A neighbouring word can decide a two-way meaning."),
        mcq("apply", 4, "What does the card say about रोधार्तिदुककषायः?",
            ("Damaged; only 'a decoction of an unclear word'", "Kept unsplit; lodhra + tinduka not adopted."),
            [("It is lodhra and tinduka, as restored", "Lodhra + tinduka is only a possible reading, not adopted."),
             ("It is the urine of goat and sheep", "The urine is the alternative named after वा."),
             ("It is a paste held in the yoni", "No धारयेत् appears; it is a wash.")],
            "The compound is damaged; the card reads only its ending, कषाय (decoction), and builds nothing on the rest.",
            "Build no question on a damaged reading."),
        T(mcq("transfer", 5, "In कषायः प्रक्षालनम् the visarga stays before प. How is the invented क्वाथः + पानम् written?",
              ("क्वाथः पानम्", "Visarga stays before प (a hard consonant)."),
              [("क्वाथो पानम्", "अः → ओ only before a voiced sound; प is not voiced."),
               ("क्वाथस्पानम्", "Visarga → स् before त/थ, not before प."),
               ("क्वाथर्पानम्", "Visarga → र् only after vowels other than अ/आ before voiced sounds.")],
              "कषायः प्रक्षालनम् keeps the visarga; so क्वाथः पानम्.",
              "Visarga + क/ख/प/फ: stays."),
          "Before क, ख, प, फ (and before श, ष, स, optionally) a visarga stays as visarga."),
    ],
}

# ===================================================================== NOTES_HI
NOTES_HI = {
    "54": ("दो छपी पंक्तियाँ (०२.०१.५९ और ६०) जुड़ी हैं। विश्वास ऊँचा। "
           "छपा ‘प्रियंगु’ = प्रियङ्गु (ङ्ग के स्थान पर अनुस्वार, छपाई की आदत)। ‘कल्क’ यहाँ पुंलिङ्ग माना गया। "
           "दूसरी पंक्ति नाम-वाक्य है; किसका प्रक्षालन, पाठ नहीं कहता (सम्भवतः योनि का)। "
           "सन्धियाँ: कल्कम् + वा → कल्कं वा; कषायः + प्रक्षालनम् → कषायः प्रक्षालनम् (प से पहले विसर्ग बना रहता है)। "
           "‘योनौ’ इ-कारान्त स्त्रीलिङ्ग का सप्तमी एकवचन है, द्विवचन नहीं।"),
    "55": ("विश्वास मध्यम। ‘क्वाथ’ तीन बार आता है; ‘वासशर्करं’ एक के साथ है या तीनों के साथ, या दो और वस्तुएँ हैं, संस्कृत से तय नहीं। "
           "‘मधुकपुष्प-काश्मर्यफल’ लिया गया; ‘मधुक; काश्मर्य के पुष्प और फल’ भी सम्भव। "
           "छपा ‘वास’ ह्रस्व अ से है, ‘वासा’ (अडूसा) पढ़ा गया: सम्भावित, निश्चित नहीं। काकोली की पहचान विवादित। "
           "सन्धियाँ: क्वाथम् + उत्पल → क्वाथमुत्पल; क्वाथम् + मधुक → क्वाथं मधुक; शर्करम् + पिबेत् → शर्करं पिबेत्।"),
    "56": ("अधूरा वाक्य: ‘पिबेत्’ यहाँ नहीं कहा गया। श्वेत चन्दन = Santalum album (सम्भावित); क्षौद्र = शहद (मानक)। "
           "‘सक्षौद्रम्’ बहुव्रीहि: स + क्षौद्र। सन्धि: क्वाथम् + वा → क्वाथं वा।"),
    "57": ("अधूरा वाक्य, क्रिया नहीं। धव = Anogeissus latifolia (सम्भावित); धातकी = Woodfordia fruticosa (मानक)। "
           "पौधे का भाग नहीं बताया। सन्धि: कल्कम् + वा → कल्कं वा।"),
    "58": ("विश्वास मध्यम। अधूरा वाक्य। मधुरसा की पहचान विवादित (कई पौधे इस नाम के), इसलिए आधुनिक नाम नहीं; "
           "मृद्वीका = Vitis vinifera (मानक)। इस इकाई में मधुक की पहचान नहीं दी गई। "
           "समास में सन्धि नहीं (मधुरसा + मृद्वीका: आ के बाद व्यंजन)।"),
    "59": ("विश्वास मध्यम। नाम-वाक्य। समास दो तरह: ‘शम्याक, गवाक्षी और क्षीर’ (लिया गया) या ‘शम्याक और गवाक्षी का क्षीर (दूधिया रस)’; "
           "इस पर कोई प्रश्न नहीं। शम्याक = सम्भवतः Cassia fistula (विवादित); गवाक्षी = Citrullus colocynthis (सम्भावित)। "
           "सन्धि: क्षीरम् + विरेकः → क्षीरं विरेकः।"),
    "60": ("चन्दन का रंग (श्वेत या रक्त) नहीं कहा गया; इकाई ५६ में श्वेत था। पयस्या की पहचान विवादित (इकाई ४७ देखें)। "
           "सन्धि: कल्कम् + योनौ → कल्कं योनौ। (डेटा का नोट पंक्ति-संख्या ‘62’ और ‘50’ देता है, जो इकाई ५६ और ४७ हैं।)"),
    "61": ("विश्वास मध्यम। गैरिक खनिज (लाल गेरू) है, इसलिए उसका ‘कषाय’ केवल छपे पाठ के अनुसार; अर्थ सम्भवतः गेरू सहित अरिष्ट का काढ़ा। "
           "अरिष्ट = सम्भवतः नीम (विवादित; रीठा भी सुझाया गया)। "
           "सन्धियाँ: गैरिक + अरिष्ट → गैरिकारिष्ट (अ + अ → आ); कषायः + प्रक्षालनम् (विसर्ग बना रहता है)।"),
    "62": ("विश्वास कम। दो पंक्तियाँ (०२.०१.६८ और ६९)। दूसरी पंक्ति का ‘क्षीरिवृक्षभवालकाथं’ क्षतिग्रस्त है: "
           "‘भवालकाथ’ कोई शब्द नहीं; सम्भवतः क्षीरी वृक्षों (दूधिया रस वाले, अंजीर-वर्ग, सम्भावित) से जुड़ा कोई क्वाथ, बीच का भाग पुनः नहीं बनता; बिना विच्छेद रखा गया। "
           "‘समाक्षिकम्’ = मधु सहित (माक्षिक नाम का खनिज भी है, पर सीधा अर्थ शहद)। "
           "‘कटुकाऽश्वगंधा’ का ऽ छपाई की आदत है, लोप नहीं: कटुका + अश्वगन्धा (आ + अ → आ)। सन्धि: क्वाथम् + पिबेत् → क्वाथं पिबेत्।"),
    "63": ("छपा ‘चूर्ण’ सम्भवतः ‘चूर्णं’ है (अनुस्वार छूटा; द्वितीया एकवचन चाहिए)। "
           "‘एतेषाम्’ पिछली कफज औषधियों की ओर, कौन-सी, नहीं कहा। ‘मधुघृताभ्याम्’ द्वन्द्व, तृतीया द्विवचन; अनुपात नहीं। "
           "सन्धियाँ: एतेषाम् + एव → एतेषामेव; मधुघृताभ्याम् + लिह्यात् → मधुघृताभ्यां लिह्यात्।"),
    "64": ("अधूरा वाक्य, क्रिया नहीं। मदनफल की पहचान इकाई ५० में: Randia dumetorum (मानक), हिन्दी मैनफल "
           "(डेटा का नोट ‘unit 53’ कहता है, जो पंक्ति ०२.०१.५३ यानी इकाई ५० है)। "
           "‘कषायेण’ में ण: ष के बाद न का ण (णत्व)।"),
    "65": ("विश्वास मध्यम। ‘तत्’ = इकाई ६४ का मदनफल (सबसे पास की औषधि; सीधा अर्थ, इकाई में नाम नहीं)। "
           "सन्धियाँ: तत् + कल्कम् → तत्कल्कम् (क से पहले त् बना रहता है); तत्कल्कम् + एव → तत्कल्कमेव।"),
    "66": ("विश्वास कम। ‘रोधार्तिदुक’ क्षतिग्रस्त, कोई ज्ञात औषधि नहीं; ‘रोध-’ सम्भवतः लोध्र; लोध्र + तिन्दुक एक सम्भव पाठ, अपनाया नहीं गया; "
           "बिना विच्छेद रखा। अन्त का ‘कषाय’ काढ़ा पढ़ा गया। ‘बस्त’ = बकरा (मूत्राशय भी अर्थ, पर ‘मेष’ साथ होने से पशु)। "
           "मूत्र बिना किसी शर्त के कहा गया। सन्धियाँ: कषायः + प्रक्षालनम्; प्रक्षालनम् + बस्त → प्रक्षालनं बस्त; मूत्रम् + वा → मूत्रं वा।"),
}

# ===================================================================== AIDS
AIDS = {
    "54": {
        "diagram": {"groups": [
            {"label": "योनौ धारयेत्", "items": ["प्रियंगु", "तिल", "कल्क"]},
            {"label": "प्रक्षालनम्", "items": ["सरल", "मुद्गपर्णी", "कषाय"]}]},
        "sandhi": "म् + व → ं व: कल्कम् + वा → कल्कं वा · अः + प: कषायः + प्रक्षालनम् (विसर्ग बना रहता है)।",
        "contrast": "धारण: कल्क (लेप), भीतर रखना ↔ प्रक्षालन: कषाय (काढ़ा), धोना।",
        "frame": "इकाई दोष का नाम नहीं लेती; क्रम से यह वातज आर्तवदोष (इकाई ५२ से) की चिकित्सा में आती है।",
    },
    "55": {
        "diagram": {"groups": [
            {"label": "पित्तजे … पिबेत्", "items": ["काकोली-द्वय, विदारी-मूल: क्वाथ", "उत्पल, पद्मक: क्वाथ",
                                              "मधुक-पुष्प, काश्मर्य-फल: क्वाथ"]},
            {"label": "साथ (किसके, अनिश्चित)", "items": ["वास", "शर्करा"]}]},
        "chunks": "पित्तजे | काकोलीद्वयविदारीमूलक्वाथम् | उत्पलपद्मकक्वाथं | मधुकपुष्पकाश्मर्यफलक्वाथं | वासशर्करं पिबेत्।",
        "sandhi": "म् + स्वर: क्वाथम् + उत्पल → क्वाथमुत्पल · म् + व्यंजन: क्वाथम् + मधुक → क्वाथं मधुक।",
        "letters": "तीन क्वाथ: का-उ-म (काकोली, उत्पल, मधुक), हर क्वाथ का पहला अक्षर (मेरी याद-पद्धति)।",
    },
    "56": {
        "frame": "वा (अथवा, इकाई ५५ के बाद) → श्वेतचन्दन-क्वाथ → सक्षौद्र (शहद सहित); क्रिया नहीं कही।",
        "sandhi": "म् + व → ं व: क्वाथम् + वा → क्वाथं वा · स + क्षौद्रम् → सक्षौद्रम् (बहुव्रीहि)।",
        "puns": "केवल सुनने की सहायता: ‘स-क्षौद्र’ में ‘स’ = साथ: शहद साथ।",
    },
    "57": {
        "frame": "वा (अथवा) → धव + धातकी → कल्क; न क्रिया, न भाग।",
        "anchors": "धातकी = धाय (मानक); धव = धौ (सम्भावित)।",
        "sandhi": "म् + व → ं व: कल्कम् + वा → कल्कं वा।",
    },
    "58": {
        "chunks": "घृतेन वा | मधुक | मधुरसा | मृद्वीका | कल्कं।",
        "frame": "घृतेन (घी के साथ) → मधुक, मधुरसा, मृद्वीका का कल्क; क्रिया नहीं।",
        "letters": "म-म-म: मधुक, मधुरसा, मृद्वीका, तीनों ‘म’ से (मेरी याद-पद्धति)।",
    },
    "59": {
        "frame": "नाम-वाक्य: शम्याक-गवाक्षी-क्षीरम् (कर्ता) = विरेकः (विरेचन)।",
        "contrast": "सूची-पाठ: शम्याक, गवाक्षी और क्षीर ↔ दूसरा पाठ: शम्याक और गवाक्षी का क्षीर (दोनों खुले)।",
        "sandhi": "म् + व → ं व: क्षीरम् + विरेकः → क्षीरं विरेकः।",
    },
    "60": {
        "chunks": "चंदनपयस्याकल्कं | योनौ | धारयेत्।",
        "contrast": "इकाई ५६: श्वेतचन्दन (रंग कहा) ↔ इकाई ६०: चन्दन (रंग नहीं कहा)।",
        "sandhi": "म् + य → ं य: कल्कम् + योनौ → कल्कं योनौ।",
    },
    "61": {
        "sandhi": "अ + अ → आ: गैरिक + अरिष्ट → गैरिकारिष्ट · अः + प: कषायः + प्रक्षालनम् (विसर्ग बना रहता है)।",
        "frame": "नाम-वाक्य: गैरिक-अरिष्ट-कषायः = प्रक्षालनम्।",
        "anchors": "गैरिक = लाल गेरू (खनिज, मानक); अरिष्ट = सम्भवतः नीम (विवादित)।",
    },
    "62": {
        "diagram": {"groups": [
            {"label": "श्लैष्मिके … क्वाथं पिबेत्", "items": ["कुटज", "कटुका", "अश्वगन्धा"]},
            {"label": "समाक्षिकं वा (पंक्ति क्षतिग्रस्त)", "items": ["अस्पष्ट पद: क्षीरिवृक्ष-…"]}]},
        "sandhi": "आ + अ → आ: कटुका + अश्वगन्धा → कटुकाश्वगन्धा (छपा ऽ केवल आदत) · म् + प → ं प: क्वाथम् + पिबेत् → क्वाथं पिबेत्।",
        "letters": "क-क-अ: कुटज, कटुका, अश्वगन्धा (मेरी याद-पद्धति)।",
        "frame": "यहाँ से कफज (श्लैष्मिक) क्रम आरम्भ; दूसरी पंक्ति पर कुछ नहीं टिकाया।",
    },
    "63": {
        "frame": "एतेषाम् एव (इन्हीं, पिछली कफज औषधियों) का चूर्ण → मधु + घृत के साथ → चाटे।",
        "sandhi": "म् + स्वर: एतेषाम् + एव → एतेषामेव · म् + ल → ं ल: मधुघृताभ्याम् + लिह्यात् → मधुघृताभ्यां लिह्यात्।",
        "chunks": "एतेषामेव वा | चूर्ण | मधुघृताभ्यां | लिह्यात्।",
    },
    "64": {
        "contrast": "पित्त-क्रम का शोधन: विरेक (इकाई ५९) ↔ कफ-क्रम का शोधन: वमन (इकाई ६४)।",
        "frame": "मदनफल-कषायेण (काढ़े से) → वमनम्; क्रिया नहीं।",
        "anchors": "मदनफल = मैनफल, Randia dumetorum (मानक, इकाई ५०)।",
    },
    "65": {
        "diagram": {"groups": [
            {"label": "तत् = मदनफल (इकाई ६४, सीधा अर्थ)", "items": ["तत्कल्कम्", "एव", "च", "योनौ धारयेत्"]}]},
        "sandhi": "त् + क: तत् + कल्कम् → तत्कल्कम् · म् + स्वर: तत्कल्कम् + एव → तत्कल्कमेव।",
        "pegs": "मेरा बनाया चित्र: एक मैनफल, दो रास्ते: एक ओर काढ़े का प्याला (वमन), दूसरी ओर लेप की कटोरी (धारण)। (केवल याद के लिए)",
    },
    "66": {
        "contrast": {"groups": [
            {"label": "वातज (क्रम से, इकाई ५४)", "items": ["कल्क: प्रियंगु, तिल", "प्रक्षालन: सरल, मुद्गपर्णी"]},
            {"label": "पित्तज (क्रम से, इकाई ६०-६१)", "items": ["कल्क: चन्दन, पयस्या", "प्रक्षालन: गैरिक, अरिष्ट"]},
            {"label": "कफज (क्रम से, इकाई ६५-६६)", "items": ["कल्क: मदनफल", "प्रक्षालन: अस्पष्ट काढ़ा, या बस्त-मेष मूत्र"]}]},
        "sandhi": "अः + प: कषायः + प्रक्षालनम् · म् + ब → ं ब: प्रक्षालनम् + बस्त → प्रक्षालनं बस्त · म् + व: मूत्रम् + वा → मूत्रं वा।",
        "frame": "पक्का भाग: प्रक्षालनम् … बस्तमेषमूत्रं वा; पहला समास क्षतिग्रस्त।",
    },
}

# ===================================================================== IMAGE_SPECS
IMAGE_SPECS = {
    ("54", "diagram"): {
        "file": "sh1-dharana-prakshalana-54.svg",
        "alt": ("Split of unit 54: held in the yoni, a paste of priyangu and tila; the wash, a decoction of sarala and "
                "mudgaparni."),
        "type": "split",
        "title": "इकाई ५४: धारण और प्रक्षालन",
        "cols": [["योनि में धारण (कल्क)", ["प्रियंगु", "तिल"]],
                 ["प्रक्षालन (कषाय)", ["सरल", "मुद्गपर्णी"]]],
    },
    ("55", "diagram"): {
        "file": "sh1-pitta-kvatha-55.svg",
        "alt": ("Table of unit 55: in the Pitta-type one drinks three decoctions (kakoli pair and vidari root; utpala and "
                "padmaka; madhuka flower and kashmarya fruit), with vasa and sugar, whose reach is undecided."),
        "type": "table",
        "title": "पित्तज: पिए (इकाई ५५)",
        "heads": ["क्वाथ", "द्रव्य"],
        "rows": [["पहला", "काकोली-द्वय, विदारी-मूल"],
                 ["दूसरा", "उत्पल, पद्मक"],
                 ["तीसरा", "मधुक-पुष्प, काश्मर्य-फल"],
                 ["साथ (किसके, अनिश्चित)", "वास, शर्करा"]],
    },
    ("62", "diagram"): {
        "file": "sh1-kapha-kvatha-62.svg",
        "alt": ("Mindmap of unit 62: in the Kapha-type one drinks a decoction of kutaja, katuka and ashvagandha; "
                "the second line, with honey, is damaged and unclear."),
        "type": "mermaid",
        "code": ("mindmap\n"
                 "  श्लैष्मिक: क्वाथ पिए\n"
                 "    कुटज\n"
                 "    कटुका\n"
                 "    अश्वगन्धा\n"
                 "    अथवा मधु सहित\n"
                 "      पद क्षतिग्रस्त\n"),
    },
    ("64", "contrast"): {
        "file": "sh1-vireka-vamana-64.svg",
        "alt": ("Split comparing the cleansing named in the two lists: purgation (vireka) with shamyaka, gavakshi and milk "
                "in the Pitta-type list (unit 59), and emesis (vamana) with a decoction of madanaphala in the Kapha-type "
                "list (unit 64)."),
        "type": "split",
        "title": "शोधन: पित्त-क्रम और कफ-क्रम",
        "cols": [["विरेक (इकाई ५९)", ["शम्याक", "गवाक्षी", "क्षीर"]],
                 ["वमन (इकाई ६४)", ["मदनफल-कषाय"]]],
    },
    ("65", "diagram"): {
        "file": "sh1-madanaphala-65.svg",
        "alt": ("Flowchart of units 64 and 65: madanaphala as a decoction gives emesis (unit 64); its paste is held in the "
                "yoni (unit 65), on the plain reading of tat."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"मदनफल\"] --> B[\"कषाय से वमन<br/>(इकाई ६४)\"]\n"
                 "  A --> C[\"उसी का कल्क<br/>(इकाई ६५)\"]\n"
                 "  C --> D[\"योनि में धारण\"]\n"),
    },
    ("66", "contrast"): {
        "file": "sh1-yoni-upaya-66.svg",
        "alt": ("Table of the local measures in the three doṣa lists by their place in the text: Vata (unit 54) paste of "
                "priyangu and tila, wash of sarala and mudgaparni; Pitta (units 60-61) paste of candana and payasya, wash of "
                "gairika and arishta; Kapha (units 65-66) paste of madanaphala, wash of an unclear decoction or goat and "
                "sheep urine."),
        "type": "table",
        "title": "योनि-उपाय, दोष-क्रम से",
        "heads": ["क्रम (इकाई)", "कल्क · प्रक्षालन"],
        "rows": [["वातज (५४)", "प्रियंगु-तिल · सरल-मुद्गपर्णी"],
                 ["पित्तज (६०-६१)", "चन्दन-पयस्या · गैरिक-अरिष्ट"],
                 ["कफज (६५-६६)", "मदनफल · अस्पष्ट काढ़ा या मूत्र"]],
    },
}
