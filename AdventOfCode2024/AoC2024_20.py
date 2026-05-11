from collections import deque

for file in ["AoC2024_20_test.txt","AoC2024_20_data.txt"]:

    with open(file, "r") as f:
        data = f.read()
        
    G = data.split('\n')
    G =[[x for x in line] for line in G]
    R = len(G)
    C = len(G[0])
    
    for r in range(R):
        for c in range(C):
            if G[r][c]=='S':
                start = (r,c)
            elif G[r][c]=='E':
                end = (r,c)
                
    track = [(r,c) for r in range(R) for c in range(C) if G[r][c] != '#']

    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    ans = [0,0]
                    
    def shortest_paths(start,end):
        Q = deque([])
        Q.append((start,0))
        costs = [ ['#' for _ in range(C)] for _ in range(R)]
        while Q:
            pos,cost = Q.popleft()
            r,c = pos
            if costs[r][c]!='#' and costs[r][c]<=cost:
                continue
            costs[r][c]=cost
            if pos == end:
                continue
            for (dr,dc) in directions:
                if 0<=r+dr<R and 0<=c+dc<C and G[r+dr][c+dc]!='#':
                    Q.append(((r+dr,c+dc),cost+1))
                    
        return(costs)
        
        
    times_to_start = shortest_paths(start,end)
    times_to_end = shortest_paths(end,start)
    
    def output(p1,p2):
        for r in range(R):
            s=''
            for c in range(C):
                if G[r][c]=='#':
                    s+='#'
                elif (r,c)==p1:
                    s+='S'
                elif (r,c)==p2:
                    s+='E'
                else:
                    s+='.'
            print(s)
    
    time_no_cheat=times_to_end[start[0]][start[1]]
    
    D = [2,20]
    l = {"AoC2024_20_test.txt":70,"AoC2024_20_data.txt":100}
    
    for d in D:
        for r1,c1 in track:
            if times_to_start[r1][c1] is None:
                continue
            p1 = r1,c1
            for dr in range(-d, d+1):
                rem = d - abs(dr)
                for dc in range(-rem, rem+1):
                    r2 = r1+dr
                    c2 = c1+dc
                    if 0<=r2<R and 0<=c2<C:
                        if G[r2][c2]=='#':
                            continue
                        p2=r2,c2
                        distance = abs(dr) + abs(dc)
                        if (time_no_cheat-times_to_end[r2][c2]-times_to_start[r1][c1]-distance)>=l[file]:
                            if d==D[0]:
                                ans[0]+=1
                            else:
                                ans[1]+=1
    print(ans)