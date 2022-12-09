f = open("data.txt", "r")
data = f.read()
data=data.split('\n\n')
f.close()
valid,optional = 0,0
for k in range(len(data)):
    data[k]=data[k].replace('\n',' ')
    data[k]=data[k].split(' ')
    if len(data[k])==8:
        valid = valid+1
    if len(data[k])==7:
        cid = False
        for key in data[k]:
            if key[:3]=='cid':
                cid = True
                break
        if not cid:
            optional = optional +1

print(valid,optional)
print(valid+optional)