import string
from collections import Counter
with open("AoC2016_04_data.txt", "r") as f:
    data = f.read()
    
    
data = data.split('\n')
ans = [0,0]
alphabet = string.ascii_lowercase

def find_most_frequents(word):
    counts = Counter(word)
    return ''.join(letter
        for letter, _ in sorted(
            counts.items(),
            key=lambda x: (-x[1], x[0])
        )[:5])

for line in data:
    parts = line.split('-')
    enc_name = '-'.join(parts[:-1])
    ID, chk = parts[-1].split('[')
    ID = int(ID)
    chk = chk[:-1]
    name_letters = enc_name.replace('-', '')
    
    if find_most_frequents(name_letters)==chk:
        ans[0] += ID
        
        s = ''
        for ch in enc_name:
            if ch=='-':
                s+= ' '
            else:
                s+= chr(ord('a')+(ord(ch)-ord('a')+ID)%len(alphabet))
        if "northpole object storage" == s:
            ans[1]=ID

print(ans)