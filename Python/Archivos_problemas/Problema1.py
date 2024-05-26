# 2 listas, una con nombres y otra con apellidos

nombres = ['Danny', 'Kenny', 'Mandy', 'Ronny']
apellidos = ['I', 'Mr', 'Olmedo', 'Alcar']

with open("Python\\Archivos_problemas\\problema1.txt", "a", encoding = "UTF-8") as archivo:
    archivo.writelines([(f"{nombre},{apellido}\n") for nombre, apellido in zip(nombres, apellidos)])
