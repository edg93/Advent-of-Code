from IntcodeComputer import computer

with open("AoC2019_05_data.txt", "r") as file:
    data0 = file.read()
    
data0 = [int(x) for x in data0.split(',')]

for ip in [1,5]:
    data = {n:x for n,x in enumerate(data0)}
    output = 0
    i,base=0,0
    while output == 0:
        data,i,base,output = computer(data,ip,i,base)
    print(output)