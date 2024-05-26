# Cambiar el tipo de dato de una columna
import pandas as pd

df = pd.read_csv("Python\\Archivos_problemas\\texto_csv.csv", names = ["Nombre", "Apellido", "Edad"])

#Convertir la edad dada en el tipo string
df["Edad"] = df["Edad"].astype(str)

# Dira que ahora es un string
#print(type(df["Edad"][0]))

# Reemplazo datos de nombre, especificamente a "Ronny" por "Tonto" en el mismo df
df["Nombre"] = df["Nombre"].replace("Ronny", "Tonto") # Puedes añadir "inplace = True" para que los cambios se apliquen directamente
print(df)

# DROPNA(): Elimina las filas que lee con datos faltantes
df = df.dropna() #si enviamos como parametro "axis = 1", eliminara las columnas con datos varios
print(df)

#DROP_DUPLICATES(): Elimina las filas repetidas
df = df.drop_duplicates()
print(df)

# To_csv(): Crea un dataframe con el resultante del programa (limpio)
df.to_csv("Python\\Archivos_problemas\\texto_csv_limpio.csv")