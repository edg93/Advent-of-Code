import re

f = open("data.txt", "r")
data = f.read()
data=data.split('\n\n')
f.close()

numbers,tables=data[0],data[1:]
numbers = numbers.split(',')
numbers = [int(x) for x in numbers]

for i in range(len(tables)):
    tables[i]=tables[i].split('\n',)
    for j in range(len(tables[i])):
        tables[i][j]=tables[i][j].strip(' ')
        tables[i][j]=re.sub(' +', ' ', tables[i][j])
        tables[i][j]=tables[i][j].split(' ')
        tables[i][j]=[int(x) for x in tables[i][j]]
        
#per ogni tabella le accoppio la trasposta
for i in range(len(tables)):
    tables[i] = [tables[i],list(map(list, zip(*tables[i])))]

#PART 1
def winner(numbers,tables):
    for n in numbers:
        for pair in tables:
            for table in pair:
                for line in table:
                    if n in line:
                        line.remove(n)
                    if len(line)==0:
                        somma = 0
                        for line in table:
                            for x in line:
                                somma += x
                        return(somma*n)

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
                    somma = 0
                    for line in table:
                        for x in line:
                            somma += x
                    return(somma*n)
                else:
                    to_remove += [pair]
        for pair in to_remove:
            tables.remove(pair)
print(last_winner(numbers,tables))