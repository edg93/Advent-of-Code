with open("AoC2020_14_data.txt", "r") as file:
    data = file.read()
data = data.split('\n')

memory1,memory2 = {},{}

def recursion(currentNumbers,x):
    newNumbers=[]
    for n in currentNumbers:
        newNumbers.append(n)
        newNumbers.append(n + x)
    return newNumbers

for instruction in data:
    if instruction[:4]=='mask':
        mask = instruction[7:]
        XX=[]
        ones = 0
        zeros = []
        for i in range(len(mask)):
            if mask[len(mask)-i-1] == 'X':
                XX.append(2**i)
            elif mask[len(mask)-i-1] == '1':
                ones += 2**i
            else:
                zeros.append(i)
    else:
        addressBIN,value = [int(x) for x in instruction[4:].split('] = ')]
        #Part1
        number=0
        v = bin(value)[2:]
        for i in range(len(mask)):
            if i>len(v)-1:
                n=0
            else:
                n=int(v[len(v)-i-1])
            if mask[len(mask)-i-1]=='1':
                number += 2**i
            elif mask[len(mask)-i-1]=='X':
                number += n*2**i
        memory1[addressBIN]=number
        #Part2
        address=ones
        addressBIN=bin(addressBIN)[2:]
        for i in range(len(addressBIN)):
            if i in zeros:
                address += int(addressBIN[len(addressBIN)-i-1])*2**i
        currentNumbers=[0]
        
        for x in XX:
            currentNumbers = recursion(currentNumbers,x)
        for n in currentNumbers:
            memory2[address+n]=value

for m in [memory1,memory2]:
    ans = 0
    for key in m.keys():
        ans += m[key]
    print(ans)