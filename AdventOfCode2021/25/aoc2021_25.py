"Day 25 of AOC2021"
with open("data.txt", "r") as file:
    data = file.read()
    
data = data.split('\n')
    
G = [[x for x in y] for y in data ]

R = len(G)
C = len(G[0])

move = True
counter = 0

while move:
    to_move = set()
    move = False
    for r in range(R):
        for c in range(C):
            cc = (c+1)%C
            rr = (r+1)%R
            if G[r][c]=='>' and G[r][cc]=='.':
                to_move.add((r,c))
                move = True
    for x in to_move:
        r,c = x[0],x[1]
        cc = (c+1)%C
        G[r][c]='.'
        G[r][cc]='>'

        
    to_move = set()
    for r in range(R):
        for c in range(C):
            cc = (c+1)%C
            rr = (r+1)%R
            if G[r][c]=='v' and G[rr][c]=='.':
                to_move.add((r,c))
                move = True
    for x in to_move:
        r,c = x[0],x[1]
        rr = (r+1)%R
        G[r][c]='.'
        G[rr][c]='v'
    counter +=1
    
print(counter)