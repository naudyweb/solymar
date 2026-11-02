# SolyMar Paracas — Guía del Proyecto (`GEMINI.md`)

Sitio web estático bilingüe (español/inglés) para la agencia de turismo y aventura **SolyMar Paracas** en Paracas, Perú (`https://solymarparacas.com`).

---

## Tecnologías y Activos
- **Frontend:** HTML5 semántico, Tailwind CSS v4 (`src/input.css` → `css/style.css` minificado).
- **Tipografía e Iconos (Autoalojados):**
  - Fuente **Inter** (pesos 300–600): `css/fonts/inter-latin.woff2` y `css/fonts/inter-latin-ext.woff2` con `font-display: swap`.
  - Iconos **Material Symbols Outlined**: subset WOFF2 autoalojado en `css/fonts/material-symbols-outlined.woff2` (~10.5 KB, generado automáticamente por `update_icon_font.py` con solo los iconos usados en el sitio y `font-display: swap`).
  - **Importante:** No usar enlaces externos a `fonts.googleapis.com` ni `fonts.gstatic.com`.
- **Interactividad:** JavaScript Vanilla modular en `/js/` cargado siempre con atributo `defer`.
- **Imágenes:** Originales en `/img/` y variantes responsivas WebP en `/img/w/` (`480w`, `680w`, `960w`, `1264w`, `1600w`, calidad `68`).

---

## Estructura del Proyecto
- `/*.html`: Páginas en español (inicio, índice de tours y 15 páginas de actividades).
- `/en/*.html`: Versiones espejo en inglés de todas las páginas.
- `/blog/*.html` y `/en/blog/*.html`: Artículos e índice del blog en español e inglés.
- `/src/input.css`: Fuente de Tailwind CSS v4, tokens de color (tema claro/oscuro), reglas `@font-face` y animaciones.
- `/css/`:
  - `style.css`: Bundle compilado y minificado de Tailwind CSS v4.
  - `fonts/`: Fuentes WOFF2 autoalojadas (`inter-latin.woff2`, `inter-latin-ext.woff2`, `material-symbols-outlined.woff2`).
- `/js/`:
  - `header.js`: Inyección dinámica del `<header>` (menú "Experiencias" por categorías, selector de idioma `ES`/`EN`, selector de tema claro/oscuro y CTA de reserva).
  - `footer.js`: Inyección dinámica del `<footer>`, botón flotante de WhatsApp y carga diferida de Google Analytics (`gtag.js`).
  - `hero-slider.js`: Carrusel cross-fade con efecto Ken Burns para las tarjetas de fotos del hero.
- **Scripts de construcción y mantenimiento:**
  - `generate_pages.py`: Fuente de verdad que genera las 30 páginas de tours (`/*.html` y `/en/*.html`) y los índices `tours.html` / `en/tours.html`.
  - `optimize_images.py`: Genera las variantes WebP responsivas en `img/w/`.
  - `update_icon_font.py`: Escanea todos los `.html`, `.js` y `.py` para descargar en `css/fonts/material-symbols-outlined.woff2` únicamente los glifos utilizados.
  - `generate_sitemap.py`: Genera `sitemap.xml`.
  - `dev_server.py`: Servidor local que resuelve URLs limpias (`/tours` → `tours.html`) igual que `.htaccess` en producción.
  - `upload.sh`: Despliegue incremental por FTPS (`lftp mirror`) mediante lista blanca hacia `/public_html`.

---

## Comandos de Construcción y Despliegue

```bash
# 1. Regenerar variantes WebP (480w, 680w, 960w, 1264w, 1600w) al añadir/cambiar fotos
python3 optimize_images.py

# 2. Regenerar todas las páginas de tours e índices (ES/EN)
python3 generate_pages.py

# 3. Actualizar subset de iconos Material Symbols en css/fonts/material-symbols-outlined.woff2
python3 update_icon_font.py

# 4. Compilar y minificar Tailwind CSS v4 para producción
npx tailwindcss -i ./src/input.css -o ./css/style.css --minify

# 5. Desarrollo local (watch de CSS + servidor con URLs limpias)
npx tailwindcss -i ./src/input.css -o ./css/style.css --watch
python3 dev_server.py

# 6. Previsualizar y desplegar a producción por FTPS
bash upload.sh --dry-run
bash upload.sh
```

---

## Convenciones de Desarrollo

1. **Páginas generadas vs. manuales:**
   - **Generadas (`generate_pages.py`):** Todas las páginas individuales de tours y `tours.html` / `en/tours.html`. Nunca editar sus `.html` directamente; modificar `generate_pages.py` y ejecutar `python3 generate_pages.py`.
   - **Manuales:** `index.html`, `en/index.html`, `blog/*.html` y `en/blog/*.html`.
2. **Invalidación de caché (`ASSET_VERSION`):**
   - `.htaccess` cachea CSS y JS por 1 mes y fuentes WOFF2 por 1 año.
   - Al modificar `css/style.css` o cualquier archivo en `js/*.js`, incrementar `ASSET_VERSION` (p. ej. `2026110201`) en `generate_pages.py` y actualizar el parámetro `?v=` en las páginas manuales (`index.html`, `en/index.html`, `blog/*.html`, `en/blog/*.html`).
3. **Sistema de diseño ("Raus") y Modo Oscuro:**
   - Usar siempre los tokens semánticos definidos en `src/input.css`: `bg-surface`, `bg-surface-container`, `bg-surface-container-low`, `bg-secondary-container`, `text-on-surface`, `text-on-surface-variant`, `text-primary`, `bg-tertiary`, `text-on-tertiary`, y radios `rounded-chip`, `rounded-card`, `rounded-hero`.
   - Cada página incluye en `<head>` el script inline que aplica `data-theme="light|dark"` desde `localStorage` antes del primer pintado.
4. **URLs limpias:**
   - Todos los enlaces internos se escriben sin extensión `.html` (`islas-ballestas`, `tours`, `blog/`).

---

## Optimizaciones PageSpeed Insights y Accesibilidad (Reglas Obligatorias)

Para mantener el rendimiento en móvil y escritorio según las auditorías de Google Lighthouse:

1. **Cero recursos bloqueantes externos (`render-blocking-insight`, `font-display-insight`, `cache-insight`):**
   - Todas las fuentes (`Inter` y `Material Symbols Outlined`) se sirven localmente desde `css/fonts/*.woff2` referenciadas en `src/input.css` con `font-display: swap`.
   - `.material-symbols-outlined` tiene dimensiones fijas (`width: 1em; height: 1em; overflow: hidden`) para evitar CLS durante la carga de iconos.
   - Todos los `<script src="...">` (`header.js`, `footer.js`, `hero-slider.js`) deben llevar el atributo `defer`.
2. **Priorización del elemento LCP y Hero Slider (`image-delivery-insight`, `lcp-discovery`):**
   - La primera imagen del hero (`<img class="hero-slide is-active">`) lleva `fetchpriority="high" decoding="async"`, `width="1264" height="848"` y su correspondiente `<link rel="preload" as="image" imagesrcset="..." imagesizes="..." fetchpriority="high" />` en el `<head>`.
   - Todas las diapositivas secundarias del `.hero-slider` (`idx > 0`) y cualquier segundo slider en la página llevan obligatoriamente `loading="lazy" decoding="async"`.
   - En `src/input.css`, `.hero-slide:not(.is-active)` permanece con `display: none` hasta que `js/hero-slider.js` añade la clase `.is-ready` `1500ms` después de `window.load` (omitiendo además sliders ocultos con `offsetParent === null`), evitando que imágenes secundarias o de escritorio se descarguen en móvil durante el LCP.
   - El logo del header (`img/SolyMar-web.webp`) **no** debe usar `fetchpriority="high"` para no competir en ancho de banda con la imagen LCP.
3. **Imágenes responsivas (`680w`) y atributos `sizes` precisos:**
   - `optimize_images.py` genera los anchos `(480, 680, 960, 1264, 1600)` con `QUALITY = 68`. El corte de `680w` es crítico para pantallas móviles (`412px` CSS × `1.75` DPR = `665px` reales en contenedores con padding `px-4`).
   - Usar `sizes` acordes al ancho real renderizado:
     - Hero principal: `(min-width: 1024px) 58vw, calc(100vw - 2rem)`
     - Tarjetas de experiencias en inicio (carrusel móvil `w-[82%] sm:w-[60%]`): `(min-width: 1024px) 66vw|33vw, (min-width: 768px) 50vw, (min-width: 640px) 60vw, 82vw`
     - Miniaturas del blog en inicio (`104px` en móvil, `220px` en `sm:`): `(min-width: 640px) 220px, 104px`
     - Artículos del blog (`max-w-[760px]`): `(min-width: 800px) 760px, calc(100vw - 2rem)`
4. **Scripts de terceros diferidos (`unused-javascript`):**
   - `gtag.js` (`G-557963487`) en `js/footer.js` se inyecta únicamente tras la primera interacción del usuario (`pointerdown`, `touchstart`, `scroll`, `keydown`) o como respaldo `5500ms` después de `window.load`.
5. **Accesibilidad WCAG 2.5.3 (`label-content-name-mismatch`):**
   - Si un botón o enlace tiene texto visible (como el selector de idioma `EN` / `ES` en `js/header.js`), su `aria-label` debe comenzar con ese mismo texto visible (`EN — Switch to English` / `ES — Cambiar a Español`).
