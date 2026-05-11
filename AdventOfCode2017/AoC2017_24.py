from collections import deque
for file in ["AoC2017_24_test.txt","AoC2017_24_data.txt"]:
    with open(file, "r") as f:
        data = f.read()
        
    data = data.splitlines()
    ans = [0,0]
    
    components = set()
    for line in data:
        a,b = line.split('/')
        components.add((int(a),int(b)))
    
    Q = deque()
    Q.append(((0,), components))
   
    longest = 0
    while Q:
        l,remaining=Q.pop()
        extended = False
        for a,b in remaining:
            if a==l[-1]:
                Q.append((l+(a,b),remaining-{(a,b)}))
                extended=True
            elif b==l[-1]:
                Q.append((l+(b,a),remaining-{(a,b)}))
                extended=True
        if not extended:
            ans[0]=max(ans[0],sum(l))
            bridge_len = (len(l)-1)//2
            if bridge_len==longest:
                ans[1]=max(ans[1],sum(l))
            elif bridge_len>longest:
                ans[1]=sum(l)
                longest=bridge_len
        
    print(ans)