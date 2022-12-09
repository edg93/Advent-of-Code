from copy import copy

f = open("data.txt", "r")
data = f.read()
data = data.split('\n')

myTime = int(data[0])
buses = data[1].split(',')
busesCopy = buses.copy()
for bus in buses:
    if bus == 'x':
        busesCopy.remove(bus)
       
time=0
myBus=''
for bus in busesCopy:
    newT = (int(myTime/int(bus))+1)*int(bus)

    if time==0 or newT<time:
        time=newT
        myBus=bus
        
print((time-myTime)*int(myBus))