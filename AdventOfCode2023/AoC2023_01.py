with open("AoC2023_01_data.txt", "r") as file:
    data = file.read()
    
data = data.split('\n')
ans1,ans2 = 0,0

for line in data:
    d1,d2 = [],[]
    for i,c in enumerate(line):
        if c.isnumeric():
            d1.append(c)
            d2.append(c)
        for d,val in enumerate(['one','two','three','four','five','six','seven','eight','nine']):
            if line[i:].startswith(val):
                d2.append(str(d+1))
    ans1+=int(d1[0]+d1[-1])
    ans2+=int(d2[0]+d2[-1])

print(ans1,ans2)