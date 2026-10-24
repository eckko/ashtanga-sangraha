from helpers import mcq, match, order, fill, multi, accepts


AUTHORED = {}

# ---------------------------------------------------------------- unit 52
AUTHORED["52"] = {
    "title": "पंचमी पुरीषधरा नाम",
    "question": "By unit 52, what is the fifth kalā, and what does it do with the mala?",
    "rule": ("Fifth kalā: Purīṣadharā ('faeces-bearing'). It separates (विभजति) the mala (waste, faeces) that lies in the "
             "unduka (probably the caecum), within the koṣṭha (storehouse), on one possible reading."),
    "limits": ("Prose. Printed मा is read सा on a possible correction. 'Resting on the intestine and the āma and pakva "
               "seats' and 'within the koṣṭha, in the unduka' are uncertain in sense (the join कोष्ठ + अन्तर् is sure); "
               "unduka = caecum is probable. No question on these."),
    "explain_hi": ("सात कलाओं में पाँचवीं कला पुरीषधरा, यानी पुरीष (मल) धारण करने वाली, है। "
                   "यह कोष्ठ के भीतर उण्डुक (सम्भवतः अन्धान्त्र) में स्थित मल को अलग करती है (विभजति)। "
                   "‘अन्त्रामपक्वाशयाश्रिता’ को ‘अन्त्र और आम-पक्व आशयों पर टिकी’ पढ़ा गया है, पर यह पाठ पक्का नहीं। "
                   "छपा ‘मा’ सम्भवतः ‘सा’ (वह) है; यह सुधार सम्भावित है। "
                   "इन अनिश्चित अंशों पर कोई प्रश्न नहीं।"),
    "hook": "पाँचवीं कला: मल को अलग करे।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 52, what is the fifth kalā named?",
            ("पुरीषधरा", "पंचमी पुरीषधरा नाम."),
            [("पित्तधरा", "Pittadharā is the sixth kalā (unit 53)."),
             ("श्लेष्मधरा", "Śleṣmadharā is the fourth kalā (unit 51)."),
             ("शुक्रधरा", "Śukradharā is the seventh kalā (unit 55).")],
            "The fifth kalā is Purīṣadharā, faeces-bearing.",
            "पंचमी पुरीषधरा नाम."),
        order(1, "Put these printed words of unit 52 in the line's order.",
              ["पंचमी पुरीषधरानाम", "ह्यंत्रामपक्वाशयाश्रिता", "कोष्ठांतरुंदुकस्थं", "मलं", "विभजति"],
              "The fifth, named Purīṣadharā; resting on the intestine (and the seats); lying in the unduka within the koṣṭha; "
              "the mala; it separates.",
              "पंचमी पुरीषधरानाम → ह्यंत्रामपक्वाशयाश्रिता → कोष्ठांतरुंदुकस्थं → मलं → विभजति."),
        match(2, "Match each word of unit 52 to its meaning.",
              [["पञ्चमी", "fifth"], ["पुरीष", "faeces"], ["कोष्ठ", "storehouse (trunk)"], ["आश्रिता", "resting on"],
               ["विभजति", "separates, divides"]],
              "The fifth kalā, faeces-bearing, resting on the seats, separates the mala in the koṣṭha.",
              "पञ्चमी, पुरीष, कोष्ठ, आश्रिता, विभजति.", role="extend",
              teaches="पुरीषधरा = पुरीष (faeces) + धरा (bearing): the kalā is named for what it holds."),
        mcq("discriminate", 3, "Which split of ह्यंत्र... in unit 52 is right?",
            ("हि + अन्त्र", "इ before a dissimilar vowel becomes य्: हि + अन्त्र → ह्यन्त्र."),
            [("हि + यन्त्र", "हि before य stays हि: that would be printed हि यन्त्र."),
             ("हे + अन्त्र", "ए + अ would give हेऽन्त्र, not ह्यन्त्र."),
             ("ह्य + अन्त्र", "ह्य is not a word, and अ + अ would give ह्यान्त्र.")],
            "हि (indeed) + अन्त्र (intestine): इ + अ → य.",
            "इ + dissimilar vowel → य्."),
        mcq("apply", 4, "By unit 52, what does Purīṣadharā do with the mala?",
            ("It separates it (विभजति)", "मलं विभजति: it separates the mala."),
            [("It cooks it fully (पचति)", "Cooking is said of Pittadharā (unit 53), not of this kalā."),
             ("It dries it out (शोषयति)", "Drying by Pitta's heat is Pittadharā's work (unit 53)."),
             ("It sets it moving (प्रवर्तयति)", "Setting in motion is said of śukra by Śukradharā (unit 55).")],
            "Purīṣadharā separates the mala.",
            "मलं विभजति."),
        mcq("transfer", 5, "By the rule of कोष्ठ + अन्तर् → कोष्ठान्तर्, how is वेद + अन्तः joined?",
            ("वेदान्तः", "अ + अ → आ, as कोष्ठ + अन्तर् → कोष्ठान्तर्."),
            [("वेदेन्तः", "ए comes from अ + इ, not from अ + अ."),
             ("वेदोन्तः", "ओ comes from अ + उ, not from अ + अ."),
             ("वेदन्तः", "Two short अ sounds merge into a long आ, not a short अ.")],
            "वेद + अन्तः = वेदान्तः, like कोष्ठ + अन्तर् = कोष्ठान्तर्.",
            "अ + अ → आ.",
            teaches="A short अ followed by a short अ joins as long आ: कोष्ठ + अन्तर् → कोष्ठान्तर्."),
    ],
}

# ---------------------------------------------------------------- unit 53
AUTHORED["53"] = {
    "title": "षष्ठी पित्तधरा नाम",
    "question": "By unit 53, where does Pittadharā lie, and what does it do with the food?",
    "rule": ("Sixth kalā: Pittadharā, between the pakva and āma seats. Being the seat of the inner fire, it holds by force "
             "the food heading to the pakvāśaya, dries it by Pitta's heat, cooks it, and releases the cooked."),
    "limits": ("Prose. āmāśaya = stomach and pakvāśaya = large intestine are probable equivalents only. The line gives no "
               "time or quantity. The doubled avagraha is a print habit; printed पक्कं = पक्वम्, विधार्य्य = विधार्य."),
    "explain_hi": ("छठी कला पित्तधरा है, जो पक्व (पके) और आम (कच्चे) के आशयों के बीच में स्थित है। "
                   "भीतरी अग्नि (अन्तरग्नि) का अधिष्ठान होने से यह आमाशय से पक्वाशय की ओर जाते अन्न को बल से रोकती है। "
                   "फिर पित्त के तेज से उसे सुखाती हुई पकाती है और पके हुए को छोड़ देती है। "
                   "आमाशय = सम्भवतः जठर, पक्वाशय = सम्भवतः बड़ी आँत; ये आधुनिक नाम केवल सम्भावित हैं।"),
    "hook": "रोके, सुखाए, पकाए, छोड़े: पित्तधरा का काम।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 53, where does Pittadharā lie?",
            ("Between the pakva and āma seats", "पक्वामाशयमध्यस्था: in the middle of the pakva and āma seats."),
            [("Below the opening of the basti", "That is the place of Śukradharā (unit 55)."),
             ("Inside the flesh, with the blood", "That is Raktadharā, the second kalā (unit 49)."),
             ("In the head, under the skull", "Fat in the head, under the skull, is described with Medodharā (unit 50).")],
            "Pittadharā lies between the seats of the digested and the raw.",
            "पक्वामाशयमध्यस्था."),
        order(1, "Put these phrases of unit 53 in the line's order.",
              ["आमाशयात्पक्वाशयोन्मुखमन्नं", "बलेन विधार्य्य", "पित्ततेजसा शोषयंती", "पचति", "पक्कं च विमुंचति"],
              "The food heading from the āmāśaya to the pakvāśaya; held by force; dried by Pitta's heat; cooked; the cooked "
              "released.",
              "अन्नं → बलेन विधार्य्य → पित्ततेजसा शोषयंती → पचति → पक्कं च विमुंचति."),
        match(2, "Match each word of unit 53 to its meaning.",
              [["अन्तरग्नि", "inner fire"], ["अधिष्ठान", "seat"], ["उन्मुख", "facing toward"], ["शोषयन्ती", "drying"],
               ["विमुञ्चति", "releases"]],
              "As seat of the inner fire, it holds the food facing the pakvāśaya, dries it, cooks it and releases it.",
              "अन्तरग्नि, अधिष्ठान, उन्मुख, शोषयन्ती, विमुञ्चति.", role="extend",
              teaches="अन्तरग्नि = the inner (digestive) fire; Pittadharā is its seat (अधिष्ठान)."),
        mcq("discriminate", 3, "Which split of पक्वाशयोन्मुखम् is right?",
            ("पक्वाशय + उन्मुखम्", "अ + उ → ओ: पक्वाशय + उन्मुखम् → पक्वाशयोन्मुखम्."),
            [("पक्वाशयः + उन्मुखम्", "अः before उ drops its visarga: that would give पक्वाशय उन्मुखम्."),
             ("पक्वाशयो + न्मुखम्", "न्मुखम् is not a word; the word is उन्मुखम् (facing toward)."),
             ("पक्वाशये + उन्मुखम्", "ए + उ does not give ओ; ए before a vowel becomes अय् (or अ).")],
            "पक्वाशय (seat of the digested) + उन्मुखम् (facing toward): अ + उ → ओ.",
            "अ + उ → ओ."),
        multi("apply", 4, "By unit 53, which does Pittadharā do to the food?",
              [("Holds it by force", "Right: बलेन विधार्य."),
               ("Separates the waste in the unduka", "That is Purīṣadharā's work (unit 52)."),
               ("Dries it by the heat of Pitta", "Right: पित्ततेजसा शोषयन्ती."),
               ("Makes it pervade the whole body", "Pervading the whole body is said of Śukradharā (unit 55)."),
               ("Releases what is cooked", "Right: पक्वं च विमुञ्चति.")],
              [0, 2, 4],
              "It holds the food by force, dries it by Pitta's heat, cooks it and releases the cooked.",
              "बलेन विधार्य, पित्ततेजसा शोषयन्ती पचति, पक्वं च विमुञ्चति."),
        mcq("transfer", 5, "By the rule of पक्वाशय + उन्मुखम्, how is सूर्य + उदयः (sunrise) joined?",
            ("सूर्योदयः", "अ + उ → ओ, as पक्वाशय + उन्मुखम् → पक्वाशयोन्मुखम्."),
            [("सूर्यौदयः", "औ comes from अ + ओ or औ, not from अ + उ."),
             ("सूर्यूदयः", "अ + उ does not give ऊ; ऊ comes from उ + उ."),
             ("सूर्यादयः", "आ comes from अ + अ, not from अ + उ.")],
            "सूर्य + उदयः = सूर्योदयः, like पक्वाशय + उन्मुखम् = पक्वाशयोन्मुखम्.",
            "अ + उ → ओ.",
            teaches="अ followed by उ joins as ओ: पक्वाशय + उन्मुखम् → पक्वाशयोन्मुखम्."),
    ],
}

# ---------------------------------------------------------------- unit 54
AUTHORED["54"] = {
    "title": "ततोऽसावन्नस्य ग्रहणात्पुनर्ग्रहणीसंज्ञा",
    "question": "By unit 54, why is the organ called grahaṇī, and what is its strength?",
    "rule": ("From its taking up (ग्रहण) of food it has the name grahaṇī. Its strength (बल) is Pitta itself, which is named "
             "agni (fire); it keeps the body going (शरीरं वर्तयति); 'supported by the fire' rests on a possible correction of printed नाए."),
    "limits": ("Prose. The opening clause (दोषाधिष्ठिता तु दौर्बल्यादाममेव) has no verb; its sense is only probable. "
               "असौ points back to the layer of unit 53, which this line does not name. The misprinted 'नाए', the parse of "
               "एकयोगक्षेमा and grahaṇī = duodenum or small-intestine region (disputed): no question on these."),
    "explain_hi": ("यह गद्य-पंक्ति ग्रहणी नाम का कारण बताती है: अन्न को ग्रहण करने (पकड़ने) से उसका नाम ग्रहणी है। "
                   "‘असौ’ (वह) इकाई ५३ की कला की ओर संकेत करता है, जिसका नाम यहाँ नहीं लिया गया। "
                   "उसका बल पित्त ही है, जिसका नाम अग्नि है; वह शरीर को चलाती है; ‘अग्नि से सहारा पाकर’ एक सम्भावित सुधार (छपा ‘नाए’) पर टिका है। "
                   "पहला खण्ड (दोषों से अधिष्ठित होने पर दुर्बलता से केवल आम) बिना क्रिया का है, उसका अर्थ केवल सम्भावित है। "
                   "ग्रहणी का आधुनिक नाम (ड्यूओडिनम या छोटी आँत का क्षेत्र) विवादित है।"),
    "hook": "अन्न को ग्रहण करे, इसलिए ग्रहणी; बल उसका पित्त-अग्नि।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 54, why does the organ get the name grahaṇī?",
            ("From its taking up of the food", "अन्नस्य ग्रहणात्: from its taking up of food."),
            [("From its place below the basti", "The place below the basti is Śukradharā's (unit 55)."),
             ("From its holding of the semen", "Holding śukra is Śukradharā's work (unit 55)."),
             ("From its being made of fat", "Fat belongs to Medodharā (unit 50).")],
            "It takes up (ग्रहण) food, so it is named grahaṇī.",
            "अन्नस्य ग्रहणात् ग्रहणीसंज्ञा."),
        order(1, "Put these phrases of unit 54 in the line's order.",
              ["ततोऽसावन्नस्य ग्रहणात्", "पुनर्ग्रहणीसंज्ञा", "बलं च तस्याः", "पित्तमेवाग्न्याभिधानम्", "शरीरं वर्त्तयति"],
              "Hence, from its taking up of food, again the name grahaṇī; and its strength is Pitta itself, named agni; it "
              "keeps the body going.",
              "ग्रहणात् → ग्रहणीसंज्ञा → बलं च तस्याः → पित्तमेव... → शरीरं वर्त्तयति."),
        match(2, "Match each word of unit 54 to its meaning.",
              [["ग्रहण", "taking up, grasping"], ["संज्ञा", "name"], ["बल", "strength"], ["शरीर", "body"],
               ["वर्तयति", "keeps going, sustains"]],
              "From taking up food, the name grahaṇī; its strength is Pitta; it keeps the body going.",
              "ग्रहण, संज्ञा, बल, शरीर, वर्तयति.", role="extend",
              teaches="ग्रहणी is named from ग्रहण (taking up): the organ that takes up the food."),
        mcq("discriminate", 3, "Which split of ततोऽसावन्नस्य is right?",
            ("ततः + असौ + अन्नस्य", "अः + अ → ओऽ; औ before a vowel → आव्."),
            [("तत् + असौ + अन्नस्य", "त् before a vowel becomes द्: that would give तदसौ."),
             ("ततो + असाव + अन्नस्य", "ततो and असाव are not the words; they are ततः and असौ."),
             ("ततः + असा + वन्नस्य", "असा and वन्नस्य are not words; the words are असौ and अन्नस्य.")],
            "ततः (hence) + असौ (that one) + अन्नस्य (of food).",
            "अः + अ → ओऽ; औ + vowel → आव्."),
        mcq("apply", 4, "By unit 54, what is the strength (बल) of the grahaṇī?",
            ("Pitta itself, which is named agni", "बलं च तस्याः पित्तमेव अग्न्यभिधानम्."),
            [("Kapha, which holds the joints firm", "Kapha holding the joints is Śleṣmadharā's (unit 51)."),
             ("Vāyu, which carries the food on", "The unit names Pitta, not Vāyu, as its strength."),
             ("The blood of the liver and spleen", "Blood in the liver and spleen is Raktadharā's (unit 49).")],
            "Its strength is Pitta itself, which has the name agni.",
            "बलं च तस्याः पित्तमेव."),
        mcq("transfer", 5, "By the rule of असौ + अन्नस्य → असावन्नस्य, how is तौ + इति (those two, thus) joined?",
            ("ताविति", "औ before a vowel becomes आव्, as असौ + अन्नस्य → असावन्नस्य."),
            [("तायिति", "आय् comes from ऐ before a vowel, not from औ."),
             ("तविति", "अव् comes from ओ; औ gives आव् with a long आ."),
             ("तौइति", "औ does not stay unchanged before a vowel inside a sentence.")],
            "तौ + इति = ताविति, like असौ + अन्नस्य = असावन्नस्य.",
            "औ + vowel → आव्.",
            teaches="औ before a vowel becomes आव्: असौ + अन्नस्य → असावन्नस्य."),
    ],
}

# ---------------------------------------------------------------- unit 55
AUTHORED["55"] = {
    "title": "सप्तमी शुक्रधरा नाम",
    "question": "By unit 55, where is Śukradharā placed, and what does it do?",
    "rule": ("Seventh kalā: Śukradharā ('semen-bearing'). At two aṅgulas on the right side and below the opening of the basti (bladder, probable), "
             "resting on the urinary passage, pervading the whole body, it sets śukra (semen) in motion."),
    "limits": ("Prose. 'Two aṅgulas' from what is not stated: no question on it. basti = urinary bladder is probable here. "
               "The line does not say how śukra flows or pervades."),
    "explain_hi": ("सातवीं कला शुक्रधरा, यानी शुक्र (वीर्य) धारण करने वाली, है। "
                   "यह दाहिने पार्श्व में दो अंगुल पर और बस्ति (सम्भवतः मूत्राशय) के द्वार के नीचे, मूत्रमार्ग पर टिकी है। "
                   "यह सारे शरीर में फैली हुई है और शुक्र को प्रवृत्त करती है। "
                   "दो अंगुल किस स्थान से, यह पंक्ति नहीं कहती।"),
    "hook": "सातवीं कला: दाहिनी ओर, बस्ति-द्वार के नीचे, शुक्र को प्रवृत्त करे।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 55, what does Śukradharā do?",
            ("It sets śukra (semen) in motion", "शुक्रं प्रवर्त्तयति."),
            [("It holds the Kapha (joints firm)", "Kapha in the joints is Śleṣmadharā's (unit 51)."),
             ("It separates the mala (in unduka)", "Separating the mala is Purīṣadharā's (unit 52)."),
             ("It cooks the food (Pitta's heat)", "Cooking by Pitta's heat is Pittadharā's (unit 53).")],
            "Śukradharā sets śukra in motion.",
            "शुक्रं प्रवर्त्तयति."),
        order(1, "Put these phrases of unit 55 in the line's order.",
              ["सप्तमी शुक्रधरा नाम", "द्व्यंगुले दक्षिणे पार्श्वे", "बस्तिद्वारस्य चाधो", "मूत्रमार्गमाश्रिता",
               "सकलशरीरव्यापिनी", "शुक्रं प्रवर्त्तयति"],
              "The seventh, Śukradharā; at two aṅgulas on the right side; and below the basti's opening (bladder, probable); resting on the "
              "urinary passage; pervading the whole body; it sets śukra in motion.",
              "नाम → द्व्यंगुले... → बस्तिद्वारस्य चाधो → मूत्रमार्गमाश्रिता → सकलशरीरव्यापिनी → शुक्रं प्रवर्त्तयति."),
        match(2, "Match each word of unit 55 to its meaning.",
              [["दक्षिण", "right"], ["पार्श्व", "flank, side"], ["बस्तिद्वार", "opening of the basti (bladder, probable)"],
               ["मूत्रमार्ग", "urinary passage"], ["व्यापिनी", "pervading"]],
              "On the right side, below the basti's opening (bladder, probable), on the urinary passage, pervading the body.",
              "दक्षिण, पार्श्व, बस्तिद्वार, मूत्रमार्ग, व्यापिनी.", role="extend",
              teaches="बस्ति here = the bladder (urinary bladder, probable); बस्तिद्वार = its opening."),
        mcq("discriminate", 3, "Which split of चाधो (before मूत्रमार्ग) in unit 55 is right?",
            ("च + अधः", "अ + अ → आ, and अः before the voiced consonant म becomes ओ."),
            [("चा + अधः", "चा is not a word; the particle is च (and)."),
             ("च + अधम्", "म् would not become ओ; it would stay as म् or ं."),
             ("चे + अधः", "ए + अ would give चेऽधः, not चाधः.")],
            "च (and) + अधः (below): अ + अ → आ; अधः + मूत्र → अधो मूत्र.",
            "अ + अ → आ; अः + voiced consonant → ओ."),
        multi("apply", 4, "By unit 55, which describe the place of Śukradharā?",
              [("On the right side", "Right: दक्षिणे पार्श्वे."),
               ("Below the basti's opening", "Right: बस्तिद्वारस्य चाधः; basti = bladder, probable."),
               ("Above the navel, on the left", "The unit says the right side, and names no navel."),
               ("Resting on the urinary passage", "Right: मूत्रमार्गमाश्रिता."),
               ("Between the āma and pakva seats", "That is the place of Pittadharā (unit 53).")],
              [0, 1, 3],
              "Right side, below the basti's opening (bladder, probable), resting on the urinary passage.",
              "दक्षिणे पार्श्वे बस्तिद्वारस्य चाधो मूत्रमार्गमाश्रिता."),
        fill(5, "By the rule of द्वि + अङ्गुले → द्व्यङ्गुले, join प्रति + अक्षम्. Type it in Devanagari or in English letters "
                "(e.g. dharma): ____",
             accepts("प्रत्यक्षम्"),
             "प्रति + अक्षम् = प्रत्यक्षम्: इ before the dissimilar vowel अ becomes य्, as in द्व्यङ्गुले.",
             "इ before a dissimilar vowel becomes य्: द्वि + अङ्गुले → द्व्यङ्गुले.",
             "इ + dissimilar vowel → य्.", role="transfer"),
    ],
}

# ---------------------------------------------------------------- unit 56
AUTHORED["56"] = {
    "title": "दोषा धातवोमलाश्च प्रागुदिताः",
    "question": "What does unit 56 say about the doṣas, dhātus and malas?",
    "rule": ("The line points back: the doṣas, the dhātus and the malas have been stated before (प्राक् उदिताः)."),
    "limits": ("Prose, one short line. It does not say where they were stated and names none of them; the copula is "
               "supplied. No question on where."),
    "explain_hi": ("यह छोटी गद्य-पंक्ति पीछे की ओर संकेत करती है: दोष, धातु और मल पहले कहे जा चुके हैं। "
                   "कहाँ कहे गए, यह पंक्ति नहीं बताती, और किसी दोष, धातु या मल का नाम यहाँ नहीं है। "
                   "‘प्रागुदिताः’ = प्राक् (पहले) + उदिताः (कहे गए); स्वर से पहले क् का ग् हुआ है। "
                   "क्रिया (हैं) समझी जाती है।"),
    "hook": "दोष, धातु, मल: पहले कहे जा चुके।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 56, what is said of the doṣas, dhātus and malas?",
            ("They have been stated before", "प्रागुदिताः: stated before."),
            [("They will be stated in the next part", "प्राक् means before, not later."),
             ("They are the same as the kalās", "The line does not equate them with the kalās."),
             ("They are not taught in this book", "They have been stated before, so they are taught.")],
            "They have been stated before (प्राक् उदिताः).",
            "प्राक् + उदिताः = stated before."),
        order(1, "Put the three names of unit 56 in the line's order.",
              ["दोषाः", "धातवः", "मलाः"],
              "The doṣas, the dhātus and the malas have been stated before.",
              "दोषाः → धातवः → मलाः."),
        fill(2, "Type the word of unit 56 that means 'before', in Devanagari or in English letters (e.g. dharma): ____",
             accepts("प्राक्", "prāk", "प्राग्", "prak", "prag"),
             "प्राक् (before) + उदिताः (stated) → प्रागुदिताः.",
             "प्राक् = before; before a vowel its क् becomes ग्: प्राक् + उदिताः → प्रागुदिताः.",
             "प्राक् + उदिताः → प्रागुदिताः."),
        mcq("discriminate", 3, "Why is दोषाः printed दोषा before धातवः?",
            ("After आ, the visarga drops before a voiced sound", "ध is voiced, so दोषाः → दोषा."),
            [("After आ, the visarga becomes ओ before a voiced ध", "ओ comes from a visarga after short अ, not after आ."),
             ("दोषा is the feminine singular form", "The data reads दोषाः, masculine nominative plural."),
             ("A visarga drops before every consonant of any kind", "Before unvoiced sounds it stays or changes; it is not dropped.")],
            "दोषाः + धातवः = दोषा धातवः: आः before a voiced sound loses its visarga.",
            "आः + voiced sound → आ."),
        mcq("apply", 4, "Why does मलाः become मलाश् before च in unit 56?",
            ("Before च, a visarga becomes श्", "विसर्ग + च → श्च: मलाः + च → मलाश्च."),
            [("Before च, a visarga becomes र्", "र् arises after vowels other than अ/आ before voiced sounds; च is unvoiced."),
             ("Before च, a visarga becomes स्", "स् arises before त or थ, not before च."),
             ("Before च, a visarga becomes ओ", "ओ arises from अः before a voiced consonant; च is unvoiced.")],
            "मलाः + च = मलाश्च: before च the visarga becomes श्.",
            "Visarga + च → श्च."),
        mcq("transfer", 5, "By the rule of धातवः + मलाः → धातवो मलाः, how is बालः + गच्छति (the boy goes) written?",
            ("बालो गच्छति", "अः before the voiced consonant ग becomes ओ, as धातवः + मलाः."),
            [("बाला गच्छति", "Dropping the visarga to आ is the rule after आ, not after short अ."),
             ("बालर्गच्छति", "र् comes after vowels other than अ and आ."),
             ("बालः गच्छति", "Before a voiced consonant the visarga after अ does not stay.")],
            "बालः + गच्छति = बालो गच्छति, like धातवः + मलाः = धातवो मलाः.",
            "अः + voiced consonant → ओ.",
            teaches="अः before a voiced consonant becomes ओ: धातवः + मलाः → धातवो मलाः."),
    ],
}

# ---------------------------------------------------------------- unit 57
AUTHORED["57"] = {
    "title": "पंच बुद्धींद्रियाणि",
    "question": "By unit 57, what are the five sense-organs of cognition, and what are their objects?",
    "rule": ("Five buddhīndriyas: śrotra (hearing), sparśana (touch), darśana (sight), rasana (taste), ghrāṇa (smell). "
             "Their objects (विषय), in order (क्रमात्): śabda (sound), sparśa (touch), rūpa (form), rasa (taste), gandha (smell)."),
    "limits": ("Prose, two printed lines. समभागतया ('by equal shares') is rendered literally; that it means one object for "
               "each organ is only presumed: no question on it. The seats (organs) of the five come in unit 58."),
    "explain_hi": ("ज्ञान की पाँच इन्द्रियाँ (बुद्धीन्द्रियाँ) हैं: श्रोत्र, स्पर्शन, दर्शन, रसन और घ्राण। "
                   "उनके विषय क्रम से शब्द, स्पर्श, रूप, रस और गन्ध हैं। "
                   "‘समभागतया’ (समान भाग होने से) का शब्दार्थ ही रखा गया है; इसका अर्थ सम्भवतः हर इन्द्रिय का एक विषय है, पर पंक्ति इससे अधिक नहीं कहती। "
                   "इन इन्द्रियों के अधिष्ठान (कान, त्वचा आदि) इकाई ५८ में आते हैं।"),
    "hook": "सुनना, छूना, देखना, चखना, सूँघना; शब्द, स्पर्श, रूप, रस, गन्ध।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 57, which of these is one of the five buddhīndriyas?",
            ("घ्राण (smell)", "घ्राणं च: smell is the fifth in the list."),
            [("पाणि (hand)", "The hand is an organ of action (unit 58)."),
             ("पाद (foot)", "The foot is an organ of action (unit 58)."),
             ("उपस्थ (genital organ)", "The genital organ is an organ of action (unit 58).")],
            "The five are śrotra, sparśana, darśana, rasana and ghrāṇa.",
            "श्रोत्रं स्पर्शनं दर्शनं रसनं घ्राणं च."),
        order(1, "Put the five buddhīndriyas of unit 57 in the line's order.",
              ["श्रोत्रम्", "स्पर्शनम्", "दर्शनम्", "रसनम्", "घ्राणम्"],
              "Hearing, touch, sight, taste, smell.",
              "श्रोत्रम् → स्पर्शनम् → दर्शनम् → रसनम् → घ्राणम्."),
        match(2, "Match each object (viṣaya) of unit 57 to its meaning.",
              [["शब्द", "sound"], ["स्पर्श", "touch"], ["रूप", "form"], ["रस", "taste"], ["गन्ध", "smell"]],
              "The objects in order: sound, touch, form, taste, smell.",
              "शब्द, स्पर्श, रूप, रस, गन्ध.", role="extend",
              teaches="विषय = the object of a sense: शब्द, स्पर्श, रूप, रस, गन्ध."),
        mcq("discriminate", 3, "Which split of बुद्धींद्रियाणि is right?",
            ("बुद्धि + इन्द्रियाणि", "इ + इ → ई: बुद्धि + इन्द्रियाणि → बुद्धीन्द्रियाणि."),
            [("बुद्धिं + द्रियाणि", "द्रियाणि is not a word; the word is इन्द्रियाणि."),
             ("बुद्धे + इन्द्रियाणि", "ए + इ does not give ई."),
             ("बुद्धः + इन्द्रियाणि", "अः + इ would give बुद्ध इन्द्रियाणि.")],
            "बुद्धि (cognition) + इन्द्रियाणि (sense-organs): इ + इ → ई.",
            "इ + इ → ई."),
        mcq("apply", 4, "A learner lists the objects as शब्द, रूप, स्पर्श, रस, गन्ध. By unit 57, what is wrong?",
            ("रूप and स्पर्श are swapped", "The printed order is शब्द, स्पर्श, रूप, रस, गन्ध."),
            [("रस and गन्ध are swapped", "रस comes before गन्ध, as the learner has it."),
             ("शब्द should come last", "शब्द comes first in the printed list."),
             ("Nothing: it is the printed order", "The printed order puts स्पर्श before रूप.")],
            "The printed order is शब्द, स्पर्श, रूप, रस, गन्ध.",
            "शब्दस्पर्शरूपरसगन्धाः."),
        mcq("transfer", 5, "By the rule of बुद्धि + इन्द्रियाणि, how is मुनि + इन्द्रः (chief of sages) joined?",
            ("मुनीन्द्रः", "इ + इ → ई, as बुद्धि + इन्द्रियाणि → बुद्धीन्द्रियाणि."),
            [("मुन्यिन्द्रः", "य् arises only before a dissimilar vowel; इ + इ is similar."),
             ("मुनेन्द्रः", "ए comes from अ + इ, not from इ + इ."),
             ("मुनिन्द्रः", "Two इ sounds make a long ई, not a short इ.")],
            "मुनि + इन्द्रः = मुनीन्द्रः, like बुद्धि + इन्द्रियाणि = बुद्धीन्द्रियाणि.",
            "इ + इ → ई.",
            teaches="Two इ sounds join as long ई: बुद्धि + इन्द्रियाणि → बुद्धीन्द्रियाणि."),
    ],
}

# ---------------------------------------------------------------- unit 58
AUTHORED["58"] = {
    "title": "पंच बुद्धींद्रियाधिष्ठानानि",
    "question": "By unit 58, what are the seats of the five sense-organs, and which are the five organs of action?",
    "rule": ("Seats of the buddhīndriyas: the two ears, the skin, the two eyes, the tongue, the two nostrils. Five "
             "karmendriyas: speech (on a possible correction), anus (apāyu), genital organ (upastha), hand, foot."),
    "limits": ("Prose, two printed lines. The first karmendriya is read वाक् (speech) on a possible correction of printed "
               "वाव-: no question rests on it. Printed जिव्हा = जिह्वा (spelling variant). No function is given here; "
               "the purposes follow in unit 59."),
    "explain_hi": ("ज्ञानेन्द्रियों के अधिष्ठान हैं: दोनों कान, त्वचा, दोनों आँखें, जीभ और दोनों नासिकाएँ। "
                   "कर्म की पाँच इन्द्रियाँ हैं: वाक् (वाणी), अपायु (गुदा), उपस्थ (जननेन्द्रिय), पाणि (हाथ) और पाद (पैर)। "
                   "छपा ‘वाव-’ सम्भवतः ‘वाग्-’ की भूल है, इसलिए ‘वाक्’ एक सम्भावित सुधार पर टिका है। "
                   "कर्णौ, अक्षिणी और नासिके द्विवचन हैं; त्वक् और जिह्वा एकवचन। "
                   "इनके प्रयोजन इकाई ५९ में आते हैं।"),
    "hook": "कान, त्वचा, आँख, जीभ, नाक; और कर्म के लिए वाक्, गुदा, उपस्थ, हाथ, पैर।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 58, which of these is a karmendriya (organ of action)?",
            ("पाणि (hand)", "पाणि is one of the five organs of action."),
            [("त्वक् (skin)", "The skin is a seat of a sense-organ of cognition."),
             ("अक्षि (eye)", "The eyes are a seat of a sense-organ of cognition."),
             ("कर्ण (ear)", "The ears are a seat of a sense-organ of cognition.")],
            "The hand (पाणि) is an organ of action.",
            "...उपस्थपाणिपादसंज्ञकानि."),
        order(1, "Put the seats of the buddhīndriyas in unit 58 in the line's order.",
              ["कर्णौ", "त्वक्", "अक्षिणी", "जिह्वा", "नासिके"],
              "The two ears, the skin, the two eyes, the tongue, the two nostrils.",
              "कर्णौ → त्वक् → अक्षिणी → जिह्वा → नासिके."),
        match(2, "Match each organ of action in unit 58 to its meaning.",
              [["अपायु", "anus"], ["उपस्थ", "genital organ"], ["पाणि", "hand"], ["पाद", "foot"]],
              "Four of the five organs of action: anus, genital organ, hand, foot.",
              "अपायु, उपस्थ, पाणि, पाद.", role="extend",
              teaches="अपायु = anus and उपस्थ = genital organ (both standard)."),
        multi("discriminate", 3, "By the data's grammar, which seats in unit 58 are named in the dual?",
              [("त्वक्", "Feminine nominative singular: one skin."),
               ("कर्णौ", "Right: masculine nominative dual, the two ears."),
               ("जिह्वा", "Feminine nominative singular: one tongue."),
               ("अक्षिणी", "Right: neuter nominative dual, the two eyes."),
               ("नासिके", "Right: feminine nominative dual, the two nostrils.")],
              [1, 3, 4],
              "कर्णौ, अक्षिणी and नासिके are duals; त्वक् and जिह्वा are singular.",
              "Dual endings here: -औ (m.), -ई (n.), -ए (f.)."),
        mcq("apply", 4, "Which split of त्वगक्षिणी is right?",
            ("त्वक् + अक्षिणी", "क् at the end of a word becomes ग् before a vowel."),
            [("त्वग + अक्षिणी", "त्वग is not the word, and अ + अ would give त्वगाक्षिणी."),
             ("त्वक् + क्षिणी", "क्षिणी is not a word; the word is अक्षिणी (the two eyes)."),
             ("त्वचा + अक्षिणी", "आ + अ would give त्वचाक्षिणी, with no ग्.")],
            "त्वक् (skin) + अक्षिणी (the two eyes): क् → ग् before a vowel.",
            "Final क् + vowel → ग्."),
        mcq("transfer", 5, "By the rule of त्वक् + अक्षिणी → त्वगक्षिणी, how is दिक् + अन्तः (horizon) joined?",
            ("दिगन्तः", "Final क् becomes ग् before a vowel, as त्वक् + अक्षिणी."),
            [("दिकन्तः", "Before a vowel the final क् becomes the voiced ग्."),
             ("दिङन्तः", "ङ् arises before a nasal, not before a vowel."),
             ("दिगान्तः", "The short अ of अन्तः stays short.")],
            "दिक् + अन्तः = दिगन्तः, like त्वक् + अक्षिणी = त्वगक्षिणी.",
            "Final क् + vowel → ग्.",
            teaches="A word-final क् becomes ग् before a vowel: त्वक् + अक्षिणी → त्वगक्षिणी."),
    ],
}

# ---------------------------------------------------------------- unit 59
AUTHORED["59"] = {
    "title": "तान्यपिच वचनोत्सर्गहर्षादानगमनार्थानि",
    "question": "By unit 59, what are the organs of action for, and why is the mind beyond the senses?",
    "rule": ("The organs of action serve speaking, discharge, delight, taking and going. The mind (मनस्) is beyond the "
             "sense-organs (अतीन्द्रिय), because of its association (अन्वय) with all objects."),
    "limits": ("Prose, two printed lines. The five purposes follow the order of the five organs of unit 58, but the text "
               "does not state which purpose belongs to which organ: no question pairs them. The copula is supplied."),
    "explain_hi": ("पहली पंक्ति: वे (कर्मेन्द्रियाँ) भी वचन, उत्सर्ग, हर्ष, आदान (ग्रहण) और गमन के लिए हैं। "
                   "ये पाँच प्रयोजन इकाई ५८ की पाँच इन्द्रियों के ही क्रम में हैं, पर कौन-सा प्रयोजन किस इन्द्रिय का है, यह पाठ नहीं कहता। "
                   "दूसरी पंक्ति: मन इन्द्रियों से परे (अतीन्द्रिय) है, क्योंकि उसका सब विषयों से अन्वय (सम्बन्ध) है। "
                   "‘अतीन्द्रियम्’ = अति + इन्द्रियम्।"),
    "hook": "बोलना, त्यागना, हर्ष, लेना, चलना; मन सब विषयों से जुड़ा, इसलिए इन्द्रियों से परे।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 59, why is the mind (manas) beyond the sense-organs?",
            ("Its association with all objects", "सर्वार्थैरन्वयात्: because of its association with all objects."),
            [("It is joined with no object at all", "The opposite: it is associated with all objects."),
             ("It lies wholly outside the body", "The line says nothing of the mind lying outside the body."),
             ("It works only through speech", "Speech is not named as the reason.")],
            "The mind is beyond the senses because it is associated with all objects.",
            "अतीन्द्रियं तु मनः सर्वार्थैरन्वयात्."),
        order(1, "Put the five purposes of unit 59 in the line's order.",
              ["वचन", "उत्सर्ग", "हर्ष", "आदान", "गमन"],
              "Speaking, discharge, delight, taking, going.",
              "वचन → उत्सर्ग → हर्ष → आदान → गमन."),
        match(2, "Match each word of the second line of unit 59 to its meaning.",
              [["अतीन्द्रिय", "beyond the sense-organs"], ["मनस्", "mind"], ["सर्वार्थ", "all objects"],
               ["अन्वय", "association, connection"]],
              "The mind is beyond the senses, from its association with all objects.",
              "अतीन्द्रिय, मनस्, सर्वार्थ, अन्वय.", role="extend",
              teaches="अन्वय = association, connection: the mind is linked with all objects."),
        mcq("discriminate", 3, "Which split of अतींद्रियं is right?",
            ("अति + इन्द्रियम्", "इ + इ → ई: अति + इन्द्रियम् → अतीन्द्रियम्."),
            [("अत् + इन्द्रियम्", "त् before a vowel would become द्: अदिन्द्रियम्."),
             ("अते + इन्द्रियम्", "ए + इ does not give ई."),
             ("अतिं + द्रियम्", "द्रियम् is not a word; the word is इन्द्रियम्.")],
            "अति (beyond) + इन्द्रियम् (sense-organ): इ + इ → ई.",
            "इ + इ → ई."),
        mcq("apply", 4, "In unit 59, what does आदान, one of the five purposes, mean?",
            ("Taking", "आदान = taking, grasping."),
            [("Giving", "Giving is दान; आ-दान is taking."),
             ("Going", "Going is गमन, the last purpose."),
             ("Speaking", "Speaking is वचन, the first purpose.")],
            "आदान = taking.",
            "आदान = taking."),
        mcq("transfer", 5, "By the rule of सर्वार्थैः + अन्वयात्, how is देवैः + उक्तम् (said by the gods) written?",
            ("देवैरुक्तम्", "After ऐ, a visarga becomes र् before a vowel, as सर्वार्थैः + अन्वयात्."),
            [("देवायुक्तम्", "आय् comes from ऐ without a visarga; here the visarga gives र्."),
             ("देवैः उक्तम्", "Before a vowel the visarga after ऐ does not stay; it becomes र्."),
             ("देवोक्तम्", "ओ comes from अ + उ; the word ends in ऐः.")],
            "देवैः + उक्तम् = देवैरुक्तम्, like सर्वार्थैः + अन्वयात् = सर्वार्थैरन्वयात्.",
            "Visarga after a vowel other than अ/आ → र् before a vowel or voiced consonant.",
            teaches="After a vowel other than अ/आ, a visarga becomes र् before a vowel: सर्वार्थैः + अन्वयात् → सर्वार्थैरन्वयात्."),
    ],
}

# ---------------------------------------------------------------- unit 60
AUTHORED["60"] = {
    "title": "तद्योगेन चेंद्रियाणामर्थप्रवृत्तिः",
    "question": "By unit 60, through what do the sense-organs engage with their objects?",
    "rule": ("Through union with it (तद्योगेन), that is the mind of unit 59, the sense-organs engage with their objects "
             "(अर्थप्रवृत्ति)."),
    "limits": ("Prose, one short line. तत् = the mind, as the data's note reads it from unit 59. The line does not say how "
               "the union happens; the copula is supplied."),
    "explain_hi": ("यह छोटी गद्य-पंक्ति कहती है: उसके (मन के) योग से इन्द्रियों की विषयों में प्रवृत्ति होती है। "
                   "‘तत्’ इकाई ५९ के मन की ओर संकेत करता है। "
                   "‘अर्थ’ यहाँ इन्द्रिय का विषय है। "
                   "योग कैसे होता है, यह पंक्ति नहीं बताती।"),
    "hook": "मन जुड़े, तभी इन्द्रिय विषय की ओर चले।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 60, through what do the sense-organs engage with their objects?",
            ("Through union with the mind", "तद्योगेन: by union with it, the mind."),
            [("Through the heat of Pitta", "Pitta's heat cooks the food in unit 53; it is not named here."),
             ("Through the strength of Kapha", "Kapha is not named in unit 60."),
             ("Through the seats (āśaya)", "The seats are listed later (unit 62), not named here.")],
            "Union with the mind makes the senses engage with their objects.",
            "तद्योगेन इन्द्रियाणामर्थप्रवृत्तिः."),
        order(1, "Put the words of unit 60 in the line's order.",
              ["तद्योगेन", "च", "इन्द्रियाणाम्", "अर्थप्रवृत्तिः"],
              "By union with it, and, of the sense-organs, the engagement with objects.",
              "तद्योगेन → च → इन्द्रियाणाम् → अर्थप्रवृत्तिः."),
        match(2, "Match each word of unit 60 to its meaning.",
              [["योग", "union"], ["इन्द्रिय", "sense-organ"], ["अर्थ", "object"], ["प्रवृत्ति", "engagement, activity"]],
              "By union with the mind, the sense-organs engage with objects.",
              "योग, इन्द्रिय, अर्थ, प्रवृत्ति.", role="extend",
              teaches="अर्थ here = the object of a sense; अर्थप्रवृत्ति = engagement with objects."),
        mcq("discriminate", 3, "Which split of चेंद्रियाणाम् is right?",
            ("च + इन्द्रियाणाम्", "अ + इ → ए: च + इन्द्रियाणाम् → चेन्द्रियाणाम्."),
            [("चे + इन्द्रियाणाम्", "चे is not a word; the particle is च (and)."),
             ("च + एन्द्रियाणाम्", "एन्द्रियाणाम् is not the word; it is इन्द्रियाणाम्."),
             ("चः + इन्द्रियाणाम्", "च has no visarga; it is an indeclinable.")],
            "च (and) + इन्द्रियाणाम् (of the sense-organs): अ + इ → ए.",
            "अ + इ → ए."),
        mcq("apply", 4, "Why is तत् printed तद् in तद्योगेन?",
            ("त् before the voiced य becomes द्", "A final त् becomes द् before a voiced sound."),
            [("त् before the unvoiced य stays त्", "य is voiced, and the print has द्."),
             ("त् before य becomes the nasal न्", "न् arises before a nasal; य is not a nasal."),
             ("त् before any consonant becomes द्", "Before unvoiced consonants त् stays (आमाशयात्पक्वाशय).")],
            "तत् + योगेन = तद्योगेन: त् → द् before a voiced sound.",
            "त् + voiced sound → द्."),
        fill(5, "By the rule of च + इन्द्रियाणाम् → चेन्द्रियाणाम्, join न + इति. Type it in Devanagari or in English letters "
                "(e.g. dharma): ____",
             accepts("नेति"),
             "न + इति = नेति: अ + इ → ए, as च + इन्द्रियाणाम् → चेन्द्रियाणाम्.",
             "अ followed by इ joins as ए: च + इन्द्रियाणाम् → चेन्द्रियाणाम्.",
             "अ + इ → ए.", role="transfer"),
    ],
}

# ---------------------------------------------------------------- unit 61
AUTHORED["61"] = {
    "title": "बुद्धिकर्मेन्द्रियोभयात्मकत्वाच्च",
    "question": "By unit 61, what nature does the line give to the mind of unit 59?",
    "rule": ("And because of having the nature of both (उभयात्मकत्व): of the sense-organs of cognition and of the organs "
             "of action. The ablative -त्वात् gives a reason."),
    "limits": ("Prose, one compound word. The subject (the mind, from unit 59) and the verb are carried over and not "
               "supplied: the line does not say what follows from this reason. No question on that."),
    "explain_hi": ("यह पंक्ति एक ही समास है: ‘और बुद्धि तथा कर्म, दोनों इन्द्रियों के स्वभाव वाला होने से’। "
                   "कर्ता (मन, इकाई ५९ से) और क्रिया यहाँ नहीं दिए गए; वे पिछली पंक्तियों से चले आते हैं। "
                   "‘-त्वात्’ पञ्चमी है और कारण बताता है: ‘होने से’। "
                   "इस कारण से क्या सिद्ध होता है, यह पंक्ति स्वयं नहीं कहती।"),
    "hook": "मन: ज्ञान और कर्म, दोनों इन्द्रियों के स्वभाव वाला।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 61, the mind has the nature of what?",
            ("Of both kinds of indriya", "उभयात्मकत्वात्: of the nature of both, cognition and action."),
            [("Of the organs of action only", "The line says both kinds, not action only."),
             ("Of the sense-organs only", "The line says both kinds, not cognition only."),
             ("Of neither kind of indriya", "उभय means both, not neither.")],
            "The mind has the nature of both the buddhīndriyas and the karmendriyas.",
            "बुद्धिकर्मेन्द्रियोभयात्मकत्वात्."),
        order(1, "Put the members of the compound of unit 61 in order.",
              ["बुद्धि", "कर्म", "इन्द्रिय", "उभय", "आत्मकत्वात्"],
              "Cognition, action, sense-organ, both, from having the nature.",
              "बुद्धि → कर्म → इन्द्रिय → उभय → आत्मकत्वात्."),
        match(2, "Match each member of unit 61 to its meaning.",
              [["बुद्धि", "cognition"], ["कर्म", "action"], ["उभय", "both"], ["आत्मक", "having the nature of"]],
              "Having the nature of both: cognition and action.",
              "बुद्धि, कर्म, उभय, आत्मक.", role="extend",
              teaches="उभयात्मक = having the nature of both."),
        mcq("discriminate", 3, "Which split of ...इन्द्रियोभय... is right?",
            ("इन्द्रिय + उभय", "अ + उ → ओ: इन्द्रिय + उभय → इन्द्रियोभय."),
            [("इन्द्रियः + उभय", "अः before उ drops its visarga: that would give इन्द्रिय उभय."),
             ("इन्द्रियो + भय", "भय (fear) is not the word; the word is उभय (both)."),
             ("इन्द्रिये + उभय", "ए + उ does not give ओ.")],
            "इन्द्रिय (sense-organ) + उभय (both): अ + उ → ओ.",
            "अ + उ → ओ."),
        mcq("apply", 4, "What does the ablative ending -त्वात् express in unit 61?",
            ("A reason: because of its being", "The data: abl. sg.; English 'because of having the nature'."),
            [("A place: in the state of being", "A place would need the locative (-त्वे)."),
             ("A purpose: for the sake of being", "A purpose would need the dative (-त्वाय)."),
             ("A time: at the moment of being", "Time would need the locative, not the ablative.")],
            "-त्वात् = because of being: an ablative of reason.",
            "Ablative -त्वात् → 'because of being'."),
        mcq("transfer", 5, "By the rule of आत्मकत्वात् + च → आत्मकत्वाच्च, how is तस्मात् + च (and therefore) written?",
            ("तस्माच्च", "त् before च becomes च्, as आत्मकत्वात् + च."),
            [("तस्माद्च", "द् arises before a voiced sound; च is unvoiced."),
             ("तस्माश्च", "श् comes from a visarga before च, not from त्."),
             ("तस्मा च", "The final त् is not dropped before च.")],
            "तस्मात् + च = तस्माच्च, like आत्मकत्वात् + च = आत्मकत्वाच्च.",
            "त् + च → च्च.",
            teaches="A final त् before च becomes च्: आत्मकत्वात् + च → आत्मकत्वाच्च."),
    ],
}

# ---------------------------------------------------------------- unit 62
AUTHORED["62"] = {
    "title": "क्रमादसृक्कफामपित्तपक्ववायुमूत्राधाराः",
    "question": "By unit 62, which receptacles are listed as the seats (āśaya), and in what order?",
    "rule": ("The seats (आशय), in order (क्रमात्): the receptacles (आधार) of blood (असृज्), Kapha, āma (the raw), Pitta, "
             "pakva (the digested), Vāyu and urine."),
    "limits": ("Prose. The printed समाशयाः gives no sense; 'seven' rests on a possible correction (सप्ताशयाः): no question "
               "on the number or on that word. The line names no organ for any seat."),
    "explain_hi": ("आशय (आधार) क्रम से हैं: असृक् (रक्त), कफ, आम (कच्चा), पित्त, पक्व (पका), वायु और मूत्र के आधार। "
                   "छपा ‘समाशयाः’ अर्थ नहीं देता; ‘सप्ताशयाः’ (सात आशय) एक सम्भावित सुधार है, क्योंकि सात नाम गिनाए गए हैं "
                   "और इकाई ६३ गर्भाशय को ‘आठवाँ’ कहती है। "
                   "इस पंक्ति में किसी आशय का अंग-नाम नहीं दिया गया। "
                   "संख्या और ‘समाशयाः’ पर कोई प्रश्न नहीं।"),
    "hook": "रक्त, कफ, आम, पित्त, पक्व, वायु, मूत्र: आशयों का क्रम।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 62, which receptacle comes first in the list of seats?",
            ("Of blood (असृज्)", "क्रमादसृक्...: blood comes first."),
            [("Of urine (मूत्र)", "Urine comes last in the list."),
             ("Of Kapha (कफ)", "Kapha comes second, after blood."),
             ("Of Vāyu (वायु)", "Vāyu comes sixth, before urine.")],
            "The list opens with the receptacle of blood.",
            "असृक्कफामपित्तपक्ववायुमूत्राधाराः."),
        order(1, "After असृक् (blood), put the next receptacles of unit 62 in order.",
              ["कफ", "आम", "पित्त", "पक्व", "वायु", "मूत्र"],
              "Blood, then Kapha, āma, Pitta, pakva, Vāyu, urine.",
              "कफ → आम → पित्त → पक्व → वायु → मूत्र."),
        match(2, "Match each word of unit 62 to its meaning.",
              [["असृज्", "blood"], ["आम", "raw, undigested"], ["पक्व", "digested"], ["मूत्र", "urine"],
               ["आधार", "receptacle"]],
              "Receptacles of blood, Kapha, the raw, Pitta, the digested, Vāyu and urine.",
              "असृज्, आम, पक्व, मूत्र, आधार.", role="extend",
              teaches="आधार = receptacle: each seat is named by what it holds."),
        mcq("discriminate", 3, "Which split of कफाम... in unit 62 is right?",
            ("कफ + आम", "अ + आ → आ: कफ + आम → कफाम."),
            [("कफा + अम", "कफा and अम are not the words; they are कफ and आम."),
             ("कफः + आम", "अः before आ drops its visarga: that would give कफ आम."),
             ("कफे + आम", "ए + आ would give कफ आम or कफयाम, not कफाम.")],
            "कफ (Kapha) + आम (the raw): अ + आ → आ.",
            "अ + आ → आ."),
        mcq("apply", 4, "A learner places the Pitta seat between Kapha and āma in unit 62's list. What is right?",
            ("Pitta comes between āma and pakva", "The order is ... आम, पित्त, पक्व ..."),
            [("Pitta comes between blood and Kapha", "Blood is followed directly by Kapha."),
             ("Pitta comes between Vāyu and urine", "Vāyu is followed directly by urine."),
             ("Pitta comes last, after urine", "Urine closes the list.")],
            "āma, then Pitta, then pakva.",
            "...कफामपित्तपक्व..."),
        mcq("transfer", 5, "By the rule of क्रमात् + असृक् → क्रमादसृक्, how is तत् + अपि (that too) joined?",
            ("तदपि", "त् before a vowel becomes द्, as क्रमात् + असृक्."),
            [("ततपि", "Before a vowel the final त् becomes the voiced द्."),
             ("तन्नपि", "न् arises before a nasal, not before a vowel."),
             ("तदेपि", "The अ of अपि does not change to ए.")],
            "तत् + अपि = तदपि, like क्रमात् + असृक् = क्रमादसृक्.",
            "त् + vowel → द्.",
            teaches="A final त् becomes द् before a vowel: क्रमात् + असृक् → क्रमादसृक्."),
    ],
}

# ---------------------------------------------------------------- unit 63
AUTHORED["63"] = {
    "title": "स्त्रीणां पित्तपक्वाशययोर्मध्ये गर्भाशयोऽष्टमः",
    "question": "By unit 63, what eighth seat do women have, and where is it?",
    "rule": ("In women (स्त्रीणाम्) the eighth seat is the garbhāśaya (womb, uterus: standard), in the middle (मध्ये) "
             "between the Pitta seat and the pakvāśaya."),
    "limits": ("Prose. 'Eighth' counts on from the list of unit 62. The line gives no size or other description of the "
               "womb; the copula is supplied."),
    "explain_hi": ("स्त्रियों में एक आठवाँ आशय भी है: गर्भाशय, यानी गर्भ का आशय (मानक अर्थ: गर्भाशय, uterus)। "
                   "यह पित्त के आशय और पक्वाशय के बीच में (मध्ये) है। "
                   "‘आठवाँ’ इकाई ६२ की सूची के बाद की गिनती है। "
                   "‘गर्भाशयोऽष्टमः’ = गर्भाशयः + अष्टमः; अः + अ → ओऽ।"),
    "hook": "स्त्रियों में आठवाँ: पित्त और पक्व के बीच गर्भाशय।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 63, which seat do women have in addition, as the eighth?",
            ("गर्भाशय (womb)", "गर्भाशयोऽष्टमः: the womb is the eighth."),
            [("पक्वाशय (pakva)", "The pakva seat is one of the list of unit 62."),
             ("आमाशय (āma)", "The āma seat is one of the list of unit 62."),
             ("मूत्राधार (urine)", "The urine seat closes the list of unit 62.")],
            "In women, the eighth seat is the garbhāśaya.",
            "स्त्रीणां ... गर्भाशयोऽष्टमः."),
        order(1, "Put the words of unit 63 in the line's order.",
              ["स्त्रीणाम्", "पित्तपक्वाशययोः", "मध्ये", "गर्भाशयः", "अष्टमः"],
              "Of women, of the Pitta and pakva seats, in the middle, the garbhāśaya, the eighth.",
              "स्त्रीणाम् → पित्तपक्वाशययोः → मध्ये → गर्भाशयः → अष्टमः."),
        match(2, "Match each word of unit 63 to its meaning.",
              [["स्त्रीणाम्", "of women"], ["मध्ये", "in the middle"], ["गर्भाशय", "womb"], ["अष्टम", "eighth"]],
              "Of women, in the middle (of the two seats), the womb is the eighth.",
              "स्त्रीणाम्, मध्ये, गर्भाशय, अष्टम.", role="extend",
              teaches="गर्भाशय = गर्भ + आशय: the seat of the embryo, the womb (uterus, standard)."),
        mcq("discriminate", 3, "Which split of गर्भाशयोऽष्टमः is right?",
            ("गर्भाशयः + अष्टमः", "अः + अ → ओऽ: the अ of अष्टमः is dropped (ऽ)."),
            [("गर्भाशये + अष्टमः", "ए + अ would give गर्भाशयेऽष्टमः."),
             ("गर्भाशयो + ष्टमः", "ष्टमः is not a word; the word is अष्टमः (eighth)."),
             ("गर्भाशय + अष्टमः", "अ + अ would give गर्भाशयाष्टमः.")],
            "गर्भाशयः (womb) + अष्टमः (eighth): अः + अ → ओऽ.",
            "अः + अ → ओऽ."),
        mcq("apply", 4, "By unit 63, where does the garbhāśaya lie?",
            ("Between the Pitta and pakva seats", "पित्तपक्वाशययोर्मध्ये."),
            [("Between the blood and Kapha seats", "The line names the Pitta and pakva seats."),
             ("Between the Vāyu and urine seats", "The line names the Pitta and pakva seats."),
             ("Between the āma and Pitta seats", "The line names Pitta and pakva, not āma.")],
            "The womb lies between the Pitta seat and the pakvāśaya.",
            "पित्तपक्वाशययोर्मध्ये."),
        mcq("transfer", 5, "By the rule of गर्भाशयः + अष्टमः, how is नरः + अयम् (this man) written?",
            ("नरोऽयम्", "अः + अ → ओऽ, as गर्भाशयः + अष्टमः → गर्भाशयोऽष्टमः."),
            [("नरायम्", "अ + अ → आ holds only without a visarga."),
             ("नर अयम्", "Before short अ the visarga after अ gives ओ, with ऽ."),
             ("नररयम्", "र् comes after vowels other than अ and आ.")],
            "नरः + अयम् = नरोऽयम्, like गर्भाशयः + अष्टमः = गर्भाशयोऽष्टमः.",
            "अः + अ → ओऽ.",
            teaches="अः before short अ becomes ओ and the अ is dropped (ऽ): गर्भाशयः + अष्टमः → गर्भाशयोऽष्टमः."),
    ],
}


# ===================================================================== NOTES_HI
NOTES_HI = {
    "52": ("गद्य; विश्वास मध्यम। पाठ-चिह्न (सम्भावित): छपा ‘मा’ → ‘सा’ (कला के लिए स्त्रीलिंग सर्वनाम)। "
           "‘अन्त्रामपक्वाशयाश्रिता’ को ‘अन्त्र और आम-पक्व आशयों पर टिकी’ पढ़ना पक्का नहीं; ‘कोष्ठान्तर्-उन्दुक-स्थम्’ को "
           "‘कोष्ठ के भीतर, उण्डुक में’ पढ़ना एक सम्भव पाठ है। उण्डुक = अन्धान्त्र (सम्भावित; बड़ी आँत का भाग भी पढ़ा जाता है)। "
           "इन पर कोई प्रश्न नहीं। छपाई में जुड़े: पुरीषधरानाम = पुरीषधरा नाम। सन्धि जाँची: हि + अन्त्र → ह्यन्त्र "
           "(इ + भिन्न स्वर → य्); अन्त्र + आम → अन्त्राम, पक्व + आशय → पक्वाशय (अ + आ → आ); कोष्ठ + अन्तर् → कोष्ठान्तर् "
           "(अ + अ → आ); अन्तर् + उन्दुक → अन्तरुन्दुक; ‘स्थं’, ‘मलं’: व्यंजन से पहले म् → ं।"),
    "53": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। ‘पक्वामाशय’ = पक्व(आशय) और आमाशय (डेटा की टिप्पणी, इकाई ६२ की तरह)। "
           "आमाशय = सम्भवतः जठर, पक्वाशय = सम्भवतः बड़ी आँत। छपाई: दोहरा अवग्रह (ऽऽ) छपाई की आदत है; ‘विधार्य्य’ = विधार्य; "
           "‘पक्कं’ = पक्वम्; ‘शोषयंतीपचति’ = शोषयन्ती पचति। सन्धि जाँची: हि + अन्तर् → ह्यन्तर्; अग्नि + अधिष्ठानतया → "
           "अग्न्यधिष्ठानतया (इ + भिन्न स्वर → य्); अधिष्ठानतया + आमाशयात् → अधिष्ठानतयाऽऽमाशयात् (आ + आ → आ); "
           "आमाशयात् + पक्वाशय (अघोष प से पहले त् अपरिवर्तित); पक्वाशय + उन्मुखम् → पक्वाशयोन्मुखम् (अ + उ → ओ); "
           "उन्मुखम् + अन्नम् → उन्मुखमन्नम्।"),
    "54": ("गद्य; विश्वास मध्यम। पाठ-चिह्न (सम्भावित): ‘साऽग्निनाएपस्तब्ध...’ में ‘नाए’ सन्धि नहीं है; सुझाव "
           "‘अग्निनोपस्तब्ध’ (या अग्निना उपस्तब्ध)। पहला खण्ड बिना क्रिया का है; ‘असौ’ इकाई ५३ की कला की ओर है, जिसका नाम यहाँ "
           "नहीं। ‘पुनः’ = फिर (या ‘और भी’); ‘एकयोगक्षेमा’ का बहुव्रीहि-विभाजन पक्का नहीं; ग्रहणी का आधुनिक नाम विवादित। इन पर "
           "कोई प्रश्न नहीं। छपा ‘अग्न्याभिधानम्’ में आ दीर्घ है, जबकि अग्नि + अभिधानम् से ‘अग्न्यभिधानम्’ अपेक्षित है (डेटा में "
           "चिह्नित नहीं)। सन्धि जाँची: दौर्बल्यात् + आमम् → दौर्बल्यादामम् (त् + स्वर → द्); ततः + असौ → ततोऽसौ (अः + अ → ओऽ); "
           "असौ + अन्नस्य → असावन्नस्य (औ + स्वर → आव्); पुनर् + ग्रहणी → पुनर्ग्रहणी; एव + अग्नि → एवाग्नि (अ + अ → आ); "
           "सा + अग्निना → साऽग्निना (आ + अ → आ, ऽ छपाई का चिह्न); ‘वर्त्तयति’ = वर्तयति।"),
    "55": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। ‘दो अंगुल’ किससे, यह नहीं कहा गया (डेटा की टिप्पणी)। बस्ति = मूत्राशय "
           "(सम्भावित); शुक्र = वीर्य (मानक)। सन्धि जाँची: द्वि + अङ्गुले → द्व्यङ्गुले (इ + भिन्न स्वर → य्); च + अधः → चाधः "
           "(अ + अ → आ); अधः + मूत्र → अधो मूत्र (अः + घोष व्यंजन → ओ); मूत्रमार्गम् + आश्रिता → मूत्रमार्गमाश्रिता; "
           "‘प्रवर्त्तयति’ = प्रवर्तयति।"),
    "56": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। दोष, धातु, मल शास्त्रीय शब्द रखे गए; कहाँ पहले कहे गए, यह नहीं बताया। "
           "छपाई में जुड़े: ‘धातवोमलाश्च’ = धातवो मलाश्च। सन्धि जाँची: दोषाः + धातवः → दोषा धातवः (आः + घोष → आ); "
           "धातवः + मलाः → धातवो मलाः (अः + घोष व्यंजन → ओ); मलाः + च → मलाश्च (च से पहले विसर्ग → श्); "
           "प्राक् + उदिताः → प्रागुदिताः (स्वर से पहले क् → ग्)।"),
    "57": ("गद्य; विश्वास मध्यम; दो छपी पंक्तियाँ (०२.०५.६०, ०२.०५.६१); कोई पाठ-चिह्न नहीं। ‘समभागतया’ का शब्दार्थ रखा गया; "
           "‘हर इन्द्रिय का एक विषय’ केवल सम्भावित अर्थ है। इन्द्रियों के अधिष्ठान इकाई ५८ में। सन्धि जाँची: बुद्धि + इन्द्रियाणि → "
           "बुद्धीन्द्रियाणि (इ + इ → ई); तेषाम् → तेषां (व्यंजन से पहले ं); क्रमात् + विषयाः → क्रमाद्विषयाः (त् + घोष → द्); "
           "छपा पंच = पञ्च, गंध = गन्ध।"),
    "58": ("गद्य; विश्वास उच्च; दो छपी पंक्तियाँ (०२.०५.६२, ०२.०५.६३)। पाठ-चिह्न (सम्भावित): ‘वावपायू...’ → ‘वागपायू...’ "
           "(ग के स्थान पर व की छपाई-भूल); वाक् = वाणी इसी सुधार पर टिका है, इस पर कोई प्रश्न नहीं। छपा ‘जिव्हा’ = जिह्वा "
           "(वर्तनी-भेद)। अपायु = गुदा, उपस्थ = जननेन्द्रिय (दोनों मानक)। कर्णौ, अक्षिणी, नासिके द्विवचन। सन्धि जाँची: "
           "त्वक् + अक्षिणी → त्वगक्षिणी (स्वर से पहले क् → ग्); ‘नासिकेच’ = नासिके च; कर्म + इन्द्रियाणि → कर्मेन्द्रियाणि "
           "(अ + इ → ए); अपायु + उपस्थ → अपायूपस्थ (उ + उ → ऊ)।"),
    "59": ("गद्य; विश्वास उच्च; दो छपी पंक्तियाँ (०२.०५.६४, ०२.०५.६५); कोई पाठ-चिह्न नहीं। पाँच प्रयोजन इकाई ५८ की पाँच "
           "कर्मेन्द्रियों के क्रम में हैं, पर जोड़ी पाठ में नहीं कही गई। हर्ष = आनन्द; अन्वय = सम्बन्ध, साथ चलना। सन्धि जाँची: "
           "तानि + अपि → तान्यपि (इ + भिन्न स्वर → य्); ‘तान्यपिच’ = तान्यपि च; वचन + उत्सर्ग → वचनोत्सर्ग (अ + उ → ओ); "
           "हर्ष + आदान → हर्षादान, गमन + अर्थानि → गमनार्थानि (अ + आ/अ → आ); अति + इन्द्रियम् → अतीन्द्रियम् (इ + इ → ई); "
           "सर्वार्थैः + अन्वयात् → सर्वार्थैरन्वयात् (ऐः + स्वर → ऐर्)।"),
    "60": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। ‘तत्’ = मन (इकाई ५९)। क्रिया समझी जाती है। सन्धि जाँची: तत् + योगेन → "
           "तद्योगेन (त् + घोष → द्); च + इन्द्रियाणाम् → चेन्द्रियाणाम् (अ + इ → ए); इन्द्रियाणाम् + अर्थ → इन्द्रियाणामर्थ "
           "(स्वर से पहले म्)।"),
    "61": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। अधूरी पंक्ति: कर्ता (मन, इकाई ५९ से) और क्रिया नहीं दिए गए। सन्धि जाँची: "
           "कर्म + इन्द्रिय → कर्मेन्द्रिय (अ + इ → ए); इन्द्रिय + उभय → इन्द्रियोभय (अ + उ → ओ); उभय + आत्मक → उभयात्मक "
           "(अ + आ → आ); आत्मकत्वात् + च → आत्मकत्वाच्च (त् + च → च्च)।"),
    "62": ("गद्य; विश्वास मध्यम। पाठ-चिह्न (सम्भावित): छपा ‘समाशयाः’ अर्थ नहीं देता; सुझाव ‘सप्ताशयाः’, क्योंकि सात नाम हैं और "
           "इकाई ६३ गर्भाशय को ‘अष्टमः’ कहती है। संख्या इसी सुधार पर टिकी है; इस पर कोई प्रश्न नहीं। किसी आशय का अंग-नाम यहाँ "
           "नहीं। सन्धि जाँची: क्रमात् + असृक् → क्रमादसृक् (त् + स्वर → द्); असृक् + कफ → असृक्कफ (परिवर्तन नहीं); कफ + आम → "
           "कफाम (अ + आ → आ); मूत्र + आधाराः → मूत्राधाराः।"),
    "63": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। ‘पित्तपक्वाशययोः’ को द्विवचन ‘पित्त के आशय और पक्वाशय का’ पढ़ा गया। "
           "गर्भाशय = uterus (मानक)। सन्धि जाँची: स्त्रीणाम् → स्त्रीणां (व्यंजन से पहले ं); पक्वाशययोः + मध्ये → "
           "पक्वाशययोर्मध्ये (ओः + घोष → ओर्); गर्भ + आशयः → गर्भाशयः; गर्भाशयः + अष्टमः → गर्भाशयोऽष्टमः (अः + अ → ओऽ)।"),
}


# ===================================================================== AIDS
AIDS = {
    "52": {
        "chunks": "पंचमी पुरीषधरानाम | मा | ह्यंत्रामपक्वाशयाश्रिता | कोष्ठांतरुंदुकस्थं | मलं विभजति",
        "frame": "क्रम: चौथी श्लेष्मधरा (इकाई ५१) → पाँचवीं पुरीषधरा (यह इकाई) → छठी पित्तधरा (इकाई ५३)। काम: मल को अलग करना।",
        "sandhi": "इ + भिन्न स्वर → य्: हि + अन्त्र → ह्यन्त्र · अ + अ → आ: कोष्ठ + अन्तर् → कोष्ठान्तर्।",
    },
    "53": {
        "chain": {"steps": ["आमाशय से पक्वाशय की ओर जाता अन्न", "बल से रोकती है (विधार्य)", "पित्त के तेज से सुखाती है",
                            "पकाती है (पचति)", "पके को छोड़ती है (विमुञ्चति)"]},
        "chunks": "षष्ठी पित्तधरा नाम | पक्वामाशयमध्यस्था | सा ह्यन्तरग्न्यधिष्ठानतया | ऽऽमाशयात्पक्वाशयोन्मुखमन्नं | "
                  "बलेन विधार्य्य | पित्ततेजसा शोषयंती पचति | पक्कं च विमुंचति",
        "seesaw": "आम (कच्चा) ↔ पक्व (पका): दोनों इसी पंक्ति में; पित्तधरा दोनों आशयों के बीच है और कच्चे को पका बनाकर छोड़ती है।",
        "sandhi": "अ + उ → ओ: पक्वाशय + उन्मुखम् → पक्वाशयोन्मुखम् · इ + भिन्न स्वर → य्: अग्नि + अधिष्ठानतया → अग्न्यधिष्ठानतया।",
    },
    "54": {
        "diagram": {"groups": [
            {"label": "नाम का कारण", "items": ["अन्न का ग्रहण (पकड़ना)", "इसलिए नाम: ग्रहणी"]},
            {"label": "बल", "items": ["उसका बल: पित्त ही", "पित्त का नाम: अग्नि", "अग्नि से सहारा (सम्भावित सुधार)", "शरीर को चलाती है"]}]},
        "chunks": "दोषाधिष्ठिता तु दौर्बल्यादाममेव | ततोऽसावन्नस्य ग्रहणात् | पुनर्ग्रहणीसंज्ञा | बलं च तस्याः | "
                  "पित्तमेवाग्न्याभिधानम् | अतः साऽग्निना... | शरीरं वर्त्तयति",
        "anchors": "ग्रहण → ग्रहणी: जो अन्न को ग्रहण करे, वही ग्रहणी (शब्द से नाम; मेरी याद-पद्धति)।",
        "sandhi": "अः + अ → ओऽ: ततः + असौ → ततोऽसौ · औ + स्वर → आव्: असौ + अन्नस्य → असावन्नस्य।",
    },
    "55": {
        "diagram": {"groups": [
            {"label": "स्थान", "items": ["दो अंगुल पर", "दाहिने पार्श्व में", "बस्ति-द्वार के नीचे", "मूत्रमार्ग पर टिकी"]},
            {"label": "गुण और काम", "items": ["सारे शरीर में फैली", "शुक्र को प्रवृत्त करती"]}]},
        "chunks": "सप्तमी शुक्रधरा नाम | द्व्यंगुले दक्षिणे पार्श्वे | बस्तिद्वारस्य चाधो | मूत्रमार्गमाश्रिता | "
                  "सकलशरीरव्यापिनी | शुक्रं प्रवर्त्तयति",
        "sandhi": "इ + भिन्न स्वर → य्: द्वि + अङ्गुले → द्व्यङ्गुले · अः + घोष व्यंजन → ओ: अधः + मूत्र → अधो मूत्र।",
    },
    "56": {
        "chunks": "दोषा | धातवो | मलाश्च | प्रागुदिताः",
        "sandhi": "आः + घोष → आ: दोषाः + धातवः → दोषा धातवः · अः + घोष व्यंजन → ओ: धातवः + मलाः → धातवो मलाः · "
                  "विसर्ग + च → श्च: मलाः + च → मलाश्च · स्वर से पहले क् → ग्: प्राक् + उदिताः → प्रागुदिताः।",
        "letters": "क्रम से पहले अक्षर: दो-धा-म (दोष, धातु, मल)। (मेरी याद-पद्धति)",
    },
    "57": {
        "diagram": {"groups": [
            {"label": "पाँच बुद्धीन्द्रियाँ (छपे क्रम में)", "items": ["श्रोत्र", "स्पर्शन", "दर्शन", "रसन", "घ्राण"]},
            {"label": "विषय (क्रम से)", "items": ["शब्द", "स्पर्श", "रूप", "रस", "गन्ध"]}]},
        "chunks": "पंच बुद्धींद्रियाणि | श्रोत्रं स्पर्शनं दर्शनं रसनं घ्राणं च | तेषां समभागतया | क्रमाद्विषयाः | "
                  "शब्दस्पर्शरूपरसगंधाः",
        "sandhi": "इ + इ → ई: बुद्धि + इन्द्रियाणि → बुद्धीन्द्रियाणि · त् + घोष → द्: क्रमात् + विषयाः → क्रमाद्विषयाः।",
        "letters": "इन्द्रियाँ, पहले अक्षर: श्रो-स्प-द-र-घ्रा; विषय: श-स्प-रू-र-ग। (मेरी याद-पद्धति)",
    },
    "58": {
        "diagram": {"groups": [
            {"label": "बुद्धीन्द्रियों के अधिष्ठान", "items": ["दोनों कान", "त्वचा", "दोनों आँखें", "जीभ", "दोनों नासिकाएँ"]},
            {"label": "पाँच कर्मेन्द्रियाँ", "items": ["वाक् (वाणी; सम्भावित सुधार)", "अपायु (गुदा)", "उपस्थ (जननेन्द्रिय)",
                                                  "पाणि (हाथ)", "पाद (पैर)"]}]},
        "chunks": "पंच बुद्धींद्रियाधिष्ठानानि | कर्णौ त्वगक्षिणी जिव्हा नासिके च | पंच कर्मेन्द्रियाणि | "
                  "वावपायूपस्थपाणिपादसंज्ञकानि",
        "sandhi": "स्वर से पहले क् → ग्: त्वक् + अक्षिणी → त्वगक्षिणी · उ + उ → ऊ: अपायु + उपस्थ → अपायूपस्थ।",
        "contrast": "इसी इकाई में दो सूचियाँ: ज्ञान की इन्द्रियों के अधिष्ठान (कान, त्वचा, आँख, जीभ, नाक) ↔ कर्म की इन्द्रियाँ "
                    "(वाक्, अपायु, उपस्थ, पाणि, पाद)।",
    },
    "59": {
        "chunks": "तान्यपि च | वचनोत्सर्गहर्षादानगमनार्थानि | अतींद्रियं तु मनः | सर्वार्थैरन्वयात्",
        "frame": "पहली पंक्ति: कर्मेन्द्रियों के पाँच प्रयोजन (वचन, उत्सर्ग, हर्ष, आदान, गमन) → दूसरी पंक्ति: मन इन्द्रियों से परे, "
                 "कारण: सब विषयों से अन्वय।",
        "sandhi": "इ + इ → ई: अति + इन्द्रियम् → अतीन्द्रियम् · ऐः + स्वर → ऐर्: सर्वार्थैः + अन्वयात् → सर्वार्थैरन्वयात्।",
    },
    "60": {
        "chunks": "तद्योगेन | चेंद्रियाणाम् | अर्थप्रवृत्तिः",
        "chain": {"steps": ["मन (तत्, इकाई ५९)", "उसका योग", "इन्द्रियों की विषयों में प्रवृत्ति"]},
        "sandhi": "त् + घोष → द्: तत् + योगेन → तद्योगेन · अ + इ → ए: च + इन्द्रियाणाम् → चेन्द्रियाणाम्।",
    },
    "61": {
        "chunks": "बुद्धि | कर्म | इन्द्रिय | उभय | आत्मकत्वात् | च",
        "frame": "कर्ता मन (इकाई ५९ से चला आता): ज्ञान और कर्म, दोनों इन्द्रियों के स्वभाव वाला होने से। क्रिया नहीं दी गई।",
        "sandhi": "अ + उ → ओ: इन्द्रिय + उभय → इन्द्रियोभय · त् + च → च्च: आत्मकत्वात् + च → आत्मकत्वाच्च।",
    },
    "62": {
        "diagram": {"steps": ["असृक् (रक्त)", "कफ", "आम (कच्चा)", "पित्त", "पक्व (पका)", "वायु", "मूत्र"]},
        "chunks": "समाशयाः | क्रमात् | असृक् कफ आम पित्त पक्व वायु मूत्र | आधाराः",
        "letters": "क्रम के पहले अक्षर: अ-क-आ-पि-प-वा-मू। (मेरी याद-पद्धति)",
        "sandhi": "त् + स्वर → द्: क्रमात् + असृक् → क्रमादसृक् · अ + आ → आ: कफ + आम → कफाम।",
    },
    "63": {
        "diagram": {"steps": ["पित्त का आशय", "गर्भाशय (आठवाँ, स्त्रियों में)", "पक्वाशय"]},
        "chunks": "स्त्रीणां | पित्तपक्वाशययोर्मध्ये | गर्भाशयोऽष्टमः",
        "sandhi": "अः + अ → ओऽ: गर्भाशयः + अष्टमः → गर्भाशयोऽष्टमः · ओः + घोष → ओर्: पक्वाशययोः + मध्ये → पक्वाशययोर्मध्ये।",
    },
}


# ===================================================================== IMAGE_SPECS
IMAGE_SPECS = {
    ("53", "chain"): {
        "file": "sh5-pittadhara-53.svg",
        "alt": ("Chain of unit 53, five steps of Pittadharā: the food heading from the āmāśaya to the pakvāśaya; held by "
                "force; dried by the heat of Pitta; cooked; the cooked is released."),
        "type": "chain",
        "title": "इकाई ५३: पित्तधरा अन्न के साथ",
        "steps": ["आमाशय से पक्वाशय की ओर अन्न", "बल से रोकती है", "पित्त के तेज से सुखाती है", "पकाती है",
                  "पके को छोड़ती है"],
    },
    ("54", "diagram"): {
        "file": "sh5-grahani-54.svg",
        "alt": ("Two flowcharts of unit 54. First: taking up food, hence the name grahaṇī. Second: its strength is Pitta; "
                "Pitta is named agni; supported by agni; it keeps the body going."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"अन्न का ग्रहण\"] --> B[\"इसलिए नाम: ग्रहणी\"]\n"
                 "  C[\"उसका बल: पित्त ही\"]\n"
                 "  C --> D[\"पित्त का नाम: अग्नि\"]\n"
                 "  D --> E[\"अग्नि से सहारा (सम्भावित सुधार)\"]\n"
                 "  E --> F[\"शरीर को चलाती है\"]\n"),
    },
    ("55", "diagram"): {
        "file": "sh5-shukradhara-55.svg",
        "alt": ("Table of unit 55, Śukradharā: at two aṅgulas on the right side; below the opening of the bladder (basti, "
                "probable); resting on the urinary passage; pervading the whole body; sets śukra (semen) in motion."),
        "type": "table",
        "title": "इकाई ५५: सातवीं कला शुक्रधरा",
        "heads": ["छपा अंश", "अर्थ"],
        "rows": [["द्व्यंगुले दक्षिणे पार्श्वे", "दाहिने पार्श्व में, दो अंगुल पर"],
                 ["बस्तिद्वारस्य चाधो", "बस्ति (सम्भवतः मूत्राशय) के द्वार के नीचे"],
                 ["मूत्रमार्गमाश्रिता", "मूत्रमार्ग पर टिकी"], ["सकलशरीरव्यापिनी", "सारे शरीर में फैली"],
                 ["शुक्रं प्रवर्त्तयति", "शुक्र (वीर्य) को प्रवृत्त करती है"]],
    },
    ("57", "diagram"): {
        "file": "sh5-buddhindriya-57.svg",
        "alt": ("Two columns of unit 57, each in printed order: the five buddhīndriyas (śrotra, sparśana, darśana, rasana, "
                "ghrāṇa) and their objects in order (śabda, sparśa, rūpa, rasa, gandha)."),
        "type": "split",
        "title": "इकाई ५७: पाँच बुद्धीन्द्रियाँ और विषय",
        "cols": [["इन्द्रियाँ (छपे क्रम में)", ["१ श्रोत्र", "२ स्पर्शन", "३ दर्शन", "४ रसन", "५ घ्राण"]],
                 ["विषय (क्रम से)", ["१ शब्द", "२ स्पर्श", "३ रूप", "४ रस", "५ गन्ध"]]],
    },
    ("58", "diagram"): {
        "file": "sh5-adhishthana-karmendriya-58.svg",
        "alt": ("Two columns of unit 58: the seats of the buddhīndriyas (two ears, skin, two eyes, tongue, two nostrils) and "
                "the five karmendriyas (speech, on a possible correction; anus; genital organ; hand; foot)."),
        "type": "split",
        "title": "इकाई ५८: अधिष्ठान और कर्मेन्द्रियाँ",
        "cols": [["बुद्धीन्द्रियों के अधिष्ठान", ["दोनों कान", "त्वचा", "दोनों आँखें", "जीभ", "दोनों नासिकाएँ"]],
                 ["पाँच कर्मेन्द्रियाँ", ["वाक् (सम्भावित सुधार)", "अपायु (गुदा)", "उपस्थ (जननेन्द्रिय)", "पाणि (हाथ)",
                                        "पाद (पैर)"]]],
    },
    ("62", "diagram"): {
        "file": "sh5-ashaya-62.svg",
        "alt": ("Numbered table of unit 62, the seats in printed order: 1 blood (asṛj), 2 Kapha, 3 āma (the raw), 4 Pitta, "
                "5 pakva (the digested), 6 Vāyu, 7 urine."),
        "type": "table",
        "title": "इकाई ६२: आशयों का क्रम",
        "heads": ["क्रम", "किसका आधार"],
        "rows": [["१", "असृक् (रक्त)"], ["२", "कफ"], ["३", "आम (कच्चा)"], ["४", "पित्त"], ["५", "पक्व (पका)"],
                 ["६", "वायु"], ["७", "मूत्र"]],
    },
    ("63", "diagram"): {
        "file": "sh5-garbhashaya-63.svg",
        "alt": ("Flowchart of unit 63: in women, the garbhāśaya (womb), the eighth seat, lies between the Pitta seat and "
                "the pakvāśaya."),
        "type": "mermaid",
        "code": ("flowchart LR\n"
                 "  subgraph S[\"स्त्रियों में\"]\n"
                 "    A[\"पित्त का आशय\"] --- B[\"मध्य में: गर्भाशय, आठवाँ\"]\n"
                 "    B --- C[\"पक्वाशय\"]\n"
                 "  end\n"),
    },
}
