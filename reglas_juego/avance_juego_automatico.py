#Se encarga de actualizar la posición de las piezas en el tablero a medida que avanza el juego
import random
from reglas_juego.excepciones import EntradaNoNumericaError, JugadorInvalidoError, MovimientoInvalidoError, validar_entrada_numerica
from reglas_juego.estado_juego import EstadoJuego
from reglas_juego.cambio_fichas import cambio_de_color_fichas
from reglas_juego.inicializa_tablero import mostrar_tablero
from reglas_juego.movimientos import posibles_movimientos, reglas_de_movimiento

def turnos(turno, new_fila, new_columna, estado):
            #comprueba que si las reglas se cumplen, entonces se produzca el cambio en el tablero
            if(reglas_de_movimiento(estado,turno,new_fila,new_columna)):
                cambio_de_color_fichas(estado,turno,new_fila,new_columna,estado.tablero)
                if turno == 1: #turno de las negras
                    estado.tablero[new_fila][new_columna] = 2  # Ficha negra
                    estado.ficha_negra([new_fila,new_columna])
                    turno = 2 #siguiente turno: blancas
                    
                elif turno == 2: #turno de las blancas
                    estado.tablero[new_fila][new_columna] = 1  # Ficha blanca
                    estado.ficha_blanca([new_fila,new_columna])
                    turno = 1 #siguiente turno: negras
                
                else:
                    raise JugadorInvalidoError()
            else: 
                 raise MovimientoInvalidoError()

            return turno, estado.tablero 


def ganador(estado, turno):
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

# PARTIDA IA VS IA

def partida_automática(turno, estado):
    contador_salta_turno = 0
    
    while contador_salta_turno<2:

                movimientos = posibles_movimientos(estado,turno)
                if (len(movimientos) != 0):
                    accion_seleccionada = random.choice(movimientos)
                    turno = turnos(turno, accion_seleccionada[0], accion_seleccionada[1], estado)[0]   
                    contador_salta_turno = 0
                    
                else:
                    contador_salta_turno +=1
                    if turno == 1:
                        turno = 2
                    else: 
                        turno = 1

    return ganador(estado,turno)



#PARTIDA HUMANO VS HUMANO

def partida_manual(estado):
    turno = 1  # Empieza el jugador negro
    contador_salta_turno = 0

    while (contador_salta_turno<2):
        mostrar_tablero(estado.tablero)        
        
        if turno == 1:
            print("\nTurno del jugador NEGRO (●)")
        else:
            print("\nTurno del jugador BLANCO (○)")
            
        movimientos = posibles_movimientos(estado, turno)
            
        if (len(movimientos) != 0):
                    #Selección de casilla a la que se mueve la ficha
                    new_fila = validar_entrada_numerica(input("Ingrese la fila a donde va a mover la ficha (0-7): "))
                    new_columna = validar_entrada_numerica(input("Ingrese la columna a donde va a mover la ficha (0-7): "))
                    
                    if not (0 <= new_fila <= 7 and 0 <= new_columna <= 7):
                        print("Posición inválida. Las coordenadas deben estar entre 0 y 7.")
                        continue
                    if not (estado.tablero[new_fila][new_columna] == 0):
                        print("Posición inválida. En esa posición ya se encuentra una ficha.")
                        continue
                    
                    try:
                        turno, _ = turnos(turno, new_fila, new_columna, estado)
                        contador_salta_turno = 0
                    except EntradaNoNumericaError as e:
                        print(e)
                    except MovimientoInvalidoError:
                        print("Movimiento inválido. Intente de nuevo.")
                    except JugadorInvalidoError:
                        print("Error: turno inválido.")
        else:
                    print("No hay movimientos posibles, le toca al otro jugador")
                    contador_salta_turno +=1
                    if turno == 1:
                        turno = 2
                    else: 
                        turno = 1

    print("Juego terminado")
    if (ganador(turno) == 1):
          print("GANASTES")
    elif (ganador(turno) == -1):
          print("PERDISTES")
    else:
          print("EMPATE")
            



#PARTIDA IA VS HUMANO

def partida_mixta(estado):
    turno = 1  # Empieza el jugador negro
    contador_salta_turno = 0
    print("¿Quieres jugar como NEGRO (●) o BLANCO (○)?")
    print("\nFichas blancas -> 1")
    print("\nFichas negras -> 2")
    modo = validar_entrada_numerica(input("Elija sus fichas: "))

    humano = 1 if modo == 2 else 2
    ia = 2 if humano == 1 else 1

    while (contador_salta_turno<2):
        mostrar_tablero(estado.tablero)        
        
        if turno == 1:
            print("\nTurno del jugador NEGRO (●)")
        else:
            print("\nTurno del jugador BLANCO (○)")
            
        movimientos = posibles_movimientos(estado, turno)
            
        if (len(movimientos) != 0):
            if turno == humano:
                try:
                    new_fila = validar_entrada_numerica(input("Ingrese la fila (0-7): "))
                    new_columna = validar_entrada_numerica(input("Ingrese la columna (0-7): "))

                    if not (0 <= new_fila <= 7 and 0 <= new_columna <= 7):
                        print("Coordenadas fuera de rango. Deben estar entre 0 y 7.")
                        continue
                    if estado.tablero[new_fila][new_columna] != 0:
                        print("Ya hay una ficha en esa posición.")
                        continue

                    turno, _ = turnos(turno, new_fila, new_columna, estado)
                    contador_salta_turno = 0

                except EntradaNoNumericaError as e:
                    print(e)
                except MovimientoInvalidoError:
                    print("Movimiento inválido. Intente de nuevo.")
                except JugadorInvalidoError:
                    print("Error: turno inválido.")

            else:  # Turno de la IA
                accion = random.choice(movimientos)
                turno, _ = turnos(turno, accion[0], accion[1], estado)
                contador_salta_turno = 0

        else:
                    print("No hay movimientos posibles, le toca al otro jugador")
                    contador_salta_turno +=1
                    if turno == 1:
                        turno = 2
                    else: 
                        turno = 1

    print("Juego terminado")
    if (ganador(turno) == 1):
          print("GANASTES")
    elif (ganador(turno) == -1):
          print("PERDISTES")
    else:
          print("EMPATE")
            

