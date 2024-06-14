
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
    0: [1, 5],
    1: [5],
    2: [0, 3, 4],
    3: [4, 7],
    4: [6],
    5: [2, 4],
    6: [3, 7],
    7: []
}


componentR = DFS(0, graph, [False] * len(graph), [])

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
