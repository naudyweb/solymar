document.addEventListener("DOMContentLoaded", () => {
    const isEn = window.location.pathname.includes('/en/');
    const pathPrefix = isEn ? "" : ""; // Las rutas son relativas al archivo actual
    const rootPath = isEn ? "../" : "";
    
    const translations = {
        es: {
            experiences: "Experiencias",
            about: "Nosotros",
            blog: "Blog",
            faq: "Preguntas Frecuentes",
            book: "RESERVAR",
            tours: {
                snorkel: "Snorkel",
                buceo: "Buceo",
                trekking: "Trekking",
                parapente: "Parapente",
                adrenarena: "Adrenarena",
                atv: "ATV y Go Kart",
                ballestas: "Islas Ballestas",
                reserva: "Reserva Nacional"
            }
        },
        en: {
            experiences: "Experiences",
            about: "About Us",
            blog: "Blog",
            faq: "FAQ",
            book: "BOOK NOW",
            tours: {
                snorkel: "Snorkeling",
                buceo: "Diving",
                trekking: "Trekking",
                parapente: "Paragliding",
                adrenarena: "Adrenarena",
                atv: "ATV & Go Kart",
                ballestas: "Ballestas Islands",
                reserva: "National Reserve"
            }
        }
    };

    const t = isEn ? translations.en : translations.es;
    const langPath = isEn ? "" : ""; 

    const headerHTML = `
        <div class="header__container">
            <div class="header__brand">
                <a href="${rootPath}index.html">
                    <img class="header__logo" src="${rootPath}img/SolyMar-web.webp" alt="SolyMar Paracas" fetchpriority="high" decoding="async" />
                </a>
            </div>
            <button class="header__menu-toggle" aria-label="Menu">
                <span class="header__menu-icon"></span>
            </button>
            <div class="header__nav">
                <div class="header__nav-item">
                    <a class="header__nav-link" href="javascript:void(0);">${t.experiences}</a>
                    <div class="header__dropdown">
                        <a href="${rootPath}snorkel.html" class="header__dropdown-link">${t.tours.snorkel}</a>
                        <a href="${rootPath}buceo.html" class="header__dropdown-link">${t.tours.buceo}</a>
                        <a href="${rootPath}trekking.html" class="header__dropdown-link">${t.tours.trekking}</a>
                        <a href="${rootPath}parapente.html" class="header__dropdown-link">${t.tours.parapente}</a>
                        <a href="${rootPath}adrenarena.html" class="header__dropdown-link">${t.tours.adrenarena}</a>
                        <a href="${rootPath}atv-gokart.html" class="header__dropdown-link">${t.tours.atv}</a>
                        <a href="${rootPath}islas-ballestas.html" class="header__dropdown-link">${t.tours.ballestas}</a>
                        <a href="${rootPath}reserva-nacional-paracas.html" class="header__dropdown-link">${t.tours.reserva}</a>
                    </div>
                </div>
                <a class="header__nav-link" href="${rootPath}index.html#nosotros">${t.about}</a>
                <a class="header__nav-link" href="${rootPath}blog.html">${t.blog}</a>
                <a class="header__nav-link" href="${rootPath}index.html#faq">${t.faq}</a>
            </div>
            <a href="https://wa.me/51961542547" class="header__cta">${t.book}</a>
        </div>
    `;

    const placeholder = document.getElementById('header-placeholder');
    if (placeholder) {
        placeholder.innerHTML = headerHTML;
        placeholder.classList.add('header'); // Asegura que tenga la clase para estilos

        // Re-adjuntar lógica de menú móvil
        const menuToggle = placeholder.querySelector('.header__menu-toggle');
        const headerNav = placeholder.querySelector('.header__nav');
        
        if (menuToggle && headerNav) {
            menuToggle.addEventListener('click', () => {
                const isExpanded = menuToggle.getAttribute('aria-expanded') === 'true';
                menuToggle.setAttribute('aria-expanded', !isExpanded);
                headerNav.classList.toggle('active');
            });
        }
    }
});
