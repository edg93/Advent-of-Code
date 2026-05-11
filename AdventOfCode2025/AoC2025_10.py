from collections import deque
from time import time

for file in ["AoC2025_10_test.txt","AoC2025_10_data.txt"]:
    with open(file, "r") as f:
        data = f.read()
    
    data = data.split('\n')
    ans = [0,0]
    
    def click(lights,button):
        for i,light in enumerate(lights):
            if i in button:
                if light=='#':
                    lights = lights[:i] + '.' + lights[i+1:]
                else:
                    lights = lights[:i] + '#' + lights[i+1:]
        return lights
    
    def all_off(lights):
        return '#' not in lights
    
    def reduce_fixed_joltage(joltages,index,buttons):
        to_return = set()
        n = len(buttons)
        if n==0:
            return set()
        bounds = tuple([min(joltages[i] for i in button) for button in buttons])
        possibilities = bounded_compositions(joltages[index],bounds,n)
        for presses in possibilities:
            new_joltages = list(joltages)
            valid = True
            for p, button in zip(presses, buttons):
                if p == 0:
                    continue
                for i in button:
                    new_joltages[i] -= p
                    if new_joltages[i] < 0:
                        valid = False
                        break
            
            if valid:
                to_return.add(tuple(new_joltages))
        return to_return
    
    compositions_cash = {}
    def bounded_compositions(j,bounds,n):
        if n == 1:
            if j<= bounds[-1]:
                return [(j,)]
            else:
                return []
        if (j,bounds,n) in compositions_cash:
            return compositions_cash[(j,bounds,n)]
        result = []
        for i in range(min(j,bounds[-n]) + 1):
            for rest in bounded_compositions(j - i,bounds, n - 1):
                result.append((i,) + rest)
        compositions_cash[(j,bounds,n)]=result
        return result
    
    def order_indices(active_buttons,free_indices,n):
        buttons_by_index = {}
        for i in range(n):
            buttons_by_index[i]=tuple([b for b in active_buttons if i in b])
        if len(free_indices)==1:
            return [(list(free_indices)[0],active_buttons)]
        indices_frequencies = [[0,i] for i in range(n)]
        for button in active_buttons:
            for index in button:
                indices_frequencies[index][0]+=1
        indices_frequencies.sort()
        indices_ordered = [index for (_,index) in indices_frequencies]
        for j in range(len(indices_ordered)):
            index = indices_ordered[j]
            if index in free_indices and len(buttons_by_index[index])>0:
                surviving_buttons = tuple([button for button in active_buttons if button not in buttons_by_index[index]])
                return [(index,buttons_by_index[index])] + order_indices(surviving_buttons,free_indices-{index},n)
        l = []
        for index in free_indices:
            l += [(index,())]
        return l
    
    def alternative_order_indices(buttons,joltages):
        indices = [(joltages[i],i) for i in range(len(joltages))]
        indices.sort()
        indices = [i for (_,i) in indices]
        buttons_selected = []
        buttons_eliminated = set()
        for j in range(len(indices)):
            buttons_selected.append(tuple([button for button in buttons if indices[j] in button and button not in buttons_eliminated]))
            buttons_eliminated|=set(buttons_selected[-1])
        
        to_return = []
        for index,buttons_selected in zip(indices,buttons_selected):
            to_return.append((index,buttons_selected))
        return to_return
    
    t0 = time()
    for i,line in enumerate(data):
        if i not in [34]:
            continue
        t = time()
        print(i,len(data),line)
        
        #PARSING
        lights,rest = line.split('] ')
        lights = lights.strip('[')
        buttons, joltages = rest.split(' {')        
        joltages = tuple([int(x) for x in joltages.strip('}').split(',')])
        n = len(joltages)
        buttons = [ x.strip('()') for x in buttons.split()]
        buttons = tuple([tuple([int(y) for y in x.split(',')]) for x in buttons])
        
        #PART 1
        Q = deque([])
        Q.append((lights,0))
        seen = set()
        while Q:
            lights,moves = Q.popleft()
            if all_off(lights):
                ans[0]+=moves
                break
            for button in buttons:
                new_lights = click(lights,button)
                if new_lights in seen:
                    continue
                seen.add(new_lights)
                Q.append((new_lights,moves+1))
        
        #PART 2
        Q = deque([])
        moves = 0
        #new_joltages = list(joltages)
        #best_button = max(buttons, key=len)
        #while min(new_joltages)>50:
        #    for i in range(n):
        #        if i in best_button:
        #            new_joltages[i]-=1
        #    moves +=1
        #joltages = tuple(new_joltages)
        Q.append((joltages,moves))
        indices = set([i for i in range(n)])
        indices_ordered = order_indices(buttons,indices,n)
        #indices_ordered = alternative_order_indices(buttons,joltages)
        surviving_buttons={}
        for j in range(n):
            index,index_buttons = indices_ordered[n-1-j]
            if j == 0:
                surviving_buttons[index]=index_buttons
            else: surviving_buttons[index] = set(index_buttons)|set(surviving_buttons[indices_ordered[n-j][0]])
                
        min_moves = {}
        goal = tuple([0 for _ in range(n)])
        for index,index_buttons in indices_ordered:
            print(index,len(index_buttons),len(surviving_buttons[index]))
            for j in range(len(Q)):
                if j==0:
                    print(len(Q))
                joltages,moves = Q.popleft()
                s = tuple(joltages)
                if s in min_moves and moves>min_moves[s]:
                    continue
                if goal in min_moves and moves+max(joltages)>=min_moves[goal]:
                    print('fddfds')
                    continue
                if len(index_buttons)==0 and len(surviving_buttons)>0:
                    break
                if len(surviving_buttons[index])==1:
                    p = max(joltages)
                    new_joltages = list(joltages)
                    valid = True
                    for k in index_buttons[0]:
                        new_joltages[k]-=p
                    for joltage in new_joltages:
                        if joltage !=0:
                            valid = False
                            break
                    if valid:
                        new_joltages = tuple(new_joltages)
                        if new_joltages in min_moves:
                            min_moves[new_joltages] = min(min_moves[new_joltages],moves+p)
                        else:
                            min_moves[new_joltages] = moves+p
                    continue
                            
                if joltages[index]==0:
                    Q.append((joltages,moves))
                    continue
                new_joltages_set = reduce_fixed_joltage(joltages,index,index_buttons)
                for new_joltages in new_joltages_set:
                    if new_joltages not in min_moves or moves+joltages[index]<min_moves[new_joltages]:
                        if goal in min_moves and moves+joltages[index]+max(new_joltages)>=min_moves[goal]:
                            continue
                        min_moves[new_joltages]=moves+joltages[index]
                        Q.append((new_joltages,moves+joltages[index]))
        
        ans[1]+=min_moves[goal]
        print('iteration time. {}s, total time: {}s'.format(round(time()-t),round(time()-t0)))

    print(ans)
    
#Problemi: 12 (ca 10m) 32,34,70,115 (ca 9m), 137 (ca 4min)
# 14333 ans sugli altri casi
# 12+115+137 -> 408

#32          -> 141
#1 5 13
#1
#3 2 8
#1150626
#2 2 6
#11739361
#5 1 4
#115665634
#0 1 3
#44303584
#4 1 2
#8520583

#34
#0 4 13
#1
#2 3 9
#12257
#4 2 6
#3552345
#7 1 4
#46239566
#1 2 3
#45483374

#70
#8 5 12
#1
#9 3 7
#316251
#1 1 4
#146577276