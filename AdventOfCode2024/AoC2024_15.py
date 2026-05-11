from collections import deque

for file in ["AoC2024_15_test.txt","AoC2024_15_data.txt"]:
    with open(file, "r") as f:
        data = f.read()        

    ans = [0,0]
    direction = {'>':(0,1),'<':(0,-1),'^':(-1,0),'v':(1,0)}
    
    grid,moves = data.split('\n\n')
    grid = grid.split('\n')
    
    R = len(grid)
    C = len(grid[0])
    R2 = R
    C2 = 2*C
    G = []
    G2 = []
    boxes =set()
    for r in range(R):
        G.append([])
        G2.append([])
        for c in range (C):
            G[r].append(grid[r][c])
            if G[r][c]=='@':
                robot = (r,c)
                G[r][c]='.'
                G2[r]+=['.','.']
            elif G[r][c]=='.':
                G2[r]+=['.','.']
            elif G[r][c]=='#':
                G2[r]+=['#','#']
            else:
                G2[r]+=['.','.']
                boxes.add((r,2*c))
                
                
    robot2 = (robot[0],2*robot[1])
    
    def output(G):
        R = len(G)
        C = len(G[0])
        for r in range(R):
            s=''
            for c in range(C):
                s+=G[r][c]
            print(s)
    
    def find_last_ball(r,c,dr,dc):
        while G[r+dr][c+dc]=='O':
            r+=dr
            c+=dc
        if G[r+dr][c+dc]=='#':
            return(r,c),False
        else:
            return(r,c),True
        
    def compute_GPS(G):
        GPS_sum = 0
        for r in range(R):
            for c in range(C):
                if G[r][c]=='O':
                    GPS_sum+=100*r+c
        return GPS_sum
    
    def move_boxes_vertically(r,c,dr,boxes):
        moved = True
        boxes_to_move = set()
        Q = deque([	])
        if (r+dr,c) in boxes:
            Q.append((r+dr,c))
            boxes_to_move.add((r+dr,c))
        elif (r+dr,c-1) in boxes:
            Q.append((r+dr,c-1))
            boxes_to_move.add((r+dr,c-1))
        
        while Q:
            r_box,c_box = Q.pop()
            if G2[r_box+dr][c_box]=='#' or G2[r_box+dr][c_box+1]=='#':
                moved = False
                break
            if (r_box+dr,c_box) in boxes:
                boxes_to_move.add((r_box+dr,c_box))
                Q.append((r_box+dr,c_box))
            if (r_box+dr,c_box-1) in boxes:
                Q.append((r_box+dr,c_box-1))
                boxes_to_move.add((r_box+dr,c_box-1))
            if (r_box+dr,c_box+1) in boxes:
                Q.append((r_box+dr,c_box+1))
                boxes_to_move.add((r_box+dr,c_box+1))
        if moved:
            boxes_to_add =set()
            for (r,c) in boxes_to_move:
                
                boxes.remove((r,c))
                boxes_to_add.add((r+dr,c))
            boxes |= boxes_to_add
        return moved,boxes
    
    def move_boxes_horizontally(r,c,dc,boxes):
        moved = False
        if dc == -1:
            factor = 2
        else:
            factor =1
        boxes_to_move = {(r,c+factor*dc)}
        c+=factor*dc
        while (r,c+2*dc) in boxes:
            boxes_to_move.add((r,c+2*dc))
            c+=2*dc
        if dc==-1:
            factor =1
        else:
            factor=2
        if G2[r][c+factor*dc]=='.':
            moved = True
            for (r,c) in boxes_to_move:
                boxes.remove((r,c))
                boxes.add((r,c+dc))

        return moved, boxes
    
    def output2(G2,boxes,robot2):
        for r in range(R2):
            s = ''
            for c in range(C2):
                if robot2 == (r,c):
                    s+='@'
                elif (r,c) in boxes:
                    s+='['
                elif (r,c-1) in boxes:
                    s+=']'
                else:
                    s+=G2[r][c]
            print(s)

    for move in moves:
        if move == '\n':
            continue
        dr,dc = direction[move]
        r,c = robot
        if G[r+dr][c+dc]!='#':
            if G[r+dr][c+dc]=='.':
                robot = (r+dr,c+dc)
            else:
                last_ball,free=find_last_ball(r,c,dr,dc)
                if free:
                    last_ball_r,last_ball_c = last_ball
                    G[last_ball_r+dr][last_ball_c+dc]='O'
                    G[r+dr][c+dc]='.'
                    robot = (r+dr,c+dc)
        r,c = robot2
        if G2[r+dr][c+dc]!='#':
            if dc==0 and (r+dr,c) not in boxes and (r+dr,c-1) not in boxes:
                robot2 = (r+dr,c+dc)
            elif dc==1 and (r,c+dc) not in boxes:
                robot2 = (r+dr,c+dc)
            elif dc==-1 and (r,c+2*dc) not in boxes:
                robot2 = (r+dr,c+dc)
            else:
                if dr == 0:
                    moved,boxes = move_boxes_horizontally(r,c,dc,boxes)
                else:
                    moved,boxes = move_boxes_vertically(r,c,dr,boxes)

                if moved:
                    robot2 = (r+dr,c+dc)
                    
    for box in boxes:
        ans[1]+= 100*box[0]+box[1]
    ans[0]=compute_GPS(G)

    print(ans)