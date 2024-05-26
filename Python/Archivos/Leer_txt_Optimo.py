
# WITH nos trae menos errores de excepciones, se asigna a archivo
with open("Python\\Archivos\\texto_aja.txt", encoding = "UTF-8") as archivo:
    print('Hola') # Este mensaje aparecera solo si el archivo se pudo abrir
    print(archivo.read())
    
# No es necesario cerrarlo al usar WITH OPEN