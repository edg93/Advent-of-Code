with open("AoC2015_08_data.txt", "r") as file:
     data = file.read()
    
data = data.split('\n')

ans = [0,0]

for line in data:
    print(line)
    n = len(line)
    m = len(line)
    l = len(line)
    i = 0
    while i < n:
        if line[i]=='\\' :
            if line[i+1] in ['\\','\"']:
                m-=1
                i+=1
            else:
                m-=3
                i+=3
        i+=1
    m-=2

    l+=2+line.count('\"')+line.count('\\')
    ans[0]+=n-m
    ans[1]+=l-n
print(ans)