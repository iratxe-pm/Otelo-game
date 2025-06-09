#PARTIDA VS PARTIDA

from reglas_juego.avance_juego import ganador, turnos
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

        if turno == 1:
            print("\nTurno del jugador NEGRO (●)")
        else:
            print("\nTurno del jugador BLANCO (○)")
        mostrar_tablero(estado.tablero)
        time.sleep(1)
    print("Juego terminado")
    if (ganador(estado,turno) == 1):
          print("GANASTES")
    elif (ganador(estado,turno) == -1):
          print("PERDISTES")
    else:
          print("EMPATE")
            
   