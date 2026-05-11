from collections import defaultdict

with open("AoC2024_10_data.txt", "r") as file:
    data = file.read()
    
G = data.split('\n')
R,C = len(G),len(G[0])
D = ((-1,0),(1,0),(0,-1),(0,1))
ans1,ans2 = 0,0

def show(p):
    for r in range(R):
        s=''
        for c in range(C):
            if p == 1:
                if (r,c) in score.keys():
                    s+=str(len(score[(r,c)]))+'\t'
                else:
                    s+= '.\t'
            else:
                if (r,c) in paths.keys():
                    s+=str(paths[(r,c)])+'\t'
                else:
                    s+= '.\t'
        print(s)
        
score = {}
paths = {}
values = defaultdict(set)

for r in range(R):
    for c in range(C):
        values[int(G[r][c])].add((r,c))
        if G[r][c]=='9':
            score[(r,c)]={(r,c)}
            paths[(r,c)]=1
        
for i in range(8,-1,-1):
    for r,c in values[i]:
        score[(r,c)] = set()
        paths[(r,c)]=0
        for dr,dc in D:
            rr,cc = r+dr,c+dc
            if (rr,cc) in values[i+1]:
                score[(r,c)] = score[(r,c)] | score[(rr,cc)]
                paths[(r,c)] += paths[(rr,cc)]
                
for p in values[0]:
    ans1 += len(score[p])
    ans2 += paths[p]
        
print(ans1,ans2)