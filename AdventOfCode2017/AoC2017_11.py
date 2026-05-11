with open('AoC2017_11_data.txt', "r") as f:
    data = f.read()


data = data.split(',')
ans = [0,0]

DIR = {'n':(0,1,-1),'ne':(1,0,-1),'se':(1,-1,0),'s':(0,-1,1),'sw':(-1,0,1),'nw':(-1,1,0)}

x,y,z = 0,0,0
def hex_distance(x,y,z):
    return (abs(x) + abs(y) + abs(z))//2

for d in data:
    dx,dy,dz = DIR[d]
    x+=dx
    y+=dy
    z+=dz
    ans[1] = max(ans[1],hex_distance(x,y,z))

ans[0] = hex_distance(x,y,z)
print(ans)