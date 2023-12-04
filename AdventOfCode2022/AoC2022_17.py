from time import time

with open("AoC2022_17_data.txt", "r") as file:
    data = file.read()

p1 = {(2,0),(3,0),(4,0),(5,0)}
p2 = {(3,0),(2,1),(3,1),(4,1),(3,2)}
p3 = {(2,0),(3,0),(4,0),(4,1),(4,2)}
p4 = {(2,0),(2,1),(2,2),(2,3)}
p5 = {(2,0),(2,1),(3,0),(3,1)}

pieces = (p1,p2,p3,p4,p5)
t0 = time()
def move(piece,direction):
    if direction == 'L':
        if any([x==0 for (x,y) in piece]):
            return piece
        return set([(x-1,y) for (x,y) in piece])
    elif direction == 'R':
        if any([x==6 for (x,y) in piece]):
            return piece
        return set([(x+1,y) for (x,y) in piece])
    elif direction == 'U':
        return set([(x,y+1) for (x,y) in piece])
    elif direction == 'D':
        return set([(x,y-1) for (x,y) in piece])

def generate_key(G,m):
    return frozenset([(x,m-y) for (x,y) in G if m-y<=10])

for n in [2022,1000000000000]:
    S = set([(x,0) for x in range(7)])
    t = 0
    top = 0
    d = {}
    p = 0
    added = 0
    while p < n:
        piece = pieces[p%5]
        piece = set([(x,y+top+4) for (x,y) in piece])
        p+=1
        while True:
            if data[t]=='<':
                piece = move(piece,'L')
                if piece & S:
                    piece = move(piece,'R')
            else:
                piece = move(piece,'R')
                if piece & S:
                    piece = move(piece,'L')
            t = (t+1)%len(data)
            piece = move(piece,'D')
            if piece & S:
                piece = move(piece,'U')
                S = S | piece
                top = max([y for (x,y) in S])
                key = (t,p%5,generate_key(S,top))
                if key in d.keys():
                    diff_top = top-d[key][1]
                    diff_p = p - d[key][0]
                    cicles = (n-p)//diff_p
                    p += cicles*diff_p
                    added += cicles*diff_top
                d[key]=(p,top)
                break
            
    print(top+added)
print(time()-t0)