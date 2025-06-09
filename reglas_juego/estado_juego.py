class EstadoJuego:
    """
    Representa el estado actual del juego, incluyendo la posición de las fichas blancas y negras y el tablero.

    Atributos:
        fichas_blancas (list): Lista de posiciones [fila, columna] de fichas blancas.
        fichas_negras (list): Lista de posiciones [fila, columna] de fichas negras.
        tablero (list): Matriz 8x8 que representa el tablero con 0 = vacío, 1 = ficha blanca, 2 = ficha negra.
    """
    def __init__(self):
        """
        Inicializa el estado del juego con las posiciones iniciales de las fichas blancas y negras, 
            y construye el tablero llamando a la función `inicializar_tablero`.
        """
        self.fichas_blancas = [[3, 4], [4, 3]]
        self.fichas_negras = [[4, 4], [3, 3]]
        self.tablero = self.inicializar_tablero()

    def inicializar_tablero(self):
        """
        Crea el tablero vacío de 8x8 y coloca las fichas blancas y negras en sus posiciones iniciales.

        Retorna:
            list: Matriz 8x8 con el estado inicial del tablero.
        """
        Tablero = [[0 for _ in range(8)] for _ in range(8)]
        for i in self.fichas_blancas:
            Tablero[i[0]][i[1]] = 1
        for i in self.fichas_negras:
            Tablero[i[0]][i[1]] = 2
        return Tablero

    def ficha_negra(self, extra=None):
        """
        Obtiene la lista de posiciones de fichas negras, y opcionalmente añade una nueva ficha.

        Parámetros:
            extra (list, opcional): Posición [fila, columna] de una ficha negra a añadir.

        Retorna:
            list: Lista actualizada de posiciones de fichas negras.
        """
        if extra:
            self.fichas_negras.append(extra)
        return self.fichas_negras

    def ficha_blanca(self, extra=None):
        """
        Obtiene la lista de posiciones de fichas blancas, y opcionalmente añade una nueva ficha.

        Parámetros:
            extra (list, opcional): Posición [fila, columna] de una ficha blanca a añadir.

        Retorna:
            list: Lista actualizada de posiciones de fichas blancas.
        """
        if extra:
            self.fichas_blancas.append(extra)
        return self.fichas_blancas
    def is_terminal(self):
        """
        Indica si el juego ha terminado: no quedan casillas vacías o ninguno de los jugadores
        tiene movimientos.
        """
        # Se puede mejorar comprobando saltos consecutivos, pero simplificado:
        vacias = any(self.tablero[f][c] == 0 for f in range(8) for c in range(8))
        return not vacias