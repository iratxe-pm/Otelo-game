
from reglas_juego.excepciones import EntradaNoNumericaError, ValorFueraDeRango, validar_entrada_numerica, verificar_valor_en_rango
from partidas.partida_automatica import partida_automática
from partidas.partida_manual import partida_manual
from partidas.partida_mixta import partida_mixta
from reglas_juego.estado_juego import EstadoJuego
from partida_ia_vs_ia import partida_ia_vs_ia

def main():
    """
        Ejecuta el juego en tres modos diferentes:
            1. Humano vs Humano
            2. Humano vs IA
            3. IA vs IA *

        * NOTA: Si se quiere generar datos de entrenamiento nuevos para entrenar la red neuronal se debe de:
            1º descomentar la línea: " # partida_ia_vs_ia() " (línea: 39 )
            2º comentar la línea: " partida_automática(EstadoJuego()) (línea: 40 ) "
    """
    print("Bienvenido al editor de tablero de Otelo")

if __name__ == "__main__":
    print("1) Humano vs Humano")
    print("2) Humano vs IA")
    print("3) IA vs IA")

    while True:
        try: 
            modo = input("Selecciona modo: ")
            validar_entrada_numerica(modo)
            modo = int(modo)
            verificar_valor_en_rango(modo, 1, 3)

            if modo == 1:
                partida_manual(EstadoJuego())
            elif modo == 2:
                partida_mixta(EstadoJuego())
            elif modo == 3:
                # partida_ia_vs_ia()  # para generar datos de entrenamiento
                partida_automática(EstadoJuego())  # IA vs IA

            break 

        except (EntradaNoNumericaError, ValorFueraDeRango)  as e:
            print(f"Error: {e}. Inténtalo de nuevo.\n")



 