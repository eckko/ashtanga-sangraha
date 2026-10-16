from helpers import mcq, match, order, fill, multi, accepts


def ex(q, teaches):
    """Give an order question (extend role) its teaches field."""
    q["role"] = "extend"
    q["teaches"] = teaches
    return q


AUTHORED = {}

# ---------------------------------------------------------------- unit 14
AUTHORED["14"] = {
    "title": "आयुर्वेदोपदेशेषु विधेयः परमादरः",
    "question": "What attitude does the first line ask the reader to hold toward the teachings of Āyurveda?",
    "rule": ("आयुर्वेदोपदेशेषु विधेयः परमादरः = Supreme regard is to be paid to "
             "the teachings of Āyurveda. This line finishes a sentence begun in unit 13."),
    "limits": ("The first line finishes a verse begun in unit 13. The second line (Brahmā and the "
               "eternal nectar of Āyurveda) is doubtful in the print: सार्थम् may mean 'with its "
               "meaning' or 'meaningful', and बुद्ध्वा may stand for स्मृत्वा. No question rests on it."),
    "explain_hi": ("पहली पंक्ति पिछले श्लोक का वाक्य पूरा करती है: आयुर्वेद के उपदेशों के प्रति "
                   "परम आदर रखना चाहिए। ‘विधेयः’ का अर्थ है ‘किया जाना चाहिए’, यानी यह आदेश का "
                   "रूप है, बीते काम का नहीं। ‘उपदेशेषु’ सप्तमी बहुवचन है: ‘उपदेशों में’। "
                   "दूसरी पंक्ति ब्रह्मा के आयुर्वेदरूपी सनातन अमृत को जानने की बात शुरू करती है, "
                   "पर उसका पाठ संदिग्ध है और वाक्य अगले श्लोक में चलता है।"),
    "hook": "उपदेशों में · करना चाहिए · परम आदर।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "What attitude toward the teachings of Āyurveda does the first line urge?",
            ("Supreme regard", "आदर is regard, and परम makes it the highest."),
            [("Careful doubt", "The line does not ask for doubt."),
             ("Quiet pride", "The line does not speak of pride."),
             ("Mild fear", "The line does not speak of fear.")],
            "The line says supreme regard is to be paid to the teachings of Āyurveda.",
            "आयुर्वेदोपदेशेषु विधेयः परमादरः = supreme regard is to be paid."),
        match(1, "Match each word of the first line to its meaning.",
              [["उपदेशेषु", "in the teachings"], ["विधेयः", "to be paid, to be done"],
               ["परम", "supreme"], ["आदरः", "regard"]],
              "These words carry the whole instruction of the line.",
              "उपदेशेषु = in the teachings; विधेयः = to be done; परम = supreme; आदरः = regard."),
        ex(order(2, "Put the three words of the first line in the verse's order.",
                 ["आयुर्वेदोपदेशेषु", "विधेयः", "परमादरः"],
                 "The line names where (in the teachings), then what is to be done, then what: supreme regard.",
                 "आयुर्वेदोपदेशेषु → विधेयः → परमादरः."),
           "A short instruction can be held as three steps: where it applies, what is to be done, and the thing to do."),
        mcq("discriminate", 3, "Which is the right split of आयुर्वेदोपदेशेषु?",
            ("आयुर्वेद + उपदेशेषु", "अ + उ joins as ओ, so आयुर्वेद + उपदेशेषु is written आयुर्वेदोपदेशेषु."),
            [("आयुर्वेदः + उपदेशेषु", "This would be written आयुर्वेद उपदेशेषु."),
             ("आयुर्वेदे + उपदेशेषु", "This would be written आयुर्वेदयुपदेशेषु."),
             ("आयुर्वेदौ + उपदेशेषु", "This would be written आयुर्वेदावुपदेशेषु.")],
            "आयुर्वेदोपदेशेषु = आयुर्वेद (Āyurveda) + उपदेशेषु (in the teachings).",
            "अ + उ → ओ."),
        mcq("apply", 4,
            "विधेयः means to be done, to be paid. Which translation fits विधेयः परमादरः?",
            ("Supreme regard is to be paid", "विधेयः says what should be done; परमादरः is the regard."),
            [("Supreme regard was paid", "विधेयः is not a past form."),
             ("The supreme one pays regard", "परमादरः is the thing paid, not the payer."),
             ("Regard for the supreme is lost", "Nothing here speaks of loss.")],
            "विधेयः is a 'to be done' form and agrees with आदरः: regard is what is to be paid.",
            "विधेयः + noun = that noun is to be done."),
        mcq("transfer", 5,
            "Join नव (new) and उपदेशेषु (in the teachings) by the same sandhi. Which spelling results?",
            ("नवोपदेशेषु", "अ + उ gives ओ, as in आयुर्वेदोपदेशेषु."),
            [("नवुपदेशेषु", "The two vowels do not simply merge into उ."),
             ("नवूपदेशेषु", "अ + उ does not give ऊ."),
             ("नवौपदेशेषु", "औ comes from अ + ओ or अ + औ, not from अ + उ.")],
            "The rule of the verse works on any word ending in अ that meets उ.",
            "अ + उ → ओ.",
            teaches="When a word ending in अ meets a word beginning with उ, the two vowels join as ओ: नव + उपदेशेषु → नवोपदेशेषु."),
    ],
}

# ---------------------------------------------------------------- unit 15
AUTHORED["15"] = {
    "title": "ददौ दक्षाय सोऽश्विभ्यां",
    "question": "In what order is the teaching handed on, and which four aims does the second line name?",
    "rule": ("He gave it to Dakṣa; Dakṣa to the two Aśvins; they to Śatakratu (Indra). "
             "Second line: diseases that obstruct dharma, wealth, desire and liberation."),
    "limits": ("The giver in the first clause is Brahmā of unit 14, supplied from there; "
               "that सः means Dakṣa is by sense. The second line begins a clause that ends "
               "in unit 16 and 17, so it is cut off here."),
    "explain_hi": ("पहली पंक्ति शिक्षा के हस्तांतरण की कड़ी है: ददौ (दिया) दक्ष को, फिर सः यानी "
                   "दक्ष ने दोनों अश्विनों को, और उन दोनों ने ततः (तब) शतक्रतु इंद्र को। देने वाला "
                   "पिछले श्लोक का ब्रह्मा है। हर पाने वाला चतुर्थी में है (-आय, -भ्याम्, -वे)। "
                   "दूसरी पंक्ति में चार पुरुषार्थ हैं: धर्म, अर्थ, काम, मोक्ष, और उनमें विघ्न डालने "
                   "वाले रोग। वाक्य अगले श्लोकों में पूरा होता है।"),
    "hook": "ब्रह्मा → दक्ष → अश्विनौ → इंद्र · धर्म, अर्थ, काम, मोक्ष में विघ्न करते रोग…",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "The teaching is handed down a chain. Who is the first receiver named in this verse?",
            ("Dakṣa", "ददौ दक्षाय: he gave to Dakṣa."),
            [("The two Aśvins", "They receive it second."),
             ("Indra (Śatakratu)", "He is the last receiver in the line."),
             ("Punarvasu", "He is not named in this verse.")],
            "The chain opens with Dakṣa, then the Aśvins, then Indra.",
            "First receiver: दक्ष."),
        match(1, "Match each word of the first line to its meaning.",
              [["ददौ", "gave"], ["दक्षाय", "to Dakṣa"],
               ["अश्विभ्याम्", "to the two Aśvins"], ["शतक्रतवे", "to Śatakratu (Indra)"]],
              "Three receivers, each in the 'to' form, and the verb 'gave'.",
              "ददौ = gave; दक्षाय = to Dakṣa; अश्विभ्याम् = to the two Aśvins; शतक्रतवे = to Śatakratu."),
        ex(order(2, "Put the receivers in the order the verse hands the teaching on.",
                 ["दक्षाय", "अश्विभ्याम्", "शतक्रतवे"],
                 "Dakṣa first, then the two Aśvins, then Śatakratu (Indra).",
                 "दक्ष → अश्विनौ → शतक्रतु."),
           "A line of teaching can be held as a chain of receivers: Dakṣa, the two Aśvins, Śatakratu."),
        mcq("discriminate", 3, "Which is the right split of सोऽश्विभ्याम्?",
            ("सः + अश्विभ्याम्", "A visarga after अ before अ becomes ओ, and the अ is marked by ऽ: सोऽश्विभ्याम्."),
            [("सा + अश्विभ्याम्", "This would be written साश्विभ्याम्."),
             ("सौ + अश्विभ्याम्", "This would be written सावश्विभ्याम्."),
             ("सः + श्विभ्याम्", "श्विभ्याम् is not a word.")],
            "सोऽश्विभ्याम् = सः (he) + अश्विभ्याम् (to the two Aśvins).",
            "सः + अ → सोऽ."),
        multi("apply", 4, "Which four aims does the second line name? Choose all that apply.",
              [("धर्म", "Named: first in the compound."),
               ("अर्थ", "Named: second."),
               ("काम", "Named: third."),
               ("मोक्ष", "Named: fourth."),
               ("आयुः", "Life is not one of the four in this line."),
               ("कीर्ति", "Fame is not named here.")],
              [0, 1, 2, 3],
              "धर्मार्थकाममोक्षाणाम् is a list of four, in the 'of' form: of dharma, wealth, desire and liberation.",
              "The four: धर्म, अर्थ, काम, मोक्ष."),
        mcq("transfer", 5,
            "In an invented line ददौ शिष्याय स गुरुः, who receives what is given?",
            ("The pupil (शिष्याय)", "The ending -आय marks the receiver."),
            [("The teacher (गुरुः)", "गुरुः is the one who gives (ending -ः)."),
             ("Nobody: ददौ means took", "ददौ means gave."),
             ("Both together", "Only one receiver is named.")],
            "As in ददौ दक्षाय, the 'to' form names the receiver of a gift.",
            "Receiver of ददौ = the word in -आय.",
            teaches="After ददौ ('gave') the receiver stands in the -आय form: दक्षाय 'to Dakṣa', शिष्याय 'to the pupil'."),
    ],
}

# ---------------------------------------------------------------- unit 16
AUTHORED["16"] = {
    "title": "नरेषु पीड्यमानेषु पुरस्कृत्य पुनर्वसुं",
    "question": "Whom do they put at the head, and which names are listed?",
    "rule": ("When men were being afflicted, putting Punarvasu at the head: "
             "Dhanvantari, Bharadvāja, Nimi, Kāśyapa and Kaśyapa. The verb comes in unit 17."),
    "limits": ("The sentence runs on: the finite verb उपाजग्मुः is in unit 17. The list gives "
               "both काश्यप and कश्यप; whether these are two persons or a repeated name is "
               "uncertain, so no question rests on it. Who stands where in the list, beyond the "
               "order printed, is not explained."),
    "explain_hi": ("यह आधा वाक्य है। ‘नरेषु पीड्यमानेषु’ दोनों सप्तमी बहुवचन हैं: ‘मनुष्यों के पीड़ित "
                   "होने पर’। ‘पुरस्कृत्य’ का अर्थ है ‘आगे करके’; यह -य वाला रूप इसलिए है कि धातु के "
                   "आगे ‘पुरस्’ जुड़ा है। आगे किया गया व्यक्ति पुनर्वसु है (-म् वाला रूप)। दूसरी पंक्ति "
                   "नामों की सूची है: धन्वन्तरि, भरद्वाज, निमि, काश्यप, कश्यप। क्रिया ‘उपाजग्मुः’ अगले "
                   "श्लोक में आती है।"),
    "hook": "मनुष्य पीड़ित हुए → पुनर्वसु को आगे करके → धन्वन्तरि, भरद्वाज, निमि, काश्यप, कश्यप…",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Men are suffering, and a group sets out. Which name does the verse put at the head?",
            ("Punarvasu", "पुरस्कृत्य पुनर्वसुम्: having put Punarvasu in front."),
            [("Indra", "Indra is the one approached in unit 17, not the one put at the head."),
             ("Brahmā", "Brahmā is not named in this verse."),
             ("Dakṣa", "Dakṣa is not named in this verse.")],
            "Punarvasu is placed in front; the other names follow in the list.",
            "पुरस्कृत्य पुनर्वसुम् = putting Punarvasu at the head."),
        match(1, "Match each word of the first line to its meaning.",
              [["नरेषु", "among men"], ["पीड्यमानेषु", "being afflicted"],
               ["पुरस्कृत्य", "having put in front"], ["पुनर्वसुम्", "Punarvasu"]],
              "The first line is a condition plus an act of putting someone in front.",
              "नरेषु = among men; पीड्यमानेषु = being afflicted; पुरस्कृत्य = having put in front; पुनर्वसुम् = Punarvasu."),
        ex(order(2, "Put the four words of the first line in the verse's order.",
                 ["नरेषु", "पीड्यमानेषु", "पुरस्कृत्य", "पुनर्वसुम्"],
                 "Men, afflicted, putting in front, Punarvasu.",
                 "नरेषु → पीड्यमानेषु → पुरस्कृत्य → पुनर्वसुम्."),
           "The line reads as: when men are afflicted (two words), putting Punarvasu in front (two words)."),
        mcq("discriminate", 3,
            "पुरस्कृत्य means having put in front. Why does it end in -य and not -त्वा?",
            ("A word, पुरस्, stands before the root", "A 'having done' word takes -य when something is joined before the root."),
            [("The verb is in the plural", "Number does not decide between -य and -त्वा."),
             ("The act is still going on", "A 'having done' word names a finished act."),
             ("-त्वा is used only after ध", "-त्वा is not limited to roots in ध.")],
            "A 'having done' word has -त्वा after a plain root (बुद्ध्वा) and -य when a word or prefix is joined before it (पुरस्कृत्य).",
            "Plain root + -त्वा; word or prefix + root + -य."),
        multi("apply", 4, "Which of these names appear in this verse? Choose all that apply.",
              [("धन्वन्तरि", "Named in the second line."),
               ("भरद्वाज", "Named in the second line."),
               ("निमि", "Named in the second line."),
               ("अग्निवेश", "Not named in this verse."),
               ("सुश्रुत", "Not named in this verse.")],
              [0, 1, 2],
              "The second line gives Dhanvantari, Bharadvāja, Nimi, Kāśyapa and Kaśyapa.",
              "Named here: धन्वन्तरि, भरद्वाज, निमि (then काश्यप, कश्यप)."),
        mcq("transfer", 5,
            "An invented phrase जनेषु रुग्णेषु (रुग्ण = sick) follows नरेषु पीड्यमानेषु. What does it mean?",
            ("When the people are sick", "Two words in -एषु that agree give 'when (they are) so and so'."),
            [("Of the sick people", "That would end in -नाम्, not -एषु."),
             ("By the sick people", "That would end in -ऐः, not -एषु."),
             ("To the sick people", "That would end in -भ्यः, not -एषु.")],
            "As नरेषु पीड्यमानेषु = when men are afflicted, जनेषु रुग्णेषु = when the people are sick.",
            "Noun + describing word, both in -एषु = 'when (they are) so'.",
            teaches="Two agreeing words in -एषु, a noun and its describing word, tell the situation: जनेषु रुग्णेषु 'when the people are sick'."),
    ],
}

# ---------------------------------------------------------------- unit 17
AUTHORED["17"] = {
    "title": "महर्षयो महात्मानस्तथालम्बायनादयः",
    "question": "Who approached whom, and how is he described?",
    "rule": ("The great sages, the high-souled, and Alambāyana and others approached "
             "Śatakratu, a refuge, lord of the immortals."),
    "limits": ("The verse completes the sentence of unit 16, whose list of names may be the same "
               "company; the card does not decide that. It says nothing yet of what they asked. "
               "The printed तथा'लम्बायन has an avagraha that तथा + अलम्बायन would not need."),
    "explain_hi": ("यहाँ उपाजग्मुः (पहुँचे) क्रिया आ गई। कर्ता हैं महर्षि, महात्मा और आलम्बायन आदि। "
                   "वे शतक्रतु (इंद्र) के पास पहुँचे, जिन्हें दो नाम दिए गए हैं: शरण्य (शरण देने वाला) "
                   "और अमरेश्वर (अमरों का स्वामी)। पाने वाला ‘शतक्रतुम्’ -म् वाले रूप में है। "
                   "सन्धि: महर्षयः + महात्मानः → महर्षयो महात्मानः; शतक्रतुम् + उपाजग्मुः → "
                   "शतक्रतुमुपाजग्मुः।"),
    "hook": "महर्षि, महात्मा, आलम्बायन आदि → शतक्रतु: शरण, अमरों के ईश्वर।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "How is Śatakratu described as the sages come to him?",
            ("A refuge, the lord of the immortals", "शरण्यम् अमरेश्वरम्: a refuge, lord of the immortals."),
            [("A king of men, lord of the earth", "The verse calls him lord of the immortals."),
             ("A pupil of the great sages", "He is the one approached, not their pupil."),
             ("A guard of heaven's gate", "No such guard is named here.")],
            "The two titles are शरण्य (giving refuge) and अमरेश्वर (lord of the immortals).",
            "शतक्रतु = शरण्य, अमरेश्वर."),
        match(1, "Match each word of the verse to its meaning.",
              [["महर्षयः", "great sages"], ["महात्मानः", "high-souled"],
               ["उपाजग्मुः", "approached"], ["शरण्यम्", "a refuge"]],
              "Doers, a quality of the doers, the act, and a title of the one approached.",
              "महर्षयः = great sages; महात्मानः = high-souled; उपाजग्मुः = approached; शरण्यम् = refuge."),
        ex(order(2, "Put the words of the second line in the verse's order.",
                 ["शतक्रतुम्", "उपाजग्मुः", "शरण्यम्", "अमरेश्वरम्"],
                 "The one approached, the act, then his two titles.",
                 "शतक्रतुम् → उपाजग्मुः → शरण्यम् → अमरेश्वरम्."),
           "The second line names the one approached, what was done, then two titles of the one approached."),
        mcq("discriminate", 3, "Which is the right split of शतक्रतुमुपाजग्मुः?",
            ("शतक्रतुम् + उपाजग्मुः", "A final म् joins the vowel that follows: म् + उ is written मु."),
            [("शतक्रतुः + उपाजग्मुः", "This would be written शतक्रतुरुपाजग्मुः."),
             ("शतक्रतु + मुपाजग्मुः", "मुपाजग्मुः is not a word."),
             ("शतक्रतुम् + पाजग्मुः", "पाजग्मुः is not a word.")],
            "शतक्रतुमुपाजग्मुः = शतक्रतुम् (Śatakratu, the one approached) + उपाजग्मुः (they approached).",
            "म् + vowel: the म् is written with the vowel."),
        multi("apply", 4, "Who approached Śatakratu according to this verse? Choose all that apply.",
              [("The great sages", "Named: महर्षयः."),
               ("Alambāyana and others", "Named: आलम्बायनादयः."),
               ("Dakṣa", "Dakṣa is named in unit 15, not here."),
               ("Brahmā", "Brahmā is not named in this verse.")],
              [0, 1],
              "The doers are the sages and Alambāyana with others; Śatakratu is the one approached.",
              "Doers: महर्षि, आलम्बायन आदि."),
        mcq("transfer", 5,
            "In the invented line ऋषयो विष्णुमुपाजग्मुः, who is approached?",
            ("Viṣṇu (विष्णुम्)", "The -म् form marks the one approached, as in शतक्रतुम्."),
            [("The sages (ऋषयः)", "ऋषयः are the doers."),
             ("Both of them", "Only one is approached."),
             ("Nobody: it means they left", "उपाजग्मुः means they approached.")],
            "The same pattern as the verse: doers + one approached in -म् + उपाजग्मुः.",
            "Doers (ऋषयो) + one approached (-म्) + उपाजग्मुः.",
            teaches="With उपाजग्मुः ('approached') the one approached stands in the -म् form, and a doer's -ः turns to ओ before a voiced sound: ऋषयः + विष्णुम् → ऋषयो विष्णुम्."),
    ],
}

# ---------------------------------------------------------------- unit 18
AUTHORED["18"] = {
    "title": "तान्दृष्ट्वैव सहस्राक्षो निजगाद यथागमं",
    "question": "What did the thousand-eyed one do on seeing them, and what did he declare?",
    "rule": ("On seeing them, the thousand-eyed one (Indra) declared, according to the tradition, "
             "the Veda that protects life, the subsidiary Veda (Upaveda) of Atharvan."),
    "limits": ("The sentence goes on in unit 19 with a clause 'which the Grandfather understood'. "
               "That सहस्राक्ष is Indra is by context. उपवेदम् अथर्वणः is rendered as 'the Upaveda of "
               "Atharvan (the Atharva Veda)'; the verse says no more than that."),
    "explain_hi": ("इंद्र उन्हें देखते ही बोले। ‘दृष्ट्वा’ (देखकर) पहले हुई क्रिया है और ‘निजगाद’ (कहा) बाद की; "
                   "दोनों का कर्ता सहस्राक्ष है। ‘यथागमम्’ का भाव है ‘परंपरा के अनुसार’, यानी जैसा आगम में है। "
                   "दूसरी पंक्ति बताती है कि क्या कहा: आयु की रक्षा करने वाला वेद, अथर्ववेद का उपवेद। "
                   "वाक्य अगले श्लोक में आगे बढ़ता है।"),
    "hook": "देखते ही इंद्र बोले · परंपरा से · आयु का रक्षक वेद, अथर्व का उपवेद।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "The sages have come to Indra for refuge. What does he do on seeing them?",
            ("He declares a teaching", "निजगाद: he spoke, declared."),
            [("He sends them away", "Nothing of the kind is said."),
             ("He stays silent", "The verb says he spoke."),
             ("He asks them for gifts", "No gift is mentioned here.")],
            "Indra speaks out a teaching as soon as he sees them.",
            "तान् दृष्ट्वा निजगाद = having seen them, he declared."),
        match(1, "Match each word to its meaning.",
              [["सहस्राक्षः", "thousand-eyed (Indra)"], ["निजगाद", "declared"],
               ["यथागमम्", "according to the tradition"], ["आयुषः", "of life"]],
              "The doer, the act, the manner, and the 'of life' that qualifies the Veda.",
              "सहस्राक्षः = thousand-eyed; निजगाद = declared; यथागमम् = according to tradition; आयुषः = of life."),
        ex(order(2, "Put the words of the second line in the verse's order.",
                 ["आयुषः", "पालकम्", "वेदम्", "उपवेदम्", "अथर्वणः"],
                 "Of life, protector, Veda, subsidiary Veda, of Atharvan.",
                 "आयुषः → पालकम् → वेदम् → उपवेदम् → अथर्वणः."),
           "The second line builds up the thing declared: of life, a protector, a Veda, a subsidiary Veda, of Atharvan."),
        mcq("discriminate", 3, "Which is the right split of तान्दृष्ट्वैव?",
            ("तान् + दृष्ट्वा + एव", "आ + ए joins as ऐ, so दृष्ट्वा + एव is written दृष्ट्वैव."),
            [("ताः + दृष्ट्वा + एव", "ताः is feminine; the sages are masculine, तान्."),
             ("तान् + दृष्ट्वै + व", "व alone is not a word here."),
             ("तान् + दृष्टः + एव", "This would be written दृष्ट एव.")],
            "तान्दृष्ट्वैव = तान् (them) + दृष्ट्वा (having seen) + एव (at once).",
            "आ + ए → ऐ."),
        mcq("apply", 4,
            "दृष्ट्वा means 'having seen'. What does it tell us about the order of events?",
            ("Seeing came first, then declaring", "A 'having done' word names the act before the main verb."),
            [("Declaring came first, then seeing", "That would reverse the order."),
             ("Two persons did these two acts", "Both acts have the same doer."),
             ("The seeing never took place", "It is stated as done.")],
            "Indra saw, then spoke: दृष्ट्वा precedes निजगाद, and the doer is the same.",
            "-त्वा word: its act comes before the main verb, same doer."),
        mcq("transfer", 5,
            "Join गत्वा (having gone) and एव by the same sandhi. Which spelling results?",
            ("गत्वैव", "आ + ए gives ऐ, as in दृष्ट्वैव."),
            [("गत्वेव", "That would be अ + इ or ए, not आ + ए."),
             ("गत्वाव", "The ए does not vanish."),
             ("गत्वौव", "औ comes from आ + ओ or आ + औ.")],
            "The rule that gave दृष्ट्वैव works for any word ending in आ that meets ए.",
            "आ + ए → ऐ.",
            teaches="A word ending in आ followed by ए joins as ऐ: दृष्ट्वा + एव → दृष्ट्वैव, गत्वा + एव → गत्वैव."),
    ],
}

# ---------------------------------------------------------------- unit 19
AUTHORED["19"] = {
    "title": "कायबालग्रहोर्ध्वांगशल्यदंष्ट्राजरावृषैः",
    "question": "Which eight divisions does the verse name, and who understood the Veda?",
    "rule": ("The sacred Veda has attained the state of eight limbs through: body, child, seizers, "
             "upper part, dart, fang, old age and bull; the Grandfather understood it."),
    "limits": ("The eight terms are given in their literal senses; the verse does not explain "
               "them. 'Veda' is supplied from unit 18 as what gatam and yam refer to. पितामह "
               "is Brahmā by gloss in the data."),
    "explain_hi": ("यह श्लोक आठ विभाग गिनाता है: काय, बाल, ग्रह, ऊर्ध्वांग, शल्य, दंष्ट्रा, जरा और वृष। "
                   "इन विभागों से वह वेद ‘अष्टांगता’ (आठ अंगों की अवस्था) को प्राप्त हुआ। यहाँ आठों नाम शब्दार्थ "
                   "में दिए गए हैं, उनकी व्याख्या श्लोक नहीं करता। दूसरी पंक्ति में बताया है कि इस पवित्र "
                   "वेद को पितामह ने जाना (बुबुधे)। ‘वेद’ पिछले श्लोक से लिया गया है।"),
    "hook": "काय · बाल · ग्रह · ऊर्ध्वांग · शल्य · दंष्ट्रा · जरा · वृष → आठ अंग; जाना पितामह ने।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "A Veda has attained the state of eight limbs. Who understood it, according to the verse?",
            ("The Grandfather (Brahmā)", "यं पितामहः बुबुधे: which the Grandfather understood."),
            [("Indra", "Indra declared it in unit 18; the verse says the Grandfather understood it."),
             ("Dakṣa", "Dakṣa is not named in this verse."),
             ("Punarvasu", "Punarvasu is not named in this verse.")],
            "बुबुधे means understood, and its doer is पितामहः.",
            "पितामहः बुबुधे = the Grandfather understood."),
        match(1, "Match each term of the first line to its literal meaning.",
              [["काय", "body"], ["बाल", "child"], ["ग्रह", "seizers"],
               ["शल्य", "dart"], ["जरा", "old age"]],
              "Five of the eight terms; the verse does not explain how they are used.",
              "काय = body; बाल = child; ग्रह = seizers; शल्य = dart; जरा = old age."),
        ex(order(2, "Put the first seven terms in the verse's order.",
                 ["काय", "बाल", "ग्रह", "ऊर्ध्वांग", "शल्य", "दंष्ट्रा", "जरा"],
                 "The line runs: body, child, seizers, upper part, dart, fang, old age, and then bull.",
                 "काय → बाल → ग्रह → ऊर्ध्वांग → शल्य → दंष्ट्रा → जरा (→ वृष)."),
           "The eight terms are a fixed list; saying them in order is the way to hold them."),
        mcq("discriminate", 3, "Which is the right split of ग्रहोर्ध्वांग?",
            ("ग्रह + ऊर्ध्वांग", "अ + ऊ joins as ओ, so ग्रह + ऊर्ध्वांग is written ग्रहोर्ध्वांग."),
            [("ग्रहः + ऊर्ध्वांग", "This would be written ग्रह ऊर्ध्वांग."),
             ("ग्रहे + ऊर्ध्वांग", "This would be written ग्रहयूर्ध्वांग."),
             ("ग्रही + ऊर्ध्वांग", "This would be written ग्रह्यूर्ध्वांग.")],
            "ग्रहोर्ध्वांग = ग्रह (seizers) + ऊर्ध्वांग (upper part).",
            "अ + ऊ → ओ."),
        mcq("apply", 4,
            "Which word is the doer of बुबुधे ('understood')?",
            ("पितामहः", "The ending -ः marks the doer."),
            [("पुण्यम्", "The ending -म् marks the thing understood."),
             ("अष्टांगताम्", "This is the state attained, in -म् form."),
             ("गतम्", "This is the attained Veda, in -म् form.")],
            "पितामहः (the Grandfather) is the doer; यम् is the Veda he understood.",
            "Doer in -ः; the thing acted on in -म्."),
        mcq("transfer", 5,
            "Join वन (forest) and ऊर्ध्वम् (upward) by the same sandhi. Which spelling results?",
            ("वनोर्ध्वम्", "अ + ऊ gives ओ, as in ग्रहोर्ध्वांग."),
            [("वनूर्ध्वम्", "अ + ऊ does not give ऊ."),
             ("वनार्ध्वम्", "आ is for अ + अ."),
             ("वनौर्ध्वम्", "औ is for अ + ओ or अ + औ.")],
            "The sandhi in ग्रहोर्ध्वांग works the same on any word ending in अ.",
            "अ + ऊ → ओ.",
            teaches="A word ending in अ followed by ऊ joins as ओ: ग्रह + ऊर्ध्व → ग्रहोर्ध्व, वन + ऊर्ध्वम् → वनोर्ध्वम्."),
    ],
}

# ---------------------------------------------------------------- unit 20
AUTHORED["20"] = {
    "title": "गृहीत्वा ते तमाम्नायं प्रकाशं च परस्परं",
    "question": "What did the sages do with that teaching, and how are they described at the end?",
    "rule": ("Having received that traditional teaching, openly and mutually, ... the supreme sages "
             "(were) delighted. The second line is damaged in the print."),
    "limits": ("The word आयुःपूर्णानुषं is garbled in the scan, so the middle of line 2 and the "
               "meaning of लोकम् are not settled; no question rests on them. प्रकाशम् may be 'openly' "
               "or 'illumination'. Earlier translations that make the world delighted read "
               "मुदिताः wrongly."),
    "explain_hi": ("ऋषियों ने उस आम्नाय (परंपरा से आई शिक्षा) को ग्रहण किया; ‘गृहीत्वा’ पहले की क्रिया है। "
                   "‘परस्परम्’ का अर्थ है ‘आपस में’। ‘प्रकाशम्’ को ‘खुले रूप से’ पढ़ा गया है, पर वह ‘प्रकाश’ संज्ञा "
                   "भी हो सकता है। दूसरी पंक्ति का बीच का शब्द ‘आयुःपूर्णानुषं’ बिगड़ा हुआ है, इसलिए उसका अर्थ तय नहीं। "
                   "पक्का इतना है कि ‘मुदिताः’ (प्रसन्न) बहुवचन में ‘परमर्षयः’ के साथ है: परम ऋषि प्रसन्न हुए।"),
    "hook": "शिक्षा ग्रहण की · आपस में · प्रसन्न हुए परम ऋषि।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "After receiving the teaching, how are the supreme sages described?",
            ("Delighted", "मुदिताः परमर्षयः: the supreme sages, delighted."),
            [("Afraid", "No fear is mentioned."),
             ("Angry", "No anger is mentioned."),
             ("Doubtful", "No doubt is mentioned.")],
            "The last two words say the supreme sages were delighted.",
            "मुदिताः = delighted."),
        match(1, "Match each word to its meaning.",
              [["गृहीत्वा", "having received"], ["आम्नायम्", "traditional teaching"],
               ["परस्परम्", "mutually"], ["मुदिताः", "delighted"]],
              "The act, what was received, how, and the result.",
              "गृहीत्वा = having received; आम्नायम् = traditional teaching; परस्परम् = mutually; मुदिताः = delighted."),
        ex(order(2, "Put the first three words of the unit in order.",
                 ["गृहीत्वा", "ते", "तमाम्नायम्"],
                 "Having received, they, that teaching.",
                 "गृहीत्वा → ते → तमाम्नायम्."),
           "The unit opens with the act of receiving, then the receivers (ते), then what they received."),
        mcq("discriminate", 3, "Which is the right split of तमाम्नायम्?",
            ("तम् + आम्नायम्", "A final म् joins the next vowel: तम् + आम्नायम् is written तमाम्नायम्."),
            [("तस्य + आम्नायम्", "This would be written तस्याम्नायम्."),
             ("तान् + आम्नायम्", "This would be written तानाम्नायम्."),
             ("तमाम् + नायम्", "नायम् is not a word here.")],
            "तमाम्नायम् = तम् (that) + आम्नायम् (traditional teaching).",
            "म् + vowel: the म् is written with the vowel."),
        mcq("apply", 4,
            "The unit ends with मुदिताः परमर्षयः. Who is delighted?",
            ("The supreme sages", "मुदिताः is plural and goes with परमर्षयः."),
            [("The world (लोकम्)", "लोकम् ends in -म्, which marks a thing acted on, not the one delighted."),
             ("The teaching (आम्नायम्)", "आम्नायम् is what they received."),
             ("Nobody: it means forgotten", "मुदिताः means delighted.")],
            "मुदिताः and परमर्षयः are both plural and both name the sages.",
            "Describing word and noun agree: मुदिताः परमर्षयः."),
        mcq("transfer", 5,
            "In the invented line शिष्याः पाठं गृहीत्वा मुदिताः अभवन् (became), who is delighted, and when?",
            ("The pupils, after receiving the lesson", "गृहीत्वा comes first; मुदिताः goes with शिष्याः."),
            [("The lesson, after the pupils receive it", "पाठम् is what was received."),
             ("The pupils, before receiving the lesson", "गृहीत्वा names the earlier act."),
             ("The teacher, after giving the lesson", "No teacher is named.")],
            "As in the verse: a -त्वा word, then a describing word in -आः that agrees with the doers.",
            "-त्वा act first; -आः describing word agrees with the plural doers.",
            teaches="A 'having done' word (-त्वा) names the earlier act, and a plural describing word like मुदिताः goes with the plural doers (शिष्याः)."),
    ],
}

# ---------------------------------------------------------------- unit 21
AUTHORED["21"] = {
    "title": "स्थित्यर्थमायुर्वेदस्य तेऽथ तंत्राणि चक्रिरे",
    "question": "For what purpose did they compose treatises?",
    "rule": ("For the continuance of Āyurveda they then composed treatises. "
             "The second line begins a list of names whose text is doubtful."),
    "limits": ("The second line (कृत्वा ... सुश्रुतान्) is doubtful: the name मांब्य is probably "
               "mangled, the line is one syllable short, and 'having made' has no stated "
               "complement. This card asks only about the first line. The sentence runs into unit 22."),
    "explain_hi": ("पहली पंक्ति में उद्देश्य और क्रिया है: आयुर्वेद के ‘स्थित्यर्थम्’ यानी बने रहने के लिए, "
                   "उन्होंने तब ‘तंत्राणि’ (ग्रंथ) रचे। ‘चक्रिरे’ भूतकाल का रूप है: ‘उन्होंने रचा’। ‘तंत्राणि’ नपुंसक "
                   "बहुवचन है, इसलिए कई ग्रंथ। दूसरी पंक्ति में नामों की सूची है (अग्निवेश आदि), पर उसमें ‘मांब्य’ "
                   "बिगड़ा लगता है और पंक्ति अधूरी है, इसलिए इस कार्ड में उसका प्रश्न नहीं है।"),
    "hook": "आयुर्वेद के टिके रहने के लिए · तब · ग्रंथ रचे।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "For what purpose do they compose treatises, according to the first line?",
            ("For the continuance of Āyurveda", "स्थित्यर्थम् आयुर्वेदस्य: for the sake of its continuance."),
            [("For their own fame", "The line states no such purpose."),
             ("To end the teaching of Āyurveda", "The line says the opposite: its continuance."),
             ("For the pleasure of kings", "No king is mentioned.")],
            "The purpose is स्थिति, the staying on, of Āyurveda.",
            "स्थित्यर्थम् = for the sake of continuance."),
        match(1, "Match each word of the first line to its meaning.",
              [["स्थित्यर्थम्", "for the sake of continuance"], ["आयुर्वेदस्य", "of Āyurveda"],
               ["तंत्राणि", "treatises"], ["चक्रिरे", "they composed"]],
              "The purpose, whose, what, and the act.",
              "स्थित्यर्थम् = for continuance; आयुर्वेदस्य = of Āyurveda; तंत्राणि = treatises; चक्रिरे = they composed."),
        ex(order(2, "Put the words of the first line in the verse's order.",
                 ["स्थित्यर्थम्", "आयुर्वेदस्य", "तेऽथ", "तंत्राणि", "चक्रिरे"],
                 "Purpose, of Āyurveda, they then, treatises, composed.",
                 "स्थित्यर्थम् → आयुर्वेदस्य → तेऽथ → तंत्राणि → चक्रिरे."),
           "The line puts the purpose first and the act last: for continuance, of Āyurveda, they then, treatises, composed."),
        mcq("discriminate", 3, "Which is the right split of स्थित्यर्थम्?",
            ("स्थिति + अर्थम्", "इ before a different vowel becomes य्: स्थिति + अर्थम् is written स्थित्यर्थम्."),
            [("स्थित्य + अर्थम्", "This would be written स्थित्यार्थम्."),
             ("स्थितिः + अर्थम्", "This would be written स्थितिरर्थम्."),
             ("स्थिते + अर्थम्", "This would be written स्थितेऽर्थम्.")],
            "स्थित्यर्थम् = स्थिति (continuance) + अर्थम् (for the sake of).",
            "इ + other vowel → य् + vowel."),
        mcq("apply", 4,
            "तंत्राणि ends in the neuter plural -आणि, and चक्रिरे is a past form. What follows?",
            ("Several treatises were composed", "Plural noun and a past act."),
            [("One treatise was composed", "Plural -आणि does not mean one."),
             ("Treatises are still to be composed", "चक्रिरे is past, not future."),
             ("The treatises composed the sages", "तंत्राणि is the thing made, not the doers.")],
            "तंत्राणि is plural, so several treatises, and चक्रिरे says it was done.",
            "Neuter plural -आणि = several; चक्रिरे = they made (past)."),
        mcq("transfer", 5,
            "Join ते and अपि by the same sandhi as ते + अथ → तेऽथ. Which spelling results?",
            ("तेऽपि", "ए stays before अ, and the lost अ is marked by ऽ."),
            [("तयपि", "ए becomes अय् before other vowels, not before अ."),
             ("ताऽपि", "ए does not turn into आ."),
             ("तौपि", "ए does not turn into औ.")],
            "As ते + अथ gives तेऽथ, ते + अपि gives तेऽपि.",
            "ए + अ → ए + ऽ.",
            teaches="After ए an initial अ is dropped and marked by ऽ: ते + अथ → तेऽथ, ते + अपि → तेऽपि."),
    ],
}

# ---------------------------------------------------------------- unit 22
AUTHORED["22"] = {
    "title": "करालादींश्च सच्छिष्यान् ग्राहयामासुरादृताः",
    "question": "Whom did they cause to learn, and what did they then make?",
    "rule": ("And Karāla and others, as good disciples, they caused to learn (it), respectfully. "
             "Then they too each composed their own treatise."),
    "limits": ("ग्राहयामासुः has no stated object (the teaching is understood). आदृताः 'respectful' "
               "may describe the teachers or the pupils, so the card builds nothing on it. The "
               "sentence runs on: 'those that were composed' is the object of the verb in unit 23."),
    "explain_hi": ("पहली पंक्ति: कराल आदि अच्छे शिष्यों को ‘ग्राहयामासुः’ यानी सिखवाया, आदर के साथ। "
                   "यह प्रेरणार्थक रूप है: सिखाने वाले अलग, सीखने वाले अलग। दूसरी पंक्ति: फिर उन्होंने भी अपना-अपना "
                   "तंत्र रचा (‘स्वंस्वम्’ = हर एक का अपना)। ‘तानि कृतानि च’ (और रचे हुए वे) अगले श्लोक की क्रिया "
                   "का कर्म है। सन्धि: सत् + शिष्यान् → सच्छिष्यान्; ततः + ते → ततस्ते; चक्रुः + तानि → चक्रुस्तानि।"),
    "hook": "कराल आदि सुशिष्यों को सिखवाया · फिर अपना-अपना तंत्र रचा · और रचे हुए वे…",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Karāla and others are called good disciples. What is done for them?",
            ("They are made to learn it", "ग्राहयामासुः: they caused to learn."),
            [("They are sent away", "Nothing of the kind is said."),
             ("They are made kings", "No kingship is mentioned."),
             ("They are asked to be silent", "The verb is about learning.")],
            "The good disciples are made to learn the teaching.",
            "ग्राहयामासुः = they caused to learn."),
        match(1, "Match each word to its meaning.",
              [["सच्छिष्यान्", "good disciples"], ["ग्राहयामासुः", "they caused to learn"],
               ["स्वंस्वम्", "each his own"], ["चक्रुः", "they made"]],
              "The learners, the causing, the 'own', and the making.",
              "सच्छिष्यान् = good disciples; ग्राहयामासुः = caused to learn; स्वंस्वम् = each his own; चक्रुः = they made."),
        ex(order(2, "Put the phrases of the second line in the verse's order.",
                 ["स्वंस्वं तंत्रं", "ततः", "तेऽपि", "चक्रुः", "तानि कृतानि च"],
                 "Each his own treatise, then, they too, made, and those made.",
                 "स्वंस्वं तंत्रं → ततः → तेऽपि → चक्रुः → तानि कृतानि च."),
           "The second line goes: each his own treatise, then they too made (it), and those that were made."),
        mcq("discriminate", 3, "Which is the right split of सच्छिष्यान्?",
            ("सत् + शिष्यान्", "त् before श joins as च्छ: सत् + शिष्यान् is written सच्छिष्यान्."),
            [("सः + शिष्यान्", "This would be written स शिष्यान्."),
             ("सच् + शिष्यान्", "No such word सच् is given in the data."),
             ("सा + शिष्यान्", "This would be written सा शिष्यान्.")],
            "सच्छिष्यान् = सत् (good) + शिष्यान् (disciples).",
            "त् + श → च् + छ."),
        mcq("apply", 4,
            "ग्राहयामासुः means 'they caused to learn'. Who learns?",
            ("The disciples", "The causing is done to the disciples, who are in -आन् form."),
            [("The sages themselves", "They are the ones who cause."),
             ("Nobody learns", "The point of the act is that someone learns."),
             ("The treatises", "Treatises are things, not learners.")],
            "The sages are the doers of the causing; Karāla and the other disciples are the learners.",
            "Causing verb: one makes another learn."),
        mcq("transfer", 5,
            "Join ऋषयः and ते as in ततः + ते → ततस्ते. Which spelling results?",
            ("ऋषयस्ते", "A visarga before त becomes स्."),
            [("ऋषयोते", "ओ is for a voiced sound; त is not voiced."),
             ("ऋषयते", "The consonant स् is not dropped."),
             ("ऋषयश्ते", "श् is for च or छ, not for त.")],
            "ततः + ते gave ततस्ते; the same rule works here.",
            "ः + त → स् + त.",
            teaches="A visarga before त becomes स्: ततः + ते → ततस्ते, चक्रुः + तानि → चक्रुस्तानि, ऋषयः + ते → ऋषयस्ते."),
    ],
}

# ---------------------------------------------------------------- unit 23
AUTHORED["23"] = {
    "title": "गुरून् संश्रावयामासुः सर्षिसंघान्सुमेधसः",
    "question": "To whom did they recite the treatises, and what did the treatises gain?",
    "rule": ("The highly intelligent ones recited them to their teachers together with the assemblies "
             "of sages. Praised by them, those works of theirs gained standing on earth."),
    "limits": ("'Them' (the treatises) is supplied from unit 22. सर्षिसंघान् is read as a bahuvrīhi "
               "describing the teachers (together with groups of sages). Who exactly तैः means is "
               "by sense: the ones to whom the works were recited."),
    "explain_hi": ("पिछले श्लोक के ‘रचे हुए तंत्रों’ को सुमेधा (बुद्धिमान) शिष्यों ने गुरुओं को सुनाया, ऋषि-समूहों "
                   "सहित। ‘संश्रावयामासुः’ प्रेरणार्थक रूप है: ‘सुनवाया, सुनाया’। दूसरी पंक्ति में फल है: उनसे "
                   "(तैः) सराहे गए वे ग्रंथ पृथ्वी पर प्रतिष्ठा को प्राप्त हुए। क्रम इस प्रकार है: सुनाना, सराहना, "
                   "प्रतिष्ठा। सन्धि: तानि + एषाम् → तान्येषाम्।"),
    "hook": "गुरुओं और ऋषि-संघों को सुनाया → उनसे सराहे गए → पृथ्वी पर प्रतिष्ठा।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "To whom do the intelligent ones recite the treatises?",
            ("Their teachers, with assemblies of sages", "गुरून् सर्षिसंघान्: teachers together with groups of sages."),
            [("Kings and their courts", "No king is mentioned."),
             ("The common people", "No such listeners are named."),
             ("The two Aśvins", "They are named in unit 15, not here.")],
            "The works are recited to the teachers, who sit with groups of sages.",
            "गुरून् संश्रावयामासुः = they made the teachers hear."),
        match(1, "Match each word to its meaning.",
              [["गुरून्", "teachers"], ["संश्रावयामासुः", "made hear, recited"],
               ["सुमेधसः", "of good intelligence"], ["प्रशस्तानि", "praised"],
               ["लेभिरे", "obtained"]],
              "Five words that carry the sequence: recited, praised, obtained.",
              "गुरून् = teachers; संश्रावयामासुः = recited; सुमेधसः = of good intelligence; प्रशस्तानि = praised; लेभिरे = obtained."),
        ex(order(2, "Put the words of the second line in the verse's order.",
                 ["तैः", "प्रशस्तानि", "तान्येषाम्", "प्रतिष्ठाम्", "भुवि", "लेभिरे"],
                 "By them, praised, those of theirs, standing, on earth, obtained.",
                 "तैः → प्रशस्तानि → तान्येषाम् → प्रतिष्ठाम् → भुवि → लेभिरे."),
           "The second line runs: by them, praised, those works of theirs, standing, on earth, they obtained."),
        mcq("discriminate", 3, "Which is the right split of तान्येषाम्?",
            ("तानि + एषाम्", "इ before a different vowel becomes य्: तानि + एषाम् is written तान्येषाम्."),
            [("तान + एषाम्", "This would be written तानैषाम्."),
             ("तानि + ऐषाम्", "This would be written तान्यैषाम्."),
             ("तानः + एषाम्", "This would be written तान एषाम्.")],
            "तान्येषाम् = तानि (those) + एषाम् (of them).",
            "इ + other vowel → य् + vowel."),
        multi("apply", 4, "Which statements agree with this unit? Choose all that apply.",
              [("The treatises were recited to the teachers", "Stated in the first line."),
               ("The treatises were praised", "Stated: प्रशस्तानि."),
               ("The treatises gained standing on earth", "Stated: प्रतिष्ठां भुवि लेभिरे."),
               ("The treatises were kept secret from the sages", "The opposite: they were recited before groups of sages.")],
              [0, 1, 2],
              "The unit gives the order: recited, praised, standing gained.",
              "Recited → praised → gained standing."),
        mcq("transfer", 5,
            "Join पुस्तकानि and अपि by the same sandhi as तानि + एषाम् → तान्येषाम्. Which spelling results?",
            ("पुस्तकान्यपि", "इ before a different vowel becomes य्."),
            [("पुस्तकानपि", "The इ is not simply dropped."),
             ("पुस्तकानयपि", "The य् must join the consonant न्: न्य."),
             ("पुस्तकानीपि", "इ does not lengthen here.")],
            "तानि + एषाम् gave तान्येषाम्; the same rule works here.",
            "इ + other vowel → य् + vowel.",
            teaches="A final इ before a different vowel becomes य्: तानि + एषाम् → तान्येषाम्, पुस्तकानि + अपि → पुस्तकान्यपि."),
    ],
}

# ---------------------------------------------------------------- unit 24
AUTHORED["24"] = {
    "title": "तेषामेकैकमव्यापि समस्तव्याधिसोधने",
    "question": "What does the verse say about each single treatise, and about taking up each in turn?",
    "rule": ("Each one of them is not all-embracing for all diseases; but if each treatise is "
             "taken up in turn, there is a complete wasting of a man's life."),
    "limits": ("सोधने in the print is probably शोधने ('clearing') or साधने ('curing'); the card builds "
               "nothing on that word. पुरुषायुषसंक्षयः may also be read पुरुषायुषः संक्षयः. The reasoning "
               "continues in unit 25."),
    "explain_hi": ("पहली पंक्ति कहती है कि उन तंत्रों में से हर एक (एकैकम्) सब रोगों के लिए व्यापक नहीं है "
                   "(अव्यापि); रोग वाला अंतिम शब्द छपाई में संदिग्ध है (‘शोधन’ या ‘साधन’)। दूसरी पंक्ति में ‘तु’ "
                   "(परंतु) से बात पलटती है: हर तंत्र में अलग-अलग लगने पर पुरुष की आयु का पूरा क्षय हो जाता है। "
                   "‘प्रति-तंत्र’ का अर्थ है ‘हर तंत्र’। सन्धि: प्रतितंत्र + अभियोगे → प्रतितंत्राभियोगे।"),
    "hook": "हर तंत्र अधूरा · पर हर तंत्र में लगे तो आयु पूरी खप जाए।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "Does the verse say that each single treatise is all-embracing?",
            ("No: each is not all-embracing", "अव्यापि means not all-embracing."),
            [("Yes: each covers everything", "That is the opposite of अव्यापि."),
             ("It says nothing of treatises", "The word तेषाम् refers to the treatises."),
             ("Yes, but only the first one", "No treatise is singled out.")],
            "तेषाम् एकैकम् अव्यापि: of those, each one is not all-embracing.",
            "एकैकम् अव्यापि = each one is not all-embracing."),
        match(1, "Match each word of the verse to its meaning.",
              [["तेषाम्", "of those"], ["एकैकम्", "each one"],
               ["अव्यापि", "not all-embracing"], ["तु", "but"]],
              "Four small words that carry the whole turn of the argument.",
              "तेषाम् = of those; एकैकम् = each one; अव्यापि = not all-embracing; तु = but."),
        ex(order(2, "Put these five phrases of the verse in their order.",
                 ["तेषाम्", "एकैकम्", "अव्यापि", "प्रतितंत्राभियोगे", "पुरुषायुषसंक्षयः"],
                 "Of those, each one, not all-embracing; then, in pursuit of each treatise, loss of a man's life.",
                 "तेषाम् → एकैकम् → अव्यापि → प्रतितंत्राभियोगे → पुरुषायुषसंक्षयः."),
           "The two lines are held as two halves: each one is not all-embracing; pursuing each in turn wastes a man's life."),
        mcq("discriminate", 3, "Which is the right split of प्रतितंत्राभियोगे?",
            ("प्रतितंत्र + अभियोगे", "अ + अ joins as आ: प्रतितंत्र + अभियोगे is written प्रतितंत्राभियोगे."),
            [("प्रतितंत्री + अभियोगे", "This would be written प्रतितंत्र्यभियोगे."),
             ("प्रतितंत्रे + अभियोगे", "This would be written प्रतितंत्रेऽभियोगे."),
             ("प्रतितंत्र + भियोगे", "भियोगे is not a word.")],
            "प्रतितंत्राभियोगे = प्रतितंत्र (each treatise) + अभियोगे (in the pursuit).",
            "अ + अ → आ."),
        mcq("apply", 4,
            "What does the verse say happens if each treatise is taken up in turn?",
            ("A complete wasting of a man's life", "पुरुषायुषसंक्षयः: total loss of a man's life."),
            [("A man gains a long life", "The verse says the reverse."),
             ("All diseases go at once", "The first line says each one is not all-embracing."),
             ("The treatises merge into one", "Nothing like that is said.")],
            "तु ('but') turns the argument: pursuing each in turn uses up a man's whole life.",
            "प्रतितंत्राभियोगे तु = but in pursuing each treatise; result: loss of life."),
        mcq("transfer", 5,
            "On the pattern of प्रतितंत्र (for each treatise), what does प्रतिगृहम् mean?",
            ("In each house", "प्रति before a noun gives 'each, every'."),
            [("Many houses together", "प्रति does not mean 'many together'."),
             ("The owner of the house", "प्रति does not name an owner."),
             ("The best house", "प्रति does not mean 'best'.")],
            "प्रति + noun names each one of them: प्रतितंत्र each treatise, प्रतिगृहम् each house.",
            "प्रति + noun = each such thing.",
            teaches="प्रति before a noun gives 'each, every': प्रतितंत्र 'each treatise', प्रतिगृहम् 'each house'."),
    ],
}

# ---------------------------------------------------------------- unit 25
AUTHORED["25"] = {
    "title": "भवत्यध्ययनेनैव यस्मात्प्रोक्तः पुनःपुनः",
    "question": "Why does the verse say 'by study alone', and what have the authors stated?",
    "rule": ("It comes about by study alone, because that very matter has been stated again and "
             "again by the authors of the treatises, here and there with some special point."),
    "limits": ("The subject of भवति is not stated; the card keeps it as 'it' and does not say what "
               "comes about. The sentence follows unit 24 and goes on in the next verse."),
    "explain_hi": ("पहली पंक्ति कहती है कि यह ‘अध्ययन से ही’ होता है, और कारण (‘यस्मात्’ = क्योंकि) आगे है: "
                   "वही अर्थ (विषय) तंत्रकारों ने बार-बार (पुनःपुनः) कहा है। ‘प्रोक्तः’ ‘अर्थः’ के साथ चलता है। "
                   "दूसरी पंक्ति में जोड़ है: कहीं-कहीं कुछ विशेषता के साथ। ‘भवति’ का कर्ता श्लोक में नहीं "
                   "बताया गया। सन्धि: अध्ययनेन + एव → अध्ययनेनैव; एव + अर्थः → एवार्थः।"),
    "hook": "अध्ययन से ही · क्योंकि वही बात बार-बार कही · कहीं-कहीं कुछ विशेष।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Do the authors of the treatises state different matters, or the same matter?",
            ("The same matter, again and again", "स एवार्थः प्रोक्तः पुनःपुनः: that very matter, stated again and again."),
            [("Wholly different matters in each", "The verse says the very same matter."),
             ("Opposite matters that clash", "No clash is mentioned."),
             ("Nothing at all, they are silent", "The verse says it was stated.")],
            "The verse says the matter is the same, with some special point here and there.",
            "स एवार्थः = that very matter."),
        match(1, "Match each word to its meaning.",
              [["अध्ययनेन", "by study"], ["पुनःपुनः", "again and again"],
               ["तंत्रकारैः", "by the authors of treatises"], ["विशेषतः", "in particular"]],
              "The means, the repetition, the authors, and the added point.",
              "अध्ययनेन = by study; पुनःपुनः = again and again; तंत्रकारैः = by the authors; विशेषतः = in particular."),
        ex(order(2, "Put the phrases of the second line in the verse's order.",
                 ["तंत्रकारैः", "स एवार्थः", "क्वचित्", "कश्चित्", "विशेषतः"],
                 "By the authors, that very matter, somewhere, some, in particular.",
                 "तंत्रकारैः → स एवार्थः → क्वचित् → कश्चित् → विशेषतः."),
           "The second line says who, what, and then how it varies: somewhere some special point."),
        mcq("discriminate", 3, "Which is the right split of एवार्थः?",
            ("एव + अर्थः", "अ + अ joins as आ: एव + अर्थः is written एवार्थः."),
            [("एवः + अर्थः", "This would be written एवोऽर्थः."),
             ("एवे + अर्थः", "This would be written एवेऽर्थः."),
             ("एवौ + अर्थः", "This would be written एवावर्थः.")],
            "एवार्थः = एव (the very) + अर्थः (matter).",
            "अ + अ → आ."),
        mcq("apply", 4,
            "प्रोक्तः means 'stated'. Which noun of the second line does it go with?",
            ("अर्थः", "Both end in -ः: the matter is what is stated."),
            [("तंत्रकारैः", "This is 'by the authors', the ones who state."),
             ("अध्ययनेन", "This is 'by study', from line 1."),
             ("विशेषतः", "This is 'in particular', not a noun in the doer's form.")],
            "प्रोक्तः and अर्थः agree: the matter has been stated by the authors.",
            "Describing word and noun agree in form: प्रोक्तः ~ अर्थः."),
        mcq("transfer", 5,
            "On the pattern of तंत्रकारैः (by the authors of treatises), which word means by the authors of poems?",
            ("काव्यकारैः", "काव्य (poem) + कार (maker) + the 'by, many' ending -ऐः."),
            [("काव्यकारः", "This is one author, as the doer."),
             ("काव्यकारेण", "This is 'by one author'."),
             ("काव्यकारम्", "This is one author, the one acted on.")],
            "तंत्र + कारैः gives 'by the makers of treatises'; काव्य + कारैः gives 'by the makers of poems'.",
            "Work + कार + ऐः = by the makers of that work (many).",
            teaches="A word for a work plus कार ('maker') names its author, and -ऐः means 'by (many)': तंत्रकारैः, काव्यकारैः."),
    ],
}


NOTES_HI = {
    "14": ("विश्वास: मध्यम। छपी जोड़ी मीटर से एक पंक्ति खिसकी है: पंक्ति १.१६ श्लोक (इकाई १३) को पूरा करती है और "
           "पंक्ति १.१७ नया श्लोक शुरू करती है (अगली इकाई की पहली पंक्ति के साथ)। ‘सार्थं’ को ‘सह-अर्थम्’ (अर्थ सहित) "
           "पढ़ा गया है; ‘सार्थ’ (सार्थक, अमृत का विशेषण) भी सम्भव है। पुस्तक के हिन्दी-टिप्पण में ‘बुद्ध्वा’ की जगह "
           "‘स्मृत्वा’ सुझाया गया है; छपा ‘बुद्ध्वा’ रखा गया है। दोनों बातें संदिग्ध हैं, इसलिए दूसरी पंक्ति पर कोई प्रश्न नहीं बनाया गया। "
           "‘आयुर्वेदोपदेशेषु’ में अ + उ → ओ और ‘परमादरः’ में अ + आ → आ जाँचे गए।"),
    "15": ("विश्वास: उच्च। जोड़ी मीटर से एक पंक्ति खिसकी है: पंक्ति १.१८ पिछला श्लोक पूरा करती है और १.१९ नया श्लोक "
           "शुरू करती है (अगली इकाई के साथ)। ‘ददौ’ का कर्ता पिछली इकाई का ब्रह्मा है; ‘सः’ को दक्ष मानना अर्थ के आधार पर है। "
           "‘सोऽश्विभ्याम्’ = सः + अश्विभ्याम् (विसर्ग → ओ, अवग्रह)। दूसरी पंक्ति अधूरा वाक्य है, जो इकाई १६ में आगे बढ़ता है।"),
    "16": ("विश्वास: मध्यम। जोड़ी मीटर से एक पंक्ति खिसकी है (१.२० पिछले श्लोक की, १.२१ नए की)। सूची में ‘काश्यप’ और "
           "‘कश्यप’ दोनों छपे हैं (१६ अक्षर, छन्द ठीक); ये दो व्यक्ति हैं या एक नाम दोहराया गया है, यह अनिश्चित है, इसलिए इस पर "
           "प्रश्न नहीं बनाया गया। किसी दूसरे संस्करण से मिलान उचित होगा। सीमित क्रिया ‘उपाजग्मुः’ अगली इकाई में है। "
           "‘पुरस्कृत्य’ में -य रूप धातु के आगे ‘पुरस्’ होने से है।"),
    "17": ("विश्वास: उच्च। जोड़ी मीटर से एक पंक्ति खिसकी है (१.२२ पिछले श्लोक की, १.२३ नए की)। ‘तथा’लम्बायन’ में अवग्रह छपा है, "
           "जबकि तथा + अलम्बायन सामान्यतः ‘तथालम्बायन’ ही देता; इससे अर्थ नहीं बदलता। ‘महर्षयो’ में विसर्ग → ओ (घोष ‘म’ से पहले); "
           "‘शतक्रतुमुपाजग्मुः’ में म् + उ → मु; ‘अमरेश्वरम्’ में अ + ई → ए।"),
    "18": ("विश्वास: उच्च। जोड़ी मीटर से एक पंक्ति खिसकी है (१.२४ पिछले श्लोक की, १.२५ नए की)। ‘वेदम् उपवेदम्’ को ‘निजगाद’ के कर्म "
           "माना गया; ‘जिसे पितामह ने जाना’ वाला उपवाक्य अगली इकाई में है। ‘सहस्राक्ष’ = इंद्र, यह संदर्भ से है। छपाई में "
           "दंड ‘अथर्वणः’ से चिपका है। ‘तान्दृष्ट्वैव’ में आ + ए → ऐ; ‘सहस्राक्षो’ में विसर्ग → ओ।"),
    "19": ("विश्वास: उच्च। जोड़ी मीटर से एक पंक्ति खिसकी है (१.२६ पिछले श्लोक की, १.२७ नए की)। आठों पद शब्दार्थ में दिए गए हैं, "
           "तकनीकी व्याख्या नहीं की गई। ‘वेद’ पिछली इकाई से लिया गया है (‘गतम्’ और ‘यम्’ का पूर्वपद)। ‘ग्रहोर्ध्वांग’ में अ + ऊ → ओ; "
           "‘बुबुधेयम्’ = बुबुधे + यम्। श्लोक में आठ अंग ‘अष्टांगताम्’ से कहे गए हैं।"),
    "20": ("विश्वास: निम्न। जोड़ी मीटर से एक पंक्ति खिसकी है (१.२८ पिछले श्लोक की, १.२९ नए की)। ‘आयुःपूर्णानुषं’ बिगड़ा हुआ पाठ है "
           "(‘अनुष’ शब्द नहीं है); संभावित ‘आयुःपूर्णम् अनूनं’ पर सुझाव है, पर अनिश्चित, और ऐसा पढ़ने पर १७ अक्षर होते। "
           "इस पंक्ति पर कोई प्रश्न नहीं बनाया गया। ‘प्रकाशं’ के दो अर्थ संभव हैं (‘खुले रूप से’ या संज्ञा ‘प्रकाश’)। "
           "‘मुदिताः’ कर्ता ऋषियों के साथ बहुवचन विशेषण है; इसे सकर्मक पढ़ना (लोक को प्रसन्न किया) गलत है। "
           "‘परमर्षयः’ = परम + ऋषयः (अ + ऋ → अर्)।"),
    "21": ("विश्वास: निम्न। जोड़ी मीटर से एक पंक्ति खिसकी है (१.३० पिछले श्लोक की, १.३१ नए की)। दूसरी पंक्ति में ‘मांब्य’ नाम संभवतः "
           "बिगड़ा है (‘मांडव्य’ का अनुमान, पर निश्चित नहीं); पंक्ति में १५ अक्षर हैं, यानी एक कम। ‘कृत्वा’ का कोई पूरक नहीं दिया गया "
           "(‘शिष्य बनाकर’ अर्थ से समझा जाता है)। इसलिए प्रश्न केवल पहली पंक्ति पर हैं। ‘तेऽथ’ = ते + अथ; ‘स्थित्यर्थम्’ = स्थिति + अर्थम्।"),
    "22": ("विश्वास: मध्यम। जोड़ी मीटर से एक पंक्ति खिसकी है (१.३२ पिछले श्लोक की, १.३३ नए की)। ‘ग्राहयामासुः’ का कर्म नहीं दिया गया। "
           "‘आदृताः’ गुरुओं का भी विशेषण हो सकता है और शिष्यों का भी; ‘आदरपूर्वक’ ढीला अनुवाद है। ‘तानि कृतानि च’ अगली इकाई की "
           "क्रिया का कर्म है। सन्धि: करालादीन् + च → करालादींश्च; सत् + शिष्यान् → सच्छिष्यान्; ग्राहयामासुः + आदृताः → "
           "ग्राहयामासुरादृताः; ततः + ते → ततस्ते; चक्रुः + तानि → चक्रुस्तानि।"),
    "23": ("विश्वास: उच्च। जोड़ी मीटर से एक पंक्ति खिसकी है (१.३४ पिछले श्लोक की, १.३५ नए की)। ‘सर्षिसंघान्’ को बहुव्रीहि मानकर ‘गुरून्’ का "
           "विशेषण पढ़ा गया है (ऋषि-समूहों सहित गुरु); ‘उन्हें’ (तंत्रों) पिछली इकाई से लिया गया। ‘तैः’ किसे इंगित करता है, यह अर्थ के "
           "आधार पर है। ‘तान्येषाम्’ = तानि + एषाम् (इ → य्)।"),
    "24": ("विश्वास: मध्यम। जोड़ी मीटर से एक पंक्ति खिसकी है (१.३६ पिछले श्लोक की, १.३७ नए की)। पहली पंक्ति का अंतिम शब्द ‘सोधने’ संभवतः "
           "‘शोधने’ (छाँटना, निकालना) है, या ‘साधने’ (सिद्ध करना, ठीक करना); मीटर ‘साधने’ की ओर झुकता है, अर्थ दोनों चलता है। "
           "अनुवाद ‘शोधन’ का पक्ष लेता है; इस शब्द पर कोई प्रश्न नहीं बना। ‘पुरुषायुषसंक्षयः’ में समास ‘पुरुष-आयुष-संक्षयः’ पढ़ा गया; "
           "‘पुरुषायुषः संक्षयः’ (विसर्ग लुप्त) भी संभव है। ‘प्रतितंत्राभियोगे’ = प्रतितंत्र + अभियोगे।"),
    "25": ("विश्वास: मध्यम। जोड़ी मीटर से एक पंक्ति खिसकी है (१.३८ पिछले श्लोक की, १.३९ अगले श्लोक की शुरुआत)। ‘भवति’ का कर्ता नहीं दिया गया "
           "(संभवतः पिछली इकाई का आयु-क्षय, या विषय का ज्ञान), इसलिए अनुवाद ‘यह’ रखता है। ‘प्रोक्तः’ ‘अर्थः’ के साथ चलता है। "
           "‘कश्चित् विशेषतः’ = ‘कुछ विशेषता के साथ’। सन्धि: अध्ययनेन + एव → अध्ययनेनैव; एव + अर्थः → एवार्थः।"),
}

AIDS = {
    "14": {
        "chunks": "आयुर्वेदोपदेशेषु | विधेयः | परमादरः ‖ आयुर्वेदामृतं | सार्थं | ब्रह्मा | बुद्ध्वा | सनातनं ‖ (दूसरी पंक्ति का पाठ संदिग्ध)",
        "sandhi": "आयुर्वेद + उपदेशेषु → आयुर्वेदोपदेशेषु (अ + उ → ओ) · परम + आदरः → परमादरः (अ + आ → आ)।",
        "anchors": "उपदेश = उप + देश (पास से बताना) · विधेय = वि + धा (विधान करने योग्य) · आदर ← आ + दृ (ध्यान से सम्मान)।",
        "pegs": "मेरा बनाया चित्र: एक पुस्तक पर सबसे ऊपर रखा मुकुट, और उसके सामने झुका हुआ सिर: परम आदर।",
    },
    "15": {
        "diagram": {"steps": ["ब्रह्मा ने दिया (पिछली इकाई से)", "दक्ष को (दक्षाय)", "दोनों अश्विनों को (अश्विभ्याम्)", "शतक्रतु इंद्र को (शतक्रतवे)"]},
        "chunks": "ददौ दक्षाय | सोऽश्विभ्यां | तौ शतक्रतवे ततः ‖ धर्मार्थकाममोक्षाणां | विघ्नकारिभिरामयैः",
        "sandhi": "सः + अश्विभ्याम् → सोऽश्विभ्याम् (विसर्ग → ओ, अ का ऽ) · विघ्नकारिभिः + आमयैः → विघ्नकारिभिरामयैः (विसर्ग → र् स्वर से पहले)।",
        "letters": "द-अ-शत: ददौ, दक्ष, अश्विनौ, शतक्रतु: चार नामों की कड़ी (मेरा बनाया सूत्र, श्लोक में नहीं)।",
        "pegs": "मेरा बनाया चित्र: एक दीया हाथ से हाथ में जाता हुआ: ब्रह्मा, दक्ष, दो अश्विन, इंद्र।",
    },
    "16": {
        "chunks": "नरेषु पीड्यमानेषु | पुरस्कृत्य पुनर्वसुं ‖ धन्वन्तरि | भरद्वाज | निमि | काश्यप | कश्यपाः",
        "sandhi": "पुरस्कृत्य में -य (-त्वा नहीं) क्योंकि धातु के आगे ‘पुरस्’ जुड़ा है · धन्वन्तरि-भरद्वाज-निमि-काश्यप-कश्यपाः एक समस्त पद है।",
        "frame": "जब कुछ लोग (नरेषु) किसी स्थिति में हों (पीड्यमानेषु), तब वाक्य का साँचा: ‘…होने पर, X को आगे करके, …’। (मेरा बनाया साँचा)",
        "puns": "केवल सुनने की सहायता (मेरी बनाई): ‘पुर’ = आगे, ‘कृत्य’ = करके → पुरस्कृत्य = आगे करके।",
    },
    "17": {
        "diagram": {"steps": ["महर्षि, महात्मा और आलम्बायन आदि", "पास पहुँचे (उपाजग्मुः)", "शतक्रतु: शरण्य, अमरेश्वर"]},
        "chunks": "महर्षयो महात्मानः | तथा आलम्बायनादयः ‖ शतक्रतुम् उपाजग्मुः | शरण्यम् अमरेश्वरम्",
        "sandhi": "महर्षयः + महात्मानः → महर्षयो महात्मानः (विसर्ग → ओ) · शतक्रतुम् + उपाजग्मुः → शतक्रतुमुपाजग्मुः (म् + उ → मु) · अमर + ईश्वरम् → अमरेश्वरम् (अ + ई → ए)।",
        "anchors": "शरण्य ← शरण (आश्रय) · अमरेश्वर = अमर (जो न मरे) + ईश्वर (स्वामी)।",
    },
    "18": {
        "chunks": "तान् दृष्ट्वा एव | सहस्राक्षो | निजगाद | यथागमम् ‖ आयुषः पालकं | वेदम् | उपवेदम् | अथर्वणः",
        "sandhi": "तान् + दृष्ट्वा + एव → तान्दृष्ट्वैव (आ + ए → ऐ) · यथा + आगमम् → यथागमम् (आ + आ → आ) · सहस्राक्षः → सहस्राक्षो (विसर्ग → ओ)।",
        "anchors": "सहस्र-अक्ष = हज़ार आँखों वाला · आगम = परंपरा से आया (आ + गम्) · पालक ← पाल् (रक्षा करना)।",
        "pegs": "मेरा बनाया चित्र: हज़ार आँखों वाला इंद्र जैसे ही ऋषियों को देखता है, एक वेद-ग्रंथ हाथ में उठा लेता है।",
    },
    "19": {
        "diagram": {"groups": [{"label": "आठ विभाग (शब्दार्थ)", "items": ["काय", "बाल", "ग्रह", "ऊर्ध्वांग", "शल्य", "दंष्ट्रा", "जरा", "वृष"]}]},
        "chunks": "काय | बाल | ग्रह | ऊर्ध्वांग | शल्य | दंष्ट्रा | जरा | वृषैः ‖ गतम् अष्टांगताम् | पुण्यं | बुबुधे यं पितामहः",
        "sandhi": "ग्रह + ऊर्ध्वांग → ग्रहोर्ध्वांग (अ + ऊ → ओ) · बुबुधे + यम् → बुबुधेयम् (ए + य: कोई परिवर्तन नहीं)।",
        "letters": "काबाग्रऊश-दंजवृ: आठ नामों के पहले अक्षर जोड़कर बना मेरा बनाया सूत्र (श्लोक में नहीं)।",
        "pegs": "मेरा बनाया चित्र: एक आठ-हाथ वाली आकृति: शरीर, बच्चा, पकड़ने वाले, ऊपरी भाग, काँटा, दाँत, बूढ़ा, बैल।",
    },
    "20": {
        "chunks": "गृहीत्वा | ते | तम् आम्नायम् | प्रकाशं च | परस्परम् ‖ (बीच का शब्द बिगड़ा) | लोकम् | मुदिताः | परमर्षयः",
        "sandhi": "तम् + आम्नायम् → तमाम्नायम् (म् + आ) · परम + ऋषयः → परमर्षयः (अ + ऋ → अर्)।",
        "anchors": "आम्नाय ← आ + म्ना (बार-बार दोहराकर सीखा) · परस्पर = एक-दूसरे का · मुदित ← मुद् (प्रसन्न होना)।",
    },
    "21": {
        "chunks": "स्थित्यर्थम् | आयुर्वेदस्य | तेऽथ | तंत्राणि | चक्रिरे ‖ (दूसरी पंक्ति संदिग्ध, नामों की सूची)",
        "sandhi": "स्थिति + अर्थम् → स्थित्यर्थम् (इ → य्) · ते + अथ → तेऽथ (ए के बाद अ का लोप, ऽ)।",
        "anchors": "स्थिति = टिके रहना · तंत्र = ग्रंथ/शास्त्र · चक्रिरे ← कृ (करना), भूतकाल।",
        "frame": "उद्देश्य → कर्ता → क्या रचा → क्रिया: ‘X के लिए, वे, ग्रंथ, रचे’। (मेरा बनाया साँचा)",
    },
    "22": {
        "chain": {"steps": ["कराल आदि सुशिष्य (सच्छिष्यान्)", "उन्हें सिखवाया (ग्राहयामासुः)", "तब उन्होंने भी अपना-अपना तंत्र रचा", "और रचे हुए वे… (अगली इकाई में)"]},
        "chunks": "करालादींश्च | सच्छिष्यान् | ग्राहयामासुः | आदृताः ‖ स्वंस्वं तंत्रं | ततस्तेऽपि | चक्रुः | तानि कृतानि च",
        "sandhi": "सत् + शिष्यान् → सच्छिष्यान् · ततः + ते → ततस्ते · चक्रुः + तानि → चक्रुस्तानि · ग्राहयामासुः + आदृताः → ग्राहयामासुरादृताः।",
        "anchors": "ग्राहयामासुः = ग्रह् (लेना) का प्रेरणार्थक: ‘लिवाया, सिखवाया’ · स्वंस्वम् = अपना-अपना।",
    },
    "23": {
        "diagram": {"steps": ["गुरुओं और ऋषि-संघों को सुनाया", "उनसे सराहे गए (तैः प्रशस्तानि)", "पृथ्वी पर प्रतिष्ठा पाई (भुवि लेभिरे)"]},
        "chunks": "गुरून् संश्रावयामासुः | सर्षिसंघान् | सुमेधसः ‖ तैः प्रशस्तानि | तान्येषां | प्रतिष्ठां भुवि लेभिरे",
        "sandhi": "तानि + एषाम् → तान्येषाम् (इ → य्) · सर्षिसंघान् सुमेधसः: बीच में अलग शब्द, जुड़कर छपे।",
        "anchors": "सुमेधस् = सु + मेधा (अच्छी बुद्धि) · प्रतिष्ठा = प्रति + स्था (स्थिर खड़ा होना)।",
    },
    "24": {
        "contrast": {"groups": [{"label": "एक-एक तंत्र", "items": ["सब रोगों में व्यापक नहीं (अव्यापि)"]},
                                {"label": "हर तंत्र में लगना", "items": ["पुरुष की आयु का पूर्ण क्षय"]}]},
        "chunks": "तेषाम् | एकैकम् | अव्यापि | समस्तव्याधि… ‖ प्रतितंत्राभियोगे | तु | पुरुषायुषसंक्षयः",
        "sandhi": "प्रतितंत्र + अभियोगे → प्रतितंत्राभियोगे (अ + अ → आ) · एकैकम् + अव्यापि → एकैकमव्यापि (म् + अ)।",
        "anchors": "अव्यापि = अ + व्यापि (फैला हुआ नहीं) · संक्षय = सम् + क्षय (पूरी कमी) · प्रति- = हर एक।",
    },
    "25": {
        "chunks": "भवति अध्ययनेन एव | यस्मात् | प्रोक्तः | पुनःपुनः ‖ तंत्रकारैः | स एवार्थः | क्वचित् कश्चित् विशेषतः",
        "sandhi": "अध्ययनेन + एव → अध्ययनेनैव (अ + ए → ऐ) · एव + अर्थः → एवार्थः (अ + अ → आ) · सः + एव → स एव (विसर्ग का लोप)।",
        "anchors": "पुनःपुनः = बार-बार · तंत्रकार = तंत्र + कार (रचने वाला) · विशेषतः = विशेष + तः (विशेष रूप से)।",
        "puns": "केवल सुनने की सहायता (मेरी बनाई): ‘अध्ययन-एव’ → ‘अध्ययनैव’: पढ़ाई ही।",
    },
}

IMAGE_SPECS = {
    ("15", "diagram"): {
        "file": "ch1b02-hand-down-15.svg",
        "alt": "Chain of receivers in verse 15: the giver of unit 14 gives to Daksha, Daksha to the two Ashvins, and the two to Shatakratu (Indra).",
        "type": "mermaid",
        "code": ('flowchart TD\n'
                 '  A["ब्रह्मा ने दिया<br/>(पिछली इकाई)"] --> B["दक्ष को"]\n'
                 '  B --> C["दोनों अश्विनों को"]\n'
                 '  C --> D["शतक्रतु इंद्र को"]\n'),
    },
    ("19", "diagram"): {
        "file": "ch1b02-eight-limbs-19.svg",
        "alt": "Mind map of verse 19: the eight limbs in order: body, child, seizers, upper part, dart, fang, old age, bull.",
        "type": "mermaid",
        "code": ('mindmap\n'
                 '  अष्टांग\n'
                 '    काय\n'
                 '    बाल\n'
                 '    ग्रह\n'
                 '    ऊर्ध्वांग\n'
                 '    शल्य\n'
                 '    दंष्ट्रा\n'
                 '    जरा\n'
                 '    वृष\n'),
    },
    ("22", "chain"): {
        "file": "ch1b02-learn-compose-22.svg",
        "alt": "Chain in verse 22: Karala and other good disciples are made to learn; then they too compose their own treatise.",
        "type": "chain",
        "title": "सिखवाना और रचना",
        "steps": ["कराल आदि सुशिष्य", "उन्हें सिखवाया", "अपना-अपना तंत्र रचा"],
    },
    ("23", "diagram"): {
        "file": "ch1b02-recite-praise-23.svg",
        "alt": "Flow in verse 23: the treatises are recited to the teachers with groups of sages, are praised by them, and gain standing on earth.",
        "type": "mermaid",
        "code": ('flowchart TD\n'
                 '  A["गुरुओं और ऋषि-संघों<br/>को सुनाया"] --> B["उनसे सराहे गए"]\n'
                 '  B --> C["पृथ्वी पर प्रतिष्ठा"]\n'),
    },
    ("24", "contrast"): {
        "file": "ch1b02-each-treatise-24.svg",
        "alt": "Table of verse 24: each treatise alone is not all-embracing; taking up each treatise in turn wastes a man's whole life.",
        "type": "table",
        "title": "एक-एक तंत्र बनाम हर तंत्र में लगना",
        "heads": ["स्थिति", "श्लोक का कथन"],
        "rows": [["एक-एक तंत्र", "सब रोगों में व्यापक नहीं"],
                 ["हर तंत्र में लगना", "पुरुष की आयु का पूर्ण क्षय"]],
    },
}
