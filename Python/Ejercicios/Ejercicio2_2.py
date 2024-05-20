
# Numeros primos entre el cero y el numero que se pasa como parametro

def es_primo(num_a_comprobar):
    if num_a_comprobar < 1:
        return False
    for i in range (2, num_a_comprobar // 2):
        if (num_a_comprobar % i == 0):
            return False
    return True

def num_primos(num):
    return [x + 1 for x in range (1, num) if es_primo(x + 1)]

numero = int(input('Dame un numero: '))
print('Los numeros primos hasta el parametro dado son: ')
print(num_primos(numero))