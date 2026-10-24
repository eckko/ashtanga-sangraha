from helpers import mcq, match, order, fill, multi, accepts


AUTHORED = {}

# ---------------------------------------------------------------- unit 1
AUTHORED["1"] = {
    "title": "अथातो गर्भव्यापदं शारीरं व्याख्यास्यामः",
    "question": "By unit 1, what does this chapter set out to explain?",
    "rule": ("Opening formula: now, therefore (अथ अतः), we shall explain (व्याख्यास्यामः, future) garbhavyāpad, the mishaps "
             "of the garbha (embryo, pregnancy), the śārīra (what relates to the body)."),
    "limits": ("A prose line. That शारीरम् names the Śārīrasthāna is probable only; the line itself says 'relating to the "
               "body'. Garbhavyāpad = complications of pregnancy is a probable modern equivalent. No mishap is named here."),
    "explain_hi": ("यह अध्याय की आरम्भिक गद्य-पंक्ति है: अब इसके बाद (अथातः) हम गर्भव्यापद का व्याख्यान करेंगे। "
                   "गर्भव्यापद = गर्भ की विपत्तियाँ, यानी सम्भवतः गर्भावस्था की जटिलताएँ। "
                   "‘शारीरम्’ का शब्दार्थ है ‘शरीर सम्बन्धी’; यह शारीरस्थान का नाम हो सकता है, पर पंक्ति यह स्पष्ट नहीं कहती। "
                   "‘व्याख्यास्यामः’ भविष्यत् काल, उत्तम पुरुष बहुवचन है: हम व्याख्या करेंगे।"),
    "hook": "अथातो: अब गर्भ की विपत्तियों की बात।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 1, what does this chapter set out to explain?",
            ("The mishaps of pregnancy", "गर्भव्यापदम्: the mishaps (vyāpad) of the garbha."),
            [("The bones and the joints of the body", "Bones and joints are not the topic named in unit 1."),
             ("The signs of death", "Signs of death are not the topic named in unit 1."),
             ("The six seasons", "No season is named; the topic is garbhavyāpad.")],
            "The chapter promises to explain garbhavyāpad, the mishaps of pregnancy.",
            "गर्भव्यापदं व्याख्यास्यामः = we shall explain the mishaps of the garbha."),
        order(1, "Put the words of unit 1 in the line's order.",
              ["अथ", "अतः", "गर्भव्यापदम्", "शारीरम्", "व्याख्यास्यामः"],
              "Now, therefore, the mishaps of the garbha, relating to the body, we shall explain.",
              "अथ → अतः → गर्भव्यापदम् → शारीरम् → व्याख्यास्यामः."),
        match(2, "Match each word of unit 1 to its meaning.",
              [["अथ", "now"], ["अतः", "therefore"], ["गर्भ", "embryo, pregnancy"], ["व्यापद्", "mishap, disorder"],
               ["व्याख्यास्यामः", "we shall explain"]],
              "अथ अतः opens the chapter; गर्भ + व्यापद् = mishap of the garbha.",
              "अथ, अतः, गर्भ, व्यापद्, व्याख्यास्यामः.", role="extend",
              teaches="व्यापद् = mishap, disorder: गर्भव्यापद् = mishap of the garbha."),
        mcq("discriminate", 3, "Which split of अथातो is right?",
            ("अथ + अतः", "अ + अ → आ, and अः before the voiced ग becomes ओ."),
            [("अथा + तः", "तः is not a word; the word is अतः (therefore)."),
             ("अथः + अतः", "अथ has no visarga; it is an indeclinable."),
             ("अथ + आतः", "आतः is not the word; the word is अतः.")],
            "अथ (now) + अतः (therefore) = अथातः; before गर्भ the visarga gives ओ: अथातो.",
            "अ + अ → आ; अः + voiced consonant → ओ."),
        mcq("apply", 4, "What does the verb व्याख्यास्यामः of unit 1 express?",
            ("We shall explain (future)", "The data labels it 1st person plural future."),
            [("We explained (past)", "-स्यामः is a future ending, not a past one."),
             ("He will explain (3rd sg.)", "-मः marks the 1st person plural: we."),
             ("You shall explain (2nd pl.)", "-मः marks the 1st person plural, not you.")],
            "व्याख्यास्यामः = we shall explain: future, 1st person plural.",
            "-स्यामः = future, 1st person plural."),
        mcq("transfer", 5, "By the rule of अथ + अतः, how is न + अस्ति (is not) written when joined?",
            ("नास्ति", "अ + अ → आ, as अथ + अतः → अथातः."),
            [("नेस्ति", "ए comes from अ + इ, not from अ + अ."),
             ("नोस्ति", "ओ comes from अ + उ, not from अ + अ."),
             ("नऽस्ति", "The avagraha marks an अ dropped after ए or ओ, not after अ.")],
            "न + अस्ति = नास्ति, like अथ + अतः = अथातः.",
            "अ + अ → आ.",
            teaches="A short अ followed by a short अ joins as long आ: अथ + अतः → अथातः."),
    ],
}

# ---------------------------------------------------------------- unit 2
AUTHORED["2"] = {
    "title": "स्त्री चेदापन्नगर्भा परिहार्याण्यसेवेत",
    "question": "By unit 2, what situation opens the chapter's first case?",
    "rule": ("If (चेत्) a woman who is pregnant (आपन्नगर्भा, 'one whose garbha has come about') should indulge in the "
             "things to be avoided (परिहार्याणि): a conditional clause; the main clause comes in later units."),
    "limits": ("Prose, a conditional clause only. The things to be avoided are not named here. The verb is read आसेवेत on a "
               "correction (print has short अ): no question on the verb's form or sandhi."),
    "explain_hi": ("यह गद्य-पंक्ति एक शर्त कहती है: यदि गर्भवती स्त्री परिहार्य, यानी त्यागने योग्य, का सेवन करे। "
                   "‘आपन्नगर्भा’ बहुव्रीहि है: जिसे गर्भ प्राप्त हुआ है, यानी गर्भवती। "
                   "कौन-सी चीज़ें त्यागने योग्य हैं, यह यहाँ नहीं कहा गया; ‘परिहार्याणि’ नपुंसक बहुवचन है और संज्ञा नहीं दी गई। "
                   "मुख्य वाक्य आगे की इकाइयों में आता है। "
                   "क्रिया ‘आसेवेत’ सुधारे पाठ पर पढ़ी गई है (छपा रूप ह्रस्व अ वाला है)।"),
    "hook": "चेत्: यदि गर्भवती त्यागने योग्य का सेवन करे...",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 2, what does the pregnant woman do that sets up the case?",
            ("She indulges in things to be avoided", "परिहार्याणि (आ)सेवेत: she indulges in the avoidable."),
            [("She keeps every rule of her pregnancy", "The case is the opposite: she indulges in the things to be avoided."),
             ("She has already given birth to the child", "आपन्नगर्भा: she is pregnant, not delivered."),
             ("She takes a medicine to help conception", "She is already pregnant (आपन्नगर्भा); no medicine is named.")],
            "The case opens: if she indulges in things to be avoided.",
            "स्त्री चेदापन्नगर्भा परिहार्याणि आसेवेत."),
        order(1, "Put the words of unit 2 in the line's order.",
              ["स्त्री", "चेत्", "आपन्नगर्भा", "परिहार्याणि", "(आ)सेवेत"],
              "A woman, if, pregnant, things to be avoided, should indulge in.",
              "स्त्री → चेत् → आपन्नगर्भा → परिहार्याणि → (आ)सेवेत."),
        match(2, "Match each word of unit 2 to its meaning.",
              [["स्त्री", "woman"], ["चेत्", "if"], ["आपन्नगर्भा", "pregnant"], ["परिहार्य", "to be avoided"]],
              "If a pregnant woman indulges in the things to be avoided.",
              "स्त्री, चेत्, आपन्नगर्भा, परिहार्य.", role="extend",
              teaches="आपन्नगर्भा is a bahuvrīhi: आपन्न (come about) + गर्भ = she whose garbha has come about."),
        mcq("discriminate", 3, "Which split of चेदापन्न is right?",
            ("चेत् + आपन्न", "त् before a vowel becomes द्: चेत् + आपन्न → चेदापन्न."),
            [("चेद + आपन्न", "चेद is not a word; the particle is चेत् (if)."),
             ("चेत् + अपन्न", "अपन्न is not the word, and a short अ would give चेदपन्न."),
             ("चे + दापन्न", "चे and दापन्न are not words; the words are चेत्, आपन्न.")],
            "चेत् (if) + आपन्न (come about): त् + vowel → द्.",
            "त् + vowel → द्."),
        multi("apply", 4, "Which statements fit unit 2?",
              [("It lists the things to be avoided", "The note: the avoidable things are not named here."),
               ("It is a conditional, an if-clause", "Right: चेत् makes it a condition."),
               ("It gives the treatment in this line", "The treatment comes in later units."),
               ("आपन्नगर्भा means a pregnant woman", "Right: one whose garbha has come about.")],
              [1, 3],
              "An if-clause about a pregnant woman; the avoidables are not named.",
              "स्त्री चेदापन्नगर्भा ... आसेवेत."),
        mcq("transfer", 5, "By the pattern of आपन्नगर्भा (she whose garbha has come about), what does जितक्रोधः mean?",
            ("One whose anger has been conquered", "Bahuvrīhi: जित (conquered) + क्रोध, the person who has it."),
            [("Anger that conquers the others", "जित is conquered, not conquering."),
             ("One who conquers by his anger", "That would be an instrumental sense, not this compound."),
             ("One who makes the others angry", "Nothing in जित means making angry.")],
            "जितक्रोधः = he whose anger is conquered, as आपन्नगर्भा = she whose garbha has come about.",
            "Bahuvrīhi: participle + noun = one who has that.",
            teaches="A bahuvrīhi names the person who has the thing: आपन्न + गर्भा = she whose garbha has come about."),
    ],
}

# ---------------------------------------------------------------- unit 3
AUTHORED["3"] = {
    "title": "तत्र यस्या बस्तिपार्श्वश्रोणियोनिमुखेषु शूलं",
    "question": "By unit 3, which signs in a pregnant woman call for the treatment that follows?",
    "rule": ("In that case, she who has pain (शूल) in the basti (bladder region), the flanks (पार्श्व), the hips (श्रोणि) "
             "and the mouth of the yoni, or the sight of puṣpa (probably bleeding)."),
    "limits": ("Prose; the sentence continues in unit 4. Whether मुख goes with yoni only or with all the places is not "
               "certain: no question on it. Puṣpa (the 'flower') = bleeding in pregnancy is probable; the text says only 'sight of the flower'."),
    "explain_hi": ("यह गद्य-पंक्ति दो लक्षण बताती है: बस्ति (मूत्राशय-क्षेत्र), पार्श्व, श्रोणि और योनिमुख में शूल, या पुष्प का दिखना। "
                   "पुष्प का शब्दार्थ ‘फूल’ है; यहाँ यह सम्भवतः रक्तस्राव का मुहावरा है। "
                   "‘मुख’ केवल योनि से जुड़ता है या सब स्थानों से, यह पक्का नहीं। "
                   "वाक्य यहाँ पूरा नहीं होता: ‘ताम् ... उपाचरेत्’ इकाई ४ में है। "
                   "‘यस्याः’ (जिसके) का विसर्ग ब से पहले लुप्त हुआ है: यस्या बस्ति...।"),
    "hook": "चार स्थानों में शूल, या पुष्प दिखे: उपचार आगे।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 3, besides pain, which sign is named?",
            ("The sight of puṣpa, probably bleeding", "पुष्पदर्शनं वा: or the sight of the 'flower'."),
            [("A high fever with thirst and burning", "No fever is named in unit 3."),
             ("A swelling of the feet and of the whole face", "No swelling is named in unit 3."),
             ("A loss of all desire for any food", "No loss of appetite is named in unit 3.")],
            "Pain, or the sight of puṣpa.",
            "शूलं पुष्पदर्शनं वा स्यात्."),
        order(1, "Put the places of pain in unit 3 in the line's order.",
              ["बस्ति", "पार्श्व", "श्रोणि", "योनिमुख"],
              "Bladder region, flanks, hips, mouth of the yoni.",
              "बस्ति → पार्श्व → श्रोणि → योनिमुख."),
        match(2, "Match each word of unit 3 to its meaning.",
              [["बस्ति", "bladder region"], ["पार्श्व", "flank, side"], ["श्रोणि", "hip, pelvis"], ["शूल", "pain"],
               ["पुष्पदर्शन", "sight of puṣpa (probably bleeding)"]],
              "Four places of pain, and the second sign, puṣpadarśana.",
              "बस्ति, पार्श्व, श्रोणि, शूल, पुष्पदर्शन.", role="extend",
              teaches="पुष्प (flower) is an idiom for bleeding, probably: पुष्पदर्शन = sight of the flower."),
        mcq("discriminate", 3, "Why is यस्याः printed यस्या before बस्ति in unit 3?",
            ("After आ, the visarga drops before a voiced sound", "ब is voiced, so यस्याः → यस्या."),
            [("After आ, the visarga becomes ओ before ब", "ओ comes from a visarga after short अ, not after आ."),
             ("यस्या is a nominative form meaning who", "The data reads यस्याः, genitive: of whom."),
             ("The visarga drops before every consonant", "Before unvoiced sounds it stays or changes; it is not dropped.")],
            "यस्याः + बस्ति = यस्या बस्ति: आः before a voiced sound loses its visarga.",
            "आः + voiced sound → आ."),
        multi("apply", 4, "Which signs in unit 3 call for the treatment that follows?",
              [("Pain in the flanks", "Right: पार्श्व is one of the places of pain."),
               ("Fever with thirst", "No fever is named."),
               ("The sight of puṣpa", "Right: पुष्पदर्शनं वा."),
               ("Swelling of the feet", "No swelling is named.")],
              [0, 2],
              "Pain in the named places, or the sight of puṣpa.",
              "शूलं पुष्पदर्शनं वा."),
        mcq("transfer", 5, "By the rule of यस्या बस्ति, how is कन्याः + वदन्ति (the girls speak) written?",
            ("कन्या वदन्ति", "आः before the voiced व loses its visarga, as यस्याः + बस्ति."),
            [("कन्यो वदन्ति", "ओ comes from a visarga after short अ, not after आ."),
             ("कन्यार्वदन्ति", "र् comes after vowels other than अ and आ."),
             ("कन्याः वदन्ति", "Before a voiced sound the visarga after आ does not stay.")],
            "कन्याः + वदन्ति = कन्या वदन्ति, like यस्याः + बस्ति = यस्या बस्ति.",
            "आः + voiced sound → आ.",
            teaches="A visarga after आ is dropped before a voiced sound: यस्याः + बस्ति → यस्या बस्ति."),
    ],
}

# ---------------------------------------------------------------- unit 4
AUTHORED["4"] = {
    "title": "तां मृदुमुखशिशिरास्तरणशयनस्थाम्",
    "question": "By unit 4, how is she laid, and with what is she treated?",
    "rule": ("Her (ताम्), lying on a bed with a soft, cool spread and her head slightly lowered (ईषदवनतशिरसम्), one should "
             "treat (उपाचरेत्) with cool plasters (प्रदेह), sprinklings (परिषेक) and the like."),
    "limits": ("Main clause of the sentence begun in unit 3. मुख (surface) may be a misprint for सुख (comfortable), and the "
               "grouping of the first compound is uncertain: no question on मुख. No plaster or liquid is named here."),
    "explain_hi": ("यह इकाई ३ में शुरू हुए वाक्य का मुख्य भाग है। "
                   "उसे कोमल और शीतल बिछावन वाली शय्या पर लिटाएँ, सिर थोड़ा झुका हुआ (ईषदवनतशिरसम्) हो। "
                   "फिर शीतल प्रदेह (लेप), परिषेक (सींचना) आदि से उपचार करें। "
                   "‘मुख’ (सतह) के स्थान पर ‘सुख’ (आरामदायक) भी पाठ हो सकता है, और पहले समास का विभाजन पक्का नहीं। "
                   "कौन-से लेप या द्रव, यह आगे की इकाइयों में आता है।"),
    "hook": "कोमल-शीतल शय्या, सिर थोड़ा नीचे, शीतल लेप-परिषेक।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 4, how is her head placed?",
            ("Slightly lowered", "ईषदवनतशिरसम्: with the head slightly bent down."),
            [("Raised on pillows", "The head is lowered, not raised."),
             ("Kept upright, sitting", "She lies on a bed; she is not sitting."),
             ("Turned to one side", "No turning is named; the head is slightly lowered.")],
            "She lies with her head slightly lowered.",
            "ईषत् (slightly) + अवनत (lowered) + शिरस् (head)."),
        order(1, "Put these words of unit 4 in the line's order.",
              ["ताम्", "मृदुमुखशिशिरास्तरणशयनस्थाम्", "ईषदवनतशिरसम्", "शीतप्रदेहपरिषेकादिभिः", "उपाचरेत्"],
              "Her, on a soft cool bed, head slightly lowered, with cool plasters, sprinklings and the like, one should treat.",
              "ताम् → ...शयनस्थाम् → ईषदवनतशिरसम् → शीतप्रदेहपरिषेकादिभिः → उपाचरेत्."),
        match(2, "Match each word of unit 4 to its meaning.",
              [["शिशिर", "cool"], ["आस्तरण", "spread, bedding"], ["ईषत्", "slightly"], ["अवनत", "bent down, lowered"],
               ["प्रदेह", "plaster, paste applied"], ["परिषेक", "sprinkling, pouring"]],
              "A cool bed, the head slightly lowered, cool plasters and sprinklings.",
              "शिशिर, आस्तरण, ईषत्, अवनत, प्रदेह, परिषेक.", role="extend",
              teaches="प्रदेह = a plaster applied; परिषेक = sprinkling, pouring over."),
        mcq("discriminate", 3, "Which split of आदिभिरुपाचरेत् is right?",
            ("आदिभिः + उपाचरेत्", "After इ, a visarga before a vowel becomes र्."),
            [("आदिभिर् + पाचरेत्", "पाचरेत् is not the verb; the verb is उपाचरेत्."),
             ("आदिभि + रुपाचरेत्", "रुपाचरेत् is not a word; the र् comes from the visarga."),
             ("आदिभ्यः + उपाचरेत्", "अः + उ would not give इर्; the data reads आदिभिः.")],
            "आदिभिः (with ... and the like) + उपाचरेत् (should treat): इः + vowel → इर्.",
            "A visarga after a vowel other than अ/आ → र् before a vowel or voiced consonant."),
        mcq("apply", 4, "A pregnant woman has the pain of unit 3. By unit 4, which treatment is used?",
            ("Cool plasters and sprinklings", "शीतप्रदेहपरिषेकादिभिः: cool plasters, sprinklings and the like."),
            [("Hot pastes and warm baths", "The unit says cool (शीत), not hot."),
             ("Smoke of herbs and walking", "No smoke or walking is named in unit 4."),
             ("Massage of the whole body with warm oil", "No warm oil is named; the measures are cool.")],
            "She is treated with cool measures: plasters, sprinklings and the like.",
            "शीतप्रदेहपरिषेकादिभिः उपाचरेत्."),
        mcq("transfer", 5, "By the rule of आदिभिरुपाचरेत्, how is मुनिः + आगच्छति (the sage comes) written?",
            ("मुनिरागच्छति", "After इ, the visarga becomes र् before a vowel."),
            [("मुनियागच्छति", "य् comes from a vowel इ, not from इः."),
             ("मुनोरागच्छति", "The इ of मुनि does not change to ओ."),
             ("मुनि आगच्छति", "After इ the visarga becomes र्; it is not dropped.")],
            "मुनिः + आगच्छति = मुनिरागच्छति, like आदिभिः + उपाचरेत् = आदिभिरुपाचरेत्.",
            "इः + vowel → इर्.",
            teaches="A visarga after a vowel other than अ/आ becomes र् before a vowel: आदिभिः + उपाचरेत् → आदिभिरुपाचरेत्."),
    ],
}

# ---------------------------------------------------------------- unit 5
AUTHORED["5"] = {
    "title": "तद्यथा",
    "question": "What does तद्यथा do in unit 5?",
    "rule": ("तद्यथा (that is as follows) introduces the list of measures that comes from unit 6 onward. "
             "तत् + यथा: त् before the voiced य becomes द्."),
    "limits": ("One word in print, prose. It names no measure itself; the measures follow in the next units."),
    "explain_hi": ("‘तद्यथा’ का अर्थ है ‘वह इस प्रकार है’। "
                   "यह शब्द आगे आने वाले उपायों की सूची का आरम्भ करता है, जो इकाई ६ से शुरू होती है। "
                   "यह तत् (वह) + यथा (जैसे, यानी) है; घोष य से पहले त् का द् हुआ है। "
                   "इस इकाई में स्वयं कोई उपाय नहीं कहा गया।"),
    "hook": "तद्यथा: अब सूची आती है।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What does तद्यथा in unit 5 do?",
            ("It introduces the list that follows", "The note: it introduces the measures from unit 6 on."),
            [("It closes the long list of the whole chapter", "It opens a list; it does not close one."),
             ("It names the drug to be given now", "No drug is named in तद्यथा."),
             ("It states the dose of the remedy", "No dose is given in तद्यथा.")],
            "तद्यथा = that is as follows: a list comes next.",
            "तद्यथा introduces a list."),
        match(1, "Match each part of unit 5 to its meaning.",
              [["तत्", "that"], ["यथा", "as, namely"], ["तद्यथा", "that is as follows"]],
              "तत् + यथा = तद्यथा, that is as follows.",
              "तत् = that; यथा = as, namely."),
        fill(2, "तत् and यथा are joined as ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("तद्यथा"),
             "तत् + यथा = तद्यथा: त् becomes द् before the voiced य.",
             "A final त् becomes द् before a vowel or a voiced consonant such as य (not before nasals, ल, ज, ड): तत् + यथा → तद्यथा.",
             "तत् + यथा → तद्यथा."),
        mcq("discriminate", 3, "Why is तत् written तद् in तद्यथा?",
            ("त् becomes द् before the voiced य", "य is a voiced sound; त् takes the voiced द्."),
            [("द् marks the plural of तत्", "Number is not marked by द्; it is sandhi."),
             ("य makes the sound before it unvoiced", "The change goes the other way: त् becomes voiced द्."),
             ("द् marks the instrumental case here", "Case is not marked by द्; it is sandhi.")],
            "Before the voiced य, the unvoiced त् becomes voiced द्.",
            "त् + vowel or voiced ग, ब, य ... → द् (not before nasals, ल, ज, ड)."),
        mcq("apply", 4, "In unit 5, what kind of line is तद्यथा?",
            ("A prose line leading into a list", "The data types it prose; it introduces the measures."),
            [("A full verse (śloka) of four quarters", "It is one word of prose, not a verse."),
             ("A full instruction with its own verb", "There is no verb; it only introduces the list."),
             ("A list of drugs for her to drink", "It names no drug; the list comes after it.")],
            "A one-word prose line that opens the list of measures.",
            "तद्यथा = that is as follows."),
        mcq("transfer", 5, "By the rule of तद्यथा, how is सत् + गुणः (a good quality) written when joined?",
            ("सद्गुणः", "त् before the voiced ग becomes द्, as तत् + यथा."),
            [("सत्गुणः", "Before a voiced ग the त् does not stay unvoiced."),
             ("सग्गुणः", "त् becomes द् here; it does not copy the ग."),
             ("सन्गुणः", "न् is not taken before ग here; the result is द्.")],
            "सत् + गुणः = सद्गुणः, like तत् + यथा = तद्यथा.",
            "त् + voiced consonant (not a nasal, ल, ज or ड) → द्.",
            teaches="A final त् becomes द् before a vowel or a voiced consonant such as ग, ब, य (before nasals, ल, ज, ड it assimilates instead): तत् + यथा → तद्यथा."),
    ],
}

# ---------------------------------------------------------------- unit 6
AUTHORED["6"] = {
    "title": "सहस्रधौतेन सर्पिषाऽधोनाभेः सर्वतः प्रदिह्यात्",
    "question": "By unit 6, with what is she smeared, and where?",
    "rule": ("With ghee (सर्पिस्) washed a thousand times (सहस्रधौत), one should smear (प्रदिह्यात्) all round "
             "(सर्वतः) below the navel (अधो नाभेः)."),
    "limits": ("What the ghee is washed with is not stated, and the object (the area) is not named. The avagraha in "
               "सर्पिषाऽधो is only a mark of the print: no question on it. No amount is given."),
    "explain_hi": ("यह गद्य-पंक्ति पहला उपाय बताती है: हज़ार बार धोए हुए घी (सहस्रधौत सर्पि) से नाभि के नीचे चारों ओर लेप करें। "
                   "घी किससे धोया जाए, यह नहीं कहा गया। "
                   "‘अधोनाभेः’ में अधः (नीचे) + नाभेः (नाभि से) है; घोष न से पहले अः का ओ हुआ है। "
                   "‘सर्पिषाऽधो’ का अवग्रह छपाई का चिह्न है; आ + अ से केवल आ बनता है। "
                   "छपाई में ‘सहस्रधौतेन’ और ‘सर्पिषा’ जुड़े हुए छपे हैं।"),
    "hook": "हज़ार बार धुला घी, नाभि के नीचे चारों ओर।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 6, what is smeared below the navel?",
            ("Ghee washed a thousand times", "सहस्रधौतेन सर्पिषा: with ghee washed a thousand times."),
            [("Honey mixed with fine sugar", "Honey with sugar is licked in unit 12, not smeared here."),
             ("Cow's milk with madhuka water", "These are sprinkled in unit 8, not smeared here."),
             ("The blood of the hare and deer", "The blood is drunk in unit 14, not smeared here.")],
            "Ghee washed a thousand times is smeared below the navel.",
            "सहस्रधौतेन सर्पिषा ... प्रदिह्यात्."),
        order(1, "Put the words of unit 6 in the line's order.",
              ["सहस्रधौतेन", "सर्पिषा", "अधः", "नाभेः", "सर्वतः", "प्रदिह्यात्"],
              "With thousand-washed ghee, below the navel, all round, one should smear.",
              "सहस्रधौतेन → सर्पिषा → अधः → नाभेः → सर्वतः → प्रदिह्यात्."),
        match(2, "Match each word of unit 6 to its meaning.",
              [["सहस्र", "thousand"], ["धौत", "washed"], ["सर्पिस्", "ghee"], ["नाभि", "navel"],
               ["सर्वतः", "all round"], ["प्रदिह्यात्", "should smear"]],
              "Thousand-washed ghee is smeared all round below the navel.",
              "सहस्र, धौत, सर्पिस्, नाभि, सर्वतः, प्रदिह्यात्.", role="extend",
              teaches="सहस्रधौत = washed a thousand times; सर्पिस् = ghee."),
        mcq("discriminate", 3, "Which split of अधोनाभेः is right?",
            ("अधः + नाभेः", "अः before the voiced न becomes ओ."),
            [("अध + उनाभेः", "उनाभेः is not a word; the word is नाभेः."),
             ("अधौ + नाभेः", "अधौ is not a word; the word is अधः."),
             ("अधे + नाभेः", "अधे is not a word; the ओ comes from अः.")],
            "अधः (below) + नाभेः (the navel): अः + voiced न → ओ.",
            "अः + voiced consonant → ओ."),
        mcq("apply", 4, "By unit 6, where exactly is the ghee smeared?",
            ("All round, below the navel", "अधो नाभेः सर्वतः: all round below the navel."),
            [("Only above the navel", "अधः means below, not above."),
             ("On the head and face", "The head is not named in unit 6."),
             ("On the soles of both of the feet", "The feet are not named in unit 6.")],
            "Below the navel, on all sides.",
            "अधः = below; सर्वतः = on all sides."),
        mcq("transfer", 5, "By the rule of अधोनाभेः, how is अधः + मुखम् (face downward) written when joined?",
            ("अधोमुखम्", "अः before the voiced म becomes ओ, as अधः + नाभेः."),
            [("अधमुखम्", "The visarga after अ does not simply vanish before म."),
             ("अधर्मुखम्", "र् comes after vowels other than अ and आ."),
             ("अधामुखम्", "अः does not become आ before म.")],
            "अधः + मुखम् = अधोमुखम्, like अधः + नाभेः = अधोनाभेः.",
            "अः + voiced consonant → ओ.",
            teaches="A visarga after अ becomes ओ before a voiced consonant: अधः + नाभेः → अधोनाभेः."),
    ],
}

# ---------------------------------------------------------------- unit 7
AUTHORED["7"] = {
    "title": "मधुकसर्पिषा सुशीतेन पिचुमाप्लाव्य",
    "question": "By unit 7, what is soaked, in what, and where is it placed?",
    "rule": ("Having soaked (आप्लाव्य) a picu (a pad or wad, often of cotton) in very cool (सुशीत) madhuka-ghee "
             "(madhuka: licorice, standard), one should place (स्थापयेत्) it near the yoni."),
    "limits": ("मधुकसर्पिषा may also be read 'madhuka and ghee'; how the madhuka-ghee is made is not stated. No size of picu "
               "or time is given. Madhuka (licorice) is not madhūka (Madhuca), a different drug."),
    "explain_hi": ("बहुत ठण्डे (सुशीत) मधुक-घृत में पिचु, यानी रुई का फाहा, भिगोकर (आप्लाव्य) योनि के पास रखें। "
                   "मधुक = मुलेठी (मानक पहचान); मधूक (महुआ) अलग द्रव्य है। "
                   "‘मधुकसर्पिषा’ को ‘मधुक और घी’ भी पढ़ा जा सकता है; मधुक-घृत कैसे बनता है, यह नहीं कहा गया। "
                   "‘आप्लाव्य’ उपसर्ग (आ) वाला पूर्वकालिक रूप है, इसलिए -य, -त्वा नहीं। "
                   "‘पिचुमाप्लाव्य’ में पिचुम् + आप्लाव्य है।"),
    "hook": "ठण्डे मुलेठी-घी में फाहा भिगोओ, योनि के पास रखो।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 7, where is the soaked picu placed?",
            ("Near the yoni", "योनिसमीपे स्थापयेत्: one should place it near the yoni."),
            [("On the navel", "The navel area is smeared in unit 6; the picu goes near the yoni."),
             ("Under the head", "The head is not named in unit 7."),
             ("On the breasts", "The breasts are not named in unit 7.")],
            "The soaked pad is placed near the yoni.",
            "योनिसमीपे स्थापयेत्."),
        order(1, "Put the words of unit 7 in the line's order.",
              ["मधुकसर्पिषा", "सुशीतेन", "पिचुम्", "आप्लाव्य", "योनिसमीपे", "स्थापयेत्"],
              "In madhuka-ghee, very cool, a picu, having soaked, near the yoni, one should place.",
              "मधुकसर्पिषा → सुशीतेन → पिचुम् → आप्लाव्य → योनिसमीपे → स्थापयेत्."),
        match(2, "Match each word of unit 7 to its meaning.",
              [["मधुक", "licorice (standard)"], ["सुशीत", "very cool"], ["पिचु", "pad or wad, of cotton"],
               ["आप्लाव्य", "having soaked"], ["समीपे", "near"]],
              "A pad soaked in very cool licorice-ghee is placed near the yoni.",
              "मधुक, सुशीत, पिचु, आप्लाव्य, समीपे.", role="extend",
              teaches="मधुक = licorice (Glycyrrhiza glabra, standard); पिचु = a pad or wad."),
        mcq("discriminate", 3, "Why does आप्लाव्य end in -य and not in -त्वा?",
            ("It has the prefix आ-, so it takes -य", "With a prefix the absolutive ends in -य."),
            [("The -य marks a passive verb form", "आप्लाव्य is an absolutive: having soaked."),
             ("The -य marks the optative mood", "The optative here is स्थापयेत्, not आप्लाव्य."),
             ("The -य marks a plural object", "पिचुम् is singular; -य is not a number ending.")],
            "आ + प्लाव्य: a prefixed verb forms its absolutive with -य.",
            "Absolutive: -त्वा without a prefix, -य with a prefix."),
        fill(4, "The pad soaked in unit 7 is called ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("पिचु", None, "पिचुम्"),
             "पिचुमाप्लाव्य = पिचुम् + आप्लाव्य: having soaked a picu.",
             "पिचु = a pad or wad, often of cotton; पिचुम् is its accusative.",
             "पिचुम् आप्लाव्य = having soaked a pad.", role="apply"),
        mcq("transfer", 5, "By the rule of आप्लाव्य, which is the absolutive (having known) of the prefixed verb वि-√ज्ञा?",
            ("विज्ञाय", "With the prefix वि-, the absolutive takes -य, as आ-प्लाव्य."),
            [("विज्ञात्वा", "-त्वा is not used when a prefix is present."),
             ("विज्ञायते", "विज्ञायते is a present passive, not an absolutive."),
             ("विज्ञास्यति", "विज्ञास्यति is a future, not an absolutive.")],
            "वि + ज्ञा → विज्ञाय, like आ + प्लु (causative) → आप्लाव्य.",
            "Prefixed verb → absolutive in -य.",
            teaches="A verb with a prefix forms its absolutive (having done) with -य, not -त्वा: आप्लाव्य = having soaked."),
    ],
}

# ---------------------------------------------------------------- unit 8
AUTHORED["8"] = {
    "title": "गव्येन पयसा मधुकम्बुना न्यग्रोधादिकषायेण वा",
    "question": "By unit 8, with which liquids is she sprinkled?",
    "rule": ("One should sprinkle (परिषेचयेत्) with cow's milk (गव्येन पयसा), with madhuka-water, or with a decoction "
             "(कषाय) of nyagrodha (banyan, standard) and the others."),
    "limits": ("Printed मधुकम्बुना has short अ (मधुकाम्बुना expected): no question on its sandhi. The members of the nyagrodha "
               "group are not listed here. The object (her or the area) is not named. No amount is given."),
    "explain_hi": ("तीन विकल्पों से परिषेक (सींचना) करें: गाय के दूध से, मधुक (मुलेठी) के जल से, या न्यग्रोध (बरगद) आदि के काढ़े से। "
                   "‘न्यग्रोधादि’ = न्यग्रोध और अन्य; समूह के बाकी वृक्ष यहाँ नहीं गिनाए गए। "
                   "किसे सींचें, यह स्पष्ट नहीं लिखा। "
                   "‘गव्येन पयसा’ में विशेषण और संज्ञा दोनों तृतीया एकवचन हैं: गाय के दूध से। "
                   "छपा ‘मधुकम्बुना’ ह्रस्व अ वाला है; मधुक + अम्बुना से मधुकाम्बुना अपेक्षित है।"),
    "hook": "दूध, मुलेठी-जल, या बरगद-काढ़ा: सींचो।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 8, what is done with cow's milk, madhuka-water or the nyagrodha decoction?",
            ("They are sprinkled over her", "परिषेचयेत्: one should sprinkle."),
            [("They are smeared below the navel", "Smearing below the navel is ghee, in unit 6."),
             ("They are licked with honey", "Licking with honey is unit 12."),
             ("They are placed in the yoni", "Oils are placed in the yoni in unit 9.")],
            "These three liquids are for sprinkling.",
            "... वा परिषेचयेत्."),
        order(1, "Put the liquids of unit 8 in the line's order.",
              ["गव्येन पयसा", "मधुकम्बुना", "न्यग्रोधादिकषायेण", "परिषेचयेत्"],
              "With cow's milk, with madhuka-water, or with the decoction of nyagrodha and the others, one should sprinkle.",
              "गव्येन पयसा → मधुकम्बुना → न्यग्रोधादिकषायेण → परिषेचयेत्."),
        match(2, "Match each word of unit 8 to its meaning.",
              [["गव्य", "from the cow"], ["पयस्", "milk"], ["अम्बु", "water"], ["न्यग्रोध", "banyan (standard)"],
               ["कषाय", "decoction"]],
              "Cow's milk, madhuka-water, decoction of the nyagrodha group.",
              "गव्य, पयस्, अम्बु, न्यग्रोध, कषाय.", role="extend",
              teaches="कषाय in a sprinkling liquid = decoction; न्यग्रोध = banyan (Ficus benghalensis, standard)."),
        mcq("discriminate", 3, "What does -आदि add in न्यग्रोधादिकषायेण?",
            ("And the others: a group from nyagrodha", "न्यग्रोध + आदि = nyagrodha and so on."),
            [("Only the nyagrodha tree, alone", "-आदि adds others; it does not limit."),
             ("The bark of the nyagrodha tree", "Bark is त्वक्; it is not named here."),
             ("A second, later decoction of it", "-आदि does not mean a second decoction.")],
            "न्यग्रोधादि = nyagrodha and the others of its group.",
            "-आदि = and so on, beginning with."),
        multi("apply", 4, "Which liquids does unit 8 name for sprinkling?",
              [("Cow's milk", "Right: गव्येन पयसा."),
               ("Hot water", "No hot water; the measures are cool."),
               ("Madhuka-water", "Right: मधुकम्बुना."),
               ("A decoction of nyagrodha and the others", "Right: न्यग्रोधादिकषायेण.")],
              [0, 2, 3],
              "Cow's milk, madhuka-water, or the nyagrodha-group decoction.",
              "गव्येन पयसा मधुकम्बुना न्यग्रोधादिकषायेण वा."),
        mcq("transfer", 5, "By the pattern of गव्येन पयसा, which phrase means with cool water (जल, neuter)?",
            ("शीतेन जलेन", "Adjective and noun both instrumental singular, as गव्येन पयसा."),
            [("शीतं जलेन", "शीतं is not instrumental; it must agree with जलेन."),
             ("शीतेन जलम्", "जलम् is not instrumental; both words take -एन."),
             ("शीतस्य जलेन", "शीतस्य is genitive; it must agree in case.")],
            "शीतेन जलेन = with cool water, like गव्येन पयसा = with cow's milk.",
            "An adjective agrees with its noun in case, number and gender.",
            teaches="An adjective takes the same case as its noun: गव्येन (inst.) पयसा (inst.) = with cow's milk."),
    ],
}

# ---------------------------------------------------------------- unit 9
AUTHORED["9"] = {
    "title": "परिपीततत्वरसानि च तैलानियोनौ निधापयेत्",
    "question": "By unit 9, what is placed in the yoni, and what is the other option?",
    "rule": ("One should have oils (तैलानि) placed in the yoni (योनौ निधापयेत्); or a picu (wad) of milk-and-ghee "
             "(क्षीरसर्पिस्) cooked (सिद्ध) with its śṛṅga."),
    "limits": ("Low confidence. परिपीततत्वरसानि is damaged: only परिपीत (absorbed) is clear; the reading तत्-त्वग्-रस is a "
               "conjecture. शृङ्ग (horn) = shoot is probable, and what तत् points to is not sure: no question on these."),
    "explain_hi": ("योनि में तेल रखवाएँ (निधापयेत्); तेलों का विशेषण ‘परिपीततत्वरसानि’ क्षतिग्रस्त है, केवल ‘परिपीत’ (भली भाँति सोखा) स्पष्ट है। "
                   "‘तत्-त्वक्-रस’ (उनकी छाल का रस) केवल अनुमानित पाठ है। "
                   "दूसरा विकल्प: उसके शृङ्ग के साथ पकाए (सिद्ध) दूध-घी का पिचु। "
                   "शृङ्ग का अर्थ ‘सींग’ है; यहाँ ‘कोंपल’ सम्भावित है, निश्चित नहीं, और ‘तत्’ किसे दिखाता है, यह भी पक्का नहीं। "
                   "दूसरी पंक्ति में क्रिया इकाई ७ से समझी जाती है।"),
    "hook": "योनि में तेल; या दूध-घी का फाहा।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 9, what is to be placed in the yoni?",
            ("Oils (तैलानि)", "तैलानि योनौ निधापयेत्: one should have oils placed in the yoni."),
            [("Hare's blood", "The blood is drunk in unit 14."),
             ("Rice-water", "Rice-water is not named in unit 9."),
             ("Red ochre (गैरिक)", "Red ochre is in the powder of unit 12.")],
            "Oils are placed in the yoni.",
            "तैलानि योनौ निधापयेत्."),
        order(1, "Put these clear words of unit 9 in the line's order.",
              ["तैलानि", "योनौ", "निधापयेत्", "क्षीरसर्पिषः", "पिचुम्"],
              "Oils, in the yoni, one should have placed; or of milk-and-ghee, a picu.",
              "तैलानि → योनौ → निधापयेत् → क्षीरसर्पिषः → पिचुम्."),
        match(2, "Match each clear word of unit 9 to its meaning.",
              [["तैल", "oil"], ["योनौ", "in the yoni"], ["निधापयेत्", "should have placed"],
               ["क्षीरसर्पिस्", "milk and ghee"], ["सिद्ध", "cooked"]],
              "Oils placed in the yoni; or a pad of cooked milk-and-ghee.",
              "तैल, योनौ, निधापयेत्, क्षीरसर्पिस्, सिद्ध.", role="extend",
              teaches="योनौ is locative singular: in the yoni; सिद्ध = cooked, prepared."),
        mcq("discriminate", 3, "Which split of तच्छृङ्ग is right?",
            ("तत् + शृङ्ग", "त् + श → च्छ: तत् + शृङ्ग → तच्छृङ्ग."),
            [("तच् + छृङ्ग", "छृङ्ग is not a word; the word is शृङ्ग."),
             ("तद् + शृङ्ग", "There is no द् here; the word is तत्, and श is unvoiced."),
             ("तः + छृङ्ग", "तः is not a word, and छृङ्ग is not one either.")],
            "तत् (that, its) + शृङ्ग: त् + श → च्छ.",
            "त् + श → च्छ."),
        multi("apply", 4, "Which statements fit unit 9?",
              [("The oils are placed in the yoni", "Right: तैलानि योनौ निधापयेत्."),
               ("The line itself names the tree of the śṛṅga", "Only तत् (its) is printed; what it points to is not sure."),
               ("The line names the trees for the oils", "No trees are named in unit 9."),
               ("Only परिपीत of the first compound is clear", "Right: the rest is damaged.")],
              [0, 3],
              "Oils in the yoni are clear; the compound and the śṛṅga are uncertain.",
              "तैलानि योनौ निधापयेत्."),
        mcq("transfer", 5, "By the rule of तच्छृङ्ग, how is तत् + शरीरम् (that body) written when joined?",
            ("तच्छरीरम्", "त् + श → च्छ, as तत् + शृङ्ग → तच्छृङ्ग."),
            [("तद्शरीरम्", "त् does not become द् before the unvoiced श."),
             ("तश्शरीरम्", "त् does not become श् here."),
             ("तज्शरीरम्", "ज् is voiced; it does not stand before the unvoiced श.")],
            "तत् + शरीरम् = तच्छरीरम्, like तत् + शृङ्ग = तच्छृङ्ग.",
            "त् + श → च्छ.",
            teaches="A final त् with a following श gives च्छ: तत् + शृङ्ग → तच्छृङ्ग."),
    ],
}

# ---------------------------------------------------------------- unit 10
AUTHORED["10"] = {
    "title": "अतिस्रवति तु रक्ते",
    "question": "By unit 10, what is done when the blood flows too much?",
    "rule": ("But when the blood flows too much (अतिस्रवति रक्ते, locative absolute), one should make her take "
             "(प्राशयेत्) an akṣa measure (अक्षमात्रम्) from that very (ततः एव) preparation."),
    "limits": ("ततः एव points back to the milk-and-ghee of unit 9 (the data's reading). The data notes akṣa = picu = karṣa, "
               "about 10 g in the standard reckoning; the line gives no number of doses or days."),
    "explain_hi": ("अब नया प्रसंग: रक्त बहुत बहे तो (अतिस्रवति रक्ते) उसी (ततः एव) में से अक्ष की मात्रा खिलाएँ (प्राशयेत्)। "
                   "‘ततः एव’ इकाई ९ के दूध-घी की ओर संकेत करता है। "
                   "अक्ष एक तौल है; डेटा के अनुसार अक्ष, पिचु और कर्ष पर्याय हैं, मानक गणना में लगभग १० ग्राम। "
                   "कितनी बार या कितने दिन, यह नहीं कहा गया। "
                   "‘तत एव’ में ततः का विसर्ग ए से पहले लुप्त हुआ है।"),
    "hook": "रक्त अधिक बहे: उसी में से अक्ष-भर खिलाओ।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 10, in which condition is an akṣa measure given?",
            ("When the blood flows too much", "अतिस्रवति तु रक्ते: when the blood flows too much."),
            [("When no blood has been seen", "That case begins in unit 23."),
             ("When the fetus has turned down", "No turning is named in unit 10."),
             ("When the pain has gone away", "No end of pain is named in unit 10.")],
            "The measure is for excessive flow of blood.",
            "अतिस्रवति रक्ते = when the blood flows too much."),
        order(1, "Put the words of unit 10 in the line's order.",
              ["अतिस्रवति", "तु", "रक्ते", "ततः एव", "अक्षमात्रम्", "प्राशयेत्"],
              "Flowing too much, but, the blood, from that very, an akṣa measure, one should make her take.",
              "अतिस्रवति → तु → रक्ते → ततः एव → अक्षमात्रम् → प्राशयेत्."),
        match(2, "Match each word of unit 10 to its meaning.",
              [["अतिस्रवति", "flowing too much"], ["रक्त", "blood"], ["ततः", "from that"],
               ["अक्ष", "a unit of weight"], ["प्राशयेत्", "should make her take"]],
              "When blood flows too much, an akṣa of that very preparation is given.",
              "अतिस्रवति, रक्त, ततः, अक्ष, प्राशयेत्.", role="extend",
              teaches="अति- = too much: अतिस्रवति = flowing too much."),
        mcq("discriminate", 3, "Which split of तत एव in unit 10 is right?",
            ("ततः + एव", "After अ, a visarga before a vowel other than अ is dropped."),
            [("तत + एव", "तत + एव would join to ततैव (अ + ए → ऐ)."),
             ("ततो + एव", "ततो is not a base form; ओ is itself a sandhi result of ततः, and the word is ततः."),
             ("तते + व", "व is not the word; the word is एव.")],
            "ततः (from that) + एव (very): अः before ए → अ, with a gap left.",
            "अः + vowel other than अ → अ (visarga dropped)."),
        mcq("apply", 4, "A pregnant woman bleeds too much. By unit 10, what is done?",
            ("She is made to take an akṣa measure", "अक्षमात्रं प्राशयेत्."),
            [("She is given cleansing (śodhana)", "Unit 21 excludes the cleansing treatments."),
             ("She is made to fast for a day", "No fasting is named in unit 10."),
             ("She is made to walk about and to yawn", "No walking or yawning is named in unit 10.")],
            "An akṣa measure of that very preparation is given.",
            "ततः एव अक्षमात्रं प्राशयेत्."),
        mcq("transfer", 5, "By the rule of तत एव, how is रामः + इति (thus, Rāma) written?",
            ("राम इति", "अः before इ drops its visarga, as ततः + एव."),
            [("रामो इति", "ओ comes before voiced consonants, not before इ."),
             ("रामेति", "After the visarga drops, the vowels are not joined again."),
             ("रामरिति", "र् comes after vowels other than अ and आ.")],
            "रामः + इति = राम इति, like ततः + एव = तत एव.",
            "अः + vowel other than अ → अ (visarga dropped).",
            teaches="A visarga after अ is dropped before a vowel other than अ, and the gap stays: ततः + एव → तत एव."),
    ],
}

# ---------------------------------------------------------------- unit 11
AUTHORED["11"] = {
    "title": "केवलादेव वा क्षीरसर्पिषः",
    "question": "By unit 11, what is the other source of the measure?",
    "rule": ("Or from the milk-and-ghee (क्षीरसर्पिस्) alone, plain (केवलात् एव): the measure and the verb are carried "
             "from unit 10."),
    "limits": ("Elliptical: no verb or measure is printed here. केवल (plain) contrasts with the milk-ghee cooked with "
               "tat-śṛṅga of unit 9, whose śṛṅga is uncertain. No amount of its own is given."),
    "explain_hi": ("अथवा केवल (सादे) दूध-घी में से ही। "
                   "यहाँ क्रिया और मात्रा नहीं छपी; वे इकाई १० से समझी जाती हैं। "
                   "‘केवलात्’ उस दूध-घी के विपरीत है जो इकाई ९ में शृङ्ग के साथ पकाया गया था, यानी यह सादा है। "
                   "‘केवलादेव’ में केवलात् + एव है; स्वर से पहले त् का द् हुआ है।"),
    "hook": "या सादा दूध-घी ही।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 11, what is the other source of the measure?",
            ("Milk-and-ghee alone, plain", "केवलात् एव क्षीरसर्पिषः: from the plain milk-and-ghee."),
            [("Honey mixed with sugar", "Honey and sugar come in unit 12."),
             ("A decoction of banyan", "The nyagrodha decoction is sprinkled in unit 8."),
             ("Hare's blood with honey added", "Hare's blood is unit 14.")],
            "Or from the plain milk-and-ghee.",
            "केवलादेव वा क्षीरसर्पिषः."),
        order(1, "Put the words of unit 11 in the line's order.",
              ["केवलात्", "एव", "वा", "क्षीरसर्पिषः"],
              "From the plain, indeed, or, milk-and-ghee.",
              "केवलात् → एव → वा → क्षीरसर्पिषः."),
        match(2, "Match each word of unit 11 to its meaning.",
              [["केवल", "alone, plain"], ["एव", "indeed, only"], ["वा", "or"], ["क्षीर", "milk"], ["सर्पिस्", "ghee"]],
              "Or from the plain milk-and-ghee.",
              "केवल, एव, वा, क्षीर, सर्पिस्.", role="extend",
              teaches="क्षीरसर्पिस् = milk and ghee together; केवल = plain, alone."),
        mcq("discriminate", 3, "Which split of केवलादेव is right?",
            ("केवलात् + एव", "त् before a vowel becomes द्."),
            [("केवला + देव", "देव (god) has no place here; the word is एव."),
             ("केवल + अदेव", "अदेव is not the word; the words are केवलात्, एव."),
             ("केवलाः + एव", "आः + ए would lose the visarga: केवला एव.")],
            "केवलात् (from the plain) + एव: त् + vowel → द्.",
            "त् + vowel → द्."),
        fill(4, "Or from the plain milk-and-ghee: ____ एव वा क्षीरसर्पिषः (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("केवलात्", None, "केवलाद्"),
             "केवलादेव = केवलात् + एव.",
             "केवलात् is ablative singular of केवल: from the plain one.",
             "केवलात् एव = from the plain one alone.", role="apply"),
        mcq("transfer", 5, "By the rule of केवलादेव, how is जगत् + ईशः (lord of the world) written when joined?",
            ("जगदीशः", "त् before a vowel becomes द्, as केवलात् + एव."),
            [("जगतीशः", "Before a vowel the त् does not stay unvoiced."),
             ("जगदेशः", "The ई of ईशः does not change to ए."),
             ("जगनीशः", "त् does not become न् before a vowel.")],
            "जगत् + ईशः = जगदीशः, like केवलात् + एव = केवलादेव.",
            "त् + vowel → द्.",
            teaches="A final त् becomes द् before a vowel: केवलात् + एव → केवलादेव."),
    ],
}

# ---------------------------------------------------------------- unit 12
AUTHORED["12"] = {
    "title": "पद्मोत्पलकुमुदकिंजल्कं च समधुशर्करं लेहयेत्",
    "question": "By unit 12, what two things is she made to lick?",
    "rule": ("She is made to lick (लेहयेत्) the filaments (किञ्जल्क) of padma, utpala and kumuda with honey and sugar; or a "
             "powder of dhātakī, gairika, sarjarasa and rasāñjana with honey (समधु)."),
    "limits": ("That किञ्जल्क goes with all three flowers, and that dhātakī is part of the powder, are the data's readings, "
               "not sure. Labels: padma, dhātakī, gairika standard; utpala, kumuda, sarjarasa, rasāñjana probable."),
    "explain_hi": ("दो विकल्प चटाने के हैं (लेहयेत्)। "
                   "पहला: पद्म (कमल, मानक), उत्पल (सम्भावित: जल-कुमुदिनी) और कुमुद (सम्भावित: श्वेत कुमुदिनी) के केसर (किञ्जल्क), शहद और शर्करा के साथ। "
                   "दूसरा: धातकी (धाय, मानक), गैरिक (गेरू, मानक), सर्जरस (सम्भावित: साल की राल) और रसाञ्जन (सम्भावित: रसौत) का चूर्ण, केवल शहद के साथ। "
                   "केसर तीनों फूलों का है, और धातकी चूर्ण का भाग है, ये डेटा के पढ़े हुए अर्थ हैं, निश्चित नहीं। "
                   "‘पद्मोत्पल’ में पद्म + उत्पल है (अ + उ → ओ)।"),
    "hook": "कमल-केसर शहद-शक्कर से; या धाय-गेरू चूर्ण शहद से।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 12, with what are the flower filaments licked?",
            ("With honey and sugar", "समधुशर्करम्: with honey and sugar (śarkarā)."),
            [("With ghee and with milk", "Ghee and milk are not named in unit 12."),
             ("With salt and oil", "Salt and oil are not named in unit 12."),
             ("With goat's milk", "Goat's milk is not named in unit 12.")],
            "The filaments are licked with honey and sugar.",
            "स + मधु + शर्करा = with honey and sugar."),
        order(1, "Put the parts of unit 12 in the line's order.",
              ["पद्मोत्पलकुमुदकिंजल्कम्", "समधुशर्करम्", "लेहयेत्", "धातकी", "गैरिकसर्जरसरसाञ्जनचूर्णम्", "समधु"],
              "The filaments, with honey and sugar, one should make her lick; dhātakī, the powder of gairika ..., with honey.",
              "...किंजल्कम् → समधुशर्करम् → लेहयेत् → धातकी → ...चूर्णम् → समधु."),
        match(2, "Match each word of unit 12 to its meaning, with the data's label.",
              [["पद्म", "lotus (standard)"], ["किञ्जल्क", "filaments, stamens"], ["शर्करा", "sugar"],
               ["धातकी", "woodfordia flowers (standard)"], ["गैरिक", "red ochre (standard)"]],
              "Lotus filaments with honey and sugar; dhātakī and red ochre in the powder.",
              "पद्म, किञ्जल्क, शर्करा, धातकी, गैरिक.", role="extend",
              teaches="किञ्जल्क = the filaments of a flower; गैरिक = red ochre (standard)."),
        mcq("discriminate", 3, "Which split of पद्मोत्पल is right?",
            ("पद्म + उत्पल", "अ + उ → ओ: पद्म + उत्पल = पद्मोत्पल."),
            [("पद्मः + उत्पल", "A compound member has no visarga here."),
             ("पद्मो + त्पल", "त्पल is not a word; the word is उत्पल."),
             ("पद्म + ओत्पल", "ओत्पल is not a word, and अ + ओ would give औ.")],
            "पद्म (lotus) + उत्पल (probably a water lily): अ + उ → ओ.",
            "अ + उ → ओ."),
        mcq("apply", 4, "By unit 12, which of these goes into the powder licked with honey?",
            ("Gairika (red ochre)", "गैरिक is a member of the powder."),
            [("Śarkarā (sugar)", "Sugar goes with the filaments; the powder is only समधु."),
             ("Padma filaments", "The filaments are the first lickable, not the powder."),
             ("Nyagrodha bark and shoots", "The nyagrodha bark-and-shoot paste is unit 13.")],
            "The powder: dhātakī, gairika, sarjarasa, rasāñjana, with honey.",
            "गैरिकसर्जरसरसाञ्जनचूर्णं वा समधु."),
        mcq("transfer", 5, "By the rule of समधु (with honey), what does सजलम् mean?",
            ("With water", "स- = with: स + जल = with water, as स + मधु."),
            [("Without water", "Without would be निर्- or अ-, not स-."),
             ("Water and honey", "स- does not add honey; it means with."),
             ("A lot of water", "स- does not mean much; it means with.")],
            "सजलम् = with water, like समधु = with honey.",
            "स- (prefix) = with.",
            teaches="स- before a noun means with: स + मधु = समधु, with honey."),
    ],
}

# ---------------------------------------------------------------- unit 13
AUTHORED["13"] = {
    "title": "न्यग्रोधादित्वक्प्रवालकल्कंवा",
    "question": "By unit 13, from which parts of which trees is the paste made?",
    "rule": ("Or a paste (कल्क) of the bark (त्वक्) and the tender shoots (प्रवाल) of nyagrodha (banyan, standard) and "
             "the others."),
    "limits": ("Elliptical: no verb is printed, and how the paste is used is not stated. The members of the nyagrodha group "
               "are not listed. No amount is given."),
    "explain_hi": ("अथवा न्यग्रोध (बरगद) आदि की छाल (त्वक्) और कोंपल (प्रवाल) का कल्क, यानी लुगदी। "
                   "क्रिया नहीं छपी; कल्क का प्रयोग कैसे हो, यह नहीं बताया गया। "
                   "‘न्यग्रोधादि’ = न्यग्रोध और अन्य, जैसे इकाई ८ में। "
                   "छपाई में ‘कल्कंवा’ जुड़ा है: कल्कम् + वा → कल्कं वा (व्यंजन से पहले म् का अनुस्वार)।"),
    "hook": "बरगद आदि की छाल और कोंपल की लुगदी।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 13, which parts of the trees go into the paste?",
            ("Bark and tender shoots", "त्वक्प्रवाल: bark and tender shoots."),
            [("Roots and flowers", "Roots and flowers are not named in unit 13."),
             ("Ripe fruits and their seeds", "Fruits and seeds are not named in unit 13."),
             ("Leaves and resin", "Leaves and resin are not named in unit 13.")],
            "The paste is of bark and tender shoots.",
            "त्वक् + प्रवाल + कल्क."),
        order(1, "Put the parts of the compound of unit 13 in order.",
              ["न्यग्रोध", "आदि", "त्वक्", "प्रवाल", "कल्कम्"],
              "Nyagrodha, and the others, bark, tender shoots, paste.",
              "न्यग्रोध → आदि → त्वक् → प्रवाल → कल्कम्."),
        match(2, "Match each word of unit 13 to its meaning.",
              [["न्यग्रोध", "banyan (standard)"], ["आदि", "and the others"], ["त्वक्", "bark"],
               ["प्रवाल", "tender shoot"], ["कल्क", "paste"]],
              "A paste of the bark and shoots of the nyagrodha group.",
              "न्यग्रोध, आदि, त्वक्, प्रवाल, कल्क.", role="extend",
              teaches="कल्क = a paste of ground drugs; प्रवाल = a tender shoot."),
        mcq("discriminate", 3, "Why is कल्कम् printed कल्कं before वा in unit 13?",
            ("Final म् before a consonant becomes ं", "व is a consonant, so कल्कम् → कल्कं."),
            [("The ं marks the plural of कल्क", "कल्कम् is singular; ं here is sandhi."),
             ("The ं marks the instrumental", "कल्कम् is accusative; ं here is sandhi."),
             ("Final म् becomes ं before vowels too", "Before a vowel म् joins it: कल्कमत्र.")],
            "कल्कम् + वा = कल्कं वा: म् before a consonant → anusvāra.",
            "Final म् + consonant → ं."),
        multi("apply", 4, "Which statements fit unit 13?",
              [("It is made from nyagrodha alone", "-आदि adds the other trees of the group."),
               ("The paste is of bark and tender shoots", "Right: त्वक्प्रवालकल्कम्."),
               ("How the paste is used is not stated", "Right: the note says so."),
               ("The paste is to be drunk with milk", "No milk or drinking is named.")],
              [1, 2],
              "Bark and shoots of the nyagrodha group; the use is not stated.",
              "न्यग्रोधादित्वक्प्रवालकल्कं वा."),
        mcq("transfer", 5, "By the rule of कल्कं वा, how is फलम् + वा (or the fruit) written?",
            ("फलं वा", "Final म् before the consonant व becomes ं."),
            [("फलो वा", "ओ comes from अः, not from अम्."),
             ("फलमा वा", "No vowel is added after म्."),
             ("फलान् वा", "That changes the word to the plural.")],
            "फलम् + वा = फलं वा, like कल्कम् + वा = कल्कं वा.",
            "Final म् + consonant → ं.",
            teaches="A final म् before a consonant becomes anusvāra: कल्कम् + वा → कल्कं वा."),
    ],
}

# ---------------------------------------------------------------- unit 14
AUTHORED["14"] = {
    "title": "शशौणहरिणरुधिरं वा सक्षौद्रं पाययेत्",
    "question": "By unit 14, what is she made to drink, and with what?",
    "rule": ("Or one should make her drink (पाययेत्, causative) the blood (रुधिर) of the hare (शश) and the deer (हरिण), "
             "probably also of the eṇa antelope, with honey (सक्षौद्रम्)."),
    "limits": ("Printed शशौण: the eṇa antelope rests on a conjecture (शश + एण → शशैण): no question on it. No amount or "
               "number of times is given."),
    "explain_hi": ("अथवा खरगोश (शश) और हिरण (हरिण) का रक्त (रुधिर) शहद (क्षौद्र) के साथ पिलाएँ। "
                   "छपा ‘शशौण’ अस्पष्ट है; ‘एण’ मृग अनुमानित पाठ (शश + एण → शशैण) पर है, इसलिए सम्भावित। "
                   "‘पाययेत्’ प्रेरणार्थक विधिलिङ् है: पिलाए, यानी उसे पान कराए। "
                   "मात्रा नहीं दी गई।"),
    "hook": "खरगोश-हिरण का रक्त, शहद के साथ पिलाओ।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 14, what is she made to drink?",
            ("Blood of the hare and the deer", "शश...हरिणरुधिरम्: the blood of the hare ... and the deer."),
            [("Juice pressed from bitter neem leaves", "No neem is named in unit 14."),
             ("Hot water with black pepper and salt", "Nothing hot or sharp is named; the measures here are cool."),
             ("Sour gruel with rock salt and oil", "No gruel or salt is named in unit 14.")],
            "Hare's and deer's blood, with honey.",
            "...रुधिरं वा सक्षौद्रं पाययेत्."),
        order(1, "Put the words of unit 14 in the line's order.",
              ["शशौणहरिणरुधिरम्", "वा", "सक्षौद्रम्", "पाययेत्"],
              "The blood of the hare ... and deer, or, with honey, one should make her drink.",
              "शशौणहरिणरुधिरम् → वा → सक्षौद्रम् → पाययेत्."),
        match(2, "Match each word of unit 14 to its meaning.",
              [["शश", "hare"], ["हरिण", "deer"], ["रुधिर", "blood"], ["क्षौद्र", "honey"],
               ["पाययेत्", "should make her drink"]],
              "The blood of the hare and deer, with honey, to drink.",
              "शश, हरिण, रुधिर, क्षौद्र, पाययेत्.", role="extend",
              teaches="क्षौद्र = honey; सक्षौद्रम् = with honey."),
        mcq("discriminate", 3, "What does the causative पाययेत् of unit 14 mean?",
            ("One should make her drink", "Causative of √पा: make (her) drink."),
            [("She should drink by herself", "That would be पिबेत्, not the causative."),
             ("One drank it in the past", "पाययेत् is optative, not past."),
             ("She will drink it later", "पाययेत् is optative, not future.")],
            "पाययेत् = one should make (her) drink: causative optative.",
            "Causative: पिबति (drinks) → पाययति (makes drink)."),
        multi("apply", 4, "Whose blood does unit 14 name for certain?",
              [("Goat (अज)", "No goat is named in unit 14."),
               ("Hare (शश)", "Right: शश, hare."),
               ("Boar (वराह)", "No boar is named in unit 14."),
               ("Deer (हरिण)", "Right: हरिण, deer.")],
              [1, 3],
              "Hare and deer are sure; the eṇa antelope is conjectural.",
              "शश ... हरिण ... रुधिरम्."),
        mcq("transfer", 5, "By the pattern of पाययेत्, which causative optative means one should make (him) know?",
            ("ज्ञापयेत्", "Causative of √ज्ञा with -पय-, as √पा → पाययेत्."),
            [("जानीयात्", "जानीयात् is the plain optative: he should know."),
             ("ज्ञास्यति", "ज्ञास्यति is a future: he will know."),
             ("ज्ञातवान्", "ज्ञातवान् is a past form: he knew.")],
            "ज्ञापयेत् = one should make (him) know, like पाययेत् = one should make (her) drink.",
            "Causative optative: √पा → पाययेत्, √ज्ञा → ज्ञापयेत्.",
            teaches="A causative (make someone do) optative: √पा (drink) → पाययेत्, one should make her drink."),
    ],
}


# ===================================================================== NOTES_HI
NOTES_HI = {
    "1": ("गद्य-पंक्ति; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। ‘शारीरम्’ सम्भवतः स्थान का नाम है, पर शब्दार्थ ‘शरीर सम्बन्धी’ रखा गया। "
          "गर्भव्यापद = गर्भावस्था की जटिलताएँ (सम्भावित)। सन्धि जाँची: अथ + अतः → अथातः (अ + अ → आ); अतः + गर्भ... → अथातो गर्भ... "
          "(अः + घोष व्यंजन → ओ); व्यंजन से पहले म् → ं (गर्भव्यापदं, शारीरं)।"),
    "2": ("गद्य; विश्वास मध्यम। पाठ-चिह्न: छपा ‘परिहार्याण्यसेवेत’ (ह्रस्व अ); परिहार्याणि + आसेवेत से ‘परिहार्याण्यासेवेत’ अपेक्षित, "
          "इसलिए क्रिया सुधारे पाठ पर पढ़ी गई; इस पर कोई प्रश्न नहीं। त्यागने योग्य वस्तुएँ यहाँ नामित नहीं। सन्धि जाँची: चेत् + आपन्न → "
          "चेदापन्न (त् + स्वर → द्); आपन्नगर्भा और परिहार्याणि छपाई में जुड़े हैं। वाक्य आगे की इकाइयों में चलता है।"),
    "3": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। वाक्य इकाई ४ में पूरा होता है। ‘मुख’ केवल योनि से या पूरी सूची से जुड़ता है, यह "
          "अनिश्चित है। पुष्पदर्शन = रक्तस्राव (सम्भावित)। सन्धि जाँची: यस्याः + बस्ति → यस्या बस्ति (आः + घोष → आ); शूलम् और "
          "पुष्पदर्शनम् का म् व्यंजन से पहले ं।"),
    "4": ("गद्य; विश्वास मध्यम। पाठ-चिह्न: ‘मृदुमुख’ के स्थान पर ‘मृदुसुख’ (आरामदायक) सम्भव, पर छपा पाठ रखा गया; पहले समास का "
          "विभाजन अनिश्चित। सन्धि जाँची: ताम् → तां (व्यंजन से पहले); शिशिर + आस्तरण → शिशिरास्तरण (अ + आ → आ); शयनस्थाम् + ईषत् "
          "→ शयनस्थामीषत्; ईषत् + अवनत → ईषदवनत (त् + स्वर → द्); आदिभिः + उपाचरेत् → आदिभिरुपाचरेत् (इः + स्वर → इर्); उप + आचरेत् "
          "→ उपाचरेत्।"),
    "5": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। यह इकाई ६ से आरम्भ होने वाले उपायों की सूची का परिचय है। सन्धि जाँची: तत् + यथा → "
          "तद्यथा (घोष य से पहले त् → द्)।"),
    "6": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। ‘सहस्रधौतेन’ और ‘सर्पिषा’ छपाई में जुड़े हैं। ‘सर्पिषाऽधो’ का अवग्रह छपाई का चिह्न "
          "है (सर्पिषा + अधः से केवल सर्पिषाधः बनता); इस पर प्रश्न नहीं। सन्धि जाँची: अधः + नाभेः → अधोनाभेः (अः + घोष व्यंजन → ओ); "
          "नाभेः + सर्वतः में विसर्ग स से पहले बना रहता है। घी किससे धोया जाए, और कर्म (स्थान), नहीं कहे गए।"),
    "7": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। मधुक = मुलेठी (मानक); मधूक (महुआ) अलग द्रव्य। ‘मधुकसर्पिषा’ को द्वन्द्व "
          "(मधुक और घी) भी पढ़ा जा सकता है। सन्धि जाँची: सु + शीतेन → सुशीतेन; पिचुम् + आप्लाव्य → पिचुमाप्लाव्य (स्वर से पहले म्); "
          "आ + प्लाव्य → आप्लाव्य (उपसर्ग सहित, इसलिए -य)।"),
    "8": ("गद्य; विश्वास उच्च। पाठ-चिह्न: छपा ‘मधुकम्बुना’ ह्रस्व अ वाला; मधुक + अम्बुना → मधुकाम्बुना अपेक्षित (अ + अ → आ); इस "
          "सन्धि पर प्रश्न नहीं। न्यग्रोध = बरगद (मानक)। न्यग्रोधादि समूह के सदस्य यहाँ नहीं गिनाए। सन्धि जाँची: न्यग्रोध + आदि → "
          "न्यग्रोधादि (अ + आ → आ)। कर्म (किसे सींचें) नहीं कहा गया।"),
    "9": ("गद्य; विश्वास निम्न। पाठ-चिह्न: ‘परिपीततत्वरसानि’ क्षतिग्रस्त; ‘तत्त्व’ शब्द यहाँ नहीं बैठता; ‘परिपीत-तत्-त्वग्-रसानि’ "
          "(उनकी छाल के रस सोखे) केवल अनुमान, अपनाया नहीं गया। ‘तैलानि’ और ‘योनौ’ छपाई में जुड़े हैं। शृङ्ग = कोंपल सम्भावित (विवादित); "
          "‘तत्’ इकाई ८ के न्यग्रोध-समूह की ओर, यह भी अनुमान। सन्धि जाँची: तत् + शृङ्ग → तच्छृङ्ग (त् + श → च्छ); पिचुम् → पिचुं "
          "(पंक्ति-अन्त में छपा ं)। दूसरी पंक्ति की क्रिया इकाई ७ से समझी जाती है।"),
    "10": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। ‘ततः एव’ इकाई ९ के दूध-घी की ओर (डेटा का पाठ)। डेटा के अनुसार अक्ष = पिचु = "
           "कर्ष, मानक गणना में लगभग १० ग्राम। सन्धि जाँची: ततः + एव → तत एव (अः + अ-भिन्न स्वर → अ, विसर्ग लोप); एव + अक्ष → "
           "एवाक्ष (अ + अ → आ); अक्षमात्रम् → अक्षमात्रं।"),
    "11": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। मात्रा और क्रिया इकाई १० से समझी जाती हैं, छपी नहीं। ‘केवलात्’ = सादा, इकाई ९ "
           "के शृङ्ग-सिद्ध दूध-घी के विपरीत। सन्धि जाँची: केवलात् + एव → केवलादेव (त् + स्वर → द्)।"),
    "12": ("गद्य; विश्वास मध्यम; दो छपी पंक्तियाँ। [02.04.13] किञ्जल्क तीनों फूलों का माना गया; ‘पद्म, उत्पल और कुमुद का किञ्जल्क’ "
           "भी सम्भव। पहचान: पद्म = कमल (मानक); उत्पल = जल-कुमुदिनी (सम्भावित); कुमुद = श्वेत कुमुदिनी (सम्भावित)। [02.04.14] "
           "पाठ-चिह्न: ‘धातकी’ के बाद छपा रिक्त स्थान, पर एकवचन ‘चूर्णम्’ से धातकी चूर्ण का भाग मानी गई; दूसरा पाठ: ‘धातकी, या "
           "गैरिक-सर्जरस-रसाञ्जन का चूर्ण’। धातकी (मानक), गैरिक (मानक), सर्जरस = साल की राल (सम्भावित), रसाञ्जन = रसौत "
           "(सम्भावित)। क्रिया ‘लेहयेत्’ दूसरी पंक्ति में भी समझी जाती है। सन्धि जाँची: पद्म + उत्पल → पद्मोत्पल (अ + उ → ओ); "
           "छपा किंजल्क = किञ्जल्क, रसांजन = रसाञ्जन।"),
    "13": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। क्रिया नहीं छपी; कल्क का प्रयोग नहीं बताया गया। ‘कल्कं’ और ‘वा’ छपाई में जुड़े। "
           "सन्धि जाँची: न्यग्रोध + आदि → न्यग्रोधादि (अ + आ → आ); त्वच् का पद-रूप त्वक् (अघोष प से पहले क्); कल्कम् + वा → कल्कं "
           "वा (व्यंजन से पहले म् → ं)।"),
    "14": ("गद्य; विश्वास मध्यम। पाठ-चिह्न: छपा ‘शशौण’; ‘औण’ कोई ज्ञात शब्द नहीं; शश + एण → शशैण (अ + ए → ऐ) अनुमानित पाठ, "
           "इसलिए एण मृग ‘सम्भवतः’। इस पर कोई प्रश्न नहीं। सन्धि जाँची: रुधिरम् + वा → रुधिरं वा; स + क्षौद्रम् → सक्षौद्रम्; "
           "क्षौद्रम् → क्षौद्रं (व्यंजन से पहले)।"),
}


# ===================================================================== AIDS
AIDS = {
    "1": {
        "chunks": "अथातो | गर्भव्यापदं | शारीरं | व्याख्यास्यामः",
        "sandhi": "अ + अ → आ: अथ + अतः → अथातः · अः + घोष व्यंजन → ओ: अथातः + गर्भ... → अथातो गर्भ...",
        "frame": "कब: अथ अतः (अब, इसलिए) → किसका: गर्भव्यापदम् (गर्भ की विपत्तियाँ) → क्रिया: व्याख्यास्यामः (हम व्याख्या करेंगे)।",
    },
    "2": {
        "chunks": "स्त्री चेद् | आपन्नगर्भा | परिहार्याण्यसेवेत",
        "sandhi": "त् + स्वर → द्: चेत् + आपन्न → चेदापन्न।",
        "frame": "शर्त: चेत् (यदि) → कर्ता: स्त्री आपन्नगर्भा (गर्भवती) → कर्म: परिहार्याणि (त्यागने योग्य, नाम नहीं) → क्रिया: आसेवेत (सेवन करे)। मुख्य वाक्य आगे।",
    },
    "3": {
        "diagram": {"groups": [
            {"label": "शूल के स्थान (क्रम से)", "items": ["बस्ति (मूत्राशय-क्षेत्र)", "पार्श्व", "श्रोणि", "योनिमुख"]},
            {"label": "या", "items": ["पुष्पदर्शन (सम्भवतः रक्तस्राव)"]}]},
        "chunks": "तत्र यस्या | बस्तिपार्श्वश्रोणियोनिमुखेषु शूलं | पुष्पदर्शनं वा स्यात्",
        "sandhi": "आः + घोष → आ: यस्याः + बस्ति → यस्या बस्ति।",
        "letters": "चार स्थानों के पहले अक्षर क्रम से: ब-पा-श्रो-यो (बस्ति, पार्श्व, श्रोणि, योनिमुख)। (मेरी याद-पद्धति)",
    },
    "4": {
        "chain": {"steps": ["कोमल-शीतल बिछावन की शय्या पर", "सिर थोड़ा झुका हुआ", "शीतल प्रदेह, परिषेक आदि से उपचार"]},
        "chunks": "तां | मृदुमुखशिशिरास्तरणशयनस्थाम् | ईषदवनतशिरसं | शीतप्रदेहपरिषेकादिभिः | उपाचरेत्",
        "sandhi": "त् + स्वर → द्: ईषत् + अवनत → ईषदवनत · इः + स्वर → इर्: आदिभिः + उपाचरेत् → आदिभिरुपाचरेत्।",
        "contrast": "सब शीतल: बिछावन शिशिर, लेप शीत, परिषेक शीत; सिर ऊँचा नहीं, थोड़ा नीचे। (मेरी याद-पद्धति)",
    },
    "5": {
        "sandhi": "त् + घोष (स्वर, ग, ब, य ...) → द्: तत् + यथा → तद्यथा।",
        "anchors": "याद-सूत्र: ‘तद्यथा’ = अब सूची शुरू; उपाय इकाई ६ से। (मेरी याद-पद्धति)",
    },
    "6": {
        "chunks": "सहस्रधौतेन सर्पिषा | अधोनाभेः सर्वतः | प्रदिह्यात्",
        "sandhi": "अः + घोष व्यंजन → ओ: अधः + नाभेः → अधोनाभेः।",
        "frame": "साधन: सहस्रधौतेन सर्पिषा (हज़ार बार धुले घी से) → कहाँ: अधः नाभेः सर्वतः (नाभि के नीचे चारों ओर) → क्रिया: प्रदिह्यात् (लेप करे)।",
    },
    "7": {
        "chain": {"steps": ["सुशीत मधुक-घृत (मुलेठी, मानक)", "उसमें पिचु भिगोना (आप्लाव्य)", "योनि के पास रखना (स्थापयेत्)"]},
        "chunks": "मधुकसर्पिषा सुशीतेन | पिचुमाप्लाव्य | योनिसमीपे स्थापयेत्",
        "sandhi": "स्वर से पहले म्: पिचुम् + आप्लाव्य → पिचुमाप्लाव्य।",
    },
    "8": {
        "diagram": {"groups": [
            {"label": "परिषेक के द्रव (क्रम से)", "items": ["गाय का दूध", "मधुक (मुलेठी) का जल",
                                                          "न्यग्रोध (बरगद, मानक) आदि का काढ़ा"]}]},
        "chunks": "गव्येन पयसा | मधुकम्बुना | न्यग्रोधादिकषायेण वा | परिषेचयेत्",
        "sandhi": "अ + आ → आ: न्यग्रोध + आदि → न्यग्रोधादि।",
    },
    "9": {
        "chunks": "परिपीततत्वरसानि (?) च | तैलानियोनौ निधापयेत् | तच्छृङ्गसिद्धस्य वा | क्षीरसर्पिषः पिचुं",
        "sandhi": "त् + श → च्छ: तत् + शृङ्ग → तच्छृङ्ग।",
        "frame": "पहला: तैलानि (कर्म) → योनौ (कहाँ) → निधापयेत् (रखवाए) · या दूसरा: शृङ्ग-सिद्ध क्षीरसर्पि का पिचु (क्रिया इकाई ७ से)।",
    },
    "10": {
        "chain": {"steps": ["रक्त बहुत बहे (अतिस्रवति रक्ते)", "उसी में से (ततः एव)", "अक्ष-मात्रा खिलाए (प्राशयेत्)"]},
        "chunks": "अतिस्रवति तु रक्ते | तत एवाक्षमात्रं | प्राशयेत्",
        "sandhi": "अः + अ-भिन्न स्वर → अ: ततः + एव → तत एव · अ + अ → आ: एव + अक्ष → एवाक्ष।",
    },
    "11": {
        "chunks": "केवलादेव वा | क्षीरसर्पिषः",
        "sandhi": "त् + स्वर → द्: केवलात् + एव → केवलादेव।",
        "contrast": "इकाई ९: शृङ्ग के साथ पका दूध-घी ↔ इकाई ११: केवल (सादा) दूध-घी।",
    },
    "12": {
        "diagram": {"groups": [
            {"label": "पहला लेह: शहद + शर्करा के साथ", "items": ["पद्म (कमल, मानक)", "उत्पल (सम्भावित)",
                                                              "कुमुद (सम्भावित)", "इनका किञ्जल्क (केसर; तीनों का माना गया)"]},
            {"label": "दूसरा लेह: केवल शहद के साथ, चूर्ण", "items": ["धातकी (धाय, मानक; चूर्ण में मानी गई)", "गैरिक (गेरू, मानक)",
                                                                  "सर्जरस (साल-राल, सम्भावित)", "रसाञ्जन (रसौत, सम्भावित)"]}]},
        "chunks": "पद्मोत्पलकुमुदकिंजल्कं च | समधुशर्करं लेहयेत् | धातकी गैरिकसर्जरसरसांजनचूर्णं वा | समधु",
        "sandhi": "अ + उ → ओ: पद्म + उत्पल → पद्मोत्पल।",
        "contrast": "पहले लेह में शहद और शर्करा दोनों; दूसरे चूर्ण में केवल शहद (समधु)।",
    },
    "13": {
        "chunks": "न्यग्रोधादि | त्वक्प्रवाल | कल्कं वा",
        "sandhi": "व्यंजन से पहले म् → ं: कल्कम् + वा → कल्कं वा।",
        "frame": "किसका: न्यग्रोधादि (बरगद आदि) → कौन-से भाग: त्वक् (छाल), प्रवाल (कोंपल) → क्या: कल्क (लुगदी)। क्रिया नहीं छपी।",
    },
    "14": {
        "chunks": "शशौणहरिणरुधिरं वा | सक्षौद्रं पाययेत्",
        "sandhi": "अ + ए → ऐ: शश + एण → शशैण (अनुमानित पाठ; छपा शशौण)।",
        "frame": "किसका रक्त: शश (खरगोश), (सम्भवतः एण), हरिण → किसके साथ: सक्षौद्रम् (शहद सहित) → क्रिया: पाययेत् (पिलाए)।",
    },
}


# ===================================================================== IMAGE_SPECS
IMAGE_SPECS = {
    ("3", "diagram"): {
        "file": "sh4-garbhini-shula-3.svg",
        "alt": ("Two columns of unit 3. Places of pain in line order: bladder region (basti), flanks, hips, mouth of the "
                "yoni. Or: the sight of puṣpa, probably bleeding."),
        "type": "split",
        "title": "इकाई ३: शूल या पुष्पदर्शन",
        "cols": [["शूल के स्थान (क्रम से)", ["१ बस्ति (मूत्राशय-क्षेत्र)", "२ पार्श्व", "३ श्रोणि", "४ योनिमुख"]],
                 ["या", ["पुष्पदर्शन (सम्भवतः रक्तस्राव)"]]],
    },
    ("4", "chain"): {
        "file": "sh4-shita-upachara-4.svg",
        "alt": ("Chain of unit 4: on a bed with a soft, cool spread; head slightly lowered; treated with cool plasters, "
                "sprinklings and the like."),
        "type": "chain",
        "title": "इकाई ४: शीतल उपचार",
        "steps": ["कोमल-शीतल बिछावन की शय्या पर", "सिर थोड़ा झुका हुआ", "शीतल प्रदेह, परिषेक आदि से उपचार"],
    },
    ("7", "chain"): {
        "file": "sh4-madhuka-pichu-7.svg",
        "alt": ("Chain of unit 7: very cool madhuka-ghee (madhuka: licorice, standard); soak a picu (pad) in it; place it "
                "near the yoni."),
        "type": "chain",
        "title": "इकाई ७: मधुक-घृत का पिचु",
        "steps": ["सुशीत मधुक-घृत (मुलेठी, मानक)", "उसमें पिचु भिगोना", "योनि के पास रखना"],
    },
    ("8", "diagram"): {
        "file": "sh4-parisheka-dravya-8.svg",
        "alt": ("Table of unit 8, the three sprinkling liquids in line order: cow's milk; madhuka (licorice) water; "
                "decoction of nyagrodha (banyan, standard) and the others. Action: sprinkle."),
        "type": "table",
        "title": "इकाई ८: परिषेक के द्रव",
        "heads": ["छपा शब्द", "अर्थ"],
        "rows": [["गव्येन पयसा", "गाय के दूध से"], ["मधुकम्बुना", "मधुक (मुलेठी) के जल से"],
                 ["न्यग्रोधादिकषायेण वा", "या न्यग्रोध (बरगद, मानक) आदि के काढ़े से"],
                 ["परिषेचयेत्", "सींचे"]],
    },
    ("10", "chain"): {
        "file": "sh4-atisrava-aksha-10.svg",
        "alt": ("Flowchart of unit 10: when the blood flows too much, from that very preparation, give an akṣa measure."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"रक्त बहुत बहे\"] --> B[\"उसी में से\"]\n"
                 "  B --> C[\"अक्ष-मात्रा खिलाए\"]\n"),
    },
    ("12", "diagram"): {
        "file": "sh4-leha-dvaya-12.svg",
        "alt": ("Two columns of unit 12. First lickable, with honey and sugar: filaments of padma (lotus, standard), utpala "
                "(probable) and kumuda (probable). Second, a powder with honey only: dhātakī (standard), gairika red ochre "
                "(standard), sarjarasa sal resin (probable), rasāñjana (probable)."),
        "type": "split",
        "title": "इकाई १२: दो लेह",
        "cols": [["शहद + शर्करा के साथ", ["पद्म (कमल, मानक)", "उत्पल (सम्भावित)", "कुमुद (सम्भावित)",
                                        "इनका किञ्जल्क (केसर; तीनों का माना गया)"]],
                 ["चूर्ण, केवल शहद के साथ", ["धातकी (धाय, मानक; चूर्ण में मानी गई)", "गैरिक (गेरू, मानक)", "सर्जरस (सम्भावित)",
                                            "रसाञ्जन (सम्भावित)"]]],
    },
}
