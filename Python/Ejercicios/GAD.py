def topological_sort(grafo):
    top_sorted = []
    ready = []
    incount = {}

    for nodo in grafo.keys():  # por cada nodo que pertenece al grafo
        incount[nodo] = indegree(grafo, nodo)  # extraer el indegree del nodo (num de predecesores)
        print("Indegree de",nodo,"es",incount[nodo])
        if incount[nodo] == 0:  # nodo sin predecesores puede usarse
            ready.append(nodo)
    print('Indegree:', incount)
    print('READY:', ready)

    while len(ready) > 0:  # mientras haya nodos listos para ordenarse
        nodo = ready.pop()
        print('Nodo para usarse', nodo)
        top_sorted.append(nodo)  # nodo es insertado en orden topológico
        for vecino in grafo[nodo]:
            print(vecino, ':', incount[vecino], '- 1')
            incount[vecino] -= 1  # queda 1 predecesor menos
            if incount[vecino] == 0:
                ready.append(vecino)
        print('READY:', ready)
    return top_sorted

def indegree(grafo,nodo):
    c=0
    for i in grafo:
        if nodo in grafo[i]:
            c=c+1
    return c 

grafo={ 
    "A":["C"],
    "B":["C","D"],
    "C":["D"],
    "D":["E"],
    "E":[]
} 
print("El orden topologico es:",topological_sort(grafo))