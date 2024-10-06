import random

class Pregunta:
    def __init__(self, categoria, pregunta, opciones, opcion_correcta):
        self.categoria = categoria
        self.pregunta = pregunta
        self.opciones = opciones
        self.opcion_correcta = opcion_correcta

class Preguntados:
    def __init__(self):
        self.categorias = {
    "Cultura General": [
        Pregunta(
            "Cultura General",
            "¿Cuál es la capital de Italia?",
            ["a) Roma", "b) Milán", "c) Venecia", "d) Florencia"],
            "a"        ),
        Pregunta(
            "Cultura General",
            "¿Qué país es famoso por sus canguros?",
            ["a) Sudáfrica", "b) Australia", "c) Canadá", "d) Argentina"],
            "b"        ),
        Pregunta(
            "Cultura General",
            "¿Cuál es el idioma más hablado en el mundo?",
            ["a) Inglés", "b) Mandarín", "c) Español", "d) Árabe"],
            "b"        ),
        Pregunta(
            "Cultura General",
            "¿Cuál es el océano más grande del mundo?",
            ["a) Atlántico", "b) Índico", "c) Ártico", "d) Pacífico"],
            "d"        ),
        Pregunta(
            "Cultura General",
            "¿Qué instrumento musical tiene cuerdas y se toca con un arco?",
            ["a) Piano", "b) Guitarra", "c) Violín", "d) Saxofón"],
            "c"        )
    ],
    "Historia": [
        Pregunta(
            "Historia",
            "¿En qué año se descubrió América?",
            ["a) 1492", "b) 1500", "c) 1607", "d) 1776"],
            "a"        ),
        Pregunta(
            "Historia",
            "¿Quién fue el primer emperador de Roma?",
            ["a) Julius César", "b) Augusto", "c) Nerón", "d) Tiberio"],
            "b"        ),
        Pregunta(
            "Historia",
            "¿Qué guerra fue conocida como 'La Gran Guerra'?",
            ["a) Primera Guerra Mundial", "b) Segunda Guerra Mundial", "c) Guerra Civil Española", "d) Guerra de Vietnam"],
            "a"        ),
        Pregunta(
            "Historia",
            "¿Qué civilización construyó las pirámides de Egipto?",
            ["a) Mayas", "b) Aztecas", "c) Incas", "d) Egipcios"],
            "d"        ),
        Pregunta(
            "Historia",
            "¿Qué año marcó la caída del Muro de Berlín?",
            ["a) 1989", "b) 1991", "c) 1985", "d) 2000"],
            "a"        )
    ],
    "Deportes": [
        Pregunta(
            "Deportes",
            "¿Cuántos jugadores hay en un equipo de fútbol?",
            ["a) 9", "b) 10", "c) 11", "d) 12"],
            "c"        ),
        Pregunta(
            "Deportes",
            "¿Cuál es el deporte más popular en los Estados Unidos?",
            ["a) Fútbol", "b) Baloncesto", "c) Béisbol", "d) Fútbol americano"],
            "d"        ),
        Pregunta(
            "Deportes",
            "¿Qué país ganó la Copa Mundial de Fútbol de 2014?",
            ["a) Alemania", "b) Brasil", "c) Argentina", "d) Italia"],
            "a"        ),
        Pregunta(
            "Deportes",
            "¿En qué deporte se utiliza un disco llamado 'puck'?",
            ["a) Hockey", "b) Béisbol", "c) Baloncesto", "d) Fútbol"],
            "a"        ),
        Pregunta(
            "Deportes",
            "¿Qué atleta es conocido como 'El hombre más rápido del mundo'?",
            ["a) Usain Bolt", "b) Carl Lewis", "c) Jesse Owens", "d) Michael Johnson"],
            "a"        )
    ],
    "Ciencia": [
        Pregunta(
            "Ciencia",
            "¿Qué es el ADN?",
            ["a) Ácido Desoxirribonucleico", "b) Ácido Dextroribonucleico", "c) Ácido Deoxirribonucleico", "d) Ácido Dextrónico"],
            "a"        ),
        Pregunta(
            "Ciencia",
            "¿Cuál es el planeta más cercano al sol?",
            ["a) Venus", "b) Marte", "c) Mercurio", "d) Tierra"],
            "c"        ),
        Pregunta(
            "Ciencia",
            "¿Qué gas es esencial para la respiración humana?",
            ["a) Dióxido de carbono", "b) Oxígeno", "c) Nitrógeno", "d) Helio"],
            "b"        ),
        Pregunta(
            "Ciencia",
            "¿Qué tipo de animal es un delfín?",
            ["a) Mamífero", "b) Pez", "c) Reptil", "d) Anfibio"],
            "a"        ),
        Pregunta(
            "Ciencia",
            "¿Qué partícula subatómica tiene carga positiva?",
            ["a) Electrón", "b) Neutrón", "c) Protón", "d) Fotón"],
            "c"        )
    ],
    "Geografía": [
        Pregunta(
            "Geografía",
            "¿Cuál es la capital de Japón?",
            ["a) Pekín", "b) Seúl", "c) Tokio", "d) Bangkok"],
            "c"        ),
        Pregunta(
            "Geografía",
            "¿Cuál es el país más grande del mundo?",
            ["a) Canadá", "b) Rusia", "c) China", "d) Estados Unidos"],
            "b"        ),
        Pregunta(
            "Geografía",
            "¿Cuál es la montaña más alta del mundo?",
            ["a) K2", "b) Kangchenjunga", "c) Everest", "d) Makalu"],
            "c"        ),
        Pregunta(
            "Geografía",
            "¿Qué continente tiene más países?",
            ["a) África", "b) Asia", "c) Europa", "d) América"],
            "a"        ),
        Pregunta(
            "Geografía",
            "¿Cuál es la capital de Egipto?",
            ["a) El Cairo", "b) Túnez", "c) Trípoli", "d) Jartum"],
            "a"        )
    ]
}
        self.opcion_correctas = 0

    def Pregunta_random(self):
        categoria = random.choice(list(self.categorias.keys()))
        Pregunta = random.choice(self.categorias[categoria])
        return Pregunta

    def jugarpreguntados(self):
        print("\033[1m¡Bienvenido a Preguntados!\033[0m\n")
        print("El objetivo del jugador es responder correctamente\na las preguntas para avanzar en el juego.\n")
        print("El jugador gana si logra responder correctamente 5\npreguntas consecutivas. Si falla una pregunta, el juego termina.")
        while self.opcion_correctas < 2:
            Pregunta = self.Pregunta_random()
            print(f"\nCategoría: {Pregunta.categoria}")
            print(Pregunta.pregunta)
            for option in Pregunta.opciones:
                print(option)
            respuesta = input("Elige una opción (A, B, C, D): ").lower()
            while respuesta:
                if respuesta not in ["a", "b", "c", "d"]:
                    print("\nOpción no válida. Tienes que responder alguna de las opciones.")
                    respuesta = input("Elige una opción (A, B, C, D): ").lower()
                    continue
                if respuesta == Pregunta.opcion_correcta:
                    self.opcion_correctas += 1
                    print(f"\nTu respuesta es:{respuesta}")
                    print("\033[1m¡Respuesta correcta!\033[0m")
                    print(f"Llevas {self.opcion_correctas} respuestas correctas seguidas.")
                    respuesta=""
                    break
                else:
                    print(f"\nTu respuesta es:{respuesta}")
                    print(f"Respuesta incorrecta. ¡Has perdido!la respuesta correcta era la:{Pregunta.opcion_correcta}")
                    self.jugar_nuevamente()
                    break
        else:
            print(f"\n\033[1m¡Felicidades has ganado!\033[0m\nHas respondido {self.opcion_correctas} preguntas correctamente.\n")
            self.jugar_nuevamente()

    def jugar_nuevamente(self):
        print("\n¿Quieres jugar de nuevo? (si/no)\n")
        respuesta_reinicio = input("¿Quieres jugar otra partida? (si/no): ").lower()
        while respuesta_reinicio:
            if respuesta_reinicio == "si":
                print("Has respondido que si\n\n-------------------------------------\n")
                self.reset()
                self.jugarpreguntados()
            if respuesta_reinicio == "no":
                print("\n\033[1m---- GAME OVER ----\033[1m\n")
                break
            else:
                print("Respuesta no valida. Responde 'si' o 'no'")
                respuesta_reinicio = input("¿Quieres jugar otra partida? (si/no): ")

    def reset(self):
        self.opcion_correctas = 0
        self.respuesta_reinicio = ""
        self.jugarpreguntados()
