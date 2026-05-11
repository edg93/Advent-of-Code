
for file in ["AoC2018_12_test.txt","AoC2018_12_data.txt"]:
    with open(file, "r") as f:
        data = f.read()
        
    ans = [0,0]
    
    initial_state,rules = data.split('\n\n')
    initial_state = initial_state.split()[-1]
    
    plants = {i for i,c in enumerate(initial_state) if c == '#'}

    rules = rules.split('\n')
    
    rules_dic = {}
    for rule in rules:
        before,after = rule.split(' => ')
        rules_dic[before]=after
        
    rules_on = {k for k,v in rules_dic.items() if v == '#'}

    def evolve(plants):
        new_gen = set()
        for i in range(min(plants)-2, max(plants)+3):
            pattern = ''.join(
                '#' if i+j in plants else '.'
                for j in (-2,-1,0,1,2)
            )
            if pattern in rules_on:
                new_gen.add(i)
        return new_gen
    
    def output(plants):
        s= ''
        for i in range(100,220):
            if i in plants:
                s+='#'
            else:
                s+='.'
        print(s)
        
    N = 50000000000
    plants_sums = [sum(plants)]
    stabilised = False
    gen = 0
    while not stabilised:
        gen+=1
        plants=evolve(plants)
        plants_sums.append(sum(plants))
        if gen==20:
            ans[0]=sum(plants)
        if len(plants_sums)>4 and plants_sums[-1] - plants_sums[-2] == plants_sums[-2] - plants_sums[-3]:
            stabilised = True
            
    
    diff = plants_sums[-1]-plants_sums[-2]
    ans[1] = sum(plants)+diff*(N-gen)
    print(ans)