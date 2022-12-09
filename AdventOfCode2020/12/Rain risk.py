f = open("data.txt", "r")
data = f.read()
data=data.split('\n')

orientation = [0 for x in range(len(data))]
orientation[-1  ]=90

moves = {"N":[],"S":[],"E":[],"W":[]}

for k in range(len(data)):
    instruction = data[k]
    if instruction[0]=='L':
        orientation[k]=(orientation[k-1]-int(instruction[1:]))%360
    elif instruction[0]=='R':
        orientation[k]=(orientation[k-1]+int(instruction[1:]))%360
    elif instruction[0]=='N':
        orientation[k]=orientation[k-1]
        moves["N"]=moves["N"]+[int(instruction[1:])]
    elif instruction[0]=='S':
        orientation[k]=orientation[k-1]
        moves["S"]=moves["S"]+[int(instruction[1:])]
    elif instruction[0]=='E':
        orientation[k]=orientation[k-1]
        moves["E"]=moves["E"]+[int(instruction[1:])]
    elif instruction[0]=='W':
        orientation[k]=orientation[k-1]
        moves["W"]=moves["W"]+[int(instruction[1:])]
    elif instruction[0]=='F':
        orientation[k]=orientation[k-1]
        if orientation[k]==0:
            moves["N"]=moves["N"]+[int(instruction[1:])]
        elif orientation[k]==90:
            moves["E"]=moves["E"]+[int(instruction[1:])]
        elif orientation[k]==180:
            moves["S"]=moves["S"]+[int(instruction[1:])]
        elif orientation[k]==270:
            moves["W"]=moves["W"]+[int(instruction[1:])]

def computePosition(dict):
    position = [0,0]
    for move in dict["N"]:
        position[1]=position[1]+move
    for move in dict["E"]:
        position[0]=position[0]+move
    for move in dict["S"]:
        position[1]=position[1]-move
    for move in dict["W"]:
        position[0]=position[0]-move
    return position
       
finalPos=computePosition(moves)
print(finalPos)
print(abs(finalPos[0])+abs(finalPos[1]))