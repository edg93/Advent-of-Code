with open("AoC2021_02_data.txt", "r") as file:
    data = file.read()
data=data.split('\n')

h1,d1=0,0
h2,d2,aim=0,0,0

for line in data:
    cmd, n = line.split(' ')
    if cmd == 'forward':
        h1 += int(n)
        h2 += int(n)
        d2 += aim*int(n)
    elif cmd == 'up':
        d1 -= int(n)
        aim -= int(n)
    elif cmd == 'down':
        d1 += int(n)
        aim += int(n)
        
print(h1*d1)
print(h2*d2)