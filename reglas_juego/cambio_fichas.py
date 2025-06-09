##cambio de color


def cambio_de_color_fichas(estado, turno, fila, columna):
    # 1) Damos por válido el movimiento y colocamos la ficha
    if turno == 2:
        valor = 1
        estado.fichas_blancas.append([fila, columna])
    else:
        valor = 2
        estado.fichas_negras.append([fila, columna])

    estado.tablero[fila][columna] = valor

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
    if(ficha_propia == "blanca"):
        fichas_propias = estado.ficha_blanca()
        fichas_oponente = estado.ficha_negra()
    else:
        fichas_propias = estado.ficha_negra()
        fichas_oponente = estado.ficha_blanca()

    direcciones = [(-1,0),(1,0),(0,1),(0,-1),(1,-1),(-1,1),(1,1),(-1,-1)]
    fichas_cambiar_global = []
   
    for dx,dy in direcciones:
        fila, columna = posicion_fila_ficha + dx, posicion_columna_ficha + dy
        fichas_cambiar = []
        while 0<=fila<8 and 0<=columna<8:
            if [fila,columna] in fichas_oponente:
                
                fichas_cambiar.append([fila,columna])
            elif [fila,columna] in fichas_propias:
                #se para de coger fichas blancas
                if fichas_cambiar:
                    #hago extend, para no tener una lista dentro de otra lista
                    fichas_cambiar_global.extend(fichas_cambiar)
                    break
            else:
                break
            # Avanzamos una casilla más en la dirección actual
            fila += dx
            columna += dy 
    return fichas_cambiar_global
