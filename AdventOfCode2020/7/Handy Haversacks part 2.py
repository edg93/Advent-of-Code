f = open("prova.txt", "r")
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
            inside = inside + [[int(word), rule[i+2] + ' ' + rule[i+3]]]
    dictionary[colour] = inside

def bags(col):
    inside = dictionary[col]
    if inside==[]:
        return 1
    else:
        sum = 1
        for possibility in inside:
            sum = sum + possibility[0]*bags(possibility[1])
        return sum

print(bags('shiny gold')-1)