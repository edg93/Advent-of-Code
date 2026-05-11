from collections import deque

for file in ["AoC2018_15_test.txt","AoC2018_15_data.txt"]:
    
    def parsing(filename):
        with open(filename, "r") as file:
            data = file.read()
            
        data = data.split('\n')
        R,C = len(data),len(data[0])
        G = [[None for _ in range(C)] for _ in range(R)]
        
        units = {}
        for r in range(R):
            for c in range(C):
                G[r][c] = data[r][c]
                if G[r][c] in 'EG':
                    units[(r,c)] = [data[r][c],200]
        return G,R,C,units
            
    def output(G):
        for r in range(R):
            s = ''
            for c in range(C):
                s+=G[r][c]
            print(s)
        print()
        
    def move(pos):
        team = units[pos][0]
        enemies = [pos for pos, value in units.items() if value[0] != team]
        targets =  []
        for enemy in enemies:
            r,c = enemy
            for dr,dc in DIR:
                if 0<=r+dr<R and 0<=c+dc<C and G[r+dr][c+dc]=='.':
                    targets.append((r+dr,c+dc))
        
        distances = BFS(pos)
        
        reachable = [t for t in targets if t in distances]
        if not reachable:
            return pos #doesn't move if there are no reachable targets
        
        min_dist = min(distances[t] for t in reachable)
        
        chosen = min([t for t in reachable if distances[t] == min_dist], key=lambda x: (x[0], x[1]))
        distances = BFS(chosen)
        r,c = pos
        steps = []
        for dr,dc in DIR:
            nxt = (r+dr, c+dc)
            if nxt in distances and distances[nxt] == min_dist - 1:
                steps.append(nxt)
        
        return min(steps, key=lambda x: (x[0], x[1]))
        
    def BFS(start):
        distances = {start:0}
        Q = deque([start])
        while Q:
            r,c = Q.popleft()
            for dr,dc in DIR:
                rr,cc = r+dr,c+dc
                if 0<=rr<R and 0<=cc<C and G[rr][cc]=='.' and (rr,cc) not in distances:
                    distances[(rr,cc)]=distances[(r,c)]+1
                    Q.append((rr,cc))
        return distances
    
    def attack(pos,elf_attack=3):
        r,c = pos
        team,_ = units[(r,c)]
        enemies = []
        for dr,dc in DIR:
            p = (r+dr,c+dc)
            if p in units and units[p][0]!=team:
                enemies.append(p)
                
        if not enemies:
            return False
        target = min(enemies, key=lambda p: (units[p][1], p[0], p[1]))
        if team == 'E':
            units[target][1] -= elf_attack
        else:
            units[target][1] -= 3
        if units[target][1] <= 0:
            del units[target]
            G[target[0]][target[1]] = '.'
        return True
    
    def turn(G,elf_attack):
        units_in_order = sorted(units.keys(), key=lambda x: (x[0], x[1]))
        for pos in units_in_order:
            if pos not in units:
                continue  # died earlier this round
                
            team, hp = units[pos]

            r,c = pos
            if not any(u[0] != team for u in units.values()):
                return False

            # 1) try to attack
            if attack(pos,elf_attack):
                continue
    
            # 2) move
            new_pos = move(pos)
            if new_pos != pos:
                del units[pos]
                units[new_pos] = [team, hp]
                G[pos[0]][pos[1]] = '.'
                G[new_pos[0]][new_pos[1]] = team
                pos = new_pos
    
            # 3) try to attack again
            attack(pos,elf_attack)
            
            elfs_now = len([u for u in units if units[u][0]=='E'])
            if elf_attack>3 and elfs_now != initial_elfs:
                return False #match interrupted, elfs lost
            
        return True #match_ongoing
    
    ans = [None,None]
    DIR = ((-1,0),(0,-1),(0,1),(1,0))
    elf_attack = 3
    while not ans[1]:
        rounds = 0
        G,R,C,units = parsing(file)
        initial_elfs = sum(1 for u in units.values() if u[0] == 'E')
        match_ongoing = True
        while match_ongoing:
            match_ongoing = turn(G,elf_attack)
            if match_ongoing:
                rounds += 1
        if elf_attack == 3:
            total_hp = sum(u[1] for u in units.values())
            ans[0] = rounds * total_hp
        if initial_elfs == sum(1 for u in units.values() if u[0]=='E'):
            total_hp = sum(u[1] for u in units.values())
            ans[1] = rounds * total_hp
            break
        elf_attack+=1

    print(ans)