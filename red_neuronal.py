from keras.utils import set_random_seed
set_random_seed(394867)

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

from keras import Sequential, Input
from keras.layers import Dense, BatchNormalization, Dropout

from keras.optimizers import SGD

#CUANDO SE VAYA A ENTRENAR CON MÁS PARTIDAS: 
# PRIMERO: EJECUTAR SIMULACION SIN RED Y GENERAR CSV (DESCOMENTAR COSAS EN MTCS Y JUEGO OTELO)
# SEGUNDO: VOLVER A COMENTAR ESAS COSAS Y DEJARLO COMO ESTABA (ANTES DE TOCAR LA RED Y DESPUES DE CREAR CSV)
# TERCERO: ENTRENAR LA RED EJECUTANDO EN LA TERMINAL EL COMANDO: PYTHON RED_NEURONAL.PY (EJECUTAR FICHERO CON RED)
# CUARTO: COMPROBAR QUE SE CREA ARCHIVO RED_OTELO.H5
# QUINTO: EJECUTAR NORMAL EL JUEGO EN IA VS IA O IA VS HUMANO PA PROBAR SU FUNCIONAMIENTO (NO DEBE DE DAR ERROR, SOLO VA LENTO)
# SI SE CAMBIAN LOS PARÁMETROS DE LA RED, REALIZAR A PARTIR DEL PASO TERCERO

partidas_otelo = pd.read_csv("partidas_ia_vs_ia.csv")
print(partidas_otelo.head())


# Atributos
atributos = partidas_otelo.loc[:, '(0, 0)':'turno']
print(atributos.head())
#Objetivos
objetivo = partidas_otelo.loc[:, 'ha_ganado']
print(objetivo.head())

# separa los que se usan para entrenar y para probar
(atributos_entrenamiento, atributos_prueba,
    objetivo_entrenamiento, objetivo_prueba) = train_test_split(
        atributos, objetivo,
        test_size=.2
)

# Crear red 
red_otelo = Sequential([
    Input(shape=(65,)),                   # entra 64 casillas + 1 turno
    Dense(256, activation='relu'),        # capa grande = captar patrones complejos / relu = eficiente, aprede relaciones no lineale
    Dropout(0.3),                         #apaga una parte de las neuronas pa q no memorice

    Dense(128, activation='relu'),
    Dropout(0.3),

    Dense(64, activation='relu'),
    Dropout(0.2),

    Dense(1, activation='tanh')           # Salida en rango [-1, 1]
])

# Compilar 
optimizador = SGD(learning_rate=0.001)
red_otelo.compile(
    optimizer=optimizador,
    loss='mean_squared_error',
    metrics=['mean_absolute_error']
)

#Entrena
red_otelo.fit(
    atributos_entrenamiento,        # entrenamiento
    objetivo_entrenamiento,         # objetivo
    batch_size=64,                  # Tamaño del "lote" de entrenamiento
    epochs=300,                     # Número de veces que se recorre todo el dataset
    validation_split=0.1,           # Porcentaje de datos usados para validación
    verbose=1                       # Nivel de detalle de la salida en consola
)

#Evalua
red_otelo.evaluate(atributos_prueba, objetivo_prueba)

red_otelo.save('red_otelo.h5')