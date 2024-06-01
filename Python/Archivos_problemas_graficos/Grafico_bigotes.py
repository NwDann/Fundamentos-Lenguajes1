
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Python\\Archivos_problemas_graficos\\Bigotes.csv")

sns.boxplot(x = "Categoria", y = "Valor", data = df)

plt.show()