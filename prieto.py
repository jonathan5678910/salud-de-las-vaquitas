import tkinter as tk                                    #salud de las vaquitas

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Prieto.py - Control de Ganado")
ventana.geometry("700x600")
ventana.configure(bg="#f0f0f0")

# 📌 Creación de un Frame para cada "Hoja"
frame_hoja1 = tk.Frame(ventana)
frame_hoja2 = tk.Frame(ventana)
frame_hoja3 = tk.Frame(ventana)

# 📌 Creación del Canvas para mostrar información en cada hoja
canvas1 = tk.Canvas(frame_hoja1, width=650, height=250, bg="white", relief="sunken", bd=3)
canvas1.pack(pady=20)

canvas2 = tk.Canvas(frame_hoja2, width=650, height=250, bg="white", relief="sunken", bd=3)
canvas2.pack(pady=20)

canvas3 = tk.Canvas(frame_hoja3, width=650, height=250, bg="white", relief="sunken", bd=3)
canvas3.pack(pady=20)


# 📌 Función para actualizar el Canvas
def actualizar_canvas(canvas, texto):
    canvas.delete("all")
    canvas.create_text(325, 125, text=texto, font=("Arial", 12, "bold"), fill="black", width=600)


# 📌 Funciones de cálculo en Hoja 1 (Pasto necesario)
entradas_animales_pasto = {}
animales = ["Vacas", "Toros", "Terneros", "Burros", "Caballos/Yeguas", "Mulas", "Ovejas/Chivos"]

frame_entrada_pasto = tk.Frame(frame_hoja1, bg="#f0f0f0")
frame_entrada_pasto.pack(pady=10)

tk.Label(frame_entrada_pasto, text="🔢 Ingresa la cantidad de cada animal:", font=("Arial", 10, "bold")).pack()

for animal in animales:
    frame = tk.Frame(frame_entrada_pasto)
    frame.pack(fill="x")

    tk.Label(frame, text=f"{animal}: ", font=("Arial", 10)).pack(side="left")

    entrada = tk.Entry(frame, width=5)
    entrada.pack(side="left")
    entradas_animales_pasto[animal] = entrada


def calcular_pasto():
    consumo_por_animal = {
        "Vacas": 40, "Toros": 45, "Terneros": 25, "Burros": 15,
        "Caballos/Yeguas": 30, "Mulas": 20, "Ovejas/Chivos": 10
    }

    total_pasto = 0
    detalles = "🌿 Consumo de pasto por día:\n"

    for animal, entrada in entradas_animales_pasto.items():
        cantidad = entrada.get()
        if cantidad.isdigit():
            cantidad = int(cantidad)
            total_pasto += cantidad * consumo_por_animal[animal]
            detalles += f"- {animal}: {cantidad} x {consumo_por_animal[animal]} kg = {cantidad * consumo_por_animal[animal]} kg\n"

    detalles += f"\n📌 **Total de pasto necesario:** {total_pasto} kg/día"
    actualizar_canvas(canvas1, detalles)


tk.Button(frame_hoja1, text="Calcular pasto necesario", command=calcular_pasto, font=("Arial", 10), bg="#0077b6",
          fg="white").pack(pady=10)


# 📌 Funciones de cálculo en Hoja 2 (Temperaturas)
def temperatura_animales():
    texto = ("🌡️ Temperatura que soportan:\n"
             "- Vacas: Día 35°C / Noche -10°C\n"
             "- Toros: Día 30°C / Noche -15°C\n"
             "- Terneros: Día 33°C / Noche -5°C\n"
             "- Burros: Día 40°C / Noche -5°C\n"
             "- Caballos/Yeguas: Día 38°C / Noche -8°C\n"
             "- Mulas: Día 42°C / Noche -6°C\n"
             "- Ovejas/Chivos: Día 39°C / Noche -7°C")
    actualizar_canvas(canvas2, texto)


tk.Button(frame_hoja2, text="Mostrar temperaturas", command=temperatura_animales, font=("Arial", 10), bg="#0077b6",
          fg="white").pack(pady=10)

# 📌 Funciones de cálculo en Hoja 3 (Agua necesaria)
entradas_animales_agua = {}

frame_entrada_agua = tk.Frame(frame_hoja3, bg="#f0f0f0")
frame_entrada_agua.pack(pady=10)

tk.Label(frame_entrada_agua, text="💧 Ingresa la cantidad de cada animal:", font=("Arial", 10, "bold")).pack()

for animal in animales:
    frame = tk.Frame(frame_entrada_agua)
    frame.pack(fill="x")

    tk.Label(frame, text=f"{animal}: ", font=("Arial", 10)).pack(side="left")

    entrada = tk.Entry(frame, width=5)
    entrada.pack(side="left")
    entradas_animales_agua[animal] = entrada


def calcular_agua():
    consumo_por_animal = {
        "Vacas": 50, "Toros": 60, "Terneros": 30, "Burros": 20,
        "Caballos/Yeguas": 40, "Mulas": 25, "Ovejas/Chivos": 12
    }

    total_agua = 0
    detalles = "💧 Consumo de agua por día:\n"

    for animal, entrada in entradas_animales_agua.items():
        cantidad = entrada.get()
        if cantidad.isdigit():
            cantidad = int(cantidad)
            total_agua += cantidad * consumo_por_animal[animal]
            detalles += f"- {animal}: {cantidad} x {consumo_por_animal[animal]} L = {cantidad * consumo_por_animal[animal]} L\n"

    detalles += f"\n📌 **Total de agua necesaria:** {total_agua} L/día"
    actualizar_canvas(canvas3, detalles)


tk.Button(frame_hoja3, text="Calcular agua necesaria", command=calcular_agua, font=("Arial", 10), bg="#0077b6",
          fg="white").pack(pady=10)


# 📌 Función para cambiar entre hojas
def mostrar_hoja(hoja):
    frame_hoja1.pack_forget()
    frame_hoja2.pack_forget()
    frame_hoja3.pack_forget()

    if hoja == 1:
        frame_hoja1.pack()
    elif hoja == 2:
        frame_hoja2.pack()
    elif hoja == 3:
        frame_hoja3.pack()


# 📌 Botones de navegación entre hojas
frame_navegacion = tk.Frame(ventana, bg="#f0f0f0")
frame_navegacion.pack(side="bottom", fill="x")

tk.Button(frame_navegacion, text="🌿 Hoja 1: Pasto", command=lambda: mostrar_hoja(1), font=("Arial", 10), bg="#28a745",
          fg="white").pack(side="left", padx=5, pady=5)
tk.Button(frame_navegacion, text="🌡️ Hoja 2: Temperaturas", command=lambda: mostrar_hoja(2), font=("Arial", 10),
          bg="#dc3545", fg="white").pack(side="left", padx=5, pady=5)
tk.Button(frame_navegacion, text="💧 Hoja 3: Agua", command=lambda: mostrar_hoja(3), font=("Arial", 10), bg="#0077b6",
          fg="white").pack(side="left", padx=5, pady=5)

tk.Button(frame_navegacion, text="❌ Salir", command=ventana.quit, font=("Arial", 12, "bold"), bg="#d62828",
          fg="white").pack(side="right", padx=5, pady=5)

mostrar_hoja(1)

ventana.mainloop()
