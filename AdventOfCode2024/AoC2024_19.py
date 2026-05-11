from collections import deque

for file in ["AoC2024_19_test.txt","AoC2024_19_data.txt"]:
    with open(file, "r") as f:
        data = f.read()        
        
    ans = [0,0]
    storage,orders = data.split('\n\n')
    storage = storage.split(', ')
    storage=set(storage)
    orders = orders.split('\n')
    
    impossible_orders = set()
    possible_orders = {}
    
    def check_order(order):
        
        for j in range(1,len(order)+1):
            Q = deque([])
            truncated_order = order[len(order)-j:]
            Q.append(truncated_order)

            if truncated_order in possible_orders.keys():
                continue
            while Q:
                new_order = Q.pop()
                impossible = True
                
                if new_order == '':
                    if truncated_order in possible_orders.keys():
                        possible_orders[truncated_order]+=1
                    else:
                        possible_orders[truncated_order]=1
                    continue
                
                if new_order in possible_orders.keys():
                    if truncated_order in possible_orders.keys():
                        possible_orders[truncated_order]+=possible_orders[new_order]
                    else:
                        possible_orders[truncated_order]=possible_orders[new_order]
                    impossible = False
                    continue
                
                for model in storage:
                    new_order_sliced = new_order[len(model):]
                    if new_order_sliced in impossible_orders:
                        continue
                    if new_order[:len(model)]==model:
                        Q.append(new_order_sliced)
                        impossible = False
                if impossible:
                    impossible_orders.add(new_order)


        if order in possible_orders.keys():
            return possible_orders[order]
        else:
            return 0

    for i,order in enumerate(orders):
        possible_ways = check_order(order)
        if possible_ways!=0:
            ans[0]+=1
        ans[1]+=possible_ways
    
    print(ans)