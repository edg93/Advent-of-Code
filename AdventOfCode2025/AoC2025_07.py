for file in ["AoC2025_07_test.txt","AoC2025_07_data.txt"]:
    with open(file, "r") as file:
        data = file.read()
    
    data = data.split('\n')
    ans = [0,0]
    current_line = [0 for _ in range(len(data[0]))]
    
    for line in data:
        for c,s in enumerate(line):
            if s=='S':
                current_line[c]=1
            elif s=='^' and current_line[c]!=0:
                current_line[c-1]+=current_line[c]
                current_line[c+1]+=current_line[c]
                current_line[c]=0
                ans[0]+=1
    
    ans[1]=sum(current_line)
    print(ans)Z