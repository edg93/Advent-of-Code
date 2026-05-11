for file in ["AoC2018_07_test.txt","AoC2018_07_data.txt"]:
    with open(file, "r") as f:
        data = f.read()        

    links = {}

    data = data.split('\n')
    ans = ['',0]
    steps = set()
    ends = set()
    requirements = {}
    for line in data:
        start,end = line.split(' must be finished before step ')
        start = start[-1]
        end = end[0]
        steps|={start,end}
        ends.add(end)
        if start in links.keys():
            links[start].add(end)
        else:
            links[start]={end}    
        if end in requirements.keys():
            requirements[end].add(start)
        else:
            requirements[end]={start}
    
    #part1
    availables = list(steps-ends)
    done = set()
    
    while availables:
        availables.sort(reverse=True)
        step = availables.pop()
        ans[0] += step
        done.add(step)
        if step not in links.keys():
            continue
        for new_step in links[step]:
            if requirements[new_step]<=done and (new_step not in done):
                availables.append(new_step) 
    
    #part2
    availables = []
    done = set()
    t=0
    in_progress = {(x,0) for x in steps-ends}
    if file == "AoC2018_07_test.txt":
        workers = 2
        factor = 60
    else:
        workers = 5
        factor = 0
    
    def update(in_progress,t):
        new_in_progress =set()
        completed = set()
        for step,time in in_progress:
            if time+1==ord(step)-4-factor:
                completed.add(step)
            else:
                new_in_progress.add((step,time+1))
        return new_in_progress,completed,t+1
    
    while done!=steps:
        availables.sort(reverse=True)
        in_progress,completed,t = update(in_progress,t)
        for step_completed in completed:
            done.add(step_completed)
            if step_completed not in links.keys():
                continue
            for new_step in links[step_completed]-done:
                if requirements[new_step]<=done:
                    availables.append(new_step)
                
        while len(availables)>0 and len(in_progress)<workers:
            step = availables.pop()
            in_progress.add((step,0))
            

    ans[1]=t
            
    print(ans)
    