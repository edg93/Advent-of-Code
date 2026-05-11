from collections import defaultdict,deque
for file in ["AoC2017_18_test.txt","AoC2017_18_data.txt"]:
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
    
    def run_line(i,registers,inqueue,outqueue,part_1):
        op, a, *b = program[i]
        if op == 'snd':
            if part_1:
                inqueue.append(get_value(a,registers))
            else:
                outqueue.append(get_value(a,registers))
                return i+1, False, True
        elif op == 'rcv':
            if part_1:
                if get_value(a,registers) != 0:
                    return i,True,False
            else:
                if inqueue:
                    registers[a] = inqueue.popleft()
                else:
                    return i,True,False
        else:
            b = get_value(b[0],registers)
            if op == 'set':
                registers[a] = b
            elif op == 'add':
                registers[a] += b
            elif op == 'mul':
                registers[a] *= b
            elif op == 'mod':
                registers[a] %= b
            elif op == 'jgz':
                if get_value(a,registers)>0:
                    return i+b,False,False
        return i+1,False,False
    
    registers = defaultdict(int)
    i = 0
    sounds = []
    while 0<=i<len(program):
        i,done,_ = run_line(i,registers,sounds,None,True)
        if done:
            ans[0]=sounds[-1]
            break
        
    r0,r1 = defaultdict(int),defaultdict(int)
    r1['p'] = 1
    i0,i1 = 0,0
    sent_0,sent_1 = deque(),deque()
    terminated = False
    while True:
        i1,waiting_1,sent = run_line(i1,r1,sent_0,sent_1,False)
        if sent:
            ans[1] += 1
        while waiting_1:
            i0,waiting_0,_ = run_line(i0,r0,sent_1,sent_0,False)
            if sent_0:
                break
            if waiting_0:
                terminated = True
                break
        if terminated:
            break
    print(ans)