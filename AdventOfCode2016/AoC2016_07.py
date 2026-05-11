for file in ["AoC2016_07_data.txt"]:
    with open(file, "r") as f:
        data = f.read()
    
    data = data.splitlines()
    ans = [0,0]
    
    for line in data:
        inside = False
        abba_inside = False
        abba_outside = False
        hypernets = []
        for i,a in enumerate(line):
            if a=='[':
                s = ''
                inside = True
            elif a== ']':
                inside = False
                hypernets.append(s)
                s = ''
            elif i <= len(line)-4:
                b, c, d = line[i+1:i+4]
                if a == d and b == c and a != b:
                    if not inside:
                        abba_outside = True
                    else:
                        abba_inside = True
            if inside:
                s+=a
                
        aba_bab = False
        inside = False
        for i,a in enumerate(line):
            if a=='[':
                inside = True
            elif a== ']':
                inside = False
            if not inside and i <= len(line)-3:
                b,c = line[i+1:i+3]
                if a == c:
                    bab = b+a+b
                    if any(bab in x for x in hypernets):
                        aba_bab = True
                        
        if abba_outside and not abba_inside:
            ans[0]+=1
        if aba_bab:
            ans[1]+=1
            
        
    print(ans)