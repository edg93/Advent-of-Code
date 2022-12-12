import numpy as np

with open("AoC2019_01_data.txt", "r") as file:
    data = file.read()

data = [int(x) for x in data.split('\n')]

#part 1
fuel = np.array([x//3-2 for x in data]).sum()
print(fuel)

#part 2
def compute_fuel(module):
    return module//3-2

total_fuel = 0
for module in data:
    fuel = compute_fuel(module)
    total_fuel += fuel
    while fuel>0:
        fuel = compute_fuel(fuel)
        if fuel>0:
            total_fuel+=fuel
            
print(total_fuel)
