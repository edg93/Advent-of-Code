import re

password =  'vzbxkghb'
n = 8

ans = [0,0]

def valid(password):
    valid = False
    for i in range(n-2):
        if ord(password[i+2])==ord(password[i+1])+1==ord(password[i])+2:
            valid = True
    
    pairs = re.findall(r'(.)\1', password)
    
    # We use a set to count unique pairs
    unique_pairs = set(pairs)
    
    # Check if there are at least 2 different pairs
    if len(unique_pairs) < 2:
        valid = False
    return valid

def increment(password):
    j = len(password)-1
    rest = 1
    while rest ==1:
        
        ord_j = ord(password[j])
        new_ord = ord_j+rest
        rest = 0
        if new_ord == ord('z')+1:
            new_ord = ord('a')
            rest = 1
            
        if new_ord in [ord('l'),ord('o')]:
            new_ord+=1
        elif new_ord==ord('i'):
            new_ord+=2
        
        password = password[:j] + chr(new_ord) + password[j+1:]
        j-=1
    return password

for i,ch in enumerate(password):
    if ch in ['i','l','o']:
        if ch == 'o':
            
            password = password[:i]+chr(ord('p'))+'a'*(len(password)-i-1)
        else:
            password = password[:i]+chr(ord('j'))+'a'*(len(password)-i-1)
            break
        
while not valid(password):
    password = increment(password)

ans[0]=password
password = increment(password)
while not valid(password):
    password = increment(password)
ans[1]=password
print(ans)