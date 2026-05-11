
for file in ["AoC2025_06_test.txt","AoC2025_06_data.txt"]:
    with open(file, "r") as file:
        data = file.read()
        
    ans = [0,0]
    
    data = data.split('\n')
    ready = True
    
    for i in range(len(data[0])):
        ok = False
        for j in range(len(data)):
            if data[j][i] != ' ':
                ok = True
                break
        if not ok:
            ready = True
        else:
            if ready:
                op = data[-1][i:].strip(' ').split(' ')[0]
                factors = []
                for j in range(len(data)-1):
                    factor = ''
                    number_started = False
                    k = 0
                    while True :
                        if i+k==len(data[0]):
                            break
                        if  number_started and data[j][i+k]==' ':
                            break
                        factor +=data[j][i+k]
                        if factor[-1].isnumeric():
                            number_started = True
                        k+=1
                    factors.append(factor)
                new_factors = []
                for i in range(max([len(x) for x in factors])):
                    new_factor = ''
                    for k in range(len(factors)):
                        if i<len(factors[k]):
                            new_factor+=factors[k][i]
                        else:
                            new_factor += ' '
                    new_factors.append(new_factor)
                if op == '+':
                    result1 = 0
                    result2 = 0
                    for factor in factors:
                        result1 += int(factor)
                    for factor in new_factors:
                        if factor.strip() !='':
                            result2 += int(factor)
                    ans[1] += result2
                    ans[0] += result1
                else:
                    result1 = 1
                    result2 = 1
                    for factor in factors:
                        result1 *= int(factor)
                    for factor in new_factors:
                        if factor.strip() != '':
                            result2 *= int(factor)
                    ans[0] += result1
                    ans[1] += result2
                ready = False
        
    print(ans)