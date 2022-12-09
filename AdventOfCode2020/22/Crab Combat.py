from copy import copy

f = open("data.txt", "r")
data = f.read()
data=data.split('Player 2:')

player1=data[0].split('\n')[1:-2]
player2=data[1].split('\n')[1:]

    

def round(p1,p2):
    a1,a2 = p1[0],p2[0]
    p1,p2 = p1[1:],p2[1:]
    if int(a1)>int(a2):
        p1 = p1 + [a1,a2]
    else:
        p2 = p2 + [a2,a1]
    return p1,p2

def score(p):
    tot = 0
    for k in range(len(p)):
        tot = tot + (len(p)-k)*int(p[k])
    return tot

while not (player1==[] or player2 == []):
    print(player1,player2)
    player1,player2 = round(player1,player2)


print(player1, score(player1))
print(player2, score(player2))