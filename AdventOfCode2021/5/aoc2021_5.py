f = open("data.txt", "r")
data = f.read()
data=data.split('\n')
f.close()

#PART 1
points = {}

def result(points):
    counter = 0
    for key in points.keys():
        if points[key]>1:
            counter+=1
    return counter

for line in data:
    line = line.split(' -> ')
    x1,y1 = [int(x) for x in line[0].split(',')]
    x2,y2 = [int(x) for x in line[1].split(',')]
    if x1==x2:
        for i in range(abs(y2-y1)+1):
            if(x1,min(y1,y2)+i) not in points.keys():
                points[(x1,min(y1,y2)+i)]=1
            else:
                points[(x1,min(y1,y2)+i)]+=1
    
    if y1==y2:
        for i in range(abs(x2-x1)+1):
            if(min(x1,x2)+i,y1) not in points.keys():
                points[(min(x1,x2)+i,y1)]=1
            else:
                points[(min(x1,x2)+i,y1)]+=1
    
print(result(points))

#PART 2            
points = {}

for line in data:
    line = line.split(' -> ')
    x1,y1 = [int(x) for x in line[0].split(',')]
    x2,y2 = [int(x) for x in line[1].split(',')]
    if x1==x2:
        for i in range(abs(y2-y1)+1):
            if(x1,min(y1,y2)+i) not in points.keys():
                points[(x1,min(y1,y2)+i)]=1
            else:
                points[(x1,min(y1,y2)+i)]+=1
    
    if y1==y2:
        for i in range(abs(x2-x1)+1):
            if(min(x1,x2)+i,y1) not in points.keys():
                points[(min(x1,x2)+i,y1)]=1
            else:
                points[(min(x1,x2)+i,y1)]+=1
    
    if abs(x1-x2)==abs(y1-y2):
        for i in range(abs(x1-x2)+1):
            if (x2-x1>0 and y2-y1>0) or (x2-x1<0 and y2-y1<0):
                if(min(x1,x2)+i,min(y1,y2)+i) not in points.keys():
                    points[(min(x1,x2)+i,min(y1,y2)+i)]=1
                else:
                    points[(min(x1,x2)+i,min(y1,y2)+i)]+=1
            else:
                if(min(x1,x2)+i,max(y1,y2)-i) not in points.keys():
                    points[(min(x1,x2)+i,max(y1,y2)-i)]=1
                else:
                    points[(min(x1,x2)+i,max(y1,y2)-i)]+=1

print(result(points))