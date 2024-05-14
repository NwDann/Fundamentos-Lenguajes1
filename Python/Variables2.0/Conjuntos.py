# SET: Funcion que crea un conjunto

conjunto = set(['dato1', 'dato2'])

# Una forma de ingresar un conjunto dentro de otro conjunto

conjunto1 = frozenset(['dato1', 'dato2'])

conjunto2 = {conjunto1, 'dato3'}


print(conjunto)

print(conjunto2)

# Teoria de conjuntos

conjunto1 = {1, 3 , 5, 7}

conjunto2 = {1, 3, 7}

   # SUBCONJUNTOS
resultado1 = conjunto2.issubset(conjunto1) #Conjunto2 es un subconjunto de Conjunto1? -> Booleano
resultado2 = conjunto1.issubset(conjunto2) #Conjunto1 es un subconjunto de Conjunto2? -> Booleano

resultado3 = conjunto2 <= conjunto1 #Conjunto2 es un subconjunto de Conjunto1? -> Booleano
resultado4 = conjunto1 <= conjunto2 #Conjunto1 es un subconjunto de Conjunto2? -> Booleano

print(resultado1)

print(resultado2)

print(resultado3)

print(resultado4)

   # SUPERCONJUNTOS
resultado1 = conjunto2.issuperset(conjunto1) #Conjunto2 es un superconjunto de Conjunto1? -> Booleano
resultado2 = conjunto1.issuperset(conjunto2) #Conjunto1 es un superconjunto de Conjunto2? -> Booleano

resultado3 = conjunto2 > conjunto1 #Conjunto2 es un superconjunto de Conjunto1? -> Booleano
resultado4 = conjunto1 > conjunto2 #Conjunto1 es un superconjunto de Conjunto2? -> Booleano

print(resultado1)

print(resultado2)

print(resultado3)

print(resultado4)

   #CONJUNTOS DISTINTOS
resultado1 = conjunto1.isdisjoint(conjunto2) #Conjunto1 y Conjunto2 no tienen ningun elemento en comun

print(resultado1)