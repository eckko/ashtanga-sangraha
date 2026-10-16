from helpers import mcq, match, order, fill, multi, accepts


def T(q, teaches):
    """Add a `teaches` line to a question that has no such parameter."""
    q["teaches"] = teaches
    return q


AUTHORED = {}

# ---------------------------------------------------------------- unit 14
AUTHORED["14"] = {
    "title": "ताभ्यामतः सुयुक्ताभ्यां",
    "question": "What does the physician who treats with the two well applied avoid, and how is the one who goes to a patient described?",
    "rule": ("Treating with the two (named just before) well applied, he does "
             "not err. A relative clause begins: he who goes only when "
             "called, well dressed, on good omens."),
    "limits": ("The sentence runs across units: the relative clause (यो याति) "
               "is completed only in later units. The two things meant by "
               "ताभ्याम् are named before this unit and are not tested here."),
    "explain_hi": ("यह वाक्य पिछली इकाई से चला आ रहा है: ‘ताभ्याम्’ का अर्थ है "
                   "‘इन दोनों से’ (जिन दो का नाम ठीक पहले आया है), और "
                   "‘सुयुक्ताभ्याम्’ का अर्थ है भली-भाँति प्रयोग किए हुए। इन "
                   "दोनों के भली-भाँति प्रयोग से चिकित्सा करने वाला भूल नहीं "
                   "करता। दूसरी पंक्ति ‘यो याति’ से एक सम्बन्ध-वाक्य शुरू करती "
                   "है: जो बुलाए जाने पर ही जाता है, सुन्दर वेश में और शुभ "
                   "निमित्तों के साथ। यह वाक्य यहाँ पूरा नहीं होता; ‘जो … वह’ "
                   "का दूसरा भाग आगे की इकाइयों में आता है।"),
    "hook": "दो का भली-भाँति प्रयोग → भूल नहीं; जो जाता है: बुलाने पर ही · सुवेश · शुभ निमित्त (वाक्य आगे चलता है)।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "The verse says that a physician who treats with the two well applied does what?",
            ("He does not err",
             "चिकित्सन्नापराध्यति: न अपराध्यति, he does not err."),
            [("He avoids all patients", "The verse says he treats (चिकित्सन्); it does not say he avoids patients."),
             ("He charges a fee", "No fee is mentioned in the verse."),
             ("He leaves it to others", "He is the one treating (चिकित्सन्), not one who hands over.")],
            "ताभ्यां सुयुक्ताभ्यां चिकित्सन् न अपराध्यति: treating with the two well applied, he does not err.",
            "Well-applied pair + treating: he does not err."),
        match(1, "Match each word of the verse to its meaning.",
              [["अपराध्यति", "errs"], ["आहूतः", "called"],
               ["सुवेषः", "well dressed"], ["सुनिमित्ततः", "on good omens"]],
              "These four words carry the verse: the verb of line 1 and the three marks of the one who goes in line 2.",
              "अपराध्यति = errs; आहूतः = called; सुवेषः = well dressed; सुनिमित्ततः = on good omens."),
        T(order(2, "Arrange these phrases of line 2 in the verse's order.",
                ["आहूतएव", "यो याति", "सुवेषः", "सुनिमित्ततः"],
                "Line 2 reads: आहूतएव यो याति, सुवेषः सुनिमित्ततः.",
                "He goes only when called, well dressed, on good omens.", role="extend"),
          "A relative clause (यः …) can open with its condition first (आहूतएव) and put its verb (याति) after it."),
        mcq("discriminate", 3, "Which is the right split of चिकित्सन्नापराध्यति?",
            ("चिकित्सन् + न + अपराध्यति",
             "न + अ gives ना (अ + अ → आ), so न + अपराध्यति is written नापराध्यति."),
            [("चिकित्सन् + ना + अपराध्यति", "ना is not the negative word here; the negative is न."),
             ("चिकित्सत् + न + अपराध्यति", "The participle in the data is चिकित्सन्, ending in न्."),
             ("चिकित्सन्न + आपराध्यति", "आपराध्यति is not a word; the verb is अपराध्यति.")],
            "The participle चिकित्सन् ends in न्; then comes the negative न, and its अ joins the अ of अपराध्यति to make ना.",
            "न + अपराध्यति → नापराध्यति (अ + अ → आ)."),
        multi("apply", 4, "Which of these does the verse say about the one who goes?",
              [("He goes only when called", "Right: आहूतएव."),
               ("He is well dressed", "Right: सुवेषः."),
               ("He goes on good omens", "Right: सुनिमित्ततः."),
               ("He carries medicines with him", "Nothing is said of carrying anything."),
               ("He goes at night", "The time of going is not mentioned.")],
              [0, 1, 2],
              "The three marks are: called, well dressed, on good omens. Nothing is said of medicines or night.",
              "Marks of the one who goes: called, well dressed, good omens."),
        mcq("transfer", 5,
            "An invented line says आहूत एव शिष्यो गच्छति. What does it say?",
            ("The pupil goes only when called",
             "एव after आहूतः limits the going to when he is called, as in the verse."),
            [("The pupil goes though he is not called", "एव means 'only'; it excludes going uncalled."),
             ("The pupil calls everyone and goes", "आहूतः is 'called', a passive sense, not 'calls'."),
             ("The pupil is called but never goes", "गच्छति says he goes.")],
            "आहूतः + एव → आहूत एव (the visarga is lost before एव); एव fixes the condition: only when called.",
            "आहूत एव + verb = does it only when called.",
            teaches="आहूतः (called) with एव (only) makes a condition: he acts only when called."),
    ],
}

# ---------------------------------------------------------------- unit 15
AUTHORED["15"] = {
    "title": "गत्वा ऽऽतुरार्थादन्यत्र",
    "question": "What does the physician do after going to the patient, and what does he not do?",
    "rule": ("Having gone, he sets his mind nowhere other than on the "
             "patient's concern, and he examines the diseases properly, by "
             "the particulars beginning with the cause (nidāna)."),
    "limits": ("Continues the relative clause (यो याति). The printed कचित् "
               "is a flagged slip for क्वचित् and no question rests on it. "
               "The verse says only 'beginning with nidāna', not the full list."),
    "explain_hi": ("यह पिछले सम्बन्ध-वाक्य (‘जो जाता है…’) की अगली कड़ी है। वहाँ "
                   "जाकर वह रोगी के प्रयोजन को छोड़कर कहीं और मन नहीं लगाता। "
                   "दूसरी पंक्ति में वह रोगों की भली-भाँति परीक्षा करता है, और "
                   "यह परीक्षा ‘निदान आदि विशेष बातों’ से होती है; सूची का "
                   "नाम यहाँ केवल ‘निदान से आरम्भ’ है, पूरी सूची श्लोक में नहीं "
                   "है। ‘गत्वा’ एक पूर्वकालिक रूप है: जाकर।"),
    "hook": "जाकर: मन केवल रोगी के काम में · रोगों की परीक्षा निदान आदि से।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "After going to the patient, the physician of this verse sets his mind where?",
            ("Only on the patient's concern",
             "न निधत्ते मनः आतुरार्थात् अन्यत्र: he puts his mind nowhere other than the patient's concern."),
            [("On his own fee", "No fee is mentioned."),
             ("On the king's court", "The king is not in this verse."),
             ("On whatever is nearby", "The verse says nowhere else (अन्यत्र न).")],
            "आतुरार्थात् अन्यत्र न: nowhere other than on the patient's concern.",
            "Mind only on the patient's concern."),
        match(1, "Match each word of the verse to its meaning.",
              [["गत्वा", "having gone"], ["मनः", "mind"],
               ["व्याधीन्", "diseases"], ["परीक्षते", "examines"]],
              "Two words from each line: the going and the mind in line 1, the diseases and their examination in line 2.",
              "गत्वा = having gone; मनः = mind; व्याधीन् = diseases; परीक्षते = examines."),
        fill(2, "The word for 'mind' in line 1 is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("मनः"),
             "मनः is the neuter accusative of मनस्, mind: न निधत्ते मनः, he does not place his mind.",
             "मनः is the thing placed (object of निधत्ते); the verse says it is placed nowhere else than on the patient's concern.",
             "मनः = mind."),
        mcq("discriminate", 3, "Which is the right split of सम्यग्निदानादिविशेषतः?",
            ("सम्यक् + निदान + आदि + विशेषतः",
             "Final क् becomes ग् before the voiced न, and निदान + आदि joins as निदानादि."),
            [("सम्यः + निदान + आदि + विशेषतः", "सम्यः is not a word; the adverb is सम्यक्."),
             ("सम्यक् + निदानादि + शेषतः", "The last word is विशेषतः, by the particulars, not शेषतः."),
             ("सम् + यग्निदान + आदि + विशेषतः", "यग्निदान is not a word.")],
            "सम्यक् (properly) + निदान-आदि (beginning with the cause) + विशेषतः (by the particulars).",
            "Final क् → ग् before a voiced consonant: सम्यक् + निदान → सम्यग्निदान."),
        multi("apply", 4, "Which of these does the verse say the physician does after going?",
              [("He puts his mind nowhere but on the patient's concern", "Right: line 1."),
               ("He examines the diseases properly", "Right: line 2, परीक्षते सम्यक्."),
               ("He examines them by the particulars beginning with the cause", "Right: निदानादिविशेषतः."),
               ("He takes a gift", "Taking a gift is a separate rule, in a different unit."),
               ("He praises his own skill", "Nothing of the kind is said.")],
              [0, 1, 2],
              "The unit has two statements: the mind kept on the patient's concern, and the proper examination of the diseases by the cause and the rest.",
              "After going: mind on the concern; proper examination of the diseases."),
        mcq("transfer", 5,
            "An invented line says भुक्त्वा शिष्यः पठति. What does it say?",
            ("Having eaten, the pupil studies",
             "भुक्त्वा is the 'having done' form, like गत्वा: the eating comes first."),
            [("The pupil studies, then he eats", "The भुक्त्वा form puts eating first."),
             ("The pupil studies while eating", "The form does not say both go on together."),
             ("The pupil will eat after studying", "That would reverse the order.")],
            "A word in -त्वा, like गत्वा and भुक्त्वा, names an earlier action by the same doer.",
            "-त्वा form = having done, before the main verb.",
            teaches="A -त्वा word (गत्वा, भुक्त्वा) means 'having done', an action before the main verb by the same doer."),
    ],
}

# ---------------------------------------------------------------- unit 16
AUTHORED["16"] = {
    "title": "गोपनीयां च तद्वार्त्तां",
    "question": "What does the physician not do with the patient's secret report?",
    "rule": ("He does not make the patient's report, which is to be kept "
             "secret, known outside. Line 2 adds that he does not rashly "
             "let the time of treatment slip."),
    "limits": ("Confidence is medium. Line 2 is hard: तस्याऽपि could be "
               "'of him also' or 'of it also'; no question rests on those "
               "words. Continues the relative clause (यो याति)."),
    "explain_hi": ("पहली पंक्ति स्पष्ट है: रोगी का गोपनीय समाचार (‘वार्त्ता’) वह "
                   "बाहर प्रकट नहीं करता। ‘गोपनीयाम्’ और ‘वार्त्ताम्’ दोनों "
                   "स्त्रीलिंग द्वितीया एकवचन हैं, इसलिए पहला शब्द दूसरे को "
                   "विशेषित करता है: जो रखने योग्य है। दूसरी पंक्ति कठिन है: "
                   "भाव यह है कि वह अचानक या बिना सोचे चिकित्सा का समय निकलने "
                   "नहीं देता (‘क्रियाकालम् अहापयन्’)। ‘तस्याऽपि’ दो तरह "
                   "पढ़ा जा सकता है, इसलिए इस पर प्रश्न नहीं रखा गया है।"),
    "hook": "गोपनीय बात बाहर नहीं · चिकित्सा का समय हाथ से नहीं जाने देता (पंक्ति २ कठिन)।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "What does the physician not make known outside?",
            ("The patient's report that is to be kept secret",
             "गोपनीयां तद्वार्त्तां न प्रकाशयते बहिः: he does not make it known outside."),
            [("The medicines he uses", "No medicines are mentioned in line 1."),
             ("The fee he has agreed", "No fee is mentioned."),
             ("The name of his teacher", "No teacher is mentioned.")],
            "The object is तद्वार्त्ताम्, his (the patient's) report, qualified by गोपनीयाम्, to be kept secret.",
            "He does not reveal the patient's secret report."),
        order(1, "Arrange these phrases of line 1 in the verse's order.",
              ["गोपनीयां च", "तद्वार्त्तां", "न प्रकाशयते", "बहिः"],
              "Line 1 reads: गोपनीयां च तद्वार्त्तां न प्रकाशयते बहिः.",
              "To be kept secret + his report + does not make known + outside."),
        T(match(2, "Match each word of the verse to its meaning.",
                [["गोपनीयाम्", "to be kept secret"], ["वार्त्ताम्", "report"],
                 ["प्रकाशयते", "makes known"], ["बहिः", "outside"]],
                "These four words make up line 1 apart from the particles.",
                "गोपनीयाम् = to be kept secret; वार्त्ताम् = report; प्रकाशयते = makes known; बहिः = outside.",
                role="extend"),
          "A word in -अनीय (गोपनीय) is a gerundive: it means 'to be done', here 'to be kept (secret)'."),
        mcq("discriminate", 3, "Which word does गोपनीयाम् describe?",
            ("वार्त्ताम्",
             "Both are feminine accusative singular, so they agree: the report to be kept secret."),
            [("प्रकाशयते", "That is a verb; an adjective does not describe a verb."),
             ("बहिः", "बहिः is an indeclinable word, 'outside'; it has no case to agree with."),
             ("क्रियाकालम्", "That is masculine, in line 2; गोपनीयाम् is feminine.")],
            "Agreement of gender, number and case: गोपनीयाम् and वार्त्ताम् are both feminine, accusative, singular.",
            "An adjective agrees with its noun in gender, number and case."),
        multi("apply", 4, "Which of these does the verse say about the physician?",
              [("He does not make the secret report known outside", "Right: line 1."),
               ("The report he keeps back is called गोपनीय", "Right: गोपनीयां … तद्वार्त्ताम्."),
               ("He does not rashly let the time of treatment slip", "Right: the sense of line 2 (the finer reading is uncertain)."),
               ("He tells the king the report", "Nothing like this is said."),
               ("He writes the report down", "Nothing about writing is said.")],
              [0, 1, 2],
              "Line 1 keeps the secret; line 2, read plainly, does not let the time of treatment pass.",
              "Secret kept; treatment time not rashly lost."),
        mcq("transfer", 5,
            "An invented phrase says श्रवणीया कथा. What does it mean?",
            ("A story to be heard",
             "श्रवणीय is a gerundive of √श्रु, 'to be heard', and कथा is feminine like it."),
            [("A story that has been heard", "Past sense would need a different ending (श्रुत)."),
             ("A story that hears", "The gerundive is passive in sense; the story is what is heard."),
             ("A hearer of stories", "श्रवणीया is an adjective of कथा, not a person.")],
            "-अनीय gives 'to be …' (गोपनीय = to be kept; श्रवणीय = to be heard).",
            "-अनीय = to be done.",
            teaches="A gerundive in -अनीय (गोपनीय, श्रवणीय) means 'to be done' and agrees with its noun."),
    ],
}

# ---------------------------------------------------------------- unit 17
AUTHORED["17"] = {
    "title": "जानाति चोपचरितुं स वैद्यः",
    "question": "Who attains success, and what should the physician not take?",
    "rule": ("The long sentence ends: that physician, who knows how to "
             "treat, attains success. A new rule: he should not take a gift "
             "from women when their master is turned away."),
    "limits": ("Line 1 closes the sentence begun at यो याति; line 2 is a "
               "new rule. 'तदध्यक्षे पराङ्मुखे' is read as 'their master "
               "being turned away'; whether he is absent or unwilling is not "
               "fixed, so no question rests on it."),
    "explain_hi": ("पहली पंक्ति उस लम्बे वाक्य का उत्तर-भाग है जो ‘यो याति’ से शुरू "
                   "हुआ था: ‘वह वैद्य जो उपचार करना जानता है, सिद्धि पाता है’। "
                   "दूसरी पंक्ति नया नियम है: स्त्रियों से कोई ‘आमिष’ (भेंट) "
                   "न ले, जब उनका स्वामी (संरक्षक) विमुख हो। ‘विमुख’ का भाव "
                   "अनुपस्थित भी हो सकता है और अनिच्छुक भी; श्लोक इसे तय नहीं "
                   "करता। ‘नाददीतामिषम्’ में न + आददीत + आमिषम् का जुड़ाव है: "
                   "दोनों बार अ + आ → आ।"),
    "hook": "उपचार जानने वाला वैद्य → सिद्धि · स्त्रियों से भेंट न ले (स्वामी विमुख हो तब)।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Who, according to line 1, attains success (सिद्धि)?",
            ("The physician who knows how to treat",
             "जानाति चोपचरितुं स वैद्यः सिद्धिमश्नुते: he who knows to treat attains success."),
            [("The physician who is wealthy", "Wealth is not mentioned."),
             ("The physician who is famous", "Fame is not mentioned."),
             ("The physician who is old", "Age is not mentioned.")],
            "जानाति उपचरितुम्: he knows how to treat; such a physician attains siddhi.",
            "Knows how to treat → attains success."),
        match(1, "Match each word of the verse to its meaning.",
              [["सिद्धिम्", "success"], ["अश्नुते", "attains"],
               ["जानाति", "knows"], ["आमिषम्", "gift"]],
              "Three words of line 1 and the object of the new rule in line 2.",
              "सिद्धिम् = success; अश्नुते = attains; जानाति = knows; आमिषम् = gift."),
        T(order(2, "Arrange these phrases of line 1 in the verse's order.",
                ["जानाति", "चोपचरितुं", "स वैद्यः", "सिद्धिमश्नुते"],
                "Line 1 reads: जानाति चोपचरितुं स वैद्यः सिद्धिमश्नुते.",
                "Knows + to treat + that physician + attains success.", role="extend"),
          "सः (that) picks up the earlier यः (who): the relative clause ends with 'that physician …'."),
        mcq("discriminate", 3, "Which is the right split of नाददीतामिषं?",
            ("न + आददीत + आमिषम्",
             "न + आ gives ना, and आददीत + आमिषम् joins as आददीतामिषम्: अ + आ → आ each time."),
            [("ना + ददीत + आमिषम्", "The negative is न; ना here is न + the first आ of आददीत."),
             ("न + आददी + तामिषम्", "तामिषम् is not a word."),
             ("नाद + दीत + आमिषम्", "Neither नाद nor दीत is a word of this verse.")],
            "न (not) + आददीत (should take) + आमिषम् (gift).",
            "अ + आ → आ: न + आददीत → नाददीत."),
        multi("apply", 4, "Which of these does the verse say?",
              [("The physician who knows how to treat attains success", "Right: line 1."),
               ("He should not take a gift from women", "Right: line 2."),
               ("The rule is about when their master is turned away", "Right: तदध्यक्षे पराङ्मुखे."),
               ("He should take gifts openly from women", "The verse says न आददीत, he should not take."),
               ("Success comes from wealth", "The verse ties success to knowing how to treat.")],
              [0, 1, 2],
              "Line 1 gives success to the one who knows how to treat; line 2 forbids taking a gift from women when their master is turned away.",
              "Success: knows to treat. Rule: no gift from women (master turned away)."),
        mcq("transfer", 5,
            "An invented line says नाचरेत् पापम्. What does it say?",
            ("One should not do evil",
             "आचरेत् is an optative, 'should do'; न + आचरेत् gives नाचरेत्."),
            [("One did not do evil", "The optative ending -एत् is 'should', not past."),
             ("One should do evil", "The negative न is in the word."),
             ("Evil does not come", "पापम् is the object of आचरेत्; evil is not the subject.")],
            "-एत् is the optative ('should'), as in नाददीत; न + आ → ना.",
            "Optative = should; न + आ → ना.",
            teaches="The optative (-एत्, -ईत) means 'should'; with न it forbids, and न + आ- joins as ना-."),
    ],
}

# ---------------------------------------------------------------- unit 18
AUTHORED["18"] = {
    "title": "नारीभिश्च रहसि स्थानं",
    "question": "What should the physician avoid with women, and what patient does line 2 begin to list?",
    "rule": ("He should avoid staying with women in private and joking with "
             "them. Line 2 begins a list of patients (a patient hated by the "
             "king and good physicians, and others), which the next unit "
             "continues."),
    "limits": ("Confidence is medium. In line 2, तद्वेषिणं is flagged "
               "(probably तद्द्वेषिणं 'hating them') and द्विषम् may mean the "
               "physician's or the king's enemy; no question rests on these. "
               "The verb वर्जयेत् of line 1 is understood to govern the list."),
    "explain_hi": ("पहली पंक्ति में नियम सीधा है: स्त्रियों के साथ एकान्त में रहना "
                   "और परिहास (हँसी-मज़ाक) वह छोड़े (‘वर्जयेत्’)। दूसरी पंक्ति "
                   "से रोगियों की एक सूची शुरू होती है, जिसमें ‘वर्जयेत्’ ही "
                   "क्रिया समझी जाती है: जो रोगी राजा और सज्जन वैद्यों से "
                   "द्वेष-पात्र है, उनसे द्वेष रखता है, या शत्रु है; सूची अगली "
                   "इकाई में चलती है। ‘तद्वेषिणम्’ पर पाठ-शंका है, इसलिए उसे "
                   "प्रश्न में नहीं रखा। ‘नृपसद्वैद्यैः’ में तृतीया बहुवचन "
                   "‘द्वारा’ का भाव देता है: राजा और सज्जन वैद्यों द्वारा।"),
    "hook": "स्त्रियों के साथ एकान्त-वास और परिहास छोड़े · फिर छोड़े जाने वाले रोगियों की सूची शुरू।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "In line 1, with women, what does the verse tell the physician to avoid?",
            ("Staying in private, and joking",
             "नारीभिः रहसि स्थानं परिहासं च वर्जयेत्: avoid staying in private with women and joking."),
            [("Speaking, and writing", "Neither speech nor writing is named."),
             ("Treating them, and visiting them", "Treating women is not forbidden in the verse."),
             ("Eating, and sleeping", "Neither is named.")],
            "वर्जयेत् takes two objects: स्थानम् (staying) in private, and परिहासम् (joking), both with women.",
            "Avoid private company and joking with women."),
        match(1, "Match each word of the verse to its meaning.",
              [["नारीभिः", "with women"], ["रहसि", "in private"],
               ["स्थानम्", "staying"], ["परिहासम्", "joking"]],
              "The four content words of line 1.",
              "नारीभिः = with women; रहसि = in private; स्थानम् = staying; परिहासम् = joking."),
        T(order(2, "Arrange these phrases of line 1 in the verse's order.",
                ["नारीभिश्च", "रहसि", "स्थानं", "परिहासं च", "वर्जयेत्"],
                "Line 1 reads: नारीभिश्च रहसि स्थानं परिहासं च वर्जयेत्.",
                "With women + in private + staying + joking + should avoid.", role="extend"),
          "The verb वर्जयेत् comes last and governs both objects, and, in this text, the accusatives of line 2 as well."),
        mcq("discriminate", 3, "Which is the right split of नृपसद्वैद्यैर्द्विष्टं?",
            ("नृप + सत् + वैद्यैः + द्विष्टम्",
             "सत् becomes सद् before the voiced व, and वैद्यैः becomes वैद्यैर् before the voiced द्वि."),
            [("नृपस + द्वैद्यैः + द्विष्टम्", "द्वैद्यैः is not a word."),
             ("नृपसद् + वैद्यः + द्विष्टम्", "The ending is -ऐः (plural 'by'), not the singular वैद्यः."),
             ("नृप + सत् + वैद्यैः + विष्टम्", "The participle is द्विष्टम्, hated; विष्टम् would lose the द्.")],
            "नृप + सत् + वैद्यैः = by the king and good physicians; द्विष्टम् = hated.",
            "Visarga → र् and त् → द् before voiced consonants."),
        multi("apply", 4, "Which of these does the verse list as things or persons to avoid?",
              [("Staying with women in private", "Right: line 1."),
               ("Joking with women", "Right: line 1."),
               ("A patient hated by the king and good physicians", "Right: line 2 (the list begins; the verb is understood)."),
               ("Treating a young patient", "Age is not mentioned in this unit."),
               ("Speaking to the king", "Speaking to the king is not mentioned.")],
              [0, 1, 2],
              "Line 1 gives two things to avoid with women; line 2 begins the patients to avoid.",
              "Avoid: private company, joking, and the patient hated by king and good physicians."),
        mcq("transfer", 5,
            "An invented phrase says शिष्यैः पठितं शास्त्रम्. What does it mean?",
            ("The treatise read by the pupils",
             "शिष्यैः is instrumental plural 'by the pupils', as in वैद्यैः द्विष्टम्, 'hated by the physicians'."),
            [("The pupils read by the treatise", "The pupils are the doers (शिष्यैः), not the thing read."),
             ("The treatise to be read by one pupil", "शिष्यैः is plural, and पठितम् is past, not 'to be'."),
             ("The pupils who will read the treatise", "पठितम् is past, not future.")],
            "With a past participle, the instrumental names the doer: 'by whom'.",
            "Instrumental + past participle = done by.",
            teaches="A past participle with an instrumental (द्विष्टं वैद्यैः, पठितं शिष्यैः) means 'done by' the instrumental noun."),
    ],
}

# ---------------------------------------------------------------- unit 19
AUTHORED["19"] = {
    "title": "चंडं शोकातुरं भीरुं",
    "question": "Which kinds of patient does this list name?",
    "rule": ("Nine descriptions, all accusative: fierce, stricken with "
             "grief, timid, ungrateful, one who thinks himself a physician; "
             "lacking equipment, agitated, disobedient, whose life is spent."),
    "limits": ("The list continues from the previous unit, whose verb "
               "वर्जयेत् (should avoid) is understood; this unit has no verb. "
               "The verse gives no reason for any item and does not say what "
               "'lacking equipment' covers."),
    "explain_hi": ("यह इकाई पिछली इकाई की सूची का बाकी भाग है: क्रिया ‘वर्जयेत्’ वहाँ "
                   "थी, यहाँ केवल द्वितीया में विशेषण हैं। पहली पंक्ति: चण्ड "
                   "(उग्र), शोकातुर (शोक से पीड़ित), भीरु (डरपोक), कृतघ्न (किए "
                   "उपकार को न मानने वाला), वैद्यमानी (अपने को वैद्य मानने वाला)। "
                   "दूसरी पंक्ति: हीनोपकरण (साधनों से रहित), व्यग्र (व्याकुल), "
                   "अविधेय (आज्ञा न मानने वाला), गतायुष (जिसकी आयु जा चुकी)। "
                   "श्लोक इनमें से किसी का कारण नहीं बताता।"),
    "core": False,
    "hook": "उग्र · शोकातुर · भीरु · कृतघ्न · वैद्यमानी ‖ साधनहीन · व्याकुल · आज्ञा न माने · गतायु।",
    "questions": [
        mcq("pretest", 0,
            "The first word of the list, चण्डम्, describes a person who is what?",
            ("Fierce",
             "चण्ड means fierce."),
            [("Timid", "Timid is भीरु, the third word of line 1."),
             ("Ungrateful", "Ungrateful is कृतघ्न, the fourth word."),
             ("Agitated", "Agitated is व्यग्र, in line 2.")],
            "The list opens with चण्डम्, fierce; timid and ungrateful come later in the line.",
            "चण्ड = fierce."),
        order(1, "Arrange these items of line 1 in the verse's order.",
              ["चंडं", "शोकातुरं", "भीरुं", "कृतघ्नं", "वैद्यमानिनं"],
              "Line 1 reads: चंडं शोकातुरं भीरुं कृतघ्नं वैद्यमानिनं.",
              "Fierce, stricken with grief, timid, ungrateful, one who thinks himself a physician."),
        T(match(2, "Match each word of the verse to its meaning.",
                [["भीरुम्", "timid"], ["कृतघ्नम्", "ungrateful"],
                 ["व्यग्रम्", "agitated"], ["गतायुषम्", "whose life has gone"]],
                "Four of the nine descriptions.",
                "भीरुम् = timid; कृतघ्नम् = ungrateful; व्यग्रम् = agitated; गतायुषम् = whose life has gone.",
                role="extend"),
          "All nine words are accusative singular and masculine, the same case and gender as one person."),
        mcq("discriminate", 3, "Which is the right split of हीनोपकरणं?",
            ("हीन + उपकरणम्",
             "अ + उ gives ओ, so हीन + उपकरणम् is written हीनोपकरणम्: lacking equipment."),
            [("हीनः + उपकरणम्", "That would be written हीन उपकरणम् (the visarga drops before उ)."),
             ("हीना + उपकरणम्", "आ + उ would give हीनोपकरणम् too, but हीना is a feminine form, not this word."),
             ("हीनो + पकरणम्", "पकरणम् is not a word.")],
            "The first member हीन (lacking) joins उपकरण (equipment) by अ + उ → ओ.",
            "अ + उ → ओ: हीन + उपकरण → हीनोपकरण."),
        multi("apply", 4, "Which of these are named in the list?",
              [("Ungrateful", "Right: कृतघ्नम्."),
               ("One who thinks himself a physician", "Right: वैद्यमानिनम्."),
               ("Disobedient", "Right: अविधेयम्."),
               ("Greedy", "Greed is not named."),
               ("Talkative", "Talkativeness is not named.")],
              [0, 1, 2],
              "The nine items are fixed; greed and talkativeness are not among them.",
              "Ungrateful, self-styled physician, disobedient: yes. Greedy, talkative: no."),
        mcq("transfer", 5,
            "An invented phrase says पण्डितमानिनं शिष्यम्. What does it describe?",
            ("A pupil who thinks himself learned",
             "-मानिन् after a word means 'thinking oneself that', as in वैद्यमानिनम्."),
            [("A pupil who respects the learned", "-मानिन् is about thinking oneself, not respecting others."),
             ("A learned pupil of a physician", "वैद्य is not in the phrase; and -मानिन् does not mean 'learned'."),
             ("A pupil who is proud of his teacher", "The pride is in himself being learned, not in a teacher.")],
            "वैद्यमानिन् = thinking himself a physician; पण्डितमानिन् = thinking himself learned.",
            "X-मानिन् = one who thinks himself X.",
            teaches="A word ending in -मानिन् means 'one who thinks himself …': वैद्यमानी, पण्डितमानी."),
    ],
}

# ---------------------------------------------------------------- unit 20
AUTHORED["20"] = {
    "title": "जिजीविषुर्व्याधितोऽपि",
    "question": "Whom should even a sick person who wants to live avoid, and why?",
    "rule": ("Even a sick person who wishes to live should avoid physicians "
             "who lack the qualities stated earlier and who sell treatment; "
             "for they are the forerunners of death."),
    "limits": ("The verb 'should avoid' is not printed in the unit; it is "
               "understood from the preceding verse. The verse does not say "
               "which earlier qualities, nor what 'selling treatment' covers."),
    "explain_hi": ("इस श्लोक में रोगी के लिए नियम है: जीने की इच्छा रखने वाला रोगी "
                   "भी उन वैद्यों को छोड़े जिनमें पहले बताए गुण नहीं हैं और जो "
                   "क्रिया (चिकित्सा) बेचते हैं। कारण ‘हि ते’ से दिया गया है: वे "
                   "मृत्यु के अग्रेसर (आगे चलने वाले) हैं। ‘छोड़े’ वाली क्रिया "
                   "इस इकाई में छपी नहीं है, पिछले श्लोक से समझी जाती है। "
                   "‘जिजीविषुर्व्याधितोऽपि’ में जिजीविषुः + व्याधितः + अपि जुड़े हैं।"),
    "hook": "जीने की इच्छा वाला रोगी भी: गुणहीन और चिकित्सा बेचने वाले वैद्य से बचे — वे मृत्यु के अग्रदूत।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Why, according to the verse, are such physicians to be avoided?",
            ("They are the forerunners of death",
             "मृत्योः अग्रेसराः हि ते: for they go ahead of death."),
            [("They are poor", "Poverty is not mentioned."),
             ("They are far away", "Distance is not mentioned."),
             ("They are too young", "Age is not mentioned.")],
            "The reason is the clause मृत्योरग्रेसरा हि ते: they are indeed the forerunners of death.",
            "Reason: they are forerunners of death."),
        match(1, "Match each word of the verse to its meaning.",
              [["जिजीविषुः", "desirous of living"], ["व्याधितः", "afflicted with disease"],
               ["अग्रेसराः", "forerunners"], ["मृत्योः", "of death"]],
              "Words of both lines: the one who wants to live, and the ones who go ahead of death.",
              "जिजीविषुः = desirous of living; व्याधितः = afflicted with disease; अग्रेसराः = forerunners; मृत्योः = of death."),
        T(order(2, "Arrange these phrases of line 2 in the verse's order.",
                ["क्रियाविक्रयिणः", "वैद्यान्", "मृत्योः", "अग्रेसराः", "हि ते"],
                "Line 2 reads: क्रियाविक्रयिणो वैद्यान्मृत्योरग्रेसरा हि ते.",
                "Sellers of treatment + physicians + of death + forerunners + indeed they.", role="extend"),
          "A short reason clause can close the verse: मृत्योः अग्रेसराः हि ते, 'for they are death's forerunners'."),
        mcq("discriminate", 3, "Which is the right split of जिजीविषुर्व्याधितोऽपि?",
            ("जिजीविषुः + व्याधितः + अपि",
             "The visarga becomes र् before the voiced व्, and अः + अ gives ओऽ."),
            [("जिजीविषुर् + आधितः + अपि", "आधितः is not a word; the word is व्याधितः."),
             ("जिजीविषुः + व्याधित + अपि", "The nominative needs the visarga: व्याधितः; its loss would not give ओऽ."),
             ("जिजीविषु + र्व्याधितः + अपि", "र्व्याधितः is not a word.")],
            "जिजीविषुः (desirous of living) + व्याधितः (sick) + अपि (even).",
            "ः → र् before a voiced consonant; अः + अ → ोऽ."),
        mcq("apply", 4,
            "A sick man who wants to live meets a physician who sells treatment and lacks the earlier qualities. What does the verse say?",
            ("He should avoid him",
             "वैद्यान् … क्रियाविक्रयिणः: such physicians are to be avoided, even by a sick person who wants to live."),
            [("He should hurry to him", "The verse calls such physicians forerunners of death."),
             ("He should pay him in advance", "Paying is not mentioned."),
             ("He should ask the king to choose", "The king is not in this verse.")],
            "The verse bars both marks together: lacking the earlier qualities and selling treatment.",
            "Avoid physicians lacking the qualities and selling treatment."),
        mcq("transfer", 5,
            "An invented phrase says राज्ञः अग्रेसरो दूतः. What does it say?",
            ("The messenger goes ahead of the king",
             "अग्रेसर is 'going in front', and the genitive names whom he goes ahead of, as मृत्योः अग्रेसराः."),
            [("The king goes ahead of the messenger", "The genitive राज्ञः names the one who is led, not the leader."),
             ("The messenger is the king's enemy", "Nothing says enemy; अग्रेसर is 'forerunner'."),
             ("The king is the messenger's servant", "Nothing says servant.")],
            "Genitive + अग्रेसर = forerunner of that person.",
            "X's अग्रेसर = one who goes ahead of X.",
            teaches="Genitive + अग्रेसर means 'forerunner of': मृत्योरग्रेसराः, राज्ञोऽग्रेसरः."),
    ],
}

# ---------------------------------------------------------------- unit 21
AUTHORED["21"] = {
    "title": "भिषक् द्रव्याण्युपस्थाता",
    "question": "What are the four quarters (pāda) of treatment?",
    "rule": ("The physician, the medicines, the attendant and the patient "
             "are declared the four quarters of treatment; each of them has "
             "four qualities."),
    "limits": ("The verse names the four quarters and says each has four "
               "qualities; the qualities themselves come in the next two "
               "units. 'तच्चतुर्गुणम्' is read as तत् + चतुर्गुणम्, 'that, "
               "four-quality, for each'."),
    "explain_hi": ("चिकित्सा के चार ‘पाद’ (चरण, आधार) यहाँ गिनाए गए हैं: भिषक् "
                   "(वैद्य), द्रव्य (औषधियाँ), उपस्थाता (परिचारक) और रोगी। "
                   "‘पाद’ का अर्थ चौथाई या पैर है: चार पैरों पर चिकित्सा खड़ी "
                   "है। दूसरी पंक्ति कहती है कि इनमें से प्रत्येक चार गुणों "
                   "वाला है; वे गुण अगले दो श्लोकों में आते हैं। ‘द्रव्याण्युपस्थाता’ "
                   "में द्रव्याणि + उपस्थाता जुड़े हैं: इ + उ → यु।"),
    "hook": "चार पाद: वैद्य · द्रव्य · परिचारक · रोगी — हर एक के चार गुण।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "Which are the four quarters (pāda) of treatment in this verse?",
            ("Physician, medicines, attendant, patient",
             "भिषक् द्रव्याणि उपस्थाता रोगी: these are the four."),
            [("Physician, patient, disease, season", "Disease and season are not among the four."),
             ("Teacher, pupil, treatise, practice", "These are not the four quarters."),
             ("Medicine, diet, rest, prayer", "Diet, rest and prayer are not named.")],
            "The verse lists exactly four and calls them पादचतुष्टयम्, the four quarters of treatment.",
            "Four quarters: physician, medicines, attendant, patient."),
        match(1, "Match each Devanagari word to its meaning.",
              [["भिषक्", "physician"], ["द्रव्याणि", "medicines"],
               ["उपस्थाता", "attendant"], ["रोगी", "patient"]],
              "The four quarters, in the order of line 1.",
              "भिषक् = physician; द्रव्याणि = medicines; उपस्थाता = attendant; रोगी = patient."),
        T(order(2, "Arrange the four quarters in the verse's order.",
                ["भिषक्", "द्रव्याणि", "उपस्थाता", "रोगी"],
                "Line 1 reads: भिषक् द्रव्याण्युपस्थाता रोगी.",
                "Physician, medicines, attendant, patient.", role="extend"),
          "The order of the quarters (physician, medicines, attendant, patient) is also the order of their qualities in the next two units."),
        mcq("discriminate", 3, "Which is the right split of द्रव्याण्युपस्थाता?",
            ("द्रव्याणि + उपस्थाता",
             "इ before a different vowel becomes य्: द्रव्याणि + उपस्थाता → द्रव्याण्युपस्थाता."),
            [("द्रव्याण + उपस्थाता", "अ + उ would give ओ, द्रव्याणोपस्थाता."),
             ("द्रव्याणः + उपस्थाता", "The plural of द्रव्य is द्रव्याणि; a visarga ending is not formed."),
             ("द्रव्याणु + उपस्थाता", "उ + उ would give ऊ, द्रव्याणूपस्थाता.")],
            "द्रव्याणि is the neuter nominative plural 'medicines'; its इ becomes य् before उ.",
            "इ + other vowel → य् + vowel."),
        mcq("apply", 4,
            "A clinic has a skilled physician, medicines and a patient, but nobody to attend. Which quarter is missing?",
            ("The attendant",
             "उपस्थाता is the third quarter; the other three are present."),
            [("The medicines", "The clinic has medicines."),
             ("The physician", "The clinic has a physician."),
             ("The patient", "The clinic has a patient.")],
            "Of the four named quarters, only the attendant is absent.",
            "The four quarters: physician, medicines, attendant, patient."),
        mcq("transfer", 5,
            "An invented line says प्रत्येकं तत्त्रिगुणम्, like प्रत्येकं तच्चतुर्गुणम्. What does it say?",
            ("Each of them has three qualities",
             "प्रत्येकम् is 'each one'; त्रिगुण is 'having three qualities', as चतुर्गुण is 'four'."),
            [("All of them together have one quality", "प्रत्येकम् means each, not all together."),
             ("Each of them has four qualities", "त्रि is three; four is चतुर्."),
             ("Three of them have no quality", "गुण is quality; nothing says none.")],
            "A number + गुण names how many qualities something has; प्रत्येकम् spreads it over each item.",
            "प्रत्येकम् + n-गुणम् = each has n qualities.",
            teaches="प्रत्येकम् = each one; number + गुण (त्रिगुणम्, चतुर्गुणम्) = having that many qualities."),
    ],
}

# ---------------------------------------------------------------- unit 22
AUTHORED["22"] = {
    "title": "दक्षस्तीर्थात्तशास्त्रार्थो",
    "question": "What four qualities has the physician, and what four the medicine?",
    "rule": ("The physician is skilled, has taken the meaning of the "
             "treatises from a teacher, has seen the work done, and is pure. "
             "The medicine has many preparations, many qualities, is well "
             "endowed and is suitable."),
    "limits": ("तीर्थ is literally a ford; it is read here as a teacher or "
               "authoritative source. 'Preparations' (कल्प) and 'well "
               "endowed' are not explained in the verse. The verb is "
               "understood, not printed."),
    "explain_hi": ("पिछले श्लोक में कहा गया था कि हर पाद के चार गुण हैं; यहाँ पहले दो "
                   "पादों के चार-चार गुण हैं। वैद्य: दक्ष (कुशल), तीर्थ से "
                   "शास्त्रों का अर्थ ग्रहण किया हुआ (तीर्थ यहाँ गुरु या प्रमाण "
                   "के अर्थ में समझा गया है), दृष्टकर्मा (कर्म को देखा हुआ) और "
                   "शुचि (पवित्र)। औषध: बहुकल्प (अनेक रूप-विधियों वाला), बहुगुण, "
                   "सम्पन्न और योग्य। कौन-सा गुण किसका है, यह श्लोक के क्रम "
                   "से स्पष्ट है।"),
    "hook": "वैद्य: कुशल · गुरु से शास्त्रार्थ · कर्म देखा · शुचि ‖ औषध: बहुकल्प · बहुगुण · सम्पन्न · योग्य।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "Which of these is a quality of the medicine in this verse?",
            ("Suitable (योग्य)",
             "योग्यमौषधम्: the medicine is suitable."),
            [("Skilled (दक्ष)", "Skilled is the physician's quality in line 1."),
             ("Pure (शुचि)", "Pure is the physician's quality in line 1."),
             ("One who has seen the work done", "That is the physician's quality (दृष्टकर्मा).")],
            "Line 2 gives the medicine four qualities; योग्य is the last of them.",
            "Medicine: many preparations, many qualities, well endowed, suitable."),
        order(1, "Arrange the four qualities of the physician in the verse's order.",
              ["दक्षः", "तीर्थात्तशास्त्रार्थः", "दृष्टकर्मा", "शुचिः"],
              "Line 1 reads: दक्षस्तीर्थात्तशास्त्रार्थो दृष्टकर्मा शुचिर्भिषक्.",
              "Skilled, taken the treatises' meaning from a teacher, has seen the work, pure."),
        T(match(2, "Match each quality of the medicine to its meaning.",
                [["बहुकल्पम्", "of many preparations"], ["बहुगुणम्", "of many qualities"],
                 ["सम्पन्नम्", "well endowed"], ["योग्यम्", "suitable"]],
                "The four qualities of the medicine, line 2.",
                "बहुकल्पम् = of many preparations; बहुगुणम् = of many qualities; सम्पन्नम् = well endowed; योग्यम् = suitable.",
                role="extend"),
          "बहु- + a noun makes a description 'having many …' (बहुकल्प, बहुगुण)."),
        mcq("discriminate", 3, "Which is the right split of शुचिर्भिषक्?",
            ("शुचिः + भिषक्",
             "The visarga becomes र् before the voiced भ्."),
            [("शुचिर् + इषक्", "इषक् is not a word; the word is भिषक्."),
             ("शुचि + र्भिषक्", "र्भिषक् is not a word."),
             ("शुचिः + अभिषक्", "अभिषक् is not a word.")],
            "शुचिः (pure) + भिषक् (physician).",
            "ः → र् before a voiced consonant."),
        mcq("apply", 4,
            "A physician has learned the meaning of the treatises from a teacher but did not see the work done. Which quality is missing?",
            ("दृष्टकर्मा",
             "He lacks the quality of one who has seen the work done."),
            [("दक्षः", "Nothing is said about his skill."),
             ("शुचिः", "Nothing is said about his purity."),
             ("तीर्थात्तशास्त्रार्थः", "He has this: he learned the meaning from a teacher.")],
            "The four qualities are separate; the missing one is दृष्टकर्मा.",
            "Four qualities of the physician: skilled, learned from a teacher, has seen work, pure."),
        mcq("transfer", 5,
            "An invented phrase says बहुफलं वृक्षम्. What does it describe?",
            ("A tree with many fruits",
             "बहु- joined to a neuter noun makes a description 'having many …', as in बहुगुणम्."),
            [("A tree with no fruit", "बहु- is 'many', not 'no'."),
             ("Many trees bearing fruit", "वृक्षम् is singular; one tree."),
             ("A fruit of a big tree", "फल is inside the description, not a separate noun with वृक्ष as owner.")],
            "बहुगुणम् is 'having many qualities'; बहुफलम् is 'having many fruits'.",
            "बहु- + noun = having many …",
            teaches="बहु- before a noun makes a description 'having many …': बहुकल्पम्, बहुगुणम्, बहुफलम्."),
    ],
}

# ---------------------------------------------------------------- unit 23
AUTHORED["23"] = {
    "title": "अनुरक्तः शुचिर्दक्षो",
    "question": "What four qualities has the attendant, and what four the patient?",
    "rule": ("The attendant is devoted, pure, skilled and intelligent. The "
             "patient is wealthy, obedient to the physician, able to make "
             "his condition known, and possessed of mental strength."),
    "limits": ("ज्ञापकः is read as 'one who can inform the physician of his "
               "complaint'; another reading is 'one who understands', so "
               "no question rests on it. The verb is understood, not printed."),
    "explain_hi": ("यह श्लोक तीसरे और चौथे पाद के चार-चार गुण देता है। परिचारक: "
                   "अनुरक्त (स्नेह-भक्ति वाला), शुचि, दक्ष और बुद्धिमान्। रोगी: "
                   "आढ्य (धनवान्), भिषग्वश्य (वैद्य के वश में, आज्ञाकारी), "
                   "ज्ञापक (अपनी बात बता सकने वाला; इसका दूसरा पाठ ‘समझने वाला’ "
                   "भी हो सकता है) और सत्त्ववान् (मनोबल वाला)। ‘शुचि’ और ‘दक्ष’ "
                   "इस श्लोक में परिचारक के गुण हैं, जैसे पिछले में वैद्य के।"),
    "hook": "परिचारक: अनुरक्त · शुचि · दक्ष · बुद्धिमान् ‖ रोगी: आढ्य · वैद्य के वश · बता सके · सत्त्ववान्।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "In this verse, who is described as devoted (अनुरक्त)?",
            ("The attendant",
             "अनुरक्तः … परिचारकः: the attendant is devoted."),
            [("The physician", "The physician's qualities were given in the previous unit."),
             ("The medicine", "The medicine's qualities were given in the previous unit."),
             ("The patient", "The patient's qualities are in line 2: wealthy, obedient and so on.")],
            "Line 1 is about the attendant (परिचारकः): devoted, pure, skilled, intelligent.",
            "Attendant: devoted, pure, skilled, intelligent."),
        order(1, "Arrange the four qualities of the attendant in the verse's order.",
              ["अनुरक्तः", "शुचिः", "दक्षः", "बुद्धिमान्"],
              "Line 1 reads: अनुरक्तः शुचिर्दक्षो बुद्धिमान्परिचारकः.",
              "Devoted, pure, skilled, intelligent."),
        T(match(2, "Match each quality of the patient to its meaning.",
                [["आढ्यः", "wealthy"], ["भिषग्वश्यः", "obedient to the physician"],
                 ["सत्त्ववान्", "having mental strength"], ["अनुरक्तः", "devoted"]],
                "Three qualities of the patient in line 2, and one word from line 1 to keep apart.",
                "आढ्यः = wealthy; भिषग्वश्यः = obedient to the physician; सत्त्ववान् = having mental strength. अनुरक्तः (devoted) belongs to line 1, the attendant.",
                role="extend"),
          "First member + वश्य (भिषग्वश्य) means 'under the control of' that first member."),
        mcq("discriminate", 3, "Which is the right split of भिषग्वश्यः?",
            ("भिषक् + वश्यः",
             "Final क् becomes ग् before the voiced व."),
            [("भिषः + वश्यः", "भिषः is not a word."),
             ("भिषग् + अश्यः", "अश्यः is not a word."),
             ("भिष + ग्वश्यः", "ग्वश्यः is not a word.")],
            "भिषक् (physician) + वश्यः (under control): obedient to the physician.",
            "क् → ग् before a voiced consonant."),
        multi("apply", 4, "Which qualities does the verse give the patient?",
              [("Wealthy", "Right: आढ्यः."),
               ("Obedient to the physician", "Right: भिषग्वश्यः."),
               ("Possessed of mental strength", "Right: सत्त्ववान्."),
               ("Devoted", "Devoted is the attendant's quality in line 1."),
               ("Intelligent", "Intelligent is the attendant's quality in line 1.")],
              [0, 1, 2],
              "Line 2 gives the patient his qualities; devoted and intelligent are the attendant's.",
              "Patient: wealthy, obedient, able to make known, mentally strong."),
        mcq("transfer", 5,
            "An invented phrase says गुरुवश्यः शिष्यः. What does it describe?",
            ("A pupil obedient to the teacher",
             "वश्य gives 'under the control of' the first member, as भिषग्वश्यः is under the physician."),
            [("A teacher obedient to the pupil", "The first member names who controls: गुरु."),
             ("A pupil who rules the teacher", "That would be the reverse."),
             ("A pupil without a teacher", "Nothing here says 'without'.")],
            "Same pattern as भिषग्वश्यः: the first member is the one who has control.",
            "X-वश्य = under the control of X.",
            teaches="X-वश्य = under X's control, obedient to X (भिषग्वश्यः, गुरुवश्यः)."),
    ],
}

# ---------------------------------------------------------------- unit 24
AUTHORED["24"] = {
    "title": "यद्वैद्ये विगुणे पादा",
    "question": "What two reasons are given here for the physician's importance?",
    "rule": ("Since, when the physician lacks qualities, the other quarters "
             "are useless even if qualified; and since a qualified physician "
             "keeps going even patients lacking the other quarters."),
    "limits": ("Confidence is medium. Both lines are 'since' clauses; the "
               "conclusion comes in the next unit. In line 2, सपादहीनान् is "
               "read as सः + पादहीनान्; one could also read a compound, so "
               "no question rests on it."),
    "explain_hi": ("यहाँ दो कारण (‘यत्’ = क्योंकि) दिए गए हैं। पहला: जब वैद्य "
                   "विगुण (गुणहीन) हो तो बाकी पाद गुणवान् होते हुए भी अनर्थक हैं। "
                   "दूसरा: गुणवान् वैद्य उन रोगियों को भी ‘यापयेत्’ (चला ले, टिकाए "
                   "रखे) जिनके पास बाकी पाद नहीं हैं। निष्कर्ष इस इकाई में नहीं है: "
                   "वह अगले श्लोक की पहली पंक्ति में आता है। दूसरी पंक्ति में "
                   "‘सपादहीनान्’ का पाठ दो तरह से पढ़ा जा सकता है, इसलिए प्रश्न "
                   "पहली पंक्ति और सरल भाव पर रखे हैं।"),
    "hook": "यत्: वैद्य गुणहीन तो बाकी पाद व्यर्थ · गुणवान् वैद्य पादहीन रोगी को भी चला ले (निष्कर्ष आगे)।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "When the physician lacks qualities, what happens to the other quarters?",
            ("They are useless, even if qualified",
             "गुणवन्तोऽप्यनर्थकाः: even though they have qualities, they are useless."),
            [("They make up for him", "The verse says the opposite: they become useless."),
             ("They are doubled in value", "Nothing like this is said."),
             ("They are replaced by new ones", "Replacement is not mentioned.")],
            "यद्वैद्ये विगुणे पादा गुणवन्तोऽपि अनर्थकाः: when the physician lacks qualities, the quarters are useless though they have qualities.",
            "Physician without qualities: other quarters useless."),
        order(1, "Arrange these phrases of line 1 in the verse's order.",
              ["यद्वैद्ये", "विगुणे", "पादाः", "गुणवन्तोऽपि", "अनर्थकाः"],
              "Line 1 reads: यद्वैद्ये विगुणे पादा गुणवंतोऽप्यनर्थकाः.",
              "Since in the physician + lacking qualities + the quarters + even qualified + useless."),
        T(match(2, "Match each word of the verse to its meaning.",
                [["विगुणे", "lacking qualities"], ["गुणवन्तः", "having qualities"],
                 ["अनर्थकाः", "useless"], ["यापयेत्", "may keep going"]],
                "Three words of line 1 and the verb of line 2.",
                "विगुणे = lacking qualities; गुणवन्तः = having qualities; अनर्थकाः = useless; यापयेत् = may keep going.",
                role="extend"),
          "वि-/अन्- style prefixes reverse a meaning: विगुण = without qualities, अनर्थक = without use."),
        mcq("discriminate", 3, "Which is the right split of गुणवंतोऽप्यनर्थकाः?",
            ("गुणवन्तः + अपि + अनर्थकाः",
             "अः + अ gives ोऽ, and अपि + अ… joins as अप्य…: इ before a different vowel becomes य्."),
            [("गुणवान् + अपि + अनर्थकाः", "गुणवान् is the singular; the quarters are plural, गुणवन्तः."),
             ("गुणवन्त + ओपि + अनर्थकाः", "ओपि is not a word."),
             ("गुणवन्तः + आपि + अनर्थकाः", "आपि is not a word; the word is अपि.")],
            "गुणवन्तः (having qualities, plural) + अपि (even) + अनर्थकाः (useless).",
            "अः + अ → ोऽ; इ + other vowel → य्."),
        mcq("apply", 4,
            "The medicine, attendant and patient are all qualified, but the physician lacks qualities. What does the verse say?",
            ("The three are useless",
             "वैद्ये विगुणे … पादा अनर्थकाः: the other quarters are useless."),
            [("The three make treatment succeed", "That is the opposite of the verse."),
             ("The patient alone decides the result", "The patient is one of the quarters named useless here."),
             ("The medicine alone is enough", "The medicine too is one of the quarters, useless without the physician.")],
            "The verse says a qualified rest cannot rescue a physician without qualities.",
            "Physician unqualified → qualified other quarters useless."),
        mcq("transfer", 5,
            "An invented line says सारथौ विगुणे रथोऽनर्थकः. What does it say?",
            ("When the charioteer lacks qualities, the chariot is useless",
             "Noun and adjective both in the locative (सारथौ विगुणे) set the condition, as वैद्ये विगुणे."),
            [("The charioteer is useless because the chariot lacks qualities", "The locative phrase is the charioteer lacking qualities."),
             ("Though the chariot lacks qualities, the driver is useful", "The locative names the charioteer, not the chariot."),
             ("The chariot lacks qualities and so the driver is a fool", "Nothing about a fool is said.")],
            "A noun + adjective in the locative states the condition, 'when X is so': वैद्ये विगुणे.",
            "Locative noun + adjective = when X is so.",
            teaches="A noun and its adjective both in the locative (वैद्ये विगुणे, सारथौ विगुणे) mean 'when X is so'."),
    ],
}

# ---------------------------------------------------------------- unit 25
AUTHORED["25"] = {
    "title": "चिकित्सायास्तमेवातः",
    "question": "Whom do they call the chief cause of treatment, and how is disease divided?",
    "rule": ("Therefore they know him (the physician) alone as the chief "
             "cause of treatment. Disease is twofold, curable and "
             "incurable, and each of the two is again twofold."),
    "limits": ("तम् is the physician of the previous unit. The four classes "
               "reached by the second division are named only in the next "
               "unit. The printed साध्योऽसाध्यइति is read as साध्यः असाध्यः "
               "इति (a flagged scan slip)."),
    "explain_hi": ("पहली पंक्ति पिछली इकाई का निष्कर्ष है: ‘अतः’ (इसलिए) उसी वैद्य को "
                   "चिकित्सा का प्रधान कारण माना जाता है। ‘विदुः’ के साथ दो "
                   "द्वितीया हैं: तम् और प्रधानं कारणम्, यानी ‘उसे प्रधान कारण "
                   "जानते हैं’। दूसरी पंक्ति में रोग पहले दो प्रकार का है, साध्य "
                   "और असाध्य, और ये दोनों फिर दो-दो प्रकार के हैं; चारों के नाम "
                   "अगले श्लोक में आते हैं। छपा ‘साध्योऽसाध्यइति’ स्कैन की "
                   "चूक है; पढ़ना है साध्यः असाध्यः इति।"),
    "hook": "इसलिए वैद्य ही चिकित्सा का प्रधान कारण · रोग = साध्य/असाध्य, और हर एक फिर दो प्रकार का।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "In line 1, whom do they know as the chief cause of treatment?",
            ("The physician",
             "तमेव: him alone, the physician of the previous unit, is the chief cause."),
            [("The medicine", "The medicine is only one of the quarters."),
             ("The patient", "The patient is only one of the quarters."),
             ("The attendant", "The attendant is only one of the quarters.")],
            "Because the physician's lack of qualities makes the other quarters useless, they call him the chief cause.",
            "The physician alone is the chief cause."),
        order(1, "Arrange these phrases of line 2 in the verse's order.",
              ["साध्योऽसाध्य इति", "व्याधिर्द्विधा", "तौ तु पुनर्द्विधा"],
              "Line 2 reads: साध्यः असाध्यः इति व्याधिः द्विधा, तौ तु पुनः द्विधा.",
              "Curable, incurable: thus disease is twofold; those two again twofold."),
        T(match(2, "Match each word of the verse to its meaning.",
                [["प्रधानम्", "chief"], ["कारणम्", "cause"],
                 ["साध्यः", "curable"], ["असाध्यः", "incurable"]],
                "Two words of line 1 and two of line 2.",
                "प्रधानम् = chief; कारणम् = cause; साध्यः = curable; असाध्यः = incurable.",
                role="extend"),
          "अ- before a word reverses it: साध्य (curable), असाध्य (incurable)."),
        mcq("discriminate", 3, "Which is the right split of साध्योऽसाध्य इति?",
            ("साध्यः + असाध्यः + इति",
             "अः + अ gives ोऽ, and असाध्यः + इति loses its visarga before इ."),
            [("साध्य + ओसाध्य + इति", "ओसाध्य is not a word."),
             ("साध्यः + साध्यः + इति", "The second word has the negative अ-: असाध्यः, incurable."),
             ("साध्यः + असाध्यम् + इति", "The disease (व्याधिः) is masculine; असाध्यम् is neuter.")],
            "साध्यः (curable) + असाध्यः (incurable) + इति (thus).",
            "अः + अ → ोऽ."),
        mcq("apply", 4,
            "A learner says: the verse divides disease into curable and incurable, and each is again divided. Is that right?",
            ("Yes: two, then each of the two again twofold",
             "व्याधिर्द्विधा, तौ तु पुनर्द्विधा says exactly that."),
            [("No: it divides disease into curable only", "Incurable is named too."),
             ("No: it divides disease into three", "The verse says twofold, then twofold again."),
             ("No: it names the four classes here", "The four names come in the next unit.")],
            "The unit gives the first division and the second division but not the names of the final classes.",
            "Disease: curable/incurable, each again twofold."),
        mcq("transfer", 5,
            "An invented line says तमेव गुरुं श्रेष्ठं विदुः. What does it say?",
            ("They know that teacher alone as the best",
             "विदुः takes two accusatives: 'know X as Y', as तमेव प्रधानं कारणं विदुः."),
            [("They know the best teacher but not him", "तमेव says him alone, not a different one."),
             ("He alone knows the best teacher", "The doer of विदुः is 'they', and the accusatives are what they know."),
             ("They do not know him as the best", "There is no negative in the line.")],
            "विदुः + two accusatives = 'they know X as Y'; एव = alone.",
            "विदुः X Y = they know X as Y.",
            teaches="With विदुः (they know) two accusatives give 'know X as Y'; एव limits it to X alone."),
    ],
}

# ---------------------------------------------------------------- unit 26
AUTHORED["26"] = {
    "title": "सुसाध्यः कृच्छ्रसाध्यश्च",
    "question": "What are the four classes of disease named here?",
    "rule": ("Easily curable (सुसाध्य), curable with difficulty "
             "(कृच्छ्रसाध्य), to be sustained or palliated (याप्य), and the "
             "one that admits no remedy (अनुपक्रम)."),
    "limits": ("Line 2 begins a sentence that runs into the next unit and "
               "has no verb here, so no question rests on it. The verse does "
               "not say which of the four belongs under 'curable' or "
               "'incurable'."),
    "explain_hi": ("पिछले श्लोक में रोग साध्य-असाध्य और फिर हर एक दो-दो प्रकार का "
                   "बताया गया था; यहाँ चारों नाम आते हैं: सुसाध्य (आसानी से ठीक "
                   "होने वाला), कृच्छ्रसाध्य (कठिनाई से साध्य), याप्य (जिसे "
                   "चलाया या टिकाया जा सके) और अनुपक्रम (जिसमें कोई उपक्रम "
                   "यानी उपाय नहीं चलता)। दूसरी पंक्ति एक वाक्य की शुरुआत है, जो "
                   "अगली इकाई में पूरा होता है: सब औषधियाँ सह सकने वाले शरीर में, "
                   "युवा पुरुष में, जिसने अपने को जीत रखा हो। उस वाक्य की क्रिया "
                   "यहाँ नहीं है, इसलिए नतीजा आगे देखें।"),
    "hook": "चार रोग: सुसाध्य · कृच्छ्रसाध्य · याप्य · अनुपक्रम (पंक्ति २ का वाक्य आगे चलता है)।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "Which set names the four classes of disease in this verse?",
            ("Easily curable, curable with difficulty, to be sustained, without remedy",
             "सुसाध्यः कृच्छ्रसाध्यः याप्यः अनुपक्रमः: these four."),
            [("Easily curable, curable, incurable, fatal", "Curable, incurable and fatal are not the four names."),
             ("Mild, severe, to be sustained, without remedy", "Mild and severe are not named."),
             ("Curable, incurable, recent, old", "Recent and old are not named.")],
            "The verse names four: सुसाध्य, कृच्छ्रसाध्य, याप्य, अनुपक्रम.",
            "Four classes: सुसाध्य, कृच्छ्रसाध्य, याप्य, अनुपक्रम."),
        order(1, "Arrange the four classes in the verse's order.",
              ["सुसाध्यः", "कृच्छ्रसाध्यः", "याप्यः", "अनुपक्रमः"],
              "Line 1 reads: सुसाध्यः कृच्छ्रसाध्यश्च याप्यो यश्चानुपक्रमः.",
              "Easily curable, curable with difficulty, to be sustained, without remedy."),
        T(match(2, "Match each class to its meaning.",
                [["सुसाध्यः", "easily curable"], ["कृच्छ्रसाध्यः", "curable with difficulty"],
                 ["याप्यः", "to be sustained (palliated)"], ["अनुपक्रमः", "admitting no remedy"]],
                "The four classes of line 1.",
                "सुसाध्यः = easily curable; कृच्छ्रसाध्यः = curable with difficulty; याप्यः = to be sustained (palliable); अनुपक्रमः = admitting no remedy.",
                role="extend"),
          "सु- means 'easily', कृच्छ्र- 'with difficulty': they qualify साध्य (to be accomplished, curable)."),
        mcq("discriminate", 3, "Which is the right split of यश्चानुपक्रमः?",
            ("यः + च + अनुपक्रमः",
             "The visarga becomes श् before च, and च + अ gives चा, since अ + अ → आ."),
            [("यत् + च + अनुपक्रमः", "यत् would not give श्; the word is यः (which)."),
             ("यः + चा + नुपक्रमः", "नुपक्रमः is not a word."),
             ("यस् + चानुपक्रमः", "चानुपक्रमः is not a word; and the particle is च.")],
            "यः (which) + च (and) + अनुपक्रमः (without remedy).",
            "ः + च → श्च; अ + अ → आ."),
        mcq("apply", 4,
            "A physician says a disease can only be sustained. Which class name of the verse says this?",
            ("याप्य",
             "याप्य means to be sustained (palliated)."),
            [("सुसाध्य", "That is 'easily curable'."),
             ("कृच्छ्रसाध्य", "That is 'curable with difficulty'."),
             ("अनुपक्रम", "That is 'admits no remedy'.")],
            "याप्यः is the third class, 'to be sustained'.",
            "याप्य = to be sustained."),
        mcq("transfer", 5,
            "Invented path names: सुगम्यः and कृच्छ्रगम्यः, like सुसाध्यः and कृच्छ्रसाध्यः. What do they mean?",
            ("Easy to go along; to be gone along with difficulty",
             "सु- is 'easily' and कृच्छ्र- 'with difficulty', before गम्य, 'to be gone'."),
            [("Hard to go along; easy to go along", "The two prefixes are swapped."),
             ("Gone along; not gone along", "Nothing marks past or negative."),
             ("Easy to leave; hard to leave", "गम्य is 'to be gone along', not leaving.")],
            "The pattern सु-/कृच्छ्र- + a word 'to be done' gives 'easy to' and 'hard to'.",
            "सु- = easily; कृच्छ्र- = with difficulty.",
            teaches="सु- (easily) and कृच्छ्र- (with difficulty) before a 'to be done' word grade how hard it is."),
    ],
}


NOTES_HI = {
    "14": "विश्वास: उच्च। ‘चिकित्सन्नापराध्यति’ = चिकित्सन् + न + अपराध्यति (न + अ → ना)। ‘आहूतएव’ = आहूतः + एव (अः + ए में विसर्ग लुप्त; मुद्रित पाठ में जुड़ा लिखा है)। ‘ताभ्याम्’ वही दो हैं जिनका नाम पिछली इकाई में आया है; वे यहाँ नहीं हैं। ‘यो याति’ से शुरू हुआ सम्बन्ध-वाक्य आगे की इकाइयों में चलता है और बाद में ‘स वैद्यः सिद्धिमश्नुते’ पर पूरा होता है। ‘सुनिमित्ततः’ का अर्थ शुभ निमित्तों के साथ/बाद; पुस्तक ‘शुभ शकुन’ कहती है। कोई पाठ-चिह्न नहीं।",
    "15": "विश्वास: उच्च। मुद्रित ‘कचित्’ पाठ-चिह्न में है: यह ‘क्वचित्’ (कहीं भी) की चूक है (व छूटा); इस शब्द पर कोई प्रश्न नहीं रखा। ‘गत्वा ऽऽतुरार्थात्’ में दोहरा ऽ आतुर के लुप्त आरम्भिक आ का मुद्रित चिह्न है: गत्वा + आतुर-अर्थात्। ‘सम्यग्निदानादिविशेषतः’ = सम्यक् + निदान + आदि + विशेषतः (क् → ग् घोष न से पहले; निदान + आदि → निदानादि)। ‘निदानादि’ का अर्थ केवल ‘निदान से आरम्भ करके’ है; पूरी सूची पाठ में नहीं। यह पिछले सम्बन्ध-वाक्य (यो याति) की अगली कड़ी है।",
    "16": "विश्वास: मध्यम। पंक्ति १ स्पष्ट है (गोपनीयाम् और वार्त्ताम् दोनों स्त्री. द्वि. ए.)। पंक्ति २ कठिन है: ‘सहसा न च तस्याऽपि क्रियाकालमहापयन्’ को ‘बिना विचारे नहीं, उसका भी चिकित्सा-काल निकलने न देता’ पढ़ा गया है। ‘तस्याऽपि’ को ‘तस्याः अपि’ (उस [चिकित्सा] का भी) भी पढ़ा जा सकता है; पुस्तक का भाव ढीले रूप में लिया गया है। ‘वार्त्ताम्’ का मुद्रित रूप त्त वाला है। इस पंक्ति पर बारीक प्रश्न नहीं रखे। यह भी ‘यो याति’ वाले वाक्य का भाग है।",
    "17": "विश्वास: उच्च। पंक्ति १ ‘यो याति …’ वाले लम्बे वाक्य को पूरा करती है (‘स वैद्यः सिद्धिमश्नुते’); पंक्ति २ नया नियम है। संधियाँ जाँची: जानाति + च + उपचरितुम् → जानाति चोपचरितुम् (अ + उ → ओ); न + आददीत + आमिषम् → नाददीतामिषम् (अ + आ → आ दोनों बार); पराक् + मुखे → पराङ्मुखे। ‘आमिष’ का शाब्दिक अर्थ मांस/लालच है, यहाँ भेंट। ‘तदध्यक्षे पराङ्मुखे’ का अर्थ दो तरह जा सकता है (स्वामी अनुपस्थित/अनिच्छुक); पुस्तक ‘अनुपस्थित’ लेती है।",
    "18": "विश्वास: मध्यम। पाठ-चिह्न: ‘तद्वेषिणं’ सम्भवतः ‘तद्द्वेषिणं’ (उनसे द्वेष रखने वाला) है; द् छूटा लगता है। ‘द्विषम्’ का अर्थ वैद्य का या राजा का शत्रु हो सकता है; पुस्तक ‘शत्रु’ लेती है। ‘नृपसद्वैद्यैः’ = नृप + सत् + वैद्यैः (राजा और सज्जन वैद्यों द्वारा; द्वन्द्व)। ‘वर्जयेत्’ पंक्ति १ की क्रिया है और इसे ही अगली सूची (पंक्ति २ और अगली इकाई) की क्रिया माना गया है। ‘आर्त्तम्’ मुद्रित वर्तनी है (आर्तम्)। इन अस्पष्ट शब्दों पर प्रश्न नहीं रखे।",
    "19": "विश्वास: उच्च। इस इकाई में क्रिया नहीं है; ‘वर्जयेत्’ पिछली इकाई से समझा जाता है। संधियाँ: हीन + उपकरणम् → हीनोपकरणम् (अ + उ → ओ); गत + आयुषम् → गतायुषम् (अ + आ → आ)। ‘वैद्यमानिनम्’ = वैद्य + मानिनम् (अपने को वैद्य मानने वाला)। ‘हीनोपकरण’ में कौन-से साधन, पाठ नहीं बताता। मुद्रित ‘चंडं’ आदि अनुस्वार वाली वर्तनी है (चण्डम्)। कोई पाठ-चिह्न नहीं।",
    "20": "विश्वास: उच्च। ‘छोड़े’ (वर्जयेत्/परिवर्जयेत्) जैसी क्रिया इकाई में छपी नहीं है; पिछले श्लोक से समझी गई है। ‘जिजीविषुर्व्याधितोऽपि’ = जिजीविषुः + व्याधितः + अपि (ः → र् घोष व से पहले; अः + अ → ोऽ)। ‘क्रियाविक्रयिणो’ में क्रिया = चिकित्सा-कर्म (‘बेचने वाले’ = विक्रयिन्)। ‘वैद्यान्मृत्योरग्रेसरा’ = वैद्यान् + मृत्योः + अग्रेसराः (वैद्यान् के बाद म् का जुड़ाव; विसर्ग → र् अ से पहले)। ‘पूर्वोक्त गुण’ कौन-से हैं, यह श्लोक नहीं कहता। कोई पाठ-चिह्न नहीं।",
    "21": "विश्वास: उच्च। ‘द्रव्याण्युपस्थाता’ = द्रव्याणि + उपस्थाता (इ → य् उ से पहले)। ‘पादचतुष्टयम्’ = पाद + चतुष्टयम् (चार पादों का समूह)। ‘तच्चतुर्गुणम्’ = तत् + चतुर्गुणम् (त् + च → च्च), ‘प्रत्येकम्’ के साथ: प्रत्येक वह चार गुणों वाला है। ‘निर्दिष्टम्’ का कर्ता चारों पाद हैं (नपुंसक एकवचन ‘समूह’ के अर्थ में)। कोई पाठ-चिह्न नहीं।",
    "22": "विश्वास: उच्च। ‘दक्षस्तीर्थात्तशास्त्रार्थः’ = दक्षः + तीर्थात् + आत्त + शास्त्र + अर्थः। ‘तीर्थ’ का शाब्दिक अर्थ घाट है; यहाँ गुरु/प्रमाण-स्रोत समझा गया है। तीर्थ + आत्त (अ + आ → आ) और तीर्थात् + आत्त (त् + आ → त्त) दोनों का रूप एक ही है, इसलिए इसे विभाजन-प्रश्न नहीं बनाया। ‘शुचिर्भिषक्’ = शुचिः + भिषक्। ‘योग्यमौषधम्’ = योग्यम् + औषधम्। ‘कल्प’ का अर्थ यहाँ औषध की बनावट/रूप-विधि है; श्लोक उसे स्पष्ट नहीं करता। क्रिया (हो) अध्याहृत है। कोई पाठ-चिह्न नहीं।",
    "23": "विश्वास: उच्च। ‘शुचिर्दक्षो’ = शुचिः + दक्षः। ‘भिषग्वश्यः’ = भिषक् + वश्यः (क् → ग्)। ‘ज्ञापक’ पुस्तक में ‘रोग बता सकने वाला’ है; दूसरा पाठ ‘जानने-समझने वाला’ है, इसलिए इसे प्रश्न में नहीं रखा। ‘सत्त्ववान्’ = मनोबल वाला। ‘सत्त्ववानपि’ का ‘अपि’ पूरे पद-समूह के साथ ‘और भी’ जैसा काम करता है। क्रिया (हो) अध्याहृत है। कोई पाठ-चिह्न नहीं।",
    "24": "विश्वास: मध्यम। ‘यद्वैद्ये’ = यत् + वैद्ये (त् → द् व से पहले), यहाँ ‘क्योंकि’। ‘गुणवंतोऽप्यनर्थकाः’ = गुणवन्तः + अपि + अनर्थकाः। पंक्ति २ में ‘सपादहीनान्’ को सः + पादहीनान् पढ़ा गया है (पुस्तक का विभाजन भी यही); इसे एक समास ‘सपाद-हीन’ (चौथाई-रहित) भी पढ़ा जा सकता है, इसलिए इस पर प्रश्न नहीं रखा। ‘आर्त्तान्’ मुद्रित वर्तनी है (आर्तान्)। ‘यापयेत्’ = चला ले, टिकाए रखे। दोनों पंक्तियाँ ‘क्योंकि’ वाक्य हैं; निष्कर्ष अगली इकाई में।",
    "25": "विश्वास: उच्च। पाठ-चिह्न: मुद्रित ‘साध्योऽसाध्यइति’ सम्भवतः स्कैन की चूक है; ‘साध्यः असाध्यः इति’ पढ़ने पर पंक्ति में १६ अक्षर होते हैं (मुद्रित में १५)। ‘चिकित्सायास्तमेवातः’ = चिकित्सायाः + तम् + एव + अतः (विसर्ग → स् त से पहले)। ‘तम्’ पिछली इकाई का वैद्य है। ‘तौ तु पुनर्द्विधा’ का अर्थ: वे दोनों फिर दो-दो प्रकार के हैं; चारों नाम अगली इकाई में हैं। इस इकाई में हमने सुधरा रूप ही उपयोग किया।",
    "26": "विश्वास: उच्च। ‘कृच्छ्रसाध्यश्च’ = कृच्छ्रसाध्यः + च (ः → श् च से पहले)। ‘यश्चानुपक्रमः’ = यः + च + अनुपक्रमः (ः → श्; अ + अ → आ)। ‘सर्वौषधक्षमे’ = सर्व + औषध + क्षमे (अ + औ → औ)। पंक्ति २ एक वाक्य की शुरुआत है जो अगली इकाई में पूरा होता है; अंग्रेज़ी/हिन्दी में कोष्ठक के शब्द समझे गए हैं, छपे नहीं। ‘जितात्मन्’ = आत्म-संयमी (दूसरा अर्थ ‘जीता हुआ मन’)। चारों नामों का दो वर्गों (साध्य/असाध्य) में कौन-सा कहाँ आता है, श्लोक नहीं कहता। कोई पाठ-चिह्न नहीं।",
}


AIDS = {
    "14": {
        "frame": "किसने: जो चिकित्सा दो (पिछली इकाई में नामित) का भली-भाँति प्रयोग करके करता है · क्या: भूल नहीं करता · जो जाता है: बुलाने पर ही, सुवेश में, शुभ निमित्त पर (वाक्य आगे चलता है)।",
        "sandhi": "न + अपराध्यति → नापराध्यति (अ + अ → आ); चिकित्सन् के बाद यह न जुड़ता है। आहूतः + एव → आहूत एव (अः के बाद ए: विसर्ग लुप्त; मुद्रित पाठ में आहूतएव)।",
        "chunks": "ताभ्यामतः सुयुक्ताभ्यां | चिकित्सन्नापराध्यति ‖ आहूतएव यो याति | सुवेषः सुनिमित्ततः।",
        "anchors": "आहूत = बुलाया हुआ (आ + ह्वे) · सुवेष = सु + वेष, अच्छा पहनावा · सुनिमित्त = शुभ निमित्त (शकुन)।",
    },
    "15": {
        "frame": "क्या करके: जाकर · क्या नहीं: मन रोगी के काम के सिवा कहीं नहीं · क्या करता है: रोगों की परीक्षा, निदान आदि विशेष बातों से।",
        "diagram": {"steps": ["गत्वा (जाकर)", "मन केवल आतुरार्थ पर", "व्याधीन् परीक्षते (रोगों की परीक्षा)", "सम्यक् · निदानादि-विशेषतः"]},
        "sandhi": "गत्वा + आतुर-अर्थात् (मुद्रित: गत्वा ऽऽतुरार्थात्) · सम्यक् + निदान → सम्यग्निदान (क् → ग्) · निदान + आदि → निदानादि (अ + आ → आ)।",
        "chunks": "गत्वा ऽऽतुरार्थादन्यत्र | न निधत्ते मनः कचित् ‖ व्याधीन्परीक्षते सम्यक् | निदानादिविशेषतः।",
        "pegs": "मेरा बनाया चित्र: वैद्य घर पहुँचा, जेब से मन निकालकर रोगी के सिरहाने रखता है; बगल में निदान लिखी पर्ची। (यह मेरी स्मृति-कल्पना है, श्लोक का वर्णन नहीं।)",
    },
    "16": {
        "frame": "क्या नहीं करता: रोगी की गोपनीय बात बाहर प्रकट नहीं · चिकित्सा का समय अचानक (बिना विचारे) निकलने नहीं देता (पंक्ति २ कठिन)।",
        "diagram": {"steps": ["गोपनीयां तद्वार्त्तां", "न प्रकाशयते बहिः", "सहसा न", "क्रियाकालम् अहापयन्"]},
        "anchors": "गोपनीय ← गुप् (रक्षा करना) + अनीय = रखने योग्य · वार्त्ता = समाचार, बात · प्रकाशयते = प्रकट करता है · बहिः = बाहर।",
        "chunks": "गोपनीयां च तद्वार्त्तां | न प्रकाशयते बहिः ‖ सहसा न च तस्याऽपि | क्रियाकालमहापयन्।",
    },
    "17": {
        "frame": "पंक्ति १: जो उपचार करना जानता है, वह वैद्य सिद्धि पाता है (पिछले ‘जो’ का उत्तर) · पंक्ति २: स्त्रियों से भेंट न ले, जब उनका स्वामी विमुख हो।",
        "diagram": {"steps": ["यो याति … (पिछली इकाइयाँ)", "जानाति चोपचरितुं", "स वैद्यः", "सिद्धिमश्नुते"]},
        "sandhi": "जानाति + च + उपचरितुम् → जानाति चोपचरितुम् (अ + उ → ओ) · न + आददीत + आमिषम् → नाददीतामिषम् (अ + आ → आ दोनों बार) · पराक् + मुखे → पराङ्मुखे।",
        "chunks": "जानाति चोपचरितुं | स वैद्यः सिद्धिमश्नुते ‖ नाददीतामिषं स्त्रीभ्यः | तदध्यक्षे पराङ्मुखे।",
        "puns": "केवल सुनने की सहायता (मेरी बनाई): ‘आमिष’ सुनकर ‘आम-इश’ याद करें: ‘मुफ़्त का आम’, यानी भेंट; यह श्लोक का अर्थ नहीं।",
    },
    "18": {
        "frame": "क्रिया: वर्जयेत् (छोड़े) · पंक्ति १ के कर्म: स्त्रियों के साथ एकान्त में रहना, परिहास · पंक्ति २: छोड़े जाने वाले रोगियों की सूची शुरू (आगे चलती है)।",
        "diagram": {"groups": [
            {"label": "स्त्रियों के साथ वर्जित", "items": ["रहसि स्थानं", "परिहासं"]},
            {"label": "सूची शुरू (पंक्ति २)", "items": ["आर्त्तं", "नृपसद्वैद्यैर्द्विष्टं"]}]},
        "sandhi": "नृप + सत् + वैद्यैः + द्विष्टम् → नृपसद्वैद्यैर्द्विष्टम् (त् → द् व से पहले; ः → र् द से पहले)। नारीभिः + च → नारीभिश्च (ः → श्)।",
        "chunks": "नारीभिश्च रहसि | स्थानं परिहासं च वर्जयेत् ‖ आर्त्तं च नृपसद्वैद्यैः | द्विष्टं तद्वेषिणं द्विषं।",
        "anchors": "रहसि = एकान्त में · परिहास = हँसी-मज़ाक · द्विष्ट ← द्विष् (द्वेष करना) का भूत-कृदन्त = द्वेष किया गया।",
    },
    "19": {
        "diagram": {"groups": [
            {"label": "पंक्ति १", "items": ["चंडं", "शोकातुरं", "भीरुं", "कृतघ्नं", "वैद्यमानिनं"]},
            {"label": "पंक्ति २", "items": ["हीनोपकरणं", "व्यग्रं", "अविधेयं", "गतायुषं"]}]},
        "anchors": "चण्ड = उग्र · शोकातुर = शोक + आतुर (पीड़ित) · भीरु = डरपोक · कृतघ्न = किए (उपकार) को मिटाने वाला · वैद्यमानी = अपने को वैद्य मानने वाला · अविधेय = जिसे आज्ञा में न रखा जा सके · गतायुष = जिसकी आयु जा चुकी।",
        "sandhi": "हीन + उपकरणम् → हीनोपकरणम् (अ + उ → ओ) · गत + आयुषम् → गतायुषम् (अ + आ → आ) · व्यग्रम् + अविधेयम् जुड़कर ‘व्यग्रमविधेयं’।",
        "chunks": "चंडं शोकातुरं भीरुं | कृतघ्नं वैद्यमानिनं ‖ हीनोपकरणं व्यग्रम् | अविधेयं गतायुषं।",
        "pegs": "मेरा बनाया चित्र: नौ मुखौटे एक कतार में: गुस्सैल, रोता, काँपता, मुँह फेरता, ‘डॉक्टर’ टोपी पहने, खाली झोला, घबराया, आज्ञा न मानता, घड़ी रुकी हुई। (केवल याद के लिए; श्लोक का वर्णन नहीं।)",
    },
    "20": {
        "frame": "कौन: जीने की इच्छा वाला रोगी भी · क्या: उन वैद्यों से बचे जो पूर्वोक्त गुणों से रहित हैं और चिकित्सा बेचते हैं · क्यों: वे मृत्यु के आगे चलने वाले हैं।",
        "diagram": {"steps": ["जिजीविषुः व्याधितोऽपि", "वैद्यान् (वर्जित)", "पूर्वोक्तगुणवर्जितान् · क्रियाविक्रयिणः", "मृत्योरग्रेसरा हि ते"]},
        "sandhi": "जिजीविषुः + व्याधितः + अपि → जिजीविषुर्व्याधितोऽपि (ः → र् व से पहले; अः + अ → ोऽ) · वैद्यान् + मृत्योः → वैद्यान्मृत्योः · मृत्योः + अग्रेसराः → मृत्योरग्रेसराः।",
        "anchors": "जिजीविषु = जीने की इच्छा करने वाला · विक्रयिन् = बेचने वाला · अग्रेसर = आगे चलने वाला (अग्र + सर)।",
        "chunks": "जिजीविषुर्व्याधितोऽपि | पूर्वोक्तगुणवर्जितान् ‖ क्रियाविक्रयिणो वैद्यान् | मृत्योरग्रेसरा हि ते।",
    },
    "21": {
        "diagram": {"groups": [
            {"label": "चिकित्सा के चार पाद", "items": ["भिषक्", "द्रव्याणि", "उपस्थाता", "रोगी"]}]},
        "frame": "क्या: चिकित्सा के चार पाद · कौन-से: वैद्य, औषधियाँ, परिचारक, रोगी · हर एक: चार गुणों वाला (गुण अगले श्लोकों में)।",
        "pegs": "मेरा बनाया चित्र: चार पैरों वाली मेज़ (चिकित्सा); पैरों पर नाम: वैद्य, औषध, परिचारक, रोगी; एक पैर टूटा तो मेज़ डगमगाए। (श्लोक में टूटे पैर की बात नहीं; पाद = पैर का चित्र मेरा है।)",
        "sandhi": "द्रव्याणि + उपस्थाता → द्रव्याण्युपस्थाता (इ → य् उ से पहले) · तत् + चतुर्गुणम् → तच्चतुर्गुणम् (त् + च → च्च)।",
        "chunks": "भिषक् द्रव्याण्युपस्थाता | रोगी पादचतुष्टयं ‖ चिकित्सितस्य निर्दिष्टं | प्रत्येकं तच्चतुर्गुणं।",
        "anchors": "भिषक् = वैद्य · उपस्थाता = पास खड़ा रहने वाला, परिचारक · पाद = चरण/चौथाई · चतुष्टय = चार का समूह।",
    },
    "22": {
        "diagram": {"groups": [
            {"label": "वैद्य के चार गुण", "items": ["दक्षः", "तीर्थात्तशास्त्रार्थः", "दृष्टकर्मा", "शुचिः"]},
            {"label": "औषध के चार गुण", "items": ["बहुकल्पं", "बहुगुणं", "संपन्नं", "योग्यं"]}]},
        "frame": "पंक्ति १: वैद्य के चार गुण · पंक्ति २: औषध के चार गुण · अगली इकाई: परिचारक और रोगी के चार-चार गुण।",
        "sandhi": "दक्षः + तीर्थात् → दक्षस्तीर्थात् · तीर्थात् + आत्त → तीर्थात्त (वही रूप तीर्थ + आत्त का भी) · शुचिः + भिषक् → शुचिर्भिषक् · योग्यम् + औषधम् → योग्यमौषधम्।",
        "chunks": "दक्षस्तीर्थात्तशास्त्रार्थो | दृष्टकर्मा शुचिर्भिषक् ‖ बहुकल्पं बहुगुणं | संपन्नं योग्यमौषधं।",
        "puns": "केवल सुनने की सहायता (मेरी बनाई): ‘दृष्टकर्मा’ = ‘दृष्टि + कर्म’: जिसने काम आँख से देखा है। यह याद करने की युक्ति है।",
    },
    "23": {
        "diagram": {"groups": [
            {"label": "परिचारक के चार गुण", "items": ["अनुरक्तः", "शुचिः", "दक्षः", "बुद्धिमान्"]},
            {"label": "रोगी के चार गुण", "items": ["आढ्यः", "भिषग्वश्यः", "ज्ञापकः", "सत्त्ववान्"]}]},
        "contrast": "‘शुचि’ और ‘दक्ष’ पिछले श्लोक में वैद्य के गुण थे, यहाँ परिचारक के हैं। ‘आढ्य’ (धनवान्) केवल रोगी का गुण है, ‘अनुरक्त’ केवल परिचारक का।",
        "sandhi": "शुचिः + दक्षः → शुचिर्दक्षः (ः → र् द से पहले; फिर दक्षः → दक्षो) · भिषक् + वश्यः → भिषग्वश्यः (क् → ग्) · सत्त्ववान् + अपि → सत्त्ववानपि।",
        "chunks": "अनुरक्तः शुचिर्दक्षो | बुद्धिमान्परिचारकः ‖ आढ्यो रोगी भिषग्वश्यो | ज्ञापकः सत्त्ववानपि।",
    },
    "24": {
        "frame": "यत् (क्योंकि) १: वैद्य गुणहीन हो तो गुणवान् पाद भी बेकार · यत् २: गुणवान् वैद्य पादहीन रोगियों को भी चला ले · निष्कर्ष: अगली इकाई।",
        "diagram": {"groups": [
            {"label": "कारण १ (पंक्ति १)", "items": ["वैद्ये विगुणे", "पादाः", "गुणवन्तोऽपि", "अनर्थकाः"]},
            {"label": "कारण २ (पंक्ति २)", "items": ["गुणवान्", "पादहीनान्", "आर्त्तान् अपि", "यापयेत्"]}]},
        "contrast": "वैद्य गुणहीन: गुणवान् पाद भी अनर्थक ↔ वैद्य गुणवान्: पादहीन रोगी भी चल जाए। दोनों कारण वैद्य की प्रधानता दिखाते हैं।",
        "sandhi": "यत् + वैद्ये → यद्वैद्ये (त् → द्) · गुणवन्तः + अपि + अनर्थकाः → गुणवन्तोऽप्यनर्थकाः (अः + अ → ोऽ; इ → य् अ से पहले)।",
        "chunks": "यद्वैद्ये विगुणे पादा | गुणवंतोऽप्यनर्थकाः ‖ सपादहीनानप्यार्त्तान् | गुणवान् यच्च यापयेत्।",
    },
    "25": {
        "diagram": {"steps": ["वैद्य ही चिकित्सा का प्रधान कारण (अतः)", "व्याधि द्विधा: साध्य · असाध्य", "तौ तु पुनर्द्विधा (प्रत्येक दो प्रकार का)"]},
        "frame": "निष्कर्ष: इसलिए वैद्य ही प्रधान कारण · विभाजन: रोग = साध्य/असाध्य; ये दोनों फिर दो-दो प्रकार के (चारों नाम अगली इकाई में)।",
        "sandhi": "साध्यः + असाध्यः + इति → साध्योऽसाध्य इति (मुद्रित: साध्योऽसाध्यइति) · व्याधिः + द्विधा → व्याधिर्द्विधा · पुनः + द्विधा → पुनर्द्विधा · तम् + एव + अतः → तमेवातः।",
        "chunks": "चिकित्सायास्तमेवातः | प्रधानं कारणं विदुः ‖ साध्योऽसाध्यइति व्याधिः | द्विधा तौ तु पुनर्द्विधा।",
        "anchors": "प्रधान = मुख्य · कारण = कारण/साधन · साध्य = जो सिद्ध/ठीक किया जा सके · द्विधा = दो प्रकार से · विदुः = वे जानते हैं (विद् का रूप)।",
    },
    "26": {
        "diagram": {"groups": [
            {"label": "चार रोग (पंक्ति १)", "items": ["सुसाध्यः", "कृच्छ्रसाध्यः", "याप्यः", "अनुपक्रमः"]}]},
        "frame": "क्या: रोग के चार भेद · नाम: सुसाध्य, कृच्छ्रसाध्य, याप्य, अनुपक्रम · पंक्ति २: एक वाक्य का आरम्भ (शरीर सब औषधियाँ सहे, युवा, आत्म-संयमी); पूरा अगली इकाई में।",
        "contrast": "सुसाध्य (आसानी से) ↔ कृच्छ्रसाध्य (कठिनाई से) ↔ याप्य (टिकाने योग्य) ↔ अनुपक्रम (कोई उपाय नहीं): चारों की जोड़ियाँ मेरी याद के लिए सजाई हैं, श्लोक ने केवल नाम दिए हैं।",
        "sandhi": "कृच्छ्रसाध्यः + च → कृच्छ्रसाध्यश्च (ः → श्) · यः + च + अनुपक्रमः → यश्चानुपक्रमः · सर्व + औषध + क्षमे → सर्वौषधक्षमे (अ + औ → औ)।",
        "chunks": "सुसाध्यः कृच्छ्रसाध्यश्च | याप्यो यश्चानुपक्रमः ‖ सर्वौषधक्षमे देहे | यूनः पुंसो जितात्मनः।",
    },
}


IMAGE_SPECS = {
    ("19", "diagram"): {
        "file": "ch2b02-varjya-19.svg",
        "alt": "Mind map: nine descriptions of a patient in verse order: fierce, stricken with grief, timid, ungrateful, one who thinks himself a physician, lacking equipment, agitated, disobedient, whose life is spent",
        "type": "mermaid",
        "code": ('mindmap\n  रोगी के नौ विशेषण\n    चंडं\n    शोकातुरं\n    भीरुं\n'
                 '    कृतघ्नं\n    वैद्यमानिनं\n    हीनोपकरणं\n    व्यग्रं\n'
                 '    अविधेयं\n    गतायुषं'),
    },
    ("21", "diagram"): {
        "file": "ch2b02-pada-21.svg",
        "alt": "Mind map: the four quarters (pada) of treatment: physician, medicines, attendant, patient",
        "type": "mermaid",
        "code": 'mindmap\n  चिकित्सा के चार पाद\n    भिषक्\n    द्रव्याणि\n    उपस्थाता\n    रोगी',
    },
    ("22", "diagram"): {
        "file": "ch2b02-vaidya-aushadha-22.svg",
        "alt": "Two columns: the four qualities of the physician (skilled, took the treatises' meaning from a teacher, has seen the work, pure) and the four qualities of the medicine (many preparations, many qualities, well endowed, suitable)",
        "type": "split",
        "title": "श्लोक २२: वैद्य और औषध के चार-चार गुण",
        "cols": [["वैद्य", ["दक्षः", "तीर्थात्तशास्त्रार्थः", "दृष्टकर्मा", "शुचिः"]],
                 ["औषध", ["बहुकल्पं", "बहुगुणं", "संपन्नं", "योग्यं"]]],
    },
    ("23", "diagram"): {
        "file": "ch2b02-paricharaka-rogi-23.svg",
        "alt": "Two columns: the four qualities of the attendant (devoted, pure, skilled, intelligent) and the four of the patient (wealthy, obedient to the physician, able to make known, having mental strength)",
        "type": "split",
        "title": "श्लोक २३: परिचारक और रोगी के चार-चार गुण",
        "cols": [["परिचारक", ["अनुरक्तः", "शुचिः", "दक्षः", "बुद्धिमान्"]],
                 ["रोगी", ["आढ्यः", "भिषग्वश्यः", "ज्ञापकः", "सत्त्ववान्"]]],
    },
    ("25", "diagram"): {
        "file": "ch2b02-vyadhi-25.svg",
        "alt": "Flowchart: disease is twofold, curable and incurable; each of these two is again twofold",
        "type": "mermaid",
        "code": ('flowchart TD\n  A["व्याधि द्विधा"] --> B["साध्य"]\n  A --> C["असाध्य"]\n'
                 '  B --> D["फिर दो प्रकार"]\n  C --> E["फिर दो प्रकार"]'),
    },
    ("26", "diagram"): {
        "file": "ch2b02-sadhya-26.svg",
        "alt": "Mind map: the four classes of disease named in verse 26: easily curable, curable with difficulty, to be sustained, without remedy",
        "type": "mermaid",
        "code": 'mindmap\n  रोग के चार भेद\n    सुसाध्यः\n    कृच्छ्रसाध्यः\n    याप्यः\n    अनुपक्रमः',
    },
}
