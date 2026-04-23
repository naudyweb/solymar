document.addEventListener("DOMContentLoaded", () => {
    // Detectar idioma y contexto basado en la ruta
    const pathSegments = window.location.pathname.split('/').filter(s => s.length > 0);
    const isEn = pathSegments.includes('en');
    const isBlog = pathSegments.includes('blog');
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
            blog: "Blog",
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
            blog: "Blog",
            rights: "© 2026 SolyMar Paracas. All rights reserved.",
            waText: "Hello%2C+I+would+like+more+information+about+your+tours",
            waFloatText: "Hello%2C+I'm+visiting+the+website+and+want+information+about+tours"
        }
    };

    const t = translations[lang];

    // Generar Footer
    const footerContainer = document.querySelector('.footer');
    if (footerContainer) {
        const pathPrefix = isEn ? (isBlog ? "../../" : "../") : (isBlog ? "../" : "");
        
        footerContainer.className = "bg-surface-container pt-24 px-8 md:px-12 text-on-surface";
        footerContainer.innerHTML = `
            <div class="max-w-[1536px] mx-auto flex flex-col gap-16 md:flex-row md:justify-between md:items-start mb-20">
                <div class="max-w-[400px] flex flex-col gap-8">
                    <div class="flex flex-col gap-8">
                        <img alt="SolyMar Paracas" class="h-14 w-auto self-start" loading="lazy" decoding="async"
                            src="${pathPrefix}img/SolyMar-web.png" />
                    </div>
                    <p class="text-on-surface-variant text-base leading-relaxed">${t.description}</p>
                    <div class="flex flex-col gap-4">
                        <div class="flex items-center gap-4 font-semibold">
                            <span class="material-symbols-outlined text-primary">phone</span>
                            <span>+51 961 542 547</span>
                        </div>
                        <div class="flex items-center gap-4 font-semibold">
                            <span class="material-symbols-outlined text-primary">location_on</span>
                            <span>Paracas – Pisco</span>
                        </div>
                    </div>
                    <div class="flex gap-4">
                        <a class="text-primary transition-opacity hover:opacity-80" href="https://facebook.com/solymarparacas" target="_blank" aria-label="Facebook">
                            <svg class="w-6 h-6 fill-current" viewBox="0 0 24 24"><path d="M14 13.5h2.5l1-4H14v-2c0-1.03 0-2 2-2h1.5V2.14c-.326-.043-1.557-.14-2.857-.14C11.928 2 10 3.657 10 6.7v2.8H7v4h3V22h4v-8.5z"/></svg>
                        </a>
                        <a class="text-primary transition-opacity hover:opacity-80" href="https://instagram.com/solymarparacas" target="_blank" aria-label="Instagram">
                            <svg class="w-6 h-6 fill-current" viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 100 12.324 6.162 6.162 0 000-12.324zM12 16a4 4 0 110-8 4 4 0 010 8zm6.406-11.845a1.44 1.44 0 100 2.881 1.44 1.44 0 000-2.881z"/></svg>
                        </a>
                    </div>
                </div>
                <div class="flex flex-wrap gap-16 md:gap-32">
                    <div>
                        <h5 class="text-sm font-extrabold uppercase text-primary mb-6 tracking-wider">${t.experiences}</h5>
                        <ul class="flex flex-col gap-4 list-none p-0">
                            <li><a class="text-on-surface-variant no-underline transition-colors hover:text-primary" href="${pathPrefix}snorkel">Snorkel</a></li>
                            <li><a class="text-on-surface-variant no-underline transition-colors hover:text-primary" href="${pathPrefix}buceo">Buceo</a></li>
                            <li><a class="text-on-surface-variant no-underline transition-colors hover:text-primary" href="${pathPrefix}trekking">Trekking</a></li>
                            <li><a class="text-on-surface-variant no-underline transition-colors hover:text-primary" href="${pathPrefix}parapente">Parapente</a></li>
                            <li><a class="text-on-surface-variant no-underline transition-colors hover:text-primary" href="${pathPrefix}adrenarena">Adrenarena</a></li>
                            <li><a class="text-on-surface-variant no-underline transition-colors hover:text-primary" href="${pathPrefix}atv-gokart">ATV & Go Kart</a></li>
                            <li><a class="text-on-surface-variant no-underline transition-colors hover:text-primary" href="${pathPrefix}islas-ballestas">Islas Ballestas</a></li>
                        </ul>
                    </div>
                    <div>
                        <h5 class="text-sm font-extrabold uppercase text-primary mb-6 tracking-wider">${t.support}</h5>
                        <ul class="flex flex-col gap-4 list-none p-0">
                            <li><a class="text-on-surface-variant no-underline transition-colors hover:text-primary" href="${pathPrefix}index#faq">${t.faq}</a></li>
                            <li><a class="text-on-surface-variant no-underline transition-colors hover:text-primary" href="${pathPrefix}index#nosotros">${t.about}</a></li>
                            <li><a class="text-on-surface-variant no-underline transition-colors hover:text-primary" href="${pathPrefix}blog/">${t.blog}</a></li>
                            <li><a class="text-on-surface-variant no-underline transition-colors hover:text-primary" href="https://api.whatsapp.com/send?phone=51961542547&text=${t.waText}">${t.contact}</a></li>
                        </ul>
                    </div>
                </div>
            </div>
            <div class="max-w-[1536px] mx-auto py-10 border-t border-black/5 flex flex-col items-center gap-4 text-center md:flex-row md:justify-between md:text-left">
                <span class="text-[0.8125rem] text-black/50">${t.rights}</span>
                <span class="text-[0.8125rem] font-bold opacity-30 uppercase tracking-widest">Paracas – Pisco</span>
            </div>
        `;
    }

    // Botón flotante de WhatsApp
    const waButton = document.createElement('a');
    waButton.href = `https://api.whatsapp.com/send?phone=51961542547&text=${t.waFloatText}`;
    waButton.className = "fixed w-[60px] h-[60px] bottom-10 right-10 bg-[#25d366] text-white rounded-full flex items-center justify-center z-[9999] shadow-lg transition-transform hover:scale-110 md:w-[50px] md:h-[50px] md:bottom-5 md:right-5";
    waButton.target = "_blank";
    waButton.setAttribute('aria-label', 'WhatsApp');
    waButton.innerHTML = `<svg class="w-9 h-9 md:w-8 md:h-8 fill-current" viewBox="0 0 24 24"><path d="M12.031 21c-1.566-.002-3.1-.42-4.444-1.213l-4.938 1.295 1.32-4.811c-.87-1.373-1.332-2.955-1.332-4.57 0-4.78 3.89-8.67 8.673-8.67h.01c4.782 0 8.665 3.89 8.665 8.67 0 4.78-3.883 8.67-8.665 8.67 5.787 0 10.485-4.698 10.485-10.485 0-5.787-4.698-10.485-10.485-10.485C6.244.03 1.545 4.728 1.545 10.515c0 1.954.537 3.847 1.554 5.485L1.5 22.5l6.671-1.75a10.45 10.45 0 003.86.736V21zM16.541 15.174c-.267-.133-1.579-.78-1.823-.868-.244-.09-.422-.133-.6.133s-.688.868-.844 1.045c-.156.177-.312.2-.578.066a7.447 7.447 0 01-2.195-1.353 8.163 8.163 0 01-1.523-1.89c-.156-.266-.017-.41.116-.543.12-.12.267-.311.4-.467.133-.156.178-.267.267-.444.09-.178.044-.334-.023-.467s-.6-1.445-.823-1.978c-.217-.518-.438-.448-.6-.456-.156-.008-.334-.008-.511-.008-.178 0-.467.067-.711.334A2.08 2.08 0 006.13 10.4c0 1.244.867 2.444.989 2.6s1.778 2.711 4.311 3.733c.6.244 1.066.39 1.433.5a3.42 3.42 0 001.564.089c.477-.075 1.488-.6 1.7-1.177.211-.578.211-1.066.145-1.178-.067-.111-.245-.178-.512-.31z"/></svg>`;
    document.body.appendChild(waButton);

    // Selector de Idioma Flotante (Esquina inferior izquierda)
    const langSwitcher = document.createElement('div');
    langSwitcher.className = "fixed bottom-10 left-10 bg-surface/90 backdrop-blur-md px-5 py-2.5 rounded-full flex items-center gap-2.5 shadow-lg z-[9999] border border-black/5 md:bottom-5 md:left-5";
    
    // Obtener el nombre del archivo actual (ej: snorkel)
    let currentPath = window.location.pathname;
    let currentFile = currentPath.split('/').pop().replace('.html', '');
    
    // Manejar el caso de que el path sea la raíz / o /en/ o /blog/
    if (!currentFile || currentFile === "" || currentFile === "en" || currentFile === "blog") {
        currentFile = "index";
    }

    const esPath = isBlog ? (isEn ? "../../blog/" : "./") : (isEn ? "../" : "./");
    const enPath = isBlog ? (isEn ? "./" : "../en/blog/") : (isEn ? "./" : "en/");

    const esLink = `${esPath}${currentFile}`;
    const enLink = `${enPath}${currentFile}`;

    langSwitcher.innerHTML = `
        <a href="${esLink}" class="no-underline text-sm font-extrabold transition-all hover:scale-110 ${!isEn ? 'text-primary opacity-100' : 'text-on-surface-variant opacity-60'}" title="Español">🇵🇪 ES</a>
        <span class="text-black/10 font-light">|</span>
        <a href="${enLink}" class="no-underline text-sm font-extrabold transition-all hover:scale-110 ${isEn ? 'text-primary opacity-100' : 'text-on-surface-variant opacity-60'}" title="English">EN 🇺🇸</a>
    `;
    document.body.appendChild(langSwitcher);
});
