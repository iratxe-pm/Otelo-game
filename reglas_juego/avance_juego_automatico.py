#Se encarga de actualizar la posición de las piezas en el tablero a medida que avanza el juego
from copy import copy, deepcopy
import random
from reglas_juego.estado_juego import EstadoJuego
from reglas_juego.cambio_fichas import cambio_de_color_fichas
from reglas_juego.inicializa_tablero import ficha_blanca, ganadores, ficha_negra, mostrar_tablero
from reglas_juego.movimientos import posibles_movimientos, reglas_de_movimiento

def turnos(turno, new_fila, new_columna, estado):
            #comprueba que si las reglas se cumplen, entonces se produzca el cambio en el tablero
            if(reglas_de_movimiento(turno,new_fila,new_columna)):
                cambio_de_color_fichas(turno,new_fila,new_columna,estado.tablero)
                if turno == 1: #turno de las negras
                    estado.tablero[new_fila][new_columna] = 2  # Ficha negra
                    estado.ficha_negra([new_fila,new_columna])
                    turno = 2 #siguiente turno: blancas
                    
                elif turno == 2: #turno de las blancas
                    estado.tablero[new_fila][new_columna] = 1  # Ficha blanca
                    estado.ficha_blanca([new_fila,new_columna])
                    turno = 1 #siguiente turno: negras
            

            return turno, estado.tablero 



def partida_automática(turno, estado):
    contador_salta_turno = 0
    juego_sigue = True
    
    while juego_sigue:

        if(contador_salta_turno<2):
                movimientos = posibles_movimientos(estado.tablero,turno)
                if (len(movimientos) != 0):
                    accion_seleccionada = random.choice(movimientos)
                    #solo interesa turno
                    turno, _ = turnos(turno, accion_seleccionada[0], accion_seleccionada[1], estado)   
                
                else:
                    contador_salta_turno +=1
                    if turno == 1:
                        turno = 2
                    else: 
                        turno = 1

        else:
                juego_sigue = False
                return ganador(estado,turno)

def ganador(estado, turno):
    if (len(estado.ficha_negra()) > len(estado.ficha_blanca())):
        if turno == 1:
            return 1
        else:
            return -1

    elif (len(estado.ficha_negra()) < len(estado.ficha_blanca())):
        if turno == 1:
            return -1
        else:
            return 1
    else:
        return 0          

