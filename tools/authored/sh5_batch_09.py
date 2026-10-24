from helpers import mcq, match, order, fill, multi, accepts


AUTHORED = {}

# ---------------------------------------------------------------- unit 102
AUTHORED["102"] = {
    "title": "सक्थिनि पंच पादनखाः",
    "question": "By unit 102, which bones are counted first in each lower limb (sakthi)?",
    "rule": ("In each single lower limb (सक्थि): five foot-nails (पादनख); in each toe (अङ्गुली) three bones; those are "
             "fifteen. The nails are counted among the bones, as printed."),
    "limits": ("Prose. The print splits 'each single' over two words with a stray -a (तत्रैकै कस्मिन): no question on that "
               "form. 'Those are fifteen' is taken as 3 bones x 5 toes; the Sanskrit does not say what it counts, so no "
               "question rests on that sum."),
    "explain_hi": ("यह गद्य-पंक्ति एक सक्थि, यानी एक निचले अंग, की अस्थियों की गिनती आरम्भ करती है। "
                   "पहले पाँच पादनख (पैर के नाखून) गिने गए हैं; छपे पाठ में नख भी अस्थियों में गिने गए हैं। "
                   "फिर प्रत्येक अंगुली में तीन अस्थियाँ बताई गई हैं, और अन्त में ‘तानि पंचदश’, वे पन्द्रह। "
                   "‘पन्द्रह’ को पाँच अंगुलियों की तीन-तीन अस्थियाँ माना गया है, पर संस्कृत स्वयं नहीं कहती कि क्या गिना गया। "
                   "छपाई में ‘एकैकस्मिन्’ (एक-एक में) दो टुकड़ों में बँटा है।"),
    "hook": "एक पैर: पाँच नख, हर अंगुली में तीन, कुल पन्द्रह।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 102, how many bones are in each toe of the lower limb?",
            ("Three", "प्रत्येकमङ्गुल्यां त्रीण्यस्थीनि: in each toe three bones."),
            [("Two", "The line says three (त्रीणि), not two."),
             ("Four", "The line says three (त्रीणि), not four."),
             ("Seven", "The line says three (त्रीणि), not seven.")],
            "In each toe there are three bones.",
            "प्रत्येकम् अङ्गुल्याम् त्रीणि अस्थीनि."),
        order(1, "Put the printed parts of unit 102 in the line's order.",
              ["तत्रैकै कस्मिन सक्थिनि", "पंच पादनखाः", "प्रत्येकमंगुल्यां", "त्रीण्यस्थीनि", "तानि पंचदश"],
              "In each lower limb, five foot-nails; in each toe, three bones; those are fifteen.",
              "सक्थिनि → पादनखाः → अङ्गुल्याम् → त्रीण्यस्थीनि → पञ्चदश."),
        match(2, "Match each word of unit 102 to its meaning.",
              [["सक्थि", "lower limb"], ["पादनख", "foot-nail"], ["प्रत्येकम्", "in each"], ["अङ्गुली", "toe (here)"],
               ["अस्थि", "bone"]],
              "In each lower limb: five foot-nails, and three bones in each toe.",
              "सक्थि, पादनख, प्रत्येकम्, अङ्गुली, अस्थि.", role="extend",
              teaches="सक्थि = thigh or the whole leg; here the lower limb whose bones are counted."),
        mcq("discriminate", 3, "Which split of त्रीण्यस्थीनि in unit 102 is right?",
            ("त्रीणि + अस्थीनि", "इ before an unlike vowel becomes य्: त्रीणि + अस्थीनि → त्रीण्यस्थीनि."),
            [("त्रीण् + यस्थीनि", "यस्थीनि is not a word; the word is अस्थीनि (bones)."),
             ("त्रीण्य + अस्थीनि", "त्रीण्य is not a word; the number is त्रीणि (three)."),
             ("त्रीणे + अस्थीनि", "ए + अ would give त्रीणेऽस्थीनि, not त्रीण्यस्थीनि.")],
            "त्रीणि (three) + अस्थीनि (bones): इ + अ → य.",
            "इ + unlike vowel → य् + that vowel."),
        multi("apply", 4, "A student counts one lower limb by unit 102. Which items does the line give?",
              [("Five foot-nails", "Right: पञ्च पादनखाः."),
               ("Four bones in each toe", "The line says three in each toe, not four."),
               ("Three bones in each toe", "Right: प्रत्येकमङ्गुल्यां त्रीण्यस्थीनि."),
               ("Ten foot-nails in each limb", "The line says five foot-nails, not ten.")],
              [0, 2],
              "Five foot-nails, and three bones in each toe.",
              "पञ्च पादनखाः; प्रत्येकमङ्गुल्यां त्रीण्यस्थीनि."),
        mcq("transfer", 5, "By the rule of त्रीणि + अस्थीनि, how is इति + अपि (thus also) written when joined?",
            ("इत्यपि", "इ before अ becomes य्, as त्रीणि + अस्थीनि → त्रीण्यस्थीनि."),
            [("इतेपि", "ए comes from अ + इ, not from इ + अ."),
             ("इतीपि", "ई comes from इ + इ, not from इ + अ."),
             ("इत्यापि", "या would come from इ + आ, but the second word has a short अ.")],
            "इति + अपि = इत्यपि, like त्रीणि + अस्थीनि = त्रीण्यस्थीनि.",
            "इ + अ → य.",
            teaches="इ before an unlike vowel becomes य्: त्रीणि + अस्थीनि → त्रीण्यस्थीनि."),
    ],
}

# ---------------------------------------------------------------- unit 103
AUTHORED["103"] = {
    "title": "पंचपादशलाकाः तत्प्रतिबंधकमेकं",
    "question": "By unit 103, which further bones of the lower limb are counted after the toes?",
    "rule": ("Five foot-rods (पादशलाका), one binder (प्रतिबन्धक) of them, two each in the kūrca, the ankle (गुल्फ) and the "
             "shank (जङ्घा); then one each in further places (last word doubtful)."),
    "limits": ("Low confidence. The last word is printed पाणि (hand); 'heel' (पार्ष्णि) is a conjecture: no question on the last "
               "word. Kūrca is kept untranslated (sense uncertain). That 'their' (तत्-) means the rods is the data's reading."),
    "explain_hi": ("यह गद्य-पंक्ति इकाई १०२ की निचले अंग वाली गिनती को आगे बढ़ाती है। "
                   "पाँच पादशलाकाएँ (पैर की शलाका, यानी छड़ जैसी अस्थियाँ) हैं, और उनका एक प्रतिबन्धक (बाँधने वाला)। "
                   "फिर कूर्च, गुल्फ (टखना) और जङ्घा (घुटने से नीचे का भाग) में दो-दो अस्थियाँ। "
                   "अन्तिम शब्द छपाई में ‘पाणि’ (हाथ) है, जो पैर की सूची में नहीं बैठता; अनुमानित पाठ ‘पार्ष्णि’ (एड़ी) है, और उसके साथ जानु व ऊरु में एक-एक। "
                   "कूर्च का अर्थ अनिश्चित है, इसलिए उसका अनुवाद नहीं किया गया।"),
    "hook": "पाँच शलाका, एक बन्धक, फिर दो-दो।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 103, how many pādaśalākās (foot-rods) are counted in a lower limb?",
            ("Five", "पञ्च पादशलाकाः: five foot-rods."),
            [("Three", "The line says five (पञ्च), not three."),
             ("Ten", "The line says five (पञ्च), not ten."),
             ("Eight", "The line says five (पञ्च), not eight.")],
            "Five foot-rods are counted.",
            "पञ्च पादशलाकाः."),
        order(1, "Put these parts of unit 103 in the line's order.",
              ["पंचपादशलाकाः", "तत्प्रतिबंधकमेकं", "द्वे द्वे", "कूर्च्चगुल्फजंघासु", "एकैकं पाणिर्जानूरुषु"],
              "Five foot-rods; one binder of them; two each in the kūrca, ankle and shank; one each in the last places.",
              "पादशलाकाः → प्रतिबन्धकम् → द्वे द्वे → कूर्चगुल्फजङ्घासु → एकैकम्."),
        match(2, "Match each word of unit 103 to its meaning.",
              [["शलाका", "rod, splint"], ["प्रतिबन्धक", "binder"], ["गुल्फ", "ankle"], ["जङ्घा", "shank"],
               ["द्वे द्वे", "two each"]],
              "Five rods, one binder, and two each in the kūrca, ankle and shank.",
              "शलाका, प्रतिबन्धक, गुल्फ, जङ्घा, द्वे द्वे.", role="extend",
              teaches="पादशलाका = foot-rod: शलाका is a rod or splint, so the rod-like bones of the foot."),
        mcq("discriminate", 3, "Which split of जंघास्वेकैकं in unit 103 is right?",
            ("जङ्घासु + एकैकम्", "उ before an unlike vowel becomes व्: जङ्घासु + एकैकम् → जङ्घास्वेकैकम्."),
            [("जङ्घा + स्वेकैकम्", "स्वेकैकम् is not a word; the place word ends in -सु (in)."),
             ("जङ्घासो + एकैकम्", "ओ + ए would give अव्: जङ्घासवेकैकम्, not स्वे."),
             ("जङ्घास्व + एकैकम्", "जङ्घास्व is not a form; the locative plural is जङ्घासु.")],
            "जङ्घासु (in the shanks, in a list) + एकैकम् (one each): उ + ए → वे.",
            "उ + unlike vowel → व् + that vowel."),
        multi("apply", 4, "Which statements fit unit 103 as the card reads it?",
              [("It counts ten foot-rods", "The line says five foot-rods (पञ्च)."),
               ("It counts one binder (प्रतिबन्धक)", "Right: तत्प्रतिबन्धकम् एकम्."),
               ("It gives two each in the kūrca, ankle and shank", "Right: द्वे द्वे कूर्चगुल्फजङ्घासु."),
               ("It gives three each in the ankle and shank", "The line says two each (द्वे द्वे), not three.")],
              [1, 2],
              "Five rods, one binder, two each in the kūrca, ankle and shank.",
              "पञ्च पादशलाकाः, एकं प्रतिबन्धकम्, द्वे द्वे कूर्चगुल्फजङ्घासु."),
        mcq("transfer", 5, "By the rule of जङ्घासु + एकैकम्, how is वस्तु + एव (the thing itself) written when joined?",
            ("वस्त्वेव", "उ before ए becomes व्, as जङ्घासु + एकैकम् → जङ्घास्वेकैकम्."),
            [("वस्तेव", "ए alone would come from अ + इ or अ + ए, not from उ + ए."),
             ("वस्तवेव", "अव् comes from ओ before a vowel, not from उ."),
             ("वस्तोव", "ओ comes from अ + उ, not from उ + ए.")],
            "वस्तु + एव = वस्त्वेव, like जङ्घासु + एकैकम् = जङ्घास्वेकैकम्.",
            "उ + ए → वे.",
            teaches="उ before an unlike vowel becomes व्: जङ्घासु + एकैकम् → जङ्घास्वेकैकम्."),
    ],
}

# ---------------------------------------------------------------- unit 104
AUTHORED["104"] = {
    "title": "सर्वाणिच नखास्थ्यादीनि सक्थिवद्वाह्वोश्च",
    "question": "By unit 104, how are the bones of the two arms counted?",
    "rule": ("All the bones beginning with the nails (नखास्थ्यादीनि) are, as in the lower limb (सक्थिवत्), also in the two "
             "arms (बाह्वोः): the arm count is not given anew but follows the leg."),
    "limits": ("Prose, elliptical: the verb 'are' is understood. No new numbers are given. The print has वाह्वोः for बाह्वोः "
               "(v/b, normalised). 'Beginning with the nail(-bone)s' is the data's reading of नखास्थ्यादीनि."),
    "explain_hi": ("यह छोटी गद्य-पंक्ति कहती है कि नख-अस्थि आदि सभी अस्थियाँ, सक्थि के समान, दोनों बाहुओं में भी हैं। "
                   "यानी हाथों की गिनती अलग से नहीं दी गई; इकाई १०२-१०३ की पैर वाली गिनती ही बाहुओं पर लागू होती है। "
                   "‘सक्थिवत्’ में -वत् का अर्थ है ‘के समान’। "
                   "छपाई में ‘वाह्वोः’ है, जिसे ‘बाह्वोः’ (दोनों बाहुओं में) पढ़ा गया; छपाई में व/ब का अदल-बदल आम है। "
                   "क्रिया ‘हैं’ समझी जाती है, लिखी नहीं गई।"),
    "hook": "जैसा पैर, वैसी बाँह।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 104, where is the bone count of the lower limb repeated?",
            ("In the two arms", "सक्थिवद्बाह्वोश्च: as in the lower limb, also in the two arms."),
            [("In the head and neck", "The line names the arms (बाह्वोः), not the head or neck."),
             ("In the back", "The line names the arms (बाह्वोः), not the back."),
             ("In the chest", "The line names the arms (बाह्वोः), not the chest.")],
            "The leg's count holds for the two arms as well.",
            "सक्थिवत् बाह्वोः च."),
        order(1, "Put the words of unit 104 in the line's order.",
              ["सर्वाणि च", "नखास्थ्यादीनि", "सक्थिवत्", "बाह्वोः च"],
              "And all, beginning with the nail-bones, as in the lower limb, also in the two arms.",
              "सर्वाणि च → नखास्थ्यादीनि → सक्थिवत् → बाह्वोः च."),
        match(2, "Match each word of unit 104 to its meaning.",
              [["सर्वाणि", "all"], ["नख", "nail"], ["आदि", "beginning with"], ["-वत्", "like, as in"],
               ["बाहु", "arm"]],
              "All, beginning with the nails, as in the lower limb, in the two arms.",
              "सर्वाणि, नख, आदि, -वत्, बाहु.", role="extend",
              teaches="-वत् after a noun means 'like, as in': सक्थिवत् = as in the lower limb."),
        mcq("discriminate", 3, "Which split of नखास्थ्यादीनि in unit 104 is right?",
            ("नख + अस्थि + आदीनि", "अ + अ → आ (नखास्थि), then इ before आ → य् (अस्थ्यादीनि)."),
            [("नखा + स्थि + आदीनि", "नखा and स्थि are not the words; they are नख and अस्थि."),
             ("नख + आस्थि + आदीनि", "आस्थि is not the word for bone; the word is अस्थि."),
             ("नख + अस्थ्य + आदीनि", "अस्थ्य is not a word; the य् comes from the इ of अस्थि.")],
            "नख (nail) + अस्थि (bone) + आदीनि (beginning with): अ + अ → आ; इ + आ → या.",
            "अ + अ → आ; इ + unlike vowel → य्."),
        mcq("apply", 4, "A student has the bone count of one lower limb. By unit 104, what follows for each arm?",
            ("The same items as in the lower limb", "सक्थिवत्: as in the lower limb, so the arm repeats the leg's count."),
            [("Half the items of the lower limb", "Nothing is halved; the arms follow the leg (सक्थिवत्)."),
             ("No bones at all are counted there", "The line counts them by the leg's pattern, it does not drop them."),
             ("Twice the items of the lower limb", "Nothing is doubled; the arms follow the leg (सक्थिवत्).")],
            "Each arm has the same count as the lower limb.",
            "सक्थिवत् = as in the lower limb."),
        mcq("transfer", 5, "By the pattern of सक्थिवत् (as in the lower limb), what does पितृवत् mean in a new example?",
            ("Like a father", "-वत् after a noun means 'like': पितृ (father) + वत् = like a father."),
            [("From the father", "From would be an ablative ending, not -वत्."),
             ("For the father", "For would be a dative ending, not -वत्."),
             ("Without a father", "Nothing in -वत् means without.")],
            "पितृवत् = like a father, as सक्थिवत् = as in the lower limb.",
            "Noun + -वत् = like that noun.",
            teaches="-वत् makes 'like, as in': सक्थिवत् = as in the lower limb."),
    ],
}

# ---------------------------------------------------------------- unit 105
AUTHORED["105"] = {
    "title": "चतुर्विंशतिः पर्शुकाः",
    "question": "By unit 105, how many parśukās (ribs) are counted?",
    "rule": ("Twenty-four (चतुर्विंशतिः) ribs (पर्शुकाः). The number word is feminine singular; the counted noun stands "
             "in the plural beside it."),
    "limits": ("Prose, two words; no verb is printed (the copula is understood). The line does not say whether the 24 are "
               "per side or in all: no question on that."),
    "explain_hi": ("यह दो शब्दों की गद्य-पंक्ति है: चौबीस पर्शुकाएँ, यानी पसलियाँ। "
                   "‘चतुर्विंशति’ = चतुर् (चार) + विंशति (बीस)। "
                   "संख्या-शब्द ‘चतुर्विंशतिः’ स्त्रीलिंग एकवचन है, जबकि गिनी गई वस्तु ‘पर्शुकाः’ बहुवचन में है। "
                   "पंक्ति यह नहीं बताती कि चौबीस एक ओर की हैं या कुल। "
                   "क्रिया ‘हैं’ समझी जाती है।"),
    "hook": "चौबीस पसलियाँ: चार और बीस।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 105, how many parśukās (ribs) are counted?",
            ("Twenty-four", "चतुर्विंशतिः पर्शुकाः: twenty-four ribs."),
            [("Twelve", "The line says twenty-four, not twelve."),
             ("Eighteen", "The line says twenty-four, not eighteen."),
             ("Twenty-eight", "The line says twenty-four, not twenty-eight.")],
            "Twenty-four ribs.",
            "चतुर्विंशतिः = twenty-four."),
        match(1, "Match each part of unit 105 to its meaning.",
              [["चतुर्", "four"], ["विंशति", "twenty"], ["चतुर्विंशति", "twenty-four"], ["पर्शुका", "rib"]],
              "चतुर् + विंशति = twenty-four; पर्शुका = rib.",
              "चतुर्, विंशति, चतुर्विंशति, पर्शुका."),
        fill(2, "In unit 105 the ribs are called ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("पर्शुकाः", "parśukāḥ", "पर्शुका"),
             "पर्शुकाः = ribs; twenty-four are counted.",
             "पर्शुका = rib (standard).",
             "चतुर्विंशतिः पर्शुकाः."),
        mcq("discriminate", 3, "Which statement about unit 105 is right?",
            ("It gives 24 ribs, not saying per side or in all", "The note: per side or in all is not said."),
            [("It gives 12 ribs, counted on each side", "The number is 24, and no side is named."),
             ("It gives 24 ribs, counted on each side", "The line does not say 'on each side'."),
             ("It gives 48 ribs, counted as 24 on each of two sides", "The number is 24, and no side is named.")],
            "Twenty-four ribs; the line leaves per side or in all open.",
            "चतुर्विंशतिः पर्शुकाः: no side is named."),
        mcq("apply", 4, "Why is पर्शुकाः plural while चतुर्विंशतिः is singular in unit 105?",
            ("विंशति is a feminine number noun, used in the singular", "The data: चतुर्विंशतिः is f. nom. sg.; the counted noun is plural."),
            [("चतुर्विंशतिः is a dual form of the number", "The data labels it nom. sg., not dual."),
             ("पर्शुकाः is a genitive form, 'of the rib'", "The genitive sg. of पर्शुका is पर्शुकायाः; पर्शुकाः is nom. pl."),
             ("The print has lost a plural ending on the number word here", "No print error is noted; the singular is regular.")],
            "Numbers like विंशति are feminine singular nouns; the counted noun stays plural beside them.",
            "विंशति etc. = f. sg. number noun + plural noun."),
        mcq("transfer", 5, "By the pattern of चतुर्विंशतिः पर्शुकाः, which new phrase means twenty horses?",
            ("विंशतिरश्वाः", "Singular number noun + plural noun; इः before अ becomes इर्."),
            [("विंशतिरश्वः", "अश्वः is singular; the counted noun stands in the plural."),
             ("विंशतयोऽश्वाः", "विंशतयः is the plural of the number, 'twenties', not twenty."),
             ("विंशतेरश्वाः", "विंशतेः is genitive/ablative, 'of twenty', not the number itself.")],
            "विंशतिः + अश्वाः = विंशतिरश्वाः: twenty horses.",
            "f. sg. number + plural noun; इः + vowel → इर्.",
            teaches="चतुर्विंशतिः पर्शुकाः: the number word is singular, the counted noun plural."),
    ],
}

# ---------------------------------------------------------------- unit 106
AUTHORED["106"] = {
    "title": "तावंत्येव तत्स्थालकान्यर्बुदानि च",
    "question": "By unit 106, what is said to be as many as the ribs?",
    "rule": ("Just as many (तावन्ति एव) as the ribs of unit 105 are their (तत्-) sthālakas and arbudas: the count is "
             "given by reference, not by a numeral."),
    "limits": ("Prose; the copula is understood. Sthālaka (literally small dish) and arbuda (literally lump) are not firmly "
               "identified: no question on what they are. Whether 'as many' counts each or both together is not said."),
    "explain_hi": ("यह गद्य-पंक्ति पिछली इकाई की पसलियों से जुड़ी है: ‘तावन्त्येव’, उतने ही। "
                   "उनके (तत्-, यानी पसलियों के) स्थालक और अर्बुद उतने ही हैं जितनी पसलियाँ। "
                   "स्थालक का शब्दार्थ छोटी थाली और अर्बुद का उभार या गाँठ है; आधुनिक शरीर-रचना में इनकी पक्की पहचान नहीं दी गई। "
                   "अर्बुद अन्यत्र ‘ट्यूमर’ भी होता है, पर यहाँ शब्दार्थ ‘उभार’ रखा गया है। "
                   "कोई संख्या दोबारा नहीं लिखी गई।"),
    "hook": "जितनी पसलियाँ, उतने स्थालक, उतने अर्बुद।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 106, how does the number of sthālakas and arbudas compare with the ribs?",
            ("As many as the ribs", "तावन्त्येव: just as many, referring to the ribs of unit 105."),
            [("Twice as many as the ribs", "तावन्ति means as many, not twice as many."),
             ("Half as many as the ribs", "तावन्ति means as many, not half as many."),
             ("One more than the ribs", "तावन्ति means as many; nothing is added.")],
            "They are as many as the ribs.",
            "तावन्ति एव = just as many."),
        order(1, "Put the words of unit 106 in the line's order.",
              ["तावन्ति", "एव", "तत्स्थालकानि", "अर्बुदानि", "च"],
              "Just as many are their sthālakas and arbudas.",
              "तावन्ति → एव → तत्स्थालकानि → अर्बुदानि → च."),
        match(2, "Match each small word of unit 106 to its meaning.",
              [["तावन्ति", "as many"], ["एव", "just"], ["तत्-", "their"], ["च", "and"]],
              "Just as many are their sthālakas and arbudas.",
              "तावन्ति, एव, तत्-, च.", role="extend",
              teaches="तावन्ति = as many: it repeats an earlier number without writing it again."),
        mcq("discriminate", 3, "Which split of तावंत्येव in unit 106 is right?",
            ("तावन्ति + एव", "इ before ए becomes य्: तावन्ति + एव → तावन्त्येव."),
            [("तावन्त्य + एव", "तावन्त्य is not a form; the word is तावन्ति."),
             ("तावन्ते + एव", "ए + ए would give तावन्त एव, not त्येव."),
             ("तावन् + त्येव", "त्येव is not a word; the words are तावन्ति and एव.")],
            "तावन्ति (as many) + एव (just): इ + ए → ये.",
            "इ + unlike vowel → य् + that vowel."),
        multi("apply", 4, "Which statements fit unit 106?",
              [("Its count is given by reference, not by a numeral", "Right: तावन्ति, as many, with no number written."),
               ("It gives a new number for the sthālakas", "No number is written; the count is 'as many'."),
               ("It repeats the word पर्शुका from unit 105", "पर्शुका is not repeated; तत्- (their) points back."),
               ("Its तत्- (their) points back to the ribs", "Right: the note says तत्- refers to the ribs of unit 105.")],
              [0, 3],
              "The count is 'as many as the ribs', and तत्- points to the ribs.",
              "तावन्त्येव तत्स्थालकानि."),
        mcq("transfer", 5, "By the rule of तावन्ति + एव, how is अस्ति + एव (is indeed) written when joined?",
            ("अस्त्येव", "इ before ए becomes य्, as तावन्ति + एव → तावन्त्येव."),
            [("अस्तेव", "ए alone would come from अ + इ or अ + ए, not from इ + ए."),
             ("अस्तीव", "ई comes from इ + इ, not from इ + ए."),
             ("अस्तयेव", "अय् comes from ए before a vowel; अस्ति ends in इ.")],
            "अस्ति + एव = अस्त्येव, like तावन्ति + एव = तावन्त्येव.",
            "इ + ए → ये.",
            teaches="इ before an unlike vowel becomes य्: तावन्ति + एव → तावन्त्येव."),
    ],
}

# ---------------------------------------------------------------- unit 107
AUTHORED["107"] = {
    "title": "त्रिंशत् पृष्ठे",
    "question": "By unit 107, what number is given for the back?",
    "rule": ("Thirty (त्रिंशत्) in the back (पृष्ठे, locative 'in'). The line appears to continue the bone count of units "
             "100-106, but the counted noun is not printed."),
    "limits": ("Prose, two words; no verb and no counted noun are printed. That bones are meant is a grouping inference from "
               "the units before; the card does not supply the noun."),
    "explain_hi": ("यह दो शब्दों की गद्य-पंक्ति है: तीस, पीठ में। "
                   "‘पृष्ठे’ पृष्ठ (पीठ) का सप्तमी एकवचन है: पीठ में। "
                   "पंक्ति सम्भवतः इकाई १००-१०६ की अस्थि-गिनती को आगे बढ़ाती है, पर ‘अस्थियाँ’ शब्द यहाँ छपा नहीं। "
                   "क्रिया भी नहीं लिखी; ‘हैं’ समझा जाता है।"),
    "hook": "पीठ में तीस।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 107, what number is given for the back?",
            ("Thirty", "त्रिंशत् पृष्ठे: thirty in the back."),
            [("Eight", "त्रिंशत् is thirty, not eight."),
             ("Thirteen", "त्रिंशत् is thirty, not thirteen."),
             ("Twenty-four", "त्रिंशत् is thirty, not twenty-four.")],
            "Thirty in the back.",
            "त्रिंशत् = thirty; पृष्ठे = in the back."),
        match(1, "Match each part of unit 107 to its meaning.",
              [["त्रिंशत्", "thirty"], ["पृष्ठ", "back"], ["पृष्ठे", "in the back"]],
              "त्रिंशत् पृष्ठे = thirty in the back.",
              "त्रिंशत्, पृष्ठ, पृष्ठे."),
        fill(2, "In unit 107 the number 'thirty' is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("त्रिंशत्", "triṃśat", "त्रिंशद्"),
             "त्रिंशत् = thirty; पृष्ठे = in the back.",
             "त्रिंशत् = thirty.",
             "त्रिंशत् पृष्ठे."),
        mcq("discriminate", 3, "What does unit 107 leave unprinted?",
            ("What is being counted", "The note: the counted thing (bones) is not stated in the line."),
            [("How many there are", "The number is printed: त्रिंशत्, thirty."),
             ("Where they are found", "The place is printed: पृष्ठे, in the back."),
             ("Nothing; it names bones", "No word for bones is printed in the line.")],
            "The number and the place are printed; the counted noun is not.",
            "त्रिंशत् पृष्ठे: number + place, no noun."),
        mcq("apply", 4, "If त्रिंशत् stood before अस्थीनि (bones) in a new phrase, how would the two be joined?",
            ("त्रिंशदस्थीनि", "त् before a vowel becomes द्."),
            [("त्रिंशतस्थीनि", "Before a vowel the final त् becomes द्; it does not stay त्."),
             ("त्रिंशन्नस्थीनि", "न् would come before a nasal, not before a vowel."),
             ("त्रिंशच्चस्थीनि", "च्च comes from त् before च, not before a vowel.")],
            "त्रिंशत् + अस्थीनि = त्रिंशदस्थीनि.",
            "त् + vowel → द्."),
        mcq("transfer", 5, "By the pattern of पृष्ठे (in the back, from पृष्ठ), how is in the house said from गृह?",
            ("गृहे", "An अ-stem takes -ए for 'in': पृष्ठ → पृष्ठे, गृह → गृहे."),
            [("गृहम्", "गृहम् is the nominative/accusative, not 'in the house'."),
             ("गृहेण", "गृहेण is the instrumental, 'by the house'."),
             ("गृहात्", "गृहात् is the ablative, 'from the house'.")],
            "गृहे = in the house, like पृष्ठे = in the back.",
            "अ-stem + -ए = locative singular, 'in'.",
            teaches="पृष्ठे is the locative singular of पृष्ठ: -ए on an अ-stem means 'in'."),
    ],
}

# ---------------------------------------------------------------- unit 108
AUTHORED["108"] = {
    "title": "अष्टावुरसि",
    "question": "By unit 108, what number is given for the chest?",
    "rule": ("Eight (अष्टौ) in the chest (उरसि). Printed as one word: अष्टौ before a vowel becomes अष्टाव् (औ → आव्)."),
    "limits": ("Prose, one printed word; no verb and no counted noun are printed. That bones are meant is a grouping "
               "inference from the units before. Per side or in all is not said."),
    "explain_hi": ("यह एक छपे शब्द की गद्य-पंक्ति है: आठ, छाती में। "
                   "‘अष्टावुरसि’ = अष्टौ (आठ) + उरसि (छाती में); स्वर से पहले औ का आव् हुआ है। "
                   "‘उरसि’ उरस् (छाती) का सप्तमी एकवचन है। "
                   "गिनी गई वस्तु (सम्भवतः अस्थियाँ) और क्रिया छपी नहीं; पिछली इकाइयों की गिनती से जोड़ा गया है।"),
    "hook": "छाती में आठ: अष्टौ उरसि।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 108, what number is given for the chest?",
            ("Eight", "अष्टावुरसि: eight in the chest."),
            [("Thirty", "अष्टौ is eight, not thirty."),
             ("Six", "अष्टौ is eight, not six."),
             ("Thirteen", "अष्टौ is eight, not thirteen.")],
            "Eight in the chest.",
            "अष्टौ = eight; उरसि = in the chest."),
        match(1, "Match each part of unit 108 to its meaning.",
              [["अष्टौ", "eight"], ["उरस्", "chest"], ["उरसि", "in the chest"], ["अष्टावुरसि", "eight in the chest"]],
              "अष्टौ + उरसि = अष्टावुरसि: eight in the chest.",
              "अष्टौ, उरस्, उरसि, अष्टावुरसि."),
        fill(2, "In unit 108 'in the chest' is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("उरसि", "urasi"),
             "उरसि = in the chest, the locative singular of उरस्.",
             "उरसि = in the chest.",
             "अष्टौ + उरसि → अष्टावुरसि."),
        mcq("discriminate", 3, "Why is अष्टौ printed अष्टाव् before उरसि in unit 108?",
            ("औ before a vowel becomes आव्", "अष्टौ + उरसि → अष्टावुरसि."),
            [("औ before a vowel becomes ओ", "ओ does not come from औ; औ before a vowel gives आव्."),
             ("A visarga of अष्टः becomes व्", "अष्टौ has no visarga; the व् comes from its औ."),
             ("अष्टाव is the plain word for eight", "The word is अष्टौ; अष्टाव् is its form before a vowel.")],
            "अष्टौ (eight) + उरसि (in the chest): औ + उ → आवु.",
            "औ + vowel → आव् + that vowel."),
        multi("apply", 4, "Which statements fit unit 108?",
              [("It names the bones it counts", "No word for bones is printed in the line."),
               ("It says eight on each side", "The line does not say per side or in all."),
               ("It joins two words in one printed word", "Right: अष्टौ + उरसि → अष्टावुरसि."),
               ("Its verb 'are' is understood, not printed", "Right: no verb is printed.")],
              [2, 3],
              "One printed word of two; the verb and the counted noun are not printed.",
              "अष्टावुरसि = अष्टौ उरसि."),
        mcq("transfer", 5, "By the rule of अष्टावुरसि, how is तौ + इति (those two, thus) written when joined?",
            ("ताविति", "औ before a vowel becomes आव्, as अष्टौ + उरसि → अष्टावुरसि."),
            [("तविति", "अव् comes from ओ before a vowel, not from औ."),
             ("तायिति", "आय् comes from ऐ before a vowel, not from औ."),
             ("तौति", "औ before a vowel does not swallow the vowel; it becomes आव्.")],
            "तौ + इति = ताविति, like अष्टौ + उरसि = अष्टावुरसि.",
            "औ + vowel → आव्.",
            teaches="औ before a vowel becomes आव्: अष्टौ + उरसि → अष्टावुरसि."),
    ],
}

# ---------------------------------------------------------------- unit 109
AUTHORED["109"] = {
    "title": "एकैकं भगे त्रिके",
    "question": "By unit 109, what is given for the bhaga and the trika?",
    "rule": ("One each (एकैकम्) in the bhaga (probably the pubic region) and in the trika (probably the sacral region). "
             "एकैकम् = एक + एकम् (अ + ए → ऐ)."),
    "limits": ("Prose; no verb and no counted noun are printed (bones by grouping). Bhaga usually means the female genitals; "
               "as a place for a bone, the pubic region is probable only. Trika = sacral region, probable."),
    "explain_hi": ("यह गद्य-पंक्ति कहती है: एक-एक, भग में और त्रिक में। "
                   "भग का सामान्य अर्थ स्त्री-जननांग है; अस्थि के स्थान के रूप में इसे सम्भवतः जघन-क्षेत्र पढ़ा गया है। "
                   "त्रिक सम्भवतः त्रिकास्थि (कमर के नीचे का) क्षेत्र है। "
                   "‘एकैकम्’ = एक + एकम्, अ + ए → ऐ। "
                   "गिनी गई वस्तु और क्रिया छपी नहीं; अस्थि-गिनती से जोड़ा गया है।"),
    "hook": "भग में एक, त्रिक में एक।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 109, how many are given in the bhaga and in the trika?",
            ("One each", "एकैकं भगे त्रिके: one each in the bhaga and the trika."),
            [("Two each", "एकैकम् means one each, not two each."),
             ("Three each", "एकैकम् means one each, not three each."),
             ("Eight in all", "एकैकम् means one each; eight is not named here.")],
            "One each in the two places.",
            "एकैकम् = one each."),
        order(1, "Put the words of unit 109 in the line's order.",
              ["एकैकम्", "भगे", "त्रिके"],
              "One each, in the bhaga, in the trika.",
              "एकैकम् → भगे → त्रिके."),
        match(2, "Match each word of unit 109 to its meaning.",
              [["एकैकम्", "one each"], ["भगे", "in the bhaga (probably pubic region)"],
               ["त्रिके", "in the trika (probably sacral region)"]],
              "One each in the bhaga and in the trika.",
              "एकैकम्, भगे, त्रिके.", role="extend",
              teaches="एकैकम् = one each: the number one repeated, one for every place named."),
        mcq("discriminate", 3, "Which split of एकैकं in unit 109 is right?",
            ("एक + एकम्", "अ + ए → ऐ: एक + एकम् → एकैकम्."),
            [("एकै + कम्", "एकै and कम् are not the words; the words are एक and एकम्."),
             ("ऐक + एकम्", "The first word is एक, not ऐक."),
             ("एके + एकम्", "ए + ए would give एक एकम्, not एकैकम्.")],
            "एक + एकम् = एकैकम्: अ + ए → ऐ.",
            "अ + ए → ऐ."),
        mcq("apply", 4, "भगे and त्रिके share the ending -ए. What does it mean in unit 109?",
            ("In (locative singular)", "The data: both are loc. sg., 'in the bhaga, in the trika'."),
            [("By (instrumental singular)", "The instrumental of an अ-stem ends in -एन, not -ए."),
             ("From (ablative singular)", "The ablative of an अ-stem ends in -आत्, not -ए."),
             ("Of (genitive singular)", "The genitive of an अ-stem ends in -अस्य, not -ए.")],
            "-ए here is the locative: in the bhaga, in the trika.",
            "अ-stem + -ए = locative singular, 'in'."),
        mcq("transfer", 5, "By the rule of एक + एकम्, how is न + एव (not at all) written when joined?",
            ("नैव", "अ + ए → ऐ, as एक + एकम् → एकैकम्."),
            [("नेव", "ए comes from अ + इ; अ + ए gives ऐ."),
             ("नोव", "ओ comes from अ + उ, not from अ + ए."),
             ("नयेव", "य् comes from इ before a vowel; न ends in अ.")],
            "न + एव = नैव, like एक + एकम् = एकैकम्.",
            "अ + ए → ऐ.",
            teaches="Short अ before ए joins as ऐ: एक + एकम् → एकैकम्."),
    ],
}

# ---------------------------------------------------------------- unit 110
AUTHORED["110"] = {
    "title": "नितंबयोश्च द्वे",
    "question": "By unit 110, what number is given for the two nitambas (hips)?",
    "rule": ("And two (द्वे) in the two nitambas (नितम्बयोः, locative dual). Before च the visarga becomes श्: "
             "नितम्बयोः + च → नितम्बयोश्च."),
    "limits": ("Prose; no verb and no counted noun are printed (bones by grouping). Whether 'two' is the total or per side is "
               "not stated: no question rests on it."),
    "explain_hi": ("यह गद्य-पंक्ति कहती है: और दोनों नितम्बों में दो। "
                   "‘नितम्बयोः’ नितम्ब (कूल्हा, नितम्ब; मानक) का सप्तमी द्विवचन है: दोनों नितम्बों में। "
                   "च से पहले विसर्ग श् बना है: नितम्बयोश्च। "
                   "‘दो’ कुल हैं या हर ओर, यह पंक्ति नहीं बताती। "
                   "गिनी गई वस्तु और क्रिया छपी नहीं।"),
    "hook": "दोनों नितम्बों में दो।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 110, what number is given for the nitambas (hips)?",
            ("Two", "नितम्बयोश्च द्वे: and two in the two hips."),
            [("Eight", "द्वे is two, not eight."),
             ("Five", "द्वे is two, not five."),
             ("Three", "द्वे is two, not three.")],
            "Two in the hips.",
            "द्वे = two."),
        match(1, "Match each part of unit 110 to its meaning.",
              [["नितम्ब", "hip, buttock"], ["नितम्बयोः", "in the two hips"], ["च", "and"], ["द्वे", "two"]],
              "And two in the two hips.",
              "नितम्ब, नितम्बयोः, च, द्वे."),
        fill(2, "In unit 110 the number 'two' is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("द्वे", "dve"),
             "द्वे = two (neuter/feminine dual).",
             "द्वे = two.",
             "नितम्बयोश्च द्वे."),
        mcq("discriminate", 3, "Which split of नितंबयोश्च in unit 110 is right?",
            ("नितम्बयोः + च", "A visarga before च becomes श्."),
            [("नितम्बयो + श्च", "श्च is not a word; the word is च (and)."),
             ("नितम्बयोस् + च", "स् before च would itself become श्; the form is नितम्बयोः."),
             ("नितम्ब + योश्च", "योश्च is not a word; -योः is the dual ending.")],
            "नितम्बयोः (in the two hips) + च (and): ः before च → श्.",
            "Visarga before च → श्."),
        mcq("apply", 4, "What does unit 110 leave open about its 'two'?",
            ("Whether it is the total or per side", "The note: total or per side is not stated."),
            [("Whether the place is the hips", "The place is printed: नितम्बयोः, in the two hips."),
             ("Whether the number is really two", "The number is printed: द्वे, two."),
             ("Whether च (and) joins it to the list of the units before", "च (and) is printed and adds it to the count.")],
            "Total or per side is not stated.",
            "नितम्बयोश्च द्वे: side not stated."),
        mcq("transfer", 5, "By the pattern of नितम्बयोः (in the two hips), how is in the two hands said from हस्त?",
            ("हस्तयोः", "An अ-stem takes -योः for the locative dual, as नितम्ब → नितम्बयोः."),
            [("हस्तेषु", "-एषु is the locative plural, in three or more."),
             ("हस्ते", "Here -ए would be 'in the hand', singular."),
             ("हस्तैः", "-ऐः is the instrumental plural, 'by the hands'.")],
            "हस्तयोः = in the two hands, like नितम्बयोः = in the two hips.",
            "अ-stem + -योः = locative dual.",
            teaches="नितम्बयोः is a locative dual: -योः on an अ-stem means 'in the two'."),
    ],
}

# ---------------------------------------------------------------- unit 111
AUTHORED["111"] = {
    "title": "तद्वदक्षकंसांसफलकेषु",
    "question": "By unit 111, how is the number given for the shoulder region?",
    "rule": ("तद्वत् (likewise) carries the number of unit 110 forward without writing it; the places stand in the "
             "locative plural (-एषु) and end with अंसफलक, the shoulder-blade (standard)."),
    "limits": ("Low confidence: the compound's division is uncertain (अक्षक + अंस + अंसफलक, or अक्ष-कंस); akṣaka = collarbone "
               "is probable on a conjecture. No question on akṣaka, aṃsa as a separate item, or the division."),
    "explain_hi": ("यह एक लम्बे समास वाली गद्य-पंक्ति है: ‘तद्वत्’, उसी प्रकार, यानी इकाई ११० जितनी संख्या, जो दोबारा नहीं लिखी गई। "
                   "अनुमानित पाठ पर स्थान हैं: अक्षक (सम्भवतः हँसली), अंस (कन्धा) और अंसफलक (कन्धे की चपटी हड्डी, मानक)। "
                   "छपा ‘कंसांस’ सम्भवतः ‘कांसांस’ की भूल है; ‘अक्ष-कंस’ भी पढ़ा जा सकता है, इसलिए विभाजन पक्का नहीं। "
                   "दोनों पाठों में अंत का ‘अंसफलकेषु’ (अंसफलकों में) पक्का है। "
                   "गिनी गई वस्तु और क्रिया छपी नहीं।"),
    "hook": "तद्वत्: संख्या वही, स्थान कन्धे के।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 111, how is the number for these places given?",
            ("Not printed: तद्वत् carries it over", "The note: 'likewise' = the same number as in unit 110."),
            [("As eight, printed in this very line", "No number is printed; तद्वत् carries it over."),
             ("As thirty, printed in this very line", "No number is printed; तद्वत् carries it over."),
             ("As one each, printed in this very line", "No number is printed; तद्वत् carries it over.")],
            "The number is not printed; तद्वत् carries it over.",
            "तद्वत् = likewise."),
        match(1, "Match each sure part of unit 111 to its meaning.",
              [["तद्", "that"], ["-वत्", "like, as"], ["तद्वत्", "likewise"], ["अंसफलक", "shoulder-blade"],
               ["-एषु", "in (locative plural)"]],
              "तद्वत् = likewise; अंसफलकेषु = in the shoulder-blades.",
              "तद्, -वत्, तद्वत्, अंसफलक, -एषु."),
        fill(2, "The word for likewise that opens unit 111 is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("तद्वत्", "tadvat", "तद्वद्"),
             "तद्वत् = likewise: तद् (that) + वत् (like); before a vowel it is printed तद्वद्.",
             "तद्वत् = तद् + वत्: it repeats the last number without writing it.",
             "तद्वत् = likewise."),
        mcq("discriminate", 3, "Which split of the opening तद्वदक्ष... of unit 111 is right?",
            ("तद्वत् + अक्ष...", "त् before a vowel becomes द्: तद्वत् + अ → तद्वद."),
            [("तद्वद + क्ष...", "तद्वद is not the word; the word is तद्वत्."),
             ("तद्व + दक्ष...", "तद्व is not a word; the word is तद्वत्."),
             ("तद् + वदक्ष...", "वदक्ष is not a word; -वत् belongs to तद्.")],
            "तद्वत् (likewise) + अक्ष...: त् + vowel → द्.",
            "त् + vowel → द्."),
        mcq("apply", 4, "What does तद्वत् (likewise) carry over in unit 111?",
            ("The number of unit 110, not written again", "The note: 'likewise' = in the same number as in unit 110."),
            [("The places of unit 110, the two hips", "The places here are new; only the number carries over."),
             ("Twice the number of unit 110", "Likewise means the same, not twice."),
             ("The number thirty of unit 107", "The note ties 'likewise' to unit 110, not unit 107.")],
            "तद्वत् repeats the number of unit 110 without writing it.",
            "तद्वत् = likewise, the same number."),
        mcq("transfer", 5, "By the rule of तद्वत् + अ..., how is जगत् + ईशः (lord of the world) written when joined?",
            ("जगदीशः", "त् before a vowel becomes द्."),
            [("जगतीशः", "Before a vowel the final त् becomes द्; it does not stay त्."),
             ("जगन्नीशः", "न् would come before a nasal, not before a vowel."),
             ("जगच्चीशः", "च्च comes from त् before च, not before a vowel.")],
            "जगत् + ईशः = जगदीशः, like तद्वत् + अ... = तद्वद...",
            "त् + vowel → द्.",
            teaches="Final त् before a vowel becomes द्: तद्वत् + अक्ष... → तद्वदक्ष..."),
    ],
}

# ---------------------------------------------------------------- unit 112
AUTHORED["112"] = {
    "title": "तथागंडकर्णशंखेषु जत्रुतालुनोश्च",
    "question": "By unit 112, which places are named 'likewise'?",
    "rule": ("Likewise (तथा, the number of units 110-111, not restated) in the cheeks (गण्ड), ears (कर्ण) and temples "
             "(शङ्ख), and in the jatru and the palate (तालु)."),
    "limits": ("Prose; no verb and no counted noun are printed. Jatru = the collarbone region is probable only. "
               "शङ्ख = temple (standard) here; it also means conch."),
    "explain_hi": ("यह गद्य-पंक्ति ‘तथा’, वैसे ही, से आरम्भ होती है: संख्या वही जो इकाई ११०-१११ में है, दोबारा लिखी नहीं गई। "
                   "स्थान दो समूहों में हैं: गण्ड (गाल), कर्ण (कान), शंख (कनपटी, मानक) में; और जत्रु व तालु में। "
                   "जत्रु सम्भवतः हँसली या गर्दन-कन्धे के मिलने का स्थान है। "
                   "‘तालुनोश्च’ में च से पहले विसर्ग श् बना है। "
                   "शंख का दूसरा अर्थ ‘शंख’ (समुद्री) भी है, पर यहाँ कनपटी।"),
    "hook": "गाल, कान, कनपटी; फिर जत्रु और तालु।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 112, which places come first after 'likewise' (तथा)?",
            ("Cheeks, ears and temples", "तथा गण्डकर्णशङ्खेषु: in the cheeks, ears and temples."),
            [("Lips, chin and eyebrows", "None of these is named in unit 112."),
             ("Belly, navel and lips", "None of these is named in unit 112."),
             ("Eyelids, chin and the two lips", "None of these is named in unit 112.")],
            "Cheeks, ears and temples come first.",
            "गण्ड, कर्ण, शङ्ख."),
        order(1, "Put the words of unit 112 in the line's order.",
              ["तथा", "गण्ड", "कर्ण", "शङ्ख", "जत्रु", "तालु"],
              "Likewise in the cheeks, ears and temples, and in the jatru and the palate.",
              "तथा → गण्ड → कर्ण → शङ्ख → जत्रु → तालु."),
        match(2, "Match each place of unit 112 to its meaning.",
              [["गण्ड", "cheek"], ["कर्ण", "ear"], ["शङ्ख", "temple (here)"], ["तालु", "palate"],
               ["जत्रु", "probably the collarbone region"]],
              "Cheeks, ears, temples; jatru and palate.",
              "गण्ड, कर्ण, शङ्ख, तालु, जत्रु.", role="extend",
              teaches="शङ्ख here is the temple (standard); जत्रु is probably the collarbone region."),
        mcq("discriminate", 3, "What does तथा (likewise) carry over in unit 112?",
            ("The number of units 110-111, not written again", "The note: 'likewise' repeats the number, not restated."),
            [("A new number printed after the places", "No number is printed in unit 112."),
             ("The place 'hips' from unit 110", "The places here are new; only the number carries over."),
             ("The word 'teeth' from the next unit, unit 113", "Teeth come in the next unit; तथा looks back, not forward.")],
            "तथा repeats the number of the lines before.",
            "तथा = likewise, the same number."),
        multi("apply", 4, "Which places does unit 112 name?",
              [("Lips", "Lips are not named in unit 112."),
               ("Cheeks", "Right: गण्ड."),
               ("Eyebrows", "Eyebrows are not named in unit 112."),
               ("Palate", "Right: तालु.")],
              [1, 3],
              "Cheeks and palate are among its places.",
              "गण्डकर्णशङ्खेषु जत्रुतालुनोश्च."),
        mcq("transfer", 5, "By the rule of तालुनोः + च, how is नद्योः + च (and in the two rivers) written when joined?",
            ("नद्योश्च", "A visarga before च becomes श्."),
            [("नद्यो च", "Before च the visarga is not dropped; it becomes श्."),
             ("नद्योच्च", "च्च comes from त् before च, not from a visarga."),
             ("नद्योर्च", "र् is not the form before an unvoiced च; it becomes श्.")],
            "नद्योः + च = नद्योश्च, like तालुनोः + च = तालुनोश्च.",
            "Visarga before च → श्.",
            teaches="A visarga before च becomes श्: तालुनोः + च → तालुनोश्च."),
    ],
}

# ---------------------------------------------------------------- unit 113
AUTHORED["113"] = {
    "title": "त्रयोदश ग्रीवायां",
    "question": "By unit 113, which counts are given for the neck, throat, jaw, teeth, nose and head?",
    "rule": ("Thirteen in the neck, four in the kaṇṭhanāḍī, two in the jaw-joints, thirty-two teeth and as many "
             "ulūkhalas (तद्वत्), three in the nose, six in the head."),
    "limits": ("Prose; the counted noun is printed only for the teeth. Kaṇṭhanāḍī = windpipe and ulūkhala = tooth-socket are "
               "probable. No question on the case or number of हनुबन्धने."),
    "explain_hi": ("यह लम्बी गद्य-पंक्ति सिर-गर्दन की गिनती देती है: तेरह ग्रीवा (गर्दन) में, चार कण्ठनाड़ी (सम्भवतः श्वासनली) में, दो हनुबन्धन (जबड़े के जोड़ों) में। "
                   "फिर बत्तीस दाँत, और ‘तद्वत्’ उतने ही उलूखल (शब्दार्थ ओखली; सम्भवतः दाँतों के गड्ढे)। "
                   "अन्त में तीन नाक में और छह सिर में। "
                   "‘द्वात्रिंशद्दन्ताः’ में घोष द से पहले त् का द् हुआ है। "
                   "दाँतों के अतिरिक्त गिनी गई वस्तु छपी नहीं; अस्थि-गिनती से जोड़ा गया है।"),
    "hook": "गर्दन १३, कण्ठ ४, जबड़ा २, दाँत ३२, नाक ३, सिर ६।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 113, how many teeth are counted?",
            ("Thirty-two", "द्वात्रिंशद्दन्ताः: thirty-two teeth."),
            [("Twenty-eight", "द्वात्रिंशत् is thirty-two, not twenty-eight."),
             ("Thirty", "द्वात्रिंशत् is thirty-two, not thirty."),
             ("Twenty-four", "द्वात्रिंशत् is thirty-two, not twenty-four.")],
            "Thirty-two teeth.",
            "द्वात्रिंशत् = thirty-two."),
        order(1, "Put these parts of unit 113 in the line's order.",
              ["त्रयोदश ग्रीवायाम्", "चत्वारि कण्ठनाड्याम्", "द्वे हनुबन्धने", "द्वात्रिंशद्दन्ताः", "त्रीणि नासायाम्",
               "षट् शिरसि"],
              "Neck 13, kaṇṭhanāḍī 4, jaw-joints 2, teeth 32, nose 3, head 6.",
              "ग्रीवा → कण्ठनाडी → हनुबन्धन → दन्ताः → नासा → शिरस्."),
        match(2, "Match each place of unit 113 to its count.",
              [["ग्रीवा (neck)", "13"], ["कण्ठनाडी (probably windpipe)", "4"], ["दन्ताः (teeth)", "32"],
               ["नासा (nose)", "3"], ["शिरस् (head)", "6"]],
              "Neck 13, kaṇṭhanāḍī 4, teeth 32, nose 3, head 6.",
              "त्रयोदश, चत्वारि, द्वात्रिंशत्, त्रीणि, षट्.", role="extend",
              teaches="त्रयोदश = 13, चत्वारि = 4, द्वात्रिंशत् = 32, त्रीणि = 3, षट् = 6."),
        mcq("discriminate", 3, "Which split of द्वात्रिंशद्दंताः in unit 113 is right?",
            ("द्वात्रिंशत् + दन्ताः", "त् before the voiced द becomes द्."),
            [("द्वात्रिंशद + दन्ताः", "द्वात्रिंशद is not the word; the number is द्वात्रिंशत्."),
             ("द्वात्रिंश + द्दन्ताः", "द्दन्ताः is not a word; the word is दन्ताः."),
             ("द्वात्रिंशत् + अन्ताः", "That would give one द्: द्वात्रिंशदन्ताः.")],
            "द्वात्रिंशत् (thirty-two) + दन्ताः (teeth): त् + द → द्द.",
            "त् + voiced consonant → द्."),
        mcq("apply", 4, "By unit 113, how many ulūkhalas (probably tooth-sockets) does तद्वत् give?",
            ("Thirty-two, as many as the teeth", "The note: तद्वत् = as many, thirty-two sockets for thirty-two teeth."),
            [("Six, as many as in the head", "तद्वत् follows the teeth, not the head."),
             ("Three, as many as in the nose", "तद्वत् follows the teeth, not the nose."),
             ("Thirteen, as many as in the neck", "तद्वत् follows the teeth, not the neck.")],
            "As many ulūkhalas as teeth: thirty-two.",
            "द्वात्रिंशद्दन्ताः तद्वदुलूखलानि च."),
        mcq("transfer", 5, "By the rule of द्वात्रिंशत् + दन्ताः, how is तत् + दानम् (that gift) written when joined?",
            ("तद्दानम्", "त् before the voiced द becomes द्."),
            [("तत्दानम्", "Before a voiced द the final त् becomes द्; it does not stay त्."),
             ("तन्दानम्", "न् would come before a nasal, not before द."),
             ("तच्दानम्", "च् (or च्छ) comes from त् before च, छ or श, not before द.")],
            "तत् + दानम् = तद्दानम्, like द्वात्रिंशत् + दन्ताः = द्वात्रिंशद्दन्ताः.",
            "त् + voiced consonant → द्.",
            teaches="Final त् before a voiced consonant becomes द्: द्वात्रिंशत् + दन्ताः → द्वात्रिंशद्दन्ताः."),
    ],
}

# ---------------------------------------------------------------- unit 114
AUTHORED["114"] = {
    "title": "तानि कपालसंज्ञानि",
    "question": "By unit 114, which bones are named kapāla, and where are they?",
    "rule": ("Those (bones) in the knees, hips, shoulders, cheeks, palate, temples, groin, 'middle' and heads are named "
             "kapāla (कपालसंज्ञानि, 'plates'): the first of the bone classes."),
    "limits": ("Prose; the copula is understood. 'मध्य' (middle) is kept as printed; वङ्क्षणमध्य (middle of the groin) is a "
               "possible division: no question on वङ्क्षण or मध्य. The other classes come in units 115-117."),
    "explain_hi": ("यह गद्य-पंक्ति अस्थियों का पहला वर्ग बताती है: जानु, नितम्ब, अंस, गण्ड, तालु, शंख, वंक्षण, मध्य और सिरों में स्थित अस्थियाँ ‘कपाल’ कहलाती हैं। "
                   "कपाल का शब्दार्थ खपरा या चपटी प्लेट है; यह खोपड़ी भी हो सकता है, पर यहाँ एक अस्थि-वर्ग का नाम है। "
                   "‘तानि’ (वे) इकाई १०७-११३ में गिनी अस्थियों की ओर संकेत करता है। "
                   "‘मध्य’ छपे रूप में रखा गया है; ‘वंक्षणमध्य’ (वंक्षण का मध्य) भी पढ़ा जा सकता है। "
                   "रुचक, तरुण, वलय और नलक वर्ग इकाई ११५-११७ में आते हैं।"),
    "hook": "चपटी प्लेट जैसी हड्डियाँ: कपाल।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 114, what name is given to the bones of the knees, hips, shoulders and head?",
            ("Kapāla (plates)", "कपालसंज्ञानि: named kapāla."),
            [("Nalaka (tubes)", "Nalaka is a later class (unit 117), not the name here."),
             ("Valaya (rings)", "Valaya is a later class (unit 116), not the name here."),
             ("Taruṇa (tender)", "Taruṇa is a later class (unit 116), not the name here.")],
            "They are named kapāla.",
            "कपालसंज्ञानि = named kapāla."),
        order(1, "Put these places of unit 114 in the line's order.",
              ["जानु", "नितम्ब", "अंस", "गण्ड", "तालु", "शङ्ख"],
              "Knee, hip, shoulder, cheek, palate, temple (then groin, middle, head).",
              "जानु → नितम्ब → अंस → गण्ड → तालु → शङ्ख."),
        match(2, "Match each word of unit 114 to its meaning.",
              [["जानु", "knee"], ["नितम्ब", "hip"], ["अंस", "shoulder"], ["कपाल", "plate, potsherd"],
               ["संज्ञ", "named"]],
              "Bones at the knee, hip, shoulder... are named kapāla, plates.",
              "जानु, नितम्ब, अंस, कपाल, संज्ञ.", role="extend",
              teaches="कपाल = plate (literally potsherd): the name of one class of bone."),
        mcq("discriminate", 3, "Which split of नितंबांस in unit 114 is right?",
            ("नितम्ब + अंस", "अ + अ → आ: नितम्ब + अंस → नितम्बांस."),
            [("नितम्बाम् + स", "स is not a word here; the word is अंस (shoulder)."),
             ("नितम्ब + आंस", "आंस is not the word; the word for shoulder is अंस."),
             ("नितम्बे + अंस", "ए + अ would give नितम्बेऽंस, not नितम्बांस.")],
            "नितम्ब (hip) + अंस (shoulder): अ + अ → आ.",
            "अ + अ → आ."),
        multi("apply", 4, "Which places of the body hold kapāla bones by unit 114?",
              [("The knee", "Right: जानु is in the list."),
               ("The teeth", "Teeth are rucakas (unit 115), not kapālas."),
               ("The nose", "The nose is not in the kapāla list (unit 116 puts it with the taruṇas)."),
               ("The shoulder", "Right: अंस is in the list.")],
              [0, 3],
              "Knee and shoulder are in the kapāla list.",
              "जानुनितम्बांस... कपालसंज्ञानि."),
        mcq("transfer", 5, "By the pattern of कपालसंज्ञानि (named kapāla), what does नलकसंज्ञानि mean in a new example?",
            ("Those named nalaka", "-संज्ञ at the end of a compound = named, as कपालसंज्ञानि = named kapāla."),
            [("Those without the nalaka", "Nothing in -संज्ञ means without."),
             ("Those larger than nalaka", "Nothing in -संज्ञ means larger."),
             ("Those inside the nalaka", "Nothing in -संज्ञ means inside.")],
            "नलकसंज्ञानि = named nalaka, as कपालसंज्ञानि = named kapāla.",
            "X + संज्ञ = named X (bahuvrīhi).",
            teaches="कपालसंज्ञानि is a bahuvrīhi: those whose name (संज्ञा) is kapāla."),
    ],
}


# ===================================================================== NOTES_HI
NOTES_HI = {
    "102": ("गद्य; विश्वास मध्यम। पाठ-चिह्न (सम्भावित): छपा ‘तत्रैकै कस्मिन’ एक ही शब्द ‘एकैकस्मिन्’ (एक-एक में) को दो टुकड़ों में बाँटता है और "
            "अन्त में फालतू -अ है; इस रूप पर कोई प्रश्न नहीं। ‘तानि पंचदश’ को ३ × ५ माना गया; संस्कृत नहीं कहती कि क्या गिना गया। "
            "नख छपे पाठ में अस्थियों में गिने गए। ‘नखाःप्रत्येकम्’ छपाई में जुड़ा है। सन्धि जाँची: तत्र + एक → तत्रैक (अ + ए → ऐ); "
            "त्रीणि + अस्थीनि → त्रीण्यस्थीनि (इ + अ → य); प्रत्येकम् + अङ्गुल्याम् → प्रत्येकमङ्गुल्याम्; छपा पंच/मंगुल्यां = पञ्च/मङ्गुल्याम्।"),
    "103": ("गद्य; विश्वास निम्न। पाठ-चिह्न: छपा ‘पाणि’ (हाथ) पैर की सूची में नहीं बैठता और समास में विसर्ग/र् भी नहीं होना चाहिए; "
            "अनुमानित पाठ ‘पार्ष्णि’ (एड़ी)। अन्तिम शब्द पर कोई प्रश्न नहीं। ‘कूर्च’ का अर्थ अनिश्चित है, इसलिए उसका अनुवाद नहीं किया गया। "
            "‘तत्’ को शलाकाओं की ओर माना गया। छपा ‘कूर्च्च’ (दोहरा च) सामान्य किया गया। जोड़: ५ + १५ + ५ + १ + २ + २ + २ + १ + १ + १ = ३५, "
            "सक्थि का चौथाई भाग; यह केवल गणना का प्रमाण है। सन्धि जाँची: जङ्घासु + एकैकम् → जङ्घास्वेकैकम् (उ + ए → वे); "
            "प्रतिबन्धकम् + एकम् → प्रतिबन्धकमेकम्।"),
    "104": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। छपा ‘वाह्वोः’ = बाह्वोः (व/ब का अदल-बदल, सामान्य किया गया)। ‘सर्वाणिच’ = सर्वाणि च। "
            "क्रिया समझी जाती है। सन्धि जाँची: नख + अस्थि + आदीनि → नखास्थ्यादीनि (अ + अ → आ; इ + आ → या); सक्थिवत् + बाह्वोः → "
            "सक्थिवद्बाह्वोः (घोष ब से पहले त् → द्); बाह्वोः + च → बाह्वोश्च (च से पहले विसर्ग → श्)।"),
    "105": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। क्रिया न छपी, न जोड़ी गई। चौबीस एक ओर हैं या कुल, पंक्ति नहीं बताती। "
            "चतुर्विंशतिः स्त्रीलिंग एकवचन, पर्शुकाः स्त्रीलिंग बहुवचन। सन्धि जाँची: चतुर् + विंशतिः → चतुर्विंशतिः; विसर्ग प से पहले बना रहा।"),
    "106": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। ‘तत्-’ इकाई १०५ की पसलियों की ओर। स्थालक और अर्बुद की आधुनिक पहचान पक्की नहीं "
            "(सम्भवतः पसलियों के प्याले और गाँठ जैसे जोड़ वाले सिरे, यह केवल अनुमान है)। अर्बुद अन्यत्र ट्यूमर; यहाँ शब्दार्थ ‘उभार’। "
            "सन्धि जाँची: तावन्ति + एव → तावन्त्येव (इ + ए → ये); तत्स्थालकानि + अर्बुदानि → तत्स्थालकान्यर्बुदानि (इ + अ → य); छपा तावंत्येव = तावन्त्येव।"),
    "107": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। समूह-टिप्पणी: पंक्ति सम्भवतः इकाई १००-१०६ की अस्थि-गिनती आगे बढ़ाती है; "
            "गिनी गई वस्तु (अस्थियाँ) छपी नहीं, जोड़ी नहीं गई। क्रिया समझी जाती है। ‘पृष्ठे’ यहाँ सप्तमी एकवचन (पीठ में)।"),
    "108": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। छपा ‘अष्टावुरसि’ = अष्टौ उरसि। समूह-टिप्पणी: अस्थि-गिनती जारी, वस्तु छपी नहीं। "
            "क्रिया समझी जाती है। सन्धि जाँची: अष्टौ + उरसि → अष्टावुरसि (औ + स्वर → आव्)।"),
    "109": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। समूह-टिप्पणी: अस्थि-गिनती जारी, वस्तु छपी नहीं। भग का सामान्य अर्थ स्त्री-जननांग; "
            "अस्थि-स्थान के रूप में जघन-क्षेत्र सम्भावित ही है। त्रिक = त्रिकास्थि-क्षेत्र (सम्भावित)। सन्धि जाँची: एक + एकम् → एकैकम् "
            "(अ + ए → ऐ); छपा एकैकं (व्यंजन से पहले म् → ं)।"),
    "110": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। समूह-टिप्पणी: अस्थि-गिनती जारी, वस्तु छपी नहीं। ‘दो’ कुल है या हर ओर, यह नहीं कहा गया। "
            "सन्धि जाँची: नितम्बयोः + च → नितम्बयोश्च (च से पहले विसर्ग → श्); छपा नितंब = नितम्ब।"),
    "111": ("गद्य; विश्वास निम्न। पाठ-चिह्न: छपा ‘कंसांस’ सम्भवतः ‘कांसांस’ (अक्षक + अंस + अंसफलक) की भूल; छपा रूप ‘अक्ष-कंस’ भी पढ़ा जा सकता है; "
            "अर्थ पक्का नहीं। अक्षक = हँसली (सम्भावित, अनुमानित पाठ पर)। दोनों पाठों में ‘अंसफलकेषु’ पक्का (अंसफलक = कन्धे की चपटी हड्डी, मानक)। "
            "‘तद्वत्’ = इकाई ११० जितनी संख्या, जो दोहराई नहीं गई। समूह-टिप्पणी: अस्थि-गिनती जारी। सन्धि जाँची: तद्वत् + अ... → तद्वद... (त् + स्वर → द्)।"),
    "112": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। ‘तथा’ इकाई ११०-१११ की संख्या दोहराता है, जो फिर नहीं लिखी गई। जत्रु = हँसली या "
            "गर्दन-कन्धे के मिलने का क्षेत्र (सम्भावित); शंख = कनपटी (मानक), दूसरा अर्थ समुद्री शंख। सन्धि जाँची: तालुनोः + च → तालुनोश्च "
            "(च से पहले विसर्ग → श्); ‘तथागंड’ छपाई में जुड़ा है (तथा गण्ड..., कोई ध्वनि-परिवर्तन नहीं)।"),
    "113": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। समूह-टिप्पणी: अस्थि-गिनती जारी। ‘तद्वत्’ = उतने ही (बत्तीस दाँतों के लिए बत्तीस उलूखल), "
            "संख्या दोहराई नहीं गई। कण्ठनाडी = श्वासनली और उलूखल = दाँत का गड्ढा, दोनों सम्भावित। छपा ‘कंठनाड्यांद्वे’ दो शब्द जोड़ता है "
            "(कण्ठनाड्याम् द्वे)। ‘हनुबन्धने’ को दो जबड़े-जोड़ माना गया; इसके रूप पर कोई प्रश्न नहीं। सन्धि जाँची: द्वात्रिंशत् + दन्ताः → "
            "द्वात्रिंशद्दन्ताः (त् + घोष → द्); तद्वत् + उलूखलानि → तद्वदुलूखलानि (त् + स्वर → द्)।"),
    "114": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। ‘तानि’ इकाई १०७-११३ में गिनी अस्थियों की ओर। ‘मध्य’ छपे रूप में रखा, कोई और अर्थ नहीं "
            "जोड़ा; ‘वंक्षणमध्य’ (वंक्षण का मध्य) भी सम्भव। कपाल = खपरा, प्लेट, खोपड़ी भी; यहाँ एक अस्थि-वर्ग का नाम (देखें इकाई ११८)। "
            "सन्धि जाँची: नितम्ब + अंस → नितम्बांस (अ + अ → आ); शिरःसु में स से पहले विसर्ग छपा है।"),
}


# ===================================================================== AIDS
AIDS = {
    "102": {
        "diagram": {"groups": [
            {"label": "एक सक्थि (निचला अंग) में, क्रम से", "items": ["पाँच पादनख", "प्रत्येक अंगुली में तीन अस्थियाँ",
                                                              "‘वे पन्द्रह’ (३ × ५ माना गया)"]}]},
        "chunks": "तत्रैकै कस्मिन सक्थिनि | पंच पादनखाः | प्रत्येकमंगुल्यां त्रीण्यस्थीनि | तानि पंचदश",
        "sandhi": "अ + ए → ऐ: तत्र + एक... → तत्रैक... · इ + अ → य: त्रीणि + अस्थीनि → त्रीण्यस्थीनि।",
        "frame": "कहाँ: एक-एक सक्थि में → क्या: पाँच पादनख → हर अंगुली में: तीन अस्थियाँ → योग: पन्द्रह।",
    },
    "103": {
        "diagram": {"groups": [
            {"label": "पक्का पाठ", "items": ["पाँच पादशलाकाएँ", "उनका एक प्रतिबन्धक", "कूर्च, गुल्फ, जङ्घा में दो-दो"]},
            {"label": "अनुमानित पाठ पर", "items": ["एड़ी (छपा ‘पाणि’), जानु, ऊरु में एक-एक"]}]},
        "chunks": "पंचपादशलाकाः | तत्प्रतिबंधकमेकं | द्वे द्वे कूर्च्चगुल्फजंघास्वेकैकं | पाणिर्जानूरुषु",
        "sandhi": "उ + ए → वे: जङ्घासु + एकैकम् → जङ्घास्वेकैकम्।",
        "anchors": "पाँच शलाकाएँ पाँच अंगुलियों जैसी गिनती: पाँच नख, पाँच शलाका। (मेरी याद-पद्धति)",
    },
    "104": {
        "chunks": "सर्वाणिच | नखास्थ्यादीनि | सक्थिवद्वाह्वोश्च",
        "sandhi": "अ + अ → आ, इ + आ → या: नख + अस्थि + आदीनि → नखास्थ्यादीनि · त् + घोष → द्: सक्थिवत् + बाह्वोः → सक्थिवद्बाह्वोः।",
        "frame": "क्या: नख-अस्थि आदि सब → किसके समान: सक्थिवत् (पैर जैसे) → कहाँ: बाह्वोः (दोनों बाहुओं में)।",
    },
    "105": {
        "chunks": "चतुर्विंशतिः | पर्शुकाः",
        "letters": "चतुर्-विंशति: ‘चार-बीस’ = चौबीस; हिन्दी ‘चौबीस’ में भी चौ (चार) + बीस। (मेरी याद-पद्धति)",
        "frame": "संख्या: चतुर्विंशतिः (स्त्री. एकवचन) → वस्तु: पर्शुकाः (बहुवचन) → क्रिया: समझी जाती है।",
    },
    "106": {
        "chain": {"steps": ["इकाई १०५: चौबीस पर्शुकाएँ", "तावन्त्येव: उतने ही", "उनके स्थालक", "और अर्बुद"]},
        "chunks": "तावंत्येव | तत्स्थालकान्यर्बुदानि च",
        "sandhi": "इ + ए → ये: तावन्ति + एव → तावन्त्येव · इ + अ → य: स्थालकानि + अर्बुदानि → स्थालकान्यर्बुदानि।",
    },
    "107": {
        "chunks": "त्रिंशत् | पृष्ठे",
        "frame": "संख्या: त्रिंशत् (तीस) → स्थान: पृष्ठे (पीठ में) → वस्तु: छपी नहीं (अस्थि-गिनती से)।",
        "pegs": "‘पृष्ठ’ = पीठ, और पुस्तक का ‘पृष्ठ’ भी: पीठ पर तीस पन्ने। (मेरी याद-पद्धति, केवल याद की सहायता)",
    },
    "108": {
        "chunks": "अष्टाव् | उरसि",
        "sandhi": "औ + स्वर → आव्: अष्टौ + उरसि → अष्टावुरसि।",
        "frame": "संख्या: अष्टौ (आठ) → स्थान: उरसि (छाती में) → वस्तु और क्रिया: छपी नहीं।",
    },
    "109": {
        "chunks": "एकैकं | भगे | त्रिके",
        "sandhi": "अ + ए → ऐ: एक + एकम् → एकैकम्।",
        "frame": "संख्या: एकैकम् (एक-एक) → स्थान: भगे (सम्भवतः जघन), त्रिके (सम्भवतः त्रिकास्थि-क्षेत्र)।",
    },
    "110": {
        "chunks": "नितंबयोश्च | द्वे",
        "sandhi": "च से पहले विसर्ग → श्: नितम्बयोः + च → नितम्बयोश्च।",
        "frame": "स्थान: नितम्बयोः (दोनों नितम्बों में) → संख्या: द्वे (दो; कुल या हर ओर, अनकहा)।",
    },
    "111": {
        "chunks": "तद्वद् | अक्षक(?)कंसांस | फलकेषु",
        "sandhi": "त् + स्वर → द्: तद्वत् + अ... → तद्वद...",
        "frame": "संख्या: तद्वत् (इकाई ११० जितनी) → स्थान: अनुमानित पाठ पर अक्षक, अंस; पक्का: अंसफलक (कन्धे की चपटी हड्डी)।",
    },
    "112": {
        "diagram": {"groups": [
            {"label": "तथा (वही संख्या): पहला समूह", "items": ["गण्ड (गाल)", "कर्ण (कान)", "शंख (कनपटी)"]},
            {"label": "च: दूसरा समूह", "items": ["जत्रु (सम्भवतः हँसली-क्षेत्र)", "तालु"]}]},
        "chunks": "तथागंडकर्णशंखेषु | जत्रुतालुनोश्च",
        "sandhi": "च से पहले विसर्ग → श्: तालुनोः + च → तालुनोश्च।",
        "letters": "स्थानों के पहले अक्षर क्रम से: ग-क-शं, ज-ता (गण्ड, कर्ण, शंख; जत्रु, तालु)। (मेरी याद-पद्धति)",
    },
    "113": {
        "diagram": {"groups": [
            {"label": "सिर-गर्दन की गिनती (क्रम से)", "items": ["१३ ग्रीवा में", "४ कण्ठनाड़ी में (सम्भवतः श्वासनली)",
                                                         "२ हनुबन्धन में", "३२ दाँत", "उतने ही उलूखल (सम्भवतः दाँतों के गड्ढे)",
                                                         "३ नाक में", "६ सिर में"]}]},
        "chunks": "त्रयोदश ग्रीवायां | चत्वारि कंठनाड्यां | द्वे हनुबंधने | द्वात्रिंशद्दंताः | तद्वदुलूखलानि च | त्रीणि नासायां | षट् शिरसि",
        "sandhi": "त् + घोष → द्: द्वात्रिंशत् + दन्ताः → द्वात्रिंशद्दन्ताः · त् + स्वर → द्: तद्वत् + उलूखलानि → तद्वदुलूखलानि।",
        "pegs": "नीचे से ऊपर की यात्रा: गर्दन → कण्ठ → जबड़ा → दाँत → नाक → सिर; सबसे बड़ा अंक दाँतों का, ३२। (मेरी याद-पद्धति)",
    },
    "114": {
        "diagram": {"groups": [
            {"label": "कपाल नाम वाली अस्थियों के स्थान (क्रम से)",
             "items": ["जानु", "नितम्ब", "अंस", "गण्ड", "तालु", "शंख", "वंक्षण", "मध्य (छपे रूप में)", "सिर"]}]},
        "chunks": "तानि | जानुनितंबांसगंडतालुशंखवंक्षणमध्यशिरःसु | कपालसंज्ञानि",
        "sandhi": "अ + अ → आ: नितम्ब + अंस → नितम्बांस।",
        "letters": "स्थानों के पहले अक्षर क्रम से: जा-नि-अं-ग-ता-शं-वं-म-शि। (मेरी याद-पद्धति)",
    },
}


# ===================================================================== IMAGE_SPECS
IMAGE_SPECS = {
    ("102", "diagram"): {
        "file": "sh5-sakthi-nakha-102.svg",
        "alt": ("Table of unit 102, one lower limb: five foot-nails; three bones in each toe; 'those are fifteen', taken as "
                "3 x 5 (the Sanskrit does not say what it counts)."),
        "type": "table",
        "title": "इकाई १०२: एक सक्थि की पहली गिनती",
        "heads": ["छपा अंश", "अर्थ"],
        "rows": [["पंच पादनखाः", "पाँच पादनख"], ["प्रत्येकमंगुल्यां त्रीण्यस्थीनि", "हर अंगुली में तीन अस्थियाँ"],
                 ["तानि पंचदश", "वे पन्द्रह (३ × ५ माना गया)"]],
    },
    ("103", "diagram"): {
        "file": "sh5-padashalaka-103.svg",
        "alt": ("Two columns of unit 103. Sure reading: five foot-rods (pādaśalākā); one binder of them; two each in the "
                "kūrca, ankle and shank. On a conjectural reading: one each in the heel (printed pāṇi), knee and thigh."),
        "type": "split",
        "title": "इकाई १०३: पादशलाका और आगे",
        "cols": [["पक्का पाठ", ["पाँच पादशलाकाएँ", "उनका एक प्रतिबन्धक", "कूर्च, गुल्फ, जङ्घा में दो-दो"]],
                 ["अनुमानित पाठ पर", ["एड़ी (छपा पाणि)", "जानु", "ऊरु", "इनमें एक-एक"]]],
    },
    ("106", "chain"): {
        "file": "sh5-sthalaka-arbuda-106.svg",
        "alt": ("Chain of unit 106: twenty-four ribs (unit 105); just as many; their sthālakas; and arbudas."),
        "type": "chain",
        "title": "इकाई १०६: उतने ही",
        "steps": ["इकाई १०५: चौबीस पर्शुकाएँ", "तावन्त्येव: उतने ही", "उनके स्थालक", "और अर्बुद"],
    },
    ("112", "diagram"): {
        "file": "sh5-ganda-talu-112.svg",
        "alt": ("Two columns of unit 112, likewise (same number): first group cheek (gaṇḍa), ear (karṇa), temple (śaṅkha); "
                "second group jatru (probably the collarbone region) and palate (tālu)."),
        "type": "split",
        "title": "इकाई ११२: तथा, दो समूह",
        "cols": [["तथा: पहला समूह", ["गण्ड (गाल)", "कर्ण (कान)", "शंख (कनपटी)"]],
                 ["च: दूसरा समूह", ["जत्रु (सम्भवतः हँसली-क्षेत्र)", "तालु"]]],
    },
    ("113", "diagram"): {
        "file": "sh5-griva-shiras-113.svg",
        "alt": ("Table of unit 113 in line order: neck 13; kaṇṭhanāḍī (probably windpipe) 4; jaw-joints 2; teeth 32; "
                "ulūkhala (probably tooth-sockets) as many; nose 3; head 6."),
        "type": "table",
        "title": "इकाई ११३: गर्दन से सिर तक",
        "heads": ["स्थान (क्रम से)", "संख्या"],
        "rows": [["ग्रीवा", "१३"], ["कण्ठनाड़ी (सम्भवतः श्वासनली)", "४"], ["हनुबन्धन", "२"], ["दाँत", "३२"],
                 ["उलूखल (सम्भवतः दाँतों के गड्ढे)", "उतने ही"], ["नासा", "३"], ["सिर", "६"]],
    },
    ("114", "diagram"): {
        "file": "sh5-kapala-114.svg",
        "alt": ("Table of unit 114: the places of the bones named kapāla (plates), numbered in line order: 1 knee, 2 hip, "
                "3 shoulder, 4 cheek, 5 palate, 6 temple, 7 groin, 8 'middle' (as printed), 9 head."),
        "type": "table",
        "title": "इकाई ११४: कपाल नाम वाली अस्थियाँ",
        "heads": ["क्रम", "स्थान"],
        "rows": [["१", "जानु"], ["२", "नितम्ब"], ["३", "अंस"], ["४", "गण्ड"], ["५", "तालु"], ["६", "शंख"],
                 ["७", "वंक्षण"], ["८", "मध्य (छपे रूप में)"], ["९", "सिर"]],
    },
}
