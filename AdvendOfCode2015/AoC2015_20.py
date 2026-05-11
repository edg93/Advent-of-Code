ans = [None,None]

TARGET = 34_000_000

# Upper bound guess (works fine for this problem)
MAX_HOUSES = 1_000_000
houses = [0] * (MAX_HOUSES)

for elf in range(1, MAX_HOUSES):
    for house in range(elf, MAX_HOUSES , elf):
        houses[house] += 10 * elf

for i, presents in enumerate(houses):
    if presents >= TARGET:
        ans[0]=i
        break
    
houses = [0] * (MAX_HOUSES)

for elf in range(1, MAX_HOUSES):
    for house in range(elf, min(elf*(50+1),MAX_HOUSES) , elf):
        houses[house] += 11 * elf

above_target = []

for i, presents in enumerate(houses):
    if presents >= TARGET:
        ans[1]=i
        break
    

print(ans)