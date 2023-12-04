with open("AoC2022_22_data.txt", "r") as file:
    data = file.read()
grid, instructions = data.strip().split('\n\n')
grid = grid.split('\n')
grid[0]=' '*50+grid[0]
#grid[0]=' '*8+grid[0]


G = {}
position1=0
position2=0
orientation1 = (1,0)
orientation2 = (1,0)
clockwise = {(1,0):(0,-1),(-1,0):(0,1),(0,1):(1,0),(0,-1):(-1,0)}
counterclockwise = {(1,0):(0,1),(-1,0):(0,-1),(0,1):(-1,0),(0,-1):(1,0)}

for l,line in enumerate(grid):
    for i in range(len(line)):
        if line[i]!=' ':
            if l==0 and position1 == 0:
                position1 = (i,0)
                position2 = (i,0)
            G[(i,l)]=line[i]

i = 0 

def change_face(position):
    x,y = position
    if y==50 and 100<=x<150:
        x1 = 99
        y1 = x-50
        orientation = (-1,0)
    elif 50<=y<100 and x==100:
        x1 = 50+y
        y1 = 49
        orientation = (0,1)
        
    elif x==150 and 0<=y<50:
        x1 = 99
        y1 = 149-y
        orientation = (-1,0)
    elif 100<=y<150 and x==100:
        x1 = 149
        y1 = 149-y
        orientation = (-1,0)
    
    elif 50<=x<100 and y==150:
        x1 = 49
        y1 = 100+x
        orientation = (-1,0)
    elif 150<=y<200 and x==50:
        x1 = y-100
        y1 = 149
        orientation = (0,1)
            
    elif y==99 and 0<=x<50:
        x1 = 50
        y1 = 50+x
        orientation = (1,0)
    elif 50<=y<100 and x==49:
        x1 = y-50
        y1 = 100
        orientation = (0,-1)
        
    elif y==200 and 0<=x<50:
        x1 = x+100
        y1 = 0
        orientation = (0,-1)
    elif y==-1 and 100<=x<150:
        x1 = x-100
        y1 = 199
        orientation = (0,1)
        
    elif 150<=y<200 and x==-1:
        x1 = y-100
        y1 = 0
        orientation = (0,-1)
    elif y==-1 and 50<=x<100:
        x1 = 0
        y1 = x+100
        orientation = (1,0)
         
    elif 100<=y<150 and x==-1:
        x1 = 50
        y1 = 149-y
        orientation = (1,0)
    elif 0<=y<50 and x==49: 
        x1 = 0
        y1 = 149-y
        orientation = (1,0)
    
    return (x1,y1),orientation

while i<len(instructions):
    if instructions[i]=='R':
        orientation1 = clockwise[orientation1]
        orientation2 = clockwise[orientation2]
        i+=1
    elif instructions[i]=='L':
        orientation1 = counterclockwise[orientation1]
        orientation2 = counterclockwise[orientation2]
        i+=1
    else:
        c = ''
        while i<len(instructions) and instructions[i] not in ['R','L']:
            c+=instructions[i]
            i+=1
        for k in range(int(c)):
            
            x1,y1=position1
            x2,y2=position2
            if position2==(49,189):
                print(orientation2, c)
            dx1,dy1=orientation1
            dx2,dy2=orientation2
            new_position1 = (x1+dx1,y1-dy1)
            new_position2 = (x2+dx2,y2-dy2)
            new_orientation2 = orientation2
            if new_position2 not in G.keys():
                new_position2,new_orientation2 = change_face(new_position2)
            if new_position1 not in G.keys():
                raw = [xx for (xx,yy) in G.keys() if yy==y1]
                column = [yy for (xx,yy) in G.keys() if xx==x1]
                if orientation1 == (1,0):
                    new_position1 = (min(raw),y1)
                elif orientation1 == (-1,0):
                    new_position1 = (max(raw),y1)
                elif orientation1 == (0,1):
                    new_position1 = (x1,max(column))
                else:
                    new_position1 = (x1,min(column))
            if G[new_position1]=='.':
                position1 = new_position1
            if G[new_position2]=='.':
                position2 = new_position2
                orientation2 = new_orientation2
    
def score(position,orientation):
    if orientation == (1,0):
        score = 0
    elif orientation == (-1,0):
        score = 2
    elif orientation == (0,1):
        score = 3
    else:
        score = 1
    return (position[1]+1)*1000+4*(position[0]+1)+score

print(score(position1,orientation1))
print(score(position2,orientation2))
