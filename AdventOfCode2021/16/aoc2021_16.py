"Day 16 of AOC2021"

with open("data.txt", "r") as file:
    data = file.read()

l = len(data)*4
my_string = int(data,16)
my_string = bin(my_string)[2:]
my_string = '0'*(l-len(my_string))+my_string

def read(string):
    version = int(string[:3],2)
    ID = int(string[3:6],2)
    string = string[6:]
    if ID==4:
        n,string = read_lv(string)
    else:
        x,string,y= read_pack(string)
        version += y
        n=0
        if ID==0:
            n=sum(x)
        if ID==1:
            n=1
            for xx in x:
                n*=xx
        if ID==2:
            n=min(x)
        if ID==3:
            n=max(x)
        if ID==5:
            if x[0]>x[1]:
                n=1
        if ID==6:
            if x[0]<x[1]:
                n=1
        if ID==7:
            if x[0]==x[1]:
                n=1
    return n,string,version

def read_pack(string):
    version = 0
    n = []
    if string[0]=='0':
        string=string[1:]
        a,string = string[:15],string[15:]
        a = int(a,2)
        packet,string = string[:a],string[a:]
        while len(packet)>0:
            x, packet,y = read(packet)
            version += y
            n += [x]
    else:
        string=string[1:]
        a,string = string[:11],string[11:]
        a = int(a,2)
        for _ in range(a):
            x,string,y = read(string)
            version += y
            n += [x]
    return n,string,version

def read_lv(string):
    literal_value = ''
    last = False
    while not last:
        if string[0]=='0':
            last = True
        string = string[1:]
        literal_value += string[:4]
        string = string[4:]
    literal_value = int(literal_value,2)
    return literal_value,string

print(read(my_string))
