from copy import copy

f = open("data.txt", "r")
data = f.read()
data=data.split('\n')
dataNew =[]
dict = {}

for line in data:
    line=line.split(' (')
    line[0]=line[0].split(' ')
    line[1]=line[1][9:]
    line[1]=line[1].split(', ')
    line[1][-1]=line[1][-1][:-1]
    dataNew = dataNew + [line[0]]
    for allergene in line[1]:
        #print(allergene)
        if allergene not in dict.keys():
            dict[allergene]=line[0]
        else:
            ingredientsCopy=copy(dict[allergene])
            for ingredient in dict[allergene]:
                if ingredient not in line[0]:
                    ingredientsCopy.remove(ingredient)
            dict[allergene]=ingredientsCopy
            
for k in range(2):
    for key in dict.keys():
        if len(dict[key])==1:
            ingredient = dict[key][0]
            for key1 in dict.keys():
                if key1!=key and ingredient in dict[key1]:
                    dict[key1].remove(ingredient)

keys = list(dict.keys())
for key in keys:
    dict[key] = dict[key][0]

keys.sort()

total = 0
for line in dataNew:
    for key in dict.keys():
        if dict[key] in line:
            line.remove(dict[key])
    total = total + len(line)
    
part2 = ''
for key in keys:
    part2 = part2 + ',' + dict[key]

part2 = part2[1:]
print(part2)
print(total)
