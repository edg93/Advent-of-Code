from collections import defaultdict
for file in ["AoC2017_23_data.txt"]:
    with open(file, "r") as f:
        data = f.read()
        
data = data.splitlines()
program = [line.split() for line in data]
ans = [0,0]

def get_value(p,registers):
    try:
        return int(p)
    except ValueError:
        return registers[p]

def run_line(i,registers):
    op, X, Y = program[i]
    Y = get_value(Y,registers)
    if op == 'set':
        registers[X] = Y
    elif op == 'sub':
        registers[X] -= Y
    elif op == 'mul':
        ans[0]+=1
        registers[X] *= Y
    elif op == 'jnz':
        if get_value(X,registers)!=0:
            return i+Y
    return i+1

registers = defaultdict(int)

i = 0
while 0<=i<len(program):
    i = run_line(i,registers)
    
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def optimized_program():
    h = 0
    for b in range(105700, 122701, 17):
        if not is_prime(b):
            h += 1
    return h

ans[1] = optimized_program()
print(ans)