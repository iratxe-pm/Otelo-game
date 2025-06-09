#PARTIDA IA VS HUMANO

from reglas_juego.avance_juego import ganador, turnos
from mcts import mcts
from reglas_juego.excepciones import EntradaNoNumericaError, JugadorInvalidoError, MovimientoInvalidoError, PosicionOcupada, ValorFueraDeRango, validar_entrada_numerica, verificar_poosicion_en_tablero, verificar_valor_en_rango
from partidas.mostrar_tablero import mostrar_tablero
from reglas_juego.movimientos import posibles_movimientos


def partida_mixta(estado):
    """
    Controla una partida mixta entre un jugador humano y la inteligencia artificial (IA) en Othello/Reversi.

    Algoritmo:
        1. Se inicializa el contador de turnos saltados en 0 y se establece que el turno inicial corresponde a las fichas negras (turno = 1).
        2. Se solicita al jugador humano que elija si desea jugar con las fichas NEGRAS (●) o BLANCAS (○), validando su entrada.
            - Si elige las fichas blancas, el jugador humano será el turno 2 y la IA el turno 1; y viceversa.
        3. Mientras el contador de turnos consecutivos sin movimientos válidos sea menor que 2:
            a. Se muestra el tablero actual.
            b. Se indica el turno actual (NEGRO o BLANCO).
            c. Se calculan los movimientos válidos del jugador actual usando la función `posibles_movimientos`.
            - Si hay movimientos posibles:
                i. Si es el turno del jugador humano:
                    - Se solicita la fila y columna del movimiento.
                    - Si todo es correcto, se realiza el movimiento con `turnos`.
                    - Si el movimiento es válido, se reinicia el contador de saltos.
                    - Si ocurre un error, se captura la excepción correspondiente:
                ii. Si es el turno de la IA:
                    - La IA selecciona una jugada utilizando el algoritmo Monte Carlo Tree Search (MCTS), llamando a la función `mcts`.
                    - Se ejecuta el movimiento usando `turnos`.
                    - Se reinicia el contador de turnos saltados.
            - Si no hay movimientos válidos:
                i. Se notifica al jugador.
                ii. Se incrementa el contador de turnos saltados.
                iii. Se cambia el turno al otro jugador.
        4. Si ambos jugadores consecutivos no tienen movimientos válidos, la partida finaliza.
        5. Se determina el ganador mediante la función `ganador`.

    Lanza:
        ValorFueraDeRango: Se lanza cuando se intenta seleccionar una posición fuera del tablero.
        
        PosicionOcupada: Se lanza cuando se intenta poner una ficha en una posición ocupada.

        MovimientoInvalidoError: Se lanza cuando se intenta realizar un movimiento que no cumple las reglas del juego.
    
        JugadorInvalidoError: Se lanza cuando el valor del turno no corresponde a un jugador válido (distinto de 1 o 2).
    
        EntradaNoNumericaError: Se lanza cuando la entrada del usuario no es un número entero válido.

    Parámetros:
        estado (EstadoJuego): Objeto que representa el estado actual del juego, incluyendo el tablero y las listas de fichas.
    """
    
    turno = 1  # Empieza el jugador negro
    contador_salta_turno = 0
    print("¿Quieres jugar como NEGRO (●) o BLANCO (○)?")
    print("\nFichas NEGRAS -> 1")
    print("\nFichas BLANCAS -> 2")
    while True:
        try:
            modo = validar_entrada_numerica(input("Elija sus fichas: "))
            verificar_valor_en_rango(modo, 1, 2)
            break  # solo si todo va bien
        except (EntradaNoNumericaError, ValorFueraDeRango) as e:
            print(f"Error: {e}. Intente de nuevo.\n")

    while (contador_salta_turno<2):
        mostrar_tablero(estado.tablero)        
        
        if turno == 1:
            print("\nTurno del jugador NEGRO (●)")
        else:
            print("\nTurno del jugador BLANCO (○)")
            
        movimientos = posibles_movimientos(estado, turno)
            
        if (len(movimientos) != 0):
            if turno == modo:
                try:
                    new_fila = validar_entrada_numerica(input("Ingrese la fila a donde va a mover la ficha (0-7): "))
                    verificar_valor_en_rango(new_fila, 0, 7)
                    new_columna = validar_entrada_numerica(input("Ingrese la columna a donde va a mover la ficha (0-7): "))
                    verificar_valor_en_rango(new_columna, 0, 7)
                    verificar_poosicion_en_tablero(new_fila, new_columna, estado.tablero)

                    turno, _ = turnos(turno, new_fila, new_columna, estado)
                    contador_salta_turno = 0

                except (EntradaNoNumericaError,  ValorFueraDeRango, PosicionOcupada, MovimientoInvalidoError, JugadorInvalidoError)   as e:
                    print(f"Error: {e}. Intentalo de nuevo.")

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
    equipo = "Negras" if turno == 1 else "Blancas"

    if ganador(estado, turno) == 1:
        print(f"LAS {equipo} GANAN")
    elif ganador(estado, turno) == -1:
        print(f"LAS {equipo} PIERDEN")
    else:
        print("EMPATE")
            

