for file in ["AoC2018_02_test.txt","AoC2018_02_data.txt"]:
    with open(file, "r") as f:
        data = f.read()
        
    data = data.split('\n')
    
    ans = [0,0]
    two,three = 0,0
    
    for line in data:
        for c in line:
            if line.count(c)==2:
                two+=1
                break
        for c in line:
            if line.count(c)==3:
                three+=1
                break
            
    ans[0]=two*three
    
    for i,line in enumerate(data[:-1]):
        for line1 in data[i+1:]:
            exactly_one = False
            for j,c in enumerate(line):
                if c!=line1[j]:
                    if exactly_one:
                        exactly_one = False
                        break
                    exactly_one=True
                    different_c = j
            if exactly_one:
                ans[1] = line[:different_c]+line[different_c+1:]
    print(ans)
