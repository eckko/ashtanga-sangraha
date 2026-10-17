from helpers import mcq, match, order, fill, multi, accepts

AUTHORED = {}

# ---------------------------------------------------------------- unit 37
AUTHORED["37"] = {
    "title": "शालिषष्टिकगोधूम",
    "question": "Which foods does line 1 list, and what does line 2 say of the means?",
    "rule": ("Line 1 lists śāli, ṣaṣṭika, wheat, mung, meat, ghee and the like. "
             "Line 2: through combination with agreeable, kindling medicinal "
             "substances, by means that give relish and digestion."),
    "limits": ("No main verb: the phrases continue from the unit before and "
               "the sentence goes on in unit 38. Śāli and ṣaṣṭika are names "
               "of rice kinds only. No amounts, no way of combining, and no "
               "effect beyond what line 2 states."),
    "explain_hi": ("यह इकाई एक लंबे वाक्य का बीच का हिस्सा है, इसलिए इसमें अपनी क्रिया नहीं है। "
                   "पहली पंक्ति में शालि, षष्टिक, गेहूँ (गोधूम), मूँग (मुद्ग), मांस और घृत "
                   "‘आदि’ के साथ गिनाए गए हैं, और अंत का ‘-भिः’ तृतीया बहुवचन है: ‘इनसे’। "
                   "दूसरी पंक्ति कहती है कि हृद्य (मन को प्रिय) और दीपन भैषज्य द्रव्यों के संयोग से, "
                   "ऐसे साधनों द्वारा जो रुचि और पाचन देते हैं। मात्रा या विधि इस इकाई में नहीं है।"),
    "hook": "शालि, षष्टिक, गोधूम, मुद्ग, मांस, घृत — आदि से; और संयोग रुचि-पाचन देने वाला।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What does line 1 of this unit list?",
            ("Foods such as rice, wheat, mung, meat and ghee",
             "Line 1 names शालि, षष्टिक, गोधूम, मुद्ग, मांस and घृत."),
            [("Kinds of enema and massage", "Massage and enemas come in the next unit."),
             ("Signs by which a disease is known", "No sign of any disease is named here."),
             ("Names of the seasons of the year", "No season is named in this unit.")],
            "Line 1 is a list of foods, ending with आदि, 'and the like'.",
            "शालि · षष्टिक · गोधूम · मुद्ग · मांस · घृत · आदि."),
        order(1, "Put the foods of line 1 in the order of the verse.",
              ["शालि", "षष्टिक", "गोधूम", "मुद्ग", "मांस", "घृत"],
              "The line runs शालि, षष्टिक, गोधूम, मुद्ग, मांस, घृत and then आदि.",
              "शालि · षष्टिक · गोधूम · मुद्ग · मांस · घृत."),
        match(2, "Match each food name of line 1 to its meaning.",
              [["गोधूम", "wheat"], ["मुद्ग", "mung"], ["मांस", "meat"], ["घृत", "ghee"]],
              "These four names stand inside the long joined word of line 1.",
              "गोधूम = wheat; मुद्ग = mung; मांस = meat; घृत = ghee.",
              role="extend",
              teaches="A list of foods can be joined into one long word that ends in आदिभिः, 'with these and the like'."),
        mcq("discriminate", 3, "Which is the right split of संयोगाद्रुचि-?",
            ("संयोगात् + रुचि",
             "A final त् before a voiced sound such as र becomes द्."),
            [("संयोगाः + रुचि", "A visarga here would give संयोगा रुचि, not द्."),
             ("संयोगा + द्रुचि", "द्रुचि is not a word on the card."),
             ("संयोगाम् + रुचि", "A final म् would stay म् or become a dot, not द्.")],
            "संयोगात् (from the combination, ablative) + रुचि (relish) join as संयोगाद्रुचि.",
            "त् + voiced sound → द्: संयोगात् + रुचि = संयोगाद्रुचि."),
        mcq("apply", 4, "What does the ending -भिः of ...घृतादिभिः show?",
            ("Instrumental plural: 'with' or 'by means of' these",
             "The ending -भिः marks the instrumental plural."),
            [("Genitive plural: 'of' these", "The genitive plural would end in -आम्."),
             ("Locative plural: 'in' these", "The locative plural would end in -एषु."),
             ("Nominative plural: 'these' as subject", "The nominative plural would end in -आः or -इ.")],
            "The foods are the means: the ending -भिः says 'with ... and the like'.",
            "-भिः = instrumental plural, 'with / by means of'."),
        mcq("transfer", 5, "Following रुचिपक्तिदैः, what does the invented word सुखदैः mean?",
            ("By (means) giving happiness",
             "A compound ending in -द gives 'giving' the first part, here happiness."),
            [("By (means) free from happiness", "-द does not mean free from."),
             ("By happy ones", "The idea is 'giving' happiness, not being happy."),
             ("Of (those) giving happiness", "The ending -ऐः is instrumental, not 'of'.")],
            "In रुचिपक्तिदैः the end -द means 'giving' relish and digestion; सुखदैः works the same way.",
            "X-द (from दा, to give) = giving X.",
            teaches="A compound ending in -द means 'giving' the first part: रुचिपक्तिद = giving relish and digestion; सुखद = giving happiness."),
    ],
}

# ---------------------------------------------------------------- unit 38
AUTHORED["38"] = {
    "title": "साभ्यंगोद्वर्तनस्नान",
    "question": "By which means, and what does the person obtain?",
    "rule": ("By means of oil massage together with rubbing, bathing, and "
             "nirūha and sneha enemas (basti): thus he obtains comfort (शर्म) "
             "and keenness of all the fires."),
    "limits": ("The reading 'nirūha and sneha as two kinds of basti' is the "
               "data's choice. साभ्यंग may attach to the whole list. 'Fire' "
               "(पावक) is read as the digestive fires. The sentence goes on in "
               "unit 39, which gives more things obtained; no question here "
               "depends on that."),
    "explain_hi": ("पिछली इकाई के उपायों के बाद यहाँ और साधन गिनाए गए हैं: अभ्यंग सहित उद्वर्तन, स्नान, "
                   "और निरूह तथा स्नेह बस्तियाँ। ‘साभ्यंग’ का अर्थ है ‘अभ्यंग के साथ’। "
                   "दूसरी पंक्ति में फल बताया गया है: ‘तथा’ वह शर्म (सुख) और सब अग्नियों की "
                   "तीक्ष्णता (पाटव) प्राप्त करता है। ‘लभते’ वर्तमान, आत्मनेपद है। "
                   "वाक्य अगली इकाई में भी चलता है, इसलिए यहाँ केवल इसी इकाई की बात पूछी गई है।"),
    "hook": "अभ्यंग, उद्वर्तन, स्नान, निरूह-स्नेह बस्ति — से सुख और सब अग्नियों की तीक्ष्णता।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What does the person obtain, as the second line of this unit puts it?",
            ("Comfort and keenness of all the fires",
             "The line says शर्म and सर्वपावकपाटवम्."),
            [("Wealth and children", "Neither is named in this unit."),
             ("Victory and fame", "Neither is named in this unit."),
             ("Speech and beauty", "Neither is named in this unit.")],
            "लभते शर्म सर्वपावकपाटवम्: he obtains comfort and keenness of all the fires.",
            "लभते = obtains; शर्म = comfort; सर्वपावकपाटवम् = keenness of all fires."),
        order(1, "Put the means of line 1 in the order of the verse.",
              ["साभ्यंग", "उद्वर्तन", "स्नान", "निरूह", "स्नेह", "बस्ति"],
              "The line runs: with massage, rubbing, bathing, then nirūha, sneha and basti.",
              "साभ्यंग · उद्वर्तन · स्नान · निरूह · स्नेह · बस्ति."),
        mcq("extend", 2, "Which is the right split of साभ्यंगोद्वर्तन-?",
            ("स + अभ्यंग + उद्वर्तन",
             "स + अ gives आ; and अभ्यंग + उ gives ओ."),
            [("सा + भ्यंग + उद्वर्तन", "भ्यंग is not a word."),
             ("स + अभ्यंगः + उद्वर्तन", "A visarga would not disappear like this before उ."),
             ("साभ्य + ंगो + द्वर्तन", "None of these parts is a word.")],
            "स (with) + अभ्यंग (oil massage) + उद्वर्तन (rubbing) join as साभ्यंगोद्वर्तन.",
            "अ + अ → आ; अ + उ → ओ.",
            teaches="Two short a-sounds join into आ (स + अभ्यंग = साभ्यंग), and अ + उ joins into ओ (अभ्यंग + उद्वर्तन = अभ्यंगोद्वर्तन)."),
        match(3, "Match each word of line 2 to its meaning.",
              [["शर्म", "comfort"], ["पावक", "fire"], ["पाटव", "keenness"], ["लभते", "obtains"]],
              "These four words carry the result of the verse.",
              "शर्म = comfort; पावक = fire; पाटव = keenness; लभते = obtains.",
              role="discriminate"),
        multi("apply", 4, "Which of these are named in line 1?",
              [("अभ्यंग (oil massage)", "Right: it opens the list, inside साभ्यंग."),
               ("स्नान (bathing)", "Right: it is the third item."),
               ("बस्ति (enema)", "Right: it closes the list."),
               ("वमन (emesis)", "Not in line 1."),
               ("नस्य (nasal drops)", "Not in line 1.")],
              [0, 1, 2],
              "Line 1 names massage, rubbing, bathing and the two kinds of basti; emesis and nasal drops are not in it.",
              "Line 1: अभ्यंग, उद्वर्तन, स्नान, निरूह, स्नेह, बस्ति."),
        mcq("transfer", 5, "By the pattern of साभ्यंग, what does the invented word सपुत्रः mean?",
            ("Together with a son",
             "स- at the start means 'together with'."),
            [("Without a son", "'Without' would be अ- or निः-, not स-."),
             ("Born of a son", "Nothing in स- means 'born of'."),
             ("Of a son", "That would be पुत्रस्य.")],
            "साभ्यंग = स + अभ्यंग, 'together with massage'; सपुत्र = 'together with a son'.",
            "स- + noun = 'together with'.",
            teaches="A word that begins with स- in a compound means 'together with' the rest: साभ्यंग = with oil massage; सपुत्र = with a son."),
    ],
}

# ---------------------------------------------------------------- unit 39
AUTHORED["39"] = {
    "title": "धीवर्णेंद्रियवैमल्यं",
    "question": "What do the two lines name?",
    "rule": ("Line 1 names clarity of intellect, complexion and senses, virility "
             "and length of life. Line 2 begins a relative clause: 'those that "
             "arise from bhūtas, poison, wind, fire, wounds, fractures and the like'."),
    "limits": ("Line 1 finishes the things obtained in unit 38. Line 2 begins a "
               "clause that is completed in unit 40, so the noun it speaks of is "
               "not in this unit. भूत here means beings or spirits. The verse "
               "says nothing of how any of these is brought about."),
    "explain_hi": ("पहली पंक्ति पिछली इकाई के ‘लभते’ का शेष कर्म पूरा करती है: बुद्धि, वर्ण और "
                   "इन्द्रियों की निर्मलता, वृषता और आयु की दीर्घता। दूसरी पंक्ति ‘ये’ से एक नया वाक्यांश "
                   "शुरू करती है: ‘जो भूत, विष, वायु, अग्नि, क्षत, भंग आदि से उत्पन्न होते हैं’। "
                   "जिसके बारे में यह कहा जा रहा है, वह शब्द (गदाः) अगली इकाई में आता है, "
                   "इसलिए यहाँ वाक्य अधूरा है। यहाँ ‘भूत’ का अर्थ प्राणी या आत्माएँ है।"),
    "hook": "बुद्धि-वर्ण-इन्द्रिय की निर्मलता, वृषता, दीर्घ आयु; और — जो भूत, विष, वायु, अग्नि, क्षत, भंग से उपजे।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "Line 2 lists bhūtas, poison, wind, fire, wounds and fractures. What do they share?",
            ("Each is a source from which something arises",
             "संभवाः means 'arising from': the list gives the sources."),
            [("Each is a remedy that something removes", "Nothing in the line calls them remedies."),
             ("Each is a food that something is eaten with", "None of the six is a food here."),
             ("Each is a season in which something occurs", "None of the six is a season.")],
            "भूतविषवाय्वग्निक्षतभंगादिसंभवाः = arising from bhūtas, poison, wind, fire, wounds, fractures and the like.",
            "-संभव = arising from; the list gives the sources."),
        order(1, "Put the sources of line 2 in the order of the verse.",
              ["भूत", "विष", "वायु", "अग्नि", "क्षत", "भंग"],
              "The line runs भूत, विष, वायु, अग्नि, क्षत, भंग and then आदि.",
              "भूत · विष · वायु · अग्नि · क्षत · भंग."),
        match(2, "Match each source of line 2 to its meaning.",
              [["भूत", "beings or spirits"], ["विष", "poison"], ["क्षत", "wound"], ["भंग", "fracture"]],
              "These four words stand in the long joined word of line 2.",
              "भूत = beings or spirits; विष = poison; क्षत = wound; भंग = fracture.",
              role="extend",
              teaches="In this list भूत means beings or spirits, and the other nouns are plain words for poison, wound and fracture."),
        mcq("discriminate", 3, "Which is the right split of धीवर्णेंद्रिय-?",
            ("धी + वर्ण + इन्द्रिय",
             "अ + इ joins as ए: वर्ण + इन्द्रिय = वर्णेन्द्रिय."),
            [("धी + वर्णे + न्द्रिय", "न्द्रिय is not a word."),
             ("धी + वर्ण + एन्द्रिय", "एन्द्रिय is not a word; the ए comes from joining."),
             ("धीव + र्णेन्द्रिय", "Neither part is a word.")],
            "धी (intellect), वर्ण (complexion) and इन्द्रिय (sense) are joined; अ + इ became ए.",
            "अ + इ → ए: वर्ण + इन्द्रिय = वर्णेन्द्रिय."),
        multi("apply", 4, "Which of these are named in line 2 as sources?",
              [("poison (विष)", "Right: it is the second item."),
               ("fire (अग्नि)", "Right: it is the fourth item."),
               ("fractures (भंग)", "Right: it is the sixth item."),
               ("cold (शीत)", "Not in line 2."),
               ("hunger (क्षुध्)", "Not in line 2.")],
              [0, 1, 2],
              "Poison, fire and fractures are in the list; cold and hunger are not.",
              "Line 2: भूत, विष, वायु, अग्नि, क्षत, भंग, आदि."),
        mcq("transfer", 5, "By the pattern of ...संभवाः, what does the invented word जलसंभवाः mean?",
            ("Arising from water",
             "-संभव at the end means 'arising from' the first part."),
            [("Dwelling in water", "Dwelling would be a different ending, such as -स्थ."),
             ("Leading to water", "'Leading to' is not what -संभव says."),
             ("Protecting water", "Nothing in -संभव means protecting.")],
            "In भूतविष...संभवाः the end -संभव means 'arising from'; जलसंभवाः works the same.",
            "X-संभव = arising from X.",
            teaches="A compound ending in -संभव means 'arising from' the first part: भंगादिसंभव = arising from fractures and the like; जलसंभव = arising from water."),
    ],
}

# ---------------------------------------------------------------- unit 40
AUTHORED["40"] = {
    "title": "कामक्रोधभयाद्याश्च",
    "question": "What does line 1 call the diseases that come from desire, anger and fear?",
    "rule": ("Those from desire, anger, fear and the like are called "
             "adventitious (आगन्तु) diseases. Line 2 begins a new list: "
             "abandonment of errors of the intellect, calming of the senses, memory."),
    "limits": ("Line 1 completes the clause begun in unit 39. Line 2 is a list "
               "with no verb in this unit: the verse does not say here what "
               "these three do. स्मृति may also be 'mindfulness'."),
    "explain_hi": ("पहली पंक्ति पिछली इकाई का वाक्य पूरा करती है: जो काम, क्रोध, भय आदि से (उत्पन्न होते हैं), "
                   "‘वे आगन्तु गद (रोग) होते हैं’। ‘तेस्युः’ में ‘ते स्युः’ (वे हों) है। दूसरी पंक्ति नई सूची "
                   "शुरू करती है: प्रज्ञापराधों का त्याग, इन्द्रियों का उपशम और स्मृति। इस इकाई में "
                   "इनकी क्रिया नहीं है, इसलिए यह नहीं कहा जा सकता कि ये क्या करते हैं। "
                   "‘स्मृति’ का अर्थ सजगता भी हो सकता है।"),
    "hook": "काम-क्रोध-भय आदि से जो उपजें, वे आगन्तु गद; फिर सूची: प्रज्ञापराध-त्याग, इन्द्रिय-उपशम, स्मृति।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "What does line 1 call the diseases coming from desire, anger, fear and the like?",
            ("Adventitious (आगन्तु) diseases",
             "The line says तेस्युरागंतवो गदाः: they would be the adventitious diseases."),
            [("Innate (निज) diseases", "The verse does not use निज in this unit."),
             ("Seasonal (ऋतुज) diseases", "Nothing in the line is about a season."),
             ("Diseases of the body alone", "The line gives no such name.")],
            "आगन्तु means adventitious; गद means disease; the line calls the diseases from desire, anger and fear by that name.",
            "काम-क्रोध-भय-आदि → आगन्तु गद."),
        order(1, "Put the three named causes of line 1 in the order of the verse.",
              ["काम", "क्रोध", "भय"],
              "The line runs काम, क्रोध, भय and then आद्याः, 'and the like'.",
              "काम · क्रोध · भय."),
        match(2, "Match each word to its meaning.",
              [["आगन्तु", "adventitious"], ["गद", "disease"], ["त्याग", "abandonment"], ["उपशम", "calming"]],
              "Two words come from line 1 and two from line 2.",
              "आगन्तु = adventitious; गद = disease; त्याग = abandonment; उपशम = calming.",
              role="extend",
              teaches="The nouns त्यागः and इन्द्रियोपशमः of line 2 are single words; त्याग means abandonment and उपशम means calming."),
        mcq("discriminate", 3, "Which is the right split of तेस्युरागंतवो?",
            ("ते + स्युः + आगंतवः",
             "A visarga after उ before a vowel becomes र्: स्युः + आ = स्युरा."),
            [("ते + स्यू + रागंतवः", "रागंतवः is not a word."),
             ("तेस् + युरा + गंतवः", "None of these parts is a word."),
             ("ते + स्युर् + रागंतवः", "A र् would not be written twice here.")],
            "ते (they) + स्युः (would be) + आगंतवः (adventitious); the final visarga also became ओ before the voiced ग of गदाः.",
            "उः + vowel → उर् + vowel: स्युः + आगंतवः = स्युरागंतवः."),
        fill(4, "The word for 'diseases' in line 1 is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("गदाः"),
             "गदाः is the plural of गद, disease.",
             "गदाः (diseases) ends the clause of line 1.",
             "गदाः = diseases.", role="apply"),
        mcq("transfer", 5, "By the pattern of कामक्रोधभयाद्याः, what does the invented word रूपरसगंधाद्याः mean?",
            ("Form, taste, smell and the like",
             "-आद्याः means 'having these as the first', that is 'and the like'."),
            [("The end of form, taste and smell", "आद्य means first, not end."),
             ("Without form, taste and smell", "'Without' would use a negating अ-."),
             ("The best among form, taste and smell", "आद्य here gives 'first of a group', not 'best'.")],
            "In कामक्रोधभयाद्याः the end -आद्याः turns the list into 'desire, anger, fear and the like'.",
            "X-Y-आद्याः = X, Y and the like.",
            teaches="A list ending in -आद्याः means 'these and the like': कामक्रोधभयाद्याः = desire, anger, fear and the like."),
    ],
}

# ---------------------------------------------------------------- unit 41
AUTHORED["41"] = {
    "title": "देशकालात्मविज्ञानं",
    "question": "What does the unit list in line 1 and line 2?",
    "rule": ("Line 1 gives knowledge of place, time and self (and a following of "
             "conduct: the word is damaged). Line 2: the pacificatory rite "
             "prescribed in the Atharva (Veda), worship of unfavourable grahas."),
    "limits": ("The printed सवृत्तस्य is probably a damaged सद्वृत्तस्य "
               "('of good conduct'); no question uses it. A list with no verb. "
               "'graha' stays graha (planet or seizing spirit). The verse "
               "does not say what any item does."),
    "explain_hi": ("यह इकाई सूची है और इसमें क्रिया नहीं है। पहली पंक्ति में देश, काल और आत्मा (स्वयं) का ज्ञान है; "
                   "उसके बाद ‘सवृत्तस्य अनुवर्तनम्’ छपा है, जहाँ ‘सवृत्त’ संभवतः ‘सद्वृत्त’ (अच्छा आचरण) है, "
                   "पर यह अनुमान है और प्रश्नों में नहीं लिया गया। दूसरी पंक्ति में अथर्व में विहित शान्ति (शान्ति कर्म) "
                   "और प्रतिकूल ग्रहों की अर्चना गिनाई गई है। ‘ग्रह’ को ग्रह ही रखा गया है।"),
    "hook": "देश-काल-आत्मा का ज्ञान · (सद्वृत्त का अनुसरण) · अथर्व-विहित शान्ति · प्रतिकूल ग्रहों की अर्चना।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "Which rite does line 2 name first, and where is it said to be prescribed?",
            ("A pacificatory rite prescribed in the Atharva (Veda)",
             "अथर्वविहिता शान्तिः is the first item of line 2."),
            [("A sacrifice prescribed in the Ṛgveda", "The line names the Atharva, not the Ṛgveda."),
             ("A penance prescribed in the law books", "The line names the Atharva."),
             ("A bath prescribed in the Yajurveda", "The line names the Atharva, and a pacificatory rite.")],
            "अथर्वविहिता शान्तिः = the pacificatory rite prescribed in the Atharva (Veda).",
            "अथर्वविहिता शान्तिः = pacificatory rite prescribed in the Atharva."),
        order(1, "Put the three things whose knowledge opens line 1 in the order of the verse.",
              ["देश", "काल", "आत्मा"],
              "The word runs देश, काल, आत्म and then विज्ञानम्, 'knowledge'.",
              "देश · काल · आत्मा."),
        match(2, "Match each word of line 2 to its meaning.",
              [["प्रतिकूल", "unfavourable"], ["अर्चन", "worship"], ["शान्ति", "pacificatory rite"], ["विहित", "prescribed"]],
              "These four words build the two items of line 2.",
              "प्रतिकूल = unfavourable; अर्चन = worship; शान्ति = pacificatory rite; विहित = prescribed.",
              role="extend",
              teaches="विहित means 'prescribed': अथर्वविहिता is 'prescribed in the Atharva'."),
        mcq("discriminate", 3, "Which is the right split of प्रतिकूलग्रहार्चनं?",
            ("प्रतिकूल + ग्रह + अर्चनं",
             "अ + अ joins as आ: ग्रह + अर्चन = ग्रहार्चन."),
            [("प्रति + कूलग्रह + आर्चनं", "आर्चनं is not a word."),
             ("प्रतिकूल + ग्रहार् + चनं", "ग्रहार् and चनं are not words."),
             ("प्रतिकूलग्र + हार्चनं", "Neither part is a word.")],
            "प्रतिकूल (unfavourable) + ग्रह (graha) + अर्चनं (worship) make one word.",
            "अ + अ → आ: ग्रह + अर्चन = ग्रहार्चन."),
        multi("apply", 4, "Which of these are named in this unit?",
              [("knowledge of place", "Right: देश opens line 1."),
               ("knowledge of time", "Right: काल is next."),
               ("worship of unfavourable grahas", "Right: it closes line 2."),
               ("oil massage", "Massage is in unit 38."),
               ("bathing", "Bathing is in unit 38.")],
              [0, 1, 2],
              "Place, time and the worship of unfavourable grahas are in the unit; massage and bathing belong to unit 38.",
              "Unit 41: देश, काल, आत्मा; अथर्वविहिता शान्तिः; प्रतिकूलग्रहार्चनम्."),
        mcq("transfer", 5, "By the pattern of अथर्वविहिता, what does the invented phrase वेदविहितं कर्म mean?",
            ("An action prescribed in the Veda",
             "-विहित means 'prescribed in' the first part."),
            [("An action rejected by the Veda", "विहित does not mean rejected."),
             ("An action done before the Veda", "Nothing in विहित gives 'before'."),
             ("An action that is the Veda itself", "विहित says 'prescribed', not 'identical with'.")],
            "In अथर्वविहिता the first part says where, the second says 'prescribed'; वेदविहित is built the same.",
            "X-विहित = prescribed in X.",
            teaches="A compound X-विहित means 'prescribed in X': अथर्वविहिता = prescribed in the Atharva; वेदविहित = prescribed in the Veda."),
    ],
}

# ---------------------------------------------------------------- unit 42
AUTHORED["42"] = {
    "title": "भूताद्यस्पर्शनोपायो",
    "question": "What has been indicated separately, and what shown in brief?",
    "rule": ("The means of not being touched by bhūtas and the like has been "
             "indicated, each separately. For non-arising, this procedure has "
             "been shown in brief."),
    "limits": ("Whose non-arising is meant is in unit 43 (innate and "
               "adventitious disorders): this unit does not say it. The verse "
               "does not repeat the means here."),
    "explain_hi": ("पहली पंक्ति कहती है कि भूत आदि के स्पर्श से बचने का उपाय ‘पृथक्-पृथक्’ (अलग-अलग) बताया जा चुका है। "
                   "दूसरी पंक्ति में ‘अनुत्पत्त्यै’ (उत्पन्न न होने के लिए) चतुर्थी है, और ‘समासेन’ का "
                   "अर्थ है ‘संक्षेप में’। ‘यह विधि दिखाई गई है’ कहकर पूरा वाक्य बंद होता है। "
                   "किसके उत्पन्न न होने की बात है, यह अगली इकाई में आता है, इसलिए यहाँ केवल इतना पूछा गया है "
                   "जितना इन दो पंक्तियों में है।"),
    "hook": "उपाय अलग-अलग बताया; अनुत्पत्ति के लिए यह विधि संक्षेप में दिखाई गई।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "What does the unit say has been shown in brief?",
            ("This procedure, for non-arising",
             "विधिरेषः प्रदर्शितः with अनुत्पत्त्यै and समासेन."),
            [("A cure for each single disease", "No cure for single diseases is named."),
             ("A list of all medicines", "No list of medicines is named here."),
             ("A rule for the seasons of the year", "No season is named here.")],
            "The second line says: for non-arising, this procedure has been shown in brief.",
            "अनुत्पत्त्यै समासेन विधिरेषः प्रदर्शितः."),
        order(1, "Put the parts of line 2 in the order of the verse.",
              ["अनुत्पत्त्यै", "समासेन", "विधिरेषः", "प्रदर्शितः"],
              "The line runs अनुत्पत्त्यै, समासेन, विधिः एषः, प्रदर्शितः.",
              "अनुत्पत्त्यै · समासेन · विधिरेषः · प्रदर्शितः."),
        match(2, "Match each word to its meaning.",
              [["पृथक्पृथक्", "separately"], ["समासेन", "in brief"],
               ["अनुत्पत्त्यै", "for non-arising"], ["प्रदर्शितः", "shown"]],
              "These four words carry the two statements of the unit.",
              "पृथक्पृथक् = separately; समासेन = in brief; अनुत्पत्त्यै = for non-arising; प्रदर्शितः = shown.",
              role="extend",
              teaches="Words such as पृथक्पृथक् (doubled for 'each separately') and समासेन ('in brief') tell how a matter has been treated."),
        mcq("discriminate", 3, "Which is the right split of विधिरेषः?",
            ("विधिः + एषः",
             "A visarga after इ before a vowel becomes र्."),
            [("विधि + रेषः", "रेषः is not a word."),
             ("विधिरे + षः", "षः is not a word."),
             ("विधिः + अषः", "अषः is not a word on the card.")],
            "विधिः (procedure) + एषः (this) join as विधिरेषः.",
            "इः + vowel → इर् + vowel: विधिः + एषः = विधिरेषः."),
        mcq("apply", 4, "How does line 1 say the means of not being touched by bhūtas has been indicated?",
            ("Each one separately",
             "पृथक्पृथक् means separately."),
            [("All together as one", "The line says the opposite: separately."),
             ("Only in the next chapter", "The line says it has been indicated already."),
             ("Without naming any means", "The line says a means has been indicated.")],
            "निर्दिष्टश्च पृथक्पृथक्: and indicated, each separately.",
            "पृथक्पृथक् = each separately."),
        mcq("transfer", 5, "By the pattern of अनुत्पत्त्यै, what does the invented रक्षायै in विधिः रक्षायै mean?",
            ("For protection",
             "A feminine word's dative singular ends in -ऐ and says 'for'."),
            [("By protection", "'By' would be रक्षया."),
             ("In protection", "'In' would be रक्षायाम्."),
             ("From protection", "'From' would be रक्षायाः.")],
            "अनुत्पत्त्यै is the dative of अनुत्पत्ति: 'for non-arising'; रक्षायै is the dative of रक्षा.",
            "Feminine dative singular -ऐ = for the sake of.",
            teaches="The dative singular of a feminine word ends in -ऐ (अनुत्पत्त्यै, रक्षायै) and says 'for ...': purpose."),
    ],
}

# ---------------------------------------------------------------- unit 43
AUTHORED["43"] = {
    "title": "निजागंतुविकाराणां",
    "question": "Of which disorders, and for what, is this line?",
    "rule": ("A single line: of innate and adventitious disorders, and for the "
             "pacification of those that have arisen. It completes unit 42."),
    "limits": ("This is one half-verse line; the printed pairs run one line out "
               "of step, so the verb is in unit 42 (shown). Here only the "
               "objects of the purpose are stated, nothing else."),
    "explain_hi": ("यह अकेली पंक्ति है और इकाई ४२ का वाक्य पूरा करती है। ‘निज’ (सहज) और ‘आगन्तु’ (बाहर से आने वाले) "
                   "विकारों के लिए, और जो विकार उत्पन्न हो चुके हैं उनकी शान्ति के लिए। "
                   "‘शान्तये’ चतुर्थी है: ‘शान्ति के लिए’। पिछली इकाई की ‘अनुत्पत्त्यै’ और यहाँ की ‘शान्तये’ "
                   "दो उद्देश्य हैं। क्रिया (प्रदर्शितः) यहाँ नहीं है।"),
    "hook": "निज और आगन्तु विकार — और उत्पन्न हुओं की शान्ति के लिए।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "For what does this line say, regarding disorders that have already arisen?",
            ("For their pacification",
             "उत्पन्नानां च शान्तये: and for the pacification of those arisen."),
            [("For their increase", "The word is शान्तये, pacification."),
             ("For their naming", "The line says pacification."),
             ("For their diagnosis", "The line says pacification.")],
            "उत्पन्नानां are those that have arisen; शान्तये is 'for pacification'.",
            "उत्पन्नानां च शान्तये = for the pacification of those arisen."),
        order(1, "Put the parts of the line in the order of the verse.",
              ["निजागंतुविकाराणाम्", "उत्पन्नानाम्", "च", "शान्तये"],
              "The line runs निजागंतुविकाराणाम्, उत्पन्नानाम्, च, शान्तये.",
              "निजागंतुविकाराणाम् · उत्पन्नानाम् · च · शान्तये."),
        match(2, "Match each word to its meaning.",
              [["निज", "innate"], ["आगन्तु", "adventitious"], ["विकार", "disorder"], ["शान्ति", "pacification"]],
              "These four words make up the whole line.",
              "निज = innate; आगन्तु = adventitious; विकार = disorder; शान्ति = pacification.",
              role="extend",
              teaches="निज (innate) and आगन्तु (adventitious) are the two kinds of disorder the line names; शान्ति is the aim for those that have arisen."),
        mcq("discriminate", 3, "Which is the right split of निजागंतुविकाराणां?",
            ("निज + आगंतु + विकाराणां",
             "अ + आ joins as आ: निज + आगंतु = निजागंतु."),
            [("निजा + गंतु + विकाराणां", "गंतु alone is not the word on the card."),
             ("निजाग + तुविकाराणां", "Neither part is a word."),
             ("निजः + आगंतु + विकाराणां", "A visarga would not vanish like this.")],
            "निज (innate) + आगंतु (adventitious) + विकाराणां (of disorders) join into one word.",
            "अ + आ → आ: निज + आगंतु = निजागंतु."),
        fill(4, "The word for 'for pacification' is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("शान्तये"),
             "शान्तये is the dative singular of शान्ति: 'for pacification'.",
             "शान्तये ends the line and gives the purpose.",
             "शान्तये = for pacification.", role="apply"),
        mcq("transfer", 5, "By the pattern of शान्तये, what does the invented word शुद्धये mean?",
            ("For purification",
             "The dative singular of a word in -इ ends in -अये and says 'for'."),
            [("By purification", "'By' would be शुद्ध्या."),
             ("In purification", "'In' would be शुद्धौ."),
             ("Purification as the subject", "The subject would be शुद्धिः.")],
            "शान्तये is the dative of शान्ति; शुद्धये is the dative of शुद्धि.",
            "-इ word, dative singular -अये = for.",
            teaches="A feminine word in -इ can take the dative singular in -अये: शान्ति → शान्तये, 'for pacification'; शुद्धि → शुद्धये, 'for purification'."),
    ],
}

# ---------------------------------------------------------------- unit 44
AUTHORED["44"] = {
    "title": "शीतोद्भवं दोषचयं",
    "question": "Which accumulations are purified and what does the person never incur?",
    "rule": ("One who purifies the doṣa accumulation born of winter in spring, "
             "that born of summer, and that of the rainy season at the passing "
             "of the clouds, never incurs seasonal diseases."),
    "limits": ("The scan read अकाले for the time of the summer-born "
               "accumulation; अभ्रकाले ('in the time of clouds') is an editor's "
               "change, so no question rests on that time. 'Passing of the "
               "clouds' is not named as any one season. The verse names no "
               "means of purifying."),
    "explain_hi": ("यह उपजाति छंद का श्लोक है। जो वसन्त में शीत से उत्पन्न दोष-संचय का शोधन करता है, "
                   "और ग्रीष्म से उत्पन्न संचय का भी, तथा मेघों के जाने (घनात्यय) पर वर्षा-ऋतु के संचय का, "
                   "‘शीघ्र और सम्यक्’ — वह ऋतुओं से उत्पन्न रोगों को कभी नहीं पाता। "
                   "ग्रीष्मज संचय के समय का शब्द (अभ्रकाले) छपाई में संपादित है, इसलिए उस पर प्रश्न नहीं बना। "
                   "‘रोगानृतुजान्न’ में रोगान् + ऋतुजान् + न है।"),
    "hook": "वसन्त में शीतज संचय · ग्रीष्मज संचय · घनात्यय पर वार्षिक संचय — शोधन; ऋतुज रोग कभी नहीं।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "Which accumulation does the verse say is purified in spring?",
            ("The doṣa accumulation born of winter",
             "शीतोद्भवं दोषचयं वसंते विशोधयन्."),
            [("The doṣa accumulation of the rainy season", "That one is purified at the passing of the clouds."),
             ("The accumulation of poison in a wound", "Nothing like this is in the verse."),
             ("The accumulation of old age", "Nothing like this is in the verse.")],
            "In spring, the accumulation of doṣa born of winter is purified.",
            "वसंते = in spring; शीतोद्भवं दोषचयं = the winter-born doṣa accumulation."),
        order(1, "Put the three accumulations purified in the verse in the order of the verse.",
              ["शीतोद्भव", "ग्रीष्मज", "वार्षिक"],
              "The verse runs: born of winter, born of summer, then that of the rainy season.",
              "शीतोद्भव · ग्रीष्मज · वार्षिक."),
        match(2, "Match each word to its meaning.",
              [["वसंते", "in spring"], ["घनात्यये", "at the passing of the clouds"],
               ["आशु", "quickly"], ["सम्यक्", "properly"]],
              "These four words say when and how the purifying is done.",
              "वसंते = in spring; घनात्यये = at the passing of the clouds; आशु = quickly; सम्यक् = properly.",
              role="extend",
              teaches="घनात्यये is घन (cloud) + अत्यये (at the passing): a locative that says 'when'."),
        mcq("discriminate", 3, "Which is the right split of रोगानृतुजान्न?",
            ("रोगान् + ऋतुजान् + न",
             "Final न् stays before a vowel and joins it; ऋतुजान् + न joins as ऋतुजान्न."),
            [("रोगाः + ऋतुजान् + न", "A visarga before ऋ would give रोगा ऋ..., not रोगान्."),
             ("रोग + आनृतुजान् + न", "आनृतुजान् is not a word."),
             ("रोगान् + तुजान् + न", "तुजान् is not a word.")],
            "रोगान् (diseases) + ऋतुजान् (born of seasons) + न (not) join as रोगानृतुजान्न.",
            "Final न् + vowel stay joined: रोगान् + ऋतुजान् = रोगानृतुजान्."),
        mcq("apply", 4, "What does the verse say the one who purifies in this way does not incur?",
            ("Diseases born of the seasons",
             "रोगानृतुजान्न जातु: never the diseases born of seasons."),
            [("Diseases born of wounds", "Wounds are not named in this verse."),
             ("Diseases born of fear", "Fear is not named in this verse."),
             ("Diseases born of poison", "Poison is not named in this verse.")],
            "प्राप्नोति रोगानृतुजान्न जातु = he never incurs the diseases born of seasons.",
            "ऋतुजान् रोगान् न जातु = never the season-born diseases."),
        mcq("transfer", 5, "By the pattern of ग्रीष्मजम्, what does the invented phrase मेघजं जलम् mean?",
            ("Water born of the cloud",
             "-ज at the end means 'born of' the first part."),
            [("A cloud born of water", "That would be जलजो मेघः, the order reversed."),
             ("Water that fills the cloud", "-ज says 'born of', not 'filling'."),
             ("Water going to the cloud", "Nothing in -ज says 'going to'.")],
            "ग्रीष्मज = born of summer, शीतोद्भव = born of winter, ऋतुज = born of seasons; मेघज = born of the cloud.",
            "X-ज = born of X.",
            teaches="A compound ending in -ज (or -उद्भव) means 'born of' the first part: ग्रीष्मज = born of summer; ऋतुज = born of seasons; मेघज = born of the cloud."),
    ],
}

# ---------------------------------------------------------------- unit 45
AUTHORED["45"] = {
    "title": "नित्यं हिताहारविहारसेवी",
    "question": "What is the person like, and what does he become?",
    "rule": ("One who constantly follows wholesome food and conduct, acts after "
             "consideration, is unattached to sense-objects, is generous, "
             "even-minded, devoted to truth, forbearing and attends upon "
             "trustworthy persons becomes free from disease."),
    "limits": ("दातासमः is read 'dātā samaḥ' (generous, even-minded); 'dātā "
               "asamaḥ' is possible, so no question uses that item. The verse "
               "states the result in its own words and no more."),
    "explain_hi": ("यह उपजाति का श्लोक एक व्यक्ति के गुण गिनाकर परिणाम बताता है। जो नित्य हित आहार-विहार का सेवन करता है, "
                   "विचारकर कार्य करता है, विषयों में अनासक्त है, दाता और सम है, सत्यपरायण, क्षमावान् और "
                   "आप्त (विश्वसनीय) जनों की सेवा करने वाला है — वह ‘अरोग’ (रोगरहित) होता है। "
                   "‘दातासमः’ को ‘दाता सम’ पढ़ा गया है; ‘दाता असम’ भी संभव है, इसलिए उस पर प्रश्न नहीं बना। "
                   "‘आप्तोपसेवी’ में आप्त + उपसेवी है।"),
    "hook": "हित आहार-विहार, विचारकर कर्म, अनासक्ति, सत्य, क्षमा, आप्त-सेवा — ऐसा मनुष्य अरोग होता है।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "What does the verse say the person with these habits becomes?",
            ("Free from disease (अरोग)",
             "भवत्यरोगः closes the verse."),
            [("Free from debt", "Debt is not mentioned."),
             ("Famous among kings", "Fame is not mentioned."),
             ("Learned in every text", "Learning is not mentioned.")],
            "The last words are भवत्यरोगः: he becomes free from disease.",
            "भवति अरोगः = becomes free from disease."),
        order(1, "Put these habits in the order of the verse (leaving out दातासमः).",
              ["हिताहारविहारसेवी", "समीक्ष्यकारी", "विषयेष्वसक्तः", "सत्यपरः", "क्षमावान्", "आप्तोपसेवी"],
              "The verse runs: follower of wholesome food and conduct, acts after consideration, unattached, devoted to truth, forbearing, attends upon the trustworthy.",
              "हिताहारविहारसेवी · समीक्ष्यकारी · विषयेष्वसक्तः · सत्यपरः · क्षमावान् · आप्तोपसेवी."),
        mcq("extend", 2, "Which is the right split of विषयेष्वसक्तः?",
            ("विषयेषु + असक्तः",
             "A final उ before a different vowel becomes व्: विषयेषु + अ = विषयेष्वसक्तः."),
            [("विषयेषो + असक्तः", "ओ + अ would give विषयेषोऽसक्तः."),
             ("विषयेष + वसक्तः", "वसक्तः is not a word."),
             ("विषयेषु + सक्तः", "That would give विषयेषु सक्तः, 'attached', without the व.")],
            "विषयेषु (in sense-objects) + असक्तः (unattached); उ + अ became व् + अ.",
            "उ + different vowel → व् + vowel: विषयेषु + असक्तः.",
            teaches="A final उ before a different vowel becomes व् and the vowel joins it: विषयेषु + असक्तः = विषयेष्वसक्तः."),
        match(3, "Match each word to its meaning.",
              [["समीक्ष्यकारी", "acting after consideration"], ["असक्तः", "unattached"],
               ["सत्यपरः", "devoted to truth"], ["क्षमावान्", "forbearing"]],
              "These four words are four of the habits of the verse.",
              "समीक्ष्यकारी = acting after consideration; असक्तः = unattached; सत्यपरः = devoted to truth; क्षमावान् = forbearing.",
              role="discriminate"),
        multi("apply", 4, "Which of these does the verse say of the person?",
              [("He acts after consideration", "Right: समीक्ष्यकारी."),
               ("He is unattached to sense-objects", "Right: विषयेष्वसक्तः."),
               ("He attends upon trustworthy persons", "Right: आप्तोपसेवी."),
               ("He gives up all food", "The verse speaks of wholesome food, not of giving it up."),
               ("He avoids every companion", "The verse says he attends upon trustworthy persons.")],
              [0, 1, 2],
              "The first three are in the verse; the last two say the opposite of what it states.",
              "समीक्ष्यकारी · विषयेष्वसक्तः · आप्तोपसेवी."),
        mcq("transfer", 5, "By the pattern of आप्तोपसेवी, what does the invented गुरुसेवी mean?",
            ("One who attends upon a teacher",
             "-सेवी names one who follows or attends the first part."),
            [("One who is served by a teacher", "The teacher is the one attended, not the server."),
             ("One who leaves a teacher", "-सेवी does not mean leaving."),
             ("The teacher of one who serves", "-सेवी names the one who serves.")],
            "हिताहारविहारसेवी = one who follows wholesome food and conduct; आप्तोपसेवी = one who attends upon the trustworthy.",
            "X-सेवी = one who follows or attends X.",
            teaches="A compound ending in -सेवी names one who follows or attends the first part: हिताहारविहारसेवी; आप्तोपसेवी; गुरुसेवी."),
    ],
}

# ---------------------------------------------------------------- unit 46
AUTHORED["46"] = {
    "title": "अर्थेष्वलभ्येष्वकृतप्रयत्नं",
    "question": "Which words of line 1 can be read plainly?",
    "rule": ("Line 1 describes a person who makes no effort in unobtainable "
             "objects, always shows regard for those that have means, and "
             "(line 2) has conquered the senses. Only the words are tested."),
    "limits": ("Low confidence. The clause 'तत्कालयुक्तं यदि नास्ति दैव' is "
               "ambiguous (daiva for daivam, 'fate'?); no question rests on it "
               "or on the verse's claim about diseases. नोनुतपंति is "
               "unexplained. Questions test only plain words of line 1."),
    "explain_hi": ("इस श्लोक का पाठ अनिश्चित है (विश्वास: कम), इसलिए प्रश्न केवल पहली पंक्ति के साफ़ शब्दों पर हैं। "
                   "पहली पंक्ति कहती है: ‘अलभ्य’ (न पाने योग्य) विषयों में जो प्रयत्न नहीं करता, और ‘उपायवत्’ "
                   "(उपाय वाले) विषयों में सदा आदर रखता है। दूसरी पंक्ति का ‘जितेन्द्रिय’ शब्द साफ़ है, पर ‘तत्कालयुक्तं ... दैव’ वाला "
                   "अंश दो तरह से पढ़ा जा सकता है और ‘दैव’ में अन्तिम अनुस्वार छूटा लगता है; इसलिए उस पर और रोगों वाले दावे पर कोई प्रश्न नहीं है।"),
    "hook": "न पाने योग्य में प्रयत्न नहीं, उपाय वालों में आदर, जितेन्द्रिय — (अंतिम अंश अस्पष्ट, परखा नहीं)।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "Which word of line 1 means 'unobtainable'?",
            ("अलभ्येषु",
             "अलभ्य = unobtainable (a-labhya)."),
            [("उपायवत्सु", "This means 'in those having means'."),
             ("कृतादरं", "This means 'showing regard'."),
             ("अर्थेषु", "This means 'in objects'.")],
            "अर्थेषु अलभ्येषु: in unobtainable objects.",
            "अलभ्य = unobtainable."),
        match(1, "Match each word to its meaning.",
              [["अलभ्य", "unobtainable"], ["अकृतप्रयत्न", "making no effort"],
               ["कृतादर", "showing regard"], ["जितेन्द्रिय", "one who has conquered the senses"]],
              "Two words come from line 1 and one from line 2; these are the plain compounds.",
              "अलभ्य = unobtainable; अकृतप्रयत्न = making no effort; कृतादर = showing regard; जितेन्द्रिय = one who has conquered the senses.",
              role="warmup"),
        order(2, "Put the three phrases of line 1 in the order of the verse.",
              ["अर्थेष्वलभ्येष्वकृतप्रयत्नम्", "कृतादरम्", "नित्यमुपायवत्सु"],
              "The line runs: in unobtainable objects making no effort, showing regard, always in those having means.",
              "अर्थेष्वलभ्येष्वकृतप्रयत्नम् · कृतादरम् · नित्यमुपायवत्सु.",
              role="extend",
              teaches="A line can be read in three phrases: the first with no effort, the second 'showing regard', the third 'always in those having means'."),
        mcq("discriminate", 3, "Which is the right split of अर्थेष्वलभ्येष्वकृतप्रयत्नं?",
            ("अर्थेषु + अलभ्येषु + अकृतप्रयत्नं",
             "A final उ before a different vowel becomes व्."),
            [("अर्थेष + वलभ्येष + वकृतप्रयत्नं", "वलभ्येष is not a word."),
             ("अर्थेषो + अलभ्येषो + अकृतप्रयत्नं", "ओ + अ would give ओऽ."),
             ("अर्थेषु + लभ्येषु + कृतप्रयत्नं", "That would drop the negating अ- and change the meaning.")],
            "अर्थेषु + अलभ्येषु + अकृतप्रयत्नं: उ + अ became व्, so the words are joined.",
            "उ + different vowel → व् + vowel."),
        multi("apply", 4, "Which words of line 1 begin with the negating अ-?",
              [("अलभ्येषु", "Right: a-labhya, unobtainable."),
               ("अकृतप्रयत्नं", "Right: a-kṛta-prayatna, effort not made."),
               ("कृतादरं", "कृत + आदर: the आ comes from joining, not from a negation."),
               ("उपायवत्सु", "It begins with उ, not a negation.")],
              [0, 1],
              "Only अलभ्येषु and अकृतप्रयत्नं carry the negating अ-.",
              "अ- negates: अलभ्य, अकृत-."),
        mcq("transfer", 5, "By the pattern of उपायवत्सु, what does the invented धनवत्सु mean?",
            ("Among (those) having wealth",
             "-वत् means 'having' the first part."),
            [("Among (those) without wealth", "'Without' would use a negating अ-."),
             ("For the sake of wealth", "That would be a dative, धनाय."),
             ("From wealth", "That would be धनात्.")],
            "उपायवत्सु = in those having means (upāya); धनवत्सु = among those having wealth.",
            "X-वत् = having X.",
            teaches="A word in -वत् means 'having' the first part: उपायवत् = having means; धनवत् = having wealth."),
    ],
}

# ---------------------------------------------------------------- unit 47
AUTHORED["47"] = {
    "title": "कालोऽनुकूलो विषया मनोज्ञा",
    "question": "What are always for the happiness of the steadfast person?",
    "rule": ("A favourable time, agreeable sense-objects, righteous acts, and "
             "action followed by happiness; a controllable mind (sattva) and a "
             "clear intellect: these are always for the happiness of the steadfast."),
    "limits": ("क्रियाः कर्म may be read as two items or one phrase ('acts, "
               "action'); the question chunks them together. सत्त्व is taken "
               "as 'mind'; it can also be 'strength of mind'. The verse says no "
               "more than this about happiness."),
    "explain_hi": ("यह उपजाति का श्लोक सुख के साधनों को गिनाकर ‘धीर’ (स्थिर बुद्धि वाले) के लिए उन्हें ‘सदा सुख के लिए’ "
                   "कहता है। पहली पंक्ति में अनुकूल काल, मन को भाने वाले विषय, धर्म्य क्रियाएँ और सुखानुबंधि "
                   "कर्म हैं। दूसरी पंक्ति में वश में रहने वाला सत्त्व और निर्मल बुद्धि है। ‘विषया’ और ‘मनोज्ञा’ में "
                   "अंत का विसर्ग घोष व्यंजन से पहले छूटा है: विषयाः, मनोज्ञाः — यह वर्तनी की भूल नहीं है। "
                   "‘भवंति’ बहुवचन में सबके साथ जुड़ता है।"),
    "hook": "अनुकूल काल, मनोज्ञ विषय, धर्म्य क्रिया, सुखानुबंधि कर्म, विधेय सत्त्व, विशद बुद्धि — धीर के लिए सदा सुख।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "For whom does the verse say these are for happiness?",
            ("For the steadfast person (धीर)",
             "धीरस्य सदासुखाय names the steadfast person."),
            [("For the king alone", "No king is mentioned."),
             ("For the physician alone", "No physician is mentioned."),
             ("For the student alone", "No student is mentioned.")],
            "भवंति धीरस्य सदासुखाय = they are always for the happiness of the steadfast person.",
            "धीरस्य सदा सुखाय = for the steadfast, always for happiness."),
        order(1, "Put these items in the order of the verse.",
              ["कालोऽनुकूलः", "विषया मनोज्ञाः", "धर्म्याः क्रियाः कर्म सुखानुबंधि", "सत्त्वं विधेयम्", "विशदा च बुद्धिः"],
              "The verse runs: favourable time, agreeable sense-objects, righteous acts and happy action, controllable mind, clear intellect.",
              "कालः · विषयाः · क्रिया-कर्म · सत्त्वं · बुद्धिः."),
        match(2, "Match each word to its meaning.",
              [["अनुकूल", "favourable"], ["मनोज्ञ", "agreeable"], ["विधेय", "controllable"], ["विशद", "clear"]],
              "These four words describe time, objects, mind and intellect.",
              "अनुकूल = favourable; मनोज्ञ = agreeable; विधेय = controllable; विशद = clear.",
              role="extend",
              teaches="Each item of the verse gets one describing word: time is अनुकूल, objects मनोज्ञ, mind विधेय, intellect विशद."),
        mcq("discriminate", 3, "The printed word विषया ends in -आ. What is the full form?",
            ("विषयाः, with the visarga dropped before a voiced sound",
             "A trailing -आ can be -आः with the visarga dropped before a voiced consonant."),
            [("विषयः, a single object", "One object would be विषयः, not विषया."),
             ("विषयाम्, 'object' as the one acted on", "The verb भवंति is plural and needs a plural subject."),
             ("विषये, 'in the object'", "This would end in -ए, not -आ.")],
            "विषयाः मनोज्ञाः: sense-objects, agreeable; the next word starts with the voiced म.",
            "-आ for -आः before a voiced sound: not a typo."),
        multi("apply", 4, "Which of these does the verse list as being for the steadfast person's happiness?",
              [("a controllable mind (सत्त्व)", "Right: सत्त्वं विधेयम्."),
               ("a clear intellect (बुद्धि)", "Right: विशदा च बुद्धिः."),
               ("a favourable time", "Right: कालोऽनुकूलः."),
               ("unrestrained senses", "Not in the verse."),
               ("great wealth", "Not in the verse.")],
              [0, 1, 2],
              "A controllable mind, a clear intellect and a favourable time are listed; unrestrained senses and great wealth are not.",
              "कालः · विषयाः · क्रियाः · कर्म · सत्त्वं · बुद्धिः."),
        mcq("transfer", 5, "By the pattern of सुखानुबंधि, what does the invented लाभानुबंधि कर्म mean?",
            ("Action followed by gain",
             "-अनुबंधि at the end means 'followed by' the first part."),
            [("Action without gain", "'Without' would use a negating अ-."),
             ("Action that follows gain", "The first part is what follows the action, not what comes first."),
             ("Gain born of action", "The word is built on 'followed by', not 'born of'.")],
            "सुखानुबंधि कर्म = action followed by happiness; लाभानुबंधि कर्म = action followed by gain.",
            "X-अनुबंधि = followed by X.",
            teaches="A compound ending in -अनुबंधि means 'followed by' the first part: सुखानुबंधि = followed by happiness; लाभानुबंधि = followed by gain."),
    ],
}

# ---------------------------------------------------------------- unit 48
AUTHORED["48"] = {
    "title": "इति रोगानुत्पादनीयो नाम",
    "question": "What does the closing line say?",
    "rule": ("'Thus the fifth chapter, named Rogānutpādanīya.' A prose closing "
             "line; the numeral 5 after it is the chapter number."),
    "limits": ("A prose colophon, not a verse. The title means the chapter on "
               "diseases not to be allowed to arise; the line says nothing "
               "about the contents."),
    "explain_hi": ("यह अध्याय की समाप्ति की गद्य पंक्ति है: ‘इति रोगानुत्पादनीयो नाम पंचमोऽध्यायः’, अर्थात् "
                   "इस प्रकार रोगानुत्पादनीय नामक पाँचवाँ अध्याय। ‘इति’ का अर्थ ‘इस प्रकार’ है, ‘नाम’ का ‘नाम से’, "
                   "‘पंचम’ का ‘पाँचवाँ’। अंत की ‘५’ अध्याय की संख्या है। "
                   "छपाई में ‘पंचमो ऽध्यायः’ के बीच खाली स्थान है; वह ‘पंचमः अध्यायः’ का संधि-रूप है।"),
    "hook": "इति — रोगानुत्पादनीय नाम — पाँचवाँ अध्याय समाप्त।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What is the name of the fifth chapter, as this closing line gives it?",
            ("Rogānutpādanīya",
             "रोगानुत्पादनीयो नाम पंचमोऽध्यायः."),
            [("Dinacaryā", "That is the name of chapter 3."),
             ("Ṛtucaryā", "That is the name of chapter 4."),
             ("Śiṣyopanayanīya", "That is the name of chapter 2.")],
            "The line names the chapter रोगानुत्पादनीय.",
            "इति रोगानुत्पादनीयो नाम पंचमोऽध्यायः."),
        order(1, "Put the words of the closing line in the order of the line.",
              ["इति", "रोगानुत्पादनीयः", "नाम", "पंचमः", "अध्यायः"],
              "The line runs इति, रोगानुत्पादनीयः, नाम, पंचमः, अध्यायः.",
              "इति · रोगानुत्पादनीयः · नाम · पंचमः · अध्यायः."),
        match(2, "Match each word to its meaning.",
              [["इति", "thus"], ["नाम", "by name"], ["पंचम", "fifth"]],
              "These three words are the frame of the closing line.",
              "इति = thus; नाम = by name; पंचम = fifth.",
              role="extend",
              teaches="A chapter's closing line follows a frame: इति + title + नाम + number + अध्यायः."),
        mcq("discriminate", 3, "Which is the right split of रोगानुत्पादनीयो नाम?",
            ("रोगानुत्पादनीयः + नाम",
             "अः before a voiced sound such as न becomes ओ."),
            [("रोगानुत्पादनीयम् + नाम", "म् before न would stay as म् or a dot, not ओ."),
             ("रोगानुत्पादनीयाः + नाम", "आः before a voiced sound drops to आ, not ओ."),
             ("रोगानुत्पादनीये + नाम", "ए stays ए, it does not become ओ.")],
            "The title word ends in -अः; before नाम it became -ओ.",
            "अः + voiced sound → ओ."),
        fill(4, "The word for 'chapter' in the closing line is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("अध्यायः"),
             "अध्यायः means chapter.",
             "अध्यायः ends the line.",
             "अध्यायः = chapter.", role="apply"),
        mcq("transfer", 5, "Following पंचमोऽध्यायः, how are षष्ठः (sixth) and अध्यायः joined?",
            ("षष्ठोऽध्यायः",
             "षष्ठः + अध्यायः: अः + अ becomes ओऽ."),
            [("षष्ठेऽध्यायः", "ए would be the locative, 'in the sixth chapter'."),
             ("षष्ठाध्यायः", "This joins as a compound and shows no visarga change."),
             ("षष्ठ अध्यायः", "The visarga before अ becomes ओऽ here, not a gap.")],
            "पंचमः + अध्यायः gives पंचमोऽध्यायः; षष्ठः + अध्यायः gives षष्ठोऽध्यायः.",
            "अः + अ → ओऽ.",
            teaches="The masculine ordinal ends in -अः; before अध्यायः it joins as ओऽ: पंचमोऽध्यायः, षष्ठोऽध्यायः."),
    ],
}

NOTES_HI = {
    "37": "विश्वास: मध्यम। यह तृतीया-वाक्यांश इकाई ३६ (आहारैः) से चला आता है; इस इकाई में क्रिया नहीं है। शालि और षष्टिक चावल के प्रकार हैं, नाम की तरह रखे गए। ‘हृद्य’ का शाब्दिक अर्थ ‘हृदय का’, यहाँ ‘प्रिय’। ‘रुचिपक्तिदैः’ को साधनों का विशेषण माना गया है। संधि जाँची: संयोगात् + रुचि → संयोगाद्रुचि (त् → द्); रुचि-पक्ति-दैः में -द ‘देने वाला’ है। पाठभेद या अनिश्चित अंश सूचीबद्ध नहीं है।",
    "38": "विश्वास: मध्यम। ‘साभ्यंग’ = स + अभ्यंग, ‘अभ्यंग के साथ’, पूरी सूची से जुड़ सकता है। ‘निरूहस्नेहबस्तिभिः’ को ‘निरूह और स्नेह बस्तियाँ’ पढ़ा गया है। ‘पावक’ का शाब्दिक अर्थ ‘अग्नि’, पुस्तक उसे पाचन-अग्नियाँ मानती है। संधि जाँची: स + अभ्यंग → साभ्यंग; अभ्यंग + उद्वर्तन → अभ्यंगोद्वर्तन (अ + उ → ओ)। वाक्य अगली इकाई में चलता है।",
    "39": "विश्वास: मध्यम। पहली पंक्ति इकाई ३८ के ‘लभते’ के शेष कर्म पूरा करती है; दूसरी पंक्ति ‘ये … संभवाः’ का वाक्यांश शुरू करती है जिसका संज्ञा-पद (गदाः) इकाई ४० में है। ‘भूत’ = प्राणी या आत्माएँ; ‘वायु’ यहाँ हवा। अनुवाद के अंत में ‘...’ है क्योंकि वाक्य अधूरा है। संधि जाँची: वर्ण + इन्द्रिय → वर्णेन्द्रिय (अ + इ → ए); दैर्घ्यम् + आयुषः → दैर्घ्यमायुषः; भूत-विष-वायु-अग्नि: वायु + अग्नि → वाय्वग्नि (उ → व्)।",
    "40": "विश्वास: मध्यम। ‘कामक्रोधभयाद्याः’ = ‘काम, क्रोध, भय जिनके आदि में हैं’। छपा ‘तेस्युर’ वस्तुतः ‘ते स्युः’ है। पहली पंक्ति इकाई ३९ के ‘ये’ वाक्यांश को पूरा करती है; दूसरी पंक्ति नई सूची शुरू करती है, क्रिया नहीं। ‘स्मृति’ का अर्थ सजगता भी हो सकता है। संधि जाँची: स्युः + आगंतवः → स्युरागंतवः (विसर्ग → र्); आगंतवः + गदाः → आगंतवो गदाः; भय + आद्याः → भयाद्याः।",
    "41": "विश्वास: मध्यम। पाठ-चिह्न: छपा ‘सवृत्तस्यानुवर्त्तनं’ में ‘सद्वृत्त’ अपेक्षित है (‘द्’ छूटा लगता है, छंद अपरिवर्तित); यह अनुमान है, इसलिए उस अंश पर प्रश्न नहीं। ‘आत्मविज्ञान’ का अर्थ ‘स्व का ज्ञान’ भी हो सकता है। ‘ग्रह’ को ग्रह ही रखा गया है (तारे या पकड़ने वाली शक्ति)। सूची में क्रिया नहीं है। संधि जाँची: देश-काल-आत्म-विज्ञान में काल + आत्म → कालात्म; ग्रह + अर्चन → ग्रहार्चन।",
    "42": "विश्वास: उच्च। ‘अनुत्पत्त्यै’ का कर्म-पद (निजागंतुविकाराणाम्) इकाई ४३ में है। ‘पृथक्पृथक्’ द्वित्व से ‘अलग-अलग’। ‘निर्दिष्ट’ और ‘प्रदर्शित’ भूतकालिक कृदंत हैं। संधि जाँची: विधिः + एषः → विधिरेषः; भूत-आदि-अस्पर्शन-उपायः → भूताद्यस्पर्शनोपायः (इ + अ → य्; अ + उ → ओ); निर्दिष्टः + च → निर्दिष्टश्च। यह इकाई ४२ का दूसरा आधा और ४३ मिलकर एक श्लोक है।",
    "43": "विश्वास: उच्च। यह अकेली पंक्ति है; ‘अनुत्पत्त्यै … विधिरेषः प्रदर्शितः’ (इकाई ४२) इसे पूरा करता है। निज + आगन्तु + विकाराणाम् का समास द्वंद्व-फिर-तत्पुरुष है। ‘उत्पन्नानाम्’ षष्ठी बहुवचन है। संधि जाँची: निज + आगंतु → निजागंतु (अ + आ → आ); उत्पन्नानाम् + च → उत्पन्नानां च (अनुस्वार)।",
    "44": "विश्वास: मध्यम। पाठ-चिह्न: ‘ग्रीष्मजमभ्रकाले’ में स्कैन ‘अकाले’ पढ़ता था; ‘अभ्र-’ ऊपरी संपादकीय परिवर्तन है (छंद ४४ में २२ अक्षर इसी से पूरे होते हैं); अंग्रेज़ी का ‘(the rains)’ इसी पर टिका है, इसलिए ग्रीष्मज संचय के शोधन के काल पर प्रश्न नहीं बना। ‘घनात्यये’ = मेघों के जाने पर; ऋतु का नाम श्लोक में नहीं है। कर्ता (विशोधयन्) ऊपर से जोड़ा गया है। उपजाति, २२ अक्षर। संधि जाँची: रोगान् + ऋतुजान् + न → रोगानृतुजान्न।",
    "45": "विश्वास: उच्च। ‘दातासमः’ को ‘दाता समः’ पढ़ा गया है; ‘दाता असमः’ (अतुल्य दाता) व्याकरण से संभव है, इसलिए उस पर प्रश्न नहीं। ‘विहार’ = सामान्य आचरण; ‘आप्त’ = विश्वसनीय जन। उपजाति, २२ अक्षर। संधि जाँची: विषयेषु + असक्तः → विषयेष्वसक्तः (उ → व्); आप्त + उपसेवी → आप्तोपसेवी (अ + उ → ओ); क्षमावान् + आप्त → क्षमावानाप्तो…।",
    "46": "विश्वास: कम। ‘तत्कालयुक्तं यदि नास्ति दैव’ अस्पष्ट है: ‘दैव’ में अनुस्वार छूटा लगता है (‘दैवम्’ अपेक्षित, सुझाव), और ‘उस समय से जुड़ा’ दो तरह से पढ़ा जा सकता है; पुस्तक इसे प्रतिकूल भाग्य मानती है। इसलिए इस अंश पर और रोगों के दावे पर कोई प्रश्न नहीं बना; प्रश्न केवल साफ़ शब्दों पर हैं। छपा ‘नोनुतपंति’ (न + अनुतपंति) की संधि सामान्य नियम से नहीं बैठती; इसलिए उस पर प्रश्न नहीं। ‘उपायवत्सु’ = उपाय वालों में। उपजाति, २२ अक्षर। संधि जाँची: विषयेषु-रूप अर्थेषु + अलभ्येषु → अर्थेष्वलभ्येषु (उ/उ → व्)।",
    "47": "विश्वास: उच्च। ‘विषया’ और ‘मनोज्ञा’ विसर्ग-रहित रूप हैं (विषयाः, मनोज्ञाः); यह वर्तनी की भूल नहीं है। ‘क्रियाः कर्म’ को दो पद या एक वाक्यांश दोनों पढ़ा जा सकता है; यहाँ दो माना गया पर प्रश्न इन्हें साथ रखता है। ‘सत्त्व’ = मन (सत्त्व); ‘सत्त्व’ का अर्थ मन का बल भी हो सकता है। उपजाति, २२ अक्षर। संधि जाँची: कालः + अनुकूलः → कालोऽनुकूलः; सुख + अनुबंधि → सुखानुबंधि।",
    "48": "विश्वास: उच्च। गद्य समाप्ति-पंक्ति है। ‘रोगानुत्पादनीय’ = रोग + अनुत्पादनीय, ‘जिन रोगों को उत्पन्न नहीं होने देना है’; शीर्षक का अर्थ पुस्तक के अनुसार रोगों के न उत्पन्न होने पर अध्याय। अंत का ‘५’ अध्याय-संख्या है। संधि जाँची: रोगानुत्पादनीयः + नाम → रोगानुत्पादनीयो नाम; पंचमः + अध्यायः → पंचमोऽध्यायः (छपा ‘पंचमो ऽध्यायः’ में बीच का स्थान छपाई का है)।",
}

AIDS = {
    "37": {
        "diagram": {"groups": [
            {"label": "पंक्ति १: इन द्रव्यों से",
             "items": ["शालि", "षष्टिक", "गोधूम", "मुद्ग", "मांस", "घृत", "आदि"]},
            {"label": "पंक्ति २: साधन",
             "items": ["हृद्य-दीपन भैषज्य का संयोग", "रुचि और पाचन देने वाले"]}]},
        "chunks": "शालिषष्टिकगोधूम | मुद्गमांसघृतादिभिः ‖ हृद्यदीपनभैषज्य | संयोगाद्रुचिपक्तिदैः।",
        "sandhi": "त् + घोष → द्: संयोगात् + रुचि → संयोगाद्रुचि। घृत + आदिभिः → घृतादिभिः (अ + आ → आ)।",
        "anchors": "शालि, षष्टिक = चावल के नाम · गोधूम = गेहूँ · मुद्ग = मूँग · घृत = घी · रुचि = स्वाद की इच्छा · पक्ति = पाचन · -द = देने वाला।",
    },
    "38": {
        "diagram": {"steps": ["साधन: अभ्यंग सहित उद्वर्तन, स्नान, निरूह, स्नेह, बस्ति", "वह प्राप्त करता है (लभते)", "फल: शर्म और सब अग्नियों की तीक्ष्णता"]},
        "chunks": "साभ्यंगोद्वर्तन | स्नाननिरूहस्नेहबस्तिभिः ‖ तथा स लभते शर्म | सर्वपावकपाटवं।",
        "sandhi": "अ + अ → आ: स + अभ्यंग → साभ्यंग। अ + उ → ओ: अभ्यंग + उद्वर्तन → अभ्यंगोद्वर्तन।",
        "anchors": "स- = के साथ · अभ्यंग = तेल-मालिश · उद्वर्तन = उबटन-मलना · शर्म = सुख · पाटव = तीक्ष्णता · पावक = अग्नि।",
    },
    "39": {
        "diagram": {"groups": [
            {"label": "पंक्ति १: प्राप्त (इकाई ३८ से जुड़ा)",
             "items": ["बुद्धि-वर्ण-इन्द्रिय की निर्मलता", "वृषता", "आयु की दीर्घता"]},
            {"label": "पंक्ति २: ‘ये’ — जो इनसे उपजें",
             "items": ["भूत", "विष", "वायु", "अग्नि", "क्षत", "भंग", "आदि"]}]},
        "chunks": "धीवर्णेंद्रियवैमल्यं | वृषतां दैर्घ्यमायुषः ‖ ये भूतविषवाय्वग्नि | क्षतभंगादिसंभवाः।",
        "sandhi": "अ + इ → ए: वर्ण + इन्द्रिय → वर्णेन्द्रिय। उ + अ → व्: वायु + अग्नि → वाय्वग्नि।",
        "frame": "पंक्ति १: ‘लभते’ के बाकी कर्म · पंक्ति २: ‘ये … संभवाः’ — संज्ञा अगली इकाई में।",
    },
    "40": {
        "diagram": {"groups": [
            {"label": "जिनसे उपजे",
             "items": ["काम", "क्रोध", "भय", "आदि"]},
            {"label": "वे कहलाते हैं",
             "items": ["आगन्तु गद"]}]},
        "chunks": "कामक्रोधभयाद्याश्च | तेस्युरागंतवो गदाः ‖ त्यागः प्रज्ञापराधानां | इंद्रियोपशमः स्मृतिः।",
        "sandhi": "उः + स्वर → उर्: स्युः + आगंतवः → स्युरागंतवः। अः + घोष → ओ: आगंतवः + गदाः → आगंतवो गदाः।",
        "anchors": "आगन्तु = बाहर से आने वाला · गद = रोग · प्रज्ञापराध = बुद्धि की भूल · उपशम = शमन · स्मृति = याद।",
    },
    "41": {
        "chunks": "देशकालात्मविज्ञानं | सवृत्तस्यानुवर्त्तनं (अंतिम शब्द क्षतिग्रस्त) ‖ अथर्वविहिता शांतिः | प्रतिकूलग्रहार्चनं।",
        "sandhi": "अ + आ → आ: काल + आत्म → कालात्म। अ + अ → आ: ग्रह + अर्चन → ग्रहार्चन।",
        "anchors": "विहित = विधान किया गया · शान्ति = शान्ति कर्म · प्रतिकूल = विपरीत · अर्चन = पूजा।",
    },
    "42": {
        "chunks": "भूताद्यस्पर्शनोपायो | निर्दिष्टश्च पृथक्पृथक् ‖ अनुत्पत्त्यै समासेन | विधिरेषः प्रदर्शितः।",
        "sandhi": "इः + स्वर → इर्: विधिः + एषः → विधिरेषः। इ + अ → य्: भूत + आदि + अस्पर्शन → भूताद्यस्पर्शन।",
        "frame": "पंक्ति १: उपाय अलग-अलग बताया · पंक्ति २: अनुत्पत्ति के लिए यह विधि संक्षेप में।",
        "anchors": "पृथक् = अलग · समास = संक्षेप · अनुत्पत्ति = उत्पन्न न होना · प्रदर्शित = दिखाया गया।",
    },
    "43": {
        "chunks": "निजागंतुविकाराणा- | मुत्पन्नानां च शांतये।",
        "sandhi": "अ + आ → आ: निज + आगंतु → निजागंतु। म् → अनुस्वार: उत्पन्नानाम् + च → उत्पन्नानां च।",
        "anchors": "निज = सहज · आगन्तु = बाहर से आने वाला · विकार = रोग, विकृति · शान्तये = शान्ति के लिए (चतुर्थी)।",
        "frame": "इकाई ४२ का शेष: अनुत्पत्त्यै (निज-आगन्तु के लिए) · शान्तये (उत्पन्नों के लिए)।",
    },
    "44": {
        "diagram": {"groups": [
            {"label": "संचय",
             "items": ["शीतोद्भव", "ग्रीष्मज", "वार्षिक"]},
            {"label": "शोधन का काल",
             "items": ["वसन्त", "अभ्रकाल (संपादित पाठ)", "घनात्यय"]}]},
        "chunks": "शीतोद्भवं दोषचयं वसंते | विशोधयन् ग्रीष्मजमभ्रकाले ‖ घनात्यये वार्षिकमाशु सम्यक् | प्राप्नोति रोगानृतुजान्न जातु।",
        "sandhi": "न् + स्वर साथ: रोगान् + ऋतुजान् → रोगानृतुजान्। ‘ान् + न’: ऋतुजान् + न → ऋतुजान्न।",
        "frame": "क्या: तीन संचय · कब: वसन्त, (अभ्रकाल), घनात्यय · कैसे: शीघ्र और सम्यक् · फल: ऋतुज रोग कभी नहीं।",
    },
    "45": {
        "diagram": {"groups": [
            {"label": "गुण (श्लोक के क्रम में)",
             "items": ["हित आहार-विहार", "विचारकर कार्य", "विषयों में अनासक्त", "दाता, सम", "सत्यपरायण", "क्षमावान्", "आप्त-सेवी"]},
            {"label": "फल",
             "items": ["अरोग होता है"]}]},
        "chunks": "नित्यं हिताहारविहारसेवी | समीक्ष्यकारी विषयेष्वसक्तः ‖ दातासमः सत्यपरः | क्षमावानाप्तोपसेवी च भवत्यरोगः।",
        "sandhi": "उ + अ → व्: विषयेषु + असक्तः → विषयेष्वसक्तः। अ + उ → ओ: आप्त + उपसेवी → आप्तोपसेवी।",
        "anchors": "-सेवी = सेवन करने वाला · -कारी = करने वाला · आप्त = विश्वसनीय · समीक्ष्य = विचारकर · अरोग = नीरोग।",
    },
    "46": {
        "chunks": "अर्थेष्वलभ्येष्वकृतप्रयत्नं | कृतादरं नित्यमुपायवत्सु ‖ (दूसरी पंक्ति का अंत अस्पष्ट, यहाँ नहीं दिया)",
        "sandhi": "उ + अ → व्: अर्थेषु + अलभ्येषु → अर्थेष्वलभ्येषु; अलभ्येषु + अकृत → अलभ्येष्वकृत।",
        "anchors": "अलभ्य = न पाने योग्य · अकृतप्रयत्न = जिसने प्रयत्न नहीं किया · कृतादर = आदर रखने वाला · उपायवत् = उपाय वाला · जितेन्द्रिय = इन्द्रियों को जीतने वाला।",
    },
    "47": {
        "diagram": {"groups": [
            {"label": "पंक्ति १",
             "items": ["अनुकूल काल", "मनोज्ञ विषय", "धर्म्य क्रियाएँ", "सुखानुबंधि कर्म"]},
            {"label": "पंक्ति २",
             "items": ["विधेय सत्त्व", "विशद बुद्धि", "धीर के लिए सदा सुख"]}]},
        "chunks": "कालोऽनुकूलो विषया मनोज्ञा | धर्म्याः क्रियाः कर्म सुखानुबंधि ‖ सत्त्वं विधेयं विशदा च बुद्धिः | भवंति धीरस्य सदासुखाय।",
        "sandhi": "अः + अ → ओऽ: कालः + अनुकूलः → कालोऽनुकूलः। विसर्ग-रहित: विषया = विषयाः, मनोज्ञा = मनोज्ञाः (घोष से पहले)।",
        "anchors": "अनुकूल = हितकर · मनोज्ञ = मन को भाने वाला · विधेय = वश में रहने वाला · विशद = निर्मल · धीर = स्थिरबुद्धि।",
    },
    "48": {
        "chunks": "इति रोगानुत्पादनीयो नाम | पंचमोऽध्यायः ॥ ५ ॥",
        "sandhi": "अः + घोष → ओ: रोगानुत्पादनीयः + नाम → रोगानुत्पादनीयो नाम। अः + अ → ओऽ: पंचमः + अध्यायः → पंचमोऽध्यायः।",
        "anchors": "इति = इस प्रकार · नाम = नाम से · पंचम = पाँचवाँ · अध्याय = अध्याय।",
    },
}

IMAGE_SPECS = {
    ("37", "diagram"): {
        "file": "ch5b04-means-37.svg",
        "alt": "Two columns: line 1 names shali, shashtika, wheat, mung, meat, ghee and the like; line 2 names combination with agreeable kindling medicinal substances and means that give relish and digestion",
        "type": "split",
        "title": "श्लोक ३७: द्रव्य और साधन",
        "cols": [["पंक्ति १: इन द्रव्यों से", ["शालि", "षष्टिक", "गोधूम", "मुद्ग", "मांस", "घृत", "आदि"]],
                 ["पंक्ति २: साधन", ["हृद्य-दीपन भैषज्य का संयोग", "रुचि-पाचन देने वाले"]]],
    },
    ("38", "diagram"): {
        "file": "ch5b04-means-result-38.svg",
        "alt": "Flowchart: by oil massage with rubbing, bathing, nirūha and sneha enemas, he obtains comfort and keenness of all the fires",
        "type": "mermaid",
        "code": ('flowchart TD\n  A["अभ्यंग सहित उद्वर्तन,<br/>स्नान, निरूह,<br/>स्नेह, बस्ति"] --> B["वह प्राप्त करता है"]\n'
                 '  B --> C["शर्म (सुख)"]\n  B --> D["सब अग्नियों की<br/>तीक्ष्णता"]\n'),
    },
    ("39", "diagram"): {
        "file": "ch5b04-sources-39.svg",
        "alt": "Mind map: those arising from bhuta, poison, wind, fire, wound, fracture and the like",
        "type": "mermaid",
        "code": ('mindmap\n  जो इनसे उत्पन्न\n    भूत\n    विष\n    वायु\n    अग्नि\n    क्षत\n    भंग\n    आदि\n'),
    },
    ("40", "diagram"): {
        "file": "ch5b04-agantu-40.svg",
        "alt": "Mind map: adventitious diseases from desire, anger, fear and the like",
        "type": "mermaid",
        "code": ('mindmap\n  आगन्तु गद\n    काम से\n    क्रोध से\n    भय से\n    आदि से\n'),
    },
    ("44", "diagram"): {
        "file": "ch5b04-accumulations-44.svg",
        "alt": "Table: winter-born accumulation in spring; summer-born accumulation in the time of clouds (an edited reading); rainy-season accumulation at the passing of the clouds",
        "type": "table",
        "title": "श्लोक ४४: संचय और शोधन का काल",
        "heads": ["संचय", "शोधन का काल"],
        "rows": [["शीतोद्भव दोषचय", "वसन्त"],
                 ["ग्रीष्मज", "अभ्रकाल (संपादित पाठ)"],
                 ["वार्षिक", "घनात्यय (मेघों के जाने पर)"]],
    },
    ("45", "diagram"): {
        "file": "ch5b04-arogah-45.svg",
        "alt": "Mind map: the person who follows wholesome food and conduct, acts after consideration, is unattached, generous and even-minded, devoted to truth, forbearing and attends the trustworthy becomes free from disease",
        "type": "mermaid",
        "code": ('mindmap\n  अरोग होता है\n    हित आहार-विहार\n    विचारकर कार्य\n    विषयों में अनासक्त\n'
                 '    दाता, सम\n    सत्यपरायण\n    क्षमावान्\n    आप्त-सेवी\n'),
    },
    ("47", "diagram"): {
        "file": "ch5b04-sukha-47.svg",
        "alt": "Mind map: for the steadfast person always for happiness: favourable time, agreeable objects, righteous acts, action followed by happiness, controllable mind, clear intellect",
        "type": "mermaid",
        "code": ('mindmap\n  धीर को सदा सुख\n    अनुकूल काल\n    मनोज्ञ विषय\n    धर्म्य क्रियाएँ\n'
                 '    सुखानुबंधि कर्म\n    विधेय सत्त्व\n    विशद बुद्धि\n'),
    },
}
