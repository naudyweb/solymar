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
        <div class="max-w-[1536px] mx-auto px-8 h-20 flex justify-between items-center">
            <div class="flex items-center">
                <a href="${rootPath}index">
                    <img class="h-10 w-auto" src="${rootPath}img/SolyMar-web.webp" alt="SolyMar Paracas" fetchpriority="high" decoding="async" />
                </a>
            </div>
            
            <!-- Hamburger Menu Button -->
            <button class="md:hidden relative w-10 h-10 flex items-center justify-center focus:outline-none z-[1100]" aria-label="Menu" id="mobile-menu-btn">
                <div class="w-6 h-0.5 bg-primary relative transition-all duration-300 before:content-[''] before:absolute before:w-6 before:h-0.5 before:bg-primary before:-top-2 before:left-0 before:transition-all before:duration-300 after:content-[''] after:absolute after:w-6 after:h-0.5 after:bg-primary after:top-2 after:left-0 after:transition-all after:duration-300" id="hamburger-icon"></div>
            </button>

            <!-- Navigation -->
            <div class="fixed top-0 -right-full w-[80%] max-w-[300px] h-screen bg-surface flex flex-col pt-24 px-8 gap-2 shadow-2xl transition-all duration-400 z-[1000] md:static md:w-auto md:max-w-none md:h-auto md:bg-transparent md:flex-row md:items-center md:pt-0 md:px-0 md:gap-8 md:shadow-none md:transition-none" id="mobile-nav">
                <div class="relative group">
                    <a class="block py-4 border-b border-surface-variant text-base font-bold uppercase tracking-wider text-on-surface-variant hover:text-primary transition-colors md:py-2 md:border-none md:text-[0.8125rem]" href="javascript:void(0);">${t.experiences}</a>
                    <div class="block pl-6 md:absolute md:top-full md:left-1/2 md:-translate-x-1/2 md:hidden md:group-hover:block md:bg-surface md:min-w-[220px] md:py-4 md:rounded-lg md:shadow-xl md:z-50">
                        <a href="${rootPath}snorkel" class="block py-3 text-sm text-on-surface-variant hover:bg-surface-container hover:text-primary md:px-8">${t.tours.snorkel}</a>
                        <a href="${rootPath}buceo" class="block py-3 text-sm text-on-surface-variant hover:bg-surface-container hover:text-primary md:px-8">${t.tours.buceo}</a>
                        <a href="${rootPath}trekking" class="block py-3 text-sm text-on-surface-variant hover:bg-surface-container hover:text-primary md:px-8">${t.tours.trekking}</a>
                        <a href="${rootPath}parapente" class="block py-3 text-sm text-on-surface-variant hover:bg-surface-container hover:text-primary md:px-8">${t.tours.parapente}</a>
                        <a href="${rootPath}adrenarena" class="block py-3 text-sm text-on-surface-variant hover:bg-surface-container hover:text-primary md:px-8">${t.tours.adrenarena}</a>
                        <a href="${rootPath}atv-gokart" class="block py-3 text-sm text-on-surface-variant hover:bg-surface-container hover:text-primary md:px-8">${t.tours.atv}</a>
                        <a href="${rootPath}islas-ballestas" class="block py-3 text-sm text-on-surface-variant hover:bg-surface-container hover:text-primary md:px-8">${t.tours.ballestas}</a>
                        <a href="${rootPath}reserva-nacional-paracas" class="block py-3 text-sm text-on-surface-variant hover:bg-surface-container hover:text-primary md:px-8">${t.tours.reserva}</a>
                    </div>
                </div>
                <a class="block py-4 border-b border-surface-variant text-base font-bold uppercase tracking-wider text-on-surface-variant hover:text-primary transition-colors md:py-2 md:border-none md:text-[0.8125rem]" href="${rootPath}index#nosotros">${t.about}</a>
                <a class="block py-4 border-b border-surface-variant text-base font-bold uppercase tracking-wider text-on-surface-variant hover:text-primary transition-colors md:py-2 md:border-none md:text-[0.8125rem]" href="${rootPath}blog/">${t.blog}</a>
                <a class="block py-4 border-b border-surface-variant text-base font-bold uppercase tracking-wider text-on-surface-variant hover:text-primary transition-colors md:py-2 md:border-none md:text-[0.8125rem]" href="${rootPath}index#faq">${t.faq}</a>
            </div>
            <a href="https://wa.me/51961542547" class="hidden md:block bg-primary text-white py-3 px-6 rounded-full text-[0.8125rem] font-bold tracking-wider hover:bg-primary-container transition-colors">${t.book}</a>
        </div>
    `;

    const placeholder = document.getElementById('header-placeholder');
    if (placeholder) {
        placeholder.innerHTML = headerHTML;
        placeholder.className = 'fixed top-0 w-full z-[1000] bg-surface/95 backdrop-blur-md border-b border-black/5';

        const menuToggle = document.getElementById('mobile-menu-btn');
        const headerNav = document.getElementById('mobile-nav');
        const hamburgerIcon = document.getElementById('hamburger-icon');
        
        if (menuToggle && headerNav) {
            menuToggle.addEventListener('click', (e) => {
                e.preventDefault();
                const isOpen = headerNav.classList.contains('right-0');
                
                if (!isOpen) {
                    headerNav.classList.remove('-right-full');
                    headerNav.classList.add('right-0');
                    menuToggle.setAttribute('aria-expanded', 'true');
                    // Hamburger animation
                    hamburgerIcon.classList.add('bg-transparent');
                    hamburgerIcon.classList.remove('bg-primary');
                    hamburgerIcon.classList.add('before:rotate-45', 'before:top-0', 'after:-rotate-45', 'after:top-0');
                    hamburgerIcon.classList.remove('before:-top-2', 'after:top-2');
                    document.body.style.overflow = 'hidden';
                } else {
                    headerNav.classList.add('-right-full');
                    headerNav.classList.remove('right-0');
                    menuToggle.setAttribute('aria-expanded', 'false');
                    // Hamburger animation
                    hamburgerIcon.classList.remove('bg-transparent');
                    hamburgerIcon.classList.add('bg-primary');
                    hamburgerIcon.classList.remove('before:rotate-45', 'before:top-0', 'after:-rotate-45', 'after:top-0');
                    hamburgerIcon.classList.add('before:-top-2', 'after:top-2');
                    document.body.style.overflow = '';
                }
            });

            headerNav.querySelectorAll('a').forEach(link => {
                link.addEventListener('click', () => {
                    if (link.getAttribute('href') === 'javascript:void(0);') return;
                    headerNav.classList.add('-right-full');
                    headerNav.classList.remove('right-0');
                    hamburgerIcon.classList.remove('bg-transparent');
                    hamburgerIcon.classList.add('bg-primary');
                    hamburgerIcon.classList.remove('before:rotate-45', 'before:top-0', 'after:-rotate-45', 'after:top-0');
                    hamburgerIcon.classList.add('before:-top-2', 'after:top-2');
                    document.body.style.overflow = '';
                });
            });
        }
    }
});
