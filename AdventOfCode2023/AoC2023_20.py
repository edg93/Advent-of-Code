from collections import defaultdict,deque
from math import gcd

def lcm(a, b):
    return a * b // gcd(a, b)

def parse_input(lines):
    modules = {}
    inputs = defaultdict(list)  # destination -> list of sources

    # First pass: parse module types and outputs
    for line in lines:
        left, right = line.strip().split(" -> ")
        outputs = right.split(", ")

        if left == "broadcaster":
            name = left
            modules[name] = {
                "type": "broadcaster",
                "outputs": outputs,
            }
        else:
            prefix = left[0]
            name = left[1:]

            if prefix == "%":
                modules[name] = {
                    "type": "flipflop",
                    "outputs": outputs,
                    "state": False,  # OFF initially
                }
            elif prefix == "&":
                modules[name] = {
                    "type": "conjunction",
                    "outputs": outputs,
                    "memory": {},    # filled later
                }

        # Track reverse edges
        for out in outputs:
            inputs[out].append(name)

    # Second pass: initialize conjunction memory
    for name, module in modules.items():
        if module["type"] == "conjunction":
            module["memory"] = {src: 0 for src in inputs[name]}

    return modules, inputs

def detect_cycle(src, dst, pulse):
    global press

    if src not in seen:
        seen[src] = press
    elif src not in cycles:
        cycles[src] = press - seen[src]

def press_button(modules):
    """
    Simulate one button press.

    - modules: parsed module graph (mutated in-place)
    - count_pulses: whether to count low/high pulses
    - hook: optional callback for part 2
        hook(src, dst, pulse) is called for every pulse
    """
    Q = deque()
    Q.append(("button", "broadcaster", 0))

    low = high = 0
    

    while Q:
        src, dst, pulse = Q.popleft()

        # Count pulses (Part 1)
        if pulse == 0:
            low += 1
        else:
            high += 1
            
        if dst == rx_parent and pulse == 1:
            detect_cycle(src, dst, pulse)

        # If destination is not a module (e.g. "rx"), stop
        if dst not in modules:
            continue
        
        

        module = modules[dst]
        mtype = module["type"]

        # Broadcaster
        if mtype == "broadcaster":
            for out in module["outputs"]:
                Q.append((dst, out, pulse))

        # Flip-flop
        elif mtype == "flipflop":
            if pulse == 1:
                continue  # ignores high pulses

            module["state"] = not module["state"]
            out_pulse = 1 if module["state"] else 0

            for out in module["outputs"]:
                Q.append((dst, out, out_pulse))

        # Conjunction
        elif mtype == "conjunction":
            module["memory"][src] = pulse

            # If all inputs are high → send low
            if all(v == 1 for v in module["memory"].values()):
                out_pulse = 0
            else:
                out_pulse = 1

            for out in module["outputs"]:
                Q.append((dst, out, out_pulse))

    return low, high


with open("AoC2023_20_data.txt", "r") as file:
    data = file.read().splitlines()

ans = [0,1]

modules,inputs = parse_input(data)

total_low = total_high = 0

for _ in range(1000):
    lo, hi = press_button(modules)
    total_low += lo
    total_high += hi

ans[0] = total_high*total_low

modules,inputs = parse_input(data)
rx_parent = inputs['rx'][0]
important_inputs = set(modules[rx_parent]["memory"].keys())
seen = {}
cycles = {}
press = 0

while len(cycles) < len(important_inputs):
    press += 1
    press_button(modules)

#note that seen and cycles are the same, so there is not offset at the beginning.
for c in cycles.values():
    ans[1] = lcm(ans[1], c)

print(ans)