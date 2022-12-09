"Day 21 of AOC2021"
with open("data.txt", "r") as file:
    data = file.read()
    
data = data.split('\n')

lights = {}

for line in data:
    a,line = line.split(' ')
    x,y,z = line.split(',')
    dx = [int(i) for i in x[2:].split('..')]
    dy = [int(i) for i in y[2:].split('..')]
    dz = [int(i) for i in z[2:].split('..')]
    print(dx,dy,dz)
    if (-51<dx[0]<51 and -51<dy[0]<51 and -51<dz[0]<51) or (-51<dx[1]<51 and -51<dy[1]<51 and -51<dz[1]<51):
        for x in range(dx[0],dx[1]+1):
            for y in range(dy[0],dy[1]+1):
                for z in range(dz[0],dz[1]+1):
                    
                    if a=='on':
                        lights[(x,y,z)]='on'
                    else:
                        lights[(x,y,z)]='off'

sol1=0                
for point in lights:
    if lights[point]=='on':
        sol1+=1
        
        
print(sol1)

lights = []

for line in data:
    a,line = line.split(' ')
    x,y,z = line.split(',')
    dx = [int(i) for i in x[2:].split('..')]
    dy = [int(i) for i in y[2:].split('..')]
    dz = [int(i) for i in z[2:].split('..')]
    if len(lights)==0:
        lights = [(dx,dy,dz)]
    else:
        new_cubes = [(dx,dy,dz)]
        cut=True
        while cut:
            cut=False
            for c in new_cubes:
                for cube in lights:
                    if (cube[0][0]<c[0][1] and cube[0][1]>c[0][0]) and (cube[1][0]<c[1][1] or cube[1][1]>c[1][0]) and (cube[2][0]<c[2][1] or cube[2][1]>c[2][0]):
                        if a == 'on':
                            new_cubes.remove(c)
                            x_int = [max(c[0][0],cube[0][0]),min(c[0][1],cube[0][1])]
                            y_int = [max(c[1][0],cube[1][0]),min(c[1][1],cube[1][1])]
                            z_int = [max(c[2][0],cube[2][0]),min(c[2][1],cube[2][1])]
                            
                            to_add = set()
                            #devo aggiungerne 6
                                
                                
                            for i in to_add:
                                if i[0][0]!=i[0][1] and i[1][0]!=i[1][1] and i[2][0]!=i[2][1]:
                                    new_cubes += [i]
                            cut = True
                            break
                        else:
                            
                if cut:
                    break

sol2=0                
for c in lights:
    sol2+= (c[0][1]-c[0][0]+1)*(c[1][1]-c[1][0]+1)*(c[2][1]-c[2][0]+1)
        
        
print(sol1)