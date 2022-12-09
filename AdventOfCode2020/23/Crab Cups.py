prova = [3,8,9,1,2,5,4,6,7]
data = [2,4,7,8,1,9,3,5,6]

numbers = [1,2,3,4,5,6,7,8,9]

def round(cups):
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
    data = round(data)
print(data)

