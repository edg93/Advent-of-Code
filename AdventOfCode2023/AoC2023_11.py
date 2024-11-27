with open("AoC2023_11_data.txt", "r") as file:
    data = file.read()

data = data.split('\n')
R,C = len(data),len(data[0])
r_set,c_set = set(),set()
galaxies = []

for r in range(R):
    for c in range(C):
        if data[r][c] == '#':
            r_set.add(r)
            c_set.add(c)
            galaxies.append((r,c))

empty_r = list(set(range(R))-r_set)
empty_c = list(set(range(C))-c_set)
empty_r.sort()
empty_c.sort()

def expand(l,galaxies):
    g_exp = []
    for galaxy in galaxies:
        x,y=galaxy[0],galaxy[1]
        for i,r in enumerate(empty_r):
            if x>r+i*l:
                x+=l
        for i,c in enumerate(empty_c):
            if y>c+i*l:
                y+=l
        g_exp.append((x,y))
    return g_exp

for l in [1,999999]:
    ans = 0
    g_exp = expand(l,galaxies)
    for i,g1 in enumerate(g_exp):
        for g2 in g_exp[i+1:]:
            ans += abs(g1[0]-g2[0])+abs(g1[1]-g2[1])            
    print(ans)
