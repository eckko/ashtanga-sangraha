from helpers import mcq, match, order, fill, multi, accepts


def T(q, teaches):
    q["teaches"] = teaches
    return q


AUTHORED = {}

# ---------------------------------------------------------------- unit 14
AUTHORED["14"] = {
    "title": "स्थिते तु रक्ते रोमराजी",
    "question": "What does unit 14 say appears when the blood has settled, and where does the blood go?",
    "rule": ("When the blood has settled, a line of hair (romarājī) appears; and the blood (asṛk) goes upward "
             "to the remainder of the jarāyu (probably the foetal membrane)."),
    "limits": ("The second clause can also be read 'the remainder of the jarāyu goes up as blood'; the card takes asṛk as subject, "
               "and no question rests on the choice. On whose body the line of hair appears is not stated. "
               "jarāyu as foetal membrane is a probable identification."),
    "explain_hi": ("यह गद्य-पंक्ति गर्भ ठहरने के बाद रक्त की बात आगे बढ़ाती है। रक्त के स्थिर हो जाने पर रोमराजी, यानी रोमों की पंक्ति, प्रकट होती है; "
                   "यह किसके शरीर पर, पंक्ति नहीं बताती। फिर ‘असृक्’ (रक्त का ही दूसरा नाम) ऊपर जरायु के शेष को प्राप्त होता है। "
                   "जरायु सम्भवतः गर्भ की झिल्ली है (इकाई १३)। दूसरा खण्ड दो तरह पढ़ा जा सकता है; कार्ड असृक् को कर्ता मानता है।"),
    "hook": "रक्त ठहरा: रोमराजी उभरी, असृक् ऊपर चला।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 14, what appears when the blood has settled?",
            ("A line of hair (रोमराजी)", "रोमराजी प्रादुर्भवति: a line of hair appears."),
            [("The menstrual flow again", "Unit 11 says the ārtava is no longer seen."),
             ("A swelling of the feet", "No swelling of the feet is named in this unit."),
             ("The first embryonic mass", "The kalala is named for the first month in unit 17.")],
            "When the blood has settled, a line of hair (romarājī) appears.",
            "स्थिते रक्ते → रोमराजी प्रादुर्भवति."),
        order(1, "Put these words of unit 14 in their printed order.",
              ["स्थिते तु रक्ते", "रोमराजी", "प्रादुर्भवति", "जरायुशेषम्", "ऊर्ध्वमसृक्", "प्रतिपद्यते"],
              "First the time (the blood settled), then the line of hair appears, then the blood goes up to the jarāyu's remainder.",
              "स्थिते रक्ते → रोमराजी प्रादुर्भवति → जरायुशेषम् → ऊर्ध्वम् असृक् प्रतिपद्यते."),
        T(match(2, "Match each word of unit 14 to its meaning on the card.",
                [["स्थिते", "when settled"], ["रोमराजी", "line of hair"], ["प्रादुर्भवति", "appears"],
                 ["असृक्", "blood"], ["प्रतिपद्यते", "goes to, reaches"]],
                "These five words carry the two events: the hair-line appears, the blood goes upward.",
                "स्थिते, रोमराजी, प्रादुर्भवति, असृक्, प्रतिपद्यते.", role="extend"),
          "असृक् (stem असृज्) is another word for blood, like रक्त."),
        mcq("discriminate", 3, "Which split of चोर्ध्वम् is right?",
            ("च + ऊर्ध्वम्", "अ + ऊ → ओ: च + ऊर्ध्वम् → चोर्ध्वम्."),
            [("चौ + ऊर्ध्वम्", "औ + ऊ would give चावूर्ध्वम्, not चोर्ध्वम्."),
             ("चे + ऊर्ध्वम्", "ए before a vowel does not give ओ."),
             ("चोर् + ध्वम्", "चोर् and ध्वम् are not the card's words.")],
            "च (and) + ऊर्ध्वम् (upward): अ + ऊ merges into ओ.",
            "अ/आ + उ/ऊ → ओ."),
        mcq("apply", 4, "In unit 14, which word is another name for रक्त (blood)?",
            ("असृक्", "असृक् (असृज्) is a synonym of रक्त, both 'blood'."),
            [("जरायु", "जरायु is probably the foetal membrane, not blood."),
             ("रोमराजी", "रोमराजी is a line of hair."),
             ("ऊर्ध्वम्", "ऊर्ध्वम् means upward.")],
            "The line begins with रक्ते and later calls the blood असृक्.",
            "असृक् = रक्त = blood."),
        T(mcq("transfer", 5, "By the rule of चोर्ध्वम्, how is जल + ऊर्मिः written when joined?",
              ("जलोर्मिः", "अ + ऊ → ओ, as in च + ऊर्ध्वम् → चोर्ध्वम्."),
              [("जलौर्मिः", "अ + ऊ gives ओ, not the vṛddhi vowel औ."),
               ("जलूर्मिः", "The अ does not simply drop before ऊ."),
               ("जलवूर्मिः", "No व् is inserted after अ.")],
              "च + ऊर्ध्वम् → चोर्ध्वम्; so जल + ऊर्मिः → जलोर्मिः.",
              "अ + ऊ → ओ."),
          "अ or आ before उ or ऊ merges into ओ."),
    ],
}

# ---------------------------------------------------------------- unit 15
AUTHORED["15"] = {
    "title": "तस्मात्पीनकपोलपयोधरता",
    "question": "Which changes does unit 15 name as following from that?",
    "rule": "From that come plumpness of the cheeks and breasts, and blackness of the lips and nipples.",
    "limits": ("Elliptical: no verb is printed or supplied. Whose cheeks and breasts is not stated; the sense is taken as "
               "the bodily changes of pregnancy. What तस्मात् (from that) points back to is not named in the line."),
    "explain_hi": ("यह छोटी गद्य-पंक्ति बिना क्रिया के दो बदलाव गिनाती है। ‘तस्मात्’, यानी उससे: गाल (कपोल) और स्तन (पयोधर) मोटे (पीन) होते हैं, "
                   "और ओंठ (ओष्ठ) और चूचुक काले (कृष्ण) होते हैं। ‘पयोधर’ का शब्दार्थ है दूध धारण करने वाला, यानी स्तन। "
                   "‘-ता’ और ‘-त्व’ भाव बताते हैं: पीनता = मोटापन, कृष्णत्व = कालापन। "
                   "किसके अंग, यह नहीं कहा; अर्थ गर्भ के समय के बदलाव का है।"),
    "hook": "गाल-स्तन पीन, ओंठ-चूचुक कृष्ण।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 15, which parts become plump (पीन)?",
            ("The cheeks and the breasts", "पीनकपोलपयोधरता: plumpness of cheeks and breasts."),
            [("The lips and the nipples", "Those become black (कृष्ण), not plump."),
             ("The hands and the feet", "Hands and feet are not named in this unit."),
             ("The belly and the thighs", "Belly and thighs are not named in this unit.")],
            "Plump: cheeks and breasts; black: lips and nipples.",
            "पीन → कपोल, पयोधर."),
        order(1, "Put the body parts of unit 15 in their printed order.",
              ["कपोल", "पयोधर", "ओष्ठ", "चूचुक"],
              "The plump pair (cheeks, breasts) comes first, then the black pair (lips, nipples).",
              "कपोल → पयोधर → ओष्ठ → चूचुक."),
        T(match(2, "Match each word of unit 15 to its meaning on the card.",
                [["पीन", "plump"], ["कपोल", "cheek"], ["पयोधर", "breast"], ["कृष्ण", "black"], ["चूचुक", "nipple"]],
                "Two qualities (plump, black) and the parts they qualify.",
                "पीन, कपोल, पयोधर, कृष्ण, चूचुक.", role="extend"),
          "पयोधर literally means 'milk-bearer', a word for the breast."),
        mcq("discriminate", 3, "Which pairing of change and part does unit 15 state?",
            ("Black lips, plump cheeks", "कृष्णौष्ठ: black lips; पीनकपोल: plump cheeks."),
            [("Black cheeks, plump lips", "The qualities are swapped: cheeks are plump, lips black."),
             ("Plump nipples, black breasts", "Swapped: breasts are plump, nipples black."),
             ("Black breasts, plump lips", "Breasts are plump and lips black, not the reverse.")],
            "पीन goes with कपोल and पयोधर; कृष्ण goes with ओष्ठ and चूचुक.",
            "पीन: कपोल, पयोधर · कृष्ण: ओष्ठ, चूचुक."),
        mcq("apply", 4, "Which split of कृष्णौष्ठ is right?",
            ("कृष्ण + ओष्ठ", "अ + ओ → औ (vṛddhi): कृष्ण + ओष्ठ → कृष्णौष्ठ."),
            [("कृष्ण + उष्ठ", "उष्ठ is not a word; the lip is ओष्ठ."),
             ("कृष्णौ + ओष्ठ", "औ + ओ would give कृष्णावोष्ठ."),
             ("कृष्णम् + ओष्ठ", "म् before ओ would give कृष्णमोष्ठ.")],
            "कृष्ण (black) + ओष्ठ (lip): अ + ओ merges into औ.",
            "अ/आ + ओ/औ → औ."),
        T(mcq("transfer", 5, "Like पीनता (plumpness) in unit 15, what does मधुरता mean?",
              ("Sweetness, the state of being sweet", "-ता makes a noun of state: मधुर → मधुरता."),
              [("A sweet thing to eat", "-ता names the state, not a thing."),
               ("Very sweet indeed", "-ता is no word of degree."),
               ("Making a thing sweet", "-ता names a state, not an action.")],
              "पीन (plump) → पीनता (plumpness); मधुर (sweet) → मधुरता (sweetness).",
              "-ता / -त्व after a word = the state of being that."),
          "-ता (f.) and -त्व (n.) make nouns of state: पीनता, कृष्णत्व."),
    ],
}

# ---------------------------------------------------------------- unit 16
AUTHORED["16"] = {
    "title": "स्तनाश्रयमेव च",
    "question": "What does unit 16 say happens, in her who has given birth, to that which rests in the breasts?",
    "rule": ("That which rests in the breasts, having reached the state of breast-milk (stanya) in her who has given birth, "
             "is nourished again by the rasa (nutrient juice) of food."),
    "limits": ("Low confidence. The subject is not stated (probably the blood of unit 14, not asserted). The damaged word "
               "केंफोपतरंजितं is read by conjecture as 'tinged with Kapha'; no question rests on it. "
               "stanya = breast milk is standard."),
    "explain_hi": ("इस पंक्ति का कर्ता नहीं छपा; सम्भवतः इकाई १४ का रक्त, पर यह पक्का नहीं। जो स्तनों में ही आश्रय पाता है, वह प्रसूता "
                   "(जिसने जन्म दिया) में स्तन्य, यानी दूध, की अवस्था को प्राप्त होता है। फिर वह आहार के रस (पोषक द्रव) से पुष्ट होता है। "
                   "बीच का शब्द ‘केंफोपतरंजितं’ बिगड़ा हुआ है; अनुमान से ‘कफ से रंजित’ पढ़ा गया है, इसलिए उस पर कोई प्रश्न नहीं।"),
    "hook": "स्तन में ठहरा, दूध बना, आहार-रस से फिर पुष्ट।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 16, by what is it nourished again?",
            ("By the rasa (nutrient juice) of food", "पुनराहाररसेनाप्यायते: nourished again by food-rasa."),
            [("By medicated ghee given daily", "No ghee is named in this unit."),
             ("By the blood of the embryo", "The embryo's blood is not named here."),
             ("By water drunk at night", "No water or time of day is named.")],
            "It is nourished again by the rasa of food (आहाररसेन).",
            "आहाररस = the nutrient juice of food."),
        order(1, "Put these phrases of unit 16 in their printed order (the damaged word left out).",
              ["स्तनाश्रयमेव च", "स्तन्यतामुपगतम्", "प्रसूतायाः", "पुनराहाररसेनाप्यायते"],
              "Resting in the breasts, reaching the state of milk, in her who has given birth, nourished again by food-rasa.",
              "स्तनाश्रय → स्तन्यता उपगत → प्रसूतायाः → आहाररसेन आप्यायते."),
        T(match(2, "Match each word of unit 16 to its meaning on the card.",
                [["स्तनाश्रय", "resting in the breasts"], ["स्तन्य", "breast milk"], ["प्रसूता", "she who has given birth"],
                 ["पुनर्", "again"], ["आप्यायते", "is nourished"]],
                "Five sure words of the line; the damaged word is left out.",
                "स्तनाश्रय, स्तन्य, प्रसूता, पुनर्, आप्यायते.", role="extend"),
          "स्तन्य is breast milk (standard identification); स्तन्यता is the state of being milk."),
        mcq("discriminate", 3, "Which split of पुनराहार is right?",
            ("पुनर् + आहार", "पुनर् ends in र्, which joins the following vowel."),
            [("पुन + राहार", "पुन and राहार are not the card's words."),
             ("पुना + आहार", "पुना is not a word; the word is पुनर्."),
             ("पुनरा + हार", "पुनरा is not a word; the food is आहार.")],
            "पुनर् (again) + आहार (food): the र् is kept before the vowel.",
            "पुनर् + vowel → पुनर् joined to it."),
        mcq("apply", 4, "In unit 16, what does प्रसूतायाः tell us?",
            ("Of her who has given birth", "प्रसूतायाः: f. gen. sg., 'of her who has given birth'."),
            [("Of the embryo in the womb", "The embryo is not named in this unit."),
             ("Of a woman before conception", "प्रसूता means one who has already given birth."),
             ("Of the nurse who feeds the child", "No nurse is named in this unit.")],
            "The milk-state is reached in her who has given birth (प्रसूता).",
            "प्रसूता = she who has given birth."),
        T(mcq("transfer", 5, "Like प्रसूतायाः (of her who has given birth), what does बालायाः mean?",
              ("Of the girl", "-आयाः of an आ-stem feminine is the genitive singular here."),
              [("The girls (as subject)", "That would be बालाः."),
               ("By the girl", "That would be बालया."),
               ("In the girl", "That would be बालायाम्.")],
              "प्रसूता → प्रसूतायाः (of her); बाला → बालायाः (of the girl).",
              "आ-stem feminine: -आयाः = of (genitive singular)."),
          "Feminine आ-stems take -आयाः in the genitive singular: प्रसूता → प्रसूतायाः."),
    ],
}

# ---------------------------------------------------------------- unit 17
AUTHORED["17"] = {
    "title": "तत्र प्रथमे मासे",
    "question": "What does unit 17 say arises in the first month?",
    "rule": "Of these (months), in the first month a kalala arises: the first embryonic mass, probably the early embryo.",
    "limits": ("kalala as zygote or early embryo is a probable equivalent, not exact. The unit names only the first month; "
               "the second and third follow in units 18 and 19."),
    "explain_hi": ("यहाँ से गर्भ का मास-क्रम आरम्भ होता है। ‘तत्र’, यानी उनमें: पहले मास में कलल उत्पन्न होता है। "
                   "कलल गर्भ की पहली अवस्था है, भ्रूण का पहला पिण्ड; आधुनिक अर्थ (आरम्भिक भ्रूण) सम्भावित है, सटीक नहीं। "
                   "‘प्रथमे मासे’ सप्तमी है और समय बताती है: पहले मास में। दूसरा और तीसरा मास इकाई १८ और १९ में आते हैं।"),
    "hook": "पहला मास: कलल।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 17, what arises in the first month?",
            ("A kalala, the first embryonic mass", "प्रथमे मासे कललं जायते."),
            [("A dense mass (घन)", "The ghana is named for the second month (unit 18)."),
             ("The five sprouts", "Sprouting in five ways is the third month (unit 19)."),
             ("A line of hair", "The line of hair appears in unit 14.")],
            "In the first month a kalala arises.",
            "प्रथम मास → कलल."),
        order(1, "Put the words of unit 17 in their printed order.",
              ["तत्र", "प्रथमे", "मासे", "कललम्", "जायते"],
              "Of these, in the first month, a kalala arises.",
              "तत्र → प्रथमे → मासे → कललम् → जायते."),
        T(match(2, "Match each word of unit 17 to its meaning on the card.",
                [["तत्र", "of these, there"], ["प्रथमे", "in the first"], ["मासे", "in the month"],
                 ["कलल", "the first embryonic mass"], ["जायते", "arises"]],
                "Five words: the frame, the time, the thing, the verb.",
                "तत्र, प्रथमे, मासे, कलल, जायते.", role="extend"),
          "कलल is the first stage of the embryo; 'early embryo' is a probable modern equivalent."),
        mcq("discriminate", 3, "Which split of the printed कललंजायते is right?",
            ("कललम् + जायते", "Final म् before a consonant is written as anusvāra: कललं जायते."),
            [("कलल + अंजायते", "अंजायते is not a word."),
             ("कलला + जायते", "कलला is not the card's word; it is कललम्."),
             ("कललः + अजायते", "Neither कललः nor अजायते is the card's form.")],
            "कललम् (kalala, nom.) + जायते (arises); the print runs them together.",
            "म् + consonant → ं (anusvāra)."),
        mcq("apply", 4, "In unit 17, what does the locative प्रथमे मासे tell?",
            ("When it arises: in the first month", "The locative gives the time: in the first month."),
            [("What arises: the first month", "What arises is the kalala, not the month."),
             ("From where: out of the month", "A source would need the ablative."),
             ("Whose: belonging to the first month", "Possession would need the genitive.")],
            "प्रथमे मासे (locative) = in the first month: the time of arising.",
            "Locative of time = in, at, during."),
        T(mcq("transfer", 5, "Built like प्रथमे मासे कललं जायते, what does वसन्ते पुष्पं जायते mean?",
              ("In spring a flower arises", "वसन्ते is a locative of time, like प्रथमे मासे."),
              [("Spring arises from the flower", "पुष्पम् is the subject; वसन्ते is not an object."),
               ("A flower gives rise to spring", "जायते means arises, not gives rise to."),
               ("The flower of spring is born", "वसन्ते is locative, not genitive (वसन्तस्य).")],
              "प्रथमे मासे = in the first month; वसन्ते = in spring.",
              "Locative = the time when; nominative = what arises."),
          "A locative noun gives the time: in the first month, in spring."),
    ],
}

# ---------------------------------------------------------------- unit 18
AUTHORED["18"] = {
    "title": "द्वितीये घनः पेश्यर्बुदं वा",
    "question": "What three forms does unit 18 name for the second month, and with what does it link them?",
    "rule": ("In the second month: a dense mass (ghana), or a peśī (muscle-like lump), or an arbuda (lump); from these, "
             "in order (kramāt), males, females and neuters."),
    "limits": ("No verb is printed or supplied. Which form goes with which sex is left to the word क्रमात् (in order); "
               "the unit does not spell out the pairing, so no question rests on it. napuṃsaka is kept as 'neuter'."),
    "explain_hi": ("दूसरे मास में तीन में से एक रूप कहा गया है: घन (ठोस पिण्ड), पेशी (मांस-पेशी जैसा टुकड़ा) या अर्बुद (गाँठ)। "
                   "फिर ‘तेभ्यः क्रमात्’: उनसे, क्रम से, पुरुष, स्त्री और नपुंसक। "
                   "कौन-सा रूप किससे जुड़ता है, यह केवल ‘क्रमात्’ पर छोड़ा गया है; पंक्ति इसे खोलकर नहीं कहती। "
                   "पंक्ति में कोई क्रिया नहीं छपी।"),
    "hook": "दूसरा मास: घन, पेशी या अर्बुद।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "With which month does unit 18 name the ghana, peśī or arbuda?",
            ("The second month", "द्वितीये: in the second (month)."),
            [("The first month", "The first month has the kalala (unit 17)."),
             ("The third month", "The third month has the five sprouts (unit 19)."),
             ("The fourth month", "No fourth month is named in this unit.")],
            "द्वितीये (in the second) opens the unit.",
            "द्वितीय मास → घन, पेशी या अर्बुद."),
        order(1, "Put these words of unit 18 in their printed order.",
              ["द्वितीये", "घनः", "पेश्यर्बुदं वा", "तेभ्यः", "क्रमात्", "पुंस्त्रीनपुंसकानि"],
              "The month, the three forms, then 'from these, in order', then the three sexes.",
              "द्वितीये → घनः → पेशी/अर्बुदम् वा → तेभ्यः → क्रमात् → पुम्-स्त्री-नपुंसक."),
        T(match(2, "Match each word of unit 18 to its meaning on the card.",
                [["घन", "dense mass"], ["पेशी", "muscle-like lump"], ["अर्बुद", "lump, swelling"],
                 ["वा", "or"], ["क्रमात्", "in order, respectively"]],
                "Three forms joined by 'or', and the order word that links them to the sexes.",
                "घन, पेशी, अर्बुद, वा, क्रमात्.", role="extend"),
          "क्रमात् = in order, respectively: it links two lists item by item without spelling the pairs out."),
        mcq("discriminate", 3, "Which split of पेश्यर्बुदम् is right?",
            ("पेशी + अर्बुदम्", "ई + अ → य्: पेशी + अर्बुदम् → पेश्यर्बुदम्."),
            [("पेश्य + अर्बुदम्", "अ + अ would give पेश्यार्बुदम्."),
             ("पेशे + अर्बुदम्", "ए + अ would give पेशेऽर्बुदम्."),
             ("पेश् + यर्बुदम्", "यर्बुदम् is not a word.")],
            "पेशी (muscle-like lump) + अर्बुदम् (lump): ई before अ becomes य्.",
            "इ/ई + a different vowel → य् + that vowel."),
        multi("apply", 4, "Which are true of unit 18?",
              [("It names the second month", "Right: द्वितीये."),
               ("It joins the three forms with वा (or)", "Right: घनः पेशी अर्बुदं वा."),
               ("It spells out which form becomes male", "The pairing is left to क्रमात्; it is not spelled out."),
               ("It has a printed verb such as 'arises'", "No verb is printed in this unit.")],
              [0, 1],
              "The unit names the month and three forms joined by वा; it has no verb and spells out no pairing.",
              "द्वितीये; घनः पेश्यर्बुदं वा; क्रमात्."),
        T(mcq("transfer", 5, "By the rule of पेश्यर्बुदम्, how is नदी + अस्ति written when joined?",
              ("नद्यस्ति", "ई + अ → य्, as in पेशी + अर्बुदम् → पेश्यर्बुदम्."),
              [("नदास्ति", "The ई does not drop before अ."),
               ("नद्यास्ति", "The अ stays short; ई + अ gives य, not या."),
               ("नदेस्ति", "ई + अ does not give ए.")],
              "पेशी + अर्बुदम् → पेश्यर्बुदम्; so नदी + अस्ति → नद्यस्ति.",
              "ई + अ → य."),
          "इ or ई before a different vowel becomes य्."),
    ],
}

# ---------------------------------------------------------------- unit 19
AUTHORED["19"] = {
    "title": "तृतीये पञ्चधा प्ररोहति",
    "question": "What does unit 19 say happens in the third month?",
    "rule": "In the third month it (the embryo, understood) sprouts in five ways.",
    "limits": ("The subject 'it' is not printed; the card takes it as the embryo. The five are not named here; "
               "unit 21 lists them, after the formula तद्यथा (namely) of unit 20."),
    "explain_hi": ("तीसरे मास में वह (गर्भ, जो छपा नहीं, समझा गया) पाँच प्रकार से अंकुरित होता है। "
                   "‘पञ्चधा’ यानी पाँच प्रकार से; ‘-धा’ प्रत्यय प्रकार बताता है। ‘प्ररोहति’ पौधे के अंकुर निकलने जैसा शब्द है। "
                   "पाँच कौन-से हैं, यह इकाई २१ बताती है; इकाई २० का ‘तद्यथा’ (जैसे कि) उन्हें जोड़ता है।"),
    "hook": "तीसरा मास: पाँच अंकुर।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 19, in which month does it sprout in five ways?",
            ("The third month", "तृतीये: in the third (month)."),
            [("The first month", "The first month has the kalala (unit 17)."),
             ("The second month", "The second month has ghana, peśī or arbuda (unit 18)."),
             ("The fifth month", "No fifth month is named here.")],
            "तृतीये पञ्चधा प्ररोहति: in the third, it sprouts in five ways.",
            "तृतीय मास → पञ्चधा प्ररोह."),
        order(1, "Put the words of unit 19 in their printed order.",
              ["तृतीये", "पंचधा", "प्ररोहति"],
              "The month, the manner, the verb.",
              "तृतीये → पंचधा → प्ररोहति."),
        fill(2, "In unit 19, it sprouts ____ (in five ways). Type it in Devanagari or in English letters (e.g. pancadha).",
             accepts("पञ्चधा"),
             "पञ्चधा (printed पंचधा) = in five ways.",
             "पञ्च (five) + -धा (in … ways) = in five ways.",
             "-धा after a number = in so many ways."),
        mcq("discriminate", 3, "What does पञ्चधा mean in unit 19?",
            ("In five ways", "-धा after a number means 'in so many ways'."),
            [("Five times over", "Five times would be पञ्चकृत्वः."),
             ("The fifth one", "The fifth would be पञ्चम."),
             ("Within five days", "No days are named here.")],
            "पञ्चधा = in five ways (five sprouts).",
            "number + -धा = in that many ways."),
        mcq("apply", 4, "Unit 19 prints no subject for प्ररोहति. Whom does the card take it to be?",
            ("The embryo, understood", "The note: subject 'it' (the embryo) is understood."),
            [("The mother's blood", "The card does not take the blood as subject here."),
             ("The line of hair", "The line of hair belongs to unit 14."),
             ("The breast milk", "Breast milk belongs to unit 16.")],
            "प्ररोहति (it sprouts) has the embryo as its understood subject.",
            "Unstated subject = the embryo."),
        T(mcq("transfer", 5, "तृतीये = in the third (month). How is in the fourth month said?",
              ("चतुर्थे मासे", "Ordinal and noun both in the locative, like तृतीये (मासे)."),
              [("चतुर्थः मासः", "That is the nominative: the fourth month (as subject)."),
               ("चतुर्धा मासे", "चतुर्धा means in four ways, not fourth."),
               ("चतुर्थस्य मासस्य", "That is the genitive: of the fourth month.")],
              "प्रथमे, द्वितीये, तृतीये (मासे); so चतुर्थे मासे = in the fourth month.",
              "Ordinal + मासे in the locative = in the Nth month."),
          "Ordinals agree with मास in the locative to give the month: तृतीये मासे."),
    ],
}

# ---------------------------------------------------------------- unit 20
AUTHORED["20"] = {
    "title": "तद्यथा",
    "question": "What does the formula तद्यथा of unit 20 do?",
    "rule": "तद्यथा (tat + yathā), 'namely', is a stock formula that introduces a list: here the five sprouts named in unit 21.",
    "limits": "The unit is the formula alone and has no content of its own; the list it introduces is in unit 21.",
    "explain_hi": ("‘तद्यथा’ एक स्थिर सूत्र-शब्द है: ‘वह जैसे कि’, यानी ‘अर्थात्’ या ‘जैसे’। यह आगे आने वाली सूची का परिचय देता है। "
                   "यहाँ वह सूची इकाई २१ में है: तीसरे मास के पाँच अंकुर (इकाई १९)। "
                   "सन्धि: तत् + यथा; त् घोष अक्षर य से पहले द् बन जाता है, इसलिए ‘तद्यथा’।"),
    "hook": "तद्यथा: अब सूची आती है।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What does तद्यथा (unit 20) mean?",
            ("Namely", "तत् + यथा: 'that, as', i.e. namely."),
            [("Therefore", "Therefore would be तस्मात् (unit 15)."),
             ("Otherwise", "Otherwise is अन्यथा (unit 24)."),
             ("Simultaneously", "Simultaneously is युगपत् (unit 22).")],
            "तद्यथा = namely: it opens a list.",
            "तद्यथा = namely."),
        order(1, "Put the steps that form तद्यथा in order.",
              ["तत् + यथा", "त् stands before the voiced य", "त् becomes द्", "तद्यथा"],
              "The two words meet; the voiced य turns त् into द्; the joined form results.",
              "तत् + यथा → त् before voiced य → द् → तद्यथा."),
        fill(2, "The formula meaning 'namely' in unit 20 is ____ (one joined word). Type it in Devanagari or in English letters (e.g. tadyatha).",
             accepts("तद्यथा"),
             "तद्यथा = तत् + यथा, namely.",
             "तत् + यथा → तद्यथा: a stock formula that opens a list.",
             "तत् + य → तद्य."),
        mcq("discriminate", 3, "Which split of तद्यथा is right?",
            ("तत् + यथा", "त् before the voiced य becomes द्."),
            [("तद् + अयथा", "That would join as तदयथा."),
             ("तदा + यथा", "तदा + यथा would stay तदा यथा."),
             ("तद्य + था", "तद्य and था are not the card's words.")],
            "तत् (that) + यथा (as, namely).",
            "त् + voiced consonant → द्."),
        mcq("apply", 4, "In this chapter, what does तद्यथा (unit 20) introduce?",
            ("The list of the five sprouts", "Unit 21 lists the two thighs, two arms and head."),
            [("The list of the first three months", "The months come before, in units 17 to 19."),
             ("The list of the plump body parts", "Those were named before, in unit 15."),
             ("The list of things born after birth", "Teeth and the rest are named in unit 22.")],
            "तद्यथा opens the list of the five sprouts of unit 19, given in unit 21.",
            "तद्यथा → the list that follows."),
        T(mcq("transfer", 5, "By the rule of तद्यथा, how is तत् + वनम् written when joined?",
              ("तद्वनम्", "त् before the voiced व becomes द्."),
              [("तन्वनम्", "त् becomes न् only before a nasal."),
               ("तच्वनम्", "त् becomes च् only before च/छ."),
               ("तत्वनम्", "Before the voiced व the त् must become द्.")],
              "तत् + यथा → तद्यथा; so तत् + वनम् → तद्वनम्.",
              "त् + voiced consonant → द्."),
          "A final त् becomes द् before a voiced sound (vowel or voiced consonant)."),
    ],
}

# ---------------------------------------------------------------- unit 21
AUTHORED["21"] = {
    "title": "सक्थिनी बाहू शिरश्च",
    "question": "Which five sprouts does unit 21 list?",
    "rule": "The five sprouts of the third month are: the two thighs (legs), the two arms and the head.",
    "limits": "No verb is printed; the line is the list announced in unit 19 and opened by तद्यथा (unit 20). सक्थि is thigh, also used for the leg.",
    "explain_hi": ("यह इकाई १९ के पाँच अंकुरों की सूची है: दोनों सक्थि (जाँघें या टाँगें), दोनों बाहु और सिर; दो, दो और एक, कुल पाँच। "
                   "‘सक्थिनी’ और ‘बाहू’ द्विवचन हैं, ‘शिरः’ एकवचन। "
                   "सन्धि: शिरः + च → शिरश्च (विसर्ग च से पहले श् बनता है)। पंक्ति में कोई क्रिया नहीं।"),
    "hook": "दो टाँगें, दो बाहें, एक सिर: पाँच अंकुर।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "Unit 21 names the five sprouts. Which list is it?",
            ("Two thighs, two arms and the head", "सक्थिनी बाहू शिरश्च."),
            [("Two eyes, two ears and the nose", "Eyes, ears and nose are not named here."),
             ("Two hands, two feet and the heart", "The heart is not named; the list is thighs, arms, head."),
             ("Two thighs, two arms and the belly", "The fifth is the head (शिरः), not the belly.")],
            "Two thighs (legs), two arms and the head make the five.",
            "सक्थिनी (2) + बाहू (2) + शिरः (1)."),
        order(1, "Put the five sprouts of unit 21 in their printed order.",
              ["सक्थिनी", "बाहू", "शिरश्च"],
              "Thighs first, then arms, then the head.",
              "सक्थिनी → बाहू → शिरः."),
        T(match(2, "Match each word of unit 21 to its meaning on the card.",
                [["सक्थिनी", "the two thighs (legs)"], ["बाहू", "the two arms"], ["शिरः", "head"], ["च", "and"]],
                "Three body words and the joining 'and'.",
                "सक्थिनी, बाहू, शिरः, च.", role="extend"),
          "सक्थिनी is the neuter dual of सक्थि (thigh); बाहू is the dual of बाहु (arm)."),
        mcq("discriminate", 3, "Which split of शिरश्च is right?",
            ("शिरः + च", "Visarga before च becomes श्: शिरश्च."),
            [("शिर + श्च", "श्च is not a word."),
             ("शिरस् + श्च", "श्च is not a word; the word is च."),
             ("शिरा + च", "शिरा would mean a vein; the word is शिरः, head.")],
            "शिरः (head) + च (and).",
            "Visarga + च/छ → श्."),
        mcq("apply", 4, "Which two words of unit 21 are dual (a pair)?",
            ("सक्थिनी and बाहू", "Both are nom. dual: the two thighs, the two arms."),
            [("बाहू and शिरः", "शिरः is singular: one head."),
             ("सक्थिनी and शिरः", "शिरः is singular."),
             ("शिरः and च", "च is an indeclinable, 'and'.")],
            "सक्थिनी (n. du.) and बाहू (m. du.) are duals; शिरः is singular.",
            "Dual: सक्थिनी, बाहू · singular: शिरः."),
        T(mcq("transfer", 5, "By the rule of शिरश्च, how is रामः + च written when joined?",
              ("रामश्च", "Visarga before च becomes श्."),
              [("रामोच", "Visarga becomes ओ only before a voiced sound."),
               ("रामस्च", "Before च the sibilant is श्, not स्."),
               ("रामच्च", "Visarga does not become च्.")],
              "शिरः + च → शिरश्च; so रामः + च → रामश्च.",
              "Visarga + च → श्च."),
          "A visarga before च or छ becomes श्."),
    ],
}

# ---------------------------------------------------------------- unit 22
AUTHORED["22"] = {
    "title": "सक्थ्यादिप्ररोहैककालमेव",
    "question": "What does unit 22 say arises at the time of the sprouting, what is excepted, and how they become distinct?",
    "rule": ("At the very time of the sprouting of the thighs and the rest, all the limbs, parts and sense organs (indriya) "
             "come to be simultaneously, except teeth and the rest, born after birth; but in order they become distinct."),
    "limits": ("Who 'they' are in 'in order they become distinct' is left open: all the parts, or only the later-born ones; "
               "no question rests on it. सर्वांगावयवेंद्रियाणि is read as a series of three terms, not a closed compound."),
    "explain_hi": ("जिस समय सक्थि आदि (इकाई २१ के पाँच) अंकुरित होते हैं, उसी समय सब अंग, अवयव और इन्द्रियाँ एक साथ (युगपत्) उत्पन्न होते हैं। "
                   "अपवाद: जन्म के बाद के समय में होने वाले दाँत आदि (अन्यत्र = छोड़कर)। "
                   "‘किन्तु क्रम से (क्रमेण) वे स्पष्ट होते हैं’: ‘वे’ कौन, सब अंग या केवल बाद वाले, यह खुला छोड़ा गया है। "
                   "यानी उत्पत्ति एक साथ, स्पष्टता क्रम से।"),
    "hook": "बनते एक साथ, खिलते क्रम से; दाँत जन्म के बाद।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 22, which are excepted from arising simultaneously?",
            ("Teeth and the rest, born after birth", "अन्यत्र जन्मोत्तरकालजेभ्यो दन्तादिभ्यः."),
            [("The thighs and the arms", "They are the sprouts at whose time all arise."),
             ("The sense organs (indriya)", "The indriyas are among those that arise together."),
             ("The head and the face", "Neither is named as an exception.")],
            "All arise together except those born after birth, the teeth and the rest.",
            "अन्यत्र (except) + दन्तादिभ्यः."),
        order(1, "Put these phrases of unit 22 in their printed order.",
              ["सक्थ्यादिप्ररोहैककालमेव च", "सर्वांगावयवेंद्रियाणि", "युगपत्संभवन्ति", "अन्यत्र जन्मोत्तरकालजेभ्यो",
               "दंतादिभ्यः", "क्रमेण तु स्पष्टीभवंति"],
              "The time, the things that arise, 'together', the exception, the teeth, then 'in order they become distinct'.",
              "एककालम् → सर्वाङ्ग… → युगपत् → अन्यत्र … दन्तादिभ्यः → क्रमेण स्पष्टीभवन्ति."),
        T(match(2, "Match each word of unit 22 to its meaning on the card.",
                [["युगपत्", "simultaneously"], ["अन्यत्र", "except"], ["जन्मोत्तरकालज", "born in the time after birth"],
                 ["क्रमेण", "in order, gradually"], ["स्पष्टीभवन्ति", "become distinct"]],
                "Five words carry the teaching: together, except the later-born, then distinct in order.",
                "युगपत्, अन्यत्र, जन्मोत्तरकालज, क्रमेण, स्पष्टीभवन्ति.", role="extend"),
          "अन्यत्र with an ablative (…भ्यः) means 'except': अन्यत्र दन्तादिभ्यः = except the teeth and the rest."),
        mcq("discriminate", 3, "What contrast does unit 22 draw?",
            ("They arise together, but become distinct in order", "युगपत् सम्भवन्ति … क्रमेण तु स्पष्टीभवन्ति."),
            [("They arise in order, but become distinct together", "This reverses युगपत् and क्रमेण."),
             ("They arise before the sprouts, then vanish", "They arise at the same time as the sprouts."),
             ("Teeth arise first, the limbs come last", "Teeth are the exception, born after birth.")],
            "Arising is simultaneous (युगपत्); becoming distinct is in order (क्रमेण).",
            "युगपत् सम्भव ↔ क्रमेण स्पष्टता."),
        mcq("apply", 4, "Which split of संभवन्त्यन्यत्र is right?",
            ("संभवन्ति + अन्यत्र", "इ + अ → य्: संभवन्त्यन्यत्र."),
            [("संभवन्तु + अन्यत्र", "उ + अ would give संभवन्त्वन्यत्र."),
             ("संभवन्ते + अन्यत्र", "ए + अ would give संभवन्तेऽन्यत्र."),
             ("संभवन्त्यन् + यत्र", "संभवन्त्यन् is not a word.")],
            "संभवन्ति (they come to be) + अन्यत्र (except).",
            "इ + a different vowel → य् + that vowel."),
        T(mcq("transfer", 5, "Built like अन्यत्र दन्तादिभ्यः, what does सर्वे गताः अन्यत्र रामात् mean?",
              ("All went, except Rāma", "अन्यत्र with the ablative रामात् = except Rāma."),
              [("All went with Rāma", "With would need सह and an instrumental."),
               ("All went to Rāma", "To would need an accusative (रामम्)."),
               ("All went elsewhere than Rāma's", "अन्यत्र with an ablative here means except.")],
              "अन्यत्र + ablative = except: अन्यत्र दन्तादिभ्यः, अन्यत्र रामात्.",
              "अन्यत्र + ablative = except X."),
          "अन्यत्र with an ablative noun means 'except that'."),
    ],
}

# ---------------------------------------------------------------- unit 23
AUTHORED["23"] = {
    "title": "एषा प्रकृतिः",
    "question": "What does unit 23 call the course just described?",
    "rule": "This is the prakṛti: the natural, normal state (course).",
    "limits": ("The copula 'is' is understood. Here प्रकृति means the normal course, not body-type or primal matter. "
               "What एषा (this) points back to is not spelled out; it is taken as the course just described."),
    "explain_hi": ("दो शब्दों की यह पंक्ति निर्णय देती है: ‘यह प्रकृति है’, यानी यही स्वाभाविक, सामान्य क्रम है। "
                   "‘है’ समझा जाता है, छपा नहीं। यहाँ प्रकृति का अर्थ शरीर की प्रकृति (देह-स्वभाव) या मूल प्रकृति नहीं, सामान्य क्रम है। "
                   "‘एषा’ स्त्रीलिंग है क्योंकि वह स्त्रीलिंग ‘प्रकृतिः’ से मेल खाती है। अगली इकाई इसका उल्टा, विकृति, बताती है।"),
    "hook": "यही सामान्य क्रम: एषा प्रकृतिः।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What does unit 23 call 'this' (एषा)?",
            ("prakṛti, the normal state", "एषा प्रकृतिः: this is the prakṛti."),
            [("vikṛti, the abnormal state", "vikṛti is named in unit 24, as otherwise than this."),
             ("kalala, the first mass", "kalala is the first month (unit 17)."),
             ("jarāyu, the membrane", "jarāyu is not named here.")],
            "This is the prakṛti, the natural, normal state.",
            "एषा = प्रकृतिः."),
        multi("warmup", 1, "Which are true of unit 23?",
              [("एषा is feminine, agreeing with प्रकृतिः", "Right: both are f. nom. sg."),
               ("No verb is printed; 'is' is understood", "Right: the copula is understood."),
               ("प्रकृतिः is in the accusative", "It is nominative singular."),
               ("It lists five items", "It has only two words and no list.")],
              [0, 1],
              "Two words, both feminine nominative, with 'is' understood.",
              "एषा (f. nom.) + प्रकृतिः (f. nom.) + 'is'."),
        fill(2, "Unit 23: एषा ____ (this is the normal state). Type it in Devanagari or in English letters (e.g. prakriti).",
             accepts("प्रकृतिः", None, "प्रकृति"),
             "एषा प्रकृतिः = this is the prakṛti, the normal state.",
             "प्रकृति here = the natural, normal course.",
             "प्रकृति = normal state; विकृति = deviation."),
        mcq("discriminate", 3, "What does प्रकृति mean in unit 23?",
            ("The natural, normal course", "The note: here prakṛti is the normal course."),
            [("A person's body-type", "The note rules this sense out here."),
             ("Primal matter of the world", "The note rules this sense out here."),
             ("A disease of the embryo", "A deviation would be vikṛti, not prakṛti.")],
            "प्रकृति in unit 23 is the normal course, as against विकृति in unit 24.",
            "प्रकृति (here) = normal course."),
        mcq("apply", 4, "Unit 23 prints no verb. How is एषा प्रकृतिः read?",
            ("With 'is' understood: this is the prakṛti", "A nominal sentence: the copula is understood."),
            [("As a question: is this prakṛti", "Nothing marks a question."),
             ("As an order: make this prakṛti", "No command form is present."),
             ("As 'this belongs to prakṛti'", "That would need a genitive, प्रकृतेः.")],
            "Two nominatives with 'is' understood: this is the prakṛti.",
            "Nominal sentence: X Y = X is Y."),
        T(mcq("transfer", 5, "Like एषा प्रकृतिः, which pronoun goes with नदी (a river, f.) to say: this is the river?",
              ("एषा नदी", "एषा is f. nom. sg., agreeing with the feminine नदी."),
              [("एषः नदी", "एषः is masculine; नदी is feminine."),
               ("एतत् नदी", "एतत् is neuter; नदी is feminine."),
               ("एताम् नदी", "एताम् is accusative; the subject needs the nominative.")],
              "एषा agrees with प्रकृतिः (f.); so एषा नदी.",
              "Pronoun agrees with its noun in gender, case and number."),
          "The pronoun एतद् takes the gender of its noun: एषः (m.), एषा (f.), एतत् (n.)."),
    ],
}

# ---------------------------------------------------------------- unit 24
AUTHORED["24"] = {
    "title": "विकृतिरतोऽन्यथा",
    "question": "What does unit 24 call anything otherwise than this?",
    "rule": "Otherwise than this (the prakṛti of unit 23) is vikṛti: deviation, the abnormal state.",
    "limits": "The copula is understood. The unit names no particular deviation.",
    "explain_hi": ("इकाई २३ ने सामान्य क्रम को प्रकृति कहा; यह पंक्ति कहती है: इससे अन्यथा (अलग) जो हो, वह विकृति, यानी असामान्य अवस्था है। "
                   "‘अतः’ = इससे, ‘अन्यथा’ = अन्य प्रकार से। कौन-सी विकृति, यह यहाँ नहीं बताया। "
                   "सन्धि: विकृतिः + अतः → विकृतिरतः; अतः + अन्यथा → अतोऽन्यथा (अवग्रह ऽ लुप्त अ का चिह्न)।"),
    "hook": "प्रकृति से अन्यथा = विकृति।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What does unit 24 call 'otherwise than this'?",
            ("vikṛti, the abnormal state", "विकृतिः अतः अन्यथा."),
            [("prakṛti, the normal state", "prakṛti is the normal course of unit 23."),
             ("kalala, the first mass", "kalala is the first month's mass (unit 17)."),
             ("stanya, the breast milk", "stanya belongs to unit 16.")],
            "Otherwise than this is vikṛti, deviation.",
            "अतः अन्यथा = विकृतिः."),
        order(1, "Put the three words of unit 24 in their printed order.",
              ["विकृतिः", "अतः", "अन्यथा"],
              "vikṛti, than this, otherwise.",
              "विकृतिः → अतः → अन्यथा."),
        T(match(2, "Match each word of unit 24 to its meaning on the card.",
                [["विकृति", "deviation, abnormal state"], ["अतः", "than this"], ["अन्यथा", "otherwise"]],
                "Three words: the name, the reference point and the difference.",
                "विकृति, अतः, अन्यथा.", role="extend"),
          "अतः (than this) points back to the prakṛti of unit 23."),
        mcq("discriminate", 3, "Which split of विकृतिरतोऽन्यथा is right?",
            ("विकृतिः + अतः + अन्यथा", "इः + vowel → इर्; अः + अ → ओऽ."),
            [("विकृतिः + रतः + अन्यथा", "रतः is not the card's word; the र् is the visarga."),
             ("विकृति + अतः + न्यथा", "न्यथा is not a word; the word is अन्यथा."),
             ("विकृतिर + तो + अन्यथा", "विकृतिर and तो are not words.")],
            "विकृतिः (deviation) + अतः (than this) + अन्यथा (otherwise).",
            "इः + vowel → इर्; अः + अ → ओऽ."),
        mcq("apply", 4, "In अतोऽन्यथा, what does the sign ऽ mark?",
            ("The अ of अन्यथा, dropped after ओ", "अः + अ → ओ, and the lost अ is shown by ऽ."),
            [("A visarga that must be restored", "The visarga became ओ; ऽ marks the lost अ."),
             ("A long vowel to be held", "ऽ marks a dropped अ, not length."),
             ("A damaged letter in the print", "ऽ is a regular sign (avagraha), not damage.")],
            "अतः + अन्यथा → अतोऽन्यथा: ऽ (avagraha) stands for the dropped अ.",
            "अः + अ → ओऽ."),
        T(mcq("transfer", 5, "By the rule of अतोऽन्यथा, how is रामः + अत्र written when joined?",
              ("रामोऽत्र", "अः + अ → ओऽ, as in अतः + अन्यथा."),
              [("रामरत्र", "Visarga → र् only after a vowel other than अ/आ."),
               ("रामा अत्र", "अः + अ does not give आ."),
               ("रामस्त्र", "Visarga → स् only before त/थ.")],
              "अतः + अन्यथा → अतोऽन्यथा; so रामः + अत्र → रामोऽत्र.",
              "अः + अ → ओऽ."),
          "अः before अ becomes ओ and the अ drops, marked by ऽ (avagraha)."),
    ],
}

# ---------------------------------------------------------------- unit 25
AUTHORED["25"] = {
    "title": "यथास्वं च गर्भस्य",
    "question": "What does unit 25 say becomes established in the embryo's mind and body?",
    "rule": ("Each according to its own, the states (bhāva) of the embryo that conform to the sign (liṅga) of one of male, "
             "female or neuter become established in the mind and in the body."),
    "limits": ("The printed अन्यतर्म is uncertain (anyatara 'either of two' or anyatama 'any of many'); no question rests on it. "
               "The unit does not say which states are meant."),
    "explain_hi": ("यह इकाई नया प्रकरण खोलती है: स्त्रीकर, पुरुषकर और नपुंसककर भाव। गर्भ के भाव (अवस्थाएँ, स्वभाव), अपने-अपने अनुसार, "
                   "पुरुष, स्त्री या नपुंसक में से किसी एक के लिंग (चिह्न) के अनुरूप ही होते हैं, और मन में तथा शरीर में स्थित होते हैं। "
                   "कौन-से भाव, यह यहाँ नहीं बताया। छपा ‘अन्यतर्म’ अनिश्चित है (अन्यतर या अन्यतम); दोनों में अर्थ ‘किसी एक’ बनता है।"),
    "hook": "जैसा लिंग, वैसे भाव: मन में भी, शरीर में भी।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 25, where do the states (bhāva) become established?",
            ("In the mind and in the body", "मनसि शरीरे च संतिष्ठन्ते."),
            [("In the blood and the milk", "Blood and milk are not named here."),
             ("In the head alone", "The unit names the mind and the body."),
             ("In the mother's mind", "They are the embryo's states (गर्भस्य).")],
            "The states become established in the mind and in the body.",
            "मनसि शरीरे च."),
        order(1, "Put these phrases of unit 25 in their printed order.",
              ["यथास्वं च", "गर्भस्य", "पुंस्त्रीनपुंसकान्यतर्मलिंगानुरूपा एव", "भावा", "मनसि शरीरे च", "संतिष्ठंते"],
              "Each by its own, of the embryo, conforming to one sex's sign, the states, in mind and body, are established.",
              "यथास्वम् → गर्भस्य → …लिङ्गानुरूपाः एव → भावाः → मनसि शरीरे च → संतिष्ठन्ते."),
        T(match(2, "Match each word of unit 25 to its meaning on the card.",
                [["यथास्वम्", "each according to its own"], ["अनुरूप", "conforming to"], ["भाव", "state, disposition"],
                 ["मनसि", "in the mind"], ["संतिष्ठन्ते", "become established"]],
                "Five sure words of the sentence; the uncertain अन्यतर्म is left out.",
                "यथास्वम्, अनुरूप, भाव, मनसि, संतिष्ठन्ते.", role="extend"),
          "भाव here is a state or disposition; the unit does not say which ones."),
        mcq("discriminate", 3, "By unit 25, to what do the embryo's states conform?",
            ("The sign of one of male, female or neuter", "…लिङ्गानुरूपाः: conforming to the sign (liṅga) of one of them."),
            [("The season in which it was conceived", "No season is named in this unit."),
             ("The food the mother eats", "Food is not named in this unit."),
             ("The month of its growth", "No month is named in this unit.")],
            "The states conform to the liṅga (sign) of one of male, female or neuter.",
            "लिङ्गानुरूप = conforming to the sign."),
        mcq("apply", 4, "In the printed अनुरूपा एव, what happened to अनुरूपाः?",
            ("Its visarga dropped before the vowel ए", "आः + vowel → आ, with the gap kept: अनुरूपा एव."),
            [("It is a feminine singular word", "It is m. nom. pl., agreeing with भावाः."),
             ("It lost its last vowel to एव", "The आ stays; only the visarga goes."),
             ("A word has dropped out of the print", "Nothing is missing; this is regular sandhi.")],
            "अनुरूपाः + एव → अनुरूपा एव: visarga after आ drops before a vowel.",
            "आः + vowel → आ (gap stays)."),
        T(mcq("transfer", 5, "By the rule of अनुरूपा एव, how is बालाः + इह written when joined?",
              ("बाला इह", "आः + vowel → आ, and the two words stay apart."),
              [("बालेह", "The visarga drops first; आ and इ are then not merged."),
               ("बालारिह", "Visarga → र् only after a vowel other than अ/आ."),
               ("बालोऽिह", "ओऽ arises only from अः + अ.")],
              "अनुरूपाः + एव → अनुरूपा एव; so बालाः + इह → बाला इह.",
              "आः + vowel → आ + vowel (no further joining)."),
          "After आ, a visarga drops before a vowel and the vowels are not joined."),
    ],
}

# ===================================================================== NOTES_HI
NOTES_HI = {
    "14": ("छपा ‘प्रादुर्भवतिजरायुशेषं’ = प्रादुर्भवति जरायुशेषम् (छपाई में शब्द जुड़े; निश्चित)। "
           "दूसरा खण्ड दो तरह पढ़ा जा सकता है: ‘असृक् जरायुशेष को जाता है’ (लिया गया) या ‘जरायुशेष रक्त रूप में ऊपर जाता है’। "
           "रोमराजी किसके शरीर पर, नहीं कहा। सन्धियाँ: च + ऊर्ध्वम् → चोर्ध्वम् (अ + ऊ → ओ); ऊर्ध्वम् + असृक् → ऊर्ध्वमसृक्; "
           "प्रादुस् + भवति → प्रादुर्भवति।"),
    "15": ("छपाई में सब शब्द जुड़े हैं: तस्मात् + पीनकपोलपयोधरता + कृष्णौष्ठचूचुकत्वम्। कोई क्रिया नहीं छपी, न जोड़ी गई। "
           "सन्धि: कृष्ण + ओष्ठ → कृष्णौष्ठ (अ + ओ → औ); ओष्ठ के साथ समास में ‘कृष्णोष्ठ’ भी विकल्प से बनता है, छपा रूप औ वाला है। "
           "पयोधर = स्तन, कपोल = गाल, चूचुक = चूचुक (मानक)।"),
    "16": ("विश्वास कम। ‘केंफोपतरंजितं’ बिगड़ा शब्द है; अनुमान से ‘कफोपरञ्जितम्’ (कफ से रंजित) पढ़ा गया है, पाठ अनिश्चित। "
           "कर्ता नहीं छपा (सम्भवतः इकाई १४ का रक्त; कहा नहीं गया)। "
           "सन्धियाँ: स्तनाश्रयम् + एव → स्तनाश्रयमेव; पुनर् + आहार → पुनराहार; आहाररसेन + आप्यायते → आहाररसेनाप्यायते (अ + आ → आ)। "
           "स्तन्य = स्तन का दूध (मानक)।"),
    "17": ("छपा ‘कललंजायते’ = कललम् जायते (म् व्यंजन से पहले अनुस्वार; छपाई में जुड़ा)। "
           "कलल = गर्भ की पहली अवस्था; आधुनिक अर्थ (आरम्भिक भ्रूण) सम्भावित, सटीक नहीं।"),
    "18": ("कोई क्रिया नहीं छपी। घन, पेशी, अर्बुद की पुरुष, स्त्री, नपुंसक से जोड़ी केवल ‘क्रमात्’ पर छोड़ी गई है; पंक्ति इसे नहीं खोलती। "
           "सन्धियाँ: पेशी + अर्बुदम् → पेश्यर्बुदम् (ई + अ → य); क्रमात् + पुम् → क्रमात्पुम्।"),
    "19": ("कर्ता ‘वह’ (गर्भ) समझा गया है। छपा ‘पंचधा’ = पञ्चधा (अनुस्वार और ञ् एक ही)। पाँच अंकुर इकाई २१ में गिनाए गए हैं।"),
    "20": ("स्थिर सूत्र ‘तद् यथा’ = जैसे कि; इकाई २१ की सूची का परिचय। सन्धि: तत् + यथा → तद्यथा (त् घोष य से पहले द्)। "
           "यही सूत्र इकाई २७ में भी आता है।"),
    "21": ("इकाई १९ के पाँच अंकुरों की सूची: दो सक्थि, दो बाहु, सिर। सक्थि = जाँघ, टाँग के लिए भी। कोई क्रिया नहीं। "
           "सन्धि: शिरः + च → शिरश्च (विसर्ग + च → श्च)।"),
    "22": ("‘क्रमेण तु स्पष्टीभवन्ति’ का कर्ता खुला: सब अंग या केवल जन्म के बाद वाले। ‘सर्वांगावयवेंद्रियाणि’ को तीन शब्दों की शृंखला पढ़ा गया। "
           "सन्धियाँ: सक्थि + आदि → सक्थ्यादि; प्ररोह + एक → प्ररोहैक (अ + ए → ऐ); सर्व + अङ्ग → सर्वाङ्ग; अवयव + इन्द्रियाणि → अवयवेन्द्रियाणि (अ + इ → ए); "
           "सम्भवन्ति + अन्यत्र → सम्भवन्त्यन्यत्र; जन्म + उत्तर → जन्मोत्तर; -जेभ्यः + दन्त → -जेभ्यो दन्त (अः + घोष → ओ)।"),
    "23": ("‘है’ समझा जाता है। यहाँ प्रकृति = सामान्य क्रम (इकाई २४ की विकृति के विपरीत), देह-प्रकृति या मूल प्रकृति नहीं।"),
    "24": ("‘है’ समझा जाता है। छपा ‘विकृतिरतोऽन्यथा’ = विकृतिः + अतः + अन्यथा। "
           "सन्धियाँ: इः + अ → इर्: विकृतिरतः; अः + अ → ओऽ: अतोऽन्यथा।"),
    "25": ("छपा ‘अन्यतर्म’ अनिश्चित: अन्यतर (दो में से एक) या अन्यतम (अनेक में से एक); तीन लिंगों के लिए अन्यतम अपेक्षित। "
           "‘अनुरूपा एव’ = अनुरूपाः + एव (आः + स्वर → आ), सही सन्धि। ‘भावा मनसि’ के लिए डेटा ‘भावाः’ सुझाता है; "
           "पर आः के बाद घोष म से पहले विसर्ग का लोप नियमित है, इसलिए छपा ‘भावा’ भी ठीक सन्धि है। "
           "छपा ‘यथास्वंच’ = यथास्वम् च। कौन-से भाव, नहीं कहा।"),
}

# ===================================================================== AIDS
AIDS = {
    "14": {
        "chain": {"steps": ["रक्त स्थिर हुआ", "रोमराजी प्रकट होती है", "असृक् ऊपर जाता है", "जरायु-शेष को प्राप्त"]},
        "sandhi": ("अ + ऊ → ओ: च + ऊर्ध्वम् → चोर्ध्वम् · म् + स्वर: ऊर्ध्वम् + असृक् → ऊर्ध्वमसृक् · "
                   "उस् + भ → उर्भ: प्रादुस् + भवति → प्रादुर्भवति।"),
        "anchors": "रक्त = असृक्: एक ही पंक्ति में दोनों नाम (रक्ते … असृक्)।",
    },
    "15": {
        "diagram": {"groups": [
            {"label": "पीन (मोटे)", "items": ["कपोल (गाल)", "पयोधर (स्तन)"]},
            {"label": "कृष्ण (काले)", "items": ["ओष्ठ (ओंठ)", "चूचुक"]}]},
        "sandhi": "अ + ओ → औ: कृष्ण + ओष्ठ → कृष्णौष्ठ · त् + प: तस्मात् + पीन → तस्मात्पीन (बदलाव नहीं)।",
        "letters": "क-प पीन, ओ-चू कृष्ण: पहले दो मोटे, बाद के दो काले (मेरी याद-पद्धति)।",
    },
    "16": {
        "chain": {"steps": ["स्तनों में आश्रय", "प्रसूता में स्तन्य (दूध) बनता", "आहार-रस से फिर पुष्ट"]},
        "sandhi": "अ + आ → आ: आहाररसेन + आप्यायते → आहाररसेनाप्यायते · र् + स्वर: पुनर् + आहार → पुनराहार · म् + उ: स्तन्यताम् + उपगतम् → स्तन्यतामुपगतम्।",
        "frame": "कर्ता छपा नहीं; बीच का शब्द बिगड़ा (कफ से रंजित?, अनुमान)। पक्का: स्तन → दूध → आहार-रस से पोषण।",
    },
    "17": {
        "frame": "तत्र (उनमें, मासों में) → प्रथमे मासे (पहले मास में) → कललम् जायते (कलल बनता है)।",
        "anchors": "मास-क्रम आरम्भ: १ कलल · २ घन/पेशी/अर्बुद · ३ पाँच अंकुर (इकाई १७-१९)।",
        "sandhi": "म् + ज → ं: कललम् + जायते → कललं जायते (छपाई में जुड़ा)।",
    },
    "18": {
        "diagram": {"groups": [
            {"label": "दूसरे मास के रूप (वा)", "items": ["घन", "पेशी", "अर्बुद"]},
            {"label": "तेभ्यः क्रमात्", "items": ["पुरुष", "स्त्री", "नपुंसक"]}]},
        "sandhi": "ई + अ → य: पेशी + अर्बुदम् → पेश्यर्बुदम् · त् + प: क्रमात् + पुम् → क्रमात्पुम्।",
        "frame": "द्वितीये (दूसरे में) → घनः, पेशी, अर्बुदम् वा → तेभ्यः क्रमात् (उनसे क्रम से) → पुम्-स्त्री-नपुंसकानि। जोड़ी खोलकर नहीं कही।",
    },
    "19": {
        "frame": "तृतीये (तीसरे मास में) → पञ्चधा (पाँच प्रकार से) → प्ररोहति (अंकुरित होता है); पाँच कौन, इकाई २१।",
        "puns": "मेरी बनाई, केवल सुनने की सहायता: ‘पञ्च-धा’ = ‘पाँच धाराएँ’ जैसी, पाँच दिशाओं में अंकुर।",
    },
    "20": {
        "sandhi": "त् + य → द्य: तत् + यथा → तद्यथा (घोष य से पहले त् → द्)।",
        "frame": "तद्यथा = ‘जैसे कि’: इकाई १९ (पाँच प्रकार से) → इकाई २० (तद्यथा) → इकाई २१ (सूची)।",
    },
    "21": {
        "diagram": {"groups": [
            {"label": "पाँच अंकुर", "items": ["सक्थिनी (दो जाँघें)", "बाहू (दो बाहें)", "शिरः (सिर)"]}]},
        "sandhi": "विसर्ग + च → श्च: शिरः + च → शिरश्च।",
        "pegs": "मेरा बनाया चित्र: एक तारे के पाँच कोने: नीचे दो टाँगें, बगल में दो बाहें, ऊपर सिर। (केवल याद के लिए)",
    },
    "22": {
        "seesaw": "युगपत् सम्भवन्ति (एक साथ उत्पन्न) ↔ क्रमेण स्पष्टीभवन्ति (क्रम से स्पष्ट)।",
        "chain": {"steps": ["सक्थि आदि के अंकुरण का समय", "सब अंग, अवयव, इन्द्रियाँ एक साथ", "अपवाद: जन्म के बाद के दाँत आदि",
                            "पर क्रम से स्पष्ट"]},
        "sandhi": ("इ + अ → य: सम्भवन्ति + अन्यत्र → सम्भवन्त्यन्यत्र · अ + उ → ओ: जन्म + उत्तर → जन्मोत्तर · "
                   "अ + ए → ऐ: प्ररोह + एक → प्ररोहैक · अः + द → ओ द: -जेभ्यः + दन्त → -जेभ्यो दन्त।"),
        "chunks": "सक्थ्यादिप्ररोहैककालमेव च | सर्वांगावयवेंद्रियाणि | युगपत्संभवन्ति | अन्यत्र जन्मोत्तरकालजेभ्यो दंतादिभ्यः | क्रमेण तु स्पष्टीभवंति।",
    },
    "23": {
        "frame": "एषा (यह, स्त्रीलिंग) + प्रकृतिः (सामान्य क्रम) + ‘है’ समझा जाता।",
        "anchors": "प्रकृति (इकाई २३) ↔ विकृति (इकाई २४): ‘प्र’ = पहले वाला सामान्य, ‘वि’ = विपरीत (मेरी याद-पद्धति)।",
    },
    "24": {
        "contrast": "प्रकृति (इकाई २३): सामान्य, स्वाभाविक क्रम ↔ विकृति (इकाई २४): इससे अन्यथा, असामान्य अवस्था।",
        "sandhi": "इः + अ → इर्: विकृतिः + अतः → विकृतिरतः · अः + अ → ओऽ: अतः + अन्यथा → अतोऽन्यथा।",
    },
    "25": {
        "chain": {"steps": ["गर्भ का लिंग: पुरुष, स्त्री या नपुंसक में से एक", "उसके अनुरूप ही भाव", "यथास्वम् (अपने-अपने अनुसार)",
                            "मन में और शरीर में स्थित"]},
        "sandhi": "आः + स्वर → आ: अनुरूपाः + एव → अनुरूपा एव · आः + म → आ म: भावाः + मनसि → भावा मनसि · म् + च: यथास्वम् + च → यथास्वं च।",
        "frame": "नया प्रकरण: स्त्रीकर, पुरुषकर, नपुंसककर भाव। कौन-से भाव, अभी नहीं बताया।",
    },
}

# ===================================================================== IMAGE_SPECS
IMAGE_SPECS = {
    ("14", "chain"): {
        "file": "sh2-romaraji-14.svg",
        "alt": ("Chain of unit 14: the blood settles; a line of hair (romaraji) appears; the blood (asrk) goes upward; "
                "it reaches the remainder of the jarayu (one reading of an ambiguous clause)."),
        "type": "chain",
        "title": "इकाई १४: रक्त स्थिर होने पर",
        "steps": ["रक्त स्थिर हुआ", "रोमराजी प्रकट होती है", "असृक् ऊपर जाता है", "जरायु-शेष को प्राप्त"],
    },
    ("15", "diagram"): {
        "file": "sh2-pina-krishna-15.svg",
        "alt": ("Mind map of unit 15: from that, plumpness of two parts (cheeks, breasts) and blackness of two parts "
                "(lips, nipples)."),
        "type": "mermaid",
        "code": ("mindmap\n"
                 "  तस्मात्: उससे\n"
                 "    पीनता: मोटापन\n"
                 "      कपोल: गाल\n"
                 "      पयोधर: स्तन\n"
                 "    कृष्णत्व: कालापन\n"
                 "      ओष्ठ: ओंठ\n"
                 "      चूचुक\n"),
    },
    ("18", "diagram"): {
        "file": "sh2-ghana-peshi-arbuda-18.svg",
        "alt": ("Two lists of unit 18 in printed order: the forms of the second month (ghana, peshi or arbuda), and "
                "'from these, in order' (male, female, neuter); the pairing is not spelled out."),
        "type": "split",
        "title": "दूसरा मास (इकाई १८): जोड़ी केवल ‘क्रमात्’",
        "cols": [["दूसरे मास के रूप (वा)", ["घन", "पेशी", "अर्बुद"]],
                 ["तेभ्यः क्रमात्", ["पुरुष", "स्त्री", "नपुंसक"]]],
    },
    ("21", "diagram"): {
        "file": "sh2-pancha-praroha-21.svg",
        "alt": "Mind map of unit 21: the five sprouts of the third month: two thighs (legs), two arms and the head.",
        "type": "mermaid",
        "code": ("mindmap\n"
                 "  पाँच अंकुर\n"
                 "    सक्थिनी = दो जाँघें\n"
                 "    बाहू = दो बाहें\n"
                 "    शिरः = सिर\n"),
    },
    ("22", "chain"): {
        "file": "sh2-yugapat-krama-22.svg",
        "alt": ("Flowchart of unit 22: at the time of the sprouting of the thighs and the rest, all limbs, parts and sense "
                "organs arise together, except teeth and the rest born after birth; but in order they become distinct."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"सक्थि आदि का<br/>अंकुरण-काल\"] --> B[\"सब अंग, अवयव,<br/>इन्द्रियाँ: एक साथ\"]\n"
                 "  B -.- X[\"अपवाद: दाँत आदि<br/>जन्म के बाद\"]\n"
                 "  B --> C[\"पर क्रम से<br/>स्पष्ट होते\"]\n"),
    },
    ("24", "contrast"): {
        "file": "sh2-prakriti-vikriti-24.svg",
        "alt": "Split of units 23 and 24: prakrti, the natural normal course, against vikrti, otherwise than this, the abnormal state.",
        "type": "split",
        "title": "प्रकृति और विकृति (इकाई २३-२४)",
        "cols": [["प्रकृति (एषा)", ["स्वाभाविक, सामान्य क्रम"]],
                 ["विकृति (अतोऽन्यथा)", ["इससे अन्यथा", "असामान्य अवस्था"]]],
    },
    ("25", "chain"): {
        "file": "sh2-linga-bhava-25.svg",
        "alt": ("Flowchart of unit 25: the sign of one of male, female or neuter; the embryo's states conform to it, each "
                "according to its own; they become established in the mind and in the body."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"लिंग: पुरुष, स्त्री या<br/>नपुंसक में से एक\"] --> B[\"उसके अनुरूप ही<br/>गर्भ के भाव\"]\n"
                 "  B --> C[\"मन में\"]\n"
                 "  B --> D[\"शरीर में\"]\n"),
    },
}
