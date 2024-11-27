from collections import deque
from time import time

with open("AoC2023_12_data.txt", "r") as file:
    data = file.read()

data = data.split('\n')

ans1,ans2=0,0

def check(springs,groups):
    springs += '.'
    c1,c2=0,0
    l = len(groups)
    for symbol in springs:
        if c2>=l:
            if symbol == '#':
                return False
        if symbol=='#':
            c1 += 1
        elif c1>0 and symbol!='#':
            if c1 != groups[c2]:
                return False
            else:
                c1=0
                c2+=1

    if c2!=l and c1 !=groups[c2]:
        return False
    return True

t0 = time()
for j,line in enumerate(data):
    if j%20==0:    
        print(j)
    springs, groups = line.split()
    groups = [int(x) for x in groups.split(',')]
    Q = deque()
    Q.append(springs)
    sum_groups = sum(groups)
    l = len (springs)
    while Q:
        s = Q.popleft()
        c0,c1=0,0
        for i,ch in enumerate(s):
            if ch == '#':
                c0+=1
            elif ch == '?':
                Q.append(s[:i]+'#'+s[i+1:])
                Q.append(s[:i]+'.'+s[i+1:])
                break
            else:
                c1+=1
            if c0 == sum_groups:
                ans2+=1
                if check(s,groups):
                    ans1+=1
                break
            if l-c1<sum_groups:
                break

print(ans1,ans2)
print(time()-t0)

ans1,ans2=0,0
for j,line in enumerate(data):
    if j%20==0:    
        print(j)
    springs, groups = line.split()
    groups = [int(x) for x in groups.split(',')]
    springs = springs + '?' + springs + '?' + springs
    groups *=3
    Q = deque()
    Q.append(springs)
    sum_groups = sum(groups)
    l = len (springs)
    while Q:
        s = Q.popleft()
        c0,c1=0,0
        for i,ch in enumerate(s):
            if ch == '#':
                c0+=1
            elif ch == '?':
                Q.append(s[:i]+'#'+s[i+1:])
                Q.append(s[:i]+'.'+s[i+1:])
                break
            else:
                c1+=1
            if c0 == sum_groups:
                ans2+=1
                if check(s,groups):
                    ans1+=1
                break
            if l-c1<sum_groups:
                break

print(ans1,ans2)
print(time()-t0)
