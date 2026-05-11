with open("AoC2016_09_data.txt") as f:
    data = f.read().strip()

ans = [0,0]

def decompress(s,part_2=False):
    i = 0
    result = 0
    while i < len(s):
        if s[i] == '(':
            j = 1
            marker = ''
            while s[i + j] != ')':
                marker += s[i + j]
                j += 1
            length, times = [int(x) for x in marker.split('x')]
            i += j + 1 + length
            if part_2:
                segment = s[i-length:i]
                length = decompress(segment,part_2)
            result += length * times
        else:
            result += 1
            i += 1
    return result

ans[0] = decompress(data)
ans[1] = decompress(data,True)

print(ans)