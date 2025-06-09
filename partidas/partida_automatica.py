#PARTIDA VS PARTIDA

from reglas_juego.avance_juego import ganador, turnos
from partidas.mostrar_tablero import mostrar_tablero
from reglas_juego.movimientos import posibles_movimientos
from mcts import mcts  # Asegúrate de importar tu función MCTS correctamente
from reglas_juego.estado_juego import EstadoJuego

import time

def partida_automática(estado):
    """
    Controla una partida automática entre dos inteligencias artificiales (IA) en el juego Othello/Reversi.

    Algoritmo:
        1. Se inicializa el turno con el jugador negro (turno = 1).
        2. Se muestra el estado inicial del tablero.
        3. Se entra en un bucle que se ejecuta hasta que ambos jugadores consecutivos no tengan movimientos válidos:
            a. Se calculan los movimientos posibles para el jugador actual usando `posibles_movimientos`.
                - Si hay movimientos disponibles:
                    i. La IA selecciona una jugada utilizando el algoritmo Monte Carlo Tree Search (MCTS), llamando a la función `mcts`.
                    ii. Se realiza el movimiento con `turnos`, que actualiza el estado del juego y alterna el turno.
                - Si no hay movimientos disponibles:
                    i. Se verifica si el otro jugador también está bloqueado.
                        - Si ambos jugadores están bloqueados, el juego termina.
                        - Si no, se cambia el turno al otro jugador y continúa el bucle.
            b. Se muestra el tablero actualizado.
            c. Se imprime de quién es el turno (NEGRO o BLANCO).
            d. Se hace una pausa de 1 segundo con `time.sleep` para simular el tiempo de pensamiento.
        4. Al finalizar, se determina el resultado de la partida con la función `ganador`:
            - Si gana el jugador negro, se imprime "GANÓ NEGRO".
            - Si gana el jugador blanco, se imprime "GANÓ BLANCO".
            - En caso de empate, se imprime "EMPATE".

    Parámetros:
        estado (EstadoJuego): Objeto que representa el estado actual del juego, incluyendo el tablero y las fichas.
    """

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
    equipo = "Negras" if turno == 1 else "Blancas"

    if ganador(estado, turno) == 1:
        print(f"LAS {equipo} GANAN")
    elif ganador(estado, turno) == -1:
        print(f"LAS {equipo} PIERDEN")
    else:
        print("EMPATE")
            
   