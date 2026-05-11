with open("AoC2018_10_data.txt", "r") as f:
    data = f.read()        
    
data = data.split('\n')
points = set()
time=0

for line in data:
    pos,v = line.split('> velocity=<')
    pos = pos.split('position=<')[1]
    x,y = [int(i) for i in pos.split(', ')]
    vx,vy = [int(i) for i in v[:-1].split(', ')]
    points.add((x,y,vx,vy))

def output(points):
    X = [min(x for x,_,_,_ in points),max(x for x,_,_,_ in points)]
    Y = [min(y for _,y,_,_ in points),max(y for _,y,_,_ in points)]
    points_temp = {(x, y) for x, y, _, _ in points}
    for y in range(Y[0],Y[1]+1):
        s = ''
        for x in range(X[0],X[1]+1):
            if (x,y) in points_temp:
                s+='#'
            else:
                s+='.'
        print(s)
      
def is_compact(points):
    Y = [min(y for _,y,_,_ in points),max(y for _,y,_,_ in points)]
    if Y[1]-Y[0]<10:
        output(points)
        return True
    return False

def step(points):
    new_points = set()
    for x,y,vx,vy in points:
        new_points.add((x+vx,y+vy,vx,vy))
    return new_points

while not is_compact(points):
    time+=1
    points = step(points)
print(time)