from helpers import mcq, match, order, fill, multi, accepts

AUTHORED = {}

# ---------------------------------------------------------------- unit 40
AUTHORED["40"] = {
    "title": "ईक्ष्वाकुस्तु विशेषेण",
    "question": "In which ailments does unit 40 say ikṣvāku is especially to be applied?",
    "rule": ("Ikṣvāku (bitter bottle gourd, probable) is especially to be applied (योज्यः) in kāsa (cough), śvāsa "
             "(breath-trouble), jvara (fever), chardi (vomiting), viṣa (poison) and phlegm-ailments."),
    "limits": ("Whether -roga covers every member or only śleṣma is open. The text does not say bitter; the identification "
               "(Lagenaria siceraria) is probable. The printed long ī is a variant or misprint, not questioned. No dose is given."),
    "explain_hi": ("यहाँ से इक्ष्वाकु यानी कड़वी लौकी (सम्भावित पहचान) के वमन-योग शुरू होते हैं। "
                   "‘तु’ इसे पिछले द्रव्य जीमूतक से अलग करता है: इक्ष्वाकु तो विशेष रूप से इन रोगों में लगाया जाए। "
                   "सूची है: कास यानी खाँसी, श्वास यानी साँस फूलना, ज्वर यानी बुखार, छर्दि यानी उल्टी, विष और कफ के रोग। "
                   "‘योज्यः’ का अर्थ है ‘प्रयोग करने योग्य’; यह पुंलिङ्ग इक्ष्वाकुः से मेल खाता है। "
                   "पाठ ‘कड़वी’ नहीं कहता; कड़वी लौकी की पहचान सम्भावित है।"),
    "hook": "खाँसी, साँस, बुखार, उल्टी, विष, कफ: इन छह में इक्ष्वाकु विशेष।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "Which drug does unit 40 say is especially to be applied in cough, fever and vomiting?",
            ("Ikṣvāku, probably the bitter bottle gourd", "ईक्ष्वाकुस्तु विशेषेण … योज्यः: ikṣvāku is especially to be applied."),
            [("Madana, the emetic nut fruit", "Madana is the drug of the earlier sections, not of this unit."),
             ("Kuṭaja (vatsaka)", "Kuṭaja is not named in this unit."),
             ("Jīmūtaka, probably the bitter luffa", "Jīmūtaka is the drug of the section before; this unit turns to ikṣvāku.")],
            "Unit 40 opens the ikṣvāku section: ikṣvāku is especially to be applied in these ailments.",
            "इक्ष्वाकु = bitter bottle gourd (probable); विशेषेण = especially; योज्यः = to be applied."),
        order(1, "Put the ailments of unit 40 in the order of the text.",
              ["कास", "श्वास", "ज्वर", "छर्दि", "विष", "श्लेष्मरोग"],
              "कासश्वासज्वरच्छर्दिविषश्लेष्मरोगेषु: cough, breath-trouble, fever, vomiting, poison, phlegm-ailments.",
              "कास · श्वास · ज्वर · छर्दि · विष · श्लेष्मरोग."),
        match(2, "Match each ailment of unit 40 to its meaning.",
              [["कास", "cough"], ["श्वास", "breath-trouble (dyspnoea)"], ["ज्वर", "fever"], ["छर्दि", "vomiting"]],
              "The first four members of the compound, with the standard equivalents the card gives.",
              "कास = cough; श्वास = breathlessness; ज्वर = fever; छर्दि = vomiting.",
              role="extend",
              teaches="कास = cough, श्वास = breath-trouble (dyspnoea), ज्वर = fever, छर्दि = vomiting (standard equivalents)."),
        mcq("discriminate", 3, "Which is the right split of ज्वरच्छर्दि inside the compound of unit 40?",
            ("ज्वर + छर्दि", "After a short vowel, छ is written च्छ: ज्वर + छर्दि → ज्वरच्छर्दि."),
            [("ज्वर + च्छर्दि", "There is no word च्छर्दि; the च् is added by sandhi before छ."),
             ("ज्वरः + छर्दि", "Visarga before छ becomes श्: that would give ज्वरश्छर्दि."),
             ("ज्वरम् + छर्दि", "Final म् before छ becomes anusvara: that would give ज्वरंछर्दि.")],
            "ज्वर (fever) + छर्दि (vomiting): after a short vowel छ doubles to च्छ.",
            "Short vowel + छ → च्छ (ज्वर + छर्दि → ज्वरच्छर्दि)."),
        mcq("apply", 4, "A patient has vomiting and the effects of poison. Does unit 40 name ikṣvāku for him?",
            ("Yes: both chardi and viṣa are named", "छर्दि and विष both stand in the list of unit 40."),
            [("No: only cough and fever are named", "The list has six members, chardi and viṣa among them."),
             ("Only for poison, not for vomiting", "छर्दि (vomiting) is named in the same list."),
             ("Only for vomiting, not for poison", "विष (poison) is named in the same list.")],
            "Chardi (vomiting) and viṣa (poison) are both in the list of unit 40.",
            "कास, श्वास, ज्वर, छर्दि, विष, श्लेष्मरोग: all six are named."),
        mcq("transfer", 5, "योज्यः agrees with the masculine इक्ष्वाकुः. Which form fits a new sentence about oil: तैलं कासे ____?",
            ("योज्यम्", "तैल is neuter singular, so the gerundive is योज्यम्."),
            [("योज्यः", "योज्यः is masculine; तैलम् is neuter."),
             ("योज्या", "योज्या is feminine singular."),
             ("योज्याः", "योज्याः is masculine or feminine plural.")],
            "A gerundive (to be applied) takes the gender and number of its noun: इक्ष्वाकुः योज्यः, तैलं योज्यम्.",
            "Gerundive agrees with its noun: m. योज्यः, n. योज्यम्, f. योज्या.",
            teaches="योज्य (to be applied, √युज्) agrees with its noun: इक्ष्वाकुः योज्यः (m.), तैलं योज्यम् (n.)."),
    ],
}

# ---------------------------------------------------------------- unit 41
AUTHORED["41"] = {
    "title": "तस्यापुष्पफलस्य प्रवालैः",
    "question": "Which part of ikṣvāku goes into milk in unit 41, at what stage, and for whom?",
    "rule": ("The sprouts (प्रवाल) of ikṣvāku, taken while it is without flower and fruit, go into milk (boiled, by the data's "
             "correction), for one whose Pitta is excessive and in fever of Pitta and Kapha."),
    "limits": ("Low confidence. Printed श्रुतं ('heard') is read as śṛtam (boiled): not questioned. The last clause "
               "(flowers and the rest, applied like rātajīmūta) has an unclear word and is not questioned. "
               "अपुष्पफल may also mean not yet flowered or fruited. 'That one' (तस्य) is ikṣvāku by the order of the text."),
    "explain_hi": ("‘तस्य’ यानी उसका, पाठ-क्रम से इक्ष्वाकु का। "
                   "जब पौधा फूल और फल से रहित हो (अपुष्पफल), तब उसके प्रवाल यानी नए पल्लव दूध के साथ लिए जाते हैं; डेटा छपे ‘श्रुतं’ को ‘शृतम्’ (उबाला हुआ) पढ़ता है। "
                   "यह दूध उस रोगी के लिए है जिसका पित्त बढ़ा हुआ हो (उद्रिक्तपित्त), और पित्त-कफ के ज्वर में। "
                   "अन्त में फूल आदि के प्रयोग किसी और द्रव्य के समान बताए गए हैं, पर वह शब्द (रातजीमूत) अस्पष्ट है।"),
    "hook": "फूल-फल से पहले के कोमल पत्ते, दूध में: बढ़े पित्त और पित्त-कफ ज्वर के लिए।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "Which part of ikṣvāku is taken with milk in unit 41?",
            ("Its sprouts (प्रवाल)", "प्रवालैः = with the sprouts."),
            [("Its fresh roots (मूल)", "Roots are not named in this unit."),
             ("Its seeds (बीज)", "Seeds come in line 05.01.48, not here."),
             ("Its bark (त्वक्)", "Bark is not named in this unit.")],
            "The milk is prepared with the sprouts of the plant while it bears no flower or fruit.",
            "प्रवाल = sprout, young shoot."),
        match(1, "Match each word of unit 41 to its meaning.",
              [["प्रवाल", "sprout"], ["क्षीर", "milk"], ["अपुष्पफल", "without flower and fruit"],
               ["उद्रिक्तपित्त", "one whose Pitta is excessive"]],
              "The part used, the liquid, the stage of the plant and the patient.",
              "प्रवाल = sprout; क्षीर = milk; अपुष्पफल = flowerless and fruitless; उद्रिक्तपित्त = with excessive Pitta."),
        mcq("extend", 2, "At what stage of the plant are the sprouts of unit 41 taken?",
            ("When it has no flower or fruit", "अपुष्पफलस्य = of that (plant) without flower and fruit."),
            [("When its fruit is fully ripe", "Ripe fruit is the opposite of अपुष्पफल."),
             ("When it is dried in the sun", "Drying is not named in this unit."),
             ("When it is in full flower", "अ-पुष्प means without flower.")],
            "अपुष्पफल is a bahuvrīhi: (the plant) that has no flower and no fruit.",
            "अ- (not) + पुष्प-फल (flower and fruit) = without flower and fruit.",
            teaches="अपुष्पफल = without flower and fruit: the sprouts of unit 41 are taken while the plant bears no flower or fruit (it may also mean not yet flowered)."),
        mcq("discriminate", 3, "Which is the right split of क्षीरमुद्रिक्तपित्ते?",
            ("क्षीरम् + उद्रिक्तपित्ते", "Final म् joins the next vowel in writing: क्षीरम् + उ… → क्षीरमु…."),
            [("क्षीरम् + मुद्रिक्तपित्ते", "There is no word मुद्रिक्त; म् + म would be written क्षीरम्मुद्रिक्त."),
             ("क्षीरः + उद्रिक्तपित्ते", "क्षीर is neuter (क्षीरम्); अः before उ would give क्षीर उद्रिक्त…."),
             ("क्षीरा + उद्रिक्तपित्ते", "आ + उ would give ओ: क्षीरोद्रिक्त….")],
            "क्षीरम् (milk) + उद्रिक्तपित्ते (in one whose Pitta is excessive).",
            "Final म् before a vowel is written joined: क्षीरम् + उद्रिक्त → क्षीरमुद्रिक्त."),
        multi("apply", 4, "For which two states does unit 41 name the sprout milk?",
              [("Excessive Pitta", "Right: उद्रिक्तपित्ते = in one whose Pitta is excessive."),
               ("Fever of Pitta and Kapha", "Right: पित्तकफज्वरे = in fever of Pitta and Kapha."),
               ("Fever of Vāta alone", "Wrong: Vāta is not named in this unit."),
               ("Goitre and tumour", "Wrong: these come in line 05.01.48, not here.")],
              [0, 1],
              "The milk is for one with excessive Pitta and for Pitta-Kapha fever.",
              "उद्रिक्तपित्ते · पित्तकफज्वरे."),
        mcq("transfer", 5, "उद्रिक्तपित्ते means in one whose Pitta is excessive. What does a new word उद्रिक्तकफे mean?",
            ("In one whose Kapha is excessive", "Same bahuvrīhi: उद्रिक्त (excessive) + कफ, locative."),
            [("In one whose Kapha is lost", "Lost would be क्षीणकफ; उद्रिक्त is excessive."),
             ("In one whose Pitta is calmed", "The new word names Kapha, and उद्रिक्त is not calmed."),
             ("For the full removal of all Kapha", "Removal would be कफहर; this is a locative of the patient.")],
            "उद्रिक्त + दोष as a bahuvrīhi = the one whose doṣa is excessive.",
            "उद्रिक्तपित्त / उद्रिक्तकफ = one whose Pitta / Kapha is excessive.",
            teaches="उद्रिक्त + doṣa is a bahuvrīhi for the patient: उद्रिक्तपित्त (excessive Pitta), उद्रिक्तकफ (excessive Kapha)."),
    ],
}

# ---------------------------------------------------------------- unit 42
AUTHORED["42"] = {
    "title": "इक्ष्वाकुफलस्वरसं वा",
    "question": "What does the patient of unit 42 drink, prepared how, and in which conditions?",
    "rule": ("Or the patient desiring emesis drinks the expressed juice of the ikṣvāku fruit prepared in threefold milk, "
             "in Pitta, in kapha-pīnasa (chronic nasal catarrh) and in svarasāda (hoarseness)."),
    "limits": ("Threefold milk is the plain sense; the exact measure is not stated. पिबेत is a middle optative, kept as "
               "printed. No dose is given."),
    "explain_hi": ("एक और योग: इक्ष्वाकु के फल का स्वरस, यानी ताज़ा निचोड़ा रस। "
                   "उसे तिगुने दूध में तैयार किया जाता है (त्रिगुणक्षीरसाधित); ठीक माप पाठ नहीं बताता। "
                   "वमन चाहने वाला रोगी (वमनार्थी आतुरः) इसे पिए। "
                   "दशाएँ हैं: पित्त, कफ-पीनस यानी पुराना जुकाम, और स्वरसाद यानी आवाज़ बैठना।"),
    "hook": "रस तिगुने दूध में: पित्त, जुकाम और बैठी आवाज़ वाले वमनार्थी के लिए।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "What does the patient of unit 42 drink?",
            ("Fruit juice cooked in threefold milk", "इक्ष्वाकुफलस्वरसं … त्रिगुणक्षीरसाधितम् … पिबेत."),
            [("The ikṣvāku seeds in she-goat's milk", "Seeds in goat's milk come in line 05.01.48."),
             ("Fruit paste taken with meat broth", "Paste with meat broth comes in line 05.01.55."),
             ("Plain fruit oil taken with honey", "Oil comes in line 05.01.53, and honey is not named here.")],
            "The expressed juice of the ikṣvāku fruit, prepared in threefold milk, is drunk.",
            "स्वरस = expressed juice; त्रिगुणक्षीरसाधित = prepared in threefold milk."),
        order(1, "Put these parts of unit 42 in the order of the text.",
              ["इक्ष्वाकुफलस्वरसम्", "त्रिगुणक्षीरसाधितम्", "आतुरः", "पित्ते कफपीनसे स्वरसादे", "वमनार्थी पिबेत"],
              "The juice, how it is prepared, who drinks, in which conditions, and the verb.",
              "स्वरसं वा · त्रिगुणक्षीरसाधितम् · आतुरः · पित्ते कफपीनसे स्वरसादे · वमनार्थी पिबेत."),
        match(2, "Match each word of unit 42 to its meaning.",
              [["कफपीनस", "chronic nasal catarrh"], ["स्वरसाद", "hoarseness, loss of voice"],
               ["वमनार्थी", "one desiring emesis"], ["आतुर", "the patient"]],
              "Two conditions and the two words for the one who drinks.",
              "कफपीनस = Kapha-type catarrh; स्वरसाद = failing voice; वमनार्थी = desiring emesis; आतुर = patient.",
              role="extend",
              teaches="कफपीनस = chronic nasal catarrh, स्वरसाद = hoarseness (standard); वमनार्थी = desiring emesis; आतुर = patient."),
        mcq("discriminate", 3, "Which English rendering of unit 42 has one wrong word?",
            ("The patient desiring purgation should drink it", "Wrong: वमनार्थी is desiring emesis (vomiting), not purgation."),
            [("The patient desiring emesis should drink it", "Correct: वमनार्थी = desiring emesis."),
             ("The patient wanting to vomit should drink it", "Correct: emesis is vomiting."),
             ("The sick man seeking emesis should drink it", "Correct: आतुर = the sick man, the patient.")],
            "वमन = emesis; विरेचन would be purgation, a different procedure.",
            "वमनार्थी = वमन + अर्थी = one desiring emesis."),
        mcq("apply", 4, "A patient with hoarseness wants to vomit. In what is the ikṣvāku juice of unit 42 prepared?",
            ("In threefold milk", "त्रिगुणक्षीरसाधितम् = prepared in threefold milk."),
            [("In whey (मस्तु)", "Whey goes with the fruit in line 05.01.50."),
             ("In meat broth", "Meat broth goes with the paste in line 05.01.55."),
             ("In buttermilk (तक्र)", "Buttermilk is named in line 05.01.51, not here.")],
            "For svarasāda the juice is prepared in threefold milk and drunk by the one desiring emesis.",
            "त्रि-गुण-क्षीर = threefold milk; साधित = prepared."),
        mcq("transfer", 5, "वमनार्थी means one desiring emesis. What does a new word विरेचनार्थी mean?",
            ("One desiring purgation", "विरेचन (purgation) + अर्थी (desiring)."),
            [("One who has been purged", "That would be विरिक्त; -अर्थी is desiring."),
             ("One who fears purgation", "Fearing would need -भीरु; -अर्थी is desiring."),
             ("A drug that causes purging", "A drug would be विरेचन itself, not -अर्थी.")],
            "-अर्थी after a noun = one who desires it.",
            "X + अर्थी = one desiring X: वमनार्थी, विरेचनार्थी.",
            teaches="-अर्थी after a noun means 'one desiring it': वमनार्थी (desiring emesis), विरेचनार्थी (desiring purgation)."),
    ],
}

# ---------------------------------------------------------------- unit 43 (verse)
AUTHORED["43"] = {
    "title": "जीर्णे वा समुद्धृतबीजे फले",
    "question": "How is the curd of verse 43 made inside the fruit?",
    "rule": ("Or pour milk into an old fruit whose seeds are taken out; the curd formed in it is for phlegm-cough and the "
             "other ailments named."),
    "limits": ("The fruit is ikṣvāku by the order of the text. The ailment compound has a likely misprint (श्वासु- for "
               "श्वासा-, at the śvāsa-aruci joint): the list is not questioned. No time for the curd to form and no dose are given."),
    "explain_hi": ("यह अनोखी विधि फल को ही बरतन बनाती है। "
                   "पुराना (जीर्ण) फल लें, उसके बीज निकाल दें (समुद्धृतबीज), और उसमें दूध डालें (प्रक्षिपेत्)। "
                   "उसी में बना दही (तत्र जातं दधि) कफ की खाँसी, साँस, अरुचि और उल्टी में दिया जाता है। "
                   "रोगों वाले समास में एक छपाई-दोष है, इसलिए उस सूची पर प्रश्न नहीं बना।"),
    "hook": "पुराना फल, बीज बाहर, दूध अन्दर: फल में ही जमा दही।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "Into what does verse 43 have milk poured?",
            ("An old fruit, its seeds taken out", "जीर्णे … समुद्धृतबीजे फले क्षीरं प्रक्षिपेत्."),
            [("A fresh fruit, with its seeds kept in", "The fruit is old (जीर्ण) and the seeds are taken out."),
             ("A clay pot holding the sprouts", "No pot or sprouts are named in this verse."),
             ("A hollow root of the same plant", "No root is named in this verse.")],
            "Milk is poured into an old fruit from which the seeds have been taken out.",
            "जीर्ण = old; समुद्धृतबीज = with seeds taken out; प्रक्षिपेत् = should pour in."),
        order(1, "Put these phrases of verse 43 in the order of the text.",
              ["जीर्णे वा", "समुद्धृतबीजे फले", "क्षीरं प्रक्षिपेत्", "तत्र जातं दधि"],
              "Old fruit, seeds taken out, milk poured in, curd formed there.",
              "जीर्णे वा · समुद्धृतबीजे फले · क्षीरं प्रक्षिपेत् · तत्र जातं दधि."),
        match(2, "Match each word of verse 43 to its meaning.",
              [["जीर्ण", "old"], ["समुद्धृतबीज", "with the seeds taken out"], ["प्रक्षिपेत्", "should pour in"],
               ["जात", "formed"]],
              "The state of the fruit, what is removed, what is done, and what happens to the milk.",
              "जीर्ण = old; समुद्धृतबीज = seeds taken out; प्रक्षिपेत् = should pour in; जात = formed (√जन्).",
              role="extend",
              teaches="Verse 43: जीर्ण = old, समुद्धृतबीज = whose seeds are taken out, प्रक्षिपेत् = should pour in, जात = formed."),
        mcq("discriminate", 3, "Where does the curd of verse 43 form?",
            ("Inside the fruit itself", "तत्र जातं दधि = the curd formed there, in the fruit."),
            [("In a copper vessel", "No vessel is named; तत्र points to the fruit."),
             ("In a separate pot of whey", "Whey is not named in this verse."),
             ("In the patient's belly", "तत्र refers to the fruit just named, not the belly.")],
            "तत्र (there) takes up the fruit into which the milk was poured.",
            "तत्र = there, in it (the fruit)."),
        mcq("apply", 4, "A helper has a fresh fruit with its seeds inside. What must differ for the method of verse 43?",
            ("It must be old, with seeds removed", "जीर्णे … समुद्धृतबीजे: old, and with the seeds taken out."),
            [("It must be boiled and powdered", "Neither boiling nor powdering is named here."),
             ("It must be soaked in goat's milk", "Goat's milk belongs to the seeds of line 05.01.48."),
             ("It must be dried and then dusted", "Drying and dusting are not named in this verse.")],
            "The text asks for an old fruit from which the seeds have been taken out.",
            "जीर्ण + समुद्धृतबीज: the two conditions of the fruit."),
        mcq("transfer", 5, "जातम् agrees with the neuter दधि. Which form fits a new phrase with the feminine पेया: तत्र ____ पेया?",
            ("जाता", "पेया is feminine singular, so the participle is जाता."),
            [("जातम्", "जातम् is neuter, like दधि; पेया is feminine."),
             ("जातः", "जातः is masculine singular."),
             ("जाताः", "जाताः is plural; पेया is singular.")],
            "The past participle takes the gender and number of its noun: दधि जातम्, पेया जाता.",
            "Participle agrees with its noun: n. जातम्, f. जाता, m. जातः.",
            teaches="जात (formed, √जन्) agrees with its noun: दधि जातम् (n.), पेया जाता (f.)."),
    ],
}

# ---------------------------------------------------------------- unit 44
AUTHORED["44"] = {
    "title": "इक्ष्वाकुबीजानि वा",
    "question": "In what are the ikṣvāku seeds of unit 44 soaked, and for which ailments?",
    "rule": ("Or ikṣvāku seeds soaked in she-goat's milk, in poison, gulma, udara, goitre, nodular swelling, tumour and "
             "filariasis."),
    "limits": ("The unit has no verb; the use is understood. Modern equivalents are standard (data): gulma = abdominal lump, "
               "galagaṇḍa = goitre, granthi = nodular swelling, arbuda = tumour, ślīpada = filariasis; udara here is an "
               "ailment term. No dose is given."),
    "explain_hi": ("इस योग में इक्ष्वाकु के बीज बकरी के दूध में भिगोए (भावित) जाते हैं। "
                   "रोग हैं: विष, गुल्म यानी पेट की गाँठ, उदर यानी पेट का बढ़ना, गलगण्ड यानी घेंघा, ग्रन्थि यानी गाँठ, अर्बुद यानी रसौली और श्लीपद यानी हाथीपाँव। "
                   "ये अधिकतर गाँठ और सूजन वाले रोग हैं। "
                   "इकाई में क्रिया नहीं; प्रयोग पिछली पंक्तियों से समझा जाता है।"),
    "hook": "बकरी के दूध में भीगे बीज: गाँठ, घेंघा, रसौली और हाथीपाँव पर।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In what are the ikṣvāku seeds of unit 44 soaked?",
            ("She-goat's milk", "छागीक्षीरभावितानि = soaked in she-goat's milk."),
            [("Cow's urine (गोमूत्र)", "Cow's urine is not named in this unit."),
             ("Honey water", "Honey is not named in this unit."),
             ("Rice water", "Rice water is not named in this unit.")],
            "The seeds are soaked in the milk of a she-goat (छागी).",
            "छागी = she-goat; क्षीर = milk; भावित = soaked."),
        order(1, "Put these ailments of unit 44 in the order of the text.",
              ["गुल्म", "उदर", "गलगण्ड", "ग्रन्थि", "अर्बुद", "श्लीपद"],
              "विषगुल्मोदरगलगण्डग्रन्थ्यर्बुदश्लीपदेषु: after poison come these six in this order.",
              "विष · गुल्म · उदर · गलगण्ड · ग्रन्थि · अर्बुद · श्लीपद."),
        match(2, "Match each ailment of unit 44 to its modern equivalent.",
              [["गुल्म", "abdominal lump"], ["गलगण्ड", "goitre"], ["अर्बुद", "tumour"],
               ["श्लीपद", "filariasis (elephantiasis)"]],
              "The standard equivalents given in the unit data.",
              "गुल्म = abdominal lump; गलगण्ड = goitre; अर्बुद = tumour; श्लीपद = filariasis.",
              role="extend",
              teaches="गुल्म = abdominal lump, गलगण्ड = goitre (neck-swelling), अर्बुद = tumour, श्लीपद = filariasis (standard)."),
        mcq("discriminate", 3, "Which is the right split of ग्रन्थ्यर्बुद in unit 44?",
            ("ग्रन्थि + अर्बुद", "इ + अ → य: ग्रन्थि + अर्बुद → ग्रन्थ्यर्बुद."),
            [("ग्रन्थ्य + अर्बुद", "अ + अ would give आ: ग्रन्थ्यार्बुद."),
             ("ग्रन्थिः + अर्बुद", "इः before a vowel becomes इर्: ग्रन्थिरर्बुद."),
             ("ग्रन्थु + अर्बुद", "उ + अ would give व: ग्रन्थ्वर्बुद.")],
            "ग्रन्थि (nodular swelling) + अर्बुद (tumour): इ before a different vowel becomes य्.",
            "इ + अ → य (ग्रन्थि + अर्बुद → ग्रन्थ्यर्बुद)."),
        multi("apply", 4, "Which two of these ailments does unit 44 name for the soaked seeds?",
              [("Ślīpada (filariasis)", "Right: श्लीपद closes the list."),
               ("Kuṣṭha (skin disease)", "Wrong: kuṣṭha heads the list of line 05.01.49, not this one."),
               ("Arbuda (tumour)", "Right: अर्बुद is in the list."),
               ("Jvara (fever)", "Wrong: fever is not named in this unit.")],
              [0, 2],
              "Arbuda and ślīpada are in the list; kuṣṭha and fever are not.",
              "विष, गुल्म, उदर, गलगण्ड, ग्रन्थि, अर्बुद, श्लीपद."),
        mcq("transfer", 5, "भावितानि agrees with the neuter plural बीजानि. Which new phrase about one fruit agrees correctly?",
            ("छागीक्षीरभावितं फलम्", "फलम् is neuter singular, so भावितम्."),
            [("छागीक्षीरभावितः फलम्", "भावितः is masculine; फलम् is neuter."),
             ("छागीक्षीरभाविता फलम्", "भाविता is feminine singular."),
             ("छागीक्षीरभावितानि फलम्", "भावितानि is plural; फलम् is singular.")],
            "The participle (soaked) agrees with its noun: बीजानि भावितानि, फलं भावितम्.",
            "Participle agrees in gender and number: n. pl. भावितानि, n. sg. भावितम्.",
            teaches="भावित (soaked) agrees with its noun: बीजानि भावितानि (n. pl.), फलं भावितम् (n. sg.)."),
    ],
}

# ---------------------------------------------------------------- unit 45
AUTHORED["45"] = {
    "title": "इक्ष्वाकुफलमध्यं वा",
    "question": "Which part of the ikṣvāku fruit does unit 45 use, and for which ailments?",
    "rule": ("Or the inner part (मध्य) of the ikṣvāku fruit, in kuṣṭha, poison, gulma, udara, nodular swelling, tumour, "
             "filariasis and the rest: almost the list of line 05.01.48, headed by kuṣṭha."),
    "limits": ("The printed गरगंड may be a damaged गलगण्ड (as in line 05.01.48); kept as gara (concocted poison) and gaṇḍa "
               "(swelling), an open point: not questioned. No verb and no dose are given."),
    "explain_hi": ("अब फल का मध्य भाग, यानी भीतर का गूदा, लिया जाता है। "
                   "सूची लगभग पिछले बीज-योग (पंक्ति 05.01.48) जैसी है, पर उसके आगे कुष्ठ यानी कोढ़ समेत त्वचा के रोग जुड़े हैं। "
                   "फिर विष, गुल्म, उदर, ग्रन्थि, अर्बुद और श्लीपद आते हैं। "
                   "छपा ‘गरगंड’ शायद ‘गलगण्ड’ का बिगड़ा रूप है; डेटा इसे गर यानी बनाया हुआ विष और गण्ड पढ़ता है, जो खुला प्रश्न है।"),
    "hook": "बीज के बाद गूदा: वही गाँठ-सूजन की सूची, आगे कुष्ठ।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "Which part of the ikṣvāku fruit does unit 45 use?",
            ("Its inner part (मध्य)", "इक्ष्वाकुफलमध्यम् = the inner part of the ikṣvāku fruit."),
            [("Its rind (त्वक्)", "The rind is not named in this unit."),
             ("Its stalk (वृन्त)", "The stalk is not named in this unit."),
             ("Its seeds (बीज)", "Seeds were the drug of line 05.01.48.")],
            "Unit 45 uses the inner part of the fruit.",
            "मध्य = inner part, middle."),
        order(1, "Put these ailments of unit 45 in the order of the text.",
              ["कुष्ठ", "विष", "गुल्म", "उदर", "अर्बुद", "श्लीपद"],
              "कुष्ठविषगुल्मोदर…अर्बुदश्लीपदेषु: kuṣṭha heads the list and ślīpada closes it.",
              "कुष्ठ · विष · गुल्म · उदर · … · अर्बुद · श्लीपद."),
        match(2, "Match each ailment of unit 45 to its meaning.",
              [["कुष्ठ", "skin diseases, including leprosy"], ["विष", "poison"], ["उदर", "belly-ailment"],
               ["ग्रन्थि", "nodular swelling"]],
              "Four clear members of the list, with the equivalents of the card.",
              "कुष्ठ = skin disease; विष = poison; उदर = belly-ailment; ग्रन्थि = nodular swelling.",
              role="extend",
              teaches="कुष्ठ = skin diseases including leprosy, विष = poison, उदर = belly-ailment, ग्रन्थि = nodular swelling."),
        mcq("discriminate", 3, "Which ailment heads the list of unit 45, beyond the seed list of line 05.01.48?",
            ("Kuṣṭha (skin disease)", "The compound opens with कुष्ठ, which line 05.01.48 lacks."),
            [("Ślīpada (filariasis)", "Ślīpada closes both lists."),
             ("Arbuda (tumour)", "Arbuda stands in both lists."),
             ("Gulma (abdominal lump)", "Gulma stands in both lists.")],
            "The inner-part list repeats most of the seed list and adds kuṣṭha at its head.",
            "कुष्ठ heads the list of unit 45."),
        fill(4, "The part of the fruit in unit 45 is इक्ष्वाकुफल____. Type it in Devanagari or in English letters (e.g. dharma).",
             accepts("मध्यम्", "madhyam", "मध्य", "madhya"),
             "इक्ष्वाकुफलमध्यम् = the inner part (मध्य) of the ikṣvāku fruit.",
             "In unit 45 the part used is मध्य, the inner part of the ikṣvāku fruit.",
             "मध्य = inner part.", role="apply"),
        mcq("transfer", 5, "इक्ष्वाकुफलमध्यम् is the inner part of the ikṣvāku fruit. What does a new phrase बिल्वफलमध्यम् mean?",
            ("The inner part of the bilva fruit", "Same tatpuruṣa: बिल्व-फल-मध्य = inner part of the bilva fruit."),
            [("The bilva fruit and its stalk", "मध्य is the inner part, not a second item."),
             ("The hard outer rind of bilva fruit", "Rind would be त्वक्; मध्य is the inner part."),
             ("The middle of the bilva tree", "फल names the fruit, not the tree.")],
            "X-फल-मध्य = the inner part of the fruit of X.",
            "Tatpuruṣa: the last member is the head: फल-मध्य = inner part of the fruit.",
            teaches="X-फल-मध्यम् (tatpuruṣa) = the inner part of the fruit of X: इक्ष्वाकुफलमध्यम्, बिल्वफलमध्यम्."),
    ],
}

# ---------------------------------------------------------------- unit 46 (verse)
AUTHORED["46"] = {
    "title": "इक्ष्वाकुफलं मस्तुना",
    "question": "With what is the ikṣvāku fruit taken in verse 46, for what, and what buttermilk follows?",
    "rule": ("The ikṣvāku fruit with whey (मस्तु), in kuṣṭha, poison and pale-ailments (anaemia); or buttermilk with honey "
             "and saindhava (rock salt)."),
    "limits": ("Low confidence. सद्रिपकं in line 05.01.51 is not understood (perhaps damaged) and is not questioned; whether it "
               "is a separate item or qualifies the buttermilk is open. पाण्डु is pale, not yellow."),
    "explain_hi": ("पहली पंक्ति: इक्ष्वाकु का फल मस्तु यानी दही के पानी के साथ, कुष्ठ, विष और पाण्डु-रोग यानी रक्ताल्पता में। "
                   "दूसरी पंक्ति एक और विकल्प देती है: मधु और सैन्धव यानी सेंधा नमक मिला तक्र यानी छाछ। "
                   "बीच का शब्द ‘सद्रिपक’ समझ में नहीं आता; वह अलग विकल्प है या छाछ का विशेषण, यह तय नहीं। "
                   "पाण्डु का अर्थ फीका रंग है, पीला नहीं।"),
    "hook": "फल + दही का पानी, या छाछ + शहद + सेंधा नमक।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "With what is the ikṣvāku fruit taken in the first line of verse 46?",
            ("Whey (मस्तु)", "मस्तुना = with whey, the watery part of curd."),
            [("Meat broth (मांसरस)", "Meat broth goes with the paste in line 05.01.55."),
             ("Goat's milk (छागीक्षीर)", "Goat's milk is for the seeds of line 05.01.48."),
             ("Cane juice (इक्षुरस)", "Cane juice is not named in this verse.")],
            "The fruit is taken with mastu, whey.",
            "मस्तु = whey; मस्तुना = with whey (instrumental)."),
        order(1, "Put the ailments of the first line of verse 46 in the order of the text.",
              ["कुष्ठ", "विष", "पाण्ड्वामय"],
              "कुष्ठविषपाण्ड्वामयेषु: skin disease, poison, pale-ailment.",
              "कुष्ठ · विष · पाण्ड्वामय."),
        match(2, "Match each word of verse 46 to its meaning.",
              [["मस्तु", "whey"], ["तक्र", "buttermilk"], ["पाण्ड्वामय", "pale-ailment (anaemia)"],
               ["सैन्धव", "rock salt (saindhava)"]],
              "Two liquids, one ailment and one salt of the verse.",
              "मस्तु = whey; तक्र = buttermilk; पाण्ड्वामय = pale-ailment; सैन्धव = rock salt.",
              role="extend",
              teaches="Verse 46: मस्तु = whey, तक्र = buttermilk, पाण्ड्वामय = pale-ailment (anaemia), सैन्धव = rock salt."),
        mcq("discriminate", 3, "Which is the right split of पाण्ड्वामय in verse 46?",
            ("पाण्डु + आमय", "उ before a different vowel becomes व्: पाण्डु + आमय → पाण्ड्वामय."),
            [("पाण्डु + अमय", "उ + अ would give व, short: पाण्ड्वमय."),
             ("पाण्डुः + आमय", "उः before a vowel becomes उर्: पाण्डुरामय."),
             ("पाण्डो + आमय", "ओ before आ becomes अव्: पाण्डवामय.")],
            "पाण्डु (pale) + आमय (ailment): उ + आ → वा.",
            "उ + आ → वा (पाण्डु + आमय → पाण्ड्वामय)."),
        mcq("apply", 4, "What is added to the buttermilk in the second line of verse 46?",
            ("Honey and saindhava", "समधुसैन्धवम् = with honey and saindhava (rock salt)."),
            [("Ghee and jaggery", "Neither ghee nor jaggery is named in this verse."),
             ("Ginger and long pepper", "These are not named in this verse."),
             ("Milk and sugar", "Neither is named with the buttermilk.")],
            "The buttermilk comes with honey and rock salt.",
            "स- (with) + मधु (honey) + सैन्धव (rock salt)."),
        mcq("transfer", 5, "समधुसैन्धवम् means with honey and saindhava. What does a new word सगुडघृतम् mean?",
            ("With jaggery and ghee", "स- (with) + गुड (jaggery) + घृत (ghee)."),
            [("Without jaggery and ghee", "Without would need निर्- or अ-; स- is with."),
             ("Jaggery cooked in ghee", "No cooking is in the word; स- only joins the two as additions."),
             ("Jaggery only, no ghee", "Both members are added: गुड and घृत.")],
            "स- before a dvandva of additions = together with all of them.",
            "स- = with: समधुसैन्धव, सगुडघृत.",
            teaches="The prefix स- means 'with': समधुसैन्धवम् (with honey and rock salt), सगुडघृतम् (with jaggery and ghee)."),
    ],
}

# ---------------------------------------------------------------- unit 47
AUTHORED["47"] = {
    "title": "तदेव वा मध्यं",
    "question": "What does unit 47 have the patient eat, and with what?",
    "rule": "Or one should eat that same inner part (of the ikṣvāku fruit) together with jaggery.",
    "limits": ("सगुडपलम् is read 'with a pala of jaggery'; it could also be 'with jaggery (and) a pala', so the quantity is "
               "not questioned. 'That same inner part' points to line 05.01.49 by the order of the text. No ailment is named."),
    "explain_hi": ("‘तदेव मध्यम्’ यानी वही मध्य भाग: पंक्ति 05.01.49 वाला इक्ष्वाकु-फल का गूदा। "
                   "इस बार उसे गुड़ के साथ खाया जाता है (भक्षयेत्)। "
                   "‘सगुडपलम्’ को डेटा ‘एक पल गुड़ सहित’ पढ़ता है; पर ‘गुड़ सहित, एक पल’ भी पढ़ा जा सकता है, इसलिए मात्रा पर प्रश्न नहीं। "
                   "यहाँ कोई रोग नहीं गिनाया गया।"),
    "hook": "वही गूदा, अब गुड़ के साथ: पियो नहीं, खाओ।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What does one eat in unit 47?",
            ("That same inner part, with jaggery", "तदेव … मध्यं सगुड… भक्षयेत्."),
            [("The seeds, soaked in honey water", "Seeds and honey are not named in this unit."),
             ("The fruit oil, mixed with whey", "Oil and whey are not named in this unit."),
             ("The young sprouts, boiled in milk", "Sprouts belong to line 05.01.44.")],
            "The inner part of the fruit is eaten together with jaggery.",
            "मध्य = inner part; गुड = jaggery; भक्षयेत् = should eat."),
        order(1, "Put the words of unit 47 in the order of the text.",
              ["तदेव", "वा", "मध्यम्", "सगुडपलम्", "भक्षयेत्"],
              "तदेव वा मध्यं सगुडपलं भक्षयेत्: that same, or, inner part, with jaggery, should eat.",
              "तदेव · वा · मध्यम् · सगुडपलम् · भक्षयेत्."),
        match(2, "Match each word of unit 47 to its meaning.",
              [["तदेव", "that same"], ["मध्य", "inner part"], ["गुड", "jaggery"], ["भक्षयेत्", "should eat"]],
              "What, which part, with what, and the verb.",
              "तदेव = that same; मध्य = inner part; गुड = jaggery; भक्षयेत् = should eat.",
              role="extend",
              teaches="Unit 47: तदेव = that same, मध्य = inner part, गुड = jaggery, भक्षयेत् = should eat."),
        mcq("discriminate", 3, "Which is the right split of तदेव?",
            ("तत् + एव", "त् before a vowel becomes द्: तत् + एव → तदेव."),
            [("तदा + एव", "आ + ए would give ऐ: तदैव."),
             ("तत् + इव", "That would give तदिव (like that)."),
             ("तद् + अव", "That would give तदव, not तदेव.")],
            "तत् (that) + एव (same, very): त् → द् before a vowel.",
            "त् + vowel → द् + vowel (तत् + एव → तदेव)."),
        mcq("apply", 4, "By the order of the text, the inner part of unit 47 is that of which earlier line?",
            ("The ikṣvāku fruit of line 05.01.49", "Line 05.01.49 names इक्ष्वाकुफलमध्यम्; तदेव मध्यम् takes it up."),
            [("The seeds in goat's milk, 05.01.48", "That line names seeds, not an inner part."),
             ("The sprouts in milk of 05.01.44", "That line names sprouts, not an inner part."),
             ("The old seedless fruit of 05.01.46", "That line names a whole fruit used as a vessel.")],
            "तदेव मध्यम् = that same inner part: the one named in line 05.01.49.",
            "तद् + एव points back to what was just named."),
        mcq("transfer", 5, "तदेव joins तत् and एव (that very). What does a new word तत्रैव mean?",
            ("In that very place", "तत्र (there) + एव (very): अ + ए → ऐ."),
            [("Then once again", "Again would be पुनः; तत्र is there."),
             ("Not in that same place", "There is no negative in the word."),
             ("In every place", "Everywhere would be सर्वत्र.")],
            "एव after a word stresses it: तदेव = that very; तत्रैव = in that very place.",
            "एव = very, just; अ + ए → ऐ (तत्र + एव → तत्रैव).",
            teaches="एव stresses the word before it: तदेव (that very one), तत्रैव (in that very place, अ + ए → ऐ)."),
    ],
}

# ---------------------------------------------------------------- unit 48
AUTHORED["48"] = {
    "title": "इक्ष्वाकुफलतैलं वा पिबेत्",
    "question": "What does unit 48 give the patient to drink?",
    "rule": "Or one should drink the oil of the ikṣvāku fruit.",
    "limits": "No ailment, dose or way of making the oil is given in this unit.",
    "explain_hi": ("यह इक्ष्वाकु-खण्ड की सबसे छोटी इकाई है। "
                   "इक्ष्वाकु के फल का तेल (इक्ष्वाकुफलतैल) पिया जाए। "
                   "समास तत्पुरुष है: इक्ष्वाकु का फल, और उस फल का तेल। "
                   "तेल कैसे बने, कितना पिया जाए या किस रोग में, यह यहाँ नहीं कहा।"),
    "hook": "इक्ष्वाकु फल का तेल: बस पी लो।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What does one drink in unit 48?",
            ("Oil of the ikṣvāku fruit", "इक्ष्वाकुफलतैलं … पिबेत् = should drink the oil of the ikṣvāku fruit."),
            [("Juice of the ikṣvāku fruit", "Juice (स्वरस) was the drink of line 05.01.45; here it is तैल."),
             ("Ghee of the ikṣvāku fruit", "Ghee is not named in this unit."),
             ("Brew of the ikṣvāku root", "No root or decoction is named in this unit.")],
            "Unit 48 gives the oil of the ikṣvāku fruit to drink.",
            "तैल = oil; पिबेत् = should drink."),
        order(1, "Put the parts of unit 48 in the order of the text.",
              ["इक्ष्वाकु", "फल", "तैलम्", "वा", "पिबेत्"],
              "इक्ष्वाकुफलतैलं वा पिबेत्: the compound members, then or, then the verb.",
              "इक्ष्वाकु · फल · तैलम् · वा · पिबेत्."),
        match(2, "Match each word of unit 48 to its meaning.",
              [["तैल", "oil"], ["फल", "fruit"], ["वा", "or"], ["पिबेत्", "should drink"]],
              "The members of the compound, the particle and the verb.",
              "तैल = oil; फल = fruit; वा = or; पिबेत् = should drink.",
              role="extend",
              teaches="Unit 48: तैल = oil, फल = fruit, वा = or, पिबेत् = should drink (√पा, optative)."),
        mcq("discriminate", 3, "Which English rendering of unit 48 has one wrong word?",
            ("Or one should eat the oil of the ikṣvāku fruit", "Wrong: पिबेत् is should drink, not eat (that is भक्षयेत्)."),
            [("Or one should drink the oil of the ikṣvāku fruit", "Correct: this is the card's rendering."),
             ("Or he should drink the ikṣvāku fruit's oil", "Correct: the same sense in other words."),
             ("Or the oil of the ikṣvāku fruit should be drunk", "Correct: a passive turn of the same sense.")],
            "पिबेत् (√पा) = should drink; भक्षयेत् of line 05.01.52 = should eat.",
            "पिबेत् = drink; भक्षयेत् = eat."),
        fill(4, "The verb of unit 48 that means should drink is ____. Type it in Devanagari or in English letters (e.g. dharma).",
             accepts("पिबेत्", "pibet"),
             "पिबेत् = should drink: optative of √पा.",
             "पिबेत् (√पा, optative) = should drink.",
             "पिबेत् = should drink.", role="apply"),
        mcq("transfer", 5, "इक्ष्वाकुफलतैलम् is the oil of the ikṣvāku fruit. What does a new word बिल्वफलतैलम् mean?",
            ("Oil of the bilva fruit", "Same tatpuruṣa: बिल्व-फल-तैल = oil of the bilva fruit."),
            [("Bilva fruit and its oil", "A tatpuruṣa names one thing, the oil, not two."),
             ("Fruit fried in bilva oil", "The word has no frying; तैल is the head."),
             ("Bilva oil with fruit juice", "No juice is in the word.")],
            "In a tatpuruṣa the last member is the head: X-फल-तैल = the oil of the fruit of X.",
            "Tatpuruṣa: X-फल-तैल = oil of X fruit.",
            teaches="X-फल-तैलम् (tatpuruṣa) = the oil of the fruit of X: इक्ष्वाकुफलतैलम्, बिल्वफलतैलम्."),
    ],
}

# ---------------------------------------------------------------- unit 49
AUTHORED["49"] = {
    "title": "तत्फलस्वरसभावितैव वा",
    "question": "What stirred drink does unit 49 make, with what, and for which ailments?",
    "rule": ("Or a mantha (stirred drink) with saktu (parched-grain flour), in phlegm-fever, cough, throat-ailments and "
             "arocaka; the saktu is probably soaked in the juice of that fruit (damaged reading)."),
    "limits": ("Low confidence. The printed -भावितैव does not agree with सक्तुभिः; the repair -भावितैः एव is a guess, so "
               "the soaking is not questioned. Whether श्लेष्म goes with ज्वर alone is not certain. No dose is given."),
    "explain_hi": ("यहाँ सक्तु यानी सत्तू से मन्थ, यानी घोलकर मथा हुआ पेय, बनता है। "
                   "सत्तू उसी (इक्ष्वाकु) फल के स्वरस में भिगोए जाते हैं; पर छपा रूप ‘भावितैव’ व्याकरण में ठीक नहीं बैठता, इसलिए यह अंश अनिश्चित है। "
                   "रोग हैं: कफ-ज्वर, कास यानी खाँसी, कण्ठ के रोग और अरोचक यानी खाने में अरुचि।"),
    "hook": "रस में भीगे सत्तू का मन्थ: कफ-बुखार, खाँसी, गला, अरुचि।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "Which preparation does unit 49 make with saktu?",
            ("A mantha (stirred drink)", "सक्तुभिर्मन्थम् = a mantha with saktu."),
            [("A peyā (a thin rice gruel)", "Peyā is not named in this unit."),
             ("A leha (licked paste)", "A leha is made in line 05.01.58, not here."),
             ("A surā (grain liquor)", "Surā is not named in this unit.")],
            "Saktu (parched-grain flour) is made into a mantha, a stirred drink.",
            "सक्तु = parched-grain flour; मन्थ = stirred drink."),
        order(1, "Put the ailments of unit 49 in the order of the text.",
              ["श्लेष्मज्वर", "कास", "कण्ठरोग", "अरोचक"],
              "श्लेष्मज्वरकासकण्ठरोगारोचकेषु: phlegm-fever, cough, throat-ailments, distaste for food.",
              "श्लेष्मज्वर · कास · कण्ठरोग · अरोचक."),
        match(2, "Match each word of unit 49 to its meaning.",
              [["सक्तु", "parched-grain flour"], ["मन्थ", "stirred drink"], ["कण्ठरोग", "throat-ailment"],
               ["अरोचक", "distaste for food"]],
              "The flour, the drink, and two of the ailments.",
              "सक्तु = parched-grain flour; मन्थ = stirred drink; कण्ठरोग = throat-ailment; अरोचक = anorexia.",
              role="extend",
              teaches="सक्तु = parched-grain flour, मन्थ = stirred drink, कण्ठरोग = throat-ailment, अरोचक = distaste for food (anorexia)."),
        mcq("discriminate", 3, "Which is the right split of सक्तुभिर्मन्थम्?",
            ("सक्तुभिः + मन्थम्", "इः before a voiced sound becomes इर्: सक्तुभिः + मन्थम् → सक्तुभिर्मन्थम्."),
            [("सक्तुभि + र्मन्थम्", "There is no word र्मन्थम्; the र् comes from the visarga."),
             ("सक्तुभिम् + मन्थम्", "That would give सक्तुभिं मन्थम्, with anusvara."),
             ("सक्तुभिः + अमन्थम्", "That would give सक्तुभिरमन्थम्, with a vowel after र्.")],
            "सक्तुभिः (with saktu) + मन्थम् (stirred drink): visarga after इ → र् before म.",
            "इः / उः before a voiced sound → इर् / उर् (सक्तुभिः + मन्थम् → सक्तुभिर्मन्थम्)."),
        multi("apply", 4, "Which two of these does unit 49 name for the saktu mantha?",
              [("Throat-ailments", "Right: कण्ठरोग is in the list."),
               ("Goitre", "Wrong: goitre (गलगण्ड) is in line 05.01.48, not here."),
               ("Filariasis", "Wrong: ślīpada is in lines 05.01.48 and 05.01.49, not here."),
               ("Arocaka (distaste for food)", "Right: अरोचक closes the list.")],
              [0, 3],
              "Throat-ailments and arocaka are named; goitre and filariasis are not.",
              "श्लेष्मज्वर, कास, कण्ठरोग, अरोचक."),
        mcq("transfer", 5, "सक्तुभिः + मन्थम् gives सक्तुभिर्मन्थम्. How is a new pair सक्तुभिः + युक्तम् (joined with saktu) written?",
            ("सक्तुभिर्युक्तम्", "य is voiced, so इः → इर्: सक्तुभिर्युक्तम्."),
            [("सक्तुभिस्युक्तम्", "Visarga becomes स् before त्/थ्, a voiceless sound; य is voiced, so it becomes र्."),
             ("सक्तुभियुक्तम्", "After इ the visarga is not dropped; it becomes र्."),
             ("सक्तुभिः युक्तम्", "Before a voiced sound the visarga must change; it becomes र्.")],
            "Visarga after इ or उ becomes र् before any voiced sound (म, य, a vowel).",
            "इः + voiced → इर्.",
            teaches="Visarga after इ/उ becomes र् before a voiced sound: सक्तुभिर्मन्थम्, सक्तुभिर्युक्तम्."),
    ],
}

# ---------------------------------------------------------------- unit 50
AUTHORED["50"] = {
    "title": "इक्ष्वाकुकल्कं मांसरसेन",
    "question": "With what is the ikṣvāku paste of unit 50 taken, and in which conditions?",
    "rule": "Ikṣvāku paste (कल्क) with meat broth, in Vāta-Kapha, gulma (abdominal lump) and persistent fevers.",
    "limits": ("The compound may also be read 'persistent fevers of Vāta, Kapha and gulma'; the grouping is not questioned. "
               "प्रसक्त = attached, persistent. No dose is given. This closes the ikṣvāku section."),
    "explain_hi": ("इक्ष्वाकु का कल्क, यानी पीसी हुई लुगदी, मांस के रस के साथ लिया जाता है। "
                   "दशाएँ: वात-कफ, गुल्म यानी पेट की गाँठ, और प्रसक्त यानी लगे रहने वाले ज्वर। "
                   "समास को ‘वात, कफ और गुल्म के लगे रहने वाले ज्वर’ भी पढ़ा जा सकता है; यह दो-तरफ़ा है। "
                   "इसके बाद पाठ तुम्बी के बीजों की ओर मुड़ता है।"),
    "hook": "लुगदी + मांस-रस: टिके हुए बुखार और गुल्म पर।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "With what is the ikṣvāku paste of unit 50 taken?",
            ("Meat broth (मांसरस)", "मांसरसेन = with meat broth."),
            [("Whey (मस्तु)", "Whey goes with the fruit in line 05.01.50."),
             ("Honey (मधु)", "Honey is not named in this unit."),
             ("Goat's milk (छागीक्षीर)", "Goat's milk is for the seeds of line 05.01.48.")],
            "The paste is taken with meat broth.",
            "मांसरस = meat broth; मांसरसेन = with meat broth."),
        match(1, "Match each word of unit 50 to its meaning.",
              [["कल्क", "paste"], ["मांसरस", "meat broth"], ["प्रसक्त", "persistent"], ["गुल्म", "abdominal lump"]],
              "The form of the drug, its vehicle and two words of the conditions.",
              "कल्क = paste; मांसरस = meat broth; प्रसक्त = persistent; गुल्म = abdominal lump."),
        order(2, "Put the members of the compound of unit 50 in the order of the text.",
              ["वात", "कफ", "गुल्म", "प्रसक्त", "ज्वर"],
              "वातकफगुल्मप्रसक्तज्वरेषु: Vāta, Kapha, gulma, persistent, fevers.",
              "वात · कफ · गुल्म · प्रसक्त · ज्वर.",
              role="extend",
              teaches="The conditions of unit 50 run वात · कफ · गुल्म · प्रसक्त · ज्वर (persistent fevers come last)."),
        mcq("discriminate", 3, "Which English rendering of unit 50 has one wrong word?",
            ("Ikṣvāku paste with milk, in persistent fevers", "Wrong: मांसरसेन is with meat broth, not milk."),
            [("Ikṣvāku paste with meat broth, in persistent fevers", "Correct: this follows the card."),
             ("Ikṣvāku paste with meat soup, in lasting fevers", "Correct: soup and lasting render the same words."),
             ("A paste of ikṣvāku with meat broth, in long fevers", "Correct: प्रसक्त ज्वर = persistent, long fevers.")],
            "मांसरस = meat broth; प्रसक्त = persistent.",
            "मांस = meat; रस = broth, juice."),
        mcq("apply", 4, "A patient has a persistent fever. Which ikṣvāku preparation does unit 50 give?",
            ("The paste, with meat broth", "इक्ष्वाकुकल्कं मांसरसेन … प्रसक्तज्वरेषु."),
            [("The oil, with nothing else", "The oil of line 05.01.53 names no fever."),
             ("The seeds, in goat's milk", "The seeds of line 05.01.48 name no fever."),
             ("The fruit, with whey", "The fruit with whey of line 05.01.50 names no fever.")],
            "For persistent fevers unit 50 gives ikṣvāku paste with meat broth.",
            "प्रसक्तज्वर → इक्ष्वाकुकल्क + मांसरस."),
        mcq("transfer", 5, "इक्ष्वाकुकल्कं मांसरसेन is ikṣvāku paste with meat broth. What does a new phrase बिल्वकल्कं मधुना mean?",
            ("Bilva paste with honey", "कल्क = paste; मधुना (instrumental) = with honey."),
            [("Bilva brew with honey", "A brew would be क्वाथ; कल्क is paste."),
             ("Honey paste with bilva", "The paste is of bilva; honey is the vehicle."),
             ("Bilva juice and honey", "Juice would be स्वरस; कल्क is paste.")],
            "X-कल्क = paste of X; an instrumental noun names what it is taken with.",
            "Instrumental = with: मांसरसेन (with meat broth), मधुना (with honey).",
            teaches="X-कल्कम् + instrumental = paste of X taken with: इक्ष्वाकुकल्कं मांसरसेन, बिल्वकल्कं मधुना."),
    ],
}

# ---------------------------------------------------------------- unit 51
AUTHORED["51"] = {
    "title": "बिल्वमूलप्रस्थकाथेन वा",
    "question": "Which seeds does unit 51 treat, and in a liquid made from which root?",
    "rule": ("Or one should boil tumbī (bottle gourd, probable) seeds in a decoction of a prastha of bilva (bael) root."),
    "limits": ("Printed काथेन, काधयेत् are read as kvāthena (decoction), kvāthayet (should boil): not questioned. Whether the "
               "prastha measures the root or the decoction is unclear. Tumbī is named apart from ikṣvāku, though both are given as Lagenaria."),
    "explain_hi": ("यहाँ से नया खण्ड शुरू होता है: तुम्बी यानी लौकी (सम्भावित) के बीजों का लेह। "
                   "पहला कदम: एक प्रस्थ बिल्व यानी बेल (मानक पहचान) की जड़ का काढ़ा, और उसमें तुम्बी के बीज उबाले जाएँ। "
                   "छपे ‘काथेन’ और ‘काधयेत्’ को डेटा ‘क्वाथेन’ और ‘क्वाथयेत्’ पढ़ता है। "
                   "प्रस्थ एक माप है; वह जड़ का है या काढ़े का, यह साफ़ नहीं।"),
    "hook": "बेल की जड़ का काढ़ा, उसमें लौकी के बीज: लेह की पहली सीढ़ी।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "Which seeds are treated in unit 51?",
            ("Tumbī seeds (bottle gourd)", "तुम्बीबीजानि = tumbī seeds."),
            [("Madana seeds (emetic nut)", "Madana is not named in this unit."),
             ("Ikṣvāku seeds (bitter bottle gourd)", "Ikṣvāku seeds were the drug of line 05.01.48; here it is tumbī."),
             ("Bilva seeds (bael fruit)", "Bilva gives the root here, not the seeds.")],
            "Unit 51 starts the tumbī section: tumbī seeds go into a bilva-root liquid.",
            "तुम्बी = bottle gourd (probable); बीज = seed."),
        match(1, "Match each word of unit 51 to its meaning.",
              [["बिल्व", "bael, Aegle marmelos"], ["मूल", "root"], ["तुम्बी", "bottle gourd (probable)"], ["बीज", "seed"]],
              "The plant and part of the liquid, and the plant and part treated in it.",
              "बिल्व = bael (standard); मूल = root; तुम्बी = bottle gourd (probable); बीज = seed."),
        fill(2, "The part of bilva used in unit 51 is बिल्व____ (root). Type it in Devanagari or in English letters (e.g. dharma).",
             accepts("मूल", "mūla", "mula"),
             "बिल्वमूल = the root (मूल) of bilva.",
             "In unit 51 the bilva part is मूल, the root.",
             "मूल = root."),
        mcq("discriminate", 3, "What is प्रस्थ in unit 51?",
            ("A measure of quantity", "The card: prastha is a measure; what it measures is not clear."),
            [("A kind of root", "मूल is the root; प्रस्थ is a measure."),
             ("A cooking vessel", "No vessel is named in this unit."),
             ("A second plant name", "The plants are bilva and tumbī; प्रस्थ is a measure.")],
            "प्रस्थ is a measure; the text does not say whether it measures the root or the decoction.",
            "प्रस्थ = a measure (kept as prastha)."),
        mcq("apply", 4, "A helper has bilva leaves but no bilva root. Does he have what unit 51 names?",
            ("No: the text names bilva root", "बिल्वमूल = bilva root; leaves are not named."),
            [("Yes: any bilva part will do", "The text names the root only."),
             ("Yes: the text names the leaves", "No leaves are named in this unit."),
             ("No: the text names bilva fruit", "The text names the root, not the fruit.")],
            "The liquid is made from bilva root (मूल).",
            "बिल्व + मूल = bilva root."),
        mcq("transfer", 5, "बिल्वमूल is the root of bilva. What does a new word निम्बमूलम् mean?",
            ("The root of nimba", "Same tatpuruṣa: निम्ब + मूल = root of nimba (neem)."),
            [("Nimba and a root", "A tatpuruṣa names one thing, the root."),
             ("The fruit of nimba", "Fruit would be फल; मूल is root."),
             ("A root like nimba", "Likeness would need -वत् or -सदृश.")],
            "X-मूल = the root of X: the last member is the head.",
            "Tatpuruṣa: बिल्वमूल, निम्बमूल = root of bilva, of nimba.",
            teaches="X-मूलम् (tatpuruṣa) = the root of X: बिल्वमूल (bael root), निम्बमूल (neem root)."),
    ],
}

# ---------------------------------------------------------------- unit 52
AUTHORED["52"] = {
    "title": "ततस्तस्मिंस्त्रिभागघृते",
    "question": "What is added, in what quantities, into the ghee-liquid of unit 52?",
    "rule": ("Then into that (ghee-liquid) one adds tumbī seeds ground, equal to the ghee; jīmūta (misprinted), mahājālinī, "
             "vatsaka (kuṭaja) and kṛtavedhana, each at a smaller portion (damaged word); and trikaṭuka equal to the decoction."),
    "limits": ("Low confidence. त्रिभाग (a third or three parts) is open; the 'half that portion' word and the member jīmūta "
               "are misprinted: none is questioned. Trikaṭuka equal to the decoction is literal. Mahājālinī is unidentified."),
    "explain_hi": ("यह लेह की दूसरी सीढ़ी है। ‘ततः’ यानी फिर, उसमें (बेल के काढ़े में), जिसमें घृत भी है, ये डाले जाएँ। "
                   "पहले तुम्बी के बीज, पीसकर, घृत के बराबर। "
                   "फिर प्रत्येक, एक अंश में: जीमूत, महाजालिनी (अज्ञात), वत्सक यानी कुटज (सम्भावित) और कृतवेधन यानी तोरई (सम्भावित)। "
                   "अन्त में काढ़े के बराबर त्रिकटु यानी सोंठ, पीपर और काली मिर्च। "
                   "‘त्रिभाग’ तीसरा भाग है या तीन भाग, यह खुला प्रश्न है।"),
    "hook": "बीज घी-बराबर, चार द्रव्य थोड़े-थोड़े, त्रिकटु काढ़े-बराबर: फिर डाल दो।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "What does unit 52 add last, in a quantity equal to the decoction?",
            ("Trikaṭuka", "क्वाथतुल्यमेव च त्रिकटुकमावपेत् = trikaṭuka equal to the decoction."),
            [("Rock salt", "Rock salt is not named in this unit."),
             ("Honey", "Honey is not named in this unit."),
             ("Jaggery", "Jaggery is not named in this unit.")],
            "Last comes trikaṭuka, equal to the decoction.",
            "त्रिकटुक = dry ginger, long pepper, black pepper (standard)."),
        order(1, "Put these parts of unit 52 in the order of the text.",
              ["घृतसमानि पिष्ट्वा तुम्बीबीजानि", "प्रत्येकं …महाजालिनीवत्सककृतवेधनानि", "क्वाथतुल्यमेव च त्रिकटुकम्", "आवपेत्"],
              "Ground tumbī seeds, then each of the four drugs, then trikaṭuka, then the verb: should add.",
              "तुम्बीबीजानि → …कृतवेधनानि → त्रिकटुकम् → आवपेत्."),
        match(2, "Match each word of unit 52 to its meaning.",
              [["त्रिकटुक", "dry ginger, long pepper, black pepper"], ["वत्सक", "kuṭaja, Holarrhena (probable)"],
               ["कृतवेधन", "ridged gourd, Luffa acutangula (probable)"], ["पिष्ट्वा", "having ground"]],
              "Three drug names with the data's identifications, and the verb of grinding.",
              "त्रिकटुक = three pungents (standard); वत्सक = kuṭaja; कृतवेधन = ridged gourd; पिष्ट्वा = having ground.",
              role="extend",
              teaches="त्रिकटुक = dry ginger + long pepper + black pepper (standard); वत्सक = kuṭaja (probable); कृतवेधन = ridged gourd (probable)."),
        mcq("discriminate", 3, "How much of the ground तुम्बी seeds does unit 52 take?",
            ("Equal to the ghee", "घृतसमानि = equal to the ghee."),
            [("Equal to the decoction", "Equal to the decoction is the trikaṭuka, not the seeds."),
             ("Double the ghee", "No doubling is named in this unit."),
             ("One pala in all", "No pala is named in this unit.")],
            "The seeds are ground and taken equal to the ghee; trikaṭuka is equal to the decoction.",
            "घृतसम = equal to the ghee; क्वाथतुल्य = equal to the decoction."),
        multi("apply", 4, "Which two of these drug names stand in the compound …महाजालिनीवत्सककृतवेधनानि of unit 52?",
              [("Mahājālinī", "Right: महाजालिनी is in the list."),
               ("Madana fruit", "Wrong: madana is not named in this unit."),
               ("Vatsaka (kuṭaja)", "Right: वत्सक is in the list."),
               ("Bilva root", "Wrong: bilva root gives the decoction of line 05.01.56; it is not in this list.")],
              [0, 2],
              "The drug compound names jīmūta, mahājālinī, vatsaka and kṛtavedhana.",
              "…महाजालिनी-वत्सक-कृतवेधनानि: a dvandva of drug names."),
        mcq("transfer", 5, "पिष्ट्वा (having ground) is built with -त्वा on a root with no prefix. Which new form means having drunk (√पा)?",
            ("पीत्वा", "√पा with no prefix takes -त्वा: पीत्वा, having drunk."),
            [("पिबेत्", "पिबेत् is optative: should drink."),
             ("पातुम्", "पातुम् is the infinitive: to drink."),
             ("पेयम्", "पेयम् is a gerundive: to be drunk.")],
            "A root without a prefix forms its absolutive (having done) with -त्वा.",
            "No prefix → -त्वा (पिष्ट्वा, पीत्वा); with prefix → -य.",
            teaches="-त्वा makes 'having done' from a root with no prefix: पिष्ट्वा (having ground), पीत्वा (having drunk)."),
    ],
}

# ---------------------------------------------------------------- unit 53
AUTHORED["53"] = {
    "title": "ततः पुनरपि",
    "question": "What does unit 53 make of the mixture at the end?",
    "rule": "Then, having heated it again, one should prepare a leha (licked preparation).",
    "limits": ("Low confidence. Printed श्रुत्वा ('having heard') is read as 'having boiled'; its exact form and root are "
               "uncertain and it is not questioned. No time or test of readiness is given."),
    "explain_hi": ("यह लेह की तीसरी सीढ़ी है। "
                   "‘ततः पुनरपि’ यानी फिर, एक बार और: पिछली पंक्ति (05.01.57) में सब द्रव्य डालने के बाद मिश्रण फिर पकाया जाता है। "
                   "छपा ‘श्रुत्वा’ (सुनकर) यहाँ अर्थ नहीं देता; डेटा उसे ‘उबालकर’ पढ़ता है, पर सही रूप अनिश्चित है। "
                   "फल: लेह, यानी चाटने योग्य गाढ़ी औषध, तैयार करे (साधयेत्)।"),
    "hook": "फिर एक बार पकाओ, और लेह तैयार।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What does one prepare in unit 53?",
            ("A leha (licked preparation)", "लेहं साधयेत् = should prepare a leha."),
            [("A mantha (stirred drink)", "The mantha was made in line 05.01.54, not here."),
             ("A dadhi (curd in the fruit)", "Curd was made in line 05.01.47, not here."),
             ("A surā (grain liquor)", "Surā is not named in this unit.")],
            "The mixture is heated again and made into a leha.",
            "लेह = licked preparation; साधयेत् = should prepare."),
        order(1, "Put these words of unit 53 in the order of the text.",
              ["ततः", "पुनरपि", "लेहम्", "साधयेत्"],
              "ततः पुनरपि … लेहं साधयेत्: then, again, (heating it), a leha, should prepare.",
              "ततः · पुनरपि · लेहम् · साधयेत्."),
        match(2, "Match each word of unit 53 to its meaning.",
              [["ततः", "then"], ["पुनरपि", "again"], ["लेह", "licked preparation"], ["साधयेत्", "should prepare"]],
              "The four clear words of the unit.",
              "ततः = then; पुनरपि = again; लेह = licked preparation; साधयेत् = should prepare.",
              role="extend",
              teaches="Unit 53: ततः = then, पुनरपि = again (पुनर् + अपि), लेह = licked preparation, साधयेत् = should prepare."),
        mcq("discriminate", 3, "Which is the right split of पुनरपि?",
            ("पुनर् + अपि", "पुनः keeps its र् before a vowel: पुनर् + अपि → पुनरपि."),
            [("पुन + रपि", "There is no word रपि; the र् belongs to पुनर्."),
             ("पुनरा + अपि", "आ + अ would give आ: पुनरापि."),
             ("पुनर + पि", "There is no word पि; the second word is अपि.")],
            "पुनः (again) + अपि (also): the र् of पुनर् shows before the vowel.",
            "पुनः + vowel → पुनर् + vowel (पुनरपि)."),
        mcq("apply", 4, "By the order of the text, what does ततः (then) in unit 53 follow?",
            ("Adding the drugs and trikaṭuka", "Line 05.01.57 adds the seeds, the four drugs and trikaṭuka; then comes this unit."),
            [("Licking the leha and drinking", "Licking comes after, in line 05.01.59."),
             ("Pouring milk into an old fruit", "That is the curd method of line 05.01.46."),
             ("Soaking seeds in goat's milk", "That is the seed method of line 05.01.48.")],
            "ततः follows the adding of line 05.01.57: the mixture is heated again into a leha.",
            "ततः = then, after the step just given."),
        mcq("transfer", 5, "साधयेत् means he should prepare. Which new form means they should prepare (वैद्याः लेहं ____)?",
            ("साधयेयुः", "Optative 3rd plural ends in -युः: साधयेयुः."),
            [("साधयेत्", "साधयेत् is 3rd singular: he should prepare."),
             ("साधयन्ति", "साधयन्ति is present: they prepare, not should."),
             ("साधयेम", "साधयेम is 1st plural: we should prepare.")],
            "Optative 3rd person: singular -एत्, plural -एयुः.",
            "Optative: साधयेत् (he should), साधयेयुः (they should).",
            teaches="Optative 3rd person: साधयेत् = he should prepare, साधयेयुः = they should prepare."),
    ],
}

# ---------------------------------------------------------------- unit 54
AUTHORED["54"] = {
    "title": "तमवलिह्य",
    "question": "How is the leha of unit 54 taken, and where is the same procedure said to be stated?",
    "rule": ("Having licked it, one drinks something after; the procedure (kalpa) is to be understood as stated separately "
             "for the four members of the great five roots, beginning with kāśmarya (gambhārī)."),
    "limits": ("Low confidence. What is drunk after (pramathyā and ghee) is a conjectural repair of a damaged token: not "
               "questioned. Which four roots are meant is an inference (the text lists none); kāśmarya = Gmelina arborea (standard)."),
    "explain_hi": ("लेह की अन्तिम सीढ़ी: उसे चाटकर (अवलिह्य) पीछे से कुछ पिया जाता है (अनुपिबेत्); डेटा उसे प्रमथ्या और घृत पढ़ता है, पर यह अनुमान है। "
                   "फिर पाठ कहता है: यही कल्प, यानी विधि, काश्मर्य यानी गम्भारी आदि महापञ्चमूल के चार अंगों के लिए अलग-अलग कहा हुआ जानना चाहिए। "
                   "महापञ्चमूल के पाँच नाम पाठ यहाँ नहीं गिनाता। "
                   "‘अवलिह्य’ में उपसर्ग ‘अव’ है, इसलिए -त्वा नहीं, -य लगा है।"),
    "hook": "चाटो, पीछे से पियो; और काश्मर्य आदि चार मूलों में भी यही विधि।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What is done first with the leha in unit 54?",
            ("It is licked (अवलिह्य)", "तमवलिह्य = having licked it."),
            [("It is smelt (उपजिघ्रन्)", "Smelling is not named in this unit."),
             ("It is rubbed on the skin", "No rubbing is named in this unit."),
             ("It is poured into the nose", "No nasal use is named in this unit.")],
            "The leha is licked, and something is drunk after it.",
            "अवलिह्य = having licked (अव-√लिह्)."),
        order(1, "Put these parts of unit 54 in the order of the text.",
              ["तमवलिह्य", "कल्पः", "काश्मर्यादिषु चतुर्षु", "महापञ्चमूलाङ्गेषु", "पृथक्पृथगुक्तो वेदितव्यः"],
              "Having licked it … the procedure, for the four beginning with kāśmarya, members of the great five roots, "
              "stated separately, to be known.",
              "तमवलिह्य · कल्पः · काश्मर्यादिषु चतुर्षु · महापञ्चमूलाङ्गेषु · पृथक्पृथगुक्तो वेदितव्यः."),
        match(2, "Match each word of unit 54 to its meaning.",
              [["अवलिह्य", "having licked"], ["कल्प", "procedure"], ["पृथक् पृथक्", "separately"],
               ["वेदितव्य", "to be known"]],
              "The action, the procedure, how it is stated and what one must do with it.",
              "अवलिह्य = having licked; कल्प = procedure; पृथक् पृथक् = separately; वेदितव्य = to be known.",
              role="extend",
              teaches="Unit 54: अवलिह्य = having licked, कल्प = procedure, पृथक् पृथक् = separately, वेदितव्य = to be known."),
        mcq("discriminate", 3, "Why does अवलिह्य end in -य and not in -त्वा?",
            ("The root has a prefix (अव-)", "With a prefix the absolutive takes -य: अव + √लिह् → अवलिह्य."),
            [("The root is in the causative", "No causative is in अवलिह्य; the -य comes from the prefix."),
             ("The subject is in the plural", "Number does not change an absolutive."),
             ("The form is a future tense", "An absolutive (having done) is not a tense.")],
            "Absolutive: -त्वा without a prefix (पिष्ट्वा), -य with a prefix (अवलिह्य).",
            "Prefix + root → -य; bare root → -त्वा."),
        mcq("apply", 4, "For what does unit 54 say the same procedure is stated separately?",
            ("The four great-five-root members", "काश्मर्यादिषु चतुर्षु महापञ्चमूलाङ्गेषु: the four, beginning with kāśmarya."),
            [("The madana flowers and fruits", "These belong to line 05.01.30, not to this statement."),
             ("Jīmūtaka and drugs of its kind", "These are named in line 05.01.32, not here."),
             ("The tumbī seeds and the bilva root", "These make the leha itself; the statement names the four members from kāśmarya on.")],
            "The kalpa is to be known as stated separately for the four members of the great five roots, from kāśmarya on.",
            "महापञ्चमूल = the great five roots; काश्मर्य = gambhārī (standard)."),
        mcq("transfer", 5, "अव + √लिह् gives अवलिह्य (having licked). Which new form means having drunk after (अनु + √पा)?",
            ("अनुपीय", "With the prefix अनु the absolutive takes -य: अनुपीय."),
            [("अनुपीत्वा", "-त्वा is for a root with no prefix; अनु needs -य."),
             ("अनुपिबेत्", "अनुपिबेत् is optative: should drink after."),
             ("अनुपातुम्", "अनुपातुम् is an infinitive: to drink after.")],
            "A prefixed root forms its absolutive with -य: अवलिह्य, अनुपीय.",
            "Prefix + root → -य (अवलिह्य, अनुपीय).",
            teaches="With a prefix, 'having done' takes -य: अवलिह्य (having licked), अनुपीय (having drunk after)."),
    ],
}


NOTES_HI = {
    "40": ("विश्वास: मध्यम। छपा ‘ईक्ष्वाकु’ (दीर्घ ई) आगे की पंक्तियों के ‘इक्ष्वाकु’ (ह्रस्व इ) से भिन्न है; यह पाठभेद या छपाई-दोष है। "
           "खुला बिन्दु (05.01.43): इसे दोष न मानकर पाठभेद मानने का सुझाव; इस पर प्रश्न नहीं बना। "
           "अन्तिम ‘रोग’ सब सदस्यों पर लगे या केवल ‘श्लेष्म’ पर, यह दो-तरफ़ा है। "
           "सन्धि जाँची: ईक्ष्वाकुस्तु = ईक्ष्वाकुः + तु (विसर्ग → स् त से पहले); ज्वरच्छर्दि = ज्वर + छर्दि (ह्रस्व स्वर के बाद छ → च्छ)। "
           "पहचान (सम्भावित): इक्ष्वाकु = कड़वी लौकी, Lagenaria siceraria का कड़वा रूप; पाठ ‘कड़वी’ नहीं कहता।"),
    "41": ("विश्वास: निम्न। छपा ‘श्रुतं’ (सुना हुआ) दूध के साथ अर्थ नहीं देता; डेटा ‘शृतम्’ (उबाला हुआ) पढ़ता है (ऋ/उ का भ्रम)। "
           "‘रातजीमूतवत्’ में ‘रात’ अज्ञात शब्द है, कोई शब्द गिरा या बदला हो सकता है; खुला बिन्दु (05.01.44): इस चिह्न की ‘सुझाव’ प्रविष्टि वास्तविक सुझाव नहीं। "
           "इन दोनों पर प्रश्न नहीं बना। ‘अपुष्पफल’ = फूल-फल रहित, या ‘जिसमें अभी फूल-फल न आए हों’। "
           "‘तस्य’ पाठ-क्रम से इक्ष्वाकु। सन्धि जाँची: क्षीरमुद्रिक्तपित्ते = क्षीरम् + उद्रिक्तपित्ते।"),
    "42": ("विश्वास: मध्यम। ‘पिबेत’ आत्मनेपद विधिलिङ् रूप है, छपे रूप में रखा। "
           "‘त्रिगुणक्षीर’ = तिगुना दूध; ठीक माप पाठ में नहीं। "
           "सन्धि जाँची: त्रिगुणक्षीरसाधितमातुरः = …साधितम् + आतुरः; वमनार्थी = वमन + अर्थी (अ + अ → आ)। "
           "पहचान (मानक): कफपीनस = पुराना जुकाम; स्वरसाद = आवाज़ बैठना।"),
    "43": ("विश्वास: मध्यम। छपा ‘श्वासुरुच्छर्दिषु’ में ‘उ’ सम्भवतः छपाई-दोष है; श्वास + अरुच् से ‘श्वासारुच्’ बनना चाहिए। "
           "इसलिए रोग-सूची पर प्रश्न नहीं बना। ‘श्लेष्मकास’ = कफ की खाँसी, या कफ और खाँसी अलग-अलग भी। "
           "‘जीर्णे’ = पुराने (फल में)। फल पाठ-क्रम से इक्ष्वाकु का। "
           "सन्धि: ‘तत्र जातं दधि’ में कोई परिवर्तन नहीं; ‘क्षीरं प्रक्षिपेत्’ में अन्त्य म् → अनुस्वार।"),
    "44": ("विश्वास: मध्यम। क्रिया नहीं; प्रयोग पिछली पंक्तियों से समझा जाता है। "
           "छपे ‘गंड’, ‘ग्रंथि’ = गण्ड, ग्रन्थि (अनुस्वार)। "
           "सन्धि जाँची: गुल्मोदर = गुल्म + उदर (अ + उ → ओ); ग्रन्थ्यर्बुद = ग्रन्थि + अर्बुद (इ + अ → य)। "
           "पहचान (मानक): गुल्म = पेट की गाँठ, गलगण्ड = घेंघा, ग्रन्थि = गाँठ, अर्बुद = रसौली, श्लीपद = हाथीपाँव; उदर यहाँ रोग-वाचक है।"),
    "45": ("विश्वास: मध्यम। छपा ‘गरगंड’ सम्भवतः पंक्ति 05.01.48 के ‘गलगण्ड’ का बिगड़ा रूप है; डेटा इसे ‘गर’ (बनाया हुआ विष) और ‘गण्ड’ अलग पढ़ता है। "
           "खुला बिन्दु (05.01.49): इस पर ‘सम्भावित’ चिह्न जोड़ने का सुझाव; इसलिए गर और गण्ड पर प्रश्न नहीं बना। "
           "सन्धि जाँची: गुल्मोदर = गुल्म + उदर; ग्रन्थ्यर्बुद = ग्रन्थि + अर्बुद। क्रिया नहीं।"),
    "46": ("विश्वास: निम्न। पंक्ति 05.01.51 का ‘सद्रिपकं’ पहचाना नहीं गया (शायद ‘स-’ और कोई बिगड़ा शब्द); इस पर प्रश्न नहीं बना। "
           "‘वा’ सद्रिपक और तक्र को विकल्प बनाता है, या सद्रिपक तक्र का विशेषण है: दो-तरफ़ा। "
           "शब्दावली के अनुसार पाण्डु = फीका, पीला नहीं। सैन्धव = सेंधा नमक। "
           "सन्धि जाँची: पाण्ड्वामय = पाण्डु + आमय (उ + आ → वा)। छपे ‘पांड्वामयेषु’, ‘सैंधवं’ में अनुस्वार।"),
    "47": ("विश्वास: मध्यम। ‘सगुडपलम्’ = एक पल गुड़ सहित, या ‘गुड़ सहित (और) एक पल’; किसका पल, यह साफ़ नहीं। मात्रा पर प्रश्न नहीं बना। "
           "‘तदेव मध्यम्’ पंक्ति 05.01.49 के इक्ष्वाकु-फल-मध्य की ओर संकेत, पाठ-क्रम से। "
           "सन्धि जाँची: तदेव = तत् + एव (त् → द्)। डेटा ‘भक्षयेत्’ को ‘प्रेरणार्थक’ लिखता है; √भक्ष् चुरादि है, अर्थ प्रेरणा का नहीं (रिपोर्ट किया)।"),
    "48": ("विश्वास: उच्च। कोई छपाई-दोष चिह्नित नहीं। ‘इक्ष्वाकुफलतैलम्’ तत्पुरुष: इक्ष्वाकु के फल का तेल। "
           "तेल बनाने की विधि, मात्रा या रोग इस पंक्ति में नहीं। ‘पिबेत्’ परस्मैपद (पंक्ति 05.01.45 के ‘पिबेत’ से भिन्न)।"),
    "49": ("विश्वास: निम्न। छपा ‘भावितैव’ सक्तुभिः से मेल नहीं खाता; ‘भावितैर् एव’ (र् गिरा) एक अनुमान है, या ‘भाविता एव’ किसी अनकहे स्त्रीलिङ्ग शब्द के साथ। "
           "इसलिए भिगोने वाले अंश पर प्रश्न नहीं बना। "
           "सन्धि जाँची: सक्तुभिर्मन्थम् = सक्तुभिः + मन्थम् (इः → इर् घोष से पहले); कण्ठरोगारोचक = …रोग + अरोचक (अ + अ → आ)। छपा ‘कंठ’ = कण्ठ।"),
    "50": ("विश्वास: मध्यम। समास दो तरह पढ़ा जा सकता है: ‘वात-कफ, गुल्म और लगे रहने वाले ज्वर’ या ‘वात, कफ और गुल्म के लगे रहने वाले ज्वर’; समूहन पर प्रश्न नहीं बना। "
           "प्रसक्त = लगा हुआ, टिका हुआ। कोई छपाई-दोष चिह्नित नहीं। इसके बाद तुम्बी-खण्ड आरम्भ होता है।"),
    "51": ("विश्वास: मध्यम। छपे ‘काथेन’ और ‘काधयेत्’ = क्वाथेन (काढ़े से) और क्वाथयेत् (उबाले); क्-व का संयुक्त अक्षर छपाई में खो गया। "
           "खुला बिन्दु (05.01.56): चिह्न का ‘src’ पूरा छपा शब्द होना चाहिए। इन दोनों शब्दों पर प्रश्न नहीं बना। "
           "प्रस्थ जड़ का माप है या काढ़े का, यह साफ़ नहीं। पहचान: बिल्व = बेल, Aegle marmelos (मानक); तुम्बी = लौकी, Lagenaria siceraria (सम्भावित), इक्ष्वाकु से अलग नाम।"),
    "52": ("विश्वास: निम्न। खुला बिन्दु (05.01.57): ‘त्रिभाग’ = तीसरा भाग या तीन भाग; अनुवाद एक को तथ्य मानते हैं। इस पर प्रश्न नहीं बना। "
           "‘तदर्द्धाशिकानि’ में अनुस्वार गिरा (तदर्धांशिकानि), और ‘जीमुत’ में ह्रस्व उ (जीमूत): इन सदस्यों पर प्रश्न नहीं बना; बाकी स्पष्ट सदस्यों पर बने। "
           "‘त्रिकटुक काढ़े के बराबर’ शाब्दिक है, विचित्र मात्रा सुधारी नहीं गई। महाजालिनी अज्ञात। "
           "सन्धि जाँची: ततस्तस्मिंस्त्रिभाग… = ततः + तस्मिन् + त्रिभाग… (विसर्ग → स्, न् → ंस् त से पहले); त्रिकटुकमावपेत् = त्रिकटुकम् + आवपेत्।"),
    "53": ("विश्वास: निम्न। छपा ‘श्रुत्वा’ (सुनकर) अर्थ नहीं देता; ‘उबालकर’ अभिप्रेत लगता है, पर शुद्ध रूप (शृत्वा, श्रात्वा या श्रपयित्वा) अनिश्चित है। "
           "इस शब्द पर प्रश्न नहीं बना। सन्धि जाँची: पुनरपि = पुनः (पुनर्) + अपि।"),
    "54": ("विश्वास: निम्न। छपा ‘प्रमध्यामनुपिबेत्तद्वद्धमेव’ = सम्भवतः ‘प्रमथ्याम् अनुपिबेत् तद्वद् घृतम् एव’ (ध/थ भ्रम, और ‘ऋत’ गिरा)। "
           "खुला बिन्दु (05.01.59): एक ही शब्द पर दो चिह्न, इन्हें मिलाने का सुझाव। प्रमथ्या और घृत पर प्रश्न नहीं बना। "
           "महापञ्चमूल (मानक): बिल्व, अग्निमन्थ, श्योनाक, काश्मर्य, पाटला; पाठ यहाँ इन्हें नहीं गिनाता, और ‘चार’ कौन से हैं यह अनुमान है। "
           "सन्धि जाँची: तमवलिह्य = तम् + अवलिह्य; पृथगुक्तो वेदितव्यः = पृथक् + उक्तः (क् → ग्, अः → ओ घोष से पहले)।"),
}


AIDS = {
    "40": {
        "diagram": {"groups": [{"label": "इक्ष्वाकु विशेष रूप से (पाठ-क्रम)",
                                "items": ["कास", "श्वास", "ज्वर", "छर्दि", "विष", "श्लेष्मरोग"]}]},
        "sandhi": "ह्रस्व स्वर + छ → च्छ: ज्वर + छर्दि → ज्वरच्छर्दि; विसर्ग → स् त से पहले: ईक्ष्वाकुः + तु → ईक्ष्वाकुस्तु।",
        "anchors": "कास = खाँसी · श्वास = साँस फूलना · ज्वर = बुखार · छर्दि = उल्टी · योज्य = प्रयोग करने योग्य।",
    },
    "41": {
        "frame": "क्या: इक्ष्वाकु के प्रवाल · कब: जब फूल-फल न हों · किसमें: दूध · किसके लिए: बढ़ा पित्त, पित्त-कफ ज्वर।",
        "anchors": "प्रवाल = नया पल्लव · अपुष्पफल = फूल-फल रहित · उद्रिक्त = बढ़ा हुआ · क्षीर = दूध।",
        "sandhi": "म् + स्वर: क्षीरम् + उद्रिक्तपित्ते → क्षीरमुद्रिक्तपित्ते; अ + अ → आ: तस्य + अपुष्पफलस्य → तस्यापुष्पफलस्य।",
    },
    "42": {
        "chain": {"steps": ["इक्ष्वाकु-फल का स्वरस", "तिगुने दूध में तैयार", "वमन चाहने वाला रोगी पिए",
                            "पित्त, कफ-पीनस, स्वरसाद में"]},
        "anchors": "स्वरस = ताज़ा निचोड़ा रस · त्रिगुण = तिगुना · आतुर = रोगी · पीनस = जुकाम · स्वरसाद = आवाज़ बैठना।",
        "contrast": "वमनार्थी = वमन (उल्टी) चाहने वाला · विरेचनार्थी = विरेचन (दस्त) चाहने वाला।",
    },
    "43": {
        "chain": {"steps": ["पुराना फल लो", "उसके बीज निकालो", "उसमें दूध डालो", "उसी में दही जमे"]},
        "anchors": "जीर्ण = पुराना · समुद्धृत = निकाला हुआ · प्रक्षिपेत् = डाले · जात = बना हुआ · दधि = दही।",
        "pegs": "मेरा बनाया चित्र: खोखला फल (सम्भवतः कड़वी लौकी) एक छोटी मटकी है, जिसमें डाला दूध दही बन जाता है।",
    },
    "44": {
        "diagram": {"groups": [{"label": "बकरी के दूध में भीगे बीज (पाठ-क्रम)",
                                "items": ["विष", "गुल्म", "उदर", "गलगण्ड", "ग्रन्थि", "अर्बुद", "श्लीपद"]}]},
        "sandhi": "अ + उ → ओ: गुल्म + उदर → गुल्मोदर; इ + अ → य: ग्रन्थि + अर्बुद → ग्रन्थ्यर्बुद।",
        "anchors": "छागी = बकरी · भावित = भिगोया · गलगण्ड = घेंघा · अर्बुद = रसौली · श्लीपद = हाथीपाँव।",
    },
    "45": {
        "contrast": "पंक्ति 05.01.48: बीज, सूची विष से शुरू · पंक्ति 05.01.49: फल का मध्य, सूची कुष्ठ से शुरू।",
        "anchors": "मध्य = भीतर का गूदा · कुष्ठ = कोढ़ समेत त्वचा-रोग · ग्रन्थि = गाँठ · अर्बुद = रसौली।",
        "chunks": "इक्ष्वाकुफलमध्यं वा | कुष्ठविषगुल्मोदर | गरगण्डग्रन्थ्यर्बुदश्लीपदेषु।",
    },
    "46": {
        "contrast": "पहली पंक्ति: फल + मस्तु → कुष्ठ, विष, पाण्डु-रोग · दूसरी पंक्ति: सद्रिपक (अस्पष्ट), या मधु-सैन्धव सहित तक्र।",
        "anchors": "मस्तु = दही का पानी · तक्र = छाछ · सैन्धव = सेंधा नमक · पाण्डु = फीका · आमय = रोग।",
        "sandhi": "उ + आ → वा: पाण्डु + आमय → पाण्ड्वामय।",
    },
    "47": {
        "chunks": "तदेव वा | मध्यम् | सगुडपलम् | भक्षयेत्।",
        "sandhi": "त् + स्वर → द्: तत् + एव → तदेव।",
        "contrast": "पिबेत् = पिए (पंक्ति 05.01.53, तेल) · भक्षयेत् = खाए (यहाँ, गूदा)।",
    },
    "48": {
        "chunks": "इक्ष्वाकु-फल-तैलम् | वा | पिबेत्।",
        "anchors": "तैल = तेल · फल = फल · पिबेत् = पिए (√पा)।",
        "frame": "क्या: इक्ष्वाकु-फल का तेल · कैसे: पीना · कितना, किस रोग में: पाठ नहीं कहता।",
    },
    "49": {
        "diagram": {"groups": [{"label": "सत्तू का मन्थ (पाठ-क्रम)",
                                "items": ["श्लेष्मज्वर", "कास", "कण्ठरोग", "अरोचक"]}]},
        "sandhi": "इः + घोष → इर्: सक्तुभिः + मन्थम् → सक्तुभिर्मन्थम्; अ + अ → आ: रोग + अरोचक → रोगारोचक।",
        "anchors": "सक्तु = सत्तू · मन्थ = घोलकर मथा पेय · कण्ठ = गला · अरोचक = अरुचि।",
    },
    "50": {
        "chain": {"steps": ["इक्ष्वाकु का कल्क", "मांस-रस के साथ", "वात-कफ, गुल्म, लगे रहने वाले ज्वर में"]},
        "anchors": "कल्क = पीसी लुगदी · मांसरस = मांस का रस · प्रसक्त = टिका हुआ · गुल्म = पेट की गाँठ।",
        "frame": "इक्ष्वाकु-खण्ड के रूप: प्रवाल (दूध) · स्वरस · फल में दही · बीज · मध्य · फल + मस्तु · मध्य + गुड़ · तेल · मन्थ · कल्क।",
    },
    "51": {
        "frame": "द्रव: एक प्रस्थ बेल-जड़ का काढ़ा · उसमें: तुम्बी के बीज · क्रिया: उबाले।",
        "anchors": "बिल्व = बेल · मूल = जड़ · प्रस्थ = एक माप · तुम्बी = लौकी (सम्भावित) · बीज = बीज।",
        "chain": {"steps": ["बेल-जड़ का काढ़ा (पंक्ति 05.01.56)", "घी-द्रव में बीज, द्रव्य, त्रिकटु (05.01.57)",
                            "फिर पकाकर लेह (05.01.58)", "चाटकर पीछे पिए (05.01.59)"]},
    },
    "52": {
        "chain": {"steps": ["तुम्बी के बीज पीसकर, घी के बराबर", "जीमूत, महाजालिनी, वत्सक, कृतवेधन: प्रत्येक",
                            "त्रिकटु, काढ़े के बराबर", "सब डाले (आवपेत्)"]},
        "anchors": "पिष्ट्वा = पीसकर · प्रत्येकम् = हर एक · त्रिकटु = सोंठ, पीपर, काली मिर्च · आवपेत् = डाले।",
        "contrast": "घृतसम = घी के बराबर (बीज) · क्वाथतुल्य = काढ़े के बराबर (त्रिकटु)।",
    },
    "53": {
        "chunks": "ततः | पुनरपि श्रुत्वा | लेहं साधयेत्।",
        "anchors": "ततः = फिर · पुनरपि = एक बार और · लेह = चाटने की गाढ़ी औषध · साधयेत् = तैयार करे।",
        "sandhi": "पुनः + अपि → पुनरपि (पुनर् का र् स्वर से पहले दिखता है)।",
    },
    "54": {
        "chain": {"steps": ["लेह चाटे (अवलिह्य)", "पीछे से पिए (अनुपिबेत्)",
                            "यही कल्प काश्मर्य आदि चार मूलों में", "अलग-अलग कहा जाने"]},
        "contrast": "बिना उपसर्ग -त्वा: पिष्ट्वा, पीत्वा · उपसर्ग के साथ -य: अवलिह्य, अनुपीय।",
        "anchors": "अवलिह्य = चाटकर · कल्प = विधि · काश्मर्य = गम्भारी · पृथक् पृथक् = अलग-अलग · वेदितव्य = जानने योग्य।",
    },
}


IMAGE_SPECS = {
    ("40", "diagram"): {
        "file": "ka1-ikshvaku-uses-40.svg",
        "alt": ("Mind map of unit 40: ikshvaku especially applied in six ailments: kasa, shvasa, jvara, "
                "chardi, visha and phlegm-ailments"),
        "type": "mermaid",
        "code": ("mindmap\n  इक्ष्वाकु विशेष रूप से\n    कास यानी खाँसी\n    श्वास\n    ज्वर यानी बुखार\n"
                 "    छर्दि यानी उल्टी\n    विष\n    कफ के रोग\n"),
    },
    ("42", "chain"): {
        "file": "ka1-juice-milk-42.svg",
        "alt": ("Flowchart of unit 42: expressed juice of the ikshvaku fruit, prepared in threefold milk, drunk by the "
                "patient desiring emesis, in pitta, kapha-pinasa and svarasada"),
        "type": "mermaid",
        "code": ('flowchart TD\n  A["इक्ष्वाकु-फल का स्वरस"] --> B["तिगुने दूध में तैयार"]\n'
                 '  B --> C["वमनार्थी रोगी पिए"]\n  C --> D["पित्त"]\n  C --> E["कफ-पीनस"]\n  C --> F["स्वरसाद"]\n'),
    },
    ("43", "chain"): {
        "file": "ka1-fruit-curd-43.svg",
        "alt": ("Chain of verse 43: take an old fruit, take out its seeds, pour milk into it, and the curd forms in it"),
        "type": "chain",
        "title": "श्लोक ४३: फल में दही",
        "steps": ["पुराना फल", "बीज निकाले", "उसमें दूध डाले", "उसी में दही जमे"],
    },
    ("44", "diagram"): {
        "file": "ka1-seed-ailments-44.svg",
        "alt": ("Mind map of unit 44: ikshvaku seeds soaked in she-goat's milk, used in seven ailments: "
                "visha, gulma, udara, galaganda, granthi, arbuda and shlipada"),
        "type": "mermaid",
        "code": ("mindmap\n  बकरी के दूध में भीगे बीज\n    विष\n    गुल्म यानी पेट की गाँठ\n    उदर\n"
                 "    गलगण्ड यानी घेंघा\n    ग्रन्थि यानी गाँठ\n    अर्बुद यानी रसौली\n    श्लीपद यानी हाथीपाँव\n"),
    },
    ("46", "contrast"): {
        "file": "ka1-whey-buttermilk-46.svg",
        "alt": ("Table of verse 46: first line, the ikshvaku fruit with whey in kushtha, visha and pale-ailments; second "
                "line, sadripaka (unclear) or buttermilk with honey and rock salt"),
        "type": "table",
        "title": "श्लोक ४६: दो पंक्तियाँ",
        "heads": ["पंक्ति", "योग"],
        "rows": [["पहली", "फल + मस्तु: कुष्ठ, विष, पाण्डु"], ["दूसरी", "सद्रिपक (अस्पष्ट)"],
                 ["दूसरी", "तक्र + मधु + सेंधा नमक"]],
    },
    ("50", "chain"): {
        "file": "ka1-paste-broth-50.svg",
        "alt": ("Flowchart of unit 50: ikshvaku paste with meat broth, in vata-kapha, gulma and persistent fevers"),
        "type": "mermaid",
        "code": ('flowchart TD\n  A["इक्ष्वाकु का कल्क"] --> B["मांस-रस के साथ"]\n'
                 '  B --> C["वात-कफ"]\n  B --> D["गुल्म"]\n  B --> E["लगे रहने वाले ज्वर"]\n'),
    },
    ("52", "chain"): {
        "file": "ka1-tumbi-additions-52.svg",
        "alt": ("Flowchart of unit 52: into the ghee-liquid go ground tumbi seeds equal to the ghee, then each of jimuta, "
                "mahajalini, vatsaka and kritavedhana, then trikatuka equal to the decoction, all added"),
        "type": "mermaid",
        "code": ('flowchart TD\n  A["बेल-जड़ का काढ़ा और घी"] --> B["तुम्बी-बीज पीसे<br/>घी के बराबर"]\n'
                 '  B --> C["जीमूत, महाजालिनी<br/>वत्सक, कृतवेधन"]\n  C --> D["त्रिकटु<br/>काढ़े के बराबर"]\n'
                 '  D --> E["सब डाले"]\n'),
    },
    ("54", "chain"): {
        "file": "ka1-lick-kalpa-54.svg",
        "alt": ("Flowchart of unit 54: the leha is licked, a drink follows after it, and the same procedure is to be known "
                "as stated separately for the four members of the great five roots beginning with kashmarya"),
        "type": "mermaid",
        "code": ('flowchart TD\n  A["लेह चाटे"] --> B["पीछे से पिए"]\n'
                 '  B --> C["यही कल्प"]\n  C --> D["काश्मर्य आदि चार<br/>महापञ्चमूल-अंग"]\n'
                 '  D --> E["अलग-अलग कहा<br/>ऐसा जानें"]\n'),
    },
}
