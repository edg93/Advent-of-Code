"Day 5 of AOC2022"
with open("AoC2022_05_data.txt", "r") as file:
    data = file.read()
    
p1,p2 = [x.split('\n') for x in data.split('\n\n')]

ans1,ans2='',''
craters,craters1 = {},{}

for i in range(1,len(p1[0]),4):
    craters[int(p1[-1][i])]=[]
    craters1[int(p1[-1][i])]=[]
    
for i in range(len(p1)-1):
    line = p1[i]
    for j in range(1,len(line),4):
        if line[j] != ' ':
            craters[j//4+1] = [line[j]]+craters[j//4+1]
            craters1[j//4+1] = [line[j]]+craters1[j//4+1]

for line in p2:
    line = line.split(' ')
    move = craters[int(line[3])][-int(line[1]):]
    move1 = list(reversed(craters1[int(line[3])][-int(line[1]):]))
    craters[int(line[3])] = craters[int(line[3])][:-int(line[1])]
    craters1[int(line[3])] = craters1[int(line[3])][:-int(line[1])]
    craters[int(line[-1])] += move
    craters1[int(line[-1])] += move1
        
for i in craters.keys():
    ans1+=craters1[i][-1]
    ans2+=craters[i][-1]

print(ans1)
print(ans2) 