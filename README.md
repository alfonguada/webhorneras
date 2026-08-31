# Las Horneras de Cobeta — sitio Flask

Migración del sitio WordPress (Hoteller + Elementor) a Flask, reconstruida a
partir de copias archivadas en Wayback Machine (el sitio original está caído
desde ago-2026 tras un compromiso de seguridad — ver dosier de análisis).

## Arrancar en local

```bash
python -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe run.py
```

Se sirve en `http://127.0.0.1:5050/` (puerto configurable con la variable de
entorno `PORT`).

## Estructura

```
app/
  data/apartamentos.py   # datos de los 5 apartamentos (incl. IDs de widget AvaiBook)
  templates/              # Jinja2, un fichero por página
  static/css/style.css    # sistema de diseño (paleta y tipografía reales del sitio original)
  static/fonts/           # fuente de marca "ogilen" autoalojada
  routes.py                # todas las rutas
  forms.py                 # formularios (Flask-WTF)
  config.py                # datos de la empresa + credenciales pendientes
```

## Pendiente (marcado como `TODO` en el código)

- **Fotos reales.** Solo se recuperaron del archivo el logo, el icono de marca
  y una foto de portada — el resto de imágenes (apartamentos, restaurante,
  catering, entorno, foodtruck) nunca fueron archivadas por Wayback Machine.
  Sustituir los bloques de color marcados "(pendiente de sustituir)" en
  `index.html`, `apartamento_detalle.html`, `casa_de_comidas.html`,
  `catering_rural.html`, `foodtruck.html` y `entorno.html`.
- **Email de contacto real.** `routes.py::contacto()` solo registra el
  mensaje en el log; falta conectar `Flask-Mail`/SMTP con
  `config.py::MAIL_*` una vez el propietario facilite credenciales.
- **Newsletter real.** `routes.py::newsletter()` solo registra el alta;
  falta la llamada a la API de Mailchimp con `config.py::MAILCHIMP_*`.
- **Widget de búsqueda AvaiBook.** El HTML archivado no incluía el
  `<script>` que activa `div.avaibook-search-widget` (se generaba desde el
  panel de AvaiBook). Pedir al propietario el snippet actual — ver
  `apartamentos.html` y `disponibilidad.html`.
- **Carta del restaurante.** No se conservaron los platos (se cargaban vía
  el plugin `mp-restaurant-menu`, no quedaron en el HTML estático). Rellenar
  `carta.html`.
- **Historia.** La página original ya tenía estos textos sin rellenar en el
  sitio real; `historia.html` conserva la estructura con marcadores
  `[Pendiente]`.
- **Dirección de la empresa inconsistente.** El Aviso Legal archivado usa
  "C/ Castillo, 1 y 3" y la Política de Privacidad usa "Calle Calvario, 2".
  Confirmar con el propietario cuál es correcta.
- **Mapa de Google en /contacto/.** Placeholder de momento.

## Antes de desplegar

- Cambiar `SECRET_KEY` (variable de entorno, no hardcodear).
- Revisar primero el incidente de seguridad del WordPress original (ver
  dosier de análisis) antes de dar por bueno ningún contenido "actual" sin
  volver a verificarlo en vivo.
