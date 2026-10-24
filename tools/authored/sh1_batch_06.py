from helpers import mcq, match, order, fill, multi, accepts


def T(q, teaches):
    q["teaches"] = teaches
    return q


AUTHORED = {}

# ---------------------------------------------------------------- unit 67
AUTHORED["67"] = {
    "title": "कुणपरेतसि धातकीपुष्प",
    "question": "What does unit 67 have one drink in kuṇapa-retas, and cooked with what?",
    "rule": ("In kuṇapa-retas (probably semen with a corpse-like smell) one should make him drink ghee cooked with dhātakī "
             "flowers, khadira, arjuna and dāḍima; a second, damaged alternative follows."),
    "limits": ("Low confidence. The damaged अमनादिभिः (perhaps मदनादिभिः) is only conjectural; no question rests on it. "
               "खदिार्जुन is read as खदिर + अर्जुन. Kuṇapa as a smell is probable. No dose or duration is given."),
    "explain_hi": ("यह गद्य-पंक्ति कुणप-रेतस् की चिकित्सा देती है; कुणप यानी शव, और सामान्य समझ "
                   "है शव जैसी गन्ध वाला शुक्र (सम्भावित अर्थ)। उसमें घी पिलाना है जो धातकी के फूल, खदिर (खैर), अर्जुन और दाडिम "
                   "(अनार) के साथ पकाया गया हो। ‘पाययेत्’ प्रेरणार्थक रूप है: (उसे) पिलाए। "
                   "दूसरा विकल्प ‘अमनादिभिः’ क्षतिग्रस्त है; ‘मदनादिभिः’ केवल अनुमान है, इसलिए उस पर कोई प्रश्न नहीं।"),
    "hook": "शव-गन्धी शुक्र? धातकी, खैर, अर्जुन, अनार वाला घी पिलाओ।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 67, what is the man to be made to drink?",
            ("Ghee (सर्पिः)", "सर्पिः पाययेत्: one should make him drink ghee."),
            [("Milk (क्षीर)", "Milk is not named in this unit."),
             ("A decoction (क्वाथ)", "A decoction is named in units 70 and 71, not here."),
             ("Honey (मधु)", "Honey is not named in this unit.")],
            "The unit ends: सर्पिः पाययेत्, one should make him drink ghee cooked with the named drugs.",
            "सर्पिः = ghee; पाययेत् = should make (him) drink."),
        order(1, "Put these words of unit 67 in their printed order.",
              ["कुणपरेतसि", "धातकीपुष्प…दाडिमैः", "सिद्धम्", "सर्पिः", "पाययेत्"],
              "Fault, then the drugs, cooked, then the ghee and the verb (the damaged word left out).",
              "कुणपरेतसि → धातकीपुष्प…दाडिमैः → सिद्धम् → सर्पिः → पाययेत्."),
        T(match(2, "Match each word of unit 67 to its meaning on the card.",
                [["दाडिम", "pomegranate (Punica granatum)"], ["सिद्ध", "cooked"],
                 ["अर्जुन", "Terminalia arjuna"], ["सर्पिः", "ghee"]],
                "दाडिम and अर्जुन carry standard identifications in the data; the ghee (सर्पिः) is cooked (सिद्ध) with them.",
                "दाडिम, अर्जुन: standard identifications; सिद्ध = cooked; सर्पिः = ghee.", role="extend"),
          "The ghee is cooked (सिद्धम्) with the plants of the list: dāḍima is pomegranate, arjuna Terminalia arjuna."),
        mcq("discriminate", 3, "By the probable sense on the card, what is kuṇapa-retas?",
            ("Corpse-smelling semen", "कुणप = corpse; the usual understanding is a corpse-like smell (probable)."),
            [("Semen with knots or lumps", "That is granthi-retas, in unit 68."),
             ("Semen containing pus", "That is pūya-retas, in unit 68."),
             ("Semen with urine and feces", "That is mūtra-purīṣa-retas, in unit 69.")],
            "Literally corpse-semen; the card takes it, as probable, as semen smelling like a corpse.",
            "कुणप = corpse; कुणपरेतस् = corpse-like (smelling) semen, probable."),
        mcq("apply", 4, "What does the causative form पाययेत् tell us here?",
            ("One should make him drink it", "पाययेत् is the causative optative of √पा: should make (him) drink."),
            [("It should be poured on him", "√पा means to drink; nothing is poured."),
             ("He should drink it after a month", "No time is given in the unit."),
             ("It should be held in the mouth", "Holding (धारण) belongs to unit 71.")],
            "पाययेत् = should cause to drink; the plain form would be पिबेत् (should drink), as in unit 71.",
            "पाययेत् (causative) = make drink; पिबेत् = drink."),
        T(mcq("transfer", 5, "An invented line reads बालं क्षीरं पाययेत्. What does it say?",
              ("Make the child drink milk", "पाययेत् is causative: make (the child) drink."),
              [("The child should drink milk on his own", "That would be बालः क्षीरं पिबेत्, the plain verb."),
               ("One should give milk to the cow", "बालम् is the child, not a cow."),
               ("The child should not drink milk", "There is no न (not) in the line.")],
              "As सर्पिः पाययेत् = make him drink ghee, बालं क्षीरं पाययेत् = make the child drink milk.",
              "पाययति (causative of √पा) = makes (someone) drink something."),
          "The causative पाययति takes both the drinker and the drink in the accusative: make X drink Y."),
    ],
}

# ---------------------------------------------------------------- unit 68
AUTHORED["68"] = {
    "title": "ग्रन्थिरेतसि पाषाणभिदा",
    "question": "What does unit 68 name for granthi-retas and for pūya-retas?",
    "rule": ("For granthi-retas (semen with knots or lumps): pāṣāṇabhid, or the ash of palāśa. For pūya-retas (semen with "
             "pus): the two groups beginning with parūṣaka and with nyagrodha."),
    "limits": ("Elliptical: no verb and no form of use (decoction, paste ...) is stated; the verb of unit 67 may be carried over, "
               "but none is supplied. The members of the two groups are not given. पाषाणभिद् = Bergenia ligulata is probable only. "
               "The printed ग्रंधि is read as ग्रन्थि."),
    "explain_hi": ("इस इकाई में दो छपी पंक्तियाँ हैं, दोनों में क्रिया नहीं है। ग्रन्थि-रेतस् यानी गाँठ वाले शुक्र में पाषाणभिद् "
                   "(सम्भवतः पखानभेद) या पलाश (ढाक) की भस्म बताई गई है। "
                   "पूय-रेतस् यानी पीब वाले शुक्र में दो गण: परूषक (फालसा) आदि और न्यग्रोध (बरगद) आदि; ‘आदिभ्याम्’ का द्विवचन "
                   "इन्हीं दो गणों को बताता है। गणों के सदस्य यहाँ नहीं दिए गए, और प्रयोग का रूप भी नहीं।"),
    "hook": "गाँठ वाला शुक्र: पाषाणभिद् (सम्भवतः पखानभेद) या ढाक-भस्म; पीब वाला: फालसा-गण और बरगद-गण।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 68, what is named for granthi-retas?",
            ("Pāṣāṇabhid, or palāśa ash", "पाषाणभिदा पलाशभस्मना वा: with pāṣāṇabhid or with palāśa ash."),
            [("Candana, given as a decoction", "Candana is named for an ārtava fault in unit 71."),
             ("Triphalā, as a paste", "Triphalā belongs to unit 71."),
             ("Hiṅgu, cooked together with citraka", "Hiṅgu and citraka are named in unit 69.")],
            "For semen with knots or lumps: pāṣāṇabhid, or the ash of palāśa.",
            "ग्रन्थिरेतस् → पाषाणभिद् / पलाशभस्म."),
        match(1, "Match each word of unit 68 to its meaning on the card.",
              [["ग्रन्थि", "knot, lump"], ["पूय", "pus"], ["भस्म", "ash"], ["न्यग्रोध", "banyan (Ficus benghalensis)"]],
              "ग्रन्थि and पूय name the two faults; भस्म and न्यग्रोध belong to the remedies.",
              "ग्रन्थि = knot; पूय = pus; भस्म = ash; न्यग्रोध = banyan."),
        T(order(2, "Put these words of unit 68 in their printed order.",
                ["ग्रन्थिरेतसि", "पाषाणभिदा", "पलाशभस्मना", "पूयरेतसि", "परूषकादिन्यग्रोधादिभ्याम्"],
                "Fault, then its two remedies; second fault, then its two groups.",
                "ग्रन्थिरेतसि → पाषाणभिदा → पलाशभस्मना → पूयरेतसि → परूषकादि-न्यग्रोधादि.", role="extend"),
          "Each line names a fault in the locative (-रेतसि, in ... semen) and then the remedy in the instrumental."),
        mcq("discriminate", 3, "What does the card take the dual ending of परूषकादिन्यग्रोधादिभ्याम् to mean?",
            ("Two drug groups: parūṣaka-, nyagrodha-", "आदि = beginning with; the dual counts the two named groups."),
            [("Two doses, morning and evening", "No dose or time is given."),
             ("Two persons, the woman and the man", "That dual is स्त्रीपुंसौ of unit 72."),
             ("Two single plants, with no others at all", "आदि (beginning with) marks groups, not single plants.")],
            "परूषकादि and न्यग्रोधादि are two groups; the dual ending is read once, on the second.",
            "X-आदि = X and the like; the dual -भ्याम् = by the two."),
        multi("apply", 4, "Which does unit 68 state?",
              [("For granthi-retas, pāṣāṇabhid is named", "Right: पाषाणभिदा."),
               ("Palāśa ash is the alternative for granthi-retas", "Right: पलाशभस्मना वा, or with palāśa ash."),
               ("The members of the nyagrodha group are listed", "No member is listed; only the group's name."),
               ("The remedies are to be drunk", "No verb is stated in this unit.")],
              [0, 1],
              "The unit names the drugs only; how they are used and the group members are not given.",
              "वा = or: pāṣāṇabhid, or palāśa ash."),
        T(mcq("transfer", 5, "By the join of परूषक + आदि, how is चन्दन + आदि written?",
              ("चन्दनादि", "अ + आ → आ, as in परूषक + आदि → परूषकादि."),
              [("चन्दनेदि", "अ + आ does not give ए."),
               ("चन्दनोदि", "ओ comes from अ + उ, not अ + आ."),
               ("चन्दनआदि", "Two vowels meeting in a compound must join.")],
              "परूषक + आदि → परूषकादि; so चन्दन + आदि → चन्दनादि (candana and the like).",
              "अ + आ → आ."),
          "A final अ and an initial आ merge into one long आ."),
    ],
}

# ---------------------------------------------------------------- unit 69
AUTHORED["69"] = {
    "title": "मूत्रपुरीषरेतसि वायुनाऽतिविकृते",
    "question": "What two preparations does unit 69 give for mūtra-purīṣa-retas greatly altered by Vāyu?",
    "rule": ("For mūtra-purīṣa-retas greatly altered by Vāyu: hiṅgu, (probably) uśīra and citraka; or else the one cooked with "
             "citraka, vitunnaka, priyaṅgu, hiṅgu, samaṅgā and mṛṇāla, with elā and moca powder as the addition."),
    "limits": ("Low confidence. The sense of mūtra-purīṣa-retas (semen with urine and feces) is probable only. The printed शीर is "
               "read as उशीर by conjecture; no question rests on it. No verb; what is cooked is not named. Vitunnaka, samaṅgā and "
               "moca are of disputed identity."),
    "explain_hi": ("यह एक लम्बी, बिना क्रिया की गद्य-पंक्ति है। मूत्र-पुरीष-रेतस् (सम्भवतः मूत्र और मल के लक्षण वाला शुक्र), जो वायु से "
                   "अत्यन्त विकृत हो, उसके लिए दो विकल्प हैं। पहला: हींग, चित्रक, और बीच का शब्द जो अनुमान से उशीर (खस) पढ़ा गया। "
                   "दूसरा, ‘अथवा’ के बाद: चित्रक, वितुन्नक, प्रियंगु, हींग, समंगा और मृणाल से सिद्ध किया हुआ, ऊपर से एला और मोच का "
                   "चूर्ण डालकर (प्रतीवाप)। क्या पकाया जाए, यह नहीं बताया; चित्रक और हींग दोनों सूचियों में हैं।"),
    "hook": "वायु से बिगड़ा शुक्र: हींग-चित्रक, या छह द्रव्यों का सिद्ध योग, ऊपर एला-मोच का चूर्ण।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 69, by what has the semen been greatly altered?",
            ("By Vāyu (वायुना)", "वायुनाऽतिविकृते: greatly altered by Vāyu, the wind."),
            [("By Pitta (heat)", "Pitta is not named in this unit."),
             ("By Kapha", "Kapha is not named in this unit."),
             ("By the blood (rakta)", "Blood is not named in this unit.")],
            "The fault is mūtra-purīṣa-retas that Vāyu has greatly altered.",
            "वायुना = by Vāyu; अतिविकृत = greatly altered."),
        order(1, "Put the six drugs of the second (cooked) list in their printed order.",
              ["चित्रक", "वितुन्नक", "प्रियङ्गु", "हिङ्गु", "समङ्गा", "मृणाल"],
              "After अथवा the compound runs citraka, vitunnaka, priyaṅgu, hiṅgu, samaṅgā, mṛṇāla, then सिद्धम् (cooked).",
              "चित्रक → वितुन्नक → प्रियङ्गु → हिङ्गु → समङ्गा → मृणाल."),
        T(match(2, "Match each word of unit 69 to its meaning on the card.",
                [["अथवा", "or else"], ["सिद्ध", "cooked"], ["चूर्ण", "powder"], ["प्रतीवाप", "addition"],
                 ["अतिविकृत", "greatly altered"]],
                "These words build the second preparation: or else, cooked, with powder as the addition.",
                "अथवा, सिद्ध, चूर्ण, प्रतीवाप, अतिविकृत.", role="extend"),
          "प्रतीवाप is an addition put into a cooked preparation; here it is the powder of elā and moca."),
        mcq("discriminate", 3, "Which two drugs stand in both lists of unit 69, as printed?",
            ("Citraka and hiṅgu", "Both are in the first list and again in the cooked list."),
            [("Elā and moca", "These two are only the added powder."),
             ("Samaṅgā and mṛṇāla", "These two are only in the cooked list."),
             ("Vitunnaka and priyaṅgu", "These two are only in the cooked list.")],
            "First list: hiṅgu, (uśīra), citraka; second: citraka, vitunnaka, priyaṅgu, hiṅgu, samaṅgā, mṛṇāla.",
            "Citraka and hiṅgu recur in both lists."),
        mcq("apply", 4, "In the second preparation of unit 69, what part do elā and moca play?",
            ("Their powder is the addition", "एलामोचचूर्णप्रतीवापम्: with elā-moca powder as the addition."),
            [("They are cooked with the six drugs", "The six drugs are the cooked list; elā and moca come as powder."),
             ("They make up the whole first list", "The first list is hiṅgu, (uśīra), citraka."),
             ("They are taken alone, instead", "They are named only as the addition.")],
            "The six drugs make the cooked preparation; elā and moca powder is added to it.",
            "प्रतीवाप = addition (of a powder)."),
        T(mcq("transfer", 5, "By the join in चित्रकैरथवा, how is फलैः + अथवा written?",
              ("फलैरथवा", "Visarga after ऐ becomes र् before a vowel, as in चित्रकैः + अथवा."),
              [("फलैथवा", "The अ of अथवा cannot vanish here."),
               ("फलैश्थवा", "Visarga becomes श् only before a palatal consonant (च, छ, श), never before a vowel."),
               ("फलै अथवा", "Visarga after ऐ does not drop before a vowel; it becomes र्.")],
              "चित्रकैः + अथवा → चित्रकैरथवा; so फलैः + अथवा → फलैरथवा.",
              "ऐः + vowel → ऐर् + vowel."),
          "A visarga after ऐ (any vowel but अ/आ) becomes र् before a vowel."),
    ],
}

# ---------------------------------------------------------------- unit 70
AUTHORED["70"] = {
    "title": "तथा ग्रन्थ्यार्तवे",
    "question": "What decoction does unit 70 give for granthi-ārtava?",
    "rule": "Likewise, in granthi-ārtava (menstrual blood with knots or lumps): a decoction of pāṭhā, trikaṇṭaka and vṛkṣaka.",
    "limits": ("Elliptical: the verb is not stated here (पिबेत् stands in the next unit) and none is supplied. All three "
               "identifications are probable only; the part used of each is not stated. The line is not metrical."
               ""),
    "explain_hi": ("‘तथा’ (उसी प्रकार) से पाठ शुक्र-दोषों से आर्तव-दोषों पर आता है। ग्रन्थि-आर्तव यानी गाँठ वाले आर्तव में पाठा, "
                   "त्रिकण्टक (सम्भवतः गोखरू) और वृक्षक (सम्भवतः कुटज) का क्वाथ बताया गया है। "
                   "‘ग्रन्थ्यार्तवे’ में ग्रन्थि + आर्तवे की सन्धि है: इ + आ → या। "
                   "क्रिया यहाँ नहीं है; अंगों (जड़, छाल आदि) का भी उल्लेख नहीं।"),
    "hook": "गाँठ वाला आर्तव: पाठा, त्रिकण्टक, वृक्षक (सम्भवतः गोखरू, कुटज) का काढ़ा।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 70, in what form are pāṭhā, trikaṇṭaka and vṛkṣaka given?",
            ("As a decoction (क्वाथ)", "…वृक्षकक्वाथम्: the decoction of these three."),
            [("As a paste (कल्क)", "Paste (कल्क) is named in units 71 and 73."),
             ("As an ash (भस्म)", "Ash is named for palāśa in unit 68."),
             ("As a fine powder (चूर्ण)", "Powder is named in unit 69.")],
            "The compound ends in क्वाथम्: a decoction of pāṭhā, trikaṇṭaka and vṛkṣaka.",
            "क्वाथ = decoction."),
        order(1, "Put the members of the compound of unit 70 in their printed order.",
              ["पाठा", "त्रिकण्टक", "वृक्षक", "क्वाथ"],
              "The three drugs come first, then क्वाथ (decoction) closes the compound.",
              "पाठा → त्रिकण्टक → वृक्षक → क्वाथ."),
        T(match(2, "Match each word of unit 70 to its meaning on the card.",
                [["पाठा", "Cissampelos pareira (probable)"], ["त्रिकण्टक", "Tribulus terrestris (probable)"],
                 ["वृक्षक", "kuṭaja (probable)"], ["तथा", "likewise"]],
                "The three plant identifications are probable in the data; तथा links this to the faults before.",
                "पाठा, त्रिकण्टक, वृक्षक (all probable); तथा = likewise.", role="extend"),
          "The three drugs are identified as probable only: pāṭhā Cissampelos pareira, trikaṇṭaka Tribulus terrestris, vṛkṣaka kuṭaja."),
        mcq("discriminate", 3, "Which split of ग्रन्थ्यार्तवे is right?",
            ("ग्रन्थि + आर्तवे", "इ before a different vowel becomes य्: ग्रन्थि + आर्तवे → ग्रन्थ्यार्तवे."),
            [("ग्रन्थ + यार्तवे", "यार्तवे is not a word of the card."),
             ("ग्रन्थी + अर्तवे", "ई + short अ would give ग्रन्थ्यर्तवे, with a short a."),
             ("ग्रन्थिम् + आर्तवे", "म् before आ would give ग्रन्थिमार्तवे.")],
            "ग्रन्थि (knot) + आर्तवे (in ārtava).",
            "इ + आ → य् + आ."),
        mcq("apply", 4, "The ārtava fault of unit 70 shares its first member with which semen fault of unit 68?",
            ("Granthi-retas", "Both are named with ग्रन्थि, knot or lump."),
            [("Pūya-retas", "Pūya (pus) appears with ārtava in unit 71, not here."),
             ("Kuṇapa-retas", "Kuṇapa is the fault of unit 67."),
             ("Mūtra-purīṣa-retas", "That is the fault of unit 69.")],
            "Unit 68 treats ग्रन्थिरेतस्; unit 70 turns to ग्रन्थ्यार्तव: the same knot, now in ārtava.",
            "ग्रन्थि-रेतस् (unit 68) ↔ ग्रन्थि-आर्तव (unit 70)."),
        T(mcq("transfer", 5, "By the join of ग्रन्थि + आर्तवे, how is प्रति + आगच्छति written?",
              ("प्रत्यागच्छति", "इ + आ → य् + आ, as in ग्रन्थ्यार्तवे."),
              [("प्रतागच्छति", "The इ cannot vanish; it turns into य्."),
               ("प्रतेगच्छति", "इ + आ does not give ए."),
               ("प्रतियागच्छति", "य् replaces the इ; the इ does not remain.")],
              "ग्रन्थि + आर्तवे → ग्रन्थ्यार्तवे; so प्रति + आगच्छति → प्रत्यागच्छति (comes back).",
              "इ + a different vowel → य् + that vowel."),
          "A final इ before a different vowel becomes य्."),
    ],
}

# ---------------------------------------------------------------- unit 71
AUTHORED["71"] = {
    "title": "कुणपपूयार्तवे चन्दनक्वाथम्",
    "question": "What does unit 71 give to drink in kuṇapa-pūya-ārtava, and what else is named here?",
    "rule": ("In kuṇapa-pūya-ārtava one should drink a decoction of candana; and here also the paste and decoction of "
             "triphalā, holding (dhāraṇa) and sipping or rinsing (ācamana)."),
    "limits": ("The last clause is two verbless duals; which of paste and decoction goes with holding or sipping is not "
               "stated, so the card does not pair them. Kuṇapa as smell is probable; candana's kind is not stated. "
               "Ācamana is sipping (or rinsing the mouth), not a yoni wash."),
    "explain_hi": ("कुणप-पूय-आर्तव यानी (सम्भवतः) शव जैसी गन्ध और पीब वाले आर्तव में चन्दन का क्वाथ पीना है। "
                   "फिर ‘चात्र’ (और यहाँ): त्रिफला (हरड़, बहेड़ा, आँवला) का कल्क और क्वाथ, तथा धारण और आचमन। "
                   "ये दो द्विवचन बिना क्रिया के साथ-साथ रखे हैं; कौन किसके साथ जाए, पाठ नहीं बताता, इसलिए यहाँ जोड़ी नहीं बनाई गई। "
                   "आचमन मुख्यतः घूँट लेना (मुँह धोना भी) है, योनि-प्रक्षालन नहीं।"),
    "hook": "चन्दन का काढ़ा पियो; त्रिफला: कल्क और काढ़ा, धारण और आचमन।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 71, what should one drink in kuṇapa-pūya-ārtava?",
            ("A decoction of candana", "चन्दनक्वाथं पिबेत्: one should drink a candana decoction."),
            [("Ghee cooked with dāḍima", "Ghee with dāḍima belongs to unit 67."),
             ("The ash of palāśa", "Palāśa ash belongs to unit 68."),
             ("A decoction of pāṭhā", "Pāṭhā decoction belongs to unit 70.")],
            "The first clause: in this ārtava fault, drink a decoction of candana.",
            "चन्दनक्वाथ = candana decoction; पिबेत् = should drink."),
        match(1, "Match each word of unit 71 to its meaning on the card.",
              [["कल्क", "paste"], ["क्वाथ", "decoction"], ["धारण", "holding, retaining"],
               ["आचमन", "sipping (also rinsing the mouth)"]],
              "Two forms of triphalā (paste, decoction) and two acts (holding, sipping) are named.",
              "कल्क = paste; क्वाथ = decoction; धारण = holding; आचमन = sipping."),
        T(order(2, "Put these words of unit 71 in their printed order.",
                ["कुणपपूयार्तवे", "चन्दनक्वाथम्", "पिबेत्", "त्रिफलाकल्कक्वाथौ", "धारणाचमने"],
                "Fault, decoction, verb; then the triphalā pair and the pair of acts.",
                "कुणपपूयार्तवे → चन्दनक्वाथम् → पिबेत् → त्रिफलाकल्कक्वाथौ → धारणाचमने.", role="extend"),
          "The unit has one full sentence (with पिबेत्) and then a verbless clause of two duals."),
        mcq("discriminate", 3, "Does unit 71 say which of paste and decoction goes with holding, and which with sipping?",
            ("No; no pairing is stated", "Two duals with no verb; the pairing is not stated."),
            [("Yes; the paste is for sipping", "No pairing is stated in the text."),
             ("Yes; the decoction is for holding", "No pairing is stated in the text."),
             ("Yes; both go only with holding", "आचमन is named too, and no pairing is given.")],
            "त्रिफलाकल्कक्वाथौ and धारणाचमने stand together; the card does not claim who goes with whom.",
            "Two duals listed, no verb, no stated pairing."),
        mcq("apply", 4, "Which is not one of the three myrobalans of triphalā as the card names them?",
            ("Candana", "Candana is the separate decoction to drink, not part of triphalā."),
            [("Harītakī", "Harītakī is one of the three."),
             ("Bibhītaka", "Bibhītaka is one of the three."),
             ("Āmalaka", "Āmalaka is one of the three.")],
            "Triphalā = harītakī, bibhītaka and āmalaka (standard).",
            "त्रिफला = the three fruits: harītakī, bibhītaka, āmalaka."),
        T(mcq("transfer", 5, "By the join of च + अत्र, how is न + अस्ति written?",
              ("नास्ति", "अ + अ → आ, as in च + अत्र → चात्र."),
              [("नेस्ति", "अ + अ does not give ए."),
               ("नोस्ति", "ओ comes from अ + उ, not अ + अ."),
               ("नअस्ति", "The two vowels must join.")],
              "च + अत्र → चात्र; so न + अस्ति → नास्ति (is not).",
              "अ + अ → आ."),
          "Two short अ sounds meeting merge into one long आ."),
    ],
}

# ---------------------------------------------------------------- unit 72
AUTHORED["72"] = {
    "title": "सर्वेषु च शुक्रार्तवदोषेषु",
    "question": "How does unit 72 say all faults of semen and ārtava are to be treated, and whom?",
    "rule": ("In all faults of semen and ārtava one should treat both the woman and the man, again and again, with the actions "
             "beginning with sneha (oleation), especially with uttarabasti."),
    "limits": ("The actions that follow sneha are not listed here. The number of uttarabastis and their contents are not stated. "
               "The printed सर्वेषुच is सर्वेषु च."),
    "explain_hi": ("यह पंक्ति शुक्र और आर्तव के सभी दोषों के लिए एक सामान्य नियम देती है। ‘स्त्रीपुंसौ’ द्विवचन है: स्त्री और पुरुष, दोनों "
                   "का उपचार करना है। उपचार स्नेह (तेल या वसा) से आरम्भ होने वाले कर्मों से, और विशेष रूप से उत्तरबस्ति से। "
                   "‘पुनः पुनः’ यानी बार-बार; पहला ‘पुनः’ छपाई में ‘उत्तरबस्तिभिः’ से जुड़ा है। "
                   "स्नेह के बाद कौन-से कर्म, यह सूची यहाँ नहीं दी गई।"),
    "hook": "दोष किसी का भी: दोनों का उपचार, स्नेह से शुरू, उत्तरबस्ति ख़ास, बार-बार।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 72, who is to be treated in all faults of semen and ārtava?",
            ("Both the woman and the man", "स्त्रीपुंसौ is a dual: the woman and the man, both."),
            [("Only the woman", "The dual स्त्रीपुंसौ names both."),
             ("Only the man", "The dual स्त्रीपुंसौ names both."),
             ("The child who is to be born", "No child is named in this unit.")],
            "स्त्रीपुंसौ … उपाचरेत्: one should treat the woman and the man.",
            "स्त्रीपुंसौ = the woman and the man (dual)."),
        order(1, "Put these words of unit 72 in their printed order.",
              ["सर्वेषु", "शुक्रार्तवदोषेषु", "स्त्रीपुंसौ", "स्नेहादिकर्मभिः", "उत्तरबस्तिभिः", "उपाचरेत्"],
              "In all faults of semen and ārtava → the couple → with sneha and the rest → uttarabasti → should treat.",
              "सर्वेषु → दोषेषु → स्त्रीपुंसौ → स्नेहादिकर्मभिः → उत्तरबस्तिभिः → उपाचरेत्."),
        T(match(2, "Match each word of unit 72 to its meaning on the card.",
                [["स्नेहादिकर्म", "actions beginning with sneha"], ["विशेषेण", "especially"],
                 ["पुनः पुनः", "again and again"], ["उपाचरेत्", "should treat"]],
                "These words give the means, the stress, the repetition and the verb.",
                "स्नेहादिकर्म, विशेषेण, पुनः पुनः, उपाचरेत्.", role="extend"),
          "स्नेह = oleation with oil or fat; स्नेहादि = the series of actions that begins with it."),
        mcq("discriminate", 3, "Which split of विशेषेणोत्तरबस्तिभिः is right?",
            ("विशेषेण + उत्तरबस्तिभिः", "अ + उ → ओ: विशेषेण + उत्तर → विशेषेणोत्तर."),
            [("विशेषेणो + उत्तरबस्तिभिः", "विशेषेणो is no word; the ओ comes from अ + उ."),
             ("विशेषेणम् + उत्तरबस्तिभिः", "म् before उ would give विशेषेणमुत्तर…"),
             ("विशेषेण + ओत्तरबस्तिभिः", "ओत्तरबस्ति is no word; the word is उत्तरबस्ति.")],
            "विशेषेण (especially) + उत्तरबस्तिभिः (with uttarabastis).",
            "अ + उ → ओ."),
        mcq("apply", 4, "Which treatment does unit 72 single out with विशेषेण (especially)?",
            ("Uttarabasti", "विशेषेणोत्तरबस्तिभिः: especially with uttarabastis."),
            [("Picu wads in the yoni", "Picu is named in unit 73."),
             ("Triphalā paste", "Triphalā belongs to unit 71."),
             ("Candana decoction", "Candana belongs to unit 71.")],
            "Among the actions beginning with sneha, uttarabasti is named as especially to be used.",
            "विशेषेण उत्तरबस्तिभिः = especially with uttarabasti."),
        T(mcq("transfer", 5, "An invented line reads गुरुशिष्यौ वदतः. What does it say?",
              ("The teacher and the pupil speak", "A dual dvandva names both, like स्त्रीपुंसौ; वदतः is dual too."),
              [("The teacher speaks to the pupil", "Both are subjects; no 'to' is expressed."),
               ("The teachers of the pupil speak", "-औ is a dual dvandva, not a genitive."),
               ("Two teachers speak", "The dvandva names two different persons, teacher and pupil.")],
              "As स्त्रीपुंसौ = the woman and the man, गुरुशिष्यौ = the teacher and the pupil.",
              "A dvandva of two nouns in the dual = both of them."),
          "A dvandva compound of two nouns takes the dual and names both together."),
    ],
}

# ---------------------------------------------------------------- unit 73
AUTHORED["73"] = {
    "title": "यथास्वं च योनौ",
    "question": "What does unit 73 add to the treatment of unit 72?",
    "rule": "And in the yoni, as suited to each: with pastes (kalka) and with picu (cotton-wool wads).",
    "limits": ("The unit has no verb; it appears to continue unit 72 (उपाचरेत् carried over). Which paste suits which fault is not "
               "stated (यथास्वम्)."),
    "explain_hi": ("यह छोटी पंक्ति इकाई ७२ के वाक्य को आगे बढ़ाती लगती है; क्रिया ‘उपाचरेत्’ वहीं से समझी जाती है। "
                   "योनि में, जिसके लिए जो उचित हो (यथास्वम्), कल्कों और पिचुओं से उपचार। पिचु यानी रूई का फाहा (मानक)। "
                   "कौन-सा कल्क किस दोष के लिए, यह यहाँ नहीं कहा।"),
    "hook": "भीतर का उपचार: यथायोग्य कल्क और रूई के फाहे।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 73, where are the pastes and the picu used?",
            ("In the yoni", "योनौ: in the yoni (vagina)."),
            [("In the mouth", "Sipping (ācamana) was in unit 71; here it is the yoni."),
             ("On the head", "The head is not named."),
             ("On the navel", "The navel is not named.")],
            "योनौ कल्कैः पिचुभिश्च: in the yoni, with pastes and picu.",
            "योनौ = in the yoni."),
        order(1, "Put the words of unit 73 in their printed order.",
              ["यथास्वम्", "योनौ", "कल्कैः", "पिचुभिः"],
              "As suited to each → in the yoni → with pastes → with picu.",
              "यथास्वम् → योनौ → कल्कैः → पिचुभिः."),
        T(match(2, "Match each word of unit 73 to its meaning on the card.",
                [["यथास्वम्", "as suited to each"], ["योनौ", "in the yoni"], ["कल्क", "paste"],
                 ["पिचु", "cotton-wool wad"]],
                "Four words: the manner, the place, and the two means.",
                "यथास्वम्, योनौ, कल्क, पिचु.", role="extend"),
          "पिचु is a wad or swab of cotton (standard)."),
        mcq("discriminate", 3, "Which split of पिचुभिश्च is right?",
            ("पिचुभिः + च", "Visarga becomes श् before च: पिचुभिः + च → पिचुभिश्च."),
            [("पिचुभि + श्च", "श्च is no word."),
             ("पिचुभिम् + च", "म् before च would be written पिचुभिं च."),
             ("पिचुभिश + च", "पिचुभिश is no word; the ending is -भिः.")],
            "पिचुभिः (with picu) + च (and).",
            "Visarga + च → श्च."),
        mcq("apply", 4, "Unit 73 has no verb. Which verb does the card take as carried over?",
            ("उपाचरेत् (should treat) of unit 72", "The unit appears to continue unit 72, whose verb is उपाचरेत्."),
            [("पिबेत् (should drink) of unit 71", "Pastes and wads in the yoni are not drunk."),
             ("पाययेत् (make drink) of unit 67", "Unit 67 is a separate prescription."),
             ("आसेवेताम् (the two should follow) of unit 74", "That verb comes after this unit.")],
            "The card's grouping note: the unit appears to continue unit 72; its verb उपाचरेत् is understood.",
            "Verbless unit → verb carried from the unit it continues."),
        T(mcq("transfer", 5, "By the join in पिचुभिश्च, how is रामः + च written?",
              ("रामश्च", "Visarga becomes श् before च."),
              [("रामर्च", "र् replaces visarga only after other vowels before voiced sounds."),
               ("रामोच", "अः → ओ only before voiced sounds; च is unvoiced."),
               ("रामस्च", "स् comes before त/थ; before च it is श्.")],
              "पिचुभिः + च → पिचुभिश्च; so रामः + च → रामश्च.",
              "Visarga + च/छ → श्."),
          "A visarga before च or छ becomes श्."),
    ],
}

# ---------------------------------------------------------------- unit 74
AUTHORED["74"] = {
    "title": "इत्येवं विशुद्धशुक्रार्तवौ",
    "question": "What should the purified couple do, and how long is the ṛtu by unit 74?",
    "rule": ("The two whose semen and ārtava are thus purified should follow the procedure stated earlier. The ṛtu is the one "
             "with ārtava seen, and it lasts twelve nights."),
    "limits": ("'The procedure stated earlier' is not described here. The sense of ṛtu as the woman's season for conception is "
               "probable. Other views on the length follow in units 75 to 77."),
    "explain_hi": ("इस इकाई में दो छपी पंक्तियाँ हैं। पहली: इस प्रकार जिन दोनों (पुरुष और स्त्री) के शुक्र और आर्तव शुद्ध हो गए, वे पहले कही "
                   "गई विधि का पालन करें; ‘आसेवेताम्’ द्विवचन है। दूसरी: ऋतु तो वह है जिसमें आर्तव दिखाई दे, और वह बारह रात तक "
                   "रहता है। ऋतु का अर्थ यहाँ सम्भवतः गर्भधारण योग्य काल है। "
                   "आगे की इकाइयाँ (७५-७७) दूसरों के मत देती हैं।"),
    "hook": "शुद्ध हुए दोनों, अब विधि; ऋतु: आर्तव दिखे, बारह रात।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 74, how long does the ṛtu last?",
            ("Twelve nights", "द्वादशरात्रं भवति: it lasts twelve nights."),
            [("Sixteen nights", "Sixteen is the view of others in unit 75."),
             ("A whole month", "A month is the view of some in unit 76."),
             ("Seven nights", "Seven is not named.")],
            "ऋतुस्तु दृष्टार्तवो द्वादशरात्रं भवति: twelve nights.",
            "द्वादशरात्र = twelve nights."),
        order(1, "Put these phrases of unit 74 in their printed order.",
              ["इत्येवम्", "विशुद्धशुक्रार्तवौ", "पूर्वोक्तं विधिम्", "आसेवेताम्", "ऋतुस्तु दृष्टार्तवः", "द्वादशरात्रं भवति"],
              "Line 1: thus, the purified two, the earlier procedure, should follow. Line 2: the ṛtu, seen ārtava, twelve nights.",
              "इत्येवम् → विशुद्ध… → पूर्वोक्तं विधिम् → आसेवेताम् → ऋतुः → द्वादशरात्रम्."),
        T(match(2, "Match each word of unit 74 to its meaning on the card.",
                [["विशुद्ध", "purified"], ["पूर्वोक्त", "stated earlier"], ["आसेवेताम्", "the two should follow"],
                 ["दृष्टार्तव", "with ārtava seen"], ["द्वादशरात्र", "twelve nights"]],
                "Three words belong to line 1, two to line 2.",
                "विशुद्ध, पूर्वोक्त, आसेवेताम्, दृष्टार्तव, द्वादशरात्र.", role="extend"),
          "आसेवेताम् is a dual verb: the two (man and woman) should follow (practise) the procedure."),
        mcq("discriminate", 3, "Which split of पूर्वोक्तम् is right?",
            ("पूर्व + उक्तम्", "अ + उ → ओ: पूर्व + उक्तम् → पूर्वोक्तम्."),
            [("पूर्वो + क्तम्", "क्तम् is no word; the second word is उक्तम्."),
             ("पूर्वम् + उक्तम्", "म् before उ would give पूर्वमुक्तम्."),
             ("पूर्व + ओक्तम्", "ओक्तम् is no word; the ओ comes from अ + उ.")],
            "पूर्व (earlier) + उक्तम् (stated).",
            "अ + उ → ओ."),
        mcq("apply", 4, "Who are the two that should follow the earlier procedure (आसेवेताम्)?",
            ("The purified man and woman", "The bahuvrīhi describes two persons, the couple treated in unit 72."),
            [("The physician and the patient", "The compound describes persons whose semen and ārtava are purified."),
             ("Two women who are in their ṛtu", "Semen belongs to the man; the two are a couple."),
             ("Semen and ārtava themselves", "The compound is a bahuvrīhi: persons having them, not the fluids.")],
            "विशुद्धशुक्रार्तवौ = the two whose semen and ārtava are purified: the man and the woman.",
            "Bahuvrīhi in the dual = the two persons who have X."),
        T(mcq("transfer", 5, "By the join in ऋतुस्तु, how is गुरुः + तु written?",
              ("गुरुस्तु", "Visarga becomes स् before त, as in ऋतुः + तु → ऋतुस्तु."),
              [("गुरुर्तु", "र् replaces visarga before voiced sounds; त is unvoiced."),
               ("गुरोतु", "No ओ arises here; the visarga turns into स्."),
               ("गुरुश्तु", "श् replaces visarga before च or छ, not before त.")],
              "ऋतुः + तु → ऋतुस्तु; so गुरुः + तु → गुरुस्तु.",
              "Visarga + त/थ → स्."),
          "A visarga before त or थ becomes स्."),
    ],
}

# ---------------------------------------------------------------- unit 75
AUTHORED["75"] = {
    "title": "षोडशरात्रमित्यन्ये",
    "question": "What length of the ṛtu do others give in unit 75?",
    "rule": "According to others, (the ṛtu lasts) sixteen nights.",
    "limits": "No verb; the subject (the ṛtu of unit 74) is understood. The unit reports others' view and does not judge it.",
    "explain_hi": ("यह तीन शब्दों की गद्य-पंक्ति है: ‘षोडशरात्रम् इति अन्ये’। ‘इति अन्ये’ बताता है कि यह दूसरों का मत है। "
                   "इकाई ७४ में ऋतु बारह रात का था; यहाँ अन्य आचार्यों के अनुसार सोलह रात। "
                   "‘इत्यन्ये’ में इति + अन्ये की सन्धि है: इ + अ → य।"),
    "hook": "हम: बारह रात; अन्ये: सोलह।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "According to others in unit 75, how long is the ṛtu?",
            ("Sixteen nights", "षोडशरात्रम् इति अन्ये: sixteen nights, say others."),
            [("Twelve nights", "Twelve nights is the statement of unit 74."),
             ("A whole month", "A month is the view of some, in unit 76."),
             ("Ten nights", "Ten is not named.")],
            "Others give sixteen nights.",
            "षोडश = sixteen; अन्ये = others."),
        match(1, "Match each word of unit 75 to its meaning on the card.",
              [["षोडश", "sixteen"], ["रात्र", "night(s)"], ["इति", "thus (marks a quoted view)"], ["अन्ये", "others"]],
              "The whole unit: sixteen nights, thus (say) others.",
              "षोडश, रात्र, इति, अन्ये."),
        fill(2, "In unit 75 the word for others is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("अन्ये"),
             "अन्ये = others (nominative plural); इति अन्ये = so say others.",
             "अन्ये (others) marks a view held by other authorities.",
             "अन्ये = others."),
        mcq("discriminate", 3, "Which split of इत्यन्ये is right?",
            ("इति + अन्ये", "इ before अ becomes य्: इति + अन्ये → इत्यन्ये."),
            [("इत्य + अन्ये", "अ + अ would give इत्यान्ये, with a long आ."),
             ("इति + यन्ये", "यन्ये is no word."),
             ("इतिः + अन्ये", "इति is indeclinable; it has no visarga.")],
            "इति (thus) + अन्ये (others).",
            "इ + अ → य् + अ."),
        mcq("apply", 4, "How does unit 75 stand to the twelve nights of unit 74?",
            ("It adds another view", "इति अन्ये marks the view of others beside the text's own."),
            [("It corrects twelve as a misprint", "Nothing says twelve is wrong; others simply differ."),
             ("It adds sixteen to the twelve", "Sixteen is an alternative length, not a sum."),
             ("It is the text's own final ruling", "इति अन्ये reports others; it is not the text's own statement.")],
            "Unit 74: twelve nights; unit 75: sixteen nights, according to others.",
            "X इति अन्ये = X, say others."),
        T(mcq("transfer", 5, "An invented line reads दशरात्रमित्यपरे. What does it say?",
              ("Ten nights, say others", "X इति अपरे = so say others, like X इति अन्ये."),
              [("Ten nights, for other women", "अपरे is masculine nominative: other (authorities), not women."),
               ("Not ten nights, say others", "There is no न (not) in the line."),
               ("Ten other nights follow", "इति marks a quoted view, not a sequence.")],
              "Like षोडशरात्रमित्यन्ये, दशरात्रमित्यपरे = ten nights, say others.",
              "X इति अन्ये / अपरे = X, according to others."),
          "X इति अन्ये (or अपरे) reports a view held by others."),
    ],
}

# ---------------------------------------------------------------- unit 76
AUTHORED["76"] = {
    "title": "शुद्धयोनिगर्भाशयार्तवाया मासमपि",
    "question": "What length do some give in unit 76, and for which woman?",
    "rule": "But according to some, even a month, for (the woman) whose yoni, womb (garbhāśaya) and ārtava are pure.",
    "limits": ("No verb; the unit appears to continue the length of the ṛtu of units 74-75. The final visarga of the genitive "
               "(…ārtavāyāḥ) is missing in print. The unit reports an opinion."),
    "explain_hi": ("‘केचित्’ यानी कुछ लोग: उनके अनुसार ऋतु एक मास भी हो सकता है, पर उस स्त्री के लिए जिसकी योनि, गर्भाशय और आर्तव शुद्ध हों। "
                   "समास स्त्रीलिंग षष्ठी एकवचन है, इसलिए एक स्त्री समझी जाती है। गर्भाशय का शाब्दिक अर्थ है गर्भ का आशय (स्थान)। "
                   "छपाई में अन्त का विसर्ग छूटा लगता है।"),
    "hook": "कुछ कहते: शुद्ध योनि, गर्भाशय, आर्तव हो तो पूरा मास भी।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "According to some in unit 76, how long may the ṛtu be?",
            ("Even a month", "मासमपि तु केचित्: but some (say) even a month."),
            [("Twelve nights only", "Twelve nights is unit 74's statement."),
             ("Sixteen nights only", "Sixteen is the others' view of unit 75."),
             ("Two months", "Two months are not named.")],
            "Some extend it to even a month for a woman whose yoni, womb and ārtava are pure.",
            "मासम् अपि = even a month; केचित् = some."),
        order(1, "Put the members of the compound of unit 76 in their printed order.",
              ["शुद्ध", "योनि", "गर्भाशय", "आर्तव"],
              "Pure → yoni → womb → ārtava: the compound names what must be pure.",
              "शुद्ध → योनि → गर्भाशय → आर्तव."),
        T(match(2, "Match each word of unit 76 to its meaning on the card.",
                [["गर्भाशय", "womb (seat of the embryo)"], ["मास", "month"], ["अपि", "even"], ["केचित्", "some"]],
                "गर्भाशय names the organ; the rest give the length and whose view it is.",
                "गर्भाशय, मास, अपि, केचित्.", role="extend"),
          "गर्भाशय = गर्भ (embryo) + आशय (seat): the womb."),
        mcq("discriminate", 3, "For which woman do some allow even a month in unit 76?",
            ("One with pure yoni, womb, ārtava", "शुद्धयोनिगर्भाशयार्तवायाः: of her whose yoni, womb, ārtava are pure."),
            [("One who has not yet borne a child", "Childbirth is not named."),
             ("One whose ārtava is not seen", "Unseen ārtava belongs to unit 77."),
             ("One whose semen fault was treated", "Semen belongs to the man; the compound names her organs.")],
            "The condition is purity of yoni, womb and ārtava.",
            "शुद्ध + योनि + गर्भाशय + आर्तव."),
        mcq("apply", 4, "A teacher says the ṛtu may last a month for a woman with pure yoni, womb and ārtava. Whose view does he repeat?",
            ("That of some (केचित्) in unit 76", "मासमपि तु केचित्: the month is the view of some."),
            [("The text's own view in unit 74", "Unit 74 gives twelve nights."),
             ("The others (अन्ये) of unit 75", "Unit 75's others give sixteen nights."),
             ("The others (अपरे) of unit 77", "Unit 77's others speak of unseen ārtava.")],
            "Twelve nights (74), sixteen say others (75), even a month say some (76).",
            "केचित् = some: the month view of unit 76."),
        T(mcq("transfer", 5, "An invented line reads वर्षमपि तु केचित्. What does it say?",
              ("But some (say) even a year", "X अपि तु केचित् = but some (say) even X."),
              [("But some (say) not even a year", "There is no न (not) in the line."),
               ("But each year some (come)", "No verb of coming is present."),
               ("But some (say) a year at most", "अपि = even, not 'at most'.")],
              "As मासमपि तु केचित् = but some (say) even a month, वर्षमपि तु केचित् = even a year.",
              "अपि = even; केचित् = some."),
          "अपि after a word stresses it: even X; केचित् marks the view of some."),
    ],
}

# ---------------------------------------------------------------- unit 77
AUTHORED["77"] = {
    "title": "तद्वददृष्टार्तवोऽप्यस्तीत्यपरे",
    "question": "What do others say also exists in unit 77?",
    "rule": "According to others, in the same way there is also one with ārtava not seen.",
    "limits": ("The unstated noun is shown as 'one'; its masculine form fits ṛtu. What तद्वत् (in the same way) likens it to is "
               "not stated. The unit reports others' view."),
    "explain_hi": ("‘इति अपरे’ से दूसरों का मत आता है: उसी प्रकार ऐसा भी होता है जिसमें आर्तव दिखाई न दे। "
                   "‘अदृष्टार्तवः’ पुंलिंग है, इसलिए यह ऋतु के साथ मेल खाता है, पर संज्ञा पाठ में नहीं है। "
                   "इकाई ७४ में ऋतु ‘दृष्टार्तव’ था; यहाँ ‘अ-’ लगाकर ‘अदृष्टार्तव’। "
                   "‘तद्वत्’ किसकी तरह, यह नहीं बताया।"),
    "hook": "दिखे आर्तव वाला ऋतु तो है ही; अपरे कहते: न दिखे वाला भी।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "According to others in unit 77, what also exists?",
            ("One with ārtava not seen", "अदृष्टार्तवोऽप्यस्ति: there is also one with ārtava not seen."),
            [("A ṛtu of sixteen nights", "That is the view of others in unit 75."),
             ("A month for a pure woman", "That is the view of some in unit 76."),
             ("Ārtava that has knots or lumps", "Knotted ārtava is the fault of unit 70.")],
            "Others say: in the same way there is also one with unseen ārtava.",
            "अदृष्टार्तव = with ārtava not seen."),
        order(1, "Put the words of unit 77 in their printed order.",
              ["तद्वत्", "अदृष्टार्तवः", "अपि", "अस्ति", "इति", "अपरे"],
              "Likewise → not-seen-ārtava → also → is → thus → others.",
              "तद्वत् → अदृष्टार्तवः → अपि → अस्ति → इति → अपरे."),
        T(match(2, "Match each word of unit 77 to its meaning on the card.",
                [["तद्वत्", "in the same way"], ["अदृष्ट", "not seen"], ["अस्ति", "is, exists"], ["अपरे", "others"]],
                "Four words carry the claim and whose claim it is.",
                "तद्वत्, अदृष्ट, अस्ति, अपरे.", role="extend"),
          "अपरे, like अन्ये, means others: it marks a view reported, not the text's own."),
        mcq("discriminate", 3, "Which split starts तद्वददृष्टार्तवः correctly?",
            ("तद्वत् + अदृष्टार्तवः", "त् becomes द् before a vowel: तद्वत् + अ… → तद्वद…"),
            [("तद्वत् + दृष्टार्तवः", "That would be written तद्वद्दृष्ट… with two द्."),
             ("तद्व + अदृष्टार्तवः", "तद्व is no word; the word is तद्वत्."),
             ("तद्वद + अदृष्टार्तवः", "अ + अ would give तद्वदादृष्ट… with a long आ.")],
            "तद्वत् (likewise) + अदृष्टार्तवः (one with ārtava not seen).",
            "त् + vowel → द् + vowel."),
        mcq("apply", 4, "What does the अ- of अदृष्टार्तव add, against दृष्टार्तव of unit 74?",
            ("Negation: ārtava not seen", "अ- before a word denies it: अ-दृष्ट = not seen."),
            [("Stress: ārtava plainly seen", "अ- does not strengthen; it negates."),
             ("Time: ārtava seen earlier", "अ- adds no time."),
             ("Number: many ārtavas", "अ- adds no plural.")],
            "Unit 74's ṛtu is दृष्टार्तव (ārtava seen); unit 77's others add अदृष्टार्तव (not seen).",
            "अ- (before a consonant) = not."),
        T(mcq("transfer", 5, "By the join in अदृष्टार्तवोऽपि, how is रामः + अपि written?",
              ("रामोऽपि", "अः + अ → ओ, and the अ that drops is marked ऽ."),
              [("रामाऽपि", "अः + अ does not give आ."),
               ("रामरपि", "र् replaces visarga only after vowels other than अ/आ."),
               ("रामसपि", "Visarga does not become स् before a vowel.")],
              "अदृष्टार्तवः + अपि → अदृष्टार्तवोऽपि; so रामः + अपि → रामोऽपि.",
              "अः + अ → ओऽ."),
          "A visarga after अ, before अ, gives ओ; the following अ drops and is marked with ऽ."),
    ],
}

# ---------------------------------------------------------------- unit 78
AUTHORED["78"] = {
    "title": "क्षामप्रसन्नवदनाम्",
    "question": "By what signs does verse 78 say one should know a woman to be in her ṛtu?",
    "rule": ("One should know a woman to be in her ṛtu (ṛtumatī) who has a lean, clear face, throbbing hips and breasts, "
             "drooping eyes (reading probable) and belly, and desire for a man."),
    "limits": ("The printed अक्षु is read as अक्षि (eye), a possible correction; the printed पुंस्कामा is read as accusative "
               "पुंस्कामाम्. No question rests on the eye. The verse gives signs only, no cause or time."),
    "explain_hi": ("यह अनुष्टुभ् श्लोक ऋतुमती स्त्री के लक्षण देता है; सारे विशेषण द्वितीया स्त्रीलिंग में ‘स्त्रियम्’ के साथ हैं, क्रिया ‘विद्यात्’ "
                   "(जाने) है। मुख कृश और प्रसन्न, श्रोणि (कूल्हे) और पयोधर (स्तन) फड़कते हुए, आँखें (पाठ सम्भावित) और कुक्षि शिथिल, "
                   "और पुरुष की कामना। ‘स्फुरच्छ्रोणि’ में स्फुरत् + श्रोणि की सन्धि है।"),
    "hook": "कृश-प्रसन्न मुख, फड़कते अंग, ढीली कुक्षि, पुरुष-कामना: ऋतुमती।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By verse 78, as what should one know such a woman?",
            ("As one in her ṛtu", "विद्याद् ऋतुमतीं स्त्रियम्: know her as a woman in her ṛtu."),
            [("As one already pregnant", "Pregnancy is not named in the verse."),
             ("As one with an ārtava fault", "No fault is named; these are signs of the ṛtu."),
             ("As one past her ṛtu", "The signs mark a woman in her ṛtu (ऋतुमती), not one past it.")],
            "The signs mark a ṛtumatī, a woman in her season.",
            "ऋतुमती = a woman in her ṛtu."),
        order(1, "Put these phrases of verse 78 in their printed order.",
              ["क्षामप्रसन्नवदनाम्", "स्फुरच्छ्रोणिपयोधराम्", "स्रस्त…कुक्षिम्", "पुंस्कामाम्", "विद्यादृतुमतीं स्त्रियम्"],
              "Face, then hips and breasts (line 1); drooping belly, desire, then the verb and object (line 2).",
              "वदन → श्रोणि-पयोधर → कुक्षि → पुंस्कामा → ऋतुमती."),
        T(match(2, "Match each word of verse 78 to its meaning on the card.",
                [["क्षाम", "lean"], ["स्फुरत्", "throbbing"], ["श्रोणि", "hip"], ["पयोधर", "breast"], ["कुक्षि", "belly"]],
                "Five words of the signs; पयोधर literally means water-bearer.",
                "क्षाम, स्फुरत्, श्रोणि, पयोधर, कुक्षि.", role="extend"),
          "पयोधर (literally water-bearer) is a standard word for breast."),
        mcq("discriminate", 3, "Which split of स्फुरच्छ्रोणि is right?",
            ("स्फुरत् + श्रोणि", "त् + श → च्श, optionally च्छ before a vowel or semivowel (the print has च्छ): स्फुरत् + श्रोणि → स्फुरच्छ्रोणि."),
            [("स्फुरच् + छ्रोणि", "छ्रोणि is no word; the word is श्रोणि."),
             ("स्फुर + च्छ्रोणि", "च्छ्रोणि is no word."),
             ("स्फुरन् + श्रोणि", "न् + श would not give च्छ.")],
            "स्फुरत् (throbbing) + श्रोणि (hip).",
            "त् + श → च्श, optionally च्छ before a vowel or semivowel (the print has च्छ)."),
        multi("apply", 4, "Which signs does verse 78 list for a woman in her ṛtu?",
              [("A lean, clear face", "Right: क्षामप्रसन्नवदनाम्."),
               ("Throbbing hips and breasts", "Right: स्फुरच्छ्रोणिपयोधराम्."),
               ("Desire for a man", "Right: पुंस्कामा(म्)."),
               ("Fever and thirst", "Neither is named."),
               ("A heavy, swollen face", "The face is lean (क्षाम) and clear.")],
              [0, 1, 2],
              "The verse lists face, hips and breasts, drooping eyes (reading probable) and belly, and desire for a man.",
              "Signs: क्षाम-प्रसन्न वदन, स्फुरत् श्रोणि-पयोधर, स्रस्त कुक्षि, पुंस्काम."),
        T(mcq("transfer", 5, "By the join in स्फुरच्छ्रोणि, how is महत् + शास्त्रम् written?",
              ("महच्छास्त्रम्", "त् + श → च्श, optionally च्छ before a vowel or semivowel (च्श also correct), as in स्फुरत् + श्रोणि."),
              [("महद्शास्त्रम्", "त् → द् happens before voiced sounds; श is unvoiced."),
               ("महन्शास्त्रम्", "त् → न् (optional) happens only before nasals."),
               ("महश्शास्त्रम्", "That change is for visarga, not for त्.")],
              "स्फुरत् + श्रोणि → स्फुरच्छ्रोणि; so महत् + शास्त्रम् → महच्छास्त्रम्.",
              "त् + श → च्श, optionally च्छ before a vowel or semivowel."),
          "A final त् before श becomes च्, and the श may then become छ (before a vowel or semivowel): च्छ; च्श is also correct."),
    ],
}

# ---------------------------------------------------------------- unit 79
AUTHORED["79"] = {
    "title": "पद्मं संकोचमायाति",
    "question": "What simile does verse 79 use for the yoni, and what does the yoni then not do?",
    "rule": ("As a lotus contracts when the day has passed, so (when the ṛtu has passed, reading probable) that yoni does not receive semen inside."),
    "limits": ("The printed कृतावतीते is read as ऋतावतीते (ऋतौ अतीते, when the ṛtu has passed) by changing one letter; no question "
               "rests on that word. The exact organ meant by yoni is not specified by the word."),
    "explain_hi": ("यह अनुष्टुभ् श्लोक ‘यथा … तथा’ की उपमा है। जैसे दिन बीत जाने पर कमल सिकुड़ जाता है, वैसे ही (ऋतु बीत जाने पर) वह योनि "
                   "शुक्र को भीतर ग्रहण नहीं करती। ‘ऋतु बीतने पर’ वाला शब्द छपाई में ‘कृतावतीते’ है; एक अक्षर बदलकर ‘ऋतावतीते’ "
                   "पढ़ा गया, यह अनुमान है। उपमा के पक्के अंश: कमल ↔ योनि, सिकुड़ना ↔ शुक्र ग्रहण न करना।"),
    "hook": "साँझ को कमल बंद; (ऋतु बीते, पाठ सम्भावित) तो योनि भी बंद।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By verse 79, what happens to the lotus when the day has passed?",
            ("It contracts", "पद्मं संकोचमायाति: the lotus comes to contraction."),
            [("It opens wide", "संकोच is contraction, the opposite."),
             ("It sheds its petals", "No shedding is named."),
             ("It turns towards the moon", "No moon is named.")],
            "As the day passes, the lotus closes up (संकोचम् आयाति).",
            "संकोच = contraction; आयाति = comes to."),
        order(1, "Put these phrases of verse 79 in their printed order (the doubtful word left out).",
              ["पद्मं संकोचमायाति", "दिनेऽतीते यथा", "तथा", "योनिः सा शुक्रम्", "नान्तः प्रतीच्छति"],
              "Line 1 gives the lotus; line 2 gives the yoni that does not receive semen.",
              "पद्म … यथा → तथा → योनिः → न प्रतीच्छति."),
        T(match(2, "Match each word of verse 79 to its meaning on the card.",
                [["पद्म", "lotus"], ["संकोच", "contraction"], ["अन्तः", "inside"], ["प्रतीच्छति", "receives"]],
                "Two words for the lotus half, two for the yoni half.",
                "पद्म, संकोच, अन्तः, प्रतीच्छति.", role="extend"),
          "प्रतीच्छति (from प्रति + √इष्) = receives; with न it means does not receive."),
        mcq("discriminate", 3, "Which split of दिनेऽतीते is right?",
            ("दिने + अतीते", "ए + अ: the अ drops and is marked ऽ: दिनेऽतीते."),
            [("दिन + अतीते", "अ + अ would give दिनातीते."),
             ("दिनः + अतीते", "अः + अ would give दिनोऽतीते."),
             ("दिने + तीते", "तीते is no word; ऽ marks a dropped अ.")],
            "दिने (the day, locative) + अतीते (having passed).",
            "ए + अ → एऽ."),
        mcq("apply", 4, "In the simile of verse 79, what stands for the lotus?",
            ("The yoni", "यथा पद्मम् … तथा योनिः: the yoni matches the lotus."),
            [("The semen", "The semen is what is not received."),
             ("The day", "The day is the time that passes in the lotus half; it is not the lotus."),
             ("The face of the woman in her ṛtu", "No face is named in this verse.")],
            "Lotus ↔ yoni; contracting ↔ not receiving semen inside.",
            "यथा X … तथा Y: X is the likeness of Y."),
        T(mcq("transfer", 5, "By the join in दिनेऽतीते, how is वने + अस्मिन् written?",
              ("वनेऽस्मिन्", "ए + अ: the अ drops, marked ऽ."),
              [("वनास्मिन्", "ए + अ does not give आ."),
               ("वनैस्मिन्", "ए + अ does not give ऐ."),
               ("वनोऽस्मिन्", "ओऽ comes from अः + अ, not from ए.")],
              "दिने + अतीते → दिनेऽतीते; so वने + अस्मिन् → वनेऽस्मिन् (in this forest).",
              "ए + अ → एऽ."),
          "A final ए before अ stays; the अ drops and is marked with avagraha ऽ."),
    ],
}

# ---------------------------------------------------------------- unit 80
AUTHORED["80"] = {
    "title": "मासेनोपचितं रक्तम्",
    "question": "What does verse 80 say of the blood that comes in the ṛtu?",
    "rule": ("Blood accumulated over a month, in the ṛtu again, by the two dhamanīs, slightly dark and ill-smelling: Vāyu "
             "sends it out from the mouth of the yoni (verb reading probable: सृजेत्)."),
    "limits": ("The printed verb सृदेत् is not a form; सृजेत् (would send out) is a possible correction, so no question rests on "
               "the verb. Dhamanī is a vessel or channel (probable); the two are not named."),
    "explain_hi": ("यह अनुष्टुभ् श्लोक एक ही वाक्य है। एक मास में संचित रक्त, ऋतु में फिर, दो धमनियों द्वारा, थोड़ा काला और दुर्गन्ध वाला: "
                   "वायु उसे योनि-मुख से निकालता है। धमनी यानी नाड़ी या वाहिका (सम्भावित); कौन-सी दो, यह नहीं बताया। "
                   "छपा ‘सृदेत्’ कोई रूप नहीं; ‘सृजेत्’ सम्भावित सुधार है।"),
    "hook": "मास भर जमा, दो धमनियों से, थोड़ा काला, दुर्गन्धी: वायु बाहर करे।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By verse 80, over how long is the blood accumulated?",
            ("A month", "मासेनोपचितं रक्तम्: blood accumulated over a month."),
            [("Twelve nights in all", "Twelve nights is the ṛtu of unit 74."),
             ("Sixteen nights", "Sixteen nights is the others' ṛtu of unit 75."),
             ("A full year", "A year is not named.")],
            "The blood is collected over a month and comes again in the ṛtu.",
            "मासेन = over a month; उपचित = accumulated."),
        order(1, "Put these phrases of verse 80 in their printed order.",
              ["मासेनोपचितं रक्तम्", "धमनीभ्याम्", "ऋतौ पुनः", "ईषत्कृष्णं विगन्धं च", "वायुः", "योनिमुखात्"],
              "Line 1: the blood, the two vessels, in the ṛtu again; line 2: its colour and smell, Vāyu, from the yoni's mouth.",
              "रक्तम् → धमनीभ्याम् → ऋतौ पुनः → ईषत्कृष्णम् → वायुः → योनिमुखात्."),
        T(match(2, "Match each word of verse 80 to its meaning on the card.",
                [["धमनी", "vessel, channel (probable)"], ["ईषत्", "slightly"], ["विगन्ध", "ill-smelling"],
                 ["योनिमुख", "mouth of the yoni"], ["उपचित", "accumulated"]],
                "Five words describe the blood and its way out.",
                "धमनी, ईषत्, विगन्ध, योनिमुख, उपचित.", role="extend"),
          "धमनी is a vessel or channel (probable); the verse speaks of two, by which the blood comes."),
        mcq("discriminate", 3, "Which split of मासेनोपचितम् is right?",
            ("मासेन + उपचितम्", "अ + उ → ओ: मासेन + उपचितम् → मासेनोपचितम्."),
            [("मासेनः + उपचितम्", "मासेनः is no form; अः before उ would drop the visarga."),
             ("मासम् + उपचितम्", "म् before उ would give मासमुपचितम्."),
             ("मासेन + ओपचितम्", "ओपचित is no word; the word is उपचित.")],
            "मासेन (over a month) + उपचितम् (accumulated).",
            "अ + उ → ओ."),
        multi("apply", 4, "Which does verse 80 say of the blood in the ṛtu?",
              [("It is slightly dark", "Right: ईषत्कृष्णम्."),
               ("It is ill-smelling", "Right: विगन्धम्."),
               ("It is bright red", "It is slightly dark (ईषत्कृष्ण), not bright red."),
               ("It was collected over a week", "मासेन: over a month.")],
              [0, 1],
              "Slightly dark, ill-smelling, accumulated over a month, coming by two vessels.",
              "ईषत्कृष्ण, विगन्ध."),
        T(mcq("transfer", 5, "An invented phrase reads ईषत्पीतं वस्त्रम्. What does it mean?",
              ("A slightly yellow cloth", "ईषत् = slightly, as in ईषत्कृष्णम् = slightly dark."),
              [("A very yellow cloth", "ईषत् lessens; it does not intensify."),
               ("A cloth without yellow", "ईषत् is not a negation."),
               ("A yellow, ill-smelling cloth", "No smell is named in the phrase.")],
              "ईषत्कृष्णम् = slightly dark; so ईषत्पीतम् = slightly yellow.",
              "ईषत् + adjective = slightly (so)."),
          "ईषत् before an adjective softens it: slightly X."),
    ],
}

# ===================================================================== NOTES_HI
NOTES_HI = {
    "67": ("विश्वास कम। छपा ‘खदिार्जुन’ सन्धि नहीं; खदिर + अर्जुन → खदिरार्जुन (अ + अ → आ) पढ़ा गया, छपाई में ‘र’ छूटा लगता है। "
           "छपा ‘सिद्धममनादिभिर्वा’ क्षतिग्रस्त: ‘अमनादिभिः’ सम्भवतः ‘मदनादिभिः’ (द और म का स्थान बदला), केवल अनुमान। "
           "कुणप का अर्थ शव-गन्ध सम्भावित। पहचान: खदिर, अर्जुन, दाडिम मानक। "
           "सन्धि: अमनादिभिः + वा → अमनादिभिर्वा।"),
    "68": ("दो छपी पंक्तियाँ, दोनों में क्रिया नहीं। छपा ‘ग्रंधि’ (ध) ग्रन्थि पढ़ा गया। पाषाणभिद् = पाषाणभेद (पखानभेद, सम्भावित)। "
           "‘आदिभ्याम्’ का द्विवचन दो गणों (परूषकादि, न्यग्रोधादि) का; पहला ‘आदि’ समास-रूप में है। "
           "दोनों पंक्तियाँ छन्द-बद्ध नहीं, गद्य जैसी हैं। सन्धि: परूषक + आदि → परूषकादि।"),
    "69": ("विश्वास कम। छपा ‘हिंगुशीर’: हिङ्गु + उशीर → हिङ्गूशीर (दीर्घ ऊ) होना चाहिए; ‘शीर’ अकेला निरर्थक, इसलिए उशीर अनुमान है। "
           "‘मोचचूर्ण’ को मोच + चूर्ण पढ़ा (मोचा-चूर्ण भी सम्भव)। वितुन्नक, समङ्गा, मोच की पहचान विवादित। "
           "सन्धियाँ: वायुना + अतिविकृते → वायुनाऽतिविकृते (आ + अ → आ, छपाई ऽ लगाती है); चित्रकैः + अथवा → चित्रकैरथवा; "
           "सिद्धम् + एला → सिद्धमेला।"),
    "70": ("क्रिया यहाँ नहीं; ‘पिबेत्’ अगली इकाई (७१) में है। पहचान तीनों सम्भावित: पाठा, त्रिकण्टक (गोखरू, श्वदंष्ट्रा जैसा), "
           "वृक्षक (कुटज)। पंक्ति छन्द-बद्ध नहीं, गद्य जैसी है। सन्धि: ग्रन्थि + आर्तवे → ग्रन्थ्यार्तवे (इ + आ → या)।"),
    "71": ("अन्तिम खण्ड दो द्विवचनों का बिना क्रिया का वाक्य: कल्क-क्वाथ और धारण-आचमन; जोड़ी पाठ में नहीं कही गई। "
           "आचमन = घूँट लेना / मुँह धोना, प्रक्षालन नहीं। त्रिफला = हरीतकी, बिभीतक, आमलक (मानक)। "
           "सन्धियाँ: कुणप + पूय + आर्तवे → कुणपपूयार्तवे; च + अत्र → चात्र; धारण + आचमने → धारणाचमने।"),
    "72": ("विश्वास ऊँचा। छपा ‘सर्वेषुच’ = सर्वेषु च। ‘पुनः पुनः’ में पहला पुनः ‘उत्तरबस्तिभिः’ से जुड़ा छपा है। "
           "सन्धियाँ: शुक्र + आर्तव → शुक्रार्तव; कर्मभिः + विशेषेण → कर्मभिर्विशेषेण; विशेषेण + उत्तर → विशेषेणोत्तर (अ + उ → ओ); "
           "पुनर् + उपाचरेत् → पुनरुपाचरेत्।"),
    "73": ("इकाई ७२ का वाक्य आगे बढ़ता लगता है; क्रिया ‘उपाचरेत्’ वहीं से। पिचु = रूई का फाहा (मानक)। "
           "सन्धि: पिचुभिः + च → पिचुभिश्च (विसर्ग + च → श्च); यथास्वम् → यथास्वं (अनुस्वार)।"),
    "74": ("दो छपी पंक्तियाँ। ‘इति’ पिछले कथन को बन्द करता है। ‘पूर्वोक्तम्’ पुंलिंग, ‘विधिम्’ के साथ मेल। ऋतु = गर्भधारण-काल (सम्भावित)। "
           "सन्धियाँ: इति + एवम् → इत्येवम्; पूर्व + उक्तम् → पूर्वोक्तम्; ऋतुः + तु → ऋतुस्तु; दृष्टार्तवः + द्वादश → दृष्टार्तवो द्वादश।"),
    "75": ("विश्वास ऊँचा। क्रिया नहीं; ‘इति अन्ये’ दूसरों का मत। संख्या छपे अनुसार। "
           "सन्धियाँ: षोडशरात्रम् + इति → षोडशरात्रमिति; इति + अन्ये → इत्यन्ये।"),
    "76": ("छपा ‘…आर्तवाया’ में षष्ठी का विसर्ग छूटा लगता है: आर्तवायाः। स्त्रीलिंग बहुव्रीहि एक स्त्री की ओर संकेत करता है। "
           "इकाई ७४-७५ के ऋतु-काल का क्रम आगे। सन्धियाँ: गर्भ + आशय → गर्भाशय; मासम् + अपि → मासमपि।"),
    "77": ("बिना कही संज्ञा ‘एक’ दिखाई गई; पुंलिंग रूप ऋतु से मेल खाता है। ‘तद्वत्’ किससे तुलना, यह नहीं कहा। "
           "सन्धियाँ: तद्वत् + अदृष्ट → तद्वददृष्ट; अदृष्टार्तवः + अपि → अदृष्टार्तवोऽपि; अपि + अस्ति → अप्यस्ति; "
           "अस्ति + इति → अस्तीति; इति + अपरे → इत्यपरे।"),
    "78": ("दो छपी पंक्तियाँ, एक श्लोक। छपा ‘स्रस्ताक्षु’: ‘अक्षु’ कोई शब्द नहीं, ‘अक्षि’ (आँख) अपेक्षित, सम्भावित सुधार। "
           "छपा ‘पुंस्कामा’: ‘स्त्रियम्’ से मेल के लिए ‘पुंस्कामाम्’ अपेक्षित, अनुस्वार छूटा लगता है। "
           "सन्धियाँ: स्फुरत् + श्रोणि → स्फुरच्छ्रोणि; विद्यात् + ऋतुमतीम् → विद्यादृतुमतीम्।"),
    "79": ("छपा ‘कृतावतीते’ अर्थहीन; ‘ऋतावतीते’ (ऋतौ + अतीते, औ + अ → आव) एक अक्षर के अनुमान पर टिका है। "
           "सन्धियाँ: संकोचम् + आयाति → संकोचमायाति; दिने + अतीते → दिनेऽतीते; न + अन्तः → नान्तः; प्रति + इच्छति → प्रतीच्छति।"),
    "80": ("छपा ‘सृदेत्’ कोई क्रिया-रूप नहीं; √सृज् का ‘सृजेत्’ सम्भावित सुधार (द/ज की भूल)। धमनी = वाहिका (सम्भावित); "
           "दो कौन-सी, नहीं कहा। सन्धियाँ: मासेन + उपचितम् → मासेनोपचितम्; धमनीभ्याम् + ऋतौ → धमनीभ्यामृतौ; "
           "वायुः + योनि → वायुर्योनि।"),
}

# ===================================================================== AIDS
AIDS = {
    "67": {
        "frame": "दोष (सप्तमी): कुणपरेतसि → द्रव्य (तृतीया): धातकीपुष्प, खदिर, अर्जुन, दाडिम → सिद्धं सर्पिः → पाययेत्।",
        "chunks": "कुणपरेतसि | धातकीपुष्पखदिार्जुनदाडिमैः (पढ़ें: खदिर-अर्जुन) | सिद्धम् | अमनादिभिर्वा (क्षतिग्रस्त) | सर्पिः पाययेत्।",
        "sandhi": "अ + अ → आ: खदिर + अर्जुन → खदिरार्जुन · इः + व → इर्व: अमनादिभिः + वा → अमनादिभिर्वा।",
    },
    "68": {
        "contrast": {"groups": [
            {"label": "ग्रन्थिरेतस् (गाँठ)", "items": ["पाषाणभिद्", "या पलाश-भस्म"]},
            {"label": "पूयरेतस् (पीब)", "items": ["परूषक आदि गण", "न्यग्रोध आदि गण"]}]},
        "sandhi": "अ + आ → आ: परूषक + आदि → परूषकादि; न्यग्रोध + आदिभ्याम् → न्यग्रोधादिभ्याम्।",
        "anchors": "दोष सप्तमी में (-रेतसि), उपाय तृतीया में (-भिदा, -भस्मना, -आदिभ्याम्)।",
    },
    "69": {
        "diagram": {"groups": [
            {"label": "दोष", "items": ["मूत्र-पुरीष-रेतस्", "वायु से अति विकृत"]},
            {"label": "पहला योग", "items": ["हिङ्गु", "उशीर (अनुमान)", "चित्रक"]},
            {"label": "अथवा: सिद्ध योग", "items": ["चित्रक", "वितुन्नक", "प्रियङ्गु", "हिङ्गु", "समङ्गा", "मृणाल"]},
            {"label": "प्रतीवाप", "items": ["एला-चूर्ण", "मोच-चूर्ण"]}]},
        "sandhi": "ऐः + अ → ऐर: चित्रकैः + अथवा → चित्रकैरथवा · म् + ए: सिद्धम् + एला → सिद्धमेला · आ + अ → आ (छपाई ऽ लगाती है): वायुना + अति → वायुनाऽति।",
        "anchors": "चित्रक और हिङ्गु दोनों सूचियों में: ‘दो पुराने मित्र, दोनों जगह’ (मेरी याद-पद्धति)।",
    },
    "70": {
        "sandhi": "इ + आ → या: ग्रन्थि + आर्तवे → ग्रन्थ्यार्तवे।",
        "contrast": "इकाई ६८: ग्रन्थि-रेतस् (शुक्र में गाँठ) ↔ इकाई ७०: ग्रन्थि-आर्तव (आर्तव में गाँठ); ‘तथा’ दोनों को जोड़ता है।",
        "chunks": "तथा | ग्रन्थ्यार्तवे | पाठा-त्रिकण्टक-वृक्षक | क्वाथम्।",
    },
    "71": {
        "diagram": {"groups": [
            {"label": "पीना", "items": ["चन्दन-क्वाथ"]},
            {"label": "त्रिफला के रूप", "items": ["कल्क", "क्वाथ"]},
            {"label": "प्रयोग", "items": ["धारण", "आचमन"]}]},
        "sandhi": "अ + अ → आ: च + अत्र → चात्र · अ + आ → आ: पूय + आर्तवे → पूयार्तवे; धारण + आचमने → धारणाचमने।",
        "frame": "दो द्विवचन साथ-साथ: कल्क-क्वाथ, धारण-आचमन; कौन किसके साथ, पाठ नहीं कहता।",
    },
    "72": {
        "diagram": {"groups": [
            {"label": "कब", "items": ["शुक्र-आर्तव के सब दोषों में"]},
            {"label": "किसका", "items": ["स्त्री और पुरुष दोनों"]},
            {"label": "किससे", "items": ["स्नेह आदि कर्म", "विशेषतः उत्तरबस्ति"]},
            {"label": "कितनी बार", "items": ["बार-बार"]}]},
        "sandhi": "अ + उ → ओ: विशेषेण + उत्तर → विशेषेणोत्तर · इः + व → इर्व: कर्मभिः + विशेषेण → कर्मभिर्विशेषेण · पुनर् + उ → पुनरु।",
        "anchors": "‘स्त्रीपुंसौ’: शुक्र या आर्तव, कोई भी दोष हो, उपचार दोनों का।",
    },
    "73": {
        "frame": "क्रिया ‘उपाचरेत्’ इकाई ७२ से · कहाँ: योनौ · कैसे: यथास्वम् · किससे: कल्कैः, पिचुभिः।",
        "sandhi": "विसर्ग + च → श्च: पिचुभिः + च → पिचुभिश्च।",
        "pegs": "मेरा बनाया चित्र: एक कटोरी में कल्क, पास में रूई का फाहा (केवल याद के लिए)।",
    },
    "74": {
        "frame": "पंक्ति १: शुद्ध हुए दोनों → पूर्वोक्त विधि का पालन · पंक्ति २: ऋतु = दृष्टार्तव, बारह रात।",
        "sandhi": "अ + उ → ओ: पूर्व + उक्तम् → पूर्वोक्तम् · अः + घोष → ओ: दृष्टार्तवः + द्वादश → दृष्टार्तवो द्वादश · उः + त → उस्त: ऋतुः + तु → ऋतुस्तु।",
        "anchors": "बारह = द्वादश; दोनों ‘द’ से: ‘द्वादश, दृष्ट’ (मेरी याद-पद्धति)।",
    },
    "75": {
        "sandhi": "इ + अ → य: इति + अन्ये → इत्यन्ये · म् + इ: षोडशरात्रम् + इति → षोडशरात्रमिति।",
        "anchors": "इकाई ७४: १२ रात (पाठ का अपना); इकाई ७५: १६ रात (अन्ये)।",
    },
    "76": {
        "contrast": {"groups": [
            {"label": "पाठ (इकाई ७४)", "items": ["१२ रात"]},
            {"label": "अन्ये (इकाई ७५)", "items": ["१६ रात"]},
            {"label": "केचित् (इकाई ७६)", "items": ["एक मास भी", "शुद्ध योनि-गर्भाशय-आर्तव वाली"]}]},
        "sandhi": "अ + आ → आ: गर्भ + आशय → गर्भाशय · म् + अ: मासम् + अपि → मासमपि।",
        "chunks": "शुद्ध-योनि-गर्भाशय-आर्तवायाः | मासम् अपि | तु | केचित्।",
    },
    "77": {
        "contrast": "इकाई ७४: दृष्टार्तव (आर्तव दिखे) ↔ इकाई ७७: अदृष्टार्तव (आर्तव न दिखे)।",
        "sandhi": "त् + अ → द: तद्वत् + अदृष्ट → तद्वददृष्ट · अः + अ → ओऽ: अदृष्टार्तवः + अपि → अदृष्टार्तवोऽपि · इ + अ → य: अपि + अस्ति → अप्यस्ति।",
        "chunks": "तद्वत् | अदृष्टार्तवः | अपि अस्ति | इति अपरे।",
    },
    "78": {
        "diagram": {"groups": [
            {"label": "मुख", "items": ["कृश", "प्रसन्न"]},
            {"label": "फड़कते", "items": ["श्रोणि", "पयोधर"]},
            {"label": "शिथिल", "items": ["आँखें (पाठ सम्भावित)", "कुक्षि"]},
            {"label": "मन", "items": ["पुरुष की कामना"]}]},
        "sandhi": "त् + श → च्श, विकल्प से च्छ (श के बाद स्वर या य/व/र हो तो; छपा च्छ): स्फुरत् + श्रोणि → स्फुरच्छ्रोणि · त् + ऋ → दृ: विद्यात् + ऋतुमतीम् → विद्यादृतुमतीम्।",
        "chunks": "क्षामप्रसन्नवदनां | स्फुरच्छ्रोणिपयोधरां | स्रस्ताक्षुकुक्षिं | पुंस्कामा | विद्यादृतुमतीं स्त्रियम्।",
    },
    "79": {
        "contrast": {"groups": [
            {"label": "उपमान (यथा)", "items": ["पद्म", "दिन बीतने पर", "संकोच"]},
            {"label": "उपमेय (तथा)", "items": ["योनि", "ऋतु बीतने पर (पाठ सम्भावित)", "शुक्र भीतर ग्रहण नहीं"]}]},
        "sandhi": "ए + अ → एऽ: दिने + अतीते → दिनेऽतीते · अ + अ → आ: न + अन्तः → नान्तः · इ + इ → ई: प्रति + इच्छति → प्रतीच्छति।",
        "story": "मेरी बनाई कथा: साँझ हुई, तालाब का कमल धीरे-धीरे बंद हुआ; अब उसमें कुछ नहीं समाता। (केवल याद के लिए)",
    },
    "80": {
        "chain": {"steps": ["मास भर संचित रक्त", "ऋतु में फिर", "दो धमनियों द्वारा", "थोड़ा काला, दुर्गन्धी",
                            "वायु: योनि-मुख से (क्रिया का पाठ सम्भावित)"]},
        "sandhi": "अ + उ → ओ: मासेन + उपचितम् → मासेनोपचितम् · म् + ऋ: धमनीभ्याम् + ऋतौ → धमनीभ्यामृतौ · उः + य → उर्य: वायुः + योनि → वायुर्योनि।",
        "chunks": "मासेनोपचितं रक्तं | धमनीभ्यामृतौ पुनः | ईषत्कृष्णं विगन्धं च | वायुर्योनिमुखात् | सृदेत् (पाठ सम्भावित: सृजेत्)।",
    },
}

# ===================================================================== IMAGE_SPECS
IMAGE_SPECS = {
    ("68", "contrast"): {
        "file": "sh1-granthi-puya-retas-68.svg",
        "alt": ("Two columns for unit 68: semen with knots (granthi-retas) takes pashanabhid or palasha ash; semen with pus "
                "(puya-retas) takes the group beginning with parushaka and the group beginning with nyagrodha."),
        "type": "split",
        "title": "शुक्र-दोष और उपाय (इकाई ६८)",
        "cols": [["ग्रन्थिरेतस् (गाँठ)", ["पाषाणभिद्", "या पलाश-भस्म"]],
                 ["पूयरेतस् (पीब)", ["परूषक आदि गण", "न्यग्रोध आदि गण"]]],
    },
    ("69", "diagram"): {
        "file": "sh1-mutra-purisha-retas-69.svg",
        "alt": ("Flowchart of unit 69: semen with urine and feces, greatly altered by Vayu, has two options: hingu, ushira "
                "(conjectural) and chitraka; or a preparation cooked with chitraka, vitunnaka, priyangu, hingu, samanga and "
                "mrinala, with ela and moca powder as the addition."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"मूत्र-पुरीष-रेतस्<br/>वायु से अति विकृत\"] --> B[\"हिङ्गु, उशीर (अनुमान),<br/>चित्रक\"]\n"
                 "  A -->|\"अथवा\"| C[\"चित्रक, वितुन्नक,<br/>प्रियङ्गु, हिङ्गु,<br/>समङ्गा, मृणाल से सिद्ध\"]\n"
                 "  C --> D[\"प्रतीवाप:<br/>एला-मोच चूर्ण\"]\n"),
    },
    ("72", "diagram"): {
        "file": "sh1-stripumsau-72.svg",
        "alt": ("Table of unit 72: when, in all faults of semen and artava; whom, both woman and man; with what, the actions "
                "beginning with sneha, especially uttarabasti; how often, again and again."),
        "type": "table",
        "title": "सब दोषों में (इकाई ७२)",
        "heads": ["प्रश्न", "उत्तर"],
        "rows": [["कब", "शुक्र-आर्तव के सब दोषों में"], ["किसका", "स्त्री और पुरुष दोनों"],
                 ["किससे", "स्नेह आदि कर्म; विशेषतः उत्तरबस्ति"], ["कितनी बार", "बार-बार"]],
    },
    ("76", "contrast"): {
        "file": "sh1-ritu-kala-76.svg",
        "alt": ("Table of the views on the length of the ritu in units 74 to 76: the text, twelve nights; others, sixteen "
                "nights; some, even a month for a woman whose yoni, womb and artava are pure."),
        "type": "table",
        "title": "ऋतु कितनी रातें? (इकाई ७४-७६)",
        "heads": ["किसका मत", "अवधि"],
        "rows": [["पाठ (इकाई ७४)", "१२ रात"],
                 ["अन्ये (इकाई ७५)", "१६ रात"],
                 ["केचित् (इकाई ७६)", "एक मास भी (शुद्ध हो तो)"]],
    },
    ("78", "diagram"): {
        "file": "sh1-ritumati-78.svg",
        "alt": ("Mindmap of verse 78, signs of a woman in her ritu: face lean and clear; hips and breasts throbbing; eyes "
                "(reading probable) and belly drooping; desire for a man."),
        "type": "mermaid",
        "code": ("mindmap\n"
                 "  ऋतुमती\n"
                 "    मुख\n"
                 "      कृश\n"
                 "      प्रसन्न\n"
                 "    फड़कते\n"
                 "      श्रोणि\n"
                 "      पयोधर\n"
                 "    शिथिल\n"
                 "      आँखें, पाठ सम्भावित\n"
                 "      कुक्षि\n"
                 "    पुरुष की कामना\n"),
    },
    ("79", "contrast"): {
        "file": "sh1-padma-upama-79.svg",
        "alt": ("Table of the simile of verse 79: the lotus matches the yoni; the day passing matches the ritu passing "
                "(reading probable); the lotus contracting matches the yoni not receiving semen inside."),
        "type": "table",
        "title": "कमल की उपमा (इकाई ७९)",
        "heads": ["उपमान (यथा)", "उपमेय (तथा)"],
        "rows": [["पद्म (कमल)", "योनि"],
                 ["दिन बीतने पर", "ऋतु बीतने पर (पाठ सम्भावित)"],
                 ["संकोच", "शुक्र भीतर ग्रहण नहीं"]],
    },
    ("80", "chain"): {
        "file": "sh1-masika-rakta-80.svg",
        "alt": ("Chain of verse 80: blood accumulated over a month; in the ritu again; by the two dhamanis; slightly dark and "
                "ill-smelling; Vayu, from the mouth of the yoni (the verb's reading is probable)."),
        "type": "chain",
        "title": "ऋतु में रक्त (इकाई ८०)",
        "steps": ["मास भर संचित रक्त", "ऋतु में फिर", "दो धमनियों द्वारा", "थोड़ा काला, दुर्गन्धी",
                  "वायु: योनि-मुख से (क्रिया का पाठ सम्भावित)"],
    },
}
