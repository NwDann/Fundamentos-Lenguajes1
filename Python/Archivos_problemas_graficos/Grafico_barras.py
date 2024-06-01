
import pandas as pd
import matplotlib.pyplot as plt # Visualizacion de datos graficamente
import seaborn as sns # Creacion de graficos estadisticos

df = pd.read_csv("Python\\Archivos_problemas_graficos\\Ingresos.csv")

sns.barplot(x = "Fuente", y = "Ingresos", data = df)

# Obtencion del total de ingresos
total_ingresos = df["Ingresos"].sum()
print(total_ingresos)

plt.show()