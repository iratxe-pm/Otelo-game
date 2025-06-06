from reglas_juego.avance_de_juego import modificar_tablero
from reglas_juego.inicializa_tablero import ficha_blanca, ficha_negra, tablero


def main():
    print("Bienvenido al editor de tablero de Otelo")
    
    # Inicializar tablero vacío
    
    # Permitir al usuario modificar el tablero
    modificar_tablero(tablero(ficha_blanca (), ficha_negra ()))

if __name__ == "__main__":
    main()
    