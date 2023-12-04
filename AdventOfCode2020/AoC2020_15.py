lastApperance = {1:[0,1],20:[0,2],11:[0,3],6:[0,4],12:[0,5],0:[0,6]}

counter = len(lastApperance)
lastNumber = 0
while counter!=30000000:
    counter += 1
    if counter == 2021:
        print(lastNumber)
    if counter%500000==0:
        print(counter)
    if lastApperance[lastNumber][0]==0:
        lastNumber = 0
        lastApperance[lastNumber]=[lastApperance[lastNumber][1],counter]
    else:
        lastNumber=lastApperance[lastNumber][1]-lastApperance[lastNumber][0]
        if lastNumber in lastApperance.keys():
            lastApperance[lastNumber]=[lastApperance[lastNumber][1],counter]
        else:
            lastApperance[lastNumber]=[0,counter]
print(lastNumber)