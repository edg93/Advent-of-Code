from  collections import deque
with open("AoC2015_09_data.txt", "r") as file:
     data = file.read()
    
data = data.split('\n')

ans = [10e9,0]

locations = set()
connections = {}

for line in data:
    a,_,b,_,distance = line.split()
    locations.add(a)
    locations.add(b)
    distance = int(distance)
    if a in connections:
        connections[a].append((b,distance))
    else:
        connections[a] = [(b,distance)]
    if b in connections:
        connections[b].append((a,distance))
    else:
        connections[b] = [(a,distance)]
    
for start in locations:
    Q = deque([])
    Q.append((start,0,{start}))
    while Q:
        pos,distance,visited = Q.popleft()
        
        if len(visited)==len(locations):
            ans[0]=min(ans[0],distance)
            ans[1]=max(ans[1],distance)
            continue
        else:
            for city,d in connections[pos]:
                if city in visited:
                    continue
                Q.append((city,distance+d,visited|{city}))

    
    
print(ans)