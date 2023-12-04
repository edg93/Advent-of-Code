with open("AoC2022_23_data.txt", "r") as file:
    data = file.read()
data=data.strip().split('\n')

elves = set()

for y in range(len(data)):
    for x in range(len(data[y])):
        if data[y][x]=='#':
            elves.add((x,y))

def score(elves):
    X = (0,0)
    Y = (0,0)
    for elf in elves:
        X = (min(X[0],elf[0]),max(X[1],elf[0]))
        Y = (min(Y[0],elf[1]),max(Y[1],elf[1]))
    return X,Y,(X[1]-X[0]+1)*(Y[1]-Y[0]+1)-len(elves)

def show(elves):
    G = []
    X,Y,s = score(elves)
    for y in range(Y[1]-Y[0]+1):
        G.append([' ' for x in range(X[1]-X[0]+1)])
    for elf in elves:
        G[elf[1]][elf[0]]='#'
    for line in G:
        print(''.join(line))
        
def is_free(elf,elves,direction='ALL'):
    if direction == 'ALL':
        for x in [-1,0,1]:
            for y in [-1,0,1]:
                if (x!=0 or y!=0) and (elf[0]+x,elf[1]+y) in elves:
                    return False
        return True
    elif direction == (0,1):
        for x in [-1,0,1]:
            if (elf[0]+x,elf[1]+1) in elves:
                return False
        return True
    elif direction == (0,-1):
        for x in [-1,0,1]:
            if (elf[0]+x,elf[1]-1) in elves:
                return False
        return True
    elif direction == (1,0):
        for y in [-1,0,1]:
            if (elf[0]+1,elf[1]+y) in elves:
                return False
        return True
    elif direction == (-1,0):
        for y in [-1,0,1]:
            if (elf[0]-1,elf[1]+y) in elves:
                return False
        return True
    
counter = 0
directions = [(0,-1),(0,1),(-1,0),(1,0)]
moved = True
turns = 1

while moved:
    moves = {}
    moves_counter = {}
    for elf in elves:
        if is_free(elf,elves):
            continue
        else:
            for i in range(4):
                direction = directions[(counter+i)%4]
                if is_free(elf,elves,direction):
                    move = (elf[0]+direction[0],elf[1]+direction[1])
                    moves[elf]=move
                    if move in moves_counter.keys():
                        moves_counter[move]+=1
                    else:
                        moves_counter[move]=1
                    break
                else:
                    continue
    moved=False
    for before,after in moves.items():
        if moves_counter[after]==1:
            moved= True
            elves.remove(before)
            elves.add(after)
    if turns == 10:
        print(score(elves)[2])
    counter = (counter+1)%4
    if not moved:
        print(turns)
    turns += 1