


import tkinter as tk


ventana = tk.Tk()
ventana.title("Mostrar Nombre Completo")
ventana.geometry("300x250")


etiqueta_nombre = tk.Label(ventana, text="Nombre:", font=("Arial", 12))
etiqueta_nombre.pack(pady=(10, 0))
entrada_nombre = tk.Entry(ventana, font=("Arial", 12))
entrada_nombre.pack(pady=5)


etiqueta_apellido = tk.Label(ventana, text="Apellido:", font=("Arial", 12))
etiqueta_apellido.pack(pady=(10, 0))
entrada_apellido = tk.Entry(ventana, font=("Arial", 12))
entrada_apellido.pack(pady=5)


def mostrar_nombre_completo():
    nombre = entrada_nombre.get()
    apellido = entrada_apellido.get()
    nombre_completo = f"{nombre} {apellido}"
    etiqueta_resultado.config(text=f"Nombre completo: {nombre_completo}")


boton = tk.Button(ventana, text="Mostrar el Nombre", command=mostrar_nombre_completo)
boton.pack(pady=15)


etiqueta_resultado = tk.Label(ventana, text="", font=("Arial", 12), fg="blue")
etiqueta_resultado.pack(pady=5)


ventana.mainloop()

