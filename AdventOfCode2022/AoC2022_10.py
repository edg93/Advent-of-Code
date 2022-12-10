with open("AoC2022_10_data.txt", "r") as file:
    data = file.read()
data=data.strip().split('\n')

cycle = 1
ans1 = 0
sprite = 0
CRT = ''

def script(cycle,ans1,CRT,sprite):
    if (cycle-20)%40==0:
        ans1 += cycle*(sprite+1)
    if sprite<=len(CRT)<sprite+3:
        CRT += '#'
    else:
        CRT += ' '
    if cycle%40==0:
        print(CRT)
        CRT = ''
    cycle += 1
    return cycle,ans1,CRT

for line in data:
    cycle,ans1,CRT = script(cycle,ans1,CRT,sprite)
    if line != 'noop':
        cycle,ans1,CRT = script(cycle,ans1,CRT,sprite)
        sprite += int(line.split()[-1])

print(ans1)