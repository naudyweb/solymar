# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

SolyMar Paracas is a bilingual (Spanish/English) static website for a tourism agency in Paracas, Peru. Production domain: **solymarparacas.com**. Deployed via FTP to a shared hosting server.

## Commands

**Compile CSS (watch mode during development):**
```bash
npx tailwindcss -i ./src/input.css -o ./css/style.css --watch
```

**Build CSS (one-time):**
```bash
npx tailwindcss -i ./src/input.css -o ./css/style.css
```

**Run local dev server:**
```bash
python3 -m http.server
```

**Generate tour pages from templates:**
```bash
python3 generate_pages.py
```

**Generate sitemap:**
```bash
python3 generate_sitemap.py
```

**Deploy to production (FTP sync via lftp):**
```bash
bash upload.sh
```

**Export tour catalog for the reservas subsite:**
```bash
python3 export_tours_json.py
```

**Compile CSS for the reservas subsite:**
```bash
npx tailwindcss -i ./reservas/src/input.css -o ./reservas/css/style.css
```

**Deploy the reservas subsite (separate FTP target, /public_html/reservas):**
```bash
bash upload_reservas.sh   # falls back to `python upload_reservas.py` if lftp isn't installed
```

## Architecture

### Bilingual Structure
- `/*.html` — Spanish pages (root)
- `/en/*.html` — English mirror pages
- `/blog/*.html` — Spanish blog articles
- `/en/blog/*.html` — English blog articles

Language detection happens at runtime in JS based on whether `/en/` appears in `window.location.pathname`.

### Dynamic Header & Footer
Every page contains two placeholders:
- `<div id="header-placeholder"></div>` — filled by `js/header.js`
- `<div class="footer"></div>` — filled by `js/footer.js`

Both scripts detect the current language and path depth to compute correct relative URLs (`rootPath`, `baseNavPath`). **All global nav changes must be made in these JS files**, not in individual HTML pages.

### CSS / Tailwind v4
- Source: `src/input.css` — defines the theme (color tokens, font) and scans `**/*.html` and `js/**/*.js` for class usage.
- Output: `css/style.css` — compiled bundle committed to the repo and served directly.
- Custom theme tokens (defined in `src/input.css`): `primary`, `primary-container`, `secondary`, `tertiary`, `tertiary-container`, `on-tertiary`, `surface`, `surface-container`, `surface-container-low`, `on-surface`, `on-surface-variant`, `sand`. Always use these tokens instead of arbitrary colors.
- Visual identity ("desierto + Humboldt"): `tertiary` (flamingo) is the only UI accent and is reserved for prices and booking buttons; every booking CTA uses the same label ("Reservar por WhatsApp" / "Book on WhatsApp"). Headings use the `font-display` utility (Archivo at 125% width, loaded from Google Fonts with the `wdth` axis). Radius rule: photos and panels `rounded-sm`, interactive buttons `rounded-full`. No uppercase eyebrow labels above headings.
- Motion lives in `src/input.css` (`rise-in`, `candelabro-draw`) and is gated behind `prefers-reduced-motion`.

### Page Generation
`generate_pages.py` is the source of truth for all tour pages. It contains structured data (titles, descriptions, prices, FAQ, schema.org markup) for each tour in both languages and renders them into HTML files. **Edit tour content in `generate_pages.py`, then re-run it** — don't edit generated HTML files by hand for content changes.

### Deployment
`upload.sh` syncs the working directory to `/public_html` on the FTP server using `lftp --only-newer`. It excludes dev files (`node_modules/`, `src/`, `.git/`, `generate_*.py`, etc.). The script contains FTP credentials — do not commit changes to those credentials.

### URL Rewriting
`.htaccess` strips `.html` extensions from public URLs (e.g., `/snorkel` → `snorkel.html`). Internal HTML links still use `.html` extensions so they work on the local dev server too. Permanent redirects for retired pages (e.g., `atv-gokart` → `mini-buggies-paracas`) are managed in `.htaccess`.

Two rules exist only because of the `reservas` subdomain (see below) — do not remove them as dead code:
- The canonical-domain redirect (`HTTP_HOST !^solymarparacas\.com$` → redirect) explicitly excludes `reservas.solymarparacas.com`, otherwise it would force-redirect the subdomain to the main site.
- A rule blocks (`403`) `/reservas/*` when the host is `solymarparacas.com`, because that folder is also reachable that way (it lives inside `public_html`, see below).

### Reservas subsite (internal booking/voucher tool)
`reservas/` is a self-contained PHP app for **reservas.solymarparacas.com**. In practice the hosting panel created that subdomain's document root as `public_html/reservas` — a subfolder of the main site's hosting account, not a truly separate root — which is why the main `.htaccess` needs the two reservas-specific rules described above. It is staff-only (single shared password) and lets the team create a reservation for any tour on the live site, then generate/download a bilingual PDF voucher, and search past reservations.

- **Data model**: SQLite via PDO (`reservas/db.php`), file at `reservas/data/reservas.sqlite` (gitignored — created on first run, lives only on the server, never synced by deploy).
- **Schema migrations**: `reservas_migrate()` in `db.php` adds new columns with `ALTER TABLE ADD COLUMN` (checking `PRAGMA table_info` first) instead of recreating the table, because production already has real reservations saved. Any future schema change must follow this same non-destructive pattern.
- **Tour catalog**: `export_tours_json.py` reads the `tours` dict straight out of `generate_pages.py` (via `ast.literal_eval`, without importing/executing the file — importing it would regenerate the whole site as a side effect) and writes `reservas/tours.json`. Re-run it whenever tours change in `generate_pages.py`, then redeploy `reservas/`.
- **Auth**: one shared password, hashed with `password_hash()` in `reservas/config.php` (gitignored — copy `reservas/config.sample.php` and follow its instructions to generate the hash). Session-based (`reservas/auth.php`). The host has no SSH access, so to (re)generate the hash: temporarily upload a minimal PHP script that calls `password_hash($_POST['password'], PASSWORD_DEFAULT)` and prints the result, use it once from the browser, then delete it from the server immediately — never leave it deployed.
- **Pick-up location / mini-map**: `reservas/maps.php` extracts coordinates from whatever the staff pastes into the pick-up field — bare coordinates, a URL with `@lat,lng`, `?q=`/`?ll=` params, or a shortened `maps.app.goo.gl` link (resolved by following its redirect with curl). The voucher's mini-map uses the Google Maps Static API, keyed by `GOOGLE_MAPS_STATIC_API_KEY` in `config.php` (restrict it by HTTP referrer to the domain and by API to "Maps Static API"). If no coordinates can be parsed, the voucher still shows a "View on Google Maps" link without the image.
- **PDF**: generated client-side with a vendored copy of `html2pdf.js` (`reservas/js/html2pdf.bundle.min.js`, no CDN) rendering the styled `#voucher` div from `reservas/voucher.php`.
- **Styling**: its own Tailwind build (`reservas/src/input.css` → `reservas/css/style.css`) and its own copy of the logo (`reservas/img/`), so the subsite has no runtime dependency on files outside `reservas/`.
- **Deployment**: `upload_reservas.sh` (gitignored, contains credentials) mirrors `reservas/` to `/public_html/reservas` using the same VPS FTP credentials as the main site, always excluding `data/*.sqlite` and `config.php` so a deploy never overwrites live reservations or the production password. `upload_reservas.py` (also gitignored) is a `ftplib`-based fallback for when `lftp` isn't installed, mirroring the `upload.py` fallback for the main site.
- The main `upload.sh`/`upload.py` explicitly exclude `reservas/` so the internal tool and its customer data are never pushed to the public site's document root.
