import juego_otelo 
import math
import random
#los de ficha negra son los nodos de nivel impar, y lo de blanca se encuentran en el nivel par

"""
Funcionamiento:
se crea un árbol y por cada nodo que se accede; al principio uno de los hijos de raiz
"""


class crear_nodo:
    def __init__ (self, tablero, turno, padre= None, action= None):
        self.posicion = tablero #guarda la posicion del tablero,  con la accion action ya implicada
        self.turno = turno #guarda el turno de este estado en concreto
        self.padre = padre #el estado anterior
        self.action = action #guarda la accion que hace que lleguen a ese nodo
        self.hijos = [] #guarda los hijos de ese nodo; son los nuevos estados del tablero
        self.acciones_posibles = juego_otelo.posibles_movimientos(tablero,turno) #aqui guarda las acciones de ese nodo que pueda tomar
        self.acciones_realizadas = [] #para comprobar si se ha extendido del todo o no el nodo
        #estos dos de abajo sirve para calcular después el UCT 
        self.visitas = 0 #se guarda el numero de veces q se accede a este nodo; al inicio es 0 pq solo se crea no se visita
        self.recompensa_acomulada = 0 #va guardando la recompensa
        

#uct valor de la constante es sqrt(2) pq lo dice q lo hagamos segun un documento a survey of monte carlo tree search methods
#1000 iteraciones
#el mcts primero explora todos sus hijos, y luego cuando ya cuando se conozca se explota
def mcts(tablero,turno,iteraccion = 1000):
    raiz = crear_nodo(tablero,turno)
    for i in range(0,iteraccion):
        #se le manda el nodo raiz, porque la selección siempre se empieza por el nodo raí
        nodo_seleccionado = seleccion_nodo_siguiente(raiz)
    accion = [0,0]
    return accion

#primera fase del árbol mcts

def seleccion_nodo_siguiente(nodo):

    #este if es por si cuando se busca el nodo, si la partida se ha acabado, entonces elige ese nodo y no se expande
    #si cumple este if, significa que es un nodo terminal
    #se pone asi porque tiene que comprobar los dos turnos
    if (len(juego_otelo.posibles_movimientos(nodo.posicion,1)) == 0 and len(juego_otelo.posibles_movimientos(nodo.posicion,2)) == 0):
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
    for accion in nodo.acciones_posibles:
        if not accion in nodo.acciones_hechas:
            tablero_nuevo = nodo.tablero[accion[0]][accion[1]]
            if(nodo.turno == 2):
                turno = 1
            else:
                turno = 2
            nodo_obtenido = crear_nodo(tablero_nuevo,turno,nodo,accion)
            nodo.hijos.append(nodo_obtenido)
            #si la accion no se ha tomado todavía entonces se sigue y se añade a la lista de acciones ya hechas
            nodo.acciones_hechas.append(accion)
            return nodo_obtenido

def seleccion_hijo_uct(nodo):
    c = math.sqrt(2)
    uct_mejor = 0 #al inicio del todo el uct mejor es 0
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


    

