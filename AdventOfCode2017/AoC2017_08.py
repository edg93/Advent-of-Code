from collections import defaultdict
for file in ["AoC2017_08_test.txt","AoC2017_08_data.txt"]:
    with open(file, "r") as f:
        data = f.read()
    data = data.splitlines()
    ans = [0,-10e9]
    
    registers = defaultdict(int)
    
    def valid(condition,registers):
        reg, op, value = condition.split()
        value = int(value)
        reg_value = registers[reg]
        if op == '>':
            return reg_value > value
        elif op == '<':
            return reg_value < value
        elif op == '>=':
            return reg_value >= value
        elif op == '<=':
            return reg_value <= value
        elif op == '==':
            return reg_value == value
        elif op == '!=':
            return reg_value != value
    
    for line in data:
        rest,condition = line.split(' if ')
        register,op,n = rest.split()
        n = int(n)
        if valid(condition,registers):
            if op=='inc':
                registers[register] += n

            else:
                registers[register] -= n
                
        ans[1] = max(ans[1],max(registers.values()))
    ans[0] = max(registers.values())
    print(ans)
