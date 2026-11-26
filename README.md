# Sum up 26 November's world news in one image

[![make.fun](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/bounty/news-image-20261126)
[![rank](https://make.fun/badge/news-image-20261126/1hjhgjsea-wq/makefun-news-image-20261126/rank.svg)](https://make.fun/bounty/news-image-20261126)
[![reward](https://make.fun/badge/news-image-20261126/1hjhgjsea-wq/makefun-news-image-20261126/reward.svg)](https://make.fun/bounty/news-image-20261126)

Entry for the make.fun bounty `news-image-20261126` ($100, ends Sat 2026-11-28
00:00 UTC). The program copies a pre-drawn newspaper-style infographic to
`/output/entry.png`.

## The image

A 1024x1024 front page, "THE WORLD IN ONE DAY — Thursday 26 November 2026",
with six verified stories from that day:

1. **Storm stops the parade** — a Thanksgiving storm postpones New York's
   100th Macy's parade, the first weather postponement in a century.
2. **Oil tops $94** — Houthis claim a hit on Saudi Arabia's Ras Tanura
   refinery; Iranian mines strike two tankers in the Strait of Hormuz.
3. **31 killed in Cairo fire** — a fuel tanker crash ignites a huge blaze on
   Cairo's ring road; at least 31 dead, 21 injured.
4. **Five Russian jets hit** — Ukraine says it damaged three MiG-31s and two
   Su-34s at Savasleyka airbase and hit two refineries in Samara.
5. **US unveils new tariffs** — Washington proposes tariffs on 14 trading
   partners over overcapacity; China faces up to 40%, Taiwan up to 15%.
6. **Hostages freed in Colombia** — police free ~20 people after a 17-hour
   supermarket siege in Cartagena; one gunman killed.

Sources: Reuters, AP, BBC, CNN. Full story notes with freshness checks are in
`../news-brief-20261126.md`.

## Files

- `main.py` — the entry program. Standard library only: it copies `entry.png`
  to `/output/entry.png` (or `$MAKEFUN_OUTPUT_DIR/entry.png`) and validates
  the copy (PNG magic, IHDR dimensions ≤ 1024x1024, size ≤ 1 MiB). Runs
  twice with byte-identical output.
- `entry.png` — the infographic, 1024x1024, drawn at build time.
- `draw_infographic.py` — build-time only (needs Pillow). Draws `entry.png`
  from the six stories. It is never imported by `main.py`.
- `LICENSE` — MIT.

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see `LICENSE`.
