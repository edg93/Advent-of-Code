for file in ["AoC2024_17_data.txt"]:
    with open(file, "r") as f:
        data = f.read()        
        
    part,program = data.split('\n\n')
    program = program.split(': ')[1]
    program = [int(x) for x in program.split(',')]
    part = part.split('\n')
    registers = {}
    for register in part:
        key,value = register.split(': ')
        key = key[-1]
        value = int(value)
        registers[key]=value
    ans = [None,None]
        
    def combo(registers,n):
        if n in [0,1,2,3]: return n
        if n==4: return registers['A']
        if n==5: return registers['B']
        if n==6: return registers['C']
        if n==7: print('ERROR')
    
    def run_instruction(opcode,operand,registers,s):
        jump=False
        cmb = combo(registers,operand)
        if opcode==0:
            registers['A'] //= 2 ** cmb
        elif opcode==1:
            registers['B']=registers['B']^operand
        elif opcode==2:
            registers['B'] = cmb%8
        elif opcode==3:
            if registers['A']!=0:
                jump = True
        elif opcode==4:
            registers['B'] = registers['B']^registers['C']
        elif opcode==5:
            s+= str(cmb%8)+','
        elif opcode==6:
            registers['B']=registers['A']//2**cmb
        elif opcode==7:
            registers['C']=registers['A']//2**cmb
        
        return jump,registers,s
    
    def run_program(program,registers):
        s = ''
        pointer = 0
        while pointer<len(program):
            opcode = program[pointer]
            operand =program[pointer+1]
            jump,registers,s = run_instruction(opcode,operand,registers,s)
            if not jump:
                pointer+=2
            else:
                pointer = operand
        if len(s)>0 and s[-1]==',':
            s = s[:-1]
        return s

    ans[0]=run_program(program,registers.copy())
    
    def first_output(program, A):
        registers = {'A': A, 'B': 0, 'C': 0}
        s = run_program(program,registers)
        return int(s.split(',')[0])
    
    candidates = [0]

    for i in range(1, len(program) + 1):
        target = program[-i]
        new_candidates = []
    
        for base in candidates:
            for d in range(8):
                A = base * 8 + d
                if first_output(program, A) == target:
                    new_candidates.append(A)
    
        candidates = new_candidates

    ans[1] = min(candidates)
    print(ans)