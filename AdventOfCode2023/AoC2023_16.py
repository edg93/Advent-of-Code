with open("AoC2023_16_data.txt", "r") as file:
    data = file.read()

data = data.split('\n')
ans1,ans2=0,0
R,C = len(data),len(data[0])

def compute_energised(start):
    Q = [start]
    already_done = set()
    energised = set()
    while Q:
        r,c,_dir = Q.pop()
        if 0<=r<R and 0<=c<C and (r,c,_dir) not in already_done:
            already_done.add((r,c,_dir))
            energised.add((r,c))
            if _dir == '^':
                if data[r][c]=='|':
                    Q.append((r-1,c,_dir)) 
                elif data[r][c] == '-':
                    Q.append((r,c-1,'<'))
                    Q.append((r,c+1,'>'))
                elif data[r][c] == '\\':
                    Q.append((r,c-1,'<')) 
                elif data[r][c] == '/':
                    Q.append((r,c+1,'>')) 
                else:
                    Q.append((r-1,c,_dir))
            elif _dir == '>':
                if data[r][c]=='|':
                    Q.append((r-1,c,'^'))
                    Q.append((r+1,c,'v')) 
                elif data[r][c] == '-':
                    Q.append((r,c+1,_dir))
                elif data[r][c] == '\\':
                    Q.append((r+1,c,'v')) 
                elif data[r][c] == '/':
                    Q.append((r-1,c,'^')) 
                else:
                    Q.append((r,c+1,_dir))
            elif _dir == '<':
                if data[r][c]=='|':
                    Q.append((r-1,c,'^'))
                    Q.append((r+1,c,'v')) 
                elif data[r][c] == '-':
                    Q.append((r,c-1,_dir))
                elif data[r][c] == '\\':
                    Q.append((r-1,c,'^')) 
                elif data[r][c] == '/':
                    Q.append((r+1,c,'v')) 
                else:
                    Q.append((r,c-1,_dir))
            elif _dir == 'v':
                if data[r][c]=='|':
                    Q.append((r+1,c,_dir)) 
                elif data[r][c] == '-':
                    Q.append((r,c-1,'<'))
                    Q.append((r,c+1,'>'))
                elif data[r][c] == '\\':
                    Q.append((r,c+1,'>')) 
                elif data[r][c] == '/':
                    Q.append((r,c-1,'<')) 
                else:
                    Q.append((r+1,c,_dir))
    return len(energised)

ans1 = compute_energised((0,0,'>'))
print(ans1)

starts = []
for r in range(R):
    starts.append((r,0,'>'))
    starts.append((r,C-1,'<'))
for c in range(C):
    starts.append((0,c,'v'))
    starts.append((R-1,c,'^'))

for start in starts:
    ans2 = max(ans2,compute_energised(start))
    
print(ans2)