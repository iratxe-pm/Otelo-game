from partidas.partida_automatica import partida_automática
from partidas.partida_manual import partida_manual
from partidas.partida_mixta import partida_mixta
from reglas_juego.estado_juego import EstadoJuego
from partida_ia_vs_ia import partida_ia_vs_ia


def main():
    print("Bienvenido al editor de tablero de Otelo")
    
    # Inicializar tablero vacío
    
    # Permitir al usuario modificar el tablero

if __name__ == "__main__":
    print("1) Humano vs Humano")
    print("2) Humano vs IA")
    print("3) IA vs IA")
    modo = input("Selecciona modo: ")

    if(modo == "1"):
        partida_manual(EstadoJuego())
    elif (modo == "2"):
        partida_mixta(EstadoJuego())
    elif (modo == "3"):
        #partida_ia_vs_ia() # ejecutar SOLO para crear csv
        partida_automática(EstadoJuego()) #ejecutar pa ver flujo
    else:
        print("Incorrecto, tienes que elegir entre 1,2 y 3.")
    