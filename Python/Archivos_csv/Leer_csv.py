
import csv

with open("Python\\Archivos_csv\\texto_csv.csv") as archivo:
    print("Se pudo leer")
    
    resultado = csv.reader(archivo)
    
    for fila in resultado:
        print(fila)