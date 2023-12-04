from math import gcd
positions = [[-15,1,4],[1,-10,-8],[-5,4,9],[4,6,-2]]
#positions = [[-1,0,2],[2,-10,-7],[4,-8,8],[3,5,-1]] #test
#positions = [[-8,-10,0],[5,5,10],[2,-7,3],[9,-8,-3]] #test

velocities = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]]

N = len(positions)

d = set()

def update(positions,velocities):
    for n in range(N):
        for n1 in range(N):
            if n!=n1:
                for x in range(3):
                    if positions[n][x]>positions[n1][x]:
                        velocities[n][x] -= 1
                    elif positions[n][x]<positions[n1][x]:
                        velocities[n][x] += 1
    for n in range(N):
        for x in range(3):
            positions[n][x] += velocities[n][x]
    return positions,velocities

def energy(pos,vel):
    E = 0
    for n in range(N):
        (x,y,z) = pos[n]
        P = abs(x)+abs(y)+abs(z)
        (x,y,z) = vel[n]
        K = abs(x)+abs(y)+abs(z)
        E += K*P
    return E

d = [set(),set(),set()]
found = [False,False,False]
i=0
while True:
    i+=1
    for k in range(3):
        if not found[k] and tuple([x[k] for x in positions+velocities]) in d[k]:
            found[k]=i-1
        d[k].add(tuple([x[k] for x in positions+velocities]))
    positions,velocities = update(positions,velocities)
    if i==1000:
        print(energy(positions,velocities))
    if found[0] and found[1] and found[2]:
        break
    
temp = found[0]*found[1]//gcd(found[0],found[1]) 
print(temp*found[2]//gcd(temp,found[2]))