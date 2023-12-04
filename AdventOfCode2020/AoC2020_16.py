with open("AoC2020_16_data.txt", "r") as file:
    data = file.read()

rules,myTicket,tickets = data.split('\n\n')
myTicket = myTicket.split('\n')[1]

rules = rules.split('\n')
tickets = [tuple([int(y) for y in x.split(',')]) for x in tickets.split('\n')[1:]]
myTicket = tuple([int(x) for x in myTicket.split(',')])
rules_dict = {}

for rule in rules:
    rule = rule.split(' ')
    value,key = (rule[-3],rule[-1]),rule[0]
    if len(rule)==5:
        key += ' '+rule[1]
    value= tuple([tuple([int(x) for x in y.split('-')]) for y in value])
    rules_dict[key[:-1]]=value
    
poss,solution = {},{}
for rule in rules_dict.keys():
    poss[rule]=set([i for i in range(len(myTicket))])

ans1 = 0
for ticket in tickets:
    for i,n in enumerate(ticket):
        ok = False
        for int1,int2 in rules_dict.values():
            if int1[0]<=n<=int1[1] or int2[0]<=n<=int2[1]:
                ok = True
                break
        if not ok:
            ans1 += n
        else:
            for rule,(int1,int2) in rules_dict.items():
                if i in poss[rule] and not (int1[0]<=n<=int1[1] or int2[0]<=n<=int2[1]):
                    poss[rule].remove(i)
print(ans1)

ans2 = 1
while True:
    for rule in rules_dict.keys():
        a = poss[rule]-set(solution.values())
        if len(a)==1:
            solution[rule],=list(a)
    if len(solution)==len(poss):
        break

for rule in rules_dict.keys():
    if rule.split()[0]=='departure':
        ans2 *= myTicket[solution[rule]]
print(ans2)