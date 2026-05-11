data = '.^..^....^....^^.^^.^.^^.^.....^.^..^...^^^^^^.^^^^.^.^^^^^^^.^^^^^..^.^^^.^^..^.^^.^....^.^...^^.^.'
ans = [0,0]

traps = set([i for i in range(len(data)) if data[i]=='^'])

def update(traps):
    new_traps = set()
    for pos in range(len(data)):
        if pos-1 in traps and pos in traps and pos+1 not in traps:
            new_traps.add(pos)
            continue
        if pos-1 not in traps and pos in traps and pos+1 in traps:
            new_traps.add(pos)
            continue
        if pos-1 in traps and pos not in traps and pos+1 not in traps:
            new_traps.add(pos)
            continue
        if pos+1 in traps and pos not in traps and pos-1 not in traps:
            new_traps.add(pos)
            continue
    return new_traps

def output(traps):
    s = ''
    for i in range(len(data)):
        if i in traps:
            s+='^'
        else:
            s+='.'
    print(s)
    
for i in range(400000):

    ans[1]+=len(data)-len(traps)
    if i == 39:
        ans[0]=ans[1]
    traps = update(traps)
    
print(ans)