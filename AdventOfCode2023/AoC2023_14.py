for file in ["AoC2023_14_test.txt","AoC2023_14_data.txt"]:

    with open(file, "r") as f:
        data = f.read()
    
    data = data.split('\n')
    R,C = len(data),len(data[0])
    G = [[data[r][c] for c in range(C)] for r in range(R)]
    ans = [0,0]
    
    def tilt_line(line, forward=True):
        """
        line: list of characters ('.', 'O', '#')
        forward=True  → rocks go to the start
        forward=False → rocks go to the end
        """
        n = len(line)
        out = line[:]          # copy
        i = 0
    
        while i < n:
            if line[i] == '#':
                i += 1
                continue
            j = i
            while j < n and line[j] != '#':
                j += 1
            segment = line[i:j]
            rocks = segment.count('O')
            spaces = len(segment) - rocks
            if forward:
                out[i:j] = ['O'] * rocks + ['.'] * spaces
            else:
                out[i:j] = ['.'] * spaces + ['O'] * rocks
            i = j
        return out
    
    def tilt_north(G):
        for c in range(C):
            col = [G[r][c] for r in range(R)]
            col = tilt_line(col, forward=True)
            for r in range(R):
                G[r][c] = col[r]
    
    def tilt_south(G):
        for c in range(C):
            col = [G[r][c] for r in range(R)]
            col = tilt_line(col, forward=False)
            for r in range(R):
                G[r][c] = col[r]
    
    def tilt_west(G):
        for r in range(len(G)):
            G[r] = tilt_line(G[r], forward=True)
    
    def tilt_east(G):
        for r in range(len(G)):
            G[r] = tilt_line(G[r], forward=False)
    
    def compute_load(G):
        load = 0
        for c in range(C):
            value = R
            for r in range(R):
                if G[r][c] == '#':
                    value = R - r
                elif G[r][c] == 'O':
                    load += value
                value -= 1
        return load
        
    def output():
        for r in range(R):
            s = ''
            for c in range(C):
                s+=G[r][c]
            print(s)
        
    seen = {}
    step = 0
    N = 1000000000
    while True:
        state = tuple(tuple(row) for row in G)
        if state in seen:
            start = seen[state]
            cycle_len = step - start
            break
    
        tilt_north(G)
        if ans[0]==0:
            ans[0] = compute_load(G)
        tilt_west(G)
        tilt_south(G)
        tilt_east(G)
        seen[state] = step
        step += 1
        
    
    remaining_cycles = (N - start) % cycle_len
    for _ in range(remaining_cycles):
        tilt_north(G)
        tilt_west(G)
        tilt_south(G)
        tilt_east(G)
    
    ans[1] = compute_load(G)
            
        
    print(ans)
