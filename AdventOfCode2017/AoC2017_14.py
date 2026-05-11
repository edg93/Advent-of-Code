data = 'wenycdww'

ans = [0,0]


def hash_knot(s):
    result = ''
    L = 256
    
    def wrap(rope,pos,skip,lengths):
        for n in lengths:
            for i in range(n//2):
                a = (pos+i)%L
                b = (pos+n-1-i)%L
                rope[a],rope[b] = rope[b],rope[a]
            pos = (pos+n+skip)%L
            skip += 1
        return rope,pos,skip

    lengths = [ord(c) for c in s] + [17, 31, 73, 47, 23]
    
    rope = [i for i in range(L)]
    pos,skip = 0,0
    for _ in range(64):
        rope,pos,skip = wrap(rope,pos,skip,lengths)
        
    dense_hash = []
    for block in range(16):
        h = rope[block * 16]
        for i in range(1, 16):
            h ^= rope[block * 16 + i]
        dense_hash.append(h)
    
    for x in dense_hash:
        c = hex(x)[2:]
        if len(c)==1:
            result += '0'
        result += c
    return result

def hex_to_bits(hex_string):
    bits = ""
    for c in hex_string:
        bits += bin(int(c, 16))[2:].zfill(4)
    return bits

used = set()
for i in range(128):
    line = hex_to_bits(hash_knot(data+'-'+str(i)))
    for j,ch in enumerate(line):
        if ch == '1':
            used.add((i,j))
            
ans[0] = len(used)

DIR = ((1,0),(-1,0),(0,1),(0,-1))
def find_group(x,y,used):
    group = {(x,y)}
    stack = [(x,y)]
    while stack:
        x,y = stack.pop()
        for dx,dy in DIR:
            nx,ny = x+dx,y+dy
            if (nx,ny) in used and (nx,ny) not in group:
                group.add((nx,ny))
                stack.append((nx,ny))
    return group

while used:
    x,y = used.pop()
    group = find_group(x,y,used)
    ans[1]+=1
    used -= group
    
print(ans)