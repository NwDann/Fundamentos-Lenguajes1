
def DFS(start, graph, searched, componentR):
    componentR.append(start)
    searched[start] = True
    print(searched)
    print(f"Vecinos de {start} : {graph[start]}")
    
    for neighbor in graph[start]:
        if not searched[neighbor]:
            DFS(neighbor, graph, searched, componentR)
            print(f"Final de una rama en {neighbor}")
            print(f"Vuelve a {start}")
            print()
    return componentR

graph = {
    0: [],
    1: [2, 3],
    2: [1, 3, 4, 5],
    3: [1, 2, 5, 7, 8],
    4: [2, 5],
    5: [2, 3, 4, 6],
    6: [5],
    7: [3, 8],
    8: [3, 7]
}


componentR = DFS(1, graph, [False] * len(graph), [])

print(f"Busqueda DFS dio como resultado : {componentR}")

graph2 = {
    "start" : ["F", "A", "B"],
    "A" : ["E", "B"],
    "B" : ["D", "C"],
    "C" : ["D"],
    "D" : [],
    "E" : ["D"],
    "F" : []
}

componentR = DFS("start", graph2, {key : False for key in graph2.keys()}, [])

print(f"Busqueda DFS dio como resultado : {componentR}")
