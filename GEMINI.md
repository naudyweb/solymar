# SolyMar Paracas - Project Overview

SolyMar Paracas is a static website for a tourism agency based in Paracas, Peru. The site showcases various adventure activities including diving, snorkeling, trekking, paragliding, and more.

## Technologies
- **Frontend:** HTML5, Vanilla CSS3
- **Fonts:** Manrope (Google Fonts)
- **Icons:** Material Symbols Outlined
- **Interactivity:** Vanilla JavaScript (embedded in HTML files)
- **Assets:** Images are primarily hosted on external services (Unsplash, Google User Content)

## Project Structure
- `/*.html`: Individual pages for the home screen and each specific activity.
- `/css/`:
    - `base.css`: Shared variables, resets, and common component styles (header, footer).
    - `[page].css`: Desktop-specific styles for a given page.
    - `[page]-tablet.css`: Tablet-specific media queries and adjustments.
    - `[page]-mobile.css`: Mobile-specific media queries and adjustments.

## Building and Running
This is a pure static project and does not require a build step.
- **Development:** Open `index.html` directly in a browser or use a simple static server:
  - `npx serve .`
  - `python3 -m http.server`
- **Deployment:** The entire root directory can be served by any static web host.

## Development Conventions
- **CSS Naming:** Follows a BEM-inspired convention (e.g., `.header__container`, `.activity-card__title`).
- **Responsive Design:** Styles are modularized by device type. When modifying layout, ensure changes are reflected or accounted for in the corresponding `-tablet.css` and `-mobile.css` files.
- **Navigation:** The header and footer are duplicated across HTML files. Any change to the navigation menu must be synchronized across all `.html` files.
- **External Links:** WhatsApp booking links and social media links are hardcoded in the HTML; verify the phone numbers and handles if updates are needed.
