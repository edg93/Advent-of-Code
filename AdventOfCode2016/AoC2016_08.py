for file in ["AoC2016_08_data.txt"]:
    with open(file, "r") as f:
        data = f.read()
    
    data = data.splitlines()
    
    lights = set()
    R,C = 6,50
    
    def output(lights):
        for r in range(R):
            s = ''
            for c in range(C):
                if (r,c) in lights:
                    s+='#'
                else:
                    s+='.'
            print(s)
    
    for line in data:
        line = line.split()
        if line[0] == 'rotate':
            n = int(line[-1])
            to_remove = set()
            to_add = set()
            if line[1] == 'column':
                c = int(line[2].split('=')[-1])    
                for (i,j) in lights:
                    if j==c:
                        to_remove.add((i,j))
                        to_add.add(((i+n)%R,j))
            elif line[1] == 'row':
                r = int(line[2].split('=')[-1])
                for (i,j) in lights:
                    if i==r:
                        to_remove.add((i,j))
                        to_add.add((i,(j+n)%C))
            lights -= to_remove
            lights |= to_add
        else:
            c,r = [int(a) for a in line[1].split('x')]
            for i in range(r):
                for j in range(c):
                    lights.add((i,j))
        
    ans = len(lights)
    output(lights)
    print(ans)