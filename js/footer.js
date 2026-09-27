(function () {
    const gtagScript = document.createElement('script');
    gtagScript.async = true;
    gtagScript.src = "https://www.googletagmanager.com/gtag/js?id=G-M8XTGFB65Y";
    document.head.appendChild(gtagScript);

    window.dataLayer = window.dataLayer || [];
    function gtag() { dataLayer.push(arguments); }
    window.gtag = gtag;
    gtag('js', new Date());
    gtag('config', 'G-M8XTGFB65Y');
})();

document.addEventListener("DOMContentLoaded", () => {
    // Detectar idioma y contexto basado en la ruta
    const pathSegments = window.location.pathname.split('/').filter(s => s.length > 0);
    const isEn = pathSegments.includes('en');
    const isBlog = pathSegments.includes('blog');
    const lang = isEn ? 'en' : 'es';

    // Traducciones del Footer
    const translations = {
        es: {
            description: "Tu agencia de tours personalizados en Paracas: Islas Ballestas, Reserva Nacional, buggies en Huacachina, buceo, parapente y traslados privados.",
            contact: "Contacto",
            experiences: "Experiencias",
            support: "Soporte",
            faq: "Preguntas frecuentes",
            about: "Nosotros",
            blog: "Blog",
            rights: "© 2026 SolyMar Paracas. Todos los derechos reservados.",
            waText: "Hola%2C+quiero+más+información+sobre+sus+tours",
            waFloatText: "Hola%2C+vengo+de+la+web+y+quiero+información+sobre+los+tours",
            tours: {
                ballestas: "Islas Ballestas",
                reserva: "Reserva Nacional",
                combo: "Combo Full Day",
                huacachina: "Buggies Huacachina",
                parapente: "Parapente",
                buceo: "Buceo",
                traslados: "Traslados privados",
                all: "Ver todos los tours"
            }
        },
        en: {
            description: "Your personalized tour agency in Paracas: Ballestas Islands, National Reserve, Huacachina dune buggies, diving, paragliding, and private transfers.",
            contact: "Contact",
            experiences: "Experiences",
            support: "Support",
            faq: "FAQ",
            about: "About us",
            blog: "Blog",
            rights: "© 2026 SolyMar Paracas. All rights reserved.",
            waText: "Hello%2C+I+would+like+more+information+about+your+tours",
            waFloatText: "Hello%2C+I'm+visiting+the+website+and+want+information+about+tours",
            tours: {
                ballestas: "Ballestas Islands",
                reserva: "National Reserve",
                combo: "Combo Full Day",
                huacachina: "Huacachina Buggies",
                parapente: "Paragliding",
                buceo: "Scuba Diving",
                traslados: "Private transfers",
                all: "View all tours"
            }
        }
    };

    const t = translations[lang];
    const langPath = isEn ? "en/" : "";

    // Generar Footer
    const footerContainer = document.querySelector('.footer');
    if (footerContainer) {
        const pathPrefix = isEn ? (isBlog ? "../../" : "../") : (isBlog ? "../" : "");
        const baseNavPath = `${pathPrefix}${langPath}`;
        const link = "text-on-surface-variant transition-colors hover:text-primary";
        const tourItems = [
            ["islas-ballestas.html", t.tours.ballestas],
            ["reserva-nacional-paracas.html", t.tours.reserva],
            ["ballestas-y-reserva-full-day.html", t.tours.combo],
            ["buggies-sandboard-huacachina.html", t.tours.huacachina],
            ["parapente.html", t.tours.parapente],
            ["buceo.html", t.tours.buceo],
            ["transporte-personalizado.html", t.tours.traslados]
        ].map(([href, label]) => `<li><a class="${link}" href="${baseNavPath}${href}">${label}</a></li>`).join("");

        footerContainer.className = "bg-surface-container text-on-surface px-4 sm:px-8 pt-20";
        footerContainer.innerHTML = `
            <div class="max-w-[1336px] mx-auto grid grid-cols-1 gap-14 pb-16 md:grid-cols-12 md:gap-10">
                <div class="md:col-span-5 flex flex-col gap-6 max-w-[420px]">
                    <a href="${baseNavPath}index.html" class="self-start">
                        <img alt="SolyMar Paracas" class="h-12 w-auto" width="310" height="100" loading="lazy" decoding="async" src="${pathPrefix}img/SolyMar-web.png" />
                    </a>
                    <p class="text-on-surface-variant leading-relaxed">${t.description}</p>
                    <div class="flex flex-col gap-3 font-medium">
                        <a href="tel:+51961542547" class="inline-flex items-center gap-3 hover:text-primary">
                            <span class="material-symbols-outlined text-primary" aria-hidden="true">call</span>+51 961 542 547
                        </a>
                        <span class="inline-flex items-center gap-3">
                            <span class="material-symbols-outlined text-primary" aria-hidden="true">location_on</span>El Chaco, Paracas, Ica
                        </span>
                    </div>
                    <div class="flex gap-5">
                        <a class="text-primary transition-opacity hover:opacity-70" href="https://facebook.com/solymarparacas" target="_blank" rel="noopener" aria-label="Facebook">
                            <svg class="w-6 h-6 fill-current" viewBox="0 0 24 24" aria-hidden="true"><path d="M14 13.5h2.5l1-4H14v-2c0-1.03 0-2 2-2h1.5V2.14c-.326-.043-1.557-.14-2.857-.14C11.928 2 10 3.657 10 6.7v2.8H7v4h3V22h4v-8.5z"/></svg>
                        </a>
                        <a class="text-primary transition-opacity hover:opacity-70" href="https://instagram.com/solymarparacas" target="_blank" rel="noopener" aria-label="Instagram">
                            <svg class="w-6 h-6 fill-current" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 100 12.324 6.162 6.162 0 000-12.324zM12 16a4 4 0 110-8 4 4 0 010 8zm6.406-11.845a1.44 1.44 0 100 2.881 1.44 1.44 0 000-2.881z"/></svg>
                        </a>
                    </div>
                </div>
                <nav class="md:col-span-4" aria-label="${t.experiences}">
                    <h2 class="font-display text-lg text-primary mb-5">${t.experiences}</h2>
                    <ul class="grid grid-cols-1 gap-3 sm:grid-cols-2 sm:gap-x-8">
                        ${tourItems}
                        <li><a class="font-semibold text-primary underline decoration-sand decoration-2 underline-offset-4" href="${baseNavPath}tours.html">${t.tours.all}</a></li>
                    </ul>
                </nav>
                <nav class="md:col-span-3" aria-label="${t.support}">
                    <h2 class="font-display text-lg text-primary mb-5">${t.support}</h2>
                    <ul class="flex flex-col gap-3">
                        <li><a class="${link}" href="${baseNavPath}index.html#faq">${t.faq}</a></li>
                        <li><a class="${link}" href="${baseNavPath}index.html#nosotros">${t.about}</a></li>
                        <li><a class="${link}" href="${baseNavPath}blog/index.html">${t.blog}</a></li>
                        <li><a class="${link}" href="https://api.whatsapp.com/send?phone=51961542547&text=${t.waText}" target="_blank" rel="noopener">${t.contact}</a></li>
                    </ul>
                </nav>
            </div>
            <div class="max-w-[1336px] mx-auto py-8 border-t border-primary/15 text-sm text-on-surface-variant">
                <span>${t.rights}</span>
            </div>
        `;
    }

    // Botón flotante de WhatsApp
    const waButton = document.createElement('a');
    waButton.href = `https://api.whatsapp.com/send?phone=51961542547&text=${t.waFloatText}`;
    waButton.className = "fixed w-14 h-14 bottom-5 right-5 bg-[#25d366] text-white rounded-full flex items-center justify-center z-[900] shadow-[0_10px_30px_-6px_rgba(10,61,82,0.45)] transition-transform hover:-translate-y-0.5 active:scale-95";
    waButton.target = "_blank";
    waButton.rel = "noopener";
    waButton.setAttribute('aria-label', 'WhatsApp');
    waButton.innerHTML = `<svg class="w-7 h-7 fill-current" viewBox="0 0 24 24" aria-hidden="true"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413Z"/></svg>`;
    document.body.appendChild(waButton);
});
