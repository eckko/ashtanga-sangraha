from helpers import mcq, match, order, fill, multi, accepts


AUTHORED = {}

# ---------------------------------------------------------------- unit 217
AUTHORED["217"] = {
    "title": "तथाऽभ्यंगलेपादिवीर्य्यं त्वचि",
    "question": "By unit 217, what do 'they' carry, and what do they take up?",
    "rule": ("Likewise (तथा) they carry (नयन्ति) the potency (वीर्य) of oil massage (अभ्यङ्ग), paste (लेप) and the like, "
             "fully matured (विपक्वम्) in the skin (त्वचि); and they take up (गृह्णन्ति) touch (स्पर्श)."),
    "limits": ("Low confidence. 'They' is unnamed (probably the vessels of unit 216) and the destination is not stated: "
               "no question on either. The printed तं (read तत्) and the spelling गृण्हंति (for गृह्णन्ति) are flagged: "
               "questions use only the sure sense (they carry, they take up), never these forms."),
    "explain_hi": ("यह गद्य-पंक्ति इकाई २१६ के बाद आती है और ‘तथा’ (इसी प्रकार) से दूसरा काम जोड़ती है। "
                   "वे अभ्यंग (तेल-मालिश) और लेप आदि के वीर्य यानी शक्ति को, जो त्वचा में पूरी तरह पक चुकी है, ले जाती हैं। "
                   "और वे स्पर्श को ग्रहण करती हैं। "
                   "‘वे’ कौन हैं, इस इकाई में नाम नहीं; डेटा के अनुसार सम्भवतः इकाई २१६ वाली ही (स्त्रीलिङ्ग) नाड़ियाँ, यानी सिरा-धमनी। "
                   "वीर्य कहाँ ले जाया जाता है, यह भी नहीं बताया। "
                   "विश्वास निम्न है, इसलिए प्रश्न केवल पक्के अंशों पर हैं।"),
    "hook": "त्वचा में पका अभ्यंग-लेप आदि का वीर्य: वे ले जाती हैं; और स्पर्श ग्रहण करती हैं।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 217, whose potency (वीर्य) is carried after it has matured in the skin?",
            ("Of oil massage, paste and the like", "अभ्यङ्गलेपादिवीर्यम्: the potency of abhyaṅga, lepa and the like."),
            [("Of the food eaten and the water drunk", "Food and drink are not named in unit 217; it names massage and paste."),
             ("Of the semen and the menstrual blood", "Śukra and rajas are measured in units 223 and 225, not carried here."),
             ("Of the bones and the joints of the limbs", "Bones and joints are not named in unit 217.")],
            "They carry the potency of oil massage (abhyaṅga), paste (lepa) and the like, matured in the skin.",
            "अभ्यङ्गलेपादिवीर्यं त्वचि विपक्वम्."),
        order(1, "Put these printed parts of unit 217 in the line's order.",
              ["तथाऽभ्यंगलेपादिवीर्य्यं", "त्वचि", "विपक्वंतंनयंति", "स्पर्शं च", "गृण्हंति"],
              "Likewise the potency of massage, paste and the like, in the skin, matured, they carry; and touch they take up.",
              "तथा … वीर्यम् → त्वचि → विपक्वम् … नयन्ति → स्पर्शं च → गृह्णन्ति."),
        match(2, "Match each word of unit 217 to its meaning.",
              [["अभ्यङ्ग", "oil massage"], ["लेप", "paste, plaster"], ["वीर्य", "potency"], ["त्वच्", "skin"],
               ["स्पर्श", "touch"]],
              "The potency of oil massage and paste, matured in the skin, is carried; touch is taken up.",
              "अभ्यङ्ग, लेप, वीर्य, त्वच्, स्पर्श.", role="extend",
              teaches="-आदि at the end of a list means 'and the like': अभ्यङ्गलेपादि = oil massage, paste and the like."),
        mcq("discriminate", 3, "By unit 217, what has happened to that potency in the skin (त्वचि)?",
            ("It has fully matured there", "विपक्वम् = fully matured, past participle of वि-√पच्."),
            [("It has flowed out there as sweat", "Sweat is carried in unit 216; unit 217 says the potency matured."),
             ("It has become countless there", "'Countless' is said of the srotas in unit 218, not of a potency."),
             ("It has been bound there to dung", "Binding to the dung is said in unit 221 of a liquid.")],
            "The potency of massage and paste is वीर्यं त्वचि विपक्वम्: fully matured in the skin.",
            "त्वचि विपक्वम् = fully matured in the skin."),
        multi("apply", 4, "Which two actions does unit 217 give to its unnamed subject ('they')?",
              [("They cook the food (पचन्ति)", "Cooking food is not said in unit 217."),
               ("They carry the potency (नयन्ति)", "Right: वीर्यं … नयन्ति, they carry the potency."),
               ("They cover the joints (प्रच्छादयन्ति)", "Covering the joints is said in unit 212 (probably of the peśīs), not in unit 217."),
               ("They take up touch (गृह्णन्ति)", "Right: स्पर्शं च गृह्णन्ति, and they take up touch.")],
              [1, 3],
              "They carry the matured potency, and they take up touch.",
              "वीर्यं … नयन्ति; स्पर्शं च गृह्णन्ति."),
        mcq("transfer", 5, "By the rule of स्पर्शं च (स्पर्शम् + च), how is फलम् + च (and the fruit) written inside a sentence?",
            ("फलं च", "A final म् before a consonant inside a sentence is written as anusvāra, as स्पर्शम् + च → स्पर्शं च."),
            [("फलश्च", "श् before च comes from a visarga, not from a final म्."),
             ("फलो च", "ओ comes from अः before a voiced consonant; च is not voiced, and the word ends in म्."),
             ("फला च", "The म् is not dropped with a long आ; it becomes anusvāra.")],
            "फलम् + च → फलं च, like स्पर्शम् + च → स्पर्शं च.",
            "Final म् + consonant (inside a sentence) → ं.",
            teaches="A final म् before a consonant inside a sentence is written ं: स्पर्शम् + च → स्पर्शं च."),
    ],
}

# ---------------------------------------------------------------- unit 218
AUTHORED["218"] = {
    "title": "स्रोतांसि पुनरसंख्येयान्येव",
    "question": "By unit 218, what is said about the number of the srotas (bodily channels)?",
    "rule": "The srotas (स्रोतांसि, bodily channels), however (पुनः), are indeed (एव) countless (असंख्येयानि).",
    "limits": ("A short prose line; the copula 'are' is understood. Srotas is kept as a doctrinal term with no modern "
               "equivalent. The line gives no count and names no srotas; it does not say why they are countless."),
    "explain_hi": ("यह छोटी गद्य-पंक्ति कहती है कि स्रोत यानी शरीर के मार्ग तो असंख्य ही हैं। "
                   "‘पुनः’ यहाँ ‘तो, परन्तु’ के अर्थ में है: पहले गिनी गई चीज़ों के बाद स्रोतों की गिनती नहीं हो सकती। "
                   "‘असंख्येय’ = अ (नहीं) + संख्येय (गिनने योग्य), यानी जिन्हें गिना न जा सके। "
                   "‘एव’ बात पर ज़ोर देता है: असंख्य ही। "
                   "स्रोतस् शास्त्रीय शब्द है; कोई आधुनिक पर्याय नहीं रखा गया।"),
    "hook": "स्रोत गिनती से बाहर: असंख्येय ही।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 218, how many srotas (bodily channels) are there?",
            ("Countless", "असंख्येयानि एव: indeed countless."),
            [("Three hundred and sixty", "Three hundred and sixty is the count of the bones in unit 100."),
             ("Sixteen, like the jālas", "Sixteen is the count of the jālas (nets) in unit 93."),
             ("Ten, like the seats of life", "Ten is the count of the seats of life in unit 90.")],
            "स्रोतांसि पुनः असंख्येयानि एव: the srotas are indeed countless.",
            "स्रोतांसि असंख्येयानि."),
        order(1, "Put the words of unit 218 in the line's order.",
              ["स्रोतांसि", "पुनः", "असंख्येयानि", "एव"],
              "The srotas, however, countless, indeed.",
              "स्रोतांसि → पुनः → असंख्येयानि → एव."),
        match(2, "Match each word of unit 218 to its meaning.",
              [["स्रोतस्", "bodily channel"], ["पुनः", "however, again"], ["असंख्येय", "countless"],
               ["एव", "indeed"]],
              "The srotas (channels), however, are indeed countless.",
              "स्रोतस्, पुनः, असंख्येय, एव.", role="extend",
              teaches="असंख्येय = अ (not) + संख्येय (to be counted): what cannot be counted."),
        mcq("discriminate", 3, "Which split of पुनरसंख्येयान्येव is right?",
            ("पुनः + असंख्येयानि + एव", "पुनः (base पुनर्) keeps its र् before a vowel; इ + ए → ये."),
            [("पुनर + संख्येयानि + एव", "पुनर is not a word, and without the अ the meaning would flip to 'countable'."),
             ("पुनः + असंख्येयान् + एव", "न् + ए would give नेव, with no य; the य comes from इ."),
             ("पुनः + असंख्येये + एव", "ए before ए would give -येय एव, not -यान्येव; the word is असंख्येयानि.")],
            "पुनः (पुनर्) + असंख्येयानि + एव → पुनरसंख्येयान्येव.",
            "पुनर् + vowel → पुनर…; इ + a different vowel → य्."),
        mcq("apply", 4, "A student says that unit 218 lists the srotas one by one. What is wrong with that?",
            ("It lists none; it calls them countless", "The line only says the srotas are countless (असंख्येय)."),
            [("It lists them, but only in the women", "Women are not mentioned in unit 218."),
             ("It lists them, but counts only three", "No number at all is given in unit 218."),
             ("It lists them, but under the name sirā", "Sirā and the rest are taken up in unit 219, not listed here.")],
            "Unit 218 gives no list: स्रोतांसि पुनरसंख्येयान्येव.",
            "स्रोतांसि असंख्येयानि = no count, no list."),
        mcq("transfer", 5, "By the rule of असंख्येयानि + एव → असंख्येयान्येव, how is फलानि + एव (the fruits indeed) joined?",
            ("फलान्येव", "इ before a different vowel becomes य्, as असंख्येयानि + एव."),
            [("फलानेव", "ए from a join comes from अ + इ; here it is इ + ए."),
             ("फलान्यैव", "The ए of एव stays ए after य्; it does not become ऐ."),
             ("फलानैव", "ऐ comes from अ + ए; फलानि ends in इ.")],
            "फलानि + एव = फलान्येव, like असंख्येयानि + एव = असंख्येयान्येव.",
            "इ + a different vowel → य् + that vowel.",
            teaches="इ before a different vowel becomes य्: असंख्येयानि + एव → असंख्येयान्येव."),
    ],
}

# ---------------------------------------------------------------- unit 219
AUTHORED["219"] = {
    "title": "तथाऽपि तु सिरादीनि",
    "question": "By unit 219, how and where will the sirā and the rest be taught?",
    "rule": ("Even so (तथापि तु), the sirā and the rest (सिरादीनि) will be taught (उपदेक्ष्यन्ते) elsewhere (अन्यत्र), "
             "broadly, in outline (यथास्थूलम्), and as their use requires (यथोपयोगम्)."),
    "limits": ("A prose line. It does not say where 'elsewhere' is or which items 'and the rest' covers: no question on "
               "either. The printed avagraha in तथाऽपि is a print habit (तथा अपि)."),
    "explain_hi": ("यह गद्य-पंक्ति इकाई २१८ के बाद आती है: स्रोत असंख्य हैं, फिर भी (तथापि तु) सिरा आदि का उपदेश होगा। "
                   "वह उपदेश दूसरी जगह (अन्यत्र) होगा, स्थूल रूप से यानी मोटे तौर पर (यथास्थूलम्), और उपयोग के अनुसार (यथोपयोगम्)। "
                   "‘उपदेक्ष्यन्ते’ भविष्यत् कर्मवाच्य है: सिखाए जाएँगे। "
                   "‘अन्यत्र’ कौन-सा स्थान है और ‘आदि’ में क्या-क्या है, पंक्ति नहीं बताती।"),
    "hook": "असंख्य होकर भी: सिरा आदि मोटे तौर पर, काम भर, आगे सिखाए जाएँगे।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 219, what will be done with the sirā and the rest?",
            ("They will be taught elsewhere", "अन्यत्र उपदेक्ष्यन्ते: they will be taught elsewhere."),
            [("They are counted here, one by one", "No count is given in unit 219; the teaching is put off."),
             ("They are left out, never to be taught", "उपदेक्ष्यन्ते says they will be taught."),
             ("They are measured here in handfuls", "Handful measures belong to the fluids from unit 222 on.")],
            "सिरादीनि … अन्यत्र उपदेक्ष्यन्ते: they will be taught elsewhere.",
            "अन्यत्र उपदेक्ष्यन्ते = will be taught elsewhere."),
        order(1, "Put these printed parts of unit 219 in the line's order.",
              ["तथाऽपि तु", "सिरादीनि", "यथास्थूलं", "यथोपयोगं", "चान्यत्रोपदेक्ष्यंते"],
              "Even so, the sirā and the rest, broadly and as use requires, will be taught elsewhere.",
              "तथापि तु → सिरादीनि → यथास्थूलम् → यथोपयोगम् → च अन्यत्र उपदेक्ष्यन्ते."),
        match(2, "Match each word of unit 219 to its meaning.",
              [["तथापि", "even so"], ["स्थूल", "gross, broad"], ["उपयोग", "use"], ["अन्यत्र", "elsewhere"],
               ["उपदेक्ष्यन्ते", "will be taught"]],
              "Even so, the sirā and the rest will be taught elsewhere, broadly and as use requires.",
              "तथापि, स्थूल, उपयोग, अन्यत्र, उपदेक्ष्यन्ते.", role="extend",
              teaches="यथा- before a noun means 'according to': यथास्थूलम् = according to the gross (outline), "
                      "यथोपयोगम् = according to use."),
        mcq("discriminate", 3, "Which split of यथोपयोगं is right?",
            ("यथा + उपयोगम्", "आ + उ → ओ: यथा + उपयोगम् → यथोपयोगम्."),
            [("यथा + अपयोगम्", "आ + अ would give आ (यथापयोगम्), not ओ."),
             ("यथो + पयोगम्", "Neither यथो nor पयोगम् is a word here."),
             ("यथाः + उपयोगम्", "A visarga after आ is dropped before a vowel; no ओ would arise.")],
            "यथा (according to) + उपयोगम् (use) → यथोपयोगम्.",
            "आ + उ → ओ."),
        mcq("apply", 4, "In unit 219, what does the form उपदेक्ष्यन्ते tell about the teaching of the sirā and the rest?",
            ("It is still to come, later", "उपदेक्ष्यन्ते is a future passive: they will be taught."),
            [("It was given in an earlier line", "The form is future, not past."),
             ("It is being given in this line", "The line gives no teaching on sirā; it points ahead."),
             ("It is forbidden to give at all", "Nothing forbids it; the form says it will be done.")],
            "उपदेक्ष्यन्ते (3 pl. fut. pass. उप-√दिश्) = they will be taught.",
            "उपदेक्ष्यन्ते = will be taught (future)."),
        mcq("transfer", 5, "By the rule of यथा + उपयोगम् → यथोपयोगम्, how is महा + उत्सवः (a great festival) joined?",
            ("महोत्सवः", "आ + उ → ओ, as यथा + उपयोगम्."),
            [("महौत्सवः", "औ comes from अ/आ + ओ or औ, not from आ + उ."),
             ("महात्सवः", "The उ is not lost; आ + उ gives ओ."),
             ("महुत्सवः", "The आ is not lost; आ + उ gives ओ.")],
            "महा + उत्सवः = महोत्सवः, like यथा + उपयोगम् = यथोपयोगम्.",
            "आ + उ → ओ.",
            teaches="आ followed by उ joins as ओ: यथा + उपयोगम् → यथोपयोगम्."),
    ],
}

# ---------------------------------------------------------------- unit 220
AUTHORED["220"] = {
    "title": "इत्येवं परिसंख्याता शरीरे",
    "question": "By unit 220, what has now been enumerated in the body?",
    "rule": ("Thus (इति एवम्) the corporeal entities (मूर्तिमन्तः भावाः, entities having form) in the body (शरीरे) have "
             "been enumerated (परिसंख्याताः); the data reads them as firm (स्थिराः)."),
    "limits": ("A prose line. The printed मूर्त्ति मंतःस्थिरा is read मूर्तिमन्तः स्थिराः ('firm'); मूर्तिमन्तोऽस्थिराः "
               "('not firm') is also possible: no question on firm or not firm. The printed परिसंख्याता probably lost its "
               "visarga (flag): no question on that form."),
    "explain_hi": ("यह गद्य-पंक्ति एक गिनती को समाप्त करती है: ‘इत्येवम्’ यानी इस प्रकार। "
                   "शरीर में जो मूर्तिमान भाव हैं, यानी जिनका ठोस रूप है, वे गिनाए जा चुके (परिसंख्याताः)। "
                   "छपे ‘मूर्त्ति मंतःस्थिरा’ को डेटा ‘मूर्तिमन्तः स्थिराः’ (स्थिर) पढ़ता है; ‘मूर्तिमन्तोऽस्थिराः’ (अस्थिर) भी सम्भव है, इसलिए यह बात खुली है। "
                   "डेटा के अनुसार इनके सामने अगली इकाई (२२१) के द्रव रखे गए हैं। "
                   "‘-मत्’ प्रत्यय का अर्थ है ‘वाला’: मूर्तिमत् = रूप वाला।"),
    "hook": "मूर्तिमान भाव गिन लिए; अब द्रवों की बारी।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 220, what has been done with the corporeal entities (भाव) in the body?",
            ("They have been enumerated", "परिसंख्याताः: enumerated, counted out."),
            [("They will be taught elsewhere", "Teaching elsewhere is said of the sirā and the rest in unit 219."),
             ("They are said to be countless", "'Countless' is said of the srotas in unit 218."),
             ("They are measured in handfuls", "The handful measures belong to the fluids of units 222 to 226.")],
            "इत्येवं परिसंख्याताः शरीरे मूर्तिमन्तः … भावाः: thus the corporeal entities have been enumerated.",
            "परिसंख्याताः = enumerated."),
        order(1, "Put these printed parts of unit 220 in the line's order.",
              ["इत्येवं", "परिसंख्याता", "शरीरे", "मूर्त्ति मंतःस्थिरा", "भावाः"],
              "Thus enumerated, in the body, the corporeal (firm, as read) entities.",
              "इत्येवम् → परिसंख्याताः → शरीरे → मूर्तिमन्तः … → भावाः."),
        match(2, "Match each word of unit 220 to its meaning.",
              [["इति", "thus"], ["परिसंख्यात", "enumerated"], ["शरीर", "body"], ["मूर्तिमत्", "having form, corporeal"],
               ["भाव", "entity, factor"]],
              "Thus the corporeal entities in the body have been enumerated.",
              "इति, परिसंख्यात, शरीर, मूर्तिमत्, भाव.", role="extend",
              teaches="-मत् (nominative plural -मन्तः) means 'having': मूर्तिमत् = having form (मूर्ति)."),
        mcq("discriminate", 3, "Which split of इत्येवं is right?",
            ("इति + एवम्", "इ before a different vowel becomes य्: इति + एवम् → इत्येवम्."),
            [("इत्य + एवम्", "इत्य is not a word; the य् is the changed इ of इति."),
             ("इती + एवम्", "इति has a short इ; ई + ए would also give ये, but इती is not the word."),
             ("इति + इवम्", "इ + इ would give ई (इतीवम्), not ये.")],
            "इति (thus) + एवम् (so) → इत्येवम्.",
            "इ + a different vowel → य्."),
        mcq("apply", 4, "If मूर्तिमन्तः means 'having form', what kind of entities (भावाः) does unit 220 close?",
            ("Those with a bodily form", "मूर्ति (form) + -मत् (having): entities that have form."),
            [("Those with no form at all", "That would be अमूर्त; unit 220 says मूर्तिमन्तः."),
             ("Those of the mind alone", "The mind is not named; the entities are 'in the body', with form."),
             ("Those that are liquids", "The liquids (द्रव) are taken up in unit 221, after this close.")],
            "मूर्तिमन्तः भावाः = entities having form, in the body.",
            "मूर्तिमत् = having form."),
        mcq("transfer", 5, "By the pattern of मूर्तिमत् (having form), what does a new example बुद्धिमान् पुरुषः mean?",
            ("A man having intellect", "-मत् means 'having', as मूर्तिमत् = having form."),
            [("A man without intellect", "'Without' would need अ- or निर्-; -मत् means 'having'."),
             ("The intellect of a man", "That would be पुरुषस्य बुद्धिः; बुद्धिमान् describes the man."),
             ("A man made of intellect", "'Made of' would be -मय; -मत् means 'having'.")],
            "बुद्धि + -मत् → बुद्धिमान् (nom. sg. m.): having intellect, like मूर्ति + -मत् = having form.",
            "X + -मत् = having X.",
            teaches="-मत् after a noun means 'having it': मूर्तिमत् = having form; nom. pl. मूर्तिमन्तः."),
    ],
}

# ---------------------------------------------------------------- unit 221
AUTHORED["221"] = {
    "title": "द्रवास्तु",
    "question": "By unit 221, which group is taken up next, and what is named with it?",
    "rule": ("As for the liquids (द्रवाः तु): the line speaks of what, falling away through excess (अतियोगेन च्यवमानम्), "
             "binds on to (अनुबध्नाति) the dung (पुरीष), and likewise the urine, the blood and the other dhātus in the body."),
    "limits": ("A prose line, low confidence; it runs on into unit 222. The syntax is unclear: no antecedent for यत् तत्, "
               "no stated subject, and च्यवमानम् may go with the dung instead: no question asks what falls away or "
               "what binds. The printed अन्यांच (for अन्यांश्च) is flagged."),
    "explain_hi": ("यह गद्य-पंक्ति मूर्तिमान भावों (इकाई २२०) के बाद द्रवों (द्रवाः) पर आती है; ‘तु’ यहाँ ‘अब, परन्तु’ का भाव देता है। "
                   "पंक्ति शब्दशः कहती है: जो अतियोग से च्युत होता हुआ पुरीष यानी मल को बाँधता है, वैसे ही मूत्र, रुधिर और शरीर के अन्य धातुओं को। "
                   "वाक्य की बनावट स्पष्ट नहीं: ‘यत् तत्’ किसकी ओर है, कर्ता कौन है, और ‘च्यवमानम्’ द्रव के साथ है या मल के साथ, तय नहीं। "
                   "डेटा के अनुसार वाक्य इकाई २२२ में आगे चलता है, जहाँ उदक की परिभाषा है। "
                   "इसलिए प्रश्न केवल इकाई में नामित वस्तुओं और शब्दों पर हैं।"),
    "hook": "अब द्रव: मल, मूत्र, रुधिर और अन्य धातुओं के साथ।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "After the corporeal entities, which group does unit 221 take up?",
            ("The liquids (द्रवाः)", "द्रवास्तु: as for the liquids."),
            [("The channels (स्रोतांसि)", "The srotas were called countless in unit 218."),
             ("The body-hairs (लोमानि)", "The hairs are spoken of in unit 215."),
             ("The bones (अस्थीनि)", "The bones were counted much earlier, from unit 100.")],
            "द्रवाः तु: as for the liquids.",
            "द्रवाः = the liquids."),
        order(1, "Put the things named in unit 221 in the line's order.",
              ["पुरीष (मल)", "मूत्र", "रुधिर", "अन्य धातु"],
              "Dung; likewise urine, blood and the other dhātus in the body.",
              "पुरीषम् → मूत्रम् → रुधिरम् → अन्यान् धातून्."),
        match(2, "Match each word of unit 221 to its meaning.",
              [["द्रव", "liquid"], ["अतियोग", "excess"], ["पुरीष", "dung"], ["मूत्र", "urine"], ["रुधिर", "blood"]],
              "The liquids; through excess; the dung, urine, blood and other dhātus.",
              "द्रव, अतियोग, पुरीष, मूत्र, रुधिर.", role="extend",
              teaches="अनुबध्नाति (अनु-√बन्ध्) = binds on to, attaches; its objects here are in the accusative (-म्, -आन्)."),
        mcq("discriminate", 3, "Which split of द्रवास्तु is right?",
            ("द्रवाः + तु", "A visarga before त becomes स्: द्रवाः + तु → द्रवास्तु."),
            [("द्रवः + अस्तु", "अः + अ would give ओऽ (द्रवोऽस्तु), not आस्."),
             ("द्रवाः + अस्तु", "A visarga after आ is dropped before a vowel (द्रवा अस्तु)."),
             ("द्रवास्त + उ", "द्रवास्त is not a word; the word is द्रवाः.")],
            "द्रवाः (liquids) + तु (as for) → द्रवास्तु.",
            "Visarga + त → स्."),
        multi("apply", 4, "Which of these does unit 221 name?",
              [("Urine (मूत्र)", "Right: तथा मूत्रम्, likewise the urine."),
               ("Head-hair (केश)", "Head-hair is named in unit 215, not in unit 221."),
               ("Brain (मस्तिष्क)", "The brain is named in unit 224, not in unit 221."),
               ("Blood (रुधिर)", "Right: रुधिरम् follows मूत्रम्.")],
              [0, 3],
              "Unit 221 names the dung, urine, blood and the other dhātus.",
              "पुरीषम् … मूत्रं रुधिरम् अन्यान् … धातून्."),
        mcq("transfer", 5, "By the rule of द्रवाः + तु → द्रवास्तु, how is नराः + तत्र (the men there) joined?",
            ("नरास्तत्र", "A visarga before त becomes स्, as द्रवाः + तु."),
            [("नरा तत्र", "The visarga after आ is dropped only before a voiced sound; त is not voiced."),
             ("नरोस्तत्र", "आ does not turn into ओ; only the visarga changes."),
             ("नराश्तत्र", "श् stands before च/छ/श; before त the visarga becomes स्.")],
            "नराः + तत्र = नरास्तत्र, like द्रवाः + तु = द्रवास्तु.",
            "Visarga + त/थ → स्.",
            teaches="A visarga before त or थ becomes स्: द्रवाः + तु → द्रवास्तु."),
    ],
}

# ---------------------------------------------------------------- unit 222
AUTHORED["222"] = {
    "title": "तदुदकं: उदक के रूप और द्रवों की अंजलि",
    "question": "By unit 222, what three forms make up udaka (water), and which fluids are then measured by the añjali?",
    "rule": ("Udaka is what has gone through the whole body, held by the outer skin; what, within the skin, gone to a wound, "
             "is called lasīkā; and what flows from the hair-pores as sweat. Udaka, rasa, blood, dung, śleṣman, pitta, urine, "
             "vasā, medas and marrow each have their own añjali measure."),
    "limits": ("A long prose line, low confidence; the clauses are loosely joined. No number is printed for any fluid: the "
               "rising series 'beginning with one' is only a probable reading, so no question asks a fluid's number. "
               "Lasīkā (lymph), vasā, medas and marrow keep the data's 'probable' label."),
    "explain_hi": ("यह लम्बी गद्य-पंक्ति इकाई २२१ के द्रवों की बात आगे बढ़ाती है। "
                   "पहले तीन ‘यत्’ वाक्य: जो पूरे शरीर में फैला है और जिसे बाहरी त्वचा धारण करती है; जो त्वचा के भीतर घाव में ‘लसीका’ (सम्भवतः लसीका-द्रव) कहलाता है; "
                   "और जो ऊष्मा से बँधा रोमकूपों से निकलता ‘स्वेद’ (पसीना) कहलाता है: वह उदक यानी जल है। "
                   "फिर क्रम से: उदक, रस (आहार का सार), रक्त, शकृत् (मल), श्लेष्मन्, पित्त (यहाँ शरीर का द्रव), मूत्र, वसा, मेदस् और मज्जा, हर एक की अपनी-अपनी अंजलि (अंजुलि भर) का माप। "
                   "पंक्ति ‘पूर्व के अनुसार एक से आरम्भ होकर संख्या की वृद्धि’ कहती है, पर किसी की संख्या छपी नहीं; हर स्तर पर एक-एक बढ़ना केवल सम्भावित अर्थ है। "
                   "इसलिए किसी द्रव की संख्या पर प्रश्न नहीं।"),
    "hook": "शरीर भर में (त्वचा थामे), घाव में, पसीने में: तीनों उदक; फिर दस द्रव अपनी-अपनी अंजलि से नपे।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 222, what is the fluid called that, bound with heat, flows out of the hair-pores?",
            ("Sweat (स्वेद)", "स्वेदवाच्यम्: called sweat."),
            [("Lasīkā (लसीका)", "Lasīkā is the name of the fluid in a wound, within the skin."),
             ("Rasa (रस)", "Rasa is the essence of food, the first measured after udaka."),
             ("Urine (मूत्र)", "Urine is one of the fluids measured; it does not come from the pores.")],
            "यच्चोष्मणाऽनुबद्धं रोमकूपेभ्योऽभिनिष्पतत् स्वेदवाच्यम्: bound with heat, flowing from the hair-pores, called sweat.",
            "रोमकूप → स्वेद."),
        order(1, "Put the first six fluids measured in unit 222 in the line's order.",
              ["उदक", "रस", "रक्त", "शकृत्", "श्लेष्मन्", "पित्त"],
              "Water, rasa (essence of food), blood, dung, śleṣman, pitta; then urine, vasā, medas and marrow follow.",
              "उदक → रस → रक्त → शकृत् → श्लेष्मन् → पित्त."),
        match(2, "Match each term of unit 222 to what the line says of it.",
              [["लसीका", "the name of the fluid in a wound"], ["स्वेद", "flows out of the hair-pores"],
               ["रस", "the essence of food"], ["शकृत्", "dung"], ["मूत्र", "urine"]],
              "Lasīkā is the wound fluid, sweat flows from the pores, rasa is the essence of food; dung and urine are measured too.",
              "लसीका, स्वेद, रस, शकृत्, मूत्र.", role="extend",
              teaches="-आख्य at the end of a compound means 'named': रसाख्य = named rasa; -वाच्य = to be called: स्वेदवाच्य."),
        mcq("discriminate", 3, "Unit 222 speaks of 'an increase of number beginning with one'. Which fluid's own number does it print?",
            ("None: no fluid's number is printed", "The data: the measure of each substance is not stated numerically."),
            [("Sweat's, printed as three añjali", "Sweat is a form of udaka; no number is printed for it or any fluid."),
             ("Every fluid's, as one añjali", "The line speaks of an increase, so they are not all alike."),
             ("Rasa's, printed as half an añjali", "Half an añjali is said of śukra in unit 223, not here.")],
            "Only 'each by its own añjali measure ... an increase of number beginning with one' is printed.",
            "No numbers are printed in unit 222."),
        multi("apply", 4, "By unit 222, which of these are called udaka (water)?",
              [("What is named rasa", "Rasa, the essence of food, is measured next to udaka; it is not one of its forms."),
               ("What is called sweat", "Right: the fluid from the hair-pores called sweat is udaka."),
               ("What is called marrow", "Marrow (majjan) is the last fluid measured, not a form of udaka."),
               ("What is called lasīkā", "Right: the fluid in a wound called lasīkā is udaka.")],
              [1, 3],
              "The three 'yat' clauses (through the whole body, held by the outer skin; lasīkā; sweat) together are udaka.",
              "यच्च … यच्च … यच्च … तदुदकम्."),
        mcq("transfer", 5, "By the pattern of व्रणगतम् (gone to a wound), what does a new example हृदयगतम् mean?",
            ("Situated in the heart", "-गत = gone to, situated in, as व्रणगत = gone to a wound."),
            [("Made out of the heart", "'Made of' would be -मय; -गत means gone to, situated in."),
             ("Larger than the heart", "-गत makes no comparison."),
             ("Measured by the heart", "A measure would be -प्रमाण, as in अञ्जलिप्रमाण.")],
            "हृदय + -गत = gone into, situated in the heart, like व्रण + -गत = gone to a wound.",
            "X-गत = gone to / situated in X.",
            teaches="-गत at the end of a compound means 'gone to, situated in': सर्वशरीरगत, व्रणगत."),
    ],
}

# ---------------------------------------------------------------- unit 223
AUTHORED["223"] = {
    "title": "अर्द्धंजलिःशुक्रस्य",
    "question": "By unit 223, what is the measure of śukra (semen)?",
    "rule": "Half a cupped handful (अर्ध-अञ्जलिः) of śukra (शुक्रस्य, semen, standard): a measure in the series of unit 222.",
    "limits": ("A short prose line with no verb. The printed अर्द्धंजलिः is read अर्ध-अञ्जलिः (lost आ and space taken as print "
               "slips; text_flag: possible): no question on that printed form or its join. The line does not say for whom the "
               "measure holds."),
    "explain_hi": ("यह छोटी गद्य-पंक्ति इकाई २२२ के अंजलि-माप की श्रृंखला को आगे बढ़ाती है। "
                   "शुक्र यानी वीर्य की आधी अंजलि (अंजुलि भर का आधा)। "
                   "पंक्ति में क्रिया नहीं; ‘है’ समझा जाता है। "
                   "‘शुक्रस्य’ षष्ठी है: किसका माप, शुक्र का। "
                   "छपा ‘अर्द्धंजलिः’ डेटा में ‘अर्ध + अञ्जलिः’ पढ़ा गया है; आ का छूटना और जगह न होना सम्भवतः छपाई की चूक है (पाठ-चिह्न: सम्भावित)।"),
    "hook": "शुक्र: आधी अंजलि।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 223, how much śukra (semen) is there?",
            ("Half a cupped handful", "अर्द्धंजलिः शुक्रस्य (read अर्ध-अञ्जलिः): half an añjali of śukra."),
            [("Four cupped handfuls", "Four añjali is said of rajas in women, in unit 225."),
             ("Two cupped handfuls", "Two is said of breast milk, in unit 226."),
             ("Eight cupped handfuls", "No such measure is given for śukra.")],
            "Half a cupped handful (añjali) of śukra.",
            "अर्ध-अञ्जलिः शुक्रस्य."),
        match(1, "Match each word of unit 223 to its meaning.",
              [["अर्ध", "half"], ["अञ्जलि", "cupped handful"], ["शुक्र", "semen"]],
              "Half a cupped handful of śukra (semen).",
              "अर्ध, अञ्जलि, शुक्र."),
        fill(2, "Unit 223 measures śukra by half a cupped handful. Type its Sanskrit word for 'half': ____ (Devanagari or English letters, e.g. veda).",
             accepts("अर्ध", "ardha", "अर्द्ध", "arddha"),
             "अर्ध (half) + अञ्जलिः (cupped handful); the print doubles the द (अर्द्ध).",
             "अर्ध = half; अर्ध-अञ्जलि = half a cupped handful.",
             "अर्ध = half."),
        mcq("discriminate", 3, "Unit 223 has no verb. Which rendering of it is right?",
            ("Half a cupped handful of śukra", "A measure in the series: 'is' is understood."),
            [("Half of the śukra fills a hand", "The half is of the añjali, not of the śukra."),
             ("A handful of śukra is halved", "Nothing is said to be halved; अर्ध is part of the measure."),
             ("Śukra is half of the body", "The body is not mentioned; the line gives a handful measure.")],
            "अर्ध-अञ्जलिः (half a cupped handful) + शुक्रस्य (of śukra).",
            "अर्ध-अञ्जलिः शुक्रस्य = half an añjali of śukra."),
        mcq("apply", 4, "Unit 223 continues the series of unit 222. In what unit of measure is śukra given?",
            ("In añjali, cupped handfuls", "अञ्जलि, the measure of each fluid in unit 222."),
            [("In aṅguli, finger-breadths", "Finger-breadths are not the measure used for these fluids."),
             ("In bindu, single drops", "Drops are not mentioned; the measure is the añjali."),
             ("In pala, units of weight", "No weight is given; the measure is the añjali.")],
            "Each fluid is measured by its own añjali; śukra by half an añjali.",
            "अञ्जलि = the measure of the fluids."),
        mcq("transfer", 5, "By the pattern of अर्ध-अञ्जलिः शुक्रस्य, what does a new example अर्धाञ्जलिस्तैलस्य mean?",
            ("Half a cupped handful of oil", "The genitive names what is measured, as शुक्रस्य."),
            [("Oil filling half the body", "The body is not named; अर्धाञ्जलि is a handful measure."),
             ("Two cupped handfuls of oil", "अर्ध means half, not two."),
             ("Half the oil kept in a hand", "The half goes with the handful (अर्ध-अञ्जलि), not with the oil.")],
            "अर्धाञ्जलिः + तैलस्य → अर्धाञ्जलिस्तैलस्य (visarga + त → स्): half a cupped handful of oil.",
            "Measure (nom.) + substance (gen.) = so much of it.",
            teaches="A measure word with a genitive gives 'so much of X': अर्ध-अञ्जलिः शुक्रस्य = half an añjali of śukra."),
    ],
}

# ---------------------------------------------------------------- unit 224
AUTHORED["224"] = {
    "title": "तावदेव मस्तिष्क मोजश्च",
    "question": "By unit 224, which two are given 'that much only'?",
    "rule": "That much only (तावत् एव): the brain (मस्तिष्क, standard) and ojas (ओजस्, vital essence).",
    "limits": ("A short prose line with no verb. 'That much' points back to the measure before it; the data reads it as half "
               "an añjali, as in unit 223, but the line does not say so: no question on the amount. Ojas is a doctrinal "
               "term with no modern equivalent."),
    "explain_hi": ("यह छोटी गद्य-पंक्ति माप की श्रृंखला में दो और नाम जोड़ती है: मस्तिष्क और ओज। "
                   "‘तावदेव’ = उतना ही; डेटा इसे इकाई २२३ वाली आधी अंजलि मानता है, पर पंक्ति यह नहीं लिखती। "
                   "ओज शास्त्रीय शब्द है (जीवन का सार); कोई आधुनिक पर्याय नहीं रखा गया। "
                   "छपा ‘मस्तिष्क मोजश्च’ = मस्तिष्कम् ओजः च; म् अगले शब्द के साथ छपा है।"),
    "hook": "मस्तिष्क और ओज: उतना ही।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 224, which two are given 'that much only' (तावदेव)?",
            ("The brain and ojas", "मस्तिष्कम् ओजश्च: the brain and ojas."),
            [("Milk and rajas", "Rajas and breast milk come in units 225 and 226."),
             ("Urine and blood", "Urine and blood are among the fluids of unit 222."),
             ("Sweat and lasīkā", "Sweat and lasīkā are forms of udaka in unit 222.")],
            "तावदेव मस्तिष्कमोजश्च: that much only, the brain and ojas.",
            "मस्तिष्कम्, ओजः."),
        order(1, "Put the words of unit 224 in the line's order.",
              ["तावत्", "एव", "मस्तिष्कम्", "ओजः", "च"],
              "That much only: the brain and ojas.",
              "तावत् → एव → मस्तिष्कम् → ओजः → च."),
        match(2, "Match each word of unit 224 to its meaning.",
              [["तावत्", "so much"], ["एव", "only, exactly"], ["मस्तिष्क", "brain"], ["ओजस्", "vital essence (ojas)"]],
              "That much only: the brain and ojas.",
              "तावत्, एव, मस्तिष्क, ओजस्.", role="extend",
              teaches="तावत् = so much, pointing back to a measure already given; with एव: that much only."),
        mcq("discriminate", 3, "Which split of the printed मस्तिष्क मोजश्च is right?",
            ("मस्तिष्कम् + ओजः + च", "The म् of मस्तिष्कम् is printed with the next word; ओजः + च → ओजश्च."),
            [("मस्तिष्क + मोजः + च", "मोजः is not a word; the म् belongs to मस्तिष्कम्."),
             ("मस्तिष्कम् + ओज + श्च", "श्च is not a word; श् is the changed visarga of ओजः."),
             ("मस्तिष्कम् + ओजः + अश्च", "अश्च is not a word here; the line ends in च, and.")],
            "मस्तिष्कम् (brain) + ओजः (ojas) + च (and); visarga + च → श्.",
            "Visarga + च → श्."),
        mcq("apply", 4, "In तावदेव, what does एव add to तावत् (so much)?",
            ("Exactly that much, the same", "एव = only, exactly: that much and no other."),
            [("Twice that much, doubled", "Nothing doubles the amount; एव only stresses it."),
             ("Less than that, a little", "एव does not reduce the amount."),
             ("Not that much, none at all", "एव is not a negation.")],
            "तावत् एव = that much only.",
            "एव = only, exactly."),
        mcq("transfer", 5, "By the rule of तावत् + एव → तावदेव, how is यावत् + एव (as much as) joined?",
            ("यावदेव", "A final त् before a vowel becomes द्, as तावत् + एव."),
            [("यावतेव", "The त् does not stay unvoiced before a vowel; it becomes द्."),
             ("यावन्नेव", "न्न् comes (optionally) from त् before a nasal, not before a vowel."),
             ("यावच्चेव", "च्च् comes from त् before च, not before a vowel.")],
            "यावत् + एव = यावदेव, like तावत् + एव = तावदेव.",
            "Final त् + vowel → द्.",
            teaches="A final त् before a vowel becomes द्: तावत् + एव → तावदेव."),
    ],
}

# ---------------------------------------------------------------- unit 225
AUTHORED["225"] = {
    "title": "स्त्रीणां रजसोऽजल्यश्चतस्रः",
    "question": "By unit 225, what measure of rajas is given for women?",
    "rule": ("In women (स्त्रीणाम्), four (चतस्रः) cupped handfuls (अञ्जल्यः) of rajas (रजसः, menstrual blood, probably)."),
    "limits": ("A short prose line with no verb. Rajas as menstrual blood is a probable identification. The printed अजल्यः "
               "is read अञ्जल्यः (nasal dropped in print, flagged): no question rests on the printed form."),
    "explain_hi": ("यह छोटी गद्य-पंक्ति स्त्रियों के लिए एक माप देती है: रजस् की चार अंजलियाँ। "
                   "रजस् यहाँ सम्भवतः मासिक धर्म का रक्त है (सम्भावित पहचान)। "
                   "‘चतस्रः’ (चार) स्त्रीलिङ्ग है, इसलिए यहाँ अंजलि स्त्रीलिङ्ग (अञ्जल्यः) पढ़ी गई है। "
                   "छपे ‘अजल्यः’ में ञ् छूटा है; डेटा इसे अञ्जल्यः पढ़ता है।"),
    "hook": "स्त्रियों में रजस्: चार अंजलि।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 225, how many cupped handfuls of rajas are there in women?",
            ("Four (चतस्रः)", "अञ्जल्यश्चतस्रः: four cupped handfuls."),
            [("Two (द्वौ)", "Two is said of breast milk in unit 226."),
             ("Half (अर्ध)", "Half is said of śukra in unit 223."),
             ("Eight (अष्टौ)", "Eight is not the measure given for rajas.")],
            "स्त्रीणां रजसः अञ्जल्यः चतस्रः: four añjali of rajas in women.",
            "चतस्रः = four."),
        match(1, "Match each word of unit 225 to its meaning.",
              [["स्त्री", "woman"], ["रजस्", "menstrual blood (probably)"], ["अञ्जलि", "cupped handful"],
               ["चतस्रः", "four (feminine)"]],
              "In women, four cupped handfuls of rajas.",
              "स्त्री, रजस्, अञ्जलि, चतस्रः."),
        fill(2, "Complete unit 225: रजसोऽजल्यः (read …ञ्जल्यः) ____ (four, feminine). Type it in Devanagari or English letters (e.g. tri).",
             accepts("चतस्रः", "catasraḥ", "chatasrah", "chatasra"),
             "अञ्जल्यः चतस्रः: four cupped handfuls; चतस्रः is the feminine of 'four'.",
             "चतस्रः = four, feminine nominative plural, agreeing with अञ्जल्यः.",
             "चतस्रः = four (feminine)."),
        mcq("discriminate", 3, "Why is the numeral चतस्रः (four) feminine in unit 225?",
            ("It agrees with अञ्जल्यः (handfuls)", "Both are feminine nominative plural; añjali is read feminine here."),
            [("It agrees with स्त्रीणाम् (of women)", "स्त्रीणाम् is genitive; चतस्रः is nominative, so they do not agree."),
             ("It agrees with रजसः (of rajas)", "रजसः is neuter genitive singular; it cannot agree with चतस्रः."),
             ("All numerals here are feminine", "द्वौ in unit 226 is masculine, so not all are feminine.")],
            "चतस्रः (f. nom. pl.) agrees with अञ्जल्यः (f. nom. pl.).",
            "A numeral agrees with its noun in gender, case and number."),
        mcq("apply", 4, "A learner renders unit 225 as: In women, four handfuls of semen. Which word of it is wrong?",
            ("semen", "रजस् is rajas (menstrual blood, probably); semen is śukra (unit 223)."),
            [("women", "स्त्रीणाम् = of women, in women: right."),
             ("four", "चतस्रः = four: right."),
             ("handfuls", "अञ्जल्यः = cupped handfuls: right.")],
            "The line is about rajas, not śukra.",
            "रजस् ≠ शुक्र."),
        mcq("transfer", 5, "By the rule of रजसः + अ… → रजसोऽ…, how is शिष्यः + अयम् (this pupil) joined?",
            ("शिष्योऽयम्", "अः before अ becomes ओ and the अ is marked by ऽ, as रजसः + अ… → रजसोऽ…."),
            [("शिष्यायम्", "अः does not give आ; before अ it gives ओऽ."),
             ("शिष्य अयम्", "The visarga is dropped like this only before vowels other than अ."),
             ("शिष्यरयम्", "र् comes from a visarga after vowels other than अ/आ.")],
            "शिष्यः + अयम् = शिष्योऽयम्, like रजसः + अ… = रजसोऽ….",
            "अः + अ → ओऽ.",
            teaches="अः before अ becomes ओ and the अ drops, marked ऽ: रजसः + अञ्जल्यः → रजसोऽञ्जल्यः."),
    ],
}

# ---------------------------------------------------------------- unit 226
AUTHORED["226"] = {
    "title": "स्तन्यस्य द्वौ",
    "question": "By unit 226, what number is given for breast milk (stanya)?",
    "rule": "Of breast milk (स्तन्यस्य), two (द्वौ): the measure (añjali) is understood from the line before.",
    "limits": ("A two-word prose line with no verb and no measure word; the data takes añjali as understood. द्वौ is "
               "masculine, unlike the feminine चतस्रः of unit 225; the data only notes this, so no question asks why."),
    "explain_hi": ("यह दो शब्दों की गद्य-पंक्ति है: स्तन्य यानी स्तन के दूध के दो। "
                   "माप का शब्द (अंजलि) नहीं लिखा; डेटा के अनुसार इकाई २२५ से समझा जाता है। "
                   "‘द्वौ’ पुंलिङ्ग द्विवचन है, जबकि इकाई २२५ का ‘चतस्रः’ स्त्रीलिङ्ग था; यह भेद केवल दर्ज है, कारण नहीं बताया। "
                   "‘स्तन्यस्य’ षष्ठी है: किसका माप, स्तन्य का।"),
    "hook": "स्तन का दूध: दो।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 226, what number is given for breast milk (स्तन्य)?",
            ("Two (द्वौ)", "स्तन्यस्य द्वौ: of breast milk, two."),
            [("Four (चतस्रः)", "Four is said of rajas in unit 225."),
             ("Half (अर्ध)", "Half is said of śukra in unit 223."),
             ("Countless (असंख्येय)", "Countless is said of the srotas in unit 218.")],
            "स्तन्यस्य द्वौ: two of breast milk.",
            "द्वौ = two."),
        mcq("warmup", 1, "What does स्तन्य mean in unit 226?",
            ("Breast milk", "स्तन्य = what belongs to the breast (स्तन): breast milk."),
            [("The breast itself", "The breast is स्तन; स्तन्य is the milk of it."),
             ("Menstrual blood", "That is rajas, in unit 225."),
             ("Semen", "That is śukra, in unit 223.")],
            "स्तन्य = breast milk.",
            "स्तन्य = breast milk."),
        fill(2, "Complete unit 226: स्तन्यस्य ____ (two). Type it in Devanagari or English letters (e.g. eka).",
             accepts("द्वौ", "dvau", "dwau"),
             "स्तन्यस्य द्वौ: of breast milk, two.",
             "द्वौ = two (masculine nominative dual).",
             "द्वौ = two."),
        mcq("discriminate", 3, "In unit 226, why is स्तन्यस्य in the genitive (-स्य)?",
            ("It names whose measure is given", "स्तन्यस्य द्वौ: two (handfuls) of breast milk."),
            [("It is the subject that acts", "No verb and no action: the genitive names the substance."),
             ("It names the place of the milk", "A place would be locative (-ए); -स्य is genitive."),
             ("It names who receives the milk", "A receiver would be dative (-आय); -स्य is genitive.")],
            "The genitive names what the number measures: of breast milk.",
            "स्तन्यस्य = of breast milk."),
        multi("apply", 4, "Which of these are true of unit 226?",
              [("It has a verb of its own", "There is no verb in the line."),
               ("It names breast milk", "Right: स्तन्यस्य, of breast milk."),
               ("It gives the number two", "Right: द्वौ, two."),
               ("It prints the word अञ्जलि", "No measure word is printed; the data takes it as understood.")],
              [1, 2],
              "Unit 226 is only स्तन्यस्य द्वौ: breast milk, two.",
              "स्तन्यस्य द्वौ."),
        mcq("transfer", 5, "By the pattern of द्वौ (two, masculine dual), which new phrase means two hands (हस्त, masculine)?",
            ("द्वौ हस्तौ", "Masculine द्वौ with the dual हस्तौ."),
            [("द्वे हस्तौ", "द्वे is the feminine/neuter form; हस्त is masculine."),
             ("द्वौ हस्ताः", "हस्ताः is plural; with two the noun is dual."),
             ("द्वौ हस्तः", "हस्तः is singular; with two the noun is dual.")],
            "द्वौ हस्तौ: two hands, masculine dual.",
            "Two + masculine noun → द्वौ + dual.",
            teaches="द्वौ is the masculine nominative dual of 'two'; its noun is also dual: द्वौ हस्तौ."),
    ],
}

# ---------------------------------------------------------------- unit 227
AUTHORED["227"] = {
    "title": "उभयमपि चैतद्रसप्रसादात्मकमिति",
    "question": "By unit 227, of what nature are 'both of these'?",
    "rule": ("And both of these as well (उभयम् अपि च एतत्) are of the nature of the clear essence (प्रसाद) of rasa "
             "(रसप्रसादात्मकम्); इति closes the statement."),
    "limits": ("A short prose line; the copula is understood. Which two 'both' means is not stated (the data reads rajas and "
               "breast milk of units 225 and 226): no question asks it. इति is a closing particle, not translated."),
    "explain_hi": ("यह गद्य-पंक्ति कहती है कि ये दोनों भी रस के प्रसाद यानी स्वच्छ सार के स्वरूप हैं। "
                   "‘उभयम्’ = दोनों; पंक्ति नहीं बताती कौन-से दो, डेटा इन्हें इकाई २२५-२२६ के रजस् और स्तन्य मानता है। "
                   "‘रसप्रसादात्मकम्’ = रस का प्रसाद (स्वच्छ, सूक्ष्म भाग) जिसका स्वरूप है। "
                   "रस इकाई २२२ में ‘आहार का सार’ कहा गया है। "
                   "‘इति’ कथन समाप्त करता है।"),
    "hook": "दोनों: रस का स्वच्छ सार।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 227, of what nature are 'both of these'?",
            ("Of the clear essence of rasa", "रसप्रसादात्मकम्: of the nature of rasa's clear essence."),
            [("Of the waste part of rasa", "प्रसाद is the clear essence, not a waste."),
             ("Of the heat of the body", "Heat (ऊष्मन्) is named in unit 222, not here."),
             ("Of the essence of marrow", "Marrow is not named in unit 227; the line names rasa.")],
            "उभयमपि चैतद्रसप्रसादात्मकम्: both are of the nature of rasa's clear essence.",
            "रसप्रसादात्मकम्."),
        order(1, "Put these words of unit 227 in the line's order.",
              ["उभयम्", "अपि", "एतत्", "रसप्रसादात्मकम्", "इति"],
              "Both, as well, this, of the nature of rasa's clear essence, thus.",
              "उभयम् → अपि → (च) एतत् → रसप्रसादात्मकम् → इति."),
        match(2, "Match each word of unit 227 to its meaning.",
              [["उभय", "both"], ["अपि", "also, as well"], ["प्रसाद", "clear essence"], ["आत्मक", "having the nature of"]],
              "Both of these as well are of the nature of the clear essence of rasa.",
              "उभय, अपि, प्रसाद, आत्मक.", role="extend",
              teaches="-आत्मक at the end of a compound means 'having X as its nature': रसप्रसादात्मक."),
        mcq("discriminate", 3, "Which split of चैतद्रसप्रसादात्मकम् is right?",
            ("च + एतत् + रसप्रसादात्मकम्", "अ + ए → ऐ (चैतत्); त् before the voiced र becomes द्."),
            [("च + इतत् + रसप्रसादात्मकम्", "अ + इ gives ए, not ऐ; and इतत् is not a word."),
             ("चैत + द्रसप्रसादात्मकम्", "Neither चैत nor द्रस- is a word here."),
             ("च + एतत् + अरसप्रसादात्मकम्", "An अ- here would give चैतदरस-, which is not printed.")],
            "च (and) + एतत् (this) + रसप्रसादात्मकम् → चैतद्रसप्रसादात्मकम्.",
            "अ + ए → ऐ; त् + voiced consonant → द्."),
        mcq("apply", 4, "A learner renders unit 227 as: Both of these are of the nature of the waste of rasa. Which word is wrong?",
            ("waste", "प्रसाद is the clear essence, the refined part, not waste."),
            [("both", "उभयम् = both: right."),
             ("nature", "-आत्मकम् = having the nature of: right."),
             ("rasa", "रस is named in the compound: right.")],
            "रसप्रसाद = the clear essence of rasa.",
            "प्रसाद = clear essence."),
        mcq("transfer", 5, "By the rule of च + एतत् → चैतत्, how is तत्र + एव (right there) joined?",
            ("तत्रैव", "अ + ए → ऐ, as च + एतत् → चैतत्."),
            [("तत्रेव", "ए comes from अ + इ; अ + ए gives ऐ."),
             ("तत्रौव", "औ comes from अ + ओ or औ, not from अ + ए."),
             ("तत्राव", "The ए is not lost; अ + ए gives ऐ.")],
            "तत्र + एव = तत्रैव, like च + एतत् = चैतत्.",
            "अ + ए → ऐ.",
            teaches="अ followed by ए joins as ऐ: च + एतत् → चैतत्."),
    ],
}

# ---------------------------------------------------------------- unit 228
AUTHORED["228"] = {
    "title": "समधातोः पंरिमाणमिदं",
    "question": "By unit 228, for whom do these measures hold?",
    "rule": "This (इदम्) is the measure (परिमाण) for one whose dhātus are in balance (समधातोः).",
    "limits": ("A short prose line; the copula is understood. The printed पंरिमाणम् has a stray anusvāra (flagged, read "
               "परिमाणम्): no question on that form. The line does not say how the measures change when the dhātus are "
               "not in balance."),
    "explain_hi": ("यह गद्य-पंक्ति पिछले माप की बात समेटती है: यह सम धातु वाले का परिमाण है। "
                   "‘समधातु’ बहुव्रीहि है: जिसके धातु सम यानी संतुलन में हैं, वह व्यक्ति। "
                   "‘इदम्’ (यह) पहले कहे माप की ओर संकेत करता है। "
                   "धातु शास्त्रीय शब्द है, वैसे ही रखा गया। "
                   "छपे ‘पंरिमाणम्’ का अनुस्वार छपाई की चूक है; शब्द ‘परिमाण’ है।"),
    "hook": "ये माप: संतुलित धातु वाले शरीर के।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 228, for whom is this measure given?",
            ("One whose dhātus are balanced", "समधातोः: of one with balanced dhātus."),
            [("One whose dhātus are increased", "Increase is not the state named; सम means balanced."),
             ("One whose dhātus are wasted", "Wasting is not the state named; सम means balanced."),
             ("One who is still in the womb", "The fetus is not named in unit 228.")],
            "समधातोः परिमाणमिदम्: this is the measure for one with balanced dhātus.",
            "समधातु = one whose dhātus are balanced."),
        match(1, "Match each word of unit 228 to its meaning.",
              [["सम", "even, balanced"], ["परिमाण", "measure"], ["इदम्", "this"]],
              "This is the measure for one whose dhātus are balanced.",
              "सम, परिमाण, इदम्."),
        mcq("extend", 2, "What kind of compound is समधातु in unit 228?",
            ("A bahuvrīhi: one whose dhātus are even", "It describes a person by his dhātus: सम + धातु."),
            [("A dvandva: 'the even and the dhātu'", "A dvandva would join two things as 'and'; here सम describes धातु."),
             ("A tatpuruṣa: 'the dhātu of the even'", "No genitive link 'of the even' is meant; it describes a person."),
             ("No compound: two separate words", "समधातोः is one word with one ending.")],
            "समधातु = he whose dhātus are सम (balanced): a bahuvrīhi.",
            "बहुव्रीहि = 'he whose X is Y'.",
            teaches="A bahuvrīhi names someone by what he has: समधातु = one whose dhātus are balanced."),
        mcq("discriminate", 3, "In unit 228, what does इदम् (this) stand for?",
            ("The measure: 'this is the measure'", "इदम् (n. nom. sg.) goes with परिमाणम् (n. nom. sg.)."),
            [("The person: 'this is the man'", "No man is named; इदम् agrees with परिमाणम्."),
             ("The body: 'this is the body'", "शरीर is not in unit 228; इदम् goes with परिमाणम्."),
             ("The dhātu: 'this is the dhātu'", "धातु is masculine here; इदम् is neuter like परिमाणम्.")],
            "परिमाणम् इदम्: this (is) the measure.",
            "इदम् + परिमाणम् = this measure."),
        multi("apply", 4, "Which of these are true of unit 228?",
              [("It names a disease", "No disease is named in unit 228."),
               ("It gives a new añjali number", "No number is given in unit 228."),
               ("It speaks of a measure", "Right: परिमाणमिदम्, this is the measure."),
               ("It names balanced dhātus", "Right: समधातोः, of one with balanced dhātus.")],
              [2, 3],
              "Unit 228 says only: this is the measure for one with balanced dhātus.",
              "समधातोः परिमाणमिदम्."),
        mcq("transfer", 5, "By the pattern of परिमाणम् + इदम् → परिमाणमिदम्, how is वचनम् + इदम् (this word) joined?",
            ("वचनमिदम्", "A final म् before a vowel joins that vowel, as परिमाणम् + इदम्."),
            [("वचनंइदम्", "The anusvāra stands for म् only before a consonant."),
             ("वचनेदम्", "The म् is not lost; अ + इ → ए does not apply across म्."),
             ("वचनमीदम्", "म् + इ keeps the short इ; nothing lengthens it.")],
            "वचनम् + इदम् = वचनमिदम्, like परिमाणम् + इदम् = परिमाणमिदम्.",
            "Final म् + vowel → the म् joins the vowel.",
            teaches="A final म् before a vowel joins it: परिमाणम् + इदम् → परिमाणमिदम्."),
    ],
}


# ===================================================================== NOTES_HI
NOTES_HI = {
    "217": ("गद्य-पंक्ति; विश्वास निम्न। पाठ-चिह्न: (१) छपा ‘गृण्हंति’ = गृह्णन्ति का अमानक वर्तनी-रूप (सम्भावित); (२) छपा "
            "‘विपक्वंतंनयंति’ = विपक्वम् तत् नयन्ति, ‘तं’ को ‘तत्’ पढ़ा (तत् + न → तन् न विकल्प से, छपा तं; सम्भावित; पुंलिङ्ग ‘तम्’ हो तो कर्म "
            "बदलेगा)। इन दोनों पर प्रश्न नहीं। कर्ता इस इकाई में नहीं; डेटा के अनुसार सम्भवतः इकाई २१६ वाली स्त्रीलिङ्ग नाड़ियाँ (सिरा-धमनी)। "
            "‘नयन्ति’ का गन्तव्य नहीं बताया, कुछ जोड़ा नहीं गया। अभ्यंग = तेल-मालिश, लेप = लेप लगाना (मानक)। ‘वीर्य्यं’ में य का "
            "द्वित्व छपाई की आदत। ‘तथाऽभ्यंग’ का अवग्रह छपाई की आदत (तथा अभ्यङ्ग), लोप नहीं। सन्धि जाँची: लेप + आदि → लेपादि "
            "(अ + आ → आ); स्पर्शम् + च → स्पर्शं च (वाक्य के भीतर म् + व्यंजन → ं)।"),
    "218": ("गद्य-पंक्ति; विश्वास उच्च; पाठ-चिह्न नहीं। स्रोतस् शास्त्रीय शब्द (मार्ग); कोई आधुनिक पर्याय नहीं रखा। क्रिया ‘हैं’ "
            "समझी जाती है। सन्धि जाँची: पुनः (मूल पुनर्) + असंख्येयानि → पुनरसंख्येयानि (स्वर से पहले र्); असंख्येयानि + एव → "
            "असंख्येयान्येव (इ + भिन्न स्वर → य्); ‘असंख्येय’ = असङ्ख्येय (अनुस्वार = ङ्)।"),
    "219": ("गद्य-पंक्ति; विश्वास उच्च; पाठ-चिह्न नहीं। ‘तथाऽपि’ का अवग्रह छपाई की आदत (तथा अपि)। ‘यथास्थूलम्’ = स्थूल के "
            "अनुसार, यानी मोटे तौर पर; ‘यथोपयोगम्’ = उपयोग के अनुसार। ‘उपदेक्ष्यन्ते’ = उप-√दिश्, भविष्यत् कर्मवाच्य, प्रथम पुरुष "
            "बहुवचन। छपाई में ‘यथास्थूलंयथोपयोगं’ जुड़ा छपा। सन्धि जाँची: तथा + अपि → तथापि (आ + अ → आ); सिरा + आदीनि → "
            "सिरादीनि (आ + आ → आ); यथा + उपयोगम् → यथोपयोगम् (आ + उ → ओ); च + अन्यत्र → चान्यत्र (अ + अ → आ); अन्यत्र + "
            "उपदेक्ष्यन्ते → अन्यत्रोपदेक्ष्यन्ते (अ + उ → ओ)।"),
    "220": ("गद्य-पंक्ति; विश्वास मध्यम। पाठ-चिह्न: छपा ‘परिसंख्याता’ → सम्भावित ‘परिसंख्याताः’ (श से पहले विसर्ग लुप्त नहीं होता; "
            "भावाः से मेल)। छपा ‘मूर्त्ति मंतःस्थिरा’ को मूर्तिमन्तः स्थिराः पढ़ा (बीच में भटकी जगह; ‘स्थिराः’ का विसर्ग भावाः से पहले "
            "नियम से लुप्त); दूसरा पाठ ‘मूर्तिमन्तोऽस्थिराः’ (अस्थिर) भी सम्भव; इस पर प्रश्न नहीं। ‘मूर्त्ति’ में त का द्वित्व छपाई की "
            "आदत। डेटा के अनुसार इनके सामने इकाई २२१ के द्रव रखे गए हैं। सन्धि जाँची: इति + एवम् → इत्येवम् (इ + भिन्न स्वर → य्)।"),
    "221": ("गद्य-पंक्ति; विश्वास निम्न। वाक्य सम्भवतः इकाई २२२ में आगे चलता है, जहाँ उदक की परिभाषा है। वाक्य-रचना अस्पष्ट: "
            "‘यत् तत्’ का पूर्ववर्ती नहीं, ‘अनुबध्नाति’ का कर्ता नहीं लिखा (सम्भवतः द्रव), और ‘च्यवमानम्’ पुरीष का विशेषण भी हो सकता "
            "है (‘अतियोग से गिरता मल’); अनुवाद शब्दक्रम पर है, कोई निर्णय नहीं। पाठ-चिह्न: छपा ‘अन्यांच’ → सम्भावित ‘अन्यांश्च’ "
            "(अन्यान् + च → अन्यांश्च; श् छूटा; तुलना इकाई २२९ का ‘अपरांश्चा’)। पुरीष = मल, रुधिर = रक्त। सन्धि जाँची: द्रवाः + तु "
            "→ द्रवास्तु (विसर्ग + त → स्); यत् + तत् → यत्तत्; तत् + अतियोगेन → तदतियोगेन (त् + स्वर → द्); पुरीषम् + अनुबध्नाति → "
            "पुरीषमनुबध्नाति; रुधिरम् + अन्यान् → रुधिरमन्यान्।"),
    "222": ("गद्य-पंक्ति; विश्वास निम्न। लम्बा वाक्य, सम्बन्धवाचक वाक्य ढीले जुड़े; अनुवाद छपे क्रम पर। तीनों ‘यत्’ वाक्य ‘तदुदकम्’ "
            "(वह उदक है) की परिभाषा माने गए। किसी द्रव की संख्या छपी नहीं; ‘यथापूर्वम् एकादिसंख्याप्रवृद्धिः’ का शब्दशः अर्थ "
            "रखा, हर स्तर पर एक-एक बढ़ना सम्भावित अर्थ है, कथित नहीं। ‘तस्य आद्यस्य’ = उसका (उदक) और प्रथम (रस) का; दूसरा पाठ: "
            "आद्य केवल रस का विशेषण। लसीका = लसीका-द्रव (सम्भावित), वसा = मांसपेशी की चर्बी (सम्भावित), मेदस् = मेद धातु "
            "(सम्भावित), मज्जन् = मज्जा धातु (सम्भावित); श्लेष्मन् और पित्त यहाँ शरीर के द्रव। पाठ-चिह्न: छपा ‘प्रमाणेण’ → "
            "‘प्रमाणेन’ (लगभग निश्चित; ‘-णेण’ कोई रूप नहीं)। ‘विभर्त्ति’ में त का द्वित्व छपाई की आदत; ‘ऊष्मणाऽनुबद्धं’ का अवग्रह "
            "छपाई की आदत। छपाई में ‘वसायाः मेदसो’ सन्धि बिना (नियम से वसाया मेदसो)। सन्धि जाँची: यत् + च → यच्च (त् + च → च्च); "
            "त्वक् + विभर्ति → त्वग्विभर्ति (क् + घोष व्यंजन → ग्); च + ऊष्मणा → चोष्मणा (अ + ऊ → ओ); रोमकूपेभ्यः + अभि → "
            "रोमकूपेभ्योऽभि (अः + अ → ओऽ); तत् + उदकम् → तदुदकम् (त् + स्वर → द्); तस्य + आद्यस्य → तस्याद्यस्य (अ + आ → आ); "
            "च + आहार → चाहार; रस + आख्य → रसाख्य; मेदसः + मज्ज्ञः → मेदसो मज्ज्ञः (अः + घोष व्यंजन → ओ); मज्ज्ञः + च → "
            "मज्ज्ञश्च (विसर्ग + च → श्); स्वेन + अञ्जलि → स्वेनाञ्जलि (अ + अ → आ); एक + आदि → एकादि।"),
    "223": ("गद्य-पंक्ति; विश्वास मध्यम; क्रिया नहीं, इकाई २२२ की माप-श्रृंखला आगे। शुक्र = वीर्य (मानक)। पाठ-चिह्न: छपा "
            "‘अर्द्धंजलिःशुक्रस्य’ → ‘अर्द्धाञ्जलिः शुक्रस्य’ (सम्भावित): अर्ध + अञ्जलिः में आ (अ + अ → आ) छूटा और शब्दों के बीच "
            "जगह नहीं; दोनों छपाई की चूक, अलग पाठ नहीं। ‘ं’ = ञ् (ज से पहले, जैसे ‘अंजलि’)। ‘अर्द्ध’ में द का द्वित्व छपाई की आदत। "
            "इस छपे रूप पर प्रश्न नहीं।"),
    "224": ("गद्य-पंक्ति; विश्वास मध्यम; पाठ-चिह्न नहीं; क्रिया नहीं। ‘तावत् एव’ = उतना ही; डेटा इसे इकाई २२३ की आधी अंजलि मानता "
            "है, पर यहाँ लिखा नहीं; इस मात्रा पर प्रश्न नहीं। मस्तिष्क = दिमाग (मानक)। ओजस् शास्त्रीय शब्द, आधुनिक पर्याय नहीं। "
            "छपा ‘मस्तिष्क मोजश्च’ = मस्तिष्कम् ओजः च (म् अगले शब्द के साथ, जगह गलत)। सन्धि जाँची: तावत् + एव → तावदेव "
            "(त् + स्वर → द्); मस्तिष्कम् + ओजः → मस्तिष्कमोजः; ओजः + च → ओजश्च (विसर्ग + च → श्)।"),
    "225": ("गद्य-पंक्ति; विश्वास मध्यम; क्रिया नहीं। रजस् = सम्भवतः मासिक धर्म का रक्त (सम्भावित; प्रसंग स्त्रियों के द्रवों का)। "
            "पाठ-चिह्न: छपा ‘रजसोऽजल्यश्चतस्रः’ → ‘रजसोऽञ्जल्यश्चतस्रः’ (लगभग निश्चित; ञ् छपाई में छूटा, तुलना इकाई २२२ का "
            "‘स्वेनांजलि’)। ‘चतस्रः’ स्त्रीलिङ्ग है, इसलिए यहाँ अंजलि स्त्रीलिङ्ग (अञ्जल्यः) पढ़ी गई। सन्धि जाँची: रजसः + अञ्जल्यः → "
            "रजसोऽञ्जल्यः (अः + अ → ओऽ); अञ्जल्यः + चतस्रः → अञ्जल्यश्चतस्रः (विसर्ग + च → श्); ‘स्त्रीणां’ में अन्त्य म् अगले "
            "व्यंजन से पहले ं।"),
    "226": ("गद्य-पंक्ति; विश्वास मध्यम; पाठ-चिह्न नहीं; क्रिया नहीं। माप-शब्द (अंजलि, जैसा इकाई २२५ में) समझा जाता है, जोड़ा नहीं "
            "गया। ‘द्वौ’ पुंलिङ्ग द्विवचन है, इकाई २२५ के स्त्रीलिङ्ग ‘चतस्रः’ से भिन्न (यहाँ अंजलि पुंलिङ्ग मानी गई); यह भेद केवल दर्ज, "
            "इस पर प्रश्न नहीं। स्तन्य = स्तन का दूध।"),
    "227": ("गद्य-पंक्ति; विश्वास मध्यम; पाठ-चिह्न नहीं। ‘उभयम्’ = दोनों; डेटा इन्हें इकाई २२५-२२६ के रजस् और स्तन्य मानता है, पंक्ति "
            "नाम नहीं लेती; इस पर प्रश्न नहीं। ‘इति’ कथन समाप्त करता है, अनुवाद में नहीं। रसप्रसाद = रस का स्वच्छ, सूक्ष्म भाग। क्रिया "
            "समझी जाती है। सन्धि जाँची: उभयम् + अपि → उभयमपि; च + एतत् → चैतत् (अ + ए → ऐ); एतत् + रस → एतद्रस (त् + घोष "
            "व्यंजन → द्); रस + प्रसाद + आत्मकम् → रसप्रसादात्मकम् (अ + आ → आ); ...आत्मकम् + इति → ...आत्मकमिति।"),
    "228": ("गद्य-पंक्ति; विश्वास मध्यम। पाठ-चिह्न: छपा ‘पंरिमाणमिदं’ → ‘परिमाणम् इदम्’ (सम्भावित; अनुस्वार छपाई की चूक)। "
            "समधातु = जिसके धातु साम्य में हों (बहुव्रीहि; धातु शास्त्रीय शब्द रखा)। क्रिया ‘है’ समझी जाती है। सन्धि जाँची: "
            "परिमाणम् + इदम् → परिमाणमिदम् (म् स्वर से मिलता है); अन्त का ‘इदं’ छपाई की वर्तनी।"),
}


# ===================================================================== AIDS
AIDS = {
    "217": {
        "diagram": {"groups": [
            {"label": "वे ले जाती हैं (नयन्ति)", "items": ["अभ्यंग (तेल-मालिश) का वीर्य", "लेप का वीर्य", "आदि (ऐसी ही चीज़ों) का वीर्य",
                                                   "जो त्वचा में पूरा पक चुका"]},
            {"label": "वे ग्रहण करती हैं (गृह्णन्ति)", "items": ["स्पर्श"]}]},
        "chunks": "तथाऽभ्यंगलेपादिवीर्य्यं | त्वचि | विपक्वंतंनयंति | स्पर्शं च | गृण्हंति",
        "sandhi": "अ + आ → आ: लेप + आदि → लेपादि · वाक्य के भीतर म् + व्यंजन → ं: स्पर्शम् + च → स्पर्शं च।",
        "frame": "कौन: (इकाई में नाम नहीं; सम्भवतः इकाई २१६ वाली) → क्या ले जातीं: त्वचा में पका अभ्यंग-लेप आदि का वीर्य → और क्या ग्रहण करतीं: स्पर्श।",
    },
    "218": {
        "chunks": "स्रोतांसि | पुनरसंख्येयान्येव",
        "sandhi": "पुनः (मूल पुनर्) + स्वर → पुनर्: पुनरसंख्येयानि · इ + भिन्न स्वर → य्: असंख्येयानि + एव → असंख्येयान्येव।",
        "letters": "अ + संख्येय = जो गिना न जा सके; ‘अ’ उलट देता है। (केवल याद की सहायता)",
    },
    "219": {
        "chain": {"steps": ["फिर भी (तथापि तु)", "सिरा आदि", "स्थूल रूप से (यथास्थूलम्)", "उपयोग के अनुसार (यथोपयोगम्)",
                            "दूसरी जगह सिखाए जाएँगे (अन्यत्र उपदेक्ष्यन्ते)"]},
        "chunks": "तथाऽपि तु | सिरादीनि | यथास्थूलंयथोपयोगं | चान्यत्रोपदेक्ष्यंते",
        "sandhi": "आ + उ → ओ: यथा + उपयोगम् → यथोपयोगम् · अ + अ → आ: च + अन्यत्र → चान्यत्र · अ + उ → ओ: अन्यत्र + उपदेक्ष्यन्ते → अन्यत्रोपदेक्ष्यन्ते।",
    },
    "220": {
        "chunks": "इत्येवं | परिसंख्याता | शरीरे | मूर्त्ति मंतःस्थिरा | भावाः",
        "sandhi": "इ + भिन्न स्वर → य्: इति + एवम् → इत्येवम्।",
        "frame": "क्या हुआ: परिसंख्याताः (गिना दिए) → कहाँ: शरीरे → कौन: मूर्तिमन्तः भावाः (रूप वाले भाव; ‘स्थिर’ पाठ अनिश्चित)।",
    },
    "221": {
        "chain": {"steps": ["द्रव (तु)", "अतियोग से च्युत होता हुआ (द्रव या मल? अन्वय अस्पष्ट)", "पुरीष (मल) को बाँधता है", "वैसे ही मूत्र",
                            "रुधिर", "और शरीर के अन्य धातु"]},
        "chunks": "द्रवास्तु | यत्तदतियोगेन | च्यवमानं | पुरीषमनुबध्नाति | तथामूत्रंरुधिरमन्यांच | शरीरे धातून्",
        "sandhi": "विसर्ग + त → स्: द्रवाः + तु → द्रवास्तु · त् + स्वर → द्: तत् + अतियोगेन → तदतियोगेन।",
    },
    "222": {
        "diagram": {"groups": [
            {"label": "उदक के तीन रूप (पंक्ति के क्रम में)",
             "items": ["१ पूरे शरीर में, जिसे बाहरी त्वचा धारण करती", "२ त्वचा के भीतर घाव में: ‘लसीका’",
                       "३ ऊष्मा से बँधा, रोमकूपों से निकलता: ‘स्वेद’"]}]},
        "chain": {"steps": ["उदक, रस (आहार का सार)", "रक्त, शकृत् (मल)", "श्लेष्मन्, पित्त", "मूत्र, वसा", "मेदस्, मज्जन्",
                            "हर एक अपनी-अपनी अंजलि से (संख्या छपी नहीं)"]},
        "chunks": ("यच्च सर्वशरीरगतं बाह्या त्वग्विभर्त्ति | यच्चत्वगंतरे व्रणगतं लसीकाशब्दवाच्यं | "
                   "यच्चोष्मणाऽनुबद्धं रोमकूपेभ्योऽभिनिष्पतत्स्वेदवाच्यं | तदुदकं | तस्याद्यस्य चाहारसारस्य रसाख्यस्य | "
                   "तथारक्तस्य शकृतः श्लेष्मणः पित्तस्य मूत्रस्य वसायाः मेदसो मज्ज्ञश्च | स्वेन स्वेनांजलिप्रमाणेण | "
                   "यथापूर्वमेकादिसंख्याप्रवृद्धिः"),
        "sandhi": ("त् + स्वर → द्: तत् + उदकम् → तदुदकम् · अः + अ → ओऽ: रोमकूपेभ्यः + अभि → रोमकूपेभ्योऽभि · "
                   "अः + घोष व्यंजन → ओ: मेदसः + मज्ज्ञः → मेदसो मज्ज्ञः।"),
    },
    "223": {
        "chunks": "अर्द्धंजलिःशुक्रस्य",
        "sandhi": "सम्भावित पढ़त (पाठ-चिह्न): अर्ध + अञ्जलिः → अर्धाञ्जलिः (अ + अ → आ); छपा रूप अर्द्धंजलिः है, इस जोड़ पर प्रश्न नहीं।",
        "frame": "कितना: अर्ध-अञ्जलिः (आधी अंजलि) → किसका: शुक्रस्य (शुक्र का)।",
    },
    "224": {
        "chunks": "तावदेव | मस्तिष्क मोजश्च",
        "sandhi": "त् + स्वर → द्: तावत् + एव → तावदेव · विसर्ग + च → श्: ओजः + च → ओजश्च।",
        "frame": "कितना: तावत् एव (उतना ही; पिछले माप की ओर) → किनका: मस्तिष्क और ओज।",
    },
    "225": {
        "chunks": "स्त्रीणां | रजसोऽजल्यश्चतस्रः",
        "sandhi": "अः + अ → ओऽ: रजसः + अञ्जल्यः → रजसोऽञ्जल्यः · विसर्ग + च → श्: अञ्जल्यः + चतस्रः → अञ्जल्यश्चतस्रः।",
        "frame": "किनमें: स्त्रीणाम् (स्त्रियों में) → किसका: रजसः → कितना: अञ्जल्यः चतस्रः (चार अंजलि)।",
    },
    "226": {
        "chunks": "स्तन्यस्य | द्वौ",
        "frame": "किसका: स्तन्यस्य (स्तन के दूध का) → कितना: द्वौ (दो; माप-शब्द समझा जाता है)।",
        "pegs": "स्तन दो, तो दूध भी ‘दो’: मेरा बनाया जोड़, पाठ का कथन नहीं। (केवल याद की सहायता)",
    },
    "227": {
        "chunks": "उभयमपि | चैतद्रसप्रसादात्मकमिति",
        "sandhi": "अ + ए → ऐ: च + एतत् → चैतत् · त् + घोष व्यंजन → द्: एतत् + रस → एतद्रस।",
        "frame": "कौन: उभयम् (दोनों; नाम नहीं लिए) → किस स्वरूप के: रस का प्रसाद (स्वच्छ सार)।",
    },
    "228": {
        "chunks": "समधातोः | पंरिमाणमिदं",
        "sandhi": "म् + स्वर → मिलकर: परिमाणम् + इदम् → परिमाणमिदम्।",
        "frame": "किसका: समधातोः (संतुलित धातु वाले का) → क्या: परिमाणम् इदम् (यह माप)।",
    },
}


# ===================================================================== IMAGE_SPECS
IMAGE_SPECS = {
    ("217", "diagram"): {
        "file": "sh5-tvak-virya-217.svg",
        "alt": ("Table of unit 217, two actions of an unnamed subject: they carry the potency of oil massage, paste and the "
                "like, fully matured in the skin; and they take up touch."),
        "type": "table",
        "title": "इकाई २१७: दो काम (कर्ता अनाम)",
        "heads": ["काम", "किसका / क्या"],
        "rows": [["ले जाती हैं (नयन्ति)", "अभ्यंग, लेप आदि का वीर्य"], ["वह वीर्य", "त्वचा में पूरा पका"],
                 ["ग्रहण करती हैं", "स्पर्श"], ["कर्ता", "इकाई में नाम नहीं"]],
    },
    ("219", "chain"): {
        "file": "sh5-siradi-upadesha-219.svg",
        "alt": ("Chain of unit 219 in line order: even so; the sirā and the rest; broadly; according to use; will be taught "
                "elsewhere."),
        "type": "chain",
        "title": "इकाई २१९: सिरा आदि का उपदेश आगे",
        "steps": ["फिर भी (तथापि तु)", "सिरा आदि", "स्थूल रूप से", "उपयोग के अनुसार", "अन्यत्र सिखाए जाएँगे"],
    },
    ("221", "chain"): {
        "file": "sh5-drava-221.svg",
        "alt": ("Chain of unit 221 in line order: the liquids; falling away through excess (syntax unclear); binds on to the "
                "dung; likewise the urine; the blood; and the other dhātus in the body."),
        "type": "chain",
        "title": "इकाई २२१: द्रव (अन्वय अस्पष्ट)",
        "steps": ["द्रव", "अतियोग से च्युत होता (द्रव या मल? अस्पष्ट)", "पुरीष (मल) को बाँधता", "वैसे ही मूत्र", "रुधिर", "शरीर के अन्य धातु"],
    },
    ("222", "diagram"): {
        "file": "sh5-udaka-rupa-222.svg",
        "alt": ("Numbered table of unit 222, the three forms called udaka (water) in line order: 1 what pervades the whole "
                "body and the outer skin holds; 2 within the skin in a wound, called lasīkā; 3 bound with heat, flowing "
                "from the hair-pores, called sweat."),
        "type": "table",
        "title": "इकाई २२२: उदक के तीन रूप",
        "heads": ["क्रम", "रूप (पंक्ति के क्रम में)"],
        "rows": [["१", "पूरे शरीर में; बाहरी त्वचा धारण करती"], ["२", "त्वचा के भीतर घाव में: लसीका"],
                 ["३", "ऊष्मा से बँधा, रोमकूपों से: स्वेद"], ["तीनों", "वह उदक (जल) है"]],
    },
    ("222", "chain"): {
        "file": "sh5-anjali-krama-222.svg",
        "alt": ("Numbered table of unit 222, the ten fluids measured by their own añjali, in line order: 1 udaka, 2 rasa, "
                "3 blood, 4 dung, 5 śleṣman, 6 pitta, 7 urine, 8 vasā, 9 medas, 10 marrow; no numbers of añjali are "
                "printed."),
        "type": "table",
        "title": "इकाई २२२: द्रवों का क्रम (संख्या छपी नहीं)",
        "heads": ["पंक्ति में स्थान", "द्रव (अंजलि-संख्या नहीं)"],
        "rows": [["१", "उदक (जल)"], ["२", "रस (आहार का सार)"], ["३", "रक्त"], ["४", "शकृत् (मल)"], ["५", "श्लेष्मन्"],
                 ["६", "पित्त (यहाँ शरीर का द्रव)"], ["७", "मूत्र"], ["८", "वसा (सम्भवतः पेशी की चर्बी)"],
                 ["९", "मेदस् (सम्भवतः मेद धातु)"], ["१०", "मज्जन् (सम्भवतः मज्जा धातु)"]],
    },
}
