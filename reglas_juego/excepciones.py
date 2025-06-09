class MovimientoInvalidoError(Exception):
    """
    Excepción lanzada cuando un movimiento no cumple las reglas del juego.

    Attributes:
        mensaje (str): Descripción del error.
    """
    def __init__(self, mensaje="Movimiento inválido según las reglas del juego."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class JugadorInvalidoError(Exception):
    """
    Excepción lanzada cuando se elige un turno que no es 1 ni 2.

    Attributes:
        mensaje (str): Descripción del error.
    """
    def __init__(self, mensaje="Turno inválido. Jugador no reconocido."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class EntradaNoNumericaError(Exception):
    """
    Excepción lanzada cuando la entrada no es un número válido.

    Atributos:
        valor (str): Valor de la entrada que causó el error.
    """
    def __init__(self, valor):
        super().__init__(f"Entrada inválida: '{valor}' no es un número.")
        self.valor = valor
    
def validar_entrada_numerica(entrada):
    """
    Valida que la entrada sea un número entero positivo.

    Parámetros:
        entrada (_type_): _description_

    Lanza:
        EntradaNoNumericaError: Si la entrada no es un número entero positivo.

    Retorna:
        int: La entrada convertida a entero.
    """
    if not entrada.isdigit():
        raise EntradaNoNumericaError(entrada)
    return int(entrada)


class ValorFueraDeRango(Exception):
    def __init__(self, valor, minimo, maximo):
        super().__init__(f"El valor {valor} no está entre {minimo} y {maximo}")

def verificar_valor_en_rango(valor, minimo, maximo):
    if not (minimo <= valor <= maximo):
        raise ValorFueraDeRango(valor, minimo, maximo)
    
class PosicionOcupada(Exception):
    def __init__(self, fila, columna):
        super().__init__(f"La posición ({fila},{columna}) ya está ocupada en el tablero por otra ficha")

def verificar_poosicion_en_tablero(fila, columna, tablero):
    if tablero[fila][columna] != 0:
        raise PosicionOcupada(fila, columna)