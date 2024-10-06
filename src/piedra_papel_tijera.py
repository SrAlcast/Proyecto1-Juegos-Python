import random

class PiedraPapelTijeraLagartoSpock:
    opciones = ['piedra', 'papel', 'tijera', 'lagarto', 'spock']
    reglas = {
        'piedra': ['tijera', 'lagarto'],
        'papel': ['piedra', 'spock'],
        'tijera': ['papel', 'lagarto'],
        'lagarto': ['spock', 'papel'],
        'spock': ['tijera', 'piedra']
    }

    def __init__(self, rondas_para_ganar=3):
        self.victorias_jugador = 0
        self.victorias_maquina = 0
        self.rondas_jugadas=1
        self.rondas_para_ganar = rondas_para_ganar

    def determinar_ganador(self, opcion_jugador, opcion_maquina):
        if opcion_jugador == opcion_maquina:
            return 'Empate'
        elif opcion_maquina in self.reglas[opcion_jugador]:
            return 'Jugador'
        else:
            return 'Máquina'

    def jugar_ronda(self):
        """Ejecuta una ronda del juego."""
        print(f"Ronda {self.rondas_jugadas}")
        print("Elige: piedra, papel, tijera, lagarto, spock")
        opcion_jugador = input("Elige piedra, papel, tijera, lagarto, spock : ").lower()

        if opcion_jugador not in self.opciones:
            print("   Opción no válida. Intenta de nuevo.\n")
            return  

        opcion_maquina = random.choice(self.opciones)
        print(f"\nTú elgiste: {opcion_jugador}")
        print(f"Máquina eligió: {opcion_maquina}")

        ganador = self.determinar_ganador(opcion_jugador, opcion_maquina)

        if ganador == 'Jugador':
            self.victorias_jugador += 1
            self.rondas_jugadas +=1
            print("¡Ganaste esta ronda!")
        elif ganador == 'Máquina':
            self.victorias_maquina += 1
            self.rondas_jugadas +=1
            print("La máquina ganó esta ronda.")
        else:
            self.rondas_jugadas +=1
            print("Esta ronda fue empate.")
        print(f"\nMarcador: Jugador {self.victorias_jugador} - {self.victorias_maquina} Máquina\n")
    
    def jugar_de_nuevo(self):
        """Pregunta al jugador si desea continuar, en un bucle hasta obtener una respuesta válida."""
        while True:
            respuesta = input("¿Quieres jugar otra vez? (si/no): ").lower()
            if respuesta == 'si':
                return True
            elif respuesta == 'no':
                return False
            else:
                print("Opción no válida. Por favor, ingresa 'si' o 'no' para continuar.")
 
    def jugarPiedraPapelTijeraLagartoSpock(self):
        print("\033[1m¡Bienvenido a Piedra, Papel, Tijera, Lagarto, Spock!\033[0m\n\n\
Gana el primero que llegue a 3 victorias\n\n\
Reglas del juego:\n\
Piedra aplasta a tijera y aplasta a lagarto.\n\
Papel envuelve a piedra y refuta a Spock.\n\
Tijera corta a papel y decapita a lagarto.\n\
Lagarto envenena a Spock y devora a papel.\n\
Spock aplasta a tijera y vaporiza a piedra.\n"
        )
        while True:
            self.jugar_ronda()
            # Comprobar si uno de los jugadores ha alcanzado el número de victorias necesarias
            if self.victorias_jugador == self.rondas_para_ganar or self.victorias_maquina == self.rondas_para_ganar:
                if self.victorias_jugador == self.rondas_para_ganar:
                    print(f"\033[1m¡Felicidades! Ganaste el juego con {self.victorias_jugador} victorias.\033[0m\n \n¿Quieres jugar otra vez? (si/no)\n")
                else:
                    print(f"\033[1mLa máquina ganó el juego con {self.victorias_maquina} victorias.\033[0m\n \n¿Quieres jugar otra vez? (si/no)\n")
                if not self.jugar_de_nuevo():
                    print("\n\033[1m---- GAME OVER ----\033[0m\n")
                    break
                else:
                    print("\033[1m\nNueva Partida!\033[0m\n")
                    self.victorias_jugador = 0
                    self.victorias_maquina = 0
                    self.rondas_jugadas=1




