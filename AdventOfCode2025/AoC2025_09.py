from collections import deque



for file in ["AoC2025_09_test.txt","AoC2025_09_data.txt"]:
    with open(file, "r") as f:
        data = f.read()
        
    data = data.split('\n')
    ans = [0,0]
    points = set()
    rectangles = {}
    segments = []
    
    boundary = set()
    
    for i,line in enumerate(data):
        x,y = [int(a) for a in line.split(',')]
        points.add((x,y))
        if i!=len(data)-1:
            x2,y2 = [int(a) for a in data[i+1].split(',')]
        else:
            x2,y2 = [int(a) for a in data[0].split(',')]
        segments.append([x,y,x2,y2])
    
    def sign(d):
        if d > 0:
            return 1
        if d < 0:
            return -1
        return 0

    for (x1,y1,x2,y2) in segments:
        dx = sign(x2-x1)
        dy = sign(y2-y1)
        x,y = x1,y1
        while (x,y) != (x2,y2):
            boundary.add((x,y))
            x += dx
            y += dy
        boundary.add((x2,y2))
    
    minx = min(x for x,y in boundary) - 1
    maxx = max(x for x,y in boundary) + 1
    miny = min(y for x,y in boundary) - 1
    maxy = max(y for x,y in boundary) + 1
    
    outside = set()
    Q = deque([(minx, miny)])
    outside.add((minx,miny))

    while Q:
        if len(outside)%10000==0:
            print(len(outside))
        x,y = Q.popleft()
        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx,ny = x+dx, y+dy
            if (nx,ny) in outside: continue
            if nx < minx or nx > maxx or ny < miny or ny > maxy: continue
            if (nx,ny) in boundary: continue
            outside.add((nx,ny))
            Q.append((nx,ny))

    interior = {
        (x,y)
        for x in range(minx+1, maxx)
            for y in range(miny+1, maxy)
                if (x,y) not in outside and (x,y) not in boundary
    }
     

    def valid(x,y):
        if (x,y) in boundary|interior:
            return True 
        return False
    
    ps = [[0] * (maxy + 2) for _ in range(maxx + 2)]
    
    for x, y in boundary|interior:
        ps[x+1][y+1] = 1   # +1 to handle 0-index for prefix sum
    # Compute prefix sums
    for x in range(1, maxx + 2):
        for y in range(1, maxy + 2):
            ps[x][y] += ps[x-1][y] + ps[x][y-1] - ps[x-1][y-1]
            
    def rectangle_allowed(x1, y1, x2, y2):
        # x1,y1 and x2,y2 are inclusive
        x1 += 1; y1 += 1; x2 += 1; y2 += 1  # shift for prefix sum
        count = ps[x2][y2] - ps[x1-1][y2] - ps[x2][y1-1] + ps[x1-1][y1-1]
        return count == (x2 - x1 + 1) * (y2 - y1 + 1)
    

    for (x1,y1) in points:
        for (x2,y2) in points:
            if (x1!=x2 or y1!=y2) and (x2,y2,x1,y1) not in rectangles.keys():
                rectangles[(x1,y1,x2,y2)]=abs(x2-x1+1)*abs(y2-y1+1)

    
    
    for rectangle,area in rectangles.items():
        x,y,x1,y1=rectangle
        if rectangle_allowed(x,y,x1,y1):
            ans[1]=max(ans[1],area)
        if rectangle_allowed(x1,y1,x,y):
            ans[1]=max(ans[1],area)    
            
            
    ans[0]=max(rectangles.values())
    print(ans)
