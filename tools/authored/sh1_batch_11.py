from helpers import mcq, match, order, fill, multi, accepts


def T(q, teaches):
    q["teaches"] = teaches
    return q


AUTHORED = {}

# ---------------------------------------------------------------- unit 134
AUTHORED["134"] = {
    "title": "शुक्रे शुक्रे घृतमण्डाभे",
    "question": "By unit 134, which colour of the foetus goes with each appearance of the śukra?",
    "rule": ("Śukra resembling ghee-maṇḍa goes with fairness (गौरत्व) of the foetus, resembling oil with darkness "
             "(कृष्णत्व), resembling honey with dusky colour (श्यामत्व). The line has no verb."),
    "limits": ("Prose, no verb. Whose śukra is meant is not stated (unit 145 uses śukra of women too), so the card says "
               "reproductive fluid. The वा after the first item is not explained and is left undecided. घृतमण्ड is kept "
               "as ghee-maṇḍa; its exact sense is not asserted."),
    "explain_hi": ("यह गद्य-पंक्ति बताती है कि शुक्र यानी प्रजनन द्रव की आभा से गर्भ का वर्ण कैसे जुड़ा है। "
                   "घृतमण्ड जैसा होने पर गर्भ में गौरता, तेल जैसा होने पर कालापन, और शहद जैसा होने पर साँवलापन। "
                   "‘शुक्रे शुक्रे’ की पुनरुक्ति को ‘प्रत्येक शुक्र में’ पढ़ा गया है; पंक्ति में कोई क्रिया नहीं है। "
                   "‘घृतमण्डाभे’ के बाद आया ‘वा’ स्पष्ट नहीं है, इसलिए उस पर कुछ तय नहीं किया गया। "
                   "किसका शुक्र है, यह नहीं कहा गया।"),
    "hook": "घी-सा → गौर, तेल-सा → काला, शहद-सा → श्याम।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 134, which colour of the foetus goes with śukra that resembles oil?",
            ("Darkness (कृष्णत्व)", "तैलाभे कृष्णत्वम्: resembling oil, darkness."),
            [("Fairness (गौरत्व)", "Fairness goes with śukra resembling ghee-maṇḍa."),
             ("Dusky colour (श्यामत्व)", "Dusky colour goes with śukra resembling honey."),
             ("Reddish colour (रक्तता)", "No reddish colour is named in unit 134.")],
            "The line pairs oil-like śukra with darkness of the foetus.",
            "तैलाभे → कृष्णत्वम्."),
        order(1, "Put these words of unit 134 in the line's order.",
              ["घृतमण्डाभे", "गौरत्वम्", "तैलाभे", "कृष्णत्वम्", "मध्वाभे", "श्यामत्वम्"],
              "Each appearance is followed by its colour: ghee-maṇḍa, fair; oil, dark; honey, dusky.",
              "घृतमण्ड → गौर, तैल → कृष्ण, मधु → श्याम."),
        match(2, "Match each appearance of the śukra in unit 134 to the foetus's colour.",
              [["घृतमण्डाभ (like ghee-maṇḍa)", "fairness"], ["तैलाभ (like oil)", "darkness"],
               ["मध्वाभ (like honey)", "dusky colour"]],
              "The line gives three pairs of appearance and colour.",
              "घृतमण्डाभ-गौर, तैलाभ-कृष्ण, मध्वाभ-श्याम.", role="extend",
              teaches="-आभ at the end of a compound means resembling: तैल + आभ = like oil."),
        mcq("discriminate", 3, "Which split of मध्वाभे is right?",
            ("मधु + आभे", "उ before the vowel आ becomes व्: मधु + आभे → मध्वाभे."),
            [("मधु + अभे", "उ + short अ would give मध्वभे, with a short a."),
             ("मध्वा + भे", "भे is not a word of the card; the member is आभे."),
             ("मधो + आभे", "मधो is not the card's word; ओ + आ would give मधवाभे.")],
            "मधु (honey) + आभे (resembling): उ + आ → वा.",
            "उ + a different vowel → व् + that vowel."),
        multi("apply", 4, "Which statements about unit 134 match the card?",
              [("Śukra like ghee-maṇḍa goes with fairness of the foetus", "Right: घृतमण्डाभे ... गौरत्वम्."),
               ("Śukra like honey goes with dusky colour", "Right: मध्वाभे श्यामत्वम्."),
               ("The line states that it is the father's śukra", "Whose śukra is meant is not stated."),
               ("The line has a finite verb such as भवति", "The line is elliptical: it has no verb.")],
              [0, 1],
              "Two pairs are stated; whose śukra it is, and any verb, are not.",
              "Three pairs, no verb, owner of the śukra unstated."),
        mcq("transfer", 5, "By the rule of मध्वाभे, how is साधु + आचारः (good conduct) written as one compound?",
            ("साध्वाचारः", "उ + आ → वा, as in मधु + आभे → मध्वाभे."),
            [("साधूचारः", "उ + आ does not give ऊ."),
             ("साधवाचारः", "That would need a base साधो; उ itself becomes व्."),
             ("साधुआचारः", "Inside a compound the two vowels must join.")],
            "साधु + आचारः = साध्वाचारः, like मधु + आभे = मध्वाभे.",
            "उ + a different vowel → व् + that vowel.",
            teaches="A final उ before a different vowel becomes व्: मधु + आभे → मध्वाभे."),
    ],
}

# ---------------------------------------------------------------- unit 135
AUTHORED["135"] = {
    "title": "क्षीरादिमधुराणामुपयोगात्",
    "question": "By unit 135, what in the mother's life goes with fairness of the child, and what with dusky colour?",
    "rule": ("Likewise: from the mother's use of sweet things beginning with milk, and from her sport in water, fairness; "
             "from (the use of) mixed ones, dusky colour. The cause of darkness rests on a conjectural reading."),
    "limits": ("Low confidence. The middle clause (तिलांन्नविदाहिनो: sesame-food and burning-causing ones, darkness) is a "
               "conjectural reading of a damaged ending, and तिलान्न may be one item or two; no question uses it. "
               "उपयोगात् (use) is understood, not repeated, in the second and third clauses."),
    "explain_hi": ("यह इकाई पिछली इकाई की तरह (‘तथा’) वर्ण के कारण बताती है, पर अब माता के आचरण से। "
                   "माता द्वारा दूध आदि मधुर पदार्थों के सेवन से और जल में विहार से गौरता होती है। "
                   "मिले-जुलों (व्यामिश्र) के सेवन से साँवलापन; ‘उपयोगात्’ यहाँ दोहराया नहीं गया, समझा जाता है। "
                   "बीच का खण्ड (तिल-अन्न और विदाही से कालापन) क्षतिग्रस्त अन्त पर अनुमानित पाठ है, इसलिए उस पर प्रश्न नहीं। "
                   "‘उदकविहाराच्च’ में उदकविहारात् + च है (त् + च → च्च)।"),
    "hook": "माता: दूध-मधुर और जल-विहार → गौर; मिला-जुला → श्याम।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 135, besides the use of milk and sweet things, what of the mother goes with fairness?",
            ("Her sport in water", "मातुः उदकविहारात् च गौरता."),
            [("Her sleep by day", "Sleep is not named in unit 135."),
             ("Her fasting", "Fasting is not named in unit 135."),
             ("Her walks in the sun", "No walk in the sun is named.")],
            "Fairness comes from the use of milk and sweets, and from the mother's sport in water.",
            "क्षीरादिमधुर-उपयोग + उदकविहार → गौरता."),
        order(1, "Put these words of unit 135 in the line's order.",
              ["तथा", "क्षीरादिमधुराणाम्", "उपयोगात्", "मातुः", "उदकविहारात्", "गौरता"],
              "Likewise, of milk-and-sweets, from the use, of the mother, from sport in water, fairness.",
              "तथा → क्षीरादिमधुराणाम् → उपयोगात् → मातुः → उदकविहारात् → गौरता."),
        match(2, "Match each word of unit 135 to its meaning.",
              [["क्षीर", "milk"], ["मधुर", "sweet"], ["उपयोग", "use"], ["उदकविहार", "sport in water"],
               ["व्यामिश्र", "mixed"]],
              "These words carry the sure first and last clauses.",
              "क्षीर, मधुर, उपयोग, उदकविहार, व्यामिश्र.", role="extend",
              teaches="X-आदि = X and the like: क्षीरादिमधुर = sweet things beginning with milk."),
        mcq("discriminate", 3, "Which split of उदकविहाराच्च is right?",
            ("उदकविहारात् + च", "त् before च becomes च्: उदकविहारात् + च → उदकविहाराच्च."),
            [("उदकविहारः + च", "A visarga before च would give उदकविहारश्च."),
             ("उदकविहारम् + च", "A final म् would give उदकविहारं च."),
             ("उदकविहारा + च्च", "च्च is not a word; the particle is च.")],
            "उदकविहारात् (from sport in water) + च (and): त् + च → च्च.",
            "Final त् + च → च्च."),
        mcq("apply", 4, "By unit 135, what goes with the use of mixed (व्यामिश्र) ones?",
            ("Dusky colour (श्यामता)", "व्यामिश्राणां श्यामता."),
            [("Fairness (गौरता)", "Fairness goes with milk, sweets and sport in water."),
             ("Darkness (कृष्णता)", "Darkness belongs to the middle clause, not to the mixed ones."),
             ("No change of colour", "The line names a colour for the mixed ones.")],
            "The last clause pairs the mixed ones with dusky colour.",
            "व्यामिश्र → श्यामता."),
        mcq("transfer", 5, "By the rule of मातुरुदक, how is गुरुः + आगच्छति (the teacher comes) written?",
            ("गुरुरागच्छति", "After उ a visarga becomes र् before a vowel, as मातुः + उदक → मातुरुदक."),
            [("गुरु आगच्छति", "The visarga is dropped like this only after अ or आ."),
             ("गुरुवागच्छति", "उ turns into व् only when no visarga follows it."),
             ("गुरुसागच्छति", "The visarga does not become स् before a vowel.")],
            "गुरुः + आगच्छति = गुरुरागच्छति, like मातुः + उदक = मातुरुदक.",
            "Visarga after a vowel other than अ/आ → र् before a vowel or voiced consonant.",
            teaches="A visarga after a vowel other than अ or आ becomes र् before a vowel: मातुः + उदक → मातुरुदक."),
    ],
}

# ---------------------------------------------------------------- unit 136
AUTHORED["136"] = {
    "title": "देशकुलानुवृत्तितश्च वर्णभेदः",
    "question": "By unit 136, what further cause of difference in colour is named?",
    "rule": ("And difference of colour (वर्णभेद) comes by conformity to country and family (देश-कुल-अनुवृत्ति). "
             "-तः on अनुवृत्ति gives the sense by, from."),
    "limits": ("A short line with no verb. It does not say how country or family act. वर्ण here is skin colour, as in the "
               "preceding units, not caste."),
    "explain_hi": ("यह छोटी गद्य-पंक्ति वर्ण-भेद का एक और कारण बताती है: देश और कुल का अनुवर्तन, यानी उनके अनुसार होना। "
                   "‘अनुवृत्तितः’ में ‘-तः’ प्रत्यय ‘से, के कारण’ का अर्थ देता है। "
                   "यहाँ ‘वर्ण’ का अर्थ त्वचा का रंग है, जाति नहीं, क्योंकि पिछली इकाइयाँ गौर, कृष्ण और श्याम की बात कर रही हैं। "
                   "‘अनुवृत्तितश्च’ में अनुवृत्तितः + च है (विसर्ग → श् च से पहले)।"),
    "hook": "देश और कुल के अनुसार भी रंग का भेद।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 136, conformity to what brings a difference of colour?",
            ("Country and family", "देशकुलानुवृत्तितः: by conformity to country and family."),
            [("Season and time of day", "No season or time is named in unit 136."),
             ("Food and drink of the father", "Food is the cause in unit 135, of the mother."),
             ("Planets and stars", "No planets or stars are named.")],
            "Country (देश) and family (कुल) are the two named.",
            "देश-कुल-अनुवृत्ति → वर्णभेद."),
        order(1, "Put the members of unit 136 in the line's order.",
              ["देश", "कुल", "अनुवृत्तितः", "च", "वर्णभेदः"],
              "Country, family, by conformity, and, difference of colour.",
              "देश → कुल → अनुवृत्तितः → च → वर्णभेदः."),
        T(fill(2, "In unit 136, the word for colour (of the skin) is ____ (type it in Devanagari or in English letters, e.g. dharma).",
               accepts("वर्ण", None, "varna"),
               "वर्णभेदः = वर्ण (colour) + भेद (difference).",
               "वर्ण here = colour of the skin.",
               "वर्ण = colour."),
          "वर्णभेद = difference of colour; here वर्ण means skin colour, not caste."),
        mcq("discriminate", 3, "What does कुल mean in unit 136, by the card?",
            ("Family", "देशकुल: country and family."),
            [("Country", "That is देश."),
             ("Colour", "That is वर्ण."),
             ("Difference", "That is भेद.")],
            "देश = country, कुल = family; conformity to both brings a difference of colour.",
            "कुल = family."),
        mcq("apply", 4, "Which split of अनुवृत्तितश्च is right?",
            ("अनुवृत्तितः + च", "A visarga before च becomes श्: अनुवृत्तितः + च → अनुवृत्तितश्च."),
            [("अनुवृत्तितम् + च", "A final म् would give अनुवृत्तितं च."),
             ("अनुवृत्तित + श्च", "श्च is not a word; the particle is च."),
             ("अनुवृत्तितत् + च", "A final त् would give अनुवृत्तितच्च.")],
            "अनुवृत्तितः (by conformity) + च (and).",
            "Visarga + च → श्च."),
        mcq("transfer", 5, "By the rule of अनुवृत्तितश्च, how is रामः + च (and Rāma) written?",
            ("रामश्च", "Visarga before च → श्, as in अनुवृत्तितः + च."),
            [("रामो च", "अः → ओ happens before a voiced sound; च is not voiced."),
             ("रामच्च", "That is the rule for a final त्, not a visarga."),
             ("रामर्च", "Visarga does not become र् after अ before च.")],
            "रामः + च = रामश्च, like अनुवृत्तितः + च = अनुवृत्तितश्च.",
            "Visarga + च/छ → श्.",
            teaches="A visarga before च becomes श्: अनुवृत्तितः + च → अनुवृत्तितश्च."),
    ],
}

# ---------------------------------------------------------------- unit 137
AUTHORED["137"] = {
    "title": "तेजोधातोरुदकाकाशधातुसंपर्कात्",
    "question": "By unit 137, which contacts of the elements go with fair, dark and dusky colour?",
    "rule": ("Fairness from contact of the fire element (तेजोधातु) with the water and space elements; darkness from "
             "contact with earth and air; dusky colour when all elements are in balance (सर्वधातुसाम्य)."),
    "limits": ("Here धातु means element, not body tissue. That the second contact is the fire element's is understood "
               "from the first clause, not stated. The line has no verb and does not say how the contact works."),
    "explain_hi": ("यह इकाई वर्ण के कारण महाभूतों (धातु = तत्त्व) की भाषा में बताती है। "
                   "तेजस् धातु का जल और आकाश धातु से संपर्क हो तो गौरता, पृथ्वी और वायु से संपर्क हो तो कालापन, "
                   "और सब धातुएँ सम हों तो साँवलापन। "
                   "दूसरे खण्ड में ‘तेजस् का’ लिखा नहीं, पहले खण्ड से समझा जाता है। "
                   "यहाँ ‘धातु’ शरीर की सात धातुएँ नहीं, बल्कि तत्त्व हैं। "
                   "‘संपर्काद्गौरता’ में संपर्कात् + गौरता है (त् → द् घोष व्यंजन से पहले)।"),
    "hook": "तेज + जल-आकाश → गौर; पृथ्वी-वायु → काला; सब सम → श्याम।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 137, which colour goes with all the elements being in balance?",
            ("Dusky colour (श्यामता)", "सर्वधातुसाम्ये श्यामता."),
            [("Fairness (गौरता)", "Fairness goes with fire meeting water and space."),
             ("Darkness (कृष्णता)", "Darkness goes with contact with earth and air."),
             ("Reddish colour (रक्तता)", "No reddish colour is named in unit 137.")],
            "Balance of all elements gives dusky colour.",
            "सर्वधातुसाम्य → श्यामता."),
        order(1, "Put these words of unit 137 in the line's order.",
              ["उदकाकाशधातुसंपर्कात्", "गौरता", "भूवायुसंपर्कात्", "कृष्णता", "सर्वधातुसाम्ये", "श्यामता"],
              "Each cause comes before its colour: water-space, fair; earth-air, dark; balance, dusky.",
              "जल-आकाश → गौर, भू-वायु → कृष्ण, सर्वसाम्य → श्याम."),
        match(2, "Match each condition of unit 137 to its colour.",
              [["तेजस् + उदक-आकाश संपर्क", "fairness"], ["भू-वायु संपर्क", "darkness"],
               ["सर्वधातुसाम्य", "dusky colour"]],
              "Three conditions, three colours, in the same order as units 134 and 135.",
              "जल-आकाश-गौर, भू-वायु-कृष्ण, साम्य-श्याम.", role="extend",
              teaches="साम्य = balance, evenness; सर्वधातुसाम्ये = when all elements are in balance (locative)."),
        mcq("discriminate", 3, "What does धातु mean in unit 137, by the card?",
            ("Element (fire, water, space, earth, air)", "The note: the great elements, not body tissue."),
            [("Body tissue (blood, flesh and the rest)", "The note says the bodily tissue is not meant here."),
             ("Verbal root of a word", "The card gives no grammatical sense here."),
             ("Metal or mineral", "The card gives no such sense.")],
            "धातु = element in this unit.",
            "धातु here = element."),
        mcq("apply", 4, "Which split of संपर्काद्गौरता is right?",
            ("संपर्कात् + गौरता", "Final त् before the voiced ग becomes द्."),
            [("संपर्कः + गौरता", "A visarga would give संपर्को गौरता."),
             ("संपर्कम् + गौरता", "A final म् would give संपर्कं गौरता."),
             ("संपर्का + द्गौरता", "द्गौरता is not a word.")],
            "संपर्कात् (from contact) + गौरता (fairness): त् → द्.",
            "Final त् + voiced consonant → द्."),
        mcq("transfer", 5, "By the rule of संपर्काद्गौरता, how is जगत् + गुरुः (teacher of the world) written?",
            ("जगद्गुरुः", "त् before the voiced ग becomes द्."),
            [("जगत्गुरुः", "त् does not stay unvoiced before ग."),
             ("जगच्गुरुः", "त् becomes च् only before च/छ."),
             ("जगोगुरुः", "ओ comes from a visarga, not from त्.")],
            "जगत् + गुरुः = जगद्गुरुः, like संपर्कात् + गौरता.",
            "Final त् + voiced consonant → द्.",
            teaches="A final त् before a voiced consonant becomes द्: संपर्कात् + गौरता → संपर्काद्गौरता."),
    ],
}

# ---------------------------------------------------------------- unit 138
AUTHORED["138"] = {
    "title": "सत्त्वविशेषकराणि",
    "question": "By unit 138, what brings about the special features of the child's sattva (mind)?",
    "rule": ("Sattva-shaping factors: the sattva of mother and father, the repeated hearings of the pregnant woman, "
             "one's own accumulated karma, and past practice (पूर्वाभ्यास)."),
    "limits": ("What is heard is not stated. अन्तर्वत्न्याः (pregnant woman) and अभीक्ष्णम् (repeated) rest on possible "
               "corrections of the print; भवति after कर्म is kept literally. No question uses the owner of the hearings."),
    "explain_hi": ("अब विषय वर्ण से सत्त्व यानी मन पर आता है। सत्त्व में विशेषता लाने वाले कारण गिनाए गए हैं: "
                   "माता-पिता का सत्त्व, गर्भवती के बार-बार के श्रवण, अपना संचित कर्म, और पूर्व अभ्यास। "
                   "क्या सुना जाए, यह नहीं कहा गया। "
                   "छपे ‘अंतैर्वत्न्याः’ को अन्तर्वत्न्याः और ‘अभीक्ष्ण,’ को अभीक्ष्णम् पढ़ना सम्भावित सुधार है। "
                   "‘पूर्वाभ्यासश्चेति’ = पूर्वाभ्यासः + च + इति।"),
    "hook": "मन को गढ़ते हैं: माता-पिता का मन, बार-बार सुनना, अपना कर्म, पुराना अभ्यास।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 138, the listed factors bring about special features of what?",
            ("Sattva, the mind", "सत्त्वविशेषकराणि: bringing about special features of sattva."),
            [("Skin colour", "Colour is the subject of units 134 to 137."),
             ("Height and build of the body", "Body build is not named in unit 138."),
             ("Whether the child is a boy or girl", "Sex is not the subject of unit 138.")],
            "The list concerns the sattva (mind) of the child.",
            "सत्त्व = mind."),
        order(1, "Put the sattva-shaping factors of unit 138 in the line's order.",
              ["मातापितृसत्त्वानि", "श्रुतयः", "स्वोपचितं कर्म", "पूर्वाभ्यासः"],
              "Parents' sattva, hearings, own accumulated karma, past practice.",
              "मातापितृसत्त्व → श्रुति → स्वोपचित कर्म → पूर्वाभ्यास."),
        match(2, "Match each word of unit 138 to its meaning.",
              [["सत्त्व", "mind"], ["श्रुति", "hearing"], ["उपचित", "accumulated"], ["कर्म", "action (karma)"],
               ["अभ्यास", "practice"]],
              "These words name the four factors.",
              "सत्त्व, श्रुति, उपचित, कर्म, अभ्यास.", role="extend",
              teaches="स्व-उपचित = one's own accumulated: स्व + उपचितम् → स्वोपचितम् (अ + उ → ओ)."),
        mcq("discriminate", 3, "Which is NOT among the sattva-shaping factors of unit 138?",
            ("The mother's use of milk and sweets", "That is a cause of colour in unit 135."),
            [("The sattva of mother and father", "Named: मातापितृसत्त्वानि."),
             ("One's own accumulated karma", "Named: स्वोपचितं कर्म."),
             ("Past practice", "Named: पूर्वाभ्यासः.")],
            "Diet belongs to the colour units; unit 138 lists mind-shaping factors.",
            "Four factors: parents' sattva, hearings, own karma, past practice."),
        mcq("apply", 4, "Which split of पूर्वाभ्यासश्चेति is right?",
            ("पूर्वाभ्यासः + च + इति", "Visarga + च → श्च; अ + इ → ए."),
            [("पूर्वाभ्यास + श्च + इति", "श्च is not a word; the particle is च."),
             ("पूर्वाभ्यासः + चे + इति", "चे is not a word of the card."),
             ("पूर्वाभ्यासः + च + एति", "अ + ए would give ऐ: चैति.")],
            "पूर्वाभ्यासः (past practice) + च (and) + इति (thus).",
            "Visarga + च → श्च; अ + इ → ए."),
        mcq("transfer", 5, "By the rule of चेति, how is न + इति (not so) written when joined?",
            ("नेति", "अ + इ → ए, as च + इति → चेति."),
            [("नैति", "ऐ comes from अ + ए, not अ + इ."),
             ("नीति", "अ + इ does not give ई."),
             ("नयिति", "No य् is put in between.")],
            "न + इति = नेति, like च + इति = चेति.",
            "अ + इ → ए.",
            teaches="अ or आ before इ or ई joins into ए: च + इति → चेति."),
    ],
}

# ---------------------------------------------------------------- unit 139
AUTHORED["139"] = {
    "title": "भवन्ति चात्र",
    "question": "What does the short formula of unit 139 announce?",
    "rule": ("भवन्ति च अत्र: and here there are (verses). The formula introduces the verses that follow; the word "
             "verses is not in the Sanskrit."),
    "limits": ("Only two printed words. The noun 'verses' is supplied in brackets; nothing about the content of the "
               "verses is said here."),
    "explain_hi": ("यह छोटा सूत्र आगे आने वाले श्लोकों की भूमिका है: ‘और इस विषय में (श्लोक) हैं।’ "
                   "‘श्लोक’ शब्द संस्कृत में नहीं है, कोष्ठक में जोड़ा गया है। "
                   "‘भवन्ति’ प्रथम पुरुष बहुवचन वर्तमान है (‘हैं’); इकाई 138 का ‘भवति’ एकवचन था। "
                   "‘चात्र’ = च + अत्र (अ + अ → आ)। इसके बाद की इकाइयाँ (140 से 145) छन्दोबद्ध हैं।"),
    "hook": "भवन्ति चात्र = और यहाँ (श्लोक) हैं।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What does unit 139 introduce?",
            ("The verses that follow", "The note: a formula introducing the verses that follow."),
            [("The end of the chapter", "The colophon is unit 146."),
             ("A list of medicines", "No medicine is named."),
             ("A new speaker", "No speaker is named.")],
            "भवन्ति चात्र introduces the verses after it.",
            "भवन्ति चात्र = and here there are (verses)."),
        match(1, "Match each word of unit 139 to its meaning.",
              [["भवन्ति", "there are"], ["च", "and"], ["अत्र", "here, in this matter"]],
              "Three words make the whole formula.",
              "भवन्ति, च, अत्र."),
        T(fill(2, "And here there are (verses): भवन्ति च ____ (type it in Devanagari or in English letters, e.g. dharma).",
               accepts("अत्र"),
               "The line is भवन्ति चात्र, read भवन्ति च अत्र.",
               "अत्र = here, in this matter.",
               "अत्र = here."),
          "अत्र = here; च + अत्र joins as चात्र."),
        mcq("discriminate", 3, "Which split of चात्र is right?",
            ("च + अत्र", "अ + अ → आ: च + अत्र → चात्र."),
            [("चा + त्र", "त्र alone is not a word."),
             ("च + आत्र", "आत्र is not a word of the card."),
             ("चः + अत्र", "The particle is च, without a visarga.")],
            "च (and) + अत्र (here).",
            "अ + अ → आ."),
        mcq("apply", 4, "By the card, what form is भवन्ति?",
            ("Third person plural, present: there are", "Labelled 3 pl. pres. of √भू."),
            [("Third person singular, present: there is", "That is भवति, as in unit 138."),
             ("First person plural, present: we are", "That would be भवामः."),
             ("Third person dual, present: two are", "That would be भवतः.")],
            "भवन्ति = they are, there are: plural, because several verses follow.",
            "-अन्ति = 3 pl. present."),
        mcq("transfer", 5, "By the rule of चात्र, how is न + अत्र (not here) written when joined?",
            ("नात्र", "अ + अ → आ, as in च + अत्र."),
            [("नेत्र", "अ + अ does not give ए."),
             ("नत्र", "One अ is not simply dropped."),
             ("नोत्र", "अ + अ does not give ओ.")],
            "न + अत्र = नात्र, like च + अत्र = चात्र.",
            "अ + अ → आ.",
            teaches="Two short अ sounds at a word joint become one long आ: च + अत्र → चात्र."),
    ],
}

# ---------------------------------------------------------------- unit 140
AUTHORED["140"] = {
    "title": "आर्तवं तिष्ठति चिरम्",
    "question": "By the sure part of unit 140, in whom does the ārtava stay long?",
    "rule": ("In cheerful (मुदिता) women of Kapha nature (कफात्मन्), the ārtava stays long (चिरं तिष्ठति); in the opposite, "
             "otherwise. ārtava = menstrual blood, the female reproductive element (probable)."),
    "limits": ("Low confidence. मत्त्यासु is damaged and not interpreted; घृतक्षीरादि (ghee, milk and the like) is not joined "
               "into a firm sense. 'Women' is shown only by the feminine endings; what the ārtava stays in is not stated. "
               "Questions use line 2 and the two sure words of line 1."),
    "explain_hi": ("यहाँ से श्लोक आरम्भ होते हैं। दूसरी पंक्ति स्पष्ट है: आर्तव देर तक ठहरता है; विपरीत (स्त्रियों) में इससे अन्यथा। "
                   "पहली पंक्ति के ‘मुदितासु’ (प्रसन्न) और ‘कफात्मसु’ (कफ स्वभाव वाली) सप्तमी बहुवचन हैं; ‘मुदितासु’ का स्त्रीलिंग अन्त ‘-आसु’ है, "
                   "इसी से स्त्रियों का अर्थ निकलता है, संज्ञा लिखी नहीं। "
                   "‘मत्त्यासु’ क्षतिग्रस्त है और ‘घृतक्षीरादि’ का पक्का अर्थ नहीं बैठता, इसलिए उन पर प्रश्न नहीं। "
                   "आर्तव किसमें ठहरता है, यह नहीं कहा गया।"),
    "hook": "प्रसन्न, कफ-स्वभाव वाली में आर्तव देर तक; विपरीत में उल्टा।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By line 2 of unit 140, what stays long (चिरम्)?",
            ("The ārtava (आर्तव)", "आर्तवं तिष्ठति चिरम्."),
            [("The foetus (गर्भ)", "The foetus is not named in unit 140."),
             ("The colour of the child", "Colour is not the subject of this line."),
             ("The man's śukra", "Śukra is not named in unit 140.")],
            "Line 2 says the ārtava stays long.",
            "आर्तवं तिष्ठति चिरम्."),
        order(1, "Put the words of line 2 of unit 140 in the verse's order.",
              ["आर्तवम्", "तिष्ठति", "चिरम्", "विपरीतासु", "अतः", "अन्यथा"],
              "The ārtava stays long; in the opposite ones, otherwise than this.",
              "आर्तवम् → तिष्ठति → चिरम् → विपरीतासु → अतः → अन्यथा."),
        match(2, "Match each word of unit 140 to its meaning.",
              [["मुदिता", "cheerful"], ["कफात्मन्", "whose nature is Kapha"], ["तिष्ठति", "stays"],
               ["चिरम्", "for long"], ["विपरीत", "opposite"]],
              "These are the sure words of the unit.",
              "मुदिता, कफात्मन्, तिष्ठति, चिरम्, विपरीत.", role="extend",
              teaches="-आसु is the feminine locative plural: मुदितासु = in cheerful (women)."),
        mcq("discriminate", 3, "Which split of विपरीतास्वतोऽन्यथा is right?",
            ("विपरीतासु + अतः + अन्यथा", "उ + अ → व; अः + अ → ओ with ऽ for the lost अ."),
            [("विपरीतास्वः + अतः + अन्यथा", "विपरीतास्वः is not a word; the form is विपरीतासु."),
             ("विपरीतासु + अतो + न्यथा", "न्यथा is not a word; the अ of अन्यथा is shown by ऽ."),
             ("विपरीतासु + तः + अन्यथा", "तः alone is not a word; the word is अतः.")],
            "विपरीतासु (in the opposite) + अतः (than this) + अन्यथा (otherwise).",
            "उ + अ → व; अः + अ → ओऽ."),
        multi("apply", 4, "Which two sure words does line 1 of unit 140 contain?",
              [("मुदितासु (in cheerful ones)", "Right: printed in line 1 (मुदितासुकफात्मसु)."),
               ("कफात्मसु (in ones whose nature is Kapha)", "Right: printed in line 1."),
               ("वृद्धासु (in elderly ones)", "Age is not named in unit 140."),
               ("गर्भिणीषु (in pregnant ones)", "Pregnancy is not named in unit 140.")],
              [0, 1],
              "Line 1's sure words are मुदितासु and कफात्मसु; मत्त्यासु is damaged.",
              "मुदितासु कफात्मसु."),
        mcq("transfer", 5, "By the rule of विपरीतास्वतः, how is वस्तु + अत्र (the thing here) written when joined?",
            ("वस्त्वत्र", "उ + अ → व, as विपरीतासु + अतः → विपरीतास्वतः."),
            [("वस्तूत्र", "उ + अ does not give ऊ."),
             ("वस्तोत्र", "उ + अ does not give ओ."),
             ("वस्तात्र", "उ is not dropped before अ.")],
            "वस्तु + अत्र = वस्त्वत्र, like विपरीतासु + अतः.",
            "उ + a different vowel → व् + that vowel.",
            teaches="A final उ before a different vowel becomes व्: विपरीतासु + अतः → विपरीतास्वतः."),
    ],
}

# ---------------------------------------------------------------- unit 141
AUTHORED["141"] = {
    "title": "निपातादेव गृह्णाति रागम्",
    "question": "By line 1 of unit 141, what is the taking of colour compared to?",
    "rule": ("From the mere falling (निपात) it takes colour (राग), as a clean cloth (वासो यथामलम्) does. Line 2 is a bare "
             "list: certainly, the foetus (conjectural), likewise seed, field, prepared seed."),
    "limits": ("Low confidence. What takes the colour (the subject of गृह्णाति) is not stated and not decided. Line 2 has no "
               "verb, गर्भः is a conjectural reading of गर्भतथा, and the link between seed and field is not stated; "
               "no question rests on line 2."),
    "explain_hi": ("पहली पंक्ति एक उपमा है: जैसे स्वच्छ वस्त्र, निपात (गिरने) मात्र से ही रंग ग्रहण कर लेता है; क्या गिरता है, यह नहीं बताया गया। "
                   "रंग कौन ग्रहण करता है (गृह्णाति का कर्ता), यह नहीं कहा गया; पिछली इकाई का आर्तव हो सकता है, पर यह तय नहीं। "
                   "दूसरी पंक्ति केवल शब्दों की सूची है: निश्चित, (अनुमानित पाठ पर) गर्भ, बीज, क्षेत्र, तैयार किया हुआ बीज; "
                   "इनका आपसी सम्बन्ध नहीं बताया गया, इसलिए उस पर प्रश्न नहीं। "
                   "‘निपातादेव’ = निपातात् + एव (त् → द् स्वर से पहले)।"),
    "hook": "स्वच्छ कपड़े जैसा: गिरते ही रंग पकड़ ले।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In line 1 of unit 141, to what is the taking of colour compared?",
            ("A clean cloth", "वासो यथाऽमलम्: as a clean cloth (वासः अमलम्)."),
            [("A clear crystal", "No crystal is named."),
             ("Still water in a pot", "No water is named."),
             ("Fresh milk", "No milk is named in unit 141.")],
            "The taking of colour is compared to a clean cloth; what takes it is not stated.",
            "वासः यथा अमलम् = as a clean cloth."),
        order(1, "Put the words of line 1 of unit 141 in the verse's order.",
              ["निपातादेव", "गृह्णाति", "रागम्", "वासः", "यथा", "अमलम्"],
              "From the mere falling it takes colour, a cloth, as, clean.",
              "निपातादेव → गृह्णाति → रागम् → वासः → यथा → अमलम्."),
        match(2, "Match each word of line 1 of unit 141 to its meaning.",
              [["निपात", "falling"], ["गृह्णाति", "takes"], ["राग", "colour"], ["वासः", "cloth"],
               ["अमल", "clean"]],
              "These five words carry the simile.",
              "निपात, गृह्णाति, राग, वासः, अमल.", role="extend",
              teaches="यथा = as: it marks the thing compared, here a clean cloth."),
        mcq("discriminate", 3, "Which split of निपातादेव is right?",
            ("निपातात् + एव", "Final त् before a vowel becomes द्: निपातादेव."),
            [("निपातम् + एव", "A final म् would give निपातमेव."),
             ("निपातः + एव", "A visarga after अ would give निपात एव."),
             ("निपाते + एव", "ए before ए would not give आदे.")],
            "निपातात् (from the falling) + एव (just, even).",
            "Final त् + vowel → द्."),
        mcq("apply", 4, "What does the card leave undecided in line 1 of unit 141?",
            ("What it is that takes the colour", "The subject of गृह्णाति is not stated and not decided."),
            [("Whether the cloth is clean", "अमलम् states that it is clean."),
             ("Which word means colour", "रागम् is glossed colour."),
             ("Whether there is a comparison", "यथा states the comparison.")],
            "Only the subject of गृह्णाति is open; the simile itself is plain.",
            "Subject of गृह्णाति: not stated."),
        mcq("transfer", 5, "By the rule of निपातादेव, how is तस्मात् + एव (from that itself) written?",
            ("तस्मादेव", "त् before a vowel becomes द्, as in निपातात् + एव."),
            [("तस्मातेव", "त् does not stay unvoiced before a vowel."),
             ("तस्माच्चेव", "च्च comes before च, not before a vowel."),
             ("तस्मान्नेव", "न्न comes before a nasal, not before a vowel.")],
            "तस्मात् + एव = तस्मादेव, like निपातात् + एव = निपातादेव.",
            "Final त् + vowel → द्.",
            teaches="A final त् before a vowel becomes द्: निपातात् + एव → निपातादेव."),
    ],
}

# ---------------------------------------------------------------- unit 142
AUTHORED["142"] = {
    "title": "अविरुद्धे ध्रुवं दैवे",
    "question": "By unit 142, when does an action succeed, and so when should puṃsavana be applied?",
    "rule": ("When fate (दैव) is unopposed, an action applied in time certainly succeeds (सिद्धि); therefore one should "
             "apply puṃsavana and the like before the manifestation (व्यक्ति) of the foetus."),
    "limits": ("The foetus is not named here; व्यक्ति is read as its manifestation, as in unit 115. दैव is not explained. "
               "पुंसवनाद्यस्मात् is read पुंसवनादि + अस्मात् (therefore), not यस्मात्; पूर्व is read पूर्वम् (possible correction)."),
    "explain_hi": ("यह श्लोक कर्म की सफलता की शर्तें बताता है: दैव विरुद्ध न हो और कर्म समय पर किया जाए, तो उसकी सिद्धि निश्चित है। "
                   "इसी कारण (अस्मात्) पुंसवन आदि को (गर्भ के) व्यक्त होने से पहले प्रयोग में लाना चाहिए। "
                   "पुंसवन = पुत्र-प्राप्ति का संस्कार (इकाई 115 देखें)। "
                   "‘प्रयोजयेत्’ विधिलिङ् है: ‘प्रयोग करे, करना चाहिए’। "
                   "छपा ‘पूर्व’ पूर्वम् पढ़ा गया (सम्भावित सुधार)।"),
    "hook": "दैव अनुकूल + समय पर कर्म = सिद्धि; इसलिए पुंसवन पहले।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 142, when should puṃsavana and the like be applied?",
            ("Before the manifestation", "पूर्वं व्यक्तेः प्रयोजयेत्."),
            [("Right after the birth", "Birth is not named in unit 142."),
             ("At the time of delivery", "Delivery is not named in unit 142."),
             ("Only after the eighth month of pregnancy", "No month is named in unit 142.")],
            "The rite is to be applied before manifestation.",
            "पूर्वं व्यक्तेः = before manifestation."),
        order(1, "Put these parts of unit 142 in the verse's order.",
              ["अविरुद्धे ध्रुवं दैवे", "काले युक्तस्य कर्मणः", "सिद्धिः", "पुंसवनादि", "व्यक्तेः", "प्रयोजयेत्"],
              "Fate unopposed, action applied in time, success; puṃsavana and the like, before manifestation, should apply.",
              "दैव → काल-युक्त कर्म → सिद्धि → पुंसवनादि → व्यक्तेः → प्रयोजयेत्."),
        match(2, "Match each word of unit 142 to its meaning.",
              [["दैव", "fate"], ["अविरुद्ध", "unopposed"], ["सिद्धि", "success"], ["व्यक्ति", "manifestation"],
               ["प्रयोजयेत्", "one should apply"]],
              "These words carry the condition and the rule.",
              "दैव, अविरुद्ध, सिद्धि, व्यक्ति, प्रयोजयेत्.", role="extend",
              teaches="अस्मात् (from this) here means therefore: the rule follows from the condition."),
        mcq("discriminate", 3, "What form does the card give प्रयोजयेत्?",
            ("Optative: one should apply", "Labelled 3 sg. opt. causative."),
            [("Past: he applied", "The label is optative, not past."),
             ("Future: he will apply", "The label is optative, not future."),
             ("Present plural: they apply", "The label is third person singular.")],
            "प्रयोजयेत् = one should apply, an optative.",
            "-एत् = optative, should."),
        multi("apply", 4, "Which statements match unit 142?",
              [("Success needs fate to be unopposed", "Right: अविरुद्धे दैवे."),
               ("The action must be applied in time", "Right: काले युक्तस्य कर्मणः."),
               ("Puṃsavana succeeds whatever fate may be", "Fate being unopposed is a condition."),
               ("The verse names the month for puṃsavana", "No month is named.")],
              [0, 1],
              "Two conditions: fate unopposed and timely action.",
              "अविरुद्ध दैव + काल-युक्त कर्म → सिद्धि."),
        mcq("transfer", 5, "Built like प्रयोजयेत्, which word means one should go?",
            ("गच्छेत्", "-एत् on the stem गच्छ-: optative, one should go."),
            [("गच्छति", "That means he goes."),
             ("गमिष्यति", "That means he will go."),
             ("अगच्छत्", "That means he went.")],
            "गच्छेत् = one should go, like प्रयोजयेत् = one should apply.",
            "-एत् = optative, one should.",
            teaches="-एत् on an a-stem verb gives the optative: one should do it."),
    ],
}

# ---------------------------------------------------------------- unit 143
AUTHORED["143"] = {
    "title": "जाताश्चैवं रूपवन्तः",
    "question": "By unit 143, what are those born in this way like?",
    "rule": ("Those born thus are beautiful (रूपवन्तः), of great sattva (महासत्त्वाः), long-lived (चिरायुषः). Good sons would "
             "be releasers from debt (ऋणान्मोचयितारः), regarded so by those who have sons."),
    "limits": ("Line 1 has no verb. The kind of debt is not stated. पुत्रिणां मताः is read 'regarded by those who have "
               "sons'; 'accounted among those with sons' is possible, and the subject division of line 2 can go two ways. "
               "No question uses those readings."),
    "explain_hi": ("यह श्लोक बताता है कि इस प्रकार (पिछली विधि से) जन्मे सन्तान रूपवान, महान् सत्त्व वाले और दीर्घायु होते हैं। "
                   "दूसरी पंक्ति: अच्छे पुत्र ऋण से मुक्त कराने वाले हों (स्युः), पुत्र वालों द्वारा माने गए। "
                   "कौन-सा ऋण, यह नहीं कहा गया। ‘पुत्रिणां मताः’ का दूसरा अर्थ भी सम्भव है, इसलिए उस पर प्रश्न नहीं। "
                   "‘ऋणान्मोचयितारः’ = ऋणात् + मोचयितारः (त् → न् अनुनासिक से पहले, विकल्प से; द् भी शुद्ध; जैसा छपा है)।"),
    "hook": "ऐसे जन्मे: सुन्दर, बड़े मन वाले, दीर्घायु; अच्छे पुत्र ऋण से छुड़ाते हैं।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 143, the releasers (मोचयितारः) release from what?",
            ("From debt (ऋण)", "ऋणात् मोचयितारः: releasers from debt."),
            [("From disease (रोग)", "Disease is not named in unit 143."),
             ("From fear", "Fear is not named in unit 143."),
             ("From poverty (दारिद्र्य)", "Poverty is not named in unit 143.")],
            "The verse names releasers from debt (ऋणात्).",
            "ऋणात् = from debt."),
        order(1, "Put these words of unit 143 in the verse's order.",
              ["जाताः", "रूपवन्तः", "महासत्त्वाः", "चिरायुषः", "ऋणात्", "मोचयितारः"],
              "Born, beautiful, of great sattva, long-lived; from debt, releasers.",
              "जाताः → रूपवन्तः → महासत्त्वाः → चिरायुषः → ऋणात् → मोचयितारः."),
        match(2, "Match each word of unit 143 to its meaning.",
              [["रूपवत्", "having beauty"], ["महासत्त्व", "of great sattva (mind)"], ["चिरायुस्", "long-lived"],
               ["ऋण", "debt"], ["सुपुत्र", "good son"]],
              "These words carry the praise of the children.",
              "रूपवत्, महासत्त्व, चिरायुस्, ऋण, सुपुत्र.", role="extend",
              teaches="चिर + आयुस् = whose life is long: a bahuvrīhi describing the children."),
        mcq("discriminate", 3, "Which split of ऋणान्मोचयितारः is right?",
            ("ऋणात् + मोचयितारः", "त् before the nasal म is printed as न् (optional; द् is also correct)."),
            [("ऋणम् + मोचयितारः", "A final म् would give ऋणं मोचयितारः."),
             ("ऋणः + मोचयितारः", "A visarga would give ऋणो मोचयितारः."),
             ("ऋणा + न्मोचयितारः", "न्मोचयितारः is not a word.")],
            "ऋणात् (from debt) + मोचयितारः (releasers).",
            "Final त् + nasal → optionally न् (द् is also correct; the print has न्)."),
        mcq("apply", 4, "A translation of line 1 of unit 143 reads: 'Those born thus are beautiful, of great sattva, short-lived.' Which word is wrong?",
            ("short-lived", "चिरायुषः means long-lived, not short-lived."),
            [("born", "जाताः = born (ones): right."),
             ("beautiful", "रूपवन्तः = having beauty: right."),
             ("of great sattva", "महासत्त्वाः = of great sattva (mind): right.")],
            "Line 1 calls those born thus long-lived (चिरायुषः).",
            "चिर + आयुस् = long-lived."),
        mcq("transfer", 5, "By the rule of ऋणान्मोचयितारः, how is सत् + मार्गः (good path) usually written?",
            ("सन्मार्गः", "त् before the nasal म may become न् (optional; सद्मार्गः is also correct)."),
            [("सत्मार्गः", "त् does not stay unvoiced before a nasal."),
             ("सच्मार्गः", "त् becomes च् only before च/छ."),
             ("समार्गः", "The consonant is not lost.")],
            "सत् + मार्गः = सन्मार्गः, like ऋणात् + मोचयितारः.",
            "Final त् + nasal → optionally न् (द् is also correct).",
            teaches="A final त् before a nasal may become न् (optional; द् is also correct): ऋणात् + मोचयितारः → ऋणान्मोचयितारः."),
    ],
}

# ---------------------------------------------------------------- unit 144
AUTHORED["144"] = {
    "title": "दैवताचारशौचादिरता",
    "question": "By line 1 of unit 144, what kind of woman bears a child of great qualities?",
    "rule": ("She who is devoted to the gods, conduct, purity and the like (दैवत-आचार-शौच-आदि-रता) bears one of great "
             "qualities (महागुणम्). The woman is shown only by the feminine रता."),
    "limits": ("Low confidence for line 2: धावति (runs, is carried on) and prāgjanma (former birth, or birth before) are not "
               "made firm, so no question uses line 2. दैवत may also go with आचार (conduct towards the gods)."),
    "explain_hi": ("पहली पंक्ति कहती है: जो देवताओं, आचार, शौच आदि में रत है, वह महान् गुणों वाले (सन्तान) को जन्म देती है। "
                   "‘स्त्री’ शब्द नहीं है; स्त्रीलिंग ‘रता’ से समझा जाता है, और ‘महागुणम्’ के साथ भी संज्ञा नहीं। "
                   "दूसरी पंक्ति कठिन है: आचरण किया हुआ पूर्व जन्म के अभ्यास के योग से ‘दौड़ता’ (आगे चलता) है; "
                   "इसका अर्थ पक्का नहीं, इसलिए उस पर प्रश्न नहीं। "
                   "‘दैवत’ को ‘आचार’ के साथ (देवताओं के प्रति आचार) भी पढ़ा जा सकता है।"),
    "hook": "देव, आचार, शौच में रत माता → महागुण सन्तान।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By line 1 of unit 144, the woman devoted to what bears one of great qualities?",
            ("Gods, conduct, purity and the like", "दैवताचारशौचादिरता."),
            [("Wealth, ornaments, fine clothes and the like", "Wealth is not named."),
             ("Sleep, rest and the like", "Sleep is not named."),
             ("Sweet food and water-sport", "Those are causes of colour in unit 135.")],
            "Devotion to gods, conduct, purity and the like is named.",
            "दैवत, आचार, शौच, आदि + रता."),
        order(1, "Put the words of line 1 of unit 144 in the verse's order.",
              ["दैवत", "आचार", "शौच", "आदिरता", "सूते", "महागुणम्"],
              "Gods, conduct, purity, and the like, devoted; bears; one of great qualities.",
              "दैवत → आचार → शौच → आदिरता → सूते → महागुणम्."),
        match(2, "Match each word of line 1 of unit 144 to its meaning.",
              [["आचार", "conduct"], ["शौच", "purity"], ["रता", "devoted"], ["सूते", "bears, gives birth to"],
               ["महागुण", "of great qualities"]],
              "These words carry the whole first line.",
              "आचार, शौच, रता, सूते, महागुण.", role="extend",
              teaches="-रत at the end of a compound = devoted to: X-रता = (a woman) devoted to X."),
        mcq("discriminate", 3, "By the card, how is it known that a woman is meant in line 1?",
            ("From the feminine ending of रता", "The note: 'woman' is understood from the feminine ratā."),
            [("The word स्त्री appears in the line", "No noun for woman is stated."),
             ("The verb सूते is feminine", "Verbs carry no gender."),
             ("The word योषित् appears in the line", "योषितः comes in unit 145.")],
            "The feminine रता alone shows that a woman is meant.",
            "रता = f. nom. sg."),
        multi("apply", 4, "Which statements about unit 144 match the card?",
              [("No noun for woman is stated in line 1", "Right: understood from रता."),
               ("The sense of line 2 is not made firm", "Right: the note says the sentence is hard."),
               ("Line 2 says former-birth practice fixes the child's colour", "Colour is not named; line 2 is unsettled."),
               ("Line 1 says the child will be a son", "महागुणम् has no noun; no son is named.")],
              [0, 1],
              "Line 1 implies the woman by gender; line 2 stays unsettled.",
              "रता → woman understood; line 2 not firm."),
        mcq("transfer", 5, "By the rule of रता, which word means a woman devoted to dharma, as subject?",
            ("धर्मरता", "Feminine nominative singular, like दैवताचारशौचादिरता."),
            [("धर्मरतः", "That is masculine: a man devoted to dharma."),
             ("धर्मरतम्", "That is neuter or accusative, not a feminine subject."),
             ("धर्मरताः", "That is plural, not one woman.")],
            "धर्म + रता = धर्मरता, like ...आदि + रता.",
            "-रता = feminine nom. sg., devoted to.",
            teaches="रत (devoted) takes the feminine -आ for a woman: X-रता = she who is devoted to X."),
    ],
}

# ---------------------------------------------------------------- unit 145
AUTHORED["145"] = {
    "title": "योषितोऽपि स्रवन्त्येव शुक्रम्",
    "question": "By unit 145, do women too discharge śukra, and is it thought to do nothing for the foetus?",
    "rule": ("Women too discharge śukra (here: reproductive fluid) at union with a man. It is not thought (न चिन्त्यते) "
             "that it does nothing at all for the foetus: a double negation."),
    "limits": ("The verse does not say what women's śukra does for the foetus; it only denies that it does nothing. "
               "śukra is normally semen; applied to women the card reads reproductive fluid."),
    "explain_hi": ("यह श्लोक कहता है कि स्त्रियाँ भी पुरुष के साथ समागम में शुक्र (प्रजनन द्रव) का स्राव करती ही हैं। "
                   "दूसरी पंक्ति में दोहरा निषेध है: ‘वह गर्भ के लिए कुछ नहीं करता’ — ऐसा नहीं सोचा जाता। "
                   "वह गर्भ के लिए क्या करता है, यह नहीं बताया गया। "
                   "‘योषितोऽपि’ = योषितः + अपि (अः + अ → ओऽ); ‘स्रवन्त्येव’ = स्रवन्ति + एव (इ + ए → ये)।"),
    "hook": "स्त्रियाँ भी शुक्र स्रवित करती हैं; वह ‘कुछ नहीं करता’ — ऐसा नहीं माना जाता।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 145, who too discharge śukra at union?",
            ("Women", "योषितोऽपि स्रवन्त्येव शुक्रम्."),
            [("Only men", "अपि (too) adds women to men."),
             ("Only pregnant women", "Pregnancy is not named in line 1."),
             ("Children", "Children are not named.")],
            "Women too discharge śukra at union with a man.",
            "योषितः अपि = women too."),
        order(1, "Put these words of line 1 of unit 145 in the verse's order.",
              ["योषितः", "अपि", "स्रवन्ति", "शुक्रम्", "पुंसः", "समागमे"],
              "Women, too, discharge, śukra, of a man, at union.",
              "योषितः → अपि → स्रवन्ति → शुक्रम् → पुंसः → समागमे."),
        match(2, "Match each word of unit 145 to its meaning.",
              [["योषित्", "woman"], ["स्रवन्ति", "discharge"], ["पुंस्", "man"], ["समागम", "union"],
               ["चिन्त्यते", "is thought"]],
              "These words carry both lines.",
              "योषित्, स्रवन्ति, पुंस्, समागम, चिन्त्यते.", role="extend",
              teaches="चिन्त्यते is passive: is thought; न चिन्त्यते = is not thought."),
        mcq("discriminate", 3, "What does line 2 of unit 145 say of women's śukra?",
            ("It is not thought to do nothing for the foetus", "Both negatives are printed: न ... करोति इति न चिन्त्यते."),
            [("It is thought to do nothing for the foetus", "This drops the second न of न चिन्त्यते."),
             ("It alone forms the whole foetus", "The verse makes no such claim."),
             ("It does harm to the foetus", "Harm is not named.")],
            "The line denies the view that it does nothing.",
            "न किंचित् करोति इति न चिन्त्यते."),
        mcq("apply", 4, "A translation reads: 'Women too discharge śukra at union with a child.' Which word is wrong?",
            ("child", "पुंसः means of a man, not of a child."),
            [("Women", "योषितः = women: right."),
             ("too", "अपि = too: right."),
             ("union", "समागमे = at union: right.")],
            "The line says union with a man (पुंसः).",
            "पुंसः = of a man."),
        mcq("transfer", 5, "By the rule of स्रवन्त्येव, how is अस्ति + एव (is indeed) written when joined?",
            ("अस्त्येव", "इ before ए becomes य्, as स्रवन्ति + एव → स्रवन्त्येव."),
            [("अस्तेव", "इ + ए does not give a plain ए."),
             ("अस्तैव", "इ + ए does not give ऐ."),
             ("अस्तीव", "That is अस्ति + इव, not अस्ति + एव.")],
            "अस्ति + एव = अस्त्येव, like स्रवन्ति + एव.",
            "इ + a different vowel → य् + that vowel.",
            teaches="A final इ before a different vowel becomes य्: स्रवन्ति + एव → स्रवन्त्येव."),
    ],
}

# ---------------------------------------------------------------- unit 146
AUTHORED["146"] = {
    "title": "इति पुत्रकामीयो नाम प्रथमोऽध्यायः",
    "question": "How does the colophon of unit 146 name the chapter just ended?",
    "rule": ("इति पुत्रकामीयः नाम प्रथमः अध्यायः: thus (ends) the first chapter, named Putrakāmīya (relating to the "
             "desire for a son)."),
    "limits": ("A colophon only. The verb 'ends' is not in the Sanskrit; इति marks the close."),
    "explain_hi": ("यह अध्याय की समाप्ति-पंक्ति (पुष्पिका) है: ‘इस प्रकार पुत्रकामीय नामक प्रथम अध्याय।’ "
                   "‘पुत्रकामीय’ का अर्थ है ‘पुत्र की कामना से सम्बन्धित’; इकाई 3 में इसी नाम की घोषणा थी। "
                   "‘पुत्रकामीयो नाम’ में पुत्रकामीयः + नाम है (अः → ओ घोष व्यंजन से पहले), "
                   "और ‘प्रथमोऽध्यायः’ में प्रथमः + अध्यायः (अः + अ → ओऽ)।"),
    "hook": "इति पुत्रकामीयो नाम प्रथमोऽध्यायः: पहला अध्याय पूरा।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What name does the colophon of unit 146 give the chapter?",
            ("Putrakāmīya", "पुत्रकामीयो नाम: named Putrakāmīya."),
            [("Ārtavavyāpad", "The colophon names no such chapter."),
             ("Garbhiṇīcaryā", "The colophon names no such chapter."),
             ("Śukraśodhana", "The colophon names no such chapter.")],
            "The chapter is named Putrakāmīya.",
            "पुत्रकामीयः नाम."),
        order(1, "Put the words of the colophon in its order.",
              ["इति", "पुत्रकामीयः", "नाम", "प्रथमः", "अध्यायः"],
              "Thus, Putrakāmīya, named, first, chapter.",
              "इति → पुत्रकामीयः → नाम → प्रथमः → अध्यायः."),
        match(2, "Match each word of the colophon to its meaning.",
              [["इति", "thus"], ["पुत्रकामीय", "relating to the desire for a son"], ["नाम", "named"],
               ["प्रथम", "first"], ["अध्याय", "chapter"]],
              "Five words make the whole colophon.",
              "इति, पुत्रकामीय, नाम, प्रथम, अध्याय.", role="extend",
              teaches="X नाम = named X: नाम after a name marks it as a title."),
        mcq("discriminate", 3, "Which split of प्रथमोऽध्यायः is right?",
            ("प्रथमः + अध्यायः", "अः + अ → ओ, and ऽ marks the lost अ."),
            [("प्रथमा + अध्यायः", "आ + अ would give प्रथमाध्यायः."),
             ("प्रथम + ध्यायः", "ध्यायः is not a word; the noun is अध्यायः."),
             ("प्रथमम् + अध्यायः", "A final म् would give प्रथममध्यायः.")],
            "प्रथमः (first) + अध्यायः (chapter).",
            "अः + अ → ओऽ."),
        mcq("apply", 4, "Which split of पुत्रकामीयोनाम is right?",
            ("पुत्रकामीयः + नाम", "अः before the voiced न becomes ओ."),
            [("पुत्रकामीयम् + नाम", "A final म् would give पुत्रकामीयं नाम."),
             ("पुत्रकामी + योनाम", "योनाम is not a word."),
             ("पुत्रकामीय + उनाम", "उनाम is not a word.")],
            "पुत्रकामीयः + नाम: अः → ओ before a voiced consonant.",
            "अः + voiced consonant → ओ."),
        mcq("transfer", 5, "By the rule of प्रथमोऽध्यायः, how is द्वितीयः + अध्यायः (second chapter) written?",
            ("द्वितीयोऽध्यायः", "अः + अ → ओ with ऽ, as in प्रथमः + अध्यायः."),
            [("द्वितीयाध्यायः", "That joins a plain अ, not अः."),
             ("द्वितीय अध्यायः", "Visarga drops this way only before vowels other than अ."),
             ("द्वितीयरध्यायः", "अः does not become र् here.")],
            "द्वितीयः + अध्यायः = द्वितीयोऽध्यायः.",
            "अः + अ → ओऽ.",
            teaches="A final अः before अ becomes ओ, and the अ is shown by ऽ: प्रथमः + अध्यायः → प्रथमोऽध्यायः."),
    ],
}

# ===================================================================== NOTES_HI
NOTES_HI = {
    "134": ("गद्य-पंक्ति; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। छपा ‘घृतमंदाभे’ है; डेटा का पद-विभाग इसे घृत-मण्ड-आभे पढ़ता है "
            "(घृतमण्ड को शाब्दिक ‘घी-मण्ड’ रखा गया, निश्चित अर्थ नहीं बताया गया)। ‘शुक्रे शुक्रे’ की पुनरुक्ति वितरणार्थक मानी गई। "
            "‘घृतमण्डाभे’ के बाद का ‘वा’ अस्पष्ट है, तय नहीं। किसका शुक्र है, नहीं कहा गया; इकाई 145 स्त्रियों के लिए भी शुक्र शब्द "
            "प्रयुक्त करती है। सन्धि जाँची: तैल + आभे → तैलाभे (अ + आ → आ); मधु + आभे → मध्वाभे (उ + आ → वा)।"),
    "135": ("विश्वास निम्न। पाठ-चिह्न: (1) ‘उपयोगाम्मातुर्’ — सम्भावित सुधार उपयोगान्मातुर् (त् + म → न्म, विकल्प से), छपा म्; "
            "(2) ‘तिलांन्नविदाहिनो’ — क्षतिग्रस्त अन्त, सम्भावित तिलान्नविदाहिनाम्; पाठ अनुमानित, और ‘तिलान्न’ एक पद या दो, तय नहीं; "
            "(3) ‘श्यामत्ता’ = श्यामता (दोहरा त् निश्चित वर्तनी-भेद)। ‘उपयोगात्’ दूसरे-तीसरे खण्ड में समझा जाता है। "
            "सन्धि जाँची: मातुः + उदक → मातुरुदक (उ के बाद विसर्ग → र्); उदकविहारात् + च → उदकविहाराच्च।"),
    "136": ("विश्वास उच्च; कोई पाठ-चिह्न नहीं; क्रिया नहीं। ‘वर्ण’ = त्वचा का रंग (जाति नहीं)। ‘अनुवृत्तितः’ में ‘-तः’ अपादानार्थक। "
            "सन्धि जाँची: अनुवृत्तितः + च → अनुवृत्तितश्च (विसर्ग → श्)।"),
    "137": ("विश्वास मध्यम; कोई पाठ-चिह्न नहीं; क्रिया नहीं। ‘धातु’ = महाभूत/तत्त्व, शरीर-धातु नहीं। दूसरे खण्ड में ‘तेजस् का’ "
            "पहले खण्ड से समझा जाता है, लिखा नहीं। सन्धि जाँची: तेजस् + धातोः → तेजोधातोः (अस् → ओ घोष से पहले); "
            "धातोः + उदक → धातोरुदक (विसर्ग → र्); संपर्कात् + गौरता → संपर्काद्गौरता (त् → द्)।"),
    "138": ("विश्वास मध्यम। पाठ-चिह्न: ‘सत्व’ = सत्त्व (वर्तनी); ‘अंतैर्वत्न्याः’ → अन्तर्वत्न्याः (सम्भावित, अर् का ऐ हो गया); "
            "‘अभीक्ष्ण,’ → अभीक्ष्णम् (सम्भावित, अन्तिम म् लुप्त; अल्पविराम छपाई-चिह्न)। ‘भवति’ कर्म के बाद शाब्दिक रखा गया, "
            "वाक्य सँवारा नहीं गया। क्या सुना जाए, नहीं कहा गया। सन्धि जाँची: पूर्वाभ्यासः + च + इति → पूर्वाभ्यासश्चेति।"),
    "139": ("विश्वास उच्च; कोई पाठ-चिह्न नहीं। आगे के श्लोकों की भूमिका; ‘श्लोक’ शब्द संस्कृत में नहीं, कोष्ठक में। "
            "सन्धि: च + अत्र → चात्र (अ + अ → आ)। छपा ‘भवंति’ = भवन्ति (अनुस्वार = न्)।"),
    "140": ("विश्वास निम्न; दो छपी पंक्तियाँ (02.01.157–158) एक वाक्य। पाठ-चिह्न: ‘घृतक्षीरदि’ → घृतक्षीरादि (सम्भावित); "
            "‘मत्त्यासु’ क्षतिग्रस्त, स्त्रीलिंग सप्तमी बहुवचन जैसा, पुनर्स्थापित नहीं। ‘घृतक्षीरादि’ और ‘मत्त्यासु’ का पक्का अर्थ नहीं बैठता। "
            "स्त्रियाँ केवल स्त्रीलिंग अन्त से; आर्तव किसमें ठहरता है, नहीं कहा गया; आर्तव = रज/स्त्री-बीज (सम्भावित)। "
            "छपा ‘मुदितासुकफात्मसु’ = मुदितासु कफात्मसु। सन्धि: विपरीतासु + अतः + अन्यथा → विपरीतास्वतोऽन्यथा।"),
    "141": ("विश्वास निम्न; दो छपी पंक्तियाँ। ‘गृह्णाति’ का कर्ता नहीं कहा गया (सम्भवतः पिछला आर्तव), तय नहीं; ‘निपात’ की व्याख्या नहीं। "
            "पाठ-चिह्न: ‘गर्भतथा’ → गर्भस्तथा (सम्भावित, स् लुप्त) — इसलिए ‘गर्भ’ अनुमानित। दूसरी पंक्ति में क्रिया नहीं; "
            "‘ध्रुवम्’ क्रियाविशेषण या गर्भ का विशेषण; ‘उपस्कृतम्’ क्षेत्र और बीज दोनों से भी जुड़ सकता है। "
            "छपा ‘यथाऽमलं’: सामान्य लेखन यथामलम् (आ + अ → आ); ऽ यहाँ मिले हुए अ को दिखाता है। "
            "सन्धि: निपातात् + एव → निपातादेव; वासः + यथा → वासो यथा।"),
    "142": ("विश्वास मध्यम; दो छपी पंक्तियाँ एक वाक्य (कर्ता ‘सिद्धिः’ दूसरी पंक्ति में)। पाठ-चिह्न: ‘पूर्व’ → पूर्वम् (सम्भावित)। "
            "‘पुंसवनाद्यस्मात्’ = पुंसवनादि + अस्मात् (इ + अ → य), यस्मात् नहीं — समीक्षा का निर्णय। "
            "‘व्यक्तेः’ = (गर्भ के) व्यक्त होने से, इकाई 115 की तरह; गर्भ यहाँ नामित नहीं। दैव की व्याख्या नहीं।"),
    "143": ("विश्वास मध्यम; कोई पाठ-चिह्न नहीं। पहली पंक्ति में क्रिया नहीं। ‘पुत्रिणां मताः’ = पुत्र वालों द्वारा माने गए; "
            "दूसरा अर्थ ‘पुत्र वालों में गिने गए’ भी सम्भव; दूसरी पंक्ति का कर्ता-विभाग भी दो तरह। ऋण का प्रकार नहीं कहा गया। "
            "सन्धि: जाताः + च → जाताश्च; ऋणात् + मोचयितारः → ऋणान्मोचयितारः (त् → न्, विकल्प से; द् भी शुद्ध; जैसा छपा)।"),
    "144": ("विश्वास निम्न; कोई पाठ-चिह्न नहीं। ‘स्त्री’ शब्द नहीं, स्त्रीलिंग ‘रता’ से समझा जाता है। ‘दैवत’ को ‘आचार’ के साथ "
            "(देवताओं के प्रति आचार) भी पढ़ा जा सकता है। दूसरी पंक्ति: ‘धावति’ (दौड़ता, आगे चलता; ‘धोता’ भी) का अर्थ पक्का नहीं; "
            "‘प्राग्जन्म’ = पूर्व जन्म या पहले का जन्म, तय नहीं। छपा ‘चाचरितंप्राग्जन्म’ = च + आचरितम् + प्राग्जन्म।"),
    "145": ("विश्वास मध्यम; कोई पाठ-चिह्न नहीं। शुक्र सामान्यतः वीर्य; स्त्रियों के सन्दर्भ में प्रजनन द्रव पढ़ा गया। "
            "दोहरा निषेध छपे अनुसार: ‘तत् गर्भस्य न किंचित् करोति’ इति ‘न चिन्त्यते’। "
            "सन्धि: योषितः + अपि → योषितोऽपि; स्रवन्ति + एव → स्रवन्त्येव; तत् + न → तन्न (विकल्प से); किंचित् + तु → किंचित्तु; करोति + इति → करोतीति।"),
    "146": ("पुष्पिका; विश्वास उच्च; कोई पाठ-चिह्न नहीं। अन्तिम ‘इति’ समाप्ति-सूचक। छपा ‘पुत्रकामीयोनाम’ = पुत्रकामीयः नाम। "
            "सन्धि: प्रथमः + अध्यायः → प्रथमोऽध्यायः (अः + अ → ओऽ)।"),
}

# ===================================================================== AIDS
AIDS = {
    "134": {
        "diagram": {"groups": [
            {"label": "शुक्र की आभा", "items": ["घृतमण्ड जैसा", "तेल जैसा", "शहद जैसा"]},
            {"label": "गर्भ का वर्ण", "items": ["गौरत्व", "कृष्णत्व", "श्यामत्व"]}]},
        "chunks": "तत्र शुक्रे शुक्रे | घृतमंदाभे वा गर्भस्य गौरत्वं | तैलाभे कृष्णत्वं | मध्वाभे श्यामत्वं",
        "sandhi": "उ + आ → वा: मधु + आभे → मध्वाभे · अ + आ → आ: तैल + आभे → तैलाभे।",
        "pegs": "मेरा बनाया चित्र: तीन कटोरियाँ — घी (हल्का), तेल (गहरा), शहद (बीच का) — हर एक के आगे उसी रंग का छोटा शिशु। (केवल याद के लिए)",
    },
    "135": {
        "diagram": {"groups": [
            {"label": "माता का आचरण", "items": ["दूध आदि मधुर का सेवन, जल-विहार", "तिल-अन्न, विदाही (अनुमानित पाठ)", "व्यामिश्र (मिले-जुले)"]},
            {"label": "वर्ण", "items": ["गौरता", "कृष्णता", "श्यामता"]}]},
        "chunks": "तथा क्षीरादिमधुराणामुपयोगात् | मातुरुदकविहाराच्च गौरता | तिलान्नविदाहिनां (?) कृष्णता | व्यामिश्राणां श्यामता",
        "sandhi": "उ के बाद विसर्ग → र् स्वर से पहले: मातुः + उदक → मातुरुदक · त् + च → च्च: उदकविहारात् + च → उदकविहाराच्च।",
        "contrast": "इकाई 134: शुक्र की आभा से वर्ण ↔ इकाई 135: माता के आहार-विहार से वर्ण। क्रम दोनों में एक: गौर, कृष्ण, श्याम।",
    },
    "136": {
        "chunks": "देशकुलानुवृत्तितश्च | वर्णभेदः",
        "sandhi": "विसर्ग + च → श्च: अनुवृत्तितः + च → अनुवृत्तितश्च।",
        "anchors": "याद-सूत्र: ‘देश-कुल’ = जहाँ और जिस घर में जन्म; उसी के अनुसार रंग का भेद। (मेरी याद-पद्धति)",
    },
    "137": {
        "diagram": {"groups": [
            {"label": "तेजस् का जल-आकाश से संपर्क", "items": ["गौरता"]},
            {"label": "पृथ्वी-वायु से संपर्क", "items": ["कृष्णता"]},
            {"label": "सब धातुओं का साम्य", "items": ["श्यामता"]}]},
        "chunks": "तथा तेजोधातोः | उदकाकाशधातुसंपर्काद्गौरता | भूवायुसंपर्कात् कृष्णता | सर्वधातुसाम्ये श्यामता",
        "sandhi": "त् → द् घोष से पहले: संपर्कात् + गौरता → संपर्काद्गौरता · विसर्ग → र् स्वर से पहले: धातोः + उदक → धातोरुदक।",
        "contrast": "तीनों इकाइयों में एक ही क्रम — 134: घी/तेल/शहद · 135: दूध-जलविहार / (तिल-विदाही) / मिश्र · 137: जल-आकाश / भू-वायु / साम्य → गौर / कृष्ण / श्याम।",
    },
    "138": {
        "diagram": {"groups": [
            {"label": "सत्त्व-विशेष के कारण (क्रम से)", "items": ["माता-पिता का सत्त्व", "बार-बार के श्रवण", "स्वोपचित कर्म", "पूर्वाभ्यास"]}]},
        "chunks": "सत्त्वविशेषकराणि पुनः | मातापितृसत्त्वानि | अन्तर्वत्न्याः श्रुतयश्चाभीक्ष्णम् | स्वोपचितं कर्म भवति | पूर्वाभ्यासश्चेति",
        "sandhi": "विसर्ग + च → श्च, अ + इ → ए: पूर्वाभ्यासः + च + इति → पूर्वाभ्यासश्चेति · अ + उ → ओ: स्व + उपचितम् → स्वोपचितम्।",
        "letters": "चार कारणों के पहले अक्षर: मा-श्रु-स्व-पू (माता-पिता, श्रुति, स्वकर्म, पूर्वाभ्यास)। (मेरी याद-पद्धति)",
    },
    "139": {
        "chunks": "भवन्ति | च | अत्र",
        "sandhi": "अ + अ → आ: च + अत्र → चात्र।",
        "contrast": "इकाई 138: भवति (एकवचन, ‘है’) ↔ इकाई 139: भवन्ति (बहुवचन, ‘हैं’)।",
    },
    "140": {
        "seesaw": "मुदिता, कफात्मा स्त्रियों में: आर्तव चिरं तिष्ठति ↔ विपरीत स्त्रियों में: अतः अन्यथा।",
        "chunks": "घृतक्षीरादि मत्त्यासु (?) | मुदितासु कफात्मसु ‖ आर्तवं तिष्ठति चिरं | विपरीतास्वतोऽन्यथा",
        "sandhi": "उ + अ → व: विपरीतासु + अतः → विपरीतास्वतः · अः + अ → ओऽ: अतः + अन्यथा → अतोऽन्यथा।",
    },
    "141": {
        "story": "मेरी बनाई कल्पना (केवल याद के लिए): स्वच्छ वस्त्र गिरने मात्र से रंग पकड़ लेता है। क्या गिरता है और किस वस्तु की तुलना है, श्लोक नहीं कहता।",
        "chunks": "निपातादेव गृह्णाति | रागं वासो यथाऽमलं ‖ ध्रुवं गर्भ(स्)तथा | बीजं क्षेत्रं | बीजमुपस्कृतं",
        "sandhi": "त् → द् स्वर से पहले: निपातात् + एव → निपातादेव · अः → ओ घोष से पहले: वासः + यथा → वासो यथा।",
    },
    "142": {
        "chain": {"steps": ["दैव अविरुद्ध हो", "काल में युक्त कर्म", "सिद्धि (ध्रुवम्)", "अस्मात् (इसलिए)", "पुंसवन आदि", "व्यक्ति से पहले"]},
        "chunks": "अविरुद्धे ध्रुवं दैवे | काले युक्तस्य कर्मणः ‖ सिद्धिः | पुंसवनाद्यस्मात् | पूर्वं व्यक्तेः प्रयोजयेत्",
        "sandhi": "इ + अ → य: पुंसवनादि + अस्मात् → पुंसवनाद्यस्मात् · त् + प → त्प: अस्मात् + पूर्वम् → अस्मात्पूर्वम्।",
        "frame": "शर्त (सप्तमी: अविरुद्धे दैवे, काले) → फल (सिद्धिः) → निष्कर्ष (अस्मात् ... प्रयोजयेत्)।",
    },
    "143": {
        "diagram": {"groups": [
            {"label": "जाताः (ऐसे जन्मे)", "items": ["रूपवन्तः", "महासत्त्वाः", "चिरायुषः"]},
            {"label": "सुपुत्राः", "items": ["ऋणान्मोचयितारः", "पुत्रिणां मताः"]}]},
        "chunks": "जाताश्चैवं | रूपवन्तो महासत्त्वाश्चिरायुषः ‖ ऋणान्मोचयितारः स्युः | सुपुत्राः पुत्रिणां मताः",
        "sandhi": "त् → न् अनुनासिक से पहले (विकल्प से; द् भी शुद्ध; जैसा छपा): ऋणात् + मोचयितारः → ऋणान्मोचयितारः · अः → ओ घोष से पहले: रूपवन्तः + महा → रूपवन्तो महा।",
        "pegs": "मेरा बनाया चित्र: तीन दीपक — सुन्दर रूप, बड़ा मन, लम्बी बाती (लम्बी आयु); पास में खुली हुई ऋण की गाँठ। (केवल याद के लिए)",
    },
    "144": {
        "chunks": "दैवताचारशौचादिरता | सूते महागुणं ‖ धावत्येवं चाचरितं | प्राग्जन्माभ्यासयोगतः",
        "frame": "पंक्ति 1: कौन (…रता, स्त्रीलिंग) → क्रिया (सूते) → किसे (महागुणम्)। पंक्ति 2 का अर्थ अनिश्चित।",
        "sandhi": "इ + ए → ये: धावति + एवम् → धावत्येवम् · अ + आ → आ: च + आचरितम् → चाचरितम्।",
    },
    "145": {
        "chunks": "योषितोऽपि स्रवन्त्येव | शुक्रं पुंसः समागमे ‖ गर्भस्य तन्न किंचित्तु | करोतीति न चिन्त्यते",
        "sandhi": "अः + अ → ओऽ: योषितः + अपि → योषितोऽपि · इ + ए → ये: स्रवन्ति + एव → स्रवन्त्येव · इ + इ → ई: करोति + इति → करोतीति।",
        "frame": "भीतरी वाक्य: ‘तत् गर्भस्य न किंचित् करोति’ (कुछ नहीं करता) + इति + बाहरी ‘न चिन्त्यते’ (ऐसा नहीं सोचा जाता) = दोहरा निषेध।",
    },
    "146": {
        "chunks": "इति | पुत्रकामीयो नाम | प्रथमोऽध्यायः",
        "sandhi": "अः → ओ घोष से पहले: पुत्रकामीयः + नाम → पुत्रकामीयो नाम · अः + अ → ओऽ: प्रथमः + अध्यायः → प्रथमोऽध्यायः।",
        "anchors": "याद-सूत्र: इकाई 3 में घोषणा ‘पुत्रकामियं (= पुत्रकामीयं) शारीरं व्याख्यास्यामः’, इकाई 146 में समाप्ति ‘पुत्रकामीयो नाम प्रथमोऽध्यायः’। (मेरी याद-पद्धति)",
    },
}

# ===================================================================== IMAGE_SPECS
IMAGE_SPECS = {
    ("134", "diagram"): {
        "file": "sh1-shukra-abha-134.svg",
        "alt": ("Table of unit 134: shukra resembling ghee-manda goes with fairness of the foetus, resembling oil with "
                "darkness, resembling honey with dusky colour."),
        "type": "table",
        "title": "शुक्र की आभा और गर्भ का वर्ण (इकाई १३४)",
        "heads": ["शुक्र की आभा", "गर्भ का वर्ण"],
        "rows": [["घृतमण्ड जैसा", "गौरत्व"], ["तेल जैसा", "कृष्णत्व"], ["शहद जैसा", "श्यामत्व"]],
    },
    ("135", "diagram"): {
        "file": "sh1-matr-ahara-varna-135.svg",
        "alt": ("Table of unit 135: the mother's use of milk and sweet things and her sport in water go with fairness; "
                "sesame-food and burning-causing things (conjectural reading) with darkness; mixed ones with dusky colour."),
        "type": "table",
        "title": "माता का आचरण और वर्ण (इकाई १३५)",
        "heads": ["माता का आचरण", "वर्ण"],
        "rows": [["दूध आदि मधुर, जल-विहार", "गौरता"], ["तिल-अन्न, विदाही (अनुमानित)", "कृष्णता"],
                 ["व्यामिश्र (मिले-जुले)", "श्यामता"]],
    },
    ("137", "diagram"): {
        "file": "sh1-dhatu-varna-137.svg",
        "alt": ("Flowchart of unit 137: the fire element in contact with water and space gives fairness; contact with earth "
                "and air gives darkness; balance of all elements gives dusky colour."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"तेजस् धातु\"] -->|\"जल, आकाश से संपर्क\"| B[\"गौरता\"]\n"
                 "  A -.->|\"भू, वायु से संपर्क<br/>(तेजस् का: समझा गया)\"| C[\"कृष्णता\"]\n"
                 "  D[\"सब धातुओं का साम्य\"] --> E[\"श्यामता\"]\n"),
    },
    ("138", "diagram"): {
        "file": "sh1-sattva-karana-138.svg",
        "alt": ("Mind map of unit 138: the factors that bring about special features of sattva (mind): the sattva of mother "
                "and father, the repeated hearings, one's own accumulated karma, and past practice."),
        "type": "mermaid",
        "code": ("mindmap\n"
                 "  सत्त्व-विशेष के कारण\n"
                 "    माता-पिता का सत्त्व\n"
                 "    बार-बार के श्रवण\n"
                 "    स्वोपचित कर्म\n"
                 "    पूर्वाभ्यास\n"),
    },
    ("142", "chain"): {
        "file": "sh1-pumsavana-kala-142.svg",
        "alt": ("Flowchart of unit 142: fate unopposed and an action applied in time lead to certain success; therefore "
                "puṃsavana and the like are to be applied before manifestation."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"दैव अविरुद्ध\"] --> C[\"सिद्धि निश्चित\"]\n"
                 "  B[\"काल में युक्त कर्म\"] --> C\n"
                 "  C -->|\"इसलिए\"| D[\"पुंसवन आदि\"]\n"
                 "  D --> E[\"व्यक्ति से पहले प्रयोग\"]\n"),
    },
    ("143", "diagram"): {
        "file": "sh1-suputra-143.svg",
        "alt": ("Mind map of unit 143: those born thus are beautiful, of great sattva and long-lived; good sons are "
                "releasers from debt, regarded so by those who have sons."),
        "type": "mermaid",
        "code": ("mindmap\n"
                 "  इकाई १४३\n"
                 "    ऐसे जन्मे\n"
                 "      रूपवान\n"
                 "      महासत्त्व\n"
                 "      दीर्घायु\n"
                 "    सुपुत्र\n"
                 "      ऋण से छुड़ाने वाले\n"
                 "      पुत्रवालों के माने\n"),
    },
}
