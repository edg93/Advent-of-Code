for file in ["AoC2025_11_test.txt","AoC2025_11_data.txt"]:
    with open(file, "r") as f:
        data = f.read()
        
    data = data.split('\n')
    ans = [0,0]
    
    links = {}
    paths = {}
    
    for line in data:
        device,outputs = line.split(': ')
        outputs = outputs.split()
        links[device]= set(outputs)   
    
    def from_a_to_b(a,b):
        pos = a
        if pos == b:
            return 1
        if pos == 'out':
            return 0
        if (pos,b) in paths.keys():
            return paths[(pos,b)]
        total = 0
        for output in links[pos]:
            total += from_a_to_b(output,b)
            
        paths[(pos,b)]=total
        return total
                    
    ans[0] = from_a_to_b('you','out')
    ans[1] = from_a_to_b('svr','dac')*from_a_to_b('dac','fft')*from_a_to_b('fft','out')+from_a_to_b('svr','fft')*from_a_to_b('fft','dac')*from_a_to_b('dac','out')
    print(ans)