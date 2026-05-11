from collections import defaultdict
with open("AoC2016_10_data.txt") as f:
    data = f.read().strip()

data = data.splitlines()
ans = [0,0]

bots = defaultdict(list)
bots_connections = {}
outputs = {}
bot_or_output = {'output':False,'bot':True}

for line in data:
    line = line.split()
    if line[0] == 'value':
        bots[int(line[-1])].append(int(line[1]))
    else:
        bots_connections[int(line[1])] = (int(line[6]),bot_or_output[line[5]],int(line[-1]),bot_or_output[line[-2]])
        
def give_microchips(bot, state):
    bots = state["bots"]
    connections = state["connections"]
    outputs = state["outputs"]

    a, b = bots[bot]
    low, high = min(a, b), max(a, b)

    if (low, high) == (17, 61):
        state["compare_bot"] = bot

    low_target, low_is_bot, high_target, high_is_bot = connections[bot]

    # Give low chip
    if low_is_bot:
        bots[low_target].append(low)
        if len(bots[low_target]) == 2:
            give_microchips(low_target, state)
    else:
        outputs[low_target] = low

    # Give high chip
    if high_is_bot:
        bots[high_target].append(high)
        if len(bots[high_target]) == 2:
            give_microchips(high_target, state)
    else:
        outputs[high_target] = high

    bots[bot].clear()
    
    
state = {
    "bots": bots,
    "connections": bots_connections,
    "outputs": outputs,
    "compare_bot": None
}

for bot in bots:
    if len(bots[bot]) == 2:
        give_microchips(bot,state)
        break
        
ans[0] = state['compare_bot']
ans[1] = outputs[0]*outputs[1]*outputs[2]
        
print(ans)