for file in ["AoC2024_25_test.txt","AoC2024_25_data.txt"]:

    with open(file, "r") as f:
        data = f.read()

    data = data.split('\n\n')
    ans = 0
    
    keys = set()
    locks = set()
    
    for tool in data:
        tool = tool.split('\n')
        H = len(tool)-2

        pins = [-1 for _ in range(len(tool[0]))]

        for r in range(len(tool)):
            for c in range(len(tool[r])):
                if tool[r][c]=='#':
                    pins[c]+=1
        if '.' in  tool[0]:
            keys.add(tuple(pins))
        else:
            locks.add(tuple(pins))

    for key in keys:
        for lock in locks:
            compatible = True
            for i in range(len(key)):
                if lock[i]+key[i]>H:
                    compatible=False
                    break
            if compatible:
                ans+=1

    print(ans)