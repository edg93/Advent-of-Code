"Day 17 of AOC2021"
import time
from math import sqrt

#x_target = [x for x in range(20,31)]
#y_target = [x for x in range(-10,-4)]

x_target = [x for x in range(240,293)]
y_target = [x for x in range(-90,-56)]


vx_list = [x+1 for x in range(int(sqrt(x_target[0])),x_target[-1])]
vy_list = [x for x in range(y_target[0],x_target[-1])]
      
print(len(vy_list),len(vx_list))
max_v = (0,-10000)
max_h = 0
counter = 0

t0 = time.time()

for vx in vx_list:
    for vy in vy_list:
        x,y = 0,0
        vxx,vyy = vx,vy
        h = 0
        while y>y_target[0]:
            if vyy==0:
                h = y
            x += vxx
            y += vyy
            if vxx>0:
                vxx -= 1
            elif vxx <0:
                vxx += 1
            vyy -= 1
            if x in x_target and y in y_target:
                if vy>max_v[1]:
                    max_v = (vx,vy)
                    max_h = h
                counter+=1
                break
                
t1= time.time()
print(t1-t0)
print(max_h)
print(counter)
