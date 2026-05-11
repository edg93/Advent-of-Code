from copy import deepcopy
for file in ["AoC2016_23_test.txt","AoC2016_23_data.txt"]:

    with open(file, "r") as f:
        data = f.read()
    data = data.splitlines()
    data = [line.split() for line in data]
    ans = [0,0]
    
    def value(x, regs):
        return regs[x] if x in regs else int(x)
    
    def run(data,registers):
        i = 0
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
            elif op == 'tgl':
                x = value(args[0],registers)
                if not 0<=i+x<len(data):
                    i+=1
                    continue
                op_1,*args_1 = data[i+x]
                if len(args_1)==1:
                    if op_1 == 'inc':
                        data[i+x][0] = 'dec'
                    else:
                        data[i+x][0] = 'inc'
                else:
                    if op_1 == 'jnz':
                        data[i+x][0] = 'cpy'
                    else:
                        data[i+x][0] = 'jnz'
            i+=1
        return registers['a']
    
    registers = {'a':7,'b':0,'c':0,'d':0}
    ans[0] = run(deepcopy(data),registers)
    registers = {'a':12,'b':0,'c':0,'d':0}
    ans[1] = run(deepcopy(data),registers)
    
    print(ans)