from IntcodeComputer import computer

with open("AoC2019_07_data.txt", "r") as file:
    data0 = file.read()

def get_parameter(i,mode):
    if mode == 0:
        return data[data[i]]
    elif mode == 1:
        return data[i]

def run(part,data,ip,i,op,mode):
    while i<len(data):
        x=data[i]
        i+=1
        opc = x%100
        if opc==99:
            break
        p1 = x//(10**2)%10
        p2 = x//(10**3)%10
        p1 = get_parameter(i,p1)
        if opc == 1:
            data[data[i+2]]=p1+get_parameter(i+1,p2)
            i+=3
        elif opc == 2:
            data[data[i+2]]=p1*get_parameter(i+1,p2)
            i+=3
        elif opc == 3:
            if mode:
                data[data[i]]=ip[0]
                mode=False
            else:
                data[data[i]]=ip[1]
            i+=1
        elif opc == 4:
            op = p1
            i+=1
            if data[i] == 99:
                return data,op,i,mode,True
            if part==2:
                return data,op,i,mode,False
        elif opc == 5:
            if p1!=0:
                i = get_parameter(i+1,p2)
            else:
                i+=2
        elif opc == 6:
            if p1==0:
                i = get_parameter(i+1,p2)
            else:
                i+=2
        elif opc == 7:
            if p1<get_parameter(i+1,p2):
                data[data[i+2]]=1
            else:
                data[data[i+2]]=0
            i+=3
        elif opc == 8:
            if p1==get_parameter(i+1,p2):
                data[data[i+2]]=1
            else:
                data[data[i+2]]=0  
            i+=3

SS = [(1,{0,1,2,3,4}),(2,{5,6,7,8,9})]

for part,S in SS:
    ans = 0
    for i1 in S:
        for i2 in S-{i1}:
            for i3 in S-{i1,i2}:
                for i4 in S-{i1,i2,i3}:
                    for i5 in S-{i1,i2,i3,i4}:
                        data_list = [([int(x) for x in data0.split(',')],0,0,True) for _ in range(5)]
                        output = 0
                        end = False
                        while not end:
                            for n,i in enumerate([i1,i2,i3,i4,i5]):
                                data,k,op,mode = data_list[n]
                                data,output,k,mode,end = run(part,data,(i,output),k,op,mode)

                                data_list[n]=(data,k,output,mode)
                        ans = max(ans,output)
    print(ans)