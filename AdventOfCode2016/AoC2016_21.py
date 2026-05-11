from collections import deque
with open("AoC2016_21_data.txt", "r") as f:
    data = f.read()
    
data = data.splitlines()
ans = [0,0]

def base_rotation(pw,a):
    i = pw.index(a)
    if i>=4:
        i+=1
    pw.rotate(i+1)
    return pw

def inverse_base_rotation(pw, a):
    n = len(pw)

    # Try all possible left rotations
    for i in range(n):
        candidate = pw.copy()
        candidate.rotate(-i)          # undo guess

        # Apply forward rule
        test = candidate.copy()
        base_rotation(test, a)

        if test == pw:
            return candidate

    raise ValueError("No valid inverse rotation found")

def apply(line, pw, reverse=False):
    line = line.split()

    if line[0] == 'swap':
        a, b = line[2], line[5]
        if line[1] == 'letter':
            i_a, i_b = pw.index(a), pw.index(b)
            pw[i_a], pw[i_b] = pw[i_b], pw[i_a]
        else:
            a, b = int(a), int(b)
            pw[a], pw[b] = pw[b], pw[a]

    elif line[0] == 'reverse':
        a, b = int(line[2]), int(line[4])
        pw[a:b+1] = reversed(pw[a:b+1])

    elif line[0] == 'rotate':
        pw = deque(pw)
        if line[1] == 'left':
            n = int(line[2])
            pw.rotate(n if reverse else -n)

        elif line[1] == 'right':
            n = int(line[2])
            pw.rotate(-n if reverse else n)

        elif line[1] == 'based':
            a = line[6]
            pw = inverse_base_rotation(pw, a) if reverse else base_rotation(pw, a)

        pw = list(pw)

    elif line[0] == 'move':
        a, b = int(line[2]), int(line[5])
        if reverse:
            a, b = b, a
        ch = pw.pop(a)
        pw.insert(b, ch)

    return pw

pw = list('abcdefgh')
for line in data:
    pw = apply(line,pw)
            
ans[0] = ''.join(pw)

pw = list('fbgdceah')
for line in reversed(data):
    pw = apply(line,pw,True)
        
ans[1] = ''.join(pw)
    
print(ans)