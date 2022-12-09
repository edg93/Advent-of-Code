"Day 19 of AOC2021"
from time import time
from copy import copy
with open("data.txt", "r") as file:
    data = file.read()
    
data = data.split('\n\n')

t = time()
scanners = {}

for i in range(len(data)):
    data[i]=data[i].split('\n')
    key = data[i][0].strip('--- scanner')
    value = set()
    for x in data[i][1:]:
        x = [int(y) for y in x.split(',')]
        value.add(tuple(x))
    scanners[int(key)]=value
    
beacons = set()
for b in scanners[0]:
    beacons.add(b)
    
def compare(s1,s2):
    for s in s1:
        for t in s2:
            x=s[0]-t[0]
            y=s[1]-t[1]
            z=s[2]-t[2]
            counter=1
            for ss in s1:
                for tt in s2:
                    if ss[0]-tt[0]==x and ss[1]-tt[1]==y and ss[2]-tt[2]==z:
                        counter+=1
            if counter>11:
                return True,(x,y,z)
    return False,None

def orientations(s):
    o = []
    for x in [-1,1]:
        for y in [-1,1]:
            for z in [-1,1]:
                for i in range(3):
                    new_s=set()
                    if x*y*z==1:
                        for ss in s:
                            new_s.add((ss[(0+i)%3]*x, ss[(1+i)%3]*y, ss[(2+i)%3]*z))
                    else:
                        for ss in s:
                            new_s.add((ss[(0+i)%3]*x, ss[(2+i)%3]*y, ss[(1+i)%3]*z))
                    o.append(new_s)
    return o

done = set([(0,(0,0,0))])
to_do = set([i+1 for i in range(len(scanners)-1)])
done_pairs = set([(x,x) for x in range(len(scanners))])
to_add = set([(0,(0,0,0))]) 

while to_do:
    last_add = copy(to_add)
    to_add = set()
    for j in last_add:
        for i in to_do:
            if (i,j[0]) in done_pairs or (j[0],i) in done_pairs:
                continue
            for s in orientations(scanners[i]):
                ok, diff = compare(scanners[j[0]],s)
                done_pairs.add((i,j[0]))
                if ok:
                    scanners[i]=s
                    diff = (j[1][0]+diff[0], j[1][1]+diff[1], j[1][2]+diff[2])
                    for x in s:
                        translated_x = (x[0]+diff[0],x[1]+diff[1],x[2]+diff[2])
                        beacons.add(translated_x)
                    to_add.add((i,diff))
                    print(len(to_do))
                    break
    done = done | to_add
    to_do = to_do-set([x[0] for x in to_add])

m=0
for x in done:
    x=x[1]
    for y in done:
        y=y[1]
        d = abs(x[0]-y[0])+abs(x[1]-y[1])+abs(x[2]-y[2])
        if d>m:
            m=d
            
print(len(beacons))
print(m)
print(time()-t)