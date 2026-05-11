from collections import defaultdict
from IntcodeComputer import intcode_vm
with open("AoC2019_19_data.txt", "r") as file:
    data = file.read()
    
data = [int(x) for x in data.split(',')]

ans = [0,None]
d = defaultdict(int)
for n,i in enumerate(data):
    d[n]=i
    
dim = 50

for y in range(50):
    for x in range(50):
        vm = intcode_vm(d.copy(), [x, y])
        response = next(vm)   # exactly one output
        if response == 1:
            ans[0] += 1
            

def beam_at(x, y):
    vm = intcode_vm(d.copy(), [x, y])
    return next(vm)

x,y = 300,0
while beam_at(x, y) == 0:
    y += 1

while True:
    while beam_at(x, y) == 0:
        x += 1

    if beam_at(x + 99, y - 99) == 1:
        ans[1] = x * 10000 + (y - 99)
        break

    y += 1
    
print(ans)