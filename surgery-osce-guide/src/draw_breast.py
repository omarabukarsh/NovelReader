"""Topic 7: breast & axilla (patient draped; schematic diagram for quadrants)."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from art import *
from draw_head import neck_torso, head, gown_front, HAIR, HAIR_S
OUT = os.path.join(os.path.dirname(__file__), "svg")


def hair_long():
    d = smooth([(204, 150), (186, 240), (178, 340), (188, 420), (230, 452), (300, 440), (370, 452), (412, 420), (422, 340),
                (414, 240), (396, 150), (380, 70), (300, 30), (220, 70)], t=.5)
    return part(d, HAIR, [smooth([(188, 420), (230, 452), (300, 440), (370, 452), (412, 420), (380, 430), (300, 424), (220, 430)], t=.4)], [],
                ["M 214 300 C 210 350 214 400 226 440", "M 386 300 C 390 350 386 400 374 440"], [], [], shade_fill=HAIR_S)


def arm_limb(ch, w=(30, 24, 21), right=True):
    """Arm outline along [shoulder, elbow, wrist]; shoulder end left open (merges with the torso)."""
    a = profile(ch, [(0.0, w[0]), (0.5, w[0] * .95), (1.0, w[1]), (1.5, w[2] * 1.1), (2.0, w[2])], +1)
    b = profile(ch, [(2.0, w[2]), (1.5, w[2] * 1.15), (1.0, w[1]), (0.5, w[0]), (0.0, w[0] * 1.05)], -1)
    d = smooth(a + b, t=.5)
    st = smooth(a, closed=False) + " " + smooth(b, closed=False)
    sh = smooth(profile(ch, [(0.1, -w[0]), (1.0, -w[1]), (1.9, -w[2]), (1.9, -w[2] * .2), (1.0, -w[1] * .3), (0.1, -w[0] * .3)], +1), t=.4)
    end = profile(ch, [(2.0, w[2]), (2.0, -w[2])], +1)
    st += f" M {end[0][0]:.1f} {end[0][1]:.1f} L {end[1][0]:.1f} {end[1][1]:.1f}"
    return part(d, SKIN, [sh], [], [], [smooth(profile(ch, [(0.9, 6), (1.0, 0), (1.1, 6)], +1), closed=False)], [], stroke=st)


def arm_with_hand(ch, left_side=True, hand_ang=None, palmar=False):
    out = arm_limb(ch)
    ang = hand_ang if hand_ang is not None else math.degrees(math.atan2(ch[2][1] - ch[1][1], ch[2][0] - ch[1][0]))
    out += hand_svg("flat", ch[2][0], ch[2][1], ang, .72, left=not left_side, glove=False, arm="none", open_wrist=True, palmar=palmar)
    return out


def drape():
    d = "M 40 500 C 140 520 240 560 300 566 C 360 560 460 520 560 500 L 600 900 L 0 900 Z"
    return part(d, GOWN, ["M 0 760 L 600 760 L 600 900 L 0 900 Z"], [], ["M 300 566 C 300 680 300 780 300 900", "M 160 540 C 170 660 176 760 170 900",
                                                                         "M 440 540 C 430 660 424 760 430 900"], [], [])


def figure(pose):
    L, R = (96, 500), (504, 500)
    if pose == "sides":
        armsL, armsR = [L, (78, 690), (88, 860)], [R, (522, 690), (512, 860)]
    elif pose == "hips":
        armsL, armsR = [L, (20, 650), (140, 760)], [R, (580, 650), (460, 760)]
    else:  # raised
        armsL, armsR = [L, (66, 320), (150, 150)], [R, (534, 320), (450, 150)]
    out = [hair_long(), neck_torso(False), drape()]
    if pose == "raised":
        out.insert(0, arm_with_hand(armsL, True) + arm_with_hand(armsR, False))
        out.append(head())
    else:
        out.append(head())
        out.append(arm_with_hand(armsL, True) + arm_with_hand(armsR, False))
    # head hair cap (fringe) is part of head(); long hair behind already drawn
    return "\n".join(out)


def positions():
    g = []
    for i, p in enumerate(("sides", "hips", "raised")):
        g.append(f'<g transform="translate({i * 340 + 10} 0) scale(.55)">{figure(p)}</g>')
        if i:
            g.append(lines([f"M {i * 340 + 4} 40 L {i * 340 + 4} 500"], 1.5, "#d6dee7"))
    return svg(1030, 500, "\n".join(g), y0=20)


# ------------------------------------------------------------------ schematic: right breast, quadrants & axillary tail
CX, CY = 205, 650


def chest_diagram(lines_=True):
    out = []
    TL = [(244, 300), (238, 340), (233, 382), (220, 408), (182, 430), (122, 450), (82, 474), (62, 520), (66, 620), (80, 760), (92, 900)]
    T = TL + [(600 - p[0], p[1]) for p in TL][::-1]
    out.append(part(smooth(T, t=.5), SKIN, [smooth([(62, 520), (66, 620), (80, 760), (92, 900), (124, 900), (108, 760), (98, 620), (96, 530)], t=.4)],
                    [], [], ["M 286 478 C 240 468 170 464 104 474", "M 314 478 C 360 468 430 464 496 474", "M 292 474 C 296 480 304 480 308 474",
                             "M 240 306 C 252 360 272 430 288 470", "M 360 306 C 348 360 328 430 312 470", "M 300 490 L 300 900"], []))
    # axillary fold (arm by the side, slightly abducted)
    out.append(lines(["M 66 520 C 80 560 92 600 100 640"], 2.2, INK))
    br = smooth([(CX, CY - 110), (CX + 80, CY - 90), (CX + 110, CY), (CX + 88, CY + 90), (CX, CY + 118), (CX - 86, CY + 96),
                 (CX - 112, CY + 10), (CX - 104, CY - 46), (CX - 128, CY - 110), (CX - 132, CY - 140), (CX - 100, CY - 128), (CX - 60, CY - 104)], t=.5)
    out.append(part(br, "#f5d2b5", [smooth([(CX + 88, CY + 90), (CX, CY + 118), (CX - 86, CY + 96), (CX - 40, CY + 92), (CX + 40, CY + 86)], t=.4)],
                    [], [], [], [], sw=2.4))
    are = smooth([(CX + 20 * math.cos(a), CY + 20 * math.sin(a)) for a in [i * math.pi / 6 for i in range(12)]])
    nip = smooth([(CX + 7 * math.cos(a), CY + 7 * math.sin(a)) for a in [i * math.pi / 4 for i in range(8)]])
    out.append(part(are, "#d9a08a", [], [], [], [], [], sw=2) + part(nip, "#c4826c", [], [], [], [], [], sw=1.6))
    # drape over the other side
    out.append(part("M 300 520 C 340 500 460 490 560 500 L 610 900 L 300 900 Z", GOWN, ["M 300 760 L 610 760 L 610 900 L 300 900 Z"], [],
                    ["M 380 510 C 390 640 396 760 392 900", "M 480 500 C 486 640 490 760 494 900"], [], []))
    if lines_:
        out.append(lines([f"M {CX} {CY - 130} L {CX} {CY + 135}", f"M {CX - 130} {CY} L {CX + 130} {CY}"], 3, "#167a8b")
                   .replace('opacity="1"', 'opacity="1" stroke-dasharray="12 8"'))
    return "\n".join(out)


def quadrant_map():
    return svg(600, 560, chest_diagram(), y0=380)


def palpation():
    b = chest_diagram(lines_=False)
    for k in range(7):
        a = -math.pi / 2 + k * 2 * math.pi / 7
        x, y = CX + 72 * math.cos(a), CY + 72 * math.sin(a)
        b += f'<path d="M {x + 10:.0f} {y:.0f} A 10 10 0 1 1 {x:.0f} {y - 10:.0f}" fill="none" stroke="#167a8b" stroke-width="3"/>'
    b += f'<path d="M {CX + 112} {CY} A 112 112 0 1 1 {CX + 110} {CY - 20}" fill="none" stroke="#167a8b" stroke-width="3" stroke-dasharray="10 8"/>'
    b += hand_at("flat", (CX - 46, CY - 46), -140, .9, what="middle", left=True, arm_len=300)
    return svg(600, 560, b, y0=380)


def axilla():
    out = [hair_long(), neck_torso(False), drape(), head()]
    # examiner's right forearm (sleeve) supports the patient's forearm; examiner's left hand in the axilla
    # examiner's forearm under the patient's forearm, hand cupping the elbow
    out.append(hand_at("flat", (-40, 628), -18, .95, what="mid4", left=False, arm_len=360))
    out.append(arm_with_hand([(92, 500), (-60, 610), (-230, 700)], True))
    # examiner's other hand: fingertips pushed up into the apex of the axilla
    out.append(hand_at("tips", (92, 534), -86, .95, what="mid4", left=True, thumb=False, arm_len=300))
    return svg(820, 640, "\n".join(out), x0=-260, y0=160)


ALL = dict(breast_quadrant_map=quadrant_map, breast_positions=positions, breast_palpation=palpation, breast_axilla=axilla)
if __name__ == "__main__":
    for k in (sys.argv[1:] or ALL):
        save(k, ALL[k](), OUT)
