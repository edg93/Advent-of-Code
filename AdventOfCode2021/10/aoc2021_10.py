"Day 10 of AOC2021"
with open("data.txt", "r") as file:
    data = file.read()
data = data.split('\n')

points = {')':3,']':57,'}':1197,'>':25137}
brackets = {'(':')','[':']','{':'}','<':'>'}
points2 = {'(':1,'[':2,'{':3,'<':4}
sol1 = 0
line_scores = []

for line in data:
    change = True
    corrupted = False
    score = 0
    while change:
        change = False
        to_delete = []
        for i in range(len(line)-1):
            if line[i] in brackets.keys():
                if brackets[line[i]]==line[i+1]:
                    change = True
                    to_delete += [i]
        for i in to_delete[::-1]:
            line = line[:i]+line[i+2:]
    for i in range(len(line)):
        if line[i] in brackets.values():
            sol1 += points[line[i]]
            corrupted = True
            break
    if not corrupted:
        for i in range(len(line)):
            score = score*5 + points2[line[-i-1]]
        line_scores += [score]
        
print(sol1)
line_scores.sort()
print(line_scores[len(line_scores)//2])

