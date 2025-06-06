#Ficha negra
#Lista de fichas negras que están en el tablero, cada vez que hay una nueva ficha blanca se añade a esta lista
lista_negra=  [[4, 4], [3, 3]]
def ficha_negra (extra = None):
    if extra:
        lista_negra.append(extra)
    return lista_negra


#Ficha blanca
#Lista de fichas blancas que están en el tablero, cada vez que hay una nueva ficha blanca se añade a esta lista
lista_blanca = [[3, 4], [4, 3]]
def ficha_blanca (extra = None):
    if extra:
        lista_blanca.append(extra)
    return lista_blanca
#Ganadores
#Lista los ganadores de las partidas anteriores
lista_ganadores=  []
def ganadores (extra = None):
    if extra:
        lista_ganadores.append(extra)
    return lista_ganadores


#Se encarga de mostrar el tablero y las fichas
def mostrar_tablero(tablero):
    print("\n   0   1   2   3   4   5   6   7")
    print("  +---+---+---+---+---+---+---+---+")
    blancas_coords = []
    negras_coords = []

    for fila in range(8):
        print(f"{fila} |", end="")
        for columna in range(8):
            if tablero[fila][columna] == 0:
                print("   |", end="")
            elif tablero[fila][columna] == 2:
                print(" ● |", end="")  # Negra
                negras_coords.append((fila, columna))
            else:
                print(" ○ |", end="")  # Blanca
                blancas_coords.append((fila, columna))
        print("\n  +---+---+---+---+---+---+---+---+")

#inicializa tablero:
# 0 = casilla vacía, 2 = ficha negra, 1 = ficha blanca
# estado inicial del tablero

def tablero(blanca, negra) : 
    Tablero = []
    for fila in range (0,8):
        Fila = []
        for columna in range (0,8):
            Fila.append(0)
        Tablero.append(Fila)

    for i in blanca:
        Tablero [i[0]][i[1]] = 1

    for i in negra:
        Tablero [i[0]][i[1]] = 2

    return Tablero