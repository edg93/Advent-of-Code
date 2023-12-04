from collections import deque
with open("AoC2022_12_data.txt", "r") as file:
    data = file.read()
data=data.strip().split('\n')

def moves(position):
    moves = set()
    for mov in DIR:
        r,c = position
        h = ord(data[r][c])
        r += mov[0]
        c += mov[1]
        if 0<=r<R and 0<=c<C and ord(data[r][c])-h>=-1:
            moves.add((r,c))
    return moves

    for line in data:
        print(line)
    for line in dist:
        print(line)
for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == 'S':
            start = (i,j)
            data[i]=data[i][:j]+'a'+data[i][j+1:]
        elif data[i][j] == 'E':
            end = (i,j)
            data[i]=data[i][:j]+'z'+data[i][j+1:]

DIR = ((1,0),(-1,0),(0,1),(0,-1))
R,C = len(data),len(data[0])
dist = [[None for i in range(C)] for j in range(R)]
ans2 = 1e9
Q = deque()
Q.append((end,0))
visited = set()

while Q:
    (r,c),d=Q.popleft()
    h = ord(data[r][c])
    for (rr,cc) in moves((r,c)):
        if (rr,cc) in visited:
            continue
        if dist[rr][cc]==None:
            dist[rr][cc] = d+1
        visited.add((rr,cc))
        Q.append(((rr,cc),d+1))
    
for r in range(R):
    for c in range(C):
        if data[r][c]=='a' and dist[r][c]!=None:
            ans2 = min(ans2,dist[r][c])
print(dist[start[0]][start[1]])
print(ans2)