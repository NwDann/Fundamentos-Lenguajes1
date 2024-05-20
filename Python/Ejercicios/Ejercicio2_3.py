# Fibonacci
# 0, 1, 1, 2, 3, 5, 8, 13, 21

def fibonnaci(limite : int):
    a, b, i = 0, 1, 1
    resultado = [0]
    while limite >= a + b:
        resultado.append(a + b)
        b = a
        a = resultado[i]
        i += 1
    return resultado

limite = int(input('Dame el limite de la sucesion: '))
print(fibonnaci(limite))
        