"Day 15 of AOC2021"
from collections import deque
import heapq

with open("data.txt", "r") as file:
    data = file.read()
    
G = data.split('\n')
for i in range(len(G)):
    l = []
    for letter in G[i]:
        l.append(int(letter))
    G[i]=l

R = len(G)
C = len(G[0])
 

#Questo funziona solo con giù/dx
done=set()
def solve(r,c,n,visited):
    print(r,c)
    if (r,c) in done:
        return done[(r,c)]
    if r<0 or r>=n*R or c<0 or c>=n*C:
        return 10000000
    if(r,c) in visited:
        return 10000000
        
    cost = G[r%R][c%C] + (r//R) + (c//C)
    while cost >9:
        cost -= 9
    if r==n*R-1 and c==n*C-1:
        return cost
        
    visited.add((r,c))
    ans = cost + min(solve(r+1,c,n,visited),solve(r,c+1,n,visited))
    done[(r,c)]=ans
    
    return ans


DR = [-1,0,1,0]
DC = [0,1,0,-1]
def solve2(n):
    Q = [(0,0,0)]
    D = [[None for _ in range(n*C)] for _ in range(n*R)]
    while Q:
        dist,r,c = heapq.heappop(Q)
        if r<0 or r>=n*R or c<0 or c>=n*C:
            continue

        cost = G[r%R][c%C] + (r//R) + (c//C)
        while cost >9:
            cost -= 9
        cost += dist
        
        if D[r][c] is None or cost<D[r][c]:
            D[r][c]=cost
        else:
            continue
        
        if r==n*R-1 and c==n*C-1:
            break
        
        for d in range(4):
            rr = r+DR[d]
            cc = c+DC[d]
            heapq.heappush(Q,(D[r][c],rr,cc))
            
    return D[n*R-1][n*C-1]-G[0][0]

#Questo ci mette troppo
def solve3(n):
    Q = deque([(0,0,0)])
    D = [[None for _ in range(n*C)] for _ in range(n*R)]
    while Q:
        dist,r,c = Q.popleft()
        if r<0 or r>=n*R or c<0 or c>=n*C:
            continue

        cost = G[r%R][c%C] + (r//R) + (c//C)
        while cost >9:
            cost -= 9
        cost += dist

        
        if D[r][c] is None or cost<D[r][c]:
            D[r][c]=cost
        else:
            continue
        
        for d in range(4):
            rr = r+DR[d]
            cc = c+DC[d]
            Q.append((D[r][c],rr,cc))

    return D[n*R-1][n*C-1]-G[0][0]

print(solve2(1))
print(solve2(5))

