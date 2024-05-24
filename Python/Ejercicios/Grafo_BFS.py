
from collections import deque
from typing import Callable

def person_is_seller(person : str) -> bool:
    return person == "Peggy"


def build_path(predecesors : dict, goal, start):
    path = [goal]
    
    while goal in predecesors:
        goal = predecesors[goal]
        path.append(goal)
    
    path.append(start)
    path.reverse()
    return path


def search(start, graph, funtion : Callable) -> bool | list:
    search_queue = deque(graph[start])
    searched = []
    predecesors = {}
    
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                return funtion(predecesors, person, start)
            
            else:
                for neighbor in graph[person]:
                    if neighbor not in searched and neighbor not in predecesors:
                        search_queue.append(neighbor)
                        predecesors[neighbor] = person
                searched.append(person)
                
    return False

# Inicio

graph = {
    'You' : ['Bob', 'Claire', 'Alice'],
    'Bob' : ['Anuj', 'Peggy'],
    'Alice' : ['Peggy'],
    'Claire' : ['Thom', 'Jonny'],
    'Anuj' : [],
    'Peggy' : [],
    'Jonny' : [],
    'Thom' : []
}

ojo = search('You', graph)

if not ojo:
    print('Mango seller is not inside our graph')
else:
    print(f"Path from you to mango seller: {ojo}")

