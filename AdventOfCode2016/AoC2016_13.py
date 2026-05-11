from collections import deque

data = 1350
DIR = ((0,1),(1,0),(0,-1),(-1,0))
ans = [0,0]

def valid(x,y):
    n = bin(x*x + 3*x + 2*x*y + y + y*y + data).count('1')
    if n%2==0:
        return True
    return False

def shortest_path(start,end=None,part2=False):
    x,y = start
    Q = deque([(x,y,0)])
    visited = set()
    
    while Q:
        x,y,steps = Q.popleft()
        
        if not part2 and (x,y) == end:
            return steps
        if part2 and steps>49:
            continue
        visited.add((x,y))
        for dx,dy in DIR:
            nx, ny = x + dx, y + dy
            if nx >= 0 and ny >= 0 and valid(nx, ny):
                if (nx,ny) not in visited:
                    visited.add((nx, ny))
                    Q.append((nx, ny, steps + 1))
    if part2:
        return len(visited)

start = (1,1)
end = (31,39)
ans[0] = shortest_path(start,end)
ans[1] = shortest_path(start,part2=True)

print(ans)