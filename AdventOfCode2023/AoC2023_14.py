with open("AoC2023_14_test.txt", "r") as file:
    data = file.read()

data = data.split('\n')
R,C = len(data),len(data[0])

ans1,ans2=0,0

rocks_r=[[] for _ in range(R)]
rocks_c=[[] for _ in range(C)]

for c in range(C):
    for r in range(R):
        if data[r][c]=='#':
            rocks_r[r].append(c)
            rocks_c[c].append(r)


def up(data):
    load = 0
    for c in range(C):
        empty_cell = R
        for r in range(R):
            if data[r][c]=='#':
                empty_cell = R-r-1
            elif data[r][c]=='O':
                load += empty_cell
                empty_cell -= 1
    return load
print(up(data))