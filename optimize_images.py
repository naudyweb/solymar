"""Generate responsive WebP variants for the site's photos.

For every source image listed in SOURCES, writes img/w/<name>-<width>.webp at
each width in WIDTHS (never upscaling; the original width is always included).
Pages reference them through `srcset` (see generate_pages.py `img_attrs` and the
hand-written pages). Re-run after adding or replacing a photo:

    python3 optimize_images.py
"""
import os
from PIL import Image

WIDTHS = (480, 960, 1600)
QUALITY = 76
OUT_DIR = "img/w"
SOURCES = [
    "img/adrenarena.jpg", "img/atv-gokart.jpg", "img/ballestas-y-reserva-full-day.jpg",
    "img/bicicleta-reserva-paracas.jpg", "img/buceo.jpg", "img/caminata-paracas.jpg",
    "img/huacachina.jpg", "img/islas-ballestas.jpg", "img/kayak-paddle.jpg",
    "img/parapente.jpg", "img/reserva-nacional-paracas.jpg", "img/ruta-del-pisco.jpg",
    "img/scooter-reserva-paracas.png", "img/tambo-colorado.jpg", "img/trekking.jpg",
    "img/yakupark.jpg",
]


def variant_widths(original_width):
    widths = sorted({w for w in WIDTHS if w < original_width} | {min(original_width, max(WIDTHS))})
    return widths


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    for src in SOURCES:
        name = os.path.splitext(os.path.basename(src))[0]
        with Image.open(src) as im:
            im = im.convert("RGB")
            for w in variant_widths(im.width):
                out = os.path.join(OUT_DIR, f"{name}-{w}.webp")
                if os.path.exists(out) and os.path.getmtime(out) >= os.path.getmtime(src):
                    continue
                h = round(im.height * w / im.width)
                im.resize((w, h), Image.LANCZOS).save(out, "WEBP", quality=QUALITY, method=6)
                print(f"{out}  {os.path.getsize(out) // 1024} KB")


if __name__ == "__main__":
    main()
