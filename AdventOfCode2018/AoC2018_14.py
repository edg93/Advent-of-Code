goal = '760221'
goal_digits = [int(c) for c in goal]
elf1,elf2 = 0,1
recipes = [3,7]
ans = [0,0]

def step(recipes,elf1,elf2):
    sum_recipes = recipes[elf1]+recipes[elf2]
    if sum_recipes >= 10:
        recipes.append(1)
    recipes.append(sum_recipes%10)
    elf1 += 1+recipes[elf1]
    elf1 %= len(recipes)
    elf2 += 1+recipes[elf2]
    elf2 %= len(recipes)
    return recipes,elf1,elf2

while len(recipes)<=int(goal)+10:
    recipes,elf1,elf2 = step(recipes,elf1,elf2)

s = ''
for i in recipes[int(goal):int(goal)+10]:
    s += str(i)
ans[0] = int(s)

elf1,elf2 = 0,1
recipes = [3,7]

while True:
    recipes,elf1,elf2 = step(recipes,elf1,elf2)
    L = len(recipes)
    if recipes[L-len(goal_digits):] == goal_digits:
        ans[1] = L-len(goal_digits)
        break
    if recipes[L-len(goal_digits)-1:-1] == goal_digits:
        ans[1] = L-1-len(goal_digits)
        break

print(ans)