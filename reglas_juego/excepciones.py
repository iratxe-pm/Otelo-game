class MovimientoInvalidoError(Exception):
    def __init__(self, mensaje="Movimiento inválido según las reglas del juego."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class JugadorInvalidoError(Exception):
    def __init__(self, mensaje="Turno inválido. Jugador no reconocido."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class EntradaNoNumericaError(Exception):
    def __init__(self, valor):
        super().__init__(f"Entrada inválida: '{valor}' no es un número.")
        self.valor = valor
    
def validar_entrada_numerica(entrada):
        if not entrada.isdigit():
            raise EntradaNoNumericaError(entrada)
        return int(entrada)