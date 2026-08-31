from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Email, Length


class ContactoForm(FlaskForm):
    """Replica los campos del Contact Form 7 original de /contacto/."""

    nombre = StringField("Nombre", validators=[DataRequired(), Length(max=120)])
    correo = StringField("Correo electrónico", validators=[DataRequired(), Email()])
    concepto = StringField("Asunto", validators=[Length(max=200)])
    contenido = TextAreaField(
        "¿En qué podemos ayudarte?", validators=[DataRequired(), Length(max=4000)]
    )


class NewsletterForm(FlaskForm):
    """Replica el formulario de Mailchimp for WP del footer."""

    email = StringField("Correo electrónico", validators=[DataRequired(), Email()])
