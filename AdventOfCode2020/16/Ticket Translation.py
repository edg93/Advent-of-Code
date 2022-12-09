f = open("data.txt", "r")
data = f.read()
data = data.split('\n\n')

rules,myTicket,tickets = data[0],data[1],data[2]

rules = rules.split('\n')
tickets = tickets.split('\n')[1:]
myTicket = myTicket.split('\n')[1]

error = 0

for k in range(len(rules)):
    rules[k] = rules[k].split(' ')
    rules[k] = [rules[k][-3],rules[k][-1]]
    rules[k] = [[int(rules[k][0].split('-')[0]),int(rules[k][0].split('-')[1])],[int(rules[k][1].split('-')[0]),int(rules[k][1].split('-')[1])]]
    
for k in range(len(tickets)):
    tickets[k] = tickets[k].split(',')
    for number in tickets[k]:
        n = int(number)
        ok = False
        for rule in rules:
            if (n >= rule[0][0] and n <= rule[0][1]) or (n >= rule[1][0] and n <= rule[1][1]):
                ok = True
                break
        if not ok:
            error = error + n
            
print(error)
