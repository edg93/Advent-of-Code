from collections import deque

for file in ["AoC2024_21_test.txt","AoC2024_21_data.txt"]:

    with open(file, "r") as f:
        data = f.read()

    data = data.split('\n')

    ans = [0,0]
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    buttons_dict = {(0,1):'>',(0,-1):'<',(1,0):'v',(-1,0):'^'}

    def num_pad_shortest_path(outputs,start):
        shortest_paths = set()
        G = [['7','8','9'],['4','5','6'],['1','2','3'],[None,'0','A']]
        R,C = 4,3
        for output in outputs:
            costs = [[10e4 for _ in range(C)] for _ in range(R)]
            Q = deque([])
            Q.append((start,0,0,'',costs))
            while Q:
                pos,index,cost,sequence,costs = Q.popleft()
                r,c = pos
                if costs[r][c] < cost:
                    continue
                costs[r][c]=cost
                if index == len(output):
                    shortest_paths.add(sequence)
                    continue
                if G[r][c] == output[index]:
                    costs = [[10e4 for _ in range(C)] for _ in range(R)]
                    Q.append((pos,index+1,cost+1,sequence+'A',costs))
                    continue
                for dr,dc in directions:
                    if 0<=r+dr<R and 0<=c+dc<C and G[r+dr][c+dc]!=None:
                        Q.append(((r+dr,c+dc),index,cost+1,sequence+buttons_dict[(dr,dc)],costs))
        return shortest_paths
    
            
    def dir_pad_shortest_path(outputs,start):
        G = [[None,'^','A'],['<','v','>']]
        R,C = 2,3
        shortest_paths = set()

        for output in outputs:
            costs = [[10e4 for _ in range(C)] for _ in range(R)]
            Q = deque([])
            Q.append((start,0,0,'',costs))
            while Q:
                pos,index,cost,sequence,costs = Q.popleft()
                r,c = pos
                if costs[r][c] < cost:
                    continue
                costs[r][c]=cost
                if index == len(output):
                    shortest_paths.add(sequence)
                    continue
                if G[r][c] == output[index]:
                    costs = [[10e4 for _ in range(C)] for _ in range(R)]
                    Q.append((pos,index+1,cost+1,sequence+'A',costs))
                    continue
                for dr,dc in directions:
                    if 0<=r+dr<R and 0<=c+dc<C and G[r+dr][c+dc]!=None:
                        Q.append(((r+dr,c+dc),index,cost+1,sequence+buttons_dict[(dr,dc)],costs))
        return shortest_paths
            
    for line in data:
        print(line)
        first_pad = num_pad_shortest_path([line],(3,2))
        
        second_pad = dir_pad_shortest_path(first_pad,(0,2))
        d =  {}
        
        for x in second_pad:
            if len(x) not in d.keys():
                d[len(x)]={x}
            else:
                d[len(x)].add(x)
        min_length = min([x for x in d.keys()])
        second_pad = d[min_length]
        #second_pad = [min(second_pad)]
        third_pad = dir_pad_shortest_path(second_pad,(0,2))

        cost = min([len(x) for x in third_pad])
        print(cost)
        ans[0] += cost*int(line[:-1])
        
    print(ans)

    #1 69408
    #2 86628
    #3 152792
    #4 199168
    #5 