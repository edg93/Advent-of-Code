def addr(inp_1,inp_2,output,r):
    r[output]=r[inp_1]+r[inp_2]
    return r

def addi(inp_1,inp_2,output,r):
    r[output]=r[inp_1]+inp_2
    return r

def mulr(inp_1,inp_2,output,r):
    r[output]=r[inp_1]*r[inp_2]
    return r

def muli(inp_1,inp_2,output,r):
    r[output]=r[inp_1]*inp_2
    return r

def banr(inp_1,inp_2,output,r):
    r[output]=r[inp_1]&r[inp_2]
    return r

def bani(inp_1,inp_2,output,r):
    r[output]=r[inp_1]&inp_2
    return r

def borr(inp_1,inp_2,output,r):
    r[output]=r[inp_1]|r[inp_2]
    return r

def bori(inp_1,inp_2,output,r):
    r[output]=r[inp_1]|inp_2
    return r

def setr(inp_1,inp_2,output,r):
    r[output]=r[inp_1]
    return r

def seti(inp_1,inp_2,output,r):
    r[output]=inp_1
    return r

def gtir(inp_1,inp_2,output,r):
    r[output] = int(inp_1 > r[inp_2])
    return r

def gtri(inp_1,inp_2,output,r):
    r[output] = int(r[inp_1] > inp_2)
    return r

def gtrr(inp_1,inp_2,output,r):
    r[output] = int(r[inp_1] > r[inp_2])
    return r

def eqir(inp_1,inp_2,output,r):
    r[output] = int(inp_1 == r[inp_2])
    return r

def eqri(inp_1,inp_2,output,r):
    r[output] = int(r[inp_1] == inp_2)
    return r

def eqrr(inp_1,inp_2,output,r):
    r[output] = int(r[inp_1] == r[inp_2])
    return r

OPS = {"addr": addr, "addi": addi,"mulr": mulr,"muli": muli,
"banr": banr,"bani": bani,"borr": borr,"bori": bori,
"setr": setr,"seti": seti,"gtir": gtir,"gtri": gtri,
"gtrr": gtrr,"eqir": eqir,"eqri": eqri,"eqrr": eqrr,}

with open("AoC2018_19_data.txt", "r") as f:
    data = f.read()
    
data = data.splitlines()
pointer,data = data[0],data[1:]
ans = [0,0]

registers = [0,0,0,0,0,0]
pointer = int(pointer[-1])
while 0 <= registers[pointer] < len(data):
    op, a, b, c = data[registers[pointer]].split()
    registers = OPS[op](int(a), int(b), int(c), registers)
    registers[pointer] += 1
            
ans[0] = registers[0]

N = 10551264
ans[1] = sum(i for i in range(1, N+1) if N % i == 0)

print(ans)
