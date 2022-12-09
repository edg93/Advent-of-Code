f = open("data.txt", "r")
seats = f.read()
seats=seats.split('\n')
f.close()
print(seats[0])
print(seats[33])
maximum=0
for n in range(len(seats)):
    seat = seats[n]
    row=0
    column=0
    for k in range(7):
        if seat[k]=='B':
            row = row + 2**(6-k)
    for k in range(3):
        if seat[7+k]=='R':
            column = column + 2**(2-k)
    seats[n] = row*8+column
    
print(seats[0])
print(seats[33])

seats.sort()

for k in range(len(seats)):
    if k!=len(seats)-1:
        if seats[k]+1!=seats[k+1]:
            print(seats[k+1])
