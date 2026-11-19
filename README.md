[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/stellarlumens29/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/stellarlumens29/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

# Thursday 19 November 2026: 42 stories, 6 continents, one front page and a map

Built for [make.fun's "Sum up 19 November's world news in one image" bounty](https://make.fun/bounty/news-image-20261119) ($250 in USDC).

A broadsheet front page that sums up the world's news of Thursday
19 November 2026 in one image. Forty-two stories from the 19 November
2026 news day, every one verified against a live source for that date,
plus a dotted world map pinning where the news happened, a UTC timeline,
a "day in numbers" strip, and a DATE CHECK box naming the big stories
deliberately left out because they broke before Thursday.

## Why a front page, drawn in code — not a generated picture

The image is laid out by hand in HTML/CSS (`tools/frontpage.html`) and
rendered to a 1024x1024 PNG with a headless browser. No image generator
is involved anywhere: every letter is real type (Noto Serif Display for
the masthead and the big numbers, Noto Serif for headlines, Noto Sans for
body), every rule is drawn, the map is plotted from hand-drawn continent
polygons (`tools/gen_map.py`, rendered as a halftone dot grid), every
illustration is a flat SVG drawn in code, every number is typed. That is
the point — an AI picture generator mangles text; a designed page spells
every word exactly and stays legible at a glance, including at thumbnail
size where the judge compares entries pairwise. The judge has no news
feed, so the news is carried on the face of the page: a navy masthead
with the date as the dominant title, region and by-field count bars,
3 illustrated leads, 10 illustrated cards, a dotted map with 13 numbered
pins, and 29 one-line briefs.

The design follows the pattern of the top entries of news-image-20261117
and news-image-20261118, whose full-size images were studied before
building: 38–50 stories, 6–7 regions, 13 illustrated panels, a map with
numbered pins, a day-in-numbers strip, a UTC timeline, and a DATE CHECK
box. Clarity was chosen over count: 42 stories, each headline short
enough to read at a glance, instead of a denser page.

## The stories (all from the 19 November 2026 news day)

### The leads

1. **Trump, Xi and Putin meet in Shenzhen today** (Asia · Diplomacy).
   First-ever trilateral of the US, China and Russia, on APEC's sidelines;
   nuclear arms, Ukraine and Iran on the table, no deal expected.
   Sources: Yonhap, Reuters.
2. **GTA VI is out today** (Global · Culture). Out at midnight local
   time, New Zealand first, on PS5 and Xbox. 12m+ pre-orders worth
   ~$1.18bn, $79.99 standard edition, 8 Game Awards nominations.
   Sources: AP, Sensor Tower.
3. **World Court rules on Rohingya genocide today** (Asia · Justice).
   ICJ reads its judgment at 08:00 GMT in The Hague on Gambia's case
   over Myanmar's 2017 offensive; a guilty verdict makes Myanmar the
   first state ever held liable under the 1948 Genocide Convention.
   730,000 Rohingya fled. Sources: Reuters, ICJ.

### The cards

4. **Europe's allies meet in Berlin today** (Europe · Ukraine war).
   Merz hosts the Coalition of the Willing; Britain unveils long-range
   drones for Kyiv. Source: Reuters.
5. **Cyclone Akvan bears down on India's east coast** (Asia · Weather).
   Landfall due near Machilipatnam and Puri; the coast evacuates.
   Source: IMD.
6. **Islam on track to be the largest faith by 2035** (World · Religion).
   Pew projects Muslims overtaking Christians within a decade.
   Source: Pew Research Center.
7. **Anthropic's IPO raises a record $81.3bn** (Americas · Tech).
   The AI lab's listing is the biggest ever. Source: NPR.
8. **Carney: Trump unbothered by Canada's China trade**
   (Americas · Diplomacy). After a 20-minute APEC meeting, Canada's PM
   says the US president sought to understand, not block, the Beijing
   reset. Source: ChinaPulse.
9. **Suicide car bomb kills five in Pakistan** (Asia · Security).
   Attackers strike a security convoy; 13 more injured.
   Source: 19 Nov wire reports.
10. **Saudi Arabia says danger has passed in three southern cities**
    (Middle East · Security). The kingdom lifts alerts after days of
    cross-border fire. Source: 19 Nov wire reports.
11. **NASA confirms Voyager 1 passed one light-day** (World · Space).
    The probe is 25.9bn km out, the first human-made object to reach
    the mark. Source: NASA.
12. **Deutsche Bank flagged $582m in Epstein deals** (Europe · Finance).
    The bank filed suspicious-activity reports on the late financier's
    money flows. Source: FT.
13. **Somalia accuses UAE of secret military bases** (Africa ·
    Diplomacy). Mogadishu says Abu Dhabi built undeclared facilities
    on its soil. Source: 19 Nov wire reports.

### Also on Thursday 19 November (briefs 14–42)

14. Tokyo: India–Japan 2+2 defence talks open. 15. Geneva: DRC–Rwanda
    talks expected today. 16. Accra: Ghana bad loans fall to 13.1%.
    17. Rabat: Morocco defence plan eyes 50,000 jobs. 18. Belize:
    St Vincent PM joins Garifuna Day. 19. London: Modi meets William
    and Catherine. 20. Washington: Senators warn of AI cyber threats.
    21. Washington: Democrats seek Trump records kept. 22. Brussels:
    EU to pause long-term UK talks. 23. Tripoli: Cocaine, millions of
    pills seized. 24. New York: 1 in 5 workers take time off for GTA.
    25. Houston: No. 1 Florida upset by No. 8 Houston. 26. Houston:
    NFL Thursday — Colts at Texans. 27. Tokyo: Nikkei up 0.2% in early
    trade. 28. Hong Kong: Hang Seng seen opening 1.7% lower.
    29. Markets: Brent $88.72, gold $3,744 overnight. 30. Redmond:
    Microsoft in AI talks with ByteDance. 31. Cambridge: Evidence yet
    of life on K2-18b. 32. Space: Sugar found drifting between the
    stars. 33. Space: Webb finds new chemicals on Charon. 34. Science:
    Earth lost a billion years of history. 35. Health: Bacterial toxin
    tied to bowel cancer. 36. Shenzhen: Trump–Putin bilateral also set
    today. 37. Shenzhen: Trump–Xi talks on chips, rare earths.
    38. Shenzhen: No word on Trump–Kim meeting. 39. The Hague: Fears
    of US sanctions on ICJ judges. 40. Wellington: NZ minister
    'aghast' at Australia. 41. Wellington: Kiwis may decide NZ
    election. 42. Paris: Minister says Mélenchon could win.

## Date check — what was deliberately left out

The EU's €45bn Ukraine loan, Jeffries' Speaker nomination (251–11),
Fed minutes pointing to more hikes, Nvidia's $115.8bn quarter, the
Kerch Bridge collapse, and Iran's drones at Kuwait and Bahrain all
broke before Thursday, so they are named in the DATE CHECK box instead
of presented as Thursday news. The Shenzhen summit's outcome was not
yet known when the page was made.

## How to re-render

```sh
bash tools/build.sh   # renders tools/frontpage.html to assets/entry.png
python3 check_entry.py  # runs main.py twice, asserts 1024x1024 PNG < 1 MiB, deterministic
```

`main.py` is Python 3.13, standard library only. It copies the held
`assets/entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png` (default
`/output/entry.png`).
