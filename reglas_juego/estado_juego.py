class EstadoJuego:
    def __init__(self):
        self.fichas_blancas = [[3, 4], [4, 3]]
        self.fichas_negras = [[4, 4], [3, 3]]
        self.tablero = self.inicializar_tablero()

    def inicializar_tablero(self):
        Tablero = [[0 for _ in range(8)] for _ in range(8)]
        for i in self.fichas_blancas:
            Tablero[i[0]][i[1]] = 1
        for i in self.fichas_negras:
            Tablero[i[0]][i[1]] = 2
        return Tablero

    def ficha_negra(self, extra=None):
        if extra:
            self.fichas_negras.append(extra)
        return self.fichas_negras

    def ficha_blanca(self, extra=None):
        if extra:
            self.fichas_blancas.append(extra)
        return self.fichas_blancas
