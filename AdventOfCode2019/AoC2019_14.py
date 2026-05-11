from collections import defaultdict
with open("AoC2019_14_data.txt", "r") as file:
    data = file.read()
    
data = data.split('\n')

reactions = {}
ans = [0,0]

for line in data:
    ingredients_str, output_str = line.split(' => ')
    out_qty, out_chem = output_str.split()
    out_qty = int(out_qty)
    
    ingredients = [ (int(qty), chem) for qty, chem in 
                    (ing.split() for ing in ingredients_str.split(', ')) ]
    
    reactions[out_chem] = (out_qty, ingredients)

def ore_required(fuel_amount):
    needs = [(fuel_amount, 'FUEL')]
    storage = defaultdict(int)
    ore = 0
    
    while needs:
        quantity, material = needs.pop()
        if material == 'ORE':
            ore += quantity
            continue
        if storage[material] >= quantity:
            storage[material] -= quantity
            continue
        quantity -= storage[material]
        storage[material] = 0
        
        produced, ingredients = reactions[material]
        times = -(-quantity // produced)  # ceiling division
        storage[material] += times * produced - quantity
        
        for n, ing in ingredients:
            needs.append((n * times, ing))
    return ore

ans[0] = ore_required(1)

# Binary search
low, high = 1, 10**12
while low < high:
    mid = (low + high + 1) // 2
    if ore_required(mid) <= 1_000_000_000_000:
        low = mid
    else:
        high = mid - 1

ans[1] = low
print(ans)