##cambio de color
from reglas_juego.inicializa_tablero import ficha_blanca, ficha_negra


def cambio_de_color_fichas(turno,posicion_fila_ficha,posicion_columna_ficha,tablero):
    if(turno == 2):
        ficha_propia ="blanca"
        negras = obtener_fichas_cambiar(ficha_propia,posicion_fila_ficha,posicion_columna_ficha)
        for n in negras:
            ficha_blanca().append(n)
            ficha_negra().remove(n)
            tablero[n[0]][n[1]] = 1

    else:
        ficha_propia ="negra"
        blancas = obtener_fichas_cambiar(ficha_propia,posicion_fila_ficha,posicion_columna_ficha)
        for n in blancas:
            ficha_blanca().remove(n)
            ficha_negra().append(n)
            tablero[n[0]][n[1]] = 2

#se le manda la ficha a cambiar, en la posicion que se quiere cambiar
def obtener_fichas_cambiar(ficha_propia,posicion_fila_ficha,posicion_columna_ficha):
    if(ficha_propia == "blanca"):
        fichas_propias = ficha_blanca()
        fichas_oponente = ficha_negra()
    else:
        fichas_propias = ficha_negra()
        fichas_oponente = ficha_blanca()

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
