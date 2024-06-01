
import pandas as pd
import matplotlib.pyplot as plt # Visualizacion de datos graficamente
import seaborn as sns # Creacion de graficos estadisticos

df = pd.read_csv("Python\\Archivos_problemas_graficos\\Dinero.csv")

sns.scatterplot(x = "Tiempo", y = "Dinero", data = df)

plt.show()