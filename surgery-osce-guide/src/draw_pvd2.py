"""Topic 1 illustrations, part 2 (re-uses the approved geometry of draw_pvd.py)."""
import sys, os, math
sys.path.insert(0, os.path.dirname(__file__))
from art import *
from draw_pvd import (RFOOT, RFOOT_SHADE, RFOOT_LIGHT, RFOOT_LINES, RFOOT_FAINT, RFOOT_WEIGHT, leg_from_above,
                      gown_top, far_leg, LEG_FRONT, LEG_BACK, FOOT_SIDE, OUT)

PALE = "#f7e9df"
A0, KA0 = (740, 455), math.degrees(math.atan2(175, 428))


def chain_from(H, a1, a2, l1=495, l2=462):
    K = add(H, (math.cos(math.radians(a1)), math.sin(math.radians(a1))), l1)
    A = add(K, (math.cos(math.radians(a2)), math.sin(math.radians(a2))), l2)
    return [H, K, A]


def side_leg(ch, pale=False, extra=""):
    """Side (lateral) view of a right leg along chain [hip, knee, ankle] with the approved foot profile."""
    a2 = math.degrees(math.atan2(ch[2][1] - ch[1][1], ch[2][0] - ch[1][0]))
    rot = a2 - KA0
    c, s = math.cos(math.radians(rot)), math.sin(math.radians(rot))
    def F(p):
        x, y = p[0] - A0[0], p[1] - A0[1]
        return (ch[2][0] + x * c - y * s, ch[2][1] + x * s + y * c)
    front = profile(ch, LEG_FRONT, +1)
    back = profile(ch, LEG_BACK, -1)
    foot = [F(p) for p in FOOT_SIDE]
    d = smooth(front + foot + back + [add(ch[0], (-80, 90)), add(ch[0], (-80, -130))], t=.5)
    shade = [
        smooth(profile(ch, [(0, 86), (0.4, 82), (0.8, 66), (0.95, 50), (1.1, 52), (1.3, 74), (1.6, 56), (1.95, 31)], -1)
               + profile(ch, [(1.95, 12), (1.6, 26), (1.3, 40), (1.1, 26), (0.95, 22), (0.8, 30), (0.4, 44), (0, 50)], -1), t=.4),
        smooth([F(p) for p in [(868, 374), (848, 420), (822, 468), (800, 504), (776, 521), (800, 470), (830, 420), (850, 380)]], t=.4),
    ]
    light = [smooth(profile(ch, [(0.2, 72), (0.6, 68), (0.9, 56), (0.98, 60), (1.2, 42), (1.6, 36), (1.9, 30),
                                 (1.9, 22), (1.6, 26), (1.2, 32), (0.98, 48), (0.9, 44), (0.6, 56), (0.2, 60)], +1), t=.4)]
    T = lambda d_: tpath(d_, F)
    lines_ = [T("M 726 462 C 734 450 750 448 758 458 C 762 468 756 478 746 480"),
              T("M 842 352 C 848 344 856 342 862 346 C 866 352 864 360 858 364"),
              T("M 856 338 C 862 332 870 332 874 338"), T("M 866 334 C 870 330 876 331 878 336")]
    faint = [smooth(profile(ch, [(0.92, 50), (0.97, 64), (1.03, 60), (1.06, 46), (1.02, 34), (0.95, 36)], +1)),
             smooth(profile(ch, [(1.15, 40), (1.5, 40), (1.85, 34)], +1), closed=False),
             smooth(profile(ch, [(1.2, -30), (1.4, -40), (1.6, -30)], +1), closed=False),
             T("M 800 386 C 820 400 836 420 846 440"), T("M 790 420 C 800 440 806 470 800 500")]
    if pale:
        extra += f'<path d="{smooth([F(p) for p in FOOT_SIDE] + profile(ch, [(1.97, -30), (1.82, -36), (1.82, 38), (1.97, 35)], +1), t=.4)}" fill="{PALE}" opacity=".9"/>'
    weight = [smooth(back[:9], closed=False)]
    return part(d, SKIN, shade, light, lines_, faint, weight, extra=extra)


def gown_on(ch, hem=0.62):
    a = profile(ch, [(0.0, 92), (0.3, 90), (hem, 85)], +1)
    h = profile(ch, [(hem + .02, 60), (hem + .04, 20), (hem + .03, -20), (hem + .01, -60)], +1)
    b = profile(ch, [(hem, -93), (0.3, -96)], +1)
    d = smooth(a + h + b + [(ch[0][0] + 240, 521), (ch[0][0] - 80, 521), (ch[0][0] - 80, ch[0][1] - 130)], t=.45)
    shade = [smooth(profile(ch, [(0.0, -60), (hem, -60), (hem, -95), (0.3, -98), (0, -98)], +1) +
                    [(ch[0][0] + 240, 521), (ch[0][0] - 80, 521)], t=.4)]
    m = profile(ch, [(0.1, 40), (0.3, 30), (0.45, 10)], +1)
    folds = [smooth(m, closed=False), smooth(profile(ch, [(0.2, -40), (0.4, -60), (0.5, -80)], +1), closed=False)]
    return part(d, GOWN, shade, [], folds, [], [])


def couch(x0=-400, x1=1200, y=520, h=80):
    return "\n".join([blob(f"M {x0} {y} L {x1} {y} L {x1} {y + h} L {x0} {y + h} Z", COUCH),
                      blob(f"M {x0} {y} L {x1} {y} L {x1} {y + 12} L {x0} {y + 12} Z", COUCH_H),
                      lines([f"M {x0} {y} L {x1} {y}", f"M {x0} {y + h - 14} L {x1} {y + h - 14}"], 2.4, INK)])


def pillow_head(x, y):
    """Edge of pillow only (head is out of frame)."""
    return part(f"M {x} {y} C {x + 40} {y - 30} {x + 160} {y - 34} {x + 220} {y - 10} L {x + 230} {y + 40} L {x} {y + 40} Z", "#eef3f7", ["M 0 0"], [], [], [], [])


# ------------------------------------------------------------------ 1. temperature (from above)
def temperature():
    b = [blob("M 34 -10 L 566 -10 L 566 910 L 34 910 Z", COUCH),
         blob("M 108 160 C 100 420 128 700 140 880 L 262 880 C 274 700 292 420 292 160 Z", "#0d1b2e", .5),
         blob("M 492 160 C 500 420 472 700 460 880 L 338 880 C 326 700 308 420 308 160 Z", "#0d1b2e", .5),
         leg_from_above(), f'<g transform="translate(600 0) scale(-1 1)">{leg_from_above()}</g>']
    b.append(hand_svg("flat", 92, 560, 2, .76, left=True, palmar=True, arm_len=260))
    b.append(arrow("M 214 660 C 216 600 218 470 220 420", dash="10 8"))
    b.append(arrow("M 300 600 L 368 600", w=3.5) + arrow("M 300 600 L 232 600", w=3.5))
    return svg(600, 520, "\n".join(b), y0=240)


# ------------------------------------------------------------------ 2. capillary refill (foot from above)
def cap_refill():
    b = [blob("M 0 100 L 800 100 L 800 600 L 0 600 Z", "#ffffff"), blob("M 0 128 L 800 128 L 800 600 L 0 600 Z", COUCH),
         blob("M 0 128 L 800 128 L 800 146 L 0 146 Z", COUCH_H), lines(["M 0 146 L 800 146"], 2, "#122238"),
         part(RFOOT, SKIN, RFOOT_SHADE, RFOOT_LIGHT, RFOOT_LINES, RFOOT_FAINT, RFOOT_WEIGHT, transform="translate(470 18) scale(-1 1)"),
         blob("M 452 280 C 470 360 470 470 462 600 L 440 600 C 450 480 458 380 448 280 Z", "#0d1b2e", .45),
         part(RFOOT, SKIN, RFOOT_SHADE, RFOOT_LIGHT, RFOOT_LINES, RFOOT_FAINT, RFOOT_WEIGHT)]
    body, thumb, sl = pen_hand(214, 326, -48, .95, left=False, arm_len=260)
    b += [body, thumb, sl]
    return svg(800, 500, "\n".join(b), y0=100)


# ------------------------------------------------------------------ 3. femoral pulse (hips from above)
def hips():
    d = smooth([(196, -20), (186, 60), (166, 140), (152, 230), (156, 330), (166, 450), (176, 600), (330, 600, 'c'),
                (336, 470), (342, 390), (350, 360, 'c'), (358, 390), (364, 470), (370, 600, 'c'), (524, 600, 'c'),
                (534, 450), (544, 330), (548, 230), (534, 140), (514, 60), (504, -20)], t=.5)
    shade = [smooth([(196, -20), (186, 60), (166, 140), (152, 230), (156, 330), (166, 450), (176, 600), (206, 600),
                     (196, 450), (190, 330), (188, 230), (196, 140), (214, 60), (220, -20)], t=.4),
             smooth([(504, -20), (514, 60), (534, 140), (548, 230), (544, 330), (534, 450), (524, 600), (500, 600),
                     (512, 450), (520, 330), (522, 230), (510, 140), (494, 60)], t=.4),
             smooth([(338, 600), (342, 470), (348, 380), (352, 380), (356, 470), (362, 600)], t=.4)]
    light = [smooth([(230, 40), (250, 200), (250, 400), (240, 590), (276, 590), (290, 400), (290, 200), (270, 40)], t=.4),
             smooth([(430, 40), (412, 200), (412, 400), (420, 590), (454, 590), (460, 400), (456, 200), (466, 40)], t=.4)]
    faint = ["M 196 150 C 230 200 280 250 320 296", "M 504 150 C 470 200 420 250 380 296",
             "M 188 140 C 192 132 200 130 206 136", "M 512 140 C 508 132 500 130 494 136",
             "M 240 330 C 250 420 262 500 270 590", "M 460 330 C 450 420 438 500 430 590"]
    return part(d, SKIN, shade, light, [], faint, [])


def femoral():
    b = [blob("M 40 -40 L 660 -40 L 660 640 L 40 640 Z", COUCH),
         blob("M 140 0 C 128 200 140 400 160 640 L 540 640 C 560 400 572 200 560 0 Z", "#0d1b2e", .45), hips()]
    # modesty drape over the pubic area
    b.append(part("M 268 180 C 300 170 400 170 432 180 C 428 240 410 300 380 352 C 366 372 334 372 320 352 C 290 300 272 240 268 180 Z",
                  "#eef3f8", ["M 300 300 C 330 330 370 330 400 300 L 380 352 C 366 372 334 372 320 352 Z"], [],
                  ["M 300 200 C 320 240 330 280 336 330", "M 400 200 C 384 240 372 280 366 330"], [], [], shade_fill="#d3dde7"))
    b.append(part("M 120 -60 L 580 -60 L 580 60 C 520 80 440 84 350 76 C 260 84 180 80 120 60 Z", GOWN,
                  ["M 120 30 C 200 52 280 56 350 50 C 420 56 500 52 580 30 L 580 70 L 120 70 Z"], [],
                  ["M 200 -40 C 206 0 210 30 206 70", "M 350 -40 C 352 0 352 40 350 76", "M 500 -40 C 494 0 490 30 494 70"], [], []))
    b.append(blob("M 252 236 C 262 228 280 232 286 244 C 280 252 262 252 252 236 Z", SKIN_S, .8))
    b.append(hand_svg("press2", 98, 318, -16, .88, arm_len=260))
    return svg(620, 560, "\n".join(b), x0=40, y0=-20)


# ------------------------------------------------------------------ 4. posterior tibial pulse (medial view of the ankle)
def pt_pulse():
    ch = chain_from((-160, 430), 0, 2)
    b = [couch(), f'<g transform="translate(1020 0) scale(-1 1)">{side_leg(ch)}</g>']
    b.append(hand_svg("press2", 318, 330, 112, .9, arm_len=260))
    return svg(760, 560, "\n".join(b), x0=40, y0=40)


# ------------------------------------------------------------------ 5. Buerger's test (leg raised)
def buerger():
    H = (-160, 430)
    ch = chain_from(H, -40, -40)
    b = [couch(), far_leg(), gown_on(ch)]
    b.insert(2, side_leg(ch, pale=True))
    # examiner's hand under the heel
    heel = profile(ch, [(1.9, -40)], +1)[0]
    b.append(hand_svg("flat", heel[0] + 112, heel[1] + 78, -150, .9, left=True, palmar=True, arm_len=300))
    # angle guide at the hip
    b.append(lines(["M -160 430 L 260 430", "M -160 430 L 180 145"], 2.5, "#167a8b", .9))
    b.append(f'<path d="M 140 430 A 300 300 0 0 0 70 237" fill="none" stroke="#167a8b" stroke-width="3" stroke-dasharray="8 6"/>')
    b.append(arrow("M 560 330 C 600 280 630 240 650 200", w=4))
    return svg(1080, 1020, "\n".join(b), x0=-200, y0=-420)


# ------------------------------------------------------------------ 6. tourniquet test
def tourniquet():
    H = (-160, 430)
    ch = chain_from(H, -28, -28)
    strap_c = profile(ch, [(0.42, 92), (0.42, -92)], +1)
    strap = profile(ch, [(0.38, 96), (0.46, 96), (0.46, -98), (0.38, -98)], +1)
    sd = smooth([strap[0], lerp(strap[0], strap[3], .5), strap[3], strap[2], lerp(strap[1], strap[2], .5), strap[1]], t=.3)
    b = [couch(), far_leg(), side_leg(ch), gown_on(ch, hem=.3),
         part(sd, "#7b8794", [smooth([strap[3], strap[2], lerp(strap[1], strap[2], .5), lerp(strap[0], strap[3], .5)], t=.3)], [],
              [f"M {strap_c[0][0]:.0f} {strap_c[0][1]:.0f} L {strap_c[1][0]:.0f} {strap_c[1][1]:.0f}"], [], [], shade_fill="#5d6773")]
    # tourniquet tails
    tail = profile(ch, [(0.42, 96)], +1)[0]
    b.append(part(f"M {tail[0]-8:.0f} {tail[1]:.0f} C {tail[0]-30:.0f} {tail[1]-50:.0f} {tail[0]-10:.0f} {tail[1]-90:.0f} {tail[0]+14:.0f} {tail[1]-110:.0f} "
                  f"L {tail[0]+26:.0f} {tail[1]-100:.0f} C {tail[0]+6:.0f} {tail[1]-80:.0f} {tail[0]-8:.0f} {tail[1]-46:.0f} {tail[0]+10:.0f} {tail[1]:.0f} Z", "#7b8794", [], [], [], [], []))
    b.append(hand_svg("flat", 760, 140, -118, .9, left=True, palmar=True, arm_len=300))
    return svg(1080, 820, "\n".join(b), x0=-200, y0=-220)


# ------------------------------------------------------------------ 7. pitting oedema (side view, thumb on shin)
def straight_leg_scene():
    ch = chain_from((-160, 430), -1, 1.5)
    return ch, [couch(), side_leg(ch), gown_on(ch, hem=.55)]


def pitting():
    ch, b = straight_leg_scene()
    pit = profile(ch, [(1.62, 44)], +1)[0]
    b.append(blob(f"M {pit[0]-50:.0f} {pit[1]+4:.0f} C {pit[0]-44:.0f} {pit[1]+14:.0f} {pit[0]-30:.0f} {pit[1]+14:.0f} {pit[0]-24:.0f} {pit[1]+4:.0f} Z", SKIN_S, 1))
    b.append(lines([f"M {pit[0]-52:.0f} {pit[1]+4:.0f} C {pit[0]-44:.0f} {pit[1]+16:.0f} {pit[0]-30:.0f} {pit[1]+16:.0f} {pit[0]-22:.0f} {pit[1]+4:.0f}"], 1.6, INK))
    # thumb on the shin, fingers wrapped around the calf (same grip as the approved popliteal drawing)
    from draw_pvd import pop_hand, sleeve
    h = pop_hand()
    g = part(h["d"], GLOVE, h["shade"], h["light"], h["lines"], h["faint"], []) + sleeve(256, 340, 180, 300, 174)
    b.append(f'<g transform="translate({pit[0] + 6:.0f} {pit[1] + 2:.0f}) rotate(-22) translate(-412 -262)">{g}</g>')
    return svg(900, 560, "\n".join(b), x0=150, y0=40)


# ------------------------------------------------------------------ 8. calf circumference
def calf_measure():
    ch, b = straight_leg_scene()
    tt = profile(ch, [(1.12, 56)], +1)[0]                      # tibial tuberosity
    tp = profile(ch, [(1.34, 62), (1.34, -84)], +1)           # tape line (10 cm below)
    tp2 = profile(ch, [(1.37, 62), (1.37, -86)], +1)
    tape = smooth([tp[0], lerp(tp[0], tp[1], .5), tp[1], tp2[1], lerp(tp2[0], tp2[1], .5), tp2[0]], t=.25)
    ticks = []
    for k in range(1, 12):
        a, c = lerp(tp[0], tp[1], k / 12), lerp(tp2[0], tp2[1], k / 12)
        ticks.append(f"M {a[0]:.1f} {a[1]:.1f} L {lerp(a, c, .45)[0]:.1f} {lerp(a, c, .45)[1]:.1f}")
    b.append(part(tape, "#f3d34a", [], [], [], ticks, [], sw=2.2, shade_fill="#d7b52f"))
    b.append(part(f"M {tp[0][0]:.0f} {tp[0][1]:.0f} C {tp[0][0]+20:.0f} {tp[0][1]-60:.0f} {tp[0][0]+60:.0f} {tp[0][1]-90:.0f} {tp[0][0]+90:.0f} {tp[0][1]-110:.0f} "
                  f"L {tp[0][0]+98:.0f} {tp[0][1]-100:.0f} C {tp[0][0]+70:.0f} {tp[0][1]-80:.0f} {tp[0][0]+34:.0f} {tp[0][1]-50:.0f} {tp2[0][0]:.0f} {tp2[0][1]:.0f} Z", "#f3d34a", [], [], [], [], [], sw=2.2))
    body, thumb, sl = pen_hand(tp[0][0] + 150, tp[0][1] - 230, 112, .9, arm_len=240)
    b += [body, thumb, sl]
    # 10 cm guide from tibial tuberosity
    b.append(lines([f"M {tt[0]:.0f} {tt[1]-40:.0f} L {tt[0]:.0f} {tt[1]-8:.0f}", f"M {tp[0][0]:.0f} {tp[0][1]-40:.0f} L {tp[0][0]:.0f} {tp[0][1]-10:.0f}"], 2.5, "#167a8b"))
    b.append(arrow(f"M {tt[0]+4:.0f} {tt[1]-30:.0f} L {tp[0][0]-4:.0f} {tp[0][1]-30:.0f}", w=3) +
             arrow(f"M {tp[0][0]-4:.0f} {tp[0][1]-30:.0f} L {tt[0]+4:.0f} {tt[1]-30:.0f}", w=3))
    return svg(900, 560, "\n".join(b), x0=150, y0=40)


ALL = dict(pvd_temperature=temperature, pvd_cap_refill=cap_refill, pvd_femoral_pulse=femoral, pvd_pt_pulse=pt_pulse,
           pvd_buerger=buerger, pvd_tourniquet=tourniquet, pvd_pitting=pitting, pvd_calf_measure=calf_measure)

if __name__ == "__main__":
    for k in (sys.argv[1:] or ALL):
        print(save(k, ALL[k](), OUT))
