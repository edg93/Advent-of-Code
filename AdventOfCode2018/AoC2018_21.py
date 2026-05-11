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
    r[output] = int(r[inp_1]    > r[inp_2])
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

with open("AoC2018_21_data.txt", "r") as file:
    data = file.read().split('\n')
    
pointer,data = data[0],data[1:]
ans = [0,0]

registers = [0,0,0,0,0,0]
pointer = int(pointer[-1])

seen = set()
last = None
"""
while 0 <= registers[pointer] < len(data):
    ip = registers[pointer]
    op, a, b, c = data[ip].split()

    # This is the halt check
    if op == "eqrr":
        print(len(seen))
        value = registers[int(a)]

        # Part 1: first value seen
        if ans[0] == 0:
            ans[0] = value

        # Part 2: detect repetition
        if value in seen:
            ans[1] = last
            break

        seen.add(value)
        last = value

    registers = OPS[op](int(a), int(b), int(c), registers)
    registers[pointer] += 1
"""

seen = set()
last = None

r3 = 0

while True:
    r4 = r3 | 65536
    r3 = 10649702

    while True:
        r3 = ((r3 + (r4 & 255)) * 65899) & 0xFFFFFF
        if r4 < 256:
            break
        r4 //= 256

    # Part 1
    if not seen:
        ans[0] = r3

    # Part 2
    if r3 in seen:
        ans[1] = last
        break

    seen.add(r3)
    last = r3

print(ans)