with open("AoC2015_03_data.txt", "r") as file:
     data = file.read()
     
ans = [0,0]

pos = (0,0)
houses_1 = set()
houses_1.add(pos)

directions ={'>':(1,0),'<':(-1,0),'^':(0,1),'v':(0,-1)}

for ch in data:
    dx,dy = directions[ch]
    pos = (pos[0]+dx,pos[1]+dy)
    houses_1.add(pos)


pos_santa = (0,0)
pos_robot = (0,0)
houses_2 = set()
houses_2.add(pos_santa)
for i,ch in enumerate(data):
    dx,dy = directions[ch]
    if i%2==0:
        pos_santa = (pos_santa[0]+dx,pos_santa[1]+dy)
        houses_2.add(pos_santa)
    else:
        pos_robot = (pos_robot[0]+dx,pos_robot[1]+dy)
        houses_2.add(pos_robot)

ans[0]=len(houses_1)
ans[1]=len(houses_2)

print(ans)