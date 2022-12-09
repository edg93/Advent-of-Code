with open("data.txt", "r") as file:
    data = file.read()
    
numbers=[int(x) for x in data.split('\n')]

numbers.sort()

numbers=[0] + numbers + [numbers[-1]+3]

diff1 = 0
diff3 = 0

for k in range(len(numbers)-1):
    if numbers[k+1]-numbers[k]==1:
        diff1 = diff1+1
    elif numbers[k+1]-numbers[k]==3:
        diff3 = diff3+1
        
print(diff1*diff3)