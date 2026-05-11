from collections import deque
DIRS = [(0,1),(1,0),(0,-1),(-1,0)]

def bfs_distances(grid, start):
    """BFS from one point, returning distances to all numbered points."""
    R, C = len(grid), len(grid[0])
    sr, sc = start
    Q = deque([(sr, sc, 0)])
    visited = {(sr, sc)}
    dists = {}

    while Q:
        r, c, d = Q.popleft()

        if grid[r][c].isdigit():
            dists[int(grid[r][c])] = d

        for dr, dc in DIRS:
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] != '#' and (nr, nc) not in visited:
                visited.add((nr, nc))
                Q.append((nr, nc, d + 1))

    return dists


def solve(grid, return_to_zero=False):
    R, C = len(grid), len(grid[0])

    # Locate numbered points
    points = {
        int(grid[r][c]): (r, c)
        for r in range(R)
        for c in range(C)
        if grid[r][c].isdigit()
    }

    labels = sorted(points.keys())
    N = len(labels)

    # Precompute pairwise distances
    dist = [[None]*N for _ in range(N)]
    for a in labels:
        dmap = bfs_distances(grid, points[a])
        for b in labels:
            dist[a][b] = dmap[b]

    # TSP-style BFS/DP
    ALL = (1 << N) - 1
    start = 0

    Q = deque([(start, 1 << start, 0)])
    seen = {}

    best = float('inf')

    while Q:
        pos, mask, cost = Q.popleft()

        if (pos, mask) in seen and seen[(pos, mask)] <= cost:
            continue
        seen[(pos, mask)] = cost

        if mask == ALL:
            if return_to_zero:
                cost += dist[pos][start]
            best = min(best, cost)
            continue

        for nxt in range(N):
            if not (mask & (1 << nxt)):
                Q.append((nxt,mask | (1 << nxt),cost + dist[pos][nxt]))

    return best

# --------- Run on inputs ---------

for file in ["AoC2016_24_test.txt", "AoC2016_24_data.txt"]:
    with open(file) as f:
        grid = f.read().splitlines()

    part1 = solve(grid, return_to_zero=False)
    part2 = solve(grid, return_to_zero=True)
    print(file, "Part 1:", part1, "Part 2:", part2)