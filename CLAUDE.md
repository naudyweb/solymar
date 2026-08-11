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

**Deploy the reservas subsite (separate FTP target):**
```bash
bash upload_reservas.sh
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
- Custom theme tokens (defined in `src/input.css`): `primary`, `primary-container`, `secondary`, `tertiary`, `surface`, `surface-container`, `surface-container-low`, `on-surface`, `on-surface-variant`. Always use these tokens instead of arbitrary colors.

### Page Generation
`generate_pages.py` is the source of truth for all tour pages. It contains structured data (titles, descriptions, prices, FAQ, schema.org markup) for each tour in both languages and renders them into HTML files. **Edit tour content in `generate_pages.py`, then re-run it** — don't edit generated HTML files by hand for content changes.

### Deployment
`upload.sh` syncs the working directory to `/public_html` on the FTP server using `lftp --only-newer`. It excludes dev files (`node_modules/`, `src/`, `.git/`, `generate_*.py`, etc.). The script contains FTP credentials — do not commit changes to those credentials.

### URL Rewriting
`.htaccess` strips `.html` extensions from public URLs (e.g., `/snorkel` → `snorkel.html`). Internal HTML links still use `.html` extensions so they work on the local dev server too. Permanent redirects for retired pages (e.g., `atv-gokart` → `mini-buggies-paracas`) are managed in `.htaccess`.

### Reservas subsite (internal booking/voucher tool)
`reservas/` is a self-contained PHP app deployed separately to the **reservas.solymarparacas.com** subdomain (its own document root — not a subfolder of the public site). It is staff-only (single shared password) and lets the team create a reservation for any tour on the live site, then generate/download a bilingual PDF voucher, and search past reservations.

- **Data model**: SQLite via PDO (`reservas/db.php`), file at `reservas/data/reservas.sqlite` (gitignored — created on first run, lives only on the server, never synced by deploy).
- **Tour catalog**: `export_tours_json.py` reads the `tours` dict straight out of `generate_pages.py` (via `ast.literal_eval`, without importing/executing the file — importing it would regenerate the whole site as a side effect) and writes `reservas/tours.json`. Re-run it whenever tours change in `generate_pages.py`, then redeploy `reservas/`.
- **Auth**: one shared password, hashed with `password_hash()` in `reservas/config.php` (gitignored — copy `reservas/config.sample.php` and follow its instructions to generate the hash). Session-based (`reservas/auth.php`).
- **PDF**: generated client-side with a vendored copy of `html2pdf.js` (`reservas/js/html2pdf.bundle.min.js`, no CDN) rendering the styled `#voucher` div from `reservas/voucher.php`.
- **Styling**: its own Tailwind build (`reservas/src/input.css` → `reservas/css/style.css`) and its own copy of the logo (`reservas/img/`), so the subsite has no runtime dependency on files outside `reservas/`.
- **Deployment**: `upload_reservas.sh` (gitignored, contains credentials — fill in `FTP_USER`/`FTP_PASS`/`REMOTE_DIR` once the subdomain exists in the hosting panel) mirrors `reservas/` to the subdomain's document root, always excluding `data/` and `config.php` so a deploy never overwrites live reservations or the production password.
- The main `upload.sh` explicitly excludes `reservas/` so the internal tool and its customer data are never pushed to the public site's document root.
