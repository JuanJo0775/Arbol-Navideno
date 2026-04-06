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

# ==========================
# FUNCIÓN GENERADORA DEL ÁRBOL
# ==========================

def generar_forma_arbol(altura, angulo=70):
    """
    Genera la forma del árbol como una lista de strings.
    
    Args:
        altura: Número de filas del triángulo
        angulo: Ángulo de inclinación en grados (aprox 70 para árbol típico)
    """
    arbres = []
    
    # Calcular incremento de asteriscos por fila basado en el ángulo
    # Para 70 grados: ~2.7 asteriscos por fila
    incremento = (angulo / 25)  # Ajuste para obtener la proporción correcta
    
    max_asteriscos = 1 + (altura - 1) * incremento
    max_asteriscos = int(max_asteriscos)
    
    if max_asteriscos % 2 == 0:
        max_asteriscos += 1
    
    espacios_totales = max_asteriscos - 1
    
    # Agregar estrella en la punta
    espacios_punta = espacios_totales // 2
    arbres.append(" " * espacios_punta + "★" + " " * espacios_punta)
    arbres.append("")
    
    # Generar el triángulo de asteriscos
    for fila in range(altura):
        num_asteriscos = 1 + fila * int(incremento)
        if num_asteriscos > max_asteriscos:
            num_asteriscos = max_asteriscos
        
        espacios = (max_asteriscos - num_asteriscos) // 2
        ligne = " " * espacios + "*" * num_asteriscos + " " * espacios
        arbres.append(ligne)
    
    # Agregar el tronco (solo dos |)
    espacios_tronco = (max_asteriscos - 1) // 2
    
    for _ in range(2):
        arbres.append(" " * espacios_tronco + "|" + " " * espacios_tronco)
    
    return arbres

# Generar el árbol con altura 10 y ángulo ~70 grados
arbol = generar_forma_arbol(altura=10, angulo=70)

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
root.title("Feliz Navidad")
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
