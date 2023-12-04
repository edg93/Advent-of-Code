with open("AoC2020_02_data.txt", "r") as file:
    data = file.read()
data=data.split('\n')

ans1,ans2=0,0

for line in data:
    line = line.split()
    a,b=[int(x) for x in line[0].split('-')]
    ch, pw = line[1][0],line[2]
    n = 0
    for letter in pw:
        if letter==ch:
            n += 1
    if a<=n<=b:
        ans1 += 1
    if (pw[a-1]==ch and pw[b-1]!=ch) or (pw[a-1]!=ch and pw[b-1]==ch):
        ans2 += 1

print(ans1)
print(ans2)