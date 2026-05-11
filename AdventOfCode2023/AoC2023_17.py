import heapq

for file in ["AoC2023_17_test.txt","AoC2023_17_data.txt"]:
    with open(file, "r") as f:
        data = f.read()
        
    ans = [0,0]
    data = data.split('\n')
    R,C = len(data),len(data[0])
    
    DIR = ((1,0),(-1,0),(0,1),(0,-1))
             
    def find_min(min_steps,max_steps):
        costs = {}
        
        pq = []
        for dr, dc in DIR:
            if 0<=dr*min_steps<R and 0<=dc*min_steps<C:
                heapq.heappush(pq, (0, 0, 0, dr, dc, 0))
                
    
        while pq:
            cost, r, c, dr, dc, steps = heapq.heappop(pq)
            state = (r, c, dr, dc, steps)
            if state in costs and costs[state] <= cost:
                continue
            if 0<=r+dr*(min_steps-steps)<R and 0<= c+dc*(min_steps-steps)<C:
                costs[state] = cost
            else:
                continue
            if steps < min_steps:
                
                if  0 <= r+dr < R and 0 <= c+dc < C:
                    heapq.heappush(pq,(cost + int(data[r+dr][c+dc]), r+dr, c+dc, dr, dc, steps+1))
                continue
                
            for ndr,ndc in DIR:
                if (ndr, ndc) == (-dr, -dc):
                    continue
                nr, nc = r + ndr, c + ndc
                if (ndr, ndc) == (dr, dc):
                    new_steps = steps + 1
                else:
                    new_steps = 1
                if  0 <= nr < R and 0 <= nc < C and new_steps<=max_steps:
                    heapq.heappush(pq,(cost + int(data[nr][nc]), nr, nc, ndr, ndc, new_steps))
        
        return min([costs[key] for key in costs if key[0]==R-1 and key[1]==C-1])
    
    ans[0] = find_min(1,3)
    ans[1] = find_min(4,10)
    print(ans)