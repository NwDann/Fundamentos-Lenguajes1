
import pandas as pd
#                                                              Cambia el nombre de las primeras filas
df = pd.read_csv("Python\\Archivos_csv\\texto_csv.csv", names = ["Name", "LastName", "Age"])
df2 = pd.read_csv("Python\\Archivos_csv\\texto_csv.csv", names = ["Name", "LastName", "Age"])

# DataFrame : Archivos multidimensionales similares a las hojas de calculo

# Imprime todos los datos
#print(df)

# Obtencion de los datos de la columna Nombre
nombres = df["Name"]

#cadena = "0123456789"
# Tecnica slicing con :
#print(cadena[3:4])

# Ordenar el dataframe por la edad ascendentemente
df_sorted = df.sort_values(by = "Age")
#print(df_sorted)

# Ordenar el dataframe por la edad de forma descendente
df_sorted = df.sort_values(by = "Age", ascending = False)
#print(df_sorted)

# Concatenar dos dataframes
df_concatenado = pd.concat([df, df2])
#print(df_concatenado)

# Acceso a las primeras 2 filas con head()
primer_fila = df.head(2)
print(primer_fila)

# Acceso a las ultimas 2 filas con tail()
ultimas_filas = df.tail(2)
print(ultimas_filas)

# Acceso a la cantidad de filas y columnas con shape
filas, columnas = df.shape
print(f"Numero de filas: {filas} y numero de columnas: {columnas}")

# Datos estadisticos del dataframe
info = df.describe()
#print(info)

# Acceso a un elemento especifico con loc (edad de la fila 2)
elemento = df.loc[2, "Age"]
#print(elemento)

# Acceso a un elemento especifico con iloc, esta vez con indices (edad de la fila 2)
elemento = df.iloc[2, 2]
#print(elemento)

# Acceso a todas las filas de una columna
apellidos = df.iloc[:, 1] #[todas las filas, de la columna apellido]
#print(apellidos)

# Acceso a todas las columnas de una fila
fila3 = df.iloc[2, :] #[de la fila 3, todas las columnas]
#print(fila3)

# Acceso a filas con edad mayor que 30
mayor_30 = df.loc[df["Age"] <= 30, :]
print(mayor_30)