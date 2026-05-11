with open("AoC2018_25_data.txt", "r") as file:
    data = file.read()
    
data = data.splitlines()
points = [tuple([int(x) for x in line.split(',')]) for line in data]

def distance(p1, p2):
    return sum(abs(a-b) for a,b in zip(p1,p2))

constellations = []
for p in points:
    close = []
    for c in constellations:
        if any(distance(p,q) <= 3 for q in c):
            close.append(c)
    
    if not close:
        constellations.append({p})
    else:
        # merge all constellations + new point
        new_c = {p}
        for c in close:
            new_c |= c
            constellations.remove(c)
        constellations.append(new_c)


ans = len(constellations)
print(ans)
