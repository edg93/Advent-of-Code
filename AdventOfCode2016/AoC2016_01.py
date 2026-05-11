for file in ["AoC2016_01_data.txt"]:
    with open(file, "r") as f:
        data = f.read()
        
        
    data = data.split(', ')
    DIR = ((-1,0),(0,1),(1,0),(0,-1))
    ans = [None,None]
    
    r,c = 0,0
    dir_idx = 0
    
    visited = {(r,c)}
    
    for line in data:
        turn,steps = line[0],int(line[1:])
        dir_idx = (dir_idx + (1 if turn == 'R' else -1)) % 4
        dr,dc = DIR[dir_idx]
        
        for _ in range(steps):
            r += dr
            c += dc
            if (r,c) in visited and ans[1] is None:
                ans[1] = abs(r)+abs(c)
            visited.add((r,c))
        
    ans[0] = abs(r)+abs(c)
    print(ans)  