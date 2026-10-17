from helpers import mcq, match, order, fill, multi, accepts

AUTHORED = {}

# ---------------------------------------------------------------- unit 1
AUTHORED["1"] = {
    "title": "अथातो रोगानुत्पादनीयम्",
    "question": "What chapter does this opening formula announce?",
    "rule": ("The formula 'athāto … vyākhyāsyāmaḥ' says: now, therefore, we shall "
             "explain the chapter named Rogānutpādanīya (the non-arising of disease)."),
    "limits": ("The line gives only the chapter's name and the promise to explain it. "
               "It names no disease, urge or remedy; those begin in unit 2."),
    "explain_hi": ("हर अध्याय की तरह यह पंक्ति सूत्र-वाक्य है: ‘अथ’ (अब) और ‘अतः’ (इसलिए), "
                   "फिर अध्याय का नाम ‘रोगानुत्पादनीय’, और अंत में ‘व्याख्यास्यामः’ (हम व्याख्या करेंगे)। "
                   "नाम का भाव है रोगों का उत्पन्न न होना। ‘रोग’ और ‘अनुत्पादनीय’ मिलकर "
                   "‘रोगानुत्पादनीय’ बने हैं (अ + अ → आ)। इस पंक्ति में अभी कोई रोग या उपाय नहीं आया।"),
    "hook": "अब, इसलिए: रोगों के न उपजने वाले अध्याय की व्याख्या करेंगे।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What does the verb 'व्याख्यास्यामः' say?",
            ("We shall explain", "The ending -स्यामः is the first person plural of the future: we shall."),
            [("We have explained", "That would be a past form; this one is future."),
             ("He explains", "The ending is first person plural, 'we', not 'he'."),
             ("Let no one explain", "Nothing here forbids; it is a promise.")],
            "व्याख्यास्यामः is first person plural future: 'we shall explain'.",
            "व्याख्यास्यामः = we shall explain."),
        order(1, "Put the words of the formula in the verse's order.",
              ["अथ", "अतः", "रोगानुत्पादनीयम्", "अध्यायम्", "व्याख्यास्यामः"],
              "The line runs: now, therefore, the Rogānutpādanīya chapter, we shall explain.",
              "अथातो रोगानुत्पादनीयमध्यायं व्याख्यास्यामः."),
        fill(2, "The chapter announced is called an ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("अध्यायम्", None, "अध्याय"),
             "अध्यायम् means 'chapter'; it ends in -म् because it is what 'we shall explain'.",
             "अध्याय is the word for a chapter; in the formula it stands in the accusative (अध्यायम्) as the object of the verb.",
             "अध्याय = chapter.", role="extend"),
        mcq("discriminate", 3, "Which is the right split of the first word, अथातो?",
            ("अथ + अतः", "अ + अ gives आ (अथातः); the visarga then becomes ओ before the voiced र of the next word."),
            [("अथा + तो", "तो is not a word here; the pieces are अथ and अतः."),
             ("अथ + आतः", "आतः would not give अथातो; the second part starts with a short अ."),
             ("अथः + अतः", "अथ ends in -अ and takes no visarga.")],
            "अथ (now) + अतः (therefore) = अथातः, and before the voiced र the visarga becomes ओ: अथातो.",
            "अ + अ → आ; अः before a voiced consonant → ओ."),
        match(4, "Match each word of the formula to its meaning.",
              [["अथ", "now"], ["अतः", "therefore"], ["अध्यायम्", "chapter"],
               ["व्याख्यास्यामः", "we shall explain"]],
              "These four words carry the whole announcement.",
              "अथ = now; अतः = therefore; अध्याय = chapter; व्याख्यास्यामः = we shall explain.",
              role="apply"),
        mcq("transfer", 5, "Which form means we shall go?",
            ("गमिष्यामः", "-ष्यामः is the 'we shall' ending, like -स्यामः in व्याख्यास्यामः."),
            [("गच्छामः", "This is 'we go', the present."),
             ("अगच्छाम", "This is 'we went', the past."),
             ("गच्छेम", "This is 'we should go', the wish form.")],
            "The future 'we shall' ends in -ष्यामः or -स्यामः.",
            "-स्यामः/-ष्यामः = we shall.",
            teaches="The first person plural future ends in -स्यामः or -ष्यामः (व्याख्यास्यामः, गमिष्यामः): 'we shall …'."),
    ],
}

# ---------------------------------------------------------------- unit 2
AUTHORED["2"] = {
    "title": "वेगान्न धारयेत्",
    "question": "Which urges does the verse say one should not hold back?",
    "rule": ("One should not hold back (न धारयेत्) the urges (वेगान्) of fourteen things: wind, "
             "stool, urine, sneeze, thirst, hunger; sleep, cough, exertion-breath, yawning, "
             "tears, vomiting, semen."),
    "limits": ("The verse only lists the urges and forbids holding them back. It gives no "
               "reason here. 'श्रम' and 'श्वास' are taken as two members; they may also be "
               "read as 'breathing from exertion'."),
    "explain_hi": ("अध्याय का पहला नियम यही है: वेगों को न रोके। पहली पंक्ति में छह वेग हैं: "
                   "वात (अधोवायु), विट् (मल), मूत्र, क्षव (छींक), तृट् (प्यास) और क्षुधा (भूख)। "
                   "दूसरी पंक्ति में आठ और: निद्रा, कास (खाँसी), श्रम और श्वास, जृंभा (जम्भाई), "
                   "अश्रु (आँसू), छर्दि (वमन) और रेतस् (वीर्य)। सारा समास षष्ठी बहुवचन में है और "
                   "‘वेगान्’ पर टिका है; क्रिया ‘धारयेत्’ है, ‘न’ के साथ निषेध बनाती हुई।"),
    "hook": "चौदह वेग गिन लो, किसी को भी रोको मत।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "Which pair is named in the FIRST line of the verse?",
            ("Sneeze and thirst", "क्षव and तृट् both stand in the first line."),
            [("Yawning and tears", "जृंभा and अश्रु are in the second line."),
             ("Sleep and cough", "निद्रा and कास open the second line."),
             ("Vomiting and semen", "छर्दि and रेतस् close the second line.")],
            "The first line lists wind, stool, urine, sneeze, thirst, hunger.",
            "First line: वात, विट्, मूत्र, क्षव, तृट्, क्षुधा."),
        match(1, "Match each urge to its meaning.",
              [["क्षव", "sneeze"], ["तृट्", "thirst"], ["क्षुधा", "hunger"],
               ["जृंभा", "yawning"], ["अश्रु", "tears"]],
              "Each word names an urge that the verse says is not to be held back.",
              "क्षव = sneeze; तृट् = thirst; क्षुधा = hunger; जृंभा = yawning; अश्रु = tears."),
        fill(2, "The verb meaning 'one should hold back' is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("धारयेत्", None, "धारयेद्"),
             "धारयेत् is the 'should' form of the verb धृ in its causative: one should hold back.",
             "धारयेत् ('one should hold back') with न makes a prohibition: न धारयेत् = one should not hold back.",
             "न धारयेत् = one should not hold back.", role="extend"),
        mcq("discriminate", 3, "Which is the right split of धारयेद्वात-?",
            ("धारयेत् + वात", "A final त् becomes द् before a voiced sound, here व."),
            [("धारयेद + वात", "The verb form ends in -त्; there is no word धारयेद."),
             ("धारयेः + वात", "A visarga would not turn into द्."),
             ("धारयेते + वात", "Nothing here gives द् from -ते.")],
            "धारयेत् (one should hold back) + वात (wind): त् → द् before the voiced व.",
            "Final त् → द् before a voiced sound."),
        order(4, "Put the last six urges of the second line in the verse's order.",
              ["श्रम", "श्वास", "जृंभा", "अश्रु", "छर्दि", "रेतस्"],
              "The second line ends: exertion, breath, yawning, tears, vomiting, semen.",
              "श्रम · श्वास · जृंभा · अश्रु · छर्दि · रेतस्.", role="apply"),
        mcq("transfer", 5, "Which invented sentence means: one should not hold back a yawn?",
            ("जृंभां न धारयेत्", "Object in the accusative + न + धारयेत्, as in the verse."),
            [("जृंभां धारयेत्", "Without न this says one should hold it back."),
             ("जृंभा न धारयेत्", "The object is not in the accusative (-ाम्) as the verse has it."),
             ("जृंभां न धारयति", "This says 'he does not hold back', a plain statement, not 'one should not'.")],
            "The pattern is: urge (accusative) + न + धारयेत्.",
            "वेगान् न धारयेत् = one should not hold back the urges.",
            teaches="The verse's pattern for a prohibition is: the thing in the accusative + न + धारयेत् ('one should not hold back'); drop न and the sense reverses."),
    ],
}

# ---------------------------------------------------------------- unit 3
AUTHORED["3"] = {
    "title": "अधोवातस्य रोधेन",
    "question": "What does the unit say arises from suppressing the downward wind?",
    "rule": ("By suppression (रोधेन) of the downward wind come gulma, udāvarta, pain, fatigue; "
             "retention of wind, urine and stool; damage of sight and fire; heart ailments."),
    "limits": ("The verb 'arise' is understood. 'वध' (damage) is taken for both sight and "
               "agni; संग may reach only the three listed. gulma and udāvarta are names; "
               "the unit does not explain them."),
    "explain_hi": ("पहला वेग वात (अधोवायु) है और यह इकाई बताती है कि उसे रोकने से क्या होता है। "
                   "‘रोधेन’ (रोकने से) ही कारण है। पहली पंक्ति में चार: गुल्म, उदावर्त, रुक् (पीड़ा) और क्लम "
                   "(थकान)। दूसरी पंक्ति में: वात-मूत्र-मल का संग (रुकना), दृष्टि और अग्नि की हानि, "
                   "और हृद्गद (हृदय के रोग)। गुल्म और उदावर्त केवल नाम हैं; श्लोक उनकी व्याख्या नहीं करता।"),
    "hook": "अधोवात रोका, तो गुल्म-उदावर्त से हृदय तक रोग।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "From suppressing what does the unit say gulma and udāvarta arise?",
            ("The downward wind", "अधोवातस्य रोधेन: by suppression of the downward wind."),
            [("Stool", "Stool is not the cause named in these lines."),
             ("A sneeze", "A sneeze is not mentioned here."),
             ("Thirst", "Thirst is not mentioned here.")],
            "The first words are अधोवातस्य रोधेन, 'by suppression of the downward wind'.",
            "अधोवातस्य रोधेन = by suppression of the downward wind."),
        order(1, "Put the four conditions of the first line in the verse's order.",
              ["गुल्म", "उदावर्त", "रुक्", "क्लम"],
              "Line 1 runs: gulma, udāvarta, pain, fatigue.",
              "गुल्म · उदावर्त · रुक् · क्लम."),
        match(2, "Match each word to its meaning.",
              [["अधोवात", "downward wind"], ["रोध", "suppression"], ["रुक्", "pain"],
               ["क्लम", "fatigue"], ["हृद्गद", "heart ailment"]],
              "Plain words of the unit: the cause, and some of its results.",
              "अधोवात = downward wind; रोध = suppression; रुक् = pain; क्लम = fatigue; हृद्गद = heart ailment.",
              role="extend",
              teaches="A list of results can be one compound joined by 'and' (गुल्मोदावर्तरुक्क्लमाः): the last member carries the plural ending shared by all."),
        mcq("discriminate", 3, "Which is the right split of अधोवातस्य?",
            ("अधः + वातस्य", "A visarga after अ becomes ओ before a voiced sound (व)."),
            [("अध + वातस्य", "Then the join would stay अधवातस्य, with no ओ."),
             ("अधा + वातस्य", "आ + व gives अधावातस्य, not अधोवातस्य."),
             ("अधोः + वातस्य", "There is no word अधोः here; the ओ comes from the visarga.")],
            "अधः (downward) + वातस्य (of wind): अः → ओ before the voiced व.",
            "अः before a voiced consonant → ओ."),
        order(4, "Put the three parts of the second line in the verse's order.",
              ["वातमूत्रशकृत्संग", "दृष्ट्यग्निवध", "हृद्गद"],
              "The line runs: retention of wind, urine and stool; damage to sight and agni; heart ailments.",
              "वातमूत्रशकृत्संग · दृष्ट्यग्निवध · हृद्गद.", role="apply"),
        mcq("transfer", 5, "Which word means by effort, as रोधेन means by suppression?",
            ("यत्नेन", "-एन is the 'by, through' ending on a word like रोध."),
            [("यत्नस्य", "-स्य means 'of effort'."),
             ("यत्नात्", "-आत् means 'from effort'."),
             ("यत्ने", "-ए means 'in effort'.")],
            "रोधेन is रोध + the 'by' ending -एन; यत्न works the same way.",
            "-एन = by, through.",
            teaches="A word like रोध takes -एन for 'by, through' (रोधेन = by suppression); likewise यत्नेन = by effort."),
    ],
}

# ---------------------------------------------------------------- unit 4
AUTHORED["4"] = {
    "title": "स्नेहस्वेदविधिस्तत्र",
    "question": "What does the unit say is recommended here?",
    "rule": ("In that case the method of oleation and sweating, wicks, foods, drinks and "
             "enemas are recommended, as what sets the wind moving in its proper course."),
    "limits": ("'तत्र' (in that case) follows the previous unit. The verse names the means "
               "only: no dose or manner. वातानुलोमनम् may qualify the whole list or be one more "
               "item; the card takes it as qualifying the list."),
    "explain_hi": ("पिछली इकाई के रोगों के बाद ‘तत्र’ (उस दशा में) यह इकाई उपाय गिनाती है। "
                   "स्नेहन-स्वेदन की विधि, बत्तियाँ, भोजन, पेय और बस्तियाँ: यही पाँच नाम हैं। "
                   "‘शस्तम्’ (हितकर कहा गया) एकवचन है पर पूरी सूची के लिए है। अंत में "
                   "‘वातानुलोमनम्’ बताता है कि ये वायु को ठीक मार्ग पर चलाने वाले हैं। "
                   "श्लोक केवल नाम देता है, मात्रा या ढंग नहीं।"),
    "hook": "स्नेह-स्वेद, बत्ती, भोजन, पान, बस्ति: वात को सीधे मार्ग पर।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "With which pair does the list of means open?",
            ("Oleation and sweating", "स्नेहस्वेदविधिः comes first."),
            [("Enemas and wicks", "These come later in the list."),
             ("Foods and drinks", "These stand in the middle."),
             ("Fasting and rest", "Neither is named in this unit.")],
            "The list opens with स्नेहस्वेदविधिः, the method of oleation and sweating.",
            "First: स्नेहस्वेदविधि."),
        order(1, "Put the five means in the order of the verse.",
              ["स्नेहस्वेदविधि", "वर्त्तयः", "भोजनानि", "पानानि", "बस्तयः"],
              "The unit runs: oleation-sweating method, wicks, foods, drinks, enemas.",
              "स्नेहस्वेदविधि · वर्त्तयः · भोजनानि · पानानि · बस्तयः."),
        match(2, "Match each word to its meaning.",
              [["वर्त्तयः", "wicks"], ["भोजनानि", "foods"], ["पानानि", "drinks"],
               ["बस्तयः", "enemas"], ["शस्तम्", "recommended"]],
              "Names of the means, plus the word that recommends them.",
              "वर्त्ति = wick; भोजन = food; पान = drink; बस्ति = enema; शस्तम् = recommended.",
              role="extend",
              teaches="Several different things may share one neuter singular 'recommended' (शस्तम्) when the list is taken as a whole."),
        mcq("discriminate", 3, "Which is the right split of बस्तयश्चैव?",
            ("बस्तयः + च + एव", "Visarga + च → श्च; च + एव → चैव."),
            [("बस्तयः + चै + व", "चै + व is not a word split; the pieces are च and एव."),
             ("बस्तय + श्चै + व", "श्चै is not a word."),
             ("बस्तयः + श्च + एव", "श्च is only the joined form, not a word on its own.")],
            "बस्तयः (enemas) + च (and) + एव (indeed).",
            "अः + च → श्च; अ + ए → ऐ."),
        multi("apply", 4, "Which of these does the unit name among the recommended means?",
              [("foods (भोजन)", "Right: named."),
               ("drinks (पान)", "Right: named."),
               ("enemas (बस्ति)", "Right: named."),
               ("induced vomiting", "Not named in this unit."),
               ("nasal drops", "Not named in this unit.")],
              [0, 1, 2],
              "Foods, drinks and enemas are in the list; induced vomiting and nasal drops are not named here.",
              "Named: स्नेहस्वेदविधि, वर्ति, भोजन, पान, बस्ति."),
        mcq("transfer", 5, "Which is the joined form of वायुः + तत्र?",
            ("वायुस्तत्र", "A visarga before त becomes स् (as विधिः + तत्र = विधिस्तत्र)."),
            [("वायुतत्र", "The visarga does not simply vanish before त."),
             ("वायुर्तत्र", "र् comes before voiced sounds, not before त."),
             ("वायुशतत्र", "श comes before च, not before त.")],
            "विधिः + तत्र becomes विधिस्तत्र; वायुः + तत्र becomes वायुस्तत्र.",
            "Visarga + त → स्त.",
            teaches="A visarga before त becomes स् (स्नेहस्वेदविधिः + तत्र = स्नेहस्वेदविधिस्तत्र)."),
    ],
}

# ---------------------------------------------------------------- unit 5
AUTHORED["5"] = {
    "title": "शकृतः पिंडिकोद्वेष्ट",
    "question": "What does the unit list for suppressing stool?",
    "rule": ("From (suppressing) stool: calf cramps, nasal catarrh, headache; upward wind, "
             "cutting pain, obstruction of the heart."),
    "limits": ("The cause word (suppression) is understood from the genitive शकृतः. "
               "'ऊर्ध्वं वायुः' may mean 'wind moving upward' or 'upward wind as a condition'; "
               "no question rests on that."),
    "explain_hi": ("अब दूसरा वेग: शकृत् (मल)। ‘शकृतः’ षष्ठी में है और ‘रोकने से’ का भाव अध्याहार है। "
                   "पहली पंक्ति में तीन: पिंडिकाओं की ऐंठन, प्रतिश्याय (नाक का जुकाम) और सिर की पीड़ा। "
                   "दूसरी पंक्ति में: ऊपर की ओर वायु, परिकर्त (काटने जैसी पीड़ा) और हृदय की रुकावट। "
                   "संधि: पिंडिका + उद्वेष्ट → पिंडिकोद्वेष्ट; हृदयस्य + उपरोधनम् → हृदयस्योपरोधनम्।"),
    "hook": "मल रुका: पिंडली, जुकाम, सिरदर्द; वायु ऊपर, हृदय में रुकावट।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "Which condition does the first line name for stool suppression?",
            ("Cramps of the calves", "पिंडिकोद्वेष्ट is the twisting of the calves."),
            [("Gulma", "Gulma belongs to the downward-wind unit, not this one."),
             ("Tremor", "Tremor is not in this unit."),
             ("Stone (अश्मरी)", "Not in this unit.")],
            "Line 1 names calf cramps, nasal catarrh and head pain.",
            "Line 1: पिंडिकोद्वेष्ट, प्रतिश्याय, शिरोरुज्."),
        match(1, "Match each word to its meaning.",
              [["शकृत्", "stool"], ["प्रतिश्याय", "nasal catarrh"], ["शिरोरुज्", "head pain"],
               ["परिकर्त", "cutting pain"], ["हृदय", "heart"]],
              "Plain words of the unit.",
              "शकृत् = stool; प्रतिश्याय = nasal catarrh; शिरोरुज् = head pain; परिकर्त = cutting pain; हृदय = heart."),
        order(2, "Put the six conditions in the order of the verse.",
              ["पिंडिकोद्वेष्ट", "प्रतिश्याय", "शिरोरुज्", "ऊर्ध्वं वायुः", "परिकर्त", "हृदयोपरोधन"],
              "Line 1 gives three, line 2 gives three: calf cramps, catarrh, head pain; upward wind, cutting pain, heart obstruction.",
              "पिंडिकोद्वेष्ट · प्रतिश्याय · शिरोरुज् · ऊर्ध्वं वायुः · परिकर्त · हृदयोपरोधन.",
              role="extend",
              teaches="The unit's genitive (शकृतः) leans on an understood 'suppression'; the six results come as two lines of three."),
        mcq("discriminate", 3, "Which is the right split of हृदयस्योपरोधनम्?",
            ("हृदयस्य + उपरोधनम्", "अ + उ gives ओ."),
            [("हृदयस्य + ओपरोधनम्", "The ओ is made by the join; there is no word ओपरोधनम्."),
             ("हृदयः + उपरोधनम्", "The first word is the genitive हृदयस्य."),
             ("हृदयस्यो + परोधनम्", "परोधनम् is not the word; it is उपरोधनम्.")],
            "हृदयस्य (of the heart) + उपरोधनम् (obstruction): अ + उ → ओ.",
            "अ + उ → ओ."),
        multi("apply", 4, "Which of these does the unit give for stool suppression?",
              [("catarrh of the nose", "Right: प्रतिश्याय."),
               ("head pain", "Right: शिरोरुज्."),
               ("cutting pain", "Right: परिकर्त."),
               ("gulma", "Not in this unit."),
               ("stone (अश्मरी)", "Not in this unit.")],
              [0, 1, 2],
              "Catarrh, head pain and cutting pain are all in the unit; gulma and stone are not.",
              "Named: पिंडिकोद्वेष्ट, प्रतिश्याय, शिरोरुज्, परिकर्त, हृदयोपरोधन."),
        mcq("transfer", 5, "Which is the joined form of गंगा + उदक?",
            ("गंगोदक", "आ + उ → ओ, as in पिंडिका + उद्वेष्ट = पिंडिकोद्वेष्ट."),
            [("गंगौदक", "औ comes from अ/आ + ओ or औ, not from उ."),
             ("गंगाउदक", "A vowel meeting a vowel is joined in careful Sanskrit."),
             ("गंगुदक", "The long आ does not simply drop with उ.")],
            "पिंडिका + उद्वेष्ट gives पिंडिकोद्वेष्ट; गंगा + उदक gives गंगोदक.",
            "अ/आ + उ → ओ.",
            teaches="A word ending in अ or आ followed by उ joins as ओ (पिंडिका + उद्वेष्ट = पिंडिकोद्वेष्ट; गंगा + उदक = गंगोदक)."),
    ],
}

# ---------------------------------------------------------------- unit 6
AUTHORED["6"] = {
    "title": "मुखेन विट्प्रवृत्तिः",
    "question": "What does this unit record besides the earlier ailments?",
    "rule": ("Passing of stool through the mouth, and the ailments stated before, are "
             "recorded; then breaking pain of the limbs, stone, and pains in the bladder, "
             "penis and groin."),
    "limits": ("The edition's pairing is kept: line 1 still closes the stool topic, and line 2 "
               "begins a list that goes on in unit 7, so no cause is stated inside this unit. "
               "The printed spelling of the penis word (मैंढ्र) is read as 'meḍhra'."),
    "explain_hi": ("इस इकाई की पहली पंक्ति मल की चर्चा को पूरा करती है: मुख से मल का निकलना और पहले कहे हुए रोग "
                   "भी ‘स्मृत’ (बताए गए) हैं। दूसरी पंक्ति नई सूची शुरू करती है: अंगभंग (अंगों का टूटना), "
                   "अश्मरी, और बस्ति, मेढ्र तथा वंक्षण की वेदना। इस सूची की क्रिया और कारण अगली इकाई "
                   "में आते हैं, इसलिए यहाँ कारण पर कोई प्रश्न नहीं। छपाई के जोड़े और वाक्य एक पंक्ति आगे-पीछे हैं।"),
    "hook": "मुख से मल, पहले वाले रोग; फिर अंगभंग, अश्मरी, तीन जगह वेदना।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What does line 1 say passes through the mouth?",
            ("Stool", "विट्प्रवृत्ति: passing of stool."),
            [("Urine", "Urine is not named in line 1."),
             ("Wind", "Wind is not named in line 1."),
             ("Breath", "Breath is not named in line 1.")],
            "मुखेन विट्प्रवृत्तिः = passing of stool through the mouth.",
            "मुखेन विट्प्रवृत्तिः = stool passing through the mouth."),
        match(1, "Match each word to its meaning.",
              [["मुख", "mouth"], ["वेदना", "pain"], ["वंक्षण", "groin"],
               ["अश्मरी", "stone"], ["पूर्वोक्त", "stated before"]],
              "Plain words of the unit.",
              "मुख = mouth; वेदना = pain; वंक्षण = groin; अश्मरी = stone; पूर्वोक्त = stated before."),
        order(2, "Put these items of the unit in the verse's order.",
              ["मुखेन विट्प्रवृत्तिः", "पूर्वोक्ता आमयाः", "अंगभंग", "अश्मरी", "बस्तिमैंढ्रवंक्षणवेदनाः"],
              "Line 1: stool through the mouth, earlier ailments; line 2: limb-breaking pain, stone, pains in three places.",
              "मुखेन विट्प्रवृत्तिः · पूर्वोक्ता आमयाः · अंगभंग · अश्मरी · बस्तिमैंढ्रवंक्षणवेदनाः.",
              role="extend",
              teaches="A sentence may run past its line: here line 2 starts a new list whose cause is stated only in the next unit."),
        mcq("discriminate", 3, "Which is the right split of पूर्वोक्ताश्चामयाः?",
            ("पूर्वोक्ताः + च + आमयाः", "Visarga + च → श्च; च + आ → चा."),
            [("पूर्वोक्ता + शचा + मयाः", "शचा is not a word."),
             ("पूर्वोक्ताः + चा + मयाः", "The word is आमयाः, not मयाः."),
             ("पूर्वोक्त + आश्च + आमयाः", "There is no word आश्च.")],
            "पूर्वोक्ताः (stated before) + च (and) + आमयाः (ailments).",
            "अः + च → श्च; अ + आ → आ."),
        multi("apply", 4, "Which are named as places of pain in line 2?",
              [("bladder", "Right: बस्ति here names a place of pain."),
               ("penis", "Right: मेढ्र (printed मैंढ्र)."),
               ("groin", "Right: वंक्षण."),
               ("head", "Not named in this line."),
               ("heart", "Not named in this line.")],
              [0, 1, 2],
              "Line 2 ends with pains of the bladder, penis and groin.",
              "बस्ति, मेढ्र, वंक्षण + वेदना."),
        mcq("transfer", 5, "Which is the joined form of रोगः + च?",
            ("रोगश्च", "Visarga + च → श्च, as in पूर्वोक्ताः + च = पूर्वोक्ताश्च."),
            [("रोगच", "The visarga does not just drop before च."),
             ("रोगस्च", "स् is for त, not for च."),
             ("रोगोच", "ओ comes before voiced sounds; च is not voiced.")],
            "विट्प्रवृत्तिः + च gives विट्प्रवृत्तिश्च; रोगः + च gives रोगश्च.",
            "Visarga + च → श्च.",
            teaches="A visarga before च becomes श् (विट्प्रवृत्तिः + च = विट्प्रवृत्तिश्च; रोगः + च = रोगश्च)."),
    ],
}

# ---------------------------------------------------------------- unit 7
AUTHORED["7"] = {
    "title": "स्युर्मूत्ररोधात्पूर्वे च",
    "question": "What does the unit give as the remedy for the urine ailments?",
    "rule": ("From suppression of urine the ailments (just listed) may arise, and mostly the "
             "earlier ones too; their remedy is wicks, anointing, immersion baths, sweating "
             "and enema treatment."),
    "limits": ("The first line completes the sentence begun in unit 6. 'पूर्वे' is read as the "
               "earlier diseases. The printed spelling of 'wicks' and 'anointing' is faulty; the "
               "list is read as in the data. Names only: no dose, no manner."),
    "explain_hi": ("पिछली इकाई की सूची का कारण यहाँ पूरा होता है: ‘मूत्ररोधात्’ (मूत्र रोकने से) वे रोग "
                   "‘स्युः’ (हो सकते हैं), और प्रायः पहले के रोग भी। फिर ‘तदौषधम्’ (उसका उपचार) के बाद पाँच नाम "
                   "आते हैं: बत्ती, अभ्यंग, अवगाह, स्वेदन और बस्तिकर्म। ‘प्रायः’ का अर्थ है ‘अधिकतर’, "
                   "यानी कोई पक्का नियम नहीं। श्लोक केवल नाम गिनाता है।"),
    "hook": "मूत्र रोका तो वही रोग; उपाय: बत्ती, अभ्यंग, अवगाह, स्वेद, बस्ति।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "From suppression of what does line 1 say the ailments may arise?",
            ("Urine", "मूत्ररोधात्: from suppression of urine."),
            [("Stool", "Stool was the topic of the earlier units, not of this line."),
             ("A sneeze", "A sneeze is not mentioned in this line."),
             ("Thirst", "Thirst is not mentioned in this line.")],
            "The line opens with स्युः मूत्ररोधात्.",
            "मूत्ररोधात् = from suppression of urine."),
        match(1, "Match each word to its meaning.",
              [["मूत्र", "urine"], ["रोध", "suppression"], ["औषध", "remedy"],
               ["प्रायः", "mostly"], ["पूर्वे", "the earlier ones"]],
              "Plain words of the first line.",
              "मूत्र = urine; रोध = suppression; औषध = remedy; प्रायः = mostly; पूर्वे = the earlier ones."),
        order(2, "After the wicks, put the four remedies in the verse's order.",
              ["अभ्यंग", "अवगाह", "स्वेदन", "बस्तिकर्म"],
              "Line 2 runs: wicks, anointing, immersion baths, sweating, enema treatment.",
              "अभ्यंग · अवगाह · स्वेदन · बस्तिकर्म.", role="extend",
              teaches="The first three members are in one compound (…अवगाहाः) and the last two stand as separate words, all naming the remedy."),
        mcq("discriminate", 3, "Which is the right split of मूत्ररोधात्पूर्वे?",
            ("मूत्ररोधात् + पूर्वे", "A final त् before प stays त्."),
            [("मूत्ररोधा + त्पूर्वे", "त्पूर्वे is not a word."),
             ("मूत्ररोध + आत्पूर्वे", "There is no word आत्पूर्वे."),
             ("मूत्ररोधाः + पूर्वे", "A visarga would show in the print, not त्.")],
            "मूत्ररोधात् (from suppression of urine) + पूर्वे (the earlier ones).",
            "Final त् before प is unchanged."),
        multi("apply", 4, "Which are named as the remedy in this unit?",
              [("anointing (अभ्यंग)", "Right: named."),
               ("immersion baths (अवगाह)", "Right: named."),
               ("enema treatment (बस्तिकर्म)", "Right: named."),
               ("ghee before the meal", "Not in this unit."),
               ("bringing on a sneeze", "Not in this unit.")],
              [0, 1, 2],
              "Line 2 names wicks, anointing, immersion baths, sweating and enema treatment.",
              "Remedy: वर्ति, अभ्यंग, अवगाह, स्वेदन, बस्तिकर्म."),
        mcq("transfer", 5, "Which word means from suppression of an urge?",
            ("वेगरोधात्", "-आत् is the 'from' ending, as in मूत्ररोधात्."),
            [("वेगरोधेन", "-एन means 'by'."),
             ("वेगरोधे", "-ए means 'in'."),
             ("वेगरोधस्य", "-स्य means 'of'.")],
            "मूत्ररोधात् is 'from suppression of urine'; वेगरोधात् is 'from suppression of an urge'.",
            "-आत् = from.",
            teaches="A word like रोध takes -आत् for 'from, because of' (मूत्ररोधात् = from suppression of urine; वेगरोधात् = from suppression of an urge)."),
    ],
}

# ---------------------------------------------------------------- unit 8
AUTHORED["8"] = {
    "title": "अन्नपानं च विड्भेदि",
    "question": "What does the unit recommend for the ailments from stool and from urine?",
    "rule": ("In wasting ailments from stool retention, food and drink that loosen stool; in "
             "those from urine, ghee before the meal is recommended."),
    "limits": ("The first line has no verb; 'is recommended' (शस्यते) is understood from line 2. "
               "'पाने च' can mean 'in drinking' or the manner of taking: it is left out. "
               "'यक्ष्म' is a named group; no modern diagnosis is meant."),
    "explain_hi": ("यह इकाई दो स्थितियों के लिए बताती है। मल के रुकने से उत्पन्न यक्ष्मों में "
                   "‘विड्भेदि’ (मल को ढीला करने वाले) अन्न और पेय। मूत्र से उत्पन्न रोगों में "
                   "‘प्राग्भक्तात्’ (भोजन से पहले) घी ‘शस्यते’ (हितकर कहा गया है)। पहली पंक्ति में क्रिया "
                   "नहीं है, वह दूसरी पंक्ति से आती है। ‘पाने च’ दो तरह पढ़ा जा सकता है, इसलिए उस पर कोई प्रश्न नहीं।"),
    "hook": "मल-रोध में विड्भेदि अन्न-पान; मूत्रज में भोजन से पहले घी।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What does line 2 recommend before the meal?",
            ("Ghee", "प्राग्भक्ताच्छस्यते घृतम्: ghee is recommended before the meal."),
            [("Wicks", "Wicks are not named in this unit."),
             ("Sweating", "Sweating is not named in this unit."),
             ("Enemas", "Enemas are not named in this unit.")],
            "The line says ghee is recommended before the meal.",
            "प्राग्भक्तात् = before the meal; घृतम् = ghee."),
        match(1, "Match each word to its meaning.",
              [["प्राग्भक्तात्", "before the meal"], ["घृतम्", "ghee"],
               ["विड्भेदि", "stool-loosening"], ["मूत्रज", "arising from urine"],
               ["शस्यते", "is recommended"]],
              "Words of the unit.",
              "प्राग्भक्तात् = before the meal; घृत = ghee; विड्भेदि = stool-loosening; मूत्रज = arising from urine; शस्यते = is recommended."),
        fill(2, "The word for 'ghee' in line 2 is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("घृतम्", None, "घृत"),
             "घृतम् is the thing recommended; it is the subject of शस्यते.",
             "घृत is the word for ghee; ending -म् shows the neuter singular subject of 'is recommended'.",
             "घृतम् = ghee.", role="extend"),
        mcq("discriminate", 3, "Which is the right split of विड्विबन्धोत्थेषु?",
            ("विड्विबन्ध + उत्थेषु", "अ + उ gives ओ."),
            [("विड्विबन्धो + थेषु", "थेषु is not a word."),
             ("विड्विबन्ध + ओत्थेषु", "The ओ comes from the join; there is no word ओत्थेषु."),
             ("विड्विबन्धा + उत्थेषु", "आ + उ would also give ओ, but the first part has a short अ.")],
            "विड्विबन्ध (retention of stool) + उत्थेषु (arising from): अ + उ → ओ.",
            "अ + उ → ओ."),
        order(4, "Leaving out small words, put the phrases of the unit in the verse's order.",
              ["अन्नपानम्", "विड्भेदि", "विड्विबन्धोत्थेषु यक्ष्मसु", "मूत्रजेषु", "प्राग्भक्ताच्छस्यते घृतम्"],
              "Line 1: food and drink, stool-loosening, in the ailments from stool retention; line 2: from urine, ghee before the meal.",
              "अन्नपानम् · विड्भेदि · विड्विबन्धोत्थेषु यक्ष्मसु · मूत्रजेषु · प्राग्भक्ताच्छस्यते घृतम्.",
              role="apply"),
        mcq("transfer", 5, "Which word means in forests?",
            ("वनेषु", "-एषु is the 'in' ending in the plural, as in मूत्रजेषु 'in those arising from urine'."),
            [("वनैः", "-ऐः means 'by'."),
             ("वनानाम्", "-आनाम् means 'of'."),
             ("वनेन", "-एन means 'by' (singular).")],
            "मूत्रजेषु is the 'in (those)' form; वन works the same: वनेषु.",
            "-एषु = in (plural).",
            teaches="A plural word with -एषु means 'in …' (विड्विबन्धोत्थेषु, मूत्रजेषु = in those arising from…); likewise वनेषु = in forests."),
    ],
}

# ---------------------------------------------------------------- unit 9
AUTHORED["9"] = {
    "title": "अवपीडकमेतच्च",
    "question": "Which clear words and joins does this obscure unit still show?",
    "rule": ("The unit is obscure; its meaning is not tested. Only plain words and joins are "
             "used: एतत्, च, संज्ञितम्, धारणात्, पुनः, and the sandhi एतत् + च = एतच्च."),
    "limits": ("Low confidence. Line 1 is obscure and the technical word 'avapīḍaka' is not "
               "explained here; no question rests on what the unit teaches. 'धारणात् पुनः' really "
               "opens the next sentence (unit 10). Only words and joins are tested."),
    "explain_hi": ("यह इकाई छपाई में अस्पष्ट है और विश्वास कम है। पहली पंक्ति का भाव (‘जीर्णान्तिक’, "
                   "‘योजनाद्वय’) और ‘अवपीडक’ नामक शब्द यहाँ नहीं समझाए गए, इसलिए अर्थ पर प्रश्न नहीं हैं। "
                   "दूसरी पंक्ति में साफ़ शब्द हैं: एतत् (यह), च (और), संज्ञितम् (नाम दिया गया) और "
                   "‘धारणात् पुनः’ (फिर रोकने से), जो असल में अगले वाक्य की शुरुआत है। केवल शब्द और संधि याद करें।"),
    "hook": "अस्पष्ट इकाई: बस शब्द और संधि पहचानो; अर्थ पर भरोसा नहीं।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "Which is the right split of एतच्च?",
            ("एतत् + च", "A final त् before च becomes च्."),
            [("एत + च्च", "च्च is not a word."),
             ("एतः + च", "A visarga before च would give श्च."),
             ("एतद् + च", "द् would stay द्; it does not become च्.")],
            "एतत् (this) + च (and): त् + च → च्च.",
            "Final त् + च → च्च."),
        match(1, "Match each plain word of line 2 to its meaning.",
              [["एतत्", "this"], ["च", "and"], ["संज्ञितम्", "is named"],
               ["धारणात्", "from holding back"], ["पुनः", "again"]],
              "Only the clear words are tested.",
              "एतत् = this; च = and; संज्ञितम् = is named; धारणात् = from holding back; पुनः = again."),
        fill(2, "The word for 'again' in line 2 is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("पुनः"),
             "पुनः means 'again'; the visarga may be dropped when typing.",
             "पुनः is a word that never changes its ending; it means 'again'.",
             "पुनः = again.", role="extend"),
        mcq("discriminate", 3, "Which is the right split of धारणात्पुनः?",
            ("धारणात् + पुनः", "A final त् before प stays त्."),
            [("धारणा + त्पुनः", "त्पुनः is not a word."),
             ("धारण + आत्पुनः", "There is no word आत्पुनः."),
             ("धारणाः + पुनः", "A visarga would show in the print, not त्.")],
            "धारणात् (from holding back) + पुनः (again).",
            "Final त् before प is unchanged."),
        order(4, "Put the words of line 2 in the verse's order.",
              ["अवपीडकम्", "एतत्", "च", "संज्ञितम्", "धारणात्", "पुनः"],
              "Line 2 runs: avapīḍaka, this, and, is named, from holding back, again.",
              "अवपीडकम् · एतत् · च · संज्ञितम् · धारणात् · पुनः.", role="apply"),
        mcq("transfer", 5, "Which is the joined form of तत् + च?",
            ("तच्च", "Final त् before च becomes च्, as in एतत् + च = एतच्च."),
            [("तत्च", "The join changes the त."),
             ("तद्च", "द् is for voiced sounds; च is not voiced."),
             ("ततच", "No letter is added or dropped like this.")],
            "एतत् + च gives एतच्च; तत् + च gives तच्च.",
            "त् + च → च्च.",
            teaches="A final त् before च becomes च् (एतत् + च = एतच्च; तत् + च = तच्च)."),
    ],
}

# ---------------------------------------------------------------- unit 10
AUTHORED["10"] = {
    "title": "उद्गारस्यारुचिः कंपः",
    "question": "What does the unit list for holding back a belch?",
    "rule": ("From (holding back) a belch: distaste for food, tremor, obstruction in heart and "
             "chest, distension, cough, hiccups; the remedy is as for hiccups."),
    "limits": ("'Holding back' comes from धारणात् at the end of unit 9, so the unit alone has the "
               "genitive उद्गारस्य. हृदयोरसोः is a dual read as 'in heart and chest'."),
    "explain_hi": ("अब तीसरा वेग: उद्गार (डकार)। ‘रोकने से’ का भाव पिछली इकाई के ‘धारणात्’ से आता है। "
                   "सूची में छह नाम: अरुचि, कंप, हृदय और छाती में विबंध, आध्मान (अफारा), कास और हिध्मा। "
                   "अंत में कहा गया है कि उपचार ‘हिध्मावत्’ है, यानी हिचकी के समान। ‘हृदय + उरसोः’ मिलकर "
                   "हृदयोरसोः बना है (अ + उ → ओ)।"),
    "hook": "डकार रोका: अरुचि, कंप, विबंध, अफारा, खाँसी, हिचकी।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "Which urge does the unit's first word, उद्गारस्य, name?",
            ("A belch", "उद्गार is a belch."),
            [("A sneeze", "A sneeze is the topic of unit 11."),
             ("A cough", "Cough is in the list of results, not the urge here."),
             ("Hiccups", "Hiccups are in the list of results, not the urge here.")],
            "The unit opens with उद्गारस्य, 'of a belch'.",
            "उद्गार = belch."),
        order(1, "Put the six results in the order of the verse.",
              ["अरुचि", "कंप", "विबंध", "आध्मान", "कास", "हिध्मा"],
              "The verse runs: distaste for food, tremor, obstruction, distension, cough, hiccups.",
              "अरुचि · कंप · विबंध · आध्मान · कास · हिध्मा."),
        match(2, "Match each word to its meaning.",
              [["अरुचि", "distaste for food"], ["कंप", "tremor"], ["आध्मान", "distension"],
               ["कास", "cough"], ["हिध्मा", "hiccups"]],
              "Names of the results listed.",
              "अरुचि = distaste for food; कंप = tremor; आध्मान = distension; कास = cough; हिध्मा = hiccups.",
              role="extend",
              teaches="The prefix अ- negates: अरुचि is the lack of taste or liking for food."),
        mcq("discriminate", 3, "Which is the right split of हृदयोरसोः?",
            ("हृदय + उरसोः", "अ + उ gives ओ."),
            [("हृदयो + रसोः", "रसोः is not the word; it is उरसोः."),
             ("हृदय + ओरसोः", "The ओ is made by the join; there is no word ओरसोः."),
             ("हृदयः + उरसोः", "A visarga before उ would give हृदय उरसोः, not ओ.")],
            "हृदय (heart) + उरसोः (in the chest, dual): अ + उ → ओ.",
            "अ + उ → ओ."),
        multi("apply", 4, "Which of these does the unit name as results?",
              [("tremor", "Right: कंप."),
               ("cough", "Right: कास."),
               ("hiccups", "Right: हिध्मा."),
               ("calf cramps", "That is in the stool unit."),
               ("head pain", "That is in the sneeze unit.")],
              [0, 1, 2],
              "Tremor, cough and hiccups are in the list; calf cramps and head pain are not.",
              "Results: अरुचि, कंप, विबंध, आध्मान, कास, हिध्मा."),
        mcq("transfer", 5, "Which word means like a snake?",
            ("सर्पवत्", "-वत् at the end means 'like, as for', as in हिध्मावत्."),
            [("सर्पस्य", "-स्य means 'of a snake'."),
             ("सर्पेण", "-एण means 'by a snake'."),
             ("सर्पतः", "-तः means 'from a snake'.")],
            "हिध्मावत् is 'like hiccup'; सर्पवत् is 'like a snake'.",
            "X-वत् = like X.",
            teaches="A word ending in -वत् means 'like, as for' the first part (हिध्मावत् = as for hiccups; सर्पवत् = like a snake)."),
    ],
}

# ---------------------------------------------------------------- unit 11
AUTHORED["11"] = {
    "title": "शिरोर्तीन्द्रियदौर्बल्य",
    "question": "What does the unit list for holding back a sneeze?",
    "rule": ("From (holding back) a sneeze: head pain, weakness of the senses, stiffness of the "
             "neck and ardita; then a list of means: sharp smoke, collyrium, sniffing, nasal "
             "drops, looking at the sun."),
    "limits": ("The sentence ends in unit 12, where the verb 'one should bring on' stands. "
               "'अर्क' is read as the sun but may be a drug name, so it is not tested. ardita is "
               "a name only; no diagnosis. Printed 'शिरोर्ति' is शिरः + अर्ति."),
    "explain_hi": ("चौथा वेग: क्षुत् (छींक)। ‘क्षुतेः’ से छींक रोकने के परिणाम गिनाए गए हैं: सिर में पीड़ा, "
                   "इंद्रियों की दुर्बलता, मन्या (गर्दन) की जकड़न और अर्दित। दूसरी पंक्ति में उपाय के नाम आते हैं: "
                   "तीखा धुआँ, अंजन, सूँघना, नस्य, और सूर्य को देखना। इनके साथ की क्रिया अगली इकाई में है। "
                   "‘अर्क’ का अर्थ दो तरह लिया जा सकता है, इसलिए उस पर प्रश्न नहीं हैं।"),
    "hook": "छींक रोकी: सिरदर्द, इंद्रिय-दुर्बलता, गर्दन-जकड़न, अर्दित।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "From holding back which urge does the first line list its results?",
            ("A sneeze", "क्षुतेः: from a sneeze."),
            [("A belch", "A belch was the topic of unit 10."),
             ("A cough", "Cough is not the urge in this unit."),
             ("A yawn", "A yawn is not the urge in this unit.")],
            "The first line ends with क्षुतेः, 'from a sneeze'.",
            "क्षुतेः = from a sneeze."),
        order(1, "Put the four results of the first line in the verse's order.",
              ["शिरोर्ति", "इन्द्रियदौर्बल्य", "मन्यास्तंभ", "अर्दित"],
              "Line 1 runs: head pain, weakness of the senses, stiffness of the neck, ardita.",
              "शिरोर्ति · इन्द्रियदौर्बल्य · मन्यास्तंभ · अर्दित."),
        match(2, "Match each word to its meaning.",
              [["शिरोर्ति", "head pain"], ["इन्द्रियदौर्बल्य", "weakness of the senses"],
               ["मन्यास्तंभ", "stiffness of the neck"], ["अंजन", "collyrium"],
               ["नावन", "nasal drops"]],
              "Words of the two lines.",
              "शिरोर्ति = head pain; इन्द्रिय-दौर्बल्य = weakness of the senses; मन्या-स्तंभ = stiffness of the neck; अंजन = collyrium; नावन = nasal drops.",
              role="extend",
              teaches="In a compound the last member names the thing, the earlier ones qualify it: मन्या-स्तंभ is 'stiffness of the neck'."),
        mcq("discriminate", 3, "Which is the right split of the printed शिरोर्ति?",
            ("शिरः + अर्ति", "A visarga after अ becomes ओ before a voiced sound; here the अ of अर्ति is absorbed."),
            [("शिर + ओर्ति", "ओर्ति is not a word."),
             ("शिरो + र्ति", "र्ति is not a word."),
             ("शिरः + उर्ति", "उर्ति is not a word.")],
            "शिरः (head) + अर्ति (pain): शिरोऽर्ति, printed here without the avagraha.",
            "अः + अ → ओऽ."),
        order(4, "Leaving out the last member (looking at the sun), put the four means in the verse's order.",
              ["तीक्ष्णधूम", "अंजन", "आघ्राण", "नावन"],
              "Line 2 runs: sharp smoke, collyrium, sniffing, nasal drops, (then looking at the sun).",
              "तीक्ष्णधूम · अंजन · आघ्राण · नावन.", role="apply"),
        mcq("transfer", 5, "Which word means by fruits?",
            ("फलैः", "-ऐः is the plural 'by' ending, as in विलोकनैः."),
            [("फलेन", "-एन means 'by a fruit' (singular)."),
             ("फलेषु", "-एषु means 'in fruits'."),
             ("फलानाम्", "-आनाम् means 'of fruits'.")],
            "विलोकनैः is 'by lookings'; फलैः is 'by fruits'.",
            "-ऐः = by (plural).",
            teaches="A plural word in -ऐः means 'by, through' (विलोकनैः = by looking, among many means; फलैः = by fruits)."),
    ],
}

# ---------------------------------------------------------------- unit 12
AUTHORED["12"] = {
    "title": "प्रवर्त्तयेत्क्षुतिं सक्तां",
    "question": "What does the unit say to do about a held-back sneeze?",
    "rule": ("One should bring on the held-back sneeze, practise sweating and anointing, apply "
             "wind-relieving food, and ghee after the meal."),
    "limits": ("This unit finishes the sentence of unit 11. The verse gives names only: no dose "
               "and no manner. 'उत्तरभक्तकम्' is read as 'after the meal'."),
    "explain_hi": ("छींक की इकाई यहाँ पूरी होती है। रुकी हुई छींक (‘सक्ताम्’) को ‘प्रवर्तयेत्’ "
                   "(प्रवृत्त करे); स्वेद और अभ्यंग का सेवन करे (द्विवचन ‘स्वेदाभ्यंगौ’); वातनाशक अन्न "
                   "‘योज्यम्’ (प्रयोग के योग्य) है, और घी भोजन के ‘उत्तर’ (बाद) में। "
                   "संधि: च + उत्तरभक्तकम् → चोत्तरभक्तकम्। श्लोक केवल नाम देता है, मात्रा नहीं।"),
    "hook": "रुकी छींक को चलाओ; स्वेद-अभ्यंग, वातनाशक अन्न, भोजन बाद घी।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What does the verse say to do with a held-back sneeze?",
            ("Bring it on", "प्रवर्त्तयेत्क्षुतिं सक्ताम्: one should bring on the held-back sneeze."),
            [("Hold it back longer", "The verse says the opposite."),
             ("Ignore it", "The verse gives an action: bring it on."),
             ("Wait for it to pass", "No waiting is mentioned.")],
            "प्रवर्त्तयेत् = one should bring on; क्षुतिं सक्ताम् = the held-back sneeze.",
            "प्रवर्त्तयेत् क्षुतिं सक्ताम् = one should bring on the held-back sneeze."),
        order(1, "Put the phrases of the unit in the verse's order.",
              ["प्रवर्त्तयेत्क्षुतिं सक्तां", "स्वेदाभ्यंगौ च शीलयेत्", "योज्यं वातघ्नमन्नं च", "घृतं चोत्तरभक्तकम्"],
              "The unit runs: bring on the sneeze; sweating and anointing; wind-relieving food; ghee after the meal.",
              "प्रवर्त्तयेत्क्षुतिं सक्तां · स्वेदाभ्यंगौ च शीलयेत् · योज्यं वातघ्नमन्नं च · घृतं चोत्तरभक्तकम्."),
        match(2, "Match each word to its meaning.",
              [["सक्ताम्", "held back"], ["स्वेदाभ्यंगौ", "sweating and anointing"],
               ["योज्यम्", "to be applied"], ["उत्तरभक्तकम्", "after the meal"],
               ["शीलयेत्", "one should practise"]],
              "Words of the unit.",
              "सक्त = held back; स्वेद-अभ्यंग = sweating and anointing; योज्य = to be applied; उत्तरभक्तक = after the meal; शीलयेत् = one should practise.",
              role="extend",
              teaches="A word in -य like योज्य can mean 'to be done' (to be applied): the thing is fit or due to be used."),
        mcq("discriminate", 3, "Which is the right split of चोत्तरभक्तकम्?",
            ("च + उत्तरभक्तकम्", "अ + उ gives ओ."),
            [("चो + त्तरभक्तकम्", "त्तरभक्तकम् is not a word."),
             ("च + ओत्तरभक्तकम्", "The ओ is made by the join; there is no word ओत्तरभक्तकम्."),
             ("चः + उत्तरभक्तकम्", "A visarga would not join to give चोत्त-.")],
            "च (and) + उत्तरभक्तकम् (after the meal): अ + उ → ओ.",
            "अ + उ → ओ."),
        multi("apply", 4, "Which does the unit say should be done or applied?",
              [("sweating (स्वेद)", "Right: स्वेदाभ्यंगौ शीलयेत्."),
               ("anointing (अभ्यंग)", "Right: स्वेदाभ्यंगौ शीलयेत्."),
               ("ghee after the meal", "Right: घृतं चोत्तरभक्तकम्."),
               ("ghee before the meal", "The unit says after, not before."),
               ("looking at the sun", "Not named in this unit.")],
              [0, 1, 2],
              "Sweating, anointing and ghee after the meal are named; ghee before the meal and looking at the sun are not.",
              "Named: स्वेद, अभ्यंग, वातघ्न अन्न, उत्तरभक्त घृत."),
        mcq("transfer", 5, "Which word means two feet, as स्वेदाभ्यंगौ names a pair?",
            ("पादौ", "The dual of an a-word ends in -औ, as in स्वेदाभ्यंगौ."),
            [("पादाः", "-आः is the plural 'feet'."),
             ("पादम्", "-म् is one foot."),
             ("पादेन", "-एन means 'by a foot'.")],
            "स्वेदाभ्यंगौ names a pair; पादौ is the pair of feet.",
            "Dual of an a-word: -औ.",
            teaches="The dual of a word in -अ ends in -औ in the nominative and accusative (स्वेदाभ्यंगौ = two things; पादौ = two feet)."),
    ],
}

# ================================================================= NOTES
NOTES_HI = {
    "1": "विश्वास: उच्च। कोई पाठ-दोष नहीं। संधि जाँची: अथातो = अथ + अतः (अ + अ → आ, फिर विसर्ग → ओ र के पहले); रोगानुत्पादनीयम् = रोग + अनुत्पादनीयम् (अ + अ → आ)।",
    "2": "विश्वास: उच्च। श्रम और श्वास को दो अलग पद लिया गया है; पुस्तक का विभाजन भी वही है, पर ‘श्रम से चढ़ी साँस’ पढ़ना भी संभव है। ‘च्छर्द्दि’ छर्दि का वर्तनी-भेद है। संधि जाँची: धारयेद्वात = धारयेत् + वात (त् → द् घोष से पहले); वेगान्न = वेगान् + न।",
    "3": "विश्वास: उच्च। ‘वध’ दृष्टि और अग्नि दोनों पर लगता है; ‘संग’ केवल वात-मूत्र-मल पर या अधिक पर, यह दो तरह पढ़ा जा सकता है। गुल्म और उदावर्त केवल नाम रखे गए हैं। क्रिया ‘होते हैं’ अध्याहार है। संधि जाँची: अधोवातस्य = अधः + वातस्य (अः → ओ)।",
    "4": "विश्वास: उच्च। ‘शस्तम्’ एकवचन है और बहुवचन सूची के लिए सामूहिक है। ‘वातानुलोमनम्’ पूरी सूची का विशेषण लिया गया है; उसे एक और सदस्य मानना भी संभव है। संधि जाँची: बस्तयश्चैव = बस्तयः + च + एव; विधिस्तत्र = विधिः + तत्र।",
    "5": "विश्वास: उच्च। ‘शकृतः’ षष्ठी है, ‘रोधात्/रोधेन’ अध्याहार। ‘परिकर्तः’ यहाँ पुल्लिंग है (प्रायः ‘परिकर्तिका’)। ‘ऊर्ध्वं वायुः’ का दो तरह अर्थ संभव है, उस पर प्रश्न नहीं। संधि जाँची: पिंडिकोद्वेष्ट = पिंडिका + उद्वेष्ट; हृदयस्योपरोधनम् = हृदयस्य + उपरोधनम्।",
    "6": "विश्वास: मध्यम। संयोजन: पहली पंक्ति मल के विषय को पूरा करती है, दूसरी पंक्ति (मूत्र-रोध की सूची) की क्रिया अगली इकाई की पहली पंक्ति में है; छपाई का जोड़ा रखा गया है। छपा ‘मैंढ्र’ को डेटा में ‘मेढ्र’ लिया गया है। ‘अश्मरी’ का शाब्दिक अर्थ ‘पथरी’। संधि जाँची: पूर्वोक्ताश्चामयाः = पूर्वोक्ताः + च + आमयाः।",
    "7": "विश्वास: मध्यम। पाठ-चिह्न: ‘वत्त्यंभ्यंगावगाहाश्च’ में वर्ति का र् छूटा है और अनुस्वार अतिरिक्त है (सुझाव: वर्त्त्यभ्यङ्गावगाहाश्च); अर्थ वही रहता है, पर प्रश्नों में बत्ती को छोड़ा गया। पहली पंक्ति पिछली इकाई की सूची की क्रिया पूरी करती है। ‘पूर्वे’ = पहले बताए रोग। ‘बस्तिकर्मच’ बिना खाली स्थान छपा है।",
    "8": "विश्वास: मध्यम। पहली पंक्ति में क्रिया नहीं है, ‘शस्यते’ दूसरी पंक्ति से अध्याहार। ‘पाने च’ दो तरह पढ़ा जा सकता है (पीने में, या सेवन का ढंग), इसलिए नहीं लिया गया। यक्ष्म केवल एक नामित वर्ग है। संधि जाँची: विड्विबन्धोत्थेषु = विड्विबन्ध + उत्थेषु (अ + उ → ओ)।",
    "9": "विश्वास: कम। पहली पंक्ति अस्पष्ट है (‘जीर्णान्तिकं’, ‘योजनाद्वयं’ के दो पाठ संभव) और ‘अवपीडक’ तकनीकी शब्द बिना अर्थ के रखा गया है; अनुवाद अस्थायी है। ‘धारणात् पुनः’ (5.17) संपादकों द्वारा अगले विषय का आरंभ चिह्नित है और असल में इकाई 10 के वाक्य में जाता है। इसलिए कोई प्रश्न अर्थ पर नहीं, केवल साफ़ शब्दों और संधि (एतत् + च = एतच्च; धारणात् + पुनः) पर है।",
    "10": "विश्वास: उच्च। ‘रोकने से’ पिछली इकाई के ‘धारणात्’ से आता है (इकाई 9 की टिप्पणी देखें)। हृदयोरसोः द्विवचन है, सप्तमी के अर्थ में लिया गया। ‘हिध्मावत्’ = हिचकी के समान। संधि जाँची: हृदयोरसोः = हृदय + उरसोः (अ + उ → ओ)।",
    "11": "विश्वास: उच्च। वाक्य इकाई 12 में पूरा होता है (प्रवर्तयेत् क्षुतिं सक्ताम्)। छपा ‘शिरोर्ति’ शिरः + अर्ति है (सामान्यतः शिरोऽर्ति)। ‘अर्क’ को सूर्य लिया गया है, पर यह औषधि का नाम भी हो सकता है; तय नहीं, इसलिए उस पर प्रश्न नहीं। अर्दित नाम भर है, निदान नहीं। ‘क्षुतेः’ क्षुति का षष्ठी/पंचमी रूप है।",
    "12": "विश्वास: उच्च। ‘प्रवर्त्तयेत्’ में ‘त्त’ दोहरा छपा है (वर्तनी-भेद)। ‘उत्तरभक्तक’ = भोजन के बाद का (घी)। संधि जाँची: चोत्तरभक्तकम् = च + उत्तरभक्तकम् (अ + उ → ओ); स्वेदाभ्यंगौ = स्वेद + अभ्यंगौ (अ + अ → आ)।",
}

# ================================================================= AIDS
AIDS = {
    "1": {
        "chunks": "अथातो | रोगानुत्पादनीयमध्यायं | व्याख्यास्यामः।",
        "sandhi": "अ + अ → आ: अथ + अतः → अथातः; अः + र → ओ र: अथातो रोग…। रोग + अनुत्पादनीयम् → रोगानुत्पादनीयम्।",
        "frame": "कब: अब, इसलिए · क्या: रोगानुत्पादनीय अध्याय · क्रिया: व्याख्या करेंगे।",
    },
    "2": {
        "diagram": {"groups": [
            {"label": "पहली पंक्ति के छह वेग", "items": ["वात", "विट्", "मूत्र", "क्षव", "तृट्", "क्षुधा"]},
            {"label": "दूसरी पंक्ति के आठ वेग", "items": ["निद्रा", "कास", "श्रम", "श्वास", "जृंभा", "अश्रु", "छर्दि", "रेतस्"]}]},
        "chunks": "वेगान्न धारयेद् | वातविण्मूत्रक्षवतृट्क्षुधाम् ‖ निद्राकासश्रमश्वास | जृंभाश्रुच्छर्दिरेतसाम्।",
        "sandhi": "त् → द् घोष से पहले: धारयेत् + वात → धारयेद्वात। वेगान् + न → वेगान्न।",
        "frame": "क्या न करें: वेगों को न रोकें · कितने: छह (पहली पंक्ति) + आठ (दूसरी) · क्रिया: न धारयेत्।",
        "pegs": "मेरा बनाया क्रम: ऊपर की रेखा में छह वेग, नीचे की रेखा में आठ और। केवल याद के लिए।",
    },
    "3": {
        "diagram": {"groups": [
            {"label": "पहली पंक्ति", "items": ["गुल्म", "उदावर्त", "रुक्", "क्लम"]},
            {"label": "दूसरी पंक्ति", "items": ["वात-मूत्र-मल का संग", "दृष्टि-अग्नि का वध", "हृद्गद"]}]},
        "chunks": "अधोवातस्य रोधेन | गुल्मोदावर्तरुक्क्लमाः ‖ वातमूत्रशकृत्संग | दृष्ट्यग्निवधहृद्गदाः।",
        "sandhi": "अः + घोष → ओ: अधः + वातस्य → अधोवातस्य। अ + उ → ओ: गुल्म + उदावर्त → गुल्मोदावर्त।",
        "frame": "किसे रोका: अधोवात · कैसे: रोध से · क्या हुआ: चार पहली पंक्ति में, तीन भाग दूसरी में।",
    },
    "4": {
        "chunks": "स्नेहस्वेदविधिस्तत्र | वर्त्तयो भोजनानि च ‖ पानानि बस्तयश्चैव | शस्तं वातानुलोमनम्।",
        "sandhi": "विसर्ग + त → स्त: विधिः + तत्र → विधिस्तत्र। विसर्ग + च → श्च: बस्तयः + च → बस्तयश्च।",
        "frame": "कहाँ: उस दशा में · क्या: स्नेह-स्वेद-विधि, बत्ती, भोजन, पान, बस्ति · कैसे: वात को ठीक मार्ग पर चलाने वाले।",
    },
    "5": {
        "diagram": {"groups": [{"label": "मल रोकने से", "items": [
            "पिंडिकोद्वेष्ट", "प्रतिश्याय", "शिरोरुज्", "ऊर्ध्वं वायुः", "परिकर्त", "हृदयोपरोधन"]}]},
        "chunks": "शकृतः पिंडिकोद्वेष्ट | प्रतिश्यायशिरोरुजः ‖ ऊर्ध्वं वायुः परिकर्तो | हृदयस्योपरोधनम्।",
        "sandhi": "अ/आ + उ → ओ: पिंडिका + उद्वेष्ट → पिंडिकोद्वेष्ट; हृदयस्य + उपरोधनम् → हृदयस्योपरोधनम्।",
        "pegs": "मेरा बनाया चित्र: नीचे पिंडली से ऊपर सिर तक चढ़ती एक रेखा। केवल याद के लिए, श्लोक का दावा नहीं।",
    },
    "6": {
        "chunks": "मुखेन विट्प्रवृत्तिश्च | पूर्वोक्ताश्चामयाः स्मृताः ‖ अंगभंगाश्मरीबस्ति | मैंढ्रवंक्षणवेदनाः।",
        "sandhi": "विसर्ग + च → श्च: विट्प्रवृत्तिः + च → विट्प्रवृत्तिश्च; पूर्वोक्ताः + च + आमयाः → पूर्वोक्ताश्चामयाः।",
        "frame": "पहली पंक्ति: मुख से मल, पहले के रोग · दूसरी पंक्ति: अंगभंग, अश्मरी, तीन जगह वेदना (बस्ति, मेढ्र, वंक्षण)।",
    },
    "7": {
        "diagram": {"groups": [{"label": "मूत्र-रोध का उपचार", "items": [
            "वर्ति", "अभ्यंग", "अवगाह", "स्वेदन", "बस्तिकर्म"]}]},
        "chunks": "स्युर्मूत्ररोधात्पूर्वे च | प्रायो रोगास्तदौषधम् ‖ वत्त्यंभ्यंगावगाहाश्च | स्वेदनं बस्तिकर्म च।",
        "sandhi": "त् + प अपरिवर्तित: मूत्ररोधात् + पूर्वे। अः + र → ओ: प्रायः + रोगाः → प्रायो रोगाः।",
        "anchors": "रोध = रोकना · औषध = उपचार · प्रायः = अधिकतर · अवगाह = डुबकी वाला स्नान।",
    },
    "8": {
        "chunks": "अन्नपानं च विड्भेदि | विड्विबन्धोत्थेषु यक्ष्मसु ‖ मूत्रजेषु तु पाने च | प्राग्भक्ताच्छस्यते घृतम्।",
        "sandhi": "अ + उ → ओ: विड्विबन्ध + उत्थेषु → विड्विबन्धोत्थेषु। प्राग्भक्तात् + शस्यते → प्राग्भक्ताच्छस्यते।",
        "frame": "मल-रोध से यक्ष्म में: विड्भेदि अन्न-पान · मूत्रज रोगों में: भोजन से पहले घी।",
        "contrast": "विड्भेदि (मल-रोध वाले में) ↔ मूत्रज (मूत्र वाले में): दो स्थितियाँ, दो उपाय।",
    },
    "9": {
        "chunks": "अवपीडकमेतच्च | संज्ञितं धारणात्पुनः।",
        "sandhi": "त् + च → च्च: एतत् + च → एतच्च। त् + प अपरिवर्तित: धारणात् + पुनः।",
        "anchors": "एतत् = यह · संज्ञितम् = नाम दिया गया · धारणात् = रोकने से · पुनः = फिर। (पहली पंक्ति अस्पष्ट, उसका अर्थ यहाँ नहीं लिया।)",
    },
    "10": {
        "diagram": {"groups": [{"label": "डकार रोकने से", "items": [
            "अरुचि", "कंप", "विबंध", "आध्मान", "कास", "हिध्मा"]}]},
        "chunks": "उद्गारस्यारुचिः कंपो | विबंधो हृदयोरसोः ‖ आध्मानकासहिध्माश्च | हिध्मावत्तत्र भेषजम्।",
        "sandhi": "अ + उ → ओ: हृदय + उरसोः → हृदयोरसोः। उद्गारस्य + अरुचिः → उद्गारस्यारुचिः।",
        "pegs": "मेरा बनाया चित्र: डकार से सीना कंपता है, अरुचि के बाद अफारा, खाँसी, हिचकी। केवल याद के लिए।",
    },
    "11": {
        "diagram": {"groups": [
            {"label": "छींक रोकने से", "items": ["शिरोर्ति", "इन्द्रियदौर्बल्य", "मन्यास्तंभ", "अर्दित"]},
            {"label": "दूसरी पंक्ति के साधन", "items": ["तीक्ष्णधूम", "अंजन", "आघ्राण", "नावन", "अर्क-विलोकन"]}]},
        "chunks": "शिरोर्तीन्द्रियदौर्बल्य | मन्यास्तंभार्दितं क्षुतेः ‖ तीक्ष्णधूमांजनाघ्राण | नावनार्कविलोकनैः।",
        "sandhi": "विसर्ग + अ → ओ: शिरः + अर्ति → शिरोर्ति। इ + इ → ई: अर्ति + इन्द्रिय → अर्तीन्द्रिय।",
        "frame": "किसे रोका: क्षुत् · क्या हुआ: चार · किन साधनों से: पाँच (क्रिया अगली इकाई में)।",
    },
    "12": {
        "chunks": "प्रवर्त्तयेत्क्षुतिं सक्तां | स्वेदाभ्यंगौ च शीलयेत् ‖ योज्यं वातघ्नमन्नं च | घृतं चोत्तरभक्तकम्।",
        "sandhi": "अ + अ → आ: स्वेद + अभ्यंगौ → स्वेदाभ्यंगौ। अ + उ → ओ: च + उत्तरभक्तकम् → चोत्तरभक्तकम्।",
        "frame": "पहली पंक्ति: छींक को प्रवृत्त करो, स्वेद-अभ्यंग करो · दूसरी पंक्ति: वातनाशक अन्न, भोजन के बाद घी।",
        "contrast": "उत्तरभक्त (भोजन के बाद) ↔ प्राग्भक्त (भोजन से पहले, इकाई 8): दोनों शब्द अलग इकाइयों में।",
    },
}

# ================================================================= IMAGES
IMAGE_SPECS = {
    ("2", "diagram"): {
        "file": "ch5b01-vega-2.svg",
        "alt": "Two columns: the six urges of line 1 (wind, stool, urine, sneeze, thirst, hunger) and the eight of line 2 (sleep, cough, exertion, breath, yawning, tears, vomiting, semen)",
        "type": "split",
        "title": "श्लोक २: न रोकने योग्य वेग",
        "cols": [["पहली पंक्ति (६)", ["वात", "विट्", "मूत्र", "क्षव", "तृट्", "क्षुधा"]],
                 ["दूसरी पंक्ति (८)", ["निद्रा", "कास", "श्रम", "श्वास", "जृंभा", "अश्रु", "छर्दि", "रेतस्"]]],
    },
    ("3", "diagram"): {
        "file": "ch5b01-adhovata-3.svg",
        "alt": "Two columns: line 1 gives gulma, udavarta, pain, fatigue; line 2 gives retention of wind-urine-stool, damage of sight and fire, heart ailments",
        "type": "split",
        "title": "श्लोक ३: अधोवात के रोध से",
        "cols": [["पहली पंक्ति", ["गुल्म", "उदावर्त", "रुक्", "क्लम"]],
                 ["दूसरी पंक्ति", ["वात-मूत्र-मल का संग", "दृष्टि-अग्नि का वध", "हृद्गद"]]],
    },
    ("5", "diagram"): {
        "file": "ch5b01-shakrit-5.svg",
        "alt": "Mind map: from stool suppression six conditions: calf cramps, nasal catarrh, head pain, upward wind, cutting pain, heart obstruction",
        "type": "mermaid",
        "code": ('mindmap\n  मल रोकने से\n    पिंडली की ऐंठन\n    प्रतिश्याय\n    सिर की पीड़ा\n'
                 '    ऊर्ध्वं वायुः\n    परिकर्त\n    हृदय में रुकावट\n'),
    },
    ("7", "diagram"): {
        "file": "ch5b01-mutra-7.svg",
        "alt": "Mind map: remedy for the ailments of urine suppression, five names: wicks, anointing, immersion baths, sweating, enema treatment",
        "type": "mermaid",
        "code": ('mindmap\n  मूत्र-रोध का उपचार\n    वर्ति\n    अभ्यंग\n    अवगाह\n    स्वेदन\n    बस्तिकर्म\n'),
    },
    ("10", "diagram"): {
        "file": "ch5b01-udgara-10.svg",
        "alt": "Mind map: from holding back a belch six results: distaste for food, tremor, obstruction, distension, cough, hiccups",
        "type": "mermaid",
        "code": ('mindmap\n  डकार रोकने से\n    अरुचि\n    कंप\n    हृदय-छाती में विबंध\n'
                 '    आध्मान\n    कास\n    हिध्मा\n'),
    },
    ("11", "diagram"): {
        "file": "ch5b01-kshuti-11.svg",
        "alt": "Two columns: results of holding back a sneeze (head pain, weakness of senses, neck stiffness, ardita) and the means of line 2 (sharp smoke, collyrium, sniffing, nasal drops, looking at the sun)",
        "type": "split",
        "title": "श्लोक ११: छींक रोकने पर",
        "cols": [["क्या होता है", ["शिरोर्ति", "इन्द्रियदौर्बल्य", "मन्यास्तंभ", "अर्दित"]],
                 ["साधनों के नाम", ["तीक्ष्णधूम", "अंजन", "आघ्राण", "नावन", "अर्क-विलोकन"]]],
    },
}
