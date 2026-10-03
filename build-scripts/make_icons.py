# -*- coding: utf-8 -*-
"""Generate icon-192.png / icon-512.png for Leo-Ritual (ripple mark)."""
import os
import sys
from PIL import Image, ImageDraw

OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(__file__))

BG = (180, 96, 122)     # --accent dusty rose
RING = (247, 244, 241)  # cream


def make(size):
    ss = 4
    S = size * ss
    img = Image.new("RGB", (S, S), BG)
    d = ImageDraw.Draw(img)
    cx = cy = S / 2

    radii = [0.42, 0.30, 0.185, 0.07]
    colors = [RING, BG, RING, BG]
    for r, col in zip(radii, colors):
        rr = S * r
        d.ellipse([cx - rr, cy - rr, cx + rr, cy + rr], fill=col)

    return img.resize((size, size), Image.LANCZOS)


for s in (192, 512):
    make(s).save(os.path.join(OUT, "icon-%d.png" % s))
    print("wrote icon-%d.png" % s)
