import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-cambia-esto-en-produccion")

    # Datos de la empresa (Aviso Legal / Política de Privacidad archivados)
    RAZON_SOCIAL = "Experiencias con H & D, S.L."
    NIF = "B05481924"
    DIRECCION = "Calle Castillo, s/n, 19443 Cobeta (Guadalajara)"
    TELEFONO = "621240349"
    TELEFONO_VISIBLE = "621 240 349"
    EMAIL_INFO = "info@lashorneras.com"
    EMAIL_RESERVAS = "reservas@lashorneras.com"
    NUM_REGISTRO_TURISTICO = "19012170072"
    CLASIFICACION = "3 estrellas verdes"
    FACEBOOK_URL = "https://www.facebook.com/lashornerasdecobeta"
    INSTAGRAM_URL = "https://www.instagram.com/las.horneras/"
    WHATSAPP_NUMERO = "34621240349"  # formato internacional sin '+' para wa.me

    # --- Integraciones pendientes de credenciales reales del propietario ---
    # Envío de email del formulario de contacto (Flask-Mail / SMTP)
    MAIL_SERVER = os.environ.get("MAIL_SERVER", "")
    MAIL_PORT = int(os.environ.get("MAIL_PORT", 587))
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME", "")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD", "")
    MAIL_DESTINATARIO = os.environ.get("MAIL_DESTINATARIO", EMAIL_INFO)

    # Alta en newsletter (API de Mailchimp)
    MAILCHIMP_API_KEY = os.environ.get("MAILCHIMP_API_KEY", "")
    MAILCHIMP_LIST_ID = os.environ.get("MAILCHIMP_LIST_ID", "")
    MAILCHIMP_SERVER_PREFIX = os.environ.get("MAILCHIMP_SERVER_PREFIX", "")

    # Motor de reservas AvaiBook: el código de propiedad para el CTA
    # "¡RESERVA YA!" es distinto por apartamento (ver
    # app/data/apartamentos.py -> avaibook_cod_alojamiento), no una
    # constante global.
    # Widget general de disponibilidad (home / disponibilidad)
    AVAIBOOK_WIDGET_ID = os.environ.get("AVAIBOOK_WIDGET_ID", "95614")
    AVAIBOOK_WIDGET_TOKEN = os.environ.get(
        "AVAIBOOK_WIDGET_TOKEN", "f+lKL0tEb/q8nViSK7EClQ=="
    )
