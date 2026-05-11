with open("AoC2024_05_data.txt", "r") as file:
    data = file.read()
    
rules,updates = data.split('\n\n')
rules = rules.split('\n')
updates = updates.split('\n')

ans1,ans2 = 0,0

d = {}

for rule in rules:
    p1,p2 = [ int(x) for x in rule.split('|')]
    if p1 in d.keys():
        d[p1].add(p2)
    else:
        d[p1]={p2}

for update in updates:
    update = [int(x) for x in update.split(',')]
    ok = True
    for i in range(len(update)):
        if not ok:
            break
        for j in range(i+1,len(update)):
            if not update[j] in d[update[i]]:
                ok = False
                break
    if ok:
        ans1 += update[len(update)//2]
    else:
        l = []
        while update:
            for i in range(len(update)):
                p1 = update[i]
                ok = True
                for j in range(len(update)):
                    p2 = update[j]
                    if p1 in d[p2]:
                        ok = False
                if ok:
                    l.append(p1)
                    update.remove(p1)
                    break

        ans2 += l[len(l)//2]

print(ans1,ans2)