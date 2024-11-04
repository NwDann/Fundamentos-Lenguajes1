
def comp_y_contar_areas(L, N, M, rayos_A, rayos_B):
    # Conjuntos para almacenar posiciones únicas de rayos en cada dirección
    arribaA = list()
    derechaA = list()
    arribaB = list()
    izquierdaB = list()
    
    # Procesar rayos del láser A
    for tipo, coord in rayos_A:
        if tipo == 'U':
            arribaA.add(coord)  # Coordenadas que intersectan la parte superior
        elif tipo == 'R':
            derechaA.add(coord)    # Coordenadas que intersectan la derecha
    
    # Procesar rayos del láser B
    for tipo, coord in rayos_B:
        if tipo == 'U':
            arribaB.add(coord)  # Coordenadas que intersectan la parte superior
        elif tipo == 'L':
            izquierdaB.add(coord)    # Coordenadas que intersectan la izquierda
    
    total_areas = (len(arribaA) + len(derechaA) + 1) * len(izquierdaB)
    arribaB.sort()
    arribaA.sort()
    for i in arribaB:
        cont = 0
        for j in arribaA:
            if(i > j):
                cont += 1
            else:
                break
        if cont == 0:
            total_areas += len(arribaA) + len(derechaA) + 1
        else:
            
            total_areas += len(arribaA) + len(derechaA) + cont + 1
    return total_areas

L, N, M = map(int, input().split())
lucesA = []
lucesB = []

for _ in range(N):
    lugar, distancia = input().split()
    lucesA.append((lugar, int(distancia)))

for _ in range(M):
    lugar, distancia = input().split()
    lucesB.append((lugar, int(distancia)))

print(comp_y_contar_areas(L, N, M, lucesA, lucesB)) 
