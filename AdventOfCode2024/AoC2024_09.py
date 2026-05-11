with open("AoC2024_09_data.txt", "r") as file:
    data = file.read()
    

ans1,ans2 = 0,0

#data = '2333133121414131402'

l = []

for i,c in enumerate(data):
    for _ in range(int(c)):
        if i%2 == 0:
            l += [i//2]
        else:
            l += ['.']

i,j = 0,len(l)-1

while i <= j:
    if l[i] != '.':
        ans1 += i*l[i]
        i += 1
    else:
        if l[j] != '.':
            ans1 += i*l[j]
            i += 1
        j -= 1
            


#Part 2
index = 0
ID = 0
spaces = set()
files = []
for i,c in enumerate(data):
    c=int(c)
    if i%2 == 0:
        file =[ID,index,c]
        files.append(tuple(file))
        ID+=1
        index+=c
    else:
        if c==0:
           continue
        else:
            spaces.add((index,c))
            index+=c
            
new_files = set()

def sum_up_to(n):
    return int(n*(n+1)/2)

def checksum(files):
    tot = 0
    for (ID,pos,dim) in files:
        tot += ID*(sum_up_to(pos+dim-1)-sum_up_to(pos-1))

    return tot

for i in range(len(files)-1,-1,-1):
    file_ID,file_pos,file_dim = files[i]
    moved = False
    new_pos = file_pos
    for space_pos,space_dim in spaces:
        if space_dim>=file_dim and space_pos<new_pos:
            new_pos = space_pos
            new_space_dim = space_dim-file_dim
            
    if new_pos != file_pos:
        new_files.add((file_ID,new_pos,file_dim))
        spaces.remove((new_pos,file_dim+new_space_dim))
        if new_space_dim>0:
            spaces.add((new_pos+file_dim,new_space_dim))
    else:
        new_files.add(files[i])

ans2 = checksum(new_files)

print(ans1,ans2)
