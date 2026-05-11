for file in ["AoC2018_08_test.txt","AoC2018_08_data.txt"]:
    with open(file, "r") as f:
        data = f.read()        

    ans = [0,0]
    data = [int(x) for x in data.split()]
    
    
    def sum_meta(i):
        n_child = data[i]
        n_meta = data[i+1]
        s = 0
        i+=2
        for j in range(n_child):
            meta,index = sum_meta(i)
            i=index
            s+=meta
        for j in range(n_meta):
            s+=data[i]
            i+=1
        return s,i
    
    def p2(i):
        n_child = data[i]
        n_meta = data[i+1]
        s = 0
        i+=2
        child_sums = []
        if n_child == 0:
            for j in range(n_meta):
                s+=data[i]
                i+=1
        else:
            for j in range(n_child):
                child_sum,index = p2(i)
                i=index
                child_sums.append(child_sum)
            for j in range(n_meta):
                if data[i]-1 in range(len(child_sums)):
                    s+=child_sums[data[i]-1]
                i+=1
        return s,i
    
    
    ans[0]=sum_meta(0)[0]
    ans[1]=p2(0)[0]
    print(ans)
