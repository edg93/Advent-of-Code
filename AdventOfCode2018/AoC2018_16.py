def addr(inp_1,inp_2,output,r):
    r = r.copy()
    r[output]=r[inp_1]+r[inp_2]
    return r

def addi(inp_1,inp_2,output,r):
    r = r.copy()
    r[output]=r[inp_1]+inp_2
    return r

def mulr(inp_1,inp_2,output,r):
    r = r.copy()
    r[output]=r[inp_1]*r[inp_2]
    return r

def muli(inp_1,inp_2,output,r):
    r = r.copy()
    r[output]=r[inp_1]*inp_2
    return r

def banr(inp_1,inp_2,output,r):
    r = r.copy()
    r[output]=r[inp_1]&r[inp_2]
    return r

def bani(inp_1,inp_2,output,r):
    r = r.copy()
    r[output]=r[inp_1]&inp_2
    return r

def borr(inp_1,inp_2,output,r):
    r = r.copy()
    r[output]=r[inp_1]|r[inp_2]
    return r

def bori(inp_1,inp_2,output,r):
    r = r.copy()
    r[output]=r[inp_1]|inp_2
    return r

def setr(inp_1,inp_2,output,r):
    r = r.copy()
    r[output]=r[inp_1]
    return r

def seti(inp_1,inp_2,output,r):
    r = r.copy()
    r[output]=inp_1
    return r

def gtir(inp_1,inp_2,output,r):
    r = r.copy()
    r[output] = int(inp_1 > r[inp_2])
    return r

def gtri(inp_1,inp_2,output,r):
    r = r.copy()
    r[output] = int(r[inp_1] > inp_2)
    return r

def gtrr(inp_1,inp_2,output,r):
    r = r.copy()
    r[output] = int(r[inp_1] > r[inp_2])
    return r

def eqir(inp_1,inp_2,output,r):
    r = r.copy()
    r[output] = int(inp_1 == r[inp_2])
    return r

def eqri(inp_1,inp_2,output,r):
    r = r.copy()
    r[output] = int(r[inp_1] == inp_2)
    return r

def eqrr(inp_1,inp_2,output,r):
    r = r.copy()
    r[output] = int(r[inp_1] == r[inp_2])
    return r

OPS = {"addr": addr, "addi": addi,"mulr": mulr,"muli": muli,
"banr": banr,"bani": bani,"borr": borr,"bori": bori,
"setr": setr,"seti": seti,"gtir": gtir,"gtri": gtri,
"gtrr": gtrr,"eqir": eqir,"eqri": eqri,"eqrr": eqrr,}

for file in ["AoC2018_16_data.txt"]:
    with open(file, "r") as f:
        data = f.read()
        
    ans = [0,0]
    
    part_1,part_2 = data.split('\n\n\n\n')
    part_1 = part_1.split('\n\n')
    part_2 = part_2.split('\n')
    
    opcodes = {i: set(OPS.values()) for i in range(16)}
    
    for case in part_1:
        before,instruction,after = case.split('\n')
        before = before.split(': [')[1][:-1]
        after = after.split(':  [')[1][:-1]
        instruction = [int(x) for x in instruction.split()]
        after = [int(x) for x in after.split(', ')]
        before = [int(x) for x in before.split(', ')]
        
        n,inp_1,inp_2,output = instruction
        matching = {op for op in OPS.values() if op(inp_1, inp_2, output, before) == after}
        opcodes[n] &= matching
        
        if len(matching)>=3:
            ans[0]+=1
            
    resolved = {}

    while len(resolved) < 16:
        for code, opset in opcodes.items():
            if code in resolved:
                continue
            if len(opset) == 1:
                op = next(iter(opset))
                resolved[code] = op
    
                for other in opcodes:
                    if other != code:
                        opcodes[other].discard(op)
    
    registers = [0,0,0,0]
    
    for line in part_2:
        n,inp_1,inp_2,output = [int(x) for x in line.split()]
        registers = resolved[n](inp_1,inp_2,output,registers)
        
    ans[1] = registers[0]
    print(ans)