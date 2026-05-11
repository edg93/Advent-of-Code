with open("AoC2024_01_data.txt", "r") as file:
    data = file.read()
    
data = data.split('\n')
ans1,ans2 = 0,0

l1,l2 = [],[]
d= {}

for line in data:
    a,b = [int(x) for x in line.split()]
    l1.append(a)
    l2.append(b)
    if b in d.keys():
        d[b]+=1
    else:
        d[b]=1
    
l1.sort()
l2.sort()

for i in range(len(l1)):
    ans1 += abs(l1[i]-l2[i])
    if l1[i] in d.keys():
        ans2 += l1[i]*d[l1[i]]
    
print(ans1,ans2)