from helpers import mcq, match, order, fill, multi, accepts


AUTHORED = {}

# ---------------------------------------------------------------- unit 39
AUTHORED["39"] = {
    "title": "यस्यां छिन्नायां ... दुश्चिकित्स्यतमानि",
    "question": "By unit 39, what happens when the sixth skin is cut, and what arises resting on it?",
    "rule": ("Of the sixth skin (प्राणधरा, unit 38): when it is cut, one faints (ताम्यति) and, as it were, enters blinding "
             "darkness; resting on it, sores (अरुस्) arise at the joints, black-red, thick-rooted, most difficult to treat."),
    "limits": ("Prose. The two relative clauses (यस्याम्, याम्) refer to the sixth skin of unit 38 (data note). Who faints is "
               "unstated ('one'). कृष्णरक्त may be 'black-red' or 'black and red': no question on it. The data gives no modern "
               "disease name for arus."),
    "explain_hi": ("यह गद्य-पंक्ति इकाई ३८ की छठी त्वचा, प्राणधरा, के बारे में दो बातें कहती है। "
                   "जब यह कटती है (छिन्नायाम्), तो व्यक्ति मूर्छित-सा हो जाता है (ताम्यति) और मानो अन्धे अन्धकार में प्रवेश करता है। "
                   "और इसी के आश्रय पर (अधिष्ठाय) जोड़ों में (पर्वसु) अरुस् यानी घाव उत्पन्न होते हैं। "
                   "ये घाव काले-लाल, मोटी जड़ वाले (स्थूलमूल) और अत्यन्त कठिनाई से चिकित्सा योग्य (दुश्चिकित्स्यतम) हैं। "
                   "‘कृष्णरक्त’ को ‘काला-लाल’ या ‘काला और लाल’ दोनों पढ़ा जा सकता है; डेटा अरुस् का कोई आधुनिक नाम नहीं देता।"),
    "hook": "प्राणधरा कटे तो अँधेरा; उसी पर जोड़ों में कठिन घाव।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 39, what happens to a person when this skin is cut?",
            ("One faints and enters darkness, as it were", "ताम्यति, अन्धमिव च तमः प्रविशति: one faints and enters darkness."),
            [("One loses all feeling in the skin of the limbs", "Loss of feeling is not named in unit 39."),
             ("Blood and fat flow out of the cut in a stream", "No flow of blood or fat is named in unit 39."),
             ("The skin heals at once and leaves no mark", "Healing is not named; the unit says one faints.")],
            "When it is cut, one faints and, as it were, enters blinding darkness.",
            "यस्यां छिन्नायां ताम्यति, अन्धमिव च तमः प्रविशति."),
        order(1, "Put these phrases of unit 39 in the line's order.",
              ["यस्यां छिन्नायां", "ताम्यत्यंधमिवच तमः प्रविशति", "यां चाधिष्ठायारूंषि जायंते", "पर्वसु",
               "कृष्णरक्तानि स्थूलमूलानि", "दुश्चिकित्स्यतमानि"],
              "When it is cut, one faints and enters darkness; resting on it, sores arise at the joints, black-red, "
              "thick-rooted, most difficult to treat.",
              "यस्यां छिन्नायां → ताम्यति ... प्रविशति → यां चाधिष्ठायारूंषि जायंते → पर्वसु → कृष्णरक्तानि स्थूलमूलानि → "
              "दुश्चिकित्स्यतमानि."),
        match(2, "Match each word of unit 39 to its meaning.",
              [["छिन्ना", "cut"], ["ताम्यति", "faints, is distressed"], ["पर्वसु", "at the joints"],
               ["स्थूलमूल", "thick-rooted"], ["दुश्चिकित्स्यतम", "most difficult to treat"]],
              "Cut, one faints; the sores at the joints are thick-rooted and most difficult to treat.",
              "छिन्ना, ताम्यति, पर्वसु, स्थूलमूल, दुश्चिकित्स्यतम.", role="extend",
              teaches="अरुस् (plural अरूंषि) = sores, wounds; they arise resting on (अधिष्ठाय) the sixth skin."),
        mcq("discriminate", 3, "Which split of ताम्यत्यंधम् is right?",
            ("ताम्यति + अन्धम्", "इ before a different vowel becomes य्: ताम्यति + अन्धम् → ताम्यत्यन्धम्."),
            [("ताम्यत् + यन्धम्", "यन्धम् is not a word; the word is अन्धम् (blind)."),
             ("ताम्यत्य + अन्धम्", "ताम्यत्य is not a form; the verb is ताम्यति (faints)."),
             ("ताम्यते + अन्धम्", "ए + अ would give ताम्यतेऽन्धम्, with ए kept and ऽ.")],
            "ताम्यति (faints) + अन्धम् (blind): इ + अ → य.",
            "इ + a different vowel → य् + that vowel."),
        multi("apply", 4, "Which features of the sores (arus) does unit 39 name?",
              [("They arise at the joints", "Right: पर्वसु, at the joints."),
               ("They are thick-rooted", "Right: स्थूलमूलानि."),
               ("They heal by themselves in a few days", "The unit says the opposite: most difficult to treat."),
               ("They are most difficult to treat", "Right: दुश्चिकित्स्यतमानि."),
               ("They arise only on the face", "The unit names the joints, not the face.")],
              [0, 1, 3],
              "At the joints, thick-rooted, most difficult to treat (and black-red).",
              "अरूंषि जायंते पर्वसु ... स्थूलमूलानि दुश्चिकित्स्यतमानि."),
        mcq("transfer", 5, "By the pattern of दुश्चिकित्स्यतम (most difficult to treat), what does प्रियतम mean?",
            ("Dearest, the most dear", "-तम marks the highest degree, as in दुश्चिकित्स्य-तम."),
            [("Dearer than one other", "'Dearer' would be -तर (प्रियतर), not -तम."),
             ("Not dear in the least", "Nothing in -तम makes a negative."),
             ("Made dear by another", "-तम is a degree suffix, not a causative.")],
            "प्रियतम = dearest, like दुश्चिकित्स्यतम = most difficult to treat.",
            "-तम = most (the highest degree).",
            teaches="The suffix -तम makes 'most': दुश्चिकित्स्य (hard to treat) + तम = most difficult to treat."),
    ],
}

# ---------------------------------------------------------------- unit 40
AUTHORED["40"] = {
    "title": "अन्ये तु सप्त त्वचो वदंति",
    "question": "By unit 40, how many skins do the others speak of?",
    "rule": ("Others (अन्ये), however (तु), speak of seven skins (सप्त त्वचः): a second view beside the six skins of "
             "units 31-39."),
    "limits": ("Prose. The 'others' are unnamed. The seven are named and measured from unit 41 on; this line names none."),
    "explain_hi": ("यह छोटी गद्य-पंक्ति एक मतान्तर, यानी दूसरा मत, आरम्भ करती है। "
                   "अब तक (इकाई ३१-३९) छह त्वचाएँ बताई गईं; ‘अन्ये तु’, यानी दूसरे लोग तो, सात त्वचाएँ कहते हैं। "
                   "ये दूसरे लोग कौन हैं, यह नहीं बताया गया। "
                   "सातों के नाम और माप इकाई ४१ से आते हैं। "
                   "‘त्वचो वदंति’ में त्वचः का विसर्ग घोष व से पहले ओ बना है।"),
    "hook": "छह नहीं, सात: दूसरों का मत।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 40, how many skins do the others speak of?",
            ("Seven", "सप्त त्वचः: seven skins."),
            [("Six", "Six is the view of units 31-39; the others say seven."),
             ("Five", "Five is not the number in unit 40."),
             ("Eight", "Eight is not the number in unit 40.")],
            "Others, however, speak of seven skins.",
            "अन्ये तु सप्त त्वचो वदंति."),
        order(1, "Put the words of unit 40 in the line's order.",
              ["अन्ये", "तु", "सप्त", "त्वचो", "वदंति"],
              "Others, however, seven skins speak of.",
              "अन्ये → तु → सप्त → त्वचो → वदंति."),
        match(2, "Match each word of unit 40 to its meaning.",
              [["अन्ये", "others"], ["तु", "but, however"], ["सप्त", "seven"], ["त्वचः", "skins"], ["वदन्ति", "they say"]],
              "Others, however, say there are seven skins.",
              "अन्ये, तु, सप्त, त्वचः, वदन्ति.", role="extend",
              teaches="अन्ये तु ... वदन्ति = 'others, however, say': it brings in another opinion (मतान्तर)."),
        mcq("discriminate", 3, "Why is त्वचः printed त्वचो before वदंति in unit 40?",
            ("अः becomes ओ before a voiced consonant", "व is a voiced consonant, so त्वचः + वदंति → त्वचो वदंति."),
            [("ओ is a plural ending of त्वच्", "The form is त्वचः; the ओ comes from sandhi."),
             ("अः becomes ओ before any consonant", "Before unvoiced sounds it stays or becomes श्/ष्/स्."),
             ("After अ the visarga drops before व", "After अ it becomes ओ here; the plain drop is after आ.")],
            "त्वचः + वदंति = त्वचो वदंति: अः before a voiced consonant → ओ.",
            "अः + voiced consonant → ओ."),
        fill(4, "In unit 40 the others say there are ____ skins. Type the number word in Devanagari or in English letters "
                "(e.g. dharma).",
             accepts("सप्त", None, "seven"),
             "सप्त = seven: अन्ये तु सप्त त्वचो वदंति.",
             "सप्त = seven, the others' count of the skins.",
             "अन्ये तु सप्त त्वचो वदंति.", role="apply"),
        mcq("transfer", 5, "By the rule of त्वचो वदंति, how is बालः + गच्छति (the boy goes) joined?",
            ("बालो गच्छति", "अः before the voiced ग becomes ओ, as त्वचः + वदंति."),
            [("बाला गच्छति", "The visarga drops this way after आ; बालः has a short अ."),
             ("बालर्गच्छति", "र् comes from a visarga after vowels other than अ and आ."),
             ("बालः गच्छति", "Before a voiced sound the visarga after अ does not stay.")],
            "बालः + गच्छति = बालो गच्छति, like त्वचः + वदंति = त्वचो वदंति.",
            "अः + voiced consonant → ओ.",
            teaches="A visarga after short अ becomes ओ before a voiced consonant: त्वचः + वदंति → त्वचो वदंति."),
    ],
}

# ---------------------------------------------------------------- unit 41
AUTHORED["41"] = {
    "title": "तत्रप्रथमा भासिनी नाम",
    "question": "By unit 41, what is the first of the seven skins, what does it make manifest, and how thick is it?",
    "rule": ("The first skin is Bhāsinī: it makes manifest (अवभासिनी) the colours (वर्ण) and the five chāyās beginning with "
             "kha (space); its measure is an eighteenth part of a vrīhi (rice grain, standard)."),
    "limits": ("Prose. chāyā is 'shadow, reflection' in the plainest sense (also lustre): no question on its exact sense. The "
               "five chāyās are not listed beyond 'beginning with kha'. vrīhi (Oryza sativa, standard) is here a unit of measure."),
    "explain_hi": ("सात त्वचाओं वाले मत में पहली त्वचा भासिनी है। "
                   "वह वर्णों को और ख यानी आकाश आदि पाँच छायाओं को प्रकट करती है (अवभासिनी)। "
                   "छाया का सीधा अर्थ छाया या प्रतिबिम्ब है, कान्ति भी हो सकता है; पाँचों छायाएँ यहाँ गिनाई नहीं गईं। "
                   "उसका माप व्रीहि यानी धान के दाने (Oryza sativa, मानक) का अठारहवाँ भाग है। "
                   "आगे की त्वचाओं के माप भी व्रीहि से दिए गए हैं: पहले उसके भाग, फिर एक और दो पूरे दाने।"),
    "hook": "भासिनी: रंग दिखाए, धान का अठारहवाँ भाग।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 41, what is the first skin of the seven called?",
            ("भासिनी", "तत्र प्रथमा भासिनी नाम: the first is named Bhāsinī."),
            [("लोहिनी", "Lohinī is the second (unit 42)."),
             ("रोहिणी", "Rohiṇī is the sixth (unit 44)."),
             ("श्वेता", "Śvetā is the third (unit 42).")],
            "The first of the seven is Bhāsinī.",
            "तत्र प्रथमा भासिनी नाम."),
        order(1, "Put these phrases of unit 41 in the line's order.",
              ["तत्रप्रथमा भासिनी नाम", "या वर्णानामवभासिनी", "खादीनां च पंचानांछायानां", "सा व्रीहेरष्टादशभागप्रमाणा"],
              "The first is named Bhāsinī, which makes manifest the colours and the five chāyās beginning with kha; it is of an "
              "eighteenth part of a vrīhi.",
              "तत्रप्रथमा भासिनी नाम → या वर्णानामवभासिनी → खादीनां च पंचानांछायानां → सा व्रीहेरष्टादशभागप्रमाणा."),
        match(2, "Match each word of unit 41 to its meaning.",
              [["अवभासिनी", "making manifest"], ["वर्ण", "colour"], ["पञ्च", "five"], ["ख", "space"],
               ["अष्टादशभाग", "an eighteenth part"]],
              "Bhāsinī makes manifest the colours and the five chāyās from kha; it is an eighteenth of a vrīhi.",
              "अवभासिनी, वर्ण, पञ्च, ख, अष्टादशभाग.", role="extend",
              teaches="-प्रमाणा = 'of the measure of': each of the seven skins is measured in parts of a vrīhi grain."),
        mcq("discriminate", 3, "Which split of व्रीहेरष्टादश is right?",
            ("व्रीहेः + अष्टादश", "After ए, the visarga becomes र् before a vowel."),
            [("व्रीहे + रष्टादश", "रष्टादश is not a word; the र् comes from the visarga."),
             ("व्रीहिः + अष्टादश", "इः would give व्रीहिरष्टादश; the data reads व्रीहेः."),
             ("व्रीहयः + अष्टादश", "अः + अ would give व्रीहयोऽष्टादश.")],
            "व्रीहेः (of a vrīhi) + अष्टादश (eighteen): एः + vowel → एर्.",
            "A visarga after a vowel other than अ/आ → र् before a vowel."),
        mcq("apply", 4, "By unit 41, what does Bhāsinī make manifest?",
            ("The colours and five chāyās from kha", "वर्णानामवभासिनी खादीनां च पंचानां छायानाम्."),
            [("The joints and the bones of the limbs", "Joints and bones are not named in unit 41."),
             ("The heat that digests all the food", "Digestion is not named in unit 41."),
             ("The sores that rise at the joints", "The sores belong to the sixth skin of the six (unit 39).")],
            "Bhāsinī makes manifest the colours and the five chāyās beginning with space.",
            "या वर्णानामवभासिनी खादीनां च पंचानां छायानाम्."),
        mcq("transfer", 5, "By the rule of व्रीहेरष्टादश, how is अग्नेः + अपि (even of fire) joined?",
            ("अग्नेरपि", "After ए, the visarga becomes र् before a vowel, as व्रीहेः + अष्टादश."),
            [("अग्नेऽपि", "ए + अ → एऽ only with no visarga; here the visarga gives र्."),
             ("अग्नोऽपि", "ओ comes from a visarga after short अ, not after ए."),
             ("अग्नयपि", "अय् comes from a bare ए before a vowel, not from एः.")],
            "अग्नेः + अपि = अग्नेरपि, like व्रीहेः + अष्टादश = व्रीहेरष्टादश.",
            "एः + vowel → एर्.",
            teaches="A visarga after ए becomes र् before a vowel: व्रीहेः + अष्टादश → व्रीहेरष्टादश."),
    ],
}

# ---------------------------------------------------------------- unit 42
AUTHORED["42"] = {
    "title": "द्वितीया लोहिनी नाम · तृतीया श्वेता नाम",
    "question": "By unit 42, what are the second and third skins named, and what are their measures?",
    "rule": ("Second skin: Lohinī, of a sixteenth part (षोडशभाग); third: Śvetā, of a twelfth part (द्वादशभाग). 'Of a vrīhi' "
             "is carried from unit 41, not printed here."),
    "limits": ("Two printed lines, prose; no verb (copula understood). 'Of a vrīhi' is understood from unit 41 and not "
               "supplied by the data. The skins are not described beyond name and measure."),
    "explain_hi": ("इस इकाई में दो छपी पंक्तियाँ हैं। "
                   "दूसरी त्वचा लोहिनी नाम की है, उसका माप सोलहवाँ भाग (षोडशभाग) है। "
                   "तीसरी श्वेता नाम की है, उसका माप बारहवाँ भाग (द्वादशभाग) है। "
                   "‘व्रीहि का’ शब्द यहाँ छपा नहीं; वह इकाई ४१ से समझा जाता है। "
                   "द्वितीया, तृतीया स्त्रीलिंग हैं, क्योंकि वे त्वच् (स्त्रीलिंग) के विशेषण हैं।"),
    "hook": "लोहिनी सोलहवाँ, श्वेता बारहवाँ भाग।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 42, what is the measure of Lohinī?",
            ("A sixteenth part", "षोडशभागप्रमाणा: of a sixteenth part."),
            [("A twelfth part", "A twelfth part is Śvetā's measure."),
             ("An eighteenth part", "An eighteenth part is Bhāsinī's (unit 41)."),
             ("Two whole grains", "Two grains is the seventh skin's (unit 45).")],
            "Lohinī, the second, is of a sixteenth part.",
            "द्वितीया लोहिनी नाम षोडशभागप्रमाणा."),
        order(1, "Put these words of unit 42 in the lines' order.",
              ["द्वितीया", "लोहिनी नाम", "षोडशभागप्रमाणा", "तृतीया", "श्वेता नाम", "द्वादशभागप्रमाणा"],
              "Second, named Lohinī, of a sixteenth part; third, named Śvetā, of a twelfth part.",
              "द्वितीया → लोहिनी नाम → षोडशभागप्रमाणा → तृतीया → श्वेता नाम → द्वादशभागप्रमाणा."),
        match(2, "Match each word of unit 42 to its meaning.",
              [["द्वितीया", "second"], ["तृतीया", "third"], ["षोडश", "sixteen"], ["द्वादश", "twelve"], ["भाग", "part"]],
              "Second (Lohinī) a sixteenth part; third (Śvetā) a twelfth part.",
              "द्वितीया, तृतीया, षोडश, द्वादश, भाग.", role="extend",
              teaches="षोडश = sixteen, द्वादश = twelve: the fraction of a vrīhi that measures each skin."),
        mcq("discriminate", 3, "Which pairing is right by unit 42?",
            ("Śvetā: the third, a twelfth part", "तृतीया श्वेता नाम द्वादशभागप्रमाणा."),
            [("Śvetā: the second, a sixteenth part", "The second, of a sixteenth part, is Lohinī."),
             ("Lohinī: the third, a twelfth part", "Lohinī is the second, of a sixteenth part."),
             ("Lohinī: the second, a twelfth part", "Lohinī's measure is a sixteenth part.")],
            "Lohinī = second, a sixteenth; Śvetā = third, a twelfth.",
            "द्वितीया लोहिनी षोडश-; तृतीया श्वेता द्वादश-."),
        multi("apply", 4, "Which statements fit unit 42?",
              [("The word vrīhi is printed in both lines", "Not printed: 'of a vrīhi' is carried from unit 41."),
               ("Lohinī is the second skin", "Right: द्वितीया लोहिनी नाम."),
               ("Lohinī's measure is an eighteenth part", "An eighteenth is Bhāsinī's; Lohinī's is a sixteenth."),
               ("Śvetā's measure is a twelfth part", "Right: द्वादशभागप्रमाणा.")],
              [1, 3],
              "Lohinī is second (a sixteenth), Śvetā third (a twelfth); vrīhi is understood from unit 41.",
              "द्वितीया लोहिनी ... तृतीया श्वेता ... द्वादशभागप्रमाणा."),
        mcq("transfer", 5, "द्वितीया agrees with the feminine त्वच्. With शाखा (branch, f.), how is the second branch said?",
            ("द्वितीया शाखा", "The feminine of द्वितीय ends in -आ, as द्वितीया (त्वक्)."),
            [("द्वितीयः शाखा", "द्वितीयः is masculine; शाखा is feminine."),
             ("द्वितीयं शाखा", "द्वितीयम् is neuter; शाखा is feminine."),
             ("द्वितीयी शाखा", "द्वितीय takes -आ in the feminine; -ई is for चतुर्थी, पञ्चमी.")],
            "द्वितीया शाखा = the second branch, as द्वितीया (त्वक्) = the second skin.",
            "An ordinal agrees in gender: द्वितीय → द्वितीया (f.).",
            teaches="Ordinals agree with their noun: with the feminine त्वच्, द्वितीय → द्वितीया, तृतीय → तृतीया."),
    ],
}

# ---------------------------------------------------------------- unit 43
AUTHORED["43"] = {
    "title": "चतुर्थीताम्रानामाष्टभागप्रमाणा · पंचमी वेदिनी नाम",
    "question": "By unit 43, what are the fourth and fifth skins named, and what are their measures?",
    "rule": ("Fourth skin: Tāmrā, of an eighth part (अष्टभाग); fifth: Vedinī, of a fifth part (पञ्चभाग). 'Of a vrīhi' is "
             "carried from unit 41."),
    "limits": ("Two printed lines, prose; no verb. The first line is printed without spaces. 'Of a vrīhi' is understood, not "
               "supplied. Nothing is said of the skins beyond name and measure."),
    "explain_hi": ("इस इकाई में दो छपी पंक्तियाँ हैं। "
                   "चौथी त्वचा ताम्रा नाम की है, उसका माप आठवाँ भाग (अष्टभाग) है। "
                   "पाँचवीं वेदिनी नाम की है, उसका माप पाँचवाँ भाग (पञ्चभाग) है। "
                   "पहली पंक्ति छपाई में बिना रिक्त स्थान के है: चतुर्थी ताम्रा नाम अष्टभागप्रमाणा। "
                   "‘व्रीहि का’ इकाई ४१ से समझा जाता है।"),
    "hook": "ताम्रा आठवाँ, वेदिनी पाँचवाँ भाग।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 43, what is the fifth skin named?",
            ("वेदिनी", "पंचमी वेदिनी नाम: the fifth is named Vedinī."),
            [("ताम्रा", "Tāmrā is the fourth."),
             ("रोहिणी", "Rohiṇī is the sixth (unit 44)."),
             ("श्वेता", "Śvetā is the third (unit 42).")],
            "The fifth skin is Vedinī.",
            "पंचमी वेदिनी नाम पंचभागप्रमाणा."),
        order(1, "Put these words of unit 43 in the lines' order.",
              ["चतुर्थी", "ताम्रा नाम", "अष्टभागप्रमाणा", "पंचमी", "वेदिनी नाम", "पंचभागप्रमाणा"],
              "Fourth, named Tāmrā, of an eighth part; fifth, named Vedinī, of a fifth part.",
              "चतुर्थी → ताम्रा नाम → अष्टभागप्रमाणा → पंचमी → वेदिनी नाम → पंचभागप्रमाणा."),
        match(2, "Match each word of unit 43 to its meaning.",
              [["चतुर्थी", "fourth"], ["पञ्चमी", "fifth"], ["अष्टभाग", "an eighth part"], ["पञ्चभाग", "a fifth part"]],
              "Fourth (Tāmrā) an eighth; fifth (Vedinī) a fifth.",
              "चतुर्थी, पञ्चमी, अष्टभाग, पञ्चभाग.", role="extend",
              teaches="चतुर्थी, पञ्चमी are feminine ordinals in -ई (fourth, fifth), agreeing with त्वच्."),
        mcq("discriminate", 3, "The print runs ताम्रानामाष्टभाग together. Which split of नामाष्टभाग is right?",
            ("नाम + अष्टभाग", "अ + अ → आ: नाम + अष्ट → नामाष्ट."),
            [("नामः + अष्टभाग", "नाम has no visarga; अः + अ would give नामोऽष्ट."),
             ("नामे + अष्टभाग", "ए + अ would give नामेऽष्ट, with ए kept."),
             ("नामा + ष्टभाग", "ष्टभाग is not a word; the numeral is अष्ट.")],
            "नाम (named) + अष्टभाग (an eighth part): अ + अ → आ.",
            "अ + अ → आ."),
        mcq("apply", 4, "By unit 43, which skin has the measure of an eighth part?",
            ("Tāmrā, the fourth", "चतुर्थी ताम्रा नाम अष्टभागप्रमाणा."),
            [("Vedinī, the fifth", "Vedinī is of a fifth part."),
             ("Lohinī, the second", "Lohinī is of a sixteenth part (unit 42)."),
             ("Rohiṇī, the sixth", "Rohiṇī is of one vrīhi (unit 44).")],
            "Tāmrā, the fourth, is of an eighth part.",
            "चतुर्थी ताम्रा नाम अष्टभागप्रमाणा."),
        mcq("transfer", 5, "By the rule of नाम + अष्ट → नामाष्ट, how is च + अपि (and also) joined?",
            ("चापि", "अ + अ → आ, as नाम + अष्ट → नामाष्ट."),
            [("चेपि", "ए comes from अ + इ, not from अ + अ."),
             ("चोपि", "ओ comes from अ + उ, not from अ + अ."),
             ("चऽपि", "ऽ marks an अ dropped after ए or ओ, not after अ.")],
            "च + अपि = चापि, like नाम + अष्टभाग = नामाष्टभाग.",
            "अ + अ → आ.",
            teaches="A short अ meeting a short अ gives long आ: नाम + अष्टभाग → नामाष्टभाग."),
    ],
}

# ---------------------------------------------------------------- unit 44
AUTHORED["44"] = {
    "title": "षष्ठीरोहिणी नाम व्रीहिप्रमाणा",
    "question": "By unit 44, what is the sixth skin named and what is its measure?",
    "rule": ("Sixth skin: Rohiṇī, of the measure of a vrīhi (rice grain, standard), a whole grain, not a part of one."),
    "limits": ("Prose; no verb. षष्ठीरोहिणी is two words run together in the print. Nothing is said of Rohiṇī beyond name "
               "and measure."),
    "explain_hi": ("छठी त्वचा रोहिणी नाम की है। "
                   "उसका माप पूरे एक व्रीहि यानी धान के दाने (Oryza sativa, मानक) का है, किसी भाग का नहीं। "
                   "पहली पाँच त्वचाओं के माप दाने के भाग थे (अठारहवाँ, सोलहवाँ, बारहवाँ, आठवाँ, पाँचवाँ)। "
                   "छपाई में ‘षष्ठीरोहिणी’ दो शब्द जुड़े हुए हैं: षष्ठी रोहिणी।"),
    "hook": "रोहिणी: पूरा एक धान।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 44, what is the measure of Rohiṇī?",
            ("One whole vrīhi grain", "व्रीहिप्रमाणा: of the measure of a vrīhi."),
            [("Two whole vrīhi grains", "Two grains is the seventh skin's (unit 45)."),
             ("A fifth part of a grain", "A fifth part is Vedinī's (unit 43)."),
             ("An eighth part of a grain", "An eighth part is Tāmrā's (unit 43).")],
            "Rohiṇī is of the measure of one vrīhi.",
            "षष्ठी रोहिणी नाम व्रीहिप्रमाणा."),
        order(1, "Put the words of unit 44 in the line's order.",
              ["षष्ठी", "रोहिणी", "नाम", "व्रीहिप्रमाणा"],
              "The sixth, Rohiṇī by name, of the measure of a vrīhi.",
              "षष्ठी → रोहिणी → नाम → व्रीहिप्रमाणा."),
        match(2, "Match each word of unit 44 to its meaning.",
              [["षष्ठी", "sixth"], ["नाम", "by name"], ["व्रीहि", "rice grain (standard)"], ["प्रमाण", "measure"]],
              "The sixth, named Rohiṇī, has the measure of a rice grain.",
              "षष्ठी, नाम, व्रीहि, प्रमाण.", role="extend",
              teaches="व्रीहिप्रमाणा = having the measure of a vrīhi: a whole grain, after five fractions."),
        mcq("discriminate", 3, "Which skin of the seven has exactly the measure of one vrīhi?",
            ("रोहिणी", "षष्ठी रोहिणी नाम व्रीहिप्रमाणा."),
            [("मांसधरा", "Māṃsadharā is of two vrīhis (unit 45)."),
             ("भासिनी", "Bhāsinī is of an eighteenth part (unit 41)."),
             ("वेदिनी", "Vedinī is of a fifth part (unit 43).")],
            "Rohiṇī, the sixth, is of one vrīhi.",
            "षष्ठी रोहिणी ... व्रीहिप्रमाणा."),
        mcq("apply", 4, "Unit 44 is printed षष्ठीरोहिणी. How is it read?",
            ("षष्ठी रोहिणी, two words run together", "The data: words run together in the print; no sandhi change."),
            [("षष्ठीर् ओहिणी, with an र् of sandhi", "ओहिणी is not a word; the name is रोहिणी."),
             ("षष्ठि + ईरोहिणी, a vowel joining", "ईरोहिणी is not a word; the ordinal is षष्ठी."),
             ("षष्ठ्या रोहिणी, an instrumental case", "The data reads षष्ठी, nominative: the sixth.")],
            "षष्ठीरोहिणी = षष्ठी रोहिणी: a missing space, nothing more.",
            "षष्ठी (sixth) + रोहिणी (name), run together."),
        mcq("transfer", 5, "By the pattern of व्रीहिप्रमाणा, what does अङ्गुलप्रमाणा (अङ्गुल, a finger-breadth) say of a layer?",
            ("Its measure is a finger-breadth", "-प्रमाणा = having the measure of, as व्रीहिप्रमाणा."),
            [("It has the shape of a finger", "प्रमाण is measure, not shape."),
             ("It covers all of the fingers", "प्रमाण says how large, not what it covers."),
             ("It is thinner than a finger", "Nothing in -प्रमाणा compares smaller or larger.")],
            "अङ्गुलप्रमाणा = of the measure of a finger-breadth, like व्रीहिप्रमाणा = of the measure of a vrīhi.",
            "X-प्रमाणा = having the measure of X.",
            teaches="-प्रमाणा after a measure word gives the size: व्रीहिप्रमाणा = of the measure of a rice grain."),
    ],
}

# ---------------------------------------------------------------- unit 45
AUTHORED["45"] = {
    "title": "सप्तमी मांसधरा नाम व्रीहिद्वयप्रमाणा",
    "question": "By unit 45, what is the seventh skin named and what is its measure?",
    "rule": ("Seventh skin: Māṃsadharā ('flesh-bearing'), of the measure of two vrīhis (व्रीहिद्वय, a pair of rice grains)."),
    "limits": ("Prose; no verb. The same name Māṃsadharā is given to the first kalā in unit 48 (data note); here it is a "
               "skin. Nothing is said of it beyond name and measure."),
    "explain_hi": ("सातवीं और अन्तिम त्वचा मांसधरा, यानी मांस धारण करने वाली, नाम की है। "
                   "उसका माप दो व्रीहि, यानी धान के दो दानों, का है (व्रीहिद्वय = दानों का जोड़ा)। "
                   "यही नाम इकाई ४८ में पहली कला को भी दिया गया है; यहाँ यह त्वचा है। "
                   "इस प्रकार सात त्वचाओं के माप बढ़ते क्रम में हैं: अठारहवाँ भाग से दो दानों तक।"),
    "hook": "मांसधरा: दो धान।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 45, what is the measure of the seventh skin?",
            ("Two vrīhi grains", "व्रीहिद्वयप्रमाणा: of the measure of a pair of vrīhis."),
            [("One vrīhi grain", "One grain is Rohiṇī's, the sixth (unit 44)."),
             ("A fifth of a grain", "A fifth part is Vedinī's (unit 43)."),
             ("A twelfth of a grain", "A twelfth part is Śvetā's (unit 42).")],
            "The seventh, Māṃsadharā, is of two vrīhis.",
            "सप्तमी मांसधरा नाम व्रीहिद्वयप्रमाणा."),
        order(1, "Put the words of unit 45 in the line's order.",
              ["सप्तमी", "मांसधरा", "नाम", "व्रीहिद्वयप्रमाणा"],
              "The seventh, Māṃsadharā by name, of the measure of two vrīhis.",
              "सप्तमी → मांसधरा → नाम → व्रीहिद्वयप्रमाणा."),
        match(2, "Match each word of unit 45 to its meaning.",
              [["सप्तमी", "seventh"], ["मांस", "flesh"], ["धरा", "bearing, holding"], ["द्वय", "pair"],
               ["प्रमाण", "measure"]],
              "The seventh, flesh-bearing, has the measure of a pair of vrīhis.",
              "सप्तमी, मांस, धरा, द्वय, प्रमाण.", role="extend",
              teaches="-धरा = 'bearing, holding': मांसधरा = flesh-bearing."),
        mcq("discriminate", 3, "Which is right about the name मांसधरा in this chapter?",
            ("It names this skin and also the first kalā", "Data note: the first kalā of unit 48 has the same name."),
            [("It names only this skin, no other layer", "Unit 48 gives the same name to the first kalā."),
             ("It names the sixth skin of the six-skin list", "The sixth of the six is Prāṇadharā (unit 38)."),
             ("It names the second kalā, the blood-bearing", "The second kalā is Raktadharā (unit 49).")],
            "Māṃsadharā is the seventh skin here and the first kalā in unit 48.",
            "सप्तमी मांसधरा (त्वक्); प्रथमा मांसधरा (कला)."),
        mcq("apply", 4, "What does the name मांसधरा of unit 45 mean?",
            ("Flesh-bearing", "मांस (flesh) + धरा (bearing)."),
            [("Blood-bearing", "Blood-bearing is असृग्धरा or रक्तधरा."),
             ("Fat-bearing", "Fat-bearing is मेदोधरा (unit 50)."),
             ("Life-bearing", "Life-bearing is प्राणधरा (unit 38).")],
            "मांसधरा = flesh-bearing.",
            "मांस + धरा = flesh-bearing."),
        mcq("transfer", 5, "By the pattern of व्रीहिद्वय (a pair of vrīhis), what does नेत्रद्वय mean?",
            ("The pair of eyes", "द्वय = pair, as in व्रीहिद्वय."),
            [("The second eye", "'Second' would be द्वितीय, not द्वय."),
             ("Two eye diseases", "Nothing in नेत्रद्वय names a disease."),
             ("The eyes and ears", "द्वय is a pair of the same thing, the eyes.")],
            "नेत्रद्वय = the pair of eyes, like व्रीहिद्वय = a pair of vrīhis.",
            "X-द्वय = a pair of X.",
            teaches="-द्वय after a noun means 'a pair of': व्रीहिद्वय = two rice grains."),
    ],
}

# ---------------------------------------------------------------- unit 46
AUTHORED["46"] = {
    "title": "यस्तु ध्वात्वाशयांतरेषु क्लेदोऽवतिष्ठते",
    "question": "By unit 46, what is a kalā, and how does it come about?",
    "rule": ("The moisture (क्लेद) that stays between the seats, cooked by their own heats, covered by snāyu, śleṣman and "
             "jarāyu, is the dhātus' essence like heartwood; with rasa as remainder, from smallness, it is called kalā."),
    "limits": ("Prose. 'Dhātu-seats' rests on a possible correction (printed ध्वात्वाशय): no question on it. The case of "
               "काष्ठ is uncertain. snāyu = ligament and jarāyu = membrane are probable; śleṣman (Kapha) may also mean a "
               "mucous layer: no question on these identifications. kalā is kept as the Sanskrit term."),
    "explain_hi": ("यह गद्य-पंक्ति बताती है कि कला क्या है। "
                   "जो क्लेद यानी नमी आशयों (सम्भवतः धातुओं के आशयों) के बीच के स्थानों में ठहरती है, अपनी-अपनी ऊष्माओं से पकती है, "
                   "और स्नायु, श्लेष्मा तथा जरायु (सम्भवतः झिल्ली) से ढकी रहती है, वह लकड़ी के सार की तरह धातुओं का सार है। "
                   "अल्प होने के कारण उसमें रस शेष रहता है, और उसका नाम कला है। "
                   "छपा ‘ध्वात्वाशय’ सम्भवतः ‘धात्वाशय’ की छपाई-भूल है; यह सुधार केवल सम्भावित है। "
                   "कला को आधुनिक नाम दिए बिना संस्कृत शब्द ही रखा गया है।"),
    "hook": "पकी, ढकी नमी, लकड़ी के सार जैसी: कला।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 46, what is it that, so formed, is called kalā?",
            ("A moisture that stays and is cooked", "क्लेदोऽवतिष्ठते ... विपक्वः ... कलासंज्ञः."),
            [("A bone that grows between joints", "No bone is named; the kalā is a moisture (kleda)."),
             ("A clot of blood under the skin", "No clot is named; the kalā is a moisture."),
             ("A hair that grows out of flesh", "No hair is named; the kalā is a moisture.")],
            "The kleda that stays between the seats and is cooked by the heats is named kalā.",
            "यः क्लेदोऽवतिष्ठते ... कलासंज्ञः."),
        order(1, "Put these phrases of unit 46 in the line's order.",
              ["यस्तु ध्वात्वाशयांतरेषु क्लेदोऽवतिष्ठते", "यथास्वमूष्माभिर्विपक्कः", "स्नायुश्लेष्मजरायुच्छन्नः",
               "काष्ठइव सारो", "धातुसारः", "रसशेषोऽल्पत्वात्कलासंज्ञः"],
              "The moisture that stays ..., cooked by its own heats, covered by snāyu, śleṣman and jarāyu, like heartwood, "
              "the essence of the dhātus, with rasa as remainder from smallness, is named kalā.",
              "क्लेदोऽवतिष्ठते → विपक्कः → ...च्छन्नः → काष्ठइव सारो → धातुसारः → कलासंज्ञः."),
        match(2, "Match each word of unit 46 to its meaning.",
              [["क्लेद", "moisture"], ["ऊष्मन्", "heat, warmth"], ["विपक्व", "well cooked"], ["छन्न", "covered"],
               ["सार", "heartwood, essence"], ["संज्ञा", "name"]],
              "Moisture, cooked by heats, covered, the essence like heartwood, named kalā.",
              "क्लेद, ऊष्मन्, विपक्व, छन्न, सार, संज्ञा.", role="extend",
              teaches="कलासंज्ञः = having the name kalā: संज्ञा = name."),
        mcq("discriminate", 3, "Which split of रसशेषोऽल्पत्वात् is right?",
            ("रसशेषः + अल्पत्वात्", "अः + अ → ओ, and the second अ drops, marked ऽ."),
            [("रसशेषे + अल्पत्वात्", "ए + अ would give रसशेषेऽल्पत्वात्, with ए."),
             ("रसशेषः + ल्पत्वात्", "ल्पत्वात् is not a word; the word is अल्पत्वात्."),
             ("रसशेषम् + अल्पत्वात्", "म् before a vowel stays: रसशेषमल्पत्वात्.")],
            "रसशेषः (with rasa as remainder) + अल्पत्वात् (from smallness): अः + अ → ओऽ.",
            "अः + अ → ओऽ."),
        multi("apply", 4, "By unit 46, which cover the moisture that becomes kalā?",
              [("अस्थि", "Bone is not named among the coverings."),
               ("स्नायु", "Right: स्नायु is the first of the three."),
               ("केश", "Hair is not named among the coverings."),
               ("श्लेष्मन्", "Right: श्लेष्म- is the second."),
               ("जरायु", "Right: जरायु is the third.")],
              [1, 3, 4],
              "It is covered by snāyu, śleṣman and jarāyu: स्नायुश्लेष्मजरायुच्छन्नः.",
              "स्नायु-श्लेष्म-जरायु-च्छन्नः."),
        mcq("transfer", 5, "By the rule of रसशेषोऽल्पत्वात्, how is देवः + अयम् (this is a god) joined?",
            ("देवोऽयम्", "अः + अ → ओ, the अ marked ऽ, as रसशेषः + अल्पत्वात्."),
            [("देवायम्", "आ comes from अ + अ with no visarga."),
             ("देवरयम्", "र् comes from a visarga after vowels other than अ and आ."),
             ("देव अयम्", "The visarga drops this way before vowels other than अ.")],
            "देवः + अयम् = देवोऽयम्, like रसशेषः + अल्पत्वात् = रसशेषोऽल्पत्वात्.",
            "अः + अ → ओऽ.",
            teaches="A visarga after short अ before short अ: अः → ओ and the अ drops (ऽ): रसशेषः + अल्पत्वात् → रसशेषोऽल्पत्वात्."),
    ],
}

# ---------------------------------------------------------------- unit 47
AUTHORED["47"] = {
    "title": "ता ध्वात्वाशयांतरमर्यादाः सप्त कलाः",
    "question": "By unit 47, how many kalās are there, and what are they said to be?",
    "rule": ("Those (ताः) are the seven kalās, the boundaries (मर्यादा) of the spaces between the seats (आशय)."),
    "limits": ("Prose; no verb. 'Dhātu-seats' rests on a possible correction (printed ध्वात्वाशय, as in unit 46): no "
               "question on it. The kalās are named from unit 48 on."),
    "explain_hi": ("यह पंक्ति इकाई ४६ की परिभाषा के बाद कहती है: वे सात कलाएँ हैं। "
                   "वे आशयों (सम्भवतः धातुओं के आशयों) के बीच के स्थानों की मर्यादाएँ, यानी सीमाएँ, हैं। "
                   "छपा ‘ध्वात्वाशय’ इकाई ४६ की तरह सम्भवतः ‘धात्वाशय’ की भूल है। "
                   "सातों कलाओं के नाम इकाई ४८ से आते हैं। "
                   "‘ता ध्वा...’ में ताः का विसर्ग घोष ध से पहले लुप्त हुआ है।"),
    "hook": "सात कलाएँ: आशयों के बीच की सीमाएँ।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 47, what are the kalās said to be?",
            ("Boundaries of the spaces between seats", "-अन्तरमर्यादाः: boundaries of the spaces between."),
            [("The roots from which the hairs grow", "Hair is not named in unit 47."),
             ("The seats of all the skin diseases", "Seats of skin diseases belong to the skins (units 35-37)."),
             ("The paths of food in the belly", "Food paths are not named in unit 47.")],
            "The seven kalās are the boundaries of the spaces between the seats.",
            "ता ...आशयान्तरमर्यादाः सप्त कलाः."),
        order(1, "Put the words of unit 47 in the line's order.",
              ["ता", "ध्वात्वाशयांतरमर्यादाः", "सप्त", "कलाः"],
              "Those, the boundaries of the spaces between the seats, are the seven kalās.",
              "ता → ध्वात्वाशयांतरमर्यादाः → सप्त → कलाः."),
        match(2, "Match each word of unit 47 to its meaning.",
              [["ताः", "those"], ["अन्तर", "space between"], ["आशय", "seat, receptacle"], ["मर्यादा", "boundary"],
               ["सप्त", "seven"]],
              "Those seven kalās are the boundaries of the spaces between the seats.",
              "ताः, अन्तर, आशय, मर्यादा, सप्त.", role="extend",
              teaches="मर्यादा = boundary, limit: the kalās mark off the spaces between the seats."),
        mcq("discriminate", 3, "Why is ताः printed ता before ध्वात्वाशय- in unit 47?",
            ("After आ, the visarga drops before a voiced sound", "ध is voiced, so ताः + ध्वा- → ता ध्वा-."),
            [("ता is the singular form, 'she'", "The singular is सा; the data reads plural ताः."),
             ("After आ, the visarga becomes ओ before ध", "ओ comes from a visarga after short अ."),
             ("The visarga drops before every consonant", "Before unvoiced sounds it stays or changes.")],
            "ताः + ध्वा... = ता ध्वा...: आः before a voiced sound loses its visarga.",
            "आः + voiced sound → आ."),
        fill(4, "Unit 47 names the seven ____ (membrane-like layers). Type the word in Devanagari or in English letters "
                "(e.g. dharma).",
             accepts("कलाः", None, "कला", "kala", "kalah", "kalas"),
             "सप्त कलाः: the seven kalās.",
             "कला = a membrane-like layer; there are seven.",
             "ता ... सप्त कलाः.", role="apply"),
        mcq("transfer", 5, "By the rule of ता ध्वा-, how is अश्वाः + धावन्ति (the horses run) joined?",
            ("अश्वा धावन्ति", "आः before the voiced ध loses its visarga, as ताः + ध्वा-."),
            [("अश्वो धावन्ति", "ओ comes from a visarga after short अ, not after आ."),
             ("अश्वार्धावन्ति", "र् comes after vowels other than अ and आ."),
             ("अश्वाः धावन्ति", "Before a voiced sound the visarga after आ does not stay.")],
            "अश्वाः + धावन्ति = अश्वा धावन्ति, like ताः + ध्वा- = ता ध्वा-.",
            "आः + voiced sound → आ.",
            teaches="A visarga after आ is dropped before a voiced sound: ताः + ध्वात्वाशय- → ता ध्वात्वाशय-."),
    ],
}

# ---------------------------------------------------------------- unit 48
AUTHORED["48"] = {
    "title": "तासां प्रथमामांसधरा नाम",
    "question": "By unit 48, what is the first kalā, and what spreads in it, like what?",
    "rule": ("First kalā: Māṃsadharā. In it, in the flesh, the networks (प्रतान) of sirā, snāyu, dhamanī and srotas spread, "
             "as those of lotus-fibres (बिस) and stalks (मृणाल) do in muddy water on the ground."),
    "limits": ("Sirā = vein and dhamanī = artery are probable (not sharply separated in all texts); snāyu = ligament "
               "probable; srotas kept as the doctrinal term. Spelling flags (srotāsām, -ṃnāṃ, pratānā) are possible print "
               "slips; the sense is clear. Lotus = Nelumbo nucifera (standard)."),
    "explain_hi": ("सात कलाओं में पहली मांसधरा है; यही नाम इकाई ४५ में सातवीं त्वचा का भी था। "
                   "इसमें, मांस में, सिरा (सम्भवतः शिरा), स्नायु (सम्भवतः स्नायुबन्ध), धमनी (सम्भवतः रक्तवाहिनी) और स्रोतस् "
                   "के फैले हुए जाल (प्रतान) होते हैं। "
                   "उपमा: जैसे भूमि पर कीचड़ वाले पानी में बिस और मृणाल, यानी कमल (Nelumbo nucifera, मानक) के रेशे और नाल, फैले रहते हैं। "
                   "‘स्रोतासां’, ‘-लांनां’ और ‘प्रताना’ में छपाई की सम्भावित भूलें हैं; अर्थ स्पष्ट है।"),
    "hook": "मांस में नलियों का जाल, जैसे कीचड़ में कमलनाल।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 48, what is the first kalā named?",
            ("मांसधरा", "तासां प्रथमा मांसधरा नाम."),
            [("रक्तधरा", "Raktadharā is the second kalā (unit 49)."),
             ("मेदोधरा", "Medodharā is the third kalā (unit 50)."),
             ("श्लेष्मधरा", "Śleṣmadharā is the fourth kalā (unit 51).")],
            "The first kalā is Māṃsadharā.",
            "तासां प्रथमा मांसधरा नाम."),
        order(1, "Put the structures spreading in the flesh in unit 48 in the line's order.",
              ["सिरा", "स्नायु", "धमनी", "स्रोतस्"],
              "Sirā, snāyu, dhamanī, srotas: their networks spread in the flesh.",
              "सिरा → स्नायु → धमनी → स्रोतस्."),
        match(2, "Match each word of unit 48 to its meaning.",
              [["मांसे", "in the flesh"], ["पङ्कोदके", "in muddy water"], ["बिस", "lotus root-fibre"],
               ["मृणाल", "lotus stalk"], ["प्रतान", "spreading network"]],
              "In the flesh the networks spread like lotus-fibres and stalks in muddy water.",
              "मांसे, पङ्कोदके, बिस, मृणाल, प्रतान.", role="extend",
              teaches="प्रतान = a spreading network of tendrils: the vessels and channels spread in the flesh this way."),
        mcq("discriminate", 3, "Which split of पंकोदके is right?",
            ("पङ्क + उदके", "अ + उ → ओ: पङ्क + उदके → पङ्कोदके."),
            [("पङ्कः + उदके", "अः + उ would give पङ्क उदके, the visarga lost."),
             ("पङ्को + दके", "दके is not a word; the word is उदके (in water)."),
             ("पङ्क + ओदके", "ओदक is not a word; water is उदक.")],
            "पङ्क (mud) + उदके (in water): अ + उ → ओ.",
            "अ + उ → ओ."),
        mcq("apply", 4, "In the simile of unit 48, what are the networks in the flesh likened to?",
            ("Lotus-fibres and stalks in muddy water", "भूमाविव पङ्कोदके बिसमृणालानां प्रतानाः."),
            [("Roots of a tree deep in the dry ground", "No tree roots are named; the simile is of lotus."),
             ("Threads of a spider's web on a wall", "No web is named; the simile is of lotus."),
             ("Cracks that open in earth in summer", "No cracks are named; the simile is of lotus.")],
            "Like the spreading lotus-fibres and stalks in muddy water on the ground.",
            "भूमाविव पङ्कोदके बिसमृणालानां प्रतानाः."),
        mcq("transfer", 5, "By the rule of पङ्क + उदके, how is नील + उत्पलम् (blue lotus) joined?",
            ("नीलोत्पलम्", "अ + उ → ओ, as पङ्क + उदके → पङ्कोदके."),
            [("नीलौत्पलम्", "औ comes from अ + ओ or औ, not from अ + उ."),
             ("नीलुत्पलम्", "अ does not simply vanish before उ; they merge into ओ."),
             ("नीलात्पलम्", "आ comes from अ + अ, not from अ + उ.")],
            "नील + उत्पलम् = नीलोत्पलम्, like पङ्क + उदके = पङ्कोदके.",
            "अ + उ → ओ.",
            teaches="अ + उ join as ओ: पङ्क + उदके → पङ्कोदके."),
    ],
}

# ---------------------------------------------------------------- unit 49
AUTHORED["49"] = {
    "title": "द्वितीया रक्तधरा नाम",
    "question": "By unit 49, where is the second kalā, where is blood especially, and how does it flow from a cut?",
    "rule": ("Second kalā: Raktadharā, inside the flesh. Blood (शोणित) is in it, especially in the sirā, spleen and liver; "
             "from a cut (क्षत) the blood flows like milk from a milky tree."),
    "limits": ("'From the flesh' rests on a possible correction (printed मांशात्): no question on it. Sirā = vein is "
               "probable; plīhan = spleen and yakṛt = liver standard. The milky tree (latex) is not named."),
    "explain_hi": ("दूसरी कला रक्तधरा नाम की है; वह मांस के भीतर है। "
                   "उसमें शोणित यानी रक्त रहता है, और विशेष रूप से सिरा (सम्भवतः शिरा), प्लीहा (तिल्ली, मानक) और यकृत (जिगर, मानक) में। "
                   "कटने पर (क्षतात्) क्षतज, यानी घाव से जन्मा रक्त, वैसे बहता है जैसे दूध वाले (क्षीरी) वृक्ष से दूध। "
                   "छपा ‘मांशात्’ सम्भवतः ‘मांसात्’ (मांस से) की भूल है; यह सुधार सम्भावित है। "
                   "कौन-सा दूधिया वृक्ष, यह नहीं कहा गया।"),
    "hook": "कटे तो रक्त ऐसे बहे, जैसे दूधिया पेड़ से दूध।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 49, what is the second kalā named?",
            ("रक्तधरा", "द्वितीया रक्तधरा नाम."),
            [("मेदोधरा", "Medodharā is the third kalā (unit 50)."),
             ("पित्तधरा", "Pittadharā is the sixth kalā."),
             ("पुरीषधरा", "Purīṣadharā is the fifth kalā.")],
            "The second kalā is Raktadharā, blood-bearing.",
            "द्वितीया रक्तधरा नाम."),
        order(1, "Put these phrases of unit 49 in the line's order.",
              ["द्वितीया रक्तधरा नाम", "मांसस्याभ्यंतरतः", "तस्यां शोणितं", "विशेषतश्च सिराप्लीहयकृत्सु भवति",
               "क्षतात्क्षतजं", "वृक्षादिव क्षीरिणः क्षीरं प्रवर्त्तते"],
              "The second, Raktadharā, inside the flesh; in it is blood, especially in sirā, spleen and liver; from a cut "
              "the blood flows like milk from a milky tree.",
              "रक्तधरा → मांसस्याभ्यंतरतः → तस्यां शोणितं → विशेषतश्च ... भवति → क्षतात्क्षतजं → वृक्षादिव ... प्रवर्त्तते."),
        match(2, "Match each word of unit 49 to its meaning.",
              [["शोणित", "blood"], ["प्लीहन्", "spleen"], ["यकृत्", "liver"], ["क्षतज", "blood, lit. wound-born"],
               ["क्षीरिन्", "milk-bearing (tree)"]],
              "Blood is in it, especially in the spleen and liver; the wound-born blood flows like milk from a milky tree.",
              "शोणित, प्लीहन्, यकृत्, क्षतज, क्षीरिन्.", role="extend",
              teaches="क्षतज = क्षत (wound) + ज (born): a name for blood that flows from a cut."),
        mcq("discriminate", 3, "Which split of वृक्षादिव is right?",
            ("वृक्षात् + इव", "त् before a vowel becomes द्: वृक्षात् + इव → वृक्षादिव."),
            [("वृक्षः + इव", "अः + इ would give वृक्ष इव, with no द्."),
             ("वृक्षा + दिव", "दिव is not the word; the particle is इव (like)."),
             ("वृक्षम् + इव", "म् before a vowel stays: वृक्षमिव.")],
            "वृक्षात् (from a tree) + इव (like): त् + vowel → द्.",
            "त् + vowel → द्."),
        multi("apply", 4, "By unit 49, where especially is the blood?",
              [("In the sirā", "Right: सिरा- is named first."),
               ("In the joints", "The joints are made firm by Kapha (unit 51), not named here."),
               ("In the spleen", "Right: प्लीह-."),
               ("In the large bones", "The large bones hold majjā (unit 50)."),
               ("In the liver", "Right: यकृत्सु.")],
              [0, 2, 4],
              "Especially in the sirā, spleen and liver: विशेषतश्च सिराप्लीहयकृत्सु.",
              "विशेषतश्च सिराप्लीहयकृत्सु भवति."),
        mcq("transfer", 5, "By the rule of वृक्षादिव, how is जगत् + ईशः (lord of the world) joined?",
            ("जगदीशः", "त् before a vowel becomes द्, as वृक्षात् + इव → वृक्षादिव."),
            [("जगतीशः", "Before a vowel the त् becomes द्; it does not stay."),
             ("जगन्नीशः", "त् may become न् (optionally) only before a nasal, not before ई."),
             ("जगदिशः", "The long ई of ईशः stays long: -दीशः.")],
            "जगत् + ईशः = जगदीशः, like वृक्षात् + इव = वृक्षादिव.",
            "त् + vowel → द्.",
            teaches="A final त् becomes द् before a vowel: वृक्षात् + इव → वृक्षादिव."),
    ],
}

# ---------------------------------------------------------------- unit 50
AUTHORED["50"] = {
    "title": "तृतीया मेदोधरा नाम",
    "question": "By unit 50, where is the fat of the third kalā, and what is it called in the head and in the large bones?",
    "rule": ("Third kalā: Medodharā. Fat (मेदस्) is in it, in the belly and in the small bones, with blood; in the head, "
             "covered by the skull, it is called mastiṣka; in the large bones it is majjā (marrow)."),
    "limits": ("Low confidence. मस्तु लुंग- read as mastuluṅga is conjectural: no question on it. medas, mastiṣka (brain) and "
               "majjā (marrow) are standard. The last clause has no verb ('it is' understood)."),
    "explain_hi": ("तीसरी कला मेदोधरा, यानी मेद धारण करने वाली, है; इस इकाई का विश्वास निम्न है। "
                   "मेद यानी चर्बी उसमें, उदर में और छोटी अस्थियों में रक्त के साथ रहता है। "
                   "वही सिर में, कपाल से ढका हुआ, मस्तिष्क नाम वाला है। "
                   "अनुमानित पाठ पर उसे मस्तुलुंग भी कहा गया है; छपाई में ‘मस्तु’ और ‘लुंगारख्यं’ अलग हैं, इसलिए यह पक्का नहीं। "
                   "बड़ी अस्थियों में वह मज्जा है।"),
    "hook": "मेद: पेट में मेद, सिर में मस्तिष्क, बड़ी हड्डी में मज्जा।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 50, what is the fat in the large bones?",
            ("Majjā, the marrow", "स्थूलास्थिषु तु मज्जा."),
            [("Mastiṣka, the brain", "Mastiṣka is its name in the head."),
             ("Kleda, the moisture", "Kleda is the moisture of unit 46."),
             ("Śleṣman, the Kapha", "Śleṣman makes the joints firm (unit 51).")],
            "In the large bones it is majjā.",
            "स्थूलास्थिषु तु मज्जा."),
        order(1, "Put the places of unit 50 in the line's order.",
              ["उदरे", "अण्वस्थिषु", "शिरसि", "स्थूलास्थिषु"],
              "In the belly, in the small bones, in the head, in the large bones.",
              "उदरे → अण्वस्थिषु → शिरसि → स्थूलास्थिषु."),
        match(2, "Match each word of unit 50 to its meaning.",
              [["उदर", "belly"], ["अणु", "small"], ["कपाल", "skull"], ["स्थूल", "large"], ["मज्जा", "marrow"]],
              "Fat in the belly and small bones; in the head under the skull; marrow in the large bones.",
              "उदर, अणु, कपाल, स्थूल, मज्जा.", role="extend",
              teaches="The one medas has different names by place: mastiṣka in the head, majjā in the large bones."),
        mcq("discriminate", 3, "Which split of मेदोधरा is right?",
            ("मेदस् + धरा", "Final -अस् (visarga) becomes ओ before a voiced consonant: मेदोधरा."),
            [("मेद + उधरा", "उधरा is not a word; the word is धरा (bearing)."),
             ("मेदे + धरा", "ए would stay before ध (मेदेधरा); it gives no ओ."),
             ("मेदम् + धरा", "म् before a consonant would give मेदंधरा.")],
            "मेदस् (fat) + धरा (bearing): -अस् before the voiced ध → ओ.",
            "अः (from -अस्) + voiced consonant → ओ."),
        mcq("apply", 4, "By unit 50, what is this same fat called in the head, covered by the skull?",
            ("मस्तिष्क", "शिरसि कपालप्रतिच्छन्नं मस्तिष्काख्यम्."),
            [("मज्जा", "Majjā is its name in the large bones."),
             ("क्लेद", "Kleda is the moisture of unit 46."),
             ("शोणित", "Śoṇita is the blood of unit 49.")],
            "In the head, under the skull, it is called mastiṣka.",
            "तदेव च शिरसि कपालप्रतिच्छन्नं मस्तिष्काख्यम्."),
        mcq("transfer", 5, "By the rule of मेदस् + धरा → मेदोधरा, how is मनस् + रथ (a wish) joined?",
            ("मनोरथ", "-अस् before the voiced र becomes ओ, as मेदस् + धरा."),
            [("मनारथ", "आ appears when the visarga after आ drops, not after अ."),
             ("मनर्रथ", "र् comes from a visarga after vowels other than अ/आ."),
             ("मनस्रथ", "The स् does not stay before a voiced sound.")],
            "मनस् + रथ = मनोरथ, like मेदस् + धरा = मेदोधरा.",
            "-अस् + voiced consonant → ओ.",
            teaches="A final -अस् becomes ओ before a voiced consonant: मेदस् + धरा → मेदोधरा."),
    ],
}

# ---------------------------------------------------------------- unit 51
AUTHORED["51"] = {
    "title": "चतुर्थी श्लेष्मधरा नाम",
    "question": "By unit 51, what is the fourth kalā, and what does its śleṣman do to the joints?",
    "rule": ("Fourth kalā: Śleṣmadharā ('Kapha-bearing'). Joined (आश्लेषित) by the śleṣman (Kapha), all the joints "
             "(सर्वसन्धयः) become firm (दृढ)."),
    "limits": ("Low confidence. 'Situated in it' rests on a possible correction (printed तस्तस्थेन); the last word "
               "सोपांगावाक्षाः is unintelligible (conjecture: with subsidiary parts): no question on either. The doubled "
               "avagraha is a print habit."),
    "explain_hi": ("चौथी कला श्लेष्मधरा, यानी श्लेष्मा (कफ) धारण करने वाली, है; इस इकाई का विश्वास निम्न है। "
                   "श्लेष्मा से जुड़ी हुई (आश्लेषिताः) सब सन्धियाँ, यानी जोड़, दृढ़ हो जाती हैं। "
                   "छपा ‘तस्तस्थेन’ सम्भवतः ‘तत्स्थेन’ (उसमें स्थित) है; यह सुधार सम्भावित है। "
                   "अन्तिम छपा शब्द ‘सोपांगावाक्षाः’ अस्पष्ट है; ‘उपांग अवयवों सहित’ केवल अनुमान है। "
                   "इन दोनों पर कोई प्रश्न नहीं।"),
    "hook": "कफ जोड़े, जोड़ दृढ़।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 51, what is the fourth kalā named?",
            ("Śleṣmadharā", "चतुर्थी श्लेष्मधरा नाम."),
            [("Purīṣadharā", "Purīṣadharā is the fifth kalā."),
             ("Pittadharā", "Pittadharā is the sixth kalā."),
             ("Medodharā", "Medodharā is the third kalā (unit 50).")],
            "The fourth kalā is Śleṣmadharā.",
            "चतुर्थी श्लेष्मधरा नाम."),
        order(1, "Put these words of unit 51 in the line's order.",
              ["चतुर्थी श्लेष्मधरा नाम", "श्लेष्मणाऽऽश्लेषिताः", "सर्वसंधयो", "दृढा भवंति"],
              "The fourth, Śleṣmadharā; joined by the śleṣman, all the joints become firm.",
              "चतुर्थी श्लेष्मधरा नाम → श्लेष्मणाऽऽश्लेषिताः → सर्वसंधयो → दृढा भवंति."),
        match(2, "Match each word of unit 51 to its meaning.",
              [["श्लेष्मन्", "Kapha"], ["आश्लेषित", "joined, clasped"], ["सन्धि", "joint"], ["दृढ", "firm"],
               ["भवन्ति", "become"]],
              "Joined by Kapha, all the joints become firm.",
              "श्लेष्मन्, आश्लेषित, सन्धि, दृढ, भवन्ति.", role="extend",
              teaches="आश्लेषित = joined, clasped: the śleṣman holds the joints together."),
        mcq("discriminate", 3, "Which split of श्लेष्मणाऽऽश्लेषिताः is right?",
            ("श्लेष्मणा + आश्लेषिताः", "आ + आ → आ; the doubled ऽ is a print habit."),
            [("श्लेष्मणः + आश्लेषिताः", "अः + आ would give श्लेष्मण आश्लेषिताः."),
             ("श्लेष्मणि + आश्लेषिताः", "इ + आ would give श्लेष्मण्याश्लेषिताः."),
             ("श्लेष्मणे + आश्लेषिताः", "ए + आ would give श्लेष्मणयाश्लेषिताः or श्लेष्मण आश्लेषिताः.")],
            "श्लेष्मणा (by śleṣman) + आश्लेषिताः (joined): आ + आ → आ.",
            "आ + आ → आ."),
        mcq("apply", 4, "By unit 51, what happens to the joints joined by śleṣman?",
            ("They become firm", "सर्वसंधयो दृढा भवंति."),
            [("They become loose", "The unit says firm (दृढ), not loose."),
             ("They fill with fat", "Fat is the third kalā's (unit 50)."),
             ("They turn very hot", "Heat is not named in unit 51.")],
            "All the joints become firm.",
            "सर्वसन्धयो दृढा भवन्ति."),
        mcq("transfer", 5, "By the rule of श्लेष्मणा + आश्लेषिताः, how is विद्या + आलयः (school) joined?",
            ("विद्यालयः", "आ + आ → आ, as श्लेष्मणा + आश्लेषिताः."),
            [("विद्येलयः", "ए comes from अ/आ + इ, not from आ + आ."),
             ("विद्यौलयः", "औ comes from अ/आ + ओ/औ, not from आ + आ."),
             ("विद्ययलयः", "No य् arises between आ and आ; they merge into आ.")],
            "विद्या + आलयः = विद्यालयः, like श्लेष्मणा + आश्लेषिताः = श्लेष्मणाऽऽश्लेषिताः.",
            "आ + आ → आ.",
            teaches="Two आ sounds merge into one आ: श्लेष्मणा + आश्लेषिताः → श्लेष्मणाश्लेषिताः (printed with ऽऽ)."),
    ],
}


# ===================================================================== NOTES_HI
NOTES_HI = {
    "39": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। दोनों सम्बन्ध-वाक्य (यस्याम्, याम्) इकाई ३८ की छठी त्वचा (प्राणधरा) की ओर हैं "
           "(डेटा की टिप्पणी)। ‘कृष्णरक्त’ काला-लाल या काला और लाल, दोनों तरह पढ़ा जा सकता है; अरुस् का आधुनिक नाम नहीं दिया गया। "
           "छपा ‘अंधमिवच’ = अन्धम् इव च (छपाई में जुड़े)। सन्धि जाँची: यस्याम् → यस्यां, छिन्नायाम् → छिन्नायां (व्यंजन से पहले ं); "
           "ताम्यति + अन्धम् → ताम्यत्यन्धम् (इ + भिन्न स्वर → य्); च + अधिष्ठाय → चाधिष्ठाय और अधिष्ठाय + अरूंषि → अधिष्ठायारूंषि "
           "(अ + अ → आ); दुः + चिकित्स्य → दुश्चिकित्स्य (च से पहले विसर्ग → श्)।"),
    "40": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। ‘अन्ये’ (दूसरे लोग) के नाम नहीं दिए गए। ‘त्वचः’ यहाँ वदंति का कर्म है (डेटा: "
           "द्वितीया बहुवचन)। सन्धि जाँची: त्वचः + वदंति → त्वचो वदंति (अः + घोष व्यंजन → ओ)।"),
    "41": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। छाया = छाया, प्रतिबिम्ब (कान्ति भी सम्भव); पाँचों छायाएँ गिनाई नहीं गईं। व्रीहि = धान "
           "(Oryza sativa, मानक), यहाँ माप की इकाई। छपाई: ‘तत्रप्रथमा’ और ‘पंचानांछायानां’ में केवल रिक्त स्थान छूटा है। सन्धि जाँची: "
           "वर्णानाम् + अवभासिनी → वर्णानामवभासिनी (स्वर से पहले म्); ख + आदि → खादि (अ + आ → आ); व्रीहेः + अष्टादश → व्रीहेरष्टादश "
           "(एः + स्वर → एर्)।"),
    "42": ("गद्य; विश्वास उच्च; दो छपी पंक्तियाँ (०२.०५.४३, ०२.०५.४४); कोई पाठ-चिह्न नहीं। दोनों में ‘व्रीहि का’ इकाई ४१ से समझा "
           "जाता है, छपा नहीं, और अनुवाद में भी जोड़ा नहीं गया। क्रिया (है) समझी जाती है। द्वितीया, तृतीया स्त्रीलिंग, त्वच् से मेल। "
           "कोई सन्धि-परिवर्तन नहीं।"),
    "43": ("गद्य; विश्वास उच्च; दो छपी पंक्तियाँ (०२.०५.४५, ०२.०५.४६); कोई पाठ-चिह्न नहीं। पहली पंक्ति बिना रिक्त स्थान के छपी: "
           "चतुर्थी ताम्रा नाम अष्टभागप्रमाणा। ‘व्रीहि का’ इकाई ४१ से समझा जाता है। सन्धि जाँची: नाम + अष्टभाग → नामाष्टभाग "
           "(अ + अ → आ); छपा पंच = पञ्च।"),
    "44": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। ‘षष्ठीरोहिणी’ = षष्ठी रोहिणी, केवल रिक्त स्थान छूटा। व्रीहि = धान (Oryza sativa, "
           "मानक), यहाँ पूरे दाने का माप। कोई सन्धि-परिवर्तन नहीं।"),
    "45": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। यही नाम मांसधरा इकाई ४८ में पहली कला का भी है (डेटा की टिप्पणी)। "
           "व्रीहिद्वय = दो व्रीहि। कोई सन्धि-परिवर्तन नहीं; छपा मांस का ं अनुस्वार है।"),
    "46": ("गद्य; विश्वास मध्यम। पाठ-चिह्न (सम्भावित): छपा ‘ध्वात्वाशयांतरेषु’, ‘धात्वाशयांतरेषु’ (ध → ध्व छपाई-भूल) सुझाया गया; "
           "इस पर कोई प्रश्न नहीं। ‘विपक्कः’ = विपक्वः (क्क = क्व, वर्तनी)। ‘काष्ठइव’ = काष्ठ + इव बिना सन्धि; काष्ठ की विभक्ति अनिश्चित "
           "(‘काष्ठे’ अपेक्षित)। स्नायु = स्नायुबन्ध (सम्भावित), जरायु = झिल्ली (सम्भावित); श्लेष्मा = कफ, या श्लेष्मिक परत भी। "
           "सन्धि जाँची: यः + तु → यस्तु (त से पहले विसर्ग → स्); क्लेदः + अवतिष्ठते → क्लेदोऽवतिष्ठते (अः + अ → ओऽ); "
           "ऊष्माभिः + विपक्वः → ऊष्माभिर्विपक्वः (इः + घोष → इर्); जरायु + छन्नः → जरायुच्छन्नः (ह्रस्व स्वर के बाद छ → च्छ); "
           "सारः + धातु- → सारो धातु- (अः + घोष व्यंजन → ओ); रसशेषः + अल्पत्वात् → रसशेषोऽल्पत्वात्।"),
    "47": ("गद्य; विश्वास उच्च। पाठ-चिह्न (सम्भावित): छपा ‘ध्वात्वाशयांतरमर्यादाः’, इकाई ४६ की तरह ‘धात्वाशय-’ सुझाया गया; इस पर "
           "कोई प्रश्न नहीं। ‘मर्यादाः’ ताः का विधेय (सीमाएँ) पढ़ा गया। सन्धि जाँची: ताः + ध्वा... → ता ध्वा... (आः + घोष → आ)।"),
    "48": ("गद्य; विश्वास मध्यम। पाठ-चिह्न (सम्भावित, वर्तनी): ‘स्रोतासां’ → स्रोतसां; ‘बिसमृणालांनां’ → बिसमृणालानां; ‘प्रताना’ → "
           "प्रतानाः (बहुवचन क्रिया भवंति के कारण)। सिरा = शिरा, धमनी = रक्तवाहिनी (दोनों सम्भावित); कमल = Nelumbo nucifera (मानक)। "
           "सन्धि जाँची: तासाम् → तासां; ‘प्रथमामांसधरा’ = प्रथमा मांसधरा (रिक्त स्थान छूटा); भूमौ + इव → भूमाविव (औ + स्वर → आव्; "
           "छपा ब, ब/व का अदल-बदल); पङ्क + उदके → पङ्कोदके (अ + उ → ओ)।"),
    "49": ("गद्य; विश्वास मध्यम। पाठ-चिह्न (सम्भावित): छपा ‘मांशाच्च’ → मांसाच्च (श के स्थान पर स); ‘मांस से’ इसी पर टिका है, इस पर "
           "कोई प्रश्न नहीं। सिरा (सम्भावित), प्लीहा और यकृत (मानक)। क्षीरी वृक्ष = दूधिया रस वाला पेड़, नाम नहीं दिया। सन्धि जाँची: "
           "मांसस्य + अभ्यन्तरतः → मांसस्याभ्यन्तरतः (अ + अ → आ); अभ्यन्तरतः + तस्याम् → अभ्यन्तरतस्तस्याम् (त से पहले विसर्ग → स्); "
           "विशेषतः + च → विशेषतश्च (च से पहले → श्); मांसात् + च → मांसाच्च (त् + च → च्च); वृक्षात् + इव → वृक्षादिव (त् + स्वर → द्); "
           "छपा प्रवर्त्तते = प्रवर्तते।"),
    "50": ("गद्य; विश्वास निम्न। पाठ-चिह्न (सम्भावित): ‘मस्तिष्कख्यं’ → मस्तिष्काख्यं (दीर्घ आ लुप्त); ‘लुंगारख्यं’ → लुङ्गाख्यं (अधिक र्); "
           "‘मस्तु लुंगाख्यं’ को मस्तुलुङ्ग पढ़ना अनुमान है, क्योंकि छपाई में रिक्त स्थान है और ‘मस्तु’ का साधारण अर्थ दही का पानी भी है; इस पर "
           "कोई प्रश्न नहीं। अन्तिम खण्ड में क्रिया नहीं छपी। सन्धि जाँची: मेदस् + धरा → मेदोधरा (घोष व्यंजन से पहले); मेदः + हि → मेदो हि (अः + घोष व्यंजन → ओ); "
           "उदरे + अणु → उदरेऽणु (ए + अ → एऽ); अणु + अस्थिषु → अण्वस्थिषु (उ + भिन्न स्वर → व्); तत् + एव → तदेव; ‘चशिरसि’ = च शिरसि; "
           "स्थूल + अस्थिषु → स्थूलास्थिषु।"),
    "51": ("गद्य; विश्वास निम्न। पाठ-चिह्न (सम्भावित): ‘तस्तस्थेन’ → तत्स्थेन (उसमें स्थित); अन्तिम शब्द ‘सोपांगावाक्षाः’ अस्पष्ट, अनुमान "
           "‘सोपाङ्गावयवाः’ (उपांग-अवयवों सहित); दोनों पर कोई प्रश्न नहीं। ‘श्लेष्मणाऽऽश्लेषिताः’ का दोहरा अवग्रह छपाई की आदत है। सन्धि "
           "जाँची: श्लेष्मणा + आश्लेषिताः (आ + आ → आ); सर्वसन्धयः + दृढाः → सर्वसन्धयो दृढाः (अः + घोष व्यंजन → ओ); दृढाः + भवन्ति → "
           "दृढा भवन्ति (आः + घोष → आ)।"),
}


# ===================================================================== AIDS
AIDS = {
    "39": {
        "diagram": {"groups": [
            {"label": "कटने पर (यस्यां छिन्नायाम्)", "items": ["ताम्यति (मूर्छित-सा होता है)", "मानो अन्धे अन्धकार में प्रवेश"]},
            {"label": "इसके आश्रय पर (यां चाधिष्ठाय)", "items": ["अरुस् (घाव) उत्पन्न", "पर्वसु (जोड़ों में)", "कृष्णरक्त (काले-लाल)",
                                                          "स्थूलमूल (मोटी जड़ वाले)", "दुश्चिकित्स्यतम"]}]},
        "chunks": "यस्यां छिन्नायां | ताम्यत्यंधमिवच तमः प्रविशति | यां चाधिष्ठायारूंषि जायंते | पर्वसु | कृष्णरक्तानि स्थूलमूलानि "
                  "दुश्चिकित्स्यतमानि",
        "sandhi": "इ + भिन्न स्वर → य्: ताम्यति + अन्धम् → ताम्यत्यन्धम् · अ + अ → आ: च + अधिष्ठाय → चाधिष्ठाय।",
        "frame": "किसकी: छठी त्वचा प्राणधरा (इकाई ३८) → (१) कटने पर: मूर्छा, अन्धकार → (२) इसके आश्रय पर: जोड़ों में कठिन अरुस्।",
    },
    "40": {
        "chunks": "अन्ये तु | सप्त त्वचो | वदंति",
        "sandhi": "अः + घोष व्यंजन → ओ: त्वचः + वदंति → त्वचो वदंति।",
        "contrast": "इकाई ३१-३९: छह त्वचाएँ ↔ इकाई ४०: ‘अन्ये तु’, दूसरों के मत में सात।",
    },
    "41": {
        "diagram": {"groups": [
            {"label": "पहली त्वचा: भासिनी", "items": ["वर्णों को प्रकट करती", "ख (आकाश) आदि पाँच छायाओं को प्रकट करती",
                                                   "माप: व्रीहि का अठारहवाँ भाग"]}]},
        "chunks": "तत्रप्रथमा भासिनी नाम | या वर्णानामवभासिनी | खादीनां च पंचानांछायानां | सा व्रीहेरष्टादशभागप्रमाणा",
        "sandhi": "एः + स्वर → एर्: व्रीहेः + अष्टादश → व्रीहेरष्टादश · अ + आ → आ: ख + आदि → खादि।",
        "anchors": "भासिनी और अवभासिनी एक ही धातु भास् (चमकना) से: जो चमकाए, वही रंग दिखाए। (मेरी याद-पद्धति)",
    },
    "42": {
        "diagram": {"groups": [
            {"label": "दूसरी: लोहिनी", "items": ["माप: सोलहवाँ भाग (षोडश)"]},
            {"label": "तीसरी: श्वेता", "items": ["माप: बारहवाँ भाग (द्वादश)"]}]},
        "chunks": "द्वितीया लोहिनी नाम | षोडशभागप्रमाणा || तृतीया श्वेता नाम | द्वादशभागप्रमाणा",
        "frame": "क्रम (द्वितीया/तृतीया) → नाम (लोहिनी/श्वेता) + नाम → माप (षोडश-/द्वादश-भागप्रमाणा); ‘व्रीहि का’ इकाई ४१ से।",
        "letters": "अंकों के पहले अक्षर: लो-षो (लोहिनी षोडश), श्वे-द्वा (श्वेता द्वादश)। (मेरी याद-पद्धति)",
    },
    "43": {
        "diagram": {"groups": [
            {"label": "चौथी: ताम्रा", "items": ["माप: आठवाँ भाग (अष्ट)"]},
            {"label": "पाँचवीं: वेदिनी", "items": ["माप: पाँचवाँ भाग (पञ्च)"]}]},
        "chunks": "चतुर्थी ताम्रा नाम | अष्टभागप्रमाणा || पंचमी वेदिनी नाम | पंचभागप्रमाणा",
        "sandhi": "अ + अ → आ: नाम + अष्टभाग → नामाष्टभाग।",
        "pegs": "पाँचवीं वेदिनी का माप पाँचवाँ भाग: क्रम और माप एक ही अंक। (मेरी याद-पद्धति)",
    },
    "44": {
        "chunks": "षष्ठी रोहिणी नाम | व्रीहिप्रमाणा",
        "frame": "क्रम: षष्ठी → नाम: रोहिणी → माप: पूरा एक व्रीहि (भाग नहीं)।",
        "anchors": "अब तक भाग (१/१८ … १/५); रोहिणी पर पहली बार पूरा दाना। (मेरी याद-पद्धति)",
    },
    "45": {
        "chunks": "सप्तमी मांसधरा नाम | व्रीहिद्वयप्रमाणा",
        "frame": "क्रम: सप्तमी → नाम: मांसधरा (मांस धारण करने वाली) → माप: व्रीहिद्वय (दो दाने)।",
        "letters": "सातों त्वचाओं के पहले अक्षर क्रम से: भा-लो-श्वे-ता-वे-रो-मां (भासिनी, लोहिनी, श्वेता, ताम्रा, वेदिनी, रोहिणी, "
                   "मांसधरा)। (मेरी याद-पद्धति)",
        "anchors": "ध्यान: मांसधरा नाम इकाई ४८ में पहली कला का भी है; यहाँ यह सातवीं त्वचा है।",
    },
    "46": {
        "chain": {"steps": ["क्लेद (नमी) आशयों के बीच ठहरती है", "अपनी-अपनी ऊष्माओं से पकती है",
                            "स्नायु, श्लेष्मा, जरायु से ढकी", "लकड़ी के सार जैसी: धातुओं का सार",
                            "अल्पता से रस शेष", "नाम: कला"]},
        "chunks": "यस्तु ध्वात्वाशयांतरेषु क्लेदोऽवतिष्ठते | यथास्वमूष्माभिर्विपक्कः | स्नायुश्लेष्मजरायुच्छन्नः | काष्ठइव सारो | "
                  "धातुसारः | रसशेषोऽल्पत्वात्कलासंज्ञः",
        "sandhi": "अः + अ → ओऽ: रसशेषः + अल्पत्वात् → रसशेषोऽल्पत्वात् · ह्रस्व स्वर के बाद छ → च्छ: जरायु + छन्नः → जरायुच्छन्नः।",
        "story": "मेरा बनाया चित्र: जैसे पेड़ के तने के भीतर कठोर सार-लकड़ी होती है, वैसे ही धातुओं के बीच पकी, ढकी नमी उनका सार है, "
                 "जिसे कला कहते हैं। (केवल याद की सहायता)",
    },
    "47": {
        "chunks": "ता | ध्वात्वाशयांतरमर्यादाः | सप्त कलाः",
        "sandhi": "आः + घोष → आ: ताः + ध्वा... → ता ध्वा...।",
        "frame": "कर्ता: ताः (वे) → विधेय: आशयान्तर-मर्यादाः (बीच के स्थानों की सीमाएँ) → संख्या और नाम: सप्त कलाः।",
    },
    "48": {
        "diagram": {"groups": [
            {"label": "शरीर में: मांस में", "items": ["सिरा", "स्नायु", "धमनी", "स्रोतस्", "इनके फैले जाल (प्रतान)"]},
            {"label": "उपमा में: भूमि पर कीचड़ वाले पानी में", "items": ["बिस (कमल के रेशे)", "मृणाल (कमलनाल)", "इनके फैले जाल"]}]},
        "chunks": "तासां प्रथमामांसधरा नाम | यस्यां मांसे | सिरास्नायुधमनीस्रोतासां | भूमाबिव पंकोदके | बिसमृणालांनां | प्रताना भवंति",
        "sandhi": "अ + उ → ओ: पङ्क + उदके → पङ्कोदके · औ + स्वर → आव्: भूमौ + इव → भूमाविव (छपा भूमाबिव)।",
        "letters": "चारों के पहले अक्षर क्रम से: सि-स्ना-ध-स्रो (सिरा, स्नायु, धमनी, स्रोतस्)। (मेरी याद-पद्धति)",
    },
    "49": {
        "diagram": {"groups": [
            {"label": "रक्तधरा: मांस के भीतर", "items": ["उसमें शोणित (रक्त)", "विशेषतः सिरा (सम्भवतः शिरा)", "प्लीहा (तिल्ली, मानक)",
                                                     "यकृत (जिगर, मानक)"]},
            {"label": "उपमा", "items": ["क्षत (घाव) से क्षतज (रक्त) बहता है", "जैसे दूधिया वृक्ष से दूध"]}]},
        "chunks": "द्वितीया रक्तधरा नाम | मांसस्याभ्यंतरतः | तस्यां शोणितं | विशेषतश्च सिराप्लीहयकृत्सु भवति | मांशाच्च क्षतात्क्षतजं | "
                  "वृक्षादिव क्षीरिणः क्षीरं प्रवर्त्तते",
        "sandhi": "त् + स्वर → द्: वृक्षात् + इव → वृक्षादिव · च से पहले विसर्ग → श्: विशेषतः + च → विशेषतश्च।",
        "letters": "विशेष स्थान क्रम से: सि-प्ली-य (सिरा, प्लीहा, यकृत्)। (मेरी याद-पद्धति)",
    },
    "50": {
        "diagram": {"groups": [
            {"label": "मेद (चर्बी) कहाँ और किस नाम से", "items": ["मेदोधरा में, उदर में, छोटी अस्थियों में: मेद, रक्त के साथ",
                                                             "सिर में, कपाल से ढका: मस्तिष्क",
                                                             "(अनुमानित पाठ पर: मस्तुलुंग भी)",
                                                             "बड़ी अस्थियों में: मज्जा"]}]},
        "chunks": "तृतीया मेदोधरा नाम | मेदो हि तस्यामुदरेऽण्वस्थिषु च सरक्तं भवति | तदेव चशिरसि कपालप्रतिच्छन्नं मस्तिष्कख्यं | "
                  "मस्तु लुंगारख्यं च | स्थूलास्थिषु तु मज्जा",
        "sandhi": "-अस् + घोष व्यंजन → ओ: मेदस् + धरा → मेदोधरा · उ + भिन्न स्वर → व्: अणु + अस्थिषु → अण्वस्थिषु।",
        "contrast": "एक ही मेद, तीन स्थान: उदर/छोटी अस्थि में मेद ↔ सिर में मस्तिष्क ↔ बड़ी अस्थि में मज्जा।",
    },
    "51": {
        "chunks": "चतुर्थी श्लेष्मधरा नाम | तस्तस्थेन हि श्लेष्मणाऽऽश्लेषिताः | सर्वसंधयो दृढा भवंति | सोपांगावाक्षाः (अस्पष्ट)",
        "sandhi": "आ + आ → आ: श्लेष्मणा + आश्लेषिताः · अः + घोष व्यंजन → ओ: सर्वसन्धयः + दृढाः → सर्वसन्धयो दृढाः।",
        "chain": {"steps": ["श्लेष्मधरा कला", "श्लेष्मा (कफ) से जुड़ीं", "सब सन्धियाँ दृढ़ होती हैं"]},
    },
}


# ===================================================================== IMAGE_SPECS
IMAGE_SPECS = {
    ("39", "diagram"): {
        "file": "sh5-pranadhara-39.svg",
        "alt": ("Two columns of unit 39 about the sixth skin. When cut: one faints; as it were enters blinding darkness. "
                "Resting on it: sores (arus) arise at the joints, black-red, thick-rooted, most difficult to treat."),
        "type": "split",
        "title": "इकाई ३९: छठी त्वचा (प्राणधरा)",
        "cols": [["कटने पर", ["मूर्छित-सा होना", "मानो अन्धे अन्धकार में प्रवेश"]],
                 ["इसके आश्रय पर अरुस् (घाव)", ["जोड़ों में", "काले-लाल", "मोटी जड़ वाले", "अत्यन्त कठिन चिकित्सा"]]],
    },
    ("41", "diagram"): {
        "file": "sh5-bhasini-41.svg",
        "alt": ("Table of unit 41: the first of seven skins is Bhāsinī; it makes manifest the colours and the five chāyās "
                "beginning with space (kha); its measure is an eighteenth part of a vrīhi (rice grain, standard)."),
        "type": "table",
        "title": "इकाई ४१: पहली त्वचा भासिनी",
        "heads": ["छपा अंश", "अर्थ"],
        "rows": [["तत्रप्रथमा भासिनी नाम", "उनमें पहली, भासिनी नाम की"], ["वर्णानामवभासिनी", "वर्णों को प्रकट करने वाली"],
                 ["खादीनां च पंचानांछायानां", "और ख (आकाश) आदि पाँच छायाओं को"],
                 ["व्रीहेरष्टादशभागप्रमाणा", "माप: व्रीहि (धान, मानक) का अठारहवाँ भाग"]],
    },
    ("42", "diagram"): {
        "file": "sh5-lohini-shveta-42.svg",
        "alt": ("Table of unit 42: second skin Lohinī, a sixteenth part; third skin Śvetā, a twelfth part (of a vrīhi, "
                "understood from unit 41)."),
        "type": "table",
        "title": "इकाई ४२: दूसरी और तीसरी त्वचा",
        "heads": ["क्रम और नाम", "माप (व्रीहि का, इकाई ४१ से)"],
        "rows": [["दूसरी: लोहिनी", "सोलहवाँ भाग"], ["तीसरी: श्वेता", "बारहवाँ भाग"]],
    },
    ("43", "diagram"): {
        "file": "sh5-tamra-vedini-43.svg",
        "alt": ("Table of unit 43: fourth skin Tāmrā, an eighth part; fifth skin Vedinī, a fifth part (of a vrīhi, "
                "understood from unit 41)."),
        "type": "table",
        "title": "इकाई ४३: चौथी और पाँचवीं त्वचा",
        "heads": ["क्रम और नाम", "माप (व्रीहि का, इकाई ४१ से)"],
        "rows": [["चौथी: ताम्रा", "आठवाँ भाग"], ["पाँचवीं: वेदिनी", "पाँचवाँ भाग"]],
    },
    ("46", "chain"): {
        "file": "sh5-kala-46.svg",
        "alt": ("Chain of unit 46, six points in line order: moisture (kleda) stays between the seats; cooked by the respective heats; covered by "
                "snāyu, śleṣman and jarāyu; like heartwood, the essence of the dhātus; rasa remains from smallness; "
                "named kalā."),
        "type": "chain",
        "title": "इकाई ४६: कला क्या है (पंक्ति के क्रम में)",
        "steps": ["क्लेद (नमी) आशयों के बीच ठहरती है", "अपनी-अपनी ऊष्माओं से पकती है", "स्नायु, श्लेष्मा, जरायु से ढकी",
                  "लकड़ी के सार जैसी: धातुओं का सार", "अल्पता से रस शेष", "नाम: कला"],
    },
    ("48", "diagram"): {
        "file": "sh5-mamsadhara-kala-48.svg",
        "alt": ("Two columns of unit 48. In the body, in the flesh of the first kalā Māṃsadharā: networks of sirā, snāyu, "
                "dhamanī and srotas. In the simile, in muddy water on the ground: networks of lotus-fibres (bisa) and "
                "lotus-stalks (mṛṇāla)."),
        "type": "split",
        "title": "इकाई ४८: मांसधरा कला की उपमा",
        "cols": [["शरीर में: मांस में", ["सिरा", "स्नायु", "धमनी", "स्रोतस्", "इनके फैले जाल"]],
                 ["उपमा: कीचड़ वाले पानी में", ["बिस (कमल के रेशे)", "मृणाल (कमलनाल)", "इनके फैले जाल"]]],
    },
    ("49", "diagram"): {
        "file": "sh5-raktadhara-49.svg",
        "alt": ("Two columns of unit 49. Raktadharā, inside the flesh: blood is in it, especially in the sirā (probably "
                "veins), spleen and liver (standard). Simile: from a cut the blood flows, as milk from a milky tree."),
        "type": "split",
        "title": "इकाई ४९: रक्तधरा कला",
        "cols": [["रक्तधरा: मांस के भीतर", ["उसमें शोणित (रक्त)", "विशेषतः सिरा (सम्भवतः शिरा)", "प्लीहा (तिल्ली, मानक)", "यकृत (जिगर, मानक)"]],
                 ["उपमा", ["घाव से रक्त बहता है", "जैसे दूधिया वृक्ष से दूध"]]],
    },
    ("50", "diagram"): {
        "file": "sh5-medodhara-50.svg",
        "alt": ("Table of unit 50: in Medodharā, the belly and the small bones, fat with blood; in the head under the skull "
                "it is called mastiṣka (and, on a conjectural reading, mastuluṅga); in the large bones, majjā (marrow)."),
        "type": "table",
        "title": "इकाई ५०: एक मेद, तीन स्थान",
        "heads": ["कहाँ", "क्या कहलाता है"],
        "rows": [["मेदोधरा, उदर, छोटी अस्थियाँ", "मेद (रक्त के साथ)"],
                 ["सिर में, कपाल से ढका", "मस्तिष्क (अनुमानित पाठ पर मस्तुलुंग भी)"],
                 ["बड़ी अस्थियाँ", "मज्जा"]],
    },
}
