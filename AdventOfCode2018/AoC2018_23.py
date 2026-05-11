import heapq

# --- helpers ---
def manhattan(p1, p2):
    return sum(abs(p1[i]-p2[i]) for i in range(3))

def bots_in_range(cube_min, size):
    """Count how many bots intersect this cube"""
    count = 0
    cube_max = (cube_min[0]+size-1, cube_min[1]+size-1, cube_min[2]+size-1)
    for x, y, z, r in bots:
        d = 0
        for i, val in enumerate((x,y,z)):
            if val < cube_min[i]:
                d += cube_min[i] - val
            elif val > cube_max[i]:
                d += val - cube_max[i]
        if d <= r:
            count += 1
    return count

def power_of_two(n):
    p = 1
    while p < n:
        p *= 2
    return p

# --- main ---
for file in ["AoC2018_23_test.txt","AoC2018_23_data.txt"]:
    with open(file) as f:
        lines = f.read().splitlines()

    ans = [0, 0]
    bots = []
    max_r = 0
    max_bot = (0,0,0)

    for line in lines:
        x,y,z,r = line.split(',')
        x = int(x[5:])
        y = int(y)
        z = int(z[:-1])
        r = int(r[3:])
        bots.append((x,y,z,r))
        if r > max_r:
            max_r = r
            max_bot = (x,y,z)

    # Part 1
    ans[0] = sum(1 for bot in bots if manhattan(bot,max_bot) <= max_r)

    # Part 2
    min_x = min(x for x, y, z, r in bots)
    max_x = max(x for x, y, z, r in bots)
    min_y = min(y for x, y, z, r in bots)
    max_y = max(y for x, y, z, r in bots)
    min_z = min(z for x, y, z, r in bots)
    max_z = max(z for x, y, z, r in bots)

    # Bounding cube (power of 2)
    size = power_of_two(max(max_x-min_x, max_y-min_y, max_z-min_z))
    cube_min = (min_x, min_y, min_z)

    # max-heap: (-count, -size, distance to origin, cube_min)
    heap = []
    count = bots_in_range(cube_min, size)
    heapq.heappush(heap, (-count, size, cube_min))

    best = None
    best_count = 0

    while heap:
        neg_count, size, cube_min = heapq.heappop(heap)
        count = -neg_count

        # prune: if max possible bots in this cube < best so far, skip
        if count < best_count:
            continue

        # if cube is size 1, candidate point
        if size == 1:
            x, y, z = cube_min
            d = manhattan((0,0,0), (x,y,z))
            if best is None or count > best[0] or (count == best[0] and d < best[1]):
                best = (count, d)
                best_count = count
            continue

        # subdivide cube
        half = size // 2
        for dx in [0, half]:
            for dy in [0, half]:
                for dz in [0, half]:
                    new_min = (cube_min[0]+dx, cube_min[1]+dy, cube_min[2]+dz)
                    new_count = bots_in_range(new_min, half)
                    if new_count <best_count:
                        continue
                    heapq.heappush(heap, (-new_count, half, new_min))

    ans[1] = best[1]
    print(ans)