with open("AoC2019_16_data.txt", "r") as f:
    data = f.read()

ans = [0,0]

pattern = [0,1,0,-1]

signal = [int(x) for x in data]
n = len(signal)

for _ in range(100):
    new_signal = []
    for i in range(n):
        total = 0
        for j in range(n):
            pattern_index = ((j + 1) // (i + 1)) % 4
            total += signal[j] * pattern[pattern_index]
        new_signal.append(abs(total) % 10)

    signal = new_signal
          
ans[0] = ''.join([str(x) for x in signal[:8]])

signal = [int(c) for c in data] * 10_000
offset = int(data[:7])
signal = signal[offset:]    

for _ in range(100):
    suffix_sum = 0
    for i in range(len(signal) - 1, -1, -1):
        suffix_sum += signal[i]
        signal[i] = suffix_sum % 10

ans[1] = "".join(map(str, signal[:8]))
print(ans)