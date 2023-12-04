from functools import cmp_to_key

with open("AoC2022_13_data.txt", "r") as file:
    data = file.read()
data=data.strip().split('\n\n')

def compare(p1,p2):
    if isinstance(p1,int) and isinstance(p2,int):
        if p1<p2:
            return -1
        elif p1>p2:
            return 1
        else:
            return 0
    elif isinstance(p1,list) and isinstance(p2,list):
        i=0
        while i<len(p1) and i<len(p2):
            c = compare(p1[i],p2[i])
            if c in [-1,1]:
                return c
            i+=1
        if i==len(p1) and i<len(p2):
            return -1
        elif i==len(p2) and i<len(p1):
            return 1
        else:
            return 0
    elif isinstance(p1,int) and isinstance(p2,list):
        return compare([p1],p2)
    elif isinstance(p1,list) and isinstance(p2,int):
        return compare(p1,[p2])
    else:
        return 0

    
ans1 = 0
ans2 = 1

a = '[[2]]'
b = '[[6]]'
P = ['[[2]]','[[6]]']

for i in range(len(data)):    
    p1,p2 = data[i].split('\n')
    
    p1 = eval(p1)
    p2 = eval(p2)
    P.append(p1)
    P.append(p2)
    if compare(p1,p2)==-1:
        ans1 += i+1
print(ans1)

P = sorted(P, key=cmp_to_key(lambda p1,p2: compare(p1,p2)))

for i,l in enumerate(P):
    if l in [a,b]:
        ans2 *= i+1
print(ans2)