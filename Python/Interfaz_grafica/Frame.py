
from tkinter import *

# window sera un objeto de la clase Tk
window = Tk()

# TITLE: Asignar un titulo al window
window.title("Primer window hecho")

#RESIZABLE: Permite declarar si el ancho o alto pueden ser modificados por el usuario
window.resizable(False, False)

#ICONBITMAP: Cambia el icono del programa
window.iconbitmap("C:\\Users\\Hp\\Documents\\GitHub\\Fundamentos-Lenguajes1\\Python\\Interfaz_grafica\\icono.ico")

#GEOMETRY: Cambia el tamaño de la ventana
window.geometry("800x600")

#CONFIG: Varios parametros, pero este cambia el color del fondo de la ventana
window.config(bg = "orange")


#FRAME de la libreria tk
primer_frame = Frame()

# Empaqueta el window con el frame creado, puede ir parametro de ubicacion "side" para el frame
# Algunas entradas para side: left, right, top (centrar arriba)
primer_frame.pack(side = "left")

# CONFIG: Varios parametros, pero este cambia el color del fondo del frame, alto y ancho tambien
primer_frame.config(bg = "red", width = "300", height = "300")



# MAINLOOP: Mostrar el window
window.mainloop()

#NOTA: Cambia la extension py por pyw para que el cmd no se muestre al usuario