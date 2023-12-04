with open("AoC2020_05_data.txt", "r") as file:
    data = file.read()
data=data.split('\n')

for i,seat in enumerate(data):
    r,c = 0,0
    for k in range(7):
        if seat[k]=='B':
            r += 2**(6-k)
    for k in range(3):
        if seat[7+k]=='R':
            c += 2**(2-k)
    data[i] = r*8+c
    
data.sort()
print(data[-1])

for k in range(len(data)):
    if data[k]+1!=data[k+1]:
        print(data[k]+1)
        break