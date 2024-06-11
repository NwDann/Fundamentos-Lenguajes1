
from scipy.interpolate import lagrange
import numpy as np
import matplotlib.pyplot as plt
x = [-30, -16, -7, 6, 20]
y = [17, 15, 10, 7,12]

polynomial = lagrange(x, y)

print(polynomial)
x_values = np.linspace(min(x), max(x), 100)
y_values = polynomial(x_values)

plt.scatter(x, y, color='red', label='Datos Originales')

plt.plot(x_values, y_values, label='Polinomio Interpolado')

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Interpolación de Lagrange')
plt.legend()

plt.grid(True)
plt.show()



