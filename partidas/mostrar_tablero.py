#Se encarga de mostrar el tablero y las fichas
def mostrar_tablero(tablero):
    print("\n   0   1   2   3   4   5   6   7")
    print("  +---+---+---+---+---+---+---+---+")

    for fila in range(8):
        print(f"{fila} |", end="")
        for columna in range(8):
            if tablero[fila][columna] == 0:
                print("   |", end="")
            elif tablero[fila][columna] == 2:
                print(" ● |", end="")  # Negra
            else:
                print(" ○ |", end="")  # Blanca
        print("\n  +---+---+---+---+---+---+---+---+")

