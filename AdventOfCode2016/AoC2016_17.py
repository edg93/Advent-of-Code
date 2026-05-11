from collections import deque
from hashlib import md5

doors_DIR = {'U':(0,-1),'D':(0,1),'L':(-1,0),'R':(1,0)}

data = 'pslxynzg'
ans = [None,None]

x,y = 0,0

Q = deque([])
Q.append((x,y,''))

def open_doors(s):
    result = []
    s = md5((data+s).encode()).hexdigest()
    for i,d in enumerate('UDLR'):
        if s[i] in 'bcdef':
            result.append(d)
    return result


while Q:
    x,y,s = Q.popleft()
    if (x,y) == (3,3):
        if not ans[0]:
            ans[0]=s
        ans[1] = len(s)
        continue

    for door in open_doors(s):
        dx,dy = doors_DIR[door]
        if 0<=x+dx<4 and 0<=y+dy<4:
            Q.append((x+dx,y+dy,s+door))

print(ans)