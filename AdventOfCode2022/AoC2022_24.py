from time import time 
with open("AoC2022_24_ex.txt", "r") as file:
    data = file.read()
data=data.strip().split('\n')

R=len(data)
C=len(data[0])
blizards = set()
t0=time()
for r,line in enumerate(data):
    for c in range(len(line)):
        if r==0 and line[c]=='.':
            start = (r,c)
        elif r==len(data)-1 and line[c]=='.':
            end = (r,c)
        if line[c] in ['<','>','v','^']:
            blizards.add((r,c,line[c]))
    
def update(blizards):
    new_blizards = set()
    for r,c,d in blizards:
        if d == 'v':
            if r+1!=R-1:
                new_blizards.add((r+1,c,d))
            else:
                new_blizards.add((1,c,d))
        elif d == '>':
            if c+1!=C-1:
                new_blizards.add((r,c+1,d))
            else:
                new_blizards.add((r,1,d))
        elif d == '<':
            if c-1!=0:
                new_blizards.add((r,c-1,d))
            else:
                new_blizards.add((r,C-2,d))
        elif d == '^':
            if r-1!=0:
                new_blizards.add((r-1,c,d))
            else:
                new_blizards.add((R-2,c,d))
    return new_blizards

def free(r,c,blizards):
    if (r,c,'>') in blizards:
        return False
    if (r,c,'<') in blizards:
        return False
    if (r,c,'v') in blizards:
        return False
    if (r,c,'^') in blizards:
        return False
    if (r,c) != end and r==R-1:
        return False
    if c==0 or c==C-1:
        return False
    if (r,c) != start and r==0:
        return False
    return True

visited = {}
T=1000
blizards_time = {0:blizards}
def move(position,blizards,turns,goal):
    global T
    if turns+1 in blizards_time.keys():
        blizards = blizards_time[turns+1]
    else:
        blizards = update(blizards)
        blizards_time[turns+1]=blizards
    r,c = position
    if turns >= T:
        return T
    if position == goal:
        T = min(T,turns)
        return turns
    key = (position,turns)
    if key in visited.keys():
        return visited[key]
    m = int(1e10)
    if goal == end:
        for dr,dc in [(1,0),(0,1),(0,0),(-1,0),(0,-1)]:
            if free(r+dr,c+dc,blizards):
                m=min(m,move((r+dr,c+dc),blizards,turns+1,goal))  
    elif goal == start:
        for dr,dc in [(-1,0),(0,-1),(0,0),(1,0),(0,1)]:
            if free(r+dr,c+dc,blizards):
                m=min(m,move((r+dr,c+dc),blizards,turns+1,goal))  
    visited[key]=m               
    return m

t1 = move(start,blizards,0,end)
print(t1)
T=1000
visited = {}

t2=move(end,blizards,t1,start)
print(t2)
T=1000
visited = {}

t3=move(start,blizards,t2,end)
print(t3)
print(time()-t0)