# Proyecto Módulo 1

![imagen](https://www.rotulatumismo.com/47000-large_default/neon-game-zone.jpg))

## Introducción

¡Bienvenido a nuestro primer proyecto! En este proyecto, una empresa nos ha contactado para desarrollar una serie de videojuegos clásicos utilizando Python. A continuación, se describen brevemente los juegos seleccionados y cómo se implementó la consola de selección de juegos.

## Juegos Seleccionados

### 1. Preguntados

En este juego, los jugadores responden a una serie de preguntas de diversas categorías (cultura general, historia, entretenimiento, etc.). El objetivo es responder correctamente 10 preguntas seguidas. Si el jugador falla en alguna pregunta, el juego termina.

### 2. Tres en Raya

Este clásico juego de estrategia se juega en un tablero de 3x3. Dos jugadores (el usuario y la máquina) se turnan para colocar sus símbolos (X o O) en el tablero. El primero en alinear tres símbolos en horizontal, vertical o diagonal gana la partida.

### 3. Ahorcado

El jugador intenta adivinar una palabra secreta eligiendo letras. Cada vez que el jugador falla, se dibuja una parte del personaje en la horca. El juego termina cuando el jugador adivina la palabra completa o se completa el dibujo del ahorcado.

### 4. Piedra, Papel, Tijera, Lagarto, Spock

Los jugadores eligen entre cinco opciones y se determina el ganador según las reglas del juego. Gana el primero que alcance tres victorias. Este juego es una variante divertida del clásico piedra, papel y tijera, incorporando más opciones.

### 5. Hundir la Flota (Descartado)

Aunque inicialmente se pensó en incluir "Hundir la Flota", finalmente decidí no implementarlo en este proyecto. El enfoque se mantuvo en los otros cuatro juegos seleccionados.

## Consola de Selección de Juegos

Para facilitar la experiencia del usuario, implementé una consola de selección de juegos que permite al jugador elegir entre los diferentes juegos disponibles. La consola funciona de la siguiente manera:

1. **Menú Principal**: Al iniciar el programa, se presenta un menú donde el usuario puede seleccionar el juego que desea jugar.
  
2. **Selección de Juego**: Cada opción del menú está vinculada a una función específica de cada juego. El usuario simplemente elige el número correspondiente al juego deseado.

3. **Repetición**: Al finalizar un juego, se ofrece al jugador la opción de volver a jugar el mismo juego, regresar al menú de selección de juegos o salir del programa.

4. **Estructura Modular**: Cada juego está implementado como una clase en su propio archivo `.py`, lo que facilita la gestión del código y la escalabilidad del proyecto.

## Instalación

Para instalar y ejecutar el proyecto en tu máquina local, sigue estos pasos:

1. **Clona el repositorio**:
   ```bash
   git clone [URL del repositorio]
