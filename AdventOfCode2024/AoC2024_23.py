from collections import defaultdict



for file in ["AoC2024_23_test.txt","AoC2024_23_data.txt"]:
    with open(file, "r") as f:
        data = f.read()

    data = data.split('\n')
    ans = [0,0]
    
    pairs = set()
    computers = set()
    adj = defaultdict(set)

       
    for line in data:
        pairs.add(tuple(line.split('-')))
        for computer in line.split('-'):
            computers.add(computer)
        a, b = line.split('-')
        adj[a].add(b)
        adj[b].add(a)
        
        
    triplets =set()
    
    def bronk(R, P, X, cliques):
        if not P and not X:
            cliques.append(R)
            return
        for v in list(P):
            bronk(
                R | {v},
                P & adj[v],
                X & adj[v],
                cliques
            )
            P.remove(v)
            X.add(v)
            
    cliques = []
    bronk(set(), set(adj.keys()), set(), cliques)
    largest = max(cliques, key=len)
    ans[1] = ",".join(sorted(largest))
    

    for pair in pairs:
        computer1,computer2 = pair
        for computer3 in adj[computer1]:
            if 't' not in [computer1[0],computer2[0],computer3[0]]:
                continue
            if (computer1,computer3) in pairs or (computer3,computer1) in pairs:
                if (computer2,computer3) in pairs or (computer3,computer2) in pairs:
                    triplets.add((computer1,computer2,computer3))
                
    groups = {}
    ans[0]=len(triplets)//3
    print(ans)