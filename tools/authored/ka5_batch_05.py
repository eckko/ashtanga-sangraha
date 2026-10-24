from helpers import mcq, match, order, fill, multi, accepts

# Kalpasthana chapter 5 (Siddhabastikalpa), units 62-73 (lines 05.05.122-141).
# 62-65: Agnivesha asks which fruit is best in basti; Punarvasu names fruits for diseases
#   and ranks madana foremost in asthapana (05.05.124-129).
# 66-73: the disciples ask how a basti clears the doshas of the whole body (05.05.130-133);
#   the teacher answers that wind is the one cause, so basti is half, or even the whole, of treatment.

AUTHORED = {}

# ---------------------------------------------------------------- unit 62
AUTHORED["62"] = {
    "title": "पृच्छतिस्म मुनिमित्यथ धीमान्",
    "question": "What does Agniveśa ask the sage in verse 62, and who answers?",
    "rule": ("The wise Agniveśa asked the sage: of the fruits, which may be always beneficial "
             "in basti-action (enema procedure)? Punarvasu instructed him. The answer begins "
             "in the next verse (05.05.124)."),
    "limits": ("The verse only frames the question: it names no fruit. पृच्छति स्म is a present "
               "with स्म, giving a past sense. The question runs across both lines and ends at स्यात्. "
               "The sage asked (मुनिम्) is named Punarvasu in line 2."),
    "explain_hi": ("यह श्लोक फलों के प्रकरण का आरम्भ है और एक संवाद के रूप में है। "
                   "बुद्धिमान् अग्निवेश मुनि से पूछते हैं: फलों में से कौन-सा बस्तिकर्म में सदा हितकर होगा? "
                   "‘पृच्छति स्म’ वर्तमान काल का रूप है, पर ‘स्म’ के साथ इसका अर्थ भूतकाल का हो जाता है: ‘पूछा’। "
                   "दूसरी पंक्ति के अन्त में बताया गया है कि पुनर्वसु ने उसे (‘तम्’, यानी अग्निवेश को) उपदेश दिया। "
                   "उत्तर अगले श्लोक से शुरू होता है; इस श्लोक में किसी फल का नाम नहीं है।"),
    "hook": "अग्निवेश का प्रश्न: बस्ति में सदा हितकर फल कौन? उत्तर देंगे पुनर्वसु।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "What does Agniveśa ask the sage about in verse 62?",
            ("Which fruit is always good in basti",
             "किं तु फलानां बस्तिकर्मणि हितं सततं स्यात्: which of the fruits may be always beneficial in basti-action."),
            [("Which oil suits a Kapha anuvāsana",
              "Oils for anuvāsana came earlier; verse 62 asks about fruits."),
             ("How much decoction a nirūha needs",
              "No measure is asked about in verse 62."),
             ("When a basti must never be given",
              "The question is about what is beneficial, not about forbidden times.")],
            "The question is about fruits (फलानाम्) that are beneficial (हितम्) in basti-action (बस्तिकर्मणि).",
            "Verse 62: Agniveśa asks which fruit is always beneficial in basti; Punarvasu answers."),
        match(1, "Match each word of verse 62 to its meaning.",
              [["धीमान्", "wise"], ["हितम्", "beneficial"], ["सततम्", "always"],
               ["प्रशशास", "instructed"]],
              "These words describe the asker, the question and the answer.",
              "धीमान् = wise; हितम् = beneficial; सततम् = always; प्रशशास = instructed."),
        order(2, "Put these phrases of verse 62 in the order of the verse.",
              ["पृच्छतिस्म मुनिम्", "धीमान् अग्निवेशः", "किं तु फलानाम्", "बस्तिकर्मणि हितम्",
               "पुनर्वसुः प्रशशास"],
              "First the asking, then the asker, then the question about fruits in basti, then Punarvasu's instruction.",
              "पृच्छतिस्म मुनिम् · धीमान् अग्निवेशः · किं तु फलानाम् · बस्तिकर्मणि हितम् · पुनर्वसुः प्रशशास.",
              role="extend",
              teaches="Verse 62 runs: he asked the sage; the wise Agniveśa; which of the fruits; beneficial in basti; Punarvasu instructed."),
        mcq("discriminate", 3, "Which is the right split of मुनिमित्यथ?",
            ("मुनिम् + इति + अथ",
             "म् joins the next vowel (मुनिमि-), and इ before a different vowel becomes य्: इति + अथ = इत्यथ."),
            [("मुनिमि + त्यथ", "Neither piece is a word."),
             ("मुनिः + इति + अथ", "A visarga after इ before a vowel becomes र्: that would give मुनिरित्यथ."),
             ("मुनिम् + इत + अथ", "इत + अथ would give इताथ (अ + अ = आ), not इत्यथ.")],
            "मुनिम् (the sage, accusative) + इति (thus) + अथ (then).",
            "इ + different vowel → य् + vowel: इति + अथ = इत्यथ."),
        mcq("apply", 4, "In verse 62, whom does तम् (him) refer to, the one Punarvasu instructed?",
            ("Agniveśa, the one who asked",
             "The card: तम् = him, Agniveśa, who asked the question."),
            [("The sage who was asked",
              "The sage asked is Punarvasu himself, the one who instructs."),
             ("The fruit asked about",
              "तम् is masculine and is the person instructed; फल is neuter."),
             ("The other disciples together",
              "Other disciples appear only in 05.05.131, and तम् is singular.")],
            "Agniveśa asks, Punarvasu (the sage) instructs him (तम्).",
            "पुनर्वसुः (subject) प्रशशास तम् (Agniveśa)."),
        mcq("transfer", 5,
            "Like पृच्छति स्म (asked), what does the invented वदति स्म mean?",
            ("he spoke",
             "A present form with स्म takes a past sense: वदति स्म = he spoke."),
            [("he will speak", "स्म does not make a future."),
             ("he should speak", "That would be the optative वदेत्."),
             ("he is not speaking", "स्म is not a negative; न would be.")],
            "पृच्छति स्म = asked; in the same way वदति स्म = spoke.",
            "Present tense + स्म = past sense.",
            teaches="A present-tense verb followed by स्म has a past sense (पृच्छति स्म = asked; वदति स्म = spoke)."),
    ],
}

# ---------------------------------------------------------------- unit 63
AUTHORED["63"] = {
    "title": "इह कुष्ठहिता गैरागिरी",
    "question": "Which fruits does verse 63 name, and for which diseases?",
    "rule": ("Punarvasu's answer begins with fruits for diseases: gairāgirī (unclear word) in kuṣṭha; "
             "the ikṣvāku fruit for those with prameha; the kuṭaja fruit foremost in heart ailment; "
             "the kauṭa-fruit in pāṇḍu."),
    "limits": ("Low confidence. गैरागिरी is not a known name: kept as printed, unidentified; no question "
               "uses it. कौटफल is unidentified. ikṣvāku = probably bitter bottle gourd (Lagenaria siceraria, "
               "probable); kuṭaja = kurchi (Holarrhena antidysenterica, standard). The Hindi wording of "
               "the disease names is an open owner point (05.05.124)."),
    "explain_hi": ("यहाँ पुनर्वसु का उत्तर शुरू होता है: अलग-अलग रोगों में कौन-सा फल हितकर है। "
                   "पहला नाम ‘गैरागिरी’ अस्पष्ट है; अनुमानित पाठ के अनुसार वह कुष्ठ (त्वचा के रोगों का समूह) में हितकर कहा गया है। "
                   "प्रमेह वालों के लिए इक्ष्वाकु का फल यानी सम्भवतः कड़वी लौकी हितकर है। "
                   "कुटज यानी कुड़ा का फल हृदय के रोग में श्रेष्ठ है, और कौट फल (पहचान अज्ञात) पाण्डु यानी रक्ताल्पता में। "
                   "‘प्रवरम्’ (श्रेष्ठ) दूसरी पंक्ति के उत्तरार्ध पर भी लागू माना गया है।"),
    "hook": "कुष्ठ, प्रमेह, हृदय, पाण्डु: चार रोग, हर एक का अपना फल।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Which fruit does verse 63 call foremost (प्रवरम्) in heart ailment?",
            ("The fruit of kuṭaja",
             "कुटजस्य फलं हृदामये प्रवरम्: the kuṭaja fruit is foremost in heart ailment."),
            [("The fruit of ikṣvāku", "The ikṣvāku fruit is for those with prameha."),
             ("The kauṭa-fruit", "The kauṭa-fruit is named for pāṇḍu."),
             ("The fruit of madana", "Madana comes in the next verse, not for heart ailment here.")],
            "हृदामये = in heart ailment; the fruit named for it is kuṭaja's.",
            "कुटज फल → हृदामय (heart ailment)."),
        match(1, "Match each word of verse 63 to its meaning.",
              [["इह", "here"], ["हितम्", "beneficial"], ["हृदामये", "in heart ailment"],
               ["प्रवरम्", "foremost"]],
              "These words carry the framing and the praise of the fruits.",
              "इह = here; हितम् = beneficial; हृदामये = in heart ailment; प्रवरम् = foremost."),
        order(2, "Put the diseases of verse 63 in the order the verse names them.",
              ["कुष्ठ", "प्रमेह", "हृदामय", "पाण्डु"],
              "The verse runs: kuṣṭha, prameha, heart ailment, pāṇḍu.",
              "कुष्ठहिता · प्रमेहिणाम् · हृदामये · पाण्डुषु.",
              role="extend",
              teaches="Verse 63 names four diseases in this order: kuṣṭha, prameha, heart ailment (hṛdāmaya), pāṇḍu."),
        mcq("discriminate", 3, "Which is the right split of हितमिक्ष्वाकुफलं?",
            ("हितम् + इक्ष्वाकुफलम्",
             "Final म् simply joins a following vowel: हितम् + इ- = हितमि-."),
            [("हित + मिक्ष्वाकुफलम्", "मिक्ष्वाकु is not a word."),
             ("हितम + इक्ष्वाकुफलम्", "अ + इ would give ए: हितमेक्ष्वाकु-."),
             ("हिते + इक्ष्वाकुफलम्", "ए before इ becomes अय् or अ, not -मि-.")],
            "हितम् (beneficial) + इक्ष्वाकु-फलम् (the ikṣvāku fruit).",
            "म् + vowel: the म् joins the vowel (हितम् + इ = हितमि)."),
        match(4, "Match each fruit of verse 63 to the disease it is named for.",
              [["इक्ष्वाकुफल", "prameha"], ["कुटज-फल", "heart ailment"], ["कौटफल", "pāṇḍu"]],
              "Each clear fruit is tied to one disease in the verse.",
              "इक्ष्वाकु → प्रमेह; कुटज → हृदामय; कौट → पाण्डु.",
              role="apply"),
        mcq("transfer", 5,
            "प्रमेहिणाम् is the genitive plural of प्रमेहिन्. Which form means 'of the strong (बलिन्)'?",
            ("बलिनाम्",
             "An -इन् stem makes its genitive plural in -इनाम् (प्रमेहिणाम् has ण only because of the र before it)."),
            [("बलीनाम्", "The vowel stays short in -इनाम्."),
             ("बलिनः", "This is the nominative plural or the genitive singular."),
             ("बलिना", "This is the instrumental singular, 'by the strong one'.")],
            "प्रमेहिन् → प्रमेहिणाम्; बलिन् → बलिनाम्.",
            "-इन् stem: genitive plural -इनाम्.",
            teaches="Nouns in -इन् (प्रमेहिन्, बलिन्) form the genitive plural in -इनाम् (ण after र: प्रमेहिणाम्)."),
    ],
}

# ---------------------------------------------------------------- unit 64
AUTHORED["64"] = {
    "title": "मदनं सर्वगदाविरोधि तु",
    "question": "What does verse 64 say of kṛtavedhana and of madana's tastes?",
    "rule": ("Kṛtavedhana (probably ridge gourd) is beneficial in udara; madana (emetic nut) is not "
             "opposed to any disease. It is sweet, with astringent and bitter; it is not dry; on a "
             "conjectural reading, with pungent, hot and slimy."),
    "limits": ("Low confidence. Whether उदरे is the belly or the disease udara is an open point (05.05.126): "
               "no question on it. The last compound (सकटृष्णपिच्छिलं) rests on a suggested reading: no question. "
               "सर्वगदाविरोधि could also be split -गदा-विरोधि; only the data's reading is given, without a question."),
    "explain_hi": ("पहली पंक्ति दो फल बताती है: कृतवेधन यानी सम्भवतः तोरई उदर में हितकर है, और मदन यानी मैनफल किसी रोग का विरोधी नहीं है। "
                   "फिर मदन के गुण आते हैं: वह मधुर है, कसैले और कड़वे के साथ। "
                   "‘तत् अरूक्षम्’: वह रूखा नहीं है; यहाँ ‘अ-’ निषेध का अर्थ देता है। "
                   "अन्तिम समास की छपाई बिगड़ी है; अनुमानित पाठ के अनुसार उसमें तीखा, उष्ण और चिपचिपा गुण हैं। "
                   "मदन का वर्णन अगले श्लोक में पूरा होता है।"),
    "hook": "मैनफल: मीठा, साथ में कसैला-कड़वा, पर रूखा नहीं।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Which taste does verse 64 name first for madana?",
            ("Sweet (मधुर)", "मधुरम् opens line 2: madana is sweet."),
            [("Sour (अम्ल)", "Sour is not named in verse 64."),
             ("Salty (लवण)", "Salty is not named in verse 64."),
             ("Bitter alone", "Bitter is named, but only with sweet and astringent.")],
            "मधुरं सकषायतिक्तकम्: sweet, with astringent and bitter.",
            "Madana: मधुर, with कषाय and तिक्त."),
        match(1, "Match each word of verse 64 to its meaning.",
              [["मधुरम्", "sweet"], ["कषाय", "astringent"], ["तिक्तक", "bitter"],
               ["अरूक्षम्", "not dry"]],
              "These words give madana's qualities on the clear part of line 2.",
              "मधुरम् = sweet; कषाय = astringent (taste); तिक्तक = bitter; अरूक्षम् = not dry."),
        order(2, "Put these words of verse 64 in the order of the verse.",
              ["कृतवेधनम्", "हितम्", "मदनम्", "मधुरम्", "अरूक्षम्"],
              "Line 1 names kṛtavedhana, beneficial, then madana; line 2 gives madana's qualities: sweet, then not dry.",
              "कृतवेधनं · हितं · मदनं · मधुरं · अरूक्षं.",
              role="extend",
              teaches="Verse 64 first names kṛtavedhana as beneficial, then madana, then madana's qualities: sweet ... not dry."),
        mcq("discriminate", 3, "Which is the right split of तदरूक्षं?",
            ("तत् + अरूक्षम्",
             "त् becomes द् before a vowel: तत् + अ- = तद-; अरूक्षम् = not dry."),
            [("तत् + रूक्षम्", "त् before र becomes द्: that would print तद्रूक्षम्, and mean the opposite."),
             ("तदा + रूक्षम्", "That would print तदारूक्षम्, with a long आ."),
             ("तद + अरूक्षम्", "अ + अ would merge into आ: तदारूक्षम्.")],
            "तत् (that) + अरूक्षम् (not dry): madana is not dry.",
            "त् → द् before a vowel; the vowel stays separate: तदरूक्षम्."),
        mcq("apply", 4, "In सकषायतिक्तकम् of verse 64, what does the first part स- add?",
            ("with (astringent and bitter)",
             "स- = with: madana is sweet with astringent and bitter."),
            [("without (astringent and bitter)", "Without would be निर्- or अ-, not स-."),
             ("very (astringent and bitter)", "Very would be अति-, as in अतिगहन."),
             ("equal to (astringent and bitter)", "Equal would be सम, not the prefix स-.")],
            "The card glosses स- as 'with': sweet, with astringent and bitter.",
            "स- at the head of a compound = 'with, accompanied by'."),
        mcq("transfer", 5,
            "Like अरूक्षम् (not dry) from रूक्षम्, which form means 'not sour' from अम्लम्?",
            ("अनम्लम्",
             "The negative अ- becomes अन्- before a vowel: अन् + अम्लम् = अनम्लम्."),
            [("अअम्लम्", "Before a vowel the negative takes the form अन्-."),
             ("साम्लम्", "स- + अम्ल means 'with sour', not 'not sour'."),
             ("अम्लतमम्", "-तम means 'most': 'most sour'.")],
            "अ- before a consonant (अरूक्ष), अन्- before a vowel (अनम्ल).",
            "Negative prefix: अ- before consonants, अन्- before vowels.",
            teaches="The negative prefix is अ- before a consonant (अरूक्ष, not dry) and अन्- before a vowel (अनम्ल, not sour)."),
    ],
}

# ---------------------------------------------------------------- unit 65
AUTHORED["65"] = {
    "title": "कफपित्तहृदाशुकारि",
    "question": "Why is madana held foremost in āsthāpana, according to verse 65?",
    "rule": ("Madana removes Kapha and Pitta, acts quickly, is harmless and makes the wind move in its "
             "natural direction; therefore it is held foremost among fruit and the rest in applications "
             "of āsthāpana (decoction enema)."),
    "limits": ("Madana is the subject carried over from 05.05.126-127; it is not named again here. "
               "The verse gives no dose and no method. हृत् is read as 'removing'; the reading 'heart' "
               "is not supported by the sentence (data note)."),
    "explain_hi": ("यह श्लोक मदन यानी मैनफल का वर्णन पूरा करता है और पुनर्वसु का उत्तर यहीं समाप्त होता है। "
                   "मदन कफ और पित्त को हरता है, शीघ्र काम करता है, हानिरहित है और वायु का अनुलोमन करता है, यानी उसे स्वाभाविक दिशा में चलाता है। "
                   "‘अतः’ (इसलिए) इन्हीं गुणों की ओर संकेत करता है। "
                   "इसी कारण फल आदि में मदन को आस्थापन यानी क्वाथ-बस्ति के प्रयोगों में श्रेष्ठ माना गया है। "
                   "अग्निवेश के प्रश्न (श्लोक ६२) का यही सीधा उत्तर है।"),
    "hook": "कफ-पित्त हरे, जल्दी करे, हानि न करे, वायु सीधी करे: इसलिए आस्थापन में मैनफल सबसे आगे।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "In which use does verse 65 hold madana foremost?",
            ("In āsthāpana (decoction enema) uses",
             "आस्थापनयोजनासु: in the applications of āsthāpana."),
            [("In anuvāsana (oil enema) uses", "The verse names āsthāpana, not anuvāsana."),
             ("In nasal medicine (nasya) uses", "Nasal medicine is not mentioned."),
             ("In ointments for the skin", "No ointment is mentioned.")],
            "प्रवरं ... आस्थापनयोजनासु: foremost in applications of āsthāpana.",
            "Madana = प्रवर in आस्थापन."),
        match(1, "Match each quality of madana in verse 65 to its meaning.",
              [["कफपित्तहृत्", "removing Kapha and Pitta"], ["आशुकारि", "acting quickly"],
               ["निरपायम्", "harmless"], ["पवनानुलोमि", "moving the wind in its natural direction"]],
              "The four qualities that make madana foremost.",
              "हृत् = removing; आशु = quick; निरपाय = without harm; अनुलोमि = moving in the natural direction."),
        order(2, "Put madana's qualities in the order verse 65 gives them.",
              ["कफपित्तहृत्", "आशुकारि", "निरपायम्", "पवनानुलोमि"],
              "Removing Kapha and Pitta, quick-acting, harmless, moving the wind rightly.",
              "कफपित्तहृत् · आशुकारि · निरपायं · पवनानुलोमि.",
              role="extend",
              teaches="Verse 65 lists madana's qualities: removes Kapha-Pitta, acts quickly, is harmless, moves the wind in its natural direction."),
        mcq("discriminate", 3, "Which is the right split of कफपित्तहृदाशुकारि?",
            ("कफपित्तहृत् + आशुकारि",
             "त् becomes द् before a vowel: हृत् + आशु- = हृदाशु-."),
            [("कफपित्तहृत + आशुकारि", "अ + आ would give आ with त kept: हृताशु-."),
             ("कफपित्तहृद् + अशुकारि", "द् + अ would print हृदशु-, with a short अ."),
             ("कफपित्तहृदा + शुकारि", "शुकारि is not a word.")],
            "हृत् (removing) + आशुकारि (acting quickly).",
            "त् → द् before a vowel: हृत् + आ = हृदा."),
        mcq("apply", 4, "In verse 65, what does अतः (therefore) point back to?",
            ("The qualities listed in line 1",
             "Because madana removes Kapha-Pitta, acts fast, is harmless and moves the wind rightly, it is foremost."),
            [("Agniveśa's wisdom in verse 62", "His wisdom is not the reason given."),
             ("The kuṭaja fruit of verse 63", "Kuṭaja is foremost in heart ailment, not the reason here."),
             ("A dose stated in line 2", "No dose is stated in verse 65.")],
            "अतः links the qualities (line 1) to the ranking (line 2).",
            "Qualities (line 1) → अतः → प्रवर (line 2)."),
        mcq("transfer", 5,
            "By the rule of हृत् + आशु = हृदाशु, how do जगत् + ईशः join?",
            ("जगदीशः", "त् becomes द् before a vowel, and the vowel stays: जगदीशः."),
            [("जगतीशः", "Before a vowel the त् turns voiced, द्."),
             ("जगन्नीशः", "त् becomes न् only before a nasal, and ई is not a nasal."),
             ("जगदेशः", "The vowel ई would not change to ए.")],
            "हृत् + आशु = हृदाशु; जगत् + ईशः = जगदीशः.",
            "Final त् → द् before a vowel.",
            teaches="A final त् becomes द् before a vowel (हृत् + आशुकारि = हृदाशुकारि; जगत् + ईशः = जगदीशः)."),
    ],
}

# ---------------------------------------------------------------- unit 66
AUTHORED["66"] = {
    "title": "अथ मुनिवृषभे निगद्य वाक्यम्",
    "question": "What happens after the sage finishes speaking, in unit 66?",
    "rule": ("Then, when the bull among sages (muni-vṛṣabha) had spoken his words and stopped, "
             "(the disciple) again made a request."),
    "limits": ("The one who makes the request is not named here; 05.05.131 says he bowed with the other "
               "disciples (Agniveśa by context, not stated). मुनिवृषभ is an epithet, here for Punarvasu by context. "
               "The request itself comes in 05.05.131-133."),
    "explain_hi": ("फलों वाला उत्तर समाप्त होने के बाद संवाद आगे बढ़ता है। "
                   "‘मुनिवृषभ’ का अर्थ है मुनियों में बैल जैसा, यानी मुनियों में श्रेष्ठ; प्रसंग से यह पुनर्वसु हैं। "
                   "‘मुनिवृषभे … स्थितवति’ सप्तमी में है: जब वे वचन कहकर रुक गए, तब। "
                   "तभी शिष्य ने फिर (‘भूयः’) निवेदन किया; ‘विज्ञापयाम् बभूव’ परोक्ष भूतकाल का बना हुआ (आम्-वाला) रूप है। "
                   "निवेदन करने वाले का नाम इस इकाई में नहीं है।"),
    "hook": "गुरु रुके, शिष्य ने फिर विनती की।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "What happens in unit 66?",
            ("After the sage stops, a request is made again",
             "मुनिवृषभे ... स्थितवति विज्ञापयांबभूव भूयः: when the sage had stopped, he again made a request."),
            [("The sage names a new fruit for basti use",
              "No fruit is named in unit 66."),
             ("The disciples leave the sage in silence",
              "Nobody leaves; a request is made."),
             ("The sage puts a question to the disciples",
              "The request comes from the disciple side, not from the sage.")],
            "The unit is a bridge: the sage stops, the disciple asks again.",
            "Unit 66: the sage stops speaking; a new request follows."),
        match(1, "Match each word of unit 66 to its meaning.",
              [["निगद्य", "having spoken"], ["वाक्यम्", "words"], ["स्थितवति", "when he had stopped"],
               ["भूयः", "again"]],
              "These words tell what the sage did and what followed.",
              "निगद्य = having spoken; वाक्यम् = words; स्थितवति = when he had stopped; भूयः = again."),
        order(2, "Put these words of unit 66 in the order of the text.",
              ["मुनिवृषभे", "निगद्य", "वाक्यम्", "स्थितवति", "विज्ञापयांबभूव"],
              "The sage, having spoken his words, stopped; then (he) made a request.",
              "मुनिवृषभे · निगद्य · वाक्यं · स्थितवति · विज्ञापयांबभूव.",
              role="extend",
              teaches="Unit 66: the sage (मुनिवृषभे), having spoken (निगद्य) his words (वाक्यम्), stopped (स्थितवति); a request was made (विज्ञापयांबभूव)."),
        mcq("discriminate", 3, "What does वृषभ (bull) mean inside मुनिवृषभ in unit 66?",
            ("The best, the chief among sages",
             "The card: 'bull among sages', an epithet for the chief sage."),
            [("A bull that belongs to a sage", "The card reads it as an epithet, not an animal."),
             ("A sage who rides on a bull", "Riding is not in the word."),
             ("The youngest sage of a group", "वृषभ in an epithet means the foremost, not the youngest.")],
            "X-वृषभ = the bull among X, the foremost of X.",
            "मुनिवृषभ = मुनियों में श्रेष्ठ."),
        mcq("apply", 4, "In मुनिवृषभे ... स्थितवति, what do the two locatives express?",
            ("When the sage had stopped",
             "A noun and participle in the locative give the time of the main action: 'when the sage had stopped'."),
            [("Where the request was made", "No place is named; the locatives give the time."),
             ("To whom the request was made", "A person addressed is not put in this pair of locatives."),
             ("Why the sage had stopped", "No reason for stopping is given.")],
            "Locative absolute: मुनिवृषभे स्थितवति = when the sage had stopped.",
            "Noun + participle in the locative = 'when ...'."),
        mcq("transfer", 5,
            "विज्ञापयांबभूव is a perfect built with -आम् + बभूव. Which invented form is built the same way?",
            ("कारयांबभूव", "-आम् + बभूव after a causative stem, like विज्ञापयांबभूव."),
            [("कारयति", "This is the present, 'causes to do'."),
             ("कारयित्वा", "This is the absolutive, 'having caused to do'."),
             ("कारितवान्", "This is the -वत् past active participle.")],
            "Causative stems take the perfect with -आम् and an auxiliary (बभूव, चकार, आस).",
            "Periphrastic perfect = stem + -आम् + बभूव / चकार / आस.",
            teaches="Causative stems form the perfect with -आम् plus an auxiliary: विज्ञापयाम् बभूव, कारयाम् बभूव."),
    ],
}

# ---------------------------------------------------------------- unit 67
AUTHORED["67"] = {
    "title": "इदमतिगहनं सहान्यशिष्यैः",
    "question": "How does the disciple approach the sage with his new question in unit 67?",
    "rule": ("This very profound (matter): bowed down to the ground together with the other disciples, "
             "having placed the joined hands (añjali) in front. The sentence runs on into 05.05.132-133."),
    "limits": ("No verb here; the question itself is in 05.05.132-133. The print has 'jalim': añjali "
               "rests on a suggested reading (text_flags), so no question uses it. इदम् is read as the "
               "object of the question that follows."),
    "explain_hi": ("यह इकाई प्रश्न से पहले की विनय-भरी मुद्रा बताती है। "
                   "‘इदम् अतिगहनम्’: यह अत्यन्त गहन विषय, जिसके बारे में आगे प्रश्न होगा। "
                   "पूछने वाला अन्य शिष्यों के साथ भूमि पर झुका हुआ है (‘अवनिगतः’), और आगे हाथ जोड़कर, यानी अञ्जलि रखकर। "
                   "छपाई में ‘जलिम्’ है; ‘अञ्जलिम्’ सुझाया गया पाठ है। "
                   "वाक्य की क्रिया इस इकाई में नहीं है; प्रश्न अगली पंक्तियों में आता है।"),
    "hook": "गहन प्रश्न से पहले: सब शिष्य भूमि पर झुके, हाथ जुड़े।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "How does unit 67 describe the matter about to be asked (इदम्)?",
            ("Very profound", "अतिगहनम् = very deep, profound."),
            [("Very simple", "The word is अतिगहन, very deep, the opposite of simple."),
             ("Already settled", "Nothing says it was settled; it is about to be asked."),
             ("Secret, not to be told", "Secrecy is not mentioned.")],
            "इदम् अतिगहनम् = this very profound (matter).",
            "अति (very) + गहन (deep) = अतिगहन."),
        match(1, "Match each word of unit 67 to its meaning.",
              [["अतिगहनम्", "very profound"], ["अन्यशिष्यैः", "with the other disciples"],
               ["अवनिगतः", "bowed down to the ground"], ["अग्रतः", "in front"], ["निधाय", "having placed"]],
              "These words describe the matter and the posture of the disciple.",
              "अतिगहनम् = very profound; अन्यशिष्यैः = other disciples; अवनिगतः = bowed to the ground; अग्रतः = in front; निधाय = having placed."),
        order(2, "Put these words of unit 67 in the order of the text.",
              ["इदम्", "अतिगहनम्", "सह", "अन्यशिष्यैः", "अवनिगतः"],
              "First the matter (this, very profound), then the company (with the other disciples), then the posture (bowed).",
              "इदम् · अतिगहनं · सह · अन्यशिष्यैः · अवनिगतः.",
              role="extend",
              teaches="Unit 67 names the matter first (इदम् अतिगहनम्), then the company (सह अन्यशिष्यैः) and the bow (अवनिगतः)."),
        mcq("discriminate", 3, "Which is the right split of सहान्यशिष्यैः?",
            ("सह + अन्यशिष्यैः", "अ + अ merge into आ: सह + अन्य- = सहान्य-."),
            [("सहा + न्यशिष्यैः", "Neither सहा nor न्यशिष्य is a word."),
             ("सहः + अन्यशिष्यैः", "अः before अ becomes ओ with avagraha: सहोऽन्य-."),
             ("सह + न्यशिष्यैः", "Without a vowel to merge there would be no आ: सहन्य-.")],
            "सह (together with) + अन्य-शिष्यैः (other disciples).",
            "अ + अ → आ."),
        mcq("apply", 4, "Which case does सह (together with) take in unit 67?",
            ("The instrumental (अन्यशिष्यैः)",
             "अन्यशिष्यैः is instrumental plural, the case सह takes."),
            [("The accusative (इदम्)", "इदम् is the object of the question, not the word with सह."),
             ("The nominative (अवनिगतः)", "अवनिगतः describes the speaker himself."),
             ("The locative (मुनिवृषभे)", "That locative is in unit 66 and gives the time.")],
            "सह + instrumental: सह अन्यशिष्यैः = together with the other disciples.",
            "सह takes the instrumental."),
        mcq("transfer", 5,
            "Using the rule of सह अन्यशिष्यैः, which invented phrase means 'together with the teacher'?",
            ("गुरुणा सह", "गुरुणा is the instrumental of गुरु, the case सह takes."),
            [("गुरुं सह", "गुरुम् is accusative; सह takes the instrumental."),
             ("गुरोः सह", "गुरोः is genitive or ablative."),
             ("गुरौ सह", "गुरौ is locative.")],
            "सह + instrumental, whatever the noun: अन्यशिष्यैः सह, गुरुणा सह.",
            "सह takes the instrumental.",
            teaches="सह ('together with') takes the instrumental: सह अन्यशिष्यैः, गुरुणा सह."),
    ],
}

# ---------------------------------------------------------------- unit 68
AUTHORED["68"] = {
    "title": "चित्रकर्मगुणकृद्गुरुणोक्तः",
    "question": "What question about the basti do the disciples put in verse 68?",
    "rule": ("The basti, said by the teacher to produce varied actions and benefits ... quickly arrives ... "
             "from the body on all sides: how does it drive away the doṣas?"),
    "limits": ("Low confidence. The phrase ऊर्ध्वम् ... न नाभेः is disputed: the data has 'goes upward, not from "
               "the navel', a reviewer proposes 'does not go above the navel' (open, 05.05.132); no question on it. "
               "चानुस is unclear. Questions use only the clear words."),
    "explain_hi": ("यह शिष्यों का प्रश्न है, जो 05.05.131 से चल रहा है। "
                   "वे कहते हैं: गुरु ने बस्ति को विचित्र कर्म और गुण करने वाला कहा है। "
                   "पहली पंक्ति का ‘ऊर्ध्वम् … न नाभेः’ वाला अंश विवादित है: डेटा में ‘ऊपर जाता है, नाभि से नहीं’, और समीक्षक का सुझाव ‘नाभि से ऊपर नहीं जाता’। "
                   "दूसरी पंक्ति में ‘चानुस’ अस्पष्ट है। "
                   "स्पष्ट बात अन्तिम प्रश्न है: वह शीघ्र, देह से सब ओर से, दोषों को कैसे हटाता है? उत्तर अगली इकाई में गुरु देते हैं।"),
    "hook": "प्रश्न: एक बस्ति पूरे शरीर के दोष कैसे हटाए?",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "What do the disciples ask at the end of verse 68?",
            ("How the basti drives away the doṣas",
             "कथम् अपोहति दोषान्: how does it drive away the doṣas?"),
            [("Which fruit is best for the basti",
              "That was Agniveśa's earlier question (verse 62)."),
             ("How long a basti must be held in",
              "No time of holding is asked."),
             ("Who first taught the basti to men",
              "No first teacher is asked about.")],
            "The question ends with कथम् अपोहति दोषान्.",
            "Verse 68 asks: how does the basti remove the doṣas?"),
        match(1, "Match each word of verse 68 to its meaning.",
              [["गुरुणा", "by the teacher"], ["उक्तः", "said"], ["शीघ्रम्", "quickly"],
               ["कथम्", "how"], ["अपोहति", "drives away"]],
              "These are the clear words of the question.",
              "गुरुणा = by the teacher; उक्तः = said; शीघ्रम् = quickly; कथम् = how; अपोहति = drives away."),
        order(2, "Put these clear words of line 2 of verse 68 in the order of the verse.",
              ["शीघ्रम्", "आपतति", "देहात्", "कथम्", "दोषान्"],
              "Line 2 runs: quickly arrives ... from the body ... how ... the doṣas.",
              "शीघ्रम् · आपतति · देहात् · कथम् · दोषान्.",
              role="extend",
              teaches="Line 2 of verse 68 ends the question: quickly (शीघ्रम्) ... from the body (देहात्) ... how (कथम्) does it drive away the doṣas (दोषान्)?"),
        mcq("discriminate", 3, "Which is the right split of गुरुणोक्तः?",
            ("गुरुणा + उक्तः", "आ + उ merge into ओ: गुरुणा + उक्तः = गुरुणोक्तः."),
            [("गुरुणो + क्तः", "क्तः is not a word."),
             ("गुरुणः + उक्तः", "अः before उ loses its visarga and stays apart: गुरुण उक्तः."),
             ("गुरुणे + उक्तः", "ए before उ becomes अय् or अ, not ओ.")],
            "गुरुणा (by the teacher) + उक्तः (said).",
            "आ + उ → ओ."),
        mcq("apply", 4, "In गुरुणा उक्तः, what does the instrumental गुरुणा show?",
            ("Who did the saying: said by the teacher",
             "With a past passive participle (उक्तः) the instrumental names the agent."),
            [("To whom it was said: said to the teacher", "The one addressed would be dative or accusative."),
             ("From whom it came: taken from the teacher", "Source would be ablative (गुरोः)."),
             ("About whom it was said: said of the teacher", "The basti, not the teacher, is the subject spoken of.")],
            "Past passive participle + instrumental agent: गुरुणा उक्तः = said by the teacher.",
            "-त participle + instrumental = 'X-ed by'."),
        mcq("transfer", 5,
            "On the model of गुरुणा उक्तः, which invented phrase means 'said by the sage (मुनि)'?",
            ("मुनिना उक्तः", "मुनिना is the instrumental of मुनि, the agent with उक्तः."),
            [("मुनिम् उक्तः", "मुनिम् is accusative."),
             ("मुनेः उक्तः", "मुनेः is genitive or ablative."),
             ("मुनये उक्तः", "मुनये is dative, 'to the sage'.")],
            "Agent in the instrumental with a passive participle: गुरुणा उक्तः, मुनिना उक्तः.",
            "Instrumental agent + -त participle.",
            teaches="With a past passive participle the doer stands in the instrumental: गुरुणा उक्तः, मुनिना उक्तः."),
    ],
}

# ---------------------------------------------------------------- unit 69
AUTHORED["69"] = {
    "title": "ऊचे गुरुः",
    "question": "What does the teacher say everything in the body is subject to, in unit 69?",
    "rule": ("The teacher said: this of the body, whatever is resting outside or within, is subject to "
             "the wind (māruta) that is stimita (still, stagnant)."),
    "limits": ("Low confidence; a literal reading. स्तिमित may mean 'still, stagnant' or 'wet, steady': no "
               "question on its sense. How यत् and एतत् relate is not fully resolved. The teacher is not "
               "named here (Punarvasu by context)."),
    "explain_hi": ("अब गुरु उत्तर देना आरम्भ करते हैं: ‘ऊचे गुरुः’, गुरु ने कहा। "
                   "उनके अनुसार शरीर का यह सब, जो बाहर या भीतर आश्रित है, स्तिमित वायु के वश में है। "
                   "‘स्तिमित’ का अर्थ यहाँ ‘रुका हुआ, ठहरा’ लिया गया है, पर ‘गीला, स्थिर’ भी हो सकता है। "
                   "स्पष्ट बात इतनी है: शरीर में जो कुछ है, वह वायु के वश में है; यही उत्तर आगे की इकाइयों का आधार है। "
                   "पंक्ति कठिन है, इसलिए अनुवाद शब्दशः है।"),
    "hook": "गुरु बोले: देह के भीतर-बाहर सब वायु के वश में।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Who speaks in unit 69?",
            ("The teacher (गुरुः)", "ऊचे गुरुः = the teacher said."),
            [("The questioning disciple", "The disciple asked in the units before; here the teacher answers."),
             ("The other disciples together", "ऊचे is singular, and its subject is गुरुः."),
             ("A patient given the basti", "No patient speaks.")],
            "ऊचे (said) + गुरुः (the teacher).",
            "Unit 69 opens the teacher's answer: ऊचे गुरुः."),
        match(1, "Match each word of unit 69 to its meaning.",
              [["ऊचे", "said"], ["देहस्य", "of the body"], ["बहिः", "outside"], ["अन्तरे", "within"]],
              "The speaking verb and the places named.",
              "ऊचे = said; देहस्य = of the body; बहिः = outside; अन्तरे = within."),
        mcq("extend", 2, "According to unit 69, to what is this (of the body) subject (वश्य)?",
            ("To the wind (māruta)", "मारुत-वश्यम्: subject to the wind."),
            [("To Pitta", "Pitta is not named in unit 69."),
             ("To Kapha", "Kapha is not named in unit 69."),
             ("To the basti", "The basti is not named in unit 69.")],
            "स्तिमित-मारुत-वश्यम्: subject to the (stimita) wind.",
            "Unit 69: what is in the body is subject to the wind.",
            teaches="The teacher's answer starts from the wind: what rests outside or within the body is subject to the wind (मारुत)."),
        mcq("discriminate", 3, "Which pair of places does unit 69 name for what is in the body?",
            ("Outside or within", "बहिः ... अन्तरे वा: outside or within."),
            [("In the branches or the storehouse", "Those (शाखा, कोष्ठ) come in verse 71."),
             ("In the head or in the feet", "Head and feet are not named here."),
             ("In the belly or the heart", "Neither is named in unit 69.")],
            "यत् बहिः अपाश्रितम् अन्तरे वा = whatever rests outside or within.",
            "बहिः = outside; अन्तरे = within."),
        order(4, "Put these words of unit 69 in the order of the text.",
              ["ऊचे", "गुरुः", "मारुतवश्यम्", "देहस्य", "बहिः"],
              "The teacher said; subject to the wind; of the body; outside ...",
              "ऊचे · गुरुः · (स्तिमित)मारुतवश्यम् · देहस्य · बहिः.",
              role="apply"),
        mcq("transfer", 5,
            "Like देहस्य (of the body), which invented form means 'of the wind' from मारुत?",
            ("मारुतस्य", "An -अ noun makes its genitive singular in -अस्य, like देहस्य."),
            [("मारुतम्", "This is the accusative."),
             ("मारुतेन", "This is the instrumental, 'by the wind'."),
             ("मारुते", "This is the locative, 'in the wind'.")],
            "देह → देहस्य; मारुत → मारुतस्य.",
            "-अ stem: genitive singular -अस्य.",
            teaches="Masculine -अ nouns form the genitive singular in -अस्य: देहस्य (of the body), मारुतस्य (of the wind)."),
    ],
}

# ---------------------------------------------------------------- unit 70
AUTHORED["70"] = {
    "title": "दुष्टस्य तस्य जनयन्ननुलोमताम्",
    "question": "What does the basti do to the spoiled wind, in unit 70?",
    "rule": ("Producing the natural direction (anulomatā) in that spoiled (wind), the basti destroys "
             "... groups of diseases (the first part of the last word is damaged)."),
    "limits": ("Low confidence. विषमान्तिरोगपूगान् is kept unsplit: its first part is damaged; no question on "
               "it. The noun of दुष्टस्य तस्य is not stated; it is read as the wind of 05.05.134."),
    "explain_hi": ("गुरु का उत्तर आगे बढ़ता है। "
                   "वह दूषित (वायु), जिसकी बात पिछली पंक्ति में थी, उसमें बस्ति अनुलोमता उत्पन्न करती है, यानी उसे स्वाभाविक दिशा में चलाती है। "
                   "ऐसा करते हुए बस्ति रोगों के समूहों को नष्ट करती है। "
                   "अन्तिम शब्द का पहला भाग (‘विषमान्ति-’) छपाई में बिगड़ा है; केवल अन्त ‘रोग-पूग’ (रोगों के समूह) स्पष्ट है। "
                   "‘दुष्टस्य तस्य’ की संज्ञा नहीं कही गई; इसे वायु पढ़ा गया है।"),
    "hook": "बस्ति बिगड़ी वायु को सीधा चलाए, और रोग-समूह मिटें।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "What does the basti produce in the spoiled one, in unit 70?",
            ("Movement in the natural direction",
             "जनयन् अनुलोमताम्: producing the natural direction (anulomatā)."),
            [("Heat in the region of the belly", "Heat is not mentioned."),
             ("Dryness throughout the whole body", "Dryness is not mentioned."),
             ("Stillness, stopping all movement", "Anulomatā is movement in the natural direction, not stopping.")],
            "अनुलोमता = the natural direction; the basti produces it in the spoiled (wind).",
            "बस्ति → अनुलोमता."),
        match(1, "Match each word of unit 70 to its meaning.",
              [["दुष्टस्य", "of the spoiled one"], ["जनयन्", "producing"],
               ["अनुलोमताम्", "natural direction"], ["हिनस्ति", "destroys"]],
              "These words carry the action of the basti.",
              "दुष्टस्य = of the spoiled; जनयन् = producing; अनुलोमताम् = natural direction; हिनस्ति = destroys."),
        order(2, "Put these words of unit 70 in the order of the text.",
              ["दुष्टस्य", "तस्य", "जनयन्", "अनुलोमताम्", "बस्तिः", "हिनस्ति"],
              "Of that spoiled one, producing the natural direction, the basti destroys ...",
              "दुष्टस्य · तस्य · जनयन् · अनुलोमतां · बस्तिः · हिनस्ति.",
              role="extend",
              teaches="Unit 70: of that spoiled (wind), producing the natural direction, the basti destroys (groups of diseases)."),
        mcq("discriminate", 3, "Which is the right split of बस्तिर्हिनस्ति?",
            ("बस्तिः + हिनस्ति", "इः before a voiced sound (ह) becomes इर्: बस्तिर्हिनस्ति."),
            [("बस्तिम् + हिनस्ति", "म् before ह would become an anusvara: बस्तिं हिनस्ति."),
             ("बस्ति + र्हिनस्ति", "र्हिनस्ति is not a word."),
             ("बस्तेः + हिनस्ति", "That would print बस्तेर्हिनस्ति, with ए.")],
            "बस्तिः (the basti, subject) + हिनस्ति (destroys).",
            "Visarga after इ/उ before a voiced sound → र्."),
        mcq("apply", 4, "In unit 70, who is doing the producing (जनयन्)?",
            ("The basti (बस्तिः)", "जनयन् is nominative masculine and goes with बस्तिः, the subject of हिनस्ति."),
            [("The spoiled wind", "The wind is in the genitive (दुष्टस्य तस्य); it is what is acted on."),
             ("The teacher who speaks", "The teacher is the speaker, not the subject of this sentence."),
             ("The groups of diseases", "They are the object of हिनस्ति, in the accusative.")],
            "जनयन् (nom.) agrees with बस्तिः: the basti, producing the natural direction, destroys ...",
            "A present participle agrees with its subject."),
        mcq("transfer", 5,
            "Like जनयन् (producing) beside जनयति, which form means 'going' beside गच्छति?",
            ("गच्छन्", "The present participle masculine nominative singular ends in -अन्: जनयन्, गच्छन्."),
            [("गत्वा", "This is the absolutive, 'having gone'."),
             ("गन्तुम्", "This is the infinitive, 'to go'."),
             ("गतः", "This is the past participle, 'gone'.")],
            "जनयति → जनयन्; गच्छति → गच्छन्.",
            "Present participle (m. nom. sg.) = present stem + -न्.",
            teaches="The present participle 'X-ing' (m. nom. sg.) is the present stem + न्: जनयन् (producing), गच्छन् (going)."),
    ],
}

# ---------------------------------------------------------------- unit 71
AUTHORED["71"] = {
    "title": "शाखागताः कोष्ठगताश्च रोगाः",
    "question": "What does verse 71 name as the cause of diseases wherever they arise?",
    "rule": ("Diseases gone to the branches (śākhā) or the storehouse (koṣṭha), and those born in the vital "
             "spots, the upper parts and all the parts and limbs: in their origin there is no other cause "
             "beyond wind (vāyu)."),
    "limits": ("śākhā and koṣṭha are rendered literally ('branch', 'storehouse'). The long compound of line 1 "
               "is read as a list of places of origin. The verse names no single disease."),
    "explain_hi": ("यह गुरु के उत्तर का मुख्य सिद्धान्त है। "
                   "रोग चाहे शाखा में गए हों या कोष्ठ में, चाहे मर्मों में, ऊर्ध्व भाग में या सब अवयवों और अंगों में उत्पन्न हुए हों, "
                   "उन सबके जन्म में वायु से परे कोई और हेतु नहीं है। "
                   "‘वायोः परम्’ में वायु पञ्चमी में है: ‘वायु के सिवा, वायु से परे’। "
                   "यही कारण है कि वायु को जीतने वाली बस्ति इतनी बड़ी चिकित्सा मानी जाती है (अगले श्लोक)।"),
    "hook": "शाखा, कोष्ठ, मर्म, ऊपर, हर अंग: रोग कहीं भी हो, जन्म का हेतु वायु ही।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "According to verse 71, what is the cause in the origin of these diseases?",
            ("Wind (vāyu), and no other",
             "न तु कश्चिद् अन्यो वायोः परं ... हेतुः: no other cause beyond wind."),
            [("Pitta, and no other", "Pitta is not named in verse 71."),
             ("Kapha joined with Pitta", "Neither is named as the cause here."),
             ("All three doṣas equally", "The verse names one cause only: wind.")],
            "वायोः परम् न कश्चिद् अन्यः हेतुः: there is no cause other than wind.",
            "Verse 71: of diseases everywhere, the cause is wind."),
        match(1, "Match each word of verse 71 to its meaning.",
              [["शाखा", "branch"], ["कोष्ठ", "storehouse"], ["मर्म", "vital spot"],
               ["हेतुः", "cause"], ["जन्मनि", "in origin"]],
              "The places of disease and the words of the conclusion.",
              "शाखा = branch; कोष्ठ = storehouse; मर्म = vital spot; हेतुः = cause; जन्मनि = in origin."),
        order(2, "Put the places of diseases in the order verse 71 names them.",
              ["शाखा", "कोष्ठ", "मर्म", "ऊर्ध्व", "सर्व अवयव-अङ्ग"],
              "Branches, storehouse, then vital spots, the upper (parts), all parts and limbs.",
              "शाखागताः · कोष्ठगताः · मर्म-ऊर्ध्व-सर्वावयवाङ्गजाः.",
              role="extend",
              teaches="Verse 71 lists the places of disease: śākhā, koṣṭha, marma, the upper parts, all parts and limbs."),
        mcq("discriminate", 3, "Which is the right split of कोष्ठगताश्च?",
            ("कोष्ठगताः + च", "आः before च becomes आश्: कोष्ठगताश्च."),
            [("कोष्ठगतान् + च", "न् before च would give an anusvara with श्: कोष्ठगतांश्च."),
             ("कोष्ठगतम् + च", "म् before च would become an anusvara: कोष्ठगतं च."),
             ("कोष्ठगता + अश्च", "अश्च is not a word.")],
            "कोष्ठगताः (gone to the storehouse, nom. pl., with रोगाः) + च (and).",
            "Visarga before च/छ → श्."),
        multi("apply", 4, "Which of these does verse 71 name as places of diseases?",
              [("the branches (शाखा)", "Named first."),
               ("the storehouse (कोष्ठ)", "Named second."),
               ("the vital spots (मर्म)", "Named at the head of the long compound."),
               ("the navel (नाभि)", "The navel is named in verse 68, not here."),
               ("the eyes alone", "No such place is named.")],
              [0, 1, 2],
              "Verse 71: śākhā, koṣṭha, marma, the upper parts, all parts and limbs.",
              "Places named: शाखा, कोष्ठ, मर्म, ऊर्ध्व, सर्व अवयव-अङ्ग."),
        mcq("transfer", 5,
            "वायोः परम् puts वायु in the ablative ('beyond wind'). Which invented phrase means 'other than honey'?",
            ("मधुनः अन्यत्", "मधुनः is the ablative of मधु; अन्य and पर take the ablative."),
            [("मधु अन्यत्", "मधु is nominative or accusative."),
             ("मधुना अन्यत्", "मधुना is instrumental."),
             ("मधुनि अन्यत्", "मधुनि is locative.")],
            "'Other than / beyond X' takes X in the ablative: वायोः परम्, मधुनः अन्यत्.",
            "अन्य / पर + ablative.",
            teaches="Words meaning 'other than, beyond' (अन्य, पर) take the ablative: वायोः परम्, मधुनः अन्यत्."),
    ],
}

# ---------------------------------------------------------------- unit 72
AUTHORED["72"] = {
    "title": "विक्षेपसंहारकरो हि वायुः",
    "question": "What does wind do to the wastes, and why is basti the remedy, in verse 72?",
    "rule": ("Wind is the doer of the scattering and gathering of the accumulations of wastes (faeces, Pitta "
             "and so on); for pacifying that greatly increased (wind) there is no other remedy equal to basti, "
             "because ... (continues in 05.05.140)."),
    "limits": ("शोष in the list of wastes is odd and may be corrupt (open, 05.05.138): no question on it. "
               "शमायं has a stray anusvara (text_flags): no question on it. The 'because' clause ends in the next verse."),
    "explain_hi": ("पहली पंक्ति वायु का काम बताती है: मल-संचयों का, यानी विट् (मल), शोष, पित्त आदि के संचयों का, बिखेरना और समेटना वही करता है। "
                   "‘शोष’ यहाँ अटपटा है और छपाई की भूल हो सकती है। "
                   "दूसरी पंक्ति कहती है: उस अत्यन्त बढ़े हुए वायु के शमन के लिए बस्ति के समान दूसरी कोई औषध नहीं है। "
                   "‘यस्मात्’ (क्योंकि) से कारण शुरू होता है, जो अगले श्लोक में पूरा होता है। "
                   "छपा ‘वस्तेः’ = बस्तेः (व/ब का अदल-बदल)।"),
    "hook": "मल बिखेरे-समेटे वायु; बढ़ी वायु के लिए बस्ति जैसी दवा नहीं।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "What does verse 72 say wind does to the accumulations of wastes?",
            ("It scatters and gathers them", "विक्षेप-संहार-करः: the doer of scattering and gathering."),
            [("It burns and digests them", "Burning and digesting are not named."),
             ("It cools and hardens them", "Cooling and hardening are not named."),
             ("It hides and stores them", "Hiding and storing are not named.")],
            "विक्षेप = scattering; संहार = gathering; कर = doer.",
            "Wind = विक्षेप-संहार-कर of the wastes."),
        match(1, "Match each word of verse 72 to its meaning.",
              [["विक्षेप", "scattering"], ["संहार", "gathering"], ["अतिवृद्धस्य", "of the greatly increased"],
               ["भेषजम्", "remedy"], ["समम्", "equal"]],
              "These words carry what wind does and the claim about basti.",
              "विक्षेप = scattering; संहार = gathering; अतिवृद्धस्य = of the greatly increased; भेषजम् = remedy; समम् = equal."),
        mcq("extend", 2, "Which remedy does verse 72 say has no equal for the greatly increased wind?",
            ("Basti", "नान्यद् बस्तेः समं भेषजम्: no other remedy equal to basti."),
            [("Madana fruit", "Madana is praised in verse 65, for āsthāpana; it is not named here."),
             ("Kuṭaja fruit", "Kuṭaja is for heart ailment (verse 63), not named here."),
             ("Nasal medicine", "Nasal medicine is not mentioned.")],
            "बस्तेः (than basti) समम् (equal) न अन्यत् भेषजम्.",
            "Verse 72: for increased wind no remedy equals basti.",
            teaches="Verse 72 says that for pacifying greatly increased wind there is no remedy equal to basti."),
        mcq("discriminate", 3, "Which is the right split of विक्षेपसंहारकरो हि?",
            ("विक्षेपसंहारकरः + हि", "अः before a voiced sound (ह) becomes ओ: करो हि."),
            [("विक्षेपसंहारकरम् + हि", "म् before ह would become an anusvara: करं हि."),
             ("विक्षेपसंहारकरे + हि", "ए stays ए before ह: करे हि."),
             ("विक्षेपसंहारकराः + हि", "आः before a voiced sound drops the visarga: करा हि.")],
            "विक्षेपसंहारकरः (doer of scattering and gathering) + हि (for).",
            "अः + voiced consonant → ओ."),
        order(4, "Put these words of line 2 of verse 72 in the order of the verse.",
              ["तस्य", "अतिवृद्धस्य", "अन्यत्", "बस्तेः", "भेषजम्", "यस्मात्"],
              "Of that greatly increased (wind) ... no other ... than basti ... remedy ... because.",
              "तस्य · अतिवृद्धस्य · (न) अन्यत् · बस्तेः · (समं) भेषजम् · (अस्ति) यस्मात्.",
              role="apply"),
        mcq("transfer", 5,
            "नान्यद् is न + अन्यत्. By the same rule, how do न + अस्ति join?",
            ("नास्ति", "अ + अ merge into आ: न + अस्ति = नास्ति."),
            [("नोस्ति", "ओ is not made from अ + अ."),
             ("नस्ति", "The two vowels merge into a long आ, not a short अ."),
             ("नेस्ति", "ए comes from अ + इ, not अ + अ.")],
            "न + अन्यत् = नान्यत्; न + अस्ति = नास्ति.",
            "अ + अ → आ.",
            teaches="Two short अ vowels merge into आ: न + अन्यत् = नान्यत्, न + अस्ति = नास्ति."),
    ],
}

# ---------------------------------------------------------------- unit 73
AUTHORED["73"] = {
    "title": "चिकित्सार्धमिति ब्रुवन्ति",
    "question": "Why is basti called half, or even the whole, of treatment in verse 73?",
    "rule": ("When the wind is conquered with effort, Pitta, Kapha and the rest, stirred by it, are pacified "
             "too. Therefore they call (basti) half of treatment; some call basti even the whole of treatment."),
    "limits": ("The verse completes the 'because' (यस्मात्) of 05.05.139. In the first claim the object "
               "(basti) is not named; it is understood from context. The verse names no one who says it."),
    "explain_hi": ("यह श्लोक पिछले ‘क्योंकि’ को पूरा करता है। "
                   "जब वायु (अनिल) यत्न से जीत लिया जाता है, तो उसी से प्रेरित पित्त, कफ आदि भी शान्त हो जाते हैं। "
                   "‘जिते अनिले’ सप्तमी में है: ‘वायु के जीते जाने पर’। "
                   "इसलिए विद्वान बस्ति को ‘चिकित्सा का आधा’ कहते हैं, और कुछ लोग तो बस्ति को सम्पूर्ण चिकित्सा ही कहते हैं। "
                   "यहीं से बस्ति के प्रधान कर्म होने की बात निकलती है।"),
    "hook": "वायु जीती तो पित्त-कफ भी शान्त: इसलिए बस्ति आधी चिकित्सा, कुछ के मत में पूरी।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "What do some (एके) call basti, according to verse 73?",
            ("Even the whole of treatment", "सर्वां चिकित्साम् अपि बस्तिम् एके: some (call) basti even the whole treatment."),
            [("Only a small aid to treatment", "The verse ranks it far higher."),
             ("A quarter of all treatment", "A quarter is not mentioned."),
             ("A treatment for Kapha alone", "Kapha is pacified with the wind; the verse does not limit basti to it.")],
            "They say 'half of treatment'; some say even 'the whole treatment'.",
            "Basti = चिकित्सार्ध; for some, सर्वा चिकित्सा."),
        match(1, "Match each word of verse 73 to its meaning.",
              [["शाम्यन्ति", "are pacified"], ["यत्नेन", "with effort"], ["जिते", "when conquered"],
               ["ईरिताः", "stirred"], ["अर्धम्", "half"]],
              "These words carry the reasoning and the claim.",
              "शाम्यन्ति = are pacified; यत्नेन = with effort; जिते = when conquered; ईरिताः = stirred; अर्धम् = half."),
        order(2, "Put the steps of verse 73's reasoning in order.",
              ["वायु यत्न से जीता गया", "उससे प्रेरित पित्त-कफ आदि भी शान्त",
               "इसलिए: चिकित्सा का आधा", "कुछ के मत में: सम्पूर्ण चिकित्सा"],
              "Wind conquered → Pitta, Kapha stirred by it also pacified → therefore half of treatment → for some, the whole.",
              "जिते अनिले · शाम्यन्ति पित्तकफादयः · तस्मात् चिकित्सार्धम् · सर्वां चिकित्साम् एके.",
              role="extend",
              teaches="Verse 73 argues: conquer the wind and what it stirs is pacified too; so basti is half of treatment, for some the whole."),
        mcq("discriminate", 3, "Which is the right split of पित्तकफादयोऽपि?",
            ("पित्तकफादयः + अपि", "अः before अ becomes ओ and the अ is marked by avagraha: -यो ऽपि."),
            [("पित्तकफादय + अपि", "अ + अ would merge into आ: -यापि."),
             ("पित्तकफादयम् + अपि", "म् would join the vowel: -यमपि."),
             ("पित्तकफादयः + पि", "पि is not a word.")],
            "पित्तकफादयः (Pitta, Kapha and the rest) + अपि (also).",
            "अः + अ → ओऽ."),
        mcq("apply", 4, "Why are Pitta and Kapha pacified when the wind is conquered, per verse 73?",
            ("They are stirred by the wind", "तदीरिताः: stirred by it (the wind); with it conquered, they settle."),
            [("Basti removes them from the head", "No head is named in verse 73."),
             ("They were never increased at all", "The verse says they are pacified, so they were stirred."),
             ("Madana dries them out at once", "Madana is not named in verse 73.")],
            "तत्-ईरिताः = stirred by it: they follow the wind.",
            "Wind conquered → what it stirred is pacified."),
        mcq("transfer", 5,
            "जिते अनिले means 'when the wind is conquered'. Which invented phrase means 'when the sun has risen'?",
            ("उदिते सूर्ये", "Participle and noun both in the locative: the time of the main action."),
            [("उदितः सूर्यः", "This is a plain statement: 'the sun (has) risen'."),
             ("उदितेन सूर्येण", "This is instrumental: 'by the risen sun'."),
             ("उदितं सूर्यम्", "This is accusative: 'the risen sun' as an object.")],
            "Locative absolute: जिते अनिले, उदिते सूर्ये.",
            "Noun + participle in the locative = 'when ...'.",
            teaches="A noun with a participle, both in the locative, means 'when ...': जिते अनिले (when wind is conquered), उदिते सूर्ये (when the sun has risen)."),
    ],
}


NOTES_HI = {
    "62": ("विश्वास: उच्च। संधि जाँची: मुनिमित्यथ = मुनिम् + इति + अथ; धीमानग्निवेश = धीमान् + अग्निवेशः (इह से पहले विसर्ग लुप्त); "
           "स्यात्तं = स्यात् + तम्; पुनर्वसुरिति = पुनर्वसुः + इति। ‘पृच्छति स्म’ = वर्तमान + स्म, भूतकाल का अर्थ। "
           "प्रश्न 05.05.122 से 05.05.123 तक चलता है; पहला ‘इति’ प्रश्न का आरम्भ, दूसरा ‘प्रशशास’ के साथ। "
           "डेटा का हिन्दी अनुवाद ‘क्या’ दो बार दोहराता है; अंग्रेज़ी में भी उद्धरण-चिह्न टूटे हैं (रिपोर्ट किया)।"),
    "63": ("विश्वास: निम्न। ‘गैरागिरी’ ज्ञात नाम नहीं; छपा रूप रखा गया, पहचान अज्ञात, ‘हिता’ से स्त्रीलिंग। "
           "इक्ष्वाकु = सम्भवतः कड़वी लौकी (Lagenaria siceraria, सम्भावित); कुटज = कुड़ा (Holarrhena antidysenterica, मानक); कौटफल अज्ञात। "
           "कुष्ठ यहाँ रोग-समूह, कूठ द्रव्य नहीं। ‘प्रवरम्’ दूसरे अर्धांश पर भी। "
           "खुला अवलोकन (05.05.124): हिन्दी में कुष्ठ और प्रमेह के आधुनिक नाम का शब्दांकन मालिक के निर्णय पर; इस पर प्रश्न नहीं। "
           "संधि: हितमिक्ष्वाकुफलं = हितम् + इक्ष्वाकुफलम्; पांडुषु = पाण्डुषु (अनुस्वार-वर्तनी)।"),
    "64": ("विश्वास: निम्न। खुला अवलोकन (05.05.126): ‘उदरे’ पेट या उदर-रोग, मालिक का निर्णय बाकी; इस पर प्रश्न नहीं। "
           "कृतवेधन = सम्भवतः तोरई (Luffa acutangula, सम्भावित); मदन = मैनफल (Randia dumetorum, मानक)। "
           "text_flags: छपा ‘सकटृष्णपिच्छिलं’ में ‘टृष्ण’; सुझाया पाठ सकटूष्णपिच्छिल (कटु-उष्ण-पिच्छिल); इस समास पर प्रश्न नहीं। "
           "‘सर्वगदाविरोधि’ डेटा में सर्व-गद-अविरोधि; छपे रूप से -गदा-विरोधि भी बन सकता है, इसलिए इस पर प्रश्न नहीं। "
           "संधि जाँची: तदरूक्षं = तत् + अरूक्षम्। कषाय यहाँ रस (कसैला)।"),
    "65": ("विश्वास: मध्यम। संधि: कफपित्तहृदाशुकारि = -हृत् + आशुकारि (त् → द्); यन्निरपायं = यत् + निरपायम्; "
           "तदतः = तत् + अतः; स्मृतमास्थापनयोजनाष्विति = स्मृतम् + आस्थापनयोजनासु + इति (छपा ‘-ष्विति’ में ष, शुद्ध रूप -स्विति)। "
           "‘हृद्’ = हृदय वाला पाठ वाक्य से समर्थित नहीं (डेटा)। कर्ता मदन 05.05.126-127 से। अन्तिम ‘इति’ अनुवाद से बाहर।"),
    "66": ("विश्वास: मध्यम। ‘विज्ञापयांबभूव’ = विज्ञापयाम् बभूव (आम्-वाला परोक्ष भूत, णिजन्त)। "
           "‘स्थितवति’ = क्तवतु-प्रत्ययान्त, सप्तमी; ‘मुनिवृषभे स्थितवति’ सति-सप्तमी। "
           "निवेदक का नाम नहीं; 05.05.131 से प्रसंगवश अग्निवेश। ‘मुनिवृषभ’ प्रसंग से पुनर्वसु। "
           "पंक्ति छन्दोबद्ध दिखती है, पर डेटा में गद्य-इकाई।"),
    "67": ("विश्वास: मध्यम। text_flags: छपा ‘-ऽजलिम्’; सुझाया पाठ ‘-ऽञ्जलिम्’ (ञ छूटा)। केवल यही सदस्य प्रश्नों से बाहर; "
           "सह, अन्यशिष्यैः, अवनिगतः, अग्रतः स्पष्ट हैं। संधि: सहान्यशिष्यैः = सह + अन्यशिष्यैः; अवनिगतोऽञ्जलिम् = अवनिगतः + अञ्जलिम्। "
           "वाक्य अधूरा, 05.05.132-133 में आगे; ‘इदम्’ आगे के प्रश्न का कर्म माना गया।"),
    "68": ("विश्वास: निम्न। खुला अवलोकन (05.05.132, गम्भीर): ‘ऊर्ध्वम् … न नाभेः’ का अर्थ: डेटा ‘ऊपर जाता है, नाभि से नहीं’; "
           "समीक्षक: ऊर्ध्वम् + पञ्चमी = ‘नाभि से ऊपर नहीं जाता’। निर्णय बाकी; इस पर प्रश्न नहीं। "
           "खुला अवलोकन (05.05.133): ‘चानुस’ अपुनर्स्थापनीय, ‘अनुस’ अस्पष्ट (तीन अक्षर का शब्द अपेक्षित); इस पर प्रश्न नहीं। "
           "संधि जाँची: गुरुणोक्तः = गुरुणा + उक्तः; चैति = च + एति; कथमपोहति = कथम् + अपोहति।"),
    "69": ("विश्वास: निम्न, शब्दशः पाठ। ‘स्तिमित’ = रुका, ठहरा; ‘गीला, स्थिर’ भी सम्भव। यत् और एतत् का सम्बन्ध पूरी तरह स्पष्ट नहीं। "
           "छपा ‘यद्वहि:’ = यत् + बहिः (व/ब का अदल-बदल); ‘मंतरे’ = अन्तरे (अनुस्वार-वर्तनी)। ‘ऊचे’ = √वच् परोक्ष भूत, आत्मनेपद।"),
    "70": ("विश्वास: निम्न। ‘विषमान्तिरोगपूगान्’ बिना विभाजन रखा गया: पहला भाग बिगड़ा (शायद विषम-आन्तर-रोग-पूग, पक्का नहीं); "
           "केवल ‘रोग-पूग’ (रोगों के समूह) स्पष्ट। ‘दुष्टस्य तस्य’ की संज्ञा अनुक्त, 05.05.134 का वायु माना गया। "
           "संधि: जनयन्ननुलोमताम् = जनयन् + अनुलोमताम् (ह्रस्व स्वर के बाद न् द्वित्व); बस्तिर्हिनस्ति = बस्तिः + हिनस्ति।"),
    "71": ("विश्वास: मध्यम। संधि जाँची: कोष्ठगताश्च = कोष्ठगताः + च; रोगा मर्म- = रोगाः + मर्म- (आः के बाद सघोष से पहले विसर्ग लोप); "
           "मर्मोर्ध्व = मर्म + ऊर्ध्व; कश्चिदन्यो = कश्चित् + अन्यः; हेतुरस्ति = हेतुः + अस्ति। "
           "लम्बा समास मर्म-ऊर्ध्व-सर्व-अवयव-अङ्ग-ज उत्पत्ति-स्थानों की सूची माना गया। छपा ‘संति’ = सन्ति।"),
    "72": ("विश्वास: मध्यम। खुला अवलोकन (05.05.138): सूची में ‘शोष’ अटपटा, शायद ‘श्लेष्म’ की भूल; सुरक्षित सुझाव नहीं; इस पर प्रश्न नहीं। "
           "text_flags: ‘शमायं’ में अतिरिक्त अनुस्वार, शुद्ध ‘शमाय’ (चतुर्थी); इस पर प्रश्न नहीं। "
           "छपा ‘वस्तेः’ = बस्तेः। संधि: विक्षेपसंहारकरो हि = -करः + हि; नान्यद्वस्तेः = न + अन्यत् + बस्तेः। ‘यस्मात्’ का वाक्य 05.05.140 में पूरा।"),
    "73": ("विश्वास: मध्यम। 05.05.139 के ‘यस्मात्’ का वाक्य यहाँ पूरा। संधि: जिते ऽनिले = जिते + अनिले (ए के बाद अ लोप, अवग्रह); "
           "पित्तकफादयोऽपि = -आदयः + अपि; तस्माच्चिकित्सा = तस्मात् + चिकित्सा। छपा ‘चिकित्सार्द्धम्’ (द्द) = चिकित्सार्धम्। "
           "पहले कथन का कर्म (बस्ति) अनुक्त, प्रसंग से। अनिल = वायु।"),
}


AIDS = {
    "62": {
        "story": "अग्निवेश मुनि से पूछते हैं: फलों में बस्तिकर्म में सदा हितकर कौन? पुनर्वसु उसे उपदेश देते हैं; उत्तर अगले श्लोक से।",
        "sandhi": "म् + स्वर, इ + अ → य: मुनिम् + इति + अथ → मुनिमित्यथ; उः + इ → उरि: पुनर्वसुः + इति → पुनर्वसुरिति।",
        "anchors": "पृच्छति स्म = पूछा · धीमान् = बुद्धिमान् · हित = हितकर · सततम् = सदा · प्रशशास = उपदेश दिया।",
    },
    "63": {
        "diagram": {"groups": [{"label": "कुष्ठ", "items": ["गैरागिरी (अस्पष्ट)"]},
                               {"label": "प्रमेह", "items": ["इक्ष्वाकु फल"]},
                               {"label": "हृदामय", "items": ["कुटज फल (प्रवर)"]},
                               {"label": "पाण्डु", "items": ["कौट फल"]}]},
        "sandhi": "म् + स्वर: हितम् + इक्ष्वाकुफलम् → हितमिक्ष्वाकुफलम्; अ + आ → आ: हृद् + आमये → हृदामये।",
        "anchors": "इक्ष्वाकु = सम्भवतः कड़वी लौकी · कुटज = कुड़ा · हृदामय = हृदय का रोग · प्रवर = श्रेष्ठ · पाण्डु = रक्ताल्पता।",
    },
    "64": {
        "frame": "पंक्ति १: कृतवेधन उदर में हितकर · मदन किसी रोग का विरोधी नहीं · पंक्ति २: मदन मधुर, कसैले-कड़वे के साथ, रूखा नहीं, (अनुमानित) तीखा-उष्ण-पिच्छिल।",
        "sandhi": "त् → द् स्वर से पहले: तत् + अरूक्षम् → तदरूक्षम् (‘अरूक्ष’ = रूखा नहीं, ‘रूक्ष’ नहीं)।",
        "anchors": "कृतवेधन = सम्भवतः तोरई · मदन = मैनफल · मधुर = मीठा · कषाय = कसैला · तिक्त = कड़वा · अरूक्ष = जो रूखा नहीं।",
    },
    "65": {
        "diagram": {"groups": [{"label": "मदन के गुण", "items": ["कफ-पित्त हरे", "शीघ्र काम करे", "निरपाय", "वायु का अनुलोमन"]},
                               {"label": "इसलिए", "items": ["आस्थापन में श्रेष्ठ"]}]},
        "sandhi": "त् → द् स्वर से पहले: हृत् + आशुकारि → हृदाशुकारि; त् + न → न्न: यत् + निरपायम् → यन्निरपायम्।",
        "anchors": "हृत् = हरने वाला · आशु = शीघ्र · निरपाय = हानिरहित · अनुलोमि = सीधी दिशा में चलाने वाला · प्रवर = श्रेष्ठ।",
    },
    "66": {
        "frame": "समय: मुनिश्रेष्ठ वचन कहकर रुके (सति-सप्तमी) · क्रिया: फिर निवेदन किया · कर्ता: अनुक्त (प्रसंग से अग्निवेश)।",
        "contrast": "निगद्य ↔ स्थितवति: निगद्य = कहकर (ल्यप्, उपसर्ग नि- के साथ); स्थितवति = रुक जाने पर (क्तवतु, सप्तमी)।",
        "anchors": "मुनिवृषभ = मुनियों में श्रेष्ठ · निगद्य = कहकर · वाक्य = वचन · भूयः = फिर · विज्ञापयाम् बभूव = निवेदन किया।",
    },
    "67": {
        "chunks": "इदम् अतिगहनम् | सह अन्यशिष्यैः | अवनिगतः | (अ)ञ्जलिम् अग्रतः | निधाय",
        "sandhi": "अ + अ → आ: सह + अन्यशिष्यैः → सहान्यशिष्यैः; अः + अ → ओऽ: अवनिगतः + अञ्जलिम् → अवनिगतोऽञ्जलिम्।",
        "anchors": "अतिगहन = बहुत गहरा · अन्य = दूसरे · अवनि = भूमि · अग्रतः = आगे · निधाय = रखकर।",
    },
    "68": {
        "frame": "किसने कहा: गुरु · किसके बारे में: बस्ति, विचित्र कर्म-गुण करने वाली · प्रश्न: वह शीघ्र, देह से सब ओर से, दोषों को कैसे हटाती है?",
        "sandhi": "आ + उ → ओ: गुरुणा + उक्तः → गुरुणोक्तः; अ + ए → ऐ: च + एति → चैति; म् + स्वर: कथम् + अपोहति → कथमपोहति।",
        "anchors": "चित्र = विविध · कृत् = करने वाला · उक्त = कहा गया · शीघ्र = जल्दी · अपोहति = हटाता है।",
    },
    "69": {
        "frame": "वक्ता: गुरु · विषय: देह का जो कुछ बाहर या भीतर आश्रित है · उत्तर: वह स्तिमित वायु के वश में है।",
        "sandhi": "त् + ब → द्ब: यत् + बहिः → यद्बहिः (छपा ‘यद्वहि’, व/ब); म् + स्वर: अपाश्रितम् + अन्तरे → अपाश्रितमन्तरे।",
        "anchors": "ऊचे = कहा · मारुत = वायु · वश्य = वश में · बहिः = बाहर · अन्तरे = भीतर।",
    },
    "70": {
        "chain": {"steps": ["दूषित (वायु)", "बस्ति उसमें अनुलोमता उत्पन्न करे", "रोगों के समूह नष्ट (शब्द का पहला भाग अस्पष्ट)"]},
        "sandhi": "न् द्वित्व ह्रस्व स्वर के बाद: जनयन् + अनुलोमताम् → जनयन्ननुलोमताम्; इः → इर् सघोष से पहले: बस्तिः + हिनस्ति → बस्तिर्हिनस्ति।",
        "anchors": "दुष्ट = दूषित · जनयन् = उत्पन्न करता हुआ · अनुलोमता = स्वाभाविक दिशा · हिनस्ति = नष्ट करता है · पूग = समूह।",
    },
    "71": {
        "diagram": {"groups": [{"label": "रोग कहाँ", "items": ["शाखा", "कोष्ठ", "मर्म", "ऊर्ध्व", "सब अवयव-अंग"]},
                               {"label": "जन्म का हेतु", "items": ["केवल वायु"]}]},
        "sandhi": "आः → आश् च से पहले: कोष्ठगताः + च → कोष्ठगताश्च; अ + ऊ → ओ: मर्म + ऊर्ध्व → मर्मोर्ध्व; उः + अ → उर: हेतुः + अस्ति → हेतुरस्ति।",
        "anchors": "शाखा = डाली (शाखा) · कोष्ठ = कोठा (कोष्ठ) · मर्म = मर्म-स्थान · हेतु = कारण · जन्म = उत्पत्ति।",
    },
    "72": {
        "chain": {"steps": ["वायु: मल-संचयों का विक्षेप और संहार करे", "वायु अत्यन्त बढ़े", "उसके शमन के लिए बस्ति के समान औषध नहीं", "क्योंकि … (अगला श्लोक)"]},
        "sandhi": "अः → ओ सघोष से पहले: -करः + हि → -करो हि; अ + अ → आ: न + अन्यत् → नान्यत्; त् → द् सघोष से पहले: अन्यत् + बस्तेः → अन्यद्बस्तेः।",
        "anchors": "विक्षेप = बिखेरना · संहार = समेटना · आचय = संचय · अतिवृद्ध = बहुत बढ़ा · भेषज = औषध · सम = बराबर।",
    },
    "73": {
        "chain": {"steps": ["वायु यत्न से जीता गया", "उससे प्रेरित पित्त-कफ आदि भी शान्त", "इसलिए बस्ति: चिकित्सा का आधा", "कुछ के मत में: सम्पूर्ण चिकित्सा"]},
        "sandhi": "अः + अ → ओऽ: -आदयः + अपि → -आदयोऽपि; त् + च → च्च: तस्मात् + चिकित्सा → तस्माच्चिकित्सा।",
        "anchors": "शाम्यन्ति = शान्त होते हैं · यत्न = प्रयत्न · जित = जीता हुआ · ईरित = प्रेरित · अर्ध = आधा · एके = कुछ लोग।",
    },
}


IMAGE_SPECS = {
    ("62", "story"): {
        "file": "ka5-phala-prashna-62.svg",
        "alt": ("Flowchart of verse 62: the wise Agnivesha asks the sage which of the fruits may be always "
                "beneficial in basti-action; Punarvasu instructs him"),
        "type": "mermaid",
        "code": ('flowchart TD\n  A["धीमान् अग्निवेश"] --> B["मुनि से प्रश्न"]\n'
                 '  B --> C["फलों में बस्तिकर्म में<br/>सदा हितकर कौन?"]\n'
                 '  C --> D["पुनर्वसु ने<br/>उपदेश दिया"]\n'),
    },
    ("63", "diagram"): {
        "file": "ka5-phala-roga-63.svg",
        "alt": ("Table of verse 63: four fruits and the diseases they are named for: gairagiri (unclear) in kushtha, "
                "ikshvaku fruit for prameha, kutaja fruit foremost in heart ailment, kauta fruit in pandu"),
        "type": "table",
        "title": "श्लोक ६३: फल और रोग",
        "heads": ["फल", "किसमें हितकर"],
        "rows": [["गैरागिरी (अस्पष्ट)", "कुष्ठ"], ["इक्ष्वाकु फल", "प्रमेह वालों के लिए"],
                 ["कुटज फल", "हृदय रोग में श्रेष्ठ"], ["कौट फल", "पाण्डु"]],
    },
    ("65", "diagram"): {
        "file": "ka5-madana-pravara-65.svg",
        "alt": ("Mind map of verse 65: madana removes Kapha and Pitta, acts quickly, is harmless and moves the "
                "wind in its natural direction; therefore it is foremost in asthapana"),
        "type": "mermaid",
        "code": ('mindmap\n  मदन: आस्थापन में श्रेष्ठ\n    कफ-पित्त हरे\n    शीघ्र काम करे\n'
                 '    निरपाय\n    वायु का अनुलोमन\n'),
    },
    ("70", "chain"): {
        "file": "ka5-anulomata-70.svg",
        "alt": ("Chain of unit 70: the spoiled (wind); the basti produces its natural direction; groups of diseases "
                "are destroyed (first part of the word unclear)"),
        "type": "chain",
        "title": "इकाई ७०: बस्ति का काम",
        "steps": ["दूषित (वायु)", "बस्ति अनुलोमता उत्पन्न करे", "रोग-समूह नष्ट (पहला भाग अस्पष्ट)"],
    },
    ("71", "diagram"): {
        "file": "ka5-vayu-hetu-71.svg",
        "alt": ("Mind map of verse 71: diseases in the branches, the storehouse, the vital spots, the upper parts "
                "and all parts and limbs have no cause of origin other than wind"),
        "type": "mermaid",
        "code": ('mindmap\n  रोगों का हेतु: केवल वायु\n    शाखा में\n    कोष्ठ में\n    मर्म में\n'
                 '    ऊर्ध्व भाग में\n    सब अवयव-अंगों में\n'),
    },
    ("72", "chain"): {
        "file": "ka5-vikshepa-samhara-72.svg",
        "alt": ("Flowchart of verse 72: wind scatters and gathers the accumulations of wastes; for the greatly "
                "increased wind no remedy equals basti; the reason follows in the next verse"),
        "type": "mermaid",
        "code": ('flowchart TD\n  A["वायु: मल-संचयों का<br/>विक्षेप और संहार"] --> B["वायु अत्यन्त बढ़े"]\n'
                 '  B --> C["शमन के लिए बस्ति के<br/>समान औषध नहीं"]\n'
                 '  C --> D["क्योंकि ...<br/>अगला श्लोक"]\n'),
    },
    ("73", "chain"): {
        "file": "ka5-chikitsardha-73.svg",
        "alt": ("Flowchart of verse 73: when wind is conquered with effort, Pitta, Kapha and the rest stirred by it "
                "are pacified; therefore basti is called half of treatment, and by some the whole treatment"),
        "type": "mermaid",
        "code": ('flowchart TD\n  A["वायु यत्न से जीता"] --> B["उससे प्रेरित<br/>पित्त-कफ आदि भी शान्त"]\n'
                 '  B --> C["इसलिए बस्ति:<br/>चिकित्सा का आधा"]\n'
                 '  B --> D["कुछ के मत में:<br/>सम्पूर्ण चिकित्सा"]\n'),
    },
}
