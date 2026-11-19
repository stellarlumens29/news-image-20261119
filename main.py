#!/usr/bin/env python3
"""news-image-20261119 — "Thursday 19 November 2026: 42 stories,
6 continents, one front page and a map, date-checked".

A code-drawn editorial broadsheet, not a generated picture: the front page
is laid out in HTML/CSS (tools/frontpage.html, Noto Serif Display + Noto
Sans) and rendered to a 1024x1024 PNG with a headless browser. This
program copies the held image to $MAKEFUN_OUTPUT_DIR/entry.png (default
/output/entry.png).

Deterministic: no randomness, no time, no network — two runs write
identical bytes. The image is 1024x1024, ~363 KiB, under the 1 MiB gate.

Design (studied from the winning entries of news-image-20261117 and
news-image-20261118, whose full-size images were read before building):
a navy masthead band with the date as the dominant title; a region count
bar and a by-field count bar; a "day in numbers" strip; a UTC timeline;
3 big illustrated leads and 10 small illustrated cards (13 illustrated
panels, every one drawn in code as flat SVG — no AI imagery); a dotted
world map with numbered pins; 29 one-line briefs; and a DATE CHECK box
naming the big stories deliberately left out because they broke before
Thursday. 42 stories, all verified against live sources for 19 Nov 2026.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "assets", "entry.png")


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dst)
    print(f"wrote {dst} ({os.path.getsize(dst)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
