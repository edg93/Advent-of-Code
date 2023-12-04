with open("AoC2021_03_data.txt", "r") as file:
    data = file.read()
data= data.split('\n')

#PART 1
N = len(data)
n = len(data[0])
epsilon = [0 for i in range(n)] # contiene i più comuni
l = [0 for i in range(n)]

for x in data:
    for i in range(n):
        if x[i]=='0':
            l[i]-=1
        else:
            l[i]+=1
a,b=0,0

for i in range(n):
    if l[i]>0:
        epsilon[i]=1
        
for i in range(n):
    a += (1-epsilon[-i-1])*2**i
    b += epsilon[-i-1]*2**i

print(a*b)

#PART 2
most = [1 for i in range(N)]
less = [1 for i in range(N)]

first,second = 0,0

for i in range(n):
    a,b = [],[]
    for j in range(N):
        if most[j]==1:
            a+=[int(data[j][i])]
        if less[j]==1:
            b+=[int(data[j][i])]
    ones = a.count(1)
    for j in range(N):
        if ones>=len(a)-ones:
            if data[j][i]==str(0):
                most[j]=0
        else:
            if data[j][i]==str(1):
                most[j]=0
    ones = b.count(1)
    for j in range(N):
        if ones>=len(b)-ones:
            if data[j][i]==str(1):
                less[j]=0
        else:
            if data[j][i]==str(0):
                less[j]=0
    for r in range(N):
        if most.count(1)==1 and most[r]==1: 
            first = data[r]
        if less.count(1)==1 and less[r]==1:
            second = data[r]

print(int(first,2)*int(second,2))