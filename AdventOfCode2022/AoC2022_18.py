with open("AoC2022_18_data.txt", "r") as file:
    data = file.read()
data=data.strip().split('\n')

cubes = set()

Z = [1e7,-1e7]
Y = [1e7,-1e7]
X = [1e7,-1e7]

for line in data:
    coord = tuple([int(x) for x in line.split(',')])
    cubes.add(coord)
    Z[0]=min(Z[0],coord[2])
    Z[1]=max(Z[1],coord[2])
    Y[0]=min(Y[0],coord[2])
    Y[1]=max(Y[1],coord[2])
    X[0]=min(X[0],coord[2])
    X[1]=max(X[1],coord[2])

def is_inside(point,volume):
    x,y,z = point
    if x<X[0] or x>X[1] or y<Y[0] or y>Y[1] or z<Z[0] or z>Z[1]:
        return False
    t = True
    for dx in [-1,0,1]:
        for dy in [-1,0,1]:
            for dz in [-1,0,1]:
                if dx==dy==0 or dx==dz==0 or dy==dz==0:
                    p1 = (x+dx,y+dy,z+dz)
                    if p1 not in volume and p1 not in cubes:
                        volume.add(p1)
                        t = t and is_inside(p1,volume)
    return t         

def show_layer(z):
    print(z)
    for y in range(Y[0],Y[1]+1):
        raw = ''
        for x in range(X[0],X[1]+1):
            if (x,y,z) in cubes:
                raw+='#'
            else:
                raw += ' '
        print(raw)

def show(cubes):
    for z in range(Z[0],Z[1]):
        show_layer(z)
        
ans1,ans2=0,0

for cube in cubes:
    n1,n2 = 0,0
    for x in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]:
        p = (cube[0]+x[0],cube[1]+x[1],cube[2]+x[2])
        if p not in cubes:
            n1+=1
            if not is_inside(p,set(p)):
                n2+=1
    ans1 += n1
    ans2 += n2
    
print(ans1)
print(ans2)