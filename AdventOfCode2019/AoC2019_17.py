from IntcodeComputer import run_intcode
with open('AoC2019_17_data.txt', "r") as f:
    data = f.read()

data = [int(x) for x in data.split(',')]
ans = [0,0]
ascii_map, _ = run_intcode(data)

G = []
line = []
for ch in ascii_map:
    if ch == '\n':
        if line:
            G.append(line)
            line = []
    else:
        line.append(ch)

R,C = len(G),len(G[0])
DIR = ((0,1),(1,0),(0,-1),(-1,0))
DIRS = {
    '^': (-1, 0),
    'v': (1, 0),
    '<': (0, -1),
    '>': (0, 1)
}
RIGHT = {'^': '>', '>': 'v', 'v': '<', '<': '^'}
LEFT  = {'^': '<', '<': 'v', 'v': '>', '>': '^'}
        
for r in range(1,R-1):
    for c in range(1,C-1):
        if G[r][c]=='#' and all(G[r+dr][c+dc] == '#' for dr, dc in DIR):
            ans[0] += r*c

for r, row in enumerate(G):
    for c, ch in enumerate(row):
        if ch in "^v<>":
            robot_pos = (r, c)
            robot_dir = ch
            
path = []
r, c = robot_pos

while True:
    dr, dc = DIRS[robot_dir]
    # Count steps forward
    steps = 0
    while 0 <= r+dr < R and 0 <= c+dc < C and G[r+dr][c+dc] == '#':
        r += dr
        c += dc
        steps += 1
    if steps > 0:
        path.append(str(steps))
    # Try turning left or right
    turned = False
    for turn, new_dir in [('L', LEFT[robot_dir]), ('R', RIGHT[robot_dir])]:
        dr, dc = DIRS[new_dir]
        if 0 <= r+dr < R and 0 <= c+dc < C and G[r+dr][c+dc] == '#':
            path.append(turn)
            robot_dir = new_dir
            turned = True
            break
    if not turned:
        break
            
# A B A B A C B C A C
# A = R4L10L10
# B = L8R12R10R4
# C = L8L8R10R4

main_routine = "A,B,A,B,A,C,B,C,A,C\n"
funcA = "R,4,L,10,L,10\n"
funcB = "L,8,R,12,R,10,R,4\n"
funcC = "L,8,L,8,R,10,R,4\n"
video = "n\n"  # 'y' for live video, 'n' for no

inputs = main_routine + funcA + funcB + funcC + video

data[0] = 2

ascii_output, dust = run_intcode(data, inputs)#print(output)
ans[1] = dust

print(ascii_output)
print(ans)