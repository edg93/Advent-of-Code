import re
with open("AoC2021_04_data.txt", "r") as file:
    data = file.read()
data=data.split('\n\n')

numbers = [int(x) for x in data[0].split(',')]
tables = [x.split('\n') for x in data[1:]]

for t in range(len(tables)):
    for r in range(len(tables[t])):
        tables[t][r]=tables[t][r].strip(' ')
        tables[t][r]=re.sub(' +', ' ', tables[t][r])
        tables[t][r]=[int(x) for x in tables[t][r].split(' ')]
    tables[t] = (tables[t],list(map(list, zip(*tables[t])))) #per ogni tabella le accoppio la trasposta

def score(table):
    s = 0
    for line in table:
        for x in line:
            s += x
    return s

#PART 1
def winner(numbers,tables):
    for n in numbers:
        for pair in tables:
            for table in pair:
                for line in table:
                    if n in line:
                        line.remove(n)
                    if len(line)==0:
                        return(score(table)*n)

print(winner(numbers,tables))   

#PART 2            
def last_winner(numbers,tables):
    for n in numbers:
        to_remove = []
        for pair in tables:
            remove = False
            for table in pair:
                for line in table:
                    if n in line:
                        line.remove(n)
                    if len(line)==0:
                        remove = True
            if remove:
                if len(tables)==1:
                    return(score(table)*n)
                else:
                    to_remove += [pair]
        for pair in to_remove:
            tables.remove(pair)
print(last_winner(numbers,tables))