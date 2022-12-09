f = open("data.txt", "r")
data = f.read()
data = data.split('\n')

sum=0

memory = {}
mask = ''

for instruction in data:

    if instruction[:4]=='mask':
        mask = instruction[7:]
    else:
        instruction = instruction[4:]
        k=0
        number=0
        a = ''
        while instruction[k] in '0123456789':
            a = a + instruction[k]
            k = k+1
        b = int(instruction[k+4:])
        b = bin(b)[2:]
        for i in range(len(mask)):
            if i>len(b)-1:
                n=0
            else:
                n=int(b[len(b)-i-1])
            if mask[len(mask)-i-1]=='1':
                number = number + pow(2,i)
            elif mask[len(mask)-i-1]=='X':
                number = number + n*pow(2,i)
        #print(number)
        memory[a]=number

for key in memory.keys():
    sum = sum + memory[key]
    
print(sum)