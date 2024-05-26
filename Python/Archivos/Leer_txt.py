
#                                                 Este apartado es para leer cualquier caracter
archivo = open("Python\\Archivos\\texto_aja.txt", encoding = "UTF-8")

# Es necesaria la funcion read, lectura de archivo completo. Una vez leido, no se puede leer mas
#resultado = archivo.read()

# Para leer varias lineas representadas en una lista, hay que usarla cuidadosamente por RAM
#resultado = archivo.readlines()

# Para leer una sola linea
resultado = archivo.readline(3) # El parametro determina el numero de caracteres a leer

# Se debe cerrar el archivo
archivo.close()

print(resultado)

