# PARTIDA IA VS IA
import random
from reglas_juego.avance_juego import ganador, turnos
from reglas_juego.movimientos import posibles_movimientos

def partida_automática(turno, estado):
    contador_salta_turno = 0
    
    while contador_salta_turno<2:

                movimientos = posibles_movimientos(estado,turno)
                if (len(movimientos) != 0):
                    accion_seleccionada = random.choice(movimientos)
                    turno = turnos(turno, accion_seleccionada[0], accion_seleccionada[1], estado)[0]   
                    contador_salta_turno = 0
                    
                else:
                    contador_salta_turno +=1
                    if turno == 1:
                        turno = 2
                    else: 
                        turno = 1

    return ganador(estado,turno)
