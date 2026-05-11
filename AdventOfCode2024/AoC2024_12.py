from collections import defaultdict, deque
for file in ["AoC2024_12_test.txt","AoC2024_12_data.txt"]:
    with open(file, "r") as f:
        data = f.read()
        
    G = data.split('\n')
    R,C = len(G),len(G[0])
    D = ((0,1),(1,0),(0,-1),(-1,0))
    ans = [0,0]
    
    explored = set()
    
    def count_sides(area):
        sides = 0
        for r, c in area:
            # North
            if (r-1, c) not in area:
                if (r, c-1) not in area or (r-1, c-1) in area:
                    sides += 1
            # South
            if (r+1, c) not in area:
                if (r, c-1) not in area or (r+1, c-1) in area:
                    sides += 1
            # West
            if (r, c-1) not in area:
                if (r-1, c) not in area or (r-1, c-1) in area:
                    sides += 1
            # East
            if (r, c+1) not in area:
                if (r-1, c) not in area or (r-1, c+1) in area:
                    sides += 1
        return sides
    
    for r in range(R):
        for c in range(C):
            if (r,c) not in explored:
                crop = G[r][c]
                area = {(r,c)}
                perimeter = 0
                explored.add((r,c))
                Q = deque()

                for dr,dc in D:
                    Q.append((r+dr,c+dc))
                while Q:
                    r1,c1 = Q.popleft()
                    if (r1,c1) in area:
                        continue
                    if 0<=r1<R and 0<=c1<C and G[r1][c1]==crop:
                        explored.add((r1,c1))
                        area.add((r1,c1))
                        for dr,dc in D:
                            Q.append((r1+dr,c1+dc))
                    else:
                        perimeter +=1
                ans[0] += len(area)*perimeter
                ans[1] += len(area)*count_sides(area)
                
    print(ans)