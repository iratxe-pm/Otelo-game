#PARTIDA IA VS HUMANO

from reglas_juego.avance_juego import ganador, turnos
from mcts import mcts
from reglas_juego.excepciones import EntradaNoNumericaError, JugadorInvalidoError, MovimientoInvalidoError, validar_entrada_numerica
from partidas.mostrar_tablero import mostrar_tablero
from reglas_juego.movimientos import posibles_movimientos


def partida_mixta(estado):
    """
    Controla una partida mixta entre un jugador humano y la inteligencia artificial (IA) en Othello/Reversi.

    Algoritmo:
        1. Se inicializa el contador de turnos saltados en 0 y se establece que el turno inicial corresponde a las fichas negras (turno = 1).
        2. Se solicita al jugador humano que elija si desea jugar con las fichas NEGRAS (●) o BLANCAS (○), validando su entrada con `validar_entrada_numerica`.
            - Si elige las fichas blancas, el jugador humano será el turno 2 y la IA el turno 1; y viceversa.
        3. Mientras el contador de turnos consecutivos sin movimientos válidos sea menor que 2:
            a. Se muestra el tablero actual.
            b. Se indica el turno actual (NEGRO o BLANCO).
            c. Se calculan los movimientos válidos del jugador actual usando la función `posibles_movimientos`.
            - Si hay movimientos posibles:
                i. Si es el turno del jugador humano:
                    - Se solicita la fila y columna del movimiento.
                    - Se valida que estén dentro del rango permitido (0-7) y que la casilla esté vacía.
                    - Si todo es correcto, se realiza el movimiento con `turnos`.
                    - Si el movimiento es válido, se reinicia el contador de saltos.
                    - Si ocurre un error, se captura la excepción correspondiente:
                        * EntradaNoNumericaError: si la entrada no es un número válido.
                        * MovimientoInvalidoError: si el movimiento no cumple las reglas.
                        * JugadorInvalidoError: si el turno no corresponde al jugador.
                ii. Si es el turno de la IA:
                    - La IA selecciona una jugada utilizando el algoritmo Monte Carlo Tree Search (MCTS), llamando a la función `mcts`.
                    - Se ejecuta el movimiento usando `turnos`.
                    - Se reinicia el contador de turnos saltados.
            - Si no hay movimientos válidos:
                i. Se notifica al jugador.
                ii. Se incrementa el contador de turnos saltados.
                iii. Se cambia el turno al otro jugador.
        4. Si ambos jugadores consecutivos no tienen movimientos válidos, la partida finaliza.
        5. Se determina el ganador mediante la función `ganador`:
            - Si gana el jugador humano, se imprime "GANASTE".
            - Si pierde, se imprime "PERDISTE".
            - En caso de empate, se imprime "EMPATE".

    Lanza:
        MovimientoInvalidoError: Se lanza cuando se intenta realizar un movimiento que no cumple las reglas del juego.
    
        JugadorInvalidoError: Se lanza cuando el valor del turno no corresponde a un jugador válido (distinto de 1 o 2).
    
        EntradaNoNumericaError: Se lanza cuando la entrada del usuario no es un número entero válido.

    Parámetros:
        estado (EstadoJuego): Objeto que representa el estado actual del juego, incluyendo el tablero y las listas de fichas.
    """
    
    turno = 1  # Empieza el jugador negro
    contador_salta_turno = 0
    print("¿Quieres jugar como NEGRO (●) o BLANCO (○)?")
    print("\nFichas blancas -> 1")
    print("\nFichas negras -> 2")
    modo = validar_entrada_numerica(input("Elija sus fichas: "))

    humano = 1 if modo == 2 else 2
    ia = 2 if humano == 1 else 1

    while (contador_salta_turno<2):
        mostrar_tablero(estado.tablero)        
        
        if turno == 1:
            print("\nTurno del jugador NEGRO (●)")
        else:
            print("\nTurno del jugador BLANCO (○)")
            
        movimientos = posibles_movimientos(estado, turno)
            
        if (len(movimientos) != 0):
            if turno == humano:
                try:
                    new_fila = validar_entrada_numerica(input("Ingrese la fila (0-7): "))
                    new_columna = validar_entrada_numerica(input("Ingrese la columna (0-7): "))

                    if not (0 <= new_fila <= 7 and 0 <= new_columna <= 7):
                        print("Coordenadas fuera de rango. Deben estar entre 0 y 7.")
                        continue
                    if estado.tablero[new_fila][new_columna] != 0:
                        print("Ya hay una ficha en esa posición.")
                        continue

                    turno, _ = turnos(turno, new_fila, new_columna, estado)
                    contador_salta_turno = 0

                except EntradaNoNumericaError as e:
                    print(e)
                except MovimientoInvalidoError:
                    print("Movimiento inválido. Intente de nuevo.")
                except JugadorInvalidoError:
                    print("Error: turno inválido.")

            else:  # Turno de la IA
                accion = mcts(estado.tablero, turno)
                turno, _ = turnos(turno, accion[0], accion[1], estado)
                contador_salta_turno = 0

        else:
            print("No hay movimientos posibles, le toca al otro jugador")
            contador_salta_turno +=1
            if turno == 1:
                turno = 2
            else: 
                turno = 1

    print("Juego terminado")
    if (ganador(estado,turno) == 1):
          print("GANASTES")
    elif (ganador(estado,turno) == -1):
          print("PERDISTES")
    else:
          print("EMPATE")
            

