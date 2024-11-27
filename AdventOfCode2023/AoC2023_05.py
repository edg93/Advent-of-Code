from time import time

with open("AoC2023_05_data.txt", "r") as file:
    data = file.read()
    
data = data.split('\n\n')
seeds = [int(x) for x in data[0].split()[1:]]

ans1,ans2 = 10e11,0
maps,maps_rev = {},{}

for block in data[1:]:
    lines = block.split('\n')
    _from,_,_to = lines[0].split()[0].split('-')
    intervals = [[int(x) for x in y.split()] for y in lines[1:]]
    maps[_from]=[_to,intervals]
    maps_rev[_to]=[_from,intervals]

def solve(_from,n):
    if _from == 'location':
        return n
    else:
        n1 = None
        for interval in maps[_from][1]:
            if interval[1]<= n < interval[1]+interval[2]:
                n1 = interval[0]+n-interval[1]
        if not n1:
            n1=n
        
        return solve(maps[_from][0],n1)

def solve_rev(_to,n):
    if _to == 'seed':
        return n
    else:
        n1 = None
        for interval in maps_rev[_to][1]:
            if interval[0] <= n < interval[0]+interval[2]:
                n1 = interval[1]+n-interval[0]
        if not n1:
            n1=n
        
        return solve_rev(maps_rev[_to][0],n1)

for seed in seeds:
    loc = solve('seed',seed)
    if loc<ans1:
        ans1 = loc

t0=time()

c=0

while ans2==0:
    n = solve_rev('location',c)
    for i in range(len(seeds)):
        if i%2==0:
            if seeds[i] <= n < seeds[i]+seeds[i+1]:
                ans2 = c
    c+=1
        
print(time()-t0)

print(ans1,ans2)