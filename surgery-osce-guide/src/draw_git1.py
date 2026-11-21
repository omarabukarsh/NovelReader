"""Topic 3: hands & nails (patient), Schamroth window, asterixis."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from art import *
OUT = os.path.join(os.path.dirname(__file__), "svg")
NAIL, NAIL_S = "#f6d9cf", "#e3b7a8"


def finger_side(x, y, ang=0, sc=1.0, clubbed=False, flip=False, glove=False):
    """Side view of the distal finger, pointing +x, nail on top. One outline for the finger, one for the nail."""
    if clubbed:
        F = [(-10, -17), (40, -19), (62, -21), (80, -26), (104, -26), (124, -16), (130, 0), (122, 14), (100, 22),
             (74, 20), (56, 15), (30, 16), (-10, 17)]
        N = [(70, -24), (84, -31), (104, -31), (122, -21), (128, -10), (124, -8), (116, -18), (100, -25), (84, -25), (72, -21)]
    else:
        F = [(-10, -17), (40, -18), (64, -18), (84, -19), (104, -18), (120, -12), (126, 0), (120, 10), (100, 14),
             (74, 13), (56, 12), (30, 15), (-10, 17)]
        N = [(72, -19), (86, -23), (104, -22), (118, -17), (124, -10), (120, -9), (112, -14), (100, -17), (86, -17), (74, -16)]
    fn = affine(x, y, sc, ang, flipy=flip)
    T = lambda pts: tpath(smooth(pts, t=.5), fn)
    To = lambda pts: tpath(smooth(pts, closed=False, t=.5), fn)
    fill = GLOVE if glove else SKIN
    sh = T([(-10, 8), (56, 6), (100, 8), (122, 4), (120, 10), (100, 14), (74, 13), (56, 12), (30, 15), (-10, 17)])
    out = part(T(F), fill, [sh], [], [tpath("M 54 -17 C 52 -10 52 -4 54 0", fn), tpath("M 58 12 C 60 6 60 2 58 -2", fn)], [], [], stroke=To(F))
    out += part(T(N), NAIL, [], [T([(86, -22), (104, -21), (116, -16), (104, -18), (88, -19)])], [], [], [], sw=1.8, light_fill="#fff3ee")
    return out


def fingertip_pair_window():
    b = []
    # normal pair: diamond window; clubbed pair: window obliterated
    b.append(finger_side(150, 360, -90, 1.6, False, flip=False))
    b.append(finger_side(250, 360, -90, 1.6, False, flip=True))
    b.append(finger_side(560, 360, -90, 1.6, True, flip=False))
    b.append(finger_side(642, 360, -90, 1.6, True, flip=True))
    b.append('<path d="M 200 188 L 210 168 L 200 148 L 190 168 Z" fill="none" stroke="#167a8b" stroke-width="3"/>')
    b.append(lines(["M 120 420 L 280 420", "M 530 420 L 672 420"], 2, "#c8d2dc"))
    return svg(800, 440, "\n".join(b), y0=60)


def hand_map():
    b = []
    # top: normal vs clubbed fingertip profiles with nail-fold angle guide
    b.append(finger_side(40, 150, 0, 2.2, False))
    b.append(finger_side(380, 150, 0, 2.2, True))
    b.append(lines(["M 196 112 L 230 110 L 296 98", "M 538 104 L 572 92 L 640 96"], 2.4, "#167a8b"))
    b.append(lines(["M 30 250 L 670 250"], 1.5, "#d6dee7"))
    # bottom: dorsal view and palmar view
    b.append(hand_svg("flat", 190, 760, -90, 1.55, left=False, glove=False, arm="skin", arm_len=120))
    b.append(hand_svg("flat", 520, 760, -90, 1.55, left=False, glove=False, arm="skin", arm_len=120, palmar=True))
    b.append(blob(smooth([(456, 710), (474, 680), (492, 692), (494, 726), (474, 742)]), "#e46f63", .33))
    b.append(blob(smooth([(584, 702), (568, 676), (550, 686), (548, 722), (566, 736)]), "#e46f63", .33))
    b.append(lines(["M 540 600 C 542 620 540 640 536 664"], 3, INK_SOFT, .8))
    return svg(700, 780, "\n".join(b))


def side_hand_up(x, y, ang=-60, sc=1.0):
    fn = affine(x, y, sc, ang)
    T = lambda d: tpath(d, fn)
    H = [(-20, -17), (40, -20), (80, -19), (110, -15), (140, -11), (165, -7), (176, 0), (170, 7), (140, 9), (110, 11),
         (86, 15), (60, 25), (30, 25), (-20, 19)]
    TH = [(24, 6), (56, 2), (86, 4), (100, 9), (94, 15), (60, 20), (30, 22)]
    body = part(T(smooth(H)), SKIN, [T(smooth([(-20, 10), (40, 12), (86, 10), (140, 4), (170, 4), (140, 9), (86, 15), (30, 25), (-20, 19)], t=.4))],
                [T(smooth([(10, -12), (80, -14), (150, -6), (80, -9), (10, -6)], t=.4))],
                [T("M 110 -15 C 112 -8 112 -2 110 4"), T("M 140 -11 C 142 -6 142 -2 140 2")],
                [T("M 92 -6 L 170 -2"), T("M 96 2 L 160 4"), T("M 160 -8 C 166 -8 170 -4 170 -2 C 166 -3 162 -5 160 -8 Z")], [],
                stroke=T(smooth(H, closed=False)))
    thumb = part(T(smooth(TH)), SKIN, [T(smooth([(40, 16), (90, 12), (94, 15), (60, 20)], t=.4))], [], [T("M 70 4 C 72 10 72 14 70 18")], [], [])
    return body + thumb


def asterixis():
    b = []
    fa = forearm_local(380, 32, 40)
    fn = affine(470, 330, 1.0, 0)
    b.append(part(tpath(fa["d"], fn), SKIN, [tpath(s, fn) for s in fa["shade"]], [], [], [tpath(s, fn) for s in fa["faint"]], [], stroke=tpath(fa["stroke"], fn)))
    b.append(part("M 40 270 L 140 278 L 136 384 L 36 392 Z", GOWN, [], [], ["M 120 286 C 126 320 126 350 120 378"], [], []))
    b.append(side_hand_up(470, 330, -62, 1.15))
    b.append(f'<path d="M 640 70 A 230 230 0 0 1 690 210" fill="none" stroke="#167a8b" stroke-width="4" stroke-dasharray="9 7"/>')
    b.append(arrow("M 664 120 C 676 150 684 176 690 206", w=4) + arrow("M 672 150 C 664 120 652 96 638 74", w=4))
    return svg(760, 460, "\n".join(b), y0=-20)


ALL = dict(git1_hand_map=hand_map, git1_hands=fingertip_pair_window, git1_asterixis=asterixis)
if __name__ == "__main__":
    for k in (sys.argv[1:] or ALL):
        save(k, ALL[k](), OUT)
