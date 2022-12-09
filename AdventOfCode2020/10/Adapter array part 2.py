with open("data.txt", "r") as file:
    data = file.read()
    
numbers=[int(x) for x in data.split('\n')]
numbers.sort()

numbers=[0] + numbers + [numbers[-1]+3]

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