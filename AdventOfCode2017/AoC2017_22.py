for file in ["AoC2017_22_data.txt"]:
    with open(file, "r") as f:
        data = f.read()
        
data = data.splitlines()
R,C = len(data),len(data[0])
ans = [0,0]
DIR = {0:(1,0),1:(0,-1),2:(-1,0),3:(0,1)}

infected = set()
for r in range(R):
    for c in range(C):
        if data[r][c]=='#':
            infected.add((r,c))
            
def part_1(infected,virus,d):
    count = 0
    for _ in range(10000):
        r,c = virus
        if virus in infected:
            d = (d+1)%4
            infected.remove(virus)
        else:
            d = (d-1)%4
            infected.add(virus)
            count+=1
        dr,dc = DIR[d]
        virus = r+dr,c+dc
    return count

def part_2(infected,virus,d):
    count = 0
    flagged,weakened = set(),set()
    for _ in range(10_000_000):
        r,c = virus
        if virus in infected:
            d = (d+1)%4
            infected.remove(virus)
            flagged.add(virus)
        elif virus in weakened:
            weakened.remove(virus)
            infected.add(virus)
            count+=1
        elif virus in flagged:
            d = (d+2)%4
            flagged.remove(virus)
        else:
            d = (d-1)%4
            weakened.add(virus)
            
        dr,dc = DIR[d]
        virus = r+dr,c+dc
    return count

virus = R//2,C//2  
ans[0] = part_1(set(infected),virus,2)

virus = R//2,C//2
ans[1] = part_2(set(infected),virus,2)

print(ans)