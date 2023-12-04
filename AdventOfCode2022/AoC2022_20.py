with open("AoC2022_20_data.txt", "r") as file:
    data = file.read()
data = data.strip().split('\n')

L = len(data)


def shuffle(l):
    for i in range(L):
        for j in range(L):
            if l[j][0] == i:
                break
        val = l[j]
        new_pos = j + l[j][1]
    
        while new_pos >= L or new_pos<0:
            new_pos = int(new_pos % L+new_pos//L)
    
        l = l[:j]+l[j+1:]
        l = l[:new_pos]+[val]+l[new_pos:]
    return l

def answer(l):
    for j in range(L):
        if l[j][1] == 0:
            break
    return l[(j+1000)%L][1]+l[(j+2000)%L][1]+l[(j+3000)%L][1]

data = [int(x) for x in data]
l = list(enumerate(data))

l = shuffle(l)
print(answer(l))

data = [x*811589153 for x in data]
l = list(enumerate(data))

for _ in range(10):
    l= shuffle(l)
print(answer(l))