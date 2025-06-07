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
    if ficha == "negra":
        fichas_contrarias = ficha_blanca()
        fichas_propias = ficha_negra()
    else:
        fichas_contrarias = ficha_negra()
        fichas_propias = ficha_blanca()
        
    for [fila,columna] in fichas_contrarias :
        cumple = comprobar(fichas_propias,fichas_contrarias,fila,columna,posicion_fila_nueva,posicion_columna_nueva)
        if cumple:
            break
    return cumple

# Comprueba la horizontal, la vertical y la diagonal para realizar el movimiento
def comprobar(fichas_propias,fichas_contrarias,fila_ficha_contraria,columna_ficha_contraria,posicion_fila_nueva,posicion_columna_nueva):
    cumple = False

    cumple = comprobar_horizontal(fichas_propias,fichas_contrarias,fila_ficha_contraria,columna_ficha_contraria,posicion_fila_nueva,posicion_columna_nueva)
    if (not cumple):
        cumple = comprobar_vertical(fichas_propias,fichas_contrarias,fila_ficha_contraria,columna_ficha_contraria,posicion_fila_nueva,posicion_columna_nueva)
        if(not cumple):
            cumple = comprobar_diagonal(fichas_propias,fichas_contrarias,fila_ficha_contraria,columna_ficha_contraria,posicion_fila_nueva,posicion_columna_nueva)

    return cumple

#HORIZONTAL
def comprobar_horizontal(fichas_propias,fichas_contrarias,fila_ficha_contraria,columna_ficha_contraria,posicion_fila_nueva,posicion_columna_nueva):
    cumple = False
    if(fila_ficha_contraria == posicion_fila_nueva):
        #derecha
        if (columna_ficha_contraria == posicion_columna_nueva + 1) :
            for c_pos in range(posicion_columna_nueva+2,8): #pongo 8-la posicion, pq quiero llegar desde esa columna a la última columna
                #veo si en las siguientes columnas a la derecha, hay alguna del color de mi turno
                if ([posicion_fila_nueva,c_pos] in fichas_contrarias):
                    continue
                elif ([posicion_fila_nueva,c_pos] in fichas_propias):
                    # Si encontramos una del mismo color, la secuencia es válida
                    cumple = True
                    break
                else:
                    # Si no hay ficha blanca ni del mismo color: hay un hueco o una del enemigo, no sirve
                    break
        #izquierda            
        elif ((columna_ficha_contraria == posicion_columna_nueva-1)):
            for c_neg in range(posicion_columna_nueva - 2, -1, -1): 
                #veo si en las siguientes columnas a la derecha, hay alguna del color de mi turno
                if ([posicion_fila_nueva,c_neg] in fichas_contrarias):
                    continue
                elif ([posicion_fila_nueva,c_neg] in fichas_propias):
                    # Si encontramos una del mismo color, la secuencia es válida
                    cumple = True
                    break
                else:
                    # Si no hay ficha blanca ni del mismo color: hay un hueco o una del enemigo, no sirve
                    break
    return cumple

#VERTICAL
def comprobar_vertical(fichas_propias,fichas_contrarias,fila_ficha_contraria,columna_ficha_contraria,posicion_fila_nueva,posicion_columna_nueva):
    cumple = False
    if(columna_ficha_contraria == posicion_columna_nueva):
        #abajo
        if ((fila_ficha_contraria == posicion_fila_nueva+1)):
            for f_pos in range(posicion_fila_nueva+2,8): #pongo 8-la posicion, pq quiero llegar desde esa columna a la última columna
                #veo si en las siguientes columnas a la derecha, hay alguna del color de mi turno
                if ([f_pos,posicion_columna_nueva] in fichas_contrarias):
                    continue
                elif ([f_pos,posicion_columna_nueva] in fichas_propias):
                    # Si encontramos una del mismo color, la secuencia es válida
                    cumple = True
                    break
                else:
                    # Si no hay ficha blanca ni del mismo color: hay un hueco o una del enemigo, no sirve
                    break
        #arriba       
        elif((fila_ficha_contraria == posicion_fila_nueva-1)):
            for f_neg in range(posicion_fila_nueva -2, -1, -1): 
                #veo si en las siguientes columnas a la derecha, hay alguna del color de mi turno
                if ([f_neg,posicion_columna_nueva] in fichas_contrarias):
                    continue
                elif ([f_neg,posicion_columna_nueva] in fichas_propias):
                    # Si encontramos una del mismo color, la secuencia es válida
                    cumple = True
                    break
                else:
                    # Si no hay ficha blanca ni del mismo color: hay un hueco o una del enemigo, no sirve
                    break
    return cumple

#DIAGONAL
def comprobar_diagonal(fichas_propias,fichas_contrarias,fila_ficha_contraria,columna_ficha_contraria,posicion_fila_nueva,posicion_columna_nueva):
    cumple = False
            #yo quiero ponerla a la izquierda abajo de una ficha contraria  
            # este si funciona    
    if (columna_ficha_contraria == posicion_columna_nueva +1 and fila_ficha_contraria == posicion_fila_nueva -1):
        return comprobar_diagonal_arriba_derecha(fichas_propias,fichas_contrarias,posicion_fila_nueva,posicion_columna_nueva)

    #este no
    #pongo la nueva ficha a la derecha abajo de una ficha contraria    
    elif (columna_ficha_contraria == posicion_columna_nueva-1 and fila_ficha_contraria == posicion_fila_nueva -1):
        return comprobar_diagonal_arriba_izquierda(fichas_propias,fichas_contrarias,posicion_fila_nueva,posicion_columna_nueva)
    
    #pongo la nueva ficha a la derecha arriba de una ficha contraria
    elif (columna_ficha_contraria == posicion_columna_nueva-1 and fila_ficha_contraria == posicion_fila_nueva +1):
        return comprobar_diagonal_abajo_izquierda(fichas_propias,fichas_contrarias,posicion_fila_nueva,posicion_columna_nueva)

    #este 
    #pongo la nueva ficha a la izquierda arriba de una ficha contraria
    elif (columna_ficha_contraria == posicion_columna_nueva+1 and fila_ficha_contraria == posicion_fila_nueva +1):
        return comprobar_diagonal_abajo_derecha(fichas_propias,fichas_contrarias,posicion_fila_nueva,posicion_columna_nueva)
    else:
        return cumple
            
    

#pongo la ficha abajo izquierda
#SI FUNCIONA
def comprobar_diagonal_arriba_derecha(fichas_propias,fichas_contrarias,posicion_fila_nueva,posicion_columna_nueva):
    cumple = False
    columna_a_comprobar = posicion_columna_nueva + 2
    fila_a_comprobar = posicion_fila_nueva -2
    while (0<=columna_a_comprobar<8 and 0<=fila_a_comprobar<8):
        if ([fila_a_comprobar,columna_a_comprobar] in fichas_contrarias):
            columna_a_comprobar +=1
            fila_a_comprobar -=1
            continue
        elif ([fila_a_comprobar,columna_a_comprobar] in fichas_propias):
            # Si encontramos una del mismo color, la secuencia es válida
            cumple = True
            break
        else:
            # Si no hay ficha blanca ni del mismo color: hay un hueco o una del enemigo, no sirve
            break
    return cumple

#pongo la ficha arriba derecha
#SI FUNCIONA
def comprobar_diagonal_abajo_izquierda(fichas_propias,fichas_contrarias,posicion_fila_nueva,posicion_columna_nueva):
    cumple = False
    columna_a_comprobar = posicion_columna_nueva - 2
    fila_a_comprobar = posicion_fila_nueva + 2
    while (0<=columna_a_comprobar<8 and 0<=fila_a_comprobar<8):
        if ([fila_a_comprobar,columna_a_comprobar] in fichas_contrarias):
            columna_a_comprobar -=1
            fila_a_comprobar +=1
            continue
        elif ([fila_a_comprobar,columna_a_comprobar] in fichas_propias):
            # Si encontramos una del mismo color, la secuencia es válida
            cumple = True
            break
        else:
            # Si no hay ficha blanca ni del mismo color: hay un hueco o una del enemigo, no sirve
            break
    return cumple

#pongo la ficha arriba izquierda
#SI FUNCIONAAAA
def comprobar_diagonal_abajo_derecha(fichas_propias,fichas_contrarias,posicion_fila_nueva,posicion_columna_nueva):
    cumple = False
    columna_a_comprobar = posicion_columna_nueva + 2
    fila_a_comprobar = posicion_fila_nueva + 2
    while (0<=columna_a_comprobar<8 and 0<=fila_a_comprobar<8):
        if ([fila_a_comprobar,columna_a_comprobar] in fichas_contrarias):
            columna_a_comprobar +=1
            fila_a_comprobar +=1
            continue
        elif ([fila_a_comprobar,columna_a_comprobar] in fichas_propias):
            # Si encontramos una del mismo color, la secuencia es válida
            cumple = True
            break
        else:
            # Si no hay ficha blanca ni del mismo color: hay un hueco o una del enemigo, no sirve
            break
            
    return cumple

#pongo la ficha, abajo derecha
#SI FUNCIONAAA
def comprobar_diagonal_arriba_izquierda(fichas_propias,fichas_contrarias,posicion_fila_nueva,posicion_columna_nueva):
    cumple = False
    columna_a_comprobar = posicion_columna_nueva - 2
    fila_a_comprobar = posicion_fila_nueva - 2
    while (0<=columna_a_comprobar<8 and 0<=fila_a_comprobar<8):
        if ([fila_a_comprobar,columna_a_comprobar] in fichas_contrarias):
            columna_a_comprobar -=1
            fila_a_comprobar -=1
            continue
        elif ([fila_a_comprobar,columna_a_comprobar] in fichas_propias):
            # Si encontramos una del mismo color, la secuencia es válida
            cumple = True
            break
        else:
            # Si no hay ficha blanca ni del mismo color: hay un hueco o una del enemigo, no sirve
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
                                puede_jugar = comprobar(fichas_blancas,fichas_negras,fila_n,columna_n,fila_tabl,columna_tabl)
                                if puede_jugar:
                                    posibles_acciones.append([fila_tabl,columna_tabl])
                    else:
                        if(len(fichas_blancas)>0):
                            for[fila_b,columna_b] in fichas_blancas:
                                puede_jugar = comprobar(fichas_negras,fichas_blancas,fila_b,columna_b,fila_tabl,columna_tabl)
                                if puede_jugar:
                                    posibles_acciones.append([fila_tabl,columna_tabl])            
    return posibles_acciones