with open("AoC2020_01_data.txt", "r") as file:
    data = file.read()
data=data.split('\n')

data = [int(x) for x in data]
L = len(data)

for k in range(L):
    for j in range(L-k):
        if data[k]+data[k+j] == 2020:
            ans1 = data[k]*data[k+j]
        for l in range(L-k-j):
            if data[k]+data[k+j]+data[k+j+l] == 2020:
                ans2 = data[k]*data[k+j]*data[k+j+l]

print(ans1)
print(ans2)