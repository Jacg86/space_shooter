# Space Invaders

Un juego clásico de disparos en el espacio creado con Python y PyGame.

## Desarrollador
-  [Julio Curiel](https://github.com/Jacg86)

## Requisitos
- Python 3.x
- PyGame (`pip install pygame`)

## Cómo jugar
1.  Ejecuta el juego: `python -m space_shooter.main` (desde el directorio padre) o `python main.py` (dentro de la carpeta).
2.  **Menú Principal**: Presiona `ENTER` para comenzar.
3.  **Controles**:
    -   `Flecha Izquierda` / `Flecha Derecha`: Mover la nave.
    -   `Espacio`: Disparar.
4.  **Objetivo**: Destruye a los enemigos (cuadros rojos) para ganar puntos. Evita que te toquen.
5.  **Game Over**: Si un enemigo te toca, el juego termina. Presiona `ENTER` para volver al menú.

## Estructura del Proyecto
-   `main.py`: Archivo principal con el bucle del juego y menús.
-   `player.py`: Clase del jugador.
-   `enemy.py`: Clase de los enemigos.
-   `bullet.py`: Clase de los disparos.
-   `utils.py`: Constantes y funciones de utilidad.
