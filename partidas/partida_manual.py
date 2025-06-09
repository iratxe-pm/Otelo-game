
#PARTIDA HUMANO VS HUMANO
from reglas_juego.avance_juego import ganador, turnos
from reglas_juego.excepciones import EntradaNoNumericaError, JugadorInvalidoError, MovimientoInvalidoError, validar_entrada_numerica
from partidas.mostrar_tablero import mostrar_tablero
from reglas_juego.movimientos import posibles_movimientos

def partida_manual(estado):
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