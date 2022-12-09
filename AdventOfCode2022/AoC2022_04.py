"Day 4 of AOC2022"
with open("AoC2022_04_data.txt", "r") as file:
    data = file.read()
    
data = data.split('\n')

ans1,ans2=0,0

for line in data:
    a1,a2=line.split(',')
    a1=[int(x) for x in a1.split('-')]
    a2=[int(x) for x in a2.split('-')]
    if (a1[0]>=a2[0] and a1[1]<=a2[1]) or (a1[0]<=a2[0] and a1[1]>=a2[1]):
        ans1+=1
    if (a1[0]>=a2[0] and a1[0]<=a2[1]) or (a1[1]>=a2[0] and a1[1]<=a2[1]) or (a2[0]>=a1[0] and a2[0]<=a1[1]) or (a2[0]>=a1[0] and a2[0]<=a1[1]):
        ans2+=1
print(ans1)
print(ans2)