from functools import cmp_to_key
with open("AoC2022_13_data.txt", "r") as file:
    data = file.read()
data=data.strip().split('\n\n')

def compare(p1,p2):
    i,j = 0,0
    while i< len(p1):
        s1,s2 = p1[i],p2[j]
        if j>= len(p2):
            return False
        if s1==s2:
            if s1 in '0123456789':
                n1 = int(p1[i:].split(',')[0].split(']')[0])
                n2 = int(p2[j:].split(',')[0].split(']')[0])
                if n1>n2:
                    return False
                elif n1<n2:
                    return True
            i+=1
            j+=1
            continue
        elif s1==']':
            return True
        elif s2 == ']':
            return False
        elif s1 in ['[',',']:
            i += 1
            if s1 == '[':
                n2 = len(p2[j:].split(',')[0].split(']')[0])
                p2 = p2[:j+n2]+']'+p2[j+n2:]
            continue
        elif s2 in ['[',',']:
            j += 1
            if s2 == '[':
                n1 = len(p1[i:].split(',')[0].split(']')[0])
                p1 = p1[:i+n1]+']'+p1[i+n1:]
            continue
        else:
            n1 = int(p1[i:].split(',')[0].split(']')[0])
            n2 = int(p2[j:].split(',')[0].split(']')[0])

            if n1< n2:
                return True
            elif n1>n2:
                return False
    return True

ans1 = 0
ans2 = 1

a = '[[2]]'
b = '[[6]]'
P = ['[[2]]','[[6]]']
P_ordered = []
for i in range(len(data)):    
    p1,p2 = data[i].split('\n')
    P.append(p1)
    P.append(p2)
    
    if compare(p1,p2):
        ans1 += i+1
print(ans1)

i = 0
while i <len(P):
    print(i)
    for p1 in P:
        c = 0
        for p2 in P:
            if p1!=p2 and compare(p2,p1):
                c+=1
            if c>i:
                break
        if c==i:
            P_ordered.append(p1)
            break
    i+=1
for i,l in enumerate(P_ordered):
    if l in [a,b]:
        ans2 *= i+1
print(ans2)

P = sorted(P, key=cmp_to_key(lambda p1,p2: compare(p1,p2)==-1))