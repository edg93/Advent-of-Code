f = open("data.txt", "r")
seats = f.read()
seats=seats.split('\n')
f.close()

maximum=0
for seat in seats:
    row=0
    column=0
    for k in range(7):
        if seat[k]=='B':
            row = row + 2**(6-k)
    for k in range(3):
        if seat[6+k]=='R':
            column = column + 2**(3-k)
    maximum= max(maximum,row*8+column)
    
print(maximum)