A = 703
B = 516
N = 2147483647
factor_A = 16807
factor_B = 48271
ans = [0,0]

def gen_1(start, factor):
    val = start
    while True:
        val = (val * factor) % 2147483647
        yield val

A_gen = gen_1(A, factor_A)
B_gen = gen_1(B, factor_B)
for _ in range(40_000_000):
    if (next(A_gen) & 0xFFFF) == (next(B_gen) & 0xFFFF):
        ans[0] += 1

def gen_2(start, factor, multiple):
    val = start
    while True:
        val = (val * factor) % 2147483647
        if val % multiple == 0:
            yield val
        
A_gen = gen_2(A, factor_A, 4)
B_gen = gen_2(B, factor_B, 8)
for _ in range(5_000_000):
    if (next(A_gen) & 0xFFFF) == (next(B_gen) & 0xFFFF):
        ans[1] += 1

print(ans)