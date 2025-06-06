#Tablero
#Se encarga de mostrar el tablero y las fichas
def mostrar_tablero(tablero):
    print("\n   0   1   2   3   4   5   6   7")
    print("  +---+---+---+---+---+---+---+---+")
    blancas_coords = []
    negras_coords = []

    for fila in range(8):
        print(f"{fila} |", end="")
        for columna in range(8):
            if tablero[fila][columna] == 0:
                print("   |", end="")
            elif tablero[fila][columna] == 1:
                print(" ● |", end="")  # Negra
                negras_coords.append((fila, columna))
            else:
                print(" ○ |", end="")  # Blanca
                blancas_coords.append((fila, columna))
        print("\n  +---+---+---+---+---+---+---+---+")

#Se encarga de actualizar la posición de las piezas en el tablero a medida que avanza el juego
def modificar_tablero(tablero):
    turno = 1  # Empieza el jugador negro
    contador_salta_turno = 0
    juego_sigue = True
    
    while juego_sigue:
        mostrar_tablero(tablero)
        #sirve para contar, que si los dos jugadores salta, entonces se acaba la partida; cada vez que se empieza a jugar empieza en 0
        
        
        if turno == 1:
            print("\nTurno del jugador NEGRO (●)")
        else:
            print("\nTurno del jugador BLANCO (○)")
            
        print("Opciones:")
        print("1. Mover ficha")
        print("2. Terminar el juego")
        
        opcion = input("Seleccione una opción (1-2): ")
        
        if opcion == "2":
            break
            
        try:

            if(contador_salta_turno<2):
                print("aqui no entra")
                if (posibles_movimientos(turno)):
                    print("entra aqui")
                    #Selección de casilla a la que se mueve la ficha
                    new_fila = int(input("Ingrese la fila a donde va a mover la ficha (0-7): "))
                    new_columna = int(input("Ingrese la columna a donde va a mover la ficha (0-7): "))
                else:
                    print("No hay movimientos posibles, le toca al otro jugador")
                    contador_salta_turno +=1
                    if turno == 1:
                        turno = 2
                    else: 
                        turno = 1
            else:
                print("Juego terminado")
                juego_sigue = False
                break
            
            
            
            #Mira que las coordenadas a donde se mueve estén dentro del tablero
            if not (0 <= new_fila <= 7 and 0 <= new_columna <= 7):
                print("Posición inválida. Las coordenadas deben estar entre 0 y 7.")
                continue
            

            #comprueba que si las reglas se cumplen, entonces se produzca el cambio en el tablero
            if turno == 1: #turno de las negras
                print("nueva fila",new_fila)
                print("nueva c",new_fila)
                if not (tablero[new_fila][new_columna] == 0):
                    print("Posición inválida. En esa posición ya se encuentra una ficha.")
                    continue
                if(reglas_de_movimiento(turno,new_fila,new_columna)):
                    tablero[new_fila][new_columna] = 1  # Ficha negra
                    ficha_negra([new_fila,new_columna])
                    cambio_de_color_fichas(turno,new_fila,new_columna,tablero)
                    turno = 2
                else:
                    print("No cumple con las reglas.")
                    
            elif turno == 2: #turno de las blancas
                if not (tablero[new_fila][new_columna] == 0):
                    print("Posición inválida. En esa posición ya se encuentra una ficha.")
                    continue
                if (reglas_de_movimiento(turno,new_fila,new_columna)):
                    tablero[new_fila][new_columna] = 2  # Ficha blanca
                    ficha_blanca([new_fila,new_columna])
                    cambio_de_color_fichas(turno,new_fila,new_columna,tablero)
                    turno = 1
                else:
                    print("No cumple con las reglas.")
            else:
                print("Opción no válida. Intente de nuevo.")
            
            

        except ValueError:
            print("Por favor ingrese números válidos.")

#Ficha negra
#Lista de fichas blancas que están en el tablero, cada vez que hay una nueva ficha blanca se añade a esta lista
lista=  [[4, 4], [3, 3]]
def ficha_negra (extra = None):
    if extra:
        lista.append(extra)
    return lista


#Ficha blanca
#Lista de fichas blancas que están en el tablero, cada vez que hay una nueva ficha blanca se añade a esta lista
lista_blanca = [[3, 4], [4, 3]]
def ficha_blanca (extra = None):
    if extra:
        lista_blanca.append(extra)
    return lista_blanca

##Reglas

#Inicio del tablero

#inicializa tablero:
# 0 = casilla vacía, 1 = ficha negra, 2 = ficha blanca
# estado inicial del tablero
def tablero(blanca, negra) : 
    Tablero = []
    for fila in range (0,8):
        Fila = []
        for columna in range (0,8):
            Fila.append(0)
        Tablero.append(Fila)

    for i in blanca:
        Tablero [i[0]][i[1]] = 2

    for i in negra:
        Tablero [i[0]][i[1]] = 1

    return Tablero
    
#Turnos de juego
#reglas de movimiento del juego, recibe la posicion de la ficha que quiere mover y la posición del tablero al que quiere mover la ficha
#los parametros son turno, para saber si es turno de una blanca o negra
def reglas_de_movimiento(turno, posicion_fila_nueva, posicion_columna_nueva) : 
    if(turno == 1):
        ficha = "negra"
        cumple_con_las_reglas = comprobar_coordenadas_alrededor(ficha,posicion_fila_nueva,posicion_columna_nueva)
    else:
        ficha = "blanca"
        cumple_con_las_reglas = comprobar_coordenadas_alrededor(ficha,posicion_fila_nueva,posicion_columna_nueva)
    return cumple_con_las_reglas


#para comprobar q hay blancas 
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

def comprobar(fichas_propias,fila_ficha_contraria,columna_ficha_contraria,posicion_fila_nueva,posicion_columna_nueva):
    cumple = False

    cumple = comprobar_horizontal(fichas_propias,fila_ficha_contraria,columna_ficha_contraria,posicion_fila_nueva,posicion_columna_nueva)
    if (not cumple):
        cumple = comprobar_vertical(fichas_propias,fila_ficha_contraria,columna_ficha_contraria,posicion_fila_nueva,posicion_columna_nueva)
        if(not cumple):
            cumple = comprobar_diagonal(fichas_propias,fila_ficha_contraria,columna_ficha_contraria,posicion_fila_nueva,posicion_columna_nueva)

    return cumple

def comprobar_horizontal(fichas_propias,fila_ficha_contraria,columna_ficha_contraria,posicion_fila_nueva,posicion_columna_nueva):
    cumple = False
    print("entra primero")
    if ((columna_ficha_contraria == posicion_columna_nueva + 1) and (fila_ficha_contraria == posicion_fila_nueva)):
        print("fichas",fichas_propias)
        for c_pos in range(2,8-posicion_columna_nueva): #pongo 8-la posicion, pq quiero llegar desde esa columna a la última columna
            #veo si en las siguientes columnas a la derecha, hay alguna del color de mi turno
            for [fila,columna] in fichas_propias:
                if(fila == posicion_fila_nueva):
                    if(columna == posicion_columna_nueva+c_pos):
                        cumple = True
                if cumple:
                    break
            if cumple:
                break
                
    #si sigue siendo falso, comprueba si la blanca se encuentra a la izquierda de la negra y que se encuentre en la misma fila
    if (not cumple and (columna_ficha_contraria == posicion_columna_nueva-1) and (fila_ficha_contraria == posicion_fila_nueva)):
        for c_neg in range(2,posicion_columna_nueva+1): 
            #veo si en las siguientes columnas a la izquierda, hay alguna negra

            for [fila,columna] in fichas_propias:
                if(fila == posicion_fila_nueva):
                    if(columna == posicion_columna_nueva-c_neg):
                        cumple = True
                if cumple:
                    break
            if cumple:
                break

    return cumple

def comprobar_vertical(fichas_propias,fila_ficha_contraria,columna_ficha_contraria,posicion_fila_nueva,posicion_columna_nueva):
    cumple = False
    #si ponemos la nueva ficha abajo de una blanca
    if ((fila_ficha_contraria == posicion_fila_nueva+1) and (columna_ficha_contraria == posicion_columna_nueva)):
        for f_pos in range(2,8-posicion_fila_nueva):       
            #comparo que antes de terminar el tablero hay en la misma columna, en otra fila en el otro lado de la ficha blanca una ficha negra
            #es decir, por debajo de la blanca
            for [fila,columna] in fichas_propias:
                if(columna == posicion_columna_nueva):
                    if(fila ==  posicion_fila_nueva+f_pos):
                        cumple = True
                if cumple:
                    break
            if cumple:
                break
                
    #si no se cumple la condición anterior, veo si hay una por encima (en la fila de antes de la nueva)
    if(not cumple and (fila_ficha_contraria == posicion_fila_nueva-1) and (columna_ficha_contraria == posicion_columna_nueva)):
        print("entra segunda")
        for f_neg in range(2,posicion_fila_nueva+1):
            #comparo que antes de terminar el tablero hay en la misma columna, en otra fila en el otro lado de la ficha blanca una ficha negra
            #es decir, por arriba de la blanca
            for [fila,columna] in fichas_propias:
                if(columna == posicion_columna_nueva):
                    if(fila ==  posicion_fila_nueva-f_neg):
                        cumple = True
                if cumple:
                    break
            if cumple:
                break
    return cumple

def comprobar_diagonal(fichas_propias,fila_ficha_contraria,columna_ficha_contraria,posicion_fila_nueva,posicion_columna_nueva):
    cumple = False

    for f_neg in range(2,posicion_fila_nueva):
        #comprueba si es diagonal derecha arriba
        if (columna_ficha_contraria == posicion_columna_nueva+1 and fila_ficha_contraria == posicion_fila_nueva -1):
            for c_pos in range(2,8-posicion_columna_nueva): 
                #compruebo q hay una negra en el otro lado de la diagonal de la ficha blanca
                for [fila,columna] in fichas_propias:
                    if((columna == posicion_columna_nueva+c_pos) and (fila == posicion_fila_nueva-f_neg)):
                        cumple = True
                    if cumple:
                        break
                if cumple:
                    break

        #comprueba si es diagonal izquierda abajo
        if (not cumple and (columna_ficha_contraria == posicion_columna_nueva-1 and fila_ficha_contraria == posicion_fila_nueva -1)):
            for c_neg in range(2,posicion_columna_nueva+1): 
                #compruebo q hay una negra en el otro lado de la diagonal de la ficha blanca
                for [fila,columna] in fichas_propias:
                    if((columna == posicion_columna_nueva-c_neg) and (fila == posicion_fila_nueva-f_neg)):
                        cumple = True
                    if cumple:
                        break
                if cumple:
                    break
    
            
    for f_pos in range(2,8-posicion_fila_nueva):

        #comprueba si es diagonal izquierda arriba
        if (not cumple and (columna_ficha_contraria == posicion_columna_nueva-1 and fila_ficha_contraria == posicion_fila_nueva +1)):
            for c_neg in range(2,posicion_columna_nueva+1):
                #compruebo q hay una negra en el otro lado de la diagonal de la ficha blanca
                for [fila,columna] in fichas_propias:
                    if((columna == posicion_columna_nueva-c_neg) and (fila == posicion_fila_nueva+f_pos)):
                        cumple = True
                    if cumple:
                        break
                if cumple:
                    break

        #comprueba si es diagonal derecha abajo
        if (not cumple and (columna_ficha_contraria == posicion_columna_nueva+1 and fila_ficha_contraria == posicion_fila_nueva +1)):
            for c_pos in range(2,8-posicion_columna_nueva): 
                #compruebo q hay una negra en el otro lado de la diagonal de la ficha blanca
                for [fila,columna] in fichas_propias:
                    if((columna == posicion_columna_nueva+c_pos) and (fila == posicion_fila_nueva+f_pos)):
                        cumple = True
                    if cumple:
                        break
                if cumple:
                    break
            
    return cumple


##cambio de color

def cambio_de_color_fichas(turno,posicion_fila_ficha,posicion_columna_ficha,tablero):
    if(turno == 2):
        ficha_propia ="blanca"
        negras = obtener_fichas_cambiar(ficha_propia,posicion_fila_ficha,posicion_columna_ficha)
        for n in negras:
            ficha_blanca().append(n)
            ficha_negra().remove(n)
            tablero[n[0]][n[1]] = 2

    else:
        ficha_propia ="negra"
        blancas = obtener_fichas_cambiar(ficha_propia,posicion_fila_ficha,posicion_columna_ficha)
        for n in blancas:
            ficha_blanca().remove(n)
            ficha_negra().append(n)
            tablero[n[0]][n[1]] = 1

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

##Turno

#devuelve true si puede jugar
def posibles_movimientos(turno):
    puede_jugar = False
    if (turno == 1):
        ficha_actual = "negra"
    else:
        ficha_actual = "blanca"
    fichas_blancas = ficha_blanca()
    fichas_negras = ficha_negra()
    if (len(fichas_blancas) + len(fichas_negras)<64):
        for fila_tabl in range(8):
            for columna_tabl in range(8):
                if (([fila_tabl, columna_tabl] not in ficha_blanca()) and ([fila_tabl, columna_tabl] not in ficha_negra())):
                    if ficha_actual == "blanca":
                        if(len(fichas_negras)>0):
                            for[fila_n, columna_n] in fichas_negras:
                                puede_jugar = comprobar(fichas_blancas,fila_n,columna_n,fila_tabl,columna_tabl)
                                if puede_jugar:
                                    break
                    else:
                        if(len(fichas_blancas)>0):
                            for[fila_b,columna_b] in fichas_blancas:
                                if comprobar(fichas_negras,fila_b,columna_b,fila_tabl,columna_tabl):
                                    puede_jugar = True
                                    break
                            if puede_jugar:
                                break
                   
                if puede_jugar:
                        break
            if puede_jugar:
                        break
                
    return puede_jugar

def main():
    print("Bienvenido al editor de tablero de Otelo")
    
    # Inicializar tablero vacío
    
    # Permitir al usuario modificar el tablero
    modificar_tablero(tablero(ficha_blanca (), ficha_negra ()))

if __name__ == "__main__":
    main()
    