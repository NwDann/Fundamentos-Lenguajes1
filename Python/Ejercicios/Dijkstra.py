
#----------------------------ALGORITMO------------------------------------

def find_lowest_cost_node(costs, processed):
    lowest_cost = float("inf")
    lowest_cost_node = None
    
    for node in costs:
        cost = costs[node]
        
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
            
    return lowest_cost_node

def dijkstra_algorithm(ponderated_graph, costs, parents):
    processed = []
    node = find_lowest_cost_node(costs, processed)
    
    while node is not None:
        cost = costs[node]
        neighbors = ponderated_graph[node]
        
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            
            if n not in costs or costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs, processed)
    
    return parents

def build_path(predecessors, end):
    path = [end]
    while end in predecessors:
        end = predecessors[end]
        if end is not None:
            path.append(end)
    
    path.reverse()
    return path

# ------------------------EJEMPLO--------------------------

ponderated_graph = {
    "start" : {
        "A" : 6,
        "B" : 2
    },
    "A" : {
        "end" : 1
    },
    "B" : {
        "A" : 3,
        "end" : 5
    },
    "end" : {}
}

infinity = float("inf")
costs = {
    "A" : 6,
    "B" : 2,
    "end" : infinity
}

parents = {
    "A" : "start",
    "B" : "start",
    "start" : None
}

#-------------------------------INICIO--------------------------

parents = dijkstra_algorithm(ponderated_graph, costs, parents)
print(build_path(parents, "end"))




ponderated_graph1 = {
    "S" : {
        "B" : 4,
        "C" : 8,
        "A" : 16
    },
    "B" : {
        "C" : 3
    },
    "C" : {
        "A" : 7,
        "F" : 1
    },
    "A" : {
        "D" : 2
    },
    "D" : {},
    "F" : {
        "D" : 6, 
        "A" : 5
    }
}

costs1 = {
    "S": 0,
    "A": float("inf"),
    "B": float("inf"),
    "C": float("inf"),
    "D": float("inf"),
    "F": float("inf")
}

# Inicialización de padres
parents1 = {
    "A": None,
    "B": None,
    "C": None,
    "D": None,
    "F": None,
    "S": None
}

parents1 = dijkstra_algorithm(ponderated_graph1, costs1, parents1)
print(build_path(parents1, "D"))