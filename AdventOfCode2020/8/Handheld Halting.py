f = open("data.txt", "r")
data = f.read()
lines=data.split('\n')
f.close()

def nextLine(nLine, line,accumulator):
    if line[:3]=='acc':
        accumulator = accumulator + int(line[4:])
        return nLine+1,accumulator
    elif line[:3]=='nop':
        return nLine+1,accumulator
    elif line[:3]=='jmp':
        return nLine+int(line[4:]),accumulator
    
accumulator = 0
nLine = 0
alreadyDone = []
    
while nLine not in alreadyDone:
    line=lines[nLine]
    alreadyDone = alreadyDone + [nLine]
    nLine,accumulator=nextLine(nLine,line,accumulator)
    
print(accumulator)
print(alreadyDone)