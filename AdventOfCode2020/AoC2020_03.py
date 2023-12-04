with open("AoC2020_03_data.txt", "r") as file:
    data = file.read()
data=data.split('\n')

L = len(data[0])

slopes=((1,1),(3,1),(5,1),(7,1),(1,2))
ans2=1
for (r,c) in slopes:
    trees = 0
    position = -r
    for i,line in enumerate(data):
        if i%c == 0:
            position = (position + r)%L
            if line[position]=='#':
                trees += 1
    if (r,c)==(3,1):
        print(trees)
    ans2 *= trees
    
print(ans2)