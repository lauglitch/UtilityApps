import tkinter as tk
import random

# Definición de esencias y sus pesos
esencias = ["Tierra ⛰️", "Aire 🌬️", "Agua 🌊", "Fuego 🔥"]
pesos = [35, 30, 20, 15]


def generar_esencia():
    esencia = random.choices(esencias, weights=pesos, k=1)[0]
    resultado_label.config(text=f"Esencia: {esencia}")
    historial.insert(tk.END, esencia)
    contador_label.config(text=f"Total generadas: {historial.size()}")


def cerrar_app():
    root.destroy()


# Interfaz principal
root = tk.Tk()
root.title("Generador de Esencias Elementales")
root.geometry("400x400")
root.configure(bg="#804fa1")  # Fondo de la ventana

# Contenedor principal
frame = tk.Frame(root, padx=20, pady=20, bg="#662b8d")
frame.pack(expand=True, fill="both")

# Botón de generar
boton_generar = tk.Button(
    frame,
    text="🔮 Generar Esencia",
    font=("Arial", 14),
    command=generar_esencia,
    bg="#b388eb",
    fg="white",
    activebackground="#d3a4f5",
)
boton_generar.pack(pady=10)

# Etiqueta de resultado
resultado_label = tk.Label(
    frame,
    text="Pulsa el botón para comenzar",
    font=("Arial", 12),
    bg="#662b8d",
    fg="white",
)
resultado_label.pack()

# Contador
contador_label = tk.Label(
    frame, text="Nº Esencias generadas: 0", font=("Arial", 10), bg="#662b8d", fg="white"
)
contador_label.pack(pady=5)

# Historial
historial = tk.Listbox(
    frame, height=10, width=30, bg="#f3e5f5", fg="#4a0072", font=("Arial", 10)
)
historial.pack(pady=5)


root.mainloop()
