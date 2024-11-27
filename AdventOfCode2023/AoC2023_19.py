with open("AoC2023_19_data.txt", "r") as file:
    data = file.read()

workflows,parts = data.split('\n\n')
ans1,ans2=0,0
workflows = workflows.split()
parts = parts.split()

wf_dict = {}

for wf in workflows:
    key,value=wf.split('{')
    value = value[:-1].split(',')
    wf_dict[key]=value
        
def rate(x,m,a,s):
    wf = wf_dict['in']
    while wf:
        for rule in wf:
            if ':' in rule:
                p1,p2 = rule.split(':')
                if 'x' in p1:
                    f = lambda x: eval(p1)
                    if f(x):
                        if p2=='A':
                            return True
                        elif p2== 'R':
                            return False
                        else:
                            wf = wf_dict[p2]
                            break
                elif 'm' in p1:
                    f = lambda m: eval(p1)
                    if f(m):
                        if p2=='A':
                            return True
                        elif p2== 'R':
                            return False
                        else:
                            wf = wf_dict[p2]
                            break
                elif 'a' in p1:
                    f = lambda a: eval(p1)
                    if f(a):
                        if p2=='A':
                            return True
                        elif p2== 'R':
                            return False
                        else:
                            wf = wf_dict[p2]
                            break
                elif 's' in p1:
                    f = lambda s: eval(p1)
                    if f(s):
                        if p2=='A':
                            return True
                        elif p2== 'R':
                            return False
                        else:
                            wf = wf_dict[p2]
                            break
            elif rule=='A':
                return True
            elif rule=='R':
                return False
            else:
                wf = wf_dict[rule]
                break
    
for part in parts:
    x,m,a,s = part[1:-1].split(',')
    x = int(x[2:])
    m = int(m[2:])
    a = int(a[2:])
    s = int(s[2:])
    if rate(x,m,a,s):
        ans1 += x+m+a+s
        
print(ans1)