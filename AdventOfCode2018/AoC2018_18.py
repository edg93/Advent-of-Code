for file in ["AoC2018_18_test.txt","AoC2018_18_data.txt"]:

    with open(file, "r") as f:
        data = f.read()
    
    def output(G):
        for r in range(R):
            print(''.join(G[r]))
            
    def adjacent_acres(r,c):
        l = []
        for dr in [-1,0,1]:
            for dc in [-1,0,1]:
                if dr==dc==0:
                    continue
                if 0<=r+dr<R and 0<=c+dc<C:
                    l.append((r+dr,c+dc))
        return l
    
    def simulate_minute(G):
        new_G = [row.copy() for row in G]

        for r in range(R):
            for c in range(C):
                adj = [G[r1][c1] for (r1,c1) in adjacent_acres(r,c)]
                if G[r][c] == '.':
                    if adj.count('|')>=3:
                        new_G[r][c]='|'
                elif G[r][c] == '|':
                    if adj.count('#')>=3:
                        new_G[r][c]='#'
                    
                elif G[r][c] == '#':
                    if '#' not in adj or '|' not in adj:
                        new_G[r][c] = '.'
        return new_G
    
    def value(G):
        lumberyards = sum(row.count('#') for row in G)
        woods = sum(row.count('|') for row in G)
        return lumberyards*woods
    
    data = data.splitlines()
    G = [list(line) for line in data]
    R,C = len(G),len(G[0])
    ans = [0,0]
    seen_states = {}
    total_minutes = 1_000_000_000
    minute = 0
    
    while minute < total_minutes:
        state = '\n'.join(''.join(row) for row in G)
        
        if minute == 10:
            ans[0] = value(G)
        
        if state in seen_states:
            cycle_start = seen_states[state]
            cycle_length = minute - cycle_start
            remaining = (total_minutes - cycle_start) % cycle_length
            
            for _ in range(remaining):
                G = simulate_minute(G)
            break
        
        seen_states[state] = minute
        G = simulate_minute(G)  
        minute += 1

    ans[1] = value(G)
    print(ans)