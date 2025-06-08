
"""
partidas = 1

def partida_ia_vs_ia():
    return 2

fichero_ia_vs_ia = pd.DataFrame()#crea un dataframe vacío sin líneas ni columnas
#dataframe cada columna puede tener un tipo distinto


def crear_linea_csv(tablero,turno, ganador):
    #esto sirve para crear la linea del csv, le paso el tablero, el estado del tablero, sale el 1,2 según la coordenada, y guarda, el que gana 
    linea = tablero.copy()#aqui creo las columnas del dataframe, esto se lo paso luego al dataframe; es asi porque tablero
    #es un diccionario, entonces tiene (0,0),(0,1),... hasta el final
    #y ahora le añado estas dos columnas, con ese valor
    linea["turno"] = turno
    linea["ganador"] = ganador #en este diccionario que es el tablero, añado una clave para guardar al ganador y su valor
    return linea

for i in range(partidas+1):

    sigue_jugando = True

    turno = 1 #se empieza siempre por elturno 1

    tablero = tablero(ficha_blanca(), ficha_negra()) #creo un tablero vacío

    partida_realizada = [] #sirve para ir guardando los estados de la partida para después añadirlos en el csv

    while sigue_jugando :

        #compruebo si se ha terminado la partida
        if((len(posibles_movimientos(tablero,1)) == 0) and (len(posibles_movimientos(tablero,2)) == 0)) :
            ganador = ganador(turno)
            for linea in partida_realizada:
                if(linea[1] == turno):
                    linea[2] = ganador
                else:
                    if(ganador == 0):
                        linea[2] = 0
                    elif (ganador == 1):
                        linea[2] = -1
                    else:
                        linea[2] = 1

                #concatena lo que ya tenia guardado con el nuevo creado de esta partida
                #lo de ignore_index, ignora los indices anteriores
                df_estados_partidas = pd.concat([df_estados_partidas, pd.DataFrame([linea])], ignore_index=True)
            break

        if len(posibles_movimientos(tablero,turno)) == 0 :
            turno = 3 - turno
            continue

        accion_elegida = mcts(tablero,turno)

        turnos(turno,accion_elegida[0],accion_elegida[1],tablero)

        #en cada estado, se especifica al principio antes de saber quien es de verdad el ganador, se pone quien va ganando de momento
        ganador = ganador(turno)

        nueva_linea = crear_linea_csv(tablero,turno,ganador)
        partida_realizada.append(nueva_linea)

        turno = 3 - turno
        """

from reglas_juego.avance_juego_automatico import turnos
from reglas_juego.inicializa_tablero import tablero, ficha_blanca, ficha_negra, mostrar_tablero
from reglas_juego.movimientos import posibles_movimientos
from reglas_juego.avance_de_juego import modificar_tablero
from mcts import mcts  # Asegúrate de importar tu función MCTS correctamente
from reglas_juego.estado_juego import EstadoJuego

import time

def partida_ia_vs_ia():
    estado = EstadoJuego()
    estado.tablero = tablero(ficha_blanca(), ficha_negra())    
    turno = 1  # Empieza la ficha blanca (o cambia a 2 si prefieres que empiece negra)

    print("Inicio de la partida IA vs IA")
    mostrar_tablero(estado.tablero)
    while True:
        movimientos = posibles_movimientos(estado, turno)
        if not movimientos:
        # Comprobar si el otro jugador también está bloqueado
            if not posibles_movimientos(estado, 3 - turno):
                break
            turno = 3 - turno
            continue

        accion = mcts(estado.tablero, turno)
        turno, estado.tablero = turnos(turno, accion[0], accion[1], estado)

        print(f"\nIA con turno {turno} coloca ficha en {accion}")
        mostrar_tablero(estado.tablero)
        time.sleep(1)
   
    
        

