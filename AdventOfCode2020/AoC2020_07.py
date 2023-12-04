with open("AoC2020_07_data.txt", "r") as file:
    data = file.read()
rules=data.split('\n')

dictionary = {}

for rule in rules:
    rule = rule.split(' ')
    colour = rule[0] + ' ' + rule[1]
    inside = []
    for i in range(len(rule[2:])-2):
        word = rule[1+i]
        if word in '123456789':
            inside.append((int(word),rule[i+2] + ' ' + rule[i+3]))
    dictionary[colour] = inside

def check(col):
    inside = dictionary[col]
    if inside == []:
        return False
    if 'shiny gold' in [x[1] for x in inside]:
        return True
    for value in inside:
        if check(value[1]):
            return True
    return False

def bags(col):
    inside = dictionary[col]
    if inside==[]:
        return 0
    else:
        s = 0
        for possibility in inside:
            s += possibility[0]*(bags(possibility[1])+1)
        return s

ans1 = 0
for colour in dictionary.keys():
    if colour != 'shiny gold' and check(colour):
        ans1 += 1
    
print(ans1)
print(bags('shiny gold'))