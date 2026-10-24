from helpers import mcq, match, order, fill, multi, accepts


AUTHORED = {}

# ---------------------------------------------------------------- unit 26
AUTHORED["26"] = {
    "title": "वैशेषिकं लिंगसंकरे",
    "question": "What does unit 26 say about a mixture of signs, and how sure is its reading?",
    "rule": ("In a mixture of signs (लिंगसंकर), the distinguishing determination goes by where there is greater "
             "abundance (भूयस्त्व); from that, the states belong to one or the other. The reading is conjectural."),
    "limits": ("Low confidence. The printed यवो is read as यतः (where) and ततोऽन्यतरा as ततोऽन्यतराः only as possible "
               "corrections; वैशेषिकम् may also be the first member of a compound. The unit does not name the signs that "
               "are mixed. No question rests on these readings. Prose, not a verse."),
    "explain_hi": ("यह गद्य-पंक्ति लिंगों (चिह्नों) के मिश्रण की बात करती है। "
                   "अनुमानित पाठ पर अर्थ है: लिंगों के मिश्रण में विशेष निर्धारण वहाँ से होता है जहाँ अधिकता (भूयस्त्व) हो, "
                   "और उससे भाव दोनों में से किसी एक के होते हैं। "
                   "छपा ‘यवो’ (जौ) यहाँ अर्थ नहीं देता; डेटा इसे ‘यतः’ पढ़ता है, जो केवल सम्भावित सुधार है। "
                   "कौन-से चिह्न मिले हैं, यह इकाई नहीं कहती। "
                   "विश्वास निम्न है, इसलिए प्रश्न केवल पक्के शब्दों और सन्धि पर हैं।"),
    "hook": "चिह्न मिले हों तो जो अधिक हो, उसी से निर्णय (अनुमानित पाठ)।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 26, what does लिंगसंकरे mean?",
            ("In a mixture of signs", "लिंग-संकरे: sign; in a mixture (locative)."),
            [("In the absence of signs", "संकर is mixture, not absence."),
             ("In the order of signs", "No order is named; संकर means mixture."),
             ("In a single clear sign", "A mixture is the opposite of a single sign.")],
            "लिंगसंकर = mixture of signs; -ए gives the locative, in.",
            "लिंग = sign, संकर = mixture."),
        order(1, "Put these printed pieces of unit 26 in the line's order.",
              ["वैशेषिकं", "लिंगसंकरे तु", "भूयस्त्वं", "ततोऽन्यतरा भावाः"],
              "Distinguishing, in a mixture of signs but, greater abundance, from that one or the other states.",
              "वैशेषिकं → लिंगसंकरे तु → (यवो) भूयस्त्वं → ततोऽन्यतरा भावाः."),
        match(2, "Match each sure word of unit 26 to its meaning on the card.",
              [["लिंगसंकर", "mixture of signs"], ["भूयस्त्व", "greater abundance"],
               ["भाव", "state"], ["तु", "but"]],
              "These words are sure; यवो, the ending of अन्यतरा and the role of वैशेषिकं stay doubtful.",
              "लिंगसंकर, भूयस्त्व, भाव, तु.", role="extend",
              teaches="-त्व makes an abstract noun: भूयस् (more) + त्व = भूयस्त्व, greater abundance."),
        mcq("discriminate", 3, "Which split of the start of ततोऽन्यतरा is right?",
            ("ततः + अन्यतरा", "अः before अ becomes ओ and the अ is dropped (ऽ): ततः + अन्यतरा → ततोऽन्यतरा."),
            [("तत् + अन्यतरा", "त् + अ would give तदन्यतरा."),
             ("ततम् + अन्यतरा", "A final म् would give ततमन्यतरा."),
             ("ततो + न्यतरा", "न्यतरा is not a word; the word is अन्यतर.")],
            "ततः (from that) + अन्यतरा(ः) (one or the other); the avagraha marks the dropped अ.",
            "अः + अ → ओऽ."),
        multi("apply", 4, "Which statements about unit 26 match the card?",
              [("The unit names the signs that are mixed", "No signs are named in unit 26."),
               ("The data takes यवो as barley in this line", "The flag says barley makes no sense here."),
               ("The reading of the unit is of low confidence", "Right: confidence is low; यवो → यतः is only possible."),
               ("भूयस्त्व means greater abundance", "Right: the card glosses it so.")],
              [2, 3],
              "Two statements follow from the card; the signs are not named and यवो is not read as barley.",
              "Low confidence; sure words: लिंगसंकर, भूयस्त्व, भाव."),
        mcq("transfer", 5, "By the rule of ततोऽन्यतरा, how is रामः + अपि (Rāma too) written?",
            ("रामोऽपि", "अः + अ → ओ, with the अ dropped (ऽ), as ततः + अन्यतरा."),
            [("रामापि", "The visarga does not vanish into a long आ."),
             ("रामरपि", "र् comes only after vowels other than अ or आ."),
             ("रामसपि", "The visarga does not become स् before a vowel.")],
            "रामः + अपि = रामोऽपि, like ततः + अन्यतरा = ततोऽन्यतरा.",
            "अः + अ → ओऽ.",
            teaches="A visarga after अ before अ: अः becomes ओ and the next अ is dropped (ऽ): ततः + अन्यतरा → ततोऽन्यतरा."),
    ],
}

# ---------------------------------------------------------------- unit 27
AUTHORED["27"] = {
    "title": "तद्यथा",
    "question": "What does the formula तद्यथा of unit 27 do?",
    "rule": "तद्यथा = तत् + यथा, namely: a stock formula that introduces the list of unit 28. Final त् before य is written द्.",
    "limits": "Two words only; it names nothing itself. The list it introduces is in unit 28. Prose, not a verse.",
    "explain_hi": ("‘तद्यथा’ एक प्रचलित सूत्र है, जिसका अर्थ है ‘वह जैसे कि’, यानी ‘जैसे’। "
                   "यह आगे की सूची (इकाई 28) की भूमिका है। "
                   "इसमें तत् + यथा है; अन्तिम त् घोष व्यंजन य से पहले द् हो जाता है। "
                   "‘तत्’ नपुंसकलिंग प्रथमा एकवचन है।"),
    "hook": "तद्यथा = ‘जैसे कि’: अब सूची आती है।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By the card, what does तद्यथा in unit 27 introduce?",
            ("The list in unit 28", "The note: the formula introduces the list in line 28 (card 28)."),
            [("The end of the chapter", "The chapter does not end here."),
             ("A quoted verse", "No verse follows; unit 28 is prose."),
             ("The name of a speaker", "No speaker is named.")],
            "तद्यथा opens the list of unit 28.",
            "तद्यथा = namely."),
        mcq("warmup", 1, "What does तद्यथा mean?",
            ("Namely", "तत् (that) + यथा (as): that is, namely."),
            [("Therefore", "Therefore is तस्मात्, in unit 34."),
             ("And then", "And then is तदा च, in unit 31."),
             ("Others however", "Others however is अन्ये तु, in unit 36.")],
            "तद्यथा = namely, as follows.",
            "तद्यथा = namely."),
        fill(2, "तद्यथा = ____ + यथा (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("तत्", None, "तद्", "tad"),
             "तत् (that) + यथा (as); त् before य is written द्.",
             "A final त् before a voiced sound such as य becomes द्: तत् + यथा → तद्यथा.",
             "तत् + यथा → तद्यथा."),
        mcq("discriminate", 3, "Which split of तद्यथा is right?",
            ("तत् + यथा", "त् before the voiced य becomes द्."),
            [("तम् + यथा", "A final म् would give तं यथा."),
             ("तत् + अथा", "अथा is not a word; the word is यथा."),
             ("तद्य + था", "Neither तद्य nor था is a word here.")],
            "तत् (that) + यथा (as, namely).",
            "त् + य → द्य."),
        multi("apply", 4, "Which statements about unit 27 match the card?",
              [("तद्यथा itself names a woman-making state", "It names nothing; the states come in unit 28."),
               ("तत् in तद्यथा is neuter nominative singular", "Right: the card labels tat n. nom. sg."),
               ("तत् here is ablative, from that", "From that would be तस्मात्; तत् is nominative."),
               ("The formula introduces the list of unit 28", "Right: the note says so.")],
              [1, 3],
              "तद्यथा = तत् (n. nom. sg.) + यथा, introducing unit 28's list.",
              "तत् = n. nom. sg.; तद्यथा introduces a list."),
        mcq("transfer", 5, "By the rule of तद्यथा, how is एतत् + वनम् (this forest) written?",
            ("एतद्वनम्", "त् before the voiced व becomes द्, as तत् + यथा → तद्यथा."),
            [("एतत्वनम्", "त् does not stay unvoiced before व."),
             ("एतच्वनम्", "त् becomes च् only before a palatal (च, छ, श), not before व."),
             ("एतन्वनम्", "त् becomes न् only before a nasal.")],
            "एतत् + वनम् = एतद्वनम्, like तत् + यथा = तद्यथा.",
            "Final त् + voiced consonant → द्.",
            teaches="A final त् before a voiced consonant (here य) becomes द्: तत् + यथा → तद्यथा."),
    ],
}

# ---------------------------------------------------------------- unit 28
AUTHORED["28"] = {
    "title": "क्लैब्यं भीरुत्वमवैशारद्यं",
    "question": "By unit 28, which states are the woman-making (स्त्रीकर) states?",
    "rule": ("Woman-making states: klaibya (unmanliness), timidity, lack of confidence, bewilderment, unsteadiness, "
             "heaviness below, lack of compactness, laxity, softness, the states of womb and seed, and other fitting ones."),
    "limits": ("Prose: list and label in one sentence. Klaibya is a trait of unmanliness; impotence is only a probable "
               "modern equivalent. The sense of गर्भाशयबीजभाव and of युक्ताः (fitting, or joined) is not secure; "
               "no question uses them."),
    "explain_hi": ("‘तद्यथा’ के बाद यह सूची आती है, और पूरी पंक्ति एक वाक्य है: ये सब ‘स्त्रीकर भाव’ हैं। "
                   "क्लैब्य (पुरुषत्व की कमी, आधुनिक अर्थ नपुंसकता सम्भावित), भीरुता, आत्मविश्वास की कमी, मोह, अस्थिरता, "
                   "नीचे का भारीपन, गठन की कमी, शिथिलता और मृदुता गिनाई गई हैं। "
                   "फिर गर्भाशय और बीज के भाव, और ‘इसी प्रकार के अन्य उचित’ भाव; इन दोनों का ठीक अर्थ पक्का नहीं। "
                   "अवैशारद्य, अनवस्थान, असंहनन में निषेधार्थक अ-/अन्- है। "
                   "इकाई 29 और 30 इन्हीं से पुंकर और नपुंसककर भाव बताती हैं।"),
    "hook": "डर, ढीलापन, कोमलता, अस्थिरता: ये स्त्रीकर भाव।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 28, what are timidity, laxity and softness called?",
            ("Woman-making states (स्त्रीकरा भावाः)", "The list closes with स्त्रीकराभावाः = स्त्रीकराः भावाः."),
            [("Man-making states (पुंकराः)", "Man-making are the opposite ones, in unit 29."),
             ("Neuter-making states", "Neuter-making are the mixed ones, in unit 30."),
             ("Signs of a stable embryo", "Stability of the embryo comes in unit 38.")],
            "The whole list is labelled woman-making states.",
            "List of unit 28 = स्त्रीकरा भावाः."),
        order(1, "Put these states of unit 28 in the line's order.",
              ["क्लैब्यम्", "भीरुत्वम्", "मोहः", "अधोगुरुत्वम्", "शैथिल्यम्", "मार्दवम्"],
              "Klaibya, timidity, (lack of confidence), bewilderment, (unsteadiness), heaviness below, (lack of "
              "compactness), laxity, softness.",
              "क्लैब्य → भीरुत्व → मोह → अधोगुरुत्व → शैथिल्य → मार्दव."),
        match(2, "Match each state of unit 28 to its meaning.",
              [["भीरुत्व", "timidity"], ["अवैशारद्य", "lack of confidence"], ["अनवस्थान", "unsteadiness"],
               ["शैथिल्य", "laxity"], ["मार्दव", "softness"]],
              "Five of the listed woman-making states.",
              "भीरुत्व, अवैशारद्य, अनवस्थान, शैथिल्य, मार्दव.", role="extend",
              teaches="The negative prefix is अ- before a consonant (अ + संहनन = असंहनन) and अन्- before a vowel (अन् + अवस्थान = अनवस्थान)."),
        mcq("discriminate", 3, "Which is NOT among the woman-making states of unit 28?",
            ("Compactness (संहनन)", "The list has असंहनन, lack of compactness, its opposite."),
            [("Heaviness below (अधोगुरुत्व)", "Named in the list."),
             ("Bewilderment (मोह)", "Named in the list."),
             ("Laxity (शैथिल्य)", "Named in the list.")],
            "Lack of compactness is listed; compactness itself is not.",
            "असंहनन (lack of compactness) is woman-making."),
        multi("apply", 4, "Which states of unit 28 carry the negative prefix अ- or अन्-?",
              [("मार्दव", "मार्दव (softness) has no negative prefix."),
               ("अवैशारद्य", "Right: अ + वैशारद्य, lack of confidence."),
               ("अनवस्थान", "Right: अन् + अवस्थान, unsteadiness."),
               ("मोह", "मोह (bewilderment) has no negative prefix."),
               ("असंहनन", "Right: अ + संहनन, lack of compactness.")],
              [1, 2, 4],
              "Three listed states are negatives of a quality; softness and bewilderment are not.",
              "अ-/अन्- = lacking: अवैशारद्य, अनवस्थान, असंहनन."),
        mcq("transfer", 5, "By the pattern of अनवस्थान and असंहनन, what is the negative of आरोग्य (health)?",
            ("अनारोग्य", "Before a vowel the negative prefix is अन्-: अन् + आरोग्य."),
            [("अआरोग्य", "अ- stands only before a consonant."),
             ("अमारोग्य", "The negative prefix is never अम्-."),
             ("आनारोग्य", "The prefix has a short अ, not आ.")],
            "अन् + आरोग्य = अनारोग्य, ill-health, like अन् + अवस्थान = अनवस्थान.",
            "अ- before a consonant, अन्- before a vowel.",
            teaches="The negative prefix is अ- before a consonant (असंहनन) and अन्- before a vowel (अनवस्थान)."),
    ],
}

# ---------------------------------------------------------------- unit 29
AUTHORED["29"] = {
    "title": "ततो विपरीताः पुंकराः",
    "question": "By unit 29, which states are man-making (पुंकर)?",
    "rule": "Those opposite to these (the woman-making states of unit 28) are man-making. भावाः is understood from unit 28; the copula is understood.",
    "limits": ("Three words, no verb. The unit does not list the opposites one by one; reading a single opposite (e.g. "
               "confidence for lack of confidence) applies its rule. Prose, not a verse."),
    "explain_hi": ("यह छोटी पंक्ति कहती है: इनसे (इकाई 28 के स्त्रीकर भावों से) विपरीत भाव पुरुष बनाने वाले हैं। "
                   "‘भावाः’ शब्द इकाई 28 से समझा जाता है, और ‘हैं’ भी लिखा नहीं गया। "
                   "विपरीत भाव एक-एक करके गिनाए नहीं गए; जैसे अवैशारद्य का विपरीत वैशारद्य, यह नियम लगाकर समझना है। "
                   "‘ततो विपरीताः’ में ततः + विपरीताः है: अः घोष व्यंजन से पहले ओ हो जाता है।"),
    "hook": "स्त्रीकर का उल्टा = पुंकर।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 29, which states are man-making?",
            ("Those opposite to the woman-making ones", "ततो विपरीताः पुंकराः: opposite to these."),
            [("Those mixed with the woman-making ones", "The mixed ones are neuter-making, unit 30."),
             ("The woman-making ones in greater amount", "Unit 29 speaks of opposites, not amounts."),
             ("The states of womb and seed", "Those are among the woman-making states of unit 28.")],
            "Opposites of the unit 28 list are man-making.",
            "विपरीत → पुंकर."),
        order(1, "Put the words of unit 29 in the line's order.",
              ["ततः", "विपरीताः", "पुंकराः"],
              "Than these, opposite, man-making.",
              "ततः → विपरीताः → पुंकराः."),
        match(2, "Match each word of unit 29 to its meaning.",
              [["ततः", "than these"], ["विपरीत", "opposite"], ["पुंकर", "man-making"]],
              "Three words make the sentence; भावाः is understood.",
              "ततः, विपरीत, पुंकर.", role="extend",
              teaches="-कर at the end of a compound means making: पुं- (man) + कर = man-making, as स्त्री + कर = woman-making."),
        mcq("discriminate", 3, "Which word is understood in unit 29 though not printed, by the card?",
            ("भावाः (states), from unit 28", "The note: bhāvāḥ is understood from 28."),
            [("गर्भः (embryo)", "The note supplies states, not embryo."),
             ("दोषाः (doṣas)", "No doṣa is named or supplied."),
             ("स्त्री (woman)", "Woman is not the understood subject.")],
            "The man-making ones are states, as in unit 28.",
            "पुंकराः (भावाः)."),
        mcq("apply", 4, "Applying unit 29, which state would be man-making?",
            ("Confidence, the opposite of अवैशारद्य", "Unit 28 lists lack of confidence; its opposite is man-making."),
            [("Timidity (भीरुत्व)", "Timidity is listed as woman-making in unit 28."),
             ("Softness (मार्दव)", "Softness is listed as woman-making in unit 28."),
             ("Laxity (शैथिल्य)", "Laxity is listed as woman-making in unit 28.")],
            "The opposite of a listed woman-making state is man-making.",
            "Opposite of a स्त्रीकर भाव → पुंकर."),
        mcq("transfer", 5, "By the rule of ततो विपरीताः, how is नरः + गच्छति (the man goes) written?",
            ("नरो गच्छति", "अः before a voiced consonant becomes ओ, as ततः + विपरीताः."),
            [("नरा गच्छति", "The visarga is not replaced by a long आ."),
             ("नरर्गच्छति", "र् comes only after vowels other than अ or आ."),
             ("नरश्गच्छति", "श् comes only before च, छ or श.")],
            "नरः + गच्छति = नरो गच्छति, like ततः + विपरीताः = ततो विपरीताः.",
            "अः + voiced consonant → ओ.",
            teaches="अः before a voiced consonant becomes ओ: ततः + विपरीताः → ततो विपरीताः."),
    ],
}

# ---------------------------------------------------------------- unit 30
AUTHORED["30"] = {
    "title": "संकीर्णा नपुंसककराः",
    "question": "By unit 30, which states make a neuter (नपुंसक)?",
    "rule": ("The mixed (संकीर्ण) states are neuter-making. With units 28 and 29 this gives three classes: the listed "
             "states make a woman, their opposites a man, a mixture a neuter."),
    "limits": ("Two words, no verb; भावाः is understood from unit 28. The unit does not say which states are mixed or in "
               "what proportion. Prose, not a verse."),
    "explain_hi": ("यह पंक्ति तीसरा वर्ग बताती है: मिले-जुले (संकीर्ण) भाव नपुंसक बनाने वाले हैं। "
                   "इकाई 28 के भाव स्त्रीकर, इकाई 29 में उनके विपरीत पुंकर, और यहाँ मिले-जुले नपुंसककर। "
                   "‘भावाः’ और ‘हैं’ समझे जाते हैं। कौन-से भाव किस अनुपात में मिलें, यह नहीं कहा गया। "
                   "‘संकीर्णा नपुंसक’ में संकीर्णाः + नपुंसक है: आः घोष व्यंजन से पहले विसर्ग खो देता है।"),
    "hook": "स्त्रीकर, उल्टे पुंकर, मिले-जुले नपुंसककर।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 30, which states are neuter-making?",
            ("The mixed ones (संकीर्णाः)", "संकीर्णा नपुंसककराः: the mixed ones are neuter-making."),
            [("The opposite ones (विपरीताः)", "The opposite ones are man-making, unit 29."),
             ("The listed ones of unit 28 alone", "Those are woman-making."),
             ("The abundant ones (भूयस्त्व)", "Abundance is the topic of unit 26, not of unit 30.")],
            "Mixed states make a neuter.",
            "संकीर्ण → नपुंसककर."),
        match(1, "Match each class of states (units 28 to 30) to what it makes.",
              [["the list of unit 28", "woman-making (स्त्रीकर)"], ["their opposites", "man-making (पुंकर)"],
               ["mixed ones", "neuter-making (नपुंसककर)"]],
              "Units 28, 29 and 30 give the three classes in this order.",
              "list → स्त्रीकर, opposite → पुंकर, mixed → नपुंसककर."),
        fill(2, "The mixed ones are neuter-making: ____ नपुंसककराः (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("संकीर्णाः", None, "संकीर्णा", "sankirna"),
             "संकीर्णाः (mixed), printed संकीर्णा before नपुंसककराः.",
             "संकीर्ण = mixed; printed संकीर्णा because आः loses its visarga before न.",
             "संकीर्णाः = mixed."),
        mcq("discriminate", 3, "Which split of संकीर्णा नपुंसककराः is right?",
            ("संकीर्णाः + नपुंसककराः", "आः before the voiced न drops its visarga: संकीर्णा नपुंसक-."),
            [("संकीर्णम् + नपुंसककराः", "A final म् would give संकीर्णं नपुंसक-."),
             ("संकीर्णः + नपुंसककराः", "अः before न would give संकीर्णो नपुंसक-."),
             ("संकीर्णात् + नपुंसककराः", "A final त् before न would give संकीर्णान्नपुंसक-.")],
            "संकीर्णाः (mixed, nom. pl.) + नपुंसककराः.",
            "आः + voiced consonant → आ (visarga dropped)."),
        multi("apply", 4, "Which statements about unit 30 match the card?",
              [("संकीर्ण means mixed", "Right: the card glosses saṅkīrṇāḥ as mixed."),
               ("The unit says which states are mixed", "It does not say which states, or in what proportion."),
               ("नपुंसककर means woman-making", "It means neuter-making; woman-making is स्त्रीकर."),
               ("The sentence has no printed verb", "Right: the copula is understood.")],
              [0, 3],
              "Mixed ones are neuter-making; nothing more is stated.",
              "संकीर्णाः (भावाः) नपुंसककराः."),
        mcq("transfer", 5, "By the rule of संकीर्णा नपुंसककराः, how is देवाः + गच्छन्ति (the gods go) written?",
            ("देवा गच्छन्ति", "आः before a voiced consonant drops the visarga."),
            [("देवो गच्छन्ति", "ओ comes from अः, not from आः."),
             ("देवार्गच्छन्ति", "र् comes only after vowels other than अ or आ."),
             ("देवाश्गच्छन्ति", "श् comes only before च, छ or श.")],
            "देवाः + गच्छन्ति = देवा गच्छन्ति, like संकीर्णाः + नपुंसककराः.",
            "आः + voiced consonant → आ.",
            teaches="आः before a voiced consonant loses its visarga: संकीर्णाः + नपुंसककराः → संकीर्णा नपुंसककराः."),
    ],
}

# ---------------------------------------------------------------- unit 31
AUTHORED["31"] = {
    "title": "तदा चास्यचेतना प्रव्यक्ता",
    "question": "By unit 31, what of the embryo becomes fully manifest then?",
    "rule": "And then its consciousness (चेतना) becomes fully manifest. अस्य (its) refers to the embryo.",
    "limits": ("तदा (then) points back to a time given earlier; this unit does not name it. It does not say what "
               "consciousness consists of. Prose, not a verse. The print runs चास्यचेतना together; the split is certain."),
    "explain_hi": ("यह पंक्ति कहती है: ‘और तब इसकी चेतना पूरी तरह प्रकट हो जाती है।’ "
                   "‘अस्य’ (इसकी) गर्भ के लिए है। "
                   "‘तब’ किस समय की ओर इशारा करता है, यह इस इकाई में नहीं कहा गया। "
                   "छपा ‘चास्यचेतना’ = च + अस्य + चेतना (अ + अ → आ)। "
                   "अगली इकाई बताती है कि तब से गर्भ हिलता है और इन्द्रिय-विषयों की इच्छा करता है।"),
    "hook": "तब गर्भ में चेतना जाग उठती है।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 31, what of the embryo becomes fully manifest then?",
            ("Its consciousness (चेतना)", "चेतना प्रव्यक्ता भवति."),
            [("Its heart (हृदय)", "The heart is the topic of unit 33."),
             ("Its sex, male or female", "Sex is not named in unit 31."),
             ("Its colour", "Colour is not named in unit 31.")],
            "Consciousness becomes fully manifest.",
            "चेतना प्रव्यक्ता."),
        order(1, "Put the words of unit 31 in the line's order.",
              ["तदा", "च", "अस्य", "चेतना", "प्रव्यक्ता", "भवति"],
              "Then, and, its, consciousness, fully manifest, becomes.",
              "तदा → च → अस्य → चेतना → प्रव्यक्ता → भवति."),
        match(2, "Match each word of unit 31 to its meaning.",
              [["तदा", "then"], ["अस्य", "its"], ["चेतना", "consciousness"], ["प्रव्यक्ता", "fully manifest"],
               ["भवति", "becomes"]],
              "Five words carry the sentence.",
              "तदा, अस्य, चेतना, प्रव्यक्ता, भवति.", role="extend",
              teaches="प्रव्यक्ता agrees with चेतना (feminine nominative singular): consciousness, fully manifest."),
        mcq("discriminate", 3, "Which split of चास्य is right?",
            ("च + अस्य", "अ + अ → आ: च + अस्य → चास्य."),
            [("च + इस्य", "अ + इ would give चेस्य."),
             ("चत् + अस्य", "A final त् would give चदस्य."),
             ("चम् + अस्य", "A final म् would give चमस्य.")],
            "च (and) + अस्य (its).",
            "अ + अ → आ."),
        mcq("apply", 4, "In unit 31, whose consciousness does अस्य refer to, by the card?",
            ("The embryo's", "The note: asya refers to the embryo."),
            [("The mother's", "For the mother a feminine form अस्याः would be needed."),
             ("The father's", "The father is not the subject here."),
             ("The physician's", "No physician is named.")],
            "अस्य (m. gen. sg.) = its, the embryo's.",
            "अस्य = of it (the embryo)."),
        mcq("transfer", 5, "By the rule of चास्य, how is न + अस्ति (is not) written?",
            ("नास्ति", "अ + अ → आ, as च + अस्य → चास्य."),
            [("नस्ति", "The two vowels join into long आ, not short अ."),
             ("नयस्ति", "No य् is put in between."),
             ("नोस्ति", "अ + अ does not give ओ.")],
            "न + अस्ति = नास्ति, like च + अस्य = चास्य.",
            "अ + अ → आ.",
            teaches="अ before अ joins into long आ: च + अस्य → चास्य."),
    ],
}

# ---------------------------------------------------------------- unit 32
AUTHORED["32"] = {
    "title": "ततश्च तत्प्रभृति स्पंदते",
    "question": "By unit 32, what does the embryo do from then on?",
    "rule": "And from then on it moves (throbs, स्पन्दते) and has desire (अभिलाष) for the five objects of the senses.",
    "limits": ("The subject (the embryo) is understood. स्पन्दते may mean moves or throbs. The printed पंचेंद्वियार्थेषु is "
               "read as पञ्चेन्द्रियार्थेषु (a likely correction of a letter scramble); no question rests on that word. "
               "Prose, not a verse."),
    "explain_hi": ("इकाई 31 के बाद: ‘और तब से वह हिलता (या स्पन्दित होता) है और पाँचों इन्द्रियों के विषयों की अभिलाषा करता है।’ "
                   "कर्ता गर्भ है, जो लिखा नहीं गया। "
                   "‘अभिलाषं करोति’ का शब्दार्थ है ‘इच्छा करता है’। "
                   "छपा ‘पंचेंद्वियार्थेषु’ अक्षरों की उलट-पलट लगता है; डेटा इसे ‘पञ्चेन्द्रियार्थेषु’ पढ़ता है (सम्भावित सुधार)। "
                   "‘स्पंदतेऽभिलाषं’ में स्पन्दते + अभिलाषम् है: ए के बाद अ लुप्त होकर ऽ बनता है।"),
    "hook": "चेतना के बाद: हलचल और इन्द्रिय-विषयों की चाह।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 32, from then on what does the embryo do besides having desire?",
            ("It moves, or throbs (स्पन्दते)", "स्पन्दते: moves, throbs."),
            [("It sleeps", "Sleep is not named in unit 32."),
             ("It cries aloud", "No crying is named."),
             ("It takes food by mouth", "No food is named.")],
            "Movement and desire are the two things named.",
            "स्पन्दते + अभिलाषं करोति."),
        order(1, "Put these words of unit 32 in the line's order.",
              ["ततश्च", "तत्प्रभृति", "स्पन्दते", "अभिलाषम्", "करोति"],
              "And then, from then on, moves, desire, (for the sense objects) makes.",
              "ततश्च → तत्प्रभृति → स्पन्दते → अभिलाषम् → करोति."),
        match(2, "Match each word of unit 32 to its meaning.",
              [["तत्प्रभृति", "from then on"], ["स्पन्दते", "moves, throbs"], ["अभिलाष", "desire"],
               ["करोति", "makes, has"]],
              "Four words carry the sure part of the line.",
              "तत्प्रभृति, स्पन्दते, अभिलाष, करोति.", role="extend",
              teaches="अभिलाषं करोति = literally makes desire, i.e. has desire; करोति with a noun of feeling means to have it."),
        mcq("discriminate", 3, "Which split of ततश्च is right?",
            ("ततः + च", "A visarga before च becomes श्."),
            [("तत् + च", "A final त् would give तच्च."),
             ("ततम् + च", "A final म् would give ततं च."),
             ("तत + श्च", "श्च is not a word; the particle is च.")],
            "ततः (then) + च (and).",
            "Visarga + च → श्च."),
        mcq("apply", 4, "Which split of स्पंदतेऽभिलाषं is right?",
            ("स्पन्दते + अभिलाषम्", "ए before अ stays; the अ is dropped and shown by ऽ."),
            [("स्पन्दतः + अभिलाषम्", "A visarga would give स्पन्दतोऽभिलाषम्."),
             ("स्पन्दति + अभिलाषम्", "इ + अ would give स्पन्दत्यभिलाषम्."),
             ("स्पन्दते + भिलाषम्", "भिलाष is not a word; the word is अभिलाष.")],
            "स्पन्दते (moves) + अभिलाषम् (desire).",
            "ए + अ → एऽ."),
        mcq("transfer", 5, "By the rule of स्पन्दतेऽभिलाषम्, how is वने + अस्मिन् (in this forest) written?",
            ("वनेऽस्मिन्", "A final ए before अ stays and the अ is dropped (ऽ)."),
            [("वनास्मिन्", "ए does not turn into आ."),
             ("वनोऽस्मिन्", "ओऽ comes from अः, not from ए."),
             ("वनैस्मिन्", "ए + अ does not give ऐ.")],
            "वने + अस्मिन् = वनेऽस्मिन्, like स्पन्दते + अभिलाषम्.",
            "ए + अ → एऽ.",
            teaches="A final ए before अ stays, and the अ is dropped (ऽ): स्पन्दते + अभिलाषम् → स्पन्दतेऽभिलाषम्."),
    ],
}

# ---------------------------------------------------------------- unit 33
AUTHORED["33"] = {
    "title": "मातृजं ह्यस्य हृदयं",
    "question": "By unit 33, where does the embryo's heart come from, and how is it joined to the mother?",
    "rule": ("For its heart (हृदय) is born of the mother (मातृज), and is joined to the mother's heart by dhamanīs "
             "(vessels) that carry rasa."),
    "limits": ("Whose rasa (तद्रस) is meant, the mother's or the heart's, is not stated. Dhamanī is a tube-like vessel; "
               "whether artery or umbilical vessel is not said. The line does not say which way the rasa flows. "
               "हि (for) gives a reason for what was said before. Prose, not a verse."),
    "explain_hi": ("यह पंक्ति कारण बताती है (‘हि’ = क्योंकि): गर्भ का हृदय माता से उत्पन्न (मातृज) है। "
                   "वह रस ले जाने वाली धमनियों यानी नलिका-जैसी वाहिनियों द्वारा माता के हृदय से जुड़ा रहता है। "
                   "‘तद्रस’ में ‘तत्’ किसका है, माता का या हृदय का, यह स्पष्ट नहीं; और धमनी धमनी-नाड़ी है या नाल की वाहिनी, यह भी नहीं कहा गया। "
                   "रस किस दिशा में बहता है, यह भी नहीं बताया गया। "
                   "अगली इकाई (34) इसी से निष्कर्ष निकालती है।"),
    "hook": "गर्भ का हृदय माँ से बना, धमनियों से माँ के हृदय से बँधा।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 33, the embryo's heart is born of whom?",
            ("Of the mother (मातृज)", "मातृजं ह्यस्य हृदयम्: its heart is born of the mother."),
            [("Of the father", "The line says मातृज, born of the mother."),
             ("Of the five elements", "No elements are named in unit 33."),
             ("Of its own past karma", "Karma is not named in unit 33.")],
            "The heart is मातृज.",
            "हृदय = मातृज."),
        order(1, "Put these pieces of unit 33 in the line's order.",
              ["मातृजं ह्यस्य हृदयं", "तद्रसहारिणीभिः", "धमनीभिः", "मातृहृदयेन", "अभिसंबद्धं भवति"],
              "Born of the mother its heart, rasa-carrying, by dhamanīs, to the mother's heart, joined is.",
              "मातृज हृदय → रसहारिणी → धमनी → मातृहृदय → अभिसंबद्ध."),
        match(2, "Match each word of unit 33 to its meaning.",
              [["मातृज", "born of the mother"], ["हृदय", "heart"], ["धमनी", "vessel (tube-like channel)"],
               ["अभिसंबद्ध", "joined, connected"]],
              "These words carry the line's two claims.",
              "मातृज, हृदय, धमनी, अभिसंबद्ध.", role="extend",
              teaches="-ज at the end of a compound means born of: मातृ + ज = मातृज, born of the mother."),
        mcq("discriminate", 3, "By unit 33, through what is the embryo's heart joined to the mother's heart?",
            ("By rasa-carrying dhamanīs (vessels)", "रसहारिणीभिर्धमनीभिः: by dhamanīs carrying rasa."),
            [("By sinews (स्नायु)", "No sinews are named."),
             ("By the bones", "No bones are named."),
             ("By the breath (प्राण)", "No breath is named.")],
            "The joining is by dhamanīs, in the instrumental plural.",
            "धमनीभिः अभिसंबद्धम्."),
        mcq("apply", 4, "Which split of ह्यस्य is right?",
            ("हि + अस्य", "इ before अ becomes य्: हि + अस्य → ह्यस्य."),
            [("हे + अस्य", "ए + अ would give हेऽस्य."),
             ("ह्य + अस्य", "ह्य is not a word; अ + अ would give ह्यास्य."),
             ("हम् + अस्य", "हम् is not a word; a final म् would give हमस्य.")],
            "हि (for) + अस्य (its).",
            "इ + a different vowel → य् + that vowel."),
        mcq("transfer", 5, "By the rule of ह्यस्य, how is इति + आह (thus he says) written?",
            ("इत्याह", "इ before आ becomes य्, as हि + अस्य → ह्यस्य."),
            [("इतयाह", "अय् comes from ए before a vowel, not from इ."),
             ("इताह", "The इ is not dropped."),
             ("इतेह", "इ + आ does not give ए.")],
            "इति + आह = इत्याह, like हि + अस्य = ह्यस्य.",
            "इ + a different vowel → य्.",
            teaches="A final इ before a different vowel becomes य्: हि + अस्य → ह्यस्य."),
    ],
}

# ---------------------------------------------------------------- unit 34
AUTHORED["34"] = {
    "title": "तस्मात्तयोस्ताभिः श्रद्धा",
    "question": "By unit 34, what arises because of the joining described in unit 33?",
    "rule": "Therefore, in the two, through those (vessels), a longing (श्रद्धा) arises. Here श्रद्धा means longing, desire, not faith.",
    "limits": ("The sentence continues unit 33. Who the two (तयोः) are is not stated: mother and embryo, or the two hearts; "
               "ताभिः is taken as the dhamanīs of unit 33. No question asks who the two are. Prose, not a verse."),
    "explain_hi": ("‘तस्मात्’ (इसलिए) इकाई 33 से जोड़ता है: हृदय धमनियों से जुड़े हैं, इसलिए उन दोनों में उनके द्वारा श्रद्धा उत्पन्न होती है। "
                   "यहाँ श्रद्धा का अर्थ इच्छा, लालसा है, धार्मिक आस्था नहीं; आगे की इकाइयाँ इसी इच्छा (दौर्हृद) की बात करती हैं। "
                   "‘तयोः’ (उन दोनों में) माता और गर्भ हो सकते हैं या दोनों हृदय; यह लिखा नहीं, इसलिए तय नहीं किया गया। "
                   "‘ताभिः’ को इकाई 33 की धमनियाँ माना गया है। "
                   "‘तयोस्ताभिः’ में तयोः + ताभिः है: विसर्ग त से पहले स् बनता है।"),
    "hook": "धमनियाँ जोड़ती हैं, इसलिए इच्छा जागती है।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 34, what arises (संपद्यते)?",
            ("A longing (श्रद्धा)", "श्रद्धा संपद्यते: a longing arises."),
            [("A pain", "No pain is named."),
             ("A fever", "No fever is named."),
             ("Sleep", "No sleep is named.")],
            "A longing arises in the two, through the vessels.",
            "श्रद्धा संपद्यते."),
        order(1, "Put the words of unit 34 in the line's order.",
              ["तस्मात्", "तयोः", "ताभिः", "श्रद्धा", "संपद्यते"],
              "Therefore, in the two, through them, longing, arises.",
              "तस्मात् → तयोः → ताभिः → श्रद्धा → संपद्यते."),
        match(2, "Match each word of unit 34 to its meaning.",
              [["तस्मात्", "therefore"], ["ताभिः", "through them"], ["श्रद्धा", "longing, desire"],
               ["संपद्यते", "arises"]],
              "Four of the five words; who the two (तयोः) are is left open.",
              "तस्मात्, ताभिः, श्रद्धा, संपद्यते.", role="extend",
              teaches="ताभिः is feminine instrumental plural, so the card can take it up as the धमनीभिः (feminine) of unit 33."),
        mcq("discriminate", 3, "What does श्रद्धा mean in unit 34, by the card?",
            ("Longing, desire", "The note: longing, desire, not faith."),
            [("Religious faith", "The note says not faith here."),
             ("Respect for a teacher", "The card gives no such sense."),
             ("Fear", "The card gives no such sense.")],
            "श्रद्धा here = longing, leading to the daurhṛda of units 35 to 37.",
            "श्रद्धा = longing."),
        mcq("apply", 4, "Which split of तयोस्ताभिः is right?",
            ("तयोः + ताभिः", "A visarga before त becomes स्."),
            [("तयः + ताभिः", "That would give तयस्ताभिः."),
             ("तयोम् + ताभिः", "A final म् would give तयोंताभिः."),
             ("तयोः + स्ताभिः", "स्ताभिः is not a word; the word is ताभिः.")],
            "तयोः (in the two) + ताभिः (through them).",
            "Visarga + त → स्त."),
        mcq("transfer", 5, "By the rule of तयोस्ताभिः, how is रामः + तत्र (Rāma, there) written?",
            ("रामस्तत्र", "A visarga before त becomes स्."),
            [("रामो तत्र", "ओ comes only before a voiced sound; त is unvoiced."),
             ("रामश्तत्र", "श् comes only before च, छ or श."),
             ("रामत्तत्र", "A visarga does not become त्.")],
            "रामः + तत्र = रामस्तत्र, like तयोः + ताभिः = तयोस्ताभिः.",
            "Visarga + त/थ → स्.",
            teaches="A visarga before त becomes स्: तयोः + ताभिः → तयोस्ताभिः."),
    ],
}

# ---------------------------------------------------------------- unit 35
AUTHORED["35"] = {
    "title": "द्विहृदयां नारीं दौर्हदिनीत्याचक्षते",
    "question": "By unit 35, what is a two-hearted (द्विहृदया) woman called?",
    "rule": ("And so they call a woman with two hearts (द्विहृदया) daurhṛdinī, a woman with longings. "
             "द्विहृदया is a bahuvrīhi: she who has two hearts."),
    "limits": ("The print has दौर्हदिनी; दौर्हृदिनी (from daurhṛda, longing) is a possible correction of ha for hṛ, and "
               "the meaning is the same. Whose the two hearts are is not stated here. Prose, not a verse."),
    "explain_hi": ("‘तथा च’ (और इसी प्रकार): दो हृदय वाली स्त्री को दौर्हृदिनी, यानी इच्छाओं वाली, कहते हैं। "
                   "‘द्विहृदया’ बहुव्रीहि है: जिसके दो हृदय हों; यह गर्भवती स्त्री के लिए है। "
                   "दो हृदय माता और गर्भ के हैं, यह यहाँ लिखा नहीं गया। "
                   "छपा ‘दौर्हदिनी’ है; ‘दौर्हृदिनी’ सम्भावित सुधार है (हृ की जगह ह)। "
                   "‘दौर्हृदिनीत्याचक्षते’ = दौर्हृदिनी + इति + आचक्षते।"),
    "hook": "दो हृदय वाली = दौर्हृदिनी, इच्छाओं वाली।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 35, which woman is called दौर्हदिनी (read daurhṛdinī), a woman with longings?",
            ("The two-hearted (द्विहृदया) woman", "द्विहृदयां नारीं दौर्हृदिनीत्याचक्षते."),
            [("A woman in her monthly period", "No monthly period is named."),
             ("A woman who has recently given birth", "Childbirth is not named."),
             ("A woman past child-bearing age", "No age is named.")],
            "The two-hearted woman is called daurhṛdinī.",
            "द्विहृदया = दौर्हृदिनी."),
        order(1, "Put these printed pieces of unit 35 in the line's order.",
              ["तथा च", "द्विहृदयां", "नारीं", "दौर्हदिनीत्याचक्षते"],
              "And so, two-hearted, woman, daurhṛdinī thus they call.",
              "तथा च → द्विहृदयां → नारीं → दौर्हदिनीत्याचक्षते."),
        match(2, "Match each word of unit 35 to its meaning.",
              [["द्विहृदया", "two-hearted"], ["नारी", "woman"], ["इति", "thus (marks the name)"],
               ["आचक्षते", "they call"]],
              "The name is marked by इति and governed by आचक्षते.",
              "द्विहृदया, नारी, इति, आचक्षते.", role="extend",
              teaches="द्वि-हृदया is a bahuvrīhi: it names the one who has two hearts, not the hearts."),
        mcq("discriminate", 3, "By the card, does unit 35 say whose the two hearts are?",
            ("No, the line does not say", "The note: whether the hearts are the mother's and the embryo's is not stated here."),
            [("Yes: the mother's and the embryo's", "The note says this is not stated here."),
             ("Yes: the mother's and the father's", "The father is not named."),
             ("Yes: the heart and the mind", "The mind is not named.")],
            "The line calls the woman two-hearted and says no more.",
            "द्विहृदया: whose hearts, unstated."),
        mcq("apply", 4, "Which split of इत्याचक्षते is right?",
            ("इति + आचक्षते", "इ before आ becomes य्: इति + आचक्षते → इत्याचक्षते."),
            [("इति + अचक्षते", "इ + short अ would give इत्यचक्षते."),
             ("इत्या + चक्षते", "इत्या is not a word here."),
             ("इत् + याचक्षते", "Neither इत् nor याचक्षते is the word here.")],
            "इति (thus) + आचक्षते (they call).",
            "इ + आ → या."),
        mcq("transfer", 5, "By the pattern of द्विहृदया, what does the name दीर्घबाहुः (of a man) mean?",
            ("One who has long arms", "A bahuvrīhi names the owner, as द्विहृदया = she who has two hearts."),
            [("The length of an arm", "That would be बाहुदैर्घ्य, a noun of length."),
             ("One who has two arms", "दीर्घ means long, not two."),
             ("A long road for the arms", "No road is in the compound.")],
            "दीर्घ (long) + बाहु (arm) as a bahuvrīhi: one whose arms are long.",
            "Bahuvrīhi = the one who has X.",
            teaches="A bahuvrīhi compound names its owner: द्वि + हृदया = (the woman) who has two hearts."),
    ],
}

# ---------------------------------------------------------------- unit 36
AUTHORED["36"] = {
    "title": "अन्ये तु पक्षत्रयात्प्रभृति",
    "question": "By unit 36, when do others place the time of daurhṛda, and what should be given when the wish is intense?",
    "rule": ("Others give the daurhṛda time as from three fortnights (one and a half months) up to the fifth month. "
             "When her wish is intense, one should give her, as desired, even the unwholesome joined with the wholesome."),
    "limits": ("Two printed lines of prose. Whether the fifth month is included is unclear. No food is named, nor what "
               "is joined with the wholesome, nor the giver. दौर्हद is printed for daurhṛda (possible correction). "
               "The view that तु sets aside is not in this unit."),
    "explain_hi": ("‘अन्ये तु’ से दूसरे आचार्यों का मत आता है: तीन पक्ष (डेढ़ मास) से लेकर पाँचवें मास तक दौर्हृद का काल होता है। "
                   "पाँचवाँ मास शामिल है या नहीं, यह स्पष्ट नहीं। "
                   "दूसरी पंक्ति कहती है: इच्छा तीव्र हो तो उसे मनचाहा अहित भी, हित से युक्त करके, देना चाहिए। "
                   "कौन-सी वस्तु दी जाए, यह नहीं कहा गया; न देने वाले का नाम है। "
                   "‘काममहितमप्यस्यै’ = कामम् + अहितम् + अपि + अस्यै।"),
    "hook": "डेढ़ मास से पाँचवें मास तक दौर्हृद; तीव्र इच्छा हो तो अहित भी, हित के साथ।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By the others in unit 36, from when does the time of daurhṛda run?",
            ("From three fortnights", "पक्षत्रयात् प्रभृति: from three fortnights, one and a half months."),
            [("From the first day", "No first day is named."),
             ("From the third month", "Three fortnights, not three months."),
             ("From the seventh month", "The time ends at the fifth month.")],
            "The time runs from three fortnights up to the fifth month.",
            "पक्षत्रय → आ पञ्चमात् मासात्."),
        order(1, "Put these pieces of unit 36 in the lines' order.",
              ["अन्ये तु", "पक्षत्रयात्प्रभृति", "आपंचमान्मासात्", "दौर्हदकालमाहुः", "प्रार्थनायां च तीव्रायाम्",
               "हितोपसंहितं दद्यात्"],
              "Others, from three fortnights, up to the fifth month, call the daurhṛda time; when the wish is intense, "
              "(the unwholesome) joined with the wholesome one should give.",
              "अन्ये → पक्षत्रय → पञ्चम मास → दौर्हृदकाल → तीव्र प्रार्थना → हितोपसंहित दद्यात्."),
        match(2, "Match each phrase of unit 36 to its meaning.",
              [["पक्षत्रय", "three fortnights"], ["आ पञ्चमात् मासात्", "up to the fifth month"],
               ["दौर्हदकाल (= दौर्हृदकाल)", "time of longing"], ["अहित", "unwholesome"], ["हित", "wholesome"]],
              "These phrases carry the time and the advice.",
              "पक्षत्रय, आ पञ्चमात्, दौर्हृदकाल, अहित, हित.", role="extend",
              teaches="आ with the ablative means up to: आ पञ्चमात् मासात् = up to the fifth month."),
        mcq("discriminate", 3, "By unit 36, when her wish is intense, what should be given to her?",
            ("Even the unwholesome, joined with the wholesome", "काममहितमप्यस्यै हितोपसंहितं दद्यात्."),
            [("Only the wholesome, never the unwholesome", "The line allows even the unwholesome."),
             ("Nothing until after the fifth month", "No such delay is stated."),
             ("A medicine to stop the longing", "No medicine is named.")],
            "The intense wish is met, the unwholesome being joined with the wholesome.",
            "तीव्र प्रार्थना → अहितम् अपि हितोपसंहितम्."),
        mcq("apply", 4, "A woman is two months pregnant. By the others of unit 36, is she within the daurhṛda time?",
            ("Yes: two months is past three fortnights", "Two months = four fortnights, within three fortnights to the fifth month."),
            [("No: it begins only at the fifth month", "The fifth month is where it ends."),
             ("No: it ends at three fortnights", "Three fortnights is where it begins."),
             ("The unit gives no time at all", "It gives three fortnights to the fifth month.")],
            "Three fortnights is one and a half months; two months is inside the span.",
            "दौर्हृदकाल (अन्य मत) = तीन पक्ष से पाँचवें मास तक."),
        mcq("transfer", 5, "By the rule of काममहितम्, how is अहम् + अपि (I too) written?",
            ("अहमपि", "A final म् before a vowel stays म् and joins it, as कामम् + अहितम्."),
            [("अहंपि", "Anusvāra stands for म् only before a consonant."),
             ("अहोऽपि", "ओऽ comes from अः, not from अम्."),
             ("अहापि", "The म् is not dropped.")],
            "अहम् + अपि = अहमपि, like कामम् + अहितम् = काममहितम्.",
            "Final म् + vowel → म joined to the vowel.",
            teaches="A final म् before a vowel stays म् and is written joined to it: कामम् + अहितम् → काममहितम्."),
    ],
}

# ---------------------------------------------------------------- unit 37
AUTHORED["37"] = {
    "title": "दौर्हृदविमानाद्धि वायुः",
    "question": "By unit 37, why must the daurhṛda not be disregarded?",
    "rule": ("From disregard of the daurhṛda (longing), vāyu, agitated and moving inside the body, may cause "
             "destruction (probably miscarriage) or deformity of the embryo."),
    "limits": ("Vināśa (destruction of the embryo) is kept as destruction; miscarriage is its probable modern sense. "
               "कुर्यात् is optative, may cause: it is a risk, not a certainty. The printed ं before ऽ in प्रकुपितोंऽतः is "
               "likely spurious. The line names no other doṣa and no treatment. Prose, not a verse."),
    "explain_hi": ("‘हि’ (क्योंकि) इकाई 36 की सलाह का कारण देता है। "
                   "दौर्हृद की उपेक्षा से वायु कुपित होकर शरीर के भीतर घूमता है, और गर्भ का नाश (सम्भवतः गर्भपात) या विरूपता कर सकता है। "
                   "‘कुर्यात्’ विधिलिङ् है, ‘कर सकता है’: यह आशंका है, निश्चित फल नहीं। "
                   "‘विमान’ यहाँ उपेक्षा, इच्छा का अनादर है। "
                   "‘दौर्हृदविमानाद्धि’ = दौर्हृदविमानात् + हि (त् + ह → द्ध)।"),
    "hook": "इच्छा ठुकराई तो वायु भड़की: गर्भ-नाश या विरूपता।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 37, what may follow disregard of the daurhṛda?",
            ("Agitated vāyu may destroy or deform the embryo", "वायुः प्रकुपितः ... गर्भस्य विनाशं वैरूप्यं वा कुर्यात्."),
            [("Pitta may cause fever in the mother", "No pitta or fever is named."),
             ("Kapha may make the child sleepy", "No kapha is named."),
             ("No harm; the longing fades by itself", "The line names harm to the embryo.")],
            "Disregard → agitated vāyu → destruction or deformity.",
            "दौर्हृदविमान → कुपित वायु → विनाश/वैरूप्य."),
        order(1, "Put the steps of unit 37 in the line's order.",
              ["दौर्हृदविमानात्", "वायुः प्रकुपितः", "अन्तःशरीरम् अनुचरन्", "गर्भस्य विनाशं वैरूप्यं वा", "कुर्यात्"],
              "From disregard, vāyu agitated, moving inside the body, destruction or deformity of the embryo, may cause.",
              "विमान → कुपित वायु → अनुचरन् → विनाश/वैरूप्य → कुर्यात्."),
        match(2, "Match each word of unit 37 to its meaning.",
              [["विमान", "disregard, refusal"], ["प्रकुपित", "agitated"], ["अनुचरन्", "moving along"],
               ["विनाश", "destruction (probably miscarriage)"], ["वैरूप्य", "deformity"]],
              "These words carry the chain of harm.",
              "विमान, प्रकुपित, अनुचरन्, विनाश, वैरूप्य.", role="extend",
              teaches="-आत् on an a-stem is the ablative, from: दौर्हृदविमानात् = from disregard of the longing."),
        mcq("discriminate", 3, "Which of these does unit 37 NOT name?",
            ("Fever of the mother", "No fever is named in unit 37."),
            [("Agitated vāyu", "Named: वायुः प्रकुपितः."),
             ("Destruction of the embryo", "Named: गर्भस्य विनाशम्."),
             ("Deformity of the embryo", "Named: वैरूप्यम्.")],
            "The line names agitated vāyu, destruction and deformity only.",
            "विनाश वा वैरूप्य."),
        mcq("apply", 4, "Which split of विमानाद्धि is right?",
            ("विमानात् + हि", "Final त् before ह: त् → द् and ह → ध, written द्ध."),
            [("विमानः + हि", "A visarga would give विमानो हि."),
             ("विमानम् + हि", "A final म् would give विमानं हि."),
             ("विमाना + द्धि", "द्धि is not a word; the particle is हि.")],
            "विमानात् (from disregard) + हि (for).",
            "त् + ह → द्ध (as printed here)."),
        mcq("transfer", 5, "By the rule of विमानाद्धि, how is तत् + हितम् (that wholesome thing) written?",
            ("तद्धितम्", "त् before ह becomes द् and ह becomes ध, as in विमानाद्धि."),
            [("तत्हितम्", "त् does not stay unvoiced before ह."),
             ("तच्छितम्", "छ comes from श after त्, not from ह."),
             ("तन्हितम्", "त् becomes न् only before a nasal.")],
            "तत् + हितम् = तद्धितम्, like विमानात् + हि = विमानाद्धि.",
            "त् + ह → द्ध (द्ह is also allowed).",
            teaches="A final त् before ह becomes द्, and the ह is usually written ध: विमानात् + हि → विमानाद्धि."),
    ],
}

# ---------------------------------------------------------------- unit 38
AUTHORED["38"] = {
    "title": "लब्धदौर्हृदा तु वीर्यवंतं",
    "question": "By unit 38, what son does a woman whose longing is fulfilled bear?",
    "rule": ("But she whose longing has been fulfilled (लब्धदौर्हृदा) bears a vigorous (वीर्यवत्) and long-lived "
             "(चिरायुस्) son. Line 2, on a conjectural reading: in the fourth (month) the limbs show and the embryo is stable."),
    "limits": ("Prose, two printed lines. Line 1's subject is only a feminine bahuvrīhi; no noun woman is printed. In "
               "line 2 अंगप्रत्यंग and प्रव्यक्त are conjectural, and month after चतुर्थे is understood. No question rests "
               "on the line 2 reading; one multi option only says it is conjectural."),
    "explain_hi": ("पहली पंक्ति इकाई 37 का उलटा पक्ष है: जिसकी दौर्हृद-इच्छा पूरी कर दी गई हो, वह वीर्यवान् और दीर्घायु पुत्र को जन्म देती है। "
                   "‘लब्धदौर्हृदा’ बहुव्रीहि है; ‘स्त्री’ शब्द छपा नहीं। "
                   "दूसरी पंक्ति चौथे (मास) की बात शुरू करती है: अनुमानित पाठ पर अङ्ग-प्रत्यङ्ग का विभाग प्रकट होता है और गर्भ स्थिर होता है। "
                   "छपे ‘अङ्गमत्त्यंग’ और ‘प्रन्यक्तो’ के सुधार अनुमानित हैं, इसलिए उस पंक्ति पर प्रश्न नहीं। "
                   "‘चिरायुषम्’ में चिर + आयुषम् है (अ + आ → आ)।"),
    "hook": "इच्छा पूरी तो पुत्र बलवान और दीर्घायु।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 38, what son does a woman whose longing was fulfilled bear?",
            ("A vigorous, long-lived son", "वीर्यवन्तं चिरायुषं च पुत्रं प्रसूते."),
            [("A fair, learned son", "Fairness and learning are not named."),
             ("A son with a deformity", "Deformity is the risk of disregard, unit 37."),
             ("A short-lived, gentle son", "The son is long-lived.")],
            "Fulfilled longing → a vigorous and long-lived son.",
            "लब्धदौर्हृदा → वीर्यवान्, चिरायु पुत्र."),
        order(1, "Put these words of line 1 of unit 38 in the line's order.",
              ["लब्धदौर्हृदा तु", "वीर्यवंतं", "चिरायुषं च", "पुत्रं", "प्रसूते"],
              "She whose longing is fulfilled, vigorous, and long-lived, son, bears.",
              "लब्धदौर्हृदा → वीर्यवन्तम् → चिरायुषम् → पुत्रम् → प्रसूते."),
        match(2, "Match each word of line 1 of unit 38 to its meaning.",
              [["लब्ध", "obtained, fulfilled"], ["वीर्यवत्", "vigorous"], ["चिरायुस्", "long-lived"],
               ["प्रसूते", "bears, gives birth to"]],
              "These words carry the sure first line.",
              "लब्ध, वीर्यवत्, चिरायुस्, प्रसूते.", role="extend",
              teaches="लब्ध-दौर्हृदा is a bahuvrīhi: she whose longing has been obtained."),
        mcq("discriminate", 3, "Which word of unit 38 means long-lived?",
            ("चिरायुषम्", "चिर (long) + आयुषम् (life): long-lived."),
            [("वीर्यवन्तम्", "That means vigorous."),
             ("लब्धदौर्हृदा", "That means she whose longing is fulfilled."),
             ("प्रसूते", "That means bears, gives birth to.")],
            "चिरायुषम् = long-lived, said of the son.",
            "चिरायुस् = long-lived."),
        multi("apply", 4, "Which statements about unit 38 match the card?",
              [("The noun month is printed after चतुर्थे", "Month is understood, not printed."),
               ("A woman whose longing is fulfilled bears a vigorous, long-lived son", "Right: line 1."),
               ("The reading limbs and minor limbs in line 2 is conjectural", "Right: अङ्गमत्त्यंग is corrected only as a possibility."),
               ("Line 1 names the woman with the noun नारी", "No noun woman is printed; only the bahuvrīhi.")],
              [1, 2],
              "Line 1 is sure; line 2 is conjectural, and month and woman are not printed.",
              "Line 1 sure; line 2 conjectural."),
        mcq("transfer", 5, "By the rule of चिरायुषम्, how is दीर्घ + आयुः (long life) written as one compound?",
            ("दीर्घायुः", "अ + आ → आ, as चिर + आयुषम् → चिरायुषम्."),
            [("दीर्घआयुः", "Inside a compound the two vowels must join."),
             ("दीर्घयुः", "The vowels join into long आ, not short अ."),
             ("दीर्घोयुः", "अ + आ does not give ओ.")],
            "दीर्घ + आयुः = दीर्घायुः, like चिर + आयुषम् = चिरायुषम्.",
            "अ + आ → आ.",
            teaches="अ before आ joins into long आ: चिर + आयुषम् → चिरायुषम्."),
    ],
}


NOTES_HI = {
    "26": ("गद्य-पंक्ति; विश्वास निम्न। पाठ-चिह्न: (1) छपा ‘यवो’ → यतः/यतो (सम्भावित; ‘यव’ = जौ यहाँ अर्थहीन, यतो ... ततो सहसम्बन्धी जोड़ा); "
           "(2) ‘ततोऽन्यतरा’ → ततोऽन्यतराः (सम्भावित, भावाः से मेल के लिए बहुवचन)। ‘वैशेषिकं’ को नपुंसक प्रथमा ‘विशेष निर्धारण’ माना गया; "
           "समास का पूर्वपद होना भी सम्भव। छपा ‘वैशेषिकंलिंगसंकरे’ जुड़ा हुआ है। कौन-से लिंग मिले हैं, नहीं कहा गया। "
           "सन्धि जाँची: ततः + अन्यतरा → ततोऽन्यतरा (अः + अ → ओऽ)।"),
    "27": ("विश्वास उच्च; कोई पाठ-चिह्न नहीं। प्रचलित सूत्र ‘तद् यथा’, इकाई 28 की सूची की भूमिका। "
           "सन्धि जाँची: तत् + यथा → तद्यथा (त् → द् घोष व्यंजन से पहले)।"),
    "28": ("विश्वास मध्यम; कोई पाठ-चिह्न नहीं। पूरी सूची और अन्त का ‘स्त्रीकराभावाः’ (= स्त्रीकराः भावाः) एक वाक्य है। "
           "‘क्लैब्य’ यहाँ पुरुषत्व की कमी का स्वभाव-गुण; आधुनिक अर्थ (नपुंसकता) सम्भावित। ‘गर्भाशयबीजभावाः’ का पूर्वपद-सम्बन्ध पक्का नहीं; "
           "‘युक्ताः ... अपरे’ = ‘अन्य उचित’, पर ‘युक्त’ का अर्थ ‘जुड़े’ भी हो सकता है। "
           "सन्धि जाँची: भीरुत्वम् + अवैशारद्यम् → भीरुत्वमवैशारद्यम्; मोहः + अनवस्थानम् → मोहोऽनवस्थानम्; "
           "अधोगुरुत्वम् (अधः + गुरुत्वम्, अः → ओ घोष से पहले); भावाः + तथा → भावास्तथा; युक्ताः + च + अपरे → युक्ताश्चापरे।"),
    "29": ("विश्वास उच्च; कोई पाठ-चिह्न नहीं। ‘भावाः’ इकाई 28 से समझा जाता है; क्रिया (हैं) लुप्त। "
           "सन्धि जाँची: ततः + विपरीताः → ततो विपरीताः (अः → ओ घोष व्यंजन से पहले)।"),
    "30": ("विश्वास उच्च; कोई पाठ-चिह्न नहीं। ‘भावाः’ इकाई 28 से, क्रिया लुप्त। कौन-से भाव मिले हों, नहीं कहा गया। "
           "सन्धि जाँची: संकीर्णाः + नपुंसककराः → संकीर्णा नपुंसककराः (आः के बाद घोष व्यंजन से पहले विसर्ग लोप)।"),
    "31": ("विश्वास उच्च। पाठ-चिह्न: छपा ‘चास्यचेतना’ = च + अस्य + चेतना (केवल शब्द-अन्तर, निश्चित)। ‘अस्य’ = गर्भ का। "
           "‘तदा’ किस समय की ओर है, यह इकाई नहीं कहती। सन्धि जाँची: च + अस्य → चास्य (अ + अ → आ)।"),
    "32": ("विश्वास मध्यम। पाठ-चिह्न: छपा ‘पंचेंद्वियार्थेषु’ → पञ्चेन्द्रियार्थेषु (सम्भावित, ‘द्वि/द्रि’ अक्षरों की उलट-पलट)। "
           "कर्ता (गर्भ) लुप्त; ‘स्पन्दते’ = हिलता या स्पन्दित होता। ‘अभिलाषं करोति’ शब्दशः ‘इच्छा करता है’। "
           "सन्धि जाँची: ततः + च → ततश्च (विसर्ग → श्); स्पन्दते + अभिलाषम् → स्पन्दतेऽभिलाषम् (ए + अ → एऽ)।"),
    "33": ("विश्वास मध्यम; कोई पाठ-चिह्न नहीं। छपा लम्बा पद ‘तद्रसहारिणीभिर्धमनीभिर्मातृहृदयेनाभिसंबद्धं’ कई शब्द जोड़ता है। "
           "‘तद्रस’ में ‘तत्’ माता का है या हृदय का, स्पष्ट नहीं। धमनी = नलिका-जैसी वाहिनी; धमनी-नाड़ी या नाल-वाहिनी, नहीं कहा गया। "
           "हृदय = हृदय (मानक)। सन्धि जाँची: हि + अस्य → ह्यस्य (इ → य्); हारिणीभिः + धमनीभिः → हारिणीभिर्धमनीभिः "
           "(इ के बाद विसर्ग → र् घोष से पहले); मातृहृदयेन + अभिसंबद्धम् → मातृहृदयेनाभिसंबद्धम् (अ + अ → आ)।"),
    "34": ("विश्वास मध्यम; कोई पाठ-चिह्न नहीं। वाक्य इकाई 33 से जुड़ा (GROUPING)। ‘तयोः’ = माता और गर्भ, या दोनों हृदय: तय नहीं। "
           "‘ताभिः’ = इकाई 33 की धमनियाँ (स्वाभाविक, पर लिखा नहीं)। ‘श्रद्धा’ = इच्छा, आस्था नहीं। "
           "सन्धि जाँची: तस्मात् + तयोः → तस्मात्तयोः; तयोः + ताभिः → तयोस्ताभिः (विसर्ग → स् त से पहले)।"),
    "35": ("विश्वास मध्यम। पाठ-चिह्न: छपा ‘दौर्हदिनी’ → दौर्हृदिनी (सम्भावित, हृ की जगह ह)। ‘द्विहृदया’ = दो हृदय वाली (बहुव्रीहि), "
           "गर्भवती के लिए; दो हृदय किसके, यहाँ नहीं कहा गया। सन्धि जाँची: दौर्हृदिनी + इति → दौर्हृदिनीति (ई + इ → ई); "
           "इति + आचक्षते → इत्याचक्षते (इ + आ → या)।"),
    "36": ("विश्वास मध्यम; दो छपी पंक्तियाँ (02.02.36–37)। पाठ-चिह्न: ‘दौर्हद’ → दौर्हृद (सम्भावित); ‘तीव्रायांकाममहितमप्यस्यै’ "
           "शब्द-अन्तर निश्चित। ‘आ पञ्चमात् मासात्’ = पाँचवें मास तक; पाँचवाँ शामिल है या नहीं, स्पष्ट नहीं। तीन पक्ष = डेढ़ मास। "
           "‘हितोपसंहितम्’ = हित से युक्त; क्या युक्त किया जाए, नहीं कहा गया; कोई संज्ञा (भोजन आदि) नहीं। ‘दद्यात्’ का कर्ता लुप्त। "
           "सन्धि जाँची: प्रभृति + आ → प्रभृत्या (इ + आ → या); मासात् + दौर्हद → मासाद्दौर्हद; कामम् + अहितम् → काममहितम्; "
           "अपि + अस्यै → अप्यस्यै; हित + उपसंहितम् → हितोपसंहितम् (अ + उ → ओ)।"),
    "37": ("विश्वास उच्च। पाठ-चिह्न: ‘प्रकुपितोंऽतः’ → प्रकुपितोऽन्तः (सम्भावित, ऽ से पहले का अनुस्वार फालतू)। "
           "‘विनाश’ = गर्भ का नाश, यानी सम्भवतः गर्भपात; ‘विमान’ = उपेक्षा, अनादर। ‘कुर्यात्’ विधिलिङ्, ‘कर सकता है’। "
           "सन्धि जाँची: दौर्हृदविमानात् + हि → दौर्हृदविमानाद्धि (त् + ह → द्ध; द्ह भी वैकल्पिक); "
           "प्रकुपितः + अन्तः → प्रकुपितोऽन्तः (अः + अ → ओऽ)।"),
    "38": ("विश्वास मध्यम; दो छपी पंक्तियाँ (02.02.39–40)। पंक्ति 1: दौर्हृद-विषय जारी (GROUPING); कर्ता केवल स्त्रीलिंग बहुव्रीहि, "
           "‘स्त्री’ शब्द छपा नहीं। पंक्ति 2 के पाठ-चिह्न अनुमानित: ‘अङ्गमत्त्यंग’ → अङ्गप्रत्यङ्ग (त्य/त्त्य और प्र/म का भ्रम); "
           "‘प्रन्यक्तो’ → प्रव्यक्तो (व्य/न्य का भ्रम)। ‘चतुर्थे’ के साथ ‘मास’ छपा नहीं, क्रम से समझा जाता है। "
           "‘भवति’ दोनों खण्डों के लिए। सन्धि जाँची: चिर + आयुषम् → चिरायुषम् (अ + आ → आ); गर्भः + च → गर्भश्च; "
           "स्थिरः + भवति → स्थिरो भवति।"),
}


AIDS = {
    "26": {
        "chunks": "वैशेषिकं | लिंगसंकरे तु | यवो (= यतः?) भूयस्त्वं | ततोऽन्यतरा भावाः",
        "sandhi": "अः + अ → ओऽ: ततः + अन्यतरा → ततोऽन्यतरा।",
        "frame": "अनुमानित ढाँचा: यतः (जहाँ) अधिकता → ततः (वहाँ से) एक पक्ष के भाव। ‘यतः’ केवल सम्भावित पाठ है।",
    },
    "27": {
        "chunks": "तत् | यथा",
        "sandhi": "त् → द् घोष व्यंजन से पहले: तत् + यथा → तद्यथा।",
        "anchors": "याद-सूत्र: ‘तद्यथा’ सुनते ही समझो, अब सूची आएगी। (मेरी याद-पद्धति)",
    },
    "28": {
        "diagram": {"groups": [
            {"label": "स्त्रीकर भाव (क्रम से)", "items": ["क्लैब्य", "भीरुत्व", "अवैशारद्य", "मोह", "अनवस्थान",
                                                 "अधोगुरुत्व", "असंहनन", "शैथिल्य", "मार्दव",
                                                 "गर्भाशय-बीज के भाव", "अन्य उचित भाव"]}]},
        "chunks": ("क्लैब्यं भीरुत्वमवैशारद्यं | मोहोऽनवस्थानम् | अधोगुरुत्वमसंहननं | शैथिल्यं मार्दवं | "
                   "गर्भाशयबीजभावास्तथा | युक्ताश्चापरे | स्त्रीकराभावाः"),
        "sandhi": ("म् + स्वर: भीरुत्वम् + अवैशारद्यम् → भीरुत्वमवैशारद्यम् · अः + अ → ओऽ: मोहः + अनवस्थानम् → मोहोऽनवस्थानम् · "
                   "विसर्ग + च → श्च, अ + अ → आ: युक्ताः + च + अपरे → युक्ताश्चापरे।"),
        "letters": "पहले अक्षर क्रम से: क्लै-भी-अवै-मो-अन-अधो-असं-शै-मा (मेरी याद-पद्धति)।",
    },
    "29": {
        "chunks": "ततो | विपरीताः | पुंकराः",
        "sandhi": "अः → ओ घोष व्यंजन से पहले: ततः + विपरीताः → ततो विपरीताः।",
        "frame": "ततः = इनसे, यानी इकाई 28 के स्त्रीकर भावों से; उनके विपरीत भाव पुंकर।",
    },
    "30": {
        "frame": "तीन वर्ग — इकाई 28: सूची के भाव → स्त्रीकर · इकाई 29: विपरीत → पुंकर · इकाई 30: संकीर्ण (मिले-जुले) → नपुंसककर।",
        "chunks": "संकीर्णा | नपुंसककराः",
        "sandhi": "आः के बाद घोष व्यंजन से पहले विसर्ग लोप: संकीर्णाः + नपुंसककराः → संकीर्णा नपुंसककराः।",
    },
    "31": {
        "chunks": "तदा च | अस्य चेतना | प्रव्यक्ता भवति",
        "sandhi": "अ + अ → आ: च + अस्य → चास्य।",
        "chain": {"steps": ["तदा (तब)", "अस्य (गर्भ की) चेतना", "प्रव्यक्ता भवति (पूरी तरह प्रकट)"]},
    },
    "32": {
        "chunks": "ततश्च | तत्प्रभृति | स्पंदते | अभिलाषं | पंचेंद्वियार्थेषु (= पञ्चेन्द्रियार्थेषु?) | करोति",
        "sandhi": "विसर्ग + च → श्च: ततः + च → ततश्च · ए + अ → एऽ: स्पन्दते + अभिलाषम् → स्पन्दतेऽभिलाषम्।",
        "pegs": "मेरा बनाया चित्र: गर्भ में एक नन्हा दीपक जलता है (चेतना), फिर लौ हिलने लगती है (स्पन्दन) और पाँच खिड़कियों की ओर झुकती है (पाँच इन्द्रिय-विषय)। (केवल याद के लिए)",
    },
    "33": {
        "diagram": {"groups": [
            {"label": "गर्भ का हृदय", "items": ["मातृज (माता से उत्पन्न)"]},
            {"label": "किससे जुड़ा", "items": ["रस-वाहिनी धमनियों द्वारा", "माता के हृदय से"]}]},
        "chunks": "मातृजं ह्यस्य हृदयं | तद्रसहारिणीभिः | धमनीभिः | मातृहृदयेन | अभिसंबद्धं भवति",
        "sandhi": ("इ + अ → य: हि + अस्य → ह्यस्य · इ के बाद विसर्ग → र् घोष से पहले: हारिणीभिः + धमनीभिः → हारिणीभिर्धमनीभिः · "
                   "अ + अ → आ: मातृहृदयेन + अभिसंबद्धम् → मातृहृदयेनाभिसंबद्धम्।"),
        "anchors": "याद-सूत्र: ‘मातृज’ = माँ से जन्मा; और धमनियों से माँ के हृदय से जुड़ा। (मेरी याद-पद्धति)",
    },
    "34": {
        "chain": {"steps": ["इकाई 33: हृदय धमनियों से जुड़े", "तस्मात् (इसलिए)", "तयोः (उन दोनों में)", "ताभिः (उनके द्वारा, सम्भवतः धमनियाँ)",
                            "श्रद्धा (इच्छा) उत्पन्न"]},
        "chunks": "तस्मात् | तयोः | ताभिः | श्रद्धा | संपद्यते",
        "sandhi": "विसर्ग → स् त से पहले: तयोः + ताभिः → तयोस्ताभिः · त् + त → त्त: तस्मात् + तयोः → तस्मात्तयोः।",
    },
    "35": {
        "chunks": "तथा च | द्विहृदयां नारीं | दौर्हदिनी (= दौर्हृदिनी?) | इति | आचक्षते",
        "sandhi": "ई + इ → ई: दौर्हृदिनी + इति → दौर्हृदिनीति · इ + आ → या: इति + आचक्षते → इत्याचक्षते।",
        "frame": "बहुव्रीहि: द्वि (दो) + हृदय → द्विहृदया = जिसके दो हृदय हों (स्त्री)। नाम-वाक्य: द्वितीया में X (द्विहृदयां नारीं) ... Y इति आचक्षते = X को Y कहते हैं।",
    },
    "36": {
        "chain": {"steps": ["अन्ये तु (दूसरे कहते हैं)", "तीन पक्ष (डेढ़ मास) से", "पाँचवें मास तक: दौर्हृद-काल",
                            "इच्छा तीव्र हो तो", "अहित भी, हित से युक्त करके, दें"]},
        "chunks": "अन्ये तु | पक्षत्रयात्प्रभृति | आपंचमान्मासात् | दौर्हदकालमाहुः ‖ प्रार्थनायां च तीव्रायां | काममहितमप्यस्यै | हितोपसंहितं दद्यात्",
        "sandhi": ("म् + स्वर: कामम् + अहितम् → काममहितम् · इ + अ → य: अपि + अस्यै → अप्यस्यै · "
                   "अ + उ → ओ: हित + उपसंहितम् → हितोपसंहितम्।"),
        "anchors": "याद-सूत्र: तीन पक्ष = डेढ़ मास; ‘पक्षत्रय’ से ‘पञ्चम’ तक (प से प तक)। (मेरी याद-पद्धति)",
    },
    "37": {
        "chain": {"steps": ["दौर्हृद की उपेक्षा", "वायु कुपित", "शरीर के भीतर घूमता", "गर्भ का विनाश या विरूपता (कर सकता है)"]},
        "chunks": "दौर्हृदविमानाद्धि | वायुः प्रकुपितः | अन्तःशरीरमनुचरन् | गर्भस्य विनाशं वैरूप्यं वा | कुर्यात्",
        "sandhi": ("त् + ह → द्ध: विमानात् + हि → विमानाद्धि · अः + अ → ओऽ: प्रकुपितः + अन्तः → प्रकुपितोऽन्तः · "
                   "म् + स्वर: अन्तःशरीरम् + अनुचरन् → अन्तःशरीरमनुचरन्।"),
        "story": "कथा-रूप (पंक्ति का ही क्रम): इच्छा ठुकराई गई → भीतर वायु भड़की → शरीर में घूमी → गर्भ पर संकट।",
    },
    "38": {
        "chain": {"steps": ["लब्धदौर्हृदा (जिसकी इच्छा पूरी हुई)", "प्रसूते (जन्म देती है)", "वीर्यवान् और चिरायु पुत्र"]},
        "chunks": "लब्धदौर्हृदा तु | वीर्यवंतं चिरायुषं च | पुत्रं प्रसूते ‖ चतुर्थे | अङ्गमत्त्यंगविभागः (?) प्रन्यक्तो (?) | गर्भश्च स्थिरो भवति",
        "sandhi": "अ + आ → आ: चिर + आयुषम् → चिरायुषम् · विसर्ग + च → श्च: गर्भः + च → गर्भश्च · अः → ओ घोष से पहले: स्थिरः + भवति → स्थिरो भवति।",
        "frame": "बहुव्रीहि: लब्ध (प्राप्त) + दौर्हृद → लब्धदौर्हृदा = जिसकी इच्छा पूरी हुई (स्त्री)।",
    },
}


IMAGE_SPECS = {
    ("28", "diagram"): {
        "file": "sh2-strikara-bhava-28.svg",
        "alt": ("Mind map of unit 28: the eleven woman-making states, numbered 1 to 11 in the line's order: klaibya, timidity, lack of "
                "confidence, bewilderment, unsteadiness, heaviness below, lack of compactness, laxity, softness, the "
                "states of womb and seed, and other fitting ones."),
        "type": "mermaid",
        "code": ("mindmap\n"
                 "  स्त्रीकर भाव\n"
                 "    १ क्लैब्य\n"
                 "    २ भीरुत्व\n"
                 "    ३ अवैशारद्य\n"
                 "    ४ मोह\n"
                 "    ५ अनवस्थान\n"
                 "    ६ अधोगुरुत्व\n"
                 "    ७ असंहनन\n"
                 "    ८ शैथिल्य\n"
                 "    ९ मार्दव\n"
                 "    १० गर्भाशय-बीज भाव\n"
                 "    ११ अन्य उचित भाव\n"),
    },
    ("30", "frame"): {
        "file": "sh2-bhava-varga-30.svg",
        "alt": ("Table of units 28 to 30: the listed states make a woman, their opposites make a man, mixed states make "
                "a neuter."),
        "type": "table",
        "title": "भावों के तीन वर्ग (इकाई २८–३०)",
        "heads": ["भाव", "क्या बनाते हैं"],
        "rows": [["सूची के भाव (२८)", "स्त्रीकर"], ["उनके विपरीत (२९)", "पुंकर"], ["मिले-जुले (३०)", "नपुंसककर"]],
    },
    ("33", "diagram"): {
        "file": "sh2-matrja-hridaya-33.svg",
        "alt": ("Diagram of unit 33: the embryo's heart, born of the mother, is joined to the mother's heart by "
                "rasa-carrying dhamanis (vessels); no direction of flow is shown."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"गर्भ का हृदय (मातृज)\"] --- B[\"रस-वाहिनी धमनियाँ\"]\n"
                 "  B --- C[\"माता का हृदय\"]\n"),
    },
    ("36", "chain"): {
        "file": "sh2-daurhrida-kala-36.svg",
        "alt": ("Flowchart of unit 36: by others, the daurhrida time runs from three fortnights up to the fifth month; "
                "when the wish is intense, even the unwholesome is given, joined with the wholesome."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"तीन पक्ष से (डेढ़ मास)\"] --> B[\"दौर्हद-काल (अन्य मत)\"]\n"
                 "  B --> C[\"पाँचवें मास तक\"]\n"
                 "  D[\"इच्छा तीव्र हो\"] --> E[\"अहित भी दें, हित से युक्त करके\"]\n"),
    },
    ("37", "chain"): {
        "file": "sh2-daurhrida-vimana-37.svg",
        "alt": ("Flowchart of unit 37: disregard of the daurhrida agitates vayu, which moves inside the body and may "
                "cause destruction or deformity of the embryo."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"दौर्हृद की उपेक्षा\"] --> B[\"वायु कुपित\"]\n"
                 "  B --> C[\"शरीर के भीतर घूमता, कर सकता है:\"]\n"
                 "  C --> D[\"गर्भ का विनाश\"]\n"
                 "  C -->|\"या\"| E[\"गर्भ की विरूपता\"]\n"),
    },
}
