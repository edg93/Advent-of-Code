f = open("data.txt", "r")
data = f.read()
data=data.split('\n')
f.close()

#PART 1
n=len(data[0])

epsilon = [0 for i in range(n)] # contiene i più comuni
gamma = [0 for i in range(n)] # contiene i meno comuni

l = [0 for i in range(n)]

for x in data:
    for i in range(n):
        if x[i]=='0':
            l[i]-=1
        else:
            l[i]+=1

for i in range(n):
    if l[i]>0:
        epsilon[i]=1
    elif l[i]<0:
        gamma[i]=1
        
a,b=0,0

for i in range(n):
    a+=gamma[-i-1]*2**i
    b+=epsilon[-i-1]*2**i

print(a*b)

#PART 2
most = [1 for i in range(len(data))]
less = [1 for i in range(len(data))]

first = 0
second = 0

for i in range(n):
    a,b = [],[]
    print(less)
    for j in range(len(data)):
        if most[j]==1:
            a+=[int(data[j][i])]
        if less[j]==1:
            b+=[int(data[j][i])]
            
    ones = a.count(1)
    if ones>=len(a)-ones:
        for j in range(len(data)):
            if data[j][i]==str(0):
                most[j]=0
    else:
        for j in range(len(data)):
            if data[j][i]==str(1):
                most[j]=0
     
    ones = b.count(1)
    if ones>=len(b)-ones:
        for j in range(len(data)):
            if data[j][i]==str(1):
                less[j]=0
    else:
        for j in range(len(data)):
            if data[j][i]==str(0):
                less[j]=0
    if most.count(1)==1:
        for r in range(len(most)):
            if most[r]==1:
                first = data[r]
    if less.count(1)==1:
        for r in range(len(less)):
            if less[r]==1:
                second = data[r]

print(first,second)
print(int(first,2)*int(second,2))