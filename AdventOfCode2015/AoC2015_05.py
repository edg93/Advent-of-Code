with open("AoC2015_05_data.txt", "r") as file:
     data = file.read()
     
data = data.split('\n')
     
ans = [0,0]
vowels = ['a','e','i','o','u']
l = ['ab','cd','pq','xy']

def nice_part1(s):
    vowels_count = 0
    double_letter = False
    nice = True
    
    for i,ch in enumerate(s):
        if ch in vowels:
            vowels_count+=1
        if i>0:
            if s[i-1]==ch:
                double_letter = True
            if s[i-1]+ch in l:
                nice = False

    if vowels_count<3 or not double_letter:
        nice = False
    return nice

def nice_part2(s):
    # Check repeating letter with one in between
    criteria2 = any(s[i] == s[i+2] for i in range(len(s)-2))
    
    # Check non-overlapping pair
    seen = {}
    criteria1 = False
    for i in range(len(s)-1):
        pair = s[i:i+2]
        if pair in seen:
            if i - seen[pair] >= 2:  # non-overlapping
                criteria1 = True
                break
        else:
            seen[pair] = i
            
    return criteria1 and criteria2
        
    
    
for line in data:
    if nice_part1(line):
        ans[0]+=1
    if nice_part2(line):
        ans[1]+=1
    
    
print(ans)