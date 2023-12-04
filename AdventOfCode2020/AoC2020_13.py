with open("AoC2020_13_data.txt", "r") as file:
    data = file.read()

data = data.split('\n')

time = int(data[0])
data = data[1].split(',')
buses = [(int(bus),k) for k,bus in enumerate(data) if bus!='x']

myTime = 1e9
for bus in buses:
    bus = bus[0]
    newT = (time//bus+1)*bus

    if newT<myTime:
        myTime=newT
        myBus=bus
        
print((myTime-time)*myBus)

N=1
listN=[]
listy=[]
ans2=0

for bus in buses:
    N=N*bus[0]
        
for bus in buses:
    listN.append(N//bus[0])
    found = False
    k=N//bus[0]
    while not found:
        if k%bus[0]==1:
            listy.append(int(k*bus[0]/N))
            found=True
        k += N//bus[0]

for k in range(len(listy)):
    ans2 += listy[k]*listN[k]*(buses[k][0]-buses[k][1])

print(ans2%N)