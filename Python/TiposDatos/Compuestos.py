# Datos que tienen mas datos dentro de si

# [] LISTA

lista = ["Danny", "I", True, 1.73]
print(lista)
print(lista[0])
print(lista[1])

# () TUPLA: NO SE PUEDEN MODIFICAR SUS ELEMENTOS, PERO SE PUEDE REDEFINIR

tupla = ("Danny", "I", True, 1.73)
print(tupla[0])
tupla = ("HOLAAAAAAAAAAAA")
#tupla[0] = "HELLO"  esto esta mal

# {} SET O CONJUNTO: NO TIENEN UN ORDEN FIJO, NO SE PUEDEN MODIFICAR SUS ELEMENTOS, PERO SE PUEDE REDEFINIR

conjunto = {"Danny", "I", True, 1.73}
conjunto = {"HOLAAAAAAAAAAA"}
#conjunto[0] = "HELLO"  Esto esta mal
#print(conjunto[1])  No puedo imprimir elementos del conjunto
print(conjunto)
conjunto = {"Danny", "I", True, 1.73, "Danny"}
print(conjunto) #Los elementos repetidos no se almacenan

# {} DICCIONARIO (CLAVE : VALOR)

diccionario = {
    'nombre' : "Danny",
    'Apellido' : "I",
    'Esta bien' : True,
    'duplicado' : "Danny"
    
}

print(diccionario['nombre'])