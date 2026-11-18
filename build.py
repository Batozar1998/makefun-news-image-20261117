"""Build news-image-20261117 entry.png (1024x1024, JPEG bytes, <1 MiB).

Dense front page in the winners' style: masthead + hero + 5 featured panels
+ world-map / day-in-figures band + 28 brief stories grouped by continent.
34 stories, 6 continents. Drawn with Pillow primitives only — deterministic,
no network. Run: python3 build.py  (writes entry.png next to this file)
"""
import math
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
W, H = 1024, 1024
NAVY = (13, 27, 46)
NAVY2 = (24, 44, 78)
GOLD = (212, 175, 55)
GOLD_D = (168, 132, 32)
WHITE = (255, 255, 255)
INK = (20, 20, 20)
GREY = (90, 90, 90)
PAPER = (242, 240, 235)
PANEL = (255, 255, 255)
LINE = (200, 200, 200)

FB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FS = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"

CONTINENT_COLORS = {
    "EUROPE": (30, 80, 160),
    "ASIA": (176, 42, 42),
    "AFRICA": (196, 120, 20),
    "NORTH AMERICA": (20, 120, 90),
    "SOUTH AMERICA": (120, 60, 160),
    "OCEANIA": (20, 110, 170),
}


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(d, text, fnt, max_w, max_lines=None):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=fnt) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    if max_lines and len(lines) > max_lines:
        lines = lines[:max_lines]
        # trim last line until an ellipsis fits
        while lines and d.textlength(lines[-1] + "…", font=fnt) > max_w:
            lines[-1] = lines[-1][:-1]
        lines[-1] = lines[-1] + "…"
    return lines


# ---------------------------------------------------------------- art (from v1)
def draw_bridge(d, x, y, w, h):
    # night sea + bridge deck, two towers, cables, blast burst, drones
    d.rectangle([x, y, x + w, y + h], fill=(24, 44, 78))
    d.rectangle([x, y + 100, x + w, y + h], fill=(16, 34, 64))
    for cx in (x + 130, x + 330):
        d.rectangle([cx - 6, y + 18, cx + 6, y + 100], fill=(180, 190, 205))
    d.rectangle([x + 8, y + 96, x + w - 8, y + 106], fill=(200, 205, 215))
    for tx in range(x + 40, x + w - 30, 46):
        d.line([(tx, y + 98), (x + 130, y + 22)], fill=(150, 160, 175), width=2)
        d.line([(tx, y + 98), (x + 330, y + 22)], fill=(150, 160, 175), width=2)
    bx, by = x + 232, y + 62  # blast
    for r, c in ((34, (255, 140, 40)), (24, (255, 200, 60)), (13, (255, 240, 160))):
        d.ellipse([bx - r, by - r, bx + r, by + r], fill=c)
    for ang in range(0, 360, 30):
        a = math.radians(ang)
        d.line([(bx, by), (bx + 44 * math.cos(a), by + 44 * math.sin(a))],
               fill=(255, 160, 50), width=3)
    for dx, dy in ((70, 30), (400, 42)):
        d.ellipse([x + dx - 4, y + dy - 4, x + dx + 4, y + dy + 4], fill=(255, 255, 255))


def draw_bridge_wide(d, x, y, w, h):
    # same scene, towers/cables/blast positioned by fraction of width
    d.rectangle([x, y, x + w, y + h], fill=(24, 44, 78))
    d.rectangle([x, y + h - 26, x + w, y + h], fill=(16, 34, 64))
    t1, t2 = x + int(w * 0.27), x + int(w * 0.68)
    for cx in (t1, t2):
        d.rectangle([cx - 7, y + 14, cx + 7, y + h - 30], fill=(180, 190, 205))
    d.rectangle([x + 6, y + h - 34, x + w - 6, y + h - 24], fill=(200, 205, 215))
    for tx in range(x + 24, x + w - 16, 40):
        d.line([(tx, y + h - 32), (t1, y + 18)], fill=(150, 160, 175), width=2)
        d.line([(tx, y + h - 32), (t2, y + 18)], fill=(150, 160, 175), width=2)
    bx, by = x + int(w * 0.48), y + int(h * 0.42)
    for r, c in ((40, (255, 140, 40)), (28, (255, 200, 60)), (15, (255, 240, 160))):
        d.ellipse([bx - r, by - r, bx + r, by + r], fill=c)
    for ang in range(0, 360, 30):
        a = math.radians(ang)
        d.line([(bx, by), (bx + 52 * math.cos(a), by + 52 * math.sin(a))],
               fill=(255, 160, 50), width=3)
    for dx, dy in ((0.12, 0.25), (0.85, 0.32)):
        px, py = x + int(w * dx), y + int(h * dy)
        d.ellipse([px - 5, py - 5, px + 5, py + 5], fill=(255, 255, 255))


def draw_chip(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(12, 60, 38))
    cx, cy = x + 150, y + 69
    for i in range(5):
        d.line([(x + 20, cy - 44 + i * 22), (cx - 52, cy - 44 + i * 22)],
               fill=(60, 180, 120), width=3)
        d.line([(cx + 52, cy - 44 + i * 22), (x + w - 20, cy - 44 + i * 22)],
               fill=(60, 180, 120), width=3)
    d.rounded_rectangle([cx - 52, cy - 52, cx + 52, cy + 52], radius=10,
                        fill=(20, 20, 20), outline=(120, 220, 160), width=3)
    d.text((cx, cy - 8), "AI", font=font(FB, 34), fill=(140, 230, 170), anchor="mm")
    d.text((cx, cy + 26), "CHIP", font=font(FB, 20), fill=(140, 230, 170), anchor="mm")
    ax, ay = x + w - 78, y + 30
    d.line([(ax, ay + 26), (ax + 22, ay), (ax + 44, ay + 26)], fill=(90, 230, 130), width=7)
    d.line([(ax + 22, ay + 2), (ax + 22, ay + 34)], fill=(90, 230, 130), width=7)


def draw_gavel(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(74, 52, 32))
    cx, cy = x + 245, y + 14
    d.rectangle([cx - 4, cy, cx + 4, cy + 84], fill=(255, 220, 150))
    d.rectangle([cx - 90, cy + 8, cx + 90, cy + 14], fill=(255, 220, 150))
    d.ellipse([cx - 10, cy - 8, cx + 10, cy + 10], fill=(255, 220, 150))
    for sx in (cx - 90, cx + 90):
        d.line([(sx, cy + 11), (sx - 26, cy + 58)], fill=(255, 220, 150), width=3)
        d.line([(sx, cy + 11), (sx + 26, cy + 58)], fill=(255, 220, 150), width=3)
        d.polygon([(sx - 30, cy + 58), (sx + 30, cy + 58), (sx, cy + 78)],
                  fill=(210, 170, 110))
    d.rectangle([cx - 46, cy + 84, cx + 46, cy + 96], fill=(255, 220, 150))
    d.text((x + 24, y + 16), "GUILTY", font=font(FB, 30), fill=(255, 220, 150))


def draw_jet(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(135, 190, 225))
    d.ellipse([x + w - 120, y + 8, x + w - 20, y + 108], fill=(255, 120, 90))
    for i, yy in enumerate((30, 62, 94)):
        d.line([(x + 20, y + yy), (x + 300, y + yy + 18)], fill=(255, 255, 255), width=3)
    jx, jy = x + 300, y + 60
    d.polygon([(jx - 120, jy + 26), (jx + 60, jy - 6), (jx + 120, jy + 4),
               (jx + 40, jy + 14), (jx + 30, jy + 30), (jx - 60, jy + 34)],
              fill=(40, 50, 70))
    d.polygon([(jx - 40, jy + 26), (jx + 10, jy + 44), (jx + 60, jy + 30)],
              fill=(40, 50, 70))


def draw_virus(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(245, 235, 220))
    cx, cy = x + 110, y + 69
    for ang in range(0, 360, 25):
        a = math.radians(ang)
        d.line([(cx + 34 * math.cos(a), cy + 34 * math.sin(a)),
                (cx + 52 * math.cos(a), cy + 52 * math.sin(a))],
               fill=(200, 40, 40), width=5)
    d.ellipse([cx - 36, cy - 36, cx + 36, cy + 36], fill=(220, 60, 60))
    for dx, dy in ((-14, -10), (12, -14), (0, 12), (16, 8), (-16, 14)):
        d.ellipse([cx + dx - 6, cy + dy - 6, cx + dx + 6, cy + dy + 6], fill=(160, 20, 20))
    d.text((x + 200, y + 30), "5,400+", font=font(FB, 52), fill=(180, 30, 30))
    d.text((x + 202, y + 92), "CASES IN 2026", font=font(FB, 22), fill=(120, 30, 30))


def draw_crash(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(38, 44, 58))
    for sx, sy, sr in ((70, 30, 22), (150, 48, 16), (420, 26, 18)):
        d.ellipse([x + sx - sr, y + sy - sr, x + sx + sr, y + sy + sr], fill=(70, 78, 100))
    px, py = x + 250, y + 62
    d.polygon([(px - 110, py + 10), (px + 70, py - 26), (px + 110, py - 8),
               (px + 30, py + 6), (px + 20, py + 22), (px - 60, py + 26)],
              fill=(200, 205, 215))
    for i in range(5):
        d.ellipse([px - 150 - i * 26, py + 18 + i * 8 - 12, px - 126 - i * 26, py + 18 + i * 8 + 12],
                  fill=(120, 120, 130))


def render_art(draw_fn, w, h):
    """Render an art function at its native 490x126 size, then scale to (w, h)."""
    tmp = Image.new("RGB", (490, 126), WHITE)
    td = ImageDraw.Draw(tmp)
    draw_fn(td, 0, 0, 490, 126)
    return tmp.resize((w, h), Image.LANCZOS)


# ---------------------------------------------------------------- world map
# 48 x 24 equirectangular land bitmap (rows = 90N..-90S in 7.5 deg steps).
MAP_GRID = [
    "................................................",
    "..######......###.................................",
    ".###########..###.....###......################....",
    "..##########...##.....####....#################....",
    "..##########...###...######..##################...",
    "...##########..##########...##################....",
    "....########..###########...#############.........",
    "....########....#####..###..#########.............",
    ".....#####.....#####..###...######..###...........",
    "......###......#####..##....###...####............",
    ".......##......######..##....###...###............",
    ".........###....#####....###...####...............",
    ".........####...#####.....###....####.............",
    "..........####..#####..#...###...####............",
    "..........####..####....###..####................",
    "..........####..###.....###..####................",
    "..........###....#......###...##.................",
    "..........##............................##......",
    "..........#.....................................",
    "................................................",
    "................................................",
    "................................................",
    "................................................",
    "................................................",
]
# (lon, lat) of the six featured stories, for gold markers on the map.
MAP_MARKERS = [
    (34, 45),    # Crimea bridge
    (-122, 37),  # NVIDIA, California
    (2.3, 49),   # Paris
    (140, 36),   # Japan
    (-77, 39),   # Washington DC (measles, US-wide)
    (86.5, 55),  # Kemerovo
]


def draw_map(d, x, y, w, h):
    cw, ch = w / 48, h / 24
    d.rectangle([x, y, x + w, y + h], fill=(232, 238, 244))
    for r, row in enumerate(MAP_GRID):
        for c, ch_ in enumerate(row):
            if ch_ == "#":
                cx, cy = x + c * cw + cw / 2, y + r * ch + ch / 2
                d.ellipse([cx - 2.1, cy - 2.1, cx + 2.1, cy + 2.1], fill=NAVY2)
    for lon, lat in MAP_MARKERS:
        col = (lon + 180) / 7.5
        row = (90 - lat) / 7.5
        mx, my = x + col * cw, y + row * ch
        d.ellipse([mx - 5, my - 5, mx + 5, my + 5], fill=GOLD, outline=WHITE, width=2)
    # continent labels on solid pills, placed in open ocean so dots never
    # show through and no label is clipped by the map edge
    lf = font(FB, 11)
    for txt, lx, ly in (("N. AMERICA", 0.03, 0.06), ("EUROPE", 0.30, 0.20),
                        ("AFRICA", 0.44, 0.80), ("ASIA", 0.68, 0.06),
                        ("S. AMERICA", 0.24, 0.66), ("OCEANIA", 0.70, 0.82)):
        px, py = x + int(w * lx), y + int(h * ly)
        tw = d.textlength(txt, font=lf)
        d.rounded_rectangle([px - 3, py - 2, px + tw + 3, py + 13], radius=4,
                            fill=(232, 238, 244))
        d.text((px, py), txt, font=lf, fill=(90, 100, 115))


# ---------------------------------------------------------------- content
HERO = ("CRIMEA BRIDGE HIT",
        "Ukraine's drones and missiles strike the Kerch bridge",
        "A span collapses into the sea as traffic halts; Zelensky calls "
        "the operation \u2018unprecedented\u2019.")

FEATURED = [
    ("NVIDIA'S BIG NIGHT",
     "Bumper results, but no return for Huang.",
     draw_chip),
    ("DEPARDIEU ADMITS GUILT",
     "French star pleads guilty in a Paris court.",
     draw_gavel),
    ("JETS SCRAMBLED",
     "Fighters up after Russian planes breach airspace.",
     draw_jet),
    ("MEASLES COMEBACK",
     "US loses elimination status after 26 years.",
     draw_virus),
    ("PLANE CRASH IN RUSSIA",
     "Military plane crashes; all 19 on board killed.",
     draw_crash),
]

FIGURES = [
    ("5,400+", "measles cases in the US in 2026"),
    ("19", "killed in the Kemerovo plane crash"),
    ("146,000", "marched in France's cost-of-living protests"),
    ("13M", "joined Pope Leo's South America tour"),
]

# (continent, headline) — headlines kept <= 50 chars so they wrap to <= 2 lines.
BRIEFS = [
    ("EUROPE", "Russia hits two Kyiv bridges; heating cut"),
    ("EUROPE", "France cost-of-living march draws 146,000"),
    ("EUROPE", "UK sanctions 8 firms over West Bank building"),
    ("EUROPE", "Deutsche Bank shares fall 6% on 15m-file leak"),
    ("EUROPE", "Pattinson is the new Bond \u2014 Bezos defends pick"),
    ("EUROPE", "Five EU states plan Rwanda return hub for 2027"),
    ("ASIA", "Mongolia's president says he will resign"),
    ("ASIA", "West calls for Gaza crossings to open"),
    ("ASIA", "Woman, 72, shot dead in the West Bank"),
    ("ASIA", "Houthis advance on Aden; Saudis swap commander"),
    ("ASIA", "Iranian drones target US base in Bahrain"),
    ("ASIA", "Trump in Manila; hundreds held in protests"),
    ("AFRICA", "DR Congo Ebola \u2018out of control\u2019 \u2014 5,500 dead"),
    ("AFRICA", "Two mass shootings in South Africa kill 17"),
    ("AFRICA", "Mozambique's Mondlane on trial for terrorism"),
    ("AFRICA", "Guinea arrests 1,200 in gold-mining crackdown"),
    ("AFRICA", "Senegal, Cameroon, Morocco reach AFCON 2027"),
    ("AFRICA", "Rwanda genocide trial opens in Paris"),
    ("NORTH AMERICA", "FAA halts router work after 20,000 flights cut"),
    ("NORTH AMERICA", "Hack via Optimizely hits 178 sites, incl. BBC"),
    ("NORTH AMERICA", "Trump deposition deadline extended in BBC case"),
    ("SOUTH AMERICA", "Pope Leo ends tour; 13m join South America events"),
    ("SOUTH AMERICA", "Pope hit in face by rosary thrown in Lima"),
    ("SOUTH AMERICA", "Hegseth to visit Colombia, deliver C-130"),
    ("SOUTH AMERICA", "Brazil probes Vance-linked donor network"),
    ("OCEANIA", "Cyclone Xavier sets November record at Cat 5"),
    ("OCEANIA", "Melbourne Cup horse found dead in a dumpster"),
    ("OCEANIA", "Australia challenged at COP31 over coal and gas"),
]

# columns balanced by item count: 9 / 10 / 9
COLUMNS = [
    [("EUROPE", 6), ("OCEANIA", 3)],
    [("ASIA", 6), ("SOUTH AMERICA", 4)],
    [("AFRICA", 6), ("NORTH AMERICA", 3)],
]


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    M, G = 14, 6  # margin, gap between bands

    # ---- masthead (0..84)
    d.rectangle([0, 0, W, 84], fill=NAVY)
    d.rectangle([0, 84, W, 90], fill=GOLD)
    d.text((W // 2, 36), "THE WORLD TODAY", font=font(FS, 50), fill=WHITE, anchor="mm")
    d.text((W // 2, 72), "TUESDAY 17 NOVEMBER 2026  \u2022  34 STORIES  \u2022  6 CONTINENTS",
           font=font(FB, 17), fill=GOLD, anchor="mm")

    # ---- hero: Crimea (96..252)
    hy, hh = 96, 156
    d.rounded_rectangle([M, hy, W - M, hy + hh], radius=10, fill=PANEL,
                        outline=LINE, width=2)
    draw_bridge_wide(d, M, hy, 470, hh)
    # redraw the panel border over the square-cornered art
    d.rounded_rectangle([M, hy, W - M, hy + hh], radius=10, outline=LINE, width=2)
    tx = M + 470 + 18
    d.text((tx, hy + 16), "TOP STORY", font=font(FB, 14), fill=GOLD_D)
    d.text((tx, hy + 44), HERO[0], font=font(FB, 30), fill=INK)
    d.text((tx, hy + 82), HERO[1], font=font(FB, 16), fill=(40, 40, 40))
    for i, ln in enumerate(wrap(d, HERO[2], font(FR, 14), W - M - tx - 14)):
        d.text((tx, hy + 108 + i * 18), ln, font=font(FR, 14), fill=GREY)

    # ---- featured row: 5 panels (258..394)
    fy, fh = 258, 136
    pw = 192
    total_w = 5 * pw + 4 * 8
    fx0 = (W - total_w) // 2
    for i, (head, cap, draw_fn) in enumerate(FEATURED):
        x = fx0 + i * (pw + 8)
        d.rounded_rectangle([x, fy, x + pw, fy + fh], radius=8, fill=PANEL,
                            outline=LINE, width=2)
        art = render_art(draw_fn, pw, 58)
        img.paste(art, (x, fy))
        d.rounded_rectangle([x, fy, x + pw, fy + fh], radius=8,
                            outline=LINE, width=2)
        d.line([(x, fy + 58), (x + pw, fy + 58)], fill=LINE, width=2)
        hf = font(FB, 15)
        lines = wrap(d, head, hf, pw - 14, max_lines=2)
        yy = fy + 64
        for ln in lines:
            d.text((x + 7, yy), ln, font=hf, fill=INK)
            yy += 18
        cf = font(FR, 12)
        for ln in wrap(d, cap, cf, pw - 14, max_lines=2):
            d.text((x + 7, yy), ln, font=cf, fill=GREY)
            yy += 14

    # ---- middle band: figures | map | figures (400..546)
    my, mh = 400, 146
    d.rounded_rectangle([M, my, W - M, my + mh], radius=8, fill=PANEL,
                        outline=LINE, width=2)
    map_w, map_h = 300, mh
    map_x = (W - map_w) // 2
    draw_map(d, map_x, my, map_w, map_h)
    d.rounded_rectangle([M, my, W - M, my + mh], radius=8, outline=LINE, width=2)
    d.line([(map_x - 10, my + 8), (map_x - 10, my + mh - 8)], fill=LINE, width=2)
    d.line([(map_x + map_w + 10, my + 8), (map_x + map_w + 10, my + mh - 8)],
           fill=LINE, width=2)
    # figures: two stacked on each side of the map
    fig_zones = [(M + 12, map_x - 24), (map_x + map_w + 24, W - M - 12)]
    for zi, (zx0, zx1) in enumerate(fig_zones):
        for fi in range(2):
            num, lab = FIGURES[zi * 2 + fi]
            cy = my + 14 + fi * 72
            d.text((zx0, cy), num, font=font(FB, 30), fill=NAVY)
            lf = font(FR, 12)
            for j, ln in enumerate(wrap(d, lab, lf, zx1 - zx0, max_lines=2)):
                d.text((zx0, cy + 36 + j * 15), ln, font=lf, fill=GREY)

    # ---- briefs: 3 columns (552..1006)
    by = 552
    col_w = (W - 2 * M - 2 * 10) // 3
    hf, bf = font(FB, 15), font(FB, 14)
    # index briefs by continent, preserving order
    by_cont = {}
    for cont, head in BRIEFS:
        by_cont.setdefault(cont, []).append(head)
    for ci, groups in enumerate(COLUMNS):
        x = M + ci * (col_w + 10)
        yy = by
        for cont, _n in groups:
            d.text((x, yy), cont, font=hf, fill=CONTINENT_COLORS[cont])
            yy += 20
            for head in by_cont[cont]:
                for ln in wrap(d, head, bf, col_w - 4, max_lines=2):
                    d.text((x, yy), ln, font=bf, fill=INK)
                    yy += 17
                yy += 9  # gap between items
            yy += 6  # gap after group

    # ---- footer
    d.text((W // 2, 1014),
           "All 34 stories reported 17 Nov 2026  \u2022  full source list in the entry README",
           font=font(FR, 14), fill=GREY, anchor="mm")

    out = HERE / "entry.png"
    img.save(out, "JPEG", quality=88)
    print(out, out.stat().st_size, "bytes")


if __name__ == "__main__":
    main()
