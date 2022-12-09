"Day 7 of AOC2022"
from collections import defaultdict

with open("AoC2022_07_data.txt", "r") as file:
    data = file.read()

d = defaultdict(int)
path = ['']
space=70000000
free=30000000
ans1=0
ans2 = space

for line in data.split('\n'):
    if line[0] == '$':
        cmd = line.split(' ')
        if cmd[1]=='cd':
            if cmd[2]=='/':
                path = ['']
            elif cmd[2]=='..':
                path.pop()
            else:
                path.append(cmd[-1])
    else:
        dim, name = line.split(' ')
        if dim!='dir':
            for i in range(len(path)):
                subpath=path[:i+1]
                string = '/'.join(subpath)
                d[string]+=int(dim)

space_unused = space - d['']
to_free = free-space_unused

for folder in d.keys():
    folder_dim=d[folder]
    if folder_dim<100000:
        ans1+=folder_dim
    if folder_dim>to_free:
        ans2=min(ans2,folder_dim)
                
print(ans1)
print(ans2)