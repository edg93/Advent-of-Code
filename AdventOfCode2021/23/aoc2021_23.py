"Day 23 of AOC2021"
from collections import deque
  
cost = {'A':1,'B':10,'C':100,'D':1000}

pos = {'A':'BDDC','B':'ABCA','C':'BABD','D':'CCAD','h':[None,None,None,None,None,None,None],'$':0}
#pos = {'A':'BC','B':'AA','C':'BD','D':'CD','h':[None,None,None,None,None,None,None],'$':0}

N = len(pos['A'])

def turn(pos,min_cost):
    check = True
    while check:
        check = False
        for i in range(len(pos['h'])):
            x = pos['h'][i]
            if x is not None and pos[x].count(x)==len(pos[x]) and free_path(pos,i,x):
                pos['h'][i]=None
                pos['$'] += cost[x]*compute_cost(pos,i,x)
                pos[x]+=x
                check = True
        for letter,pile in pos.items():
            if letter not in ['h','$'] and len(pile)>0:
                true_letter = pile[-1]
                if letter == 'A':
                    a = 1
                    b = 2
                elif letter == 'B':
                    if true_letter == 'A':
                        a = 3
                        b = 2
                    else:
                        a = 2
                        b = 3
                elif letter == 'C':
                    if true_letter == 'D':
                        a = 3
                        b = 4
                    else: 
                        a = 4
                        b = 3
                else:
                    a = 5
                    b = 4
                if pile[-1]!=letter and free_path(pos,a,true_letter) and pos[true_letter].count(true_letter)==len(pos[true_letter]):
                    pos['$']+=cost[true_letter]*(compute_cost(pos,b,true_letter)+compute_cost(pos,b,letter))
                    pos[letter] = pos[letter][:-1]
                    pos[true_letter]+=true_letter
                    check = True
    if pos['A']== 'A'*N and pos['B']=='B'*N and pos['C']=='C'*N and pos['D']=='D'*N:
        if pos['$'] < min_cost:
             min_cost = pos['$']
             return pos['$']
    pos_list = []
    for K in ['A','B','C','D']:
        if len(pos[K])>0 and pos[K].count(K)!=len(pos[K]):
            for i in range(len(pos['h'])):
                letter = pos[K][-1]
                c = compute_cost(pos,i,K)
                pos[K] = pos[K][:-1]
                if pos['h'][i]==None and free_path(pos,i,K):
                    pos['h'][i]=letter
                    new_h = pos['h'].copy()
                    new_pos = pos.copy()
                    new_pos['h']=new_h
                    new_pos['$'] += cost[letter]*c
                    pos_list += [new_pos]
                    pos['h'][i]=None
                pos[K]+=letter
                    
            
    return pos_list

def free_path(pos,i,home):
    if home=='A':
        if i<2:
            for j in range(2-i-1):
                if pos['h'][2-j-1]!=None:
                    return False
            return True
        else:
            for j in range(i-2):
                if pos['h'][2+j]!=None:
                    return False
            return True
    elif home=='B':
        if i<3:
            for j in range(3-i-1):
                if pos['h'][3-j-1]!=None:
                    return False
            return True
        else:
            for j in range(i-3):
                if pos['h'][3+j]!=None:
                    return False
            return True
    elif home=='C':
        if i<4:
            for j in range(4-i-1):
                if pos['h'][4-j-1]!=None:
                    return False
            return True
        else:
            for j in range(i-4):
                if pos['h'][4+j]!=None:
                    return False
            return True
    elif home=='D':
        if i<5:
            for j in range(5-i-1):
                if pos['h'][5-j-1]!=None:
                    return False
            return True
        else:
            for j in range(i-5):
                if pos['h'][5+j]!=None:
                    return False
            return True
        
def compute_cost(pos,i,home):
    cost = 0
    if pos[home].count(home)==len(pos[home]):
        cost += N-len(pos[home])
    else:
        cost += N-len(pos[home])+1
    if home == 'A':
        if i <2:
            cost += 2-i
        elif i==6:
            cost += 8
        else:
            cost += 2*(i-2)+1 
    elif home == 'B':
        if i < 2:
            cost+=4-i
        elif i>4:
            cost+=i
        elif i == 2 or i==3:
            cost+=1
        else:
            cost+=3
    elif home == 'C':
        if i < 2:
            cost+=6-i
        elif i>4:
            cost+=i-2
        elif i == 4 or i==3:
            cost+=1
        else:
            cost+=3
    elif home == 'D':
        if i >4:
            cost += i-4
        elif i==0:
            cost += 8
        else:
            cost += 2*(4-i)+1 
    return cost

min_cost = 10e9
Q = deque([pos])

while Q:
    pos = Q.popleft()
    new_pos = turn(pos,min_cost)
    if type(new_pos)==int:
        if new_pos < min_cost:
            min_cost = new_pos
    else:
        for x in new_pos:
            Q.append(x)

print(min_cost)