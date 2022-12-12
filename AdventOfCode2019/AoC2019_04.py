r0,r1 = 367479,893698
count = 0
pw1 = set()
pw2 = set()
for x in range(r0,r1):
    x = str(x)
    decreasing = True
    pair = False
    pair2 = False
    skip = False
    for i in range(len(x)-1):
        if int(x[i])>int(x[i+1]):
            decreasing = False
        if skip:
            if i!=len(x)-2 and x[i]!=x[i+1]:
                skip = False
            continue
        if x[i]==x[i+1]:
            pair = True
            if pair2:
                continue
            else:
                pair2 = True
                if i!=len(x)-2 and x[i]==x[i+2]:
                    pair2 = False
                    skip = True
    if decreasing and pair:
        pw1.add(int(x))
        if pair2:
            pw2.add(int(x))

print(len(pw1),len(pw2))