with open("AoC2015_23_data.txt", "r") as file:
    data = file.read()
    
data = data.split('\n')

ans = [0,0]

variables = {'a':0,'b':0}

def run_program(variables):
    i = 0
    while i<len(data):
        line=data[i]
        instruction = line[:3]
        if instruction == 'jio':
            _,variable,diff = line.split()
            variable = variable[0]
            diff = int(diff)
            if variables[variable] ==1:
                i += diff
                continue
        elif instruction == 'jie':
            _,variable,diff = line.split()
            variable = variable[0]
            diff = int(diff)
            if variables[variable]%2 ==0:
                i += diff
                continue
        else:
            variable = line.split()[1]
            if instruction == 'hlf':
                variables[variable]/=2
    
            elif instruction == 'tpl':
                variables[variable] *=3
            elif instruction == 'inc':
                variables[variable] +=1
            else:
                i+=int(variable)
                continue
        i+=1
    
    return variables['b']
    
ans[0]=run_program(variables)
variables = {'a':1,'b':0}
ans[1]=run_program(variables)
print(ans)