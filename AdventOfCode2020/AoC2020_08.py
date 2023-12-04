with open("AoC2020_08_data.txt", "r") as file:
    data = file.read()
lines=data.split('\n')

def nextLine(nLine, line, accumulator):
    instruction,n = line.split()
    if instruction=='acc':
        accumulator = accumulator + int(n)
        return nLine+1,accumulator
    elif instruction=='nop':
        return nLine+1,accumulator
    elif instruction=='jmp':
        return nLine+int(n),accumulator
    
accumulator = 0
nLine = 0
alreadyDone = set()

while nLine not in alreadyDone:
    line=lines[nLine]
    alreadyDone.add(nLine)
    nLine,accumulator=nextLine(nLine,line,accumulator)
    
print(accumulator)

for k in range(len(lines)):
    linesCopy = lines.copy()
    accumulator = 0
    nLine = 0
    alreadyDone = set()

    if lines[k][:3] == 'nop':
        linesCopy[k] = 'jmp'+lines[k][3:]
    elif lines[k][:3] == 'jmp':
        linesCopy[k] = 'nop'+lines[k][3:]

    while nLine not in alreadyDone:
            line=linesCopy[nLine]
            alreadyDone.add(nLine)
            nLine,accumulator=nextLine(nLine,line,accumulator)
            if nLine==len(lines):
                print(accumulator)
                break
