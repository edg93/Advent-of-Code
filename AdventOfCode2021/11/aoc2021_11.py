"Day 11 of AOC2021"
with open("data.txt", "r") as file:
    data = file.read()
data = data.split('\n')
for i in range(len(data)):
    data[i]=list(data[i])
    for j in range(len(data[i])):
        data[i][j]=int(data[i][j])
        
def update(octopus):
    for r in range(len(octopus)):
        for c in range(len(octopus[r])):
            octopus[r][c]+=1
    return octopus
            
def flash(octopus,n_flash):
    flashed= False
    for r in range(len(octopus)):
        for c in range(len(octopus[0])):
            if octopus[r][c]>9:
                octopus[r][c]=0
                n_flash += 1
                for dr in [-1,0,1]:
                    rr = r + dr
                    for dc in [-1,0,1]:
                        cc = c + dc
                        if 0<=rr<len(octopus) and 0<=cc<len(octopus[0]) and octopus[rr][cc]!=0:
                            octopus[rr][cc]+=1
                            flashed=True
    return octopus, flashed, n_flash

def show(octopus):
    for line in octopus:
        print(' '.join([str(x) for x in line]))
        
def turn(octopus,n_flash):
    everybody_flashed = False
    octopus = update(octopus)
    flashed = True
    old_flash=n_flash
    while flashed:
        octopus,flashed,n_flash = flash(octopus,n_flash)
    if n_flash-old_flash == len(octopus)*len(octopus[0]):
        everybody_flashed=True
    return octopus, n_flash, everybody_flashed
        
n_flash=0

for n in range(1000):
    data,n_flash,everybody_flashed= turn(data,n_flash)
    if n==99:
        print(n_flash)
    if everybody_flashed:
        print(n+1)
        break

                
                
        