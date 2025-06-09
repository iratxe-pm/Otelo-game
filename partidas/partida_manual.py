
#PARTIDA HUMANO VS HUMANO
from reglas_juego.avance_juego import ganador, turnos
from reglas_juego.excepciones import EntradaNoNumericaError, JugadorInvalidoError, MovimientoInvalidoError, validar_entrada_numerica
from partidas.mostrar_tablero import mostrar_tablero
from reglas_juego.movimientos import posibles_movimientos

def partida_manual(estado):
    """
    Controla una partida manual entre dos jugadores (jugador vs jugador) de Othello/Reversi.

    Algoritmo:
        1. Se inicia el bucle del juego, que continuará hasta que dos turnos consecutivos no tengan movimientos válidos.
        2. En cada turno:
            a. Se muestra el tablero con el estado actual.
            b. Se indica de quién es el turno: NEGRO (●) o BLANCO (○).
            c. Se calculan los posibles movimientos del jugador actual con la función `posibles_movimientos`.
                - Si hay movimientos disponibles:
                    i. Se solicita al jugador que introduzca la fila y columna donde desea colocar su ficha.
                    ii. Se valida que la entrada esté dentro de los límites del tablero (0 a 7).
                    iii. Se verifica que la casilla seleccionada esté vacía.
                    iv. Si todo es válido, se realiza el movimiento con la función `turnos`, que también devuelve el jugador del siguiente turno.
                    v. Si el movimiento es exitoso, se reinicia el contador de turnos saltados.
                    vi. Si ocurre algún error, se lanza y captura una excepción adecuada, y se muestra un mensaje correspondiente:
                        - EntradaNoNumericaError: si la entrada no es un número válido.
                        - MovimientoInvalidoError: si el movimiento no cumple las reglas del juego.
                        - JugadorInvalidoError: si el valor del turno es inválido.
                - Si no hay movimientos disponibles:
                    i. Se notifica al jugador y se incrementa el contador de turnos saltados.
                    ii. Se cambia el turno al otro jugador.
        3. Si ambos jugadores consecutivos no tienen movimientos, se termina la partida.
        4. Se determina el ganador mediante la función `ganador`:
            - Si gana el jugador del último turno, se muestra "GANASTE".
            - Si pierde, se muestra "PERDISTE".
            - En caso de empate, se muestra "EMPATE".

    Lanza:
        MovimientoInvalidoError: Se lanza cuando se intenta realizar un movimiento que no cumple las reglas del juego.
    
        JugadorInvalidoError: Se lanza cuando el valor del turno no corresponde a un jugador válido (distinto de 1 o 2).
    
        EntradaNoNumericaError: Se lanza cuando la entrada del usuario no es un número entero válido.

    Parámetros: estado (EstadoJuego): Objeto que representa el estado actual del juego, incluyendo el tablero y las listas de fichas.
    """

    turno = 1  # Empieza el jugador negro
    contador_salta_turno = 0

    while (contador_salta_turno<2):
        mostrar_tablero(estado.tablero)        
        
        if turno == 1:
            print("\nTurno del jugador NEGRO (●)")
        else:
            print("\nTurno del jugador BLANCO (○)")
            
        movimientos = posibles_movimientos(estado, turno)
            
        if (len(movimientos) != 0):
                try:
                    #Selección de casilla a la que se mueve la ficha
                    new_fila = validar_entrada_numerica(input("Ingrese la fila a donde va a mover la ficha (0-7): "))
                    new_columna = validar_entrada_numerica(input("Ingrese la columna a donde va a mover la ficha (0-7): "))
                    
                    if not (0 <= new_fila <= 7 and 0 <= new_columna <= 7):
                        print("Posición inválida. Las coordenadas deben estar entre 0 y 7.")
                        continue
                    if not (estado.tablero[new_fila][new_columna] == 0):
                        print("Posición inválida. En esa posición ya se encuentra una ficha.")
                        continue
                   
                    turno, _ = turnos(turno, new_fila, new_columna, estado)
                    contador_salta_turno = 0

                except EntradaNoNumericaError as e:
                        print(e)
                except MovimientoInvalidoError:
                        print("Movimiento inválido. Intente de nuevo.")
                except JugadorInvalidoError:
                        print("Error: turno inválido.")
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