"""Topic 9: surgical skills – instruments, gloving, knots, suturing, suture packet."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from art import *
OUT = os.path.join(os.path.dirname(__file__), "svg")
STEEL, STEEL_S, STEEL_H = "#c9d1d9", "#97a3ae", "#f4f7f9"
THREAD = "#6b4fa0"


def T_(x, y, ang, sc):
    fn = affine(x, y, sc, ang)
    return lambda d: tpath(d, fn)


def ring(cx, cy, r1, r2):
    o = smooth([(cx + r1 * math.cos(a), cy + r1 * math.sin(a)) for a in [i * math.pi / 6 for i in range(12)]])
    i = smooth([(cx + r2 * math.cos(a), cy + r2 * math.sin(a)) for a in [i * math.pi / 6 for i in range(12)]][::-1])
    return o + " " + i


def needle_holder(x, y, ang=0, sc=1.0, open_=0):
    """Tip at local (300,0) pointing +x; rings at x~0..60."""
    T = T_(x, y, ang, sc)
    a = open_
    sh1 = f"M 40 {-20 - a} C 100 {-16 - a} 170 -8 210 -6 L 210 2 C 170 0 100 {-6 - a} 44 {-8 - a} Z"
    sh2 = f"M 40 {20 + a} C 100 {16 + a} 170 8 210 6 L 210 -2 C 170 0 100 {6 + a} 44 {8 + a} Z"
    jaws = "M 206 -9 L 290 -5 C 300 -4 302 4 290 5 L 206 9 Z"
    out = []
    for sh, rcy in ((sh1, -26 - a), (sh2, 26 + a)):
        out.append(part(T(sh), STEEL, [], [], [], [], [], sw=2))
        out.append(f'<path d="{T(ring(22, rcy, 22, 14))}" fill="{STEEL}" fill-rule="evenodd" stroke="{INK}" stroke-width="2"/>')
    out.append(part(T(jaws), STEEL, [T("M 206 2 L 296 2 C 300 4 296 5 290 5 L 206 9 Z")], [T("M 214 -6 L 280 -3 L 280 -1 L 214 -3 Z")],
                    [T(f"M {xx} -4 L {xx + 4} 4") for xx in range(240, 292, 7)], [], [], sw=2, shade_fill=STEEL_S, light_fill=STEEL_H))
    out.append(part(T(smooth([(196, -12), (214, -12), (218, 0), (214, 12), (196, 12), (192, 0)])), STEEL_S, [], [], [], [], [], sw=2))
    return "\n".join(out)


def forceps(x, y, ang=0, sc=1.0):
    """Toothed dissecting forceps, tip at local (240,0)."""
    T = T_(x, y, ang, sc)
    a1 = "M 0 -14 C 80 -14 160 -8 238 -3 L 240 0 L 236 1 C 160 -2 80 -6 0 -6 Z"
    a2 = "M 0 14 C 80 14 160 8 238 3 L 240 0 L 236 -1 C 160 2 80 6 0 6 Z"
    return (part(T(a1), STEEL, [], [T("M 10 -12 L 150 -9 L 150 -8 L 10 -10 Z")], [T(f"M {xx} -12 L {xx} -7") for xx in range(30, 90, 10)], [], [], sw=2, light_fill=STEEL_H)
            + part(T(a2), STEEL_S, [], [], [T(f"M {xx} 12 L {xx} 7") for xx in range(30, 90, 10)], [], [], sw=2))


def curved_needle(cx, cy, r=34, a0=200, a1=335, w=3.2):
    p0 = (cx + r * math.cos(math.radians(a0)), cy + r * math.sin(math.radians(a0)))
    p1 = (cx + r * math.cos(math.radians(a1)), cy + r * math.sin(math.radians(a1)))
    return (f'<path d="M {p0[0]:.1f} {p0[1]:.1f} A {r} {r} 0 0 1 {p1[0]:.1f} {p1[1]:.1f}" fill="none" stroke="{INK}" stroke-width="{w + 2.4}" stroke-linecap="round"/>'
            f'<path d="M {p0[0]:.1f} {p0[1]:.1f} A {r} {r} 0 0 1 {p1[0]:.1f} {p1[1]:.1f}" fill="none" stroke="{STEEL}" stroke-width="{w}" stroke-linecap="round"/>')


def thread(d, w=3.2, color=THREAD):
    return (f'<path d="{d}" fill="none" stroke="{INK}" stroke-width="{w + 2}" stroke-linecap="round" stroke-linejoin="round"/>'
            f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>')


def skin_pad(x0=120, y0=300, w=560, h=200, wound=True):
    top = f"M {x0} {y0} L {x0 + w} {y0} L {x0 + w + 40} {y0 + 60} L {x0 + 40} {y0 + 60} Z"
    out = part(f"M {x0} {y0} L {x0 + w} {y0} L {x0 + w + 40} {y0 + 60} L {x0 + w + 40} {y0 + 60 + h * .35} L {x0 + 40} {y0 + 60 + h * .35} L {x0} {y0 + h * .35} Z",
               "#f2c9a7", [f"M {x0 + 40} {y0 + 60} L {x0 + w + 40} {y0 + 60} L {x0 + w + 40} {y0 + 60 + h * .35} L {x0 + 40} {y0 + 60 + h * .35} Z",
                           f"M {x0 + 40} {y0 + 72} L {x0 + w + 40} {y0 + 72} L {x0 + w + 40} {y0 + 60 + h * .35} L {x0 + 40} {y0 + 60 + h * .35} Z"],
               [], [], [], [], sw=2.4, shade_fill="#f3d98a")
    if wound:
        out += part(f"M {x0 + 100} {y0 + 30} C {x0 + 220} {y0 + 24} {x0 + 360} {y0 + 24} {x0 + 470} {y0 + 30} C {x0 + 360} {y0 + 38} {x0 + 220} {y0 + 38} {x0 + 100} {y0 + 30} Z",
                    "#b33a3a", [], [], [], [], [], sw=1.8)
    return out


# ------------------------------------------------------------------ sterile gloving
def glove_wrapper():
    return part("M 40 360 L 760 360 L 800 560 L 0 560 Z", "#f4f1e8", ["M 0 540 L 800 540 L 800 560 L 0 560 Z"], [],
                ["M 400 360 L 400 560"], ["M 60 380 L 380 380", "M 420 380 L 740 380"], [], sw=2.2, shade_fill="#e2ddd0")


def folded_cuff(x, y, ang, sc=1.0, w=50, ln=46):
    T = T_(x, y, ang, sc)
    return part(T(f"M 0 {-w} L {-ln} {-w - 4} L {-ln} {w + 4} L 0 {w} Z"), GLOVE, [T(f"M {-ln} {w * .3} L 0 {w * .3} L 0 {w} L {-ln} {w + 4} Z")],
                [], [T(f"M -8 {-w + 2} L -8 {w - 2}")], [], [], sw=2.4)


def glove1():
    b = [glove_wrapper()]
    # left (spare) glove lying in the wrapper
    b.append(hand_svg("flat", 600, 470, -90, .9, left=True, arm="none"))
    b.append(folded_cuff(600, 470, -90, .9))
    # right hand entering the first glove (cuff still folded) + bare forearm
    b.append(hand_svg("flat", 330, 330, -100, 1.0, glove=True, arm="skin", arm_len=260))
    b.append(folded_cuff(330, 330, -100, 1.0))
    # bare left hand pinches the folded cuff edge (inside surface only)
    body, thumb, sl = pen_at((290, 360), -10, 1.0, left=True, glove=False, arm="skin", arm_len=220)
    b += [body, thumb]
    return svg(820, 620, "\n".join(b), y0=20)


def glove2():
    b = [glove_wrapper()]
    # left hand going into the second glove; gloved right fingers under its cuff
    b.append(hand_svg("flat", 420, 360, -80, 1.0, left=True, glove=True, arm="skin", arm_len=260))
    b.append(hand_at("flat", (430, 392), 175, .95, what="mid4", glove=True, arm="none"))
    b.append(folded_cuff(420, 360, -80, 1.0))
    return svg(820, 620, "\n".join(b), y0=20)


# ------------------------------------------------------------------ instrument tie
def knot1():
    b = [skin_pad()]
    # suture through the wound: short tail left, long end to the left hand
    b.append(thread("M 300 330 C 290 300 260 290 240 300"))
    b.append(thread("M 330 330 C 340 280 380 250 420 236 C 460 222 500 214 560 190"))
    b.append(needle_holder(140, 120, 22, 1.0))
    # two wraps of the long end around the needle-holder jaws
    for k in (0, 1):
        x = 360 + k * 14
        b.append(thread(f"M {x} 236 C {x - 10} 220 {x + 4} 206 {x + 16} 214 C {x + 24} 222 {x + 18} 236 {x + 8} 240"))
    body, thumb, sl = pen_at((560, 190), 200, 1.0, left=True, arm_len=240)
    b += [body, thumb, sl]
    body, thumb, sl = pen_at((150, 140), 22, 1.0, arm_len=240)
    b += [body, thumb, sl]
    return svg(820, 560, "\n".join(b), y0=10)


def knot2():
    b = [skin_pad()]
    # throw laid flat across the wound, hands pulling in opposite directions
    b.append(thread("M 300 330 C 310 318 330 318 340 330"))
    b.append(thread("M 316 322 C 270 300 220 280 160 262"))
    b.append(thread("M 324 322 C 380 300 460 280 560 262"))
    b.append(lines(["M 300 326 C 310 316 330 316 344 326"], 2, INK))
    b.append(thread("M 160 262 L 140 258"))
    b.append(needle_holder(-140, 258, 0, 1.0))
    body, thumb, sl = pen_at((560, 262), 200, 1.0, left=True, arm_len=240)
    b += [body, thumb, sl]
    body, thumb, sl = pen_at((-120, 258), 0, 1.0, arm_len=200)
    b += [body, thumb, sl]
    b.append(arrow("M 100 210 L 30 204", w=4) + arrow("M 470 220 L 540 214", w=4))
    return svg(960, 560, "\n".join(b), x0=-240, y0=10)


# ------------------------------------------------------------------ needle loading & first bite
def needle_load():
    b = [needle_holder(60, 300, 0, 2.0)]
    b.append(curved_needle(620, 336, 52, 190, 350, 5))
    b.append(thread("M 570 330 C 560 380 540 420 520 470", 3))
    body, thumb, sl = pen_at((150, 300), 0, 1.2, arm_len=240)
    b += [body, thumb, sl]
    b.append(lines(["M 662 280 L 662 250", "M 572 280 L 572 250"], 2.4, "#167a8b"))
    b.append(arrow("M 590 258 L 572 258", w=2.5) + arrow("M 600 258 L 662 258", w=2.5))
    return svg(760, 460, "\n".join(b), x0=0, y0=140)


def suture():
    b = [skin_pad()]
    b.append(curved_needle(400, 312, 28, 200, 300, 4))
    b.append(needle_holder(130, 180, 30, 1.0))
    body, thumb, sl = pen_at((150, 200), 30, 1.0, arm_len=240)
    b += [body, thumb, sl]
    b.append(forceps(640, 170, 140, 1.0))
    body, thumb, sl = pen_at((600, 210), 140, 1.0, left=True, arm_len=240)
    b += [body, thumb, sl]
    b.append(lines(["M 372 300 L 372 260"], 2.4, "#167a8b"))
    return svg(820, 560, "\n".join(b), y0=10)


# ------------------------------------------------------------------ suture packet (no text – fields are blank bars)
def packet_map():
    b = [part("M 40 40 L 760 40 L 760 520 L 40 520 Z", "#f4f6f9", ["M 40 500 L 760 500 L 760 520 L 40 520 Z"], [], [], [], [], sw=2.6, shade_fill="#dfe5ec")]
    b.append(part("M 40 40 L 760 40 L 760 110 L 40 110 Z", "#6b4fa0", [], [], [], [], [], sw=2.6))
    bar = lambda x, y, w, h=12, c="#9aa6b2": blob(f"M {x} {y} L {x + w} {y} L {x + w} {y + h} L {x} {y + h} Z", c)
    b += [bar(70, 62, 220, 20, "#ffffff"), bar(70, 88, 140, 10, "#d9cdee")]
    b += [bar(300, 62, 110, 26, "#ffffff"), bar(560, 62, 150, 20, "#ffffff")]
    # needle drawing (actual size) + point symbol + needle length
    b.append(curved_needle(150, 300, 70, 200, 340, 5))
    b.append('<path d="M 400 260 L 430 312 L 370 312 Z" fill="#1f3a5e"/>')
    b.append(lines(["M 560 300 L 700 300", "M 560 290 L 560 310", "M 700 290 L 700 310"], 2.6, "#1f3a5e"))
    b += [bar(560, 320, 140, 12), bar(370, 330, 70, 10)]
    # coiled suture window
    b.append(part("M 80 380 L 360 380 L 360 470 L 80 470 Z", "#e8f1f8", [], [], [], [], [], sw=2))
    for i in range(4):
        b.append(thread(f"M 100 {396 + i * 18} C 160 {388 + i * 18} 280 {404 + i * 18} 340 {396 + i * 18}", 2.4))
    b += [bar(420, 400, 260, 12), bar(420, 424, 200, 12), bar(420, 448, 230, 12)]
    b.append("".join(f'<path d="M {x} 470 L {x} 494" stroke="#1d2a3a" stroke-width="{1 + (x % 3)}"/>' for x in range(600, 740, 5)))
    return svg(800, 560, "\n".join(b))


ALL = dict(sk_glove1=glove1, sk_glove2=glove2, sk_knot1=knot1, sk_knot2=knot2, sk_needle_load=needle_load, sk_suture=suture, sk_packet_map=packet_map)
if __name__ == "__main__":
    for k in (sys.argv[1:] or ALL):
        save(k, ALL[k](), OUT)
