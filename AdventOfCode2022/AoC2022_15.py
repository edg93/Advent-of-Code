with open("AoC2022_15_data.txt", "r") as file:
    data = file.read()
data=data.strip().split('\n')

def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
       raise Exception('lines do not intersect')

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return x, y

def distance(s,b):
    return abs(b[0]-s[0])+abs(b[1]-s[1])

y = 2000000
#y = 10
pairs = {}
ans1 = set()

for line in data:
    line = line.split()
    s = (int(line[2][2:-1]),int(line[3][2:-1]))
    b = (int(line[-2][2:-1]),int(line[-1][2:]))

    d = distance(b,s)
    dsy = abs(s[1]-y)
    pairs[(s,d)]=b
    if d-dsy>0:
        for c in range(d-dsy+1):
            ans1.add(s[0]+c)
            ans1.add(s[0]-c)

for r,c in pairs.values():
    if r==y and c in ans1:
        ans1.remove(c)

print(len(ans1))

for (x,y),d in pairs.keys():
    for (x1,y1),d1 in pairs.keys():
        xd,yd = x+d/2,y-d/2
        x1d,y1d = x1-d1/2,y1+d1/2
        q,q1 = yd-xd,y1d-x1d
        if 1<abs(q1-q)<4:
            L1 = ((x+d,y),(x,y-d))
            L2 = ((x1,y1+d1),(x1-d1,y1))

        yd,y1d = y+d/2,y1-d1/2
        q,q1 = yd+xd,y1d+x1d
        if 1<abs(q1-q)<4:
            L3 = ((x+d,y),(x,y+d))
            
print(int(line_intersection(L2, L3)[0]*4000000+line_intersection(L1, L3)[1]))