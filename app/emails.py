import logging

from flask import current_app
from flask_mail import Message

from app import mail

logger = logging.getLogger(__name__)


def enviar_notificacion(asunto, cuerpo, responder_a=None):
    """Envía un email a los destinatarios configurados (MAIL_DESTINATARIOS).

    Si el envío falla (SMTP sin configurar, credenciales incorrectas, etc.)
    se registra el error pero no se propaga: el visitante ya ha recibido su
    confirmación y su solicitud queda igualmente en el log del servidor.
    """
    destinatarios = current_app.config.get("MAIL_DESTINATARIOS", [])
    if not destinatarios or not current_app.config.get("MAIL_SERVER"):
        logger.warning("Email no enviado (SMTP sin configurar): %s", asunto)
        return False

    # Los campos de formulario llegan directos al asunto del email; un envío
    # con saltos de línea podría intentar inyectar cabeceras (Bcc, etc.).
    # Flask-Mail ya lo rechaza con BadHeaderError, pero preferimos sanear
    # aquí para no perder silenciosamente la notificación.
    asunto = asunto.replace("\r", " ").replace("\n", " ")

    try:
        msg = Message(subject=asunto, recipients=destinatarios, body=cuerpo)
        if responder_a:
            msg.reply_to = responder_a
        mail.send(msg)
        return True
    except Exception:
        logger.exception("Fallo al enviar email: %s", asunto)
        return False
