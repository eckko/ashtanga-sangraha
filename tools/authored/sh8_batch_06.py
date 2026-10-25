from helpers import mcq, match, order, fill, multi, accepts


def T(q, teaches):
    q["teaches"] = teaches
    return q


AUTHORED = {}

# ---------------------------------------------------------------- unit 63
AUTHORED["63"] = {
    "title": "तच्चोभयमप्यन्यथादृष्टं गजसिंहे",
    "question": "By unit 63, what is said of the two judgements of strength from body size, and where is that seen?",
    "rule": ("Both of these (तत् च उभयम्), the two judgements of unit 62 (strong from a large body, weak from a "
             "small or thin one), are also seen to be otherwise (अपि अन्यथादृष्टम्) in the elephant and the lion (गजसिंहे)."),
    "limits": ("Prose. The text does not say how each judgement is 'otherwise' in the elephant or the lion: no "
               "question asks which animal shows which. 'Both' = the two judgements of unit 62 (data's note), whose "
               "opening verb is a conjectural reading."),
    "explain_hi": ("और वे दोनों भी (तच्चोभयमपि) हाथी और सिंह में (गजसिंहे) अन्य प्रकार से देखे गए हैं (अन्यथादृष्टम्)। "
                   "डेटा के अनुसार ‘दोनों’ इकाई ६२ के दो अनुमान हैं: बड़े शरीर से ‘यह बलवान है’ और कृश या छोटे शरीर से ‘यह अल्पबल है’। "
                   "यानी केवल शरीर का आकार देखकर बल का अनुमान गलत भी निकल सकता है। "
                   "हाथी और सिंह में कौन-सा अनुमान किस प्रकार उलटा दिखता है, यह पाठ नहीं बताता, इसलिए उस पर कोई प्रश्न नहीं। "
                   "डेटा ‘गजसिंहे’ को द्वन्द्व समास का सप्तमी एकवचन पढ़ता है: हाथी और सिंह में।"),
    "hook": "गज और सिंह: केवल आकार से बल का अनुमान सदा ठीक नहीं।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 63, what does अन्यथा mean?",
            ("Otherwise, in another way", "अन्यथा = otherwise: अन्यथादृष्टम्, seen to be otherwise."),
            [("In the very same way", "That would be तथा or एवम्; अन्यथा is the opposite."),
             ("Only now and then", "That would be कदाचित्; अन्यथा means otherwise."),
             ("From a great distance", "That would be दूरात्; अन्यथा means otherwise.")],
            "अन्यथा = otherwise; अन्यथादृष्टम् = seen to be otherwise.",
            "अन्यथा = otherwise."),
        order(1, "Put the words of unit 63 in the printed order.",
              ["तत्", "च", "उभयम्", "अपि", "अन्यथादृष्टम्", "गजसिंहे"],
              "That; and; both; also; seen to be otherwise; in the elephant and the lion.",
              "तत् → च → उभयम् → अपि → अन्यथादृष्टम् → गजसिंहे."),
        match(2, "Match each word of unit 63 to its meaning.",
              [["उभय", "both"], ["अन्यथा", "otherwise"], ["दृष्ट", "seen"], ["गज", "elephant"],
               ["सिंह", "lion"]],
              "उभय = both, अन्यथा = otherwise, दृष्ट = seen, गज = elephant, सिंह = lion.",
              "उभय, अन्यथा, दृष्ट, गज, सिंह.", role="extend",
              teaches="गजसिंहे is read (data) as the locative singular of the dvandva गज-सिंह: 'in the elephant and the lion'."),
        mcq("discriminate", 3, "Which split of तच्चोभयमप्यन्यथा in unit 63 is right?",
            ("तत् + च + उभयम् + अपि + अन्यथा", "त् before च → च्; अ + उ → ओ; इ before a different vowel → य्."),
            [("तच् + च + उभयम् + अपि + अन्यथा", "तच् is not a word; the च् comes from तत् before च."),
             ("तत् + चो + भयम् + अपि + अन्यथा", "चो is not a word; the ओ comes from च + उभयम्."),
             ("तत् + च + उभयम् + अप्य + न्यथा", "अप्य and न्यथा are not words; अपि + अन्यथा gives अप्यन्यथा.")],
            "तत् (that) + च (and) + उभयम् (both) + अपि (also) + अन्यथा (otherwise).",
            "त् + च → च्च; अ + उ → ओ; इ + अ → य."),
        mcq("apply", 4, "A physician judges a big man strong by his size alone. By unit 63, what is true of such a judgement?",
            ("It is seen to go wrong at times", "तच्चोभयमप्यन्यथादृष्टम्: both judgements are also seen to be otherwise."),
            [("It holds for every living being", "Unit 63 says both judgements are seen to be otherwise."),
             ("It is right only in old persons", "Unit 63 names no age; it says the judgements can fail."),
             ("It is right only in the cold season", "Unit 63 names no season; it says the judgements can fail.")],
            "Body size alone can mislead: the elephant and the lion show it.",
            "उभयम् अपि अन्यथादृष्टम् = both are also seen to be otherwise."),
        mcq("transfer", 5, "By the pattern of अपि + अन्यथा → अप्यन्यथा, how is दधि + अत्र (curd here) joined in a new example?",
            ("दध्यत्र", "इ before a different vowel → य्: दधि + अत्र → दध्यत्र."),
            [("दधीत्र", "ई comes from इ + इ; here the second vowel is अ."),
             ("दधेत्र", "ए comes from अ + इ; here इ stands first."),
             ("दधयत्र", "अय् comes from ए before a vowel; here the vowel is इ.")],
            "दधि + अत्र = दध्यत्र, like अपि + अन्यथा = अप्यन्यथा.",
            "इ + unlike vowel → य्.",
            teaches="इ, उ, ऋ before a different vowel become य्, व्, र्: अपि + अन्यथा → अप्यन्यथा."),
    ],
}

# ---------------------------------------------------------------- unit 64
AUTHORED["64"] = {
    "title": "तत्र सर्वैः सारैरुपैतो भवत्यतिबलः",
    "question": "By unit 64, what marks one who is endowed with all the sāras (essences)?",
    "rule": ("One endowed with all the sāras (सर्वैः सारैः उपैतः) is exceedingly strong, able to bear hardship, steady in "
             "body, of well-composed gait, with a resonant, deep voice, honoured, usually with offspring of equal "
             "qualities, and long-lived (दीर्घायुः)."),
    "limits": ("Prose list; the sāras are not listed here (unit 60 names eight). गौरव = heaviness or gravity of "
               "bearing: no question on which. 'manda' with both old age and illness, and where prāyaḥ belongs, are "
               "readings: no question on them, nor on the printed form उपैतो."),
    "explain_hi": ("जो सब सारों से युक्त हो (सर्वैः सारैः उपैतः), वह अत्यन्त बलवान (अतिबलः) होता है; यह इकाई उसके लक्षणों की लम्बी सूची है। "
                   "वह परम गौरव से युक्त (भारीपन या गरिमा), क्लेश सहने में समर्थ, सब कामों के आरम्भ में अपने पर आशा रखने वाला, कल्याण में लगा हुआ, "
                   "स्थिर शरीर और सुसंयत चाल वाला होता है। "
                   "उसका स्वर अनुनाद-सहित, स्निग्ध, गम्भीर और महान होता है; उसे सुख, ऐश्वर्य और धन का उपभोग और सम्मान मिलता है। "
                   "डेटा के पाठ में बुढ़ापा और रोग मन्द होते हैं, प्रायः समान गुणों वाली विस्तृत सन्तान होती है, और वह दीर्घायु होता है। "
                   "सार कौन-से हैं, यह यहाँ नहीं गिनाया; इकाई ६० आठ सार बताती है।"),
    "hook": "सब सार: अतिबल से दीर्घायु तक, लक्षणों की लम्बी माला।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In unit 64, what does अतिबल mean?",
            ("Exceedingly strong", "अति (exceedingly) + बल (strength): अतिबलः."),
            [("Without strength", "That would be अबल or निर्बल; अति means exceedingly."),
             ("Of middle strength", "That would need मध्य; अति means exceedingly."),
             ("Strong only in youth", "अति names a degree, not an age.")],
            "अति = exceedingly, बल = strength.",
            "अतिबल = exceedingly strong."),
        order(1, "Put these marks of unit 64 in the printed order.",
              ["अतिबलः", "क्लेशक्षमः", "स्थिरशरीरः", "सुसमाहितगतिः", "सन्मानभाक्", "दीर्घायुः"],
              "Exceedingly strong; able to bear hardship; steady in body; of well-composed gait; receiving honour; long-lived.",
              "अतिबलः → क्लेशक्षमः → स्थिरशरीरः → सुसमाहितगतिः → सन्मानभाक् → दीर्घायुः."),
        match(2, "Match each mark of unit 64 to its meaning.",
              [["क्लेशक्षम", "able to bear hardship"], ["प्रत्याशावान्", "having hope in himself"],
               ["कल्याणाभिनिवेशी", "devoted to the good"], ["सुसमाहितगति", "of well-composed gait"],
               ["दीर्घायु", "long-lived"]],
              "क्लेश-क्षम = able to bear hardship, प्रत्याशा-वान् = having hope, कल्याण-अभिनिवेशी = devoted to the good, "
              "सु-समाहित-गति = of well-composed gait, दीर्घ-आयु = long-lived.",
              "क्लेशक्षम, प्रत्याशावान्, कल्याणाभिनिवेशी, सुसमाहितगति, दीर्घायु.", role="extend",
              teaches="-वान् (from -वत्) after a noun means 'having it': प्रत्याशा-वान् = having hope."),
        multi("discriminate", 3, "Which of these does unit 64 name among the marks of one with all the sāras?",
              [("Unable to bear hardship", "Not named: क्लेशक्षमः says he can bear hardship."),
               ("A resonant, smooth, deep, great voice", "Named: सानुनादस्निग्धगम्भीरमहास्वरः."),
               ("A short span of life", "Not named: दीर्घायुः says he is long-lived."),
               ("Receiving honour", "Named: सन्मानभाक्, receiving honour."),
               ("Enjoying comfort, lordship and wealth", "Named: सुखैश्वर्यवित्तोपभोगः.")],
              [1, 3, 4],
              "Voice, honour and enjoyment are in the list; inability to bear hardship and a short life are their opposites.",
              "क्लेशक्षमः ... महास्वरः सुखैश्वर्यवित्तोपभोगः सन्मानभाक् ... दीर्घायुश्च."),
        mcq("apply", 4, "Which gloss of a word of unit 64 has a wrong meaning?",
            ("दीर्घायुः = short-lived", "दीर्घ means long: दीर्घायुः = long-lived, so this gloss is wrong."),
            [("स्थिरशरीरः = steady in body", "This gloss is right: स्थिर (steady) + शरीर (body)."),
             ("क्लेशक्षमः = bears hardship", "This gloss is right: क्लेश (hardship) + क्षम (able to bear)."),
             ("कल्याणाभिनिवेशी = set on good", "This gloss is right: devoted to the good (कल्याण).")],
            "दीर्घ = long; दीर्घायुः = long-lived.",
            "दीर्घायुः = long-lived."),
        mcq("transfer", 5, "By the pattern of प्रत्याशावान् (having hope), what does धनवान् mean in a new example?",
            ("Having wealth", "-वान् = having: धन-वान् = having wealth."),
            [("Lacking wealth", "Lacking wealth would be निर्धन; -वान् means having."),
             ("Giving wealth", "Giving wealth would be धनद; -वान् means having."),
             ("Seeking wealth", "Seeking wealth would be धनार्थी; -वान् means having.")],
            "धनवान् = having wealth, like प्रत्याशावान् = having hope.",
            "-वत् (nom. -वान्) = possessing.",
            teaches="The suffix -वत् (masc. nom. sg. -वान्) after a noun means 'possessing it': प्रत्याशावान्, धनवान्."),
    ],
}

# ---------------------------------------------------------------- unit 65
AUTHORED["65"] = {
    "title": "तद्विपरीतस्त्वसारः मध्यो मध्यगुणः",
    "question": "By unit 65, who is असार, and what are the qualities of the middle one?",
    "rule": ("The opposite of that (तद्विपरीतः), the one with all the sāras of unit 64, is असार (without sāra); the "
             "middle one (मध्यः) has middling qualities (मध्यगुणः)."),
    "limits": ("Prose, no verb printed. 'That' = the one endowed with all the sāras of unit 64 (data's reading). "
               "Whether asāra means lacking every sāra is not stated: no question on it. No list of the middle one's "
               "qualities is given."),
    "explain_hi": ("उसका विपरीत (तद्विपरीतः) तो असार है, यानी सार से रहित; मध्य वाला (मध्यः) मध्यम गुणों वाला (मध्यगुणः) है। "
                   "डेटा ‘तत्’ को इकाई ६४ का सब सारों वाला व्यक्ति मानता है। "
                   "असार का अर्थ हर एक सार का पूरा अभाव है या नहीं, यह पाठ नहीं बताता। "
                   "‘तद्विपरीतस्त्वसारः’ में तत् + विपरीतः (व से पहले त् → द्), विपरीतः + तु (त से पहले विसर्ग → स्) और तु + असारः (उ + अ → व) की सन्धियाँ हैं। "
                   "कोई क्रिया छपी नहीं; ‘है’ समझा जाता है।"),
    "hook": "सब सार, उलटा असार, बीच वाला मध्य।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 65, what does असार mean?",
            ("Without sāra (essence)", "अ (without) + सार (essence): असारः."),
            [("Full of every sāra", "That is the one of unit 64; अ- negates."),
             ("Rich in one sāra alone", "अ- negates; it does not single out one sāra."),
             ("Of middling sāra (essence)", "The middle one is मध्यः; असार is without sāra.")],
            "अ- = without; असार = without sāra.",
            "असार = without essence."),
        order(1, "Put the words of unit 65 in the printed order.",
              ["तद्विपरीतः", "तु", "असारः", "मध्यः", "मध्यगुणः"],
              "The opposite of that; but; without sāra; the middle one; of middling qualities.",
              "तद्विपरीतः → तु → असारः → मध्यः → मध्यगुणः."),
        match(2, "Match each word of unit 65 to its meaning.",
              [["तद्विपरीत", "opposite of that"], ["तु", "but, however"], ["असार", "without sāra"],
               ["मध्य", "the middle one"], ["मध्यगुण", "of middling qualities"]],
              "तत्-विपरीत = opposite of that, तु = but, असार = without sāra, मध्य = middle, मध्य-गुण = of middling qualities.",
              "तद्विपरीत, तु, असार, मध्य, मध्यगुण.", role="extend",
              teaches="मध्यगुणः is a bahuvrīhi: one whose qualities are middling."),
        mcq("discriminate", 3, "Which split of तद्विपरीतस्त्वसारः in unit 65 is right?",
            ("तत् + विपरीतः + तु + असारः", "त् before व → द्; ः before त → स्; उ + अ → व."),
            [("तत् + विपरीतः + तु + सारः", "तु + सारः would print तु सारः; the व comes from उ + अ of असारः."),
             ("तद्वि + परीतः + तु + असारः", "तद्वि is not a word; तत् + विपरीतः gives तद्विपरीतः."),
             ("तत् + विपरीतः + अस्तु + असारः", "विपरीतः + अस्तु would print विपरीतोऽस्तु; the स्त is from ः + तु.")],
            "तत् (that) + विपरीतः (opposite) + तु (but) + असारः (without sāra).",
            "त् + व → द्व; ः + त → स्त; उ + अ → व."),
        mcq("apply", 4, "Why is मध्यः printed मध्यो before मध्यगुणः in unit 65?",
            ("अः before a voiced consonant → ओ", "म is a voiced consonant: मध्यः + मध्यगुणः → मध्यो मध्यगुणः."),
            [("आः before a voiced consonant → ओ", "आः drops its visarga before a voiced sound; it does not give ओ."),
             ("Every visarga before म → ओ", "Not every: after इ or उ a visarga before म gives र्."),
             ("ओ is the noun's own ending", "मध्यः is the nominative singular; ओ comes only from sandhi.")],
            "मध्यः + मध्यगुणः: अः before the voiced consonant म → ओ.",
            "अः + voiced consonant → ओ."),
        mcq("transfer", 5, "By the pattern of मध्यः + मध्यगुणः → मध्यो मध्यगुणः, how is नरः + गच्छति (the man goes) joined in a new example?",
            ("नरो गच्छति", "अः before the voiced consonant ग → ओ: नरो गच्छति."),
            [("नर गच्छति", "अः loses its visarga only before vowels other than अ; ग is a consonant."),
             ("नरर्गच्छति", "र् comes from a visarga after a vowel other than अ/आ before a voiced sound; here the vowel is अ."),
             ("नरस्गच्छति", "स् comes from a visarga before the voiceless त or थ, not before ग.")],
            "नरः + गच्छति = नरो गच्छति, like मध्यः + मध्यगुणः = मध्यो मध्यगुणः.",
            "अः + voiced consonant → ओ.",
            teaches="A final अः before a voiced consonant becomes ओ: मध्यः + मध्यगुणः → मध्यो मध्यगुणः."),
    ],
}

# ---------------------------------------------------------------- unit 66
AUTHORED["66"] = {
    "title": "प्रमाणं पुनः स्वांगुलैः",
    "question": "By unit 66, by what unit is the body's measure given?",
    "rule": ("The measure (प्रमाणम्), moreover (पुनः), is by one's own aṅgulas (स्वाङ्गुलैः), finger-breadths. This "
             "line introduces the measurements that follow."),
    "limits": ("Prose, no verb printed. स्व = one's own; how one aṅgula is fixed is not stated. The measures "
               "themselves begin in unit 67."),
    "explain_hi": ("प्रमाण (माप) फिर अपने अंगुलों से (स्वाङ्गुलैः) है; अंगुल = एक अंगुली की चौड़ाई। "
                   "यह पंक्ति आगे आने वाले अंग-मापों की भूमिका है; माप इकाई ६७ से शुरू होते हैं। "
                   "‘स्व’ = अपना; एक अंगुल किस प्रकार ठीक किया जाए, यह यहाँ नहीं बताया। "
                   "‘स्वाङ्गुलैः’ में स्व + अङ्गुलैः (अ + अ → आ) है, और ‘-ऐः’ तृतीया बहुवचन है: अंगुलों से।"),
    "hook": "अपने ही अंगुल से अपना माप।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 66, what is the body measured in?",
            ("One's own finger-breadths", "स्वाङ्गुलैः: by one's own aṅgulas, finger-breadths."),
            [("A royal rod of fixed length", "No rod is named; स्व-अङ्गुल = one's own finger-breadth."),
             ("Grains laid in a row", "No grains are named; the unit is the aṅgula."),
             ("Lengths of a fixed rope", "No rope is named; the unit is the aṅgula.")],
            "स्व (one's own) + अङ्गुल (finger-breadth).",
            "प्रमाणं स्वाङ्गुलैः."),
        match(1, "Match each word of unit 66 to its meaning.",
              [["प्रमाण", "measure"], ["पुनः", "moreover"], ["स्व", "one's own"], ["अङ्गुल", "finger-breadth"]],
              "प्रमाण = measure, पुनः = moreover, स्व = one's own, अङ्गुल = finger-breadth.",
              "प्रमाण, पुनः, स्व, अङ्गुल."),
        fill(2, "Unit 66: प्रमाणं ____ स्वांगुलैः (moreover). Type it in Devanagari or in English letters (e.g. dharma).",
             accepts("पुनः", None, "punah", "puna"),
             "पुनः (moreover): प्रमाणं पुनः स्वांगुलैः.",
             "पुनः here marks a new topic, 'moreover': after strength, the measures of the body.",
             "प्रमाणं पुनः स्वाङ्गुलैः."),
        mcq("discriminate", 3, "Which split of स्वांगुलैः in unit 66 is right?",
            ("स्व + अङ्गुलैः", "अ + अ → आ: स्व + अङ्गुलैः → स्वाङ्गुलैः."),
            [("सु + अङ्गुलैः", "सु + अ gives स्व with a short अ (स्वङ्गुलैः); the print has आ."),
             ("स्वाङ्ग + उलैः", "उलैः is not a word; the word is अङ्गुल."),
             ("स्वः + अङ्गुलैः", "स्वः (heaven) would join as स्वरङ्गुलैः; the word here is स्व, own.")],
            "स्व (one's own) + अङ्गुलैः (by finger-breadths): अ + अ → आ.",
            "अ + अ → आ."),
        mcq("apply", 4, "In unit 66, what case is स्वाङ्गुलैः, and what does it say?",
            ("Instrumental plural: by aṅgulas", "-ऐः is the instrumental plural of an अ-stem: by (one's own) aṅgulas."),
            [("Locative plural: in aṅgulas", "The locative plural would be स्वाङ्गुलेषु."),
             ("Genitive plural: of aṅgulas", "The genitive plural would be स्वाङ्गुलानाम्."),
             ("Accusative plural: aṅgulas", "The accusative plural would be स्वाङ्गुलान्.")],
            "स्वाङ्गुलैः = by one's own aṅgulas (instrumental of means).",
            "-ऐः = instrumental plural."),
        mcq("transfer", 5, "By the pattern of स्व + अङ्गुल → स्वाङ्गुल, how is स्व + अर्थ (one's own aim) joined in a new example?",
            ("स्वार्थ", "अ + अ → आ: स्व + अर्थ → स्वार्थ."),
            [("स्वर्थ", "The two अ merge into a long आ, not a short अ."),
             ("स्वोर्थ", "ओ comes from अ + उ; here the second vowel is अ."),
             ("स्वैर्थ", "ऐ comes from अ + ए or ऐ; here the second vowel is अ.")],
            "स्व + अर्थ = स्वार्थ, like स्व + अङ्गुल = स्वाङ्गुल.",
            "अ + अ → आ.",
            teaches="Two अ (short or long) merge into a long आ: स्व + अङ्गुलैः → स्वाङ्गुलैः."),
    ],
}

# ---------------------------------------------------------------- unit 67
AUTHORED["67"] = {
    "title": "पादांगुष्ठप्रदेशिन्यौ द्व्यंगुलायते",
    "question": "By unit 67, how long are the big toe and the second toe, and how are the other three toes measured?",
    "rule": ("The big toe and the second toe (प्रदेशिनी) of the foot are two aṅgulas long; the other three, in order, "
             "each successive one, are less by a fifth part, or less by their nail (तन्नखहीनाः वा)."),
    "limits": ("Prose. 'A fifth part' of what, and whose nail ('तत्' = the preceding toe's or each toe's own), are "
               "not stated: no question on either. How a nail's length is fixed is not said. The other three toes are "
               "not named. प्रदेशिनी of the foot = second toe (standard)."),
    "explain_hi": ("पैर का अँगूठा (अङ्गुष्ठ) और प्रदेशिनी, यानी अँगूठे के बाद की अंगुली, दोनों दो अंगुल लम्बे हैं (द्व्यङ्गुलायते)। "
                   "बाकी तीन (तिस्रः अन्याः) क्रम से, एक के बाद एक (उत्तरोत्तरम्), पाँचवें भाग से कम हैं, या उनके नख भर से कम (तन्नखहीनाः वा)। "
                   "पाँचवाँ भाग किसका, और ‘तत्’ पिछली अंगुली का नख है या हर अंगुली का अपना, यह पाठ खुला छोड़ता है। "
                   "‘द्व्यङ्गुलायते’ स्त्रीलिंग द्विवचन है और दोनों अंगुलियों (प्रदेशिन्यौ) से मेल खाता है।"),
    "hook": "अँगूठा, प्रदेशिनी: दो-दो अंगुल; आगे की तीन घटती जाएँ।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 67, which toe is the प्रदेशिनी of the foot?",
            ("The second toe", "प्रदेशिनी (the pointing one) applied to the foot = the second toe (standard)."),
            [("The little toe", "The little toe is among the other three, which are not named."),
             ("The big toe", "The big toe is the अङ्गुष्ठ, named beside it."),
             ("The heel's end", "The heel is not a toe; प्रदेशिनी names a toe.")],
            "पाद-अङ्गुष्ठ-प्रदेशिन्यौ = the big toe and the second toe of the foot.",
            "प्रदेशिनी (foot) = second toe."),
        order(1, "Put the phrases of unit 67 in the printed order.",
              ["पादाङ्गुष्ठप्रदेशिन्यौ", "द्व्यङ्गुलायते", "तिस्रः अन्याः", "क्रमेण उत्तरोत्तरम्"],
              "The big toe and second toe; two aṅgulas long; the other three; in order, each successive.",
              "Which toes → length → the other three → in order."),
        match(2, "Match each word of unit 67 to its meaning.",
              [["अङ्गुष्ठ", "big toe"], ["प्रदेशिनी", "second toe"], ["आयत", "long"], ["तिस्रः", "three"],
               ["उत्तरोत्तरम्", "each successive one"]],
              "अङ्गुष्ठ = big toe, प्रदेशिनी = second toe, आयत = long, तिस्रः = three, उत्तरोत्तरम् = each successive one.",
              "अङ्गुष्ठ, प्रदेशिनी, आयत, तिस्रः, उत्तरोत्तरम्.", role="extend",
              teaches="द्व्यङ्गुलायते is feminine dual: it agrees with the two toes, प्रदेशिन्यौ."),
        mcq("discriminate", 3, "By unit 67, how long are the big toe and the second toe of the foot?",
            ("Two aṅgulas long", "द्व्यङ्गुलायते: two aṅgulas long."),
            [("Four aṅgulas long", "Four aṅgulas is the length of the prapada, sole and heel (unit 68)."),
             ("Fourteen aṅgulas long", "Fourteen is the length of the whole foot (unit 68)."),
             ("One aṅgula long", "द्वि = two: द्व्यङ्गुल, two aṅgulas.")],
            "द्वि (two) + अङ्गुल + आयत (long).",
            "द्व्यङ्गुलायते = two aṅgulas long."),
        mcq("apply", 4, "In unit 67, what does तिस्रः अन्याः (the other three) refer to?",
            ("The other toes, unnamed", "तिस्रः अन्याः: the three toes after the big toe and the second toe; the text does not name them."),
            [("The prapada, sole and heel", "Those three parts come in unit 68, not here."),
             ("Three fingers of the hand", "The line speaks of the foot: पादाङ्गुष्ठप्रदेशिन्यौ."),
             ("The ankles and the shank", "Those are named in unit 69, not here.")],
            "तिस्रः (three, f.) अन्याः (other, f.): the remaining three toes, not named.",
            "तिस्रः अन्याः = the other three (toes)."),
        mcq("transfer", 5, "By the pattern of तिस्रः + अन्याः → तिस्रोऽन्याः, how is रामः + अत्र (Rāma here) joined in a new example?",
            ("रामोऽत्र", "अः + अ → ओ, and the अ is marked by ऽ: रामोऽत्र."),
            [("रामात्र", "अ + अ → आ holds for two vowels; here a visarga stands between."),
             ("राम अत्र", "अः loses its visarga with a gap before vowels other than अ; here the vowel is अ."),
             ("रामरत्र", "र् comes from a visarga after a vowel other than अ/आ; here the vowel is अ.")],
            "रामः + अत्र = रामोऽत्र, like तिस्रः + अन्याः = तिस्रोऽन्याः.",
            "अः + अ → ओऽ.",
            teaches="A final अः before a short अ becomes ओ, and the अ is dropped, marked by ऽ: तिस्रः + अन्याः → तिस्रोऽन्याः."),
    ],
}

# ---------------------------------------------------------------- unit 68
AUTHORED["68"] = {
    "title": "चतुरंगुलायताः पृथक्प्रपदपादतलपाष्ण्यः",
    "question": "By unit 68, how long are the prapada, sole and heel, and what are the foot's length and girth?",
    "rule": ("The prapada (front of the foot), the sole (पादतल) and the heel (पाष्णि) are separately four aṅgulas long "
             "and six, five and four aṅgulas broad; the foot is exactly fourteen in length and fourteen in girth."),
    "limits": ("Prose. Which part has which breadth (six, five, four) follows the order only by the natural reading: "
               "no question pairs a breadth with a part. No sum of the parts is given. No question rests on the "
               "unusual printed form पाष्ण्यः. "),
    "explain_hi": ("प्रपद (पैर का अगला भाग), पादतल (तलवा) और पाष्णि (एड़ी) अलग-अलग (पृथक्) चार अंगुल लम्बे हैं। "
                   "वे छः, पाँच और चार अंगुल चौड़े हैं; कौन-सा भाग कितना चौड़ा, यह जोड़ी केवल क्रम से स्वाभाविक पाठ है, छपी नहीं। "
                   "पूरा पैर (पादः) लम्बाई में चौदह ही (चतुर्दश एव) और घेरे (परिणाह) में भी चौदह ही है; अंक के बाद ‘अंगुल’ समझा जाता है।"),
    "hook": "आगे, बीच, एड़ी: चार-चार लम्बे; पूरा पैर चौदह लम्बा, चौदह घेरा।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In unit 68, what is the प्रपद?",
            ("The front of the foot", "प्रपद = forepart of the foot (standard)."),
            [("The sole of the foot", "The sole is the पादतल, named beside it."),
             ("The ankle above the foot", "The ankle is the गुल्फ (unit 69)."),
             ("The cap of the knee", "The knee is the जानु (unit 72); no kneecap is named.")],
            "प्रपद = front of the foot, पादतल = sole.",
            "प्रपद = front of the foot."),
        order(1, "Put the phrases of unit 68 in the printed order.",
              ["चतुरङ्गुलायताः", "पृथक्", "प्रपदपादतलपाष्ण्यः", "षट्पञ्चचतुरङ्गुलविस्तृताः", "चतुर्दश एव आयामेन",
               "पादः चतुर्दश एव परिणाहेन"],
              "Four aṅgulas long; separately; the prapada, sole and heel; six, five, four broad; fourteen in length; the foot fourteen in girth.",
              "Length → separately → the parts → breadths → foot's length → foot's girth."),
        match(2, "Match each word of unit 68 to its meaning.",
              [["प्रपद", "front of the foot"], ["पादतल", "sole"], ["पृथक्", "separately"], ["आयाम", "length"],
               ["परिणाह", "girth"]],
              "प्रपद = front of the foot, पादतल = sole, पृथक् = separately, आयाम = length, परिणाह = girth.",
              "प्रपद, पादतल, पृथक्, आयाम, परिणाह.", role="extend",
              teaches="आयाम (length), विस्तृत / विस्तार (breadth) and परिणाह (girth) name the three measures used in these units."),
        mcq("discriminate", 3, "By unit 68, what are the length and the girth of the whole foot?",
            ("Fourteen and fourteen", "चतुर्दशैवायामेन पादश्चतुर्दशैव परिणाहेन: fourteen in length, fourteen in girth."),
            [("Four and fourteen", "Four aṅgulas is the foot's height (unit 70), not its length."),
             ("Fourteen and thirty", "Thirty is the girth of the thigh (unit 73)."),
             ("Eighteen and eighteen", "Eighteen is the length of the shank and thigh (unit 71).")],
            "पादः: fourteen in length and fourteen in girth.",
            "चतुर्दश एव आयामेन, चतुर्दश एव परिणाहेन."),
        mcq("apply", 4, "By unit 68, how long is each of the prapada, the sole and the heel?",
            ("Four aṅgulas, separately", "चतुरङ्गुलायताः पृथक्: four aṅgulas long, each separately."),
            [("Six, five and four", "Six, five and four are their breadths (विस्तृताः), not lengths."),
             ("Two aṅgulas, each", "Two aṅgulas is the length of the two first toes (unit 67)."),
             ("Fourteen aṅgulas, each", "Fourteen is the length of the whole foot.")],
            "पृथक् = separately: each is four aṅgulas long.",
            "चतुरङ्गुलायताः पृथक्."),
        mcq("transfer", 5, "By the pattern of चतुर्दश + एव → चतुर्दशैव, how is अत्र + एव (here itself) joined in a new example?",
            ("अत्रैव", "अ + ए → ऐ: अत्र + एव → अत्रैव."),
            [("अत्रेव", "ए comes from अ + इ or ई; here the second vowel is ए."),
             ("अत्रोव", "ओ comes from अ + उ or ऊ; here the second vowel is ए."),
             ("अत्रयेव", "अय् comes from ए before a vowel; here ए follows अ.")],
            "अत्र + एव = अत्रैव, like चतुर्दश + एव = चतुर्दशैव.",
            "अ + ए → ऐ.",
            teaches="अ before ए or ऐ gives ऐ: चतुर्दश + एव → चतुर्दशैव."),
    ],
}

# ---------------------------------------------------------------- unit 69
AUTHORED["69"] = {
    "title": "तथा गुल्फौ जंघामध्यंच",
    "question": "By unit 69, which parts are named after तथा (likewise)?",
    "rule": ("Likewise (तथा) the two ankles (गुल्फौ) and the middle of the shank (जङ्घामध्यम्). No measure and no verb "
             "are printed; both are carried from the context."),
    "limits": ("Elliptical prose. Which measure applies is not stated: तथा may carry one from unit 68, or a "
               "measure dropped out in print; no question on it. जङ्घा = the lower leg between knee and ankle "
               "(standard), not the thigh."),
    "explain_hi": ("वैसे ही (तथा) दोनों गुल्फ यानी टखने (गुल्फौ) और जंघा का मध्य (जङ्घामध्यम्)। "
                   "यहाँ जंघा = घुटने से टखने तक की टाँग; हिन्दी की ‘जाँघ’ नहीं, जाँघ के लिए पाठ ‘ऊरु’ कहता है। "
                   "इस पंक्ति में न कोई माप छपा है न क्रिया; ‘तथा’ शायद इकाई ६८ से कोई माप लाता है, या छपाई में माप छूट गया हो, यह तय नहीं। "
                   "‘गुल्फौ’ द्विवचन है: दोनों टखने।"),
    "hook": "तथा: दोनों टखने और जंघा का मध्य।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 69, what is the गुल्फ?",
            ("The ankle", "गुल्फ = ankle (standard)."),
            [("The knee", "The knee is the जानु (unit 72)."),
             ("The heel", "The heel is not the part named here."),
             ("The thigh", "The thigh is the ऊरु (unit 71).")],
            "गुल्फौ = the two ankles.",
            "गुल्फ = ankle."),
        match(1, "Match each word of unit 69 to its meaning.",
              [["तथा", "likewise"], ["गुल्फ", "ankle"], ["जङ्घा", "shank, lower leg"], ["मध्य", "middle"],
               ["च", "and"]],
              "तथा = likewise, गुल्फ = ankle, जङ्घा = shank, मध्य = middle, च = and.",
              "तथा, गुल्फ, जङ्घा, मध्य, च."),
        T(multi("extend", 2, "Which statements fit unit 69?",
                [("जङ्घा here means the thigh", "Does not fit: जङ्घा is the lower leg; the thigh is ऊरु."),
                 ("तथा here means 'likewise'", "Fits: तथा = likewise."),
                 ("It names the knee and the thigh", "Does not fit: the knee (जानु) and the thigh (ऊरु) come in units 72 and 71."),
                 ("It names the ankles and the middle of the shank", "Fits: गुल्फौ जङ्घामध्यं च.")],
                [1, 3],
                "तथा = likewise; the two ankles and the middle of the shank are named; the thigh is ऊरु, not जङ्घा.",
                "तथा गुल्फौ जङ्घामध्यं च."),
          "तथा (likewise) links the line to its neighbours; जङ्घा is the shank (lower leg), not the thigh (ऊरु)."),
        mcq("discriminate", 3, "In unit 69, what does the ending of गुल्फौ show?",
            ("Dual: the two ankles", "गुल्फौ is masc. nom. dual: the two ankles."),
            [("Plural: many ankles", "The plural would be गुल्फाः."),
             ("Singular: one ankle", "The singular would be गुल्फः."),
             ("Instrumental: by the ankle", "The instrumental would be गुल्फेन.")],
            "गुल्फौ = the two ankles (dual).",
            "-औ here = nom. dual of an अ-stem."),
        mcq("apply", 4, "Why is जङ्घामध्यम् printed जंघामध्यं before च in unit 69?",
            ("A final म् before a consonant is ं", "म् before the consonant च is written as anusvāra: जंघामध्यं च."),
            [("A final म् before च is dropped", "It is not dropped; it is written as ं."),
             ("ं marks the plural number here", "जङ्घामध्यम् is neut. nom. singular; ं is only sandhi."),
             ("ं is the ending of a dual noun", "The neuter dual would be जङ्घामध्ये.")],
            "जङ्घामध्यम् + च → जंघामध्यं च: final म् before a consonant → ं.",
            "म् + consonant → ं."),
        mcq("transfer", 5, "By the pattern of जङ्घामध्यम् + च → जंघामध्यं च, how is फलम् + च (and the fruit) written in a new example?",
            ("फलं च", "Final म् before the consonant च → ं: फलं च."),
            [("फल च", "The म् is not dropped; it is written as ं."),
             ("फलश्च", "श् comes from a visarga before च, not from म्."),
             ("फलो च", "ओ comes from अः before a voiced consonant; here there is म्, and च is voiceless.")],
            "फलम् + च = फलं च, like जङ्घामध्यम् + च = जंघामध्यं च.",
            "म् + consonant → ं.",
            teaches="A final म् before a consonant inside a sentence is written as anusvāra ं: जङ्घामध्यं च, फलं च."),
    ],
}

# ---------------------------------------------------------------- unit 70
AUTHORED["70"] = {
    "title": "चतुरंगुलोत्सेधः पादः",
    "question": "By unit 70, how high is the foot?",
    "rule": "The foot (पादः) is four aṅgulas in height (चतुरङ्गुलोत्सेधः).",
    "limits": ("Prose, no verb printed; 'is' is understood. The line gives only the height; the foot's length and "
               "girth are in unit 68."),
    "explain_hi": ("पैर (पादः) ऊँचाई (उत्सेध) में चार अंगुल का है। "
                   "‘चतुरङ्गुलोत्सेधः’ बहुव्रीहि है: जिसकी ऊँचाई चार अंगुल हो; यह ‘पादः’ का विशेषण है। "
                   "इसमें चतुर् + अङ्गुल और अङ्गुल + उत्सेधः (अ + उ → ओ) जुड़े हैं। "
                   "पैर की लम्बाई और घेरा, दोनों चौदह, इकाई ६८ में हैं।"),
    "hook": "पैर की ऊँचाई: बस चार अंगुल।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 70, what does उत्सेध mean?",
            ("Height", "उत्सेध = height."),
            [("Girth", "Girth is परिणाह (unit 68)."),
             ("Breadth", "Breadth is विस्तार (unit 74)."),
             ("Weight", "No weight is named; उत्सेध = height.")],
            "उत्सेध = height.",
            "उत्सेध = height."),
        match(1, "Match each part of unit 70 to its meaning.",
              [["चतुर्", "four"], ["अङ्गुल", "finger-breadth"], ["उत्सेध", "height"], ["पाद", "foot"]],
              "चतुर् = four, अङ्गुल = finger-breadth, उत्सेध = height, पाद = foot.",
              "चतुर्, अङ्गुल, उत्सेध, पाद."),
        fill(2, "Unit 70: चतुरंगुलोत्सेधः ____ (the foot). Type it in Devanagari or in English letters (e.g. dharma).",
             accepts("पादः", None, "padah", "pada"),
             "पादः (the foot): चतुरङ्गुलोत्सेधः पादः.",
             "चतुरङ्गुलोत्सेधः is a bahuvrīhi in the masculine, agreeing with पादः: the foot whose height is four aṅgulas.",
             "चतुरङ्गुलोत्सेधः पादः."),
        mcq("discriminate", 3, "Which split of चतुरंगुलोत्सेधः in unit 70 is right?",
            ("चतुर् + अङ्गुल + उत्सेधः", "र् joins the vowel; अ + उ → ओ: -अङ्गुल + उत्सेधः → -अङ्गुलोत्सेधः."),
            [("चतुर् + अङ्गुलः + उत्सेधः", "अः before उ would give a gap (अङ्गुल उत्सेधः), not ओ."),
             ("चतुर् + अङ्गुलो + त्सेधः", "त्सेधः is not a word; the ओ comes from अ + उ."),
             ("चतुर् + अङ्गुल + ओत्सेधः", "ओत्सेधः is not a word; the word is उत्सेध.")],
            "चतुर् (four) + अङ्गुल + उत्सेधः (height): अ + उ → ओ.",
            "अ + उ → ओ."),
        mcq("apply", 4, "By unit 70, which measure of the foot is four aṅgulas?",
            ("Its height", "चतुरङ्गुलोत्सेधः: the height (उत्सेध) is four aṅgulas."),
            [("Its full length", "The foot's length is fourteen (unit 68)."),
             ("Its girth", "The foot's girth is fourteen (unit 68)."),
             ("Its big toe", "The big toe is two aṅgulas long (unit 67).")],
            "उत्सेध = height: four aṅgulas.",
            "चतुरङ्गुलोत्सेधः पादः."),
        mcq("transfer", 5, "By the pattern of चतुरङ्गुलोत्सेधः, what does षडङ्गुलोत्सेधः mean in a new example?",
            ("Six aṅgulas high", "षट् (six) + अङ्गुल + उत्सेध (height): six aṅgulas high."),
            [("Six aṅgulas in girth", "Girth would need परिणाह: षडङ्गुलपरिणाहः."),
             ("Six aṅgulas broad", "Breadth would need विस्तार: षडङ्गुलविस्तारः."),
             ("Six aṅgulas long", "Length would need आयाम: षडङ्गुलायामः.")],
            "षडङ्गुलोत्सेधः = six aṅgulas high, like चतुरङ्गुलोत्सेधः = four aṅgulas high.",
            "number + अङ्गुल + उत्सेध = so many aṅgulas high.",
            teaches="A measure-bahuvrīhi joins number + अङ्गुल + the dimension: चतुरङ्गुलोत्सेधः = having a height of four aṅgulas."),
    ],
}

# ---------------------------------------------------------------- unit 71
AUTHORED["71"] = {
    "title": "अष्टादशायामा जंघाऊरुश्च",
    "question": "By unit 71, how long are the shank and the thigh?",
    "rule": ("The shank (जङ्घा) and the thigh (ऊरुः च) are eighteen in length (अष्टादशायामा); the feminine singular "
             "agrees with जङ्घा and is understood for both."),
    "limits": ("Prose, no verb printed. 'aṅgula' is understood after the numeral. The print keeps जंघा and ऊरुः "
               "apart (जंघाऊरु-) with no vowel join: no question on that join."),
    "explain_hi": ("जंघा (घुटने से टखने तक की टाँग) और ऊरु (जाँघ) लम्बाई में अठारह (अंगुल) हैं। "
                   "‘अष्टादशायामा’ स्त्रीलिंग एकवचन है; यह ‘जङ्घा’ से मेल खाता है और दोनों के लिए समझा जाता है। "
                   "इसमें अष्टादश + आयामा (अ + आ → आ) है; अष्टादश = आठ और दस, यानी अठारह। "
                   "छपाई में ‘जंघाऊरु’ बिना स्वर-सन्धि के है।"),
    "hook": "टाँग अठारह, जाँघ अठारह।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 71, what is the ऊरु?",
            ("The thigh", "ऊरु = thigh (standard)."),
            [("The shank", "The shank is the जङ्घा, named beside it."),
             ("The knee", "The knee is the जानु (unit 72)."),
             ("The ankle", "The ankle is the गुल्फ (unit 69).")],
            "जङ्घा = shank, ऊरु = thigh.",
            "ऊरु = thigh."),
        order(1, "Put the words of unit 71 in the printed order.",
              ["अष्टादशायामा", "जङ्घा", "ऊरुः", "च"],
              "Eighteen in length; the shank; the thigh; and.",
              "अष्टादशायामा → जङ्घा → ऊरुः → च."),
        match(2, "Match each word of unit 71 to its meaning.",
              [["अष्टादश", "eighteen"], ["आयाम", "length"], ["जङ्घा", "shank, lower leg"], ["ऊरु", "thigh"]],
              "अष्टादश = eighteen, आयाम = length, जङ्घा = shank, ऊरु = thigh.",
              "अष्टादश, आयाम, जङ्घा, ऊरु.", role="extend",
              teaches="अष्टादशायामा is feminine singular, agreeing with जङ्घा; it is understood for the thigh too."),
        mcq("discriminate", 3, "By unit 71, how long are the shank and the thigh?",
            ("Eighteen in length", "अष्टादशायामा: eighteen in length."),
            [("Thirty in length", "Thirty is the thigh's girth (unit 73), not a length."),
             ("Fourteen in length", "Fourteen is the length of the foot (unit 68)."),
             ("Sixteen in length", "Sixteen is the breadth of the kaṭī (unit 74).")],
            "अष्टादश = eighteen; आयाम = length.",
            "अष्टादशायामा जङ्घा ऊरुश्च."),
        mcq("apply", 4, "Which split of अष्टादशायामा in unit 71 is right?",
            ("अष्टादश + आयामा", "अ + आ → आ: अष्टादश + आयामा → अष्टादशायामा."),
            [("अष्टादशः + आयामा", "अः before आ would give a gap (अष्टादश आयामा), not one आ."),
             ("अष्टादश + यामा", "अ + य gives अय (अष्टादशयामा); the print has आया."),
             ("अष्टादशा + यामा", "अष्टादशा is not the numeral; the numeral is अष्टादश.")],
            "अष्टादश (eighteen) + आयामा (in length): अ + आ → आ.",
            "अ + आ → आ."),
        mcq("transfer", 5, "By the pattern of अष्टादश (eight + ten = eighteen), what number is द्वादश in a new example?",
            ("Twelve", "द्वा (two) + दश (ten) = twelve, like अष्ट + दश = eighteen."),
            [("Twenty", "Twenty is विंशति."),
             ("Two", "Two alone is द्वि."),
             ("Two hundred", "Two hundred is द्विशत.")],
            "द्वादश = 2 + 10 = twelve, like अष्टादश = 8 + 10 = eighteen.",
            "unit + दश = 11 to 19.",
            teaches="The numbers eleven to nineteen put the unit before दश: अष्टा-दश = eighteen, द्वा-दश = twelve."),
    ],
}

# ---------------------------------------------------------------- unit 72
AUTHORED["72"] = {
    "title": "चतुरंगुलं जानु",
    "question": "By unit 72, what measure is given for the knee, and what is left unstated?",
    "rule": "The knee (जानु) is of four aṅgulas (चतुरङ्गुलम्); the neuter agrees with the neuter noun जानु.",
    "limits": ("Prose, no verb printed. Which dimension (length, breadth, height) the four aṅgulas measure is not "
               "stated: no question asks which dimension is meant."),
    "explain_hi": ("जानु यानी घुटना चार अंगुल (चतुरङ्गुलम्) का है। "
                   "कौन-सा माप, लम्बाई, चौड़ाई या ऊँचाई, यह पाठ नहीं बताता। "
                   "‘चतुरङ्गुलम्’ नपुंसकलिंग है, क्योंकि ‘जानु’ नपुंसकलिंग है। "
                   "छपाई में ‘चतुरंगुलं जानु’: व्यंजन से पहले अन्तिम म् अनुस्वार (ं) लिखा गया।"),
    "hook": "घुटना: चार अंगुल, किस दिशा में यह खुला।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 72, what is the जानु?",
            ("The knee", "जानु = knee."),
            [("The ankle", "The ankle is the गुल्फ (unit 69)."),
             ("The thigh", "The thigh is the ऊरु (unit 71)."),
             ("The heel", "The heel is not the part named here.")],
            "जानु = knee.",
            "जानु = knee."),
        match(1, "Match each part of unit 72 to its meaning.",
              [["चतुर्", "four"], ["अङ्गुल", "finger-breadth"], ["जानु", "knee"]],
              "चतुर् = four, अङ्गुल = finger-breadth, जानु = knee.",
              "चतुर्, अङ्गुल, जानु."),
        fill(2, "Unit 72: चतुरंगुलं ____ (the knee). Type it in Devanagari or in English letters (e.g. dharma).",
             accepts("जानु", None, "janu"),
             "जानु (the knee): चतुरंगुलं जानु.",
             "जानु is a neuter उ-stem; its nominative singular is जानु, so the measure stands in the neuter: चतुरङ्गुलम्.",
             "चतुरङ्गुलं जानु."),
        mcq("discriminate", 3, "What does unit 72 leave unstated?",
            ("Which dimension is meant", "Length, breadth or height: the line does not say."),
            [("How many aṅgulas it is", "It says four: चतुरङ्गुलम्."),
             ("Which body part is meant", "It names the knee: जानु."),
             ("Which unit is used", "The unit is in the word itself: अङ्गुल.")],
            "Four aṅgulas, the knee: both stated; the dimension is not.",
            "चतुरङ्गुलं जानु (dimension not stated)."),
        mcq("apply", 4, "Why does चतुरङ्गुलम् stand in the neuter in unit 72?",
            ("It agrees with जानु, a neuter", "जानु is n. nom. sg., so its adjective is neuter: चतुरङ्गुलम्."),
            [("It agrees with पादः of unit 70", "पादः is masculine and belongs to unit 70; here the noun is जानु."),
             ("It is the object of a verb", "No verb is printed; चतुरङ्गुलम् is nominative with जानु."),
             ("It marks a count of four knees", "The count four is of aṅgulas; जानु is singular.")],
            "चतुरङ्गुलम् (n.) agrees with जानु (n.).",
            "An adjective agrees with its noun in gender."),
        mcq("transfer", 5, "By the pattern of चतुरंगुलं जानु, what does द्वादशाङ्गुलं फलकम् say in a new example?",
            ("The board is twelve aṅgulas", "द्वादश-अङ्गुलम् agrees with फलकम् (board): of twelve aṅgulas."),
            [("The board is two aṅgulas", "Two would be द्व्यङ्गुलम्; द्वादश is twelve."),
             ("The board is twenty aṅgulas", "Twenty would be विंशत्यङ्गुलम्; द्वादश is twelve."),
             ("There are twelve boards", "फलकम् is singular; twelve counts the aṅgulas.")],
            "द्वादशाङ्गुलं फलकम् = the board is twelve aṅgulas, like चतुरङ्गुलं जानु.",
            "number + अङ्गुल (neuter) + neuter noun.",
            teaches="A number + अङ्गुल compound takes the gender of the noun it measures: चतुरङ्गुलं जानु, द्वादशाङ्गुलं फलकम्."),
    ],
}

# ---------------------------------------------------------------- unit 73
AUTHORED["73"] = {
    "title": "त्रिंशदंगुलपरिणाहऊरुः",
    "question": "By unit 73, what is the girth of the thigh, and why is the visarga missing before ऊरुः?",
    "rule": ("The thigh (ऊरुः) is thirty aṅgulas in girth (त्रिंशदङ्गुलपरिणाहः). Printed परिणाहऊरुः = परिणाहः + ऊरुः: अः before a "
             "vowel other than अ loses its visarga, and the gap stays."),
    "limits": "Prose, no verb printed. The line gives only the girth; the thigh's length is in unit 71.",
    "explain_hi": ("ऊरु यानी जाँघ घेरे (परिणाह) में तीस अंगुल की है। "
                   "छपा ‘परिणाहऊरुः’ = परिणाहः + ऊरुः: अ के अलावा किसी स्वर से पहले अः का विसर्ग लुप्त होता है, और फिर कोई दूसरी सन्धि नहीं होती। "
                   "‘त्रिंशदङ्गुल’ में त्रिंशत् + अङ्गुल है: स्वर से पहले त् → द्। "
                   "जाँघ की लम्बाई, अठारह, इकाई ७१ में है।"),
    "hook": "जाँघ का घेरा: तीस अंगुल।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 73, what does परिणाह mean?",
            ("Girth", "परिणाह = girth, circumference."),
            [("Height", "Height is उत्सेध (unit 70)."),
             ("Length", "Length is आयाम (unit 71)."),
             ("Breadth", "Breadth is विस्तार (unit 74).")],
            "परिणाह = girth.",
            "परिणाह = girth."),
        order(1, "Put the parts of unit 73 in the printed order.",
              ["त्रिंशत्", "अङ्गुल", "परिणाहः", "ऊरुः"],
              "Thirty; aṅgula; girth; the thigh.",
              "त्रिंशत् → अङ्गुल → परिणाहः → ऊरुः."),
        match(2, "Match each part of unit 73 to its meaning.",
              [["त्रिंशत्", "thirty"], ["अङ्गुल", "finger-breadth"], ["परिणाह", "girth"], ["ऊरु", "thigh"]],
              "त्रिंशत् = thirty, अङ्गुल = finger-breadth, परिणाह = girth, ऊरु = thigh.",
              "त्रिंशत्, अङ्गुल, परिणाह, ऊरु.", role="extend",
              teaches="त्रिंशत् + अङ्गुल → त्रिंशदङ्गुल: a final त् before a vowel becomes द्."),
        mcq("discriminate", 3, "By unit 73, what is the girth of the thigh?",
            ("Thirty aṅgulas", "त्रिंशदङ्गुलपरिणाहः: thirty aṅgulas in girth."),
            [("Eighteen aṅgulas", "Eighteen is the thigh's length (unit 71)."),
             ("Fourteen aṅgulas", "Fourteen is the foot's girth (unit 68)."),
             ("Fifty aṅgulas", "Fifty is the girth of the kaṭī (unit 74).")],
            "त्रिंशत् = thirty: the thigh's girth.",
            "त्रिंशदङ्गुलपरिणाह ऊरुः."),
        mcq("apply", 4, "Why is परिणाहः printed परिणाह (no visarga) before ऊरुः in unit 73?",
            ("अः drops ः before a vowel not अ", "अः before a vowel other than अ loses its visarga: परिणाह ऊरुः."),
            [("अः before any vowel becomes ओ", "ओ arises before a voiced consonant (or as ओऽ before अ), not before ऊ."),
             ("The visarga before ऊ becomes र्", "र् comes after vowels other than अ/आ; here the vowel is अ."),
             ("The ः is left out by a misprint", "The data calls the dropped visarga regular sandhi, not a misprint.")],
            "परिणाहः + ऊरुः → परिणाह ऊरुः (visarga lost in hiatus).",
            "अः + vowel other than अ → अ (gap)."),
        mcq("transfer", 5, "By the pattern of परिणाहः + ऊरुः → परिणाह ऊरुः, how is रामः + इति joined in a new example?",
            ("राम इति", "अः before a vowel other than अ loses its visarga; the gap stays: राम इति."),
            [("रामो इति", "ओ arises from अः before a voiced consonant; इ is a vowel."),
             ("रामेति", "After the visarga drops, the two vowels are not joined again."),
             ("रामरिति", "र् comes from a visarga after a vowel other than अ/आ; here the vowel is अ.")],
            "रामः + इति = राम इति, like परिणाहः + ऊरुः = परिणाह ऊरुः.",
            "अः + vowel other than अ → अ (gap).",
            teaches="A final अः before a vowel other than अ loses its visarga, and the gap stays: परिणाह ऊरुः."),
    ],
}

# ---------------------------------------------------------------- unit 74
AUTHORED["74"] = {
    "title": "षडायामौ मुष्कमेंढ्रौ; षोडशविस्तारा कटी",
    "question": "By unit 74, what are the measures of the muṣka and meḍhra, and of the kaṭī?",
    "rule": ("The muṣka (scrotum or testicles) and meḍhra (penis) are both six in length, and eight and five in "
             "girth; the kaṭī (hip or waist region) is sixteen in breadth and fifty in girth."),
    "limits": ("Prose, two printed lines joined. Pairing 'eight and five' with the two organs in order is the natural "
               "reading, not stated: no question asks which organ is eight. Printed मेंढ्र is read मेढ्र. muṣka = "
               "testicle or scrotum (standard; the dictionaries give both). 'aṅgula' is understood after the numerals."),
    "explain_hi": ("मुष्क (अण्डकोश या वृषण) और मेढ्र (शिश्न), दोनों लम्बाई में छः हैं और घेरे में आठ और पाँच हैं। "
                   "आठ और पाँच की जोड़ी क्रम से दोनों अंगों पर लगाना स्वाभाविक पाठ है, छपा नहीं; इसलिए उस पर प्रश्न नहीं। "
                   "दूसरी पंक्ति: कटी (कमर या कूल्हे का भाग) चौड़ाई में सोलह और घेरे में पचास है; अंक के बाद ‘अंगुल’ समझा जाता है। "
                   "छपा ‘मेंढ्र’ डेटा में ‘मेढ्र’ पढ़ा गया है। "
                   "‘मुष्कमेढ्रावष्ट’ में मेढ्रौ + अष्ट है: स्वर से पहले औ → आव्।"),
    "hook": "छः लम्बे, आठ-पाँच घेरे; कटी सोलह चौड़ी, पचास घेरा।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In unit 74, what is the कटी?",
            ("The hip or waist region", "कटी = hip or waist region (standard)."),
            [("The chest or breast region", "The chest is not named in unit 74; कटी is the hip region."),
             ("The neck or throat region", "The neck is not named in unit 74; कटी is the hip region."),
             ("The shoulder or arm region", "The shoulder is not named in unit 74; कटी is the hip region.")],
            "कटी = hip or waist region.",
            "कटी = hip, waist region."),
        order(1, "Put the phrases of unit 74 in the printed order.",
              ["षडायामौ", "मुष्कमेढ्रौ", "अष्टपञ्चपरिणाहौ", "षोडशविस्तारा", "कटी", "पञ्चाशत्परिणाहा"],
              "Six in length; the muṣka and meḍhra; eight and five in girth; sixteen in breadth; the kaṭī; fifty in girth.",
              "षडायामौ → मुष्कमेढ्रौ → अष्टपञ्चपरिणाहौ → षोडशविस्तारा → कटी → पञ्चाशत्परिणाहा."),
        match(2, "Match each word of unit 74 to its meaning.",
              [["मुष्क", "scrotum or testicles"], ["मेढ्र", "penis"], ["कटी", "hip or waist region"],
               ["विस्तार", "breadth"], ["परिणाह", "girth"], ["आयाम", "length"]],
              "मुष्क = scrotum or testicles, मेढ्र = penis, कटी = hip region, विस्तार = breadth, परिणाह = girth, आयाम = length.",
              "मुष्क, मेढ्र, कटी, विस्तार, परिणाह, आयाम.", role="extend",
              teaches="The dual -औ of षडायामौ, मुष्कमेढ्रौ and अष्टपञ्चपरिणाहौ marks the two organs taken together."),
        mcq("discriminate", 3, "By unit 74, what are the breadth and the girth of the कटी?",
            ("Sixteen broad, fifty around", "षोडशविस्तारा कटी पञ्चाशत्परिणाहा: sixteen broad, fifty in girth."),
            [("Fifty broad, sixteen around", "The numbers are swapped: षोडश goes with विस्तार."),
             ("Sixteen broad, thirty around", "Thirty is the thigh's girth (unit 73)."),
             ("Six broad, fifty around", "Six is the length of the muṣka and meḍhra.")],
            "कटी: breadth sixteen, girth fifty.",
            "षोडशविस्तारा कटी पञ्चाशत्परिणाहा."),
        mcq("apply", 4, "Why is -मेढ्रौ printed -मेंढ्राव् before अष्ट in unit 74?",
            ("औ before a vowel → आव्", "-मेढ्रौ + अष्ट-: औ before a vowel becomes आव्."),
            [("औ before a vowel is dropped", "It is not dropped; it becomes आव्."),
             ("औ + अ → ओ in all cases", "ओ comes from अ + उ; औ before a vowel gives आव्."),
             ("आव् is part of the stem", "The stem is मेढ्र; आव् comes only from sandhi.")],
            "-मेढ्रौ + अष्ट → -मेढ्रावष्ट: औ + vowel → आव्.",
            "औ + vowel → आव्."),
        mcq("transfer", 5, "By the pattern of -मेढ्रौ + अष्ट → -मेढ्रावष्ट, how is तौ + अपि (those two too) joined in a new example?",
            ("तावपि", "औ before a vowel → आव्: तौ + अपि → तावपि."),
            [("तौऽपि", "ऽ marks an अ dropped after ए or ओ, not after औ."),
             ("तापि", "औ is not dropped; it becomes आव्."),
             ("तवपि", "अव् comes from ओ before a vowel; here the vowel is औ.")],
            "तौ + अपि = तावपि, like -मेढ्रौ + अष्ट = -मेढ्रावष्ट.",
            "औ + vowel → आव्.",
            teaches="ए, ऐ, ओ, औ before a vowel become अय्, आय्, अव्, आव्: -मेढ्रौ + अष्ट → -मेढ्रावष्ट."),
    ],
}

# ================================================================ NOTES_HI
NOTES_HI = {
    "63": ("गद्य; विश्वास मध्यम; पंक्ति ०२.०८.७६; कोई पाठ-चिह्न नहीं, कोई अस्पष्ट पंक्ति नहीं। डेटा के अनुसार ‘उभयम्’ इकाई ६२ (छपी पंक्ति ७५) "
           "के दो अनुमानों की ओर संकेत है; इकाई ६२ की आरम्भिक क्रिया स्वयं अनुमानित पाठ है। ‘गजसिंहे’ द्वन्द्व ‘गजसिंह’ का सप्तमी एकवचन पढ़ा गया; "
           "हाथी और सिंह में कौन-सा अनुमान किस प्रकार उलटा है, पाठ नहीं कहता। सन्धि जाँची: तत् + च → तच्च (च से पहले त् → च्); "
           "च + उभयम् → चोभयम् (अ + उ → ओ); उभयम् + अपि → उभयमपि; अपि + अन्यथा → अप्यन्यथा (इ + भिन्न स्वर → य्); "
           "दृष्टम् + गज- → दृष्टं गज- (व्यंजन से पहले अन्तिम म् → ं)।"),
    "64": ("गद्य; विश्वास मध्यम; पंक्ति ०२.०८.७७; कोई पाठ-चिह्न नहीं। सार यहाँ गिनाए नहीं (इकाई ६० में आठ)। ‘तत्र’ का पूर्वपद नहीं बताया। "
           "‘गौरव’ = शरीर का भारीपन या आचरण की गरिमा, दोनों अर्थ सम्भव। ‘मन्द’ जरा और आमय दोनों के साथ, और ‘प्रायः’ आगे या पीछे के पद से, "
           "ये पढ़ने के ढंग हैं। छपा ‘उपैतो’ है; डेटा इसे उप-√इ का कृदन्त ‘उपैतः’ लेता है, (उप-√इ से रूप ‘उपेत’ होता; ‘उपैत’ उप + आ + √इ से भी समझा जा सकता है): इस रूप पर प्रश्न नहीं। "
           "सन्धि जाँची: सारैः + उपैतः → सारैरुपैतः (ऐः + स्वर → ऐर्); उपैतः + भवति → उपैतो भवति (अः + घोष व्यंजन → ओ); "
           "भवति + अतिबलः → भवत्यतिबलः (इ + भिन्न स्वर → य्); -आरम्भेषु + आत्मनि → -आरम्भेष्वात्मनि (उ + भिन्न स्वर → व्); "
           "प्रायः + तुल्य- → प्रायस्तुल्य- (त से पहले विसर्ग → स्); -अपत्यः + दीर्घायुः → -अपत्यो दीर्घायुः; दीर्घायुः + च → दीर्घायुश्च। "
           "‘क्लेशक्षमःसर्वा-’ में स से पहले विसर्ग छपा है (स् भी शुद्ध)।"),
    "65": ("गद्य; विश्वास मध्यम; पंक्ति ०२.०८.७८; कोई पाठ-चिह्न नहीं। ‘तत्’ = इकाई ६४ (छपी पंक्ति ७७) का सब सारों वाला व्यक्ति, डेटा का पाठ। "
           "असार = हर सार का पूरा अभाव या नहीं, यह नहीं कहा। क्रिया समझी जाती है। सन्धि जाँची: तत् + विपरीतः → तद्विपरीतः (घोष व से पहले त् → द्); "
           "विपरीतः + तु → विपरीतस्तु (त से पहले विसर्ग → स्); तु + असारः → त्वसारः (उ + अ → व); मध्यः + मध्यगुणः → मध्यो मध्यगुणः "
           "(अः + घोष व्यंजन → ओ)। ‘असारः मध्यो’ में विसर्ग वाक्यांश के अन्त में है, इसलिए सन्धि नहीं की गई।"),
    "66": ("गद्य; विश्वास उच्च; पंक्ति ०२.०८.७९; कोई पाठ-चिह्न नहीं। आगे के अंग-मापों की भूमिका; क्रिया समझी जाती है। "
           "सन्धि जाँची: स्व + अङ्गुलैः → स्वाङ्गुलैः (अ + अ → आ); प्रमाणम् + पुनः → प्रमाणं पुनः (व्यंजन से पहले म् → ं)। "
           "छपाई में ‘स्वांगुलैः’ अनुस्वार के साथ, विभाजन अङ्गुल।"),
    "67": ("गद्य; विश्वास मध्यम; पंक्ति ०२.०८.८०; कोई पाठ-चिह्न नहीं। पैर की प्रदेशिनी = अँगूठे के बाद की अंगुली (मानक)। बाकी तीन अंगुलियों के नाम नहीं; "
           "‘पाँचवाँ भाग’ किसका, और ‘तत्’ पिछली अंगुली का नख या हर अंगुली का अपना, दोनों खुले; नख की लम्बाई कैसे तय हो, यह भी नहीं कहा। "
           "सन्धि जाँची: द्वि + अङ्गुल → द्व्यङ्गुल (इ + भिन्न स्वर → य्); -अङ्गुल + आयते → -अङ्गुलायते (अ + आ → आ); "
           "तिस्रः + अन्याः → तिस्रोऽन्याः (अः + अ → ओऽ); क्रमेण + उत्तर- → क्रमेणोत्तर- (अ + उ → ओ); -हीनाः + तत् → -हीनास्तत् "
           "(त से पहले विसर्ग → स्); तत् + नख → तन्नख (नासिक्य से पहले त् → न् वैकल्पिक, द् भी शुद्ध); -हीनाः + वा → -हीना वा "
           "(घोष ध्वनि से पहले आः का विसर्ग लुप्त)।"),
    "68": ("गद्य; विश्वास मध्यम; पंक्ति ०२.०८.८१; कोई पाठ-चिह्न नहीं। प्रपद = पैर का अगला भाग, पाष्णि = एड़ी (मानक)। छः, पाँच, चार की चौड़ाई "
           "तीन भागों पर क्रम से लगाना स्वाभाविक पाठ है, छपा नहीं। भागों का कोई योग पाठ नहीं देता। छपा ‘पाष्ण्यः’ असामान्य रूप है (सामान्य पार्ष्णि/पाष्णि का प्रथमा बहुवचन -णयः), उस पर प्रश्न नहीं। "
           "सन्धि जाँची: चतुर् + अङ्गुल → चतुरङ्गुल; -अङ्गुल + आयताः → -अङ्गुलायताः (अ + आ → आ); -विस्तृताः + चतुर्दश → "
           "-विस्तृताश्चतुर्दश और पादः + चतुर्दश → पादश्चतुर्दश (च से पहले विसर्ग → श्); चतुर्दश + एव → चतुर्दशैव (अ + ए → ऐ); "
           "एव + आयामेन → एवायामेन (अ + आ → आ)।"),
    "69": ("गद्य; विश्वास मध्यम; पंक्ति ०२.०८.८२; कोई पाठ-चिह्न नहीं। अधूरी पंक्ति: न माप छपा है, न क्रिया। ‘तथा’ शायद इकाई ६८ (छपी पंक्ति ८१) "
           "से कोई माप (जैसे घेरा) लाता है, या छपाई में माप छूट गया; डेटा यह दावा नहीं करता। इकाई ७० (छपी पंक्ति ८३) नया विषय, पैर की ऊँचाई, आरम्भ करती है। "
           "गुल्फ = टखना, जङ्घा = घुटने से टखने तक की टाँग (मानक); हिन्दी ‘जाँघ’ नहीं। सन्धि जाँची: जङ्घामध्यम् + च → जंघामध्यं च "
           "(व्यंजन से पहले म् → ं; छपाई में बिना स्थान ‘जंघामध्यंच’)।"),
    "70": ("गद्य; विश्वास उच्च; पंक्ति ०२.०८.८३; कोई पाठ-चिह्न नहीं। क्रिया समझी जाती है; अंक के साथ ‘अंगुल’ छपा है। "
           "सन्धि जाँची: चतुर् + अङ्गुल → चतुरङ्गुल; -अङ्गुल + उत्सेधः → -अङ्गुलोत्सेधः (अ + उ → ओ)। ‘उत्सेधः पादः’ में प से पहले विसर्ग ज्यों का त्यों।"),
    "71": ("गद्य; विश्वास मध्यम; पंक्ति ०२.०८.८४; कोई पाठ-चिह्न नहीं। ‘अष्टादशायामा’ स्त्रीलिंग एकवचन, ‘जङ्घा’ से मेल, दोनों के लिए समझा जाता है; "
           "ऊरु = जाँघ (मानक); अंक के बाद ‘अंगुल’ समझा जाता है। छपा ‘जंघाऊरु-’ बिना स्वर-सन्धि है (आ + ऊ सामान्यतः ओ देता); डेटा इस पर कुछ नहीं कहता, "
           "इसलिए इस पर प्रश्न नहीं। सन्धि जाँची: अष्टादश + आयामा → अष्टादशायामा (अ + आ → आ); ऊरुः + च → ऊरुश्च (च से पहले विसर्ग → श्)।"),
    "72": ("गद्य; विश्वास उच्च; पंक्ति ०२.०८.८५; कोई पाठ-चिह्न नहीं। माप कौन-सा (लम्बाई, चौड़ाई), यह नहीं बताया। क्रिया समझी जाती है। "
           "सन्धि जाँची: चतुरङ्गुलम् + जानु → चतुरंगुलं जानु (व्यंजन से पहले म् → ं)।"),
    "73": ("गद्य; विश्वास उच्च; पंक्ति ०२.०८.८६; कोई पाठ-चिह्न नहीं। छपा ‘परिणाहऊरुः’ = परिणाहः + ऊरुः: अ के अलावा स्वर से पहले अः का विसर्ग लुप्त, "
           "नियमित सन्धि (डेटा)। सन्धि जाँची: त्रिंशत् + अङ्गुल → त्रिंशदङ्गुल (स्वर से पहले त् → द्)।"),
    "74": ("गद्य; विश्वास मध्यम; दो छपी पंक्तियाँ (०२.०८.८७ और ०२.०८.८८) जोड़ी गईं; कोई पाठ-चिह्न नहीं। छपा ‘मेंढ्र’ डेटा में ‘मेढ्र’ पढ़ा गया (संयुक्ताक्षर "
           "से पहले अनुनासिक, वर्तनी सामान्य की गई)। मुष्क = अण्डकोश या वृषण (मानक, कोश दोनों देते हैं), मेढ्र = शिश्न, कटी = कमर या कूल्हे का भाग (मानक)। "
           "‘आठ और पाँच’ की जोड़ी क्रम से दोनों अंगों पर, स्वाभाविक पाठ, छपी नहीं। सन्धि जाँची: षट् + आयामौ → षडायामौ (स्वर से पहले ट् → ड्); "
           "-मेढ्रौ + अष्ट- → -मेढ्रावष्ट- (स्वर से पहले औ → आव्)।"),
}

# ================================================================ AIDS
AIDS = {
    "63": {
        "chain": {"steps": ["इकाई ६२, अनुमान १: बड़ा शरीर, तो बलवान", "इकाई ६२, अनुमान २: कृश या छोटा शरीर, तो अल्पबल",
                            "इकाई ६३: दोनों अन्यथा भी देखे गए", "उदाहरण: गज और सिंह (किस प्रकार, यह नहीं कहा)"]},
        "chunks": "तच्चोभयमप्यन्यथादृष्टं | गजसिंहे",
        "sandhi": ("च से पहले त् → च्: तत् + च → तच्च · अ + उ → ओ: च + उभयम् → चोभयम् · इ + भिन्न स्वर → य्: अपि + अन्यथा → "
                   "अप्यन्यथा।"),
    },
    "64": {
        "diagram": {"groups": [
            {"label": "तत्र सर्वैः सारैरुपैतो भवति", "items": [
                "अतिबलः", "परमगौरवयुक्तः", "क्लेशक्षमः", "सर्वारम्भेष्वात्मनि प्रत्याशावान्", "कल्याणाभिनिवेशी",
                "स्थिरशरीरः", "सुसमाहितगतिः", "सानुनादस्निग्धगम्भीरमहास्वरः", "सुखैश्वर्यवित्तोपभोगः", "सन्मानभाक्",
                "मन्दजरामयः, प्रायः तुल्यगुणविस्तीर्णापत्यः", "दीर्घायुः"]}]},
        "frame": ("कौन: सर्वैः सारैः उपैतः (सब सारों से युक्त) → बल: अतिबल, क्लेशक्षम → शरीर: स्थिर, सुसमाहित गति, महान स्वर → "
                  "जीवन: सुख, ऐश्वर्य, सम्मान → अन्त: दीर्घायु।"),
        "sandhi": ("ऐः + स्वर → ऐर्: सारैः + उपैतः → सारैरुपैतः · इ + भिन्न स्वर → य्: भवति + अतिबलः → भवत्यतिबलः · "
                   "उ + भिन्न स्वर → व्: -आरम्भेषु + आत्मनि → -आरम्भेष्वात्मनि · त से पहले विसर्ग → स्: प्रायः + तुल्य → प्रायस्तुल्य।"),
        "pegs": "बल → शरीर → स्वर → सुख → सम्मान → आयु: सूची को छः पड़ावों में याद करें। (मेरी बनाई याद-पद्धति)",
    },
    "65": {
        "diagram": {"groups": [
            {"label": "तद्विपरीतस्तु", "items": ["असारः: सार से रहित"]},
            {"label": "मध्यः", "items": ["मध्यगुणः: मध्यम गुणों वाला"]}]},
        "chunks": "तद्विपरीतस्त्वसारः | मध्यो मध्यगुणः",
        "sandhi": ("घोष व से पहले त् → द्: तत् + विपरीतः → तद्विपरीतः · त से पहले विसर्ग → स्: विपरीतः + तु → विपरीतस्तु · "
                   "उ + अ → व: तु + असारः → त्वसारः · अः + घोष व्यंजन → ओ: मध्यः + मध्यगुणः → मध्यो मध्यगुणः।"),
    },
    "66": {
        "chunks": "प्रमाणं पुनः | स्वांगुलैः",
        "sandhi": "अ + अ → आ: स्व + अङ्गुलैः → स्वाङ्गुलैः · व्यंजन से पहले अन्तिम म् → ं: प्रमाणम् + पुनः → प्रमाणं पुनः।",
        "anchors": "स्व = अपना: हर व्यक्ति अपने ही अंगुल से नापा जाता है; आगे के सारे अंक इसी अंगुल में। (मेरी याद-पद्धति)",
    },
    "67": {
        "diagram": {"groups": [
            {"label": "पादांगुष्ठप्रदेशिन्यौ", "items": ["द्व्यंगुलायते: दो अंगुल लम्बे"]},
            {"label": "तिस्रोऽन्याः क्रमेणोत्तरोत्तरं", "items": ["पंचमभागहीनाः", "तन्नखहीना वा"]}]},
        "chunks": "पादांगुष्ठप्रदेशिन्यौ | द्व्यंगुलायते | तिस्रोऽन्याः | क्रमेणोत्तरोत्तरं | पंचमभागहीनास्तन्नखहीना वा",
        "sandhi": ("इ + भिन्न स्वर → य्: द्वि + अङ्गुल → द्व्यङ्गुल · अः + अ → ओऽ: तिस्रः + अन्याः → तिस्रोऽन्याः · "
                   "अ + उ → ओ: क्रमेण + उत्तर → क्रमेणोत्तर · घोष ध्वनि से पहले आः का विसर्ग लुप्त: -हीनाः + वा → -हीना वा।"),
    },
    "68": {
        "diagram": {"groups": [
            {"label": "चतुरंगुलायताः पृथक्", "items": ["प्रपद", "पादतल", "पाष्णि"]},
            {"label": "षट्पंचचतुरंगुलविस्तृताः", "items": ["छः, पाँच, चार (जोड़ी छपी नहीं)"]},
            {"label": "पादः", "items": ["चतुर्दशैवायामेन", "चतुर्दशैव परिणाहेन"]}]},
        "chunks": "चतुरंगुलायताः | पृथक्प्रपदपादतलपाष्ण्यः | षट्पंचचतुरंगुलविस्तृताश्चतुर्दशैवायामेन | पादश्चतुर्दशैव परिणाहेन",
        "sandhi": ("च से पहले विसर्ग → श्: -विस्तृताः + चतुर्दश → -विस्तृताश्चतुर्दश, पादः + चतुर्दश → पादश्चतुर्दश · "
                   "अ + ए → ऐ: चतुर्दश + एव → चतुर्दशैव · अ + आ → आ: एव + आयामेन → एवायामेन।"),
        "anchors": "आगे-बीच-पीछे: प्रपद, तल, पाष्णि, तीनों चार-चार लम्बे; पूरा पैर चौदह का दोहरा: लम्बाई भी, घेरा भी। (मेरी याद-पद्धति)",
    },
    "69": {
        "frame": "जोड़: तथा (वैसे ही) → क्या: गुल्फौ (दोनों टखने), जङ्घामध्यम् (जंघा का मध्य) → माप: छपा नहीं → क्रिया: छपी नहीं।",
        "chunks": "तथा | गुल्फौ | जंघामध्यंच",
        "sandhi": "व्यंजन से पहले अन्तिम म् → ं: जङ्घामध्यम् + च → जंघामध्यं च।",
    },
    "70": {
        "chunks": "चतुरंगुलोत्सेधः | पादः",
        "sandhi": "अ + उ → ओ: -अङ्गुल + उत्सेधः → -अङ्गुलोत्सेधः।",
        "anchors": "तीन माप याद रखें: आयाम = लम्बाई, परिणाह = घेरा, उत्सेध = ऊँचाई; पैर: १४, १४, ४। (मेरी याद-पद्धति)",
    },
    "71": {
        "chunks": "अष्टादशायामा | जंघाऊरुश्च",
        "sandhi": "अ + आ → आ: अष्टादश + आयामा → अष्टादशायामा · च से पहले विसर्ग → श्: ऊरुः + च → ऊरुश्च।",
        "letters": "अष्टा-दश: आठ और दस, अठारह; जंघा और ऊरु, दोनों अठारह। (केवल सुनने की सहायता)",
    },
    "72": {
        "chunks": "चतुरंगुलं | जानु",
        "sandhi": "व्यंजन से पहले अन्तिम म् → ं: चतुरङ्गुलम् + जानु → चतुरंगुलं जानु।",
    },
    "73": {
        "chunks": "त्रिंशदंगुलपरिणाह | ऊरुः",
        "sandhi": ("स्वर से पहले त् → द्: त्रिंशत् + अङ्गुल → त्रिंशदङ्गुल · अ के अलावा स्वर से पहले अः का विसर्ग लुप्त: "
                   "परिणाहः + ऊरुः → परिणाह ऊरुः।"),
        "anchors": "जाँघ: लम्बाई अठारह (इकाई ७१), घेरा तीस (इकाई ७३)। (मेरी याद-पद्धति)",
    },
    "74": {
        "diagram": {"groups": [
            {"label": "मुष्कमेंढ्रौ", "items": ["षडायामौ: लम्बाई छः", "अष्टपंचपरिणाहौ: घेरा आठ और पाँच"]},
            {"label": "कटी", "items": ["षोडशविस्तारा: चौड़ाई सोलह", "पंचाशत्परिणाहा: घेरा पचास"]}]},
        "chunks": "षडायामौ | मुष्कमेंढ्रावष्टपंचपरिणाहौ || षोडशविस्तारा | कटी | पंचाशत्परिणाहा",
        "sandhi": "स्वर से पहले ट् → ड्: षट् + आयामौ → षडायामौ · स्वर से पहले औ → आव्: -मेढ्रौ + अष्ट → -मेढ्रावष्ट।",
    },
}

# ================================================================ IMAGE_SPECS
IMAGE_SPECS = {
    ("63", "chain"): {
        "file": "sh8-anyatha-gaja-63.svg",
        "alt": ("Flowchart of card 63: the two judgements of card 62, a large body means strong and a thin or small "
                "body means weak, are both also seen to be otherwise, in the elephant and the lion."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"कार्ड ६२: बड़ा शरीर, बलवान\"] --> C[\"दोनों अन्यथा भी दिखे\"]\n"
                 "  B[\"कार्ड ६२: कृश शरीर, अल्पबल\"] --> C\n"
                 "  C --> D[\"गज और सिंह में\"]\n"),
    },
    ("64", "diagram"): {
        "file": "sh8-sarva-sara-64.svg",
        "alt": ("Table of card 64 in printed order: the marks of one endowed with all the sāras, from exceedingly "
                "strong to long-lived."),
        "type": "table",
        "title": "कार्ड ६४: सब सारों वाले के लक्षण",
        "heads": ["क्रम", "लक्षण"],
        "rows": [["१", "अतिबल: अत्यन्त बलवान"], ["२", "परम गौरव: भारीपन या गरिमा"], ["३", "क्लेशक्षम: क्लेश सहने वाला"],
                 ["४", "प्रत्याशावान्: अपने पर आशा"], ["५", "कल्याणाभिनिवेशी"], ["६", "स्थिरशरीर"],
                 ["७", "सुसमाहितगति: सुसंयत चाल"], ["८", "सानुनाद, स्निग्ध, गम्भीर महास्वर"], ["९", "सुख, ऐश्वर्य, धन का उपभोग"],
                 ["१०", "सन्मानभाक्: सम्मान पाने वाला"], ["११", "मन्दजरामय: मन्द जरा और रोग"], ["१२", "प्रायः तुल्यगुणविस्तीर्णापत्य: समान गुणों वाली विस्तृत सन्तान"], ["१३", "दीर्घायु"]],
    },
    ("67", "diagram"): {
        "file": "sh8-padanguli-67.svg",
        "alt": ("Table of card 67: the big toe and the second toe are two aṅgulas long; the other three, in order, are "
                "less by a fifth part or by their nail."),
        "type": "table",
        "title": "कार्ड ६७: पैर की अंगुलियाँ",
        "heads": ["अंगुली", "लम्बाई"],
        "rows": [["अङ्गुष्ठ: अँगूठा", "दो अंगुल"], ["प्रदेशिनी: दूसरी अंगुली", "दो अंगुल"],
                 ["अन्य तीन, क्रम से", "पाँचवाँ भाग कम, या नख-भर कम"]],
    },
    ("68", "diagram"): {
        "file": "sh8-pada-mana-68.svg",
        "alt": ("Table of card 68: prapada, sole and heel each four aṅgulas long; breadths six, five, four (pairing not "
                "printed); the whole foot fourteen in length and fourteen in girth."),
        "type": "table",
        "title": "कार्ड ६८: पैर के माप",
        "heads": ["भाग", "माप (अंगुल)"],
        "rows": [["प्रपद, पादतल, पाष्णि", "हर एक चार लम्बा"], ["उनकी चौड़ाई", "छः, पाँच, चार (जोड़ी छपी नहीं)"],
                 ["पूरा पैर: आयाम", "चौदह"], ["पूरा पैर: परिणाह", "चौदह"]],
    },
    ("74", "diagram"): {
        "file": "sh8-kati-74.svg",
        "alt": ("Table of card 74: muṣka and meḍhra six in length and eight and five in girth (pairing not printed); "
                "kaṭī sixteen in breadth and fifty in girth."),
        "type": "table",
        "title": "कार्ड ७४: मुष्क, मेढ्र और कटी",
        "heads": ["अंग", "माप (अंगुल)"],
        "rows": [["मुष्क और मेढ्र: लम्बाई", "छः"], ["मुष्क और मेढ्र: घेरा", "आठ और पाँच (जोड़ी छपी नहीं)"],
                 ["कटी: चौड़ाई", "सोलह"], ["कटी: घेरा", "पचास"]],
    },
    ("65", "diagram"): {
        "file": "sh8-asara-madhya-65.svg",
        "alt": ("Table of card 65: the opposite of the one with all the sāras (card 64) is without sāra; the middle "
                "one has middling qualities."),
        "type": "table",
        "title": "कार्ड ६५: असार और मध्य",
        "heads": ["कौन", "क्या"],
        "rows": [["तत्: सब सारों वाला (कार्ड ६४)", "अतिबल आदि लक्षण"], ["तद्विपरीतः", "असार: सार से रहित"],
                 ["मध्यः", "मध्यगुण: मध्यम गुण"]],
    },
}
