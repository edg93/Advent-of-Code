from collections import deque
from itertools import combinations

items = ((1,2),(1,2),(1,1),(1,1),(1,1))
ans = [10e9,0]

def valid(items):
    for floor in [1,2,3,4]:
        generators = set([x for x in range(len(items)) if items[x][0]==floor])
        chips = set([x for x in range(len(items)) if items[x][1]==floor])
        
        if generators:
            for chip in chips:
                if chip not in generators:
                    return False
                
    return True
        

def generate_moves(items,elevator): #To be completed
    states = []
    
    # list movable objects on current floor
    movable = []
    for i, (g, c) in enumerate(items):
        if g == elevator:
            movable.append(("g", i))
        if c == elevator:
            movable.append(("c", i))
            
    # elevator directions
    for direction in (-1, 1):
        new_floor = elevator + direction
        if not (1 <= new_floor <= 4):
            continue
        
        # prune downward moves if nothing below
        if direction == -1:
            if all(g >= elevator and c >= elevator for g,c in items):
                continue

        # choose 1 or 2 objects to move
        for k in [1,2]:
            for moved in combinations(movable, k):
                new_items = list(items)
    
                for kind, idx in moved:
                    g, c = new_items[idx]
                    if kind == "g":
                        new_items[idx] = (new_floor, c)
                    else:
                        new_items[idx] = (g, new_floor)
    
                states.append((tuple(new_items), new_floor))
    
    return states
        
def solve(items):
    Q = deque([(items,1,0)])
    visited = set()
    
    while Q:
        items,elevator,steps = Q.popleft()
        key = (elevator, tuple(sorted(items)))
        
        if key in visited:
            continue
        visited.add(key)
        if all(g == 4 and c == 4 for g, c in items):
            return steps
        
        states = generate_moves(items,elevator)
        
        for new_items,new_elevator in states:
            if valid(new_items):
                Q.append((new_items, new_elevator, steps + 1))

ans[0] = solve(items)
items = ((1,2),(1,2),(1,1),(1,1),(1,1),(1,1),(1,1))
ans[1] = solve(items)

print(ans)

