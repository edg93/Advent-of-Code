"Day 9 of AOC2021"
with open("data.txt", "r") as file:
    data = file.read()
data = data.split('\n')

sol1 = 0
basins = []
R = len(data)
C = len(data[0])
DR = [-1,0,1,0]
DC = [0,1,0,-1]

def neighbors(points,r,c):
    neighbors = []
    for d in range(4):
        rr = r + DR[d]
        cc = c + DC[d]
        if 0<=rr<R and 0<=cc<C:
            neighbors+=[(rr,cc)]
    return neighbors

def check_basin(points,i,j,already_basin):
    for neighbor in neighbors(points,i,j):
        if neighbor not in already_basin:
            point1 = int(points[neighbor[0]][neighbor[1]])
            point = int(points[i][j])
            if point1 > point and point1 != 9:
                already_basin += [neighbor]
                check_basin(points,neighbor[0],neighbor[1],already_basin)
    return already_basin

for i in range(len(data)):
    for j in range(len(data[i])):
        n=int(data[i][j])
        vicini = [int(data[x[0]][x[1]]) for x in neighbors(data,i,j)]
        if n < min(vicini):
            sol1 += n+1
            basins += [len(check_basin(data,i,j,[(i,j)]))]

basins.sort()            
sol2 = basins[-1]*basins[-2]*basins[-3]

print(sol1)
print(sol2)