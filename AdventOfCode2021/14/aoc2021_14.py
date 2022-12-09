"Day 14 of AOC2021"
from copy import copy

with open("data.txt", "r") as file:
    data = file.read()
    
s,temp = data.split('\n\n')
temp = temp.split('\n')
rules = {}
letters = {}
pairs = {}

for rule in temp:
    a,b=rule.split(' -> ')
    rules[a]=b
    pairs[a]=0

for letter in s:
    if letter in letters:
        letters[letter]+=1    
    else:
        letters[letter] = 1

for i in range(len(s)-1):
    pairs[s[i:i+2]]+=1

steps = 40

for i in range(steps):
    pairs_copy = copy(pairs)
    for a,b in pairs.items():
        c = rules[a]
        if c in letters:
            letters[c]+=b
        else:
            letters[c]=b
        pairs_copy[a[0]+c] += b
        pairs_copy[c+a[1]] += b
        pairs_copy[a]=pairs_copy[a]-pairs[a]
    if i == 9:
        l = list(letters.values())
        l.sort()
        print(l[-1]-l[0])

    pairs = copy(pairs_copy)
    
l = list(letters.values())
l.sort()
print(l[-1]-l[0])