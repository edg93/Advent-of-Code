from collections import defaultdict
with open('AoC2017_12_data.txt', "r") as f:
    data = f.read()


data = data.splitlines()
ans = [0,0]

links = defaultdict(set)
nodes = set()

for line in data:
    node,rest = line.split(' <-> ')
    node = int(node)
    rest = [int(x) for x in rest.split(', ')]
    nodes |= set(rest+[node])
    for node1 in rest:
        links[node].add(node1)
        links[node1].add(node)
        
def find_group(n):
    group = {n}
    stack = [n]
    while stack:
        node = stack.pop()
        for x in links[node]:
            if x not in group:
                group.add(x)
                stack.append(x)
    return group

while nodes:
    node = nodes.pop()
    group = find_group(node)
    
    if 0 in group:
        ans[0] = len(group)
    ans[1]+=1
    nodes -= group
    
print(ans)