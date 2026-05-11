s = '1113222113'

ans=[0,0]

for j in range(50):
    print(j)
    new_s = []
    i = 0
    while i < len(s):
        ch = s[i]
        k = 1
        while i + k < len(s) and s[i + k] == ch:
            k += 1
        new_s.append(str(k))
        new_s.append(ch)
        i += k
    s = ''.join(new_s)
    if j == 39:
        ans[0]=len(s)
    

ans[1]=len(s)

print(ans)