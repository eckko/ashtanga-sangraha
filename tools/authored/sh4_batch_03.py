from helpers import mcq, match, order, fill, multi, accepts


AUTHORED = {}

# ---------------------------------------------------------------- unit 28
AUTHORED["28"] = {
    "title": "अपूर्णत्रिमासायास्तु पुष्पदर्शने",
    "question": "By unit 28, what happens when bleeding is seen before three months are complete, and why?",
    "rule": ("When puṣpa (bleeding) is seen in her whose three months are not complete, the garbha generally (प्रायः) "
             "does not stay, because its sāra (essence, firmness) has not yet developed (असंजातसारत्वात्)."),
    "limits": ("प्रायः = generally, not always. The exact doctrinal sense of sāra is not given. 'Months of pregnancy' is "
               "understood from garbha, not printed. No treatment or later month is "
               "covered here. Prose; the data says unit 29 appears to continue this sentence."),
    "explain_hi": ("यह गद्य-पंक्ति कहती है कि जिस स्त्री के तीन मास पूरे नहीं हुए, उसमें पुष्प यानी रक्तस्राव दिखे तो गर्भ प्रायः नहीं टिकता। "
                   "कारण भी दिया गया है: उसमें सार (दृढ़ता, ठोसपन) अभी उत्पन्न नहीं हुआ होता (असंजातसारत्वात्)। "
                   "‘प्रायः’ का अर्थ है अधिकतर, हमेशा नहीं। "
                   "‘सार’ का ठीक शास्त्रीय अर्थ यहाँ नहीं बताया गया। "
                   "‘अपूर्णत्रिमासा’ बहुव्रीहि है: जिसके तीन मास पूरे नहीं हुए।"),
    "hook": "तीन मास से पहले स्राव: सार नहीं बना, गर्भ प्रायः नहीं टिकता।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 28, what generally happens to the garbha when bleeding is seen before three months?",
            ("It generally does not stay", "गर्भः प्रायो न तिष्ठति: the garbha generally does not stay."),
            [("It is lost in each and every case", "प्रायः means generally, not always; the unit does not say every case."),
             ("It grows on, only slower", "No slower growth is named; the unit says it generally does not stay."),
             ("It stays firm, unharmed", "The unit says the opposite: it generally does not stay.")],
            "Before three months, with bleeding, the garbha generally does not stay.",
            "पुष्पदर्शने गर्भः प्रायो न तिष्ठति."),
        order(1, "Put the words of unit 28 in the line's order.",
              ["अपूर्णत्रिमासायाः तु", "पुष्पदर्शने", "गर्भः", "प्रायः", "न तिष्ठति", "असंजातसारत्वात्"],
              "Of her whose three months are not complete, but, at the sight of puṣpa, the garbha, generally, does not "
              "stay, because sāra has not developed.",
              "अपूर्णत्रिमासायाः तु → पुष्पदर्शने → गर्भः → प्रायः → न तिष्ठति → असंजातसारत्वात्."),
        match(2, "Match each word of unit 28 to its meaning.",
              [["अपूर्णत्रिमासा", "she whose three months are not complete"], ["पुष्प", "the 'flower': bleeding"],
               ["प्रायः", "generally"], ["सार", "essence, firmness"], ["असंजात", "not yet developed"]],
              "The time, the sign, the result (generally not staying) and its reason.",
              "अपूर्णत्रिमासा, पुष्प, प्रायः, सार, असंजात.", role="extend",
              teaches="असंजातसारत्वात् = because of the state of having sāra not yet developed: -त्वात् gives the reason."),
        mcq("discriminate", 3, "Why is प्रायः printed प्रायो before न in unit 28?",
            ("अः before voiced न becomes ओ", "Visarga after अ before a voiced sound (न is voiced) becomes ओ."),
            [("ओ marks a dual ending here", "प्रायः is an indeclinable in the data; it has no dual."),
             ("अः becomes ओ before any consonant", "Not before an unvoiced one: गर्भः प्रायः keeps the visarga before प."),
             ("प्रायो is a vocative form here", "प्रायः is the indeclinable 'generally'; nobody is addressed.")],
            "प्रायः + न = प्रायो न, because न is a voiced sound.",
            "अः + voiced sound → ओ."),
        mcq("apply", 4, "A woman in her fifth month shows bleeding. Does unit 28's statement cover her case?",
            ("No: it covers only the first three", "अपूर्णत्रिमासायाः: the unit speaks of her whose three months are not complete."),
            [("Yes: it covers every month alike", "The unit is limited to her whose three months are not complete."),
             ("Yes: after three months it never stays", "Unit 28 says nothing about after three months."),
             ("No: it covers bleeding after birth", "The unit is about pregnancy, before three months are complete.")],
            "Unit 28 is limited to the time before three months are complete.",
            "अपूर्णत्रिमासा = she whose three months are not complete."),
        mcq("transfer", 5, "By the rule of तिष्ठत्यसंजात..., how is तिष्ठति + अत्र (stays here) written when joined?",
            ("तिष्ठत्यत्र", "इ before a different vowel becomes य्: तिष्ठति + अत्र → तिष्ठत्यत्र."),
            [("तिष्ठतेऽत्र", "ए + अ would give एऽ, but the verb ends in इ, not ए."),
             ("तिष्ठतात्र", "इ does not vanish before अ, nor does it become आ."),
             ("तिष्ठतीत्र", "ई comes from इ + इ, not from इ + अ.")],
            "तिष्ठति + अत्र = तिष्ठत्यत्र, like तिष्ठति + असंजात... = तिष्ठत्यसंजात....",
            "इ + a different vowel → य् + that vowel.",
            teaches="A final इ before a different vowel becomes य्: तिष्ठति + असंजात → तिष्ठत्यसंजात."),
    ],
}

# ---------------------------------------------------------------- unit 29
AUTHORED["29"] = {
    "title": "आमान्वये चोर्ध्वमपि",
    "question": "What do the sure parts of unit 29 say, and why is its sense left open?",
    "rule": ("Printed: आमान्वये च ऊर्ध्वम् अपि विरुद्धोपक्रमत्वात्: 'and in connection with āma, even afterwards, because of "
             "conflicting treatment' (one reading). -त्वात् gives a reason: because of being so."),
    "limits": ("Low confidence; the data calls the sense obscure and builds nothing firm on it. 'Even afterwards' (after three "
               "months?) is a guess; विरुद्धोपक्रम may be conflicting treatments or contrary treatment. No verb is printed. "
               "Questions stay on the words, splits and the ending -त्वात्."),
    "explain_hi": ("यह छोटी गद्य-पंक्ति कहती है: आम यानी कच्चे, अपक्व पदार्थ के अनुबन्ध में, आगे (बाद में) भी, विरुद्ध उपक्रम के कारण। "
                   "डेटा इसका अर्थ अस्पष्ट मानता है और इस पर कुछ पक्का नहीं बनाता; विश्वास निम्न है। "
                   "एक पाठ के अनुसार आम के लिए जो उपचार ठीक है, वह गर्भ के लिए उपयुक्त उपचार से टकराता है; दूसरे के अनुसार ‘विरुद्धोपक्रम’ = उलटा उपचार। "
                   "‘ऊर्ध्वमपि’ (बाद में भी) का अर्थ ‘तीन मास के बाद भी’ होना केवल अनुमान है। "
                   "पक्की बात इतनी है कि ‘-त्वात्’ कारण बताता है: ऐसा होने के कारण।"),
    "hook": "आमान्वये, बाद में भी, विरुद्ध उपक्रम के कारण: अर्थ अस्पष्ट (एक पाठ: उपचार टकराते हैं)।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 29, what does the ending -त्वात् of विरुद्धोपक्रमत्वात् express?",
            ("Because of being so", "-त्व (the state) + ablative -आत्: because of the state, a reason."),
            [("For the sake of it", "Purpose is -अर्थम्, not -त्वात्."),
             ("In spite of it all", "-त्वात् gives a reason, not a concession."),
             ("After having done it", "An absolutive (-त्वा, -य) means after having; -त्वात् is an ablative.")],
            "-त्वात् = because of being (so): it gives the reason.",
            "-त्व + -आत् (ablative) = because of the state."),
        order(1, "Put the words of unit 29 in the line's order.",
              ["आमान्वये", "च", "ऊर्ध्वम्", "अपि", "विरुद्धोपक्रमत्वात्"],
              "In connection with āma, and, afterwards, even, because of conflicting treatment.",
              "आमान्वये → च → ऊर्ध्वम् → अपि → विरुद्धोपक्रमत्वात्."),
        match(2, "Match each word of unit 29 to its gloss in the data.",
              [["आम", "raw, undigested material"], ["अन्वय", "connection, following"], ["ऊर्ध्वम्", "afterwards, above"],
               ["अपि", "even"], ["उपक्रम", "treatment"]],
              "The words are sure even though the sense of the whole is obscure.",
              "आम, अन्वय, ऊर्ध्वम्, अपि, उपक्रम.", role="extend",
              teaches="आमान्वये = आम + अन्वये (अ + अ → आ): in connection with āma."),
        mcq("discriminate", 3, "Which split of चोर्ध्वमपि is right?",
            ("च + ऊर्ध्वम् + अपि", "अ + ऊ → ओ; म् joins the following vowel: चोर्ध्वमपि."),
            [("चो + ऊर्ध्वम् + अपि", "चो is not a word; the particle is च."),
             ("च + ओर्ध्वम् + अपि", "ओर्ध्वम् is not a word, and अ + ओ would give औ."),
             ("च + ऊर्ध्वः + अपि", "ऊर्ध्वः + अपि would give ऊर्ध्वोऽपि, with ओऽ, not मपि.")],
            "च (and) + ऊर्ध्वम् (afterwards) + अपि (even).",
            "अ + ऊ → ओ; म् + vowel stays म्."),
        multi("apply", 4, "Which statements fit unit 29 by its data?",
              [("Its data calls the sense obscure", "Right: the notes say the sense is obscure and build nothing firm."),
               ("It names the conflicting treatments", "No treatment is named in unit 29."),
               ("It contains āma, raw undigested matter", "Right: आमान्वये, in connection with āma."),
               ("It states a firm month for ऊर्ध्वम्", "After three months is only a guess, marked with a question.")],
              [0, 2],
              "Obscure sense; the word āma is sure; no treatment and no firm time are given.",
              "आमान्वये च ऊर्ध्वम् अपि विरुद्धोपक्रमत्वात्."),
        mcq("transfer", 5, "By the rule of चोर्ध्वम् (च + ऊर्ध्वम्), how is जल + ऊर्मिः (a wave of water) written when joined?",
            ("जलोर्मिः", "अ + ऊ → ओ, as च + ऊर्ध्वम् → चोर्ध्वम्."),
            [("जलौर्मिः", "औ comes from अ + ओ or औ, not from अ + ऊ."),
             ("जलूर्मिः", "The अ does not simply drop before ऊ."),
             ("जलवूर्मिः", "व् comes from उ/ऊ before another vowel, not from अ.")],
            "जल + ऊर्मिः = जलोर्मिः, like च + ऊर्ध्वम् = चोर्ध्वम्.",
            "अ + ऊ → ओ.",
            teaches="A short अ followed by ऊ joins as ओ: च + ऊर्ध्वम् → चोर्ध्वम्."),
    ],
}

# ---------------------------------------------------------------- unit 30
AUTHORED["30"] = {
    "title": "तत्र रूक्षशीतानि प्रयुंजीत",
    "question": "By unit 30, what kind of (ones) should one apply in that case?",
    "rule": ("In that case (तत्र) one should apply (प्रयुञ्जीत, optative) dry (रूक्ष) and cool (शीत) (ones). "
             "रूक्षशीतानि is a dvandva of two qualities, neuter plural; the noun is not printed."),
    "limits": ("The nouns are unstated; the data writes '(ones)' and says the list comes in unit 32. Which case तत्र points "
               "to is not named inside this unit. No dose or time is given."),
    "explain_hi": ("यह गद्य-पंक्ति कहती है: उस स्थिति में (तत्र) रूक्ष और शीतल (द्रव्यों/उपायों) का प्रयोग करे। "
                   "‘रूक्षशीतानि’ द्वन्द्व है: रूक्ष (सूखा) और शीत (ठंडा), नपुंसकलिंग बहुवचन; संज्ञा छपी नहीं है, इसलिए डेटा ‘(ones)’ लिखता है। "
                   "सूची आगे इकाई ३२ में आती है। "
                   "‘प्रयुञ्जीत’ विधिलिङ् (आत्मनेपद) है: प्रयोग करे, करना चाहिए।"),
    "hook": "उस स्थिति में: रूक्ष और शीत।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 30, what kind of (ones) should one apply in that case?",
            ("Dry and cool ones", "रूक्षशीतानि: रूक्ष (dry) and शीत (cool)."),
            [("Hot and moist ones", "The unit says cool and dry, the opposite."),
             ("Heavy and warm ones", "Neither heavy nor warm is named in unit 30."),
             ("Sour and hot ones", "Neither sour nor hot is named in unit 30.")],
            "Dry and cool (ones) are applied.",
            "रूक्षशीतानि प्रयुञ्जीत."),
        order(1, "Put the words of unit 30 in the line's order.",
              ["तत्र", "रूक्षशीतानि", "प्रयुंजीत"],
              "In that case, dry and cool (ones), one should apply.",
              "तत्र → रूक्षशीतानि → प्रयुंजीत."),
        match(2, "Match each word of unit 30 to its meaning.",
              [["तत्र", "in that case"], ["रूक्ष", "dry"], ["शीत", "cool"], ["प्रयुञ्जीत", "one should apply"]],
              "Four words: the case, two qualities, and the verb.",
              "तत्र, रूक्ष, शीत, प्रयुञ्जीत.", role="extend",
              teaches="रूक्षशीतानि is a dvandva: रूक्ष and शीत, both qualities of the unstated (ones)."),
        mcq("discriminate", 3, "By its data, what form is प्रयुञ्जीत in unit 30?",
            ("Optative: one should apply", "The data: 3 sg. optative middle of प्र-√युज्: one should apply."),
            [("Past tense: one applied", "The data reads optative, not a past tense."),
             ("Future: one will apply", "The data reads optative, not a future."),
             ("Command: you, apply!", "It is third person optative, not a second-person imperative.")],
            "-ईत here is the optative middle ending: one should apply.",
            "प्रयुञ्जीत = 3 sg. optative middle: should apply."),
        mcq("apply", 4, "Someone renders unit 30 as: In that case one should apply dry and cool foods. What is wrong?",
            ("No noun is printed in the line", "The data: the nouns are unstated, so it writes (ones)."),
            [("रूक्ष means oily, not dry", "रूक्ष means dry; oily would be स्निग्ध."),
             ("शीत means hot, not cool", "शीत means cool; hot would be उष्ण."),
             ("तत्र means never, not in that case", "तत्र is glossed in that case; it is no negative.")],
            "Foods is added; the line names no noun.",
            "रूक्षशीतानि: the noun is not stated."),
        mcq("transfer", 5, "By the pattern of रूक्षशीतानि, what does a new example लघुशीतानि mean?",
            ("Light and cool ones", "A dvandva of two qualities, like रूक्ष + शीत: light and cool."),
            [("Light because they are cool", "A dvandva joins with and; it gives no reason."),
             ("The lightness of cool ones", "-आनि is a neuter plural of adjectives, not an abstract noun."),
             ("Cool, but not at all light", "Nothing is negated; both qualities hold.")],
            "लघु (light) + शीत (cool) = light and cool (ones).",
            "Quality + quality as a dvandva: X and Y (ones).",
            teaches="Two quality words joined as a dvandva in the neuter plural mean 'X and Y (ones)': रूक्षशीतानि = dry and cool (ones)."),
    ],
}

# ---------------------------------------------------------------- unit 31
AUTHORED["31"] = {
    "title": "तद्यथा",
    "question": "What does तद्यथा do in unit 31?",
    "rule": ("तद्यथा = तत् (that) + यथा (as, namely): 'that is as follows'. It introduces a list. त् before the voiced य "
             "becomes द्."),
    "limits": ("One word, prose. The list it introduces is not in this unit; the data says it comes in unit 32. "
               "No verb is printed."),
    "explain_hi": ("‘तद्यथा’ का अर्थ है: वह इस प्रकार है। "
                   "यह शब्द आगे आने वाली सूची का परिचय देता है; सूची इस इकाई में नहीं, आगे की इकाई में है। "
                   "इसमें तत् + यथा है: घोष ध्वनि य से पहले त् का द् हो जाता है।"),
    "hook": "तद्यथा = वह इस प्रकार है: अब सूची आएगी।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What does तद्यथा do in unit 31?",
            ("Introduces: that is as follows", "तत् (that) + यथा (as, namely): it opens a list."),
            [("Closes a list: thus it is ended", "Closing is done by इति; तद्यथा opens."),
             ("Gives a cause: because of it", "A cause would be तस्मात् or -त्वात्; यथा means as, namely."),
             ("Marks time: after that one", "After that would be ततः or तदनन्तरम्.")],
            "तद्यथा = that is as follows.",
            "तत् + यथा = that (is) as follows."),
        match(1, "Match each part of unit 31 to its meaning.",
              [["तत्", "that"], ["यथा", "as, namely"], ["तद्यथा", "that is as follows"]],
              "Two words make the phrase that is as follows.",
              "तत्, यथा, तद्यथा."),
        fill(2, "Complete the split: तद्यथा = तत् + ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("यथा", None, "yatha"),
             "तत् + यथा: the second word is यथा (as, namely).",
             "तद्यथा = तत् + यथा; त् before the voiced य becomes द्.",
             "तत् + यथा → तद्यथा."),
        mcq("discriminate", 3, "Which split of तद्यथा is right?",
            ("तत् + यथा", "त् before the voiced य becomes द्: तत् + यथा → तद्यथा."),
            [("तत् + अथा", "अथा is not a word, and त् + अ would give तदथा."),
             ("तद + यथा", "तद is not a word here, and it would give तदयथा."),
             ("तद्य + था", "तद्य and था are not the words; the words are तत् and यथा.")],
            "तत् (that) + यथा (as, namely).",
            "त् + voiced sound → द्."),
        mcq("apply", 4, "Which rule makes तत् + यथा into तद्यथा?",
            ("त् before a voiced sound → द्", "य is voiced, so त् becomes द्."),
            [("त् before य becomes च्", "च् would come before श, च or छ, not before य."),
             ("त् is dropped before य", "The त् stays as द्; it is not dropped."),
             ("त् doubles before य", "No doubling: त् simply becomes द्.")],
            "A final त् before a voiced sound becomes द्.",
            "त् + voiced sound → द्."),
        mcq("transfer", 5, "By the rule of तद्यथा, how is एतत् + युद्धम् (this battle) written when joined?",
            ("एतद्युद्धम्", "त् before the voiced य becomes द्, as तत् + यथा."),
            [("एतत्युद्धम्", "Before a voiced sound the त् does not stay."),
             ("एतन्युद्धम्", "त् becomes न् only before a nasal; य is not a nasal."),
             ("एतच्युद्धम्", "च् comes before श, च or छ, not before य.")],
            "एतत् + युद्धम् = एतद्युद्धम्, like तत् + यथा = तद्यथा.",
            "त् + voiced sound → द्.",
            teaches="A final त् before a voiced sound becomes द्: तत् + यथा → तद्यथा."),
    ],
}

# ---------------------------------------------------------------- unit 32
AUTHORED["32"] = {
    "title": "प्रागुपवासं तथा ... स्निग्धशीतानि पूर्ववत्",
    "question": "By unit 32, what is given first, what else is given, and what once āma has been overcome?",
    "rule": ("First fasting (प्राक् उपवासम्); likewise (तथा) the drink of one decoction (printed काथ, read क्वाथ) of a drug list; and as food: thin gruel (peyā) of "
             "grass-grains, śāli and ṣaṣṭika, with soups of mudga and the like; but when āma is overcome, unctuous and cool "
             "(ones) as before."),
    "limits": ("Medium confidence. घन (mustā) and कट्वंग are conjectural readings, and काथ is read as क्वाथ (decoction): no "
               "question rests on them. The e in षष्टिकेपेयाम् is a possible print slip. tṛṇadhānya grains are not listed. "
               "No amount is given; as before is not spelt out here."),
    "explain_hi": ("यह लम्बी गद्य-पंक्ति कहती है: पहले उपवास; तथा (साथ ही) दुरालभा, अमृता, उशीर, पर्पटक आदि द्रव्यों के एक काढ़े का पान; "
                   "और भोजन के रूप में तृणधान्य, शालि और साठी चावल की पेया (पतली लपसी), मूँग आदि के यूष के साथ। "
                   "जब आम जीत लिया जाए (जिते त्वामे), तब पहले की तरह स्निग्ध और शीतल (द्रव्य)। "
                   "पहचानें डेटा के लेबल के साथ: अमृता (गिलोय), उशीर (खस), अतिविषा (अतीस), धान्यक (धनिया) मानक; पर्पटक सम्भावित; दुरालभा विवादित। "
                   "‘घन’ और ‘कट्वंग’ अनुमानित पाठ हैं, और छपा ‘काथ’ ‘क्वाथ’ (काढ़ा) पढ़ा गया है; इन पर कोई प्रश्न नहीं।"),
    "hook": "पहले उपवास; साथ में काढ़ा और पेया-यूष; आम जीते तो स्निग्ध-शीत।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 32, what is done first?",
            ("Fasting (उपवास)", "प्रागुपवासम्: first, fasting."),
            [("Smoke of herbs (धूम)", "No smoke is named in unit 32."),
             ("Oil rubbing (अभ्यङ्ग)", "No oil rubbing is named in unit 32."),
             ("Day sleep (दिवास्वप्न)", "No sleep is named in unit 32.")],
            "Fasting comes first: प्राक् = first.",
            "प्राक् उपवासम्."),
        order(1, "Put these phrases of unit 32 in the line's order.",
              ["प्रागुपवासं", "दुरालभाऽमृतोशीर...काथपानं", "तृणधान्यशालिषष्टिकेपेयामशनं च", "मुद्गादियूषैः",
               "जिते त्वामे स्निग्धशीतानि पूर्ववत्"],
              "First fasting; the drink of the drug list; the gruel as food; with soups of mudga and the like; when āma is "
              "overcome, unctuous and cool as before.",
              "उपवास → पान → पेया-अशन → मुद्गादि-यूष → जिते आमे स्निग्धशीतानि."),
        match(2, "Match each drug of unit 32 to the identification its data gives.",
              [["अमृता", "guḍūcī, Tinospora cordifolia (standard)"], ["उशीर", "vetiver root (standard)"],
               ["अतिविषा", "Aconitum heterophyllum (standard)"], ["धान्यक", "coriander (standard)"],
               ["पर्पटक", "Fumaria parviflora (probable)"], ["दुरालभा", "Alhagi or Fagonia (disputed)"]],
              "Six drugs of the list, each with the label its data gives.",
              "अमृता, उशीर, अतिविषा, धान्यक: standard; पर्पटक: probable; दुरालभा: disputed.", role="extend",
              teaches="Drug names stand together in one compound that ends in -पानम् (drinking)."),
        mcq("discriminate", 3, "Which split of त्वामे in जिते त्वामे is right?",
            ("तु + आमे", "उ before a different vowel becomes व्: तु + आमे → त्वामे."),
            [("तु + अमे", "उ + अ would give त्वमे, with a short अ."),
             ("ते + आमे", "ए + आ would give तयामे or त आमे, not त्वामे."),
             ("त्वा + मे", "The words are तु (but) and आमे (when āma), not त्वा and मे.")],
            "तु (but) + आमे (when āma): उ + आ → वा.",
            "उ + a different vowel → व् + that vowel."),
        mcq("apply", 4, "By unit 32, when are unctuous and cool (ones) given, as before?",
            ("When āma is overcome", "जिते तु आमे: but when āma has been overcome."),
            [("Before the fast begins", "The fast comes first; unctuous and cool come last."),
             ("With the first decoction", "The decoction is a separate measure; unctuous and cool come once āma is overcome."),
             ("Only on the first day", "No day is named; the condition is that āma is overcome.")],
            "Unctuous and cool (ones) follow once āma has been overcome.",
            "जिते त्वामे स्निग्धशीतानि पूर्ववत्."),
        mcq("transfer", 5, "By the rule of त्वामे (तु + आमे), how is मधु + आनय (bring honey) written when joined?",
            ("मध्वानय", "उ before a different vowel becomes व्: मधु + आनय → मध्वानय."),
            [("मधुआनय", "उ and आ are not left side by side in sandhi."),
             ("मधोनय", "उ + आ does not give ओ."),
             ("मधूनय", "ऊ comes from उ + उ, not from उ + आ.")],
            "मधु + आनय = मध्वानय, like तु + आमे = त्वामे.",
            "उ + आ → वा.",
            teaches="A final उ before आ becomes व्: तु + आमे → त्वामे."),
    ],
}

# ---------------------------------------------------------------- unit 33
AUTHORED["33"] = {
    "title": "आमगर्भे तु पतिते मद्यानामन्यतमं",
    "question": "By unit 33, what is she made to drink when the āma-garbha has fallen, and for what two purposes?",
    "rule": ("When the āma-garbha (unripe embryo; probably an early miscarriage) has fallen, one should make her drink any "
             "one of the madyas, according to capacity, for cleansing the garbha-koṣṭha (probably the womb) and for "
             "forgetting the pain (arti)."),
    "limits": ("āma-garbha as early pregnancy loss and garbha-koṣṭha as the womb are probable. Whose capacity (drinker's or "
               "physician's) is not decided: no question on it. No madya is named and no amount is given."),
    "explain_hi": ("जब आमगर्भ यानी कच्चा गर्भ (सम्भवतः आरम्भिक गर्भपात) गिर जाए, तब सामर्थ्य के अनुसार मद्यों में से कोई एक (अन्यतम) पिलाए। "
                   "दो प्रयोजन बताए गए हैं: गर्भकोष्ठ (सम्भवतः गर्भाशय) की शुद्धि, और अर्ति यानी पीड़ा को भुलाना। "
                   "‘सामर्थ्यतः’ पीने वाली के सामर्थ्य से है या वैद्य के, यह तय नहीं। "
                   "किसी मद्य का नाम या मात्रा नहीं दी गई। "
                   "‘-अर्थम्’ समास के अन्त में ‘के लिए’ बताता है।"),
    "hook": "कच्चा गर्भ गिरा: कोई एक मद्य, शुद्धि और पीड़ा-विस्मरण के लिए।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 33, what is she made to drink when the āma-garbha has fallen?",
            ("Any one of the madyas", "मद्यानामन्यतमं पाययेत्: any one of the madyas."),
            [("Fresh sugarcane juice", "Sugarcane juice is not named in unit 33."),
             ("Cold water with sugar", "Cold water with sugar is not named in unit 33."),
             ("Fresh, thin buttermilk", "Buttermilk is not named in unit 33.")],
            "Any one of the intoxicating drinks (madya), according to capacity.",
            "मद्यानाम् अन्यतमं पाययेत्."),
        order(1, "Put the phrases of unit 33 in the line's order.",
              ["आमगर्भे तु पतिते", "मद्यानामन्यतमं", "सामर्थ्यतः", "पाययेत्", "गर्भकोष्ठविशुद्ध्यर्थम्",
               "अर्तिविस्मरणार्थं च"],
              "When the āma-garbha has fallen, any one of the madyas, according to capacity, one should make her drink, "
              "for cleansing the garbha-koṣṭha and for forgetting the pain.",
              "आमगर्भे तु पतिते → मद्यानामन्यतमं → सामर्थ्यतः → पाययेत् → ...विशुद्ध्यर्थम् → ...विस्मरणार्थं च."),
        match(2, "Match each word of unit 33 to its meaning.",
              [["आमगर्भ", "unripe embryo"], ["पतित", "fallen"], ["अन्यतम", "any one"],
               ["सामर्थ्यतः", "according to capacity"], ["अर्ति", "pain, distress"]],
              "The event, the drink (any one), the measure, and the pain it helps to forget.",
              "आमगर्भ, पतित, अन्यतम, सामर्थ्यतः, अर्ति.", role="extend",
              teaches="अन्यतम = any one (of several): मद्यानाम् अन्यतमम् = any one of the madyas."),
        multi("discriminate", 3, "Which purposes of the drink does unit 33 name?",
              [("To make the embryo grow", "The embryo has fallen; growth is not a purpose here."),
               ("To cleanse the garbha-koṣṭha", "Right: गर्भकोष्ठविशुद्ध्यर्थम्."),
               ("To stop all further bleeding", "Stopping bleeding is not named in unit 33."),
               ("To forget the pain (arti)", "Right: अर्तिविस्मरणार्थम्.")],
              [1, 3],
              "Two purposes: cleansing the garbha-koṣṭha and forgetting the pain.",
              "...विशुद्ध्यर्थम् अर्तिविस्मरणार्थं च."),
        mcq("apply", 4, "By the data of unit 33, what is the garbha-koṣṭha?",
            ("Probably the womb", "garbha-koṣṭha = the storehouse of the embryo, probably the womb."),
            [("Probably the mother's chest", "The data reads the embryo's storehouse, probably the womb."),
             ("Probably the mother's bladder", "The bladder is not how the data reads garbha-koṣṭha."),
             ("Probably the drinker's mouth", "The mouth is not the storehouse of the embryo.")],
            "koṣṭha = storehouse; garbha-koṣṭha = probably the womb.",
            "गर्भकोष्ठ = probably the womb."),
        mcq("transfer", 5, "By the pattern of अर्तिविस्मरणार्थम्, what does a new example रोगनाशार्थम् mean?",
            ("For destroying disease", "-अर्थम् at the end of a compound = for the purpose of."),
            [("Because disease is gone", "Because of would be an ablative such as -त्वात्."),
             ("The destroyer of disease", "-अर्थम् gives a purpose, not an agent."),
             ("After disease is gone", "After having would be an absolutive, not -अर्थम्.")],
            "रोग (disease) + नाश (destruction) + अर्थम् (for) = for destroying disease.",
            "X-अर्थम् = for the purpose of X.",
            teaches="-अर्थम् at the end of a compound means for the purpose of: अर्तिविस्मरणार्थम् = for forgetting the pain."),
    ],
}

# ---------------------------------------------------------------- unit 34
AUTHORED["34"] = {
    "title": "अमद्यपां ... यवागूभिरुपाचरेत्",
    "question": "By unit 34, how is a non-drinker of madya treated, and for how long?",
    "rule": ("A non-drinker of madya (अमद्यपा) is treated with thick gruels (यवागू) of uddālaka and the like, joined with "
             "pācanīya (digestion-promoting) substances, without sneha and salt, with sesame, for as many days as there are "
             "months."),
    "limits": ("Uddālaka is disputed (probably a kind of kodo millet). That the months are those of the pregnancy is "
               "understood, not printed: no question rests on it. No pācanīya drug and no amount are named. The closing इति "
               "is not translated."),
    "explain_hi": ("जो मद्य नहीं पीती (अमद्यपा), उसका उपचार उद्दालक आदि की यवागू यानी गाढ़ी लपसियों से करे। "
                   "ये यवागू पाचनीय द्रव्यों से युक्त, स्नेह (तेल-वसा) और लवण (छपा ‘लोण’) से रहित, और तिल सहित हों। "
                   "अवधि: जितने मास, उतने दिन। "
                   "मास गर्भ के हैं, यह समझा जाता है, छपा नहीं। "
                   "उद्दालक की पहचान विवादित है (सम्भवतः कोदो की कोई किस्म)।"),
    "hook": "मद्य नहीं पीती: तिल वाली, बिना स्नेह-नमक की यवागू, जितने मास उतने दिन।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 34, with what is a non-drinker of madya treated?",
            ("Thick gruels (यवागू)", "...यवागूभिरुपाचरेत्: with yavāgūs, thick gruels."),
            [("Cold water baths (स्नान)", "No bath is named in unit 34."),
             ("Fruit juice (फलरस)", "No fruit juice is named in unit 34."),
             ("Milk drinks (क्षीर)", "No milk is named in unit 34.")],
            "She is treated with thick gruels of uddālaka and the like.",
            "उद्दालकादियवागूभिः उपाचरेत्."),
        order(1, "Put the words of unit 34 in the line's order.",
              ["अमद्यपां", "पाचनीयद्रव्योपहिताभिः", "स्नेहलोणवर्जाभिः", "सतिलाभिः", "उद्दालकादियवागूभिः",
               "उपाचरेत्"],
              "The non-drinker, with gruels joined with digestives, without sneha and salt, with sesame, of uddālaka and the "
              "like, one should treat.",
              "अमद्यपां → पाचनीय... → स्नेहलोणवर्जाभिः → सतिलाभिः → उद्दालकादियवागूभिः → उपाचरेत्."),
        match(2, "Match each word of unit 34 to its meaning.",
              [["अमद्यपा", "a non-drinker of madya"], ["पाचनीय", "digestion-promoting"], ["वर्ज", "without"],
               ["सतिल", "with sesame"], ["यवागू", "thick gruel"]],
              "Who is treated, and what the gruel is like.",
              "अमद्यपा, पाचनीय, वर्ज, सतिल, यवागू.", role="extend",
              teaches="-वर्ज at the end of a compound = without: स्नेहलोणवर्ज = without sneha and salt."),
        mcq("discriminate", 3, "By unit 34, what is kept out of the gruels?",
            ("Sneha and salt", "स्नेहलोणवर्जाभिः: without sneha and salt."),
            [("Sesame and uddālaka", "Sesame is added (सतिलाभिः); uddālaka is the grain of the gruel."),
             ("Digestive substances", "They are added: पाचनीयद्रव्योपहिताभिः."),
             ("All grains and sesame", "The gruel is of uddālaka and the like, with sesame.")],
            "Fat and salt are left out; digestives and sesame are added.",
            "स्नेहलोणवर्जाभिः सतिलाभिः."),
        mcq("apply", 4, "By unit 34, for how long are the gruels given?",
            ("As many days as months", "यावन्तो मासास्तावन्त्यहानि: as many days as there are months."),
            [("As many months as days", "This reverses the line: days are counted by months."),
             ("Seven days in all cases", "No fixed number of days is printed."),
             ("Until bleeding has stopped", "No such end point is named in unit 34.")],
            "The count of days equals the count of months.",
            "यावन्तो मासाः तावन्त्यहानि."),
        mcq("transfer", 5, "By the rule of मासास्तावन्ति (मासाः + तावन्ति), how is बालाः + तिष्ठन्ति (the boys stand) written?",
            ("बालास्तिष्ठन्ति", "Visarga before त becomes स्, as मासाः + तावन्ति."),
            [("बाला तिष्ठन्ति", "आः drops its visarga before a voiced sound; त is unvoiced."),
             ("बालाश्तिष्ठन्ति", "Before त the visarga becomes स्, not श्."),
             ("बालोस्तिष्ठन्ति", "The आ does not change to ओ.")],
            "बालाः + तिष्ठन्ति = बालास्तिष्ठन्ति, like मासाः + तावन्ति = मासास्तावन्ति.",
            "Visarga before त → स्.",
            teaches="A visarga before त becomes स्: मासाः + तावन्ति → मासास्तावन्ति."),
    ],
}

# ---------------------------------------------------------------- unit 35
AUTHORED["35"] = {
    "title": "ततः प्रीणनैर्बलानुरक्षिभिरस्नेहैराहारैः",
    "question": "By unit 35, with what foods is she then treated, and until when?",
    "rule": ("Then (ततः), with foods that are refreshing (प्रीणन), strength-protecting (बलानुरक्षिन्) and without sneha "
             "(अस्नेह), until (आ + ablative) the cleansing of doṣa, dhātu and kleda."),
    "limits": ("No verb is printed; the data carries उपाचरेत् from unit 34. दोषधातुक्लेद may also mean 'the kleda of doṣa "
               "and dhātu': no question rests on that grouping. No food is named."),
    "explain_hi": ("फिर (ततः) ऐसे आहारों से उपचार हो जो प्रीणन (तृप्त करने वाले), बल की रक्षा करने वाले और स्नेह-रहित (अस्नेह) हों। "
                   "यह तब तक चले जब तक दोष, धातु और क्लेद (गीलापन, आर्द्र मल) की शुद्धि न हो जाए; ‘आ’ + पंचमी = तक। "
                   "क्रिया छपी नहीं है; डेटा पिछली इकाई का ‘उपाचरेत्’ लेता है। "
                   "‘दोषधातुक्लेद’ को ‘दोष और धातु का क्लेद’ भी पढ़ सकते हैं; इस पर प्रश्न नहीं।"),
    "hook": "फिर: तृप्तिकर, बलरक्षक, बिना स्नेह का आहार, शुद्धि होने तक।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 35, what kind of foods are given then?",
            ("Refreshing, strength-guarding, no sneha", "प्रीणनैर्बलानुरक्षिभिरस्नेहैराहारैः."),
            [("Sour, salty and heavy, in large measure", "None of these qualities is named in unit 35."),
             ("Raw, bitter and scanty, once a day", "None of these qualities is named in unit 35."),
             ("Fermented, sour and very rich", "None of these qualities is named in unit 35.")],
            "Foods that refresh, guard strength and are without sneha.",
            "प्रीणन, बलानुरक्षिन्, अस्नेह आहार."),
        order(1, "Put the words of unit 35 in the line's order.",
              ["ततः", "प्रीणनैः", "बलानुरक्षिभिः", "अस्नेहैः", "आहारैः", "आ दोषधातुक्लेदशुद्धेः"],
              "Then, with refreshing, strength-protecting, non-unctuous foods, until the cleansing of doṣa, dhātu and kleda.",
              "ततः → प्रीणनैः → बलानुरक्षिभिः → अस्नेहैः → आहारैः → आ ...शुद्धेः."),
        match(2, "Match each word of unit 35 to its meaning.",
              [["प्रीणन", "refreshing, gratifying"], ["बलानुरक्षिन्", "protecting strength"], ["अस्नेह", "without sneha"],
               ["क्लेद", "moisture, wet matter"], ["शुद्धि", "cleansing"]],
              "Three qualities of the foods and the end point (cleansing).",
              "प्रीणन, बलानुरक्षिन्, अस्नेह, क्लेद, शुद्धि.", role="extend",
              teaches="अ- before a consonant negates: स्नेह → अस्नेह, without sneha."),
        mcq("discriminate", 3, "In आ दोषधातुक्लेदशुद्धेः, what does आ with the ablative mean here?",
            ("Until", "The data: ā + ablative = until (the cleansing)."),
            [("Without", "Without would be a word like विना or -वर्ज."),
             ("Because of", "The data reads ā + ablative as until, not as a cause."),
             ("Together with", "Together with would be सह or स-.")],
            "आ + ablative = until: until the cleansing of doṣa, dhātu and kleda.",
            "आ + ablative = until."),
        mcq("apply", 4, "A cook adds ghee to these foods. Does that fit unit 35?",
            ("No: the foods are without sneha", "अस्नेहैः आहारैः: the foods are without sneha (oil, fat)."),
            [("Yes: ghee will guard her strength", "The foods must guard strength, but they are also asneha."),
             ("Yes: any refreshing food will do", "Refreshing is not enough; the foods are without sneha."),
             ("No: the foods must all be raw", "Raw is not named; the reason is that they are without sneha.")],
            "Ghee is a sneha, so it does not fit foods that are asneha.",
            "अस्नेह = without sneha."),
        mcq("transfer", 5, "By the rule of अस्नेहैराहारैः (अस्नेहैः + आहारैः), how is पुष्पैः + अर्चति (worships with flowers) written?",
            ("पुष्पैरर्चति", "After ऐ the visarga becomes र् before a voiced sound (here a vowel)."),
            [("पुष्पैः अर्चति", "Before a vowel the visarga after ऐ does not stay."),
             ("पुष्पा अर्चति", "ऐ does not change to आ."),
             ("पुष्पैसर्चति", "स् comes before त or थ, not before a vowel.")],
            "पुष्पैः + अर्चति = पुष्पैरर्चति, like अस्नेहैः + आहारैः = अस्नेहैराहारैः.",
            "A vowel other than अ/आ + ः, before a voiced sound → र्.",
            teaches="After a vowel other than अ or आ, the visarga becomes र् before a voiced sound: अस्नेहैः + आहारैः → अस्नेहैराहारैः."),
    ],
}

# ---------------------------------------------------------------- unit 36
AUTHORED["36"] = {
    "title": "आमगर्भशेषेण हि पुनः पुनः शूलम्",
    "question": "By unit 36, why must no remnant of the āma-garbha be left, and how is she treated?",
    "rule": ("For (हि), with a remnant (शेष) of the āma-garbha, pain (शूल) would cling on again and again. Therefore (तस्मात्) "
             "one should treat with sharp (तीक्ष्ण) (ones), leaving no remnant (अनवशेषयन्)."),
    "limits": ("Two printed lines joined. The sharp measures are not named; the data writes '(ones)'. अनुषज्येत is read as "
               "'would persist, recur'. The print has 'cupā-' where ca + upācaret gives copācaret (text flag)."),
    "explain_hi": ("पहली पंक्ति कारण देती है: आमगर्भ का शेष रह जाए तो शूल यानी पीड़ा बार-बार लगी रहेगी (‘हि’ = क्योंकि)। "
                   "दूसरी पंक्ति निष्कर्ष देती है: इसलिए (तस्मात्) तीक्ष्ण (उपायों) से, कुछ भी शेष न छोड़ते हुए, उपचार करे। "
                   "तीक्ष्ण उपाय कौन-से हैं, यह नहीं बताया गया। "
                   "‘अनवशेषयन्’ णिजन्त वर्तमान कृदन्त है: कुछ भी शेष न रहने देते हुए। "
                   "छपे ‘...यञ्चुपाचरेत्’ में ‘चु’ है, जबकि च + उपाचरेत् से ‘चोपाचरेत्’ बनता है (पाठ-चिह्न)।"),
    "hook": "शेष बचा तो बार-बार शूल; इसलिए तीक्ष्ण से, कुछ न बचे।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 36, what follows if a remnant of the āma-garbha stays?",
            ("Pain again and again", "पुनः पुनः शूलमनुषज्येत: pain would cling on again and again."),
            [("Fever every night", "No fever is named in unit 36."),
             ("Swollen hands, feet", "No swelling is named in unit 36."),
             ("A loss of all hunger", "No loss of hunger is named in unit 36.")],
            "A remnant brings pain again and again.",
            "आमगर्भशेषेण ... पुनः पुनः शूलम्."),
        order(1, "Put the parts of unit 36 in the line's order.",
              ["आमगर्भशेषेण हि", "पुनः पुनः", "शूलमनुषज्येत", "तस्मात्", "तीक्ष्णैः", "अनवशेषयन् उपाचरेत्"],
              "Because of a remnant, again and again, pain would cling on; therefore, with sharp ones, leaving nothing, one "
              "should treat.",
              "शेष → पुनः पुनः → शूल → तस्मात् → तीक्ष्णैः → अनवशेषयन् उपाचरेत्."),
        match(2, "Match each word of unit 36 to its meaning.",
              [["शेष", "remnant"], ["पुनः पुनः", "again and again"], ["शूल", "pain"], ["तीक्ष्ण", "sharp, strong"],
               ["अनवशेषयन्", "leaving no remainder"]],
              "The cause (remnant), its effect (pain again and again), and the remedy.",
              "शेष, पुनः पुनः, शूल, तीक्ष्ण, अनवशेषयन्.", role="extend",
              teaches="अनवशेषयन् = अन् (not) + अवशेषयन् (making remain): making nothing remain."),
        mcq("discriminate", 3, "What jobs do हि and तस्मात् do in unit 36?",
            ("हि gives the cause; तस्मात् the result", "हि = for, because; तस्मात् = therefore."),
            [("Both mark time: then, and then", "Neither is a time word here; they give cause and result."),
             ("हि negates; तस्मात् names a place", "हि is not a negative, and तस्मात् is therefore."),
             ("Both only add emphasis here", "The data glosses हि as for, because, and तस्मात् as therefore.")],
            "Cause (हि) in the first line, conclusion (तस्मात्) in the second.",
            "हि = because; तस्मात् = therefore."),
        mcq("apply", 4, "By unit 36, how should one treat, given the risk of a remnant?",
            ("With sharp ones, leaving nothing", "तीक्ष्णैः अनवशेषयन् उपाचरेत्."),
            [("With mild ones, little by little", "The unit says sharp (तीक्ष्ण), not mild."),
             ("With cooling ones, only once", "The unit says sharp ones, leaving no remnant."),
             ("Not at all: wait till it passes", "The unit says one should treat (उपाचरेत्).")],
            "Sharp measures, so that no remnant is left.",
            "तीक्ष्णैः अनवशेषयन् उपाचरेत्."),
        mcq("transfer", 5, "By the pattern of अनवशेषयन् (अन् + अवशेषयन्), how is the negative of उचित (proper) made?",
            ("अनुचित", "Before a vowel the negative is अन्-: अन् + उचित → अनुचित."),
            [("अउचित", "Before a vowel the negative is अन्-, not अ-."),
             ("नउचित", "The negative prefix is अ-/अन्-, not न-."),
             ("अवुचित", "There is no व् in the negative prefix.")],
            "अन् + उचित = अनुचित, like अन् + अवशेषयन् = अनवशेषयन्.",
            "Negative prefix: अ- before a consonant, अन्- before a vowel.",
            teaches="The negative prefix is अन्- before a vowel: अन् + अवशेषयन् → अनवशेषयन्."),
    ],
}

# ---------------------------------------------------------------- unit 37
AUTHORED["37"] = {
    "title": "ततः परं स्नेहपानैर्बस्तिभिराहारैश्च",
    "question": "By unit 37, with which three means is she treated after that, and with what qualities?",
    "rule": ("After that (ततः परम्): with drinks of sneha, bastis (enemas) and foods that are dīpanīya, pācanīya, jīvanīya, "
             "bṛṃhaṇīya, sweet (madhura) and Vāta-removing (वातहर)."),
    "limits": ("The six qualities may qualify only the foods (the data's reading) or all three means: no question on that. "
               "No drug or recipe is named. The verb is carried from before; the closing इति is not translated."),
    "explain_hi": ("इसके बाद (ततः परम्) तीन साधनों से उपचार: स्नेह-पान, बस्ति (एनिमा) और आहार। "
                   "गुण छह शब्दों में: दीपनीय (अग्नि जगाने वाले), पाचनीय (पाचक), जीवनीय (जीवन बढ़ाने वाले), बृंहणीय (पुष्टिकर), मधुर और वातहर। "
                   "डेटा ये गुण पास वाले शब्द ‘आहारैः’ से जोड़ता है, पर ये तीनों से भी जुड़ सकते हैं; इस पर प्रश्न नहीं। "
                   "कोई द्रव्य या विधि नहीं बताई गई; क्रिया पीछे से आती है।"),
    "hook": "फिर स्नेह, बस्ति, आहार: दीपन-पाचन-जीवन-बृंहण, मधुर, वातहर।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 37, which three means are named after that?",
            ("Sneha drinks, bastis, foods", "स्नेहपानैर्बस्तिभिराहारैश्च."),
            [("Nasal drops, smoke, baths", "None of these is named in unit 37."),
             ("Plasters, oil, cold packs", "None of these is named in unit 37."),
             ("Wine, sleep and long daily walks", "None of these is named in unit 37.")],
            "Drinks of sneha, bastis (enemas) and foods.",
            "स्नेहपानैः बस्तिभिः आहारैः च."),
        order(1, "Put the six qualities of unit 37 in the line's order.",
              ["दीपनीय", "पाचनीय", "जीवनीय", "बृंहणीय", "मधुर", "वातहर"],
              "Kindling, digestive, life-promoting, nourishing, sweet, Vāta-removing.",
              "दीपनीय → पाचनीय → जीवनीय → बृंहणीय → मधुर → वातहर."),
        match(2, "Match each quality of unit 37 to its meaning.",
              [["दीपनीय", "kindling the digestive fire"], ["पाचनीय", "promoting digestion"],
               ["जीवनीय", "life-promoting"], ["बृंहणीय", "nourishing, bulk-promoting"], ["वातहर", "removing Vāta"]],
              "Five of the six qualities; the sixth is madhura, sweet.",
              "दीपनीय, पाचनीय, जीवनीय, बृंहणीय, वातहर.", role="extend",
              teaches="-नीय words name what a thing does: दीपनीय = kindling, बृंहणीय = nourishing."),
        mcq("discriminate", 3, "How is आहारैः + च written, as in unit 37?",
            ("आहारैश्च", "The visarga becomes श् before च."),
            [("आहारैर्च", "र् comes before a voiced sound; च is unvoiced."),
             ("आहारैस्च", "स् comes before त or थ, not before च."),
             ("आहारै च", "The visarga is not simply dropped before च.")],
            "आहारैः + च = आहारैश्च.",
            "Visarga before च → श्."),
        multi("apply", 4, "Which qualities does the last compound of unit 37 name?",
              [("Sweet (madhura)", "Right: मधुर is the fifth quality."),
               ("Sour (amla)", "Sour is not named in unit 37."),
               ("Light (laghu)", "Light is not named in unit 37."),
               ("Vāta-removing (vātahara)", "Right: वातहर is the sixth quality.")],
              [0, 3],
              "Sweet and Vāta-removing are among the six; sour and light are not.",
              "दीपनीय, पाचनीय, जीवनीय, बृंहणीय, मधुर, वातहर."),
        mcq("transfer", 5, "By the pattern of वातहर, what does a new example श्रमहर mean?",
            ("Removing fatigue", "-हर at the end = removing: श्रम (fatigue) + हर."),
            [("Caused by fatigue", "-हर means removing, not caused by (-ज)."),
             ("Full of fatigue", "-हर means removing, not full of (-मय)."),
             ("Fatigue's own cause", "-हर names what takes away, not a cause.")],
            "श्रम + हर = removing fatigue, like वात + हर = removing Vāta.",
            "X-हर = removing X.",
            teaches="-हर at the end of a compound means removing: वातहर = removing Vāta."),
    ],
}

# ---------------------------------------------------------------- unit 38
AUTHORED["38"] = {
    "title": "यस्याः पुष्पमर्हति जातसारे गर्भे",
    "question": "By unit 38, what may appear when the fetus has acquired its sāra, and through what?",
    "rule": ("The fetus having acquired its sāra (जातसारे गर्भे), through not avoiding what is to be avoided "
             "(वर्ज्यानाम् अवर्जनात्) there may be the sight of puṣpa (bleeding), or some other flow from the yoni."),
    "limits": ("The sense of पुष्पमर्हति is not firm (puṣpa is due, or who is fit for puṣpa): no question on it. puṣpa = "
               "probably menstrual-type bleeding. The things to be avoided are not listed here. The sentence appears to run on "
               "(यस्याः here, तस्याः in unit 39)."),
    "explain_hi": ("यह गद्य-पंक्ति नए विषय (उपविष्टक आदि) की भूमिका है। "
                   "गर्भ जातसार हो चुका हो, यानी उसमें सार (दृढ़ता) बन गया हो, और त्याज्य बातों का त्याग न करने से (वर्ज्यानामवर्जनात्) "
                   "पुष्प यानी सम्भवतः रज जैसा स्राव दिख सकता है, या योनि से कोई और स्राव हो सकता है। "
                   "‘पुष्पमर्हति’ का अर्थ पक्का नहीं (पुष्प उचित हो, या जो पुष्प के योग्य हो); इस पर प्रश्न नहीं। "
                   "वाक्य आगे चलता है: यहाँ ‘यस्याः’, अगली इकाई में ‘तस्याः’।"),
    "hook": "सार बन चुका, परहेज़ न किया: पुष्प या दूसरा योनि-स्राव।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 38, through what may the bleeding appear?",
            ("Not avoiding what is to be avoided", "वर्ज्यानामवर्जनात्: from not avoiding the things to be avoided."),
            [("Too much fasting and dry food here", "Fasting and dry food are not named in unit 38."),
             ("A fall or a blow on the belly", "A fall or a blow is not named in unit 38."),
             ("The fetus having no sāra at all", "The unit says the fetus has acquired its sāra (जातसारे).")],
            "Non-avoidance of what is to be avoided.",
            "वर्ज्यानाम् अवर्जनात् पुष्पदर्शनं स्यात्."),
        order(1, "Put the parts of unit 38 in the line's order.",
              ["यस्याः पुष्पमर्हति", "जातसारे गर्भे", "वर्ज्यानामवर्जनात्", "पुष्पदर्शनं स्यात्", "अन्यद्वा योनिस्रवणं"],
              "Of her for whom puṣpa is due, the fetus having its sāra, through non-avoidance, the sight of puṣpa may be, or "
              "another flow from the yoni.",
              "यस्याः ... → जातसारे गर्भे → वर्ज्यानामवर्जनात् → पुष्पदर्शनं स्यात् → अन्यद्वा योनिस्रवणं."),
        match(2, "Match each word of unit 38 to its meaning.",
              [["जातसार", "whose sāra has arisen"], ["वर्ज्य", "to be avoided"], ["अवर्जन", "non-avoidance"],
               ["अन्यत्", "other"], ["योनिस्रवण", "flow from the yoni"]],
              "The state of the fetus, the cause and the two possible signs.",
              "जातसार, वर्ज्य, अवर्जन, अन्यत्, योनिस्रवण.", role="extend",
              teaches="वर्ज्य = to be avoided (gerundive); अ-वर्जन = not avoiding."),
        mcq("discriminate", 3, "What does जातसारे गर्भे say about the fetus?",
            ("Its sāra has arisen", "जात-सार: one whose sāra (essence, firmness) has arisen."),
            [("It is already born", "जात here qualifies सार (arisen), not the birth of the fetus."),
             ("It has no sāra yet", "That would be असंजातसार; जातसार is the opposite."),
             ("It has died within", "Nothing about death is said in unit 38.")],
            "जातसारे गर्भे = the fetus having acquired its sāra.",
            "जातसार = whose sāra has arisen (bahuvrīhi)."),
        mcq("apply", 4, "Her fetus is jātasāra, but she keeps doing what she was told to avoid. What may follow, by unit 38?",
            ("Sight of puṣpa, or another flow", "पुष्पदर्शनं स्यादन्यद्वा योनिस्रवणम्."),
            [("A belly that grows too fast", "Fast growth is not named in unit 38."),
             ("Milk coming in far too early", "Early milk is not named in unit 38."),
             ("Swelling of the hands and feet", "Swelling is not named in unit 38.")],
            "Bleeding (puṣpa) or some other flow from the yoni may appear.",
            "पुष्पदर्शनम् स्यात् अन्यत् वा योनिस्रवणम्."),
        mcq("transfer", 5, "By the rule of अन्यद्वा (अन्यत् + वा), how is तत् + वचनम् (that statement) written when joined?",
            ("तद्वचनम्", "त् before the voiced व becomes द्, as अन्यत् + वा."),
            [("तत्वचनम्", "Before a voiced sound the त् does not stay."),
             ("तव्वचनम्", "त् does not become व् before व."),
             ("तन्वचनम्", "त् becomes न् only before a nasal; व is not a nasal.")],
            "तत् + वचनम् = तद्वचनम्, like अन्यत् + वा = अन्यद्वा.",
            "त् + voiced sound → द्.",
            teaches="A final त् before a voiced sound becomes द्: अन्यत् + वा → अन्यद्वा."),
    ],
}

# ---------------------------------------------------------------- unit 39
AUTHORED["39"] = {
    "title": "तस्यास्तन्निमित्तं वायुः प्रकुपितः",
    "question": "By unit 39, what does provoked Vāyu do to the fetus's rasa-carrying channel?",
    "rule": ("For her, on that account, Vāyu (Vāta), provoked, having seized Pitta and Śleṣman (Kapha), presses upon the "
             "fetus's rasa-carrying nāḍī (probably the umbilical cord) and stays there."),
    "limits": ("nāḍī as the umbilical cord is probable, not stated by the word (nāḍī = channel, vessel). rasa = the first "
               "dhātu, nutrient fluid. On that account appears (data) to point back to unit 38 (तस्याः answers यस्याः)."),
    "explain_hi": ("उसी कारण से (तन्निमित्तम्) कुपित वायु यानी वात, पित्त और श्लेष्मा (कफ) दोनों को पकड़कर (परिगृह्य), "
                   "गर्भ की रसवहा नाड़ी को दबाकर (प्रतिपीड्य) वहीं ठहर जाता है (अवतिष्ठते)। "
                   "रस यहाँ पहली धातु, पोषक द्रव है। "
                   "नाड़ी को गर्भनाल मानना सम्भावित है; शब्द का अर्थ केवल नली या वाहिका है। "
                   "‘तस्याः’ पिछली इकाई के ‘यस्याः’ का उत्तर है।"),
    "hook": "कुपित वात ने पित्त-कफ पकड़े, रसवहा नाड़ी दबाई, वहीं टिक गया।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 39, which doṣa is provoked and seizes the other two?",
            ("Vāyu (Vāta)", "वायुः प्रकुपितः पित्तश्लेष्माणौ परिगृह्य."),
            [("Pitta (bile)", "Pitta is one of the two that are seized."),
             ("Kapha (phlegm)", "Śleṣman (Kapha) is one of the two that are seized."),
             ("Rakta (blood)", "Blood is not named in unit 39.")],
            "Provoked Vāyu seizes Pitta and Kapha.",
            "वायुः प्रकुपितः."),
        order(1, "Put the steps of unit 39 in the line's order.",
              ["वायुः प्रकुपितः", "पित्तश्लेष्माणौ परिगृह्य", "गर्भस्य रसवहां नाडीं", "प्रतिपीड्य", "अवतिष्ठते"],
              "Vāyu, provoked, having seized Pitta and Kapha, the fetus's rasa-carrying channel, having pressed upon, stays.",
              "प्रकुपित → परिगृह्य → रसवहा नाडी → प्रतिपीड्य → अवतिष्ठते."),
        match(2, "Match each word of unit 39 to its meaning.",
              [["प्रकुपित", "provoked"], ["परिगृह्य", "having seized"], ["रसवहा", "rasa-carrying"],
               ["प्रतिपीड्य", "having pressed upon"], ["अवतिष्ठते", "stays, remains"]],
              "The chain of actions of provoked Vāyu.",
              "प्रकुपित, परिगृह्य, रसवहा, प्रतिपीड्य, अवतिष्ठते.", role="extend",
              teaches="परिगृह्य and प्रतिपीड्य are absolutives (having done): a prefixed root takes -य."),
        mcq("discriminate", 3, "Why does पित्तश्लेष्माणौ end in -औ in unit 39?",
            ("Dual: Pitta and Śleṣman, two", "The data: dvandva, m. acc. dual: the two doṣas."),
            [("Plural: all of the doṣas", "Only two doṣas are joined, so the form is dual."),
             ("Singular: Pitta on its own", "Śleṣman is joined to Pitta; the form is dual."),
             ("Locative: in Pitta and Kapha", "The data reads accusative dual: the object of परिगृह्य.")],
            "Two doṣas in a dvandva take the dual: पित्तश्लेष्माणौ.",
            "पित्तश्लेष्माणौ = m. acc. dual."),
        mcq("apply", 4, "By the data of unit 39, what is the fetus's rasa-carrying nāḍī?",
            ("Probably the umbilical cord", "The data: probably the umbilical cord (probable)."),
            [("Probably the mother's windpipe", "The data reads the umbilical cord, probably."),
             ("Probably a nerve of the spine", "The data reads channel, vessel: probably the umbilical cord."),
             ("Probably the mother's food pipe", "The data reads the umbilical cord, probably.")],
            "nāḍī = channel; here probably the umbilical cord.",
            "रसवहा नाडी = probably the umbilical cord."),
        mcq("transfer", 5, "By the pattern of परिगृह्य and प्रतिपीड्य, which form is the absolutive of आ + √गम् (to come)?",
            ("आगम्य", "A prefixed root forms its absolutive in -य: आ + गम् → आगम्य."),
            [("आगत्वा", "-त्वा is used for a root without a prefix (गत्वा)."),
             ("आगमित्वा", "-त्वा is not used after a prefix, and गम् has no इ here."),
             ("आगच्छ", "आगच्छ is an imperative (come!), not an absolutive.")],
            "आ + गम् + य = आगम्य (having come), like परि + गृह् + य = परिगृह्य.",
            "Prefix + root → absolutive in -य, not -त्वा.",
            teaches="With a prefix, the absolutive takes -य, not -त्वा: परि + √ग्रह् → परिगृह्य, प्रति + √पीड् → प्रतिपीड्य."),
    ],
}

# ---------------------------------------------------------------- unit 40
AUTHORED["40"] = {
    "title": "ततो नाड्यां दोषैः कुल्यायामिव",
    "question": "By unit 40, how is the nāḍī blocked, and what happens to the fetus?",
    "rule": ("Then, the nāḍī being covered by the doṣas, as a canal (कुल्या) by grass, leaves and the like, rasa is not "
             "carried properly; the fetus, not attaining growth, settles down (उपविशति) or dries up (उपशुष्यति)."),
    "limits": ("nāḍī as the umbilical cord is probable. The names upaviṣṭaka and upaśuṣkaka come in later units; here only "
               "the verbs. The print has 'cupa-' where ca + upaviśati would give copaviśati; no question on it."),
    "explain_hi": ("तब दोषों से नाड़ी (सम्भवतः गर्भनाल) ढक जाती है, जैसे नहर (कुल्या) तिनकों, पत्तों आदि से ढक जाती है; यह उपमा मूल में ही है (कुल्यायामिव)। "
                   "रस ठीक से नहीं बहता (असम्यग्वहनात्), इसलिए गर्भ वृद्धि नहीं पाता। "
                   "तब वह बैठ जाता है (उपविशति) या सूख जाता है (उपशुष्यति)। "
                   "ये दो क्रियाएँ आगे के नाम उपविष्टक और उपशुष्कक की ओर संकेत करती हैं। "
                   "छपे ‘अनाप्नुवञ्चुपविशति’ में ‘चु’ है, जबकि च + उपविशति से ‘चोपविशति’ बनता।"),
    "hook": "तिनकों से ढकी नहर: रस न बहे, गर्भ न बढ़े, बैठे या सूखे।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 40, to what is the blocking of the nāḍī compared?",
            ("A canal covered by grass, leaves", "कुल्यायामिव तृणपत्रादिभिः: as a canal by grass, leaves and the like."),
            [("A pot sealed tight with clay", "No pot is named in unit 40."),
             ("A road blocked by many fallen stones", "No road is named in unit 40."),
             ("A river dried up in summer", "No river or summer is named in unit 40.")],
            "The nāḍī covered by doṣas is like a canal covered by grass and leaves.",
            "कुल्यायाम् इव तृणपत्रादिभिः प्रतिच्छन्नायाम्."),
        order(1, "Put the parts of unit 40 in the line's order.",
              ["ततो नाड्यां दोषैः", "कुल्यायामिव तृणपत्रादिभिः", "प्रतिच्छन्नायां", "रसस्यासम्यग्वहनाद्",
               "गर्भो वृद्धिमनाप्नुवन्", "उपविशत्युपशुष्यति वा"],
              "Then the nāḍī by doṣas, as a canal by grass and leaves, being covered; from rasa's improper flow the fetus, "
              "not growing, settles down or dries up.",
              "नाड्यां दोषैः → कुल्यायामिव → प्रतिच्छन्नायां → असम्यग्वहनात् → वृद्धिमनाप्नुवन् → उपविशति / उपशुष्यति."),
        match(2, "Match each word of unit 40 to its meaning.",
              [["कुल्या", "canal"], ["तृणपत्र", "grass and leaves"], ["प्रतिच्छन्न", "covered over, blocked"],
               ["असम्यग्वहन", "improper carrying"], ["उपविशति", "settles down"], ["उपशुष्यति", "dries up"]],
              "The simile, the block, the cause and the two outcomes.",
              "कुल्या, तृणपत्र, प्रतिच्छन्न, असम्यग्वहन, उपविशति, उपशुष्यति.", role="extend",
              teaches="इव = as, like: कुल्यायामिव = as in a canal."),
        multi("discriminate", 3, "Which outcomes for the fetus does unit 40 name?",
              [("It is born before its time", "Early birth is not named in unit 40."),
               ("It settles down", "Right: उपविशति."),
               ("It dries up", "Right: उपशुष्यति."),
               ("It grows too large", "The unit says it does not attain growth.")],
              [1, 2],
              "Not attaining growth, the fetus settles down or dries up.",
              "उपविशत्युपशुष्यति वा."),
        mcq("apply", 4, "By unit 40, why does the fetus not attain growth?",
            ("Rasa is not carried properly", "रसस्यासम्यग्वहनात्: owing to improper carrying of rasa."),
            [("The mother eats far too little", "Her food is not named in unit 40."),
             ("Too much blood has been lost", "Blood loss is not named in unit 40."),
             ("The womb has grown too cold", "Cold is not named in unit 40.")],
            "The blocked nāḍī does not carry rasa properly.",
            "रसस्य असम्यग्वहनात् गर्भो वृद्धिम् अनाप्नुवन्."),
        mcq("transfer", 5, "By the rule of असम्यग्वहनात् (असम्यक् + वहनात्), how is दिक् + विजयः (conquest of the quarters) written?",
            ("दिग्विजयः", "क् before the voiced व becomes ग्, as असम्यक् + वहनात्."),
            [("दिक्विजयः", "Before a voiced sound the क् does not stay."),
             ("दिङ्विजयः", "क् becomes ङ् only before a nasal; व is not a nasal."),
             ("दिच्विजयः", "क् does not become च् before व.")],
            "दिक् + विजयः = दिग्विजयः, like असम्यक् + वहनात् = असम्यग्वहनात्.",
            "क् + voiced sound → ग्.",
            teaches="A final क् before a voiced sound becomes ग्: असम्यक् + वहनात् → असम्यग्वहनात्."),
    ],
}


# ===================================================================== NOTES_HI
NOTES_HI = {
    "28": ("गद्य-पंक्ति; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। ‘अपूर्णत्रिमासा’ बहुव्रीहि; ‘गर्भ के मास’ गर्भ शब्द से समझे जाते हैं। "
           "‘सार’ का ठीक शास्त्रीय अर्थ नहीं दिया गया। पुष्पदर्शने सप्तमी (भाव-सप्तमी जैसी), स्त्री षष्ठी में। छपा ‘असंजात’ = असञ्जात। "
           "सन्धि जाँची: अपूर्णत्रिमासायाः + तु → अपूर्णत्रिमासायास्तु (विसर्ग + त → स्); प्रायः + न → प्रायो न (अः + घोष → ओ); "
           "गर्भः प्रायः (प से पहले विसर्ग बना रहता है); तिष्ठति + असंजात → तिष्ठत्यसंजात (इ + अ → य)।"),
    "29": ("विश्वास निम्न; अर्थ अस्पष्ट, डेटा इस पर कुछ पक्का नहीं बनाता। ‘ऊर्ध्वम् अपि’ = बाद में भी (तीन मास के बाद? केवल अनुमान); "
           "‘विरुद्धोपक्रमत्वात्’ के दो पाठ: उपचार आपस में टकराते हैं, या उलटा उपचार। क्रिया नहीं; डेटा इसे इकाई २८ का आगे का भाग मानता है। "
           "सन्धि जाँची: आम + अन्वये → आमान्वये (अ + अ → आ); च + ऊर्ध्वम् → चोर्ध्वम् (अ + ऊ → ओ); ऊर्ध्वम् + अपि → ऊर्ध्वमपि; "
           "विरुद्ध + उपक्रम → विरुद्धोपक्रम (अ + उ → ओ)।"),
    "30": ("विश्वास उच्च; कोई पाठ-चिह्न नहीं। संज्ञा छपी नहीं, डेटा ‘(ones)’ लिखता है; सूची इकाई ३२ में। ‘तत्र’ किस स्थिति की ओर है, "
           "इकाई के भीतर नहीं कहा गया। छपा ‘प्रयुंजीत’ = प्रयुञ्जीत (अनुस्वार ञ् के स्थान पर), विधिलिङ् आत्मनेपद प्रथम पुरुष एकवचन। "
           "‘रूक्षशीतानि’ द्वन्द्व, नपुंसक बहुवचन।"),
    "31": ("विश्वास उच्च; कोई पाठ-चिह्न नहीं। एक शब्द की पंक्ति, आगे की सूची (इकाई ३२) का परिचय। "
           "सन्धि जाँची: तत् + यथा → तद्यथा (घोष य से पहले त् → द्)।"),
    "32": ("विश्वास मध्यम। पाठ-चिह्न: ‘पर्पटकघ्नचंदन’ → सम्भवतः पर्पटकघनचन्दन (घन = मुस्ता, अनुमानित); ‘कटुंगधान्यककाथपानं’ → "
           "सम्भवतः कट्वङ्गधान्यकक्वाथपानम् (कट्वंग अज्ञात; काथ = क्वाथ); ‘षष्टिकेपेयाम्’ में ए सम्भवतः छपाई की भूल (षष्टिकपेयाम्)। "
           "इन पर प्रश्न नहीं। पहचान-लेबल डेटा के अनुसार: दुरालभा विवादित, अमृता-उशीर-अतिविषा-धान्यक मानक, पर्पटक सम्भावित। "
           "तृणधान्य कौन-से, नहीं बताया गया। सन्धि जाँची: प्राक् + उपवासम् → प्रागुपवासम् (क् + स्वर → ग्); दुरालभा + अमृता → "
           "दुरालभाऽमृता (आ + अ → आ; छपाई में ऽ); अमृता + उशीर → अमृतोशीर (आ + उ → ओ); चन्दन + अतिविषा → चन्दनातिविषा; "
           "पेयाम् + अशनम् → पेयामशनम्; मुद्ग + आदि → मुद्गादि; यूषैः + जिते → यूषैर्जिते (ऐः + घोष → ऐर्); तु + आमे → त्वामे (उ + आ → वा)।"),
    "33": ("विश्वास मध्यम; कोई पाठ-चिह्न नहीं। छपाई में ‘पतिते’ और ‘मद्यानाम्’ जुड़े हैं। ‘सामर्थ्यतः’ पीने वाली का या वैद्य का, तय नहीं; "
           "आमगर्भ = सम्भवतः आरम्भिक गर्भपात, गर्भकोष्ठ = सम्भवतः गर्भाशय (दोनों सम्भावित)। छपा ‘अर्त्ति’ = अर्ति। "
           "सन्धि जाँची: मद्यानाम् + अन्यतमम् → मद्यानामन्यतमम्; पाययेत् + गर्भ → पाययेद्गर्भ (त् + घोष → द्); "
           "विशुद्धि + अर्थम् → विशुद्ध्यर्थम् (इ + अ → य); ...अर्थम् + अर्ति → ...अर्थमर्ति।"),
    "34": ("विश्वास मध्यम; कोई पाठ-चिह्न नहीं। छपा ‘मासा स्तावंत्यहानीति’ = मासास्तावन्त्यहानीति (विसर्ग का स् अगले शब्द से छपा)। "
           "मास गर्भ के, यह समझा जाता है, छपा नहीं; अनुवाद शब्दशः। उद्दालक विवादित (सम्भवतः कोदो की किस्म; कुछ ग्रन्थों में यह कॉर्डिया का नाम भी)। "
           "‘लोण’ = लवण। अन्तिम ‘इति’ का अनुवाद नहीं किया गया। सन्धि जाँची: द्रव्य + उपहिताभिः → द्रव्योपहिताभिः (अ + उ → ओ); "
           "सतिलाभिः + उद्दालक → सतिलाभिरुद्दालक (इः + घोष → इर्); यवागूभिः + उपाचरेत् → यवागूभिरुपाचरेत्; उपाचरेत् + यावन्तः → "
           "उपाचरेद्यावन्तः; यावन्तः + मासाः → यावन्तो मासाः (अः + घोष → ओ); मासाः + तावन्ति → मासास्तावन्ति (विसर्ग + त → स्); "
           "तावन्ति + अहानि → तावन्त्यहानि; अहानि + इति → अहानीति (इ + इ → ई)।"),
    "35": ("विश्वास उच्च; कोई पाठ-चिह्न नहीं। क्रिया (उपाचरेत्) इकाई ३४ से ली गई। ‘आ’ + पंचमी = तक। ‘दोषधातुक्लेद’ = दोष, धातु और क्लेद "
           "(सूची-पाठ), या ‘दोष-धातु का क्लेद’; इस पर प्रश्न नहीं। सन्धि जाँची: ततः प्रीणनैः (प से पहले विसर्ग बना); प्रीणनैः + बल → "
           "प्रीणनैर्बल; बल + अनुरक्षिभिः → बलानुरक्षिभिः (अ + अ → आ); अनुरक्षिभिः + अस्नेहैः → अनुरक्षिभिरस्नेहैः; अस्नेहैः + आहारैः → "
           "अस्नेहैराहारैः; आहारैः + आ → आहारैरा (इ/ऐ आदि के बाद विसर्ग, घोष या स्वर से पहले → र्)।"),
    "36": ("दो छपी पंक्तियाँ (०२.०४.३८, ०२.०४.३९) एक इकाई में। विश्वास उच्च। पाठ-चिह्न: ‘तस्मात्तीक्ष्णैरनवशेषयञ्चुपाचरेत्’ → "
           "डेटा का सुझाव ‘...अनवशेषयञ् चोपाचरेत्’ (च + उपाचरेत् → चोपाचरेत्; छपे में चु); पर न् + च का शुद्ध मेल ‘अनवशेषयंश्च’ होता, इसलिए पाठ अनिश्चित है (‘अनवशेषयन्नुपाचरेत्’ भी सम्भव)। ‘अनुषज्येत’ = बार-बार लगा रहे (डेटा का पाठ); "
           "तीक्ष्ण उपाय नामित नहीं। सन्धि जाँची: शूलम् + अनुषज्येत → शूलमनुषज्येत; तस्मात् + तीक्ष्णैः → तस्मात्तीक्ष्णैः (अघोष त से पहले त् बना); "
           "तीक्ष्णैः + अनवशेषयन् → तीक्ष्णैरनवशेषयन्; अन् + अवशेषयन् → अनवशेषयन्।"),
    "37": ("विश्वास उच्च; कोई पाठ-चिह्न नहीं। छह गुण-शब्द पुंलिंग बहुवचन: केवल आहारों के (डेटा का पाठ) या तीनों के; तय नहीं। "
           "बस्ति = एनिमा। क्रिया पीछे से; अन्तिम ‘इति’ अनुवाद में नहीं। सन्धि जाँची: परम् + स्नेह → परं स्नेह; स्नेहपानैः + बस्तिभिः → "
           "स्नेहपानैर्बस्तिभिः; बस्तिभिः + आहारैः → बस्तिभिराहारैः; आहारैः + च → आहारैश्च (विसर्ग + च → श्); ...हरैः + इति → ...हरैरिति।"),
    "38": ("विश्वास मध्यम; कोई पाठ-चिह्न नहीं। ‘पुष्पमर्हति’ के दो पाठ: पुष्प उचित (देय) हो, या जो पुष्प के योग्य हो (रजस्वला आयु की); "
           "तय नहीं, इस पर प्रश्न नहीं। पुष्प = सम्भवतः रज जैसा स्राव। वाक्य आगे चलता है (यस्याः ... तस्याः, इकाई ३९)। "
           "सन्धि जाँची: पुष्पम् + अर्हति → पुष्पमर्हति; वर्ज्यानाम् + अवर्जनात् → वर्ज्यानामवर्जनात्; अवर्जनात् पुष्प (अघोष प से पहले त् बना); "
           "स्यात् + अन्यत् → स्यादन्यत् (त् + स्वर → द्); अन्यत् + वा → अन्यद्वा (त् + घोष → द्)।"),
    "39": ("विश्वास उच्च; कोई पाठ-चिह्न नहीं। नाड़ी = सम्भवतः गर्भनाल (शब्द केवल नली/वाहिका); रस = पहली धातु। ‘तस्याः’ इकाई ३८ के "
           "‘यस्याः’ का उत्तर। सन्धि जाँची: तस्याः + तत् → तस्यास्तत् (विसर्ग + त → स्); तत् + निमित्तम् → तन्निमित्तम् (अनुनासिक से पहले "
           "त् → न्; वैकल्पिक, तद्निमित्तम् भी सम्भव, इसलिए प्रश्न नहीं); प्रतिपीड्य + अवतिष्ठते → प्रतिपीड्यावतिष्ठते (अ + अ → आ)।"),
    "40": ("विश्वास उच्च; कोई पाठ-चिह्न नहीं। नाड़ी = सम्भवतः गर्भनाल। उपमा (कुल्यायामिव) मूल में है। ‘उपविशति’ और ‘उपशुष्यति’ आगे के "
           "नाम उपविष्टक, उपशुष्कक की ओर संकेत। छपा ‘अनाप्नुवञ्चुपविशति’: डेटा इसे अनाप्नुवन् + च + उपविशति पढ़ता है; च हो तो "
           "‘अनाप्नुवंश्चोपविशति’ बनता, और छपा रूप ‘अनाप्नुवन्नुपविशति’ भी हो सकता है (डेटा में चिह्नित नहीं), इसलिए प्रश्न नहीं। सन्धि जाँची: ततः + नाड्याम् → ततो नाड्याम्; कुल्यायाम् + इव → कुल्यायामिव; "
           "रसस्य + असम्यक् → रसस्यासम्यक्; असम्यक् + वहनात् → असम्यग्वहनात् (क् + घोष → ग्); वहनात् + गर्भः → वहनाद्गर्भः; "
           "गर्भः + वृद्धिम् → गर्भो वृद्धिम्; उपविशति + उपशुष्यति → उपविशत्युपशुष्यति (इ + उ → यु)।"),
}


# ===================================================================== AIDS
AIDS = {
    "28": {
        "chain": {"steps": ["तीन मास पूरे नहीं", "पुष्प (रक्तस्राव) दिखे", "गर्भ प्रायः नहीं टिकता",
                            "कारण: सार उत्पन्न नहीं हुआ"]},
        "chunks": "अपूर्णत्रिमासायास्तु | पुष्पदर्शने | गर्भः प्रायो न तिष्ठति | असंजातसारत्वात्",
        "sandhi": "विसर्ग + त → स्: अपूर्णत्रिमासायाः + तु → अपूर्णत्रिमासायास्तु · अः + घोष → ओ: प्रायः + न → प्रायो न · "
                  "इ + अ → य: तिष्ठति + असंजात → तिष्ठत्यसंजात।",
        "frame": "कब: अपूर्णत्रिमासायाः पुष्पदर्शने → क्या: गर्भः प्रायः न तिष्ठति → क्यों: असंजातसारत्वात् (पंचमी = कारण)।",
    },
    "29": {
        "chunks": "आमान्वये | चोर्ध्वमपि | विरुद्धोपक्रमत्वात्",
        "sandhi": "अ + अ → आ: आम + अन्वये → आमान्वये · अ + ऊ → ओ: च + ऊर्ध्वम् → चोर्ध्वम् · अ + उ → ओ: विरुद्ध + उपक्रम → विरुद्धोपक्रम।",
        "frame": "किसमें: आमान्वये (आम के अनुबन्ध में) → कब: ऊर्ध्वम् अपि (बाद में भी) → क्यों: विरुद्धोपक्रमत्वात् (एक पाठ: उपचार टकराते हैं)। "
                 "अर्थ अस्पष्ट; क्रिया नहीं।",
    },
    "30": {
        "chunks": "तत्र | रूक्षशीतानि | प्रयुंजीत",
        "frame": "कब: तत्र (उस स्थिति में) → क्या: रूक्षशीतानि (रूक्ष और शीत; संज्ञा नहीं छपी) → क्रिया: प्रयुञ्जीत (प्रयोग करे)।",
        "anchors": "याद-सूत्र: रूखा और ठंडा, ‘रू-शी’। (मेरी याद-पद्धति)",
    },
    "31": {
        "sandhi": "त् + घोष → द्: तत् + यथा → तद्यथा।",
        "anchors": "याद-सूत्र: तद्यथा = ‘जैसे कि’, सूची का दरवाज़ा। (मेरी याद-पद्धति)",
        "frame": "तत् (वह) + यथा (इस प्रकार): परिचय-वाक्य; क्रिया नहीं।",
    },
    "32": {
        "chain": {"steps": ["१ पहले उपवास", "२ तथा: द्रव्यों के काथ का पान", "३ और भोजन: तृणधान्य, शालि, षष्टिक की पेया",
                            "४ साथ में मूँग आदि के यूष", "५ आम जीतने पर: स्निग्ध-शीत, पहले की तरह"]},
        "diagram": {"groups": [
            {"label": "काथ के द्रव्य (क्रम से)", "items": ["दुरालभा: जवासा/धमासा (विवादित)", "अमृता: गिलोय (मानक)",
                                                        "उशीर: खस (मानक)", "पर्पटक: पित्तपापड़ा (सम्भावित)",
                                                        "घन (अनुमानित पाठ): नागरमोथा (सम्भावित)", "चन्दन",
                                                        "अतिविषा: अतीस (मानक)", "बला: बरियार",
                                                        "कट्वंग (अनुमानित पाठ): अज्ञात", "धान्यक: धनिया (मानक)"]}]},
        "chunks": "प्रागुपवासं | तथा दुरालभाऽमृतोशीरपर्पटकघ्नचंदनातिविषाबलाकटुंगधान्यककाथपानं | "
                  "तृणधान्यशालिषष्टिकेपेयामशनं च | मुद्गादियूषैः | जिते त्वामे | स्निग्धशीतानि पूर्ववत्",
        "sandhi": "क् + स्वर → ग्: प्राक् + उपवासम् → प्रागुपवासम् · आ + उ → ओ: अमृता + उशीर → अमृतोशीर · "
                  "ऐः + घोष → ऐर्: यूषैः + जिते → यूषैर्जिते · उ + आ → वा: तु + आमे → त्वामे।",
    },
    "33": {
        "diagram": {"groups": [
            {"label": "कब", "items": ["आमगर्भ गिर जाने पर"]},
            {"label": "क्या", "items": ["मद्यों में से कोई एक", "सामर्थ्य के अनुसार"]},
            {"label": "किसलिए", "items": ["१ गर्भकोष्ठ की शुद्धि", "२ पीड़ा भुलाना"]}]},
        "chunks": "आमगर्भे तु पतिते | मद्यानामन्यतमं | सामर्थ्यतः पाययेत् | गर्भकोष्ठविशुद्ध्यर्थम् | अर्त्तिविस्मरणार्थं च",
        "sandhi": "त् + घोष → द्: पाययेत् + गर्भ → पाययेद्गर्भ · इ + अ → य: विशुद्धि + अर्थम् → विशुद्ध्यर्थम्।",
    },
    "34": {
        "diagram": {"groups": [
            {"label": "यवागू में साथ", "items": ["पाचनीय द्रव्य", "तिल"]},
            {"label": "यवागू में नहीं", "items": ["स्नेह (तेल-वसा)", "लवण"]}]},
        "chunks": "अमद्यपां | पाचनीयद्रव्योपहिताभिः | स्नेहलोणवर्जाभिः | सतिलाभिः | उद्दालकादियवागूभिः | उपाचरेत् | "
                  "यावंतो मासास्तावंत्यहानीति",
        "sandhi": "अः + घोष → ओ: यावन्तः + मासाः → यावन्तो मासाः · विसर्ग + त → स्: मासाः + तावन्ति → मासास्तावन्ति · "
                  "इ + अ → य: तावन्ति + अहानि → तावन्त्यहानि।",
        "anchors": "याद-सूत्र: जितने मास, उतने दिन। (मेरी याद-पद्धति)",
    },
    "35": {
        "chunks": "ततः | प्रीणनैर्बलानुरक्षिभिरस्नेहैराहारैः | आदोषधातुक्लेदशुद्धेः",
        "sandhi": "ऐः/इः + घोष → ऐर्/इर्: प्रीणनैः + बल → प्रीणनैर्बल, अस्नेहैः + आहारैः → अस्नेहैराहारैः · अ + अ → आ: बल + अनुरक्षिभिः → बलानुरक्षिभिः।",
        "frame": "कब: ततः → किससे: आहारैः (प्रीणन, बलानुरक्षी, अस्नेह) → कब तक: आ ...शुद्धेः (आ + पंचमी = तक); क्रिया पीछे से।",
    },
    "36": {
        "chain": {"steps": ["आमगर्भ का शेष", "बार-बार शूल", "इसलिए (तस्मात्)", "तीक्ष्ण से उपचार", "कुछ भी शेष न रहे"]},
        "chunks": "आमगर्भशेषेण हि | पुनः पुनः | शूलमनुषज्येत || तस्मात् | तीक्ष्णैः | अनवशेषयञ्चुपाचरेत्",
        "frame": "कारण (हि): शेष → शूल बार-बार; निष्कर्ष (तस्मात्): तीक्ष्णैः, अनवशेषयन्, उपाचरेत्।",
        "contrast": "शेष (बचा हुआ) ↔ अनवशेष (कुछ न बचे): पहली पंक्ति की समस्या, दूसरी पंक्ति का उपाय; दोनों इसी इकाई में।",
    },
    "37": {
        "diagram": {"groups": [
            {"label": "साधन", "items": ["स्नेह-पान", "बस्ति", "आहार"]},
            {"label": "गुण (क्रम से)", "items": ["१ दीपनीय", "२ पाचनीय", "३ जीवनीय", "४ बृंहणीय", "५ मधुर", "६ वातहर"]}]},
        "chunks": "ततः परं | स्नेहपानैर्बस्तिभिराहारैश्च | दीपनीयपाचनीयजीवनीयबृंहणीयमधुरवातहरैरिति",
        "sandhi": "विसर्ग + च → श्: आहारैः + च → आहारैश्च · इः/ऐः + घोष → र्: बस्तिभिः + आहारैः → बस्तिभिराहारैः।",
        "letters": "छह गुण क्रम से: दी-पा-जी-बृं-म-वा। (मेरी याद-पद्धति)",
    },
    "38": {
        "chain": {"steps": ["गर्भ जातसार (सार बन चुका)", "त्याज्य का त्याग नहीं", "पुष्प दिखे, या योनि से अन्य स्राव"]},
        "chunks": "यस्याः पुष्पमर्हति | जातसारे गर्भे | वर्ज्यानामवर्जनात् | पुष्पदर्शनं स्यात् | अन्यद्वा योनिस्रवणं",
        "sandhi": "त् + स्वर → द्: स्यात् + अन्यत् → स्यादन्यत् · त् + घोष → द्: अन्यत् + वा → अन्यद्वा।",
    },
    "39": {
        "chain": {"steps": ["उसी कारण से", "वायु (वात) कुपित", "पित्त और कफ को पकड़कर", "गर्भ की रसवहा नाड़ी दबाकर",
                            "वहीं ठहर जाता है"]},
        "chunks": "तस्यास्तन्निमित्तं | वायुः प्रकुपितः | पित्तश्लेष्माणौ परिगृह्य | गर्भस्य रसवहां नाडीं | प्रतिपीड्यावतिष्ठते",
        "sandhi": "विसर्ग + त → स्: तस्याः + तत् → तस्यास्तत् · अ + अ → आ: प्रतिपीड्य + अवतिष्ठते → प्रतिपीड्यावतिष्ठते।",
        "frame": "कर्ता: वायुः प्रकुपितः → साथ ली: पित्तश्लेष्माणौ (परिगृह्य) → कर्म: रसवहां नाडीम् (प्रतिपीड्य) → क्रिया: अवतिष्ठते।",
    },
    "40": {
        "chain": {"steps": ["दोषों से नाड़ी ढकी", "जैसे नहर तिनकों-पत्तों से", "रस ठीक से नहीं बहता", "गर्भ को वृद्धि नहीं",
                            "बैठ जाता है या सूख जाता है"]},
        "chunks": "ततो नाड्यां दोषैः | कुल्यायामिव तृणपत्रादिभिः | प्रतिच्छन्नायां | रसस्यासम्यग्वहनाद् | गर्भो वृद्धिमनाप्नुवन् | "
                  "उपविशत्युपशुष्यति वा",
        "sandhi": "क् + घोष → ग्: असम्यक् + वहनात् → असम्यग्वहनात् · अः + घोष → ओ: गर्भः + वृद्धिम् → गर्भो वृद्धिम् · "
                  "इ + उ → यु: उपविशति + उपशुष्यति → उपविशत्युपशुष्यति।",
        "story": "मूल की उपमा: खेत की नहर (कुल्या) में तिनके और पत्ते भर जाएँ तो पानी आगे नहीं पहुँचता; वैसे ही दोषों से ढकी नाड़ी रस नहीं पहुँचाती, "
                 "और गर्भ बढ़ता नहीं।",
    },
}

# ===================================================================== IMAGE_SPECS
IMAGE_SPECS = {
    ("28", "chain"): {
        "file": "sh4-apurna-trimasa-28.svg",
        "alt": ("Flowchart of unit 28: three months not complete, bleeding (puṣpa) seen, then the garbha generally does "
                "not stay; the reason given: its sāra has not developed."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"तीन मास पूरे नहीं\"] --> B[\"पुष्प (रक्तस्राव) दिखे\"]\n"
                 "  B --> C[\"गर्भ प्रायः नहीं टिकता\"]\n"
                 "  D[\"सार उत्पन्न नहीं हुआ\"] -->|\"कारण\"| C\n"),
    },
    ("32", "chain"): {
        "file": "sh4-upavasa-krama-32.svg",
        "alt": ("Chain of unit 32 in line order: 1 first fasting; 2 drinking the decoction of the drugs; 3 food: gruel of "
                "grass-grains, śāli and ṣaṣṭika; 4 with soups of mudga and the like; 5 when āma is overcome, unctuous and "
                "cool, as before."),
        "type": "chain",
        "title": "इकाई ३२: पंक्ति में उपाय (पंक्ति का क्रम)",
        "steps": ["१ पहले उपवास", "२ तथा: द्रव्यों के काथ का पान", "३ और भोजन: तृणधान्य, शालि, षष्टिक की पेया",
                  "४ साथ में मूँग आदि के यूष", "५ आम जीतने पर: स्निग्ध-शीत, पहले की तरह"],
    },
    ("32", "diagram"): {
        "file": "sh4-kvatha-dravya-32.svg",
        "alt": ("Table of the ten drugs of the decoction in unit 32, in line order, with the data's labels: durālabhā "
                "(disputed), amṛtā guḍūcī (standard), uśīra vetiver (standard), parpaṭaka (probable), ghana nut-grass "
                "(conjectural reading, probable), candana sandalwood, ativiṣā (standard), balā, kaṭvaṅga (conjectural "
                "reading, unidentified), dhānyaka coriander (standard)."),
        "type": "table",
        "title": "इकाई ३२: काथ के द्रव्य",
        "heads": ["द्रव्य (क्रम से)", "पहचान"],
        "rows": [["दुरालभा", "जवासा या धमासा (विवादित)"], ["अमृता", "गिलोय (मानक)"], ["उशीर", "खस (मानक)"],
                 ["पर्पटक", "पित्तपापड़ा (सम्भावित)"], ["घन (अनुमानित पाठ)", "नागरमोथा (सम्भावित)"], ["चन्दन", "चन्दन"],
                 ["अतिविषा", "अतीस (मानक)"], ["बला", "बरियार"], ["कट्वंग (अनुमानित पाठ)", "अज्ञात"],
                 ["धान्यक", "धनिया (मानक)"]],
    },
    ("33", "diagram"): {
        "file": "sh4-madya-prayojana-33.svg",
        "alt": ("Flowchart of unit 33: when the āma-garbha has fallen, any one of the madyas according to capacity; for "
                "two purposes: 1 cleansing the garbha-koṣṭha (probably the womb), 2 forgetting the pain."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"आमगर्भ गिरने पर\"] --> B[\"कोई एक मद्य, सामर्थ्य अनुसार\"]\n"
                 "  B --> C[\"१ गर्भकोष्ठ की शुद्धि\"]\n"
                 "  B --> D[\"२ पीड़ा भुलाना\"]\n"),
    },
    ("34", "diagram"): {
        "file": "sh4-amadyapa-yavagu-34.svg",
        "alt": ("Two columns of unit 34, the gruel for a non-drinker: with digestive substances and sesame; without sneha "
                "(fat) and salt."),
        "type": "split",
        "title": "इकाई ३४: मद्य न पीने वाली की यवागू",
        "cols": [["यवागू में साथ", ["पाचनीय द्रव्य", "तिल"]],
                 ["यवागू में नहीं", ["स्नेह (तेल-वसा)", "लवण"]]],
    },
    ("36", "chain"): {
        "file": "sh4-amagarbha-shesha-36.svg",
        "alt": ("Flowchart of unit 36: a remnant of the āma-garbha brings pain again and again; therefore treatment with "
                "sharp (ones), so that no remnant is left."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"आमगर्भ का शेष\"] --> B[\"बार-बार शूल\"]\n"
                 "  B -->|\"इसलिए\"| C[\"तीक्ष्ण से उपचार\"]\n"
                 "  C --> D[\"कुछ भी शेष न रहे\"]\n"),
    },
    ("37", "diagram"): {
        "file": "sh4-snehapana-guna-37.svg",
        "alt": ("Two columns of unit 37: the three means (sneha drinks, bastis, foods) and the six qualities in line order "
                "(dīpanīya, pācanīya, jīvanīya, bṛṃhaṇīya, sweet, Vāta-removing)."),
        "type": "split",
        "title": "इकाई ३७: साधन और गुण",
        "cols": [["साधन", ["स्नेह-पान", "बस्ति", "आहार"]],
                 ["गुण (क्रम से)", ["१ दीपनीय", "२ पाचनीय", "३ जीवनीय", "४ बृंहणीय", "५ मधुर", "६ वातहर"]]],
    },
    ("39", "chain"): {
        "file": "sh4-vayu-nadi-39.svg",
        "alt": ("Numbered flowchart of unit 39: 1 on that account, 2 Vāyu provoked, 3 having seized Pitta and Kapha, "
                "4 pressing the fetus's rasa-carrying nāḍī (probably the umbilical cord), 5 stays there."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"१ उसी कारण से\"] --> B[\"२ वायु कुपित\"]\n"
                 "  B --> C[\"३ पित्त और कफ को पकड़कर\"]\n"
                 "  C --> D[\"४ रसवहा नाड़ी दबाकर\"]\n"
                 "  D --> E[\"५ वहीं ठहरता है\"]\n"),
    },
    ("40", "chain"): {
        "file": "sh4-kulya-upama-40.svg",
        "alt": ("Flowchart of unit 40: the nāḍī covered by doṣas, like a canal by grass and leaves; rasa does not flow "
                "properly; the fetus does not grow; it settles down or dries up."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  S[\"जैसे नहर तिनकों-पत्तों से\"] -.->|\"उपमा\"| A\n"
                 "  A[\"दोषों से नाड़ी ढकी\"] --> B[\"रस ठीक से नहीं बहता\"]\n"
                 "  B --> C[\"गर्भ को वृद्धि नहीं\"]\n"
                 "  C --> D[\"बैठ जाता है\"]\n"
                 "  C -->|\"या\"| E[\"सूख जाता है\"]\n"),
    },
}
