#Turnos de juego
#reglas de movimiento del juego, recibe la posicion de la ficha que quiere mover y 
# la posición del tablero al que quiere mover la ficha
#los parametros son turno, para saber si es turno de una blanca o negra

def reglas_de_movimiento(estado,turno, posicion_fila_nueva, posicion_columna_nueva) : 
    """
    Determina si la casilla (posicion_fila_nueva, posicion_columna_nueva) es una jugada válida según las normas de Othello/Reversi 
        para el jugador en turno.

    Flujo:
      1. Identifica el color de la ficha según el turno.
      2. Llama a `comprobar_coordenadas_alrededor`, que explora las ocho
         direcciones para verificar que al menos una captura sea posible.
      3. Devuelve el resultado de esa comprobación.

    Parámetros:
        estado (EstadoJuego): Estado actual del tablero y las listas de fichas.
        turno (int): Identificador del jugador actual (1 = negras, otro = blancas).
        posicion_fila_nueva (int): Fila donde se intentará colocar la nueva ficha.
        posicion_columna_nueva (int): Columna donde se intentará colocar la nueva ficha.

    Retorna:
        bool: True si al colocar la ficha en esa posición se captura al menos una ficha contraria; False en caso contrario.
    """
    if(turno == 1):
        ficha = "negra"
        cumple_con_las_reglas = comprobar_coordenadas_alrededor(estado,ficha,posicion_fila_nueva,posicion_columna_nueva)
    else:
        ficha = "blanca"
        cumple_con_las_reglas = comprobar_coordenadas_alrededor(estado,ficha,posicion_fila_nueva,posicion_columna_nueva)
    return cumple_con_las_reglas


#para comprobar q hay coordenadas al rededor de la ficha válidas
def comprobar_coordenadas_alrededor(estado,ficha,posicion_fila_nueva,posicion_columna_nueva):
    cumple = False
    if ficha == "negra":
        fichas_contrarias = estado.ficha_blanca()
        fichas_propias = estado.ficha_negra()
    else:
        fichas_contrarias = estado.ficha_negra()
        fichas_propias = estado.ficha_blanca()
        
    for [fila,columna] in fichas_contrarias :
        cumple = comprobar(fichas_propias,fichas_contrarias,fila,columna,posicion_fila_nueva,posicion_columna_nueva)
        if cumple:
            break
    return cumple


def comprobar(fichas_propias,fichas_contrarias,fila_ficha_contraria,columna_ficha_contraria,posicion_fila_nueva,posicion_columna_nueva):
    """
    Verifica si al colocar una ficha en (posicion_fila_nueva, posicion_columna_nueva) se captura al menos una ficha 
    contraria en alguna de las tres orientaciones: horizontal, vertical o diagonal.

    Para cada orientación (horizontal, vertical y diagonal), comprueba:
      1. Que haya al menos una ficha contraria contigua a la nueva posición.
      2. Que tras esa(s) ficha(s) contraria(s) aparezca una ficha propia sin huecos intermedios.
      3. Si se cumple, devuelve True.

    Parámetros:
        fichas_propias (list[list[int]]): Lista de coordenadas [fila, columna] de las fichas del jugador actual.
        fichas_contrarias (list[list[int]]): Lista de coordenadas [fila, columna] de las fichas del oponente.
        fila_ficha_contraria (int): Fila de una ficha contraria.
        columna_ficha_contraria (int): Columna de esa ficha contraria.
        posicion_fila_nueva (int): Fila donde se quiere colocar la nueva ficha.
        posicion_columna_nueva (int): Columna donde se quiere colocar la nueva ficha.

    Devuelve:
        bool: True si en alguna de las tres orientaciones (horizontal, vertical o diagonal) se produce una captura válida, False en caso contrario.
    """
    cumple = False

    cumple = comprobar_horizontal(fichas_propias,fichas_contrarias,fila_ficha_contraria,columna_ficha_contraria,posicion_fila_nueva,posicion_columna_nueva)
    if (not cumple):
        cumple = comprobar_vertical(fichas_propias,fichas_contrarias,fila_ficha_contraria,columna_ficha_contraria,posicion_fila_nueva,posicion_columna_nueva)
        if(not cumple):
            cumple = comprobar_diagonal(fichas_propias,fichas_contrarias,fila_ficha_contraria,columna_ficha_contraria,posicion_fila_nueva,posicion_columna_nueva)

    return cumple


def comprobar_horizontal(fichas_propias,fichas_contrarias,fila_ficha_contraria,columna_ficha_contraria,posicion_fila_nueva,posicion_columna_nueva):
    """
    Verifica si colocando una ficha en (posicion_fila_nueva, posicion_columna_nueva) se capturan fichas enemigas en la misma fila, 
        bien hacia la derecha o hacia la izquierda.

    Algoritmo:
      1. Comprueba que la ficha contraria esté justo adyacente a la nueva posición.
      2. Recorre en la misma dirección (derecha o izquierda) hasta:
         a. Encontrar una ficha propia → devuelve True.
         b. Encontrar un hueco o llegar al borde → termina y devuelve False.

    Parámetros:
        fichas_propias (List[List[int]]): Coordenadas de fichas del jugador.
        fichas_contrarias (List[List[int]]): Coordenadas de fichas del oponente.
        fila_ficha_contraria (int): Fila de una ficha contraria.
        columna_ficha_contraria (int): Columna de esa ficha contraria.
        posicion_fila_nueva (int): Fila donde se quiere colocar la nueva ficha.
        posicion_columna_nueva (int): Columna donde se quiere colocar la nueva ficha.

    Retorna:
        bool: True si al menos en una dirección horizontal se produce una captura, False en caso contrario.
    """
    cumple = False
    if(fila_ficha_contraria == posicion_fila_nueva):

        if (columna_ficha_contraria == posicion_columna_nueva + 1) :
            for c_pos in range(posicion_columna_nueva+2,8): 
                if ([posicion_fila_nueva,c_pos] in fichas_contrarias):
                    continue
                elif ([posicion_fila_nueva,c_pos] in fichas_propias):
                    cumple = True
                    break
                else:
                    break
                 
        elif ((columna_ficha_contraria == posicion_columna_nueva-1)):
            for c_neg in range(posicion_columna_nueva - 2, -1, -1): 
                if ([posicion_fila_nueva,c_neg] in fichas_contrarias):
                    continue
                elif ([posicion_fila_nueva,c_neg] in fichas_propias):
                    cumple = True
                    break
                else:
                    break
    return cumple

#VERTICAL
def comprobar_vertical(fichas_propias,fichas_contrarias,fila_ficha_contraria,columna_ficha_contraria,posicion_fila_nueva,posicion_columna_nueva):
    """
    Verifica si colocando una ficha en (posicion_fila_nueva, posicion_columna_nueva) se capturan fichas enemigas en la misma columna, 
        bien hacia arriba o hacia abajo.

    Algoritmo:
      1. Comprueba que la ficha contraria esté justo adyacente a la nueva posición.
      2. Recorre en la misma dirección (arriba o abajo) hasta:
         a. Encontrar una ficha propia → devuelve True.
         b. Encontrar un hueco o llegar al borde → termina y devuelve False.

    Parámetros:
        fichas_propias (List[List[int]]): Coordenadas de fichas del jugador.
        fichas_contrarias (List[List[int]]): Coordenadas de fichas del oponente.
        fila_ficha_contraria (int): Fila de una ficha contraria.
        columna_ficha_contraria (int): Columna de esa ficha contraria.
        posicion_fila_nueva (int): Fila donde se quiere colocar la nueva ficha.
        posicion_columna_nueva (int): Columna donde se quiere colocar la nueva ficha.

    Retorna:
        bool: True si al menos en una dirección vertival se produce una captura, False en caso contrario.
    """
    cumple = False
    if(columna_ficha_contraria == posicion_columna_nueva):

        if ((fila_ficha_contraria == posicion_fila_nueva+1)):
            for f_pos in range(posicion_fila_nueva+2,8): 
                if ([f_pos,posicion_columna_nueva] in fichas_contrarias):
                    continue
                elif ([f_pos,posicion_columna_nueva] in fichas_propias):
                    cumple = True
                    break
                else:
                    break
     
        elif((fila_ficha_contraria == posicion_fila_nueva-1)):
            for f_neg in range(posicion_fila_nueva -2, -1, -1): 
                if ([f_neg,posicion_columna_nueva] in fichas_contrarias):
                    continue
                elif ([f_neg,posicion_columna_nueva] in fichas_propias):
                    cumple = True
                    break
                else:
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


def posibles_movimientos(estado, turno):
    """
    Calcula las posiciones válidas donde el jugador actual puede colocar una ficha.

    Recorre todas las casillas del tablero y selecciona aquellas que:
      1. Están vacías.
      2. Aún existen fichas del oponente en el tablero.
      3. Al colocarse allí, capturan al menos una ficha enemiga según las reglas de Othello/Reversi,
         lo cual se verifica llamando a la función `comprobar`.

    Parámetros:
        estado (EstadoJuego): Objeto que contiene el tablero y las posiciones de fichas.
        turno (int): Identificador del jugador actual (1 = negras, otro = blancas).

    Devuelve:
        List[List[int, int]]: Lista de coordenadas [fila, columna] donde el movimiento es válido.
    """
    posibles_acciones = []
    if (turno == 1):
        ficha_actual = "negra"
    else:
        ficha_actual = "blanca"

    fichas_blancas = estado.ficha_blanca()
    fichas_negras = estado.ficha_negra()
    tablero = estado.tablero
    if (len(fichas_blancas) + len(fichas_negras)<64):
        for fila_tabl in range(8):
            for columna_tabl in range(8):
                if (tablero[fila_tabl][columna_tabl] == 0):
                    if ficha_actual == "blanca":
                        if(len(fichas_negras)>0):
                            for[fila_n, columna_n] in fichas_negras:
                                puede_jugar = comprobar(fichas_blancas,fichas_negras,fila_n,columna_n,fila_tabl,columna_tabl)
                                if puede_jugar:  
                                    if not [fila_tabl,columna_tabl] in posibles_acciones:
                                        posibles_acciones.append([fila_tabl,columna_tabl])
                    else:
                        if(len(fichas_blancas)>0):
                            for[fila_b,columna_b] in fichas_blancas:
                                puede_jugar = comprobar(fichas_negras,fichas_blancas,fila_b,columna_b,fila_tabl,columna_tabl)
                                if puede_jugar:
                                    if not [fila_tabl,columna_tabl] in posibles_acciones:
                                        posibles_acciones.append([fila_tabl,columna_tabl])           
    return posibles_acciones
