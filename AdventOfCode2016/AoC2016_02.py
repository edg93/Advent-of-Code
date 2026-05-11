for file in ["AoC2016_02_test.txt","AoC2016_02_data.txt"]:
    with open(file, "r") as f:
        data = f.read()
        
    data = data.split('\n')
    DIR = {'U':(-1,0),'R':(0,1),'D':(1,0),'L':(0,-1)}
    ans = ['','']
    
    KEYPAD_2 = {
        (-2, 0): '1',
        (-1, -1): '2', (-1, 0): '3', (-1, 1): '4',
        (0, -2): '5', (0, -1): '6', (0, 0): '7', (0, 1): '8', (0, 2): '9',
        (1, -1): 'A', (1, 0): 'B', (1, 1): 'C',
        (2, 0): 'D',
    }
    
    r,c = 1,1
    
    for line in data:
        for ch in line:
            dr,dc = DIR[ch]
            if 0<=r+dr<3 and 0<=c+dc<3:
                r += dr
                c += dc
        ans[0] += str(r*3+c+1)
    
    ans[0] = int(ans[0])
    
    r,c = 0,-2
    
    for line in data:
        for ch in line:
            dr,dc = DIR[ch]
            nr, nc = r+dr, c+dc
            if (nr, nc) in KEYPAD_2:
                r, c = nr, nc
        ans[1] += KEYPAD_2[(r,c)]
    
    print(ans)