with open("AoC2020_11_data.txt", "r") as file:
    data = file.read()
data=data.split('\n')

R,C=len(data),len(data[0])
DIR = ((0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1))

def neighbours(G,r,c):
    n = 0
    for (dr,dc) in DIR:
        if 0<=r+dr<R and 0<=c+dc<C and G[r+dr][c+dc]=='#':
            n +=1
    return n

def neighbours1(G,r,c):
    n = 0
    for (dr,dc) in DIR:
        k=1
        while 0<=r+dr*k<R and 0<=c+dc*k<C:
            if G[r+dr*k][c+dc*k]=='#':
                n +=1
            if G[r+dr*k][c+dc*k]!='.':
                break
            k += 1
    return n

def show(G):
    for line in G:
        line = ''.join(line)
        print(line)
        
def iteration(G,part):
    to_occupy, to_free = set(),set()
    changed = False
    for i in range(R):
        for j in range(C):
            if part==3:
                n = neighbours(G,i,j)
            else:
                n = neighbours1(G,i,j)
            if G[i][j]=='L' and n==0:
                to_occupy.add((i,j))
                changed = True
            if G[i][j]=='#' and n>part:
                to_free.add((i,j))
                changed=True
    for (i,j) in to_occupy:
        G[i][j]='#'
    for (i,j) in to_free:
        G[i][j]='L'
    return G,changed

for part in [3,4]:
    G = [[x for x in line] for line in data]
    changed = True
    while changed:
        G,changed=iteration(G,part)
    ans=0
    for i in range(R):
        for j in range(C):
            if G[i][j]=='#':
                ans += 1
    print(ans)