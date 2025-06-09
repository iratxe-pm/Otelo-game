from reglas_juego.excepciones import JugadorInvalidoError, MovimientoInvalidoError
from reglas_juego.cambio_fichas import cambio_de_color_fichas
from reglas_juego.movimientos import reglas_de_movimiento,posibles_movimientos 
import random

def turnos(turno_llega, new_fila, new_columna, estado):
    """
    Actualiza el estado del juego y alterna el turno tras un movimiento válido.

    Algoritmo:
        1. Se verifica si el movimiento es válido llamando a `reglas_de_movimiento`.
            1.1. Si el movimiento es válido, se actualizan las fichas capturadas y el tablero,
                 añadiendo la nueva ficha según el jugador actual.
                 Luego, se alterna el turno al jugador contrario.
        2. Si el turno recibido no es 1 ni 2, se lanza `JugadorInvalidoError`.
        3. Si el movimiento no cumple las reglas, se lanza `MovimientoInvalidoError`.

    Parámetros:
        turno_llega (int): Identificador del jugador actual (1 = negras, 2 = blancas).
        new_fila (int): Fila donde se quiere colocar la nueva ficha.
        new_columna (int): Columna donde se quiere colocar la nueva ficha.
        estado (EstadoJuego): Objeto que contiene el tablero y las posiciones de fichas.

    Excepciones:
        JugadorInvalidoError: Se lanza si el turno no es ni 1 ni 2.
        MovimientoInvalidoError: Se lanza si el movimiento no es válido según las reglas.

    Retorna:
        tuple:
            - int: Turno del siguiente jugador (1 o 2).
            - EstadoJuego: Estado actualizado del juego con el tablero modificado.
    """

    if(reglas_de_movimiento(estado,turno_llega,new_fila,new_columna)):
        cambio_de_color_fichas(estado,turno_llega,new_fila,new_columna)
        if turno_llega == 1: 
            estado.tablero[new_fila][new_columna] = 2  
            estado.ficha_negra([new_fila,new_columna])
            turno = 2 
            
        elif turno_llega == 2: 
            estado.tablero[new_fila][new_columna] = 1 
            estado.ficha_blanca([new_fila,new_columna])
            turno = 1 
        
        else:
            turno = turno_llega
            raise JugadorInvalidoError()
    else: 
        turno = turno_llega
        raise MovimientoInvalidoError()

    return turno, estado

def sincronizar_fichas_desde_tablero(estado):
    """
    Sincroniza las listas de fichas blancas y negras con el estado actual del tablero.

    Este método actualiza las listas `fichas_blancas` y `fichas_negras` del objeto `estado`
        para que reflejen correctamente la posición de las fichas en el tablero, según los valores almacenados.

    Algoritmo:
        1. Recorre todas las casillas del tablero.
        2. Si el valor de una casilla es 1, añade sus coordenadas a `fichas_blancas`.
        3. Si el valor de una casilla es 2, añade sus coordenadas a `fichas_negras`.

    Parámetros:
        estado (EstadoJuego): Instancia del estado del juego que contiene el tablero y las listas de fichas.
    """
    estado.fichas_blancas = []
    estado.fichas_negras = []
    for fila in range(8):
        for col in range(8):
            if estado.tablero[fila][col] == 1:
                estado.fichas_blancas.append([fila, col])
            elif estado.tablero[fila][col] == 2:
                estado.fichas_negras.append([fila, col])


def partida_simulada(turno_llega, estado):
    """
    Se utiliza para crear los datos de entrenamiento de la red neuronal

    Simula una partida automática entre dos jugadores hasta que se termine el juego o se produzcan dos turnos consecutivos sin movimientos posibles.

    Algoritmo:
        1. Mientras no se hayan producido dos turnos consecutivos sin movimientos y el juego no haya terminado:
            - Obtiene los posibles movimientos para el jugador actual.
            - Si hay movimientos:
                - Elige uno al azar y ejecuta el movimiento con la función `turnos`.
                - Si el movimiento es inválido, captura la excepción y detiene la simulación.
                - Reinicia el contador de turnos sin movimiento.
            - Si no hay movimientos:
                - Incrementa el contador de turnos sin movimiento.
                - Cambia el turno al jugador contrario.
        2. Al terminar, determina el ganador con la función `ganador`.

    Parámetros:
        turno_llega (int): Turno del jugador que inicia la simulación (1 = negras, 2 = blancas).
        estado (EstadoJuego): Estado inicial del juego.

    Excepciones:
        MovimientoInvalidoError: Se lanza si el movimiento no es válido según

    Retorna:
        tuple:
            - gana (int): Resultado de la partida (1 si gana el jugador actual, -1 si pierde, 0 empate).
            - tablero (list): Estado final del tablero (matriz 8x8).
            - turno (int): Turno del jugador que finaliza la partida.
    """
    contador_salta_turno = 0
    turno = turno_llega
    
    while contador_salta_turno < 2 and not estado.is_terminal():
        movimientos = posibles_movimientos(estado, turno)
        
        if movimientos:
            accion_seleccionada = random.choice(movimientos)
            try:
                turno, estado = turnos(turno, accion_seleccionada[0], accion_seleccionada[1], estado)
            except MovimientoInvalidoError:
                print(f"Movimiento inválido en partida automática: turno {turno}, acción {accion_seleccionada}")
                break
            contador_salta_turno = 0  
        else:
            contador_salta_turno += 1
            turno = 2 if turno == 1 else 1  
            
    gana = ganador(estado, turno)
    return gana, estado.tablero, turno


def ganador(estado, turno):
    """
    Determina el ganador de la partida basándose en la cantidad de fichas de cada color y el turno en que finaliza.

    Algoritmo:
        1. Cuenta la cantidad de fichas negras y blancas.
        2. Si hay más fichas negras, devuelve 1 si el turno es de negras (1), o -1 si es de blancas (2).
        3. Si hay más fichas blancas, devuelve 1 si el turno es de blancas (2), o -1 si es de negras (1).
        4. En caso de empate, devuelve 0.

    Parámetros:
        estado (EstadoJuego): Objeto que contiene el tablero y las posiciones de fichas.
        turno (int): Identificador del jugador actual (1 = negras, 2 = blancas).

    Retorno:
        int: 
            - 1 si gana el jugador correspondiente al turno actual,
            - -1 si pierde,
            - 0 en caso de empate.
    """
    if (len(estado.ficha_negra()) > len(estado.ficha_blanca())):
        if turno == 1:
            return 1
        else:
            return -1

    elif (len(estado.ficha_negra()) < len(estado.ficha_blanca())):
        if turno == 1:
            return -1
        else:
            return 1
    else:
        return 0          


