data = [11,11,13,7,0,15,5,5,4,4,1,1,7,1,15,11]

ans = [0,0]

seen = {}
steps = 0

while tuple(data) not in seen:
    seen[tuple(data)] = steps
    max_bank = max(data)
    idx = data.index(max_bank)
    data[idx] = 0
    for k in range(max_bank):
        data[(idx+k+1)%len(data)]+=1
    ans[0]+=1
    steps +=1
    
ans[1] = ans[0]-seen[tuple(data)]
print(ans)