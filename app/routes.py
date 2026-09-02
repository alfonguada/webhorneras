import logging

from flask import Blueprint, Response, abort, current_app, flash, redirect, render_template, url_for

from app import limiter
from app.data.apartamentos import APARTAMENTOS, get_apartamento
from app.emails import enviar_notificacion
from app.forms import CateringForm, ContactoForm, NewsletterForm, ReservaMesaForm

main_bp = Blueprint("main", __name__)
logger = logging.getLogger(__name__)


@main_bp.route("/")
def index():
    return render_template("index.html", apartamentos=APARTAMENTOS)


@main_bp.route("/apartamentos/")
def apartamentos():
    return render_template("apartamentos.html", apartamentos=APARTAMENTOS)


@main_bp.route("/apartamentos/<slug>/")
def apartamento_detalle(slug):
    apto = get_apartamento(slug)
    if apto is None:
        abort(404)
    otros = [a for a in APARTAMENTOS if a["slug"] != slug]
    return render_template("apartamento_detalle.html", apto=apto, otros=otros)


@main_bp.route("/casa-de-comidas/", methods=["GET", "POST"])
@limiter.limit("5/minute;20/hour", methods=["POST"])
def casa_de_comidas():
    form = ReservaMesaForm()
    if form.validate_on_submit():
        if form.empresa.data:
            # Honeypot relleno -> bot. Fingimos éxito sin enviar nada.
            flash("¡Gracias! Hemos recibido tu solicitud de reserva y te confirmaremos en breve.", "success")
            return redirect(url_for("main.casa_de_comidas") + "#reservar")
        logger.info(
            "Nueva reserva de mesa: %s <%s> tel:%s — %s a las %s para %s comensales. %s",
            form.nombre.data,
            form.correo.data,
            form.telefono.data,
            form.fecha.data,
            form.hora.data,
            form.comensales.data,
            form.comentario.data,
        )
        enviar_notificacion(
            asunto=f"Nueva reserva de mesa: {form.nombre.data} ({form.comensales.data} pers.)",
            cuerpo=(
                f"Nombre: {form.nombre.data}\n"
                f"Correo: {form.correo.data}\n"
                f"Teléfono: {form.telefono.data}\n"
                f"Fecha: {form.fecha.data}\n"
                f"Hora: {form.hora.data}\n"
                f"Comensales: {form.comensales.data}\n"
                f"Comentario: {form.comentario.data or '(sin comentario)'}"
            ),
            responder_a=form.correo.data,
        )
        flash("¡Gracias! Hemos recibido tu solicitud de reserva y te confirmaremos en breve.", "success")
        return redirect(url_for("main.casa_de_comidas") + "#reservar")
    return render_template("casa_de_comidas.html", form=form)


@main_bp.route("/catering-rural/", methods=["GET", "POST"])
@limiter.limit("5/minute;20/hour", methods=["POST"])
def catering_rural():
    form = CateringForm()
    if form.validate_on_submit():
        if form.empresa.data:
            flash("¡Gracias! Hemos recibido tu solicitud de presupuesto y te contactaremos en breve.", "success")
            return redirect(url_for("main.catering_rural") + "#presupuesto")
        logger.info(
            "Nueva solicitud de catering: %s <%s> tel:%s — %s el %s para %s comensales. %s",
            form.nombre.data,
            form.correo.data,
            form.telefono.data,
            dict(form.tipo_evento.choices).get(form.tipo_evento.data, form.tipo_evento.data),
            form.fecha_evento.data or "(sin fecha indicada)",
            form.comensales.data,
            form.mensaje.data,
        )
        enviar_notificacion(
            asunto=f"Nueva solicitud de catering: {form.nombre.data} ({form.comensales.data} pers.)",
            cuerpo=(
                f"Nombre: {form.nombre.data}\n"
                f"Correo: {form.correo.data}\n"
                f"Teléfono: {form.telefono.data}\n"
                f"Tipo de evento: {dict(form.tipo_evento.choices).get(form.tipo_evento.data, form.tipo_evento.data)}\n"
                f"Fecha del evento: {form.fecha_evento.data or '(sin fecha indicada)'}\n"
                f"Comensales: {form.comensales.data}\n"
                f"Mensaje: {form.mensaje.data or '(sin mensaje)'}"
            ),
            responder_a=form.correo.data,
        )
        flash("¡Gracias! Hemos recibido tu solicitud de presupuesto y te contactaremos en breve.", "success")
        return redirect(url_for("main.catering_rural") + "#presupuesto")
    return render_template("catering_rural.html", form=form)


@main_bp.route("/foodtruck/")
def foodtruck():
    return render_template("foodtruck.html")


@main_bp.route("/entorno/")
def entorno():
    return render_template("entorno.html")


@main_bp.route("/actividades/")
def actividades():
    return render_template("actividades.html")


@main_bp.route("/comodidades/")
def comodidades():
    return render_template("comodidades.html", apartamentos=APARTAMENTOS)


@main_bp.route("/disponibilidad/")
def disponibilidad():
    return render_template("disponibilidad.html")


@main_bp.route("/carta/")
def carta():
    return render_template("carta.html")


@main_bp.route("/historia/")
def historia():
    return render_template("historia.html", apartamentos=APARTAMENTOS)


@main_bp.route("/faq/")
def faq():
    # En el sitio original esta página estaba vacía; el FAQ real vive
    # en la portada (sección con datos estructurados AIOSEO).
    return redirect(url_for("main.index") + "#faq")


@main_bp.route("/contacto/", methods=["GET", "POST"])
@limiter.limit("5/minute;20/hour", methods=["POST"])
def contacto():
    form = ContactoForm()
    if form.validate_on_submit():
        if form.empresa.data:
            flash("Gracias por escribirnos. Te responderemos lo antes posible.", "success")
            return redirect(url_for("main.contacto"))
        logger.info(
            "Nuevo mensaje de contacto: %s <%s> — %s: %s",
            form.nombre.data,
            form.correo.data,
            form.concepto.data,
            form.contenido.data,
        )
        enviar_notificacion(
            asunto=f"Nuevo mensaje de contacto: {form.nombre.data} — {form.concepto.data or 'Sin asunto'}",
            cuerpo=(
                f"Nombre: {form.nombre.data}\n"
                f"Correo: {form.correo.data}\n"
                f"Asunto: {form.concepto.data or '(sin asunto)'}\n\n"
                f"{form.contenido.data}"
            ),
            responder_a=form.correo.data,
        )
        flash("Gracias por escribirnos. Te responderemos lo antes posible.", "success")
        return redirect(url_for("main.contacto"))
    return render_template("contacto.html", form=form)


@main_bp.route("/newsletter/", methods=["POST"])
@limiter.limit("5/minute;20/hour")
def newsletter():
    form = NewsletterForm()
    if form.validate_on_submit():
        # TODO: dar de alta al suscriptor en Mailchimp usando
        # current_app.config["MAILCHIMP_*"] una vez el propietario facilite
        # las credenciales reales.
        logger.info("Nueva suscripción a newsletter: %s", form.email.data)
        flash("¡Gracias por suscribirte!", "success")
    else:
        flash("Revisa el correo electrónico introducido.", "error")
    return redirect(url_for("main.index") + "#newsletter")


@main_bp.route("/aviso-legal/")
def aviso_legal():
    return render_template("legal/aviso_legal.html")


@main_bp.route("/politica-privacidad/")
def politica_privacidad():
    return render_template("legal/politica_privacidad.html")


@main_bp.route("/politica-de-cookies/")
def politica_cookies():
    return render_template("legal/politica_cookies.html")


@main_bp.route("/politica-de-reservas/")
def politica_reservas():
    return render_template("legal/politica_reservas.html")


@main_bp.route("/regimen-interno/")
def regimen_interno():
    return render_template("legal/regimen_interno.html")


# El sitio original no tenía robots.txt ni sitemap.xml archivados en
# Wayback Machine (ver dosier de análisis) — se generan de cero aquí.

@main_bp.route("/robots.txt")
def robots_txt():
    lines = [
        "User-agent: *",
        "Allow: /",
        f"Sitemap: {url_for('main.sitemap_xml', _external=True)}",
    ]
    return Response("\n".join(lines), mimetype="text/plain")


# (endpoint, changefreq, priority) — páginas de producto/venta primero,
# contenido de apoyo después, legales al final con prioridad mínima.
_SITEMAP_ENDPOINTS = [
    ("main.index", "daily", "1.0"),
    ("main.apartamentos", "weekly", "0.9"),
    ("main.casa_de_comidas", "weekly", "0.9"),
    ("main.catering_rural", "weekly", "0.8"),
    ("main.foodtruck", "weekly", "0.8"),
    ("main.carta", "daily", "0.7"),
    ("main.comodidades", "monthly", "0.6"),
    ("main.disponibilidad", "weekly", "0.6"),
    ("main.entorno", "monthly", "0.6"),
    ("main.actividades", "monthly", "0.6"),
    ("main.historia", "monthly", "0.5"),
    ("main.contacto", "monthly", "0.5"),
    ("main.aviso_legal", "yearly", "0.2"),
    ("main.politica_privacidad", "yearly", "0.2"),
    ("main.politica_cookies", "yearly", "0.2"),
    ("main.politica_reservas", "yearly", "0.2"),
    ("main.regimen_interno", "yearly", "0.2"),
]


@main_bp.route("/sitemap.xml")
def sitemap_xml():
    entries = [
        (url_for(ep, _external=True), changefreq, priority)
        for ep, changefreq, priority in _SITEMAP_ENDPOINTS
    ]
    entries += [
        (url_for("main.apartamento_detalle", slug=a["slug"], _external=True), "weekly", "0.9")
        for a in APARTAMENTOS
    ]
    xml = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    xml += [
        f"  <url><loc>{loc}</loc><changefreq>{changefreq}</changefreq><priority>{priority}</priority></url>"
        for loc, changefreq, priority in entries
    ]
    xml.append("</urlset>")
    return Response("\n".join(xml), mimetype="application/xml")


@main_bp.route("/llms.txt")
def llms_txt():
    """Resumen del sitio en formato llms.txt (llmstxt.org) para que los
    sistemas de IA (ChatGPT, Perplexity, Google AI Overviews...) puedan
    citar a Las Horneras de Cobeta con datos correctos y actualizados."""
    lines = [
        "# Las Horneras de Cobeta",
        "",
        "> Apartamentos rurales, casa de comidas y catering rural en Cobeta, "
        "Guadalajara, dentro del Parque Natural del Alto Tajo (España).",
        "",
        "Las Horneras de Cobeta es un alojamiento rural de 5 apartamentos "
        f"(Andrea, Petronila, Florencia, Martina e Hipólita) situado en {current_app.config['DIRECCION']}, "
        "que incluye una casa de comidas con cocina tradicional al horno de leña, "
        "un servicio de catering rural para bodas, comuniones, bautizos y eventos, "
        "y una foodtruck itinerante (La Conchi) disponible para alquiler.",
        "",
        f"Teléfono: {current_app.config['TELEFONO_VISIBLE']} · "
        f"Email: {current_app.config['EMAIL_INFO']} · "
        f"Nº de registro turístico: {current_app.config['NUM_REGISTRO_TURISTICO']} · "
        f"Clasificación: {current_app.config['CLASIFICACION']}",
        "",
        "## Alojamiento",
        f"- [Apartamentos]({url_for('main.apartamentos', _external=True)}): los 5 apartamentos rurales, con tamaño, ocupación y precio desde.",
    ]
    lines += [
        f"- [{a['nombre']}]({url_for('main.apartamento_detalle', slug=a['slug'], _external=True)}): "
        f"{a['subtitulo']} — {a['m2']} m², {a['ocupacion']}, desde {a['precio_desde']}€/día."
        for a in APARTAMENTOS
    ]
    lines += [
        f"- [Comodidades]({url_for('main.comodidades', _external=True)}): comparativa de los 5 apartamentos.",
        f"- [Disponibilidad]({url_for('main.disponibilidad', _external=True)}): buscador de fechas y reserva online (AvaiBook).",
        "",
        "## Gastronomía",
        f"- [Casa de Comidas]({url_for('main.casa_de_comidas', _external=True)}): restaurante con cocina tradicional al horno de leña, asados y platos caseros para recoger. Reserva de mesa online, por WhatsApp o por teléfono.",
        f"- [Carta]({url_for('main.carta', _external=True)}): carta, menú de asado, carta de vinos, bebidas y postres, y menú para llevar.",
        f"- [Catering Rural]({url_for('main.catering_rural', _external=True)}): catering para bodas, comuniones, bautizos, eventos de empresa y comidas populares en Cobeta y el Alto Tajo. Presupuesto personalizado por formulario.",
        f"- [La Conchi Foodtruck]({url_for('main.foodtruck', _external=True)}): foodtruck de cocina tradicional para eventos, ferias y acciones promocionales; alquiler desde 200€/día.",
        "",
        "## Entorno y experiencias",
        f"- [Entorno]({url_for('main.entorno', _external=True)}): Cobeta, el Alto Tajo, miradores, rutas de senderismo y pueblos cercanos (Molina de Aragón, Ablanque, Olmeda de Cobeta).",
        f"- [Actividades]({url_for('main.actividades', _external=True)}): visita guiada a Cobeta, resinero por un día, salida al campo, retorno de los grandes herbívoros.",
        f"- [Historia]({url_for('main.historia', _external=True)}): el origen del nombre «Las Horneras» y la historia de cada una de las cinco horneras que dan nombre a los apartamentos.",
        "",
        "## Contacto",
        f"- [Contacto]({url_for('main.contacto', _external=True)}): formulario de contacto, ubicación y datos de la empresa.",
    ]
    return Response("\n".join(lines), mimetype="text/plain")
