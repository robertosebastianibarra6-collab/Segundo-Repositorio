#Roberto Sebastian Ibarra Aguilar
#CBTIS89
#Ventana de saludo

import tkinter as tk

ventana=tk.Tk()
ventana.title("Ventana de saludo")
ventana.geometry("400x300")

etiqueta=tk.Label(ventana, text="Hola, buenos dias", font=("Arial",16))
etiqueta.pack(pady=20)

def saludar():
    etiqueta.config(text="Que tal, ¿Como estas?")


boton= tk.Button(ventana, text="Saludar", command=saludar)
boton.pack(pady=10)

ventana.mainloop()
