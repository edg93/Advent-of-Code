#Sugar: capacity 3, durability 0, flavor 0, texture -3, calories 2
#Sprinkles: capacity -3, durability 3, flavor 0, texture 0, calories 9
#Candy: capacity -1, durability 0, flavor 4, texture 0, calories 1
#Chocolate: capacity 0, durability 0, flavor -2, texture 2, calories 8


ingredients = ['sugar','sprinkles','candy','chocholate']

properties = {
    'capacity':    [ 3, -3, -1,  0],
    'durability':  [ 0,  3,  0,  0],
    'flavor':      [ 0,  0,  4, -2],
    'texture':     [-3,  0,  0,  2],
}

calories  = [2,9,1,8]

ans = [0,0]

for a in range(101):
    for b in range(101 - a):
        for c in range(101 - a - b):
            d = 100 - a - b - c
            
            amounts = [a, b, c, d]
            
            totals = []
            for prop in properties.values():
                total = sum(x*y for x, y in zip(prop, amounts))
                totals.append(max(total, 0))
            calory_total =sum(x*y for x,y in zip(calories,amounts))
            
            score = 1
            for t in totals:
                score *= t
            ans[0] = max(ans[0],score)
            if calory_total == 500:
                ans[1] = max(ans[1],score)
print(ans)