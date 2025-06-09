def mostrar_tablero(tablero):
    """
    Muestra por consola el estado del tablero de Othello/Reversi con coordenadas y fichas.

    Imprime las coordenadas de filas y columnas, y representa cada casilla como:
      - Espacio vacío si el valor es 0.
      - ● para fichas negras (valor 2).
      - ○ para fichas blancas (valor 1).

    Parámetro:
        tablero (List[List[int]]): Matriz 8×8 con los valores:
            0 = casilla vacía,
            1 = ficha blanca,
            2 = ficha negra.
    """
    print("\n   0   1   2   3   4   5   6   7")
    print("  +---+---+---+---+---+---+---+---+")

    for fila in range(8):
        print(f"{fila} |", end="")
        for columna in range(8):
            if tablero[fila][columna] == 0:
                print("   |", end="")
            elif tablero[fila][columna] == 2:
                print(" ● |", end="")  
            else:
                print(" ○ |", end="") 
        print("\n  +---+---+---+---+---+---+---+---+")

