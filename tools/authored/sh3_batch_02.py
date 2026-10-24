from helpers import mcq, match, order, fill, multi, accepts


def T(q, teaches):
    q["teaches"] = teaches
    return q


AUTHORED = {}

# ---------------------------------------------------------------- unit 14
AUTHORED["14"] = {
    "title": "गर्भोत्पीडनात्तु दोषा हृदयं प्राप्य विदहंति",
    "question": "By unit 14, what makes the doṣas burn, and what arises then?",
    "rule": ("But (तु) from the pressure of the embryo (गर्भोत्पीडन) the doṣas reach the heart (हृदय) and burn (विदहन्ति); "
             "then (ततः) itching (कण्डू) arises."),
    "limits": ("Low confidence. The last word कंडूकिकिसं is unclear: kaṇḍū + kikisa (probably stretch marks; probable), "
               "compound type unclear, no verb after it; no question rests on it. The line does not name its speaker."),
    "explain_hi": ("यह गद्य-पंक्ति जलन का कारण देती है: गर्भ के दबाव (उत्पीडन) से दोष हृदय तक पहुँचकर जलाते हैं। "
                   "‘तु’ (तो, परन्तु) पिछली इकाई में स्त्रियों के मत (केशों से जलन) के बाद आता है; यह पंक्ति वक्ता का नाम नहीं लेती। "
                   "‘ततः’ (तब) के बाद खुजली (कण्डू) उत्पन्न होती है। "
                   "अन्तिम शब्द ‘कंडूकिकिसं’ अस्पष्ट है: किकिस सम्भवतः गर्भावस्था की त्वचा की खिंचाव-धारियाँ (सम्भावित पहचान), "
                   "समास का प्रकार अस्पष्ट; इस पर कोई प्रश्न नहीं। "
                   "‘प्राप्य’ (पहुँचकर) में उपसर्ग ‘प्र’ है, इसलिए ‘-य’ लगा है, ‘-त्वा’ नहीं।"),
    "hook": "गर्भ दबाए → दोष हृदय तक → जलन → तब खुजली।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 14, from what do the doṣas reach the heart and burn?",
            ("From the pressure of the embryo", "गर्भोत्पीडनात्: from the pressure of the embryo."),
            [("From the arising of the embryo's hair", "That is the women's view in card 13, which Ātreya rejects."),
             ("From eating too much salty food", "No food is named in unit 14."),
             ("From scratching the skin of the belly", "Scratching is named in card 20, not as a cause here.")],
            "The cause given is the pressure of the embryo.",
            "गर्भोत्पीडनात् → दोषा हृदयं प्राप्य विदहन्ति."),
        order(1, "Put the steps of unit 14 in the line's order.",
              ["गर्भोत्पीडनात्", "दोषा हृदयं प्राप्य", "विदहन्ति", "ततः", "कण्डूर्जायते"],
              "Pressure of the embryo, the doṣas reach the heart, they burn, then itching arises.",
              "उत्पीडन → हृदय तक दोष → दाह → ततः कण्डू."),
        match(2, "Match each word of unit 14 to its meaning.",
              [["उत्पीडन", "pressure"], ["दोषाः", "the doṣas"], ["हृदयम्", "the heart"],
               ["विदहन्ति", "they burn"], ["कण्डूः", "itching"]],
              "These words carry the cause, the place, the action and the result.",
              "उत्पीडन, दोषाः, हृदयम्, विदहन्ति, कण्डूः.", role="extend",
              teaches="ततः = then: it links the burning to the itching that follows."),
        mcq("discriminate", 3, "Why does प्राप्य (having reached) end in -य and not in -त्वा?",
            ("Its verb has a prefix (प्र-), and with a prefix the absolutive takes -य",
             "The data: absolutive of प्र + √आप्; a prefixed verb takes -य."),
            [("The ending -य marks a plural subject, the doṣas", "-य does not mark number; the absolutive has no person or number."),
             ("The ending -य makes it a command: let them reach", "A command would be an imperative; प्राप्य is an absolutive."),
             ("The ending -य shows a future: they will reach", "No future ending is here; the data gives absolutive.")],
            "प्र + √आप् + य = प्राप्य, having reached.",
            "Absolutive: -त्वा without a prefix, -य with a prefix."),
        multi("apply", 4, "Which statements does unit 14 make?",
              [("The embryo's hair causes the burning", "That is the women's view of card 13, not this line."),
               ("The doṣas reach the heart and burn", "Right: दोषा हृदयं प्राप्य विदहन्ति."),
               ("After that, itching arises", "Right: ततः कण्डूर्जायते."),
               ("A medicine for the burning is named", "No medicine is named in unit 14; the treatment starts in card 15.")],
              [1, 2],
              "Pressure → doṣas reach the heart and burn → then itching.",
              "दोषा ... विदहन्ति; ततः कण्डूर्जायते."),
        mcq("transfer", 5, "By the rule of कण्डूर्जायते, how is वधूः + गच्छति (the bride goes) written when joined?",
            ("वधूर्गच्छति", "A visarga after ऊ becomes र् before a voiced sound, as कण्डूः + जायते."),
            [("वधूगच्छति", "The visarga after ऊ is not simply dropped."),
             ("वधूस्गच्छति", "स् comes only before त or थ, not before ग."),
             ("वधुर्गच्छति", "The long ऊ is not shortened.")],
            "वधूः + गच्छति = वधूर्गच्छति, like कण्डूः + जायते = कण्डूर्जायते.",
            "ऊः + voiced sound → ऊर्.",
            teaches="A visarga after a vowel other than अ/आ becomes र् before a voiced sound: कण्डूः + जायते → कण्डूर्जायते."),
    ],
}

# ---------------------------------------------------------------- unit 15
AUTHORED["15"] = {
    "title": "नवनीतस्य मधुरौषधसिद्धस्य पाणितलमात्रमस्यै दद्यात्",
    "question": "By unit 15, what should be given to her, how much, and cooked with what?",
    "rule": ("In that case (तत्र) one should give her (अस्यै) a palm's measure (पाणितलमात्र) of fresh butter (नवनीत) cooked "
             "with sweet medicines (मधुरौषधसिद्ध)."),
    "limits": ("Medium confidence. The printed कोलोडकेन is read as कोलोदकेन, with kola water (kola probably jujube) on a "
               "possible correction of ड to द; if कोलोडक were a word it is unknown. No question rests on it. The line does not "
               "name the sweet medicines. A prose line."),
    "explain_hi": ("उस अवस्था में (तत्र) इस स्त्री को (अस्यै) मधुर औषधों से पकाया हुआ नवनीत (ताज़ा मक्खन) हथेली भर दे। "
                   "‘पाणितलमात्रम्’ = हथेली के माप भर; ‘नवनीतस्य’ षष्ठी है: मक्खन का (उतना भाग)। "
                   "छपा ‘कोलोडकेन’ सम्भवतः ‘कोलोदकेन’ (कोल यानी सम्भवतः बेर का जल) है; यह सुधार अनुमानित है, इस पर प्रश्न नहीं। "
                   "कौन-से मधुर औषध, यह पंक्ति नहीं बताती। "
                   "‘मधुरौषध’ में मधुर + औषध है (अ + औ → औ)।"),
    "hook": "हथेली भर मक्खन, मधुर औषध से पका, उसी को।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 15, what should be given to her?",
            ("Fresh butter cooked with sweet medicines", "नवनीतस्य मधुरौषधसिद्धस्य."),
            [("Milk gruel containing ghee", "That is the eighth-month drink of card 23."),
             ("A paste of sandalwood and lotus stalk", "That paste is for rubbing, in card 16."),
             ("Water cooked with mālatī and madhuka", "That water is for pouring, in card 19.")],
            "Fresh butter (navanīta) cooked with sweet medicines.",
            "नवनीत, मधुरौषधसिद्ध."),
        order(1, "Put these words of unit 15 in the line's order.",
              ["तत्र", "नवनीतस्य", "मधुरौषधसिद्धस्य", "पाणितलमात्रम्", "अस्यै", "दद्यात्"],
              "In that case, of fresh butter, cooked with sweet medicines, a palm's measure, to her, one should give.",
              "तत्र → नवनीतस्य → मधुरौषधसिद्धस्य → पाणितलमात्रम् → अस्यै → दद्यात्."),
        match(2, "Match each word of unit 15 to its meaning.",
              [["नवनीत", "fresh butter"], ["मधुर", "sweet"], ["औषध", "medicines"], ["सिद्ध", "cooked"],
               ["पाणितल", "palm of the hand"], ["मात्र", "measure"]],
              "Six members give what, cooked how, and how much.",
              "नवनीत, मधुर, औषध, सिद्ध, पाणितल, मात्र.", role="extend",
              teaches="-मात्र at the end = the measure of: पाणितलमात्रम् = as much as a palm holds."),
        mcq("discriminate", 3, "Which split of मधुरौषध is right?",
            ("मधुर + औषध", "अ + औ → औ: मधुर + औषध = मधुरौषध."),
            [("मधुरः + औषध", "A compound member has no visarga; अः before औ would give मधुर औषध."),
             ("मधुरम् + औषध", "A final म् would stay: मधुरमौषध."),
             ("मधुरो + षध", "षध is not a word; the word is औषध (medicine).")],
            "मधुर (sweet) + औषध (medicine): अ + औ → औ.",
            "अ + औ → औ."),
        mcq("apply", 4, "By unit 15, to whom is the butter given (अस्यै)?",
            ("To her, the pregnant woman", "अस्यै = to her (f. dative); the data: the pregnant woman."),
            [("To the embryo directly", "अस्यै is feminine; the embryo (गर्भ) is masculine."),
             ("To the physician", "The physician is the one who gives; अस्यै is feminine."),
             ("To the women who speak in card 13", "अस्यै is singular: one woman.")],
            "अस्यै: dative feminine singular, to her.",
            "अस्यै दद्यात् = one should give to her."),
        mcq("transfer", 5, "By the dative अस्यै, what does बालिकायै फलं दद्यात् mean?",
            ("One should give a fruit to the girl", "-ऐ (-यै) is the feminine dative: to the girl."),
            [("One should take a fruit from the girl", "From would be ablative बालिकायाः."),
             ("One should give the girl's fruit", "Of would be genitive बालिकायाः."),
             ("The girl should give a fruit", "The girl would then be nominative बालिका.")],
            "बालिकायै = to the girl, as अस्यै = to her.",
            "Feminine dative -ऐ/-यै = to.",
            teaches="The feminine dative in -ऐ marks the receiver: अस्यै दद्यात् = one should give to her."),
    ],
}

# ---------------------------------------------------------------- unit 16
AUTHORED["16"] = {
    "title": "चंदनमृणालकल्कैश्च स्तनोदरं",
    "question": "By unit 16, which pastes and which powders are used on the breast and belly?",
    "rule": ("Pastes (कल्क) of sandalwood (चन्दन) and lotus stalk (मृणाल) on the breast and belly (स्तनोदर); or (वा) "
             "powders (चूर्ण) of śirīṣa, (dhātakī,) mustard (सर्षप) and madhuka. कल्क = paste, चूर्ण = powder."),
    "limits": ("Two printed lines; the second has no verb of its own. मृद्गीयात् is read मृद्नीयात् (should rub), a possible "
               "correction. घातुकी read as धातकी is conjectural: no question on it. madhuka: probably licorice (or mahua). "
               "Who rubs is understood."),
    "explain_hi": ("पहली पंक्ति: चन्दन (Santalum album, मानक) और मृणाल (कमलनाल, मानक) के कल्कों (लेप) से स्तन और पेट को मले। "
                   "छपा ‘मृद्गीयात्’ कोई रूप नहीं; ‘मृद्नीयात्’ (मले) सम्भावित सुधार है। "
                   "दूसरी पंक्ति, ‘वा’ (अथवा): शिरीष (Albizia lebbeck, मानक), अनुमानित पाठ पर धातकी, सर्षप (सरसों, मानक) और "
                   "मधुक (सम्भवतः मुलेठी) के चूर्णों से; क्रिया पहली पंक्ति से आती है। "
                   "भेद: पहले समूह में कल्क (गीला लेप), दूसरे में चूर्ण (सूखा पिसा)। "
                   "‘स्तनोदरम्’ एकवचन द्वन्द्व है: स्तन और उदर।"),
    "hook": "चन्दन-मृणाल का लेप, या शिरीष-सरसों-मधुक का चूर्ण: स्तन-पेट पर।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 16, which parts of the body are named for the pastes?",
            ("The breast and belly (स्तनोदरम्)", "स्तनोदरम् = breast and belly, a singular dvandva."),
            [("The head and feet", "No head or feet are named."),
             ("The back and the loins", "No back or loins are named."),
             ("The palms of the hands", "The palm is a measure in card 15, not here.")],
            "स्तन (breast) + उदर (belly).",
            "स्तनोदरम् = breast and belly."),
        order(1, "Put these words of unit 16 in the text's order.",
              ["चन्दन", "मृणाल", "स्तनोदरम्", "शिरीष", "सर्षप", "मधुक"],
              "Sandalwood, lotus stalk, breast and belly; then śirīṣa, mustard, madhuka.",
              "चन्दन → मृणाल → स्तनोदरम् → शिरीष → सर्षप → मधुक."),
        match(2, "Match each plant name of unit 16 to its meaning, as the data labels it.",
              [["चन्दन", "sandalwood (standard)"], ["मृणाल", "lotus stalk (standard)"],
               ["शिरीष", "Albizia lebbeck (standard)"], ["सर्षप", "mustard (standard)"],
               ["मधुक", "probably licorice (probable)"]],
              "Four standard identifications and one probable one.",
              "चन्दन, मृणाल, शिरीष, सर्षप: standard; मधुक: probable.", role="extend",
              teaches="An identification keeps its label: मधुक is only probably licorice."),
        mcq("discriminate", 3, "By unit 16, in what form is each group used?",
            ("First group as pastes (कल्क), second as powders (चूर्ण)", "कल्कैः for candana and mṛṇāla; चूर्णैः for the second group."),
            [("Both groups as pastes (कल्क)", "The second group ends in चूर्णैः, powders."),
             ("First group as powders, second as pastes", "It is the other way round."),
             ("Both groups cooked in oil (तैल)", "No oil is named in unit 16.")],
            "कल्क = paste; चूर्ण = powder.",
            "चन्दनमृणालकल्कैः ... चूर्णैर्वा."),
        multi("apply", 4, "Which plants does unit 16 name in the powder group?",
              [("चन्दन (sandalwood)", "Sandalwood is in the paste group."),
               ("शिरीष (Albizia lebbeck)", "Right: शिरीष opens the powder group."),
               ("मृणाल (lotus stalk)", "Lotus stalk is in the paste group."),
               ("सर्षप (mustard)", "Right: सर्षप is in the powder group.")],
              [1, 3],
              "Powders: śirīṣa, (dhātakī, conjectural), mustard, madhuka.",
              "शिरीष...सर्षपमधुकचूर्णैर्वा."),
        mcq("transfer", 5, "By the rule of कल्कैश्च, how is रामः + च (and Rāma) written when joined?",
            ("रामश्च", "A visarga before च becomes श्, as कल्कैः + च → कल्कैश्च."),
            [("रामच", "The visarga is not simply dropped before च."),
             ("रामो च", "अः → ओ only before a voiced sound; च is unvoiced."),
             ("रामर्च", "र् comes after vowels other than अ/आ, before a voiced sound.")],
            "रामः + च = रामश्च, like कल्कैः + च = कल्कैश्च.",
            "Visarga + च → श्च.",
            teaches="A visarga before च/छ becomes श्: कल्कैः + च → कल्कैश्च."),
    ],
}

# ---------------------------------------------------------------- unit 17
AUTHORED["17"] = {
    "title": "कुटजार्जकबीजमुस्ताहरिद्राकल्कैर्वा",
    "question": "By unit 17, which two further sets of pastes are offered?",
    "rule": ("Or (वा) pastes of kuṭaja and arjaka seeds, mustā and haridrā; or (वा) pastes of nimba, kola, surasā and "
             "mañjiṣṭhā. Each वा gives one alternative set."),
    "limits": ("No verb: the verb is carried from card 16 (the rubbing). That बीज (seed) goes with both kuṭaja and arjaka is "
               "the data's reading. arjaka (a basil), kola (jujube) and surasā (holy basil) are probable only; surasa is read "
               "as surasā. No question rests on these three identities."),
    "explain_hi": ("यह गद्य-पंक्ति कार्ड 16 के उपचार के दो और विकल्प देती है; क्रिया वहीं से आती है। "
                   "पहला समूह: कुटज (कुड़ा) और अर्जक (सम्भवतः एक तुलसी) के बीज, मुस्ता (नागरमोथा), हरिद्रा (हल्दी) के कल्क। "
                   "दूसरा समूह: निम्ब (नीम), कोल (सम्भवतः बेर), सुरसा (सम्भवतः तुलसी), मञ्जिष्ठा (मजीठ) के कल्क। "
                   "दोनों ‘वा’ (अथवा) से अलग विकल्प बनते हैं। "
                   "‘कुटजार्जक’ में कुटज + अर्जक है (अ + अ → आ)।"),
    "hook": "कुटज-अर्जक-मुस्ता-हल्दी, या नीम-कोल-सुरसा-मजीठ: दोनों लेप।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 17, in what form are these medicines used?",
            ("As pastes (कल्क)", "Both sets end in कल्कैः, with pastes."),
            [("As powders (चूर्ण)", "Powders are the second group of card 16."),
             ("Cooked in oil (तैल)", "Oil comes in card 18."),
             ("As a water to pour", "Pouring with water is card 19.")],
            "Both sets are pastes.",
            "...कल्कैर्वा ... कल्कैर्वा."),
        order(1, "Put these plant names of unit 17 in the text's order.",
              ["कुटज", "अर्जक", "मुस्ता", "हरिद्रा", "निम्ब", "मञ्जिष्ठा"],
              "First set: kuṭaja, arjaka, mustā, haridrā; second: nimba ... mañjiṣṭhā.",
              "कुटज → अर्जक → मुस्ता → हरिद्रा → निम्ब → मञ्जिष्ठा."),
        match(2, "Match each plant of unit 17 to its identification (all standard in the data).",
              [["कुटज", "Holarrhena antidysenterica"], ["मुस्ता", "nut grass, Cyperus rotundus"],
               ["हरिद्रा", "turmeric"], ["निम्ब", "neem"], ["मञ्जिष्ठा", "Indian madder, Rubia cordifolia"]],
              "These five carry standard identifications in the data.",
              "कुटज, मुस्ता, हरिद्रा, निम्ब, मञ्जिष्ठा.", role="extend",
              teaches="Only these five are standard here; arjaka, kola and surasā are probable only."),
        mcq("discriminate", 3, "What do the two वा of unit 17 tell?",
            ("Each set is an alternative (or ... or)", "वा = or: each set is one more option."),
            [("Both sets are mixed into one paste", "वा does not mean and; no mixing is said."),
             ("The sets are used one after the other", "No order of use is given; वा marks options."),
             ("वा names a further plant", "वा is an indeclinable, or.")],
            "वा ... वा = or ... or.",
            "वा = or."),
        mcq("apply", 4, "By unit 17, which set contains haridrā (turmeric)?",
            ("The set with kuṭaja, arjaka seeds and mustā", "कुटजार्जकबीजमुस्ताहरिद्राकल्कैः."),
            [("The set with nimba and mañjiṣṭhā", "That set has nimba, kola, surasā, mañjiṣṭhā."),
             ("The set with sandalwood and lotus stalk", "That is card 16."),
             ("A set of its own", "हरिद्रा is inside the first compound.")],
            "Haridrā closes the first set.",
            "कुटज-अर्जकबीज-मुस्ता-हरिद्रा."),
        mcq("transfer", 5, "By the rule of कुटजार्जक, how is देव + अर्चनम् (worship of the god) joined?",
            ("देवार्चनम्", "अ + अ → आ, as कुटज + अर्जक → कुटजार्जक."),
            [("देवेर्चनम्", "ए comes from अ + इ, not अ + अ."),
             ("देवौर्चनम्", "औ comes from अ + औ, not अ + अ."),
             ("देवोऽर्चनम्", "ओऽ comes from अः + अ; देव has no visarga.")],
            "देव + अर्चनम् = देवार्चनम्.",
            "अ + अ → आ.",
            teaches="Two short अ join as आ: कुटज + अर्जक → कुटजार्जक."),
    ],
}

# ---------------------------------------------------------------- unit 18
AUTHORED["18"] = {
    "title": "शशहरिणपुनर्नवा... तैलेनाभ्यंगः",
    "question": "By unit 18, with which three things is the oil massage (abhyaṅga) done?",
    "rule": ("Abhyaṅga (oil massage) with (1) water cooked with hare, deer, punarnavā, mālatī, madhuka; (2) triphalā mixed "
             "with spotted-deer blood; (3) oil cooked with karavīra-leaf paste."),
    "limits": ("Which parts of hare and deer are used is not stated. How the three instruments combine is not stated. "
               "mālatī is disputed (possibly a jasmine); madhuka probable (licorice); the oil's kind is not named. The printed "
               "सिद्धैनांभसा is likely a misprint for सिद्धेनाम्भसा: no question on it."),
    "explain_hi": ("एक ही अभ्यंग (तेल-मालिश) के तीन साधन तृतीया में आते हैं: "
                   "(1) शश (खरगोश), हरिण (हिरन), पुनर्नवा, मालती (पहचान विवादित) और मधुक (सम्भवतः मुलेठी) से पकाया जल; "
                   "(2) पृषत (चित्तीदार हिरन) के रुधिर से युक्त त्रिफला (हरड़, बहेड़ा, आँवला); "
                   "(3) करवीर (कनेर) के पत्तों के कल्क से पकाया तेल। "
                   "खरगोश-हिरन का कौन-सा भाग, और तीनों कैसे मिलते हैं, यह नहीं कहा गया।"),
    "hook": "जल, त्रिफला, कनेर-तेल: तीन साधन, एक अभ्यंग।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 18, which procedure ends the line?",
            ("Abhyaṅga, oil massage (अभ्यङ्गः)", "तैलेनाभ्यङ्गः: oil massage with oil."),
            [("Pariṣeka, pouring", "Pouring is card 19."),
             ("Āsthāpana, a decoction enema", "That is card 26."),
             ("Avoiding scratching", "That is card 20.")],
            "The line names abhyaṅga.",
            "...तैलेनाभ्यङ्गः."),
        order(1, "Put these names of unit 18 in the text's order.",
              ["शश", "हरिण", "पुनर्नवा", "पृषतरुधिर", "त्रिफला", "करवीरपत्र"],
              "Hare, deer, punarnavā (in the water); spotted-deer blood, triphalā; karavīra leaves (in the oil).",
              "शश → हरिण → पुनर्नवा → पृषतरुधिर → त्रिफला → करवीरपत्र."),
        match(2, "Match each word of unit 18 to its meaning.",
              [["शश", "hare"], ["हरिण", "deer"], ["पृषत", "spotted deer"],
               ["पुनर्नवा", "Boerhavia diffusa (standard)"], ["करवीर", "oleander, Nerium oleander (standard)"]],
              "Three animals and two plants of the line.",
              "शश, हरिण, पृषत, पुनर्नवा, करवीर.", role="extend",
              teaches="त्रिफला = the three fruits (harītakī, bibhītaka, āmalakī), standard."),
        mcq("discriminate", 3, "By unit 18, what is mixed with the blood of the spotted deer?",
            ("Triphalā", "पृषतरुधिरयुक्तया त्रिफलया: triphalā mixed with spotted-deer blood."),
            [("The oil", "The oil is cooked with karavīra-leaf paste."),
             ("The water", "The water is cooked with hare, deer and plants."),
             ("The karavīra leaves", "The leaves are a paste for cooking the oil.")],
            "पृषतरुधिरयुक्ता goes with त्रिफला (both f. inst. sg.).",
            "पृषतरुधिरयुक्तया त्रिफलया."),
        multi("apply", 4, "Which statements fit unit 18?",
              [("The oil is cooked with a paste of karavīra leaves", "Right: करवीरपत्रकल्कसिद्धेन तैलेन."),
               ("The parts of hare and deer used are stated", "The data: the parts are not stated."),
               ("The line says how the three are combined", "The data: how they combine is not stated."),
               ("Triphalā is mixed with spotted-deer blood", "Right: पृषतरुधिरयुक्तया त्रिफलया.")],
              [0, 3],
              "Oil with karavīra paste; triphalā with spotted-deer blood; parts and combining are left open.",
              "तैलेन ... त्रिफलया ... अभ्यङ्गः."),
        mcq("transfer", 5, "By the rule of तैलेनाभ्यङ्गः, how is जलेन + अभिषेकः (sprinkling with water) joined?",
            ("जलेनाभिषेकः", "अ + अ → आ, as तैलेन + अभ्यङ्गः."),
            [("जलेनेभिषेकः", "अ + अ does not give ए."),
             ("जलेनोऽभिषेकः", "ओऽ comes from अः + अ; जलेन has no visarga."),
             ("जलेनभिषेकः", "The second अ is not simply lost.")],
            "जलेन + अभिषेकः = जलेनाभिषेकः.",
            "अ + अ → आ.",
            teaches="A final अ and an initial अ join as आ: तैलेन + अभ्यङ्गः → तैलेनाभ्यङ्गः."),
    ],
}

# ---------------------------------------------------------------- unit 19
AUTHORED["19"] = {
    "title": "परिषेकः पुनर्मालतीमधुकसिद्धेनांभसा",
    "question": "By unit 19, what is the pouring (pariṣeka) done with?",
    "rule": ("Pouring (परिषेक) with water (अम्भस्) cooked (सिद्ध) with mālatī and madhuka. सिद्ध at the end of a compound = "
             "cooked with."),
    "limits": ("No verb (elliptical). पुनः is taken as again; it could also mean and further: no question on it. mālatī is "
               "disputed (possibly a jasmine); madhuka is probable (licorice). The line does not say on which part of the body."),
    "explain_hi": ("फिर (पुनः) मालती और मधुक से पकाए जल से परिषेक, यानी शरीर पर धारा से डालना। "
                   "मालती की पहचान विवादित है (सम्भवतः चमेली की एक जाति), मधुक सम्भवतः मुलेठी। "
                   "‘पुनः’ का अर्थ ‘फिर’ लिया गया है, ‘और आगे’ भी हो सकता है; इस पर प्रश्न नहीं। "
                   "पंक्ति में क्रिया नहीं है। "
                   "‘सिद्धेनाम्भसा’ में सिद्धेन + अम्भसा है (अ + अ → आ)।"),
    "hook": "मालती-मधुक का जल: ऊपर से धारा।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 19, what does परिषेक mean?",
            ("Pouring, affusion", "परिषेकः = pouring, affusion."),
            [("Oil massage", "Oil massage (अभ्यङ्ग) is card 18."),
             ("Rubbing with powders", "That is उद्वर्तन, card 21."),
             ("A decoction enema", "That is आस्थापन, card 26.")],
            "परिषेक = pouring.",
            "परिषेकः = pouring."),
        order(1, "Put the words of unit 19 in the line's order.",
              ["परिषेकः", "पुनः", "मालती", "मधुक", "सिद्धेन", "अम्भसा"],
              "Pouring, again, mālatī, madhuka, cooked with, with water.",
              "परिषेकः → पुनः → मालती → मधुक → सिद्धेन → अम्भसा."),
        match(2, "Match each word of unit 19 to its meaning.",
              [["परिषेक", "pouring"], ["मालती", "mālatī (identity disputed)"], ["मधुक", "probably licorice"],
               ["सिद्ध", "cooked"], ["अम्भस्", "water"]],
              "What is done, with what, cooked with what.",
              "परिषेक, मालती, मधुक, सिद्ध, अम्भस्.", role="extend",
              teaches="X-सिद्ध = cooked with X: मालतीमधुकसिद्ध = cooked with mālatī and madhuka."),
        mcq("discriminate", 3, "Which split of सिद्धेनांभसा (सिद्धेनाम्भसा) is right?",
            ("सिद्धेन + अम्भसा", "अ + अ → आ: सिद्धेन + अम्भसा."),
            [("सिद्धेने + अम्भसा", "ए + अ would give सिद्धेनेऽम्भसा."),
             ("सिद्धेनम् + अम्भसा", "A final म् would give सिद्धेनमम्भसा."),
             ("सिद्धेन + भसा", "भसा is not the word; with no अ there would be no आ.")],
            "सिद्धेन (cooked with) + अम्भसा (with water).",
            "अ + अ → आ."),
        mcq("apply", 4, "By unit 19, with what is the water cooked?",
            ("Mālatī and madhuka", "मालतीमधुकसिद्धेन."),
            [("Hare and deer", "Hare and deer are in the water of card 18, not here."),
             ("Karavīra leaves", "Karavīra leaves cook the oil of card 18."),
             ("Triphalā", "Triphalā is in card 18.")],
            "Only mālatī and madhuka are named here.",
            "मालतीमधुकसिद्धेनाम्भसा."),
        mcq("transfer", 5, "By the rule of पुनर्मालती, how is पुनः + आगच्छति (comes again) joined?",
            ("पुनरागच्छति", "पुनः keeps its र् before a vowel or voiced sound, as पुनर्मालती."),
            [("पुनागच्छति", "The र् of पुनर् is not dropped before a vowel."),
             ("पुनोऽगच्छति", "पुनर् does not join like अः; ओऽ would also lose the आ."),
             ("पुनस्आगच्छति", "स् is not used before a vowel.")],
            "पुनः + आगच्छति = पुनरागच्छति.",
            "पुनर् keeps र् before a voiced sound.",
            teaches="पुनः ends in र्, which shows before a voiced sound or vowel: पुनः + मालती → पुनर्मालती."),
    ],
}

# ---------------------------------------------------------------- unit 20
AUTHORED["20"] = {
    "title": "कंडूयनं वर्जयेत्",
    "question": "By unit 20, what should she avoid?",
    "rule": "She should avoid (वर्जयेत्) scratching (कण्डूयन). The optative -एत् gives an instruction: should.",
    "limits": ("The subject is not printed; the pregnant woman is understood. The line gives no reason; the itching of "
               "card 14 is the context, not stated here."),
    "explain_hi": ("दो शब्दों की गद्य-पंक्ति: खुजलाना (कण्डूयन) त्याग दे (वर्जयेत्)। "
                   "कर्ता छपा नहीं; गर्भवती स्त्री समझी जाती है। "
                   "‘वर्जयेत्’ विधिलिङ् है: ‘-एत्’ से ‘करे, करना चाहिए’ का निर्देश बनता है। "
                   "कारण यहाँ नहीं लिखा; कार्ड 14 की खुजली इसका प्रसंग है।"),
    "hook": "खुजली हो, फिर भी खुजलाओ मत।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 20, what should she avoid?",
            ("Scratching", "कण्डूयनं वर्जयेत्."),
            [("Sweet food", "Sweet food is advised in card 22."),
             ("Bathing", "Bathing is advised in card 21."),
             ("Sandalwood", "Sandalwood is used in cards 16 and 21.")],
            "Scratching is to be avoided.",
            "कण्डूयनम् = scratching."),
        match(1, "Match each part of unit 20 to its meaning.",
              [["कण्डूयनम्", "scratching"], ["वर्जयेत्", "should avoid"], ["-एत्", "should (optative ending)"]],
              "Two words and the ending that makes the instruction.",
              "कण्डूयनम्, वर्जयेत्, -एत्."),
        T(fill(2, "She should avoid scratching: कंडूयनं ____ (type it in Devanagari or in English letters, e.g. dharma).",
               accepts("वर्जयेत्"),
               "The line is कंडूयनं वर्जयेत्.",
               "वर्जयेत् = should avoid.",
               "वर्जयेत् = should avoid."),
          "वर्जयेत् = she should avoid: optative of √वृज् (causative)."),
        mcq("discriminate", 3, "What does the form वर्जयेत् express?",
            ("An instruction: she should avoid", "The data: 3 sg. optative, should avoid."),
            [("A past fact: she avoided", "A past form would be different; -एत् is optative."),
             ("A future: she will avoid", "No future ending is here."),
             ("A plain present: she avoids", "The present would be वर्जयति.")],
            "-एत् = optative: should.",
            "वर्जयेत् = should avoid."),
        mcq("apply", 4, "By unit 20, who is to avoid scratching?",
            ("The pregnant woman, understood; no subject is printed", "The data: subject understood, the pregnant woman."),
            [("The physician, named in the line", "No one is named in the line."),
             ("The embryo", "The embryo cannot scratch; the data names the woman."),
             ("The women who speak in card 13", "Those women report a view; they are not the subject here.")],
            "The subject is understood, not printed.",
            "Subject understood: the pregnant woman."),
        mcq("transfer", 5, "By the optative -एत् of वर्जयेत्, what does सत्यं वदेत् mean?",
            ("One should speak the truth", "-एत् = should, as वर्जयेत् = should avoid."),
            [("One spoke the truth", "A past would need a past form."),
             ("One will speak the truth", "A future would be वदिष्यति."),
             ("One is speaking the truth", "The present would be वदति.")],
            "वदेत् = should speak.",
            "-एत् = should.",
            teaches="The optative ending -एत् gives a rule of conduct: वर्जयेत् = should avoid, वदेत् = should speak."),
    ],
}

# ---------------------------------------------------------------- unit 21
AUTHORED["21"] = {
    "title": "त्वग्भेदे वैरूप्यपरिहारार्थं",
    "question": "By unit 21, what should she use when the skin splits, and for what purpose?",
    "rule": ("When the skin splits (त्वग्भेदे), to avoid disfigurement (वैरूप्यपरिहारार्थम्), she should use (शीलयेत्) bathing, "
             "rubbing with powders (उद्वर्तन) and sandalwood. -अर्थम् = for the purpose of."),
    "limits": ("The line does not say what splits the skin; the data says probably the stretch marks of the previous units, "
               "not stated. No amounts or ingredients of the udvartana are given. The subject (the pregnant woman) is understood."),
    "explain_hi": ("त्वचा फटने पर (त्वग्भेदे), कुरूपता से बचने के लिए (वैरूप्यपरिहारार्थम्), स्नान, उद्वर्तन (उबटन) और चन्दन का "
                   "प्रयोग करे (शीलयेत्)। "
                   "‘-अर्थम्’ का अर्थ है ‘के लिए’। "
                   "त्वचा का फटना सम्भवतः पिछली इकाइयों की खिंचाव-धारियाँ हैं, पर पंक्ति यह नहीं कहती। "
                   "‘त्वग्भेदे’ में त्वक् + भेदे है: क् घोष से पहले ग् बनता है।"),
    "hook": "त्वचा फटे: स्नान, उबटन, चन्दन, ताकि रूप न बिगड़े।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 21, when is this care used?",
            ("When the skin splits", "त्वग्भेदे: when the skin splits."),
            [("When the hair arises", "Hair is the women's view of card 13."),
             ("In the eighth month", "The eighth month is card 23."),
             ("After the child is born", "No birth is named here.")],
            "त्वक् (skin) + भेद (splitting), locative: when.",
            "त्वग्भेदे = when the skin splits."),
        order(1, "Put the words of unit 21 in the line's order.",
              ["त्वग्भेदे", "वैरूप्यपरिहारार्थम्", "स्नानोद्वर्तनम्", "चन्दनम्", "च", "शीलयेत्"],
              "When the skin splits, to avoid disfigurement, bathing and udvartana, sandalwood, and, she should use.",
              "त्वग्भेदे → वैरूप्यपरिहारार्थम् → स्नानोद्वर्तनम् → चन्दनम् → च → शीलयेत्."),
        match(2, "Match each word of unit 21 to its meaning.",
              [["त्वक्", "skin"], ["भेद", "splitting"], ["वैरूप्य", "disfigurement"], ["परिहार", "avoidance"],
               ["उद्वर्तन", "rubbing with powders"], ["शीलयेत्", "should make use of"]],
              "When, why, what and the verb.",
              "त्वक्, भेद, वैरूप्य, परिहार, उद्वर्तन, शीलयेत्.", role="extend",
              teaches="-अर्थम् at the end = for the purpose of: वैरूप्यपरिहारार्थम् = to avoid disfigurement."),
        mcq("discriminate", 3, "Which split of स्नानोद्वर्तनम् is right?",
            ("स्नान + उद्वर्तनम्", "अ + उ → ओ: स्नान + उद्वर्तनम्."),
            [("स्नानः + उद्वर्तनम्", "अः before उ would give स्नान उद्वर्तनम्."),
             ("स्नानम् + उद्वर्तनम्", "A final म् would give स्नानमुद्वर्तनम्."),
             ("स्नानो + द्वर्तनम्", "द्वर्तनम् is not a word; the word is उद्वर्तनम्.")],
            "स्नान (bathing) + उद्वर्तन (rubbing with powders).",
            "अ + उ → ओ."),
        multi("apply", 4, "Which does unit 21 tell her to use?",
              [("Bathing (स्नान)", "Right: स्नानोद्वर्तनम्."),
               ("An oil enema", "No enema is named in unit 21."),
               ("Rubbing with powders (उद्वर्तन)", "Right: स्नानोद्वर्तनम्."),
               ("Scratching the skin", "Scratching is to be avoided, card 20."),
               ("Sandalwood (चन्दन)", "Right: चन्दनं च.")],
              [0, 2, 4],
              "Bathing, udvartana and sandalwood.",
              "स्नानोद्वर्तनं चन्दनं च शीलयेत्."),
        mcq("transfer", 5, "By the rule of त्वग्भेदे, how is वाक् + दानम् (promise) joined?",
            ("वाग्दानम्", "क् becomes ग् before a voiced sound, as त्वक् + भेदे."),
            [("वाक्दानम्", "Before the voiced द the क् does not stay."),
             ("वाङ्दानम्", "क् becomes ङ् only before a nasal."),
             ("वाच्दानम्", "क् does not become च्.")],
            "वाक् + दानम् = वाग्दानम्, like त्वक् + भेदे = त्वग्भेदे.",
            "Final क् → ग् before a voiced sound.",
            teaches="A final क् becomes ग् before a voiced sound: त्वक् + भेदे → त्वग्भेदे."),
    ],
}

# ---------------------------------------------------------------- unit 22
AUTHORED["22"] = {
    "title": "मधुरं चाहारमल्प... भुंजीत",
    "question": "By unit 22, what kind of food should she eat, and what is kept little?",
    "rule": ("She should eat (भुञ्जीत) sweet food (मधुर आहार), little in quantity, with little fat and salt "
             "(अल्पस्नेहलवण) and little water as after-drink (अल्पोदकानुपान)."),
    "limits": ("The unit names no month and no foods by name; the subject is understood. अल्प is taken as little in "
               "quantity. स्नेह = oil or fat, its kind not named."),
    "explain_hi": ("और वह मधुर आहार खाए (भुञ्जीत): मात्रा में थोड़ा, थोड़े स्नेह (तेल या वसा) और नमक वाला, "
                   "और भोजन के बाद थोड़े जल का अनुपान। "
                   "‘अल्प’ तीन बार आता है: आहार की मात्रा, स्नेह-लवण, और अनुपान का जल। "
                   "‘अल्पस्नेहलवणम्’ और ‘अल्पोदकानुपानम्’ बहुव्रीहि हैं, आहार के विशेषण: ‘जिसमें ... थोड़ा हो’। "
                   "कोई मास या भोजन का नाम इस पंक्ति में नहीं।"),
    "hook": "मीठा, थोड़ा; चिकनाई-नमक थोड़ा; ऊपर से पानी थोड़ा।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 22, what kind of food should she eat?",
            ("Sweet food, little in quantity", "मधुरं चाहारम् अल्पम्."),
            [("Salty food, in plenty", "Salt is to be little (अल्पलवण)."),
             ("Sour and dry food", "The line says sweet (मधुर)."),
             ("Bitter food with much water", "The line says sweet, with little water.")],
            "Sweet and little.",
            "मधुरम् आहारम् अल्पम्."),
        order(1, "Put the words of unit 22 in the line's order.",
              ["मधुरम्", "आहारम्", "अल्पम्", "अल्पस्नेहलवणम्", "अल्पोदकानुपानम्", "भुञ्जीत"],
              "Sweet food, little, with little fat and salt, with little water after, she should eat.",
              "मधुरम् → आहारम् → अल्पम् → अल्पस्नेहलवणम् → अल्पोदकानुपानम् → भुञ्जीत."),
        match(2, "Match each word of unit 22 to its meaning.",
              [["मधुर", "sweet"], ["आहार", "food"], ["अल्प", "little"], ["स्नेह", "oil or fat"],
               ["लवण", "salt"], ["अनुपान", "after-drink"]],
              "The food, its taste and what is kept little.",
              "मधुर, आहार, अल्प, स्नेह, लवण, अनुपान.", role="extend",
              teaches="अल्प- opening a bahuvrīhi = having little: अल्पस्नेहलवणम् = (food) having little fat and salt."),
        mcq("discriminate", 3, "Which split of अल्पोदकानुपानम् is right?",
            ("अल्प + उदक + अनुपानम्", "अ + उ → ओ and अ + अ → आ."),
            [("अल्पो + दक + अनुपानम्", "दक is not a word; the word is उदक (water)."),
             ("अल्प + उदका + नुपानम्", "नुपानम् is not a word; the word is अनुपान."),
             ("अल्प + ओदक + अनुपानम्", "अ + ओ would give औ, and ओदक is not a word.")],
            "अल्प (little) + उदक (water) + अनुपान (after-drink).",
            "अ + उ → ओ; अ + अ → आ."),
        multi("apply", 4, "What does unit 22 keep little (अल्प)?",
              [("The amount of food", "Right: आहारम् अल्पम्."),
               ("The sweetness of the food", "The food is sweet; sweetness is not limited."),
               ("The oil or fat and the salt", "Right: अल्पस्नेहलवणम्."),
               ("The water taken after the meal", "Right: अल्पोदकानुपानम्."),
               ("The number of meals a day", "No number of meals is given.")],
              [0, 2, 3],
              "Three things are little: quantity, fat-and-salt, after-drink water.",
              "अल्पम् ... अल्पस्नेहलवणम् ... अल्पोदकानुपानम्."),
        mcq("transfer", 5, "By the bahuvrīhi अल्पस्नेहलवणम्, what does अल्पधनः पुरुषः mean?",
            ("A man having little wealth", "अल्प + धन as a bahuvrīhi describing पुरुषः."),
            [("A man of great wealth", "अल्प means little, not great."),
             ("A man with no wealth at all", "अल्प is little, not none."),
             ("A man who gives little wealth", "Giving is not in the compound.")],
            "अल्पधनः = having little wealth, as अल्पस्नेहलवणम् = having little fat and salt.",
            "अल्प-X (bahuvrīhi) = having little X.",
            teaches="A bahuvrīhi with अल्प- describes its noun: अल्पस्नेहलवणम् आहारम् = food having little fat and salt."),
    ],
}

# ---------------------------------------------------------------- unit 23
AUTHORED["23"] = {
    "title": "अष्टमे क्षीरयवागूं सर्पिष्मतीं पिबेत्",
    "question": "By unit 23, what should she drink in the eighth (month), and what objection follows?",
    "rule": ("In the eighth (month) she should drink milk gruel (क्षीरयवागू) containing ghee (सर्पिष्मती). An objection "
             "follows: not so (नेति), from fear of a tawny-colour affliction (पैङ्गल्याबाध) to the embryo."),
    "limits": ("Low confidence. षंढकाथो does not parse: it may hide a speaker's name or a form of कथ्; no question on who "
               "objects. Of what the tawny colour is, is not stated. The compound क्षीरयवागू could also be gruel and milk. "
               "The discussion continues into card 24."),
    "explain_hi": ("आठवें (मास) में वह घी वाली (सर्पिष्मती) दूध की यवागू पिए। "
                   "फिर आपत्ति आती है: ‘नेति’ (ऐसा नहीं), क्योंकि गर्भ को पिंगलता (पीला-भूरा रंग) की बाधा का भय है। "
                   "छपा ‘षंढकाथो’ अस्पष्ट है: सम्भवतः किसी आपत्ति करने वाले आचार्य का नाम, पर यह अनुमान है; इस पर प्रश्न नहीं। "
                   "पिंगलता किसकी, यह नहीं कहा। "
                   "यह चर्चा अगली इकाई (कार्ड 24) में चलती है।"),
    "hook": "आठवें में घी-दूध की यवागू; आपत्ति: गर्भ पीला-भूरा न हो जाए।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 23, what should she drink in the eighth (month)?",
            ("Milk gruel containing ghee", "क्षीरयवागूं सर्पिष्मतीं पिबेत्."),
            [("Water cooked with mālatī", "That water is for pouring, card 19."),
             ("Jujube water with honey", "Jujube water goes into the enema of card 26."),
             ("Plain cold water", "The line names milk gruel with ghee.")],
            "Milk gruel with ghee.",
            "क्षीरयवागूम् सर्पिष्मतीम्."),
        order(1, "Put these words of unit 23 in the text's order.",
              ["अष्टमे", "क्षीरयवागूम्", "सर्पिष्मतीम्", "पिबेत्", "नेति", "भयात्"],
              "In the eighth, milk gruel, containing ghee, she should drink; not so, from fear.",
              "अष्टमे → क्षीरयवागूम् → सर्पिष्मतीम् → पिबेत् → नेति → भयात्."),
        match(2, "Match each word of unit 23 to its meaning.",
              [["क्षीर", "milk"], ["यवागू", "gruel"], ["सर्पिष्मती", "containing ghee"],
               ["पैङ्गल्य", "tawny colour"], ["आबाध", "affliction"], ["भय", "fear"]],
              "The drink, then the words of the objection's reason.",
              "क्षीर, यवागू, सर्पिष्मती, पैङ्गल्य, आबाध, भय.", role="extend",
              teaches="-भयात् = from fear of: the ablative gives the reason of the objection."),
        mcq("discriminate", 3, "By unit 23, what reason does the objection give?",
            ("Fear of a tawny-colour affliction to the embryo", "गर्भस्य पैङ्गल्याबाधभयात्."),
            [("The gruel is too heavy for the mother", "No heaviness is named."),
             ("Ghee causes itching of the skin", "Itching is card 14; no such link is said."),
             ("The eighth month is too early for gruel", "No timing objection is made.")],
            "The reason: fear of tawny colour to the embryo.",
            "पैङ्गल्याबाधभयात्."),
        mcq("apply", 4, "Which split of नेति is right?",
            ("न + इति", "अ + इ → ए: न + इति = नेति."),
            [("न + एति", "अ + ए would give ऐ: नैति."),
             ("ने + इति", "ए + इ would not give नेति; ने is not the word."),
             ("नः + इति", "नः is not the word; the word is न (not).")],
            "न (not) + इति (thus).",
            "अ + इ → ए."),
        mcq("transfer", 5, "By the -मती of सर्पिष्मतीम्, what does बुद्धिमती कन्या mean?",
            ("A girl having intelligence", "-मती (f. of -मत्) = having, agreeing with a feminine noun."),
            [("A girl without intelligence", "-मती means having, not lacking."),
             ("The intelligence of a girl", "बुद्धिमती describes कन्या; it is not a genitive."),
             ("A girl giving intelligence", "-मती does not mean giving.")],
            "बुद्धिमती = having intelligence, as सर्पिष्मती = having ghee.",
            "-मत् / -मती = having.",
            teaches="-मत् (feminine -मती) = having: सर्पिष्मती यवागू = gruel having ghee."),
    ],
}

# ---------------------------------------------------------------- unit 24
AUTHORED["24"] = {
    "title": "अस्ति पैंगल्याबाधस्तथाप्येवं कुर्वीत",
    "question": "By unit 24, what is granted, and what is still advised?",
    "rule": ("There is (अस्ति) the tawny-colour affliction; even so (तथापि), one should act thus (एवं कुर्वीत). "
             "तथापि marks a concession: granted, yet."),
    "limits": ("The line does not name its speaker. That एवम् (thus) points to the gruel with ghee of card 23 comes from "
               "context, not stated. The line continues the discussion begun in card 23."),
    "explain_hi": ("पिंगलता की बाधा है (अस्ति), फिर भी (तथापि) ऐसा ही करे (एवं कुर्वीत)। "
                   "यह मान लेने वाला उत्तर है: जोखिम माना, पर उपदेश नहीं छोड़ा। "
                   "‘एवम्’ सन्दर्भ से कार्ड 23 की घी वाली यवागू की ओर संकेत करता है; यह लिखा नहीं। "
                   "वक्ता का नाम इस पंक्ति में नहीं। "
                   "‘अप्येवम्’ में अपि + एवम् है (इ + ए → ये)।"),
    "hook": "बाधा है, तो भी यही करो।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 24, what does the line grant?",
            ("That the tawny-colour affliction exists", "अस्ति पैङ्गल्याबाधः."),
            [("That there is no affliction at all", "अस्ति = there is."),
             ("That the gruel cures the tawny colour", "No cure is said."),
             ("That the affliction falls on the mother", "The line does not say on whom.")],
            "The affliction is granted.",
            "अस्ति पैङ्गल्याबाधः."),
        order(1, "Put the words of unit 24 in the line's order.",
              ["अस्ति", "पैङ्गल्याबाधः", "तथा", "अपि", "एवम्", "कुर्वीत"],
              "There is the affliction; even so, thus one should act.",
              "अस्ति → पैङ्गल्याबाधः → तथा → अपि → एवम् → कुर्वीत."),
        match(2, "Match each word of unit 24 to its meaning.",
              [["अस्ति", "there is"], ["आबाध", "affliction"], ["तथापि", "even so"],
               ["एवम्", "thus"], ["कुर्वीत", "one should act"]],
              "Grant, concession, and the advice.",
              "अस्ति, आबाध, तथापि, एवम्, कुर्वीत.", role="extend",
              teaches="तथापि = even so: it keeps an advice after granting a drawback."),
        mcq("discriminate", 3, "Which split of अप्येवं (अप्येवम्) is right?",
            ("अपि + एवम्", "इ + ए → ये: अपि + एवम्."),
            [("अप्य + एवम्", "अ + ए would give ऐ: अप्यैवम्."),
             ("अपि + इवम्", "इ + इ would give ई: अपीवम्."),
             ("अप् + येवम्", "Neither अप् nor येवम् is the word here.")],
            "अपि (even) + एवम् (thus).",
            "इ + a different vowel → य्."),
        mcq("apply", 4, "By unit 24, what stance does the line take?",
            ("It grants the risk but keeps the advice", "अस्ति ... तथाप्येवं कुर्वीत."),
            [("It denies that there is any risk", "अस्ति grants it."),
             ("It drops the advice because of the risk", "तथापि ... कुर्वीत keeps it."),
             ("It advises a different drink", "No new drink is named.")],
            "A concession: yes, but still do it.",
            "अस्ति ... तथापि ... कुर्वीत."),
        mcq("transfer", 5, "By the rule of पैङ्गल्याबाधस्तथा, how is रामः + तत्र (Rāma there) joined?",
            ("रामस्तत्र", "A visarga before त becomes स्, as आबाधः + तथा."),
            [("रामो तत्र", "अः → ओ only before a voiced sound; त is unvoiced."),
             ("रामर्तत्र", "र् comes after vowels other than अ/आ."),
             ("रामतत्र", "The visarga is not simply dropped before त.")],
            "रामः + तत्र = रामस्तत्र.",
            "Visarga + त → स्त.",
            teaches="A visarga before त/थ becomes स्: पैङ्गल्याबाधः + तथा → पैङ्गल्याबाधस्तथा."),
    ],
}

# ---------------------------------------------------------------- unit 25
AUTHORED["25"] = {
    "title": "नीरुजं ... अपत्यं जनयतीति भगवान्आत्रेयः",
    "question": "By unit 25, what kind of child does she bear, and who says so?",
    "rule": ("She bears a child (अपत्य) free of disease (नीरुज), endowed with excellence of strength, complexion, sattva "
             "and firm build (बल, वर्ण, सत्त्व, संहनन), foremost among kinsmen: so says Ātreya."),
    "limits": ("The subject of जनयति is not printed; the woman who follows the regimen is understood. सत्त्व is kept as a "
               "doctrinal term (mind, mental strength). The verb of speaking for Ātreya is carried by इति."),
    "explain_hi": ("वह ऐसी सन्तान को जन्म देती है जो रोग-रहित (नीरुज) हो, बल, वर्ण (रंग), सत्त्व (मन की शक्ति) और संहनन "
                   "(शरीर की सुगठित रचना) की सम्पदा से युक्त हो, और सम्बन्धियों में अग्रगण्य हो। "
                   "‘इति भगवान् आत्रेयः’: ऐसा भगवान् आत्रेय कहते हैं। "
                   "कर्ता छपा नहीं; ऊपर का नियम मानने वाली स्त्री समझी जाती है। "
                   "‘जनयतीति’ में जनयति + इति है (इ + इ → ई)।"),
    "hook": "नीरोग, बल-वर्ण-सत्त्व-संहनन से भरपूर, कुल में अग्रणी: आत्रेय का वचन।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 25, what is the child first said to be?",
            ("Free of disease (नीरुज)", "नीरुजम्: free of disease."),
            [("Of tawny colour", "Tawny colour is the feared affliction of cards 23-24."),
             ("Born early, in the seventh month", "No early birth is named."),
             ("Weak but long-lived", "The child is endowed with strength (बल).")],
            "The child is free of disease.",
            "नीरुजम् अपत्यम्."),
        order(1, "Put these words of unit 25 in the line's order.",
              ["नीरुजम्", "बल", "वर्ण", "सत्त्व", "संहनन", "अपत्यम्"],
              "Free of disease; strength, complexion, sattva, build; child.",
              "नीरुजम् → बल → वर्ण → सत्त्व → संहनन → अपत्यम्."),
        match(2, "Match each word of unit 25 to its meaning.",
              [["नीरुज", "free of disease"], ["बल", "strength"], ["वर्ण", "complexion"],
               ["सत्त्व", "sattva, mind, mental strength"], ["संहनन", "firm build of the body"],
               ["अग्रगण्य", "foremost"]],
              "The qualities of the child.",
              "नीरुज, बल, वर्ण, सत्त्व, संहनन, अग्रगण्य.", role="extend",
              teaches="सम्पद् = excellence, उपेत = endowed with: बल...संहननसम्पदुपेतम् = endowed with the excellence of these four."),
        mcq("discriminate", 3, "Which split of जनयतीति is right?",
            ("जनयति + इति", "इ + इ → ई: जनयति + इति."),
            [("जनयती + ति", "ति is not a word here; इति is the quoting word."),
             ("जनयते + इति", "ए + इ would give जनयत इति, with a gap."),
             ("जनयत् + ईति", "ईति is not the word; the word is इति.")],
            "जनयति (she produces) + इति (thus).",
            "इ + इ → ई."),
        mcq("apply", 4, "By unit 25, among whom is the child foremost?",
            ("Among its kinsmen (ज्ञातीनाम्)", "ज्ञातीनामग्रगण्यम्: foremost among kinsmen."),
            [("Among the physicians", "No physicians are named."),
             ("Among the children of its age", "The line says kinsmen (ज्ञाति)."),
             ("Among Ātreya's pupils", "Ātreya is the speaker, not a group.")],
            "ज्ञातीनाम् = among kinsmen.",
            "ज्ञातीनाम् अग्रगण्यम्."),
        mcq("transfer", 5, "By the rule of जनयतीति, how is गच्छति + इति (thus he goes) joined?",
            ("गच्छतीति", "इ + इ → ई, as जनयति + इति."),
            [("गच्छतेति", "ए comes from अ + इ, not इ + इ."),
             ("गच्छत्यिति", "य् comes before a different vowel, not before इ."),
             ("गच्छतिति", "The two इ do not shorten to one इ.")],
            "गच्छति + इति = गच्छतीति.",
            "इ + इ → ई.",
            teaches="Two इ join as ई: जनयति + इति → जनयतीति."),
    ],
}

# ---------------------------------------------------------------- unit 26
AUTHORED["26"] = {
    "title": "बदरोदकेन ... युक्तेनास्थापयेत्",
    "question": "By unit 26, which enema is given, and with what?",
    "rule": ("One should give an āsthāpana (decoction enema) with jujube water (बदरोदक) joined with palala, milk, curd, "
             "whey (मस्तु), oil, salt, fruit, ghee and honey."),
    "limits": ("palala is disputed (possibly sesame paste; flesh is another meaning): no question on it. Ghee rests on "
               "reading printed गृत as घृत: no question on it. The fruit is not named. Amounts and the month are not given; "
               "the pregnant woman is understood."),
    "explain_hi": ("बदर (बेर, मानक) के जल से, जिसमें पलल (पहचान विवादित; सम्भवतः तिल की लुगदी), दूध, दही, मस्तु (दही का पानी), "
                   "तेल, नमक, फल, घी और मधु मिले हों, आस्थापन (काढ़े की वस्ति) दे। "
                   "छपा ‘गृत’ कोई शब्द नहीं; ‘घृत’ (घी) सम्भावित सुधार है। "
                   "कौन-सा फल, कितनी मात्रा, यह नहीं कहा। "
                   "‘बदरोदकेन’ में बदर + उदकेन है (अ + उ → ओ)।"),
    "hook": "बेर-जल में दूध-दही-मस्तु-तेल-नमक-मधु: आस्थापन वस्ति।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 26, which procedure is named?",
            ("Āsthāpana, a decoction enema", "आस्थापयेत्: one should give an āsthāpana."),
            [("Abhyaṅga, an oil massage", "That is card 18."),
             ("Pariṣeka, pouring", "That is card 19."),
             ("A drink of milk gruel", "That is card 23.")],
            "The verb आस्थापयेत् names the decoction enema.",
            "आस्थापयेत् = give an āsthāpana."),
        order(1, "Put these substances of unit 26 in the text's order.",
              ["पयः", "दधि", "मस्तु", "तैल", "लवण", "मधु"],
              "Milk, curd, whey, oil, salt, ... honey.",
              "पयः → दधि → मस्तु → तैल → लवण → मधु."),
        match(2, "Match each word of unit 26 to its meaning.",
              [["बदर", "jujube (standard)"], ["पयस्", "milk"], ["दधि", "curd"], ["मस्तु", "whey"],
               ["लवण", "salt"], ["मधु", "honey"]],
              "The base water and five of the added substances.",
              "बदर, पयस्, दधि, मस्तु, लवण, मधु.", role="extend",
              teaches="The base of the enema is बदरोदक, jujube water; the others are joined (युक्त) to it."),
        mcq("discriminate", 3, "Which split of बदरोदकेन is right?",
            ("बदर + उदकेन", "अ + उ → ओ: बदर + उदकेन."),
            [("बदरो + दकेन", "दकेन is not a word; the word is उदक (water)."),
             ("बदरः + उदकेन", "अः before उ would give बदर उदकेन."),
             ("बदरम् + उदकेन", "A final म् would give बदरमुदकेन.")],
            "बदर (jujube) + उदक (water).",
            "अ + उ → ओ."),
        multi("apply", 4, "Which substances does unit 26 name?",
              [("Sandalwood", "Sandalwood is in cards 16 and 21."),
               ("Curd (दधि)", "Right: पयोदधि."),
               ("Whey (मस्तु)", "Right: मस्तु."),
               ("Turmeric", "Turmeric is in card 17."),
               ("Honey (मधु)", "Right: मधुयुक्तेन.")],
              [1, 2, 4],
              "Curd, whey and honey are in the list.",
              "पललपयोदधिमस्तुतैललवणफल(घृत)मधु."),
        mcq("transfer", 5, "By the rule of पयोदधि (पयस् + दधि), how is मनस् + रथः (wish) joined in a compound?",
            ("मनोरथः", "Stem-final -अस् becomes ओ before a voiced consonant, as पयस् + दधि → पयोदधि."),
            [("मनस्रथः", "The स् does not stay before a voiced consonant."),
             ("मनरथः", "The -अस् is not simply dropped."),
             ("मनोऽरथः", "ऽ marks a lost अ; रथः does not begin with अ.")],
            "मनस् + रथः = मनोरथः, like पयस् + दधि = पयोदधि.",
            "-अस् + voiced consonant → -ओ.",
            teaches="A stem in -अस् shows -ओ before a voiced consonant: पयस् + दधि → पयोदधि."),
    ],
}


# ===================================================================== NOTES_HI
NOTES_HI = {
    "14": ("गद्य; विश्वास निम्न; कोई पाठ-चिह्न नहीं। अन्तिम शब्द ‘कंडूकिकिसं’ अस्पष्ट: कण्डू + किकिस (किक्किस), किकिस सम्भवतः "
           "गर्भावस्था की त्वचा की खिंचाव-धारियाँ (सम्भावित); ‘कंडूर्जायते’ के बाद कण्डू की पुनरावृत्ति अटपटी है, समास का प्रकार "
           "अस्पष्ट, और पंक्ति बिना क्रिया के समाप्त होती लगती है; इस पर प्रश्न नहीं। वक्ता का नाम नहीं। "
           "सन्धि जाँची: गर्भ + उत्पीडनात् → गर्भोत्पीडनात् (अ + उ → ओ); उत्पीडनात् + तु → उत्पीडनात्तु; दोषाः + हृदयम् → दोषा हृदयम् "
           "(आः → आ घोष से पहले); कण्डूः + जायते → कण्डूर्जायते (ऊ के बाद विसर्ग → र्)।"),
    "15": ("गद्य; विश्वास मध्यम। पाठ-चिह्न: छपा ‘कोलोडकेन’ सम्भवतः ‘कोलोदकेन’ (ड/द की छपाई-भूल); कोल + उदक = कोल का जल, "
           "कोल सम्भवतः बेर (Ziziphus jujuba, सम्भावित; कोल के अन्य अर्थ भी)। यदि ‘कोलोडक’ कोई शब्द हो तो अज्ञात; इस पर प्रश्न नहीं। "
           "‘अस्यै’ = इस (गर्भवती) स्त्री को। सन्धि जाँची: मधुर + औषध → मधुरौषध (अ + औ → औ); पाणितलमात्रम् + अस्यै → "
           "पाणितलमात्रमस्यै (म् स्वर से मिलता है)।"),
    "16": ("गद्य; विश्वास मध्यम; दो छपी पंक्तियाँ (02.03.16 और 02.03.17)। पाठ-चिह्न: ‘मृद्गीयात्’ कोई रूप नहीं, ‘मृद्नीयात्’ "
           "(√मृद्, क्र्यादि, विधिलिङ्) सम्भावित सुधार (ग/न भ्रम); ‘घातुकी’ ज्ञात औषध नहीं, ‘धातकी’ (Woodfordia fruticosa) अनुमानित "
           "पाठ (घ/ध भ्रम) — इस पर प्रश्न नहीं। मधुक सम्भवतः मुलेठी (Glycyrrhiza glabra), दूसरा विकल्प महुआ (Madhuca longifolia)। "
           "दूसरी पंक्ति में क्रिया पहली से आती है; मलने वाली गर्भवती स्त्री समझी जाती है। "
           "सन्धि जाँची: कल्कैः + च → कल्कैश्च; स्तन + उदरम् → स्तनोदरम् (अ + उ → ओ); चूर्णैः + वा → चूर्णैर्वा (ऐ के बाद विसर्ग → र्)।"),
    "17": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। क्रिया कार्ड 16 से आती है। ‘कोळ’ का ‘ळ’ ल माना गया (छपाई की आदत)। "
           "‘बीज’ कुटज और अर्जक दोनों से जुड़ा माना गया (डेटा का पाठ)। छपा ‘सुरस’ सुरसा (सम्भवतः तुलसी) पढ़ा गया; अर्जक "
           "सम्भवतः एक श्वेत तुलसी, कोल सम्भवतः बेर — ये तीनों सम्भावित, इन पर प्रश्न नहीं। "
           "सन्धि जाँची: कुटज + अर्जक → कुटजार्जक (अ + अ → आ); कल्कैः + वा → कल्कैर्वा (ऐ के बाद विसर्ग → र्)।"),
    "18": ("गद्य; विश्वास मध्यम। पाठ-चिह्न: ‘सिद्धैनांभसा’ सिद्धेन + अम्भसा की नियमित सन्धि नहीं (नियमित: सिद्धेनाम्भसा); ऐ/ए "
           "छपाई-भूल सम्भव — इस पर प्रश्न नहीं। खरगोश-हिरन का कौन-सा भाग (सम्भवतः मांस) — लिखा नहीं। जल, रुधिर-युक्त त्रिफला "
           "और तेल एक ही अभ्यंग के तीन साधन; कैसे मिलें, नहीं कहा। मालती विवादित; मधुक सम्भावित; करवीर = Nerium oleander (मानक); "
           "त्रिफला = हरीतकी, बिभीतक, आमलकी (मानक); तेल का प्रकार नहीं। सन्धि जाँची: तैलेन + अभ्यङ्गः → तैलेनाभ्यङ्गः (अ + अ → आ)।"),
    "19": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। क्रिया नहीं (अध्याहार)। ‘पुनः’ = फिर, या ‘और आगे’ — दोनों सम्भव, प्रश्न नहीं। "
           "मालती, मधुक: कार्ड 18 जैसी पहचान (विवादित / सम्भावित)। सन्धि जाँची: पुनर् + मालती → पुनर्मालती (र् घोष से पहले रहता है); "
           "सिद्धेन + अम्भसा → सिद्धेनाम्भसा (अ + अ → आ), छपा ‘सिद्धेनांभसा’ (अनुस्वार = म्)।"),
    "20": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। कर्ता अलिखित (गर्भवती स्त्री समझी जाती है)। वर्जयेत् = √वृज्, णिजन्त, विधिलिङ्, "
           "प्रथम पुरुष एकवचन। सन्धि: कण्डूयनम् + वर्जयेत् → कण्डूयनं वर्जयेत् (पदान्त म् व्यञ्जन से पहले अनुस्वार)।"),
    "21": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। छपा ‘अर्थंस्नान’ और ‘चशीलयेत्’ बिना अन्तराल — दो-दो शब्द, अर्थ नहीं बदलता। "
           "त्वग्भेद सम्भवतः पिछली इकाइयों की खिंचाव-धारियाँ, पर लिखा नहीं। सन्धि जाँची: त्वक् + भेदे → त्वग्भेदे (क् → ग् घोष से पहले); "
           "परिहार + अर्थम् → परिहारार्थम् (अ + अ → आ); स्नान + उद्वर्तनम् → स्नानोद्वर्तनम् (अ + उ → ओ)।"),
    "22": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। ‘अल्प’ मात्रा के अर्थ में (थोड़ा)। कर्ता अलिखित। भुञ्जीत = √भुज्, विधिलिङ्, "
           "आत्मनेपद। सन्धि जाँची: च + आहारम् → चाहारम् (अ + आ → आ); आहारम् + अल्पम् → आहारमल्पम्; अल्प + उदक → अल्पोदक "
           "(अ + उ → ओ); उदक + अनुपानम् → उदकानुपानम् (अ + अ → आ)।"),
    "23": ("गद्य; विश्वास निम्न; दो छपी पंक्तियाँ (02.03.24 और 02.03.25)। पाठ-चिह्न: ‘षंढकाथो’ विभक्त नहीं होता — सम्भवतः किसी वक्ता "
           "का नाम (तुलना: कार्ड 13 का ‘भगवान् आत्रेयः’) या √कथ् का रूप; कोई निश्चित पाठ नहीं, इस पर प्रश्न नहीं। "
           "‘अष्टमे’ = आठवें (मास) में। क्षीरयवागू = दूध की यवागू (‘यवागू और दूध’ भी सम्भव, नहीं अपनाया)। पैङ्गल्य = पीला-भूरा रंग, "
           "किसका — लिखा नहीं। वर्गीकरण: चर्चा कार्ड 24 में चलती है। सन्धि जाँची: न + इति → नेति (अ + इ → ए)।"),
    "24": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। ‘एवम्’ सन्दर्भ से कार्ड 23 की घी वाली यवागू की ओर, लिखा नहीं। वक्ता अलिखित। "
           "सन्धि जाँची: पैङ्गल्य + आबाधः → पैङ्गल्याबाधः (अ + आ → आ); आबाधः + तथा → आबाधस्तथा (विसर्ग → स् त से पहले); "
           "तथा + अपि → तथापि (आ + अ → आ); अपि + एवम् → अप्येवम् (इ + ए → ये)।"),
    "25": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। जनयति का कर्ता अलिखित (नियम मानने वाली स्त्री)। सत्त्व पारिभाषिक शब्द (मन, "
           "मानसिक बल); संहनन = शरीर की सुगठित रचना। सन्धि जाँची: सम्पद् + उपेतम् → सम्पदुपेतम्; ज्ञातीनाम् + अग्रगण्यम् → "
           "ज्ञातीनामग्रगण्यम्; जनयति + इति → जनयतीति (इ + इ → ई); छपा ‘भगवान्आत्रेयः’ = भगवान् आत्रेयः।"),
    "26": ("गद्य; विश्वास मध्यम। पाठ-चिह्न: ‘गृत’ कोई शब्द नहीं; ‘घृत’ (घी) सम्भावित सुधार — इस पर प्रश्न नहीं। पलल विवादित: "
           "सम्भवतः तिल-कल्क, ‘मांस’ भी अर्थ। फल अनिर्दिष्ट; मस्तु = दही का पानी। बदर = Ziziphus jujuba (मानक)। "
           "सन्धि जाँची: बदर + उदकेन → बदरोदकेन (अ + उ → ओ); पयस् + दधि → पयोदधि (अस् → ओ घोष से पहले); "
           "युक्तेन + आस्थापयेत् → युक्तेनास्थापयेत् (अ + आ → आ)।"),
}

# ===================================================================== AIDS
AIDS = {
    "14": {
        "chain": {"steps": ["गर्भ का दबाव (उत्पीडन)", "दोष हृदय तक पहुँचते", "दोष जलाते (विदाह)", "तब खुजली (कण्डू)"]},
        "chunks": "गर्भोत्पीडनात्तु | दोषा हृदयं प्राप्य | विदहंति | ततः कंडूर्जायते | कंडूकिकिसं (?)",
        "sandhi": "अ + उ → ओ: गर्भ + उत्पीडनात् → गर्भोत्पीडनात् · आः → आ घोष से पहले: दोषाः + हृदयम् → दोषा हृदयम् · ऊ के बाद विसर्ग → र्: कण्डूः + जायते → कण्डूर्जायते।",
    },
    "15": {
        "frame": "कब (तत्र) → किसका (नवनीतस्य) → कैसा (मधुरौषधसिद्धस्य) → कितना (पाणितलमात्रम्) → किसे (अस्यै) → क्रिया (दद्यात्)।",
        "chunks": "तत्र | कोलोडकेन (?) | नवनीतस्य | मधुरौषधसिद्धस्य | पाणितलमात्रमस्यै | दद्यात्",
        "sandhi": "अ + औ → औ: मधुर + औषध → मधुरौषध · म् + स्वर: पाणितलमात्रम् + अस्यै → पाणितलमात्रमस्यै।",
    },
    "16": {
        "contrast": {"groups": [
            {"label": "कल्क (लेप) से", "items": ["चन्दन (मानक)", "मृणाल, कमलनाल (मानक)"]},
            {"label": "या चूर्ण से", "items": ["शिरीष (मानक)", "धातकी (अनुमानित पाठ)", "सर्षप, सरसों (मानक)",
                                              "मधुक (सम्भवतः मुलेठी)"]}]},
        "chunks": "चंदनमृणालकल्कैश्च | स्तनोदरं | मृद्गीयात् (= मृद्नीयात्?) | शिरीषघातुकीसर्षपमधुकचूर्णैर्वा",
        "sandhi": "विसर्ग + च → श्च: कल्कैः + च → कल्कैश्च · अ + उ → ओ: स्तन + उदरम् → स्तनोदरम् · ऐ के बाद विसर्ग → र्: चूर्णैः + वा → चूर्णैर्वा।",
    },
    "17": {
        "diagram": {"groups": [
            {"label": "पहला विकल्प: कल्क", "items": ["कुटज (कुड़ा) के बीज", "अर्जक के बीज (सम्भवतः तुलसी)", "मुस्ता (नागरमोथा)",
                                                 "हरिद्रा (हल्दी)"]},
            {"label": "या दूसरा विकल्प: कल्क", "items": ["निम्ब (नीम)", "कोल (सम्भवतः बेर)", "सुरसा (सम्भवतः तुलसी)",
                                                    "मञ्जिष्ठा (मजीठ)"]}]},
        "chunks": "कुटजार्जकबीजमुस्ताहरिद्राकल्कैर्वा | निम्बकोळसुरसमंजिष्ठाकल्कैर्वा",
        "sandhi": "अ + अ → आ: कुटज + अर्जक → कुटजार्जक · ऐ के बाद विसर्ग → र्: कल्कैः + वा → कल्कैर्वा।",
    },
    "18": {
        "diagram": {"groups": [
            {"label": "१ जल, पकाया हुआ", "items": ["शश (खरगोश)", "हरिण (हिरन)", "पुनर्नवा", "मालती (विवादित)",
                                              "मधुक (सम्भवतः मुलेठी)"]},
            {"label": "२ त्रिफला", "items": ["पृषत (चित्तीदार हिरन) के रुधिर से युक्त"]},
            {"label": "३ तेल, पकाया हुआ", "items": ["करवीर (कनेर) के पत्तों का कल्क"]}]},
        "chunks": "शशहरिणपुनर्नवामालतीमधुकसिद्धैनांभसा | पृषतरुधिरयुक्तया त्रिफलया | करवीरपत्रकल्कसिद्धेन च | तैलेनाभ्यंगः",
        "sandhi": "अ + अ → आ: तैलेन + अभ्यङ्गः → तैलेनाभ्यङ्गः · नियमित सिद्धेन + अम्भसा → सिद्धेनाम्भसा (छपा ‘सिद्धैनांभसा’, सम्भवतः भूल)।",
    },
    "19": {
        "frame": "क्या (परिषेकः) → फिर (पुनः) → किससे पका (मालतीमधुकसिद्धेन) → किससे (अम्भसा); क्रिया नहीं।",
        "chunks": "परिषेकः | पुनर्मालतीमधुकसिद्धेनांभसा",
        "sandhi": "र् घोष से पहले रहता है: पुनर् + मालती → पुनर्मालती · अ + अ → आ: सिद्धेन + अम्भसा → सिद्धेनाम्भसा।",
    },
    "20": {
        "chunks": "कंडूयनं | वर्जयेत्",
        "frame": "कर्म (कण्डूयनम्) + क्रिया (वर्जयेत्, विधिलिङ्: ‘करना चाहिए’); कर्ता गर्भवती स्त्री, अलिखित।",
        "anchors": "याद-सूत्र: कण्डू (खुजली, कार्ड 14) हो, पर कण्डूयन (खुजलाना) नहीं। (मेरी याद-पद्धति)",
    },
    "21": {
        "chain": {"steps": ["त्वचा फटना (त्वग्भेद)", "कुरूपता से बचाव के लिए", "स्नान, उद्वर्तन, चन्दन का प्रयोग"]},
        "chunks": "त्वग्भेदे | वैरूप्यपरिहारार्थं | स्नानोद्वर्तनं | चंदनं च | शीलयेत्",
        "sandhi": "क् → ग् घोष से पहले: त्वक् + भेदे → त्वग्भेदे · अ + अ → आ: परिहार + अर्थम् → परिहारार्थम् · अ + उ → ओ: स्नान + उद्वर्तनम् → स्नानोद्वर्तनम्।",
    },
    "22": {
        "chunks": "मधुरं चाहारम् | अल्पम् | अल्पस्नेहलवणम् | अल्पोदकानुपानं | भुंजीत",
        "sandhi": "अ + आ → आ: च + आहारम् → चाहारम् · अ + उ → ओ: अल्प + उदक → अल्पोदक · अ + अ → आ: उदक + अनुपानम् → उदकानुपानम्।",
        "frame": "आहार कैसा: मधुर → मात्रा अल्प → स्नेह-लवण अल्प → अनुपान-जल अल्प → क्रिया (भुञ्जीत)।",
    },
    "23": {
        "chain": {"steps": ["आठवाँ (मास)", "घी वाली दूध की यवागू पिए", "आपत्ति: ‘नहीं’ (वक्ता अस्पष्ट)",
                            "कारण: गर्भ को पिंगलता का भय"]},
        "chunks": "अष्टमे | क्षीरयवागूं सर्पिष्मतीं | पिबेत् | नेति | षंढकाथो (?) | गर्भस्य पैंगल्याबाधभयात्",
        "sandhi": "अ + इ → ए: न + इति → नेति।",
    },
    "24": {
        "chunks": "अस्ति | पैंगल्याबाधः | तथापि | एवं | कुर्वीत",
        "sandhi": "विसर्ग → स् त से पहले: आबाधः + तथा → आबाधस्तथा · आ + अ → आ: तथा + अपि → तथापि · इ + ए → ये: अपि + एवम् → अप्येवम्।",
        "frame": "मानना (अस्ति ... आबाधः) → फिर भी (तथापि) → उपदेश वही (एवं कुर्वीत)।",
    },
    "25": {
        "diagram": {"groups": [
            {"label": "सन्तान (अपत्य) कैसी", "items": ["नीरुज (रोग-रहित)", "१ बल", "२ वर्ण", "३ सत्त्व", "४ संहनन",
                                                  "ज्ञातियों में अग्रगण्य"]},
            {"label": "वक्ता", "items": ["भगवान् आत्रेय"]}]},
        "chunks": "नीरुजं | बलवर्णसत्त्वसंहननसंपदुपेतं | ज्ञातीनामग्रगण्यम् | अपत्यं जनयति | इति भगवान् आत्रेयः",
        "sandhi": "द् + स्वर: सम्पद् + उपेतम् → सम्पदुपेतम् · इ + इ → ई: जनयति + इति → जनयतीति · म् + स्वर: ज्ञातीनाम् + अग्रगण्यम् → ज्ञातीनामग्रगण्यम्।",
    },
    "26": {
        "diagram": {"groups": [
            {"label": "आधार", "items": ["बदर (बेर) का जल"]},
            {"label": "युक्त (क्रम से)", "items": ["पलल (विवादित)", "पयः (दूध)", "दधि (दही)", "मस्तु (दही का पानी)", "तैल",
                                                "लवण", "फल", "घृत (सुधार-पाठ)", "मधु"]}]},
        "chunks": "बदरोदकेन | पललपयोदधिमस्तुतैललवणफलगृतमधुयुक्तेन | आस्थापयेत्",
        "sandhi": "अ + उ → ओ: बदर + उदकेन → बदरोदकेन · अस् → ओ घोष से पहले: पयस् + दधि → पयोदधि · अ + आ → आ: युक्तेन + आस्थापयेत् → युक्तेनास्थापयेत्।",
    },
}

# ===================================================================== IMAGE_SPECS
IMAGE_SPECS = {
    ("14", "chain"): {
        "file": "sh3-garbha-pidana-14.svg",
        "alt": ("Flowchart of unit 14: pressure of the embryo, the doṣas reach the heart, they burn, then itching arises."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"गर्भ का दबाव\"] --> B[\"दोष हृदय तक पहुँचते\"]\n"
                 "  B --> C[\"दोष जलाते (विदाह)\"]\n"
                 "  C -->|\"तब\"| D[\"खुजली (कण्डू)\"]\n"),
    },
    ("16", "contrast"): {
        "file": "sh3-kalka-churna-16.svg",
        "alt": ("Two columns for unit 16: pastes (kalka) of sandalwood and lotus stalk; or powders (cūrṇa) of śirīṣa, "
                "dhātakī (conjectural reading), mustard and madhuka (probably licorice), for the breast and belly."),
        "type": "split",
        "title": "स्तन-उदर पर (इकाई १६)",
        "cols": [["कल्क (लेप)", ["चन्दन (मानक)", "मृणाल, कमलनाल (मानक)"]],
                 ["या चूर्ण", ["शिरीष (मानक)", "धातकी (अनुमानित पाठ)", "सरसों (मानक)", "मधुक (सम्भवतः मुलेठी)"]]],
    },
    ("17", "diagram"): {
        "file": "sh3-kalka-vikalpa-17.svg",
        "alt": ("Two columns for unit 17, two alternative paste sets: kuṭaja and arjaka seeds, mustā, haridrā; or nimba, "
                "kola (probable), surasā (probable), mañjiṣṭhā."),
        "type": "split",
        "title": "दो विकल्प, दोनों कल्क (इकाई १७)",
        "cols": [["पहला", ["कुटज के बीज", "अर्जक के बीज (सम्भावित)", "मुस्ता", "हरिद्रा"]],
                 ["या दूसरा", ["निम्ब", "कोल (सम्भावित)", "सुरसा (सम्भावित)", "मञ्जिष्ठा"]]],
    },
    ("18", "diagram"): {
        "file": "sh3-abhyanga-sadhana-18.svg",
        "alt": ("Table of unit 18, the three instruments of one abhyaṅga in the text's order: water cooked with hare, deer "
                "and plants; triphalā mixed with spotted-deer blood; oil cooked with karavīra-leaf paste."),
        "type": "table",
        "title": "अभ्यंग के तीन साधन (इकाई १८)",
        "heads": ["साधन", "किसके साथ"],
        "rows": [["१ जल", "शश, हरिण, पुनर्नवा, मालती (विवादित), मधुक से पका"],
                 ["२ त्रिफला", "पृषत (चित्तीदार हिरन) के रुधिर से युक्त"],
                 ["३ तेल", "करवीर-पत्र के कल्क से पका"]],
    },
    ("21", "chain"): {
        "file": "sh3-tvagbheda-21.svg",
        "alt": ("Flowchart of unit 21: when the skin splits, to avoid disfigurement, she should use bathing, rubbing with "
                "powders (udvartana) and sandalwood."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"त्वचा फटना\"] -->|\"कुरूपता से बचाव हेतु\"| B[\"प्रयोग करे\"]\n"
                 "  B --> C[\"स्नान\"]\n"
                 "  B --> D[\"उद्वर्तन (उबटन)\"]\n"
                 "  B --> E[\"चन्दन\"]\n"),
    },
    ("23", "chain"): {
        "file": "sh3-ashtama-yavagu-23.svg",
        "alt": ("Flowchart of unit 23: in the eighth month she drinks milk gruel with ghee; an objection says not so (speaker "
                "unclear); its reason is fear of a tawny-colour affliction to the embryo."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"आठवाँ मास\"] --> B[\"घी वाली दूध-यवागू पिए\"]\n"
                 "  B --> C[\"आपत्ति: ऐसा नहीं\"]\n"
                 "  C -->|\"कारण\"| D[\"गर्भ को पिंगलता का भय\"]\n"),
    },
    ("25", "diagram"): {
        "file": "sh3-apatya-guna-25.svg",
        "alt": ("Numbered table of unit 25: the child is free of disease, endowed with strength, complexion, sattva and firm "
                "build, and foremost among kinsmen; the speaker is Ātreya."),
        "type": "table",
        "title": "सन्तान कैसी (इकाई २५, आत्रेय का वचन)",
        "heads": ["गुण", "अर्थ"],
        "rows": [["नीरुज", "रोग-रहित"], ["१ बल", "शक्ति"], ["२ वर्ण", "रंग"], ["३ सत्त्व", "मन की शक्ति"],
                 ["४ संहनन", "सुगठित शरीर"], ["अग्रगण्य", "ज्ञातियों में प्रथम"]],
    },
    ("26", "diagram"): {
        "file": "sh3-asthapana-26.svg",
        "alt": ("Table of unit 26: the base is jujube water; joined with palala (disputed), milk, curd, whey, oil, salt, fruit, "
                "ghee (corrected reading) and honey, for an āsthāpana enema."),
        "type": "table",
        "title": "आस्थापन वस्ति (इकाई २६)",
        "heads": ["भाग", "द्रव्य (क्रम से)"],
        "rows": [["आधार", "बदर (बेर) का जल"], ["युक्त", "पलल (विवादित), दूध, दही"],
                 ["युक्त", "मस्तु, तेल, नमक"], ["युक्त", "फल, घृत (सुधार-पाठ), मधु"]],
    },
}
