with open("AoC2023_21_data.txt", "r") as file:
    data = file.read()

data = data.split('\n')
R,C = len(data),len(data[0])
DIR = [(0,1),(1,0),(-1,0),(0,-1)]

rocks = set()
for r,line in enumerate(data):
    for c,ch in enumerate(line):
        if ch=='#':
            rocks.add((r,c))
        elif ch=='S':
            points = {(r,c)}

def move(points):
    new_points = set()
    for point in points:
        for d in DIR:
            if 0<=point[0]+d[0]<R and 0<=point[1]+d[1]<C and (point[0]+d[0],point[1]+d[1]) not in rocks:
                new_points.add((point[0]+d[0],point[1]+d[1]))
    return new_points

for _ in range(3649):
    points = move(points)
    print(_+1, len(points))
