from IntcodeComputer import run_intcode

with open('AoC2019_21_data.txt', "r") as f:
    data = f.read()

data = [int(x) for x in data.split(',')]

ans = [0,0]

script = 'NOT A J\nNOT B T\nOR T J\nNOT C T\nOR T J\nAND D J\nWALK\n'
ascii_out, damage = run_intcode(data, script)
print("ASCII output:\n", ascii_out)
print("Final numeric output:", damage)
ans[0] = damage

script = 'NOT A J\nNOT B T\nOR T J\nNOT C T\nOR T J\nAND D J\nNOT E T\nNOT T T\nOR H T\nAND T J\nRUN\n'
ascii_out, damage = run_intcode(data, script)
print("ASCII output:\n", ascii_out)
print("Final numeric output:", damage)
ans[1] = damage

print(ans)