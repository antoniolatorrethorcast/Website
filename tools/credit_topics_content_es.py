"""Guías en español (2026-11-26): optimización del punto de corte y análisis de inferencia de rechazados.
Traducción de credit_topics_content_en.py, con las mismas cifras ilustrativas."""

DATE = "2026-11-26"

CUTOFF = dict(
    FILE="optimizacion-punto-de-corte-credito.html",
    TITLE="Punto de corte en scoring de crédito: cómo optimizarlo — Thorcast.AI",
    DESC=("Cómo fijar el punto de corte de un score de crédito que maximiza la utilidad: PD de equilibrio, ejemplo con "
          "números, tasa de aprobación vs tasa de malos, análisis de swap set, cortes por segmento y cada cuánto revisarlos."),
    H1="Optimización del punto de corte en crédito: cómo fijar el corte que maximiza la utilidad",
    TAG="GUÍA",
    META="Thorcast.AI · Actualizado el 26 de noviembre de 2026 · 9 min de lectura",
    CRUMB="Optimización del punto de corte",
    ABOUT="Optimización del punto de corte de un score de crédito",
    SECTIONS=[
        (None,
         "<p>Un modelo de crédito ordena a los solicitantes por riesgo. El <strong>punto de corte</strong> convierte ese orden "
         "en una decisión: se aprueba a todos los que quedan sobre él y se rechaza al resto. Es el número del proceso de crédito "
         "que más dinero mueve y, muchas veces, el que se elige con menos análisis. Esta guía explica cómo fijarlo con números, "
         "paso a paso, para equipos de riesgo, política de crédito y finanzas de bancos, financieras, fintechs y retail financiero.</p>"
         "<p>Las cifras de los ejemplos son <strong>ilustrativas</strong>: números redondos elegidos para mostrar el método, no "
         "datos de ninguna cartera.</p>"),
        ("Qué decide el punto de corte",
         "<p>Mover el corte cambia un error por otro. Si lo subes, apruebas menos y pierdes menos por mora, pero rechazas a "
         "clientes que habrían pagado. Si lo bajas, ganas más ingresos a cambio de más pérdidas. Los dos números que se suelen "
         "mirar son:</p><ul>"
         "<li><strong>Tasa de aprobación (cut-off rate):</strong> la proporción de solicitantes que queda sobre el corte. Una "
         "tasa de 60 % significa que se aprueban seis de cada diez. Algunos equipos llaman «cut-off rate» a la proporción "
         "rechazada; aclara cuál usas en cada informe.</li>"
         "<li><strong>Tasa de malos de los aprobados:</strong> la proporción de créditos aprobados que se espera caiga en mora "
         "en la ventana de desempeño (por ejemplo, 90 días de mora en 12 meses).</li></ul>"
         "<p>Ninguno de los dos dice dónde parar. La utilidad sí.</p>"),
        ("Paso 1: la probabilidad de incumplimiento de equilibrio",
         "<p>Para un solicitante, aprobar conviene cuando la ganancia esperada supera la pérdida esperada:</p>"
         "<p><strong>Utilidad esperada = (1 − PD) × margen − PD × pérdida</strong></p>"
         "<p>donde <em>PD</em> es la probabilidad de incumplimiento que el modelo asigna, <em>margen</em> es lo que ganas con un "
         "crédito que se paga (intereses y comisiones, menos costo de fondeo y operación) y <em>pérdida</em> es lo que pierdes con "
         "uno que cae en mora (exposición × severidad, neto de recuperos). Si la utilidad esperada es cero, se obtiene la "
         "<strong>PD de equilibrio</strong>:</p>"
         "<p><strong>PD de equilibrio = margen ÷ (margen + pérdida)</strong></p>"
         "<p>Ejemplo ilustrativo: un crédito de 1.000 deja un margen de 150 si se paga y una pérdida de 650 si cae en mora. La PD "
         "de equilibrio es 150 ÷ 800 = 18,75 %. Cada solicitante con PD menor a 18,75 % suma utilidad esperada; cada uno sobre "
         "ese valor la resta. El corte óptimo es el score donde la PD cruza esa línea, siempre que el modelo esté calibrado.</p>"),
        ("Paso 2: un ejemplo con números",
         "<p>Supón 10.000 solicitantes repartidos en cinco tramos de riesgo de 2.000 cada uno, con la misma economía de arriba "
         "(cifras ilustrativas):</p>"
         "<div class=\"cmp-wrap\"><table class=\"cmp-table\"><thead><tr><th>Tramos aprobados</th><th>Tasa de aprobación</th>"
         "<th>Tasa de malos de los aprobados</th><th>Utilidad esperada</th></tr></thead><tbody>"
         "<tr><td>Solo A (PD 2 %)</td><td>20 %</td><td>2,0 %</td><td>268.000</td></tr>"
         "<tr><td>A–B (PD hasta 5 %)</td><td>40 %</td><td>3,5 %</td><td>488.000</td></tr>"
         "<tr><td>A–C (PD hasta 10 %)</td><td>60 %</td><td>5,7 %</td><td>628.000</td></tr>"
         "<tr><td>A–D (PD hasta 18 %)</td><td>80 %</td><td>8,8 %</td><td><strong>640.000</strong></td></tr>"
         "<tr><td>Todos (PD hasta 32 %)</td><td>100 %</td><td>13,4 %</td><td>428.000</td></tr>"
         "</tbody></table></div>"
         "<p>La utilidad es máxima al aprobar los tramos A a D. El tramo D aporta muy poco (12.000 en 2.000 créditos) porque su "
         "PD de 18 % está justo bajo el equilibrio de 18,75 %; el tramo E, con 32 %, pierde 212.000. De ahí salen dos lecciones:</p><ul>"
         "<li>Los tramos cercanos al equilibrio casi no cambian la utilidad, pero sí el volumen y el riesgo. Ahí entran el "
         "apetito de riesgo, el capital y la estrategia.</li>"
         "<li>El óptimo es frágil. Si la pérdida por mora sube de 650 a 700, la PD de equilibrio baja a 17,6 % y el tramo D pasa "
         "a ser negativo: el mejor corte sube a A–C. El corte tiene que seguir a la economía, no al revés.</li></ul>"),
        ("Paso 3: revisa las restricciones",
         "<p>El corte que maximiza la utilidad es el punto de partida, no la respuesta final. Antes de fijarlo, revisa:</p><ul>"
         "<li><strong>Apetito de riesgo:</strong> la tasa de malos o la pérdida esperada máxima que aprobó el directorio.</li>"
         "<li><strong>Capital y fondeo:</strong> cuánto volumen soporta el balance.</li>"
         "<li><strong>Metas de volumen:</strong> el crecimiento puede justificar aprobar a propósito un tramo marginal, con su costo explícito.</li>"
         "<li><strong>Regulación y trato justo:</strong> reglas de capacidad de pago, crédito responsable y explicación de rechazos.</li>"
         "<li><strong>Calibración:</strong> la lógica del equilibrio solo funciona si una PD de 10 % significa de verdad unas 10 "
         "moras de cada 100. Revisa la calibración con datos recientes y fuera del periodo de entrenamiento.</li></ul>"),
        ("Paso 4: análisis de swap set al cambiar de modelo",
         "<p>Cuando un modelo nuevo reemplaza al actual, compara las dos políticas solicitante por solicitante, con la misma "
         "tasa de aprobación:</p><ul>"
         "<li><strong>Swap-ins:</strong> solicitantes que el modelo nuevo aprueba y el antiguo rechazaba.</li>"
         "<li><strong>Swap-outs:</strong> solicitantes que el modelo antiguo aprobaba y el nuevo rechaza.</li></ul>"
         "<p>El modelo nuevo es mejor si los swap-ins son menos riesgosos que los swap-outs. El problema: solo observas el "
         "desempeño de los swap-outs, porque los swap-ins fueron rechazados. Su desempeño hay que estimarlo, que es justamente "
         "lo que hace la <a href=\"analisis-inferencia-de-rechazados.html\">inferencia de rechazados</a>, o medirlo con una "
         "prueba controlada y acotada bajo el corte antiguo.</p>"),
        ("Paso 5: un corte o varios",
         "<p>Un solo corte supone que todos los solicitantes tienen la misma economía. Muchas veces no es así: márgenes, montos y "
         "recuperos cambian por producto, canal y segmento. Fijar un corte por segmento, cada uno con su propia PD de equilibrio, "
         "suele sumar utilidad con el mismo riesgo total. Mantén pocos segmentos, para poder explicarlos y monitorearlos, y "
         "documenta por qué existe cada uno.</p>"),
        ("Paso 6: revísalo con una frecuencia fija",
         "<p>Un corte óptimo hace seis meses puede no serlo hoy. Revísalo cuando cambien el costo de fondeo, los precios, la "
         "severidad de las pérdidas, la mezcla de solicitantes o el escenario macroeconómico, y al menos cada trimestre. "
         "Monitorea la tasa de aprobación, la mora temprana de las cosechas recientes y la calibración del score: un desvío en "
         "cualquiera de ellas es la señal para recalcular el corte.</p>"),
        ("Errores frecuentes",
         "<ul><li>Elegir el corte por tasa de aprobación («aprobamos el 60 %») sin relación con la economía.</li>"
         "<li>Usar un score sin calibrar como si fuera una probabilidad.</li>"
         "<li>Medir la política nueva solo sobre los solicitantes que aprobaba la antigua.</li>"
         "<li>Mantener el mismo corte después de que cambian los precios o el costo de fondeo.</li>"
         "<li>Fijar el corte en una planilla que nadie puede auditar después.</li></ul>"),
        ("Cómo se hace en Thorcast",
         "<p>En Thorcast, el paso del score a la decisión se hace con <strong>capas de decisión</strong>. Las "
         "<strong>Thorcast Decision Layers</strong> preconfiguradas incluyen el punto de corte de originación: ingresas la "
         "economía de tu política, como lo que ganas con un crédito que se paga y lo que pierdes con uno que cae en mora, y ves "
         "aprobación, riesgo y utilidad en cada corte, lado a lado. Cuando la decisión no calza con una capa estándar, por "
         "ejemplo reglas distintas por segmento, se la describes a MJÖ en lenguaje natural y el agente arma una "
         "<strong>Customized Decision Layer</strong> que tú revisas y apruebas.</p>"
         "<p>Así el corte se recalcula con los mismos supuestos cada vez que cambia la economía, y los supuestos y resultados "
         "quedan documentados para el comité de riesgo y el validador.</p>"),
    ],
    FAQ=[
        ("¿Qué es el punto de corte de un score de crédito?",
         "Es el umbral de score que separa a los solicitantes que se aprueban de los que se rechazan. Quienes quedan sobre el "
         "corte se aprueban, o pasan a la siguiente etapa del proceso; el resto se rechaza."),
        ("¿Qué es el cut-off rate?",
         "Normalmente, la tasa de aprobación en un punto de corte: la proporción de solicitantes que queda sobre él. Algunos "
         "equipos lo usan para la proporción rechazada, así que conviene poner siempre la definición junto al número."),
        ("¿Cómo se calcula el punto de corte óptimo?",
         "Calcula la PD de equilibrio, margen ÷ (margen + pérdida), y aprueba a los solicitantes cuya PD calibrada esté bajo ese "
         "valor. Después ajusta por apetito de riesgo, capital, metas de volumen y regulación, y revisa el resultado con una "
         "tabla de utilidad por tramo de score."),
        ("¿Cada cuánto hay que revisar el punto de corte?",
         "Cada vez que cambia la economía (precios, costo de fondeo, severidad) o la mezcla de solicitantes, y al menos cada "
         "trimestre. La tasa de aprobación, la mora temprana y la calibración indican cuándo recalcularlo."),
        ("¿Qué relación hay entre el punto de corte y la inferencia de rechazados?",
         "Bajar el corte significa aprobar a solicitantes que la política anterior rechazaba y cuyo desempeño nunca se observó. "
         "La inferencia de rechazados estima cómo se habrían comportado, para que el nuevo corte no se fije sobre una muestra sesgada."),
    ],
    MORE=[
        ("analisis-inferencia-de-rechazados.html", "Análisis de inferencia de rechazados: guía paso a paso"),
        ("blog-12-es.html", "Inferencia de rechazados (reject inference) en credit scoring"),
        ("blog-03.html", "Beyond the score: why the cutoff decision is where the money is (en inglés)"),
        ("como-elegir-software-scoring-crediticio.html", "Cómo elegir software de scoring crediticio"),
        ("scoring-crediticio-ia.html", "Scoring crediticio con IA y datos alternativos"),
        ("tutorials-es.html", "Tutoriales en video"),
    ],
)

REJECT = dict(
    FILE="analisis-inferencia-de-rechazados.html",
    TITLE="Inferencia de rechazados en scoring: guía paso a paso — Thorcast.AI",
    DESC=("Cómo hacer un análisis de inferencia de rechazados (reject inference) en scoring de crédito: datos necesarios, "
          "ejemplo de parcelling con números, elección del método, validación y qué documentar."),
    H1="Análisis de inferencia de rechazados: guía paso a paso con un ejemplo",
    TAG="GUÍA",
    META="Thorcast.AI · Actualizado el 26 de noviembre de 2026 · 9 min de lectura",
    CRUMB="Análisis de inferencia de rechazados",
    ABOUT="Inferencia de rechazados en scoring de crédito",
    SECTIONS=[
        (None,
         "<p>Un score de originación aprende de los créditos que otorgaste, pero se aplica a todos los que postulan. La "
         "<strong>inferencia de rechazados</strong> (reject inference) estima cómo se habrían comportado los solicitantes "
         "rechazados, para que el modelo nuevo no aprenda solo de quienes dejó pasar la política anterior. Nuestro artículo sobre "
         "<a href=\"blog-12-es.html\">métodos y errores de la inferencia de rechazados</a> explica por qué existe el problema y "
         "las técnicas principales. Esta guía es la parte práctica: cómo hacer el análisis, paso a paso, con un ejemplo.</p>"
         "<p>Las cifras del ejemplo son <strong>ilustrativas</strong>, elegidas para mostrar el método.</p>"),
        ("Paso 1: arma la muestra de todos los solicitantes",
         "<p>Necesitas todas las solicitudes del periodo, no solo los créditos:</p><ul>"
         "<li>Un identificador y la fecha de la solicitud.</li>"
         "<li>La <strong>decisión</strong>: aprobada o rechazada. Separa a quienes fueron aprobados pero no tomaron el crédito: "
         "no son ni buenos ni malos.</li>"
         "<li>El <strong>desempeño</strong> de los aprobados, con una definición y ventana fijas (por ejemplo, 90 días de mora "
         "en 12 meses).</li>"
         "<li>Las mismas variables para aprobados y rechazados, tomadas al momento de la solicitud.</li></ul>"
         "<p>Si los rechazados no tienen las variables, o se filtraron del data warehouse, la inferencia no es posible. "
         "Corregir esa falta de datos es el primer entregable.</p>"),
        ("Paso 2: construye el score preliminar",
         "<p>Entrena un modelo solo con los aprobados (el modelo de «buenos y malos conocidos») o usa un score existente en el "
         "que confíes. Su trabajo es ordenar a los rechazados por riesgo. Comprueba que ordena bien en una muestra de aprobados "
         "fuera del periodo de entrenamiento antes de inferir nada con él.</p>"),
        ("Paso 3: infiere el desempeño (ejemplo de parcelling)",
         "<p>Asigna un score a todos, aprobados y rechazados, y agrúpalos en tramos de riesgo. En cada tramo, toma la tasa de "
         "malos observada de los aprobados y asígnales a los rechazados una tasa mayor, porque dentro del mismo tramo suelen "
         "ser más riesgosos. Aquí el factor de ajuste es 1,5:</p>"
         "<div class=\"cmp-wrap\"><table class=\"cmp-table\"><thead><tr><th>Tramo</th><th>Aprobados</th>"
         "<th>Tasa de malos observada</th><th>Rechazados</th><th>Tasa de malos inferida (×1,5)</th><th>Malos inferidos</th></tr></thead><tbody>"
         "<tr><td>1 (menor riesgo)</td><td>4.000</td><td>2 %</td><td>200</td><td>3 %</td><td>6</td></tr>"
         "<tr><td>2</td><td>3.000</td><td>4 %</td><td>400</td><td>6 %</td><td>24</td></tr>"
         "<tr><td>3</td><td>2.000</td><td>7 %</td><td>800</td><td>10,5 %</td><td>84</td></tr>"
         "<tr><td>4</td><td>800</td><td>12 %</td><td>1.200</td><td>18 %</td><td>216</td></tr>"
         "<tr><td>5 (mayor riesgo)</td><td>200</td><td>20 %</td><td>1.400</td><td>30 %</td><td>420</td></tr>"
         "<tr><td>Total</td><td>10.000</td><td>4,8 %</td><td>4.000</td><td>18,8 %</td><td>750</td></tr>"
         "</tbody></table></div>"
         "<p>Con <em>parcelling</em>, 750 de los 4.000 rechazados se marcan como malos, al azar dentro de cada tramo y en esas "
         "proporciones, y el resto como buenos. Con <em>fuzzy augmentation</em>, cada rechazado entra dos veces, una como bueno "
         "y otra como malo, ponderado por las probabilidades inferidas. En ambos casos la muestra de entrenamiento pasa de "
         "10.000 a 14.000 registros y su tasa de malos sube de 4,8 % a 8,8 %, más cerca de la población que el modelo va a evaluar.</p>"),
        ("Paso 4: elige el método",
         "<div class=\"cmp-wrap\"><table class=\"cmp-table\"><thead><tr><th>Situación</th><th>Opción razonable</th></tr></thead><tbody>"
         "<tr><td>Pocos rechazos, o la política anterior fue casi aleatoria en la zona que te importa</td><td>Entrenar solo con aprobados y documentar por qué</td></tr>"
         "<tr><td>Un score preliminar confiable y suficientes solicitantes por tramo</td><td>Parcelling</td></tr>"
         "<tr><td>Prefieres llevar la incertidumbre en vez de forzar etiquetas</td><td>Fuzzy augmentation</td></tr>"
         "<tr><td>Hay datos de buró de rechazados que obtuvieron crédito en otra entidad</td><td>Usar primero ese desempeño real e inferir solo el resto</td></tr>"
         "<tr><td>Es posible una prueba controlada y acotada bajo el corte</td><td>Hacerla: el desempeño observado vale más que cualquier inferencia</td></tr>"
         "</tbody></table></div>"),
        ("Paso 5: fija los parámetros con cuidado",
         "<ul><li><strong>Tramos:</strong> los tramos por cuantiles mantienen tamaños parejos; los de igual ancho siguen la "
         "escala del score. Fija un mínimo de registros por tramo.</li>"
         "<li><strong>Factor de ajuste:</strong> justifícalo con lo que el negocio sabe de los rechazados, o con datos de buró. "
         "Prueba un rango, no un solo valor.</li>"
         "<li><strong>Peso de la población rechazada:</strong> controla cuánto mueve la inferencia al modelo final.</li>"
         "<li><strong>Calibración y topes:</strong> calibra las probabilidades preliminares (Platt o regresión isotónica) y pon "
         "topes a los valores extremos para que no dominen.</li></ul>"),
        ("Paso 6: valida el resultado",
         "<p>La inferencia no se puede validar con los propios registros inferidos. Estas son las pruebas que un analista o "
         "validador debería ver:</p><ul>"
         "<li><strong>Medir solo con desempeño real.</strong> Los registros inferidos van al entrenamiento, nunca a la muestra "
         "de prueba ni a un fold de prueba de la validación cruzada.</li>"
         "<li><strong>Comparar con el modelo de solo aprobados</strong> en la misma muestra de prueba fuera de periodo: el "
         "desempeño no debería caer y el orden de los aprobados debería mantenerse estable.</li>"
         "<li><strong>Revisar la tasa de malos inferida:</strong> mayor que la de los aprobados en cada tramo, creciente con el "
         "riesgo y coherente con la evidencia de buró que haya.</li>"
         "<li><strong>Sensibilidad:</strong> repetir con otros factores y pesos. Si el modelo final cambia mucho, la inferencia "
         "está definiendo el resultado y necesita una justificación más sólida.</li>"
         "<li><strong>Revisión del swap set:</strong> mirar a quiénes aprobaría el modelo nuevo que el antiguo rechazaba, con la "
         "misma tasa de aprobación. Ahí es donde importa la inferencia, y donde se toma la "
         "<a href=\"optimizacion-punto-de-corte-credito.html\">decisión del punto de corte</a>.</li></ul>"),
        ("Paso 7: documenta la decisión",
         "<p>La validación del modelo va a preguntar por qué el modelo aprueba perfiles que la política anterior rechazaba. "
         "Deja por escrito la población rechazada usada, el score preliminar, el método y sus parámetros, la tasa de malos "
         "inferida por tramo, la comparación con el modelo de solo aprobados y las razones de la elección final, incluida la "
         "decisión de no usar inferencia.</p>"),
        ("Cómo se hace en Thorcast",
         "<p>En Thorcast, la inferencia de rechazados es un paso opcional entre la preparación de datos y el modelamiento. "
         "Aparece cuando el objetivo es binario y se declaró una población rechazada, con una columna de estado de aprobación. "
         "Permite parcelling y fuzzy augmentation, con el score preliminar generado automáticamente o tomado de un score "
         "existente, y ajustes de tramos, método de tramos, mínimo de registros por tramo, peso de la población rechazada, "
         "topes de probabilidad y calibración.</p>"
         "<p>Antes de cambiar nada, una vista previa compara el dataset de solo aprobados con el aumentado: registros, malos "
         "observados, malos inferidos, tasas de malos y un resumen por tramo, con advertencias. Tú decides si lo usas. Las filas "
         "inferidas se usan solo para entrenar, así que todas las métricas se calculan con desempeño real.</p>"),
    ],
    FAQ=[
        ("¿Qué significa «rechazado por scoring»?",
         "Significa que la solicitud se rechazó porque el score de crédito quedó bajo el punto de corte de la entidad. El score "
         "estima el riesgo de no pagar a partir de los datos del solicitante; cada entidad fija su propio corte, por eso la "
         "misma persona puede ser rechazada en una y aprobada en otra."),
        ("¿Qué es el análisis de inferencia de rechazados?",
         "Es el proceso de estimar cómo se habrían comportado los solicitantes de crédito rechazados y sumarlos a los datos de "
         "entrenamiento, para corregir el sesgo de una muestra formada solo por créditos aprobados."),
        ("¿Qué método de inferencia de rechazados es mejor?",
         "No hay uno que gane siempre. Parcelling y fuzzy augmentation son los más usados porque se pueden explicar. El "
         "desempeño real, de buró o de una prueba controlada, supera a cualquier inferencia cuando se puede obtener."),
        ("¿La inferencia de rechazados siempre mejora el modelo?",
         "No. Reemplaza desempeños que faltan por supuestos, y la evidencia académica sobre sus beneficios es mixta. Úsala como "
         "una decisión documentada y probada, y compárala con el modelo de solo aprobados sobre desempeño real."),
        ("¿Se pueden usar los registros inferidos para medir el modelo?",
         "No. Van solo al entrenamiento. Medir un modelo con desempeños inferidos es evaluarlo con sus propios supuestos."),
    ],
    MORE=[
        ("blog-12-es.html", "Inferencia de rechazados (reject inference) en credit scoring"),
        ("optimizacion-punto-de-corte-credito.html", "Optimización del punto de corte en crédito"),
        ("como-elegir-software-scoring-crediticio.html", "Cómo elegir software de scoring crediticio"),
        ("scoring-crediticio-ia.html", "Scoring crediticio con IA y datos alternativos"),
        ("tutorials-es.html", "Tutoriales en video"),
    ],
)
