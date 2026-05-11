for file in ["AoC2018_04_test.txt","AoC2018_04_data.txt"]:
    with open(file, "r") as f:
        data = f.read()        

    data = data.split('\n')
    ans = [0,0]
    
    data.sort()
    
    guards = {}
    
    for line in data:
        timestamp,event = line.split('] ')
        time = timestamp[1:].split()[1]
        mm = [int(x) for x in time.split(':')][1]
        
        if '#' in event:
            guard = int(event.split('#')[1].split()[0])
        if event == "falls asleep":
            t0=mm
        if event == "wakes up":
            for t in range(t0,mm):
                if guard in guards.keys():
                    guards[guard][t]+=1
                else:
                    guards[guard] = [0 for _ in range(60)]
                    guards[guard][t]=1

    
    max_guard = max(guards, key=lambda k: sum(guards[k]))
    mm = max(range(len(guards[max_guard])), key=lambda i: guards[max_guard][i])
    ans[0]=max_guard*mm
    
    max_guard = max(guards, key=lambda k: max(guards[k]))
    mm = max(range(len(guards[max_guard])), key=lambda i: guards[max_guard][i])
    ans[1]=max_guard*mm
    
    print(ans)