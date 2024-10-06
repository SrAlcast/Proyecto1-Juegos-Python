import random

class TresEnRaya:
    def __init__(self):
        """Inicializa el tablero, establece los símbolos y determina quién empieza."""
        self.tablero = [[" " for _ in range(3)] for _ in range(3)]  # Tablero vacío 3x3
        self.jugador = "X"  # Jugador siempre será "X"
        self.maquina = "O"  # La máquina será "O"
        self.turno_actual = random.choice([self.jugador, self.maquina])  # Selección aleatoria de quién empieza
        self.juego_activo = True  # Para controlar si el juego está en marcha

    def mostrar_tablero(self):
        """Muestra el tablero actual en la consola."""
        for fila in self.tablero:
            print(" | ".join(fila))
            print("__" * 5)  # Separador de filas

    def es_posicion_valida(self, fila, columna):
        """Verifica si la posición dada está vacía."""
        return self.tablero[fila][columna] == " "

    def hacer_movimiento(self, fila, columna, jugador):
        """Coloca el símbolo del jugador en la posición especificada."""
        if self.es_posicion_valida(fila, columna):
            self.tablero[fila][columna] = jugador
            return True
        return False

    def movimiento_maquina(self):
        """La máquina elige una casilla disponible aleatoriamente."""
        while True:
            fila = random.randint(0, 2)
            columna = random.randint(0, 2)
            if self.hacer_movimiento(fila, columna, self.maquina):
                break
        print("\nLa máquina ha hecho su movimiento.\n")

    def hay_ganador(self, jugador):
        """Verifica si el jugador ha conseguido tres en raya."""
        # Comprobación de filas
        for fila in self.tablero:
            if all([celda == jugador for celda in fila]):
                return True

        # Comprobación de columnas
        for columna in range(3):
            if all([self.tablero[fila][columna] == jugador for fila in range(3)]):
                return True

        # Comprobación de diagonales
        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] == jugador:
            return True
        if self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] == jugador:
            return True

        return False

    def tablero_lleno(self):
        """Verifica si el tablero está lleno."""
        return all([celda != " " for fila in self.tablero for celda in fila])

    def turno_jugador(self):
        """Gestiona el turno del jugador pidiendo coordenadas."""
        while True:
            try:
                fila = int(input("Elige una fila (0, 1, 2): "))
                columna = int(input("Elige una columna (0, 1, 2): "))
                if fila in [0, 1, 2] and columna in [0, 1, 2]:
                    if self.hacer_movimiento(fila, columna, self.jugador):
                        break
                    else:
                        print("La casilla ya está ocupada. Intenta otra.")
                else:
                    print("Entrada no válida. Debes elegir números entre 0 y 2.")
            except ValueError:
                print("Entrada no válida. Introduce un número.")

    def jugartresenraya(self):
        print("\033[1m¡Bienvenido al Tres en Raya!\033[0m\n")
        print("El objetivo del juego es conseguir alinear tres de tus símbolos\n" 
            "de manera horizontal, vertical o diagonal antes que el oponente.\n")
        print("Este es el tablero de juego. Escoge la posicion por filas y columnas\n"
              "con posiciones del 0 al 2, de izquierda a derecha y de arriba a bajo\n")
        while self.juego_activo:
            self.mostrar_tablero()
            if self.turno_actual == self.jugador:
                print("\nEs tu turno:\n")
                self.turno_jugador()
                if self.hay_ganador(self.jugador):
                    self.mostrar_tablero()
                    print("\n\033[1m¡Felicidades! ¡Has ganado!\033[0m")
                    print("¿Quieres jugar otra partida? (si/no)")
                    self.juego_activo = False
                else:
                    self.turno_actual = self.maquina
            else:
                self.movimiento_maquina()
                if self.hay_ganador(self.maquina):
                    self.mostrar_tablero()
                    print("La máquina ha ganado. ¡Suerte la próxima vez!")
                    print("¿Quieres jugar otra partida? (si/no)")
                    self.juego_activo = False
                else:
                    self.turno_actual = self.jugador

            # Verificar si el tablero está lleno y hay empate
            if self.tablero_lleno() and self.juego_activo:
                print("El tablero está lleno. ¡Es un empate!")
                self.juego_activo = False

        # Preguntar si quieren jugar de nuevo
        self.jugar_nuevamente()

    def jugar_nuevamente(self):
        respuesta_reinicio = input("¿Quieres jugar otra partida? (si/no): ").lower()
        while respuesta_reinicio:
            if respuesta_reinicio == "si":
                print("Has respondido que si\n-------------------------------------\n")
                self.__init__()  # Reiniciar el juego
                self.jugartresenraya()
            elif respuesta_reinicio == "no":
                print("\n\033[1m---- GAME OVER ----\033[1m")
                break
            else:
                print("Respuesta no valida. Responde si o no")
                respuesta_reinicio = input("¿Quieres jugar otra partida? (si/no): ")

