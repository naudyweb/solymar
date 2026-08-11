# -*- coding: utf-8 -*-
import datetime

# Clean URLs (without .html extension) for all pages
tours_keys = [
    "islas-ballestas",
    "reserva-nacional-paracas",
    "ballestas-y-reserva-full-day",
    "buggies-sandboard-huacachina",
    "ruta-del-pisco-bodegas-ica",
    "paracas-huacachina-full-day",
    "sobrevuelo-lineas-de-nazca",
    "parapente",
    "buceo",
    "kayak-paddle-paracas",
    "mini-buggies-paracas",
    "tambo-colorado",
    "yakupark-paracas",
    "trekking",
    "adrenarena",
    "transporte-personalizado"
]

other_pages = [
    {"es": "", "en": "en/", "priority": "1.0"},
    {"es": "tours", "en": "en/tours", "priority": "0.8"},
    {"es": "blog/", "en": "en/blog/", "priority": "0.8"},
    {"es": "blog/lima-a-paracas", "en": "en/blog/lima-a-paracas", "priority": "0.8"}
]

# Generate XML entries
today = datetime.date.today().strftime("%Y-%m-%d")

xml_content = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xhtml="http://www.w3.org/1999/xhtml">
"""

# Helper to format URL entry
def make_entry(loc, alt_es, alt_en, alt_x, priority):
    return f"""  <url>
    <loc>{loc}</loc>
    <xhtml:link rel="alternate" hreflang="es" href="{alt_es}"/>
    <xhtml:link rel="alternate" hreflang="en" href="{alt_en}"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="{alt_x}"/>
    <lastmod>{today}</lastmod>
    <priority>{priority}</priority>
  </url>
"""

# Other pages
for page in other_pages:
    alt_es = f"https://solymarparacas.com/{page['es']}"
    alt_en = f"https://solymarparacas.com/{page['en']}"
    alt_x = alt_es
    
    # Spanish entry
    xml_content += make_entry(alt_es, alt_es, alt_en, alt_x, page["priority"])
    # English entry
    xml_content += make_entry(alt_en, alt_es, alt_en, alt_x, page["priority"])

# Tours pages
for key in tours_keys:
    alt_es = f"https://solymarparacas.com/{key}"
    alt_en = f"https://solymarparacas.com/en/{key}"
    alt_x = alt_es
    
    # Spanish entry
    xml_content += make_entry(alt_es, alt_es, alt_en, alt_x, "0.8")
    # English entry
    xml_content += make_entry(alt_en, alt_es, alt_en, alt_x, "0.8")

xml_content += "</urlset>\n"

with open("sitemap.xml", "w", encoding="utf-8") as f:
    f.write(xml_content)

print("sitemap.xml successfully generated and updated!")
