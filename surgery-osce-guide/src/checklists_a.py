# -*- coding: utf-8 -*-
"""Checklist-driven content, topics 1-3.

Topic = dict(id, num, title, subtitle, ar, checklists=[(title, [(phase, note, [items])])], map, tables, links)
item  = (step, how / what you may find, optional figure id)
"""


def HELP(expose, position, hello="Introduce yourself, confirm name &amp; DOB, explain, gain consent (offer a chaperone)"):
    return ("HELP", "", [
        ("H — Hello", hello),
        ("E — Exposure", expose),
        ("L — Lighting", "Good light; privacy (curtains / door closed)"),
        ("P — Position", position + "; ask: <i>“Are you in any pain?”</i>"),
        ("Wash hands", "Before touching the patient"),
    ])


def END(complete, inv, ddx):
    return ("End of station", "", [
        ("Tell the examiner how you would complete", complete),
        ("Thank patient &amp; help them get dressed", "Cover the patient, wash hands"),
        ("Summary &amp; differential", ddx),
        ("Investigations", inv),
    ])


TOPICS_A = [
# =====================================================================================
dict(
    id="pvd", num=1, title="Peripheral Vascular Disease",
    subtitle="Lower-limb arterial exam (acute &amp; chronic ischaemia) · peripheral pulses · varicose veins · leg swelling (DVT)",
    ar="فحص الطرف السفلي لمريض الأوعية: ابحث عن علامات نقص التروية الحاد (الـ <bdi dir='ltr'>6 Ps</bdi>) والمزمن (تغيّرات الجلد، القُرَح، ضعف النبض)، "
       "ثم افحص الدوالي (اختبار العاصبة) وتورّم الساق (الجلطة الوريدية ومقياس <bdi dir='ltr'>Wells</bdi>). القاعدة الذهبية: قارن دائماً بين الطرفين.",
    checklists=[
        ("A. Arterial examination of the lower limb", [
            HELP("Both legs from groin to toes; groin covered with a sheet", "Supine, head on one pillow"),
            ("Inspection", "start from the end of the bed", [
                ("General look", "Comfort, rest pain (legs hanging off bed), nicotine stains, walking aids"),
                ("Colour", "Pallor, cyanosis, dependent rubor"),
                ("Trophic changes", "Hair loss, thin shiny skin, thick dystrophic nails"),
                ("Ulcers &amp; gangrene", "Toe tips, between toes, heels — <b>lift the heels &amp; part the toes</b>"),
                ("Scars &amp; amputations", "Bypass grafts, vein-harvest scars"),
                ("Muscle wasting / swelling", "Compare both sides"),
            ]),
            ("Palpation", "always compare both sides", [
                ("Temperature", "Back of hand, distal → proximal", "pvd_temperature"),
                ("Capillary refill", "Press big-toe pulp 5 s — normal &lt; 2 s", "pvd_cap_refill"),
                ("Femoral pulse", "Mid-inguinal point; check radio-femoral delay", "pvd_femoral_pulse"),
                ("Popliteal pulse", "Knee flexed 30°, thumbs on tibial tuberosity, fingertips press into the fossa", "pvd_popliteal_pulse"),
                ("Posterior tibial pulse", "Behind the medial malleolus", "pvd_pt_pulse"),
                ("Dorsalis pedis pulse", "Lateral to the EHL tendon", "pvd_dp_pulse"),
                ("Abdominal aorta", "Expansile mass = AAA"),
            ]),
            ("Auscultation", "", [
                ("Bruits", "Over the femoral arteries and the aorta"),
            ]),
            ("Special tests", "", [
                ("Buerger’s angle", "Raise the leg — pale at &lt; 20° = severe ischaemia", "pvd_buerger"),
                ("Buerger’s test", "Then legs hanging over the edge → reactive hyperaemia (<i>sunset foot</i>)"),
                ("Sensation &amp; movement of toes", "Paraesthesia / paralysis = threatened limb (acute ischaemia)"),
                ("ABPI", "State: <i>“I would measure the ABPI with a hand-held Doppler”</i>"),
            ]),
            END("Examine the cardiovascular system, abdomen (AAA) and lower-limb neurology",
                "ABPI, arterial duplex, CT angiography; FBC, lipids, HbA1c, ECG",
                "Chronic limb ischaemia (claudication → critical ischaemia) vs acute limb ischaemia (embolus / thrombosis)"),
        ]),
        ("B. Varicose veins", [
            HELP("Both legs from groin to toes", "<b>Standing</b>"),
            ("Inspection", "patient standing — front and back", [
                ("Distribution", "GSV (medial leg &amp; thigh) vs SSV (back of calf); saphena varix in the groin"),
                ("Skin of the gaiter area", "Haemosiderin, eczema, lipodermatosclerosis, venous ulcer above the medial malleolus"),
            ]),
            ("Palpation", "", [
                ("Warmth / tenderness", "Thrombophlebitis"),
                ("Pitting oedema", "Level of pitting"),
                ("Cough impulse at SFJ", "2–3 cm below and lateral to the pubic tubercle"),
                ("Tap test", "Tap the top of the vein, feel the impulse below = incompetent valves"),
            ]),
            ("Special tests", "", [
                ("Tourniquet test", "Lying, raise leg, tourniquet below SFJ, stand: stay empty = SFJ incompetence; fill = lower perforator", "pvd_tourniquet"),
                ("Trendelenburg test", "Same, with your fingers on the SFJ"),
                ("Doppler", "State: hand-held Doppler at the SFJ and SPJ"),
            ]),
            END("Full arterial exam (before compression stockings); abdominal and pelvic exam",
                "Venous duplex ultrasound (gold standard); ABPI before compression",
                "Primary varicose veins vs secondary (post-DVT, pelvic mass)"),
        ]),
        ("C. Leg swelling / suspected DVT", [
            HELP("Both legs from groin to toes", "Supine"),
            ("Inspection", "", [
                ("Swelling", "Unilateral or bilateral"),
                ("Skin", "Redness, dilated superficial veins, scars, plaster marks"),
            ]),
            ("Palpation", "", [
                ("Temperature", "Warm leg"),
                ("Tenderness", "Along the deep veins (calf, popliteal, femoral)"),
                ("Pitting oedema", "Firm thumb pressure over the tibia for 10 s", "pvd_pitting"),
                ("Calf circumference", "10 cm below the tibial tuberosity — ≥ 3 cm difference", "pvd_calf_measure"),
                ("Wells score", "Calculate it (see table)"),
            ]),
            END("Examine abdomen &amp; pelvis (mass), chest (PE), heart (failure)",
                "Wells ≥ 2 → duplex ultrasound; Wells ≤ 1 → D-dimer, if positive → duplex; FBC, U&amp;E, clotting",
                "DVT, cellulitis, ruptured Baker’s cyst, lymphoedema; bilateral → heart / liver / kidney failure"),
        ]),
    ],
    map=dict(img="pvd_inspection_map", title="Lower limbs – patient supine, viewed from above",
             markers=[(1, 35, 16), (2, 42.5, 37), (3, 57, 46), (4, 31, 52), (5, 71, 55), (6, 41, 79),
                      (7, 63, 80), (8, 33, 94), (9, 60, 95), (10, 26, 84)],
             rows=[("Groin (lift the gown edge)", "Femoral pulse, bypass scars, saphena varix, lymph nodes"),
                   ("Medial knee &amp; thigh (GSV course)", "Varicose veins, vein-harvest scar"),
                   ("Medial knee (other leg)", "Bypass / harvest scars – compare sides"),
                   ("Shins", "Pallor, hair loss, thin shiny skin, pitting oedema"),
                   ("Calves", "Muscle wasting (chronic) / swelling, redness (DVT)"),
                   ("Gaiter area, above medial malleolus", "Venous ulcer, haemosiderin, eczema, lipodermatosclerosis"),
                   ("Ankles", "Oedema – level of pitting"),
                   ("Toes &amp; between toes", "Arterial ulcers, gangrene, fungal infection"),
                   ("Toe-nails", "Thick dystrophic nails (chronic ischaemia)"),
                   ("Heels (lift them up!)", "Pressure ulcers – commonly missed")]),
    tables=[
        dict(title="ABPI = ankle systolic ÷ brachial systolic", head=["ABPI", "Meaning", "Clinical picture"],
             rows=[["&gt; 1.3", "Calcified, unreliable", "Diabetes, CKD (use toe pressures)"],
                   ["0.9 – 1.3", "Normal", "—"],
                   ["0.5 – 0.9", "Mild–moderate PAD", "Intermittent claudication"],
                   ["&lt; 0.5", "Severe PAD / critical ischaemia", "Rest pain, ulcers, gangrene"]]),
        dict(title="Wells score for DVT", head=["Feature", "Points"],
             rows=[["Active cancer", "+1"], ["Paralysis, paresis or recent leg plaster", "+1"],
                   ["Bedridden ≥ 3 days or major surgery &lt; 12 weeks", "+1"], ["Tenderness along the deep veins", "+1"],
                   ["Entire leg swollen", "+1"], ["Calf swelling ≥ 3 cm vs other leg", "+1"],
                   ["Pitting oedema in the symptomatic leg only", "+1"], ["Collateral superficial (non-varicose) veins", "+1"],
                   ["Previous DVT", "+1"], ["Alternative diagnosis at least as likely", "−2"],
                   ["<b>≥ 2 = DVT likely · ≤ 1 = unlikely</b>", ""]]),
        dict(title="Acute vs chronic limb ischaemia", head=["", "Acute", "Chronic"],
             rows=[["Onset", "Sudden (hours)", "Gradual (months – years)"],
                   ["Cause", "Embolus (AF) or thrombosis", "Atherosclerosis"],
                   ["Picture", "6 Ps: pain, pallor, pulseless, paraesthesia, paralysis, perishingly cold", "Claudication → rest pain, ulcers, trophic changes"],
                   ["Management", "Emergency: heparin, embolectomy", "Risk factors, exercise, revascularisation"]]),
    ],
    links=[("Arterial exam", "peripheral arterial examination OSCE"), ("Varicose veins", "varicose veins examination OSCE tourniquet test"),
           ("DVT / leg swelling", "DVT examination OSCE Wells score")],
),
# =====================================================================================
dict(
    id="thy", num=2, title="Thyroid &amp; Cervical Lymph Nodes",
    subtitle="History of a neck swelling · hyper- and hypothyroidism · cervical lymphadenopathy · general &amp; local thyroid exam",
    ar="أمام تورّم في الرقبة اسأل: هل يتحرك مع البلع (الغدة الدرقية) أم مع إخراج اللسان (كيس القناة الدرقية اللسانية) أم هو عقدة لمفاوية؟ "
       "ثم حدّد الحالة الوظيفية للغدة من اليدين والنبض والعينين، وافحص الغدة من الخلف والعقد اللمفاوية بترتيب ثابت.",
    checklists=[
        ("A. History of a neck swelling", [
            ("Introduction", "", [("Hello &amp; consent", "Name, age, occupation; explain")]),
            ("The swelling", "", [
                ("Onset &amp; duration", "When and how noticed"),
                ("Change in size", "Rapid growth = malignancy / bleed into a cyst"),
                ("Pain", "Thyroiditis, haemorrhage"),
            ]),
            ("Pressure symptoms", "", [
                ("Dysphagia", "Difficulty swallowing"),
                ("Dyspnoea / stridor", "Worse lying flat"),
                ("Hoarseness", "Recurrent laryngeal nerve → suspect malignancy"),
            ]),
            ("Thyroid status", "", [
                ("Hyperthyroid symptoms", "Weight loss, heat intolerance, palpitations, tremor, diarrhoea"),
                ("Hypothyroid symptoms", "Weight gain, cold intolerance, constipation, lethargy"),
                ("Eye symptoms", "Grittiness, protrusion, double vision (Graves’)"),
            ]),
            ("Background", "", [
                ("Malignancy risk", "Neck irradiation, family history (MEN 2)"),
                ("Drugs", "Amiodarone, lithium, iodine"),
                ("B symptoms", "Fever, night sweats, weight loss (lymphoma / TB)"),
            ]),
            ("End of station", "", [("ICE, summary &amp; provisional diagnosis", "")]),
        ]),
        ("B. General &amp; local examination of the thyroid", [
            HELP("Neck down to the clavicles", "Sitting on a chair with space behind"),
            ("General exam — thyroid status", "", [
                ("Behaviour", "Restless vs slow"),
                ("Hands", "Warm &amp; sweaty vs cold &amp; dry; acropachy, onycholysis"),
                ("Fine tremor", "Arms out, sheet of paper on the hands", "thy_tremor"),
                ("Pulse", "Rate and rhythm (AF)"),
                ("Eyes — inspection", "Exophthalmos (from side &amp; above), lid retraction"),
                ("Lid lag &amp; eye movements", "Follow finger downwards; H-pattern", "thy_lidlag"),
            ]),
            ("Neck inspection", "from the front and side", [
                ("Swelling", "Site, size, shape; scars, dilated veins"),
                ("Swallowing test", "Sip of water → thyroid swelling rises", "thy_swallow"),
                ("Tongue protrusion", "Thyroglossal cyst moves up", "thy_tongue"),
            ]),
            ("Palpation", "from behind, neck slightly flexed", [
                ("Thyroid lobes &amp; isthmus", "Size, shape, consistency, surface, tenderness", "thy_palpation"),
                ("Palpate while swallowing", "Can you get below the lower border?"),
                ("Trachea", "Fingertip in the suprasternal notch: central?", "thy_trachea"),
                ("Cervical lymph nodes", "In a fixed order (see C)", "thy_nodes"),
            ]),
            ("Percussion &amp; auscultation", "", [
                ("Percuss the manubrium", "Dull = retrosternal extension"),
                ("Auscultate each lobe", "Bruit = Graves’"),
            ]),
            ("Special tests", "", [
                ("Pemberton’s sign", "Arms up 1 min → facial plethora = thoracic inlet obstruction"),
                ("Reflexes, proximal myopathy, shins", "Slow-relaxing reflexes; stand from chair; pretibial myxoedema"),
            ]),
            END("Check BP, examine the heart, vocal cords (laryngoscopy)",
                "TFT (TSH, free T4), antibodies (TRAb, anti-TPO), neck ultrasound, FNAC, isotope scan, CT for retrosternal goitre",
                "Multinodular goitre, Graves’ disease, solitary nodule (adenoma vs carcinoma), thyroiditis"),
        ]),
        ("C. Cervical lymph nodes", [
            HELP("Neck down to the clavicles", "Sitting; stand behind the patient"),
            ("Palpation in order", "from behind, both hands, compare sides", [
                ("Submental", "Under the chin"),
                ("Submandibular", "Under the jaw"),
                ("Pre- &amp; post-auricular", "In front of and behind the ear"),
                ("Occipital", "Back of the head"),
                ("Anterior cervical chain", "Along sternomastoid"),
                ("Posterior triangle", "Behind sternomastoid"),
                ("Supraclavicular", "Left = Virchow’s node (Troisier’s sign)"),
                ("Describe any node", "Site, size, number, consistency, tenderness, fixity, matting, skin"),
            ]),
            END("Examine drainage area (scalp, mouth, throat), other node groups, liver &amp; spleen",
                "FBC, ESR, ultrasound, FNAC / excision biopsy, CT",
                "Reactive, TB, lymphoma, metastatic carcinoma"),
        ]),
    ],
    map=dict(img="thy_neck_map", title="Anterior neck – patient sitting",
             markers=[(1, 50, 43.4), (2, 37.5, 55.3), (3, 50, 67.4), (4, 32.5, 73.7), (5, 40.5, 25.8), (6, 62.5, 36.8), (7, 80, 52.6), (8, 68, 65.8)],
             rows=[("Midline, below thyroid cartilage", "Thyroid isthmus; thyroglossal cyst (higher, moves with tongue)"),
                   ("Either side of the trachea", "Thyroid lobes – diffuse goitre, nodules"),
                   ("Lower neck / suprasternal notch", "Lower border of goitre, tracheal deviation"),
                   ("Above the clavicles &amp; sternum", "Collar scar, dilated veins (retrosternal goitre)"),
                   ("Below the jaw", "Submandibular / submental nodes"),
                   ("Along sternomastoid", "Anterior chain nodes; branchial cyst"),
                   ("Posterior triangle", "Posterior triangle nodes, cystic hygroma"),
                   ("Left supraclavicular fossa", "Virchow’s node (Troisier’s sign)")]),
    tables=[
        dict(title="Hyperthyroidism vs hypothyroidism", head=["", "Hyperthyroid", "Hypothyroid"],
             rows=[["Weight", "Loss, ↑ appetite", "Gain"], ["Temperature", "Heat intolerance, sweating", "Cold intolerance"],
                   ["Hands", "Warm, sweaty, fine tremor", "Cold, dry"], ["Pulse", "Tachycardia, AF", "Bradycardia"],
                   ["Eyes", "Lid retraction, lid lag, exophthalmos", "Periorbital puffiness"],
                   ["Bowels", "Diarrhoea", "Constipation"], ["Reflexes", "Brisk", "Slow-relaxing"]]),
        dict(title="Neck lumps by position", head=["Position", "Likely diagnosis"],
             rows=[["Midline", "Thyroid isthmus, thyroglossal cyst, dermoid cyst"],
                   ["Anterior triangle", "Thyroid lobe, lymph nodes, branchial cyst, carotid body tumour"],
                   ["Posterior triangle", "Lymph nodes (TB, lymphoma), cystic hygroma"],
                   ["Supraclavicular", "Virchow’s node (left), lung / breast metastases"]]),
    ],
    links=[("Thyroid exam", "thyroid examination OSCE"), ("Cervical lymph nodes", "cervical lymph node examination OSCE"),
           ("Neck lump history", "neck lump history taking OSCE")],
),
# =====================================================================================
dict(
    id="git1", num=3, title="GIT (I): History &amp; General Examination",
    subtitle="Gastrointestinal history taking · general examination related to GI disease",
    ar="التاريخ المرضي للجهاز الهضمي: الشكوى الرئيسية (للألم استخدم <bdi dir='ltr'>SOCRATES</bdi>) ثم الأعراض المصاحبة وعلامات الخطر. "
       "الفحص العام: اليدين ثم العينين والفم والرقبة والصدر بحثاً عن علامات أمراض الكبد المزمنة وفقر الدم.",
    checklists=[
        ("A. GI history", [
            ("Introduction", "", [("Hello &amp; consent", "Name, age, occupation, residence")]),
            ("Presenting complaint", "", [
                ("Pain — SOCRATES", "Site, Onset, Character, Radiation, Associations, Time, Exacerbating/relieving, Severity"),
            ]),
            ("Associated GI symptoms", "", [
                ("Vomiting", "Content; haematemesis"),
                ("Dysphagia / dyspepsia", "Solids vs liquids; heartburn"),
                ("Bowel habit", "Diarrhoea / constipation, PR bleeding, melaena"),
                ("Jaundice", "Dark urine, pale stools, itching"),
                ("Distension, appetite, weight", ""),
            ]),
            ("Red flags — ALARM", "", [
                ("Ask specifically", "Anaemia, Loss of weight, Anorexia, Recent/progressive, Melaena, Swallowing difficulty"),
            ]),
            ("Background", "", [
                ("Past history", "Surgery, endoscopy, IBD, liver disease, transfusions"),
                ("Drugs", "NSAIDs, steroids, anticoagulants, iron"),
                ("Family history", "Colorectal cancer, IBD"),
                ("Social", "Alcohol units, smoking, travel, schistosomiasis (canal water)"),
            ]),
            ("End of station", "", [("Systemic review, ICE, summary &amp; differential", "")]),
        ]),
        ("B. General examination related to GI disease", [
            HELP("Hands, arms, face, neck, chest", "Lying at 45°"),
            ("End of bed", "", [
                ("General look", "Jaundice, cachexia, pallor, distress"),
                ("Position", "Lying still = peritonitis; restless = colic"),
            ]),
            ("Hands &amp; arms", "", [
                ("Nails", "Clubbing (Schamroth window), leukonychia, koilonychia", "git1_hands"),
                ("Palms", "Palmar erythema, Dupuytren’s contracture"),
                ("Asterixis", "Arms out, wrists cocked back 15 s", "git1_asterixis"),
                ("Arms", "Bruising, scratch marks; pulse (state BP, temperature)"),
            ]),
            ("Face", "", [
                ("Eyes", "Patient looks up, pull lower lid down: jaundice, pallor", "git1_eyes"),
                ("Mouth", "Angular stomatitis, glossitis, ulcers, fetor hepaticus"),
            ]),
            ("Neck, chest &amp; legs", "", [
                ("Left supraclavicular fossa", "Virchow’s node (Troisier’s sign)", "git1_virchow"),
                ("Chest", "Spider naevi, gynaecomastia, loss of body hair"),
                ("Legs", "Pitting oedema"),
            ]),
            END("Full abdominal exam, hernial orifices, genitalia and PR",
                "FBC, LFT, U&amp;E, INR, albumin; ultrasound; endoscopy",
                "Chronic liver disease, iron-deficiency anaemia, GI malignancy"),
        ]),
    ],
    map=dict(img="git1_hand_map", title="Hands &amp; nails – what to look for",
             markers=[(1, 80, 12.2), (2, 25.1, 58.3), (3, 32.3, 60.3), (4, 67.7, 89.7), (5, 77.1, 80.8), (6, 27.1, 94.9)],
             rows=[("Nail shape (side view)", "Clubbing – IBD, cirrhosis, coeliac disease"),
                   ("Nail bed colour", "Leukonychia (low albumin)"),
                   ("Nail contour", "Koilonychia – spoon nails (iron deficiency)"),
                   ("Thenar / hypothenar eminences", "Palmar erythema (chronic liver disease)"),
                   ("Palmar fascia, ring finger", "Dupuytren’s contracture (alcohol)"),
                   ("Wrist / forearm", "Asterixis, scratch marks, bruising")]),
    tables=[
        dict(title="Signs of chronic liver disease", head=["Region", "Signs"],
             rows=[["Hands", "Clubbing, leukonychia, palmar erythema, Dupuytren’s, asterixis"],
                   ["Face", "Jaundice, spider naevi, fetor hepaticus"], ["Chest", "Gynaecomastia, spider naevi, loss of body hair"],
                   ["Abdomen", "Hepatosplenomegaly, ascites, caput medusae"], ["Legs", "Oedema, bruising"]]),
        dict(title="Types of jaundice", head=["", "Pre-hepatic", "Hepatic", "Post-hepatic"],
             rows=[["Cause", "Haemolysis", "Hepatitis, cirrhosis", "Stones, cancer head of pancreas"],
                   ["Urine", "Normal", "Dark", "Dark"], ["Stool", "Normal", "Normal / pale", "Pale"],
                   ["Itching", "No", "±", "Yes"]]),
    ],
    links=[("GI history", "gastrointestinal history taking OSCE"), ("GI general exam", "gastrointestinal examination OSCE hands clubbing asterixis")],
),
]
