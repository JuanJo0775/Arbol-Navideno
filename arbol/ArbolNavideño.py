import tkinter as tk
import random
import pygame

# ==========================
# CONFIGURACIÓN DE MÚSICA
# ==========================

# Inicializar pygame para manejar sonido
pygame.mixer.init()

# Cargar y reproducir la música (asegúrate de que la ruta sea correcta)
pygame.mixer.music.load("media/Sonido_de_Navidad.mp3")
pygame.mixer.music.play(-1)  # (-1) = reproducir en bucle

# ==========================
# CONFIGURACIÓN DEL ÁRBOL
# ==========================

# Colores posibles de las luces
colores = ["red", "green", "cyan", "magenta", "blue", "white"]

# Estructura del árbol navideño
arbol = [
    "       ★       ",
    "               ",
    "       *       ",
    "      ***      ",
    "     *****     ",
    "    *******    ",
    "   *********   ",
    "  ***********  ",
    " ************* ",
    "***************",
    "      | |      ",
    "      | |      ",
]

# ==========================
# FUNCIÓN DE DIBUJO
# ==========================

def generar_arbol():
    """Dibuja el árbol navideño en el canvas, con luces parpadeantes."""
    canvas.delete("all")
    tamaño_fuente = 18

    # Obtener tamaño del canvas
    alto_canvas = canvas.winfo_height()
    ancho_canvas = canvas.winfo_width()
    alto_arbol = len(arbol) * (tamaño_fuente + 2)

    # Centrar el árbol verticalmente
    y_inicial = (alto_canvas - alto_arbol) // 2

    # Dibujar cada línea
    for i, linea in enumerate(arbol):
        y = y_inicial + i * (tamaño_fuente + 2)
        texto_ancho = len(linea) * 11
        x_inicial = (ancho_canvas - texto_ancho) // 2  # Centrado horizontal

        for j, ch in enumerate(linea):
            if ch == "*":
                color = random.choice(colores)
                canvas.create_text(
                    x_inicial + j * 12, y, text=ch, fill=color, font=("Consolas", tamaño_fuente)
                )
            elif ch == "★":
                canvas.create_text(
                    x_inicial + j * 12, y, text=ch, fill="yellow", font=("Consolas", tamaño_fuente + 4)
                )
            elif ch in "|=_-":
                canvas.create_text(
                    x_inicial + j * 12, y, text=ch, fill="white", font=("Consolas", tamaño_fuente)
                )

    # Actualizar cada medio segundo
    root.after(500, generar_arbol)

# ==========================
# CONFIGURACIÓN DE LA VENTANA
# ==========================

root = tk.Tk()
root.title("Árbol de Navidad 🎄")
root.configure(bg="black")

# Centrar la ventana en pantalla
window_width = 450
window_height = 500
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_pos = (screen_width // 2) - (window_width // 2)
y_pos = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x_pos}+{y_pos}")

# Crear el canvas donde se dibuja el árbol
canvas = tk.Canvas(root, width=window_width, height=window_height, bg="black", highlightthickness=0)
canvas.pack(fill="both", expand=True)

# ==========================
# INICIAR ANIMACIÓN
# ==========================

generar_arbol()
root.mainloop()
