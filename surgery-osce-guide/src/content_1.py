# -*- coding: utf-8 -*-
"""Topics 1-3. Step tuples: ('open'|'close'|None, html)."""

WIPER = ("open", "<b>WIPER</b> — <b>W</b>ash hands · <b>I</b>ntroduce yourself, confirm patient name &amp; DOB · "
         "<b>P</b>ermission: explain the examination and get consent (offer a chaperone) · "
         "<b>E</b>xpose {expose} · <b>R</b>eposition {position}. Ask: <i>“Any pain anywhere?”</i>")


def wiper(expose, position):
    return ("open", WIPER[1].format(expose=expose, position=position))


def closing(complete, inv, ddx="Give a short differential diagnosis"):
    return [
        ("close", "<b>Thank</b> the patient, <b>cover</b> them up and help them dress · <b>wash hands</b>."),
        ("close", "<b>Summarise</b> your positive and important negative findings to the examiner."),
        ("close", f"<b>Differential diagnosis</b> — {ddx}."),
        ("close", f"<b>To complete the examination</b> I would… {complete}"),
        ("close", f"<b>Investigations</b> — {inv}"),
    ]


TOPICS_A = [
# =====================================================================================
dict(
    id="pvd", num=1, title="Peripheral Vascular Disease",
    subtitle="Lower-limb arterial exam (acute &amp; chronic ischaemia) · peripheral pulses · varicose veins · leg swelling (DVT)",
    ar="فحص الطرف السفلي لمريض الأوعية: ابحث عن علامات نقص التروية الحاد (الـ <bdi dir='ltr'>6 Ps</bdi>) والمزمن (تغيّرات الجلد، القُرَح، ضعف النبض)، "
       "ثم افحص الدوالي (اختبار العاصبة/ترندلنبرغ) وتورّم الساق (الجلطة الوريدية العميقة ومقياس <bdi dir='ltr'>Wells</bdi>). "
       "القاعدة الذهبية: قارن دائماً بين الطرفين.",
    lookfor=[
        ("Inspection", ["Colour: pallor, cyanosis, dependent rubor", "Hair loss, thin shiny skin",
                        "Thickened / dystrophic toe-nails", "Ulcers – tips of toes, between toes, heels, pressure points",
                        "Gangrene (dry / wet) or previous amputations", "Muscle wasting (thigh, calf)",
                        "Scars – bypass grafts, vein harvest, fasciotomy", "Swelling / oedema",
                        "Venous changes – varicosities, haemosiderin, eczema, lipodermatosclerosis",
                        "Lift the heels &amp; part the toes – hidden ulcers"]),
        ("Palpation", ["Temperature (back of hand, compare sides)", "Capillary refill time (&lt; 2 s)",
                       "Femoral pulse (+ radio-femoral delay)", "Popliteal pulse", "Posterior tibial pulse",
                       "Dorsalis pedis pulse", "Abdominal aorta (AAA – expansile?)"]),
        ("Acute ischaemia – the 6 Ps", ["Pain", "Pallor", "Pulselessness", "Paraesthesia", "Paralysis",
                                        "Perishingly cold (poikilothermia)"]),
        ("Special tests", ["Auscultate for bruits (femoral, aorta)", "Buerger’s angle", "Buerger’s test (sunset foot)",
                           "ABPI with hand-held Doppler", "Sensation &amp; power"]),
        ("Varicose veins", ["Inspect STANDING – distribution GSV / SSV", "Skin changes in the gaiter area",
                            "Cough impulse at the saphenofemoral junction (SFJ)", "Tap test", "Tourniquet / Trendelenburg test",
                            "Doppler / duplex of the junctions"]),
        ("Leg swelling / DVT", ["Unilateral vs bilateral", "Pitting oedema (press 10 s over the tibia)",
                                "Calf circumference 10 cm below tibial tuberosity (≥ 3 cm difference)",
                                "Tenderness along the deep veins", "Dilated superficial (collateral) veins",
                                "Warmth / redness", "Wells score"]),
    ],
    procedures=[
        ("A. Arterial examination of the lower limb", [
            wiper("both legs from the groin to the toes (underwear on, groin covered with a sheet)", "supine, head on one pillow"),
            (None, "<b>General inspection</b> from the end of the bed: comfort, pain at rest (legs hanging over the bed edge), "
                   "nicotine-stained fingers, walking aids, oxygen, amputations, around the bed (GTN spray, cigarettes)."),
            (None, "<b>Close inspection</b> of both legs: colour, trophic changes, ulcers, gangrene, scars, wasting. "
                   "<b>Lift the heels and separate the toes.</b>"),
            (None, "<b>Temperature</b> – back of your hand, moving distal → proximal, comparing both legs at the same level."),
            (None, "<b>Capillary refill</b> – press the pulp of the big toe for 5 s; normal refill &lt; 2 s."),
            (None, "<b>Pulses</b> (always both sides): <b>femoral</b> at the mid-inguinal point; <b>popliteal</b> – knee flexed ~30°, "
                   "both thumbs on the tibial tuberosity, fingertips of both hands pressing into the popliteal fossa; "
                   "<b>posterior tibial</b> – behind the medial malleolus (one-third of the way to the Achilles tendon); "
                   "<b>dorsalis pedis</b> – lateral to the extensor hallucis longus tendon over the 1st intermetatarsal space."),
            (None, "Palpate the <b>abdominal aorta</b> (expansile mass = AAA) and check <b>radio-femoral delay</b>."),
            (None, "<b>Auscultate</b> for bruits over the femoral arteries (and aorta / iliacs)."),
            (None, "<b>Buerger’s test</b>: raise both legs slowly; note the angle at which the foot turns pale "
                   "(<b>Buerger’s angle &lt; 20° = severe ischaemia</b>). Then sit the patient up with legs hanging: "
                   "reactive hyperaemia (<i>sunset foot</i>) confirms ischaemia."),
            (None, "<b>Neurology</b>: light-touch sensation and active movement of toes (paraesthesia / paralysis = threatened limb)."),
            (None, "State: <i>“I would measure the <b>ABPI</b> with a hand-held Doppler.”</i>"),
            *closing("examine the cardiovascular system, the abdomen (AAA) and do a neurological exam of the lower limbs; measure ABPI.",
                     "bedside: ABPI, ECG, BM/HbA1c; bloods: FBC, U&amp;E, lipids, clotting; imaging: arterial duplex, CT angiography / MR angiography.",
                     "chronic limb ischaemia (intermittent claudication / critical limb ischaemia) vs acute limb ischaemia (embolus / thrombosis)"),
        ]),
        ("B. Varicose veins", [
            wiper("both legs from the groin to the toes", "<b>standing</b> on a step"),
            (None, "<b>Inspect standing</b> from front and back: distribution – <b>GSV</b> (medial leg &amp; thigh) vs <b>SSV</b> "
                   "(posterior calf); saphena varix in the groin; skin changes in the gaiter area (haemosiderin, venous eczema, "
                   "lipodermatosclerosis, atrophie blanche, venous ulcer above the medial malleolus)."),
            (None, "<b>Palpate</b>: warmth/tenderness (thrombophlebitis), pitting oedema, <b>cough impulse</b> at the SFJ "
                   "(2–3 cm below and lateral to the pubic tubercle)."),
            (None, "<b>Tap test</b>: tap the upper end of the varicosity and feel the impulse distally – transmitted = incompetent valves."),
            (None, "<b>Tourniquet test</b>: patient lying, raise the leg to empty the veins, apply a tourniquet just below the SFJ, "
                   "then stand the patient. Veins stay empty → SFJ incompetence controlled; veins fill → incompetent perforator "
                   "below the tourniquet. Repeat lower down (mid-thigh, below knee)."),
            (None, "<b>Trendelenburg test</b>: same as above using your fingers pressing on the SFJ instead of a tourniquet."),
            (None, "State: <i>“I would use a hand-held Doppler at the SFJ and SPJ.”</i>"),
            *closing("perform a full arterial exam (before compression stockings), abdominal and pelvic exam (masses causing venous obstruction).",
                     "venous duplex ultrasound (gold standard), ABPI before compression therapy.",
                     "primary varicose veins (GSV/SSV incompetence) vs secondary (post-DVT, pelvic mass, AV fistula)"),
        ]),
        ("C. Lower-limb swelling / suspected DVT", [
            wiper("both legs from the groin to the toes", "supine"),
            (None, "<b>Inspect</b>: unilateral or bilateral swelling, erythema, dilated superficial veins, skin changes, scars, "
                   "plaster cast marks."),
            (None, "<b>Temperature</b> and <b>tenderness</b> along the course of the deep veins (calf, popliteal fossa, femoral vein)."),
            (None, "<b>Pitting oedema</b>: press firmly with your thumb over the lower tibia for 10 s – note the level up to which pitting extends."),
            (None, "<b>Measure calf circumference</b> 10 cm below the tibial tuberosity on both legs (≥ 3 cm difference is significant)."),
            (None, "Calculate the <b>Wells score</b> (see table)."),
            *closing("examine the abdomen and pelvis (mass compressing veins), the chest (PE), cardiovascular system (heart failure) and check for cancer.",
                     "Wells ≥ 2: proximal leg vein <b>duplex ultrasound</b> (within 4 h); Wells ≤ 1: <b>D-dimer</b>, if positive → duplex. "
                     "Also FBC, U&amp;E, LFT, clotting before anticoagulation.",
                     "DVT, cellulitis, ruptured Baker’s cyst, haematoma, lymphoedema; bilateral = heart / liver / kidney failure, hypoalbuminaemia, drugs (amlodipine)"),
        ]),
    ],
    figures=[
        ("pvd_temperature", "Back of the hand, distal → proximal, comparing both legs at the same level."),
        ("pvd_cap_refill", "Capillary refill – press the pulp of the big toe for 5 s, release, count (normal &lt; 2 s)."),
        ("pvd_femoral_pulse", "Femoral pulse – fingertips at the mid-inguinal point (midway between ASIS and pubic symphysis)."),
        ("pvd_popliteal_pulse", "Popliteal pulse – knee flexed ~30°, both thumbs on the tibial tuberosity, fingertips of both hands pressing into the popliteal fossa."),
        ("pvd_pt_pulse", "Posterior tibial pulse – behind the medial malleolus, one-third of the way to the Achilles tendon."),
        ("pvd_dp_pulse", "Dorsalis pedis pulse – index and middle fingertips just lateral to the extensor hallucis longus tendon."),
        ("pvd_buerger", "Buerger’s test – raise the leg and note the angle at which the sole turns pale."),
        ("pvd_tourniquet", "Tourniquet test – empty the veins, tourniquet below the SFJ, then stand the patient."),
        ("pvd_pitting", "Pitting oedema – firm thumb pressure over the lower tibia for 10 s."),
        ("pvd_calf_measure", "Calf circumference 10 cm below the tibial tuberosity – compare both sides."),
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
        dict(title="ABPI (ankle-brachial pressure index) = ankle systolic ÷ brachial systolic",
             head=["ABPI", "Interpretation", "Typical clinical picture"],
             rows=[["&gt; 1.3", "Non-compressible, calcified arteries – unreliable", "Diabetes, chronic kidney disease (use toe pressures)"],
                   ["1.0 – 1.3", "Normal", "—"],
                   ["0.9 – 0.99", "Borderline", "Usually asymptomatic"],
                   ["0.5 – 0.9", "Mild–moderate PAD", "Intermittent claudication"],
                   ["&lt; 0.5", "Severe PAD / critical limb ischaemia", "Rest pain, ulceration, gangrene"]]),
        dict(title="Wells score for DVT", head=["Clinical feature", "Points"],
             rows=[["Active cancer (treatment within 6 months or palliative)", "+1"],
                   ["Paralysis, paresis or recent plaster immobilisation of the leg", "+1"],
                   ["Recently bedridden ≥ 3 days or major surgery within 12 weeks", "+1"],
                   ["Localised tenderness along the deep venous system", "+1"],
                   ["Entire leg swollen", "+1"],
                   ["Calf swelling ≥ 3 cm compared with the other leg (10 cm below tibial tuberosity)", "+1"],
                   ["Pitting oedema confined to the symptomatic leg", "+1"],
                   ["Collateral superficial veins (non-varicose)", "+1"],
                   ["Previously documented DVT", "+1"],
                   ["An alternative diagnosis at least as likely as DVT", "−2"],
                   ["<b>Score ≥ 2 = DVT likely · Score ≤ 1 = DVT unlikely</b>", ""]]),
        dict(title="Acute vs chronic limb ischaemia", head=["", "Acute", "Chronic"],
             rows=[["Onset", "Sudden (hours)", "Gradual (months – years)"],
                   ["Cause", "Embolus (AF, MI) or thrombosis on plaque", "Atherosclerosis"],
                   ["Symptoms", "6 Ps", "Claudication → rest pain (worse at night, relieved by hanging the leg)"],
                   ["Skin", "White / mottled, cold", "Hairless, shiny, dystrophic nails, ulcers, gangrene"],
                   ["Collaterals", "None – limb threatened", "Developed"],
                   ["Management", "Emergency: heparin, embolectomy / thrombolysis", "Risk factors, exercise, revascularisation"]]),
        dict(title="Peripheral pulses – where to feel", head=["Pulse", "Surface landmark"],
             rows=[["Femoral", "Mid-inguinal point: midway between ASIS and pubic symphysis"],
                   ["Popliteal", "Deep in the popliteal fossa, knee flexed 30°, press against back of tibia"],
                   ["Posterior tibial", "Behind the medial malleolus, 1/3 of the way to the Achilles tendon"],
                   ["Dorsalis pedis", "Lateral to EHL tendon, over the 1st intermetatarsal space (absent in ~10% normally)"]]),
    ],
    checklist=["Washes hands, introduces self, confirms identity", "Explains, gains consent, offers chaperone",
               "Exposes legs adequately, positions supine", "Asks about pain", "General inspection from end of bed",
               "Inspects legs incl. between toes and heels", "Compares temperature (back of hand)", "Capillary refill time",
               "Femoral pulses (both)", "Popliteal pulses (both)", "Posterior tibial pulses", "Dorsalis pedis pulses",
               "Palpates abdominal aorta", "Auscultates for femoral bruits", "Buerger’s angle and test",
               "Sensation and movement of toes", "Mentions ABPI / Doppler", "Varicose veins: inspects standing, cough impulse, tap test",
               "Tourniquet / Trendelenburg test", "DVT: pitting oedema, calf measurement, Wells score",
               "Thanks patient, covers, washes hands", "Summarises, differential, completes exam, investigations"],
    links=[("Peripheral arterial examination", "peripheral arterial examination OSCE"),
           ("Varicose veins examination", "varicose veins examination OSCE tourniquet test"),
           ("DVT / leg swelling examination", "DVT examination OSCE Wells score")],
),
# =====================================================================================
dict(
    id="thy", num=2, title="Thyroid &amp; Cervical Lymph Nodes",
    subtitle="History of a neck swelling · hyper- and hypothyroidism · cervical lymphadenopathy · general &amp; local thyroid exam",
    ar="أمام تورّم في الرقبة اسأل: هل يتحرك مع البلع (الغدة الدرقية) أم مع إخراج اللسان (كيس القناة الدرقية اللسانية) أم هو عقدة لمفاوية؟ "
       "ثم حدّد الحالة الوظيفية للغدة (فرط أو قصور) من اليدين والنبض والعينين والمنعكسات، "
       "وافحص الغدة من الخلف والعقد اللمفاوية بترتيب ثابت.",
    lookfor=[
        ("History of neck swelling", ["Onset, duration, speed of growth", "Pain (thyroiditis, haemorrhage into a cyst)",
                                      "Pressure: dysphagia, dyspnoea / stridor", "Hoarseness (recurrent laryngeal nerve)",
                                      "Hyperthyroid symptoms", "Hypothyroid symptoms", "Radiation exposure, family history (MEN, thyroid cancer)",
                                      "Drugs: amiodarone, lithium, iodine, carbimazole", "B symptoms: fever, night sweats, weight loss (lymphoma / TB)",
                                      "Previous neck surgery"]),
        ("General exam – thyroid status", ["Behaviour: restless / slow", "Hands: tremor, sweaty or cold &amp; dry",
                                           "Thyroid acropachy, onycholysis, palmar erythema", "Pulse: rate, rhythm (AF)",
                                           "Eyes: exophthalmos, lid retraction, lid lag", "Eye movements (ophthalmoplegia)",
                                           "Hair &amp; skin (outer third of eyebrow loss)", "Reflexes: brisk vs slow-relaxing",
                                           "Proximal myopathy", "Pretibial myxoedema"]),
        ("Neck inspection", ["Site, size, shape of the swelling", "Moves on swallowing (thyroid)",
                             "Moves on tongue protrusion (thyroglossal cyst)", "Scars (collar incision)",
                             "Skin changes, visible veins", "Other lumps / lymph nodes", "Pemberton’s sign"]),
        ("Neck palpation (from behind)", ["Size &amp; shape (diffuse / nodular)", "Consistency", "Surface", "Tenderness",
                                          "Mobility on swallowing", "Lower border (retrosternal?)", "Tracheal position",
                                          "Cervical lymph nodes"]),
        ("Percussion &amp; auscultation", ["Percuss sternum – retrosternal extension", "Auscultate each lobe – bruit (Graves’)"]),
    ],
    procedures=[
        ("A. History of a neck swelling", [
            ("open", "Introduce yourself, confirm name / age / occupation, explain and get consent."),
            (None, "<b>Presenting complaint</b>: when and how noticed, duration, change in size (rapid = malignancy / haemorrhage), pain."),
            (None, "<b>Pressure symptoms</b>: difficulty swallowing, breathing (worse lying flat), voice change."),
            (None, "<b>Thyroid status</b>: weight change with appetite, heat / cold intolerance, sweating, palpitations, tremor, "
                   "diarrhoea / constipation, menstrual change, mood, eye symptoms."),
            (None, "<b>Risk factors for malignancy</b>: childhood neck irradiation, family history of thyroid cancer / MEN 2, "
                   "extremes of age, male sex, rapid growth, hoarseness, hard fixed lump."),
            (None, "<b>Systemic</b>: fever, night sweats, weight loss (lymphoma, TB), other lumps."),
            (None, "<b>PMH / drugs / FH / social</b>: autoimmune disease, amiodarone, lithium, iodine; smoking (Graves’ eye disease)."),
            ("close", "<b>ICE</b> (ideas, concerns, expectations); <b>summarise</b> and give your provisional diagnosis."),
        ]),
        ("B. General &amp; local examination of the thyroid", [
            wiper("the neck down to the clavicles", "sitting on a chair, with space behind them"),
            (None, "<b>General inspection</b>: body habitus, restlessness vs slowness, dress (heat / cold intolerance), voice."),
            (None, "<b>Hands</b>: warm and sweaty vs cold and dry, palmar erythema, acropachy, onycholysis. "
                   "<b>Fine tremor</b>: arms outstretched, paper on the dorsum of the hands."),
            (None, "<b>Pulse</b> (rate and rhythm – AF) and state you would check the blood pressure."),
            (None, "<b>Eyes</b>: inspect from the front, side and above (exophthalmos), lid retraction, <b>lid lag</b> "
                   "(follow your finger moving down), <b>eye movements</b> (H-pattern, ask about double vision)."),
            (None, "<b>Neck inspection</b> from the front and side; ask the patient to take a sip of water, hold it, "
                   "then <b>swallow</b> – watch the swelling rise. Ask the patient to <b>stick out the tongue</b>."),
            (None, "<b>Palpate from behind</b>, neck slightly flexed: both hands, fingertips on each lobe and the isthmus; "
                   "describe size, shape, consistency, surface, tenderness; feel again while the patient swallows. "
                   "Can you get below the lower border?"),
            (None, "<b>Trachea</b>: fingertip in the suprasternal notch – central or deviated?"),
            (None, "<b>Cervical lymph nodes</b> from behind in a fixed order (see box)."),
            (None, "<b>Percuss</b> over the manubrium (dull = retrosternal extension). <b>Auscultate</b> each lobe for a bruit."),
            (None, "<b>Pemberton’s sign</b>: arms raised above the head for 1 min → facial plethora / distress = thoracic inlet obstruction."),
            (None, "<b>Reflexes</b> (ankle / biceps), <b>proximal myopathy</b> (stand from chair, arms crossed), <b>pretibial myxoedema</b>."),
            *closing("check the blood pressure, examine the cardiovascular system and the vocal cords (laryngoscopy before surgery).",
                     "TFTs (TSH, free T4 / T3), thyroid antibodies (TRAb, anti-TPO), ultrasound neck, <b>FNAC</b> (Bethesda), "
                     "radio-isotope scan (hot / cold nodule), CT neck/chest for retrosternal goitre, serum calcium.",
                     "simple multinodular goitre, Graves’ disease, solitary thyroid nodule (adenoma vs carcinoma), thyroiditis"),
        ]),
        ("C. Examination of cervical lymph nodes", [
            wiper("the neck down to the clavicles", "sitting on a chair; stand behind the patient"),
            (None, "Inspect the neck from the front for visible lumps, scars and skin changes."),
            (None, "From behind, with the pulps of the fingers of both hands (compare sides) feel in this order: "
                   "<b>submental → submandibular → pre-auricular → post-auricular → occipital → anterior cervical chain "
                   "(along sternomastoid) → posterior triangle → supraclavicular</b>."),
            (None, "For any node describe: <b>site, size, number, consistency, tenderness, fixity, matting, overlying skin</b>."),
            (None, "Left supraclavicular node (Virchow’s) = <b>Troisier’s sign</b> → think gastric / abdominal malignancy."),
            *closing("examine the drainage area (scalp, ear, oral cavity, throat, thyroid), other node groups (axillary, inguinal), "
                     "liver and spleen.",
                     "FBC + film, ESR / CRP, LDH, ultrasound, FNAC or excision biopsy, CXR, CT neck / chest / abdomen.",
                     "reactive lymphadenitis, TB, lymphoma, metastatic carcinoma"),
        ]),
    ],
    figures=[
        ("thy_swallow", "Inspection while the patient swallows a sip of water – a thyroid swelling rises."),
        ("thy_tongue", "Tongue protrusion – a thyroglossal cyst moves upwards."),
        ("thy_palpation", "Palpation from behind: neck slightly flexed, fingertips of both hands on the lobes."),
        ("thy_trachea", "Tracheal position – fingertip in the suprasternal notch."),
        ("thy_nodes", "Cervical lymph nodes – fingertip pulps from behind, in a fixed order."),
        ("thy_tremor", "Fine tremor – arms outstretched, sheet of paper on the hands."),
        ("thy_lidlag", "Lid lag – the patient follows your finger moving downwards."),
    ],
    map=dict(img="thy_neck_map", title="Anterior neck – patient sitting",
             markers=[(1, 50, 43.4), (2, 37.5, 55.3), (3, 50, 67.4), (4, 32.5, 73.7), (5, 40.5, 25.8), (6, 62.5, 36.8), (7, 80, 52.6), (8, 68, 65.8)],
             rows=[("Midline, below thyroid cartilage", "Thyroid isthmus; thyroglossal cyst (higher, moves with tongue)"),
                   ("Either side of the trachea", "Thyroid lobes – diffuse goitre, nodules"),
                   ("Lower neck / suprasternal notch", "Lower border of goitre, tracheal deviation"),
                   ("Above the clavicles &amp; sternum", "Collar scar, dilated veins (retrosternal goitre)"),
                   ("Below the jaw", "Submandibular / submental nodes"),
                   ("Along sternomastoid", "Anterior cervical chain nodes; branchial cyst (anterior border, upper third)"),
                   ("Posterior triangle", "Posterior triangle nodes, cystic hygroma"),
                   ("Left supraclavicular fossa", "Virchow’s node (Troisier’s sign)")]),
    tables=[
        dict(title="Hyperthyroidism vs hypothyroidism", head=["", "Hyperthyroid", "Hypothyroid"],
             rows=[["Weight / appetite", "Weight loss, ↑ appetite", "Weight gain, ↓ appetite"],
                   ["Temperature", "Heat intolerance, sweating", "Cold intolerance"],
                   ["Behaviour", "Anxious, restless, irritable", "Slow, lethargic, depressed"],
                   ["Hands", "Warm, sweaty, fine tremor, acropachy (Graves’)", "Cold, dry, puffy; carpal tunnel"],
                   ["Pulse", "Tachycardia, AF, bounding", "Bradycardia"],
                   ["Eyes", "Lid retraction, lid lag, exophthalmos (Graves’)", "Periorbital puffiness"],
                   ["Skin &amp; hair", "Thin hair, pretibial myxoedema (Graves’)", "Dry coarse skin, loss of outer third of eyebrows"],
                   ["Bowels", "Diarrhoea", "Constipation"],
                   ["Periods", "Oligo- / amenorrhoea", "Menorrhagia"],
                   ["Reflexes", "Brisk", "Slow-relaxing"],
                   ["Muscles", "Proximal myopathy", "Myopathy, hoarse voice"]]),
        dict(title="Neck lumps by position", head=["Position", "Likely diagnosis"],
             rows=[["Midline", "Thyroid isthmus, thyroglossal cyst (moves with tongue), dermoid cyst, Delphian node"],
                   ["Anterior triangle", "Thyroid lobe, reactive / malignant nodes, branchial cyst, carotid body tumour (pulsatile), salivary gland"],
                   ["Posterior triangle", "Lymph nodes (TB, lymphoma, metastases), cystic hygroma (transilluminates), cervical rib"],
                   ["Supraclavicular", "Virchow’s node (left), lung / breast metastases"]]),
        dict(title="Cervical lymph node groups &amp; drainage", head=["Group", "Drains"],
             rows=[["Submental", "Tip of tongue, floor of mouth, lower lip"],
                   ["Submandibular", "Face, cheek, upper lip, anterior tongue, gums"],
                   ["Pre- / post-auricular", "Scalp, ear, eyelids"],
                   ["Occipital", "Posterior scalp"],
                   ["Deep cervical (jugulodigastric)", "Tonsil, pharynx, larynx, thyroid"],
                   ["Supraclavicular", "Thorax, breast, abdomen (left – via thoracic duct)"]]),
    ],
    checklist=["Introduces self, consent, sits patient on a chair", "Exposes neck to clavicles", "General inspection",
               "Hands: temperature, sweating, acropachy, tremor (paper)", "Pulse rate and rhythm", "Eyes: exophthalmos, lid retraction",
               "Lid lag and eye movements", "Inspects neck from front and side", "Swallowing test (water)", "Tongue protrusion test",
               "Palpates thyroid from behind, neck flexed", "Palpates during swallowing, checks lower border",
               "Tracheal position", "Cervical lymph nodes in order", "Percussion over sternum", "Auscultation for bruit",
               "Pemberton’s sign", "Reflexes / proximal myopathy / shins", "Thanks, covers, washes hands",
               "Summary, differential, investigations (TFT, US, FNAC)"],
    links=[("Thyroid examination", "thyroid examination OSCE"),
           ("Cervical lymph node examination", "cervical lymph node examination OSCE"),
           ("Neck lump history", "neck lump history taking OSCE")],
),
# =====================================================================================
dict(
    id="git1", num=3, title="GIT (I): History &amp; General Examination",
    subtitle="Gastrointestinal history taking · general examination related to GI disease",
    ar="التاريخ المرضي للجهاز الهضمي يبدأ بالشكوى الرئيسية (غالباً ألم البطن – استخدم SOCRATES) ثم الأعراض المصاحبة وعلامات الخطر (ALARM). "
       "الفحص العام يبدأ من اليدين ثم الوجه والعينين والفم والرقبة والصدر بحثاً عن علامات أمراض الكبد المزمنة وفقر الدم وسوء التغذية.",
    lookfor=[
        ("History – associated GI symptoms", ["Nausea / vomiting / haematemesis", "Dysphagia / odynophagia", "Dyspepsia / heartburn",
                                              "Change in bowel habit", "PR bleeding / melaena", "Jaundice, dark urine, pale stools, itch",
                                              "Abdominal distension", "Appetite &amp; weight loss", "Fever"]),
        ("Red flags – ALARM", ["Anaemia", "Loss of weight", "Anorexia", "Recent onset / progressive symptoms",
                               "Melaena / haematemesis", "Swallowing difficulty (dysphagia), age &gt; 55"]),
        ("Hands &amp; arms", ["Clubbing", "Leukonychia (low albumin)", "Koilonychia (iron deficiency)", "Palmar erythema",
                              "Dupuytren’s contracture", "Asterixis (flapping tremor)", "Bruising, scratch marks", "Spider naevi, track marks"]),
        ("Face, eyes &amp; mouth", ["Scleral jaundice", "Conjunctival pallor", "Xanthelasma", "Angular stomatitis",
                                     "Glossitis, mouth ulcers", "Pigmentation, fetor hepaticus"]),
        ("Neck, chest &amp; legs", ["Virchow’s node (left supraclavicular)", "Gynaecomastia", "Spider naevi (&gt; 5 = significant)",
                                     "Loss of body hair", "Ankle oedema"]),
    ],
    procedures=[
        ("A. GI history taking", [
            ("open", "Introduce yourself, confirm <b>name, age, occupation, residence</b>; explain and get consent."),
            (None, "<b>Presenting complaint</b> in the patient’s words; for pain use <b>SOCRATES</b> (Site, Onset, Character, "
                   "Radiation, Associated symptoms, Time course, Exacerbating / relieving factors, Severity)."),
            (None, "<b>Associated GI symptoms</b>: vomiting (content, blood), dysphagia, dyspepsia, bowel habit, stool colour, "
                   "PR bleeding, melaena, jaundice (urine / stool colour, itching), distension, appetite, weight."),
            (None, "<b>Red flags</b> (ALARM) – ask specifically."),
            (None, "<b>Past history</b>: previous surgery and endoscopies, peptic ulcer, IBD, liver disease, gallstones, blood transfusions."),
            (None, "<b>Drug history</b>: NSAIDs, aspirin, steroids, anticoagulants, iron, opioids, laxatives, allergies."),
            (None, "<b>Family history</b>: colorectal / gastric cancer, IBD, polyposis, liver disease."),
            (None, "<b>Social</b>: alcohol (units/week), smoking, diet, travel, IV drug use, tattoos, sexual history (hepatitis), "
                   "<b>schistosomiasis exposure</b> (canal water)."),
            (None, "<b>Systemic review</b> + <b>ICE</b>."),
            ("close", "<b>Summarise</b> the history back to the examiner and give a differential diagnosis."),
        ]),
        ("B. General examination related to GI disease", [
            wiper("the hands, arms, face, neck and chest (keep the patient covered elsewhere)", "lying at 45°"),
            (None, "<b>End of the bed</b>: jaundice, cachexia, pallor, distress, position (lying still = peritonitis; "
                   "rolling = colic), abdominal distension, drips / drains / stoma bags."),
            (None, "<b>Hands</b>: nails (clubbing – Schamroth window test, leukonychia, koilonychia), palms (erythema, "
                   "Dupuytren’s), <b>asterixis</b> (arms out, wrists cocked back for 15 s)."),
            (None, "<b>Pulse</b>, <b>arms</b> (bruising, scratch marks, track marks, muscle wasting), state BP / temperature."),
            (None, "<b>Eyes</b>: ask the patient to look up and gently pull the lower lid down – <b>scleral jaundice</b>, "
                   "<b>conjunctival pallor</b>; xanthelasma, Kayser–Fleischer rings."),
            (None, "<b>Mouth</b>: angular stomatitis, glossitis, ulcers, pigmentation (Peutz–Jeghers), dentition, fetor hepaticus."),
            (None, "<b>Neck</b>: from behind, feel the <b>left supraclavicular fossa</b> (Virchow’s node – Troisier’s sign)."),
            (None, "<b>Chest</b>: spider naevi (SVC territory), gynaecomastia, loss of body hair."),
            (None, "<b>Legs</b>: pitting oedema."),
            *closing("proceed to the full abdominal examination including hernial orifices, external genitalia and PR.",
                     "FBC, LFT, U&amp;E, clotting (INR), albumin, amylase / lipase, hepatitis serology; ultrasound abdomen; "
                     "OGD / colonoscopy as indicated.",
                     "chronic liver disease, iron-deficiency anaemia (GI blood loss), GI malignancy"),
        ]),
    ],
    figures=[
        ("git1_hands", "Inspect the hands: nails, palms and finger clubbing (Schamroth window test)."),
        ("git1_asterixis", "Asterixis – arms outstretched, wrists dorsiflexed, watch for 15 s."),
        ("git1_eyes", "Conjunctival pallor and scleral jaundice – patient looks up, gently pull the lower lid down."),
        ("git1_virchow", "Left supraclavicular fossa from behind – Virchow’s node (Troisier’s sign)."),
    ],
    map=dict(img="git1_hand_map", title="Hands &amp; nails – what to look for",
             markers=[(1, 80, 12.2), (2, 25.1, 58.3), (3, 32.3, 60.3), (4, 67.7, 89.7), (5, 77.1, 80.8), (6, 27.1, 94.9)],
             rows=[("Nail shape (side view)", "Clubbing – IBD, cirrhosis, coeliac disease, GI lymphoma"),
                   ("Nail bed colour", "Leukonychia (hypoalbuminaemia)"),
                   ("Nail contour", "Koilonychia – spoon nails (iron deficiency)"),
                   ("Thenar / hypothenar eminences", "Palmar erythema (chronic liver disease, pregnancy)"),
                   ("Palmar fascia, ring finger", "Dupuytren’s contracture (alcohol)"),
                   ("Wrist / forearm", "Asterixis, scratch marks, bruising")]),
    tables=[
        dict(title="Signs of chronic liver disease", head=["Region", "Signs"],
             rows=[["Hands", "Clubbing, leukonychia, palmar erythema, Dupuytren’s, asterixis (decompensation)"],
                   ["Face", "Jaundice, spider naevi, parotid enlargement, fetor hepaticus"],
                   ["Chest", "Gynaecomastia, spider naevi, loss of body hair"],
                   ["Abdomen", "Hepatosplenomegaly, ascites, caput medusae, testicular atrophy"],
                   ["Legs", "Oedema, bruising"]]),
        dict(title="Jaundice – pre-hepatic vs hepatic vs post-hepatic", head=["", "Pre-hepatic", "Hepatic", "Post-hepatic (obstructive)"],
             rows=[["Cause", "Haemolysis", "Hepatitis, cirrhosis, drugs", "Stones, carcinoma head of pancreas, stricture"],
                   ["Urine", "Normal colour", "Dark", "Dark"],
                   ["Stool", "Normal", "Normal / pale", "Pale"],
                   ["Itching", "No", "±", "Yes"],
                   ["Bilirubin", "Unconjugated ↑", "Mixed", "Conjugated ↑, ALP / GGT ↑↑"]]),
        dict(title="GI causes of finger clubbing", head=["Group", "Examples"],
             rows=[["Bowel", "Crohn’s disease, ulcerative colitis, coeliac disease, GI lymphoma"],
                   ["Liver", "Cirrhosis (especially biliary cirrhosis)"],
                   ["Others to remember", "Lung cancer, bronchiectasis, cyanotic heart disease, endocarditis"]]),
    ],
    checklist=["Introduces self, confirms identity, consent", "Presenting complaint with SOCRATES",
               "Associated GI symptoms", "Asks red-flag (ALARM) symptoms", "Past medical &amp; surgical history",
               "Drug history and allergies", "Family history", "Social history incl. alcohol units",
               "Systemic review and ICE", "Summarises history", "General inspection from end of bed",
               "Inspects nails and palms; tests clubbing", "Tests for asterixis", "Eyes: jaundice and pallor",
               "Examines the mouth", "Feels left supraclavicular fossa", "Chest: spider naevi, gynaecomastia",
               "Checks for leg oedema", "Thanks, covers, washes hands", "Summary, differential, plan"],
    links=[("GI history taking", "gastrointestinal history taking OSCE"),
           ("GI general examination (hands, face)", "gastrointestinal examination OSCE hands clubbing asterixis")],
),
]
