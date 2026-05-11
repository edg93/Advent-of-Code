data = '10111011111001111'
ans = [0,0]

L = 272

def solve(data, L):
    # Build data up to length L
    s = list(data)
    while len(s) < L:
        b = ['1' if c == '0' else '0' for c in reversed(s)]
        s.append('0')
        s.extend(b)
    s = s[:L]

    # Compute checksum
    while len(s) % 2 == 0:
        s = ['1' if s[i] == s[i+1] else '0' for i in range(0, len(s), 2)]

    return ''.join(s)

ans[0] = solve(data,272)
ans[1] = solve(data,35651584)
print(ans)