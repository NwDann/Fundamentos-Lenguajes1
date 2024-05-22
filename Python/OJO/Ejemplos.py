
import numpy as np
import matplotlib.pyplot as plt
import math

X = np.linspace(-10, 10, 100)

Y = [(lambda x : math.sin(x))(x) for x in X]
plt.plot(X, Y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Grafica de la ecuacion $y = \sin{x}$')
ax = plt.gca()
ax.set_ylim([-1.5, 1.5])
ax.set_xlim([-10, 10])
plt.grid(True)
plt.show()



from typing import Callable

def sign(x: float) -> int:
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0

def bisection(
a: float, b: float, *, equation: Callable[[float], float], tol: float, N: int
) -> tuple[float, int] | None:
    i = 1
    assert a < b, "a not lower than b, the interval is not valid."
    assert (
        equation(a) * equation(b) < 0
    ), "The function does not change sign over the interval."
    
    Fa = equation(a)
    p = a
    for i in range(N):
        p = a + (b - a) / 2
        FP = equation(p)
        if FP == 0 or (b - a) / 2 < tol:
            return p, i
        if sign(Fa) * sign(FP) > 0:
            a = p
            Fa = FP
        else:
            b = p
    return p, i

def newton_raphson(aproximation : float, tol : float, N : int, equation : Callable[[float], float],
                   derivate : Callable[[float], float]) -> tuple[float, int] | None:
    i = 1
    p0 = aproximation
    p = 0
    for i in range(N):
        p = p0 - equation(p0) / derivate(p0)
        if abs(p - p0) < tol:
            return p, i
        i = i + 1
        p0 = p
    return None
    