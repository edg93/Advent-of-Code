with open("AoC2019_24_data.txt", "r") as f:
    data = f.read()

data = data.splitlines()
ans = [0,0]
R,C = len(data),len(data[0])
DIR = ((1,0),(-1,0),(0,1),(0,-1))

def parse(data):
    bugs = set()
    for r in range(R):
        for c in range(C):
            if data[r][c] == '#':
                bugs.add((r,c,0))
    return bugs
            
def neighbors(r,c,level,recursive):
    nb = set()
    for dr,dc in DIR:
        nr,nc = r+dr,c+dc
        if recursive and (nr,nc) == (2,2):
            if r == 1:
                for x in range(5):    nb.add((0, x, level+1))
            elif r == 3:
                for x in range(5):    nb.add((4, x, level+1))
            elif c == 1:
                for x in range(5):    nb.add((x, 0, level+1))
            elif c == 3:
                for x in range(5):    nb.add((x, 4, level+1))
        else:
            if 0<=nr<5 and 0<=nc<5:
                nb.add((nr,nc,level))
            elif recursive:
                if nr == -1:
                    nb.add((1,2,level-1))
                elif nr == 5:
                    nb.add((3,2,level-1))
                elif nc == -1:
                    nb.add((2,1,level-1))
                elif nc == 5:
                    nb.add((2,3,level-1))
    
    return nb

def evolve(bugs,recursive=False):
    new_bugs = set()
    candidates = set()
    for r,c,l in bugs:
        candidates.add((r,c,l))
        nb = neighbors(r,c,l,recursive)
        candidates |= nb
    for r,c,l in candidates:    
        count = sum((n in bugs) for n in neighbors(r, c, l, recursive))
    
        if (r,c,l) in bugs:
            if count == 1:
                new_bugs.add((r,c,l))
        else:
            if count in {1,2}:
                new_bugs.add((r,c,l))

    return new_bugs

seen = set()
bugs = parse(data)
state = frozenset(bugs)
while state not in seen:
    seen.add(state)
    bugs = evolve(bugs)
    state = frozenset(bugs)

ans[0] = sum(2**(r*5 + c) for r,c,_ in bugs)

bugs = parse(data)
for _ in range(200):
    bugs = evolve(bugs,recursive=True)

ans[1] = len(bugs)
print(ans)