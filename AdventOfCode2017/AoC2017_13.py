with open('AoC2017_13_data.txt', "r") as f:
    data = f.read()

data = data.splitlines()

ans = [0,0]
scanners = {}

for line in data:
    r,depth = line.split(': ')
    scanners[int(r)] = int(depth)
    
for scanner,depth in scanners.items():
    if scanner % ((depth - 1) * 2) == 0:
        ans[0]+=scanner*depth
    
t = 0
while True:
    caught = False
    for scanner,depth in scanners.items():
        if (scanner + t) % ((depth - 1) * 2) == 0:
            caught = True
            break
    if not caught:
        ans[1] = t
        break
    t += 1
    
print(ans)