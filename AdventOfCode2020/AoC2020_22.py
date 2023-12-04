with open("AoC2020_22_data.txt", "r") as file:
    data = file.read()
data=data.split('Player 2:')

def round1(p1,p2):
    a1,a2 = p1[0],p2[0]
    p1,p2 = p1[1:],p2[1:]
    if a1>a2:
        p1 += [a1,a2]
    else:
        p2 += [a2,a1]
    return p1,p2

def score(p):
    tot = 0
    for k in range(len(p)):
        tot += (len(p)-k)*int(p[k])
    return tot

def round2(p1,p2,seen):
    if (score(p1),score(p2)) in seen:
        return p1,[],[]
    else:
        seen.add((score(p1),score(p2)))
    a1,a2 = p1[0],p2[0]
    p1,p2 = p1[1:],p2[1:]
    if len(p1)<a1 or len(p2)<a2:
        if a1>a2:
            p1 += [a1,a2]
        else:
            p2 += [a2,a1]
    else:
        winner = game(p1[:int(a1)],p2[:int(a2)],2)[0]
        if winner==2:
            p2 += [a2,a1]
        else:
            p1 += [a1,a2]
    return p1,p2,seen

def game(p1,p2,part):
    a = set()
    while not (p1==[] or p2 == []):
        if part==2:
            p1,p2,a = round2(p1,p2,a)
        else:
            p1,p2 = round1(p1,p2)
    if p1 == []:
        return 2,p2
    else:
        return 1,p1

for part in [1,2]:
    player1=[int(x) for x in data[0].split('\n')[1:-2]]
    player2=[int(x) for x in data[1].split('\n')[1:]]
    result = game(player1,player2,part)
    print(score(result[1]))