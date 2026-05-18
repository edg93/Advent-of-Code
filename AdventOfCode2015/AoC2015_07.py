with open("AoC2015_07_data.txt", "r") as file:
     data = file.read()
    
def value(x):
    return int(x) if x.isdigit() else values.get(x)

def parse(data):
    data = data.split('\n')
    instructions = []
    for line in data:
        parts = line.split()
        if len(parts) == 3:        # 123 -> x
            instructions.append(('ASSIGN', parts[0], None, parts[2]))
    
        elif parts[0] == 'NOT':      # NOT x -> y
            instructions.append(('NOT', parts[1], None, parts[3]))
        else:
            instructions.append((parts[1], parts[0], parts[2], parts[4]))
    return instructions

def run_instructions(instructions,values,part2=False):
    while 'a' not in values:
        for op, a, b, out in instructions:
            if part2 and out=='b':
                continue
            va = value(a)
            vb = value(b) if b else None
    
            if op == 'ASSIGN' and va is not None:
                values[out] = va & 0xFFFF
    
            elif op == 'NOT' and va is not None:
                values[out] = (~va) & 0xFFFF
    
            elif op == 'AND' and va is not None and vb is not None:
                values[out] = (va & vb) & 0xFFFF
    
            elif op == 'OR' and va is not None and vb is not None:
                values[out] = (va | vb) & 0xFFFF
    
            elif op == 'LSHIFT' and va is not None:
                values[out] = (va << int(b)) & 0xFFFF
    
            elif op == 'RSHIFT' and va is not None:
                values[out] = (va >> int(b)) & 0xFFFF
                
    return values['a']

ans =[0,0]
values = {}
instructions = parse(data)
ans[0] = run_instructions(instructions,values)
values = {}
values['b']=ans[0]
ans[1] = run_instructions(instructions,values,True)
print(ans)