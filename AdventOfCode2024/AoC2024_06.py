with open("AoC2024_06_data.txt", "r") as file:
    data = file.read()
    
G = data.split('\n')
R,C = len(G),len(G[0])
D = [(-1,0),(0,1),(1,0),(0,-1)]

ans1,ans2 = 0,0

for r in range(R):
    for c in range(C):
        if G[r][c]=='^':
            s_r,s_c=r,c

p1 = False
p1_route = set()

for new_r in range(R):
    for new_c in range(C):
        if p1 and (G[new_r][new_c]=='#' or (new_r,new_c) not in p1_route):
            continue
        r,c,d = s_r,s_c,0
        visited,visited_2 = set(),set()
        while 0<=r<R and 0<=c<C:
            if (r,c,d) in visited_2:
                ans2+=1
                break
            visited_2.add((r,c,d))
            visited.add((r,c))
            dr,dc = D[d]
            rr,cc = r+dr,c+dc
            if r in {0,R-1} or c in {0,C-1}:
                if G[new_r][new_c]=='#':
                    ans1 = len(visited)
                    p1_route = {x for x in visited}
                    p1 = True
                break
            if G[rr][cc]=='#' or (rr==new_r and cc==new_c):
                d = (d+1)%4
            else:
                r,c = rr,cc

print(ans1,ans2)