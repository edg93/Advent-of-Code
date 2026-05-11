for file in ["AoC2018_01_test.txt","AoC2018_01_data.txt"]:
    with open(file, "r") as f:
        data = f.read()
        
    data = [int(x) for x in data.split('\n')]
    ans = [0,0]

    for n in data:
        ans[0]+=n
        
    counter = 0
    seen =set()
    frequency = 0
    while True:
        if frequency in seen:
            ans[1]=frequency
            break
        seen.add(frequency)
        frequency+=data[counter%len(data)]
        counter +=1
    print(ans)