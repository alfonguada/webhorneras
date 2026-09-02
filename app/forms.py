from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, StringField, TextAreaField
from wtforms.validators import DataRequired, Email, InputRequired, Length, NumberRange, Optional


class ContactoForm(FlaskForm):
    """Replica los campos del Contact Form 7 original de /contacto/."""

    nombre = StringField("Nombre", validators=[DataRequired(), Length(max=120)])
    correo = StringField("Correo electrónico", validators=[DataRequired(), Email()])
    concepto = StringField("Asunto", validators=[Length(max=200)])
    contenido = TextAreaField(
        "¿En qué podemos ayudarte?", validators=[DataRequired(), Length(max=4000)]
    )
    empresa = StringField("Empresa", validators=[Optional(), Length(max=200)])  # honeypot


class NewsletterForm(FlaskForm):
    """Replica el formulario de Mailchimp for WP del footer."""

    email = StringField("Correo electrónico", validators=[DataRequired(), Email()])


class CateringForm(FlaskForm):
    """Formulario dedicado para presupuestos de Catering Rural / La Conchi."""

    nombre = StringField("Nombre", validators=[DataRequired(), Length(max=120)])
    correo = StringField("Correo electrónico", validators=[DataRequired(), Email()])
    telefono = StringField("Teléfono", validators=[DataRequired(), Length(max=30)])
    tipo_evento = SelectField(
        "Tipo de evento",
        choices=[
            ("boda", "Boda"),
            ("comunion", "Comunión"),
            ("bautizo", "Bautizo"),
            ("comida_popular", "Comida popular / encuentro de grupo"),
            ("empresa", "Evento de empresa"),
            ("otro", "Otro"),
        ],
        validators=[DataRequired()],
    )
    fecha_evento = StringField("Fecha del evento", validators=[Optional(), Length(max=40)])
    comensales = IntegerField(
        "Número de comensales (aprox.)",
        validators=[InputRequired(message="Indica un número aproximado"), NumberRange(min=1, max=2000)],
    )
    mensaje = TextAreaField("Cuéntanos más sobre tu evento", validators=[Optional(), Length(max=4000)])
    empresa = StringField("Empresa", validators=[Optional(), Length(max=200)])  # honeypot


class ReservaMesaForm(FlaskForm):
    """Formulario de reserva de mesa en la Casa de Comidas."""

    nombre = StringField("Nombre", validators=[DataRequired(), Length(max=120)])
    correo = StringField("Correo electrónico", validators=[DataRequired(), Email()])
    telefono = StringField("Teléfono", validators=[DataRequired(), Length(max=30)])
    fecha = StringField("Fecha", validators=[DataRequired(), Length(max=40)])
    hora = StringField("Hora", validators=[DataRequired(), Length(max=20)])
    comensales = IntegerField(
        "Número de comensales",
        validators=[InputRequired(message="Indica el número de comensales"), NumberRange(min=1, max=50)],
    )
    comentario = TextAreaField("Comentario (alergias, ocasión especial…)", validators=[Optional(), Length(max=2000)])
    empresa = StringField("Empresa", validators=[Optional(), Length(max=200)])  # honeypot
