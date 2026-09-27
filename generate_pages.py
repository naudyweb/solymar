# -*- coding: utf-8 -*-
import glob
import os
import json

# Definitions of all tours, metadata, and copy
tours = {
    "islas-ballestas": {
        "filename": "islas-ballestas.html",
        "image": "img/islas-ballestas.jpg",
        "price": "S/ 80",
        "price_val": "80",
        "price_cur": "PEN",
        "category": "mar",
        "es": {
            "title": "Tour Islas Ballestas 2026: Precio, Horarios y Reserva | SolyMar Paracas",
            "desc": "Tour en lancha a las Islas Ballestas desde el muelle El Chaco de Paracas. Salidas 8 y 10 am: lobos marinos, pingüinos de Humboldt y el Candelabro. Precio total claro, sin sorpresas.",
            "h1": "Tour a las Islas Ballestas desde Paracas",
            "keywords": "tour islas ballestas, islas ballestas precio, islas ballestas cuanto cuesta, tour ballestas paracas, islas ballestas horarios, galapagos peruanas, paseo en lancha paracas, que ver en islas ballestas",
            "subtitle": "Navega por las \"Galápagos peruanas\" y observa lobos marinos, pingüinos de Humboldt y miles de aves a pocos metros de tu lancha.",
            "intro": "Las <strong>Islas Ballestas</strong> son el destino estrella de Paracas. Bañadas por las aguas frías de la corriente de Humboldt, forman uno de los ecosistemas marinos más productivos del planeta: por algo se les llama las \"Galápagos del Perú\".",
            "intro_p2": "El recorrido parte del <strong>muelle turístico El Chaco</strong> en una lancha moderna con chalecos salvavidas y guía a bordo. Durante 2 horas navegarás junto a colonias de <strong>lobos marinos y pingüinos de Humboldt</strong>, piqueros, guanayes y zarcillos, con frecuentes avistamientos de delfines en ruta.",
            "intro_p3": "Antes de llegar a las islas, la embarcación se detiene frente al <strong>Candelabro de Paracas</strong>, un geoglifo gigante de más de 150 metros trazado en la ladera de arena, que solo puede apreciarse desde el mar.",
            "why_title": "¿Qué verás en el tour?",
            "why_items": [
                {"icon": "pets", "title": "Lobos Marinos", "desc": "Observa maternidades y colonias de lobos marinos descansando sobre las rocas."},
                {"icon": "egg", "title": "Pingüinos de Humboldt", "desc": "Hogar de simpáticos pingüinos en su entorno natural protegido."},
                {"icon": "flutter_dash", "title": "Aves Guaneras", "desc": "Miles de piqueros, guanayes, pelícanos y zarcillos cubriendo los cielos."},
                {"icon": "water", "title": "Delfines en Ruta", "desc": "Con frecuencia, grupos de delfines acompañan la embarcación en el trayecto."}
            ],
            "included": ["Lancha turística moderna", "Guía bilingüe certificado", "Duración: 2 horas aprox.", "Visita al Candelabro", "Seguro de pasajeros"],
            "excluded": ["Impuestos del muelle y SERNANP (S/ 16 adultos, S/ 8 niños)"],
            "schedule_label": "* Salidas diarias a las 8:00 AM y 10:00 AM desde el muelle El Chaco. Te recomendamos el primer turno (mar más calmado).",
            "faq_title": "Preguntas Frecuentes",
            "faqs": [
                {"q": "¿Cuánto cuesta el tour a las Islas Ballestas en 2026?", "a": "Nuestro tour cuesta S/ 80 por persona e incluye lancha moderna, guía certificado y seguro. Aparte, cada visitante paga en el muelle S/ 16 de impuestos (tasa SERNANP + embarque). A diferencia de los precios \"gancho\" que verás en internet, nosotros te informamos el costo total real antes de reservar: sin sorpresas ni cobros ocultos."},
                {"q": "¿Cuál es el mejor horario para hacer el tour?", "a": "El primer turno de las 8:00 AM es el más recomendado: el mar está más calmado, hay mejor visibilidad y la fauna está más activa. El turno de las 10:00 AM también es bueno, aunque suele haber algo más de viento y oleaje."},
                {"q": "¿Se puede bajar a las islas o nadar?", "a": "No, las Islas Ballestas son un área natural protegida. El recorrido es 100% en lancha y no se permite el desembarco ni nadar, para proteger a los lobos marinos y pingüinos."},
                {"q": "¿Es apto para niños, adultos mayores o embarazadas?", "a": "Sí, es un paseo muy seguro que no requiere esfuerzo físico: todos los pasajeros viajan sentados y con chaleco salvavidas obligatorio. Niños desde los 2 años, adultos mayores y gestantes (con embarazo sin complicaciones) lo disfrutan sin problema."},
                {"q": "¿Me puedo marear durante el paseo?", "a": "El trayecto dura 2 horas y en el primer turno el mar suele estar tranquilo. Si eres muy sensible al movimiento, toma una pastilla para el mareo 30 minutos antes de embarcar y desayuna ligero."},
                {"q": "¿Qué debo llevar al tour?", "a": "Cortavientos o casaca ligera, bloqueador solar, lentes de sol, gorra con ajuste (hay viento en el mar) y tu cámara o celular asegurado con correa. En el muelle hay baños y cafeterías para comprar agua antes de zarpar."},
                {"q": "¿Qué pasa si hay mal clima?", "a": "Si la Capitanía de Puerto cierra el muelle por oleaje anómalo, te ofrecemos reprogramar el tour al siguiente turno disponible o la devolución del 100% de tu dinero."}
            ]
        },
        "en": {
            "title": "Ballestas Islands Tour 2026: Prices, Times & Booking | SolyMar Paracas",
            "desc": "Boat tour to the Ballestas Islands from El Chaco pier, Paracas. Departures 8 & 10 am: sea lions, Humboldt penguins and the Candelabra. Clear total price, no pier surprises.",
            "h1": "Ballestas Islands Tour from Paracas",
            "keywords": "ballestas islands tour, ballestas islands price, ballestas islands tour cost, ballestas islands paracas, ballestas islands schedule, peruvian galapagos, boat tour paracas, what to see ballestas islands",
            "subtitle": "Cruise the \"Peruvian Galapagos\" and watch sea lions, Humboldt penguins and thousands of seabirds just meters from your boat.",
            "intro": "The <strong>Ballestas Islands</strong> are the star attraction of Paracas. Fed by the cold Humboldt Current, they form one of the most productive marine ecosystems on Earth, which is why they are called the \"Peruvian Galapagos\".",
            "intro_p2": "The tour departs from <strong>El Chaco tourist pier</strong> aboard a modern speedboat with life jackets and an onboard guide. For 2 hours you will cruise alongside colonies of <strong>sea lions and Humboldt penguins</strong>, boobies, cormorants and Inca terns, with frequent dolphin sightings along the way.",
            "intro_p3": "Before reaching the islands, the boat stops in front of the <strong>Paracas Candelabra</strong>, a giant geoglyph over 150 meters tall etched into the sandy hillside, visible only from the sea.",
            "why_title": "What will you see on the tour?",
            "why_items": [
                {"icon": "pets", "title": "Sea Lions", "desc": "Observe large colonies of sea lions resting and swimming in total freedom."},
                {"icon": "egg", "title": "Humboldt Penguins", "desc": "See penguins in their natural habitat within the marine reserve."},
                {"icon": "flutter_dash", "title": "Guano Birds", "desc": "Thousands of boobies, cormorants, pelicans, and terns soaring in the skies."},
                {"icon": "water", "title": "Dolphin Spotting", "desc": "Frequently, groups of playful dolphins accompany our speedboats along the way."}
            ],
            "included": ["Modern tourist speedboat", "Certified bilingual guide", "Duration: approx. 2 hours", "View of the Candelabra", "Passenger insurance"],
            "excluded": ["Pier tax & SERNANP fee (S/ 16 adults, S/ 8 children)"],
            "schedule_label": "* Daily departures at 8:00 AM and 10:00 AM from El Chaco pier. The first departure is recommended for calmer seas.",
            "faq_title": "Frequently Asked Questions",
            "faqs": [
                {"q": "How much does the Ballestas Islands tour cost in 2026?", "a": "Our tour costs S/ 80 per person and includes a modern speedboat, certified guide, and insurance. Separately, every visitor pays S/ 16 in pier taxes (SERNANP + boarding fee). Unlike the \"teaser\" prices you may see online, we tell you the real total cost before you book: no surprises, no hidden fees."},
                {"q": "What is the best departure time?", "a": "The 8:00 AM departure is the best one: the sea is calmer, visibility is better, and wildlife is most active. The 10:00 AM departure is also good, though wind and swell tend to pick up later in the morning."},
                {"q": "Can we walk on the islands or swim?", "a": "No, the Ballestas Islands are a protected reserve. The tour is 100% boat-based; stepping onto the islands or swimming is strictly prohibited to protect the sea lion and penguin colonies."},
                {"q": "Is it suitable for children, seniors, or pregnant travelers?", "a": "Yes, it is a very safe, zero-effort ride. All passengers remain seated wearing mandatory life jackets. Children from age 2, seniors, and pregnant travelers (with uncomplicated pregnancies) enjoy it without any issue."},
                {"q": "Will I get seasick?", "a": "The ride lasts 2 hours and the sea is usually calm at the first departure. If you are prone to motion sickness, take a seasickness pill 30 minutes before boarding and keep breakfast light."},
                {"q": "What should I bring?", "a": "A windbreaker or light jacket, sunscreen, sunglasses, a hat that straps on (it gets windy at sea), and your camera or phone secured with a strap. The pier has restrooms and cafés to grab water before departure."},
                {"q": "What happens in case of bad weather?", "a": "If the Port Authority closes the pier due to unusual swell, we will offer to reschedule your tour to the next available departure or issue a 100% refund."}
            ]
        }
    },
    "reserva-nacional-paracas": {
        "filename": "reserva-nacional-paracas.html",
        "image": "img/reserva-nacional-paracas.jpg",
        "price": "S/ 50",
        "price_val": "50",
        "price_cur": "PEN",
        "category": "desierto",
        "es": {
            "title": "Tour Reserva Nacional de Paracas 2026: Playa Roja y La Catedral | SolyMar",
            "desc": "Tour guiado por la Reserva Nacional de Paracas: Playa Roja, mirador La Catedral, caleta Lagunillas y desierto junto al mar. Salida 11 am con recojo en tu hotel. Agencia local.",
            "h1": "Tour por la Reserva Nacional de Paracas",
            "keywords": "reserva nacional de paracas tour, reserva nacional de paracas precio, playa roja paracas, la catedral paracas, entrada reserva paracas, que ver en la reserva de paracas, que llevar a la reserva de paracas, playa lagunillas",
            "subtitle": "Explora el único lugar del Perú donde el desierto cae en acantilados de colores directamente sobre el Océano Pacífico.",
            "intro": "La <strong>Reserva Nacional de Paracas</strong> es la única área protegida marino-costera de su tipo en el Perú: más de 335 mil hectáreas donde el desierto, los acantilados y el mar frío de la corriente de Humboldt se combinan en paisajes que no verás en ningún otro lugar.",
            "intro_p2": "En este recorrido terrestre de 3.5 horas visitarás la famosa <strong>Playa Roja</strong>, el mirador de <strong>La Catedral</strong>, los miradores de la península y la caleta de pescadores de <strong>Lagunillas</strong>, con paradas fotográficas guiadas en cada punto.",
            "intro_p3": "Es el complemento perfecto del tour a las Islas Ballestas: en un solo día conoces el lado marino y el lado desértico de Paracas, con recojo y retorno a tu hotel incluidos.",
            "why_title": "Atractivos destacados del recorrido",
            "why_items": [
                {"icon": "landscape", "title": "Playa Roja", "desc": "Su coloración rojiza única proviene de la erosión de cerros de granito rosado cercanos."},
                {"icon": "auto_awesome", "title": "La Catedral", "desc": "Mirador hacia la emblemática formación rocosa esculpida por el viento y el mar."},
                {"icon": "restaurant", "title": "Playa Lagunillas", "desc": "Caleta de pescadores donde realizamos una parada para disfrutar de gastronomía local de pescados y mariscos."},
                {"icon": "visibility", "title": "Mirador de la Península", "desc": "Una vista panorámica inigualable del contraste entre el desierto y el Océano Pacífico."}
            ],
            "included": ["Transporte turístico con aire acondicionado", "Guía profesional certificado en español", "Traslado ida y vuelta desde tu hotel", "Seguro de viaje de pasajeros"],
            "excluded": ["Boleto de ingreso SERNANP (S/ 11 adultos, S/ 5 niños)", "Almuerzo en caleta Lagunillas"],
            "schedule_label": "* Salida diaria a las 11:00 AM desde nuestra oficina o recojo en hotel. Duración: 3.5 horas aprox.",
            "faq_title": "Preguntas Frecuentes",
            "faqs": [
                {"q": "¿Cuánto cuesta el tour a la Reserva Nacional de Paracas?", "a": "Nuestro tour guiado cuesta S/ 50 por persona e incluye transporte, guía profesional y recojo en tu hotel de Paracas. Aparte se paga la entrada SERNANP: S/ 11 adultos y S/ 5 niños. Costo total real para un adulto: S/ 61, sin cobros adicionales."},
                {"q": "¿Qué se ve en el tour por la Reserva?", "a": "El circuito clásico incluye la Playa Roja (famosa por su arena granate), el mirador de La Catedral, los miradores del desierto costero y la caleta Lagunillas, donde puedes almorzar pescados y mariscos frente al mar."},
                {"q": "¿Se puede nadar en las playas de la Reserva?", "a": "En la mayoría de las playas del circuito el baño está prohibido por fuertes corrientes o para proteger la fauna. No obstante, en Playa La Mina o Raspón sí está permitido en tours específicos de temporada."},
                {"q": "¿Cuál es la tarifa de ingreso SERNANP?", "a": "La entrada general cuesta S/ 11 para adultos y S/ 5 para niños. Si también visitas las Islas Ballestas, te conviene el boleto combinado por S/ 22, válido por dos días."},
                {"q": "¿Qué debo llevar a la Reserva?", "a": "Bloqueador solar, sombrero o gorra con ajuste, lentes de sol, casaca cortavientos, agua y algo de efectivo para la entrada, artesanías o el almuerzo en Lagunillas. El clima es soleado y ventoso casi todo el año."},
                {"q": "¿Conviene ir en tour o por mi cuenta en bicicleta?", "a": "La bicicleta es una opción bonita pero exigente: son más de 30 km de recorrido con sol y viento fuerte. El tour guiado te lleva cómodo a todos los miradores, con explicación de la geología y la fauna, y con tiempo para fotos en cada parada."}
            ]
        },
        "en": {
            "title": "Paracas National Reserve Tour 2026: Red Beach & La Catedral | SolyMar",
            "desc": "Guided tour of the Paracas National Reserve: Red Beach, La Catedral viewpoint, Lagunillas cove and desert cliffs. 11 am departure with hotel pick-up. Local agency.",
            "h1": "Tour of the Paracas National Reserve",
            "keywords": "paracas national reserve tour, paracas national reserve price, red beach paracas, cathedral rock paracas, paracas entry fee, what to see in paracas reserve, what to bring paracas reserve, lagunillas beach",
            "subtitle": "Explore the only place in Peru where the desert plunges in colored cliffs straight into the Pacific Ocean.",
            "intro": "The <strong>Paracas National Reserve</strong> is Peru's only marine-coastal protected area of its kind: over 335,000 hectares where the desert, dramatic cliffs, and the cold Humboldt Current combine into landscapes you will not find anywhere else.",
            "intro_p2": "On this 3.5-hour land tour you will visit the famous <strong>Red Beach</strong>, the <strong>La Catedral</strong> viewpoint, the peninsula lookouts, and the fishing cove of <strong>Lagunillas</strong>, with guided photo stops at every point.",
            "intro_p3": "It is the perfect companion to the Ballestas Islands tour: in a single day you see both the marine and the desert side of Paracas, with hotel pick-up and drop-off included.",
            "why_title": "Highlights of the route",
            "why_items": [
                {"icon": "landscape", "title": "Red Beach", "desc": "Stunning dark red shoreline created by the erosion of nearby pink granodiorite cliffs."},
                {"icon": "auto_awesome", "title": "The Cathedral", "desc": "A viewpoint to the famous natural rock formation sculpted by wind and sea."},
                {"icon": "restaurant", "title": "Lagunillas Beach", "desc": "A charming fishing cove where we stop for a fresh seafood lunch by the ocean."},
                {"icon": "visibility", "title": "Desert Viewpoints", "desc": "Panoramas showing the stark contrast between dry yellow dunes and deep blue waters."}
            ],
            "included": ["Comfortable air-conditioned tourist transport", "Professional certified bilingual guide", "Hotel pick-up and drop-off in Paracas", "Passenger insurance"],
            "excluded": ["SERNANP park entrance fee (S/ 11 adults, S/ 5 children)", "Lunch at Lagunillas Beach"],
            "schedule_label": "* Daily departure at 11:00 AM from our office or hotel pick-up. Duration: approx. 3.5 hours.",
            "faq_title": "Frequently Asked Questions",
            "faqs": [
                {"q": "How much does the Paracas National Reserve tour cost?", "a": "Our guided tour costs S/ 50 per person and includes transport, a professional guide, and hotel pick-up in Paracas. The SERNANP entrance fee is paid separately: S/ 11 adults, S/ 5 children. Real total cost for an adult: S/ 61, with no extra charges."},
                {"q": "What will I see on the Reserve tour?", "a": "The classic circuit includes Red Beach (famous for its garnet-colored sand), the La Catedral viewpoint, the coastal desert lookouts, and Lagunillas fishing cove, where you can have a fresh seafood lunch by the ocean."},
                {"q": "Can you swim in the reserve beaches?", "a": "Swimming is prohibited at most stops due to strong currents and wildlife protection. However, swimming is allowed at specific spots like La Mina Beach on seasonal or private tours."},
                {"q": "How much is the park entrance fee?", "a": "The general entrance fee is S/ 11 for adults and S/ 5 for children. If you also plan to visit the Ballestas Islands, buy the combined ticket for S/ 22, valid for 2 days."},
                {"q": "What should I bring?", "a": "Sunscreen, a hat that straps on, sunglasses, a windbreaker, water, and some cash for the entrance fee, crafts, or lunch at Lagunillas. The weather is sunny and windy almost all year round."},
                {"q": "Is it better to visit by guided tour or by bicycle?", "a": "Cycling is scenic but demanding: the loop is over 30 km under strong sun and wind. The guided tour takes you comfortably to every viewpoint, explains the geology and wildlife, and leaves time for photos at each stop."}
            ]
        }
    },
    "ballestas-y-reserva-full-day": {
        "filename": "ballestas-y-reserva-full-day.html",
        "image": "img/ballestas-y-reserva-full-day.jpg",
        "price": "S/ 120",
        "price_val": "120",
        "price_cur": "PEN",
        "category": "desierto",
        "es": {
            "title": "Full Day Paracas 2026: Islas Ballestas + Reserva Nacional | SolyMar",
            "desc": "Lo mejor de Paracas en un día: Islas Ballestas a las 7:45 am y Reserva Nacional con Playa Roja al mediodía. Recojo en hotel o terminal de bus. Reserva directa por WhatsApp.",
            "h1": "Islas Ballestas + Reserva Nacional de Paracas en un día",
            "keywords": "full day paracas, full day paracas precio, tour paracas 1 dia, ballestas y reserva paracas, paracas en un dia, que hacer en paracas, tour completo paracas",
            "subtitle": "Lobos marinos y pingüinos por la mañana, Playa Roja y acantilados del desierto por la tarde: Paracas completo en un solo día.",
            "intro": "El <strong>Full Day Paracas</strong> es el itinerario preferido por quienes visitan Paracas por un día desde Lima o van de paso hacia Ica: combina el tour en lancha a las Islas Ballestas con el recorrido terrestre por la Reserva Nacional, sin tiempos muertos.",
            "intro_p2": "Empezamos a las 7:45 AM navegando hacia las <strong>Islas Ballestas</strong> para ver lobos marinos, pingüinos de Humboldt y el Candelabro. A media mañana continuamos por tierra hacia la <strong>Playa Roja, La Catedral y Lagunillas</strong> en la Reserva Nacional.",
            "intro_p3": "Todo coordinado por nuestro equipo local: recojo en tu hotel o en el terminal de bus, guías bilingües y guardado gratuito de equipaje en nuestra oficina si estás de paso.",
            "why_title": "Itinerario del Full Day",
            "why_items": [
                {"icon": "directions_boat", "title": "7:45 AM - Embarque Ballestas", "desc": "Embarque y navegación para observar el Candelabro, formaciones rocosas y fauna silvestre."},
                {"icon": "coffee", "title": "10:00 AM - Tiempo Libre", "desc": "Retorno al muelle de Paracas, tiempo libre para desayunar y caminar en el Boulevard El Chaco."},
                {"icon": "directions_bus", "title": "10:45 AM - Tour Reserva", "desc": "Inicio del tour terrestre hacia Playa Roja, miradores de la Catedral, y desierto costero."},
                {"icon": "restaurant", "title": "1:30 PM - Almuerzo y Retorno", "desc": "Tiempo libre para almorzar en Lagunillas antes de retornar a Paracas cerca de las 3:00 PM."}
            ],
            "included": ["Tour en lancha a Islas Ballestas", "Tour terrestre a la Reserva Nacional", "Guías bilingües certificados", "Traslado ida y vuelta desde tu hotel o estación de bus", "Seguro de viaje y chalecos salvavidas"],
            "excluded": ["Impuestos combinados de muelle y SERNANP (S/ 22 por persona)", "Almuerzos y bebidas"],
            "schedule_label": "* Salida diaria a las 7:45 AM. Retorno aproximado a las 3:00 PM. Ideal si vienes desde Lima o vas hacia Ica.",
            "faq_title": "Preguntas Frecuentes",
            "faqs": [
                {"q": "¿Cuánto cuesta el Full Day Paracas completo?", "a": "El tour cuesta S/ 120 por persona e incluye la lancha a Ballestas, el tour terrestre a la Reserva y los traslados. Aparte se paga el boleto combinado SERNANP + muelle de S/ 22 por adulto. Costo total real: S/ 142, sin cobros ocultos."},
                {"q": "¿Puedo hacer este tour si llego por la mañana en bus desde Lima?", "a": "Sí, es el caso más común. Si tu bus llega a Paracas antes de las 7:30 AM, te recogemos directamente en el terminal e iniciamos el tour de inmediato. Avísanos tu horario de llegada al reservar."},
                {"q": "¿Cuánto dura y a qué hora termina el tour?", "a": "Empieza a las 7:45 AM y termina aproximadamente a las 3:00 PM en Paracas, a tiempo para tomar un bus de tarde hacia Lima, Ica o Huacachina."},
                {"q": "¿El almuerzo está incluido?", "a": "No, pero el itinerario incluye una parada en la caleta Lagunillas, dentro de la Reserva, donde encontrarás restaurantes de pescados y mariscos frente al mar a buen precio."},
                {"q": "¿Se puede llevar equipaje durante el tour?", "a": "Sí, guardamos tus maletas gratis y de forma segura en nuestra oficina de Paracas mientras realizas los tours. Ideal si estás de paso entre Lima e Ica."},
                {"q": "¿Qué debo llevar?", "a": "Cortavientos, bloqueador, gorra con ajuste, lentes de sol, agua y efectivo para los impuestos y el almuerzo. Por la mañana en el mar hace algo de frío y al mediodía en el desierto el sol es fuerte: vístete en capas."}
            ]
        },
        "en": {
            "title": "Paracas Full Day 2026: Ballestas Islands + National Reserve | SolyMar",
            "desc": "The best of Paracas in one day: Ballestas Islands at 7:45 am and the National Reserve with Red Beach at noon. Hotel or bus terminal pick-up. Book directly via WhatsApp.",
            "h1": "Ballestas Islands & National Reserve in One Day",
            "keywords": "full day paracas, paracas full day price, paracas 1 day tour, ballestas and reserve paracas, paracas in one day, what to do in paracas, paracas day trip",
            "subtitle": "Sea lions and penguins in the morning, Red Beach and desert cliffs in the afternoon: all of Paracas in a single day.",
            "intro": "The <strong>Paracas Full Day</strong> is the favorite itinerary for travelers visiting Paracas on a day trip from Lima or passing through towards Ica: it combines the Ballestas Islands boat tour with the National Reserve land tour, with zero wasted time.",
            "intro_p2": "We start at 7:45 AM sailing to the <strong>Ballestas Islands</strong> to see sea lions, Humboldt penguins, and the Candelabra. Mid-morning we continue by land to <strong>Red Beach, La Catedral, and Lagunillas</strong> in the National Reserve.",
            "intro_p3": "Everything is coordinated by our local team: pick-up at your hotel or the bus terminal, bilingual guides, and free luggage storage at our office if you are passing through.",
            "why_title": "Full Day Itinerary",
            "why_items": [
                {"icon": "directions_boat", "title": "7:45 AM - Boat Boarding", "desc": "Boarding and navigation to observe the Candelabra geoglyph, rock arches, and marine wildlife."},
                {"icon": "coffee", "title": "10:00 AM - Free Time", "desc": "Return to El Chaco pier, time to grab a coffee or stroll around the bay Boulevard."},
                {"icon": "directions_bus", "title": "10:45 AM - Reserve Tour", "desc": "Start of the coastal land tour towards Red Beach, Cathedral viewpoint, and dunes."},
                {"icon": "restaurant", "title": "1:30 PM - Lunch & Return", "desc": "Free time to lunch at Lagunillas fishermen cove, returning to Paracas town at around 3:00 PM."}
            ],
            "included": ["Speedboat tour to the Ballestas Islands", "Land tour to the Paracas National Reserve", "Certified bilingual guides (English/Spanish)", "Pick-up and drop-off from hotel or bus station", "Passenger insurance and safety equipment"],
            "excluded": ["Combined park entrance & pier fee (S/ 22 per person)", "Lunch and drinks"],
            "schedule_label": "* Daily departures at 7:45 AM. Return around 3:00 PM. Perfect for travelers coming from Lima or heading to Ica.",
            "faq_title": "Frequently Asked Questions",
            "faqs": [
                {"q": "How much does the Paracas Full Day cost in total?", "a": "The tour costs S/ 120 per person and includes the Ballestas boat trip, the Reserve land tour, and transfers. The combined SERNANP + pier tax of S/ 22 per adult is paid separately. Real total cost: S/ 142, with no hidden charges."},
                {"q": "Can I join this tour if I arrive by bus from Lima in the morning?", "a": "Yes, this is the most common case. If your bus arrives in Paracas before 7:30 AM, we pick you up directly at the terminal and start the tour right away. Let us know your arrival time when booking."},
                {"q": "How long is the tour and when does it end?", "a": "It starts at 7:45 AM and ends around 3:00 PM in Paracas, in time to catch an afternoon bus to Lima, Ica, or Huacachina."},
                {"q": "Is lunch included?", "a": "No, but the itinerary includes a stop at Lagunillas cove, inside the Reserve, where you will find well-priced seafood restaurants right by the ocean."},
                {"q": "Can I store my luggage during the tour?", "a": "Yes, we store your bags for free and safely at our Paracas office while you are out on the tours. Perfect if you are passing through between Lima and Ica."},
                {"q": "What should I bring?", "a": "A windbreaker, sunscreen, a hat that straps on, sunglasses, water, and cash for the taxes and lunch. Mornings at sea are chilly and the midday desert sun is strong: dress in layers."}
            ]
        }
    },
    "buggies-sandboard-huacachina": {
        "filename": "buggies-sandboard-huacachina.html",
        "image": "img/huacachina.jpg",
        "price": "S/ 70",
        "price_val": "70",
        "price_cur": "PEN",
        "category": "desierto",
        "es": {
            "title": "Buggies y Sandboard en Huacachina 2026: Precio y Horarios | SolyMar",
            "desc": "Buggies tubulares y sandboard en las dunas de Huacachina, Ica, con operador formal: jaula antivuelco, arneses y chofer autorizado. Tour al atardecer con tabla incluida.",
            "h1": "Tour en Buggies y Sandboard en el desierto de Huacachina",
            "keywords": "buggies huacachina precio, sandboard huacachina, tour huacachina, tour buggies huacachina seguro, carros areneros ica, huacachina atardecer, que hacer en huacachina",
            "subtitle": "Siente la adrenalina recorriendo las dunas más altas de Sudamérica en un arenero tubular y deslizándote en tabla al atardecer.",
            "intro": "El <strong>Oasis de Huacachina</strong>, a 5 minutos de Ica, es el único oasis natural de Sudamérica: una laguna rodeada de palmeras en medio de dunas gigantes de arena fina. El tour en buggies y sandboard es su experiencia imperdible.",
            "intro_p2": "Nuestros <strong>buggies tubulares con jaula antivuelco y arneses</strong> te llevan en una montaña rusa por el desierto, conducidos por choferes autorizados que conocen cada duna. En las cumbres más altas paramos para que practiques <strong>sandboard</strong> con tabla y cera incluidas.",
            "intro_p3": "La jornada termina en un mirador natural del desierto, justo a tiempo para uno de los atardeceres más dorados del Perú. Importante: trabaja siempre con operadores formales y asegurados, como exige la autoridad regional.",
            "why_title": "¿Cómo es la aventura?",
            "why_items": [
                {"icon": "toys", "title": "Buggies Tubulares", "desc": "Vehículos areneros diseñados para subir y bajar dunas empinadas a alta velocidad con total seguridad."},
                {"icon": "sports_skateboarding", "title": "Sandboarding Libre", "desc": "Tablas incluidas. Puedes deslizarte de pie, sentado o recostado boca abajo para mayor diversión."},
                {"icon": "wb_twilight", "title": "Atardecer en el Desierto", "desc": "Parada estratégica para tomar fotos espectaculares de la puesta del sol sobre la arena."},
                {"icon": "landscape", "title": "El Oasis desde lo Alto", "desc": "Vistas increíbles de la laguna de Huacachina escondida en medio de las dunas gigantes."}
            ],
            "included": ["Recorrido en carro arenero tubular (buggy)", "Tablas de sandboard y cera especial", "Chofer profesional experimentado", "Punto de encuentro en Huacachina, Ica"],
            "excluded": ["Tasa de ingreso municipal al desierto (S/ 4.00 aprox.)", "Traslado Paracas-Ica (disponible como adicional)"],
            "schedule_label": "* Turnos recomendados a las 4:00 PM y 4:30 PM para disfrutar de la puesta del sol sin el calor sofocante del mediodía.",
            "faq_title": "Preguntas Frecuentes",
            "faqs": [
                {"q": "¿Cuánto cuesta el tour en buggies y sandboard en Huacachina?", "a": "Nuestro tour cuesta S/ 70 por persona e incluye el recorrido en buggy tubular, tablas de sandboard con cera y chofer profesional. Aparte se paga la tasa municipal de ingreso al desierto (S/ 4 aprox.). Te confirmamos el costo total antes de reservar, sin sorpresas."},
                {"q": "¿Es seguro el tour en buggies?", "a": "Con un operador formal, sí. Todos nuestros vehículos cuentan con jaula antivuelco, asientos con arnés y choferes autorizados con experiencia en el desierto. Evita los tours informales ofrecidos en la calle sin seguro ni revisión técnica: las autoridades de Ica han advertido sobre ellos."},
                {"q": "¿Se requiere experiencia para el Sandboard?", "a": "Ninguna. Si es tu primera vez, puedes deslizarte echado boca abajo (modo trineo), lo cual es sumamente fácil, seguro y divertido. Los más experimentados pueden intentarlo sentados o de pie."},
                {"q": "¿Cuál es el mejor horario para el tour?", "a": "El turno de 4:00 PM es el favorito: la arena ya no quema, la luz es perfecta para fotos y terminas viendo la puesta de sol desde lo alto de las dunas. En verano también es agradable el primer turno de la mañana."},
                {"q": "¿Cómo llego de Paracas a Huacachina?", "a": "Huacachina está a 1 hora y 20 minutos de Paracas. Ofrecemos traslados privados o puedes tomar un bus interprovincial a Ica y luego un taxi local de 10 minutos. También tenemos el tour combinado Paracas + Huacachina en un día."},
                {"q": "¿Qué debo llevar?", "a": "Lentes de sol o antiparras (el viento levanta arena), zapatillas cerradas, bloqueador y tu celular o cámara bien asegurados. Evita llevar objetos sueltos: en el buggy todo debe ir sujeto."}
            ]
        },
        "en": {
            "title": "Huacachina Dune Buggy & Sandboarding 2026: Price & Times | SolyMar",
            "desc": "Dune buggies and sandboarding on the Huacachina dunes, Ica, with a licensed operator: roll cage, harnesses and authorized drivers. Sunset tour, board included.",
            "h1": "Dune Buggy & Sandboarding Tour in Huacachina",
            "keywords": "huacachina dune buggy price, sandboarding huacachina, huacachina tour, safe buggy tour huacachina, sand dunes ica, huacachina sunset tour, things to do huacachina",
            "subtitle": "Feel the thrill riding the highest sand dunes in South America on a tubular buggy and sliding down on a sandboard at sunset.",
            "intro": "The <strong>Huacachina Oasis</strong>, 5 minutes from Ica, is South America's only natural desert oasis: a palm-fringed lagoon surrounded by giant dunes of fine sand. The dune buggy and sandboarding tour is its must-do experience.",
            "intro_p2": "Our <strong>tubular buggies with roll cages and harnesses</strong> take you on a desert rollercoaster, driven by authorized drivers who know every dune. At the highest crests we stop so you can go <strong>sandboarding</strong>, with boards and wax included.",
            "intro_p3": "The ride ends at a natural desert viewpoint just in time for one of Peru's most golden sunsets. Important: always ride with licensed, insured operators, as regional authorities require.",
            "why_title": "What to expect on this tour",
            "why_items": [
                {"icon": "toys", "title": "Tubular Buggy Ride", "desc": "Custom-built sand dunes vehicles with professional drivers for a safe and thrilling roller-coaster ride."},
                {"icon": "sports_skateboarding", "title": "Sandboarding Fun", "desc": "Boards are included. You can slide down standing, sitting, or lying face down for maximum speed."},
                {"icon": "wb_twilight", "title": "Sunset Spot", "desc": "A scenic stop to take photos of the beautiful sunset painting the desert gold."},
                {"icon": "landscape", "title": "Oasis Panoramic View", "desc": "Get amazing birds-eye shots of the beautiful lagoon nestled in the middle of the dunes."}
            ],
            "included": ["Dune buggy ride with professional driver", "Sandboards and wax", "Full safety equipment (harness/roll-cage)", "Meeting point in Huacachina Oasis, Ica"],
            "excluded": ["Municipal desert entry tax (approx. S/ 4.00)", "Transfer from Paracas to Ica (available as an extra)"],
            "schedule_label": "* Best times are 4:00 PM and 4:30 PM to enjoy the sunset and avoid the intense midday heat.",
            "faq_title": "Frequently Asked Questions",
            "faqs": [
                {"q": "How much does the Huacachina buggy and sandboarding tour cost?", "a": "Our tour costs S/ 70 per person and includes the tubular buggy ride, sandboards with wax, and a professional driver. The municipal desert entrance fee (approx. S/ 4) is paid separately. We confirm the total cost before you book, with no surprises."},
                {"q": "Is the dune buggy tour safe?", "a": "With a licensed operator, yes. All our buggies have roll cages, harness seats, and authorized, experienced desert drivers. Avoid informal street-sold tours without insurance or technical inspection; regional authorities have issued warnings about them."},
                {"q": "Do I need sandboarding experience?", "a": "Not at all. Beginners can slide down lying flat on their stomachs (sled style), which is extremely easy, safe, and fun. More adventurous riders can try sitting or standing."},
                {"q": "What is the best time for the tour?", "a": "The 4:00 PM slot is the favorite: the sand is no longer scorching, the light is perfect for photos, and you finish watching the sunset from the top of the dunes. In summer, the early morning slot is also pleasant."},
                {"q": "How do I get from Paracas to Huacachina?", "a": "Huacachina is about 1 hour and 20 minutes from Paracas. We can arrange a private transfer, or you can take an intercity bus to Ica plus a 10-minute taxi. We also offer the combined Paracas + Huacachina full-day tour."},
                {"q": "What should I bring?", "a": "Sunglasses or goggles (the wind kicks up sand), closed shoes, sunscreen, and your phone or camera well secured. Avoid loose items: everything must be strapped down in the buggy."}
            ]
        }
    },
    "ruta-del-pisco-bodegas-ica": {
        "filename": "ruta-del-pisco-bodegas-ica.html",
        "image": "img/ruta-del-pisco.jpg",
        "price": "S/ 80",
        "price_val": "80",
        "price_cur": "PEN",
        "category": "cultura",
        "es": {
            "title": "Ruta del Pisco en Ica 2026: Tour de Bodegas con Degustación | SolyMar",
            "desc": "Tour por bodegas tradicionales y artesanales del valle de Ica con degustación de piscos, vinos y cachina. Salidas desde Paracas o Ica con transporte incluido.",
            "h1": "Tour Ruta del Pisco: bodegas y viñedos de Ica",
            "keywords": "ruta del pisco ica, tour bodegas ica, degustacion pisco ica, bodegas de vino ica, tour del pisco, que bodegas visitar en ica, cata de pisco",
            "subtitle": "Recorre bodegas vitivinícolas históricas y artesanales del valle más pisquero del Perú, con degustaciones guiadas en cada parada.",
            "intro": "El Pisco es la bebida bandera del Perú y el <strong>valle de Ica</strong> es su cuna histórica: aquí se cultivan las uvas pisqueras desde el siglo XVI. En la <strong>Ruta del Pisco</strong> conocerás este legado de la mano de productores locales.",
            "intro_p2": "Visitamos una combinación de <strong>bodegas industriales de renombre y bodegas artesanales</strong> que aún emplean lagares de pisado de uva, alambiques y falcas de la época colonial, donde el proceso se explica de principio a fin.",
            "intro_p3": "En cada parada disfrutarás de <strong>degustaciones guiadas</strong> de Pisco en sus distintas variedades (Quebranta, Italia, Acholado), además de vinos dulces, cachinas y mistelas típicas de Ica.",
            "why_title": "Bodegas incluidas en el recorrido",
            "why_items": [
                {"icon": "wine_bar", "title": "Bodegas Artesanales", "desc": "Aprende el método tradicional que se mantiene intacto desde el siglo XVI, usando lagares de pisado de uva."},
                {"icon": "domain", "title": "Bodegas Industriales", "desc": "Visita viñedos modernos y conoce el proceso tecnificado de destilación a gran escala."},
                {"icon": "restaurant", "title": "Gastronomía Iqueña", "desc": "Las bodegas cuentan con excelentes restaurantes donde podrás almorzar platos típicos como la sopa seca o carapulcra."},
                {"icon": "local_bar", "title": "Degustación Completa", "desc": "Prueba piscos puros, acholados, vinos macerados y licores de crema de pisco."}
            ],
            "included": ["Transporte privado/compartido ida y vuelta", "Guía local conocedor de la historia del Pisco", "Degustaciones de piscos y vinos en cada parada"],
            "excluded": ["Entradas a las bodegas (corren por cuenta del cliente)", "Almuerzo en bodega (disponible a la carta)", "Botellas de Pisco compradas como souvenir"],
            "schedule_label": "* Salidas diarias a las 10:30 AM desde Ica o Paracas. Duración: 4.5 horas aprox.",
            "faq_title": "Preguntas Frecuentes",
            "faqs": [
                {"q": "¿Cuánto cuesta el tour de la Ruta del Pisco?", "a": "El tour cuesta S/ 80 por persona e incluye transporte ida y vuelta desde Paracas o Ica, guía local y degustaciones en cada parada. No incluye las entradas a las bodegas (corren por cuenta del cliente), almuerzo ni botellas compradas."},
                {"q": "¿Qué bodegas se visitan?", "a": "El circuito combina bodegas industriales reconocidas del valle de Ica con bodegas artesanales familiares que conservan lagares y alambiques coloniales. La selección puede variar según el día y la temporada de vendimia."},
                {"q": "¿Pueden realizar el tour personas menores de edad?", "a": "Sí, los niños y adolescentes son bienvenidos para conocer la historia y los viñedos, pero la degustación de bebidas alcohólicas está estrictamente reservada para mayores de 18 años."},
                {"q": "¿Incluye almuerzo el tour?", "a": "El tour hace una parada de almuerzo en una de las bodegas campestres, donde puedes probar platos iqueños como la carapulcra con sopa seca. El almuerzo se paga directamente según consumo."},
                {"q": "¿Es posible comprar piscos y vinos en las bodegas?", "a": "Sí, todas las bodegas cuentan con tiendas a precio de productor. Es la mejor oportunidad para llevar un pisco puro o una crema de pisco de recuerdo."},
                {"q": "¿Cuál es la mejor época para hacer la Ruta del Pisco?", "a": "Todo el año es buena época, pero de febrero a marzo coincide con la vendimia: verás la cosecha y el pisado de la uva en vivo, y en marzo se celebra el Festival Internacional de la Vendimia de Ica."}
            ]
        },
        "en": {
            "title": "Pisco Route in Ica 2026: Winery Tour & Tastings | SolyMar Paracas",
            "desc": "Tour traditional and artisanal wineries in the Ica valley with tastings of Pisco, wines and cachina. Departures from Paracas or Ica with transport included.",
            "h1": "Pisco Route Tour: Wineries & Vineyards of Ica",
            "keywords": "pisco route ica, winery tour ica, pisco tasting peru, wine cellars ica, pisco tour from paracas, which wineries to visit in ica, pisco tasting tour",
            "subtitle": "Visit historic and artisanal wineries in Peru's premier Pisco valley, with guided tastings at every stop.",
            "intro": "Pisco is Peru's national spirit and the sunny <strong>Ica valley</strong> is its historical cradle: Pisco grapes have been grown here since the 16th century. On the <strong>Pisco Route</strong> you will discover this heritage guided by local producers.",
            "intro_p2": "We visit a combination of <strong>renowned industrial wineries and family-run artisanal bodegas</strong> that still use grape-stomping presses, colonial-era stills, and clay jars (botijas), with the whole process explained from vine to glass.",
            "intro_p3": "At each stop you will enjoy <strong>guided tastings</strong> of different Pisco varieties (Quebranta, Italia, Acholado), plus sweet wines, cachina, and traditional mistelas from Ica.",
            "why_title": "Wineries & Experiences",
            "why_items": [
                {"icon": "wine_bar", "title": "Artisanal Methods", "desc": "Learn how small wineries press grapes and ferment wine in ancient clay vessels from the 16th century."},
                {"icon": "domain", "title": "Modern Distilleries", "desc": "Explore modern production plants and witness high-tech fermentation and packaging."},
                {"icon": "restaurant", "title": "Local Creole Food", "desc": "We stop at countryside winery restaurants where you can enjoy traditional dishes like Carapulcra and Sopa Seca."},
                {"icon": "local_bar", "title": "Premium Tasting", "desc": "Sample pure Piscos, blended Acholados, aromatic sweet wines, and Pisco cream liqueurs."}
            ],
            "included": ["Round-trip transport from Paracas or Ica", "Local tour guide specializing in wine & spirits", "Guided tastings at all locations"],
            "excluded": ["Winery entrance tickets (paid directly by the customer)", "Lunch at the winery (available à la carte)", "Bottled wines or spirits purchased as souvenirs"],
            "schedule_label": "* Daily departures at 10:30 AM from Ica or Paracas. Duration: approx. 4.5 hours.",
            "faq_title": "Frequently Asked Questions",
            "faqs": [
                {"q": "How much does the Pisco Route tour cost?", "a": "The tour costs S/ 80 per person and includes round-trip transport from Paracas or Ica, a local guide, and tastings at every stop. Winery entrance tickets are not included (at customer's expense), nor is lunch or purchased bottles."},
                {"q": "Which wineries do we visit?", "a": "The circuit combines renowned industrial wineries of the Ica valley with family-run artisanal bodegas that preserve colonial presses and stills. The selection may vary by day and by harvest season."},
                {"q": "Can minors join the tour?", "a": "Yes, children and teenagers are welcome to learn about the history and explore the vineyards. However, the alcohol tastings are strictly for adults aged 18 and older."},
                {"q": "Is lunch included in the price?", "a": "No, the tour stops at a countryside winery restaurant where you can try Ica specialties like carapulcra with sopa seca. Meals are paid directly at the restaurant."},
                {"q": "Can I buy wines and Piscos directly at the wineries?", "a": "Yes, all wineries have shops selling at cellar-door prices. It is the best chance to take home a pure Pisco or a Pisco cream liqueur."},
                {"q": "When is the best time for the Pisco Route?", "a": "The tour runs great all year, but February-March coincides with the grape harvest (vendimia): you will see the picking and grape-stomping live, and in March, Ica celebrates its International Harvest Festival."}
            ]
        }
    },
    "paracas-huacachina-full-day": {
        "filename": "paracas-huacachina-full-day.html",
        "image": "img/huacachina.jpg",
        "price": "S/ 190",
        "price_val": "190",
        "price_cur": "PEN",
        "category": "desierto",
        "es": {
            "title": "Paracas y Huacachina en 1 Día 2026: Ballestas + Buggies | SolyMar",
            "desc": "Islas Ballestas por la mañana y buggies con sandboard en Huacachina por la tarde. El full day más completo del sur desde Paracas, con traslados incluidos. Reserva por WhatsApp.",
            "h1": "Paracas + Huacachina en un solo día",
            "keywords": "paracas y huacachina en un dia, tour paracas huacachina, ballestas y huacachina, full day ica paracas, paracas huacachina precio, ruta sur peru",
            "subtitle": "Navega junto a lobos marinos en Paracas por la mañana y vive la adrenalina de las dunas de Huacachina por la tarde.",
            "intro": "El <strong>Full Day Paracas + Huacachina</strong> combina las dos mayores atracciones del sur del Perú en una sola jornada: la fauna marina de las Islas Ballestas y las dunas gigantes del único oasis natural de Sudamérica.",
            "intro_p2": "Comienzas a las 8:00 AM a bordo de una lancha hacia las <strong>Islas Ballestas</strong>. Luego te trasladamos en transporte climatizado al <strong>Oasis de Huacachina</strong>, con tiempo para almorzar frente a la laguna, y a las 4:00 PM subes al buggy tubular para el circuito de dunas y sandboard al atardecer.",
            "intro_p3": "Es la opción definitiva para la ruta sur: puedes regresar a Paracas o quedarte en Huacachina y continuar hacia Nazca o Arequipa, con tu equipaje viajando seguro en nuestro transporte.",
            "why_title": "Itinerario Detallado",
            "why_items": [
                {"icon": "directions_boat", "title": "8:00 AM - Islas Ballestas", "desc": "Navegación de 2 horas para conocer el Candelabro y la fauna de las islas."},
                {"icon": "directions_bus", "title": "10:30 AM - Viaje Paracas a Ica", "desc": "Traslado en transporte turístico climatizado hacia la ciudad de Ica y el Oasis de Huacachina."},
                {"icon": "restaurant", "title": "12:30 PM - Almuerzo y Paseo", "desc": "Tiempo libre en el Oasis de Huacachina para caminar, almorzar frente a la laguna o comprar souvenirs."},
                {"icon": "toys", "title": "4:00 PM - Buggies e Ica Sunset", "desc": "Tour de adrenalina pura en tubulares areneros y sandboarding por las dunas al atardecer."}
            ],
            "included": ["Navegación en lancha a Islas Ballestas", "Traslado interprovincial Paracas-Ica (Huacachina)", "Tour en carros areneros tubulares en Huacachina", "Tablas y guía para la práctica de sandboarding", "Seguro de viaje y asistencia en los puntos"],
            "excluded": ["Impuestos combinados de muelle y SERNANP (S/ 16.00 aprox.)", "Tasa municipal de desierto en Huacachina (S/ 4.00 aprox.)", "Almuerzo y bebidas"],
            "schedule_label": "* Salida diaria a las 7:45 AM desde el muelle de Paracas. Retorno opcional a Paracas o puedes quedarte en Ica (Huacachina) al finalizar el tour a las 6:30 PM.",
            "faq_title": "Preguntas Frecuentes",
            "faqs": [
                {"q": "¿Cuánto cuesta el tour Paracas + Huacachina en un día?", "a": "El tour cuesta S/ 190 por persona e incluye lancha a Ballestas, traslado Paracas-Huacachina, buggies tubulares y sandboard. Aparte se pagan los impuestos de muelle y SERNANP (S/ 16 aprox.) y la tasa municipal del desierto (S/ 4 aprox.). Total real aproximado: S/ 210, sin cobros ocultos."},
                {"q": "¿Puedo quedarme en Huacachina al finalizar el tour?", "a": "¡Sí! Muchos viajeros continúan su ruta al sur hacia Nazca o Arequipa. Puedes finalizar el tour en Huacachina con tu equipaje a bordo de nuestro transporte sin costo extra. Avísanos al reservar."},
                {"q": "¿Qué pasa con mis maletas durante el día?", "a": "Las maletas viajan seguras en la maletera del transporte climatizado que te lleva de Paracas a Huacachina, por lo que no tienes que preocuparte por dejarlas en ningún hotel."},
                {"q": "¿El tour incluye comida?", "a": "No, pero el itinerario deja tiempo libre en el oasis, donde hay una amplia variedad de restaurantes para almorzar comida criolla, marina o internacional frente a la laguna."},
                {"q": "¿Es un día muy agotador?", "a": "Es un día completo (de 7:45 AM a 6:30 PM aprox.) pero bien balanceado: navegación tranquila por la mañana, traslado con descanso al mediodía y la adrenalina de los buggies recién a las 4:00 PM. La mayoría lo termina con energía para la puesta de sol."},
                {"q": "¿Qué debo llevar?", "a": "Cortavientos para la lancha, bloqueador, lentes de sol, gorra, zapatillas cerradas para el sandboard y efectivo para impuestos y almuerzo. Todo lo demás (chalecos, tablas, cera) lo ponemos nosotros."}
            ]
        },
        "en": {
            "title": "Paracas & Huacachina in One Day 2026: Ballestas + Buggies | SolyMar",
            "desc": "Ballestas Islands boat tour in the morning and Huacachina dune buggies with sandboarding in the afternoon. The most complete full day from Paracas, transfers included.",
            "h1": "Paracas & Huacachina Full Day Tour",
            "keywords": "paracas and huacachina one day, paracas huacachina tour, ballestas and huacachina, full day ica paracas, paracas huacachina price, peru south route",
            "subtitle": "Sail alongside sea lions in Paracas by morning and ride the giant dunes of Huacachina by afternoon.",
            "intro": "The <strong>Paracas + Huacachina Full Day</strong> combines the two greatest attractions of southern Peru in a single day: the marine wildlife of the Ballestas Islands and the giant dunes of South America's only natural oasis.",
            "intro_p2": "You start at 8:00 AM sailing to the <strong>Ballestas Islands</strong>. Then we drive you in air-conditioned transport to the <strong>Huacachina Oasis</strong>, with time for lunch by the lagoon, and at 4:00 PM you board the tubular buggy for the dune circuit and sunset sandboarding.",
            "intro_p3": "It is the definitive option for the southern route: return to Paracas or stay in Huacachina and continue to Nazca or Arequipa, with your luggage traveling safely in our vehicle.",
            "why_title": "Detailed Itinerary",
            "why_items": [
                {"icon": "directions_boat", "title": "8:00 AM - Ballestas Islands", "desc": "2-hour speedboat tour to see the Candelabra geoglyph and island marine fauna."},
                {"icon": "directions_bus", "title": "10:30 AM - Drive Paracas to Ica", "desc": "Travel in an air-conditioned tourist minivan to the city of Ica and the Huacachina Oasis."},
                {"icon": "restaurant", "title": "12:30 PM - Lunch & Oasis Walk", "desc": "Free time to enjoy lunch overlooking the lagoon, walk around the oasis, or buy souvenirs."},
                {"icon": "toys", "title": "4:00 PM - Buggies & Sandboarding", "desc": "Exciting dune buggy ride and sandboarding adventure on the giant dunes at sunset."}
            ],
            "included": ["Speedboat tour to the Ballestas Islands", "Direct tourist transfer from Paracas to Huacachina (Ica)", "Tubular buggy tour in the Huacachina desert", "Sandboarding equipment and instruction", "Passenger insurance and travel coordinator assistance"],
            "excluded": ["Combined Ballestas/SERNANP tax (approx. S/ 16.00)", "Huacachina desert entrance tax (approx. S/ 4.00)", "Lunch and drinks"],
            "schedule_label": "* Daily departures at 7:45 AM. You can return to Paracas at the end of the tour or stay in Huacachina/Ica after 6:30 PM.",
            "faq_title": "Frequently Asked Questions",
            "faqs": [
                {"q": "How much does the Paracas + Huacachina one-day tour cost?", "a": "The tour costs S/ 190 per person and includes the Ballestas boat trip, the Paracas-Huacachina transfer, tubular buggies, and sandboarding. Pier/SERNANP taxes (approx. S/ 16) and the municipal desert fee (approx. S/ 4) are paid separately. Approximate real total: S/ 210, no hidden charges."},
                {"q": "Can I finish the tour in Huacachina instead of returning to Paracas?", "a": "Yes! Many travelers continue south to Nazca or Arequipa. You can end your day in Huacachina with your luggage on board at no extra cost. Just let us know when booking."},
                {"q": "Where is my luggage kept during the tour?", "a": "Your bags travel securely in the trunk of the air-conditioned vehicle that takes you from Paracas to Huacachina, so you never have to leave them at a hotel."},
                {"q": "Is food included in the tour?", "a": "No, but the itinerary leaves free time at the oasis, where you will find plenty of restaurants serving Peruvian, seafood, and international dishes by the lagoon."},
                {"q": "Is it an exhausting day?", "a": "It is a full day (approx. 7:45 AM to 6:30 PM) but well balanced: a calm boat ride in the morning, a restful transfer at noon, and the buggy adrenaline only at 4:00 PM. Most travelers finish with energy to spare for the sunset."},
                {"q": "What should I bring?", "a": "A windbreaker for the boat, sunscreen, sunglasses, a cap, closed shoes for sandboarding, and cash for taxes and lunch. Everything else (life jackets, boards, wax) is on us."}
            ]
        }
    },
    "parapente": {
        "filename": "parapente.html",
        "image": "img/parapente.jpg",
        "price": "S/ 250",
        "price_val": "250",
        "price_cur": "PEN",
        "category": "aire",
        "es": {
            "title": "Parapente en Paracas 2026: Vuelo Tándem con Video Incluido | SolyMar",
            "desc": "Vuelo en parapente biplaza sobre los acantilados de la Reserva de Paracas con piloto certificado APVL. Sin experiencia previa, video GoPro incluido. Reserva por WhatsApp.",
            "h1": "Vuelo en parapente sobre Paracas",
            "keywords": "parapente paracas, parapente paracas precio, vuelo tandem paracas, volar en parapente peru, parapente ica, parapente playa supay, deportes de aventura paracas",
            "subtitle": "Flota sobre los acantilados dorados y el mar turquesa de la Reserva Nacional de Paracas junto a un piloto certificado.",
            "intro": "Volar en <strong>parapente en Paracas</strong> es una de las experiencias de aventura más impresionantes de la costa peruana. Se realiza en modalidad tándem (biplaza), acompañado en todo momento de un piloto instructor certificado por la APVL.",
            "intro_p2": "Despegamos desde los altos acantilados de la Reserva, en puntos como <strong>Playa Supay o el Cerro Mirador</strong>, donde el viento marino constante de Paracas eleva el parapente suavemente sobre el contraste único del desierto y el mar.",
            "intro_p3": "No necesitas entrenamiento previo ni \"saltar al vacío\": el inflado del parapente es progresivo y el despegue se siente como empezar a flotar desde el suelo. A los pocos segundos ya estarás planeando con vista a toda la bahía.",
            "why_title": "Detalles del vuelo en parapente",
            "why_items": [
                {"icon": "account_circle", "title": "Piloto Instructor", "desc": "Vuelas acoplado a un piloto profesional certificado por la APVL (Asociación Peruana de Vuelo Libre)."},
                {"icon": "video_camera_back", "title": "Video HD Incluido", "desc": "Te grabamos en video de alta definición con una cámara de acción GoPro durante el vuelo para tu recuerdo."},
                {"icon": "wind_power", "title": "Vuelo de 10-15 Minutos", "desc": "Tiempo de vuelo suspendido en el aire aprovechando las corrientes térmicas y el viento costero."},
                {"icon": "explore", "title": "Vistas Espectaculares", "desc": "Contempla la bahía, las dunas, el mar y los impresionantes acantilados desérticos desde las alturas."}
            ],
            "included": ["Vuelo biplaza con piloto instructor certificado", "Uso de casco e insumos de seguridad", "Video grabado en alta definición con GoPro (traer tarjeta MicroSD o celular)", "Traslado ida y vuelta al punto de despegue en la Reserva"],
            "excluded": ["Boleto de ingreso a la Reserva Nacional (S/ 11.00)"],
            "schedule_label": "* El vuelo está sujeto a condiciones óptimas de viento. Típicamente se realiza entre la 1:00 PM y las 5:00 PM.",
            "faq_title": "Preguntas Frecuentes",
            "faqs": [
                {"q": "¿Cuánto cuesta volar en parapente en Paracas?", "a": "El vuelo tándem cuesta S/ 250 por persona e incluye piloto certificado, equipo de seguridad completo, video GoPro de tu vuelo y traslado al punto de despegue. Solo se paga aparte la entrada a la Reserva (S/ 11)."},
                {"q": "¿Cuánto dura el vuelo?", "a": "El vuelo dura entre 10 y 15 minutos según las condiciones de viento, más el tiempo de preparación y la charla de seguridad. La experiencia completa toma alrededor de 1 hora."},
                {"q": "¿Necesito experiencia para volar?", "a": "Ninguna. El piloto se encarga de todo el control del parapente. Tú solo debes seguir sus indicaciones básicas: correr unos pasos en el despegue y levantar las piernas al aterrizar."},
                {"q": "¿Da miedo o produce vértigo?", "a": "Menos de lo que imaginas. No hay caída libre ni giros bruscos: el vuelo es suave y estable, como estar sentado en una silla flotante. La mayoría de pasajeros se relaja a los pocos segundos y hasta pide acrobacias al final."},
                {"q": "¿Hay límites de edad o peso?", "a": "El peso del pasajero debe estar entre 40 kg y 90 kg por seguridad. Los menores de edad pueden volar con autorización escrita de sus padres."},
                {"q": "¿Qué pasa si no hay viento el día programado?", "a": "El vuelo libre depende del viento. Si es insuficiente o muy fuerte, esperamos a que mejore dentro de la ventana de la tarde o reprogramamos la actividad sin costo para garantizar tu seguridad."},
                {"q": "¿Qué ropa debo llevar?", "a": "Ropa cómoda de manga larga, pantalón largo y zapatillas cerradas bien ajustadas. Nosotros ponemos el casco y el arnés. Si llevas celular, debe ir bien asegurado o dejarlo con nuestro equipo en tierra."}
            ]
        },
        "en": {
            "title": "Paragliding in Paracas 2026: Tandem Flight + HD Video | SolyMar",
            "desc": "Tandem paragliding over the cliffs of the Paracas Reserve with an APVL-certified pilot. No experience needed, GoPro video included. Book via WhatsApp.",
            "h1": "Paragliding Flight over Paracas",
            "keywords": "paragliding paracas, paragliding paracas price, tandem flight paracas, paragliding peru, paragliding ica, adventure sports paracas",
            "subtitle": "Float over the golden cliffs and turquoise sea of the Paracas National Reserve with a certified pilot.",
            "intro": "Tandem <strong>paragliding in Paracas</strong> is one of the most breathtaking adventure experiences on the Peruvian coast. You fly securely attached to an instructor pilot certified by the APVL (Peruvian Free Flight Association).",
            "intro_p2": "We take off from the Reserve's high cliffs, at spots like <strong>Supay Beach or the Mirador hill</strong>, where the steady Paracas sea breeze lifts the glider smoothly over the unique contrast of desert and ocean.",
            "intro_p3": "No training or cliff-jumping involved: the glider inflates gradually and takeoff feels like gently floating off the ground. Within seconds you are soaring with a view over the entire bay.",
            "why_title": "Flight Details",
            "why_items": [
                {"icon": "account_circle", "title": "Certified Pilot", "desc": "Fly safely with an instructor certified by APVL (Peruvian Free Flight Association)."},
                {"icon": "video_camera_back", "title": "HD Video Included", "desc": "We record your flight using a GoPro action camera so you can take this memory home."},
                {"icon": "wind_power", "title": "10-15 Minute Flight", "desc": "Pure flight time suspended in the air, gliding along the coastal wind currents."},
                {"icon": "explore", "title": "Spectacular Views", "desc": "Get a bird's-eye view of the bay, the dunes, the cliffs, and the waves crashing on the shore."}
            ],
            "included": ["Tandem flight with a certified instructor pilot", "Use of helmet and professional safety harness", "GoPro HD action video recording of your flight", "Round-trip transport to the takeoff point in the Reserve"],
            "excluded": ["Paracas National Reserve entrance fee (S/ 11.00)"],
            "schedule_label": "* Paragliding is highly dependent on wind conditions. Flight windows are usually between 1:00 PM and 5:00 PM.",
            "faq_title": "Frequently Asked Questions",
            "faqs": [
                {"q": "How much does paragliding in Paracas cost?", "a": "The tandem flight costs S/ 250 per person and includes a certified pilot, full safety equipment, a GoPro video of your flight, and transport to the takeoff point. Only the Reserve entrance fee (S/ 11) is paid separately."},
                {"q": "How long is the flight?", "a": "The flight lasts 10 to 15 minutes depending on wind conditions, plus gear-up time and the safety briefing. The full experience takes about 1 hour."},
                {"q": "Do I need any previous experience?", "a": "None. The pilot does all the work. You only need to take a few running steps at takeoff and lift your legs when landing."},
                {"q": "Is it scary? Will I feel vertigo?", "a": "Less than you would think. There is no free fall and no sharp turns: the flight is smooth and stable, like sitting in a floating chair. Most passengers relax within seconds, and many ask for acrobatics at the end."},
                {"q": "Are there weight or age limits?", "a": "For safety, passenger weight must be between 40 kg (90 lbs) and 90 kg (200 lbs). Minors can fly with written parental consent."},
                {"q": "What happens if there is no wind?", "a": "Paragliding depends entirely on the wind. If it is too weak or too strong, we wait for it to adjust within the afternoon window or reschedule at no cost to guarantee your safety."},
                {"q": "What should I wear?", "a": "Comfortable long sleeves, long pants, and well-fitted closed shoes. We provide the helmet and harness. Phones must be well secured or left with our ground team."}
            ]
        }
    },
    "buceo": {
        "filename": "buceo.html",
        "image": "img/buceo.jpg",
        "price": "S/ 400",
        "price_val": "400",
        "price_cur": "PEN",
        "category": "mar",
        "es": {
            "title": "Buceo en Paracas 2026: Bautizo de Mar con Instructor | SolyMar Paracas",
            "desc": "Bautizo de buceo y salidas guiadas en Bahía de Paracas ($120 USD / S/ 400) e Islas Blanca ($220 USD / S/ 745). Instructor, equipo completo y fotos bajo el agua. Reserva por WhatsApp.",
            "h1": "Buceo en Paracas",
            "keywords": "buceo paracas, buceo paracas precio, buceo islas blanca, bautizo de buceo peru, donde bucear en peru, discover scuba diving peru, buceo con lobos marinos",
            "subtitle": "Sumérgete en los ecosistemas de la corriente de Humboldt: bosques de algas, estrellas de mar y lobos marinos curiosos.",
            "intro": "El <strong>buceo en Paracas</strong> te abre las puertas a uno de los mares más productivos del planeta: las aguas frías y ricas en nutrientes de la corriente de Humboldt concentran una vida marina que sorprende incluso a buzos experimentados.",
            "intro_p2": "Ofrecemos el <strong>Bautizo de Buceo (Discover Scuba Diving)</strong> para principiantes sin licencia y <strong>salidas guiadas para buzos certificados y aficionados</strong> en dos puntos principales: la <strong>Bahía de Paracas</strong> ($120 USD / S/ 400 soles) e <strong>Islas Blanca</strong> ($220 USD / S/ 745 soles).",
            "intro_p3": "Todas las salidas van acompañadas de instructores certificados que controlan tu flotabilidad y te guían paso a paso, con fotos y videos subacuáticos incluidos para que te lleves el recuerdo.",
            "why_title": "Opciones y puntos de inmersión",
            "why_items": [
                {"icon": "water_drop", "title": "Bahía de Paracas ($120 USD / S/ 400)", "desc": "Inmersión en la Bahía de Paracas. Ideal para principiantes y bautizos de buceo en aguas tranquilas con variada fauna marina."},
                {"icon": "landscape", "title": "Islas Blanca ($220 USD / S/ 745)", "desc": "Navegación a Islas Blanca para sumergirte en aguas cristalinas con paisajes rocosos y abundantes especies marinas."},
                {"icon": "photo_camera", "title": "Fotos Subacuáticas", "desc": "Te tomamos fotos y videos bajo el agua con cámaras especiales para que compartas tu experiencia."},
                {"icon": "shield", "title": "Equipamiento Completo", "desc": "Traje de neopreno de 5mm, tanque, regulador, chaleco compensador (BCD), máscara, aletas y plomos incluidos."}
            ],
            "custom_price_html": """<div class="flex flex-col gap-3 mb-2">
    <div class="flex justify-between items-baseline border-b border-black/10 pb-3">
        <span class="text-base font-bold text-primary">Bahía de Paracas:</span>
        <span class="text-2xl font-extrabold text-on-surface">$120 USD <span class="text-sm font-semibold text-on-surface-variant">(S/ 400)</span></span>
    </div>
    <div class="flex justify-between items-baseline border-b border-black/10 pb-3">
        <span class="text-base font-bold text-primary">Islas Blanca:</span>
        <span class="text-2xl font-extrabold text-on-surface">$220 USD <span class="text-sm font-semibold text-on-surface-variant">(S/ 745)</span></span>
    </div>
</div>""",
            "price_sub_label": "Precio por persona según punto de inmersión",
            "included": ["Clase instructiva teórica y práctica", "Una inmersión guiada por instructor de buceo", "Equipo completo de buceo (traje, tanque, regulador, BCD, plomos)", "Fotos y videos digitales bajo el agua", "Navegación en bote al punto de inmersión"],
            "excluded": ["Entrada a la Reserva Nacional SERNANP (S/ 16.00 soles no incluidos)"],
            "schedule_label": "* Salidas diarias a las 8:30 AM. Duración total de la actividad: 3.5 horas aprox.",
            "faq_title": "Preguntas Frecuentes",
            "faqs": [
                {"q": "¿Cuánto cuesta el buceo en Paracas?", "a": "El precio del buceo en Paracas varía según el punto de inmersión seleccionado:<br>• <strong>Bahía de Paracas:</strong> $120 USD ó S/ 400 soles por persona.<br>• <strong>Islas Blanca:</strong> $220 USD ó S/ 745 soles por persona.<br><br>Ambas opciones incluyen clase teórica y práctica, inmersión guiada con instructor certificado, equipo completo de buceo (traje de neopreno 5mm, tanque, regulador, BCD, plomos), fotos y videos digitales bajo el agua y navegación al punto de buceo. Solo se paga aparte la entrada a la Reserva Nacional SERNANP (S/ 16.00 soles por persona)."},
                {"q": "¿Necesito saber nadar para el Bautizo?", "a": "Es recomendable sentirse cómodo en el agua, pero no necesitas ser un nadador experto. El instructor te sostiene y controla tu flotabilidad durante toda la inmersión."},
                {"q": "¿A qué profundidad descendemos?", "a": "Para el bautizo de buceo descendemos a una profundidad máxima de entre 5 y 10 metros, ideal para observar la fauna marina con luz natural y total seguridad."},
                {"q": "¿Qué fauna se puede ver bajo el agua?", "a": "El fondo marino de Paracas alberga erizos, estrellas de mar rojas, pulpos, cangrejos, lenguados, caballitos de mar en temporada, bosques de algas y, con frecuencia, lobos marinos juveniles curiosos que se acercan a los buzos."},
                {"q": "¿El agua no es muy fría?", "a": "El mar de Paracas está entre 14°C y 17°C, por eso todos los buzos usan traje de neopreno de 5mm de cuerpo completo que mantiene el calor corporal. La sensación es fresca al inicio y cómoda durante toda la inmersión."},
                {"q": "¿Desde qué edad se puede bucear?", "a": "El bautizo de buceo se puede realizar desde los 10 años acompañado de un padre o tutor. No hay edad máxima: solo se requiere salud general estable y no tener afecciones cardíacas o respiratorias graves."},
                {"q": "¿Ya soy buzo certificado, tienen salidas para mí?", "a": "Sí, organizamos inmersiones guiadas para buzos con credencial PADI/SSI (Open Water en adelante) en puntos como Islas Blanca o Bahía de Paracas, con profundidades y perfiles adaptados a tu nivel."}
            ]
        },
        "en": {
            "title": "Scuba Diving in Paracas 2026: Discover Dive & Fun Dives | SolyMar",
            "desc": "Discover Scuba dives and guided trips in Paracas Bay ($120 USD / S/ 400) and Islas Blanca ($220 USD / S/ 745). Instructor, full gear, and underwater photos included. Book via WhatsApp.",
            "h1": "Scuba Diving in Paracas",
            "keywords": "scuba diving paracas, scuba diving paracas price, diving islas blanca, discovery dive peru, where to dive in peru, diving with sea lions peru",
            "subtitle": "Dive into the Humboldt Current ecosystems: kelp forests, red starfish, and curious sea lions.",
            "intro": "<strong>Scuba diving in Paracas</strong> opens the door to one of the most productive seas on Earth: the cold, nutrient-rich waters of the Humboldt Current concentrate marine life that surprises even experienced divers.",
            "intro_p2": "We offer the <strong>Discover Scuba Diving</strong> experience for beginners without certification, as well as <strong>guided dives for certified divers</strong> in two main locations: <strong>Paracas Bay</strong> ($120 USD / S/ 400 soles) and <strong>Islas Blanca</strong> ($220 USD / S/ 745 soles).",
            "intro_p3": "Every trip is led by certified instructors who manage your buoyancy and guide you step by step, with underwater photos and videos included so you take the memory home.",
            "why_title": "Diving Options & Dive Spots",
            "why_items": [
                {"icon": "water_drop", "title": "Paracas Bay ($120 USD / S/ 400)", "desc": "Diving experience in Paracas Bay. Perfect for beginners and discovery dives in calm, protected waters rich in marine life."},
                {"icon": "landscape", "title": "Islas Blanca ($220 USD / S/ 745)", "desc": "Boat trip to Islas Blanca to dive in clear island waters with underwater rock structures and diverse wildlife."},
                {"icon": "photo_camera", "title": "GoPro Photos & Videos", "desc": "We capture underwater HD photos and videos of your dive so you can remember and share your adventure."},
                {"icon": "shield", "title": "Complete Equipment", "desc": "5mm wetsuit, tanks, regulator, BCD jacket, mask, fins, and weights are fully provided."}
            ],
            "custom_price_html": """<div class="flex flex-col gap-3 mb-2">
    <div class="flex justify-between items-baseline border-b border-black/10 pb-3">
        <span class="text-base font-bold text-primary">Paracas Bay:</span>
        <span class="text-2xl font-extrabold text-on-surface">$120 USD <span class="text-sm font-semibold text-on-surface-variant">(S/ 400)</span></span>
    </div>
    <div class="flex justify-between items-baseline border-b border-black/10 pb-3">
        <span class="text-base font-bold text-primary">Islas Blanca:</span>
        <span class="text-2xl font-extrabold text-on-surface">$220 USD <span class="text-sm font-semibold text-on-surface-variant">(S/ 745)</span></span>
    </div>
</div>""",
            "price_sub_label": "Price per person based on selected dive spot",
            "included": ["Theoretical briefing and shallow water practice", "One guided dive with a certified instructor", "Full set of scuba gear rental (wetsuit, tank, regulator, BCD, weights)", "Digital underwater photos and videos", "Boat transport to the dive site"],
            "excluded": ["SERNANP Paracas Reserve entrance fee (S/ 16.00 soles not included)"],
            "schedule_label": "* Daily departures at 8:30 AM. Total activity duration: approx. 3.5 hours.",
            "faq_title": "Frequently Asked Questions",
            "faqs": [
                {"q": "How much does scuba diving in Paracas cost?", "a": "The price for scuba diving in Paracas depends on the selected dive spot:<br>• <strong>Paracas Bay:</strong> $120 USD or S/ 400 soles per person.<br>• <strong>Islas Blanca:</strong> $220 USD or S/ 745 soles per person.<br><br>Both options include theoretical and practical instruction, a guided dive with a certified instructor, full dive gear (5mm wetsuit, tank, regulator, BCD, weights), digital underwater photos/videos, and boat transport. The SERNANP Paracas Reserve entrance fee (S/ 16.00 soles per person) is paid separately."},
                {"q": "Do I need to know how to swim for the Discovery Dive?", "a": "Basic water comfort is recommended, but you don't need to be an expert swimmer. Your instructor holds you and manages your buoyancy throughout the dive."},
                {"q": "How deep do we go?", "a": "For first-time divers, the maximum depth is restricted to 5-10 meters (15-30 feet), which is optimal for natural light, wildlife viewing, and safety."},
                {"q": "What marine life will we see?", "a": "The cold waters host red starfish, sea urchins, octopuses, crabs, flounders, seasonal seahorses, kelp forests, and frequently curious juvenile sea lions that approach divers."},
                {"q": "Isn't the water too cold?", "a": "The Paracas sea runs between 14°C and 17°C (57-62°F), which is why all divers wear a full-length 5mm wetsuit that retains body heat. It feels brisk at first and comfortable for the whole dive."},
                {"q": "What is the minimum age to dive?", "a": "The Discover Scuba Dive is available from age 10 accompanied by a parent or guardian. There is no maximum age: only stable general health and no serious heart or respiratory conditions are required."},
                {"q": "I am a certified diver. Do you run trips for me?", "a": "Yes, we organize guided dives for credentialed divers (PADI/SSI Open Water and above) at sites like Islas Blanca or Paracas Bay, with depth profiles adapted to your level."}
            ]
        }
    },
    "kayak-paddle-paracas": {
        "filename": "kayak-paddle-paracas.html",
        "image": "img/kayak-paddle.jpg",
        "price": "S/ 60",
        "price_val": "60",
        "price_cur": "PEN",
        "category": "mar",
        "es": {
            "title": "Kayak y Paddle en Paracas 2026: Tours y Alquiler en la Bahía | SolyMar",
            "desc": "Alquiler y tours guiados de kayak y stand up paddle en la bahía de Paracas. Aguas como espejo por la mañana, ideales para principiantes y familias. Reserva por WhatsApp.",
            "h1": "Kayak y stand up paddle en Paracas",
            "keywords": "kayak paracas, paddle paracas, alquiler kayak paracas, sup paracas, deportes acuaticos paracas, kayak bahia paracas, que hacer en paracas",
            "subtitle": "Deslízate sobre las aguas mansas de la bahía al amanecer en kayak o tabla de stand up paddle.",
            "intro": "La bahía de Paracas destaca por sus aguas extremadamente mansas por las mañanas, convirtiéndola en un espejo de agua perfecto para el <strong>kayak y stand up paddle (SUP)</strong>.",
            "intro_p2": "Ofrecemos alquiler por horas para que explores a tu propio ritmo, así como tours guiados al amanecer para avistar aves y flamencos cerca de la orilla.",
            "intro_p3": "Una actividad ecológica, deportiva y sumamente relajante para iniciar el día sintiendo la brisa marina.",
            "why_title": "Modalidades y Equipamiento",
            "why_items": [
                {"icon": "rowing", "title": "Kayaks Simples y Dobles", "desc": "Kayaks de travesía estables y fáciles de maniobrar, ideales para remar solo o en pareja."},
                {"icon": "surfing", "title": "Tablas de Stand Up Paddle", "desc": "Tablas inflables y rígidas de gran estabilidad, perfectas para practicar equilibrio de pie o de rodillas."},
                {"icon": "wb_sunny", "title": "Turno del Amanecer", "desc": "Remar entre las 6:30 AM y 9:00 AM te garantiza un mar sin viento, calmado como una piscina."},
                {"icon": "flutter_dash", "title": "Avistamiento Ecológico", "desc": "Remando en silencio es posible acercarse a flamencos, pelícanos y otras aves costeras sin ahuyentarlas."}
            ],
            "included": ["Alquiler de kayak o tabla de stand up paddle", "Remos de carbono y chaleco salvavidas de uso obligatorio", "Bolsa seca para proteger tu celular u objetos de valor", "Charla técnica de remado y seguridad antes de ingresar al mar"],
            "excluded": ["Guía en el agua (opcional en modalidad tour, consultar tarifa)"],
            "schedule_label": "* Disponible todos los días desde las 6:30 AM hasta las 12:00 PM. Se recomienda la mañana para evitar vientos fuertes (Paracas).",
            "faq_title": "Preguntas Frecuentes",
            "faqs": [
                {"q": "¿Cuánto cuesta el kayak o paddle en Paracas?", "a": "El alquiler cuesta S/ 60 e incluye kayak o tabla SUP, remo, chaleco salvavidas, bolsa seca para tus cosas y la charla técnica de seguridad. El guía acompañante en el agua es opcional con tarifa adicional."},
                {"q": "¿Cuál es el mejor horario para remar?", "a": "Entre las 6:30 AM y las 9:00 AM la bahía está completamente calmada, como una piscina. Después del mediodía se levanta el viento Paracas y la remada se vuelve exigente, por eso solo operamos por la mañana."},
                {"q": "¿Es difícil mantener el equilibrio en Paddle?", "a": "Nuestras tablas son de iniciación (anchas y estables), por lo que casi todo el mundo logra ponerse de pie en los primeros 10 minutos. Si te cuesta, puedes remar de rodillas de forma muy cómoda."},
                {"q": "¿Se requiere experiencia previa?", "a": "Ninguna. Antes de ingresar al agua, nuestro personal te enseña a remar, girar y subir de nuevo a la tabla o kayak en caso de caída."},
                {"q": "¿Se mojará mi ropa?", "a": "En kayak es común mojarse ligeramente por el salpicado del remo. En paddle existe la posibilidad de caer al agua. Recomendamos ropa de baño o deportiva de secado rápido y una muda seca para el final."},
                {"q": "¿Qué fauna se puede ver desde el kayak?", "a": "Remando en silencio por la orilla es común acercarse a pelícanos, zarcillos, gaviotas y, en temporada, flamencos que se alimentan en la bahía. Lleva tu celular en la bolsa seca para las fotos."}
            ]
        },
        "en": {
            "title": "Kayak & SUP in Paracas 2026: Bay Tours & Rentals | SolyMar Paracas",
            "desc": "Rentals and guided tours of sea kayak and stand-up paddleboarding in Paracas Bay. Mirror-flat morning waters, perfect for beginners and families. Book on WhatsApp.",
            "h1": "Kayak & Stand Up Paddle in Paracas",
            "keywords": "kayak paracas, paddle paracas, rent kayak paracas, sup paracas, water sports paracas, paracas bay kayaking, things to do in paracas",
            "subtitle": "Glide over the mirror-like waters of Paracas Bay at sunrise in a kayak or stand-up paddleboard.",
            "intro": "Paracas Bay is protected from open ocean swell, offering extremely flat and calm waters in the mornings, an absolute paradise for <strong>kayaking and stand-up paddleboarding (SUP)</strong>.",
            "intro_p2": "We offer hourly rentals for independent explorers, as well as early morning guided tours to view nesting birds and pink flamingos along the coastline.",
            "intro_p3": "A peaceful, ecological, and active way to start your day in touch with the local marine breeze.",
            "why_title": "Options and Gear",
            "why_items": [
                {"icon": "rowing", "title": "Single & Double Kayaks", "desc": "Stable and easy-to-steer sit-on-top kayaks, ideal for solo paddlers or couples."},
                {"icon": "surfing", "title": "Stand-Up Paddleboards", "desc": "Wide, high-buoyancy boards designed for beginners to stand up and paddle with ease."},
                {"icon": "wb_sunny", "title": "The Golden Morning Window", "desc": "Paddling between 6:30 AM and 9:00 AM guarantees water flat as a pool before the winds pick up."},
                {"icon": "flutter_dash", "title": "Eco-friendly Wildlife Spotting", "desc": "Approach local shorebirds, pelicans, and pink flamingos quietly without disturbing their feeding."}
            ],
            "included": ["Kayak or stand-up paddleboard rental", "Paddles and mandatory high-visibility life jackets", "Dry bag for protecting your phone and camera", "Briefing on paddling techniques and safety before entering"],
            "excluded": ["In-water guide (optional for tours, please enquire)"],
            "schedule_label": "* Available daily from 6:30 AM to 12:00 PM. Morning hours are highly recommended to avoid the daily wind gusts.",
            "faq_title": "Frequently Asked Questions",
            "faqs": [
                {"q": "How much does kayaking or SUP in Paracas cost?", "a": "The rental costs S/ 60 and includes the kayak or SUP board, paddle, life jacket, a dry bag for your belongings, and the safety briefing. An accompanying in-water guide is optional at an additional rate."},
                {"q": "What is the best time to paddle?", "a": "Between 6:30 AM and 9:00 AM the bay is completely flat, like a pool. After midday the famous Paracas wind picks up and paddling gets demanding. That is why we only operate in the morning."},
                {"q": "Is it hard to balance on a Paddleboard?", "a": "We use beginner-friendly boards (wide and thick). Most people stand up within their first 10 minutes. If balancing is hard, you can comfortably paddle on your knees."},
                {"q": "Is any experience needed?", "a": "None. Our beach staff will show you how to hold the paddle, steer, and climb back aboard if you slip into the water."},
                {"q": "Will I get wet?", "a": "In a kayak, expect some paddle splashes. On a paddleboard, you might fall in. We recommend swimwear or quick-dry sportswear and a dry change of clothes for afterwards."},
                {"q": "What wildlife can I see from the kayak?", "a": "Paddling quietly along the shore, you can get close to pelicans, Inca terns, gulls and, in season, flamingos feeding in the bay. Keep your phone in the dry bag for photos."}
            ]
        }
    },
    "mini-buggies-paracas": {
        "filename": "mini-buggies-paracas.html",
        "image": "img/atv-gokart.jpg",
        "price": "S/ 120",
        "price_val": "120",
        "price_cur": "PEN",
        "category": "desierto",
        "es": {
            "title": "Cuatrimotos y Mini Buggies en Paracas 2026: Maneja tu Aventura | SolyMar",
            "desc": "Maneja tu propia cuatrimoto (ATV) o mini buggy biplaza por rutas autorizadas de la Reserva de Paracas, con guía en caravana y vistas al mar. Turnos todo el día.",
            "h1": "Tour en Cuatrimotos y Mini Buggies en Paracas",
            "keywords": "cuatrimotos paracas, cuatrimotos paracas precio, buggies paracas, atv paracas, tours paracas desierto, mini buggy paracas, que hacer en paracas aventura",
            "subtitle": "Maneja tu propia cuatrimoto individual o un mini buggy biplaza por los senderos de arena de la Reserva Nacional de Paracas.",
            "intro": "El tour de <strong>Cuatrimotos y Mini Buggies en Paracas</strong> es la aventura todoterreno más emocionante para explorar la Reserva Nacional a tu propio ritmo.",
            "intro_p2": "Conducirás vehículos automáticos de fácil manejo (cuatrimotos individuales o karts/buggies de dos asientos) siguiendo a nuestro guía instructor por rutas desérticas autorizadas hasta miradores con vistas impactantes del Océano Pacífico.",
            "intro_p3": "Siente la brisa marina y la adrenalina de transitar por planos de sal, acantilados costeros y formaciones rocosas únicas en una ruta de 2 horas.",
            "why_title": "Detalles de la aventura todoterreno",
            "why_items": [
                {"icon": "sports_motorsports", "title": "Cuatrimotos o Buggies", "desc": "Elige entre cuatrimoto individual (ATV) para máximo dinamismo o mini buggy de 2 plazas para compartir con un copiloto."},
                {"icon": "terrain", "title": "Rutas Autorizadas", "desc": "Recorre caminos establecidos de la Reserva Nacional de Paracas, visitando miradores naturales y playas del desierto."},
                {"icon": "explore", "title": "Caravana Segura", "desc": "Un guía líder encabeza la caravana regulando la velocidad y asegurando que disfrutes del recorrido con total tranquilidad."},
                {"icon": "wb_sunny", "title": "Múltiples Turnos", "desc": "Salidas programadas durante todo el día (mañana y tarde) para que lo combines con tus otras actividades."}
            ],
            "included": ["Alquiler de Cuatrimoto (ATV) o Mini Buggy de 2 plazas", "Guía instructor en ruta liderando el grupo", "Casco de seguridad y lentes de protección antipolvo", "Charla técnica previa de inducción y prueba de manejo"],
            "excluded": ["Boleto de ingreso a la Reserva Nacional de Paracas (S/ 11.00)"],
            "schedule_label": "* Salidas diarias programadas a las 9:00 AM, 11:30 AM, 2:00 PM y 4:00 PM. Duración: 2 horas aprox.",
            "faq_title": "Preguntas Frecuentes",
            "faqs": [
                {"q": "¿Cuánto cuesta el tour en cuatrimoto o mini buggy?", "a": "El tour cuesta S/ 120 e incluye el vehículo (cuatrimoto individual o mini buggy de 2 plazas), guía instructor en ruta, casco, lentes antipolvo y la práctica de manejo previa. Solo se paga aparte la entrada a la Reserva (S/ 11)."},
                {"q": "¿Se necesita experiencia para conducir?", "a": "No, todos nuestros vehículos son completamente automáticos y muy fáciles de operar. Realizamos una práctica previa antes de salir al desierto para tu seguridad."},
                {"q": "¿Es obligatorio tener licencia de conducir?", "a": "Sí, para quien vaya a conducir es obligatorio ser mayor de edad y presentar una licencia de conducir física vigente (peruana o internacional). Los menores de edad pueden viajar como acompañantes en los buggies."},
                {"q": "¿Cuál es la diferencia entre Cuatrimoto y Buggy?", "a": "La cuatrimoto (ATV) se conduce de manera individual y con manubrio (estilo motocicleta). El mini buggy es biplaza, con volante y pedales tradicionales (estilo kart), ideal para ir con copiloto."},
                {"q": "¿Qué debo llevar?", "a": "Zapatillas cerradas, bloqueador solar y un pañuelo o buff para el polvo. El casco y los lentes de protección los ponemos nosotros. Evita ropa suelta y lleva tu cámara bien asegurada."}
            ]
        },
        "en": {
            "title": "Paracas ATV & Mini Buggy Tour 2026: Drive the Desert | SolyMar",
            "desc": "Drive your own quad bike (ATV) or two-seater mini buggy along authorized trails of the Paracas Reserve, with a convoy guide and ocean views. Departures all day.",
            "h1": "ATV and Mini Buggies Desert Tour",
            "keywords": "quad bike paracas, atv paracas price, atv paracas, buggies paracas, desert tour paracas, mini buggy, paracas adventure activities",
            "subtitle": "Drive your own single quad bike or share a two-seater mini buggy across the stunning trails of the Paracas Reserve.",
            "intro": "The <strong>ATV & Mini Buggy tour in Paracas</strong> is the ultimate off-road adventure to explore the scenic coastal desert of the National Reserve at your own pace.",
            "intro_p2": "You will take the controls of easy-to-drive automatic machines (individual quad bikes or double dune karts) following an expert guide through approved tracks, stopping at high-altitude cliffs with views of the blue Pacific.",
            "intro_p3": "Feel the sea breeze and the thrill of riding across salt flats, desert dunes, and yellow cliffs in a dynamic 2-hour experience.",
            "why_title": "Tour Highlights",
            "why_items": [
                {"icon": "sports_motorsports", "title": "ATVs or Dune Buggies", "desc": "Choose a single-rider quad bike for a sporty feel, or a double-seater mini buggy to share the driving experience."},
                {"icon": "terrain", "title": "Reserve Trails", "desc": "Ride through designated pathways inside the Paracas Reserve, stopping at viewpoints and dry clay plains."},
                {"icon": "explore", "title": "Guided Convoy", "desc": "A lead instructor sets a safe pace, guiding you through the best desert trails and helping you handle the machines."},
                {"icon": "wb_sunny", "title": "Flexible Schedules", "desc": "Multiple departure times throughout the day, making it easy to fit into your travel itinerary."}
            ],
            "included": ["Rental of automatic Quad Bike (ATV) or 2-seater Mini Buggy", "Professional route instructor leading the convoy", "Safety helmet and dust protection goggles", "Pre-tour safety briefing and driving practice"],
            "excluded": ["Paracas National Reserve entrance tax (S/ 11.00)"],
            "schedule_label": "* Daily departures at 9:00 AM, 11:30 AM, 2:00 PM, and 4:00 PM. Duration: approx. 2 hours.",
            "faq_title": "Frequently Asked Questions",
            "faqs": [
                {"q": "How much does the ATV or mini buggy tour cost?", "a": "The tour costs S/ 120 and includes the vehicle (single ATV or 2-seater mini buggy), a route instructor, helmet, dust goggles, and a pre-tour driving practice. Only the Reserve entrance fee (S/ 11) is paid separately."},
                {"q": "Do I need experience to drive?", "a": "Not at all. All our ATVs and buggies are fully automatic and user-friendly. We run a brief practice test before departure to make sure you are comfortable."},
                {"q": "Is a driver's license required?", "a": "Yes, drivers must be of legal age and show a valid physical driver's license (local or international). Minors are welcome to ride as passengers in the two-seater buggies."},
                {"q": "What is the difference between an ATV and a Buggy?", "a": "The ATV (quad bike) is a single-rider vehicle with handlebars (motorcycle style). The mini buggy is a two-seater with a steering wheel and pedals (kart style), perfect for riding with a co-pilot."},
                {"q": "What should I bring?", "a": "Closed shoes, sunscreen, and a bandana or buff for the dust. We provide the helmet and protective goggles. Avoid loose clothing and keep your camera well secured."}
            ]
        }
    },
    "tambo-colorado": {
        "filename": "tambo-colorado.html",
        "image": "img/tambo-colorado.jpg",
        "price": "S/ 80",
        "price_val": "80",
        "price_cur": "PEN",
        "category": "cultura",
        "es": {
            "title": "Tour a Tambo Colorado 2026: el Palacio Inca de la Costa | SolyMar",
            "desc": "Visita Tambo Colorado, el complejo inca de adobe mejor conservado de la costa peruana, a 45 minutos de Pisco. Tour con guía, transporte y entrada incluidos.",
            "h1": "Tour a Tambo Colorado desde Paracas y Pisco",
            "keywords": "tambo colorado, tambo colorado tour, tambo colorado como llegar, sitio arqueologico pisco, ruinas incas cerca de lima, que hacer en pisco",
            "subtitle": "Visita el palacio administrativo inca de adobe mejor conservado de la costa peruana y admira sus colores originales.",
            "intro": "<strong>Tambo Colorado</strong> (también conocido como Pucallacta o Pucahuasi) fue un asentamiento inca construido durante el gobierno de Pachacútec, en el siglo XV.",
            "intro_p2": "Ubicado a unos 45 minutos de Pisco camino a Ayacucho, este sitio destaca por ser una estructura de adobes que aún conserva restos de su pintura mural original roja, amarilla y blanca.",
            "intro_p3": "Un tour cultural ideal para los amantes de la historia andina y la arqueología, alejado de las aglomeraciones de turistas.",
            "why_title": "¿Qué verás en Tambo Colorado?",
            "why_items": [
                {"icon": "architecture", "title": "Pinturas Murales Incas", "desc": "Observa los restos de pintura roja, blanca y amarilla que decoraban las hornacinas y paredes incas."},
                {"icon": "history_edu", "title": "Palacio Principal", "desc": "Recorre el Palacio Norte, los baños ceremoniales, las plazas de armas y la hornacina del trono inca."},
                {"icon": "museum", "title": "Museo de Sitio", "desc": "Pequeño museo donde se exponen cerámicas, restos textiles y herramientas encontradas durante las excavaciones."},
                {"icon": "group", "title": "Poca Concurrencia", "desc": "Disfruta de una caminata guiada tranquila, sintiendo la mística del lugar sin las multitudes de otros sitios arqueológicos."}
            ],
            "included": ["Transporte turístico climatizado ida y vuelta", "Guía local bilingüe especializado en arqueología", "Boleto de entrada al complejo arqueológico y museo de sitio", "Asistencia durante el recorrido"],
            "excluded": ["Almuerzo y bebidas"],
            "schedule_label": "* Salida diaria a las 9:00 AM desde tu hotel en Paracas o Pisco. Duración: 3.5 horas aprox.",
            "faq_title": "Preguntas Frecuentes",
            "faqs": [
                {"q": "¿Cuánto cuesta el tour a Tambo Colorado?", "a": "El tour cuesta S/ 80 por persona y es de los pocos que incluye todo: transporte climatizado ida y vuelta, guía especializado en arqueología y el boleto de entrada al complejo y su museo de sitio. Solo el almuerzo va por tu cuenta."},
                {"q": "¿Por qué se llama Tambo Colorado?", "a": "Debe su nombre al color rojo arcilla predominante en la pintura de sus adobes. Los tambos eran centros de descanso y almacenamiento situados en la red del camino inca (Qhapaq Ñan)."},
                {"q": "¿Es un tour apto para niños?", "a": "Sí, el circuito peatonal es plano y muy fácil de caminar, por lo que es una visita educativa apta y recomendada para todas las edades."},
                {"q": "¿Qué se recomienda llevar?", "a": "El complejo está en una zona de sol constante y clima seco. Lleva protector solar, sombrero, lentes de sol, agua mineral y zapatillas cómodas para caminar sobre tierra."},
                {"q": "¿Vale la pena si ya conoceré Cusco?", "a": "Sí: Tambo Colorado es único porque conserva la pintura mural original de sus muros, algo que casi no se ve en los sitios de piedra de Cusco. Además, se visita sin multitudes y se combina muy bien con los tours de Paracas."}
            ]
        },
        "en": {
            "title": "Tambo Colorado Tour 2026: Painted Inca Palace near Pisco | SolyMar",
            "desc": "Visit Tambo Colorado, the best-preserved adobe Inca complex on the Peruvian coast, 45 minutes from Pisco. Tour with guide, transport and entrance included.",
            "h1": "Tambo Colorado Inca Ruins Tour",
            "keywords": "tambo colorado, tambo colorado tour, how to get to tambo colorado, archaeological site pisco, inca ruins near lima, things to do in pisco",
            "subtitle": "Visit the best-preserved administrative Inca adobe complex on the Peruvian coast, complete with its original colors.",
            "intro": "<strong>Tambo Colorado</strong> (also known as Pucallacta) was a military and administrative outpost built under the reign of Inca Emperor Pachacutec in the 15th century.",
            "intro_p2": "Located 45 minutes up the valley from Pisco, this archaeological site is unique because its dry climate preserved the red, yellow, and white paintings on the adobe walls.",
            "intro_p3": "An exceptional cultural tour for history enthusiasts, providing a peaceful walk far away from overcrowded tourist hotspots.",
            "why_title": "Tour Highlights",
            "why_items": [
                {"icon": "architecture", "title": "Original Wall Paint", "desc": "Spot the remaining layers of red and yellow clay pigments that coated the trapezoidal niches and rooms."},
                {"icon": "history_edu", "title": "The Northern Palace", "desc": "Walk through ceremonial courtyards, Inca baths (baño del inca), barracks, and the main throne room."},
                {"icon": "museum", "title": "On-site Museum", "desc": "A small visitor center showcasing pottery, textiles, and artifacts excavated at the site."},
                {"icon": "group", "title": "Crowd-free Exploration", "desc": "Enjoy a quiet, informative tour, feeling the magic of the location at your own relaxed pace."}
            ],
            "included": ["Round-trip air-conditioned tourist transport", "Bilingual local guide specialized in history", "Entrance tickets to the ruins and museum", "On-site assistance"],
            "excluded": ["Lunch and drinks"],
            "schedule_label": "* Daily departures at 9:00 AM from Paracas or Pisco hotels. Duration: approx. 3.5 hours.",
            "faq_title": "Frequently Asked Questions",
            "faqs": [
                {"q": "How much does the Tambo Colorado tour cost?", "a": "The tour costs S/ 80 per person and is one of the few that includes everything: round-trip air-conditioned transport, an archaeology-specialized guide, and the entrance ticket to the complex and its site museum. Only lunch is on you."},
                {"q": "Why is it called Tambo Colorado?", "a": "The name means 'Red Outpost', referring to the deep red mud paint coating the structures. Tambos were roadside rest and supply hubs along the Inca road network (Qhapaq Ñan)."},
                {"q": "Is it a difficult walk?", "a": "Not at all. The tour takes place on flat dirt paths inside the ruins, making it a very easy and educational walking tour for families."},
                {"q": "What should I bring?", "a": "The site is located in a warm, dry valley. Bring sun protection, a hat, sunglasses, bottled water, and comfortable walking shoes."},
                {"q": "Is it worth it if I am already visiting Cusco?", "a": "Yes: Tambo Colorado is unique because it preserves the original wall paint of its structures, something you will hardly see at the stone sites of Cusco. It is also crowd-free and combines perfectly with the Paracas tours."}
            ]
        }
    },
    "yakupark-paracas": {
        "filename": "yakupark-paracas.html",
        "image": "img/yakupark.jpg",
        "price": "S/ 50",
        "price_val": "50",
        "price_cur": "PEN",
        "category": "mar",
        "es": {
            "title": "Yakupark Paracas 2026: Precio y Entradas al Parque Acuático | SolyMar",
            "desc": "Entradas al Yakupark de Paracas: circuito inflable con toboganes, obstáculos y trampolines sobre el mar, con salvavidas certificados. El plan favorito de las familias.",
            "h1": "Yakupark: el parque acuático inflable de Paracas",
            "keywords": "yakupark paracas, yakupark precio, yakupark entradas, parque acuatico paracas, que hacer con niños en paracas, planes familiares paracas",
            "subtitle": "Diviértete en el parque acuático inflable más grande de Sudamérica, flotando sobre las aguas tranquilas del muelle El Chaco.",
            "intro": "<strong>Yakupark Paracas</strong> es un circuito de diversión inflable gigante ubicado en la bahía de Paracas. Es una atracción familiar que promete diversión a lo grande.",
            "intro_p2": "Desafía tu agilidad cruzando pistas de obstáculos, resbalando por toboganes directo al mar, y saltando en trampolines elásticos flotantes.",
            "intro_p3": "La actividad cuenta con salvavidas profesionales y chalecos obligatorios, garantizando una tarde refrescante y divertida con total seguridad.",
            "why_title": "¿Qué incluye la diversión?",
            "why_items": [
                {"icon": "pool", "title": "Circuito de Obstáculos", "desc": "Puentes inflables, rampas resbalosas y escaladoras para competir y reír con amigos y familia."},
                {"icon": "water_slide", "title": "Toboganes al Mar", "desc": "Deslízate desde plataformas flotantes para darte un chapuzón en el océano pacífico."},
                {"icon": "health_and_safety", "title": "Seguridad Total", "desc": "Todos los usuarios ingresan equipados con chalecos salvavidas profesionales y bajo la supervisión de salvavidas."},
                {"icon": "access_time", "title": "Turnos de 45 Minutos", "desc": "Tiempo de juego continuo en las instalaciones inflables flotantes por boleto adquirido."}
            ],
            "included": ["Entrada al circuito inflable flotante Yakupark", "Chaleco salvavidas de flotación obligatoria durante el juego", "Supervisión de salvavidas certificados en el agua"],
            "excluded": ["Traslados a la playa (el parque está ubicado frente al muelle de Paracas, de fácil acceso peatonal)"],
            "schedule_label": "* Abierto todos los días de 10:00 AM a 5:30 PM. Compra tus tickets por turnos vía WhatsApp.",
            "faq_title": "Preguntas Frecuentes",
            "faqs": [
                {"q": "¿Cuánto cuesta la entrada al Yakupark?", "a": "La entrada cuesta S/ 50 por turno de 45 minutos de juego continuo e incluye el chaleco salvavidas y la supervisión de salvavidas certificados. Reserva tu turno por WhatsApp para asegurar tu cupo, especialmente en feriados y verano."},
                {"q": "¿Cuál es la edad mínima para ingresar?", "a": "La edad mínima permitida es de 5 años. Los niños menores de 10 años deben ingresar obligatoriamente acompañados de un adulto responsable en el agua."},
                {"q": "¿Es obligatorio saber nadar?", "a": "No es indispensable saber nadar perfectamente porque el uso de chaleco salvavidas de alta flotabilidad es obligatorio para todos. Además, hay salvavidas vigilando el circuito permanentemente."},
                {"q": "¿Se puede ingresar con cámaras o celulares?", "a": "No se recomienda ingresar con celulares u objetos de valor sueltos debido al riesgo de pérdida. Si usas cámaras deportivas (GoPro), deben ir sujetas con arnés de pecho o cabeza."},
                {"q": "¿Dónde queda y cómo llego?", "a": "El parque flota frente a la playa El Chaco, en plena bahía de Paracas, a pocos minutos a pie de cualquier hotel del pueblo. No necesitas traslado: llegas caminando por el malecón."}
            ]
        },
        "en": {
            "title": "Yakupark Paracas 2026: Water Park Tickets & Prices | SolyMar",
            "desc": "Tickets for Yakupark Paracas: inflatable circuit with slides, obstacles and trampolines over the sea, watched by certified lifeguards. The family favorite.",
            "h1": "Yakupark Inflatable Water Park in Paracas",
            "keywords": "yakupark paracas, yakupark price, yakupark tickets, water park paracas, what to do with kids in paracas, family activities paracas",
            "subtitle": "Have fun at South America's largest inflatable water park floating on the calm waters of Paracas bay.",
            "intro": "<strong>Yakupark Paracas</strong> is a giant floating playground set in Paracas Bay, offering a fun and refreshing challenge for kids and adults alike.",
            "intro_p2": "Test your balance crossing inflatable bridges, slip down slides directly into the sea, and bounce on floating trampolines.",
            "intro_p3": "With certified lifeguards on duty and mandatory life jackets, safety is always our priority while you splash and play.",
            "why_title": "Park Features",
            "why_items": [
                {"icon": "pool", "title": "Obstacle Courses", "desc": "Climb walls, balance beams, and slippery platforms to challenge your friends and family."},
                {"icon": "water_slide", "title": "Ocean Slides", "desc": "Slide down floating towers straight into the ocean waters of the bay."},
                {"icon": "health_and_safety", "title": "Certified Lifeguards", "desc": "A dedicated safety team monitors the area at all times. High-quality life vests are provided and mandatory."},
                {"icon": "access_time", "title": "45-Minute Passes", "desc": "Continuous play time on the floating structures per ticket purchased."}
            ],
            "included": ["General entry pass to Yakupark inflatable circuit", "Mandatory life jacket for the duration of the activity", "Continuous supervision by certified ocean lifeguards"],
            "excluded": ["Transfers (the park is located on El Chaco beach, easily accessible on foot from any hotel in Paracas)"],
            "schedule_label": "* Open daily from 10:00 AM to 5:30 PM. Pre-book your time slot easily via WhatsApp.",
            "faq_title": "Frequently Asked Questions",
            "faqs": [
                {"q": "How much is the Yakupark entrance?", "a": "The ticket costs S/ 50 per 45-minute slot of continuous play and includes the life jacket and supervision by certified lifeguards. Book your slot via WhatsApp to secure your spot, especially on holidays and in summer."},
                {"q": "What is the minimum age to participate?", "a": "The minimum age is 5 years old. Children under 10 must be accompanied by a responsible adult on the circuit at all times."},
                {"q": "Do I need to know how to swim?", "a": "Not necessarily. All participants must wear high-buoyancy life vests, and lifeguards are stationed around the structures to assist anyone in the water."},
                {"q": "Can I bring my phone or GoPro?", "a": "We advise against carrying phones or loose valuables as they sink easily. Action cameras (like GoPros) are allowed only if securely mounted on a chest or head harness."},
                {"q": "Where is it and how do I get there?", "a": "The park floats right off El Chaco beach, in the middle of Paracas Bay, a few minutes' walk from any hotel in town. No transport needed: you arrive on foot along the boardwalk."}
            ]
        }
    },
    "trekking": {
        "filename": "trekking.html",
        "image": "img/trekking.jpg",
        "price": "S/ 120",
        "price_val": "120",
        "price_cur": "PEN",
        "category": "desierto",
        "es": {
            "title": "Trekking en Paracas 2026: Golden Shadows Trek al Atardecer | SolyMar",
            "desc": "Caminata guiada por los acantilados de la Reserva Nacional de Paracas hasta la puesta de sol: el Golden Shadows Trek. 5 km con vehículo de apoyo y fotos incluidas.",
            "h1": "Trekking Sombras Doradas en Paracas",
            "keywords": "trekking paracas, golden shadows trek, senderismo reserva nacional paracas, caminata atardecer paracas, trekking sombras doradas, rutas de trekking ica, aventura paracas, hiking paracas",
            "subtitle": "Camina entre acantilados gigantescos y dunas doradas, presenciando una de las puestas de sol más mágicas del planeta.",
            "intro": "El <strong>Golden Shadows Trek</strong> (Caminata de las Sombras Doradas) es un tour de trekking exclusivo que te lleva a explorar rincones ocultos de la Reserva Nacional de Paracas.",
            "intro_p2": "Recorreremos senderos al borde de impresionantes acantilados donde el desierto cae abruptamente hacia el mar de forma espectacular.",
            "intro_p3": "La ruta culmina al atardecer, cuando la luz solar tiñe los cerros de arena y acantilados de un color dorado intenso y místico.",
            "why_title": "¿Cómo es la caminata?",
            "why_items": [
                {"icon": "directions_walk", "title": "Senderismo Moderado", "desc": "Caminata de aproximadamente 5 kilómetros apta para personas con condición física básica."},
                {"icon": "wb_twilight", "title": "Sombras Doradas", "desc": "Espectáculo visual al atardecer cuando las dunas costeras se iluminan de color oro."},
                {"icon": "explore", "title": "Acantilados Gigantes", "desc": "Miradores naturales hacia el mar abierto con formaciones de roca sedimentaria milenarias."},
                {"icon": "local_shipping", "title": "Transporte de Apoyo", "desc": "Vehículo de apoyo que acompaña al grupo para mayor seguridad y traslado de retorno."}
            ],
            "included": ["Transporte turístico ida y vuelta al punto de inicio", "Guía local certificado experto en senderismo", "Bastones de trekking (bajo solicitud)", "Fotos del recorrido tomadas por el guía"],
            "excluded": ["Boleto de entrada a la Reserva Nacional (S/ 11.00)"],
            "schedule_label": "* Salida diaria por la tarde a las 3:30 PM para coincidir con la puesta del sol. Duración: 3 horas aprox.",
            "faq_title": "Preguntas Frecuentes",
            "faqs": [
                {"q": "¿Cuánto cuesta el Golden Shadows Trek?", "a": "La caminata cuesta S/ 120 por persona e incluye transporte ida y vuelta al punto de inicio, guía certificado, bastones bajo solicitud y las fotos del recorrido tomadas por el guía. Solo se paga aparte la entrada a la Reserva (S/ 11)."},
                {"q": "¿Es una ruta físicamente exigente?", "a": "Es una ruta de nivel moderado-bajo de unos 5 km. Hay algunas pendientes suaves de arena pero el ritmo es pausado e incluye descansos en los miradores."},
                {"q": "¿Qué calzado es adecuado?", "a": "Es indispensable usar zapatillas deportivas con buen agarre o botas de caminata. No está permitido realizar el recorrido con sandalias o zapatos de suela lisa."},
                {"q": "¿Pueden ir niños al trekking?", "a": "Se recomienda para niños mayores de 10 años acostumbrados a caminar, debido a la duración de la caminata de casi 2.5 horas."},
                {"q": "¿Por qué se hace por la tarde?", "a": "La ruta está diseñada para llegar al mirador final justo cuando el sol cae sobre el mar: la luz dorada tiñe los acantilados y las dunas, el fenómeno que da nombre al trek. Además, se evita el calor del mediodía."}
            ]
        },
        "en": {
            "title": "Golden Shadows Trek: Paracas Sunset Hike in the National Reserve | SolyMar",
            "desc": "Book the Golden Shadows Trek: 3h Paracas sunset hike along cliffs & dunes of the National Reserve. S/ 120 (≈ US$ 33). English guide, photos, hotel pick-up & easy cancellation.",
            "h1": "Golden Shadows Trek: Paracas Sunset Hike in the National Reserve",
            "keywords": "trekking paracas, golden shadows trek, hiking paracas reserve, sunset walk paracas, trekking peru coast, hiking tour paracas",
            "subtitle": "Hike between gigantic ocean cliffs and golden sand dunes, witnessing a magical sunset over the Pacific.",
            "intro": "The <strong>Golden Shadows Trek</strong> is an exclusive hiking adventure that takes you to explore the hidden geographic wonders of the Paracas National Reserve.",
            "intro_p2": "We will walk along sandy trails bordering tall sea cliffs where the ocean waves meet the desert hills in dramatic fashion.",
            "intro_p3": "The hike is scheduled in the afternoon so we arrive at our final viewpoint as the setting sun colors the dunes and cliffs a brilliant gold.",
            "why_title": "Hike Highlights",
            "why_items": [
                {"icon": "directions_walk", "title": "Moderate Hiking", "desc": "A 5-kilometer (3-mile) hike suitable for active travelers with basic physical fitness."},
                {"icon": "wb_twilight", "title": "Golden Shadows", "desc": "Watch the sunlight play off the orange sand dunes, creating a glowing golden canvas."},
                {"icon": "explore", "title": "Massive Cliffs", "desc": "Hike to natural ledges overlooking the open Pacific Ocean waves crashing on the shore."},
                {"icon": "local_shipping", "title": "Safety Vehicle", "desc": "A support vehicle accompanies the group along the route for passenger security and return transfers."}
            ],
            "included": ["Round-trip tourist transport to the trail head", "Professional certified hiking guide", "Hike poles (available on request)", "Group photos taken by our guide"],
            "excluded": ["Paracas National Reserve entrance fee (S/ 11.00)"],
            "schedule_label": "* Daily departures in the afternoon at 3:30 PM. Duration: approx. 3 hours.",
            "faq_title": "Frequently Asked Questions",
            "faqs": [
                {"q": "How much does the Golden Shadows Trek cost?", "a": "The hike costs S/ 120 per person and includes round-trip transport to the trailhead, a certified guide, trekking poles on request, and photos of the hike taken by your guide. Only the Reserve entrance fee (S/ 11) is extra."},
                {"q": "Is the hike physically demanding?", "a": "The route is moderate-low difficulty, about 5 km. There are some gentle sandy climbs, but the pace is relaxed with plenty of stops at the viewpoints."},
                {"q": "What shoes should I wear?", "a": "Closed athletic shoes or hiking boots are mandatory. Flip-flops or flat-soled city shoes are not permitted for safety reasons."},
                {"q": "Can children join the trek?", "a": "We recommend this tour for children aged 10 and older who enjoy walking, given the 2.5-hour duration of the trail."},
                {"q": "Why is the trek in the afternoon?", "a": "The route is designed to reach the final viewpoint just as the sun sets over the ocean: the golden light paints the cliffs and dunes, the phenomenon that gives the trek its name. It also avoids the midday heat."}
            ]
        }
    },
    "adrenarena": {
        "filename": "adrenarena.html",
        "image": "img/adrenarena.jpg",
        "price": "S/ 150",
        "price_val": "150",
        "price_cur": "PEN",
        "category": "desierto",
        "es": {
            "title": "Adrenarena Paracas 2026: Buggies y Sandboard en Parque Privado | SolyMar",
            "desc": "Buggies tubulares y sandboard en Adrenarena, el parque de desierto privado a 15 minutos de Paracas: dunas de 150 m, circuito exclusivo y sin multitudes.",
            "h1": "Adrenarena Paracas: Buggies y Sandboard",
            "keywords": "adrenarena paracas, buggy paracas, sandboard paracas, areneros paracas, buggies cerca de paracas, aventura desierto paracas",
            "subtitle": "Disfruta de la mejor aventura en dunas gigantes dentro de un parque de desierto privado exclusivo en Paracas.",
            "intro": "<strong>Adrenarena</strong> es un parque de aventura privado ubicado a las afueras de Paracas, diseñado exclusivamente para el turismo de aventura en el desierto.",
            "intro_p2": "Con dunas de hasta 150 metros de altura, es el lugar ideal para subir a bordo de potentes buggies todoterreno y deslizarte a toda velocidad en tablas de sandboard.",
            "intro_p3": "Al ser un parque privado, garantizamos recorridos seguros en zonas exclusivas y sin las aglomeraciones de los circuitos públicos.",
            "why_title": "Lo mejor de Adrenarena",
            "why_items": [
                {"icon": "toys", "title": "Buggies de Alta Gama", "desc": "Vehículos todoterreno con motores potentes y equipamiento de seguridad homologado internacionalmente."},
                {"icon": "sports_skateboarding", "title": "Sandboard Profesional", "desc": "Tablas con fijaciones para botas que te permiten deslizarte de pie de forma controlada y segura."},
                {"icon": "security", "title": "Circuito Cerrado y Seguro", "desc": "Zonas de dunas exclusivas y vigiladas para evitar cruces con otros vehículos."},
                {"icon": "wb_sunny", "title": "Ubicación Estratégica", "desc": "A solo 15 minutos del muelle El Chaco en Paracas, sin necesidad de viajar hasta Ica."}
            ],
            "included": ["Ingreso al parque de aventura privado Adrenarena", "Paseo en buggy tubular con chofer especializado", "Tablas y equipos para la práctica de sandboarding", "Asistencia de guías socorristas en dunas"],
            "excluded": ["Traslado desde Paracas (disponible bajo solicitud)"],
            "schedule_label": "* Salidas diarias programadas. Se recomiendan turnos de tarde a partir de las 3:30 PM.",
            "faq_title": "Preguntas Frecuentes",
            "faqs": [
                {"q": "¿Cuánto cuesta la entrada a Adrenarena?", "a": "La experiencia cuesta S/ 150 por persona e incluye el ingreso al parque privado, el recorrido en buggy tubular con chofer especializado, las tablas de sandboard y la asistencia de guías en las dunas. El traslado desde Paracas está disponible bajo solicitud."},
                {"q": "¿Es apto para todas las edades?", "a": "Sí, el parque cuenta con circuitos adaptados. Ofrecemos paseos familiares pausados y circuitos de pura adrenalina para jóvenes de espíritu aventurero."},
                {"q": "¿Cuál es la diferencia con Huacachina?", "a": "Adrenarena está en Paracas, a solo 15 minutos del pueblo principal, y es un parque privado controlado: rutas exclusivas, sin cruces con otros vehículos y sin necesidad de viajar 1 hora 20 minutos hasta Ica."},
                {"q": "¿Qué debo llevar?", "a": "Ropa cómoda, zapatillas deportivas cerradas, bloqueador solar y lentes para proteger los ojos del viento y la arena. Tu cámara o celular debe ir bien asegurado dentro del buggy."},
                {"q": "¿Cuál es el mejor horario para ir?", "a": "Los turnos de tarde desde las 3:30 PM son los favoritos: la arena ya no quema para el sandboard y el circuito termina con la luz dorada del atardecer sobre las dunas."}
            ]
        },
        "en": {
            "title": "Adrenarena Paracas 2026: Private Buggy & Sandboard Park | SolyMar",
            "desc": "Tubular buggies and sandboarding at Adrenarena, the private desert park 15 minutes from Paracas: 150 m dunes, exclusive circuit and no crowds.",
            "h1": "Adrenarena Paracas: Buggies & Sandboarding",
            "keywords": "adrenarena paracas, buggy paracas, sandboarding paracas, sand dunes adventure, buggies near paracas, paracas desert adventure",
            "subtitle": "Enjoy the ultimate sand dune adventure inside an exclusive private desert park in Paracas.",
            "intro": "<strong>Adrenarena</strong> is a private adventure park located just outside Paracas, designed exclusively for dune buggies and sandboarding activities.",
            "intro_p2": "With dunes towering up to 150 meters, it is the perfect playground to ride high-powered off-road buggies and slide down sandy slopes.",
            "intro_p3": "Being a private facility, we ensure controlled and safe routes away from the crowded public tracks of the region.",
            "why_title": "Adrenarena Highlights",
            "why_items": [
                {"icon": "toys", "title": "Premium Buggies", "desc": "High-powered tubular vehicles equipped with professional roll cages and safety harness belts."},
                {"icon": "sports_skateboarding", "title": "Sandboard Equipment", "desc": "Proper sandboards with foot straps, allowing you to slide down standing up or lying down safely."},
                {"icon": "security", "title": "Exclusive Safe Trails", "desc": "Dedicated tracks inside the park, monitored to prevent collisions with other vehicles."},
                {"icon": "wb_sunny", "title": "Close to Paracas", "desc": "Located only 15 minutes away from El Chaco pier, saving you from traveling to Ica."}
            ],
            "included": ["Entry ticket to the private Adrenarena Adventure Park", "Tubular buggy tour with an experienced driver", "Sandboards and wax", "Assistance of route safety guides"],
            "excluded": ["Transport from Paracas (available on request)"],
            "schedule_label": "* Daily departures. Afternoon shifts starting at 3:30 PM are highly recommended.",
            "faq_title": "Frequently Asked Questions",
            "faqs": [
                {"q": "How much does Adrenarena cost?", "a": "The experience costs S/ 150 per person and includes entrance to the private park, the tubular buggy ride with a specialized driver, sandboards, and dune guide assistance. Transport from Paracas is available on request."},
                {"q": "Is it suitable for children?", "a": "Yes, we adjust the speed based on passenger preference. We offer calm family rides as well as high-adrenaline circuits for thrill-seekers."},
                {"q": "What is the difference between this and Huacachina?", "a": "Adrenarena is in Paracas (15 minutes from the hotels) and is a private, monitored park: exclusive trails, no crossings with other vehicles, and no need to travel 1 hour 20 minutes to Ica."},
                {"q": "What should I bring?", "a": "Comfortable sportswear, closed athletic shoes, sunblock, and sunglasses to protect your eyes from blowing sand. Cameras and phones must be well secured inside the buggy."},
                {"q": "What is the best time to go?", "a": "The afternoon slots from 3:30 PM are the favorites: the sand no longer burns for sandboarding and the circuit ends with the golden sunset light over the dunes."}
            ]
        }
    },
    "transporte-personalizado": {
        "filename": "transporte-personalizado.html",
        "image": "img/reserva-nacional-paracas.jpg",
        "price": "Cotizar",
        "price_val": "0",
        "price_cur": "PEN",
        "category": "traslados",
        "quote_only": True,
        "es": {
            "title": "Transporte Personalizado en Paracas 2026: Traslados y Tours en Ruta | SolyMar",
            "desc": "Traslados privados desde y hacia Lima, Ica, Huacachina o Nazca con base en Paracas. Convierte tu traslado en un tour con paradas que se adaptan a tu itinerario.",
            "h1": "Transporte personalizado desde y hacia Paracas",
            "keywords": "traslado lima paracas, transporte privado paracas, traslado paracas ica, transporte turistico paracas, taxi lima paracas, tour privado lima paracas, traslados con tours en ruta",
            "subtitle": "Viaja puerta a puerta entre Lima, Paracas, Ica o Nazca en vehículo privado, y convierte el trayecto en un tour con paradas a tu medida.",
            "intro": "Nuestro servicio de <strong>transporte personalizado</strong> conecta Paracas con Lima (incluido el aeropuerto Jorge Chávez), Ica, Huacachina, Nazca o cualquier ciudad de la ruta sur, en vehículos privados cómodos con chofer profesional.",
            "intro_p2": "La diferencia está en el camino: en lugar de un viaje directo, puedes <strong>agregar tours y paradas en ruta que se adaptan a tu itinerario</strong>: bodegas de la Ruta del Pisco, el sitio inca de Tambo Colorado, el oasis de Huacachina o los tours de Paracas antes de partir.",
            "intro_p3": "Tú eliges la hora de salida, las paradas y el ritmo del viaje; nosotros armamos la logística <strong>puerta a puerta</strong>, con tu equipaje siempre contigo, sin transbordos ni esperas de buses.",
            "why_title": "¿Por qué viajar con nuestro transporte privado?",
            "why_items": [
                {"icon": "route", "title": "Ruta a tu Medida", "desc": "Lima, aeropuerto, Ica, Huacachina, Nazca o el destino que necesites: diseñamos el trayecto según tu itinerario de viaje."},
                {"icon": "attractions", "title": "Tours en el Camino", "desc": "Convierte el traslado en excursión: bodegas de pisco, Tambo Colorado, Huacachina o la Reserva de Paracas, con paradas coordinadas."},
                {"icon": "airport_shuttle", "title": "Puerta a Puerta", "desc": "Te recogemos en tu hotel, aeropuerto o terminal y te dejamos exactamente donde necesitas, con tu equipaje siempre a bordo."},
                {"icon": "verified_user", "title": "Choferes Profesionales", "desc": "Vehículos modernos con mantenimiento al día y conductores formales con experiencia en la Panamericana Sur."}
            ],
            "included": ["Vehículo privado exclusivo para tu grupo (auto o minivan)", "Chofer profesional, combustible y peajes", "Recojo y llegada puerta a puerta (hotel, aeropuerto o terminal)", "Paradas y visitas coordinadas según tu itinerario", "Asistencia por WhatsApp durante todo el viaje"],
            "excluded": ["Entradas a los atractivos visitados en ruta", "Alimentación y bebidas", "Guía turístico a bordo (disponible como adicional)"],
            "schedule_label": "* Servicio disponible todos los días con reserva anticipada. La tarifa es por vehículo: cotización cerrada por WhatsApp según ruta, fecha y tamaño del grupo.",
            "faq_title": "Preguntas Frecuentes",
            "faqs": [
                {"q": "¿Cuánto cuesta el transporte personalizado?", "a": "La tarifa es por vehículo (no por persona) y depende de la ruta, las paradas que quieras agregar y el tipo de vehículo. Escríbenos tu itinerario por WhatsApp y en minutos te enviamos una cotización cerrada, sin cobros ocultos ni sorpresas."},
                {"q": "¿Qué rutas cubren?", "a": "Las más solicitadas son Lima ⇄ Paracas (incluido el aeropuerto Jorge Chávez), Paracas ⇄ Ica / Huacachina y Paracas ⇄ Nazca. También cubrimos Chincha, Cañete, Lunahuaná y cualquier punto de la Panamericana Sur."},
                {"q": "¿Qué tours puedo agregar en el camino?", "a": "Depende de tu ruta: hacia Ica puedes parar en las bodegas de la Ruta del Pisco o en Huacachina para buggies y sandboard; hacia el valle, en Tambo Colorado; y antes de salir de Paracas, las Islas Ballestas o la Reserva Nacional. Armamos el itinerario contigo por WhatsApp."},
                {"q": "¿Para cuántas personas es el servicio?", "a": "Contamos con autos para grupos pequeños y minivans para grupos grandes o con equipaje voluminoso. Indícanos cuántos viajan y te asignamos el vehículo adecuado, siempre de uso exclusivo para tu grupo."},
                {"q": "¿Con cuánta anticipación debo reservar?", "a": "Recomendamos reservar con 24 a 48 horas de anticipación para garantizar disponibilidad. En temporada alta (Semana Santa, Fiestas Patrias, feriados largos) conviene hacerlo con varios días de anticipación."},
                {"q": "¿Mi equipaje viaja seguro?", "a": "Sí. El vehículo es exclusivo para tu grupo y tu equipaje viaja contigo en la maletera durante todo el trayecto, incluidas las paradas para tours: nunca tienes que dejarlo en un hotel ni en consigna."}
            ]
        },
        "en": {
            "title": "Private Transfers in Paracas 2026: Lima, Ica & Tours en Route | SolyMar",
            "desc": "Private transfers to and from Lima, Ica, Huacachina or Nazca based in Paracas. Turn your transfer into a tour with stops that adapt to your itinerary.",
            "h1": "Custom Private Transport to and from Paracas",
            "keywords": "lima to paracas transfer, private transport paracas, paracas to ica transfer, paracas to huacachina transfer, private driver peru, lima paracas private car, transfer with tours en route",
            "subtitle": "Travel door to door between Lima, Paracas, Ica or Nazca in a private vehicle, and turn the journey into a tour with stops tailored to you.",
            "intro": "Our <strong>custom private transport</strong> service connects Paracas with Lima (including Jorge Chávez Airport), Ica, Huacachina, Nazca, or any city along the southern route, in comfortable private vehicles with a professional driver.",
            "intro_p2": "The difference is the journey itself: instead of a direct drive, you can <strong>add tours and stops en route that adapt to your itinerary</strong>: Pisco Route wineries, the Inca site of Tambo Colorado, the Huacachina Oasis, or the Paracas tours before departing.",
            "intro_p3": "You choose the departure time, the stops, and the pace; we handle the <strong>door-to-door logistics</strong>, with your luggage always with you: no bus connections, no waiting at terminals.",
            "why_title": "Why travel with our private transport?",
            "why_items": [
                {"icon": "route", "title": "Your Route, Your Way", "desc": "Lima, the airport, Ica, Huacachina, Nazca, or wherever you need: we design the journey around your travel itinerary."},
                {"icon": "attractions", "title": "Tours Along the Way", "desc": "Turn the transfer into an excursion: pisco wineries, Tambo Colorado, Huacachina, or the Paracas Reserve, with coordinated stops."},
                {"icon": "airport_shuttle", "title": "Door to Door", "desc": "We pick you up at your hotel, airport, or terminal and drop you exactly where you need, with your luggage always on board."},
                {"icon": "verified_user", "title": "Professional Drivers", "desc": "Modern, well-maintained vehicles and licensed drivers experienced on the Pan-American South highway."}
            ],
            "included": ["Private vehicle exclusively for your group (car or minivan)", "Professional driver, fuel, and tolls", "Door-to-door pick-up and drop-off (hotel, airport, or terminal)", "Stops and visits coordinated to your itinerary", "WhatsApp assistance throughout the journey"],
            "excluded": ["Entrance fees to attractions visited en route", "Meals and drinks", "Onboard tour guide (available as an add-on)"],
            "schedule_label": "* Available every day with advance booking. Rates are per vehicle: get a fixed quote via WhatsApp based on route, date, and group size.",
            "faq_title": "Frequently Asked Questions",
            "faqs": [
                {"q": "How much does the private transport cost?", "a": "The rate is per vehicle (not per person) and depends on the route, the stops you want to add, and the vehicle type. Send us your itinerary on WhatsApp and we will reply within minutes with a fixed quote: no hidden charges, no surprises."},
                {"q": "Which routes do you cover?", "a": "The most requested are Lima ⇄ Paracas (including Jorge Chávez Airport), Paracas ⇄ Ica / Huacachina, and Paracas ⇄ Nazca. We also cover Chincha, Cañete, Lunahuaná, and any point along the Pan-American South highway."},
                {"q": "What tours can I add along the way?", "a": "It depends on your route: towards Ica you can stop at the Pisco Route wineries or at Huacachina for buggies and sandboarding; up the valley, at Tambo Colorado; and before leaving Paracas, the Ballestas Islands or the National Reserve. We build the itinerary with you over WhatsApp."},
                {"q": "How many people can travel?", "a": "We have cars for small groups and minivans for larger groups or bulky luggage. Tell us how many are traveling and we will assign the right vehicle, always for your group's exclusive use."},
                {"q": "How far in advance should I book?", "a": "We recommend booking 24 to 48 hours ahead to guarantee availability. During high season (Easter, national holidays, long weekends), it is best to book several days in advance."},
                {"q": "Is my luggage safe during the trip?", "a": "Yes. The vehicle is exclusive to your group and your luggage travels with you in the trunk for the entire journey, including tour stops, so you never have to leave it at a hotel or storage."}
            ]
        }
    }
}

tours_formatted = tours

# ==========================================
# CONSTANTS & METADATA FOR ENHANCED TOURS
# ==========================================

PRICE_USD_MAP = {
    "islas-ballestas": "≈ US$ 22",
    "reserva-nacional-paracas": "≈ US$ 14",
    "ballestas-y-reserva-full-day": "≈ US$ 33",
    "buggies-sandboard-huacachina": "≈ US$ 19",
    "ruta-del-pisco-bodegas-ica": "≈ US$ 22",
    "paracas-huacachina-full-day": "≈ US$ 52",
    "parapente": "≈ US$ 68",
    "buceo": "≈ US$ 109",
    "kayak-paddle-paracas": "≈ US$ 16",
    "mini-buggies-paracas": "≈ US$ 33",
    "tambo-colorado": "≈ US$ 22",
    "yakupark-paracas": "≈ US$ 14",
    "trekking": "≈ US$ 33",
    "adrenarena": "≈ US$ 40",
    "transporte-personalizado": "Custom Quote",
}

QUICK_FACTS = {
    "islas-ballestas": {
        "es": {"sched": "8:00 AM y 10:00 AM", "sched_sub": "Salidas diarias muelle", "dur": "2 Horas", "dur_sub": "Navegación guiada", "type": "Crucero en Lancha", "type_sub": "Fauna y Candelabro", "diff": "Fácil", "diff_sub": "Todas las edades", "guide": "Guía Bilingüe", "guide_sub": "Certificado a bordo", "group": "Lancha Compartida", "group_sub": "Chaleco salvavidas inc."},
        "en": {"sched": "8:00 AM & 10:00 AM", "sched_sub": "Daily pier departures", "dur": "2 Hours", "dur_sub": "Guided navigation", "type": "Speedboat Cruise", "type_sub": "Wildlife & Candelabra", "diff": "Easy", "diff_sub": "All ages welcome", "guide": "Bilingual Guide", "guide_sub": "Certified on board", "group": "Shared Boat", "group_sub": "Life vests included"}
    },
    "reserva-nacional-paracas": {
        "es": {"sched": "Diario 11:00 AM", "sched_sub": "Recojo en hotel 10:45 AM", "dur": "3.5 Horas", "dur_sub": "Circuito terrestre", "type": "Ruta Costera", "type_sub": "Playa Roja y Catedral", "diff": "Fácil", "diff_sub": "Apto para familias", "guide": "Guía Bilingüe", "guide_sub": "Experto en geología", "group": "Grupo Reducido", "group_sub": "Miniván climatizada"},
        "en": {"sched": "Daily 11:00 AM", "sched_sub": "Hotel pick-up 10:45 AM", "dur": "3.5 Hours", "dur_sub": "Coastal road tour", "type": "Coastal Route", "type_sub": "Red Beach & Cathedral", "diff": "Easy", "diff_sub": "Family friendly", "guide": "Bilingual Guide", "guide_sub": "Geology & nature expert", "group": "Small Group", "group_sub": "Air-conditioned van"}
    },
    "ballestas-y-reserva-full-day": {
        "es": {"sched": "Diario 8:00 AM", "sched_sub": "Recojo 7:45 AM", "dur": "6.5 Horas", "dur_sub": "Día completo Paracas", "type": "Combo Mar y Desierto", "type_sub": "Ballestas + Reserva", "diff": "Fácil", "diff_sub": "Todas las edades", "guide": "Guía Bilingüe", "guide_sub": "Acompañamiento total", "group": "Grupo Reducido", "group_sub": "Tiempo para almorzar"},
        "en": {"sched": "Daily 8:00 AM", "sched_sub": "Pick-up 7:45 AM", "dur": "6.5 Hours", "dur_sub": "Full Paracas experience", "type": "Sea & Desert Combo", "type_sub": "Ballestas + Reserve", "diff": "Easy", "diff_sub": "All ages welcome", "guide": "Bilingual Guide", "guide_sub": "Full accompaniment", "group": "Small Group", "group_sub": "Lunch break included"}
    },
    "buggies-sandboard-huacachina": {
        "es": {"sched": "4:00 PM (Atardecer)", "sched_sub": "Turno estelar en dunas", "dur": "2 Horas", "dur_sub": "Adrenalina pura", "type": "Tubulares 4x4", "type_sub": "Dunas de Huacachina", "diff": "Moderado", "diff_sub": "Paseo de aventura", "guide": "Piloto Experto", "guide_sub": "Altamente calificado", "group": "Grupo Reducido", "group_sub": "Tablas incluidas"},
        "en": {"sched": "4:00 PM (Sunset)", "sched_sub": "Best golden hour slot", "dur": "2 Hours", "dur_sub": "Pure desert adrenaline", "type": "Dune Buggy 4x4", "type_sub": "Huacachina dunes", "diff": "Moderate", "diff_sub": "Adventure activity", "guide": "Pro Dune Driver", "guide_sub": "Highly experienced", "group": "Small Group", "group_sub": "Sandboards included"}
    },
    "ruta-del-pisco-bodegas-ica": {
        "es": {"sched": "Diario 10:00 AM", "sched_sub": "Recojo en hotel", "dur": "4 Horas", "dur_sub": "Recorrido vitivinícola", "type": "Cata y Tradición", "type_sub": "Bodegas artesanal e industrial", "diff": "Fácil", "diff_sub": "Cultural y gastronómico", "guide": "Guía Sommelier", "guide_sub": "Especialista pisquero", "group": "Grupo Reducido", "group_sub": "Degustación incluida"},
        "en": {"sched": "Daily 10:00 AM", "sched_sub": "Hotel pick-up", "dur": "4 Hours", "dur_sub": "Winery & vineyard trail", "type": "Tasting & Heritage", "type_sub": "Artisanal & historic cellars", "diff": "Easy", "diff_sub": "Culture & tasting", "guide": "Sommelier Guide", "guide_sub": "Pisco expert", "group": "Small Group", "group_sub": "Tastings included"}
    },
    "paracas-huacachina-full-day": {
        "es": {"sched": "Diario 8:00 AM", "sched_sub": "Salida temprano", "dur": "10 Horas", "dur_sub": "Ballestas + Huacachina", "type": "Combo Todo en Uno", "type_sub": "Mar, Reserva y Dunas", "diff": "Fácil - Moderado", "diff_sub": "Aventura completa", "guide": "Guía Bilingüe", "guide_sub": "Coordinación continua", "group": "Grupo Reducido", "group_sub": "Todos los traslados inc."},
        "en": {"sched": "Daily 8:00 AM", "sched_sub": "Early morning start", "dur": "10 Hours", "dur_sub": "Ballestas + Huacachina", "type": "All-in-One Combo", "type_sub": "Sea, Reserve & Dunes", "diff": "Easy - Moderate", "diff_sub": "Complete day trip", "guide": "Bilingual Guide", "guide_sub": "Full-day assistance", "group": "Small Group", "group_sub": "All transfers included"}
    },
    "parapente": {
        "es": {"sched": "12:00 PM - 4:00 PM", "sched_sub": "Ventana de viento óptima", "dur": "15-20 min vuelo", "dur_sub": "2h actividad total", "type": "Vuelo Tándem", "type_sub": "Cerro Maldito / Supay", "diff": "Fácil", "diff_sub": "Sin experiencia previa", "guide": "Piloto Instructor", "guide_sub": "Licencia oficial APVL", "group": "Vuelo 1 a 1", "group_sub": "Equipos homologados"},
        "en": {"sched": "12:00 PM - 4:00 PM", "sched_sub": "Optimal wind window", "dur": "15-20 min flight", "dur_sub": "2h total experience", "type": "Tandem Paragliding", "type_sub": "Cerro Maldito / Supay", "diff": "Easy", "diff_sub": "No experience needed", "guide": "Certified Pilot", "guide_sub": "Official APVL license", "group": "1-on-1 Tandem", "group_sub": "Certified safety gear"}
    },
    "buceo": {
        "es": {"sched": "Diario 9:00 AM", "sched_sub": "Muelle de Paracas", "dur": "3 Horas", "dur_sub": "Teoría + Inmersión", "type": "Bautismo PADI", "type_sub": "Fauna submarina Pacífico", "diff": "Principiantes", "diff_sub": "No requiere certificación", "guide": "Instructor PADI", "guide_sub": "Supervisión directa en agua", "group": "Atención Personal", "group_sub": "Max 2 buzos por instructor"},
        "en": {"sched": "Daily 9:00 AM", "sched_sub": "Paracas dock", "dur": "3 Hours", "dur_sub": "Theory + Pacific dive", "type": "PADI Discovery Scuba", "type_sub": "Pacific marine life", "diff": "Beginner Friendly", "diff_sub": "No prior cert required", "guide": "PADI Instructor", "guide_sub": "1-on-1 in-water care", "group": "Small Group", "group_sub": "Max 2 divers per pro"}
    },
    "kayak-paddle-paracas": {
        "es": {"sched": "6:30 AM - 9:00 AM", "sched_sub": "Mar en calma matutina", "dur": "1.5 - 2 Horas", "dur_sub": "Paseo por la bahía", "type": "Travesía a Remo", "type_sub": "Bahía de Paracas", "diff": "Fácil", "diff_sub": "Apto principiantes", "guide": "Instructor de Seguridad", "guide_sub": "Inducción y apoyo", "group": "Kayaks Simples/Dobles", "group_sub": "Chaleco salvavidas inc."},
        "en": {"sched": "6:30 AM - 9:00 AM", "sched_sub": "Calm morning waters", "dur": "1.5 - 2 Hours", "dur_sub": "Bay exploration", "type": "Paddling Tour", "type_sub": "Paracas Bay wildlife", "diff": "Easy", "diff_sub": "Beginner friendly", "guide": "Safety Instructor", "guide_sub": "Briefing & support", "group": "Single or Double", "group_sub": "Life vests included"}
    },
    "mini-buggies-paracas": {
        "es": {"sched": "Salidas programadas", "sched_sub": "Mañanas y tardes", "dur": "2 Horas", "dur_sub": "Circuito por dunas", "type": "Manejo Propio 4x4", "type_sub": "Dunas y senderos desérticos", "diff": "Fácil - Moderado", "diff_sub": "Breve instrucción previa", "guide": "Guía Líder 4x4", "guide_sub": "Vehículo guía y auxilio", "group": "2 por Buggy", "group_sub": "Casco y antiparras inc."},
        "en": {"sched": "Scheduled departures", "sched_sub": "Mornings & afternoons", "dur": "2 Hours", "dur_sub": "Dune trail driving", "type": "Self-Drive Buggies", "type_sub": "Dunes & desert trails", "diff": "Easy - Moderate", "diff_sub": "Briefing & practice", "guide": "Lead Guide & Support", "guide_sub": "Pace leader & assistance", "group": "2 per Buggy", "group_sub": "Helmet & goggles inc."}
    },
    "tambo-colorado": {
        "es": {"sched": "Diario 9:00 AM", "sched_sub": "Recojo en hotel", "dur": "3 Horas", "dur_sub": "Valle de Pisco", "type": "Arqueología Inca", "type_sub": "Palacio de adobe rojo", "diff": "Fácil", "diff_sub": "Paseo peatonal suave", "guide": "Guía de Historia", "guide_sub": "Certificado especializado", "group": "Grupo Reducido", "group_sub": "Transporte ida y vuelta"},
        "en": {"sched": "Daily 9:00 AM", "sched_sub": "Hotel pick-up", "dur": "3 Hours", "dur_sub": "Pisco river valley", "type": "Inca Archaeology", "type_sub": "Painted adobe fortress", "diff": "Easy", "diff_sub": "Gentle walking tour", "guide": "History Guide", "guide_sub": "Certified local expert", "group": "Small Group", "group_sub": "Round-trip transfer"}
    },
    "yakupark-paracas": {
        "es": {"sched": "9:00 AM - 5:00 PM", "sched_sub": "Turnos continuos", "dur": "45 min circuito", "dur_sub": "En la bahía El Chaco", "type": "Parque Acuático", "type_sub": "Obstáculos inflables en mar", "diff": "Divertido y Activo", "diff_sub": "Desde los 7 años", "guide": "Salvavidas en Agua", "guide_sub": "Staff de seguridad permanente", "group": "Circuito Abierto", "group_sub": "Chaleco obligatorio inc."},
        "en": {"sched": "9:00 AM - 5:00 PM", "sched_sub": "Continuous sessions", "dur": "45 min circuit", "dur_sub": "El Chaco beachfront", "type": "Inflatable Water Park", "type_sub": "Floating sea obstacle course", "diff": "Fun & Active", "diff_sub": "Ages 7 and older", "guide": "Certified Lifeguards", "guide_sub": "Stationed on obstacles", "group": "Open Session", "group_sub": "Mandatory vest included"}
    },
    "trekking": {
        "es": {"sched": "Diario 3:30 PM", "sched_sub": "Recojo en hotel 3:15 PM", "dur": "3 Horas", "dur_sub": "Retorno 6:30-7:00 PM", "type": "Sombras Doradas", "type_sub": "5 km acantilados y dunas", "diff": "Fácil - Moderado", "diff_sub": "Paso relajado para fotos", "guide": "Guía en Inglés / Español", "guide_sub": "Certificado en senderismo", "group": "Grupo Reducido", "group_sub": "Max 8-10 senderistas"},
        "en": {"sched": "Daily 3:30 PM", "sched_sub": "Hotel pick-up 3:15 PM", "dur": "3 Hours", "dur_sub": "Back by 6:30-7:00 PM", "type": "Golden Shadows", "type_sub": "5 km ocean cliffs & dunes", "diff": "Easy - Moderate", "diff_sub": "Relaxed photo pace", "guide": "English-Speaking Guide", "guide_sub": "Certified hiking expert", "group": "Small Group", "group_sub": "Max 8-10 hikers"}
    },
    "adrenarena": {
        "es": {"sched": "Previa reserva", "sched_sub": "Turnos mañana y tarde", "dur": "3 - 4 Horas", "dur_sub": "Experiencia completa", "type": "Parque Mega Dunas", "type_sub": "Aventura extrema desierto", "diff": "Moderado - Alto", "diff_sub": "Para amantes de emoción", "guide": "Instructores Expertos", "guide_sub": "Personal certificado", "group": "Grupo Reducido", "group_sub": "Equipos de seguridad inc."},
        "en": {"sched": "By reservation", "sched_sub": "Morning & afternoon slots", "dur": "3 - 4 Hours", "dur_sub": "Full park experience", "type": "Mega Dunes Park", "type_sub": "Extreme desert adventure", "diff": "Moderate - High", "diff_sub": "Thrill-seeker friendly", "guide": "Expert Instructors", "guide_sub": "Certified safety crew", "group": "Small Group", "group_sub": "Full safety gear inc."}
    },
    "transporte-personalizado": {
        "es": {"sched": "100% a tu medida", "sched_sub": "Disponible 24/7", "dur": "A convenir", "dur_sub": "Según ruta elegida", "type": "Traslado Privado", "type_sub": "Puerta a puerta", "diff": "Confort Ejecutivo", "diff_sub": "Vehículos modernos climatizados", "guide": "Conductor Profesional", "guide_sub": "Puntual y experimentado", "group": "Servicio Exclusivo", "group_sub": "Solo para tu grupo"},
        "en": {"sched": "100% Tailored", "sched_sub": "Available 24/7", "dur": "Flexible", "dur_sub": "Based on chosen route", "type": "Private Transfer", "type_sub": "Door-to-door service", "diff": "Executive Comfort", "diff_sub": "Modern air-conditioned cars", "guide": "Pro Driver", "guide_sub": "Punctual & experienced", "group": "Exclusive Ride", "group_sub": "Only for your group"}
    }
}

WHAT_TO_BRING = {
    "mar": {
        "es": [
            ("air", "Casaca cortavientos", "El viento marino es fresco en la lancha, especialmente en el trayecto de ida y vuelta."),
            ("wb_sunny", "Bloqueador y lentes de sol", "Alta radiación en mar abierto. Gorro o sombrero con ajuste para que no vuele."),
            ("photo_camera", "Cámara o celular con correa", "Asegura bien tus dispositivos para capturar fotos de lobos y pingüinos."),
            ("payments", "Efectivo para tasas de muelle", "S/ 16 por adulto (SERNANP + tasa de embarque) a pagar en la boletería del muelle."),
            ("medication", "Pastilla para mareo (opcional)", "Si eres sensible al movimiento, tómala 30 minutos antes de zarpar."),
            ("water_drop", "Botella de agua", "Mantente hidratado durante la travesía de 2 horas.")
        ],
        "en": [
            ("air", "Windbreaker or light jacket", "Ocean breeze can be brisk on the speedboat, especially during transit to the islands."),
            ("wb_sunny", "Sunscreen & sunglasses", "High UV reflection on open water. A hat with a chin strap is recommended."),
            ("photo_camera", "Camera or phone with strap", "Secure your device firmly to shoot photos of sea lions and penguins safely."),
            ("payments", "Cash for pier taxes", "S/ 16 per adult (SERNANP + boarding tax) paid in cash at the pier ticket booth."),
            ("medication", "Motion sickness pill (optional)", "If prone to seasickness, take medication 30 minutes before boarding."),
            ("water_drop", "Water bottle", "Stay comfortably hydrated during the 2-hour marine excursion.")
        ]
    },
    "desierto": {
        "es": [
            ("hiking", "Calzado cerrado o zapatillas", "Indispensable para caminar con tracción sobre arena y miradores rocosos."),
            ("air", "Casaca cortavientos", "En el desierto corre viento costero en las tardes; la temperatura baja rápidamente al atardecer."),
            ("wb_sunny", "Bloqueador y lentes de sol", "Fuerte reflejo del sol sobre la arena. Protege tu piel y ojos."),
            ("water_drop", "1 a 1.5 L de agua", "Lleva agua suficiente para mantenerte hidratado en el clima seco del desierto."),
            ("payments", "Efectivo para la entrada", "Entrada SERNANP (S/ 11 adultos) en efectivo si tu tour visita la Reserva."),
            ("photo_camera", "Celular con batería cargada", "Paisajes desérticos espectaculares ideales para fotografía panorámica.")
        ],
        "en": [
            ("hiking", "Closed shoes or sneakers", "Mandatory for traction on sand trails, dune climbs, and rocky cliff viewpoints."),
            ("air", "Windbreaker jacket", "Desert coastal winds pick up late afternoon; temperature cools rapidly at sunset."),
            ("wb_sunny", "Sunscreen & sunglasses", "Strong sun reflection off desert sand. Essential UV protection for skin and eyes."),
            ("water_drop", "1 to 1.5 L of water", "Stay properly hydrated throughout your desert adventure in the dry climate."),
            ("payments", "Cash for entrance fee", "SERNANP reserve gate fee (S/ 11 adults) paid in Peruvian Soles cash on arrival."),
            ("photo_camera", "Charged camera or smartphone", "Spectacular desert and coastal panoramas perfect for wide-angle photos.")
        ]
    },
    "aire": {
        "es": [
            ("badge", "DNI o Pasaporte", "Documento de identidad para el registro y seguro del vuelo tándem."),
            ("hiking", "Zapatillas cómodas y cerradas", "Calzado seguro para la carrera de despegue y aterrizaje en tierra."),
            ("air", "Cortavientos o casaca ligera", "El viento en los acantilados de despegue (Cerro Maldito / Supay) es fresco."),
            ("wb_sunny", "Lentes de sol y bloqueador", "Alta radiación en el aire y la zona de vuelo en el desierto costero."),
            ("payments", "Efectivo para ingreso a la Reserva", "S/ 11 por adulto (tasa SERNANP) a pagar en la garita del parque."),
            ("photo_camera", "Celular o cámara con correa", "El vuelo tándem incluye fotos y videos en alta definición.")
        ],
        "en": [
            ("badge", "Passport or National ID", "Identification document required for tandem flight registration and insurance."),
            ("hiking", "Comfortable closed sneakers", "Secure footwear essential for the takeoff run and smooth landing."),
            ("air", "Windbreaker or light jacket", "Coastal cliff launch sites (Cerro Maldito / Supay) are windy and fresh."),
            ("wb_sunny", "Sunglasses & sunscreen", "High solar radiation while gliding above the desert coastline."),
            ("payments", "Cash for park entrance", "SERNANP reserve gate fee (S/ 11 adults) paid in Peruvian Soles cash."),
            ("photo_camera", "Phone or camera with strap", "Tandem flights include high-definition action photos and video.")
        ]
    },
    "cultura": {
        "es": [
            ("hiking", "Zapatillas cómodas para caminar", "Los sitios arqueológicos y bodegas cuentan con senderos de tierra y adoquines."),
            ("wb_sunny", "Gorro, bloqueador y lentes de sol", "Ica y Pisco tienen clima soleado y caluroso todo el año."),
            ("water_drop", "Botella de agua", "Mantén la hidratación durante las visitas y recorridos guiados."),
            ("payments", "Efectivo para compras y degustaciones", "Para adquirir botellas de pisco artesanal, vinos o souvenirs locales."),
            ("photo_camera", "Cámara o celular", "Arquitectura inca y lagares coloniales con gran valor fotográfico e histórico.")
        ],
        "en": [
            ("hiking", "Comfortable walking shoes", "Archaeological ruins and wineries have cobblestone, dirt, and stone pathways."),
            ("wb_sunny", "Sun hat, sunscreen & sunglasses", "Ica and Pisco enjoy sunny, warm desert weather year-round."),
            ("water_drop", "Water bottle", "Stay hydrated during guided historical walks and cellar tours."),
            ("payments", "Cash for tastings and souvenirs", "Helpful for purchasing artisanal pisco bottles, wines, and local delicacies."),
            ("photo_camera", "Camera or smartphone", "Colonial lagares and Inca adobe architecture offer rich photo opportunities.")
        ]
    },
    "traslados": {
        "es": [
            ("badge", "DNI o Pasaporte", "Documento de identificación para registros en ruta y controles de tránsito."),
            ("checkroom", "Ropa cómoda de viaje", "Viste prendas confortables para trayectos interurbanos en vehículo climatizado."),
            ("battery_charging_full", "Cargador y audífonos", "Nuestros vehículos cuentan con tomas USB para cargar tus dispositivos."),
            ("water_drop", "Bebida o snacks personales", "Para disfrutar durante las paradas y el viaje por la carretera Panamericana.")
        ],
        "en": [
            ("badge", "Passport or ID", "Personal identification for highway checkpoints and hotel check-ins."),
            ("checkroom", "Comfortable travel clothing", "Dress in comfortable layers for highway journeys in air-conditioned vehicles."),
            ("battery_charging_full", "Phone charger & headphones", "Our modern vehicles feature USB ports to keep your electronics charged."),
            ("water_drop", "Water & snacks", "Enjoy refreshments during highway stops and your scenic drive along the coast.")
        ]
    }
}

# ==========================================
# MASTER HTML TEMPLATE FOR INDIVIDUAL TOURS
# ==========================================

# Responsive images: optimize_images.py writes img/w/<name>-<width>.webp variants.
def img_variants(image):
    name = os.path.splitext(os.path.basename(image))[0]
    widths = sorted(int(p.rsplit("-", 1)[1][:-5]) for p in glob.glob(f"img/w/{name}-*.webp"))
    return name, widths


def img_attrs(root_prefix, image, sizes):
    """src/srcset/sizes attributes for an <img>, falling back to the original file."""
    name, widths = img_variants(image)
    if not widths:
        return f'src="{root_prefix}{image}"'
    srcset = ", ".join(f"{root_prefix}img/w/{name}-{w}.webp {w}w" for w in widths)
    return f'src="{root_prefix}img/w/{name}-{widths[-1]}.webp" srcset="{srcset}" sizes="{sizes}"'


def img_preload(root_prefix, image):
    name, widths = img_variants(image)
    if not widths:
        return ""
    srcset = ", ".join(f"{root_prefix}img/w/{name}-{w}.webp {w}w" for w in widths)
    return f'<link rel="preload" as="image" imagesrcset="{srcset}" imagesizes="100vw" fetchpriority="high" />'


# Shared SVG snippets (WhatsApp mark from Simple Icons; Candelabro de Paracas line mark)
WA_ICON = '<svg class="w-5 h-5 fill-current shrink-0" viewBox="0 0 24 24" aria-hidden="true"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413Z"/></svg>'
CANDELABRO = ('<svg viewBox="0 0 100 180" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" '
              'stroke-linejoin="round" aria-hidden="true" class="hidden md:block absolute right-8 lg:right-24 bottom-0 h-[85%] w-auto text-sand/35">'
              '<path pathLength="1" vector-effect="non-scaling-stroke" d="M50 172V14M34 172H66M50 128C31 128 22 116 22 96V42M50 128C69 128 78 116 78 96V42'
              'M50 76L40 63M50 76L60 63M22 66L13 55M22 66L31 55M78 66L69 55M78 66L87 55"/></svg>')

template = """<!DOCTYPE html>
<html lang="{lang}">

<head>
    <meta charset="utf-8" />
    <link rel="icon" type="image/webp" href="{root_prefix}img/SolyMar-ico.webp" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <!-- ===== SEO: META TITLE & DESCRIPTION ===== -->
    <title>{title}</title>
    <meta name="description" content="{desc}">
    <meta name="robots" content="index, follow">
    <meta name="author" content="SolyMar Paracas">
    <link rel="canonical" href="{canonical}">
    <link rel="alternate" hreflang="es" href="{canonical_es}">
    <link rel="alternate" hreflang="en" href="{canonical_en}">
    <link rel="alternate" hreflang="x-default" href="{canonical_es}">

    <!-- ===== OPEN GRAPH ===== -->
    <meta property="og:type" content="website">
    <meta property="og:url" content="{canonical}">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{desc}">
    <meta property="og:image" content="https://solymarparacas.com/{image}">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">
    <meta property="og:locale" content="{locale}">
    <meta property="og:site_name" content="SolyMar Paracas">

    <!-- ===== TWITTER CARD ===== -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{title}">
    <meta name="twitter:description" content="{desc}">
    <meta name="twitter:image" content="https://solymarparacas.com/{image}">
    <!-- ===== FIN SEO ===== -->
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,400..800&display=swap" rel="stylesheet" />
    <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0,0&icon_names=access_time,account_circle,add,air,airport_shuttle,architecture,arrow_downward,arrow_forward,attractions,auto_awesome,badge,battery_charging_full,call,check,checkroom,cloud_sync,coffee,credit_card,departure_board,directions_boat,directions_bus,directions_car,directions_walk,domain,egg,event_available,expand_more,explore,flutter_dash,group,groups,health_and_safety,hiking,history_edu,info,landscape,local_activity,local_bar,local_shipping,location_on,mail,map,medication,museum,payments,pets,photo_camera,pool,record_voice_over,restaurant,restaurant_menu,route,rowing,schedule,security,sell,shield,speed,sports_motorsports,sports_skateboarding,surfing,terrain,timelapse,toys,verified,verified_user,video_camera_back,visibility,water,water_drop,water_slide,wb_sunny,wb_twilight,wind_power,wine_bar,workspace_premium&display=block" rel="stylesheet" />
    <link rel="stylesheet" href="{root_prefix}css/style.css" />
    {hero_preload}

    <!-- ===== ESTRUCTURA DE DATOS (JSON-LD) PARA GOOGLE ===== -->
    <script type="application/ld+json">
    [
      {{
        "@context": "https://schema.org",
        "@type": "TouristTrip",
        "name": {json_h1},
        "description": {json_desc},
        "touristType": ["Adventure tourism", "Eco tourism", "Nature tourism"],
        "provider": {{
          "@type": "TravelAgency",
          "name": "SolyMar Paracas",
          "url": "https://solymarparacas.com/",
          "telephone": "+51 961 542 547",
          "address": {{
            "@type": "PostalAddress",
            "streetAddress": "El Chaco, Paracas",
            "addressLocality": "Paracas",
            "addressRegion": "Ica",
            "addressCountry": "PE"
          }}
        }},
        {offers_json}"image": [
          "https://solymarparacas.com/{image}"
        ]
      }},
      {{
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
          {{
            "@type": "ListItem",
            "position": 1,
            "name": "{home_label}",
            "item": "{home_url}"
          }},
          {{
            "@type": "ListItem",
            "position": 2,
            "name": "{tours_index_label}",
            "item": "{tours_index_url}"
          }},
          {{
            "@type": "ListItem",
            "position": 3,
            "name": {json_h1},
            "item": "{canonical}"
          }}
        ]
      }}{faq_schema}
    ]
    </script>
</head>

<body class="font-sans bg-surface text-on-surface leading-relaxed antialiased overflow-x-hidden pt-16 pb-20 lg:pb-0">
    <nav id="header-placeholder"></nav>

    <main>
        <!-- Hero -->
        <section class="relative min-h-[min(78dvh,760px)] flex items-end overflow-hidden bg-deep">
            <img class="absolute inset-0 w-full h-full object-cover" {hero_img_attrs} alt="{h1}" fetchpriority="high" decoding="async" />
            <div class="absolute inset-0 bg-gradient-to-r from-deep/90 via-deep/55 to-deep/10"></div>
            <div class="absolute inset-x-0 bottom-0 h-2/3 bg-gradient-to-t from-deep/80 to-transparent"></div>
            <div class="relative w-full max-w-[1400px] mx-auto px-4 sm:px-8 pt-24 pb-14 md:pb-20">
                <div class="max-w-[860px] text-white">
                    <nav aria-label="Breadcrumb" class="rise-in text-sm text-white/75 mb-5">
                        <a href="{home_link}" class="hover:text-white hover:underline">{home_label}</a>
                        <span class="mx-2 text-sand" aria-hidden="true">/</span>
                        <a href="{tours_link}" class="hover:text-white hover:underline">{tours_index_label}</a>
                        <span class="mx-2 text-sand" aria-hidden="true">/</span>
                        <span aria-current="page">{breadcrumb_title}</span>
                    </nav>
                    <h1 class="rise-in [--i:1] font-display text-4xl sm:text-5xl lg:text-6xl leading-[1.04] mb-6 text-balance">{h1}</h1>
                    <p class="rise-in [--i:2] text-lg md:text-xl text-white/85 leading-relaxed max-w-[52ch] mb-9">{subtitle}</p>
                    <a href="https://api.whatsapp.com/send?phone=+51961542547&text={whatsapp_text}" target="_blank" rel="noopener" class="rise-in [--i:3] inline-flex items-center justify-center gap-2.5 bg-tertiary text-on-tertiary py-3.5 px-7 rounded-full font-semibold whitespace-nowrap transition-colors hover:bg-tertiary-container active:scale-[0.98]">
                        {wa_icon}
                        <span>{sidebar_whatsapp_btn}</span>
                    </a>
                </div>
            </div>
        </section>

        <!-- Datos rápidos -->
        <section class="bg-surface-container-low border-b border-primary/10 px-4 sm:px-8 py-8">
            <dl class="max-w-[1336px] mx-auto grid grid-cols-2 gap-x-6 gap-y-7 md:grid-cols-4 lg:grid-cols-7">
                <div class="flex flex-col gap-1 border-l-2 border-sand pl-4">
                    <span class="material-symbols-outlined text-xl text-primary mb-1" aria-hidden="true">schedule</span>
                    <dt class="order-last text-sm text-on-surface-variant leading-snug">{qf_sched_sub}</dt>
                    <dd class="font-semibold text-on-surface leading-snug">{qf_sched}</dd>
                </div>
                <div class="flex flex-col gap-1 border-l-2 border-sand pl-4">
                    <span class="material-symbols-outlined text-xl text-primary mb-1" aria-hidden="true">timelapse</span>
                    <dt class="order-last text-sm text-on-surface-variant leading-snug">{qf_dur_sub}</dt>
                    <dd class="font-semibold text-on-surface leading-snug">{qf_dur}</dd>
                </div>
                <div class="flex flex-col gap-1 border-l-2 border-sand pl-4">
                    <span class="material-symbols-outlined text-xl text-primary mb-1" aria-hidden="true">terrain</span>
                    <dt class="order-last text-sm text-on-surface-variant leading-snug">{qf_type_sub}</dt>
                    <dd class="font-semibold text-on-surface leading-snug">{qf_type}</dd>
                </div>
                <div class="flex flex-col gap-1 border-l-2 border-sand pl-4">
                    <span class="material-symbols-outlined text-xl text-primary mb-1" aria-hidden="true">speed</span>
                    <dt class="order-last text-sm text-on-surface-variant leading-snug">{qf_diff_sub}</dt>
                    <dd class="font-semibold text-on-surface leading-snug">{qf_diff}</dd>
                </div>
                <div class="flex flex-col gap-1 border-l-2 border-sand pl-4">
                    <span class="material-symbols-outlined text-xl text-primary mb-1" aria-hidden="true">record_voice_over</span>
                    <dt class="order-last text-sm text-on-surface-variant leading-snug">{qf_guide_sub}</dt>
                    <dd class="font-semibold text-on-surface leading-snug">{qf_guide}</dd>
                </div>
                <div class="flex flex-col gap-1 border-l-2 border-sand pl-4">
                    <span class="material-symbols-outlined text-xl text-primary mb-1" aria-hidden="true">groups</span>
                    <dt class="order-last text-sm text-on-surface-variant leading-snug">{qf_group_sub}</dt>
                    <dd class="font-semibold text-on-surface leading-snug">{qf_group}</dd>
                </div>
                <div class="col-span-2 md:col-span-2 lg:col-span-1 flex flex-col gap-1 border-l-2 border-tertiary pl-4">
                    <span class="material-symbols-outlined text-xl text-tertiary mb-1" aria-hidden="true">sell</span>
                    <dt class="order-last text-sm text-on-surface-variant leading-snug">{price_sub_label}</dt>
                    <dd class="font-semibold text-tertiary text-lg leading-snug">{qf_price_badge}</dd>
                </div>
            </dl>
        </section>

        <!-- Detalles -->
        <section class="py-16 md:py-24 px-4 sm:px-8">
            <div class="max-w-[1336px] mx-auto grid grid-cols-1 lg:grid-cols-[1fr_400px] gap-16 xl:gap-24">

                <div class="flex flex-col gap-16 md:gap-20 min-w-0">

                    <!-- Descripción -->
                    <div>
                        <h2 class="font-display text-3xl sm:text-4xl text-primary leading-[1.08] mb-7">{details_label}</h2>
                        <div class="flex flex-col gap-5 text-lg text-on-surface-variant leading-relaxed max-w-[68ch]">
                            <p>{intro}</p>
                            <p>{intro_p2}</p>
                            <p>{intro_p3}</p>
                        </div>
                        <ul class="flex flex-wrap gap-x-7 gap-y-3 mt-8 text-sm font-semibold text-on-surface">
                            <li class="inline-flex items-center gap-2"><span class="material-symbols-outlined text-primary" aria-hidden="true">verified</span>{trust_badge_guide}</li>
                            <li class="inline-flex items-center gap-2"><span class="material-symbols-outlined text-primary" aria-hidden="true">event_available</span>{trust_badge_cancel}</li>
                            <li class="inline-flex items-center gap-2"><span class="material-symbols-outlined text-primary" aria-hidden="true">directions_bus</span>{trust_badge_bus}</li>
                        </ul>
                    </div>

                    <!-- Lo más destacado -->
                    <div>
                        <h2 class="font-display text-3xl sm:text-4xl text-primary leading-[1.08] mb-8">{why_title}</h2>
                        <ul class="grid grid-cols-1 md:grid-cols-2 gap-x-10 gap-y-8">
{why_items_html}
                        </ul>
                    </div>

                    <!-- Punto de encuentro -->
                    <div class="bg-surface-container rounded-sm p-7 sm:p-10">
                        <h2 class="font-display text-2xl text-primary leading-tight mb-5 flex items-center gap-3">
                            <span class="material-symbols-outlined text-3xl" aria-hidden="true">location_on</span>
                            {meeting_card_title}
                        </h2>
                        <div class="flex flex-col gap-4 text-on-surface-variant leading-relaxed max-w-[68ch]">
                            <p>{meeting_hotel_text}</p>
                            <p>{meeting_office_text}</p>
                        </div>
                        <div class="mt-7 border-l-2 border-tertiary pl-5">
                            <p class="font-semibold text-on-surface flex items-center gap-2 mb-1">
                                <span class="material-symbols-outlined text-tertiary" aria-hidden="true">departure_board</span>
                                {bus_connection_title}
                            </p>
                            <p class="text-sm text-on-surface-variant leading-relaxed max-w-[68ch]">{bus_connection_text}</p>
                        </div>
                    </div>

                    <!-- Qué llevar -->
                    <div>
                        <h2 class="font-display text-3xl sm:text-4xl text-primary leading-[1.08] mb-8">{what_to_bring_title}</h2>
                        <div class="grid grid-cols-1 sm:grid-cols-2 gap-x-10 gap-y-6">
{what_to_bring_html}
                        </div>
                    </div>

                    <!-- Opiniones -->
                    <div>
                        <h2 class="font-display text-3xl sm:text-4xl text-primary leading-[1.08] mb-8">{reviews_title}</h2>
                        <figure class="border-l-2 border-tertiary pl-6 md:pl-8">
                            <blockquote class="font-display text-xl md:text-2xl text-on-surface leading-snug">&ldquo;{featured_review_text}&rdquo;</blockquote>
                            <figcaption class="mt-5 flex flex-wrap items-center gap-x-3 gap-y-1 text-sm">
                                <span class="font-semibold text-primary text-base">{featured_review_author}</span>
                                <span class="inline-flex items-center gap-1 text-on-surface-variant"><span class="material-symbols-outlined text-base" aria-hidden="true">verified</span>{verified_booking_label}</span>
                                <span class="text-on-surface-variant">{featured_review_date}</span>
                            </figcaption>
                        </figure>
                    </div>

                    <!-- Preguntas frecuentes -->
{faq_section_html}

                </div>

                <!-- Reserva -->
                <aside>
                    <div class="lg:sticky lg:top-24 bg-surface-container-low border border-primary/10 rounded-sm p-7 sm:p-9 flex flex-col gap-7">

                        <div>
                            <p class="flex flex-wrap items-center justify-between gap-2 text-sm">
                                <span class="font-semibold text-primary">{sidebar_guarantee_badge}</span>
                                <span class="text-on-surface-variant">{sidebar_small_group_badge}</span>
                            </p>
                            {sidebar_price_block}
                            <p class="text-sm text-on-surface-variant mt-1">{per_person_no_fees_label}</p>
                        </div>

                        <div class="border-t border-primary/15 pt-6">
                            <h2 class="font-semibold text-on-surface mb-4">{whats_included_label}</h2>
                            <ul class="flex flex-col gap-3 text-[0.9375rem]">
{included_html}{excluded_html}
                            </ul>
                        </div>

                        <ul class="flex flex-col gap-2.5 text-sm border-t border-primary/15 pt-6">
                            <li class="flex items-start gap-2.5 text-on-surface"><span class="material-symbols-outlined text-lg text-primary" aria-hidden="true">event_available</span>{cancel_guarantee_text}</li>
                            <li class="flex items-start gap-2.5 text-on-surface"><span class="material-symbols-outlined text-lg text-primary" aria-hidden="true">cloud_sync</span>{weather_guarantee_text}</li>
                            <li class="flex items-start gap-2.5 text-on-surface-variant"><span class="material-symbols-outlined text-lg text-primary" aria-hidden="true">credit_card</span>{payment_methods_text}</li>
                        </ul>

                        <div>
                            <a href="https://api.whatsapp.com/send?phone=+51961542547&text={whatsapp_text}" target="_blank" rel="noopener" class="flex w-full items-center justify-center gap-2.5 bg-tertiary text-on-tertiary py-4 px-6 rounded-full text-lg font-semibold transition-colors hover:bg-tertiary-container active:scale-[0.98]">
                                {wa_icon}
                                <span>{sidebar_whatsapp_btn}</span>
                            </a>
                            <p class="text-sm text-on-surface-variant text-center mt-3">{instant_reply_subtext}</p>
                        </div>

                        <div class="border-t border-primary/15 pt-6 text-sm">
                            <p class="text-on-surface-variant mb-3">{alt_contacts_label}</p>
                            <div class="flex flex-wrap gap-x-6 gap-y-2">
                                <a href="mailto:reservas@solymarparacas.com?subject=Booking%20Inquiry:%20{mail_subject_encoded}&body={mail_body_encoded}" class="inline-flex items-center gap-1.5 font-semibold text-primary hover:underline">
                                    <span class="material-symbols-outlined text-lg" aria-hidden="true">mail</span>{email_btn_label}
                                </a>
                                <a href="https://instagram.com/solymarparacas" target="_blank" rel="noopener" class="inline-flex items-center gap-1.5 font-semibold text-primary hover:underline">
                                    <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 100 12.324 6.162 6.162 0 000-12.324zM12 16a4 4 0 110-8 4 4 0 010 8zm6.406-11.845a1.44 1.44 0 100 2.881 1.44 1.44 0 000-2.881z"/></svg>
                                    Instagram DM
                                </a>
                            </div>
                        </div>

                        <p class="text-sm border-t border-primary/15 pt-6">
                            <strong class="block font-semibold text-on-surface">{schedule_callout_main}</strong>
                            <span class="text-on-surface-variant">{schedule_label}</span>
                        </p>

                    </div>
                </aside>

            </div>
        </section>

        <!-- Por qué elegirnos -->
        <section class="py-16 md:py-24 px-4 sm:px-8 bg-surface-container">
            <div class="max-w-[1336px] mx-auto grid grid-cols-1 gap-12 lg:grid-cols-12 lg:gap-16">
                <h2 class="lg:col-span-4 font-display text-3xl sm:text-4xl text-primary leading-[1.08] text-balance">{why_choose_us_label}</h2>
                <ul class="lg:col-span-8 grid grid-cols-1 sm:grid-cols-2 gap-x-10 gap-y-8">
                    <li class="flex gap-4 pt-5 border-t border-primary/20">
                        <span class="material-symbols-outlined text-3xl text-primary shrink-0" aria-hidden="true">shield</span>
                        <div><h3 class="font-display text-lg text-primary mb-1">{val_prop_1_title}</h3><p class="text-on-surface-variant leading-relaxed">{val_prop_1_desc}</p></div>
                    </li>
                    <li class="flex gap-4 pt-5 border-t border-primary/20">
                        <span class="material-symbols-outlined text-3xl text-primary shrink-0" aria-hidden="true">record_voice_over</span>
                        <div><h3 class="font-display text-lg text-primary mb-1">{val_prop_2_title}</h3><p class="text-on-surface-variant leading-relaxed">{val_prop_2_desc}</p></div>
                    </li>
                    <li class="flex gap-4 pt-5 border-t border-primary/20">
                        <span class="material-symbols-outlined text-3xl text-primary shrink-0" aria-hidden="true">workspace_premium</span>
                        <div><h3 class="font-display text-lg text-primary mb-1">{val_prop_3_title}</h3><p class="text-on-surface-variant leading-relaxed">{val_prop_3_desc}</p></div>
                    </li>
                    <li class="flex gap-4 pt-5 border-t border-primary/20">
                        <span class="material-symbols-outlined text-3xl text-primary shrink-0" aria-hidden="true">verified_user</span>
                        <div><h3 class="font-display text-lg text-primary mb-1">{val_prop_4_title}</h3><p class="text-on-surface-variant leading-relaxed">{val_prop_4_desc}</p></div>
                    </li>
                </ul>
            </div>
        </section>

        <!-- Reserva final -->
        <section class="relative overflow-hidden py-20 md:py-28 px-4 sm:px-8 bg-deep text-white">
            {candelabro}
            <div class="relative max-w-[1336px] mx-auto">
                <div class="max-w-[680px]">
                    <p class="text-sand font-semibold mb-4">{cta_kicker}</p>
                    <h2 class="font-display text-4xl md:text-5xl leading-[1.04] mb-6 text-balance">{cta_title}</h2>
                    <p class="text-lg md:text-xl text-white/80 leading-relaxed mb-10 max-w-[52ch]">{cta_desc}</p>
                    <div class="flex flex-col sm:flex-row sm:items-center gap-4 sm:gap-6">
                        <a href="https://api.whatsapp.com/send?phone=+51961542547&text={whatsapp_text}" target="_blank" rel="noopener" class="inline-flex items-center justify-center gap-2.5 bg-tertiary text-on-tertiary py-3.5 px-7 rounded-full font-semibold whitespace-nowrap transition-colors hover:bg-tertiary-container active:scale-[0.98]">
                            {wa_icon}
                            <span>{cta_button_label}</span>
                        </a>
                        <a href="mailto:reservas@solymarparacas.com?subject=Booking%20Inquiry:%20{mail_subject_encoded}&body={mail_body_encoded}" class="inline-flex items-center justify-center gap-2 py-3.5 px-7 rounded-full border border-white/40 font-semibold text-white transition-colors hover:bg-white/10">
                            <span class="material-symbols-outlined text-lg" aria-hidden="true">mail</span>
                            <span>{email_btn_label}</span>
                        </a>
                    </div>
                    <p class="text-sm text-white/65 mt-8">{cta_guarantee_footer}</p>
                </div>
            </div>
        </section>
    </main>

    <!-- Reserva fija en móvil -->
    <div id="mobile-book-bar" class="fixed inset-x-0 bottom-0 z-[900] lg:hidden flex items-center justify-between gap-4 bg-surface/95 backdrop-blur-md border-t border-primary/15 px-4 pt-3 pb-[max(0.75rem,env(safe-area-inset-bottom))]">
        <div class="min-w-0">
            <p class="text-xs text-on-surface-variant truncate">{price_sub_label}</p>
            <p class="font-display text-lg text-tertiary leading-tight whitespace-nowrap">{bar_price}</p>
        </div>
        <a href="https://api.whatsapp.com/send?phone=+51961542547&text={whatsapp_text}" target="_blank" rel="noopener" class="shrink-0 inline-flex items-center gap-2 bg-tertiary text-on-tertiary py-3 px-5 rounded-full text-sm font-semibold whitespace-nowrap active:scale-[0.98]">
            {wa_icon}
            <span>{sidebar_whatsapp_btn}</span>
        </a>
    </div>

    <footer class="footer"></footer>

    <script src="{root_prefix}js/header.js"></script>
    <script src="{root_prefix}js/footer.js"></script>
</body>

</html>
"""

# ==========================================
# COMMON DICTIONARY
# ==========================================

common = {
    "es": {
        "home_label": "Inicio",
        "home_url": "https://solymarparacas.com/",
        "tours_index_label": "Tours",
        "tours_index_url": "https://solymarparacas.com/tours",
        "home_link": "./",
        "tours_link": "tours",
        "details_label": "Detalles de la experiencia",
        "book_card_title": "Reservar tour",
        "price_sub_label": "Por persona",
        "per_person_no_fees_label": "Por persona · Sin cargos ocultos",
        "whats_included_label": "Qué incluye",
        "sidebar_guarantee_badge": "Salida diaria garantizada",
        "sidebar_small_group_badge": "Grupo reducido",
        "sidebar_whatsapp_btn": "Reservar por WhatsApp",
        "instant_reply_subtext": "Respuesta inmediata y confirmación de fecha",
        "alt_contacts_label": "¿No usas WhatsApp? Escríbenos aquí",
        "email_btn_label": "Enviar email",
        "schedule_callout_main": "Horario de salida",
        "cancel_guarantee_text": "Cancelación gratuita hasta 24h antes",
        "weather_guarantee_text": "Reembolso 100% si se cancela por clima",
        "payment_methods_text": "Paga con tarjeta por link seguro o efectivo",
        "trust_badge_guide": "Guías locales certificados",
        "trust_badge_cancel": "Cancelación flexible 24h",
        "trust_badge_bus": "Regreso a tiempo para buses nocturnos",
        "meeting_card_title": "Punto de encuentro y conexión de buses",
        "meeting_hotel_text": "<strong>Recojo gratuito en hotel:</strong> Te recogemos directamente en tu hotel u hostal en Paracas / El Chaco.",
        "meeting_office_text": "<strong>Oficina central:</strong> Si te hospedas fuera del centro o llegas con maletas antes del tour, te esperamos en nuestra oficina en el malecón El Chaco: <a href='https://maps.google.com/?q=SolyMar+Paracas+Peru' target='_blank' rel='noopener' class='font-bold text-primary hover:underline ml-1'>SolyMar Paracas (Google Maps)</a>",
        "bus_connection_title": "¿Tomas un bus nocturno esa misma noche?",
        "bus_connection_text": "Nuestros horarios están planificados para que regreses al pueblo con tiempo de sobra para cenar o abordar tu bus nocturno a Lima, Huacachina o Arequipa (Cruz del Sur, Peru Hop). ¡Puedes dejar tu equipaje en custodia gratuita en nuestra oficina!",
        "what_to_bring_title": "Qué llevar",
        "reviews_title": "La experiencia de nuestros clientes",
        "verified_booking_label": "Reserva verificada",
        "featured_review_text": "Excelente servicio de inicio a fin. Todo muy puntual, el guía fue súper atento y las vistas son increíbles. 100% recomendados en Paracas.",
        "featured_review_author": "Carlos Rodríguez",
        "featured_review_date": "Reseña reciente",
        "why_choose_us_label": "Por qué elegir SolyMar Paracas",
        "val_prop_1_title": "Seguridad garantizada",
        "val_prop_1_desc": "Equipos modernos, chalecos homologados y seguros de pasajeros para tu total tranquilidad.",
        "val_prop_2_title": "Guías locales expertos",
        "val_prop_2_desc": "Guías bilingües certificados apasionados por la fauna marina, el desierto y la historia.",
        "val_prop_3_title": "Operador formal autorizado",
        "val_prop_3_desc": "Agencia de viajes registrada ante MINCETUR y autoridades locales del Perú.",
        "val_prop_4_title": "Garantías flexibles",
        "val_prop_4_desc": "Cancela gratis hasta 24h antes o recibe 100% de reembolso si el clima impide la salida.",
        "cta_kicker": "Cupos limitados por turno",
        "cta_title": "¿Listo para comenzar tu aventura en Paracas?",
        "cta_desc": "Escríbenos hoy mismo para asegurar tus espacios. Coordinamos tu reserva en minutos con total flexibilidad.",
        "cta_button_label": "Reservar por WhatsApp",
        "cta_guarantee_footer": "Paga con tarjeta mediante enlace seguro o en efectivo al llegar · Cancelación sin costo hasta 24h antes",
        "locale": "es_PE"
    },
    "en": {
        "home_label": "Home",
        "home_url": "https://solymarparacas.com/en/",
        "tours_index_label": "Tours",
        "tours_index_url": "https://solymarparacas.com/en/tours",
        "home_link": "./",
        "tours_link": "tours",
        "details_label": "Adventure details",
        "book_card_title": "Book tour",
        "price_sub_label": "Per person",
        "per_person_no_fees_label": "Per person · No hidden booking fees",
        "whats_included_label": "What's included",
        "sidebar_guarantee_badge": "Guaranteed daily departure",
        "sidebar_small_group_badge": "Small group",
        "sidebar_whatsapp_btn": "Book on WhatsApp",
        "instant_reply_subtext": "Instant reply & date confirmation in English",
        "alt_contacts_label": "Don't use WhatsApp? Reach out here",
        "email_btn_label": "Send email",
        "schedule_callout_main": "Departure schedule",
        "cancel_guarantee_text": "Free cancellation up to 24h before",
        "weather_guarantee_text": "100% full refund if canceled due to weather",
        "payment_methods_text": "Pay by card via secure link or cash on arrival",
        "trust_badge_guide": "Certified bilingual guides",
        "trust_badge_cancel": "Free 24h cancellation",
        "trust_badge_bus": "Back in time for evening night buses",
        "meeting_card_title": "Meeting point & bus connections",
        "meeting_hotel_text": "<strong>Free hotel pick-up:</strong> Complimentary pick-up from any hotel, hostel, or Airbnb in Paracas town / El Chaco area.",
        "meeting_office_text": "<strong>Central meeting office:</strong> If you are staying outside the center or arriving with luggage before the tour, meet us at our boardwalk office: <a href='https://maps.google.com/?q=SolyMar+Paracas+Peru' target='_blank' rel='noopener' class='font-bold text-primary hover:underline ml-1'>SolyMar Paracas (Google Maps)</a>",
        "bus_connection_title": "Catching an evening night bus?",
        "bus_connection_text": "All our day and afternoon tours are timed so you return with plenty of time for dinner or to catch your evening night bus (Cruz del Sur, Peru Hop) to Lima, Huacachina, or Arequipa. Free luggage storage is available at our office!",
        "what_to_bring_title": "What to bring",
        "reviews_title": "Loved by travelers worldwide",
        "verified_booking_label": "Verified booking",
        "featured_review_text": "Incredible experience with SolyMar! Booking was super easy, guides spoke great English, and the scenery was breathtaking. The best operator in Paracas!",
        "featured_review_author": "Sarah Johnson, USA",
        "featured_review_date": "Recent review",
        "why_choose_us_label": "Why book with SolyMar Paracas",
        "val_prop_1_title": "Safety first",
        "val_prop_1_desc": "Modern equipment, certified guides, and complete passenger insurance for total peace of mind.",
        "val_prop_2_title": "Expert local guides",
        "val_prop_2_desc": "Friendly bilingual guides sharing historical facts, desert geology, and spotting hidden wildlife.",
        "val_prop_3_title": "Licensed operator",
        "val_prop_3_desc": "We are a formal registered tour operator recognized by Peruvian tourism authorities (MINCETUR).",
        "val_prop_4_title": "Flexible guarantees",
        "val_prop_4_desc": "Free cancellation up to 24h before or receive a 100% full refund if weather prevents departure.",
        "cta_kicker": "Limited spots per departure",
        "cta_title": "Ready to start your Paracas adventure?",
        "cta_desc": "Get in touch with us today to secure your seats. We confirm your booking in minutes with flexible options!",
        "cta_button_label": "Book on WhatsApp",
        "cta_guarantee_footer": "Pay by card via secure payment link or cash on arrival · Free cancellation up to 24h before",
        "locale": "en_US"
    }
}

# ==========================================
# GENERATE INDIVIDUAL TOUR PAGES
# ==========================================

import urllib.parse
import json
import os

for tour_key, tour_info in tours_formatted.items():
    cat = tour_info["category"]
    price_usd = PRICE_USD_MAP.get(tour_key, "")
    
    for lang in ["es", "en"]:
        root_prefix = "../" if lang == "en" else ""
        content = tour_info[lang]
        comm = common[lang]
        
        
        # Build Why Items HTML
        why_items_html = ""
        for item in content["why_items"]:
            why_items_html += f"""                            <li class="flex gap-4 pt-5 border-t border-primary/15">
                                <span class="material-symbols-outlined text-3xl text-primary shrink-0" aria-hidden="true">{item['icon']}</span>
                                <div>
                                    <h3 class="font-display text-lg text-primary leading-snug mb-1">{item['title']}</h3>
                                    <p class="text-on-surface-variant leading-relaxed">{item['desc']}</p>
                                </div>
                            </li>
"""
        
        # Build Included HTML
        included_html = ""
        for inc in content["included"]:
            included_html += f"""                                <li class="flex items-start gap-2.5 text-on-surface">
                                    <span class="material-symbols-outlined text-lg text-primary shrink-0" aria-hidden="true">check</span>
                                    <span>{inc}</span>
                                </li>
"""
        
        # Build Excluded HTML
        excluded_html = ""
        for exc in content["excluded"]:
            excluded_html += f"""                                <li class="flex items-start gap-2.5 text-on-surface-variant">
                                    <span class="material-symbols-outlined text-lg text-tertiary shrink-0" aria-hidden="true">info</span>
                                    <span>{exc}</span>
                                </li>
"""
        
        # What to bring HTML
        bring_items = WHAT_TO_BRING.get(cat, WHAT_TO_BRING["desierto"])[lang]
        what_to_bring_html = ""
        for b_icon, b_title, b_desc in bring_items:
            what_to_bring_html += f"""                            <div class="flex items-start gap-4">
                                <span class="material-symbols-outlined text-2xl text-primary shrink-0" aria-hidden="true">{b_icon}</span>
                                <div>
                                    <h3 class="font-semibold text-on-surface mb-0.5">{b_title}</h3>
                                    <p class="text-sm text-on-surface-variant leading-relaxed">{b_desc}</p>
                                </div>
                            </div>
"""
        
        # Build FAQs HTML
        faq_section_html = ""
        faq_schema = ""
        if "faqs" in content:
            faq_section_html = f"""                    <div>
                        <h2 class="font-display text-3xl sm:text-4xl text-primary leading-[1.08] mb-6">{content['faq_title']}</h2>
                        <div class="border-t-2 border-sand">"""
            
            faq_schema_items = []
            for faq in content["faqs"]:
                faq_section_html += f"""
                            <details class="group border-b border-primary/15">
                                <summary class="flex items-center justify-between gap-6 py-5 cursor-pointer list-none">
                                    <h3 class="text-base md:text-lg font-semibold text-on-surface group-open:text-primary">{faq['q']}</h3>
                                    <span class="material-symbols-outlined text-primary shrink-0 transition-transform duration-300 group-open:rotate-45" aria-hidden="true">add</span>
                                </summary>
                                <p class="pb-6 pr-8 text-on-surface-variant leading-relaxed max-w-[68ch]">{faq['a']}</p>
                            </details>"""
                
                # Build FAQ JSON-LD schema
                faq_schema_items.append(f"""      {{
        "@type": "Question",
        "name": {json.dumps(faq['q'])},
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": {json.dumps(faq['a'])}
        }}
      }}""")
            
            faq_section_html += """
                        </div>
                    </div>"""
            
            if faq_schema_items:
                faq_schema = """,
      {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
    """ + ",\n".join(faq_schema_items) + """
        ]
      }"""
        
        # WhatsApp prefilled text
        if lang == "en":
            wa_text = f"Hi! I'd like to book the {content['h1']}. Date: ___ · People: ___"
        else:
            wa_text = f"Hola! Quiero reservar el tour {content['h1']}. Fecha: ___ · Personas: ___"
        whatsapp_text_encoded = urllib.parse.quote(wa_text)
        
        # Mail prefilled
        mail_subj = f"Booking Inquiry: {content['h1']}"
        mail_body = f"Hi SolyMar Paracas!\\n\\nI would like to book: {content['h1']}\\nDate:\\nNumber of people:\\nHotel in Paracas:\\nQuestions:"
        mail_subj_enc = urllib.parse.quote(mail_subj)
        mail_body_enc = urllib.parse.quote(mail_body)
        
        # Clean canonical URL
        clean_filename = tour_info['filename'].removesuffix('.html')
        canonical_es = f"https://solymarparacas.com/{clean_filename}"
        canonical_en = f"https://solymarparacas.com/en/{clean_filename}"
        canonical = canonical_en if lang == "en" else canonical_es
        
        # Quick facts data
        qf_data = QUICK_FACTS.get(tour_key, {}).get(lang, {
            "sched": "Daily / Diarias", "sched_sub": "Check schedule",
            "dur": "2-3 Hours", "dur_sub": "Guided tour",
            "type": "Paracas Tour", "type_sub": "Nature & Adventure",
            "diff": "Easy", "diff_sub": "All levels",
            "guide": "Certified Guide", "guide_sub": "Bilingual pro",
            "group": "Small Group", "group_sub": "Personalized care"
        })
        
        # Pricing logic
        if tour_info.get("quote_only"):
            price_display = "Cotizar" if lang == "es" else "Get a Quote"
            price_sub = "Tarifa por vehículo, según ruta" if lang == "es" else "Per vehicle, based on route"
            sidebar_price_block = f'<p class="font-display text-4xl text-tertiary mt-3">{price_display}</p>'
            qf_price_badge = price_display
            offers_json = ""
        else:
            price_display = tour_info["price"]
            price_sub = content.get("price_sub_label", comm["price_sub_label"])
            usd_str = f" ({price_usd})" if price_usd else ""
            sidebar_price_block = f'''<p class="flex flex-wrap items-baseline gap-x-2 mt-3">
                                <span class="font-display text-5xl text-tertiary">{price_display}</span>
                                <span class="text-xl text-on-surface-variant">{usd_str}</span>
                            </p>'''
            qf_price_badge = f"{price_display}{usd_str}"
            offers_json = f'''"offers": {{
          "@type": "Offer",
          "price": "{tour_info['price_val']}",
          "priceCurrency": "{tour_info['price_cur']}",
          "priceValidUntil": "2026-12-31",
          "availability": "https://schema.org/InStock",
          "url": "{canonical}"
        }},
        '''
        
        # Review personalization (Sarah for trekking, Carlos for others)
        if tour_key == "trekking":
            rev_text = "The Golden Shadows Trek was the absolute highlight of my trip to Peru! Watching the sun set over the wild desert cliffs of Paracas with the ocean crashing below was breathtaking. Our guide spoke fluent English, knew the best photo angles, and made sure our small group was comfortable the entire way." if lang == "en" else "El Golden Shadows Trek fue lo más inolvidable de mi viaje a Paracas. Caminar por los acantilados viendo caer el sol sobre el mar dorado es una experiencia mágica. El guía nos tomó fotos increíbles y el ritmo fue perfecto."
            rev_author = "Sarah Johnson, Chicago, USA" if lang == "en" else "Sarah Johnson (EE. UU.)"
        else:
            rev_text = comm["featured_review_text"]
            rev_author = comm["featured_review_author"]
        
        # Render page
        rendered_html = template.format(
            lang=lang,
            root_prefix=root_prefix,
            title=content["title"],
            desc=content["desc"],
            canonical=canonical,
            canonical_es=canonical_es,
            canonical_en=canonical_en,
            locale=comm["locale"],
            h1=content["h1"],
            json_h1=json.dumps(content["h1"]),
            json_desc=json.dumps(content["desc"]),
            breadcrumb_title=content["h1"],
            image=tour_info["image"],
            subtitle=content["subtitle"],
            home_label=comm["home_label"],
            home_url=comm["home_url"],
            tours_index_label=comm["tours_index_label"],
            tours_index_url=comm["tours_index_url"],
            home_link=comm["home_link"],
            tours_link=comm["tours_link"],
            qf_sched=qf_data["sched"],
            qf_sched_sub=qf_data["sched_sub"],
            qf_dur=qf_data["dur"],
            qf_dur_sub=qf_data["dur_sub"],
            qf_type=qf_data["type"],
            qf_type_sub=qf_data["type_sub"],
            qf_diff=qf_data["diff"],
            qf_diff_sub=qf_data["diff_sub"],
            qf_guide=qf_data["guide"],
            qf_guide_sub=qf_data["guide_sub"],
            qf_group=qf_data["group"],
            qf_group_sub=qf_data["group_sub"],
            qf_price_badge=qf_price_badge,
            details_label=comm["details_label"],
            intro=content["intro"],
            intro_p2=content["intro_p2"],
            intro_p3=content["intro_p3"],
            trust_badge_guide=comm["trust_badge_guide"],
            trust_badge_cancel=comm["trust_badge_cancel"],
            trust_badge_bus=comm["trust_badge_bus"],
            why_title=content["why_title"],
            why_items_html=why_items_html,
            meeting_card_title=comm["meeting_card_title"],
            meeting_hotel_text=comm["meeting_hotel_text"],
            meeting_office_text=comm["meeting_office_text"],
            bus_connection_title=comm["bus_connection_title"],
            bus_connection_text=comm["bus_connection_text"],
            what_to_bring_title=comm["what_to_bring_title"],
            what_to_bring_html=what_to_bring_html,
            reviews_title=comm["reviews_title"],
            verified_booking_label=comm["verified_booking_label"],
            featured_review_text=rev_text,
            featured_review_author=rev_author,
            featured_review_date=comm["featured_review_date"],
            faq_section_html=faq_section_html,
            book_card_title=comm["book_card_title"],
            sidebar_guarantee_badge=comm["sidebar_guarantee_badge"],
            sidebar_small_group_badge=comm["sidebar_small_group_badge"],
            sidebar_price_block=sidebar_price_block,
            per_person_no_fees_label=comm["per_person_no_fees_label"],
            whats_included_label=comm["whats_included_label"],
            price_sub_label=price_sub,
            included_html=included_html,
            excluded_html=excluded_html,
            cancel_guarantee_text=comm["cancel_guarantee_text"],
            weather_guarantee_text=comm["weather_guarantee_text"],
            payment_methods_text=comm["payment_methods_text"],
            whatsapp_text=whatsapp_text_encoded,
            sidebar_whatsapp_btn=comm["sidebar_whatsapp_btn"],
            instant_reply_subtext=comm["instant_reply_subtext"],
            alt_contacts_label=comm["alt_contacts_label"],
            mail_subject_encoded=mail_subj_enc,
            mail_body_encoded=mail_body_enc,
            email_btn_label=comm["email_btn_label"],
            schedule_callout_main=comm["schedule_callout_main"],
            schedule_label=content["schedule_label"],
            why_choose_us_label=comm["why_choose_us_label"],
            val_prop_1_title=comm["val_prop_1_title"],
            val_prop_1_desc=comm["val_prop_1_desc"],
            val_prop_2_title=comm["val_prop_2_title"],
            val_prop_2_desc=comm["val_prop_2_desc"],
            val_prop_3_title=comm["val_prop_3_title"],
            val_prop_3_desc=comm["val_prop_3_desc"],
            val_prop_4_title=comm["val_prop_4_title"],
            val_prop_4_desc=comm["val_prop_4_desc"],
            cta_kicker=comm["cta_kicker"],
            cta_title=comm["cta_title"],
            cta_desc=comm["cta_desc"],
            cta_button_label=comm["cta_button_label"],
            cta_guarantee_footer=comm["cta_guarantee_footer"],
            offers_json=offers_json,
            wa_icon=WA_ICON,
            candelabro=CANDELABRO,
            hero_img_attrs=img_attrs(root_prefix, tour_info["image"], "100vw"),
            bar_price=price_display,
            hero_preload=img_preload(root_prefix, tour_info["image"]),
            faq_schema=faq_schema
        )
        
        # Write output file
        out_dir = "en" if lang == "en" else "."
        out_path = os.path.join(out_dir, tour_info["filename"])
        os.makedirs(out_dir, exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(rendered_html)
        print(f"Generated: {out_path}")

print("Successfully generated all enhanced individual tour pages.")

# ==========================================
# MASTER HTML TEMPLATE FOR TOURS INDEX
# ==========================================

index_template = """<!DOCTYPE html>
<html lang="{lang}">

<head>
    <meta charset="utf-8" />
    <link rel="icon" type="image/webp" href="{root_prefix}img/SolyMar-ico.webp" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <!-- ===== SEO: META TITLE & DESCRIPTION ===== -->
    <title>{title}</title>
    <meta name="description" content="{desc}">
    <meta name="robots" content="index, follow">
    <meta name="author" content="SolyMar Paracas">
    <link rel="canonical" href="{canonical}">
    <link rel="alternate" hreflang="es" href="{canonical_es}">
    <link rel="alternate" hreflang="en" href="{canonical_en}">
    <link rel="alternate" hreflang="x-default" href="{canonical_es}">

    <!-- ===== OPEN GRAPH ===== -->
    <meta property="og:type" content="website">
    <meta property="og:url" content="{canonical}">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{desc}">
    <meta property="og:image" content="https://solymarparacas.com/img/og-solymar-paracas.jpg">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">
    <meta property="og:locale" content="{locale}">
    <meta property="og:site_name" content="SolyMar Paracas">

    <!-- ===== TWITTER CARD ===== -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{title}">
    <meta name="twitter:description" content="{desc}">
    <meta name="twitter:image" content="https://solymarparacas.com/img/og-solymar-paracas.jpg">
    <!-- ===== FIN SEO ===== -->
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,400..800&display=swap" rel="stylesheet" />
    <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0,0&icon_names=access_time,account_circle,add,air,airport_shuttle,architecture,arrow_downward,arrow_forward,attractions,auto_awesome,badge,battery_charging_full,call,check,checkroom,cloud_sync,coffee,credit_card,departure_board,directions_boat,directions_bus,directions_car,directions_walk,domain,egg,event_available,expand_more,explore,flutter_dash,group,groups,health_and_safety,hiking,history_edu,info,landscape,local_activity,local_bar,local_shipping,location_on,mail,map,medication,museum,payments,pets,photo_camera,pool,record_voice_over,restaurant,restaurant_menu,route,rowing,schedule,security,sell,shield,speed,sports_motorsports,sports_skateboarding,surfing,terrain,timelapse,toys,verified,verified_user,video_camera_back,visibility,water,water_drop,water_slide,wb_sunny,wb_twilight,wind_power,wine_bar,workspace_premium&display=block" rel="stylesheet" />
    <link rel="stylesheet" href="{root_prefix}css/style.css" />
    {hero_preload}

    <!-- ===== ESTRUCTURA DE DATOS (JSON-LD) PARA GOOGLE ===== -->
    <script type="application/ld+json">
    [
      {{
        "@context": "https://schema.org",
        "@type": "ItemList",
        "name": {json_h1},
        "description": {json_desc},
        "url": "{canonical}",
        "numberOfItems": {num_items},
        "itemListElement": [
          {item_list_elements}
        ]
      }},
      {{
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
          {{
            "@type": "ListItem",
            "position": 1,
            "name": "{home_label}",
            "item": "{home_url}"
          }},
          {{
            "@type": "ListItem",
            "position": 2,
            "name": "{tours_index_label}",
            "item": "{canonical}"
          }}
        ]
      }}
    ]
    </script>
</head>

<body class="font-sans bg-surface text-on-surface leading-relaxed antialiased overflow-x-hidden pt-16">
    <nav id="header-placeholder"></nav>

    <main>
        <!-- Hero -->
        <section class="relative min-h-[min(56dvh,560px)] flex items-end overflow-hidden bg-deep">
            <img class="absolute inset-0 w-full h-full object-cover" {hero_img_attrs} alt="{h1}" fetchpriority="high" decoding="async" />
            <div class="absolute inset-0 bg-gradient-to-r from-deep/90 via-deep/60 to-deep/15"></div>
            <div class="absolute inset-x-0 bottom-0 h-2/3 bg-gradient-to-t from-deep/80 to-transparent"></div>
            <div class="relative w-full max-w-[1400px] mx-auto px-4 sm:px-8 pt-20 pb-14 md:pb-20">
                <div class="max-w-[860px] text-white">
                    <nav aria-label="Breadcrumb" class="rise-in text-sm text-white/75 mb-5">
                        <a href="{home_link}" class="hover:text-white hover:underline">{home_label}</a>
                        <span class="mx-2 text-sand" aria-hidden="true">/</span>
                        <span aria-current="page">{tours_index_label}</span>
                    </nav>
                    <h1 class="rise-in [--i:1] font-display text-4xl sm:text-5xl lg:text-6xl leading-[1.04] mb-6 text-balance">{h1}</h1>
                    <p class="rise-in [--i:2] text-lg md:text-xl text-white/85 leading-relaxed max-w-[52ch]">{subtitle}</p>
                </div>
            </div>
        </section>

        <!-- Tours -->
        <section class="py-16 md:py-24 px-4 sm:px-8">
            <div class="max-w-[1336px] mx-auto grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-x-8 gap-y-14">
{grid_html}
            </div>
        </section>

        <!-- Ayuda -->
        <section class="relative overflow-hidden py-20 md:py-28 px-4 sm:px-8 bg-deep text-white">
            {candelabro}
            <div class="relative max-w-[1336px] mx-auto">
                <div class="max-w-[680px]">
                    <h2 class="font-display text-4xl md:text-5xl leading-[1.04] mb-6 text-balance">{cta_title}</h2>
                    <p class="text-lg md:text-xl text-white/80 leading-relaxed mb-10 max-w-[52ch]">{cta_desc}</p>
                    <a href="https://api.whatsapp.com/send?phone=+51961542547&text={whatsapp_text}" target="_blank" rel="noopener" class="inline-flex items-center justify-center gap-2.5 bg-tertiary text-on-tertiary py-3.5 px-7 rounded-full font-semibold whitespace-nowrap transition-colors hover:bg-tertiary-container active:scale-[0.98]">
                        {wa_icon}
                        <span>{cta_button_label}</span>
                    </a>
                </div>
            </div>
        </section>
    </main>

    <footer class="footer"></footer>

    <script src="{root_prefix}js/header.js"></script>
    <script src="{root_prefix}js/footer.js"></script>
</body>

</html>
"""

tours_index_texts = {
    "es": {
        "title": "Tours en Paracas e Ica 2026: Precios y Reservas | Solymar Paracas",
        "desc": "Todos nuestros tours en Paracas, Pisco e Ica: Islas Ballestas, Reserva Nacional, buggies en Huacachina, buceo, parapente y traslados privados. Reserva online.",
        "h1": "Todos nuestros tours en Paracas, Pisco e Ica",
        "subtitle": "Somos SolyMar Paracas, tu agencia local de confianza. Disfruta del mar, desierto, aire y cultura con total seguridad.",
        "from_label": "Desde",
        "view_details_label": "Ver Detalles",
        "cta_title": "¿No sabes cuál elegir?",
        "cta_desc": "Escríbenos por WhatsApp y te ayudamos a diseñar un itinerario a tu medida en Paracas y los principales destinos de Ica.",
        "cta_button_label": "Escríbenos por WhatsApp",
        "whatsapp_text": "Hola!%20Quiero%20ayuda%20para%20armar%20mi%20itinerario%20de%20tours"
    },
    "en": {
        "title": "Tours in Paracas & Ica 2026: Price & Booking | Solymar Paracas",
        "desc": "Browse all our tours in Paracas, Pisco, and Ica: Ballestas Islands, National Reserve, Huacachina dune buggies, scuba diving, paragliding, and private transfers. Book online.",
        "h1": "All Our Tours in Paracas, Pisco & Ica",
        "subtitle": "We are SolyMar Paracas, your trusted local agency. Discover ocean, desert, air, and history with full safety.",
        "from_label": "From",
        "view_details_label": "View Details",
        "cta_title": "Unsure which tour to pick?",
        "cta_desc": "Message us on WhatsApp. Our local experts will help you design a customized itinerary for your trip to Paracas and Ica.",
        "cta_button_label": "Chat with us on WhatsApp",
        "whatsapp_text": "Hi!%20I'd%20like%20help%20planning%20my%20tours%20itinerary%20in%20Paracas"
    }
}

# Generate tours.html and en/tours.html
for lang in ["es", "en"]:
    root_prefix = "../" if lang == "en" else ""
    comm = common[lang]
    texts = tours_index_texts[lang]
    
    
    cat_labels = {
        "es": {
            "mar": "Aventura Marina",
            "desierto": "Desierto",
            "aire": "Actividad Aérea",
            "cultura": "Cultura e Historia",
            "traslados": "Traslados Privados"
        },
        "en": {
            "mar": "Marine Adventure",
            "desierto": "Desert",
            "aire": "Aerial Activity",
            "cultura": "Culture & History",
            "traslados": "Private Transfers"
        }
    }
    
    cat_order = {"mar": 0, "desierto": 1, "aire": 2, "cultura": 3, "traslados": 4}
    sorted_tours = sorted(tours_formatted.items(), key=lambda x: cat_order.get(x[1]["category"], 99))
    
    grid_html = ""
    item_list_elements = []
    position = 1
    
    for tour_key, tour_info in sorted_tours:
        tour_content = tour_info[lang]
        cat = tour_info["category"]
        p_usd = PRICE_USD_MAP.get(tour_key, "")
        
        cat_label = cat_labels[lang].get(cat, cat.capitalize())
        
        if tour_info.get("quote_only"):
            price_badge = "Cotizar" if lang == "es" else "Get a Quote"
        else:
            usd_note = f" ({p_usd})" if p_usd else ""
            price_badge = f"{texts['from_label']} {tour_info['price']}{usd_note}"
        
        card_html = f"""                <a href="{tour_info['filename'].removesuffix('.html')}" class="group flex flex-col gap-4">
                    <div class="h-60 md:h-64 overflow-hidden rounded-sm bg-surface-container">
                        <img class="w-full h-full object-cover transition-transform duration-700 ease-out-soft group-hover:scale-[1.03]" {img_attrs(root_prefix, tour_info['image'], "(min-width: 1024px) 33vw, (min-width: 768px) 50vw, 100vw")} alt="{tour_content['h1']}" loading="lazy" decoding="async" />
                    </div>
                    <div class="flex flex-col gap-2 flex-1">
                        <span class="text-sm text-on-surface-variant">{cat_label}</span>
                        <h2 class="font-display text-xl text-primary leading-tight group-hover:underline decoration-sand decoration-2 underline-offset-4">{tour_content['h1']}</h2>
                        <p class="text-[0.9375rem] text-on-surface-variant leading-relaxed line-clamp-3">{tour_content['desc']}</p>
                        <p class="font-semibold text-tertiary mt-auto pt-1">{price_badge}</p>
                    </div>
                </a>
"""
        grid_html += card_html
        
        clean_filename = tour_info['filename'].removesuffix('.html')
        tour_url = f"https://solymarparacas.com/en/{clean_filename}" if lang == "en" else f"https://solymarparacas.com/{clean_filename}"
        item_list_elements.append(f"""          {{
            "@type": "ListItem",
            "position": {position},
            "name": {json.dumps(tour_content['h1'])},
            "url": "{tour_url}"
          }}""")
        position += 1
    
    canonical_es = "https://solymarparacas.com/tours"
    canonical_en = "https://solymarparacas.com/en/tours"
    canonical = canonical_en if lang == "en" else canonical_es
    
    rendered_index = index_template.format(
        lang=lang,
        root_prefix=root_prefix,
        title=texts["title"],
        desc=texts["desc"],
        canonical=canonical,
        canonical_es=canonical_es,
        canonical_en=canonical_en,
        locale=comm["locale"],
        h1=texts["h1"],
        json_h1=json.dumps(texts["h1"]),
        json_desc=json.dumps(texts["desc"]),
        subtitle=texts["subtitle"],
        home_label=comm["home_label"],
        home_url=comm["home_url"],
        tours_index_label=comm["tours_index_label"],
        home_link=comm["home_link"],
        num_items=len(tours_formatted),
        item_list_elements=",\n".join(item_list_elements),
        grid_html=grid_html,
        cta_title=texts["cta_title"],
        cta_desc=texts["cta_desc"],
        whatsapp_text=texts["whatsapp_text"],
        cta_button_label=texts["cta_button_label"],
        wa_icon=WA_ICON,
        candelabro=CANDELABRO,
        hero_img_attrs=img_attrs(root_prefix, "img/reserva-nacional-paracas.jpg", "100vw"),
        hero_preload=img_preload(root_prefix, "img/reserva-nacional-paracas.jpg")
    )
    
    out_dir = "en" if lang == "en" else "."
    out_path = os.path.join(out_dir, "tours.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(rendered_index)
    print(f"Generated Tours Index: {out_path}")

print("All tour pages and index successfully generated!")
