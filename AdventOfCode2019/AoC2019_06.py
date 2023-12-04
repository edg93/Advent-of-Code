with open("AoC2019_06_data.txt", "r") as file:
    data = file.read()

data = data.split('\n')

def distance(d,inside):
    for outside in orbits_io[inside]:
        satelites.add((outside,d+1))
        if outside in orbits_io.keys():
            distance(d+1,outside)
            
def path(satelite,p,origin):
    p.append(satelite)
    if satelite != 'COM':
        path(orbits_oi[satelite],p,origin)
    else:
        paths[origin]=p
    
satelites = {('COM',0)}
orbits_io = {}
orbits_oi = {}
paths = {}

for x in data:
    i,o=x.split(')')
    orbits_oi[o]=i
    if i in orbits_io.keys():
        orbits_io[i].add(o)
    else:
        orbits_io[i]={o}
    
distance(0,'COM')
ans1=0
for x,d in satelites:
    ans1+=d
    path(x,[],x)
print(ans1)

l1 = paths['YOU']
l2 = paths['SAN']
for i in range(1,len(l1)):
    if l1[len(l1)-i]!=l2[len(l2)-i]:
        print(len(l1)-i+len(l2)-i)
        break