with open("AoC2023_24_data.txt", "r") as file:
    data = file.read()

data = data.split('\n')
ans1,ans2=0,0

test = [7,27]
test = [200000000000000,400000000000000]

def intersection(m1,q1,m2,q2):
    if m1!=m2:
        x_inter = (q2-q1)/(m1-m2)
        y_inter = x_inter*m1+q1
    return x_inter,y_inter

for i,l1 in enumerate(data):
    for j,l2 in enumerate(data[i+1:]):
        pos,vel = l1.strip().split('@')
        x1,y1,z1 = [int(x) for x in pos.strip().split(', ')]
        vx1,vy1,vz1 = [int(x) for x in vel.strip().split(', ')]
        pos,vel = l2.strip().split('@')
        x2,y2,z2 = [int(x) for x in pos.strip().split(', ')]
        vx2,vy2,vz2 = [int(x) for x in vel.strip().split(', ')]
        
        x1_f = x1+vx1
        y1_f = y1+vy1
        z1_f = z1+vz1
        x2_f = x2+vx2
        y2_f = y2+vy2
        z2_f = z2+vz2
                
        m1 = (y1_f-y1)/(x1_f-x1)
        q1 = y1-m1*x1
        m2 = (y2_f-y2)/(x2_f-x2)
        q2 = y2-m2*x2
        
        if m1!=m2:
            x_intersection = (q2-q1)/(m1-m2)
            y_intersection = x_intersection*m1+q1
        if test[0]<=x_intersection<=test[1] and test[0]<=y_intersection<=test[1]:
            past = False
            if x1_f>x1:
                if x_intersection<x1:
                    past = True
            else:
                if x_intersection>x1:
                    past = True
            if x2_f>x2:
                if x_intersection<x2:
                    past = True
            else:
                if x_intersection>x2:
                    past = True
            if not past:
                ans1+=1
print(ans1)