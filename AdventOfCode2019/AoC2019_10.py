with open("AoC2019_10_data.txt", "r") as file:
    data = file.read()

data = data.split('\n')

asteroids = set()

for r,line in enumerate(data):
    for c,x in enumerate(line):
        if x=='#':
            asteroids.add((c,r))
            
d={}

for a in asteroids:
    d[a]=set()
    c1,r1 = a
    for c2,r2 in asteroids-{a}:
        if c2==c1:
            d[a].add((1e9,r1>r2))
        else:
            d[a].add(((r1-r2)/(c2-c1),c2>c1))
        
ans1 = 0   
c1,r1 = 0,0    

for x in d.keys():
    if len(d[x])>ans1:
        ans1 = len(d[x])
        c1,r1 = x
    
print(ans1)

def insert(key):
    if key in d1.keys():
        dist = ((c1-c2)**2+(r1-r2)**2)**0.5
        ok = False
        for n,(c3,r3) in enumerate(d1[key]):
            dist1 = ((c1-c3)**2+(r1-r3)**2)**0.5
            if dist>dist1:
                d1[key]=d1[key][:n]+[(c2,r2)]+d1[key][n:]
                ok = True
                break
        if not ok:
            d1[key].append((c2,r2))
    else:
        d1[key]=[(c2,r2)]

d1 = {}
for c2,r2 in asteroids-{(c1,r1)}:
    if c2==c1:
        key = (1e9,r1>r2)
        insert(key)
    else:
        key = ((r1-r2)/(c2-c1),c2>c1)
        insert(key)

directions = list(d1.keys())

l1,l2 = [],[]
for direction in directions:
    if direction[1]==True:
        l1.append(direction)
    else:
        l2.append(direction)
l1.sort(reverse=True)
l2.sort(reverse=True)
directions = l1+l2

r,c=d1[directions[199]][-1]
print(r*100+c)