from helpers import mcq, match, order, fill, multi, accepts


def T(q, teaches):
    q["teaches"] = teaches
    return q


AUTHORED = {}

# ---------------------------------------------------------------- unit 51
AUTHORED["51"] = {
    "title": "अपिच",
    "question": "What do the two parts of the link अपिच (unit 51) mean, and why do they stay unchanged?",
    "rule": "अपि (also) + च (and) = 'and further': a stock link that opens a further statement. Before the consonant च, the इ of अपि stays.",
    "limits": ("Prose, one printed word, written without a space. It only links; the data takes the further statement "
               "to appear in unit 52, and no question rests on that link."),
    "explain_hi": ("यह एक शब्द की छोटी गद्य-पंक्ति है: ‘अपि च’, यानी और भी। "
                   "अपि (भी) और च (और) दोनों अव्यय हैं; छपाई में ये बिना जगह के लिखे गए हैं। "
                   "डेटा के अनुसार आगे की बात सम्भवतः इकाई ५२ में है। "
                   "च व्यंजन है, इसलिए अपि का इ यहाँ नहीं बदलता; स्वर से पहले वह य् बन जाता।"),
    "hook": "अपि च: एक बात और।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 51, what job does अपिच do?",
            ("It adds a further point", "अपि च = and further: it opens one more statement."),
            [("It closes the chapter", "A chapter close would be an इति formula; अपि च adds."),
             ("It asks a question now", "No question follows; the data reads अपि च here as 'and further'."),
             ("It denies the last line", "A denial would need न; अपि च adds.")],
            "अपि च = and further.",
            "अपि = also; च = and."),
        match(1, "Match each part of unit 51 to its meaning.",
              [["अपि", "also, too"], ["च", "and"], ["अपिच", "and further"]],
              "अपि = also; च = and; together: and further.",
              "अपि, च, अपिच."),
        T(multi("extend", 2, "Which statements about अपिच in unit 51 are right?",
                [("It is printed as one word", "Right: अपि and च stand without a space."),
                 ("It is a verb meaning goes", "No: अपि and च are indeclinables, not a verb."),
                 ("Its इ becomes य् before च", "No: च is a consonant, so the इ stays."),
                 ("Both its parts are indeclinables", "Right: अपि and च never change their form for case.")],
                [0, 3],
                "Two indeclinables printed together: अपि + च.",
                "अपिच = अपि + च."),
          "अपि and च are indeclinables (अव्यय): they take no case endings."),
        mcq("discriminate", 3, "Which split of the printed अपिच in unit 51 is right?",
            ("अपि + च", "Two indeclinables, written together without a space."),
            [("अप + इच", "Neither अप nor इच is the word here; the particle is अपि."),
             ("अपी + च", "अपी is not the particle; it is अपि with a short इ."),
             ("अ + पिच", "पिच is not a word; the words are अपि and च.")],
            "अपि (also) + च (and).",
            "अपिच = अपि + च."),
        mcq("apply", 4, "In the printed अपिच of unit 51, why is no sandhi change seen between अपि and च?",
            ("इ meets a consonant", "Vowel sandhi needs a vowel next; च is a consonant, so the इ stays."),
            [("च begins with a vowel", "च is a consonant, not a vowel."),
             ("अपि ends in a consonant", "अपि ends in the vowel इ."),
             ("Prose never has sandhi", "Prose has sandhi too, e.g. बलमपि in unit 53.")],
            "अपि + च: a consonant follows, so the इ stays.",
            "A final vowel stays before a consonant."),
        mcq("transfer", 5, "By the sense of च (and), what does रामः सीता च mean in a new example?",
            ("Rāma and Sītā", "च after the last word joins the two: Rāma and Sītā."),
            [("Rāma or Sītā", "'Or' would be वा; च means and."),
             ("Rāma, not Sītā", "'Not' would need न; च means and."),
             ("Rāma with Sītā's son", "No son is named; च simply joins Rāma and Sītā.")],
            "रामः सीता च = Rāma and Sītā.",
            "च = and, placed after the word it adds.",
            teaches="च (and) usually stands after the last word it joins: रामः सीता च, अपि च."),
    ],
}

# ---------------------------------------------------------------- unit 52
AUTHORED["52"] = {
    "title": "वर्षं वर्षं क्षयं याति",
    "question": "What do the sure words of unit 52 say about decay as each hundred passes, and what stays open?",
    "rule": ("For men (नृणाम्), each time a hundred has passed (याते शते शते), वर्षं वर्षं क्षयं याति: 'a year goes to "
             "decay' (or 'year after year it decays'). Line 2 names the measure (मानम्) of life accepted owing to "
             "abundance of merit (पुण्यबाहुल्यात्)."),
    "limits": ("Low confidence. Typed prose; the lines appear metrical (not asked). वर्षं वर्षं may be 'a year' or "
               "'year after year'; what decays and the hundred's unit are not stated. Line 2 is incomplete (यत् without "
               "तत्; आयुषो irregular): no question on its syntax, on what decays, or on वर्षम्'s case."),
    "explain_hi": ("इस इकाई में दो छपी पंक्तियाँ (०२.०८.६३ और ०२.०८.६४) साथ ली गई हैं; ये छन्दोबद्ध प्रतीत होती हैं, पर डेटा इन्हें गद्य रखता है। "
                   "मनुष्यों के लिए (नृणाम्), जब-जब सौ बीतते हैं (याते शते शते), ‘एक-एक वर्ष क्षय को जाता है’; दूसरा पठन ‘वर्ष-दर-वर्ष क्षय होता है’ भी सम्भव है। "
                   "किसका क्षय होता है और ‘सौ’ किसके सौ हैं, यह यहाँ नहीं कहा। "
                   "दूसरी पंक्ति में आयु का वह मान है जो पुण्य की अधिकता से (पुण्यबाहुल्यात्) माना जाता है (इष्यते); पर यह पंक्ति अधूरी है (‘यत्’ का ‘तत्’ नहीं), इसलिए इसकी वाक्य-रचना पर प्रश्न नहीं। "
                   "विश्वास कम है।"),
    "hook": "शते शते: दोहराया शब्द = हर एक।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 52, what does क्षय mean?",
            ("Decay, decline", "क्षय = wasting, decline: क्षयं याति = goes to decay."),
            [("Growth, increase", "Growth would be वृद्धि, the opposite of क्षय."),
             ("Birth, start", "Birth would be जन्म; क्षय is a decline."),
             ("Rest, sleep", "Sleep would be निद्रा; क्षय is a decline.")],
            "क्षय = decay.",
            "क्षय = decay, decline."),
        order(1, "Put the parts of line 1 of unit 52 in the printed order.",
              ["वर्षं वर्षं", "क्षयं याति", "नृणां", "याते शते शते"],
              "A year (or year after year); goes to decay; for men; each time a hundred has passed.",
              "वर्षं वर्षं → क्षयं याति → नृणां → याते शते शते."),
        match(2, "Match each word of line 1 of unit 52 to its meaning.",
              [["वर्ष", "year"], ["क्षय", "decay"], ["याति", "goes"], ["नृणाम्", "for men"], ["शत", "hundred"]],
              "वर्ष = year, क्षय = decay, याति = goes, नृणाम् = for men, शत = hundred.",
              "वर्ष, क्षय, याति, नृणाम्, शत.", role="extend",
              teaches="नृणाम् is the genitive plural of नृ (man); here it means 'for men'."),
        mcq("discriminate", 3, "Which statement about line 1 of unit 52 does the card support?",
            ("Decay comes as each hundred passes", "क्षयं याति ... याते शते शते: decay as each hundred has passed."),
            [("Growth comes as each hundred passes", "क्षयं याति is decay, not growth (वृद्धि)."),
             ("Decay comes before any hundred passes", "याते = has passed: the hundred is already gone."),
             ("Decay is said to come to the gods", "नृणाम् = for men, not for gods.")],
            "Line 1: for men, decay as each hundred has passed.",
            "Keep to what line 1 states."),
        mcq("apply", 4, "In unit 52, what does याते शते शते say?",
            ("When each hundred has passed", "याते = has passed; doubled शते = at each hundred."),
            [("Before a hundred has begun", "याते (has gone) marks a hundred already passed."),
             ("When a hundred is yet to come", "याते is a past participle: the hundred has passed."),
             ("Only after the first hundred", "The doubling शते शते means each hundred, not one.")],
            "याते शते शते = hundred by hundred having passed.",
            "Doubled word = each one in turn."),
        mcq("transfer", 5, "By the pattern of शते शते (at each hundred), what does दिने दिने mean in a new example?",
            ("Day by day, every day", "A doubled noun gives 'each, every': दिने दिने = on each day."),
            [("On two separate days only", "Two would need the dual (दिनयोः), not a doubling."),
             ("Before the day", "'Before' would need a word like पूर्वम्; the doubling means each."),
             ("Without any day", "'Without' would need विना; the doubling means each.")],
            "दिने दिने = every day, like शते शते = at each hundred.",
            "Doubled word = each, every.",
            teaches="A doubled word (शते शते) gives the sense 'each, every, one after another'."),
    ],
}

# ---------------------------------------------------------------- unit 53
AUTHORED["53"] = {
    "title": "बलमपि त्रिविधं भवति",
    "question": "By unit 53, what is said of strength (bala)?",
    "rule": "Strength (बल) also (अपि) is threefold (त्रिविधम्). The three kinds are named in unit 54.",
    "limits": ("Prose, one short sentence. अपि (also) adds bala to what was said before; with what it is compared is not "
               "stated here. The kinds come in unit 54; no question here rests on them."),
    "explain_hi": ("बल भी तीन प्रकार का होता है (बलमपि त्रिविधं भवति)। "
                   "‘अपि’ (भी) बल को पहले कही बातों से जोड़ता है; किससे, यह यहाँ नहीं कहा। "
                   "तीनों भेद अगली इकाई ५४ में गिनाए गए हैं। "
                   "सन्धि: बलम् + अपि → बलमपि (म् अगले स्वर से जुड़ता है); त्रिविधम् + भवति → त्रिविधं भवति (वाक्य में व्यंजन से पहले अन्तिम म् अनुस्वार लिखा जाता है)।"),
    "hook": "बल भी तीन तरह का।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 53, what does बल mean?",
            ("Strength", "बल = strength, power."),
            [("Measure, size", "Measure would be मान or प्रमाण."),
             ("Body", "Body would be देह or शरीर."),
             ("Season", "Season would be ऋतु.")],
            "बल = strength.",
            "बल = strength."),
        order(1, "Put the words of unit 53 in the printed order (sandhi undone).",
              ["बलम्", "अपि", "त्रिविधम्", "भवति"],
              "Strength; also; threefold; is.",
              "बलम् → अपि → त्रिविधम् → भवति."),
        match(2, "Match each word or part of unit 53 to its meaning.",
              [["बल", "strength"], ["अपि", "also"], ["त्रि", "three"], ["विध", "kind"], ["भवति", "is, becomes"]],
              "बल = strength, अपि = also, त्रि-विध = of three kinds, भवति = is.",
              "बल, अपि, त्रि, विध, भवति.", role="extend",
              teaches="त्रिविध is a bahuvrīhi, 'having three kinds': threefold."),
        mcq("discriminate", 3, "Which split of बलमपि in unit 53 is right?",
            ("बलम् + अपि", "म् joins the next vowel: बलम् + अपि → बलमपि."),
            [("बल + मपि", "मपि is not a word; the म् ends बलम्."),
             ("बलः + अपि", "अः + अ would give ओऽ: बलोऽपि, not the print."),
             ("बला + अपि", "आ + अ would give आ: बलापि, not the print.")],
            "बलम् (strength) + अपि (also).",
            "म् + vowel → म joined to the vowel."),
        mcq("apply", 4, "Why is त्रिविधम् printed त्रिविधं before भवति in unit 53?",
            ("Final म् + consonant → ं", "In a sentence, final म् before a consonant is written as anusvāra."),
            [("Final म् before a vowel → ं", "भ is a consonant; before a vowel म् would join it (बलमपि)."),
             ("ं is the neuter ending itself", "The neuter ending is -म्; ं is how it is written here."),
             ("भ makes the final म् drop", "The म् is not dropped; it is written ं.")],
            "त्रिविधम् + भवति → त्रिविधं भवति.",
            "Final म् + consonant → ं."),
        mcq("transfer", 5, "By the pattern of त्रिविधं भवति, how is बलम् + वर्धते (strength grows) written in a new sentence?",
            ("बलं वर्धते", "Final म् before a consonant is written ं: बलं वर्धते."),
            [("बलो वर्धते", "ओ comes from अः before a voiced consonant; बलम् has no visarga."),
             ("बलर्वर्धते", "र् comes from a visarga after a vowel other than अ/आ before a voiced sound; बलम् has म्, no visarga."),
             ("बला वर्धते", "आ has no source here; the म् is written ं.")],
            "बलम् + वर्धते = बलं वर्धते, like त्रिविधम् + भवति = त्रिविधं भवति.",
            "Final म् + consonant → ं.",
            teaches="Inside a sentence a final म् before a consonant is written as anusvāra: त्रिविधं भवति, बलं वर्धते."),
    ],
}

# ---------------------------------------------------------------- unit 54
AUTHORED["54"] = {
    "title": "सहजं कालकृतं युक्तिकृतं च",
    "question": "By unit 54, which are the three kinds of strength, in the printed order?",
    "rule": ("The three kinds of strength are innate (सहज), made by time (कालकृत) and made by method (युक्तिकृत). "
             "Units 55 and 56 explain them."),
    "limits": ("Verbless prose list; 'strength' is carried from unit 53, not printed. yukti = skilful application, "
               "method (data). The sub-kinds of method-made strength come in unit 56, where two are not firm."),
    "explain_hi": ("यह इकाई ५३ के तीन बल-भेद गिनाती है: सहज (जन्म के साथ आया), कालकृत (काल से बना) और युक्तिकृत (युक्ति, यानी कुशल प्रयोग, से बना)। "
                   "पंक्ति में क्रिया नहीं; ‘बल’ इकाई ५३ से आता है। "
                   "सहज और कालकृत का अर्थ इकाई ५५ में, युक्तिकृत का इकाई ५६ में खुलता है। "
                   "सहज = सह (साथ) + ज (उत्पन्न); ‘कृत’ = किया गया, बनाया गया।"),
    "hook": "जन्म से, समय से, युक्ति से: बल तीन।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In unit 54, what does सहज mean?",
            ("Born with one, innate", "सह (with) + ज (born): innate."),
            [("Gained later by effort", "That would be made by method (युक्तिकृत)."),
             ("Brought by the seasons", "That belongs to time-made strength (कालकृत)."),
             ("Lost with growing age", "सहज names what one is born with, not a loss.")],
            "सहज = innate.",
            "सह + ज = born with."),
        order(1, "Put the three kinds of strength of unit 54 in the printed order.",
              ["सहजं", "कालकृतं", "युक्तिकृतं च"],
              "Innate; made by time; and made by method.",
              "सहजं → कालकृतं → युक्तिकृतं च."),
        match(2, "Match each part of the three names in unit 54 to its meaning.",
              [["सह", "with"], ["ज", "born"], ["काल", "time"], ["युक्ति", "method, skilful application"], ["कृत", "made"]],
              "सह-ज = born with; काल-कृत = made by time; युक्ति-कृत = made by method.",
              "सह, ज, काल, युक्ति, कृत.", role="extend",
              teaches="-कृत at the end of a compound means 'made by': कालकृत = made by time."),
        mcq("discriminate", 3, "By unit 54, which kind of strength is the one a person is born with?",
            ("सहज", "सहज = born with: the innate kind."),
            [("कालकृत", "कालकृत is made by time, not inborn."),
             ("युक्तिकृत", "युक्तिकृत is made by method, not inborn."),
             ("वयःकृत", "वयःकृत (made by age, unit 55) is a kind of time-made strength.")],
            "Innate = सहज.",
            "सहज = born with."),
        mcq("apply", 4, "By unit 54, strength gained through a skilful method belongs to which kind?",
            ("युक्तिकृत, made by method", "युक्ति = skilful method: युक्तिकृत."),
            [("सहज, the kind one is born with", "सहज is inborn, not gained by method."),
             ("कालकृत, made by time", "कालकृत comes from time, not from method."),
             ("प्राकृत, the natural one", "प्राकृत describes the innate kind (unit 55), not method.")],
            "Method → युक्तिकृत.",
            "युक्तिकृत = made by method."),
        mcq("transfer", 5, "By the pattern of कालकृतम् (made by time), what does देवकृतम् mean in a new example?",
            ("Made by the gods", "noun + -कृत = made by that noun: देव-कृत = made by the gods."),
            [("Making the gods", "That would need an agent word like -कर; कृत is 'made'."),
             ("The gods' own time", "No word for time is in देवकृत; कृत is 'made'."),
             ("Not made by gods", "A negation would need अ-: अदेवकृत.")],
            "देवकृतम् = made by the gods, like कालकृतम् = made by time.",
            "X-कृत = made by X.",
            teaches="A noun before -कृत names the maker: काल-कृत = made by time, युक्ति-कृत = made by method."),
    ],
}

# ---------------------------------------------------------------- unit 55
AUTHORED["55"] = {
    "title": "तत्र सहजं देहसत्त्वयोः प्राकृतं",
    "question": "By unit 55, what is innate strength, and from what does time-made strength arise?",
    "rule": ("Of these, innate strength is the natural one (प्राकृतम्) of body and mind (देहसत्त्वयोः); time-made "
             "strength is born of the divisions of the seasons (ऋतुविभागजम्) and made by age (वयःकृतम्)."),
    "limits": ("Prose, two printed lines, copula understood; 'strength' is carried from unit 53. Reading the two "
               "descriptions as two kinds of time-made strength is the data's reading. Which seasons or ages give "
               "more strength is not stated here."),
    "explain_hi": ("इस इकाई में दो छपी पंक्तियाँ (०२.०८.६७ और ०२.०८.६८) जुड़ी हैं। "
                   "इनमें (तत्र) सहज बल देह और सत्त्व यानी मन का प्राकृत (प्रकृति से आया, स्वाभाविक) बल है। "
                   "कालकृत बल ऋतुओं के विभाग से उत्पन्न होता है और वय (आयु) से भी बनता है; डेटा इन दोनों को कालकृत के दो रूप पढ़ता है। "
                   "कौन-सी ऋतु या कौन-सी आयु अधिक बल देती है, यह यहाँ नहीं कहा। "
                   "सन्धि: कालकृतम् + ऋतु → कालकृतमृतु (म् अगले स्वर से जुड़ता है)।"),
    "hook": "सहज: देह-मन का स्वभाव; कालकृत: ऋतु और वय से।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 55, what does ऋतु mean?",
            ("Season", "ऋतु = season: ऋतुविभाग = the division of the seasons."),
            [("Food", "Food would be आहार (unit 56)."),
             ("Family", "Family would be कुल."),
             ("Effort", "Effort would be यत्न.")],
            "ऋतु = season.",
            "ऋतु = season."),
        order(1, "Put these parts of unit 55 in the printed order.",
              ["तत्र", "सहजं देहसत्त्वयोः प्राकृतं", "कालकृतमृतुविभागजं", "वयःकृतं च"],
              "Of these; the innate is the natural one of body and mind; the time-made is born of the divisions of the seasons; and made by age.",
              "तत्र → सहजं देहसत्त्वयोः प्राकृतं → कालकृतमृतुविभागजं → वयःकृतं च."),
        match(2, "Match each word of unit 55 to its meaning.",
              [["देह", "body"], ["सत्त्व", "mind"], ["प्राकृत", "natural"], ["विभाग", "division"], ["वयस्", "age"]],
              "देह = body, सत्त्व = mind, प्राकृत = natural, विभाग = division, वयस् = age.",
              "देह, सत्त्व, प्राकृत, विभाग, वयस्.", role="extend",
              teaches="देहसत्त्वयोः is a dvandva in the genitive dual: 'of body and mind'."),
        mcq("discriminate", 3, "Which split of कालकृतमृतुविभागजं in unit 55 is right?",
            ("कालकृतम् + ऋतुविभागजम्", "म् joins the next vowel ऋ: कालकृतमृतु-."),
            [("कालकृत + मृतुविभागजम्", "मृतु is not a word; the म् ends कालकृतम्."),
             ("कालकृतः + ऋतुविभागजम्", "अः before ऋ would drop to अ with a gap: कालकृत ऋतु-."),
             ("कालकृता + ऋतुविभागजम्", "आ + ऋ would give अर्: कालकृतर्तु-, not the print.")],
            "कालकृतम् (time-made) + ऋतुविभागजम् (born of the divisions of the seasons).",
            "म् + vowel → joined."),
        multi("apply", 4, "By unit 55, from what does time-made strength arise?",
              [("The divisions of the seasons", "Right: ऋतुविभागजम्."),
               ("Food and way of life", "No: that is method-made strength (unit 56)."),
               ("Age", "Right: वयःकृतम्, made by age."),
               ("The natural make of body and mind", "No: that is innate strength (सहज).")],
              [0, 2],
              "कालकृतम्: ऋतुविभागजम् and वयःकृतम्.",
              "Time-made strength = seasons + age."),
        mcq("transfer", 5, "By the pattern of ऋतुविभागजम् (born of the divisions of the seasons), what does जलजम् mean in a new example?",
            ("Born in water", "-ज at the end of a compound = born of, arising in: जल-ज = born in water."),
            [("Giving water", "Giving would need a word like -द or -प्रद; -ज means born."),
             ("Without water", "'Without' would need निर्- or अ-; -ज means born."),
             ("Drinking water", "Drinking would need -प; -ज means born.")],
            "जलजम् = born in water, like ऋतुविभागजम् = born of the seasons' divisions.",
            "X-ज = born of X.",
            teaches="-ज (from √जन्, to be born) at the end of a compound means 'born of': सह-ज, ऋतुविभाग-ज."),
    ],
}

# ---------------------------------------------------------------- unit 56
AUTHORED["56"] = {
    "title": "युक्तिकृतं पुनराहारविहारोत्थ...",
    "question": "By unit 56, what is method-made strength, and which parts of its description are not firm?",
    "rule": ("Method-made strength (युक्तिकृतम्), again (पुनः), is that arising from food and way of life "
             "(आहारविहारोत्थम्); the data reads two more kinds: the vigour-giving (ऊर्जस्करम्) and that born of yoga "
             "(योगजम्)."),
    "limits": ("Prose, copula understood. Printed उर्जस्कर is read ऊर्जस्कर (vowel length; possible). The sense of "
               "ऊर्जस्करम् and योगजम् is not firm, and yoga may mean application, combination or yoga: no question on "
               "those two. Questions rest on युक्तिकृत and food and way of life."),
    "explain_hi": ("युक्तिकृत बल फिर (पुनः) वह है जो आहार और विहार (जीवन-चर्या) से उत्पन्न होता है। "
                   "डेटा इसके दो और रूप पढ़ता है: ऊर्जस्कर (ऊर्जा देने वाला) और योगज (योग से उत्पन्न)। "
                   "पर इन दोनों का अर्थ पक्का नहीं; ‘योग’ का अर्थ प्रयोग, मेल या योग कुछ भी हो सकता है, इसलिए इन पर प्रश्न नहीं। "
                   "छपा ‘उर्जस्कर’ (ह्रस्व उ) सम्भवतः ‘ऊर्जस्कर’ है। "
                   "सन्धि: पुनर् + आहार → पुनराहार (पुनर् का र् स्वर से पहले दिखता है); विहार + उत्थम् → विहारोत्थम् (अ + उ → ओ)।"),
    "hook": "युक्ति का बल: खाना और जीना ठीक।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 56, what does आहार mean?",
            ("Food", "आहार = food, diet."),
            [("Sleep", "Sleep would be निद्रा."),
             ("Season", "Season would be ऋतु (unit 55)."),
             ("Age", "Age would be वयस् (unit 55).")],
            "आहार = food.",
            "आहार = food."),
        order(1, "Put these sure parts of unit 56 in the printed order (sandhi undone).",
              ["युक्तिकृतम्", "पुनर्", "आहार", "विहार", "उत्थम्"],
              "Method-made; again; food; way of life; arisen from.",
              "युक्तिकृतम् → पुनर् → आहार → विहार → उत्थम्."),
        match(2, "Match each sure word of unit 56 to its meaning.",
              [["युक्ति", "method, skilful application"], ["पुनः", "again, however"], ["आहार", "food"],
               ["विहार", "way of life"], ["उत्थ", "arisen from"]],
              "युक्ति = method, पुनः = again, आहार = food, विहार = way of life, उत्थ = arisen from.",
              "युक्ति, पुनः, आहार, विहार, उत्थ.", role="extend",
              teaches="-उत्थ at the end of a compound means 'arisen from': आहारविहार-उत्थ = arising from food and way of life."),
        mcq("discriminate", 3, "Which split of विहारोत्थम् in unit 56 is right?",
            ("विहार + उत्थम्", "अ + उ → ओ: विहार + उत्थम् → विहारोत्थम्."),
            [("विहारो + त्थम्", "त्थम् is not a word; ओ comes from अ + उ."),
             ("विहार + ओत्थम्", "ओत्थम् is not a word; the word is उत्थम्."),
             ("विहारा + उत्थम्", "विहारा is not the stem; it is विहार.")],
            "विहार (way of life) + उत्थम् (arisen from).",
            "अ + उ → ओ."),
        mcq("apply", 4, "In unit 56, why is पुनः seen as पुनर् before आहार?",
            ("पुनः ends in an original र्", "पुनर् is an र्-final word: its र् shows before a vowel."),
            [("Any visarga before आ is र्", "Not any: रामः + आगतः gives राम आगतः."),
             ("The र् begins the word आहार", "आहार begins with आ; the र् ends पुनर्."),
             ("अः before any vowel gives र्", "अः before a vowel gives अ or ओऽ, not र्.")],
            "पुनर् + आहार → पुनराहार.",
            "पुनर्: its र् stands before a vowel."),
        mcq("transfer", 5, "By the pattern of विहार + उत्थम् → विहारोत्थम्, how is सूर्य + उदयः (sunrise) joined in a new example?",
            ("सूर्योदयः", "अ + उ → ओ: सूर्य + उदयः → सूर्योदयः."),
            [("सूर्यौदयः", "औ comes from अ + ओ or औ, not from अ + उ."),
             ("सूर्युदयः", "The अ is not dropped; अ + उ merge into ओ."),
             ("सूर्यवुदयः", "व् comes from उ before a vowel; here उ stands second.")],
            "सूर्य + उदयः = सूर्योदयः, like विहार + उत्थम् = विहारोत्थम्.",
            "अ + उ → ओ.",
            teaches="अ or आ before उ or ऊ gives ओ: विहार + उत्थम् → विहारोत्थम्."),
    ],
}

# ---------------------------------------------------------------- unit 57
AUTHORED["57"] = {
    "title": "तद्वृद्धिकरास्त्विमे च भावा भवंति",
    "question": "By unit 57, what are 'these conditions' (भावाः) said to do?",
    "rule": ("But these conditions (भावाः), too, are producers of its increase (तद्वृद्धिकराः): 'its' = of strength "
             "(data). After तद्यथा (unit 58), unit 59 lists them."),
    "limits": ("Prose. 'Its' is read as of strength (bala); the second च may be 'and' as well as 'too': no question on "
               "it. The conditions are not named in this unit."),
    "explain_hi": ("परन्तु ये भाव (स्थितियाँ, कारक) भी उसकी, यानी बल की, वृद्धि करने वाले हैं। "
                   "‘तत्’ को डेटा बल के लिए लेता है। ‘तु’ = परन्तु, ‘च’ = भी; दूसरा च ‘और’ भी हो सकता है। "
                   "भाव यहाँ नहीं गिनाए गए; ‘तद्यथा’ (इकाई ५८) के बाद इकाई ५९ में सूची है। "
                   "सन्धियाँ: तत् + वृद्धि → तद्वृद्धि, -कराः + तु → -करास्तु, तु + इमे → त्विमे, भावाः + भवन्ति → भावा भवन्ति।"),
    "hook": "ये भाव बल बढ़ाते हैं।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 57, what does वृद्धि mean?",
            ("Increase", "वृद्धि = growth, increase."),
            [("Decay", "Decay would be क्षय (unit 52)."),
             ("Measurement", "Measurement would be मान."),
             ("Method", "Method would be युक्ति (unit 54).")],
            "वृद्धि = increase.",
            "वृद्धि = increase."),
        order(1, "Put the words of unit 57 in the printed order (sandhi undone).",
              ["तद्वृद्धिकराः", "तु", "इमे", "च", "भावाः", "भवन्ति"],
              "Producers of its increase; but; these; too; conditions; are.",
              "तद्वृद्धिकराः → तु → इमे → च → भावाः → भवन्ति."),
        match(2, "Match each word of unit 57 to its meaning.",
              [["वृद्धि", "increase"], ["कर", "making, causing"], ["इमे", "these"], ["भाव", "condition, factor"],
               ["भवन्ति", "are"]],
              "वृद्धि = increase, कर = causing, इमे = these, भाव = condition, भवन्ति = are.",
              "वृद्धि, कर, इमे, भाव, भवन्ति.", role="extend",
              teaches="-कर at the end of a compound means 'making, causing': वृद्धिकर = causing increase."),
        mcq("discriminate", 3, "Which split of तद्वृद्धिकरास्त्विमे in unit 57 is right?",
            ("तद्वृद्धिकराः + तु + इमे", "ः before त → स्; उ before इ → व्: -करास्त्विमे."),
            [("तद्वृद्धिकरा + स्तु + इमे", "स्तु is not a word here; the स् comes from the visarga."),
             ("तद्वृद्धिकराः + तु + विमे", "विमे is not a word; the व् comes from the उ of तु."),
             ("तद्वृद्धिकराः + त्वि + मे", "त्वि is not a word; the words are तु and इमे.")],
            "तद्वृद्धिकराः (producers of its increase) + तु (but) + इमे (these).",
            "ः + त → स्त; उ + इ → वि."),
        mcq("apply", 4, "Why is भावाः printed भावा before भवंति in unit 57?",
            ("Before voiced भ, आः loses ः", "भ is voiced: भावाः + भवन्ति → भावा भवन्ति."),
            [("आः before a voiced sound → ओ", "ओ comes from अः, not आः, before a voiced consonant."),
             ("Visarga before भ always → र्", "र् comes after a vowel other than अ/आ before a voiced sound; here it is आ."),
             ("Visarga before भ becomes स्", "स् arises before त or थ; भ is voiced.")],
            "भावाः + भवन्ति: आः before the voiced भ drops the visarga.",
            "आः + voiced sound → आ."),
        mcq("transfer", 5, "By the pattern of भावाः + भवन्ति → भावा भवन्ति, how is देवाः + गच्छन्ति joined in a new example?",
            ("देवा गच्छन्ति", "आः before the voiced ग drops the visarga."),
            [("देवो गच्छन्ति", "ओ comes from अः before a voiced consonant; here it is आः."),
             ("देवार्गच्छन्ति", "र् comes after a vowel other than अ/आ before a voiced sound."),
             ("देवास्गच्छन्ति", "स् arises before त or थ, not before ग.")],
            "देवाः + गच्छन्ति = देवा गच्छन्ति, like भावाः + भवन्ति = भावा भवन्ति.",
            "आः + voiced sound → आ.",
            teaches="आः drops its visarga before a voiced sound: भावाः + भवन्ति → भावा भवन्ति."),
    ],
}

# ---------------------------------------------------------------- unit 58
AUTHORED["58"] = {
    "title": "तद्यथा",
    "question": "What does the formula तद्यथा (unit 58) mean, and why is तत् printed तद्?",
    "rule": "तत् (that) + यथा (as) = तद्यथा, 'namely, as follows'. The त् becomes द् before the voiced य.",
    "limits": "Prose, one printed word: an introducing formula. The data reads the list in unit 59; no question rests on that link.",
    "explain_hi": ("यह एक शब्द की गद्य-पंक्ति है: ‘तद्यथा’ = वह इस प्रकार है, यानी। "
                   "यह सूची से पहले आने वाला परिचय-शब्द है; डेटा के अनुसार सूची इकाई ५९ में है। "
                   "तत् (वह) + यथा (जैसे); त् घोष य से पहले द् हो जाता है।"),
    "hook": "तद्यथा: अब सूची सुनो।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 58, what does तद्यथा mean?",
            ("Namely, as follows", "तत् (that) + यथा (as): that is as follows."),
            [("Therefore not so", "No negation is printed; तद्यथा introduces."),
             ("Wherever it is", "That would be यत्र; तद्यथा introduces a list."),
             ("Thus it is ended here", "Ending would be an इति formula.")],
            "तद्यथा = namely.",
            "तत् + यथा = namely."),
        match(1, "Match each part of unit 58 to its meaning.",
              [["तत्", "that"], ["यथा", "as"], ["तद्यथा", "namely, as follows"]],
              "तत् = that; यथा = as; तद्यथा = namely.",
              "तत्, यथा, तद्यथा."),
        fill(2, "In unit 58, तद्यथा joins तत् and ____ ('as'). Type it in Devanagari or in English letters (e.g. dharma).",
             accepts("यथा", None, "yatha"),
             "तत् + यथा → तद्यथा.",
             "यथा = as; with तत् it makes the formula 'namely'.",
             "तत् + यथा = तद्यथा."),
        mcq("discriminate", 3, "Which split of तद्यथा in unit 58 is right?",
            ("तत् + यथा", "त् → द् before the voiced य."),
            [("तत् + अथ", "तत् + अथ would give तदथ, with no य."),
             ("तद्य + था", "Neither तद्य nor था is the word here."),
             ("त + द्यथा", "द्यथा is not a word; the words are तत् and यथा.")],
            "तत् (that) + यथा (as).",
            "तद्यथा = तत् + यथा."),
        mcq("apply", 4, "In unit 58, why does तत् show द् before यथा?",
            ("य is a voiced sound", "Before a voiced sound such as य, final त् becomes द्."),
            [("य is a voiceless sound", "य is voiced, not voiceless."),
             ("य is a nasal sound", "य is not a nasal; before a nasal त् may optionally become न् (द् also correct)."),
             ("य is a long vowel", "य is a semivowel consonant, not a vowel.")],
            "तत् + यथा: त् before the voiced य → द्.",
            "त् + voiced sound → द्."),
        mcq("transfer", 5, "By the rule of तद्यथा, how is सत् + आचारः (good conduct) joined in a new example?",
            ("सदाचारः", "त् → द् before a vowel, as before य in तद्यथा."),
            [("सताचारः", "त् does not stay voiceless before a vowel."),
             ("सन्नाचारः", "न् may come (optionally) from त् only before a nasal; आ is a vowel."),
             ("सच्चाचारः", "च् comes from त् before च; here आ follows.")],
            "सत् + आचारः = सदाचारः, like तत् + यथा = तद्यथा.",
            "Final त् + vowel → द्.",
            teaches="A final त् becomes द् before a vowel and before voiced consonants such as य, ग, ब, व: तत् + यथा → तद्यथा."),
    ],
}

# ---------------------------------------------------------------- unit 59
AUTHORED["59"] = {
    "title": "बलवत्पुरुषे देशे जन्म",
    "question": "By unit 59, which conditions increase strength, in the printed order?",
    "rule": ("Birth in a region of strong men and in a time of that kind; a pleasant conjunction of time; excellence of "
             "the qualities of seed and field (probable), of body, food and mind; natural disposition, youth, exercise "
             "and joy."),
    "limits": ("Verbless prose list; the predicate comes from unit 57. bīja = probably semen, kṣetra = probably the womb "
               "(both probable). The kind of time (तद्विधे काले) is not named and the scope of गुण in the long compound "
               "is uncertain: no question on either."),
    "explain_hi": ("यह इकाई ५७ के बल बढ़ाने वाले भाव गिनाती है; पंक्ति में क्रिया नहीं। "
                   "बलवान् पुरुषों वाले देश में जन्म, और वैसे ही काल में; सुखद कालयोग; बीज (सम्भवतः वीर्य) और क्षेत्र (सम्भवतः गर्भाशय) के गुणों, शरीर, आहार और सत्त्व यानी मन की सम्पत्तियाँ; फिर स्वभाव, यौवन, व्यायाम और हर्ष। "
                   "‘वैसा काल’ कौन-सा है, यह नहीं बताया; लम्बे समास में ‘गुण’ किन-किन से जुड़ता है, यह भी अनिश्चित है। "
                   "सन्धि: कालयोगः + बीज- → कालयोगो बीज-, व्यायामः + हर्षः → व्यायामो हर्षः (अः + घोष व्यंजन → ओ); सुखः + च → सुखश्च।"),
    "hook": "देश, काल, बीज-क्षेत्र, शरीर, आहार, मन, स्वभाव, यौवन, व्यायाम, हर्ष: बल बढ़े।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In the list of unit 59, what does यौवन mean?",
            ("Youth", "यौवन = youth, the prime of life."),
            [("Old age", "Old age would be वार्धक्य or जरा."),
             ("Childhood", "Childhood would be बाल्य."),
             ("Sleep", "Sleep would be निद्रा.")],
            "यौवन = youth.",
            "यौवन = youth."),
        order(1, "Put the conditions of unit 59 in the printed order.",
              ["बलवत्पुरुषे देशे जन्म", "तद्विधे च काले", "सुखश्च कालयोगो", "स्वभावो यौवनं", "व्यायामो हर्षश्च"],
              "Birth in a region of strong men; and in a time of that kind; a pleasant conjunction of time; disposition, youth; exercise and joy.",
              "देश → काल → कालयोग → स्वभाव, यौवन → व्यायाम, हर्ष."),
        match(2, "Match each word of unit 59 to its meaning.",
              [["देश", "region"], ["जन्म", "birth"], ["काल", "time"], ["स्वभाव", "natural disposition"],
               ["व्यायाम", "exercise"], ["हर्ष", "joy"]],
              "देश = region, जन्म = birth, काल = time, स्वभाव = disposition, व्यायाम = exercise, हर्ष = joy.",
              "देश, जन्म, काल, स्वभाव, व्यायाम, हर्ष.", role="extend",
              teaches="बलवत्पुरुषे देशे: a bahuvrīhi in the locative, 'in a region that has strong men'."),
        mcq("discriminate", 3, "By unit 59, which of these is not listed as increasing strength?",
            ("Old age", "Old age is not in the list; youth (यौवन) is."),
            [("Youth", "यौवन is listed."),
             ("Exercise", "व्यायाम is listed."),
             ("Joy", "हर्ष is listed.")],
            "Listed: youth, exercise, joy; not old age.",
            "Keep to the printed list."),
        multi("apply", 4, "By unit 59, which belong to the conditions that increase strength?",
              [("Grief and worry", "No: the list ends with joy (हर्ष), not grief."),
               ("Birth in a region of strong men", "Right: बलवत्पुरुषे देशे जन्म."),
               ("A pleasant conjunction of time", "Right: सुखः कालयोगः."),
               ("A body made thin by fasting", "No: thinness is not among the listed conditions."),
               ("Natural disposition", "Right: स्वभावः.")],
              [1, 2, 4],
              "Birth, pleasant time-conjunction, the excellences, disposition, youth, exercise, joy.",
              "Keep to the printed list."),
        mcq("transfer", 5, "By the pattern of व्यायामः + हर्षः → व्यायामो हर्षः, how is रामः + गच्छति joined in a new example?",
            ("रामो गच्छति", "अः before the voiced consonant ग → ओ."),
            [("रामा गच्छति", "Dropping to आ happens with आः; here it is अः."),
             ("रामर्गच्छति", "र् comes after a vowel other than अ/आ before a voiced sound; here it is अ."),
             ("रामस्गच्छति", "स् arises before त or थ, not before ग.")],
            "रामः + गच्छति = रामो गच्छति, like व्यायामः + हर्षः = व्यायामो हर्षः.",
            "अः + voiced consonant → ओ.",
            teaches="अः before a voiced consonant becomes ओ: व्यायामः + हर्षः → व्यायामो हर्षः, स्वभावः + यौवनम् → स्वभावो यौवनम्."),
    ],
}

# ---------------------------------------------------------------- unit 60
AUTHORED["60"] = {
    "title": "तथासाराण्यष्टौ",
    "question": "By unit 60, which are the eight sāras, and for what are they taught?",
    "rule": ("Likewise eight sāras (essences, best qualities) are taught: skin, blood, flesh, fat, bone, marrow, semen "
             "and mind (sattva), for knowing the measure of strength (बलमानज्ञानार्थम्)."),
    "limits": ("Prose; the print runs many words together. 'Each better than the one before' rests on the conjecture "
               "उत्तरोत्तर for printed अत्तरोत्तर: no question on any ranking. उपदिश्यते is singular beside plural साराणि, "
               "read 'is taught'. Fat, marrow, semen: the data's standard names."),
    "explain_hi": ("उसी प्रकार आठ सार (सर्वोत्तम तत्त्व) बताए जाते हैं: त्वचा, रक्त, मांस, मेद (चर्बी), अस्थि (हड्डी), मज्जा, शुक्र (वीर्य) और सत्त्व (मन)। "
                   "ये बल का प्रमाण जानने के लिए (बलमानज्ञानार्थम्) सिखाए जाते हैं। "
                   "‘उत्तरोत्तर श्रेष्ठ’ (हर अगला पिछले से श्रेष्ठ) छपे ‘अत्तरोत्तर’ के अनुमानित पाठ पर टिका है, इसलिए किसी क्रम-श्रेष्ठता पर प्रश्न नहीं। "
                   "‘उपदिश्यते’ एकवचन है, ‘साराणि’ बहुवचन; डेटा इसे ‘सिखाया जाता है’ पढ़ता है। "
                   "सन्धि: साराणि + अष्टौ → साराण्यष्टौ (इ + भिन्न स्वर → य्)।"),
    "hook": "आठ सार: त्वचा से मन तक, बल नापने को।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 60, how many sāras are taught?",
            ("Eight", "साराणि अष्टौ: eight sāras."),
            [("Seven", "अष्टौ is eight, not seven (सप्त)."),
             ("Three", "अष्टौ is eight, not three (त्रयः)."),
             ("Ten", "अष्टौ is eight, not ten (दश).")],
            "अष्टौ = eight.",
            "साराण्यष्टौ = eight sāras."),
        order(1, "After त्वक् and रक्त, put the next sāras of unit 60 in the printed order.",
              ["मांस", "मेदस्", "अस्थि", "मज्जा", "शुक्र", "सत्त्व"],
              "Flesh; fat; bone; marrow; semen; mind.",
              "त्वक् → रक्त → मांस → मेदस् → अस्थि → मज्जा → शुक्र → सत्त्व."),
        match(2, "Match each sāra of unit 60 to its meaning.",
              [["त्वक्", "skin"], ["रक्त", "blood"], ["मांस", "flesh"], ["मेदस्", "fat"], ["अस्थि", "bone"],
               ["मज्जा", "marrow"]],
              "त्वक् = skin, रक्त = blood, मांस = flesh, मेदस् = fat, अस्थि = bone, मज्जा = marrow.",
              "त्वक्, रक्त, मांस, मेदस्, अस्थि, मज्जा.", role="extend",
              teaches="-आत्मक means 'consisting of': the sāras consist of skin, blood ... and mind (-सत्त्वात्मकानि)."),
        mcq("discriminate", 3, "Which split of साराण्यष्टौ in unit 60 is right?",
            ("साराणि + अष्टौ", "इ before a different vowel → य्: साराणि + अष्टौ → साराण्यष्टौ."),
            [("साराण + यष्टौ", "Neither साराण nor यष्टौ is the word here."),
             ("सार + अण्यष्टौ", "अण्यष्टौ is not a word; the words are साराणि and अष्टौ."),
             ("साराणि + यष्टौ", "इ + य would stay इय; and यष्टौ is not eight.")],
            "साराणि (sāras) + अष्टौ (eight).",
            "इ + unlike vowel → य्."),
        mcq("apply", 4, "By unit 60, for what purpose are the sāras taught?",
            ("To know the measure of strength", "बल-मान-ज्ञान-अर्थम्: for knowing the measure of strength."),
            [("To choose a person's daily food", "No food is named in unit 60."),
             ("To divide the age into three", "Dividing the age is in unit 50, not the purpose here."),
             ("To name the seasons in order", "No seasons are named in unit 60.")],
            "बलमानज्ञानार्थम् = for knowing the measure of strength.",
            "-अर्थम् = for the purpose of."),
        mcq("transfer", 5, "By the pattern of साराणि + अष्टौ → साराण्यष्टौ, how is दधि + अत्र (curd here) joined in a new example?",
            ("दध्यत्र", "इ before a different vowel → य्: दधि + अत्र → दध्यत्र."),
            [("दधात्र", "आ comes from अ + अ; here the first vowel is इ."),
             ("दधेत्र", "ए comes from अ + इ; here इ stands first."),
             ("दधीत्र", "ई comes from इ + इ; here the second vowel is अ.")],
            "दधि + अत्र = दध्यत्र, like साराणि + अष्टौ = साराण्यष्टौ.",
            "इ + unlike vowel → य्.",
            teaches="इ or ई before a different vowel becomes य्: साराणि + अष्टौ → साराण्यष्टौ."),
    ],
}

# ---------------------------------------------------------------- unit 61
AUTHORED["61"] = {
    "title": "अपिच",
    "question": "Which two words make the link अपिच of unit 61, and how would अपि join a vowel?",
    "rule": "अपिच = अपि (also) + च (and): 'and further', opening a new statement. अपि keeps its इ before a consonant; before a different vowel it would show य्.",
    "limits": "Prose, one printed word, a stock link. It names nothing; no question rests on the statement it opens.",
    "explain_hi": ("यह फिर से एक शब्द की गद्य-पंक्ति है: ‘अपि च’ = और भी। "
                   "यह आगे एक नई बात शुरू करता है; डेटा के अनुसार वह बात अगले भाग में आरम्भ होती है। "
                   "अपि (भी) और च (और) दोनों अव्यय हैं। "
                   "च से पहले अपि का इ नहीं बदलता; भिन्न स्वर से पहले वह य् बन जाता है, जैसे अपि + अस्ति → अप्यस्ति।"),
    "hook": "फिर अपि च: और एक बात।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 61, which two words are printed together as अपिच?",
            ("अपि and च", "अपि (also) + च (and), written without a space."),
            [("अपि and इव", "इव (like) would give अपीव; the print has च."),
             ("अथ and च", "अथ would give अथच; the print has अपि."),
             ("अपि and एव", "एव (only) would give अप्येव; the print has च.")],
            "अपिच = अपि + च.",
            "अपि + च."),
        mcq("warmup", 1, "What does च add in unit 61?",
            ("And", "च = and: अपि च = and further."),
            [("Or", "'Or' would be वा."),
             ("Not", "'Not' would be न."),
             ("Only", "'Only' would be एव.")],
            "च = and.",
            "च = and."),
        fill(2, "In unit 61 the link अपिच is अपि followed by ____ (and). Type it in Devanagari or in English letters (e.g. dharma).",
             accepts("च", None, "cha"),
             "अपि + च = अपिच.",
             "च is an indeclinable, 'and'; it follows the word it adds.",
             "अपि + च = अपिच."),
        mcq("discriminate", 3, "Which English rendering of अपिच in unit 61 is right?",
            ("And further", "अपि (also) + च (and): and further."),
            [("Even so not", "No negation is printed."),
             ("Only this one", "'Only' would need एव."),
             ("Or the other", "'Or' would need वा.")],
            "अपिच = and further.",
            "अपि च = and further."),
        multi("apply", 4, "Which statements about unit 61 are right?",
              [("It contains a verb", "No: अपि and च are indeclinables; there is no verb."),
               ("It names a body part", "No: the line is only a link."),
               ("It is one printed word", "Right: अपि and च are printed together."),
               ("Its two parts are indeclinables", "Right: neither takes a case ending.")],
              [2, 3],
              "One printed word, two indeclinables, no verb.",
              "अपिच = अपि + च, both indeclinables."),
        mcq("transfer", 5, "By vowel sandhi, how is अपि + अस्ति (there is also) joined in a new example?",
            ("अप्यस्ति", "इ before a different vowel becomes य्: अपि + अस्ति → अप्यस्ति."),
            [("अपास्ति", "आ comes from अ + अ; here the first vowel is इ."),
             ("अपेस्ति", "ए comes from अ + इ; here इ stands first."),
             ("अपीस्ति", "ई comes from इ + इ; here the second vowel is अ.")],
            "अपि + अस्ति = अप्यस्ति.",
            "इ + unlike vowel → य्.",
            teaches="अपि stays unchanged before a consonant (अपि च), but before a different vowel its इ becomes य् (अप्यस्ति)."),
    ],
}

# ---------------------------------------------------------------- unit 62
AUTHORED["62"] = {
    "title": "न मुच्येद्देहमात्रदर्शनादेव...",
    "question": "By unit 62, which two judgements drawn from merely seeing the body are quoted?",
    "rule": ("A physician (भिषक्) should not, on a conjectural reading, be misled merely by seeing the body "
             "(देहमात्रदर्शनात् एव): 'this one is strong from bulk or a large body; this one has little strength from "
             "thinness or a small body'."),
    "limits": ("Printed मुच्येत् ('should be released') makes no sense here; मुह्येत् ('should be deluded') is a "
               "conjecture: no question on the verb. न, the subject भिषक् and the two quoted thoughts are sure. upacaya = "
               "plumpness of flesh (standard)."),
    "explain_hi": ("अनुमानित पाठ पर: वैद्य केवल देह देखने मात्र से भ्रमित न हो कि ‘यह उपचय (मांस की पुष्टि) से या बड़े शरीर से बलवान है; यह दुबलेपन से या छोटे शरीर से अल्प बल वाला है।’ "
                   "छपा ‘मुच्येत्’ (छूटे) यहाँ अर्थ नहीं देता; ‘मुह्येत्’ (भ्रमित हो) अनुमानित पाठ है, इसलिए क्रिया पर प्रश्न नहीं। "
                   "पक्के अंश: न, भिषक्, और दोनों उद्धृत अनुमान, जिन्हें ‘इति’ बन्द करता है। "
                   "सन्धियाँ: भिषक् + अयम् → भिषगयम् (स्वर से पहले क् → ग्), -त्वात् + वा → -त्वाद्वा (घोष व से पहले त् → द्), दर्शनात् + एव → दर्शनादेव।"),
    "hook": "मोटा तो बलवान, दुबला तो निर्बल: अनुमानित पाठ पर, केवल देखकर ऐसा न मानो।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In unit 62, what does उपचय mean?",
            ("Bulk, plumpness of flesh", "उपचय = accumulation, plumpness of flesh."),
            [("Thinness of the limbs", "Thinness is कृश / कृशत्व, the opposite."),
             ("Lightness of the mind", "उपचय is bodily bulk, not a state of mind."),
             ("Weakness of the voice", "No voice is named; उपचय is bodily bulk.")],
            "उपचय = bulk of flesh.",
            "उपचय = plumpness."),
        order(1, "Put these sure parts of unit 62 in the printed order (the doubtful verb is left out).",
              ["देहमात्रदर्शनादेव", "उपचयेन महाशरीरत्वाद्वा", "बलवानयं", "कृशत्वादल्पशरीरत्वाद्वा", "अल्पबलइति"],
              "Merely from seeing the body; by bulk or from a large body; this one is strong; from thinness or a small body; of little strength, thus.",
              "देहमात्रदर्शनादेव → उपचयेन महाशरीरत्वाद्वा → बलवानयं → कृशत्वादल्पशरीरत्वाद्वा → अल्पबलइति."),
        match(2, "Match each word of unit 62 to its meaning.",
              [["भिषक्", "physician"], ["देह", "body"], ["मात्र", "merely, only"], ["कृश", "thin"], ["अल्प", "little, small"],
               ["बलवान्", "strong"]],
              "भिषक् = physician, देह = body, मात्र = merely, कृश = thin, अल्प = little, बलवान् = strong.",
              "भिषक्, देह, मात्र, कृश, अल्प, बलवान्.", role="extend",
              teaches="-त्वात् is the ablative of an abstract in -त्व: कृशत्वात् = because of thinness."),
        mcq("discriminate", 3, "In the quoted thought of unit 62, from what is a person judged strong?",
            ("Bulk or a large body", "उपचयेन महाशरीरत्वाद्वा बलवानयम्."),
            [("Thinness or a small body", "That leads to the judgement 'of little strength'."),
             ("Voice or way of walking", "No voice or gait is named in unit 62."),
             ("Diet or daily exercise", "No diet or exercise is named in unit 62.")],
            "Bulk or largeness → 'strong'; thinness or smallness → 'of little strength'.",
            "Two quoted judgements from the body alone."),
        multi("apply", 4, "By unit 62, which are quoted as grounds for judging a person of little strength?",
              [("Bulk of flesh", "No: bulk leads to the judgement 'strong'."),
               ("Thinness", "Right: कृशत्वात्."),
               ("A large body", "No: a large body leads to 'strong'."),
               ("A small body", "Right: अल्पशरीरत्वात्.")],
              [1, 3],
              "कृशत्वात् अल्पशरीरत्वात् वा अल्पबलः.",
              "Thinness or small body → 'of little strength' (quoted)."),
        mcq("transfer", 5, "By the pattern of भिषक् + अयम् → भिषगयम्, how is सम्यक् + उक्तम् (rightly said) joined in a new example?",
            ("सम्यगुक्तम्", "क् before a vowel becomes ग्: सम्यक् + उक्तम् → सम्यगुक्तम्."),
            [("सम्यकुक्तम्", "क् does not stay voiceless before a vowel."),
             ("सम्यङुक्तम्", "ङ् may come from क् only before a nasal; उ is a vowel."),
             ("सम्यखुक्तम्", "No aspiration arises; क् before a vowel gives ग्.")],
            "सम्यक् + उक्तम् = सम्यगुक्तम्, like भिषक् + अयम् = भिषगयम्.",
            "Final क् + vowel → ग्.",
            teaches="A final क् becomes ग् before a vowel or a voiced consonant: भिषक् + अयम् → भिषगयम्."),
    ],
}

# ================================================================ NOTES_HI
NOTES_HI = {
    "51": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। एक शब्द ‘अपिच’ = अपि + च, बिना जगह छपा। डेटा के अनुसार आगे का कथन छपी "
           "पंक्तियों ६३-६४ में है, यानी इकाई ५२ में। सन्धि जाँची: व्यंजन च से पहले अपि का इ नहीं बदलता।"),
    "52": ("गद्य (प्रकार डेटा का), पर पंक्तियाँ छन्दोबद्ध प्रतीत होती हैं; विश्वास कम; दो छपी पंक्तियाँ (०२.०८.६३ और ०२.०८.६४) जोड़ी गईं। "
           "‘वर्षं वर्षं’ के दो पठन: कर्ता ‘एक वर्ष’ (एकवचन ‘याति’ के साथ), या क्रियाविशेषण ‘वर्ष-दर-वर्ष’; ‘याते शते शते’ सति सप्तमी "
           "(सौ-सौ बीतने पर)। किसका क्षय होता है, यह नहीं कहा। पाठ-चिह्न (सम्भव): ‘आयुषो’ प से पहले नियमित नहीं, ‘आयुषः’ अपेक्षित; "
           "डेटा के अनुसार दूसरी पंक्ति छोटी है, कोई शब्द छूटा हो सकता है, और ‘यत्’ का ‘तत्’ नहीं; पंक्ति अक्षरशः पढ़ी गई। सन्धि जाँची: "
           "पुण्यबाहुल्यात् + यत् → पुण्यबाहुल्याद्यत् (घोष य से पहले त् → द्); यत् + मानम् → यन्मानम् (नासिक्य से पहले त् → न् वैकल्पिक, द् भी "
           "ठीक); मानम् + इष्यते → मानमिष्यते; व्यंजन से पहले अन्तिम म् → ं (वर्षं, क्षयं, नृणां)।"),
    "53": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। तीन भेद छपी पंक्ति ६६ यानी इकाई ५४ में। सन्धि जाँची: बलम् + अपि → बलमपि; "
           "त्रिविधम् + भवति → त्रिविधं भवति (वाक्य में व्यंजन से पहले अन्तिम म् → ं)।"),
    "54": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। क्रिया-रहित सूची; ‘बल’ इकाई ५३ से। युक्ति = प्रयोग, कुशल विधि; डेटा के अनुसार "
           "इसका विवरण छपी पंक्ति ६९ यानी इकाई ५६ में। सन्धि जाँची: व्यंजन से पहले अन्तिम म् → ं (सहजं कालकृतं युक्तिकृतं)।"),
    "55": ("गद्य; विश्वास मध्यम; दो छपी पंक्तियाँ (०२.०८.६७ और ०२.०८.६८) जोड़ी गईं; कोई पाठ-चिह्न नहीं। क्रिया समझी जाती है; ‘बल’ "
           "इकाई ५३ से, अंग्रेज़ी में कोष्ठक में। प्राकृत = प्रकृति से आया; सत्त्व = मन (मानक)। ‘ऋतुविभागज’ और ‘वयःकृत’ को कालकृत बल के "
           "दो रूप पढ़ना डेटा का पठन है। सन्धि जाँची: कालकृतम् + ऋतु- → कालकृतमृतु-; -जम् + वयः- → -जं वयः-; वयस् + कृतम् → वयःकृतम् "
           "(छपा रूप)।"),
    "56": ("गद्य; विश्वास मध्यम। पाठ-चिह्न (सम्भव): छपा ‘उर्जस्कर’ (ह्रस्व उ) = ऊर्जस्कर; ‘योगजं’ से पहले जगह का न होना केवल छपाई। "
           "‘योग’ अस्पष्ट (प्रयोग, मेल या योग); डेटा तीन रूप पढ़ता है, पर ऊर्जस्कर और योगज का अर्थ पक्का नहीं, इन पर प्रश्न नहीं। "
           "सन्धि जाँची: पुनर् + आहार → पुनराहार (पुनर् का अपना र्); विहार + उत्थम् → विहारोत्थम् (अ + उ → ओ); -उत्थम् + उर्ज- → -उत्थमुर्ज-।"),
    "57": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। ‘तत्’ = बल का (डेटा)। ‘तु’ = परन्तु, ‘च’ = भी; दूसरा च ‘और’ भी हो सकता है। "
           "भावों की सूची छपी पंक्ति ७२ यानी इकाई ५९ में; पंक्ति ७१ (इकाई ५८) ‘तद्यथा’ है। सन्धि जाँची: तत् + वृद्धि → तद्वृद्धि (घोष व से "
           "पहले त् → द्); -कराः + तु → -करास्तु (त से पहले विसर्ग → स्); तु + इमे → त्विमे (उ + भिन्न स्वर → व्); भावाः + भवन्ति → भावा "
           "भवन्ति (घोष ध्वनि से पहले आः का विसर्ग लुप्त)। छपा ‘भवंति’ = भवन्ति।"),
    "58": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। परिचय-सूत्र ‘तद्यथा’; सूची छपी पंक्ति ७२ यानी इकाई ५९ में। सन्धि जाँची: तत् + यथा → "
           "तद्यथा (घोष य से पहले त् → द्)।"),
    "59": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। क्रिया-रहित सूची, विधेय इकाई ५७ से। बीज = सम्भवतः वीर्य, क्षेत्र = सम्भवतः गर्भाशय "
           "(दोनों सम्भावित)। ‘तद्विधे काले’ का काल नहीं बताया। लम्बे समास में ‘गुण’ का विस्तार अनिश्चित; डेटा चार सम्पत्तियाँ पढ़ता है: "
           "बीज-क्षेत्र के गुण, शरीर, आहार, सत्त्व। छपा ‘संपतयः’ (एक त), डेटा का विभाजन sampatayaḥ, अर्थ ‘सम्पत्तियाँ’। सन्धि जाँची: "
           "बलवत् + पुरुषे → बलवत्पुरुषे; तत् + विधे → तद्विधे; सुखः + च → सुखश्च; कालयोगः + बीज- → कालयोगो बीज- और स्वभावः + यौवनम् → "
           "स्वभावो यौवनम्, व्यायामः + हर्षः → व्यायामो हर्षः (अः + घोष व्यंजन → ओ); हर्षः + च → हर्षश्च।"),
    "60": ("गद्य; विश्वास मध्यम। पाठ-चिह्न (सम्भव): ‘-त्मकान्यत्तरोत्तर-’ में ‘अत्तरोत्तर’ कोई शब्द नहीं; ‘आत्मकानि + उत्तरोत्तरवराणि’ "
           "(हर अगला श्रेष्ठ) अनुमानित पाठ है, अनुवाद में चिह्नित; श्रेष्ठता-क्रम पर प्रश्न नहीं। ‘उपदिश्यते’ एकवचन, ‘साराणि’ बहुवचन: "
           "भाववाच्य ‘सिखाया जाता है’ पढ़ा गया। छपाई में कई शब्द बिना जगह। मेदस् = चर्बी, मज्जा = मज्जा, शुक्र = वीर्य (मानक)। सन्धि जाँची: "
           "साराणि + अष्टौ → साराण्यष्टौ (इ + भिन्न स्वर → य्); त्वक् + रक्त → त्वग्रक्त (घोष र से पहले क् → ग्); मेदस् + अस्थि → मेदोऽस्थि "
           "(छपा ‘मेदोस्थि’, अवग्रह नहीं छपा); -ज्ञानार्थम् + उपदिश्यते → -ज्ञानार्थमुपदिश्यते।"),
    "61": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। ‘अपिच’ = अपि + च, बिना जगह। डेटा के अनुसार आगे का कथन अगले भाग में आरम्भ होता है। "
           "सन्धि जाँची: व्यंजन च से पहले इ अपरिवर्तित।"),
    "62": ("गद्य; विश्वास मध्यम। पाठ-चिह्न (सम्भव): छपा ‘मुच्येत्’ (छूटे) अर्थ नहीं देता; ‘मुह्येत्’ (भ्रमित हो; च्य/ह्य की भूल) अनुमानित "
           "पाठ, अनुवाद में चिह्नित; क्रिया पर प्रश्न नहीं। भिषक् कर्ता; दोनों ‘अयम्’ उद्धृत दो व्यक्ति। छपा ‘बलइति’ = बलः इति (अः + "
           "अ से भिन्न स्वर → अ, बीच में अन्तर; छपाई में साथ)। उपचय = मांस की पुष्टि (मानक)। सन्धि जाँची: -येत् + देह- → -येद्देह- (घोष द से "
           "पहले त् → द्); दर्शनात् + एव → दर्शनादेव; भिषक् + अयम् → भिषगयम् (स्वर से पहले क् → ग्); अयम् + उपचयेन → अयमुपचयेन; "
           "-त्वात् + वा → -त्वाद्वा; बलवान् + अयम् → बलवानयम्; कृशत्वात् + अल्प- → कृशत्वादल्प-; वा + अल्प- → वाऽल्प- (आ + अ → आ; अवग्रह "
           "छपाई की आदत)।"),
}

# ================================================================ AIDS
AIDS = {
    "51": {
        "chunks": "अपि | च",
        "sandhi": "व्यंजन से पहले इ नहीं बदलता: अपि + च → अपिच · भिन्न स्वर से पहले इ → य्: अपि + अस्ति → अप्यस्ति।",
        "anchors": "अपि = भी, च = और: मिलकर ‘और भी’, यानी एक बात और। (मेरी याद-पद्धति)",
    },
    "52": {
        "chunks": "वर्षं वर्षं | क्षयं याति | नृणां | याते शते शते || आयुषो | पुण्यबाहुल्याद्यन्मानमिष्यते",
        "sandhi": ("घोष य से पहले त् → द्: पुण्यबाहुल्यात् + यत् → पुण्यबाहुल्याद्यत् · नासिक्य म से पहले त् → न् (वैकल्पिक, द् भी ठीक): "
                   "यत् + मानम् → यन्मानम् · म् + स्वर: मानम् + इष्यते → मानमिष्यते।"),
        "anchors": "पक्का: पहली पंक्ति, सौ-सौ बीतने पर क्षय। खुला: वर्षं वर्षं का पठन, क्या घटता है, दूसरी पंक्ति की रचना। (मेरी याद-पद्धति)",
    },
    "53": {
        "frame": "क्या: बलम् → जोड़: अपि (भी) → कैसा: त्रिविधम् (तीन प्रकार का) → क्रिया: भवति; भेद इकाई ५४ में।",
        "chunks": "बलमपि | त्रिविधं | भवति",
        "sandhi": "म् + स्वर: बलम् + अपि → बलमपि · वाक्य में व्यंजन से पहले अन्तिम म् → ं: त्रिविधम् + भवति → त्रिविधं भवति।",
    },
    "54": {
        "chain": {"steps": ["१ सहज: जन्म के साथ", "२ कालकृत: काल से बना", "३ युक्तिकृत: युक्ति से बना"]},
        "chunks": "सहजं | कालकृतं | युक्तिकृतं च",
        "pegs": "स-का-यु: सहज, कालकृत, युक्तिकृत के पहले अक्षर। (मेरा बनाया स्मरण-सूत्र)",
    },
    "55": {
        "contrast": "सहज: देह और सत्त्व (मन) का प्राकृत बल ⇄ कालकृत: ऋतु-विभाग से उत्पन्न और वय से बना: दोनों इसी इकाई में।",
        "chunks": "तत्र | सहजं | देहसत्त्वयोः | प्राकृतं || कालकृतमृतुविभागजं | वयःकृतं च",
        "sandhi": "म् + स्वर: कालकृतम् + ऋतु- → कालकृतमृतु- · व्यंजन से पहले अन्तिम म् → ं: सहजं देह-, -जं वयः-।",
    },
    "56": {
        "chunks": "युक्तिकृतं | पुनराहारविहारोत्थमुर्जस्करंयोगजं च",
        "sandhi": "पुनर् का अपना र् स्वर से पहले: पुनर् + आहार → पुनराहार · अ + उ → ओ: विहार + उत्थम् → विहारोत्थम्।",
        "anchors": "पक्का: युक्तिकृत = आहार-विहार से उत्पन्न। अस्पष्ट: ऊर्जस्कर, योगज का अर्थ; छपा उर्ज-। (मेरी याद-पद्धति)",
    },
    "57": {
        "frame": "कौन: इमे भावाः (ये भाव) → क्या करते: तद्वृद्धिकराः (बल बढ़ाने वाले) → जोड़: तु, च → क्रिया: भवन्ति।",
        "chunks": "तद्वृद्धिकरास्त्विमे | च | भावा भवंति",
        "sandhi": ("घोष व से पहले त् → द्: तत् + वृद्धि → तद्वृद्धि · त से पहले विसर्ग → स्: -कराः + तु → -करास्तु · उ + भिन्न स्वर → व्: "
                   "तु + इमे → त्विमे · घोष ध्वनि से पहले आः → आ: भावाः + भवन्ति → भावा भवन्ति।"),
    },
    "58": {
        "chunks": "तत् | यथा",
        "sandhi": "घोष य से पहले त् → द्: तत् + यथा → तद्यथा।",
        "frame": "परिचय-सूत्र: तद्यथा (यानी) → सूची इकाई ५९ में।",
    },
    "59": {
        "diagram": {"groups": [
            {"label": "बल बढ़ाने वाले भाव (छपे क्रम में)",
             "items": ["१ बलवान् पुरुषों वाले देश में जन्म", "२ वैसे ही काल में", "३ सुखद कालयोग",
                       "४ बीज (सम्भावित: वीर्य), क्षेत्र (सम्भावित: गर्भाशय) के गुण, शरीर, आहार, सत्त्व की सम्पत्ति",
                       "५ स्वभाव", "६ यौवन", "७ व्यायाम", "८ हर्ष"]}]},
        "chunks": ("बलवत्पुरुषे देशे जन्म | तद्विधे च काले | सुखश्च कालयोगो | बीजक्षेत्रगुणशरीराहारसत्त्वसंपतयः | स्वभावो | "
                   "यौवनं | व्यायामो | हर्षश्च"),
        "sandhi": ("अः + घोष व्यंजन → ओ: कालयोगः + बीज- → कालयोगो बीज-, व्यायामः + हर्षः → व्यायामो हर्षः · च से पहले विसर्ग → श्: "
                   "सुखः + च → सुखश्च · घोष व से पहले त् → द्: तत् + विधे → तद्विधे।"),
        "pegs": "दे-का-यो | सम्पत्ति | स्व-यौ-व्या-ह: देश, काल, कालयोग; सम्पत्ति; स्वभाव, यौवन, व्यायाम, हर्ष। (मेरा बनाया स्मरण-सूत्र)",
    },
    "60": {
        "diagram": {"groups": [
            {"label": "आठ सार (छपे क्रम में)",
             "items": ["१ त्वक्: त्वचा", "२ रक्त", "३ मांस", "४ मेदस्: चर्बी", "५ अस्थि: हड्डी", "६ मज्जा",
                       "७ शुक्र: वीर्य", "८ सत्त्व: मन"]}]},
        "chunks": ("तथासाराण्यष्टौ | त्वग्रक्तमांसमेदोस्थिमज्जशुक्रसत्त्वात्मकान्यत्तरोत्तरवराणि | बलमानज्ञानार्थम् | उपदिश्यते"),
        "sandhi": ("इ + भिन्न स्वर → य्: साराणि + अष्टौ → साराण्यष्टौ · घोष र से पहले क् → ग्: त्वक् + रक्त → त्वग्रक्त · "
                   "अस् + अ → ओऽ: मेदस् + अस्थि → मेदोऽस्थि (छपा मेदोस्थि)।"),
        "pegs": "त्व-र-मां-मे | अ-म-शु-स: चार-चार अक्षरों के दो जोड़े। (मेरा बनाया स्मरण-सूत्र; कोई श्रेष्ठता-क्रम नहीं)",
    },
    "61": {
        "chunks": "अपि | च",
        "sandhi": "व्यंजन से पहले इ अपरिवर्तित: अपि + च · भिन्न स्वर से पहले इ → य्: अपि + अस्ति → अप्यस्ति।",
        "anchors": "दूसरी बार ‘अपि च’: हर बार एक नई बात खुलती है। (मेरी याद-पद्धति)",
    },
    "62": {
        "seesaw": "बलवान्: उपचय (पुष्टि) या बड़ा शरीर ⇄ अल्पबल: दुबलापन या छोटा शरीर: दोनों उद्धृत अनुमान इसी इकाई में, और केवल देह देखकर।",
        "chunks": "न मुच्येद्देहमात्रदर्शनादेव | भिषगयमुपचयेन | महाशरीरत्वाद्वा | बलवानयं | कृशत्वादल्पशरीरत्वाद्वाऽल्पबलइति",
        "sandhi": ("स्वर से पहले क् → ग्: भिषक् + अयम् → भिषगयम् · घोष व से पहले त् → द्: -त्वात् + वा → -त्वाद्वा · स्वर से पहले त् → द्: "
                   "दर्शनात् + एव → दर्शनादेव, कृशत्वात् + अल्प- → कृशत्वादल्प-।"),
        "anchors": "पक्का: न, भिषक्, दो उद्धृत अनुमान। अनुमान: मुच्येत् → मुह्येत्। (मेरी याद-पद्धति)",
    },
}

# ================================================================ IMAGE_SPECS
IMAGE_SPECS = {
    ("54", "chain"): {
        "file": "sh8-bala-trividha-54.svg",
        "alt": ("Table of card 54 in printed order: the three kinds of strength: innate (sahaja), made by time "
                "(kālakṛta), made by method (yuktikṛta)."),
        "type": "table",
        "title": "कार्ड ५४: बल के तीन भेद",
        "heads": ["क्रम", "बल का भेद"],
        "rows": [["१", "सहज: जन्म के साथ"], ["२", "कालकृत: काल से बना"], ["३", "युक्तिकृत: युक्ति से बना"]],
    },
    ("55", "contrast"): {
        "file": "sh8-sahaja-kalakrita-55.svg",
        "alt": ("Split of card 55: innate strength, the natural one of body and mind; time-made strength, born of the "
                "divisions of the seasons and made by age."),
        "type": "split",
        "title": "कार्ड ५५: सहज और कालकृत बल",
        "cols": [["सहज", ["देह और सत्त्व (मन) का", "प्राकृत"]],
                 ["कालकृत", ["ऋतु-विभाग से उत्पन्न", "वय से बना"]]],
    },
    ("59", "diagram"): {
        "file": "sh8-bala-vriddhi-59.svg",
        "alt": ("Table of card 59 in printed order: eight entries that increase strength: birth in a region of strong "
                "men; in a time of that kind; a pleasant conjunction of time; excellence of seed (probably semen) and "
                "field (probably the womb) qualities, body, food and mind; disposition; youth; exercise; joy."),
        "type": "table",
        "title": "कार्ड ५९: बल बढ़ाने वाले भाव",
        "heads": ["क्रम", "भाव"],
        "rows": [["१", "बलवान् पुरुषों वाले देश में जन्म"], ["२", "वैसे ही काल में"], ["३", "सुखद कालयोग"],
                 ["४", "बीज (सम्भावित: वीर्य), क्षेत्र (सम्भावित: गर्भाशय) के गुण, शरीर, आहार, सत्त्व की सम्पत्ति"],
                 ["५", "स्वभाव"], ["६", "यौवन"], ["७", "व्यायाम"], ["८", "हर्ष"]],
    },
    ("60", "diagram"): {
        "file": "sh8-ashta-sara-60.svg",
        "alt": ("Table of card 60 in printed order: the eight sāras: skin, blood, flesh, fat, bone, marrow, semen, "
                "mind (sattva); no ranking shown."),
        "type": "table",
        "title": "कार्ड ६०: आठ सार (छपे क्रम में)",
        "heads": ["क्रम", "सार"],
        "rows": [["१", "त्वक्: त्वचा"], ["२", "रक्त"], ["३", "मांस"], ["४", "मेदस्: चर्बी"], ["५", "अस्थि: हड्डी"],
                 ["६", "मज्जा"], ["७", "शुक्र: वीर्य"], ["८", "सत्त्व: मन"]],
    },
    ("62", "seesaw"): {
        "file": "sh8-deha-matra-62.svg",
        "alt": ("Split of card 62: the two quoted judgements from merely seeing the body: strong, from bulk or a large "
                "body; of little strength, from thinness or a small body."),
        "type": "split",
        "title": "कार्ड ६२: केवल देह देखकर अनुमान",
        "cols": [["‘बलवान्’ माना", ["उपचय (पुष्टि) से", "बड़े शरीर से"]],
                 ["‘अल्पबल’ माना", ["दुबलेपन से", "छोटे शरीर से"]]],
    },
}
