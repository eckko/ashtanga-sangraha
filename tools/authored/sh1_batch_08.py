from helpers import mcq, match, order, fill, multi, accepts


def T(q, teaches):
    q["teaches"] = teaches
    return q


AUTHORED = {}

# ---------------------------------------------------------------- unit 94
AUTHORED["94"] = {
    "title": "यदि त्वाहारानुरोधात्",
    "question": "By unit 94, what male is born when śukra abounds in the odd (nights) and is deficient in the even ones?",
    "rule": ("If, owing to conformity to diet, śukra (semen) abounds in the odd (nights) and is deficient in the even ones, "
             "then a male is born of female form, weak, or deficient in limb."),
    "limits": ("The cause āhāra-anurodha is read as 'conformity to diet'; the data says its sense is not fully clear, so no "
               "question rests on it. 'Nights' is understood, not printed. The sentence goes on in unit 95 (the female)."),
    "explain_hi": ("यह गद्य-वाक्य विषम और सम रात्रियों में शुक्र की अधिकता-कमी का एक परिणाम बताता है। "
                   "यदि आहार के अनुसार विषम रात्रियों में शुक्र अधिक और सम रात्रियों में कम हो, "
                   "तो पुरुष जन्म लेता है, पर स्त्री के आकार वाला, दुर्बल या हीन अंगों वाला। "
                   "‘आहारानुरोधात्’ का ठीक अर्थ पूरी तरह स्पष्ट नहीं है; ‘रात्रियों’ शब्द समझा जाता है, छपा नहीं। "
                   "वाक्य इकाई ९५ में स्त्री की बात से आगे चलता है।"),
    "hook": "विषम में शुक्र ज़्यादा, सम में कम: पुरुष तो, पर स्त्री-आकृति।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In unit 94, in which (nights) is śukra said to abound?",
            ("In the odd ones (अयुग्मासु)", "अयुग्मासु शुक्रस्याधिक्यता: abundance of śukra in the odd (nights)."),
            [("In the even ones (युग्मासु)", "In the even (nights) the unit puts a deficiency (न्यूनता)."),
             ("In the eleventh only", "The eleventh night comes in unit 95, with the napuṃsaka."),
             ("In the first three", "No first three nights are named in this unit.")],
            "Abundance in the odd (nights), deficiency in the even ones.",
            "अयुग्म = odd; युग्म = even."),
        order(1, "Put these parts of unit 94 in their printed order.",
              ["यदि त्वाहारानुरोधात्", "अयुग्मासु शुक्रस्याधिक्यता", "युग्मासु च न्यूनता", "ततःपुमान्",
               "स्त्र्याकृतिर्दुर्बलो हीनांगो वा जायते"],
              "If … owing to diet, abundance of śukra in the odd, deficiency in the even, then a male … is born.",
              "यदि → अयुग्मासु आधिक्यता → युग्मासु न्यूनता → ततः पुमान् → जायते."),
        T(match(2, "Match each word of unit 94 to its meaning on the card.",
                [["अयुग्म", "odd"], ["युग्म", "even"], ["आधिक्यता", "abundance"], ["न्यूनता", "deficiency"],
                 ["हीनाङ्ग", "deficient in limb"]],
                "Four words give the condition (odd/even, more/less); one describes the male born.",
                "अयुग्म, युग्म, आधिक्यता, न्यूनता, हीनाङ्ग.", role="extend"),
          "युग्म = even (paired), अयुग्म = odd (not paired); the unit sets more śukra in one against less in the other."),
        mcq("discriminate", 3, "Which split of स्त्र्याकृतिर्दुर्बलो is right?",
            ("स्त्री + आकृतिः + दुर्बलः", "ई + आ → या; इः + द → इर्द; अः before the voiced ह → ओ."),
            [("स्त्रिया + आकृतिः + दुर्बलः", "आ + आ would give स्त्रियाकृतिः, not स्त्र्याकृतिः."),
             ("स्त्री + आकृति + र्दुर्बलः", "र्दुर्बलः is not a word; the र् is the visarga of आकृतिः."),
             ("स्त्र्य + आकृतिः + दुर्बलम्", "स्त्र्य is not a word, and the printed ending is -ओ, not -म्.")],
            "स्त्री (female) + आकृतिः (form) + दुर्बलः (weak): a male of female form, weak.",
            "ई + आ → या; visarga after इ → र् before a voiced sound."),
        multi("apply", 4, "Which does unit 94 say the male born in this case may be?",
              [("Of female form", "Right: स्त्र्याकृतिः."),
               ("Weak", "Right: दुर्बलः."),
               ("Deficient in limb", "Right: हीनाङ्गः."),
               ("A napuṃsaka", "The napuṃsaka belongs to the eleventh and thirteenth nights of unit 95."),
               ("Of male form and strong", "A female of male form comes in unit 95; strong is not said.")],
              [0, 1, 2],
              "Then a male is born of female form, weak, or deficient in limb (वा = or).",
              "स्त्र्याकृतिः, दुर्बलः, हीनाङ्गः वा."),
        T(mcq("transfer", 5, "By the rule of स्त्र्याकृतिः, how is देवी + आलयः written when joined?",
              ("देव्यालयः", "ई + आ → या, as in स्त्री + आकृतिः."),
              [("देवीलयः", "The आ of आलयः cannot simply vanish."),
               ("देव्यलयः", "The long आ stays: य् + आ, not य् + अ."),
               ("देवैलयः", "ई + आ does not give ऐ.")],
              "स्त्री + आकृतिः → स्त्र्याकृतिः; so देवी + आलयः → देव्यालयः.",
              "ई + a different vowel → य् + that vowel."),
          "A final ई before a different vowel becomes य् and the vowel follows unchanged."),
    ],
}

# ---------------------------------------------------------------- unit 95
AUTHORED["95"] = {
    "title": "स्त्री च पुरुषाकृतिः",
    "question": "What female does unit 95 add, and what does it say of the eleventh and thirteenth (nights)?",
    "rule": ("And a female (is born) of male form, weak, or deficient in limb. But on the eleventh and thirteenth (nights) "
             "there would be a napuṃsaka (a person neither male nor female)."),
    "limits": ("Elliptic: 'is born' is carried from unit 94, and the unit states no cause for the female of male form. "
               "'Nights' is understood. Napuṃsaka is kept as the data glosses it (neither male nor female; eunuch, impotent)."),
    "explain_hi": ("पहली पंक्ति इकाई ९४ के वाक्य को पूरा करती है: और स्त्री (जन्म लेती है) पुरुष के आकार वाली, दुर्बल या हीन अंगों वाली। "
                   "‘जायते’ क्रिया इकाई ९४ से ली गई है; इस स्त्री का कारण यहाँ अलग से नहीं बताया गया। "
                   "दूसरी पंक्ति नई बात कहती है: ग्यारहवीं और तेरहवीं (रात्रि) में नपुंसक होगा। "
                   "नपुंसक यानी जो न पुरुष हो न स्त्री (मानक अर्थ)।"),
    "hook": "ग्यारह और तेरह: नपुंसक।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 95, on which (nights) would there be a napuṃsaka?",
            ("The eleventh and thirteenth", "एकादशीत्रयोदश्योः: on the eleventh and thirteenth."),
            [("The twelfth and fourteenth", "These numbers are not in the unit."),
             ("The ninth and fifteenth", "These numbers are not in the unit."),
             ("The tenth and the twelfth", "These numbers are not in the unit.")],
            "On the eleventh and thirteenth (nights) there would be a napuṃsaka.",
            "एकादशी = eleventh; त्रयोदशी = thirteenth."),
        order(1, "Put these parts of unit 95 in their printed order.",
              ["स्त्री च", "पुरुषाकृतिः", "दुर्बला", "हीनाङ्गी वा", "एकादशीत्रयोदश्योस्तु", "नपुंसकं स्यात्"],
              "The female of male form, weak or deficient in limb; then the eleventh and thirteenth, and the napuṃsaka.",
              "स्त्री → पुरुषाकृतिः → दुर्बला → हीनाङ्गी → एकादशी-त्रयोदशी → नपुंसकम्."),
        T(match(2, "Match each word of unit 95 to its meaning on the card.",
                [["पुरुषाकृति", "of male form"], ["दुर्बला", "weak (feminine)"], ["हीनाङ्गी", "deficient in limb (feminine)"],
                 ["एकादशी", "eleventh"], ["त्रयोदशी", "thirteenth"]],
                "Three words describe the female; two name the nights of the napuṃsaka.",
                "पुरुषाकृति, दुर्बला, हीनाङ्गी, एकादशी, त्रयोदशी.", role="extend"),
          "दुर्बला and हीनाङ्गी are the feminine forms of दुर्बल and हीनाङ्ग of unit 94."),
        mcq("discriminate", 3, "Which split of त्रयोदश्योस्तु is right?",
            ("त्रयोदश्योः + तु", "A visarga before त becomes स्: -योः + तु → -योस्तु."),
            [("त्रयोदश्यो + स्तु", "स्तु is not a word; the स् is the changed visarga."),
             ("त्रयोदशी + ओस्तु", "ओस्तु is not a word of the card."),
             ("त्रयोदश्योम् + तु", "म् before त would give ं, not स्त.")],
            "त्रयोदश्योः (end of the pair एकादशी-त्रयोदशी, locative dual: on the eleventh and thirteenth) + तु (but).",
            "Visarga + त → स्त."),
        mcq("apply", 4, "By unit 95, with the verb carried from unit 94, what female may be born?",
            ("One of male form, weak or deficient in limb", "पुरुषाकृतिः दुर्बला हीनाङ्गी वा."),
            [("One of female form, strong and long-lived", "None of these words is in the unit."),
             ("A napuṃsaka, on the even nights only", "The napuṃsaka is set on the eleventh and thirteenth."),
             ("One of fair complexion and good conduct", "Complexion and conduct are not named here.")],
            "And a female (is born) of male form, weak, or deficient in limb.",
            "स्त्री च पुरुषाकृतिः … (जायते from unit 94)."),
        T(mcq("transfer", 5, "By the rule of त्रयोदश्योस्तु, how is रामः + तु written when joined?",
              ("रामस्तु", "Visarga before त → स्, as in त्रयोदश्योः + तु."),
              [("रामोतु", "अः → ओ happens before voiced sounds; त is voiceless."),
               ("रामर्तु", "र् comes from a visarga after a vowel other than अ/आ."),
               ("रामश्तु", "श् comes before च/छ/श, not before त.")],
              "त्रयोदश्योः + तु → त्रयोदश्योस्तु; so रामः + तु → रामस्तु.",
              "Visarga + त → स्त."),
          "A visarga before त or थ becomes स्."),
    ],
}

# ---------------------------------------------------------------- unit 96
AUTHORED["96"] = {
    "title": "अथोपाध्यायः पुत्रीयं विधानम्",
    "question": "Who, by unit 96, performs what procedure?",
    "rule": "Then the teacher (upādhyāya) should perform the procedure relating to a son (putrīya).",
    "limits": ("The rite itself is not described in this unit. Upādhyāya is taken as a teacher or preceptor (probable); "
               "he may act as the officiating priest."),
    "explain_hi": ("यहाँ नया प्रसंग शुरू होता है: पुत्र-सम्बन्धी विधि। ‘अथ’ यानी तब, इसके बाद। "
                   "उपाध्याय (शिक्षक, गुरु) पुत्रीय विधान का आचरण करे। ‘पुत्रीय’ विशेषण है: पुत्र से सम्बन्धित, पुत्र के लिए। "
                   "विधि के चरण इस इकाई में नहीं बताए गए; उपाध्याय = शिक्षक, गुरु (सम्भावित); वह पुरोहित का काम कर सकता है।"),
    "hook": "अथ उपाध्याय: पुत्रीय विधान।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 96, who should perform the procedure?",
            ("The teacher (उपाध्यायः)", "अथोपाध्यायः … आचरेत्: the teacher should perform it."),
            [("The woman herself (स्त्री)", "The woman is not the subject of this unit."),
             ("The physician (वैद्यः)", "No physician is named in this unit."),
             ("The woman's mother (माता)", "No mother is named in this unit.")],
            "Then the teacher (upādhyāya) should perform the procedure relating to a son.",
            "उपाध्याय = teacher, preceptor."),
        order(1, "Put the words of unit 96 in their printed order.",
              ["अथ", "उपाध्यायः", "पुत्रीयम्", "विधानम्", "आचरेत्"],
              "Then, the teacher, relating to a son, the procedure, should perform.",
              "अथ → उपाध्यायः → पुत्रीयम् → विधानम् → आचरेत्."),
        T(match(2, "Match each word of unit 96 to its meaning on the card.",
                [["अथ", "then"], ["उपाध्याय", "teacher"], ["पुत्रीय", "relating to a son"], ["विधान", "procedure, rite"],
                 ["आचरेत्", "should perform"]],
                "Five words make the whole line.",
                "अथ, उपाध्याय, पुत्रीय, विधान, आचरेत्.", role="extend"),
          "आचरेत् is an optative: should perform; it gives the instruction."),
        mcq("discriminate", 3, "Which split of अथोपाध्यायः is right?",
            ("अथ + उपाध्यायः", "अ + उ → ओ: अथ + उपाध्यायः → अथोपाध्यायः."),
            [("अथो + पाध्यायः", "पाध्यायः is not a word of the card."),
             ("अथ + ओपाध्यायः", "अ + ओ would give औ: अथौपाध्यायः."),
             ("अथम् + उपाध्यायः", "म् before a vowel would give अथमुपाध्यायः.")],
            "अथ (then) + उपाध्यायः (the teacher).",
            "अ + उ → ओ."),
        mcq("apply", 4, "What does पुत्रीयम् tell us about the procedure (विधानम्) of unit 96?",
            ("It relates to a son", "पुत्रीय = relating to a son, for obtaining a son."),
            [("It relates to a daughter", "A daughter would be दुहितृ; the word is from पुत्र."),
             ("It is done by the son", "पुत्रीय is an adjective of the rite, not its doer."),
             ("It cures a disease", "No disease is named in this unit.")],
            "पुत्रीयं विधानम् = the procedure relating to a son.",
            "पुत्र + ईय = relating to a son."),
        T(mcq("transfer", 5, "Built like पुत्रीय (relating to a son), what does पर्वतीय mean?",
              ("Relating to a mountain", "-ईय makes an adjective: relating to X."),
              [("A small mountain", "-ईय does not make a small form."),
               ("Many mountains", "-ईय does not make a plural."),
               ("Without a mountain", "-ईय does not deny; that would need अ- or -वर्जित.")],
              "पुत्र + ईय = relating to a son; पर्वत + ईय = relating to a mountain.",
              "X + ईय = relating to X."),
          "The ending -ईय added to a noun makes an adjective: relating to, belonging to that thing."),
    ],
}

# ---------------------------------------------------------------- unit 97
AUTHORED["97"] = {
    "title": "शुद्धायास्तु मंत्रवर्जित",
    "question": "What does the fragment of unit 97 say, and what is unsure in it?",
    "rule": ("A two-word fragment: 'but for the purified woman, without mantra' (card reading). It has no verb and no stated "
             "noun; probably the procedure for her is without a mantra."),
    "limits": ("Low confidence. The sense is conjectural. A reviewer's undecided conjecture reads the first word as शूद्रायाः "
               "(for a śūdra woman) instead of शुद्धायाः; no question rests on that word. मंत्रवर्जित may have lost a final -म्. "
               "How it joins the procedure of unit 96 is unclear."),
    "explain_hi": ("यह केवल दो शब्दों का टुकड़ा है, इसमें न क्रिया है न कोई कही गई संज्ञा। "
                   "कार्ड का पाठ: ‘किन्तु शुद्ध हुई स्त्री के लिए, मन्त्र से रहित’; सम्भवतः अर्थ यह कि उसके लिए विधि बिना मन्त्र के हो। "
                   "पहला शब्द पक्का नहीं: एक अनिर्णीत अनुमान इसे ‘शूद्रायाः’ (शूद्र स्त्री के लिए) पढ़ता है, क्योंकि छपाई में द्ध और द्र गड़बड़ाते हैं। "
                   "यह इकाई ९६ की विधि से जुड़ी लगती है, पर कैसे, स्पष्ट नहीं।"),
    "hook": "दो शब्द, एक बात पक्की: मन्त्र-वर्जित।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What does मंत्रवर्जित in unit 97 mean?",
            ("Without mantra", "मन्त्र + वर्जित: excluded of the mantra, without mantra."),
            [("With many mantras", "वर्जित means left out, not many."),
             ("Chosen by mantra", "वर्जित means left out, not chosen."),
             ("Before the mantra", "वर्जित says nothing of time.")],
            "मंत्रवर्जित = without mantra.",
            "वर्जित = left out, devoid of."),
        match(1, "Match each sure part of unit 97 to its meaning on the card.",
              [["तु", "but"], ["मन्त्र", "mantra"], ["वर्जित", "without, left out"]],
              "These three parts are sure; the first word's reading is not.",
              "तु = but; मन्त्र = mantra; वर्जित = without."),
        T(multi("extend", 2, "Which are true of the line of unit 97?",
                [("It has no verb of its own", "Right: the data calls it a fragment with no verb."),
                 ("It states no noun for मंत्रवर्जित", "Right: no noun is stated; the procedure is supplied."),
                 ("It gives the words of the mantra", "The mantra's words come in unit 103."),
                 ("It names the teacher as its subject", "The teacher is named in unit 96, not here.")],
                [0, 1],
                "Two words, no verb, no stated noun: the sense is supplied from the context of unit 96.",
                "Fragment: verb and noun are understood."),
          "A fragment has no verb of its own; its sense is supplied from the context, so it is held loosely."),
        mcq("discriminate", 3, "In शुद्धायास्तु, why is a स् written before तु?",
            ("A visarga before त becomes स्", "-आयाः + तु → -आयास्तु: visarga before त → स्."),
            [("तु always begins with स्", "The particle is तु; the स् is the changed visarga."),
             ("A म् before त becomes स्", "म् before त gives anusvara, not स्."),
             ("It marks a plural ending", "The स् comes from sandhi, not from a plural.")],
            "The first word ends in a visarga (-आयाः); before तु that visarga becomes स्.",
            "Visarga + त → स्त."),
        mcq("apply", 4, "By the card, which word of unit 97 has an unsure reading?",
            ("The first word, शुद्धायाः", "An undecided conjecture reads it as शूद्रायाः; so no question rests on its sense."),
            [("The particle तु", "तु (but) is sure."),
             ("The word मन्त्र", "मन्त्र is sure; only मंत्रवर्जित may have lost a final -म्, which leaves its sense unchanged."),
             ("No word; all are sure", "The card marks the first word as unsure.")],
            "The first word may be शुद्धायाः or शूद्रायाः (undecided); तु and मन्त्रवर्जित are read with more certainty.",
            "Unsure reading: hold it loosely."),
        T(mcq("transfer", 5, "Built like मन्त्रवर्जित (without mantra), what does दोषवर्जित mean?",
              ("Free of faults", "X + वर्जित = without X: दोष (fault) + वर्जित."),
              [("Full of faults", "वर्जित means left out, the opposite of full."),
               ("Causing faults", "वर्जित does not mean causing."),
               ("Found by faults", "वर्जित does not mean found.")],
              "मन्त्रवर्जित = without mantra; दोषवर्जित = without faults.",
              "X-वर्जित = without X."),
          "वर्जित (left out) after a noun makes 'without that noun'."),
    ],
}

# ---------------------------------------------------------------- unit 98
AUTHORED["98"] = {
    "title": "यादृशं च पुत्रमाशासीत",
    "question": "By unit 98, what is the woman to be told to think upon?",
    "rule": ("The woman is to be told: 'Think upon the janapadas (regions or their peoples) that have the form, complexion and "
             "conduct of whatever kind of son you may wish for.'"),
    "limits": ("Janapada can be a region or its people; both senses are possible. The unit gives the instruction only; it "
               "does not say how long she thinks upon them or what follows (the next unit adds that she follows their ways)."),
    "explain_hi": ("स्त्री से यह कहना चाहिए: तुम जिस प्रकार के पुत्र की आशा करो, उसके रूप, वर्ण और आचरण वाले जनपदों का चिन्तन करो। "
                   "जनपद यानी प्रदेश या वहाँ के लोग (मानक); दोनों अर्थ सम्भव हैं। "
                   "समास का ‘तद्’ उस चाहे गए पुत्र की ओर संकेत करता है। "
                   "‘इति’ उद्धृत निर्देश को बन्द करता है, और ‘वाच्या’ यानी ‘कही जानी चाहिए’।"),
    "hook": "जैसा पुत्र चाहो, वैसे जनपदों का ध्यान करो।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 98, what is the woman told to think upon?",
            ("The janapadas like the wished son", "तद्रूपवर्णचरितान् जनपदान् अनुचिन्तय."),
            [("The deities named in the mantra", "The deities come later, in unit 104."),
             ("Her own parents and her elders", "Her parents are not named in this unit."),
             ("The teacher and his procedure", "The teacher belongs to unit 96.")],
            "Think upon the regions (peoples) with the form, complexion and conduct of the son you wish for.",
            "जनपद = region or its people."),
        order(1, "Put these parts of unit 98 in their printed order.",
              ["यादृशं च", "पुत्रमाशासीत", "तद्रूपवर्णचरितान्", "जनपदानुचिंतयेति", "स्त्री वाच्या"],
              "Whatever kind of son she may wish for, with that form, complexion and conduct, think upon the janapadas: "
              "so the woman is to be told.",
              "यादृशम् → पुत्रम् आशासीत → तद्रूपवर्णचरितान् → जनपदान् अनुचिन्तय इति → स्त्री वाच्या."),
        T(match(2, "Match each word of unit 98 to its meaning on the card.",
                [["रूप", "form"], ["वर्ण", "complexion"], ["चरित", "conduct"], ["जनपद", "region or its people"],
                 ["वाच्या", "is to be told"]],
                "Three words give what the son should share; one names whom to think upon; one gives the duty of telling.",
                "रूप, वर्ण, चरित, जनपद, वाच्या.", role="extend"),
          "The son's three marks are रूप (form), वर्ण (complexion) and चरित (conduct)."),
        mcq("discriminate", 3, "Which split of चिंतयेति, the end of जनपदानुचिंतयेति, is right?",
            ("चिन्तय + इति", "अ + इ → ए: चिन्तय + इति → चिन्तयेति."),
            [("चिन्तय + एति", "अ + ए would give ऐ: चिन्तयैति."),
             ("चिन्तयि + इति", "इ + इ would give ई: चिन्तयीति."),
             ("चिन्तये + ति", "ति is not a word; the closing word is इति.")],
            "अनुचिन्तय (think upon) + इति (thus): the इति closes the quoted instruction.",
            "अ + इ → ए."),
        mcq("apply", 4, "In तद्रूपवर्णचरितान्, to whom does तद् (that) point?",
            ("The son she wishes for", "The data: तद् refers to the wished-for son."),
            [("The region she thinks upon", "The regions are what have his form; तद् is the son."),
             ("The teacher of unit 96", "The teacher is not in this compound."),
             ("The husband of the woman", "No husband is named in this unit.")],
            "Regions having the form, complexion and conduct of that (wished-for) son.",
            "तद् = that (son)."),
        T(mcq("transfer", 5, "By the rule of चिन्तयेति, how is गच्छ + इति written when joined?",
              ("गच्छेति", "अ + इ → ए, as in चिन्तय + इति."),
              [("गच्छैति", "ऐ comes from अ + ए, not अ + इ."),
               ("गच्छीति", "अ + इ does not give ई."),
               ("गच्छयिति", "No य् is inserted between अ and इ.")],
              "चिन्तय + इति → चिन्तयेति; so गच्छ + इति → गच्छेति.",
              "अ + इ → ए."),
          "अ or आ before इ or ई merges into ए (गुण)."),
    ],
}

# ---------------------------------------------------------------- unit 99
AUTHORED["99"] = {
    "title": "तज्जनपदाहारविहार",
    "question": "By unit 99, what of that region should she follow?",
    "rule": ("And she should follow the food (āhāra), way of living (vihāra), practices (upacāra) and accessories "
             "(paricchada) of that region."),
    "limits": ("The whole line is one printed compound. The glosses of vihāra, upacāra and paricchada are the plainest senses; "
               "each has others (upacāra: treatment, service; paricchada: retinue, apparel). The subject (the woman) is "
               "understood from unit 98."),
    "explain_hi": ("पूरी पंक्ति एक लम्बा छपा समास है, फिर ‘च’ और क्रिया। "
                   "वह स्त्री उस जनपद (जिसका चिन्तन इकाई ९८ में कहा गया) के आहार, विहार, उपचार और परिच्छद का अनुसरण करे। "
                   "विहार = रहन-सहन, उपचार = आचार या सेवा, परिच्छद = सामग्री या वेश; इन शब्दों के और अर्थ भी सम्भव हैं। "
                   "कर्ता (स्त्री) पिछली इकाई से समझा जाता है।"),
    "hook": "जिस जनपद का ध्यान, उसी का खान-पान, रहन-सहन, वेश।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 99, what should she follow?",
            ("That region's food, living, practices, accessories", "आहार-विहार-उपचार-परिच्छदान् अनुविदधीत."),
            [("The teacher's words, his rites, fasts and vows", "The teacher is not named in this unit."),
             ("Her husband's food, his sleep, work and dress", "The husband is not named in this unit."),
             ("The mantra's words, metre, and its gods", "The mantra comes later, in units 103-104.")],
            "She should follow the food, way of living, practices and accessories of that region.",
            "अनुविदधीत = should follow, adopt."),
        order(1, "Put the four things of unit 99 in the order of the compound.",
              ["आहार", "विहार", "उपचार", "परिच्छद"],
              "Food, way of living, practices, accessories: the order of the printed compound.",
              "आहार → विहार → उपचार → परिच्छद."),
        T(match(2, "Match each word of unit 99 to its meaning on the card.",
                [["आहार", "food"], ["विहार", "way of living"], ["उपचार", "practice, service"],
                 ["परिच्छद", "accessories, dress"], ["अनुविदधीत", "should follow"]],
                "Four nouns of the compound, then the verb that governs them.",
                "आहार, विहार, उपचार, परिच्छद, अनुविदधीत.", role="extend"),
          "The four nouns form one dvandva (a list compound), all governed by अनुविदधीत."),
        mcq("discriminate", 3, "In unit 99, which split of परिच्छदांश्च is right?",
            ("परिच्छदान् + च", "न् before च becomes anusvara + श्: -दान् + च → -दांश्च."),
            [("परिच्छदाः + च", "आः + च would give परिच्छदाश्च, with no anusvara."),
             ("परिच्छदम् + च", "म् + च gives ं च with no श्."),
             ("परिच्छदांश् + च", "परिच्छदांश् is not a form; the ending is -आन्.")],
            "परिच्छदान् (accessories, accusative plural) + च (and).",
            "न् + च → ंश्च."),
        mcq("apply", 4, "In unit 99, the ways of which region should she follow?",
            ("The region she thinks upon in unit 98", "तद्-जनपद: that region, the one of unit 98."),
            [("Her husband's own birthplace", "No husband or birthplace is named."),
             ("The teacher's native region", "The teacher is not in this unit."),
             ("Any region with plenty of food", "तद् points to the regions of unit 98, not to any region.")],
            "तज्जनपद = that region: the one with the form, complexion and conduct of the wished son.",
            "तद् = that (region of unit 98)."),
        T(mcq("transfer", 5, "By the rule of परिच्छदांश्च, how is तान् + च written when joined?",
              ("तांश्च", "न् before च → anusvara + श्, as in परिच्छदान् + च."),
              [("तान्च", "In sandhi न् does not stay unchanged before च."),
               ("ताश्च", "The nasal is not lost; it stays as anusvara."),
               ("तान्श्च", "The न् itself turns to anusvara, not न् + श्.")],
              "परिच्छदान् + च → परिच्छदांश्च; so तान् + च → तांश्च.",
              "न् + च → ंश्च."),
          "A final न् before च or छ becomes anusvara with श् inserted (ंश्च)."),
    ],
}

# ---------------------------------------------------------------- unit 100
AUTHORED["100"] = {
    "title": "कर्माते च पुमान्",
    "question": "How does unit 100 say the man is to be prepared, and how does he mount the bed?",
    "rule": ("At the end of the rite the man, chaste for a month, fed on śāli rice with ghee and milk, not over-fed, happy, "
             "garlanded, cheerful, refreshed, in white, at a night-time approved by the muhūrta-expert, thinking auspicious "
             "things, mounts the well-spread bed with the right foot."),
    "limits": ("कर्माते is read as कर्मान्ते and अभिप्राइय as अभिप्राश्य (having eaten): both corrections are possible, not sure. "
               "प्राक् is taken as 'toward the east' but can mean 'first', so no question rests on the direction. The rite whose end "
               "is meant is not named here."),
    "explain_hi": ("यह एक लम्बा गद्य-वाक्य है, जिसकी एक ही मुख्य क्रिया है: आरोहेत् (चढ़े)। "
                   "कर्म के अन्त में पुरुष, जो एक मास ब्रह्मचारी रहा हो, घी और दूध के साथ शालि (धान, Oryza sativa; मानक) का भात खाकर, "
                   "अधिक न खाया हुआ, सुखी, माला पहने, प्रसन्न मन, तृप्त अंग, श्वेत वस्त्र पहने हो। "
                   "मौहूर्तिक (मुहूर्त जानने वाला, ज्योतिषी) जिस रात्रि-भाग को माने, उसमें शुभ बातें सोचता हुआ, "
                   "वह भली-भाँति बिछी शय्या पर दाहिने पैर से चढ़े। ‘प्राक्’ को पूर्व दिशा माना गया है, पर ‘पहले’ भी सम्भव है।"),
    "hook": "मास भर ब्रह्मचर्य, घी-दूध-भात, श्वेत वस्त्र, दाहिना पैर।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 100, with which foot does the man mount the bed?",
            ("With the right foot", "दक्षिणेन पादेन: with the right foot."),
            [("With the left foot", "The left foot is the woman's, in unit 101."),
             ("With both feet at once", "The unit names one foot, the right."),
             ("The unit names no foot", "It names the right foot (दक्षिणेन पादेन).")],
            "He should mount the well-spread bed with the right foot.",
            "दक्षिण = right; पाद = foot."),
        order(1, "Put these parts of unit 100 in their printed order.",
              ["पुमान्मासंब्रह्मचारी", "सर्पिःक्षीराभ्यां शाल्योदनम्", "शुक्लनिवसनो", "मौहूर्तिकानुमते रात्रिभागे",
               "दक्षिणेन पादेन"],
              "Chaste for a month, rice with ghee and milk, white clothes, the approved part of the night, the right foot.",
              "ब्रह्मचारी → शाल्योदन → शुक्लनिवसन → रात्रिभाग → दक्षिण पाद."),
        T(match(2, "Match each word of unit 100 to its meaning on the card.",
                [["ब्रह्मचारी", "chaste"], ["स्रग्वी", "wearing a garland"], ["शुक्लनिवसन", "in white clothes"],
                 ["मौहूर्तिक", "muhūrta-expert (astrologer)"], ["स्वास्तीर्ण", "well spread"]],
                "Three words describe the man, one the expert who approves the time, one the bed.",
                "ब्रह्मचारी, स्रग्वी, शुक्लनिवसन, मौहूर्तिक, स्वास्तीर्ण.", role="extend"),
          "Most of the man's marks are nominative adjectives agreeing with पुमान् (ब्रह्मचारी, स्रग्वी, शुक्लनिवसनः); the time and the bed are in other cases."),
        mcq("discriminate", 3, "Which split of नात्याशितः is right?",
            ("न + अति + आशितः", "अ + अ → आ (नाति); इ + आ → या (अत्याशितः)."),
            [("ना + अत्याशितः", "ना is not a word; the negative is न."),
             ("न + अति + अशितः", "इ + अ would give य, not या: नात्यशितः."),
             ("न + इति + आशितः", "अ + इ would give ए: नेत्याशितः.")],
            "न (not) + अति (over) + आशितः (fed): not over-fed.",
            "अ + अ → आ; इ + आ → या."),
        multi("apply", 4, "Which does unit 100 ask of the man?",
              [("Chastity for a month", "Right: मासं ब्रह्मचारी."),
               ("White clothes", "Right: शुक्लनिवसनः."),
               ("A garland", "Right: स्रग्वी."),
               ("Eating his fill and more", "नात्याशितः: he is not over-fed."),
               ("Mounting with the left foot", "He uses the right foot; the left is the woman's (unit 101).")],
              [0, 1, 2],
              "Chaste for a month, garlanded, in white clothes; not over-fed; the right foot.",
              "ब्रह्मचारी, स्रग्वी, शुक्लनिवसनः; नात्याशितः; दक्षिणेन पादेन."),
        T(mcq("transfer", 5, "By the rule of स्वास्तीर्णम् (सु + आस्तीर्णम्), how is सु + आगतम् written when joined?",
              ("स्वागतम्", "उ + आ → वा, as in सु + आस्तीर्णम्."),
              [("स्वगतम्", "The long आ stays: व् + आ, not व् + अ."),
               ("सोगतम्", "उ + आ does not give ओ."),
               ("सुवागतम्", "The उ becomes व्; it does not stay before it.")],
              "सु + आस्तीर्णम् → स्वास्तीर्णम्; so सु + आगतम् → स्वागतम्.",
              "उ + a different vowel → व् + that vowel."),
          "A final उ before a different vowel becomes व् and the vowel follows unchanged."),
    ],
}

# ---------------------------------------------------------------- unit 101
AUTHORED["101"] = {
    "title": "तद्विधैव च प्रमदा",
    "question": "How does unit 101 say the woman is prepared, and how does she ascend the bed?",
    "rule": ("The woman, prepared in just that way, with limbs made thin and oil and māṣa (black gram) as the chief food, "
             "should first ascend the bed with the left foot, on the right of the man."),
    "limits": ("'Chief' for उत्तर in तैलमाषोत्तराहारा is conjectural (it may mean additional). दक्षिणतः is taken with पुरुषस्य "
               "(on the man's right), a reading of the card. Māṣa = black gram, Vigna mungo (standard)."),
    "explain_hi": ("इकाई १०० के पुरुष की तरह स्त्री की तैयारी। ‘तद्विधा एव’ यानी उसी प्रकार तैयार की गई। "
                   "वह कृश अंगों वाली हो, और उसका आहार तेल और माष (उड़द, Vigna mungo; मानक) प्रधान हो; ‘उत्तर’ का अर्थ ‘प्रधान’ अनुमानित है। "
                   "वह पहले बाएँ पैर से पुरुष के दाहिनी ओर शय्या पर चढ़े। "
                   "पुरुष का दाहिना पैर, स्त्री का बायाँ: दोनों इकाइयाँ एक जोड़ी बनाती हैं।"),
    "hook": "पुरुष: घी-दूध, दाहिना पैर; स्त्री: तेल-उड़द, बायाँ पैर।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 101, which two foods are named in the woman's diet?",
            ("Oil and māṣa (black gram)", "तैल-माष-उत्तर-आहारा: oil and māṣa."),
            [("Ghee and milk with rice", "Ghee, milk and śāli rice are the man's, in unit 100."),
             ("Honey and sugarcane", "Neither is named in this unit."),
             ("Curd and barley", "Neither is named in this unit.")],
            "Her food has oil and māṣa (black gram) at its head.",
            "तैल = oil; माष = black gram."),
        order(1, "Put these parts of unit 101 in their printed order.",
              ["तद्विधैव च प्रमदा", "कर्शितांगी", "तैलमाषोत्तराहारा", "पूर्वं वामपादेन", "पुरुषस्य दक्षिणतः",
               "शय्यामधिरोहेत्"],
              "The woman likewise, thin-limbed, oil and māṣa as chief food, first with the left foot, on the man's right, "
              "ascends the bed.",
              "प्रमदा → कर्शिताङ्गी → तैलमाष → वामपाद → दक्षिणतः → अधिरोहेत्."),
        T(match(2, "Match each word of unit 101 to its meaning on the card.",
                [["प्रमदा", "woman"], ["कर्शिताङ्गी", "with limbs made thin"], ["माष", "black gram"], ["वाम", "left"],
                 ["अधिरोहेत्", "should ascend"]],
                "One word names her, two describe her preparation, two give how she ascends.",
                "प्रमदा, कर्शिताङ्गी, माष, वाम, अधिरोहेत्.", role="extend"),
          "माष is black gram (Vigna mungo), the standard identification of the data."),
        mcq("discriminate", 3, "Which split of तद्विधैव is right?",
            ("तद्विधा + एव", "आ + ए → ऐ: तद्विधा + एव → तद्विधैव."),
            [("तद्विध + इव", "अ + इ would give ए: तद्विधेव."),
             ("तद्विधै + व", "तद्विधै is not a word; व is not एव."),
             ("तद्विधः + एव", "अः before ए would give तद्विध एव.")],
            "तद्विधा (of that kind, feminine) + एव (just).",
            "आ + ए → ऐ."),
        mcq("apply", 4, "Unit 100 has the man mount with the right foot. By unit 101, how does the woman ascend?",
            ("First, with the left foot", "पूर्वं वामपादेन: first, with the left foot."),
            [("After him, with the right foot", "The unit says left foot and पूर्वम् (first)."),
             ("With both feet, after the man", "One foot, the left, and पूर्वम् = first."),
             ("She does not ascend at all", "शय्याम् अधिरोहेत्: she should ascend the bed.")],
            "She should first ascend the bed with the left foot, on the man's right.",
            "वाम = left; पूर्वम् = first."),
        T(mcq("transfer", 5, "By the rule of तद्विधैव, how is सदा + एव written when joined?",
              ("सदैव", "आ + ए → ऐ, as in तद्विधा + एव."),
              [("सदेव", "आ + ए gives ऐ, not ए."),
               ("सदाएव", "The two vowels must merge in sandhi."),
               ("सदायेव", "No य् is inserted between आ and ए.")],
              "तद्विधा + एव → तद्विधैव; so सदा + एव → सदैव.",
              "आ + ए → ऐ."),
          "अ or आ before ए or ऐ merges into ऐ (वृद्धि)."),
    ],
}

# ---------------------------------------------------------------- unit 102
AUTHORED["102"] = {
    "title": "तत्र मंत्रं प्रयुंजीत",
    "question": "What does unit 102 say is to be done there?",
    "rule": "There one should employ (recite) the mantra; the mantra itself follows in unit 103.",
    "limits": "The subject is not stated; the man is probably meant (conjectural), so the questions ask only that no subject is named.",
    "explain_hi": ("छोटी गद्य-पंक्ति: वहाँ (या तब) मन्त्र का प्रयोग करे। "
                   "कर्ता नहीं बताया गया; सम्भवतः पुरुष, पर यह अनुमान है। "
                   "मन्त्र स्वयं अगली इकाई (१०३) में दिया गया है। "
                   "‘प्रयुञ्जीत’ विधि-लिङ् (आत्मनेपद) है: प्रयोग करे।"),
    "hook": "तत्र: अब मन्त्र।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 102, what should one employ there?",
            ("The mantra (मन्त्रम्)", "तत्र मन्त्रं प्रयुञ्जीत."),
            [("Cold water (शीतोदकम्)", "Cold water comes at the end, in unit 106."),
             ("Oil (तैलम्)", "Oil is the woman's food in unit 101."),
             ("A garland (स्रज्)", "The garland is worn by the man in unit 100.")],
            "There one should employ the mantra.",
            "मन्त्र = mantra; प्रयुञ्जीत = should employ."),
        order(1, "Put the words of unit 102 in their printed order.",
              ["तत्र", "मंत्रं", "प्रयुंजीत"],
              "There, the mantra, should employ.",
              "तत्र → मन्त्रम् → प्रयुञ्जीत."),
        T(match(2, "Match each word of unit 102 to its meaning on the card.",
                [["तत्र", "there, then"], ["मन्त्र", "mantra"], ["प्रयुञ्जीत", "should employ, recite"]],
                "Three words make the whole line.",
                "तत्र, मन्त्र, प्रयुञ्जीत.", role="extend"),
          "प्रयुञ्जीत is an optative (3rd singular, ātmanepada): should employ."),
        mcq("discriminate", 3, "What does unit 102 itself state about who employs the mantra?",
            ("No subject is named in the line", "The subject is not stated; the data only guesses the man (conjectural)."),
            [("The teacher, named as upādhyāya", "The teacher is named in unit 96, not here."),
             ("The woman, named as pramadā", "प्रमदा is in unit 101, not here."),
             ("Both partners, by a dual verb", "प्रयुञ्जीत is singular; the dual verb is in unit 105.")],
            "The line has no stated subject; any guess is conjectural.",
            "Unstated subject: hold the guess loosely."),
        mcq("apply", 4, "Where is the mantra announced in unit 102 given?",
            ("In the next unit, 103", "The data: the mantra is given in the next unit, 103."),
            [("In unit 96, with the teacher", "Unit 96 names the procedure, not the mantra text."),
             ("Nowhere in this chapter", "It follows at once, in unit 103."),
             ("Inside unit 102 itself", "Unit 102 only says to employ it.")],
            "Unit 102 announces the mantra; unit 103 gives it.",
            "Announcement, then text."),
        T(mcq("transfer", 5, "Like प्रयुञ्जीत (should employ), what does the invented line वैद्य औषधं प्रयुञ्जीत say?",
              ("The physician should employ the medicine", "प्रयुञ्जीत = should employ (optative)."),
              [("The physician employed the medicine", "The optative is not a past tense."),
               ("The physician will employ medicine", "The optative is not a future tense."),
               ("The medicine should employ the physician", "वैद्यः is the subject (nominative); औषधम् the object.")],
              "The optative gives 'should': वैद्य (= वैद्यः) औषधं प्रयुञ्जीत = the physician should employ the medicine.",
              "Optative = should, may."),
          "The optative mood (-ईत, -एत, -एत्) gives an instruction: should do."),
    ],
}

# ---------------------------------------------------------------- unit 103
AUTHORED["103"] = {
    "title": "आहिरसि आयुरसि",
    "question": "What does the mantra of unit 103 say to its addressee, and whom does it ask to place it?",
    "rule": ("The mantra: you are the ahi; you are life; you are the support on every side. May Dhātṛ place you; may "
             "Vidhātṛ place you. Be with brahmavarcas (brahma-splendour)."),
    "limits": ("The printed आहिरसि is read as अहिरसि; the sense of ahi here is unclear (serpent is the plain meaning), so no "
               "question rests on it. Whom 'you' addresses is not stated. The closing इति ends the mantra."),
    "explain_hi": ("यह इकाई १०२ में कहा गया मन्त्र है। तुम अहि हो, तुम आयु हो, तुम सब ओर प्रतिष्ठा (आधार) हो। "
                   "धाता तुम्हें स्थापित करे, विधाता तुम्हें स्थापित करे; ब्रह्मवर्चस (आध्यात्मिक तेज) से युक्त होओ। "
                   "‘अहि’ का यहाँ अर्थ अस्पष्ट है (साधारण अर्थ साँप), और छपा दीर्घ ‘आ’ छपाई की भूल लगता है। "
                   "‘तुम’ किसे कहा गया, यह नहीं बताया गया; अन्त का ‘इति’ मन्त्र को समाप्त करता है।"),
    "hook": "आयु हो, प्रतिष्ठा हो; धाता-विधाता स्थापित करें।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In the mantra of unit 103, who are asked to place you?",
            ("Dhātṛ and Vidhātṛ", "धाता त्वा दधातु, विधाता त्वा दधातु."),
            [("Brahmā and Viṣṇu", "They are named in unit 104, not here."),
             ("Mitra and Varuṇa", "They are named in unit 104, not here."),
             ("The two Aśvins", "They are named in unit 104, not here.")],
            "May Dhātṛ place you; may Vidhātṛ place you.",
            "धाता = Establisher; विधाता = Arranger."),
        order(1, "Put these phrases of the mantra of unit 103 in their printed order.",
              ["आयुरसि", "सर्वतः प्रतिष्ठासि", "धाता त्वा दधातु", "विधाता त्वा दधातु", "ब्रह्मवर्चसा भव"],
              "You are life; you are support on every side; may Dhātṛ place you; may Vidhātṛ place you; be with brahmavarcas.",
              "आयुः → प्रतिष्ठा → धाता → विधाता → ब्रह्मवर्चसा."),
        T(match(2, "Match each word of unit 103 to its meaning on the card.",
                [["आयुः", "life"], ["प्रतिष्ठा", "support, foundation"], ["धाता", "Dhātṛ, the Establisher"],
                 ["दधातु", "may he place"], ["ब्रह्मवर्चस्", "brahma-splendour"]],
                "Two words say what 'you' are, two make the wish, one gives the last blessing.",
                "आयुः, प्रतिष्ठा, धाता, दधातु, ब्रह्मवर्चस्.", role="extend"),
          "दधातु is an imperative of √धा (place): may he place; it carries the wish of the mantra."),
        mcq("discriminate", 3, "Which split of आयुरसि is right?",
            ("आयुः + असि", "A visarga after उ becomes र् before a vowel."),
            [("आयु + रसि", "रसि is not a word; the verb is असि."),
             ("आयुर + असि", "आयुर is not a form; the word is आयुः."),
             ("आयुम् + असि", "म् before a vowel would give आयुमसि.")],
            "आयुः (life) + असि (you are).",
            "Visarga after उ → र् before a vowel."),
        mcq("apply", 4, "What is भव in ब्रह्मवर्चसा भव?",
            ("A command: be!", "भव = 2nd singular imperative of √भू: be."),
            [("A statement: he is", "'He is' would be भवति."),
             ("A past form: you were", "'You were' would be अभवः."),
             ("A wish: may he become", "'May he become' would be भवतु.")],
            "ब्रह्मवर्चसा भव = be with brahma-splendour.",
            "भव = be (2 sg. imperative)."),
        T(mcq("transfer", 5, "By the rule of आयुरसि, how is धेनुः + अस्ति written when joined?",
              ("धेनुरस्ति", "Visarga after उ → र् before a vowel, as in आयुः + असि."),
              [("धेनोस्ति", "उः does not become ओ; that change is for अः."),
               ("धेनुस्ति", "The vowel अ of अस्ति cannot vanish."),
               ("धेनुसस्ति", "Visarga becomes स् only before त/थ.")],
              "आयुः + असि → आयुरसि; so धेनुः + अस्ति → धेनुरस्ति.",
              "उः + vowel → उर् + vowel."),
          "A visarga after उ (or इ, ए …) becomes र् before a vowel or voiced consonant."),
    ],
}

# ---------------------------------------------------------------- unit 104
AUTHORED["104"] = {
    "title": "ब्रह्मा बृहस्पतिर्विष्णुः",
    "question": "Which deities does unit 104 name, and what does it ask them to bestow?",
    "rule": ("Brahmā, Bṛhaspati, Viṣṇu, Soma, Sūrya, the two Aśvins, Bhaga, and then Mitra and Varuṇa: may they bestow on "
             "me a heroic son."),
    "limits": ("It appears to continue the mantra of unit 103 (GROUPING). मे is taken as 'for me' (dative or genitive form). "
               "The closing इति ends the mantra. The unit only names the deities and the wish."),
    "explain_hi": ("मन्त्र का अगला भाग, जो इकाई १०३ से आगे चलता लगता है। "
                   "देवताओं की सूची: ब्रह्मा, बृहस्पति, विष्णु, सोम, सूर्य, दोनों अश्विनीकुमार, भग, फिर मित्र और वरुण। "
                   "ये सब मुझे वीर पुत्र प्रदान करें (दधतु, बहुवचन, क्योंकि कर्ता अनेक देवता हैं)। "
                   "अन्त का ‘इति’ मन्त्र को समाप्त करता है।"),
    "hook": "देवताओं की सूची, एक माँग: वीर पुत्र।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 104, what are the deities asked to bestow?",
            ("A heroic son (वीरं सुतम्)", "वीरं दधतु मे सुतम्."),
            [("Long life (आयुः)", "Life is named in the mantra of unit 103, not asked here."),
             ("Great wealth (महद् धनम्)", "Wealth is not named in this unit."),
             ("A daughter (दुहिता)", "The unit asks for a son (सुत).")],
            "May they bestow on me a heroic son.",
            "वीर = heroic; सुत = son."),
        order(1, "Put these deities of unit 104 in their printed order.",
              ["ब्रह्मा", "बृहस्पतिः", "विष्णुः", "सोमः", "सूर्यः", "अश्विनौ"],
              "Brahmā, Bṛhaspati, Viṣṇu, Soma, Sūrya, the two Aśvins; then Bhaga, Mitra and Varuṇa.",
              "ब्रह्मा → बृहस्पति → विष्णु → सोम → सूर्य → अश्विनौ."),
        T(match(2, "Match each word of unit 104 to its meaning on the card.",
                [["अश्विनौ", "the two Aśvins"], ["मित्रावरुणौ", "Mitra and Varuṇa"], ["वीर", "heroic"], ["सुत", "son"],
                 ["दधतु", "may they bestow"]],
                "Two words name paired deities; three make the wish.",
                "अश्विनौ, मित्रावरुणौ, वीर, सुत, दधतु.", role="extend"),
          "The ending -औ in अश्विनौ and मित्रावरुणौ marks a pair here (nominative dual)."),
        mcq("discriminate", 3, "Which split of भगोऽथ is right?",
            ("भगः + अथ", "अः + अ → ओ, and the lost अ is marked ऽ."),
            [("भगो + अथ", "भगो is not the nominative; the form is भगः."),
             ("भग + अथ", "अ + अ would give भगाथ."),
             ("भगम् + अथ", "म् before a vowel would give भगमथ.")],
            "भगः (Bhaga) + अथ (and then).",
            "अः + अ → ओऽ."),
        mcq("apply", 4, "Why is the verb दधतु in unit 104 plural, unlike दधातु in unit 103?",
            ("Its subject is the many deities", "दधतु = 3rd plural: may they bestow."),
            [("It agrees with the son, सुतम्", "सुतम् is the object (accusative), not the subject."),
             ("It agrees with the word मे", "मे means 'for me'; it is not the subject."),
             ("It honours the woman addressed", "No woman is addressed in this unit.")],
            "The deities named in the unit together are the subject: may they bestow.",
            "दधातु = may he place; दधतु = may they bestow."),
        T(mcq("transfer", 5, "By the rule of भगोऽथ, how is देवः + अयम् written when joined?",
              ("देवोऽयम्", "अः + अ → ओ, with ऽ for the lost अ."),
              [("देवायम्", "अः + अ does not give आ."),
               ("देवरयम्", "र् comes after a vowel other than अ/आ."),
               ("देव अयम्", "That gap comes before other vowels, not before अ.")],
              "भगः + अथ → भगोऽथ; so देवः + अयम् → देवोऽयम्.",
              "अः + अ → ओऽ."),
          "Final अः before अ becomes ओ and the अ is dropped, written ऽ."),
    ],
}

# ---------------------------------------------------------------- unit 105
AUTHORED["105"] = {
    "title": "ततः परस्परं सामभिः",
    "question": "By unit 105, how should the two come together?",
    "rule": "Then, having soothed each other with gentle words (sāman), the two should lie together, with joy and agreeably.",
    "limits": ("साम here as gentle, conciliatory words is probable (it can also be a Vedic chant). The printed संवेसेतां is read "
               "as संविशेताम्, a possible correction; the dual ending shows both partners as the subject."),
    "explain_hi": ("मन्त्र के बाद: तब परस्पर मधुर वचनों से एक-दूसरे को सान्त्वना देकर, हर्ष के साथ, अनुकूल रीति से दोनों सहवास करें। "
                   "‘साम’ यहाँ मधुर, मनाने वाले वचन हैं (सम्भावित); इसका अर्थ सामवेद का गान भी हो सकता है। "
                   "क्रिया द्विवचन में है, इसलिए दोनों साथी कर्ता हैं। "
                   "छपा ‘संवेसेतां’ नियमित रूप नहीं; ‘संविशेताम्’ पढ़ा गया है।"),
    "hook": "मीठे बोल, हर्ष, अनुकूलता: दोनों साथ।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 105, in what manner should the two lie together?",
            ("With joy and agreeably", "सहर्षम् अनुकूलम्: with joy, agreeably."),
            [("In silence and in haste", "Neither is said; they speak gentle words first."),
             ("With fear and in secret", "Neither word is in the unit."),
             ("After a fast of a day", "No fast is named in this unit.")],
            "Having soothed each other, the two lie together with joy and agreeably.",
            "सहर्ष = with joy; अनुकूल = agreeable."),
        order(1, "Put these parts of unit 105 in their printed order.",
              ["ततः", "परस्परं", "सामभिरभिसांत्व्य", "सहर्षमनुकूलं", "संवेसेतां"],
              "Then, each other, having soothed with gentle words, with joy and agreeably, the two should lie together.",
              "ततः → परस्परम् → अभिसान्त्व्य → सहर्षम् अनुकूलम् → संविशेताम्."),
        T(match(2, "Match each word of unit 105 to its meaning on the card.",
                [["परस्परम्", "each other"], ["अभिसान्त्व्य", "having soothed"], ["सहर्षम्", "with joy"],
                 ["अनुकूलम्", "agreeably"]],
                "Four words give how the union is to be: mutual, soothing, joyful, agreeable.",
                "परस्परम्, अभिसान्त्व्य, सहर्षम्, अनुकूलम्.", role="extend"),
          "अभिसान्त्व्य is an absolutive: having soothed, done before the main verb."),
        mcq("discriminate", 3, "Which split of सामभिरभिसांत्व्य is right?",
            ("सामभिः + अभिसान्त्व्य", "A visarga after इ becomes र् before a vowel."),
            [("सामभि + रभिसान्त्व्य", "रभिसान्त्व्य is not a word of the card."),
             ("सामभिर + अभिसान्त्व्य", "सामभिर is not a form; the ending is -भिः."),
             ("सामभिम् + अभिसान्त्व्य", "म् before a vowel would give सामभिमभि….")],
            "सामभिः (with gentle words) + अभिसान्त्व्य (having soothed).",
            "Visarga after इ → र् before a vowel."),
        mcq("apply", 4, "What does the dual verb of unit 105 show?",
            ("Both partners are the subject", "The dual ending: the two should lie together."),
            [("Only the man is the subject", "A dual verb has two doers, not one."),
             ("Only the woman is the subject", "A dual verb has two doers, not one."),
             ("The teacher and the man act", "The teacher is not in this unit.")],
            "The verb is dual (3rd person, optative): the two partners together.",
            "Dual verb = two doers."),
        T(mcq("transfer", 5, "Built like अभिसान्त्व्य (having soothed), what does उपविश्य mean?",
              ("Having sat down", "Prefix + root + -य = absolutive: having done."),
              [("To sit down", "'To sit down' would be the infinitive उपवेष्टुम्."),
               ("Sitting down now", "That would be a present participle."),
               ("He should sit down", "That would be the optative उपविशेत्.")],
              "अभि + सान्त्व् + य = having soothed; उप + विश् + य = having sat down.",
              "Prefix + root + -य = having done."),
          "With a prefix, the absolutive (having done) ends in -य instead of -त्वा."),
    ],
}

# ---------------------------------------------------------------- unit 106
AUTHORED["106"] = {
    "title": "पर्यांते चैनां शीतोदकेन",
    "question": "What does unit 106 say is done at the end?",
    "rule": "And at the end he should suddenly sprinkle her with cold water.",
    "limits": ("The subject is not stated; the man is understood (conjectural). The printed पर्यांते and पारिषिंचेत् are read as "
               "पर्यन्ते and परिषिञ्चेत् (possible corrections). The unit gives no reason for the sprinkling."),
    "explain_hi": ("और अन्त में उसे (स्त्री को) अचानक ठण्डे जल से सींचे। "
                   "कर्ता नहीं बताया गया; पुरुष समझा जाता है (अनुमान)। ‘एनाम्’ स्त्री की ओर संकेत करता है। "
                   "छपे ‘पर्यांते’ और ‘पारिषिंचेत्’ में दीर्घ ‘आ’ अपेक्षित नहीं; ‘पर्यन्ते’ और ‘परिषिञ्चेत्’ पढ़े गए हैं। "
                   "इसका कारण इकाई में नहीं दिया गया।"),
    "hook": "अन्त में, अचानक, ठण्डा जल।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 106, with what is she sprinkled?",
            ("With cold water", "शीतोदकेन: with cold water."),
            [("With warm oil", "No oil is named in this unit."),
             ("With fresh milk", "No milk is named in this unit."),
             ("With melted ghee", "No ghee is named in this unit.")],
            "He should suddenly sprinkle her with cold water.",
            "शीत = cold; उदक = water."),
        order(1, "Put the words of unit 106 in their printed order.",
              ["पर्यांते", "चैनां", "शीतोदकेन", "सहसा", "पारिषिंचेत्"],
              "At the end, and her, with cold water, suddenly, should sprinkle.",
              "पर्यन्ते → च एनाम् → शीतोदकेन → सहसा → परिषिञ्चेत्."),
        T(match(2, "Match each word of unit 106 to its meaning on the card.",
                [["पर्यन्त", "end"], ["एनाम्", "her"], ["शीत", "cold"], ["उदक", "water"], ["सहसा", "suddenly"]],
                "When, whom, with what, and how.",
                "पर्यन्त, एनाम्, शीत, उदक, सहसा.", role="extend"),
          "एनाम् is a feminine accusative pronoun: her (the woman)."),
        mcq("discriminate", 3, "Which split of चैनाम् is right?",
            ("च + एनाम्", "अ + ए → ऐ: च + एनाम् → चैनाम्."),
            [("चै + नाम्", "चै is not a word; नाम् is not the pronoun."),
             ("च + इनाम्", "अ + इ would give ए: चेनाम्."),
             ("च + अनाम्", "अ + अ would give आ: चानाम्.")],
            "च (and) + एनाम् (her).",
            "अ + ए → ऐ."),
        mcq("apply", 4, "By unit 106, when and how is the sprinkling done?",
            ("At the end, and suddenly", "पर्यन्ते … सहसा: at the end, suddenly."),
            [("Before he mounts the bed", "The unit says at the end (पर्यन्ते)."),
             ("At the start, and slowly", "पर्यन्ते = at the end; सहसा = suddenly."),
             ("After a month of chastity", "The month of chastity is in unit 100.")],
            "At the end he should suddenly sprinkle her with cold water.",
            "पर्यन्ते = at the end; सहसा = suddenly."),
        T(mcq("transfer", 5, "By the rule of शीतोदकेन (शीत + उदकेन), how is गङ्गा + उदकम् written when joined?",
              ("गङ्गोदकम्", "आ + उ → ओ, as अ + उ → ओ in शीत + उदकेन."),
              [("गङ्गौदकम्", "आ + उ gives ओ, not औ."),
               ("गङ्गुदकम्", "The आ cannot simply vanish."),
               ("गङ्गादकम्", "The उ cannot simply vanish.")],
              "शीत + उदकेन → शीतोदकेन; so गङ्गा + उदकम् → गङ्गोदकम्.",
              "अ/आ + उ → ओ."),
          "अ or आ before उ or ऊ merges into ओ (गुण)."),
    ],
}

# ===================================================================== NOTES_HI
NOTES_HI = {
    "94": ("विश्वास मध्यम। ‘आहारानुरोधात्’ = आहार के अनुरोध (अनुसरण) से; कारण का अर्थ पूरी तरह स्पष्ट नहीं। "
           "‘रात्रिषु’ समझा जाता है, छपा नहीं। छपा ‘ततःपुमान्’ = ततः पुमान् (छपाई में जुड़ा, अक्षर नहीं बदला)। "
           "सन्धियाँ: तु + आहार → त्वाहार; आहारानुरोधात् + अयुग्मासु → आहारानुरोधादयुग्मासु; स्त्री + आकृतिः → स्त्र्याकृतिः; "
           "आकृतिः + दुर्बलः → आकृतिर्दुर्बलः; दुर्बलः + हीनाङ्गः → दुर्बलो हीनाङ्गः। वाक्य इकाई ९५ में आगे।"),
    "95": ("विश्वास मध्यम। ‘जायते’ क्रिया इकाई ९४ से ली गई (GROUPING)। छपा ‘दुर्बलाहीनांगी’ = दुर्बला हीनाङ्गी (जुड़ा छपा, अक्षर ठीक)। "
           "दूसरी पंक्ति में ‘रात्रिषु’ समझा जाता है। ‘नपुंसक’ व्याकरण में नपुंसकलिङ्ग भी है, पर यहाँ व्यक्ति अभिप्रेत है। "
           "सन्धियाँ: पुरुष + आकृतिः → पुरुषाकृतिः; त्रयोदश्योः + तु → त्रयोदश्योस्तु; नपुंसकम् + स्यात् → नपुंसकं स्यात्।"),
    "96": ("विश्वास मध्यम। ‘पुत्रीय’ विशेषण: पुत्र-सम्बन्धी। विधि का वर्णन इस इकाई में नहीं। उपाध्याय = शिक्षक; पुरोहित के रूप में, सम्भावित। "
           "सन्धियाँ: अथ + उपाध्यायः → अथोपाध्यायः; विधानम् + आचरेत् → विधानमाचरेत्।"),
    "97": ("विश्वास कम। बिना क्रिया और बिना संज्ञा का टुकड़ा; अर्थ (विधि मन्त्र-रहित) अनुमान है। "
           "एक अनिर्णीत अनुमान: ‘शुद्धायास्तु’ OCR की भूल से ‘शूद्रायास्तु’ (शूद्र स्त्री के लिए) हो सकता है (द्ध/द्र की गड़बड़)। "
           "‘मंत्रवर्जित’ के अन्त में नपुंसक -म् छूटा हो सकता है (‘मन्त्रवर्जितम्’), पर छपा रूप भी चल सकता है। "
           "सन्धि: -आयाः + तु → -आयास्तु। यह इकाई ९६ की विधि से जुड़ी लगती है, कैसे, अस्पष्ट।"),
    "98": ("विश्वास मध्यम। जनपद = प्रदेश या वहाँ के लोग; दोनों अर्थ सम्भव। समास का ‘तद्’ चाहे गए पुत्र की ओर। ‘इति’ निर्देश बन्द करता है। "
           "सन्धियाँ: यादृशम् + च → यादृशं च; पुत्रम् + आशासीत → पुत्रमाशासीत; अनुचिन्तय + इति → अनुचिन्तयेति। "
           "ध्यान दें: छपा ‘जनपदानुचिंतय’ कार्ड में जनपदान् + अनुचिन्तय माना गया; नियमित सन्धि में ‘जनपदाननुचिन्तय’ होता, छपे रूप में एक न दिखता है।"),
    "99": ("विश्वास मध्यम। पूरी पंक्ति एक छपा शब्द-समूह: तद्-जनपद + आहार-विहार-उपचार-परिच्छद (द्वन्द्व) + च + क्रिया। "
           "विहार, उपचार, परिच्छद के और अर्थ भी (उपचार = चिकित्सा/सेवा; परिच्छद = परिवार/वेश)। कर्ता (स्त्री) इकाई ९८ से। "
           "सन्धियाँ: तद् + जनपद → तज्जनपद; विहार + उपचार → विहारोपचार; परिच्छदान् + च → परिच्छदांश्च; च + अनुविदधीत → चानुविदधीत।"),
    "100": ("विश्वास मध्यम। छपा ‘कर्माते’ सम्भवतः ‘कर्मान्ते’ (अनुस्वार/न छूटा)। छपा ‘अभिप्राइय’ कोई रूप नहीं; ‘अभिप्राश्य’ (खाकर) सम्भावित (श को इ पढ़ा गया)। "
            "‘प्रीणितांगः’ = प्रीणिताङ्गः, केवल वर्तनी। ‘प्राक्’ = पूर्व दिशा की ओर लिया गया (‘पहले’ भी सम्भव)। "
            "मौहूर्तिक = ज्योतिषी (मानक); शालि = धान, Oryza sativa (मानक)। "
            "सन्धियाँ: न + अति + आशितः → नात्याशितः; सु + आस्तीर्णम् → स्वास्तीर्णम्; शालि + ओदनम् → शाल्योदनम्; "
            "चिन्तयन् + तद् → चिन्तयंस्तद्; प्राक् + आरोहेत् → प्रागारोहेत्।"),
    "101": ("विश्वास मध्यम। छपा ‘वामपादेनपुरुषस्य’ = वामपादेन पुरुषस्य (जुड़ा छपा)। ‘तद्विधा एव’ = पुरुष की तरह तैयार। "
            "‘उत्तराहारा’ में ‘उत्तर’ = प्रधान लिया गया (अनुमान; ‘अतिरिक्त/बाद का’ भी सम्भव)। माष = उड़द, Vigna mungo (मानक)। "
            "‘दक्षिणतः’ को ‘पुरुषस्य’ के साथ लिया गया। सन्धियाँ: तद्विधा + एव → तद्विधैव; माष + उत्तर → माषोत्तर; शय्याम् + अधिरोहेत् → शय्यामधिरोहेत्।"),
    "102": ("विश्वास ऊँचा। कर्ता नहीं बताया; सम्भवतः पुरुष (अनुमान)। मन्त्र इकाई १०३ में। "
            "छपा ‘मंत्रं प्रयुंजीत’ = मन्त्रं प्रयुञ्जीत (अनुस्वार की वर्तनी)।"),
    "103": ("विश्वास मध्यम। छपा ‘आहिरसि’ अन्यत्र ‘अहिरसि’ पढ़ा जाता है; दीर्घ आ छपाई/लिपि की भूल लगता है। ‘अहि’ का अर्थ यहाँ अस्पष्ट। "
            "छपा ‘दधातुब्रह्मवर्चसा’ = दधातु ब्रह्मवर्चसा (जुड़ा छपा)। अन्त का ‘इति’ मन्त्र समाप्त करता है, अनुवाद नहीं किया। "
            "सन्धियाँ: आयुः + असि → आयुरसि; प्रतिष्ठा + असि → प्रतिष्ठासि; भव + इति → भवेति।"),
    "104": ("विश्वास ऊँचा। देवताओं की सूची इकाई १०३ के मन्त्र को आगे बढ़ाती लगती है (GROUPING); ‘दधतु’ का कर्ता यही देवता। "
            "‘मे’ = मेरे लिए (चतुर्थी/षष्ठी)। अन्त का ‘इति’ मन्त्र समाप्त करता है। "
            "सन्धियाँ: बृहस्पतिः + विष्णुः → बृहस्पतिर्विष्णुः; सूर्यः + तथा → सूर्यस्तथा; तथा + अश्विनौ → तथाऽश्विनौ; "
            "भगः + अथ → भगोऽथ; सुतम् + इति → सुतमिति।"),
    "105": ("विश्वास मध्यम। छपा ‘संवेसेतां’ नियमित रूप नहीं; सम्-√विश् का द्विवचन विधिलिङ् ‘संविशेताम्’ सम्भावित। "
            "‘साम’ = मधुर, मनाने वाले वचन (सम्भावित; वैदिक गान भी हो सकता है)। द्विवचन: दोनों साथी कर्ता। "
            "सन्धियाँ: सामभिः + अभिसान्त्व्य → सामभिरभिसान्त्व्य; सहर्षम् + अनुकूलम् → सहर्षमनुकूलम्।"),
    "106": ("विश्वास मध्यम। छपा ‘पर्यांते’ सम्भवतः ‘पर्यन्ते’ (दीर्घ आ अपेक्षित नहीं); छपा ‘पारिषिंचेत्’ सम्भवतः ‘परिषिञ्चेत्’ (उपसर्ग परि-)। "
            "कर्ता नहीं बताया; पुरुष समझा जाता है (अनुमान)। ‘एनाम्’ = स्त्री को। "
            "सन्धियाँ: च + एनाम् → चैनाम्; शीत + उदकेन → शीतोदकेन।"),
}

# ===================================================================== AIDS
AIDS = {
    "94": {
        "diagram": {"groups": [
            {"label": "शर्त (आहार के अनुसार, अर्थ अस्पष्ट)", "items": ["विषम रात्रियों में शुक्र अधिक", "सम रात्रियों में शुक्र कम"]},
            {"label": "परिणाम: पुरुष, पर", "items": ["स्त्री-आकृति", "दुर्बल", "या हीनांग"]}]},
        "sandhi": ("उ + आ → वा: तु + आहार → त्वाहार · त् + स्वर → द्: आहारानुरोधात् + अयुग्मासु → आहारानुरोधादयुग्मासु · "
                   "ई + आ → या: स्त्री + आकृतिः → स्त्र्याकृतिः · इः + द → इर्द: आकृतिः + दुर्बलः → आकृतिर्दुर्बलः · "
                   "अः + ह → ओ ह: दुर्बलः + हीनाङ्गः → दुर्बलो हीनाङ्गः।"),
        "frame": "यदि (विषम में अधिक, सम में कम) → ततः (पुरुष, पर स्त्री-आकृति, दुर्बल या हीनांग) जायते। स्त्री की बात इकाई ९५ में।",
    },
    "95": {
        "contrast": ("इकाई ९४ का पुरुष: स्त्री-आकृति, दुर्बल या हीनांग ↔ इकाई ९५ की स्त्री: पुरुष-आकृति, दुर्बला या हीनांगी। "
                     "और ११वीं, १३वीं रात्रि: नपुंसक।"),
        "sandhi": ("अ + आ → आ: पुरुष + आकृतिः → पुरुषाकृतिः · इः + द → इर्द: आकृतिः + दुर्बला → आकृतिर्दुर्बला · "
                   "ओः + त → ओस्त: त्रयोदश्योः + तु → त्रयोदश्योस्तु।"),
        "anchors": "११ और १३: दोनों विषम संख्याएँ, बीच में १२ छोड़कर (मेरी याद-पद्धति)।",
    },
    "96": {
        "frame": "अथ (नया प्रसंग) → उपाध्यायः (कर्ता) → पुत्रीयं विधानम् (कर्म) → आचरेत् (करे)।",
        "sandhi": "अ + उ → ओ: अथ + उपाध्यायः → अथोपाध्यायः · म् + स्वर: विधानम् + आचरेत् → विधानमाचरेत्।",
        "puns": "केवल सुनने की सहायता: ‘पुत्र-ईय’, पुत्र के लिए जो विधि।",
    },
    "97": {
        "frame": "केवल दो शब्द: [पहला शब्द, पाठ अनिश्चित] + तु (किन्तु) + मन्त्रवर्जित (मन्त्र-रहित)। क्रिया और संज्ञा समझी जाती हैं।",
        "sandhi": "आः + त → आस्त: -आयाः + तु → -आयास्तु (पहले शब्द का पाठ जो भी हो)।",
    },
    "98": {
        "chain": {"steps": ["जैसा पुत्र चाहे", "उसके रूप, वर्ण, चरित वाले", "जनपदों का चिन्तन करो", "ऐसा स्त्री से कहना चाहिए"]},
        "sandhi": ("म् + स्वर: पुत्रम् + आशासीत → पुत्रमाशासीत · अ + इ → ए: अनुचिन्तय + इति → अनुचिन्तयेति · "
                   "म् + च → ं च: यादृशम् + च → यादृशं च।"),
        "letters": "पुत्र के तीन गुण: रू-व-च (रूप, वर्ण, चरित)।",
    },
    "99": {
        "diagram": {"groups": [{"label": "उस जनपद के", "items": ["आहार", "विहार", "उपचार", "परिच्छद"]},
                               {"label": "क्रिया", "items": ["अनुविदधीत (अनुसरण करे)"]}]},
        "sandhi": ("द् + ज → ज्ज: तद् + जनपद → तज्जनपद · अ + उ → ओ: विहार + उपचार → विहारोपचार · "
                   "न् + च → ंश्च: परिच्छदान् + च → परिच्छदांश्च · अ + अ → आ: च + अनुविदधीत → चानुविदधीत।"),
        "chunks": "तज्जनपद | आहार | विहार | उपचार | परिच्छदांश्च | अनुविदधीत।",
    },
    "100": {
        "chain": {"steps": ["कर्म के अन्त में", "एक मास ब्रह्मचारी", "घी-दूध के साथ शालि-भात, अधिक नहीं",
                            "सुखी, माला, प्रसन्न, तृप्त अंग", "श्वेत वस्त्र", "मुहूर्त-ज्ञ से मान्य रात्रि-भाग",
                            "शुभ चिन्तन करता", "दाहिने पैर से शय्या पर"]},
        "sandhi": ("न + अति + आशितः → नात्याशितः (अ + अ → आ, इ + आ → या) · सु + आस्तीर्णम् → स्वास्तीर्णम् (उ + आ → वा) · "
                   "शालि + ओदनम् → शाल्योदनम् (इ + ओ → यो) · प्राक् + आरोहेत् → प्रागारोहेत् (क् + स्वर → ग्)।"),
        "frame": "एक ही मुख्य क्रिया: आरोहेत् (चढ़े)। बाकी सब शब्द ‘पुमान्’ के विशेषण या समय-स्थान बताते हैं।",
        "pegs": "मेरा बनाया चित्र: श्वेत वस्त्र, गले में माला, हाथ में घी-दूध-भात की थाली, दाहिना पैर आगे। (केवल याद के लिए)",
    },
    "101": {
        "contrast": ("पुरुष (इकाई १००): घी-दूध के साथ शालि-भात, दाहिना पैर ↔ स्त्री (इकाई १०१): तेल और माष, बायाँ पैर, "
                     "पहले, पुरुष के दाहिनी ओर।"),
        "sandhi": ("आ + ए → ऐ: तद्विधा + एव → तद्विधैव · अ + उ → ओ: माष + उत्तर → माषोत्तर · "
                   "म् + स्वर: शय्याम् + अधिरोहेत् → शय्यामधिरोहेत्।"),
        "chunks": "तद्विधैव च प्रमदा | कर्शितांगी | तैलमाषोत्तराहारा | पूर्वं वामपादेन | पुरुषस्य दक्षिणतः | शय्यामधिरोहेत्।",
    },
    "102": {
        "frame": "तत्र (वहाँ) → मन्त्रं प्रयुञ्जीत (मन्त्र का प्रयोग करे) → मन्त्र इकाई १०३ में।",
        "sandhi": "म् + प → ं प: मन्त्रम् + प्रयुञ्जीत → मन्त्रं प्रयुञ्जीत।",
    },
    "103": {
        "chunks": "आहिरसि (अर्थ अस्पष्ट) | आयुरसि | सर्वतः प्रतिष्ठासि | धाता त्वा दधातु | विधाता त्वा दधातु | ब्रह्मवर्चसा भवेति।",
        "sandhi": ("उः + अ → उर: आयुः + असि → आयुरसि · आ + अ → आ: प्रतिष्ठा + असि → प्रतिष्ठासि · "
                   "अ + इ → ए: भव + इति → भवेति।"),
        "anchors": "गिनकर याद: ‘असि’ (तुम हो) तीन बार, फिर ‘त्वा दधातु’ (तुम्हें स्थापित करे) दो बार।",
    },
    "104": {
        "diagram": {"groups": [{"label": "देवता (छपे क्रम में)",
                                "items": ["ब्रह्मा", "बृहस्पति", "विष्णु", "सोम", "सूर्य", "दोनों अश्विन्", "भग", "मित्र-वरुण"]},
                               {"label": "माँग", "items": ["वीर पुत्र दें"]}]},
        "sandhi": ("इः + व → इर्व: बृहस्पतिः + विष्णुः → बृहस्पतिर्विष्णुः · अः + त → अस्त: सूर्यः + तथा → सूर्यस्तथा · "
                   "अः + अ → ओऽ: भगः + अथ → भगोऽथ · म् + स्वर: सुतम् + इति → सुतमिति।"),
        "chunks": "ब्रह्मा बृहस्पतिर्विष्णुः | सोमः सूर्यस्तथाऽश्विनौ | भगोऽथ मित्रावरुणौ | वीरं दधतु मे सुतमिति।",
    },
    "105": {
        "chain": {"steps": ["परस्पर मधुर वचनों से सान्त्वना", "हर्ष के साथ", "अनुकूल रीति से", "दोनों सहवास करें"]},
        "sandhi": "इः + अ → इर: सामभिः + अभिसान्त्व्य → सामभिरभिसान्त्व्य · म् + स्वर: सहर्षम् + अनुकूलम् → सहर्षमनुकूलम्।",
    },
    "106": {
        "frame": "पर्यन्ते (कब) → एनाम् (किसे) → शीतोदकेन (किससे) → सहसा (कैसे) → परिषिञ्चेत् (सींचे)।",
        "sandhi": "अ + ए → ऐ: च + एनाम् → चैनाम् · अ + उ → ओ: शीत + उदकेन → शीतोदकेन।",
    },
}

# ===================================================================== IMAGE_SPECS
IMAGE_SPECS = {
    ("94", "diagram"): {
        "file": "sh1-vishama-shukra-94.svg",
        "alt": ("Flowchart of unit 94: owing to diet (sense unclear), more semen in the odd nights and less in the even "
                "nights; then a male is born of female form, weak, or deficient in limb."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"आहार के अनुसार<br/>(अर्थ अस्पष्ट)\"] --> B[\"विषम रात्रियों में<br/>शुक्र अधिक\"]\n"
                 "  A --> C[\"सम रात्रियों में<br/>शुक्र कम\"]\n"
                 "  B --> D[\"पुरुष: स्त्री-आकृति,<br/>दुर्बल या हीनांग\"]\n"
                 "  C --> D\n"),
    },
    ("95", "contrast"): {
        "file": "sh1-akriti-napumsaka-95.svg",
        "alt": ("Table of units 94 and 95: the male of unit 94 is of female form, weak or deficient in limb; the female of "
                "unit 95 is of male form, weak or deficient in limb."),
        "type": "table",
        "title": "आकृति का उलटफेर (इकाई ९४-९५)",
        "heads": ["पुरुष (इकाई ९४)", "स्त्री (इकाई ९५)"],
        "rows": [["स्त्री-आकृति", "पुरुष-आकृति"],
                 ["दुर्बल", "दुर्बला"],
                 ["या हीनांग", "या हीनांगी"]],
    },
    ("98", "chain"): {
        "file": "sh1-janapada-chintana-98.svg",
        "alt": ("Chain of unit 98: whatever son she wishes for; regions with his form, complexion and conduct; think upon "
                "those regions; so the woman is to be told."),
        "type": "chain",
        "title": "स्त्री से कहा जाए (इकाई ९८)",
        "steps": ["जैसा पुत्र चाहे", "उसके रूप, वर्ण, चरित वाले", "जनपदों का चिन्तन करो", "ऐसा स्त्री से कहना चाहिए"],
    },
    ("99", "diagram"): {
        "file": "sh1-janapada-anusarana-99.svg",
        "alt": ("Table of unit 99 in the order of the compound: of that region she should follow the food, the way of "
                "living, the practices (or service) and the accessories (or dress)."),
        "type": "table",
        "title": "उस जनपद का अनुसरण करे (इकाई ९९)",
        "heads": ["शब्द (समास के क्रम में)", "अर्थ"],
        "rows": [["आहार", "भोजन"], ["विहार", "रहन-सहन"], ["उपचार", "आचार, सेवा"], ["परिच्छद", "सामग्री, वेश"]],
    },
    ("100", "chain"): {
        "file": "sh1-purusha-tayari-100.svg",
        "alt": ("Chain of unit 100 in printed order: at the end of the rite; chaste for a month; shali rice with ghee and "
                "milk, not over-fed; happy, garlanded, cheerful, refreshed; white clothes; a part of the night approved by "
                "the muhurta-expert; thinking auspicious things; mounting the bed with the right foot."),
        "type": "chain",
        "title": "पुरुष की तैयारी (इकाई १००, छपे क्रम में)",
        "steps": ["कर्म के अन्त में", "एक मास ब्रह्मचारी", "घी-दूध के साथ शालि-भात, अधिक नहीं",
                  "सुखी, माला, प्रसन्न, तृप्त अंग", "श्वेत वस्त्र", "मुहूर्त-ज्ञ से मान्य रात्रि-भाग",
                  "शुभ चिन्तन करता", "दाहिने पैर से शय्या पर"],
    },
    ("101", "contrast"): {
        "file": "sh1-purusha-stri-pada-101.svg",
        "alt": ("Table of units 100 and 101: the man has shali rice with ghee and milk and mounts with the right foot; the "
                "woman has oil and masha (black gram) and ascends first with the left foot, on the man's right."),
        "type": "table",
        "title": "पुरुष और स्त्री (इकाई १००-१०१)",
        "heads": ["पुरुष (इकाई १००)", "स्त्री (इकाई १०१)"],
        "rows": [["घी-दूध के साथ शालि-भात", "तेल और माष (उड़द)"],
                 ["दाहिना पैर", "बायाँ पैर, पहले"],
                 ["शय्या पर चढ़े", "पुरुष के दाहिनी ओर शय्या पर चढ़े"]],
    },
    ("104", "diagram"): {
        "file": "sh1-devata-suta-104.svg",
        "alt": ("Table of unit 104 in printed order: Brahma, Brihaspati, Vishnu, Soma, Surya, the two Ashvins, Bhaga, "
                "Mitra and Varuna, asked to bestow a heroic son."),
        "type": "table",
        "title": "वीर पुत्र दें: देवता (इकाई १०४)",
        "heads": ["क्रम", "देवता"],
        "rows": [["१", "ब्रह्मा"], ["२", "बृहस्पति"], ["३", "विष्णु"], ["४", "सोम"], ["५", "सूर्य"],
                 ["६", "दोनों अश्विन्"], ["७", "भग"], ["८", "मित्र-वरुण"]],
    },
}
