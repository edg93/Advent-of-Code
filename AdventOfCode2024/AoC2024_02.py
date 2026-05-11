with open("AoC2024_02_data.txt", "r") as file:
    data = file.read()
    
data = data.split('\n')
ans1,ans2 = 0,0

def check(l,part1):
    if l[0]>l[1]:
        ascending = False
    elif l[0]<l[1]:
        ascending = True
    else:
        if part1:
            return False
        else:
            return check(l[1:],True)
    for i in range(len(l)-1):
        if (ascending and not l[i]<l[i+1]<l[i]+4) or (not ascending and not l[i]>l[i+1]>l[i]-4):
            if part1:
                return False
            else:
                if i==len(l)-2:
                    return True
                else:
                    return check(l[:i]+l[i+1:],True) or check(l[:i+1]+l[i+2:],True) or check(l[:i-1]+l[i:],True)
    return True

for line in data:
    l = [int(x) for x in line.split()]
    if check(l,True):
        ans1+=1
    if check(l,False):
        ans2+=1

print(ans1,ans2)