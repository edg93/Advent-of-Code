from collections import defaultdict
for file in ["AoC2024_24_test.txt","AoC2024_24_data.txt"]:

    with open(file, "r") as f:
        data = f.read()

    inputs,gates = data.split('\n\n')
    inputs = inputs.split('\n')
    gates = gates.split('\n')
    ans = [0,0]
    variables = {}
    for variable in inputs:
        variable,value = variable.split(': ')
        value = int(value)
        variables[variable] = value
    
    
    requirements = {}

    for gate in gates:
        a,op,b,_,c = gate.split()
        requirements[c] = (a,op,b)
        
    def find_value(c):
        a,op,b = requirements[c]
        if a not in variables.keys():
            a = find_value(a)
        else:
            a = variables[a]
        if b not in variables.keys():
            b = find_value(b)
        else:
            b = variables[b]
        
        if op == 'AND':
            c_value = min(a,b)
        elif op == 'OR':
            c_value = max(a,b)
        else:
            c_value = a^b
        variables[c]=c_value
        return c_value
        
    sol = []
    for c in requirements.keys():
        if c[0]=='z':
            
            sol.append((c,find_value(c)))
    sol.sort(reverse=True)
    
    s = ''
    for _,x in sol:
        s+=str(x)
        
    ans[0]=int(s,2)

    print(ans)
