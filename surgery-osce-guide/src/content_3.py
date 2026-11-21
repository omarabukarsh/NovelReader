# -*- coding: utf-8 -*-
"""Topics 7-9."""
from content_1 import wiper, closing

TOPICS_C = [
# =====================================================================================
dict(
    id="breast", num=7, title="Breast &amp; Axillary Lymph Nodes",
    subtitle="History of a breast lump &amp; nipple discharge · breast examination · axillary node examination",
    ar="فحص الثدي يتم بوجود مرافِقة وبعد الموافقة: النظر في أربع وضعيات، ثم الجسّ بباطن الأصابع الثلاثة الوسطى لكل الأرباع والذيل الإبطي "
       "مع البدء بالثدي السليم، ثم فحص مجموعات العقد الإبطية الخمس وفوق الترقوة. أي كتلة تُقيَّم بالتقييم الثلاثي: الفحص السريري، التصوير، والخزعة.",
    lookfor=[
        ("History – breast lump", ["Duration, how noticed", "Change in size / with menstrual cycle", "Pain",
                                   "Nipple changes or discharge", "Skin changes", "Axillary lump",
                                   "Risk factors: age, family history (BRCA), early menarche / late menopause",
                                   "Nulliparity / late first pregnancy, no breastfeeding", "HRT / OCP, previous breast disease or chest radiotherapy",
                                   "Red flags: weight loss, bone pain, breathlessness"]),
        ("History – nipple discharge", ["Unilateral or bilateral", "Single or multiple ducts", "Spontaneous or expressed",
                                        "Colour: bloody, serous, green, milky", "Associated lump", "Drugs (antipsychotics, metoclopramide), pregnancy"]),
        ("Inspection (4 positions)", ["Size &amp; symmetry", "Visible lump / contour change", "Skin: peau d’orange, erythema, ulceration",
                                      "Skin tethering / dimpling", "Nipple: retraction, inversion, deviation",
                                      "Nipple: eczema (Paget’s), discharge", "Scars", "Axilla &amp; supraclavicular fossa"]),
        ("Palpation", ["All 4 quadrants + axillary tail", "Behind the nipple-areola", "Any lump: described as a lump",
                       "Fixity to skin / pectoralis major", "Expression of discharge (by the patient)",
                       "Axillary nodes – 5 groups", "Supraclavicular &amp; cervical nodes"]),
    ],
    procedures=[
        ("A. History of a breast lump / nipple discharge", [
            ("open", "Introduce yourself, confirm identity, explain; private setting; open question."),
            (None, "<b>Lump</b>: when and how noticed, size change, relation to periods, pain, skin or nipple change, axillary lump."),
            (None, "<b>Nipple discharge</b>: side, single / multiple ducts, colour (blood → papilloma / carcinoma; "
                   "green → duct ectasia; milky → galactorrhoea), spontaneous?"),
            (None, "<b>Risk factors</b>: age, family history (breast / ovarian cancer, BRCA), menarche / menopause, parity, age at first "
                   "pregnancy, breastfeeding, HRT / OCP, previous biopsies, chest radiotherapy, alcohol, obesity."),
            (None, "<b>Metastatic symptoms</b>: bone pain, breathlessness, jaundice, headache, weight loss."),
            ("close", "<b>ICE</b>, summary and the need for <b>triple assessment</b>."),
        ]),
        ("B. Breast examination", [
            wiper("from the waist up <b>only when ready to examine</b> (drape otherwise)", "sitting on the edge of the bed; <b>female chaperone</b> present"),
            (None, "<b>Inspect</b> in 4 positions: (1) arms by the sides, (2) <b>hands pressed on the hips</b> (contracts pectoralis), "
                   "(3) <b>arms raised above the head</b>, (4) leaning forward (if large breasts)."),
            (None, "Look at: symmetry, contour, skin (peau d’orange, dimpling, erythema, ulcer), nipples (retraction, Paget’s, "
                   "discharge), scars, axillae."),
            (None, "Lie the patient at <b>45°</b> with the hand behind the head on the side being examined."),
            (None, "<b>Start with the normal breast.</b> Use the <b>flat pads of the middle three fingers</b>, small circular "
                   "movements at three pressures; cover all 4 quadrants and the <b>axillary tail</b> systematically "
                   "(clock-face or vertical strip method)."),
            (None, "Palpate <b>behind the nipple-areola</b>; ask the patient to express any discharge herself."),
            (None, "Describe any lump (site by clock face &amp; distance from nipple, size, shape, consistency, mobility, "
                   "fixity to skin and to <b>pectoralis major</b> – hands on hips)."),
            (None, "<b>Axillary nodes</b>: support the patient’s arm (her forearm on yours) to relax the muscles; "
                   "use the opposite hand. Feel the <b>apical, anterior (pectoral), posterior (subscapular), medial (central) "
                   "and lateral (humeral)</b> groups."),
            (None, "Examine the <b>supraclavicular and cervical</b> lymph nodes."),
            *closing("examine the other breast and axilla, the abdomen (liver), spine (bony tenderness) and chest.",
                     "<b>triple assessment</b>: clinical examination + imaging (ultrasound &lt; 35–40 y, mammography + US ≥ 40 y) "
                     "+ histology (core-needle biopsy / FNAC). Staging CT / bone scan if malignant.",
                     "fibroadenoma, cyst, fibrocystic change, breast abscess, fat necrosis, carcinoma"),
        ]),
    ],
    figures=[
        ("breast_positions", "Inspection positions – arms by sides, hands pressed on hips, arms raised (patient draped)."),
        ("breast_palpation", "Flat pads of the middle three fingers, small circles, clock-face pattern (diagram)."),
        ("breast_axilla", "Axillary nodes – support the patient’s arm on your forearm, palpate with the other hand."),
    ],
    map=dict(img="breast_quadrant_map", title="Breast quadrants &amp; axillary node groups (diagram)",
             markers=[(1, 25, 38.4), (2, 43.3, 38.4), (3, 25, 58), (4, 43.3, 58), (5, 15, 25), (6, 34.2, 48.2), (7, 38.3, 13.4)],
             rows=[("Upper outer quadrant", "~50% of breast cancers"), ("Upper inner quadrant", "Lump, skin dimpling"),
                   ("Lower outer quadrant", "Lump, scars"), ("Lower inner quadrant", "Lump; inspect under the breast fold"),
                   ("Axillary tail (of Spence)", "Often missed – palpate up into the axilla"),
                   ("Nipple-areola", "Retraction, Paget’s eczema, discharge, retro-areolar lump"),
                   ("Axilla &amp; supraclavicular fossa", "Axillary nodes (5 groups), Virchow’s / supraclavicular node")]),
    tables=[
        dict(title="Triple assessment", head=["Component", "Details"],
             rows=[["Clinical", "History and examination"],
                   ["Imaging", "Ultrasound (&lt; 35–40 years), mammography ± ultrasound (≥ 40 years), MRI in selected cases"],
                   ["Pathology", "Core-needle biopsy (preferred) or FNAC"],
                   ["Scoring", "Each component scored 1 (normal) – 5 (malignant); all concordant before reassurance"]]),
        dict(title="Benign vs malignant breast lump", head=["Feature", "Benign (e.g. fibroadenoma)", "Malignant"],
             rows=[["Age", "Younger (15–35)", "Older (&gt; 40)"], ["Surface / edge", "Smooth, well defined", "Irregular, ill defined"],
                   ["Consistency", "Firm, rubbery", "Hard"], ["Mobility", "Very mobile (‘breast mouse’)", "Fixed / tethered"],
                   ["Skin / nipple", "Normal", "Dimpling, peau d’orange, retraction"], ["Nodes", "None", "Hard, fixed axillary nodes"]]),
        dict(title="Nipple discharge – causes", head=["Type", "Likely cause"],
             rows=[["Bloody, single duct", "Intraduct papilloma, ductal carcinoma (DCIS / invasive)"],
                   ["Green / multicoloured, multiple ducts", "Duct ectasia"], ["Purulent", "Breast abscess / periductal mastitis"],
                   ["Milky, bilateral", "Pregnancy, lactation, prolactinoma, drugs (dopamine antagonists), hypothyroidism"],
                   ["Serous", "Fibrocystic change, early pregnancy, papilloma"]]),
        dict(title="Axillary lymph node groups", head=["Group", "Location / how to feel"],
             rows=[["Anterior (pectoral)", "Behind pectoralis major – fingers on the anterior axillary fold"],
                   ["Posterior (subscapular)", "Inside the posterior axillary fold"], ["Medial (central)", "Against the chest wall, deep in the axilla"],
                   ["Lateral (humeral)", "Along the upper humerus"], ["Apical", "High in the axilla, at its apex"]]),
    ],
    checklist=["Introduces self, consent, female chaperone", "Private, exposes only when needed", "History: lump characteristics",
               "History: nipple discharge characteristics", "History: risk factors and red flags", "Inspects with arms by sides",
               "Inspects with hands on hips", "Inspects with arms raised", "Looks at skin, nipples, scars, axillae",
               "Positions at 45°, hand behind head", "Examines normal side first", "Flat finger pads, systematic, all quadrants",
               "Includes axillary tail and retro-areolar area", "Describes lump and checks fixity to pectoralis",
               "Supports arm; examines 5 axillary groups", "Supraclavicular and cervical nodes", "Thanks, covers, washes hands",
               "Summary, triple assessment"],
    links=[("Breast examination", "breast examination OSCE"), ("Breast lump history", "breast lump history taking OSCE"),
           ("Axillary lymph node examination", "axillary lymph node examination")],
),
# =====================================================================================
dict(
    id="dfoot", num=8, title="Diabetic Foot",
    subtitle="Examination of the diabetic foot · wound dressing",
    ar="القدم السكرية تُفحص بثلاثة محاور: الجلد والتشوّهات (النظر)، الدورة الدموية (النبض وزمن عودة الامتلاء الشعري)، والأعصاب "
       "(خيط المونوفيلامنت 10 غرام والشوكة الرنانة 128 هرتز). القرحة تُصنَّف بدرجات Wagner. "
       "الغيار على الجرح يتم بتقنية معقّمة لا تلامسية (ANTT) مع تنظيف من الداخل إلى الخارج.",
    lookfor=[
        ("Inspection – skin", ["Dry, cracked skin, fissures", "Callus over pressure points", "Ulcers – plantar, heel, toe tips",
                                "Signs of infection: redness, swelling, pus, smell", "Gangrene / previous amputations",
                                "Fungal infection between toes", "Nails"]),
        ("Inspection – shape", ["Claw / hammer toes", "Hallux valgus", "Charcot foot (rocker-bottom, warm, swollen)",
                                "Prominent metatarsal heads", "Footwear – fit, wear pattern, foreign bodies"]),
        ("Vascular", ["Temperature", "Capillary refill", "Dorsalis pedis pulse", "Posterior tibial pulse",
                      "ABPI (may be falsely high – calcified) / toe pressures"]),
        ("Neurological", ["10 g monofilament (3–10 sites)", "Vibration – 128 Hz tuning fork on the hallux",
                          "Pin-prick", "Proprioception", "Ankle reflexes"]),
        ("Wound assessment (TIME)", ["Tissue – viable / non-viable", "Infection / inflammation", "Moisture – exudate amount",
                                     "Edge – advancing / undermined", "Size, depth, probe-to-bone"]),
    ],
    procedures=[
        ("A. Examination of the diabetic foot", [
            wiper("both feet and legs to the knees, socks and shoes off", "lying on the couch"),
            (None, "<b>Inspect</b> both feet including <b>soles, heels and between the toes</b>: skin, callus, ulcers, infection, "
                   "gangrene, deformities, nails. <b>Inspect the footwear.</b>"),
            (None, "<b>Vascular</b>: temperature (back of hand), capillary refill, <b>dorsalis pedis</b> and <b>posterior tibial</b> pulses; "
                   "state ABPI / toe pressures."),
            (None, "<b>Monofilament</b>: demonstrate on the sternum / hand first; patient’s eyes closed; apply the 10 g filament "
                   "<b>perpendicular to the skin until it bends</b>, hold ~1–2 s; avoid callus. Test the plantar hallux and "
                   "1st, 3rd and 5th metatarsal heads (± more sites). Ask “yes” when felt."),
            (None, "<b>Vibration</b>: strike the 128 Hz tuning fork, place it on the sternum first, then on the bony prominence of "
                   "the distal phalanx of the big toe; if absent move proximally (MTP, medial malleolus, tibial tuberosity)."),
            (None, "<b>Pin-prick</b>, <b>proprioception</b> (big toe up / down) and <b>ankle reflexes</b>."),
            (None, "If an ulcer is present: describe it (site, size, depth, edge, floor, discharge, surrounding skin), "
                   "<b>probe to bone</b> (osteomyelitis), and grade it (<b>Wagner</b>)."),
            (None, "<b>Gait</b> if appropriate."),
            *closing("examine the full peripheral vascular and neurological systems, and check blood glucose and urine.",
                     "capillary glucose, HbA1c, FBC, CRP / ESR, U&amp;E; wound swab / deep tissue culture; foot X-ray "
                     "(osteomyelitis, gas, Charcot), MRI; arterial duplex / angiography.",
                     "neuropathic, ischaemic or neuro-ischaemic diabetic foot ± infection / osteomyelitis"),
        ]),
        ("B. Wound dressing (aseptic non-touch technique)", [
            ("open", "Check the notes / dressing plan; <b>wash hands</b>, introduce yourself, confirm identity, explain, consent, "
                     "offer analgesia, ensure privacy."),
            (None, "Clean the trolley (top shelf sterile field, bottom shelf equipment): dressing pack, sterile gloves, "
                   "normal saline, chosen dressing, tape / bandage, clinical waste bag."),
            (None, "Position the patient comfortably and expose the wound; protect the bed."),
            (None, "Hand hygiene, apron, <b>non-sterile gloves</b>: remove the old dressing, look at it (amount and type of exudate), "
                   "discard it with the gloves; hand hygiene."),
            (None, "Open the dressing pack touching only the corners; arrange the sterile field; pour saline; put on <b>sterile gloves</b>."),
            (None, "<b>Assess the wound</b>: size, bed (granulation, slough, necrosis), exudate, edges, surrounding skin, odour, "
                   "signs of infection – take a swab if infected."),
            (None, "<b>Clean</b> with saline-soaked gauze from <b>clean to dirty</b> (centre outwards), one swab per stroke; "
                   "dry the surrounding skin."),
            (None, "Apply the appropriate <b>dressing</b> (e.g. non-adherent primary dressing ± absorbent secondary), "
                   "secure with tape / bandage (not too tight on an ischaemic foot); arrange <b>off-loading</b>."),
            ("close", "Dispose of waste and sharps, remove gloves, wash hands, make the patient comfortable, "
                      "<b>document</b> wound findings and the date of the next dressing."),
        ]),
    ],
    figures=[
        ("df_monofilament", "10 g monofilament – perpendicular to the skin until it bends, 1–2 s, patient’s eyes closed."),
        ("df_tuning_fork", "128 Hz tuning fork on the bony prominence of the big-toe distal phalanx."),
        ("df_cleaning", "Wound cleaning with saline gauze, from the centre outwards, sterile gloves."),
        ("df_dressing", "Apply the dressing and secure it – not too tight; arrange off-loading."),
    ],
    map=dict(img="df_sole_map", title="Sole of the foot – pressure points &amp; monofilament sites",
             markers=[(1, 68.9, 7.6), (2, 71, 27.3), (3, 47.4, 25.8), (4, 25.8, 28.8), (5, 24.7, 57.6), (6, 47.4, 87.9), (7, 47.4, 4.5)],
             rows=[("Plantar hallux", "Monofilament site; ulcer, callus"), ("1st metatarsal head", "Monofilament site; commonest neuropathic ulcer"),
                   ("3rd metatarsal head", "Monofilament site; callus"), ("5th metatarsal head", "Monofilament site; ulcer"),
                   ("Lateral border / midfoot", "Charcot deformity, pressure from shoes"), ("Heel", "Pressure ulcer (bed-bound), fissures"),
                   ("Between the toes &amp; toe tips", "Fungal infection, ischaemic ulcers, gangrene")]),
    tables=[
        dict(title="Wagner classification of diabetic foot ulcers", head=["Grade", "Description"],
             rows=[["0", "No open lesion; intact skin – deformity / callus (‘at-risk foot’)"],
                   ["1", "Superficial ulcer (skin and subcutaneous tissue)"],
                   ["2", "Deep ulcer to tendon, capsule or bone – no abscess or osteomyelitis"],
                   ["3", "Deep ulcer with abscess, osteomyelitis or joint sepsis"],
                   ["4", "Localised gangrene (toes, forefoot or heel)"],
                   ["5", "Gangrene of the whole foot"]]),
        dict(title="Neuropathic vs ischaemic diabetic foot", head=["", "Neuropathic", "Ischaemic"],
             rows=[["Temperature", "Warm", "Cold"], ["Pulses", "Bounding / present", "Weak / absent"],
                   ["Skin", "Dry, callus", "Thin, shiny, hairless"], ["Ulcer site", "Plantar pressure points", "Toe tips, heel, foot margins"],
                   ["Pain", "Painless", "Painful (may be masked by neuropathy)"], ["Sensation", "Reduced (stocking distribution)", "Usually preserved"],
                   ["Deformity", "Claw toes, Charcot foot", "—"]]),
        dict(title="Wound dressing – choosing the dressing", head=["Wound bed", "Aim", "Example dressing"],
             rows=[["Clean granulating, low exudate", "Protect, keep moist", "Non-adherent contact layer, foam"],
                   ["Heavy exudate", "Absorb", "Alginate, foam, hydrofibre"], ["Slough", "Debride", "Hydrogel, sharp debridement"],
                   ["Infected", "Reduce bio-burden", "Antimicrobial (silver / iodine) + systemic antibiotics"],
                   ["Dry necrosis on ischaemic foot", "Keep dry until revascularised", "Dry dressing"]]),
    ],
    checklist=["Introduces self, consent, exposes both feet", "Inspects soles, heels and between toes", "Inspects footwear",
               "Identifies deformities / callus / ulcers", "Temperature and capillary refill", "Dorsalis pedis and posterior tibial pulses",
               "Mentions ABPI / toe pressures", "Demonstrates monofilament first; eyes closed", "Monofilament correctly at correct sites",
               "128 Hz tuning fork on hallux", "Pin-prick, proprioception, ankle reflexes", "Grades ulcer (Wagner)",
               "Dressing: hand hygiene, trolley, equipment", "Removes old dressing with clean gloves, inspects it",
               "Sterile field, sterile gloves", "Cleans clean → dirty with saline", "Applies and secures dressing appropriately",
               "Disposes waste, documents", "Summary and plan"],
    links=[("Diabetic foot examination", "diabetic foot examination OSCE monofilament"),
           ("Wound dressing (aseptic technique)", "aseptic non touch technique wound dressing OSCE")],
),
# =====================================================================================
dict(
    id="skills", num=9, title="Surgical Skills",
    subtitle="Sterile gloving · surgical knot tying · suturing technique · suture material identification from the packet",
    ar="مهارات جراحية أساسية: لبس القفاز المعقّم دون لمس سطحه الخارجي باليد العارية، ربط العقدة المربّعة (أو عقدة الجرّاح) بالأداة، "
       "الخياطة المتقطعة البسيطة بإبرة تدخل الجلد بزاوية 90° وتتبع انحناءها، وقراءة عبوة الخيط الجراحي: النوع، القياس، الطول، وشكل الإبرة.",
    lookfor=[
        ("Sterile gloving – key rules", ["Check size, packet integrity, expiry", "Open on a clean dry surface",
                                         "Bare hand touches only the inside (folded cuff)", "Gloved hand touches only the outside",
                                         "Thumb of gloved hand kept away from skin", "Hands above the waist, in sight",
                                         "If contaminated – change gloves"]),
        ("Knot tying", ["Square (reef) knot – throws in opposite directions", "Surgeon’s knot – double first throw",
                        "Lay each throw flat – hands cross", "Approximate, don’t strangle", "At least 3 throws (more for monofilament)",
                        "Knot placed to one side of the wound", "Tails 3–5 mm (skin)"]),
        ("Suturing", ["Needle holder grip (thumb &amp; ring finger)", "Load needle 2/3 back from tip, at 90°",
                      "Toothed forceps to handle the edge", "Enter at 90°, follow the curve (pronate the wrist)",
                      "Equal bites: 3–5 mm from edge", "Spacing 5–10 mm", "Slight eversion of edges", "Sharps disposed immediately"]),
        ("Suture packet – read", ["Material / brand", "Absorbable or not", "Size (USP e.g. 3-0, and metric)", "Length (cm)",
                                  "Needle shape (circle fraction)", "Needle point (cutting / reverse cutting / round-bodied)",
                                  "Needle length (mm)", "Expiry date, LOT, sterilisation"]),
    ],
    procedures=[
        ("A. Sterile gloving – open technique", [
            ("open", "Remove jewellery, perform <b>hand hygiene</b> (surgical scrub if in theatre) and dry hands completely."),
            (None, "Check the glove <b>size, packet integrity and expiry</b>. Peel the outer packet and drop / place the inner wrapper on a clean, dry surface."),
            (None, "Open the inner wrapper touching only the <b>outer corners</b>; the cuffs face you, palms up."),
            (None, "With the non-dominant hand, pick up the dominant glove by the <b>folded cuff edge</b> (inside surface only)."),
            (None, "Slide the dominant hand in and pull the glove on, leaving the cuff folded."),
            (None, "Slide the <b>gloved fingers under the cuff</b> of the second glove (outside surface), keeping the gloved thumb "
                   "abducted away; lift it and insert the non-dominant hand."),
            (None, "Unfold that cuff over the wrist by sliding the gloved fingers under the fold; then do the same for the first glove."),
            (None, "Adjust the fingers; keep hands <b>above the waist and in front</b> of you; touch only sterile items."),
            ("close", "Removal: glove-to-glove (pinch the outside of the first), skin-to-skin (fingers inside the second), "
                      "dispose in clinical waste, hand hygiene."),
        ]),
        ("B. Instrument tie – square / surgeon’s knot", [
            ("open", "Pass the suture through the tissue; pull through leaving a <b>short tail</b> (~2–3 cm)."),
            (None, "Hold the needle holder in the dominant hand, parallel to the wound and between the two ends; long end in the other hand."),
            (None, "<b>First throw</b>: wrap the long end around the needle holder <b>twice</b> (surgeon’s knot) or once (square knot)."),
            (None, "Grasp the <b>short end</b> with the tip of the needle holder and pull the ends in <b>opposite directions</b> "
                   "(hands cross the wound) so the throw lies flat; approximate the edges only."),
            (None, "<b>Second throw</b>: wrap the long end once in the <b>opposite direction</b>, grasp the short end, pull flat in the "
                   "opposite direction to the first → square."),
            (None, "<b>Third throw</b> as the first (single) for security; more for monofilament."),
            ("close", "Pull the knot to one side of the wound; cut the tails (~3–5 mm for skin)."),
        ]),
        ("C. Simple interrupted suture", [
            ("open", "Consent, hand hygiene, sterile gloves, clean the wound, <b>local anaesthetic</b> (lidocaine 1%: max 3 mg/kg plain, "
                     "7 mg/kg with adrenaline), sterile drape."),
            (None, "Grip the needle holder with the <b>thumb and ring finger</b> in the rings, index finger along the shaft."),
            (None, "Load the needle at the tip of the jaws, <b>perpendicular</b>, about <b>2/3 of the way back</b> from the point."),
            (None, "Evert the wound edge gently with <b>toothed forceps</b> (held like a pen)."),
            (None, "Enter the skin at <b>90°</b>, 3–5 mm from the edge; <b>pronate the wrist</b> to follow the curve of the needle."),
            (None, "Exit on the opposite side at the <b>same depth and distance</b> from the edge; regrasp the needle with forceps / holder, "
                   "never with fingers."),
            (None, "Tie with an <b>instrument tie</b>; the edges should be slightly everted, not blanched."),
            (None, "Place further sutures <b>5–10 mm apart</b>; for long wounds, start in the middle and bisect."),
            ("close", "Cut tails, <b>sharps straight into the sharps bin</b>, clean and dress the wound, give suture removal advice "
                      "(face 3–5 d, scalp 7–10 d, trunk 10 d, limbs 10–14 d, palms / soles / over joints 14 d), document."),
        ]),
        ("D. Identifying a suture from its packet", [
            ("open", "Read the <b>name / material</b> and whether it is <b>absorbable</b>."),
            (None, "Read the <b>size</b>: USP (e.g. 3-0 — more zeros = thinner) and metric gauge."),
            (None, "Read the <b>length</b> of the thread (e.g. 75 cm) and its colour (dyed violet / undyed / blue)."),
            (None, "Read the <b>needle symbol</b>: curvature (e.g. 3/8 circle), <b>point type</b> (▲ cutting, ▼ reverse cutting, "
                   "● round-bodied / taper) and needle length (mm)."),
            ("close", "Check <b>expiry date</b>, LOT, sterility and packet integrity – then state a suitable use."),
        ]),
    ],
    figures=[
        ("sk_glove1", "Gloving 1 – bare hand picks up the first glove by the folded cuff (inside surface only)."),
        ("sk_glove2", "Gloving 2 – gloved fingers slide under the cuff of the second glove; gloved thumb kept away."),
        ("sk_knot1", "Instrument tie – wrap the long end around the needle holder (twice for a surgeon’s knot)."),
        ("sk_knot2", "Instrument tie – grasp the short end and pull the ends in opposite directions, throw lying flat."),
        ("sk_needle_load", "Needle loaded at the tip of the jaws, 2/3 back from the point, perpendicular."),
        ("sk_suture", "Enter the skin at 90°, 3–5 mm from the edge; evert the edge with toothed forceps."),
    ],
    map=dict(img="sk_packet_map", title="Suture packet – where to read what (generic packet)",
             markers=[(1, 22.5, 12.9), (2, 44.4, 13.4), (3, 79.4, 12.9), (4, 18.75, 42.9), (5, 50, 51.8), (6, 78.75, 53.6), (7, 68.75, 75.7), (8, 83.75, 86)],
             rows=[("Product name / material", "e.g. polyglactin 910, polypropylene, silk"), ("Size", "USP 3-0 (metric 2) – more zeros = finer"),
                   ("Length", "e.g. 75 cm; colour (violet / undyed / blue)"), ("Needle drawing (actual size)", "Curvature: 1/2, 3/8 circle, straight"),
                   ("Point symbol", "▲ cutting · ▼ reverse cutting · ● round-bodied"), ("Needle length", "e.g. 26 mm"),
                   ("Absorbable / non-absorbable", "Stated on the packet; absorbable ≠ ‘dissolvable in days’"),
                   ("LOT / expiry / sterilisation", "Check before opening; ‘do not resterilise’")]),
    tables=[
        dict(title="Common suture materials", head=["Suture", "Absorbable?", "Structure", "Strength / absorption", "Typical uses"],
             rows=[["Polyglactin 910 (Vicryl)", "Yes, synthetic", "Braided", "~50% strength at 3 wk; absorbed 56–70 d",
                    "Subcutaneous tissue, ligatures, bowel, muscle"],
                   ["Polyglactin rapid (Vicryl Rapide)", "Yes", "Braided", "~50% at 5 d; absorbed ~42 d", "Skin of face / mucosa, perineum"],
                   ["Poliglecaprone 25 (Monocryl)", "Yes", "Monofilament", "~20–30% at 2 wk; absorbed 90–120 d", "Subcuticular skin closure"],
                   ["Polydioxanone (PDS)", "Yes", "Monofilament", "Long strength (~6 wk); absorbed ~180–210 d", "Abdominal wall (mass) closure, tendons"],
                   ["Catgut (plain / chromic)", "Yes, natural", "Twisted", "Plain 7–10 d, chromic ~3 wk", "Ligatures, mucosa (where still used)"],
                   ["Silk", "No*, natural", "Braided", "Loses strength slowly", "Securing drains, ligatures"],
                   ["Polypropylene (Prolene)", "No, synthetic", "Monofilament", "Permanent", "Vascular anastomosis, hernia mesh, skin"],
                   ["Nylon (Ethilon)", "No, synthetic", "Monofilament", "Permanent (slow loss)", "Skin closure"],
                   ["Stainless steel wire", "No", "Mono / multi", "Permanent", "Sternal closure"]],
             note="* silk is classified as non-absorbable although it slowly degrades. Exact values vary by manufacturer – check the packet insert."),
        dict(title="Needle types", head=["Needle", "Cross-section", "Use"],
             rows=[["Cutting", "Triangle, cutting edge on the inner (concave) curve", "Skin"],
                   ["Reverse cutting", "Triangle, cutting edge on the outer (convex) curve – less cut-out", "Skin, tough tissue, tendon"],
                   ["Round-bodied (taper)", "Round, pushes tissue apart", "Bowel, vessels, fascia, soft tissue"],
                   ["Taper-cut", "Cutting tip + round body", "Tough fibrous tissue, calcified vessels"],
                   ["Blunt", "Round, blunt tip", "Liver, friable tissue, reduces needlestick risk"]]),
        dict(title="Choosing a size", head=["Site", "Typical size"],
             rows=[["Face", "5-0 / 6-0 non-absorbable"], ["Scalp", "3-0 / 4-0"], ["Trunk &amp; limbs", "3-0 / 4-0"],
                   ["Hands", "4-0 / 5-0"], ["Abdominal wall (fascia)", "1 or 0 loop (PDS / nylon)"], ["Vascular", "5-0 to 8-0 polypropylene"]]),
    ],
    checklist=["Hand hygiene, removes jewellery", "Checks glove size, packet and expiry", "Opens wrapper touching only corners",
               "First glove handled by inside of cuff only", "Second glove handled by outside only, thumb away",
               "Unfolds cuffs without contamination", "Hands kept above waist", "Instrument tie: correct first throw (double)",
               "Throws laid flat, opposite directions (square)", "At least 3 throws, knot to one side, tails cut correctly",
               "Needle-holder grip correct", "Needle loaded 2/3 back, perpendicular", "Toothed forceps used gently",
               "Enters at 90°, follows curve, symmetrical bites", "Correct spacing and eversion", "Sharps disposed safely",
               "Identifies suture material, absorbable or not", "Identifies size, length, needle type", "Checks expiry / sterility",
               "States appropriate use"],
    links=[("Sterile gloving", "sterile gloving open technique OSCE"), ("Instrument tie", "instrument tie surgical knot tutorial"),
           ("Simple interrupted suture", "simple interrupted suture technique OSCE"),
           ("Suture materials", "suture materials and needles explained packet")],
),
]
