from reglas_juego.movimientos import comprobar

def cambio_de_color_fichas(estado, turno, fila, columna):
    """
    Cambia el color de las fichas capturadas tras un movimiento válido.

    Según el turno, determina el color propio y calcula qué fichas del oponente deben cambiar de color tras 
        colocar la ficha en la posición indicada, llamando a la función `obtener_fichas_cambiar`.
    Actualiza las listas de fichas blancas y negras, y el tablero.

    Parámetros:
        estado (EstadoJuego): Objeto que contiene el tablero y las posiciones de fichas.
        turno (int): Identificador del jugador actual (1 = negras, otro = blancas).
        fila (int): Fila donde se quiere colocar la nueva ficha.
        columna (int): Columna donde se quiere colocar la nueva ficha.
    """
    if turno == 2:
        ficha_propia = "blanca"
        fichas_a_cambiar = obtener_fichas_cambiar(estado, ficha_propia, fila, columna)
        for pos in fichas_a_cambiar:
            if pos not in estado.fichas_blancas:
                estado.fichas_blancas.append(pos)
            if pos in estado.fichas_negras:
                estado.fichas_negras.remove(pos)
            estado.tablero[pos[0]][pos[1]] = 1  
    else:
        ficha_propia = "negra"
        fichas_a_cambiar = obtener_fichas_cambiar(estado, ficha_propia, fila, columna)
        for pos in fichas_a_cambiar:
            if pos not in estado.fichas_negras:
                estado.fichas_negras.append(pos)
            if pos in estado.fichas_blancas:
                estado.fichas_blancas.remove(pos)
            estado.tablero[pos[0]][pos[1]] = 2  


def obtener_fichas_cambiar(estado,ficha_propia,posicion_fila_ficha,posicion_columna_ficha):
    """
    Obtiene la lista de fichas del oponente que deben cambiar de color tras colocar una ficha en una posición determinada, 
        siguiendo las reglas del juego.

    Se exploran las ocho direcciones alrededor de la nueva ficha para detectar secuencias de fichas contrarias 
        que quedan "cerradas" por fichas propias. Sólo se devuelven las fichas contrarias que están encerradas y deben cambiar.

    Algoritmo:
        1. Según si la ficha es blanca o negra, asigna las listas de fichas propias y contrarias.
        2. Añade a la lista de propias la nueva casilla en la que se coloca la ficha (simulación).
        3. Itera sobre las 8 posibles direcciones para detectar secuencias cerradas de fichas contrarias.
        4. Si en una dirección hay fichas contrarias seguidas y luego una ficha propia, las fichas contrarias se marcarán para cambiar.

    Parámetros:
        estado (EstadoJuego): Estado actual del juego.
        ficha_propia (str): Color de la ficha que se coloca ("blanca" o "negra").
        posicion_fila_ficha (int): Fila donde se coloca la ficha.
        posicion_columna_ficha (int): Columna donde se coloca la ficha.

    Retorna:
        list: Lista de posiciones [fila, columna] de fichas que deben cambiar de color.
    """
    if ficha_propia == "blanca":
        propias = estado.ficha_blanca()
        contrarias = estado.ficha_negra()
    else:
        propias = estado.ficha_negra()
        contrarias = estado.ficha_blanca()

    propias.append([posicion_fila_ficha, posicion_columna_ficha])

    direcciones = [(-1,0),(1,0),(0,1),(0,-1),(1,-1),(-1,1),(1,1),(-1,-1)]
    fichas_cambiar_global = []

    for dx, dy in direcciones:
        fila, columna = posicion_fila_ficha + dx, posicion_columna_ficha + dy
        fichas_cambiar  = []
        while 0 <= fila < 8 and 0 <= columna < 8 and [fila, columna] in contrarias:
            fichas_cambiar .append([fila, columna])
            fila += dx
            columna += dy
        if [fila, columna] in propias and fichas_cambiar :
            fichas_cambiar_global.extend(fichas_cambiar )

    return fichas_cambiar_global

