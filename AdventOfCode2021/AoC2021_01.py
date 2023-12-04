with open("AoC2021_01_data.txt", "r") as file:
    data = file.read()
data=data.split('\n')

#PART 1

ans1=0
n=len(data)

for k in range(n-1):
    if int(data[k])<int(data[k+1]):
        ans1 += 1

print(ans1)

#PART 2

ans2=0

for k in range(n-3):
    if int(data[k])<int(data[k+3]):
        ans2 += 1

print(ans2)
