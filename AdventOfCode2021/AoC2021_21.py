p1 = 7-1
p2 = 3-1
dice = 0
rolls = 0
DP = {}

def turn1(p1,p2,s1,s2):
    global dice,rolls
    if s2 >= 1000:
        return s1*rolls
    pos = (p1 + 3*dice+6)%10 
    score = s1 + pos + 1
    dice = (dice + 3)%100
    rolls += 3
    return turn1(p2,pos,s2,score)
    
def turn2(p1,p2,s1,s2):
    if s2 >= 21:
        return (0,1)
    if (p1,p2,s1,s2) in DP:
        return DP[(p1,p2,s1,s2)]
    wins = (0,0)
    for d1 in [1,2,3]:
        for d2 in [1,2,3]:
            for d3 in [1,2,3]:
                pos = (p1 + d1 + d2 + d3)%10
                score = s1 + pos + 1
                x,y = turn2(p2,pos,s2,score)
                wins = (wins[0]+y,wins[1]+x)
    DP[(p1,p2,s1,s2)]=wins
    return wins
    
print(turn1(p1,p2,0,0))
print(max(turn2(p1,p2,0,0)))