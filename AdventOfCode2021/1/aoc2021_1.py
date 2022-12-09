f = open("data.txt", "r")
data = f.read()
data=data.split('\n')
f.close()

#PART 1

counter=0
n=len(data)

for k in range(n-1):
    if int(data[k])<int(data[k+1]):
        counter += 1

print(counter)

#PART 2

counter=0

for k in range(n-3):
    if int(data[k])<int(data[k+3]):
        counter += 1

print(counter)
