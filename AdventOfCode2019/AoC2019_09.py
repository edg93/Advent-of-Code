from IntcodeComputer import computer
with open("AoC2019_09_data.txt", "r") as file:
    data = file.read()
data = [int(x) for x in data.split(',')]
            
#data = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
#data = [1102,34915192,34915192,7,4,7,99,0]
for part in [1,2]:
    d = {}
    for n,i in enumerate(data):
        d[n]=i
    print(computer(d,part)[-1])
