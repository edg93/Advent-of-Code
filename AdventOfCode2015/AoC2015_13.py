from collections import deque

for file in ["AoC2015_13_test.txt","AoC2015_13_data.txt"]:
    with open(file) as f:
        data = f.read()
        
    data = data.split('\n')
    ans = [0,0]
    guests = set()
    
    pairs = {}
    
    for line in data:
        name_1,_,factor,x,_,_,_,_,_,_,name_2 = line[:-1].split()

        pair = [name_1,name_2]
        guests.add(name_1)
        guests.add(name_2)
        pair.sort()
        pair = tuple(pair)
        if factor == 'gain':
            factor = 1
        else:
            factor = -1
        if pair in pairs:
            pairs[pair]+=factor*int(x)
        else:
            pairs[pair]=factor*int(x)
    
    Q = deque([])
    Q.append((['Alice'],0))
    
    while Q:
        table,happiness = Q.pop()
        if len(table)==len(guests):
            pair = [table[0],table[-1]]
            pair.sort()
            
            ans[0]=max(ans[0],happiness+pairs[tuple(pair)])
            continue
        last_person = table[-1]
        for next_person in guests:
            if next_person not in table:
                pair = [last_person,next_person]
                pair.sort()
                Q.append((table+[next_person],happiness+pairs[tuple(pair)]))
        
    me = 'me' #lower case so when I order the pair I am always last
    
    for person in guests:
        pairs[(person,me)]=0
    guests.add(me)
    
    Q = deque([])
    Q.append((['Alice'],0))
    
    while Q:
        table,happiness = Q.pop()
        if len(table)==len(guests):
            pair = [table[0],table[-1]]
            pair.sort()
            
            ans[1]=max(ans[1],happiness+pairs[tuple(pair)])
            continue
        last_person = table[-1]
        for next_person in guests:
            if next_person not in table:
                pair = [last_person,next_person]
                pair.sort()
                Q.append((table+[next_person],happiness+pairs[tuple(pair)]))
        
    print(ans)
