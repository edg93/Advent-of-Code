with open("AoC2020_24_data.txt", "r") as file:
    data = file.read()
data=data.split('\n')

def neighbors(tile):
    x,y = tile
    return[(x+2,y),(x-2,y),(x+1,y+1),(x+1,y-1),(x-1,y+1),(x-1,y-1)]

black = set()

for line in data:
    move = [0,0]
    for k in range(len(line)):
        letter = line[k]
        if line[k-1]!='n' and line[k-1]!='s':
            if letter == 'e':
                move[0] += 2
            elif letter == 'w':
                move[0] -= 2
            elif letter == 'n':
                move[1] += 1
                if line[k+1]=='e':
                    move[0] += 1
                else:
                    move[0] -= 1
            elif letter == 's':
                move[1] -= 1
                if line[k+1]=='e':
                    move[0] += 1
                else:
                    move[0] -= 1
    if tuple(move) in black:
        black.remove(tuple(move))
    else:

        black.add(tuple(move))
        
print(len(black))
        
for k in range(100):
    toFlip = set()
    for tile in black:
        b = 0
        for n in neighbors(tile):
            if n in black:
                b += 1
            else:
                if (n,0) in toFlip:
                    continue
                b1 = 0
                for n1 in neighbors(n):
                    if n1 in black:
                        b1 += 1
                if b1==2:
                    toFlip.add((n,0))
        if b not in [1,2]:
            toFlip.add((tile,1))
    for tile,c in toFlip:
        if c==1:
            black.remove(tile)
        else:
            black.add(tile)
print(len(black))