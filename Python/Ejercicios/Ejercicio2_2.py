
# Numeros primos entre el cero y el numero que se pasa como parametro

def es_primo(num_a_comprobar):
    if num_a_comprobar < 1:
        return False
    for i in range (2, num_a_comprobar // 2 + 1):
        if (num_a_comprobar % i == 0):
            return False
    return True

def num_primos(num):
    lista = [x + 1 for x in range (1, num)]
    lista_resultante = filter(es_primo, lista)
    return lista_resultante

numero = int(input('Dame un numero: '))
print('Los numeros primos hasta el parametro dado son: ')
print(list(num_primos(numero)))