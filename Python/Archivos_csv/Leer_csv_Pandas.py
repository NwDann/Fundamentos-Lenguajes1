
import pandas as pd
#                                                              Cambia el nombre de las primeras filas
df = pd.read_csv("Python\\Archivos_csv\\texto_csv.csv", names = ["Name", "LastName", "Age"])
# DataFrame : Archivos multidimensionales similares a las hojas de calculo

# Imprime todos los datos
print(df)

# Obtencion de los datos de la columna Nombre
print(df["Name"])

cadena = "0123456789"
