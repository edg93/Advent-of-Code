with open("AoC2015_06_data.txt", "r") as file:
     data = file.read()
     
data = data.split('\n')
     
ans =[0,0]

G = [[False for _ in range(1000)] for _ in range(1000)]
G2 = [[0 for _ in range(1000)] for _ in range(1000)]


for line in data:
    p1,p2 = line.split(' through ')
    x2,y2 = [int(x) for x in p2.split(',')]
    p1,y1 = p1.split(',')
    y1 = int(y1)
    if 'toggle' in p1:
        instruction,x1 = p1.split()
    else:
        x1 = p1.split()[-1]
        if 'on' in p1:
            instruction = 'turn on'
        else:
            instruction = 'turn off'
    x1 = int(x1)
    
    if instruction == 'turn on':
        for x in range(min(x1,x2),max(x1,x2)+1):
            for y in range(min(y1,y2),max(y1,y2)+1):
                G[x][y] = True
                G2[x][y] += 1

    elif instruction == 'turn off':
        for x in range(min(x1,x2),max(x1,x2)+1):
            for y in range(min(y1,y2),max(y1,y2)+1):
                G[x][y] = False
                G2[x][y] = max(0,G2[x][y]-1)
    else:
        for x in range(min(x1,x2),max(x1,x2)+1):
            for y in range(min(y1,y2),max(y1,y2)+1):
                G2[x][y]+=2
                if G[x][y]:
                    G[x][y] = False
                else:
                    G[x][y] = True

for x in range(1000):
    for y in range(1000):
        if G[x][y]:
            ans[0]+=1
        ans[1]+=G2[x][y]


print(ans)