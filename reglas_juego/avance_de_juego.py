#Se encarga de actualizar la posición de las piezas en el tablero a medida que avanza el juego
from reglas_juego.cambio_fichas import cambio_de_color_fichas
from reglas_juego.inicializa_tablero import ficha_blanca, ganadores, ficha_negra, mostrar_tablero
from reglas_juego.movimientos import posibles_movimientos, reglas_de_movimiento

def turnos(turno, new_fila, new_columna, tablero):
            #comprueba que si las reglas se cumplen, entonces se produzca el cambio en el tablero
            if(reglas_de_movimiento(turno,new_fila,new_columna)):
                cambio_de_color_fichas(turno,new_fila,new_columna,tablero)
                if turno == 1: #turno de las negras
                    tablero[new_fila][new_columna] = 2  # Ficha negra
                    ficha_negra([new_fila,new_columna])
                    turno = 2 #siguiente turno: blancas
                    
                elif turno == 2: #turno de las blancas
                    tablero[new_fila][new_columna] = 1  # Ficha blanca
                    ficha_blanca([new_fila,new_columna])
                    turno = 1 #siguiente turno: negras
                else:
                    print("Opción no válida. Intente de nuevo.")
            else:
                    print("No cumple con las reglas.")
            

            return turno



def modificar_tablero(tablero):
    turno = 1  # Empieza el jugador negro
    contador_salta_turno = 0
    juego_sigue = True
    
    while juego_sigue:
        mostrar_tablero(tablero)        
        
        if turno == 1:
            print("\nTurno del jugador NEGRO (●)")
        else:
            print("\nTurno del jugador BLANCO (○)")
            
        try:

            if(contador_salta_turno<2):
                if (len(posibles_movimientos(tablero,turno)) != 0):
                    #Selección de casilla a la que se mueve la ficha
                    new_fila = int(input("Ingrese la fila a donde va a mover la ficha (0-7): "))
                    new_columna = int(input("Ingrese la columna a donde va a mover la ficha (0-7): "))
                    
                    #Mira que las coordenadas a donde se mueve estén dentro del tablero
                    if not (0 <= new_fila <= 7 and 0 <= new_columna <= 7):
                        print("Posición inválida. Las coordenadas deben estar entre 0 y 7.")
                        continue
                    if not (tablero[new_fila][new_columna] == 0):
                        print("Posición inválida. En esa posición ya se encuentra una ficha.")
                        continue
                    turno = turnos(turno, new_fila, new_columna, tablero)   
                
                else:
                    print("No hay movimientos posibles, le toca al otro jugador")
                    contador_salta_turno +=1
                    if turno == 1:
                        turno = 2
                    else: 
                        turno = 1

            else:
                print("Juego terminado")
                juego_sigue = False
                if (len(ficha_negra()) > len(ficha_blanca())):
                    if turno == 1:
                        ganadores(1)
                    else:
                        ganadores(-1)
                    print("¡¡¡GANA LAS NEGRAS !!!")

                elif (len(ficha_negra()) < len(ficha_blanca())):
                    if turno == 1:
                        ganadores(-1)
                    else:
                        ganadores(1)
                    print("¡¡¡GANA LAS BLANCAS !!!")
                else:
                     ganadores(0)
                     print("¡¡¡EMPATE !!!")
                break
            

        except ValueError:
            print("Por favor ingrese números válidos.")

