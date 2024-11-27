with open("AoC2023_25_data.txt", "r") as file:
    data = file.read()

data = data.split('\n')
ans1,ans2=0,0

nodes = set()
edges = {}

for line in data:
    start,ends = line.split(': ')
    ends = ends.split()
    nodes.add(start)
    for end in ends:
        nodes.add(end)
        if start in edges.keys():
            edges[start].append(end)
        else:
            edges[start] = [end]
        if end in edges.keys():
            edges[end].append(start)
        else:
            edges[end] = [start]
            
    