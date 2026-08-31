import logging

from flask import Blueprint, Response, current_app, flash, redirect, render_template, url_for

from app.data.apartamentos import APARTAMENTOS, get_apartamento
from app.forms import ContactoForm, NewsletterForm

main_bp = Blueprint("main", __name__)
logger = logging.getLogger(__name__)


@main_bp.context_processor
def inject_globals():
    """Datos disponibles en todas las plantillas (footer, nav, etc.)."""
    return {
        "apartamentos_nav": APARTAMENTOS,
        "newsletter_form": NewsletterForm(),
    }


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
        return render_template("404.html"), 404
    otros = [a for a in APARTAMENTOS if a["slug"] != slug]
    return render_template("apartamento_detalle.html", apto=apto, otros=otros)


@main_bp.route("/casa-de-comidas/")
def casa_de_comidas():
    return render_template("casa_de_comidas.html")


@main_bp.route("/catering-rural/")
def catering_rural():
    return render_template("catering_rural.html")


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
def contacto():
    form = ContactoForm()
    if form.validate_on_submit():
        # TODO: enviar email real (Flask-Mail/SMTP) usando
        # current_app.config["MAIL_*"] una vez el propietario facilite
        # credenciales. De momento se registra en el log del servidor
        # para no perder ningún envío durante el desarrollo.
        logger.info(
            "Nuevo mensaje de contacto: %s <%s> — %s: %s",
            form.nombre.data,
            form.correo.data,
            form.concepto.data,
            form.contenido.data,
        )
        flash("Gracias por escribirnos. Te responderemos lo antes posible.", "success")
        return redirect(url_for("main.contacto"))
    return render_template("contacto.html", form=form)


@main_bp.route("/newsletter/", methods=["POST"])
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


@main_bp.route("/sitemap.xml")
def sitemap_xml():
    static_endpoints = [
        "main.index", "main.apartamentos", "main.comodidades",
        "main.casa_de_comidas", "main.carta", "main.catering_rural",
        "main.foodtruck", "main.entorno", "main.actividades",
        "main.disponibilidad", "main.historia", "main.contacto",
        "main.aviso_legal", "main.politica_privacidad",
        "main.politica_cookies", "main.politica_reservas",
        "main.regimen_interno",
    ]
    urls = [url_for(ep, _external=True) for ep in static_endpoints]
    urls += [
        url_for("main.apartamento_detalle", slug=a["slug"], _external=True)
        for a in APARTAMENTOS
    ]
    xml = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    xml += [f"  <url><loc>{u}</loc></url>" for u in urls]
    xml.append("</urlset>")
    return Response("\n".join(xml), mimetype="application/xml")
