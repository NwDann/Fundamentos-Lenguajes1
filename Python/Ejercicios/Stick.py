def calcular_area_union(N, K, L):
    if K >= 2 * L:
        return N * (2 * L) ** 2
    else:
        area_cuadrado = (2 * L) ** 2
        
        area_total = 0
        for i in range(N):
            area_total += area_cuadrado
        
        return area_total - (N - 1) * (2 * L) * (K)

entrada = input()
N, K, L = map(int, entrada.split())

area = calcular_area_union(N, K, L)
print(area)
