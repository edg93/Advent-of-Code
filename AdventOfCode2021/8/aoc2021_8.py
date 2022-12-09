"Day 8 of AOC2021"
with open("data.txt", "r") as file:
    data = file.read()
data = data.split('\n')

sol1=0
sol2=0

for line in data:
    line = line.split(' | ')
    line[0],line[1]=line[0].split(' '),line[1].split(' '),
    number = ''
    for word in line[1]:
        one, four = '',''
        for word1 in line[0]:
            if len(word1)==2: one = word1
            elif len(word1)==4: four = word1
        if len(word) in [2,3,4,7]: sol1 += 1
        if len(word) == 2: number += '1'
        elif len(word) == 3: number += '7'
        elif len(word) == 4: number += '4'
        elif len(word) == 7: number += '8'
        elif len(word) == 5:
            if len(set(one) & set(word))==2: number += '3'
            else:
                if len(set(four) & set(word))==3: number += '5'
                else: number += '2'
        else:
            if len(set(one) & set(word))==2:
                if len(set(four) & set(word))==3: number += '0'
                else: number += '9'
            else: number += '6'
    sol2+=int(number)

print(sol1)
print(sol2)
