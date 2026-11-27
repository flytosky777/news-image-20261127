[![news-image-20261127](https://make.fun/badge/news-image-20261127.svg)](https://make.fun/bounty/news-image-20261127)
[![rank](https://make.fun/badge/news-image-20261127/flytosky777/news-image-20261127/rank.svg)](https://make.fun/bounty/news-image-20261127)
[![reward](https://make.fun/badge/news-image-20261127/flytosky777/news-image-20261127/reward.svg)](https://make.fun/bounty/news-image-20261127)

# The World in One Day — Friday 27 November 2026

A newspaper front page summing up 27 November 2026's world news in one
1024×1024 image, built for the make.fun `news-image-20261127` bounty.

## Stories

1. **Iran drone strike on Kuwait kills two Italian workers** (headline) —
   two Italian workers are killed in a drone attack on Kuwait; Iran denies
   responsibility. Sources: NYT, BBC, NDTV.
2. **Israel kills 10 in Gaza as Hamas weighs reply** — ten people are killed
   in Israeli strikes; Hamas considers its response. Source: Reuters.
3. **Thanksgiving storm delays Macy's parade** — the parade is postponed for
   the first time; 500,000 homes lose power, 1,000+ flights cancelled.
   Sources: BBC, iHeart.
4. **Tanker capsizes off Ibiza, one dead** — a tanker carrying 7,000 tonnes
   of diesel overturns near Ibiza; one crew member dies. Source: BBC.
5. **UK net migration lowest since 1997** — net migration falls to its
   lowest since 1997, apart from the pandemic years. Source: NYT.
6. **Depardieu to stand trial over 2018 rape claim** — the actor will face
   trial over an alleged 2018 rape of an actress. Source: BBC.

Photos are illustrative, from Wikimedia Commons. The page is drawn by
`build_frontpage.py` (Python + Pillow); `main.ts` copies the finished
`entry.png` to `/output/entry.png`, byte-identical on every run. The
photos were fetched from Commons by `fetch_assets.py` at build time;
the entry itself uses no network.

## Reproduce

```sh
python3 build_frontpage.py   # writes entry.png (1024x1024, < 1 MiB)
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```
