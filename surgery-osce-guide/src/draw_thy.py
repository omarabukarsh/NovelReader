"""Topic 2 (thyroid / neck) + topic 3 face & neck illustrations."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from art import *
from draw_head import bust, head, neck_torso, gown_front, OUT


def glass(x, y, w=56, h=86):
    d = f"M {x - w/2} {y - h/2} L {x + w/2} {y - h/2} L {x + w/2 - 7} {y + h/2} C {x + 10} {y + h/2 + 4} {x - 10} {y + h/2 + 4} {x - w/2 + 7} {y + h/2} Z"
    water = f"M {x - w/2 + 3} {y - h/6} L {x + w/2 - 3} {y - h/6} L {x + w/2 - 7} {y + h/2} C {x + 10} {y + h/2 + 4} {x - 10} {y + h/2 + 4} {x - w/2 + 7} {y + h/2} Z"
    return part(d, "#eef7fc", [water], [f"M {x - w/2 + 8} {y - h/2 + 6} L {x - w/2 + 12} {y + h/2 - 8} L {x - w/2 + 18} {y + h/2 - 8} L {x - w/2 + 14} {y - h/2 + 6} Z"],
                [], [], [], sw=2.2, shade_fill="#bfe0f3", light_fill="#ffffff")


FRONT_CLIP = "M 238 296 L 362 296 L 368 420 L 392 446 L 400 476 L 200 476 L 208 446 L 232 420 Z"


def wrap_hands(specs):
    """Hands of an examiner standing BEHIND the patient: whole hand drawn behind the neck,
    fingers redrawn in front, clipped to the anterior neck."""
    behind, front = "", ""
    for target, ang, left in specs:
        behind += hand_at("tips", target, ang, .86, what="mid4", left=left, thumb=False, arm="coat", arm_len=260)
        front += hand_at("tips", target, ang, .86, what="mid4", left=left, thumb=False, arm="none")
    cid = uid()
    front = f'<clipPath id="{cid}"><path d="{FRONT_CLIP}"/></clipPath><g clip-path="url(#{cid})">{front}</g>'
    return behind, front


def neck_map():
    return svg(400, 380, bust(), x0=100, y0=220)


def swallow():
    b = bust()
    b += arrow("M 372 452 L 372 392", "#167a8b", 5) + arrow("M 228 452 L 228 392", "#167a8b", 5)
    return svg(600, 640, b)


def tongue():
    b = bust(mouth="tongue", goitre=False, cyst=True)
    b += arrow("M 336 372 L 336 326", "#167a8b", 5)
    return svg(600, 640, b)


def palpation(nodes=False):
    if not nodes:
        be, fr = wrap_hands([((282, 424), 28, False), ((318, 424), 152, True)])
        b = bust(extra_before=be, extra_after=fr)
    else:
        be, fr = wrap_hands([((256, 328), 24, False)])
        b = bust(extra_before=be, extra_after=fr)
        route = "M 300 334 C 318 336 338 330 352 316 C 372 300 396 262 404 224 C 412 236 416 252 414 268 C 404 300 380 330 366 360 C 356 390 346 420 336 452 C 356 444 380 438 404 436 C 396 450 380 462 360 470"
        b += f'<path d="{route}" fill="none" stroke="#167a8b" stroke-width="4" stroke-dasharray="2 9" stroke-linecap="round"/>'
        b += arrow("M 372 466 L 356 472", "#167a8b", 4)
    return svg(600, 640, b)


def trachea():
    b = bust()
    b += hand_at("point", (300, 470), -112, .95, what="index", arm_len=260)
    return svg(600, 640, b)


def virchow():
    be, fr = wrap_hands([((370, 458), 150, True)])
    b = bust(goitre=False, extra_before=be, extra_after=fr)
    return svg(600, 640, b)


def lidlag():
    b = neck_torso(False) + gown_front() + head(eyes="lidlag")
    b += hand_at("point", (500, 70), -95, .8, what="index", left=True, arm_len=300)
    b += arrow("M 548 60 L 548 170", "#167a8b", 5)
    return svg(600, 400, b, y0=10)


def eyes_pallor():
    pink = "M 238 196 C 248 210 268 210 278 196 C 268 204 248 204 238 196 Z"
    b = neck_torso(False) + gown_front() + head(eyes="up")
    b += blob("M 236 194 C 248 214 268 214 280 194 C 268 206 248 206 236 194 Z", "#f2d7d0") + lines(["M 236 196 C 248 214 268 214 280 196"], 1.6, INK)
    b += hand_at("point", (256, 214), -62, .85, what="index", left=True, arm_len=300)
    return svg(600, 400, b, y0=40)


def tremor():
    b = []
    for x, left in ((175, True), (425, False)):
        b.append(hand_svg("spread", x, 600, -90, 1.25, left=left, glove=False, arm="skin", arm_len=200))
        b.append(part(f"M {x - 62} 660 L {x + 62} 660 L {x + 66} 730 L {x - 66} 730 Z", GOWN, [], [], [f"M {x - 54} 676 C {x - 20} 684 {x + 20} 684 {x + 54} 676"], [], []))
    paper = "M 96 452 L 504 440 L 508 560 L 100 572 Z"
    b.append(part(paper, "#fdfdfb", ["M 100 550 L 508 540 L 508 560 L 100 572 Z"], [], [], ["M 130 480 L 470 470", "M 130 510 L 470 500"], [], sw=2.2, shade_fill="#e6e8ea"))
    for x, y in ((84, 466), (518, 452), (86, 560), (520, 548)):
        b.append(lines([f"M {x} {y - 10} q 6 5 0 10 q -6 5 0 10"], 2.4, "#167a8b"))
    return svg(600, 560, "\n".join(b), y0=180)


ALL = dict(thy_neck_map=neck_map, thy_swallow=swallow, thy_tongue=tongue, thy_palpation=palpation,
           thy_nodes=lambda: palpation(True), thy_trachea=trachea, thy_tremor=tremor, thy_lidlag=lidlag,
           git1_eyes=eyes_pallor, git1_virchow=virchow)

if __name__ == "__main__":
    for k in (sys.argv[1:] or ALL):
        save(k, ALL[k](), OUT)
