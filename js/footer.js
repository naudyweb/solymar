document.addEventListener("DOMContentLoaded", () => {
    // Detectar idioma basado en la ruta
    const isEn = window.location.pathname.includes('/en/');
    const lang = isEn ? 'en' : 'es';

    // Traducciones del Footer
    const translations = {
        es: {
            description: "Tu agencia de tours personalizados en Paracas. Disfruta de Buceo, Snorkel, ATV, Go Kart, Parapente y Trekking.",
            contact: "Contacto",
            experiences: "Experiencias",
            support: "Soporte",
            faq: "Preguntas Frecuentes",
            about: "Nosotros",
            rights: "© 2026 SolyMar Paracas. Todos los derechos reservados.",
            waText: "Hola%2C+quiero+más+información+sobre+sus+tours",
            waFloatText: "Hola%2C+vengo+de+la+web+y+quiero+información+sobre+los+tours"
        },
        en: {
            description: "Your personalized tour agency in Paracas. Enjoy Diving, Snorkeling, ATV, Go Kart, Paragliding, and Trekking.",
            contact: "Contact",
            experiences: "Experiences",
            support: "Support",
            faq: "FAQ",
            about: "About Us",
            rights: "© 2026 SolyMar Paracas. All rights reserved.",
            waText: "Hello%2C+I+would+like+more+information+about+your+tours",
            waFloatText: "Hello%2C+I'm+visiting+the+website+and+want+information+about+tours"
        }
    };

    const t = translations[lang];

    // Mobile Menu Toggle Logic
    const menuToggle = document.querySelector('.header__menu-toggle');
    const headerNav = document.querySelector('.header__nav');
    const expLink = document.querySelector('.header__nav-link[href*="#experiencias"]');

    if (expLink && window.innerWidth <= 767) {
        expLink.addEventListener('click', (e) => { e.preventDefault(); });
    }

    if (menuToggle && headerNav) {
        menuToggle.addEventListener('click', () => {
            const isExpanded = menuToggle.getAttribute('aria-expanded') === 'true';
            menuToggle.setAttribute('aria-expanded', !isExpanded);
            headerNav.classList.toggle('active');
        });
    }

    // Generar Footer
    const footerContainer = document.querySelector('.footer');
    if (footerContainer) {
        const pathPrefix = isEn ? "../" : "";
        footerContainer.innerHTML = `
            <div class="footer__main">
                <div class="footer__brand">
                    <div class="footer__brand-info">
                        <img alt="SolyMar Paracas" class="footer__logo" loading="lazy" decoding="async"
                            src="${pathPrefix}img/SolyMar-web.png" />
                    </div>
                    <p class="footer__description">${t.description}</p>
                    <div class="footer__contact">
                        <div class="footer__contact-item">
                            <span class="material-symbols-outlined">phone</span>
                            <span>+51 961 542 547</span>
                        </div>
                        <div class="footer__contact-item">
                            <span class="material-symbols-outlined">location_on</span>
                            <span>Paracas – Pisco</span>
                        </div>
                    </div>
                    <div class="footer__socials">
                        <a class="footer__social-link" href="https://facebook.com/solymarparacas" target="_blank" aria-label="Facebook">
                            <svg class="material-icons" style="width:24px;height:24px;fill:currentColor" viewBox="0 0 24 24"><path d="M14 13.5h2.5l1-4H14v-2c0-1.03 0-2 2-2h1.5V2.14c-.326-.043-1.557-.14-2.857-.14C11.928 2 10 3.657 10 6.7v2.8H7v4h3V22h4v-8.5z"/></svg>
                        </a>
                        <a class="footer__social-link" href="https://instagram.com/solymarparacas" target="_blank" aria-label="Instagram">
                            <svg class="material-icons" style="width:24px;height:24px;fill:currentColor" viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 100 12.324 6.162 6.162 0 000-12.324zM12 16a4 4 0 110-8 4 4 0 010 8zm6.406-11.845a1.44 1.44 0 100 2.881 1.44 1.44 0 000-2.881z"/></svg>
                        </a>
                    </div>
                </div>
                <div class="footer__nav">
                    <div>
                        <h5 class="footer__nav-column-title">${t.experiences}</h5>
                        <ul class="footer__nav-list">
                            <li><a class="footer__nav-link" href="${pathPrefix}snorkel.html">Snorkel</a></li>
                            <li><a class="footer__nav-link" href="${pathPrefix}buceo.html">Buceo</a></li>
                            <li><a class="footer__nav-link" href="${pathPrefix}trekking.html">Trekking</a></li>
                            <li><a class="footer__nav-link" href="${pathPrefix}parapente.html">Parapente</a></li>
                            <li><a class="footer__nav-link" href="${pathPrefix}adrenarena.html">Adrenarena</a></li>
                            <li><a class="footer__nav-link" href="${pathPrefix}atv-gokart.html">ATV & Go Kart</a></li>
                            <li><a class="footer__nav-link" href="${pathPrefix}islas-ballestas.html">Islas Ballestas</a></li>
                        </ul>
                    </div>
                    <div>
                        <h5 class="footer__nav-column-title">${t.support}</h5>
                        <ul class="footer__nav-list">
                            <li><a class="footer__nav-link" href="${pathPrefix}index.html#faq">${t.faq}</a></li>
                            <li><a class="footer__nav-link" href="${pathPrefix}index.html#nosotros">${t.about}</a></li>
                            <li><a class="footer__nav-link" href="https://api.whatsapp.com/send?phone=51961542547&text=${t.waText}">${t.contact}</a></li>
                        </ul>
                    </div>
                </div>
            </div>
            <div class="footer__bottom">
                <span class="footer__copyright">${t.rights}</span>
                <span class="footer__tagline">Paracas – Pisco</span>
            </div>
        `;
    }

    // Botón flotante de WhatsApp
    const waButton = document.createElement('a');
    waButton.href = `https://api.whatsapp.com/send?phone=51961542547&text=${t.waFloatText}`;
    waButton.className = "whatsapp-float";
    waButton.target = "_blank";
    waButton.setAttribute('aria-label', 'WhatsApp');
    waButton.innerHTML = `<svg class="whatsapp-float__icon" viewBox="0 0 24 24" fill="currentColor"><path d="M12.031 21c-1.566-.002-3.1-.42-4.444-1.213l-4.938 1.295 1.32-4.811c-.87-1.373-1.332-2.955-1.332-4.57 0-4.78 3.89-8.67 8.673-8.67h.01c4.782 0 8.665 3.89 8.665 8.67 0 4.78-3.883 8.67-8.665 8.67 5.787 0 10.485-4.698 10.485-10.485 0-5.787-4.698-10.485-10.485-10.485C6.244.03 1.545 4.728 1.545 10.515c0 1.954.537 3.847 1.554 5.485L1.5 22.5l6.671-1.75a10.45 10.45 0 003.86.736V21zM16.541 15.174c-.267-.133-1.579-.78-1.823-.868-.244-.09-.422-.133-.6.133s-.688.868-.844 1.045c-.156.177-.312.2-.578.066a7.447 7.447 0 01-2.195-1.353 8.163 8.163 0 01-1.523-1.89c-.156-.266-.017-.41.116-.543.12-.12.267-.311.4-.467.133-.156.178-.267.267-.444.09-.178.044-.334-.023-.467s-.6-1.445-.823-1.978c-.217-.518-.438-.448-.6-.456-.156-.008-.334-.008-.511-.008-.178 0-.467.067-.711.334A2.08 2.08 0 006.13 10.4c0 1.244.867 2.444.989 2.6s1.778 2.711 4.311 3.733c.6.244 1.066.39 1.433.5a3.42 3.42 0 001.564.089c.477-.075 1.488-.6 1.7-1.177.211-.578.211-1.066.145-1.178-.067-.111-.245-.178-.512-.31z"/></svg>`;
    document.body.appendChild(waButton);

    // Selector de Idioma Flotante (Esquina inferior izquierda)
    const langSwitcher = document.createElement('div');
    langSwitcher.className = "lang-switcher";
    
    // Obtener el nombre del archivo actual (ej: snorkel.html)
    const currentFile = window.location.pathname.split('/').pop() || 'index.html';
    
    const esLink = isEn ? `../${currentFile}` : currentFile;
    const enLink = isEn ? currentFile : `en/${currentFile}`;

    langSwitcher.innerHTML = `
        <a href="${esLink}" class="lang-link ${!isEn ? 'active' : ''}">🇵🇪 ES</a>
        <span class="lang-divider">|</span>
        <a href="${enLink}" class="lang-link ${isEn ? 'active' : ''}">EN 🇺🇸</a>
    `;
    document.body.appendChild(langSwitcher);
});
