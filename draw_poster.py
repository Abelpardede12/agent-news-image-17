#!/usr/bin/env python3
"""Draw the 17 November 2026 world-news poster (1024x1024, deterministic)."""
import math

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (245, 240, 230)
INK = (20, 20, 20)
RED = (178, 34, 34)
BLUE = (30, 70, 140)
GREY = (90, 90, 90)

FONT_DIR = "/usr/share/fonts/truetype/dejavu/"


def font(name, size):
    return ImageFont.truetype(FONT_DIR + name, size)


BOLD = lambda s: font("DejaVuSans-Bold.ttf", s)
REG = lambda s: font("DejaVuSans.ttf", s)


def wrap(draw, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_star(d, cx, cy, r, color):
    pts = []
    for i in range(16):
        ang = math.pi * i / 8 - math.pi / 2
        rr = r if i % 2 == 0 else r * 0.45
        pts.append((cx + rr * math.cos(ang), cy + rr * math.sin(ang)))
    d.polygon(pts, fill=color)


def illo_tanker(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(214, 228, 240), outline=INK, width=2)
    d.rectangle([x, y + h - 26, x + w, y + h], fill=(90, 140, 190))
    d.polygon([(x + 12, y + h - 48), (x + w - 12, y + h - 48),
               (x + w - 26, y + h - 26), (x + 26, y + h - 26)], fill=(60, 60, 60))
    cw = (w - 40) // 3
    for i, col in enumerate((RED, BLUE, (220, 160, 40))):
        d.rectangle([x + 20 + i * cw, y + h - 76, x + 20 + (i + 1) * cw - 4,
                     y + h - 48], fill=col)
    d.rectangle([x + w - 40, y + h - 88, x + w - 24, y + h - 48], fill=INK)
    d.ellipse([x + w - 52, y + 18, x + w - 32, y + 38], fill=GREY)
    d.ellipse([x + w - 44, y + 6, x + w - 26, y + 24], fill=GREY)
    draw_star(d, x + 34, y + 28, 20, (230, 120, 20))


def illo_bridge(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(224, 232, 240), outline=INK, width=2)
    d.rectangle([x + 6, y + h - 40, x + w - 6, y + h - 30], fill=INK)
    d.arc([x + 16, y + 22, x + w - 16, y + h - 16], 180, 360, fill=RED, width=5)
    for fx in (0.25, 0.5, 0.75):
        px = x + w * fx
        d.line([px, y + 34, px, y + h - 40], fill=RED, width=3)
    d.ellipse([x + w - 40, y + 12, x + w - 22, y + 30], fill=INK)
    d.line([x + w - 46, y + 10, x + w - 16, y + 10], fill=INK, width=3)
    draw_star(d, x + 30, y + 30, 14, (230, 120, 20))


def illo_tent(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(226, 232, 244), outline=INK, width=2)
    d.polygon([(x + 14, y + h - 18), (x + w // 2, y + 26), (x + w - 14, y + h - 18)],
              fill=(200, 90, 60))
    d.polygon([(x + w // 2 - 11, y + h - 18), (x + w // 2, y + h - 50),
               (x + w // 2 + 11, y + h - 18)], fill=(60, 60, 60))
    for rx in range(x + 10, x + w - 8, 22):
        d.line([rx, y + 10, rx - 5, y + 28], fill=BLUE, width=3)
    d.ellipse([x + 16, y + h - 14, x + w - 16, y + h - 4], fill=(120, 160, 200))


def illo_virus(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(240, 226, 226), outline=INK, width=2)
    cx, cy = x + w // 2, y + h // 2 + 4
    for i in range(10):
        ang = 2 * math.pi * i / 10
        d.line([cx + 22 * math.cos(ang), cy + 22 * math.sin(ang),
                cx + 36 * math.cos(ang), cy + 36 * math.sin(ang)], fill=RED, width=4)
        d.ellipse([cx + 36 * math.cos(ang) - 4, cy + 36 * math.sin(ang) - 4,
                   cx + 36 * math.cos(ang) + 4, cy + 36 * math.sin(ang) + 4],
                  fill=RED)
    d.ellipse([cx - 22, cy - 22, cx + 22, cy + 22], fill=RED)
    d.ellipse([cx - 10, cy - 10, cx - 2, cy - 2], fill=(255, 200, 200))
    d.ellipse([cx + 3, cy + 5, cx + 10, cy + 12], fill=(255, 200, 200))


def illo_summit(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(226, 236, 226), outline=INK, width=2)
    cx, cy, r = x + w // 2, y + h // 2 - 8, 28
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(90, 140, 190), outline=INK, width=2)
    d.arc([cx - r, cy - 10, cx + r, cy + 10], 0, 360, fill=(255, 255, 255), width=2)
    d.line([cx, cy - r, cx, cy + r], fill=(255, 255, 255), width=2)
    bw = w // 3 - 8
    for i, col in enumerate((RED, BLUE, (220, 160, 40))):
        ph = 22 + (10 if i == 1 else 0)
        bx = x + 8 + i * (bw + 4)
        d.rectangle([bx, y + h - 14 - ph, bx + bw, y + h - 14], fill=col)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # outer frame
    d.rectangle([6, 6, W - 7, H - 7], outline=INK, width=4)

    # ---- masthead ----
    d.text((W // 2, 34), "THE WORLD IN ONE PAGE", font=BOLD(62),
           fill=INK, anchor="ma")
    d.text((W // 2, 112), "TUESDAY, 17 NOVEMBER 2026", font=BOLD(34),
           fill=RED, anchor="ma")
    d.line([24, 158, W - 24, 158], fill=INK, width=4)
    d.line([24, 164, W - 24, 164], fill=INK, width=2)

    # ---- story 1 (lead, full width) ----
    y0 = 182
    d.text((24, y0), "LEAD STORY", font=BOLD(20), fill=RED)
    d.text((24, y0 + 26), "US STRIKES IRAN", font=BOLD(42), fill=INK)
    body1 = ("US warplanes hit missile sites on Qeshm Island after attacks on "
             "tankers in the Strait of Hormuz. Oman evacuated 24 seafarers "
             "from a burning gas tanker.")
    lines = wrap(d, body1, REG(23), 620)
    yy = y0 + 82
    for ln in lines:
        d.text((24, yy), ln, font=REG(23), fill=INK)
        yy += 30
    illo_tanker(d, 680, y0 + 4, 320, 168)
    d.line([24, 366, W - 24, 366], fill=INK, width=3)

    # ---- stories 2-5, two columns ----
    stories = [
        ("UKRAINE HITS KERCH BRIDGE",
         "Ukrainian drones and missiles struck the Crimean Bridge; Russia hit "
         "bridges in Kyiv. New Ukraine-US-European peace talks held online.",
         illo_bridge),
        ("GAZA'S WINTER CRISIS",
         "The UN warns winter rains are flooding shelters as 1.7 million "
         "remain displaced. The UK, Australia, Canada and Italy urge Israel "
         "to open crossings for aid.",
         illo_tent),
        ("US LOSES MEASLES-FREE STATUS",
         "The Pan American Health Organization says the US lost measles "
         "elimination status after a year of uninterrupted spread.",
         illo_virus),
        ("SUMMIT AHEAD IN CHINA",
         "Trump heads to Asia for a rare trilateral meeting with Xi Jinping "
         "and Vladimir Putin on 19 November. NVIDIA posts record revenue.",
         illo_summit),
    ]
    col_w = 476
    col_x = [24, 524]
    row_y = [382, 646]
    for i, (head, body, illo) in enumerate(stories):
        cx = col_x[i % 2]
        cy = row_y[i // 2]
        # illustration top-right, headline wraps beside it
        illo(d, cx + col_w - 112, cy, 112, 112)
        head_lines = wrap(d, head, BOLD(30), col_w - 128)
        yy = cy + 2
        for ln in head_lines:
            d.text((cx, yy), ln, font=BOLD(30), fill=INK)
            yy += 36
        body_lines = wrap(d, body, REG(22), col_w)
        yy = cy + 122
        for ln in body_lines:
            d.text((cx, yy), ln, font=REG(22), fill=INK)
            yy += 28
        if i % 2 == 0:
            d.line([cx, cy + 240, cx + col_w, cy + 240], fill=GREY, width=1)

    d.line([24, 900, W - 24, 900], fill=INK, width=3)

    # ---- footer ticker ----
    d.rectangle([24, 910, W - 24, 1000], fill=INK)
    ticker = ("Japan scrambles jets after suspected Russian airspace violation  \u2022  "
              "Gerard Depardieu admits sexual assault charge in Paris  \u2022  "
              "COP31 climate talks in Antalya enter decisive stage")
    lines = wrap(d, ticker, BOLD(19), W - 72)
    yy = 919
    for ln in lines:
        d.text((W // 2, yy), ln, font=BOLD(19), fill=(255, 255, 255), anchor="ma")
        yy += 25

    img.save("entry.png", "PNG", optimize=True)


if __name__ == "__main__":
    main()
