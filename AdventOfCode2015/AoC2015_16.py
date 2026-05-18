with open('AoC2015_16_data.txt') as file:
    data = file.read()
    
data = data.split('\n')
    
ans = [0,0]

MFCSAM = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}

for line in data:
        name, rest = line.strip().split(': ', 1)
        sue_num = int(name.split()[1])

        properties = {}
        for item in rest.split(', '):
            k, v = item.split(': ')
            properties[k] = int(v)

        if all(MFCSAM[k] == v for k, v in properties.items()):
            ans[0]=sue_num
            
        match = True
        for k, v in properties.items():
            if k in ['pomeranians', 'goldfish']:
                if v >= MFCSAM[k]:
                    match = False
                    break
            elif k in ['cats', 'trees']:
                if v <= MFCSAM[k]:
                    match = False
                    break
            else:
                if v != MFCSAM[k]:
                    match = False
                    break
        
        if match:
            ans[1] = sue_num
print(ans)