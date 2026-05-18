with open("AoC2015_01_data.txt", "r") as file:
     line = file.read()
 
ans = [0,0]

for i,ch in enumerate(line):
    if ch=='(':
        ans[0]+=1
    else:
        ans[0]-=1
    if ans[0]==-1 and ans[1]==0:
        ans[1]=i+1

print(ans)