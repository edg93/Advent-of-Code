def get_parameter(data,i,mode,base):
    if mode == 0:
        return data[i]
    elif mode == 1:
        return i
    elif mode == 2:
        return data[i]+base
    else:
        print('problem: mode not supported')
        
def f(data,p):
    if p not in data.keys():
        data[p]=0
    return data[p]

def computer(data,ip,i=0,base=0):
    while i<len(data):
        x=data[i]
        i+=1
        opc = x%100
        p1 = x//(10**2)%10
        p1 = get_parameter(data,i,p1,base)
        if opc==99:
            return data,i,base,None
        if opc in [3,4,9]:
            i+=1
            if opc == 3:
                data[p1]=ip 
            p1 = f(data,p1)
            if opc == 4:
                return data,i,base,p1
            elif opc == 9:
                base += p1
        else:
            p2 = x//(10**3)%10
            p2 = get_parameter(data,i+1,p2,base)
            p1,p2 = f(data,p1),f(data,p2)
            if opc in [5,6]:
                if opc == 5:
                    if p1!=0:
                        i = p2-2
                elif opc == 6:
                    if p1==0:
                        i = p2-2
                i+=2
            elif opc in [1,2,7,8]:
                p3 = x//(10**4)%10
                p3 = get_parameter(data,i+2,p3,base)
                if opc == 1:
                    data[p3]=p1+p2
                elif opc == 2:
                    data[p3]=p1*p2
                elif opc == 7:
                    if p1<p2:
                        data[p3]=1
                    else:
                        data[p3]=0
                elif opc == 8:
                    if p1==p2:
                        data[p3]=1
                    else:
                        data[p3]=0  
                i+=3