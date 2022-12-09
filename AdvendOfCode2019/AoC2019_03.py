with open("AoC2019_03_data.txt", "r") as file:
    data = file.read()
    
path1,path2 = data.split('\n')

visited = set()
time_visits = {}
now = [0,0,0]
min_dist = 10e9
min_time = 10e9

def move(now,d):
    if d == 'U':
        return [now[0],now[1]+1,now[2]+1]
    elif d == 'R':
        return [now[0]+1,now[1],now[2]+1]
    elif d == 'D':
        return [now[0],now[1]-1,now[2]+1]
    elif d == 'L':
        return [now[0]-1,now[1],now[2]+1]
    
for instruction in path1.split(','):
    d,n = instruction[0],int(instruction[1:])
    for i in range(n):
        now = move(now,d)
        visited.add((now[0],now[1]))
        if (now[0],now[1]) not in time_visits.keys():
            time_visits[(now[0],now[1])]=now[2]
            
now = [0,0,0]
for instruction in path2.split(','):
    d,n = instruction[0],int(instruction[1:])
    for i in range(n):
        now = move(now,d)
        if  (now[0],now[1]) in visited:
            if abs(now[0])+abs(now[1])<min_dist:
                min_dist = abs(now[0])+abs(now[1])
            if time_visits[(now[0],now[1])]+now[2] < min_time:
                min_time = time_visits[(now[0],now[1])]+now[2]
          
print(min_dist)
print(min_time)