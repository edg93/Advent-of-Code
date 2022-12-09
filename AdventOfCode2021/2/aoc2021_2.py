f = open("data.txt", "r")
data = f.read()
data=data.split('\n')
f.close()

#PART 1

h=0
d=0

for line in data:
    command, n = line.split(' ')
    if command == 'forward':
        h += int(n)
    elif command == 'up':
        d -= int(n)
    elif command == 'down':
        d += int(n)
        
print(h*d)


#PART 2

h=0
d=0
aim = 0

for line in data:
    command, n = line.split(' ')
    if command == 'forward':
        h += int(n)
        d += aim*int(n)
    elif command == 'up':
        aim -= int(n)
    elif command == 'down':
        aim += int(n)
        
print(h*d)
