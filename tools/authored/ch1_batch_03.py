from helpers import mcq, match, order, fill, multi, accepts

AUTHORED = {}

# ---------------------------------------------------------------- unit 26
AUTHORED["26"] = {
    "title": "तेऽर्थप्रत्यायनपरा",
    "question": "What does this unit say the Aṣṭāṅgasaṃgraha comes out of?",
    "rule": ("Having condensed all the treatises (सर्वतंत्राणि संहृत्य), the "
             "Compendium of the Eight Limbs comes. Line 1 says the earlier "
             "texts were intent on conveying meaning."),
    "limits": ("Line 1 after 'they were intent on conveying the meaning' "
               "(यच्चनादृताः) is unclear in the print, and the word प्राधः in "
               "line 2 is not a word (प्राज्ञः is only a suggestion). The "
               "sentence has no stated verb and goes on in units 27 and 28."),
    "explain_hi": ("यहाँ ग्रंथ का परिचय शुरू होता है। पहली पंक्ति कहती है कि वे "
                   "(पूर्व ग्रंथ) अर्थ समझाने में लगे थे; आगे का अंश "
                   "(‘यच्चनादृताः’) छपाई में अस्पष्ट है, इसलिए उस पर भरोसा नहीं "
                   "किया गया। दूसरी पंक्ति साफ़ है: ‘अतः’ (इसलिए) सभी तंत्रों को "
                   "‘संहृत्य’ (संक्षिप्त करके) अष्टांगसंग्रह (आता है)। यह वाक्य "
                   "अगले दो युग्मों में भी चलता है, जहाँ इस ग्रंथ के गुण गिनाए जाते हैं।"),
    "hook": "सब तंत्र समेटकर, इसलिए — अष्टांगसंग्रह।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "What is the Aṣṭāṅgasaṃgraha said to be, in relation to the earlier treatises?",
            ("A condensing of all the treatises into one work",
             "सर्वतंत्राणि संहृत्य: having condensed all the treatises."),
            [("A refutation of all the treatises that came before it",
              "Nothing in the line speaks of refuting."),
             ("A copy of one single treatise, word for word",
              "The line says all the treatises, and condensed."),
             ("A commentary that explains one treatise line by line",
              "The line says it condenses them; it does not call itself a commentary.")],
            "संहृत्य means having condensed, and सर्वतंत्राणि is all the treatises.",
            "सर्वतंत्राणि संहृत्य = having condensed all the treatises."),
        match(1, "Match each word of line 2 to its meaning.",
              [["सर्वतंत्राणि", "all treatises"], ["अतः", "therefore"],
               ["संहृत्य", "having condensed"],
               ["अष्टांगसंग्रहः", "Compendium of the Eight Limbs"]],
              "These four words carry the whole claim of the second line.",
              "सर्वतंत्राणि = all treatises; अतः = therefore; संहृत्य = having condensed."),
        fill(2, "The word for 'therefore' is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("अतः"),
             "अतः means therefore: it links the claim to what came before.",
             "अतः ('from this, therefore') begins a result: the earlier texts are the reason, the compendium is the result.",
             "अतः = therefore.", role="extend"),
        mcq("discriminate", 3, "Which is the right split of सर्वतंत्राण्यतः?",
            ("सर्वतंत्राणि + अतः",
             "इ before a different vowel becomes य्: णि + अ gives ण्य."),
            [("सर्वतंत्राण + यतः", "यतः is not what stands here, and the first part would end in -अ."),
             ("सर्वतंत्राणे + अतः", "-ए + अ would give -ए with an avagraha, not ण्य."),
             ("सर्वतंत्राणः + अतः", "A visarga before अ would give -ओऽ, not ण्य.")],
            "सर्वतंत्राणि (all treatises, neuter plural) + अतः (therefore).",
            "इ + different vowel → य् + vowel: णि + अतः = ण्यतः.", ),
        order(4, "Put these parts of line 2 in the order of the verse (leaving out the unclear word).",
              ["सर्वतंत्राणि", "अतः", "संहृत्य", "अष्टांगसंग्रहः"],
              "The line runs: all treatises, therefore, having condensed, the Aṣṭāṅgasaṃgraha.",
              "सर्वतंत्राणि · अतः · संहृत्य · अष्टांगसंग्रहः.", role="apply"),
        mcq("transfer", 5,
            "Which form of सं + ग्रह् (collect) ends like संहृत्य, 'having condensed'?",
            ("संगृह्य",
             "A verb with a prefix forms its 'having done' form in -य, as संहृत्य does."),
            [("संगृहीत्वा", "-त्वा goes on a verb without prefix; with a prefix it becomes -य."),
             ("संग्रहः", "This is a noun, 'a collection', not a 'having done' form."),
             ("संगृहीतम्", "This is 'collected' (a past participle), not 'having collected'.")],
            "संहृत्य (सं + हृ) is a 'having done' form with a prefix: it ends in -य (here -त्य).",
            "Prefix + verb → 'having done' in -य.",
            teaches="A verb with a prefix forms its 'having done' word in -य (संहृत्य, संगृह्य); without a prefix it takes -त्वा."),
    ],
}

# ---------------------------------------------------------------- unit 27
AUTHORED["27"] = {
    "title": "अस्थानविस्तराक्षेप",
    "question": "What is the work free from, and what does it rest on?",
    "rule": ("The work is free from misplaced elaboration, ākṣepa, repetition "
             "and the like, and rests only on three branches (स्कंध): cause "
             "(हेतु), sign (लिंग), medicine (औषध)."),
    "limits": ("The subject is the work of unit 26; it is not named here. "
               "आक्षेप can be 'objection' or 'digression'. The verse names the "
               "three branches and does not explain them."),
    "explain_hi": ("यह युग्म पिछले वाक्य को आगे बढ़ाता है और ग्रंथ की दो विशेषताएँ बताता "
                   "है। पहली पंक्ति में वह ‘वर्जित’ (रहित) है: अस्थान में विस्तार, "
                   "आक्षेप, पुनरुक्ति आदि से। दूसरी पंक्ति में वह केवल (‘मात्र’) तीन "
                   "स्कंधों पर टिका है: हेतु, लिंग और औषध। ‘आक्षेप’ का अर्थ आपत्ति भी हो सकता "
                   "है और विषयांतर भी, इसलिए उस पर प्रश्न नहीं बने। तीनों स्कंधों की "
                   "व्याख्या इस श्लोक में नहीं है।"),
    "hook": "विस्तार-पुनरुक्ति से मुक्त · बस तीन स्कंध: हेतु, लिंग, औषध।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "On which three branches (स्कंध) does the work rest, according to this unit?",
            ("Cause, sign and medicine",
             "हेतु, लिंग, औषध are the three branches in the second line."),
            [("Vāyu, Pitta and Kapha", "These come later, in unit 31, as the doṣas."),
             ("Birth, youth and old age", "Nothing like this is in the unit."),
             ("Food, sleep and conduct", "These are not named here.")],
            "The second line names हेतु, लिंग and औषध as the three branches.",
            "Three branches: हेतु, लिंग, औषध."),
        order(1, "Put the three branches in the order of the verse.",
              ["हेतु", "लिंग", "औषध"],
              "The line runs हेतु, लिंग, औषध.",
              "हेतु · लिंग · औषध."),
        mcq("extend", 2, "Which is the right split of हेतुलिंगौषध-?",
            ("हेतु + लिंग + औषध",
             "अ + औ gives औ, so लिंग + औषध is written लिंगौषध."),
            [("हेतु + लिंगो + षध", "षध is not a word."),
             ("हेतु + लिंगा + औषध", "That would be written लिंगौषध only with a long आ, which is not there."),
             ("हेतु + लिंग + ओषध", "That would be written लिंगोषध, with ओ, not औ.")],
            "Three words are joined: हेतु (cause), लिंग (sign), औषध (medicine).",
            "अ/आ + औ → औ: लिंग + औषध = लिंगौषध.",
            teaches="When a word ending in -अ meets a word beginning with औ, the two join as औ (लिंग + औषध = लिंगौषध)."),
        match(3, "Match each part of the compound to its meaning.",
              [["वर्जितः", "free from"], ["त्रय", "a group of three"],
               ["मात्र", "only"], ["निबंधनः", "resting on"]],
              "These four words build the two descriptions of the work.",
              "वर्जितः = free from; त्रय = group of three; मात्र = only; निबंधनः = resting on.",
              role="discriminate"),
        multi("apply", 4, "Which two does the unit say the work is free from?",
              [("elaboration out of place (अस्थानविस्तर)", "Right: it is the first item of the list."),
               ("repetition (पुनरुक्त)", "Right: it is named in the list."),
               ("cause (हेतु)", "Cause is one of the three branches the work rests on."),
               ("sign (लिंग)", "Sign is one of the three branches the work rests on."),
               ("medicine (औषध)", "Medicine is one of the three branches the work rests on.")],
              [0, 1],
              "वर्जित means free from: the work is free from misplaced elaboration and repetition (and ākṣepa). The three branches are what it rests on.",
              "Free from: अस्थानविस्तर, पुनरुक्त. Rests on: हेतु, लिंग, औषध."),
        mcq("transfer", 5,
            "An invented phrase says दोषवर्जितः, like पुनरुक्तादिवर्जितः. What does it mean?",
            ("Free from faults",
             "-वर्जित at the end of a compound means free from what comes before."),
            [("Full of faults", "वर्जित means free from, not full of."),
             ("Born of faults", "'Born of' would be -ज, not -वर्जित."),
             ("Measuring faults", "Nothing in the word means measuring.")],
            "X-वर्जित = free from X: अस्थान…आदिवर्जितः is 'free from … and the like'.",
            "X-वर्जित = free from X.",
            teaches="A compound ending in -वर्जित means 'free from' the first part (पुनरुक्तादिवर्जितः; दोषवर्जितः)."),
    ],
}

# ---------------------------------------------------------------- unit 28
AUTHORED["28"] = {
    "title": "विनिगूढार्थतत्त्वानां",
    "question": "What does the work illuminate, and what does it mostly remove?",
    "rule": ("The work is the illuminator (प्रकाशक) of passages whose meaning and "
             "essence are deeply hidden, and, for the most part (भूयिष्ठम्), the "
             "remover (विनिवर्तक) of contradictions with its own and other treatises."),
    "limits": ("Only 'for the most part' is claimed for the removal. The compound "
               "स्वान्यतंत्रविरोध can also be read 'contradictions within one's own "
               "and other tantras'. The sentence goes on into unit 29."),
    "explain_hi": ("यह युग्म ग्रंथ की दो और विशेषताएँ बताता है, दोनों ‘-क’ वाले कर्तावाची शब्दों "
                   "में: ‘प्रकाशकः’ (प्रकाश करने वाला) और ‘विनिवर्तकः’ (दूर करने वाला)। "
                   "पहला उन प्रसंगों को प्रकाशित करता है जिनका अर्थ और तत्त्व बहुत छिपा है। "
                   "दूसरा अपने और दूसरे तंत्रों के विरोधों को ‘भूयिष्ठम्’ (अधिकतर) दूर करता है; "
                   "यानी सारे विरोध मिटाने का दावा नहीं है। वाक्य अगली इकाई में भी चलता है।"),
    "hook": "छिपे अर्थ का प्रकाशक · विरोधों का (अधिकतर) निवारक।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "The work is the illuminator of what kind of passages?",
            ("Passages whose meaning and essence are deeply hidden",
             "विनिगूढार्थतत्त्वानां प्रदेशानां प्रकाशकः."),
            [("Passages that repeat what was said before",
              "Repetition is what unit 27 says the work avoids."),
             ("Passages that are easy to understand",
              "The verse says the hidden ones, not the easy ones."),
             ("Passages that are missing from other works",
              "Nothing in the verse speaks of missing passages.")],
            "विनिगूढ = deeply hidden; अर्थतत्त्व = meaning and essence; प्रदेश = passage, topic.",
            "प्रकाशकः illuminates passages of hidden meaning."),
        match(1, "Match each word of the verse to its meaning.",
              [["प्रकाशकः", "illuminator"], ["विनिवर्तकः", "remover"],
               ["विरोधानां", "of the contradictions"],
               ["भूयिष्ठं", "for the most part"]],
              "The two doers (प्रकाशक, विनिवर्तक) and the two words about their object and extent.",
              "प्रकाशकः = illuminator; विनिवर्तकः = remover; विरोध = contradiction; भूयिष्ठम् = for the most part."),
        fill(2, "The word for 'illuminator' is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("प्रकाशकः"),
             "प्रकाशकः = the one who makes something shine.",
             "A word ending in -क, like प्रकाशक and विनिवर्तक, names the doer of the action: one who illuminates, one who removes.",
             "प्रकाशकः = illuminator."),
        mcq("discriminate", 3, "Which pairing matches the verse?",
            ("Illuminator of hidden passages; remover of contradictions",
             "प्रकाशकः goes with the hidden passages and विनिवर्तकः with the contradictions."),
            [("Remover of hidden passages; illuminator of contradictions",
              "The two doers are swapped."),
             ("Illuminator of hidden passages and illuminator of contradictions",
              "The second doer is विनिवर्तकः, a remover."),
             ("Remover of hidden passages and remover of contradictions",
              "The first doer is प्रकाशकः, an illuminator.")],
            "प्रकाशक goes with the hidden passages, विनिवर्तक with the contradictions.",
            "प्रकाशकः: hidden passages. विनिवर्तकः: contradictions."),
        order(4, "Put these parts of the verse in order.",
              ["विनिगूढार्थतत्त्वानां", "प्रदेशानां", "प्रकाशकः",
               "स्वान्यतंत्रविरोधानां", "भूयिष्ठं", "विनिवर्तकः"],
              "The verse first names the hidden passages and their illuminator, then the contradictions, 'for the most part', and their remover.",
              "Hidden passages → illuminator → contradictions → for the most part → remover.",
              role="apply"),
        mcq("transfer", 5, "Join ग्रंथ + अर्थ in the way स्व + अन्य is joined. Which is right?",
            ("ग्रंथार्थ",
             "अ + अ gives आ, as in स्व + अन्य = स्वान्य."),
            [("ग्रंथोर्थ", "-ओ comes from a visarga, which is not there."),
             ("ग्रंथैर्थ", "-ऐ comes from अ + ए/ऐ, not from अ + अ."),
             ("ग्रंथर्थ", "The अ + अ do not drop out.")],
            "In स्वान्य both short अ meet and make one long आ.",
            "अ + अ → आ.",
            teaches="Two short अ side by side join as one long आ: स्व + अन्य = स्वान्य, ग्रंथ + अर्थ = ग्रंथार्थ."),
    ],
}

# ---------------------------------------------------------------- unit 29
AUTHORED["29"] = {
    "title": "युगानुरूपसंदर्शो",
    "question": "What will be made by divisions, according to line 1?",
    "rule": ("A presentation suited to the age (युगानुरूपसंदर्श) will be made "
             "(करिष्यते), by divisions (विभागेन)."),
    "limits": ("Line 2 is only partly clear: the doubtful word भास्वतः is a "
               "guess, and the line may qualify the next unit's 'collection of "
               "body-treatment'. No question is built on it. Confidence of "
               "the whole unit is low."),
    "explain_hi": ("पहली पंक्ति में एक प्रतिज्ञा है: ‘युग के अनुरूप संदर्शः’ यानी युग के "
                   "अनुकूल प्रस्तुति ‘विभागेन’ (विभाग करके) की जाएगी। ‘करिष्यते’ भविष्यत् "
                   "है, कर्म के अर्थ में: ‘किया जाएगा’। दूसरी पंक्ति (नित्य उपयोग, "
                   "सर्वांगव्यापि, ‘भास्वतः’) का पाठ अनिश्चित है और संभवतः अगली इकाई से जुड़ती "
                   "है, इसलिए यहाँ केवल पहली पंक्ति पर भरोसा किया गया है।"),
    "hook": "युग के अनुरूप प्रस्तुति — विभाग से — की जाएगी।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What does line 1 say will be done by divisions?",
            ("A presentation suited to the age",
             "युगानुरूपसंदर्शः विभागेन करिष्यते."),
            [("A refutation of the other treatises",
              "Nothing in line 1 speaks of refuting."),
             ("A list of all the drugs of the earth",
              "No drugs are named in line 1."),
             ("A translation into the common speech",
              "Nothing in line 1 speaks of translating.")],
            "संदर्शः is the presentation; युगानुरूप says it is suited to the age.",
            "Line 1: a presentation suited to the age will be made by divisions."),
        match(1, "Match each word of line 1 to its meaning.",
              [["युगानुरूप", "suited to the age"], ["संदर्शः", "presentation"],
               ["विभागेन", "by division"], ["करिष्यते", "will be made"]],
              "These are the four pieces of the announcement.",
              "युगानुरूप = suited to the age; संदर्शः = presentation; विभागेन = by division; करिष्यते = will be made."),
        fill(2, "The word for 'will be made' is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("करिष्यते"),
             "करिष्यते is future, third person singular, middle voice, with a passive sense.",
             "The -ष्य- in करिष्यते marks the future ('will'); the ending -ते with the passive sense gives 'will be made'.",
             "करिष्यते = will be made (future, passive sense)."),
        mcq("discriminate", 3,
            "One word is wrong in: 'A presentation suited to the book will be made, by division.' Which?",
            ("book", "युग means age, not book."),
            [("presentation", "संदर्शः is a presentation."),
             ("will be made", "करिष्यते is future: will be made."),
             ("by division", "विभागेन means by division.")],
            "The line says suited to the age (युग), not suited to a book.",
            "युग = age."),
        order(4, "Put these parts of line 1 in the order of the verse.",
              ["युगानुरूपसंदर्शः", "विभागेन", "करिष्यते"],
              "The line runs: presentation suited to the age, by division, will be made.",
              "युगानुरूपसंदर्शः · विभागेन · करिष्यते.", role="apply"),
        mcq("transfer", 5,
            "An invented line says क्रमेण वक्ष्यते, like विभागेन करिष्यते. What does it say?",
            ("It will be told in order",
             "क्रमेण = in order (a word in -एन gives the manner); वक्ष्यते = will be told."),
            [("It was told in disorder", "वक्ष्यते is future, not past; क्रमेण is not disorder."),
             ("It will be hidden by the order", "वक्ष्यते means told, not hidden."),
             ("It tells the future", "The verb is passive: it will be told, it does not tell.")],
            "A noun in -एन says how (by what means); a verb in -ष्यते is a future passive.",
            "-एन = by, in the manner of; -ष्यते = will be (done).",
            teaches="A noun ending in -एन says how the action is done (विभागेन, क्रमेण), and -ष्यते gives 'will be done'."),
    ],
}

# ---------------------------------------------------------------- unit 30
AUTHORED["30"] = {
    "title": "संगृहीतं विशेषेण",
    "question": "What is collected in particular, and what is said about āgama?",
    "rule": ("Treatment of the body (कायचिकित्सित) is collected in particular "
             "where this work stands; here not even a trifle is devoid of "
             "āgama (traditional authority)."),
    "limits": ("The verse says 'devoid of' (वर्जित), not 'contrary to'. It does not "
               "say what the āgama is. Line 2 of the previous unit may belong "
               "with this one."),
    "explain_hi": ("पहली पंक्ति ग्रंथ की एक विशेषता बताती है: यहाँ ‘कायचिकित्सित’ (शरीर की "
                   "चिकित्सा) का ‘विशेषेण’ (विशेष रूप से) संग्रह है। दूसरी पंक्ति कहती है कि "
                   "यहाँ थोड़ा-सा भी कुछ ‘आगमवर्जित’ नहीं है, यानी आगम से खाली नहीं। ध्यान दें: "
                   "‘वर्जित’ का अर्थ ‘रहित’ है, ‘विरुद्ध’ नहीं। ‘न … किंचित् … वर्जितम्’ "
                   "यानी ‘कुछ भी रहित नहीं’, अर्थात् सब कुछ आगम से युक्त है।"),
    "hook": "कायचिकित्सा का विशेष संग्रह · कुछ भी आगम से रहित नहीं।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What does the unit say is collected in particular?",
            ("The treatment of the body",
             "संगृहीतं विशेषेण यत्र कायचिकित्सितम्."),
            [("The rules of grammar", "Grammar is not named."),
             ("The names of all drugs", "No drugs are named here."),
             ("The verses of earlier works", "The unit does not speak of earlier verses in this way.")],
            "कायचिकित्सित is the treatment of the body; विशेषेण says it is collected especially.",
            "Collected in particular: कायचिकित्सित."),
        match(1, "Match each word to its meaning.",
              [["संगृहीतम्", "collected"], ["विशेषेण", "especially"],
               ["यत्र", "where"], ["वर्जितम्", "devoid of"]],
              "These four words give the two statements of the unit.",
              "संगृहीतम् = collected; विशेषेण = especially; यत्र = where; वर्जितम् = devoid of."),
        mcq("extend", 2, "Which is the right split of किंचिदागमवर्जितम्?",
            ("किंचित् + आगम + वर्जितम्",
             "Final त् becomes voiced द् before a vowel, so किंचित् + आगम is written किंचिदागम."),
            [("किंचिदा + गम + वर्जितम्", "गम is not the word here, and किंचिदा is not a word."),
             ("किंचिः + आगम + वर्जितम्", "A visarga would give a different join, and किंचिः is not a word."),
             ("किंचिद + आगम + वर्जितम्", "किंचिद is not a word; the word is किंचित्.")],
            "किंचित् (anything) + आगम (āgama) + वर्जितम् (devoid of).",
            "Final त् → द् before a vowel.",
            teaches="A final त् is voiced to द् when a vowel or voiced sound follows (किंचित् + आगम = किंचिदागम)."),
        mcq("discriminate", 3, "Which reading of line 2 fits the Sanskrit?",
            ("Here not the slightest thing is devoid of āgama",
             "वर्जित means devoid of."),
            [("Here not the slightest thing is contrary to āgama",
              "Contrary would need a word like विरुद्ध; वर्जित means devoid of."),
             ("Here something is devoid of āgama",
              "The न (not) makes it 'nothing'."),
             ("Here not the slightest thing is collected from āgama",
              "संगृहीत is in line 1 and says something else.")],
            "न … किंचित् … आगमवर्जितम्: nothing at all is devoid of āgama.",
            "आगमवर्जित = devoid of āgama."),
        order(4, "Put these parts of line 1 in the order of the verse.",
              ["संगृहीतं", "विशेषेण", "यत्र", "कायचिकित्सितं"],
              "The line runs: collected, especially, where, treatment of the body.",
              "संगृहीतं · विशेषेण · यत्र · कायचिकित्सितं.", role="apply"),
        mcq("transfer", 5,
            "An invented line says न किंचिदत्र दोषवर्जितम्, like न किंचिदागमवर्जितम्. What does it say?",
            ("Here nothing is free from faults",
             "न … किंचित् … वर्जितम् says nothing at all is free from that."),
            [("Here everything is free from faults", "The न reverses that: not anything is free from faults."),
             ("Here something is free from faults", "न किंचित् means not anything."),
             ("Here nothing has any fault", "That is the opposite: nothing is free from faults means faults are everywhere.")],
            "Not anything is free from faults: every item has them.",
            "न किंचित् … वर्जितम् = nothing at all is devoid of …",
            teaches="न किंचित् with an adjective negates it for every item: न किंचिदागमवर्जितम् = nothing is devoid of āgama."),
    ],
}

# ---------------------------------------------------------------- unit 31
AUTHORED["31"] = {
    "title": "वायुः पित्तं कफश्चेति",
    "question": "Which doṣas does the unit name, in brief?",
    "rule": ("In brief, the doṣas are three: Vāyu, Pitta and Kapha. Line 1 "
             "says those matters and that arrangement are for brevity, and "
             "the order is otherwise."),
    "limits": ("Line 1 is elliptical: 'the order is otherwise' (क्रमोऽन्यथा) is "
               "translated as the data gives it, with the verb supplied. "
               "Vāyu is the same as Vāta. The unit does not describe the doṣas."),
    "explain_hi": ("पहली पंक्ति संक्षेप की बात करती है: वे विषय और ग्रंथ की वह रचना "
                   "‘संक्षेपाय’ (संक्षेप के लिए) हैं और ‘क्रम अन्यथा’ है। यह पंक्ति "
                   "संक्षिप्त है और क्रिया ऊपर से जोड़ी गई है। दूसरी पंक्ति साफ़ है: संक्षेप "
                   "में दोष तीन हैं: वायु, पित्त और कफ। ‘कफश्चेति’ में कफः + च + इति जुड़े हैं, "
                   "और ‘त्रयो दोषाः’ में विसर्ग ‘ओ’ बन गया है।"),
    "hook": "संक्षेप में तीन दोष: वायु · पित्त · कफ।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "Which three doṣas does the unit name?",
            ("Vāyu, Pitta and Kapha",
             "वायुः पित्तं कफश्चेति त्रयो दोषाः."),
            [("Vāyu, Pitta and blood", "Blood is not named as a doṣa here."),
             ("Pitta, Kapha and the digestive fire", "The digestive fire (agni) is in unit 34, not a doṣa here."),
             ("Vāyu, Kapha and the belly", "The belly (koṣṭha) is in unit 35, not a doṣa here.")],
            "The second line names the three in order: वायुः, पित्तम्, कफः.",
            "Three doṣas: वायु, पित्त, कफ."),
        order(1, "Put the three doṣas in the order of the verse.",
              ["वायुः", "पित्तं", "कफः"],
              "The verse runs वायुः, पित्तम्, कफः.",
              "वायुः · पित्तं · कफः."),
        mcq("extend", 2, "Why is कफः + च written कफश्च?",
            ("A visarga before च becomes श्",
             "Before च or छ the visarga turns into श्."),
            [("A visarga before a voiced sound becomes ओ", "That is the rule after अ before a voiced sound; च is not voiced."),
             ("A visarga before a vowel becomes र्", "च is not a vowel."),
             ("A visarga drops out", "It does not drop here; it changes to श्.")],
            "कफः + च + इति joins as कफश्चेति: visarga + च → श्च, and च + इ → चे.",
            "Visarga + च/छ → श्.",
            teaches="A visarga before च or छ becomes श् (कफः + च = कफश्च)."),
        mcq("discriminate", 3, "Why is it त्रयो दोषाः and not त्रयः दोषाः?",
            ("A visarga after अ before a voiced consonant becomes ओ",
             "त्रयः ends in अः and द is voiced, so अः becomes ओ."),
            [("A visarga before द becomes श्", "श् comes before च or छ."),
             ("A visarga after अ always drops", "It does not drop before a voiced consonant; it turns to ओ."),
             ("The visarga turns to र् because दोषाः is long", "र् comes after other vowels, not after अ.")],
            "त्रयः + दोषाः = त्रयो दोषाः.",
            "अः + voiced consonant → ओ."),
        match(4, "Match each word to its meaning.",
              [["संक्षेपाय", "for brevity"], ["समासतः", "in brief"],
               ["वायुः", "Vāyu (wind-humour)"], ["क्रमः", "order"]],
              "These four words are in the two lines.",
              "संक्षेपाय = for brevity; समासतः = in brief; वायुः = Vāyu; क्रमः = order.",
              role="apply"),
        mcq("transfer", 5, "Join बालः + गच्छति by the rule of त्रयः + दोषाः. Which is right?",
            ("बालो गच्छति",
             "अः before a voiced consonant (ग) becomes ओ."),
            [("बालर्गच्छति", "र् is after other vowels, not after अ."),
             ("बालश्गच्छति", "श् comes before च or छ."),
             ("बालगच्छति", "The sound does not vanish.")],
            "बालः ends in अः and ग is voiced, so ओ.",
            "अः + voiced consonant → ओ.",
            teaches="After अ, a visarga before a voiced consonant becomes ओ (त्रयः + दोषाः = त्रयो दोषाः, बालः + गच्छति = बालो गच्छति)."),
    ],
}

# ---------------------------------------------------------------- unit 32
AUTHORED["32"] = {
    "title": "प्रत्येकं ते त्रिधा",
    "question": "In what ways does each doṣa vary, and how are increase and decrease graded?",
    "rule": ("Each doṣa is threefold by increase (वृद्धि), decrease (क्षय) and "
             "equilibrium (साम्य); increase and decrease are each threefold "
             "again: high, middling, low."),
    "limits": ("'They' (ते) are the three doṣas of unit 31. Only increase and "
               "decrease are graded here; equilibrium is not. The verse does "
               "not say what the grades do."),
    "explain_hi": ("‘ते’ यानी पिछले श्लोक के तीनों दोष। पहली पंक्ति: प्रत्येक दोष ‘त्रिधा’ "
                   "(तीन प्रकार का) है: वृद्धि, क्षय और साम्य के भेद से। दूसरी पंक्ति: "
                   "‘वृद्धि’ और ‘क्षय’ भी तीन-तीन प्रकार के हैं: उत्कृष्ट, मध्य और अल्प। साम्य "
                   "के भेद नहीं गिनाए गए। ‘वृद्धिक्षयावपि’ में वृद्धिक्षयौ + अपि जुड़े हैं "
                   "(औ + अ → आव्)।"),
    "hook": "हर दोष: वृद्धि · क्षय · साम्य; वृद्धि-क्षय के भी तीन दर्जे: उत्कृष्ट · मध्य · अल्प।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By which three states is each doṣa said to be threefold?",
            ("Increase, decrease and equilibrium",
             "वृद्धिक्षयसाम्यविभेदतः."),
            [("Birth, youth and old age", "These are not named in this unit."),
             ("Morning, noon and night", "These are not named in this unit."),
             ("High, middling and low", "These are the grades of increase and decrease, not the three states.")],
            "The first line names वृद्धि, क्षय and साम्य.",
            "Three states: वृद्धि, क्षय, साम्य."),
        match(1, "Match each word to its meaning.",
              [["वृद्धि", "increase"], ["क्षय", "decrease"],
               ["साम्य", "equilibrium"], ["उत्कृष्ट", "high"]],
              "The first three are the states of line 1; उत्कृष्ट is the first grade of line 2.",
              "वृद्धि = increase; क्षय = decrease; साम्य = equilibrium; उत्कृष्ट = high."),
        mcq("extend", 2, "Which is the right split of वृद्धिक्षयावपि?",
            ("वृद्धिक्षयौ + अपि",
             "-औ before a vowel becomes आव्, so वृद्धिक्षयौ + अपि is written वृद्धिक्षयावपि."),
            [("वृद्धिक्षया + वपि", "वपि is not a word."),
             ("वृद्धिक्षय + आवपि", "आवपि is not a word."),
             ("वृद्धिक्षयाव् + अपि", "वृद्धिक्षयाव् is not a word; the आव् is the join itself.")],
            "वृद्धिक्षयौ is a pair, increase and decrease; अपि means also.",
            "औ + vowel → आव् + vowel.",
            teaches="The sound औ turns into आव् before a vowel (वृद्धिक्षयौ + अपि = वृद्धिक्षयावपि); here -औ is the dual of the joined pair."),
        mcq("discriminate", 3, "Which does the verse say are graded high, middling and low?",
            ("Increase and decrease",
             "वृद्धिक्षयावपि: increase and decrease, too, are threefold."),
            [("Equilibrium only", "Equilibrium is not graded in this unit."),
             ("Increase, decrease and equilibrium", "Only increase and decrease are graded."),
             ("Increase only", "Decrease is named with it.")],
            "The second line grades वृद्धि and क्षय only.",
            "Graded: वृद्धि and क्षय."),
        order(4, "Put the three grades in the order of the verse.",
              ["उत्कृष्ट", "मध्य", "अल्प"],
              "The compound runs उत्कृष्ट, मध्य, अल्प.",
              "उत्कृष्ट · मध्य · अल्प.", role="apply"),
        mcq("transfer", 5,
            "An invented line says प्रत्येकं ते द्विधा, like प्रत्येकं ते त्रिधा. What does it say?",
            ("Each of them is twofold",
             "द्वि is two and -धा means in that many ways, as त्रि-धा is threefold."),
            [("Each of them is threefold", "त्रिधा is threefold; द्विधा is twofold."),
             ("Together they make two", "प्रत्येकम् means each, not together."),
             ("Each of them is single", "द्वि is two, not one.")],
            "A number + -धा gives 'in that many ways'.",
            "द्वि-धा = twofold; त्रि-धा = threefold.",
            teaches="A number + -धा means 'in that many ways': द्विधा twofold, त्रिधा threefold."),
    ],
}

# ---------------------------------------------------------------- unit 33
AUTHORED["33"] = {
    "title": "विकृताविकृता देहं",
    "question": "What do the doṣas do to the body, deranged and unaltered, and where do they sit?",
    "rule": ("Deranged (विकृत), they destroy the body; unaltered (अविकृत), they "
             "make it grow. Though pervading, they have their seats below, in "
             "the middle and above, the heart and navel."),
    "limits": ("The two halves are read in parallel order (deranged: destroy; "
               "unaltered: make grow). The verse does not say which doṣa sits "
               "where; 'heart and navel' are taken as the reference points."),
    "explain_hi": ("पहली पंक्ति: दोष ‘विकृत’ (बिगड़े हुए) हों तो देह का नाश करते हैं, "
                   "‘अविकृत’ (न बिगड़े) हों तो उसे बढ़ाते हैं। इस क्रम (विकृत: नाश, अविकृत: "
                   "वृद्धि) को समानांतर पढ़ा गया है। दूसरी पंक्ति: वे ‘व्यापी’ (सर्वत्र फैले) होने पर भी "
                   "हृदय और नाभि के अधः (नीचे), मध्य और ऊर्ध्व (ऊपर) आश्रित हैं। कौन-सा दोष कहाँ, "
                   "यह श्लोक नहीं बताता।"),
    "hook": "विकृत → देह का नाश · अविकृत → देह की वृद्धि · व्यापी, फिर भी अधः-मध्य-ऊर्ध्व में आश्रित।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What do the doṣas do to the body when they are deranged?",
            ("They destroy it",
             "विकृताः देहं घ्नन्ति: deranged, they strike the body down."),
            [("They make it grow", "That is what they do when unaltered."),
             ("They leave it unchanged", "The verse gives an effect for each state."),
             ("They protect it", "Protecting is not what the verse says.")],
            "घ्नन्ति means they destroy; it goes with विकृताः.",
            "विकृत → देह का नाश."),
        match(1, "Match each word to its meaning.",
              [["विकृताः", "deranged"], ["अविकृताः", "unaltered"],
               ["घ्नन्ति", "they destroy"], ["वर्द्धयन्ति", "they make grow"]],
              "The two states and the two results of line 1.",
              "विकृताः = deranged; अविकृताः = unaltered; घ्नन्ति = they destroy; वर्द्धयन्ति = they make grow."),
        mcq("extend", 2, "What does अविकृताः mean, built from the prefix अ- and विकृताः?",
            ("Not deranged, unaltered",
             "अ- negates: अ + विकृताः = not deranged."),
            [("Deranged more strongly", "अ- does not strengthen; it negates."),
             ("Born of derangement", "'Born of' would end in -ज."),
             ("Destroyed", "The word is about the state, not about being destroyed.")],
            "अ-विकृत is the opposite of विकृत.",
            "अ- before a word negates it.",
            teaches="The prefix अ- makes the opposite of a word (विकृत deranged, अविकृत unaltered)."),
        mcq("discriminate", 3, "Which pairing matches the unit?",
            ("Deranged: destroy; unaltered: make grow",
             "The first half says विकृत → घ्नन्ति, the second अविकृत → वर्द्धयन्ति."),
            [("Deranged: make grow; unaltered: destroy", "The two results are swapped."),
             ("Deranged and unaltered both destroy", "Unaltered ones make the body grow."),
             ("Deranged and unaltered both make it grow", "Deranged ones destroy it.")],
            "The verse reads in parallel: deranged with destroy, unaltered with make grow.",
            "विकृत: नाश; अविकृत: वृद्धि."),
        order(4, "Put the three places of the doṣas in the order of the verse.",
              ["अधः", "मध्य", "ऊर्ध्व"],
              "The compound runs below, middle, above.",
              "अधः · मध्य · ऊर्ध्व.", role="apply"),
        mcq("transfer", 5, "Join व्यापिनः + अपि the way the verse does. Which is right?",
            ("व्यापिनोऽपि",
             "अः + अ becomes ओऽ: the ऽ marks the dropped अ."),
            [("व्यापिनाऽपि", "A visarga after अ does not give आ."),
             ("व्यापिनःअपि", "The visarga does change before अ."),
             ("व्यापिनैऽपि", "ऐ comes from other sounds, not from अः.")],
            "अः + अ gives ओऽ.",
            "अः + अ → ओऽ.",
            teaches="A final अः meeting an अ joins as ओऽ (व्यापिनः + अपि = व्यापिनोऽपि)."),
    ],
}

# ---------------------------------------------------------------- unit 34
AUTHORED["34"] = {
    "title": "वयोऽहोरात्रिभुक्तानां",
    "question": "Where are the doṣas in order, and how does the digestive fire become irregular, sharp or slow?",
    "rule": ("They are in the end, middle and beginning, in order, of age, "
             "day, night and meal. Through them the fire (अग्नि) becomes "
             "irregular, sharp or slow; when they are even, it is even."),
    "limits": ("The verse does not say which doṣa goes with end, middle or "
               "beginning, nor which with irregular, sharp or slow; only the "
               "order is kept. 'अहोरात्रि' is read as अहः + रात्रि (day, night), "
               "so four items stand in the first compound."),
    "explain_hi": ("पहली पंक्ति: वे (दोष) आयु, दिन, रात और भोजन के अंत, मध्य और आदि में ‘क्रमात्’ "
                   "(क्रम से) रहते हैं। दूसरी पंक्ति: उनसे अग्नि ‘विषम’, ‘तीक्ष्ण’ या ‘मंद’ होती है, "
                   "और ‘समैः’ (सम दोषों से) ‘समः’ होती है। किस दोष से कौन-सी अग्नि, या कौन-सा दोष अंत, "
                   "मध्य, आदि में, यह श्लोक में नहीं है। ‘तैर्भवेद्’ में तैः का विसर्ग ‘र्’ बना है।"),
    "hook": "असम दोषों से अग्नि विषम · तीक्ष्ण · मंद; सम दोषों से सम।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "What is the digestive fire (अग्नि) when the doṣas are even?",
            ("Even (सम)", "समैः समः: with even ones, even."),
            [("Sharp (तीक्ष्ण)", "Sharp is one of the three irregular states."),
             ("Slow (मंद)", "Slow is one of the three irregular states."),
             ("Irregular (विषम)", "Irregular is one of the three irregular states.")],
            "The last words are समैः समः: even doṣas, even fire.",
            "सम दोष → सम अग्नि."),
        match(1, "Match each word to its meaning.",
              [["विषमः", "irregular"], ["तीक्ष्णः", "sharp"],
               ["मंदः", "slow"], ["समः", "even"]],
              "These four are the states of the fire in line 2.",
              "विषमः = irregular; तीक्ष्णः = sharp; मंदः = slow; समः = even."),
        mcq("extend", 2, "Why is तैः + भवेत् written तैर्भवेत्?",
            ("A visarga after ऐ before a voiced sound becomes र्",
             "After any vowel except अ and आ, a visarga turns into र् before a voiced sound."),
            [("A visarga after ऐ before a voiced sound becomes ओ", "ओ is the result only after अ."),
             ("A visarga before भ becomes श्", "श् comes before च or छ."),
             ("A visarga drops out", "It does not drop here; it becomes र्.")],
            "तैः (by them) + भवेत् (becomes): the visarga turns into र्.",
            "Visarga after ऐ + voiced sound → र्.",
            teaches="After a vowel other than अ or आ, a visarga before a voiced sound becomes र् (तैः + भवेत् = तैर्भवेत्)."),
        mcq("discriminate", 3, "Which word-order of the fire's irregular states is right?",
            ("विषम, तीक्ष्ण, मंद",
             "The verse runs विषमः तीक्ष्णः मंदः."),
            [("तीक्ष्ण, विषम, मंद", "The verse starts with विषम."),
             ("मंद, तीक्ष्ण, विषम", "This is the reverse of the verse."),
             ("विषम, मंद, तीक्ष्ण", "तीक्ष्ण comes second in the verse.")],
            "भवेद्विषमस्तीक्ष्णो मंदः: irregular, sharp, slow.",
            "विषम · तीक्ष्ण · मंद."),
        order(4, "Put the states of the fire in the order of the verse.",
              ["विषमः", "तीक्ष्णः", "मंदः", "समः"],
              "The verse runs irregular, sharp, slow, then even for the even doṣas.",
              "विषमः · तीक्ष्णः · मंदः · समः.", role="apply"),
        mcq("transfer", 5, "Join दोषैः + भवति the way तैः + भवेत् is joined. Which is right?",
            ("दोषैर्भवति",
             "A visarga after ऐ before a voiced sound (भ) becomes र्."),
            [("दोषैओ भवति", "ओ is the result after अ, not after ऐ."),
             ("दोषैश्भवति", "श् comes before च or छ."),
             ("दोषैभवति", "The visarga does not drop.")],
            "दोषैः ends in ऐः and भ is voiced, so र्.",
            "ऐः + voiced sound → ऐर्.",
            teaches="A visarga after ऐ (and other vowels besides अ, आ) becomes र् before a voiced sound: तैर्भवेत्, दोषैर्भवति."),
    ],
}

# ---------------------------------------------------------------- unit 35
AUTHORED["35"] = {
    "title": "कोष्ठः क्रूरो मृदुर्मध्यो",
    "question": "What kinds of koṣṭha does line 1 give, and which when the doṣas are even?",
    "rule": ("The koṣṭha (belly) is harsh (क्रूर), mild (मृदु) or medium (मध्य); "
             "it is medium also when those doṣas are even. Line 2 begins a "
             "comparison that continues in unit 36."),
    "limits": ("Line 2 is incomplete here (it runs on into unit 36) and its "
               "comparison with a poison-worm is elliptical; no question is "
               "built on the comparison. Confidence is medium."),
    "explain_hi": ("पहली पंक्ति: ‘कोष्ठ’ (पेट की गुहा) तीन तरह का है: ‘क्रूर’, ‘मृदु’ या ‘मध्य’। "
                   "जब वे दोष ‘सम’ होते हैं तब भी कोष्ठ ‘मध्य’ होता है। दूसरी पंक्ति कहती है कि "
                   "जन्म के आरंभ में शुक्र और आर्तव में स्थित उन दोषों से, ‘जैसे विष से "
                   "विष के कीड़े का’, और यह वाक्य अगली इकाई में पूरा होता है। तुलना अधूरी है, "
                   "इसलिए यहाँ उस पर सवाल नहीं हैं। ‘मृदुर्मध्यो’ में मृदुः का विसर्ग ‘र्’ बना है।"),
    "hook": "कोष्ठ: क्रूर · मृदु · मध्य; दोष सम हों तो भी मध्य।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What is the koṣṭha when those doṣas are even?",
            ("Medium (मध्य)", "मध्यः स्यात्तैः समैरपि: it is medium even when they are even."),
            [("Harsh (क्रूर)", "Harsh is one of the other two kinds."),
             ("Mild (मृदु)", "Mild is one of the other two kinds."),
             ("Not named", "Line 1 names it: medium.")],
            "The line ends: medium it would be, by even doṣas as well.",
            "सम दोष → कोष्ठ मध्य."),
        order(1, "Put the three kinds of koṣṭha in the order of the verse.",
              ["क्रूरः", "मृदुः", "मध्यः"],
              "The line runs क्रूरः, मृदुः, मध्यः.",
              "क्रूरः · मृदुः · मध्यः."),
        mcq("extend", 2, "Why is मृदुः + मध्यः written मृदुर्मध्यः?",
            ("A visarga after उ before a voiced sound becomes र्",
             "After a vowel other than अ or आ, a visarga turns into र् before a voiced sound."),
            [("A visarga after उ before a voiced sound becomes ओ", "ओ is the result only after अ."),
             ("A visarga before म becomes श्", "श् comes before च or छ."),
             ("A visarga after उ always stays", "It changes before a voiced sound.")],
            "मृदुः (mild) + मध्यः (medium) join as मृदुर्मध्यः.",
            "Visarga after उ + voiced sound → र्.",
            teaches="After उ (and other vowels except अ, आ) a visarga before a voiced sound becomes र् (मृदुः + मध्यः = मृदुर्मध्यः)."),
        mcq("discriminate", 3, "Which is the right split of शुक्रार्तवस्थैः?",
            ("शुक्र + आर्तव + स्थैः",
             "अ + आ gives आ, so शुक्र + आर्तव is written शुक्रार्तव; स्थैः means abiding in."),
            [("शुक्रा + र्तव + स्थैः", "र्तव is not a word."),
             ("शुक्र + अर्तव + स्थैः", "The word is आर्तव, with long आ."),
             ("शुक्रः + आर्तव + स्थैः", "A visarga would not give शुक्रा-.")],
            "शुक्र (semen) + आर्तव (menstrual blood) + स्थैः (abiding in).",
            "अ + आ → आ."),
        match(4, "Match each word to its meaning.",
              [["कोष्ठः", "belly, abdominal cavity"], ["क्रूरः", "harsh"],
               ["मृदुः", "mild"], ["जन्मादौ", "at the beginning of birth"]],
              "The first three are the kinds of koṣṭha; जन्मादौ is in line 2.",
              "कोष्ठः = belly; क्रूरः = harsh; मृदुः = mild; जन्मादौ = at the beginning of birth.",
              role="apply"),
        mcq("transfer", 5, "Join साधुः + जनः by the rule of मृदुः + मध्यः. Which is right?",
            ("साधुर्जनः",
             "A visarga after उ before a voiced sound (ज) becomes र्."),
            [("साधुओजनः", "ओ is the result only after अ."),
             ("साधुश्जनः", "श् comes before च or छ."),
             ("साधुजनः", "The visarga does not vanish.")],
            "साधुः ends in उः and ज is voiced, so र्.",
            "उः + voiced sound → उर्.",
            teaches="A visarga after उ turns into र् before a voiced sound (मृदुर्मध्यः, साधुर्जनः)."),
    ],
}

# ---------------------------------------------------------------- unit 36
AUTHORED["36"] = {
    "title": "समधातुः समस्तासु",
    "question": "Which constitution is best and which are censured, according to line 2?",
    "rule": ("The constitution with balanced constituents (समधातु) is the best "
             "among all; those born of two doṣas (द्विदोषज) are to be censured."),
    "limits": ("Confidence is low. Line 1 reads 'three constitutions' "
               "(तिस्रः प्रकृतयः) as printed, which does not fit line 2 well; "
               "'seven' (सप्त) is only a suggestion. No question is built on "
               "the number. Line 1 also completes the sentence of unit 35."),
    "explain_hi": ("दूसरी पंक्ति स्पष्ट है और यहाँ उसी पर भरोसा किया गया है: जिस प्रकृति में "
                   "धातुएँ ‘सम’ हैं, वह ‘समस्तासु’ (सबमें) ‘श्रेष्ठा’ है, और जो दो दोषों से उत्पन्न "
                   "हैं वे ‘निंद्याः’ (निंदनीय) हैं। पहली पंक्ति में छपा ‘तिस्रः’ (तीन) संदिग्ध है: "
                   "दूसरी पंक्ति के साथ बैठता नहीं, ‘सप्त’ केवल सुझाव है। इसलिए संख्या पर कोई प्रश्न "
                   "नहीं है। यह पंक्ति पिछली इकाई के वाक्य को भी पूरा करती है।"),
    "hook": "समधातु = सबसे श्रेष्ठ · द्विदोषज = निंद्य।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "Which constitution does line 2 call the best among all?",
            ("The one with balanced constituents",
             "समधातुः समस्तासु श्रेष्ठा."),
            [("The one born of two doṣas", "These are the ones to be censured."),
             ("The one with a single raised doṣa", "No such type is named in line 2."),
             ("The one that is inferior", "Inferior is a grade named in line 1, not the best.")],
            "समधातु = with balanced constituents; श्रेष्ठा = best.",
            "समधातु: best."),
        match(1, "Match each word of line 2 to its meaning.",
              [["समधातुः", "with balanced constituents"], ["श्रेष्ठा", "best"],
               ["निंद्याः", "to be censured"], ["द्विदोषजाः", "born of two doṣas"]],
              "The two kinds of constitution and their two verdicts.",
              "समधातुः = balanced; श्रेष्ठा = best; निंद्याः = to be censured; द्विदोषजाः = born of two doṣas."),
        mcq("extend", 2, "What does -ज at the end of द्विदोषजाः mean?",
            ("Born of, arising from",
             "द्विदोषजाः = born of two doṣas."),
            [("Seated in", "Seated in would be -स्थ."),
             ("Destroying", "Destroying would be -घ्न."),
             ("Free from", "Free from would be -वर्जित.")],
            "द्वि + दोष + ज: born of two doṣas.",
            "-ज = born of.",
            teaches="A compound ending in -ज means 'born of' the first part (द्विदोषज; invented: जलज, born of water)."),
        mcq("discriminate", 3, "Which pairing matches line 2?",
            ("Balanced: best; born of two doṣas: censured",
             "Line 2 gives श्रेष्ठा to समधातु and निंद्याः to द्विदोषजाः."),
            [("Balanced: censured; born of two doṣas: best", "The two verdicts are swapped."),
             ("Balanced and born of two doṣas: both best", "The two-doṣa types are censured."),
             ("Balanced and born of two doṣas: both censured", "The balanced type is best.")],
            "समधातु is called श्रेष्ठा; द्विदोषज are निंद्याः.",
            "समधातु: श्रेष्ठ; द्विदोषज: निंद्य."),
        order(4, "Put these parts of line 2 in the order of the verse.",
              ["समधातुः", "समस्तासु", "श्रेष्ठा", "निंद्या", "द्विदोषजाः"],
              "The line runs: balanced, among all, best, to be censured, born of two doṣas.",
              "समधातुः · समस्तासु · श्रेष्ठा · निंद्या · द्विदोषजाः.", role="apply"),
        mcq("transfer", 5,
            "An invented word समदोषः is built like समधातुः. What does it describe?",
            ("One with balanced doṣas",
             "सम + noun makes 'having that noun balanced', as समधातुः has balanced constituents."),
            [("One who destroys the doṣas", "Nothing in the word means destroying."),
             ("One born of two doṣas", "That would be द्विदोषज."),
             ("One with a single doṣa", "सम means even, not single.")],
            "सम-धातु (balanced constituents) → सम-दोष (balanced doṣas).",
            "सम + noun = having that noun balanced.",
            teaches="A compound सम + a noun, used of a person or type, means 'having that thing balanced' (समधातुः, समदोषः)."),
    ],
}

# ---------------------------------------------------------------- unit 37
AUTHORED["37"] = {
    "title": "तत्र रुक्षो लघुः शीतः",
    "question": "What qualities are given to Anila and to Pitta?",
    "rule": ("Anila: dry, light, cold, rough, subtle, moving. Pitta: oily, "
             "sharp, hot, light, rank-smelling, flowing, liquid. Light "
             "(लघु) is named for both."),
    "limits": ("'सस्नेह' is literally 'having oiliness'; some read 'slightly oily'. "
               "विस्र is kept as 'rank-smelling'. The verse lists qualities only: "
               "no effects or uses. Kapha follows in unit 38."),
    "explain_hi": ("‘तत्र’ (उनमें) अनिल (वायु) के गुण पहली पंक्ति में हैं: रूक्ष, लघु, शीत, खर, "
                   "सूक्ष्म, चल। दूसरी पंक्ति में पित्त के गुण हैं: सस्नेह, तीक्ष्ण, उष्ण, लघु, विस्र, सर, "
                   "द्रव। ‘लघु’ दोनों के लिए आया है, जबकि ‘शीत’ केवल अनिल के लिए और ‘उष्ण’ केवल "
                   "पित्त के लिए है। ‘सूक्ष्मश्चलोऽनिलः’ में सूक्ष्मः + चलः + अनिलः जुड़े हैं।"),
    "hook": "अनिल: रूक्ष लघु शीत खर सूक्ष्म चल · पित्त: सस्नेह तीक्ष्ण उष्ण लघु विस्र सर द्रव।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "Which quality is named for both Anila and Pitta in this unit?",
            ("Light (लघु)", "लघु is in line 1 for Anila and in line 2 for Pitta."),
            [("Cold (शीत)", "Cold is named for Anila only."),
             ("Hot (उष्ण)", "Hot is named for Pitta only."),
             ("Liquid (द्रव)", "Liquid is named for Pitta only.")],
            "लघुः for Anila and लघु for Pitta.",
            "लघु: Anila and Pitta."),
        match(1, "Match each word to its meaning.",
              [["रूक्षः", "dry"], ["खरः", "rough"],
               ["चलः", "moving"], ["द्रवं", "liquid"]],
              "Three are qualities of Anila, द्रवम् is a quality of Pitta.",
              "रूक्षः = dry; खरः = rough; चलः = moving; द्रवं = liquid."),
        mcq("extend", 2, "Which is the right split of चलोऽनिलः?",
            ("चलः + अनिलः",
             "अः + अ becomes ओऽ; the ऽ marks the dropped अ."),
            [("चला + अनिलः", "A long आ does not give ओऽ."),
             ("चल + उनिलः", "उनिलः is not a word."),
             ("चलोः + अनिलः", "चलोः is not a form here.")],
            "चलः (moving) + अनिलः (wind) is joined as चलोऽनिलः.",
            "अः + अ → ओऽ.",
            teaches="A final अः before अ joins as ओऽ (चलः + अनिलः = चलोऽनिलः); the avagraha ऽ stands for the dropped अ."),
        mcq("discriminate", 3,
            "One word is wrong in: 'Pitta is oily, sharp, hot, heavy, rank-smelling, flowing and liquid.' Which?",
            ("heavy", "The verse says लघु, light."),
            [("oily", "सस्नेह is oily."),
             ("hot", "उष्ण is hot."),
             ("liquid", "द्रव is liquid.")],
            "Pitta is light (लघु) in the verse, not heavy.",
            "Pitta: लघु = light."),
        order(4, "Put the qualities of Anila in the order of the verse.",
              ["रूक्षः", "लघुः", "शीतः", "खरः", "सूक्ष्मः", "चलः"],
              "Line 1 runs: dry, light, cold, rough, subtle, moving.",
              "रूक्ष · लघु · शीत · खर · सूक्ष्म · चल.", role="apply"),
        mcq("transfer", 5,
            "By the pattern of सस्नेह (having oiliness), what does the invented word सगंध mean?",
            ("Having smell",
             "स- at the start means having, as सस्नेह means having oiliness."),
            [("Without smell", "Without would be अ- or निर्-."),
             ("Destroying smell", "Nothing in the word means destroying."),
             ("Very bad smell", "स- does not say bad.")],
            "सस्नेह = स + स्नेह: with oiliness; सगंध = with smell.",
            "स- + noun = having that noun.",
            teaches="The prefix स- means 'having' (सस्नेह, having oiliness; सगंध, having smell)."),
    ],
}

# ---------------------------------------------------------------- unit 38
AUTHORED["38"] = {
    "title": "स्निग्धः शीतो गुरुर्मंदः",
    "question": "What qualities does Kapha have, and what gives saṃsarga and sannipāta?",
    "rule": ("Kapha: unctuous, cold, heavy, slow, smooth, clay-like, stable. "
             "Saṃsarga and sannipāta arise from the decrease or aggravation "
             "(क्षय, कोप) of two or three of them."),
    "limits": ("मृत्स्न is literally 'clayey'; commentators may explain it "
               "differently. The verb 'arise' is supplied. The verse does not "
               "say which of saṃsarga and sannipāta goes with two and which "
               "with three, and does not describe them further."),
    "explain_hi": ("पहली पंक्ति कफ के गुण गिनाती है: स्निग्ध, शीत, गुरु, मंद, श्लक्ष्ण, मृत्स्न, स्थिर। "
                   "‘शीत’ अनिल और कफ दोनों में आया है, पर ‘गुरु’ केवल कफ के लिए है। दूसरी पंक्ति कहती "
                   "है कि ‘संसर्ग’ और ‘सन्निपात’ उनमें से दो या तीन के क्षय या कोप से होते हैं। कौन-सा "
                   "दो से और कौन-सा तीन से, यह श्लोक नहीं बताता। ‘मृत्स्न’ का अर्थ ‘मिट्टी जैसा’ है।"),
    "hook": "कफ: स्निग्ध शीत गुरु मंद श्लक्ष्ण मृत्स्न स्थिर · दो/तीन के क्षय-कोप से संसर्ग, सन्निपात।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "According to line 2, from what do saṃsarga and sannipāta arise?",
            ("The decrease or aggravation of two or three of the doṣas",
             "तद्द्वित्रिक्षयकोपतः: from the decrease or aggravation of two or three of them."),
            [("The balance of all three doṣas together", "Balance (साम्य) is not named in this unit."),
             ("The aggravation of one doṣa alone", "The line says two or three, not one."),
             ("The food taken in the morning", "No food is named in this unit.")],
            "द्वि-त्रि-क्षय-कोपतः: from two-or-three decrease-or-aggravation.",
            "संसर्ग, सन्निपात: from the क्षय or कोप of two or three."),
        match(1, "Match each word to its meaning.",
              [["स्निग्धः", "unctuous"], ["गुरुः", "heavy"],
               ["मंदः", "slow"], ["स्थिरः", "stable"]],
              "Four of the seven qualities of Kapha.",
              "स्निग्धः = unctuous; गुरुः = heavy; मंदः = slow; स्थिरः = stable."),
        mcq("extend", 2, "Why is तत् + द्वि joined as तद्द्वि-?",
            ("A final त् becomes द् before a voiced sound",
             "द is voiced, so the final त् of तत् is voiced to द्."),
            [("A final त् becomes श् before द", "श् comes from a visarga before च or छ."),
             ("A final त् stays unchanged before any sound", "त् changes before a voiced sound."),
             ("A final त् becomes न् before द", "न् is not the change here.")],
            "तत् (of them) + द्वि (two) → तद्द्वि.",
            "Final त् → द् before a voiced sound.",
            teaches="A final त् becomes द् before a voiced sound (तत् + द्वि = तद्द्वि)."),
        mcq("discriminate", 3,
            "One word is wrong in: 'Kapha is unctuous, hot, heavy, slow, smooth, clay-like and stable.' Which?",
            ("hot", "The verse says शीत, cold."),
            [("unctuous", "स्निग्ध is unctuous."),
             ("heavy", "गुरु is heavy."),
             ("stable", "स्थिर is stable.")],
            "Kapha is cold (शीत) in the verse, not hot.",
            "Kapha: शीत = cold."),
        order(4, "Put the qualities of Kapha in the order of the verse.",
              ["स्निग्धः", "शीतः", "गुरुः", "मंदः", "श्लक्ष्णः", "मृत्स्नः", "स्थिरः"],
              "Line 1 runs: unctuous, cold, heavy, slow, smooth, clay-like, stable.",
              "स्निग्ध · शीत · गुरु · मंद · श्लक्ष्ण · मृत्स्न · स्थिर.", role="apply"),
        mcq("transfer", 5,
            "By the pattern of -कोपतः, what does the invented word दोषकोपतः mean?",
            ("From the aggravation of the doṣas",
             "-तः means from, because of; कोप is aggravation."),
            [("For the decrease of the doṣas", "Decrease would be क्षय, and -तः is not 'for'."),
             ("Of the aggravation of the doṣas", "-तः is not the 'of' ending."),
             ("In the doṣas' absence", "Nothing in the word means absence.")],
            "द्वित्रिक्षयकोपतः = from the decrease or aggravation of two or three.",
            "-तः = from, because of.",
            teaches="The ending -तः means 'from, because of' (क्षयकोपतः, दोषकोपतः)."),
    ],
}

NOTES_HI = {
    "26": "विश्वास: कम। पहली पंक्ति में ‘वचने यच्चनादृताः’ अस्पष्ट छपा है (संपादक भी संदेह करते हैं; सुझाव ‘वचने यत्र नादृताः’); ‘ते अर्थ-प्रत्यायन-पराः’ तक का भाग साफ़ है। ‘आदृत’ को कर्तृवाच्य (सावधान) लिया गया है, कर्मवाच्य (आदर नहीं पाए) भी संभव है। दूसरी पंक्ति में ‘प्राधः’ शब्द नहीं है; सुझाव ‘प्राज्ञः’ (ज्ञ का ध पढ़ा गया) है, पर यह केवल अनुमान है। कोई क्रिया नहीं है; ‘संग्रहः’ प्रथमा है। संधि जाँची: तेऽर्थ = ते + अर्थ; सर्वतंत्राण्यतः = सर्वतंत्राणि + अतः (इ + अ → य)। वाक्य अगली दो इकाइयों में चलता है; श्लोक की सीमा एक पंक्ति खिसकी लगती है।",
    "27": "विश्वास: मध्यम। कर्ता (संग्रहः, इकाई २६) इस इकाई में नहीं है। ‘आक्षेप’ का अर्थ ‘आपत्ति’ या ‘विषयांतर’ दोनों हो सकता है; ‘अस्थान-विस्तर’ = अनुचित स्थान पर विस्तार। हेतु, लिंग, औषध तीन स्कंध गिनाए गए हैं। संधि जाँची: लिंग + औषध → लिंगौषध (अ + औ → औ); अस्थान…आदि + वर्जितः → आदिवर्जितः में समास ही है। पाठभेद नहीं दिया गया।",
    "28": "विश्वास: उच्च। ‘स्वान्यतंत्रविरोधानाम्’ का अर्थ ‘अपने और दूसरे तंत्रों के बीच के विरोध’ लिया गया है; ‘अपने और दूसरे तंत्रों के भीतर के विरोध’ भी संभव है। संधि जाँची: स्व + अन्य → स्वान्य (अ + अ → आ); विनिगूढ + अर्थ → विनिगूढार्थ। वाक्य अगली इकाई (करिष्यते) तक चलता है। कोई पाठभेद नहीं।",
    "29": "विश्वास: कम। दूसरी पंक्ति (नित्योपयोगेऽदुर्बोधं सर्वांगव्यापि भास्वतः) नपुंसक है और संभवतः अगली इकाई के ‘कायचिकित्सितं’ से जुड़ती है; ‘भास्वतः’ संदिग्ध है (षष्ठी/पंचमी का अन्वय नहीं बनता, सुझाव ‘भास्वत्’ अर्थात् चमकता हुआ)। अंतिम शब्दों का अनुवाद इसी सुझाव पर टिका है, इसलिए कोई प्रश्न दूसरी पंक्ति पर नहीं बना। पहली पंक्ति: ‘करिष्यते’ भविष्यत्, आत्मनेपद, कर्म के अर्थ में (डेटा के अनुसार)। ‘सर्वांग’ शरीर के अंग या अष्टांग विज्ञान के अंग, खुला छोड़ा गया है।",
    "30": "विश्वास: उच्च। छपाई में ‘मात्रामात्र मप्यत्र’ में ‘मात्रामात्रम्’ का म् अलग टुकड़े में चला गया है। पुस्तक का दिया हिन्दी ‘आगम के विरुद्ध नहीं’ जैसा पढ़ता है, पर संस्कृत ‘आगमवर्जितम्’ (आगम से रहित) कहता है। संधि जाँची: किंचित् + आगम → किंचिदागम (त् → द्)। पिछली इकाई की दूसरी पंक्ति इससे जुड़ सकती है (इकाई २९ देखें)।",
    "31": "विश्वास: मध्यम। पंक्ति १ संक्षिप्त है: ‘क्रमोऽन्यथा’ का अर्थ ‘क्रम दूसरे प्रकार का’ (अर्थात् अन्य ग्रंथों से भिन्न) लिया गया है और क्रिया ऊपर से जोड़ी गई है। वायु = वात। संधि जाँची: तेऽर्थाः = ते + अर्थाः; कफश्चेति = कफः + च + इति (विसर्ग + च → श्च; च + इ → चे); त्रयो दोषाः = त्रयः + दोषाः (अः + घोष → ओ); क्रमोऽन्यथा = क्रमः + अन्यथा।",
    "32": "विश्वास: उच्च। ‘ते’ = पिछली इकाई के तीन दोष। साम्य के उपभेद नहीं गिनाए गए। संधि जाँची: वृद्धिक्षयावपि = वृद्धिक्षयौ + अपि (औ + स्वर → आव्); उत्कृष्ट-मध्य-अल्प-तया में ‘-तया’ भाववाचक (तृतीया)। कोई पाठभेद नहीं।",
    "33": "विश्वास: मध्यम। छपा ‘विकृताविकृता’ में विकृताः और अविकृताः बिना विसर्ग के जुड़े हैं (पाठ में हिअटस नहीं रखा)। दोनों अर्ध-पंक्तियाँ समानांतर क्रम में पढ़ी गई हैं (विकृत: नाश; अविकृत: वृद्धि)। कौन-सा दोष कहाँ रहता है, श्लोक में नहीं है; ‘हृन्नाभ्योः’ को अधः/मध्य/ऊर्ध्व के संदर्भ-बिंदु लिया गया है। संधि जाँची: व्यापिनोऽपि = व्यापिनः + अपि।",
    "34": "विश्वास: उच्च। श्लोक यह नहीं बताता कि कौन-सा दोष अंत, मध्य या आदि में है, न यह कि किससे विषम, तीक्ष्ण या मंद अग्नि होती है; केवल क्रम रखा गया है। ‘अहोरात्रि’ को अहः + रात्रि पढ़ा गया है (दिन और रात अलग), इसलिए पहले समास में चार हैं; ‘अहोरात्र’ (एक) भी संभव है, इसलिए इस पर प्रश्न नहीं बना। ‘वयः’ = जीवन की अवस्था। संधि जाँची: तैर्भवेद्विषमस्तीक्ष्णो = तैः + भवेत् + विषमः + तीक्ष्णः; भवेत् + विषमः → भवेद्विषमः; मंदश्चाग्निः = मंदः + च + अग्निः; तेऽन्तमध्यादिगाः = ते + अन्त।",
    "35": "विश्वास: मध्यम। वाक्य अधूरा है और अगली इकाई की पहली पंक्ति (‘तैश्च … प्रकृतयः’) में पूरा होता है; सच्ची श्लोक-सीमा एक पंक्ति खिसकी लगती है। ‘विषेणेव विषकृमेः’ की तुलना अधूरी है, इसलिए उस पर प्रश्न नहीं बना। छपे ‘शुक्रार्तवस्थै र्जन्मादौ’ में ‘र्’ स्थैः के विसर्ग से बना है (संधि)। संधि जाँची: मृदुर्मध्यः = मृदुः + मध्यः; स्यात्तैः = स्यात् + तैः; शुक्र + आर्तव → शुक्रार्तव। कोष्ठ का अर्थ ‘पेट/उदर की गुहा’ रखा गया है।",
    "36": "विश्वास: कम। पहली पंक्ति में छपा ‘तिस्रः प्रकृतयः’ (तीन प्रकृतियाँ) अगली पंक्ति से मेल नहीं खाता, जो सम और द्विदोषज प्रकारों को भी गिनती है; सुझाव ‘सप्त’ है (संपादक भी यही कहते हैं), पर पाठ जैसा छपा है वैसा रखा गया। इसलिए पहली पंक्ति और संख्या पर प्रश्न नहीं बने। दूसरी पंक्ति स्पष्ट है; छपा ‘निंद्या’ वस्तुतः ‘निंद्याः’ है (विसर्ग घोष व्यंजन से पहले छूट गया; पुस्तक की वर्तनी-टिप्पणी देखें)। यह पंक्ति इकाई ३५ का वाक्य पूरा करती है।",
    "37": "विश्वास: उच्च। ‘सस्नेह’ का शाब्दिक अर्थ ‘स्नेह (चिकनाई) वाला’ है; कुछ ‘थोड़ा चिकना’ पढ़ते हैं। ‘विस्र’ = कच्चे मांस या मछली जैसी गंध वाला, ‘विस्र’ का अर्थ जैसा डेटा में है वैसा रखा। छपा ‘रुक्ष’ वर्तनी-भेद है (रूक्ष)। संधि जाँची: रूक्षो लघुः = रूक्षः + लघुः; सूक्ष्मश्चलोऽनिलः = सूक्ष्मः + चलः + अनिलः।",
    "38": "विश्वास: मध्यम। ‘मृत्स्न’ का शाब्दिक अर्थ ‘मिट्टी वाला’ है; टीकाकार अलग अर्थ बता सकते हैं। ‘होते हैं’ क्रिया ऊपर से जोड़ी गई है। ‘द्वि-त्रि’ और ‘संसर्ग-सन्निपात’ का क्रम जैसा छपा है वैसा रखा है, इसलिए प्रश्न यह नहीं पूछते कि कौन-सा दो से और कौन-सा तीन से। संधि जाँची: शीतो गुरुर्मंदः = शीतः + गुरुः + मंदः; गुरुर् में विसर्ग → र् (उ के बाद, घोष से पहले); सन्निपातश्च = सन्निपातः + च; तत् + द्वि → तद्द्वि।",
}

AIDS = {
    "26": {
        "chunks": "तेऽर्थप्रत्यायनपरा | वचने यच्चनादृताः (अस्पष्ट) ‖ सर्वतंत्राण्यतः | प्राधः (अस्पष्ट) | संहृत्याष्टांगसंग्रहः।",
        "sandhi": "इ + भिन्न स्वर → य्: सर्वतंत्राणि + अतः → सर्वतंत्राण्यतः। साथ ही ‘संहृत्य’ उपसर्ग (सं) वाली धातु का ‘करके’ वाला रूप है, इसलिए अंत में -य (-त्य) है।",
        "anchors": "संहृत्य ← सं + हृ (समेटकर) · अष्टांग = आठ अंग · संग्रह = संग्रह, समूह · अतः = इसलिए।",
        "frame": "पहली पंक्ति: पूर्व ग्रंथ (अर्थ में लगे) · दूसरी पंक्ति: इसलिए सब तंत्र समेटकर → अष्टांगसंग्रह।",
    },
    "27": {
        "diagram": {"groups": [
            {"label": "रहित (वर्जितः)",
             "items": ["अस्थानविस्तर", "आक्षेप", "पुनरुक्त", "आदि"]},
            {"label": "तीन स्कंध (केवल इन पर टिका)",
             "items": ["हेतु", "लिंग", "औषध"]}]},
        "chunks": "अस्थानविस्तराक्षेप | पुनरुक्तादिवर्जितः ‖ हेतुलिंगौषध | स्कंधत्रयमात्रनिबंधनः।",
        "sandhi": "अ + औ → औ: लिंग + औषध → लिंगौषध। पुनरुक्त + आदि → पुनरुक्तादि (अ + आ → आ)।",
        "frame": "कर्ता: संग्रह (पिछली इकाई) · रहित: अस्थान-विस्तार, आक्षेप, पुनरुक्ति · आधार: केवल तीन स्कंध — हेतु, लिंग, औषध।",
    },
    "28": {
        "diagram": {"groups": [
            {"label": "प्रकाशकः",
             "items": ["विनिगूढार्थतत्त्वानां", "प्रदेशानां", "प्रकाशकः"]},
            {"label": "विनिवर्तकः",
             "items": ["स्वान्यतंत्रविरोधानां", "भूयिष्ठं", "विनिवर्तकः"]}]},
        "contrast": "प्रकाशकः (प्रकाश करने वाला, छिपे प्रसंगों का) ↔ विनिवर्तकः (दूर करने वाला, विरोधों का)।",
        "sandhi": "अ + अ → आ: स्व + अन्य → स्वान्य; विनिगूढ + अर्थ → विनिगूढार्थ।",
        "chunks": "विनिगूढार्थतत्त्वानां | प्रदेशानां प्रकाशकः ‖ स्वान्यतंत्रविरोधानां | भूयिष्ठं विनिवर्तकः।",
    },
    "29": {
        "chunks": "युगानुरूपसंदर्शो | विभागेन करिष्यते ‖ (दूसरी पंक्ति अनिश्चित)",
        "frame": "क्या: युग के अनुरूप प्रस्तुति · कैसे: विभाग से · कब: करिष्यते (भविष्यत्, कर्म के अर्थ में)।",
        "anchors": "युग = काल, युग · अनुरूप = अनुकूल · संदर्श = प्रस्तुति, दिखाना · विभाग = अलग-अलग भाग।",
    },
    "30": {
        "chunks": "संगृहीतं विशेषेण | यत्र कायचिकित्सितं ‖ न मात्रामात्रमप्यत्र | किंचिदागमवर्जितं।",
        "sandhi": "त् → द् (स्वर से पहले): किंचित् + आगम → किंचिदागम। म् + अ बिना बदले: मात्रामात्रम् + अपि।",
        "contrast": "वर्जित = रहित ↔ विरुद्ध (यह अर्थ श्लोक का नहीं है): ‘आगमवर्जितं’ का अर्थ ‘आगम से खाली’ है।",
    },
    "31": {
        "diagram": {"groups": [
            {"label": "संक्षेप में तीन दोष",
             "items": ["वायुः", "पित्तं", "कफः"]}]},
        "chunks": "तेऽर्थाः स ग्रंथबंधश्च | संक्षेपाय क्रमोऽन्यथा ‖ वायुः पित्तं कफश्चेति | त्रयो दोषाः समासतः।",
        "sandhi": "विसर्ग + च → श्च: कफः + च → कफश्च। अः + घोष → ओ: त्रयः + दोषाः → त्रयो दोषाः।",
        "letters": "वा-पि-क: वायु · पित्त · कफ (शुरू के अक्षर, मेरी याद की युक्ति, श्लोक का दावा नहीं)।",
    },
    "32": {
        "diagram": {"groups": [
            {"label": "प्रत्येक दोष",
             "items": ["वृद्धि", "क्षय", "साम्य"]},
            {"label": "वृद्धि और क्षय के दर्जे",
             "items": ["उत्कृष्ट", "मध्य", "अल्प"]}]},
        "chunks": "प्रत्येकं ते त्रिधा | वृद्धिक्षयसाम्यविभेदतः ‖ उत्कृष्टमध्याल्पतया | त्रिधा वृद्धिक्षयावपि।",
        "sandhi": "औ + स्वर → आव्: वृद्धिक्षयौ + अपि → वृद्धिक्षयावपि।",
        "frame": "हर दोष: 3 स्थितियाँ (वृद्धि, क्षय, साम्य) · वृद्धि-क्षय: हर एक 3 दर्जे (उत्कृष्ट, मध्य, अल्प)।",
    },
    "33": {
        "diagram": {"groups": [
            {"label": "दशा और फल",
             "items": ["विकृताः", "देहं घ्नन्ति", "अविकृताः", "वर्द्धयन्ति"]},
            {"label": "आश्रय",
             "items": ["व्यापिनः", "हृन्नाभ्योः", "अधः", "मध्य", "ऊर्ध्व"]}]},
        "chunks": "विकृताविकृता देहं | घ्नंति ते वर्द्धयंति च ‖ ते व्यापिनोऽपि हृन्नाभ्यो- | रधोमध्योर्ध्वसंश्रयाः।",
        "contrast": "विकृत ↔ अविकृत: बिगड़े हुए देह का नाश करते हैं ↔ न बिगड़े देह को बढ़ाते हैं।",
        "sandhi": "अः + अ → ओऽ: व्यापिनः + अपि → व्यापिनोऽपि। ‘अ-’ निषेध: अ + विकृत → अविकृत।",
    },
    "34": {
        "diagram": {"groups": [
            {"label": "तैः (उनसे) अग्नि",
             "items": ["विषमः", "तीक्ष्णः", "मंदः"]},
            {"label": "समैः (सम होने पर)",
             "items": ["समः"]}]},
        "chunks": "वयोऽहोरात्रिभुक्तानां | तेऽंतमध्यादिगाः क्रमात् ‖ तैर्भवेद्विषमस्तीक्ष्णो | मंदश्चाग्निः समैः समः।",
        "sandhi": "ऐः + घोष → ऐर्: तैः + भवेत् → तैर्भवेत्। त् → द्: भवेत् + विषमः → भवेद्विषमः।",
        "frame": "कहाँ: आयु, दिन, रात, भोजन के अंत-मध्य-आदि में, क्रम से · फल: अग्नि विषम / तीक्ष्ण / मंद; सम दोषों से सम।",
        "contrast": "असम दोष ↔ सम दोष: अग्नि विषम-तीक्ष्ण-मंद ↔ अग्नि सम।",
    },
    "35": {
        "chunks": "कोष्ठः क्रूरो मृदुर्मध्यो | मध्यः स्यात्तैः समैरपि ‖ शुक्रार्तवस्थैर्जन्मादौ | विषेणेव विषकृमेः।",
        "sandhi": "उः + घोष → उर्: मृदुः + मध्यः → मृदुर्मध्यः। अ + आ → आ: शुक्र + आर्तव → शुक्रार्तव।",
        "frame": "कोष्ठ तीन तरह का: क्रूर, मृदु, मध्य · सम दोषों से भी मध्य · (वाक्य अगली इकाई में पूरा होता है)।",
        "anchors": "कोष्ठ = पेट की गुहा · क्रूर = कठोर · मृदु = कोमल · शुक्र = वीर्य · आर्तव = रज।",
    },
    "36": {
        "chunks": "(पहली पंक्ति अनिश्चित) ‖ समधातुः समस्तासु | श्रेष्ठा निंद्या द्विदोषजाः।",
        "contrast": "समधातु: श्रेष्ठ ↔ द्विदोषज: निंद्य।",
        "anchors": "सम-धातु = जिसमें धातु सम हैं (बहुव्रीहि) · द्वि-दोष-ज = दो दोषों से उत्पन्न · समस्तासु = सबमें।",
    },
    "37": {
        "diagram": {"groups": [
            {"label": "अनिल",
             "items": ["रूक्षः", "लघुः", "शीतः", "खरः", "सूक्ष्मः", "चलः"]},
            {"label": "पित्त",
             "items": ["सस्नेह", "तीक्ष्ण", "उष्ण", "लघु", "विस्र", "सर", "द्रव"]}]},
        "chunks": "तत्र रुक्षो लघुः शीतः | खरः सूक्ष्मश्चलोऽनिलः ‖ पित्तं सस्नेहतीक्ष्णोष्णं | लघु विस्रं सरं द्रवं।",
        "contrast": "अनिल: शीत · पित्त: उष्ण; लघु दोनों में।",
        "sandhi": "अः + अ → ओऽ: चलः + अनिलः → चलोऽनिलः। विसर्ग + च → श्च: सूक्ष्मः + चलः → सूक्ष्मश्चलः।",
        "pegs": "मेरा बनाया चित्र: सूखी, हल्की, ठंडी हवा (अनिल) और तेल-सा चिकना, गर्म, तेज़, बहता पित्त। केवल याद के लिए।",
    },
    "38": {
        "diagram": {"groups": [
            {"label": "कफ",
             "items": ["स्निग्धः", "शीतः", "गुरुः", "मंदः", "श्लक्ष्णः", "मृत्स्नः", "स्थिरः"]},
            {"label": "दो या तीन के क्षय-कोप से",
             "items": ["संसर्गः", "सन्निपातः"]}]},
        "chunks": "स्निग्धः शीतो गुरुर्मंदः | श्लक्ष्णो मृत्स्नः स्थिरः कफः ‖ संसर्गः सन्निपातश्च | तद्द्वित्रिक्षयकोपतः।",
        "pegs": "मेरा बनाया चित्र: भारी, चिकनी, ठंडी गीली मिट्टी की ढेली जो अपनी जगह स्थिर पड़ी है। केवल याद के लिए, श्लोक का दावा नहीं।",
        "sandhi": "त् → द्: तत् + द्वि → तद्द्वि। उः + घोष → उर्: गुरुः + मंदः → गुरुर्मंदः।",
    },
}

IMAGE_SPECS = {
    ("27", "diagram"): {
        "file": "ch1b03-skandha-27.svg",
        "alt": "Mind map: three branches (skandha) of the work: cause (hetu), sign (linga), medicine (aushadha)",
        "type": "mermaid",
        "code": ('mindmap\n  तीन स्कंध\n    हेतु\n    लिंग\n    औषध\n'),
    },
    ("32", "diagram"): {
        "file": "ch1b03-dosha-states-32.svg",
        "alt": "Mind map: each dosha has three states, increase, decrease, equilibrium; increase and decrease each have three grades: high, middling, low",
        "type": "mermaid",
        "code": ('mindmap\n  प्रत्येक दोष\n    वृद्धि\n      उत्कृष्ट\n      मध्य\n      अल्प\n'
                 '    क्षय\n      उत्कृष्ट\n      मध्य\n      अल्प\n    साम्य\n'),
    },
    ("33", "diagram"): {
        "file": "ch1b03-vikrta-33.svg",
        "alt": "Flowchart: doshas deranged destroy the body, unaltered make it grow; though pervading, they are seated below, in the middle and above the heart and navel",
        "type": "mermaid",
        "code": ('flowchart TD\n  A["दोष"] --> B["विकृत"]\n  A --> C["अविकृत"]\n'
                 '  B --> D["देह का नाश"]\n  C --> E["देह की वृद्धि"]\n'
                 '  A --> F["व्यापी, फिर भी आश्रय<br/>हृदय-नाभि के नीचे,<br/>मध्य में, ऊपर"]\n'),
    },
    ("34", "diagram"): {
        "file": "ch1b03-agni-34.svg",
        "alt": "Two columns: through them the fire becomes irregular, sharp, slow; when they are even, it is even",
        "type": "split",
        "title": "श्लोक ३४: दोषों से अग्नि",
        "cols": [["तैः (उनसे)", ["विषमः", "तीक्ष्णः", "मंदः"]],
                 ["समैः (सम होने पर)", ["समः"]]],
    },
    ("37", "diagram"): {
        "file": "ch1b03-gunas-37.svg",
        "alt": "Two columns: Anila (6 qualities: dry, light, cold, rough, subtle, moving) and Pitta (7 qualities: oily, sharp, hot, light, rank-smelling, flowing, liquid)",
        "type": "split",
        "title": "श्लोक ३७: अनिल और पित्त के गुण",
        "cols": [["अनिल", ["रूक्षः", "लघुः", "शीतः", "खरः", "सूक्ष्मः", "चलः"]],
                 ["पित्त", ["सस्नेह", "तीक्ष्ण", "उष्ण", "लघु", "विस्र", "सर", "द्रव"]]],
    },
    ("38", "diagram"): {
        "file": "ch1b03-kapha-38.svg",
        "alt": "Two columns: Kapha's seven qualities, and saṃsarga and sannipāta from the decrease or aggravation of two or three of them",
        "type": "split",
        "title": "श्लोक ३८: कफ और संसर्ग-सन्निपात",
        "cols": [["कफ", ["स्निग्धः", "शीतः", "गुरुः", "मंदः", "श्लक्ष्णः", "मृत्स्नः", "स्थिरः"]],
                 ["दो या तीन के क्षय-कोप से", ["संसर्गः", "सन्निपातः"]]],
    },
}
