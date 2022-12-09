f = open("data.txt", "r")
data = f.read()
data=data.split('\n')

flip = []


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
    if move in flip:
        flip.remove(move)
    else:
        flip = flip + [move]
        
print(len(flip))