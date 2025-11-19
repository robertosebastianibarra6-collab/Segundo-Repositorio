#Roberto Sebastian Ibarra Aguilar
#CBTIS89
#Ej12

import tkinter as tk
from tkinter import ttk

ventana=tk.Tk()
ventana.title("lista desplegable combobox")
ventana.geometry("400x300")

etiqueta = tk.Label(ventana, text="Elige una opcion: ")
etiqueta.pack(pady=10)


opciones = ["Rojo","Verde","Azul","Amarillo","Morado"]
ComboColores = ttk.Combobox(ventana, values=opciones, state="readonly")
ComboColores.pack(pady=5)


def mostrar_seleccion(event):
    selecion = ComboColores.get()

    if selecion == "Rojo":
        etiqueta_colores.config( backgraund = "red")
        color = "red"
    elif selecion == "Azul":
        etiqueta_colores.config( backgraund = "blue")
        color = "blue"
        etiqueta_resultado.config ( text=f"Has seleccionado el color {selecion}", fg = color,backgraund="black")       
    

ComboColores.bind("<<ComboboxSelected>>",mostrar_seleccion)

etiqueta_resultado = tk.Label(ventana, text="Aun no eliges una opcion ")
etiqueta_resultado.pack(pady=20)

etiqueta_colores = tk.Label(text=" ")
etiqueta_colores.pack(pady=2)

ventana.mainloop()
