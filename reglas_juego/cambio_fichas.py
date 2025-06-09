##cambio de color
from reglas_juego.movimientos import comprobar

def cambio_de_color_fichas(estado, turno, fila, columna):
    if turno == 2:
        ficha_propia = "blanca"
        fichas_a_cambiar = obtener_fichas_cambiar(estado, ficha_propia, fila, columna)
        for pos in fichas_a_cambiar:
            if pos not in estado.fichas_blancas:
                estado.fichas_blancas.append(pos)
            if pos in estado.fichas_negras:
                estado.fichas_negras.remove(pos)
            estado.tablero[pos[0]][pos[1]] = 1  # Blanca
    else:
        ficha_propia = "negra"
        fichas_a_cambiar = obtener_fichas_cambiar(estado, ficha_propia, fila, columna)
        for pos in fichas_a_cambiar:
            if pos not in estado.fichas_negras:
                estado.fichas_negras.append(pos)
            if pos in estado.fichas_blancas:
                estado.fichas_blancas.remove(pos)
            estado.tablero[pos[0]][pos[1]] = 2  # Negra


#se le manda la ficha a cambiar, en la posicion que se quiere cambiar
def obtener_fichas_cambiar(estado,ficha_propia,posicion_fila_ficha,posicion_columna_ficha):
    if ficha_propia == "blanca":
        propias = estado.ficha_blanca()
        contrarias = estado.ficha_negra()
    else:
        propias = estado.ficha_negra()
        contrarias = estado.ficha_blanca()

    # Simular la ficha nueva
    propias = propias + [[posicion_fila_ficha, posicion_columna_ficha]]

    direcciones = [(-1,0),(1,0),(0,1),(0,-1),(1,-1),(-1,1),(1,1),(-1,-1)]
    fichas_cambiar_global = []

    for dx, dy in direcciones:
        fila, columna = posicion_fila_ficha + dx, posicion_columna_ficha + dy
        fichas_cambiar  = []
        # Recolectar contrarias
        while 0 <= fila < 8 and 0 <= columna < 8 and [fila, columna] in contrarias:
            fichas_cambiar .append([fila, columna])
            fila += dx
            columna += dy
        # Confirmar el cierre con una propia simulada
        if [fila, columna] in propias and fichas_cambiar :
            fichas_cambiar_global.extend(fichas_cambiar )

    return fichas_cambiar_global

