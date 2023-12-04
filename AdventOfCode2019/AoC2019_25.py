from IntcodeComputer import computer

with open("AoC2019_25_data.txt", "r") as file:
    data0 = file.read()
    
data0 = [int(x) for x in data0.split(',')]

data = {n:x for n,x in enumerate(data0)}
