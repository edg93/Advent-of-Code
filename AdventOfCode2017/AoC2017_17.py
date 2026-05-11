from collections import deque
data = 382
ans = [0,0]

Q = deque([])

for i in range(2018):
    Q.rotate(-data)
    Q.append(i)
    
ans[0] = Q[0]

Q = deque([])

pos = 0
value_after_0 = None

for i in range(1, 50_000_001):
    pos = (pos + data) % i + 1
    if pos == 1:
        value_after_0 = i

ans[1] = value_after_0
print(ans)