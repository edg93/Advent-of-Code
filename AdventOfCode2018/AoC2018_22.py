import heapq

def erosion(target,depth):
    mod = 20183
    X, Y = target
    maxX, maxY = X+20, Y+20
    ero = [[0 for _ in range(maxY + 1)] for _ in range(maxX + 1)]
    for x in range(maxX + 1):
        for y in range(maxY + 1):
            if (x, y) == (0, 0) or (x, y) == target:
                ero[x][y] = depth % mod
            elif y == 0:
                ero[x][y] = (x * 16807 + depth) % mod
            elif x == 0:
                ero[x][y] = (y * 48271 + depth) % mod
            else:
                ero[x][y] = (ero[x - 1][y] * ero[x][y - 1] + depth) % mod
    return ero

def region(x, y):
    return E[x][y] % 3

depth =  7740
target = (12,763)
ans = [0,0]
X,Y = target
DIR = ((0,1),(1,0),(0,-1),(-1,0))
risk_level = {'|':2,'=':1,'.':0}
erosion_level = {0:'.',1:'=',2:'|'}

E = erosion(target,depth)

for x in range(X+1):
    for y in range(Y+1):
        ans[0] += region(x,y)
        
TORCH, CLIMB, NEITHER = 0, 1, 2
allowed = {
    0: {TORCH, CLIMB},       # rocky
    1: {CLIMB, NEITHER},     # wet
    2: {TORCH, NEITHER}      # narrow
}
max_X,max_Y = X+20,Y+20

seen = set()
Q = [(0,0,0,TORCH)]

while Q:
    time,x,y,current_tool = heapq.heappop(Q)
    if (x, y, current_tool) in seen:
        continue
    seen.add((x, y, current_tool))
    
    if (x, y) == target and current_tool == 0:
        ans[1] = time
        break
    
    # switch tool
    for tool in allowed[region(x,y)]:
        if tool != current_tool:
            heapq.heappush(Q, (time + 7, x, y, tool))
            
    # move
    for dx, dy in DIR:
        nx,ny = x+dx,y+dy
        if not (0<=nx<=max_X and 0<=ny<=max_Y):
            continue
        if current_tool in allowed[region(x,y)]:
            heapq.heappush(Q, (time + 1, nx, ny, current_tool))
            
print(ans)