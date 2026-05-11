for file in ["AoC2017_02_test.txt","AoC2017_02_data.txt"]:
    with open(file, "r") as f:
        data = f.read()
    
    ans = [0,0]
    
    data = data.splitlines()
    
    for line in data:
        line = [int(x) for x in line.split()]
        ans[0] += max(line)-min(line)
        for i,a in enumerate(line):
            for b in line[i+1:]:
                if a%b == 0:
                    ans[1]+=a//b
                elif b%a==0:
                    ans[1]+=b//a
    
    print(ans)