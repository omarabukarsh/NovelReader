"""Topic 1 illustrations (peripheral vascular)."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from art import *

OUT = os.path.join(os.path.dirname(__file__), "svg")

# ---------------------------------------------------------------- right foot, dorsal view, toes up
RFOOT = """M 336 600 C 334 572 327 549 322 530 C 317 512 313 500 313 486
C 311 448 303 404 299 360 C 296 330 294 302 295 278 C 295 252 293 230 296 210
C 299 190 309 178 321 178 C 335 178 343 190 345 206 C 346 214 346 220 346 225
C 348 212 349 197 352 189 C 356 179 368 177 373 187 C 376 195 377 211 377 227
C 379 213 381 201 385 196 C 390 189 400 191 403 201 C 405 211 405 222 405 233
C 407 223 409 215 413 211 C 418 206 426 208 429 217 C 431 225 431 234 431 242
C 433 235 436 229 441 228 C 448 227 452 235 453 245 C 455 259 456 273 457 289
C 461 331 460 381 456 431 C 453 463 448 487 449 505 C 450 517 456 527 453 541
C 449 557 440 569 436 600 Z"""

RFOOT_SHADE = [
    # lateral side in shadow (light from upper-left)
    "M 440 600 C 446 560 452 530 446 505 C 440 470 446 420 448 360 C 449 320 446 290 440 262 L 470 240 L 470 600 Z",
    # little web shadows at toe clefts
    "M 340 226 C 344 236 350 240 356 238 C 352 232 348 228 346 224 Z",
    "M 372 228 C 376 238 382 242 388 240 C 384 234 380 230 377 227 Z",
    "M 400 234 C 404 242 410 246 416 244 C 412 238 408 234 405 233 Z",
    "M 426 242 C 430 249 436 252 441 250 C 437 245 434 242 431 242 Z",
    # shadow below the medial malleolus and on the lateral ankle
    "M 312 500 C 322 508 334 512 346 510 C 338 520 326 524 316 520 Z",
    "M 452 500 C 440 512 430 522 432 540 C 440 530 448 520 456 512 Z",
    # toe side shades
    "M 336 190 C 344 196 345 214 346 226 L 336 226 C 340 214 340 200 336 190 Z",
    "M 368 186 C 375 196 377 214 377 228 L 369 228 C 372 214 372 198 368 186 Z",
    "M 398 196 C 404 206 405 220 405 234 L 398 234 C 400 222 400 206 398 196 Z",
    "M 424 210 C 430 218 431 230 431 242 L 425 242 C 427 232 427 220 424 210 Z",
    "M 448 232 C 453 240 455 258 457 288 L 450 288 C 450 266 450 248 448 232 Z",
]
RFOOT_LIGHT = [
    # extensor hallucis longus tendon ridge highlight
    "M 352 560 C 348 500 336 420 326 330 C 324 312 322 296 320 282 L 328 282 C 332 300 334 316 336 334 C 346 420 358 500 362 560 Z",
    # medial dorsum highlight
    "M 314 470 C 310 420 304 380 302 340 C 312 380 318 430 322 470 Z",
]
RFOOT_LINES = [
    # big-toe interphalangeal crease and nail
    "M 304 236 C 312 240 326 240 338 236",
    "M 309 200 C 309 190 315 185 321 185 C 328 185 334 190 334 200 C 334 210 328 214 321 214 C 314 214 309 210 309 200 Z",
    # lesser toe nails
    "M 357 199 C 357 192 361 188 364 188 C 368 188 371 192 371 199 C 371 205 368 207 364 207 C 360 207 357 205 357 199 Z",
    "M 387 206 C 387 200 390 197 393 197 C 397 197 399 200 399 206 C 399 211 397 213 393 213 C 390 213 387 211 387 206 Z",
    "M 414 220 C 414 215 416 213 419 213 C 422 213 424 215 424 220 C 424 224 422 226 419 226 C 416 226 414 224 414 220 Z",
    "M 440 237 C 440 233 442 231 444 231 C 447 231 448 233 448 237 C 448 240 447 242 444 242 C 442 242 440 240 440 237 Z",
    # malleoli contours
    "M 316 478 C 326 482 334 494 332 506",
    "M 452 490 C 444 498 440 512 444 524",
]
RFOOT_FAINT = [
    # EHL tendon edges + metatarsal ridges + ankle crease
    "M 330 300 C 336 360 348 450 356 540",
    "M 372 290 C 376 340 380 400 382 450",
    "M 404 300 C 408 340 410 380 410 420",
    "M 428 300 C 432 340 434 370 434 400",
    # dorsal venous arch
    "M 318 330 C 350 350 400 352 446 330",
]
RFOOT_WEIGHT = ["M 457 300 C 461 350 459 400 456 431 C 453 463 448 487 449 505",
                "M 453 541 C 449 557 440 569 436 600"]

# ---------------------------------------------------------------- gloved right hand (procedural)
def dp_hand(dx=-8, dy=0):
    T = lambda p: (p[0] + dx, p[1] + dy)
    F = lambda ch, w, **k: Finger([T(p) for p in ch], w, **k)
    fingers = [
        F([(490, 352), (448, 349), (426, 351), (411, 355)], [30, 27, 24, 21]),
        F([(484, 382), (432, 380), (402, 382), (385, 386)], [33, 31, 27, 24]),
        F([(480, 414), (421, 412), (385, 412), (364, 414)], [35, 33, 29, 26]),
        F([(484, 447), (429, 444), (393, 443), (370, 445)], [34, 32, 28, 25]),
    ]
    thumb = F([(566, 466), (534, 498), (507, 524), (488, 540)], [46, 38, 33, 29], nail_side=.15)
    return hand_shape(fingers, thumb, T((612, 350)), T((616, 472)),
                      ulnar_pts=[T((566, 340)), T((528, 335))],
                      thenar_pts=[T((590, 494))], web=20)


SLEEVE = """M 596 320 C 640 300 700 276 800 252 L 800 480 C 730 492 660 498 600 498
C 612 462 616 380 596 320 Z"""
SLEEVE_SHADE = ["M 600 498 C 660 498 730 492 800 480 L 800 440 C 730 454 660 462 606 462 Z",
                "M 596 320 C 612 360 616 430 604 498 L 626 498 C 634 430 630 360 616 312 Z"]
SLEEVE_LINES = ["M 626 312 C 640 360 642 440 628 498",
                "M 680 296 C 700 326 720 336 760 330", "M 690 452 C 720 444 760 440 798 436"]
CUFF = """M 590 336 C 598 370 602 430 598 484 L 616 488 C 620 430 616 370 608 330 Z"""


def dp_pulse():
    body = []
    # couch, seen from above; foot end at top
    body.append(blob("M 0 100 L 800 100 L 800 600 L 0 600 Z", "#ffffff"))
    body.append(blob("M 0 128 L 800 128 L 800 600 L 0 600 Z", COUCH))
    body.append(blob("M 0 128 L 800 128 L 800 146 L 0 146 Z", COUCH_H))
    body.append(lines(["M 0 146 L 800 146"], 2, "#122238"))
    # left foot (mirror image) at the left, partly cut by frame
    body.append(part(RFOOT, SKIN, RFOOT_SHADE, RFOOT_LIGHT, RFOOT_LINES, RFOOT_FAINT,
                     RFOOT_WEIGHT, transform="translate(470 18) scale(-1 1)"))
    # contact shadow of right foot on couch
    body.append(blob("M 452 280 C 470 360 470 470 462 600 L 440 600 C 450 480 458 380 448 280 Z", "#0d1b2e", .45))
    # right foot
    body.append(part(RFOOT, SKIN, RFOOT_SHADE, RFOOT_LIGHT, RFOOT_LINES, RFOOT_FAINT, RFOOT_WEIGHT))
    # soft cast shadow of the hand on the foot dorsum
    body.append(blob("M 360 440 C 400 452 440 456 470 464 C 474 480 468 498 460 520 C 440 500 400 470 356 452 Z", "#a8775a", .45))
    # skin dimples where the index & middle fingertips press
    body.append(lines(["M 350 400 C 346 408 346 420 350 428", "M 356 432 C 352 440 352 452 357 460"], 1.4, INK_SOFT, .9))
    body.append(blob("M 352 404 C 348 412 349 422 354 426 L 360 420 Z", SKIN_S, .9))
    body.append(blob("M 358 436 C 354 444 355 454 360 458 L 366 452 Z", SKIN_S, .9))
    h = dp_hand()
    body.append(part(h["d"], GLOVE, h["shade"], h["light"], h["lines"], h["faint"], []))
    body.append(part(CUFF, GLOVE, [], [], [], [], []))
    body.append(part(SLEEVE, COAT, SLEEVE_SHADE, [], SLEEVE_LINES, [], ["M 600 498 C 660 498 730 492 800 480"]))
    return svg(800, 500, "\n".join(body), y0=100)


if __name__ == "__main__":
    which = sys.argv[1:] or ["dp"]
    if "dp" in which:
        print(save("pvd_dp_pulse", dp_pulse(), OUT))


# ================================================================ popliteal pulse (side view, knee flexed)
H, K, A = (-160, 430), (312, 280), (740, 455)
LEG = [H, K, A]
LEG_FRONT = [(0.0, 80), (0.3, 78), (0.55, 74), (0.78, 66), (0.9, 62), (0.97, 67), (1.03, 64),
             (1.09, 53), (1.15, 56), (1.25, 48), (1.5, 44), (1.75, 39), (1.9, 36), (1.97, 35)]
FOOT_SIDE = [(782, 402), (812, 374), (840, 348), (858, 333), (872, 330), (881, 340), (877, 354),
             (868, 374), (848, 420), (822, 468), (800, 504), (776, 521), (752, 514), (738, 494)]
LEG_BACK = [(1.96, 30), (1.85, 32), (1.7, 42), (1.55, 58), (1.42, 69), (1.3, 72), (1.18, 63),
            (1.08, 50), (1.0, 46), (0.92, 52), (0.8, 66), (0.6, 78), (0.3, 84), (0.0, 86)]


def flexed_leg():
    front = profile(LEG, LEG_FRONT, +1)
    back = profile(LEG, LEG_BACK, -1)
    d = smooth(front + FOOT_SIDE + back + [(-240, 520), (-240, 300)], t=.5)
    shade = [
        # underside of thigh, calf, foot (light from upper-left)
        smooth(profile(LEG, [(0, 86), (0.4, 82), (0.8, 66), (0.95, 50), (1.1, 52), (1.3, 74), (1.6, 56), (1.95, 31)], -1)
               + profile(LEG, [(1.95, 12), (1.6, 26), (1.3, 40), (1.1, 26), (0.95, 22), (0.8, 30), (0.4, 44), (0, 50)], -1), t=.4),
        smooth([(868, 374), (848, 420), (822, 468), (800, 504), (776, 521), (800, 470), (830, 420), (850, 380)], t=.4),
        # below patella / beside tibial tuberosity
        smooth(profile(LEG, [(1.06, 40), (1.12, 30), (1.2, 22), (1.12, 10)], +1), t=.4),
    ]
    light = [
        smooth(profile(LEG, [(0.2, 72), (0.6, 68), (0.9, 56), (0.98, 60), (1.2, 42), (1.6, 36), (1.9, 30),
                             (1.9, 22), (1.6, 26), (1.2, 32), (0.98, 48), (0.9, 44), (0.6, 56), (0.2, 60)], +1), t=.4),
    ]
    lines_ = [
        # lateral malleolus
        "M 726 462 C 734 450 750 448 758 458 C 762 468 756 478 746 480",
        # toes seen from the lateral side: little toe + 4th toe tips, nail
        "M 842 352 C 848 344 856 342 862 346 C 866 352 864 360 858 364",
        "M 856 338 C 862 332 870 332 874 338",
        "M 866 334 C 870 330 876 331 878 336",
    ]
    faint = [
        # patella outline, fibular head, tibial crest, calf (gastrocnemius) line
        smooth([(296, 226), (318, 212), (340, 218), (344, 236), (330, 250), (306, 248)], closed=True),
        "M 360 318 C 368 310 380 312 384 322",
        "M 420 280 C 500 318 600 360 712 410",
        "M 380 360 C 420 380 470 400 520 420",
        "M 800 386 C 820 400 836 420 846 440",
        "M 848 356 C 852 352 856 352 858 356",
        "M 790 420 C 800 440 806 470 800 500",
    ]
    weight = [smooth(back[:9], closed=False), smooth(FOOT_SIDE[6:13], closed=False)]
    return part(d, SKIN, shade, light, lines_, faint, weight)


def far_leg():
    ch = [(-160, 468), (330, 474), (700, 478)]
    front = profile(ch, [(0, 54), (0.5, 52), (0.95, 46), (1.05, 44), (1.4, 36), (1.8, 30), (1.97, 28)], +1)
    foot = [(740, 440), (760, 420), (772, 402), (780, 398), (786, 408), (784, 430), (776, 470), (768, 508), (748, 521), (720, 518)]
    back = [(700, 520), (300, 521), (-200, 521)]
    d = smooth(front + foot + back + [(-240, 520), (-240, 420)], t=.5)
    shade = [smooth([(-200, 500), (700, 506), (740, 500), (780, 440), (786, 420), (790, 470), (760, 521), (-200, 521)], t=.3)]
    return part(d, "#e8bb98", shade, [], [], [], [], shade_fill="#cf9a78")


def gown_thigh():
    a = profile(LEG, [(0.0, 92), (0.3, 90), (0.62, 85)], +1)
    hem = profile(LEG, [(0.64, 60), (0.66, 20), (0.65, -20), (0.63, -60)], +1)
    b = profile(LEG, [(0.62, -93), (0.4, -96)], +1)
    d = smooth(a + [(*hem[0], ), *hem[1:]] + b + [(80, 521), (-240, 521), (-240, 300)], t=.45)
    shade = [smooth(profile(LEG, [(0.0, -60), (0.6, -60), (0.62, -95), (0.4, -98), (0, -98)], +1) + [(80, 521), (-240, 521)], t=.4)]
    folds = ["M 60 380 C 100 372 140 360 180 352", "M 40 420 C 90 430 130 440 160 470",
             "M 150 340 C 170 360 180 380 182 400", "M 0 470 C 40 480 70 500 90 520"]
    return part(d, GOWN, shade, [], folds, [], [])


def pop_hand(dx=0, dy=0, far=False):
    T = lambda p: (p[0] + dx, p[1] + dy)
    F = lambda ch, w, **k: Finger([T(p) for p in ch], w, **k)
    fingers = [
        F([(268, 240), (262, 278), (262, 302), (266, 320)], [26, 24, 21, 19]),
        F([(292, 236), (288, 280), (290, 308), (294, 328)], [29, 27, 24, 21]),
        F([(318, 234), (316, 282), (319, 312), (323, 332)], [31, 29, 26, 23]),
        F([(344, 236), (346, 278), (350, 304), (353, 322)], [30, 28, 25, 22]),
    ]
    if far:
        thumb = F([(350, 210), (372, 220), (388, 232), (398, 244)], [38, 29, 25, 22], nail_side=-.25)
    else:
        thumb = F([(350, 212), (378, 226), (400, 242), (414, 256)], [40, 31, 27, 24], nail_side=-.25)
    return hand_shape(fingers, thumb, T((262, 166)), T((338, 156)),
                      ulnar_pts=[T((254, 206))], thenar_pts=[T((356, 186))], web=18)


def sleeve(x1, x2, xt1, xt2, ybot, ytop=-10, cuff=True):
    d = smooth([(x1, ybot + 8), (xt1, ytop), (xt2, ytop), (x2, ybot - 4)], t=.2)
    d = f"M {x1} {ybot + 8} C {x1 - 6} {ybot - 60} {xt1 + 8} {ytop + 60} {xt1} {ytop} L {xt2} {ytop} C {xt2 - 4} {ytop + 60} {x2 + 6} {ybot - 60} {x2} {ybot - 4} C {x2 - 20} {ybot + 10} {x1 + 20} {ybot + 16} {x1} {ybot + 8} Z"
    shade = [f"M {x2} {ybot - 4} C {x2 + 6} {ybot - 60} {xt2 - 4} {ytop + 60} {xt2} {ytop} L {xt2 - 28} {ytop} C {xt2 - 30} {ytop + 60} {x2 - 18} {ybot - 60} {x2 - 22} {ybot} Z"]
    ln = [f"M {x1 + 4} {ybot - 14} C {x1 + 30} {ybot - 6} {x2 - 30} {ybot - 12} {x2 - 2} {ybot - 22}",
          f"M {(x1 + xt1) / 2 + 10} {(ybot + ytop) / 2} C {(x1 + x2) / 2} {(ybot + ytop) / 2 + 14} {(x2 + xt2) / 2 - 20} {(ybot + ytop) / 2 - 4} {(x2 + xt2) / 2 - 10} {(ybot + ytop) / 2 - 16}"]
    return part(d, COAT, shade, [], ln, [], [])


def popliteal():
    body = []
    # couch side view
    body.append(blob("M -10 520 L 910 520 L 910 600 L -10 600 Z", COUCH))
    body.append(blob("M -10 520 L 910 520 L 910 532 L -10 532 Z", COUCH_H))
    body.append(lines(["M -10 520 L 910 520", "M -10 586 L 910 586"], 2.4, INK))
    body.append(far_leg())
    # far hand (behind the knee): only its back/thumb show above the knee
    fh = pop_hand(36, -6, far=True)
    body.append(part(fh["d"], GLOVE, fh["shade"], fh["light"], fh["lines"], fh["faint"], [], shade_fill="#86b6d8"))
    body.append(sleeve(298, 372, 330, 430, 166))
    body.append(flexed_leg())
    body.append(gown_thigh())
    # cast shadow of near hand on lateral knee
    body.append(blob("M 356 230 C 372 262 366 300 356 330 L 340 330 C 350 300 352 262 346 236 Z", SKIN_S, .8))
    h = pop_hand()
    body.append(part(h["d"], GLOVE, h["shade"], h["light"], h["lines"], h["faint"], []))
    body.append(sleeve(256, 340, 180, 300, 174))
    return svg(900, 600, "\n".join(body))


if __name__ == "__main__" and "pop" in sys.argv:
    print(save("pvd_popliteal_pulse", popliteal(), OUT))


# ================================================================ lower-limb inspection map (from above, head at top)
RL = [(186, -40), (214, 380), (204, 700)]
MED = [(0.0, 70), (0.25, 68), (0.5, 60), (0.72, 52), (0.84, 56), (0.92, 50), (1.0, 45), (1.08, 43),
       (1.18, 54), (1.28, 58), (1.4, 52), (1.6, 40), (1.75, 32), (1.84, 29)]
LAT = [(0.0, 78), (0.25, 76), (0.5, 66), (0.72, 56), (0.88, 48), (1.0, 49), (1.06, 46), (1.12, 48),
       (1.25, 52), (1.4, 48), (1.6, 38), (1.75, 31), (1.84, 29)]
# right foot from image 1 (dorsal view) rotated 180 deg so the toes point down
FOOT_T = affine(204, 700, .62, 180, 386, 520, sy=.47)


def leg_from_above():
    med = profile(RL, MED, +1)
    lat = profile(RL, LAT, -1)
    foot = tpath(RFOOT, FOOT_T)            # starts at the medial shank, ends at lateral shank
    foot_body = foot[2:].rsplit(" Z", 1)[0]   # drop leading "M"
    d = (smooth(med, closed=False) + " L " + foot_body + " L " +
         smooth(lat[::-1], closed=False)[2:] + " Z")
    shade = [
        smooth(profile(RL, [(0, 78), (0.5, 66), (0.88, 48), (1.1, 47), (1.3, 52), (1.6, 38), (1.85, 30)], -1)
               + profile(RL, [(1.85, 14), (1.6, 18), (1.3, 28), (1.1, 26), (0.88, 26), (0.5, 40), (0, 50)], -1), t=.4),
        # hollow beside the patellar tendon and below vastus medialis
        smooth(profile(RL, [(1.02, 30), (1.08, 30), (1.14, 18), (1.08, 14)], +1), t=.5),
        smooth(profile(RL, [(0.9, 44), (0.96, 38), (1.0, 30), (0.95, 30)], +1), t=.5),
    ] + [tpath(x, FOOT_T) for x in RFOOT_SHADE]
    light = [
        smooth(profile(RL, [(0.1, 46), (0.5, 40), (0.84, 38), (1.0, 20), (1.2, 34), (1.6, 22), (1.84, 14),
                            (1.84, 2), (1.6, 6), (1.2, 12), (1.0, 6), (0.84, 14), (0.5, 16), (0.1, 18)], +1), t=.4),
    ] + [tpath(x, FOOT_T) for x in RFOOT_LIGHT]
    lines_ = [tpath(x, FOOT_T) for x in RFOOT_LINES]
    faint = [
        # patella (soft), tibial tuberosity + crest, vastus medialis line
        smooth(profile(RL, [(0.93, 4), (0.95, 22), (1.0, 25), (1.04, 14), (1.045, -6), (1.03, -22), (0.98, -26), (0.94, -18)], +1)),
        smooth(profile(RL, [(1.12, -4), (1.4, 6), (1.7, 8), (1.82, 6)], +1), closed=False),
        smooth(profile(RL, [(0.76, 48), (0.86, 34), (0.93, 28)], +1), closed=False),
    ] + [tpath(x, FOOT_T) for x in RFOOT_FAINT]
    weight = [smooth(lat[::-1][:10], closed=False)]
    return part(d, SKIN, shade, light, lines_, faint, weight)


def gown_top():
    d = ("M -10 -10 L 610 -10 L 610 130 C 580 144 540 152 500 156 C 470 172 440 178 410 170 "
         "C 370 188 330 182 300 164 C 270 182 230 188 192 174 C 160 182 120 176 96 158 "
         "C 60 156 20 146 -10 132 Z")
    shade = ["M -10 100 C 60 120 140 128 200 124 C 260 134 340 134 400 124 C 460 128 540 120 610 100 L 610 200 L -10 200 Z",
             "M 290 0 C 300 60 304 120 300 164 L 312 164 C 316 120 312 60 302 0 Z"]
    folds = ["M 300 156 C 300 110 296 60 288 10", "M 150 160 C 160 120 170 70 176 20",
             "M 450 160 C 440 120 430 70 424 20", "M 60 140 C 70 110 76 70 70 30",
             "M 540 140 C 530 110 526 70 532 30"]
    return part(d, GOWN, shade, [], folds, [], ["M 96 158 C 120 176 160 182 192 174 C 230 188 270 182 300 164 C 330 182 370 188 410 170 C 440 178 470 172 500 156"])


def inspection_map():
    body = []
    body.append(blob("M 34 -10 L 566 -10 L 566 910 L 34 910 Z", COUCH))
    body.append(blob("M 34 -10 L 54 -10 L 54 910 L 34 910 Z", COUCH_H))
    body.append(lines(["M 34 -10 L 34 910", "M 566 -10 L 566 910"], 2.4, INK))
    # contact shadows on the couch
    body.append(blob("M 108 160 C 100 420 128 700 140 880 L 262 880 C 274 700 292 420 292 160 Z", "#0d1b2e", .5))
    body.append(blob("M 492 160 C 500 420 472 700 460 880 L 338 880 C 326 700 308 420 308 160 Z", "#0d1b2e", .5))
    body.append(leg_from_above())
    body.append(f'<g transform="translate(600 0) scale(-1 1)">{leg_from_above()}</g>')
    body.append(gown_top())
    return svg(600, 900, "\n".join(body))


if __name__ == "__main__" and "map" in sys.argv:
    print(save("pvd_inspection_map", inspection_map(), OUT))
