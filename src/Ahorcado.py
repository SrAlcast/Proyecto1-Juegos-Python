import random

class Ahorcado:
    def __init__(self):
        self.palabras = ['python', 'juego', 'ahorcado', 'secreto', 'maquina', 'palabra', 'inteligencia']
        self.palabra_secreta = random.choice(self.palabras)
        self.letras_adivinadas = []
        self.intentos_fallidos = 0
        self.max_intentos = 6
    
    def mostrar_tablero(self):
        tablero = [letra if letra in self.letras_adivinadas else '_' for letra in self.palabra_secreta]
        return ' '.join(tablero)
    
    def mostrar_horca(self):
        stages = [
            """
               -----
               |   |
               |
               |
               |
               |
            ---------
            """,  # 0 intentos fallidos
            """
               -----
               |   |
               |   O
               |
               |
               |
            ---------
            """,  # 1 intento fallido: cabeza
            """
               -----
               |   |
               |   O
               |   |
               |
               |
            ---------
            """,  # 2 intentos fallidos: tronco
            """
               -----
               |   |
               |   O
               |  /|
               |
               |
            ---------
            """,  # 3 intentos fallidos: brazo izquierdo
            """
               -----
               |   |
               |   O
               |  /|\\
               |
               |
            ---------
            """,  # 4 intentos fallidos: brazo derecho
            """
               -----
               |   |
               |   O
               |  /|\\
               |  /
               |
            ---------
            """,  # 5 intentos fallidos: pierna izquierda
            """
               -----
               |   |
               |   O
               |  /|\\
               |  / \\
               |
            ---------
            """   # 6 intentos fallidos: pierna derecha (fin del juego)
        ]
        print(stages[self.intentos_fallidos])

    def jugarAhorcado(self):
        print("\033[1m¡Bienvenido al juego del Ahorcado!\n\033[0m")
        print("El objetivo d es descubrir la palabra intentando\n"
              "adivinar una letra en cada turno.\n")
        print("El juego termina cuando el jugador adivina la palabra completa\n"
              "o cuando se dibuja por completo la figura en la horca\n")

        while self.intentos_fallidos < self.max_intentos:
            self.mostrar_horca()
            print(f"\nPalabra secreta: {self.mostrar_tablero()}")
            print(f"Letras adivinadas: {' '.join(self.letras_adivinadas)}")
            print(f"Intentos restantes: {self.max_intentos - self.intentos_fallidos}")
            
            # Adivinar una letra
            letra = input("Adivina una letra: ").lower()
            
            if len(letra) != 1 or not letra.isalpha():
                print("Por favor, introduce una letra válida.")
                continue
            
            if letra in self.letras_adivinadas:
                print("Ya has adivinado esa letra, intenta con otra.")
                continue
            
            # Añadir la letra a la lista de letras adivinadas
            self.letras_adivinadas.append(letra)
            
            if letra in self.palabra_secreta:
                print(f"¡Bien hecho! La letra '{letra}' está en la palabra.")
            else:
                print(f"La letra '{letra}' no está en la palabra.")
                self.intentos_fallidos += 1
            
            # Comprobar si el jugador ha ganado
            if all(letra in self.letras_adivinadas for letra in self.palabra_secreta):
                print(f"\n\n\033[1m¡Felicidades! Has adivinado la palabra: {self.palabra_secreta}\n\033[0m")
                print("¿Quieres jugar otra partida? (si/no)")
                self.jugar_nuevamente()
                break
        else:
            self.mostrar_horca()
            print(f"\nLo siento, has sido derrotado. La palabra secreta era: {self.palabra_secreta}")
            print("¿Quieres jugar otra partida? (si/no)")
            self.jugar_nuevamente()
            
    def jugar_nuevamente(self):
        respuesta_reinicio = input("¿Quieres jugar otra partida? (si/no): ").lower()
        while respuesta_reinicio:
            if respuesta_reinicio == "si":
                print("Has respondido que si\n-------------------------------------\n")
                self.__init__()  # Reiniciar el juego
                self.jugarAhorcado()
            if respuesta_reinicio == "no":
                print("\n\033[1m---- GAME OVER ----\033[1m")
                break
            else:
                print("Respuesta no valida. Responde 'si' o 'no'")
                respuesta_reinicio = input("¿Quieres jugar otra partida? (si/no): ")
