with open("AoC2021_22_ex.txt", "r") as file:
    data = file.read()
    
data = data.split('\n')

lights = {}

for line in data:
    a,line = line.split(' ')
    x,y,z = line.split(',')
    dx = [int(i) for i in x[2:].split('..')]
    dy = [int(i) for i in y[2:].split('..')]
    dz = [int(i) for i in z[2:].split('..')]
    if -51<dx[0]<51 and -51<dy[0]<51 and -51<dz[0]<51 and -51<dx[1]<51 and -51<dy[1]<51 and -51<dz[1]<51:
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
            for nX,nY,nZ in new_cubes:
                for X,Y,Z in lights:
                    if (X[0]<nX[1] or X[1]>nX[0]) and (Y[0]<nY[1] or Y[1]>nY[0]) and (Z[0]<nZ[1] or Z[1]>nZ[0]):
                        if a == 'on':
                            new_cubes.remove((nX,nY,nZ))
                            x_int = [max(nX[0],X[0]),min(nX[1],X[1])]
                            y_int = [max(nY[0],Y[0]),min(nY[1],Y[1])]
                            z_int = [max(nZ[0],Z[0]),min(nZ[1],Z[1])]
                            
                            to_add = set()
                            #devo aggiungerne 6
                                
                            for cube in to_add:
                                if cube[0][0]!=cube[0][1] and cube[1][0]!=cube[1][1] and cube[2][0]!=cube[2][1]:
                                    new_cubes.append(cube)
                            cut = True
                            break
                            
                if cut:
                    break

sol2=0                
for c in lights:
    sol2+= (c[0][1]-c[0][0]+1)*(c[1][1]-c[1][0]+1)*(c[2][1]-c[2][0]+1)
        
print(sol2)