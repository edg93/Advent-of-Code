with open("AoC2024_13_data.txt", "r") as file:
    data = file.read()
        
costs = {'A':3,'B':1}
ans1,ans2 = 0,0
machines = data.split('\n\n')

def read_line(line):
    line = line.split(': ')[1]
    x,y = line.split(', ')
    return int(x[2:]),int(y[2:])

for machine in machines:
    A,B,prize = machine.split('\n')
    xA,yA = read_line(A)
    xB,yB = read_line(B)
    xP,yP = read_line(prize)
    for i in (0,10000000000000):
        xP,yP = i+xP,i+yP
        n = round((yP - yA/xA * xP)/(yB-xB*yA/xA))
        m = round((xP - n*xB)/xA)
        if xP == m*xA+n*xB and yP == m*yA+n*yB:
            if i==0:
                ans1+=m*3+n
            else:
                ans2+=m*3+n
        
print(ans1,ans2)