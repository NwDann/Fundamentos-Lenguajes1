
from collections import deque

def person_is_seller(person : str) -> bool:
    return person == "Peggy"

def search(name : str) -> bool:
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(f"{person} is a mango seller!")
                return True
            
            else:
                search_queue += graph[person]
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

ojo =search('You')

if not ojo:
    print('Mango seller is not inside our graph')

