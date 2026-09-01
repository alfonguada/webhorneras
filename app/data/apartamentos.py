# Datos de los 5 apartamentos, recuperados del sitio WordPress archivado
# (Wayback Machine, copias previas al compromiso de seguridad de sep-2025).
#
# avaibook_cod_alojamiento: el WordPress original enlazaba el botón "¡RESERVA
# YA!" de las 5 fichas al mismo código (370830, el de Petronila) — un bug
# real del sitio, no un dato correcto. Se obtuvieron los códigos correctos
# de cada apartamento en vivo desde bookonline.pro/es/properties/95614
# (el listado público real de Las Horneras en la plataforma de AvaiBook).
#
# Fotos: Florencia e Hipólita vienen del FTP (uploads/2018/09, resolución
# 1024x683). Andrea, Petronila y Martina vienen del listado en vivo de
# AvaiBook/bookonline.pro (más recientes y de mayor resolución, 1280px) —
# ambas fuentes son fotos reales de la propiedad, solo con procedencia y
# fecha distintas; conviene homogeneizar cuando lleguen más fotos del FTP.

APARTAMENTOS = [
    {
        "slug": "andrea",
        "nombre": "Andrea",
        "subtitulo": "Apartamento totalmente adaptado",
        "resumen": "Ideal para movilidad reducida",
        "m2": 55,
        "ocupacion": "2+2 camas individuales / sofá cama",
        "precio_desde": 100,
        "imagen": "apartamentos/andrea/01.jpg",
        "num_fotos": 10,
        "descripcion": [
            "Andrea no es solo un lugar para quedarse; es un espacio inclusivo y "
            "accesible para todos. Creado con la movilidad en mente, el apartamento "
            "cuenta con instalaciones adaptadas y comodidades diseñadas para "
            "satisfacer las necesidades de todos.",
            "Podíamos contaros miles de historias sobre Andrea, sobre todo porque "
            "esta Hornera nos acompañó hasta el año 2023. Pero nosotros lo que "
            "buscamos es rendir homenaje a esa mujer fuerte y luchadora que "
            "siempre nos arrancaba una sonrisa. Ella misma vio como su rutina "
            "cambiaba cuando de pronto necesitó una silla de ruedas para el resto "
            "de su vida. Alguno pensará que una pena, y tal vez, pero Andrea nunca "
            "lo vivió así y siempre supo cómo enfrentarse a los cambios que se lo "
            "ponían por delante.",
            "Por eso este apartamento es para ella, y para todos los que como "
            "ella, tienen unas necesidades diferentes a la mayoría de nosotros. "
            "Adaptado en su totalidad, pensado con grandes espacios y lleno, eso "
            "sí, de todo nuestro cariño por la abuela Andrea.",
        ],
        "amenities": [
            "Acceso a la propiedad independiente", "Adaptado a sillas de ruedas",
            "Baño y cocina a 80cm", "Ducha muy amplia", "Vistas a la propiedad",
            "Camas individuales 105 cm", "Cargadores USB", "WiFi gratuito",
            "Smart TV con soporte extensible", "Pet Friendly",
        ],
        "avaibook_widget_full": "141897",
        "avaibook_widget_mini": "141971",
        "avaibook_cod_alojamiento": "371207",
        "historia": (
            "Andrea nos acompañó hasta el año 2023: una mujer fuerte y luchadora "
            "que siempre nos arrancaba una sonrisa. Vio cómo su rutina cambiaba "
            "cuando necesitó una silla de ruedas para el resto de su vida, y "
            "nunca dejó de enfrentarse a los cambios con la misma entereza. Este "
            "apartamento, adaptado en su totalidad, es un homenaje a la abuela "
            "Andrea y a todos los que, como ella, tienen necesidades diferentes."
        ),
    },
    {
        "slug": "petronila",
        "nombre": "Petronila",
        "subtitulo": "Apartamento con vistas a la montaña",
        "resumen": "Ideal para enamorados",
        "m2": 45,
        "ocupacion": "2+2 / sofá cama",
        "precio_desde": 150,
        "imagen": "apartamentos/petronila/01.jpg",
        "num_fotos": 17,
        "descripcion": [
            "Petronila no es solo un apartamento; es una ventana al majestuoso "
            "paisaje que rodea nuestra querida villa. Disfruta de las mejores "
            "vistas del pueblo, la vega y las antiguas eras de Cobeta, una "
            "estampa que impresiona a cualquiera.",
            "Petronila, como puedes ver, es un espacio maravilloso para "
            "disfrutar en pareja, aunque siempre con la posibilidad de aumentar "
            "su capacidad gracias a nuestro sofá cama convertible. De techos "
            "altos de madera, dormitorio en altillo abuhardillado y espacio "
            "totalmente abierto, nos brinda la intimidad necesaria para "
            "acercarnos a los que más queremos.",
        ],
        "amenities": [
            "Smart TV de 55 pulgadas", "Enchufes y tomas USB",
            "Cocina totalmente equipada", "Plancha y tabla de planchar",
            "Bañera de diseño", "WiFi gratuito", "Terraza privada",
            "Chimenea", "Vistas panorámicas", "Sofá cama convertible",
        ],
        "avaibook_widget_full": "141898",
        "avaibook_widget_mini": "141967",
        "avaibook_cod_alojamiento": "370830",
        "historia": (
            "Petronila da nombre al apartamento con las mejores vistas de la "
            "casa: el pueblo, la vega y las antiguas eras de Cobeta se despliegan "
            "ante la ventana, la misma estampa que ella contemplaba cada día. Un "
            "espacio de techos altos e intimidad, pensado para acercarse a los "
            "que más se quiere — igual que hacía ella."
        ),
    },
    {
        "slug": "florencia",
        "nombre": "Florencia",
        "subtitulo": "Apartamento amplio y de techos altos",
        "resumen": "Ideal para viajar en familia y amigos",
        "m2": 82,
        "ocupacion": "4+4 / cama doble / sofá cama",
        "precio_desde": 200,
        "imagen": "apartamentos/florencia/01.jpg",
        "num_fotos": 11,
        "descripcion": [
            "En el corazón de su hogar, Florencia siempre tenía hueco para uno "
            "más, al igual que nuestro apartamento de gran capacidad.",
            "Si lo que más disfrutas es viajar con los tuyos a todas partes, "
            "Florencia te brinda la posibilidad de hacerlo. Gracias a su "
            "capacidad ampliable, puedes compartir tu estancia junto con los "
            "que más quieres, tal como hacía Florencia en su hogar.",
        ],
        "amenities": [
            "Amplio y luminoso", "Apartamento a dos alturas",
            "Zona de juegos en altillo", "Baño compartido y privado",
            "Cocina totalmente equipada", "Enchufes con toma USB",
            "WiFi gratuito", "Smart TV", "Chimenea", "Acceso por escalera",
        ],
        "avaibook_widget_full": "141899",
        "avaibook_widget_mini": "141968",
        "avaibook_cod_alojamiento": "370831",
        "historia": (
            "En el corazón de su hogar, Florencia siempre tenía hueco para uno "
            "más. Así era ella: acogedora, generosa, con la puerta abierta para "
            "quien llegara. El apartamento que lleva su nombre hereda esa "
            "vocación — amplio, de techos altos y capacidad ampliable, para que "
            "nadie se quede fuera cuando se viaja en familia o con amigos."
        ),
    },
    {
        "slug": "martina",
        "nombre": "Martina",
        "subtitulo": "Habitación con baño integrado",
        "resumen": "Un rincón para enamorarse — \"La Serrana\"",
        "m2": 60,
        "ocupacion": "2+2 / cama doble / sofá cama",
        "precio_desde": 150,
        "imagen": "apartamentos/martina/01.jpg",
        "num_fotos": 19,
        "descripcion": [
            "Martina es un lugar donde la historia y el romance se entrelazan, "
            "invitándote a enamorarte de la autenticidad y la calidez que lo "
            "caracterizan. ¡Deja que \"La Serrana\" sea el escenario de tu "
            "propia historia de amor!",
            "La guinda del pastel la encontrarás en el dormitorio: bañera "
            "integrada a los pies de la cama y un baño totalmente equipado "
            "detrás de su preciosa celosía de madera.",
        ],
        "amenities": [
            "Amplio y luminoso", "Terraza privada", "Bañera en la habitación",
            "Chimenea", "Cocina totalmente equipada",
            "Baño privado y compartido", "Cargadores con toma USB",
            "WiFi gratuito", "Smart TV con soporte extensible",
            "Decoración natural",
        ],
        "avaibook_widget_full": "141901",
        "avaibook_widget_mini": "141969",
        "avaibook_cod_alojamiento": "371205",
        "historia": (
            "Conocida como \"La Serrana\", Martina da nombre a un rincón donde "
            "la historia y el romance se entrelazan. El apartamento conserva ese "
            "carácter entrañable en cada detalle, desde la celosía de madera del "
            "baño hasta la bañera a los pies de la cama, invitando a vivir aquí "
            "tu propia historia de amor."
        ),
    },
    {
        "slug": "hipolita",
        "nombre": "Hipólita",
        "subtitulo": "Familiar y luminoso",
        "resumen": "Apartamento familiar",
        "m2": 55,
        "ocupacion": "4+2 / sofá cama / cama doble",
        "precio_desde": 150,
        "imagen": "apartamentos/hipolita/01.jpg",
        "num_fotos": 8,
        "descripcion": [
            "Un apartamento acogedor y sencillo, con vistas al pueblo y situado "
            "sobre el antiguo horno que existía en la propiedad. Hipólita le da "
            "nombre, una hornera cariñosa y familiar como el apartamento.",
            "Para familias y grupos de amigos. Un espacio cómodo y diáfano "
            "ideal para viajar acompañado mientras disfrutas del precioso "
            "entorno que nos rodea.",
        ],
        "amenities": [
            "Luminoso y espacioso", "Apartamento familiar",
            "Cocina totalmente equipada", "Salón/comedor", "Baño compartido",
            "Enchufes con toma USB", "Smart TV", "WiFi gratuito",
            "Chimenea", "Vistas al Castillo de Cobeta",
        ],
        "avaibook_widget_full": "141902",
        "avaibook_widget_mini": "141970",
        "avaibook_cod_alojamiento": "371206",
        "historia": (
            "Hipólita fue una hornera cariñosa y familiar, y así es el "
            "apartamento que lleva su nombre: acogedor, sencillo y luminoso, "
            "construido sobre el antiguo horno que existía en la propiedad. Un "
            "espacio pensado para familias y grupos de amigos, con vistas al "
            "Castillo de Cobeta, tal y como ella los recibía en su día."
        ),
    },
]


def get_apartamento(slug):
    for apto in APARTAMENTOS:
        if apto["slug"] == slug:
            return apto
    return None
