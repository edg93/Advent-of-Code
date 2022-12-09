f = open("data.txt", "r")
data = f.read()
data=data.split('\n')
for k in range(len(data)):
   data[k]=int(data[k])
counter=0
for k in range(len(data)):

    for j in range(len(data)-k):
        sum=data[k]+data[k+j]
        counter=counter+1
        #print(sum)
        if sum == 2020:
            print(data[k])
            print(data[k+j])
            print(data[k]*data[k+j])
