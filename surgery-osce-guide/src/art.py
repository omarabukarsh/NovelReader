"""Tiny helper library for hand-drawn style SVG illustrations.

Every body part is ONE closed Bezier outline (path `d`).  Cel shading,
highlights and inner detail lines are clipped to that outline so they never
spill out.  Outline weight varies: a base stroke plus heavier "weight lines"
on the shadow side.
"""
import itertools, os

INK = "#4a2a17"      # dark-brown outline
INK_SOFT = "#7a4a2e"
SKIN, SKIN_S, SKIN_H = "#f2c9a7", "#dba582", "#fbe1ca"
GLOVE, GLOVE_S, GLOVE_H = "#bfe1f6", "#8dbfe1", "#e6f5fd"
COAT, COAT_S = "#ffffff", "#dbe3ea"
GOWN, GOWN_S, GOWN_H = "#a9cdea", "#7fb0d8", "#cfe5f6"
COUCH, COUCH_S, COUCH_H = "#1f3a5e", "#142844", "#2e5688"
VEIN = "#5b7fb8"

_ids = itertools.count(1)


def uid(prefix="c"):
    return f"{prefix}{next(_ids)}"


def part(d, fill, shade=(), light=(), lines=(), faint=(), weight=(), sw=3.0,
         transform=None, shade_fill=None, light_fill=None, extra=""):
    """Return SVG for one body part.

    d       : closed outline path
    shade   : list of path d's filled with the shade colour, clipped to outline
    light   : list of path d's filled with highlight colour, clipped
    lines   : inner detail lines (creases, knuckles) - medium ink
    faint   : very light detail lines (tendons, veins)
    weight  : open paths drawn heavier, on the shadow side of the outline
    """
    cid = uid()
    sf = shade_fill or _shade_for(fill)
    lf = light_fill or _light_for(fill)
    t = f' transform="{transform}"' if transform else ""
    out = [f'<g{t}>',
           f'<clipPath id="{cid}"><path d="{d}"/></clipPath>',
           f'<path d="{d}" fill="{fill}"/>',
           f'<g clip-path="url(#{cid})">']
    out += [f'<path d="{s}" fill="{sf}"/>' for s in shade]
    out += [f'<path d="{s}" fill="{lf}"/>' for s in light]
    out += [f'<path d="{s}" fill="none" stroke="{INK_SOFT}" stroke-width="1.3" '
            f'stroke-linecap="round" opacity=".75"/>' for s in faint]
    out += [f'<path d="{s}" fill="none" stroke="{INK}" stroke-width="1.7" '
            f'stroke-linecap="round" stroke-linejoin="round"/>' for s in lines]
    out.append(extra)
    out.append('</g>')
    out.append(f'<path d="{d}" fill="none" stroke="{INK}" stroke-width="{sw}" '
               f'stroke-linejoin="round" stroke-linecap="round"/>')
    out += [f'<path d="{w}" fill="none" stroke="{INK}" stroke-width="{sw + 1.8}" '
            f'stroke-linecap="round"/>' for w in weight]
    out.append('</g>')
    return "\n".join(out)


def _shade_for(fill):
    return {SKIN: SKIN_S, GLOVE: GLOVE_S, COAT: COAT_S, GOWN: GOWN_S,
            COUCH: COUCH_S}.get(fill, "#00000022")


def _light_for(fill):
    return {SKIN: SKIN_H, GLOVE: GLOVE_H, COAT: "#ffffff", GOWN: GOWN_H,
            COUCH: COUCH_H}.get(fill, "#ffffff55")


def lines(ds, w=1.7, color=INK, op=1):
    return "\n".join(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{w}" '
                     f'stroke-linecap="round" stroke-linejoin="round" opacity="{op}"/>'
                     for d in ds)


def blob(d, fill, op=1):
    return f'<path d="{d}" fill="{fill}" opacity="{op}"/>'


def svg(w, h, body, x0=0, y0=0):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x0} {y0} {w} {h}">\n'
            f'<rect x="{x0}" y="{y0}" width="{w}" height="{h}" fill="#ffffff"/>\n{body}\n</svg>\n')


def save(name, content, folder):
    os.makedirs(folder, exist_ok=True)
    p = os.path.join(folder, name + ".svg")
    with open(p, "w") as f:
        f.write(content)
    return p


# ---------------------------------------------------------------- geometry helpers
import math


def _v(a, b):
    return (b[0] - a[0], b[1] - a[1])


def _norm(v):
    l = math.hypot(*v) or 1
    return (v[0] / l, v[1] / l)


def add(a, b, k=1.0):
    return (a[0] + b[0] * k, a[1] + b[1] * k)


def lerp(a, b, t):
    return (a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t)


def smooth(pts, closed=True, t=0.5):
    """Catmull-Rom spline through pts -> SVG cubic Bezier path.
    A point may be (x, y, 'c') to mark a sharp corner (no handles)."""
    P = [(p[0], p[1]) for p in pts]
    C = [len(p) > 2 and p[2] == 'c' for p in pts]
    n = len(P)
    f = lambda v: f"{v:.1f}"
    d = f"M {f(P[0][0])} {f(P[0][1])}"
    rng = range(n) if closed else range(n - 1)
    for i in rng:
        p0 = P[(i - 1) % n] if (closed or i > 0) else P[i]
        p1, p2 = P[i], P[(i + 1) % n]
        p3 = P[(i + 2) % n] if (closed or i + 2 < n) else p2
        k1 = 0 if C[i] else t / 3 * 2
        k2 = 0 if C[(i + 1) % n] else t / 3 * 2
        c1 = (p1[0] + (p2[0] - p0[0]) * k1 / 2, p1[1] + (p2[1] - p0[1]) * k1 / 2)
        c2 = (p2[0] - (p3[0] - p1[0]) * k2 / 2, p2[1] - (p3[1] - p1[1]) * k2 / 2)
        d += f" C {f(c1[0])} {f(c1[1])} {f(c2[0])} {f(c2[1])} {f(p2[0])} {f(p2[1])}"
    return d + (" Z" if closed else "")


def offset_side(chain, widths, side):
    """Offset a centreline chain by +-half width (side = +1 / -1)."""
    out = []
    for i, p in enumerate(chain):
        a = chain[max(i - 1, 0)]
        b = chain[min(i + 1, len(chain) - 1)]
        d = _norm(_v(a, b))
        n = (-d[1] * side, d[0] * side)
        out.append(add(p, n, widths[i] / 2))
    return out


class Finger:
    """chain: [base, j1, j2, tip] projected joint centres; widths per joint."""
    def __init__(self, chain, widths, nail=True, nail_side=0.0):
        self.chain, self.widths, self.nail, self.nail_side = chain, widths, nail, nail_side

    def dirn(self):
        return _norm(_v(self.chain[-2], self.chain[-1]))


def hand_shape(fingers, thumb, wrist_u, wrist_r, ulnar_pts=(), thenar_pts=(),
               web=22, shade_side=+1, palm=False):
    """Build a hand: fingers ordered ulnar->radial (little ... index), thumb last.
    Returns dict(d=outline, shade=[...], light=[...], lines=[...], faint=[...], weight=[...])."""
    # side sign that points from each finger toward the ulnar side
    ref = _v(fingers[-1].chain[0], fingers[0].chain[0])
    pts = [wrist_u, *ulnar_pts]
    lines_, faint, shade, light, weight = [], [], [], [], []

    def side_sign(fg):
        d = fg.dirn()
        n = (-d[1], d[0])
        return 1 if n[0] * ref[0] + n[1] * ref[1] > 0 else -1

    def finger_pts(fg, start_cleft, end_cleft):
        s = side_sign(fg)
        u_side = offset_side(fg.chain[1:-1], fg.widths[1:-1], s)        # ulnar side, PIP..DIP
        r_side = offset_side(fg.chain[1:-1], fg.widths[1:-1], -s)
        tip, d = fg.chain[-1], fg.dirn()
        wt = fg.widths[-1] / 2
        n = (-d[1] * s, d[0] * s)
        cap_u = add(add(tip, d, -wt * .55), n, wt * .98)
        cap_r = add(add(tip, d, -wt * .55), n, -wt * .98)
        tip_pt = add(tip, d, wt * .25)
        seq = []
        if start_cleft: seq.append(start_cleft)
        seq += u_side + [cap_u, tip_pt, cap_r] + r_side[::-1]
        if end_cleft: seq.append(end_cleft)
        return seq, s

    clefts = []
    for i in range(len(fingers) - 1):
        a, b = fingers[i], fingers[i + 1]
        m = lerp(a.chain[0], b.chain[0], .5)
        dd = _norm(add(a.dirn(), b.dirn()))
        clefts.append((*add(m, dd, web), 'c'))
    for i, fg in enumerate(fingers):
        s = side_sign(fg)
        start = None
        if i == 0:
            d = fg.dirn(); n = (-d[1] * s, d[0] * s)
            start = add(fg.chain[0], n, fg.widths[0] / 2)
        else:
            start = clefts[i - 1]
        end = clefts[i] if i < len(fingers) - 1 else None
        seq, s = finger_pts(fg, start, end)
        pts += seq
        # creases / nails / shading for this finger
        ch, w = fg.chain, fg.widths
        d = fg.dirn()
        for j in (1, 2):
            dj = _norm(_v(ch[j - 1], ch[j + 1]))
            nj = (-dj[1], dj[0])
            a_ = add(ch[j], nj, w[j] * .32); b_ = add(ch[j], nj, -w[j] * .32)
            mid = add(ch[j], dj, w[j] * .12 * (1 if j == 1 else .6))
            lines_.append(f"M {a_[0]:.1f} {a_[1]:.1f} Q {mid[0]:.1f} {mid[1]:.1f} {b_[0]:.1f} {b_[1]:.1f}")
            if j == 1:
                a2 = add(a_, dj, -w[j] * .22); b2 = add(b_, dj, -w[j] * .22)
                m2 = add(mid, dj, -w[j] * .22)
                faint.append(f"M {lerp(a2, b2, .2)[0]:.1f} {lerp(a2, b2, .2)[1]:.1f} Q {m2[0]:.1f} {m2[1]:.1f} {lerp(a2, b2, .8)[0]:.1f} {lerp(a2, b2, .8)[1]:.1f}")
        if fg.nail:
            tip = ch[-1]; wt = w[-1] / 2; n = (-d[1], d[0])
            c = add(add(tip, d, -wt * .55), n, wt * fg.nail_side)
            nl = wt * 1.05; nw = wt * .62
            p = [add(add(c, d, nl * .5), n, nw * .9), add(c, d, nl * .62), add(add(c, d, nl * .5), n, -nw * .9),
                 (*add(add(c, d, -nl * .5), n, -nw), 'c'), (*add(add(c, d, -nl * .5), n, nw), 'c')]
            faint.append(smooth(p))
        sh = offset_side(ch[1:], [x * .98 for x in w[1:]], -s * shade_side)
        sh2 = offset_side(ch[1:], [x * .25 for x in w[1:]], -s * shade_side)
        shade.append(smooth([*sh, *sh2[::-1]], t=.3))
        hl = offset_side(ch[:-1], [x * .45 for x in w[:-1]], s * shade_side)
        hl2 = offset_side(ch[:-1], [x * .18 for x in w[:-1]], s * shade_side)
        light.append(smooth([*hl, *hl2[::-1]], t=.3))
        # tendon to wrist
        wm = lerp(wrist_u, wrist_r, (i + .5) / len(fingers))
        faint.append(f"M {ch[0][0]:.1f} {ch[0][1]:.1f} Q {lerp(ch[0], wm, .5)[0]:.1f} {lerp(ch[0], wm, .5)[1]:.1f} {lerp(ch[0], wm, .8)[0]:.1f} {lerp(ch[0], wm, .8)[1]:.1f}")
    # thumb
    last = fingers[-1]
    s = side_sign(last)
    d = last.dirn(); n = (-d[1] * s, d[0] * s)
    web_pt = (*add(add(last.chain[0], n, -last.widths[0] * .5), d, web * .5), 'c')
    pts.append(web_pt)
    if thumb is not None:
        tch, tw = thumb.chain, thumb.widths
        td = thumb.dirn()
        ts = 1 if ((-td[1]) * (web_pt[0] - tch[0][0]) + td[0] * (web_pt[1] - tch[0][1])) > 0 else -1
        inner = offset_side(tch[1:-1], tw[1:-1], ts)
        outer = offset_side(tch[1:-1], tw[1:-1], -ts)
        tip = tch[-1]; wt = tw[-1] / 2; tn = (-td[1] * ts, td[0] * ts)
        pts += inner + [add(add(tip, td, -wt * .5), tn, wt * .98), add(tip, td, wt * .25),
                        add(add(tip, td, -wt * .5), tn, -wt * .98)] + outer[::-1]
        j = 2 if len(tch) > 3 else 1
        dj = _norm(_v(tch[j - 1], tch[j + 1])); nj = (-dj[1], dj[0])
        a_ = add(tch[j], nj, tw[j] * .3); b_ = add(tch[j], nj, -tw[j] * .3)
        lines_.append(f"M {a_[0]:.1f} {a_[1]:.1f} Q {add(tch[j], dj, 3)[0]:.1f} {add(tch[j], dj, 3)[1]:.1f} {b_[0]:.1f} {b_[1]:.1f}")
        if thumb.nail:
            c = add(add(tip, td, -wt * .6), tn, -wt * thumb.nail_side)
            nl, nw = wt * 1.1, wt * .6
            p = [add(add(c, td, nl * .5), tn, nw * .9), add(c, td, nl * .62), add(add(c, td, nl * .5), tn, -nw * .9),
                 (*add(add(c, td, -nl * .5), tn, -nw), 'c'), (*add(add(c, td, -nl * .5), tn, nw), 'c')]
            faint.append(smooth(p))
        sh = offset_side(tch[1:], [x * .95 for x in tw[1:]], -ts)
        sh2 = offset_side(tch[1:], [x * .2 for x in tw[1:]], -ts)
        shade.append(smooth([*sh, *sh2[::-1]], t=.3))
    pts += list(thenar_pts) + [wrist_r]
    return dict(d=smooth(pts, t=.5), shade=shade, light=light, lines=lines_, faint=faint, pts=pts)


def poly_point(chain, s):
    """Point + unit direction at arclength fraction s in [0, len(chain)-1] (segment index + t)."""
    i = min(int(s), len(chain) - 2)
    t = s - i
    p = lerp(chain[i], chain[i + 1], t)
    d = _norm(_v(chain[i], chain[i + 1]))
    # blend direction near joints for a smooth normal
    if t < .25 and i > 0:
        d0 = _norm(_v(chain[i - 1], chain[i]))
        k = .5 + t * 2
        d = _norm(add((d0[0] * (1 - k), d0[1] * (1 - k)), d, k))
    if t > .75 and i < len(chain) - 2:
        d1 = _norm(_v(chain[i + 1], chain[i + 2]))
        k = .5 + (1 - t) * 2
        d = _norm(add((d1[0] * (1 - k), d1[1] * (1 - k)), d, k))
    return p, d


def profile(chain, samples, side):
    """samples: [(s, offset), ...]; side +1 = left normal (dy,-dx), -1 = opposite."""
    out = []
    for s, off, *flag in samples:
        p, d = poly_point(chain, s)
        n = (d[1] * side, -d[0] * side)
        q = add(p, n, off)
        out.append((*q, *flag))
    return out


import re as _re


def tpath(d, fn):
    """Apply point function fn((x,y))->(x,y) to every coordinate pair of an absolute path."""
    toks = _re.findall(r"[MLCQZ]|-?\d+\.?\d*", d)
    out, nums = [], []
    for t in toks:
        if t in "MLCQZ":
            out.append(t)
        else:
            nums.append(float(t))
            if len(nums) == 2:
                x, y = fn(tuple(nums)); nums = []
                out.append(f"{x:.1f} {y:.1f}")
    return " ".join(out)


def affine(tx, ty, sc=1.0, rot=0.0, ox=0, oy=0, flip=False, sy=None):
    c, s = math.cos(math.radians(rot)), math.sin(math.radians(rot))
    sy = sc if sy is None else sy
    def fn(p):
        x, y = (p[0] - ox) * sc, (p[1] - oy) * sy
        if flip: x = -x
        return (tx + x * c - y * s, ty + x * s + y * c)
    return fn
