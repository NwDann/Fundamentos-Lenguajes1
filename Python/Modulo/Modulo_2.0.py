
#Importar un modulo dentro de nuestra carpeta

#     import Funciones_ejemplo.Saludar as m_saludar

#Importar modulos fuera de nuestra carpeta origen

import sys

print(sys.builtin_module_names) # Modulos nativos de python

print(sys.path) # Rutas, nos fijamos en la de nuestro interes

sys.path.append('c:\\Users\\Hp\\Documents\\GitHub\\Fundamentos-Lenguajes1\\Python\\Funciones_ejemplo')

import Saludar as saludo

print(saludo.saludar('Danny'))