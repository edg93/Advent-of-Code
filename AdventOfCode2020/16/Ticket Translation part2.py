f = open("data.txt", "r")
data = f.read()
data = data.split('\n\n')
rules,myTicket,tickets = data[0],data[1],data[2]
rules = rules.split('\n')
myTicket = myTicket.split('\n')[1]
tickets = [myTicket] + tickets.split('\n')[1:]
myTicket = myTicket.split(',')

for k in range(len(rules)):
    rules[k] = rules[k].split(' ')
    rules[k] = [rules[k][-3],rules[k][-1],rules[k][0][:2]]
    rules[k] = [[int(rules[k][0].split('-')[0]),int(rules[k][0].split('-')[1])],[int(rules[k][1].split('-')[0]),int(rules[k][1].split('-')[1])],rules[k][2]]

possibilities = []
for k in range(len(rules)):
    possibilities.append([])
    for j in range(len(rules)):
        possibilities[k].append([j,1])
    
for k in range(len(tickets)):
    tickets[k] = tickets[k].split(',')
    for i in range(len(tickets[k])):
        n = int(tickets[k][i])
        ok = False
        for rule in rules:
            if (n >= rule[0][0] and n <= rule[0][1]) or (n >= rule[1][0] and n <= rule[1][1]):
                ok = True
                break
        if not ok:
            break
        for j in range(len(rules)):
            rule = rules[j]
            if not ((n >= rule[0][0] and n <= rule[0][1]) or (n >= rule[1][0] and n <= rule[1][1])):
                possibilities[j][i][1] = 0
      
possCopy = [[] for x in possibilities]

for k in range(len(possibilities)):
    possCopy[k] = [x[0] for x in possibilities[k] if x[1]==1]

finish = False
solution = {}

while not finish:
    for k in range(len(possCopy)):
        a = [item for item in possCopy[k] if item not in list(solution.values())]
        if len(a)==1:
            solution[k]=a[0]
    if len(solution)==len(possCopy):
        finish = True
    
product = 1

for k in range(len(rules)):
    if rules[k][2]=='de':
        product = product*(int(myTicket[solution[k]]))

print(product)