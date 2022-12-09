f = open("data.txt", "r")
data = f.read()
data=data.split('\n')

black = []

def neighbors(tile):
    x = tile[0]
    y = tile[1]
    return[[x+2,y],[x-2,y],[x+1,y+1],[x+1,y-1],[x-1,y+1],[x-1,y-1]]

for line in data:
    move = [0,0]
    for k in range(len(line)):
        letter = line[k]
        if line[k-1]!='n' and line[k-1]!='s':
            if letter == 'e':
                move[0] = move[0]+2
            elif letter == 'w':
                move[0] = move[0]-2
            elif letter == 'n':
                move[1] = move[1] + 1
                if line[k+1]=='e':
                    move[0] = move[0] + 1
                else:
                    move[0] = move[0] - 1
            elif letter == 's':
                move[1] = move[1] - 1
                if line[k+1]=='e':
                    move[0] = move[0] + 1
                else:
                    move[0] = move[0] - 1
    if move in black:
        black.remove(move)
    else:
        black = black + [move]
     
print(len(black))
print(black)

for k in range(100):
    toflip = []
    for tile in black:
        if tile in toflip:
            continue
        b = 0
        for n in neighbors(tile):
            if n in black:
                b = b+1
            else:
                if n in toflip:
                    continue
                b1 = 0
                for n1 in neighbors(n):
                    if n1 in black:
                        b1 = b1+1
                if b1==2 and ([n,0] not in toflip):
                    toflip = toflip + [[n,0]]
        if b!=1 and b!=2 and ([tile,1] not in toflip):
            toflip = toflip + [[tile,1]]
    for tile in toflip:
        if tile[1]==1:
            black.remove(tile[0])
        else:
            black = black + [tile[0]]
    print(k, len(black))