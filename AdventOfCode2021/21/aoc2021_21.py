"Day 21 of AOC2021"
    
#players = {1:[4,0], 2:[8,0]}
players = {1:[7,0], 2:[3,0]}
last = 2
dice = 0
rolls = 0


while players[1][1]<1000 and players[2][1]<1000:
    if last == 2:
        players[1][0] = (players[1][0] + 3*dice+6)%10
        players[1][1] = players[1][1] + players[1][0]
        if players[1][0]== 0:
            players[1][1] += 10
        dice = (dice + 3)%100
        last = 1
    else:
        players[2][0] = (players[2][0] + 3*dice+6)%10
        players[2][1] = players[2][1] + players[2][0]
        if players[2][0]== 0:
            players[2][1] += 10
        dice = (dice + 3)%100
        last = 2
    rolls += 3
    
if players[1][1]<1000:
    print(players[1][1]*rolls)
else:
    print(players[2][1]*rolls)
        