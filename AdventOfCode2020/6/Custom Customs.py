f = open("data.txt", "r")
data = f.read()
groups=data.split('\n\n')
f.close()

sum=0

for group in groups:
    group=group.replace('\n','')
    counter=0
    while len(group)>0:
        letter = group[0]
        group = group.replace(letter,'')
        counter = counter+1
    sum=sum+counter
    
print(sum)