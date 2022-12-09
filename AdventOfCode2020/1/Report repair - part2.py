f = open("data.txt", "r")
data = f.read()
data=data.split('\n')
for k in range(len(data)):
   data[k]=int(data[k])
for k in range(len(data)):
    for j in range(len(data)-k):
        for l in range(len(data)-k-j):
            sum=data[k]+data[k+j]+data[k+j+l]
            #print(sum)
            if sum == 2020:
                print(data[k])
                print(data[k+j])
                print(data[k+j+l])
                print(data[k]*data[k+j]*data[k+j+l])
