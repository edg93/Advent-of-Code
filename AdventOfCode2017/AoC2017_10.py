data = [88,88,211,106,141,1,78,254,2,111,77,255,90,0,54,205]
data_str = "88,88,211,106,141,1,78,254,2,111,77,255,90,0,54,205"

ans = [0,'']
L = 256
rope = [i for i in range(L)]

def wrap(rope,pos,skip):
    for n in data:
        for i in range(n//2):
            a = (pos+i)%L
            b = (pos+n-1-i)%L
            rope[a],rope[b] = rope[b],rope[a]
        pos = (pos+n+skip)%L
        skip += 1
    return rope,pos,skip

rope,pos,skip = wrap(rope,0,0)

ans[0]=rope[0]*rope[1]
data = [ord(c) for c in data_str] + [17, 31, 73, 47, 23]

rope = [i for i in range(L)]
pos,skip = 0,0
for _ in range(64):
    rope,pos,skip = wrap(rope,pos,skip)
    
dense_hash = []
for block in range(16):
    h = rope[block * 16]
    for i in range(1, 16):
        h ^= rope[block * 16 + i]
    dense_hash.append(h)


for x in dense_hash:
    c = hex(x)[2:]
    if len(c)==1:
        ans[1] += '0'
    ans[1] += c
print(ans)