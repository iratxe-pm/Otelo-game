#Se encarga de actualizar la posición de las piezas en el tablero a medida que avanza el juego
import random
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
            

            return turno



def partida_automática(turno, tablero_actual):
    tablero = tablero_actual.copy()
    contador_salta_turno = 0
    juego_sigue = True
    
    while juego_sigue:
        mostrar_tablero(tablero)        

        if(contador_salta_turno<2):
                movimientos = posibles_movimientos(tablero,turno)
                if (len(movimientos) != 0):
                    accion_seleccionada = random.choice(movimientos)
                    turno = turnos(turno, accion_seleccionada[0], accion_seleccionada[1], tablero)   
                
                else:
                    contador_salta_turno +=1
                    if turno == 1:
                        turno = 2
                    else: 
                        turno = 1

        else:
                juego_sigue = False
                return ganador(turno)

def ganador(turno):
    if (len(ficha_negra()) > len(ficha_blanca())):
        if turno == 1:
            return 1
        else:
            return -1

    elif (len(ficha_negra()) < len(ficha_blanca())):
        if turno == 1:
            return -1
        else:
            return 1
    else:
        return 0          

