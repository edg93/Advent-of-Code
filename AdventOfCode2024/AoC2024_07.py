from collections import deque 

with open("AoC2024_07_data.txt", "r") as file:
    data = file.read()

data = data.split('\n')

for p in [1,2]:
    ans = 0
    for line in data:
        result,factors = line.split(': ')
        result = int(result)
        factors = [int(x) for x in factors.split(' ')]
        Q = deque([])
        Q.append(factors)
        while Q:            
            factors = Q.popleft()
            a,b = factors[0],factors[1]
            if len(factors)==2:
                if result in {a*b,a+b}:
                    ans += result
                    break
                if p==2 and result == int(str(a)+str(b)):
                    ans += result
                    break
                continue
            Q.append([a*b]+factors[2:])
            Q.append([a+b]+factors[2:])
            if p==2:
                n = int(str(a)+str(b))
                Q.append([n]+factors[2:])
    print(ans)