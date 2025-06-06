#Turnos de juego
#reglas de movimiento del juego, recibe la posicion de la ficha que quiere mover y 
# la posición del tablero al que quiere mover la ficha
#los parametros son turno, para saber si es turno de una blanca o negra


from reglas_juego.inicializa_tablero import ficha_blanca, ficha_negra


def reglas_de_movimiento(turno, posicion_fila_nueva, posicion_columna_nueva) : 
    if(turno == 1):
        ficha = "negra"
        cumple_con_las_reglas = comprobar_coordenadas_alrededor(ficha,posicion_fila_nueva,posicion_columna_nueva)
    else:
        ficha = "blanca"
        cumple_con_las_reglas = comprobar_coordenadas_alrededor(ficha,posicion_fila_nueva,posicion_columna_nueva)
    return cumple_con_las_reglas


#para comprobar q hay coordenadas al rededor de la ficha válidas
def comprobar_coordenadas_alrededor(ficha,posicion_fila_nueva,posicion_columna_nueva):
    cumple = False
    fichas = []
    if ficha == "negra":
        fichas = ficha_blanca()
        fichas_propias = ficha_negra()
    else:
        fichas = ficha_negra()
        fichas_propias = ficha_blanca()
        
    for [fila,columna] in fichas :
        cumple = comprobar(fichas_propias,fila,columna,posicion_fila_nueva,posicion_columna_nueva)
        if cumple:
            break
    return cumple

# Comprueba la horizontal, la vertical y la diagonal para realizar el movimiento
def comprobar(fichas_propias,fila_ficha_contraria,columna_ficha_contraria,posicion_fila_nueva,posicion_columna_nueva):
    cumple = False

    cumple = comprobar_horizontal(fichas_propias,fila_ficha_contraria,columna_ficha_contraria,posicion_fila_nueva,posicion_columna_nueva)
    if (not cumple):
        cumple = comprobar_vertical(fichas_propias,fila_ficha_contraria,columna_ficha_contraria,posicion_fila_nueva,posicion_columna_nueva)
        if(not cumple):
            cumple = comprobar_diagonal(fichas_propias,fila_ficha_contraria,columna_ficha_contraria,posicion_fila_nueva,posicion_columna_nueva)

    return cumple

#HORIZONTAL
def comprobar_horizontal(fichas_propias,fila_ficha_contraria,columna_ficha_contraria,posicion_fila_nueva,posicion_columna_nueva):
    cumple = False
    if(fila_ficha_contraria == posicion_fila_nueva):
        #derecha
        if ((columna_ficha_contraria == posicion_columna_nueva + 1)):
            for c_pos in range(2,8-posicion_columna_nueva): 
                for [fila,columna] in fichas_propias:
                    if((fila == posicion_fila_nueva) and (columna == posicion_columna_nueva+c_pos)):
                        cumple = True
                        break
                if cumple:
                    break
        #izquierda            
        elif ((columna_ficha_contraria == posicion_columna_nueva-1)):
            for c_neg in range(2,posicion_columna_nueva+1): 
                for [fila,columna] in fichas_propias:
                    if((fila == posicion_fila_nueva) and (columna == posicion_columna_nueva-c_neg)):
                        cumple = True
                        break
                if cumple:
                    break
    
    return cumple

#VERTICAL
def comprobar_vertical(fichas_propias,fila_ficha_contraria,columna_ficha_contraria,posicion_fila_nueva,posicion_columna_nueva):
    cumple = False
    if(columna_ficha_contraria == posicion_columna_nueva):
        #abajo
        if ((fila_ficha_contraria == posicion_fila_nueva+1)):
            for f_pos in range(2,8-posicion_fila_nueva):       
                for [fila,columna] in fichas_propias:
                    if((columna == posicion_columna_nueva) and (fila ==  posicion_fila_nueva+f_pos)):
                        cumple = True
                        break
                if cumple:
                    break
        #arriba       
        elif((fila_ficha_contraria == posicion_fila_nueva-1)):
            for f_neg in range(2,posicion_fila_nueva+1):
                for [fila,columna] in fichas_propias:
                    if((columna == posicion_columna_nueva) and (fila ==  posicion_fila_nueva-f_neg)):
                        cumple = True
                        break
                if cumple:
                    break
    return cumple

#DIAGONAL
def comprobar_diagonal(fichas_propias,fila_ficha_contraria,columna_ficha_contraria,posicion_fila_nueva,posicion_columna_nueva):
    cumple = False

    for f_neg in range(2,posicion_fila_nueva):
        #diagonal derecha arriba        
        if (columna_ficha_contraria == posicion_columna_nueva+1 and fila_ficha_contraria == posicion_fila_nueva -1):
            for c_pos in range(2,8-posicion_columna_nueva): 
                for [fila,columna] in fichas_propias:
                    if((columna == posicion_columna_nueva+c_pos) and (fila == posicion_fila_nueva-f_neg)):
                        cumple = True
                        break
                if cumple:
                    break

        #diagonal izquierda arriba        
        if (not cumple and (columna_ficha_contraria == posicion_columna_nueva-1 and fila_ficha_contraria == posicion_fila_nueva -1)):
            for c_neg in range(2,posicion_columna_nueva+1): 
                for [fila,columna] in fichas_propias:
                    if((columna == posicion_columna_nueva-c_neg) and (fila == posicion_fila_nueva-f_neg)):
                        cumple = True
                        break
                if cumple:
                    break
    
    for f_pos in range(2,8-posicion_fila_nueva):

         #diagonal izquierda abajo
        if (not cumple and (columna_ficha_contraria == posicion_columna_nueva-1 and fila_ficha_contraria == posicion_fila_nueva +1)):
            for c_neg in range(2,posicion_columna_nueva+1):
                for [fila,columna] in fichas_propias:
                    if((columna == posicion_columna_nueva-c_neg) and (fila == posicion_fila_nueva+f_pos)):
                        cumple = True
                        break
                if cumple:
                    break

         #diagonal derecha abajo
        if (not cumple and (columna_ficha_contraria == posicion_columna_nueva+1 and fila_ficha_contraria == posicion_fila_nueva +1)):
            for c_pos in range(2,8-posicion_columna_nueva): 
                for [fila,columna] in fichas_propias:
                    if((columna == posicion_columna_nueva+c_pos) and (fila == posicion_fila_nueva+f_pos)):
                        cumple = True
                        break
                if cumple:
                    break
            
    return cumple

#devuelve true si puede jugar
def posibles_movimientos(tablero, turno):
    posibles_acciones = []
    if (turno == 1):
        ficha_actual = "negra"
    else:
        ficha_actual = "blanca"

    fichas_blancas = ficha_blanca()
    fichas_negras = ficha_negra()

    if (len(fichas_blancas) + len(fichas_negras)<64):
        for fila_tabl in range(8):
            for columna_tabl in range(8):
                if (tablero[fila_tabl][columna_tabl] == 0):
                    if ficha_actual == "blanca":
                        if(len(fichas_negras)>0):
                            for[fila_n, columna_n] in fichas_negras:
                                puede_jugar = comprobar(fichas_blancas,fila_n,columna_n,fila_tabl,columna_tabl)
                                if puede_jugar:
                                    posibles_acciones.append([fila_tabl,columna_tabl])
                    else:
                        if(len(fichas_blancas)>0):
                            for[fila_b,columna_b] in fichas_blancas:
                                puede_jugar = comprobar(fichas_negras,fila_b,columna_b,fila_tabl,columna_tabl)
                                if puede_jugar:
                                    posibles_acciones.append([fila_tabl,columna_tabl])            
    return posibles_acciones