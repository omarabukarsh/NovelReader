"""Front view of a seated patient: head, neck, shoulders (topics 2 and 3)."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from art import *

OUT = os.path.join(os.path.dirname(__file__), "svg")
HAIR, HAIR_S = "#5b3a26", "#432a1b"
LIP = "#d98f7f"


def mirror_pts(pts, cx=300):
    return [(2 * cx - p[0], p[1], *p[2:]) for p in pts]


HEAD_L = [(262, 333), (234, 312), (216, 282), (209, 260), (198, 257), (188, 238), (184, 208), (191, 184),
          (205, 182, 'c'), (207, 150), (212, 104), (240, 58)]
HEAD = [(300, 341)] + HEAD_L + [(300, 40)] + mirror_pts(HEAD_L)[::-1]
NECK_L = [(244, 292), (238, 340), (233, 382), (220, 408), (182, 430), (122, 450), (82, 474), (62, 520), (56, 700)]
NECK = NECK_L + mirror_pts(NECK_L)[::-1]


def neck_torso(goitre=True, cyst=False):
    d = smooth(NECK, t=.5)
    shade = [smooth([(248, 292), (244, 340), (240, 382), (262, 386), (270, 340), (300, 330), (330, 340), (338, 386),
                     (360, 382), (356, 340), (352, 292), (300, 300)], t=.4),
             smooth([(82, 474), (62, 520), (56, 700), (90, 700), (92, 540), (110, 490)], t=.4),
             smooth([(518, 474), (538, 520), (544, 700), (510, 700), (508, 540), (490, 490)], t=.4)]
    light = [smooth([(276, 404), (286, 398), (292, 420), (284, 440), (276, 430)], t=.5),
             smooth([(324, 404), (314, 398), (308, 420), (316, 440), (324, 430)], t=.5)] if goitre else []
    faint = ["M 240 306 C 252 360 272 430 288 470", "M 360 306 C 348 360 328 430 312 470",
             "M 286 478 C 240 468 170 464 104 474", "M 314 478 C 360 468 430 464 496 474",
             "M 292 474 C 296 480 304 480 308 474",
             "M 288 360 C 294 370 306 370 312 360", "M 292 372 C 296 380 304 380 308 372",
             "M 140 520 C 170 540 200 548 230 550", "M 460 520 C 430 540 400 548 370 550"]
    lines_ = []
    if goitre:
        faint += ["M 268 400 C 262 420 268 446 290 452 C 296 444 304 444 310 452 C 332 446 338 420 332 400"]
        shade.append(smooth([(270, 444), (290, 456), (300, 450), (310, 456), (330, 444), (326, 462), (300, 468), (274, 462)], t=.4))
    if cyst:
        lines_ += ["M 288 346 C 290 334 310 334 312 346 C 310 356 290 356 288 346 Z"]
        light.append("M 291 342 C 296 336 304 336 309 342 C 304 340 296 340 291 342 Z")
    return part(d, SKIN, shade, light, lines_, faint, [smooth(NECK_L[3:], closed=False), smooth(mirror_pts(NECK_L)[3:], closed=False)])


def eye(cx, cy, mode="normal", side=1):
    s = side
    up = f"M {cx - 22 * s} {cy} C {cx - 12 * s} {cy - 10} {cx + 10 * s} {cy - 10} {cx + 22 * s} {cy}"
    lo = f"M {cx - 22 * s} {cy} C {cx - 10 * s} {cy + 8} {cx + 10 * s} {cy + 8} {cx + 22 * s} {cy}"
    white = f"M {cx - 22 * s} {cy} C {cx - 12 * s} {cy - 10} {cx + 10 * s} {cy - 10} {cx + 22 * s} {cy} C {cx + 10 * s} {cy + 8} {cx - 10 * s} {cy + 8} {cx - 22 * s} {cy} Z"
    iy = {"normal": cy, "lidlag": cy + 3, "up": cy - 4, "down": cy + 3}[mode]
    if mode == "lidlag":   # upper lid retracted: sclera visible above the iris
        up = f"M {cx - 22 * s} {cy} C {cx - 12 * s} {cy - 16} {cx + 10 * s} {cy - 16} {cx + 22 * s} {cy}"
        white = f"M {cx - 22 * s} {cy} C {cx - 12 * s} {cy - 16} {cx + 10 * s} {cy - 16} {cx + 22 * s} {cy} C {cx + 10 * s} {cy + 8} {cx - 10 * s} {cy + 8} {cx - 22 * s} {cy} Z"
    iris = smooth([(cx + 7.5 * math.cos(a), iy + 7.5 * math.sin(a)) for a in [i * math.pi / 4 for i in range(8)]])
    pupil = smooth([(cx + 3.2 * math.cos(a), iy + 3.2 * math.sin(a)) for a in [i * math.pi / 4 for i in range(8)]])
    cid = uid()
    return (f'<clipPath id="{cid}"><path d="{white}"/></clipPath><path d="{white}" fill="#ffffff"/>'
            f'<g clip-path="url(#{cid})"><path d="{iris}" fill="#6b4a2f"/><path d="{pupil}" fill="#1d130c"/>'
            f'<path d="{up}" fill="none" stroke="#c9b8aa" stroke-width="5" transform="translate(0 2)"/></g>'
            + lines([up], 2.6) + lines([lo], 1.3, INK_SOFT)
            + lines([f"M {cx - 18 * s} {cy - 12 - (4 if mode == 'lidlag' else 0)} C {cx - 6 * s} {cy - 18 - (4 if mode == 'lidlag' else 0)} {cx + 8 * s} {cy - 18 - (4 if mode == 'lidlag' else 0)} {cx + 20 * s} {cy - 10 - (4 if mode == 'lidlag' else 0)}"], 1.1, INK_SOFT, .7))


def head(eyes="normal", mouth="normal", tilt=0):
    d = smooth(HEAD, t=.5)
    shade = [smooth([(300, 341), (262, 333), (234, 312), (216, 282), (209, 260), (226, 262), (244, 300), (270, 322), (300, 326)], t=.4),
             smooth([(392, 258), (384, 282), (366, 312), (338, 333), (300, 341), (300, 326), (340, 318), (368, 290), (380, 250)], t=.4),
             smooth([(392, 150), (396, 200), (392, 258), (378, 250), (384, 200), (380, 150)], t=.4),
             smooth([(232, 200), (258, 206), (282, 200), (280, 194), (258, 198), (234, 194)], t=.4)]
    light = [smooth([(250, 110), (300, 100), (350, 110), (330, 130), (300, 126), (270, 130)], t=.5),
             smooth([(296, 200), (304, 200), (306, 246), (298, 250)], t=.5)]
    ln = ["M 292 200 C 290 222 286 240 280 252", "M 278 256 C 284 263 292 263 296 258", "M 322 256 C 316 263 308 263 304 258",
          "M 286 256 C 294 268 306 268 314 256"]
    faint = ["M 196 196 C 192 212 194 228 204 242", "M 200 206 C 198 218 200 228 206 234",
             "M 404 196 C 408 212 406 228 396 242", "M 400 206 C 402 218 400 228 394 234",
             "M 270 262 C 264 276 266 288 274 298", "M 330 262 C 336 276 334 288 326 298",
             "M 288 320 C 296 324 304 324 312 320"]
    out = [part(d, SKIN, shade, light, ln, faint, [smooth(HEAD[0:5], closed=False)])]
    # eyebrows
    out.append(lines(["M 230 168 C 244 158 266 156 284 163", "M 370 168 C 356 158 334 156 316 163"], 5.5, HAIR))
    out.append(eye(258, 192, eyes, 1) + eye(342, 192, eyes, -1))
    if mouth == "tongue":
        mo = "M 276 290 C 288 284 312 284 324 290 C 320 300 280 300 276 290 Z"
        tg = "M 284 292 C 284 312 290 328 300 330 C 310 328 316 312 316 292 Z"
        out.append(blob(mo, "#5a2a24") + part(tg, "#e58c8c", ["M 300 296 L 302 296 L 302 326 L 300 326 Z"], [], ["M 300 298 C 300 308 300 316 300 322"], [], [], shade_fill="#c96f72"))
        out.append(lines(["M 274 290 C 286 280 314 280 326 290", "M 278 296 C 280 300 282 302 284 304", "M 322 296 C 320 300 318 302 316 304"], 2.2))
    else:
        out.append(part("M 272 290 C 284 284 294 286 300 288 C 306 286 316 284 328 290 C 318 302 282 302 272 290 Z", LIP,
                        ["M 272 290 C 284 284 294 286 300 288 C 306 286 316 284 328 290 C 316 292 284 292 272 290 Z"], [], [], [], [], sw=2, shade_fill="#c47667"))
        out.append(lines(["M 274 290 C 286 292 314 292 326 290"], 1.8))
    # hair
    hair = smooth([(205, 152), (212, 116), (236, 98), (270, 92, 'c'), (300, 98), (334, 92), (366, 98), (388, 116), (395, 152),
                   (404, 104), (370, 44), (300, 28), (230, 44), (196, 104)], t=.5)
    out.append(part(hair, HAIR, [smooth([(205, 152), (212, 116), (236, 98), (226, 120), (214, 150)], t=.4)], 
                    [smooth([(250, 50), (300, 40), (350, 50), (330, 60), (300, 56), (270, 60)], t=.4)],
                    ["M 250 70 C 262 80 270 88 276 96", "M 340 66 C 334 78 330 86 326 94"], [], [], shade_fill=HAIR_S, light_fill="#7a5238"))
    return "\n".join(out)


def gown_front():
    d = "M 30 540 C 120 520 220 520 300 536 C 380 520 480 520 570 540 L 580 720 L 20 720 Z"
    return part(d, GOWN, ["M 20 640 L 580 640 L 580 720 L 20 720 Z", "M 296 536 C 300 600 302 660 300 720 L 312 720 C 312 660 310 600 306 536 Z"], [],
                ["M 300 540 C 300 600 300 660 300 720", "M 150 540 C 160 600 166 650 164 720", "M 450 540 C 440 600 434 650 436 720"], [], [])


def bust(eyes="normal", mouth="normal", goitre=True, cyst=False, extra_before="", extra_after=""):
    return "\n".join([extra_before, neck_torso(goitre, cyst), gown_front(), head(eyes, mouth), extra_after])


if __name__ == "__main__":
    print(save("_bust", svg(600, 640, bust()), os.path.join(os.path.dirname(__file__), "svg_test")))
