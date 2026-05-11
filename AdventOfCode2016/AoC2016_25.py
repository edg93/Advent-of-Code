
with open('AoC2016_25_data.txt', "r") as f:
    data = f.read()
data = data.splitlines()
data = [line.split() for line in data]

def value(x, regs):
    return regs[x] if x in regs else int(x)

def run(data,registers,limit=20):
    i = 0
    expected = 0
    produced = 0

    while i < len(data):
        op, *args = data[i]
        #Recognize addition's loops
        if op == 'inc':
            if (i+2 < len(data) and data[i+1][0] == 'dec' and data[i+2] == ['jnz', data[i+1][1], '-2']):
                x = data[i][1]
                y = data[i+1][1]
                n = 1
                if i+4 <len(data) and data[i+3][0] == 'dec' and data[i+3][1] != data[i+1][1] and data[i+4]== ['jnz', data[i+3][1], '-5']:
                    idx_n = data[i+3][1]
                    n = registers[idx_n]
                    registers[idx_n] = 0
                    i += 2
                registers[x] += n*registers[y]
                registers[y] = 0
                i += 3
                continue
            registers[args[0]] += 1
        
        elif op == 'dec':
            registers[args[0]] -= 1
        elif op == 'cpy':
            x = value(args[0],registers)
            if args[1] in registers:
                registers[args[1]] = x
        elif op == 'jnz':
            x = value(args[0],registers)
            if x != 0:
                n = value(args[1],registers)
                i += n
                continue
        elif op == 'out':
            v = value(args[0], registers)

            # must alternate 0,1,0,1,...
            if v != expected:
                return False

            expected ^= 1
            produced += 1

            if produced == limit:
                return True

        i+=1
    return False

for a in range(0, 10_000_000):
    regs = {'a': a, 'b': 0, 'c': 0, 'd': 0}
    output = []

    if run(data,regs):
        print(a)
        break
        
