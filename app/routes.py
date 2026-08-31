import logging

from flask import Blueprint, current_app, flash, redirect, render_template, url_for

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
