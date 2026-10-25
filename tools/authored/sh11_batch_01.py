from helpers import mcq, match, order, fill, multi, accepts


AUTHORED = {}

# ---------------------------------------------------------------- unit 1
AUTHORED["1"] = {
    "title": "अथातो विकृतव्याधिविज्ञानीयमध्यायं",
    "question": "What does the opening line of card 1 announce, and how are its words joined?",
    "rule": ("Now, therefore (अथ अतः), we shall explain (व्याख्यास्यामः) the chapter (अध्यायम्) on the knowledge of "
             "abnormal diseases (विकृतव्याधिविज्ञानीयम्): the usual opening formula with the chapter's name."),
    "limits": ("Prose, high confidence, one printed line. The line gives only the chapter's name; it does not say what the "
               "chapter teaches, so no question asks about its content. विकृत is rendered literally (altered, abnormal)."),
    "explain_hi": ("यह अध्याय का आरम्भिक सूत्र है: ‘अब, इसलिए, हम विकृतव्याधिविज्ञानीय नामक अध्याय की व्याख्या करेंगे।’ "
                   "विकृत = बदला हुआ, असामान्य; व्याधि = रोग; विज्ञानीय = जानने से सम्बन्धित। "
                   "‘व्याख्यास्यामः’ वि-आ-√ख्या का भविष्यत् काल, उत्तम पुरुष बहुवचन है: ‘हम व्याख्या करेंगे’। "
                   "यह पंक्ति केवल अध्याय का नाम देती है, उसका विषय नहीं बताती। "
                   "सन्धियाँ: अथ + अतः → अथातः (अ + अ → आ); अतः + वि- → अतो वि- (अः घोष व्यंजन से पहले → ओ)।"),
    "hook": "अथातो ... व्याख्यास्यामः: विकृत व्याधियों के ज्ञान वाला अध्याय आरम्भ।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 1, what does व्याख्यास्यामः mean?",
            ("We shall explain", "वि-आ-√ख्या, future, first person plural: we shall explain."),
            [("We have explained", "-स्यामः marks the future, not a past action."),
             ("They are explaining", "-मः is 'we'; 'they' would need another ending."),
             ("Let him explain", "That would be the imperative व्याख्यातु; this is a future, 'we'.")],
            "व्याख्यास्यामः = we shall explain.",
            "-स्यामः: future, first person plural."),
        match(1, "Match each word of card 1 to its meaning.",
              [["अथ", "now"], ["अतः", "therefore"], ["विकृत", "altered, abnormal"], ["व्याधि", "disease"],
               ["अध्याय", "chapter"]],
              "अथ = now, अतः = therefore, विकृत = altered, abnormal, व्याधि = disease, अध्याय = chapter.",
              "अथ, अतः, विकृत, व्याधि, अध्याय."),
        order(2, "Put the words of card 1 in the printed order.",
              ["अथ", "अतः", "विकृतव्याधिविज्ञानीयम्", "अध्यायम्", "व्याख्यास्यामः"],
              "Now; therefore; on the knowledge of abnormal diseases; the chapter; we shall explain.",
              "अथ → अतः → विकृतव्याधिविज्ञानीयम् → अध्यायम् → व्याख्यास्यामः.",
              role="extend",
              teaches="In the opening formula the chapter's name stands in the accusative (अध्यायम्) as the object of 'we shall explain'."),
        mcq("discriminate", 3, "Which split of अथातो in card 1 is right?",
            ("अथ + अतः", "अ + अ → आ: अथ + अतः → अथातः; before the voiced व it is printed अथातो."),
            [("अथा + अतः", "अथा is not a word; the particle is अथ, with short अ."),
             ("अथ + तः", "With तः no vowels meet: it would print अथतो."),
             ("अथात् + अः", "अथात् is not a word; the two words are अथ and अतः.")],
            "अथ (now) + अतः (therefore): अ + अ → आ.",
            "अ + अ → आ."),
        mcq("apply", 4, "Why is the म् of -विज्ञानीयम् joined to अध्यायम् in card 1?",
            ("A final म् joins a following vowel", "म् stays म् and joins the vowel: -विज्ञानीयम् + अध्यायम् → -विज्ञानीयमध्यायम्."),
            [("A final म् turns to ं before a vowel", "Anusvāra is written only before a consonant (अध्यायं व्याख्यास्यामः, same card)."),
             ("A final म् is dropped before a vowel", "It is not dropped: the print keeps म in -यमध्यायं."),
             ("Two अ sounds merge here into आ", "No two vowels meet; म् stands between them.")],
            "-विज्ञानीयम् + अध्यायम् → -विज्ञानीयमध्यायम्.",
            "Final म् + vowel → joined, unchanged."),
        mcq("transfer", 5, "By the pattern of व्याख्यास्यामः (we shall explain), what does पठिष्यामः mean in a new example?",
            ("We shall read", "-ष्यामः / -स्यामः: future, 'we': पठिष्यामः = we shall read."),
            [("We are reading", "That would be the present पठामः."),
             ("You will read", "'You' (plural) would be पठिष्यथ; -मः is 'we'."),
             ("They have read", "-ष्यामः marks the future and 'we', not a past and 'they'.")],
            "पठिष्यामः = we shall read, like व्याख्यास्यामः = we shall explain.",
            "-स्यामः / -ष्यामः = future, first person plural.",
            teaches="-स्यामः (or -ष्यामः) ends a future verb in the first person plural: व्याख्यास्यामः = we shall explain."),
    ],
}

# ---------------------------------------------------------------- unit 2
AUTHORED["2"] = {
    "title": "यस्य व्याधिरुत्पद्यते",
    "question": "By card 2, which signs, each opened by यस्य (whose), lead to the closing words स परासुः?",
    "rule": ("A string of alternative signs, each opened by यस्य: a disease arising with all its causes, premonitory signs and "
             "signs to excess; marks on face, nails, teeth, belly; and more. All close in स परासुः, one whose life-breaths are gone."),
    "limits": ("Medium confidence. Flagged readings (सवैर्, क्षणिस्य, सतृष्णो स) carry no question. piplu, vyaṅga, tilakālaka, "
               "āmāśaya (stomach) and pakvāśaya (large intestine) are probable identifications; पुष्प is read literally (flowers); "
               "ghurghuraka is probably the death rattle (data). परासु: life-breaths gone; no time or treatment."),
    "explain_hi": ("यह एक लम्बा गद्य वाक्य है: हर लक्षण ‘यस्य’ (जिसका) से शुरू होता है, और अन्त का ‘स परासुः’ (वह परासु है, यानी जिसके प्राण चले गए) सब पर लागू होता है। "
                   "पहला लक्षण: जिसका रोग अपने सब हेतुओं, पूर्वरूपों और रूपों के साथ अत्यधिक मात्रा में उत्पन्न हो। "
                   "फिर मुख पर पिप्लु, व्यंग, रेखाएँ और तिलकालक (पहचान सम्भावित), नाखूनों और दाँतों पर पुष्प (शब्दशः फूल), पेट पर अनेक रंगों की सिराएँ, "
                   "नीला-पीला-लाल श्लेष्मा, गर्दन का अवमर्द, आमाशय (सम्भवतः जठर) या पक्वाशय (सम्भवतः बड़ी आँत) से उठी परिकर्तिका, और कण्ठ में वायु का घुरघुरक शब्द। "
                   "छपे ‘सवैर्’, ‘क्षणिस्य’, ‘सतृष्णो’ के सुधार केवल सम्भावित हैं, इसलिए उन पर प्रश्न नहीं। "
                   "पंक्ति न कोई समय बताती है, न कोई उपचार।"),
    "hook": "हर ‘यस्य’ एक लक्षण, अन्त में एक फल: स परासुः।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By card 2, where are the veins of various colours (नानावर्णाः सिराः) seen?",
            ("On the belly", "उदरे वा नानावर्णाः सिराः: on the belly, veins of various colours."),
            [("On the face", "The face (मुखे) has moles, blemishes, lines and specks (probable identifications)."),
             ("On the nails", "The nails and teeth (करजरदनेषु) have flowers (पुष्पाणि)."),
             ("On the neck", "The neck has a crushing (ग्रीवावमर्दः), not veins.")],
            "उदरे = on the belly.",
            "उदर = belly."),
        match(1, "Match each word of card 2 to its meaning.",
              [["करज", "nail"], ["रदन", "tooth"], ["उदर", "belly"], ["सिरा", "vein, vessel"],
               ["गुदग्रह", "grasp of the anus"], ["घुर्घुरक", "a gurgling sound"]],
              "करज = nail, रदन = tooth, उदर = belly, सिरा = vein, गुदग्रह = grasp of the anus, घुर्घुरक = gurgling sound.",
              "करज, रदन, उदर, सिरा, गुदग्रह, घुर्घुरक."),
        order(2, "Put these sure parts of card 2 in the printed order.",
              ["हेतुप्राग्रूपरूपैः", "करजरदनेषु पुष्पाणि", "नेत्रोपदेहः", "श्लेष्मा नीलपीतलोहितः", "कण्ठे घुर्घुरकम्", "स परासुः"],
              "Causes and signs to excess; flowers on nails and teeth; coating on the eyes; coloured phlegm; gurgling in the throat; he is parāsu.",
              "हेतुप्राग्रूपरूपैः → करजरदनेषु पुष्पाणि → नेत्रोपदेहः → श्लेष्मा नीलपीतलोहितः → कण्ठे घुर्घुरकम् → स परासुः.",
              role="extend",
              teaches="Many यस्य (whose) clauses can share one closing main clause: here स परासुः ends them all."),
        mcq("discriminate", 3, "By card 2, which sign goes with parikartikā arising in the pakvāśaya (probably the large intestine)?",
            ("Excessive anal grasp", "पक्वाशयोत्था परिकर्तिकाऽतितृष्णाऽतिमात्रश्च गुदग्रहः: excessive thirst and excessive gudagraha."),
            [("Breaking of the stool", "शकृद्भेदः goes with the parikartikā of the āmāśaya, the clause before."),
             ("Gurgling in the throat", "The gurgling (घुर्घुरक) is made by vāyu in a separate clause."),
             ("Drying of the tongue", "जिह्वाशोषः belongs to the clause of the neck and throat.")],
            "āmāśaya: thirst and breaking of the stool; pakvāśaya: thirst and excessive gudagraha.",
            "पक्वाशय → अतिमात्र गुदग्रह."),
        mcq("apply", 4, "Why is हृद्यैः printed हृद्यैर् before बहुभिः in card 2?",
            ("ः after ऐ, before voiced ब, gives र्", "The visarga follows ऐ (not अ or आ) and ब is voiced: हृद्यैर्बहुभिः."),
            [("ः before every consonant always gives र्", "Not every: before च it becomes श् (बहुशश्च, same card)."),
             ("र् is part of the word's own ending", "The form is हृद्यैः (instrumental plural); र् comes only from sandhi."),
             ("ः after ऐ is always kept before ब", "The print does not keep it: it shows र् before ब.")],
            "हृद्यैः + बहुभिः → हृद्यैर्बहुभिः.",
            "Visarga after a vowel other than अ/आ, before a voiced sound → र्."),
        mcq("transfer", 5, "By the pattern of हृद्यैर्बहुभिः, how is अश्वैः + युक्तः (yoked with horses) joined in a new example?",
            ("अश्वैर्युक्तः", "ः after ऐ, before the voiced य, gives र्: अश्वैर्युक्तः."),
            [("अश्वै युक्तः", "After ऐ the visarga is not dropped before a voiced sound; it gives र्."),
             ("अश्वैस्युक्तः", "स् comes from a visarga before त or थ, not before य."),
             ("अश्वैश्युक्तः", "श् comes from a visarga before च or छ (optionally before श), not before य.")],
            "अश्वैः + युक्तः = अश्वैर्युक्तः, like हृद्यैः + बहुभिः = हृद्यैर्बहुभिः.",
            "Visarga after ऐ + voiced sound → र्.",
            teaches="A visarga after a vowel other than अ or आ becomes र् before a voiced sound: हृद्यैः + बहुभिः → हृद्यैर्बहुभिः."),
    ],
}

# ---------------------------------------------------------------- unit 3
AUTHORED["3"] = {
    "title": "भवति चात्र",
    "question": "What does the short formula of card 3 say, and how is चात्र joined?",
    "rule": "भवति च अत्र: and here there is ... . A lead-in formula with nothing named after it; च + अत्र → चात्र (अ + अ → आ).",
    "limits": ("Prose, high confidence, one printed line. The formula names nothing after 'there is'; the data takes it as "
               "introducing the units that follow, which the line itself does not state. No question asks what follows."),
    "explain_hi": ("‘भवति चात्र’ का अर्थ है ‘और इस विषय में (यह) है’। "
                   "यह एक परिचय-सूत्र है; इसके बाद क्या है, यह पंक्ति स्वयं नहीं बताती। "
                   "डेटा के अनुसार यह सम्भवतः आगे की इकाइयों (कार्ड ४ से) का परिचय देता है। "
                   "‘भवति’ √भू का वर्तमान काल, प्रथम पुरुष एकवचन है। "
                   "‘चात्र’ में च + अत्र की सन्धि है: अ + अ → आ।"),
    "hook": "भवति चात्र: ‘और यहाँ है’, एक परिचय-सूत्र।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 3, what does भवति mean?",
            ("There is", "भवति = is, there is: present of √भू."),
            [("There was", "A past would be a form like अभवत्."),
             ("There will be", "A future would be भविष्यति."),
             ("Let there be", "The imperative would be भवतु.")],
            "भवति = there is.",
            "भवति: present, third person singular of √भू."),
        match(1, "Match each word of card 3 to its meaning.",
              [["भवति", "there is"], ["च", "and"], ["अत्र", "here"]],
              "भवति = there is, च = and, अत्र = here.",
              "भवति, च, अत्र."),
        fill(2, "The word for 'here' in card 3 is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("अत्र", "atra"),
             "अत्र = here; joined with च it is printed चात्र.",
             "अत्र (here) is indeclinable; after च, अ + अ merge into आ: चात्र.",
             "अत्र = here."),
        mcq("discriminate", 3, "Which split of चात्र in card 3 is right?",
            ("च + अत्र", "अ + अ → आ: च + अत्र → चात्र."),
            [("चा + अत्र", "चा is not a word; the particle is च, with short अ."),
             ("च + त्र", "त्र is not a word; अत्र (here) is."),
             ("चात् + र", "चात् is not a word; the words are च and अत्र.")],
            "च (and) + अत्र (here): अ + अ → आ.",
            "अ + अ → आ."),
        mcq("apply", 4, "Which join in card 1 follows the same rule as च + अत्र → चात्र?",
            ("अथ + अतः → अथातः", "Same rule: अ + अ → आ."),
            [("अतः + वि- → अतो वि-", "That is a visarga change (अः before a voiced consonant → ओ), not two vowels merging."),
             ("-यम् + अध्यायम् → -यमध्यायम्", "There म् joins a vowel; no two vowels merge."),
             ("अध्यायम् + व्या- → अध्यायं व्या-", "There म् before a consonant is written ं; no vowels meet.")],
            "अथ + अतः → अथातः, like च + अत्र → चात्र.",
            "अ + अ → आ."),
        mcq("transfer", 5, "By the pattern of च + अत्र → चात्र, how is हिम + अचलः (snow-mountain) joined in a new example?",
            ("हिमाचलः", "अ + अ → आ: हिम + अचलः → हिमाचलः."),
            [("हिमचलः", "The two अ sounds merge into a long आ; neither simply vanishes."),
             ("हिमेचलः", "ए comes from अ + इ, not from अ + अ."),
             ("हिमोचलः", "ओ comes from अ + उ, not from अ + अ.")],
            "हिम + अचलः = हिमाचलः, like च + अत्र = चात्र.",
            "अ + अ → आ.",
            teaches="Short अ + short अ merge into long आ: च + अत्र → चात्र."),
    ],
}

# ---------------------------------------------------------------- unit 4
AUTHORED["4"] = {
    "title": "ज्वरो निहंति बलवान्",
    "question": "By card 4, what kind of fever does the text say kills, and whom?",
    "rule": ("A fever strong (बलवान्), deep (गम्भीरः), long-lasting (दीर्घरात्रिकः), with delirium, giddiness and breathlessness, "
             "kills (निहन्ति) the one who is wasted (क्षीणम्), swollen (शूनम्), whose fire is destroyed (हतानलम्)."),
    "limits": ("High confidence; printed lines 4 and 5. The text says only that such a fever kills; it gives no time, cause or "
               "treatment. By the data, the objects run on into card 5. anala is probably the digestive fire (data's label)."),
    "explain_hi": ("बलवान्, गहरा (गम्भीर) और दीर्घरात्रिक (शब्दशः लम्बी रातों वाला, यानी बहुत दिन चलने वाला) ज्वर, जो प्रलाप, भ्रम और श्वास से युक्त हो, मारता है (निहन्ति)। "
                   "किसे: जो क्षीण है, सूजा हुआ है (शून) और जिसकी अनल (सम्भवतः पाचन की अग्नि) नष्ट हो गई है (हतानल)। "
                   "ज्वर के विशेषण प्रथमा में हैं; क्षीणम्, शूनम्, हतानलम् द्वितीया में कर्म हैं। "
                   "डेटा के अनुसार कर्म कार्ड ५ में आगे चलते हैं। "
                   "सन्धि: ज्वरः + निहन्ति → ज्वरो निहन्ति (अः घोष व्यंजन से पहले → ओ)।"),
    "hook": "बलवान्, गम्भीर, दीर्घरात्रिक ज्वर: क्षीण, शून, हतानल को मारता है।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In card 4, what does निहन्ति mean?",
            ("Kills", "नि-√हन्, present: strikes down, kills."),
            [("Heals", "Nothing of healing is said; नि-√हन् = to strike down."),
             ("Rises", "Rising would be उत्तिष्ठति; निहन्ति = kills."),
             ("Lasts", "Lasting is said by दीर्घरात्रिकः; the verb means kills.")],
            "निहन्ति = kills.",
            "नि-√हन् = to kill."),
        match(1, "Match each word of card 4 to its meaning.",
              [["बलवान्", "strong"], ["गम्भीरः", "deep"], ["दीर्घरात्रिकः", "long-lasting"], ["प्रलाप", "delirium"],
               ["भ्रम", "giddiness"], ["श्वास", "breathlessness"]],
              "बलवान् = strong, गम्भीरः = deep, दीर्घरात्रिकः = long-lasting, प्रलाप = delirium, भ्रम = giddiness, श्वास = breathlessness.",
              "बलवान्, गम्भीरः, दीर्घरात्रिकः, प्रलाप, भ्रम, श्वास."),
        order(2, "Put the words of card 4 in the printed order.",
              ["ज्वरः", "निहन्ति", "बलवान्", "गम्भीरः", "दीर्घरात्रिकः", "सप्रलापभ्रमश्वासः"],
              "Fever; kills; strong; deep; long-lasting; with delirium, giddiness and breathlessness.",
              "ज्वरः → निहन्ति → बलवान् → गम्भीरः → दीर्घरात्रिकः → सप्रलापभ्रमश्वासः.",
              role="extend",
              teaches="The subject ज्वरः and its adjectives are nominative; the verb निहन्ति stands second in the printed line."),
        mcq("discriminate", 3, "By card 4, which word describes the one killed (accusative), not the fever?",
            ("शूनम्", "शूनम् (swollen) is accusative, an object of निहन्ति."),
            [("गम्भीरः", "गम्भीरः is nominative and describes the fever."),
             ("बलवान्", "बलवान् is nominative and describes the fever."),
             ("सप्रलापभ्रमश्वासः", "Nominative: the data takes it with ज्वरः, the fever.")],
            "Nominative -अः / -आन् → the fever; accusative -अम् → the one killed.",
            "क्षीणम्, शूनम्, हतानलम् = objects."),
        mcq("apply", 4, "Why is ज्वरः printed ज्वरो before निहन्ति in card 4?",
            ("अः before a voiced consonant → ओ", "न is a voiced consonant: ज्वरः + निहन्ति → ज्वरो निहन्ति."),
            [("अः before any consonant → ओ", "Not any: before a voiceless त it becomes स् (तुल्यस्तैल-, card 13)."),
             ("आः before a voiced consonant → ओ", "आः drops its visarga before a voiced sound; and the ending here is अः."),
             ("ओ is the nominative ending", "The nominative is ज्वरः; ओ comes only from sandhi.")],
            "ज्वरः + निहन्ति → ज्वरो निहन्ति.",
            "अः + voiced consonant → ओ."),
        mcq("transfer", 5, "By the pattern of ज्वरो निहन्ति, how is शिष्यः + नमति (the pupil bows) written in a new example?",
            ("शिष्यो नमति", "अः before the voiced न → ओ: शिष्यो नमति."),
            [("शिष्य नमति", "Before a voiced consonant अः gives ओ; only a few words such as सः and एषः drop the visarga there."),
             ("शिष्यर्नमति", "र् comes from a visarga after a vowel other than अ/आ; here it follows अ."),
             ("शिष्यस्नमति", "स् comes from a visarga before त or थ, not before न.")],
            "शिष्यः + नमति = शिष्यो नमति, like ज्वरः + निहन्ति = ज्वरो निहन्ति.",
            "अः + voiced consonant → ओ.",
            teaches="अः before a voiced consonant becomes ओ: ज्वरः + निहन्ति → ज्वरो निहन्ति."),
    ],
}

# ---------------------------------------------------------------- unit 5
AUTHORED["5"] = {
    "title": "अक्षामं सक्तवचनं रक्ताक्षं",
    "question": "By card 5, which further marks of the one affected are listed, and when may the very dry cough occur?",
    "rule": ("Objects continue: the one not emaciated (अक्षामम्, as printed), with faltering speech, red eyes and pain in the heart. "
             "Then a new subject: a very dry cough (संशुष्ककासः) that may occur in the forenoon or even the afternoon."),
    "limits": ("Medium confidence; printed lines 6, 7. अक्षामम् (not emaciated) sits oddly beside क्षीणम् (card 4); kṣāmam may "
               "be meant (flag): no question on it. Line 7 does not say what the dry cough does; the data takes it into "
               "the list begun in card 4."),
    "explain_hi": ("पहली पंक्ति कार्ड ४ के कर्म आगे बढ़ाती है: जो अक्षाम (छपे रूप में ‘कृश नहीं’) है, जिसकी वाणी अटकती है (सक्तवचन), जिसकी आँखें लाल हैं और जिसके हृदय में शूल है। "
                   "‘अक्षामम्’ कार्ड ४ के ‘क्षीणम्’ के साथ अटपटा लगता है; ‘क्षामम्’ सम्भव पाठ है, इसलिए उस पर प्रश्न नहीं। "
                   "दूसरी पंक्ति में नया कर्ता है: अत्यन्त सूखी खाँसी (संशुष्ककास), जो पूर्वाह्न में या अपराह्न में भी हो। "
                   "यह खाँसी क्या करती है, यह पंक्ति नहीं कहती। "
                   "सन्धियाँ: यः + अपराह्णे → यो ऽपराह्णे (अः + अ → ओऽ); अपराह्णे + अपि → अपराह्णे ऽपि (ए + अ → एऽ)।"),
    "hook": "अटकती वाणी, लाल आँखें, हृदय में शूल; सूखी खाँसी पूर्वाह्न या अपराह्न में।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 5, what does रक्ताक्षम् describe?",
            ("One with red eyes", "रक्त (red) + अक्ष (eye), a bahuvrīhi: red-eyed."),
            [("One with red skin", "अक्ष here is the eye; skin would be त्वच्."),
             ("One with red lips", "Lips would be ओष्ठ; अक्ष here is the eye."),
             ("One with red nails", "Nails would be नख or करज; अक्ष here is the eye.")],
            "रक्ताक्षम् = red-eyed.",
            "रक्त + अक्ष = red-eyed."),
        match(1, "Match each word of card 5 to its meaning.",
              [["सक्तवचन", "faltering speech"], ["रक्ताक्ष", "red-eyed"], ["शूलिन्", "having pain"],
               ["संशुष्क", "very dry"], ["पूर्वाह्ण", "forenoon"], ["अपराह्ण", "afternoon"]],
              "सक्त-वचन = speech stuck, faltering; रक्ताक्ष = red-eyed; शूलिन् = having pain; संशुष्क = very dry; पूर्वाह्ण = forenoon; अपराह्ण = afternoon.",
              "सक्तवचन, रक्ताक्ष, शूलिन्, संशुष्क, पूर्वाह्ण, अपराह्ण."),
        order(2, "Put these words of card 5 in the printed order.",
              ["सक्तवचनं", "रक्ताक्षं", "हृदि शूलिनं", "संशुष्ककासः", "पूर्वाह्णे", "अपराह्णे"],
              "Faltering speech; red-eyed; pain in the heart; very dry cough; in the forenoon; in the afternoon.",
              "सक्तवचनं → रक्ताक्षं → हृदि शूलिनं → संशुष्ककासः → पूर्वाह्णे → अपराह्णे.",
              role="extend",
              teaches="Line 1 keeps the accusatives of card 4; line 2 opens with a new nominative subject, संशुष्ककासः."),
        mcq("discriminate", 3, "By card 5, when may the very dry cough occur?",
            ("Forenoon, or even afternoon", "पूर्वाह्णे यो ऽपराह्णे ऽपि वा भवेत्: in the forenoon, or even the afternoon."),
            [("Only at midnight and at dawn", "Neither midnight nor dawn is named; the line names forenoon and afternoon."),
             ("Evening, or even at night", "Evening and night are not named; पूर्वाह्ण and अपराह्ण are."),
             ("Only after heavy meals", "No meal is named; the line names times of day.")],
            "पूर्वाह्ण = forenoon, अपराह्ण = afternoon.",
            "पूर्वाह्णे ... अपराह्णे ऽपि वा."),
        mcq("apply", 4, "Which split of पूर्वाह्णेयोऽपराह्णे in card 5 is right?",
            ("पूर्वाह्णे + यः + अपराह्णे", "अः + अ → ओऽ: यः + अपराह्णे → यो ऽपराह्णे."),
            [("पूर्वाह्णे + यो + पराह्णे", "पराह्णे is not the word here; the ऽ marks the lost अ of अपराह्णे."),
             ("पूर्वाह्णेय + अपराह्णे", "पूर्वाह्णेय is not a word; यः (which) stands apart."),
             ("पूर्वाह्ण + इयः + अपराह्णे", "इयः is not a word; पूर्वाह्णे ends in ए (locative).")],
            "पूर्वाह्णे (in the forenoon) + यः (which) + अपराह्णे (in the afternoon).",
            "अः + अ → ओऽ."),
        mcq("transfer", 5, "By the pattern of यः + अपराह्णे → यो ऽपराह्णे, how is मेघः + अत्र (the cloud here) joined in a new example?",
            ("मेघो ऽत्र", "अः + अ → ओ, and the अ is dropped, marked ऽ: मेघो ऽत्र."),
            [("मेघ अत्र", "अः gives अ with a gap only before vowels other than अ; before अ it gives ओऽ."),
             ("मेघरत्र", "र् comes from a visarga after a vowel other than अ/आ; here it follows अ."),
             ("मेघात्र", "Here a visarga stands between the vowels; अः + अ gives ओऽ, not आ.")],
            "मेघः + अत्र = मेघो ऽत्र, like यः + अपराह्णे = यो ऽपराह्णे.",
            "अः + अ → ओऽ.",
            teaches="अः before a short अ becomes ओ, and the अ is dropped and marked ऽ: यः + अपराह्णे → यो ऽपराह्णे."),
    ],
}

# ---------------------------------------------------------------- unit 6
AUTHORED["6"] = {
    "title": "बलमांसविहीनस्य",
    "question": "By card 6, whom does the line describe, and which colours of raktapitta does it name?",
    "rule": ("Of one deprived of strength and flesh, with phlegm-cough (श्लेष्मकास); then raktapitta (a bleeding disorder, "
             "probably): very red, black, with the lustre of the rainbow (Indra's bow)."),
    "limits": ("Medium confidence; printed lines 8, 9. Whether समन्वितः goes with card 5's cough or the person, and whether "
               "भृशम् goes with रक्तम्, are open: no question on either. Printed इद्र- is read इन्द्र-: no question on it. "
               "The discharge is not named."),
    "explain_hi": ("पहली पंक्ति: बल और मांस से रहित व्यक्ति का, श्लेष्मकास (कफ वाली खाँसी) से युक्त; ‘समन्वितः’ कार्ड ५ की सूखी खाँसी से जुड़ता है या व्यक्ति से, यह खुला है। "
                   "दूसरी पंक्ति: रक्तपित्त (सम्भवतः रक्तस्राव का रोग), बहुत लाल, काला, इन्द्रधनुष की आभा वाला। "
                   "ये रंग निकलने वाले रक्त के लगते हैं, पर रक्त का नाम इस पंक्ति में छपा नहीं। "
                   "छपा ‘इद्र’ = इन्द्र (अनुस्वार छूटा)। "
                   "‘श्लेष्मन्’ समास के पहले पद में अपना न् खोकर ‘श्लेष्म-’ बनता है।"),
    "hook": "बल-मांस से हीन, कफ की खाँसी; रक्तपित्त लाल, काला, इन्द्रधनुष-सा।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 6, what does बलमांसविहीनस्य mean?",
            ("Of one without strength and flesh", "बल (strength) + मांस (flesh) + विहीन (deprived of), genitive."),
            [("Of one rich in strength and flesh", "विहीन = deprived of, not rich in."),
             ("Of one who eats only meat", "विहीन = deprived; nothing is said of eating."),
             ("Of one with strong, firm flesh", "बल and मांस are both lost (विहीन), not firm.")],
            "बलमांसविहीनस्य = of one deprived of strength and flesh.",
            "विहीन = deprived of."),
        match(1, "Match each word of card 6 to its meaning.",
              [["बल", "strength"], ["मांस", "flesh"], ["विहीन", "deprived of"], ["भृशम्", "very, greatly"],
               ["कृष्ण", "black"]],
              "बल = strength, मांस = flesh, विहीन = deprived of, भृशम् = very, कृष्ण = black.",
              "बल, मांस, विहीन, भृशम्, कृष्ण."),
        order(2, "Put these words of card 6 in the printed order.",
              ["बलमांसविहीनस्य", "श्लेष्मकाससमन्वितः", "रक्तपित्तं", "भृशं रक्तं", "कृष्णम्"],
              "Of one without strength and flesh; with phlegm-cough; raktapitta; very red; black.",
              "बलमांसविहीनस्य → श्लेष्मकाससमन्वितः → रक्तपित्तं → भृशं रक्तं → कृष्णम्.",
              role="extend",
              teaches="Line 1 describes the person (genitive) and the phlegm-cough; line 2 opens a new head word, रक्तपित्तम्, with its colours."),
        multi("discriminate", 3, "Which colours does card 6 name for the raktapitta?",
              [("शुक्लम् (white)", "No: white is not named in card 6."),
               ("रक्तम् (red)", "Yes: भृशं रक्तम्, very red."),
               ("नीलम् (blue)", "No: blue is not named for the raktapitta."),
               ("कृष्णम् (black)", "Yes: कृष्णम्, black.")],
              [1, 3],
              "Card 6 names very red, black, and the lustre of the rainbow.",
              "भृशं रक्तं, कृष्णम्, इन्द्रधनुःप्रभम्."),
        mcq("apply", 4, "Why is श्लेष्मन् written श्लेष्म- in श्लेष्मकास of card 6?",
            ("Stems in -अन् lose न् in a compound", "As a compound's first member, श्लेष्मन् drops its final न्: श्लेष्म-कास."),
            [("श्लेष्म is the noun's nominative form", "The nominative is श्लेष्मा (card 2); the compound uses the stem without न्."),
             ("न् turns to anusvāra before क", "No anusvāra is printed; the न् is simply dropped."),
             ("Vowel sandhi with क removes न्", "न् is a consonant and क is too; no vowel sandhi applies.")],
            "श्लेष्मन् + कास → श्लेष्मकास.",
            "-अन् stem as first member → न् dropped."),
        mcq("transfer", 5, "By the pattern of श्लेष्मन् → श्लेष्मकास, how is कर्मन् + फल (fruit of action) written as a compound in a new example?",
            ("कर्मफल", "The -अन् stem drops न् in a compound: कर्म-फल."),
            [("कर्मन्फल", "The न् is not kept before the next member."),
             ("कर्मंफल", "No anusvāra: the न् is dropped, not turned to ं."),
             ("कर्माफल", "No lengthening: the stem is कर्म- with short अ.")],
            "कर्मन् + फल = कर्मफल, like श्लेष्मन् + कास = श्लेष्मकास.",
            "-अन् stem as first member → न् dropped.",
            teaches="A stem in -अन् (श्लेष्मन्, कर्मन्) drops its न् as the first member of a compound."),
    ],
}

# ---------------------------------------------------------------- unit 7
AUTHORED["7"] = {
    "title": "ताम्रहारिद्रहरितं रूपं",
    "question": "By card 7, which colours are to be shown, and what does रोमकूपप्रविसृतम् say?",
    "rule": ("It should show (दर्शयेत्) a copper-coloured, turmeric-coloured, green appearance (रूपम्), with रक्तम् (red, or blood); "
             "issued through the hair-pits (रोमकूपप्रविसृतम्); then throat, mouth and heart are named."),
    "limits": ("Low confidence; prose, printed lines 10, 11. No subject is printed (the data: raktapitta of card 6 continues). "
               "रक्तम् may be red or blood: no question on it. Printed सजतं is unclear, not translated: no question on it or "
               "on the throat, mouth and heart."),
    "explain_hi": ("डेटा के अनुसार यह गद्य इकाई दो छपी पंक्तियाँ जोड़ती है। "
                   "पहली: ताँबे के रंग का (ताम्र), हल्दी के रंग का (हारिद्र), हरा (हरित) और रक्त रूप दिखाए (दर्शयेत्); ‘रक्तम्’ लाल रंग भी हो सकता है और रक्त भी। "
                   "कर्ता छपा नहीं; डेटा इसे कार्ड ६ के रक्तपित्त का क्रम मानता है। "
                   "दूसरी: रोमकूपों (रोमछिद्रों) से निकला हुआ; फिर कण्ठ, मुख और हृदय में; अन्तिम छपा शब्द ‘सजतं’ अस्पष्ट है, इसलिए उसका अर्थ नहीं दिया गया। "
                   "‘दर्शयेत्’ √दृश् का प्रेरणार्थक विधिलिङ् है: ‘दिखाए’।"),
    "hook": "ताम्र, हारिद्र, हरित: तीन रंग, और रोमकूपों से निकला।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 7, what does रोमकूप mean?",
            ("Hair-pit", "रोम (body-hair) + कूप (pit): the pit of a hair, a pore."),
            [("Deep well", "With रोम, कूप is the pit of a hair, not a well."),
             ("Hair-lock", "रोम is body-hair; कूप adds the pit, not a lock."),
             ("Skin-wound", "No wound is named; रोमकूप is the pit of a hair.")],
            "रोमकूप = hair-pit, pore.",
            "रोम + कूप = hair-pit."),
        match(1, "Match each word of card 7 to its meaning.",
              [["ताम्र", "copper-coloured"], ["हारिद्र", "turmeric-coloured"], ["हरित", "green"], ["रूप", "appearance"],
               ["दर्शयेत्", "should show"]],
              "ताम्र = copper-coloured, हारिद्र = turmeric-coloured, हरित = green, रूप = appearance, दर्शयेत् = should show.",
              "ताम्र, हारिद्र, हरित, रूप, दर्शयेत्."),
        order(2, "Put these sure words of card 7 in the printed order.",
              ["ताम्र", "हारिद्र", "हरितं", "रूपं", "दर्शयेत्", "रोमकूपप्रविसृतं"],
              "Copper-coloured; turmeric-coloured; green; appearance; should show; issued through the hair-pits.",
              "ताम्र → हारिद्र → हरितं → रूपं → दर्शयेत् → रोमकूपप्रविसृतं.",
              role="extend",
              teaches="Line 1 lists the colours first, then the noun रूपम् and the verb दर्शयेत्; line 2 begins with रोमकूपप्रविसृतम्."),
        mcq("discriminate", 3, "How is हारिद्र in card 7 related to हरिद्रा (turmeric)?",
            ("Adjective: turmeric-coloured", "Its first vowel is strengthened (अ → आ): हारिद्र = of turmeric, turmeric-coloured."),
            [("Plural noun: many turmerics", "The plural would be हरिद्राः; हारिद्र is a derived adjective."),
             ("Verb: it dyes with turmeric", "हारिद्र goes with रूपम् as an adjective; the verb is दर्शयेत्."),
             ("Negation: not turmeric-like", "No negation is added; the strengthened vowel marks 'of, from'.")],
            "हरिद्रा → हारिद्र: a derived adjective, turmeric-coloured.",
            "Strengthened first vowel → adjective 'of, from'."),
        mcq("apply", 4, "In card 7, दर्शयेत् is a causative of √दृश् (to see). What does it mean?",
            ("Should show", "Causative of 'see' = make seen, show; -एत् optative: should show."),
            [("Should see", "That is the plain optative पश्येत्; the causative means show."),
             ("Is seen", "The passive would be दृश्यते; दर्शयेत् is an active causative."),
             ("Has been seen", "-एत् marks the optative, not a past.")],
            "दर्शयेत् = should show.",
            "Causative of √दृश् = show."),
        mcq("transfer", 5, "By the pattern of हरिद्रा → हारिद्र, what does पार्थिव (from पृथिवी, earth) mean in a new example?",
            ("Of the earth", "First vowel strengthened (ऋ → आर्): पार्थिव = of the earth."),
            [("Without earth", "No negation; the strengthened vowel means 'of, from'."),
             ("Earth itself", "The derived form describes; it is not the noun पृथिवी."),
             ("Far from earth", "Nothing marks distance; the form means 'of the earth'.")],
            "पार्थिव = of the earth, like हारिद्र = of turmeric.",
            "Strengthened first vowel → 'of, from'.",
            teaches="Strengthening the first vowel (vṛddhi) makes an adjective 'of, from': हरिद्रा → हारिद्र, turmeric-coloured."),
    ],
}

# ---------------------------------------------------------------- unit 8
AUTHORED["8"] = {
    "title": "वाससो रंजनं पूति",
    "question": "By card 8, which qualities are listed in line 1, and which ailments are named in line 2?",
    "rule": ("Line 1: staining (रञ्जनम्) of cloth (वाससः), putrid (पूति), forceful (वेगवत्) and very abundant (अतिभूरि). "
             "Line 2: the one with pāṇḍu (anaemia with pallor, standard), fever, vomiting, cough, swelling and diarrhoea."),
    "limits": ("Low confidence; printed lines 12 and 13. Line 1 names no subject (the data takes it as the discharge of cards 6-7). "
               "Printed छर्द्दं is unclear and not translated: no question on it. The verb of line 2 is carried over from card 4 "
               "(data); none is supplied."),
    "explain_hi": ("पहली पंक्ति: वस्त्र का रंगना (वाससो रञ्जनम्), सड़ा हुआ (पूति), वेग वाला (वेगवत्) और बहुत अधिक (अतिभूरि)। "
                   "किसका, यह छपा नहीं; डेटा इसे कार्ड ६-७ के स्राव का क्रम मानता है। "
                   "दूसरी पंक्ति का पहला शब्द ‘छर्द्दं’ अस्पष्ट है, इसलिए उसका अर्थ नहीं दिया गया। "
                   "फिर एक लम्बा समास: पाण्डु (रक्ताल्पता, मानक), ज्वर, छर्दि (उल्टी), कास, शोफ (सूजन) और अतिसार वाले को; -इन् = ‘वाला’। "
                   "सन्धियाँ: वेगवत् + च → वेगवच्च (च से पहले त् → च्); च + अति- → चाति- (अ + अ → आ)।"),
    "hook": "कपड़ा रँगे, सड़ा, वेग से, बहुत; पाण्डु, ज्वर, छर्दि, कास, शोफ, अतिसार।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 8, what does वाससः रञ्जनम् mean?",
            ("Staining of cloth", "वाससः (of cloth) + रञ्जनम् (colouring, staining)."),
            [("Washing of cloth", "Washing would be क्षालन; रञ्जन = colouring."),
             ("Tearing of cloth", "Nothing is torn; रञ्जन = colouring, staining."),
             ("Drying of cloth", "Drying would be शोषण; रञ्जन = staining.")],
            "वाससो रञ्जनम् = staining of cloth.",
            "रञ्जन = colouring, staining."),
        match(1, "Match each word of card 8 to its meaning.",
              [["पूति", "putrid"], ["वेगवत्", "forceful"], ["अतिभूरि", "very abundant"],
               ["पाण्डु", "anaemia with pallor"], ["शोफ", "swelling"]],
              "पूति = putrid, वेगवत् = forceful, अतिभूरि = very abundant, पाण्डु = anaemia with pallor (standard), शोफ = swelling.",
              "पूति, वेगवत्, अतिभूरि, पाण्डु, शोफ."),
        order(2, "Put the members of the long compound in line 2 of card 8 in the printed order.",
              ["पाण्डु", "ज्वर", "छर्दि", "कास", "शोफ", "अतिसारिणम्"],
              "Pāṇḍu; fever; vomiting; cough; swelling; having diarrhoea.",
              "पाण्डु → ज्वर → छर्दि → कास → शोफ → अतिसारिणम्.",
              role="extend",
              teaches="A long dvandva lists the ailments; the possessive -इन् at its end (अतिसारिन्) makes the whole mean 'the one having ...'."),
        mcq("discriminate", 3, "Which split of वेगवच्चातिभूरि in card 8 is right?",
            ("वेगवत् + च + अतिभूरि", "त् before च → च्; अ + अ → आ: वेगवच्चातिभूरि."),
            [("वेगवत् + चाति + भूरि", "चाति is not a word; च and अति have joined."),
             ("वेगव + च्च + अतिभूरि", "च्च is not a word; the first च् comes from the त् of वेगवत्."),
             ("वेगवत् + च + आतिभूरि", "आतिभूरि is not a word; the prefix is अति, with short अ.")],
            "वेगवत् (forceful) + च (and) + अतिभूरि (very abundant).",
            "त् + च → च्च; अ + अ → आ."),
        mcq("apply", 4, "What does the ending -इन् of -अतिसारिणम् in card 8 add?",
            ("Having it: one who has", "-इन् is possessive: अतिसारिन् = one having diarrhoea."),
            [("Without it: one who lacks", "Lacking would need a prefix like निर्- or अ-."),
             ("Like it: one who resembles", "Likeness would be -वत् or -आभ."),
             ("Causing it in another", "-इन् marks having, not causing.")],
            "अतिसार + इन् = one having diarrhoea.",
            "-इन् = having."),
        mcq("transfer", 5, "By the pattern of अतिसारिन् (one having diarrhoea), what does दण्डिन् mean in a new example?",
            ("One having a staff", "-इन् = having: दण्ड (staff) + इन् = one having a staff."),
            [("One without a staff", "Without would need a prefix like निर्-; -इन् means having."),
             ("One like a staff", "Like would be दण्डवत्; -इन् means having."),
             ("One who breaks staffs", "-इन् marks having, not breaking.")],
            "दण्डिन् = one having a staff, like अतिसारिन् = one having diarrhoea.",
            "-इन् = having.",
            teaches="-इन् added to a noun means 'having': अतिसारिन् = having diarrhoea."),
    ],
}

# ---------------------------------------------------------------- unit 9
AUTHORED["9"] = {
    "title": "कासश्वासौ",
    "question": "By card 9, which signs go with cough and breathlessness, and which with yakṣman?",
    "rule": ("Line 1: cough and breathlessness (कासश्वासौ, dual); the one with fever, vomiting, thirst, diarrhoea and swelling. "
             "Line 2: yakṣman (consumption, probably tuberculosis); the one with pain in the side, distension, vomiting of blood."),
    "limits": ("Medium confidence; printed lines 14 and 15. Elliptical: the verb (निहन्ति, card 4) is carried over, not printed. "
               "The last word, असंतापिन् (without burning heat), has an unclear sense in this list: no question on it. "
               "yakṣman = probably tuberculosis (data's label)."),
    "explain_hi": ("दोनों पंक्तियों में क्रिया नहीं छपी; डेटा के अनुसार कार्ड ४ की ‘निहन्ति’ आगे चलती है। "
                   "पहली पंक्ति: कास और श्वास (द्विवचन), उसको जो ज्वर, छर्दि, तृष्णा, अतीसार और शोफ से युक्त है। "
                   "दूसरी पंक्ति: यक्ष्मा (यक्ष्मन्, सम्भवतः क्षय रोग), उसको जिसे पार्श्व में पीड़ा, आनाह (पेट का तनाव) और रक्त की उल्टी है, और जो असंतापी (ताप से रहित) है। "
                   "इस अन्तिम शब्द का अर्थ इस सूची में स्पष्ट नहीं, इसलिए उस पर प्रश्न नहीं। "
                   "सन्धियाँ: तृष्णा + अतीसार → तृष्णातीसार (आ + अ → आ); छर्दि + असंतापिनम् → छर्द्यसंतापिनम् (इ + अ → य)।"),
    "hook": "कास-श्वास: ज्वर, छर्दि, तृष्णा, अतीसार, शोफ; यक्ष्मा: पार्श्वपीड़ा, आनाह, रक्त की उल्टी।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In card 9, what does कासश्वासौ name?",
            ("Cough and breathlessness", "कास-श्वासौ: a dvandva in the dual, the two together."),
            [("Fever and vomiting together", "Those are members of the next compound (ज्वरच्छर्दि-)."),
             ("Thirst and bodily swelling", "Those are members of the next compound too."),
             ("Hiccup and abdominal bloating", "Neither is in कासश्वासौ; कास = cough, श्वास = breathlessness.")],
            "कासश्वासौ = cough and breathlessness.",
            "कास = cough, श्वास = breathlessness."),
        match(1, "Match each word of card 9 to its meaning.",
              [["पार्श्वरुज्", "pain in the side"], ["आनाह", "distension"], ["रक्तच्छर्दि", "vomiting of blood"],
               ["तृष्णा", "thirst"], ["शोफ", "swelling"]],
              "पार्श्व-रुज् = side-pain, आनाह = distension, रक्त-छर्दि = vomiting of blood, तृष्णा = thirst, शोफ = swelling.",
              "पार्श्वरुज्, आनाह, रक्तच्छर्दि, तृष्णा, शोफ."),
        order(2, "Put the members of the first long compound of card 9 in the printed order.",
              ["ज्वर", "छर्दि", "तृष्णा", "अतीसार", "शोफिनम्"],
              "Fever; vomiting; thirst; diarrhoea; having swelling.",
              "ज्वर → छर्दि → तृष्णा → अतीसार → शोफिनम्.",
              role="extend",
              teaches="The ailments stand in one dvandva; the possessive ending of its last member (शोफिन्) makes it 'the one having ...'."),
        multi("discriminate", 3, "By card 9, which signs belong to the yakṣman line (line 2), not to line 1?",
              [("पार्श्वरुज् (pain in the side)", "Yes: पार्श्वरुज् is in line 2."),
               ("ज्वर (fever)", "No: fever is in line 1."),
               ("आनाह (distension)", "Yes: आनाह is in line 2."),
               ("तृष्णा (thirst)", "No: thirst is in line 1.")],
              [0, 2],
              "Line 2 (yakṣman): pain in the side, distension, vomiting of blood.",
              "यक्ष्मा → पार्श्वरुज्, आनाह, रक्तच्छर्दि."),
        mcq("apply", 4, "Which split of तृष्णातीसार in card 9 is right?",
            ("तृष्णा + अतीसार", "आ + अ → आ: तृष्णा + अतीसार → तृष्णातीसार."),
            [("तृष्णात् + ईसार", "ईसार is not a word; the noun is अतीसार."),
             ("तृष्णा + तीसार", "तीसार is not a word; अतीसार (diarrhoea) is."),
             ("तृष्णा + आतीसार", "आतीसार is not a word; the print has अतीसार, with अ.")],
            "तृष्णा (thirst) + अतीसार (diarrhoea).",
            "आ + अ → आ."),
        mcq("transfer", 5, "By the pattern of कासश्वासौ (a dual dvandva), how are राम and लक्ष्मण joined as a dual dvandva in a new example?",
            ("रामलक्ष्मणौ", "A dvandva of two takes the dual ending on its last member only: रामलक्ष्मणौ."),
            [("रामलक्ष्मणः", "-अः is singular; two persons need the dual."),
             ("रामलक्ष्मणाः", "-आः is plural; two persons need the dual."),
             ("रामौलक्ष्मणौ", "Only the last member takes the ending; राम stays a bare stem.")],
            "राम + लक्ष्मण = रामलक्ष्मणौ, like कास + श्वास = कासश्वासौ.",
            "Dvandva of two → dual ending on the last member.",
            teaches="A dvandva naming two things takes the dual ending on its last member: कास + श्वास → कासश्वासौ."),
    ],
}

# ---------------------------------------------------------------- unit 10
AUTHORED["10"] = {
    "title": "छर्द्दिर्वेगवती",
    "question": "By line 1 of card 10, what is said of the vomiting (छर्दि)?",
    "rule": ("Vomiting (छर्दिः), forceful (वेगवती), smelling of urine and faeces (मूत्रशकृद्गन्धिः), with candrikā (literally "
             "moonlight; its sense here is uncertain). Line 2 is damaged."),
    "limits": ("Low confidence; prose, printed lines 16, 17. What candrikā names is not stated: no question on it. Line 2 is "
               "damaged: सास्र (blood or tears), the unclear compound and गुंषिणो carry no question. That it continues "
               "card 9's yakṣman list is the data's guess."),
    "explain_hi": ("पहली पंक्ति स्पष्ट है: छर्दि (उल्टी) वेगवती, मूत्र और मल (शकृत्) की गन्ध वाली और चन्द्रिका सहित; चन्द्रिका का शब्दार्थ चाँदनी है, पर यहाँ उसका अर्थ अस्पष्ट है। "
                   "दूसरी पंक्ति क्षतिग्रस्त है: ‘सास्र’ में अस्र रक्त या आँसू हो सकता है, और लम्बा समास तथा ‘गुंषिणो’ अस्पष्ट हैं, इसलिए उन पर प्रश्न नहीं। "
                   "डेटा के अनुसार यह सम्भवतः कार्ड ९ की यक्ष्मा-सूची का क्रम है, पर यह निश्चित नहीं। "
                   "‘वेगवती’ स्त्रीलिंग है, क्योंकि छर्दि स्त्रीलिंग है। "
                   "सन्धियाँ: छर्दिः + वेगवती → छर्दिर्वेगवती (इ के बाद विसर्ग, घोष व से पहले → र्); शकृत् + गन्धि → शकृद्गन्धि (घोष ग से पहले त् → द्)।"),
    "hook": "वेगवती छर्दि, मूत्र-मल की गन्ध वाली; पंक्ति २ क्षतिग्रस्त।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 10, what does शकृत् mean?",
            ("Faeces", "शकृत् = faeces, stool."),
            [("Urine", "Urine is मूत्र, named just before."),
             ("Blood", "Blood would be रक्त or असृक्; शकृत् = faeces."),
             ("Mucus", "Mucus is not named here; शकृत् = faeces.")],
            "शकृत् = faeces.",
            "मूत्र = urine, शकृत् = faeces."),
        match(1, "Match each word of card 10 to its meaning.",
              [["छर्दि", "vomiting"], ["वेगवती", "forceful"], ["मूत्र", "urine"], ["शकृत्", "faeces"],
               ["गन्धि", "smelling of"]],
              "छर्दि = vomiting, वेगवती = forceful, मूत्र = urine, शकृत् = faeces, गन्धि = smelling of.",
              "छर्दि, वेगवती, मूत्र, शकृत्, गन्धि."),
        order(2, "Put the words of line 1 of card 10 in the printed order.",
              ["छर्दिः", "वेगवती", "मूत्रशकृद्गन्धिः", "सचन्द्रिका"],
              "Vomiting; forceful; smelling of urine and faeces; with candrikā.",
              "छर्दिः → वेगवती → मूत्रशकृद्गन्धिः → सचन्द्रिका.",
              role="extend",
              teaches="Line 1 is a noun with three qualities, each feminine to agree with छर्दिः."),
        mcq("discriminate", 3, "Why is शकृत् printed शकृद् before गन्धिः in card 10?",
            ("त् before voiced ग → द्", "ग is voiced, so त् becomes voiced द्: शकृद्गन्धिः."),
            [("त् before any consonant → द्", "Not any: before a voiceless one it stays त्, as in यकृत्पिण्ड- (card 13)."),
             ("द् is the stem's own final", "The stem is शकृत्; द् comes only from sandhi."),
             ("द् marks a case ending here", "No case is shown; शकृत् is a member inside the compound.")],
            "शकृत् + गन्धि → शकृद्गन्धि.",
            "त् + voiced consonant → द्."),
        mcq("apply", 4, "Why is the adjective वेगवती, not वेगवत्, in card 10?",
            ("It agrees with feminine छर्दिः", "-वत् makes -वती in the feminine; छर्दिः is feminine."),
            [("It is a verb in the present", "वेगवती is an adjective; line 1 has no verb."),
             ("Its -ई ending marks the dual", "It describes one छर्दिः: nominative singular."),
             ("Its -ई ending marks the locative", "The locative of वेगवत् (masc./neut.) would be वेगवति; this is nominative.")],
            "छर्दिः (f.) → वेगवती (f.).",
            "-वत् → feminine -वती."),
        mcq("transfer", 5, "By the pattern of छर्दिः वेगवती, which form of बलवत् (strong) goes with the feminine नारी in a new example?",
            ("बलवती", "-वत् adjectives take -वती in the feminine: नारी बलवती."),
            [("बलवान्", "बलवान् is masculine (as in card 4)."),
             ("बलवत्", "बलवत् is the stem or the neuter form."),
             ("बलवता", "बलवता is the instrumental singular.")],
            "नारी बलवती, like छर्दिः वेगवती.",
            "-वत् → feminine -वती.",
            teaches="-वत् adjectives take -वती in the feminine: वेगवत् → वेगवती with छर्दिः."),
    ],
}

# ---------------------------------------------------------------- unit 11
AUTHORED["11"] = {
    "title": "तृष्णाऽन्यरोगक्षपितं",
    "question": "By card 11, which marks go with thirst, and which with madātyaya?",
    "rule": ("Line 1: thirst (तृष्णा); the one worn down by other ailments, with the tongue outside, unconscious. Line 2: madātyaya "
             "(probably an alcohol-related disorder); the one afflicted by great cold, wasted, whose face has the lustre of oil."),
    "limits": ("Medium confidence; printed lines 18 and 19. Elliptical: the verb is carried over (data). madātyaya is a probable "
               "identification. The line gives no cause, time or treatment."),
    "explain_hi": ("पहली पंक्ति: तृष्णा (प्यास), उसको जो दूसरे रोगों से क्षीण किया गया है (अन्यरोगक्षपित), जिसकी जीभ बाहर निकली है (बहिर्जिह्व) और जो अचेत है (विचेतन)। "
                   "दूसरी पंक्ति: मदात्यय (सम्भवतः मद्य से उत्पन्न रोग), उसको जो अत्यन्त शीत से पीड़ित, क्षीण और तेल जैसी चमक वाले मुख वाला है। "
                   "क्रिया नहीं छपी; डेटा के अनुसार वह पीछे से चली आती है। "
                   "‘बहिर्जिह्व’ बहुव्रीहि है: जिसकी जीभ बाहर है। "
                   "सन्धियाँ: मदात्ययः + अति- → मदात्ययो ऽति- (अः + अ → ओऽ); शीत + आर्त → शीतार्त (अ + आ → आ)।"),
    "hook": "तृष्णा: जीभ बाहर, अचेत; मदात्यय: बहुत ठंड, तेल-सा चमकता मुख।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 11, what does बहिर्जिह्वम् describe?",
            ("His tongue is outside", "बहिः (outside) + जिह्वा (tongue), a bahuvrīhi: one whose tongue is outside."),
            [("His tongue is very dry", "Dryness (शोष) is not said here; बहिः = outside."),
             ("His tongue is red", "No colour is named; बहिः = outside."),
             ("He cannot speak at all", "Speech is not named; जिह्वा = tongue, बहिः = outside.")],
            "बहिर्जिह्वम् = one whose tongue is outside.",
            "बहिः = outside, जिह्वा = tongue."),
        match(1, "Match each word of card 11 to its meaning.",
              [["अन्यरोगक्षपित", "worn down by other ailments"], ["विचेतन", "unconscious"],
               ["अतिशीतार्त", "afflicted by great cold"], ["क्षीण", "wasted"], ["तैलप्रभानन", "with a face of oily lustre"]],
              "अन्य-रोग-क्षपित = worn down by other ailments, विचेतन = unconscious, अति-शीत-आर्त = afflicted by great cold, क्षीण = wasted, तैल-प्रभा-आनन = face with oily lustre.",
              "अन्यरोगक्षपित, विचेतन, अतिशीतार्त, क्षीण, तैलप्रभानन."),
        order(2, "Put these words of card 11 in the printed order.",
              ["तृष्णा", "अन्यरोगक्षपितं", "बहिर्जिह्वं", "विचेतनं", "मदात्ययः", "अतिशीतार्तं"],
              "Thirst; worn down by other ailments; tongue outside; unconscious; madātyaya; afflicted by great cold.",
              "तृष्णा → अन्यरोगक्षपितं → बहिर्जिह्वं → विचेतनं → मदात्ययः → अतिशीतार्तं.",
              role="extend",
              teaches="Each line opens with a nominative ailment (तृष्णा, मदात्ययः), followed by accusatives describing the person."),
        mcq("discriminate", 3, "By card 11, which describes the person in the madātyaya line, not the thirst line?",
            ("An oily-lustred face", "तैलप्रभाननम्, in line 2, with madātyaya."),
            [("The tongue held outside", "बहिर्जिह्वम् is in the thirst line."),
             ("Being unconscious", "विचेतनम् is in the thirst line."),
             ("Worn down by other ills", "अन्यरोगक्षपितम् is in the thirst line.")],
            "Thirst: worn down, tongue outside, unconscious. Madātyaya: great cold, wasted, oily-lustred face.",
            "मदात्यय → अतिशीतार्त, क्षीण, तैलप्रभानन."),
        mcq("apply", 4, "Which split of अतिशीतार्तं in card 11 is right?",
            ("अति + शीत + आर्तम्", "अ + आ → आ: शीत + आर्तम् → शीतार्तम्."),
            [("अतिशी + तार्तम्", "Neither part is a word."),
             ("अति + शीता + र्तम्", "र्तम् is not a word; आर्तम् (afflicted) is."),
             ("अति + शीतः + आर्तम्", "अः before आ would print शीत आर्तम् with a gap; in a compound the stem is शीत.")],
            "अति (very) + शीत (cold) + आर्तम् (afflicted).",
            "अ + आ → आ."),
        mcq("transfer", 5, "By the pattern of बहिर्जिह्व (one whose tongue is outside), what does दीर्घबाहुः पुरुषः mean in a new example?",
            ("A man whose arms are long", "Bahuvrīhi: दीर्घ (long) + बाहु (arm): one whose arms are long."),
            [("A man whose arms are cut", "Cut would be छिन्न; दीर्घ = long."),
             ("A man without any arms", "Without would need निर्- or वि-; दीर्घ = long."),
             ("A man whose arms are short", "Short would be ह्रस्व; दीर्घ = long.")],
            "दीर्घबाहुः = one whose arms are long, like बहिर्जिह्व = one whose tongue is outside.",
            "Bahuvrīhi: describes a person by a part of him.",
            teaches="A bahuvrīhi describes a person by a part of him: बहिर्जिह्व = one whose tongue is outside."),
    ],
}

# ---------------------------------------------------------------- unit 12
AUTHORED["12"] = {
    "title": "अर्शासि पाणिपन्नाभि",
    "question": "By card 12, where is the swelling named with arśas, and which pains and afflictions follow?",
    "rule": ("Arśas (haemorrhoids, piles; standard): the one with swelling of hands, feet, navel, anus, testicles and mouth; "
             "the one afflicted by pain of heart, side and limbs, vomiting, inflammation of the anus, and fever."),
    "limits": ("Medium confidence; printed lines 20 and 21. Elliptical: the verb is carried over (data). Printed अर्शासि is read "
               "अर्शांसि, and पार्श्वंग as पार्श्वाङ्ग (flags): no question on these. The grouping of the second compound can "
               "go two ways: no question on it."),
    "explain_hi": ("अर्श (बवासीर, मानक): हाथ, पैर, नाभि, गुदा, मुष्क (वृषण) और मुख में सूजन वाले को; "
                   "और हृदय, पार्श्व तथा अंगों में पीड़ा, छर्दि, पायु (गुदा) के पाक (शब्दशः पकना) और ज्वर से पीड़ित को। "
                   "क्रिया नहीं छपी; डेटा के अनुसार वह पीछे से चली आती है। "
                   "छपा ‘अर्शासि’ = अर्शांसि (अनुस्वार छूटा) और ‘पार्श्वंग’ = पार्श्वाङ्ग (पाठ-चिह्न), इसलिए उन पर प्रश्न नहीं। "
                   "सन्धियाँ: पद् + नाभि → पन्नाभि (नासिक्य न से पहले द् विकल्प से न् बनता है; ‘पद्नाभि’ भी शुद्ध है); "
                   "हृद् + पार्श्व → हृत्पार्श्व (अघोष प से पहले द् → त्)।"),
    "hook": "अर्श: हाथ, पैर, नाभि, गुदा, मुष्क, मुख में शोफ; हृदय-पार्श्व-अंग में पीड़ा।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In card 12, what does पाणि mean?",
            ("Hand", "पाणि = hand, the first member of the swelling list."),
            [("Foot", "Foot is पद्, the next member (पन्-नाभि)."),
             ("Navel", "Navel is नाभि, after पद्."),
             ("Mouth", "Mouth is आस्य, the last member.")],
            "पाणि = hand.",
            "पाणि = hand."),
        match(1, "Match each word of card 12 to its meaning.",
              [["पद्", "foot"], ["नाभि", "navel"], ["गुद", "anus"], ["मुष्क", "testicle"], ["आस्य", "mouth"]],
              "पद् = foot, नाभि = navel, गुद = anus, मुष्क = testicle, आस्य = mouth.",
              "पद्, नाभि, गुद, मुष्क, आस्य."),
        order(2, "Put the swelling sites of card 12 in the printed order.",
              ["पाणि", "पद्", "नाभि", "गुद", "मुष्क", "आस्य"],
              "Hand; foot; navel; anus; testicle; mouth.",
              "पाणि → पद् → नाभि → गुद → मुष्क → आस्य.",
              role="extend",
              teaches="The swelling sites run through one dvandva ending in -शोफिन् (having swelling)."),
        mcq("discriminate", 3, "Which split of पाणिपन्नाभि- in card 12 is right?",
            ("पाणि + पद् + नाभि", "द् before the nasal न may become न्: पद् + नाभि → पन्नाभि (पद्नाभि is also correct)."),
            [("पाणि + पन्न + अभि", "अभि is a prefix, not a body part; the list names नाभि (navel)."),
             ("पाणिप + नाभि", "पाणिप is not a word; पाणि and पद् are two members."),
             ("पा + णिपन् + नाभि", "Neither पा nor णिपन् is a member of this list.")],
            "पाणि (hand) + पद् (foot) + नाभि (navel).",
            "द् + न → न्न (optional; द्न also correct)."),
        mcq("apply", 4, "Why is हृद् (heart) printed हृत् before पार्श्व in card 12?",
            ("द् before a voiceless प → त्", "प is voiceless, so the voiced द् becomes voiceless त्: हृत्पार्श्व-."),
            [("द् before any consonant → त्", "Not any: before the nasal न of नाभि the same card shows न् (पन्नाभि)."),
             ("त् is the stem's own final", "The stem is हृद्; त् comes only from sandhi."),
             ("त् marks the locative case", "No case is shown; हृद् is a compound's first member.")],
            "हृद् + पार्श्व → हृत्पार्श्व.",
            "Voiced stop + voiceless consonant → voiceless stop."),
        mcq("transfer", 5, "By the pattern of हृद् + पार्श्व → हृत्पार्श्व, how is शरद् + कालः (autumn-time) joined in a new example?",
            ("शरत्कालः", "द् before the voiceless क → त्: शरत्कालः."),
            [("शरद्कालः", "द् does not stay voiced before the voiceless क."),
             ("शरन्कालः", "न् could come only before a nasal; क is not one."),
             ("शरक्कालः", "द् does not take the form of क; it only loses its voice.")],
            "शरद् + कालः = शरत्कालः, like हृद् + पार्श्व = हृत्पार्श्व.",
            "Voiced stop + voiceless consonant → voiceless stop.",
            teaches="A voiced stop before a voiceless consonant becomes voiceless: हृद् + पार्श्व → हृत्पार्श्व."),
    ],
}

# ---------------------------------------------------------------- unit 13
AUTHORED["13"] = {
    "title": "अतीसारो यकृत्पिंड",
    "question": "By card 13, with what is the diarrhoea described, and to what is it said to be similar?",
    "rule": ("Diarrhoea (अतीसारः): with (or like) liver-lumps, meat-washings and dark ones (मेचक); similar (तुल्यः) to oil, ghee, "
             "milk, curd, marrow, fat and āsava (a fermented liquor)."),
    "limits": ("Medium confidence; printed lines 22 and 23. Whether the instrumentals of line 1 mean 'with' or are completed by "
               "तुल्यः ('like') is open: no question on it. मेचक has no stated noun. By the data the sentence runs on into "
               "card 14; the line prints no verb."),
    "explain_hi": ("अतीसार (दस्त, मानक) का वर्णन: यकृत् के पिण्डों (यकृत्पिण्ड), मांस के धोवन (मांसधावन) और गहरे नीले-काले (मेचक) से; "
                   "और तेल, घी, दूध, दही, मज्जा, वसा (चर्बी) तथा आसव (किण्वित पेय) के तुल्य (समान)। "
                   "पहली पंक्ति की तृतीया विभक्तियाँ ‘से युक्त’ भी हो सकती हैं और ‘तुल्यः’ के साथ ‘जैसा’ भी; डेटा इसे खुला छोड़ता है। "
                   "मेचक के साथ कोई संज्ञा नहीं छपी। डेटा के अनुसार वाक्य कार्ड १४ में आगे चलता है। "
                   "सन्धियाँ: अतीसारः + यकृत् → अतीसारो यकृत् (अः घोष य से पहले → ओ); तुल्यः + तैल- → तुल्यस्तैल- (त से पहले ः → स्)।"),
    "hook": "अतीसार: यकृत्पिण्ड, मांसधावन, मेचक; तेल-घी-दूध-दही-मज्जा-वसा-आसव के तुल्य।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 13, what does तुल्यः mean?",
            ("Similar", "तुल्य = similar, equal."),
            [("Different", "Different would be भिन्न; तुल्य = similar."),
             ("Mixed", "Mixed would be मिश्र; तुल्य = similar."),
             ("Heavy", "Heavy would be गुरु; तुल्य = similar.")],
            "तुल्यः = similar.",
            "तुल्य = similar, equal."),
        match(1, "Match each word of card 13 to its meaning.",
              [["तैल", "oil"], ["घृत", "ghee"], ["क्षीर", "milk"], ["दधि", "curd"], ["वसा", "fat"],
               ["आसव", "a fermented liquor"]],
              "तैल = oil, घृत = ghee, क्षीर = milk, दधि = curd, वसा = fat, आसव = a fermented liquor.",
              "तैल, घृत, क्षीर, दधि, वसा, आसव."),
        order(2, "Put these members of the second-line compound of card 13 in the printed order.",
              ["तैल", "घृत", "क्षीर", "दधि", "मज्ज", "वसा"],
              "Oil; ghee; milk; curd; marrow; fat (then āsava ends the compound).",
              "तैल → घृत → क्षीर → दधि → मज्ज → वसा.",
              role="extend",
              teaches="Line 2 lists the likenesses in one dvandva in the instrumental plural (-आसवैः), after तुल्यः."),
        mcq("discriminate", 3, "Why is तुल्यः printed तुल्यस् before तैल- in card 13?",
            ("ः before voiceless त → स्", "A visarga before त or थ becomes स्: तुल्यस्तैल-."),
            [("ः before any consonant → स्", "Not any: before the voiced य it gives ओ (अतीसारो यकृत्, same card)."),
             ("स् is part of the stem", "The stem is तुल्य; स् comes only from sandhi."),
             ("ः before a voiced sound → स्", "त is voiceless; before a voiced consonant अः gives ओ.")],
            "तुल्यः + तैल- → तुल्यस्तैल-.",
            "ः + त/थ → स्."),
        multi("apply", 4, "Which words of card 13 are in the instrumental plural (ending -ऐः)?",
              [("अतीसारः", "No: अतीसारः is nominative singular."),
               ("तुल्यः", "No: तुल्यः is nominative singular."),
               ("-मेचकैः", "Yes: -ऐः on an अ-stem marks the instrumental plural."),
               ("-आसवैः", "Yes: -ऐः on an अ-stem marks the instrumental plural.")],
              [2, 3],
              "The two long compounds end in -ऐः (instrumental plural); अतीसारः and तुल्यः are nominative singular.",
              "-ऐः = instrumental plural of an अ-stem."),
        mcq("transfer", 5, "By the pattern of तुल्यस्तैल-, how is बालः + तिष्ठति (the boy stands) written in a new example?",
            ("बालस्तिष्ठति", "ः before the voiceless त → स्: बालस्तिष्ठति."),
            [("बालो तिष्ठति", "ओ comes before a voiced consonant; त is voiceless."),
             ("बालर्तिष्ठति", "र् comes after vowels other than अ/आ, before a voiced sound."),
             ("बाल तिष्ठति", "The visarga is not dropped before त; it becomes स्.")],
            "बालः + तिष्ठति = बालस्तिष्ठति, like तुल्यः + तैल- = तुल्यस्तैल-.",
            "ः + त/थ → स्.",
            teaches="A visarga before त or थ becomes स्: तुल्यः + तैल- → तुल्यस्तैल-."),
    ],
}

# ================================================================ NOTES_HI
NOTES_HI = {
    "1": ("गद्य; विश्वास उच्च; एक छपी पंक्ति (०२.११.१); कोई पाठ-चिह्न नहीं। अध्याय का नाम ‘विकृतव्याधिविज्ञानीय’; ‘विकृत’ का शब्दार्थ (बदला हुआ, असामान्य) लिया गया। "
          "अध्याय का विषय इस पंक्ति में नहीं कहा गया, इसलिए जोड़ा नहीं गया। छपा ‘-यमध्यायं’ = -यम् + अध्यायम्। "
          "सन्धि जाँची: अथ + अतः → अथातः (अ + अ → आ); अतः + वि- → अतो वि- (अः घोष व्यंजन से पहले → ओ); -विज्ञानीयम् + अध्यायम् → -विज्ञानीयमध्यायम् "
          "(म् स्वर से जुड़ता है); अध्यायम् + व्या- → अध्यायं व्या- (व्यंजन से पहले म् → ं)।"),
    "2": ("गद्य; विश्वास मध्यम; एक लम्बी छपी पंक्ति (०२.११.२)। पाठ-चिह्न (सम्भव): छपा ‘सवैर्’ = सर्वैः (र् छूटा); छपा ‘क्षणिस्य’ को ‘क्षीणस्य’ पढ़ा गया; "
          "छपा ‘सतृष्णो स’ में स से पहले ओ नियमित सन्धि नहीं, ‘सतृष्णः सः’ अभिप्रेत। इन पर प्रश्न नहीं। "
          "छपा ‘वायस्याशु’ = वा यस्य आशु; ‘चउरसो’ = च उरसः (स्वरों के बीच का अन्तर छपाई का अपना रूप)। "
          "पिप्लु, व्यंग, तिलकालक त्वचा के चिह्न (पहचान सम्भावित); आमाशय (सम्भवतः जठर), पक्वाशय (सम्भवतः बड़ी आँत); ‘पुष्प’ शब्दशः फूल। "
          "घुर्घुरक = कण्ठ की घुरघुर ध्वनि; समीक्षक के अनुसार सम्भवतः मृत्यु के समय की घरघराहट (सम्भावित)। ‘परासु’ = जिसके प्राण चले गए; पंक्ति इससे अधिक नहीं कहती। "
          "सन्धि जाँची: हृद्यैः + बहुभिः → हृद्यैर्बहुभिः (ऐ के बाद विसर्ग, घोष ब से पहले → र्); बहुभिः + अपि → बहुभिरपि; अपि + अन्न- → अप्यन्न- (इ + अ → य); "
          "बहुशः + च → बहुशश्च (च से पहले ः → श्); वा + आध्मान- → वाऽध्मान- (आ + आ → आ, ऽ छपाई की आदत)।"),
    "3": ("गद्य; विश्वास उच्च; एक छपी पंक्ति (०२.११.३); कोई पाठ-चिह्न नहीं। परिचय-सूत्र ‘भवति च अत्र’; इसके बाद कोई कर्ता नहीं छपा, इसलिए कुछ जोड़ा नहीं गया। "
          "डेटा के अनुसार यह सम्भवतः आगे की इकाइयों (छपी पंक्ति ४, कार्ड ४ से) का परिचय है। सन्धि जाँची: च + अत्र → चात्र (अ + अ → आ)।"),
    "4": ("श्लोक-इकाई; विश्वास उच्च; दो छपी पंक्तियाँ (०२.११.४ और ०२.११.५); कोई पाठ-चिह्न नहीं। ‘निहन्ति’ का कर्म पहली पंक्ति में नहीं; "
          "दूसरी पंक्ति का पहला शब्द प्रथमा (ज्वर का विशेषण), बाकी तीन द्वितीया (कर्म)। डेटा के अनुसार कर्म कार्ड ५ में आगे चलते हैं। "
          "अनल = अग्नि, सम्भवतः पाचन की अग्नि (सम्भावित)। दीर्घरात्रिक शब्दशः ‘लम्बी रातों वाला’। "
          "सन्धि जाँची: ज्वरः + निहन्ति → ज्वरो निहन्ति; गम्भीरः + दीर्घ- → गम्भीरो दीर्घ- (अः घोष व्यंजन से पहले → ओ); हत + अनल → हतानल (अ + अ → आ)।"),
    "5": ("श्लोक-इकाई; विश्वास मध्यम; दो छपी पंक्तियाँ (०२.११.६ और ०२.११.७)। पाठ-चिह्न (सम्भव): ‘अक्षामं’ (कृश नहीं) कार्ड ४ के ‘क्षीणम्’ के साथ अटपटा; "
          "‘क्षामं’ (कृश) अभिप्रेत हो सकता है, पर छपा शब्द मान्य है और वैसा ही अनुवाद हुआ। इस पर प्रश्न नहीं। "
          "सक्त = अटका हुआ, इसलिए सक्तवचन = अटकती वाणी। दूसरी पंक्ति में नया कर्ता (संशुष्ककासः); वह क्या करता है, यह नहीं कहा गया। "
          "सन्धि जाँची: यः + अपराह्णे → यो ऽपराह्णे (अः + अ → ओऽ); अपराह्णे + अपि → अपराह्णे ऽपि (ए + अ → एऽ)।"),
    "6": ("श्लोक-इकाई; विश्वास मध्यम; दो छपी पंक्तियाँ (०२.११.८ और ०२.११.९)। पाठ-चिह्न: छपा ‘कृष्णमिद्रधनुःप्रभं’ में ‘इद्र’ कोई शब्द नहीं, इन्द्र का अनुस्वार छूटा (अर्थ इन्द्रधनुष निश्चित)। "
          "‘समन्वितः’ (प्रथमा) कार्ड ५ की सूखी खाँसी से जुड़ता है या व्यक्ति से, यह खुला; ‘भृशम्’ को ‘रक्तम्’ के साथ (बहुत लाल) पढ़ा गया, अलग क्रियाविशेषण भी सम्भव। "
          "रक्तपित्त = सम्भवतः रक्तस्राव का रोग; विशेषण निकलने वाले रक्त के हैं, जिसका नाम नहीं छपा। "
          "व्याकरण जाँचा: श्लेष्मन् + कास → श्लेष्मकास (समास के पहले पद में अन्-अन्त शब्द का न् लुप्त)।"),
    "7": ("गद्य; विश्वास कम; दो छपी पंक्तियाँ (०२.११.१० और ०२.११.११); डेटा इसे गद्य मानता है। "
          "‘रक्तम्’ रंग (लाल) भी हो सकता है और संज्ञा (रक्त) भी; ‘दर्शयेत्’ का कर्ता नहीं छपा (डेटा: कार्ड ६ के रक्तपित्त का क्रम)। "
          "पाठ-चिह्न: छपा ‘सजतं’ कोई शब्द नहीं; ‘संजातम्’ या ‘सक्तम्’ निकटतम विकल्प, कोई नहीं अपनाया; शब्द अस्पष्ट है। "
          "प्रविसृत = फैलकर निकला हुआ। व्याकरण: हरिद्रा → हारिद्र (पहले स्वर की वृद्धि); दर्शयेत् = √दृश्, प्रेरणार्थक, विधिलिङ्।"),
    "8": ("श्लोक-इकाई; विश्वास कम; दो छपी पंक्तियाँ (०२.११.१२ और ०२.११.१३)। पहली पंक्ति का कर्ता नहीं छपा; डेटा इसे कार्ड ६-७ के स्राव का क्रम मानता है। "
          "पूति = सड़ा हुआ (दुर्गन्ध भी सम्भव)। पाठ-चिह्न (सम्भव): छपा ‘छर्द्दं’ अस्पष्ट; अगले समास के ‘छर्दि’ को दोहराता लगता है, इसलिए अर्थ नहीं दिया गया। "
          "छपा ‘र्द्द’ (दोहरा द) छपाई की आदत; शब्दों में ‘छर्दि’ लिखा गया। पाण्डु = रक्ताल्पता, पीलापन सहित (मानक)। "
          "सन्धि जाँची: वाससः + र- → वाससो र- (अः घोष व्यंजन से पहले → ओ); वेगवत् + च → वेगवच्च (च से पहले त् → च्); च + अति- → चाति- (अ + अ → आ); "
          "ज्वर + छर्दि → ज्वरच्छर्दि (ह्रस्व स्वर के बाद छ → च्छ)।"),
    "9": ("श्लोक-इकाई; विश्वास मध्यम; दो छपी पंक्तियाँ (०२.११.१४ और ०२.११.१५); कोई पाठ-चिह्न नहीं। अपूर्ण वाक्य: प्रथमा कर्ता, द्वितीया कर्म, क्रिया (निहन्ति) कार्ड ४ से चली आती है। "
          "छपा ‘अतीसार’ (दीर्घ ई) वैसा ही रखा गया। अन्तिम पद ‘असंतापिन्’ (ताप से रहित) शब्दशः पढ़ा गया; मारक लक्षणों की सूची में इसका अर्थ स्पष्ट नहीं, इसलिए उस पर प्रश्न नहीं। "
          "यक्ष्मन् = सम्भवतः क्षय रोग (सम्भावित)। आनाह = पेट का तनाव। "
          "सन्धि जाँची: तृष्णा + अतीसार → तृष्णातीसार (आ + अ → आ); छर्दि + असंतापिनम् → छर्द्यसंतापिनम् (इ + अ → य)।"),
    "10": ("गद्य; विश्वास कम; दो छपी पंक्तियाँ (०२.११.१६ और ०२.११.१७); डेटा इसे गद्य मानता है। "
           "चन्द्रिका = चाँदनी; यहाँ किसका नाम है, यह नहीं कहा गया (समीक्षक: सम्भवतः स्राव में चन्द्र जैसे चिह्न, अपुष्ट, अपनाया नहीं)। "
           "दूसरी पंक्ति क्षतिग्रस्त: ‘सास्र’ = स + अस्र (रक्त या आँसू); छपा समास ‘विट्पूयरुक्कासश्वासवत्य’ का अन्त नहीं बैठता, अस्पष्ट छोड़ा गया "
           "(दिखने वाले अंश: विट्, पूय, रुज्, कास, श्वास); ‘गुंषिणो’ कोई शब्द नहीं, ‘यक्ष्मिणः’ एक अपुष्ट सुझाव। इन पर प्रश्न नहीं। "
           "सन्धि जाँची: छर्दिः + वेगवती → छर्दिर्वेगवती (इ के बाद विसर्ग, घोष व से पहले → र्); शकृत् + गन्धि → शकृद्गन्धि (घोष ग से पहले त् → द्)।"),
    "11": ("श्लोक-इकाई; विश्वास मध्यम; दो छपी पंक्तियाँ (०२.११.१८ और ०२.११.१९); कोई पाठ-चिह्न नहीं। अपूर्ण वाक्य: क्रिया पीछे से चली आती है। "
           "छपा ‘तृष्णाऽन्य-’ में आ के बाद ऽ छपाई की आदत है (तृष्णा + अन्य-)। बहिर्जिह्व = जिसकी जीभ बाहर निकली हो। "
           "मदात्यय = सम्भवतः मद्य से उत्पन्न रोग (सम्भावित)। "
           "सन्धि जाँची: मदात्ययः + अति- → मदात्ययो ऽति- (अः + अ → ओऽ); बहिः + जिह्व- → बहिर्जिह्व- (घोष ज से पहले र्); शीत + आर्त → शीतार्त (अ + आ → आ)।"),
    "12": ("श्लोक-इकाई; विश्वास मध्यम; दो छपी पंक्तियाँ (०२.११.२० और ०२.११.२१)। पाठ-चिह्न: छपा ‘अर्शासि’ = अर्शांसि (नपुंसक बहुवचन, अनुस्वार छूटा); "
           "छपा ‘पार्श्वंग’ में पार्श्व + अङ्ग से दीर्घ आ (पार्श्वाङ्ग) होना चाहिए, अर्थ वही। दूसरा समास ‘हृदय, पार्श्व और अंग की पीड़ा’ एक समूह में भी पढ़ा जा सकता है; इस पर प्रश्न नहीं। "
           "आस्य = मुख (मुखड़ा भी)। "
           "सन्धि जाँची: पद् + नाभि → पन्नाभि (नासिक्य से पहले द् → न् विकल्प से; पद्नाभि भी शुद्ध); हृद् + पार्श्व → हृत्पार्श्व (अघोष प से पहले द् → त्)।"),
    "13": ("श्लोक-इकाई; विश्वास मध्यम; दो छपी पंक्तियाँ (०२.११.२२ और ०२.११.२३); कोई पाठ-चिह्न नहीं। पहली पंक्ति की तृतीया बहुवचन ‘तुल्यः’ से पूरी हो सकती हैं "
           "(तब ‘से’ के स्थान पर ‘जैसा’), डेटा इसे खुला रखता है। मेचक = गहरा नीला-काला (मोर-रंग भी); इसकी संज्ञा नहीं छपी। "
           "‘मज्ज’ समास में मज्जा/मज्जन् का रूप, यहाँ ‘मज्जा’। डेटा के अनुसार वाक्य कार्ड १४ (छपी पंक्ति २४) में आगे चलता है। "
           "सन्धि जाँची: अतीसारः + यकृत् → अतीसारो यकृत् (अः घोष व्यंजन से पहले → ओ); तुल्यः + तैल- → तुल्यस्तैल- (त से पहले ः → स्); वसा + आसवैः → वसासवैः (आ + आ → आ)।"),
}

# ================================================================ AIDS
AIDS = {
    "1": {
        "frame": "कब: अथ (अब) → क्यों: अतः (इसलिए) → क्या: विकृतव्याधिविज्ञानीयम् अध्यायम् → क्रिया: व्याख्यास्यामः (हम व्याख्या करेंगे)।",
        "chunks": "अथातो | विकृतव्याधिविज्ञानीयमध्यायं | व्याख्यास्यामः",
        "sandhi": ("अ + अ → आ: अथ + अतः → अथातः · अः घोष व्यंजन से पहले → ओ: अतः + वि- → अतो वि- · म् स्वर से जुड़ता है: "
                   "-विज्ञानीयम् + अध्यायम् → -विज्ञानीयमध्यायम् · व्यंजन से पहले म् → ं: अध्यायम् + व्याख्यास्यामः → अध्यायं व्याख्यास्यामः।"),
    },
    "2": {
        "diagram": {"groups": [
            {"label": "‘यस्य’ वाले लक्षण (छपे क्रम में)",
             "items": ["१ रोग सब हेतु, पूर्वरूप, रूप सहित अत्यधिक", "२ मुख पर पिप्लु, व्यंग, लेखा, तिलकालक (सम्भावित)",
                       "३ नख-दाँत पर पुष्प; पेट पर अनेक रंग की सिराएँ", "४ सूखते हुए: नेत्रोपदेह, पलक या नाक की सूजन, पलक का झड़ना",
                       "५ क्षीण: भूख या प्यास अन्न-पान से शान्त न हो", "६ झाग सहित रक्त; कुक्षि और छाती में शूल",
                       "७ श्लेष्मा नीला, पीला, लाल, बार-बार", "८ गर्दन का अवमर्द, जीभ सूखे, कण्ठ-मुख-गुदा का पाक",
                       "९ आमाशय से परिकर्तिका, अति प्यास, शकृद्भेद", "१० पक्वाशय से परिकर्तिका, अति प्यास, अति गुदग्रह",
                       "११ वायु चेतना नष्ट कर कण्ठ में घुरघुरक करे", "१२ क्षीण: प्यास बढ़े, हृदय-शूल, हिध्मा आदि"]},
            {"label": "सब का फल", "items": ["स परासुः: वह परासु है"]}]},
        "contrast": ("आमाशय (सम्भवतः जठर) से उठी परिकर्तिका: अति प्यास + शकृद्भेद (मल का टूटना) ⇄ पक्वाशय (सम्भवतः बड़ी आँत) से उठी "
                     "परिकर्तिका: अति प्यास + अत्यधिक गुदग्रह। दोनों इसी इकाई में।"),
        "sandhi": ("ऐ के बाद विसर्ग, घोष ब से पहले → र्: हृद्यैः + बहुभिः → हृद्यैर्बहुभिः · इ + अ → य: अपि + अन्न- → अप्यन्न- · "
                   "च से पहले ः → श्: बहुशः + च → बहुशश्च · आ + आ → आ: वा + आध्मान- → वाऽध्मान- (ऽ छपाई की आदत)।"),
    },
    "3": {
        "frame": "क्रिया: भवति (है) → और: च → कहाँ: अत्र (यहाँ, इस विषय में) → क्या है: छपा नहीं।",
        "chunks": "भवति | चात्र",
        "sandhi": "अ + अ → आ: च + अत्र → चात्र।",
    },
    "4": {
        "diagram": {"groups": [
            {"label": "ज्वर कैसा (प्रथमा)",
             "items": ["बलवान्: बलवान्", "गम्भीरः: गहरा", "दीर्घरात्रिकः: लम्बी रातों वाला", "सप्रलापभ्रमश्वासः: प्रलाप, भ्रम, श्वास सहित"]},
            {"label": "किसे मारता है (द्वितीया)",
             "items": ["क्षीणम्: क्षीण", "शूनम्: सूजा हुआ", "हतानलम्: जिसकी अनल नष्ट (सम्भवतः पाचन-अग्नि)"]}]},
        "chunks": "ज्वरो निहंति | बलवान्गंभीरो दीर्घरात्रिकः || सप्रलापभ्रमश्वासः | क्षीणं शूनं हतानलं",
        "sandhi": ("अः घोष व्यंजन से पहले → ओ: ज्वरः + निहन्ति → ज्वरो निहन्ति, गम्भीरः + दीर्घ- → गम्भीरो दीर्घ- · "
                   "अ + अ → आ: हत + अनल → हतानल।"),
    },
    "5": {
        "chunks": "अक्षामं सक्तवचनं | रक्ताक्षं हृदि शूलिनं || संशुष्ककासः | पूर्वाह्णेयोऽपराह्णेऽपि वा भवेत्",
        "seesaw": "पूर्वाह्णे (दोपहर से पहले) ⇄ अपराह्णे (दोपहर के बाद): दोनों इसी इकाई में।",
        "sandhi": "अः + अ → ओऽ: यः + अपराह्णे → यो ऽपराह्णे · ए + अ → एऽ: अपराह्णे + अपि → अपराह्णे ऽपि।",
    },
    "6": {
        "frame": "किसका: बलमांसविहीनस्य → किससे युक्त: श्लेष्मकास → फिर: रक्तपित्तम् → रंग: भृशं रक्तं, कृष्णम्, इन्द्रधनुष की आभा।",
        "chunks": "बलमांसविहीनस्य | श्लेष्मकाससमन्वितः || रक्तपित्तं भृशं रक्तं | कृष्णमिद्रधनुःप्रभं",
        "sandhi": ("अन्-अन्त शब्द समास के पहले पद में न् खोता है: श्लेष्मन् + कास → श्लेष्मकास · म् स्वर से जुड़ता है: "
                   "कृष्णम् + इद्र- → कृष्णमिद्र- (छपा ‘इद्र’ = इन्द्र)।"),
    },
    "7": {
        "chunks": "ताम्रहारिद्रहरितं रूपं | रक्तं दर्शयेत् || रोमकूपप्रविसृतं | कंठास्यहृदये सजतं",
        "letters": "हरिद्रा → हारिद्र: पहला अ आ बना (वृद्धि), अर्थ ‘हल्दी के रंग का’; पृथिवी → पार्थिव भी ऐसा ही।",
        "frame": "रंग: ताम्र, हारिद्र, हरित, रक्त → क्रिया: दर्शयेत् (दिखाए) → कहाँ से: रोमकूप → फिर: कण्ठ, मुख, हृदय (अन्तिम शब्द अस्पष्ट)।",
    },
    "8": {
        "diagram": {"groups": [
            {"label": "पंक्ति २ का समास (छपे क्रम में)",
             "items": ["१ पाण्डु: रक्ताल्पता (मानक)", "२ ज्वर: बुखार", "३ छर्दि: उल्टी", "४ कास: खाँसी", "५ शोफ: सूजन",
                       "६ अतिसारिन्: अतिसार वाला"]}]},
        "chunks": "वाससो रंजनं पूति | वेगवच्चातिभूरि च || छर्द्दं | पांडुज्वरच्छर्द्दिकासशोफातिसारिणं",
        "sandhi": ("अः घोष व्यंजन से पहले → ओ: वाससः + रञ्जनम् → वाससो रञ्जनम् · च से पहले त् → च्: वेगवत् + च → वेगवच्च · "
                   "अ + अ → आ: च + अतिभूरि → चातिभूरि · ह्रस्व स्वर के बाद छ → च्छ: ज्वर + छर्दि → ज्वरच्छर्दि।"),
    },
    "9": {
        "diagram": {"groups": [
            {"label": "पंक्ति १: कासश्वासौ",
             "items": ["ज्वर", "छर्दि", "तृष्णा", "अतीसार", "शोफ"]},
            {"label": "पंक्ति २: यक्ष्मा",
             "items": ["पार्श्व में पीड़ा", "आनाह: पेट का तनाव", "रक्त की उल्टी", "असंतापी (अर्थ अस्पष्ट)"]}]},
        "chunks": "कासश्वासौ | ज्वरच्छर्द्दितृष्णातीसारशोफिनं || यक्ष्मा | पार्श्वरुजानाहरक्तच्छर्द्यसंतापिनं",
        "sandhi": "आ + अ → आ: तृष्णा + अतीसार → तृष्णातीसार · इ + अ → य: छर्दि + असंतापिनम् → छर्द्यसंतापिनम्।",
    },
    "10": {
        "frame": "कौन: छर्दिः → कैसी: वेगवती → गन्ध: मूत्र और शकृत् की → और: सचन्द्रिका (अर्थ अस्पष्ट) → पंक्ति २: क्षतिग्रस्त।",
        "chunks": "छर्द्दिर्वेगवती | मूत्रशकृद्गंधिः सचंद्रिका || सास्र | विट्पूयरुक्कासश्वासवत्य गुंषिणो",
        "sandhi": ("इ के बाद विसर्ग, घोष व से पहले → र्: छर्दिः + वेगवती → छर्दिर्वेगवती · घोष ग से पहले त् → द्: "
                   "शकृत् + गन्धि → शकृद्गन्धि।"),
    },
    "11": {
        "contrast": ("तृष्णा: दूसरे रोगों से क्षीण, जीभ बाहर, अचेत ⇄ मदात्यय (सम्भवतः मद्य-जनित रोग): अति शीत से पीड़ित, क्षीण, "
                     "तेल-सी चमक वाला मुख। दोनों इसी इकाई में।"),
        "chunks": "तृष्णाऽन्यरोगक्षपितं | बहिर्जिह्वं विचेतनं || मदात्ययोऽतिशीतार्तं | क्षीणं तैलप्रभाननं",
        "sandhi": ("अः + अ → ओऽ: मदात्ययः + अति- → मदात्ययो ऽति- · इ के बाद विसर्ग, घोष ज से पहले → र्: बहिः + जिह्व- → बहिर्जिह्व- · "
                   "अ + आ → आ: शीत + आर्त → शीतार्त।"),
    },
    "12": {
        "diagram": {"groups": [
            {"label": "अर्श: सूजन के स्थान (छपे क्रम में)",
             "items": ["१ पाणि: हाथ", "२ पद्: पैर", "३ नाभि", "४ गुद: गुदा", "५ मुष्क: वृषण", "६ आस्य: मुख"]},
            {"label": "पीड़ा और कष्ट",
             "items": ["हृदय, पार्श्व, अंग की पीड़ा", "छर्दि", "पायु का पाक", "ज्वर"]}]},
        "chunks": "अर्शासि | पाणिपन्नाभिगुदमुष्कास्यशोफिनं || हृत्पार्श्वंगरुजाछर्द्दिपायुपाकज्वरातुरं",
        "sandhi": ("नासिक्य न से पहले द् विकल्प से न्: पद् + नाभि → पन्नाभि (पद्नाभि भी शुद्ध) · अघोष प से पहले द् → त्: "
                   "हृद् + पार्श्व → हृत्पार्श्व।"),
    },
    "13": {
        "diagram": {"groups": [
            {"label": "पंक्ति १ (-ऐः)",
             "items": ["यकृत्पिण्ड: यकृत् के पिण्ड", "मांसधावन: मांस का धोवन", "मेचक: गहरा नीला-काला"]},
            {"label": "पंक्ति २: तुल्यः (समान)",
             "items": ["तैल", "घृत", "क्षीर", "दधि", "मज्ज (मज्जा)", "वसा", "आसव"]}]},
        "chunks": "अतीसारो | यकृत्पिंडमांसधावनमेचकैः || तुल्यस्तैलघृतक्षीरदधिमज्जवसासवैः",
        "sandhi": ("अः घोष व्यंजन से पहले → ओ: अतीसारः + यकृत् → अतीसारो यकृत् · त से पहले ः → स्: तुल्यः + तैल- → तुल्यस्तैल- · "
                   "आ + आ → आ: वसा + आसवैः → वसासवैः।"),
    },
}

# ================================================================ IMAGE_SPECS
IMAGE_SPECS = {
    ("2", "diagram"): {
        "file": "sh11-parasu-2.svg",
        "alt": ("Numbered table of card 2: twelve alternative signs, each opened by yasya, in printed order (disease with all "
                "causes and signs to excess; face marks; flowers on nails and teeth and veins on the belly; eye coating and "
                "swellings; unappeased hunger or thirst; frothy blood; coloured phlegm; neck, tongue, throat signs; parikartikā "
                "of āmāśaya; of pakvāśaya; gurgling in the throat; thirst and heart pain), all closing in sa parāsuḥ."),
        "type": "table",
        "title": "कार्ड २: ‘यस्य’ लक्षण → स परासुः",
        "heads": ["क्रम", "लक्षण"],
        "rows": [["१", "रोग सब हेतु, पूर्वरूप, रूप सहित अत्यधिक"], ["२", "मुख पर पिप्लु, व्यंग, लेखा, तिलकालक"],
                 ["३", "नख-दाँत पर पुष्प; पेट पर अनेक रंग की सिराएँ"], ["४", "नेत्रोपदेह; पलक या नाक की सूजन"],
                 ["५", "भूख-प्यास अन्न-पान से शान्त न हो"], ["६", "झाग सहित रक्त; कुक्षि, छाती में शूल"],
                 ["७", "श्लेष्मा नीला, पीला, लाल"], ["८", "गर्दन का अवमर्द, जीभ सूखे, पाक"],
                 ["९", "आमाशय से परिकर्तिका"], ["१०", "पक्वाशय से परिकर्तिका"],
                 ["११", "कण्ठ में वायु का घुरघुरक"], ["१२", "प्यास बढ़े, हृदय में शूल"], ["फल", "स परासुः"]],
    },
    ("2", "contrast"): {
        "file": "sh11-ashaya-2.svg",
        "alt": ("Split of card 2: parikartikā (cutting pain) from the āmāśaya (probably the stomach) with excessive thirst and "
                "breaking of the stool, against parikartikā from the pakvāśaya (probably the large intestine) with excessive "
                "thirst and excessive grasp of the anus."),
        "type": "split",
        "title": "कार्ड २: दो आशय, दो परिकर्तिका",
        "cols": [["आमाशय से", ["सम्भवतः जठर", "परिकर्तिका", "अति प्यास", "शकृद्भेद: मल का टूटना"]],
                 ["पक्वाशय से", ["सम्भवतः बड़ी आँत", "परिकर्तिका", "अति प्यास", "अत्यधिक गुदग्रह"]]],
    },
    ("4", "diagram"): {
        "file": "sh11-jvara-4.svg",
        "alt": ("Split of card 4: the fever (nominative) is strong, deep, long-lasting and with delirium, giddiness and "
                "breathlessness; the ones it kills (accusative) are wasted, swollen, and whose fire (probably digestive) is destroyed."),
        "type": "split",
        "title": "कार्ड ४: ज्वरो निहन्ति",
        "cols": [["ज्वर कैसा", ["बलवान्", "गम्भीर: गहरा", "दीर्घरात्रिक: लम्बी रातों वाला", "प्रलाप, भ्रम, श्वास सहित"]],
                 ["किसे मारता है", ["क्षीण", "शून: सूजा हुआ", "हतानल: अनल नष्ट (सम्भवतः पाचन-अग्नि)"]]],
    },
    ("8", "diagram"): {
        "file": "sh11-pandu-8.svg",
        "alt": ("Numbered table of the long compound in line 2 of card 8, in printed order: pāṇḍu (anaemia with pallor), "
                "fever, vomiting, cough, swelling, having diarrhoea."),
        "type": "table",
        "title": "कार्ड ८: पंक्ति २ का समास",
        "heads": ["क्रम", "छपा पद: अर्थ"],
        "rows": [["१", "पाण्डु: रक्ताल्पता (मानक)"], ["२", "ज्वर: बुखार"], ["३", "छर्दि: उल्टी"], ["४", "कास: खाँसी"],
                 ["५", "शोफ: सूजन"], ["६", "अतिसारिन्: अतिसार वाला"]],
    },
    ("9", "diagram"): {
        "file": "sh11-kasa-yakshma-9.svg",
        "alt": ("Split of card 9: line 1, cough and breathlessness, with fever, vomiting, thirst, diarrhoea and swelling; "
                "line 2, yakṣman (probably tuberculosis), with pain in the side, distension, vomiting of blood, and "
                "asaṃtāpin (sense unclear)."),
        "type": "split",
        "title": "कार्ड ९: दो पंक्तियाँ, दो रोग",
        "cols": [["कासश्वासौ", ["ज्वर", "छर्दि", "तृष्णा", "अतीसार", "शोफ"]],
                 ["यक्ष्मा", ["सम्भवतः क्षय रोग", "पार्श्व में पीड़ा", "आनाह: पेट का तनाव", "रक्त की उल्टी", "असंतापी: अर्थ अस्पष्ट"]]],
    },
    ("11", "contrast"): {
        "file": "sh11-trishna-madatyaya-11.svg",
        "alt": ("Split of card 11: thirst, with the one worn down by other ailments, tongue outside, unconscious; madātyaya "
                "(probably an alcohol-related disorder), with the one afflicted by great cold, wasted, face with oily lustre."),
        "type": "split",
        "title": "कार्ड ११: तृष्णा और मदात्यय",
        "cols": [["तृष्णा", ["दूसरे रोगों से क्षीण", "जीभ बाहर", "अचेत"]],
                 ["मदात्यय", ["सम्भवतः मद्य-जनित रोग", "अति शीत से पीड़ित", "क्षीण", "तेल-सी चमक वाला मुख"]]],
    },
    ("12", "diagram"): {
        "file": "sh11-arsha-12.svg",
        "alt": ("Numbered table of card 12: with arśas (piles), swelling of hand, foot, navel, anus, testicle and mouth in "
                "printed order; then pain of heart, side and limbs, vomiting, inflammation of the anus, and fever."),
        "type": "table",
        "title": "कार्ड १२: अर्श के साथ",
        "heads": ["क्रम", "छपा पद: अर्थ"],
        "rows": [["१", "पाणि: हाथ"], ["२", "पद्: पैर"], ["३", "नाभि"], ["४", "गुद: गुदा"], ["५", "मुष्क: वृषण"],
                 ["६", "आस्य: मुख"], ["फिर", "हृदय, पार्श्व, अंग की पीड़ा"], ["फिर", "छर्दि, पायु का पाक, ज्वर"]],
    },
    ("13", "diagram"): {
        "file": "sh11-atisara-13.svg",
        "alt": ("Split of card 13: line 1 instrumentals (liver-lumps, meat-washings, dark ones); line 2, similar to oil, ghee, "
                "milk, curd, marrow, fat and āsava."),
        "type": "split",
        "title": "कार्ड १३: अतीसार",
        "cols": [["पंक्ति १ (-ऐः)", ["यकृत्पिण्ड", "मांसधावन", "मेचक: गहरा नीला-काला"]],
                 ["तुल्यः (समान)", ["तैल", "घृत", "क्षीर", "दधि", "मज्ज (मज्जा)", "वसा", "आसव"]]],
    },
}
