with open("AoC2023_15_data.txt", "r") as file:
    data = file.read()

data = data.split(',')
ans1,ans2=0,0
boxes = {}

for instruction in data:
    #part1
    s = 0
    for c in instruction:
        s = (s + ord(c))*17%256
    ans1 += s
    
    #part2
    if '=' in instruction:
        _id,lens = instruction.split('=')
    else:
        _id = instruction[:-1]
    box = 0
    for c in _id:
        box = (box + ord(c))*17%256
    if not instruction.endswith('-'):
        if box in boxes.keys():
            boxes[box][_id]=lens
        else:
            boxes[box] = {_id:lens}
    elif box in boxes.keys() and _id in boxes[box].keys():
        boxes[box].pop(_id)
            
ans2 = sum([sum([(1+box)*(i+1)*int(lens) for i,lens in enumerate(l.values())]) for box,l in boxes.items()])
print(ans1,ans2)