import hashlib

secret_key = 'bgvyzdsv'
ans = [0,0]

number = 1

while True:
    s = f"{secret_key}{number}"
    
    # Compute MD5 hash
    h = hashlib.md5(s.encode()).hexdigest()
    
    if h.startswith("00000") and ans[0]==0:
        ans[0]=number
    if h.startswith("000000"):
        ans[1]=number
        break
    
    number += 1


print(ans)