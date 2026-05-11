from time import time
t = time()
for file in ["AoC2025_08_test.txt","AoC2025_08_data.txt"]:
    with open(file, "r") as f:
        data = f.read()
        
    data = data.split('\n')
    ans = [0,0]
    circuits = {}
    
    def distance(x1,y1,z1,x2,y2,z2):
        return (x2-x1)**2+(y2-y1)**2+(z2-z1)**2
    
    distances = []
    
    for i,box1 in enumerate(data):
        x1,y1,z1 = [int(a) for a in box1.split(',')]
        data[i] = x1,y1,z1 
        circuits[i]={i}
        for j,box2 in enumerate(data[i+1:]):
            x2,y2,z2 = [int(a) for a in box2.split(',')]
            distances.append((distance(x1,y1,z1,x2,y2,z2),i,j+i+1))
            
    distances.sort()
    
    def compute_ans1(circuits):
        boxes = {x for x in range(len(data))}
        done = set()
        circuit_len = []
        for box in boxes:
            if box not in done:
                circuit_len.append(len(circuits[box]))
                done |= circuits[box]
                
        circuit_len.sort()
        return circuit_len[-1]*circuit_len[-2]*circuit_len[-3]
    
    if file == "AoC2025_08_test.txt":
        N = 10
    else:
        N = 1000
    
    for i in range(len(distances)):
        box1,box2 = distances[i][1:]
        if box2 in circuits[box1]:
            continue
        for box in circuits[box1] | circuits[box2]:
            circuits[box]= circuits[box1] | circuits[box2]
        if i==N-1:
            ans[0] = compute_ans1(circuits)

        if len(circuits[box1])==len(data):
            ans[1] = data[box1][0]*data[box2][0]
            break
    print(ans)

print(time()-t)    