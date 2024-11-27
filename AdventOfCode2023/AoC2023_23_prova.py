from collections import deque
from time import time

with open("AoC2023_23_data.txt", "r") as file:
    data = file.read()

data = data.split('\n')
R,C = len(data),len(data[0])
DIR = [(0,1),(1,0),(-1,0),(0,-1)]

for c,ch in enumerate(data[0]):
    if ch=='.':
        start = (0,c)
        break
        
for c,ch in enumerate(data[-1]):
    if ch=='.':
        end = (len(data)-1,c)
        break
        
def neighbours(state):
    r,c = state
    n = set()
    for dr,dc in DIR:
        if 0<=r+dr<R and 0<=c+dc<C and data[r+dr][c+dc]!='#':
            n.add((r+dr,c+dc))
    return n

def explore(node,departure):
    d=0
    while len(neighbours(node))==2:
        r,c=node
        for new_node in neighbours(node)-{departure}:
            d+=1
            departure=(r,c)
            node = new_node
    
    return new_node,d+1

nodes = {start,end}
edges1,edges2 = {},{}
Q = deque()
Q.append(start)

while Q:
    node = Q.popleft()
    for n1 in neighbours(node):
        p1 = True
        if n1[0]-node[0]==-1 or n1[1]-node[1]==-1:
            p1 = False
        arrival,d = explore(n1,node)
        if arrival not in nodes:
            nodes.add(arrival)
            Q.append(arrival)
        if node in edges2.keys():
            edges2[node].add((arrival,d))
        else:
            edges2[node]={(arrival,d)}
        if p1:
            if node in edges1.keys():
                edges1[node].add((arrival,d))
            else:
                edges1[node]={(arrival,d)}
      
t0 = time()
for p in [1,2]:
    def solve():
        ans = 0
        done = {}
        for node in nodes:
            done[node]=False
        def dfs(state,d):
            nonlocal count
            nonlocal ans
            if done[state]:
                return
            done[state]=True
            if state==end:
                ans=max(ans,d)
            else:
                for (arrival,d1) in edges[state]:
                    dfs(arrival,d+d1)
            done[state]=False
        dfs(start,0)
        return ans
    
    if p==1:
        edges = edges1
    else:
        edges = edges2
    ans = solve()

    print('part {}:'.format(p),ans)
print(time()-t0)