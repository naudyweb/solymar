# -*- coding: utf-8 -*-
"""
Exporta el catalogo de tours definido en generate_pages.py a reservas/tours.json,
para que la herramienta interna de reservas (PHP) use siempre los mismos datos
que la web publica, sin mantener una segunda copia a mano.

Uso: python3 export_tours_json.py
Se debe correr cada vez que se agrega/edita un tour en generate_pages.py.

Nota: generate_pages.py no tiene un bloque "if __name__ == '__main__':", asi que
un `import generate_pages` normal regeneraria todas las paginas del sitio como
efecto secundario. Para evitar eso, este script lee el archivo fuente y extrae
solo la asignacion literal `tours = {...}` con el modulo ast, sin ejecutar el
resto del archivo.
"""
import ast
import json

with open("generate_pages.py", encoding="utf-8") as f:
    _tree = ast.parse(f.read(), filename="generate_pages.py")

tours = None
for _node in _tree.body:
    if isinstance(_node, ast.Assign) and any(
        isinstance(_t, ast.Name) and _t.id == "tours" for _t in _node.targets
    ):
        tours = ast.literal_eval(_node.value)
        break

if tours is None:
    raise RuntimeError("No se encontro la variable 'tours' en generate_pages.py")

CAT_LABELS = {
    "mar": {"es": "Aventura Marina", "en": "Marine Adventure"},
    "desierto": {"es": "Desierto", "en": "Desert"},
    "aire": {"es": "Actividad Aerea", "en": "Aerial Activity"},
    "cultura": {"es": "Cultura e Historia", "en": "Culture & History"},
    "traslados": {"es": "Traslados Privados", "en": "Private Transfers"},
}
CAT_ORDER = {"mar": 0, "desierto": 1, "aire": 2, "cultura": 3, "traslados": 4}

out = []
for slug, t in tours.items():
    clean_filename = t["filename"].removesuffix(".html")
    out.append({
        "slug": slug,
        "category": t["category"],
        "category_order": CAT_ORDER.get(t["category"], 99),
        "category_label_es": CAT_LABELS.get(t["category"], {}).get("es", t["category"]),
        "category_label_en": CAT_LABELS.get(t["category"], {}).get("en", t["category"]),
        "title_es": t["es"]["h1"],
        "title_en": t["en"]["h1"],
        "price": t["price"],
        "price_val": t["price_val"],
        "price_cur": t["price_cur"],
        "price_options": t.get("price_options", []),
        "quote_only": bool(t.get("quote_only", False)),
        "schedule_es": t["es"].get("schedule_label", ""),
        "schedule_en": t["en"].get("schedule_label", ""),
        "url_es": f"https://solymarparacas.com/{clean_filename}",
        "url_en": f"https://solymarparacas.com/en/{clean_filename}",
    })

out.sort(key=lambda x: (x["category_order"], x["title_es"]))

with open("reservas/tours.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)

print(f"Exportados {len(out)} tours a reservas/tours.json")
