from copy import deepcopy

def partida_ia_vs_ia():
    return 2

def crear_linea_csv(tablero, ganador):
    linea = deepcopy(tablero)
    linea["ganador"] = ganador #en este diccionario que es el tablero, añado una clave para guardar al ganador