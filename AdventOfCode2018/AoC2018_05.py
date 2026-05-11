for file in ["AoC2018_05_test.txt","AoC2018_05_data.txt"]:
    with open(file, "r") as f:
        data = f.read()        

    ans = [0,len(data)]
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    def check(i,j,s):
        if 0<=i and j<len(s):
            c,c1 = s[i],s[j]
            if (c.islower() and c1.isupper()) or (c1.islower() and c.isupper()):
                if c.lower()==c1.lower():
                    return True
        return False
        
    def p1(s):
        to_remove = set()
        for i,c in enumerate(s):
            if i in to_remove:
                continue
            
            j = i+1
            while check(i,j,s):
                to_remove|={i,j}
                while i in to_remove:
                    i-=1
                j+=1
        return len(to_remove)
            
    ans[0]=len(data)-p1(data)
    
    for letter in alphabet:
        s = data
        s = s.replace(letter,'')
        s = s.replace(letter.upper(),'')
        ans[1]=min(ans[1],len(s)-p1(s))

    print(ans)