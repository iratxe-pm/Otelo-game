#Se encarga de actualizar la posición de las piezas en el tablero a medida que avanza el juego
from reglas_juego.excepciones import JugadorInvalidoError, MovimientoInvalidoError
from reglas_juego.cambio_fichas import cambio_de_color_fichas
from reglas_juego.movimientos import reglas_de_movimiento

def turnos(turno, new_fila, new_columna, estado):
            #comprueba que si las reglas se cumplen, entonces se produzca el cambio en el tablero
            if(reglas_de_movimiento(estado,turno,new_fila,new_columna)):
                cambio_de_color_fichas(estado,turno,new_fila,new_columna,estado.tablero)
                if turno == 1: #turno de las negras
                    estado.tablero[new_fila][new_columna] = 2  # Ficha negra
                    estado.ficha_negra([new_fila,new_columna])
                    turno = 2 #siguiente turno: blancas
                    
                elif turno == 2: #turno de las blancas
                    estado.tablero[new_fila][new_columna] = 1  # Ficha blanca
                    estado.ficha_blanca([new_fila,new_columna])
                    turno = 1 #siguiente turno: negras
                
                else:
                    raise JugadorInvalidoError()
            else: 
                 raise MovimientoInvalidoError()

            return turno, estado.tablero 


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


