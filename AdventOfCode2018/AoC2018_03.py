for file in ["AoC2018_03_test.txt","AoC2018_03_data.txt"]:
    with open(file, "r") as f:
        data = f.read()        

    data = data.split('\n')
    ans = [0,0]
    covered = set()
    counted = set()
    for line in data:
        claim,rest = line.split(' @ ')
        start,dim = rest.split(': ')
        x,y=[int(i) for i in start.split(',')]
        dx,dy = [int(i) for i in dim.split('x')]
        for xx in range(dx):
            for yy in range(dy):
                point = (x+xx,y+yy)
                if point in covered:
                    if point in counted:
                        continue
                    counted.add(point)
                    ans[0]+=1
                covered.add(point)
        
    for line in data:
        claim,rest = line.split(' @ ')
        start,dim = rest.split(': ')
        x,y=[int(i) for i in start.split(',')]
        dx,dy = [int(i) for i in dim.split('x')]
        overlap = False
        for xx in range(dx):
            for yy in range(dy):
                point = (x+xx,y+yy)
                if point in counted:
                    overlap = True
                    break
                    
            if overlap:
                break
        if not overlap:
            ans[1]=int(claim[1:])
    
    print(ans)
