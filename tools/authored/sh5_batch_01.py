from helpers import mcq, match, order, fill, multi, accepts


AUTHORED = {}

# ---------------------------------------------------------------- unit 1
AUTHORED["1"] = {
    "title": "अथातोऽंगविभागं शारीरं व्याख्यास्यामः",
    "question": "By unit 1, what does this chapter set out to explain?",
    "rule": ("Opening formula: now, therefore (अथ अतः), we shall explain (व्याख्यास्यामः, future) the aṅgavibhāga, "
             "the division of the body's parts (aṅga), which is śārīra (bodily)."),
    "limits": ("A prose line. The data reads शारीरम् as an adjective of अङ्गविभागम् ('bodily'); it may also echo the name "
               "of the Śārīra section, which the line does not say. No part is named here; the parts come from unit 2 on."),
    "explain_hi": ("यह अध्याय की आरम्भिक गद्य-पंक्ति है: अब इसलिए (अथातः) हम अंगविभाग, यानी शरीर के अंगों के विभाग, की व्याख्या करेंगे। "
                   "‘शारीरम्’ यहाँ ‘शरीर सम्बन्धी’ विशेषण माना गया है; यह शारीरस्थान के नाम की गूँज भी हो सकता है। "
                   "‘व्याख्यास्यामः’ भविष्यत् काल, उत्तम पुरुष बहुवचन है: हम व्याख्या करेंगे। "
                   "‘अथातोऽंग’ में अतः + अङ्ग है: अः के बाद अ आने पर ओ होता है और अ का लोप अवग्रह (ऽ) से दिखाया जाता है। "
                   "अंग स्वयं इकाई २ से गिनाए जाते हैं।"),
    "hook": "अथातो: अब शरीर के अंगों का बँटवारा।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 1, what does this chapter set out to explain?",
            ("The division of the body into its parts", "अङ्गविभागम्: the division (vibhāga) of the parts (aṅga)."),
            [("The mishaps that can occur in pregnancy", "Pregnancy mishaps are not the topic named in unit 1."),
             ("The signs that show death is near", "Signs of death are not the topic named in unit 1."),
             ("The six seasons and their right diet", "No season is named; the topic is aṅgavibhāga.")],
            "The chapter promises to explain the division of the body's parts.",
            "अङ्गविभागं शारीरं व्याख्यास्यामः = we shall explain the bodily division of the parts."),
        order(1, "Put the words of unit 1 in the line's order.",
              ["अथ", "अतः", "अङ्गविभागम्", "शारीरम्", "व्याख्यास्यामः"],
              "Now, therefore, the division of the parts, bodily, we shall explain.",
              "अथ → अतः → अङ्गविभागम् → शारीरम् → व्याख्यास्यामः."),
        match(2, "Match each word of unit 1 to its meaning.",
              [["अथ", "now"], ["अतः", "therefore"], ["अङ्ग", "part of the body"], ["विभाग", "division"],
               ["व्याख्यास्यामः", "we shall explain"]],
              "अथ अतः opens the chapter; अङ्ग + विभाग = the division of the parts.",
              "अथ, अतः, अङ्ग, विभाग, व्याख्यास्यामः.", role="extend",
              teaches="अङ्गविभाग = the division (vibhāga) of the body's parts (aṅga)."),
        mcq("discriminate", 3, "Which split of अतोऽंग in unit 1 is right?",
            ("अतः + अङ्ग", "अः + अ → ओ, and the second अ is dropped (shown by ऽ)."),
            [("अत + अङ्ग", "अत is not the word; the word is अतः (therefore)."),
             ("अतः + ङ्ग", "ङ्ग is not a word; the word is अङ्ग (part)."),
             ("अतु + अङ्ग", "अतु is not a word, and उ + अ would give व.")],
            "अतः (therefore) + अङ्ग (part): अः + अ → ओऽ: अतोऽङ्ग.",
            "अः + अ → ओ, and the अ that follows is dropped (ऽ)."),
        mcq("apply", 4, "In अथातोऽंगविभागं, what does the sign ऽ (avagraha) mark?",
            ("An initial अ dropped after ओ", "अतः + अङ्ग → अतोऽङ्ग: the अ of अङ्ग is dropped."),
            [("A long vowel to be held", "ऽ does not lengthen a vowel; it marks a dropped अ."),
             ("A visarga left unprinted", "The visarga became ओ; ऽ stands for the lost अ."),
             ("A pause between two lines", "ऽ is not a pause; it marks a dropped अ.")],
            "The avagraha shows that the अ of अङ्ग was dropped after the ओ of अतो.",
            "ओ + अ → ओऽ: the avagraha marks the dropped अ."),
        mcq("transfer", 5, "By the pattern of व्याख्यास्यामः (we shall explain), what does वदिष्यामः mean?",
            ("We shall speak", "-ष्यामः / -स्यामः: future, 1st person plural, as व्याख्यास्यामः."),
            [("We have spoken", "-ष्यामः is a future ending, not a past one."),
             ("They will speak", "-मः marks the 1st person plural: we, not they."),
             ("You will speak", "-मः marks the 1st person plural: we, not you.")],
            "वदिष्यामः = we shall speak, like व्याख्यास्यामः = we shall explain.",
            "-स्यामः / -ष्यामः = future, 1st person plural.",
            teaches="The ending -स्यामः (-ष्यामः) marks the future, 1st person plural: व्याख्यास्यामः = we shall explain."),
    ],
}

# ---------------------------------------------------------------- unit 2
AUTHORED["2"] = {
    "title": "सकलमपि शरीरम्; तच्च पुनः षडंगं",
    "question": "By unit 2, into which six parts (aṅga) is the body divided?",
    "rule": ("The whole is called body (शरीर). It has six parts (षडङ्ग, ṣaṭ + aṅga): the head (शिरः), the trunk "
             "(अन्तराधि), the two arms (बाहू) and the two lower limbs (सक्थिनी)."),
    "limits": ("Prose, two printed lines. The point of 'even the whole is called body' is not stated. Printed "
               "शरीरमिमित्युच्यते has two extra letters, and अन्तराधिद्वौ lacks the expected र् (both flagged): no "
               "question on these two forms. The minor parts come in unit 3."),
    "explain_hi": ("पहली पंक्ति कहती है: सम्पूर्ण को भी शरीर कहा जाता है; इसका ठीक आशय यहाँ नहीं बताया गया। "
                   "दूसरी पंक्ति शरीर के छह अंग गिनाती है: शिर, अन्तराधि यानी धड़, दो बाहु यानी भुजाएँ और दो सक्थि यानी टाँगें। "
                   "‘षडंगम्’ = षट् (छह) + अङ्ग: स्वर से पहले ट् का ड् हुआ है। "
                   "‘तच्च’ = तत् + च: च से पहले त् का च् हुआ है। "
                   "छपा ‘शरीरमिमित्युच्यते’ और ‘अन्तराधिद्वौ’ दोनों पर पाठ-चिह्न है।"),
    "hook": "षडंग: एक सिर, एक धड़, दो भुजाएँ, दो टाँगें।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 2, which set names the six parts (aṅga) of the body?",
            ("Head, trunk, two arms, two lower limbs", "शिरोऽन्तराधिद्वौ बाहू सक्थिनी च."),
            [("Head, neck, chest, belly, two feet", "Neck, chest and belly are not named among the six."),
             ("Eyes, navel, nose, two feet, and heart", "Eyes, navel and feet are minor parts (unit 3)."),
             ("Skin, blood, flesh, fat, bone, marrow", "These are not the six aṅgas of unit 2.")],
            "Six parts: head, trunk, two arms, two lower limbs.",
            "षडङ्गम्: शिरः, अन्तराधिः, द्वौ बाहू, सक्थिनी."),
        order(1, "Put the four names of the six parts of unit 2 in the line's order.",
              ["शिरः", "अन्तराधिः", "बाहू", "सक्थिनी"],
              "Head, trunk, the two arms, the two lower limbs.",
              "शिरः → अन्तराधिः → बाहू → सक्थिनी."),
        match(2, "Match each word of unit 2 to its meaning.",
              [["सकल", "whole, entire"], ["शिरस्", "head"], ["अन्तराधि", "trunk"], ["बाहु", "arm"],
               ["सक्थि", "lower limb"]],
              "The whole is body; its six parts are head, trunk, two arms, two lower limbs.",
              "सकल, शिरस्, अन्तराधि, बाहु, सक्थि.", role="extend",
              teaches="अन्तराधि = the trunk, the middle part of the body; सक्थि = the lower limb (thigh and leg)."),
        mcq("discriminate", 3, "Which split of षडंगं in unit 2 is right?",
            ("षट् + अङ्गम्", "ट् before a vowel becomes ड्: षट् + अङ्गम् → षडङ्गम्."),
            [("षड + अङ्गम्", "षड is not the word; the number is षट् (six)."),
             ("षः + अङ्गम्", "षः is not a word, and अः + अ would give ओऽ."),
             ("षडम् + गम्", "षडम् and गम् are not the words; they are षट्, अङ्गम्.")],
            "षट् (six) + अङ्गम् (part): ट् + vowel → ड्.",
            "A final ट् becomes ड् before a vowel."),
        multi("apply", 4, "Which statements fit unit 2?",
              [("The body is said to have six parts", "Right: षडङ्गम्, six parts."),
               ("The eyes are among the six parts", "The eyes are minor parts (pratyaṅga), unit 3."),
               ("The two lower limbs are among them", "Right: सक्थिनी, the two lower limbs."),
               ("The navel is one of the six parts", "The navel is a minor part (pratyaṅga), unit 3.")],
              [0, 2],
              "Six parts: head, trunk, two arms, two lower limbs; eyes and navel are minor parts.",
              "तच्च पुनः षडङ्गम्."),
        mcq("transfer", 5, "By the rule of तत् + च → तच्च, how is एतत् + च (and this) written?",
            ("एतच्च", "त् before च becomes च्, as तत् + च → तच्च."),
            [("एतद्च", "द् comes before a voiced sound; च is unvoiced."),
             ("एतश्च", "श्च comes from a visarga (अः + च), not from त्."),
             ("एतत्च", "Before च the त् does not stay; it becomes च्.")],
            "एतत् + च = एतच्च, like तत् + च = तच्च.",
            "त् + च → च्च.",
            teaches="A final त् becomes च् before च: तत् + च → तच्च."),
    ],
}

# ---------------------------------------------------------------- unit 3
AUTHORED["3"] = {
    "title": "नेत्रनाभिघ्राणिपादादीनि त्वस्य प्रत्यंगानि",
    "question": "By unit 3, what are the minor parts (pratyaṅga) of the body?",
    "rule": ("But (तु) the minor parts (प्रत्यङ्ग) of this body are the eyes (नेत्र), the navel (नाभि), the nose "
             "(read घ्राण), the feet (पाद) and so on (आदि)."),
    "limits": ("Prose. Printed घ्राणि is not a known stem; 'nose' rests on the reading घ्राण (flagged): no question on "
               "that member. आदि (and so on) means the list is open; the line names only these four."),
    "explain_hi": ("इकाई २ के छह अंगों के बाद यह पंक्ति प्रत्यंग, यानी छोटे अंग, बताती है: नेत्र, नाभि, घ्राण (नाक), पाद आदि। "
                   "‘आदि’ से सूची खुली है; केवल ये चार नाम छपे हैं। "
                   "छपा ‘घ्राणि’ कोई ज्ञात शब्द नहीं; ‘नाक’ अर्थ ‘घ्राण’ पाठ मानकर है। "
                   "‘त्वस्य’ = तु + अस्य: उ के बाद अ आने पर उ का व् होता है।"),
    "hook": "छह बड़े अंग, फिर छोटे प्रत्यंग: आँख, नाभि, (नाक), पैर आदि।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "Which of these does unit 3 name as a minor part (pratyaṅga)?",
            ("The navel", "नाभि is in the list of pratyaṅgas."),
            [("The trunk", "The trunk (antarādhi) is one of the six aṅgas, unit 2."),
             ("The head", "The head is one of the six aṅgas, unit 2."),
             ("The arms", "The arms are among the six aṅgas, unit 2.")],
            "The navel is a minor part; head, trunk and arms are main parts.",
            "नेत्रनाभि...पादादीनि प्रत्यङ्गानि."),
        order(1, "Put the words of unit 3 in the line's order.",
              ["नेत्रनाभिघ्राणिपादादीनि", "तु", "अस्य", "प्रत्यङ्गानि"],
              "Eyes, navel, nose, feet and so on, but, of this, the minor parts.",
              "...पादादीनि → तु → अस्य → प्रत्यङ्गानि."),
        match(2, "Match each word of unit 3 to its meaning.",
              [["नेत्र", "eye"], ["नाभि", "navel"], ["पाद", "foot"], ["आदि", "and so on"],
               ["प्रत्यङ्ग", "minor part"]],
              "The minor parts are the eyes, the navel, the feet and so on.",
              "नेत्र, नाभि, पाद, आदि, प्रत्यङ्ग.", role="extend",
              teaches="प्रत्यङ्ग = a minor or secondary part, as against the six main parts (aṅga)."),
        mcq("discriminate", 3, "Which split of त्वस्य in unit 3 is right?",
            ("तु + अस्य", "उ before a vowel becomes व्: तु + अस्य → त्वस्य."),
            [("ते + अस्य", "ए + अ would give तेऽस्य, not त्वस्य."),
             ("तत् + अस्य", "त् + अ would give तदस्य, not त्वस्य."),
             ("तु + स्य", "स्य is not a word; the word is अस्य (of this).")],
            "तु (but) + अस्य (of this): उ + अ → व.",
            "उ + a different vowel → व् + that vowel."),
        mcq("apply", 4, "A student calls the eye one of the six aṅgas. By units 2 and 3, what is the correction?",
            ("The eye is a minor part, a pratyaṅga", "Unit 3 lists नेत्र among the pratyaṅgas."),
            [("The eye is a seventh main aṅga", "Unit 2 counts six aṅgas; the eye is not one."),
             ("The eye is one of the great elements", "The eye is listed as a pratyaṅga, not an element."),
             ("The eye belongs to the two arms", "The eye is listed on its own as a pratyaṅga.")],
            "Six main parts in unit 2; the eye is a minor part in unit 3.",
            "नेत्र ... प्रत्यङ्गानि."),
        mcq("transfer", 5, "By the rule of तु + अस्य → त्वस्य, how is सु + अस्ति (may it be well) written?",
            ("स्वस्ति", "उ before अ becomes व्, as तु + अस्य → त्वस्य."),
            [("सोस्ति", "ओ comes from अ + उ, not from उ + अ."),
             ("सूस्ति", "उ + अ does not give a long ऊ."),
             ("सवस्ति", "The उ becomes the consonant व्; no अ is added.")],
            "सु + अस्ति = स्वस्ति, like तु + अस्य = त्वस्य.",
            "उ + अ → व.",
            teaches="Before a different vowel, उ becomes व्: तु + अस्य → त्वस्य."),
    ],
}

# ---------------------------------------------------------------- unit 4
AUTHORED["4"] = {
    "title": "महाभूतेभ्यश्चेतनाधिष्ठितेभ्योऽभिनिर्वृत्तिः",
    "question": "By unit 4, from what does origination (abhinirvṛtti) come?",
    "rule": ("Origination (अभिनिर्वृत्ति) is from the great elements (महाभूत), which consist of the great guṇas "
             "(महागुणमय) and are presided over by consciousness (चेतनाधिष्ठित)."),
    "limits": ("Low confidence. The printed आरुनेभ्यो is damaged; 'constituted of space, wind, fire, water, earth' rests on "
               "the conjecture आरब्धेभ्यः: no question on that word or on how the five names join the line. 'Great guṇas' "
               "is not taken as the three guṇas of later units."),
    "explain_hi": ("यह इकाई कहती है कि उत्पत्ति (अभिनिर्वृत्ति) महाभूतों से होती है। "
                   "ये महाभूत महागुणमय हैं और चेतना से अधिष्ठित हैं। "
                   "पंक्ति में ख (आकाश), पवन (वायु), तेज (अग्नि), जल और भूमि के नाम छपे हैं; पर इनसे जुड़ा शब्द ‘आरुनेभ्यो’ "
                   "क्षतिग्रस्त है और ‘इनसे बने’ अर्थ केवल अनुमानित पाठ ‘आरब्धेभ्यः’ पर है। "
                   "‘तेजो’ में तेजस् का अस् घोष ज से पहले ओ बना है। "
                   "इस इकाई का विश्वास कम है।"),
    "hook": "पंचमहाभूत, चेतना से अधिष्ठित: वहीं से उत्पत्ति।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 4, from what does origination (abhinirvṛtti) come?",
            ("From the great elements (mahābhūta)", "महाभूतेभ्यः ... अभिनिर्वृत्तिः."),
            [("From the six tastes (rasa) alone", "No taste is named in unit 4."),
             ("From the three doṣas in balance", "No doṣa is named in unit 4."),
             ("From the minor parts (pratyaṅga)", "The minor parts are named in unit 3, not as a source.")],
            "Origination is from the great elements.",
            "महाभूतेभ्यः अभिनिर्वृत्तिः."),
        order(1, "Put the five names in the compound of unit 4 in the line's order.",
              ["ख", "पवन", "तेजस्", "जल", "भूमि"],
              "Space, wind, fire, water, earth: the printed order of the compound.",
              "ख → पवन → तेजस् → जल → भूमि."),
        match(2, "Match each word of unit 4 to its meaning.",
              [["महाभूत", "great element"], ["चेतना", "consciousness"], ["अधिष्ठित", "presided over"],
               ["अभिनिर्वृत्ति", "origination"], ["ख", "space"]],
              "Origination is from the great elements, presided over by consciousness.",
              "महाभूत, चेतना, अधिष्ठित, अभिनिर्वृत्ति, ख.", role="extend",
              teaches="चेतनाधिष्ठित = presided over (adhiṣṭhita) by consciousness (cetanā)."),
        mcq("discriminate", 3, "Why is तेजस् printed तेजो in तेजोजल of unit 4?",
            ("Its -अस् becomes ओ before the voiced ज", "तेजस् + जल: अस् → अः → ओ before a voiced sound."),
            [("The ओ marks the dual of तेजस्", "ओ here is sandhi, not a dual ending."),
             ("जल makes any vowel before it long", "No lengthening rule applies; अस् → ओ."),
             ("Its -अस् becomes ओ before any sound", "Only before a voiced sound; before क, त ... it differs.")],
            "तेजस् + जल → तेजोजल: अस् (as visarga) + voiced consonant → ओ.",
            "अः (from अस्) + voiced consonant → ओ."),
        mcq("apply", 4, "By unit 4, what presides over the great elements from which origination comes?",
            ("Consciousness (cetanā)", "चेतनाधिष्ठितेभ्यः: presided over by consciousness."),
            [("The guṇa tamas (inertia)", "No single guṇa is named as presiding in unit 4."),
             ("The doṣa vāta (wind)", "No doṣa is named in unit 4."),
             ("The mind (manas) alone", "The line names cetanā, not manas.")],
            "The great elements are presided over by consciousness.",
            "चेतना + अधिष्ठित = presided over by consciousness."),
        mcq("transfer", 5, "By the rule of तेजस् + जल → तेजोजल, how is मनस् + हर (charming the mind) written?",
            ("मनोहर", "अस् before the voiced ह becomes ओ, as in तेजोजल."),
            [("मनर्हर", "र् comes after vowels other than अ and आ."),
             ("मनाहर", "अस् does not become आ before ह."),
             ("मनस्हर", "Before a voiced sound the स् does not stay.")],
            "मनस् + हर = मनोहर, like तेजस् + जल = तेजोजल.",
            "अस् + voiced consonant → ओ.",
            teaches="A stem in -अस् shows -ओ before a voiced consonant: तेजस् + जल → तेजोजल."),
    ],
}

# ---------------------------------------------------------------- unit 5
AUTHORED["5"] = {
    "title": "भूतानामेवच ... सारूप्यमसारूप्यं वा",
    "question": "By unit 5, how do similarity and dissimilarity of form, size, voice and so on come about?",
    "rule": ("From the special arrangement (सन्निवेशविशेष) of the elements themselves, of many forms, through the power "
             "of various actions seen and unseen, comes similarity or dissimilarity (सारूप्य / असारूप्य) of form, size, "
             "unctuousness, lustre, voice and so on, in very many kinds."),
    "limits": ("One long prose sentence. भूत is read 'elements' (after unit 4); 'beings' is also possible. The line does "
               "not say which action gives which feature, nor name the actions."),
    "explain_hi": ("यह लम्बी गद्य-पंक्ति बताती है कि आकृति, प्रमाण, स्नेह (चिकनाई), दीप्ति, स्वर आदि की समानता या असमानता क्यों होती है। "
                   "कारण है भूतों की ही विशेष संरचना (सन्निवेशविशेष), जो अनेक रूपों वाली है और दृष्ट-अदृष्ट विविध कर्मों के बल से बनती है। "
                   "यह समानता-असमानता सूक्ष्म और स्थूल के तारतम्य से भिन्न होकर अत्यन्त अनेक प्रकार की होती है। "
                   "‘भूत’ को यहाँ ‘तत्त्व’ पढ़ा गया है; ‘प्राणी’ अर्थ भी सम्भव है। "
                   "कौन-सा कर्म कौन-सा गुण देता है, यह पंक्ति नहीं कहती।"),
    "hook": "भूतों की बनावट और कर्म का बल: इसी से आकृति, स्वर आदि में समानता या असमानता।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 5, what comes about from the special arrangement of the elements?",
            ("Likeness or unlikeness of form, voice and so on", "सारूप्यमसारूप्यं वा ... निष्पद्यते."),
            [("The six parts and the minor parts of the body", "The parts are named in units 2 and 3, not here."),
             ("The five marks of the elements, in their order", "The marks are named in unit 11, not here."),
             ("The three guṇas in each of the five elements", "The guṇas of the elements come in units 6-10.")],
            "Similarity or dissimilarity of form, size, voice and so on.",
            "सारूप्यम् असारूप्यं वा निष्पद्यते."),
        order(1, "Put the qualities of unit 5 in the line's order.",
              ["आकृति", "प्रमाण", "स्नेह", "दीप्ति", "स्वर"],
              "Form, size, unctuousness, lustre, voice (and so on).",
              "आकृति → प्रमाण → स्नेह → दीप्ति → स्वर."),
        match(2, "Match each word of unit 5 to its meaning.",
              [["सन्निवेश", "arrangement"], ["दृष्ट", "seen"], ["अदृष्ट", "unseen"], ["तारतम्य", "gradation"],
               ["सारूप्य", "similarity"], ["स्नेह", "unctuousness"]],
              "The arrangement, through seen and unseen actions, gives graded similarity or dissimilarity.",
              "सन्निवेश, दृष्ट, अदृष्ट, तारतम्य, सारूप्य, स्नेह.", role="extend",
              teaches="तारतम्य = gradation in degree; सन्निवेश = arrangement, the way the parts are set together."),
        mcq("discriminate", 3, "What does the अ- of असारूप्य in unit 5 add to सारूप्य?",
            ("It negates it: dissimilarity", "अ- (not) + सारूप्य (similarity) = dissimilarity."),
            [("It makes it plural: similarities", "अ- is a negative prefix, not a plural sign."),
             ("It stresses it: great similarity", "अ- negates; it does not strengthen."),
             ("It makes it past: was similar", "A prefix अ- here does not mark tense.")],
            "सारूप्यम् असारूप्यं वा: similarity or dissimilarity.",
            "अ- before a consonant = not, un-."),
        mcq("apply", 4, "Two people differ in voice and lustre. By unit 5, through what power does this come about?",
            ("Through various actions, seen and unseen", "दृष्टादृष्टविविधकर्मवशात्: by the power of actions."),
            [("Through the guṇa sattva and nothing else", "No single guṇa is named as the cause in unit 5."),
             ("Through the number of the six main parts", "The six parts (unit 2) are not named as the cause."),
             ("Through the five marks given in unit 11", "The marks of unit 11 are not named as the cause.")],
            "The arrangement arises through the power of various actions, seen and unseen.",
            "दृष्ट-अदृष्ट-विविध-कर्म-वशात्."),
        mcq("transfer", 5, "By the pattern of सारूप्य / असारूप्य, what does असत्यम् mean in a new example?",
            ("Untruth", "अ- (not) + सत्य (truth), as अ- + सारूप्य."),
            [("Great truth", "अ- negates; it does not strengthen."),
             ("Many truths", "अ- is not a plural sign."),
             ("Half truth", "अ- means not, not half.")],
            "असत्यम् = untruth, like असारूप्यम् = dissimilarity.",
            "अ- + noun (before a consonant) = its opposite.",
            teaches="The prefix अ- before a consonant negates a word: सारूप्य (similarity) → असारूप्य (dissimilarity)."),
    ],
}

# ---------------------------------------------------------------- unit 6
AUTHORED["6"] = {
    "title": "तत्र सत्वबहुलमाकाशं",
    "question": "By unit 6, which guṇa abounds in space (ākāśa)?",
    "rule": ("Among these (तत्र: the five great elements of unit 4), space (आकाश) is abundant in sattva (सत्त्वबहुल), "
             "the guṇa of lucidity. The verb 'is' is understood."),
    "limits": ("A short prose line. Printed सत्व is read सत्त्व. The line names only space and sattva; the other "
               "elements follow in units 7 to 10."),
    "explain_hi": ("इन (पाँच महाभूतों) में आकाश सत्त्व-बहुल है, यानी उसमें सत्त्व गुण की अधिकता है। "
                   "‘तत्र’ इकाई ४ में गिनाए पाँच महाभूतों की ओर संकेत करता है। "
                   "‘सत्त्वबहुलम्’ बहुव्रीहि है और नपुंसक लिंग में आकाशम् से मेल खाता है। "
                   "छपा ‘सत्व’ सत्त्व पढ़ा गया है; क्रिया ‘है’ समझी जाती है।"),
    "hook": "आकाश = सत्त्व से भरपूर।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 6, which guṇa abounds in space (ākāśa)?",
            ("Sattva", "सत्त्वबहुलम् आकाशम्: space is abundant in sattva."),
            [("Rajas", "Rajas abounds in wind (unit 7), not in space."),
             ("Tamas", "Tamas abounds in earth (unit 10), not in space."),
             ("Ojas", "Ojas is not a guṇa named in unit 6.")],
            "Space is abundant in sattva.",
            "सत्त्वबहुलम् आकाशम्."),
        match(1, "Match each word of unit 6 to its meaning.",
              [["तत्र", "among these"], ["सत्त्व", "guṇa of lucidity"], ["बहुल", "abundant"], ["आकाश", "space"]],
              "Among these, space is abundant in sattva.",
              "तत्र, सत्त्व, बहुल, आकाश."),
        fill(2, "By unit 6, space (ākāśa) is abundant in the guṇa ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("सत्त्व", None, "सत्व", "सत्त्वम्"),
             "सत्त्वबहुलम् आकाशम्: space is abundant in sattva.",
             "सत्त्व = the guṇa of lucidity; printed सत्व is read सत्त्व.",
             "सत्त्वबहुलम् आकाशम्."),
        mcq("discriminate", 3, "Which split of सत्वबहुलमाकाशं in unit 6 is right?",
            ("सत्त्वबहुलम् + आकाशम्", "A final म् before a vowel joins it: -लम् + आ → -लमा."),
            [("सत्त्वबहुल + माकाशम्", "माकाशम् is not a word; the word is आकाशम्."),
             ("सत्त्वबहुला + आकाशम्", "आ + आ would give -लाकाशम्, with no म्."),
             ("सत्त्वबहुलः + आकाशम्", "A visarga after अ is dropped before आ; no म् would appear.")],
            "सत्त्वबहुलम् + आकाशम्: the म् simply joins the following vowel.",
            "Final म् + vowel → म् joined to the vowel."),
        mcq("apply", 4, "In unit 6, what does तत्र (among these) refer to?",
            ("The five great elements of unit 4", "The note: tatra refers to the five elements named in unit 4."),
            [("The six main parts of unit 2", "The six parts are not the elements the guṇas belong to."),
             ("The minor parts named in unit 3", "The minor parts are not what tatra points to here."),
             ("The sense organs of the later units", "tatra points back, to the five elements of unit 4.")],
            "tatra = among the five great elements named in unit 4.",
            "तत्र = among these, pointing back."),
        mcq("transfer", 5, "By the pattern of सत्त्वबहुलम् आकाशम्, what does जलबहुलः देशः mean in a new example?",
            ("A region abundant in water", "Bahuvrīhi: जल + बहुल = having much water, said of the region."),
            [("Much water from a region", "बहुल describes the region; it is not a source."),
             ("A region with no water", "बहुल is abundant, not lacking."),
             ("Water that is a region", "The compound means having much water.")],
            "जलबहुलः देशः = a region abundant in water, like सत्त्वबहुलम् आकाशम्.",
            "X-बहुल = abundant in X, agreeing with its noun.",
            teaches="X-बहुल is a bahuvrīhi, 'abundant in X', and agrees with the noun it describes: सत्त्वबहुलम् आकाशम्."),
    ],
}

# ---------------------------------------------------------------- unit 7
AUTHORED["7"] = {
    "title": "रजोबहुलो वायुः",
    "question": "By unit 7, which guṇa abounds in wind (vāyu)?",
    "rule": ("Wind (वायु) is abundant in rajas (रजोबहुल), the guṇa of activity. The verb 'is' is understood."),
    "limits": ("A two-word prose line. It names only wind and rajas; it gives no mark or effect of wind."),
    "explain_hi": ("वायु रजस्-बहुल है, यानी उसमें रजस् गुण की अधिकता है। "
                   "‘रजोबहुलः’ बहुव्रीहि है और पुंलिंग में वायुः से मेल खाता है। "
                   "‘रजो’ में रजस् का अस् घोष ब से पहले ओ बना है; ‘बहुलो वायुः’ में बहुलः का अः घोष व से पहले ओ बना है। "
                   "क्रिया ‘है’ समझी जाती है।"),
    "hook": "वायु = रजस् (सक्रियता का गुण) से भरपूर।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 7, which element is abundant in rajas?",
            ("Wind", "रजोबहुलो वायुः: wind is abundant in rajas."),
            [("Space", "Space is abundant in sattva (unit 6)."),
             ("Earth", "Earth is abundant in tamas (unit 10)."),
             ("Water", "Water is abundant in sattva and tamas (unit 9).")],
            "Wind is abundant in rajas.",
            "रजोबहुलो वायुः."),
        match(1, "Match each word of unit 7 to its meaning.",
              [["रजस्", "guṇa of activity"], ["बहुल", "abundant"], ["वायु", "wind"]],
              "Wind is abundant in rajas.",
              "रजस्, बहुल, वायु."),
        mcq("extend", 2, "In unit 7, what is रजस् (rajas)?",
            ("The guṇa of activity", "The data glosses rajas as the guṇa of activity."),
            [("The guṇa of lucidity", "That is sattva (unit 6)."),
             ("The guṇa of inertia", "That is tamas (units 9 and 10)."),
             ("The mark of hardness", "Hardness is a mark in unit 11, not a guṇa.")],
            "रजस् is the guṇa of activity.",
            "सत्त्व lucidity, रजस् activity, तमस् inertia.",
            teaches="रजस् = the guṇa of activity; wind is abundant in it."),
        mcq("discriminate", 3, "Why is बहुलः printed बहुलो before वायुः in unit 7?",
            ("अः becomes ओ before the voiced व", "व is voiced: बहुलः + वायुः → बहुलो वायुः."),
            [("ओ marks the dual number here", "रजोबहुलः is singular; ओ is sandhi."),
             ("अः becomes ओ before every sound", "Only before a voiced consonant (or अ)."),
             ("ओ shows that व is unvoiced", "व is a voiced sound; that is why ओ appears.")],
            "बहुलः + वायुः = बहुलो वायुः: अः + voiced consonant → ओ.",
            "अः + voiced consonant → ओ."),
        multi("apply", 4, "Which statements fit unit 7?",
              [("Wind is abundant in tamas", "Unit 7 says rajas, not tamas."),
               ("रजोबहुलः is masculine, agreeing with वायुः", "Right: the data marks both masculine nominative."),
               ("The line names the mark of wind", "No mark is named in unit 7."),
               ("Wind is abundant in rajas", "Right: रजोबहुलो वायुः.")],
              [1, 3],
              "Wind is abundant in rajas; the bahuvrīhi agrees with वायुः.",
              "रजोबहुलो वायुः."),
        mcq("transfer", 5, "By the rule of बहुलो वायुः, how is रामः + वदति (Rāma speaks) written?",
            ("रामो वदति", "अः before the voiced व becomes ओ, as बहुलः + वायुः."),
            [("रामर्वदति", "र् comes after vowels other than अ and आ."),
             ("रामा वदति", "अः does not become आ before व."),
             ("रामः वदति", "Before a voiced sound the visarga after अ does not stay.")],
            "रामः + वदति = रामो वदति, like बहुलः + वायुः = बहुलो वायुः.",
            "अः + voiced consonant → ओ.",
            teaches="A visarga after अ becomes ओ before a voiced consonant: बहुलः + वायुः → बहुलो वायुः."),
    ],
}

# ---------------------------------------------------------------- unit 8
AUTHORED["8"] = {
    "title": "उभयबहुलोऽग्निः",
    "question": "By unit 8, what is fire (agni) abundant in?",
    "rule": ("Fire (अग्नि) is abundant in both (उभयबहुल). The line does not name the two; the verb 'is' is understood."),
    "limits": ("'Both' is not named in the line. From units 6 and 7 it would be sattva and rajas, but the text does "
               "not say so here: no question keys which two."),
    "explain_hi": ("अग्नि ‘उभय-बहुल’ है, यानी दोनों की अधिकता वाला। "
                   "कौन-से दो, यह पंक्ति नहीं कहती; इकाई ६ और ७ के सन्दर्भ से सत्त्व और रजस् अनुमानित हैं, पर यहाँ लिखा नहीं। "
                   "‘बहुलोऽग्निः’ = बहुलः + अग्निः: अः के बाद अ आने पर ओ होता है और अ का लोप अवग्रह (ऽ) से दिखता है। "
                   "क्रिया ‘है’ समझी जाती है।"),
    "hook": "अग्नि = ‘दोनों’ से भरपूर (कौन-से, पंक्ति नहीं कहती)।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 8, which element is abundant in both?",
            ("Fire", "उभयबहुलोऽग्निः: fire is abundant in both."),
            [("Space", "Space is abundant in sattva (unit 6)."),
             ("Wind", "Wind is abundant in rajas (unit 7)."),
             ("Earth", "Earth is abundant in tamas (unit 10).")],
            "Fire is abundant in both.",
            "उभयबहुलोऽग्निः."),
        match(1, "Match each word of unit 8 to its meaning.",
              [["उभय", "both"], ["बहुल", "abundant"], ["अग्नि", "fire"]],
              "Fire is abundant in both.",
              "उभय, बहुल, अग्नि."),
        fill(2, "The word for 'both' in unit 8 is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("उभय"),
             "उभयबहुलः = abundant in both.",
             "उभय = both.",
             "उभयबहुलोऽग्निः = fire is abundant in both."),
        mcq("discriminate", 3, "Which split of बहुलोऽग्निः in unit 8 is right?",
            ("बहुलः + अग्निः", "अः + अ → ओ, and the अ of अग्निः is dropped (ऽ)."),
            [("बहुलो + ग्निः", "ग्निः is not a word; the word is अग्निः (fire)."),
             ("बहुल + अग्निः", "अ + अ would give बहुलाग्निः, with आ."),
             ("बहुलौ + अग्निः", "औ + अ would give बहुलावग्निः.")],
            "बहुलः + अग्निः = बहुलोऽग्निः: अः + अ → ओऽ.",
            "अः + अ → ओ, and the अ that follows is dropped (ऽ)."),
        mcq("apply", 4, "A reader asks which two guṇas 'both' means. What does unit 8 itself say?",
            ("It does not name the two", "The note: 'both' is not named in the unit."),
            [("It names sattva and tamas", "No guṇa is named in unit 8."),
             ("It names rajas and tamas", "No guṇa is named in unit 8."),
             ("It names all of the three", "No guṇa is named in unit 8.")],
            "The line says only 'both'; it names no guṇa.",
            "उभय = both; the two are not named here."),
        mcq("transfer", 5, "By the rule of बहुलोऽग्निः, how is बालः + अयम् (this boy) written?",
            ("बालोऽयम्", "अः + अ → ओ, with the अ dropped, as बहुलः + अग्निः."),
            [("बाल अयम्", "Before अ the visarga after अ becomes ओ; it is not just dropped."),
             ("बालरयम्", "र् comes after vowels other than अ and आ."),
             ("बालायम्", "अः + अ does not give आ.")],
            "बालः + अयम् = बालोऽयम्, like बहुलः + अग्निः = बहुलोऽग्निः.",
            "अः + अ → ओऽ.",
            teaches="A visarga after अ, before अ, gives ओ and the अ is dropped (ऽ): बहुलः + अग्निः → बहुलोऽग्निः."),
    ],
}

# ---------------------------------------------------------------- unit 9
AUTHORED["9"] = {
    "title": "सत्वतमोबहुलमंबु",
    "question": "By unit 9, which guṇas abound in water (ambu)?",
    "rule": ("Water (अम्बु) is abundant in sattva and tamas (सत्त्वतमोबहुल). The verb 'is' is understood."),
    "limits": ("A one-word prose line in print. Printed सत्व is read सत्त्व. It names only water and these two guṇas."),
    "explain_hi": ("जल (अम्बु) सत्त्व और तमस् की अधिकता वाला है। "
                   "‘सत्त्वतमोबहुलम्’ बहुव्रीहि है और नपुंसक लिंग में अम्बु से मेल खाता है। "
                   "‘तमो’ में तमस् का अस् घोष ब से पहले ओ बना है। "
                   "‘अंबु’ का अनुस्वार ब से पहले म् का सूचक है: अम्बु। "
                   "क्रिया ‘है’ समझी जाती है।"),
    "hook": "जल = सत्त्व + तमस्।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 9, which guṇas abound in water?",
            ("Sattva and tamas", "सत्त्वतमोबहुलम् अम्बु."),
            [("Sattva and rajas", "Unit 9 names sattva and tamas, not rajas."),
             ("Rajas and tamas", "Unit 9 names sattva and tamas, not rajas."),
             ("Rajas only", "Rajas is the guṇa of wind (unit 7).")],
            "Water is abundant in sattva and tamas.",
            "सत्त्वतमोबहुलम् अम्बु."),
        order(1, "Put the parts of unit 9 in the line's order.",
              ["सत्त्व", "तमस्", "बहुलम्", "अम्बु"],
              "Sattva, tamas, abundant, water.",
              "सत्त्व → तमस् → बहुलम् → अम्बु."),
        match(2, "Match each word of unit 9 to its meaning.",
              [["सत्त्व", "guṇa of lucidity"], ["तमस्", "guṇa of inertia"], ["बहुल", "abundant"], ["अम्बु", "water"]],
              "Water is abundant in sattva and tamas.",
              "सत्त्व, तमस्, बहुल, अम्बु.", role="extend",
              teaches="तमस् = the guṇa of inertia; अम्बु = water."),
        mcq("discriminate", 3, "In printed अंबु of unit 9, what does the anusvāra ं stand for?",
            ("The nasal म् before ब: अम्बु", "Before ब the anusvāra stands for the class nasal म्."),
            [("A final म् dropped from the word", "The word is अम्बु; no final म् is meant."),
             ("A long vowel: आबु", "ं is a nasal sign, not a long vowel."),
             ("A visarga after the अ: अःबु", "ं is a nasal sign, not a visarga.")],
            "अंबु = अम्बु: ं before ब stands for म्.",
            "ं before a stop = the nasal of that stop's class (ब → म्)."),
        mcq("apply", 4, "Which gender is बहुलम् in unit 9, and why?",
            ("Neuter, to agree with अम्बु", "अम्बु is neuter; the bahuvrīhi agrees with it."),
            [("Masculine, to agree with वायु", "वायु is in unit 7; here the noun is अम्बु."),
             ("Feminine, to agree with भू", "भू is in unit 10; here the noun is अम्बु."),
             ("Neuter, as every bahuvrīhi is", "Not so: रजोबहुलः (unit 7) is masculine.")],
            "सत्त्वतमोबहुलम् is neuter because अम्बु is neuter.",
            "A bahuvrīhi takes the gender of the noun it describes."),
        mcq("transfer", 5, "By the agreement in सत्त्वतमोबहुलम् अम्बु, which form fits वनम् (forest, n.) to mean abundant in trees?",
            ("वृक्षबहुलं वनम्", "Neuter, to agree with वनम्, as बहुलम् with अम्बु."),
            [("वृक्षबहुला वनम्", "बहुला is feminine; वनम् is neuter."),
             ("वृक्षबहुलो वनम्", "बहुलो (बहुलः) is masculine; वनम् is neuter."),
             ("वृक्षबहुलेन वनम्", "बहुलेन is instrumental; वनम् is nominative.")],
            "वृक्षबहुलं वनम् = a forest abundant in trees: neuter singular, like सत्त्वतमोबहुलम् अम्बु.",
            "The bahuvrīhi agrees with its noun in gender, number and case.",
            teaches="A bahuvrīhi in -बहुल takes the gender and number of its noun: सत्त्वतमोबहुलम् (n.) अम्बु (n.)."),
    ],
}

# ---------------------------------------------------------------- unit 10
AUTHORED["10"] = {
    "title": "तमोबहुला भूः",
    "question": "By unit 10, which guṇa abounds in earth (bhū)?",
    "rule": ("Earth (भू) is abundant in tamas (तमोबहुला), the guṇa of inertia. बहुला is feminine to agree with भूः."),
    "limits": ("A two-word prose line. It names only earth and tamas; the verb 'is' is understood."),
    "explain_hi": ("भूमि (भू) तमस् की अधिकता वाली है। "
                   "‘तमोबहुला’ बहुव्रीहि है और स्त्रीलिंग में भूः से मेल खाता है। "
                   "‘तमो’ में तमस् का अस् घोष ब से पहले ओ बना है। "
                   "‘बहुला’ आकारान्त है, इसलिए भूः से पहले कोई सन्धि-परिवर्तन नहीं।"),
    "hook": "भू = तमस् (जड़ता का गुण) से भरपूर।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 10, which guṇa abounds in earth?",
            ("Tamas", "तमोबहुला भूः: earth is abundant in tamas."),
            [("Sattva", "Sattva abounds in space (unit 6)."),
             ("Rajas", "Rajas abounds in wind (unit 7)."),
             ("Ojas", "Ojas is not a guṇa named in unit 10.")],
            "Earth is abundant in tamas.",
            "तमोबहुला भूः."),
        match(1, "Match each word of unit 10 to its meaning.",
              [["तमस्", "guṇa of inertia"], ["बहुला", "abundant (f.)"], ["भू", "earth"]],
              "Earth is abundant in tamas.",
              "तमस्, बहुला, भू."),
        fill(2, "By unit 10, earth is abundant in the guṇa ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("तमस्", None, "तमः", "तमो"),
             "तमोबहुला भूः: earth is abundant in tamas.",
             "तमस् = the guṇa of inertia; in a compound before ब it shows तमो.",
             "तमोबहुला भूः."),
        mcq("discriminate", 3, "Why is it तमोबहुला and not तमोबहुलो in unit 10?",
            ("It is feminine, to agree with भूः", "भू is feminine; the data marks बहुला f. nom. sg."),
            [("It is plural, for many earths", "भूः is singular; so is बहुला."),
             ("आ is the sandhi of अः before भ", "A visarga after अ gives ओ before भ, not आ."),
             ("It is neuter, as with अम्बु", "The neuter form is बहुलम्; बहुला is feminine.")],
            "तमोबहुला (f.) agrees with भूः (f.).",
            "A bahuvrīhi takes the gender of its noun."),
        mcq("apply", 4, "Which split of तमोबहुला in unit 10 is right?",
            ("तमस् + बहुला", "अस् before the voiced ब becomes ओ: तमोबहुला."),
            [("तमा + बहुला", "तमा is not the word; the guṇa is तमस्."),
             ("तम + उबहुला", "उबहुला is not a word; the word is बहुला."),
             ("तमोब + हुला", "तमोब and हुला are not words.")],
            "तमस् (inertia) + बहुला (abundant): अस् + voiced → ओ.",
            "अस् + voiced consonant → ओ."),
        mcq("transfer", 5, "By the agreement in तमोबहुला भूः, which form fits नदी (river, f.) to mean abundant in water?",
            ("जलबहुला नदी", "Feminine, to agree with नदी, as बहुला with भूः."),
            [("जलबहुलं नदी", "बहुलम् is neuter; नदी is feminine."),
             ("जलबहुलो नदी", "बहुलो (बहुलः) is masculine; नदी is feminine."),
             ("जलबहुलेन नदी", "बहुलेन is instrumental (m./n.); नदी is feminine nominative.")],
            "जलबहुला नदी = a river abundant in water: feminine singular, like तमोबहुला भूः.",
            "The bahuvrīhi agrees with its noun in gender, number and case.",
            teaches="A bahuvrīhi in -बहुल takes the feminine -बहुला with a feminine noun: तमोबहुला भूः."),
    ],
}

# ---------------------------------------------------------------- unit 11
AUTHORED["11"] = {
    "title": "तेषामप्रतिघातश्चलत्वमौष्ण्यं द्रवता काठिन्यम्",
    "question": "By unit 11, what are the marks (liṅga) of the elements, in order?",
    "rule": ("Their (तेषाम्: the five elements) marks (लिङ्ग), in order (क्रमात्), are unobstructedness (अप्रतिघात), "
             "mobility (चलत्व), heat (औष्ण्य), fluidity (द्रवता) and hardness (काठिन्य). इति closes the list."),
    "limits": ("Prose. The line says 'in order' but does not name which mark belongs to which element: no question "
               "pairs a mark with an element."),
    "explain_hi": ("उन (पाँच महाभूतों) के लिंग, यानी चिह्न, क्रम से ये हैं: अप्रतिघात (बाधा न होना), चलत्व (गतिशीलता), औष्ण्य (उष्णता), द्रवता और काठिन्य (कठोरता)। "
                   "‘क्रमात्’ कहा गया है, पर कौन-सा चिह्न किस भूत का है, यह पंक्ति नाम लेकर नहीं कहती। "
                   "‘इति’ सूची का अन्त दिखाता है। "
                   "‘क्रमाल्लिंगानि’ में क्रमात् + लिङ्गानि है: ल से पहले त् का ल् हुआ है।"),
    "hook": "पाँच चिह्न क्रम से: खुला, चलता, तपता, बहता, कठोर।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 11, which is one of the marks (liṅga) of the elements?",
            ("Mobility", "चलत्वम् is the second mark in the list."),
            [("Sweetness", "No taste is named among the marks."),
             ("Coldness", "Heat is named; coldness is not."),
             ("Dryness", "Dryness is not named among the marks.")],
            "Mobility is one of the five marks.",
            "अप्रतिघातः, चलत्वम्, औष्ण्यम्, द्रवता, काठिन्यम्."),
        order(1, "Put the marks of unit 11 in the line's order.",
              ["अप्रतिघात", "चलत्व", "औष्ण्य", "द्रवता", "काठिन्य"],
              "Unobstructedness, mobility, heat, fluidity, hardness.",
              "अप्रतिघात → चलत्व → औष्ण्य → द्रवता → काठिन्य."),
        match(2, "Match each mark of unit 11 to its meaning.",
              [["अप्रतिघात", "unobstructedness"], ["चलत्व", "mobility"], ["औष्ण्य", "heat"], ["द्रवता", "fluidity"],
               ["काठिन्य", "hardness"]],
              "The five marks, in the line's order.",
              "अप्रतिघात, चलत्व, औष्ण्य, द्रवता, काठिन्य.", role="extend",
              teaches="लिङ्ग = mark, sign; the five marks run from unobstructedness to hardness."),
        mcq("discriminate", 3, "Which split of क्रमाल्लिंगानि in unit 11 is right?",
            ("क्रमात् + लिङ्गानि", "त् before ल becomes ल्: क्रमात् + लिङ्गानि → क्रमाल्लिङ्गानि."),
            [("क्रमाल् + लिङ्गानि", "क्रमाल् is not a word; the word is क्रमात् (in order)."),
             ("क्रमा + ल्लिङ्गानि", "ल्लिङ्गानि is not a word; the word is लिङ्गानि."),
             ("क्रमः + लिङ्गानि", "A visarga would give क्रमो लिङ्गानि, not ल्ल.")],
            "क्रमात् (in order) + लिङ्गानि (marks): त् + ल → ल्ल.",
            "A final त् before ल becomes ल्."),
        mcq("apply", 4, "In unit 11, what does the इति after काठिन्यम् do?",
            ("It closes the list of marks", "The note: the closing iti marks the end of the list."),
            [("It adds a sixth mark to it", "No sixth mark follows; iti closes the list."),
             ("It means 'because' here", "iti here closes a list; it gives no reason."),
             ("It turns hardness to softness", "iti changes no meaning; it closes the list.")],
            "इति marks the end of the five marks.",
            "इति = thus: it closes a list."),
        mcq("transfer", 5, "By the pattern of चल (moving) → चलत्व (mobility), what does गुरुत्व mean in a new example?",
            ("Heaviness", "-त्व makes an abstract noun: गुरु (heavy) → heaviness."),
            [("A heavy man", "-त्व names the quality, not a person."),
             ("To make heavy", "-त्व makes a noun, not a verb."),
             ("Very heavy", "-त्व names the quality; it does not mean 'very'.")],
            "गुरुत्व = heaviness, like चलत्व = mobility.",
            "Adjective + -त्व = the quality as a noun.",
            teaches="The suffix -त्व makes an abstract noun of quality: चल (moving) → चलत्व (mobility)."),
    ],
}

# ---------------------------------------------------------------- unit 12
AUTHORED["12"] = {
    "title": "विशेषतश्च श्रोत्रादिष्विंद्रियेष्ववस्थानं",
    "question": "By unit 12, where is the abiding (avasthāna) placed, and with which objects is there association?",
    "rule": ("In particular (विशेषतः), abiding (अवस्थान) in the sense organs (इन्द्रिय) beginning with the ear (श्रोत्र), "
             "and association (अन्वय) with sound, touch, form, taste and smell, increased one by one (एकैकप्रवृद्ध)."),
    "limits": ("Prose. The line does not say which object belongs to which organ, nor explain 'increased one by one'. "
               "Printed ऐकैक is a likely misprint for एकैक (flagged): no question on that join."),
    "explain_hi": ("यह पंक्ति दो बातें कहती है: विशेष रूप से श्रोत्र (कान) आदि इन्द्रियों में अवस्थान, यानी स्थिति; "
                   "और एक-एक बढ़े हुए शब्द, स्पर्श, रूप, रस और गन्ध के साथ अन्वय, यानी सम्बन्ध। "
                   "कौन-सा विषय किस इन्द्रिय का है, और ‘एक-एक बढ़े हुए’ का ठीक आशय, यह यहाँ नहीं बताया गया। "
                   "‘श्रोत्रादिष्विन्द्रियेषु’ में श्रोत्रादिषु + इन्द्रियेषु है: इ से पहले उ का व् हुआ है। "
                   "छपा ‘ऐकैक’ सम्भवतः ‘एकैक’ की छपाई-भूल है।"),
    "hook": "कान से शुरू इन्द्रियाँ; शब्द से गन्ध तक, एक-एक बढ़ते विषय।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 12, in what is the abiding (avasthāna) placed?",
            ("In the sense organs, from the ear on", "श्रोत्रादिषु इन्द्रियेषु अवस्थानम्."),
            [("In the six parts, from the head on", "The six parts are in unit 2, not here."),
             ("In the minor parts, from the eye on", "The minor parts are in unit 3, not here."),
             ("In the five marks, from heat on", "The marks are in unit 11, not here.")],
            "Abiding in the sense organs beginning with the ear.",
            "श्रोत्रादिषु इन्द्रियेषु अवस्थानम्."),
        order(1, "Put the five objects of unit 12 in the line's order.",
              ["शब्द", "स्पर्श", "रूप", "रस", "गन्ध"],
              "Sound, touch, form, taste, smell.",
              "शब्द → स्पर्श → रूप → रस → गन्ध."),
        match(2, "Match each word of unit 12 to its meaning.",
              [["शब्द", "sound"], ["स्पर्श", "touch"], ["रूप", "form"], ["रस", "taste"], ["गन्ध", "smell"],
               ["अन्वय", "association"]],
              "Association with the five objects, from sound to smell.",
              "शब्द, स्पर्श, रूप, रस, गन्ध, अन्वय.", role="extend",
              teaches="अन्वय = association, connection; अवस्थान = abiding, residence."),
        mcq("discriminate", 3, "Which split of श्रोत्रादिष्विंद्रियेषु in unit 12 is right?",
            ("श्रोत्रादिषु + इन्द्रियेषु", "उ before इ becomes व्: -षु + इ → -ष्वि."),
            [("श्रोत्रादिषि + विन्द्रियेषु", "विन्द्रियेषु is not a word; the word is इन्द्रियेषु."),
             ("श्रोत्रादि + ष्विन्द्रियेषु", "ष्विन्द्रियेषु is not a word; the word is इन्द्रियेषु."),
             ("श्रोत्रादिषः + इन्द्रियेषु", "श्रोत्रादिषः is not the word; it is the locative श्रोत्रादिषु.")],
            "श्रोत्रादिषु (in ... beginning with the ear) + इन्द्रियेषु (in the sense organs): उ + इ → वि.",
            "उ + a different vowel → व् + that vowel."),
        multi("apply", 4, "Which statements fit unit 12?",
              [("It pairs each object with its own organ", "The note: which object belongs to which organ is not stated."),
               ("The objects run sound, touch, form, taste, smell", "Right: that is the line's order."),
               ("The sense organs are said to begin with the ear", "Right: श्रोत्रादिषु, beginning with the ear."),
               ("It names the eye as the first sense organ", "The first named is the ear (श्रोत्र).")],
              [1, 2],
              "Organs beginning with the ear; five objects from sound to smell; no pairing stated.",
              "श्रोत्रादिषु इन्द्रियेषु ... शब्दस्पर्शरूपरसगन्धैः."),
        mcq("transfer", 5, "By the rule of श्रोत्रादिषु + इन्द्रियेषु, how is मधु + इव (like honey) written?",
            ("मध्विव", "उ before इ becomes व्, as -षु + इ → -ष्वि."),
            [("मधूव", "उ + इ does not give a long ऊ."),
             ("मधिव", "The उ is not dropped; it becomes व्."),
             ("मधेव", "ए comes from अ + इ, not from उ + इ.")],
            "मधु + इव = मध्विव, like श्रोत्रादिषु + इन्द्रियेषु = श्रोत्रादिष्विन्द्रियेषु.",
            "उ + इ → वि.",
            teaches="Before a different vowel, उ becomes व्: श्रोत्रादिषु + इन्द्रियेषु → श्रोत्रादिष्विन्द्रियेषु."),
    ],
}

# ---------------------------------------------------------------- unit 13
AUTHORED["13"] = {
    "title": "तत्राकाशजानि श्रोत्रं शब्दः स्रोतांसि विविक्तता च",
    "question": "By unit 13, what is born of space (ākāśa)?",
    "rule": ("Among these (तत्र), born of space (आकाशज) are the ear (श्रोत्र), sound (शब्द), the channels (स्रोतस्) "
             "and separateness (विविक्तता)."),
    "limits": ("Prose. विविक्तता is kept as 'separateness'; 'openness, emptiness' is also possible. srotas is a "
               "doctrinal term (a channel of the body) and is not given a modern equivalent."),
    "explain_hi": ("यह पंक्ति बताती है कि आकाश से उत्पन्न (आकाशज) भाव ये हैं: श्रोत्र (कान), शब्द, स्रोतस् यानी शरीर के मार्ग, और विविक्तता यानी अलगाव। "
                   "‘विविक्तता’ का अर्थ ‘खुलापन, रिक्तता’ भी हो सकता है; सीधा अर्थ ‘अलगाव’ रखा गया है। "
                   "स्रोतस् आयुर्वेद का पारिभाषिक शब्द है, इसे किसी आधुनिक नाम से नहीं जोड़ा गया। "
                   "‘तत्राकाश’ = तत्र + आकाश: अ + आ से आ। "
                   "यहाँ से भूतज भावों की सूची शुरू होती है; वायु से उत्पन्न भाव अगली इकाई में हैं।"),
    "hook": "आकाश से: कान, शब्द, मार्ग, खालीपन।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 13, which pair is born of space (ākāśa)?",
            ("The ear and sound", "श्रोत्रं शब्दः: both are ākāśaja."),
            [("The nose and smell", "These belong to earth (unit 17), not space."),
             ("The tongue and taste", "These belong to water (unit 16), not space."),
             ("The eye and form", "Sight and form belong to fire (unit 15), not space.")],
            "The ear and sound are born of space.",
            "आकाशजानि श्रोत्रं शब्दः."),
        order(1, "Put the things born of space in unit 13 in the line's order.",
              ["श्रोत्रम्", "शब्दः", "स्रोतांसि", "विविक्तता"],
              "Ear, sound, channels, separateness.",
              "श्रोत्रम् → शब्दः → स्रोतांसि → विविक्तता."),
        match(2, "Match each word of unit 13 to its meaning.",
              [["आकाशज", "born of space"], ["श्रोत्र", "ear"], ["शब्द", "sound"], ["स्रोतस्", "channel"],
               ["विविक्तता", "separateness"]],
              "Born of space: ear, sound, channels, separateness.",
              "आकाशज, श्रोत्र, शब्द, स्रोतस्, विविक्तता.", role="extend",
              teaches="स्रोतस् = a channel of the body (a doctrinal term); विविक्तता = separateness, openness."),
        mcq("discriminate", 3, "Which split of तत्राकाशजानि in unit 13 is right?",
            ("तत्र + आकाशजानि", "अ + आ → आ: तत्र + आकाश → तत्राकाश."),
            [("तत्रा + काशजानि", "तत्रा and काशजानि are not the words; they are तत्र, आकाशजानि."),
             ("तत्रः + आकाशजानि", "तत्र has no visarga; it is an indeclinable."),
             ("तत् + राकाशजानि", "राकाशजानि is not a word; the word is आकाशजानि.")],
            "तत्र (among these) + आकाशजानि (born of space): अ + आ → आ.",
            "अ + आ → आ."),
        mcq("apply", 4, "A student adds touch to the things born of space. By unit 13, is that right?",
            ("No: touch is not in the list", "Unit 13 names ear, sound, channels, separateness only."),
            [("Yes: touch is the first item", "The first item is the ear (श्रोत्र)."),
             ("No: touch replaces sound there", "Sound is named in unit 13; touch is not named at all."),
             ("Yes: it is the last item", "The last item is separateness (विविक्तता).")],
            "Touch is not born of space in unit 13; the list is ear, sound, channels, separateness.",
            "आकाशजानि श्रोत्रं शब्दः स्रोतांसि विविक्तता च."),
        mcq("transfer", 5, "By the pattern of आकाशज (born of space), what does जलज mean in a new example?",
            ("Born of water", "-ज = born of: जल + ज, as आकाश + ज."),
            [("Giving water", "-ज means born of, not giving."),
             ("Without water", "-ज means born of, not without."),
             ("Drinking water", "-ज means born of, not drinking.")],
            "जलज = born of water, like आकाशज = born of space.",
            "X + -ज = born of X.",
            teaches="The final member -ज means 'born of': आकाशज = born of space."),
    ],
}


# ===================================================================== NOTES_HI
NOTES_HI = {
    "1": ("गद्य-पंक्ति; विश्वास उच्च; कोई पाठ-चिह्न नहीं। ‘शारीरम्’ अंगविभाग का विशेषण पढ़ा गया; शारीर नामक स्थान की गूँज भी सम्भव। "
          "सन्धि जाँची: अथ + अतः → अथातः (अ + अ → आ); अतः + अङ्ग → अतोऽङ्ग (अः + अ → ओ, अ का लोप ऽ); व्यंजन से पहले म् → ं "
          "(अंगविभागं, शारीरं); छपाई में ‘अंग’ अनुस्वार से छपा है (= अङ्ग)।"),
    "2": ("दो छपी पंक्तियाँ (02.05.2, 02.05.3); गद्य; विश्वास मध्यम। पाठ-चिह्न: छपा ‘शरीरमिमित्युच्यते’ में दो अक्षर अधिक हैं, "
          "‘शरीरम् इति उच्यते’ पढ़ा गया; छपा ‘अन्तराधिद्वौ’ में अपेक्षित र् नहीं (अन्तराधिः + द्वौ → अन्तराधिर्द्वौ)। इन दोनों पर कोई प्रश्न नहीं। "
          "पहले वाक्य का ठीक आशय नहीं बताया गया। ‘सक्थिनीच’ में च से पहले केवल रिक्त स्थान छूटा है। सन्धि जाँची: तत् + च → तच्च; "
          "षट् + अङ्गम् → षडङ्गम् (स्वर से पहले ट् → ड्); शिरः + अन्तराधि → शिरोऽन्तराधि।"),
    "3": ("गद्य; विश्वास मध्यम। पाठ-चिह्न: छपा ‘घ्राणि’ ज्ञात शब्द नहीं; ‘घ्राण’ (नाक) पढ़ा गया; इस पर कोई प्रश्न नहीं। ‘आदि’ = इत्यादि। "
          "सन्धि जाँची: तु + अस्य → त्वस्य (उ + अ → व); पाद + आदीनि → पादादीनि (अ + आ → आ); ‘प्रत्यंगानि’ = प्रत्यङ्गानि।"),
    "4": ("गद्य; विश्वास कम। पाठ-चिह्न: छपा ‘आरुनेभ्यो’ क्षतिग्रस्त और अर्थहीन; अनुवाद अनुमानित पाठ ‘आरब्धेभ्यः’ (से बने) पर है, "
          "यह अनुमान भी अनिश्चित। इसलिए पाँच नाम (ख, पवन, तेज, जल, भूमि) पंक्ति से किस सम्बन्ध में जुड़ते हैं, उस पर कोई प्रश्न नहीं; "
          "केवल उनका छपा क्रम पूछा गया। ‘महागुण’ को आगे की इकाइयों के तीन गुण नहीं माना गया। क्रिया ‘है’ समझी जाती है। "
          "सन्धि जाँची: -भ्यः + च → -भ्यश्च; तेजस् + जल → तेजोजल; -भ्यः + अभि → -भ्योऽभि; चेतना + अधिष्ठित → चेतनाधिष्ठित।"),
    "5": ("एक लम्बा गद्य-वाक्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। ‘भूत’ = तत्त्व (पिछली इकाई के अनुसार); ‘प्राणी’ भी सम्भव। "
          "स्नेह यहाँ शरीर का गुण (चिकनाई) है; तारतम्य = मात्रा का क्रमिक भेद। सन्धि जाँची: दृष्ट + अदृष्ट → दृष्टादृष्ट; "
          "-वशात् + अनेक → -वशादनेक (त् + स्वर → द्); -विशेषात् + आकृति → -विशेषादाकृति; स्वर + आदीनाम् → स्वरादीनाम्; "
          "सारूप्यम् + असारूप्यम् → सारूप्यमसारूप्यम्; -भिन्नम् + अति → -भिन्नमति; ‘एवच’ में च से पहले रिक्त स्थान छूटा है।"),
    "6": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। छपा ‘सत्व’ = सत्त्व (वर्तनी)। ‘तत्र’ इकाई ४ के पाँच महाभूतों की ओर संकेत करता है। "
          "क्रिया ‘है’ समझी जाती है। सन्धि जाँची: सत्त्वबहुलम् + आकाशम् → सत्त्वबहुलमाकाशम्; अन्त का म् → ं (आकाशं)।"),
    "7": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। क्रिया ‘है’ समझी जाती है। सन्धि जाँची: रजस् + बहुलः → रजोबहुलः (अस् + घोष → ओ); "
          "बहुलः + वायुः → बहुलो वायुः (अः + घोष व्यंजन → ओ)।"),
    "8": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। ‘उभय’ (दोनों) का नाम पंक्ति में नहीं; इकाई ६-७ के सन्दर्भ से सत्त्व और रजस् माने जा "
          "सकते हैं, पर पाठ यहाँ यह नहीं कहता; इस पर कोई प्रश्न नहीं। सन्धि जाँची: बहुलः + अग्निः → बहुलोऽग्निः (अः + अ → ओ, अ का लोप ऽ)।"),
    "9": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। छपा ‘सत्व’ = सत्त्व। क्रिया ‘है’ समझी जाती है। सन्धि जाँची: तमस् + बहुलम् → तमोबहुलम् "
          "(अस् + घोष → ओ); बहुलम् + अम्बु → बहुलमम्बु (म् + स्वर); ‘अंबु’ = अम्बु (ब से पहले ं = म्)।"),
    "10": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। क्रिया ‘है’ समझी जाती है। ‘तमोबहुला’ स्त्रीलिंग, भूः से मेल। सन्धि जाँची: "
           "तमस् + बहुला → तमोबहुला (अस् + घोष → ओ); बहुला + भूः में कोई परिवर्तन नहीं।"),
    "11": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। अन्त का ‘इति’ सूची बन्द करता है, अनुवाद में नहीं आता। ‘तेषाम्’ = पाँच महाभूतों के; "
           "कौन-सा चिह्न किस भूत का है, यह पंक्ति नाम लेकर नहीं कहती। सन्धि जाँची: तेषाम् + अप्रतिघातः → तेषामप्रतिघातः; "
           "अप्रतिघातः + चलत्वम् → अप्रतिघातश्चलत्वम् (अः + च → अश्च); चलत्वम् + औष्ण्यम् → चलत्वमौष्ण्यम्; काठिन्यम् + इति → काठिन्यमिति; "
           "क्रमात् + लिङ्गानि → क्रमाल्लिङ्गानि (त् + ल → ल्ल)।"),
    "12": ("गद्य; विश्वास मध्यम। पाठ-चिह्न: छपा ‘गंधैरैकैक’ में ‘ऐकैक’ शब्द नहीं; गन्धैः + एकैक से ‘गन्धैरेकैक’ अपेक्षित, सम्भवतः छपाई-भूल; "
           "इस पर कोई प्रश्न नहीं। कौन-सा विषय किस इन्द्रिय का है, यह यहाँ नहीं कहा गया। सन्धि जाँची: विशेषतः + च → विशेषतश्च; "
           "श्रोत्रादिषु + इन्द्रियेषु → श्रोत्रादिष्विन्द्रियेषु (उ + इ → वि); इन्द्रियेषु + अवस्थानम् → इन्द्रियेष्ववस्थानम् (उ + अ → व); "
           "-प्रवृद्धैः + अन्वयः → -प्रवृद्धैरन्वयः (ऐः + स्वर → ऐर्)।"),
    "13": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। ‘विविक्तता’ = अलगाव; ‘खुलापन, रिक्तता’ भी सम्भव। स्रोतस् पारिभाषिक शब्द है, आधुनिक "
           "नाम नहीं दिया गया। सन्धि जाँची: तत्र + आकाशजानि → तत्राकाशजानि (अ + आ → आ); श्रोत्रम् → श्रोत्रं (व्यंजन से पहले म् → ं)।"),
}


# ===================================================================== AIDS
AIDS = {
    "1": {
        "chunks": "अथातो | ऽंगविभागं | शारीरं | व्याख्यास्यामः",
        "sandhi": "अ + अ → आ: अथ + अतः → अथातः · अः + अ → ओ, अ का लोप (ऽ): अतः + अङ्ग → अतोऽङ्ग।",
        "frame": "आरम्भ: अथ अतः (अब, इसलिए) → किसकी व्याख्या: अङ्गविभागम् शारीरम् (शरीर के अंगों का विभाग) → क्रिया: व्याख्यास्यामः (हम व्याख्या करेंगे)।",
    },
    "2": {
        "diagram": {"groups": [
            {"label": "छह अंग (क्रम से)", "items": ["१ शिर (सिर)", "२ अन्तराधि (धड़)", "३-४ दो बाहु (भुजाएँ)",
                                                  "५-६ दो सक्थि (टाँगें)"]}]},
        "chunks": "सकलमपि | शरीरमिमित्युच्यते (पढ़ा: शरीरम् इति उच्यते) | तच्च पुनः षडंगं | शिरोऽन्तराधिद्वौ (पढ़ा: अन्तराधिर् द्वौ) | बाहू सक्थिनीच",
        "sandhi": "त् + च → च्च: तत् + च → तच्च · स्वर से पहले ट् → ड्: षट् + अङ्गम् → षडङ्गम्।",
        "pegs": "हाथ पर गिनो: एक सिर, एक धड़, दो हाथ, दो पैर = छह। (मेरी याद-पद्धति)",
    },
    "3": {
        "chunks": "नेत्रनाभिघ्राणिपादादीनि | त्वस्य | प्रत्यंगानि",
        "sandhi": "उ + अ → व: तु + अस्य → त्वस्य।",
        "frame": "क्या: प्रत्यङ्गानि (छोटे अंग) → किसके: अस्य (इस शरीर के) → कौन: नेत्र, नाभि, घ्राण (नाक; अनुमानित पाठ), पाद आदि।",
    },
    "4": {
        "chain": {"steps": ["महाभूत: महागुणमय", "चेतना से अधिष्ठित", "उनसे अभिनिर्वृत्ति (उत्पत्ति)"]},
        "chunks": "महागुणमयेभ्यश्च | खपवनतेजोजलभूम्यारुनेभ्यो (?) | महाभूतेभ्यश्चेतनाधिष्ठितेभ्यो | ऽभिनिर्वृत्तिः",
        "sandhi": "अस् + घोष व्यंजन → ओ: तेजस् + जल → तेजोजल · अः + अ → ओऽ: -भ्यः + अभि → -भ्योऽभि।",
        "letters": "पाँच नाम छपे क्रम में, पहले अक्षर: ख-प-ते-ज-भू (ख, पवन, तेज, जल, भूमि)। (मेरी याद-पद्धति)",
    },
    "5": {
        "chain": {"steps": ["दृष्ट-अदृष्ट विविध कर्मों के बल से", "भूतों का अनेक-रूप विशेष सन्निवेश",
                            "आकृति, प्रमाण, स्नेह, दीप्ति, स्वर आदि की", "सारूप्य या असारूप्य, अति-बहु प्रकार का"]},
        "chunks": "भूतानामेव च | दृष्टादृष्टविविधकर्मवशात् | अनेकरूपात् सन्निवेशविशेषात् | आकृतिप्रमाणस्नेहदीप्तिस्वरादीनां | "
                  "सारूप्यमसारूप्यं वा | सूक्ष्मस्थूलतारतम्यभेदभिन्नम् | अतिबहुप्रकारं निष्पद्यते",
        "seesaw": "सारूप्य (समानता) ↔ असारूप्य (असमानता) · सूक्ष्म ↔ स्थूल · दृष्ट ↔ अदृष्ट: तीनों जोड़े इसी पंक्ति में।",
    },
    "6": {
        "sandhi": "म् + स्वर: सत्त्वबहुलम् + आकाशम् → सत्त्वबहुलमाकाशम्।",
        "anchors": "आकाश खुला और निर्मल: सत्त्व (निर्मलता का गुण)। (मेरी याद-पद्धति)",
    },
    "7": {
        "sandhi": "अस् + घोष → ओ: रजस् + बहुलः → रजोबहुलः · अः + घोष व्यंजन → ओ: बहुलः + वायुः → बहुलो वायुः।",
        "anchors": "वायु सदा चलती है: रजस् (गति का गुण)। (मेरी याद-पद्धति)",
    },
    "8": {
        "sandhi": "अः + अ → ओ, अ का लोप (ऽ): बहुलः + अग्निः → बहुलोऽग्निः।",
        "anchors": "अग्नि = ‘उभय’, दोनों; पंक्ति दोनों के नाम नहीं लेती। (मेरी याद-पद्धति)",
    },
    "9": {
        "sandhi": "अस् + घोष → ओ: तमस् + बहुलम् → तमोबहुलम् · ब से पहले ं = म्: अंबु = अम्बु।",
        "frame": "किसकी अधिकता: सत्त्व + तमस् → बहुलम् (नपुंसक) → किसमें: अम्बु (जल, नपुंसक)।",
    },
    "10": {
        "sandhi": "अस् + घोष → ओ: तमस् + बहुला → तमोबहुला।",
        "frame": "किसकी अधिकता: तमस् → बहुला (स्त्रीलिंग) → किसमें: भूः (पृथ्वी, स्त्रीलिंग)।",
    },
    "11": {
        "diagram": {"groups": [
            {"label": "चिह्न (क्रम से)", "items": ["१ अप्रतिघात (बाधा न होना)", "२ चलत्व (गतिशीलता)", "३ औष्ण्य (उष्णता)",
                                               "४ द्रवता (बहाव)", "५ काठिन्य (कठोरता)"]}]},
        "chunks": "तेषाम् | अप्रतिघातश्चलत्वमौष्ण्यं | द्रवता काठिन्यम् इति | क्रमाल्लिंगानि",
        "sandhi": "त् + ल → ल्ल: क्रमात् + लिङ्गानि → क्रमाल्लिङ्गानि · अः + च → अश्च: अप्रतिघातः + चलत्वम् → अप्रतिघातश्चलत्वम्।",
        "letters": "पहले अक्षर क्रम से: अ-च-औ-द्र-का। (मेरी याद-पद्धति)",
    },
    "12": {
        "diagram": {"groups": [
            {"label": "अवस्थान", "items": ["श्रोत्र आदि इन्द्रियों में"]},
            {"label": "अन्वय: एक-एक बढ़े हुए विषय (क्रम से)", "items": ["१ शब्द", "२ स्पर्श", "३ रूप", "४ रस", "५ गन्ध"]}]},
        "chunks": "विशेषतश्च | श्रोत्रादिष्विंद्रियेष्ववस्थानं | शब्दस्पर्शरूपरसगंधैरैकैक (पढ़ा: गन्धैः एकैक) | प्रवृद्धैरन्वयः",
        "sandhi": "उ + इ → वि: श्रोत्रादिषु + इन्द्रियेषु → श्रोत्रादिष्विन्द्रियेषु · उ + अ → व: इन्द्रियेषु + अवस्थानम् → इन्द्रियेष्ववस्थानम्।",
    },
    "13": {
        "diagram": {"groups": [
            {"label": "आकाशज (क्रम से)", "items": ["१ श्रोत्र (कान)", "२ शब्द", "३ स्रोतस् (शरीर के मार्ग)", "४ विविक्तता (अलगाव)"]}]},
        "chunks": "तत्राकाशजानि | श्रोत्रं शब्दः | स्रोतांसि विविक्तता च",
        "sandhi": "अ + आ → आ: तत्र + आकाशजानि → तत्राकाशजानि।",
        "anchors": "आकाश = खाली जगह: उसी से कान, शब्द, मार्ग और खालीपन। (मेरी याद-पद्धति)",
    },
}


# ===================================================================== IMAGE_SPECS
IMAGE_SPECS = {
    ("2", "diagram"): {
        "file": "sh5-shadanga-2.svg",
        "alt": ("Numbered mind map of unit 2: the body with six parts (ṣaḍaṅga), in line order: 1 head, 2 trunk "
                "(antarādhi), 3-4 the two arms, 5-6 the two lower limbs."),
        "type": "mermaid",
        "code": ("mindmap\n"
                 "  षडंग शरीर\n"
                 "    १ शिर: सिर\n"
                 "    २ अन्तराधि: धड़\n"
                 "    ३-४ दो बाहु: भुजाएँ\n"
                 "    ५-६ दो सक्थि: टाँगें\n"),
    },
    ("4", "chain"): {
        "file": "sh5-mahabhuta-utpatti-4.svg",
        "alt": ("Flowchart of unit 4: the great elements, made of the great guṇas and presided over by consciousness, "
                "give origination. The five names (space, wind, fire, water, earth) join on a conjectural reading only."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"महागुणमय\"] --> M[\"महाभूत\"]\n"
                 "  C[\"चेतना से अधिष्ठित\"] --> M\n"
                 "  B[\"ख पवन तेज जल भूमि\"] -. \"अनुमानित पाठ\" .-> M\n"
                 "  M --> D[\"अभिनिर्वृत्ति: उत्पत्ति\"]\n"),
    },
    ("5", "chain"): {
        "file": "sh5-sarupya-5.svg",
        "alt": ("Chain of unit 5: through the power of various actions, seen and unseen; the special arrangement of the "
                "elements, of many forms; of form, size, unctuousness, lustre, voice and so on; similarity or "
                "dissimilarity, of very many kinds."),
        "type": "chain",
        "title": "इकाई ५: सारूप्य-असारूप्य कैसे",
        "steps": ["दृष्ट-अदृष्ट विविध कर्मों के बल से", "भूतों का अनेक-रूप विशेष सन्निवेश",
                  "आकृति, प्रमाण, स्नेह, दीप्ति, स्वर आदि की", "सारूप्य या असारूप्य, अति-बहु प्रकार का"],
    },
    ("11", "diagram"): {
        "file": "sh5-bhuta-linga-11.svg",
        "alt": ("Numbered table of unit 11, the marks of the elements in line order: unobstructedness, mobility, heat, "
                "fluidity, hardness. No mark is paired with an element."),
        "type": "table",
        "title": "इकाई ११: भूतों के चिह्न (क्रम से)",
        "heads": ["छपा शब्द", "अर्थ"],
        "rows": [["१ अप्रतिघात", "बाधा न होना"], ["२ चलत्व", "गतिशीलता"], ["३ औष्ण्य", "उष्णता"],
                 ["४ द्रवता", "बहाव"], ["५ काठिन्य", "कठोरता"]],
    },
    ("12", "diagram"): {
        "file": "sh5-indriya-vishaya-12.svg",
        "alt": ("Two columns of unit 12. Abiding: in the sense organs beginning with the ear. Association: with the "
                "objects increased one by one, in line order: sound, touch, form, taste, smell. No object is paired with an organ."),
        "type": "split",
        "title": "इकाई १२: अवस्थान और अन्वय",
        "cols": [["अवस्थान", ["श्रोत्र आदि इन्द्रियों में"]],
                 ["अन्वय: एक-एक बढ़े विषय", ["१ शब्द", "२ स्पर्श", "३ रूप", "४ रस", "५ गन्ध"]]],
    },
    ("13", "diagram"): {
        "file": "sh5-akashaja-13.svg",
        "alt": ("Numbered table of unit 13, what is born of space, in line order: the ear, sound, the channels (srotas), "
                "separateness."),
        "type": "table",
        "title": "इकाई १३: आकाश से उत्पन्न",
        "heads": ["छपा शब्द", "अर्थ"],
        "rows": [["१ श्रोत्रं", "कान"], ["२ शब्दः", "शब्द, ध्वनि"], ["३ स्रोतांसि", "शरीर के मार्ग (स्रोतस्)"],
                 ["४ विविक्तता", "अलगाव"]],
    },
}
