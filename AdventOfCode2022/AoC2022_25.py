with open("AoC2022_25_data.txt", "r") as file:
    data = file.read()
data=data.strip().split('\n')
    
ans = 0
D = {'=':-2, '-':-1,'0':0,'1':1,'2':2}
D1 = {2: '2', 1: '1', 0: '0', -1: '-', -2: '='}

def to_base_10(s):
    n=0
    for i in range(len(s)):
        n += D[s[len(s)-i-1]]*5**i
    return n
    
def max_value(p5):
    if p5==1:
        return 2,1
    x,n = max_value(p5//5)
    return p5*2 + x,n+1

def length(p5):
    return 

def to_snafu(n,p5,l):
    if -2 <= n <= 2:
        return D1[n]
    for d in [-2,-1,0,1,2]:
        x = n-p5*d
        if abs(x)<=max_value(p5//5)[0]:
            x = D1[d]
            x1 = to_snafu(n-p5*d, p5//5,l-1)
            while len(x+x1)<l:
                x+='0'
            return x+x1

for line in data:
    ans+=to_base_10(line)
print(ans)

p5 = 1
while ans>max_value(p5)[0]:
  p5 *= 5
print(to_snafu(ans,p5,max_value(p5)[1]))

