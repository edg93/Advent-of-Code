from collections import defaultdict
ans = [0,0]
state = 'A'
cursor = 0
slots = defaultdict(int)

for _ in range(12861455):
    if state == 'A':
        if slots[cursor]==0:
            slots[cursor]=1
            cursor += 1
            state = 'B'
        else:
            slots[cursor] = 0
            cursor -=1
            state = 'B'
    elif state == 'B':
        if slots[cursor]==0:
            slots[cursor]=1
            cursor -= 1
            state = 'C'
        else:
            slots[cursor] = 0
            cursor +=1
            state = 'E'
    elif state == 'C':
        if slots[cursor]==0:
            slots[cursor]=1
            cursor += 1
            state = 'E'
        else:
            slots[cursor] = 0
            cursor -=1
            state = 'D'
    elif state == 'D':
        slots[cursor]=1
        cursor -= 1
        state = 'A'
    elif state == 'E':
        if slots[cursor]==0:
            slots[cursor]=0
            cursor += 1
            state = 'A'
        else:
            slots[cursor] = 0
            cursor +=1
            state = 'F'
    elif state == 'F':
        if slots[cursor]==0:
            slots[cursor]=1
            cursor += 1
            state = 'E'
        else:
            slots[cursor] = 1
            cursor +=1
            state = 'A'
        
ans = sum(slots.values())
print(ans)