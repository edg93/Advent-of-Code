from copy import copy
f = open("data.txt", "r")
data = f.read()
data=data.split('\n')

data = ['.'*len(data[0])] + data + ['.'*len(data[0])]
data = ['.'+string+'.' for string in data]

def neighbours(i,j):
    return [data[i-1][j-1],data[i-1][j],data[i-1][j+1],data[i][j-1],data[i][j+1],data[i+1][j-1],data[i+1][j],data[i+1][j+1]]

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
                    if occupied>3:
                        nextstate[i] = nextstate[i][:j]+'L'+nextstate[i][j+1:]
                        change=True
    return nextstate,change

change = True
while change:
    data,change=iteration(data)
    
occupied=0
for i in range(len(data)-2):
        i = i+1
        for j in range(len(data[0])-2):
            j=j+1
            if data[i][j]=='#':
                occupied=occupied+1
                
print(occupied)