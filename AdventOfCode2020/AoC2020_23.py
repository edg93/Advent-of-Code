prova = [3,8,9,1,2,5,4,6,7]
data = [2,4,7,8,1,9,3,5,6]

numbers = [1,2,3,4,5,6,7,8,9]

def round1(cups):
    pick = cups[1:4]
    n = cups[0]
    cups = cups[:1]+cups[4:]
    found = False
    for k in range(4):
        if not found:
            for j in range(len(cups)):
                if numbers[n-k-2] == cups[j]:
                    cups=cups[:j+1] + pick + cups[j+1:]
                    found = True
                    break
    return cups[1:]+[n]
    

for j in range(100):
    data = round1(data)
print(data)

prova = [3,8,9,1,2,5,4,6,7]
successivoprova = [2,5,8,6,4,7,10,9,1]
data = [2,4,7,8,1,9,3,5,6]
successivo = [9,4,5,7,6,10,8,1,3]

n=1000000

temp = [x+11 for x in range(n-10)]
successivo = successivo + temp + [2]
successivoprova = successivoprova + temp + [3]

indexdata = data[0]
indexprova = prova[0]

def round2(succ,index):
    n1=succ[index-1]
    n2=succ[n1-1]
    n3=succ[n2-1]
    succ[index-1]=succ[n3-1]
    for k in range(4):
        destination = index-k-1
        if destination == 0:
            destination = len(succ)
        elif destination == -1:
            destination = len(succ)-1
        elif destination == -2:
            destination = len(succ)-2
        elif destination == -3:
            destination = len(succ)-3
        if destination not in [n1,n2,n3]:
            succ[n3-1]=succ[destination-1]
            succ[destination-1]=n1
            break
    
    return succ,succ[index-1]

def translate(succ):
    result = []
    last = 1
    for k in range(len(succ)):
        result += [succ[last-1]]
        last = succ[last-1]
    return result    

        
for j in range(10000000):
    successivo,indexdata = round2(successivo,indexdata)


print(successivo[0]*successivo[successivo[0]-1])