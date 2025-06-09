import pandas as pd

from reglas_juego.avance_juego import turnos,ganador
from reglas_juego.movimientos import posibles_movimientos
from mcts import mcts 
from reglas_juego.estado_juego import EstadoJuego

def crear_linea_csv(tablero,turno, ganador):
    """
    Crea una línea (diccionario) con el estado del tablero, turno y resultado para guardar en CSV.

    Parámetros:
        tablero (list): Matriz 8x8 con el estado actual.
        turno (int): Turno actual (1=negras, 2=blancas).
        ha_ganado (int): Resultado de la partida (1: gana negras, 2: gana blancas, 0: empate).

    Retorna:
        dict: Diccionario con estado del tablero, turno y resultado.
    """
    linea = {}
    for fila in range(8):
        for columna in range(8):
            clave = f"({fila}, {columna})"
            linea[clave] = tablero[fila][columna]
    
    linea["turno"] = turno
    linea["ha_ganado"] = ganador
    return linea

def partida_ia_vs_ia():
    """
    Ejecuta varias partidas entre dos IA usando MCTS y guarda los estados y resultados en un DataFrame.
    """
    partidas = 20
    fichero_ia_vs_ia = pd.DataFrame()

    for _ in range(partidas):
        estado = EstadoJuego()
        turno = 1
        partida_realizada = []

        while True:
            movimientos_posibles = posibles_movimientos(estado, turno)
            movimientos_oponente = posibles_movimientos(estado, 3 - turno)

            if len(movimientos_posibles) == 0 and len(movimientos_oponente) == 0:
                ganador_partida = ganador(estado, turno)
                for linea in partida_realizada:
                    fichero_ia_vs_ia = pd.concat([fichero_ia_vs_ia, pd.DataFrame([linea])], ignore_index=True)
                break

            if len(movimientos_posibles) == 0:
                turno = 3 - turno
                continue

            accion_elegida = mcts(estado.tablero, turno)

            turnos(turno, accion_elegida[0], accion_elegida[1], estado)

            ganador_actual = ganador(estado, turno)
            nueva_linea = crear_linea_csv(estado.tablero, turno, ganador_actual)
            partida_realizada.append(nueva_linea)

            turno = 3 - turno

    fichero_ia_vs_ia.to_csv("partidas_ia_vs_ia.csv", index=False)