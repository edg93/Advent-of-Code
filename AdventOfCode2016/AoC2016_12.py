for file in ["AoC2016_12_test.txt","AoC2016_12_data.txt"]:
    with open(file, "r") as f:
        data = f.read()
        
    data = data.splitlines()
    data = [line.split() for line in data]
    registers  = {'a':0,'b':0,'c':0,'d':0}
    ans = [0,0]
    
    def run(data,registers):
        i = 0
        while i < len(data):
            op, *args = data[i]
            #Recognize addition's loops
            if op == 'inc':
                if (i+2 < len(data) and data[i+1][0] == 'dec' and data[i+2] == ['jnz', data[i+1][1], '-2']):
                    x = data[i][1]
                    y = data[i+1][1]
                    registers[x] += registers[y]
                    registers[y] = 0
                    i += 3
                    continue
                registers[args[0]] += 1
            elif op == 'dec':
                registers[args[0]] -= 1
            elif op == 'cpy':
                x = registers[args[0]] if args[0] in registers else int(args[0])
                if args[1] in registers:
                    registers[args[1]] = x
            elif op == 'jnz':
                x = registers[args[0]] if args[0] in registers else int(args[0])
                if x != 0:
                    i += int(args[1])
                    continue
            i+=1
        return registers['a']
            
    ans[0] = run(data,registers)
    registers  = {'a':0,'b':0,'c':1,'d':0}
    ans[1] = run(data,registers)
    print(ans)