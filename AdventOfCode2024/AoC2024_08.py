with open("AoC2024_08_data.txt", "r") as file:
    data = file.read()
    
G = data.split('\n')
R,C = len(G),len(G[0])

ans1,ans2 = 0,0

antennas = {}

antinodes = set()
antinodes_2 = set()

def show(antinodes):
    for r in range(R):
        s = ''
        for c in range(C):
            if not antinodes:
                s += G[r][c]
            else:
                if G[r][c]!='.' or (r,c) not in antinodes:
                    s += G[r][c]
                else:
                    s += '#'
        print(s)

for r in range(R):
    for c in range(C):
        if G[r][c]!='.':
            if G[r][c] in antennas.keys():
                antennas[G[r][c]].add((r,c))
            else:
                antennas[G[r][c]]={(r,c)}

for antenna in antennas.keys():
    for r1,c1 in antennas[antenna]:
        for r2,c2 in antennas[antenna]:
            if r1!=r2 and c1!=c2:
                antinodes_2.add((r1,c1))
                antinodes_2.add((r2,c2))
                dr,dc = r1-r2,c1-c2
                r3,c3 = r1+dr,c1+dc
                r4,c4 = r2-dr,c2-dc
                if 0<=r3<R and 0<=c3<C:
                    antinodes.add((r3,c3))
                if 0<=r4<R and 0<=c4<C:
                    antinodes.add((r4,c4))
                while 0<=r3<R and 0<=c3<C:
                    antinodes_2.add((r3,c3))
                    r3,c3 = r3+dr,c3+dc
                while 0<=r4<R and 0<=c4<C:
                    antinodes_2.add((r4,c4))
                    r4,c4 = r4+dr,c4+dc
                
ans1 = len(antinodes)
ans2 = len(antinodes_2)
print(ans1,ans2)