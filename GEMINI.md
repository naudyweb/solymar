# SolyMar Paracas - Project Overview

SolyMar Paracas is a static website for a tourism agency based in Paracas, Peru. The site showcases various adventure activities including diving, snorkeling, trekking, paragliding, and more.

## Technologies
- **Frontend:** HTML5, Tailwind CSS v4
- **Fonts:** Manrope (Google Fonts)
- **Icons:** Material Symbols Outlined
- **Interactivity:** Vanilla JavaScript (modular components in `/js/`)
- **Assets:** Images hosted locally in `/img/` and optimized (WebP)

## Project Structure
- `/*.html`: Individual Spanish pages for the home screen and activities.
- `/en/*.html`: English versions of all pages.
- `/blog/*.html`: Blog articles and index (Spanish).
- `/en/blog/*.html`: Blog articles and index (English).
- `/css/`:
    - `style.css`: Compiled Tailwind CSS v4 bundle.
- `/js/`:
    - `header.js`: Dynamic header injection with language detection and mobile menu logic.
    - `footer.js`: Dynamic footer injection with language switcher and floating WhatsApp button.
- `/src/`:
    - `input.css`: Tailwind CSS source file.

## Building and Running
This project uses Tailwind CSS v4.
- **Development:** To watch CSS changes, run:
  - `npx tailwindcss -i ./src/input.css -o ./css/style.css --watch`
- **Static Server:** 
  - `npx serve .`
  - `python3 -m http.server`

## Development Conventions
- **CSS Naming:** Tailwind utility classes are preferred.
- **Responsive Design:** Mobile-first approach using Tailwind breakpoints (`md:`, `lg:`).
- **Navigation:** The header and footer are injected dynamically via `/js/header.js` and `/js/footer.js`. Any global changes should be made there.
- **Language Support:** Detection is based on the URL path (`/en/` segments). Links in the header and footer are automatically adjusted.
- **External Links:** WhatsApp booking links and social media links are managed in `/js/footer.js`.
