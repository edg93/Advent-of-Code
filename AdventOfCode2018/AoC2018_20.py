from collections import defaultdict,deque

with open("AoC2018_20_data.txt", "r") as f:
    data = f.read()
    
ans = [0,0]

#data = '^ESSWWN(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))$'

data = data[1:-1]

DIR = {'N':(0,1),'S':(0,-1),'E':(1,0),'W':(-1,0)}
rooms = defaultdict(set)
positions = {(0,0)}
stack = []

for ch in data:
    if ch in DIR:
        dx, dy = DIR[ch]
        new_positions = set()
        for x, y in positions:
            nx, ny = x + dx, y + dy
            rooms[(x,y)].add((nx,ny))
            rooms[(nx,ny)].add((x,y))
            new_positions.add((nx,ny))
        positions = new_positions

    elif ch == '(':
        stack.append((positions.copy(), set()))

    elif ch == '|':
        start,collected = stack[-1]
        collected |= positions
        positions = start.copy()
        stack[-1] = (start, collected)

    elif ch == ')':
        _, collected = stack.pop()
        positions |= collected
                
def print_grid(rooms, start=(0, 0)):
    xs = [x for x, y in rooms]
    ys = [y for x, y in rooms]

    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)

    # Grid dimensions (rooms + walls)
    width = (max_x - min_x + 1) * 2 + 1
    height = (max_y - min_y + 1) * 2 + 1

    grid = [['#'] * width for _ in range(height)]

    def gx(x): return (x - min_x) * 2 + 1
    def gy(y): return (max_y - y) * 2 + 1

    for (x, y), neighbors in rooms.items():
        cx, cy = gx(x), gy(y)

        grid[cy][cx] = 'X' if (x, y) == start else '.'

        for nx, ny in neighbors:
            dx, dy = nx - x, ny - y
            if dx == 1:
                grid[cy][cx + 1] = '|'
            elif dx == -1:
                grid[cy][cx - 1] = '|'
            elif dy == 1:
                grid[cy - 1][cx] = '-'
            elif dy == -1:
                grid[cy + 1][cx] = '-'

    for row in grid:
        print(''.join(row))
        
#print_grid(rooms)

Q = deque([(0,0,0)])  # x, y, steps
visited = {(0,0): 0}

while Q:
    x, y, steps = Q.popleft()
    ans[0] = max(ans[0],steps)
    for nx, ny in rooms[(x,y)]:
        if (nx,ny) not in visited:
            visited[(nx,ny)] = steps + 1
            Q.append((nx,ny,steps+1))

for v in visited.values():
    if v>=1000:
        ans[1]+=1

print(ans)