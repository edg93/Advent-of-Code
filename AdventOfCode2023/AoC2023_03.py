with open("AoC2023_03_data.txt", "r") as file:
    data = file.read()
    
data = data.split('\n')
ans1,ans2 = 0,0
symbols = set()
stars = {}

for r,line in enumerate(data):
    for c,letter in enumerate(line):
        if not letter.isnumeric() and not letter.isalpha() and letter!='.':
            symbols.add((r,c))
            if letter=='*':
                stars[(r,c)]=[]
        
for r,line in enumerate(data):
    for c,letter in enumerate(line):
        if letter.isnumeric():
            if line[c-1].isnumeric():
                continue
            n = ''
            for c1,l1 in enumerate(line[c:]):
                if l1.isnumeric():
                    n+=l1
                else:
                    break
            to_add = False
            for rr in [-1,0,1]:
                for cc in range(-1,len(n)+1):
                    if (r+rr,c+cc) in symbols:
                        to_add=True
                        if (r+rr,c+cc) in stars.keys():
                            stars[(r+rr,c+cc)].append(n)       
            if to_add:
                ans1+=int(n)
            
for key,value in stars.items():
    if len(value)==2:
        ans2+=int(value[0])*int(value[1])
            
print(ans1,ans2)