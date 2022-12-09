with open("AoC2019_05_data.txt", "r") as file:
    data = file.read()
    
data = [int(x) for x in data.split(',')]

def get_parameter(data,i,mode):
    if mode == 0:
        return data[data[i]]
    elif mode == 1:
        return data[i]

def run(data,start):
    i=0
    while i<len(data):
        x=data[i]
        i+=1
        opc = x%100
        p1 = x//(10**2)%10
        p2 = x//(10**3)%10
        if opc==99:
            break
        elif opc == 1:
            data[data[i+2]]=get_parameter(data,i,p1)+get_parameter(data,i+1,p2)
            i+=3
        elif opc == 2:
            data[data[i+2]]=get_parameter(data,i,p1)*get_parameter(data,i+1,p2)
            i+=3
        elif opc == 3:
            data[data[i]]=start
            i+=1
        elif opc == 4:
            if data[data[i]]!=0:
                print(data[data[i]])
            i+=1
        elif opc == 5:
            p1=get_parameter(data,i,p1)
            if p1!=0:
                i = get_parameter(data,i+1,p2)
            else:
                i+=2
        elif opc == 6:
            p1=get_parameter(data,i,p1)
            if p1==0:
                i = get_parameter(data,i+1,p2)
            else:
                i+=2
        elif opc == 7:
            if get_parameter(data,i,p1)<get_parameter(data,i+1,p2):
                data[data[i+2]]=1
            else:
                data[data[i+2]]=0
            i+=3
        elif opc == 8:
            if get_parameter(data,i,p1)==get_parameter(data,i+1,p2):
                data[data[i+2]]=1
            else:
                data[data[i+2]]=0  
            i+=3

run(data,1)

with open("AoC2019_05_data.txt", "r") as file:
    data = file.read()
    
data = [int(x) for x in data.split(',')]

run(data,5)