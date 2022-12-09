f = open("data.txt", "r")
data = f.read()
data=data.split('\n')
data=data[1:] #elimino la prima riga

position=0
l = len(data[0])
trees = 0
for line in data:
    position=position+3
    position=position%l
    if line[position]=='#':
        trees = trees+1
        
print(trees)