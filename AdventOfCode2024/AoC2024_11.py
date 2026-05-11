from collections import deque

s = '337 42493 1891760 351136 2 6932 73 0'
#s = '125 17'


stones = {}
for x in s.split():
    stones[int(x)]=1

def transform(n):
    if n==0:
        return [1]
    elif len(str(n))%2==0:
        ns = str(n)
        
        return [int(ns[len(ns)//2:]),int(ns[:len(ns)//2])]
        
    else: 
        return [n*2024]

def blink(stones):
    new_stones = {}

    for stone,dim in stones.items():
        stone_transformed = transform(stone)
        for new_stone in stone_transformed:
            if new_stone in new_stones.keys():
                new_stones[new_stone]+=dim
            else:
                new_stones[new_stone]=dim
    
    return new_stones

for i in range(75):
    stones = blink(stones)
    if i==24:
        ans1 = sum(stones.values())
    
ans2 = sum(stones.values())

print(ans1,ans2)
