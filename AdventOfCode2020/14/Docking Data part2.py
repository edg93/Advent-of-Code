from copy import copy

f = open("data.txt", "r")
data = f.read()
data = data.split('\n')

sum=0

memory = {}
mask = ''

def recursion(currentNumbers,XX):
    newNumbers=[]
    for n in currentNumbers:
        newNumbers.append(n)
        newNumbers.append(n + XX[0])
    XX = XX[1:]
    return newNumbers,XX

for instruction in data:
    if instruction[:4]=='mask':
        mask = instruction[7:]
        XX=[]
        ones = 0
        zeros = []
        for i in range(len(mask)):
            if mask[len(mask)-i-1] == 'X':
                XX.append(pow(2,i))
            elif mask[len(mask)-i-1] == '1':
                ones = ones + pow(2,i)
            else:
                zeros.append(i)
    else:
        address=ones
        instruction = instruction[4:]
        addressBIN = ''
        while instruction[0] in '0123456789':
            addressBIN = addressBIN + instruction[0]
            instruction = instruction[1:]
        addressBIN=bin(int(addressBIN))[2:]
        value = int(instruction[4:])
        for i in range(len(addressBIN)):
            if i in zeros:
                address = address + int(addressBIN[len(addressBIN)-i-1])*pow(2,i)
        currentNumbers=[0]
        XXcopy=copy(XX)
        while len(XXcopy)>0:
            currentNumbers,XXcopy = recursion(currentNumbers,XXcopy)
        for n in currentNumbers:
            memory[address+n]=value

for key in memory.keys():
    sum = sum + memory[key]
    
print(sum)