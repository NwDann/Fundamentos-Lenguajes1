
import matplotlib.pyplot as plt
import numpy as np
from typing import Callable
import sympy as sym
from IPython.display import display

def taylor_approx(fcn: Callable[[float], float], x0: float, n: int) -> sym.Symbol:
    x = sym.symbols("x")
    f = sym.sympify(fcn(x))
    taylor: sym.Symbol = 0
    for i in range(n + 1):
        term = f.diff(x, i).subs(x, x0) / sym.factorial(i) * (x - x0) ** i
        taylor += term
    return taylor

def plot_taylor_approx(fcn: Callable[[float], float], x0: float, max_n: int, x_range: tuple):
    x = sym.symbols("x")
    x_vals = np.linspace(x_range[0], x_range[1], 1000)
    
    original_fcn = sym.lambdify(x, fcn(x), "numpy")
    y_vals = original_fcn(x_vals)
    plt.plot(x_vals, y_vals, label=f"Funcion original", color='black')
    
    for n in range(1, max_n + 1):
        taylor_poly = taylor_approx(fcn, x0, n)
        taylor_fcn = sym.lambdify(x, taylor_poly, "numpy")
        taylor_y_vals = taylor_fcn(x_vals)
        plt.plot(x_vals, taylor_y_vals, label=f"Polinomio de taylor de orden n={n}")
    
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Taylor")
    plt.legend()
    plt.grid(True)
    plt.show()

fcn = lambda x: sym.exp(x)  # Funcion inicial

plot_taylor_approx(fcn, 0, 5, (-2, 2))




