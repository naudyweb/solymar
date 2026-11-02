"""Subset the Material Symbols font to the icons the site actually uses.

The full variable font is ~4 MB; Google Fonts can serve only the named icons
(`icon_names=`), which is ~11 KB. Scans every page and the header/footer
scripts for `material-symbols-outlined` spans and downloads the subset WOFF2
into `css/fonts/material-symbols-outlined.woff2` so it is self-hosted with a
1-year cache lifetime and zero external render-blocking CSS requests.

Run after `generate_pages.py` whenever an icon is added:

    python3 generate_pages.py && python3 update_icon_font.py
"""
import glob
import os
import re
import urllib.request

PAGES = glob.glob("*.html") + glob.glob("en/*.html") + glob.glob("blog/*.html") + glob.glob("en/blog/*.html")
SCRIPTS = ["js/header.js", "js/footer.js"]
ICON_RE = re.compile(r'material-symbols-outlined[^"]*"[^>]*>\s*([a-z0-9_]+)\s*<')
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
OUT_FONT = "css/fonts/material-symbols-outlined.woff2"


def main():
    icons = set()
    for path in PAGES + SCRIPTS:
        with open(path, encoding="utf-8") as f:
            icons.update(ICON_RE.findall(f.read()))

    url = (
        "https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0,0"
        f"&icon_names={','.join(sorted(icons))}&display=swap"
    )
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    css = urllib.request.urlopen(req).read().decode("utf-8")
    m = re.search(r"url\((https://[^)]+)\)", css)
    if not m:
        raise RuntimeError("Could not find WOFF2 URL in Google Fonts response")

    font_bytes = urllib.request.urlopen(m.group(1)).read()
    os.makedirs(os.path.dirname(OUT_FONT), exist_ok=True)
    with open(OUT_FONT, "wb") as f:
        f.write(font_bytes)

    print(f"{len(icons)} icons -> {OUT_FONT} ({len(font_bytes) / 1024:.1f} KB)")


if __name__ == "__main__":
    main()
