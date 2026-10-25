from helpers import mcq, match, order, fill, multi, accepts


AUTHORED = {}

# ---------------------------------------------------------------- unit 40
AUTHORED["40"] = {
    "title": "यः पश्येल्लभते यो वा",
    "question": "By card 40, which items appear to be the objects of लभते (obtains), and which two verbs does the card print?",
    "rule": ("He who should see (पश्येत्), or who obtains (लभते), an umbrella (छत्र), a mirror (आदर्श), an unclear item, white flowers "
             "(शुक्लाः सुमनसः), cloth (वस्त्रम्), a smearing with impure matter (अमेध्यालेपनम्) and fruit (फलम्)."),
    "limits": ("Low confidence. विशामिषं is unclear: no question on it. By the data, cards 38-39 appear to be objects of पश्येत्, "
               "the items here of लभते; the main clause is not here. The impure substance is not named; सुमनस् = flower "
               "(jasmine not stated)."),
    "explain_hi": ("जो देखे (पश्येत्), या जो पाता है (लभते): छत्र (छाता), आदर्श (दर्पण), एक अस्पष्ट शब्द ‘विशामिषं’, श्वेत पुष्प (शुक्लाः सुमनसः), "
                   "वस्त्र, अमेध्य (अशुद्ध) पदार्थ का लेप और फल। "
                   "डेटा के नोट्स के अनुसार कार्ड ३८-३९ की सूचियाँ सम्भवतः ‘पश्येत्’ के कर्म हैं और इस कार्ड की वस्तुएँ ‘लभते’ की; मुख्य वाक्य इस कार्ड में नहीं है। "
                   "‘विशामिषं’ का अर्थ अस्पष्ट है, इसलिए उस पर कोई प्रश्न नहीं; अशुद्ध पदार्थ का नाम भी नहीं छपा। "
                   "‘पश्येल्लभते’ में पश्येत् + लभते है: त् के बाद ल आए तो त् → ल्।"),
    "hook": "देखे या पाए: छाता, दर्पण, श्वेत फूल, वस्त्र, फल।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 40, what does छत्र mean?",
            ("Umbrella", "छत्र = umbrella, parasol: the first item of the list."),
            [("Necklace", "A necklace would be हार; छत्र = umbrella."),
             ("Sandal", "A sandal would be पादुका; छत्र = umbrella."),
             ("Bangle", "A bangle would be वलय; छत्र = umbrella.")],
            "छत्र = umbrella.",
            "छत्र = umbrella."),
        match(1, "Match each word of card 40 to its meaning.",
              [["छत्र", "umbrella"], ["आदर्श", "mirror"], ["सुमनसः", "flowers"], ["वस्त्रम्", "cloth"], ["फलम्", "fruit"]],
              "छत्र = umbrella, आदर्श = mirror, सुमनसः = flowers, वस्त्रम् = cloth, फलम् = fruit.",
              "छत्र, आदर्श, सुमनसः, वस्त्रम्, फलम्."),
        order(2, "Put these sure items of card 40 in the printed order.",
              ["छत्र", "आदर्श", "शुक्लाः सुमनसः", "वस्त्रम्", "अमेध्यालेपनम्", "फलम्"],
              "Line 1: umbrella, mirror (then an unclear word); line 2: white flowers, cloth, smearing with impure matter, fruit.",
              "छत्र → आदर्श → शुक्लाः सुमनसः → वस्त्रम् → अमेध्यालेपनम् → फलम्.",
              role="extend",
              teaches="The items of card 40 are a list in the accusative; by the data's notes they appear to be the objects of लभते (obtains)."),
        mcq("discriminate", 3, "Which split of पश्येल्लभते in card 40 is right?",
            ("पश्येत् + लभते", "त् before ल becomes ल्: पश्येत् + लभते → पश्येल्लभते."),
            [("पश्येः + लभते", "After ए a visarga before the voiced ल gives र्: that would print पश्येर्लभते."),
             ("पश्ये + ल्लभते", "ल्लभते is not a word; the first ल् comes from the त् of पश्येत्."),
             ("पश्ये + लभते", "With पश्ये nothing joins: it would print पश्ये लभते, with one ल.")],
            "पश्येत् (should see) + लभते (obtains): त् + ल → ल्ल.",
            "त् + ल → ल्ल."),
        multi("apply", 4, "Which statements about the two verbs of card 40 are right?",
              [("लभते is a passive form", "No: √लभ् takes the middle (-ते) endings; लभते means 'obtains', not 'is obtained'."),
               ("पश्येत् is an optative", "Right: पश्येत् is the optative of √दृश्, 'should see'."),
               ("लभते is a present form", "Right: लभते is present, third person singular."),
               ("पश्येत् is a past form", "No: पश्येत् is optative, not past.")],
              [1, 2],
              "पश्येत्: optative of √दृश्; लभते: present (middle) of √लभ्.",
              "-ते is not always passive: लभते is the middle present 'obtains'."),
        mcq("transfer", 5, "By the pattern of पश्येत् + लभते → पश्येल्लभते, how is भवेत् + लाभः (there would be gain) joined in a new example?",
            ("भवेल्लाभः", "त् before ल becomes ल्: भवेत् + लाभः → भवेल्लाभः."),
            [("भवेद्लाभः", "त् does not stop at द् before ल; it becomes ल्."),
             ("भवेन्लाभः", "न् would come from त् before a nasal; ल is not a nasal."),
             ("भवेत्लाभः", "त् does not stay before ल; it becomes ल्.")],
            "भवेत् + लाभः = भवेल्लाभः, like पश्येत् + लभते = पश्येल्लभते.",
            "त् + ल → ल्ल.",
            teaches="A final त् before ल becomes ल्: पश्येत् + लभते → पश्येल्लभते."),
    ],
}

# ---------------------------------------------------------------- unit 41
AUTHORED["41"] = {
    "title": "शैलप्रासादसफलवृक्षसिंहनरद्विपान्",
    "question": "By card 41, what should one climb, and what is said of crossing?",
    "rule": ("He should climb (आरोहेत्) mountains, palaces, fruit-bearing trees, lions, men, elephants (द्विप) and a horse-vehicle "
             "(अश्वयानम्); and should cross (तरेत्) what is printed नदन्हदोदधीन् (rivers, lakes and oceans on a conjectural reading)."),
    "limits": ("Medium confidence. The objects of तरेत् are printed नदन्हदोदधीन्; 'rivers, lakes and oceans' is a conjectural reading: "
               "no question on what is crossed. Line 1 is one compound; by the data's notes its members are the objects of आरोहेत्. "
               "The card does not say what follows."),
    "explain_hi": ("पर्वत, महल, फलदार वृक्ष, सिंह, मनुष्य और हाथी (द्विप): इन पर चढ़े (आरोहेत्), और घोड़े के वाहन (अश्वयान) पर भी; और तरे, यानी पार करे (तरेत्)। "
                   "क्या पार करे, यह छपे ‘नदन्हदोदधीन्’ में है; ‘नदों, झीलों और समुद्रों को’ अनुमानित पाठ है, इसलिए उस पर प्रश्न नहीं। "
                   "पहली पंक्ति एक ही लम्बा द्वन्द्व समास है, जिसमें विभक्ति (द्वितीया बहुवचन -आन्) केवल अन्तिम सदस्य पर लगी है। "
                   "‘आरोहेदश्वयानं’ में आरोहेत् + अश्वयानम् है: स्वर से पहले त् → द्।"),
    "hook": "पर्वत, महल, फलदार पेड़, सिंह, मनुष्य, हाथी, घोड़ा-वाहन: इन पर चढ़े।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In card 41, what does द्विप mean?",
            ("Elephant", "द्विप = elephant (literally 'twice-drinker')."),
            [("Mongoose", "A mongoose would be नकुल; द्विप = elephant."),
             ("Bull", "A bull would be वृषभ; द्विप = elephant."),
             ("Horse", "A horse is अश्व (in अश्वयानम्); द्विप = elephant.")],
            "द्विप = elephant.",
            "द्विप = elephant."),
        order(1, "Put the members of the first compound of card 41 in the printed order.",
              ["शैल", "प्रासाद", "सफलवृक्ष", "सिंह", "नर", "द्विप"],
              "Mountain, palace, fruit-bearing tree, lion, man, elephant: one dvandva ending in -द्विपान्.",
              "शैल → प्रासाद → सफलवृक्ष → सिंह → नर → द्विप."),
        match(2, "Match each word of card 41 to its meaning.",
              [["शैल", "mountain"], ["प्रासाद", "palace"], ["सफल", "with fruit"], ["आरोहेत्", "should climb"],
               ["अश्वयानम्", "horse-vehicle"]],
              "शैल = mountain, प्रासाद = palace, सफल = with fruit, आरोहेत् = should climb, अश्वयानम् = horse-vehicle.",
              "शैल, प्रासाद, सफल, आरोहेत्, अश्वयानम्.", role="extend",
              teaches="स- before a noun means 'with': स-फल = with fruit, so सफलवृक्ष = a tree bearing fruit."),
        mcq("discriminate", 3, "Why does the first line of card 41 carry only one case ending, -द्विपान्?",
            ("A dvandva puts the ending on its last member", "शैल-प्रासाद-...-द्विपान् is one dvandva: the accusative plural ending stands at the end."),
            [("Its first five words lost their endings by error", "Nothing is lost: the members of a compound take no endings."),
             ("It is a bahuvrīhi that describes the elephants", "The data reads it as a dvandva of six objects, not as words describing elephants."),
             ("It is a genitive phrase that means 'of these'", "-आन् is accusative plural, not genitive; the objects are climbed.")],
            "One dvandva, one ending: -द्विपान् (accusative plural).",
            "In a compound only the last member takes the case ending."),
        mcq("apply", 4, "Which split of आरोहेदश्वयानं in card 41 is right?",
            ("आरोहेत् + अश्वयानम्", "त् before a vowel becomes द्: आरोहेत् + अश्वयानम् → आरोहेदश्वयानम्."),
            [("आरोहेः + अश्वयानम्", "After ए a visarga before a vowel gives र्: that would print आरोहेरश्वयानम्."),
             ("आरोहे + दश्वयानम्", "दश्वयानम् is not a word; the द् comes from the त् of आरोहेत्."),
             ("आरोहेद् + श्वयानम्", "श्वयानम् is not a word; the noun is अश्वयानम् (horse-vehicle).")],
            "आरोहेत् (should climb) + अश्वयानम् (horse-vehicle).",
            "त् + vowel → द्."),
        mcq("transfer", 5, "By the pattern of आरोहेत् + अश्वयानम्, how is पिबेत् + अम्बु (he should drink water) joined in a new example?",
            ("पिबेदम्बु", "त् before a vowel becomes द्: पिबेत् + अम्बु → पिबेदम्बु."),
            [("पिबेतम्बु", "त् does not stay before a vowel; it becomes द्."),
             ("पिबेन्अम्बु", "न् would come from त् before a nasal; अ is a vowel."),
             ("पिबेम्बु", "त् is not dropped and the अ is not lost; त् → द्.")],
            "पिबेत् + अम्बु = पिबेदम्बु, like आरोहेत् + अश्वयानम् = आरोहेदश्वयानम्.",
            "त् + vowel → द्.",
            teaches="A final त् before a vowel becomes द्: आरोहेत् + अश्वयानम् → आरोहेदश्वयानम्."),
    ],
}

# ---------------------------------------------------------------- unit 42
AUTHORED["42"] = {
    "title": "पूर्वोत्तरेण गमनम्",
    "question": "Which further dream-events does card 42 list, and in what cases are they printed?",
    "rule": ("Going by the north-east (पूर्वोत्तरेण गमनम्), approaching the unapproachable (अगम्यागमनम्), death (मृतिम्), emerging from a "
             "confined place (संबाधान्निःसृतिः), and touching stars, mountains and radiant ones (स्पर्शस्तारकाचलभास्वताम्)."),
    "limits": ("Medium confidence. No verb: by the data's notes the governing verb is पश्येत् (card 40) or स्यात् (card 43), and the cases "
               "are mixed. अगम्यागमन is taken literally; any narrower legal sense is not stated here: no question on it. भास्वत् "
               "can also name the sun: no question on which."),
    "explain_hi": ("पूर्वोत्तर (ईशान) दिशा से जाना, अगम्य (जहाँ न जाना चाहिए) के पास जाना, मृत्यु, संकीर्ण स्थान से निकलना, और तारों, पर्वतों तथा प्रकाशमानों का स्पर्श। "
                   "इस कार्ड में कोई क्रिया नहीं; डेटा के अनुसार शासक क्रिया कार्ड ४० का ‘पश्येत्’ या कार्ड ४३ का ‘स्यात्’ है। "
                   "विभक्तियाँ मिली-जुली हैं: मृतिम् द्वितीया, निःसृतिः प्रथमा, संबाधात् पंचमी (से)। "
                   "‘अगम्यागमन’ का शब्दार्थ ही लिया गया; ‘भास्वत्’ सूर्य का नाम भी हो सकता है, इसलिए इन पर प्रश्न नहीं। "
                   "‘पूर्वोत्तरेण’ में पूर्व + उत्तरेण है (अ + उ → ओ)।"),
    "hook": "ईशान की ओर जाना, तंग जगह से निकलना, तारे-पर्वत छूना।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 42, what does पूर्वोत्तरेण mean?",
            ("By the north-east", "पूर्व (east) + उत्तर (north): by the north-east."),
            [("By the south-west", "South-west would be दक्षिणपश्चिम; पूर्व + उत्तर is north-east."),
             ("By the north-west", "North-west would be पश्चिमोत्तर; पूर्व is east."),
             ("By the south-east", "South-east would be पूर्वदक्षिण; उत्तर is north.")],
            "पूर्वोत्तरेण = by the north-east.",
            "पूर्व = east, उत्तर = north."),
        order(1, "Put the items of card 42 in the printed order.",
              ["पूर्वोत्तरेण गमनम्", "अगम्यागमनम्", "मृतिम्", "संबाधान्निःसृतिः", "स्पर्शः", "तारकाचलभास्वताम्"],
              "Line 1: going north-east, approaching the unapproachable, death; line 2: emerging from a confined place, touching stars, mountains, radiant ones.",
              "पूर्वोत्तरेण गमनम् → अगम्यागमनम् → मृतिम् → संबाधान्निःसृतिः → स्पर्शः → तारकाचलभास्वताम्."),
        match(2, "Match each word of card 42 to its meaning.",
              [["गमनम्", "going"], ["मृतिम्", "death"], ["संबाधात्", "from a confined place"], ["निःसृतिः", "emerging"],
               ["स्पर्शः", "touching"]],
              "गमनम् = going, मृतिम् = death, संबाधात् = from a confined place, निःसृतिः = emerging, स्पर्शः = touching.",
              "गमनम्, मृतिम्, संबाधात्, निःसृतिः, स्पर्शः.", role="extend",
              teaches="The ablative -आत् means 'from': संबाधात् = from a confined place."),
        mcq("discriminate", 3, "Which split of पूर्वोत्तरेण in card 42 is right?",
            ("पूर्व + उत्तरेण", "अ + उ → ओ: पूर्व + उत्तरेण → पूर्वोत्तरेण."),
            [("पूर्वः + उत्तरेण", "After अः the visarga drops before उ and the vowels stay apart: पूर्व उत्तरेण."),
             ("पूर्वो + त्तरेण", "त्तरेण is not a word; the ओ comes from अ + उ."),
             ("पूर्वे + उत्तरेण", "ए before उ does not give ओ; it would not print पूर्वोत्तरेण.")],
            "पूर्व (east) + उत्तरेण (by the north).",
            "अ + उ → ओ."),
        multi("apply", 4, "Which statements about the case forms of card 42 are right by the data?",
              [("मृतिम् is accusative", "Right: मृतिम् is accusative singular."),
               ("निःसृतिः is nominative", "Right: निःसृतिः is nominative singular; the cases are mixed."),
               ("तारकाचलभास्वताम् is locative", "No: -ताम् here is genitive plural, 'of stars, mountains and radiant ones'."),
               ("संबाधात् is ablative", "Right: -आत् is ablative singular, 'from a confined place'.")],
              [0, 1, 3],
              "Mixed cases: मृतिम् accusative, निःसृतिः nominative, संबाधात् ablative, -भास्वताम् genitive plural.",
              "With no verb in the card, the case forms are listed as printed."),
        mcq("transfer", 5, "By the pattern of पूर्व + उत्तरेण → पूर्वोत्तरेण, how is रक्त + उत्पलम् (red lotus) joined in a new example?",
            ("रक्तोत्पलम्", "अ + उ → ओ: रक्त + उत्पलम् → रक्तोत्पलम्."),
            [("रक्तौत्पलम्", "औ comes from अ + ओ or अ + औ, not from अ + उ."),
             ("रक्तूत्पलम्", "अ + उ does not give ऊ; it gives ओ."),
             ("रक्त्वुत्पलम्", "व् comes from उ before a vowel; here अ meets उ.")],
            "रक्त + उत्पलम् = रक्तोत्पलम्, like पूर्व + उत्तरेण = पूर्वोत्तरेण.",
            "अ + उ → ओ.",
            teaches="अ (or आ) before उ gives ओ: पूर्व + उत्तरेण → पूर्वोत्तरेण."),
    ],
}

# ---------------------------------------------------------------- unit 43
AUTHORED["43"] = {
    "title": "रोदनंपतितोत्थानं",
    "question": "Which dream-events does card 43 add, and which words of its second line are sure?",
    "rule": ("Weeping (रोदनम्), the rising of one who has fallen (पतितोत्थानम्) and the crushing of enemies (द्विषतां चावमर्दनम्); then "
             "a closing line with life (आयुः), health (आरोग्यम्) and wealth (वित्तम्)."),
    "limits": ("Low confidence. The second line's syntax is not clear (the data gives two parses), and अश्नुते 'attains' is a conjecture "
               "for printed अश्रुते: no question on who attains what. Questions stay on line 1 and on word meanings. By the data, cards 42-43 "
               "appear to be one construction."),
    "explain_hi": ("रोना, गिरे हुए का उठना, और शत्रुओं का कुचलना (अवमर्दन)। "
                   "दूसरी पंक्ति में आयु, आरोग्य और धन (वित्त) के शब्द साफ़ हैं, पर वाक्य-रचना स्पष्ट नहीं; डेटा दो पद-योजनाएँ देता है। "
                   "छपा ‘अश्रुते’ यहाँ अर्थ नहीं देता; ‘अश्नुते’ (पाता है) अनुमानित पाठ है, इसलिए कौन क्या पाता है, इस पर प्रश्न नहीं। "
                   "‘द्विषताम्’ √द्विष् (द्वेष करना) का कृदन्त, षष्ठी बहुवचन, संज्ञा की तरह: शत्रुओं का। "
                   "‘चावमर्दनं’ में च + अवमर्दनम् है (अ + अ → आ)।"),
    "hook": "रोना, गिरे का उठना, शत्रु का कुचलना; फिर आयु, आरोग्य, धन।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 43, what does रोदनम् mean?",
            ("Weeping", "रोदनम् = weeping, from √रुद् (to weep)."),
            [("Laughing", "Laughing would be हसनम्; रोदनम् = weeping."),
             ("Singing", "Singing would be गानम्; रोदनम् = weeping."),
             ("Sleeping", "Sleeping would be शयनम्; रोदनम् = weeping.")],
            "रोदनम् = weeping.",
            "रोदनम् = weeping."),
        match(1, "Match each word of card 43 to its meaning.",
              [["रोदनम्", "weeping"], ["पतित", "fallen (one)"], ["उत्थानम्", "rising up"], ["द्विषताम्", "of enemies"],
               ["अवमर्दनम्", "crushing"]],
              "रोदनम् = weeping, पतित = fallen, उत्थानम् = rising, द्विषताम् = of enemies, अवमर्दनम् = crushing.",
              "रोदनम्, पतित, उत्थानम्, द्विषताम्, अवमर्दनम्."),
        fill(2, "The word for 'health' in card 43 is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("आरोग्यम्", "ārogyam", "आरोग्य", "arogyam"),
             "आरोग्यम् = health: printed in स्यादायुरारोग्यं.",
             "आरोग्य = अरोग (a- without + रोग disease), first vowel lengthened, + -य: freedom from disease, health.",
             "आरोग्यम् = health."),
        mcq("discriminate", 3, "Which split of चावमर्दनं in card 43 is right?",
            ("च + अवमर्दनम्", "अ + अ → आ: च + अवमर्दनम् → चावमर्दनम्."),
            [("च + वमर्दनम्", "With वमर्दनम् nothing joins: it would print च वमर्दनं, without आ."),
             ("चा + वमर्दनम्", "चा is not a word; the आ comes from च + अ-."),
             ("चे + अवमर्दनम्", "ए before अ gives एऽ: that would print चेऽवमर्दनं.")],
            "च (and) + अवमर्दनम् (crushing).",
            "अ + अ → आ."),
        mcq("apply", 4, "In a dream one's foes are trampled down. Which phrase of card 43 names this?",
            ("द्विषतां चावमर्दनम्", "द्विषताम् (of enemies) + अवमर्दनम् (crushing): the crushing of enemies."),
            [("पतितोत्थानम्", "पतितोत्थानम् is the rising of a fallen one, not crushing."),
             ("रोदनम्", "रोदनम् is weeping; it names no enemies."),
             ("आयुरारोग्यम्", "आयुः and आरोग्यम् are life and health, not crushing.")],
            "द्विषतां चावमर्दनम् = and the crushing of enemies.",
            "अवमर्दन = crushing; द्विषत् = enemy."),
        mcq("transfer", 5, "By the pattern of च + अवमर्दनम् → चावमर्दनम्, how is जलं च + अन्नम् (water and food) written in a new example?",
            ("जलं चान्नम्", "अ + अ → आ: च + अन्नम् → चान्नम्."),
            [("जलं चन्नम्", "Two अ do not merge into a short अ; they give आ."),
             ("जलं चेन्नम्", "ए comes from अ + इ, not from अ + अ."),
             ("जलं चौन्नम्", "औ comes from अ + ओ or अ + औ, not from अ + अ.")],
            "च + अन्नम् = चान्नम्, like च + अवमर्दनम् = चावमर्दनम्.",
            "अ + अ → आ.",
            teaches="अ before अ merges into आ: च + अवमर्दनम् → चावमर्दनम्."),
    ],
}

# ---------------------------------------------------------------- unit 44
AUTHORED["44"] = {
    "title": "पितृदेवद्विजातीनां",
    "question": "By card 44, whose sight is not praised?",
    "rule": ("The sight (दर्शनम्) of forefathers, gods and twice-born (पितृदेवद्विजातीनाम्) who are angry, frightened and emaciated "
             "(क्रुद्धभीतकृशात्मनाम्), and of ones with dirty garments and flowers (मलिनाम्बरपुष्पाणाम्; or the same ones so dressed), is not praised (न प्रशस्यते)."),
    "limits": ("Medium confidence. मलिनाम्बरपुष्पाणाम् may name further persons or describe the same forefathers, gods and twice-born "
               "(two-way): no question on which. -आत्मन् is read 'in person'. The word 'dream' is not printed in this card."),
    "explain_hi": ("क्रुद्ध, भयभीत और कृश स्वरूप वाले पितरों, देवताओं और द्विजातियों का, और मैले वस्त्र तथा फूलों वालों का दर्शन प्रशंसित नहीं है (न प्रशस्यते)। "
                   "‘मलिनाम्बरपुष्पाणाम्’ अलग व्यक्तियों को भी बता सकता है या उन्हीं पितरों आदि का विशेषण भी हो सकता है; डेटा दोनों पढ़ाव देता है, इसलिए इस पर प्रश्न नहीं। "
                   "‘-आत्मनाम्’ को ‘स्वरूप से’ पढ़ा गया। ‘स्वप्न’ शब्द इस कार्ड में नहीं छपा। "
                   "‘कृशात्मनाम्’ में कृश + आत्मनाम् है (अ + आ → आ)।"),
    "hook": "क्रुद्ध, डरे, दुबले पितर-देव-द्विज, मैले वस्त्र-फूल: इनका दर्शन प्रशंसित नहीं।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 44, what does प्रशस्यते mean?",
            ("Is praised", "प्रशस्यते = is praised (passive of प्र-√शंस्); with न: is not praised."),
            [("Is feared", "Is feared would be भीयते; प्रशस्यते = is praised."),
             ("Is given", "Is given would be दीयते; प्रशस्यते = is praised."),
             ("Is forgotten", "Is forgotten would be विस्मर्यते; प्रशस्यते = is praised.")],
            "प्रशस्यते = is praised.",
            "प्र-√शंस् = praise."),
        order(1, "Put the phrases of card 44 in the printed order.",
              ["पितृदेवद्विजातीनाम्", "क्रुद्धभीतकृशात्मनाम्", "मलिनाम्बरपुष्पाणाम्", "दर्शनम्", "न प्रशस्यते"],
              "Whose (forefathers, gods, twice-born), how (angry, frightened, emaciated), with what (dirty garments, flowers): the sight is not praised.",
              "पितृदेवद्विजातीनाम् → क्रुद्धभीतकृशात्मनाम् → मलिनाम्बरपुष्पाणाम् → दर्शनम् → न प्रशस्यते."),
        match(2, "Match each word of card 44 to its meaning.",
              [["क्रुद्ध", "angry"], ["भीत", "frightened"], ["कृश", "emaciated"], ["मलिन", "dirty"], ["अम्बर", "garment"]],
              "क्रुद्ध = angry, भीत = frightened, कृश = emaciated, मलिन = dirty, अम्बर = garment.",
              "क्रुद्ध, भीत, कृश, मलिन, अम्बर.", role="extend",
              teaches="A bahuvrīhi such as क्रुद्ध-भीत-कृश-आत्मन् describes persons: 'who are angry, frightened and emaciated in person'."),
        mcq("discriminate", 3, "By card 44, the sight of forefathers, gods and twice-born is not praised when they are what?",
            ("Angry, frightened and emaciated", "क्रुद्ध-भीत-कृश-आत्मनाम्: angry, frightened, emaciated in person."),
            [("Pleased and wearing pure flowers", "Pleased ones with pure flowers are not in card 44; it names the angry ones."),
             ("Silent and seated far away", "Card 44 says nothing of silence or distance."),
             ("Radiant and dressed in white", "Card 44 names no radiance or white clothes; it names anger, fear, emaciation.")],
            "Not praised: the sight of angry, frightened, emaciated ones, and of ones with dirty garments and flowers (or the same ones so dressed).",
            "क्रुद्ध, भीत, कृश → न प्रशस्यते."),
        mcq("apply", 4, "Which split of कृशात्मनां in card 44 is right?",
            ("कृश + आत्मनाम्", "अ + आ → आ: कृश + आत्मनाम् → कृशात्मनाम्."),
            [("कृशः + आत्मनाम्", "After अः the visarga drops before आ and the vowels stay apart: कृश आत्मनाम्."),
             ("कृशा + त्मनाम्", "त्मनाम् is not a word; the noun is आत्मन्."),
             ("कृशे + आत्मनाम्", "ए before आ does not give आ; it would not print कृशात्मनां.")],
            "कृश (emaciated) + आत्मनाम् (in person).",
            "अ + आ → आ."),
        mcq("transfer", 5, "By the pattern of कृश + आत्मनाम् → कृशात्मनाम्, how is शान्त + आत्मा (one of calm self) joined in a new example?",
            ("शान्तात्मा", "अ + आ → आ: शान्त + आत्मा → शान्तात्मा."),
            [("शान्तत्मा", "अ + आ does not shorten to अ; it gives आ."),
             ("शान्तेत्मा", "ए comes from अ + इ, not from अ + आ."),
             ("शान्तौत्मा", "औ comes from अ + ओ or अ + औ, not from अ + आ.")],
            "शान्त + आत्मा = शान्तात्मा, like कृश + आत्मनाम् = कृशात्मनाम्.",
            "अ + आ → आ.",
            teaches="अ before आ merges into आ: कृश + आत्मनाम् → कृशात्मनाम्."),
    ],
}

# ---------------------------------------------------------------- unit 45
AUTHORED["45"] = {
    "title": "तेषामेव तु तुष्टानां",
    "question": "By card 45, whose sight in a dream is praised, and what is said of conversation with them?",
    "rule": ("But (तु) the sight in a dream (स्वप्ने) of those very ones (तेषाम् एव) when pleased (तुष्टानाम्), pure in person with flowers "
             "and garments, is praised (शस्यते); and conversation (संभाषणम्) with them (तैः) is auspicious (शुभम्)."),
    "limits": ("Medium confidence. शुद्धपुष्पाम्बरात्मनाम् can also be read 'of pure self, with flowers and garments' (two-way): no question "
               "on which. 'Those very ones' appear to be the forefathers, gods and twice-born of card 44. 'Is' is understood in the "
               "second clause."),
    "explain_hi": ("किन्तु (तु) उन्हीं (तेषामेव) का, जब वे सन्तुष्ट हों और शुद्ध फूलों और वस्त्रों वाले स्वरूप के हों, स्वप्न में दर्शन प्रशंसित है (शस्यते); "
                   "और उनके साथ बातचीत (संभाषण) शुभ है। "
                   "‘उन्हीं’ सम्भवतः कार्ड ४४ के पितर, देवता और द्विजाति हैं। "
                   "‘शस्यते’ वही क्रिया √शंस् है जो कार्ड ४४ के ‘प्रशस्यते’ में है, केवल उपसर्ग ‘प्र’ के बिना; डेटा के अनुसार यह छपाई की भूल नहीं। "
                   "‘तैश्च’ में तैः + च है: च से पहले विसर्ग → श्।"),
    "hook": "वही जब प्रसन्न और शुद्ध फूल-वस्त्र में: दर्शन प्रशंसित, बातचीत शुभ।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In card 45, what does संभाषणम् mean?",
            ("Conversation", "संभाषणम् = conversation, talking together (सम् + √भाष्)."),
            [("Quarrel", "A quarrel would be कलह; संभाषणम् = conversation."),
             ("Silence", "Silence would be मौनम्; संभाषणम् = conversation."),
             ("Disagreement", "A disagreement would be विवाद; संभाषणम् = conversation.")],
            "संभाषणम् = conversation.",
            "सम् + √भाष् = to talk together."),
        match(1, "Match each word of card 45 to its meaning.",
              [["तुष्ट", "pleased"], ["शुद्ध", "pure"], ["स्वप्ने", "in a dream"], ["तैः", "with them"], ["शुभम्", "auspicious"]],
              "तुष्ट = pleased, शुद्ध = pure, स्वप्ने = in a dream, तैः = with them, शुभम् = auspicious.",
              "तुष्ट, शुद्ध, स्वप्ने, तैः, शुभम्."),
        order(2, "Put the phrases of card 45 in the printed order.",
              ["तेषामेव तु तुष्टानाम्", "शुद्धपुष्पाम्बरात्मनाम्", "दर्शनं शस्यते स्वप्ने", "तैश्च संभाषणं शुभम्"],
              "Of those very ones when pleased; pure in person with flowers and garments; the sight is praised in a dream; and conversation with them is auspicious.",
              "तेषामेव तु तुष्टानाम् → शुद्धपुष्पाम्बरात्मनाम् → दर्शनं शस्यते स्वप्ने → तैश्च संभाषणं शुभम्.",
              role="extend",
              teaches="तु (but) turns from the sight that is not praised to a sight that is praised."),
        mcq("discriminate", 3, "Is शस्यते in card 45 a printing slip for प्रशस्यते?",
            ("No: it is √शंस् without the prefix प्र-", "The data says शस्यते is the same verb as प्रशस्यते, only without प्र-, and not a typo."),
            [("Yes: the prefix प्र- was dropped in print", "The data says it is not a typo; शस्यते is a correct form."),
             ("No: it is an active form, 'he praises'", "शस्यते is passive, 'is praised'; the active would be शंसति."),
             ("Yes: the metre needs प्रशस्यते here", "The data counts eight syllables with शस्यते; the metre does not need प्र-.")],
            "शस्यते = is praised; प्रशस्यते = is praised (with प्र-).",
            "A verb may appear with or without its prefix."),
        mcq("apply", 4, "In a dream one talks with the pleased ones of card 45. How does the card judge this conversation?",
            ("It is auspicious", "तैश्च संभाषणं शुभम्: conversation with them is auspicious."),
            [("It is not praised", "Not praised (न प्रशस्यते) is said in card 44 of the angry ones, not of this talk."),
             ("It brings a disease", "Card 45 names no disease; it calls the talk auspicious."),
             ("It is not judged", "It is judged: the card calls it शुभम्, auspicious.")],
            "संभाषणं शुभम् = conversation (with them) is auspicious.",
            "तैः संभाषणम् → शुभम्."),
        mcq("transfer", 5, "By the pattern of तैः + च → तैश्च, how is गजैः + च (and with elephants) joined in a new example?",
            ("गजैश्च", "A visarga before च becomes श्: गजैः + च → गजैश्च."),
            [("गजैर्च", "र् comes from a visarga before a voiced sound; च is not voiced."),
             ("गजैष्च", "ष् comes from a visarga before ट or ठ, not before च."),
             ("गजै च", "The visarga is not dropped before च; it becomes श्.")],
            "गजैः + च = गजैश्च, like तैः + च = तैश्च.",
            "Visarga before च or छ → श्.",
            teaches="A visarga before च or छ becomes श्: तैः + च → तैश्च."),
    ],
}

# ---------------------------------------------------------------- unit 46
AUTHORED["46"] = {
    "title": "स्वप्न के बाद स्नान और हवन",
    "question": "By card 46, what does one do after seeing dreams, and from what is one then freed?",
    "rule": ("Having seen (दृष्ट्वा) terrible or good dreams, bathed (स्नातः) in the morning (प्रातः), having offered (हुत्वा) with the "
             "Sāvitrī (सावित्र्या), purified (पूतः), one is freed (मुच्यते) from sins (पापैः) and from diseases (व्याधिभिः)."),
    "limits": ("Prose, low confidence. सर्पषानमिवर्णान् is unclear; तिलान् (sesame) is a conjecture for printed त्विलान्; "
               "what is offered is unclear: no question on it. स्वप्मान् = स्वप्नान् (certain). The subject is unnamed. "
               "No amount or other detail is given."),
    "explain_hi": ("भयंकर (दारुण) या अच्छे (शोभन) स्वप्न देखकर, प्रातः स्नान किया हुआ, सावित्री (गायत्री, मानक) से हवन करके, पवित्र हुआ व्यक्ति पापों से और रोगों से मुक्त होता है (मुच्यते)। "
                   "डेटा इसे गद्य मानता है। ‘सर्पषानमिवर्णान्’ अस्पष्ट है; ‘तिलान्’ (तिल) छपे ‘त्विलान्’ का अनुमानित पाठ है; किसका हवन हो, यह स्पष्ट नहीं, इसलिए उस पर प्रश्न नहीं। "
                   "छपा ‘स्वप्मान्’ निश्चित रूप से ‘स्वप्नान्’ है। "
                   "‘पापैः’ और ‘व्याधिभिः’ तृतीया बहुवचन हैं; ‘मुच्यते’ यहाँ तृतीया के साथ आया है।"),
    "hook": "स्वप्न देखा, प्रातः नहाया, सावित्री से हवन किया: पाप और रोग से मुक्त।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In card 46, what does प्रातः mean?",
            ("In the morning", "प्रातः = in the morning, early."),
            [("In the evening", "Evening would be सायम्; प्रातः = in the morning."),
             ("At midnight", "Midnight would be अर्धरात्रे; प्रातः = in the morning."),
             ("At noon", "Noon would be मध्याह्ने; प्रातः = in the morning.")],
            "प्रातः = in the morning.",
            "प्रातः = morning."),
        order(1, "Put these sure parts of card 46 in the printed order.",
              ["दृष्ट्वा", "दारुणान्शोभनान्वा", "प्रातः स्नातः", "हुत्वा सावित्र्या", "पूतः", "पापैर्मुच्यते व्याधिभिश्च"],
              "Having seen (dreams) terrible or good; bathed in the morning; having offered with the Sāvitrī; purified; freed from sins and diseases.",
              "दृष्ट्वा → दारुणान्शोभनान्वा → प्रातः स्नातः → हुत्वा सावित्र्या → पूतः → पापैर्मुच्यते व्याधिभिश्च."),
        match(2, "Match each word of card 46 to its meaning.",
              [["दारुण", "terrible"], ["शोभन", "good"], ["स्नातः", "bathed"], ["पूतः", "purified"], ["व्याधिभिः", "from diseases"]],
              "दारुण = terrible, शोभन = good, स्नातः = bathed, पूतः = purified, व्याधिभिः = from diseases.",
              "दारुण, शोभन, स्नातः, पूतः, व्याधिभिः.", role="extend",
              teaches="स्नातः and पूतः are past participles (√स्ना, √पू) used of the person: 'bathed', 'purified'."),
        multi("discriminate", 3, "Which statements fit the sure parts of card 46?",
              [("Only terrible dreams are named", "No: दारुणान् शोभनान् वा, terrible or good dreams."),
               ("He is bathed in the morning", "Right: प्रातः स्नातः."),
               ("He is freed from sins only, not diseases", "No: पापैर्मुच्यते व्याधिभिश्च, from sins and from diseases."),
               ("The dreams may be terrible or good", "Right: दारुणान् शोभनान् वा.")],
              [1, 3],
              "Terrible or good dreams; bathing in the morning; offering with the Sāvitrī; freed from sins and diseases.",
              "दारुण ⇄ शोभन; पापैः, व्याधिभिः च."),
        mcq("apply", 4, "In card 46, what case are पापैः and व्याधिभिः?",
            ("Instrumental plural", "-ऐः and -भिः are instrumental plural endings; मुच्यते takes them here for 'from'."),
            [("Ablative plural", "The ablative plural would be पापेभ्यः, व्याधिभ्यः."),
             ("Genitive plural", "The genitive plural would be पापानाम्, व्याधीनाम्."),
             ("Locative plural", "The locative plural would be पापेषु, व्याधिषु.")],
            "पापैः, व्याधिभिः = instrumental plural with मुच्यते (is freed).",
            "-ऐः, -भिः = instrumental plural."),
        mcq("transfer", 5, "By the pattern of हुत्वा (having offered, √हु), what does जित्वा (√जि) mean in a new example?",
            ("Having conquered", "-त्वा after a root without prefix = having done: √जि → जित्वा, having conquered."),
            [("To conquer", "To conquer would be the infinitive जेतुम्."),
             ("Conquering now", "Conquering (present) would be the participle जयन्."),
             ("Will conquer", "Will conquer would be the future जेष्यति.")],
            "जित्वा = having conquered, like हुत्वा = having offered.",
            "-त्वा (no prefix) = absolutive, 'having done'.",
            teaches="-त्वा added to an unprefixed root forms the absolutive 'having done': √हु → हुत्वा, √दृश् → दृष्ट्वा."),
    ],
}

# ---------------------------------------------------------------- unit 47
AUTHORED["47"] = {
    "title": "मंगलाचारसंपन्नःपरिवारस्तथाऽऽतुरः",
    "question": "By card 47, what is said of the retinue and of the patient?",
    "rule": ("The retinue (परिवारः) endowed with auspicious conduct (मङ्गलाचारसंपन्नः), and likewise (तथा) the patient (आतुरः): having "
             "faith (श्रद्धा-), favourable (अनुकूलः), and having an abundant collection of materials (प्रभूतद्रव्यसंग्रहः)."),
    "limits": ("Medium confidence. No verb: by the data, cards 47-48 appear to be one list closing in card 48. संपन्नः may qualify retinue "
               "and patient: no question on which. द्रव्य is not specified. Printed श्रद्धावानो does not match the data's split "
               "श्रद्धावान्: no question on that form."),
    "explain_hi": ("मंगल आचार से युक्त परिवार (रोगी के पास के लोग), और वैसे ही रोगी (आतुर): श्रद्धा वाला, अनुकूल, और प्रचुर द्रव्यों के संग्रह वाला। "
                   "इस कार्ड में क्रिया नहीं; डेटा के अनुसार कार्ड ४७-४८ सम्भवतः एक सूची है जो कार्ड ४८ में ‘वह आरोग्य का लक्षण है’ से पूरी होती है। "
                   "एकवचन ‘संपन्नः’ परिवार और रोगी दोनों के लिए हो सकता है; द्रव्य कौन-से, यह नहीं कहा। "
                   "छपा ‘श्रद्धावानो’ और डेटा का विच्छेद ‘श्रद्धावान्’ मेल नहीं खाते, इसलिए उस रूप पर प्रश्न नहीं। "
                   "‘परिवारस्तथा’ में परिवारः + तथा है: त से पहले विसर्ग → स्।"),
    "hook": "परिवार मंगल-आचार वाला, रोगी श्रद्धालु, अनुकूल, द्रव्य-सम्पन्न।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 47, what does आतुरः mean?",
            ("Patient", "आतुरः = the patient, the sick person."),
            [("Physician", "A physician would be वैद्य; आतुर = patient."),
             ("Teacher", "A teacher would be आचार्य; आतुर = patient."),
             ("Herald", "A herald or messenger would be दूत; आतुर = patient.")],
            "आतुरः = patient.",
            "आतुर = patient."),
        match(1, "Match each word of card 47 to its meaning.",
              [["परिवारः", "retinue"], ["आतुरः", "patient"], ["अनुकूलः", "favourable"], ["प्रभूत", "abundant"], ["द्रव्य", "material"]],
              "परिवारः = retinue, आतुरः = patient, अनुकूलः = favourable, प्रभूत = abundant, द्रव्य = material.",
              "परिवारः, आतुरः, अनुकूलः, प्रभूत, द्रव्य."),
        order(2, "Put these sure parts of card 47 in the printed order.",
              ["मङ्गलाचारसंपन्नः", "परिवारः", "तथा आतुरः", "अनुकूलः", "प्रभूतद्रव्यसंग्रहः"],
              "Endowed with auspicious conduct; the retinue; likewise the patient; favourable; with abundant materials.",
              "मङ्गलाचारसंपन्नः → परिवारः → तथा आतुरः → अनुकूलः → प्रभूतद्रव्यसंग्रहः.",
              role="extend",
              teaches="तथा (likewise) links the retinue and the patient as two parts of one list."),
        mcq("discriminate", 3, "Which split of तथाऽऽतुरः in card 47 is right?",
            ("तथा + आतुरः", "आ + आ → आ: तथा + आतुरः → तथातुरः; the ऽऽ is a print habit."),
            [("तथा + तुरः", "With तुरः nothing joins: it would print तथा तुरः, with no ऽऽ."),
             ("तथः + आतुरः", "तथः is not a word; the word is the indeclinable तथा."),
             ("तथे + आतुरः", "तथे is not a word, and ए before आ would not give आ.")],
            "तथा (likewise) + आतुरः (the patient).",
            "आ + आ → आ."),
        mcq("apply", 4, "A patient is agreeable and has plenty of materials at hand. Which words of card 47 fit him?",
            ("अनुकूलः and प्रभूतद्रव्यसंग्रहः", "Favourable (अनुकूलः) and having an abundant collection of materials."),
            [("मङ्गलाचार- and परिवारः", "Auspicious conduct and the retinue: neither names agreeableness or materials."),
             ("आतुरः and मङ्गलाचार-", "आतुरः names the patient, but auspicious conduct is neither agreeableness nor materials."),
             ("परिवारः and तथा", "The retinue and 'likewise': neither names agreeableness or materials.")],
            "अनुकूलः (favourable) and प्रभूत-द्रव्य-संग्रहः (abundant materials) describe the patient.",
            "अनुकूल = favourable; प्रभूत = abundant; द्रव्य = material."),
        mcq("transfer", 5, "By the pattern of प्रभूतद्रव्यसंग्रहः (having an abundant collection of materials), what does प्रभूतधनः mean in a new example?",
            ("Having abundant wealth", "प्रभूत (abundant) + धन (wealth), used of a person (masculine -धनः): one who has abundant wealth."),
            [("Without any wealth", "Without wealth would be निर्धनः; प्रभूत means abundant."),
             ("Giver of wealth", "A giver of wealth would be धनदः; प्रभूतधनः names what the person has."),
             ("Seeker of wealth", "A seeker of wealth would be धनार्थी; प्रभूतधनः names what the person has.")],
            "प्रभूतधनः = having abundant wealth, as प्रभूतद्रव्यसंग्रहः = having an abundant collection of materials.",
            "A bahuvrīhi names the one who has: प्रभूत-धन = (one) having abundant wealth.",
            teaches="A bahuvrīhi such as प्रभूत-द्रव्य-संग्रहः describes the one who has the thing: having an abundant collection of materials."),
    ],
}

# ---------------------------------------------------------------- unit 48
AUTHORED["48"] = {
    "title": "सत्त्वलक्षणसंयोगो भक्तिर्वैद्यद्विजातिषु",
    "question": "By card 48, what completes the list, and what is the whole list called?",
    "rule": ("Association with the marks of sattva (सत्त्वलक्षणसंयोगः), devotion to physicians and twice-born (भक्तिः वैद्यद्विजातिषु), "
             "and non-despondency in treatment (चिकित्सायाम् अनिर्वेदः): that (तत्) is the sign of health (आरोग्यस्य लक्षणम्)."),
    "limits": ("Medium confidence. सत्त्व is a doctrinal term (a quality of mind) and the text does not define it further. तत् refers to the "
               "signs just listed (by the data, cards 47-48). 'Is' is understood. The card names signs; it does not say how long or how sure."),
    "explain_hi": ("सत्त्व (मन का एक गुण) के लक्षणों का संयोग, वैद्यों और द्विजातियों में भक्ति, और चिकित्सा में निराश न होना (अनिर्वेद): वह (तत्) आरोग्य का लक्षण है। "
                   "डेटा के अनुसार ‘तत्’ कार्ड ४७-४८ के सब लक्षणों की ओर संकेत करता है। "
                   "‘सत्त्व’ शास्त्रीय शब्द है; पाठ इसकी और परिभाषा नहीं देता। "
                   "सन्धियाँ: संयोगः + भक्तिः → संयोगो भक्तिः (अः, घोष व्यंजन से पहले → ओ); अनिर्वेदः + तत् → अनिर्वेदस्तत् (त से पहले विसर्ग → स्)।"),
    "hook": "सत्त्व, वैद्य में भक्ति, चिकित्सा में निराशा नहीं: यही आरोग्य का लक्षण।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In card 48, what does अनिर्वेदः mean?",
            ("Absence of despondency", "अ- (not) + निर्वेद (despondency, weariness): not losing heart."),
            [("Absence of all bodily pain", "Pain would be वेदना; निर्वेद is despondency."),
             ("Absence of hunger", "Hunger would be क्षुधा; निर्वेद is despondency."),
             ("Absence of fear", "Fear would be भय; निर्वेद is despondency.")],
            "अनिर्वेदः = absence of despondency.",
            "अ- + निर्वेद = not despairing."),
        match(1, "Match each word of card 48 to its meaning.",
              [["सत्त्व", "a quality of mind"], ["भक्तिः", "devotion"], ["वैद्य", "physician"], ["चिकित्सायाम्", "in treatment"],
               ["लक्षणम्", "sign"]],
              "सत्त्व = a quality of mind, भक्तिः = devotion, वैद्य = physician, चिकित्सायाम् = in treatment, लक्षणम् = sign.",
              "सत्त्व, भक्तिः, वैद्य, चिकित्सायाम्, लक्षणम्."),
        order(2, "Put the parts of card 48 in the printed order.",
              ["सत्त्वलक्षणसंयोगः", "भक्तिर्वैद्यद्विजातिषु", "चिकित्सायामनिर्वेदः", "तदारोग्यस्य लक्षणम्"],
              "Marks of sattva; devotion to physicians and twice-born; non-despondency in treatment; that is the sign of health.",
              "सत्त्वलक्षणसंयोगः → भक्तिर्वैद्यद्विजातिषु → चिकित्सायामनिर्वेदः → तदारोग्यस्य लक्षणम्.",
              role="extend",
              teaches="तत् (that) sums up the list before it: तत् आरोग्यस्य लक्षणम्, that is the sign of health."),
        mcq("discriminate", 3, "Why is संयोगः printed संयोगो before भक्तिः in card 48?",
            ("अः before a voiced consonant → ओ", "भ is a voiced consonant: संयोगः + भक्तिः → संयोगो भक्तिः."),
            [("अः before any consonant → ओ", "Not any: before त it becomes स् (परिवारस्तथा, card 47)."),
             ("ओ is the stem's own last vowel", "The stem is संयोग; the ओ comes only from sandhi."),
             ("ओ marks a vocative, 'O union'", "The vocative would be संयोग; ओ here is from अः.")],
            "संयोगः + भक्तिः → संयोगो भक्तिः.",
            "अः + voiced consonant → ओ."),
        mcq("apply", 4, "A patient keeps faith in his physicians and does not lose heart during treatment. By card 48, these are signs of what?",
            ("Of health (आरोग्य)", "तदारोग्यस्य लक्षणम्: that is the sign of health."),
            [("Of a messenger (दूत)", "Card 48 does not speak of a messenger; it names the sign of health."),
             ("Of a dream (स्वप्न)", "Card 48 does not speak of a dream; it names the sign of health."),
             ("Of a disease (व्याधि)", "Card 48 calls these signs of health, not of a disease.")],
            "Devotion to physicians and non-despondency in treatment: signs of ārogya.",
            "तत् आरोग्यस्य लक्षणम्."),
        mcq("transfer", 5, "By the pattern of अनिर्वेदः + तत् → अनिर्वेदस्तत्, how is वृक्षः + तिष्ठति (the tree stands) joined in a new example?",
            ("वृक्षस्तिष्ठति", "A visarga before त becomes स्: वृक्षः + तिष्ठति → वृक्षस्तिष्ठति."),
            [("वृक्षो तिष्ठति", "ओ comes from अः before a voiced consonant; त is not voiced."),
             ("वृक्षर्तिष्ठति", "र् comes from a visarga after other vowels before a voiced sound."),
             ("वृक्ष तिष्ठति", "The visarga is not dropped before त; it becomes स्.")],
            "वृक्षः + तिष्ठति = वृक्षस्तिष्ठति, like अनिर्वेदः + तत् = अनिर्वेदस्तत्.",
            "Visarga before त or थ → स्.",
            teaches="A visarga before त or थ becomes स्: अनिर्वेदः + तत् → अनिर्वेदस्तत्."),
    ],
}

# ---------------------------------------------------------------- unit 49
AUTHORED["49"] = {
    "title": "इत्यत्र जन्ममरणं",
    "question": "By card 49, why is this section called Śarīra?",
    "rule": ("Since (यतः) birth and death (जन्ममरणम्) have been properly set forth (सम्यक् उदाहृतम्) here, therefore (ततः) this section "
             "(स्थानम्) of the body is called Śarīra (शरीरम् इदम् उच्यते)."),
    "limits": ("Medium confidence. इति is taken as 'thus'; it may instead quote the name: no question on it. The printed name is शरीर "
               "(not शारीर); the colophon (card 51) names the section शारीरस्थान. ततःस्थानं is printed without a space."),
    "explain_hi": ("इस प्रकार यहाँ, क्योंकि (यतः) जन्म और मरण का भली-भाँति (सम्यक्) कथन हुआ है, इसलिए (ततः) शरीर का यह स्थान (विभाग) ‘शरीर’ कहलाता है। "
                   "यतः ... ततः का जोड़ा कारण और फल को बाँधता है। "
                   "यहाँ छपा नाम ‘शरीर’ है, ‘शारीर’ नहीं; कार्ड ५१ का समाप्ति-वाक्य ‘शारीरस्थान’ कहता है। ‘इति’ को ‘इस प्रकार’ पढ़ा गया, इस पर प्रश्न नहीं। "
                   "‘सम्यगुदाहृतं’ में सम्यक् + उदाहृतम् है: स्वर से पहले क् → ग्।"),
    "hook": "जन्म और मरण यहाँ कहे गए, इसलिए इस स्थान का नाम ‘शरीर’।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In card 49, what does जन्ममरणम् mean?",
            ("Birth and death", "जन्म (birth) + मरण (death): a dvandva, birth and death."),
            [("Birth and growth", "Growth would be वृद्धि; मरण = death."),
             ("Body and mind", "Body and mind would be शरीर and मनस्; जन्म = birth."),
             ("Life and health", "Life and health would be आयुः and आरोग्य; जन्म = birth.")],
            "जन्ममरणम् = birth and death.",
            "जन्म = birth, मरण = death."),
        match(1, "Match each word of card 49 to its meaning.",
              [["यतः", "since"], ["ततः", "therefore"], ["सम्यक्", "properly"], ["उदाहृतम्", "set forth"], ["उच्यते", "is called"]],
              "यतः = since, ततः = therefore, सम्यक् = properly, उदाहृतम् = set forth, उच्यते = is called.",
              "यतः, ततः, सम्यक्, उदाहृतम्, उच्यते."),
        order(2, "Put the parts of card 49 in the printed order.",
              ["इत्यत्र", "जन्ममरणम्", "यतः सम्यगुदाहृतम्", "शरीरस्य", "ततःस्थानम्", "शरीरमिदमुच्यते"],
              "Thus here; birth and death; since properly set forth; of the body; therefore the section; this is called Śarīra.",
              "इत्यत्र → जन्ममरणम् → यतः सम्यगुदाहृतम् → शरीरस्य → ततःस्थानम् → शरीरमिदमुच्यते.",
              role="extend",
              teaches="यतः (since) ... ततः (therefore) pair a reason with its result."),
        mcq("discriminate", 3, "By card 49, why is this section called Śarīra?",
            ("Birth and death are set forth in it", "यतः जन्ममरणं सम्यक् उदाहृतम्: since birth and death have been properly set forth."),
            [("It lists the drugs for the body", "Card 49 gives no drugs as the reason; it names birth and death."),
             ("Its first word is the word śarīra", "Card 49 gives the reason as birth and death, not a first word."),
             ("Vāgbhaṭa chose it for his father", "Card 49 says nothing of a father; the reason is birth and death.")],
            "Reason (यतः): birth and death set forth; result (ततः): the section is called Śarīra.",
            "यतः ... ततः."),
        mcq("apply", 4, "Which split of सम्यगुदाहृतं in card 49 is right?",
            ("सम्यक् + उदाहृतम्", "क् before a vowel becomes ग्: सम्यक् + उदाहृतम् → सम्यगुदाहृतम्."),
            [("सम्य + गुदाहृतम्", "गुदाहृतम् is not a word; the ग् comes from the क् of सम्यक्."),
             ("सम्यक् + गुदाहृतम्", "गुदाहृतम् is not a word; the participle is उदाहृतम्."),
             ("सम्यम् + उदाहृतम्", "सम्यम् is not a word; the adverb is सम्यक्.")],
            "सम्यक् (properly) + उदाहृतम् (set forth).",
            "क् + vowel → ग्."),
        mcq("transfer", 5, "By the pattern of सम्यक् + उदाहृतम् → सम्यगुदाहृतम्, how is प्राक् + एव (even before) joined in a new example?",
            ("प्रागेव", "क् before a vowel becomes ग्: प्राक् + एव → प्रागेव."),
            [("प्राकेव", "क् does not stay before a vowel; it becomes ग्."),
             ("प्राङेव", "ङ् would come from क् before a nasal; ए is a vowel."),
             ("प्राग्येव", "No य् is inserted; ग् joins ए directly.")],
            "प्राक् + एव = प्रागेव, like सम्यक् + उदाहृतम् = सम्यगुदाहृतम्.",
            "क् + vowel → ग्.",
            teaches="A final क् before a vowel becomes ग्: सम्यक् + उदाहृतम् → सम्यगुदाहृतम्."),
    ],
}

# ---------------------------------------------------------------- unit 50
AUTHORED["50"] = {
    "title": "इति दूतादिज्ञानीयो नाम द्वादशोऽध्यायः",
    "question": "What does the colophon of card 50 name, and how is its title formed?",
    "rule": ("Thus (इति) the twelfth chapter (द्वादशः अध्यायः), named (नाम) Dūtādijñānīya: 'relating to the knowledge of the messenger "
             "and the rest' (दूत-आदि-ज्ञानीय)."),
    "limits": "Prose colophon, high confidence. It names the chapter only; it says nothing about the content beyond the title.",
    "explain_hi": ("इस प्रकार दूतादिज्ञानीय नाम का बारहवाँ अध्याय (पूरा हुआ)। "
                   "नाम दूत + आदि + ज्ञानीय से बना है: दूत आदि के ज्ञान से सम्बन्धित; -ईय का अर्थ ‘से सम्बन्धित’। "
                   "‘द्वादशोऽध्यायः’ में द्वादशः + अध्यायः है: अः + अ → ओ, और अगला अ लुप्त होकर ऽ से दिखाया जाता है। "
                   "‘दूतादिज्ञानीयो नाम’ में अः घोष व्यंजन न से पहले ओ बना।"),
    "hook": "इति ... नाम ... अध्यायः — बारहवाँ अध्याय, दूतादिज्ञानीय।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 50, what does द्वादशः mean?",
            ("Twelfth", "द्वादश = twelfth (from द्वादशन्, twelve)."),
            [("Second", "Second would be द्वितीय; द्वादश = twelfth."),
             ("Tenth", "Tenth would be दशम; द्वादश = twelfth."),
             ("Eleventh", "Eleventh would be एकादश; द्वादश = twelfth.")],
            "द्वादशः = twelfth.",
            "द्वादश = twelfth."),
        match(1, "Match each word of card 50 to its meaning.",
              [["इति", "thus"], ["दूत", "messenger"], ["आदि", "and the rest"], ["नाम", "named"], ["अध्यायः", "chapter"]],
              "इति = thus, दूत = messenger, आदि = and the rest, नाम = named, अध्यायः = chapter.",
              "इति, दूत, आदि, नाम, अध्यायः."),
        order(2, "Put the words of card 50 in the printed order.",
              ["इति", "दूतादिज्ञानीयः", "नाम", "द्वादशः", "अध्यायः"],
              "Thus; Dūtādijñānīya; named; twelfth; chapter.",
              "इति → दूतादिज्ञानीयः → नाम → द्वादशः → अध्यायः.",
              role="extend",
              teaches="A chapter colophon runs: इति + title + नाम + number + अध्यायः."),
        mcq("discriminate", 3, "Which split of द्वादशोऽध्यायः in card 50 is right?",
            ("द्वादशः + अध्यायः", "अः before अ → ओ, and that अ is elided (ऽ): द्वादशोऽध्यायः."),
            [("द्वादश + अध्यायः", "अ + अ would give आ: that would print द्वादशाध्यायः."),
             ("द्वादशो + ध्यायः", "ध्यायः is not the word here; the noun is अध्यायः."),
             ("द्वादशे + अध्यायः", "द्वादशे is locative; the colophon names the chapter in the nominative.")],
            "द्वादशः (twelfth) + अध्यायः (chapter).",
            "अः + अ → ओऽ."),
        mcq("apply", 4, "What does the title दूतादिज्ञानीय mean literally?",
            ("Relating to knowing the messenger etc.", "दूत-आदि-ज्ञानीय: relating to the knowledge of the messenger and the rest."),
            [("The messenger who knows everything", "-ईय means 'relating to'; the title is not about an all-knowing messenger."),
             ("The first messenger's own knowledge", "आदि here is 'and the rest', not 'first'; -ईय means 'relating to'."),
             ("A journey made by the messenger", "No word for journey is in the title; ज्ञान is knowledge.")],
            "दूत (messenger) + आदि (and the rest) + ज्ञानीय (relating to knowledge).",
            "-ईय = relating to."),
        mcq("transfer", 5, "By the pattern of द्वादशः + अध्यायः → द्वादशोऽध्यायः, how is वृषभः + अस्ति (there is a bull) joined in a new example?",
            ("वृषभोऽस्ति", "अः before अ → ओ, and the अ is elided (ऽ): वृषभोऽस्ति."),
            [("वृषभास्ति", "आ comes from अ + अ without a visarga; here अः meets अ."),
             ("वृषभरस्ति", "र् comes from a visarga after vowels other than अ/आ."),
             ("वृषभ अस्ति", "Before अ the visarga of अः is not just dropped; it gives ओऽ.")],
            "वृषभः + अस्ति = वृषभोऽस्ति, like द्वादशः + अध्यायः = द्वादशोऽध्यायः.",
            "अः + अ → ओऽ.",
            teaches="अः before अ becomes ओ and the following अ is elided (ऽ): द्वादशः + अध्यायः → द्वादशोऽध्यायः."),
    ],
}

# ---------------------------------------------------------------- unit 51
AUTHORED["51"] = {
    "title": "द्वितीयं शारीरस्थानं संपूर्णं",
    "question": "By card 51, what is complete, in which work, and who composed it?",
    "rule": ("Thus, in the Aṣṭāṅgasaṅgraha composed (विरचिते) by the illustrious teacher Vāgbhaṭa, son (सूनु) of the illustrious Siṃhagupta, "
             "lord of physicians, the second (द्वितीयम्) Śārīrasthāna is complete (संपूर्णम्)."),
    "limits": ("Prose colophon, high confidence. वैद्यपति is taken as an epithet of Siṃhagupta ('lord of physicians'); it could be part of his "
               "name: no question on it. 'Is' is understood. The long first word is printed without a space after इति."),
    "explain_hi": ("इस प्रकार वैद्यपति श्रीसिंहगुप्त के पुत्र (सूनु) श्रीमान् वाग्भटाचार्य द्वारा रचित अष्टाङ्गसंग्रह में दूसरा शारीरस्थान सम्पूर्ण हुआ। "
                   "‘वैद्यपति’ सिंहगुप्त का विशेषण (वैद्यों के स्वामी) माना गया; यह नाम का भाग भी हो सकता है, इसलिए इस पर प्रश्न नहीं। "
                   "कार्ड ५० अध्याय का अन्त बताता है, कार्ड ५१ पूरे स्थान (विभाग) का। "
                   "‘विरचितेऽष्टांगसंग्रहे’ में विरचिते + अष्टाङ्गसंग्रहे है: ए + अ → ए, अ लुप्त (ऽ)।"),
    "hook": "सिंहगुप्त के पुत्र वाग्भट: दूसरा शारीरस्थान सम्पूर्ण।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By card 51, whose son is Vāgbhaṭa?",
            ("Siṃhagupta's son", "सिंहगुप्त-सूनु: the son of Siṃhagupta."),
            [("Śrīkṛṣṇa's son", "Kṛṣṇa is named only in the dedication of card 52, not as a father."),
             ("No father's name", "A father is named: सिंहगुप्तसूनु, son of Siṃhagupta."),
             ("His teacher's son", "आचार्य (teacher) is Vāgbhaṭa's own title; the father is Siṃhagupta.")],
            "सूनु = son: Vāgbhaṭa, son of Siṃhagupta.",
            "सिंहगुप्त + सूनु = son of Siṃhagupta."),
        match(1, "Match each word of card 51 to its meaning.",
              [["सूनु", "son"], ["आचार्य", "teacher"], ["विरचिते", "composed"], ["द्वितीयम्", "second"], ["संपूर्णम्", "complete"]],
              "सूनु = son, आचार्य = teacher, विरचिते = composed, द्वितीयम् = second, संपूर्णम् = complete.",
              "सूनु, आचार्य, विरचिते, द्वितीयम्, संपूर्णम्."),
        order(2, "Put the parts of card 51 in the printed order.",
              ["इति", "श्रीवैद्यपतिसिंहगुप्तसूनु-", "श्रीमद्वाग्भटाचार्यविरचिते", "अष्टाङ्गसंग्रहे", "द्वितीयं शारीरस्थानम्", "संपूर्णम्"],
              "Thus; son of Siṃhagupta; composed by Vāgbhaṭa; in the Aṣṭāṅgasaṅgraha; the second Śārīrasthāna; complete.",
              "इति → ...सूनु- → ...विरचिते → अष्टाङ्गसंग्रहे → द्वितीयं शारीरस्थानम् → संपूर्णम्.",
              role="extend",
              teaches="A section colophon: इति + author (in a compound ending -विरचिते) + work (locative) + section + संपूर्णम्."),
        mcq("discriminate", 3, "Which part of the book does card 51 say is complete?",
            ("The second section, Śārīrasthāna", "द्वितीयं शारीरस्थानं संपूर्णम्: the second section is complete."),
            [("The first section, Sūtrasthāna", "Card 51 names the second section, शारीरस्थान, not the first."),
             ("Only the twelfth chapter of it", "The twelfth chapter closes in card 50; card 51 closes the whole section."),
             ("The whole Aṣṭāṅgasaṅgraha work", "Only the second section is said to be complete, not the whole work.")],
            "Card 50: the chapter ends; card 51: the second section (Śārīrasthāna) is complete.",
            "द्वितीयं शारीरस्थानं संपूर्णम्."),
        mcq("apply", 4, "Which split of विरचितेऽष्टांगसंग्रहे in card 51 is right?",
            ("विरचिते + अष्टाङ्गसंग्रहे", "ए before अ stays ए and the अ is elided (ऽ): विरचितेऽष्टाङ्गसंग्रहे."),
            [("विरचितः + अष्टाङ्गसंग्रहे", "अः before अ would give ओऽ: विरचितोऽष्टाङ्ग..."),
             ("विरचिते + ष्टाङ्गसंग्रहे", "ष्टाङ्गसंग्रहे is not a word; the title is अष्टाङ्गसंग्रह."),
             ("विरचित + इष्टाङ्गसंग्रहे", "अ + इ would give ए, but इष्टाङ्ग is not the title.")],
            "विरचिते (composed, locative) + अष्टाङ्गसंग्रहे (in the Aṣṭāṅgasaṅgraha).",
            "ए + अ → एऽ."),
        mcq("transfer", 5, "By the pattern of विरचिते + अष्टाङ्गसंग्रहे, how is गृहे + अत्र (here in the house) joined in a new example?",
            ("गृहेऽत्र", "ए before अ stays ए and the अ is elided (ऽ): गृहे + अत्र → गृहेऽत्र."),
            [("गृहात्र", "आ comes from अ + अ; here ए meets अ."),
             ("गृहयत्र", "अय् comes from ए before vowels other than अ."),
             ("गृहैत्र", "ऐ comes from अ + ए; here ए meets अ.")],
            "गृहे + अत्र = गृहेऽत्र, like विरचिते + अष्टाङ्ग- = विरचितेऽष्टाङ्ग-.",
            "ए + अ → एऽ.",
            teaches="A final ए before अ stays and the अ is elided (written ऽ): विरचिते + अष्टाङ्गसंग्रहे → विरचितेऽष्टाङ्गसंग्रहे."),
    ],
}

# ---------------------------------------------------------------- unit 52
AUTHORED["52"] = {
    "title": "श्रीकृष्णार्पणमस्तु",
    "question": "What does the closing line of card 52 say?",
    "rule": "श्रीकृष्ण-अर्पणम् अस्तु: may it be an offering (अर्पणम्) to Śrī Kṛṣṇa. A closing dedication formula.",
    "limits": ("Prose, high confidence. The text does not say whether the line is the author's or was added by a printer or scribe: no "
               "question on it."),
    "explain_hi": ("‘श्रीकृष्णार्पणमस्तु’: श्रीकृष्ण को अर्पण हो। यह समाप्ति का समर्पण-वाक्य है। "
                   "यह लेखक का है या छापने वाले या लिपिकार ने जोड़ा, पाठ नहीं बताता, इसलिए इस पर प्रश्न नहीं। "
                   "‘अस्तु’ √अस् का लोट् (आज्ञार्थ) प्रथम पुरुष एकवचन है: हो। "
                   "सन्धियाँ: कृष्ण + अर्पणम् → कृष्णार्पणम् (अ + अ → आ); अर्पणम् + अस्तु → अर्पणमस्तु (स्वर से पहले म् जुड़कर लिखा जाता है)।"),
    "hook": "श्रीकृष्णार्पणमस्तु: यह सब श्रीकृष्ण को अर्पित हो।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 52, what does अर्पणम् mean?",
            ("Offering", "अर्पणम् = offering, dedication."),
            [("Blessing", "A blessing would be आशीः; अर्पणम् = offering."),
             ("Prayer", "A prayer would be प्रार्थना; अर्पणम् = offering."),
             ("Ending", "An ending would be समाप्ति; अर्पणम् = offering.")],
            "अर्पणम् = offering.",
            "अर्पण = offering."),
        match(1, "Match each part of card 52 to its meaning.",
              [["श्री", "illustrious"], ["कृष्ण", "Kṛṣṇa (a name)"], ["अर्पणम्", "offering"], ["अस्तु", "let it be"]],
              "श्री = illustrious, कृष्ण = Kṛṣṇa, अर्पणम् = offering, अस्तु = let it be.",
              "श्री, कृष्ण, अर्पणम्, अस्तु."),
        fill(2, "The word meaning 'let it be' in card 52 is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("अस्तु", "astu"),
             "अस्तु = let it be, may it be: printed in श्रीकृष्णार्पणमस्तु.",
             "अस्तु is the imperative of √अस् (to be), third person singular.",
             "अस्तु = let it be."),
        mcq("discriminate", 3, "Which split of कृष्णार्पणम् in card 52 is right?",
            ("कृष्ण + अर्पणम्", "अ + अ → आ: कृष्ण + अर्पणम् → कृष्णार्पणम्."),
            [("कृष्णः + अर्पणम्", "अः before अ would give ओऽ: कृष्णोऽर्पणम्."),
             ("कृष्णा + र्पणम्", "र्पणम् is not a word; the noun is अर्पणम्."),
             ("कृष्ण + रपणम्", "रपणम् is not a word, and it would print कृष्णरपणम्.")],
            "कृष्ण (Kṛṣṇa) + अर्पणम् (offering).",
            "अ + अ → आ."),
        mcq("apply", 4, "What verb form is अस्तु in card 52?",
            ("Imperative of √अस्", "अस्तु = let it be: imperative, third person singular."),
            [("Optative of √अस्", "The optative is स्यात् (as in card 43), not अस्तु."),
             ("Present of √अस्", "The present is अस्ति, not अस्तु."),
             ("Future form of √भू", "The future would be भविष्यति, not अस्तु.")],
            "अस्तु: imperative 3rd sg. of √अस्.",
            "अस्ति (is), स्यात् (would be), अस्तु (let it be)."),
        mcq("transfer", 5, "By the pattern of अर्पणम् + अस्तु → अर्पणमस्तु, how is दुग्धम् + आनय (bring the milk) written in a new example?",
            ("दुग्धमानय", "A final म् before a vowel stays म् and is written joined: दुग्धमानय."),
            [("दुग्धं आनय", "ं is written for म् only before a consonant; before a vowel म् stays."),
             ("दुग्धानय", "म् is not dropped before a vowel; it stays and joins."),
             ("दुग्धोऽनय", "ओऽ comes from अः before अ; here म् meets आ.")],
            "दुग्धम् + आनय = दुग्धमानय, like अर्पणम् + अस्तु = अर्पणमस्तु.",
            "Final म् + vowel → म् written joined.",
            teaches="A final म् before a vowel stays म् and joins the vowel: अर्पणम् + अस्तु → अर्पणमस्तु."),
    ],
}


# ================================================================ NOTES_HI
NOTES_HI = {
    "40": ("पद्य (डेटा का प्रकार); विश्वास निम्न; दो छपी पंक्तियाँ (०२.१२.४६ और ०२.१२.४७) जोड़ी गईं। पाठ-चिह्न (सम्भव): ‘विशामिषं’ से स्पष्ट शब्द नहीं बनता; "
           "श/ष की गड़बड़ी से विष् या विष + आमिष जैसे अनुमान सम्भव हैं, पर कोई पाठ नहीं अपनाया गया, शब्द अस्पष्ट छोड़ा गया। "
           "डेटा के अनुसार कार्ड ३८-३९ (छपी पंक्तियाँ ४२-४५) की सूची ‘पश्येत्’ का कर्म है और इस कार्ड की वस्तुएँ ‘लभते’ का; यह ‘सम्भवतः’ कहा गया। "
           "सन्धि जाँची: पश्येत् + लभते → पश्येल्लभते (त् + ल → ल्ल); यः + वा → यो वा (अः, घोष व्यंजन से पहले → ओ); "
           "छत्र + आदर्श → छत्रादर्श (अ + आ → आ); सुमनसः + वस्त्रम् → सुमनसो वस्त्रम्; वस्त्रम् + अमेध्य- → वस्त्रममेध्य-; अमेध्य + आलेपनम् → अमेध्यालेपनम्।"),
    "41": ("पद्य; विश्वास मध्यम; दो छपी पंक्तियाँ (०२.१२.४८ और ०२.१२.४९)। पाठ-चिह्न (सम्भव): छपा ‘तरेन्नदन्हदोदधीन्’ में ‘नदन्’ और ‘हद’ अपेक्षित शब्द नहीं देते; "
           "‘तरेत् नदान् ह्रदोदधीन्’ (नदों, झीलों, समुद्रों को पार करे) अनुमानित पाठ है; छन्द से कोई प्रमाण नहीं (दोनों पढ़ावों में आठ अक्षर)। "
           "पहली पंक्ति एक द्वन्द्व (द्वितीया बहुवचन), जिसके सदस्य ‘आरोहेत्’ के कर्म हैं। "
           "सन्धि जाँची: आरोहेत् + अश्वयानम् → आरोहेदश्वयानम् (स्वर से पहले त् → द्); अश्वयानम् + च → अश्वयानं च; "
           "तरेत् + न- → तरेन्न- (अनुनासिक से पहले त् → न् वैकल्पिक है, तरेद् न- भी शुद्ध)।"),
    "42": ("पद्य; विश्वास मध्यम; दो छपी पंक्तियाँ (०२.१२.५० और ०२.१२.५१); कोई पाठ-चिह्न नहीं। कोई क्रिया नहीं; डेटा के अनुसार शासक क्रिया कार्ड ४० का ‘पश्येत्’ "
           "या कार्ड ४३ का ‘स्यात्’ है, और विभक्तियाँ मिली-जुली हैं (मृतिम् द्वितीया, निःसृतिः प्रथमा)। ‘अगम्यागमन’ का शब्दार्थ लिया गया; "
           "धर्मशास्त्र वाला अर्थ यह पंक्ति नहीं कहती। ‘भास्वत्’ सूर्य का नाम भी है; अनुवाद ‘प्रकाशमान’ रखता है। "
           "सन्धि जाँची: पूर्व + उत्तरेण → पूर्वोत्तरेण (अ + उ → ओ); गमनम् + अगम्य- → गमनमगम्य-; अगम्य + आगमनम् → अगम्यागमनम्; "
           "संबाधात् + निःसृतिः → संबाधान्निःसृतिः (त् → न् वैकल्पिक, द् भी शुद्ध); स्पर्शः + तारका- → स्पर्शस्तारका-; तारका + अचल → तारकाचल।"),
    "43": ("पद्य; विश्वास निम्न; दो छपी पंक्तियाँ (०२.१२.५२ और ०२.१२.५३)। पाठ-चिह्न: ‘रोदनंपतितोत्थानं’ में रिक्त स्थान छूटा (निश्चित); "
           "‘सबहुशोऽश्रुते’ में ‘अश्रुते’ अर्थ नहीं देता, ‘अश्नुते’ (पाता है) अनुमानित पाठ (सम्भव)। "
           "दूसरी पंक्ति की वाक्य-रचना स्पष्ट नहीं: डेटा दो पद-योजनाएँ देता है (आयु, आरोग्य, धन सूची के सदस्य, या ‘अश्नुते’ के कर्म); अनुवाद मसौदे जैसा रखा गया। "
           "सन्धि जाँची: पतित + उत्थानम् → पतितोत्थानम्; च + अवमर्दनम् → चावमर्दनम्; स्यात् + आयुः → स्यादायुः; आयुः + आरोग्यम् → आयुरारोग्यम् "
           "(उ के बाद विसर्ग, स्वर से पहले → र्); सः + बहुशः → स बहुशः; बहुशः + अ- → बहुशोऽ-।"),
    "44": ("पद्य; विश्वास मध्यम; दो छपी पंक्तियाँ (०२.१२.५४ और ०२.१२.५५); कोई पाठ-चिह्न नहीं। दोनों पंक्तियाँ एक वाक्य। "
           "‘मलिनाम्बरपुष्पाणाम्’ अलग व्यक्तियों को या उन्हीं पितर आदि को बता सकता है (दो पढ़ाव; डेटा कार्ड ४५ की ओर संकेत करता है)। "
           "सन्धि जाँची: मलिन + अम्बर → मलिनाम्बर (छपा मलिनांबर); कृश + आत्मनाम् → कृशात्मनाम् (अ + आ → आ); "
           "-नाम् + क्रुद्ध- → -नां क्रुद्ध- (व्यंजन से पहले म् → ं)।"),
    "45": ("पद्य; विश्वास मध्यम; दो छपी पंक्तियाँ (०२.१२.५६ और ०२.१२.५७); कोई पाठ-चिह्न नहीं। ‘शुद्धपुष्पाम्बरात्मनाम्’ को ‘शुद्ध स्वरूप वाले, फूल-वस्त्र सहित’ "
           "भी पढ़ा जा सकता है; सरल पढ़ाव लिया गया। ‘शस्यते’ ‘प्रशस्यते’ (कार्ड ४४) की ही क्रिया है, उपसर्ग के बिना; भूल नहीं। "
           "सन्धि जाँची: तेषाम् + एव → तेषामेव; शुद्धपुष्प + अम्बर → शुद्धपुष्पाम्बर; तैः + च → तैश्च (च से पहले विसर्ग → श्)।"),
    "46": ("गद्य (डेटा का प्रकार); विश्वास निम्न; दो छपी पंक्तियाँ (०२.१२.५८ और ०२.१२.५९)। पाठ-चिह्न: ‘स्वप्मान्’ = स्वप्नान् (निश्चित); "
           "‘सर्पषानमिवर्णान्’ अस्पष्ट, पुनर्स्थापित नहीं (अन्त का -वर्णान् द्वितीया बहुवचन साफ़; सर्पिषा या सर्षपान् जैसे अनुमान केवल चिह्न में); "
           "‘त्विलान्’ = तिलान् (तिल; सम्भव, अनुमानित)। ‘हुत्वा’ का कर्म स्पष्ट नहीं; डेटा दूसरी पद-योजना भी देता है (घी में सने तिल)। "
           "सावित्री = सविता को सम्बोधित गायत्री मन्त्र (मानक)। "
           "सन्धि जाँची: सर्पिषा + आक्तान् → सर्पिषाऽऽक्तान् (आ + आ → आ; ऽऽ छपाई की आदत); पापैः + मुच्यते → पापैर्मुच्यते (ऐ के बाद विसर्ग, घोष म से पहले → र्); "
           "व्याधिभिः + च → व्याधिभिश्च।"),
    "47": ("पद्य; विश्वास मध्यम; दो छपी पंक्तियाँ (०२.१२.६० और ०२.१२.६१)। पाठ-चिह्न: ‘मंगलाचारसंपन्नःपरिवारस्तथाऽऽतुरः’ में रिक्त स्थान छूटे (निश्चित)। "
           "डेटा के अनुसार कार्ड ४७-४८ (छपी पंक्तियाँ ६०-६३) सम्भवतः एक सूची है। ध्यान दें: छपा ‘श्रद्धावानोऽनुकूलश्च’ श्रद्धावानः + अनुकूलः (अः + अ → ओऽ) जैसा पढ़ता है, "
           "पर डेटा का विच्छेद ‘श्रद्धावान्’ (पुं. प्रथमा एक.) देता है; इस रूप पर प्रश्न नहीं। "
           "सन्धि जाँची: मङ्गल + आचार → मङ्गलाचार; परिवारः + तथा → परिवारस्तथा (त से पहले विसर्ग → स्); तथा + आतुरः → तथाऽऽतुरः (आ + आ → आ); "
           "अनुकूलः + च → अनुकूलश्च।"),
    "48": ("पद्य; विश्वास मध्यम; दो छपी पंक्तियाँ (०२.१२.६२ और ०२.१२.६३); कोई पाठ-चिह्न नहीं। ‘तत्’ कार्ड ४७-४८ के लक्षणों की ओर। ‘सत्त्व’ शास्त्रीय शब्द, परिभाषा नहीं दी। "
           "सन्धि जाँची: संयोगः + भक्तिः → संयोगो भक्तिः (अः, घोष व्यंजन से पहले → ओ); भक्तिः + वैद्य- → भक्तिर्वैद्य- (इ के बाद विसर्ग, घोष व से पहले → र्); "
           "चिकित्सायाम् + अनिर्वेदः → चिकित्सायामनिर्वेदः; अनिर्वेदः + तत् → अनिर्वेदस्तत्; तत् + आरोग्यस्य → तदारोग्यस्य (स्वर से पहले त् → द्)।"),
    "49": ("पद्य; विश्वास मध्यम; दो छपी पंक्तियाँ (०२.१२.६४ और ०२.१२.६५)। पाठ-चिह्न: ‘ततःस्थानं’ में रिक्त स्थान छूटा (निश्चित)। "
           "‘इति’ को ‘इस प्रकार’ लिया गया; यह अगले नाम को उद्धृत भी कर सकता है। छपा नाम ‘शरीर’ है, ‘शारीर’ नहीं; कार्ड ५१ ‘शारीरस्थान’ कहता है। "
           "सन्धि जाँची: इति + अत्र → इत्यत्र (इ + अ → य); सम्यक् + उदाहृतम् → सम्यगुदाहृतम् (स्वर से पहले क् → ग्); "
           "शरीरम् + इदम् + उच्यते → शरीरमिदमुच्यते।"),
    "50": ("गद्य; विश्वास उच्च; एक छपी पंक्ति (०२.१२.६६); कोई पाठ-चिह्न नहीं। अध्याय का समाप्ति-वाक्य; आरम्भ में ॥ चिह्न। "
           "सन्धि जाँची: दूत + आदि → दूतादि; दूतादिज्ञानीयः + नाम → दूतादिज्ञानीयो नाम (अः, घोष न से पहले → ओ); द्वादशः + अध्यायः → द्वादशोऽध्यायः (अः + अ → ओऽ)।"),
    "51": ("गद्य; विश्वास उच्च; एक छपी पंक्ति (०२.१२.६७)। पाठ-चिह्न: ‘इति’ के बाद रिक्त स्थान छूटा (निश्चित)। ‘वैद्यपति’ सिंहगुप्त का विशेषण माना; नाम का भाग भी हो सकता है। "
           "सन्धि जाँची: श्रीमत् + वाग्भट → श्रीमद्वाग्भट (घोष व से पहले त् → द्); वाग्भट + आचार्य → वाग्भटाचार्य; "
           "विरचिते + अष्टाङ्गसंग्रहे → विरचितेऽष्टाङ्गसंग्रहे (ए + अ → एऽ); अष्ट + अङ्ग → अष्टाङ्ग।"),
    "52": ("गद्य; विश्वास उच्च; एक छपी पंक्ति (०२.१२.६८); कोई पाठ-चिह्न नहीं। समर्पण-वाक्य; लेखक का है या छापने वाले/लिपिकार का, पाठ नहीं बताता। "
           "सन्धि जाँची: कृष्ण + अर्पणम् → कृष्णार्पणम् (अ + अ → आ); अर्पणम् + अस्तु → अर्पणमस्तु।"),
}


# ================================================================ AIDS
AIDS = {
    "40": {
        "frame": "कौन: यः (जो) → क्रिया: पश्येत् (देखे) या लभते (पाता है) → क्या पाता है (सम्भवतः): छत्र, आदर्श, (अस्पष्ट), श्वेत पुष्प, वस्त्र, अमेध्य का लेप, फल।",
        "diagram": {"groups": [
            {"label": "लभते: पाता है, सम्भवतः (छपे क्रम में)",
             "items": ["१ छत्र", "२ आदर्श", "३ विशामिषं (अस्पष्ट)", "४ शुक्लाः सुमनसः", "५ वस्त्रम्", "६ अमेध्यालेपनम्", "७ फलम्"]}]},
        "chunks": "यः पश्येल्लभते | यो वा | छत्रादर्शविशामिषं || शुक्लाः सुमनसो | वस्त्रममेध्यालेपनं | फलं",
        "sandhi": "त् + ल → ल्ल: पश्येत् + लभते → पश्येल्लभते · अः, घोष व्यंजन से पहले → ओ: यः + वा → यो वा, सुमनसः + वस्त्रम् → सुमनसो वस्त्रम्।",
    },
    "41": {
        "diagram": {"groups": [
            {"label": "आरोहेत्: चढ़े (छपे क्रम में)",
             "items": ["१ शैल", "२ प्रासाद", "३ सफलवृक्ष", "४ सिंह", "५ नर", "६ द्विप", "७ अश्वयान"]},
            {"label": "तरेत्: पार करे", "items": ["नदन्हदोदधीन् (अनुमान: नदी, झील, समुद्र)"]}]},
        "chunks": "शैलप्रासादसफलवृक्षसिंहनरद्विपान् || आरोहेदश्वयानं च | तरेन्नदन्हदोदधीन्",
        "sandhi": "स्वर से पहले त् → द्: आरोहेत् + अश्वयानम् → आरोहेदश्वयानम् · व्यंजन से पहले म् → ं: अश्वयानम् + च → अश्वयानं च।",
        "pegs": "ऊँचे से ऊँचे पर चढ़ना: पर्वत, महल, पेड़, फिर सिंह, मनुष्य, हाथी, घोड़ा। (मेरा बनाया स्मरण-क्रम: पहले स्थिर, फिर जीव)",
    },
    "42": {
        "diagram": {"groups": [
            {"label": "कार्ड ४२ (छपे क्रम में)",
             "items": ["१ पूर्वोत्तरेण गमनम्", "२ अगम्यागमनम्", "३ मृतिम्", "४ संबाधान्निःसृतिः", "५ स्पर्शः तारकाचलभास्वताम्"]}]},
        "chunks": "पूर्वोत्तरेण गमनम् | अगम्यागमनं | मृतिं || संबाधान्निःसृतिः | स्पर्शस्तारकाचलभास्वतां",
        "sandhi": "अ + उ → ओ: पूर्व + उत्तरेण → पूर्वोत्तरेण · त से पहले विसर्ग → स्: स्पर्शः + तारका- → स्पर्शस्तारका- · आ + अ → आ: तारका + अचल → तारकाचल।",
        "letters": "विभक्तियाँ मिली-जुली: मृतिम् (द्वितीया), निःसृतिः (प्रथमा), संबाधात् (पंचमी, से), -भास्वताम् (षष्ठी बहु.)।",
    },
    "43": {
        "chain": {"steps": ["रोदनम्: रोना", "पतितोत्थानम्: गिरे का उठना", "द्विषताम् अवमर्दनम्: शत्रुओं का कुचलना",
                            "फिर: आयुः, आरोग्यम्, वित्तम् (वाक्य-रचना अस्पष्ट)"]},
        "chunks": "रोदनंपतितोत्थानं | द्विषतां चावमर्दनं || यस्य स्यादायुरारोग्यं | वित्तं सबहुशोऽश्रुते",
        "sandhi": "अ + उ → ओ: पतित + उत्थानम् → पतितोत्थानम् · अ + अ → आ: च + अवमर्दनम् → चावमर्दनम् · उ के बाद विसर्ग, स्वर से पहले → र्: आयुः + आरोग्यम् → आयुरारोग्यम्।",
    },
    "44": {
        "frame": "किनका: पितृ, देव, द्विजाति → कैसे: क्रुद्ध, भीत, कृश → और (या वही): मलिन वस्त्र-फूल वाले → दर्शनम् → न प्रशस्यते।",
        "chunks": "पितृदेवद्विजातीनां | क्रुद्धभीतकृशात्मनां || मलिनांबरपुष्पाणां | दर्शनं न प्रशस्यते",
        "sandhi": "अ + आ → आ: कृश + आत्मनाम् → कृशात्मनाम् · अ + अ → आ: मलिन + अम्बर → मलिनाम्बर।",
    },
    "45": {
        "frame": "तु (किन्तु) → किनका: तेषाम् एव (उन्हीं का) → कैसे: तुष्ट, शुद्ध फूल-वस्त्र → दर्शनं शस्यते स्वप्ने → तैः संभाषणं शुभम्।",
        "chunks": "तेषामेव तु तुष्टानां | शुद्धपुष्पांबरात्मनां || दर्शनं शस्यते स्वप्ने | तैश्च संभाषणं शुभं",
        "sandhi": "म् + स्वर → जुड़ता है: तेषाम् + एव → तेषामेव · च से पहले विसर्ग → श्: तैः + च → तैश्च।",
        "anchors": "प्र-शस्यते (कार्ड ४४) और शस्यते (यहाँ): एक ही √शंस्, उपसर्ग के साथ और बिना। (मेरी याद-पद्धति)",
    },
    "46": {
        "chain": {"steps": ["दृष्ट्वा: स्वप्न देखकर (दारुण या शोभन)", "प्रातः स्नातः = सुबह नहाया", "हुत्वा सावित्र्या: सावित्री से हवन",
                            "पूतः = पवित्र हुआ", "मुच्यते: पाप और रोग से मुक्त"]},
        "chunks": "दृष्ट्वा स्वप्मान् | दारुणान्शोभनान्वा | प्रातः स्नातः | सर्पषानमिवर्णान् || हुत्वा सावित्र्या | सर्पिषाऽऽक्तांस्त्विलान्वा | पूतः | पापैर्मुच्यते व्याधिभिश्च",
        "sandhi": "ऐ के बाद विसर्ग, घोष म से पहले → र्: पापैः + मुच्यते → पापैर्मुच्यते · च से पहले विसर्ग → श्: व्याधिभिः + च → व्याधिभिश्च।",
        "letters": "-त्वा = करके: दृष्ट्वा (देखकर), हुत्वा (हवन करके)। -तः = हुआ: स्नातः, पूतः।",
    },
    "47": {
        "frame": "परिवारः = मङ्गलाचारसंपन्नः → तथा आतुरः = श्रद्धा वाला, अनुकूल, प्रभूतद्रव्यसंग्रह → (कार्ड ४८: तत् आरोग्यस्य लक्षणम्)।",
        "chunks": "मंगलाचारसंपन्नःपरिवारस्तथाऽऽतुरः || श्रद्धावानोऽनुकूलश्च | प्रभूतद्रव्यसंग्रहः",
        "sandhi": "त से पहले विसर्ग → स्: परिवारः + तथा → परिवारस्तथा · आ + आ → आ: तथा + आतुरः → तथाऽऽतुरः · च से पहले विसर्ग → श्: अनुकूलः + च → अनुकूलश्च।",
    },
    "48": {
        "diagram": {"groups": [
            {"label": "कार्ड ४७: परिवार और रोगी", "items": ["मंगल आचार", "श्रद्धा", "अनुकूलता", "प्रचुर द्रव्य"]},
            {"label": "कार्ड ४८", "items": ["सत्त्व के लक्षण", "वैद्य-द्विज में भक्ति", "चिकित्सा में अनिर्वेद"]},
            {"label": "फल", "items": ["तत् आरोग्यस्य लक्षणम्"]}]},
        "chunks": "सत्त्वलक्षणसंयोगो | भक्तिर्वैद्यद्विजातिषु || चिकित्सायामनिर्वेदस्तदारोग्यस्य | लक्षणं",
        "sandhi": "अः, घोष व्यंजन से पहले → ओ: संयोगः + भक्तिः → संयोगो भक्तिः · इ के बाद विसर्ग, घोष से पहले → र्: भक्तिः + वैद्य- → भक्तिर्वैद्य- · त से पहले विसर्ग → स्: अनिर्वेदः + तत् → अनिर्वेदस्तत्।",
        "pegs": "स-भ-अ: सत्त्व, भक्ति, अनिर्वेद, कार्ड ४८ के तीन लक्षणों के पहले अक्षर। (मेरा बनाया स्मरण-सूत्र)",
    },
    "49": {
        "chain": {"steps": ["यतः = क्योंकि", "जन्ममरणं सम्यगुदाहृतम्: जन्म-मरण ठीक से कहे", "ततः = इसलिए",
                            "शरीरस्य स्थानम्: शरीर का विभाग", "शरीरम् उच्यते: नाम ‘शरीर’"]},
        "chunks": "इत्यत्र | जन्ममरणं | यतः सम्यगुदाहृतं || शरीरस्य | ततःस्थानं | शरीरमिदमुच्यते",
        "sandhi": "इ + अ → य: इति + अत्र → इत्यत्र · स्वर से पहले क् → ग्: सम्यक् + उदाहृतम् → सम्यगुदाहृतम् · म् + स्वर → जुड़ता है: शरीरम् + इदम् → शरीरमिदम्।",
    },
    "50": {
        "frame": "इति → नाम: दूतादिज्ञानीयः → क्रम: द्वादशः → अध्यायः।",
        "chunks": "॥ इति | दूतादिज्ञानीयो नाम | द्वादशोऽध्यायः",
        "sandhi": "अः + अ → ओऽ: द्वादशः + अध्यायः → द्वादशोऽध्यायः · अः, घोष व्यंजन से पहले → ओ: दूतादिज्ञानीयः + नाम → दूतादिज्ञानीयो नाम।",
    },
    "51": {
        "frame": "इति → रचयिता: सिंहगुप्त के पुत्र वाग्भटाचार्य → ग्रन्थ: अष्टाङ्गसंग्रहे → भाग: द्वितीयं शारीरस्थानम् → संपूर्णम्।",
        "chunks": "इतिश्रीवैद्यपतिसिंहगुप्तसूनुश्रीमद्वाग्भटाचार्यविरचितेऽष्टांगसंग्रहे | द्वितीयं शारीरस्थानं | संपूर्णं",
        "sandhi": "ए + अ → एऽ: विरचिते + अष्टाङ्ग- → विरचितेऽष्टाङ्ग- · घोष व से पहले त् → द्: श्रीमत् + वाग्भट → श्रीमद्वाग्भट।",
    },
    "52": {
        "chunks": "श्रीकृष्णार्पणमस्तु",
        "sandhi": "अ + अ → आ: कृष्ण + अर्पणम् → कृष्णार्पणम् · म् + स्वर → जुड़ता है: अर्पणम् + अस्तु → अर्पणमस्तु।",
        "letters": "√अस् के तीन रूप: अस्ति (है), स्यात् (हो सकता है, कार्ड ४३), अस्तु (हो)।",
    },
}


# ================================================================ IMAGE_SPECS
IMAGE_SPECS = {
    ("40", "diagram"): {
        "file": "sh12-labhate-40.svg",
        "alt": ("Table of card 40 in printed order, the items of labhate (obtains): umbrella, mirror, viśāmiṣaṃ (unclear), "
                "white flowers, cloth, smearing with impure matter, fruit."),
        "type": "table",
        "title": "कार्ड ४०: लभते (पाता है), सम्भवतः",
        "heads": ["क्रम", "छपा शब्द: अर्थ"],
        "rows": [["१", "छत्र: छाता"], ["२", "आदर्श: दर्पण"], ["३", "विशामिषं: अस्पष्ट"], ["४", "शुक्लाः सुमनसः = श्वेत फूल"],
                 ["५", "वस्त्रम्: वस्त्र"], ["६", "अमेध्यालेपनम्: अशुद्ध लेप"], ["७", "फलम्: फल"]],
    },
    ("41", "diagram"): {
        "file": "sh12-arohet-41.svg",
        "alt": ("Table of card 41 in printed order, the objects of ārohet (should climb): mountain, palace, fruit-bearing tree, lion, "
                "man, elephant, horse-vehicle; then taret (should cross), its objects a conjectural reading."),
        "type": "table",
        "title": "कार्ड ४१: आरोहेत् (चढ़े)",
        "heads": ["क्रम", "छपा शब्द: अर्थ"],
        "rows": [["१", "शैल: पर्वत"], ["२", "प्रासाद: महल"], ["३", "सफलवृक्ष: फलदार पेड़"], ["४", "सिंह: सिंह"],
                 ["५", "नर: मनुष्य"], ["६", "द्विप: हाथी"], ["७", "अश्वयान: घोड़ा-वाहन"], ["फिर", "तरेत्: पार करे (किसे, यह अनुमान)"]],
    },
    ("42", "diagram"): {
        "file": "sh12-svapna-42.svg",
        "alt": ("Table of card 42 in printed order: going by the north-east, approaching the unapproachable, death, emerging from a "
                "confined place, touching stars, mountains and radiant ones."),
        "type": "table",
        "title": "कार्ड ४२: छपे क्रम में",
        "heads": ["क्रम", "छपा शब्द: अर्थ"],
        "rows": [["१", "पूर्वोत्तरेण गमनम्: ईशान को जाना"], ["२", "अगम्यागमनम्: अगम्य तक जाना"], ["३", "मृतिम्: मृत्यु"],
                 ["४", "संबाधान्निःसृतिः = तंग से निकलना"], ["५", "स्पर्शः = तारे, पर्वत, प्रकाशमान"]],
    },
    ("46", "chain"): {
        "file": "sh12-svapnashanti-46.svg",
        "alt": "Chain of card 46: having seen dreams; bathed in the morning; having offered with the Sāvitrī; purified; freed from sins and diseases.",
        "type": "chain",
        "title": "कार्ड ४६: क्रम से",
        "steps": ["दृष्ट्वा: स्वप्न देखकर", "प्रातः स्नातः = सुबह नहाकर", "हुत्वा सावित्र्या: सावित्री से हवन", "पूतः = पवित्र",
                  "मुच्यते: पाप, रोग से मुक्त"],
    },
    ("48", "diagram"): {
        "file": "sh12-arogya-48.svg",
        "alt": ("Table of cards 47 and 48, which the data takes as one list: auspicious conduct, faith, favourableness, abundant "
                "materials (card 47); marks of sattva, devotion to physicians and twice-born, non-despondency in treatment (card 48); "
                "that is the sign of health."),
        "type": "table",
        "title": "कार्ड ४७-४८: आरोग्य का लक्षण",
        "heads": ["कार्ड", "लक्षण"],
        "rows": [["४७", "परिवार: मंगल आचार"], ["४७", "रोगी: श्रद्धा, अनुकूल"], ["४७", "प्रचुर द्रव्य-संग्रह"],
                 ["४८", "सत्त्व के लक्षण"], ["४८", "वैद्य-द्विज में भक्ति"], ["४८", "चिकित्सा में अनिर्वेद"],
                 ["फल", "तत् आरोग्यस्य लक्षणम्"]],
    },
    ("49", "chain"): {
        "file": "sh12-sharira-49.svg",
        "alt": ("Chain of card 49: since birth and death are properly set forth, therefore this section of the body is called "
                "Śarīra."),
        "type": "chain",
        "title": "कार्ड ४९: यतः ... ततः",
        "steps": ["यतः = क्योंकि", "जन्म-मरण ठीक से कहे", "ततः = इसलिए", "नाम: ‘शरीर’"],
    },
}
