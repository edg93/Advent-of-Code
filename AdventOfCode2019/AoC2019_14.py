with open("AoC2019_14_ex.txt", "r") as file:
    data = file.read()
    
data = data.split('\n')

d = {}

for n,line in enumerate(data):
    ingredients,output = line.split(' => ')
    output = output.split(' ')
    output[0] = int(output[0])
    output = tuple(output)
    ingredients = ingredients.split(', ')
    for k,ingredient in enumerate(ingredients):
        ingredient = ingredient.split(' ')
        ingredient[0] = int(ingredient[0])
        ingredients[k]=tuple(ingredient)
    d[output[1]] = output[0],tuple(ingredients)

print(d['FUEL'])

end = False

produced = {}
needed = {'FUEL':1}
while not end:
    for x,quantity_needed in needed.items():
        
        quantity, ingredients = d[x]
        if x in produced.keys():
            produced[x] += quantity
        else:
            produced[x] = quantity
        for n,ingredient in ingredients:
            print(ingredient)
            if ingredient in needed.keys():
                needed[ingredient] += n
            else:
                needed[ingredient] = n
        end = True

    if len(needed)==0:
        end = True