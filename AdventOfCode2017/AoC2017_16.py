
with open("AoC2017_16_data.txt", "r") as f:
    data = f.read()

data = data.split(',')
ans = [0,0]

def dance(programs):
    for line in data:
        if line[0]=='s':
            l = int(line[1:])
            first_part,second_part = programs[:len(programs)-l],programs[len(programs)-l:]
            programs = second_part + first_part
        elif line[0]=='x':
            a,b = [int(x) for x in line[1:].split('/')]
            programs[a],programs[b] = programs[b],programs[a]
        else:
            a,b = line[1:].split('/')
            for i,program in enumerate(programs):
                if program == a:
                    idx_a = i
                if program == b:
                    idx_b = i
            programs[idx_a],programs[idx_b] = programs[idx_b],programs[idx_a]
    return programs

programs = [chr(ord('a')+x) for x in range(16)]
i = 0
seen = {}
while i < 1_000_000_000:
    s = ''.join(programs)
    if i == 1:
        ans[0] =s
    if s in seen:
        # cycle detected!
        cycle_length = i - seen[s]
        remaining = (1_000_000_000 - i) % cycle_length
        for _ in range(remaining):
            programs = dance(programs)
        break
    seen[s] = i
    programs = dance(programs)
    i += 1
    
ans[1] = ''.join(programs)
print(ans)