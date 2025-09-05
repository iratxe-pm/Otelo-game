import numpy as np
from reglas_juego.estado_juego import EstadoJuego
from reglas_juego.movimientos import posibles_movimientos
from reglas_juego.avance_juego import partida_simulada, turnos, sincronizar_fichas_desde_tablero
import math
import random
from copy import deepcopy
from keras.models import load_model

red_otelo = load_model("red_otelo.h5")
class crear_nodo:
    """
    Clase que representa un nodo en el árbol de búsqueda MCTS.

    Atributos:
        posicion (EstadoJuego): Estado actual del tablero con la acción aplicada.
        turno (int): Turno del jugador para este nodo (1=negras, 2=blancas).
        padre (crear_nodo): Nodo padre en el árbol.
        action (list): Acción que llevó a este estado (fila, columna).
        hijos (list): Lista de nodos hijos (estados sucesores).
        acciones_posibles (list): Acciones legales posibles desde este nodo.
        acciones_hechas (list): Acciones ya exploradas/expandidas.
        visitas (int): Número de veces que se ha visitado este nodo.
        recompensa_acomulada (float): Recompensa acumulada para el nodo.
    """
    def __init__ (self, estado, turno, padre= None, action= None):
        self.posicion = estado 
        self.turno = turno 
        self.padre = padre 
        self.action = action 
        self.hijos = [] 
        self.acciones_posibles = posibles_movimientos(estado,turno) 
        self.acciones_hechas = [] 
        self.visitas = 0 
        self.recompensa_acomulada = 0
        
def mcts(tablero,turno,iteraccion = 10):
    """
    Ejecuta el algoritmo Monte Carlo Tree Search (MCTS) para elegir la mejor acción desde un estado dado.

    Parámetros:
        tablero (list): Estado actual del tablero (matriz 8x8).
        turno (int): Turno del jugador actual (1=negras, 2=blancas).
        iteraccion (int, opcional): Número de iteraciones para la búsqueda MCTS (por defecto 100).

    Retorna:
        list: Acción seleccionada (fila, columna) que maximiza el valor esperado.

    * NOTA: si se quiere ejecutar el mcts sin red neuronal haga:
        1º descomente la línea: " #partida_simulada = simulacion(nodo_seleccionado) " (Línea: 63)
        2º comentar la línea: " partida_simulada_con_red = simulacion_con_red(nodo_seleccionado) " (Línea 64)
        3º cambie en la llamada al método retropopagación(partida_simulada_con_red, nodo_seleccionado) (Línea 65)
            partida_simulada_con_red por partida_simulada
    """
    estado_inicial = EstadoJuego()
    estado_inicial.tablero = deepcopy(tablero)
    sincronizar_fichas_desde_tablero(estado_inicial)
    
    raiz = crear_nodo(estado_inicial,turno)
    turno_raiz = turno
    for i in range(0,iteraccion):
        nodo_seleccionado = seleccion_nodo_siguiente(raiz)
        #partida_simulada = simulacion(nodo_seleccionado)
        partida_simulada_con_red = simulacion_con_red(nodo_seleccionado)
        retropopagación(partida_simulada_con_red, nodo_seleccionado, turno_raiz)

    return seleccion_hijo_uct(raiz).action


def seleccion_nodo_siguiente(nodo):
    """
    Selecciona recursivamente el siguiente nodo a expandir usando el criterio UCT.
    Si no se ha expandido completamente, se expande; si ya está expandido, selecciona por UCT.

    Parámetros:
        nodo (crear_nodo): Nodo actual en el árbol.

    Retorna:
        crear_nodo: Nodo seleccionado para expansión o nodo terminal si la partida finalizó.
    """
    if (len(posibles_movimientos(nodo.posicion,1)) == 0 and len(posibles_movimientos(nodo.posicion,2)) == 0):
        return nodo
    
    if (len(nodo.acciones_posibles) != len(nodo.acciones_hechas)):
        return expandir(nodo)
    
    hijo_mejor_uct = seleccion_hijo_uct(nodo)

    return seleccion_nodo_siguiente(hijo_mejor_uct)

def expandir(nodo):
    """
    Expande un nodo explorando una acción no visitada previamente, creando un nuevo hijo.

    Parámetros:
        nodo (crear_nodo): Nodo a expandir.

    Retorna:
        crear_nodo: Nuevo nodo hijo creado tras aplicar una acción no explorada.
    """
    for accion in nodo.acciones_posibles:
        if accion not in nodo.acciones_hechas:
            estado_copia = deepcopy(nodo.posicion)
            turno_siguiente, estado_nuevo = turnos(nodo.turno, accion[0], accion[1], estado_copia)
            nodo_obtenido = crear_nodo(estado_nuevo, turno_siguiente, nodo, accion)
            nodo.hijos.append(nodo_obtenido)
            nodo.acciones_hechas.append(accion)
            return nodo_obtenido
    return nodo


def seleccion_hijo_uct(nodo):
    """
    Selecciona el hijo del nodo con el mejor valor UCT (Upper Confidence Bound applied to Trees).
    Si un hijo no ha sido visitado se le asigna valor infinito para asegurar exploración.

    Parámetros:
        nodo (crear_nodo): Nodo padre cuyos hijos se evaluarán.

    Retorna:
        crear_nodo: Nodo hijo con el valor UCT más alto, desempatando al azar si es necesario.
    """
    c = math.sqrt(2)
    uct_mejor = float("-inf") 
    mejor_hijo = []
    for hijo in nodo.hijos:
        recompensa = hijo.recompensa_acomulada
        n_visitas = hijo.visitas
        if (n_visitas == 0): 
            uct = float("inf")
        else:
            uct = (recompensa / n_visitas) + c * math.sqrt((2 * math.log(nodo.visitas)) / n_visitas)
        
        if(uct > uct_mejor):
            uct_mejor = uct
            mejor_hijo = [hijo]
        elif (uct == uct_mejor):
            mejor_hijo.append(hijo) 

    hijo_seleccionado = random.choice(mejor_hijo) 
             
    return hijo_seleccionado

def simulacion(nodo):
    """
    Simula una partida desde el estado del nodo con movimientos aleatorios hasta finalizar la partida.

    Parámetros:
        nodo (crear_nodo): Nodo desde el cual se simula la partida.

    Retorna:
        int: Resultado de la simulación (1: gana jugador actual, -1: pierde, 0: empate).
    """
    resultado, _ , _ = partida_simulada(nodo.turno, nodo.posicion)
    return resultado

def simulacion_con_red(nodo):
    """
    Simula una partida desde el estado del nodo y evalúa el resultado con una red neuronal entrenada.

    Parámetros:
        nodo (crear_nodo): Nodo desde el cual se simula y evalúa la partida.

    Retorna:
        int: Predicción de la red neuronal sobre la probabilidad de victoria para el jugador actual.

     * NOTA: si se quiere ejecutar el mcts sin red neuronal haga:

        1º descomente las líneas comentadas (Línea 173, 174, 175)
        2º comente las líneas 177, 178 (las dos siguientes)

    """
    #resultado, tablero, turno = partida_simulada(nodo.turno, nodo.posicion)
    #tablero_vector = np.array(tablero).flatten()
    #turno_vector = np.array([turno])

    tablero_vector = np.array(nodo.posicion.tablero).flatten()
    turno_vector = np.array([nodo.turno])
    entrada_red = np.concatenate((tablero_vector, turno_vector))
    prediccion = red_otelo.predict(np.array([entrada_red]), verbose=0)[0][0]

    return prediccion

def retropopagación (partida_simulada, nodo, turno_raiz):
    """
    Propaga hacia arriba en el árbol los resultados de la simulación, actualizando visitas y recompensas.

    Parámetros:
        partida_simulada (int): Resultado o recompensa de la simulación desde el nodo.
        nodo (crear_nodo): Nodo desde donde se inicia la propagación hacia el padre.
        turno_raiz (turno): El turno desde el cual se simula la partida.
    """
    actual = nodo
    turno_actual = nodo.turno
    while actual is not None:
        actual.visitas += 1
        recompensa = 0
        # recompensa vista desde la raíz
        if turno_raiz == turno_actual:
            if partida_simulada == 1:
                recompensa = 1
            if partida_simulada == 0:
                recompensa = 0
            else:
                recompensa = -1
        elif turno_raiz != turno_actual:
            if partida_simulada == 1:
                recompensa = -1
            if partida_simulada == 0:
                recompensa = 0
            else:
                recompensa = 1

        actual.recompensa_acomulada += recompensa
        actual = actual.padre

