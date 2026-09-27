"""Subset the Material Symbols font to the icons the site actually uses.

The full variable font is ~4 MB; Google Fonts can serve only the named icons
(`icon_names=`), which is a few KB. Scans every page and the header/footer
scripts for `material-symbols-outlined` spans and rewrites the font <link> in
all pages and in generate_pages.py. Run it after generate_pages.py whenever an
icon is added:

    python3 generate_pages.py && python3 update_icon_font.py
"""
import glob
import re

PAGES = glob.glob("*.html") + glob.glob("en/*.html") + glob.glob("blog/*.html") + glob.glob("en/blog/*.html")
SCRIPTS = ["js/header.js", "js/footer.js"]
LINK_RE = re.compile(r'https://fonts\.googleapis\.com/css2\?family=Material\+Symbols\+Outlined[^"]*')
ICON_RE = re.compile(r'material-symbols-outlined[^"]*"[^>]*>\s*([a-z0-9_]+)\s*<')


def main():
    icons = set()
    for path in PAGES + SCRIPTS:
        icons.update(ICON_RE.findall(open(path, encoding="utf-8").read()))
    # Static default instance (opsz 24, wght 400, no fill): the site never varies the axes.
    url = ("https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0,0"
           f"&icon_names={','.join(sorted(icons))}&display=block")
    for path in PAGES + ["generate_pages.py"]:
        text = open(path, encoding="utf-8").read()
        new = LINK_RE.sub(url, text)
        if new != text:
            open(path, "w", encoding="utf-8").write(new)
    print(f"{len(icons)} icons: {', '.join(sorted(icons))}")


if __name__ == "__main__":
    main()
