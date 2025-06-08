#PARTIDA IA VS HUMANO

from reglas_juego.avance_juego import ganador, turnos
from mcts import mcts
from reglas_juego.excepciones import EntradaNoNumericaError, JugadorInvalidoError, MovimientoInvalidoError, validar_entrada_numerica
from partidas.mostrar_tablero import mostrar_tablero
from reglas_juego.movimientos import posibles_movimientos


def partida_mixta(estado):
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
    if (ganador(turno) == 1):
          print("GANASTES")
    elif (ganador(turno) == -1):
          print("PERDISTES")
    else:
          print("EMPATE")
            

