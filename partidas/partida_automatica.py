#PARTIDA VS PARTIDA

from reglas_juego.avance_juego import turnos
from partidas.mostrar_tablero import mostrar_tablero
from reglas_juego.movimientos import posibles_movimientos
from mcts import mcts  # Asegúrate de importar tu función MCTS correctamente
from reglas_juego.estado_juego import EstadoJuego

import time

def partida_automática(estado):
    turno = 1  # Empieza la ficha blanca (o cambia a 2 si prefieres que empiece negra)

    print("Inicio de la partida IA vs IA")
    mostrar_tablero(estado.tablero)
    while True:
        movimientos = posibles_movimientos(estado, turno)
        if not movimientos:
        # Comprobar si el otro jugador también está bloqueado
            if not posibles_movimientos(estado, 3 - turno):
                break
            turno = 3 - turno
            continue

        accion = mcts(estado.tablero, turno)
        turno, estado = turnos(turno, accion[0], accion[1], estado)

        print(f"\nIA con turno {turno} coloca ficha en {accion}")
        mostrar_tablero(estado.tablero)
        time.sleep(1)
   