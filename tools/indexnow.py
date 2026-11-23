#!/usr/bin/env python3
"""Notify IndexNow (Bing, Yandex, Seznam, Naver...) about changed URLs.

Usage:  python3 tools/indexnow.py https://thorcast.ai/es.html [more URLs...]
        python3 tools/indexnow.py --sitemap      (every URL in sitemap.xml)
The key below is public by design: it must also be served at
https://thorcast.ai/6adc77f692f969f56a1ba26b6d2a0bdd.txt so search engines can verify site ownership.
"""
import json, re, sys, urllib.request
from pathlib import Path

KEY = "6adc77f692f969f56a1ba26b6d2a0bdd"
HOST = "thorcast.ai"

def main(argv):
    if argv == ["--sitemap"]:
        urls = re.findall(r"<loc>([^<]+)</loc>", (Path(__file__).resolve().parent.parent / "sitemap.xml").read_text())
    else:
        urls = argv
    if not urls:
        sys.exit(__doc__)
    body = json.dumps({"host": HOST, "key": KEY, "keyLocation": f"https://{HOST}/{KEY}.txt", "urlList": urls}).encode()
    req = urllib.request.Request("https://api.indexnow.org/indexnow", data=body, headers={"Content-Type": "application/json; charset=utf-8"})
    with urllib.request.urlopen(req, timeout=30) as r:
        print(r.status, len(urls), "URLs submitted")

if __name__ == "__main__":
    main(sys.argv[1:])
