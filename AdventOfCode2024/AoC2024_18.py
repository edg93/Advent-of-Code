from collections import deque

for file in ["AoC2024_18_test.txt","AoC2024_18_data.txt"]:
    with open(file, "r") as f:
        data = f.read()        
        
    data = data.split('\n')
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    ans = [None,None]
    
    if file =="AoC2024_18_test.txt":
        bound_part1 = 12
        dim = 7
    else:
        bound_part1 = 1024
        dim = 71
    
    fallen_bytes = []
    
    for i,line in enumerate(data):
        x,y = [int(x) for x in line.split(',')]
        fallen_bytes.append((x,y))
    
    
    
    for i in range(bound_part1,len(data)):
        costs = [[10e9 for _ in range(dim)] for _ in range(dim)]
        print(i)
        bytes_considered = set(fallen_bytes[:i])
        Q = deque([])
        Q.append((0,0,0))
        shortest_path = None
        while Q:
            x,y,cost = Q.popleft()
            if cost>=costs[x][y]:
                continue
            costs[x][y]=cost
            if x==dim-1 and y==dim-1:
                shortest_path=cost
                break
            for dx,dy in directions:
                if 0<=x+dx<dim  and 0<=y+dy<dim and (x+dx,y+dy) not in bytes_considered:
                    Q.append((x+dx,y+dy,cost+1))
                 
        if i==bound_part1:
            ans[0]=shortest_path
        if not shortest_path:
            ans[1]=fallen_bytes[i-1]
            break
                    
    def output(bytes_list):
        for r in range(dim):
            s=''
            for c in range(dim):
                if (r,c) in bytes_list:
                    s+='O'
                else:
                    s+='.'
            print(s)
    #output(fallen_bytes_part1)
    print(ans)

    #Si potrebbe velocizzare molto usando bisezione sulla parte2.