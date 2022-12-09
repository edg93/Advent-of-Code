f = open("data.txt", "r")
data = f.read()
data=data.split('\n')

counter=0 #correct pw

for k in range(len(data)):
    string = data[k]
    a=string.split(' ')
    b=a[0].split('-')
    c=b+a[1:]
    c[2]=c[2].replace(':','')
    c[0]=int(c[0])
    c[1]=int(c[1])
    data[k]=c
    if data[k][2]==data[k][3][data[k][0]-1]:
        if data[k][2]!=data[k][3][data[k][1]-1]:
            counter = counter +1
            print(data[k])
    else:
        if data[k][2]==data[k][3][data[k][1]-1]:
            counter = counter +1
            print(data[k])

print(counter)
