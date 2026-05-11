from hashlib import md5

ans = [0,0]
data = 'ahsbgdzn'



hash_part2 = {}

def find_hash_2(s):
    original_s = s
    if s in hash_part2:
        return hash_part2[s]
    for _ in range(2017):
        s = md5(s.encode()).hexdigest()
        hash_part2[original_s]=s
    return s

hash_part1 = {}
def find_hash_1(s):
    if s in hash_part1:
        return hash_part1[s]
    new_s = md5(s.encode()).hexdigest()
    hash_part1[s]=new_s
    return new_s

def solve(part2=False):
    passwords = 0
    i = -1

    while passwords<64:
        print(passwords)
        i+=1
        if part2:
            h = find_hash_2(data+str(i))
        else:
            h = find_hash_1(data+str(i))
        for j,ch in enumerate(h):
            if j<len(h)-2 and h[j+1]==h[j+2]==ch:
                for k in range(1000):
                    if part2:
                        h_1 = find_hash_2(data+str(i+1+k))
                    else:
                        h_1 = find_hash_1(data+str(i+1+k))
                    if ch*5 in h_1:
                        passwords += 1
                        break
                break
    return i
    
ans[0]=solve()
ans[1]=solve(True)

print(ans)