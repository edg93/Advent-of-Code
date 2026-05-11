from collections import Counter
with open("AoC2017_20_data.txt", "r") as f:
    data = f.read()
    
data = data.splitlines()
ans = [0,0]

def parsing(data):
    particles = {}
    for i,line in enumerate(data):
        p,v,a = line.split(', ')
        p = [int(x) for x in p[3:-1].split(',')]
        v = [int(x) for x in v[3:-1].split(',')]
        a = [int(x) for x in a[3:-1].split(',')]
        particles[i] =(tuple(p),tuple(v),tuple(a))
    return particles

def d(p):
    x,y,z = p
    return abs(x)+abs(y)+abs(z)

def tick(particles,part1):
    min_distance = 10e10
    closest = None
    for n,(p,v,a) in particles.items():
        vx,vy,vz = v
        ax,ay,az = a
        vx,vy,vz = vx+ax, vy+ay, vz+az
        x,y,z = p
        p = x+vx, y+vy, z+vz
        v = vx,vy,vz
        particles[n] = (p,v,a)
        if d(p) < min_distance:
            min_distance = d(p)
            closest = n
        
    if part1:
        return particles,closest
    else:
        positions = Counter(p for p,_,_ in particles.values())
        to_remove = {n for n,(p,_,_) in particles.items() if positions[p] > 1}
        for n in to_remove:
            del particles[n]
        return particles,len(particles)
        
particles = parsing(data)
stable_count = 0
prev_closest = None
while stable_count < 300:  # arbitrary: 300 ticks with same closest particle
    particles,closest = tick(particles,True)
    if closest == prev_closest:
        stable_count += 1
    else:
        stable_count = 0
    prev_closest = closest
    
ans[0] = closest

particles = parsing(data)
prev_n = None
stable_count = 0
while stable_count < 300:  # arbitrary: 300 ticks with the same surviving particles
    particles,n = tick(particles,False)
    if n == prev_n:
        stable_count += 1
    else:
        stable_count = 0
    prev_n = n
    
ans[1] = n
print(ans)