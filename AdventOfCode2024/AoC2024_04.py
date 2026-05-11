with open("AoC2024_04_data.txt", "r") as file:
    data = file.read()

data = data.split("\n")
ans1,ans2 = 0,0

ans = 0
R = len(data)
C = len(data[0])

dd = ((0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1))

for r in range(R):
    for c in range(C):
        if data[r][c]=='X':
            for rr,cc in dd:
                if 0<=r+rr*3<R and 0<=c+cc*3<C and data[r+rr][c+cc]+data[r+2*rr][c+2*cc]+data[r+3*rr][c+3*cc]=='MAS':
                    ans1+=1                
        if 0<r<R-1 and 0<c<C-1 and data[r][c]=='A':
            if data[r-1][c-1]+data[r+1][c+1] in {'MS','SM'} and data[r+1][c-1]+data[r-1][c+1] in {'MS','SM'}:
                    ans2+=1

print(ans1,ans2)