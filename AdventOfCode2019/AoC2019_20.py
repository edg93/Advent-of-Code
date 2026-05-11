from collections import deque,defaultdict
with open("AoC2019_20_data.txt", "r") as f:
    data = f.read()
    
data = data.splitlines()
ans = [0,0]
DIR = ((1,0),(-1,0),(0,1),(0,-1))
R,C = len(data),len(data[0])
portals = defaultdict(list)


for r in range(R):
    for c in range(C):
        ch = data[r][c]
        if not ch.isupper():
            continue
    
        # --- Horizontal label ---
        if c + 1 < C and data[r][c + 1].isupper():
            label = ch + data[r][c+1]
    
            # Check left or right for walkable tile
            if c - 1 >= 0 and data[r][c - 1] == '.':
                pos = (r,c - 1)
            elif c + 2 < C and data[r][c + 2] == '.':
                pos = (r,c + 2)
            else:
                pos = None
    
            if pos:
                if label == "AA":
                    start = pos
                elif label == "ZZ":
                    end = pos
                else:
                    portals[label].append(pos)
    
        # --- Vertical label ---
        if r + 1 < R and data[r+1][c].isupper():
            label = ch + data[r+1][c]
    
            # Check above or below for walkable tile
            if r - 1 >= 0 and data[r-1][c] == '.':
                pos = (r-1,c)
            elif r + 2 < R and data[r+2][c] == '.':
                pos = (r+2, c)
            else:
                pos = None
    
            if pos:
                if label == "AA":
                    start = pos
                elif label == "ZZ":
                    end = pos
                else:
                    portals[label].append(pos)

shortcuts = {}
for _,(a,b) in portals.items():
    shortcuts[a]=b
    shortcuts[b]=a
    
outer = set()
for (r,c) in shortcuts:
    if r <= 2 or r >= R-3 or c <= 2 or c >= C-3:
        outer.add((r,c))    

#PART 1
Q = deque()
Q.append((start,0))
visited = set()

while Q:
    pos,steps = Q.popleft()
    if pos in visited:
        continue
    visited.add(pos)
    if pos == end:
        ans[0] = steps
        break
    r,c = pos
    for dr,dc in DIR:
        nr,nc = r+dr,c+dc
        if data[nr][nc] == '.':
            Q.append(((nr,nc),steps+1))
    if pos in shortcuts:
        Q.append((shortcuts[pos],steps+1))
    
#PART 2
Q = deque()
Q.append((start,0,0))
visited = set()

while Q:
    pos,level,steps = Q.popleft()
    if (pos,level) in visited:
        continue
    visited.add((pos,level))
    if pos == end and level==0:
        ans[1] = steps
        break
    r,c = pos
    for dr,dc in DIR:
        nr,nc = r+dr,c+dc
        if data[nr][nc] == '.':
            Q.append(((nr,nc),level,steps+1))
    if pos in shortcuts:
        if pos in outer:
            if level > 0:  # can't go above level 0
                Q.append((shortcuts[pos], level - 1, steps + 1))
        else:
            Q.append((shortcuts[pos], level + 1, steps + 1))
    
print(ans)