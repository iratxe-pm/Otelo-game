#Se encarga de actualizar la posición de las piezas en el tablero a medida que avanza el juego
from reglas_juego.excepciones import JugadorInvalidoError, MovimientoInvalidoError
from reglas_juego.cambio_fichas import cambio_de_color_fichas
from reglas_juego.movimientos import reglas_de_movimiento,posibles_movimientos 
import random

def turnos(turno_llega, new_fila, new_columna, estado):
            #comprueba que si las reglas se cumplen, entonces se produzca el cambio en el tablero
            if(reglas_de_movimiento(estado,turno_llega,new_fila,new_columna)):
                cambio_de_color_fichas(estado,turno_llega,new_fila,new_columna)
                if turno_llega == 1: #turno de las negras
                    estado.tablero[new_fila][new_columna] = 2  # Ficha negra
                    estado.ficha_negra([new_fila,new_columna])
                    turno = 2 #siguiente turno: blancas
                    
                elif turno_llega == 2: #turno de las blancas
                    estado.tablero[new_fila][new_columna] = 1  # Ficha blanca
                    estado.ficha_blanca([new_fila,new_columna])
                    turno = 1 #siguiente turno: negras
                
                else:
                    turno = turno_llega
                    raise JugadorInvalidoError()
            else: 
                turno = turno_llega
                raise MovimientoInvalidoError()

            return turno, estado

def sincronizar_fichas_desde_tablero(estado):
    estado.fichas_blancas = []
    estado.fichas_negras = []
    for fila in range(8):
        for col in range(8):
            if estado.tablero[fila][col] == 1:
                estado.fichas_blancas.append([fila, col])
            elif estado.tablero[fila][col] == 2:
                estado.fichas_negras.append([fila, col])


def partida_simulada(turno_llega, estado):
    contador_salta_turno = 0
    turno = turno_llega
    
    while contador_salta_turno < 2 and not estado.is_terminal():
        movimientos = posibles_movimientos(estado, turno)
        
        if movimientos:
            accion_seleccionada = random.choice(movimientos)
            try:
                turno, estado = turnos(turno, accion_seleccionada[0], accion_seleccionada[1], estado)
            except MovimientoInvalidoError:
                # Opcional: imprimir info para debug
                print(f"Movimiento inválido en partida automática: turno {turno}, acción {accion_seleccionada}")
                # Puedes decidir si romper, continuar, o salir
                break
            contador_salta_turno = 0  # Reinicia si hubo movimiento válido
        else:
            contador_salta_turno += 1
            turno = 2 if turno == 1 else 1  # Cambia turno correctamente
            
    return ganador(estado, turno)


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


