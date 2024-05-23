
from collections import deque

def build_graph(original_graph, start):
    marked = [False] * len(original_graph)
    search_queue = deque([start])
    marked[0] = True
    result = [-1]* len(original_graph)
    
    while search_queue:
        item = search_queue.popleft()
        
        for i in original_graph[item]:
            if not marked[i]:
                marked[i] = True
                result[i] = item
                search_queue.append(i)

    return result

graph = [[1, 2, 5], [0, 2], [0, 1, 3, 4], [2, 4, 5], [2, 3], [0, 3]]

result = build_graph(graph, 0)
print(result)
