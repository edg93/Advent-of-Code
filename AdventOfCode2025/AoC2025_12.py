
with open("AoC2025_12_data.txt", "r") as f:
    data = f.read()
    
ans = 0
    
data = data.split('\n\n')
presents = {}
presents_dim = {}

for part in data[:-1]:
    n,present = part.split(':\n')
    n = int(n)
    
    presents_dim[n] = present.count('#')
    present = present.split('\n')
    presents[n]=present
    
regions = data[-1].split('\n')


for region in regions:
    area, quantities = region.split(': ')
    R,C = [int(x) for x in area.split('x')]
    area = R*C
    quantities = [int(x) for x in quantities.split(' ')]
    
    space_needed = 0
    for i,quantity in enumerate(quantities):
        space_needed += quantity*presents_dim[i]
    
    if space_needed>area:
        continue
    
    ans +=1

print(ans)