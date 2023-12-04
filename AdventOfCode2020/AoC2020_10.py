with open("AoC2020_10_data.txt", "r") as file:
    data = file.read()
    
numbers=[int(x) for x in data.split('\n')]

numbers.sort()

numbers=[0] + numbers + [numbers[-1]+3]
diff1,diff3 = 0,0

for k in range(len(numbers)-1):
    if numbers[k+1]-numbers[k]==1:
        diff1 = diff1+1
    elif numbers[k+1]-numbers[k]==3:
        diff3 = diff3+1
        
print(diff1*diff3)

alreadyDone = [0 for x in numbers]
alreadyDone[-1]=1

def recursion(index):
    if alreadyDone[index] != 0:
        return alreadyDone[index]
    elif index == len(numbers)-2:
        if numbers[index+1]-numbers[index]<4:
            return recursion(index+1)
    elif index == len(numbers)-3:
        if numbers[index+2]-numbers[index]<4:
            return recursion(index+1)+recursion(index+2)
        elif numbers[index+1]-numbers[index]<4:
            return recursion(index+1)
    elif numbers[index+3]-numbers[index]<4:
        return recursion(index+1)+recursion(index+2)+recursion(index+3)
    elif numbers[index+2]-numbers[index]<4:
        return recursion(index+1)+recursion(index+2)
    elif numbers[index+1]-numbers[index]<4:
        return recursion(index+1)
    else:
        return 0
    
for k in range(len(alreadyDone)):
    alreadyDone[-(k+1)]=recursion(len(alreadyDone)-k-1)

print(alreadyDone[0])