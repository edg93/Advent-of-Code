with open("AoC2020_19_data.txt", "r") as file:
    data = file.read()
Rules,messages=data.split('\n\n')
messages,Rules = messages.split('\n'),Rules.split('\n')
rules = {}
solved = set()

for line in Rules:
    n,line = line.split(': ')
    if '"' in line:
        rules[int(n)]=line.replace('"','')
        solved.add(int(n))
    else:
        line = [tuple([int(x) for x in option.split()]) for option in line.split(' | ')]
        rules[int(n)]=set(line)
        
while len(solved)!=len(rules):
    for n,options in rules.items():
        if n in solved:
            continue
        to_remove,to_add = set(),set()
        for option in options:
            for i,x in enumerate(option):
                if x in solved:
                    option_copy=[x for x in option]
                    to_remove.add(tuple(option_copy))
                    if type(rules[x])==str:
                        option_copy[i]=rules[x]
                        to_add.add(tuple(option_copy))
                    else:
                        for op in rules[x]:
                            option_copy[i]=op
                            to_add.add(tuple(option_copy))
       
        for option in to_add:
            options.add(option)
        for option in to_remove:
            options.remove(option)
        ok = True
        for option in options:
            for x in option:
                if type(x)==int:
                    ok=False
                    break
        if ok:
            rules[n] = set([''.join(option) for option in options])
            solved.add(n)
ans1=0
for message in messages:
    if message in rules[0]:
        ans1+=1
        
print(ans1)