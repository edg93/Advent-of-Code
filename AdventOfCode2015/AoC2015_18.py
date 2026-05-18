with open("AoC2015_18_data.txt", "r") as file:
    data = file.read()
data = data.split('\n')
    
ans = [0,0]

d = [(1,-1),(1,0),(1,1),(0,-1),(0,1),(-1,-1),(-1,0),(-1,1)]
R,C = len(data),len(data[0])

lights = {(r,c) for r in range(R) for c in range(C) if data[r][c] == '#'}
lights_1 = set(lights)
          
def count_neighbors(lights,r,c):
    count = 0
    for dr,dc in d:
        if (r+dr,c+dc) in lights:
            count+=1
    return count

def update(lights,second_part = False):
    if second_part:
        new_lights = {(0,0),(0,C-1),(R-1,0),(R-1,C-1)}
    else:
        new_lights = set()
    for (r,c) in lights:
        count = count_neighbors(lights,r,c)
        if count in [2,3]:
            new_lights.add((r,c))
            
        for dr,dc in d:
            if 0<=r+dr<R and 0<=c+dc<C and (r+dr,c+dc) not in lights and count_neighbors(lights,r+dr,c+dc)==3:
                new_lights.add((r+dr,c+dc))
    return new_lights

def output(lights):
    for r in range(R):
        s=''
        for c in range(C):
            if (r,c) in lights:
                s+='#'
            else:
                s+='.'
        print(s)

for _ in range(100):
    lights = update(lights)
    lights_1 = update(lights_1,True)

ans[0]=len(lights)
ans[1]=len(lights_1)
print(ans)