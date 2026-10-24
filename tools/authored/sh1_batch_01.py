from helpers import mcq, match, order, fill, multi, accepts


def T(q, teaches):
    q["teaches"] = teaches
    return q


AUTHORED = {}

# ---------------------------------------------------------------- unit 1
AUTHORED["1"] = {
    "title": "श्रीगणेशाय नमः",
    "question": "To whom is homage paid in the opening line of the Śārīrasthāna, and how is that said in Sanskrit?",
    "rule": ("श्रीगणेशाय नमः: homage (नमः) to the auspicious Gaṇeśa. The one receiving homage stands in the dative "
             "(to), and नमः needs no verb."),
    "limits": ("An invocation of two words only. It says nothing about the subject of the section; Gaṇeśa is kept as "
               "a divine name and nothing further is added."),
    "explain_hi": ("शारीरस्थान की पहली पंक्ति एक मंगल-वाक्य है: ‘श्रीगणेशाय नमः’, यानी श्री गणेश को नमस्कार। "
                   "‘गणेशाय’ चतुर्थी विभक्ति (सम्प्रदान) है, जिसका अर्थ है ‘को, के लिए’। "
                   "‘नमः’ का अर्थ है नमस्कार; इसके साथ अलग क्रिया की ज़रूरत नहीं होती, और जिसे नमस्कार हो वह चतुर्थी में आता है। "
                   "विषय की बात अभी शुरू नहीं हुई; यह केवल आरम्भ का प्रणाम है।"),
    "hook": "नमः के साथ चतुर्थी: गणेशाय नमः = गणेश को नमस्कार।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "To whom is homage paid in the first line of the Śārīrasthāna?",
            ("To the auspicious Gaṇeśa", "श्रीगणेशाय = to the auspicious Gaṇeśa."),
            [("To the healer Dhanvantari", "Dhanvantari is greeted in the next line, unit 2."),
             ("To Ātreya and the sages", "Ātreya is named in unit 4 as a speaker, not greeted."),
             ("To the author's own teacher", "No teacher is named in this line.")],
            "The line is श्रीगणेशाय नमः: homage to the auspicious Gaṇeśa.",
            "श्रीगणेशाय नमः = homage to the auspicious Gaṇeśa."),
        mcq("warmup", 1, "What does the word नमः mean in unit 1?",
            ("Homage", "The card glosses नमः as homage."),
            [("Name", "Name would be नाम, a different word."),
             ("Now", "Now is अथ, which opens unit 3."),
             ("Thus, in this way", "Thus is इति, which opens unit 4.")],
            "नमः = homage; the receiver of the homage stands in the dative.",
            "नमः = homage."),
        T(fill(2, "Homage to the auspicious Gaṇeśa: श्रीगणेशाय ____ (type it in Devanagari or in English letters, e.g. dharma).",
               accepts("नमः"),
               "The line is श्रीगणेशाय नमः.",
               "नमः = homage; it takes the dative of the one honoured.",
               "नमः = homage."),
          "नमः (homage) needs no verb and goes with a dative: X-आय नमः = homage to X."),
        mcq("discriminate", 3, "Which grammar label does the card give गणेशाय?",
            ("Masculine dative singular: to Gaṇeśa", "The card labels it m. dat. sg."),
            [("Masculine genitive singular: of Gaṇeśa", "The genitive would be गणेशस्य."),
             ("Masculine ablative singular: from Gaṇeśa", "The ablative would be गणेशात्."),
             ("Masculine locative singular: in Gaṇeśa", "The locative would be गणेशे.")],
            "-आय on an a-stem is the dative singular: to Gaṇeśa.",
            "गणेशाय = m. dat. sg., to Gaṇeśa."),
        multi("apply", 4, "Which statements about unit 1 are right?",
              [("It pays homage to the auspicious Gaṇeśa", "Right: श्रीगणेशाय नमः."),
               ("The one honoured stands in the dative case", "Right: गणेशाय is dative."),
               ("It states the subject of the chapter", "The subject comes in unit 3, not here."),
               ("It contains a verb meaning I bow", "No verb occurs; नमः is a noun.")],
              [0, 1],
              "The line is homage, with the honoured one in the dative, and has no verb.",
              "श्रीगणेशाय नमः = homage (noun) + dative."),
        mcq("transfer", 5, "An invented line reads शिवाय नमः, built like श्रीगणेशाय नमः. What does it mean?",
            ("Homage to Śiva", "शिवाय is dative, like गणेशाय: to Śiva."),
            [("Śiva pays homage", "Then Śiva would be nominative, शिवः."),
             ("Homage of Śiva", "Of Śiva would be the genitive शिवस्य."),
             ("Homage from Śiva", "From Śiva would be the ablative शिवात्.")],
            "Like गणेशाय, शिवाय is a dative: homage to Śiva.",
            "X-आय नमः = homage to X.",
            teaches="With नमः the one honoured takes the dative: an a-stem ends in -आय."),
    ],
}

# ---------------------------------------------------------------- unit 2
AUTHORED["2"] = {
    "title": "धन्वन्तरये नमः",
    "question": "Who is greeted in unit 2, and what form does the name take?",
    "rule": ("धन्वन्तरये नमः: homage to Dhanvantari. धन्वन्तरये is the dative singular of the i-stem धन्वन्तरि; "
             "an i-stem makes its dative in -अये."),
    "limits": ("A second invocation of two words. Dhanvantari is kept as a name; the line says nothing more about him "
               "or about the chapter."),
    "explain_hi": ("दूसरी पंक्ति भी नमस्कार है: ‘धन्वन्तरये नमः’, यानी धन्वन्तरि को नमस्कार। "
                   "‘धन्वन्तरि’ इकारान्त पुंलिंग नाम है; उसकी चतुर्थी एकवचन ‘धन्वन्तरये’ बनती है (इ → अये)। "
                   "पहली पंक्ति की तरह यहाँ भी ‘नमः’ के साथ चतुर्थी है और कोई क्रिया नहीं। "
                   "डेटा के अनुसार छपा रूप शुद्ध है।"),
    "hook": "इकारान्त + नमः: धन्वन्तरि → धन्वन्तरये नमः।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "Who is greeted with homage in unit 2?",
            ("Dhanvantari", "धन्वन्तरये = to Dhanvantari."),
            [("Gaṇeśa", "Gaṇeśa is greeted in unit 1."),
             ("Ātreya", "Ātreya is named in unit 4 as one who spoke."),
             ("The great sages", "The great sages are the speakers of unit 4.")],
            "The line is धन्वन्तरये नमः: homage to Dhanvantari.",
            "धन्वन्तरये नमः = homage to Dhanvantari."),
        mcq("warmup", 1, "What does the ending of धन्वन्तरये show?",
            ("To: the one receiving homage", "The card labels it dative singular, to Dhanvantari."),
            [("Of: the owner of something", "That would be a genitive."),
             ("By: the doer of an act", "That would be an instrumental."),
             ("In: the place of something", "That would be a locative.")],
            "धन्वन्तरये is the dative: homage goes to him.",
            "Dative = to, the receiver of homage."),
        T(fill(2, "Homage to Dhanvantari: धन्वन्तरये ____ (type it in Devanagari or in English letters, e.g. dharma).",
               accepts("नमः"),
               "The line is धन्वन्तरये नमः, the same pattern as unit 1.",
               "नमः (homage) takes the dative of the one honoured.",
               "नमः = homage."),
          "The same word नमः closes both invocations; the honoured one is dative each time."),
        mcq("discriminate", 3, "The name's base is धन्वन्तरि. Which form is its dative singular, as printed in unit 2?",
            ("धन्वन्तरये", "An i-stem makes its dative in -अये; the card calls the printed form correct."),
            [("धन्वन्तरिणा", "That is an instrumental, by Dhanvantari."),
             ("धन्वन्तरेः", "That is the genitive or ablative form."),
             ("धन्वन्तरौ", "That is the locative, in Dhanvantari.")],
            "धन्वन्तरि + dative singular = धन्वन्तरये.",
            "Masculine i-stem dative singular: -इ → -अये."),
        multi("apply", 4, "Which statements about unit 2 are right?",
              [("It greets Dhanvantari with homage", "Right: धन्वन्तरये नमः."),
               ("Its name is an i-stem in the dative", "Right: धन्वन्तरि → धन्वन्तरये."),
               ("It says who wrote the book", "No author is named here."),
               ("The printed name is marked as a misprint", "The card calls it a correct i-stem form.")],
              [0, 1],
              "The line is homage to Dhanvantari, the name in the i-stem dative, printed correctly.",
              "धन्वन्तरये = dat. sg. of धन्वन्तरि."),
        mcq("transfer", 5, "Hari is an i-stem like धन्वन्तरि. Which form completes the invented line ____ नमः, homage to Hari?",
            ("हरये", "-इ → -अये in the dative, as धन्वन्तरि → धन्वन्तरये."),
            [("हरिये", "The i-stem dative is not made by adding -ये to the base."),
             ("हरिणे", "That is not a dative of हरि."),
             ("हरेः", "That is the genitive or ablative, of or from Hari.")],
            "हरि → हरये, as धन्वन्तरि → धन्वन्तरये.",
            "Masculine i-stem dative: -अये.",
            teaches="A masculine i-stem makes its dative singular in -अये: धन्वन्तरि → धन्वन्तरये, हरि → हरये."),
    ],
}

# ---------------------------------------------------------------- unit 3
AUTHORED["3"] = {
    "title": "अथातः पुत्रकामीयं शारीरम्",
    "question": "What does unit 3 announce that the speakers will explain?",
    "rule": ("अथ अतः पुत्रकामीयम् शारीरम् व्याख्यास्यामः: now, therefore, we shall explain the putrakāmīya (relating to one "
             "who desires a son) Śārīra (relating to the body)."),
    "limits": ("The line does not contain the word chapter; that it names the chapter Putrakāmīya of the Śārīra part is "
               "the usual reading only. The short इ of the printed पुत्रकामियं is probably for long ई."),
    "explain_hi": ("यह आरम्भ-सूत्र है: ‘अब, इसलिए, हम पुत्रकामीय शारीर की व्याख्या करेंगे।’ "
                   "‘पुत्रकामीय’ का अर्थ है ‘पुत्र चाहने वाले से सम्बन्धित’, और ‘शारीर’ का अर्थ है ‘शरीर से सम्बन्धित’। "
                   "‘व्याख्यास्यामः’ भविष्यत्-काल, उत्तम पुरुष बहुवचन है: ‘हम व्याख्या करेंगे’। "
                   "पंक्ति में ‘अध्याय’ शब्द नहीं है; इसे अध्याय का नाम मानना सामान्य पठन है। "
                   "‘अथातः’ में अथ + अतः है (अ + अ → आ)।"),
    "hook": "अथ + अतः → अथातः; पुत्रकामीय शारीर की व्याख्या करेंगे।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What does unit 3 say the speakers will now explain?",
            ("The putrakāmīya Śārīra", "पुत्रकामीयम् शारीरम् व्याख्यास्यामः."),
            [("The signs of approaching death", "The line names no such subject."),
             ("The daily routine of a healthy man", "The line names no such subject."),
             ("The treatment of fever and cough", "The line names no such subject.")],
            "The line announces the putrakāmīya Śārīra: relating to one who desires a son, relating to the body.",
            "अथातः पुत्रकामीयं शारीरं व्याख्यास्यामः."),
        order(1, "Put the words of unit 3 in the line's order.",
              ["अथ", "अतः", "पुत्रकामीयम्", "शारीरम्", "व्याख्यास्यामः"],
              "Now, therefore, the putrakāmīya Śārīra, we shall explain.",
              "अथ → अतः → पुत्रकामीयम् → शारीरम् → व्याख्यास्यामः."),
        match(2, "Match each word of unit 3 to its meaning.",
              [["अथ", "now"], ["अतः", "therefore"], ["पुत्रकामीय", "relating to one who desires a son"],
               ["शारीर", "relating to the body"], ["व्याख्यास्यामः", "we shall explain"]],
              "Five words make the whole opening formula.",
              "अथ, अतः, पुत्रकामीय, शारीर, व्याख्यास्यामः.", role="extend",
              teaches="पुत्रकामीय = पुत्र (son) + काम (desire) + -ईय (relating to)."),
        mcq("discriminate", 3, "Which split of अथातः is right?",
            ("अथ + अतः", "अ + अ → आ: अथ + अतः = अथातः."),
            [("अथा + तः", "तः alone is not a word of the card."),
             ("अथः + अतः", "There is no word अथः; the particle is अथ."),
             ("अथ + आतः", "आतः is not a word of the card.")],
            "अथ (now) + अतः (therefore) join with अ + अ → आ.",
            "अ + अ → आ."),
        mcq("apply", 4, "What form does the card give व्याख्यास्यामः?",
            ("First person plural, future: we shall explain", "The card labels it 1 pl. fut."),
            [("Third person singular, present: he explains", "The label is first person plural future, not third singular present."),
             ("Second person plural, command: explain!", "No command form is labelled here."),
             ("First person plural, past: we explained", "The label is future, not past.")],
            "व्याख्यास्यामः = we shall explain, a future of the first person plural.",
            "-स्यामः = we shall (future, 1 pl.)."),
        mcq("transfer", 5, "By the rule of अथातः, how is अत्र + अस्ति (here is) written when joined?",
            ("अत्रास्ति", "अ + अ → आ, as in अथ + अतः."),
            [("अत्रेस्ति", "अ + अ does not give ए."),
             ("अत्रस्ति", "One अ is not simply dropped."),
             ("अत्रोस्ति", "अ + अ does not give ओ.")],
            "अत्र + अस्ति = अत्रास्ति, like अथ + अतः = अथातः.",
            "Short अ + short अ → long आ.",
            teaches="Two short अ sounds meeting at a word joint become one long आ."),
    ],
}

# ---------------------------------------------------------------- unit 4
AUTHORED["4"] = {
    "title": "इति ह स्माहुरात्रेयादयः",
    "question": "Who, by unit 4, said what was announced, and how is the past shown?",
    "rule": ("Thus indeed said Ātreya and the other great sages. आहुः (they said) with ह स्म is a past-time idiom; "
             "आत्रेयादयः = Ātreya and others."),
    "limits": ("The line names only Ātreya; the others are not named. It does not say where or to whom they spoke."),
    "explain_hi": ("‘इति ह स्माहुरात्रेयादयो महर्षयः’ = ऐसा आत्रेय आदि महर्षियों ने कहा। "
                   "‘आहुः’ धातु अह् का परोक्ष (लिट्) प्रथम पुरुष बहुवचन है: ‘उन्होंने कहा’; ‘ह स्म’ के साथ यह भूतकाल का मुहावरा है। "
                   "‘आत्रेयादयः’ बहुव्रीहि है: आत्रेय जिनमें पहले हैं, यानी आत्रेय आदि। "
                   "‘महर्षयः’ में महा + ऋषयः है (आ + ऋ → अर्)।"),
    "hook": "इति ह स्म आहुः = ऐसा उन्होंने कहा; आत्रेय आदि महर्षि।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 4, who said this?",
            ("Ātreya and the other great sages", "आत्रेयादयो महर्षयः."),
            [("Dhanvantari and his pupils", "Dhanvantari is greeted in unit 2, not named as speaker."),
             ("Gaṇeśa and the other gods", "Gaṇeśa is greeted in unit 1, not named as speaker."),
             ("The author alone, in his own voice", "The verb is plural: they said.")],
            "The speakers are Ātreya and others, the great sages.",
            "आत्रेयादयः महर्षयः = Ātreya and other great sages."),
        order(1, "Put the words of unit 4 in the line's order.",
              ["इति", "ह", "स्म", "आहुः", "आत्रेयादयः", "महर्षयः"],
              "Thus, indeed, (past), they said, Ātreya and others, great sages.",
              "इति → ह → स्म → आहुः → आत्रेयादयः → महर्षयः."),
        match(2, "Match each word of unit 4 to its meaning.",
              [["इति", "thus"], ["ह", "indeed"], ["आहुः", "they said"],
               ["आत्रेयादयः", "Ātreya and others"], ["महर्षयः", "great sages"]],
              "स्म is left out: it only marks past time.",
              "इति, ह, आहुः, आत्रेयादयः, महर्षयः.", role="extend",
              teaches="ह स्म with the perfect आहुः is a past-time idiom: they said."),
        mcq("discriminate", 3, "Which split of स्माहुः is right?",
            ("स्म + आहुः", "अ + आ → आ: स्म + आहुः = स्माहुः."),
            [("स्मा + हुः", "हुः is not a word of the card."),
             ("स्मः + आहुः", "स्म is a particle with no visarga."),
             ("स्म + हुः", "This loses the आ of आहुः.")],
            "स्म (past-time particle) + आहुः (they said).",
            "अ + आ → आ."),
        mcq("apply", 4, "Which split of महर्षयः is right?",
            ("महा + ऋषयः", "आ + ऋ → अर्: महा + ऋषयः = महर्षयः."),
            [("मह + र्षयः", "र्षयः is not a word."),
             ("महर् + षयः", "षयः is not a word of the card."),
             ("महा + अर्षयः", "अर्षयः is not a word; the noun is ऋषयः.")],
            "महा (great) + ऋषयः (sages): आ + ऋ gives अर्.",
            "अ/आ + ऋ → अर्."),
        mcq("transfer", 5, "By the rule of महर्षयः, how is देव + ऋषिः (divine sage) written when joined?",
            ("देवर्षिः", "अ + ऋ → अर्, as in महा + ऋषयः."),
            [("देवऋषिः", "The two vowels are joined, not left side by side."),
             ("देवार्षिः", "अ + ऋ gives अर्, not आर्."),
             ("देवरिषिः", "ऋ becomes the र् of अर्, not रि.")],
            "देव + ऋषिः = देवर्षिः, like महा + ऋषयः = महर्षयः.",
            "अ/आ + ऋ → अर्.",
            teaches="A or आ before ऋ joins into अर्: महा + ऋषयः → महर्षयः."),
    ],
}

# ---------------------------------------------------------------- unit 5
AUTHORED["5"] = {
    "title": "अथ खलु पुमानेकविंशतिवर्षः",
    "question": "In unit 5, what kind of girl does the text say a man of twenty-one should marry?",
    "rule": ("A man of twenty-one should marry by blameless rule a girl of unlike gotra and ancestry, of a family without "
             "transmitted disease, sound in body, neither tawny nor reddish-brown, of about twelve years, not bearing "
             "frightening names, faultless."),
    "limits": ("The card reports what this classical text states and gives no present-day advice. Unit 6 gives sixteen "
               "for the woman; the two are not reconciled. Doubtful: the sense of असंचारिरोगकुल, the reading of मृदु-अरोग-प्रकृति, "
               "and how the name-list splits. No question uses them."),
    "explain_hi": ("यह एक लम्बा गद्य-वाक्य है: कर्ता ‘पुमान्’ (इक्कीस वर्ष का पुरुष) है और क्रिया अन्त में ‘उद्वहेत्’ (ब्याहे)। "
                   "बीच में कन्या के गुणों की लम्बी सूची है: असमान गोत्र और वंश की, ऐसे कुल की जिसमें रोग संचारी न हो, "
                   "रूप-शील-लक्षण से सम्पन्न, दाँत-होंठ-कान-नख-केश-स्तन अक्षत, न कपिला न पिंगला, अंग न कम न अधिक, लगभग बारह वर्ष की, "
                   "और देवता, सर्प, नदी, वृक्ष, पक्षी, नक्षत्र जैसे नाम न रखने वाली। "
                   "‘देशीय’ का अर्थ है ‘लगभग’। अनेक गुण निषेधवाचक ‘अ-/अन्-’ से बने हैं (अकपिला, अनघा)। "
                   "यह प्राचीन ग्रन्थ का कथन है; अगली इकाई में स्त्री की आयु सोलह कही गई है।"),
    "hook": "इक्कीस का पुरुष, लम्बी गुण-सूची, अन्त में क्रिया: उद्वहेत्।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 5, what is the age of the man who should marry?",
            ("Twenty-one years", "एकविंशतिवर्षः = of twenty-one years."),
            [("Twenty-five years", "Twenty-five is the man's age in unit 6."),
             ("Sixteen years", "Sixteen is the woman's age in unit 6."),
             ("Twelve years", "About twelve is said of the girl, not the man.")],
            "पुमान् एकविंशतिवर्षः: a man of twenty-one years.",
            "एक + विंशति = twenty-one."),
        order(1, "Put these descriptions of the girl in unit 5 in the text's order.",
              ["अतुल्यगोत्राम्", "रूपशीललक्षणसंपन्नाम्", "अकपिलाम्", "द्वादशवर्षदेशीयाम्", "अनघाम्"],
              "Gotra comes first, then beauty and conduct, then colour, then age, and faultless near the end.",
              "गोत्र → रूप-शील-लक्षण → अकपिला → द्वादशवर्षदेशीया → अनघा."),
        match(2, "Match each word of unit 5 to its meaning.",
              [["अतुल्यगोत्राम्", "of unlike gotra"], ["अकपिलाम्", "not tawny"],
               ["अहीनाधिकाङ्गीम्", "with limbs neither deficient nor in excess"],
               ["द्वादशवर्षदेशीयाम्", "of about twelve years"], ["अनघाम्", "faultless"]],
              "All are feminine accusatives describing the girl (कन्याम्).",
              "अतुल्यगोत्रा, अकपिला, अहीनाधिकाङ्गी, द्वादशवर्षदेशीया, अनघा.", role="extend",
              teaches="Many qualities are negatives: अ- before a consonant (अकपिला), अन्- before a vowel (अनघा)."),
        mcq("discriminate", 3, "In द्वादशवर्षदेशीयाम्, what does देशीय add to twelve years?",
            ("About, approximately", "The card glosses देशीय as approximately."),
            [("Exactly, no more or less", "That would remove the sense of देशीय."),
             ("At least, or older", "No word for at least is present."),
             ("Of the same country", "Here देशीय is glossed approximately, not country.")],
            "द्वादशवर्षदेशीया = of about twelve years.",
            "देशीय after a number = approximately."),
        multi("apply", 4, "Which does unit 5 say of the girl?",
              [("Her teeth, lips, ears, nails and hair are undamaged", "Right: अविनष्ट-दन्त-ओष्ठ-कर्ण-नख-केश..."),
               ("She is not reddish-brown", "Right: अपिङ्गलाम्."),
               ("She is of the same gotra as the man", "The text says अतुल्यगोत्राम्, of unlike gotra."),
               ("She bears the name of a river", "The text says she does not bear such names (अनुद्वहन्तीम्).")],
              [0, 1],
              "Undamaged teeth, lips and the rest, and not reddish-brown, are both in the list.",
              "अविनष्ट...; अपिङ्गला; अतुल्यगोत्रा; नामानि अनुद्वहन्ती."),
        mcq("transfer", 5, "Negatives in unit 5 use अन्- before a vowel, as अनघा. What is the negative of उचित (proper)?",
            ("अनुचित", "अन्- before the vowel उ: अनुचित."),
            [("अउचित", "अ- is not used before a vowel."),
             ("अचित", "The उ of उचित cannot be lost."),
             ("नौचित", "No such negative form exists here.")],
            "अन् + उचित = अनुचित, like अन् + अघा = अनघा.",
            "Negative prefix: अ- before a consonant, अन्- before a vowel.",
            teaches="The negative prefix is अ- before a consonant (अकपिला) and अन्- before a vowel (अनघा, अनूना)."),
    ],
}

# ---------------------------------------------------------------- unit 6
AUTHORED["6"] = {
    "title": "तस्यां षोडशवर्षीयाम्",
    "question": "By unit 6, at what ages should a man strive for a son, and in whom?",
    "rule": ("In her, of sixteen years, a man of twenty-five years should strive for the sake of a son. तस्याम् "
             "(in her, locative) points back to the girl of unit 5."),
    "limits": ("The ages are as printed. Unit 5 says the girl is about twelve at marriage; this unit says sixteen. "
               "The text does not reconcile the two, and the card does not either. No present-day advice is given."),
    "explain_hi": ("इस वाक्य में दो आयु हैं: स्त्री सोलह वर्ष की (षोडशवर्षीया) और पुरुष पच्चीस वर्ष का (पञ्चविंशतिवर्षः)। "
                   "क्रिया ‘प्रयतेत’ (प्रयत्न करे) विधिलिङ् है, और उद्देश्य ‘पुत्रार्थम्’ यानी पुत्र के लिए। "
                   "‘तस्याम्’ सप्तमी है: ‘उसमें’, जो पिछली इकाई की कन्या की ओर संकेत करता है। "
                   "पिछली इकाई में बारह वर्ष कहा गया था; ग्रन्थ दोनों को मिलाकर नहीं समझाता।"),
    "hook": "सोलह की स्त्री, पच्चीस का पुरुष: पुत्रार्थं प्रयतेत।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 6, what is the man's age when he should strive for a son?",
            ("Twenty-five years", "पञ्चविंशतिवर्षः = of twenty-five years."),
            [("Twenty-one years", "Twenty-one is the man's age at marriage in unit 5."),
             ("Sixteen years", "Sixteen is the woman's age in this unit."),
             ("Thirty years or more", "Thirty is not named.")],
            "पञ्चविंशतिवर्षः पुरुषः: a man of twenty-five years.",
            "पञ्चविंशति = twenty-five."),
        order(1, "Put the words of unit 6 in the line's order.",
              ["तस्याम्", "षोडशवर्षीयाम्", "पञ्चविंशतिवर्षः", "पुरुषः", "पुत्रार्थम्", "प्रयतेत"],
              "In her, of sixteen, a man of twenty-five, for a son, should strive.",
              "तस्याम् → षोडशवर्षीयाम् → पञ्चविंशतिवर्षः → पुरुषः → पुत्रार्थम् → प्रयतेत."),
        match(2, "Match each word of unit 6 to its meaning.",
              [["तस्याम्", "in her"], ["षोडश", "sixteen"], ["पञ्चविंशति", "twenty-five"],
               ["पुत्रार्थम्", "for the sake of a son"], ["प्रयतेत", "should strive"]],
              "Two numbers, one purpose, one verb and the pointer तस्याम्.",
              "तस्याम्, षोडश, पञ्चविंशति, पुत्रार्थम्, प्रयतेत.", role="extend",
              teaches="X + अर्थम् = for the sake of X: पुत्र + अर्थम् → पुत्रार्थम्."),
        mcq("discriminate", 3, "What case does the card give तस्याम्, and what does it mean?",
            ("Locative: in her", "The card labels it f. loc. sg., in her."),
            [("Genitive: of her", "Of her would be तस्याः."),
             ("Nominative: she", "She would be सा."),
             ("Instrumental: by her", "By her would be तया.")],
            "तस्याम् = in her, the girl of unit 5.",
            "तस्याम् = f. loc. sg."),
        multi("apply", 4, "Which are stated in unit 6?",
              [("The woman is sixteen years old", "Right: षोडशवर्षीयाम्."),
               ("The man is twenty-five years old", "Right: पञ्चविंशतिवर्षः."),
               ("The aim is a son", "Right: पुत्रार्थम्."),
               ("The marriage takes place at sixteen", "Marriage is the subject of unit 5, not this unit."),
               ("The man is twenty-one years old", "Twenty-one belongs to unit 5.")],
              [0, 1, 2],
              "Unit 6 gives the two ages and the aim; marriage is not mentioned here.",
              "षोडश, पञ्चविंशति, पुत्रार्थम्."),
        mcq("transfer", 5, "Built like पुत्रार्थम्, which word means for the sake of dharma?",
            ("धर्मार्थम्", "धर्म + अर्थम्, अ + अ → आ, as in पुत्र + अर्थम्."),
            [("धर्मअर्थम्", "The two vowels must join."),
             ("धर्मेर्थम्", "अ + अ does not give ए."),
             ("धर्मोर्थम्", "अ + अ does not give ओ.")],
            "धर्म + अर्थम् = धर्मार्थम्, for the sake of dharma.",
            "X + अर्थम् = for the sake of X.",
            teaches="अर्थम् after a noun means for the sake of it, and अ + अ joins to आ."),
    ],
}

# ---------------------------------------------------------------- unit 7
AUTHORED["7"] = {
    "title": "तदा हि तौ प्राप्तवीर्यौ",
    "question": "Why, by unit 7, are those ages chosen?",
    "rule": ("For then those two, having attained potency (वीर्य), beget offspring endowed with potency. तौ and जनयतः "
             "are dual: the two of them."),
    "limits": ("The card renders वीर्य as potency (vigour); the line does not say semen. तदा (then) is read as the time of "
               "the ages in unit 6."),
    "explain_hi": ("यह पिछली बात का कारण बताता है (‘हि’ = क्योंकि): तब वे दोनों वीर्य यानी शक्ति को प्राप्त हुए होते हैं, "
                   "और शक्ति से युक्त सन्तान को जन्म देते हैं। "
                   "‘तौ’ और ‘जनयतः’ द्विवचन हैं: दो व्यक्ति, स्त्री और पुरुष। "
                   "डेटा में यहाँ ‘वीर्य’ का अर्थ शक्ति रखा गया है, शुक्र नहीं। "
                   "‘वीर्यान्वितम्’ में वीर्य + अन्वितम् है (अ + अ → आ)।"),
    "hook": "शक्ति पाए हुए दोनों, शक्तिमान सन्तान: वीर्यान्वितम् अपत्यम्।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 7, what kind of offspring do the two beget?",
            ("Offspring endowed with potency", "वीर्यान्वितम् अपत्यम्."),
            [("Offspring of short life", "Short life is said of the too-young parents in unit 8."),
             ("Offspring of unlike gotra", "Gotra is spoken of in unit 5, about the girl."),
             ("Offspring with weak senses", "Weak senses come in unit 8, not here.")],
            "They beget offspring endowed with potency (वीर्यान्वित).",
            "वीर्य + अन्वित = endowed with potency."),
        order(1, "Put the words of unit 7 in the line's order.",
              ["तदा", "हि", "तौ", "प्राप्तवीर्यौ", "वीर्यान्वितम्", "अपत्यम्", "जनयतः"],
              "Then, for, those two, having attained potency, potent offspring, beget.",
              "तदा → हि → तौ → प्राप्तवीर्यौ → वीर्यान्वितम् → अपत्यम् → जनयतः."),
        match(2, "Match each word of unit 7 to its meaning.",
              [["तदा", "then"], ["हि", "for"], ["तौ", "those two"], ["अपत्य", "offspring"],
               ["जनयतः", "the two beget"]],
              "हि gives the reason; तौ and जनयतः are dual.",
              "तदा, हि, तौ, अपत्य, जनयतः.", role="extend",
              teaches="हि gives a reason (for); a dual subject takes a dual verb: तौ ... जनयतः."),
        mcq("discriminate", 3, "Which number do तौ and जनयतः show by the card's labels?",
            ("Dual: those two, they two beget", "Both are labelled du."),
            [("Singular: he begets", "He would be सः, with जनयति."),
             ("Plural: they all beget", "They all would be ते, with जनयन्ति."),
             ("One dual, one plural", "Both carry the dual label.")],
            "Subject and verb are both dual: the man and the woman.",
            "तौ = m. nom. du.; जनयतः = 3 du."),
        mcq("apply", 4, "How does the card render वीर्य in unit 7?",
            ("Potency, vigour", "The note says potency, not semen."),
            [("Semen", "The card notes the text does not say semen here."),
             ("A weapon", "The card gives no such sense."),
             ("A medicine or drug", "The card gives no such sense.")],
            "वीर्य = potency (vigour) on this card.",
            "वीर्य here = potency."),
        mcq("transfer", 5, "Built like वीर्यान्वितम्, which word means endowed with strength?",
            ("बलान्वितम्", "बल + अन्वितम्, अ + अ → आ."),
            [("बलअन्वितम्", "The two vowels must join."),
             ("बलेन्वितम्", "अ + अ does not give ए."),
             ("बलोन्वितम्", "अ + अ does not give ओ.")],
            "बल + अन्वितम् = बलान्वितम्, like वीर्य + अन्वितम्.",
            "X + अन्वित = endowed with X.",
            teaches="अन्वित after a noun means endowed with it: वीर्यान्वित = endowed with potency."),
    ],
}

# ---------------------------------------------------------------- unit 8
AUTHORED["8"] = {
    "title": "ऊनपञ्चविंशतिवर्षेण",
    "question": "What does unit 8 say may happen to an embryo placed when the parents are too young?",
    "rule": ("An embryo placed by a man of less than twenty-five in a woman of less than sixteen may perish, or be of short "
             "life with little strength, health and means, or with defective senses."),
    "limits": ("Low confidence. कुक्षिस्य (read कुक्षिस्थः, in the womb) and विक्लेंद्रिय (read विकलेन्द्रिय) are corrections; "
               "the end (ऋतु, first three nights, vitiated, शुक्रार्तवहति) is unclear and its sense is not stated. Questions use only "
               "the sure first part."),
    "explain_hi": ("यह इकाई चेतावनी देती है: पच्चीस से कम आयु के पुरुष द्वारा सोलह से कम आयु की स्त्री में स्थापित गर्भ "
                   "नष्ट हो सकता है, या अल्पायु, कम बल-आरोग्य-विभव वाला, या विकल इन्द्रियों वाला हो सकता है। "
                   "‘ऊन’ का अर्थ है ‘कम’ (इकाई 5 के ‘देशीय’ = लगभग से भिन्न)। "
                   "‘आहितो गर्भः’ में आहितः + गर्भः है: घोष व्यंजन से पहले अः → ओ। "
                   "वाक्य का अन्तिम भाग (ऋतु की पहली तीन रातें, दूषित होना, ‘शुक्रार्तवहति’) अस्पष्ट है और यहाँ उस पर कुछ नहीं पूछा गया।"),
    "hook": "ऊन = कम: पच्चीस से कम और सोलह से कम, तो गर्भ को हानि।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 8, what may happen to an embryo placed by a man under twenty-five in a woman under sixteen?",
            ("It may perish", "विनाशम् आप्नुयात्: it may reach destruction."),
            [("It may become twins", "Twins are not mentioned."),
             ("It may be born early but strong", "The unit lists only harms."),
             ("It may live especially long", "The unit says the opposite: short life.")],
            "The first outcome is destruction (विनाश).",
            "विनाशम् आप्नुयात् = may perish."),
        order(1, "Put these words of unit 8 in the line's order.",
              ["ऊनपञ्चविंशतिवर्षेण", "ऊनषोडशवर्षीयाम्", "आहितः", "गर्भः", "विनाशम्", "आप्नुयात्"],
              "By one under twenty-five, in one under sixteen, placed, the embryo, destruction, may reach.",
              "पुरुष → स्त्री → आहितः गर्भः → विनाशम् आप्नुयात्."),
        match(2, "Match each word of unit 8 to its meaning.",
              [["ऊन", "less than"], ["विनाश", "destruction"], ["अल्पायुः", "of short life-span"],
               ["बल", "strength"], ["आरोग्य", "health"]],
              "These words carry the sure first part of the sentence.",
              "ऊन, विनाश, अल्पायुः, बल, आरोग्य.", role="extend",
              teaches="ऊन before a number means less than it: ऊनषोडशवर्षीया = of less than sixteen years."),
        mcq("discriminate", 3, "In ऊनपञ्चविंशतिवर्षेण, what does ऊन add to twenty-five years?",
            ("Less than", "The card glosses ऊन as less than."),
            [("More than", "No word for more than is present."),
             ("About, approximately", "That is देशीय of unit 5, not ऊन."),
             ("Exactly", "ऊन changes the number; it does not fix it.")],
            "ऊनपञ्चविंशतिवर्ष = of less than twenty-five years.",
            "ऊन = less than; देशीय = about."),
        multi("apply", 4, "Which outcomes are named in the sure first part of unit 8?",
              [("Destruction of the embryo", "Right: विनाशम् आप्नुयात्."),
               ("Short life-span", "Right: अल्पायुः."),
               ("Little strength, health and means", "Right: अल्प- with बल, आरोग्य, विभव."),
               ("Birth of a girl instead of a boy", "Not named in the unit."),
               ("Birth of twins", "Not named in the unit.")],
              [0, 1, 2],
              "The sure outcomes are destruction, or short life with little strength, health and means.",
              "विनाश; अल्प-आयुः-बल-आरोग्य-विभव."),
        mcq("transfer", 5, "By the rule of आहितो गर्भः, how is रामः + गच्छति (Rāma goes) written?",
            ("रामो गच्छति", "अः before a voiced consonant → ओ, as आहितः + गर्भः → आहितो गर्भः."),
            [("रामः गच्छति", "The visarga does not stay before a voiced sound."),
             ("रामर् गच्छति", "अः does not become अर् here."),
             ("रामा गच्छति", "अः does not become आ.")],
            "रामः + गच्छति = रामो गच्छति, like आहितः + गर्भः = आहितो गर्भः.",
            "अः + voiced consonant → ओ.",
            teaches="A final अः before a voiced consonant becomes ओ: आहितः गर्भः → आहितो गर्भः."),
    ],
}

# ---------------------------------------------------------------- unit 9
AUTHORED["9"] = {
    "title": "आहारस्य सारः शुक्रसंज्ञां लभते",
    "question": "By unit 9, what part of food gets the name śukra?",
    "rule": ("The essence (सार) of food that is well transformed and has, in order (क्रमात्), reached the marrow obtains "
             "the name śukra (semen)."),
    "limits": ("The line does not name the stages between food and marrow. मज्जन् = marrow is probable (the body tissue). "
               "तत्र (there) is not explained."),
    "explain_hi": ("यह इकाई शुक्र की उत्पत्ति बताती है: भोजन जब भली-भाँति परिणत (पच) होकर क्रम से मज्जा तक पहुँचता है, "
                   "तब उसका सार ‘शुक्र’ नाम पाता है। "
                   "‘क्रमात्’ = क्रम से; बीच के चरण इस पंक्ति में गिनाए नहीं गए हैं। "
                   "‘शुक्रसंज्ञाम्’ = शुक्र नाम; ‘लभते’ = पाता है। "
                   "‘क्रमान्मज्जानम्’ में क्रमात् + मज्जानम् है: अनुनासिक से पहले त् → न्।"),
    "hook": "भोजन → भली-भाँति पचा → क्रम से मज्जा तक → सार = शुक्र।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 9, what obtains the name śukra?",
            ("The essence of well-digested food that has reached the marrow", "आहारस्य ... सारः शुक्रसंज्ञां लभते."),
            [("The blood that flows each month for three days", "That is ārtava, in unit 11."),
             ("The whole of the food eaten that day", "Only its essence (सार) is named."),
             ("The waste left over from undigested food", "The food is well transformed (सम्यक्परिणत).")],
            "The essence (सार) of food, well transformed and reaching the marrow, is called śukra.",
            "सार = essence; शुक्रसंज्ञा = the name śukra."),
        order(1, "Put the stages of unit 9 in the line's order.",
              ["आहारस्य", "सम्यक्परिणतस्य", "क्रमात्", "मज्जानमनुप्राप्तस्य", "सारः", "शुक्रसंज्ञां लभते"],
              "Food, well transformed, in order, reaching the marrow; its essence gets the name śukra.",
              "आहार → परिणत → क्रमात् → मज्जा → सार → शुक्र."),
        match(2, "Match each word of unit 9 to its meaning.",
              [["आहार", "food"], ["परिणत", "transformed, digested"], ["मज्जन्", "marrow"],
               ["सार", "essence"], ["संज्ञा", "name"]],
              "These words carry the whole chain of unit 9.",
              "आहार, परिणत, मज्जन्, सार, संज्ञा.", role="extend",
              teaches="संज्ञां लभते = obtains the name: the line defines a term."),
        mcq("discriminate", 3, "Which split of क्रमान्मज्जानम् is right?",
            ("क्रमात् + मज्जानम्", "त् before the nasal म becomes न्."),
            [("क्रमम् + मज्जानम्", "That would be written क्रमं मज्जानम्; the card has the ablative क्रमात्."),
             ("क्रमः + मज्जानम्", "A visarga would give क्रमो मज्जानम्."),
             ("क्रमा + न्मज्जानम्", "न्मज्जानम् is not a word.")],
            "क्रमात् (in order) + मज्जानम् (marrow): त् → न् before a nasal.",
            "Final त् + nasal → न् + nasal."),
        mcq("apply", 4, "By unit 9, which tissue has the food reached when its essence is named śukra?",
            ("Marrow (मज्जन्)", "मज्जानम् अनुप्राप्तस्य: having reached the marrow."),
            [("Blood (रक्त)", "Blood is not named in unit 9."),
             ("Flesh (मांस)", "Flesh is not named in unit 9."),
             ("Flesh and fat (मांस, मेदस्)", "Neither is named in unit 9.")],
            "The line names only the marrow as the point reached.",
            "मज्जानम् अनुप्राप्त = having reached the marrow."),
        mcq("transfer", 5, "By the rule of क्रमान्मज्जानम्, how is जगत् + नाथः (lord of the world) written?",
            ("जगन्नाथः", "त् before the nasal न becomes न्."),
            [("जगत्नाथः", "त् does not stay before a nasal."),
             ("जगद्नाथः", "Before a nasal it goes further, to न्."),
             ("जगनाथः", "The consonant is not lost; it becomes न्.")],
            "जगत् + नाथः = जगन्नाथः, like क्रमात् + मज्जानम् = क्रमान्मज्जानम्.",
            "Final त् + nasal → न्.",
            teaches="A final त् before a nasal (न, म) becomes न्: क्रमात् मज्जानम् → क्रमान्मज्जानम्."),
    ],
}

# ---------------------------------------------------------------- unit 10
AUTHORED["10"] = {
    "title": "गर्भाधानयोग्यं शुक्रम्",
    "question": "By unit 10, where does śukra abide, and what qualities make it fit for conception?",
    "rule": ("Śukra pervades the body, especially marrow, testicles and breasts; stirred, it issues from limb to limb. Gentle, "
             "unctuous, heavy, white, honey-scented, sweet, slimy, abundant, thick, of ghee, oil or honey colour, it is fit for conception."),
    "limits": ("Low confidence for the first sentence. The similes (ghee in milk, jaggery in sugarcane juice) rest on corrections; "
               "संप्रहन (probably union) and हृदयावेश are interpretations; कला is a doctrinal term. Questions use the list of "
               "qualities and the named sites only."),
    "explain_hi": ("पहला वाक्य बताता है कि शुक्र शरीर में कैसे रहता है: शुक्रधरा कला के आश्रय से सब अंगों में व्याप्त, और विशेषकर मज्जा, "
                   "मुष्क (वृषण) और स्तनों में; हर्ष से प्रेरित होकर, पिण्ड बनकर अंग-अंग से निकलता है। "
                   "इस वाक्य की उपमाएँ (दूध में घी, ईख के रस में गुड़) पाठ-सुधार पर टिकी हैं, इसलिए उन पर प्रश्न नहीं। "
                   "दूसरा वाक्य स्पष्ट है: सौम्य, स्निग्ध, गुरु, शुक्ल, मधु-गन्ध, मधुर, पिच्छिल, बहु, बहल, और घी, तेल या शहद में से "
                   "किसी एक के रंग का शुक्र गर्भाधान के योग्य होता है।"),
    "hook": "गर्भाधान-योग्य शुक्र: सौम्य, स्निग्ध, गुरु, शुक्ल, मधु-गन्धि, मधुर, पिच्छिल, बहु, बहल; रंग घी-तेल-मधु।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 10, śukra with the listed qualities becomes fit for what?",
            ("Conception (गर्भाधान)", "गर्भाधानयोग्यं भवति."),
            [("Digestion of food", "The card names no such use."),
             ("Healing of wounds", "The card names no such use."),
             ("Nourishing the eyes and hair", "The card names no such use.")],
            "Śukra with these qualities becomes fit for conception (garbhādhāna).",
            "गर्भाधानयोग्य = fit for conception."),
        order(1, "Put the first six qualities of fit śukra in unit 10's order.",
              ["सौम्यम्", "स्निग्धम्", "गुरु", "शुक्लम्", "मधुगन्धि", "मधुरम्"],
              "The list begins: gentle, unctuous, heavy, white, honey-scented, sweet.",
              "सौम्य → स्निग्ध → गुरु → शुक्ल → मधुगन्धि → मधुर."),
        match(2, "Match each quality of fit śukra in unit 10 to its meaning.",
              [["स्निग्ध", "unctuous"], ["गुरु", "heavy"], ["शुक्ल", "white"],
               ["पिच्छिल", "slimy"], ["बहल", "thick, dense"]],
              "All five are in the second sentence, the list of qualities.",
              "स्निग्ध, गुरु, शुक्ल, पिच्छिल, बहल.", role="extend",
              teaches="The qualities are neuter nominatives agreeing with शुक्रम्."),
        mcq("discriminate", 3, "Which colours does unit 10 allow for fit śukra?",
            ("That of ghee, oil or honey", "घृततैलक्षौद्रान्यतमवर्णम्: any one of these."),
            [("That of milk, ghee or water", "Milk and water are not in the colour list."),
             ("That of oil, blood or honey", "Blood is not in the colour list."),
             ("That of jaggery, honey or milk", "Jaggery and milk are not in the colour list.")],
            "The colour is that of any one of ghee, oil or honey (क्षौद्र).",
            "घृत, तैल, क्षौद्र: अन्यतम-वर्ण."),
        multi("apply", 4, "Where, by unit 10, does śukra abide especially?",
              [("In the marrow (मज्जा)", "Right: मज्ज-."),
               ("In the testicles (मुष्क)", "Right: -मुष्क-."),
               ("In the breasts (स्तन)", "Right: -स्तनेषु."),
               ("In the eyes", "The eyes are not named here."),
               ("In the feet", "The feet are not named here.")],
              [0, 1, 2],
              "विशेषतश्च मज्जमुष्कस्तनेषु: especially in marrow, testicles and breasts.",
              "मज्जा, मुष्क, स्तन."),
        mcq("transfer", 5, "Built like मधुगन्धि (honey-scented), what does the invented word पुष्पगन्धि mean?",
            ("Smelling of flowers", "पुष्प + गन्धि, as मधु + गन्धि = smelling of honey."),
            [("A flower with no smell", "No word for without is present."),
             ("Coloured like a flower", "गन्धि is smell, not colour (वर्ण)."),
             ("Sweet as a flower's honey", "No word for sweet is present.")],
            "X + गन्धि = smelling of X.",
            "मधुगन्धि = honey-scented.",
            teaches="X-गन्धि (a compound ending in गन्धि) describes something that smells of X."),
    ],
}

# ---------------------------------------------------------------- unit 11
AUTHORED["11"] = {
    "title": "आर्तवमित्याहुः",
    "question": "What, by unit 11, is called ārtava?",
    "rule": ("Likewise, women's blood itself, month by month, having reached the garbhakoṣṭha (probably the womb), "
             "flowing for three days, is called ārtava (menstrual blood)."),
    "limits": ("गर्भकोष्ठ = womb is probable (literally the store-room of the embryo). The line gives three days and month by "
               "month only; it says nothing of irregular cases here."),
    "explain_hi": ("इस इकाई में आर्तव की परिभाषा है: स्त्रियों का रक्त ही, हर मास गर्भकोष्ठ (सम्भवतः गर्भाशय) तक पहुँचकर, "
                   "तीन दिन बहता हुआ, ‘आर्तव’ कहलाता है। "
                   "‘तथा’ का अर्थ है ‘इसी प्रकार’। "
                   "‘त्र्यहम्’ = तीन दिन; ‘मासे मासे’ = हर महीने। "
                   "‘आर्तवमित्याहुः’ में आर्तवम् + इति + आहुः है (इ + आ → या)।"),
    "hook": "स्त्री का रक्त, हर मास, गर्भकोष्ठ तक, तीन दिन: आर्तव।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 11, for how long does the blood called ārtava flow?",
            ("Three days", "त्र्यहं प्रवर्तमानम्: flowing for three days."),
            [("Five days", "The line gives three days."),
             ("Seven days and nights", "The line gives three days."),
             ("One day", "The line gives three days.")],
            "त्र्यहम् = three days.",
            "त्रि + अह = three days."),
        order(1, "Put the phrases of unit 11 in the line's order.",
              ["रक्तमेव च स्त्रीणाम्", "मासे मासे", "गर्भकोष्ठमनुप्राप्य", "त्र्यहं प्रवर्तमानम्", "आर्तवमित्याहुः"],
              "Women's blood, month by month, reaching the garbhakoṣṭha, flowing three days, they call ārtava.",
              "रक्त → मासे मासे → गर्भकोष्ठ → त्र्यहम् → आर्तव."),
        match(2, "Match each word of unit 11 to its meaning.",
              [["मासे मासे", "month by month"], ["गर्भकोष्ठ", "womb (probable)"], ["त्र्यहम्", "for three days"],
               ["प्रवर्तमान", "flowing"], ["आर्तव", "menstrual blood"]],
              "These words make the definition.",
              "मासे मासे, गर्भकोष्ठ, त्र्यहम्, प्रवर्तमान, आर्तव.", role="extend",
              teaches="A repeated locative (मासे मासे) means every one: every month."),
        mcq("discriminate", 3, "Which split of आर्तवमित्याहुः is right?",
            ("आर्तवम् + इति + आहुः", "इ + आ → या: इति + आहुः = इत्याहुः."),
            [("आर्तवम् + इत्य + आहुः", "इत्य is not a word of the card."),
             ("आर्तवमि + त्याहुः", "Neither part is a word."),
             ("आर्तवम् + इत् + याहुः", "याहुः is not a word.")],
            "आर्तवम् (ārtava) + इति (thus) + आहुः (they say).",
            "इ + a different vowel → य् + that vowel."),
        mcq("apply", 4, "By unit 11, what must women's blood do before it is called ārtava?",
            ("Reach the garbhakoṣṭha and flow three days", "गर्भकोष्ठम् अनुप्राप्य त्र्यहं प्रवर्तमानम्."),
            [("Reach the marrow and become essence", "That is the account of śukra, unit 9."),
             ("Become a lump and issue from the limbs", "That is said of śukra, unit 10."),
             ("Mix with the essence of food for a month", "No such step is named.")],
            "The blood reaches the garbhakoṣṭha monthly and flows three days.",
            "गर्भकोष्ठ + त्र्यहम् = ārtava."),
        mcq("transfer", 5, "By the rule of इत्याहुः, how is प्रति + आगच्छति (comes back) written?",
            ("प्रत्यागच्छति", "इ + आ → या, as in इति + आहुः."),
            [("प्रतिआगच्छति", "The vowels must join."),
             ("प्रत्यगच्छति", "The long आ is kept: या, not य."),
             ("प्रतेगच्छति", "इ + आ does not give ए.")],
            "प्रति + आगच्छति = प्रत्यागच्छति.",
            "इ + आ → या.",
            teaches="A final इ before another vowel becomes य्: इति + आहुः → इत्याहुः."),
    ],
}

# ---------------------------------------------------------------- unit 12
AUTHORED["12"] = {
    "title": "अतिप्रसङ्गेनानृतावृतौ",
    "question": "By unit 12, what names does ārtava take when it goes on excessively?",
    "rule": ("Through excessive continuation (अतिप्रसङ्ग), out of season or in season, that very ārtava takes the names "
             "asṛgdara, pradara (both probable as abnormal bleeding or discharge), vyāpad (disorder) and raktayoni."),
    "limits": ("Medium confidence. The printed वातदेवा सृग्दरं is re-split as वा तद् एवासृग्दरम्. Asṛgdara and pradara are "
               "probable identifications whose use varies; the exact grammar of the names is not certain. No question rests on असृग्दर."),
    "explain_hi": ("पिछली इकाई का आर्तव (‘तद्’ = वही) जब अतिप्रसङ्ग से, ऋतु के बाहर या ऋतु में, बढ़ता है, तो उसे कई नाम मिलते हैं: "
                   "असृग्दर, प्रदर (दोनों सम्भवतः अधिक रक्तस्राव या असामान्य स्राव), व्यापद् (विकार), और रक्तयोनि। "
                   "‘अनृतावृतौ’ में अनृतौ + ऋतौ है: औ स्वर से पहले आव् बनता है। "
                   "‘असृग्दर’ वाला भाग छपे पाठ के पुनर्विभाजन पर टिका है।"),
    "hook": "अति बहे तो नाम: असृग्दर, प्रदर, व्यापद्, रक्तयोनि।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 12, through what does ārtava take these new names?",
            ("Excessive continuation (अतिप्रसङ्ग)", "अतिप्रसङ्गेन: by excessive continuation."),
            [("Cold food and drink", "No food is named."),
             ("Grief, fear and sleeplessness at night", "None of these is named."),
             ("Old age", "No age is named here.")],
            "The cause named is अतिप्रसङ्ग, excessive continuation.",
            "अतिप्रसङ्गेन = through excessive continuation."),
        order(1, "Put these words of unit 12 in the line's order.",
              ["अतिप्रसङ्गेन", "अनृतौ", "ऋतौ", "प्रदरम्", "रक्तयोनिसंज्ञाम्", "लभते"],
              "Cause, out of season, in season, the names, obtains.",
              "अतिप्रसङ्गेन → अनृतौ → ऋतौ → ... प्रदरम् ... → रक्तयोनिसंज्ञाम् → लभते."),
        match(2, "Match each word of unit 12 to its meaning.",
              [["अतिप्रसङ्ग", "excessive continuation"], ["अनृतौ", "out of season"], ["ऋतौ", "in season"],
               ["व्यापद्", "disorder"], ["लभते", "obtains"]],
              "Cause, the two times, one of the names, and the verb.",
              "अतिप्रसङ्ग, अनृतौ, ऋतौ, व्यापद्, लभते.", role="extend",
              teaches="अन्- negates ऋतु: अनृतौ = out of season, beside ऋतौ = in season."),
        mcq("discriminate", 3, "Which split of अनृतावृतौ is right?",
            ("अनृतौ + ऋतौ", "औ before a vowel becomes आव्: अनृतौ + ऋतौ = अनृतावृतौ."),
            [("अनृता + वृतौ", "वृतौ is not a word of the card."),
             ("अनृत + आवृतौ", "आवृतौ is not a word of the card."),
             ("अनृतः + ऋतौ", "A visarga would not give आव्.")],
            "अनृतौ (out of season) + ऋतौ (in season).",
            "औ + vowel → आव् + vowel."),
        multi("apply", 4, "Which names does unit 12 say ārtava obtains?",
              [("प्रदर", "Right: प्रदरम्."),
               ("व्यापद्", "Right: व्यापदम्."),
               ("रक्तयोनि", "Right: रक्तयोनिसंज्ञाम्."),
               ("रक्तपित्त", "Raktapitta is named in unit 13 as a treatment to consult."),
               ("शुक्र", "Śukra is the name of the essence of food, unit 9.")],
              [0, 1, 2],
              "Pradara, vyāpad and raktayoni are named (asṛgdara too, on the re-split reading).",
              "प्रदर, व्यापद्, रक्तयोनि."),
        mcq("transfer", 5, "By the rule of अनृतावृतौ, how is गुरौ + इति written when joined?",
            ("गुराविति", "औ + vowel → आव्: गुरौ + इति = गुराविति."),
            [("गुरौइति", "The vowels must join."),
             ("गुरविति", "औ gives आव्, with long आ."),
             ("गुरेति", "औ + इ does not give ए.")],
            "गुरौ + इति = गुराविति, like अनृतौ + ऋतौ = अनृतावृतौ.",
            "औ + vowel → आव्.",
            teaches="A final औ before a vowel becomes आव्: अनृतौ + ऋतौ → अनृतावृतौ."),
    ],
}

# ---------------------------------------------------------------- unit 13
AUTHORED["13"] = {
    "title": "तत्साधने रक्तपित्तचिकित्सितम्",
    "question": "In managing it, which two treatments does unit 13 tell one to consult?",
    "rule": ("In the management of that, one should look to the treatment of raktapitta (probably a bleeding disorder) and "
             "the remedy (प्रतिषेध) for diseases of the private parts (गुह्यरोग)."),
    "limits": ("The unit only points to other treatments; it names no drug, dose or procedure. Raktapitta is a probable "
               "identification, not one modern disease. तत् is read as the disorder just described."),
    "explain_hi": ("यह इकाई चिकित्सा के लिए दूसरे प्रकरणों की ओर संकेत करती है: उसके साधन (उपचार) में रक्तपित्त की चिकित्सा "
                   "और गुह्य रोगों का प्रतिषेध देखना चाहिए। "
                   "‘ईक्षेत’ विधिलिङ् है: ‘देखे, परामर्श करे’। "
                   "यहाँ कोई औषध या मात्रा नहीं दी गई। "
                   "‘चेक्षेत’ में च + ईक्षेत है (अ + ई → ए)।"),
    "hook": "उपचार के लिए देखो: रक्तपित्त-चिकित्सा और गुह्यरोग-प्रतिषेध।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What does unit 13 tell one to look to in managing it?",
            ("Raktapitta treatment and remedies for private-part diseases", "रक्तपित्तचिकित्सितं गुह्यरोगप्रतिषेधं च."),
            [("Fever treatment and remedies for eye diseases", "Neither is named here."),
             ("Cough treatment and the rules of marriage", "Neither is named here."),
             ("Wound treatment and remedies for head diseases", "Neither is named here.")],
            "Two treatments are named: of raktapitta, and the remedy for guhya-roga.",
            "रक्तपित्तचिकित्सित + गुह्यरोगप्रतिषेध."),
        order(1, "Put the words of unit 13 in the line's order.",
              ["तत्साधने", "रक्तपित्तचिकित्सितम्", "गुह्यरोगप्रतिषेधम्", "च", "ईक्षेत"],
              "In its management, raktapitta treatment, private-part disease remedy, and, one should look to.",
              "तत्साधने → रक्तपित्त... → गुह्यरोग... → च → ईक्षेत."),
        match(2, "Match each word of unit 13 to its meaning.",
              [["साधन", "accomplishing, treatment"], ["चिकित्सित", "treatment"], ["गुह्य", "private parts"],
               ["प्रतिषेध", "prevention, remedy"], ["ईक्षेत", "should look to"]],
              "Five words carry the pointer to the two treatments.",
              "साधन, चिकित्सित, गुह्य, प्रतिषेध, ईक्षेत.", role="extend",
              teaches="Such lines point to treatments taught elsewhere: ईक्षेत = should look to, consult."),
        mcq("discriminate", 3, "Which split of चेक्षेत is right?",
            ("च + ईक्षेत", "अ + ई → ए: च + ईक्षेत = चेक्षेत."),
            [("च + एक्षेत", "अ + ए would give ऐ: चैक्षेत."),
             ("चे + क्षेत", "क्षेत is not a word of the card."),
             ("चेत् + क्षेत", "Neither part fits; the verb is ईक्षेत.")],
            "च (and) + ईक्षेत (should look to).",
            "अ + ई → ए."),
        mcq("apply", 4, "What form does the card give ईक्षेत?",
            ("Optative: one should look to", "The card labels it 3 sg. opt.: should look to."),
            [("Past: one looked to", "The label is optative, not past."),
             ("Future: one will look to", "The label is optative, not future."),
             ("Present: one is looking to it now", "The label is optative, not present.")],
            "ईक्षेत is optative: advice, one should look to.",
            "-एत (ātmanepada optative) = one should."),
        mcq("transfer", 5, "By the rule of चेक्षेत, how is गण + ईशः (lord of the hosts) written?",
            ("गणेशः", "अ + ई → ए, as in च + ईक्षेत."),
            [("गणैशः", "अ + ई gives ए, not ऐ."),
             ("गणीशः", "अ + ई does not give ई alone."),
             ("गणयीशः", "No य् is added between अ and ई.")],
            "गण + ईशः = गणेशः, like च + ईक्षेत = चेक्षेत.",
            "अ + ई → ए.",
            teaches="अ or आ before इ or ई joins into ए: च + ईक्षेत → चेक्षेत."),
    ],
}

# ===================================================================== NOTES_HI
NOTES_HI = {
    "1": "मंगल-वाक्य; विश्वास उच्च, कोई पाठ-चिह्न नहीं। ‘श्रीगणेशाय’ को एक समस्त पद (श्री-गणेशाय, पुं. चतुर्थी एकवचन) माना गया। गणेश को केवल देव-नाम रखा गया है, और कुछ नहीं जोड़ा गया।",
    "2": "मंगल-वाक्य; विश्वास उच्च, कोई पाठ-चिह्न नहीं। छपा ‘धन्वन्तरये’ इकारान्त ‘धन्वन्तरि’ की शुद्ध चतुर्थी एकवचन है (इ → अये) — यह जाँचा गया। धन्वन्तरि को नाम के रूप में रखा गया।",
    "3": "विश्वास मध्यम। पाठ-चिह्न: छपे ‘पुत्रकामियं’ में ह्रस्व इ है; ‘पुत्र-काम + ईय’ से दीर्घ ‘पुत्रकामीयम्’ अपेक्षित है (सम्भावित छपाई-भूल)। ‘शारीरंव्याख्यास्यामः’ एक छपा शब्द है, जिसे शारीरम् + व्याख्यास्यामः पढ़ा गया। पंक्ति में ‘अध्याय’ शब्द नहीं है; इसे अध्याय-नाम मानना सामान्य पठन है। ‘अथातः’ = अथ + अतः (अ + अ → आ) जाँचा गया।",
    "4": "विश्वास उच्च, कोई पाठ-चिह्न नहीं। ‘ह स्म’ परोक्ष (लिट्) ‘आहुः’ के साथ भूतकाल का मुहावरा है। सन्धि जाँची गई: स्म + आहुः → स्माहुः (अ + आ → आ); आहुः + आत्रेय → आहुरात्रेय (विसर्ग → र् स्वर से पहले); आत्रेयादयः + महर्षयः → आत्रेयादयो महर्षयः (अः → ओ घोष व्यंजन से पहले); महा + ऋषयः → महर्षयः (आ + ऋ → अर्)।",
    "5": "विश्वास मध्यम; एक लम्बा गद्य-वाक्य (कर्ता पुमान्, क्रिया उद्वहेत्)। पाठ-चिह्न: (1) छपा ‘अनिंद्या मनिंद्येन’ = अनिन्द्याम् अनिन्द्येन (म् अगले शब्द से चिपक गया है); (2) ‘विधिनादुद्वहेत्’ में अतिरिक्त ‘दु’ सम्भव है (विधिना उद्वहेत् / विधिनोद्वहेत्); (3) ‘मृदुमरोगाप्रकृतिम्’ अनिश्चित है (स्त्रीलिंग के बीच पुंलिंग जैसा ‘मृदुम्’ और ‘अरोगा-’ का आ संदिग्ध)। अर्थ-संशय: ‘अतुल्य’ = असमान (पाठ ‘अपने से भिन्न’ नहीं कहता); ‘असंचारिरोगकुल’ का अर्थ सम्भवतः वंशानुगत रोग से रहित कुल, पर पक्का नहीं; नाम-सूची ‘नक्षत्रान्यप्रेक्ष्य...’ को दो तरह बाँटा जा सकता है; ‘चल’ का निश्चित अर्थ नहीं दिया गया। इन पर प्रश्न नहीं बनाए गए। अगली इकाई में आयु सोलह कही गई है; दोनों मिलाए नहीं गए।",
    "6": "विश्वास उच्च, कोई पाठ-चिह्न नहीं। आयु छपे पाठ के अनुसार दी गई है (इकाई 5 में लगभग बारह, यहाँ सोलह; मेल नहीं बैठाया गया)। ‘तस्याम्’ सप्तमी है और इकाई 5 की कन्या की ओर संकेत करता है। ‘पुत्रार्थम्’ अव्ययवत् प्रयोग है (पुत्र + अर्थम्, अ + अ → आ)। ‘प्रयतेत’ आत्मनेपद विधिलिङ् है।",
    "7": "विश्वास उच्च, कोई पाठ-चिह्न नहीं। ‘वीर्य’ का अर्थ यहाँ शक्ति (ओज) रखा गया है; पाठ यहाँ शुक्र नहीं कहता। छपा ‘वीर्यान्वितमपत्यं’ = वीर्यान्वितम् + अपत्यम् (म् स्वर से जुड़ा)। ‘तौ’ और ‘जनयतः’ दोनों द्विवचन हैं (डेटा का लेबल जाँचा गया)। ‘तदा’ को इकाई 6 की आयु से जोड़ा गया है।",
    "8": "विश्वास निम्न। पाठ-चिह्न: (1) ‘गर्भःकुक्षिस्य’ में ‘कुक्षिस्य’ शब्द नहीं; ‘कुक्षिस्थः’ (कोख में स्थित) सुझाव है (थ/य भ्रम); (2) ‘विक्लेंद्रियो’ = सम्भवतः ‘विकलेन्द्रियो’; (3) अन्तिम ‘शुक्रार्तवहति’ अस्पष्ट है, कोई निश्चित पुनर्पाठ नहीं (‘शुक्रार्तव का क्षय’ केवल अनुमान)। ‘ऋतावाद्ये च रात्रित्रये’ शाब्दिक रखा गया; पहली तीन रातों का आशय शब्दों में नहीं। प्रश्न केवल पहले, स्पष्ट भाग (ऊन-आयु, विनाश, अल्पायु, बल-आरोग्य-विभव) पर हैं। सन्धि: वर्षेण + ऊन → वर्षेणोन (अ + ऊ → ओ); आहितः + गर्भः → आहितो गर्भः।",
    "9": "विश्वास उच्च, कोई पाठ-चिह्न नहीं। पहचान: शुक्र = वीर्य (मानक); मज्जन् = मज्जा, शरीर की धातु (सम्भावित)। ‘तत्र’ को ‘वहाँ / उस प्रसंग में’ पढ़ा गया। छपा ‘तत्राहारस्यसम्यक्परिणतस्य’ एक छपा शब्द है; विभाजन तत्र + आहारस्य + सम्यक्परिणतस्य। ‘क्रमान्मज्जानम्’ = क्रमात् + मज्जानम् (त् → न् अनुनासिक से पहले) जाँचा गया।",
    "10": "विश्वास निम्न। पाठ-चिह्न: ‘ततु’ = सम्भवतः ‘तत् तु’; ‘क्षीरहव’ = ‘क्षीरे इव’; ‘सर्पिरिक्षुरसहव’ = ‘सर्पिः इक्षुरसे इव’; ‘सर्बोगव्यापितया’ = ‘सर्वाङ्गव्यापितया’ — उपमाएँ (दूध में घी, ईख के रस में गुड़) इन्हीं सुधारों पर टिकी हैं, इसलिए उन पर प्रश्न नहीं। ‘कला’ शास्त्रीय पद है (झिल्लीदार परत), कोई आधुनिक नाम थोपा नहीं गया। ‘संप्रहन’ = आपस में टकराना; ‘सम्भवतः सम्भोग’ व्याख्या है। ‘हृदयावेशात्’ का अर्थ भी अनिश्चित। पहले वाक्य का कर्ता नहीं छपा; ‘तत्’ को अगले वाक्य का शुक्र माना गया। पहचान: शुक्र = वीर्य (मानक), मुष्क = वृषण (मानक), मज्जा = अस्थि-मज्जा। दूसरे वाक्य की गुण-सूची साफ़ छपी है; प्रश्न उसी पर और ‘मज्जमुष्कस्तनेषु’ पर हैं।",
    "11": "विश्वास उच्च, कोई पाठ-चिह्न नहीं। ‘गर्भकोष्ठ’ = शाब्दिक ‘गर्भ का कोष्ठ’; आधुनिक अर्थ गर्भाशय (सम्भावित)। आर्तव = रजोधर्म का रक्त (मानक)। ‘मासे मासे’ = हर महीने। सन्धि: आर्तवम् + इति + आहुः → आर्तवमित्याहुः (इ + आ → या); गर्भकोष्ठम् + अनुप्राप्य → गर्भकोष्ठमनुप्राप्य।",
    "12": "विश्वास मध्यम। पाठ-चिह्न: छपा ‘वातदेवा सृग्दरं’ = ‘वा तद् एव असृग्दरम्’ पढ़ा गया (छपे रिक्त-स्थान खिसके; ‘असृग्दर’ का अ पिछले शब्द में सन्धि से मिला)। इसलिए ‘असृग्दर’ पर प्रश्न नहीं। द्वितीया-पद (असृग्दरम्, प्रदरम्, व्यापदम्, रक्तयोनिसंज्ञाम्) को प्राप्त नाम माना गया; सम्बन्ध पूरी तरह निश्चित नहीं। ‘तद्’ = इकाई 11 का आर्तव। पहचान: असृग्दर, प्रदर = अधिक रजःस्राव या योनि-स्राव (सम्भावित; प्रयोग बदलता है)। रक्तयोनि नाम ही रखा गया। ‘अनृतावृतौ’ = अनृतौ + ऋतौ (औ → आव्) जाँचा गया।",
    "13": "विश्वास उच्च, कोई पाठ-चिह्न नहीं। रक्तपित्त संस्कृत नाम ही रखा गया; आधुनिक अर्थ रक्तस्राव वाला विकार (सम्भावित, कोई एक आधुनिक रोग नहीं)। गुह्य = जननांग। ‘ईक्षेत’ = देखे, परामर्श करे (आत्मनेपद विधिलिङ्)। ‘चेक्षेत’ = च + ईक्षेत (अ + ई → ए) जाँचा गया। ‘तत्’ किस ओर संकेत करता है, डेटा स्पष्ट नहीं कहता; पिछली इकाई के विकार माना गया।",
}

# ===================================================================== AIDS
AIDS = {
    "1": {
        "frame": "किसे + नमः: जिसे प्रणाम हो वह चतुर्थी में (गणेशाय), फिर ‘नमः’; अलग क्रिया की ज़रूरत नहीं।",
        "chunks": "श्रीगणेशाय | नमः",
        "puns": "केवल सुनने की सहायता: ‘गणेश-आय’ — प्रणाम गणेश की ओर ‘आया’; ‘-आय’ = को।",
    },
    "2": {
        "frame": "इकारान्त नाम + नमः: धन्वन्तरि → धन्वन्तरये नमः (इ → अये)।",
        "chunks": "धन्वन्तरये | नमः",
        "contrast": "इकाई 1: गणेश (अकारान्त) → गणेशाय · इकाई 2: धन्वन्तरि (इकारान्त) → धन्वन्तरये। दोनों चतुर्थी, अन्त अलग।",
    },
    "3": {
        "chain": {"steps": ["अथ (अब)", "अतः (इसलिए)", "पुत्रकामीयम्", "शारीरम्", "व्याख्यास्यामः (हम कहेंगे)"]},
        "sandhi": "अ + अ → आ: अथ + अतः → अथातः · छपा ‘शारीरंव्याख्यास्यामः’ = शारीरम् + व्याख्यास्यामः (म् → ं व्यंजन से पहले)।",
        "chunks": "अथातः | पुत्रकामियं (= पुत्रकामीयम्) | शारीरं | व्याख्यास्यामः",
    },
    "4": {
        "sandhi": "अ + आ → आ: स्म + आहुः → स्माहुः · विसर्ग स्वर से पहले र्: आहुः + आत्रेय → आहुरात्रेय · अः + म → ओ: आत्रेयादयः + महर्षयः → आत्रेयादयो महर्षयः · आ + ऋ → अर्: महा + ऋषयः → महर्षयः।",
        "chunks": "इति ह | स्माहुः | आत्रेयादयः | महर्षयः",
        "frame": "इति (ऐसा) → ह स्म आहुः (कहा था) → कौन: आत्रेयादयः महर्षयः (आत्रेय आदि महर्षि)।",
    },
    "5": {
        "diagram": {"groups": [
            {"label": "पुरुष और क्रिया", "items": ["पुमान्", "एकविंशतिवर्षः", "अनिन्द्येन विधिना", "उद्वहेत्"]},
            {"label": "कन्या के गुण (क्रम से)", "items": ["अतुल्यगोत्रा", "अतुल्याभिजना", "असंचारिरोगकुलप्रसूता",
                                                    "रूपशीललक्षणसंपन्ना", "अनूना", "अविनष्ट दन्त-ओष्ठ-कर्ण-नख-केश-स्तन",
                                                    "अकपिला, अपिङ्गला", "अहीनाधिकाङ्गी", "द्वादशवर्षदेशीया",
                                                    "भयानक आदि नाम न धारण करे", "अनघा", "अनिन्द्या"]}]},
        "chunks": "अथ खलु पुमान् एकविंशतिवर्षः | कन्याम् अतुल्यगोत्राम् अतुल्याभिजनाम् ... | रूपशीललक्षणसंपन्नाम् ... | द्वादशवर्षदेशीयाम् ... | अनघाम् अनिन्द्याम् | अनिन्द्येन विधिना उद्वहेत्",
        "frame": "कर्ता (पुमान्, २१ वर्ष) → बीच में कन्या की लम्बी विशेषण-सूची (सब स्त्रीलिंग द्वितीया) → अन्त में क्रिया (उद्वहेत्)।",
        "contrast": "निषेध-उपसर्ग: व्यंजन से पहले अ- (अकपिला, अपिङ्गला, अतुल्य) ↔ स्वर से पहले अन्- (अनूना, अनघा, अनुद्वहन्ती)।",
    },
    "6": {
        "seesaw": "स्त्री: षोडशवर्षीया (सोलह वर्ष) ↔ पुरुष: पञ्चविंशतिवर्षः (पच्चीस वर्ष)।",
        "chunks": "तस्यां षोडशवर्षीयां | पञ्चविंशतिवर्षः पुरुषः | पुत्रार्थं प्रयतेत",
        "sandhi": "अ + अ → आ: पुत्र + अर्थम् → पुत्रार्थम्।",
        "pegs": "मेरा बनाया चित्र: एक तराजू, एक पलड़े पर ‘१६’ और दूसरे पर ‘२५’ लिखा, बीच में ‘पुत्रार्थम्’ की तख़्ती। (केवल याद के लिए)",
    },
    "7": {
        "chain": {"steps": ["तदा (तब, उस आयु में)", "तौ प्राप्तवीर्यौ (दोनों शक्ति पाए हुए)", "जनयतः (उत्पन्न करते हैं)", "वीर्यान्वितम् अपत्यम्"]},
        "chunks": "तदा हि तौ | प्राप्तवीर्यौ | वीर्यान्वितमपत्यं | जनयतः",
        "sandhi": "अ + अ → आ: वीर्य + अन्वितम् → वीर्यान्वितम् · म् + स्वर: वीर्यान्वितम् + अपत्यम् → वीर्यान्वितमपत्यम्।",
    },
    "8": {
        "diagram": {"groups": [
            {"label": "कारण", "items": ["ऊनपञ्चविंशतिवर्ष पुरुष", "ऊनषोडशवर्षीया स्त्री", "आहितः गर्भः"]},
            {"label": "परिणाम (वा ... वा)", "items": ["विनाश", "अल्प आयु-बल-आरोग्य-विभव", "विकल इन्द्रियाँ (पाठ-सुधार)"]}]},
        "contrast": "ऊन = कम (इकाई 8) ↔ देशीय = लगभग (इकाई 5)।",
        "sandhi": "अ + ऊ → ओ: वर्षेण + ऊन → वर्षेणोन · अः + ग → ओ: आहितः + गर्भः → आहितो गर्भः।",
        "chunks": "ऊनपञ्चविंशतिवर्षेण | ऊनषोडशवर्षीयाम् आहितो गर्भः | (कुक्षिस्थः) एव विनाशम् आप्नुयात् | अल्पायुर्बलारोग्यविभवो वा स्यात् | विकलेन्द्रियो वा | (शेष अस्पष्ट)",
    },
    "9": {
        "chain": {"steps": ["आहार (भोजन)", "सम्यक् परिणत", "क्रमात् (क्रम से)", "मज्जा तक पहुँचा", "सारः", "‘शुक्र’ नाम"]},
        "sandhi": "त् + म → न्म: क्रमात् + मज्जानम् → क्रमान्मज्जानम् · अ + आ → आ: तत्र + आहारस्य → तत्राहारस्य।",
        "chunks": "तत्र आहारस्य सम्यक्परिणतस्य | क्रमान्मज्जानमनुप्राप्तस्य | सारः | शुक्रसंज्ञां लभते",
    },
    "10": {
        "diagram": {"groups": [
            {"label": "कहाँ (विशेषतः)", "items": ["मज्जा", "मुष्क", "स्तन"]},
            {"label": "गर्भाधान-योग्य शुक्र के गुण", "items": ["सौम्य", "स्निग्ध", "गुरु", "शुक्ल", "मधुगन्धि", "मधुर",
                                                     "पिच्छिल", "बहु", "बहल", "घृत/तैल/क्षौद्र-वर्ण"]}]},
        "chunks": "तत् (तु) ... शरीरे शुक्रधरां कलामाश्रित्य ... स्थितम् | विशेषतश्च मज्जमुष्कस्तनेषु | ... अङ्गादङ्गात्प्रवर्तते ‖ तत्सौम्यं स्निग्धं गुरु शुक्लं मधुगन्धि मधुरं | पिच्छिलं बहु बहलं | घृततैलक्षौद्रान्यतमवर्णं च | शुक्रं गर्भाधानयोग्यं भवति",
        "letters": "गुणों के पहले अक्षर क्रम से: सौ-स्नि-गु-शु-म-म-पि-ब-ब (सौम्य, स्निग्ध, गुरु, शुक्ल, मधुगन्धि, मधुर, पिच्छिल, बहु, बहल)।",
        "pegs": "मेरा बनाया चित्र: एक श्वेत, गाढ़ी, शहद-सी चमकती बूँद, जिसके चारों ओर नौ छोटी तख़्तियों पर गुण लिखे हैं। (केवल याद के लिए)",
    },
    "11": {
        "chain": {"steps": ["स्त्रियों का रक्त ही", "मासे मासे (हर मास)", "गर्भकोष्ठ तक पहुँचकर", "त्र्यहम् (तीन दिन) बहता", "‘आर्तव’ कहलाता"]},
        "sandhi": "इ + आ → या: इति + आहुः → इत्याहुः · म् + स्वर: आर्तवम् + इति → आर्तवमिति · इ + अ → य: त्रि + अहम् → त्र्यहम्।",
        "chunks": "तथा रक्तमेव च स्त्रीणां | मासे मासे | गर्भकोष्ठमनुप्राप्य | त्र्यहं प्रवर्तमानम् | आर्तवमित्याहुः",
        "contrast": "इकाई 9: आहार का सार → मज्जा तक → ‘शुक्र’ ↔ इकाई 11: स्त्रियों का रक्त → गर्भकोष्ठ तक → ‘आर्तव’।",
    },
    "12": {
        "diagram": {"groups": [
            {"label": "कारण और समय", "items": ["अतिप्रसङ्गेन", "अनृतौ", "ऋतौ वा"]},
            {"label": "प्राप्त नाम", "items": ["असृग्दर (पुनर्विभाजित पाठ)", "प्रदर", "व्यापद्", "रक्तयोनि"]}]},
        "sandhi": "औ + ऋ → आवृ: अनृतौ + ऋतौ → अनृतावृतौ · अ + अ → आ: अतिप्रसङ्गेन + अनृतौ → अतिप्रसङ्गेनानृतौ।",
        "chunks": "अतिप्रसङ्गेन | अनृतावृतौ वा | तदेवासृग्दरं (पुनर्विभाजित) | प्रदरं व्यापदं च | रक्तयोनिसंज्ञां लभते",
    },
    "13": {
        "diagram": {"groups": [
            {"label": "तत्साधने (उसके उपचार में) देखें", "items": ["रक्तपित्त-चिकित्सित", "गुह्यरोग-प्रतिषेध"]}]},
        "sandhi": "अ + ई → ए: च + ईक्षेत → चेक्षेत।",
        "chunks": "तत्साधने | रक्तपित्तचिकित्सितं | गुह्यरोगप्रतिषेधं | चेक्षेत",
        "anchors": "याद-सूत्र: इस इकाई में कोई औषध नहीं, केवल दो ‘पते’ — रक्तपित्त और गुह्यरोग। (मेरी याद-पद्धति)",
    },
}

# ===================================================================== IMAGE_SPECS
IMAGE_SPECS = {
    ("5", "diagram"): {
        "file": "sh1-kanya-gunas-5.svg",
        "alt": ("Table of unit 5 in text order: the man (twenty-one years) should marry by blameless rule a girl of unlike gotra "
                "and ancestry, of a family with non-transmitting disease, endowed with beauty, conduct and marks, with undamaged "
                "teeth, lips, ears, nails, hair and breasts, neither tawny nor reddish-brown, limbs neither deficient nor in excess, "
                "of about twelve years, not bearing frightening names, faultless and blameless."),
        "type": "table",
        "title": "इकाई ५: क्रम से",
        "heads": ["पद", "अर्थ"],
        "rows": [["पुमान् एकविंशतिवर्षः", "इक्कीस वर्ष का पुरुष"],
                 ["अतुल्यगोत्रा, अतुल्याभिजना", "असमान गोत्र व वंश"],
                 ["असंचारिरोगकुलप्रसूता", "रोग असंचारी कुल"],
                 ["रूपशीललक्षणसंपन्ना", "रूप, शील, लक्षण"],
                 ["अविनष्ट दन्त-ओष्ठ आदि", "दाँत, होंठ आदि अक्षत"],
                 ["अकपिला, अपिङ्गला", "न कपिला, न पिंगला"],
                 ["अहीनाधिकाङ्गी", "अंग न कम न अधिक"],
                 ["द्वादशवर्षदेशीया", "लगभग बारह वर्ष"],
                 ["नामानि अनुद्वहन्ती", "भयानक आदि नाम नहीं"],
                 ["अनघा, अनिन्द्या", "निर्दोष, अनिन्द्य"],
                 ["अनिन्द्येन विधिना उद्वहेत्", "अनिन्द्य विधि से ब्याहे"]],
    },
    ("8", "diagram"): {
        "file": "sh1-una-garbha-8.svg",
        "alt": ("Flowchart of the sure first part of unit 8: a man under twenty-five and a woman under sixteen; the embryo placed "
                "may perish, or be of short life with little strength, health and means, or have defective senses (corrected reading)."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"पुरुष: पच्चीस से कम\"] --> C[\"आहितः गर्भः\"]\n"
                 "  B[\"स्त्री: सोलह से कम\"] --> C\n"
                 "  C -->|\"या\"| D[\"विनाश\"]\n"
                 "  C -->|\"या\"| E[\"अल्प आयु, बल,<br/>आरोग्य, विभव\"]\n"
                 "  C -->|\"या\"| F[\"विकल इन्द्रियाँ<br/>(पाठ-सुधार)\"]\n"),
    },
    ("9", "chain"): {
        "file": "sh1-shukra-9.svg",
        "alt": ("Chain of unit 9: food, well transformed, in order, reaches the marrow; its essence obtains the name shukra."),
        "type": "chain",
        "title": "शुक्र की उत्पत्ति (इकाई ९)",
        "steps": ["आहार", "सम्यक् परिणत", "क्रम से", "मज्जा तक", "सार", "‘शुक्र’ नाम"],
    },
    ("10", "diagram"): {
        "file": "sh1-shukra-gunas-10.svg",
        "alt": ("Mind map of unit 10: shukra fit for conception and its qualities in text order: gentle, unctuous, heavy, white, "
                "honey-scented, sweet, slimy, abundant, thick, and of the colour of ghee, oil or honey."),
        "type": "mermaid",
        "code": ("mindmap\n"
                 "  गर्भाधान-योग्य शुक्र\n"
                 "    सौम्य\n"
                 "    स्निग्ध\n"
                 "    गुरु\n"
                 "    शुक्ल\n"
                 "    मधुगन्धि\n"
                 "    मधुर\n"
                 "    पिच्छिल\n"
                 "    बहु\n"
                 "    बहल\n"
                 "    घृत-तैल-मधु वर्ण\n"),
    },
    ("11", "chain"): {
        "file": "sh1-artava-11.svg",
        "alt": ("Chain of unit 11: women's blood itself, month by month, reaching the garbhakoshtha, flowing for three days, "
                "is called artava."),
        "type": "chain",
        "title": "आर्तव (इकाई ११)",
        "steps": ["स्त्रियों का रक्त ही", "हर मास", "गर्भकोष्ठ तक", "तीन दिन बहता", "‘आर्तव’ नाम"],
    },
    ("12", "diagram"): {
        "file": "sh1-raktayoni-12.svg",
        "alt": ("Flowchart of unit 12: through excessive continuation, out of season or in season, that same artava obtains "
                "the names asrigdara (re-split reading), pradara, vyapad and raktayoni."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"अतिप्रसङ्ग से\"] --> B[\"अनृतौ या ऋतौ\"]\n"
                 "  B --> C[\"वही आर्तव\"]\n"
                 "  C --> D[\"नाम पाता है\"]\n"
                 "  D --> E[\"असृग्दर<br/>(पुनर्विभाजन)\"]\n"
                 "  D --> F[\"प्रदर\"]\n"
                 "  D --> G[\"व्यापद्\"]\n"
                 "  D --> H[\"रक्तयोनि\"]\n"),
    },
}
