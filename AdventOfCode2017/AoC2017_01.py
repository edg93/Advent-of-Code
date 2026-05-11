for file in ["AoC2017_01_data.txt"]:
    with open(file, "r") as f:
        data = f.read()
    
    ans = [0,0]
    
    for i,ch in enumerate(data):
        next_ch = data[(i+1)%len(data)]
        if ch==next_ch:
            ans[0]+=int(ch)
        next_ch = data[(i+len(data)//2)%len(data)]
        if ch==next_ch:
            ans[1]+=int(ch)
    
    print(ans)