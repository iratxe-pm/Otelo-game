from reglas_juego.avance_de_juego import modificar_tablero
from reglas_juego.inicializa_tablero import ficha_blanca, ficha_negra, tablero
from partida_ia_vs_ia import partida_ia_vs_ia


def main():
    print("Bienvenido al editor de tablero de Otelo")
    
    # Inicializar tablero vacío
    
    # Permitir al usuario modificar el tablero
    modificar_tablero(tablero(ficha_blanca (), ficha_negra ()))

if __name__ == "__main__":
    print("1) Humano vs Humano")
    print("2) Humano vs IA")
    print("3) IA vs IA")
    modo = input("Selecciona modo: ")

    if(modo == "1"):
        main()
    elif (modo == "2"):
        modificar_tablero(tablero(ficha_blanca(), ficha_negra()))
    elif (modo == "3"):
        partida_ia_vs_ia()
    else:
        print("Incorrecto, tienes que elegir entre 1,2 y 3.")
    