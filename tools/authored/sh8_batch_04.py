from helpers import mcq, match, order, fill, multi, accepts


def T(q, teaches):
    q["teaches"] = teaches
    return q


AUTHORED = {}

# ---------------------------------------------------------------- unit 38
AUTHORED["38"] = {
    "title": "तत्राषोडशाद्वर्षाद्बालं",
    "question": "By unit 38, up to which year does the young age (bāla) last?",
    "rule": ("Of these three ages (तत्र), the young age (बालम्) lasts up to the sixteenth year: आ with the ablative "
             "(आ षोडशात् वर्षात्) means 'up to'."),
    "limits": ("Prose, no verb (the copula is understood). Whether the sixteenth year itself is included is not stated, "
               "so no question rests on it. The three ages are named in unit 37; the next limits come in unit 39."),
    "explain_hi": ("इकाई ३७ ने वय के तीन भेद गिनाए थे: बाल, मध्य और वृद्ध; यहाँ पहले की सीमा है। "
                   "‘तत्र’ यानी उनमें; ‘आ षोडशात् वर्षात्’ यानी सोलहवें वर्ष तक; ‘बालम्’ यानी बाल वय। "
                   "आ के साथ पञ्चमी विभक्ति ‘तक’ का अर्थ देती है। "
                   "सोलहवाँ वर्ष स्वयं शामिल है या नहीं, यह पाठ नहीं बताता। "
                   "सन्धि: तत्र + आ → तत्रा (अ + आ → आ), और षोडशात् तथा वर्षात् का त् घोष ध्वनि से पहले द् बना है।"),
    "hook": "सोलह तक बाल: आ + पञ्चमी = तक।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 38, up to which year does the young age (bāla) last?",
            ("Up to the sixteenth year", "आ षोडशात् वर्षात्: up to the sixteenth year."),
            [("Up to the thirtieth year", "Thirty is the limit of youth (yauvana), a stage of the middle age (unit 44)."),
             ("Up to the twentieth year", "No twenty is named; षोडश is sixteen."),
             ("Up to the sixtieth year", "Sixty ends the middle age (unit 39), not the young age.")],
            "तत्राषोडशाद्वर्षाद्बालं: up to the sixteenth year, the young age.",
            "आ षोडशात् वर्षात् बालम्."),
        order(1, "Put the words of unit 38 in the printed order.",
              ["तत्र", "आ", "षोडशात्", "वर्षात्", "बालम्"],
              "Of these; up to; the sixteenth; year; the young age.",
              "तत्र → आ → षोडशात् → वर्षात् → बालम्."),
        match(2, "Match each word of unit 38 to its meaning.",
              [["तत्र", "of these"], ["आ (with the ablative)", "up to"], ["षोडश", "sixteenth"], ["वर्ष", "year"],
               ["बाल", "young (age)"]],
              "तत्र = of these; आ + ablative = up to; षोडशात् वर्षात् = the sixteenth year; बालम् = the young age.",
              "तत्र, आ, षोडश, वर्ष, बाल.", role="extend",
              teaches="आ with the ablative gives 'up to': आ षोडशात् वर्षात् = up to the sixteenth year."),
        mcq("discriminate", 3, "Which split of the printed तत्राषोडशाद् is right?",
            ("तत्र + आ + षोडशात्", "अ + आ → आ: तत्र + आ → तत्रा; then षोडशात् (its त् → द् before व)."),
            [("तत्रा + षोडशात्", "तत्रा is not a word; the word is तत्र, and आ (up to) is a word of its own."),
             ("तत्र + षोडशात्", "Without आ the join would be तत्र षोडशात्, with a short अ."),
             ("तत् + राषोडशात्", "राषोडशात् is not a word; तत्र is one word.")],
            "तत्र (of these) + आ (up to) + षोडशात् (the sixteenth).",
            "अ + आ → आ."),
        mcq("apply", 4, "Why is वर्षात् printed वर्षाद् before बालं?",
            ("त् before the voiced ब → द्", "ब is a voiced consonant: वर्षात् + बालम् → वर्षाद्बालम्."),
            [("त् before any consonant → द्", "Not before every consonant: before a voiceless one such as क or प, त् stays."),
             ("बालम् begins with a vowel", "बालम् begins with the consonant ब, not with a vowel."),
             ("The ablative always ends in -आद्", "At a pause the ablative ends in -आत्; -आद् comes from sandhi.")],
            "वर्षात् + बालम्: त् before a voiced consonant → द्.",
            "त् + voiced sound (not a nasal) → द्."),
        mcq("transfer", 5, "By the pattern of आ षोडशात् (up to the sixteenth), which phrase means up to the ocean, in a new example?",
            ("आ समुद्रात्", "आ with the ablative (-आत्) = up to: up to the ocean."),
            [("आ समुद्रम्", "समुद्रम् is accusative; 'up to' with आ takes the ablative."),
             ("आ समुद्रे", "समुद्रे is locative: in the ocean."),
             ("आ समुद्रेण", "समुद्रेण is instrumental: by the ocean.")],
            "आ समुद्रात् = up to the ocean, like आ षोडशात् = up to the sixteenth.",
            "आ + ablative = up to.",
            teaches="आ with the ablative marks a limit, 'up to': आ षोडशात् वर्षात्, आ समुद्रात्."),
    ],
}

# ---------------------------------------------------------------- unit 39
AUTHORED["39"] = {
    "title": "आषष्टेर्मध्यमं ततो वृद्धं",
    "question": "By unit 39, where does the middle age end, and what follows it?",
    "rule": ("Up to sixty (आ षष्टेः) is the middle age (मध्यमम्); after that (ततः), the old age (वृद्धम्). The count "
             "in years is carried from unit 38 (वर्षात्)."),
    "limits": ("Prose, no verb. The line itself names only the upper limit, sixty; 'years' is not repeated. Whether the "
               "sixtieth year is included is not stated. The stages of the middle age come in units 42 and 44."),
    "explain_hi": ("बाल वय के बाद यहाँ मध्य और वृद्ध की सीमा है। "
                   "‘आ षष्टेः’ यानी साठ तक: तब तक मध्यम वय; ‘ततः’ यानी उसके बाद वृद्ध वय। "
                   "‘वर्ष’ शब्द यहाँ फिर नहीं आता, वह इकाई ३८ से समझा जाता है। "
                   "सन्धि: षष्टेः का विसर्ग ए के बाद, घोष म से पहले र् बना (षष्टेर्मध्यमं); ततः का विसर्ग अ के बाद घोष व्यंजन व से पहले ओ बना (ततो वृद्धं)।"),
    "hook": "साठ तक मध्य, ततो वृद्ध।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 39, which age comes after sixty?",
            ("The old age", "ततो वृद्धम्: after that, the old age."),
            [("The middle age", "The middle age lasts up to sixty (आ षष्टेः मध्यमम्)."),
             ("The young age", "The young age lasts up to sixteen (unit 38)."),
             ("A fourth age", "Only three ages are named (unit 37); after sixty comes the old age.")],
            "आषष्टेर्मध्यमं ततो वृद्धं: up to sixty the middle, then the old age.",
            "ततः (after that) वृद्धम्."),
        order(1, "Put the words of unit 39 in the printed order.",
              ["आ", "षष्टेः", "मध्यमम्", "ततः", "वृद्धम्"],
              "Up to; sixty; the middle age; after that; the old age.",
              "आ → षष्टेः → मध्यमम् → ततः → वृद्धम्."),
        match(2, "Match each word of unit 39 to its meaning.",
              [["षष्टि", "sixty"], ["मध्यम", "middle (age)"], ["ततः", "after that"], ["वृद्ध", "old (age)"]],
              "आ षष्टेः = up to sixty; मध्यमम् = the middle age; ततः = after that; वृद्धम् = the old age.",
              "षष्टि, मध्यम, ततः, वृद्ध.", role="extend",
              teaches="षष्टि (sixty) is a feminine i-stem; its ablative singular षष्टेः goes with आ: up to sixty."),
        mcq("discriminate", 3, "Why is षष्टेः printed षष्टेर् before मध्यमं?",
            ("After ए, visarga before a voiced sound → र्", "म is voiced; after a vowel other than अ/आ the visarga becomes र्."),
            [("After any vowel, visarga before म → र्", "Not after अ: ततः before व gives ततो in this same line."),
             ("Visarga before every consonant → र्", "Not before every one: before a voiceless त it becomes स्."),
             ("The र् belongs to the word मध्यमम्", "The word is मध्यमम्; the र् comes from the visarga of षष्टेः.")],
            "षष्टेः + मध्यमम्: एः before a voiced consonant → एर्.",
            "इः, उः, एः ... (not अः/आः) + voiced sound → र्."),
        mcq("apply", 4, "Why is ततः printed ततो before वृद्धं?",
            ("अः before a voiced consonant → ओ", "व is a voiced consonant: ततः + वृद्धम् → ततो वृद्धम्."),
            [("आः before a voiced consonant → ओ", "The vowel is a short अ (त-तः); आः would drop its visarga."),
             ("अः before any consonant → ओ", "Not before every consonant: before त it becomes स्."),
             ("ओ is a case ending added to ततः", "ततः is an indeclinable (gram: ind.); it takes no ending.")],
            "ततः + वृद्धम्: अः before the voiced consonant व → ओ.",
            "अः + voiced consonant → ओ."),
        mcq("transfer", 5, "By the rule of ततो वृद्धं, how is ततः + गच्छति (then he goes) joined in a new example?",
            ("ततो गच्छति", "ग is a voiced consonant: अः before it → ओ, as ततः + वृद्धम् → ततो वृद्धम्."),
            [("ततर् गच्छति", "र् comes after vowels other than अ/आ; ततः has अ."),
             ("ततस् गच्छति", "स् comes before a voiceless त or थ, not before ग."),
             ("तता गच्छति", "The visarga does not lengthen अ to आ.")],
            "ततः + गच्छति = ततो गच्छति, like ततो वृद्धं.",
            "अः + voiced consonant → ओ.",
            teaches="After a short अ, a visarga before a voiced consonant becomes ओ: ततो वृद्धम्, ततो गच्छति."),
    ],
}

# ---------------------------------------------------------------- unit 40
AUTHORED["40"] = {
    "title": "तेष्वपि स्तन्याहारोभयवृत्त्या बालं त्रिविधं",
    "question": "By unit 40, how is the young age divided, and what marks it?",
    "rule": ("Among these, the young age is threefold by mode of living: on breast-milk (स्तन्य), on food (आहार), on "
             "both (उभय). In it: growth in the size of the body, and predominance of śleṣman (Kapha)."),
    "limits": ("Prose; joins two printed lines, no verb. The three kinds are not given names of their own; only the mode "
               "of living is stated. उभय = both (breast-milk and food together). श्लेष्मन् is here the name of Kapha "
               "(standard). Printed बालंत्रिविधं is two words joined in print (बालम् त्रिविधम्)."),
    "explain_hi": ("बाल वय भी तीन प्रकार का है, जीविका यानी पोषण के ढंग से: स्तन्य (माँ का दूध) पर, आहार पर, और दोनों पर। "
                   "इन तीनों के अलग नाम पाठ में नहीं हैं, केवल पोषण का ढंग कहा गया है। "
                   "उस (बाल वय) में शरीर के परिमाण की वृद्धि होती है और श्लेष्मा यानी कफ की अधिकता रहती है। "
                   "‘स्तन्याहारोभय’ में स्तन्य + आहार (अ + आ → आ) और आहार + उभय (अ + उ → ओ) की सन्धि है। "
                   "छपा ‘बालंत्रिविधं’ दो शब्द हैं, छपाई में जुड़े हुए।"),
    "hook": "दूध, अन्न या दोनों: बाल बढ़ता है, कफ बढ़ा रहता है।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 40, what grows in the young age?",
            ("The size of the body", "देहप्रमाणवृद्धिः: growth in the size (measure) of the body."),
            [("The power of the agni", "A kindled agni is named for the middle age (unit 43)."),
             ("The memory and speech", "Fullness of memory and speech is named up to forty (unit 44)."),
             ("The skin's roughness", "Roughness of the skin is named for the old age (unit 46).")],
            "तस्मिन् देहप्रमाणवृद्धिः: in it, growth in the size of the body.",
            "देह-प्रमाण-वृद्धि = growth of body size."),
        order(1, "Put the phrases of unit 40 in the printed order.",
              ["तेष्वपि", "स्तन्याहारोभयवृत्त्या", "बालंत्रिविधं", "तस्मिन्", "देहप्रमाणवृद्धिः", "श्लेष्मोद्रेकश्च"],
              "Among these also; by living on breast-milk, food or both; the young age is threefold; in it; growth of body size; and predominance of śleṣman.",
              "Division first, then the marks: तेष्वपि → ... → श्लेष्मोद्रेकश्च."),
        match(2, "Match each word of unit 40 to its meaning.",
              [["स्तन्य", "breast-milk"], ["आहार", "food"], ["उभय", "both"], ["वृत्ति", "mode of living"],
               ["उद्रेक", "predominance"]],
              "स्तन्य-आहार-उभय-वृत्त्या = by living on breast-milk, food or both; श्लेष्म-उद्रेक = predominance of śleṣman.",
              "स्तन्य, आहार, उभय, वृत्ति, उद्रेक.", role="extend",
              teaches="वृत्त्या (instrumental of वृत्ति) gives the basis of the division: 'by mode of living'."),
        mcq("discriminate", 3, "Which split of स्तन्याहारोभय is right?",
            ("स्तन्य + आहार + उभय", "अ + आ → आ (स्तन्याहार), अ + उ → ओ (आहारोभय)."),
            [("स्तन्या + हार + उभय", "स्तन्या is not the word; the stem is स्तन्य, and the आ belongs to आहार."),
             ("स्तन्य + आहार + ओभय", "ओभय is not a word; the ओ comes from अ + उ of उभय."),
             ("स्तन्य + आहारो + भय", "आहारो is not a stem; भय (fear) makes no sense here.")],
            "स्तन्य (breast-milk) + आहार (food) + उभय (both).",
            "अ + आ → आ; अ + उ → ओ."),
        multi("apply", 4, "Which statements fit unit 40?",
              [("The three kinds are given names of their own", "Not so: only the mode of living is stated, no names."),
               ("Śleṣman (Kapha) predominates in the young age", "Right: श्लेष्मोद्रेकः."),
               ("The division rests on the mode of living", "Right: स्तन्याहारोभयवृत्त्या, by living on milk, food or both."),
               ("Pitta predominates in the young age", "Pitta predominates in the middle age (unit 43)."),
               ("उभय means living on both milk and food", "Right: उभय = both (breast-milk and food together).")],
              [1, 2, 4],
              "Threefold by mode of living (milk, food, both); in it, growth of the body and predominance of śleṣman.",
              "स्तन्याहारोभयवृत्त्या बालं त्रिविधं; तस्मिन् देहप्रमाणवृद्धिः श्लेष्मोद्रेकश्च."),
        mcq("transfer", 5, "By the rule of आहार + उभय → आहारोभय, how is सूर्य + उदयः (sunrise) joined in a new example?",
            ("सूर्योदयः", "अ + उ → ओ: सूर्य + उदयः → सूर्योदयः."),
            [("सूर्यौदयः", "औ comes from अ + ओ or औ, not from अ + उ."),
             ("सूर्येदयः", "ए comes from अ + इ, not from अ + उ."),
             ("सूर्यूदयः", "ऊ comes from उ + उ; here the first vowel is अ.")],
            "सूर्य + उदयः = सूर्योदयः, like आहार + उभय = आहारोभय.",
            "अ + उ → ओ.",
            teaches="A final अ before उ joins into ओ: आहार + उभय → आहारोभय, सूर्य + उदयः → सूर्योदयः."),
    ],
}

# ---------------------------------------------------------------- unit 41
AUTHORED["41"] = {
    "title": "तेन बालस्य स्नेहमार्दव...",
    "question": "By unit 41, which qualities arise in the young age, and from what?",
    "rule": ("Because of that (तेन), in the young age there are sneha (unctuousness, or affection), softness (मार्दव), delicacy "
             "(सौकुमार्य), little anger (अल्पक्रोधत्व) and good fortune (सौभाग्य)."),
    "limits": ("Prose. स्नेह may be bodily unctuousness (the data's reading, from the Kapha of unit 40) or affection; "
               "no question rests on its sense. बालस्य may be 'of the young age' or 'of the child'; no question rests on that."),
    "explain_hi": ("‘तेन’ यानी उससे; डेटा इसे इकाई ४० की कफ-अधिकता का फल पढ़ता है। "
                   "बाल वय में पाँच बातें होती हैं: स्नेह, मार्दव (कोमलता), सौकुमार्य (सुकुमारता), अल्प क्रोध और सौभाग्य। "
                   "‘स्नेह’ के दो अर्थ हो सकते हैं: शरीर का चिकनापन या प्रेम; डेटा पहला लेता है। "
                   "‘अल्पक्रोधत्व’ में -त्व भाववाचक है: क्रोध का कम होना। "
                   "‘बालस्य’ का अर्थ ‘बाल वय में’ या ‘बालक का’, दोनों सम्भव हैं।"),
    "hook": "कफ से: चिकना, कोमल, सुकुमार, कम क्रोध, सौभाग्य।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 41, which of these is listed for the young age?",
            ("Little anger", "अल्पक्रोधत्व: the state of little anger."),
            [("Great anger", "The compound says अल्प-क्रोध: little anger, not great."),
             ("Rough skin", "Roughness of the skin is named for the old age (unit 46)."),
             ("Firm resolve", "Determination (vyavasāya) is named for the middle age (unit 43).")],
            "स्नेह, मार्दव, सौकुमार्य, अल्पक्रोधत्व, सौभाग्य.",
            "अल्प-क्रोध-त्व = little anger."),
        order(1, "Put the five qualities of unit 41 in the printed order.",
              ["स्नेह", "मार्दव", "सौकुमार्य", "अल्पक्रोधत्व", "सौभाग्य"],
              "Sneha, softness, delicacy, little anger, good fortune.",
              "स्नेह → मार्दव → सौकुमार्य → अल्पक्रोधत्व → सौभाग्य."),
        match(2, "Match each word of unit 41 to its meaning.",
              [["मार्दव", "softness"], ["सौकुमार्य", "delicacy"], ["अल्प", "little"], ["क्रोध", "anger"],
               ["सौभाग्य", "good fortune"]],
              "मार्दव = softness, सौकुमार्य = delicacy, अल्प-क्रोध = little anger, सौभाग्य = good fortune.",
              "मार्दव, सौकुमार्य, अल्प, क्रोध, सौभाग्य.", role="extend",
              teaches="-त्व makes an abstract noun: अल्प-क्रोध-त्व = the state of having little anger."),
        mcq("discriminate", 3, "Which split of सौकुमार्याल्प (in the printed compound) is right?",
            ("सौकुमार्य + अल्प", "अ + अ → आ: सौकुमार्य + अल्प → सौकुमार्याल्प."),
            [("सौकुमारी + अल्प", "ई + अ gives य: that would be सौकुमार्यल्प, with a short अ."),
             ("सौकुमार्य + इल्प", "इल्प is not a word, and अ + इ gives ए."),
             ("सौकुमार्यः + अल्प", "No visarga stands inside a compound; अः + अ would give ओऽ.")],
            "सौकुमार्य (delicacy) + अल्प (little): अ + अ → आ.",
            "अ + अ → आ."),
        multi("apply", 4, "Which statements fit unit 41?",
              [("Softness (mārdava) is one of the listed qualities", "Right: मार्दव."),
               ("The unit names Pitta as the cause", "Pitta belongs to the middle age (unit 43); the data reads तेन as the Kapha of unit 40."),
               ("स्नेह here can only mean affection", "Not so: it may be unctuousness (the data's reading) or affection."),
               ("The qualities stand in the nominative plural with भवन्ति", "Right: ...सौभाग्यानि भवन्ति, they arise.")],
              [0, 3],
              "Five qualities, nominative plural with भवन्ति; स्नेह has two possible senses.",
              "...सौभाग्यानि भवंति."),
        mcq("transfer", 5, "By -त्व in अल्पक्रोधत्व, which word means the state of being a child, in a new example?",
            ("बालत्वम्", "-त्व makes an abstract noun: बाल-त्वम् = childhood, the state of being a child."),
            [("बालतरम्", "-तर makes a comparative: younger."),
             ("बालवत्", "-वत् means 'like': like a child."),
             ("बालकम्", "बालक is a noun, 'a child', not the state of being one.")],
            "बालत्वम् = the state of being a child, like अल्पक्रोधत्व = the state of little anger.",
            "X-त्व = the state of being X.",
            teaches="The suffix -त्व forms an abstract noun, 'the state of': अल्पक्रोधत्व, बालत्वम्."),
    ],
}

# ---------------------------------------------------------------- unit 42
AUTHORED["42"] = {
    "title": "मध्यमपि त्रिविधं",
    "question": "By unit 42, what are the three stages of the middle age?",
    "rule": ("The middle age also is threefold: youth (यौवन), fullness (सम्पूर्णत्व) and non-decline (अपरिहानि). "
             "Their limits are given in unit 44."),
    "limits": ("Prose, no verb. The stages are only named here; their years come in unit 44. मध्यम् is the printed "
               "neuter form (also in unit 37), not a slip for मध्यमम्."),
    "explain_hi": ("बाल वय की तरह मध्य वय भी तीन प्रकार का है। "
                   "उसके तीन चरण: यौवन, सम्पूर्णत्व यानी पूर्णता, और अपरिहानि यानी ह्रास का न होना। "
                   "इनकी वर्ष-सीमाएँ इकाई ४४ में हैं। "
                   "‘मध्यमपि’ में मध्यम् + अपि है: स्वर से पहले अन्तिम म् म् ही लिखा जाता है, ं नहीं; यह छपाई की भूल नहीं। "
                   "‘अपरिहानि’ में अ निषेध करता है: परिहानि (ह्रास) का न होना।"),
    "hook": "मध्य के तीन: यौवन, पूर्णता, अपरिहानि।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 42, which stage of the middle age is named first?",
            ("Youth (yauvana)", "यौवनम् comes first, then सम्पूर्णत्वम् and अपरिहानिः."),
            [("Fullness (sampūrṇatva)", "Fullness is named second."),
             ("Non-decline (aparihāni)", "Non-decline is named third."),
             ("Childhood (bālya)", "Childhood belongs to the young age, not to the middle age.")],
            "यौवनं संपूर्णत्वमपरिहानिश्च: youth, fullness, non-decline.",
            "यौवन → सम्पूर्णत्व → अपरिहानि."),
        order(1, "Put the printed parts of unit 42 in order.",
              ["मध्यमपि", "त्रिविधं", "यौवनं", "संपूर्णत्वम्", "अपरिहानिश्च"],
              "The middle (age) also; threefold; youth; fullness; and non-decline.",
              "मध्यमपि → त्रिविधं → यौवनं → संपूर्णत्वम् → अपरिहानिश्च."),
        match(2, "Match each word of unit 42 to its meaning.",
              [["यौवन", "youth"], ["सम्पूर्णत्व", "fullness"], ["अपरिहानि", "non-decline"], ["त्रिविध", "threefold"]],
              "त्रिविधम् = threefold: यौवन (youth), सम्पूर्णत्व (fullness), अपरिहानि (non-decline).",
              "यौवन, सम्पूर्णत्व, अपरिहानि, त्रिविध.", role="extend",
              teaches="अ- before a noun negates it: अ-परिहानि = non-decline (परिहानि = decline)."),
        mcq("discriminate", 3, "Which split of संपूर्णत्वमपरिहानिश्च is right?",
            ("सम्पूर्णत्वम् + अपरिहानिः + च", "म् before a vowel stays म्; इः before च → इश्."),
            [("सम्पूर्णत्वम् + परिहानिः + च", "Without अ it would be printed संपूर्णत्वं परिहानिश्च, and mean decline."),
             ("सम्पूर्णत्व + मपरिहानिः + च", "मपरिहानि is not a word; the म् ends सम्पूर्णत्वम्."),
             ("सम्पूर्णत्वम् + अपरिहानेः + च", "एः before च would give अपरिहानेश्च, with ए.")],
            "सम्पूर्णत्वम् (fullness) + अपरिहानिः (non-decline) + च (and).",
            "Final म् + vowel: म् stays; visarga + च → श्."),
        mcq("apply", 4, "In मध्यमपि, why is the final म् of मध्यम् written as म् and not as ं?",
            ("It stands before a vowel", "It stands before अपि; a final म् before a vowel is written म् and joins it: मध्यम् + अपि."),
            [("It stands before a consonant", "Before a consonant inside a sentence it would be written ं."),
             ("It stands at the end of a line", "अपि follows it in the same line."),
             ("It is a misprint for मध्यमं", "The data finds no typo: this is the regular writing.")],
            "मध्यम् + अपि → मध्यमपि.",
            "Final म् + vowel → म् (joined)."),
        mcq("transfer", 5, "By the pattern of अ-परिहानि (non-decline), what does अक्रोध mean in a new example?",
            ("Absence of anger", "अ- negates: अ-क्रोध = no anger, as अ-परिहानि = no decline."),
            [("Excess of anger", "Excess would need a word like अधिक or उद्रेक."),
             ("Return of anger", "Nothing in अ- means 'return'."),
             ("Cause of anger", "अ- negates; it does not mean 'cause'.")],
            "अक्रोध = absence of anger, like अपरिहानि = absence of decline.",
            "अ- + noun = absence of it.",
            teaches="The prefix अ- (before a consonant) negates a noun: अपरिहानि, अक्रोध."),
    ],
}

# ---------------------------------------------------------------- unit 43
AUTHORED["43"] = {
    "title": "तस्मिन् पित्तोद्रेकः",
    "question": "By unit 43, which doṣa predominates in the middle age, and what follows from it?",
    "rule": ("In it (the middle age, after unit 42), predominance of Pitta; because of that, a kindled agni (दीप्ताग्निता), "
             "abundance of understanding (प्रज्ञा) and ripening (परिपाक), and determination (व्यवसाय)."),
    "limits": ("Prose, no verb. परिपाक may mean ripening (maturity) or digestion; the sense is not fixed, so no question "
               "rests on it. तस्मिन् is read as the middle age because it follows unit 42. Printed तेनदीप्ताग्निता joins two words."),
    "explain_hi": ("मध्य वय में पित्त की अधिकता रहती है। "
                   "उससे (तेन): अग्नि यानी पाचन-अग्नि का प्रदीप्त होना, प्रज्ञा यानी समझ की अधिकता, परिपाक, और व्यवसाय यानी दृढ़ निश्चय। "
                   "‘परिपाक’ का अर्थ परिपक्वता या पाचन, दोनों हो सकता है; डेटा अर्थ तय नहीं करता। "
                   "‘प्रज्ञाधिक्यपरिपाकौ’ द्विवचन है: दो बातें, प्रज्ञा की अधिकता और परिपाक। "
                   "‘दीप्ताग्निता’ में -ता भाववाचक है: प्रदीप्त अग्नि वाला होना।"),
    "hook": "मध्य में पित्त: तेज़ अग्नि, तेज़ बुद्धि, दृढ़ निश्चय।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 43, what follows from the predominance of Pitta?",
            ("A kindled digestive fire", "तेन दीप्ताग्निता: because of that, a kindled agni."),
            [("Growth in the size of the body", "Growth of body size marks the young age (unit 40)."),
             ("Wasting of all the dhātus", "Wasting of the dhātus marks the old age (unit 46)."),
             ("Softness and delicacy", "Softness and delicacy mark the young age (unit 41).")],
            "पित्तोद्रेकः तेन दीप्ताग्निता...",
            "पित्त-उद्रेक → दीप्त-अग्नि."),
        order(1, "Put the items of unit 43 in the printed order.",
              ["पित्तोद्रेकः", "दीप्ताग्निता", "प्रज्ञाधिक्य", "परिपाक", "व्यवसायः"],
              "Predominance of Pitta; kindled agni; abundance of understanding; ripening; determination.",
              "Cause first (पित्तोद्रेकः), then its four results."),
        match(2, "Match each word of unit 43 to its meaning.",
              [["उद्रेक", "predominance"], ["दीप्त", "kindled"], ["अग्नि", "digestive fire"], ["प्रज्ञा", "understanding"],
               ["व्यवसाय", "determination"]],
              "पित्त-उद्रेक, दीप्त-अग्नि-ता, प्रज्ञा-आधिक्य, व्यवसाय.",
              "उद्रेक, दीप्त, अग्नि, प्रज्ञा, व्यवसाय.", role="extend",
              teaches="तेन (by that) links the cause to its results: Pitta's predominance → kindled agni and the rest."),
        mcq("discriminate", 3, "प्रज्ञाधिक्यपरिपाकौ ends in -औ. What number does it show here?",
            ("Dual: two items", "Gram: nom. dual: abundance of prajñā, and paripāka."),
            [("Plural: three or more", "The plural of an a-stem ends in -आः, not -औ."),
             ("Singular: one item", "The singular nominative ends in -अः; -औ is the dual."),
             ("No number: an indeclinable", "It is a declined compound (nom. dual), not an indeclinable.")],
            "प्रज्ञाधिक्य + परिपाक, two items: hence the dual -औ.",
            "a-stem, nominative dual: -औ."),
        mcq("apply", 4, "What does दीप्ताग्निता mean in unit 43?",
            ("The state of having a kindled agni", "दीप्त (kindled) + अग्नि + -ता (the state of)."),
            [("The state of having a weak agni", "दीप्त means kindled, the opposite of weak."),
             ("The state of having a hot skin", "The word names agni, the digestive fire, not the skin."),
             ("The state of having a fiery anger", "The word names agni, not anger.")],
            "दीप्ताग्निता = the state of having a kindled agni.",
            "X-ता = the state of X."),
        mcq("transfer", 5, "By -ता in दीप्ताग्निता, which word means firmness (the state of being firm), in a new example?",
            ("दृढता", "-ता makes an abstract noun: दृढ-ता = firmness."),
            [("दृढतर", "-तर makes a comparative: firmer."),
             ("दृढवत्", "-वत् means 'like': like a firm one."),
             ("दृढेन", "दृढेन is an instrumental: by the firm one.")],
            "दृढता = firmness, like दीप्ताग्निता = the state of a kindled agni.",
            "X-ता = the state of X.",
            teaches="The suffix -ता (feminine) forms an abstract noun, 'the state of': दीप्ताग्निता, दृढता."),
    ],
}

# ---------------------------------------------------------------- unit 44
AUTHORED["44"] = {
    "title": "तत्रात्रिंशतो यौवनम्",
    "question": "By unit 44, what are the year-limits of the three stages of the middle age?",
    "rule": ("Up to thirty, youth (यौवन); up to forty, fullness of all the dhātus, sense-organs, strength, vigour (वीर्य), "
             "manliness, memory, speech, knowledge and the like; after this (अतः परम्), non-decline (अपरिहानि)."),
    "limits": ("Prose, no verb. Only end points are given. The printed प्रश्नय is no word; प्रश्रय (humility) is a conjecture, "
               "so no question rests on it. The end of non-decline (sixty) comes from unit 39, as the data notes. The exact "
               "scope of गुण is left open."),
    "explain_hi": ("यहाँ इकाई ४२ के तीन चरणों की सीमाएँ हैं। "
                   "तीस तक यौवन; चालीस तक सभी धातुओं, इन्द्रियों, बल, वीर्य यानी शक्ति, पौरुष, स्मरण, वचन, विज्ञान आदि गुणों की पूर्णता; उसके बाद अपरिहानि। "
                   "अपरिहानि का अन्त साठ पर है, जो इकाई ३९ से आता है। "
                   "छपा ‘प्रश्नय’ कोई शब्द नहीं; ‘प्रश्रय’ (विनय) अनुमानित पाठ है, इस पर कोई प्रश्न नहीं। "
                   "‘धात्विन्द्रिय’ में धातु + इन्द्रिय है: उ के बाद भिन्न स्वर आने पर उ → व्।"),
    "hook": "तीस तक यौवन, चालीस तक पूर्णता, फिर (साठ तक) अपरिहानि।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 44, up to which year does youth (yauvana) last?",
            ("Up to thirty", "आ त्रिंशतः यौवनम्: up to thirty, youth."),
            [("Up to forty", "Forty ends fullness (sampūrṇatva), the next stage."),
             ("Up to sixty", "Sixty ends the middle age as a whole (unit 39)."),
             ("Up to twenty", "No twenty is named in this account.")],
            "तत्रात्रिंशतो यौवनम्: up to thirty, youth.",
            "आ त्रिंशतः = up to thirty."),
        order(1, "Put these sure items of the list in unit 44 in the printed order.",
              ["धातु", "इन्द्रिय", "बल", "वीर्य", "पौरुष", "स्मरण"],
              "dhātus, sense-organs, strength, vigour, manliness, memory (then speech, knowledge ...).",
              "सर्वधात्विंद्रियबलवीर्यपौरुषस्मरण..."),
        match(2, "Match each word of unit 44 to its meaning.",
              [["त्रिंशत्", "thirty"], ["चत्वारिंशत्", "forty"], ["यौवन", "youth"], ["अतः परम्", "after this"],
               ["स्मरण", "memory"]],
              "आ त्रिंशतः यौवनम्; आ चत्वारिंशतः ... सम्पूर्णत्वम्; अतः परम् अपरिहानिः.",
              "त्रिंशत्, चत्वारिंशत्, यौवन, अतः परम्, स्मरण.", role="extend",
              teaches="त्रिंशत् and चत्वारिंशत् are feminine t-stems; their ablative -तः goes with आ: up to thirty, up to forty."),
        mcq("discriminate", 3, "By unit 44, which stage ends at forty?",
            ("Fullness (sampūrṇatva)", "आ चत्वारिंशतः ... सम्पूर्णत्वम्: up to forty, fullness."),
            [("Youth (yauvana)", "Youth ends at thirty."),
             ("Non-decline (aparihāni)", "Non-decline comes after this (अतः परम्)."),
             ("The young age (bāla)", "The young age ends at sixteen (unit 38).")],
            "Thirty: youth; forty: fullness; after: non-decline.",
            "आ चत्वारिंशतः सम्पूर्णत्वम्."),
        multi("apply", 4, "Which of these are named in unit 44 among the qualities that are full up to forty?",
              [("Memory (smaraṇa)", "Right: स्मरण is in the list."),
               ("Speech (vacana)", "Right: वचन is in the list."),
               ("Wrinkles (valī)", "Wrinkles are named for the old age (unit 45)."),
               ("Sense-organs (indriya)", "Right: इन्द्रिय is in the list."),
               ("Cough (kāsa)", "Cough is named for the old age (units 45 and 46).")],
              [0, 1, 3],
              "dhātu, indriya, bala, vīrya, pauruṣa, smaraṇa, vacana, vijñāna ... are full up to forty.",
              "सर्वधात्विंद्रियबलवीर्यपौरुषस्मरणवचनविज्ञान..."),
        mcq("transfer", 5, "By the rule of धातु + इन्द्रिय → धात्विन्द्रिय, how is मधु + इव (like honey) joined in a new example?",
            ("मध्विव", "उ before a different vowel → व्: मधु + इव → मध्विव."),
            [("मधूव", "ऊ comes from उ + उ; here the second vowel is इ."),
             ("मधेव", "ए comes from अ + इ; मधु ends in उ."),
             ("मधविव", "उ becomes व् alone; no अ is added.")],
            "मधु + इव = मध्विव, like धातु + इन्द्रिय = धात्विन्द्रिय.",
            "उ + a different vowel → व् + that vowel.",
            teaches="A final उ before a different vowel becomes व्: धातु + इन्द्रिय → धात्विन्द्रिय, मधु + इव → मध्विव."),
    ],
}

# ---------------------------------------------------------------- unit 45
AUTHORED["45"] = {
    "title": "वृद्धं तु श्वः श्वः क्षीयमाण...",
    "question": "By unit 45, how does the old age decline, and to what is it likened?",
    "rule": ("The old age, its qualities of dhātus, senses and the rest wasting day after day (श्वः श्वः), overcome by "
             "wrinkles, khalita, cough, breathlessness, weak agni and the like, sinks down like an old house rained upon."),
    "limits": ("Prose. खलित = baldness is probable (it can also mean stumbling): no question rests on its sense. जीर्ण here "
               "qualifies भवन (old, decayed), not 'digested'. The old age is the subject of अवसीदति; the house is the simile."),
    "explain_hi": ("वृद्ध वय में धातु, इन्द्रिय आदि के गुण दिन-प्रतिदिन (श्वः श्वः, ‘कल-कल’) घटते जाते हैं। "
                   "झुर्रियाँ (वली), खलित (सम्भावित: गंजापन), खाँसी (कास), श्वास यानी साँस फूलना, अग्नि की मन्दता आदि उसे दबाते हैं। "
                   "तब वृद्ध अवस्था वर्षा से भीगे पुराने घर की तरह बैठ जाती है: यह पाठ की अपनी उपमा है। "
                   "‘जीर्ण’ यहाँ घर का विशेषण है (पुराना, जर्जर), ‘पचा हुआ’ नहीं। "
                   "सन्धि: भवनम् + इव → भवनमिव (स्वर से पहले म्), इव + अभिवृष्टम् → इवाभिवृष्टम् (अ + अ → आ)।"),
    "hook": "रोज़ घटता, रोगों से दबा: बरसात में पुराना घर बैठ जाए।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 45, what is the old age likened to?",
            ("An old house rained upon", "जीर्णं भवनम् इव अभिवृष्टम्: like an old house rained upon."),
            [("A tree shaken by a storm", "No tree or storm is in the line; the simile is a house."),
             ("A lamp running out of oil", "No lamp is in the line; the simile is a house."),
             ("A river drying in summer", "No river is in the line; the simile is a house.")],
            "जीर्णं भवनमिवाभिवृष्टमवसीदति: sinks down like an old house rained upon.",
            "भवनम् इव = like a house."),
        order(1, "Put the afflictions of unit 45 in the printed order.",
              ["वली", "खलित", "कास", "श्वास", "अग्निसाद"],
              "Wrinkles, khalita (probably baldness), cough, breathlessness, weak agni, and the like.",
              "वली → खलित → कास → श्वास → अग्निसाद (आदि)."),
        match(2, "Match each word of unit 45 to its meaning.",
              [["वली", "wrinkle"], ["कास", "cough"], ["श्वास", "breathlessness"], ["भवन", "house"],
               ["अवसीदति", "sinks down"]],
              "वली, कास, श्वास overcome the old age; it sinks down (अवसीदति) like a house (भवन).",
              "वली, कास, श्वास, भवन, अवसीदति.", role="extend",
              teaches="अव-√सद् = to sink down, collapse: अवसीदति, 'it sinks down'."),
        mcq("discriminate", 3, "What does श्वः श्वः mean in unit 45?",
            ("Day after day", "श्वः = tomorrow; repeated, 'tomorrow, tomorrow' = day after day."),
            [("Only tomorrow", "The word is repeated: a steady day-by-day wasting."),
             ("Breath by breath", "श्वः is 'tomorrow', not श्वास (breath)."),
             ("Since yesterday", "Yesterday is ह्यः, not श्वः.")],
            "श्वः श्वः क्षीयमाण...: wasting day after day.",
            "श्वः श्वः = day after day."),
        mcq("apply", 4, "Which split of इवाभिवृष्टम् (printed भवनमिवाभिवृष्टम्) is right?",
            ("इव + अभिवृष्टम्", "अ + अ → आ: इव + अभिवृष्टम् → इवाभिवृष्टम्."),
            [("इवा + भिवृष्टम्", "इवा and भिवृष्टम् are not words; इव is 'like'."),
             ("इव + भिवृष्टम्", "Without अ the join would be इव भिवृष्टम्, with a short अ."),
             ("इव + उभिवृष्टम्", "अ + उ gives ओ, and उभिवृष्टम् is not a word.")],
            "इव (like) + अभिवृष्टम् (rained upon): अ + अ → आ.",
            "अ + अ → आ."),
        mcq("transfer", 5, "By the pattern of अभिभूयमानम् (being overcome), which form of √कृ means being done, in a new example?",
            ("क्रियमाणम्", "-यमान is the present passive participle: क्रियमाणम् = being done."),
            [("कृतम्", "कृतम् is the past passive participle: done."),
             ("करिष्यमाणम्", "-इष्यमाण is future: about to be done."),
             ("कुर्वत्", "कुर्वत् is the present active participle: doing.")],
            "क्रियमाणम् = being done, like अभिभूयमानम् = being overcome.",
            "Present passive participle: -यमान.",
            teaches="The present passive participle ends in -यमान: अभि-√भू → अभिभूयमान (being overcome), √कृ → क्रियमाण (being done)."),
    ],
}

# ---------------------------------------------------------------- unit 46
AUTHORED["46"] = {
    "title": "तस्मिन्मारुतोद्रेकः",
    "question": "By unit 46, which doṣa predominates in the old age, and what follows from it?",
    "rule": ("In it (the old age), predominance of māruta (a name of Vāta); because of that: looseness of the flesh and "
             "joints (and bones, on the data's split), rough skin, stooping of the body, trembling, cough, breathlessness, bringing up of śleṣman and "
             "nasal mucus, and wasting of the dhātus."),
    "limits": ("Prose, no verb. The split of श्लथासारमांससंध्यस्थिता is uncertain (…सन्धि-अस्थि-ता or …सन्धि-अ-स्थिता, "
               "instability): no question rests on it. How the compound कासश्वास…उदीरणम् groups its members is open."),
    "explain_hi": ("वृद्ध वय में मारुत यानी वात की अधिकता रहती है। "
                   "उससे: मांस और सन्धियों का ढीला और सारहीन होना (डेटा के विभाजन पर अस्थियों का भी), त्वचा की रूखाई, शरीर का झुकना, कम्पन, खाँसी, साँस फूलना, श्लेष्मा और सिंघाणक (नाक का मल) का निकलना, और धातुओं का क्षय। "
                   "‘श्लथासारमांससंध्यस्थिता’ का विभाजन अनिश्चित है (‘अस्थि-ता’ या ‘अ-स्थिता’ यानी अस्थिरता), इसलिए इस पर प्रश्न नहीं। "
                   "बाल में कफ, मध्य में पित्त, वृद्ध में वात: इकाई ४०, ४३ और ४६ यही क्रम देती हैं।"),
    "hook": "बुढ़ापे में वात: ढीला, रूखा, झुका, काँपता, घटता।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 46, which doṣa predominates in the old age?",
            ("Vāta", "मारुतोद्रेकः: predominance of māruta, a name of Vāta (standard)."),
            [("Kapha", "Kapha (śleṣman) predominates in the young age (unit 40)."),
             ("Pitta", "Pitta predominates in the middle age (unit 43)."),
             ("None", "A doṣa is named: मारुत-उद्रेकः.")],
            "तस्मिन्मारुतोद्रेकः: in it, predominance of Vāta.",
            "बाल: कफ, मध्य: पित्त, वृद्ध: वात."),
        order(1, "Put the printed parts of unit 46's list in order.",
              ["श्लथासारमांससंध्यस्थिता", "त्वक्पारुष्यम्", "अवनामः कायस्य", "वेपथुः", "कासश्वासश्लेष्मसिंघाणकोदीरणं",
               "धातुक्षयश्च"],
              "Looseness of flesh and joints (split uncertain); rough skin; stooping of the body; trembling; cough, breathlessness, bringing up of śleṣman and mucus; wasting of the dhātus.",
              "Body tissues → skin → posture → trembling → breath and mucus → dhātus."),
        match(2, "Match each word of unit 46 to its meaning.",
              [["पारुष्य", "roughness"], ["अवनाम", "stooping"], ["वेपथु", "trembling"], ["सिंघाणक", "nasal mucus"],
               ["क्षय", "wasting"]],
              "त्वक्पारुष्य, अवनाम, वेपथु, सिंघाणक, धातुक्षय.",
              "पारुष्य, अवनाम, वेपथु, सिंघाणक, क्षय.", role="extend",
              teaches="उदीरण = bringing up, expulsion: कास…सिंघाणक-उदीरणम्, the bringing up of śleṣman and nasal mucus."),
        mcq("discriminate", 3, "Which of these is named for the old age in unit 46, and not for the young age?",
            ("Trembling (vepathu)", "वेपथुः is in the list of unit 46."),
            [("Softness (mārdava)", "Softness belongs to the young age (unit 41)."),
             ("Little anger (alpakrodha)", "Little anger belongs to the young age (unit 41)."),
             ("Body growth (dehavṛddhi)", "Growth of body size belongs to the young age (unit 40).")],
            "Old age: trembling, stooping, rough skin; young age: softness, little anger, growth.",
            "वेपथुः (trembling): old age."),
        multi("apply", 4, "Which statements fit unit 46?",
              [("The skin grows soft", "The line says the opposite: त्वक्पारुष्यम्, roughness of the skin."),
               ("The body stoops", "Right: अवनामः कायस्य."),
               ("Pitta predominates in it", "Pitta belongs to the middle age (unit 43); here it is māruta."),
               ("The split of श्लथासारमांससंध्यस्थिता is uncertain", "Right: the data gives two possible parses."),
               ("The dhātus waste", "Right: धातुक्षयश्च.")],
              [1, 3, 4],
              "Vāta's predominance: stooping, trembling, rough skin, wasting of the dhātus; one compound's split is open.",
              "तस्मिन्मारुतोद्रेकः तेन ... धातुक्षयश्च."),
        mcq("transfer", 5, "Built like त्वक्पारुष्यम् (roughness of the skin), what does केशपारुष्यम् mean in a new example?",
            ("Roughness of the hair", "X-पारुष्यम् = roughness of X: केश-पारुष्यम्, roughness of the hair."),
            [("Softness of the hair", "पारुष्य means roughness, not softness."),
             ("Hair of the rough one", "The second member is the head: it names roughness, not hair."),
             ("Loss of the hair", "पारुष्य means roughness, not loss.")],
            "केशपारुष्यम् = roughness of the hair, like त्वक्पारुष्यम् = roughness of the skin.",
            "Tatpuruṣa X-Y = Y of X.",
            teaches="In a tatpuruṣa the last member is the head: त्वक्-पारुष्यम् = roughness of the skin."),
    ],
}

# ---------------------------------------------------------------- unit 47
AUTHORED["47"] = {
    "title": "अन्ये पुनराहुः",
    "question": "What does unit 47 introduce?",
    "rule": ("'Others, however, say': the line introduces the view of other (unnamed) authorities, which the data takes "
             "to be the verse of unit 48."),
    "limits": ("Prose, one short line. Who the 'others' are is not stated. That unit 48 is what they say is the data's "
               "reading ('appear to be'); no question rests on it."),
    "explain_hi": ("यह छोटी गद्य-पंक्ति दूसरे आचार्यों का मत आरम्भ करती है: ‘दूसरे फिर कहते हैं’। "
                   "वे दूसरे कौन हैं, पाठ नहीं बताता। "
                   "डेटा के अनुसार अगली इकाई (४८) का श्लोक ही उनका कथन प्रतीत होता है। "
                   "‘पुनर्’ का अन्तिम र् मूल है (विराम में पुनः लिखा जाता है); स्वर आ से पहले वह र् दिखता है: पुनराहुः। "
                   "‘आहुः’ प्रथम पुरुष बहुवचन है: वे कहते हैं।"),
    "hook": "अन्ये पुनराहुः: अब दूसरों का मत।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 47, what does अन्ये mean?",
            ("Others", "अन्ये = others (m. nom. pl.)."),
            [("We all", "'We' would be वयम्."),
             ("These", "'These' would be इमे or एते."),
             ("Both", "'Both' would be उभौ.")],
            "अन्ये पुनराहुः: others, however, say.",
            "अन्ये = others."),
        order(1, "Put the words of unit 47 in the printed order.",
              ["अन्ये", "पुनर्", "आहुः"],
              "Others; however; say.",
              "अन्ये → पुनर् → आहुः."),
        match(2, "Match each word of unit 47 to its meaning.",
              [["अन्ये", "others"], ["पुनर्", "again, however"], ["आहुः", "(they) say"]],
              "अन्ये पुनर् आहुः = others, however, say.",
              "अन्ये, पुनर्, आहुः.", role="extend",
              teaches="आहुः is the perfect, third person plural, of √अह्: 'they say'."),
        mcq("discriminate", 3, "Why does पुनर् show र् before आहुः?",
            ("Its final र् is original", "पुनर् ends in र् (पुनः at a pause); before a vowel the र् shows."),
            [("अः before a vowel always → र्", "Not so: अः before a vowel other than अ becomes अ."),
             ("A र् is added to part two vowels", "No र् is added; it belongs to पुनर्."),
             ("The र् belongs to the verb", "The verb is आहुः; the र् is the end of पुनर्.")],
            "पुनर् + आहुः → पुनराहुः.",
            "पुनर् keeps its र् before a vowel."),
        mcq("apply", 4, "What form is आहुः in unit 47?",
            ("Third person plural: they say", "Gram: 3 pl. pf. of √अह्: they say."),
            [("First person plural: we say", "'We say' is not this form; -उः marks the third plural."),
             ("Third person singular: he says", "The singular would be आह."),
             ("Second person plural: you say", "-उः is not a second-person ending.")],
            "आहुः = they say, with अन्ये (others) as subject.",
            "आहुः = they say."),
        mcq("transfer", 5, "By पुनर् + आहुः → पुनराहुः, how is पुनर् + आगच्छति (comes again) joined in a new example?",
            ("पुनरागच्छति", "पुनर् keeps its र् before a vowel: पुनरागच्छति."),
            [("पुन आगच्छति", "That treats पुनर् as an अः-word; its र् stays before a vowel."),
             ("पुनो आगच्छति", "ओ does not come from पुनर् before a vowel."),
             ("पुनस् आगच्छति", "स् does not arise before a vowel here.")],
            "पुनर् + आगच्छति = पुनरागच्छति, like पुनराहुः.",
            "पुनर् + vowel → पुनर्-.",
            teaches="Words with a final र् (पुनर्, written पुनः at a pause) show the र् before a vowel: पुनराहुः, पुनरागच्छति."),
    ],
}

# ---------------------------------------------------------------- unit 48
AUTHORED["48"] = {
    "title": "बाल्येवृद्धिः प्रभामेधा...",
    "question": "What can be said for sure about the verse of unit 48 on the decades?",
    "rule": ("A verse (anuṣṭubh) of two printed lines. It lists growth, lustre (प्रभा), intelligence (मेधा), skin, śukra "
             "(semen), eye and hearing, and says that in the decades (दशकेषु), in order (क्रमात्), the mind and all the "
             "sense-organs go (यान्ति)."),
    "limits": ("Low confidence; the sense of the pair is not firm. Print बाल्ये is kept (बाल्यं, giving ten items, is not "
               "adopted). Whether यान्ति means 'decline' or 'arrive' is open; 'years' is not in the Sanskrit. Questions ask "
               "only the printed words, their order and sandhi."),
    "explain_hi": ("इकाई ४७ के ‘दूसरे’ आचार्यों का यह श्लोक प्रतीत होता है; दो छपी पंक्तियाँ एक श्लोक के दो अर्ध हैं। "
                   "इसमें वृद्धि, प्रभा (कान्ति), मेधा (बुद्धि), त्वचा, शुक्र (वीर्य), आँख और श्रवण-इन्द्रिय गिनाए गए हैं, और कहा गया है कि दशकों में क्रम से मन और सभी इन्द्रियाँ ‘जाती हैं’ (यान्ति)। "
                   "‘यान्ति’ का अर्थ ‘चली जाती हैं’ है या ‘आती हैं’, पाठ तय नहीं करता; ‘वर्ष’ शब्द भी नहीं है। "
                   "छपा ‘बाल्ये’ रखा गया है; ‘बाल्यं’ पढ़ें तो दस दशकों के लिए दस बातें बनती हैं, पर यह अपनाया नहीं गया। "
                   "विश्वास निम्न है, इसलिए प्रश्न केवल छपे शब्दों, उनके क्रम और सन्धि पर हैं।"),
    "hook": "दशक-दशक: प्रभा, मेधा, त्वचा... मन और इन्द्रियाँ (अर्थ अनिश्चित)।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 48, what does दशकेषु mean?",
            ("In the decades", "दशक = a group of ten (years): दशकेषु, in the decades (loc. pl.)."),
            [("In the seasons", "Seasons would be ऋतुषु."),
             ("In the months", "Months would be मासेषु."),
             ("In the days", "Days would be दिनेषु.")],
            "दशकेषु क्रमाद्यान्ति: in the decades, in order, they go.",
            "दशक = group of ten."),
        order(1, "Put the printed items of unit 48's first line in order.",
              ["प्रभा", "मेधा", "त्वक्", "शुक्र", "अक्षि", "श्रुतीन्द्रिय"],
              "Lustre, intelligence, skin, śukra (semen), eye, the faculty of hearing.",
              "प्रभा → मेधा → त्वक् → शुक्र → अक्षि → श्रुतीन्द्रिय."),
        match(2, "Match each word of unit 48 to its meaning.",
              [["प्रभा", "lustre"], ["मेधा", "intelligence"], ["त्वक्", "skin"], ["अक्षि", "eye"],
               ["क्रमात्", "in order"]],
              "प्रभा, मेधा, त्वक्, अक्षि are items of the list; क्रमात् = in order, one after another.",
              "प्रभा, मेधा, त्वक्, अक्षि, क्रमात्.", role="extend",
              teaches="क्रमात् (ablative of क्रम, used as an adverb) = in order, successively."),
        mcq("discriminate", 3, "Which split of the printed क्रमाद्यांति is right?",
            ("क्रमात् + यान्ति", "त् before the voiced य → द्: क्रमाद्यान्ति."),
            [("क्रमा + द्यान्ति", "Neither क्रमा nor द्यान्ति is a word here."),
             ("क्रमम् + आद्यान्ति", "आद्यान्ति is not a word, and म् + आ would show म."),
             ("क्रमात् + आयान्ति", "That would be printed क्रमादायान्ति, with आ after द.")],
            "क्रमात् (in order) + यान्ति (they go).",
            "त् + voiced sound (not a nasal) → द्."),
        multi("apply", 4, "Which statements fit unit 48 as the data gives it?",
              [("The data fixes यान्ति as 'decline'", "Not so: 'decline' or 'arrive' is left open; only 'go' is given."),
               ("The unit is metrical: a verse", "Right: two printed lines read as one verse."),
               ("The data adopts the reading बाल्यं", "Not so: the print बाल्ये is kept; बाल्यं is not adopted."),
               ("प्रभा and मेधा are among the listed items", "Right: प्रभामेधा..."),
               ("The Sanskrit names the decades as years", "Not so: 'years' is not in the Sanskrit.")],
              [1, 3],
              "A verse; printed words sure; the sense of यान्ति and of the pair is open.",
              "Ask only what the print states."),
        mcq("transfer", 5, "By the rule of शुक्र + अक्षि → शुक्राक्षि, how is देव + अलयः joined in a new example?",
            ("देवालयः", "अ + अ → आ: देव + अलयः → देवालयः."),
            [("देवलयः", "The two अ's merge into a long आ; a short अ is wrong."),
             ("देवेलयः", "ए comes from अ + इ, not from अ + अ."),
             ("देवोलयः", "ओ comes from अ + उ, not from अ + अ.")],
            "देव + अलयः = देवालयः, like शुक्र + अक्षि = शुक्राक्षि.",
            "अ + अ → आ.",
            teaches="Short अ + short अ merge into long आ: शुक्र + अक्षि → शुक्राक्षि, देव + अलयः → देवालयः."),
    ],
}

# ---------------------------------------------------------------- unit 49
AUTHORED["49"] = {
    "title": "एवं वर्षशतमायुषः प्रमाणं",
    "question": "By unit 49, what is the measure of life?",
    "rule": "Thus (एवम्) a hundred years (वर्षशतम्) is the measure (प्रमाणम्) of life (आयुषः).",
    "limits": ("Prose, no verb (the copula is understood). The line does not say how the hundred years are reckoned, "
               "nor what एवम् sums up; no question rests on that."),
    "explain_hi": ("इस प्रकार आयु का प्रमाण सौ वर्ष है। "
                   "‘वर्षशतम्’ यानी सौ वर्ष; ‘आयुषः’ आयुस् का षष्ठी रूप: आयु का; ‘प्रमाणम्’ यानी माप। "
                   "‘एवम्’ (इस प्रकार) किस गणना को समेटता है, पंक्ति नहीं बताती। "
                   "सन्धि: वर्षशतम् + आयुषः → वर्षशतमायुषः (स्वर से पहले म्); एवम् व्यंजन से पहले एवं लिखा गया।"),
    "hook": "आयु का माप: सौ वर्ष।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 49, what is the measure of life?",
            ("A hundred years", "वर्षशतम् आयुषः प्रमाणम्: a hundred years is the measure of life."),
            [("Sixty years", "Sixty is the end of the middle age (unit 39), not of life."),
             ("A thousand years", "A thousand would be सहस्र, not शत."),
             ("Eighty years", "No eighty is named; शत is a hundred.")],
            "एवं वर्षशतमायुषः प्रमाणं.",
            "वर्ष-शत = a hundred years."),
        order(1, "Put the words of unit 49 in the printed order.",
              ["एवम्", "वर्षशतम्", "आयुषः", "प्रमाणम्"],
              "Thus; a hundred years; of life; the measure.",
              "एवम् → वर्षशतम् → आयुषः → प्रमाणम्."),
        match(2, "Match each word of unit 49 to its meaning.",
              [["एवम्", "thus"], ["वर्षशत", "a hundred years"], ["आयुस्", "life"], ["प्रमाण", "measure"]],
              "एवम् = thus; वर्षशतम् = a hundred years; आयुषः = of life; प्रमाणम् = measure.",
              "एवम्, वर्षशत, आयुस्, प्रमाण.", role="extend",
              teaches="आयुस् (life) is an s-stem; आयुषः here is its genitive singular: of life."),
        mcq("discriminate", 3, "Which split of वर्षशतमायुषः is right?",
            ("वर्षशतम् + आयुषः", "म् before a vowel stays म् and joins it: वर्षशतमायुषः."),
            [("वर्षशत + मायुषः", "मायुषः is not a word; the म् ends वर्षशतम्."),
             ("वर्षशतम् + अयुषः", "That would be printed वर्षशतमयुषः, with a short अ."),
             ("वर्षशते + आयुषः", "ए before आ would not give म; वर्षशते is not the printed word.")],
            "वर्षशतम् (a hundred years) + आयुषः (of life).",
            "Final म् + vowel → म् (joined)."),
        mcq("apply", 4, "In unit 49, which word names what is being measured?",
            ("आयुषः", "आयुषः = of life: life is what is measured."),
            [("वर्षशतम्", "वर्षशतम् is the measure itself, a hundred years."),
             ("एवम्", "एवम् = thus; it names nothing measured."),
             ("प्रमाणम्", "प्रमाणम् is the word 'measure', not what is measured.")],
            "वर्षशतम् (measure) आयुषः (of life) प्रमाणम् (the measure).",
            "Genitive = what the measure belongs to."),
        mcq("transfer", 5, "Built like वर्षशतम् (a hundred years), what does दिनशतम् mean in a new example?",
            ("A hundred days", "दिन-शतम् = a hundred of days, as वर्ष-शतम् = a hundred years."),
            [("The hundredth day", "That would need an ordinal (शततम); शतम् is the number."),
             ("A thousand days", "A thousand would be सहस्र, not शत."),
             ("A day of a hundred", "No such sense: the first member names what is counted.")],
            "दिनशतम् = a hundred days, like वर्षशतम् = a hundred years.",
            "X-शतम् = a hundred X's.",
            teaches="A noun before शतम् names what is counted: वर्षशतम् = a hundred years, दिनशतम् = a hundred days."),
    ],
}

# ---------------------------------------------------------------- unit 50
AUTHORED["50"] = {
    "title": "अस्मिन्काले संतिपुनः...",
    "question": "By unit 50, what should one do with the age (vayas) after ascertaining the measure of life?",
    "rule": ("In this time there are men whose span (because of a particular karma) is tied to a hundred years; having "
             "ascertained (उपलभ्य) the measure of their life, one should divide (विभजेत्) the age into three (त्रिधा)."),
    "limits": ("Two printed words are emended: अनाधिक (read अनधिक, 'no more than' a hundred; 'more than' is not "
               "excluded) and विशैशैः (read विशेषैः). The men's span and the means of ascertaining rest on these: no "
               "question on them."),
    "explain_hi": ("इस काल में ऐसे मनुष्य हैं जिनकी आयु विशेष कर्म के कारण सौ वर्ष से जुड़ी है; डेटा ‘सौ से अधिक न जीने वाले’ पढ़ता है, पर यह छपे ‘अनाधिक’ के संशोधन ‘अनधिक’ पर टिका है, और उलटा अर्थ ‘अधिक’ भी बाहर नहीं किया जा सकता। "
                   "उनकी आयु का प्रमाण जानकर (उपलभ्य) वय को तीन भागों में बाँटना चाहिए (त्रिधा विभजेत्)। "
                   "किससे जानें, यह ‘प्रकृतिविशैशैः’ पर टिका है, जो कोई शब्द नहीं; ‘प्रकृतिविशेषैः’ अनुमानित पाठ है। "
                   "‘वयस्त्रिधा’ में विसर्ग त से पहले स् बना है; ‘विभजेत्’ विधिलिङ् है: बाँटना चाहिए।"),
    "hook": "आयु का माप जानकर वय को तीन में बाँटो।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 50, into how many parts should the age (vayas) be divided?",
            ("Three", "वयस्त्रिधा विभजेत्: one should divide the age in three ways."),
            [("Two", "त्रिधा is 'in three ways', not two (द्विधा)."),
             ("Four", "त्रिधा is 'in three ways', not four (चतुर्धा)."),
             ("Seven", "त्रिधा is 'in three ways', not seven (सप्तधा).")],
            "वयः त्रिधा विभजेत्.",
            "त्रिधा = in three ways."),
        order(1, "Put these printed parts of unit 50 in order.",
              ["अस्मिन्काले", "मनुष्याः", "तेषां", "प्रमाणमुपलभ्य", "वयस्त्रिधा विभजेत्"],
              "In this time; men; of them; having ascertained the measure; one should divide the age in three.",
              "अस्मिन्काले → मनुष्याः → तेषां → प्रमाणमुपलभ्य → वयस्त्रिधा विभजेत्."),
        match(2, "Match each word of unit 50 to its meaning.",
              [["अस्मिन् काले", "in this time"], ["मनुष्याः", "men"], ["उपलभ्य", "having ascertained"],
               ["त्रिधा", "in three ways"], ["विभजेत्", "should divide"]],
              "अस्मिन् काले ... मनुष्याः; प्रमाणम् उपलभ्य वयः त्रिधा विभजेत्.",
              "अस्मिन् काले, मनुष्याः, उपलभ्य, त्रिधा, विभजेत्.", role="extend",
              teaches="उपलभ्य is an absolutive in -य (prefix उप + √लभ्): 'having ascertained'; the act comes before विभजेत्."),
        mcq("discriminate", 3, "Why is वयः printed वयस् before त्रिधा?",
            ("Visarga before त → स्", "Before the voiceless त the visarga becomes स्: वयस्त्रिधा."),
            [("Visarga before त → ओ", "ओ comes from अः before a voiced consonant; त is voiceless."),
             ("Visarga before त → र्", "र् comes after vowels other than अ/आ before a voiced sound."),
             ("The स् is a part of त्रिधा", "त्रिधा begins with त; the स् ends वयस्.")],
            "वयः + त्रिधा → वयस्त्रिधा.",
            "Visarga + त/थ → स्."),
        mcq("apply", 4, "Which printed word of unit 50 does the data mark as no word, read by conjecture?",
            ("प्रकृतिविशैशैः", "विशैशैः is no word; प्रकृतिविशेषैः is the conjectural reading."),
            [("उपलभ्य", "उपलभ्य is a sure word: having ascertained."),
             ("मनुष्याः", "मनुष्याः is a sure word: men."),
             ("विभजेत्", "विभजेत् is a sure word: should divide.")],
            "The second sentence's means (प्रकृतिविशैशैः) rests on a conjecture; the rest is sure.",
            "Flagged print → no question on its sense."),
        mcq("transfer", 5, "By the pattern of विभजेत् (should divide), which form of √पठ् means one should read, in a new example?",
            ("पठेत्", "-एत् is the optative third singular of thematic verbs like √भज्: पठेत्, one should read."),
            [("पठति", "पठति is the present: he reads."),
             ("पठितुम्", "पठितुम् is the infinitive: to read."),
             ("अपठत्", "अपठत् is the past (imperfect): he read.")],
            "पठेत् = one should read, like विभजेत् = one should divide.",
            "Optative 3rd singular of thematic verbs: -एत्.",
            teaches="Thematic verbs (√भज्, √पठ्) form the optative third singular in -एत्: विभजेत्, पठेत्. Other verb classes differ (ब्रूयात्)."),
    ],
}


# ================================================================= NOTES_HI
NOTES_HI = {
    "38": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। क्रिया नहीं, ‘है’ समझा जाता है। आ + पञ्चमी = ‘तक’; सोलहवाँ वर्ष शामिल है या नहीं, "
           "पाठ नहीं बताता। सन्धि जाँची: तत्र + आ → तत्रा (अ + आ → आ); षोडशात् + वर्षात् → षोडशाद्वर्षात् और वर्षात् + बालम् → "
           "वर्षाद्बालम् (त् + घोष व्यंजन → द्); पंक्ति-अन्त का ‘बालं’ छपाई में ं के साथ।"),
    "39": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। क्रिया नहीं। ‘वर्ष’ इकाई ३८ (वर्षात्) से समझा जाता है, जोड़ा नहीं गया। सन्धि जाँची: "
           "आ + षष्टेः → आषष्टेः; षष्टेः + मध्यमम् → षष्टेर्मध्यमम् (ए के बाद विसर्ग + घोष → र्); ततः + वृद्धम् → ततो वृद्धम् (अः + घोष "
           "व्यंजन → ओ); मध्यमम् + ततः → मध्यमं ततः (व्यंजन से पहले म् → ं)।"),
    "40": ("गद्य; विश्वास उच्च; दो छपी पंक्तियाँ (०२.०८.४९-५०) जुड़ी हैं। कोई पाठ-चिह्न नहीं। तीनों भेदों के अलग नाम पाठ में नहीं; ‘उभय’ = दूध "
           "और अन्न दोनों। श्लेष्मन् यहाँ कफ का नाम (मानक)। छपा ‘बालंत्रिविधं’ = बालम् त्रिविधम् (केवल छपाई का जोड़)। सन्धि जाँची: तेषु + "
           "अपि → तेष्वपि (उ + अ → व); स्तन्य + आहार → स्तन्याहार (अ + आ → आ); आहार + उभय → आहारोभय (अ + उ → ओ); श्लेष्म + "
           "उद्रेकः → श्लेष्मोद्रेकः; उद्रेकः + च → उद्रेकश्च (विसर्ग + च → श्)।"),
    "41": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। ‘स्नेह’ दो-अर्थी: चिकनापन (डेटा का पठन, इकाई ४० की कफ-अधिकता का फल) या प्रेम; "
           "‘सौभाग्य’ = सौभाग्य, आकर्षण भी। ‘बालस्य’ = बाल वय में या बालक का, दोनों सम्भव। छपा ‘बालस्यस्नेह…’ दो शब्द जुड़े छपे हैं। सन्धि "
           "जाँची: सौकुमार्य + अल्प → सौकुमार्याल्प (अ + अ → आ)। ‘भवंति’ = भवन्ति (अनुस्वार-लेखन)।"),
    "42": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। ‘मध्यम्’ छपा नपुंसक रूप (इकाई ३७ में भी), भूल नहीं। तीनों चरणों की सीमा इकाई ४४ में। "
           "सन्धि जाँची: मध्यम् + अपि → मध्यमपि (स्वर से पहले म्); सम्पूर्णत्वम् + अपरिहानिः → सम्पूर्णत्वमपरिहानिः; अपरिहानिः + च → "
           "अपरिहानिश्च (विसर्ग + च → श्)।"),
    "43": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। ‘परिपाक’ = परिपक्वता या पाचन, अर्थ तय नहीं। ‘तस्मिन्’ = मध्य वय (इकाई ४२ के बाद आने से)। "
           "‘प्रज्ञाधिक्यपरिपाकौ’ द्विवचन। छपा ‘तेनदीप्ताग्निता’ दो शब्द जुड़े। सन्धि जाँची: पित्त + उद्रेकः → पित्तोद्रेकः (अ + उ → ओ); दीप्त + "
           "अग्नि → दीप्ताग्नि (अ + अ → आ); प्रज्ञा + आधिक्य → प्रज्ञाधिक्य (आ + आ → आ); व्यवसायः + च → व्यवसायश्च।"),
    "44": ("गद्य; विश्वास मध्यम। पाठ-चिह्न (सम्भव): छपा ‘प्रश्नय’ कोई शब्द नहीं; ‘प्रश्रय’ (विनय) अनुमानित पाठ (न/र की भूल); इस पर कोई "
           "प्रश्न नहीं। ‘वीर्य’ यहाँ बल के साथ शक्ति (डेटा)। अपरिहानि का अन्त साठ (इकाई ३९)। सन्धि जाँची: तत्र + आ → तत्रा; त्रिंशतः + "
           "यौवनम् → त्रिंशतो यौवनम् (अः + घोष व्यंजन → ओ); यौवनम् + आ → यौवनमा (स्वर से पहले म्); धातु + इन्द्रिय → धात्विन्द्रिय "
           "(उ + इ → वि); सम्पूर्णत्वम् + अतः → सम्पूर्णत्वमतः।"),
    "45": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। ‘खलित’ = गंजापन (सम्भावित; ठोकर खाना भी अर्थ)। ‘जीर्ण’ = पुराना, जर्जर (भवन का "
           "विशेषण), ‘पचा’ नहीं। कर्ता ‘वृद्धम्’, क्रिया ‘अवसीदति’; घर उपमा है। मानक: वली = झुर्री, कास = खाँसी, श्वास = साँस फूलना। "
           "सन्धि जाँची: ‘धात्विंद्रियादि’ (उ + इ → वि; अ + आ → आ); ‘सादादिभिरभिभूयमानं’ (इ के बाद विसर्ग + स्वर → र्); भवनम् + इव → "
           "भवनमिव; इव + अभिवृष्टम् → इवाभिवृष्टम् (अ + अ → आ); अभिवृष्टम् + अवसीदति → अभिवृष्टमवसीदति।"),
    "46": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। ‘मारुत’ = वात का नाम (मानक)। ‘श्लथासारमांससंध्यस्थिता’ का विभाजन अनिश्चित: "
           "…सन्धि-अस्थि-ता (डेटा का पठन) या …सन्धि-अ-स्थिता (अस्थिरता); इस पर कोई प्रश्न नहीं। ‘कासश्वास…उदीरणम्’ का समूहन भी खुला। "
           "मानक: सिंघाणक = नाक का मल, वेपथु = कम्पन। सन्धि जाँची: मारुत + उद्रेकः → मारुतोद्रेकः (अ + उ → ओ); श्लथ + असार → "
           "श्लथासार; सिंघाणक + उदीरणम् → सिंघाणकोदीरणम्; धातुक्षयः + च → धातुक्षयश्च।"),
    "47": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। ‘अन्ये’ कौन हैं, नहीं बताया। डेटा: अगली छपी पंक्तियाँ ५८-५९ (यानी इकाई ४८) उनका कथन "
           "प्रतीत होती हैं। ‘पुनर्’ का र् मूल; पुनर् + आहुः → पुनराहुः। ‘आहुः’ = √अह् का परोक्ष (लिट्), प्रथम पुरुष बहुवचन।"),
    "48": ("श्लोक (अनुष्टुभ्, दो छपी पंक्तियाँ ०२.०८.५८-५९ एक श्लोक); विश्वास निम्न। पाठ-चिह्न (सम्भव, अपनाया नहीं): छपा ‘बाल्ये’ रखा गया; "
           "‘बाल्यं’ पढ़ें तो दस दशकों के लिए दस बातें बनतीं। ‘यान्ति’ = जाती हैं: घटना या आना, तय नहीं; ‘वर्ष’ शब्द संस्कृत में नहीं; बहुवचन क्रिया, "
           "‘मनः’ एकवचन। छपा ‘सर्वेद्रियाणि’ में ं नहीं दिखता; डेटा इसे सर्व-इन्द्रियाणि पढ़ता है। मानक: शुक्र = वीर्य। सन्धि जाँची: शुक्र + अक्षि → "
           "शुक्राक्षि (अ + अ → आ); श्रुति + इन्द्रियम् → श्रुतीन्द्रियम् (इ + इ → ई); क्रमात् + यान्ति → क्रमाद्यान्ति (त् + घोष → द्)।"),
    "49": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। क्रिया नहीं, ‘है’ समझा जाता है। ‘एवम्’ किसे समेटता है, पंक्ति नहीं कहती। सन्धि जाँची: "
           "एवम् + वर्षशतम् → एवं वर्षशतम् (व्यंजन से पहले म् → ं); वर्षशतम् + आयुषः → वर्षशतमायुषः (स्वर से पहले म्)।"),
    "50": ("गद्य; विश्वास मध्यम। पाठ-चिह्न (सम्भव): छपा ‘अनाधिक’ (दीर्घ आ) इस अर्थ में शब्द नहीं; ‘अनधिक’ (सौ से अधिक नहीं) संशोधन है, "
           "उलटा अर्थ ‘अधिक’ बाहर नहीं; छपा ‘विशैशैः’ कोई शब्द नहीं, ‘विशेषैः’ अनुमानित पाठ, दूसरा वाक्य इसी पर टिका। इन पर कोई प्रश्न नहीं। "
           "‘कर्मविशेषात्’ सन्ति से या समास से जुड़ सकता है। ‘वयस्त्रिधा विभजेत्’ इकाई ३७-३९ के तीन वय को फिर उठाता है। सन्धि जाँची: वयः + "
           "त्रिधा → वयस्त्रिधा (विसर्ग + त → स्); प्रमाणम् + उपलभ्य → प्रमाणमुपलभ्य; छपा ‘संतिपुनः’ = सन्ति पुनः (छपाई का जोड़)।"),
}


# ===================================================================== AIDS
AIDS = {
    "38": {
        "chunks": "तत्रा | षोडशाद्वर्षाद् | बालं",
        "frame": "किनमें: तत्र (तीन वयों में) → सीमा: आ षोडशात् वर्षात् (सोलहवें वर्ष तक) → कौन-सा वय: बालम्।",
        "sandhi": "अ + आ → आ: तत्र + आ → तत्रा · त् + घोष व्यंजन → द्: षोडशात् + वर्षात् → षोडशाद्वर्षात्; वर्षात् + बालम् → वर्षाद्बालम्।",
    },
    "39": {
        "chain": {"steps": ["आ षष्टेः: साठ तक", "मध्यम वय", "ततः: उसके बाद", "वृद्ध वय"]},
        "chunks": "आषष्टेर्मध्यमं | ततो | वृद्धं",
        "sandhi": "ए के बाद विसर्ग + घोष → र्: षष्टेः + मध्यमम् → षष्टेर्मध्यमम् · अः + घोष व्यंजन → ओ: ततः + वृद्धम् → ततो वृद्धम्।",
        "anchors": "१६ तक बाल (इकाई ३८) → ६० तक मध्य → उसके बाद वृद्ध: तीन वय, दो सीमाएँ। (मेरी याद-पद्धति)",
    },
    "40": {
        "diagram": {"groups": [
            {"label": "बाल वय: तीन भेद (पोषण से)", "items": ["स्तन्य पर", "आहार पर", "उभय: दोनों पर"]},
            {"label": "तस्मिन्: उसमें", "items": ["देह के परिमाण की वृद्धि", "श्लेष्मा (कफ) की अधिकता"]}]},
        "chunks": "तेष्वपि | स्तन्याहारोभयवृत्त्या | बालंत्रिविधं | तस्मिन् | देहप्रमाणवृद्धिः | श्लेष्मोद्रेकश्च",
        "sandhi": "अ + आ → आ: स्तन्य + आहार → स्तन्याहार · अ + उ → ओ: आहार + उभय → आहारोभय; श्लेष्म + उद्रेकः → श्लेष्मोद्रेकः।",
        "anchors": "दूध → अन्न → दोनों: बच्चे के पोषण का क्रम जैसा। (मेरी याद-पद्धति; पाठ इन्हें क्रम-अवस्था नहीं कहता)",
    },
    "41": {
        "chunks": "तेन | बालस्य | स्नेह | मार्दव | सौकुमार्य | अल्पक्रोधत्व | सौभाग्यानि | भवंति",
        "frame": "कारण: तेन (डेटा: इकाई ४० की कफ-अधिकता) → किसमें: बालस्य → क्या होता है: पाँच गुण → क्रिया: भवन्ति।",
        "pegs": "पाँच गुण पाँच उँगलियों पर: अँगूठा स्नेह, तर्जनी मार्दव, मध्यमा सौकुमार्य, अनामिका अल्पक्रोध, कनिष्ठा सौभाग्य। (मेरा बनाया चित्र)",
    },
    "42": {
        "chunks": "मध्यमपि | त्रिविधं | यौवनं | संपूर्णत्वम् | अपरिहानिश्च",
        "chain": {"steps": ["यौवन", "सम्पूर्णत्व: पूर्णता", "अपरिहानि: ह्रास का न होना"]},
        "sandhi": "स्वर से पहले म् म् ही: मध्यम् + अपि → मध्यमपि · विसर्ग + च → श्: अपरिहानिः + च → अपरिहानिश्च।",
    },
    "43": {
        "chain": {"steps": ["तस्मिन्: मध्य वय में", "पित्त की अधिकता", "तेन: उससे", "दीप्त अग्नि", "प्रज्ञा की अधिकता",
                            "परिपाक", "व्यवसाय: दृढ़ निश्चय"]},
        "chunks": "तस्मिन् | पित्तोद्रेकः | तेनदीप्ताग्निता | प्रज्ञाधिक्यपरिपाकौ | व्यवसायश्च",
        "sandhi": "अ + उ → ओ: पित्त + उद्रेकः → पित्तोद्रेकः · अ + अ → आ: दीप्त + अग्नि → दीप्ताग्नि · आ + आ → आ: प्रज्ञा + आधिक्य → प्रज्ञाधिक्य।",
        "anchors": "बाल: कफ (इकाई ४०) → मध्य: पित्त (यहाँ) → वृद्ध: वात (इकाई ४६)। (मेरी याद-पद्धति)",
    },
    "44": {
        "diagram": {"groups": [
            {"label": "मध्य वय के चरण", "items": ["तीस तक: यौवन", "चालीस तक: सम्पूर्णत्व",
                                              "इसके बाद: अपरिहानि (साठ तक, इकाई ३९)"]}]},
        "chunks": "तत्रात्रिंशतो यौवनम् | आचत्वारिंशतः | सर्वधात्विंद्रिय…प्रश्नयगुणसंपूर्णत्वम् | अतः परम् | अपरिहानिः",
        "sandhi": "अः + घोष व्यंजन → ओ: त्रिंशतः + यौवनम् → त्रिंशतो यौवनम् · उ + इ → वि: धातु + इन्द्रिय → धात्विन्द्रिय।",
        "anchors": "३० · ४० · ६०: यौवन, पूर्णता, अपरिहानि। (मेरी याद-पद्धति)",
    },
    "45": {
        "chain": {"steps": ["श्वः श्वः: दिन-प्रतिदिन", "धातु-इन्द्रिय आदि के गुण घटते", "वली, खलित, कास, श्वास, अग्निसाद आदि से दबा",
                            "वर्षा से भीगे पुराने घर की तरह", "अवसीदति: बैठ जाता है"]},
        "chunks": "वृद्धं तु | श्वः श्वः | क्षीयमाणधात्विंद्रियादिगुणं | वलीखलितकासश्वासाग्निसादादिभिरभिभूयमानं | जीर्णं भवनमिवाभिवृष्टम् | अवसीदति",
        "story": "पाठ की अपनी उपमा: पुराना घर, ऊपर से बरसात; दीवारें रोज़ थोड़ी-थोड़ी गलतीं और एक दिन घर बैठ जाता है। वैसे ही वृद्ध वय।",
        "sandhi": "अ + अ → आ: इव + अभिवृष्टम् → इवाभिवृष्टम् · स्वर से पहले म्: भवनम् + इव → भवनमिव।",
    },
    "46": {
        "diagram": {"groups": [
            {"label": "वृद्ध वय: मारुत (वात) की अधिकता से", "items": ["मांस, सन्धि की शिथिलता (विभाजन अनिश्चित)", "त्वचा की रूखाई",
                                                             "शरीर का झुकना", "कम्पन", "कास, श्वास, श्लेष्मा-सिंघाणक का निकलना",
                                                             "धातुओं का क्षय"]}]},
        "chunks": "तस्मिन्मारुतोद्रेकः | तेन | श्लथासारमांससंध्यस्थिता | त्वक्पारुष्यमवनामः कायस्य | वेपथुः | कासश्वासश्लेष्मसिंघाणकोदीरणं | धातुक्षयश्च",
        "sandhi": "अ + उ → ओ: मारुत + उद्रेकः → मारुतोद्रेकः; सिंघाणक + उदीरणम् → सिंघाणकोदीरणम् · विसर्ग + च → श्: धातुक्षयः + च → धातुक्षयश्च।",
        "anchors": "ऊपर से नीचे: ऊतक → त्वचा → मुद्रा → कम्पन → साँस-कफ → धातु। (मेरी याद-पद्धति, पाठ का क्रम ही)",
    },
    "47": {
        "frame": "कौन: अन्ये (दूसरे, नाम नहीं) → क्या करते हैं: पुनः आहुः (फिर कहते हैं) → क्या: अगला श्लोक (डेटा का पठन)।",
        "chunks": "अन्ये | पुनराहुः",
        "sandhi": "मूल र् स्वर से पहले: पुनर् + आहुः → पुनराहुः।",
    },
    "48": {
        "chunks": "बाल्येवृद्धिः | प्रभामेधात्वक्शुक्राक्षिश्रुतींद्रियं | दशकेषु क्रमाद्यांति | मनःसर्वेद्रियाणि च",
        "frame": "क्या: वृद्धि, प्रभा, मेधा, त्वक्, शुक्र, अक्षि, श्रुति-इन्द्रिय; मन और सब इन्द्रियाँ → कब: दशकेषु (दशकों में) → कैसे: क्रमात् (क्रम से) → क्या करती हैं: यान्ति (जाती हैं; अर्थ खुला)।",
        "sandhi": "अ + अ → आ: शुक्र + अक्षि → शुक्राक्षि · इ + इ → ई: श्रुति + इन्द्रियम् → श्रुतीन्द्रियम् · त् + घोष → द्: क्रमात् + यान्ति → क्रमाद्यान्ति।",
        "anchors": "प्रभा-मेधा-त्वक्, शुक्र-अक्षि-श्रुति: तीन-तीन के दो गुच्छे। (मेरी याद-पद्धति; पाठ गुच्छे नहीं बनाता)",
    },
    "49": {
        "chunks": "एवं | वर्षशतमायुषः | प्रमाणं",
        "frame": "कितना: वर्षशतम् (सौ वर्ष) → किसका: आयुषः (आयु का) → क्या: प्रमाणम् (माप)।",
        "sandhi": "स्वर से पहले म्: वर्षशतम् + आयुषः → वर्षशतमायुषः · व्यंजन से पहले म् → ं: एवम् + वर्षशतम् → एवं वर्षशतम्।",
    },
    "50": {
        "chain": {"steps": ["अस्मिन् काले: इस काल में", "विशेष कर्म के कारण सौ वर्ष से जुड़ी आयु वाले मनुष्य",
                            "उनकी आयु का प्रमाण जानकर", "वय को तीन भागों में बाँटे"]},
        "chunks": "अस्मिन्काले | संतिपुनः | कर्मविशेषादनाधिकवर्षशतजीविनो मनुष्याः | तेषां | यथोक्तैः प्रकृतिविशैशैरायुषः | प्रमाणमुपलभ्य | वयस्त्रिधा विभजेत्",
        "sandhi": "विसर्ग + त → स्: वयः + त्रिधा → वयस्त्रिधा · स्वर से पहले म्: प्रमाणम् + उपलभ्य → प्रमाणमुपलभ्य।",
    },
}


# ============================================================== IMAGE_SPECS
IMAGE_SPECS = {
    ("39", "chain"): {
        "file": "sh8-madhya-vriddha-39.svg",
        "alt": ("Chain of unit 39 in line order: up to sixty; the middle age; after that; the old age."),
        "type": "chain",
        "title": "इकाई ३९: मध्य और वृद्ध",
        "steps": ["आ षष्टेः: साठ तक", "मध्यम वय", "ततः: उसके बाद", "वृद्ध वय"],
    },
    ("40", "diagram"): {
        "file": "sh8-bala-trividha-40.svg",
        "alt": ("Flowchart of unit 40: the young age is threefold by mode of living (on breast-milk, on food, on both); "
                "in it, growth of body size and predominance of śleṣman (Kapha)."),
        "type": "mermaid",
        "code": ("flowchart LR\n"
                 "  A[\"बाल वय\"] --> B[\"त्रिविध: पोषण से\"]\n"
                 "  B --> C[\"१ स्तन्य पर\"]\n"
                 "  B --> D[\"२ आहार पर\"]\n"
                 "  B --> E[\"३ दोनों पर\"]\n"
                 "  A --> F[\"तस्मिन्: उसमें\"]\n"
                 "  F --> G[\"देह-परिमाण की वृद्धि\"]\n"
                 "  F --> H[\"श्लेष्मा (कफ) की अधिकता\"]\n"),
    },
    ("43", "chain"): {
        "file": "sh8-pitta-madhya-43.svg",
        "alt": ("Flowchart of unit 43: in the middle age, predominance of Pitta; because of that, four results in line "
                "order: kindled agni, abundance of understanding, ripening, determination."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"मध्य वय में\"] --> B[\"पित्त की अधिकता\"]\n"
                 "  B --> C[\"तेन: उससे\"]\n"
                 "  C --> D[\"१ दीप्त अग्नि\"]\n"
                 "  C --> E[\"२ प्रज्ञा की अधिकता\"]\n"
                 "  C --> F[\"३ परिपाक\"]\n"
                 "  C --> G[\"४ व्यवसाय\"]\n"),
    },
    ("44", "diagram"): {
        "file": "sh8-madhya-charan-44.svg",
        "alt": ("Table of unit 44: up to thirty, youth; up to forty, fullness of all qualities; after this, non-decline, "
                "which ends at sixty by unit 39."),
        "type": "table",
        "title": "इकाई ४४: मध्य वय के चरण",
        "heads": ["सीमा", "चरण"],
        "rows": [["आ त्रिंशतः: तीस तक", "यौवन"], ["आ चत्वारिंशतः: चालीस तक", "सम्पूर्णत्व: गुणों की पूर्णता"],
                 ["अतः परम्: इसके बाद", "अपरिहानि (साठ तक, इकाई ३९)"]],
    },
    ("45", "chain"): {
        "file": "sh8-jirna-bhavana-45.svg",
        "alt": ("Chain of unit 45: day after day; the qualities of dhātus and senses waste; overcome by wrinkles, khalita, "
                "cough, breathlessness, weak agni and the like; like an old house rained upon; it sinks down."),
        "type": "chain",
        "title": "इकाई ४५: वृद्ध वय",
        "steps": ["श्वः श्वः: दिन-प्रतिदिन", "धातु-इन्द्रिय के गुण घटते", "वली, कास, श्वास आदि से दबा",
                  "भीगे पुराने घर की तरह", "अवसीदति: बैठ जाता है"],
    },
    ("46", "diagram"): {
        "file": "sh8-vata-vriddha-46.svg",
        "alt": ("Flowchart of unit 46: in the old age, predominance of māruta (Vāta); because of that, six results in "
                "line order: looseness of flesh and joints, rough skin, stooping, trembling, cough, breathlessness, śleṣman and nasal mucus, "
                "wasting of the dhātus."),
        "type": "mermaid",
        "code": ("flowchart LR\n"
                 "  A[\"वृद्ध वय: वात की अधिकता\"] --> B[\"तेन: उससे\"]\n"
                 "  B --> C[\"१ मांस-सन्धि की शिथिलता\"]\n"
                 "  B --> D[\"२ त्वचा की रूखाई\"]\n"
                 "  B --> E[\"३ शरीर का झुकना\"]\n"
                 "  B --> F[\"४ कम्पन\"]\n"
                 "  B --> G[\"५ कास, श्वास, श्लेष्मा-सिंघाणक\"]\n"
                 "  B --> H[\"६ धातुओं का क्षय\"]\n"),
    },
}
