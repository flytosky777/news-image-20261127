#!/usr/bin/env python3
"""Fetch illustrative photos from Wikimedia Commons for the 27 Nov 2026
news front page. Writes one .jpg per topic into assets/."""
import json
import os
import urllib.request
import urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, "assets")
os.makedirs(ASSETS, exist_ok=True)

API = "https://commons.wikimedia.org/w/api.php"
UA = {"User-Agent": "makefun-news-image-entry/1.0 (contact: builder)"}

QUERIES = {
    "hero.jpg": "Shahed 136 drone",
    "gaza.jpg": "Gaza City skyline",
    "parade.jpg": "Macy's Thanksgiving Day Parade balloon",
    "tanker.jpg": "oil tanker ship sea",
    "london.jpg": "Palace of Westminster London",
    "court.jpg": "Palais de Justice Paris",
}


def search_thumb(query, width=900):
    params = {
        "action": "query",
        "format": "json",
        "generator": "search",
        "gsrsearch": query + " filetype:bitmap",
        "gsrnamespace": 6,
        "gsrlimit": 8,
        "prop": "imageinfo",
        "iiprop": "url|size|mime",
        "iiurlwidth": width,
    }
    req = urllib.request.Request(
        API + "?" + urllib.parse.urlencode(params), headers=UA)
    with urllib.request.urlopen(req, timeout=30) as r:
        data = json.load(r)
    pages = data.get("query", {}).get("pages", {})
    out = []
    for p in pages.values():
        ii = p.get("imageinfo", [{}])[0]
        if ii.get("mime") in ("image/jpeg", "image/png") and ii.get("width", 0) >= 600:
            out.append((p["title"], ii.get("thumburl") or ii.get("url"), ii["width"], ii["height"]))
    return out


def download(url, dest):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as r:
        data = r.read()
    with open(dest, "wb") as f:
        f.write(data)
    return len(data)


for name, q in QUERIES.items():
    dest = os.path.join(ASSETS, name)
    if os.path.exists(dest):
        print(f"{name}: already present")
        continue
    cands = search_thumb(q)
    print(f"{name} ({q}): {len(cands)} candidates")
    for title, url, w, h in cands:
        print(f"  - {title} {w}x{h}")
    if not cands:
        print(f"  !! no candidate for {name}")
        continue
    title, url, w, h = cands[0]
    n = download(url, dest)
    print(f"  => {title} -> {dest} ({n} bytes)")
