from collections import deque

with open("AoC2022_19_data.txt", "r") as file:
    data = file.read()
data=data.strip().split('\n')

def find_max(line,T):
    line = line.split()
    ore_cost = int(line[6])
    clay_cost = int(line[12])
    obs_cost = int(line[18]),int(line[21])
    geo_cost = int(line[-5]),int(line[-2])
    Q = deque([(1,0,0,0,0,0,0,0,T)])
    already_in_line = set()
    M=0
    while Q:
        r_ore,r_c,r_obs,r_g,ore,c,obs,g,t = Q.popleft()
        if (r_ore,r_c,r_obs,r_g,ore,c,obs,g,t) in already_in_line:
            continue
        already_in_line.add((r_ore,r_c,r_obs,r_g,ore,c,obs,g,t))
        if t==0:
            M = max(M,g)
            continue
        if t>1 and ore >= geo_cost[0] and obs >= geo_cost[1]:
            Q.append((r_ore,r_c,r_obs,r_g+1,ore+r_ore-geo_cost[0],c+r_c,obs+r_obs-geo_cost[1],g+r_g,t-1))
            continue
        if t>3 and ore >= obs_cost[0] and c >= obs_cost[1]:    
            Q.append((r_ore,r_c,r_obs+1,r_g,ore+r_ore-obs_cost[0],c+r_c-obs_cost[1],obs+r_obs,g+r_g,t-1))
        if t>5 and ore >= clay_cost:
            Q.append((r_ore,r_c+1,r_obs,r_g,ore+r_ore-clay_cost,c+r_c,obs+r_obs,g+r_g,t-1))
        if t>7 and ore >= ore_cost:
            Q.append((r_ore+1,r_c,r_obs,r_g,ore+r_ore-ore_cost,c+r_c,obs+r_obs,g+r_g,t-1))
        else:
            Q.append((r_ore,r_c,r_obs,r_g,ore+r_ore,c+r_c,obs+r_obs,g+r_g,t-1))
    return M

ans1 = 0
ans2 = 1
for n,line in enumerate(data):
    M1 = find_max(line,24)
    if n<3:
        M2 = find_max(line,32)
        ans2*=M2
    ans1+=M1*(n+1)
    print(n+1,M1,ans1)
print(ans1)
print(ans2)