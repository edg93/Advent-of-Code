f = open("data.txt", "r")
data = f.read()
rules=data.split('\n')
f.close()

dictionary = {}

for k in range(len(rules)):
    rule = rules[k]
    rule = rule.split(' ')
    colour = rule[0] + ' ' + rule[1]
    inside = []
    for i in range(len(rule[2:])-2):
        word = rule[1+i]
        if word in '123456789':
            inside = inside + [rule[i+2] + ' ' + rule[i+3]]
    dictionary[colour] = inside

def check(col):
    inside = dictionary[col]
    if inside == []:
        return False
    if 'shiny gold' in inside:
        return True
    ok = False
    for value in inside:
        ok = ok or check(value)
    return ok

counter = 0
for colour in dictionary.keys():
    if colour != 'shiny gold':
        if check(colour):
            #print(colour, dict[colour])
            counter = counter + 1
    
print(counter)