from collections import deque
from IntcodeComputer import computer
with open("AoC2019_15_data.txt", "r") as file:
    data = file.read()
    
data = [int(x) for x in data.split(',')]
d = {}
ans = [None,0]
for n,i in enumerate(data):
    d[n]=i
    
x,y = 0,0

DIR = {1:(0,1),2:(0,-1),3:(-1,0),4:(1,0)}

Q = deque([(0, 0, 0, d, 0, 0)]) #x,y,steps,d,idx,base

visited = set()
maze = {} # values: 0 = wall, 1 = empty, 2 = oxygen
maze[(0, 0)] = 1
while Q:
    x,y,steps,d,idx,base = Q.popleft()
    if (x,y) in visited:
        continue
    visited.add((x,y))
    for inp in [1,2,3,4]:
        new_d = d.copy()
        new_d,new_idx,new_base,response = computer(new_d,[inp],idx,base)
        dx,dy = DIR[inp]
        nx, ny = x + dx, y + dy
        if response == 2:
            maze[(nx, ny)] = 2
            oxygen_pos = (nx, ny)
            ans[0] = steps+1
        elif response == 1:
            maze[(nx, ny)] = 1
            Q.append((nx,ny,steps+1,new_d,new_idx,new_base))
        elif response == 0:
            maze[(nx, ny)] = 0  # wall
        
Q = deque([(oxygen_pos[0], oxygen_pos[1], 0)])
visited = {oxygen_pos}
max_minutes = 0

while Q:
    x, y, minutes = Q.popleft()
    max_minutes = max(max_minutes, minutes)
    for dx, dy in DIR.values():
        nx, ny = x + dx, y + dy
        if (nx, ny) not in visited and maze.get((nx, ny)) == 1:
            visited.add((nx, ny))
            Q.append((nx, ny, minutes + 1))
            
ans[1] = max_minutes
print(ans)