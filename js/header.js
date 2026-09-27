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
            faq: "Preguntas",
            book: "Reservar por WhatsApp",
            menu: "Abrir menú",
            waText: "Hola%2C+quiero+reservar+un+tour",
            tours: {
                ballestas: "Islas Ballestas",
                reserva: "Reserva Nacional",
                combo: "Combo Full Day",
                huacachina: "Buggies Huacachina",
                parapente: "Parapente",
                buceo: "Buceo",
                trekking: "Trekking Sombras Doradas",
                traslados: "Traslados privados",
                all: "Ver todos los tours"
            }
        },
        en: {
            experiences: "Experiences",
            about: "About us",
            blog: "Blog",
            faq: "FAQ",
            book: "Book on WhatsApp",
            menu: "Open menu",
            waText: "Hi%2C+I+would+like+to+book+a+tour",
            tours: {
                ballestas: "Ballestas Islands",
                reserva: "National Reserve",
                combo: "Combo Full Day",
                huacachina: "Huacachina Buggies",
                parapente: "Paragliding",
                buceo: "Diving",
                trekking: "Golden Shadows Trek",
                traslados: "Private transfers",
                all: "View all tours"
            }
        }
    };

    const t = isEn ? translations.en : translations.es;
    const langPath = isEn ? "en/" : "";
    const baseNavPath = `${rootPath}${langPath}`;

    // Compute language switch links
    let currentPath = window.location.pathname;
    let currentFile = currentPath.split('/').pop().replace('.html', '');
    if (!currentFile || currentFile === "" || currentFile === "en" || currentFile === "blog" || currentFile === "index") {
        currentFile = "index.html";
    } else {
        currentFile = currentFile + ".html";
    }

    const esPath = isBlog ? (isEn ? "../../blog/" : "./") : (isEn ? "../" : "./");
    const enPath = isBlog ? (isEn ? "./" : "../en/blog/") : (isEn ? "./" : "en/");

    const esLink = `${esPath}${currentFile}`;
    const enLink = `${enPath}${currentFile}`;
    const otherLangLink = isEn ? esLink : enLink;
    const otherLangText = isEn ? "ES" : "EN";
    const otherLangTitle = isEn ? "Cambiar a Español" : "Switch to English";
    const otherLangCode = isEn ? "es" : "en";

    const tourLinks = [
        ["islas-ballestas.html", t.tours.ballestas],
        ["reserva-nacional-paracas.html", t.tours.reserva],
        ["ballestas-y-reserva-full-day.html", t.tours.combo],
        ["buggies-sandboard-huacachina.html", t.tours.huacachina],
        ["parapente.html", t.tours.parapente],
        ["buceo.html", t.tours.buceo],
        ["trekking.html", t.tours.trekking],
        ["transporte-personalizado.html", t.tours.traslados]
    ].map(([href, label]) =>
        `<a href="${baseNavPath}${href}" class="block py-2.5 text-[0.9375rem] text-on-surface-variant transition-colors hover:text-primary lg:px-5">${label}</a>`
    ).join("");

    const navLink = "block py-4 text-lg font-medium text-on-surface border-b border-primary/10 transition-colors hover:text-primary lg:py-2 lg:text-[0.9375rem] lg:text-on-surface-variant lg:border-none";
    const waIcon = `<svg class="w-4 h-4 fill-current shrink-0" viewBox="0 0 24 24" aria-hidden="true"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413Z"/></svg>`;

    const headerHTML = `
        <div class="max-w-[1400px] mx-auto px-4 sm:px-8 h-16 flex justify-between items-center gap-6">
            <a href="${baseNavPath}index.html" class="shrink-0">
                <img class="h-9 w-auto" src="${rootPath}img/SolyMar-web.webp" alt="SolyMar Paracas" width="310" height="100" fetchpriority="high" decoding="async" />
            </a>

            <!-- Mobile: idioma + menú -->
            <div class="flex items-center gap-2 lg:hidden">
                <a href="${otherLangLink}" hreflang="${otherLangCode}" title="${otherLangTitle}" aria-label="${otherLangTitle}" class="text-sm font-semibold px-3 py-2 text-on-surface-variant hover:text-primary">${otherLangText}</a>
                <button type="button" class="relative w-11 h-11 flex items-center justify-center rounded-full z-[1100]" aria-label="${t.menu}" aria-expanded="false" aria-controls="mobile-nav" id="mobile-menu-btn">
                    <span class="w-6 h-0.5 bg-primary relative transition-all duration-300 before:content-[''] before:absolute before:w-6 before:h-0.5 before:bg-primary before:-top-2 before:left-0 before:transition-all before:duration-300 after:content-[''] after:absolute after:w-6 after:h-0.5 after:bg-primary after:top-2 after:left-0 after:transition-all after:duration-300" id="hamburger-icon"></span>
                </button>
            </div>

            <!-- Navegación -->
            <div class="fixed top-0 -right-full w-[86%] max-w-[360px] h-[100dvh] overflow-y-auto bg-surface flex flex-col pt-20 px-6 pb-10 shadow-[0_0_60px_rgba(10,61,82,0.18)] transition-[right] duration-400 ease-out-soft z-[1000] lg:static lg:w-auto lg:max-w-none lg:h-auto lg:overflow-visible lg:bg-transparent lg:flex-row lg:items-center lg:p-0 lg:gap-8 lg:shadow-none lg:transition-none" id="mobile-nav">
                <div class="relative group">
                    <button type="button" class="${navLink} w-full text-left flex items-center justify-between gap-1 lg:w-auto" aria-haspopup="true" id="tours-menu-btn">
                        ${t.experiences}
                        <span class="material-symbols-outlined text-xl hidden lg:inline" aria-hidden="true">expand_more</span>
                    </button>
                    <div class="pl-4 py-2 border-b border-primary/10 lg:border lg:border-primary/10 lg:absolute lg:top-full lg:left-0 lg:hidden lg:group-hover:block lg:group-focus-within:block lg:bg-surface-container-low lg:min-w-[260px] lg:p-0 lg:py-3 lg:rounded-sm lg:shadow-[0_20px_40px_-12px_rgba(10,61,82,0.25)]">
                        ${tourLinks}
                        <a href="${baseNavPath}tours.html" class="block py-2.5 text-[0.9375rem] font-semibold text-primary underline decoration-sand decoration-2 underline-offset-4 lg:px-5 lg:mt-1">${t.tours.all}</a>
                    </div>
                </div>
                <a class="${navLink}" href="${baseNavPath}index.html#nosotros">${t.about}</a>
                <a class="${navLink}" href="${baseNavPath}blog/index.html">${t.blog}</a>
                <a class="${navLink}" href="${baseNavPath}index.html#faq">${t.faq}</a>

                <div class="mt-8 flex flex-col gap-5 lg:hidden">
                    <a href="https://wa.me/51961542547?text=${t.waText}" target="_blank" rel="noopener" class="inline-flex items-center justify-center gap-2 bg-tertiary text-on-tertiary py-3.5 px-6 rounded-full font-semibold active:scale-[0.98]">${waIcon}${t.book}</a>
                    <div class="flex gap-4 text-sm font-semibold">
                        <a href="${esLink}" hreflang="es" class="${!isEn ? 'text-primary underline decoration-sand decoration-2 underline-offset-4' : 'text-on-surface-variant'}">Español</a>
                        <a href="${enLink}" hreflang="en" class="${isEn ? 'text-primary underline decoration-sand decoration-2 underline-offset-4' : 'text-on-surface-variant'}">English</a>
                    </div>
                </div>
            </div>

            <!-- Desktop: idioma + reserva -->
            <div class="hidden lg:flex items-center gap-5 shrink-0">
                <a href="${otherLangLink}" hreflang="${otherLangCode}" title="${otherLangTitle}" aria-label="${otherLangTitle}" class="text-sm font-semibold text-on-surface-variant hover:text-primary transition-colors">${otherLangText}</a>
                <a href="https://wa.me/51961542547?text=${t.waText}" target="_blank" rel="noopener" class="inline-flex items-center gap-2 bg-tertiary text-on-tertiary py-2.5 px-5 rounded-full text-sm font-semibold whitespace-nowrap transition-colors hover:bg-tertiary-container active:scale-[0.98]">${waIcon}${t.book}</a>
            </div>
        </div>
    `;

    const placeholder = document.getElementById('header-placeholder');
    if (placeholder) {
        placeholder.innerHTML = headerHTML;
        placeholder.className = 'fixed top-0 w-full z-[1000] bg-surface/90 backdrop-blur-md border-b border-primary/10';

        const menuToggle = document.getElementById('mobile-menu-btn');
        const headerNav = document.getElementById('mobile-nav');
        const hamburgerIcon = document.getElementById('hamburger-icon');

        const setOpen = (open) => {
            headerNav.classList.toggle('right-0', open);
            headerNav.classList.toggle('-right-full', !open);
            menuToggle.setAttribute('aria-expanded', String(open));
            hamburgerIcon.classList.toggle('bg-transparent', open);
            hamburgerIcon.classList.toggle('bg-primary', !open);
            ['before:rotate-45', 'before:top-0', 'after:-rotate-45', 'after:top-0'].forEach(c => hamburgerIcon.classList.toggle(c, open));
            ['before:-top-2', 'after:top-2'].forEach(c => hamburgerIcon.classList.toggle(c, !open));
            document.body.style.overflow = open ? 'hidden' : '';
        };

        if (menuToggle && headerNav) {
            menuToggle.addEventListener('click', (e) => {
                e.preventDefault();
                setOpen(!headerNav.classList.contains('right-0'));
            });

            headerNav.querySelectorAll('a').forEach(link => {
                link.addEventListener('click', () => setOpen(false));
            });

            document.addEventListener('keydown', (e) => {
                if (e.key === 'Escape' && headerNav.classList.contains('right-0')) setOpen(false);
            });
        }
    }
});
