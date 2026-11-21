"""Diagram-style illustrations: scrotal contents (topic 5) and ulcer edges (topic 6)."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from art import *
from draw_git1 import finger_side
OUT = os.path.join(os.path.dirname(__file__), "svg")
TESTIS, TESTIS_S = "#f3d6cf", "#dfb3a8"
EPI, EPI_S = "#e7b9a1", "#cf987d"
CORD, CORD_S = "#efc9b6", "#d6a68f"
SAC = "#f6dccb"
FLUID = "#cfe8f7"


def scrotal_diagram(hydrocele=False, x=0, y=0, sc=1.0):
    """Side view (lateral) of right hemiscrotum contents: cord, testis, epididymis (posterior = right)."""
    fn = affine(x, y, sc)
    T = lambda d: tpath(d, fn)
    out = []
    sac = smooth([(300, 250), (250, 280), (214, 360), (212, 460), (240, 540), (300, 580), (380, 570), (430, 520), (446, 440),
                  (436, 350), (400, 280), (350, 250)], t=.5)
    out.append(part(T(sac), SAC, [T(smooth([(420, 300), (446, 440), (430, 520), (380, 570), (400, 500), (414, 420)], t=.4))], [], [], [], [], sw=2.4))
    # spermatic cord with vas deferens
    cord = smooth([(290, 0, 'c'), (346, 0, 'c'), (352, 120), (360, 230), (372, 320), (330, 330), (316, 230), (300, 120)], t=.4)
    out.append(part(T(cord), CORD, [T(smooth([(330, 0), (346, 0), (352, 120), (360, 230), (372, 320), (354, 322), (340, 230), (334, 120)], t=.4))], [],
                    [], [T("M 334 10 C 338 120 346 230 356 320"), T("M 304 30 C 310 100 312 170 318 240")], [], sw=2.4, shade_fill=CORD_S))
    if hydrocele:
        tv = smooth([(320, 300), (262, 330), (236, 400), (240, 480), (280, 540), (340, 556), (396, 530), (420, 460), (414, 380), (380, 316)], t=.5)
        out.append(part(T(tv), FLUID, [], [T(smooth([(270, 360), (300, 330), (290, 380), (262, 420)], t=.4))], [], [], [], sw=2.4, light_fill="#ffffff"))
    testis = smooth([(318, 352), (282, 372), (266, 420), (272, 474), (304, 508), (344, 512), (376, 486), (388, 436), (378, 388), (352, 356)], t=.5)
    out.append(part(T(testis), TESTIS, [T(smooth([(378, 388), (388, 436), (376, 486), (344, 512), (360, 470), (368, 420)], t=.4))],
                    [T(smooth([(292, 390), (312, 372), (300, 410), (286, 440)], t=.4))], [], [T("M 300 400 C 320 420 330 450 332 480")], [], sw=2.4,
                    shade_fill=TESTIS_S, light_fill="#fff0ec"))
    epi = smooth([(356, 330), (384, 328), (404, 350), (406, 382), (396, 430), (392, 480), (378, 520), (352, 532), (344, 520), (366, 492),
                  (378, 440), (384, 392), (376, 362), (352, 352)], t=.5)
    out.append(part(T(epi), EPI, [T(smooth([(396, 430), (392, 480), (378, 520), (370, 500), (382, 450)], t=.4))], [], [], [], [], sw=2.4, shade_fill=EPI_S))
    return "\n".join(out)


def scrotum_map():
    return svg(560, 620, scrotal_diagram(), x0=60, y0=-20)


def testis_palp():
    b = scrotal_diagram()
    # thumb in front, index + middle behind (side views of gloved fingers)
    b += finger_side(140, 440, 0, 1.4, glove=True)
    b += finger_side(560, 414, 180, 1.3, glove=True, flip=True)
    b += finger_side(560, 470, 180, 1.3, glove=True, flip=True)
    return svg(760, 600, b, x0=20, y0=10)


def get_above():
    b = scrotal_diagram(hydrocele=True)
    b += finger_side(120, 180, 0, 1.3, glove=True)
    b += finger_side(560, 180, 180, 1.3, glove=True, flip=True)
    b += lines(["M 250 230 L 440 230"], 3, "#167a8b").replace('opacity="1"', 'opacity="1" stroke-dasharray="10 7"')
    return svg(760, 620, b, x0=20, y0=-20)


def transillum():
    b = '<defs><radialGradient id="glow" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#fff6c2" stop-opacity=".95"/>' \
        '<stop offset=".6" stop-color="#ffe680" stop-opacity=".55"/><stop offset="1" stop-color="#ffe680" stop-opacity="0"/></radialGradient></defs>'
    b += scrotal_diagram(hydrocele=True)
    b += '<path d="M 236 340 C 300 300 400 330 424 420 C 440 500 380 560 300 552 C 240 540 214 470 236 340 Z" fill="url(#glow)"/>'
    # pen torch from the side
    torch = "M 470 410 L 640 380 L 648 420 L 478 452 Z"
    b += part(torch, "#5d6773", ["M 474 440 L 646 410 L 648 420 L 478 452 Z"], ["M 480 418 L 620 393 L 621 398 L 481 423 Z"], [], [], [], shade_fill="#3e4650", light_fill="#9aa4ae")
    b += part("M 452 402 L 474 398 L 482 456 L 460 460 Z", "#b9c2cb", [], [], [], [], [])
    b += '<path d="M 452 404 L 380 380 L 390 470 L 460 458 Z" fill="#fff2a8" opacity=".55"/>'
    return svg(760, 600, b, x0=60, y0=-10)


# ------------------------------------------------------------------ ulcer edges (cross-sections)
def skin_block(x, y, w=200, h=120, kind="sloping"):
    """Skin cross-section with an ulcer; epidermis line, dermis, subcutis. kind = edge type."""
    top = y
    ul, ur = x + w * .3, x + w * .7          # ulcer mouth
    fl = y + 54                               # floor depth
    if kind == "sloping":
        surf = [(x, top), (ul - 20, top), (ul + 18, fl - 6), (ur - 18, fl - 6), (ur + 20, top), (x + w, top)]
    elif kind == "punched":
        surf = [(x, top), (ul, top, 'c'), (ul + 2, fl, 'c'), (ur - 2, fl, 'c'), (ur, top, 'c'), (x + w, top)]
    elif kind == "undermined":
        surf = [(x, top), (ul + 16, top, 'c'), (ul + 10, top + 8), (ul - 14, top + 26), (ul - 6, fl), (ur + 6, fl), (ur + 14, top + 26),
                (ur - 10, top + 8), (ur - 16, top, 'c'), (x + w, top)]
    elif kind == "rolled":
        surf = [(x, top), (ul - 30, top), (ul - 14, top - 16), (ul + 6, top - 8), (ul + 10, fl - 20), (ur - 10, fl - 20), (ur - 6, top - 8),
                (ur + 14, top - 16), (ur + 30, top), (x + w, top)]
    elif kind == "everted":
        surf = [(x, top), (ul - 30, top), (ul - 16, top - 22), (ul + 12, top - 30), (ul + 8, top - 10), (ul + 12, fl - 10), (ur - 12, fl - 10),
                (ur - 8, top - 10), (ur - 12, top - 30), (ur + 16, top - 22), (ur + 30, top), (x + w, top)]
    else:  # floor: granulation
        surf = [(x, top), (ul - 20, top), (ul + 8, fl - 14), (ur - 8, fl - 14), (ur + 20, top), (x + w, top)]
    d = smooth(surf + [(x + w, top + h, 'c'), (x, top + h, 'c')], t=.4).replace("Z", "") + " Z"
    dermis_line = f"M {x} {top + 44} C {x + w * .3} {top + 52} {x + w * .7} {top + 52} {x + w} {top + 44}"
    out = part(d, "#f2c9a7", [f"M {x} {top + 46} C {x + w * .3} {top + 54} {x + w * .7} {top + 54} {x + w} {top + 46} L {x + w} {top + h} L {x} {top + h} Z"], [],
               [], [dermis_line, f"M {x} {top + 6} L {ul - 22} {top + 6}", f"M {ur + 22} {top + 6} L {x + w} {top + 6}"], [], sw=2.4, shade_fill="#f7e2a8")
    # ulcer floor colour
    if kind in ("sloping", "floor"):
        out += blob(f"M {ul + 14} {fl - 4} C {ul + 30} {fl + 6} {ur - 30} {fl + 6} {ur - 14} {fl - 4} Z", "#d9534f", .8)
    elif kind == "punched":
        out += blob(f"M {ul + 4} {fl - 1} L {ur - 4} {fl - 1} L {ur - 4} {fl + 4} L {ul + 4} {fl + 4} Z", "#b9837a", .9)
    else:
        out += blob(f"M {ul + 2} {fl - 2} C {ul + 30} {fl + 6} {ur - 30} {fl + 6} {ur - 2} {fl - 2} Z", "#c9746b", .8)
    return out


def ulcer_map():
    kinds = ["sloping", "punched", "undermined", "rolled", "everted", "floor"]
    b = []
    for i, k in enumerate(kinds):
        x, y = 30 + (i % 3) * 250, 110 + (i // 3) * 240
        b.append(skin_block(x, y, 210, 120, k))
    return svg(800, 520, "\n".join(b), y0=10)


ALL = dict(uro_scrotum_map=scrotum_map, uro_testis_palp=testis_palp, uro_get_above=get_above, uro_transillum=transillum,
           lump_ulcer_map=ulcer_map)
if __name__ == "__main__":
    for k in (sys.argv[1:] or ALL):
        save(k, ALL[k](), OUT)
