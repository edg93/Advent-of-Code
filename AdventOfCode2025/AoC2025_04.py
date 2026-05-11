for file in ["AoC2025_04_test.txt","AoC2025_04_data.txt"]:
    with open(file, "r") as file:
        data = file.read()
        
    data = data.split('\n')
    ans = [0,0]
    dir =((1,1),(1,0),(1,-1),(0,1),(0,-1),(-1,1),(-1,0),(-1,-1))
    
    R = len(data)
    C = len(data[0])
    part1 = True
    stop = False
    while not stop:
        stop = True
        for r in range(R):
            for c in range(C):
                if data[r][c]=='@':
                    rolls = 0
                    for dr,dc in dir:
                        if 0<=r+dr<R and 0<=c+dc<C and data[r+dr][c+dc]=='@':
                            rolls+=1
                    if rolls<4:
                        if part1:
                            ans[0]+=1
                            
                        ans[1]+=1
                        data[r]=data[r][:c]+'.'+data[r][c+1:]
                        stop = False
        part1 = False
    print(ans)