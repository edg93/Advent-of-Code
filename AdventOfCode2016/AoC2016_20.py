for file in ["AoC2016_20_data.txt"]:
    with open(file, "r") as f:
        data = f.read()
        
    MAX = 4294967295
    data = data.splitlines()
    intervals = []
    ans = [0,0]
    
    for line in data:
        a,b= [int(x) for x in line.split('-')]
        intervals.append([a,b])
        
    intervals.sort()
    merged = []

    for a,b in intervals:
        if not merged or merged[-1][1]+1<a:
            merged.append([a,b])
        else:
            merged[-1][1] = max(merged[-1][1],b)
            
    ans[0] = 0 if merged[0][0] > 0 else merged[0][1]+1
    
    prev = -1
    for a,b in merged:
        ans[1] += max(0, a - (prev+1))
        prev = b
    ans[1] += MAX - prev 
        
    print(ans)