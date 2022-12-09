import matplotlib.pyplot as plt

"Day 8 of AOC2021"
with open("data.txt", "r") as file:
    data = file.read()
data=[int(x) for x in data.split(',')]
minimo,massimo = min(data),max(data)
sol1,sol2 = 10e9,10e9
d1,d2 = [],[]

for i in range(minimo,massimo):
    dist1,dist2 = 0,0
    for x in data:
        y = abs(x-i)
        dist2 += y*(y+1)//2
        dist1 += y
    if dist2<sol2:
        sol2 = dist2
    if dist1<sol1:
        sol1 = dist1
    d1 += [dist1]
    d2 += [dist2]

plt.plot(range(minimo,massimo),d1,label='sol1')
plt.plot(range(minimo,massimo),d2,label='sol2')
plt.yscale('log')
plt.legend()
plt.show()


print(sol1)
print(sol2)
