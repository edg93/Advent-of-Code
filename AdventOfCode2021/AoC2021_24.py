"Day 24 of AOC2021"
with open("AoC2021_24_data.txt", "r") as file:
    data = file.read()
    
data = data.split('\n')

my_variables = {'w':0,'x':0,'y':0,'z':0}
my_counter = 0
number = [ 9 for _ in range(14)]

scripts = []
s = []
for i,line in enumerate(data):
    if line.split()[0] == 'inp':
        if s != []:
            scripts.append(s)
        s = []
    s.append(line)

scripts.append(s)

def get_value(i,variables):
    try:
        return int(i)
    except ValueError:
        return variables[i]

def run_block(ip,script,variables):
    for line in script:
        line = line.split(' ')
        op,line = line[0],line[1:]
        if op == 'inp':
            variables[line[0]]=ip
        else:
            a,b = line
            b = get_value(b,variables)
            if op == 'add':
                variables[a]+=b
            elif op == 'mul':
                variables[a]*=b
            elif op == 'div':
                if b == 0:
                    return None
                variables[a] //= b
            elif op == 'mod':
                if variables[a]<0 or b <= 0:
                    return None
                variables[a] %= b
            elif op == 'eql':
                if variables[a]==b:
                    variables[a]=1
                else:
                    variables[a]=0
    return variables

def next_z(z, w, block):
    vars = {'w':0,'x':0,'y':0,'z':z}
    run_block(w, block, vars)
    return vars['z']


states = {0: ""}  # z -> model prefix

for i, block in enumerate(scripts):
    new_states = {}

    remaining = 14 - i - 1  # blocks left after this one

    for z, prefix in states.items():
        for w in range(1, 10):
            nz = next_z(z, w, block)

            # ❌ invalid ALU result
            if nz is None:
                continue

            # 🔪 PRUNE 2: mathematical bound
            if nz > 26 ** remaining:
                continue

            candidate = prefix + str(w)

            # keep best prefix for this nz
            if nz not in new_states or candidate > new_states[nz]:
                new_states[nz] = candidate

    states = new_states
    print(f"After block {i}: {len(states)} states")