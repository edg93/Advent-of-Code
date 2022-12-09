"Day 12 of AOC2021"
from collections import deque

with open("data.txt", "r") as file:
    data = file.read()
data = data.split('\n')
links = {}
for line in data:
    a,b=line.split('-')
    if b != 'start':
        if a not in links:
            links[a]=[b]
        else:
            links[a]+=[b]
    if a != 'start':
        if b not in links:
            links[b]=[a]
        else:
            links[b]+=[a]

queue = deque([('start',set())])
sol1 = 0 

while len(queue)>0:
    state,visited = queue.popleft()
    if state == 'end':
        sol1 += 1
        continue
    for new_state in links[state]:
        if new_state not in visited:
            new_visited = set(visited)
            if new_state.islower():
                new_visited.add(new_state)
            queue.append((new_state,new_visited))

print(sol1)

queue = deque([('start',set(),None)])
sol2 = 0

while len(queue)>0:
    state,visited,twice = queue.popleft()
    if state == 'end':
        sol2 += 1
        continue
    for new_state in links[state]:
        if new_state not in visited:
            new_visited = set(visited)
            if new_state.islower():
                new_visited.add(new_state)
            queue.append((new_state,new_visited,twice))
        elif new_state in visited and twice is None and new_state not in ['start','end']:
            queue.append((new_state,visited,new_state))

print(sol2)