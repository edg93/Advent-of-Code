"Day 24 of AOC2021"
with open("AoC2021_24_data.txt", "r") as file:
    data = file.read()
    
data = data.split('\n')

my_variables = {'w':0,'x':0,'y':0,'z':0}
my_counter = 0
number = [ 9 for _ in range(14)]

scripts = []
s = []
for i,line in enumerate(data):
    if line.split(' ')[0] == 'inp':
        if s != []:
            scripts.append(s)
        s = []
    s.append(line)

def read_line(line,variables,counter):
    line = line.split(' ')
    rule,line = line[0],line[1:]
    if rule == 'inp':
        #variables[line[0]]=number[counter]
        counter+=1
    else:
        sign=1
        if line[1][0]=='-':
            sign,line[1] = -1,line[1][1:]
        if rule == 'add':
            if line[1].isnumeric():
                variables[line[0]]+=sign*int(line[1])
            else:
                variables[line[0]]+=variables[line[1]]
        elif rule == 'mul':
            if line[1].isnumeric():
                variables[line[0]]*=sign*int(line[1])
            else:
                variables[line[0]]*=variables[line[1]]
        elif rule == 'div':
            if line[1].isnumeric():
                if line[1]=='0':
                    return None,counter
                variables[line[0]] = variables[line[0]]//(sign*int(line[1]))
            else:
                if variables[line[1]] == 0:
                    return None,counter
                variables[line[0]]*=variables[line[0]]//variables[line[1]]
        elif rule == 'mod':
            if variables[line[0]]<0:
                return None,counter
            else:
                if line[1].isnumeric():
                    if sign*int(line[1])<=0:
                        return None,counter
                    variables[line[0]] = variables[line[0]]%(sign*int(line[1]))
                else:
                    if variables[line[1]]<=0:
                        return 'ERROR',counter
                    variables[line[0]]*=variables[line[0]]%variables[line[1]]
        elif rule == 'eql':
            if line[1].isnumeric():
                if variables[line[0]]==(sign*int(line[1])):
                    variables[line[0]]=1
                else:
                    variables[line[0]]=0
            else:
                if variables[line[0]]==variables[line[1]]:
                    variables[line[0]]=1
                else:
                    variables[line[0]]=0
    return variables,counter
    
for l in data:
    my_variables,my_counter = read_line(l,my_variables,my_counter)
    if my_variables == None:
        print('stop')
        break
    #print(my_variables)

def run(ip,script,variables):
    for line in script:
        line = line.split(' ')
        rule,line = line[0],line[1:]
        if rule == 'inp':
            variables[line[0]]=ip
        else:
            sign=1
            if line[1][0]=='-':
                sign,line[1] = -1,line[1][1:]
            if rule == 'add':
                if line[1].isnumeric():
                    variables[line[0]]+=sign*int(line[1])
                else:
                    variables[line[0]]+=variables[line[1]]
            elif rule == 'mul':
                if line[1].isnumeric():
                    variables[line[0]]*=sign*int(line[1])
                else:
                    variables[line[0]]*=variables[line[1]]
            elif rule == 'div':
                if line[1].isnumeric():
                    if line[1]=='0':
                        return None
                    variables[line[0]] = variables[line[0]]//(sign*int(line[1]))
                else:
                    if variables[line[1]] == 0:
                        return None
                    variables[line[0]]*=variables[line[0]]//variables[line[1]]
            elif rule == 'mod':
                if variables[line[0]]<0:
                    return None
                else:
                    if line[1].isnumeric():
                        if sign*int(line[1])<=0:
                            return None
                        variables[line[0]] = variables[line[0]]%(sign*int(line[1]))
                    else:
                        if variables[line[1]]<=0:
                            return 'ERROR'
                        variables[line[0]]*=variables[line[0]]%variables[line[1]]
            elif rule == 'eql':
                if line[1].isnumeric():
                    if variables[line[0]]==(sign*int(line[1])):
                        variables[line[0]]=1
                    else:
                        variables[line[0]]=0
                else:
                    if variables[line[0]]==variables[line[1]]:
                        variables[line[0]]=1
                    else:
                        variables[line[0]]=0
    return variables


sol = []
for k in range(len(scripts)):
    for n in range(1,10):
        my_variables = {'w':0,'x':0,'y':0,'z':0}

        print(run(n,scripts[k],my_variables))
        
    break