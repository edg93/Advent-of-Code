from math import gcd

def lcm(L):
    lcm = 1
    for i in L:
        lcm = lcm*i//gcd(lcm, i)
    return(lcm)

with open("AoC2023_08_data.txt", "r") as file:
    data = file.read()
    
instructions,rest = data.split('\n\n')
starts,ends = set(),set()
d = {}

for line in rest.split('\n'):
    _from,_to = line.split(' = ')
    _to = _to.strip('()').split(', ')
    d[_from] = _to
    if _from[-1] == 'A':
        starts.add(_from)
    elif _from[-1]=='Z':
        ends.add(_from)
    
def run(start,end):
    counter = 0
    while start not in end:
        if instructions[counter%len(instructions)]=='L':
            start = d[start][0]
        else:
            start = d[start][1]
        counter+=1
    return counter
    
ans1 = run('AAA',['ZZZ'])
p2 = []

for start in starts:
    p2.append(run(start,ends))
    
ans2 = lcm(p2)
print(ans1,ans2)