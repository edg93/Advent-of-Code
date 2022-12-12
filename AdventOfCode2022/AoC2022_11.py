with open("AoC2022_11_data.txt", "r") as file:
    data = file.read()
data=data.strip().split('\n\n')

class monkey():
    def __init__(self,operation,test,if_true_,if_false):
        self.op = operation
        self.test = test
        self.if_true = if_true
        self.if_false = if_false
        self.inspections = [0,0]
        
    def inspect(self,obj,p):
        self.inspections[p-1] += 1
        obj = self.op(obj)
        if p == 1:
            obj = obj//3
        elif p == 2:
            obj = obj%mcm
        if obj % self.test==0:
            return obj,self.if_true
        else:
            return obj,self.if_false

monkeys = {}
iterations = {1:20,2:10000}
mcm = 1

for m in data:
    lines = m.split('\n')
    n = int(lines[0].split()[-1][:-1])
    items1 = [int(x.strip(',')) for x in lines[1].split()[2:]]
    items2 = [int(x.strip(',')) for x in lines[1].split()[2:]]
    op  = ''.join(lines[2].split()[-3:])
    op = lambda old,op=op:eval(op)
    test = int(lines[3].split()[-1])
    if_true = int(lines[4].split()[-1])
    if_false = int(lines[5].split()[-1])
    monkeys[n]= [monkey(op,test,if_true,if_false),items1,items2]
    mcm *= test

for p in [1,2]:
    ans=[]
    for _ in range(iterations[p]):
        for n in monkeys.keys():
            m=monkeys[n]
            for obj in m[p]:
                throw_to = m[0].inspect(obj,p)
                monkeys[throw_to[1]][p].append(throw_to[0])
            monkeys[n][p] = []

    for n in monkeys.keys():
        ans.append(monkeys[n][0].inspections[p-1])
    ans.sort()
    print(ans[-1]*ans[-2])