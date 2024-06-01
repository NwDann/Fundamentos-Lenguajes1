
import pandas as pd
import matplotlib.pyplot as plt # Visualizacion de datos graficamente
import seaborn as sns # Creacion de graficos estadisticos

df = pd.read_csv("Python\\Archivos_problemas_graficos\\Mandarinas.csv")

sns.lineplot(x = "Fecha", y = "Mandarinas", data = df)

plt.plot("01-08", 8, "o") # Punto en donde se comieron mas mandarinas

plt.show()