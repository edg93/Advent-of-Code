"Day 13 of AOC2021"
with open("data.txt", "r") as file:
    data = file.read()
points, instructions = data.split('\n\n')
points = points.split('\n')
instructions = instructions.split('\n')

for i in range(len(points)):
    points[i] = [int(x) for x in points[i].split(',')]
    

for i in range(len(instructions)):
    instructions[i] = instructions[i].split(' ')[2]
    instructions[i] = [instructions[i].split('=')[0],int(instructions[i].split('=')[1])]
    
def step(points,instruction):
    line = instruction[1]
    if instruction[0]=='x':
        for i in range(len(points)):
            if points[i][0]>line:
                points[i][0]=2*line-points[i][0]
    else:
        for i in range(len(points)):
            if points[i][1]>line:
                points[i][1]=2*line-points[i][1]
    return points

def count(points):
    p_set = set()
    for p in points:
        p_set.add((p[0],p[1]))
    return (len(p_set))

for instruction in instructions:
    points = step(points,instruction)
    print(count(points))
    
def draw(points):
    XX = max(points, key=lambda points: points[0])[0]
    YY = max(points, key=lambda points: points[1])[1]
    M = [['-' for y in range(XX+1)] for x in range(YY+1)]
    for point in points:
        x,y = point
        M[y][x] = '#'
    for line in M:
        print(line)

draw(points)