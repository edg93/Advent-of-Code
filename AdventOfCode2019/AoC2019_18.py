from collections import deque
from heapq import heappop, heappush

def bitmask(ch):
    return 1 << (ord(ch.lower()) - ord('a'))

def bfs_dist(start_r, start_c):
    """BFS from start: returns dict of reachable keys -> (distance, required_keys_mask)"""
    visited = set()
    q = deque()
    q.append((start_r, start_c, 0, 0))  # r, c, distance, required_keys_mask
    result = {}

    while q:
        r, c, dist, req_keys = q.popleft()
        if (r, c) in visited:
            continue
        visited.add((r,c))
        cell = G[r][c]

        # if this is a key and not start
        if cell.islower() and (r,c) != (start_r,start_c):
            result[cell] = (dist, req_keys)

        for dr, dc in DIR:
            nr, nc = r + dr, c + dc
            if not (0 <= nr < R and 0 <= nc < C):
                continue
            ncell = G[nr][nc]
            if ncell == '#':
                continue
            nreq_keys = req_keys
            if ncell.isupper():
                nreq_keys |= bitmask(ncell)
            q.append((nr, nc, dist+1, nreq_keys))

    return result

def collect_all_keys(entrances, all_keys_mask):
    """
    robots_pos: tuple of starting nodes ('@' for single robot, '@0..@3' for 4 robots)
    graph: dict mapping node -> reachable keys -> (distance, required_keys_mask)
    all_keys_mask: bitmask with all keys collected
    """
    # initial robot positions
    robots = tuple(f'@{i}' for i in range(len(entrances)))

    # build graph: node -> reachable key -> (distance, required_keys_mask)
    nodes = dict(keys)
    for i, r in enumerate(robots):
        if r[0]=='@':
            nodes[r] = entrances[i]  # use correct entrances
    graph = {}
    for node, (r,c) in nodes.items():
        graph[node] = bfs_dist(r,c)
    
    heap = []
    heappush(heap, (0, robots, 0))  # steps, robot_positions, keys_mask
    visited = {}

    while heap:
        steps, robots, keys_mask = heappop(heap)
        state = (robots, keys_mask)
        if keys_mask == all_keys_mask:
            return steps
        if state in visited and visited[state] <= steps:
            continue
        visited[state] = steps

        for i, robot in enumerate(robots):
            for key, (dist, req_keys) in graph[robot].items():
                if key[0] == '@':
                    continue
                bit = bitmask(key)
                if keys_mask & bit:
                    continue
                if req_keys & ~keys_mask:
                    continue
                new_robots = list(robots)
                new_robots[i] = key
                new_state = (tuple(new_robots), keys_mask | bit)
                heappush(heap, (steps + dist, new_state[0], new_state[1]))


with open("AoC2019_18_data.txt", "r") as f:
    data = f.read()
    
data = data.splitlines()
ans = [0,0]

DIR = ((1,0),(-1,0),(0,1),(0,-1))
R,C = len(data),len(data[0])
G = [[data[r][c] for c in range(C)] for r in range(R)]

keys = {}
doors = {}
for r in range(R):
    for c in range(C):
        cell = G[r][c]
        if cell.islower():
            keys[cell] = (r,c)
        elif cell.isupper():
            doors[cell] = (r,c)
        elif cell=='@':
            er,ec = r,c

all_keys_mask = sum(bitmask(key) for key in keys)

#PART 1
entrances = [(er,ec)]
ans[0] = collect_all_keys(entrances, all_keys_mask)

#PART 2
for dr in (-1,0,1):
    for dc in (-1,0,1):
        G[er+dr][ec+dc] = '#'

entrances = [
    (er-1, ec-1),  # top-left
    (er-1, ec+1),  # top-right
    (er+1, ec-1),  # bottom-left
    (er+1, ec+1),  # bottom-right
]
for r,c in entrances:
    G[r][c] = '.'

ans[1] = collect_all_keys(entrances, all_keys_mask)
print(ans)