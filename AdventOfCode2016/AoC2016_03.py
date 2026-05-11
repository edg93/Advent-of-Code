with open("AoC2016_03_data.txt", "r") as f:
    data = f.read()
    
    
data = data.split('\n')
ans = [0,0]

t1,t2,t3 = [],[],[]

def is_triangle(sides):
    a,b,c = sides
    if a<b+c and b<a+c and c<a+b:
        return True
    return False
    
for line in data:
    a,b,c = [int(x) for x in line.split()]
    ans[0]+=is_triangle([a,b,c])
        
    t1.append(a)
    t2.append(b)
    t3.append(c)
    if len(t1)==3:
        ans[1] += is_triangle(t1)
        ans[1] += is_triangle(t2)
        ans[1] += is_triangle(t3)
        t1,t2,t3 = [],[],[]

print(ans)