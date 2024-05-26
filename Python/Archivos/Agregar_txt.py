
# El parámetro "a" hace referencia al permiso de agregar al archivo.
with open("Python\\Archivos\\texto_aja.txt", "a", encoding = "UTF-8") as archivo:
    
    # Este comando ya no sobreescribe el archivo debido al permiso, si no, lo agrega
    archivo.write("He entrado a este archivo")
    
    # Este bucle agrega varias lineas
    archivo.writelines([(f'\nLinea {i + 1} agregada') for i in range(5)])