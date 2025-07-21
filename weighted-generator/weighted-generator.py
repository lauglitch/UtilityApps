import tkinter as tk
import random
from tkinter import messagebox

# Esencias
esencias = ["Tierra ⛰️", "Aire 🍃", "Agua 🌊", "Fuego 🔥"]


# Función para obtener pesos introducidos por el usuario
def obtener_pesos():
    try:
        pesos = [int(entry.get()) for entry in entries]
        if sum(pesos) != 100:
            raise ValueError("La suma debe ser 100")
        return pesos
    except:
        return None


# Generar esencia
def generar_esencia():
    pesos = obtener_pesos()
    if pesos:
        esencia = random.choices(esencias, weights=pesos, k=1)[0]
        resultado_label.config(text=f"Esencia: {esencia}")
        historial.insert(tk.END, esencia)
        contador_label.config(text=f"Total generadas: {historial.size()}")
    else:
        messagebox.showerror("Error", "Los porcentajes deben ser números y sumar 100.")


# Cerrar app
def cerrar_app():
    root.destroy()


# Interfaz
root = tk.Tk()
root.title("Generador de Esencias Elementales")
root.geometry("500x500")
root.configure(bg="#804fa1")

frame = tk.Frame(root, padx=20, pady=20, bg="#662b8d")
frame.pack(pady=20)

# Entrada de porcentajes
entries = []
for i, esencia in enumerate(esencias):
    fila = tk.Frame(frame, bg="#662b8d")
    fila.pack(pady=2)
    label = tk.Label(fila, text=f"{esencia} (%)", bg="#662b8d", fg="white", width=12)
    label.pack(side=tk.LEFT)
    entry = tk.Entry(fila, width=5)
    entry.insert(0, "25")  # Valor inicial
    entry.pack(side=tk.LEFT)
    entries.append(entry)

# Botón
boton_generar = tk.Button(
    frame, text="🔮 Generar Esencia", font=("Arial", 14), command=generar_esencia
)
boton_generar.pack(pady=10)

# Resultado
resultado_label = tk.Label(
    frame,
    text="Introduce los porcentajes y pulsa el botón",
    font=("Arial", 12),
    bg="#662b8d",
    fg="white",
)
resultado_label.pack()

contador_label = tk.Label(
    frame, text="Nº Esencias generadas: 0", font=("Arial", 10), bg="#662b8d", fg="white"
)
contador_label.pack(pady=5)

# Historial
historial = tk.Listbox(frame, height=10, width=40)
historial.pack(pady=5)

root.mainloop()
