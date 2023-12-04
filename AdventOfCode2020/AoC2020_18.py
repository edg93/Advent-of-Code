with open("AoC2020_18_data.txt", "r") as file:
    data = file.read()
data=data.split('\n')

def solve(tail,part):
    while '(' in tail:
        lastOpen = 0
        for k,letter in enumerate(tail):
            if letter == '(':
                lastOpen = k
            elif letter == ')':
                tail = tail[:lastOpen] + str(solve(tail[lastOpen+1:k],part)) + tail[k+1:]
                break
    tail = tail.split()
    if part==1:
        result, tail = int(tail[0]),tail[1:]
        for k,letter in enumerate(tail):
            if letter == '+':
                result += int(tail[k+1])
            elif letter == '*':   
                result *= int(tail[k+1])
        return result
    else:
        if '+' in tail:
            while True:
                for k,letter in enumerate(tail):
                    if letter == '+':
                        tail = tail[:k-1] + [int(tail[k-1])+int(tail[k+1])] + tail[k+2:]
                        break
                if '+' not in tail:
                    break
        return eval(''.join([str(x) for x in tail]))

for part in [1,2]:
    ans=0
    for line in data:
        ans += solve(line,part)
    print(ans)