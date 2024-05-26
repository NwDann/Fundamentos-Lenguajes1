
# El parámetro "w" hace referencia al permiso de escribir. Con este permiso, si no encuentra el archivo, lo crea
with open("Python\\Archivos\\texto_aja.txt", "w", encoding = "UTF-8") as archivo:
    
    # Este comando sobreescribe el archivo
    #archivo.write("He entrado a este archivo")   
    
    # Este comando tambien sobreescribe al archivo original
    archivo.writelines(["Volvi a entrar eh \n", "Tambien hice otra linea\n"])
    # Usandolo otra vez, lo que hace es añadir en vez de sobreescribir las lineas que pasamos
    archivo.writelines(["Volvi a entrar eh asdfsad\n", "Tambien hice otra linea"])