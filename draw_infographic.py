#!/usr/bin/env python3
"""Draw the 26 November 2026 world-news infographic (build time only).

Produces a 1024x1024 newspaper-style front page with six verified stories
from Thursday 26 November 2026. Uses Pillow; this script runs on the build
machine only and is NOT imported by main.py (the grader has no Pillow).
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "entry.png")

W, H = 1024, 1024
PAPER = (246, 241, 231)
INK = (26, 26, 26)
RED = (176, 42, 32)
BLUE = (31, 78, 121)
GOLD = (176, 132, 32)
GREY = (90, 86, 78)
PANEL = (255, 253, 247)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_storm(d, x, y, s):
    # Rain cloud + falling balloon (parade postponed by the storm)
    d.ellipse([x + 8, y + 18, x + 52, y + 52], fill=(120, 130, 145))
    d.ellipse([x + 30, y + 8, x + 78, y + 48], fill=(140, 150, 165))
    d.ellipse([x + 58, y + 20, x + 96, y + 52], fill=(120, 130, 145))
    d.rectangle([x + 8, y + 40, x + 96, y + 54], fill=(120, 130, 145))
    for i, rx in enumerate((x + 18, x + 42, x + 66, x + 88)):
        d.line([rx, y + 62, rx - 6, y + 78], fill=BLUE, width=4)
    d.ellipse([x + 96, y + 62, x + 122, y + 92], fill=RED)  # balloon
    d.line([x + 109, y + 92, x + 109, y + 112], fill=INK, width=2)


def draw_oil(d, x, y, s):
    # Oil droplet + flame
    d.polygon([(x + 60, y + 6), (x + 96, y + 58), (x + 88, y + 96),
               (x + 60, y + 108), (x + 32, y + 96), (x + 24, y + 58)],
              fill=(40, 40, 40))
    d.polygon([(x + 60, y + 22), (x + 76, y + 52), (x + 60, y + 62),
               (x + 44, y + 52)], fill=(255, 176, 32))
    d.polygon([(x + 60, y + 44), (x + 70, y + 62), (x + 60, y + 68),
               (x + 50, y + 62)], fill=(255, 90, 0))


def draw_fire(d, x, y, s):
    # Flame over a road
    d.polygon([(x + 60, y + 4), (x + 84, y + 40), (x + 96, y + 30),
               (x + 100, y + 70), (x + 84, y + 100), (x + 60, y + 110),
               (x + 36, y + 100), (x + 20, y + 70), (x + 24, y + 30),
               (x + 36, y + 40)], fill=(230, 90, 20))
    d.polygon([(x + 60, y + 48), (x + 74, y + 70), (x + 70, y + 92),
               (x + 60, y + 98), (x + 50, y + 92), (x + 46, y + 70)],
              fill=(255, 200, 40))
    d.rectangle([x + 6, y + 112, x + 114, y + 118], fill=INK)


def draw_jet(d, x, y, s):
    # Side-view jet: fuselage, swept wings, tail, contrail dots
    d.polygon([(x + 10, y + 58), (x + 92, y + 46), (x + 110, y + 56),
               (x + 92, y + 64), (x + 12, y + 70)], fill=(60, 70, 90))
    d.polygon([(x + 52, y + 52), (x + 74, y + 24), (x + 82, y + 26),
               (x + 66, y + 52)], fill=(60, 70, 90))
    d.polygon([(x + 20, y + 56), (x + 34, y + 34), (x + 42, y + 36),
               (x + 32, y + 56)], fill=(60, 70, 90))
    d.polygon([(x + 58, y + 64), (x + 78, y + 88), (x + 86, y + 86),
               (x + 70, y + 64)], fill=(90, 100, 120))
    for i in range(3):
        d.ellipse([x + 2 + i * 10, y + 96 + i * 4, x + 12 + i * 10,
                   y + 106 + i * 4], fill=(180, 180, 180))


def draw_tariff(d, x, y, s):
    # Rising tariff bars with a percent sign
    d.rectangle([x + 10, y + 76, x + 34, y + 110], fill=BLUE)
    d.rectangle([x + 44, y + 52, x + 68, y + 110], fill=BLUE)
    d.rectangle([x + 78, y + 26, x + 102, y + 110], fill=RED)
    d.line([x + 6, y + 110, x + 114, y + 110], fill=INK, width=3)
    d.text((x + 84, y + 2), "%", font=font(SANS_B, 30), fill=RED)


def draw_shield(d, x, y, s):
    # Police shield with a check mark (hostages freed)
    d.polygon([(x + 16, y + 8), (x + 104, y + 8), (x + 104, y + 58),
               (x + 60, y + 112), (x + 16, y + 58)], fill=BLUE)
    d.polygon([(x + 24, y + 16), (x + 96, y + 16), (x + 96, y + 56),
               (x + 60, y + 100), (x + 24, y + 56)], outline=(255, 255, 255),
              width=3)
    d.line([x + 40, y + 58, x + 55, y + 74, x + 84, y + 38], fill=(255, 255, 255),
           width=7, joint="curve")


ICONS = [draw_storm, draw_oil, draw_fire, draw_jet, draw_tariff, draw_shield]

STORIES = [
    ("STORM STOPS THE PARADE",
     "Thanksgiving storm postpones Macy's 100th parade — the first weather "
     "postponement in a century — as rain and floods hit the US East Coast."),
    ("OIL TOPS $94",
     "Houthis claim a hit on Saudi Arabia's Ras Tanura refinery; Iranian "
     "mines strike two tankers in the Strait of Hormuz. Brent crude surges."),
    ("31 KILLED IN CAIRO FIRE",
     "A fuel tanker crashes and bursts into flames on Cairo's ring road, "
     "engulfing cars and motorcycles. At least 31 dead, 21 injured."),
    ("FIVE RUSSIAN JETS HIT",
     "Ukraine says it damaged three MiG-31s and two Su-34s at Savasleyka "
     "airbase, 300 km east of Moscow, and hit two refineries in Samara."),
    ("US UNVEILS NEW TARIFFS",
     "Washington proposes sweeping tariffs on 14 trading partners over "
     "industrial overcapacity. China faces up to 40%; Taiwan up to 15%."),
    ("HOSTAGES FREED IN COLOMBIA",
     "Police storm a supermarket in Cartagena and free around 20 shoppers "
     "and staff after a 17-hour hostage siege. One gunman is killed."),
]


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # Masthead
    d.rectangle([0, 0, W, 8], fill=RED)
    title = "THE WORLD IN ONE DAY"
    tf = font(SERIF_B, 58)
    tw = d.textlength(title, font=tf)
    d.text(((W - tw) / 2, 26), title, font=tf, fill=INK)
    date = "THURSDAY 26 NOVEMBER 2026"
    df = font(SANS_B, 30)
    dw = d.textlength(date, font=df)
    d.text(((W - dw) / 2, 100), date, font=df, fill=RED)
    d.line([24, 146, W - 24, 146], fill=INK, width=3)
    d.line([24, 152, W - 24, 152], fill=INK, width=1)

    # Story grid: 2 columns x 3 rows
    gx, gy = 16, 164
    pw, ph, gap = 488, 258, 16
    hf = font(SANS_B, 25)
    bf = font(SANS, 21)
    for i, (head, body) in enumerate(STORIES):
        col, row = i % 2, i // 2
        x = gx + col * (pw + gap)
        y = gy + row * (ph + gap)
        d.rectangle([x, y, x + pw, y + ph], fill=PANEL, outline=(200, 192, 176),
                    width=2)
        # icon panel
        ix, iy = x + 14, y + 14
        d.rectangle([ix, iy, ix + 128, iy + 128], fill=(238, 232, 218),
                    outline=(200, 192, 176), width=1)
        ICONS[i](d, ix + 4, iy + 4, 1)
        # headline + body
        tx = x + 156
        twd = pw - 156 - 16
        lines = wrap(d, head, hf, twd)
        ly = y + 16
        for ln in lines:
            d.text((tx, ly), ln, font=hf, fill=INK)
            ly += 31
        blines = wrap(d, body, bf, twd)
        ly += 6
        for ln in blines[:5]:
            d.text((tx, ly), ln, font=bf, fill=(52, 50, 46))
            ly += 27

    # Footer
    fy = 164 + 3 * ph + 2 * gap + 12
    d.line([24, fy, W - 24, fy], fill=INK, width=2)
    ff = font(SANS, 19)
    foot = "Six stories from Thursday 26 November 2026  •  Sources: Reuters, AP, BBC, CNN"
    fw = d.textlength(foot, font=ff)
    d.text(((W - fw) / 2, fy + 10), foot, font=ff, fill=GREY)

    img.save(OUT, "PNG", optimize=True)
    print("wrote", OUT, os.path.getsize(OUT), "bytes")


if __name__ == "__main__":
    main()
