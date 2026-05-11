from collections import defaultdict
for file in ["AoC2017_07_test.txt","AoC2017_07_data.txt"]:
    with open(file, "r") as f:
        data = f.read()
    data = data.splitlines()
    ans = [0,None]
    
    tower = {}
    weights = {}
    
    for line in data:
        if '>' in line:
            root,leaves = line.split(' -> ')
            root,weight = root.split()
            leaves = leaves.split(', ')
            tower[root] = leaves
            
        else:
           root,weight = line.split() 
        weights[root] = int(weight[1:-1])
        
    for node in tower:
        root = True
        for leaves in tower.values():
            if node in leaves:
                root = False
                break
        if root:
            ans[0] = node
            break
        
    def branch_weight(node):
        leaves_weight = []
        if node in tower:
            for leaf in tower[node]:
                leaves_weight.append((leaf,branch_weight(leaf)))
                
        if len(set(x[1] for x in leaves_weight))>1 and ans[1] == None:
            d = defaultdict(list)
            for (leaf,weight) in leaves_weight:
                d[weight].append(leaf)
            for weight in d:
                if len(d[weight])==1:
                    wrong_weight = weight
                else:
                    right_weight = weight
            ans[1] = weights[d[wrong_weight][0]]+right_weight-wrong_weight
    
        return weights[node] + sum([x[1] for x in leaves_weight])
        
    branch_weight(ans[0])
    print(ans)