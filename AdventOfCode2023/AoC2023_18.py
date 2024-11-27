with open("AoC2023_18_data.txt", "r") as file:
    data = file.read()

data = data.split('\n')
ans1,ans2=0,0

dir_dict = {'U':(-1,0),'D':(1,0),'L':(0,-1),'R':(0,1),'3':(-1,0),'1':(1,0),'2':(0,-1),'0':(0,1)}

points1,points2 = [],[]
point1,point2 = (0,0),(0,0)

for line in data:
    _dir,l,colour = line.split()
    dr,dc = dir_dict[_dir]
    points1.append((point1[0]+dr*(int(l)),point1[1]+dc*(int(l))))
    point1 = points1[-1]
    _dir = colour[-2]
    dr,dc = dir_dict[_dir]
    l = int(colour[2:-2],16)
    points2.append((point2[0]+dr*(int(l)),point2[1]+dc*(int(l))))
    point2 = points2[-1]
    
def area(points):
    area = 0
    for x in range(len(points)):
        area += points[x][0]*(points[(x+1)%len(points)][1]-points[x-1][1])
    return abs(area)/2   

def perimeter(points):
    p = 0
    for x in range(len(points)):
        p+= abs(points[x-1][0]-points[x][0]+points[x-1][1]-points[x][1])
    return p

ans1 = int(area(points1) + perimeter(points1)/2 +1)
ans2 = int(area(points2) + perimeter(points2)/2 +1)
print(ans1,ans2)