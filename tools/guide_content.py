"""Guía en español: cómo elegir software de scoring crediticio (2026-11-24).
Hechos de terceros = los ya verificados para las comparativas (tools/compare_content.py, 23/11/2026).
Hechos de Thorcast = lo que thorcast.ai ya publica. No publicar precios aquí."""

FILE = "como-elegir-software-scoring-crediticio.html"
DATE = "2026-11-24"

TITLE = "Cómo elegir software de scoring crediticio: guía 2026 — Thorcast.AI"
DESC = ("Guía práctica para elegir software de scoring crediticio: los cinco tipos de herramientas, diez criterios de evaluación, "
        "cómo hacer una prueba de concepto justa y las señales de alerta.")
H1 = "Cómo elegir software de scoring crediticio: guía práctica 2026"
TAG = "GUÍA"
META = "Thorcast.AI · Actualizada el 24 de noviembre de 2026 · 9 min de lectura"
CRUMB = "Cómo elegir software de scoring crediticio"

INTRO = (
    "<p>Elegir una herramienta de scoring crediticio es una decisión que dura años: define qué tan rápido puedes "
    "lanzar un modelo nuevo, cuánto riesgo aceptas en cada aprobación y qué tan fácil es explicarle cada decisión a tu "
    "regulador. Esta guía es para equipos de riesgo, analítica y crédito de bancos, financieras, fintechs, retail "
    "financiero, aseguradoras y telcos que están comparando opciones.</p>"
    "<p><strong>Transparencia:</strong> esta guía la escribe Thorcast.AI, que es uno de los proveedores. Por eso "
    "decimos en qué casos encaja Thorcast y en cuáles conviene otra herramienta. Los datos de otros proveedores salen de "
    "sus propios sitios y documentación, revisados en noviembre de 2026, y enlazamos las fuentes en nuestras comparativas.</p>"
)

BEFORE_H = "Antes de mirar proveedores: define el problema"
BEFORE = [
    ("Qué decisión quieres mejorar", "Originación, comportamiento (aumentos de cupo, renovaciones), cobranza o fraude en solicitudes. Cada una tiene datos, horizontes y métricas distintas; una herramienta buena para una no siempre lo es para otra."),
    ("Cuál es tu punto de partida", "Un score de buró, un scorecard propio, reglas manuales o nada. Lo que tienes hoy es el modelo contra el que vas a comparar todo lo nuevo."),
    ("Quién va a operar la herramienta", "Un equipo de data science con experiencia, analistas de riesgo que no programan o una mezcla. Es la pregunta que más descarta opciones."),
    ("Dónde deben vivir los datos", "Nube del proveedor, tu nube o tus propios servidores. Si tus políticas no permiten que los datos salgan, descártalo desde el inicio."),
    ("Qué te exige el regulador", "Documentación de desarrollo y validación, explicación de cada rechazo, monitoreo periódico. Pide ejemplos reales de esos entregables, no solo la promesa."),
]

TYPES_H = "Los cinco tipos de herramientas"
TYPES_P = "<p>Casi todo lo que vas a encontrar cae en una de estas cinco familias. Cada una tiene un lugar; el error más común es comparar herramientas de familias distintas como si resolvieran lo mismo.</p>"
TYPES = [
    ("1. Desarrollo propio en Python o R",
     "Tu equipo construye con librerías de código abierto (por ejemplo scikit-learn, LightGBM, XGBoost u OptBinning para scorecards).",
     "Control total y costo de licencias cero.",
     "Todo depende de las personas: preparación de datos, documentación, despliegue y monitoreo hay que construirlos y mantenerlos. Los plazos se miden en meses.",
     "tienes un equipo de data science sólido y estable, y tiempo para construir la plataforma alrededor de los modelos."),
    ("2. Suites estadísticas tradicionales",
     'El ejemplo más conocido es SAS (Viya y Risk Modeling), con agrupación interactiva, weight of evidence, inferencia de rechazados y documentación automática.',
     "El estándar con el que muchos validadores y reguladores están familiarizados; máximo control sobre el scorecard clásico.",
     "Requiere un equipo formado en la herramienta; el ciclo completo de un modelo nuevo suele tomar semanas o meses.",
     'tu gobierno de modelos ya está construido sobre esa suite. Ver <a href="thorcast-vs-sas-es.html">Thorcast.AI vs SAS Viya</a>.'),
    ("3. Plataformas de AutoML y machine learning empresarial",
     'Por ejemplo DataRobot y H2O.ai: entrenan y comparan muchos algoritmos, explican predicciones y despliegan modelos para muchos casos de uso.',
     "Mucha potencia de modelamiento y gobierno para equipos de data science que manejan varios proyectos de IA.",
     "Están pensadas sobre todo para data scientists, y en su documentación no encontramos datos de terceros incluidos: los datos los aportas tú.",
     'tienes un equipo de data science con experiencia y pipelines de datos existentes. Ver <a href="thorcast-vs-datarobot-es.html">vs DataRobot</a> y <a href="thorcast-vs-h2o-es.html">vs H2O.ai</a>.'),
    ("4. Scores y motores de decisión de burós y proveedores de originación",
     "Scores genéricos de buró y motores de reglas para ejecutar la política de crédito en tiempo real.",
     "Rápidos de poner en marcha y con datos de buró incluidos.",
     "Un score genérico no aprende de tu cartera ni de tus clientes; personalizarlo suele ser un proyecto aparte.",
     "necesitas empezar a decidir ya, con poco historial propio, o ya tienes el modelo y te falta el motor para ejecutarlo."),
    ("5. Plataformas de analítica predictiva con agentes de IA y datos incluidos",
     "La categoría más nueva, donde está Thorcast.AI: agentes de IA que preparan los datos y construyen los modelos a partir de instrucciones en lenguaje natural, con datos alternativos incluidos y capas de decisión con impacto económico.",
     "Del dato crudo a un modelo en producción en horas, sin necesitar un gran equipo de data science.",
     "Son más nuevas que las suites tradicionales; pide ver los reportes técnicos y prueba con tus propios datos antes de decidir.",
     'quieres modelos propios de nivel productivo, sumar datos alternativos y cubrir más casos con el mismo equipo. Ver <a href="para-quien-es.html">para quién es Thorcast.AI</a>.'),
]

CRIT_H = "Diez criterios para evaluar, y qué preguntarle a cada proveedor"
CRIT = [
    ("Desempeño fuera de muestra", "¿Qué Gini y KS obtiene en una partición temporal (cosechas posteriores al entrenamiento), no solo en una muestra aleatoria?",
     "Solo muestran resultados de entrenamiento o de una partición aleatoria."),
    ("Datos alternativos", "¿Qué datos además de los míos puede sumar, con qué cobertura en mi país y con qué base legal?",
     "Hablan de “miles de variables” sin decir la cobertura en tu país."),
    ("Explicabilidad", "¿Cómo explico un rechazo puntual? ¿Qué entrega para la validación del modelo?",
     "No hay un reporte técnico de ejemplo que puedas ver antes de comprar."),
    ("Reproducibilidad", "Si entreno dos veces con los mismos datos, ¿obtengo el mismo modelo? ¿Queda el código o el plan versionado?",
     "Resultados que cambian entre ejecuciones sin explicación."),
    ("Del score a la decisión", "¿Puedo ver aprobación, riesgo y utilidad para cada punto de corte?",
     "Entregan un score y la política “la defines tú” en una planilla aparte."),
    ("Preparación de datos", "¿Quién une y limpia las tablas de origen, y cuánto tiempo toma?",
     "La demo empieza con un dataset ya limpio y nunca con tus tablas reales."),
    ("Despliegue y dónde viven los datos", "¿Nube, tu nube o tus servidores? ¿El scoring puede correr en mi infraestructura?",
     "Una sola opción de despliegue que no cumple tus políticas."),
    ("Monitoreo y recalibración", "¿Cómo detecto que el modelo se degradó y cuánto cuesta recalibrarlo?",
     "El monitoreo es un módulo aparte o un proyecto de integración."),
    ("Quién lo opera", "¿Un analista de riesgo que no programa puede construir y mantener un modelo?",
     "Cada cambio requiere a un data scientist o al proveedor."),
    ("Costo total", "Licencias, datos, integración, infraestructura y horas de tu equipo durante tres años.",
     "Solo cotizan la licencia y los datos se cobran aparte, por proveedor."),
]

POC_H = "Cómo hacer una prueba de concepto justa"
POC = [
    "<strong>Usa tu propia muestra.</strong> Con un identificador, el resultado real (por ejemplo, mora a 90 días) y tu score actual. Si incluyes email, teléfono y dirección, también puedes medir el aporte de los datos alternativos.",
    "<strong>Parte por tiempo, no al azar.</strong> Entrena con las solicitudes más antiguas y mide en las más recientes. Es lo más parecido a cómo va a funcionar el modelo en producción.",
    "<strong>Compara contra lo que tienes hoy.</strong> El desafiante tiene que ganarle a tu score actual en la misma muestra de prueba (Campeón–Desafiante), no a un modelo de referencia elegido por el proveedor.",
    "<strong>Revisa las variables.</strong> Cualquier variable que se conoce después de otorgar el crédito (pagos, cobranza, estado de la cuenta) es una fuga de información e infla el resultado.",
    "<strong>Mide en dinero.</strong> Además del Gini, pide la tasa de aprobación y la mora esperada en el punto de corte que usarías, y lo que eso significa en utilidad.",
    "<strong>Pide los entregables.</strong> El reporte técnico, el código o plan reproducible y cómo se desplegaría. Si no pasa la validación interna, el mejor Gini no sirve.",
]

FLAGS_H = "Señales de alerta"
FLAGS = [
    "Un Gini muy por encima de lo habitual en tu cartera: más a menudo es una fuga de información que un modelo extraordinario.",
    "Resultados sin partición temporal ni comparación contra tu modelo actual.",
    "Datos alternativos sin cobertura documentada en tu país.",
    "Una caja negra sin explicación por solicitud ni documentación para el validador.",
    "Rankings de “los 10 mejores” sin metodología: algunos sitios cobran por la posición y no marcan qué productos pagaron. Úsalos como lista inicial, nunca como evaluación.",
]

FIT_H = "Dónde encaja Thorcast.AI, y dónde no"
FIT_P = "<p>Thorcast.AI es una plataforma de analítica predictiva con agentes de IA. Para scoring crediticio, conviene cuando:</p>"
NOT_FIT = [
    "Tu gobierno de modelos está construido sobre SAS y tus validadores esperan sus entregables: ahí SAS es lo más natural.",
    "Tu equipo de data science quiere una plataforma para construir y gobernar muchos tipos de IA y agentes propios: mira DataRobot o H2O.ai.",
    "Solo necesitas un score genérico y un motor de reglas para decidir mañana, sin construir un modelo propio.",
]
NOT_FIT_P = "<p>Puede no ser la mejor opción si:</p>"

FAQ_H = "Preguntas frecuentes"
FAQ = [
    ("¿Qué es un software de scoring crediticio?",
     "Es la herramienta con la que se construye, valida, despliega y monitorea el modelo que estima la probabilidad de que un cliente no pague. Puede ir desde librerías de código abierto hasta plataformas que cubren todo el ciclo, desde los datos hasta la decisión."),
    ("¿Machine learning o scorecard tradicional?",
     "Depende de lo que te exija la validación. Los modelos de machine learning suelen discriminar mejor; un scorecard es más fácil de explicar variable por variable. Lo práctico es probar ambos con tus datos y elegir con el desempeño fuera de muestra y los requisitos de explicabilidad sobre la mesa."),
    ("¿Cuánto mejoran los datos alternativos un modelo de crédito?",
     "Depende del país, del segmento y de los datos que ya tengas. En la experiencia del equipo fundador de Thorcast, en 68 modelos de 12 países, sumar datos alternativos subió el Gini en una mediana de 35 %. La única forma de saberlo para tu cartera es medirlo en una prueba de concepto."),
    ("¿Cuánto toma una prueba de concepto?",
     "Con herramientas tradicionales suele ser un proyecto de semanas. Con Thorcast, una prueba de concepto con tu propia muestra toma alrededor de una hora: se enriquece la muestra, se entrena un modelo desafiante y se compara con tu score actual."),
]

MORE_H = "Sigue leyendo"
MORE = [
    ("scoring-crediticio-ia.html", "Modelo de scoring crediticio con IA y datos alternativos"),
    ("preguntas-frecuentes.html#gini-uplift", "Resultados de los datos alternativos por país"),
    ("blog-12-es.html", "Inferencia de rechazados en credit scoring"),
    ("thorcast-vs-datarobot-es.html", "Thorcast.AI vs DataRobot"),
    ("thorcast-vs-h2o-es.html", "Thorcast.AI vs H2O.ai"),
    ("thorcast-vs-sas-es.html", "Thorcast.AI vs SAS Viya"),
    ("para-quien-es.html", "Para quién es Thorcast.AI"),
    ("tutorials-es.html", "Tutoriales en video"),
]
