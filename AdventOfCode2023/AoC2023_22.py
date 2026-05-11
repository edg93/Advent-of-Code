from collections import defaultdict,deque

def count_fall(start):
    fallen = {start}
    Q = deque([start])
    while Q:
        b = Q.popleft()
        for above in supports[b]:
            if above in fallen:
                continue
            # Check if all supports of above are gone
            if all(s in fallen for s in supported_by[above]):
                fallen.add(above)
                Q.append(above)
    
    return len(fallen)-1

def overlap_xy(a, b):
    return not (
        a[3] < b[0] or b[3] < a[0] or
        a[4] < b[1] or b[4] < a[1]
    )

with open("AoC2023_22_data.txt", "r") as file:
    data = file.read()

data = data.splitlines()
ans = [0,0]

bricks = []
for line in data:
    p1,p2 = line.split('~')
    x1,y1,z1 =  [int(x) for x in p1.split(',')]
    x2,y2,z2 = [int(x) for x in p2.split(',')]
    brick = (
        min(x1, x2), min(y1, y2), min(z1, z2),
        max(x1, x2), max(y1, y2), max(z1, z2),
    )
    bricks.append(brick)

bricks.sort(key=lambda b: b[2])  # sort by z1

settled = []
for brick in bricks:
    x1, y1, z1, x2, y2, z2 = brick
    height = z2 - z1

    support_z = 0
    for other in settled:
        if overlap_xy(brick, other):
            support_z = max(support_z, other[5])

    new_brick = (
        x1, y1, support_z + 1,
        x2, y2, support_z + 1 + height
    )
    settled.append(new_brick)

supports = defaultdict(set)
supported_by = defaultdict(set)

for i, a in enumerate(settled):
    for j, b in enumerate(settled):
        if i == j:
            continue
        if a[5] + 1 == b[2] and overlap_xy(a, b):
            supports[i].add(j)
            supported_by[j].add(i)
            
for i in range(len(settled)):
    if all(len(supported_by[j]) > 1 for j in supports[i]):
        ans[0] += 1
        
for i in range(len(settled)):
    ans[1] += count_fall(i)
    
print(ans)