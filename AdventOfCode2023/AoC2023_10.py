with open("AoC2023_10_data.txt", "r") as file:
    data = file.read()

data = data.split('\n')
R = len(data)
C = len(data[0])

G = [[data[r][c] for c in range (C)] for r in range(R)]

points = []
def show(G):
    for line in G:
        print(''.join(line))
        
def area(points):
    area = 0
    for x in range(len(points)):
        area += points[x][0]*(points[(x+1)%len(points)][1]-points[x-1][1])
    return abs(area)/2   

def perimeter(points):
    p = 0
    for x in range(len(points)):
        p+= abs(points[x-1][0]-points[x][0]+points[x-1][1]-points[x][1])
    return p

for r,line in enumerate(G):
    for c,letter in enumerate(line):
        if letter=='S':
            sr = r
            sc= c
            p0 = (r,c)
            points.append((r,c))
            exits = set()
            if sr-1>=0 and G[r-1][c] in {'F','L','-'}:
                exits.add('left')
            if sr+1<R and G[r+1][c] in {'J','7','-'}:
                exits.add('right')
            if sc-1>=0 and G[r][c-1] in {'F','7','|'}:
                exits.add('up')
            if sc+1<C and G[r][c+1] in {'L','7','|'}:
                exits.add('down')
            if exits == {'right','left'}:
                ss = '-'
                p1 = (r,c+1)
            elif exits == {'right','up'}:
                ss = 'L'
                p1 = (r,c+1)
            elif exits == {'right','down'}:
                ss = 'F'
                p1 = (r,c+1)
            elif exits == {'left','up'}:
                ss = 'J'
                p1 = (r,c-1)
            elif exits == {'left','down'}:
                ss = '7'
                p1 = (r,c-1)
            else:
                ss = '|'
                p1 = (r+1,c)
            break
        
def step(r,c,r_prev,c_prev):
    if G[r][c]=='-':
        if c_prev==c-1:
            return r,c+1
        else:
            return r,c-1
    elif G[r][c]=='|':
        if r_prev==r-1:
            return r+1,c
        else:
            return r-1,c
    elif G[r][c]=='L':
        points.append((r,c))
        if r_prev==r-1:
            return r,c+1
        else:
            return r-1,c
    elif G[r][c]=='J':
        points.append((r,c))
        if r_prev==r:
            return r-1,c
        else:
            return r,c-1
    elif G[r][c]=='F':
        points.append((r,c))
        if r_prev==r:
            return r+1,c
        else:
            return r,c+1
    elif G[r][c]=='7':
        points.append((r,c))
        if r_prev==r:
            return r+1,c
        else:
            return r,c-1

while p1 != points[0]:
    r,c = p1
    r_prev,c_prev = p0
    p1 = step(r,c,r_prev,c_prev)
    p0 = (r,c)

ans1 = int(perimeter(points)/2)
ans2 = int(area(points)-ans1+1)
print(ans1,ans2)