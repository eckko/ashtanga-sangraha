from helpers import mcq, match, order, fill, multi, accepts

AUTHORED = {}

# ---------------------------------------------------------------- unit 77 (prose)
AUTHORED["77"] = {
    "title": "शेषेष्वपि … उपद्रवेषु",
    "question": "How, according to unit 77, should the remaining complications of emesis and purgation be treated?",
    "rule": ("In the remaining complications (upadrava) of emesis and purgation, he should counter them according to the "
             "disease (yathāmayam), having regard to the doṣas, and should look to the basti-vyāpat-siddhi."),
    "limits": ("Medium confidence. The printed चा is read as च + the अ of असम्यक् ('improperly'); no question rests on that prefix. "
               "The remaining complications are not listed. basti-vyāpat-siddhi presumably names the chapter on basti complications."),
    "explain_hi": ("यह इकाई उन उपद्रवों के लिए एक सामान्य नियम देती है जिनका अलग से वर्णन नहीं हुआ: अनुचित रूप से दिए गए वमन और "
                   "विरेचन के शेष उपद्रव। उनमें यथामयम्, यानी रोग के अनुसार, और दोषों का विचार करके (दोषान् अपेक्ष्य) प्रतिकार किया जाए। "
                   "साथ ही बस्तिव्यापत्सिद्धि को भी देखा जाए; शाब्दिक अर्थ ‘बस्ति के उपद्रवों की चिकित्सा’, सम्भवतः उस नाम का अध्याय। "
                   "छपे ‘चा’ को च + असम्यक् पढ़ा गया है; केवल रिक्त स्थान गलत जगह छपा है।"),
    "hook": "बाकी उपद्रव: रोग देखो, दोष देखो, और बस्ति-व्यापत्-सिद्धि भी देखो।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "In unit 77, according to what should the remaining complications be countered?",
            ("According to the disease",
             "यथामयम् = यथा + आमयम्: according to the disease."),
            [("According to the season", "No season (ऋतु) is named in unit 77."),
             ("According to the patient's age", "Age is not named in unit 77."),
             ("According to the drug given", "The unit says यथामयम्, by the disease, not by the drug.")],
            "Unit 77: यथामयं दोषानपेक्ष्य प्रतिकुर्यात्, counter by the disease, having regard to the doṣas.",
            "यथामयम् = according to the disease."),
        match(1, "Match each word of unit 77 to its meaning.",
              [["शेषेषु", "in the remaining"], ["उपद्रव", "complication"], ["यथामयम्", "according to the disease"],
               ["अपेक्ष्य", "having regard to"], ["प्रतिकुर्यात्", "should counter"]],
              "The unit's own glosses: the remaining complications, the measure (the disease), the regard (the doṣas), the act.",
              "शेषेषु = in the remaining; उपद्रव = complication; यथामयम् = by the disease; अपेक्ष्य = having regard to; प्रतिकुर्यात् = should counter."),
        order(2, "Put these parts of unit 77 in the order of the text.",
              ["शेषेष्वपि", "…वमनविरेचनोपद्रवेषु", "यथामयं", "दोषानपेक्ष्य", "प्रतिकुर्यात्", "वस्तिव्यापत्तिसिद्धिं चेक्षेत"],
              "Where (the remaining complications), how (by the disease, regarding the doṣas), the act, and the further reading.",
              "शेषेष्वपि · …उपद्रवेषु · यथामयं · दोषानपेक्ष्य · प्रतिकुर्यात् · …चेक्षेत.",
              role="extend",
              teaches="Unit 77 names the complications first (locative), then the two guides (disease, doṣas), the verb, and last the text to consult."),
        mcq("discriminate", 3,
            "Which split of the printed चेक्षेत is right?",
            ("च + ईक्षेत",
             "अ + ई → ए: च + ईक्षेत (should look to) → चेक्षेत."),
            [("चे + क्षेत", "क्षेत is no word; the ए comes from अ + ई."),
             ("चेत् + ईक्षेत", "चेत् before a vowel would print चेदीक्षेत."),
             ("च + एक्षेत", "अ + ए gives ऐ: that would print चैक्षेत.")],
            "च (and) + ईक्षेत (3 sg. optative middle of √ईक्ष्, should look to).",
            "अ + ई → ए: चेक्षेत = च + ईक्षेत."),
        mcq("apply", 4,
            "A complication appears that the chapter has not described. Besides countering it, what does unit 77 tell the physician to look to?",
            ("The basti-vyāpat-siddhi",
             "वस्तिव्यापत्तिसिद्धिं चेक्षेत: and he should look to the basti-vyāpat-siddhi."),
            [("The chapter on poisons", "No chapter on poisons is named in unit 77."),
             ("The rules for the diet", "Diet rules are not named in unit 77."),
             ("The list of emetic fruits", "The unit names no list of emetic fruits.")],
            "Unit 77 ends by pointing to the basti-vyāpat-siddhi, literally the cure of basti complications.",
            "Unit 77: …बस्तिव्यापत्सिद्धिं च ईक्षेत."),
        mcq("transfer", 5,
            "दोषान् + अपेक्ष्य gives दोषानपेक्ष्य. Join the invented pair गुणान् + अवेक्ष्य (having observed the qualities) the same way. Which is right?",
            ("गुणानवेक्ष्य",
             "A final न् after a long vowel joins the next vowel unchanged: गुणान् + अवेक्ष्य = गुणानवेक्ष्य."),
            [("गुणान्नवेक्ष्य", "न् is doubled only after a short vowel; here आ stands before it."),
             ("गुणांवेक्ष्य", "The vowel अ of अवेक्ष्य cannot vanish into an anusvāra."),
             ("गुणानोवेक्ष्य", "No ओ arises from न् + अ.")],
            "Same join as दोषान् + अपेक्ष्य → दोषानपेक्ष्य.",
            "Final न् (after a long vowel) + vowel → न + vowel.",
            teaches="A final न् after a long vowel joins a following vowel unchanged (दोषान् + अपेक्ष्य → दोषानपेक्ष्य; गुणान् + अवेक्ष्य → गुणानवेक्ष्य)."),
    ],
}

# ---------------------------------------------------------------- unit 78 (prose)
AUTHORED["78"] = {
    "title": "एवमुभयतोभागेऽपि शोधने",
    "question": "What does unit 78 extend to cleansing through both portions (ubhayatobhāga)?",
    "rule": ("Thus too, in cleansing through both portions (ubhayatobhāga), he should rise up (uttiṣṭhet) according to the "
             "condition (yathāvastham)."),
    "limits": ("Medium confidence. Ubhayatobhāga is probably cleansing by both the upper and the lower ways (probable; the line "
               "does not say). उत्तिष्ठेत् is literally 'should rise up'; its intended sense (set to work, proceed) is not stated, "
               "so no question rests on that sense. एवम् ('thus') points back to what precedes."),
    "explain_hi": ("‘एवम्’ यानी इसी प्रकार: पहले कही बात अब उस शोधन पर भी लागू होती है जो ‘उभयतोभाग’ है, यानी दोनों भागों वाला; "
                   "सम्भवतः ऊपर और नीचे, दोनों मार्गों से होने वाला शोधन। ऐसे शोधन में यथावस्थम्, यानी अवस्था के अनुसार, ‘उत्तिष्ठेत्’, "
                   "जिसका शाब्दिक अर्थ है ‘उठ खड़ा हो’। इसका अभिप्राय (काम में लगना, आगे बढ़ना) पंक्ति स्पष्ट नहीं करती। "
                   "‘उभयतोभागे’ ‘शोधने’ का विशेषण है; दोनों सप्तमी एकवचन हैं।"),
    "hook": "ऊपर-नीचे दोनों का शोधन? वही नियम, अवस्था देखकर।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "In unit 78, what does यथावस्थम् mean?",
            ("According to the condition",
             "यथा + अवस्थम्: according to the condition (अवस्था)."),
            [("According to the old texts", "No text or authority is named in unit 78."),
             ("After the patient's meal", "No meal is named in unit 78."),
             ("Without any further delay", "Speed is not the sense of यथावस्थम्.")],
            "यथावस्थम् = according to the condition.",
            "यथा + अवस्था → यथावस्थम्."),
        match(1, "Match each word of unit 78 to its meaning.",
              [["एवम्", "thus"], ["उभयतोभाग", "both portions"], ["शोधन", "cleansing"],
               ["यथावस्थम्", "according to the condition"], ["उत्तिष्ठेत्", "should rise up"]],
              "All five glosses are the unit's own; उत्तिष्ठेत् is kept literal.",
              "एवम् = thus; उभयतोभाग = both portions; शोधन = cleansing; यथावस्थम् = by the condition; उत्तिष्ठेत् = should rise up."),
        order(2, "Put the words of unit 78 in the order of the text.",
              ["एवम्", "उभयतोभागे", "अपि", "शोधने", "यथावस्थम्", "उत्तिष्ठेत्"],
              "Thus · in both portions · also · in cleansing · according to the condition · should rise up.",
              "एवम् · उभयतोभागे · अपि · शोधने · यथावस्थम् · उत्तिष्ठेत्.",
              role="extend",
              teaches="Unit 78 names the kind of cleansing (two locatives) before the measure यथावस्थम् and the verb उत्तिष्ठेत्."),
        mcq("discriminate", 3,
            "Which split of the printed उभयतोभागे is right?",
            ("उभयतः + भागे",
             "अः before a voiced consonant becomes ओ: उभयतः + भागे → उभयतोभागे."),
            [("उभयते + भागे", "ए does not turn into ओ; the word is उभयतः."),
             ("उभयत + ओभागे", "ओभाग is no word."),
             ("उभयतो + अभागे", "ओ + अ would print उभयतोऽभागे, with an avagraha.")],
            "उभयतः (on both sides) + भागे (in the portion): the visarga after अ turns to ओ before भ.",
            "अः + voiced consonant → ओ."),
        mcq("apply", 4,
            "Unit 78 opens with एवम् (thus). What does this word tell the reader?",
            ("The rule before applies here too",
             "एवम् … अपि: thus also; the preceding rule is carried over to cleansing through both portions."),
            [("A new, opposite rule begins here", "एवम् carries a rule over; it does not start an opposite one."),
             ("The whole chapter ends at this point", "The chapter goes on; its colophon is at 05.03.111."),
             ("Only basti is meant by this rule", "The unit speaks of शोधन through both portions, not of basti.")],
            "एवम् (thus) with अपि (also) extends what was said before.",
            "एवम् … अपि = thus also."),
        mcq("transfer", 5,
            "उभयतः + भागे gives उभयतोभागे. Which is the right join of the invented pair ततः + गच्छति (then he goes)?",
            ("ततो गच्छति",
             "अः before a voiced consonant becomes ओ: ततः + गच्छति = ततो गच्छति."),
            [("ततर् गच्छति", "ः → र् happens after vowels other than अ/आ, not after अ."),
             ("ततस् गच्छति", "ः → स् happens before त/थ, not before ग."),
             ("तता गच्छति", "अः does not become आ.")],
            "Same rule as उभयतोभागे.",
            "अः + voiced consonant → ओ.",
            teaches="A visarga after अ becomes ओ before a voiced consonant (उभयतः + भागे → उभयतोभागे; ततः + गच्छति → ततो गच्छति)."),
    ],
}

# ---------------------------------------------------------------- unit 79 (prose)
AUTHORED["79"] = {
    "title": "या तु विरेचने परिकर्त्तिका",
    "question": "Which troubles of emesis does unit 79 set against parikartikā, parisrava and pravāhaṇa of purgation?",
    "rule": ("What is parikartikā (cutting pain) in purgation is injury of the throat (kaṇṭha-kṣaṇana) in emesis; the discharge "
             "(parisrava) is the flow of Kapha (kapha-praseka); straining (pravāhaṇa) is dry belching (śuṣka-udgāra)."),
    "limits": ("Three equivalences only: no cause, sign or remedy is given here. That parisrava and pravāhaṇa belong to purgation is "
               "carried over from the first pair. kṣaṇana is literally 'hurting, wounding'. The closing इति only ends the statement."),
    "explain_hi": ("यह इकाई विरेचन के तीन उपद्रवों के वमन वाले रूप बताती है। विरेचन में जो परिकर्तिका यानी काटने जैसी पीड़ा है, वह वमन में "
                   "कण्ठक्षणन यानी गले की क्षति है। जो परिस्रव (स्राव) है, वह वमन में कफप्रसेक यानी कफ का बहना है। जो प्रवाहण (ज़ोर लगाना) है, "
                   "वह वमन में शुष्क उद्गार यानी सूखी डकार है। तीनों वाक्य ‘जो … वह …’ (या … तत्, यः … सः, यत् … सः) के ढाँचे में हैं; "
                   "क्रिया की आवश्यकता नहीं।"),
    "hook": "नीचे काट, ऊपर गला; नीचे स्राव, ऊपर कफ; नीचे ज़ोर, ऊपर सूखी डकार।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "In unit 79, what in emesis corresponds to parikartikā (cutting pain) of purgation?",
            ("Injury of the throat",
             "या तु विरेचने परिकर्त्तिका तद्वमने कंठक्षणनं: in emesis it is injury of the throat."),
            [("Dry belching (udgāra)", "Dry belching corresponds to pravāhaṇa, the third pair."),
             ("Flow of Kapha (praseka)", "The flow of Kapha corresponds to parisrava, the second pair."),
             ("Burning in the chest", "No burning is named in unit 79.")],
            "First pair: parikartikā (purgation) = kaṇṭha-kṣaṇana (emesis).",
            "परिकर्तिका ↔ कण्ठक्षणन."),
        match(1, "Match each word of unit 79 to its meaning.",
              [["परिकर्तिका", "cutting pain"], ["कण्ठक्षणन", "injury of the throat"], ["परिस्रव", "discharge"],
               ["प्रसेक", "flow"], ["प्रवाहण", "straining"]],
              "The three purgation troubles and two of their emesis counterparts, as the card glosses them.",
              "परिकर्तिका = cutting pain; कण्ठक्षणन = throat injury; परिस्रव = discharge; प्रसेक = flow; प्रवाहण = straining."),
        order(2, "Put these parts of unit 79 in the order of the text.",
              ["या तु विरेचने परिकर्त्तिका", "तद्वमने कंठक्षणनं", "यः परिस्रवः", "स कफप्रसेको", "यत्प्रवाहणं"],
              "Cutting pain, then throat injury; discharge, then flow of Kapha; then straining (paired with dry belching).",
              "परिकर्तिका · कण्ठक्षणन · परिस्रव · कफप्रसेक · प्रवाहण.",
              role="extend",
              teaches="Each pair of unit 79 names the purgation trouble with a relative word (या, यः, यत्) and its emesis form with a correlative (तत्, सः)."),
        match(3, "Match each trouble of purgation to its counterpart in emesis, as unit 79 pairs them.",
              [["परिकर्तिका", "कण्ठक्षणन"], ["परिस्रव", "कफप्रसेक"], ["प्रवाहण", "शुष्क उद्गार"]],
              "Cutting pain ↔ throat injury; discharge ↔ flow of Kapha; straining ↔ dry belching.",
              "Unit 79: three purgation troubles, three emesis counterparts.",
              role="discriminate"),
        mcq("apply", 4,
            "After an emetic, a patient has dry belching (śuṣka-udgāra). Which purgation trouble does unit 79 pair with it?",
            ("Straining (pravāhaṇa)",
             "यत्प्रवाहणं स शुष्कोद्गार: what is straining, that is dry belching."),
            [("Cutting pain (parikartikā)", "Cutting pain is paired with injury of the throat."),
             ("Discharge (parisrava)", "Discharge is paired with the flow of Kapha."),
             ("Distension (ādhmāna)", "Distension is not among the pairs of unit 79.")],
            "Third pair: pravāhaṇa (purgation) = śuṣka-udgāra (emesis).",
            "प्रवाहण ↔ शुष्क उद्गार."),
        mcq("transfer", 5,
            "तत् + वमने gives तद्वमने. Join the invented pair तत् + भोजनम् (that food) the same way. Which is right?",
            ("तद्भोजनम्",
             "त् becomes द् before a voiced consonant: तत् + भोजनम् = तद्भोजनम्."),
            [("तत्भोजनम्", "Before a voiced consonant the त् does not stay voiceless."),
             ("तन्भोजनम्", "त् → न् happens only before a nasal (न, म)."),
             ("तब्भोजनम्", "त् does not take the place of the next consonant here; it only becomes voiced.")],
            "Same rule as तद्वमने.",
            "त् + voiced consonant → द्.",
            teaches="A final त् becomes द् before a voiced consonant (तत् + वमने → तद्वमने; तत् + भोजनम् → तद्भोजनम्)."),
    ],
}

# ---------------------------------------------------------------- unit 80 (prose)
AUTHORED["80"] = {
    "title": "भवंति चात्र",
    "question": "What does the formula भवंति चात्र announce at this point of the chapter?",
    "rule": ("'And on this point there are (the following)': a lead-in formula that turns from the prose of the chapter to the "
             "verses that begin at 05.03.84."),
    "limits": ("The unit names no drug, complication or remedy. The subject of भवन्ति (the verses) is understood, not stated. "
               "The printed भवंति is the anusvāra spelling of भवन्ति."),
    "explain_hi": ("‘भवन्ति चात्र’ = ‘और इस विषय में (ये) हैं’। यह एक परिचय-सूत्र है: अब तक अध्याय गद्य में चल रहा था, और 05.03.84 से "
                   "श्लोक आरम्भ होते हैं। क्या ‘हैं’, यह शब्दों में नहीं कहा; आगे के श्लोक समझे जाते हैं। क्रिया ‘भवन्ति’ बहुवचन है, "
                   "इसलिए आगे एक से अधिक बातें आती हैं। छपा ‘भवंति’ अनुस्वार वाली वर्तनी है।"),
    "hook": "गद्य थमा, ‘भवन्ति’ बहुवचन: अब कई श्लोक।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "In unit 80, what does भवन्ति mean?",
            ("There are",
             "भवन्ति: 3rd person plural present of √भू, there are."),
            [("There was", "The data labels भवन्ति present, not past."),
             ("Let there be", "That would be an imperative (भवन्तु)."),
             ("There will be", "That would be a future (भविष्यन्ति).")],
            "भवन्ति = there are (the following).",
            "भवन्ति = 3 pl. present of √भू."),
        match(1, "Match each word of unit 80 to its meaning.",
              [["भवन्ति", "there are"], ["च", "and"], ["अत्र", "here, on this point"]],
              "The verb, the joining word and the word for 'on this point'.",
              "भवन्ति = there are; च = and; अत्र = here, on this point."),
        order(2, "Put the three words of भवंति चात्र in the order of the text.",
              ["भवंति", "च", "अत्र"],
              "The verb first, then च and अत्र, joined as चात्र.",
              "भवंति · च · अत्र.",
              role="extend",
              teaches="चात्र hides two words: च and अत्र, written together."),
        mcq("discriminate", 3,
            "Which feature of the verb भवन्ति shows that more than one thing follows?",
            ("It is a plural verb",
             "भवन्ति is 3rd person plural: 'there are', so several things (the verses) follow."),
            [("It is a past-tense verb", "The data labels it present tense, and tense says nothing of number."),
             ("It is a passive verb", "भवन्ति is an active present form, not a passive."),
             ("It is an imperative", "It is a present indicative, not an imperative.")],
            "Number, not tense, tells how many: भवन्ति is plural.",
            "भवन्ति = plural: more than one."),
        mcq("apply", 4,
            "Reading on after unit 80, what kind of text does the reader meet next?",
            ("Verses, from 05.03.84",
             "The units after the formula are verses: the first, 05.03.84-85, lists why a medicine fails."),
            [("The colophon of the chapter", "The colophon comes only at 05.03.111."),
             ("A new chapter's opening", "The third chapter has not yet ended."),
             ("More prose drug lists", "The formula turns from prose to verse.")],
            "भवन्ति चात्र introduces the verses that follow the prose.",
            "भवन्ति चात्र → verses."),
        mcq("transfer", 5,
            "च + अत्र gives चात्र. Which is the joined form of the invented pair न + अत्र (not here)?",
            ("नात्र",
             "Short अ + short अ → आ: न + अत्र = नात्र, like च + अत्र = चात्र."),
            [("नत्र", "Two अ do not shrink to one short अ; they give आ."),
             ("नोऽत्र", "ओऽ arises from अः + अ, and न has no visarga."),
             ("नैत्र", "ऐ comes from अ + ए, not from अ + अ.")],
            "Same rule as चात्र.",
            "अ + अ → आ.",
            teaches="Short अ + short अ join as आ (च + अत्र → चात्र; न + अत्र → नात्र)."),
    ],
}

# ---------------------------------------------------------------- unit 81 (verse)
AUTHORED["81"] = {
    "title": "अतिमात्रमकालेऽल्पं",
    "question": "Which six faults does verse 81 say make a medicine surely go wrong?",
    "rule": ("Excessive, at the wrong time, scanty, not soaked (bhāvita) with (ones) of equal potency (vīrya), improperly "
             "prepared, old: the medicine would surely go wrong (fail)."),
    "limits": ("जीर्णम् is rendered 'old' (glossary); 'already digested' is an OPEN alternative (05.03.85): no question on its sense. "
               "अकाले may also be 'out of season'. What the failure leads to is not said in this verse."),
    "explain_hi": ("इस श्लोक में छह कारण गिनाए गए हैं जिनसे औषध ध्रुवम्, यानी निश्चय ही, व्यापन्न होता है, यानी बिगड़ जाता है: अतिमात्र "
                   "(बहुत अधिक मात्रा), अकाल में (गलत समय पर), अल्प (बहुत थोड़ा), समान वीर्य यानी शक्ति वाले द्रव्यों से अभावित (न भिगोया "
                   "हुआ), असम्यक् संस्कृत (ठीक से तैयार न किया हुआ), और जीर्ण यानी पुराना। अतिमात्र और अल्प मात्रा के दो उलटे दोष हैं। "
                   "‘जीर्ण’ का अर्थ ‘पहले ही पचा हुआ’ भी हो सकता है; यह स्वामी के निर्णय पर खुला है।"),
    "hook": "ज़्यादा, बेवक़्त, कम, बिना भावना, ठीक न बना, पुराना: दवा बिगड़ी।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "Which of these is a fault of the medicine named in verse 81?",
            ("Being scanty (अल्पम्)",
             "अल्पम्, scanty, is the third fault of the list."),
            [("Being bitter (तिक्तम्)", "No taste is named among the faults of verse 81."),
             ("Being hot (उष्णम्)", "Heat is not named among the faults of verse 81."),
             ("Being thin (तनु)", "Thinness is not named in verse 81.")],
            "The six faults: excessive, wrong time, scanty, not soaked, improperly prepared, old.",
            "Verse 81: अल्पम् = scanty."),
        match(1, "Match each word of verse 81 to its meaning.",
              [["अतिमात्रम्", "excessive"], ["अकाले", "at the wrong time"], ["अभावितम्", "not soaked"],
               ["असम्यक्संस्कृतम्", "improperly prepared"], ["ध्रुवम्", "surely"]],
              "Four of the faults and the word that makes the failure certain.",
              "अतिमात्रम् = excessive; अकाले = wrong time; अभावितम् = not soaked; असम्यक्संस्कृतम् = improperly prepared; ध्रुवम् = surely."),
        order(2, "Put the six faults of verse 81 in the order of the verse.",
              ["अतिमात्रम्", "अकाले", "अल्पम्", "तुल्यवीर्यैरभावितम्", "असम्यक्संस्कृतम्", "जीर्णम्"],
              "Excessive · wrong time · scanty · not soaked with equal-potency ones · improperly prepared · old.",
              "अतिमात्रम् · अकाले · अल्पम् · …अभावितम् · असम्यक्संस्कृतम् · जीर्णम्.",
              role="extend",
              teaches="Verse 81 lists four faults in line 1 and two in line 2, then gives the verdict व्यापद्येतौषधं ध्रुवम्."),
        mcq("discriminate", 3,
            "Which split of the printed तुल्यवीर्यैरभावितं is right?",
            ("तुल्यवीर्यैः + अभावितम्",
             "ऐः before a vowel becomes ऐर्: तुल्यवीर्यैः + अभावितम् → तुल्यवीर्यैरभावितम्; the fault is 'not soaked'."),
            [("तुल्यवीर्यैः + भावितम्", "That would print तुल्यवीर्यैर्भावितम्, with no अ after र्."),
             ("तुल्यवीर्यै + रभावितम्", "रभावित is no word; the र् is the changed visarga."),
             ("तुल्यवीर्यैर + भावितम्", "तुल्यवीर्यैर is no form; the instrumental plural ends in ऐः.")],
            "The अ after र् is the negative अ-: अ-भावितम्, not soaked.",
            "ऐः + vowel → ऐर्: …वीर्यैरभावितम्."),
        mcq("apply", 4,
            "A medicine was given in the right dose and at the right time, but not soaked with drugs of equal potency. By verse 81, what follows?",
            ("It goes wrong (fails)",
             "Not soaked (अभावितम्) is one of the six faults: व्यापद्येतौषधं ध्रुवम्."),
            [("It works as usual", "Verse 81 says any of the six faults makes it fail."),
             ("It turns into a poison", "Poison is not named in verse 81."),
             ("It must be given twice", "No second dose is named in verse 81.")],
            "Any one of the six faults is enough: the medicine would surely go wrong.",
            "One fault → व्यापद्येत ध्रुवम्."),
        mcq("transfer", 5,
            "अकाले + अल्पम् gives अकालेऽल्पम्. Join the invented pair वने + अस्मिन् (in this forest) the same way. Which is right?",
            ("वनेऽस्मिन्",
             "ए + अ: the ए stays and the अ is dropped, marked by ऽ: वने + अस्मिन् = वनेऽस्मिन्."),
            [("वनास्मिन्", "ए does not turn into आ."),
             ("वनैस्मिन्", "ऐ arises from अ + ए, not from ए + अ."),
             ("वनोऽस्मिन्", "ओऽ arises from अः + अ; here the ending is ए.")],
            "Same rule as अकालेऽल्पम्.",
            "ए + अ → एऽ.",
            teaches="After a final ए a following अ is dropped and marked with an avagraha (अकाले + अल्पम् → अकालेऽल्पम्; वने + अस्मिन् → वनेऽस्मिन्)."),
    ],
}

# ---------------------------------------------------------------- unit 82 (verse)
AUTHORED["82"] = {
    "title": "छर्दनं न तु …",
    "question": "What can be read with confidence in verse 82, a damaged verse on emesis and purgation?",
    "rule": ("Line 1 sets chardana (vomiting, or an emetic) against a damaged word, and durvireca against recana (purging); "
             "line 2: he should make (him) drink the medicine again (bhūyaḥ); it destroys him (or that), 'for indeed they are so'."),
    "limits": ("Low confidence. दुश्छर्द्ं is damaged ('bad vomiting' is a conjecture): no question on it. The sense of line 1 is a "
               "conjecture, and the syntax of line 2 is OPEN (05.03.87): who or what निहन्ति destroys, and who 'they' are, is unknown. "
               "Questions only on clear words and joins."),
    "explain_hi": ("यह श्लोक छपाई में क्षतिग्रस्त है और इसका अर्थ अनिश्चित है। पहली पंक्ति वमन (छर्दन) और विरेचन (रेचन) के दो जोड़े रखती है: "
                   "‘छर्दन नहीं, बल्कि (क्षतिग्रस्त शब्द)’ और ‘दुर्विरेच, रेचन नहीं’। डेटा का अनुमान है कि असफल वमन ‘बुरा वमन’ और "
                   "असफल विरेचन ‘बुरा विरेचन’ बनता है, पर यह केवल अनुमान है। दूसरी पंक्ति: औषध भूयः, यानी फिर, पिलाए; फिर ‘वह उसे "
                   "नष्ट करता है, क्योंकि वे वैसे ही हैं’। कौन किसे नष्ट करता है, यह स्पष्ट नहीं।"),
    "hook": "टूटी पंक्ति: छर्दन-रेचन का जोड़ा, फिर ‘दवा दोबारा पिलाए’।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "In verse 82, what does भूयः mean in पाययेदौषधं भूयः?",
            ("Again",
             "भूयः = again, more."),
            [("Never", "Never would be न कदापि; भूयः is 'again'."),
             ("Slowly", "Slowly would be शनैः."),
             ("At night", "At night would be रात्रौ.")],
            "पाययेत् औषधं भूयः: he should make (him) drink the medicine again.",
            "भूयः = again."),
        match(1, "Match each word of verse 82 to its meaning.",
              [["छर्दन", "vomiting"], ["रेचन", "purging"], ["पाययेत्", "should make (him) drink"],
               ["औषध", "medicine"], ["निहन्ति", "destroys"]],
              "Clear words only; the damaged word of line 1 is left out.",
              "छर्दन = vomiting; रेचन = purging; पाययेत् = should make drink; औषध = medicine; निहन्ति = destroys."),
        order(2, "Put these parts of verse 82 in the order of the verse.",
              ["छर्दनं न तु", "दुर्विरेचं न रेचनं", "पाययेदौषधं", "भूयः", "तं निहंति", "तथा हि ते"],
              "Line 1: chardana, then durvireca and recana; line 2: make drink the medicine, again, it destroys, for they are so.",
              "छर्दनं न तु · दुर्विरेचं न रेचनं · पाययेदौषधं · भूयः · तं निहंति · तथा हि ते.",
              role="extend",
              teaches="Line 1 of verse 82 names the vomiting word first and the purging words second; line 2 opens with the verb पाययेत्."),
        mcq("discriminate", 3,
            "Which split of the printed भूयस्तं is right?",
            ("भूयः + तम्",
             "A visarga before त becomes स्: भूयः + तम् → भूयस्तम्."),
            [("भूय + स्तम्", "स्तम् is no word here; the स् is the changed visarga."),
             ("भूयः + स्तम्", "That would print भूयस्स्तम्, with a double स्."),
             ("भूयो + तम्", "An ओ cannot become स्.")],
            "भूयः (again) + तम् (him, that): ः → स् before त.",
            "ः + त → स्त."),
        mcq("apply", 4,
            "Which two therapies does line 1 of verse 82 set side by side?",
            ("Emesis and purgation",
             "छर्दन (vomiting) and रेचन / दुर्विरेच (purging): the two cleansings of the chapter."),
            [("Basti and sweating", "Neither basti nor sweating is named in verse 82."),
             ("Oiling and fasting", "Neither oiling nor fasting is named in verse 82."),
             ("Nasal drops and gargles", "Neither is named in verse 82.")],
            "chardana belongs to emesis, recana to purgation.",
            "छर्दन ↔ रेचन."),
        mcq("transfer", 5,
            "पाययेत् + औषधम् gives पाययेदौषधम्. Join the invented pair दद्यात् + अन्नम् (he should give food) the same way. Which is right?",
            ("दद्यादन्नम्",
             "A final त् becomes द् before a vowel: दद्यात् + अन्नम् = दद्यादन्नम्."),
            [("दद्यातन्नम्", "Before a vowel the त् does not stay voiceless."),
             ("दद्यानन्नम्", "त् → न् happens only before a nasal."),
             ("दद्याअन्नम्", "The two words are joined; the त् does not simply vanish.")],
            "Same rule as पाययेदौषधम्.",
            "त् + vowel → द्.",
            teaches="A final त् becomes द् before a vowel (पाययेत् + औषधम् → पाययेदौषधम्; दद्यात् + अन्नम् → दद्यादन्नम्)."),
    ],
}

# ---------------------------------------------------------------- unit 83 (verse)
AUTHORED["83"] = {
    "title": "यस्योर्ध्वं कफसंसृष्टं",
    "question": "In verse 83, what is done for one in whom the drunk ānulomika (medicine) goes upward mixed with Kapha?",
    "rule": ("In whom what is drunk, ānulomika (going in the natural direction), goes upward mixed with Kapha: him, made to vomit "
             "with plain (ones), cleansed and made to fast, he should make drink (it)."),
    "limits": ("Low confidence. That 'what is drunk' is the medicine, and that ānulomika means downward for a purgative, are probable, "
               "not stated. What the plain (ones) (केवलैः) are, and the object of पाययेत्, are unstated: no question on them. "
               "The syntax of आनुलोमिकम् is uncertain."),
    "explain_hi": ("जिस रोगी में पिया हुआ, आनुलोमिक यानी स्वाभाविक दिशा में चलने वाला (द्रव्य), कफ से मिलकर ऊपर की ओर चला जाए, उसके "
                   "लिए क्रम दिया गया है: पहले उसे केवलों से वमन कराया गया हो, वह शुद्ध हुआ हो, उसका लंघन यानी उपवास कराया गया हो, "
                   "तब उसे पिलाए। ‘केवल’ से कौन से द्रव्य अभिप्रेत हैं, नहीं बताया। विरेचक के लिए ‘आनुलोमिक’ सम्भवतः नीचे की ओर "
                   "जाना है, पर पंक्ति यह नहीं कहती।"),
    "hook": "दवा कफ के साथ ऊपर आई: वमन, शुद्धि, लंघन, तब पिलाओ।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "In verse 83, with what is the drink (पीतम्) mixed when it goes upward?",
            ("With Kapha",
             "कफसंसृष्टम्: mixed with Kapha."),
            [("With Pitta", "Pitta is not named in verse 83."),
             ("With blood", "Blood is not named in verse 83."),
             ("With Vāta", "Vāta is not named in verse 83.")],
            "Line 1: ऊर्ध्वं कफसंसृष्टं पीतं याति, what is drunk goes upward mixed with Kapha.",
            "कफ-संसृष्ट = mixed with Kapha."),
        match(1, "Match each word of verse 83 to its meaning.",
              [["ऊर्ध्वम्", "upward"], ["संसृष्ट", "mixed"], ["पीत", "drunk"],
               ["वमित", "made to vomit"], ["लङ्घित", "made to fast"]],
              "Three words of line 1 and two of the patient's states in line 2.",
              "ऊर्ध्वम् = upward; संसृष्ट = mixed; पीत = drunk; वमित = made to vomit; लङ्घित = made to fast."),
        order(2, "Put these words of line 2 of verse 83 in the order of the verse.",
              ["वमितं", "शुद्धं", "लंघितं", "पाययेत्"],
              "Made to vomit · cleansed · made to fast · he should make drink.",
              "वमितं · शुद्धं · लंघितं · पाययेत्.",
              role="extend",
              teaches="Three past participles (वमित, शुद्ध, लङ्घित) describe the patient before the verb पाययेत्."),
        mcq("discriminate", 3,
            "Which split of the printed यस्योर्ध्वं is right?",
            ("यस्य + ऊर्ध्वम्",
             "अ + ऊ → ओ: यस्य + ऊर्ध्वम् → यस्योर्ध्वम्."),
            [("यस्यः + ऊर्ध्वम्", "यस्यः is no form; the genitive is यस्य."),
             ("यस्यु + ऊर्ध्वम्", "उ + ऊ would give ऊ, not ओ."),
             ("यस्ये + ऊर्ध्वम्", "ए + ऊ would not give ओ.")],
            "यस्य (in whom, gen.) + ऊर्ध्वम् (upward): अ + ऊ → ओ.",
            "अ + ऊ → ओ."),
        mcq("apply", 4,
            "By verse 83, in what state is the patient before he is made to drink?",
            ("Vomited, cleansed, fasted",
             "वमितं … शुद्धं लंघितं पाययेत्: made to vomit, cleansed and made to fast, then made to drink."),
            [("Oiled, sweated and fed", "No oiling, sweating or feeding is named in verse 83."),
             ("Purged, bathed and rested", "No purging, bathing or rest is named in verse 83."),
             ("Fed, warmed and then oiled", "None of these is named in verse 83.")],
            "Line 2 gives three states of the patient, then the verb.",
            "वमित · शुद्ध · लङ्घित → पाययेत्."),
        mcq("transfer", 5,
            "याति + आनुलोमिकम् gives यात्यानुलोमिकम्. Join the invented pair अस्ति + अत्र (there is here) the same way. Which is right?",
            ("अस्त्यत्र",
             "इ before an unlike vowel becomes य्: अस्ति + अत्र = अस्त्यत्र."),
            [("अस्तेत्र", "ए would come from अ + इ, the other way round."),
             ("अस्तीत्र", "ई would come from इ + इ."),
             ("अस्तित्र", "The अ of अत्र cannot vanish.")],
            "Same rule as यात्यानुलोमिकम्.",
            "इ + unlike vowel → य् + vowel.",
            teaches="A final इ before an unlike vowel becomes य् (याति + आनुलोमिकम् → यात्यानुलोमिकम्; अस्ति + अत्र → अस्त्यत्र)."),
    ],
}

# ---------------------------------------------------------------- unit 84 (verse)
AUTHORED["84"] = {
    "title": "विबद्धेऽल्पे चिराद्दोषे",
    "question": "When does verse 84 order hot water, and which troubles does it say subside by it?",
    "rule": ("When the doṣa is held back, scanty, and flowing after a long time, he should drink hot water; by that, distension "
             "(ādhmāna), vomiting, thirst and obstruction (vibandha) subside."),
    "limits": ("Medium confidence. स्रवति is read as a locative participle with दोषे; 'it flows' is possible. चिरात् may be 'slowly'. "
               "The drinker (the patient) and the amount of water are not stated."),
    "explain_hi": ("जब दोष विबद्ध यानी रुका हुआ हो, अल्प हो और चिरात् यानी देर से बहे, तब गरम जल पिया जाए। उससे चार कष्ट शान्त होते हैं: "
                   "आध्मान यानी पेट फूलना, वमि यानी उलटी, तृष्णा यानी प्यास, और विबन्ध यानी मल और वायु की रुकावट (कब्ज़; मानक)। "
                   "एक ही क्रिया ‘अनुशाम्यति’ पूरी सूची पर लागू है। जल कितना हो, यह नहीं कहा।"),
    "hook": "दोष अटका, थोड़ा, देर से: गरम पानी; अफारा, उलटी, प्यास, कब्ज़ शान्त।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "In verse 84, what is the state of the doṣa when hot water is ordered?",
            ("Held back and scanty",
             "विबद्धेऽल्पे … दोषे: when the doṣa is held back and scanty (and flows after a long time)."),
            [("Flowing out too freely", "Too free a flow is the opposite of विबद्ध, held back."),
             ("Mixed with fresh blood", "Blood is not named in verse 84."),
             ("Moved up to the head", "No movement to the head is named in verse 84.")],
            "Three locatives describe the doṣa: held back, scanty, flowing after a long time.",
            "विबद्ध + अल्प + चिरात् स्रवत् → उष्ण जल."),
        match(1, "Match each word of verse 84 to its meaning.",
              [["विबद्ध", "held back"], ["अल्प", "scanty"], ["आध्मान", "distension"],
               ["तृष्णा", "thirst"], ["अनुशाम्यति", "subsides"]],
              "Two states of the doṣa, two of the troubles and the verb that ends the verse.",
              "विबद्ध = held back; अल्प = scanty; आध्मान = distension; तृष्णा = thirst; अनुशाम्यति = subsides."),
        order(2, "Put the four troubles that subside in verse 84 in the order of the verse.",
              ["आध्मानं", "वमिः", "तृष्णा", "विबंधः"],
              "Distension · vomiting · thirst · obstruction.",
              "आध्मानं · वमिः · तृष्णा · विबन्धः.",
              role="extend",
              teaches="Line 2 of verse 84 lists four troubles under one singular verb, अनुशाम्यति."),
        multi("discriminate", 3,
              "Which of these does verse 84 say subside by the hot water?",
              [("Distension (आध्मान)", "Right: आध्मानम् is the first trouble named."),
               ("Thirst (तृष्णा)", "Right: तृष्णा is the third trouble named."),
               ("Fainting (मूर्च्छा)", "Not named in verse 84."),
               ("Fever (ज्वर)", "Not named in verse 84."),
               ("Burning (दाह)", "Not named in verse 84.")],
              [0, 1],
              "The four that subside: ādhmāna, vomiting, thirst, vibandha.",
              "Verse 84: आध्मान, वमि, तृष्णा, विबन्ध."),
        mcq("apply", 4,
            "After a purgative a patient has bloating and thirst; the doṣa comes scanty and late. Which measure of verse 84 fits?",
            ("Drinking hot water",
             "उष्णं पिबेज्जलं: he should drink hot water; by that distension and thirst subside."),
            [("Drinking cold water", "Verse 84 orders hot (उष्ण) water, not cold."),
             ("A basti of milk", "No basti is named in verse 84."),
             ("Fasting for a day", "Fasting is not named in verse 84.")],
            "Scanty, held-back doṣa → hot water → the troubles subside.",
            "Verse 84: उष्णं जलं पिबेत्."),
        mcq("transfer", 5,
            "पिबेत् + जलम् gives पिबेज्जलम्. Join the invented pair तत् + जलम् (that water) the same way. Which is right?",
            ("तज्जलम्",
             "A final त् before ज becomes ज्: तत् + जलम् = तज्जलम्."),
            [("तद्जलम्", "Before ज the त् does not stop at द्; it becomes ज्."),
             ("तच्जलम्", "च् arises before च/छ, not before ज."),
             ("तन्जलम्", "त् → न् happens only before a nasal.")],
            "Same rule as पिबेज्जलम्.",
            "त् + ज → ज्ज.",
            teaches="A final त् becomes ज् before ज (पिबेत् + जलम् → पिबेज्जलम्; तत् + जलम् → तज्जलम्)."),
    ],
}

# ---------------------------------------------------------------- unit 85 (verse)
AUTHORED["85"] = {
    "title": "भेषजं दोषरुद्धं चेत्",
    "question": "What does verse 85 order when the medicine, obstructed by a doṣa, moves neither up nor down?",
    "rule": ("If the medicine, obstructed by a doṣa, proceeds neither upward nor downward, then, with belching or with pain in the "
             "limbs, he should apply sweating (sveda)."),
    "limits": ("The adjectives सोद्गारम्, साङ्गशूलम् agree with an unstated noun (the medicine or the condition). Which doṣa obstructs "
               "is not named, nor how the sweating is done. The rendering of अवचारयेत् ('should apply') is OPEN in the glossary."),
    "explain_hi": ("यदि दोष से रुकी हुई औषध न ऊपर जाए, न नीचे, और साथ में उद्गार यानी डकार हो या अंगों में शूल हो, तो वहाँ स्वेद, यानी "
                   "पसीना लाने वाला उपचार, प्रयोग करे। ‘चेत्’ (यदि) शर्त वाली पंक्ति खोलता है और ‘तत्र’ (वहाँ) उपाय वाली। कौन-सा दोष "
                   "रोकता है और स्वेद किस विधि से हो, यह नहीं बताया।"),
    "hook": "दवा न ऊपर न नीचे, डकार या अंग-दर्द: स्वेद दो।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "In verse 85, what treatment is ordered for the medicine that moves neither up nor down?",
            ("Sweating (sveda)",
             "स्वेदं तत्रावचारयेत्: in that case he should apply sweating."),
            [("Fasting (laṅghana)", "Fasting is not named in verse 85."),
             ("Oiling (sneha)", "Oiling is not named in verse 85."),
             ("Emesis (vamana)", "No emetic is ordered in verse 85.")],
            "The single remedy of verse 85 is स्वेद.",
            "Verse 85: स्वेदम् अवचारयेत्."),
        match(1, "Match each word of verse 85 to its meaning.",
              [["दोषरुद्ध", "obstructed by a doṣa"], ["ऊर्ध्वम्", "upward"], ["अधः", "downward"],
               ["उद्गार", "belching"], ["अङ्गशूल", "pain in the limbs"]],
              "The state of the medicine, its two blocked ways and the two signs.",
              "दोषरुद्ध = obstructed by doṣa; ऊर्ध्वम् = upward; अधः = downward; उद्गार = belching; अङ्गशूल = limb pain."),
        order(2, "Put the four quarter-lines of verse 85 in the order of the verse.",
              ["भेषजं दोषरुद्धं चेत्", "नोर्ध्वं नाधः प्रवर्त्तते", "सोद्गारं सांगशूलं वा", "स्वेदं तत्रावचारयेत्"],
              "The condition (two quarters), the signs, the remedy.",
              "भेषजं … चेत् · नोर्ध्वं नाधः … · सोद्गारं … वा · स्वेदं …",
              role="extend",
              teaches="Verse 85 runs: if-clause (चेत्), the blocked ways, the signs, and the remedy (तत्र … अवचारयेत्)."),
        mcq("discriminate", 3,
            "Which split of the printed चेन्नोर्ध्वं is right?",
            ("चेत् + न + ऊर्ध्वम्",
             "त् → न् before the nasal न; अ + ऊ → ओ: चेत् + न + ऊर्ध्वम् → चेन्नोर्ध्वम्."),
            [("चे + नोर्ध्वम्", "चे and नोर्ध्वम् are no words."),
             ("चेन् + नु + ऊर्ध्वम्", "नु + ऊर्ध्वम् would print नूर्ध्वम्, not नोर्ध्वम्."),
             ("चेत् + नौ + ऊर्ध्वम्", "नौ + ऊर्ध्वम् would print नावूर्ध्वम्.")],
            "चेत् (if) + न (not) + ऊर्ध्वम् (upward).",
            "त् + न → न्न; अ + ऊ → ओ."),
        mcq("apply", 4,
            "The medicine stays put, neither vomited nor purged, and the patient belches. By verse 85, which measure fits?",
            ("Applying sweating",
             "With belching (सोद्गारम्) when the medicine moves neither way: स्वेदम् अवचारयेत्."),
            [("Giving cold water", "Cold water is not named in verse 85."),
             ("Making him fast", "Fasting is not named in verse 85."),
             ("Giving a sharper drug", "No sharper drug is named in verse 85.")],
            "Blocked medicine with belching or limb pain → sweating.",
            "सोद्गारं साङ्गशूलं वा → स्वेद."),
        mcq("transfer", 5,
            "स + अङ्गशूलम् gives साङ्गशूलम्. Join the invented pair स + आमम् (with āma) the same way. Which is right?",
            ("सामम्",
             "अ + आ → आ: स + आमम् = सामम्, like स + अङ्ग → साङ्ग."),
            [("समम्", "The long आ of आमम् cannot shrink to अ."),
             ("सैमम्", "ऐ arises from अ + ए, not from अ + आ."),
             ("सोमम्", "ओ arises from अ + उ, not from अ + आ.")],
            "Like vowels join long: अ + अ or अ + आ → आ.",
            "अ + आ → आ.",
            teaches="अ before अ or आ joins as आ (स + अङ्गशूलम् → साङ्गशूलम्; स + आमम् → सामम्)."),
    ],
}

# ---------------------------------------------------------------- unit 86 (verse)
AUTHORED["86"] = {
    "title": "सम्यग्विरिक्तसोद्गारभेषजं",
    "question": "What does verse 86 tell the physician to do quickly, and what to do with very cold (ones)?",
    "rule": ("The medicine of (one) properly purged and with belching he should quickly scrape up (ullikhet); but when (it is) "
             "undigested and does not set in motion, the physician should check (it) with very cold (ones)."),
    "limits": ("Low confidence. How the long compound of line 1 is built is uncertain: no question on it. The method of scraping up, "
               "what is checked, and what the very cold (ones) are, are not stated."),
    "explain_hi": ("यह श्लोक दो आदेश देता है, पर पहली पंक्ति का लम्बा समास (सम्यग्विरिक्त-सोद्गार-भेषज) कैसे जुड़ता है, यह अनिश्चित है। "
                   "डेटा का पाठ: जो भली-भाँति विरेचित है और डकार ले रहा है, उसकी औषध को क्षिप्रम्, यानी शीघ्र, उल्लिखेत्, यानी खुरचकर "
                   "ऊपर निकाले; विधि नहीं बताई। दूसरी पंक्ति: (औषध) न पची हो और प्रवृत्त न हो, तो वैद्य बहुत ठण्डे द्रव्यों से स्तम्भित करे, "
                   "यानी रोके। किसे रोका जाए, यह स्पष्ट नहीं।"),
    "hook": "डकार के साथ अटकी दवा: जल्दी निकालो; न चली: बहुत ठंडे से थामो।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "In verse 86, how soon should the medicine be scraped up (उल्लिखेत्)?",
            ("Quickly (क्षिप्रम्)",
             "क्षिप्रमुल्लिखेत्: he should quickly scrape (it) up."),
            [("Slowly (शनैः)", "शनैः is not in verse 86; the word is क्षिप्रम्."),
             ("At night (रात्रौ)", "No time of day is named in verse 86."),
             ("Next day (श्वः)", "No later day is named in verse 86.")],
            "क्षिप्रम् = quickly.",
            "Verse 86: क्षिप्रम् उल्लिखेत्."),
        match(1, "Match each word of verse 86 to its meaning.",
              [["क्षिप्रम्", "quickly"], ["उल्लिखेत्", "should scrape up"], ["सुशीत", "very cold"],
               ["स्तम्भयेत्", "should check"], ["भिषक्", "physician"]],
              "Clear words of both lines; the long compound is left out.",
              "क्षिप्रम् = quickly; उल्लिखेत् = should scrape up; सुशीत = very cold; स्तम्भयेत् = should check; भिषक् = physician."),
        order(2, "Put these parts of verse 86 in the order of the verse.",
              ["सम्यग्विरिक्तसोद्गारभेषजं", "क्षिप्रमुल्लिखेत्", "अजीर्णमप्रवृत्तौ तु", "सुशीतैः", "स्तंभयेद्भिषक्"],
              "Line 1: the compound, then 'quickly scrape up'; line 2: the condition, 'with very cold (ones)', the verb and the physician.",
              "…भेषजं · क्षिप्रमुल्लिखेत् · अजीर्णमप्रवृत्तौ तु · सुशीतैः · स्तंभयेद्भिषक्.",
              role="extend",
              teaches="Each line of verse 86 ends in its own optative: उल्लिखेत् in line 1, स्तम्भयेत् in line 2."),
        mcq("discriminate", 3,
            "Which split of the printed स्तंभयेद्भिषक् is right?",
            ("स्तंभयेत् + भिषक्",
             "त् becomes द् before a voiced consonant: स्तंभयेत् + भिषक् → स्तंभयेद्भिषक्."),
            [("स्तंभये + द्भिषक्", "द्भिषक् is no word; the द् is the verb's changed त्."),
             ("स्तंभयः + भिषक्", "अः before भ would become ओ: स्तंभयो भिषक्."),
             ("स्तंभयेत् + अभिषक्", "That would print स्तंभयेदभिषक्, with अ after द्.")],
            "स्तम्भयेत् (should check) + भिषक् (the physician).",
            "त् + voiced consonant → द्."),
        mcq("apply", 4,
            "In verse 86, when (it is) undigested and does not set in motion, with what does the physician check?",
            ("Very cold ones",
             "सुशीतैः स्तंभयेद्भिषक्: the physician should check with very cold (ones)."),
            [("Very hot ones", "Verse 86 says सुशीतैः, very cold, not hot."),
             ("Sharp ones", "Sharpness is not named in verse 86."),
             ("Oily ones", "Oiliness is not named in verse 86.")],
            "Line 2: सुशीतैः, with very cold (ones), what they are is unstated.",
            "Verse 86: सुशीतैः स्तम्भयेत्."),
        mcq("transfer", 5,
            "क्षिप्रम् + उल्लिखेत् gives क्षिप्रमुल्लिखेत्. Join the invented pair जलम् + उष्णम् (the water, hot) the same way. Which is right?",
            ("जलमुष्णम्",
             "A final म् before a vowel is simply joined to it: जलम् + उष्णम् = जलमुष्णम्."),
            [("जलंउष्णम्", "The anusvāra is written before a consonant, not before a vowel."),
             ("जलोष्णम्", "The म् cannot drop to let अ + उ join as ओ."),
             ("जलमोष्णम्", "No ओ arises; म् + उ is just मु.")],
            "Same join as क्षिप्रमुल्लिखेत्.",
            "Final म् + vowel → म + vowel.",
            teaches="A final म् before a vowel joins it as a syllable (क्षिप्रम् + उल्लिखेत् → क्षिप्रमुल्लिखेत्; जलम् + उष्णम् → जलमुष्णम्)."),
    ],
}

# ---------------------------------------------------------------- unit 87 (verse)
AUTHORED["87"] = {
    "title": "कदाचिच्छ्लेष्मणा रुद्धं",
    "question": "Where, according to verse 87, does the medicine sometimes stay, and when does it move on?",
    "rule": ("Sometimes the medicine, obstructed by Kapha (śleṣman), stays in the chest; when Kapha has diminished, in the evening "
             "or at night, it moves on."),
    "limits": ("The printed सायान्हे is flagged (सायाह्ने, letters transposed): no question on that word. No remedy is given here; "
               "'it' in line 2 is the medicine, unstated."),
    "explain_hi": ("कभी-कभी (कदाचित्) औषध श्लेष्मा यानी कफ से रुककर उरस् यानी छाती में ठहरा रहता है। जब कफ क्षीण होता है, सायंकाल या "
                   "रात्रि में, तब वह प्रवृत्त होता है, यानी आगे चल पड़ता है। इस श्लोक में कोई उपाय नहीं, केवल यह बात कि रुकावट कफ के "
                   "घटने पर खुलती है। छपा ‘सायान्हे’ अक्षरों के उलट-पलट से बना लगता है; शुद्ध रूप ‘सायाह्ने’।"),
    "hook": "कफ ने छाती में दवा रोकी; कफ घटा, शाम-रात को दवा चली।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "In verse 87, where does the medicine stay when Kapha obstructs it?",
            ("In the chest (उरसि)",
             "तिष्ठत्युरसि भेषजं: the medicine stays in the chest."),
            [("In the head (शिरसि)", "The head is not named in verse 87."),
             ("In the belly (उदरे)", "The belly is not named in verse 87."),
             ("In the throat (कण्ठे)", "The throat is not named in verse 87.")],
            "उरसि = in the chest (locative of उरस्).",
            "Verse 87: तिष्ठति उरसि."),
        match(1, "Match each word of verse 87 to its meaning.",
              [["कदाचित्", "sometimes"], ["श्लेष्मन्", "Kapha"], ["रुद्ध", "obstructed"],
               ["उरस्", "chest"], ["क्षीण", "diminished"]],
              "Five clear words of the two lines.",
              "कदाचित् = sometimes; श्लेष्मन् = Kapha; रुद्ध = obstructed; उरस् = chest; क्षीण = diminished."),
        order(2, "Put these parts of verse 87 in the order of the verse.",
              ["कदाचिच्छ्लेष्मणा रुद्धं", "तिष्ठत्युरसि भेषजं", "क्षीणे श्लेष्मणि", "रात्रौ वा", "तत्प्रवर्त्तते"],
              "Obstructed by Kapha · stays in the chest · when Kapha is diminished · or at night · it moves on.",
              "कदाचिच्छ्लेष्मणा रुद्धं · तिष्ठत्युरसि भेषजं · क्षीणे श्लेष्मणि · रात्रौ वा · तत्प्रवर्त्तते.",
              role="extend",
              teaches="Line 1 of verse 87 gives the blockage, line 2 the release: Kapha diminished, then the medicine moves."),
        mcq("discriminate", 3,
            "Which split of the printed कदाचिच्छ्लेष्मणा is right?",
            ("कदाचित् + श्लेष्मणा",
             "त् + श → च्छ: कदाचित् + श्लेष्मणा → कदाचिच्छ्लेष्मणा."),
            [("कदाचि + च्छ्लेष्मणा", "कदाचि and च्छ्लेष्मणा are no words."),
             ("कदाचित् + छ्लेष्मणा", "छ्लेष्मन् is no word; the word is श्लेष्मन्."),
             ("कदाचिः + श्लेष्मणा", "कदाचिः is no form; the word is कदाचित्.")],
            "कदाचित् (sometimes) + श्लेष्मणा (by Kapha): त् before श gives च्छ.",
            "त् + श → च्छ."),
        mcq("apply", 4,
            "By verse 87, on what does the medicine's moving on depend?",
            ("Kapha becoming less",
             "क्षीणे श्लेष्मणि … तत्प्रवर्त्तते: when Kapha has diminished, it moves on."),
            [("Vāta becoming strong", "Vāta is not named in verse 87."),
             ("A fresh dose being given", "No new dose is named in verse 87."),
             ("Hot water being drunk", "Hot water is not named in verse 87.")],
            "Kapha blocks it; Kapha's diminishing releases it.",
            "क्षीणे श्लेष्मणि → प्रवर्तते."),
        mcq("transfer", 5,
            "तत् + प्रवर्त्तते gives तत्प्रवर्त्तते, unchanged. Join the invented pair तत् + पिबेत् (he should drink that) the same way. Which is right?",
            ("तत्पिबेत्",
             "Before a voiceless consonant such as प the final त् stays as it is: तत् + पिबेत् = तत्पिबेत्."),
            [("तद्पिबेत्", "त् → द् happens before voiced sounds, not before प."),
             ("तप्पिबेत्", "त् does not take the form of प."),
             ("तन्पिबेत्", "त् → न् happens only before a nasal.")],
            "Same as तत्प्रवर्त्तते: no change before a voiceless consonant.",
            "त् + voiceless consonant → त् unchanged.",
            teaches="A final त् stays unchanged before a voiceless consonant (तत् + प्रवर्तते → तत्प्रवर्तते; तत् + पिबेत् → तत्पिबेत्)."),
    ],
}

# ---------------------------------------------------------------- unit 88 (verse)
AUTHORED["88"] = {
    "title": "रूक्षान्नाहारयेज्जीर्णे …",
    "question": "What does verse 88 order in its first line, and what when the medicine is held by Vāyu?",
    "rule": ("When (it is) digested, staying, or even gone upward, he should feed dry food; but when the medicine (is held) by Vāyu "
             "(wind), he should drink another (one), with fat (sneha) and salt."),
    "limits": ("Low confidence. Two flags: रूक्षान्न… (an accusative -म् seems lost) and सनेहलवणं (स-स्नेह expected); जीर्णे ('digested' "
               "here, 'old' possible) is OPEN (05.03.98): no questions on these. The subject of the three locatives and the participle "
               "with वायुना (probably 'held') are unstated."),
    "explain_hi": ("यह श्लोक दो स्थितियाँ रखता है, पर इसकी वाक्य-रचना अनिश्चित है। पहली पंक्ति: (औषध या कफ के) जीर्ण यानी पच जाने पर, ठहरे "
                   "रहने पर, या ऊपर चले जाने पर भी, रूक्ष अन्न खिलाया जाए। दूसरी पंक्ति, ‘तु’ (किन्तु) से: यदि औषध वायु से (रुका) हो, "
                   "तो स्नेह और लवण सहित दूसरा (पेय) पिया जाए। ‘रुका’ शब्द पंक्ति में नहीं; सम्भवतः 05.03.96 से समझा जाता है। "
                   "‘जीर्णे’ का अर्थ ‘पुराना’ भी सम्भव है, और ‘सनेह’ छपाई में संदिग्ध है।"),
    "hook": "पचा, ठहरा या ऊपर गया: रूखा अन्न; वायु ने रोका: स्नेह-लवण वाला दूसरा पेय।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "In verse 88, by which doṣa is the medicine (held) in the second line?",
            ("Vāyu (वायुना)",
             "वायुना भेषजे: when the medicine (is held) by Vāyu, wind."),
            [("Kapha (श्लेष्मणा)", "Kapha is the obstructer of 05.03.96, not of this line."),
             ("Pitta (पित्तेन)", "Pitta is not named in verse 88."),
             ("Blood (रक्तेन)", "Blood is not named in verse 88.")],
            "Line 2: वायुना (instrumental), by Vāyu.",
            "वायुना = by Vāyu."),
        match(1, "Match each word of verse 88 to its meaning.",
              [["तिष्ठति", "staying"], ["ऊर्ध्वगत", "gone upward"], ["वायुना", "by Vāyu"],
               ["भेषज", "medicine"], ["पिबेत्", "should drink"]],
              "Clear words only; the flagged words are left out.",
              "तिष्ठति = staying; ऊर्ध्वगत = gone upward; वायुना = by Vāyu; भेषज = medicine; पिबेत् = should drink."),
        order(2, "Put these words of verse 88 in the order of the verse.",
              ["तिष्ठति", "ऊर्ध्वगते", "अपि वा", "वायुना", "भेषजे", "पिबेत्"],
              "Staying · gone upward · or even · by Vāyu · in the medicine · should drink.",
              "तिष्ठति · ऊर्ध्वगते · अपि वा · वायुना · भेषजे · पिबेत्.",
              role="extend",
              teaches="Line 1 of verse 88 gives the states of the unstated subject; line 2 turns to the case of Vāyu and ends in पिबेत्."),
        mcq("discriminate", 3,
            "Which split of the printed तिष्ठत्यूर्ध्वगते is right?",
            ("तिष्ठति + ऊर्ध्वगते",
             "इ before an unlike vowel becomes य्: तिष्ठति + ऊर्ध्वगते → तिष्ठत्यूर्ध्वगते."),
            [("तिष्ठत्य + ऊर्ध्वगते", "तिष्ठत्य is no form."),
             ("तिष्ठते + ऊर्ध्वगते", "ए + ऊ would not give यू."),
             ("तिष्ठत् + यूर्ध्वगते", "यूर्ध्वगत is no word.")],
            "तिष्ठति (staying) + ऊर्ध्वगते (gone upward): इ + ऊ → यू.",
            "इ + unlike vowel → य्."),
        mcq("apply", 4,
            "In verse 88, which word marks the turn to the second, different case?",
            ("तु (but)",
             "वायुना भेषजे त्वन्यत्…: तु, but, sets the Vāyu case against line 1."),
            [("वा (or)", "वा joins the states of line 1; it does not turn to a new case."),
             ("अपि (even)", "अपि only adds 'gone upward' to the list of line 1."),
             ("अन्यत् (another)", "अन्यत् names the other drink, not the turn.")],
            "तु opens the contrast: but when (held) by Vāyu …",
            "तु = but (contrast)."),
        mcq("transfer", 5,
            "तु + अन्यत् gives त्वन्यत्. Join the invented pair मधु + अस्ति (there is honey) the same way. Which is right?",
            ("मध्वस्ति",
             "उ before an unlike vowel becomes व्: मधु + अस्ति = मध्वस्ति."),
            [("मधोस्ति", "ओ would come from अ + उ, the other way round."),
             ("मधूस्ति", "ऊ would come from उ + उ."),
             ("मधवस्ति", "अव् comes from ओ before a vowel, not from उ.")],
            "Same rule as त्वन्यत्.",
            "उ + unlike vowel → व् + vowel.",
            teaches="A final उ before an unlike vowel becomes व् (तु + अन्यत् → त्वन्यत्; मधु + अस्ति → मध्वस्ति)."),
    ],
}


NOTES_HI = {
    "77": ("विश्वास: मध्यम। text_flag: छपा ‘चा’ = च + असम्यक् का अ (चासम्यक्); केवल रिक्त स्थान गलत जगह छपा। विकल्प च + सम्यक् "
           "(‘ठीक से दिए गए’) के लिए छपा आ भूल मानना पड़ेगा; इस पर प्रश्न नहीं। बस्तिव्यापत्सिद्धि सम्भवतः उस नाम का अध्याय। छपा ‘वस्ति’ "
           "बस्ति माना गया। संधि जाँची: शेषेष्वपि = शेषेषु + अपि (उ → व्); दोषानपेक्ष्य = दोषान् + अपेक्ष्य; प्रतिकुर्याद्वस्ति = "
           "प्रतिकुर्यात् + वस्ति (त् → द् घोष से पहले); चेक्षेत = च + ईक्षेत (अ + ई → ए)।"),
    "78": ("विश्वास: मध्यम। उभयतोभाग = दोनों भागों वाला; ऊपर-नीचे दोनों मार्गों का शोधन सम्भावित, पंक्ति नहीं कहती। उत्तिष्ठेत् शाब्दिक "
           "‘उठ खड़ा हो’; अभिप्राय (कार्य में लगे) नहीं कहा, इस पर प्रश्न नहीं। संधि जाँची: एवमुभयतो = एवम् + उभयतः; उभयतोभागे = "
           "उभयतः + भागे (अः → ओ घोष से पहले); भागेऽपि = भागे + अपि (ए + अ → एऽ); यथावस्थमुत्तिष्ठेत् = यथावस्थम् + उत्तिष्ठेत्।"),
    "79": ("विश्वास: उच्च। text_flag: ‘शुष्कोद्गारइति’ में इति से पहले रिक्त स्थान छूटा (केवल छपाई); इति वाक्य समाप्त करता है। छपा "
           "‘परिकर्त्तिका’ में दोहरा त्त छपाई का है (परिकर्तिका)। संबंध-सर्वनाम अपने संज्ञा का लिंग लेते हैं: या परिकर्तिका (स्त्री.) / तत् "
           "कण्ठक्षणनम् (नपुं.); यः परिस्रवः / सः कफप्रसेकः; यत् प्रवाहणम् / सः शुष्कोद्गारः। संधि जाँची: तद्वमने = तत् + वमने "
           "(त् → द्); कफप्रसेको यत् = कफप्रसेकः + यत् (अः → ओ घोष से पहले); शुष्कोद्गार = शुष्क + उद्गार (अ + उ → ओ)।"),
    "80": ("विश्वास: उच्च। परिचय-सूत्र; ‘भवन्ति’ का कर्ता (आगे के श्लोक) शब्दों में नहीं। छपा ‘भवंति’ = भवन्ति (अनुस्वार वर्तनी)। "
           "संधि जाँची: चात्र = च + अत्र (अ + अ → आ)।"),
    "81": ("विश्वास: उच्च। दो पंक्तियाँ (05.03.84, 05.03.85)। खुला बिन्दु: जीर्ण = ‘पुराना’ (शब्द-सूची) या ‘पहले ही पचा हुआ’; स्वामी का "
           "निर्णय, इस पर प्रश्न नहीं। अकाले = ‘गलत समय पर’ या ‘ऋतु के बाहर’। भावित = भिगोया हुआ (शब्द-सूची)। डेटा का हिन्दी "
           "‘वीर्य यानी सामर्थ्य’ लिखता है, शब्द-सूची ‘वीर्य यानी शक्ति’ कहती है। संधि जाँची: अतिमात्रमकाले = अतिमात्रम् + अकाले; "
           "अकालेऽल्पं = अकाले + अल्पम् (ए + अ → एऽ); तुल्यवीर्यैरभावितं = तुल्यवीर्यैः + अभावितम् (ऐः → ऐर् स्वर से पहले); "
           "व्यापद्येतौषधं = व्यापद्येत + औषधम् (अ + औ → औ)।"),
    "82": ("विश्वास: निम्न। text_flag: ‘दुश्छर्द्ं’ क्षतिग्रस्त (र्द के बाद स्वर-चिह्न नहीं); ‘दुश्छर्दम्’ अपेक्षित, अर्थ ‘बुरा वमन’ केवल अनुमान। "
           "खुला बिन्दु (05.03.86): ‘दुर्विरेचम् … रेचनम्’ के समानान्तर से ‘दुश्छर्दनम्’ भी सम्भव। खुला बिन्दु (05.03.87): ‘तं निहन्ति तथा हि ते’ "
           "की वाक्य-रचना अनिर्णीत: तम् = रोगी या बचा दोष, ‘ते’ कौन, अज्ञात। इन पर प्रश्न नहीं। छर्दन/रेचन = वमन/विरेचन, या वमनकारक/"
           "रेचक द्रव्य। संधि जाँची: पाययेदौषधं = पाययेत् + औषधम् (त् → द् स्वर से पहले); भूयस्तं = भूयः + तम् (ः → स् त से पहले)।"),
    "83": ("विश्वास: निम्न। दो पंक्तियाँ (05.03.88, 05.03.89)। ‘पीतम्’ = पिया हुआ (औषध, अकथित)। आनुलोमिक = स्वाभाविक दिशा में चलने वाला; "
           "विरेचक के लिए नीचे की ओर, सम्भावित; ‘ऊपर जाता है’ के साथ इसका मेल अटपटा है, वाक्य-रचना अनिश्चित। ‘केवलैः’ = केवल (द्रव्यों) से, "
           "कौन-से नहीं बताया; पाययेत् का कर्म अकथित। संधि जाँची: यस्योर्ध्वं = यस्य + ऊर्ध्वम् (अ + ऊ → ओ); यात्यानुलोमिकं = याति + "
           "आनुलोमिकम् (इ → य्); पाययेत्तु = पाययेत् + तु।"),
    "84": ("विश्वास: मध्यम। स्रवति को ‘दोषे’ से मेल खाता सप्तमी कृदन्त पढ़ा; ‘बहता है’ (क्रिया) भी सम्भव। चिरात् = ‘देर से’ या ‘धीरे’। "
           "पीने वाला (रोगी) अकथित। आध्मान = पेट फूलना (मानक, नपुंसक); विबन्ध = मल और वायु की रुकावट, कब्ज़ (मानक)। संधि जाँची: "
           "विबद्धेऽल्पे = विबद्धे + अल्पे (ए + अ → एऽ); चिराद्दोषे = चिरात् + दोषे (त् → द्); स्रवत्युष्णं = स्रवति + उष्णम् (इ → य्); "
           "पिबेज्जलं = पिबेत् + जलम् (त् → ज् ज से पहले); तेनाध्मानं = तेन + आध्मानम्; वमिस्तृष्णा = वमिः + तृष्णा (ः → स्); "
           "विबंधश्चानुशाम्यति = विबन्धः + च + अनुशाम्यति (ः → श् च से पहले)।"),
    "85": ("विश्वास: मध्यम। सोद्गारम्, साङ्गशूलम् नपुंसक द्वितीया, किसी अकथित संज्ञा (औषध या अवस्था) के विशेषण। ‘अवचारयेत्’ का अनुवाद "
           "‘प्रयोग करे’ शब्द-सूची में खुला। छपा ‘प्रवर्त्तते’ = प्रवर्तते। संधि जाँची: चेन्नोर्ध्वं = चेत् + न + ऊर्ध्वम् (त् → न् न से पहले; "
           "अ + ऊ → ओ); नाधः = न + अधः; सोद्गारं = स + उद्गारम् (अ + उ → ओ); सांगशूलं = स + अङ्गशूलम् (अ + अ → आ); "
           "तत्रावचारयेत् = तत्र + अवचारयेत्।"),
    "86": ("विश्वास: निम्न। ‘सम्यग्विरिक्तसोद्गारभेषजं’ की रचना अनिश्चित: ‘भली-भाँति विरेचित, डकार वाले (की) औषध’ पढ़ा गया; इस पर प्रश्न "
           "नहीं। उल्लिखेत् = खुरचकर निकाले, विधि अकथित। ‘अजीर्ण’ = न पचा। किसे रोका जाए और ‘सुशीत’ द्रव्य कौन, अकथित। संधि जाँची: "
           "सम्यग्विरिक्त = सम्यक् + विरिक्त (क् → ग् घोष से पहले); क्षिप्रमुल्लिखेत् = क्षिप्रम् + उल्लिखेत्; अजीर्णमप्रवृत्तौ = अजीर्णम् + "
           "अप्रवृत्तौ; स्तंभयेद्भिषक् = स्तम्भयेत् + भिषक् (त् → द् घोष से पहले)।"),
    "87": ("विश्वास: उच्च। text_flag: छपा ‘सायान्हे’ में अक्षर उलटे (शुद्ध ‘सायाह्ने’); इस शब्द पर प्रश्न नहीं। दूसरी पंक्ति का ‘तत्’ = औषध। "
           "डेटा का हिन्दी पहले वाक्य में औषध को स्त्रीलिंग (रुकी हुई … ठहरी) और दूसरे में पुंलिंग (वह प्रवृत्त होता है) लेता है। "
           "छपा ‘प्रवर्त्तते’ = प्रवर्तते। संधि जाँची: कदाचिच्छ्लेष्मणा = कदाचित् + श्लेष्मणा (त् + श → च्छ); तिष्ठत्युरसि = तिष्ठति + "
           "उरसि (इ → य्); तत्प्रवर्त्तते = तत् + प्रवर्तते (अघोष से पहले त् अपरिवर्तित)।"),
    "88": ("विश्वास: निम्न। text_flag 1: ‘रूक्षान्नाहारयेज्जीर्णे’ में ‘रूक्षान्नम्’ का म् लुप्त लगता है (छन्द के कारण संदिग्ध; रूक्षान्न + "
           "आहारयेत् भी सम्भव)। text_flag 2: ‘सनेहलवणं’ में ‘ससनेह/सस्नेह’ अपेक्षित, या ‘स्नेहलवणम्’ के साथ एक फालतू अ। खुला बिन्दु "
           "(05.03.98): जीर्णे = ‘पचा’ या ‘पुराना’। इन तीनों पर प्रश्न नहीं। तीन सप्तमी (जीर्णे, तिष्ठति, ऊर्ध्वगते) का कर्ता अकथित; ‘वायुना’ के "
           "साथ कृदन्त (सम्भवतः रुद्ध) पंक्ति में नहीं। संधि जाँची: तिष्ठत्यूर्ध्वगते = तिष्ठति + ऊर्ध्वगते (इ → य्); ऊर्ध्वगते ऽपि = "
           "ऊर्ध्वगते + अपि (ए + अ → एऽ, छपा रिक्त स्थान छपाई का); त्वन्यत् = तु + अन्यत् (उ → व्)।"),
}


AIDS = {
    "77": {
        "chain": {"steps": ["शेष उपद्रव (वमन-विरेचन के)", "रोग के अनुसार", "दोषों का विचार करके", "प्रतिकार",
                            "बस्तिव्यापत्सिद्धि भी देखे"]},
        "sandhi": "अ + ई → ए: च + ईक्षेत → चेक्षेत; त् → द् घोष से पहले: प्रतिकुर्यात् + वस्ति → प्रतिकुर्याद्वस्ति।",
        "anchors": "शेष = बचा हुआ · उपद्रव = उलझन, उपद्रव · यथामयम् = रोग के अनुसार · अपेक्ष्य = ध्यान में रखकर · ईक्षेत = देखे।",
    },
    "78": {
        "frame": "‘एवम् … अपि’ = ‘इसी प्रकार … भी’: पिछला नियम दोनों भागों वाले शोधन पर भी लागू।",
        "sandhi": "अः → ओ घोष से पहले: उभयतः + भागे → उभयतोभागे; ए + अ → एऽ: भागे + अपि → भागेऽपि।",
        "anchors": "उभयतः = दोनों ओर · भाग = भाग, अंश · शोधन = शुद्धि · यथावस्थम् = अवस्था के अनुसार · उत्तिष्ठेत् = उठ खड़ा हो।",
    },
    "79": {
        "contrast": {"groups": [{"label": "विरेचन में", "items": ["परिकर्तिका (काटने की पीड़ा)", "परिस्रव (स्राव)",
                                                              "प्रवाहण (ज़ोर लगाना)"]},
                                {"label": "वमन में", "items": ["कण्ठक्षणन (गले की क्षति)", "कफप्रसेक (कफ का बहना)",
                                                           "शुष्क उद्गार (सूखी डकार)"]}]},
        "frame": "‘जो … वह …’: या … तत्, यः … सः, यत् … सः — हर जोड़े में पहला विरेचन का, दूसरा वमन का।",
        "pegs": "मेरा बनाया चित्र: नीचे का रास्ता कटता है तो ऊपर गला छिलता है; नीचे रिसता है तो ऊपर कफ बहता है; नीचे ज़ोर लगता है तो ऊपर सूखी डकार।",
        "sandhi": "त् → द्: तत् + वमने → तद्वमने; अ + उ → ओ: शुष्क + उद्गार → शुष्कोद्गार।",
    },
    "80": {
        "frame": "‘भवन्ति चात्र’ = और इस विषय में (ये) हैं: गद्य के बाद श्लोकों का द्वार।",
        "sandhi": "अ + अ → आ: च + अत्र → चात्र।",
        "anchors": "भवन्ति = हैं (बहुवचन) · च = और · अत्र = यहाँ, इस विषय में।",
    },
    "81": {
        "diagram": {"groups": [{"label": "औषध बिगड़ता है जब वह", "items": ["अतिमात्र", "अकाल में", "अल्प",
                                                                         "तुल्य वीर्य से अभावित", "असम्यक् संस्कृत", "जीर्ण"]}]},
        "seesaw": "अतिमात्रम् (बहुत अधिक) ↔ अल्पम् (बहुत थोड़ा): दोनों उलटे मात्रा-दोष, दोनों से औषध बिगड़ता है।",
        "chunks": {"steps": ["अतिमात्रमकालेऽल्पं", "तुल्यवीर्यैरभावितं", "असम्यक्संस्कृतं जीर्णं", "व्यापद्येतौषधं ध्रुवं"]},
        "sandhi": "ऐः → ऐर् स्वर से पहले: तुल्यवीर्यैः + अभावितम् → तुल्यवीर्यैरभावितम् (यहाँ ‘अ’ निषेध है: अ-भावित)।",
    },
    "82": {
        "chunks": {"steps": ["छर्दनं न तु …", "दुर्विरेचं न रेचनं", "पाययेदौषधं भूयः", "तं निहंति तथा हि ते"]},
        "sandhi": "ः → स् त से पहले: भूयः + तम् → भूयस्तम्; त् → द् स्वर से पहले: पाययेत् + औषधम् → पाययेदौषधम्।",
        "anchors": "छर्दन = वमन · रेचन = विरेचन · भूयः = फिर · निहन्ति = नष्ट करता है।",
    },
    "83": {
        "chain": {"steps": ["पिया हुआ, कफ से मिलकर ऊपर गया", "केवलों से वमन कराया", "शुद्ध हुआ", "लंघन कराया",
                            "तब पिलाए"]},
        "sandhi": "अ + ऊ → ओ: यस्य + ऊर्ध्वम् → यस्योर्ध्वम्; इ → य्: याति + आनुलोमिकम् → यात्यानुलोमिकम्।",
        "anchors": "संसृष्ट = मिला हुआ · आनुलोमिक = स्वाभाविक दिशा वाला · वमित = वमन कराया · लङ्घित = उपवास कराया।",
    },
    "84": {
        "chain": {"steps": ["दोष रुका, अल्प, देर से बहता", "गरम जल पिए", "आध्मान, वमि, तृष्णा, विबन्ध शान्त"]},
        "sandhi": "त् → ज् ज से पहले: पिबेत् + जलम् → पिबेज्जलम्; ः → श् च से पहले: विबन्धः + च → विबन्धश्च।",
        "anchors": "विबद्ध = रुका · चिरात् = देर से · आध्मान = पेट फूलना · विबन्ध = कब्ज़ · अनुशाम्यति = शान्त होता है।",
    },
    "85": {
        "chain": {"steps": ["दोष से रुकी औषध", "न ऊपर, न नीचे", "डकार या अंगों में शूल", "स्वेद प्रयोग करे"]},
        "frame": "‘चेत्’ (यदि) से शर्त, ‘तत्र’ (वहाँ) से उपाय।",
        "sandhi": "त् → न् न से पहले, अ + ऊ → ओ: चेत् + न + ऊर्ध्वम् → चेन्नोर्ध्वम्; अ + उ → ओ: स + उद्गारम् → सोद्गारम्।",
    },
    "86": {
        "chunks": {"steps": ["सम्यग्विरिक्तसोद्गारभेषजं", "क्षिप्रमुल्लिखेत्", "अजीर्णमप्रवृत्तौ तु", "सुशीतैः स्तंभयेद्भिषक्"]},
        "sandhi": "त् → द् घोष से पहले: स्तम्भयेत् + भिषक् → स्तम्भयेद्भिषक्; म् + स्वर: क्षिप्रम् + उल्लिखेत् → क्षिप्रमुल्लिखेत्।",
        "anchors": "क्षिप्रम् = शीघ्र · उल्लिखेत् = खुरचकर निकाले · सुशीत = बहुत ठण्डा · स्तम्भयेत् = रोके · भिषक् = वैद्य।",
    },
    "87": {
        "chain": {"steps": ["कफ से रुकी औषध", "छाती में ठहरी", "कफ क्षीण हुआ", "सायंकाल या रात्रि", "औषध प्रवृत्त"]},
        "seesaw": "रुद्ध, तिष्ठति (रुका, ठहरा) ↔ प्रवर्तते (चल पड़ा): बीच की कड़ी है ‘क्षीणे श्लेष्मणि’।",
        "sandhi": "त् + श → च्छ: कदाचित् + श्लेष्मणा → कदाचिच्छ्लेष्मणा; इ → य्: तिष्ठति + उरसि → तिष्ठत्युरसि।",
        "anchors": "कदाचित् = कभी-कभी · श्लेष्मन् = कफ · उरस् = छाती · क्षीण = घटा हुआ · प्रवर्तते = चल पड़ता है।",
    },
    "88": {
        "contrast": "पहली पंक्ति: पचा, ठहरा या ऊपर गया → रूक्ष अन्न ↔ दूसरी पंक्ति (तु): वायु से (रुका) औषध → स्नेह-लवण सहित दूसरा पेय।",
        "sandhi": "इ → य्: तिष्ठति + ऊर्ध्वगते → तिष्ठत्यूर्ध्वगते; उ → व्: तु + अन्यत् → त्वन्यत्।",
        "anchors": "तिष्ठति = ठहरा · ऊर्ध्वगत = ऊपर गया · वायुना = वायु से · अन्यत् = दूसरा · पिबेत् = पिए।",
    },
}


IMAGE_SPECS = {
    ("77", "chain"): {
        "file": "ka3-shesha-upadrava-77.svg",
        "alt": "Flowchart of unit 77: the remaining complications of emesis and purgation are countered according to the disease, having regard to the doshas, and the basti-vyapat-siddhi is also consulted",
        "type": "mermaid",
        "code": ('flowchart TD\n  A["वमन-विरेचन के<br/>शेष उपद्रव"] --> B["रोग के अनुसार"]\n'
                 '  B --> C["दोषों का विचार"]\n  C --> D["प्रतिकार"]\n'
                 '  A --> E["बस्तिव्यापत्सिद्धि<br/>भी देखे"]\n'),
    },
    ("79", "contrast"): {
        "file": "ka3-vamana-virecana-pairs-79.svg",
        "alt": "Table of the three pairs of unit 79: cutting pain in purgation is throat injury in emesis; discharge is flow of Kapha; straining is dry belching",
        "type": "table",
        "title": "इकाई ७९: विरेचन ↔ वमन",
        "heads": ["विरेचन में", "वमन में"],
        "rows": [["परिकर्तिका (काटने की पीड़ा)", "कण्ठक्षणन (गले की क्षति)"],
                 ["परिस्रव (स्राव)", "कफप्रसेक (कफ का बहना)"],
                 ["प्रवाहण (ज़ोर लगाना)", "शुष्क उद्गार (सूखी डकार)"]],
    },
    ("81", "diagram"): {
        "file": "ka3-aushadha-fails-81.svg",
        "alt": "Mind map of the six faults of verse 81 that make a medicine go wrong: excessive, at the wrong time, scanty, not soaked with ones of equal potency, improperly prepared, old",
        "type": "mermaid",
        "code": ('mindmap\n  औषध बिगड़ता है\n    अतिमात्र\n    अकाल में\n    अल्प\n'
                 '    तुल्य वीर्य से अभावित\n    असम्यक् संस्कृत\n    जीर्ण\n'),
    },
    ("83", "chain"): {
        "file": "ka3-redrink-83.svg",
        "alt": "Flowchart of verse 83: what is drunk goes upward mixed with Kapha; the patient is made to vomit with plain ones, is cleansed, is made to fast, then is made to drink",
        "type": "mermaid",
        "code": ('flowchart TD\n  A["पिया हुआ कफ से<br/>मिलकर ऊपर गया"] --> B["केवलों से वमन"]\n'
                 '  B --> C["शुद्ध हुआ"]\n  C --> D["लंघन"]\n  D --> E["तब पिलाए"]\n'),
    },
    ("84", "chain"): {
        "file": "ka3-hot-water-84.svg",
        "alt": "Flowchart of verse 84: when the dosha is held back, scanty and flows after a long time, hot water is drunk; distension, vomiting, thirst and obstruction subside",
        "type": "mermaid",
        "code": ('flowchart TD\n  A["दोष रुका, अल्प,<br/>देर से बहता"] --> B["गरम जल पिए"]\n'
                 '  B --> C["आध्मान शान्त"]\n  B --> D["वमि शान्त"]\n  B --> E["तृष्णा शान्त"]\n'
                 '  B --> F["विबन्ध शान्त"]\n'),
    },
    ("85", "chain"): {
        "file": "ka3-sveda-85.svg",
        "alt": "Flowchart of verse 85: a medicine obstructed by a dosha moves neither up nor down; with belching or pain in the limbs, sweating is applied",
        "type": "mermaid",
        "code": ('flowchart TD\n  A["दोष से रुकी औषध"] --> B["न ऊपर, न नीचे"]\n'
                 '  B --> C["डकार"]\n  B --> D["या अंगों में शूल"]\n  C --> E["स्वेद"]\n  D --> E\n'),
    },
    ("87", "chain"): {
        "file": "ka3-kapha-chest-87.svg",
        "alt": "Flowchart of verse 87: medicine obstructed by Kapha stays in the chest; when Kapha has diminished, in the evening or at night, it moves on",
        "type": "mermaid",
        "code": ('flowchart TD\n  A["कफ से रुकी औषध"] --> B["छाती में ठहरी"]\n'
                 '  B --> C["कफ क्षीण हुआ"]\n  C --> D["सायंकाल या रात्रि में"]\n  D --> E["औषध चल पड़ी"]\n'),
    },
}
