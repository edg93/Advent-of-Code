from time import time

with open("AoC2022_16_data.txt", "r") as file:
    data = file.read()
data=data.strip().split('\n')

t0 = time()
valves = {}
opened_valves = set()
costs = {}

for line in data:
    line = line.split()
    valve = line[1]
    rate = int(line[4][5:-1])
    connections = set()
    for x in line[9:]:
        x = x.strip(',')
        connections.add(x)
        costs[(min(valve,x),max(valve,x))]=1
    valves[valve]=[rate,connections]
    if rate == 0:
        opened_valves.add(valve)

total_valves = len(valves)

def simplify(graph):
    modified = True
    while modified:
        modified = False
        for node in graph.keys():
            n,s = valves[node]
            if n==0 and len(s)==2 and node!='AA':
                modified = True
                remove_node(graph,node)
                opened_valves.remove(node)
                break
    for node in graph['AA'][1]:
        graph[node][1].remove('AA')       
    return graph

def remove_node(graph,node): #graph[node][1] deve avere dimensione 2
    node1,node2 = tuple(graph[node][1])
    graph[node1][1].remove(node)
    graph[node1][1].add(node2)
    graph[node2][1].remove(node)
    graph[node2][1].add(node1)
    del graph[node]
    costs[(min(node1,node2),max(node1,node2))]= costs[(min(node1,node),max(node1,node))] + costs[(min(node,node2),max(node,node2))]
    #del costs[(min(node1,node),max(node1,node))]
    #del costs[(min(node,node2),max(node,node2))]
    return graph
    
def move(position,time_left,opened_valves,current_pressure,last_pos,players):
    option = False
    #print(position, time_left,opened_valves)
    if time_left == 0:
        if players == 1:
            return 0
        else:
            return move('AA',26,opened_valves,0,'',players-1)
    key = (position,tuple(opened_valves),time_left,players)
    if key in dp:
        return dp[key]
    m = 0
    
    if position not in opened_valves : 
        option = True
        m = max(m,current_pressure + move(position,time_left-1,opened_valves|{position},current_pressure+valves[position][0],'',players))

    for valve in valves[position][1]:
        c=costs[min(position,valve),max(position,valve)]
        if time_left-c<0 or last_pos == valve:
            continue
        else:
            option = True
        if len(valves[position][1])==1 and position in opened_valves:
            m = max(m,c*current_pressure+move(valve,time_left-c,opened_valves,current_pressure,position,players))
        else:
            m = max(m,c*current_pressure+move(valve,time_left-c,opened_valves,current_pressure,position,players))
    if option == False:
        return time_left*current_pressure
    dp[key]=m
    return m

valves = simplify(valves)

current_pressure = 0
position = 'AA'
dp = {}

time_left = 30
ans1 = move(position,time_left,opened_valves,0,'',1)
print(ans1)
print(time()-t0)

time_left = 26
ans2 = move(position,time_left,opened_valves,0,'',2)
print(ans2)
print(time()-t0)

#print(n)