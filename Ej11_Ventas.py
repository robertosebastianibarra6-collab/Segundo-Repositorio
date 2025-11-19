#Roberto Sebastian Ibarra Aguilar
#CBTIS89
#Ventas


import tkinter as tk
from tkinter import messagebox

ventana=tk.Tk()
ventana.title("Calculo de Ventas")
ventana.geometry("400x300")


etiqueta_cantidad = tk.Label(ventana, text="Ingresa la cantidad de articulos: ")
etiqueta_cantidad.pack(pady=5)

etiqueta_cantidad = tk.Entry(ventana, justify="center")
etiqueta_cantidad.pack(pady=5)

etiqueta_precio = tk.Label(ventana, text="Ingresa el precio de los articulos: ")
etiqueta_precio.pack(pady=5)

etiqueta_precio = tk.Entry(ventana, justify="center")
etiqueta_precio.pack(pady=5)


def subtotal():
    try:
        precio = float(etiqueta_precio.get())
        cantidad = float(etiqueta_cantidad.get())
        
        subtotal = precio*cantidad

        etiqueta_resultado.config(text=f"Subtotal: {subtotal} ")
    except ValueError:
        messagebox.showerror("Error", "Por favor Ingrese una cantidad.")

def iva():
    try:
        precio = float(etiqueta_precio.get())
        cantidad = float(etiqueta_cantidad.get())
        
        subtotal = precio*cantidad
        
        iva = subtotal*0.16

        etiqueta_resultado.config(text=f"IVA: {iva}") 
    except ValueError:
        messagebox.showerror("Error", "Por favor Ingrese una cantidad.")

def total():
    try:
        precio = float(etiqueta_precio.get())
        cantidad = float(etiqueta_cantidad.get())
        
        subtotal = precio*cantidad
        
        iva = subtotal*0.16

        total = iva+subtotal

        etiqueta_resultado.config(text=f"Total: {total}") 
    except ValueError:
        messagebox.showerror("Error", "Por favor Ingrese una cantidad.")


btn_subtotal = tk.Button(ventana,text="Subtotal",command= subtotal, bg="green",fg="white")
btn_subtotal.pack(pady=5)

btn_iva = tk.Button(ventana,text="IVA",command=iva, bg="red",fg="white")
btn_iva.pack(pady=5)

btn_total = tk.Button(ventana,text="El total a pagar es de: ",command=total)
btn_total.pack(pady=5)

etiqueta_resultado = tk.Label(ventana,text="",font=("Arial",12,"bold"))
etiqueta_resultado.pack(pady=5)  

ventana.mainloop()

