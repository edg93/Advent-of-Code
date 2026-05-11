from collections import defaultdict, deque

for file in ["AoC2024_16_test.txt","AoC2024_16_data.txt"]:

    with open(file, "r") as f:
        data = f.read()
        
    G = data.split('\n')
    
    R = len(G)
    C = len(G[0])
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    

    ans = [None,None]
    
    for r in range(R):
        for c in range(C):
            if G[r][c]=='S':
                start = (r,c)
            elif G[r][c]=='E':
                end = (r,c)
                
                
    costs = {}
                
    Q = deque([])
    Q.append((start,(0,1),0))
    while Q:
        
        pos,d,cost=Q.popleft()
        r,c=pos
        if (r,c,d) in costs and costs[(r,c,d)]<cost:
            continue
        costs[(r,c,d)]=cost
        for (dr,dc) in directions:
            if 0<=r+dr<R and 0<=c+dc<C and G[r+dr][c+dc]!='#':
                if d==(dr,dc):
                    Q.append(((r+dr,c+dc),d,cost+1))
                elif dr!=-d[0] or dc!=-d[1]:
                    Q.append(((r+dr,c+dc),(dr,dc),cost+1001))
                
    ans[0]=min([costs[(end[0],end[1],x)] for x in directions if (end[0],end[1],x) in costs.keys()])
    
    Q = deque([])
    Q.append((start,(0,1),0,{start}))
    seats = set()
    while Q:
        pos,d,cost,visited=Q.popleft()
        if pos ==end and cost==ans[0]:
            seats|=visited
        r,c=pos
        if costs[(r,c,d)]<cost:
            continue
        for (dr,dc) in directions:
            if 0<=r+dr<R and 0<=c+dc<C and G[r+dr][c+dc]!='#':
                if d==(dr,dc):
                    Q.append(((r+dr,c+dc),d,cost+1,visited|{(r+dr,c+dc)}))
                elif dr!=-d[0] or dc!=-d[1]:
                    Q.append(((r+dr,c+dc),(dr,dc),cost+1001,visited|{(r+dr,c+dc)}))
            

    ans[1]=len(seats)
    print(ans)
    
    def output():
        for r in range(R):
            s=''
            for c in range(C):
                if G[r][c]=='#':
                    s+='#'
                elif (r,c) in seats:
                    s+='O'
                else:
                    s+='.'
            print(s)
                    