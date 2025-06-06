import juego_otelo 
#los de ficha negra son los nodos de nivel impar, y lo de blanca se encuentran en el nivel par

"""
Funcionamiento:
se crea un árbol y por cada nodo que se accede; al principio uno de los hijos de raiz
"""


class nodo:
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

#primera fase del árbol mcts
def seleccion_nodo_siguiente(nodo):

    #este if es por si cuando se busca el nodo, si el nodo es terminal
    if (len(juego_otelo.posibles_movimientos(nodo.posicion,1)) == 0 and len(juego_otelo.posibles_movimientos(nodo.posicion,2)) == 0):
        return nodo
