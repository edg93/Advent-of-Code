with open("AoC2023_06_data.txt", "r") as file:
    data = file.read()
    
data = data.split('\n')
times=[int(x) for x in data[0].split()[1:]]
distances=[int(x) for x in data[1].split()[1:]]
T = int(''.join(data[0].split()[1:]))
D = int(''.join(data[1].split()[1:]))

ans1 = 1
ans2 = int((T + (T**2 - 4*D)**0.5)/2) - int((T - (T**2 - 4*D)**0.5)/2)

for i,time in enumerate(times):
    ans1*=int((time + (time**2 - 4*distances[i])**0.5)/2)-int((time - (time**2 - 4*distances[i])**0.5)/2)

print(ans1,ans2)