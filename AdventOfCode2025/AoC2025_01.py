from collections import defaultdict, deque
from time import sleep

with open("AoC2025_01_data.txt", "r") as file:
    data = file.read()
    
pos = 50
ans1,ans2=0,0

for line in data.split('\n'):
    dir,n = line[0],int(line[1:])
    ans2+=n//100
    n%=100
    if  dir == 'L':
        if pos-n<=0 and pos!=0:
            ans2+=1
        pos = (pos-n)%100
    else:
        if pos+n>=100 and pos!=0:
            ans2+=1
        pos = (pos+n)%100
    if pos==0:
        ans1+=1

        
print(ans1,ans2)
        