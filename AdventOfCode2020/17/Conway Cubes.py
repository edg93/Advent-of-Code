from copy import copy
f = open("data.txt", "r")
data = f.read()
data=data.split('\n')

for k in range(7):
    data = ['.'*len(data[0])] + data + ['.'*len(data[0])]
    data = ['.'+string+'.' for string in data]
    
layer = []
for i in range(len(data)):
    layer.append('')
    for j in range(len(data)):
        layer[i] = layer[i] + '.'
        
data = [layer,layer,layer,layer,layer,layer,layer,data,layer,layer,layer,layer,layer,layer,layer]

def active(i,j,k):
    a = 0
    for ii in [i-1,i,i+1]:
        for jj in [j-1,j,j+1]:
            for kk in [k-1,k,k+1]:
                if not (ii==i and jj==j and kk==k) and data[ii][jj][kk]=='#':    
                    a = a + 1
    return a

def printData(data):
    for j in range(len(data)):
        print() 
        for i in range(len(data[0])):
            print(data[j][i])
            
def iteration(currentstate):
    nextstate=copy(currentstate)
    for i in range(len(currentstate)-2):
        i=i+1
        nextstate[i]=copy(currentstate[i])
        for j in range(len(currentstate[0])-2):
            j=j+1
            nextstate[i][j]=copy(currentstate[i][j])
            for k in range(len(currentstate[0][0])-2):
                k=k+1
                a = active(i,j,k)
                if currentstate[i][j][k]=='.':
                    if a == 3:
                        nextstate[i][j] = nextstate[i][j][:k]+'#'+nextstate[i][j][k+1:]
                elif currentstate[i][j][k]=='#':
                    if not(a == 3 or a == 2):
                        nextstate[i][j] = nextstate[i][j][:k]+'.'+nextstate[i][j][k+1:]
    return nextstate

for k in range(6):
    data=iteration(data)
    
occupied=0
for i in range(len(data)-2):
        i = i+1
        for j in range(len(data[0])-2):
            j=j+1
            for k in range(len(data[0][0])-2):
                k=k+1
                if data[i][j][k]=='#':
                    occupied=occupied+1
                
print(occupied)