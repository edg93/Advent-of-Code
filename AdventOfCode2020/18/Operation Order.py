f = open("data.txt", "r")
data = f.read()
data=data.split('\n')

def convert(line):
    convertedLINE = []
    previous=''
    for k in range(len(line)):
        letter = line[k]
        if letter == ' ':
            previous=letter
            continue
        if letter.isnumeric() and not previous.isnumeric():
            n = letter
            for digit in line[k+1:]:
                if digit.isnumeric():
                    n = n + digit
                else:
                    break
            convertedLINE.append(int(n))
        else:
            convertedLINE.append(letter)
        previous = letter
    return convertedLINE

def solve(tail):
    parentesi = False
    if '(' in tail:
        parentesi = True
    while parentesi:
        lastOpen = 0
        for k in range(len(tail)):
            letter = tail[k]
            if letter == '(':
                lastOpen = k
            elif letter == ')':
                tail = tail[:lastOpen] + [solve(tail[lastOpen+1:k])] + tail[k+1:]
                break
        if '(' not in tail:
            parentesi = False
    
    result, tail = tail[0],tail[1:]

    for k in range(len(tail)):
        letter = tail[k]
        if letter == '+':
            result = result + tail[k+1]
        elif letter == '*':   
            result = result * tail[k+1]
    return result

sum=0
for line in data:
    sum = sum + solve(convert(line))
    
print(sum)