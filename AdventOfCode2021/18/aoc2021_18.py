"Day 18 of AOC2021"

with open("data.txt", "r") as file:
    data = file.read()

data = data.split('\n')

def addizione(x,y):
    z = '['+x+','+y+']'
    check1 = True
    while check1:
        check = True
        while check:
            z, check = explode(z)
        z, check1 = split(z)
    return z

def explode(z):
    check = False
    aperte = 0
    last_digit = -1
    for i in range(len(z)):
        if z[i]=='[':
            aperte +=1
        elif z[i] == ']':
            aperte -=1
            
        if aperte > 4:
            close = 0
            for j in range(len(z)-i):
                
                if z[i+j]==']':
                    close = i+j
                    now = True
                    break
                elif z[i+j]=='[':
                    now = False
                    break
            if now:
                check = True
                sx,dx = [int(n) for n in z[i:i+j].split(',')]
                for j in range(len(z)-close):
                    if z[close+j].isdigit():
                        s = ''
                        while z[close+j].isdigit():
                            s += z[close+j]
                            j+=1
                        m = len(s)
                        s = int(s)
                        z = z[:close+j-m]+str(s+dx)+z[close+j:]
                        break
                
                z= z[:i-1]+ '0' + z[close+1:]
                if last_digit>=0:
                    s = ''
                    while z[last_digit].isdigit():
                        s = z[last_digit]+s
                        last_digit-=1
                    n = int(s)+sx
                    z = z[:last_digit+1]+str(n)+z[last_digit+1+len(s):]
                break
        if z[i].isdigit():
            last_digit = i
    return z,check


def split(z):
    #print(z)
    check = False
    for i in range(len(z)):
        if z[i].isdigit() and not z[i-1].isdigit() and z[i+1].isdigit():
            new_z = z[:i]
            s = ''
            while z[i].isdigit():
                s+=z[i]
                i +=1
            s = int(s)
            if s%2==0:
                new_z += '[' + str(s//2) +',' + str(s//2) + ']'
            else:
                new_z += '[' + str(s//2) +',' + str(s//2+1) + ']'
            new_z+=z[i:]
            z = new_z
            check = True
            break
    return z,check

def magnitude(z):
    while z[0]=='[':
        sx = ('',-1)
        for i in range(len(z)):
            if z[i]=='[':
                sx = ('[',i)
            elif z[i]==']':
                dx=i
                break
        s = int(z[sx[1]+1:dx].split(',')[0])*3+2*int(z[sx[1]+1:dx].split(',')[1])
        z = z[:sx[1]] + str(s) + z[dx+1:]
    return int(z)

somma,tail = data[0],data[1:]
for line in tail:
    somma = addizione(somma,line)

print(magnitude(somma))

sol2 = 0
for i in range(len(data)):
    a = data[i]
    for j in range(i+1,len(data)):
        b = data[j]
        m = max(magnitude(addizione(a,b)),magnitude(addizione(b,a)))
        if m>sol2:
            sol2=m
            
print(sol2)
