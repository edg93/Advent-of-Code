f = open("data.txt", "r")

steps=[[1,1],[3,1],[5,1],[7,1],[1,2]]
trees=[0,0,0,0,0]
for s in range(len(steps)):
    step=steps[s]
    step[0],step[1]=int(step[0]),int(step[1])
    f = open("data.txt", "r")
    data = f.read()
    data=data.split('\n')
    data=data[step[1]:] #elimino le prime righe
    print(step)
    position=0
    l = len(data[0])
    trees[s] = 0
    for k in range(len(data)):
        line=data[k]
        if k%step[1]==0:
            position=position+step[0]
            position=position%l
            if line[position]=='#':
                trees[s] = trees[s]+1
    f.close()
print(trees)
product=1
for n in trees:
    product = product*n
    
print(product)