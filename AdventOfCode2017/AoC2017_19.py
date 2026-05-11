for file in ["AoC2017_19_test.txt","AoC2017_19_data.txt"]:

    with open(file, "r") as f:
        data = f.read()
        
    data = data.splitlines()

    G = [list(line) for line in data]
    R,C = len(G),len(G[0])
    
    DIR = {0:(0,-1),1:(1,0),2:(0,1),3:(-1,0)}
    ans = ['',0]
    
    r,c,d = 0,data[0].index('|'),1
            
    while True:
        if G[r][c] == ' ':
            break
        if G[r][c] in '|-':
            dr,dc = DIR[d]
            r+=dr
            c+=dc
            ans[1]+=1
        elif G[r][c] == '+':
            ans[1]+=1
            if 0<=c-1 and G[r][c-1] not in ' |' and d!=2:
                c=c-1
                d=0
            elif c+1<C and G[r][c+1] not in ' |' and d!=0:
                c=c+1
                d =2 
            elif 0<= r-1 and G[r-1][c] not in ' -' and d!=1:
                r=r-1
                d=3
            elif r+1 <R and G[r+1][c] not in ' -' and d!=3:
                r=r+1
                d=1
            else:
                dr,dc = DIR[d]
                r+=dr
                c+=dc
        else:
            ans[0] += G[r][c]
            G[r][c] = '+'

    print(ans)