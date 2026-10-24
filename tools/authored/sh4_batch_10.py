from helpers import mcq, match, order, fill, multi, accepts


AUTHORED = {}

# ---------------------------------------------------------------- unit 123
AUTHORED["123"] = {
    "title": "तेन बलपौरुषस्मृतिमतिमेधाग्निवीर्य्योजांसि वर्द्धंते",
    "question": "By unit 123, what does the oil make increase, and which disorders does it make cease?",
    "rule": ("By that (the oil) strength, manly vigour, memory, understanding, intellect, digestive fire, vīrya and ojas "
             "increase (वर्धन्ते); Vāta disorders beginning with hemiplegia, convulsive disorder and facial paralysis, and "
             "gulma, hiccup, breathlessness and cough cease (निवर्तन्ते)."),
    "limits": ("The line does not call gulma, hiccup, breathlessness and cough Vāta disorders; it lists them in the same "
               "clause. तेन is the oil by the data; the oil is not named. No dose or length of use. A prose line."),
    "explain_hi": ("यह गद्य-पंक्ति बलातैल के फल बताती है; ‘तेन’ यानी उस (तेल) से। "
                   "बढ़ते हैं (वर्धन्ते): बल, पौरुष, स्मृति, मति, मेधा, अग्नि यानी पाचन-अग्नि, वीर्य और ओज। "
                   "दूर होते हैं (निवर्तन्ते): पक्षाघात (अर्धांग का लकवा), आक्षेपक (ऐंठन के दौरे), अर्दित (चेहरे का लकवा) आदि "
                   "अनेक वात-विकार, और गुल्म (पेट की गाँठ), हिध्मा (हिचकी), श्वास और कास (खाँसी)। "
                   "अन्तिम चार उसी खण्ड में गिने गए हैं; पंक्ति उन्हें वात-विकार नहीं कहती। "
                   "मात्रा या कितने दिन लेना है, यह यहाँ नहीं बताया गया।"),
    "hook": "आठ बढ़ें, वात-विकार और खाँसी-हिचकी घटें: तेन।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 123, which of these does the oil make increase?",
            ("Memory and intellect", "स्मृति and मेधा are both in the list of what increases."),
            [("Sleep and body weight", "Neither sleep nor body weight is named in unit 123."),
             ("Phlegm and body fat", "Neither is named; unit 123 lists strength, memory, ojas and others."),
             ("Thirst and sweating", "Neither thirst nor sweating is named in unit 123.")],
            "Strength, vigour, memory, understanding, intellect, digestive fire, vīrya and ojas increase.",
            "बलपौरुषस्मृतिमतिमेधाग्निवीर्योजांसि वर्धन्ते."),
        order(1, "Put these things that increase in the order of unit 123.",
              ["बल", "पौरुष", "स्मृति", "मेधा", "अग्नि", "ओजस्"],
              "Strength, manly vigour, memory, (understanding), intellect, digestive fire, (vīrya), ojas.",
              "बल → पौरुष → स्मृति → मेधा → अग्नि → ओजस्."),
        match(2, "Match each disorder of unit 123 to its modern name on the card.",
              [["पक्षाघात", "hemiplegia"], ["आक्षेपक", "convulsive disorder"], ["अर्दित", "facial paralysis"],
               ["हिध्मा", "hiccup"], ["श्वास", "breathlessness"], ["कास", "cough"]],
              "The data labels all six identifications standard.",
              "पक्षाघात, आक्षेपक, अर्दित, हिध्मा, श्वास, कास.", role="extend",
              teaches=("…आदि means 'beginning with': पक्षाघात, आक्षेपक and अर्दित head the list of Vāta disorders; "
                       "gulma, hiccup, breathlessness and cough follow in the same clause.")),
        mcq("discriminate", 3, "Which split of printed कासानिवर्त्तंते is right?",
            ("कासाः + निवर्तन्ते", "आः drops its visarga before a voiced sound: कासाः + निवर्तन्ते → कासा निवर्तन्ते."),
            [("कासः + निवर्तन्ते", "अः before a voiced sound gives ओ: that would be कासो निवर्तन्ते."),
             ("कासे + निवर्तन्ते", "A final ए stays before a consonant: that would be कासे निवर्तन्ते."),
             ("कासान् + इवर्तन्ते", "इवर्तन्ते is not a verb; the verb is निवर्तन्ते, they cease.")],
            "कासाः (coughs, the end of the compound) + निवर्तन्ते (cease).",
            "आः + voiced sound → आ (visarga dropped)."),
        multi("apply", 4, "Which statements fit unit 123 by the card?",
              [("Ojas and vīrya are among what increases", "Right: …वीर्योजांसि वर्धन्ते."),
               ("The line calls gulma and cough Vāta disorders", "They are named in the same clause; the line does not call them Vāta disorders."),
               ("Facial paralysis is among what ceases", "Right: अर्दित is in the list that ceases."),
               ("The line gives the dose of the oil", "No dose is given in unit 123.")],
              [0, 2],
              "Eight things increase; Vāta disorders and four others cease.",
              "वर्धन्ते … निवर्तन्ते."),
        mcq("transfer", 5, "By the rule of कासाः + निवर्तन्ते, how is देवाः + गच्छन्ति (the gods go) joined?",
            ("देवा गच्छन्ति", "आः drops its visarga before a voiced sound, as कासाः + निवर्तन्ते."),
            [("देवो गच्छन्ति", "ओ comes from अः before a voiced sound, not from आः."),
             ("देवार्गच्छन्ति", "र् comes from a visarga after vowels other than अ and आ."),
             ("देवाः गच्छन्ति", "Before a voiced sound आः does not keep its visarga.")],
            "देवाः + गच्छन्ति = देवा गच्छन्ति, like कासाः + निवर्तन्ते = कासा निवर्तन्ते.",
            "आः + voiced sound → आ.",
            teaches="A visarga after आ is dropped before a voiced sound: कासाः + निवर्तन्ते → कासा निवर्तन्ते."),
    ],
}

# ---------------------------------------------------------------- unit 124
AUTHORED["124"] = {
    "title": "अहरहश्चोपयुज्यमानेन षण्मासा",
    "question": "By unit 124, how is the oil used, and after how long does the swelling subside?",
    "rule": ("Used day after day (अहरहः … उपयुज्यमानेन), after six months (षण्मासात्) antravṛddhi, a swelling of the "
             "intestine (probably hernia), subsides (प्रशमम् एति). The oil is understood, not named."),
    "limits": ("Printed षण्मासा दंत्रवृद्धिः is read षण्मासाद् अन्त्रवृद्धिः, a possible re-division: no question rests on "
               "the name of the swelling. The ablative may mean after or in six months. The oil is not named in the line. "
               "A prose line."),
    "explain_hi": ("यह गद्य-पंक्ति बलातैल का एक और फल बताती है। "
                   "प्रतिदिन (अहरहः) प्रयोग किए जाने से (उपयुज्यमानेन) छह महीने बाद (षण्मासात्) अन्त्रवृद्धि, यानी सम्भवतः "
                   "हर्निया, शान्त हो जाती है (प्रशमम् एति)। "
                   "छपा ‘षण्मासा दंत्रवृद्धिः’ सम्भावित रूप से ‘षण्मासाद् अन्त्रवृद्धिः’ पढ़ा गया है (द् अगले शब्द के साथ छप गया); "
                   "इसलिए रोग के नाम पर प्रश्न नहीं। "
                   "पंचमी का अर्थ ‘छह महीने बाद’ लिया गया, ‘छह महीने में’ भी हो सकता है; तेल का नाम पंक्ति में नहीं।"),
    "hook": "रोज़ लगातार, छह महीने: सूजन शान्त।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 124, how often is it used?",
            ("Day after day", "अहरहः = day after day."),
            [("Once a month", "The unit says अहरहः, day after day."),
             ("Every third day", "No such gap is named; it is used day after day."),
             ("On alternate nights", "No such rule is named; it is used day after day.")],
            "It is used day after day.",
            "अहरहः = every day."),
        order(1, "Put the printed words of unit 124 in the line's order.",
              ["अहरहश्चोपयुज्यमानेन", "षण्मासा", "दंत्रवृद्धिः", "प्रशममेति"],
              "Day after day, being used, after six months, the swelling, subsides.",
              "अहरहश्चोपयुज्यमानेन → षण्मासा → दंत्रवृद्धिः → प्रशममेति."),
        match(2, "Match each word of unit 124 to its meaning.",
              [["अहरहः", "day after day"], ["उपयुज्यमान", "being used"], ["षण्मास", "six months"],
               ["प्रशम", "subsiding"], ["एति", "goes to, reaches"]],
              "Used day after day, after six months it reaches subsiding: it subsides.",
              "अहरहः, उपयुज्यमान, षण्मास, प्रशम, एति.", role="extend",
              teaches="प्रशमम् एति, literally 'goes to subsiding', means 'subsides'."),
        mcq("discriminate", 3, "Which split of अहरहश्चोपयुज्यमानेन is right?",
            ("अहरहः + च + उपयुज्यमानेन", "Visarga + च → श्च, and अ + उ → ओ: च + उप → चोप."),
            [("अहरहम् + च + उपयुज्यमानेन", "A final म् before च becomes ं, not श्."),
             ("अहरहे + च + उपयुज्यमानेन", "A final ए stays before च; no श् would appear."),
             ("अहरहः + चो + पयुज्यमानेन", "चो and पयुज्यमानेन are not words; the particle is च.")],
            "अहरहः (day after day) + च (and) + उपयुज्यमानेन (being used).",
            "Visarga + च → श्च; अ + उ → ओ."),
        mcq("apply", 4, "By unit 124, when does the subsiding come with daily use?",
            ("After six months", "षण्मासात्: after (or in) six months."),
            [("After six days", "The unit names months, not days: षण्मास."),
             ("After one full month", "The unit names six months, not one."),
             ("After six years", "The unit names months, not years.")],
            "With daily use, it subsides after six months.",
            "षण्मासात् = after six months."),
        mcq("transfer", 5, "By the rule of अहरहः + च, how is रामः + च (and Rāma) joined?",
            ("रामश्च", "A visarga before च becomes श्, as अहरहः + च → अहरहश्च."),
            [("रामो च", "ओ comes from अः before a voiced sound; च is not voiced."),
             ("रामर्च", "र् comes from a visarga after vowels other than अ and आ."),
             ("रामस्च", "स् comes before त or थ, not before च.")],
            "रामः + च = रामश्च, like अहरहः + च = अहरहश्च.",
            "Visarga + च → श्च.",
            teaches="A visarga before च or छ becomes श्: अहरहः + च → अहरहश्च."),
    ],
}

# ---------------------------------------------------------------- unit 125
AUTHORED["125"] = {
    "title": "वंध्याच पुत्रं गुणवंतम्",
    "question": "By unit 125, what does a barren woman obtain?",
    "rule": ("And a barren woman (वन्ध्या) obtains (लभते) a son (पुत्रम्) possessed of good qualities (गुणवन्तम्); इति "
             "closes the statement. 'As she wishes' rests on a conjectural reading."),
    "limits": ("Low confidence. Printed इच्छ्या is not a regular form; it is read इच्छया (by wish) by conjecture, or "
               "इच्छन्ती (desiring): no question rests on it. The oil is understood, not named. A prose line."),
    "explain_hi": ("यह गद्य-पंक्ति बलातैल के फलों की सूची पूरी करती है। "
                   "और वन्ध्या यानी बाँझ स्त्री गुणवान् (गुणवन्तम्) पुत्र को पाती है (लभते); ‘इति’ कथन को समाप्त करता है। "
                   "छपा ‘इच्छ्या’ नियमित रूप नहीं है; अनुमान से ‘इच्छया’ (इच्छा से) पढ़ा गया, या ‘इच्छन्ती’ (चाहती हुई) भी "
                   "सम्भव है; इस पर प्रश्न नहीं। "
                   "‘लभत’ वही ‘लभते’ है जो स्वर (इति) से पहले अ बन गया। विश्वास निम्न है।"),
    "hook": "वन्ध्या भी गुणवान् पुत्र पाती है।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 125, what does the barren woman obtain?",
            ("A son with good qualities", "पुत्रं गुणवन्तम् … लभते."),
            [("A daughter of fair looks", "The unit names a son (पुत्रम्), not a daughter."),
             ("Twin sons in one birth", "Twins are not named; one son (पुत्रम्, singular)."),
             ("A long life free of illness", "Long life is not named in unit 125.")],
            "She obtains a son possessed of good qualities.",
            "वन्ध्या पुत्रं गुणवन्तं लभते."),
        order(1, "Put the printed words of unit 125 in the line's order.",
              ["वंध्याच", "पुत्रं", "गुणवंतमिच्छ्या", "लभतइति"],
              "And a barren woman, a son, possessed of good qualities (…), obtains, thus.",
              "वंध्याच → पुत्रं → गुणवंतमिच्छ्या → लभतइति."),
        match(2, "Match each word of unit 125 to its meaning.",
              [["वन्ध्या", "barren woman"], ["पुत्र", "son"], ["गुणवत्", "possessed of good qualities"],
               ["लभते", "obtains, gets"], ["इति", "thus (closing)"]],
              "A barren woman obtains a son possessed of good qualities.",
              "वन्ध्या, पुत्र, गुणवत्, लभते, इति.", role="extend",
              teaches="गुणवत् = गुण + -वत् (possessing): possessed of good qualities; its accusative is गुणवन्तम्."),
        mcq("discriminate", 3, "Which split of printed लभतइति is right?",
            ("लभते + इति", "ए before a vowel becomes अय्; the य् is usually dropped, leaving लभत इति."),
            [("लभत + इति", "अ + इ → ए: that would give लभतेति."),
             ("लभन्ते + इति", "That would give लभन्त इति, with न्."),
             ("लभता + इति", "आ + इ → ए: that would give लभतेति.")],
            "लभते (obtains) + इति (thus): the ए becomes अ before the vowel, and a gap stays.",
            "ए + vowel (not अ) → अ(य्) + gap."),
        multi("apply", 4, "Which statements about unit 125 are right by the card?",
              [("The printed इच्छ्या is a regular form", "The data says it is not a regular form."),
               ("इति closes the statement", "Right: the closing इति marks the end."),
               ("The line names the oil", "The oil is understood, not named."),
               ("लभत is the form of लभते before a vowel", "Right: the data says so.")],
              [1, 3],
              "इति closes the statement, and लभत is लभते before a vowel.",
              "लभत इति = लभते इति."),
        mcq("transfer", 5, "By the rule of लभते + इति, how is वने + आस्ते (sits in the forest) joined?",
            ("वन आस्ते", "ए before a vowel other than अ becomes अय्, the य् usually dropped: वन आस्ते."),
            [("वनास्ते", "That is अ + आ; a final ए does not simply vanish."),
             ("वनेऽस्ते", "ऽ marks a lost short अ after ए; here आ follows."),
             ("वन्यास्ते", "य + आ comes from इ + आ, not from ए + आ.")],
            "वने + आस्ते = वन आस्ते, like लभते + इति = लभत इति.",
            "ए + vowel (not अ) → अ + gap.",
            teaches="A final ए before a vowel other than अ becomes अय्; the य् is usually dropped, leaving अ and a gap."),
    ],
}

# ---------------------------------------------------------------- unit 126
AUTHORED["126"] = {
    "title": "भवंत चात्र",
    "question": "What does the short prose formula of unit 126 do?",
    "rule": ("And on this matter there are (these): a lead-in formula to the verses that follow from unit 127. Printed "
             "भवंत is read भवन्ति."),
    "limits": ("The noun (what there are) is not printed and not supplied. Printed भवंत is read भवन्ति, a possible correction "
               "(ta for ti): no question rests on the verb's form. The formula teaches nothing of its own. A prose line."),
    "explain_hi": ("‘भवन्ति चात्र’ एक जाना-पहचाना सूत्र-वाक्य है: और इस विषय में ये हैं। "
                   "क्या हैं, यह संज्ञा छपी नहीं, और जोड़ी भी नहीं गई। "
                   "यह आगे के श्लोकों (इकाई १२७ से) की भूमिका है। "
                   "छपा ‘भवंत’ सम्भवतः छपाई की भूल है; ‘भवन्ति’ पढ़ा गया। ‘चात्र’ = च + अत्र।"),
    "hook": "भवन्ति चात्र: अब श्लोक आते हैं।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 126, what does this line do?",
            ("It leads in to the verses after it", "भवन्ति चात्र: and on this there are (these)."),
            [("It names the oil's main use", "No use is named in unit 126."),
             ("It closes the whole chapter", "The colophon comes in unit 135."),
             ("It gives a new remedy for the woman", "No remedy is named in unit 126.")],
            "A standard lead-in formula: and on this matter there are these.",
            "भवन्ति चात्र = lead-in formula."),
        mcq("warmup", 1, "Which split of चात्र is right?",
            ("च + अत्र", "अ + अ → आ: च + अत्र → चात्र."),
            [("चा + त्र", "Neither चा nor त्र is a word here."),
             ("चे + अत्र", "ए + अ would give चेऽत्र."),
             ("च + त्र", "That would be written चत्र, with no आ.")],
            "च (and) + अत्र (here, in this matter).",
            "अ + अ → आ."),
        fill(2, "In unit 126 the word for here, in this matter is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("अत्र"),
             "चात्र = च + अत्र; अत्र = here, in this matter.",
             "अत्र means here; in a text, in this matter.",
             "अत्र = here."),
        mcq("discriminate", 3, "How does unit 126 differ from the units right after it?",
            ("It is a short prose formula", "Unit 126 is prose; units 127 to 134 are verses."),
            [("It is a verse in anuṣṭubh", "The data marks unit 126 as prose, not a verse."),
             ("It is the colophon of the chapter", "The colophon is unit 135."),
             ("It is a list of drugs and doses", "No drug or dose is named in unit 126.")],
            "Unit 126 is a prose lead-in; the verses follow.",
            "भवन्ति चात्र: prose formula before verses."),
        multi("apply", 4, "Which statements about unit 126 are right by the card?",
              [("The noun after भवन्ति is printed", "It is not printed and not supplied."),
               ("The verses it leads in to begin at unit 127", "Right: it introduces the verses that follow."),
               ("It is a standard lead-in formula", "Right: and on this matter there are (these)."),
               ("It teaches a remedy of its own", "It teaches nothing of its own.")],
              [1, 2],
              "A standard lead-in to the verses from unit 127.",
              "भवन्ति चात्र."),
        mcq("transfer", 5, "By the rule of च + अत्र → चात्र, how is तत्र + अपि (even there) joined?",
            ("तत्रापि", "अ + अ → आ, as च + अत्र → चात्र."),
            [("तत्रेपि", "अ + अ does not give ए."),
             ("तत्रोऽपि", "ओऽ comes from अः + अ, not from अ + अ."),
             ("तत्र्यपि", "य comes from इ before a vowel, not from अ.")],
            "तत्र + अपि = तत्रापि, like च + अत्र = चात्र.",
            "अ + अ → आ.",
            teaches="A final अ and an initial अ merge into one long आ: च + अत्र → चात्र."),
    ],
}

# ---------------------------------------------------------------- unit 127
AUTHORED["127"] = {
    "title": "बस्तिद्वारे विपन्नायाः कुक्षिः प्रस्पंदते यदि",
    "question": "By verse 127, what should be done if the belly of a woman who has perished quivers at the time of birth?",
    "rule": ("If the belly (कुक्षि) of a woman who has perished (विपन्ना) at the bastidvāra quivers (प्रस्पन्दते) at the "
             "time of birth, then quickly (शीघ्रम्), having split (it) open, one should take out the child."),
    "limits": ("Bastidvāra is not explained (bladder-region opening or pelvic outlet): no question on it. Vipanna is "
               "ruined or dead; death is suggested, not stated. Kukṣi is the belly, not specifically the womb. The object "
               "of 'split open' is not stated."),
    "explain_hi": ("यह श्लोक मृत-सी माता से शिशु निकालने की बात कहता है। "
                   "यदि बस्तिद्वार पर विपन्न हुई स्त्री की कुक्षि यानी पेट फड़के (प्रस्पन्दते), जन्म के समय, तो तब शीघ्र "
                   "चीरकर (पाटयित्वा) शिशु को निकाले (उद्धरेत्)। "
                   "‘विपन्न’ = नष्ट या मृत; प्रसंग मृत्यु की ओर संकेत करता है, पर श्लोक यह स्पष्ट नहीं कहता। "
                   "‘बस्तिद्वार’ का अर्थ नहीं बताया गया; किसे चीरना है, वह (पेट) भी छपा नहीं। "
                   "यह वाक्य दो पंक्तियों में पूरा होता है।"),
    "hook": "पेट फड़के तो देर नहीं: शीघ्र चीरकर शिशु निकालो।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By verse 127, what is the sign that calls for quick action?",
            ("Her belly quivers", "कुक्षिः प्रस्पन्दते यदि: if the belly quivers."),
            [("Her belly grows cold", "Coldness is not named in verse 127."),
             ("Blood flows from her", "Bleeding is not named in verse 127."),
             ("Her breathing stops", "Breathing is not named in verse 127.")],
            "If the belly quivers, the child is taken out quickly.",
            "कुक्षिः प्रस्पन्दते यदि."),
        order(1, "Put these phrases of verse 127 in the verse's order.",
              ["बस्तिद्वारे", "विपन्नायाः", "कुक्षिः प्रस्पंदते यदि", "जन्मकाले", "ततः शीघ्रं", "पाटयित्वोद्धरेच्छिशुं"],
              "At the bastidvāra, of her who has perished, if the belly quivers, at the time of birth, then quickly, having split (it) open, one should take out the child.",
              "बस्तिद्वारे → विपन्नायाः → कुक्षिः प्रस्पंदते यदि → जन्मकाले → ततः शीघ्रं → पाटयित्वोद्धरेच्छिशुं."),
        match(2, "Match each word of verse 127 to its meaning.",
              [["कुक्षि", "belly"], ["प्रस्पन्दते", "quivers, throbs"], ["यदि", "if"], ["शीघ्रम्", "quickly"],
               ["पाटयित्वा", "having split open"], ["उद्धरेत्", "should take out"]],
              "If the belly quivers, then quickly, having split (it) open, one should take out the child.",
              "कुक्षि, प्रस्पन्दते, यदि, शीघ्रम्, पाटयित्वा, उद्धरेत्.", role="extend",
              teaches="यदि … ततः = if … then: the condition comes first, the action after ततः."),
        mcq("discriminate", 3, "Which split of उद्धरेच्छिशुम् is right?",
            ("उद्धरेत् + शिशुम्", "त् before श becomes च्, and the श usually becomes छ: उद्धरेच्छिशुम्."),
            [("उद्धरेः + शिशुम्", "A visarga before श stays or becomes श्; it never gives च्छ."),
             ("उद्धरेम् + शिशुम्", "A final म् before a consonant becomes ं: उद्धरें शिशुम्."),
             ("उद्धरेच् + छिशुम्", "छिशुम् is not a word; the word is शिशुम्, the child.")],
            "उद्धरेत् (should take out) + शिशुम् (the child).",
            "त् + श → च्छ (usual written form)."),
        multi("apply", 4, "Which statements about verse 127 are right by the card?",
              [("The verse says plainly that she has died", "Vipanna means ruined or dead; the verse does not say death plainly."),
               ("The verse explains what bastidvāra is", "It is not explained; it is read literally."),
               ("The action is to be done quickly", "Right: ततः शीघ्रम्."),
               ("The child is taken out after splitting (it) open", "Right: पाटयित्वा उद्धरेत् शिशुम्.")],
              [2, 3],
              "Quickly, having split (it) open, one should take out the child.",
              "ततः शीघ्रं पाटयित्वा उद्धरेत् शिशुम्."),
        mcq("transfer", 5, "By the pattern of पाटयित्वा उद्धरेत्, what does गत्वा mean in गत्वा पश्येत् (a new example)?",
            ("having gone", "-त्वा marks an action done before the main verb, as पाटयित्वा, having split open."),
            [("while going", "While going would be a present participle such as गच्छन्."),
             ("in order to go", "In order to go would be the infinitive गन्तुम्."),
             ("he went", "He went would be a past finite verb such as अगच्छत्.")],
            "गत्वा पश्येत् = having gone, he should see; like पाटयित्वा उद्धरेत्.",
            "-त्वा = having done (before the main verb).",
            teaches="An absolutive in -त्वा names an action finished before the main verb: पाटयित्वा उद्धरेत्."),
    ],
}

# ---------------------------------------------------------------- unit 128
AUTHORED["128"] = {
    "title": "मधुकं शाकबीजं च पयस्या सुरदारु च",
    "question": "By verse 128, which drugs make up the first two of the seven combinations?",
    "rule": ("First combination: madhuka (licorice, probable), the seed of śāka (teak, probable), payasyā (disputed), "
             "suradāru (deodar, probable). Second: aśmantaka (disputed), black sesame, tāmravallī (unidentified), "
             "śatāvarī (wild asparagus). Each fills a half-verse."),
    "limits": ("No verb here: 'with milk' comes in unit 131 and 'one should apply … in the seven months' in unit 132. "
               "Payasyā and aśmantaka are disputed and tāmravallī unidentified: no question asks their identity. Śāka may "
               "also mean a vegetable. No dose is given."),
    "explain_hi": ("यह श्लोक सात योगों की शृंखला खोलता है; हर आधा श्लोक एक योग है। "
                   "पहला योग: मधुक (सम्भवतः मुलेठी), शाक (सम्भवतः सागौन) का बीज, पयस्या (पहचान विवादित) और सुरदारु "
                   "(सम्भवतः देवदार)। "
                   "दूसरा योग: अश्मन्तक (पहचान विवादित), काले तिल, ताम्रवल्ली (पहचान अज्ञात) और शतावरी। "
                   "ये दूध के साथ (इकाई १३१) सात महीनों में क्रम से (इकाई १३२) दिए जाते हैं; क्रिया वहीं है। "
                   "कोई मात्रा नहीं दी गई।"),
    "hook": "पहला: मधुक-शाकबीज-पयस्या-सुरदारु; दूसरा: अश्मन्तक-तिल-ताम्रवल्ली-शतावरी।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By verse 128 and its note, what does each half-verse of this passage give?",
            ("One combination of drugs", "Each half-verse is one combination (yoga) of the seven."),
            [("A dose in measured parts", "No measure or dose is given in verse 128."),
             ("A sign of a dead fetus", "No sign is named; only drugs are listed."),
             ("A step of the delivery", "No step of delivery is named in verse 128.")],
            "Line 1 is the first combination, line 2 the second.",
            "One half-verse = one combination."),
        order(1, "Put these drugs of verse 128 in the verse's order.",
              ["मधुकं", "शाकबीजं", "सुरदारु", "अश्मंतकः", "कृष्णतिलाः", "शतावरी"],
              "Madhuka, śāka seed, (payasyā), suradāru; aśmantaka, black sesame, (tāmravallī), śatāvarī.",
              "मधुकं → शाकबीजं → सुरदारु → अश्मंतकः → कृष्णतिलाः → शतावरी."),
        match(2, "Match each drug of verse 128 to the card's identification.",
              [["मधुक", "licorice (probable)"], ["सुरदारु", "deodar (probable)"], ["कृष्णतिल", "black sesame (standard)"],
               ["शतावरी", "wild asparagus"], ["ताम्रवल्ली", "copper creeper (unidentified)"]],
              "The labels are the data's: probable, standard or unidentified.",
              "मधुक, सुरदारु, कृष्णतिल, शतावरी, ताम्रवल्ली.", role="extend",
              teaches="Suradāru and devadāru are two names of deodar (probable)."),
        mcq("discriminate", 3, "Which split of कृष्णतिलास्ताम्रवल्ली is right?",
            ("कृष्णतिलाः + ताम्रवल्ली", "A visarga before त becomes स्: कृष्णतिलास्ताम्रवल्ली."),
            [("कृष्णतिलान् + ताम्रवल्ली", "न् before त gives ंस्त: that would be कृष्णतिलांस्ताम्रवल्ली."),
             ("कृष्णतिला + स्ताम्रवल्ली", "स्ताम्रवल्ली is not a word; the drug is ताम्रवल्ली."),
             ("कृष्णतिलम् + ताम्रवल्ली", "A final म् before a consonant becomes ं: कृष्णतिलं ताम्रवल्ली.")],
            "कृष्णतिलाः (black sesame seeds) + ताम्रवल्ली (copper creeper).",
            "Visarga + त → स्त."),
        mcq("apply", 4, "Which drug of verse 128 belongs to the second combination?",
            ("शतावरी", "Line 2 is the second combination: अश्मन्तक, कृष्णतिल, ताम्रवल्ली, शतावरी."),
            [("मधुकम्", "Madhuka is in line 1, the first combination."),
             ("सुरदारु", "Suradāru is in line 1, the first combination."),
             ("शाकबीजम्", "The śāka seed is in line 1, the first combination.")],
            "Śatāvarī closes line 2, the second combination.",
            "Line 1 = first combination; line 2 = second."),
        mcq("transfer", 5, "By the rule of कृष्णतिलाः + ताम्रवल्ली, how is बालः + तिष्ठति (the boy stands) joined?",
            ("बालस्तिष्ठति", "A visarga before त becomes स्, as in कृष्णतिलास्ताम्रवल्ली."),
            [("बालो तिष्ठति", "ओ comes from अः before a voiced sound; त is not voiced."),
             ("बालश्तिष्ठति", "श् comes before च, छ or श, not before त."),
             ("बालर्तिष्ठति", "र् comes after vowels other than अ and आ, before a voiced sound.")],
            "बालः + तिष्ठति = बालस्तिष्ठति, like कृष्णतिलाः + ताम्रवल्ली.",
            "Visarga + त → स्त.",
            teaches="A visarga before त or थ becomes स्: कृष्णतिलाः + ताम्रवल्ली → कृष्णतिलास्ताम्रवल्ली."),
    ],
}

# ---------------------------------------------------------------- unit 129
AUTHORED["129"] = {
    "title": "वृक्षदनी पयस्या च लता सोत्पलसारिबा",
    "question": "By verse 129, which drugs make up the third and fourth combinations?",
    "rule": ("Third: vṛkṣadanī (mistletoe vandā, probable), payasyā (disputed), latā (a creeper, unclear), sārivā with utpala "
             "(blue water lily, probable). Fourth: anantā (disputed), sārivā, rāsnā (conjectural, disputed), padmā (unclear), "
             "madhuyaṣṭikā (licorice, standard)."),
    "limits": ("The division latā | sotpalasārivā is chosen; latā sotpalā | sārivā is the alternative: no question rests on "
               "it. Printed रास्त्रा is read rāsnā by conjecture: no question on it. Payasyā and anantā are disputed; latā and "
               "padmā unclear. No verb or dose here."),
    "explain_hi": ("यह श्लोक तीसरा और चौथा योग देता है। "
                   "तीसरा: वृक्षदनी (सम्भवतः बांदा), पयस्या (पहचान विवादित), लता (कोई बेल, पहचान अस्पष्ट) और उत्पल "
                   "(सम्भवतः नीलकमल) सहित सारिवा। "
                   "चौथा: अनन्ता (विवादित), सारिवा, रास्ना (छपा ‘रास्त्रा’, अनुमानित पाठ; पहचान विवादित), पद्मा (अस्पष्ट) और "
                   "मधुयष्टिका यानी मुलेठी। "
                   "‘लता | सोत्पलसारिवा’ का विभाग चुना गया है; ‘लता सोत्पला | सारिवा’ भी सम्भव है। "
                   "अनन्ता और सारिवा दोनों गिने गए हैं, इसलिए यहाँ अलग द्रव्य माने गए।"),
    "hook": "तीसरा: वृक्षदनी-पयस्या-लता-सारिवा; चौथा: अनन्ता-सारिवा-रास्ना-पद्मा-मुलेठी।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By verse 129, which drug is named in both of its lines?",
            ("सारिवा", "Line 1 has सोत्पलसारिबा (sārivā with utpala); line 2 has सारिवा."),
            [("मधुयष्टिका", "Madhuyaṣṭikā is only in line 2."),
             ("वृक्षदनी", "Vṛkṣadanī is only in line 1."),
             ("पद्मा", "Padmā is only in line 2.")],
            "Sārivā stands in both the third and the fourth combination.",
            "सोत्पलसारिबा … सारिवा."),
        order(1, "Put these printed words of verse 129 in the verse's order.",
              ["वृक्षदनी", "पयस्या", "सोत्पलसारिबा", "अनंता", "पद्मा", "मधुयष्टिका"],
              "Vṛkṣadanī, payasyā, (latā), sārivā with utpala; anantā, (sārivā, rāsnā), padmā, madhuyaṣṭikā.",
              "वृक्षदनी → पयस्या → सोत्पलसारिबा → अनंता → पद्मा → मधुयष्टिका."),
        match(2, "Match each drug of verse 129 to the card's identification.",
              [["मधुयष्टिका", "licorice (standard)"], ["उत्पल", "blue water lily (probable)"],
               ["वृक्षदनी", "mistletoe vandā (probable)"], ["सारिवा", "Indian sarsaparilla"],
               ["अनन्ता", "identity disputed"]],
              "The labels are the data's: standard, probable or disputed.",
              "मधुयष्टिका, उत्पल, वृक्षदनी, सारिवा, अनन्ता.", role="extend",
              teaches="स- before a noun means 'with': सोत्पल = स + उत्पल, with utpala."),
        mcq("discriminate", 3, "Which split of सोत्पल is right?",
            ("स + उत्पल", "अ + उ → ओ: स + उत्पल → सोत्पल."),
            [("सः + उत्पल", "अः before a vowel other than अ drops the visarga with a gap: स उत्पल."),
             ("सम् + उत्पल", "A final म् before a vowel joins it: समुत्पल."),
             ("सो + त्पल", "त्पल is not a word; the flower is उत्पल.")],
            "स (with) + उत्पल (blue water lily): अ + उ → ओ.",
            "अ + उ → ओ."),
        mcq("apply", 4, "Anantā and sārivā both stand in line 2 of verse 129. How does the card take them here?",
            ("As two separate drugs", "Both are listed, so they are taken as separate drugs here."),
            [("As one drug named twice", "The note takes them as separate here, since both are listed."),
             ("As a verb and its object", "Both are feminine nouns in the nominative, not a verb."),
             ("As one compound drug name", "They are printed as two separate words.")],
            "Anantā and sārivā are taken as two separate drugs here.",
            "Both listed → separate drugs."),
        mcq("transfer", 5, "By the rule of स + उत्पल → सोत्पल, how is सूर्य + उदयः (sunrise) joined?",
            ("सूर्योदयः", "अ + उ → ओ, as स + उत्पल → सोत्पल."),
            [("सूर्यौदयः", "औ comes from अ + ओ or औ, not from अ + उ."),
             ("सूर्युदयः", "The अ does not drop; अ and उ merge into ओ."),
             ("सूर्यादयः", "आ comes from अ + अ, not from अ + उ.")],
            "सूर्य + उदयः = सूर्योदयः, like स + उत्पल = सोत्पल.",
            "अ + उ → ओ.",
            teaches="A final अ and an initial उ merge into ओ: स + उत्पल → सोत्पल."),
    ],
}

# ---------------------------------------------------------------- unit 130
AUTHORED["130"] = {
    "title": "बृहतीद्वयकाश्मर्य्यक्षीरिशुंगत्वचो घृतं",
    "question": "By verse 130, which drugs make up the fifth and sixth combinations?",
    "rule": ("Fifth: the two bṛhatīs (large and small nightshade, probable), kāśmarya (gambhārī), the bark of the shoots of "
             "milk-yielding trees, and ghee. Sixth: pṛśniparṇī, balā, śigru, śvadaṃṣṭrā (puncture-vine, probable), "
             "madhuparṇikā (disputed)."),
    "limits": ("Kṣīri-śuṅga-tvacaḥ may also be read as three items (milk-yielding trees, shoots, bark); the trees are not "
               "named: no question asks which. Madhuparṇikā is disputed; śvadaṃṣṭrā has also been taken as kaṇṭakārī. No "
               "verb or dose here."),
    "explain_hi": ("यह श्लोक पाँचवाँ और छठा योग देता है। "
                   "पाँचवाँ: बृहतीद्वय यानी दोनों बृहती (सम्भवतः बड़ी और छोटी कटेरी), काश्मर्य यानी गम्भारी, क्षीरी "
                   "(दूधवाले) वृक्षों की कोंपलों की छाल, और घी। "
                   "छठा: पृश्निपर्णी (पिठवन), बला (बरियार), शिग्रु (सहजन), श्वदंष्ट्रा (सम्भवतः गोखरू) और मधुपर्णिका "
                   "(पहचान विवादित, सम्भवतः गिलोय)। "
                   "‘क्षीरिशुंगत्वचः’ को तीन अलग द्रव्य भी पढ़ा जा सकता है; क्षीरी वृक्षों के नाम यहाँ नहीं हैं।"),
    "hook": "पाँचवें में घी, छठे में सहजन-गोखरू।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By verse 130, which fat is named in the fifth combination?",
            ("Ghee (घृत)", "घृतम् closes line 1, the fifth combination."),
            [("Oil (तैल)", "No oil is named in verse 130."),
             ("Marrow (मज्जा)", "No marrow is named in verse 130."),
             ("Butter (नवनीत)", "No butter is named in verse 130.")],
            "Ghee is part of the fifth combination.",
            "…त्वचो घृतम्."),
        order(1, "Put the drugs of line 2 of verse 130 in the verse's order.",
              ["पृश्निपर्णी", "बला", "शिग्रुः", "श्वदंष्ट्रा", "मधुपर्णिका"],
              "Pṛśniparṇī, balā, śigru, śvadaṃṣṭrā, madhuparṇikā: the sixth combination.",
              "पृश्निपर्णी → बला → शिग्रुः → श्वदंष्ट्रा → मधुपर्णिका."),
        match(2, "Match each drug of verse 130 to the card's identification.",
              [["पृश्निपर्णी", "pithvan (standard)"], ["शिग्रु", "drumstick tree (standard)"],
               ["काश्मर्य", "gambhārī (standard)"], ["श्वदंष्ट्रा", "puncture-vine (probable)"], ["बला", "country mallow"]],
              "The labels are the data's: standard or probable.",
              "पृश्निपर्णी, शिग्रु, काश्मर्य, श्वदंष्ट्रा, बला.", role="extend",
              teaches="Kāśmarya is another name of gambhārī (standard)."),
        mcq("discriminate", 3, "In बृहतीद्वय, what does द्वय add?",
            ("A pair: the two bṛhatīs", "द्वय = a pair: bṛhatī and kaṇṭakārī (probable)."),
            [("A double dose of bṛhatī", "द्वय counts the plants, not doses; no dose is given."),
             ("Two parts of one bṛhatī plant", "The data reads two plants, not two parts of one."),
             ("A use in the second month", "द्वय means a pair; no month is named here.")],
            "बृहतीद्वय = the two bṛhatīs, large and small nightshade (probable).",
            "-द्वय = a pair of."),
        multi("apply", 4, "Which statements about verse 130 are right by the card?",
              [("Ghee belongs to the fifth combination", "Right: घृतम् is in line 1."),
               ("The milk-yielding trees are named in verse 130", "They are not named here."),
               ("Madhuparṇikā is a standard identification", "The data calls madhuparṇikā disputed."),
               ("Kṣīri-śuṅga-tvacaḥ can be read two ways", "Right: bark of the shoots, or three items.")],
              [0, 3],
              "Ghee is in the fifth combination; the kṣīri compound is read two ways.",
              "बृहतीद्वय… घृतम् = fifth; पृश्निपर्णी… = sixth."),
        mcq("transfer", 5, "By the pattern of बृहतीद्वय, what does नेत्रद्वय (a new example) mean?",
            ("The two eyes", "-द्वय = a pair: नेत्रद्वय = the two eyes."),
            [("The second eye", "The second would be द्वितीय, not द्वय."),
             ("An eye treated twice", "द्वय names a pair of things, not a repetition."),
             ("Two kinds of eye salve", "No salve is in the word; नेत्र = eye.")],
            "नेत्रद्वय = the pair of eyes, like बृहतीद्वय = the two bṛhatīs.",
            "X-द्वय = the pair of X.",
            teaches="-द्वय after a noun means 'the pair of': बृहतीद्वय = the two bṛhatīs."),
    ],
}

# ---------------------------------------------------------------- unit 131
AUTHORED["131"] = {
    "title": "शृंगाटकं बिसं द्राक्षा कसेरु मधुकं सिता",
    "question": "By verse 131, what is the seventh combination, and how are all the combinations taken?",
    "rule": ("Seventh: water chestnut, lotus stalk, grape, kaseru (sedge tuber, probable), madhuka (licorice, probable), "
             "sitā (white sugar, probable). All these combinations (योगान्) with milk (पयसा), each ending at a half-verse."),
    "limits": ("The sentence runs on into unit 132, which gives the verb (one should apply) and the months; this unit has no "
               "verb. No dose or quantity of milk is given. Printed सर्वैतान् is read सर्वान् एतान् by the data; no question "
               "rests on that join."),
    "explain_hi": ("यह श्लोक सातवाँ योग देता है और फिर सबको जोड़ता है। "
                   "सातवाँ: शृंगाटक (सिंघाड़ा), बिस (कमलनाल), द्राक्षा (अंगूर), कसेरु (सम्भवतः कसेरू कन्द), मधुक "
                   "(सम्भवतः मुलेठी) और सिता (सम्भवतः मिश्री)। "
                   "दूसरी पंक्ति: ये सभी योग दूध के साथ (पयसा), जो आधे श्लोक पर समाप्त होते हैं (अर्धश्लोकसमापनान्)। "
                   "क्रिया ‘योजयेत्’ अगली इकाई (१३२) में है; वाक्य वहीं पूरा होता है।"),
    "hook": "सात योग, हर एक आधा श्लोक, सब दूध के साथ।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By verse 131, with what are all these combinations taken?",
            ("With milk", "सर्वैतान् पयसा योगान्: all these combinations with milk."),
            [("With honey", "Honey is not named in verse 131."),
             ("With water", "Water is not named; पयसा means with milk."),
             ("With sour gruel", "Gruel is not named in verse 131.")],
            "All the combinations are taken with milk (पयसा).",
            "पयसा = with milk."),
        order(1, "Put the drugs of line 1 of verse 131 in the verse's order.",
              ["शृंगाटकं", "बिसं", "द्राक्षा", "कसेरु", "मधुकं", "सिता"],
              "Water chestnut, lotus stalk, grape, kaseru, madhuka, sitā: the seventh combination.",
              "शृंगाटकं → बिसं → द्राक्षा → कसेरु → मधुकं → सिता."),
        match(2, "Match each drug of verse 131 to the card's identification.",
              [["शृङ्गाटक", "water chestnut (standard)"], ["बिस", "lotus stalk (standard)"], ["द्राक्षा", "grape (standard)"],
               ["कसेरु", "sedge tuber (probable)"], ["सिता", "white sugar (probable)"]],
              "The labels are the data's: standard or probable.",
              "शृङ्गाटक, बिस, द्राक्षा, कसेरु, सिता.", role="extend",
              teaches="सिता literally means 'white'; in drug lists it is usually sugar (probable)."),
        mcq("discriminate", 3, "Which split of योगानर्ध (in योगानर्द्धश्लोकसमापनान्) is right?",
            ("योगान् + अर्ध", "A final न् after a long vowel joins the next vowel unchanged: योगानर्ध."),
            [("योगाः + अर्ध", "आः before a vowel drops the visarga and leaves a gap: योगा अर्ध."),
             ("योगानि + अर्ध", "इ before अ becomes य्: that would give योगान्यर्ध."),
             ("योगम् + अर्ध", "That would give योगमर्ध, with म.")],
            "योगान् (combinations, accusative plural) + अर्धश्लोकसमापनान् (ending at a half-verse).",
            "Final न् (after a long vowel) + vowel → न + vowel."),
        mcq("apply", 4, "What does अर्धश्लोकसमापन tell about each combination?",
            ("Each is complete within a half-verse", "Each combination fills one half-verse (units 128 to 131)."),
            [("Each is taken for half a month", "No half-month is named; श्लोक is a verse."),
             ("Each is given at half the usual dose", "No dose is given; अर्धश्लोक is a half-verse."),
             ("Each closes the chapter's verses", "The chapter closes in unit 135, a colophon.")],
            "Ardhaśloka-samāpana = ending at a half-verse: one combination per half-verse.",
            "अर्धश्लोक = half-verse."),
        mcq("transfer", 5, "By the rule of योगान् + अर्ध, how is देवान् + अर्चति (worships the gods) joined?",
            ("देवानर्चति", "A final न् after a long vowel joins the next vowel unchanged, as योगान् + अर्ध."),
            [("देवाननर्चति", "न् doubles before a vowel only after a short vowel; here आ is long."),
             ("देवा अर्चति", "That is how आः would join before a vowel, not आन्."),
             ("देवामर्चति", "A final न् does not turn into म् before a vowel.")],
            "देवान् + अर्चति = देवानर्चति, like योगान् + अर्ध = योगानर्ध.",
            "आन् + vowel → आन + vowel.",
            teaches="A final न् after a long vowel simply joins a following vowel: योगान् + अर्ध → योगानर्ध."),
    ],
}

# ---------------------------------------------------------------- unit 132
AUTHORED["132"] = {
    "title": "क्रमात्सप्तसु मासेषु गर्भे स्रवति योजयेत्",
    "question": "By verse 132, when are the seven combinations applied, and which plants does its second line name?",
    "rule": ("In sequence (क्रमात्), in the seven months, when the fetus is flowing (गर्भे स्रवति, probably miscarriage), one "
             "should apply (योजयेत्) (them): seven combinations for seven months. Line 2 names six plants whose roots come "
             "in unit 133."),
    "limits": ("Line 2 runs on into unit 133 (with the roots of these); its printed final -न् is read as a misprint "
               "(possible): no question on its case. 'Flowing' is probably miscarriage (garbhasrāva). No dose is given."),
    "explain_hi": ("यह श्लोक पिछले सात योगों की क्रिया देता है। "
                   "क्रम से (क्रमात्) सात महीनों में, गर्भ के बहने पर (गर्भे स्रवति, सम्भवतः गर्भस्राव), (उन्हें) प्रयोग करे "
                   "(योजयेत्); सात योग, सात महीने। "
                   "‘गर्भे स्रवति’ सति-सप्तमी है: गर्भ के बहते हुए। "
                   "दूसरी पंक्ति छह वनस्पतियाँ गिनाती है: कपित्थ (कैथ), बिल्व (बेल), बृहती (बड़ी कटेरी), पटोल (परवल), इक्षु "
                   "(ईख) और निदिग्धिका (कटेरी); इनकी जड़ों की बात अगली इकाई (१३३) में है। "
                   "छपे अन्तिम ‘न्’ को सम्भवतः छपाई की भूल माना गया।"),
    "hook": "सात महीने, सात योग, क्रम से।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By verse 132, in which months are the combinations applied?",
            ("In the seven months, in sequence", "क्रमात् सप्तसु मासेषु: in sequence, in the seven months."),
            [("Only in the very first month", "The verse names seven months, in sequence."),
             ("In the ninth and tenth months", "These months come later, with other milks (units 133, 134)."),
             ("In any month, all at once", "The verse says क्रमात्, in sequence, not all at once.")],
            "Seven combinations, applied in sequence over seven months.",
            "क्रमात् सप्तसु मासेषु योजयेत्."),
        order(1, "Put the plants of line 2 of verse 132 in the verse's order.",
              ["कपित्थ", "बिल्व", "बृहती", "पटोल", "इक्षु", "निदिग्धिका"],
              "Kapittha, bilva, bṛhatī, paṭola, ikṣu, nidigdhikā.",
              "कपित्थ → बिल्व → बृहती → पटोल → इक्षु → निदिग्धिका."),
        match(2, "Match each plant of verse 132 to the card's identification.",
              [["कपित्थ", "wood-apple"], ["बिल्व", "bael"], ["पटोल", "pointed gourd"], ["इक्षु", "sugarcane"],
               ["निदिग्धिका", "small nightshade"]],
              "All five identifications are standard in the data.",
              "कपित्थ, बिल्व, पटोल, इक्षु, निदिग्धिका.", role="extend",
              teaches="Bṛhatī and nidigdhikā are the large and small nightshades (standard)."),
        mcq("discriminate", 3, "Which split of पटोलेक्षु is right?",
            ("पटोल + इक्षु", "अ + इ → ए: पटोल + इक्षु → पटोलेक्षु."),
            [("पटोलम् + इक्षु", "A final म् before a vowel joins it: पटोलमिक्षु."),
             ("पटोलः + इक्षु", "अः before a vowel other than अ drops the visarga with a gap: पटोल इक्षु."),
             ("पटोले + क्षु", "क्षु is not a word; the plant is इक्षु, sugarcane.")],
            "पटोल (pointed gourd) + इक्षु (sugarcane): अ + इ → ए.",
            "अ + इ → ए."),
        mcq("apply", 4, "What does गर्भे स्रवति describe in verse 132?",
            ("The fetus flowing, probably miscarriage", "A locative absolute: with the fetus flowing (garbhasrāva, probable)."),
            [("The fetus turned the wrong way", "No turning is named in verse 132."),
             ("A woman past her tenth month", "No tenth month is named in verse 132."),
             ("The fetus growing too fast", "No growth is named in verse 132.")],
            "When the fetus is flowing, probably miscarriage, one should apply the combinations.",
            "गर्भे स्रवति = when the fetus flows."),
        mcq("transfer", 5, "By the rule of पटोल + इक्षु → पटोलेक्षु, how is गज + इन्द्रः (lord of elephants) joined?",
            ("गजेन्द्रः", "अ + इ → ए, as पटोल + इक्षु → पटोलेक्षु."),
            [("गजैन्द्रः", "ऐ comes from अ + ए or ऐ, not from अ + इ."),
             ("गजीन्द्रः", "The अ does not drop; अ and इ merge into ए."),
             ("गज्येन्द्रः", "य comes from इ before a vowel, not from अ.")],
            "गज + इन्द्रः = गजेन्द्रः, like पटोल + इक्षु = पटोलेक्षु.",
            "अ + इ → ए.",
            teaches="A final अ and an initial इ merge into ए: पटोल + इक्षु → पटोलेक्षु."),
    ],
}

# ---------------------------------------------------------------- unit 133
AUTHORED["133"] = {
    "title": "मूलैः शृतं प्रयुंजीत क्षीरं",
    "question": "By verse 133, what milk is used, and with which drugs in the ninth month?",
    "rule": ("One should use milk boiled with the roots (मूलैः शृतं क्षीरम्) of the plants just named, in the month, and "
             "likewise in the eighth; in the ninth, with sārivā, anantā (disputed), payasyā (disputed) and madhuyaṣṭī (licorice)."),
    "limits": ("Low confidence. मासे has no ordinal (a lost number, or 'for a month'): no question on which month. "
               "Line 2 has no verb or noun: 'should apply' comes in unit 134, the milk is understood. The roots are those "
               "of unit 132's plants. No dose."),
    "explain_hi": ("यह श्लोक दूध के आगे के प्रयोग देता है। "
                   "(पिछली इकाई की वनस्पतियों की) जड़ों से उबाला दूध (मूलैः शृतं क्षीरम्) ‘मासे’ में प्रयोग करे, और उसी प्रकार "
                   "आठवें में। "
                   "‘मासे’ के साथ क्रम-संख्या नहीं है: कोई संख्या छूट गई हो या ‘एक महीने तक’ अर्थ हो; यह तय नहीं। "
                   "नवें में: सारिवा, अनन्ता (विवादित), पयस्या (विवादित) और मधुयष्टि (मुलेठी) के साथ; यहाँ क्रिया नहीं, वह "
                   "इकाई १३४ में ‘योजयेत्’ है। विश्वास निम्न है।"),
    "hook": "जड़ों का दूध, फिर आठवाँ; नौवें में सारिवा-मुलेठी।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By verse 133, what is boiled with the roots?",
            ("Milk", "मूलैः शृतं … क्षीरम्: milk boiled with roots."),
            [("Oil", "No oil is named in verse 133."),
             ("Water", "No water is named in verse 133."),
             ("Ghee", "No ghee is named in verse 133.")],
            "Milk is boiled with the roots.",
            "मूलैः शृतं क्षीरम्."),
        order(1, "Put the ninth-month drugs of verse 133 in the verse's order.",
              ["सारिवा", "अनन्ता", "पयस्या", "मधुयष्टि"],
              "Sārivā, anantā, payasyā, madhuyaṣṭī.",
              "सारिवा → अनन्ता → पयस्या → मधुयष्टि."),
        match(2, "Match each word of verse 133 to its meaning.",
              [["मूल", "root"], ["शृत", "boiled"], ["प्रयुञ्जीत", "one should use"], ["क्षीर", "milk"],
               ["अष्टम", "eighth"], ["नवम", "ninth"]],
              "Milk boiled with roots is used; likewise in the eighth; in the ninth with four drugs.",
              "मूल, शृत, प्रयुञ्जीत, क्षीर, अष्टम, नवम.", role="extend",
              teaches="मूलैः शृतम् = boiled with roots: the instrumental names what the milk is boiled with."),
        mcq("discriminate", 3, "Which split of printed तथाऽष्टमे is right?",
            ("तथा + अष्टमे", "आ + अ → आ; the ऽ printed after आ is a print habit."),
            [("तथे + अष्टमे", "ए + अ would give तथेऽष्टमे, with ए kept."),
             ("तथ + ष्टमे", "Neither तथ nor ष्टमे is a word here."),
             ("तथा + ष्टमे", "ष्टमे is not a word; the word is अष्टमे, in the eighth.")],
            "तथा (likewise) + अष्टमे (in the eighth): the regular join is तथाष्टमे.",
            "आ + अ → आ."),
        multi("apply", 4, "Which statements about verse 133 are right by the card?",
              [("The milk is boiled with roots", "Right: मूलैः शृतं क्षीरम्."),
               ("The verse states a dose of milk", "No dose is given."),
               ("The ninth month adds sārivā and licorice", "Right: नवमे सारिवा… मधुयष्टिभिः."),
               ("Line 2 has its own verb", "Its verb, योजयेत्, comes in unit 134.")],
              [0, 2],
              "Milk boiled with roots; in the ninth, with sārivā, anantā, payasyā and licorice.",
              "मूलैः शृतं क्षीरम्; नवमे …भिः."),
        mcq("transfer", 5, "By the pattern of मूलैः शृतम्, what does पुष्पैः mean in पुष्पैः शृतम् (a new example)?",
            ("with flowers", "-ऐः is the instrumental plural of a-stems, as मूलैः, with roots."),
            [("of the flowers", "Of the flowers would be the genitive पुष्पाणाम्."),
             ("in the flowers", "In the flowers would be the locative पुष्पेषु."),
             ("from one flower", "From a flower would be the ablative पुष्पात्.")],
            "पुष्पैः शृतम् = boiled with flowers, like मूलैः शृतम्.",
            "-ऐः = with (instrumental plural).",
            teaches="-ऐः on an a-stem is the instrumental plural, 'with': मूलैः = with roots."),
    ],
}

# ---------------------------------------------------------------- unit 134
AUTHORED["134"] = {
    "title": "योजयेद्दशमेमासि सिद्धं क्षीरं पयस्यया",
    "question": "By verse 134, what milk is applied in the tenth month?",
    "rule": ("In the tenth month (दशमे मासि) one should apply milk cooked (सिद्धम्) with payasyā (disputed); or (अथवा) with "
             "yaṣṭimadhuka (licorice), nāgara (dry ginger) and amaradāru (deodar). Its verb also serves the ninth month of unit 133."),
    "limits": ("Payasyā's identity is disputed: no question asks it. Line 2 appears to continue line 1 (the same tenth-month "
               "milk, cooked with these instead). No dose is given."),
    "explain_hi": ("यह श्लोक दसवें महीने का योग देता है। "
                   "दसवें महीने में (दशमे मासि) पयस्या (पहचान विवादित) से पकाया दूध (सिद्धं क्षीरम्) प्रयोग करे (योजयेत्)। "
                   "अथवा यष्टिमधुक (मुलेठी), नागर (सोंठ) और अमरदारु (देवदार) से पकाया हुआ। "
                   "‘योजयेत्’ इकाई १३३ के नवें महीने के लिए भी क्रिया है। मात्रा नहीं दी गई।"),
    "hook": "दसवाँ महीना: पयस्या का दूध, या मुलेठी-सोंठ-देवदार का।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By verse 134, in which month is this milk applied?",
            ("The tenth month", "दशमे मासि: in the tenth month."),
            [("The second month", "The verse says दशमे, the tenth."),
             ("The fifth month", "The verse says दशमे, the tenth."),
             ("The sixth month", "The verse says दशमे, the tenth.")],
            "In the tenth month, milk cooked with payasyā is applied.",
            "दशमे मासि."),
        order(1, "Put these phrases of verse 134 in the verse's order.",
              ["योजयेद्दशमेमासि", "सिद्धं क्षीरं", "पयस्यया", "अथवा", "यष्टिमधुकनागरामरदारुभिः"],
              "One should apply in the tenth month milk cooked with payasyā, or with licorice, dry ginger and deodar.",
              "योजयेद्दशमेमासि → सिद्धं क्षीरं → पयस्यया → अथवा → यष्टिमधुकनागरामरदारुभिः."),
        match(2, "Match each word of verse 134 to its meaning.",
              [["दशम", "tenth"], ["सिद्ध", "cooked"], ["क्षीर", "milk"], ["अथवा", "or"],
               ["नागर", "dry ginger (standard)"], ["अमरदारु", "deodar (standard)"]],
              "Milk cooked with payasyā, or with licorice, dry ginger and deodar.",
              "दशम, सिद्ध, क्षीर, अथवा, नागर, अमरदारु.", role="extend",
              teaches="मासि, like मासे, means 'in the month': दशमे मासि = in the tenth month."),
        mcq("discriminate", 3, "Which split of योजयेद्दशमे is right?",
            ("योजयेत् + दशमे", "A final त् becomes द् before a voiced sound: योजयेद्दशमे."),
            [("योजयेः + दशमे", "A visarga after ए before a voiced sound gives र्: योजयेर्दशमे."),
             ("योजयेम् + दशमे", "A final म् before a consonant becomes ं: योजयें दशमे."),
             ("योजये + द्दशमे", "द्दशमे is not a word; the word is दशमे, in the tenth.")],
            "योजयेत् (should apply) + दशमे (in the tenth).",
            "त् + voiced sound → द्."),
        mcq("apply", 4, "By verse 134, what is the other choice (अथवा) for the tenth month?",
            ("Milk cooked with licorice, dry ginger and deodar", "अथवा यष्टिमधुकनागरामरदारुभिः."),
            [("Milk boiled with roots of kapittha, bilva and others", "That is unit 133, milk boiled with roots."),
             ("Plain milk taken with no drug at all", "The verse names drugs for the milk."),
             ("Ghee cooked with payasyā and white sugar", "The verse names milk, not ghee.")],
            "Or the milk is cooked with licorice, dry ginger and deodar.",
            "अथवा … भिः."),
        mcq("transfer", 5, "By the rule of योजयेत् + दशमे, how is भवेत् + धनम् (there should be wealth) joined?",
            ("भवेद्धनम्", "A final त् becomes द् before a voiced sound, as योजयेत् + दशमे."),
            [("भवेत्धनम्", "Before a voiced sound the final त् does not stay unvoiced."),
             ("भवेन्धनम्", "त् becomes न् only before a nasal; ध is not a nasal."),
             ("भवेच्धनम्", "त् becomes च् before च, छ or श, not before ध.")],
            "भवेत् + धनम् = भवेद्धनम्, like योजयेत् + दशमे = योजयेद्दशमे.",
            "त् + voiced sound → द्.",
            teaches="A word-final त् becomes द् before a voiced sound: योजयेत् + दशमे → योजयेद्दशमे."),
    ],
}

# ---------------------------------------------------------------- unit 135
AUTHORED["135"] = {
    "title": "इति गर्भव्यापन्नाम चतुर्थोऽध्यायः",
    "question": "What does the colophon in unit 135 name the fourth chapter?",
    "rule": ("Thus the fourth chapter, named Garbhavyāpad (mishap of the fetus). Printed गर्भव्यापन्नाम = गर्भव्यापत् + नाम."),
    "limits": "A colophon: it gives the chapter's name and number and teaches nothing else. A prose line.",
    "explain_hi": ("यह अध्याय की समाप्ति-पंक्ति (पुष्पिका) है: इस प्रकार गर्भव्यापत् नाम का चौथा अध्याय (पूरा हुआ)। "
                   "गर्भव्यापत् = गर्भ + व्यापद्: गर्भ की विपत्ति या दुर्घटना। "
                   "छपे शब्द सन्धि से जुड़े हैं: गर्भव्यापत् + नाम → गर्भव्यापन्नाम (त् + न → न्न), चतुर्थः + अध्यायः → "
                   "चतुर्थोऽध्यायः।"),
    "hook": "शारीर का चौथा अध्याय: गर्भव्यापत्।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 135, what is chapter four named?",
            ("गर्भव्यापत्", "इति गर्भव्यापन्नाम चतुर्थोऽध्यायः."),
            [("गर्भावक्रान्ति", "That is the name of chapter two."),
             ("पुत्रकामीय", "That is the name of chapter one."),
             ("बलातैल", "That is the oil taught in units 120 to 125, not a chapter name.")],
            "The colophon names the chapter Garbhavyāpad, mishap of the fetus.",
            "गर्भव्यापद् = mishap of the fetus."),
        order(1, "Put the words of unit 135 in their order.",
              ["इति", "गर्भव्यापत्", "नाम", "चतुर्थः", "अध्यायः"],
              "Thus, Garbhavyāpad, named, fourth, chapter.",
              "इति → गर्भव्यापत् → नाम → चतुर्थः → अध्यायः."),
        match(2, "Match each word of unit 135 to its meaning.",
              [["इति", "thus (closing)"], ["गर्भ", "fetus"], ["व्यापद्", "mishap, calamity"], ["नाम", "named"],
               ["चतुर्थ", "fourth"]],
              "Thus the fourth chapter, named mishap of the fetus.",
              "इति, गर्भ, व्यापद्, नाम, चतुर्थ.", role="extend",
              teaches="गर्भव्यापद् = गर्भ + व्यापद्: a mishap of the fetus, the theme of the whole chapter."),
        mcq("discriminate", 3, "Which split of गर्भव्यापन्नाम is right?",
            ("गर्भव्यापत् + नाम", "A final त् before a nasal may become न्: गर्भव्यापन्नाम."),
            [("गर्भव्यापः + नाम", "अः before a voiced sound gives ओ: गर्भव्यापो नाम."),
             ("गर्भव्यापा + नाम", "आ before न stays: गर्भव्यापानाम, with one न."),
             ("गर्भव्यापम् + नाम", "A final म् before a consonant becomes ं: गर्भव्यापं नाम.")],
            "गर्भव्यापत् (mishap of the fetus) + नाम (named): त् + न → न्न.",
            "त् + nasal → न् (may)."),
        fill(4, "In unit 135 the word for fourth is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("चतुर्थः", None, "चतुर्थ"),
             "चतुर्थः = fourth; before अध्यायः it is printed चतुर्थोऽध्यायः.",
             "चतुर्थ means fourth; ऽ shows the lost अ of अध्यायः.",
             "चतुर्थ = fourth.", role="apply"),
        mcq("transfer", 5, "By the rule of चतुर्थोऽध्यायः, how is पञ्चमः + अध्यायः (the fifth chapter) joined?",
            ("पञ्चमोऽध्यायः", "अः + अ → ओ, and ऽ marks the lost अ, as चतुर्थः + अध्यायः."),
            [("पञ्चमा अध्यायः", "आ with a gap comes from आः before a vowel, not from अः."),
             ("पञ्चम अध्यायः", "अः drops its visarga with a gap only before vowels other than अ."),
             ("पञ्चमरध्यायः", "र् comes from a visarga after vowels other than अ and आ.")],
            "पञ्चमः + अध्यायः = पञ्चमोऽध्यायः, like चतुर्थः + अध्यायः = चतुर्थोऽध्यायः.",
            "अः + अ → ओऽ.",
            teaches="अः before अ becomes ओ and the following अ is shown by ऽ: चतुर्थोऽध्यायः."),
    ],
}

# ===================================================================== NOTES_HI
NOTES_HI = {
    "123": ("गद्य-पंक्ति (02.04.139); विश्वास मध्यम; कोई पाठ-चिह्न नहीं। ‘तेन’ = उस (तेल) से, डेटा के अनुसार; तेल का नाम पंक्ति में नहीं। "
            "गुल्म, हिध्मा, श्वास, कास उसी खण्ड में गिने गए हैं; पंक्ति इन्हें वात-विकार नहीं कहती। आधुनिक नाम डेटा के अनुसार मानक "
            "(गुल्म का ठीक आधुनिक रोग तय नहीं)। दोहरे व्यंजन (वीर्य्योजांसि, वर्द्धंते, निवर्त्तंते) छपाई की आदत। सन्धि जाँची: मेधा + अग्नि → "
            "मेधाग्नि (आ + अ → आ); पक्षघात + आक्षेपक → पक्षघाताक्षेपक; आक्षेपक + अर्दित → आक्षेपकार्दित; अर्दित + आदि → अर्दितादि; "
            "कासाः + निवर्तन्ते → कासा निवर्तन्ते (आः का विसर्ग घोष से पहले लुप्त; छपाई में साथ लिखा)। ध्यान दें: वीर्य + ओजांसि का "
            "नियमित योग वीर्यौजांसि (अ + ओ → औ) होता; छपा ‘वीर्य्योजांसि’ ओ दिखाता है; डेटा इस पर कुछ नहीं कहता, इसलिए इस पर प्रश्न नहीं।"),
    "124": ("गद्य-पंक्ति (02.04.140); विश्वास मध्यम। पाठ-चिह्न (सम्भावित): छपा ‘षण्मासा दंत्रवृद्धिः’ = ‘षण्मासाद् अन्त्रवृद्धिः’; "
            "पंचमी षण्मासात् का द् (घोष से पहले त् → द्) अगले शब्द के आरम्भ में छप गया, और ‘अन्त्र’ (आँत) अभिप्रेत है, ‘दन्त्र’ नहीं। "
            "रोग के नाम पर प्रश्न नहीं। अन्त्रवृद्धि = आँत की सूजन, सम्भवतः हर्निया (सम्भावित)। पंचमी = ‘छह महीने बाद’, ‘छह महीने में’ भी "
            "सम्भव। तेल समझा जाता है। सन्धि जाँची: अहरहः + च → अहरहश्च (विसर्ग + च → श्च); च + उपयुज्यमानेन → चोपयुज्यमानेन (अ + उ → ओ); "
            "प्रशमम् + एति → प्रशममेति।"),
    "125": ("गद्य-पंक्ति (02.04.141); विश्वास निम्न। पाठ-चिह्न (सम्भावित): छपा ‘इच्छ्या’ नियमित रूप नहीं; ‘इच्छया’ (इच्छा से) पढ़ा गया; "
            "दूसरा विकल्प ‘इच्छन्ती’ (चाहती हुई)। इस पर प्रश्न नहीं। वन्ध्या = बाँझ स्त्री (मानक)। ‘लभत’ = लभते का स्वर से पहले वाला नियमित "
            "रूप, इसलिए अलग चिह्न नहीं। सन्धि जाँची: वन्ध्या + च → वन्ध्या च (छपाई में साथ); लभते + इति → लभत इति (ए + स्वर → अय्, "
            "य् का प्रायः लोप; बीच में अन्तर)। ‘इति’ कथन समाप्त करता है।"),
    "126": ("गद्य-पंक्ति (02.04.142); विश्वास उच्च। पाठ-चिह्न (सम्भावित): छपा ‘भवंत’ → ‘भवन्ति’ (ति के स्थान पर त छपाई की भूल; यही "
            "सूत्र इस अध्याय में इकाई ११० में भी है)। संज्ञा (क्या हैं) छपी नहीं, जोड़ी नहीं गई। आगे के श्लोक इकाई १२७ से। सन्धि जाँची: "
            "च + अत्र → चात्र (अ + अ → आ)।"),
    "127": ("श्लोक, दो छपी पंक्तियाँ (02.04.143, 02.04.144); विश्वास मध्यम; कोई पाठ-चिह्न नहीं। वाक्य दोनों पंक्तियों में पूरा होता है। "
            "‘विपन्न’ = नष्ट या मृत; प्रसंग मृत्यु सुझाता है, पंक्ति स्पष्ट नहीं कहती। ‘बस्तिद्वार’ नहीं समझाया गया (बस्ति-क्षेत्र का द्वार या "
            "श्रोणि-मार्ग सम्भव); शाब्दिक रखा, इस पर प्रश्न नहीं। कुक्षि = पेट, विशेषतः गर्भाशय नहीं। ‘पाटयित्वा’ का कर्म (पेट) छपा नहीं। "
            "‘जन्मकाले’ = ‘जन्म के उचित समय पर’ भी। सन्धि जाँची: पाटयित्वा + उद्धरेत् → पाटयित्वोद्धरेत् (आ + उ → ओ); उद्धरेत् + शिशुम् → "
            "उद्धरेच्छिशुम् (त् + श → च्छ, सामान्य लिखित रूप); छपा ‘शिशुं’ = शिशुम्।"),
    "128": ("श्लोक, दो छपी पंक्तियाँ (02.04.145, 02.04.146); विश्वास मध्यम; कोई पाठ-चिह्न नहीं। सात योगों की शृंखला (इकाई १२८-१३१) "
            "यहीं से; हर आधा श्लोक एक योग; दूध इकाई १३१ में, क्रिया ‘योजयेत्’ और सात महीने इकाई १३२ में। पहचान: मधुक = मुलेठी (सम्भावित; "
            "महुआ दूसरा विकल्प); शाक = सागौन (सम्भावित; ‘सब्ज़ी’ भी अर्थ); पयस्या विवादित; सुरदारु = देवदार (सम्भावित); अश्मन्तक विवादित; "
            "कृष्णतिल = काले तिल (मानक); ताम्रवल्ली अज्ञात। सन्धि जाँची: कृष्णतिलाः + ताम्रवल्ली → कृष्णतिलास्ताम्रवल्ली (विसर्ग + त → स्त)।"),
    "129": ("श्लोक, दो छपी पंक्तियाँ (02.04.147, 02.04.148); विश्वास मध्यम। पाठ-चिह्न (सम्भावित): छपा ‘रास्त्रा’ → ‘रास्ना’ (स्न के स्थान पर "
            "स्त्र, जैसे इकाई ११४ में); इस पर प्रश्न नहीं। छपा ‘सारिबा’ = सारिवा (ब/व का अदल-बदल)। विभाग ‘लता | सोत्पलसारिवा’ चुना गया; "
            "‘लता सोत्पला | सारिवा’ भी सम्भव; इस पर प्रश्न नहीं। छपा ‘वृक्षदनी’ (ह्रस्व अ); सामान्य वर्तनी ‘वृक्षादनी’; छपा रूप रखा। अनन्ता "
            "और सारिवा दोनों गिने गए, इसलिए अलग। सन्धि जाँची: स + उत्पल → सोत्पल (अ + उ → ओ)।"),
    "130": ("श्लोक, दो छपी पंक्तियाँ (02.04.149, 02.04.150); विश्वास मध्यम; कोई पाठ-चिह्न नहीं। बृहतीद्वय = बृहती और कण्टकारी (सम्भावित)। "
            "‘क्षीरिशुङ्गत्वचः’ = दूधवाले वृक्षों की कोंपलों की छाल (चुना गया अर्थ) या तीन अलग द्रव्य; वृक्षों के नाम यहाँ नहीं (बाद की परम्परा "
            "चार अंजीर-वर्गीय वृक्ष गिनती है, यहाँ नहीं कहा)। श्वदंष्ट्रा = गोखरू (सम्भावित), कण्टकारी के लिए भी यह नाम आया है। मधुपर्णिका "
            "विवादित। ‘काश्मर्य्य’ का दोहरा य् छपाई की आदत। सन्धि जाँची: …त्वचः + घृतम् → …त्वचो घृतम् (अः + घोष → ओ)।"),
    "131": ("श्लोक, दो छपी पंक्तियाँ (02.04.151, 02.04.152); विश्वास मध्यम; कोई पाठ-चिह्न नहीं। सातवाँ योग पहली पंक्ति में। दूसरी पंक्ति "
            "इकाई १३२ में चलती है (क्रिया ‘योजयेत्’)। ‘अर्धश्लोकसमापन’ = आधे श्लोक पर पूरा होने वाले। छपा ‘सर्वैतान्’ को डेटा ‘सर्वान् "
            "एतान्’ पढ़ता है (नियमित सन्धि से नहीं बनता); इस पर प्रश्न नहीं। सिता = मिश्री (सम्भावित)। सन्धि जाँची: योगान् + अर्ध… → "
            "योगानर्ध… (दीर्घ स्वर के बाद न् + स्वर, न् ज्यों का त्यों)। ‘अर्द्ध’ = अर्ध (छपाई की आदत)।"),
    "132": ("श्लोक, दो छपी पंक्तियाँ (02.04.153, 02.04.154); विश्वास मध्यम। पाठ-चिह्न (सम्भावित): ‘कपित्थ…निदिग्धिकान्’ का अन्तिम न् "
            "‘मूलैः’ (इकाई १३३) से मेल नहीं खाता; छपाई की भूल माना गया; कारक पर प्रश्न नहीं। ‘गर्भे स्रवति’ = सति-सप्तमी, गर्भ के बहने पर "
            "(गर्भस्राव, सम्भावित)। ‘उन्हें’ (योग) छपा नहीं। सात योग, सात महीने। सन्धि जाँची: पटोल + इक्षु → पटोलेक्षु (अ + इ → ए); "
            "क्रमात् + सप्तसु → क्रमात्सप्तसु।"),
    "133": ("श्लोक, दो छपी पंक्तियाँ (02.04.155, 02.04.156); विश्वास निम्न; कोई पाठ-चिह्न नहीं। ‘मासे’ के साथ क्रम-संख्या नहीं: कोई संख्या "
            "छूटी हो या ‘एक महीने तक’ अर्थ; अनिश्चित, इस पर प्रश्न नहीं (छन्द में १६ अक्षर पूरे हैं)। जड़ें इकाई १३२ की वनस्पतियों की। दूसरी "
            "पंक्ति में क्रिया और ‘दूध’ नहीं; क्रिया इकाई १३४ में। ‘तथाऽष्टमे’ और ‘सारिवाऽनंता’ में आ के बाद ऽ छपाई की आदत। सन्धि जाँची: "
            "तथा + अष्टमे → तथाष्टमे (आ + अ → आ); सारिवा + अनन्ता → सारिवानन्ता; छपा ‘क्षीरंमासे’ = क्षीरं मासे।"),
    "134": ("श्लोक, दो छपी पंक्तियाँ (02.04.157, 02.04.158); विश्वास मध्यम; कोई पाठ-चिह्न नहीं। ‘योजयेत्’ इकाई १३३ के नवें महीने के लिए भी। "
            "सिद्ध = पकाया हुआ। पयस्या विवादित। दूसरी पंक्ति पहली को आगे बढ़ाती प्रतीत होती है (वही दसवें मास का दूध, इनसे पका)। अमरदारु = "
            "देवदार (मानक); नागर = सोंठ (मानक)। सन्धि जाँची: योजयेत् + दशमे → योजयेद्दशमे (त् + घोष → द्); यष्टिमधुक + नागर → …नागर; "
            "नागर + अमरदारु → नागरामरदारु (अ + अ → आ)।"),
    "135": ("गद्य, पुष्पिका (02.04.159); विश्वास उच्च; कोई पाठ-चिह्न नहीं। सन्धि जाँची: गर्भव्यापत् + नाम → गर्भव्यापन्नाम (त् + अनुनासिक → "
            "न्; विकल्प से द् भी); चतुर्थः + अध्यायः → चतुर्थोऽध्यायः (अः + अ → ओऽ)। गर्भव्यापत् = गर्भ की विपत्ति।"),
}

# ===================================================================== AIDS
AIDS = {
    "123": {
        "seesaw": {"groups": [
            {"label": "बढ़ते हैं (वर्धन्ते)", "items": ["बल", "पौरुष", "स्मृति", "मति", "मेधा", "अग्नि", "वीर्य", "ओज"]},
            {"label": "दूर होते हैं (निवर्तन्ते)", "items": ["वात-विकार: पक्षाघात, आक्षेपक, अर्दित आदि", "गुल्म", "हिध्मा",
                                                            "श्वास", "कास"]}]},
        "chunks": "तेन | बलपौरुषस्मृतिमतिमेधाग्निवीर्य्योजांसि वर्द्धंते | पक्षघाताक्षेपकार्दितादिविविधवातविकार | "
                  "गुल्महिध्माश्वासकासा | निवर्त्तंते",
        "sandhi": "आः + घोष → आ (विसर्ग-लोप): कासाः + निवर्तन्ते → कासा निवर्तन्ते · आ + अ → आ: मेधा + अग्नि → मेधाग्नि · "
                  "अ + अ → आ: आक्षेपक + अर्दित → आक्षेपकार्दित।",
    },
    "124": {
        "frame": "कैसे: प्रतिदिन प्रयोग (अहरहः उपयुज्यमानेन) → कब तक: छह महीने (षण्मासात्) → फल: अन्त्रवृद्धि (सम्भवतः हर्निया; "
                 "सम्भावित पाठ) शान्त होती है (प्रशमम् एति)।",
        "chunks": "अहरहश्चोपयुज्यमानेन | षण्मासा | दंत्रवृद्धिः | प्रशममेति",
        "sandhi": "विसर्ग + च → श्च: अहरहः + च → अहरहश्च · अ + उ → ओ: च + उपयुज्यमानेन → चोपयुज्यमानेन · "
                  "त् + घोष → द्: षण्मासात् + अन्त्र… → षण्मासाद् अन्त्र… (सम्भावित पाठ)।",
    },
    "125": {
        "frame": "कौन: वन्ध्या (बाँझ स्त्री) → क्या पाती है: गुणवान् पुत्र (पुत्रं गुणवन्तम्) → क्रिया: लभते → समाप्ति: इति। "
                 "(‘इच्छ्या’ = इच्छा से: अनुमानित पाठ)",
        "chunks": "वंध्याच | पुत्रं | गुणवंतमिच्छ्या | लभतइति",
        "sandhi": "ए + स्वर → अ (य् का प्रायः लोप, बीच में अन्तर): लभते + इति → लभत इति।",
    },
    "126": {
        "frame": "भवन्ति (हैं) + च (और) + अत्र (इस विषय में) → आगे के श्लोकों की भूमिका (इकाई १२७ से)। संज्ञा छपी नहीं।",
        "sandhi": "अ + अ → आ: च + अत्र → चात्र।",
    },
    "127": {
        "chain": {"steps": ["बस्तिद्वार पर विपन्न स्त्री", "यदि उसकी कुक्षि फड़के", "जन्म के समय", "तब शीघ्र",
                            "चीरकर (पाटयित्वा)", "शिशु को निकाले (उद्धरेत्)"]},
        "chunks": "बस्तिद्वारे | विपन्नायाः | कुक्षिः प्रस्पंदते यदि / जन्मकाले | ततः शीघ्रं | पाटयित्वोद्धरेच्छिशुं",
        "sandhi": "आ + उ → ओ: पाटयित्वा + उद्धरेत् → पाटयित्वोद्धरेत् · त् + श → च्छ: उद्धरेत् + शिशुम् → उद्धरेच्छिशुम्।",
    },
    "128": {
        "diagram": {"groups": [
            {"label": "पहला योग (पंक्ति १)", "items": ["मधुक (मुलेठी, सम्भावित)", "शाकबीज (सागौन, सम्भावित)",
                                                     "पयस्या (विवादित)", "सुरदारु (देवदार, सम्भावित)"]},
            {"label": "दूसरा योग (पंक्ति २)", "items": ["अश्मन्तक (विवादित)", "कृष्णतिल (काले तिल, मानक)",
                                                     "ताम्रवल्ली (अज्ञात)", "शतावरी"]}]},
        "chunks": "मधुकं | शाकबीजं च | पयस्या | सुरदारु च / अश्मंतकः | कृष्णतिलास्ताम्रवल्ली | शतावरी",
        "sandhi": "विसर्ग + त → स्त: कृष्णतिलाः + ताम्रवल्ली → कृष्णतिलास्ताम्रवल्ली।",
    },
    "129": {
        "diagram": {"groups": [
            {"label": "तीसरा योग (पंक्ति १)", "items": ["वृक्षदनी (बांदा, सम्भावित)", "पयस्या (विवादित)",
                                                     "लता (अस्पष्ट)", "उत्पल-सहित सारिवा"]},
            {"label": "चौथा योग (पंक्ति २)", "items": ["अनन्ता (विवादित)", "सारिवा", "रास्ना (अनुमानित पाठ)",
                                                    "पद्मा (अस्पष्ट)", "मधुयष्टिका (मुलेठी, मानक)"]}]},
        "chunks": "वृक्षदनी | पयस्या च | लता | सोत्पलसारिबा / अनंता | सारिवा | रास्त्रा | पद्मा च | मधुयष्टिका",
        "sandhi": "अ + उ → ओ: स + उत्पल → सोत्पल।",
    },
    "130": {
        "diagram": {"groups": [
            {"label": "पाँचवाँ योग (पंक्ति १)", "items": ["दोनों बृहती (कटेरी, सम्भावित)", "काश्मर्य (गम्भारी)",
                                                       "क्षीरी वृक्षों की कोंपलों की छाल", "घृत (घी)"]},
            {"label": "छठा योग (पंक्ति २)", "items": ["पृश्निपर्णी (पिठवन)", "बला (बरियार)", "शिग्रु (सहजन)",
                                                   "श्वदंष्ट्रा (गोखरू, सम्भावित)", "मधुपर्णिका (विवादित)"]}]},
        "chunks": "बृहतीद्वय | काश्मर्य्य | क्षीरिशुंगत्वचो | घृतं / पृश्निपर्णी | बला | शिग्रुः | श्वदंष्ट्रा | मधुपर्णिका",
    },
    "131": {
        "diagram": {"groups": [
            {"label": "सातवाँ योग (पंक्ति १)", "items": ["शृंगाटक (सिंघाड़ा)", "बिस (कमलनाल)", "द्राक्षा (अंगूर)",
                                                      "कसेरु (सम्भावित)", "मधुक (मुलेठी, सम्भावित)", "सिता (मिश्री, सम्भावित)"]},
            {"label": "पंक्ति २: सब योग", "items": ["दूध के साथ (पयसा)", "हर एक आधे श्लोक पर पूरा",
                                                 "क्रिया अगली इकाई (१३२) में"]}]},
        "chunks": "शृंगाटकं | बिसं | द्राक्षा | कसेरु | मधुकं | सिता / सर्वैतान् | पयसा | योगान् | अर्द्धश्लोकसमापनान्",
        "sandhi": "दीर्घ स्वर के बाद न् + स्वर → जुड़ जाता है: योगान् + अर्ध… → योगानर्ध…।",
    },
    "132": {
        "chain": {"steps": ["सात योग (इकाई १२८-१३१)", "क्रम से (क्रमात्)", "सात महीनों में", "गर्भ बहने पर (सम्भवतः गर्भस्राव)",
                            "प्रयोग करे (योजयेत्)"]},
        "chunks": "क्रमात्सप्तसु मासेषु | गर्भे स्रवति | योजयेत् / कपित्थ | बिल्व | बृहती | पटोल | इक्षु | निदिग्धिका(न्)",
        "sandhi": "अ + इ → ए: पटोल + इक्षु → पटोलेक्षु।",
    },
    "133": {
        "diagram": {"groups": [
            {"label": "जड़ों से उबला दूध", "items": ["‘मासे’ में (संख्या छपी नहीं)", "उसी प्रकार आठवें में"]},
            {"label": "नौवें में, इनके साथ", "items": ["सारिवा", "अनन्ता (विवादित)", "पयस्या (विवादित)", "मधुयष्टि (मुलेठी)"]}]},
        "chunks": "मूलैः शृतं | प्रयुंजीत | क्षीरंमासे | तथाऽष्टमे / नवमे | सारिवाऽनंतापयस्यामधुयष्टिभिः",
        "sandhi": "आ + अ → आ: तथा + अष्टमे → तथाष्टमे (छपा ऽ छपाई की आदत)।",
    },
    "134": {
        "diagram": {"groups": [
            {"label": "दसवाँ महीना: पका दूध", "items": ["पयस्या से (विवादित)"]},
            {"label": "अथवा, इनसे", "items": ["यष्टिमधुक (मुलेठी)", "नागर (सोंठ)", "अमरदारु (देवदार)"]}]},
        "chunks": "योजयेद्दशमेमासि | सिद्धं क्षीरं | पयस्यया / अथवा | यष्टिमधुकनागरामरदारुभिः",
        "sandhi": "त् + घोष → द्: योजयेत् + दशमे → योजयेद्दशमे · अ + अ → आ: नागर + अमरदारु → नागरामरदारु।",
    },
    "135": {
        "chunks": "इति | गर्भव्यापन्नाम | चतुर्थोऽध्यायः",
        "sandhi": "त् + अनुनासिक → न्: गर्भव्यापत् + नाम → गर्भव्यापन्नाम · अः + अ → ओऽ: चतुर्थः + अध्यायः → चतुर्थोऽध्यायः।",
    },
}

# ===================================================================== IMAGE_SPECS
IMAGE_SPECS = {
    ("123", "seesaw"): {
        "file": "sh4-bala-taila-guna-123.svg",
        "alt": ("Two columns of unit 123. Increase: strength, manly vigour, memory, understanding, intellect, digestive fire, "
                "vīrya, ojas. Cease: Vāta disorders beginning with hemiplegia, convulsive disorder and facial paralysis; gulma; "
                "hiccup; breathlessness; cough."),
        "type": "split",
        "title": "इकाई १२३: तेल से (तेन)",
        "cols": [["बढ़ते हैं (वर्धन्ते)", ["१ बल", "२ पौरुष", "३ स्मृति", "४ मति", "५ मेधा", "६ अग्नि", "७ वीर्य", "८ ओज"]],
                 ["दूर होते हैं (निवर्तन्ते)", ["वात-विकार: पक्षाघात, आक्षेपक, अर्दित आदि", "गुल्म", "हिध्मा (हिचकी)",
                                                "श्वास", "कास (खाँसी)"]]],
    },
    ("127", "chain"): {
        "file": "sh4-shishu-uddharana-127.svg",
        "alt": ("Flowchart of verse 127: a woman who has perished at the bastidvāra; if her belly quivers; at the time of birth; "
                "then quickly, having split (it) open; one should take out the child."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"बस्तिद्वार पर विपन्न स्त्री\"] --> B[\"यदि कुक्षि फड़के\"]\n"
                 "  B --> C[\"जन्म के समय\"]\n"
                 "  C --> D[\"तब शीघ्र चीरकर\"]\n"
                 "  D --> E[\"शिशु को निकाले\"]\n"),
    },
    ("128", "diagram"): {
        "file": "sh4-yoga-1-2-128.svg",
        "alt": ("Table of verse 128: first combination: madhuka (licorice, probable), śāka seed (teak, probable), payasyā "
                "(disputed), suradāru (deodar, probable); second: aśmantaka (disputed), black sesame (standard), tāmravallī "
                "(unidentified), śatāvarī."),
        "type": "table",
        "title": "इकाई १२८: पहला और दूसरा योग",
        "heads": ["योग: द्रव्य", "डेटा की पहचान"],
        "rows": [["पहला: मधुक", "मुलेठी, सम्भावित"], ["पहला: शाकबीज", "सागौन का बीज, सम्भावित"],
                 ["पहला: पयस्या", "पहचान विवादित"], ["पहला: सुरदारु", "देवदार, सम्भावित"],
                 ["दूसरा: अश्मन्तक", "पहचान विवादित"], ["दूसरा: कृष्णतिल", "काले तिल, मानक"],
                 ["दूसरा: ताम्रवल्ली", "पहचान अज्ञात"], ["दूसरा: शतावरी", "शतावरी"]],
    },
    ("130", "diagram"): {
        "file": "sh4-yoga-5-6-130.svg",
        "alt": ("Two columns of verse 130. Fifth combination: the two bṛhatīs (probable), kāśmarya (gambhārī), bark of the "
                "shoots of milk-yielding trees, ghee. Sixth: pṛśniparṇī, balā, śigru, śvadaṃṣṭrā (puncture-vine, probable), "
                "madhuparṇikā (disputed)."),
        "type": "split",
        "title": "इकाई १३०: पाँचवाँ और छठा योग",
        "cols": [["पाँचवाँ योग", ["दोनों बृहती (सम्भावित)", "काश्मर्य (गम्भारी)", "क्षीरी वृक्षों की कोंपल-छाल", "घृत (घी)"]],
                 ["छठा योग", ["पृश्निपर्णी (पिठवन)", "बला (बरियार)", "शिग्रु (सहजन)", "श्वदंष्ट्रा (गोखरू, सम्भावित)",
                              "मधुपर्णिका (विवादित)"]]],
    },
    ("132", "chain"): {
        "file": "sh4-sapta-masa-132.svg",
        "alt": ("Chain of verse 132: the seven combinations of units 128 to 131; in sequence; in the seven months; when the "
                "fetus is flowing (probably miscarriage); one should apply them."),
        "type": "chain",
        "title": "इकाई १३२: सात योग, सात मास",
        "steps": ["सात योग (इकाई १२८-१३१)", "क्रम से", "सात महीनों में", "गर्भ बहने पर (सम्भवतः गर्भस्राव)", "प्रयोग करे"],
    },
    ("133", "diagram"): {
        "file": "sh4-mula-kshira-133.svg",
        "alt": ("Table of verse 133: milk boiled with roots in the month (number not printed), likewise in the eighth; in the "
                "ninth, with sārivā, anantā (disputed), payasyā (disputed) and madhuyaṣṭī (licorice)."),
        "type": "table",
        "title": "इकाई १३३: जड़ों का दूध और नौवाँ मास",
        "heads": ["मास", "दूध"],
        "rows": [["मास (संख्या छपी नहीं)", "जड़ों से उबला दूध"], ["आठवाँ", "उसी प्रकार"],
                 ["नौवाँ", "सारिवा, अनन्ता, पयस्या, मधुयष्टि के साथ"]],
    },
    ("134", "diagram"): {
        "file": "sh4-dashama-masa-134.svg",
        "alt": ("Two columns of verse 134, the tenth month: milk cooked with payasyā (disputed); or cooked with yaṣṭimadhuka "
                "(licorice), nāgara (dry ginger) and amaradāru (deodar)."),
        "type": "split",
        "title": "इकाई १३४: दसवें मास का दूध",
        "cols": [["पका दूध", ["पयस्या से (विवादित)"]],
                 ["अथवा", ["यष्टिमधुक (मुलेठी)", "नागर (सोंठ)", "अमरदारु (देवदार)"]]],
    },
}
