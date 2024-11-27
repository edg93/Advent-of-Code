with open("AoC2023_13_data.txt", "r") as file:
    data = file.read()

data = data.split('\n\n')

def find_mirror(data,errors):
    ans=0
    for pattern in data:
        pattern = pattern.split('\n')
        match = False
        for r in range(len(pattern)-1):
            n = min(r+1,len(pattern)-r-1)
            smudges = 0
            for c in range(len(pattern[0])):
                for i in range(n):
                    if pattern[r-i][c]!=pattern[r+i+1][c]:
                        smudges += 1
                if smudges>errors:
                    break
            if smudges==errors:
                ans += (r+1)*100
                match = True
                break
        if not match:
            for c in range(len(pattern[0])-1):
                n = min(c+1,len(pattern[0])-c-1)
                smudges = 0
                for line in pattern:
                    for i in range(n):
                        if line[c-i]!=line[c+i+1]:
                            smudges += 1
                    if smudges>errors:
                        break
                if smudges == errors:
                    ans += c+1
                    break
    return ans

print(find_mirror(data,0))
print(find_mirror(data,1))