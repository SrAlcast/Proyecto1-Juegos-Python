# Archivo: menu_juegos.py
from src.piedra_papel_tijera import PiedraPapelTijeraLagartoSpock
from src.TresenRaya import TresEnRaya
from src.Preguntados import Preguntados
from src.Ahorcado import Ahorcado

def mostrar_menu():
    print("------------------------------------------")
    print("\nMenu de Juegos:\n")
    print("1. Piedra, Papel, Tijera, Lagarto, Spock")
    print("2. Tres en Raya")
    print("3. Preguntados")
    print("4. Ahorcado")
    print("5. Salir\n\n------------------------------------------\n")

def elegir_juego():
    while True:
        mostrar_menu()
        opcion = input("Elige un juego (1-5): ")
        if opcion == '1':
            juego = PiedraPapelTijeraLagartoSpock()
            juego.jugarPiedraPapelTijeraLagartoSpock()
        elif opcion == '2':  # Cambiado a 'elif'
            juego = TresEnRaya()
            juego.jugartresenraya()
        elif opcion == '3':  # Cambiado a 'elif'
            juego = Preguntados()
            juego.jugarpreguntados()
        elif opcion == '4':  # Cambiado a 'elif'
            juego = Ahorcado()
            juego.jugarAhorcado()
        elif opcion == '5':  # Opción para salir
            print("\nSaliendo del programa. ¡Hasta la próxima!")
            break
        else:
            print("Opción no válida. Por favor, elige una opción entre 1 y 5.")

# Iniciar el menú de selección de juegos
elegir_juego()
