for file in ["AoC2023_12_test.txt","AoC2023_12_data.txt"]:
    with open(file, "r") as f:
        data = f.read()
    
    data = data.split('\n')
    ans = [0,0]
    
    def fit_blocks(s,blocks):
        if (s,tuple(blocks)) in cash:
            return cash[(s,tuple(blocks))]
        if s.count('#')+s.count('?')<sum(blocks):
            return 0
        count = 0
        block = blocks[0]
        for i in range(len(s)):
            if s[i]!= '.':
                if '#' in s[:i]:
                    break
                if i+block > len(s) or '.' in s[i:i+block]:
                    continue
                if i+block < len(s) and s[i+block]=='#':
                    continue
                if len(blocks)>1:
                    count += fit_blocks(s[i+block+1:],blocks[1:])
                else:
                    if '#' not in s[i+block:]:
                        count +=1
        cash[(s,tuple(blocks))]=count
        return count
    
    cash = {}
    for j,line in enumerate(data):
        springs, groups = line.split()
        groups = [int(x) for x in groups.split(',')]
        ans[0] += fit_blocks(springs,groups)
        groups = groups*5
        springs = "?".join([springs] * 5)
        count = fit_blocks(springs,groups)
        ans[1]+= count
    
    print(ans)