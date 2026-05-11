from collections import Counter

with open("AoC2016_06_data.txt", "r") as f:
    data = f.read()
    
data = data.split('\n')
columns = ['' for _ in range(len(data[0]))]

ans = ['','']

for line in data:
    for i,ch in enumerate(line):
        columns[i]+=ch
        
for column in columns:
    frequencies = Counter(column)
    ans[0] += max(frequencies, key=frequencies.get)
    ans[1] += min(frequencies, key=frequencies.get)
print(ans)