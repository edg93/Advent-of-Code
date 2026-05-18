#cost damage armor
weapons = [(8,4,0),(10,5,0),(25,6,0),(40,7,0),(74,8,0)]
armors = [(13,0,1),(31,0,2),(53,0,3),(75,0,4),(102,0,5),(0,0,0)]
rings = [(25,1,0),(50,2,0),(100,3,0),(20,0,1),(40,0,2),(80,0,3),(0,0,0)]

boss = (104,8,1)

def win(player,boss):
    player_hits = player[0]
    boss_hits = boss[0]
    player_turn = True
    while player_hits >0 and boss_hits>0:
        if player_turn:
            boss_hits -=max(1,player[1]-boss[2])
            player_turn=False
        else:
            player_hits -= max(1,boss[1]-player[2])
            player_turn=True

            
    if player_hits>0:
        return True
    return False

win_options = []
lose_options = []

for weapon in weapons:
    for armor in armors:
        for ring1 in rings:
            for ring2 in rings:
                if ring2==ring1 and ring2!=(0,0,0):
                    continue
                player = (100,weapon[1]+ring1[1]+ring2[1],armor[2]+ring1[2]+ring2[2])
                
                result = win(player, boss)
                cost = weapon[0]+armor[0]+ring1[0]+ring2[0]
                if result:
                    win_options.append(cost)
                else:
                    lose_options.append(cost)
                    
ans = [0,0]
ans[0] = min(win_options)
ans[1] = max(lose_options)
print(ans)