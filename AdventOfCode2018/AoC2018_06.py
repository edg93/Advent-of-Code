for file in ["AoC2018_06_test.txt","AoC2018_06_data.txt"]:
    with open(file, "r") as f:
        data = f.read()        

    data = data.split('\n')
    ans = [0,0]
    X = [10e9,0]
    Y = [10e9,0]
    
    
    points = set()
    areas = {}
    infinite_areas = set()
        
    for line in data:
        x,y = [int(n) for n in line.split(', ')]
        X=[min(X[0],x),max(X[1],x)]
        Y=[min(Y[0],y),max(Y[1],y)]
        points.add((x,y))
    
    
    def distance(p1,p2):
        x1,y1 = p1
        x2,y2 = p2
        return abs(x1-x2)+abs(y1-y2)
    
    for x in range(X[0],X[1]+1):
        for y in range(Y[0],Y[1]+1):
            d = 0    
            distances = []
            for point in points:
                distances.append((distance((x,y),point),point))
                d+=distances[-1][0]
                
            distances.sort()
            if distances[0][0]<distances[1][0]:
                if distances[0][1] in areas.keys():
                    areas[distances[0][1]] +=1    
                else:
                    areas[distances[0][1]] = 1
                    
            if (x in X) or (y in Y):
                infinite_areas.add(distances[0][1])
                
            if file == "AoC2018_06_test.txt":
                limit = 32
            else:
                limit = 10000
                
            if d<limit:
                ans[1]+=1

    for point in points:
        if point not in infinite_areas:
            ans[0]=max(ans[0],areas[point])
            

    print(ans)
            
