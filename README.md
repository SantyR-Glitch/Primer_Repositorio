# Propuesta de Proyecto: 
# Calculadora y Analizador de Eficiencia Energética en el Transporte.
# Santiago Alexander Rosales Avendaño

# 1. Descripción General del Proyecto:
El proyecto consiste en el desarrollo de un programa interactivo en Python diseñado para calcular, comparar y analizar el consumo energético y las emisiones asociadas a distintos medios de transporte (como vehículos de combustión interna, vehículos eléctricos y bicicletas) en trayectos determinados. 
La herramienta ofrecerá al usuario una opción clara que procesa valores de entrada y mecánicas para devolver una comparación sobre el rendimiento y el impacto ambiental de cada alternativa.

# 2. Problemática a Resolver:
En la actualidad, la toma de decisiones sobre qué usar para el transporte suele ser sin ser clara sobre el gasto energético real y sus emisiones contaminantes.
Así como la inspiración en mi clase de “Perspectivas innovadoras en la ingeniería” porque al momento de estar realizando este proyecto sobre calcular y comparar el consumo energético y las emisiones de una bicicleta contra otros vehículos no fue tan sencillo hacer los cálculos al tener que usar otros medios como excel sin estar tan familiarizados.

# Problemas más específicos de este proyecto que busca resolver:
-Falta de visibilidad sobre el consumo real: Dificultad para comparar métricas (como litros de gasolina, kilovatios-hora de electricidad o calorías humanas) en una misma unidad estándar de energía (Julios o kWh).

-Evaluación del impacto ambiental: Desconocimiento de la cantidad exacta de emisiones de dióxido de carbono (CO2) generadas por un usuario o por kilómetro recorrido según la eficiencia del vehículo.

-Toma de decisiones no optimizada: Ausencia de una herramienta accesible que permita evaluar qué medio de transporte es más eficiente en función de variables como la distancia y el peso transportado.

# 3. Propuesta de Solución (¿Cómo se va a resolver?)
La solución será mediante un algoritmo en Python con las siguientes etapas:

- Captura y validación de datos:
El programa solicitará al usuario datos del trayecto (distancia en km, inclinación o peso adicional) y del vehículo (tipo de combustible, rendimiento medio o capacidad de batería).

- Procesamiento de fórmulas mecánicas y energéticas:
Mediante funciones, se estandarizarán todas las unidades de entrada a Julios (J) o Kilovatios-hora (kWh).
Se aplicará conversión de energía química/eléctrica a trabajo mecánico, calculando el consumo total y la eficiencia en unidades de energía por kilómetro (kWh/km).
Se calcularán las emisiones estimadas de CO2 utilizando factores de emisión ya estandarizados para cada fuente energética.

- Generación de reportes y comparación:
El sistema procesa los resultados y generará en la consola un reporte usando la precisión a 2 o 3 decimales para garantizar información clara.
Mostrará un análisis comparativo que identifique el medio más eficiente para el trayecto ingresado y el porcentaje de ahorro energético o de reducción de emisiones respecto a las alternativas.
