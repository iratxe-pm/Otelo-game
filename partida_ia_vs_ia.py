from reglas_juego.avance_juego_automatico import turnos, ganador
from reglas_juego.inicializa_tablero import tablero, ficha_blanca, ficha_negra, mostrar_tablero
from reglas_juego.movimientos import posibles_movimientos
from reglas_juego.avance_de_juego import modificar_tablero
from mcts import mcts  # Asegúrate de importar tu función MCTS correctamente
from reglas_juego.estado_juego import EstadoJuego
import pandas as pd

import time

def crear_linea_csv(tablero,turno, ganador):
    linea = {}
    for fila in range(8):
        for columna in range(8):
            clave = f"({fila}, {columna})"
            linea[clave] = tablero[fila][columna]
    
    linea["turno"] = turno
    linea["ha_ganado"] = ganador
    #esto sirve para crear la linea del csv, le paso el tablero, el estado del tablero, sale el 1,2 según la coordenada, y guarda, el que gana 
    #aqui creo las columnas del dataframe, esto se lo paso luego al dataframe; es asi porque tablero
    #es un diccionario, entonces tiene (0,0),(0,1),... hasta el final
    #y ahora le añado estas dos columnas, con ese valor
    return linea


def partida_ia_vs_ia():
    estado = EstadoJuego()
    turno = 1  
    partidas = 1


    fichero_ia_vs_ia = pd.DataFrame()#crea un dataframe vacío sin líneas ni columnas
    #dataframe cada columna puede tener un tipo distinto

    
    for i in range(partidas+1):

        sigue_jugando = True

        turno = 1 #se empieza siempre por elturno 1

        tablero = estado.tablero #creo un tablero vacío

        partida_realizada = [] #sirve para ir guardando los estados de la partida para después añadirlos en el csv

        while sigue_jugando :

            #compruebo si se ha terminado la partida
            if((len(posibles_movimientos(estado,1)) == 0) and (len(posibles_movimientos(estado,2)) == 0)) :
                ganadore = ganador(estado,turno)
                for linea in partida_realizada:
                    if(linea["turno"] == turno):
                        linea["ha_ganado"] = ganadore
                    else:
                        if(ganador == 0):
                            linea["ha_ganado"] = 0
                        elif (ganador == 1):
                            linea["ha_ganado"] = -1
                        else:
                            linea["ha_ganado"] = 1
                    

                    #concatena lo que ya tenia guardado con el nuevo creado de esta partida
                    #lo de ignore_index, ignora los indices anteriores
                    fichero_ia_vs_ia = pd.concat([fichero_ia_vs_ia, pd.DataFrame([linea])], ignore_index=True)
                break

            if len(posibles_movimientos(estado,turno)) == 0 :
                turno = 3 - turno
                continue

            accion_elegida = mcts(tablero,turno)

            turnos(turno,accion_elegida[0],accion_elegida[1],estado)

            #en cada estado, se especifica al principio antes de saber quien es de verdad el ganador, se pone quien va ganando de momento
            ganadore = ganador(estado,turno)

            nueva_linea = crear_linea_csv(tablero,turno,ganadore)
            partida_realizada.append(nueva_linea)

            turno = 3 - turno

    fichero_ia_vs_ia.to_csv('partida_ia_vs_ia.csv', index=False)

"""
    print("Inicio de la partida IA vs IA")
    estado_tab = estado.tablero
    mostrar_tablero(estado_tab)

    while True:
        # 1) CONSEGUIR movimientos con el nombre CORRECTO:
        movimientos = posibles_movimientos(estado, turno)
        if not movimientos:
            if(turno == 1):
            # 1a) ni tú ni el oponente pueden mover → fin
                if not posibles_movimientos(estado, 3 - turno):
                    break
            # 1b) solo tú no puedes → pasa el turno
            turno = 3 - turno
            continue
        
        else:
            # 2) pides jugada a MCTS
            accion = mcts(estado_tab, turno)
            print("accion que elige por que si",accion)

            # 3) guardas antes quién mueve
            jugador_actual = turno
            print(f"\nIA con ficha {'●' if jugador_actual==1 else '⚪'} coloca en {accion}")

            # 4) aplicas la jugada
            turno, estado_ent = turnos(jugador_actual, accion[0], accion[1], estado)
            estado_tab = estado_ent.tablero

            # 5) muestras el nuevo tablero
            mostrar_tablero(estado_tab)
            time.sleep(1)
            """

