#Roberto Sebastian Ibarra Aguilar
#CBTIS89
#Iva y Descuento

import tkinter as tk
from tkinter import messagebox

ventana=tk.Tk()
ventana.title("Iva y Descuento")
ventana.geometry("400x300")
ventana.resizable(False,False)

etiqueta_cantidad = tk.Label(ventana, text="Ingresa una cantadad: ")
etiqueta_cantidad.pack(pady=10)

entrada_cantidad = tk.Entry(ventana,justify="center")
entrada_cantidad.pack()

def iva():
    try:
        cantidad = float(entrada_cantidad.get())

        iva = cantidad*0.16

        etiqueta_resultado.config(text=f"IVA (16%): ${iva:.2f}") # El 2F es para el nujmero de decimales que quieres 
    except ValueError:
        messagebox.showerror("Error", "Por favor Ingrese una cantidad.")

def descuento():
    try:
        cantidad = float(entrada_cantidad.get())

        desceunto = cantidad*0.10

        etiqueta_resultado.config(text=f"Desceunto (10%): ${desceunto:.2f}")  
    except ValueError:
        messagebox.showerror("Error", "Por favor Ingrese una cantidad.")                                            

def total():
    try:
        cantidad = float(entrada_cantidad.get())

        iva = cantidad*0.16
        descuento = cantidad*0.10

        total = cantidad + iva - descuento 

        etiqueta_resultado.config(text=f"Total a pagar: ${total:.2f}")

    except ValueError:
        messagebox.showerror("Error", "Por favor Ingrese una cantidad.") 


btn_iva = tk.Button(ventana,text="Calcular IVA",command=iva, bg="red",fg="white")
btn_iva.pack(pady=5)

btn_descuento = tk.Button(ventana,text="Calcular Descuento",command= descuento, bg="green",fg="white")
btn_descuento.pack(pady=5)

btn_total = tk.Button(ventana,text="El total a pagar es de: ",command=total)
btn_total.pack(pady=5)


etiqueta_resultado = tk.Label(ventana,text="",font=("Arial",12,"bold"))
etiqueta_resultado.pack(pady=15)

ventana.mainloop()















