"""Topic 6 (lump on the forearm) and topic 8 (diabetic foot)."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from art import *
from draw_pvd import RFOOT, RFOOT_SHADE, RFOOT_LIGHT, RFOOT_LINES, RFOOT_FAINT, RFOOT_WEIGHT
OUT = os.path.join(os.path.dirname(__file__), "svg")
LX, LY, LR = 470, 300, 46          # lump centre / radius on the forearm


def table_bg(w=900, h=600):
    return blob(f"M -50 -50 L {w + 50} -50 L {w + 50} {h + 50} L -50 {h + 50} Z", COUCH)


def lump(glow=False):
    pts = [(LX + LR * 1.15 * math.cos(a) * (1 + .05 * math.sin(3 * a)), LY + LR * .9 * math.sin(a)) for a in [i * math.pi / 6 for i in range(12)]]
    d = smooth(pts, t=.5)
    out = part(d, SKIN, [smooth([(LX + 40, LY - 10), (LX + 52, LY + 14), (LX + 30, LY + 38), (LX - 10, LY + 42), (LX + 20, LY + 22), (LX + 36, LY + 6)], t=.4)],
               [smooth([(LX - 30, LY - 22), (LX - 4, LY - 32), (LX + 10, LY - 24), (LX - 14, LY - 14)], t=.4)], [], [], [], sw=2.2)
    if glow:
        out += f'<path d="{d}" fill="url(#glow)"/>'
    return out


def patient_arm():
    # forearm + flat hand of the patient (dorsal surface up), lying across the table
    return hand_svg("flat", 640, 300, 0, 1.25, glove=False, arm="skin", arm_len=420)


GLOW = ('<defs><radialGradient id="glow" cx="50%" cy="50%" r="55%"><stop offset="0" stop-color="#fff6c2" stop-opacity=".95"/>'
        '<stop offset=".7" stop-color="#ffe27a" stop-opacity=".6"/><stop offset="1" stop-color="#ffe27a" stop-opacity="0"/></radialGradient></defs>')


def fluctuation():
    b = [table_bg(), patient_arm(), lump()]
    b.append(hand_at("vee", (LX, LY + 4), -90, 1.0, what="mid2", left=False, arm_len=280).replace("", ""))
    b.append(hand_at("point", (LX + 2, LY - 4), 120, .95, what="index", arm_len=280))
    return svg(760, 560, "\n".join(b), x0=170, y0=20)


def fixity():
    b = [table_bg(), patient_arm(), lump()]
    body, thumb, sl = pen_hand(LX - 150, LY - 120, 38, 1.05, arm_len=280)
    b += [body, thumb, sl]
    return svg(760, 560, "\n".join(b), x0=170, y0=20)


def transillum():
    b = [GLOW, table_bg(), patient_arm(), lump(glow=True)]
    torch = f"M {LX - 34} {LY - 40} L {LX - 194} {LY - 160} L {LX - 174} {LY - 184} L {LX - 16} {LY - 64} Z"
    b.append(part(torch, "#5d6773", [], [f"M {LX - 44} {LY - 56} L {LX - 174} {LY - 156} L {LX - 170} {LY - 162} L {LX - 40} {LY - 62} Z"], [], [], [],
                  light_fill="#9aa4ae"))
    b.append(part(f"M {LX - 36} {LY - 36} L {LX - 14} {LY - 66} L {LX - 4} {LY - 58} L {LX - 26} {LY - 28} Z", "#b9c2cb", [], [], [], [], []))
    body, thumb, sl = pen_hand(LX - 264, LY - 160, 38, 1.0, arm_len=260)
    b += [body, thumb, sl]
    return svg(760, 560, "\n".join(b), x0=170, y0=20)


def measure():
    b = [table_bg(), patient_arm(), lump()]
    ruler = f"M {LX - 110} {LY - 6} L {LX + 130} {LY - 18} L {LX + 132} {LY + 14} L {LX - 108} {LY + 26} Z"
    ticks = [f"M {LX - 100 + i * 12} {LY - 6 - i * .6:.1f} L {LX - 100 + i * 12} {LY + (2 if i % 5 else 8) - i * .6:.1f}" for i in range(20)]
    b.append(part(ruler, "#f3d34a", [], [], ticks, [], [], sw=2.2))
    b.append(arrow(f"M {LX} {LY - 50} L {LX} {LY - 90}", w=3) + arrow(f"M {LX} {LY + 60} L {LX} {LY + 100}", w=3))
    body, thumb, sl = pen_hand(LX - 260, LY - 60, 14, 1.0, arm_len=260)
    b += [body, thumb, sl]
    return svg(760, 560, "\n".join(b), x0=170, y0=20)


# ------------------------------------------------------------------ diabetic foot: plantar view of the right foot
SOLE = [(370, 800), (388, 700), (386, 600), (398, 500), (416, 420), (420, 350), (418, 290), (406, 246), (380, 228), (354, 238), (344, 270), (340, 300, 'c'),
        (334, 260), (320, 240), (300, 240), (290, 262), (290, 306, 'c'), (280, 272), (266, 260), (250, 266), (244, 290), (246, 318, 'c'),
        (238, 296), (226, 290), (212, 298), (210, 322), (212, 340, 'c'), (202, 330), (190, 334), (184, 352), (190, 376), (196, 420),
        (204, 520), (214, 640), (226, 760), (250, 836), (300, 862), (344, 846)]


def sole(ulcer=False):
    d = smooth(SOLE, t=.5)
    shade = [smooth([(386, 600), (388, 700), (370, 640), (340, 560), (348, 470), (396, 500)], t=.5),
             smooth([(198, 380), (198, 420), (204, 520), (214, 640), (226, 760), (250, 836), (262, 800), (240, 700), (230, 560), (220, 420)], t=.4)]
    light = [smooth([(270, 700), (330, 690), (350, 760), (320, 830), (270, 820), (250, 760)], t=.5),
             smooth([(230, 400), (300, 360), (400, 400), (380, 440), (300, 420), (240, 440)], t=.5),
             smooth([(362, 268), (390, 268), (402, 300), (380, 320), (360, 300)], t=.5)]
    ln = ["M 350 330 C 370 340 392 340 406 330", "M 210 372 C 260 352 330 350 404 362"]
    faint = ["M 306 316 C 296 326 278 330 266 324", "M 230 346 C 236 354 246 356 258 350",
             "M 220 470 C 260 456 330 452 392 466", "M 250 680 C 290 670 330 670 360 680"]
    out = part(d, SKIN, shade, light, ln, faint, [smooth(SOLE[25:33], closed=False)])
    if ulcer:
        out += part("M 362 392 C 376 380 398 386 400 404 C 400 420 384 428 368 422 C 356 416 354 402 362 392 Z", "#d9534f",
                    [], ["M 368 398 C 376 392 386 394 390 400 C 382 400 374 402 368 406 Z"], [], ["M 352 388 C 360 372 396 374 408 392 C 414 414 404 432 380 436"], [],
                    sw=2.2, light_fill="#f08a80")
    return out


def sole_map():
    return svg(600, 900, blob("M 0 0 L 600 0 L 600 900 L 0 900 Z", "#ffffff") + sole(), y0=220, x0=40).replace('viewBox="40 220 600 900"', 'viewBox="120 220 380 660"')


def monofilament():
    b = [sole()]
    # monofilament: handle + nylon filament buckled against the 1st metatarsal head
    b.append(part("M 520 330 L 640 210 L 654 224 L 534 344 Z", "#e9eef3", [], [], [], [], [], sw=2.2))
    b.append(f'<path d="M 527 337 C 470 350 420 380 388 418" fill="none" stroke="#2f6fb0" stroke-width="3.5" stroke-linecap="round"/>')
    body, thumb, sl = pen_at((596, 260), 135, 1.0, left=True, arm_len=260)
    b += [body, thumb, sl]
    return svg(600, 760, "\n".join(b), x0=120, y0=120)


def tuning_fork(x, y, ang=0, sc=1.0):
    fn = affine(x, y, sc, ang)
    T = lambda d: tpath(d, fn)
    fork = smooth([(0, -8, 'c'), (90, -8), (100, -26), (110, -30), (230, -30), (230, -20, 'c'), (116, -20), (110, -14), (110, 14), (116, 20),
                   (230, 20, 'c'), (230, 30, 'c'), (110, 30), (100, 26), (90, 8), (0, 8, 'c')], t=.3)
    foot = smooth([(-14, -14, 'c'), (0, -14), (0, 14), (-14, 14, 'c')], t=.2)
    return (part(T(fork), "#c9d1d9", [T("M 0 2 L 90 2 L 100 20 L 230 22 L 230 30 L 110 30 L 100 26 L 90 8 L 0 8 Z")],
                 [T("M 10 -5 L 86 -5 L 86 -2 L 10 -2 Z"), T("M 120 -27 L 224 -27 L 224 -24 L 120 -24 Z")], [], [], [], sw=2.2,
                 shade_fill="#9aa5b1", light_fill="#ffffff") +
            part(T(foot), "#9aa5b1", [], [], [], [], [], sw=2.2))


def df_tuning():
    b = [blob("M 0 100 L 800 100 L 800 600 L 0 600 Z", COUCH),
         part(RFOOT, SKIN, RFOOT_SHADE, RFOOT_LIGHT, RFOOT_LINES, RFOOT_FAINT, RFOOT_WEIGHT)]
    b.append(tuning_fork(322, 214, -60, 1.0))
    body, thumb, sl = pen_hand(420, -20, 100, 1.0, arm_len=220)
    b += [body, thumb, sl]
    b.append(lines(["M 470 0 q 8 6 0 12 q -8 6 0 12", "M 500 30 q 8 6 0 12 q -8 6 0 12"], 2.4, "#167a8b"))
    return svg(700, 560, "\n".join(b), x0=50, y0=-40)


def forceps_gauze(x, y, ang, sc=1.0):
    fn = affine(x, y, sc, ang)
    T = lambda d: tpath(d, fn)
    arm1 = "M 0 -3 L 200 -10 L 204 -4 L 0 3 Z"
    arm2 = "M 0 3 L 200 10 L 204 4 L 0 -3 Z"
    gauze = smooth([(-26, -14), (-10, -26), (8, -18), (14, 0), (6, 18), (-14, 24), (-30, 10)], t=.6)
    return (part(T(arm1), "#c9d1d9", [], [], [], [], [], sw=2) + part(T(arm2), "#b5bec8", [], [], [], [], [], sw=2) +
            part(T(gauze), "#ffffff", [T(smooth([(-30, 10), (-14, 24), (6, 18), (-10, 12)], t=.4))], [], [], [T("M -20 -10 C -10 -4 0 0 6 10"), T("M -24 4 C -14 6 -6 12 -2 20")], [],
                 sw=2.2, shade_fill="#dfe8ef"))


def df_cleaning():
    b = [sole(ulcer=True)]
    b.append(f'<path d="M 382 406 C 392 400 396 410 388 414 C 374 420 368 400 382 392 C 402 382 414 410 396 422 C 370 438 350 400 372 382" fill="none" stroke="#167a8b" stroke-width="3" stroke-dasharray="6 5"/>')
    b.append(forceps_gauze(410, 404, -40, 1.0))
    body, thumb, sl = pen_at((560, 270), 140, 1.0, left=True, arm_len=260)
    b += [body, thumb, sl]
    return svg(600, 760, "\n".join(b), x0=120, y0=120)


def df_dressing():
    b = [blob("M 0 100 L 800 100 L 800 600 L 0 600 Z", COUCH),
         part(RFOOT, SKIN, RFOOT_SHADE, RFOOT_LIGHT, RFOOT_LINES, RFOOT_FAINT, RFOOT_WEIGHT)]
    # crepe bandage turns around the forefoot (figure-of-eight)
    for y0 in (300, 336, 372):
        b.append(part(f"M 292 {y0} C 340 {y0 - 10} 410 {y0 - 14} 462 {y0 - 6} L 462 {y0 + 30} C 410 {y0 + 22} 340 {y0 + 26} 292 {y0 + 36} Z", "#f7f3ea",
                      [f"M 292 {y0 + 26} C 340 {y0 + 16} 410 {y0 + 12} 462 {y0 + 20} L 462 {y0 + 30} C 410 {y0 + 22} 340 {y0 + 26} 292 {y0 + 36} Z"], [],
                      [], [f"M 300 {y0 + 12} C 350 {y0 + 4} 410 {y0} 456 {y0 + 8}"], [], sw=2.2, shade_fill="#ddd6c6"))
    b.append(part("M 300 410 C 350 380 420 420 462 470 L 462 500 C 420 450 350 412 300 440 Z", "#f7f3ea", [], [], [], [], [], sw=2.2))
    # bandage roll in the examiner's hand
    b.append(part("M 470 470 C 520 420 600 400 640 430 L 652 460 C 610 440 540 456 486 500 Z", "#f7f3ea", [], [], [], [], [], sw=2.2))
    b.append(part(smooth([(640, 410), (676, 404), (700, 430), (696, 470), (664, 484), (636, 470), (628, 440)], t=.5), "#f7f3ea",
                  ["M 640 470 C 660 482 686 476 696 460 L 700 470 C 690 488 656 494 636 478 Z"], [], ["M 650 430 C 660 424 676 426 684 436"], [], [], sw=2.4, shade_fill="#ddd6c6"))
    b.append(hand_at("flat", (668, 440), -150, .95, what="mid4", left=True, arm_len=240))
    return svg(760, 520, "\n".join(b), x0=120, y0=100)


ALL = dict(lump_fluctuation=fluctuation, lump_fixity=fixity, lump_transillum=transillum, lump_measure=measure,
           df_sole_map=sole_map, df_monofilament=monofilament, df_tuning_fork=df_tuning, df_cleaning=df_cleaning, df_dressing=df_dressing)
if __name__ == "__main__":
    for k in (sys.argv[1:] or ALL):
        save(k, ALL[k](), OUT)
