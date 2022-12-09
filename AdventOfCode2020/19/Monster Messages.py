f = open("prova.txt", "r")
data = f.read()
data=data.split('\n')

rules = {}
reverserules = {}
message = []
for line in data:
    if line[0].isdigit():
        n = line[0]
        line = line [1:]
        for letter in line:
            if letter.isdigit():
                n = n + letter
                line = line [1:]
            else:
                break
        line = line[2:]
        if '|' in line:
            line = line.split(' | ')
        else:
            line = [line]
        for k in range(len(line)):
            line[k] = line[k].split(' ')
        rules[n]=line
    else:
        message.append(line)

for rule in rules:
    print(rule, rules[rule])
    for k in range(len(rules[rule])):
        a = rules[rule][k]
        for j in range(len(a)):
            b = a[j]
            if b not in reverserules.keys():
                reverserules[b]=[(rule,k,j)]
            else:
                reverserules[b].append((rule,k,j))
print()
for rule in rules:
    ab = True
    for i in range(len(rules[rule])):
        for j in range(len(rules[rule][i])):
            if rules[rule][i][j].isnumeric():
                ab = False
                break

    if ab:
        for appearance in reverserules[rule]:
            #for a in 
            rules[appearance[0]][appearance[1]][appearance[2]]=rules[rule]
        
for rule in rules:
    print(rule,rules[rule])
            
        