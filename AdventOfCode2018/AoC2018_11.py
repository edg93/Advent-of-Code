serial_number = 1308
    
        
ans = [0,0]


def power_level(x,y):
    rack_ID = x+10
    n = str(((rack_ID*y+serial_number)*rack_ID)%1000)
    if len(n)<3:
        return -5     
    else:
        return int(n[0])-5


def total_power(x,y,dim):
    if dim == 1:
        n = power_level(x,y)
    elif dim%2==0:
        d2 = int(dim/2)
        n = power_squares[(x,y,d2)]
        n += power_squares[(x+d2,y+d2,d2)]
        n += power_squares[(x+d2,y,d2)]
        n += power_squares[(x,y+d2,d2)]
    else:
        d2 = int((dim-1)/2)
        n = power_squares[(x,y,d2)]
        n += power_squares[(x+d2+1,y+d2+1,d2)]
        n += power_squares[(x+d2,y,d2+1)]
        n += power_squares[(x,y+d2,d2+1)]
        n -= power_squares[(x+d2,y+d2,1)]
        
    power_squares[(x,y,dim)]=n
    return n       

power_squares = {}
N = 300
max_power_p1 = -10e9
max_power_p2 = -10e9

for dim in range(1,N+1):
    for x in range(1,N+1-dim):
        for y in range(1,N+1-dim):
            power = total_power(x,y,dim)
            if power > max_power_p2:
                max_power_p2 = power
                ans[1]=x,y,dim
            if dim==3:
                if power > max_power_p1:
                    max_power_p1 = power
                    ans[0]=x,y
    
print(ans)
