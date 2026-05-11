from collections import deque

ans = [0,0]

duel = (50,500,0,set(),58) #hits, mana, mana spent, active spells,boss hits
Q = deque([])
Q.append(duel)

spells = ['MM','drain','shield','poison','recharge']
mana_costs = {'recharge':229,'poison':173,'shield':113,'drain':73,'MM':53}
min_mana = 10e9

def player_turn(spell,hits,mana,mana_spent,active_spells,boss):
    
    hits,mana,active_spells,boss = apply_effects(hits,mana,active_spells,boss)
            
    if boss<=0:
        return hits,mana,mana_spent,active_spells,boss
        
    mana -= mana_costs[spell]
    mana_spent += mana_costs[spell]
    if spell == 'MM':
        boss -= 4
    elif spell == 'drain':
        boss -= 2
        hits += 2
    else:
        if spell == 'recharge':
            active_spells.add((spell,5))
        else:
            active_spells.add((spell,6))
            
    return hits,mana,mana_spent,active_spells,boss

def apply_effects(hits,mana,active_spells,boss):
    new_active_spells = set()
    for active_spell,counter in active_spells:
        counter -=1
        if active_spell == 'poison':
            boss -= 3
        elif active_spell == 'recharge':
            mana += 101
        if counter != 0:
            new_active_spells.add((active_spell,counter))
    return hits,mana,new_active_spells,boss
            
def boss_turn(hits,mana,active_spells,boss):
    hits,mana,active_spells,boss = apply_effects(hits,mana,active_spells,boss)
                
    if 'shield' in [x for x,_ in active_spells]:
        hits -= 2
    else:
        hits -= 9
    return hits,mana,active_spells,boss
    

while Q:
    hits,mana,mana_spent,active_spells,boss = Q.pop()
    
    if mana_spent> min_mana:
        continue
        
    for spell in spells:
        
        if spell in [x for x,counter in active_spells if counter >1]:
            continue
        
        new_hits,new_mana,new_mana_spent,new_active_spells,new_boss = player_turn(spell,hits,mana,mana_spent,active_spells,boss)
        
        if new_mana <0:
            continue
        
        new_hits,new_mana,new_active_spells,new_boss = boss_turn(new_hits,new_mana,new_active_spells,new_boss)
        
        if new_boss<=0:
            if new_mana_spent<min_mana:
                min_mana = new_mana_spent
            continue
            
        if new_hits>0:
            Q.append((new_hits,new_mana,new_mana_spent,new_active_spells,new_boss))

ans[0] = min_mana


min_mana = 10e9
Q = deque([])
Q.append(duel)
while Q:
    hits,mana,mana_spent,active_spells,boss = Q.pop()
    
    if mana_spent> min_mana:
        continue
    
    hits-=1
    if hits<=0:
        continue
    for spell in spells:
        
        if spell in [x for x,counter in active_spells if counter >1]:
            continue
        
        new_hits,new_mana,new_mana_spent,new_active_spells,new_boss = player_turn(spell,hits,mana,mana_spent,active_spells,boss)
        
        if new_mana <0:
            continue

        
        new_hits-=1
        if new_hits<=0:
            continue
        
        new_hits,new_mana,new_active_spells,new_boss = boss_turn(new_hits,new_mana,new_active_spells,new_boss)
        
        if new_boss<=0:
            if new_mana_spent<min_mana:
                min_mana = new_mana_spent
            continue
            
        if new_hits>0:
            Q.append((new_hits,new_mana,new_mana_spent,new_active_spells,new_boss))
            
ans[1] = min_mana
print(ans)
