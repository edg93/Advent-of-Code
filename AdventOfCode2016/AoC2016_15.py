#Disc #1 has 5 positions; at time=0, it is at position 2.
#Disc #2 has 13 positions; at time=0, it is at position 7.
#Disc #3 has 17 positions; at time=0, it is at position 10.
#Disc #4 has 3 positions; at time=0, it is at position 2.
#Disc #5 has 19 positions; at time=0, it is at position 9.
#Disc #6 has 7 positions; at time=0, it is at position 0.

ans = [0,0]
discs = [(1,5,2),(2,13,7),(3,17,10),(4,3,2),(5,19,9),(6,7,0)]

from math import prod

def crt(congruences):
    """
    congruences: list of (remainder, modulus)
    returns smallest non-negative solution
    """
    N = prod(n for _, n in congruences)
    result = 0

    for a, n in congruences:
        Ni = N // n
        # modular inverse of Ni mod n
        inv = pow(Ni, -1, n)
        result += a * Ni * inv

    return result % N

def solve(discs):
    """
    discs: list of (disc_number, positions, start_position)
    """
    congruences = []

    for i, n, p in discs:
        a = (- (i + p)) % n
        congruences.append((a, n))

    return crt(congruences)

ans[0] = solve(discs)
discs.append((7,11,0))
ans[1] = solve(discs)
print(ans)