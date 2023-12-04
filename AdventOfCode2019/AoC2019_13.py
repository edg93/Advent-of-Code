from IntcodeComputer import computer

with open("AoC2019_13_data.txt", "r") as file:
    data0 = file.read()

data0 = [int(x) for x in data0.split(',')]

data = {n:x for n,x in enumerate(data0)}

outputs = []
output,i,base = 0,0,0
while output!=None:
    data,i,base,output = computer(data,0,i,base)
    outputs.append(output)
    
ans1=0
for i in range(2,len(outputs),3):
    if(outputs[i]==2):
        ans1+=1

print(ans1)

data = {n:x for n,x in enumerate(data0)}
data[0]=2

output,i,base,ip = 0,0,0,0
a = [0,0,0]
move = False
ball = -1
paddle = ball-1
ans2 = 0
while output!=None:
    for k in range(3):
        data,i,base,output = computer(data,ip,i,base)
        if output == None:
            break
        a[k]=output
    if a[2]==3:
        paddle = a[0]
    elif a[2]==4:
        ball = a[0]
        if move:
            ip = ball-paddle
            paddle = ball
    elif a[0]==-1 and a[1] == 0:
        ans2 = a[2]
    if not move and ball == paddle:
        move = True
    
print(ans2)
    
