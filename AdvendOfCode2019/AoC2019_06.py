with open("AoC2019_06_data.txt", "r") as file:
    data = file.read()

data = data.split('\n')

def add_orbits(d,o,orbits_toAdd,done):
    for i in d[o]:
        if i in d.keys() and i not in done:
            done.add(i)
            orbits_toAdd = orbits_toAdd | add_orbits(d,i,orbits_toAdd,done)
            return add_orbits(d,o,orbits_toAdd,done)
        else:
            return orbits_toAdd

orbits = set()
orbits_dict = {}

for x in data:
    i,o=x.split(')')
    if o in orbits_dict.keys():
        orbits_dict[o].add(i)
    else:
        orbits_dict[o]={i}
for x in data:
    i,o=x.split(')')
    for obj in add_orbits(orbits_dict,o,set(),set()):
        orbits_dict[o].add(obj)
    for obj in orbits_dict[o]:
        orbits.add((obj,o))
        
print(len(orbits))