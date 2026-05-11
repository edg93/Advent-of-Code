from IntcodeComputer import computer
from collections import deque

# Load Intcode program
with open("AoC2019_23_data.txt") as f:
    data_list = [int(x) for x in f.read().strip().split(',')]

ans = [None,0]

# --- initialize 50 computers ---
N = 50
computers = []
for addr in range(N):
    mem = defaultdict(int, {i:v for i,v in enumerate(data_list)})
    computers.append({
        "data": mem,
        "idx": 0,
        "base": 0,
        "inputs": [addr],
        "out_buf": []
    })

# --- network loop ---
nat_packet = None
last_nat_y = None
while True:
    idle = True  # Track if all computers are idle this cycle
    for comp in computers:
        data = comp["data"]
        idx = comp["idx"]
        base = comp["base"]
        inputs = comp["inputs"]
        out_buf = comp["out_buf"]

        # Run one instruction step
        result = computer(data, inputs, idx, base)
        data, idx, base, output = result
        comp["data"] = data
        comp["idx"] = idx
        comp["base"] = base

        if output == 'INPUT':
            # feed -1 if no input is queued
            if not inputs:
                inputs.append(-1)
            else:
                idle = False
            continue  # next cycle, will pick up input in next step
        idle = False
        out_buf.append(output)
        if len(out_buf) == 3:
            dest, X, Y = out_buf
            out_buf.clear()
            if dest == 255:
                if ans[0] is None:
                    ans[0] = Y
                nat_packet = (X, Y)
            else:
                computers[dest]["inputs"].append(X)
                computers[dest]["inputs"].append(Y)
                
                
    if idle and nat_packet:
        X, Y = nat_packet
        computers[0]['inputs'].append(X)
        computers[0]['inputs'].append(Y)
        if last_nat_y == Y:
            ans[1]=Y
            break
        last_nat_y = Y

print(ans)
