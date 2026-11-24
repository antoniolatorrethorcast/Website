"""Guía en español: cómo predecir la fuga de clientes (churn) en banca, seguros y telco (2026-11-24).
Cifras de ejemplo = las que thorcast.ai ya publica en los videos de casos de uso, con la misma etiqueta
(ilustrativo / simulado / caso). Sin nombres de clientes ni precios."""

FILE = "como-predecir-churn-banca-seguros-telco.html"
DATE = "2026-11-24"

TITLE = "Cómo predecir la fuga de clientes en banca, seguros y telco — Thorcast.AI"
DESC = ("Guía de modelos de churn para banca, seguros y telco: cómo definir la fuga, qué datos usar, cómo medir con tu cupo de contactos "
        "y cómo llevar el score a una campaña rentable.")
H1 = "Cómo predecir la fuga de clientes en banca, seguros y telco: guía práctica 2026"
TAG = "GUÍA"
META = "Thorcast.AI · Actualizada el 24 de noviembre de 2026 · 8 min de lectura"
CRUMB = "Cómo predecir la fuga de clientes en banca, seguros y telco"

INTRO = (
    "<p>La mayoría de las guías de churn están escritas para empresas de software por suscripción. En banca, seguros y "
    "telecomunicaciones el problema es distinto: el cliente rara vez avisa que se va, la fuga no siempre es una cancelación "
    "formal y el equipo de retención tiene un cupo fijo de llamadas, ofertas o visitas. Esta guía es para equipos de "
    "analítica, riesgo, CRM y retención de esas industrias.</p>"
    "<p>La idea central: un modelo de churn no se mide por cuántas fugas predice, sino por cuánto valor conserva con los "
    "contactos que ya puedes hacer. Las cifras de ejemplo de esta guía salen de los casos que mostramos en video en "
    'thorcast.ai, con la misma etiqueta que llevan ahí (caso, ejemplo ilustrativo o simulado).</p>'
)

DEF_H = "Primero, define qué es “irse” en tu industria"
DEF_P = ("<p>La definición del evento (el <em>target</em>) decide más el resultado que el algoritmo. Escríbela antes de mirar "
         "los datos, con un horizonte claro: “se va en los próximos 60 o 90 días”, medido desde la fecha en que harías el contacto.</p>")
DEFS = [
    ("Banca y retail financiero",
     "Pocas veces hay un cierre formal: el cliente deja de usar la tarjeta, mueve la nómina o vacía la cuenta. Define la fuga como cierre "
     "o como caída sostenida de actividad o saldo (por ejemplo, sin transacciones durante 90 días), y separa la fuga voluntaria de la "
     "cancelación por mora, que se trata con un modelo de cobranza."),
    ("Seguros de vida y salud",
     "El evento es la caducidad o el rescate de la póliza. Importa el momento: los primeros años de una póliza concentran buena parte "
     "de las caídas, así que conviene modelar la persistencia por antigüedad y no solo “cancela sí o no”."),
    ("Seguros generales y corredores",
     "La fuga ocurre sobre todo en la renovación: el cliente no renueva o se cambia a otra compañía. El horizonte natural son las "
     "semanas antes del vencimiento, que es cuando la llamada todavía puede cambiar la decisión."),
    ("Telco",
     "En contrato, el evento es la portabilidad o la baja. En prepago no hay baja: el cliente deja de recargar. Define la fuga por "
     "inactividad (por ejemplo, 30 días sin recarga ni uso) y trata por separado la migración de contrato a prepago, que no siempre es pérdida."),
]

DATA_H = "Qué datos predicen la fuga"
DATA = [
    "<strong>Comportamiento reciente.</strong> Cambios más que niveles: la caída de uso, saldo, recargas o transacciones en las últimas semanas dice más que el promedio del año.",
    "<strong>Relación con la empresa.</strong> Antigüedad, productos contratados, reclamos, llamadas al servicio al cliente, fallas de servicio y cambios de plan o de cobertura.",
    "<strong>Precio y condiciones.</strong> Alzas de tarifa o de prima, fin de un periodo promocional, vencimiento de un contrato o de una permanencia.",
    "<strong>Contexto externo.</strong> El perfil del área donde vive el cliente, la calidad de su email y su teléfono y su huella digital son señales que tus sistemas no tienen y que ayudan sobre todo cuando el historial propio es corto.",
    "<strong>Cuidado con las fugas de información.</strong> Cualquier variable que se registra después de que el cliente decidió irse (una solicitud de portabilidad, una llamada para cancelar) hace que el modelo se vea perfecto en el laboratorio y falle en producción.",
]

MEASURE_H = "Mide el modelo con tu cupo de contactos"
MEASURE = (
    "<p>La exactitud (accuracy) engaña: si el 3 % de los clientes se va, un modelo que dice “nadie se va” acierta el 97 %. Lo que "
    "importa es cuántas fugas reales encuentras dentro del cupo que tu equipo puede contactar. Ordena la cartera por score, toma "
    "los primeros N (tu cupo) y cuenta cuántos de ellos se fueron de verdad en la muestra de prueba, separada por tiempo.</p>"
    "<p>Así se ven las diferencias en los casos que publicamos:</p>"
)
CASES = [
    ("Telco móvil (caso en video)", "Con los mismos 200.000 contactos, el modelo de Thorcast encuentra 132.000 de los clientes que se irían, frente a 102.000 del modelo actual. El Gini sube de 0,44 a 0,60."),
    ("Seguros de vida (ejemplo simulado)", "En el 20 % de mayor riesgo, el modelo actual encontró 12,5 cancelaciones reales de cada 100; Thorcast, 16,5 con datos internos y 18,5 sumando datos enriquecidos."),
    ("Corredores de seguros (ejemplo)", "Con el mismo cupo de 240.000 contactos, el modelo actual encuentra 88.000 de las 160.000 pólizas que se irían; Thorcast encuentra 105.000."),
    ("Seguros de auto, renovación (escenario ilustrativo)", "Con el mismo cupo de 50.000 llamadas, de los clientes que elige el método actual se iría el 40 %; de los que elige Thorcast, el 60 %. Eso conserva unos US$ 2,8 millones más de prima al año."),
]

VALUE_H = "No todos los clientes valen lo mismo, ni todos se pueden retener"
VALUE = [
    "<strong>Prioriza por valor, no solo por riesgo.</strong> Combinar la probabilidad de fuga con el valor futuro del cliente (CLTV) "
    "pone primero a quienes más valor se llevarían. En un ejemplo ilustrativo de banca, con los mismos 30.000 contactos la oferta "
    "retiene a 1.500 clientes con Thorcast frente a 900 con el modelo actual: unos US$ 270 mil de CLTV conservado al año.",
    "<strong>Busca a quien la acción sí cambia.</strong> Hay clientes que se van a ir hagas lo que hagas y otros que se quedarían igual. "
    "El mejor uso del cupo es contactar a los que una llamada u oferta puede retener, y predecir qué incentivo funciona con cada uno.",
    "<strong>Mide con un grupo de control.</strong> Deja una parte de los clientes de alto riesgo sin contactar. Sin ese grupo no sabes "
    "cuántos se quedaron gracias a la campaña y cuántos se habrían quedado de todas formas.",
]

DEC_H = "Del score a la campaña: capas de decisión"
DEC = (
    "<p>Un modelo de fuga solo crea valor si cambia a quién se contacta. Por eso la última pieza es la regla de decisión: con un cupo "
    "fijo, cuántos contactos hago, a quién y con qué oferta, y cuánto valor conserva cada alternativa.</p>"
    "<p>En Thorcast eso lo resuelven las <strong>capas de decisión</strong>. Las <strong>Thorcast Decision Layers</strong> vienen "
    "preconfiguradas en la app: ingresas la economía de tu campaña y ves el impacto para cada punto de corte. Cuando la regla es propia "
    "de tu operación (un cupo fijo de llamadas por sucursal, ofertas distintas por segmento, costos de contacto por canal), las "
    "<strong>Customized Decision Layers</strong> te permiten describírsela a MJÖ en lenguaje natural para que arme una capa a tu medida, "
    "que tú revisas y apruebas. El resultado queda en el idioma del negocio: cuántos clientes retienes y cuánto valor conservas.</p>"
)

MISTAKES_H = "Errores comunes"
MISTAKES = [
    "Entrenar con una partición al azar en vez de por tiempo: el modelo se ve mejor de lo que va a funcionar.",
    "Definir la fuga con datos que llegan tarde (la baja formal) cuando el cliente ya se había ido meses antes.",
    "Medir con accuracy o con el Gini solamente, sin mirar cuántas fugas caen dentro del cupo de contacto.",
    "Contactar a todos los de alto riesgo con la misma oferta, sin mirar valor ni probabilidad de respuesta.",
    "Lanzar la campaña sin grupo de control y luego no poder demostrar el resultado.",
    "No monitorear el modelo: cambios de precios, de competencia o de mezcla de clientes lo degradan en pocos meses.",
]

FIT_H = "Cómo lo hace Thorcast"
FIT = [
    "<strong>NORA</strong> prepara los datos: le indicas en lenguaje natural qué necesitas (limpiar, unir tablas, construir el target) y propone un plan que tú apruebas; cada paso pasa por un motor de validación determinístico.",
    "<strong>La Data Enrichment Network</strong> convierte un email, un teléfono o una dirección en señales nuevas: más de 3.000 data points, condensados en 261 señales listas para el modelo.",
    "<strong>MJÖ</strong> construye y compara los modelos y presenta el mejor, con métricas estándar y un reporte técnico listo para auditoría.",
    "<strong>Las capas de decisión</strong> convierten el score en una campaña con impacto económico, preconfiguradas o a tu medida.",
    "<strong>Despliegue y monitoreo</strong> en Thorcast Cloud, en tus instalaciones o en la app, con recalibración cuando cambia la población.",
]

FAQ_H = "Preguntas frecuentes"
FAQ = [
    ("¿Qué es un modelo de churn?",
     "Es un modelo predictivo que estima, para cada cliente, la probabilidad de que se vaya en un horizonte definido (por ejemplo, los próximos 90 días). Sirve para ordenar la cartera y decidir a quién contactar primero con las acciones de retención disponibles."),
    ("¿Con cuánta anticipación se puede predecir la fuga?",
     "Depende de la industria y de los datos, pero el objetivo es llegar antes de que el cliente tome la decisión: semanas antes en telco y banca, y antes del vencimiento en seguros generales. Un horizonte demasiado corto deja poco margen para actuar; uno demasiado largo pierde precisión."),
    ("¿Sirve para prepago en telco?",
     "Sí, pero la fuga se define por inactividad (dejar de recargar o de usar) porque no hay una baja formal. Los datos de uso reciente y las señales externas son especialmente útiles cuando el operador tiene poca información del cliente."),
    ("¿Qué es una capa de decisión en una campaña de retención?",
     "Es la regla que convierte el score en a quién contactar, con qué oferta y con qué impacto económico. En Thorcast puedes usar capas preconfiguradas (Thorcast Decision Layers) o pedirle a MJÖ una a la medida de tu operación (Customized Decision Layers)."),
]

MORE_H = "Sigue leyendo"
MORE = [
    ("modelo-churn-fuga-clientes.html", "Modelo de churn: predicción de fuga de clientes con IA (con videos por industria)"),
    ("como-elegir-software-scoring-crediticio.html", "Cómo elegir software de scoring crediticio: guía práctica"),
    ("preguntas-frecuentes.html#gini-uplift", "Resultados de los datos alternativos por país"),
    ("para-quien-es.html", "Para quién es Thorcast.AI"),
    ("tutorials-es.html", "Tutoriales en video"),
]

ABOUT = "Predicción de fuga de clientes (churn)"
