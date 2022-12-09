from math import cos,sin
import math

f = open("data.txt", "r")
data = f.read()
data=data.split('\n')

ship=[0,0]
waypoint=[10,1]

for k in range(len(data)):
    instruction = data[k]
    if instruction[0]=='L':
        deg = int(instruction[1:])
        x,y=waypoint[0],waypoint[1]
        waypoint[0] = int(x*cos(deg*math.pi/180)) - int(y*sin(deg*math.pi/180))
        waypoint[1] = int(x*sin(deg*math.pi/180)) + int(y*cos(deg*math.pi/180))
    elif instruction[0]=='R':
        deg = -int(instruction[1:])
        x,y=waypoint[0],waypoint[1]
        waypoint[0] = int(x*cos(deg*math.pi/180)) - int(y*sin(deg*math.pi/180))
        waypoint[1] = int(x*sin(deg*math.pi/180)) + int(y*cos(deg*math.pi/180))
    elif instruction[0]=='N':
        waypoint[1]=waypoint[1]+int(instruction[1:])
    elif instruction[0]=='S':
        waypoint[1]=waypoint[1]-int(instruction[1:])
    elif instruction[0]=='E':
        waypoint[0]=waypoint[0]+int(instruction[1:])
    elif instruction[0]=='W':
        waypoint[0]=waypoint[0]-int(instruction[1:])
    elif instruction[0]=='F':
        ship[0] = ship[0] + waypoint[0]*int(instruction[1:])
        ship[1] = ship[1] + waypoint[1]*int(instruction[1:])

print(abs(ship[0])+abs(ship[1]))
