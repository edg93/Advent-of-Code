from copy import copy

f = open("data.txt", "r")
data = f.read()
lines=data.split('\n')

def nextLine(nLine, line,accumulator):
    if line[:3]=='acc':
        accumulator = accumulator + int(line[4:])
        return nLine+1,accumulator
    elif line[:3]=='nop':
        return nLine+1,accumulator
    elif line[:3]=='jmp':
        return nLine+int(line[4:]),accumulator

for k in range(len(lines)):
    linesCopy = copy(lines)
    accumulator = 0
    nLine = 0
    alreadyDone = []
    if lines[k][:3] == 'nop':
        linesCopy[k] = 'jmp'+lines[k][3:]
    
    elif lines[k][:3] == 'jmp':
        linesCopy[k] = 'nop'+lines[k][3:]

    while nLine not in alreadyDone:
            line=linesCopy[nLine]
            alreadyDone = alreadyDone + [nLine]
            nLine,accumulator=nextLine(nLine,line,accumulator)
            if nLine==len(lines):
                print(k, accumulator)
                break
