from math import cos,sin,pi

with open("AoC2020_12_data.txt", "r") as file:
    data = file.read()
data=data.split('\n')

position = [0,0]
orientation = 90

DIR = {0:'N',90:'E',180:'S',270:'W'}

def move(position,orientation,ins,n):
    if ins=='L':
        orientation=(orientation-n)%360
    elif ins=='R':
        orientation=(orientation+n)%360
    elif ins=='N':
        position[1]+=n
    elif ins=='S':
        position[1]-=n
    elif ins=='E':
        position[0]+=n
    elif ins=='W':
        position[0]-=n
    elif ins=='F':
        position,orientation = move(position,orientation,DIR[orientation],n)
    return position,orientation

def move_part2(ship,waypoint,ins,n):
    if ins=='L':
        x,y=waypoint[0],waypoint[1]
        waypoint[0] = int(x*cos(n*pi/180)) - int(y*sin(n*pi/180))
        waypoint[1] = int(x*sin(n*pi/180)) + int(y*cos(n*pi/180))
    elif ins =='R':
        x,y=waypoint[0],waypoint[1]
        waypoint[0] = int(x*cos(-n*pi/180)) - int(y*sin(-n*pi/180))
        waypoint[1] = int(x*sin(-n*pi/180)) + int(y*cos(-n*pi/180))
    elif ins =='N':
        waypoint[1] += n
    elif ins =='S':
        waypoint[1] -= n
    elif ins =='E':
        waypoint[0] += n
    elif ins =='W':
        waypoint[0] -= n
    elif ins =='F':
        ship[0] += waypoint[0]*n
        ship[1] += waypoint[1]*n
    return ship,waypoint
            
for line in data:
    ins,n = line[0],int(line[1:])
    position,orientation = move(position,orientation,ins,n)
  
print(abs(position[0])+abs(position[1]))

ship=[0,0]
waypoint=[10,1]

for line in data:
    ins,n = line[0],int(line[1:])
    ship,waypoint = move_part2(ship,waypoint,ins,n)
    
print(abs(ship[0])+abs(ship[1]))
