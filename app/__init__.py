from flask import Flask, render_template
from flask_mail import Mail

from app.config import Config

mail = Mail()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    mail.init_app(app)

    from app.data.apartamentos import APARTAMENTOS
    from app.forms import NewsletterForm
    from app.routes import main_bp

    app.register_blueprint(main_bp)

    @app.context_processor
    def inject_globals():
        """Disponible en TODAS las plantillas, incluidas las páginas de
        error (que Werkzeug puede renderizar antes de entrar en el
        blueprint, así que un context_processor de blueprint no vale)."""
        return {
            "apartamentos_nav": APARTAMENTOS,
            "newsletter_form": NewsletterForm(),
        }

    @app.errorhandler(404)
    def not_found(_error):
        return render_template("404.html"), 404

    @app.errorhandler(500)
    def server_error(_error):
        return render_template("500.html"), 500

    return app
