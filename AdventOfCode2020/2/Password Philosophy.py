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
    n = 0
    for letter in data[k][3]:
        if letter==data[k][2]:
            n = n+1
    if n>= data[k][0] and n<=data[k][1]:
        counter = counter +1
        print(data[k])

            
print(counter)
