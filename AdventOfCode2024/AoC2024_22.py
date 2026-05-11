for file in ["AoC2024_22_test.txt","AoC2024_22_data.txt"]:

    with open(file, "r") as f:
        data = f.read()

    data = data.split('\n')
    ans = [0,0]
    
    def op(n):
        m = n*64
        n = (m^n)%16777216
        m = int(n/32)
        n = (m^n)%16777216
        m = n*2048
        n = (m^n)%16777216
        
        return n
        
    bananas={}
    
    for i,line in enumerate(data):
        secret_number = int(line)
        price = secret_number%10
        last_four_diff = []
        sold = set()
        
        for j in range(2000):
            secret_number=op(secret_number)
            new_price = secret_number%10

            last_four_diff.append(new_price-price)
            if len(last_four_diff)>4:
                last_four_diff = last_four_diff[1:]
            if len(last_four_diff)==4:
                s = tuple(last_four_diff)
                if s not in sold:
                    bananas[s] = bananas.get(s, 0) + new_price
                    sold.add(s)
                
            price=new_price

        ans[0]+=secret_number
    ans[1]=max(bananas.values())
    print(ans)