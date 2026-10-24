from helpers import mcq, match, order, fill, multi, accepts


def T(q, teaches):
    q["teaches"] = teaches
    return q


AUTHORED = {}

# ---------------------------------------------------------------- unit 120
AUTHORED["120"] = {
    "title": "लक्ष्मणावटशुङ्ग... क्षीरेऽभिषुत्य",
    "question": "In unit 120, how are the drops made, how many are instilled, and which nostril goes with the wish for a daughter?",
    "rule": ("Any one of lakṣmaṇā, banyan shoots (वटशुङ्ग), sahadevā or viśvedevā is pounded in milk; she herself instils "
             "three or four drops in a nostril. The left (वामे) goes with one desiring a daughter (दुहितृकामा)."),
    "limits": ("Low confidence. The word after the right nostril (पित्रुना) is damaged; 'desiring a son' for the right is only a "
               "conjectural reading, so no question rests on it. Identities: lakṣmaṇā disputed, banyan shoots standard, sahadevā "
               "probable (Vernonia cinerea), viśvedevā unidentified (the name itself may be viśvadevā). No dose beyond the drops is given."),
    "explain_hi": ("इस गद्य-इकाई में चार द्रव्यों के नाम हैं: लक्ष्मणा (पहचान विवादित), वटशुङ्ग यानी बरगद के अंकुर (मानक), "
                   "सहदेवा (सम्भवतः सहदेई) और विश्वेदेवा (अज्ञात)। इनमें से कोई एक (अन्यतमाम्) दूध में कूटा जाता है (क्षीरे अभिषुत्य)। "
                   "फिर स्त्री स्वयं तीन या चार बूँदें नासिका-छिद्र में डाले। "
                   "‘वामे तु दुहितृकामा’ साफ़ है: बाएँ में, पुत्री की इच्छा वाली। दाहिने छिद्र के साथ जुड़ा शब्द ‘पित्रुना’ क्षतिग्रस्त है; "
                   "वहाँ ‘पुत्र की इच्छा’ केवल अनुमानित पाठ है।"),
    "hook": "चार में से कोई एक, दूध में कूटकर, तीन-चार बूँद; बायाँ = दुहितृकामा।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 120, in what is the chosen plant pounded?",
            ("In milk", "क्षीरे अभिषुत्य: having pounded in milk."),
            [("In water", "Water is not named in this unit."),
             ("In ghee", "Ghee is not named in this unit."),
             ("In honey", "Honey is not named in this unit.")],
            "क्षीरे (in milk) + अभिषुत्य (having pounded).",
            "क्षीरे = in milk."),
        order(1, "Put these phrases of unit 120 in the text's order.",
              ["अन्यतमाम्", "क्षीरे", "अभिषुत्य", "त्रीन् चतुरः वा बिन्दून्", "दक्षिणे नासापुटे", "स्वयम् आसिञ्चेत्"],
              "Any one, in milk, having pounded, three or four drops, in the right nostril, she should herself instil.",
              "अन्यतमाम् → क्षीरे → अभिषुत्य → बिन्दून् → नासापुटे → आसिञ्चेत्."),
        match(2, "Match each word of unit 120 to its meaning.",
              [["अन्यतमाम्", "any one"], ["अभिषुत्य", "having pounded"], ["बिन्दून्", "drops"],
               ["नासापुटे", "in the nostril"], ["दुहितृकामा", "desiring a daughter"]],
              "These five words carry the sure part of the procedure.",
              "अन्यतमा, अभिषुत्य, बिन्दु, नासापुट, दुहितृकामा.", role="extend",
              teaches="With a prefix, 'having done' ends in -य, and in -त्य after a short root vowel: अभि + सु → अभिषुत्य."),
        mcq("discriminate", 3, "By unit 120, in which nostril does one desiring a daughter instil the drops?",
            ("The left one", "वामे तु दुहितृकामा: in the left, desiring a daughter."),
            [("The right one", "दक्षिणे is the right; the daughter goes with वामे, the left."),
             ("Both, one after the other", "The text names a single nostril for the daughter."),
             ("Neither; she drinks them", "The drops are instilled (आसिञ्चेत्) into the nose.")],
            "वाम = left; the left nostril goes with दुहितृकामा.",
            "वामे तु दुहितृकामा = in the left, desiring a daughter."),
        mcq("apply", 4, "Which plant name of unit 120 does the card identify with the label standard?",
            ("वटशुङ्ग: banyan shoots", "Banyan shoots, Ficus benghalensis, are labelled standard."),
            [("लक्ष्मणा", "Its identity is labelled disputed."),
             ("सहदेवा", "Vernonia cinerea is labelled probable only."),
             ("विश्वेदेवा", "This name is left unidentified.")],
            "Only वटशुङ्ग (banyan shoots) carries the label standard.",
            "वटशुङ्ग = banyan shoots (standard)."),
        mcq("transfer", 5, "By the rule of अभिषुत्य, which form means having conquered, from वि + √जि?",
            ("विजित्य", "Prefix + short root vowel: -त्य, as अभि + सु → अभिषुत्य."),
            [("विजित्वा", "With a prefix the -त्वा ending is not used."),
             ("विजीय", "A short root vowel takes -त्य, not a lengthened vowel + -य."),
             ("विजेय", "That is a different form: to be conquered.")],
            "वि + जि + त्य = विजित्य, like अभि + सु + त्य = अभिषुत्य.",
            "Prefixed root: -य; after a short root vowel: -त्य.",
            teaches="A prefixed root makes 'having done' with -य, and with -त्य when the root ends in a short vowel."),
    ],
}

# ---------------------------------------------------------------- unit 121
AUTHORED["121"] = {
    "title": "न चैतान्निष्ठीवेत्",
    "question": "What does unit 121 forbid, and what do 'these' most likely refer to?",
    "rule": ("न च एतान् निष्ठीवेत्: and she should not spit these out. एतान् (masculine accusative plural) most likely means "
             "the drops (बिन्दून्) of unit 120."),
    "limits": ("A four-word line. The subject is not named; the woman of unit 120 is understood. That एतान् means the drops is the "
               "most likely reading, not stated in the line."),
    "explain_hi": ("यह छोटी पंक्ति एक निषेध है: ‘और इन्हें थूके नहीं।’ "
                   "‘निष्ठीवेत्’ विधिलिङ् है (थूके); ‘न’ के साथ इसका अर्थ है ‘न थूके’। "
                   "‘एतान्’ पुंलिंग द्वितीया बहुवचन है, जो पिछली इकाई की ‘बिन्दून्’ (बूँदें, पुंलिंग द्वितीया बहुवचन) से मेल खाता है; "
                   "इसलिए सबसे सम्भावित अर्थ है: वे बूँदें। कर्ता वही स्त्री है।"),
    "hook": "बूँदें डालीं, अब थूके नहीं: न चैतान् निष्ठीवेत्।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What does unit 121 tell her not to do?",
            ("Spit these out", "न ... निष्ठीवेत्: she should not spit (these) out."),
            [("Swallow these", "The verb is निष्ठीवेत्, spit out, not swallow."),
             ("Speak aloud", "No speaking is named in this line."),
             ("Lie down", "No lying down is named in this line.")],
            "निष्ठीवेत् = should spit out; न makes it a prohibition.",
            "न + निष्ठीवेत् = should not spit out."),
        order(1, "Put the words of unit 121 in the line's order.",
              ["न", "च", "एतान्", "निष्ठीवेत्"],
              "Not, and, these, should spit out.",
              "न → च → एतान् → निष्ठीवेत्."),
        match(2, "Match each word of unit 121 to its meaning.",
              [["न", "not"], ["च", "and"], ["एतान्", "these"], ["निष्ठीवेत्", "should spit out"]],
              "Four words make the whole line.",
              "न, च, एतान्, निष्ठीवेत्.", role="extend",
              teaches="न with an optative (-एत्) gives a prohibition: should not."),
        mcq("discriminate", 3, "Which split of चैतान् is right?",
            ("च + एतान्", "अ + ए → ऐ: च + एतान् = चैतान्."),
            [("च + इतान्", "अ + इ would give ए (चेतान्), not ऐ."),
             ("चै + तान्", "चै is not a word of the card."),
             ("चे + तान्", "चे is not a word of the card.")],
            "च (and) + एतान् (these): अ + ए joins as ऐ.",
            "अ + ए → ऐ."),
        mcq("apply", 4, "एतान् is masculine accusative plural. What does it most likely refer to, by the card?",
            ("The drops (बिन्दून्) of unit 120", "बिन्दून् is also masculine accusative plural."),
            [("The milk (क्षीर) of unit 120", "क्षीर is neuter singular."),
             ("The herbs (ओषधी) of unit 128", "ओषधी is feminine and comes later."),
             ("The old women of unit 127", "वृद्धस्त्रियः is feminine and comes later.")],
            "एतान् matches बिन्दून् in gender, case and number.",
            "एतान् (m. acc. pl.) ↔ बिन्दून् (m. acc. pl.)."),
        mcq("transfer", 5, "Built like न ... निष्ठीवेत्, what does the invented line न पिबेत् mean?",
            ("One should not drink", "न + optative = should not."),
            [("He does not drink", "That present would be न पिबति."),
             ("He did not drink", "That past would be न अपिबत्."),
             ("One should drink", "न negates the verb.")],
            "पिबेत् = should drink; with न, should not drink.",
            "न + optative = prohibition.",
            teaches="An optative verb (-एत्) with न forbids: न निष्ठीवेत् = should not spit out."),
    ],
}

# ---------------------------------------------------------------- unit 122
AUTHORED["122"] = {
    "title": "पुष्योद्धृतायाः श्वेतबृहत्याः",
    "question": "In unit 122, which plant and which part are used, when is it uprooted, and how is it given?",
    "rule": ("Likewise: from the root-paste of white bṛhatī, uprooted under Puṣya, one should instil the juice into the nose "
             "(नावयेत्)."),
    "limits": ("The subject is not stated (the card says 'one'). White bṛhatī is a white form of a Solanum, identity disputed "
               "(bṛhatī in general is probably Solanum indicum). No quantity is given."),
    "explain_hi": ("‘तथा’ (वैसे ही) से पिछले नस्य-प्रयोग से जोड़ा गया है। "
                   "द्रव्य है श्वेत बृहती, जिसे पुष्य नक्षत्र में उखाड़ा गया हो (पुष्योद्धृता); इसकी पहचान विवादित है "
                   "(बृहती सामान्यतः सम्भवतः Solanum indicum)। "
                   "क्रम: जड़ → लुगदी (कल्क) → उससे रस → नाक में डालना (नावयेत्)। "
                   "‘मूलकल्कात्’ पञ्चमी है: ‘जड़ की लुगदी से’। कर्ता नहीं कहा गया, मात्रा भी नहीं।"),
    "hook": "पुष्य में उखाड़ी श्वेत बृहती: जड़ → कल्क → रस → नस्य।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 122, which part of the white bṛhatī is used?",
            ("The root", "मूलकल्कात्: from the root-paste."),
            [("The leaf", "No leaf is named in this unit."),
             ("The flower", "No flower is named in this unit."),
             ("The fruit", "No fruit is named in this unit.")],
            "मूल = root; its paste (कल्क) gives the juice.",
            "मूलकल्क = root-paste."),
        order(1, "Put the words of unit 122 in the line's order.",
              ["तथा", "पुष्योद्धृतायाः", "श्वेतबृहत्याः", "मूलकल्कात्", "रसम्", "नावयेत्"],
              "Likewise, uprooted under Puṣya, of white bṛhatī, from the root-paste, the juice, should instil into the nose.",
              "तथा → पुष्योद्धृतायाः → श्वेतबृहत्याः → मूलकल्कात् → रसम् → नावयेत्."),
        match(2, "Match each word of unit 122 to its meaning.",
              [["तथा", "likewise"], ["पुष्योद्धृता", "uprooted under Puṣya"], ["मूलकल्क", "root-paste"],
               ["रस", "juice"], ["नावयेत्", "should instil into the nose"]],
              "Five words give the whole procedure.",
              "तथा, पुष्योद्धृता, मूलकल्क, रस, नावयेत्.", role="extend",
              teaches="-आत् on an a-stem is the ablative, from: मूलकल्कात् = from the root-paste."),
        mcq("discriminate", 3, "Which split of पुष्योद्धृतायाः is right?",
            ("पुष्य + उद्धृतायाः", "अ + उ → ओ: पुष्य + उद्धृता = पुष्योद्धृता."),
            [("पुष्यो + द्धृतायाः", "Neither part is a word of the card."),
             ("पुष्य + ओद्धृतायाः", "The ओ is the joined sound, not part of the second word."),
             ("पुष्यस् + धृतायाः", "There is no such split in the card.")],
            "पुष्य (the lunar mansion) + उद्धृता (uprooted): अ + उ joins as ओ.",
            "अ + उ → ओ."),
        mcq("apply", 4, "How does the card label the identity of श्वेत बृहती, white bṛhatī?",
            ("Disputed: a white form of a Solanum", "The white form is labelled disputed."),
            [("Standard: Ficus benghalensis", "That is the banyan of unit 120."),
             ("Probable: Vernonia cinerea", "That is sahadevā of unit 120."),
             ("Unidentified: no genus is given", "The card does name the genus Solanum.")],
            "White bṛhatī: a white form of a Solanum, identity disputed.",
            "श्वेतबृहती = disputed (a Solanum)."),
        mcq("transfer", 5, "Built like मूलकल्कात् रसम्, what does the invented phrase पुष्पात् रसम् mean?",
            ("Juice from the flower", "-आत् is the ablative, from."),
            [("Juice for the flower", "For would be the dative पुष्पाय."),
             ("Juice in the flower", "In would be the locative पुष्पे."),
             ("Juice with the flower", "With would be the instrumental पुष्पेण.")],
            "पुष्पात् = from the flower, like मूलकल्कात् = from the root-paste.",
            "a-stem ablative singular: -आत् = from.",
            teaches="An a-stem in -आत् is ablative: from. मूलकल्कात् रसम् = juice from the root-paste."),
    ],
}

# ---------------------------------------------------------------- unit 123
AUTHORED["123"] = {
    "title": "तद्वच्चोत्पलपत्रं कुमुदपत्रम्",
    "question": "Which plant parts does unit 123 name for nasal use, and what does it leave unsaid?",
    "rule": ("Likewise: a leaf (or petal) of utpala, a leaf of kumuda, the root of lakṣmaṇā and banyan shoots; and one should "
             "instil into the nose (नावयेत्)."),
    "limits": ("Elliptical: no preparation and no object of नावयेत् are stated, and the card supplies none. 'Eight' is read with "
               "the banyan shoots, but the printed order is not fully clear. utpala and kumuda are water lilies, probable only. "
               "The print तद्वचो- probably lost one च (तद्वच्चो-)."),
    "explain_hi": ("‘तद्वत्’ यानी ‘वैसे ही’: पिछली इकाई के नस्य की तरह। "
                   "चार द्रव्य: उत्पल का पत्र (सम्भवतः नीला कमल), कुमुद का पत्र (सम्भवतः रात में खिलने वाला कमल), लक्ष्मणा की जड़, "
                   "और वट के अंकुर (‘आठ’ इन्हीं से जोड़ा गया, पर छपा क्रम पूरी तरह साफ़ नहीं)। "
                   "कमल-जातीय पौधों में ‘पत्र’ का अर्थ पंखुड़ी भी हो सकता है। "
                   "इन्हें कैसे तैयार करें, यह इकाई नहीं कहती; केवल ‘नावयेत्’ (नाक में डाले) है।"),
    "hook": "उत्पल-पत्र, कुमुद-पत्र, लक्ष्मणा-मूल, वट-शुङ्ग: फिर नस्य; विधि नहीं कही।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 123, which part of lakṣmaṇā is named?",
            ("Its root", "लक्ष्मणामूलम्: the root of lakṣmaṇā."),
            [("Its leaf", "The leaves named are of utpala and kumuda."),
             ("Its shoots", "The shoots named are of the banyan."),
             ("Its flower", "No flower of lakṣmaṇā is named.")],
            "लक्ष्मणा + मूल = the root of lakṣmaṇā.",
            "लक्ष्मणामूलम् = root of lakṣmaṇā."),
        order(1, "Put the four plant items of unit 123 in the text's order.",
              ["उत्पलपत्रम्", "कुमुदपत्रम्", "लक्ष्मणामूलम्", "वटशुङ्गानि"],
              "Utpala leaf, kumuda leaf, lakṣmaṇā root, banyan shoots.",
              "उत्पल → कुमुद → लक्ष्मणा → वट."),
        match(2, "Match each item of unit 123 to its meaning on the card.",
              [["उत्पल", "probably blue water lily"], ["कुमुद", "probably night water lily"],
               ["लक्ष्मणामूल", "root of lakṣmaṇā"], ["वटशुङ्गानि", "banyan shoots"],
               ["नावयेत्", "should instil into the nose"]],
              "The two lilies are probable identifications only.",
              "उत्पल, कुमुद, लक्ष्मणामूल, वटशुङ्ग, नावयेत्.", role="extend",
              teaches="पत्र = leaf; for lotus plants it can also mean petal."),
        mcq("discriminate", 3, "What does unit 123 state about how these items are prepared?",
            ("Nothing: no preparation is named", "The unit gives only the items and नावयेत्."),
            [("They are pounded in milk", "Pounding in milk is in unit 120."),
             ("A root-paste is made and juiced", "Paste and juice are in unit 122."),
             ("They are cooked in ghee", "No ghee is named in this unit.")],
            "The unit is elliptical: items, then 'should instil into the nose'.",
            "No preparation is stated in unit 123."),
        multi("apply", 4, "Which items does unit 123 name?",
              [("A leaf of utpala", "Right: उत्पलपत्रम्."),
               ("The root of lakṣmaṇā", "Right: लक्ष्मणामूलम्."),
               ("Banyan shoots", "Right: वटशुङ्गानि."),
               ("The root of white bṛhatī", "That is unit 122."),
               ("Apāmārga", "That is named in unit 125.")],
              [0, 1, 2],
              "utpala leaf, kumuda leaf, lakṣmaṇā root and banyan shoots are named.",
              "उत्पलपत्र, कुमुदपत्र, लक्ष्मणामूल, वटशुङ्ग."),
        mcq("transfer", 5, "The card says तद्वत् + च should join as तद्वच्च. By that rule, how is तत् + च written?",
            ("तच्च", "त् before च becomes च्: तत् + च = तच्च."),
            [("तद्च", "त् turns to द् before voiced sounds; च is not voiced."),
             ("तन्च", "No nasal comes in before च."),
             ("तत्च", "त् does not stay unchanged before च.")],
            "तत् + च = तच्च, as तद्वत् + च = तद्वच्च.",
            "त् + च → च्च.",
            teaches="A final त् before च becomes च्: तद्वत् + च → तद्वच्च, तत् + च → तच्च."),
    ],
}

# ---------------------------------------------------------------- unit 124
AUTHORED["124"] = {
    "title": "शुक्लमाल्याम्बरधरा च नारी",
    "question": "In unit 124, what does the woman wear, what does she drink, with what, in what measure, and why?",
    "rule": ("A woman in white garlands and garments should drink with milk a root-paste of lakṣmaṇā uprooted under Puṣya, "
             "of the measure of an udumbara, for the birth (उत्पादाय) and the stability (स्थितये) of a son."),
    "limits": ("उदुम्बरमात्र says only 'the measure of an udumbara' (Ficus racemosa, standard); the fruit's size is the usual "
               "reading, and no weight is given. पयस् can mean milk or water; milk is taken. lakṣmaṇā remains disputed."),
    "explain_hi": ("श्वेत माला और वस्त्र पहनने वाली स्त्री (शुक्लमाल्याम्बरधरा) पुष्य नक्षत्र में उखाड़ी लक्ष्मणा की जड़ की लुगदी पिए। "
                   "मात्रा: उदुम्बर (गूलर, Ficus racemosa, मानक) के बराबर; सामान्य पठन फल के आकार का है, पर पाठ केवल ‘उदुम्बर-मात्र’ कहता है। "
                   "साथ में ‘पयसा’, दूध से (पयस् का अर्थ जल भी हो सकता है)। "
                   "उद्देश्य दो हैं, दोनों चतुर्थी में: ‘उत्पादाय’ (उत्पत्ति के लिए) और ‘स्थितये’ (स्थिति के लिए)। "
                   "‘पुत्रस्योत्पादाय’ में अ + उ → ओ की सन्धि है।"),
    "hook": "श्वेत वस्त्र, लक्ष्मणा-मूल, गूलर-भर, दूध से: पुत्र की उत्पत्ति और स्थिति के लिए।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 124, what does the woman wear?",
            ("White garlands and garments", "शुक्ल-माल्य-अम्बर-धरा: wearing white garlands and garments."),
            [("Red garlands and garments", "The colour named is शुक्ल, white."),
             ("Yellow garments only", "The colour named is शुक्ल, white."),
             ("A garland of banyan shoots", "No such garland is named.")],
            "शुक्ल = white; माल्य = garland; अम्बर = garment; धरा = wearing.",
            "शुक्लमाल्याम्बरधरा = wearing white garlands and garments."),
        order(1, "Put these words of unit 124 in the text's order.",
              ["शुक्लमाल्याम्बरधरा", "लक्ष्मणायाः", "मूलकल्कम्", "उदुम्बरमात्रम्", "पिबेत्", "स्थितये"],
              "Wearing white, of lakṣmaṇā, root-paste, udumbara-measure, should drink, for stability.",
              "वस्त्र → द्रव्य → रूप → मात्रा → क्रिया → उद्देश्य."),
        match(2, "Match each word of unit 124 to its meaning.",
              [["नारी", "woman"], ["उदुम्बरमात्रम्", "of the measure of an udumbara"], ["पिबेत्", "should drink"],
               ["उत्पादाय", "for the birth"], ["स्थितये", "for the stability"]],
              "Two datives give the two purposes.",
              "नारी, उदुम्बरमात्र, पिबेत्, उत्पादाय, स्थितये.", role="extend",
              teaches="A dative can give the purpose: उत्पादाय = for the birth, स्थितये = for the stability."),
        mcq("discriminate", 3, "What does the card say उदुम्बरमात्र means?",
            ("As much as an udumbara, used as a measure", "मात्र = measure; the text gives no weight."),
            [("Mixed with juice of the udumbara", "No udumbara juice is named."),
             ("Taken while sitting under an udumbara", "The word gives a measure, not a place."),
             ("One fixed weight stated in the text", "No weight is stated; only the measure of an udumbara.")],
            "उदुम्बरमात्रम् = of the measure of an udumbara (cluster fig).",
            "-मात्र after a thing = as much as that thing."),
        multi("apply", 4, "For which purposes does unit 124 say she drinks it?",
              [("For the birth of a son", "Right: पुत्रस्य उत्पादाय."),
               ("For the stability of the son", "Right: स्थितये."),
               ("For the birth of a daughter", "The text says पुत्रस्य, of a son."),
               ("For relief of a fever", "No illness is named here.")],
              [0, 1],
              "Two datives: उत्पादाय (birth) and स्थितये (stability), both of a son.",
              "पुत्रस्योत्पादाय स्थितये च."),
        mcq("transfer", 5, "Built like उत्पादाय, which invented form says for health, from आरोग्य (neuter a-stem)?",
            ("आरोग्याय", "a-stem dative: -आय, like उत्पादाय."),
            [("आरोग्यस्य", "That is the genitive: of health."),
             ("आरोग्येण", "That is the instrumental: by health."),
             ("आरोग्ये", "That is the locative: in health.")],
            "आरोग्य + -आय = आरोग्याय, for health.",
            "a-stem dative singular: -आय = for.",
            teaches="The dative of an a-stem ends in -आय and can state a purpose: उत्पादाय = for the birth."),
    ],
}

# ---------------------------------------------------------------- unit 125
AUTHORED["125"] = {
    "title": "तद्वदपामार्गं जीवकऋषभकौ",
    "question": "Which drugs does the list of unit 125 name, and how sure is each identification?",
    "rule": ("Likewise: a list of drugs with apāmārga (Achyranthes aspera, standard), jīvaka and ṛṣabhaka (disputed), "
             "śaṅkhapuṣpī (disputed), a middle stalk, sahacara (probable), and others; or eight banyan shoots."),
    "limits": ("Low confidence. वौरदण्ड and नम्रजीव are unclear and neither split nor identified. अग्नित्जिह्वा is read as "
               "अग्निजिह्वा (probably Gloriosa superba) and वावा as one वा, both flagged. Whether the middle stalk belongs to "
               "śaṅkhapuṣpī is not decided. No verb or preparation: the use comes from the units around it."),
    "explain_hi": ("यह केवल द्रव्यों की सूची है; क्रिया और विधि आस-पास की इकाइयों से आती है (अगली इकाई में पीसना, पकाना, नस्य)। "
                   "निश्चित नाम: अपामार्ग (चिचड़ा, मानक), जीवक और ऋषभक (दो द्रव्य, पहचान विवादित), शंखपुष्पी (पहचान विवादित), "
                   "मध्यदण्ड (बीच का डंठल), सहचर (सम्भवतः कटसरैया)। "
                   "‘वौरदण्ड’ और ‘नम्रजीव’ अस्पष्ट हैं; ‘अग्निजिह्वा’ (सम्भवतः कलिहारी) एक सुधरा पाठ है। "
                   "अन्त में ‘या आठ वट-अंकुर’ का विकल्प है।"),
    "hook": "अपामार्ग, जीवक-ऋषभक, शंखपुष्पी, सहचर ... या आठ वट-अंकुर।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "Which identification does the card give apāmārga, with the label standard?",
            ("Achyranthes aspera", "apāmārga = Achyranthes aspera (prickly chaff-flower), standard."),
            [("Ficus racemosa", "That is udumbara of unit 124."),
             ("Vernonia cinerea", "That is sahadevā of unit 120."),
             ("Ficus benghalensis", "That is the banyan (वट).")],
            "अपामार्ग = Achyranthes aspera (standard; Hindi चिचड़ा).",
            "अपामार्ग = Achyranthes aspera."),
        order(1, "Put these sure items of unit 125 in the list's order.",
              ["अपामार्गम्", "जीवक-ऋषभकौ", "शङ्खपुष्पीम्", "सहचरम्", "वटशुङ्गानि"],
              "Apāmārga, jīvaka and ṛṣabhaka, śaṅkhapuṣpī, sahacara, and last the banyan shoots.",
              "अपामार्ग → जीवक-ऋषभक → शङ्खपुष्पी → सहचर → वटशुङ्ग."),
        match(2, "Match each drug of unit 125 to the card's identification and label.",
              [["अपामार्ग", "standard: Achyranthes aspera"], ["सहचर", "probable: Barleria prionitis"],
               ["शङ्खपुष्पी", "disputed: commonly Convolvulus pluricaulis"],
               ["जीवक, ऋषभक", "two drug names, identity disputed"]],
              "Each identification keeps its own label of certainty.",
              "standard, probable, disputed: as the card gives them.", role="extend",
              teaches="A plant name keeps the certainty the data gives it: standard, probable, disputed or unidentified."),
        mcq("discriminate", 3, "What does the card do with वौरदण्ड and नम्रजीव?",
            ("Leaves them unclear, not split or identified", "Both are unclear in print."),
            [("Identifies both as banyan parts", "No such identification is given."),
             ("Identifies them as Gloriosa superba", "That probable name belongs to अग्निजिह्वा."),
             ("Reads them as one word for apāmārga", "apāmārga is a separate, clear word.")],
            "Two words of the list stay unclear; nothing is built on them.",
            "वौरदण्ड, नम्रजीव = unclear."),
        mcq("apply", 4, "Why does जीवक-ऋषभकौ end in -औ, by the card?",
            ("It joins two drug names: a dual", "Labelled dvandva, masculine accusative dual."),
            [("It names one drug with two parts", "The card names two drugs, jīvaka and ṛṣabhaka."),
             ("It is a locative: in jīvaka", "The card labels it accusative dual."),
             ("It is a plural of three or more", "The plural would end in -आन्.")],
            "जीवक + ऋषभक, two names, joined as a dual compound.",
            "Two a-stem names in a dvandva: -औ (dual)."),
        mcq("transfer", 5, "Like जीवक-ऋषभकौ, which invented compound means Rāma and Kṛṣṇa, the two of them?",
            ("रामकृष्णौ", "Two names in a dvandva take the dual -औ."),
            [("रामकृष्णः", "That singular names one person."),
             ("रामकृष्णाः", "That plural means three or more."),
             ("रामकृष्णम्", "That is an accusative singular.")],
            "Two masculine a-stem names joined: रामकृष्णौ.",
            "Dvandva of two a-stems: -औ.",
            teaches="Two names joined as 'X and Y' (dvandva) take the dual: जीवक + ऋषभक → जीवक-ऋषभकौ."),
    ],
}

# ---------------------------------------------------------------- unit 126
AUTHORED["126"] = {
    "title": "पिष्टस्य च पच्यमानस्य",
    "question": "In unit 126, what is done with the ground drugs, and where is the woman when the juice is instilled?",
    "rule": ("Having smelled the vapour of what is ground and being cooked, one should instil its juice, as before, into her "
             "standing on the threshold (देहल्यां स्थिताम्)."),
    "limits": ("Elliptical: what is ground is not named (the drugs of unit 125 are understood), and the text does not say who "
               "smells the vapour, the woman or the person instilling. स्थिताम् (feminine) points to the woman. 'As before' "
               "refers to the nasal use of unit 120 onward."),
    "explain_hi": ("इकाई 125 के द्रव्य पीसे जाते और पकाए जाते हैं (पिष्टस्य, पच्यमानस्य)। "
                   "उनकी भाप (ऊष्माणम्) सूँघकर (आघ्राय), उनका रस (तद्रसम्) देहली पर खड़ी स्त्री को पहले की तरह (पूर्ववत्) नाक में डाला जाता है। "
                   "भाप कौन सूँघता है, पाठ नहीं कहता। ‘स्थिताम्’ स्त्रीलिंग द्वितीया है, इसलिए खड़ी वाली स्त्री है। "
                   "‘पच्यमान’ कर्मवाच्य वर्तमान कृदन्त है: ‘पकाया जा रहा’।"),
    "hook": "पीसो, पकाओ, भाप सूँघो, रस डालो: देहली पर खड़ी स्त्री को।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 126, where is the woman standing when the juice is instilled?",
            ("On the threshold", "देहल्यां स्थिताम्: standing on the threshold."),
            [("Beside the fire", "No fire place is named for her."),
             ("In the bath", "Bathing is not named in this unit."),
             ("Under a banyan tree", "No tree is named as a place.")],
            "देहली = threshold; स्थिता = standing.",
            "देहल्यां स्थिताम् = standing on the threshold."),
        order(1, "Put these steps of unit 126 in the text's order.",
              ["पिष्टस्य", "पच्यमानस्य", "ऊष्माणम् आघ्राय", "तद्रसम्", "पूर्ववत् नावयेत्"],
              "Ground, being cooked, its vapour smelled, its juice, instilled as before.",
              "पीसना → पकना → भाप सूँघना → रस → नस्य."),
        match(2, "Match each word of unit 126 to its meaning.",
              [["पिष्ट", "ground"], ["पच्यमान", "being cooked"], ["ऊष्माणम्", "vapour"],
               ["देहली", "threshold"], ["पूर्ववत्", "as before"]],
              "These five words carry the procedure and the place.",
              "पिष्ट, पच्यमान, ऊष्मन्, देहली, पूर्ववत्.", role="extend",
              teaches="-यमान on a root gives a passive present participle: पच्यमान = being cooked."),
        mcq("discriminate", 3, "By the card, who smells the vapour in unit 126?",
            ("The text does not say", "The subject of आघ्राय is not stated."),
            [("The husband, named here", "No husband is named in this unit."),
             ("The physician, named here", "No physician is named in this unit."),
             ("The brāhmaṇas, named here", "Brāhmaṇas are named in unit 127, not here.")],
            "The card leaves the smeller open: the woman or the person instilling.",
            "आघ्राय has no stated subject."),
        mcq("apply", 4, "Which split of पूर्ववन्नावयेत् is right?",
            ("पूर्ववत् + नावयेत्", "त् before the nasal न is written न्: पूर्ववन्नावयेत्."),
            [("पूर्ववन् + नावयेत्", "पूर्ववन् is not a word; it is पूर्ववत्."),
             ("पूर्ववत् + आवयेत्", "The verb is नावयेत्, with न."),
             ("पूर्व + वन्नावयेत्", "वन्नावयेत् is not a word.")],
            "पूर्ववत् (as before) + नावयेत् (should instil into the nose).",
            "त् before न here shows as न्."),
        mcq("transfer", 5, "Built like पूर्ववत् (as before), what does the invented line मातृवत् रक्षेत् mean?",
            ("One should protect like a mother", "-वत् = like."),
            [("One should protect the mother", "That would be मातरं रक्षेत्."),
             ("One should protect for the mother", "That would use the dative मात्रे."),
             ("One protected like a mother", "रक्षेत् is an optative, should.")],
            "मातृवत् = like a mother, as पूर्ववत् = as before.",
            "-वत् added to a word = like it.",
            teaches="The indeclinable -वत् means 'like': पूर्ववत् = as before, मातृवत् = like a mother."),
    ],
}

# ---------------------------------------------------------------- unit 127
AUTHORED["127"] = {
    "title": "यच्चान्यदपि ब्राह्मणा वृद्धस्त्रियो वा",
    "question": "Whose further advice does unit 127 tell her to follow?",
    "rule": ("Whatever else (यत् ... अन्यत् अपि) the brāhmaṇas or old women may say, that too (तत् च) she should do (कुर्यात्)."),
    "limits": ("Nothing is added about what they may say. The subject of कुर्यात् is not stated; the woman of the previous units "
               "is understood."),
    "explain_hi": ("यह इकाई प्रयोगों की सूची को खुला छोड़ती है: ‘जो कुछ और भी ब्राह्मण या वृद्ध स्त्रियाँ कहें, वह भी करे।’ "
                   "‘यत् ... तत्’ का जोड़ा है: जो ... वह। "
                   "क्या कहें, यह नहीं बताया गया। ‘कुर्यात्’ विधिलिङ् है: करे। "
                   "‘यच्चान्यदपि’ में तीन सन्धियाँ हैं: त् + च → च्च, अ + अ → आ, त् + अ → द।"),
    "hook": "जो ब्राह्मण या वृद्ध स्त्रियाँ कहें, वह भी करे: यत् ... तत्।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 127, whose further advice should also be followed?",
            ("Brāhmaṇas or old women", "ब्राह्मणाः वृद्धस्त्रियः वा."),
            [("The king's officers", "No king is named."),
             ("The physician only", "No physician is named here."),
             ("The husband's father", "No such person is named.")],
            "ब्राह्मणाः (brāhmaṇas) or वृद्धस्त्रियः (old women).",
            "ब्राह्मणाः वृद्धस्त्रियो वा."),
        order(1, "Put these parts of unit 127 in the line's order.",
              ["यच्चान्यदपि", "ब्राह्मणाः", "वृद्धस्त्रियः", "तच्च कुर्यात्"],
              "Whatever else also, brāhmaṇas, old women, that too she should do.",
              "यच्चान्यदपि → ब्राह्मणाः → वृद्धस्त्रियः → तच्च कुर्यात्."),
        match(2, "Match each word of unit 127 to its meaning.",
              [["यत्", "what(ever)"], ["अन्यत्", "else"], ["अपि", "also"],
               ["वृद्धस्त्रियः", "old women"], ["कुर्यात्", "should do"]],
              "यत् is picked up by तत् (that) before the verb.",
              "यत्, अन्यत्, अपि, वृद्धस्त्रियः, कुर्यात्.", role="extend",
              teaches="यत् ... तत् is a pair: whatever ..., that."),
        mcq("discriminate", 3, "Which split of यच्चान्यदपि is right?",
            ("यत् + च + अन्यत् + अपि", "त् + च → च्च; अ + अ → आ; त् → द् before अ."),
            [("यच् + चान्यत् + अपि", "चान्यत् is not a word."),
             ("यत् + चान् + यदपि", "चान् and यदपि are not words here."),
             ("यत् + च + अन्य + दपि", "दपि is not a word.")],
            "यत् (what) + च (and) + अन्यत् (else) + अपि (also).",
            "त् + च → च्च; अ + अ → आ; त् + vowel → द्."),
        mcq("apply", 4, "What does unit 127 say about the content of their advice?",
            ("Nothing; it is left open", "The card adds nothing about what they may say."),
            [("It must be a mantra", "No mantra is named here."),
             ("It must be a diet rule", "No diet is named here."),
             ("It must be written down", "Nothing of the kind is said.")],
            "Whatever they say is to be done; its content is not given.",
            "यत् ... तत् च कुर्यात्: open-ended."),
        mcq("transfer", 5, "Built like unit 127, what does the invented line यद् गुरुर्वदेत् तत् कुर्यात् mean?",
            ("Whatever the teacher may say, one should do that", "यत् ... तत्: whatever ..., that."),
            [("The teacher should do whatever one says", "गुरुः is the subject of वदेत्, the one who says."),
             ("Whatever the teacher said, one did that", "वदेत् and कुर्यात् are optatives, not past."),
             ("One should speak before the teacher acts", "The teacher is the speaker here.")],
            "यद् ... तत्: whatever the teacher may say, that one should do.",
            "यत् ... तत् = whatever ..., that.",
            teaches="A clause with यत् (whatever) is picked up by तत् (that): यत् ... ब्रूयुः, तत् च कुर्यात्."),
    ],
}

# ---------------------------------------------------------------- unit 128
AUTHORED["128"] = {
    "title": "ततः प्रजास्थापनाख्या महौषधीः",
    "question": "In unit 128, which group of herbs is named, and how should she bear them?",
    "rule": ("Then she should bear (धारयेत) the great herbs called prajāsthāpana (offspring-establishing) with the head and "
             "with the right hand."),
    "limits": ("The herbs of the prajāsthāpana group are not listed here, so none is identified (Caraka names such a group; "
               "this text does not list it). The printed -नारख्या has a stray र (read -नाख्याः). Carrying on the head and "
               "holding in the right hand is the plain sense of the two instrumentals."),
    "explain_hi": ("‘ततः’ (फिर) के बाद एक नया चरण: ‘प्रजास्थापन’ (सन्तान को स्थिर करने वाली) नाम की महा-औषधियाँ। "
                   "इन्हें सिर से (शिरसा) और दाहिने हाथ से (दक्षिणेन पाणिना) धारण करे (धारयेत)। "
                   "‘शिरसा’ और ‘पाणिना’ तृतीया हैं: ‘से’। "
                   "समूह के सदस्य यहाँ नहीं गिनाए गए, इसलिए कोई पहचान नहीं दी गई। "
                   "‘महौषधीः’ में महा + ओषधीः है (आ + ओ → औ)।"),
    "hook": "प्रजास्थापन महौषधियाँ: सिर पर और दाहिने हाथ में।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 128, with what should she bear the great herbs?",
            ("With the head and the right hand", "शिरसा दक्षिणेन च पाणिना."),
            [("With the left hand and the neck", "The hand named is the right (दक्षिण)."),
             ("Around the waist", "No waist is named."),
             ("With both hands only", "The head and the right hand are named.")],
            "शिरसा (with the head) and दक्षिणेन पाणिना (with the right hand).",
            "शिरसा, दक्षिणेन पाणिना."),
        order(1, "Put these words of unit 128 in the line's order.",
              ["ततः", "महौषधीः", "शिरसा", "दक्षिणेन पाणिना", "धारयेत"],
              "Then, the great herbs, with the head, with the right hand, she should bear.",
              "ततः → महौषधीः → शिरसा → दक्षिणेन पाणिना → धारयेत."),
        match(2, "Match each word of unit 128 to its meaning.",
              [["ततः", "then"], ["महौषधीः", "great herbs"], ["शिरसा", "with the head"],
               ["पाणिना", "with the hand"], ["धारयेत", "should bear (hold)"]],
              "Two instrumentals tell how the herbs are borne.",
              "ततः, महौषधीः, शिरसा, पाणिना, धारयेत.", role="extend",
              teaches="The instrumental gives the means, with: शिरसा = with the head, पाणिना = with the hand."),
        mcq("discriminate", 3, "Does unit 128 list the herbs of the prajāsthāpana group?",
            ("No; it names only the group", "The members are not listed here."),
            [("Yes; ten herbs are listed", "Ten is Caraka's group, not listed in this text."),
             ("Yes; only lakṣmaṇā is listed", "No member is listed."),
             ("Yes; the banyan shoots are listed", "No member is listed.")],
            "The unit gives the group's name, not its members.",
            "प्रजास्थापन = a named group; members not listed here."),
        mcq("apply", 4, "Which split of महौषधीः is right?",
            ("महा + ओषधीः", "आ + ओ → औ: महा + ओषधीः = महौषधीः."),
            [("महा + उषधीः", "आ + उ would give ओ, not औ."),
             ("महो + षधीः", "Neither part is a word of the card."),
             ("महौ + षधीः", "Neither part is a word of the card.")],
            "महा (great) + ओषधीः (herbs): आ + ओ joins as औ.",
            "अ/आ + ओ → औ."),
        mcq("transfer", 5, "By the rule of महौषधीः, how is महा + ओजः written when joined?",
            ("महौजः", "आ + ओ → औ."),
            [("महोजः", "आ + ओ gives औ, not ओ."),
             ("महाओजः", "The two vowels are joined."),
             ("महवोजः", "No व comes in here.")],
            "महा + ओजः = महौजः, like महा + ओषधीः = महौषधीः.",
            "अ/आ + ओ → औ.",
            teaches="अ or आ before ओ joins into औ: महा + ओषधीः → महौषधीः."),
    ],
}

# ---------------------------------------------------------------- unit 129
AUTHORED["129"] = {
    "title": "एताभिश्च सिद्धं पयो घृतं वा",
    "question": "What three things does unit 129 tell her to do with the prajāsthāpana herbs?",
    "rule": ("With these herbs: drink milk or ghee cooked with them (पिबेत्); bathe with them on every Puṣya (स्नायात्); "
             "and always touch them in this way (आलभेत)."),
    "limits": ("Two printed lines joined. 'These' are the herbs of unit 128. पयस् can also mean water; milk is taken. "
               "सदा may go with आलभेत or with स्नायात्; आलभेत may mean touch or apply, and its object is understood. "
               "No question rests on these points."),
    "explain_hi": ("पहली पंक्ति: इन (प्रजास्थापन) औषधियों से सिद्ध किया दूध या घी पिए। "
                   "दूसरी पंक्ति: इन्हीं से हर पुष्य नक्षत्र पर स्नान करे (पुष्ये पुष्ये), और सदा इसी प्रकार स्पर्श करे (आलभेत)। "
                   "‘एताभिः’ स्त्रीलिंग तृतीया बहुवचन है, जो ‘ओषधी’ (स्त्रीलिंग) से मेल खाता है। "
                   "‘सदा’ किस क्रिया के साथ है, दो तरह पढ़ा जा सकता है; ‘आलभेत’ का अर्थ स्पर्श करना या लगाना भी हो सकता है।"),
    "hook": "पिए, नहाए, छुए: इन्हीं औषधियों से, हर पुष्य पर।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 129, when should she bathe with these herbs?",
            ("On every Puṣya", "पुष्ये पुष्ये स्नायात्."),
            [("On every full moon", "No full moon is named."),
             ("Every morning", "No morning is named."),
             ("On the fourth night only", "No fourth night is named here.")],
            "पुष्ये पुष्ये = on each Puṣya (the lunar mansion).",
            "पुष्ये पुष्ये = on every Puṣya."),
        order(1, "Put the three actions of unit 129 in the text's order.",
              ["पिबेत् (पिए)", "स्नायात् (स्नान करे)", "आलभेत (स्पर्श करे)"],
              "Drink, then bathe, then touch.",
              "पिबेत् → स्नायात् → आलभेत."),
        match(2, "Match each word of unit 129 to its meaning.",
              [["सिद्धम्", "cooked"], ["घृतम्", "ghee"], ["एताभिः", "with these"],
               ["पुष्ये पुष्ये", "on every Puṣya"], ["स्नायात्", "should bathe"]],
              "The words of the drinking and the bathing.",
              "सिद्ध, घृत, एताभिः, पुष्ये पुष्ये, स्नायात्.", role="extend",
              teaches="A doubled word means each one: पुष्ये पुष्ये = on every Puṣya."),
        mcq("discriminate", 3, "एताभिः is feminine instrumental plural. To what does it refer, by the card?",
            ("The great herbs of unit 128", "ओषधी is feminine: the herbs of unit 128."),
            [("The drops of unit 120", "बिन्दु is masculine."),
             ("The brāhmaṇas of unit 127", "ब्राह्मण is masculine."),
             ("The banyan shoots of unit 125", "शुङ्ग here is neuter.")],
            "एताभिः agrees with the feminine ओषधीः of unit 128.",
            "एताभिः (f. inst. pl.) → the herbs."),
        mcq("apply", 4, "Which split of चेत्थम् is right?",
            ("च + इत्थम्", "अ + इ → ए: च + इत्थम् = चेत्थम्."),
            [("च + एत्थम्", "एत्थम् is not a word; अ + ए would give ऐ."),
             ("चे + त्थम्", "Neither part is a word."),
             ("चेत् + थम्", "थम् is not a word.")],
            "च (and) + इत्थम् (thus): अ + इ joins as ए.",
            "अ + इ → ए."),
        mcq("transfer", 5, "Built like पुष्ये पुष्ये, what does the invented phrase दिने दिने mean?",
            ("On every day", "A doubled word means each one."),
            [("On two days only", "Doubling here does not mean two."),
             ("On the day before", "No word for before is present."),
             ("For a single day", "Doubling means each, not one.")],
            "दिने दिने = day by day, like पुष्ये पुष्ये = on every Puṣya.",
            "Doubled locative = on each.",
            teaches="Repeating a word gives 'each, every': पुष्ये पुष्ये, दिने दिने."),
    ],
}

# ---------------------------------------------------------------- unit 130
AUTHORED["130"] = {
    "title": "तथा सर्वासां जीवनीयानामोषधीनाम्",
    "question": "What does unit 130 add about the jīvanīya (life-promoting) herbs?",
    "rule": ("Likewise: the constant use (सदा उपयोगः) of all the jīvanīya (life-promoting) herbs by those various methods "
             "(तैस्तैर्विधिभिः)."),
    "limits": ("No verb is stated, and the sentence appears to run on into unit 131 (the line break falls inside the word, "
               "printed विधिभि). The members of the jīvanīya group are not listed here, so none is identified."),
    "explain_hi": ("‘तथा’ से यह भी जोड़ा गया: सभी जीवनीय (जीवन बढ़ाने वाली) औषधियों का सदा उपयोग, उन-उन विधियों से। "
                   "इस इकाई में क्रिया नहीं है; वाक्य अगली इकाई (‘(इ)ति गर्भस्थापनानि’) में चलता प्रतीत होता है। "
                   "‘जीवनीय’ एक औषध-समूह का नाम है; उसके सदस्य यहाँ नहीं गिनाए गए। "
                   "‘तैस्तैः’ = तैः + तैः, दोहराने से अर्थ ‘उन-उन (विभिन्न)’।"),
    "hook": "सब जीवनीय औषधियाँ, सदा, उन-उन विधियों से (वाक्य आगे चलता है)।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 130, which herbs are to be used constantly?",
            ("All the jīvanīya herbs", "सर्वासां जीवनीयानाम् ओषधीनाम्."),
            [("Only the lakṣmaṇā root", "The unit says all the jīvanīya herbs."),
             ("Only the white bṛhatī", "The unit says all the jīvanīya herbs."),
             ("Only the banyan shoots", "The unit says all the jīvanīya herbs.")],
            "सर्व (all) + जीवनीय (life-promoting) + ओषधी (herb).",
            "सर्वासां जीवनीयानामोषधीनाम्."),
        order(1, "Put the words of unit 130 in the line's order.",
              ["तथा", "सर्वासाम्", "जीवनीयानाम्", "ओषधीनाम्", "सदा उपयोगः", "तैस्तैर्विधिभिः"],
              "Likewise, of all, of the life-promoting, herbs, constant use, by those various methods.",
              "तथा → सर्वासाम् → जीवनीयानाम् → ओषधीनाम् → सदोपयोगः → तैस्तैर्विधिभिः."),
        match(2, "Match each word of unit 130 to its meaning.",
              [["सर्वासाम्", "of all"], ["जीवनीय", "life-promoting"], ["सदा", "always"],
               ["उपयोगः", "use"], ["विधिभिः", "by methods"]],
              "The unit is a noun phrase; no verb is stated.",
              "सर्व, जीवनीय, सदा, उपयोग, विधि.", role="extend",
              teaches="A repeated pronoun means 'various': तैस्तैः विधिभिः = by those various methods."),
        mcq("discriminate", 3, "How does the sentence of unit 130 end, by the card?",
            ("It appears to run on into unit 131", "The line break falls inside विधिभि(र्इ)ति."),
            [("With a verb in this unit", "No verb is stated in unit 130."),
             ("With the list of jīvanīya herbs", "The members are not listed here."),
             ("With a closing verse", "The unit is prose.")],
            "No verb, and the closing (इ)ति comes in unit 131.",
            "GROUPING: unit 130 continues into unit 131."),
        mcq("apply", 4, "Which split of सदोपयोगः is right?",
            ("सदा + उपयोगः", "आ + उ → ओ: सदा + उपयोगः = सदोपयोगः."),
            [("सदा + ओपयोगः", "ओपयोगः is not a word; the noun is उपयोगः."),
             ("सदो + पयोगः", "Neither part is a word of the card."),
             ("सदोप + योगः", "सदोप is not a word.")],
            "सदा (always) + उपयोगः (use): आ + उ joins as ओ.",
            "अ/आ + उ → ओ."),
        mcq("transfer", 5, "By the rule of तैः + तैः → तैस्तैः, how is रामः + तत्र written?",
            ("रामस्तत्र", "Visarga before त becomes स्."),
            [("रामो तत्र", "ओ comes before voiced sounds; त is not voiced."),
             ("रामर्तत्र", "र् does not come from this visarga before त."),
             ("रामत्तत्र", "Visarga does not become त्.")],
            "रामः + तत्र = रामस्तत्र, as तैः + तैः = तैस्तैः.",
            "Visarga + त → स्त.",
            teaches="A visarga before त becomes स्: तैः + तैः → तैस्तैः."),
    ],
}

# ---------------------------------------------------------------- unit 131
AUTHORED["131"] = {
    "title": "(इ)ति गर्भस्थापनानि",
    "question": "What does the short unit 131 call the preceding means?",
    "rule": ("गर्भस्थापनानि = foetus-establishing (ones), neuter nominative plural; the unit closes the list begun in unit 130."),
    "limits": ("The opening ति is read as इति with its इ lost (a possible reading, not certain). No noun is stated for "
               "गर्भस्थापनानि, so the card says '(ones)'. No verb."),
    "explain_hi": ("यह इकाई केवल एक समापन-वाक्यांश है: ‘इस प्रकार, गर्भ को स्थिर करने वाले।’ "
                   "छपा ‘ति’ सम्भवतः ‘इति’ है, जिसका इ छूट गया; यह अनुमान है। "
                   "‘गर्भस्थापनानि’ नपुंसक प्रथमा बहुवचन है; किस संज्ञा का विशेषण है, यह नहीं कहा गया, इसलिए ‘(वाले)’। "
                   "यह इकाई 130 के वाक्य को पूरा करती प्रतीत होती है।"),
    "hook": "गर्भ + स्थापन = गर्भ को स्थिर करने वाले।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What does गर्भस्थापनानि mean, by the card?",
            ("Foetus-establishing (ones)", "गर्भ = foetus; स्थापन = establishing."),
            [("Foetus-destroying (ones)", "स्थापन means establishing, not destroying."),
             ("Birth-hastening (ones)", "No word for hastening is present."),
             ("Womb-cleansing (ones)", "No word for cleansing is present.")],
            "गर्भस्थापन = what makes the foetus stable.",
            "गर्भस्थापनानि = foetus-establishing (ones)."),
        match(1, "Match each part of गर्भस्थापनानि to its meaning.",
              [["गर्भ", "foetus"], ["स्थापन", "establishing, making stable"], ["-आनि", "neuter plural ending: (ones)"]],
              "Two members and a neuter plural ending.",
              "गर्भ + स्थापन + -आनि."),
        mcq("extend", 2, "What grammar does the card give गर्भस्थापनानि?",
            ("Neuter nominative plural", "-आनि marks the neuter plural."),
            [("Masculine accusative plural", "That would end in -आन्."),
             ("Feminine nominative plural", "That would end in -आः."),
             ("Neuter nominative singular", "That would end in -अम्.")],
            "गर्भस्थापनानि: n. nom. pl., with no noun stated.",
            "-आनि = neuter nominative/accusative plural.",
            teaches="An a-stem neuter makes its nominative plural in -आनि."),
        multi("discriminate", 3, "Which statements about unit 131 are right?",
              [("It has no verb", "Right: no verb is stated."),
               ("No noun is stated for गर्भस्थापनानि", "Right: hence '(ones)'."),
               ("It names five new herbs", "No herb is named in this unit."),
               ("It is a metrical verse", "It is prose.")],
              [0, 1],
              "A short closing phrase: no verb and no stated noun.",
              "Unit 131 = closing phrase."),
        mcq("apply", 4, "Which unit's sentence does unit 131 appear to complete, by the card?",
            ("Unit 130", "GROUPING: the sentence of unit 130 appears to run on into 131."),
            [("Unit 132", "Unit 132 comes after and begins a new topic."),
             ("Unit 128", "Unit 128 is a complete sentence with its verb."),
             ("Unit 120", "Unit 120 is far earlier and complete.")],
            "Unit 130 has no verb and breaks off; unit 131 closes it.",
            "130 + 131 = one sentence."),
        mcq("transfer", 5, "Like गर्भस्थापनानि, what is the nominative plural of the neuter a-stem मूल (root)?",
            ("मूलानि", "Neuter a-stem: -आनि."),
            [("मूलाः", "That is the masculine plural ending."),
             ("मूलम्", "That is the singular."),
             ("मूलान्", "That is the masculine accusative plural ending.")],
            "मूल → मूलानि, like स्थापन → स्थापनानि.",
            "Neuter a-stem nominative plural: -आनि.",
            teaches="A neuter a-stem takes -आनि in the nominative plural: स्थापनानि, मूलानि."),
    ],
}

# ---------------------------------------------------------------- unit 132
AUTHORED["132"] = {
    "title": "सौम्याकृतिवचनोपचारचेष्टाः",
    "question": "What kind of attendants does unit 132 describe, and who else is named?",
    "rule": ("Attendants gentle in form, speech, service and conduct, following what is dear and beneficial (प्रियहितानुवर्तिनः); "
             "and likewise the husband (तथा भर्ता)."),
    "limits": ("No verb is stated. Whether the qualities also apply to the husband is not decided. The closing इति is not translated."),
    "explain_hi": ("परिचारक कैसे हों: सौम्य आकृति, वचन, सेवा (उपचार) और चेष्टा वाले, और प्रिय तथा हितकर का अनुसरण करने वाले। "
                   "‘तथा भर्ता’: और वैसे ही पति। गुण पति पर भी लागू हैं या नहीं, यह तय नहीं किया गया। "
                   "इस वाक्य में क्रिया नहीं है। "
                   "‘तथाभर्तेति’ = तथा + भर्ता + इति (आ + इ → ए)।"),
    "hook": "सौम्य रूप, वाणी, सेवा, चेष्टा: ऐसे परिचारक, और वैसे ही पति।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "Besides the attendants, who is named in unit 132?",
            ("The husband", "तथा भर्ता: and likewise the husband."),
            [("The physician", "No physician is named."),
             ("The brāhmaṇas", "Brāhmaṇas are in unit 127."),
             ("The woman's mother", "No mother is named.")],
            "भर्ता = husband.",
            "तथा भर्ता = likewise the husband."),
        order(1, "Put the four qualities of the attendants in the compound's order.",
              ["आकृति", "वचन", "उपचार", "चेष्टा"],
              "Gentle in form, speech, service and conduct.",
              "आकृति → वचन → उपचार → चेष्टा."),
        match(2, "Match each word of unit 132 to its meaning.",
              [["आकृति", "form"], ["वचन", "speech"], ["उपचार", "service"], ["चेष्टा", "conduct"],
               ["परिचारकाः", "attendants"]],
              "Four qualities of the attendants and the attendants themselves.",
              "आकृति, वचन, उपचार, चेष्टा, परिचारक.", role="extend",
              teaches="सौम्य (gentle) at the head of the compound qualifies all four: form, speech, service, conduct."),
        mcq("discriminate", 3, "Does unit 132 say the husband must also be gentle in form and speech?",
            ("It is not decided", "The card leaves open whether the qualities apply to him."),
            [("Yes, it says so clearly", "The text adds only तथा भर्ता."),
             ("No, it says he need not be", "Nothing of the kind is said."),
             ("Yes, and older than her too", "No age is named here.")],
            "तथा भर्ता is left without its own qualities.",
            "Whether the adjectives cover भर्ता is undecided."),
        mcq("apply", 4, "Which split of तथाभर्तेति is right?",
            ("तथा + भर्ता + इति", "आ + इ → ए: भर्ता + इति = भर्तेति."),
            [("तथा + भर्ता + एति", "आ + ए would give ऐ (भर्तैति)."),
             ("तथा + भर्तृ + इति", "ऋ before इ would give र् (भर्त्रिति)."),
             ("तथा + भर्ते + ति", "Neither भर्ते nor ति is the card's word here.")],
            "तथा (likewise) + भर्ता (husband) + इति (thus).",
            "आ + इ → ए."),
        mcq("transfer", 5, "By the rule of भर्ता + इति, how is सीता + इति written?",
            ("सीतेति", "आ + इ → ए."),
            [("सीतैति", "That would be आ + ए."),
             ("सीतिति", "The आ cannot simply vanish."),
             ("सीतायिति", "No य comes in here.")],
            "सीता + इति = सीतेति, like भर्ता + इति = भर्तेति.",
            "अ/आ + इ → ए.",
            teaches="अ or आ before इ joins into ए: भर्ता + इति → भर्तेति."),
    ],
}

# ---------------------------------------------------------------- unit 133
AUTHORED["133"] = {
    "title": "पुनश्चैनां मासादुपेयात्",
    "question": "In unit 133, after how long should he approach her again?",
    "rule": ("पुनः च एनाम् मासात् उपेयात्: and again, after a month (मासात्), he should approach her."),
    "limits": ("The subject is not stated; the third-person verb is read as the husband of unit 132. मासात् may mean 'after "
               "a month' or 'from a month onward'."),
    "explain_hi": ("यह छोटा वाक्य समय बताता है: ‘और फिर एक महीने बाद इसके पास जाए।’ "
                   "‘मासात्’ पञ्चमी है: ‘महीने के बाद’ (या ‘महीने से आगे’)। "
                   "‘उपेयात्’ (उप + इ) विधिलिङ् है: पास जाए। कर्ता नहीं कहा गया; पिछली इकाई का पति माना गया। "
                   "‘पुनश्चैनाम्’ = पुनः + च + एनाम् (विसर्ग → श् च से पहले, अ + ए → ऐ)।"),
    "hook": "पुनः, मासात्: एक महीने बाद फिर।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 133, after how long should he approach her again?",
            ("After a month", "मासात् = after a month."),
            [("After a fortnight", "No fortnight is named."),
             ("After a year", "No year is named."),
             ("After three nights", "No nights are named here.")],
            "मास = month; मासात् = after a month.",
            "मासात् = after a month."),
        order(1, "Put the words of unit 133 in the line's order.",
              ["पुनः", "च", "एनाम्", "मासात्", "उपेयात्"],
              "Again, and, her, after a month, should approach.",
              "पुनः → च → एनाम् → मासात् → उपेयात्."),
        match(2, "Match each word of unit 133 to its meaning.",
              [["पुनः", "again"], ["एनाम्", "her"], ["मासात्", "after a month"], ["उपेयात्", "should approach"]],
              "Four content words make the line.",
              "पुनः, एनाम्, मासात्, उपेयात्.", role="extend",
              teaches="An ablative of time can mean 'after': मासात् = after a month."),
        mcq("discriminate", 3, "Which split of पुनश्चैनाम् is right?",
            ("पुनः + च + एनाम्", "Visarga → श् before च; अ + ए → ऐ."),
            [("पुनः + च + इनाम्", "अ + इ would give ए, not ऐ."),
             ("पुन + श्च + एनाम्", "श्च is not a word."),
             ("पुनः + चै + नाम्", "चै is not a word.")],
            "पुनः (again) + च (and) + एनाम् (her).",
            "Visarga + च → श्च; अ + ए → ऐ."),
        mcq("apply", 4, "Who is the subject of उपेयात्, by the card?",
            ("Not stated; read as the husband", "The verb is third person; the husband of unit 132 is understood."),
            [("The woman, named here", "एनाम् (her) is the object, not the subject."),
             ("The attendants, named here", "The verb is singular; no one is named."),
             ("The physician, named here", "No physician is named.")],
            "The line names no subject; the card reads the husband.",
            "उपेयात्: subject understood."),
        mcq("transfer", 5, "By the rule of पुनः + च → पुनश्च, how is रामः + च written?",
            ("रामश्च", "Visarga before च becomes श्."),
            [("रामो च", "ओ comes before voiced sounds; च is not voiced."),
             ("रामर्च", "र् does not come from this visarga before च."),
             ("रामस्च", "स् comes before त; before च it is श्.")],
            "रामः + च = रामश्च, like पुनः + च = पुनश्च.",
            "Visarga + च → श्च.",
            teaches="A visarga before च becomes श्: पुनः + च → पुनश्च, रामः + च → रामश्च."),
    ],
}

# ===================================================================== NOTES_HI
NOTES_HI = {
    "120": ("विश्वास निम्न। पाठ-चिह्न: (1) ‘पित्रुना’ प्रयोग-योग्य शब्द नहीं; ‘वामे तु दुहितृकामा’ के विरोध से ‘पुत्रकामा’ (पुत्र की इच्छा वाली) "
            "सम्भावित अर्थ है, पर यह अनुमान है, इसलिए दाहिने छिद्र और पुत्र पर प्रश्न नहीं; (2) ‘विश्वेदेवानाम्’ सम्भवतः ‘विश्वदेवानाम्’ "
            "(एक वनस्पति-नाम), अनिश्चित। पहचान: लक्ष्मणा विवादित (प्रायः Ipomoea sepiaria मानी जाती), वटशुङ्ग = बरगद के अंकुर, "
            "Ficus benghalensis (मानक), सहदेवा = सम्भवतः Vernonia cinerea (सहदेई), विश्वेदेवा अज्ञात। ‘दुहितृकामा’ स्त्रीलिंग है, "
            "इसलिए कर्ता स्त्री है। सन्धि: क्षीरे + अभिषुत्य → क्षीरेऽभिषुत्य (ए + अ → एऽ); त्रीन् + चतुरः → त्रींश्चतुरः (न् → ंश् च से पहले)।"),
    "121": ("विश्वास उच्च, कोई पाठ-चिह्न नहीं। ‘एतान्’ (पुं. द्वितीया बहुवचन) सम्भवतः इकाई 120 की बूँदें (बिन्दून्) हैं; कर्ता स्त्री। "
            "सन्धि: च + एतान् → चैतान् (अ + ए → ऐ); एतान् + निष्ठीवेत् → एतान्निष्ठीवेत्।"),
    "122": ("विश्वास मध्यम, कोई पाठ-चिह्न नहीं। कर्ता नहीं कहा गया (इकाई 120 में ‘स्वयम्’ है, इकाई 126 किसी दूसरे के डालने की ओर संकेत कर सकती है), "
            "इसलिए अनुवाद में ‘one’। पहचान: बृहती सामान्यतः सम्भवतः Solanum indicum; श्वेत बृहती विवादित। मात्रा नहीं दी गई। "
            "सन्धि: पुष्य + उद्धृतायाः → पुष्योद्धृतायाः (अ + उ → ओ); मूलकल्कात् + रसम् → मूलकल्काद्रसम् (त् → द् घोष से पहले)। "
            "छपा ‘मूलकल्कादरसं’ नहीं, ‘मूलकल्काद्रसं’ है।"),
    "123": ("विश्वास मध्यम। पाठ-चिह्न: छपा ‘तद्वचोत्पल’; तद्वत् + च से ‘तद्वच्च’ बनना चाहिए, उत्- से पहले एक च छूटा प्रतीत होता है। "
            "इकाई अधूरी है: नावयेत् का कर्म और तैयारी नहीं कही गई; कुछ जोड़ा नहीं गया। ‘आठ’ को वटशुङ्गानि से जोड़ा गया, पर छपा क्रम "
            "‘वटशुंगानि चाष्टौ च’ पूरी तरह साफ़ नहीं, इसलिए संख्या पर प्रश्न नहीं। पत्र = पत्ता, कमल-जातीय में पंखुड़ी भी। उत्पल और कुमुद दोनों "
            "जल-कमल (सम्भावित)।"),
    "124": ("विश्वास मध्यम, कोई पाठ-चिह्न नहीं। उदुम्बर = Ficus racemosa, गूलर (मानक); ‘उदुम्बरमात्र’ = उदुम्बर जितना; फल का आकार "
            "सामान्य पठन है, पाठ केवल ‘मात्र’ कहता है। ‘पयस्’ दूध या जल; यहाँ दूध लिया गया (इकाई 120 से संगत)। "
            "सन्धि: शुक्ल-माल्य-अम्बर → शुक्लमाल्याम्बर (अ + अ → आ); पुत्रस्य + उत्पादाय → पुत्रस्योत्पादाय (अ + उ → ओ); "
            "पुष्योद्धृतायाः + लक्ष्मणायाः → पुष्योद्धृताया लक्ष्मणायाः (आः के विसर्ग का घोष से पहले लोप)।"),
    "125": ("विश्वास निम्न। पाठ-चिह्न: (1) ‘अग्नित्जिह्वाम्’ में अतिरिक्त त्; ‘अग्निजिह्वा’ पौधे का नाम (सम्भवतः Gloriosa superba, कलिहारी); "
            "(2) ‘वावा’ सम्भवतः एक ‘वा’ की पुनरावृत्ति (‘या आठ वट-अंकुर’)। ‘वौरदण्ड’ और ‘नम्रजीव’ अस्पष्ट, न विभाजित न पहचाने गए। "
            "‘मध्यदण्ड’ = बीच का डंठल; शंखपुष्पी से जुड़ा है या नहीं, तय नहीं। पहचान: अपामार्ग = Achyranthes aspera (मानक, चिचड़ा); "
            "सहचर = सम्भवतः Barleria prionitis; शंखपुष्पी विवादित (प्रायः Convolvulus pluricaulis, अन्य प्रस्ताव भी); जीवक, ऋषभक विवादित "
            "(अष्टवर्ग के द्रव्य, प्रायः Malaxis की जातियाँ मानी जाती, विकल्प-द्रव्य प्रयुक्त)। छपा ‘जीवकऋषभकौ’ में ऋ अलग रखा गया है; "
            "उस पर सन्धि-प्रश्न नहीं बनाया गया। इकाई में क्रिया नहीं।"),
    "126": ("विश्वास मध्यम, कोई पाठ-चिह्न नहीं। जो पीसा गया उसका नाम नहीं (इकाई 125 के द्रव्य समझे जाते)। ‘आघ्राय’ का कर्ता नहीं कहा गया: "
            "स्त्री या डालने वाला। ‘स्थिताम्’ (स्त्री. द्वितीया) देहली पर खड़ी स्त्री। ‘पूर्ववत्’ = इकाई 120 आदि के नस्य की तरह। "
            "सन्धि: पच्यमानस्य + ऊष्माणम् → पच्यमानस्योष्माणम् (अ + ऊ → ओ); पूर्ववत् + नावयेत् → पूर्ववन्नावयेत् (त् → न् अनुनासिक से पहले)।"),
    "127": ("विश्वास उच्च, कोई पाठ-चिह्न नहीं। कर्ता नहीं कहा गया (पिछली इकाइयों की स्त्री)। क्या कहें, यह नहीं जोड़ा गया। "
            "सन्धि: यत् + च → यच्च; च + अन्यत् → चान्यत्; अन्यत् + अपि → अन्यदपि; ब्राह्मणाः + वृद्ध → ब्राह्मणा वृद्ध (आः का विसर्ग घोष से पहले लुप्त); "
            "वृद्धस्त्रियः + वा → वृद्धस्त्रियो वा। ‘वाब्रूयुः’ को डेटा ‘वा + अब्रूयुः’ बाँटता है, पर विधिलिङ् में अ-आगम नहीं होता; "
            "शुद्ध विभाजन ‘वा + ब्रूयुः’ लगता है (अर्थ वही: कहें)। इस पर प्रश्न नहीं।"),
    "128": ("विश्वास मध्यम। पाठ-चिह्न: छपा ‘प्रजास्थापनारख्या’ में अतिरिक्त र्; ‘प्रजास्थापनाख्या’ पढ़ा गया; अन्तिम -आ, -आः का म- से पहले "
            "नियमित सन्धि-रूप है (महौषधीः से मेल)। इस समूह के सदस्य यहाँ नहीं गिनाए गए (चरक में प्रजास्थापन दस द्रव्यों का समूह है, "
            "पर यह ग्रन्थ यहाँ सूची नहीं देता), इसलिए कोई पहचान नहीं। ‘धारयेत’ आत्मनेपद णिजन्त विधिलिङ्। सन्धि: महा + ओषधीः → महौषधीः (आ + ओ → औ)।"),
    "129": ("विश्वास मध्यम; दो छपी पंक्तियाँ [02.01.145, 02.01.146] जोड़ी गईं। ‘एताभिः’ = इकाई 128 की औषधियाँ। ‘पयः’ जल भी हो सकता है; "
            "दूध लिया गया। ‘सदा’ आलभेत के साथ पढ़ा गया, स्नायात् के साथ भी जा सकता है। ‘आलभेत’ = स्पर्श करे / पकड़े, ‘लगाए’ भी सम्भव; "
            "कर्म नहीं कहा गया। इन बिन्दुओं पर प्रश्न नहीं। सन्धि: एताभिः + च → एताभिश्च (विसर्ग → श्); सिद्धम् + पयः → सिद्धं पयः; "
            "पयः + घृतम् → पयो घृतम् (अः → ओ घोष से पहले); च + इत्थम् → चेत्थम् (अ + इ → ए)।"),
    "130": ("विश्वास मध्यम। पाठ-चिह्न: छपा ‘विधिभि’; अगली इकाई के ‘ति’ को (इ)ति पढ़ें तो ‘विधिभिरिति’ बनता है, पंक्ति-अन्त पर ‘रि’ छूटा। "
            "वाक्य इकाई 131 में चलता प्रतीत होता है (GROUPING)। क्रिया नहीं। ‘जीवनीय’ एक औषध-समूह का नाम; सदस्य यहाँ नहीं गिनाए गए "
            "(चरक में दस द्रव्यों का समूह)। सन्धि: सदा + उपयोगः → सदोपयोगः (आ + उ → ओ); उपयोगः + तैः → उपयोगस्तैः और तैः + तैः → तैस्तैः "
            "(विसर्ग → स् त से पहले); तैः + विधिभिः → तैर्विधिभिः (ऐः का विसर्ग घोष से पहले र्)।"),
    "131": ("विश्वास मध्यम। पाठ-चिह्न: आरम्भ का ‘इ’ छूटा प्रतीत होता है; ‘ति’ को ‘इति’ पढ़ा गया जो इकाई 130 की सूची बन्द करता है (सम्भावित पाठ)। "
            "इस पर प्रश्न नहीं। ‘गर्भस्थापनानि’ नपुंसक प्रथमा बहुवचन विशेषण; संज्ञा नहीं कही गई, इसलिए ‘(वाले)’।"),
    "132": ("विश्वास मध्यम, कोई पाठ-चिह्न नहीं। क्रिया नहीं। गुण पति पर भी लागू हैं या नहीं, तय नहीं। अन्तिम ‘इति’ अनूदित नहीं। "
            "उपचार = सेवा; चेष्टा = आचरण। सन्धि: सौम्य + आकृति → सौम्याकृति (अ + आ → आ); वचन + उपचार → वचनोपचार (अ + उ → ओ); "
            "चेष्टाः + च → चेष्टाश्च; परिचारकाः + तथा → परिचारकास्तथा (विसर्ग → स्); भर्ता + इति → भर्तेति (आ + इ → ए)।"),
    "133": ("विश्वास मध्यम, कोई पाठ-चिह्न नहीं। कर्ता नहीं कहा गया; तृतीय पुरुष क्रिया को इकाई 132 के पति से जोड़ा गया। "
            "‘मासात्’ = महीने के बाद, या महीने से आगे। सन्धि: पुनः + च → पुनश्च (विसर्ग → श्); च + एनाम् → चैनाम् (अ + ए → ऐ); "
            "मासात् + उपेयात् → मासादुपेयात् (त् → द् स्वर से पहले)।"),
}

# ===================================================================== AIDS
AIDS = {
    "120": {
        "diagram": {"groups": [
            {"label": "इनमें से कोई एक (अन्यतमा)", "items": ["लक्ष्मणा (विवादित)", "वटशुङ्ग (मानक)", "सहदेवा (सम्भावित)", "विश्वेदेवा (अज्ञात)"]},
            {"label": "विधि", "items": ["दूध में कूटकर", "तीन या चार बूँदें", "स्वयं डाले", "बाएँ में: दुहितृकामा"]}]},
        "chunks": "लक्ष्मणा-वटशुङ्ग-सहदेवा-विश्वेदेवानाम् अन्यतमाम् | क्षीरेऽभिषुत्य | त्रींश्चतुरो वा बिन्दून् | दक्षिणे नासापुटे स्वयमासिञ्चेत् | पित्रुना (अस्पष्ट) | वामे तु दुहितृकामा",
        "contrast": "दक्षिणे (दाहिने) ↔ वामे (बाएँ): बाएँ के साथ ‘दुहितृकामा’ साफ़ है; दाहिने के साथ का शब्द क्षतिग्रस्त है।",
        "sandhi": "ए + अ → एऽ: क्षीरे + अभिषुत्य → क्षीरेऽभिषुत्य · न् + च → ंश्च: त्रीन् + चतुरः → त्रींश्चतुरः।",
    },
    "121": {
        "chunks": "न चैतान् | निष्ठीवेत्",
        "sandhi": "अ + ए → ऐ: च + एतान् → चैतान्।",
        "frame": "न + विधिलिङ् = निषेध: न निष्ठीवेत् = न थूके। एतान् (पुं. द्वि. बहु.) ↔ बिन्दून् (पुं. द्वि. बहु.)।",
    },
    "122": {
        "chain": {"steps": ["पुष्य में उखाड़ी श्वेत बृहती", "जड़ (मूल)", "लुगदी (कल्क)", "उससे रस", "नाक में डाले (नावयेत्)"]},
        "sandhi": "अ + उ → ओ: पुष्य + उद्धृतायाः → पुष्योद्धृतायाः · त् → द् घोष से पहले: मूलकल्कात् + रसम् → मूलकल्काद्रसम्।",
        "chunks": "तथा | पुष्योद्धृतायाः श्वेतबृहत्याः | मूलकल्काद्रसम् | नावयेत्",
    },
    "123": {
        "diagram": {"groups": [
            {"label": "तद्वत् (वैसे ही), क्रम से", "items": ["उत्पल-पत्र", "कुमुद-पत्र", "लक्ष्मणा-मूल", "वट-शुङ्ग (आठ?)"]},
            {"label": "फिर", "items": ["नावयेत् (तैयारी नहीं कही)"]}]},
        "sandhi": "त् + च → च्च: तद्वत् + च → तद्वच्च (छपा ‘तद्वचो-’, एक च छूटा) · अ + उ → ओ: च + उत्पल → चोत्पल · अ + अ → आ: च + अष्टौ → चाष्टौ।",
        "chunks": "तद्वच्चोत्पलपत्रम् | कुमुदपत्रम् | लक्ष्मणामूलम् | वटशुङ्गानि चाष्टौ च | नावयेत्",
    },
    "124": {
        "chain": {"steps": ["श्वेत माला-वस्त्र वाली स्त्री", "पुष्य में उखाड़ी लक्ष्मणा", "जड़ की लुगदी", "उदुम्बर-भर मात्रा", "दूध के साथ पिए", "पुत्र की उत्पत्ति व स्थिति हेतु"]},
        "sandhi": "अ + उ → ओ: पुत्रस्य + उत्पादाय → पुत्रस्योत्पादाय · अ + अ → आ: माल्य + अम्बर → माल्याम्बर।",
        "chunks": "शुक्लमाल्याम्बरधरा च नारी | पुष्योद्धृताया लक्ष्मणाया मूलकल्कम् | उदुम्बरमात्रं पयसा पिबेत् | पुत्रस्योत्पादाय स्थितये च",
        "frame": "दो उद्देश्य, दोनों चतुर्थी: उत्पादाय (उत्पत्ति के लिए) + स्थितये (स्थिति के लिए)।",
    },
    "125": {
        "diagram": {"groups": [
            {"label": "स्पष्ट नाम", "items": ["अपामार्ग (मानक)", "जीवक, ऋषभक (विवादित)", "शंखपुष्पी (विवादित)", "मध्यदण्ड", "सहचर (सम्भावित)", "अग्निजिह्वा (सुधरा पाठ)"]},
            {"label": "अस्पष्ट", "items": ["वौरदण्ड", "नम्रजीव"]},
            {"label": "विकल्प", "items": ["या आठ वट-अंकुर"]}]},
        "chunks": "तद्वत् | वौरदण्डम् (अस्पष्ट) | अपामार्गम् | जीवकऋषभकौ | शङ्खपुष्पीम् | मध्यदण्डम् | सहचरम् | नम्रजीवम् (अस्पष्ट) | अग्निजिह्वाम् | अष्टौ वा वटशुङ्गानि",
        "anchors": "याद-सूत्र (मेरा): सूची में तीन ठप्पे — मानक (अपामार्ग), सम्भावित (सहचर), विवादित (जीवक-ऋषभक, शंखपुष्पी)।",
    },
    "126": {
        "chain": {"steps": ["पीसा हुआ (पिष्ट)", "पक रहा (पच्यमान)", "भाप सूँघकर (ऊष्माणम् आघ्राय)", "उसका रस (तद्रसम्)", "देहली पर खड़ी स्त्री को", "पहले की तरह नस्य"]},
        "sandhi": "अ + ऊ → ओ: पच्यमानस्य + ऊष्माणम् → पच्यमानस्योष्माणम् · त् → न् अनुनासिक से पहले: पूर्ववत् + नावयेत् → पूर्ववन्नावयेत्।",
        "chunks": "पिष्टस्य च पच्यमानस्य | ऊष्माणमाघ्राय | तद्रसम् | देहल्यां स्थिताम् | पूर्ववन्नावयेत्",
    },
    "127": {
        "frame": "यत् (जो कुछ) ... ब्रूयुः (कहें) → तत् च कुर्यात् (वह भी करे)। कहने वाले: ब्राह्मणाः या वृद्धस्त्रियः।",
        "sandhi": "त् + च → च्च: यत् + च → यच्च · अ + अ → आ: च + अन्यत् → चान्यत् · त् → द् स्वर से पहले: अन्यत् + अपि → अन्यदपि।",
        "chunks": "यच्चान्यदपि | ब्राह्मणा वृद्धस्त्रियो वा ब्रूयुः | तच्च कुर्यात्",
    },
    "128": {
        "frame": "ततः (फिर) → कौन: प्रजास्थापन नामक महौषधियाँ → कैसे: शिरसा (सिर से) + दक्षिणेन पाणिना (दाहिने हाथ से) → धारयेत (धारण करे)।",
        "sandhi": "आ + ओ → औ: महा + ओषधीः → महौषधीः।",
        "chunks": "ततः | प्रजास्थापनाख्या महौषधीः | शिरसा | दक्षिणेन च पाणिना | धारयेत",
        "pegs": "मेरा बनाया चित्र: सिर पर औषधियों की छोटी पोटली और दाहिने हाथ में एक गुच्छा। (केवल याद के लिए)",
    },
    "129": {
        "chain": {"steps": ["इन औषधियों से सिद्ध दूध या घी पिए", "इन्हीं से हर पुष्य पर स्नान करे", "सदा इसी प्रकार स्पर्श करे"]},
        "sandhi": "विसर्ग → श् च से पहले: एताभिः + च → एताभिश्च · अः → ओ घोष से पहले: पयः + घृतम् → पयो घृतम् · अ + इ → ए: च + इत्थम् → चेत्थम्।",
        "chunks": "एताभिश्च सिद्धं पयो घृतं वा पिबेत् ‖ एताभिरेव पुष्ये पुष्ये स्नायात् | सदा चेत्थमालभेत",
    },
    "130": {
        "chunks": "तथा | सर्वासां जीवनीयानाम् ओषधीनाम् | सदोपयोगः | तैस्तैर्विधिभि(र्इति) → इकाई 131",
        "sandhi": "आ + उ → ओ: सदा + उपयोगः → सदोपयोगः · विसर्ग → स् त से पहले: तैः + तैः → तैस्तैः · विसर्ग → र् घोष से पहले: तैः + विधिभिः → तैर्विधिभिः।",
        "frame": "कौन-सी: सभी जीवनीय औषधियाँ → क्या: सदा उपयोग → कैसे: उन-उन विधियों से → (वाक्य इकाई 131 में पूरा)।",
    },
    "131": {
        "chunks": "(इ)ति | गर्भस्थापनानि",
        "frame": "गर्भ (गर्भ) + स्थापन (स्थिर करने वाला) + -आनि (नपुं. बहु.) = गर्भ को स्थिर करने वाले।",
        "contrast": "इकाई 128: प्रजा-स्थापन (सन्तान को स्थिर करने वाली) ↔ इकाई 131: गर्भ-स्थापन (गर्भ को स्थिर करने वाले)।",
    },
    "132": {
        "diagram": {"groups": [
            {"label": "परिचारक: सौम्य", "items": ["आकृति", "वचन", "उपचार", "चेष्टा"]},
            {"label": "और", "items": ["प्रिय-हित का अनुसरण"]},
            {"label": "तथा", "items": ["भर्ता (पति)"]}]},
        "sandhi": "अ + आ → आ: सौम्य + आकृति → सौम्याकृति · अ + उ → ओ: वचन + उपचार → वचनोपचार · विसर्ग → स्: परिचारकाः + तथा → परिचारकास्तथा · आ + इ → ए: भर्ता + इति → भर्तेति।",
        "chunks": "सौम्याकृतिवचनोपचारचेष्टाश्च | प्रियहितानुवर्तिनः | परिचारकाः | तथा भर्ता इति",
    },
    "133": {
        "chunks": "पुनश्चैनाम् | मासात् | उपेयात्",
        "sandhi": "विसर्ग → श् च से पहले: पुनः + च → पुनश्च · अ + ए → ऐ: च + एनाम् → चैनाम् · त् → द् स्वर से पहले: मासात् + उपेयात् → मासादुपेयात्।",
        "frame": "पुनः (फिर) + मासात् (महीने बाद) + उपेयात् (पास जाए); कर्ता नहीं कहा गया।",
    },
}

# ===================================================================== IMAGE_SPECS
IMAGE_SPECS = {
    ("120", "diagram"): {
        "file": "sh1-nasya-bindu-120.svg",
        "alt": ("Flowchart of unit 120: any one of four plants (lakshmana, disputed; banyan shoots, standard; sahadeva, probable; "
                "vishvedeva, unidentified) is pounded in milk; she herself instils three or four drops; the left nostril goes "
                "with one desiring a daughter; the word with the right nostril is damaged."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"लक्ष्मणा (विवादित)\"] --> E[\"कोई एक\"]\n"
                 "  B[\"वटशुङ्ग (मानक)\"] --> E\n"
                 "  C[\"सहदेवा (सम्भावित)\"] --> E\n"
                 "  D[\"विश्वेदेवा (अज्ञात)\"] --> E\n"
                 "  E --> F[\"दूध में कूटकर\"]\n"
                 "  F --> G[\"तीन या चार बूँदें,<br/>स्वयं डाले\"]\n"
                 "  G --> H[\"दाहिना छिद्र:<br/>शब्द क्षतिग्रस्त\"]\n"
                 "  G --> I[\"बायाँ छिद्र:<br/>पुत्री की इच्छा\"]\n"),
    },
    ("122", "chain"): {
        "file": "sh1-shveta-brihati-122.svg",
        "alt": ("Chain of unit 122: white brihati uprooted under Pushya, its root, the root-paste, the juice from it, "
                "instilled into the nose."),
        "type": "chain",
        "title": "श्वेत बृहती का नस्य (इकाई १२२)",
        "steps": ["पुष्य में उखाड़ी", "जड़", "लुगदी", "रस", "नाक में डाले"],
    },
    ("124", "chain"): {
        "file": "sh1-lakshmana-pana-124.svg",
        "alt": ("Chain of unit 124: a woman in white garlands and garments; lakshmana uprooted under Pushya; its root-paste; "
                "the measure of an udumbara; drunk with milk; for the birth and the stability of a son."),
        "type": "chain",
        "title": "लक्ष्मणा-मूल का पान (इकाई १२४)",
        "steps": ["श्वेत माला-वस्त्र", "पुष्य में उखाड़ी लक्ष्मणा", "जड़ की लुगदी", "उदुम्बर-भर", "दूध के साथ पिए", "पुत्र की उत्पत्ति, स्थिति"],
    },
    ("125", "diagram"): {
        "file": "sh1-dravya-suchi-125.svg",
        "alt": ("Table of unit 125 in list order with the card's labels: vauradanda unclear; apamarga, Achyranthes aspera, standard; "
                "jivaka and rishabhaka, disputed; shankhapushpi, disputed; middle stalk; sahacara, probable Barleria prionitis; "
                "namrajiva unclear; agnijihva, probable Gloriosa superba, corrected reading; or eight banyan shoots."),
        "type": "table",
        "title": "इकाई १२५: सूची क्रम से",
        "heads": ["नाम", "पहचान"],
        "rows": [["वौरदण्ड", "अस्पष्ट"],
                 ["अपामार्ग", "चिचड़ा (मानक)"],
                 ["जीवक, ऋषभक", "विवादित"],
                 ["शंखपुष्पी", "शंखाहुली? (विवादित)"],
                 ["मध्यदण्ड", "बीच का डंठल"],
                 ["सहचर", "कटसरैया (सम्भावित)"],
                 ["नम्रजीव", "अस्पष्ट"],
                 ["अग्निजिह्वा", "कलिहारी (सम्भावित)"],
                 ["या वटशुङ्ग", "आठ बरगद-अंकुर"]],
    },
    ("126", "chain"): {
        "file": "sh1-ushma-nasya-126.svg",
        "alt": ("Chain of unit 126: what is ground, being cooked; its vapour smelled; its juice; to the woman standing on the "
                "threshold; instilled into the nose as before."),
        "type": "chain",
        "title": "भाप और नस्य (इकाई १२६)",
        "steps": ["पीसा हुआ", "पक रहा", "भाप सूँघकर", "उसका रस", "देहली पर खड़ी को", "पहले की तरह नस्य"],
    },
    ("129", "chain"): {
        "file": "sh1-prajasthapana-129.svg",
        "alt": ("Chain of unit 129: with the prajasthapana herbs, drink milk or ghee cooked with them; bathe with them on every "
                "Pushya; always touch them in this way."),
        "type": "chain",
        "title": "इन्हीं औषधियों से (इकाई १२९)",
        "steps": ["सिद्ध दूध या घी पिए", "हर पुष्य पर स्नान", "सदा इसी प्रकार स्पर्श"],
    },
    ("132", "diagram"): {
        "file": "sh1-paricharaka-132.svg",
        "alt": ("Mind map of unit 132: attendants gentle in form, speech, service and conduct, following what is dear and "
                "beneficial; and likewise the husband."),
        "type": "mermaid",
        "code": ("mindmap\n"
                 "  परिचारक\n"
                 "    सौम्य\n"
                 "      आकृति\n"
                 "      वचन\n"
                 "      उपचार\n"
                 "      चेष्टा\n"
                 "    प्रिय और हित के अनुवर्ती\n"
                 "    तथा भर्ता\n"),
    },
}
