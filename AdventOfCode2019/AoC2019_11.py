from IntcodeComputer import computer

with open("AoC2019_11_data.txt", "r") as file:
    data0 = file.read()

data0 = [int(x) for x in data0.split(',')]

def paint(data,pos=(0,0),orientation=0,i=0,base=0):
    while True:
        if pos in white_panels:
            ip = 1
        else:
            ip = 0
        data,i,base,colour = computer(data,ip,i,base)
        painted_panels.add(pos)
        if colour == 0 and pos in white_panels:
            white_panels.remove(pos)
        elif colour == 1 and pos not in white_panels:
            white_panels.add(pos)
        elif colour not in [0,1]:
            break
        data,i,base,turn = computer(data,colour,i,base)
        if turn == 0:
            orientation = (orientation - 1)%4
        elif turn == 1:
            orientation = (orientation + 1)%4
        else:
            break
        dpos = DIR[orientation]
        pos = (pos[0]+dpos[0],pos[1]+dpos[1])
    
def show(white_panels):
    pic = [[' ' for _ in range(40)] for _ in range(6)]

    X,Y = [1e9,-1e9],[1e9,-1e9]
    for panel in white_panels:
        y,x = panel
        X[0],X[1] = min(X[0],x),max(X[1],x)
        Y[0],Y[1] = min(Y[0],y),max(Y[1],y)
    for y,x in white_panels:
        pic[-y][x]='#'
        
    for line in pic:
        print(''.join(line))

DIR = [(1,0),(0,1),(-1,0),(0,-1)]

for n,white_panels in enumerate([set(),set([(0,0)])]):
    orientation = 0
    pos = (0,0)
    data = {n:x for n,x in enumerate(data0)}
    painted_panels = set()
    paint(data)
    if n==0:
        print(len(painted_panels))

show(white_panels)


