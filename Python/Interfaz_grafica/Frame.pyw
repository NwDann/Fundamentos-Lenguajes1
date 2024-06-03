
from tkinter import *

# frame sera un objeto de la clase Tk
frame = Tk()

# TITLE: Asignar un titulo al frame
frame.title("Primer frame hecho")

#RESIZABLE: Permite declarar si el ancho o alto pueden ser modificados por el usuario
frame.resizable(False, False)

#ICONBITMAP: Cambia el icono del programa
frame.iconbitmap("C:\\Users\\Hp\\Documents\\GitHub\\Fundamentos-Lenguajes1\\Python\\Interfaz_grafica\\icono.ico")

#GEOMETRY: Cambia el tamaño de la ventana
frame.geometry("800x600")

frame.config(bg = "orange")

# MAINLOOP: Mostrar el frame
frame.mainloop()