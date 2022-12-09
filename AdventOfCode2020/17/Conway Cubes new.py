from copy import copy
f = open("data.txt", "r")
data = f.read()
data=data.split('\n')

dim=21
dimz=13

grid = {}
for i in range(dimz):
    i=i-dimz//2
    for j in range(dim):
        j=j-dim//2
        for k in range(dim):
            k=k-dim//2
            grid[(i,j,k)]='.'
    
for j in range(len(data)):
    for k in range(len(data[0])):
        grid[(0,j - len(data)//2,k - len(data[0])//2)]=data[j][k]

def active(i,j,k):
    n = 0
    for ii in [i-1,i,i+1]:
        for jj in [j-1,j,j+1]:
            for kk in [k-1,k,k+1]:
                if not (ii==i and jj==j and kk==k) and grid[(ii,jj,kk)]=='#':    
                    n = n + 1
    return n

def printData(data):
    for i in range(dimz):
        i = i-dimz//2
        print(i)
        for j in range(dim):
            j = j - dim//2
            row = ''
            for k in range(dim):
                k = k - dim//2
                row = row + grid[(i,j,k)]
            print(row)
            
def iteration(currentstate):
    nextstate=copy(currentstate)
    for i in range(dimz-2):
        i=i+1-dimz//2
        for j in range(dim-2):
            j=j+1-dim//2
            for k in range(dim-2):
                k=k+1-dim//2
                a = active(i,j,k)
                if currentstate[(i,j,k)]=='.':
                    if a == 3:
                        nextstate[(i,j,k)]='#'
                elif currentstate[(i,j,k)]=='#':
                    if not(a == 3 or a == 2):
                        nextstate[(i,j,k)] = '.'
    return nextstate

for k in range(6):
    grid=iteration(grid)

on=0
for i in range(dimz-2):
        i = i+1-dimz//2
        for j in range(dim-2):
            j=j+1-dim//2
            for k in range(dim-2):
                k=k+1-dim//2
                if grid[i,j,k]=='#':
                    on=on+1
                
print(on)