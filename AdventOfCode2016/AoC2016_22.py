from collections import deque
with open("AoC2016_22_data.txt", "r") as f:
    data = f.read()
data = data.splitlines()[2:]
ans = [0,0]

nodes = {}
DIR = ((0,1),(0,-1),(1,0),(-1,0))

for line in data:
    file,size,used,avail,_ = line.split()
    size,used,avail = int(size[:-1]),int(used[:-1]),int(avail[:-1])
    _,x,y = file.split('-')
    x,y = int(x[1:]),int(y[1:])
    nodes[(x,y)]=(size,used,avail)
    
for node,(_,used,_) in nodes.items():
    for node1,(_,_,avail) in nodes.items():
        if used==0 or node1==node:
            continue
        if used<=avail:
            ans[0]+=1
print(ans)

max_x = max(x for x, y in nodes.keys())
max_y = max(y for x, y in nodes.keys())

# Find empty node
for (x, y), (size, used, avail) in nodes.items():
    if used == 0:
        empty_node = (x, y)
        break

# Walls: any node that cannot accept any other data
empty_size = nodes[empty_node][0]
walls = { (x, y) for (x, y), (size, used, avail) in nodes.items() if used > empty_size }

# --- BFS to move empty node next to goal ---
goal = (max_x, 0)
target = (0, 0)
directions = [(0,1),(0,-1),(1,0),(-1,0)]

def bfs(start, blocked):
    """Return shortest distance from start to every reachable point avoiding blocked."""
    queue = deque([(start, 0)])
    visited = {start}
    dist_map = {start:0}
    while queue:
        (x, y), d = queue.popleft()
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if 0 <= nx <= max_x and 0 <= ny <= max_y and (nx, ny) not in visited and (nx, ny) not in blocked:
                visited.add((nx, ny))
                dist_map[(nx, ny)] = d+1
                queue.append(((nx, ny), d+1))
    return dist_map

# Find empty node distance to each adjacent of goal
adj_to_goal = [(goal[0]+dx, goal[1]+dy) for dx, dy in directions
               if 0 <= goal[0]+dx <= max_x and 0 <= goal[1]+dy <= max_y and (goal[0]+dx, goal[1]+dy) not in walls]

dist_map = bfs(empty_node, walls)
# Minimum moves to get empty node next to goal
min_empty_moves = min(dist_map[pos] for pos in adj_to_goal)

# Each move of goal left costs 5 steps (empty goes around)
goal_moves_needed = goal[0]  # distance from goal.x to 0
total_moves = min_empty_moves + 5 * (goal_moves_needed - 1) + 1  # +1 for final move into target

print("Part 2 answer:", total_moves)