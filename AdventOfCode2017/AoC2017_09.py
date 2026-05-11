with open('AoC2017_09_data.txt', "r") as f:
    data = f.read()

def score(s):
    depth,score,garbage_count,i = 0,0,0,0
    garbage = False
    while i < len(s):
        c = s[i]
        if garbage:
            if c == '!':
                i += 2
                continue
            elif c == '>':
                garbage = False
            else:
                garbage_count+=1
            i+=1
            continue
        # not in garbage
        if c == '<':
            garbage = True
        elif c == '{':
            depth += 1
        elif c == '}':
            score += depth
            depth -= 1
        i += 1
    return score,garbage_count

print(score(data))