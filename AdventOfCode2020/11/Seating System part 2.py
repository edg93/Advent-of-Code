from copy import copy
f = open("data.txt", "r")
data = f.read()
data=data.split('\n')

data = ['.'*len(data[0])] + data + ['.'*len(data[0])]
data = ['.'+string+'.' for string in data]

def neighbours(i,j):
    vicini = []
    
    vicino = data[i][j-1]
    k=1
    while vicino == '.' and k<j-1:
        k = k+1
        vicino = data[i][j-k]
    vicini.append(vicino)
    
    vicino = data[i][j+1]
    k=1
    while vicino == '.' and k<len(data[0])-j-1:
        k = k+1
        vicino = data[i][j+k]
    vicini.append(vicino)
    
    vicino = data[i-1][j]
    k=1
    while vicino == '.' and k<i-1:
        k = k+1
        vicino = data[i-k][j]
        
    vicini.append(vicino)
    
    vicino = data[i+1][j]
    k=1
    while vicino == '.' and k<len(data)-i-1:
        k = k+1
        vicino = data[i+k][j]
    vicini.append(vicino)
    
    vicino = data[i-1][j-1]
    k=1
    while vicino == '.' and k<j-1 and k<i-1:
        k = k+1
        vicino = data[i-k][j-k]
    vicini.append(vicino)
    
    vicino = data[i+1][j-1]
    k=1
    while vicino == '.' and k<len(data)-i-1 and k<j-1:
        k = k+1
        vicino = data[i+k][j-k]
    vicini.append(vicino)
    
    vicino = data[i-1][j+1]
    k=1
    while vicino == '.' and k<i-1 and k<len(data[0])-j-1:
        k = k+1
        vicino = data[i-k][j+k]
    vicini.append(vicino)
    
    vicino = data[i+1][j+1]
    k=1
    while vicino == '.' and k<len(data[0])-j-1 and k<len(data)-i-1:
        k = k+1
        vicino = data[i+k][j+k]
    vicini.append(vicino)    
    return vicini    
    
def iteration(currentstate):
    nextstate=copy(currentstate)
    change = False
    for i in range(len(currentstate)-2):
        i = i+1
        for j in range(len(currentstate[0])-2):
            j=j+1
            if currentstate[i][j]=='L' and not any(n=='#' for n in neighbours(i,j)):
                nextstate[i] = nextstate[i][:j]+'#'+nextstate[i][j+1:]
                change = True
            if currentstate[i][j]=='#':
                occupied=0
                for n in neighbours(i, j):
                    if n=='#':
                        occupied=occupied+1
                    if occupied>4:
                        nextstate[i] = nextstate[i][:j]+'L'+nextstate[i][j+1:]
                        change=True
    return nextstate,change

change = True

while change:
    #print(data)
    data,change=iteration(data)
    
occupied=0
for i in range(len(data)-2):
        i = i+1
        for j in range(len(data[0])-2):
            j=j+1
            if data[i][j]=='#':
                occupied=occupied+1
                
print(occupied)