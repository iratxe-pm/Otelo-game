import numpy as np
from reglas_juego.estado_juego import EstadoJuego
from reglas_juego.movimientos import posibles_movimientos
from reglas_juego.avance_juego import partida_simulada, turnos, sincronizar_fichas_desde_tablero
import math
import random
from copy import deepcopy
from keras.models import load_model

#los de ficha negra son los nodos de nivel impar, y lo de blanca se encuentran en el nivel par

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
        self.posicion = estado #guarda la posicion del tablero,  con la accion action ya implicada
        self.turno = turno #guarda el turno de este estado en concreto
        self.padre = padre #el estado anterior
        self.action = action #guarda la accion que hace que lleguen a ese nodo
        self.hijos = [] #guarda los hijos de ese nodo; son los nuevos estados del tablero
        self.acciones_posibles = posibles_movimientos(estado,turno) #aqui guarda las acciones de ese nodo que pueda tomar
        self.acciones_hechas = [] #para comprobar si se ha extendido del todo o no el nodo
        #estos dos de abajo sirve para calcular después el UCT 
        self.visitas = 0 #se guarda el numero de veces q se accede a este nodo; al inicio es 0 pq solo se crea no se visita
        self.recompensa_acomulada = 0 #va guardando la recompensa
        

#uct valor de la constante es sqrt(2) pq lo dice q lo hagamos segun un documento a survey of monte carlo tree search methods
#1000 iteraciones
#el mcts primero explora todos sus hijos, y luego cuando ya cuando se conozca se explota
def mcts(tablero,turno,iteraccion = 100):
    """
    Ejecuta el algoritmo Monte Carlo Tree Search (MCTS) para elegir la mejor acción desde un estado dado.

    Parámetros:
        tablero (list): Estado actual del tablero (matriz 8x8).
        turno (int): Turno del jugador actual (1=negras, 2=blancas).
        iteraccion (int, opcional): Número de iteraciones para la búsqueda MCTS (por defecto 100).

    Retorna:
        list: Acción seleccionada (fila, columna) que maximiza el valor esperado.
    """
    estado_inicial = EstadoJuego()
    estado_inicial.tablero = deepcopy(tablero)
    sincronizar_fichas_desde_tablero(estado_inicial)  # Sincronizamos fichas con tablero
    
    raiz = crear_nodo(estado_inicial,turno)
    for i in range(0,iteraccion):
        #se le manda el nodo raiz, porque la selección siempre se empieza por el nodo raí
        nodo_seleccionado = seleccion_nodo_siguiente(raiz)
        #partida_simulada = simulacion(nodo_seleccionado)
        partida_simulada_con_red = simulacion_con_red(nodo_seleccionado)
        retropopagación(partida_simulada_con_red, nodo_seleccionado)

    return seleccion_hijo_uct(raiz).action

#primera fase del árbol mcts

def seleccion_nodo_siguiente(nodo):
    """
    Selecciona recursivamente el siguiente nodo a expandir usando el criterio UCT.
    Si no se ha expandido completamente, se expande; si ya está expandido, selecciona por UCT.

    Parámetros:
        nodo (crear_nodo): Nodo actual en el árbol.

    Retorna:
        crear_nodo: Nodo seleccionado para expansión o nodo terminal si la partida finalizó.
    """

    #este if es por si cuando se busca el nodo, si la partida se ha acabado, entonces elige ese nodo y no se expande
    #si cumple este if, significa que es un nodo terminal
    #se pone asi porque tiene que comprobar los dos turnos
    if (len(posibles_movimientos(nodo.posicion,1)) == 0 and len(posibles_movimientos(nodo.posicion,2)) == 0):
        return nodo
    
    #esta es para ver que si se ha expandido; es decir que el nodo se puede expandir mas
    if (len(nodo.acciones_posibles) != len(nodo.acciones_hechas)):
        return expandir(nodo)
    
    
    #uct solo se usa cuando el nodo ya ha sido extendido, por lo tanto los hijos del nodo ya se conocen
    hijo_mejor_uct = seleccion_hijo_uct(nodo)

    #vuelve a llamar a seleccion_nodo_siguiente, para comprobar si:
    # - es terminal o no, en ese caso se devolveria ese nodo
    # - tiene acciones que no se han explorado todavía, es decir que no se ha expandido del todo, por lo que se envía ese nodo a expandir (es del que se partiría)
    # - y sino se cumple nada de los dos otros puntos, es decir no es terminal, y ya se ha expandido del todo, entonces se elige otro nodo 

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
    # Si ya se expandió todo, devuelve el nodo actual para evitar None
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
        if (n_visitas == 0): #por si todavía no se ha visitado
            uct = float("inf")
        else:
            uct = (recompensa / n_visitas) + c * math.sqrt((2 * math.log(nodo.visitas)) / n_visitas)
        
        if(uct > uct_mejor):
            uct_mejor = uct
            mejor_hijo = [hijo]#se guarda en la lista en caso deempate; se hace asi aqui para guardar solamente al de mayot
        elif (uct == uct_mejor):
            mejor_hijo.append(hijo) #en caso de empate, se añaden los dos a la lista

    #en caso de empate se elige uno al azar; si solo hay uno es ese el que se escoge
    hijo_seleccionado = random.choice(mejor_hijo) 
             
    return hijo_seleccionado

    
#simulación 
# solo se aplica la similación al nodo que ha sido elegido para expandirse
# la simulación consiste en simular una partida a partir del estado del tablero en ese momento con movimientos aleatorios
#simulacion aleatoria pa crear csv
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
    """
    resultado, tablero, turno = partida_simulada(nodo.turno, nodo.posicion)
    tablero_vector = np.array(tablero).flatten()
    turno_vector = np.array([turno])
    entrada_red = np.concatenate((tablero_vector, turno_vector))
    prediccion = red_otelo.predict(np.array([entrada_red]), verbose=0)[0][0]

    return prediccion

#retropropagación
def retropopagación (partida_simulada, nodo):
    """
    Propaga hacia arriba en el árbol los resultados de la simulación, actualizando visitas y recompensas.

    Parámetros:
        partida_simulada (int): Resultado o recompensa de la simulación desde el nodo.
        nodo (crear_nodo): Nodo desde donde se inicia la propagación hacia el padre.
    """
    actual = nodo
    while actual is not None:
        actual.visitas += 1
        actual.recompensa_acomulada += partida_simulada
        partida_simulada *= -1  # alternar perspectiva para el oponente xq el padre y el hijo tienen turnos opuestos
        actual = actual.padre #va actualizando todos los anteriores

