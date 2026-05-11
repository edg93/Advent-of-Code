for file in ["AoC2017_04_data.txt"]:
    with open(file, "r") as f:
        data = f.read()
    data = data.splitlines()
    ans = [0,0]
    
    for line in data:
        line = line.split()
        line.sort()
        valid = len(line) == len(set(line))
        if valid:
            ans[0]+=1
            for i,word in enumerate(line):
                line[i] = [x for x in word]
                line[i].sort()
                line[i] = ''.join(line[i])
            line.sort()
            valid = len(line) == len(set(line))
            if valid:
                ans[1]+=1
            
    print(ans)