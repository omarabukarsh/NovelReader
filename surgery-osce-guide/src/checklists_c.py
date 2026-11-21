# -*- coding: utf-8 -*-
"""Checklist-driven content, topics 7-9."""
from checklists_a import HELP, END

TOPICS_C = [
# =====================================================================================
dict(
    id="breast", num=7, title="Breast &amp; Axillary Lymph Nodes",
    subtitle="History of a breast lump &amp; nipple discharge · breast examination · axillary node examination",
    ar="فحص الثدي بوجود مرافِقة وبعد الموافقة: النظر في أربع وضعيات، ثم الجسّ بباطن الأصابع الثلاثة الوسطى لكل الأرباع والذيل الإبطي "
       "مع البدء بالثدي السليم، ثم العقد الإبطية الخمس وفوق الترقوة. أي كتلة تُقيَّم بالتقييم الثلاثي: الفحص، التصوير، الخزعة.",
    checklists=[
        ("A. History of a breast lump / nipple discharge", [
            ("Introduction", "", [("Hello &amp; consent", "Private setting")]),
            ("The complaint", "", [
                ("Lump", "Duration, size change, relation to periods, pain, skin / nipple change"),
                ("Nipple discharge", "One or both sides, one or many ducts, colour, spontaneous?"),
            ]),
            ("Risk factors", "", [
                ("Ask", "Age, family history (BRCA), early menarche / late menopause, nulliparity, HRT / OCP, previous radiotherapy"),
            ]),
            ("Metastatic symptoms", "", [("Ask", "Bone pain, breathlessness, weight loss")]),
            ("End of station", "", [("ICE, summary, need for triple assessment", "")]),
        ]),
        ("B. Breast &amp; axillary examination", [
            HELP("Waist up — only when ready to examine (drape otherwise)", "Sitting on the edge of the bed",
                 hello="Introduce yourself, explain, consent; <b>female chaperone</b>"),
            ("Inspection", "in 4 positions", [
                ("Positions", "Arms by sides → hands pressed on hips → arms raised → leaning forward", "breast_positions"),
                ("Symmetry &amp; contour", "Visible lump"),
                ("Skin", "Peau d’orange, dimpling / tethering, redness, ulcer"),
                ("Nipples", "Retraction, Paget’s eczema, discharge"),
                ("Scars, axillae, supraclavicular fossae", ""),
            ]),
            ("Palpation", "lying at 45°, hand behind head; <b>normal side first</b>", [
                ("All four quadrants", "Flat pads of the middle three fingers, small circles", "breast_palpation"),
                ("Axillary tail", "Up into the axilla — often missed"),
                ("Behind the nipple", "Ask the patient to express any discharge"),
                ("Any lump", "Describe it; fixity to pectoralis (hands on hips)"),
            ]),
            ("Lymph nodes", "", [
                ("Axillary — 5 groups", "Support the patient’s arm; apical, anterior, posterior, medial, lateral", "breast_axilla"),
                ("Supraclavicular &amp; cervical", ""),
            ]),
            END("Examine the other breast, liver, spine and chest",
                "<b>Triple assessment</b>: clinical + imaging (US &lt; 35–40 y, mammography ≥ 40 y) + core biopsy",
                "Fibroadenoma, cyst, fibrocystic change, abscess, fat necrosis, carcinoma"),
        ]),
    ],
    map=dict(img="breast_quadrant_map", title="Breast quadrants &amp; axillary tail (diagram)",
             markers=[(1, 25, 38.4), (2, 43.3, 38.4), (3, 25, 58), (4, 43.3, 58), (5, 15, 25), (6, 34.2, 48.2), (7, 38.3, 13.4)],
             rows=[("Upper outer quadrant", "~50% of breast cancers"), ("Upper inner quadrant", "Lump, dimpling"),
                   ("Lower outer quadrant", "Lump, scars"), ("Lower inner quadrant", "Lump; look under the breast fold"),
                   ("Axillary tail", "Often missed – palpate up into the axilla"),
                   ("Nipple-areola", "Retraction, Paget’s eczema, discharge"),
                   ("Axilla &amp; supraclavicular fossa", "Axillary nodes, supraclavicular node")]),
    tables=[
        dict(title="Benign vs malignant breast lump", head=["Feature", "Benign (e.g. fibroadenoma)", "Malignant"],
             rows=[["Age", "15–35", "&gt; 40"], ["Edge", "Smooth, well defined", "Irregular"], ["Consistency", "Firm, rubbery", "Hard"],
                   ["Mobility", "Very mobile", "Fixed / tethered"], ["Skin / nipple", "Normal", "Dimpling, peau d’orange, retraction"]]),
        dict(title="Nipple discharge", head=["Type", "Likely cause"],
             rows=[["Bloody, single duct", "Intraduct papilloma, carcinoma"], ["Green, multiple ducts", "Duct ectasia"],
                   ["Purulent", "Abscess / periductal mastitis"], ["Milky, both sides", "Pregnancy, prolactinoma, drugs"]]),
    ],
    links=[("Breast exam", "breast examination OSCE"), ("Breast lump history", "breast lump history taking OSCE")],
),
# =====================================================================================
dict(
    id="dfoot", num=8, title="Diabetic Foot",
    subtitle="Examination of the diabetic foot · wound dressing",
    ar="القدم السكرية تُفحص بثلاثة محاور: الجلد والتشوّهات، الدورة الدموية (النبض وعودة الامتلاء الشعري)، والأعصاب "
       "(المونوفيلامنت والشوكة الرنانة). القرحة تُصنَّف بدرجات <bdi dir='ltr'>Wagner</bdi>، والغيار يتم بتقنية معقّمة مع التنظيف من الداخل للخارج.",
    checklists=[
        ("A. Examination of the diabetic foot", [
            HELP("Both feet and legs to the knees; shoes and socks off", "Lying on the couch"),
            ("Inspection", "both feet — soles, heels, between the toes", [
                ("Skin", "Dry, cracked, callus over pressure points"),
                ("Ulcers &amp; infection", "Redness, swelling, pus, smell"),
                ("Gangrene / amputations", ""),
                ("Deformity", "Claw toes, hallux valgus, Charcot (rocker-bottom) foot"),
                ("Footwear", "Fit, wear pattern, foreign bodies"),
            ]),
            ("Vascular", "", [
                ("Temperature &amp; capillary refill", ""),
                ("Dorsalis pedis &amp; posterior tibial", ""),
                ("ABPI", "State it — may be falsely high (calcified) → toe pressures"),
            ]),
            ("Neurological", "", [
                ("10 g monofilament", "Show on sternum first; eyes closed; press until it bends, 1–2 s", "df_monofilament"),
                ("Vibration", "128 Hz tuning fork on the big-toe distal phalanx", "df_tuning_fork"),
                ("Pin-prick, proprioception, ankle reflexes", ""),
            ]),
            ("Ulcer (if present)", "", [("Describe, probe to bone, Wagner grade", "Probe touches bone = osteomyelitis")]),
            END("Full peripheral vascular &amp; neurological exam; check glucose",
                "Glucose, HbA1c, FBC, CRP; deep tissue culture; foot X-ray / MRI; arterial duplex",
                "Neuropathic, ischaemic or neuro-ischaemic foot ± infection / osteomyelitis"),
        ]),
        ("B. Wound dressing (aseptic non-touch technique)", [
            ("Preparation", "", [
                ("Hello, consent, analgesia", "Check the dressing plan"),
                ("Clean trolley &amp; equipment", "Dressing pack, sterile gloves, saline, dressing, waste bag"),
            ]),
            ("Old dressing", "", [("Remove with clean gloves", "Look at the exudate; discard; hand hygiene")]),
            ("Sterile field", "", [("Open pack by the corners, sterile gloves", "")]),
            ("Wound care", "", [
                ("Assess the wound — TIME", "Tissue, Infection, Moisture, Edge; size, depth"),
                ("Clean", "Saline gauze from <b>clean to dirty</b> (centre outwards)", "df_cleaning"),
                ("Dress &amp; secure", "Right dressing; not too tight; off-loading", "df_dressing"),
            ]),
            ("End of station", "", [("Dispose, wash hands, document", "Date of next dressing")]),
        ]),
    ],
    map=dict(img="df_sole_map", title="Sole of the foot – pressure points &amp; monofilament sites",
             markers=[(1, 68.9, 7.6), (2, 71, 27.3), (3, 47.4, 25.8), (4, 25.8, 28.8), (5, 24.7, 57.6), (6, 47.4, 87.9), (7, 47.4, 4.5)],
             rows=[("Plantar hallux", "Monofilament site; ulcer, callus"), ("1st metatarsal head", "Monofilament site; commonest ulcer"),
                   ("3rd metatarsal head", "Monofilament site"), ("5th metatarsal head", "Monofilament site; ulcer"),
                   ("Lateral border / midfoot", "Charcot deformity"), ("Heel", "Pressure ulcer, fissures"),
                   ("Between &amp; tips of toes", "Fungal infection, ischaemic ulcers")]),
    tables=[
        dict(title="Wagner classification", head=["Grade", "Description"],
             rows=[["0", "Intact skin – deformity / callus (at-risk foot)"], ["1", "Superficial ulcer"],
                   ["2", "Deep ulcer to tendon, capsule or bone"], ["3", "Deep ulcer + abscess / osteomyelitis"],
                   ["4", "Localised gangrene (toes, forefoot)"], ["5", "Gangrene of the whole foot"]]),
        dict(title="Neuropathic vs ischaemic foot", head=["", "Neuropathic", "Ischaemic"],
             rows=[["Temperature", "Warm", "Cold"], ["Pulses", "Present", "Weak / absent"], ["Skin", "Dry, callus", "Thin, shiny, hairless"],
                   ["Ulcer site", "Plantar pressure points", "Toe tips, heel, margins"], ["Pain", "Painless", "Painful"]]),
    ],
    links=[("Diabetic foot exam", "diabetic foot examination OSCE monofilament"), ("Wound dressing", "aseptic non touch technique wound dressing OSCE")],
),
# =====================================================================================
dict(
    id="skills", num=9, title="Surgical Skills",
    subtitle="Sterile gloving · surgical knot tying · suturing technique · suture material identification from the packet",
    ar="مهارات أساسية: لبس القفاز المعقّم دون لمس سطحه الخارجي باليد العارية، ربط العقدة المربّعة بالأداة، الخياطة المتقطعة بإبرة تدخل الجلد بزاوية 90°، "
       "وقراءة عبوة الخيط: النوع، القياس، الطول، وشكل الإبرة.",
    checklists=[
        ("A. Sterile gloving (open technique)", [
            ("Preparation", "", [
                ("Hand hygiene", "Remove jewellery; dry hands completely"),
                ("Check the packet", "Size, integrity, expiry"),
                ("Open the wrapper", "Touch the outer corners only"),
            ]),
            ("First glove", "", [
                ("Pick up by the folded cuff", "Bare hand touches the <b>inside</b> only", "sk_glove1"),
                ("Pull it on", "Leave the cuff folded"),
            ]),
            ("Second glove", "", [
                ("Gloved fingers under the cuff", "Touch the <b>outside</b> only; keep gloved thumb away", "sk_glove2"),
                ("Unfold both cuffs", "Slide gloved fingers under the fold"),
            ]),
            ("Keep sterile", "", [("Hands above waist, in view", "If contaminated – change gloves")]),
        ]),
        ("B. Instrument tie (square / surgeon’s knot)", [
            ("Set-up", "", [("Pass the suture, short tail 2–3 cm", "Needle holder parallel to the wound, between the ends")]),
            ("First throw", "", [
                ("Wrap twice around the needle holder", "Surgeon’s knot (once for a square knot)", "sk_knot1"),
                ("Grasp the short end, pull opposite ways", "Hands cross; throw lies flat; don’t strangle", "sk_knot2"),
            ]),
            ("Second &amp; third throws", "", [
                ("Wrap once in the opposite direction", "Pull flat the other way → square"),
                ("Third throw", "More for monofilament"),
            ]),
            ("Finish", "", [("Knot to one side, cut tails 3–5 mm", "")]),
        ]),
        ("C. Simple interrupted suture", [
            ("Preparation", "", [("Consent, hand hygiene, sterile gloves, clean, local anaesthetic", "Lidocaine 1%: max 3 mg/kg (7 with adrenaline)")]),
            ("Instruments", "", [
                ("Needle-holder grip", "Thumb &amp; ring finger in the rings, index along the shaft"),
                ("Load the needle", "At the jaw tip, 2/3 back from the point, perpendicular", "sk_needle_load"),
                ("Toothed forceps", "Held like a pen, gentle on the edge"),
            ]),
            ("Bite", "", [
                ("Enter at 90°, 3–5 mm from the edge", "Pronate the wrist to follow the curve", "sk_suture"),
                ("Exit symmetrically", "Same depth and distance; regrasp with instrument, not fingers"),
            ]),
            ("Tie &amp; space", "", [("Instrument tie, edges slightly everted", "Sutures 5–10 mm apart")]),
            ("Finish", "", [("Sharps to bin, dress, removal advice, document", "Face 3–5 d, scalp 7–10 d, trunk 10 d, limbs 10–14 d")]),
        ]),
        ("D. Identify a suture from its packet", [
            ("Read the packet", "see the packet map", [
                ("Material &amp; absorbable?", "e.g. polyglactin = absorbable"),
                ("Size", "USP 3-0 — more zeros = finer"),
                ("Length &amp; colour", "e.g. 75 cm, violet"),
                ("Needle symbol", "Curvature (3/8, 1/2), point (▲ cutting, ▼ reverse cutting, ● round), length"),
                ("Expiry, LOT, sterility", "Then state a suitable use"),
            ]),
        ]),
    ],
    map=dict(img="sk_packet_map", title="Suture packet – where to read what (generic packet)",
             markers=[(1, 22.5, 12.9), (2, 44.4, 13.4), (3, 79.4, 12.9), (4, 18.75, 42.9), (5, 50, 51.8), (6, 78.75, 53.6), (7, 68.75, 75.7), (8, 83.75, 86)],
             rows=[("Product name / material", "e.g. polyglactin 910, polypropylene, silk"), ("Size", "USP 3-0 (metric 2)"),
                   ("Length", "e.g. 75 cm; colour"), ("Needle drawing (actual size)", "Curvature: 1/2, 3/8 circle"),
                   ("Point symbol", "▲ cutting · ▼ reverse cutting · ● round-bodied"), ("Needle length", "e.g. 26 mm"),
                   ("Absorbable / non-absorbable", "Stated on the packet"), ("LOT / expiry / sterilisation", "Check before opening")]),
    tables=[
        dict(title="Common suture materials", head=["Suture", "Absorbable?", "Structure", "Typical uses"],
             rows=[["Polyglactin 910 (Vicryl)", "Yes (~60 d)", "Braided", "Subcutaneous tissue, ligatures, bowel"],
                   ["Poliglecaprone (Monocryl)", "Yes (~100 d)", "Monofilament", "Subcuticular skin closure"],
                   ["Polydioxanone (PDS)", "Yes (~6 months)", "Monofilament", "Abdominal wall closure"],
                   ["Catgut", "Yes (natural)", "Twisted", "Ligatures, mucosa"],
                   ["Silk", "No (natural)", "Braided", "Securing drains"],
                   ["Polypropylene (Prolene)", "No", "Monofilament", "Vascular, hernia mesh, skin"],
                   ["Nylon (Ethilon)", "No", "Monofilament", "Skin closure"]]),
        dict(title="Needle types", head=["Needle", "Use"],
             rows=[["Cutting / reverse cutting", "Skin, tough tissue"], ["Round-bodied (taper)", "Bowel, vessels, soft tissue"],
                   ["Blunt", "Liver, friable tissue"]]),
    ],
    links=[("Sterile gloving", "sterile gloving open technique OSCE"), ("Instrument tie", "instrument tie surgical knot tutorial"),
           ("Simple interrupted suture", "simple interrupted suture technique OSCE")],
),
]
