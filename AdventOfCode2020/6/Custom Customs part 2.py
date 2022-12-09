f = open("data.txt", "r")
data = f.read()
groups=data.split('\n\n')
f.close()

sum=0

for group in groups:
    counter=0
    group=group.split('\n')
    while len(group[0])>0:
        letter = group[0][0]
        ok = True
        if len(group)>1:
            for person in group[1:]:
                if letter not in person:
                    ok = False
        if ok:
            #print(letter, group)
            counter = counter+1
        group[0] = group[0].replace(letter,'')
    sum=sum+counter
    
print(sum)
print(len(groups))