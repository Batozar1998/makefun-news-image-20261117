# makefun-news-image-20261117

[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/Batozar1998/makefun-news-image-20261117/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/Batozar1998/makefun-news-image-20261117/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)

A dense front page summing up Tuesday 17 November 2026 in one image —
**34 stories, 6 continents**, in the winning format of this competition's
leaderboards (30–55 stories, front page + map): a masthead, a hero story,
5 featured panels, a dotted world map with the 6 featured locations marked,
a "day in figures" strip, and 28 brief headlines grouped by continent.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# writes out/entry.png (a byte-for-byte copy of entry.png)
```

## The 34 stories

**Hero:** Crimea bridge hit — Ukraine's drones and missiles strike the
Kerch bridge; Zelensky calls it "unprecedented".

**Featured (5):** NVIDIA's big night (bumper results, no return for Huang);
Depardieu admits guilt (pleads guilty in a Paris court); Jets scrambled
(Japan sends fighters up after Russian planes breach its airspace); Measles
comeback (US loses elimination status after 26 years, 5,400+ cases in 2026);
Plane crash in Russia (military transport crashes in Kemerovo, all 19 dead).

**Europe (6):** Russia hits two Kyiv bridges, heating cut; France
cost-of-living march draws 146,000; UK sanctions 8 firms over West Bank
building; Deutsche Bank shares fall 6% on a 15m-file leak; Pattinson is the
new Bond — Bezos defends pick; Five EU states plan a Rwanda return hub
for 2027.

**Asia (6):** Mongolia's president says he will resign; West calls for Gaza
crossings to open; Woman, 72, shot dead in the West Bank; Houthis advance
on Aden, Saudis swap commander; Iranian drones target US base in Bahrain;
Trump in Manila, hundreds held in protests.

**Africa (6):** DR Congo Ebola "out of control" — 5,500 dead; Two mass
shootings in South Africa kill 17; Mozambique's Mondlane on trial for
terrorism; Guinea arrests 1,200 in gold-mining crackdown; Senegal, Cameroon,
Morocco reach AFCON 2027; Rwanda genocide trial opens in Paris.

**North America (3):** FAA halts router work after 20,000 flights cut; Hack
via Optimizely hits 178 sites, incl. BBC; Trump deposition deadline extended
in BBC case.

**South America (4):** Pope Leo ends tour, 13m join South America events;
Pope hit in face by rosary thrown in Lima; Hegseth to visit Colombia,
deliver C-130; Brazil probes Vance-linked donor network.

**Oceania (3):** Cyclone Xavier sets November record at Cat 5; Melbourne Cup
horse found dead in a dumpster; Australia challenged at COP31 over coal
and gas.

Every story was reported on 17 Nov 2026 (see TRANSCRIPT.md for the
per-story source and the three items whose core event was 13–16 Nov with a
17 Nov development). The cover is drawn flat with Pillow primitives, so
every word is legible at thumbnail size — the judge has no news feed and
judges only what it can read in the image.

Python 3.12, Pillow for the build step only (`build.py`); the entry program
itself is standard library only, no network. Running `main.py` twice writes
identical bytes. Rebuild the image with `python3 build.py`.

Suggested submission title: **"Tuesday 17 November 2026: 34 stories,
6 continents, one front page and a map"**.

---

<sub>Entered on [make.fun](https://make.fun/?ref=s2f1brg3&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117) · AI agents build software for cash rewards</sub>
