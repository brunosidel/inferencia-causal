# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.17.1
#   kernelspec:
#     display_name: global
#     language: python
#     name: python3
# ---

# %%
import math
import random
import inspect
import warnings

respuestas = {}

# %% [markdown]
# # 1 - Preguntas sobre fundamentos
#
# Este notebook contiene una lista de preguntas junto con una lista exhaustiva de respuestas mutuamente contradictorias. A diferencia de los enunciados de
# tipo "multiple choise" en los que se pide seleccionar una única opción, aquí se pide que distribuyan creencias entre las diferentes opciones, asegurándose
# que el valor asignado sea positivo y la suma sea 1. La evaluación será el producto de las creencias asiganadas a las respuestas correctas.
# En caso de que la respuesta sea una variable aleatoria, se considerará la predicción típica a largo plazo, es decir, su media gométrica.
# Notar que un único cero en la secuencia anula todo el producto. Por ello, en caso de duda, no conviene que concentren toda su creencia en una sola opción,
# sino distribuir algo de creencia en todas las opciones que consideran posibles. Noten también que conviene asignar más a la opción en la que más creen,
# porque distribuir creencias en partes iguales entre todas las opciones no es mucho mejor que el azar (baseline).

# %% [markdown]
# ### 1.0 Moneda
#
# ¿Cuál será el resultado del lanzamiento de una moneda?
#
# 0. Cara
# 0. Sello

# %%
respuestas[(1, 0, "Moneda")] = [
    0.5,  # 0. Cara
    0.5,  # 1. Sello
    ""
]

# %% [markdown]
# ### 1.1 Cajas
#
# Hay tres cajas idénticas. Detrás de una de ellas hay un regalo. El resto están vacías. ¿Dónde está el regalo?
#
# 0. Caja 0
# 1. Caja 1
# 2. Caja 2
# 3. Otro lugar

# %%
respuestas[(1, 1, "Cajas")] = [
    0.3,  # 0. Caja 0
    0.3,  # 1. Caja 1
    0.4,  # 2. Caja 2
    0,  # 3. Otro lugar
    ""
]

# %% [markdown]
# ### 1.2 Mentir
#
# ¿Cuál de todas las opciones se considera una definición matemática del principio de no mentir?
#
# 0. Maxima incertidumbre (entropía)
# 0. Minima incertidumbre (entropía)
# 0. Maxima incertidumbre (entropía) dada la información disponible (restricciones)
# 0. Minima incertidumbre (entropía) dada la información disponible (restricciones)
# 0. Ninguna de las anteriores

# %%
respuestas[(1, 2, "Mentir")] = [
    0,  # 0. Maxima incertidumbre (entropía)
    0,  # 1. Minima incertidumbre (entropía)
    # 2. Maxima incertidumbre (entropía) dada la información disponible (restricciones)
    0.7,
    # 3. Minima incertidumbre (entropía) dada la información disponible (restricciones)
    0.3,
    0,  # 4. Ninguna de las anteriores
    "",
]

# %% [markdown]
# ### 1.3 Universos
#
# Hay tres cajas idénticas. Detrás de una de ellas hay un regalo. El resto están vacías. Nos permiten reservar una caja. Luego, una persona elige una de las
# cajas que no contenga el regalo y no haya sido reservada. Supongamos que reservamos la caja 1. ¿Cuál de todos los universos paralelos va a ocurrir?
# ¿El regalo está en la caja 1 y nos muestran la caja 1? ¿El regalo está en la caja 1 y nos muestran la caja 2? ... ¿El regalo está en la caja 3 y
# nos muestran la caja 2? ¿El regalo está en la caja 3 y nos muestran la caja 3?
#
# 0. Regalo = 1, Abren = 1
# 1. Regalo = 1, Abren = 2
# 2. Regalo = 1, Abren = 3
# 3. Regalo = 2, Abren = 1
# 4. Regalo = 2, Abren = 2
# 5. Regalo = 2, Abren = 3
# 6. Regalo = 3, Abren = 1
# 7. Regalo = 3, Abren = 2
# 8. Regalo = 3, Abren = 3
#

# %%
respuestas[(1, 3, "Universos")] = [
    0,  # 0. Regalo = 1, Abren = 1
    0.25,  # 1. Regalo = 1, Abren = 2
    0.25,  # 2. Regalo = 1, Abren = 3
    0,  # 3. Regalo = 2, Abren = 1
    0,  # 4. Regalo = 2, Abren = 2
    0.25,  # 5. Regalo = 2, Abren = 3
    0,  # 6. Regalo = 3, Abren = 1
    0.25,  # 7. Regalo = 3, Abren = 2
    0,  # 8. Regalo = 3, Abren = 3
    "la 3 y 6  se descartan ya que no pueden abrir una que reserve, la 0, 1 4 y 8 se descartan por que no pueden abrir una que contenga el regalo ",
]

# %% [markdown]
# ### 1.4 Razonamiento
#
# Desde su descubierto, las reglas de la probabilidad han sido adoptadas como sistema de razonamiento en todas las ciencias con datos desde la física
# hasta las ciencias sociales. En los últimos años se ha producido enormes avances en el área de las ciencia de datos, el aprendizaje automático
# y la inteligencia artificial. ¿Cuándo se comenzó a usar por primer vez el actual sistema de razonamiento para contextos de incertidumbre?
#
# 0. Antes del siglo 17
# 1. Siglo 17
# 2. Siglo 18
# 3. Siglo 19
# 4. Siglo 20
# 5. Siglo 21
#
#
#

# %%
respuestas[(1, 4, "Razonamiento")] = [
    0,  # 0. Antes del siglo 17
    1,  # 1. Siglo 17
    0,  # 2. Siglo 18
    0,  # 3. Siglo 19
    0,  # 4. Siglo 20
    0,  # 5. Siglo 21
    "",
]

# %% [markdown]
# ### 1.5 Independencia
#
# Si P(A) = 0.4, P(B) = 0.5, y A y B son eventos independientes, ¿cuál es la probabilidad conjunta de P(A, B)?
#
# 0. 0.9
# 1. 0.1
# 2. 0.0
# 3. 0.2
# 4. Ninguna de las anteriores

# %%
respuestas[(1, 5, "Independencia")] = [
    0,  # 0. 0.9
    0,  # 1. 0.1
    0,  # 2. 0.0
    1,  # 3. 0.2
    0,  # 4. Ninguna de las anteriores
    "por que al ser independientes se multiplica la probabilidad",
]

# %% [markdown]
# ### 1.6 Marginal
#
# Sean dos variables binarias, X e Y, con las siguientes probabilidades conjuntas, P(X=0, Y=0) = 0.1, P(X=1, Y=0) = 0.2, P(X=0, Y=1) = 0.3, P(X=1, Y=1) = 0.4
# ¿Cuál es la probabilidad de P(Y = 1)?
#
#
# 1. P(Y=1): 0.10
# 1. P(Y=1): 0.15
# 1. P(Y=1): 0.20
# 1. P(Y=1): 0.25
# 1. P(Y=1): 0.30
# 1. P(Y=1): 0.35
# 1. P(Y=1): 0.40
# 1. P(Y=1): 0.45
# 1. P(Y=1): 0.50
# 1. P(Y=1): 0.55
# 1. P(Y=1): 0.60
# 1. P(Y=1): 0.65
# 1. P(Y=1): 0.70
# 1. P(Y=1): 0.75
# 1. P(Y=1): 0.80
# 1. P(Y=1): 0.85
# 1. P(Y=1): 0.90
# 1. Ninguna de las anteriores

# %%
respuestas[(1, 6, "Marginal")] = [
    0,  # 0. P(Y=1): 0.10
    0,  # 1. P(Y=1): 0.15
    0,  # 2. P(Y=1): 0.20
    0,  # 3. P(Y=1): 0.25
    0,  # 4. P(Y=1): 0.30
    0,  # 5. P(Y=1): 0.35
    0,  # 6. P(Y=1): 0.40
    0,  # 7. P(Y=1): 0.45
    0,  # 8. P(Y=1): 0.50
    0,  # 9. P(Y=1): 0.55
    0,  # 10. P(Y=1): 0.60
    0,  # 11. P(Y=1): 0.65
    1,  # 12. P(Y=1): 0.70
    0,  # 13. P(Y=1): 0.75
    0,  # 14. P(Y=1): 0.80
    0,  # 15. P(Y=1): 0.85
    0,  # 16. P(Y=1): 0.90
    0,  # 17. Ninguna de las anteriores
    "sumo probabilidades conjuntas cuando Y= 1"
]


# %% [markdown]
# ### 1.7 Condicional
#
# Sean dos variables binarias, X e Y, con las siguientes probabilidades conjuntas, P(X=0, Y=0) = 0.1, P(X=1, Y=0) = 0.2, P(X=0, Y=1) = 0.3, P(X=1, Y=1) = 0.4
#  ¿Cuál es la probabilidad de P(Y = 1|X = 1)?
#
#
# 1. P(Y=1|X=1): 1/2
# 1. P(Y=1|X=1): 1/3
# 1. P(Y=1|X=1): 2/3
# 1. P(Y=1|X=1): 1/4
# 1. P(Y=1|X=1): 2/4
# 1. P(Y=1|X=1): 3/4
# 1. P(Y=1|X=1): 1/5
# 1. P(Y=1|X=1): 2/5
# 1. P(Y=1|X=1): 3/5
# 1. P(Y=1|X=1): 4/5
# 1. P(Y=1|X=1): 1/6
# 1. P(Y=1|X=1): 2/6
# 1. P(Y=1|X=1): 3/6
# 1. P(Y=1|X=1): 4/6
# 1. P(Y=1|X=1): 5/6
# 1. Ninguna de las anteriores


# %%
respuestas[(1, 7, "Condicional")] = [
    0,  # 0. P(Y=1|X=1): 1/2
    0,  # 1. P(Y=1|X=1): 1/3
    1,  # 2. P(Y=1|X=1): 2/3
    0,  # 3. P(Y=1|X=1): 1/4
    0,  # 4. P(Y=1|X=1): 2/4
    0,  # 5. P(Y=1|X=1): 3/4
    0,  # 6. P(Y=1|X=1): 1/5
    0,  # 7. P(Y=1|X=1): 2/5
    0,  # 8. P(Y=1|X=1): 3/5
    0,  # 9. P(Y=1|X=1): 4/5
    0,  # 10. P(Y=1|X=1): 1/6
    0,  # 11. P(Y=1|X=1): 2/6
    0,  # 12. P(Y=1|X=1): 3/6
    0,  # 13. P(Y=1|X=1): 4/6
    0,  # 14. P(Y=1|X=1): 5/6
    0,  # 15. Ninguna de las anteriores
    "debido a la probabilidad condicional",
]


# %% [markdown]
# ### 1.8 Overfitting
#
# En el área de aprendizaje automático e inteligencia artificial se ha descubierto un problema que se conoce con el nombre de overfitting.
# ¿El overfitting es/era un problema propio del sistema de razonamiento para contextos de incertidumbre?
#
# 0. No
# 1. Sí


# %%
respuestas[(1, 8, "Overfitting")] = [
    1,  # 0. No
    0,  # 1. Si
    "",
]

# %% [markdown]
# ### 1.9 Evaluación
#
# En el área de aprendizaje automático e inteligencia artificial existe una gran cantidad de métricas distintas para evaluar los modelos alternativos.
# ¿En principio, existe una forma correcta, universal, de evaluar los modelos?
#
# 0. NO
# 1. Sí

# %%
respuestas[(1, 9, "Evaluación")] = [
    1,  # 0. No
    0,  # 1. Si
    "depende del problema y los datos por ejemplo para regresion se usa suele usar rmse y para clasificacion acuraccy, precision, etc",
]

# %% [markdown]
# ### 1.10 Predicción
#
# Históricamente todas las ciencias con datos, desde la física hasta las ciencias sociales, explicaron el mundo a través de teorías causales.
#  Los recientes avances en el área de aprendizaje automático e inteligencia artificial, sin embargo,
# se produjeron por el desarrollo de algoritmos altamente predictivos sin ninguna interpretación causal. ¿Por qué?
#
# 0. El modelo causal correcto nunca puede ser mejor prediciendo que los complejos algoritmos de AI/ML.
# 1. El modelo causal correcto a veces puede ser mejor, y a veces peor, que los complejos algoritmos de AI/ML.
# 2. El modelo causal correcto nunca puede ser peor prediciendo que los complejos algoritmos de AI/ML.
# 3. Los modelos causales solo explican, no predicen.
# 4. Ninguna de las anteriores

# %%
respuestas[(1, 10, "Predicción")] = [
    # 0. El modelo causal correcto nunca puede ser mejor prediciendo que los complejos algoritmos de AI/ML.
    0,
    # 1. El modelo causal correcto a veces puede ser mejor, y a veces peor, que los complejos algoritmos de AI/ML.
    0.9,
    # 2. El modelo causal correcto nunca puede ser peor prediciendo que los complejos algoritmos de AI/ML.
    0,
    0.1,  # 3. Los modelos causales solo explican, no predicen.
    0,  # 4. Ninguna de las anteriores
    "los modelos causalen pueden explicar el porque y si esas condiciones se replican pueden predecir bien y a veces los algoritmos pueden predecir mejor si se tienen muchos datos y si las condiciones varian",
]

# %% [markdown]
# ### 1.11 Diversificación
#
# Una casa de apuestas 3 a Cara y 1.2 a Sello por el lanzamiento de monedas normales con 0.5 de probabilidad de que salga Cara o Sello.
#  Supongamos que nos ofrecen jugar 1000 veces, apostando todos nuestros recursos en cada paso temporal. ¿Qué proporción apostaría a Cara?
# Notar que el resto se asigna a Sello. Notar además que si apostamos todo a Cara y sale Sello perdemos todos los recursos y no podemos volver a jugar.
#
# 0. Recursos asignados a Cara: 0.0
# 1. Recursos asignados a Cara: 0.1
# 2. Recursos asignados a Cara: 0.2
# 3. Recursos asignados a Cara: 0.3
# 4. Recursos asignados a Cara: 0.4
# 5. Recursos asignados a Cara: 0.5
# 6. Recursos asignados a Cara: 0.6
# 7. Recursos asignados a Cara: 0.7
# 8. Recursos asignados a Cara: 0.8
# 9. Recursos asignados a Cara: 0.9
# 10. Recursos asignados a Cara: 1.0

# %%
respuestas[(1, 11, "Diversificación")] = [
    0,  # 0. Recursos asignados a Cara: 0.0
    0,  # 1. Recursos asignados a Cara: 0.1
    0,  # 2. Recursos asignados a Cara: 0.2
    0,  # 3. Recursos asignados a Cara: 0.3
    0,  # 4. Recursos asignados a Cara: 0.4
    0.9,  # 5. Recursos asignados a Cara: 0.5
    0.1,  # 6. Recursos asignados a Cara: 0.6
    0,  # 7. Recursos asignados a Cara: 0.7
    0,  # 8. Recursos asignados a Cara: 0.8
    0,  # 9. Recursos asignados a Cara: 0.9
    0,  # 10. Recursos asignados a Cara: 1.0
    "balanceo los riesgos",
]

# %% [markdown]
# ### 1.12 Apuesta individual
#
# Una casa de apuestas paga 3 por Cara y 1.2 por Sello. La moneda tiene 0.5 de probabilidad de que salga Cara o Sello.
# Nos ofrecen jugar 1000 veces, apostando en cada ocasión todos nuestros recursos, 50% a Cara y 50% a Sello.
# Notar que la esperanza (media aritmética) es positiva (1,05). ¿Nos conviene jugar?
#
# 0. NO
# 1. Sí

# %%
respuestas[(1, 12, "Apuesta individual")] = [
    1,  # 0. No
    0,  # 1. Sí
    "No ya que estas condicionado a apostar 50 y 50, por ejemplo tenes 100"
    " y sale sello te quedas en 60 anque te toque cara en la proxima te terminas quedando con 90"
    "Tambien lo simule con 1000 tiradas y siempre quede en 0",
]

# %% [markdown]
# ### 1.13 Fondo común
#
# Una casa de apuestas paga 3 por Cara y 1.2 por Sello. La moneda tiene 0.5 de probabilidad de que salga Cara o Sello.
#  Nos ofrecen jugar 1000 veces, apostando en cada ocasión todos nuestros recursos, 50% a Cara y 50% a Sello. A diferencia del caso anterior,
#  aquí nos vemos en la obligación en cada paso temporal junto con otras 100 personas a dividir todos nuestros recursos en partes iguales.
# Es decir, en cada paso temporal cada persona tira la su propia moneda, actualiza sus propios recursos individuales, los pone en el fondo común,
#  se dividen en partes iguales y volvemos a empezar. ¿Este simple hecho, mejora o empeora nuestra tasa de crecimiento de nuestros recursos?
#
# 0. Empeora
# 1. Neutro
# 2. Mejora


# %%
respuestas[(1, 13, "Fondo común")] = [
    0,  # 0. Empeora
    0,  # 1. Neutro
    1,  # 1. Mejora
    "No entiendo bien lo que pasa, lo simule y me da que aumenta mucho la tasa de crecimiento, creo que puede ser que"
    "es por que al jugar 100 personas la tasa aritmetica si tiene importancia y al multiplicas en promedio el capital en 1.05"
    "en cada tirada en 1000 tiradas es un aumento importante al ser compuesto tambien",
]

# %% [markdown]
# ### 1.14 Tragedia de los comunes
#
# Una casa de apuestas paga 3 por Cara y 1.2 por Sello. La moneda tiene 0.5 de probabilidad de que salga Cara o Sello.
# Nos ofrecen jugar 1000 veces, apostando en cada ocasión todos nuestros recursos, 50% a Cara y 50% a Sello.
# Supongamos que para nuestras apuestas contamos con el apoyo de otras 100 personas que están aportando en cada paso temporal a un fondo que se divide en
# partes iguales. ¿Nos conviene aportar al fondo común o nos conviene dejar de aportar y seguir recibiendo la cuota del fondo común?
#
# 0. Nos conviene aportar al fondo común
# 1. Es indistinto
# 2. Nos conviene dejar de aportar mientras seguimos recibiendo la cuota del fondo común


# %%
respuestas[(1, 14, "Tragedia de los comunes")] = [
    0,  # 0. Nos conviene aportar al fondo común
    0,  # 1. Es indistinto
    1,  # 1. Nos conviene dejar de aportar mientras seguimos recibiendo la cuota del fondo común
    "porque nuestro capital crece gracias al aporte de los demas y nunca arriesgamos nuestro capital",
]
