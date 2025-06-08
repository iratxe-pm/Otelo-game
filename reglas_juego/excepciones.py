class MovimientoInvalidoError(Exception):
    def __init__(self, mensaje="Movimiento inválido según las reglas del juego."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class JugadorInvalidoError(Exception):
    def __init__(self, mensaje="Turno inválido. Jugador no reconocido."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)