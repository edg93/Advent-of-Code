from collections import defaultdict, deque
from time import sleep

with open("AoC2024_14_data.txt", "r") as file:
    data = file.read()
    
data = data.split('\n')
X,Y = 101,103
#X,Y = 11,7

t = 100
ans1,ans2=0,0    

def show(robots):
    for r in range(Y):
        s = ''
        for c in range(X):
            if (c,r) in robots:
                s+='*'
            else:
                s+='.'
        print(s)

robots_set = set()
t=0

while len(robots_set)!=len(data):
    t+=1
    robots_set = set()
    robots = []
    for line in data:
        p,v = [x.split('=')[1] for x in line.split(' ')]
        x0,y0 = [int(x) for x in p.split(',')]
        vx,vy = [int(x) for x in v.split(',')]
        
        xf = (x0+t*vx)%X
        yf = (y0+t*vy)%Y
        robots.append((xf,yf))
        robots_set.add((xf,yf))
    if t==100:
        s0,s1,s2,s3 = 0,0,0,0
        
        for x,y in robots:
            if 0<=x<X//2:
                if 0<=y<Y//2:
                    s0+=1
                elif Y//2<y<Y:
                    s1+=1
            elif X//2<x<X:
                if 0<=y<Y//2:
                    s2+=1
                elif Y//2<y<Y:
                    s3+=1
                    

ans1 = s0*s1*s2*s3
ans2 = t
print(ans1,ans2)