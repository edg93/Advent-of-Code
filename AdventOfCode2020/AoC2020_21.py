with open("AoC2020_21_data.txt", "r") as file:
    data = file.read()
    
data=data.split('\n')
dataNew =[]
d = {}

for line in data:
    ingredients,allergens=line.split(' (contains ')
    ingredients=ingredients.split(' ')
    allergens=allergens[:-1].split(', ')
    dataNew += [ingredients]
    for allergene in allergens:
        if allergene not in d.keys():
            d[allergene]=set(ingredients)
        else:
            to_remove=set()
            for ingredient in d[allergene]:
                if ingredient not in ingredients:
                    to_remove.add(ingredient)
            for x in to_remove:
                d[allergene].remove(x)
            
for k in range(2):
    for key in d.keys():
        if len(d[key])==1:
            ingredient, = d[key]
            for key1 in d.keys():
                if key1!=key and ingredient in d[key1]:
                    d[key1].remove(ingredient)

keys = list(d.keys())
for key in keys:
    d[key], = d[key]

keys.sort()

ans1 = 0
for line in dataNew:
    for key in keys:
        if d[key] in line:
            line.remove(d[key])
    ans1 += len(line)
    
ans2 = ''
for key in keys:
    ans2 += ',' + d[key]

ans2 = ans2[1:]
print(ans1)
print(ans2)