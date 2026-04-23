document.addEventListener("DOMContentLoaded", () => {
    const pathSegments = window.location.pathname.split('/').filter(s => s.length > 0);
    const isEn = pathSegments.includes('en');
    const isBlog = pathSegments.includes('blog');
    const rootPath = isEn ? (isBlog ? "../../" : "../") : (isBlog ? "../" : "");
    
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

    const headerHTML = `
        <div class="header__container">
            <div class="header__brand">
                <a href="${rootPath}index">
                    <img class="header__logo" src="${rootPath}img/SolyMar-web.webp" alt="SolyMar Paracas" fetchpriority="high" decoding="async" />
                </a>
            </div>
            <button class="header__menu-toggle" aria-label="Menu" id="mobile-menu-btn">
                <span class="header__menu-icon"></span>
            </button>
            <div class="header__nav" id="mobile-nav">
                <div class="header__nav-item">
                    <a class="header__nav-link" href="javascript:void(0);">${t.experiences}</a>
                    <div class="header__dropdown">
                        <a href="${rootPath}snorkel" class="header__dropdown-link">${t.tours.snorkel}</a>
                        <a href="${rootPath}buceo" class="header__dropdown-link">${t.tours.buceo}</a>
                        <a href="${rootPath}trekking" class="header__dropdown-link">${t.tours.trekking}</a>
                        <a href="${rootPath}parapente" class="header__dropdown-link">${t.tours.parapente}</a>
                        <a href="${rootPath}adrenarena" class="header__dropdown-link">${t.tours.adrenarena}</a>
                        <a href="${rootPath}atv-gokart" class="header__dropdown-link">${t.tours.atv}</a>
                        <a href="${rootPath}islas-ballestas" class="header__dropdown-link">${t.tours.ballestas}</a>
                        <a href="${rootPath}reserva-nacional-paracas" class="header__dropdown-link">${t.tours.reserva}</a>
                    </div>
                </div>
                <a class="header__nav-link" href="${rootPath}index#nosotros">${t.about}</a>
                <a class="header__nav-link" href="${rootPath}blog/">${t.blog}</a>
                <a class="header__nav-link" href="${rootPath}index#faq">${t.faq}</a>
            </div>
            <a href="https://wa.me/51961542547" class="header__cta">${t.book}</a>
        </div>
    `;

    const placeholder = document.getElementById('header-placeholder');
    if (placeholder) {
        placeholder.innerHTML = headerHTML;
        placeholder.classList.add('header');

        const menuToggle = document.getElementById('mobile-menu-btn');
        const headerNav = document.getElementById('mobile-nav');
        
        if (menuToggle && headerNav) {
            // Eliminar listeners previos si existieran (limpieza)
            const newToggle = menuToggle.cloneNode(true);
            menuToggle.parentNode.replaceChild(newToggle, menuToggle);

            newToggle.addEventListener('click', (e) => {
                e.preventDefault();
                e.stopPropagation();
                const isExpanded = newToggle.getAttribute('aria-expanded') === 'true';
                newToggle.setAttribute('aria-expanded', !isExpanded);
                headerNav.classList.toggle('active');
                
                // Bloquear scroll del body cuando el menú está abierto
                if (headerNav.classList.contains('active')) {
                    document.body.style.overflow = 'hidden';
                } else {
                    document.body.style.overflow = '';
                }
            });

            // Cerrar menú al hacer clic en un enlace real (no en el toggle de experiencias)
            headerNav.querySelectorAll('.header__nav-link, .header__dropdown-link').forEach(link => {
                link.addEventListener('click', (e) => {
                    // Si es el enlace de experiencias (void), no cerrar el menú en móvil
                    if (link.getAttribute('href') === 'javascript:void(0);') return;
                    
                    newToggle.setAttribute('aria-expanded', 'false');
                    headerNav.classList.remove('active');
                    document.body.style.overflow = '';
                });
            });
        }
    }
});
