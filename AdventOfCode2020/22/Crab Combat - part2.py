from copy import copy

f = open("data.txt", "r")
data = f.read()
data=data.split('Player 2:')

player1=data[0].split('\n')[1:-2]
player2=data[1].split('\n')[1:]

def round(p1,p2,a):
    if [p1,p2] in a:
        return p1,[],[]
    else:
        a = a + [[p1,p2]]
    a1,a2 = p1[0],p2[0]
    p1,p2 = p1[1:],p2[1:]
    if len(p1)<int(a1) or len(p2)<int(a2):
        if int(a1)>int(a2):
            p1 = p1 + [a1,a2]
        else:
            p2 = p2 + [a2,a1]
    else:
        p1c,p2c = copy(p1),copy(p2)
        winner= game(p1c[:int(a1)],p2c[:int(a2)])[0]
        if winner==2:
            p2 = p2 + [a2,a1]
        else:
            p1 = p1 + [a1,a2]
    return p1,p2,a

def game(p1,p2):
    a=[]
    while not (p1==[] or p2 == []):
        p1,p2,a = round(p1,p2,a)
    if p1 == []:
        return 2,p2
    else:
        return 1,p1

def score(p):
    tot = 0
    for k in range(len(p)):
        tot = tot + (len(p)-k)*int(p[k])
    return tot

result = game(player1,player2)
print(result,score(result[1]))