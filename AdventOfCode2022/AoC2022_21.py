with open("AoC2022_21_data.txt", "r") as file:
    data = file.read()
data=data.strip().split('\n')

monkeys = {}

for line in data:
    line = line.split()
    m = line[0][:-1]
    if len(line)>2:
        monkeys[m]=(line[1],line[2],line[3])
    else:
        monkeys[m]=int(line[1])
        
def solve(monkey):
    if type(monkeys[monkey])==int:
        return monkeys[monkey]
    else:
        m1,op,m2 = monkeys[monkey]
        if op=='+':
            return solve(m1) + solve(m2)
        elif op=='-':
            return solve(m1) - solve(m2)
        elif op=='*':
            return solve(m1) * solve(m2)
        elif op=='/':
            return int(solve(m1) / solve(m2))
        
def solve1(monkey):
    if monkey=='humn':
        return True        
    elif type(monkeys[monkey])==int:
        return False
    else:
        m1,op,m2 = monkeys[monkey]
        return solve1(m1) or solve1(m2)

def solve2(monkey,n=0):
    if monkey=='humn':
        return n
    m1,op,m2 = monkeys[monkey]
    a = solve1(m1)
    if monkey=='root':
        if a:
            n = solve(m2)
            return solve2(m1,n)
        else:
            n = solve(m1)
            return solve2(m2,n)
    else:
        if a:
            m = solve(m2)
            if op=='+':
                return solve2(m1,n-m)
            elif op=='-':
                return solve2(m1,n+m)
            elif op=='*':
                return solve2(m1,int(n/m))
            elif op=='/':
                return solve2(m1,n*m)
        else:
            m = solve(m1)
            if op=='+':
                return solve2(m2,n-m)
            elif op=='-':
                return solve2(m2,m-n)
            elif op=='*':
                return solve2(m2,int(n/m))
            elif op=='/':
                return solve2(m2,int(m/n))
        
print(solve('root'))
print(solve2('root'))